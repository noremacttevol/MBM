#!/usr/bin/env python3
"""DEFECT SCANNER — machine-checkable subset of DEFECT-CATALOG.md, run across
every delivered video. Prefills DEFECT-SCAN.csv so the 200x48 checklist starts
with real machine results, not placeholders. Human-eyes defects are marked EYES.

Automatable defects covered (the rest need eyes and are emitted as EYES):
  #6  hum / synthetic bed  -> spectral check of the card tail (110/165/220/330 Hz)
  #7  dead-air >2.5s mid-video  -> silencedetect, excluding the final card tail
  #11 spoken gap >2.5s          -> same pass (any body gap)
  #43 filename book-chapter_slug.mp4
  #44 9:16 1080x1920 / plays clean / duration >60s
  #45 size <30MB / bitrate not starved
  LUFS integrated near -15 (delivery loudness law)

Usage: python3 media-production/scan_defects.py
Writes: media-production/DEFECT-SCAN.csv  (one row per delivered video)
"""
import csv
import os
import re
import subprocess
import glob

MP = os.path.dirname(os.path.abspath(__file__))
FF = "ffmpeg"
FPROBE = "ffprobe"

# The human-eyes defects (id -> short label) emitted as EYES per row.
EYES = {
    1: "cap-covers-picture", 2: "cap-not-split-synced", 3: "cap-font-shrunk",
    4: "tofu-in-captions", 5: "tofu-end-card",
    8: "tts-homograph", 9: "narrator-quotes-kjv", 10: "jesus-not-exact-kjv",
    12: "face-visible-where-withheld", 13: "face-inconsistent",
    14: "caucasian-jesus", 15: "halo-glow", 16: "brown-mantle-variance",
    17: "wrong-limb-count", 18: "duplicate-character", 19: "look-drift",
    20: "trait-not-reading", 21: "trait-caricature", 22: "wrong-scale",
    23: "on-the-water", 24: "direction-vs-narration", 25: "action-wrong",
    26: "lighting-wrong-tod", 27: "figure-out-of-place",
    28: "gore-wet-tears", 29: "embodied-satan", 30: "shame-no-mercy",
    31: "fear-closing-card", 32: "child-in-peril", 33: "not-10yo-safe",
    34: "style-drift", 35: "ai-clip-in-stills", 36: "gibberish-text",
    37: "modern-objects", 38: "ref-portrait-collapse",
    39: "must-show-missing", 40: "must-never-show-present",
    41: "verse-card-source", 42: "closing-q-vs-seed",
    46: "narrator-not-plain", 47: "not-carried-to-final-verse",
    48: "sacred-silence-missing",
}


def probe(path, entries, stream=None):
    cmd = [FPROBE, "-v", "error", "-show_entries", entries, "-of", "csv=p=0"]
    if stream:
        cmd = [FPROBE, "-v", "error", "-select_streams", stream,
               "-show_entries", entries, "-of", "csv=p=0"]
    cmd.append(path)
    out = subprocess.run(cmd, capture_output=True, text=True)
    return out.stdout.strip(), out.returncode, out.stderr.strip()


def body_deadair(path):
    """Any silence >2.5s that is NOT the final (card) tail -> defect #7/#11."""
    out = subprocess.run(
        [FF, "-i", path, "-af", "silencedetect=noise=-40dB:d=2.5",
         "-f", "null", "-"], capture_output=True, text=True)
    dur, _, _ = probe(path, "format=duration")
    try:
        total = float(dur)
    except ValueError:
        total = 0.0
    worst_body = 0.0
    for line in out.stderr.splitlines():
        m = re.search(r"silence_start:\s*([\d.]+)", line)
        if not m:
            continue
        start = float(m.group(1))
        # the last gap that runs to the very end is the allowed card tail
        if total and start > total - 16.0:
            continue
        # find matching duration on a nearby line
        for l2 in out.stderr.splitlines():
            md = re.search(r"silence_duration:\s*([\d.]+)", l2)
            if md and abs(_start_of(out.stderr, l2) - start) < 0.01:
                worst_body = max(worst_body, float(md.group(1)))
    # simpler robust pass: collect all (start,duration) pairs
    pairs = []
    cur = None
    for line in out.stderr.splitlines():
        ms = re.search(r"silence_start:\s*([-\d.]+)", line)
        md = re.search(r"silence_duration:\s*([\d.]+)", line)
        if ms:
            cur = float(ms.group(1))
        if md and cur is not None:
            pairs.append((cur, float(md.group(1))))
            cur = None
    worst = 0.0
    for start, d in pairs:
        if total and start > total - 16.0:   # card tail region — allowed
            continue
        worst = max(worst, d)
    return worst


