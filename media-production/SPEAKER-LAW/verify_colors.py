#!/usr/bin/env python3
"""Confirm each rebuilt video actually PAINTS the speaker colours it declares.

The existing gates catch a corrupt file or dead air, but nothing checks the thing
the whole pass exists for. If a plan's SPEAKER map silently failed to reach
caption_filter, every caption would render white, the video would decode clean,
end 1.5s after the last word, and sail through verification looking perfect.

So: compute when each non-narrator beat is on screen, pull that frame, and look
for its colour in the caption band. Reports any build whose declared colours do
not appear.
"""
import json
import os
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
MP = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import migrate  # noqa: E402

TARGET = {                       # speaker -> (r, g, b) of its caption
    "jesus":     (0xEE, 0x33, 0x22),
    "god":       (0x5B, 0xE3, 0x8B),
    "scripture": (0x8F, 0xDC, 0xFF),
    "woman":     (0xFF, 0x9E, 0xC7),
}
DEFAULTS = (0.28, 0.65, 1.60)


def timing_constants(build_dir):
    """LEAD/GAP/KJV_GAP as THIS build defines them.

    They are not uniform across the library — build-149 uses different values, and
    assuming the defaults put every probe several seconds early, which reported a
    perfectly good blue caption as missing. Read them, never assume them.
    """
    import re
    src = open(os.path.join(build_dir, "build.py"), encoding="utf-8",
               errors="replace").read()
    out = []
    for name, dflt in zip(("LEAD", "GAP", "KJV_GAP"), DEFAULTS):
        m = re.search(rf"^{name} = ([0-9.]+)", src, re.M)
        out.append(float(m.group(1)) if m else dflt)
    return out


def _dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", p], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None


def spoken_of(mp3):
    if not os.path.exists(mp3):
        return None
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", mp3, "-af",
                    "areverse,silenceremove=start_periods=1:start_threshold=-50dB:"
                    "start_duration=0.02,areverse", "-c:a", "pcm_s16le",
                    "/tmp/_vc.wav"], capture_output=True)
    return _dur("/tmp/_vc.wav")


def close(px, target, tol=48):
    return all(abs(a - b) <= tol for a, b in zip(px, target))


def frame_has(path, speaker):
    """Is this speaker's colour present in the caption band of this frame?"""
    from PIL import Image
    im = Image.open(path).convert("RGB")
    w, h = im.size
    band = im.crop((0, int(h * 0.80), w, h)).resize((w // 4, int(h * 0.20) // 4))
    tgt = TARGET[speaker]
    hits = sum(1 for px in band.getdata() if close(px, tgt))
    return hits >= 12, hits


def check(build):
    d = os.path.join(MP, build)
    plan_p = os.path.join(HERE, "plans", f"{build}.json")
    if not os.path.exists(plan_p):
        return None
    plan = json.load(open(plan_p))
    spk = {s["id"]: s["speaker"] for s in plan["segments"]}
    name = migrate.output_mp4(d)
    if not name:
        return {"build": build, "error": "no output mp4"}
    mp4 = os.path.join(d, name)

    LEAD, GAP, KJV_GAP = timing_constants(d)
    t, probes = 0.0, []
    for beat in plan.get("beats", []):
        sid = beat[0]
        s = spoken_of(os.path.join(d, "audio", f"{sid}.mp3"))
        if s is None:
            continue
        sp = spk.get(sid, "narrator")
        if sp != "narrator":
            # sample across the beat: a long line is split into caption chunks and
            # any single instant can land between two of them
            for frac in (0.3, 0.55, 0.8):
                probes.append((sid, sp, t + LEAD + s * frac))
        t += LEAD + s + (KJV_GAP if sp != "narrator" else GAP)

    # count each BEAT once, not each of its three probe instants
    want = Counter(sp for _sid, sp in {(s, p) for s, p, _ in probes})
    found, missing = Counter(), []
    for sid, sp, ts in probes:
        f = f"/tmp/_vc_{build}_{sid}.png"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{ts:.2f}",
                        "-i", mp4, "-frames:v", "1", f], capture_output=True)
        if not os.path.exists(f):
            continue
        ok, hits = frame_has(f, sp)
        if ok:
            found[sp] += 1
        else:
            missing.append((sid, sp, round(ts, 1), hits))
        os.remove(f)
    return {"build": build, "declared": dict(want), "found": dict(found),
            "missing": missing}


def main():
    names = sys.argv[1:]
    if not names:
        d = json.load(open(os.path.join(HERE, "batch-log.json")))
        names = sorted(k for k, v in d.items() if v.get("status") == "shipped")
    bad = 0
    for b in names:
        r = check(b)
        if not r:
            continue
        if r.get("error"):
            print(f"{b}: {r['error']}")
            bad += 1
            continue
        # a beat can be missed because its caption chunk had already advanced;
        # only flag a build where a whole declared SPEAKER never appears at all
        never = [sp for sp in r["declared"] if sp not in r["found"]]
        if never:
            bad += 1
            print(f"\n{b}: declared {r['declared']} but NEVER painted {never}")
            for sid, sp, ts, hits in r["missing"][:4]:
                print(f"    {sid} [{sp}] @{ts}s  hits={hits}")
        else:
            part = f"  ({len(r['missing'])} beat(s) not caught mid-chunk)" \
                   if r["missing"] else ""
            print(f"{b}: ok {r['found']}{part}")
    print(f"\n{len(names) - bad}/{len(names)} builds paint every declared colour")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