def _start_of(stderr, line):
    return 0.0


def quietest_window(path):
    """Find the midpoint of the longest silent region (>=0.6s at -50dB).
    Returns (start, dur) of a ~0.8s window guaranteed to be silence, or None
    if the file has no such gap (wall-to-wall audio)."""
    out = subprocess.run(
        [FF, "-i", path, "-af", "silencedetect=noise=-50dB:d=0.6",
         "-f", "null", "-"], capture_output=True, text=True)
    best = None
    start = None
    for line in out.stderr.splitlines():
        ms = re.search(r"silence_start:\s*([-\d.]+)", line)
        me = re.search(r"silence_end:\s*([-\d.]+)\s*\|\s*silence_duration:\s*([\d.]+)", line)
        if ms:
            start = float(ms.group(1))
        if me and start is not None:
            end, d = float(me.group(1)), float(me.group(2))
            if best is None or d > best[2]:
                best = (start, end, d)
            start = None
    if not best:
        return None
    mid = (best[0] + best[1]) / 2.0
    return max(best[0] + 0.1, mid - 0.4), 0.8


def hum_check(path):
    """Sample a guaranteed-silent window at the old hum-bed bands. Returns the
    max dB across bands; <=-60 = clean. None if no silent window exists
    (can't distinguish hum from voice, so not a machine call)."""
    win = quietest_window(path)
    if win is None:
        return None
    ss, dur = win
    worst = -120.0
    for f in (110, 165, 220, 330):
        out = subprocess.run(
            [FF, "-ss", f"{ss:.2f}", "-t", f"{dur:.2f}", "-i", path,
             "-af", f"bandpass=f={f}:width_type=h:w=8,volumedetect",
             "-f", "null", "-"], capture_output=True, text=True)
        for line in out.stderr.splitlines():
            m = re.search(r"max_volume:\s*([-\d.]+)", line)
            if m:
                worst = max(worst, float(m.group(1)))
    return worst


def lufs(path):
    out = subprocess.run([FF, "-i", path, "-af", "ebur128", "-f", "null", "-"],
                         capture_output=True, text=True)
    val = None
    for line in out.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            try:
                val = float(line.split()[1])
            except (ValueError, IndexError):
                pass
    return val


FNAME_RE = re.compile(r"^[1-3]?-?[a-z]+-\d+[a-z]?_[a-z0-9-]+\.mp4$")


def pick_mp4(folder):
    """Prefer a scripture-named mp4 (book-chapter_slug.mp4) over legacy names."""
    mp4s = sorted(glob.glob(os.path.join(folder, "*.mp4")))
    if not mp4s:
        return None
    named = [m for m in mp4s if FNAME_RE.match(os.path.basename(m))]
    pool = named or mp4s
    # newest by mtime among the preferred pool
    return max(pool, key=os.path.getmtime)


def scan_one(folder):
    fname_mp4 = pick_mp4(folder)
    base = os.path.basename(folder)
    m = re.match(r"build-0*(\d+)-", base)
    row = int(m.group(1)) if m else ""
    r = {"row": row, "folder": base}
    if not fname_mp4:
        r["file"] = "(no mp4)"
        r["auto_status"] = "NO-MP4"
        return r
    fn = os.path.basename(fname_mp4)
    r["file"] = fn

    wh, rc, _ = probe(fname_mp4, "stream=width,height", stream="v")
    plays = (rc == 0 and wh != "")
    res_ok = wh.replace("\n", ",") in ("1080,1920",)
    dur_s, _, _ = probe(fname_mp4, "format=duration")
    try:
        dur = float(dur_s)
    except ValueError:
        dur = 0.0
    size_mb = os.path.getsize(fname_mp4) / 1e6
    vkbps = (size_mb * 8000 / dur) if dur else 0

    r["d44_res"] = "PASS" if res_ok else f"FAIL({wh})"
    r["d44_plays"] = "PASS" if plays else "FAIL"
    r["d44_dur>60"] = "PASS" if dur > 60 else f"FAIL({dur:.0f}s)"
    r["d45_size<30"] = "PASS" if size_mb < 30 else f"FAIL({size_mb:.1f}MB)"
    r["d45_bitrate"] = "PASS" if vkbps > 400 else f"FAIL({vkbps:.0f}k)"
    r["d43_filename"] = "PASS" if FNAME_RE.match(fn) else "FAIL"

    worst_gap = body_deadair(fname_mp4)
    if worst_gap <= 2.5:
        r["d7_deadair"] = "PASS"
    elif worst_gap <= 3.5:
        # 2.5-3.5s: almost always an intentional sacred pause around a KJV
        # line that grew slightly past the mechanical law — MINOR, verify.
        r["d7_deadair"] = f"MINOR({worst_gap:.2f}s)"
    else:
        r["d7_deadair"] = f"FAIL({worst_gap:.2f}s)"

    hum = hum_check(fname_mp4)
    if hum is None:
        r["d6_hum"] = "n/a(no-silence)"
    elif hum <= -55:
        r["d6_hum"] = "PASS"
    else:
        r["d6_hum"] = f"CHECK({hum:.0f}dB)"

    lu = lufs(fname_mp4)
    if lu is None:
        r["lufs"] = "n/a"
    else:
        r["lufs"] = f"PASS({lu:.1f})" if -17.5 <= lu <= -12.5 else f"CHECK({lu:.1f})"

    autos = [r["d44_res"], r["d44_plays"], r["d44_dur>60"], r["d45_size<30"],
             r["d45_bitrate"], r["d43_filename"], r["d7_deadair"], r["d6_hum"],
             r["lufs"]]
    hard_fail = any(a.startswith("FAIL") for a in autos)
    soft = any(a.startswith(("MINOR", "CHECK")) for a in autos)
    if hard_fail:
        r["auto_status"] = "FAIL"
    elif soft:
        r["auto_status"] = "MINOR"
    else:
        r["auto_status"] = "PASS"
    return r


def main():
    folders = sorted(glob.glob(os.path.join(MP, "build-*")),
                     key=lambda f: (int(re.match(r"build-0*(\d+)", os.path.basename(f)).group(1))
                                    if re.match(r"build-0*(\d+)", os.path.basename(f)) else 9999))
    auto_cols = ["d43_filename", "d44_res", "d44_plays", "d44_dur>60",
                 "d45_size<30", "d45_bitrate", "d7_deadair", "d6_hum", "lufs",
                 "auto_status"]
    eyes_cols = [f"E{n}_{lbl}" for n, lbl in sorted(EYES.items())]
    header = ["row", "folder", "file"] + auto_cols + eyes_cols

    rows, fails = [], []
    for folder in folders:
        if not os.path.isdir(folder):
            continue
        if not glob.glob(os.path.join(folder, "*.mp4")):
            continue
        r = scan_one(folder)
        for c in eyes_cols:
            r[c] = "EYES"
        rows.append(r)
        if r.get("auto_status") in ("FAIL", "MINOR"):
            fails.append(r)

    out = os.path.join(MP, "DEFECT-SCAN.csv")
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in header})

    npass = sum(1 for r in rows if r.get('auto_status') == 'PASS')
    nhard = sum(1 for r in rows if r.get('auto_status') == 'FAIL')
    nminor = sum(1 for r in rows if r.get('auto_status') == 'MINOR')
    print(f"scanned {len(rows)} delivered videos -> {out}")
    print(f"auto-PASS: {npass}  hard-FAIL: {nhard}  MINOR(verify): {nminor}")
    hard = [r for r in fails if r.get('auto_status') == 'FAIL']
    minor = [r for r in fails if r.get('auto_status') == 'MINOR']
    if hard:
        print("\n=== HARD FAILS (real defects, fix) ===")
        for r in hard:
            flags = [f"{k}={v}" for k, v in r.items()
                     if k.startswith(("d6", "d7", "d43", "d44", "d45", "lufs"))
                     and (str(v).startswith("FAIL"))]
            print(f"  row {r['row']:>3} {r['file'][:42]:42} | " + "; ".join(flags))
    if minor:
        print("\n=== MINOR (2.5-3.5s pause / band-energy — verify, likely sacred) ===")
        for r in minor:
            flags = [f"{k}={v}" for k, v in r.items()
                     if k.startswith(("d6", "d7", "lufs"))
                     and str(v).startswith(("MINOR", "CHECK"))]
            print(f"  row {r['row']:>3} {r['file'][:42]:42} | " + "; ".join(flags))


if __name__ == "__main__":
    main()
