#!/usr/bin/env python3
"""Assemble Story Video #128 — "Their heart is far from me" (Mark 7:6-13).

Row 128 corrected 2026-07-23 (repeat purge 2026-07-20): the folder
build-128-famine-of-hearing held the old Amos "famine of hearing" narration,
which duplicated live #156. It is ARCHIVED (its build.py renamed, not deleted).
This Mark 7 build is the real row-128 story. build.py authored 2026-07-25 to
converge the row: the canonical heart-far transcript + its 7 stills (brought up
from _stale-dupes) render here, the only build-128 dir with a build.py.

Phase-1 STILLS-ONLY (Law E): 7 painted stills, Ken Burns drift, narration,
serif captions (caption-v2 bottom band, chunked + synced — CAPTION LAW), a
SILENT cream closing card. NO AI motion clips, NO music bed (HUM PURGE law):
audio is narration + intentional silence only.

SPEAKER-LAW: who is speaking is declared once in make_narration.py and decides
BOTH the narration voice and the caption colour. Jesus's quoted Isaiah/Mark
lines (j1/j2/j3) are red-letter KJV; the narrator (n1..n5) is white. Beat
durations are derived from the narration audio (LEAD + spoken + gap); the video
ends TAIL seconds after the last spoken word.

STORY-COVERAGE-LAW: 7 stills carry the 7 beats of the PRESCRIPTION.
  s1-the-complaint / s2-the-simple-meal  <- n1 splits mid-segment (the complaint,
      then the cutaway to the disciples' simple meal)
  s3-he-answers                          <- n2
  s4-lips-near-heart-far                 <- j1 + n3 (the Isaiah indictment, the retell)
  s4b-laying-aside-the-commandment       <- j2 ("commandment of God laid aside")
  s5-the-corban-excuse                   <- n4
  s6-he-names-it                         <- j3
  s7-the-honest-heart                    <- n5 (warm hold for the closing card)

Output: mark-7_heart-far-from-me.mp4, 1080x1920 H.264 30fps, <25MB.
"""
import os
import shutil
import subprocess
import textwrap

import make_narration  # SEGMENTS -> verbatim caption text + speaker per segment
from mbm_caption_timing import caption_filter
from mbm_speakers import is_scripture

FF = shutil.which("ffmpeg") or "ffmpeg"
FPROBE = shutil.which("ffprobe") or "ffprobe"
A, S, FPS = "assets", "segs", 30
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
CREAM, INK = "0xF7F2E9", "0x3B2A1E"
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-the-complaint.jpeg"
S2 = "s2-the-simple-meal.jpeg"
S3 = "s3-he-answers.jpeg"
S4 = "s4-lips-near-heart-far.jpeg"
S5 = "s5-the-corban-excuse.jpeg"
S6 = "s6-he-names-it.jpeg"
S4B = "s4b-laying-aside-the-commandment.jpeg"
S7 = "s7-the-honest-heart.jpeg"

TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}

# BEATS: (segment_name, [(image, marker), ...], zoom_dir). The still may be a
# LIST — the picture switches mid-segment at the timestamp where the marker
# words are spoken (STORY-COVERAGE-LAW). The first sub-still's marker is unused.
BEATS = [
    ("n1", [(S1, "in"), (S2, "They had seen his disciples")], "in"),
    ("n2", [(S3, "in")], "in"),
    ("j1", [(S4, "in")], "in"),    # lips near, heart far
    ("n3", [(S4, "out")], "out"),  # same image, the retell
    ("j2", [(S4B, "in")], "in"),   # its own still: commandment of God laid aside
    ("n4", [(S5, "in")], "in"),    # the corban excuse
    ("j3", [(S6, "in")], "in"),    # he names it plainly
    ("n5", [(S7, "in")], "in"),    # the honest heart, warm hold into the card
]

# The closing card is SILENT (heart-far has no card narration): a cream card
# with the reflective question, read in quiet. No card.mp3 exists or is needed.
CARD_TEXT = "Is your heart near him,\nor only your lips?"
CARD_DUR = 5.0

LEAD = 0.28
GAP = 0.65
KJV_GAP = 1.60   # sacred hold after each of Jesus's lines (is_scripture)
# No-dead-air law: the video ends TAIL seconds after the last spoken word.
TAIL = 1.5


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FFMPEG ERROR:\n", r.stderr[-1600:], flush=True)
        raise SystemExit(1)


def dur_of(path):
    out = subprocess.run(
        [FPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(out.stdout.strip())


def spoken_of(path):
    tmp = f"{S}/_spoken.wav"
    run([FF, "-y", "-v", "error", "-i", path, "-af",
         "areverse,silenceremove=start_periods=1:start_threshold=-50dB:"
         "start_duration=0.02,areverse", "-c:a", "pcm_s16le", tmp])
    return dur_of(tmp)


def marker_time(seg_id, marker):
    """Segment-local second at which the marker words are spoken, from the
    narration timing sidecar (STORY-COVERAGE-LAW mid-segment switch)."""
    import json
    import re
    with open(f"audio/{seg_id}.timing.json") as f:
        timing = json.load(f)

    def norm(x):
        return re.sub(r"[^a-z0-9 ]", "", x.lower()).strip()

    mk = norm(marker)
    for s in timing:
        nt = norm(s["text"])
        i = nt.find(mk)
        if i >= 0:
            return s["start"] + (s["end"] - s["start"]) * (i / max(1, len(nt)))
    raise SystemExit(f"STORY-COVERAGE: marker {marker!r} not found in {seg_id}.timing.json")


def _zoompan(zd, frames):
    z = f"1.001+0.09*on/{frames}" if zd == "in" else f"1.091-0.09*on/{frames}"
    return (f"scale=2160:3840:force_original_aspect_ratio=increase,"
            f"crop=2160:3840,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},scale=1080:1920:flags=lanczos")


def build_still(seg_id, src, dur, zdir, spoken_end, cap_text, speaker, first, last):
    cap = caption_filter(seg_id, dur, spoken_end, cap_text, speaker)
    tail = ""
    if first:
        tail = ",fade=t=in:st=0:d=1.2"
    if last:
        tail = f",fade=t=out:st={dur-1.0}:d=1.0"
    # STORY-COVERAGE-LAW: one or more stills inside one narration segment,
    # switching at the timestamps where the words turn. Render each sub-still,
    # concat, then draw the segment's captions over the joined clip.
    cuts = [0.0] + [LEAD + marker_time(seg_id, m) for _s, m in src[1:]] + [dur]
    subs = []
    for i, (img, _m) in enumerate(src):
        d = cuts[i + 1] - cuts[i]
        if d <= 0:
            raise SystemExit(f"STORY-COVERAGE: switch times out of order in {seg_id}")
        zd = zdir if i % 2 == 0 else ("out" if zdir == "in" else "in")
        out = f"{S}/{seg_id}_p{i}.mp4"
        run([FF, "-y", "-loop", "1", "-i", f"{A}/{img}", "-t", f"{d:.3f}",
             "-filter_complex", f"[0:v]{_zoompan(zd, max(1, int(d * FPS)))}[v]",
             "-map", "[v]"] + ENC + [out])
        subs.append(out)
    lst = f"{S}/{seg_id}_parts.txt"
    with open(lst, "w") as f:
        for p in subs:
            f.write(f"file '{os.path.basename(p)}'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", lst,
         "-filter_complex", f"[0:v]null{cap}{tail}[v]",
         "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


# --- MBM box-guard: strip Unicode line/paragraph separators + control chars that
# drawtext renders as tofu boxes at line ends (Cameron complaint 2026-07-23). ---
_MBM_SEP = {0x2028:0x20,0x2029:0x20,0x0085:0x20,0x000b:0x20,0x000c:0x20,0x000d:0x20}
for _c in list(range(0x00,0x09))+list(range(0x0e,0x20))+list(range(0x7f,0xa0)):
    _MBM_SEP[_c]=None
def _mbm_clean(_t):
    return _t.translate(_MBM_SEP)


def build_card(dur, text):
    # AUTO-WRAP CARD LAW (2026-07-21): re-wrap every line to fit 1080px, one
    # textfile per line (a newline never enters a textfile — the tofu bug).
    size = 48
    lh = size + 22
    lines = [w for para in _mbm_clean(text).split("\n")
             for w in (textwrap.wrap(para, width=30) or [""])]
    L = len(lines)
    vf = ""
    for j, ln in enumerate(lines):
        if not ln.strip():
            continue
        tf = f"{S}/card_{j}.txt"
        with open(tf, "w", encoding="utf-8") as f:
            f.write(ln)
        y = f"(h-{L * lh})/2+{j * lh}"
        vf += (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize={size}:"
               f"fontcolor={INK}:x=(w-text_w)/2:y={y},")
    vf += f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8"
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/card.mp4"])


def main():
    os.makedirs(S, exist_ok=True)

    spoken = {n: spoken_of(f"audio/{n}.mp3") for n, _, _ in BEATS}

    timeline, audio_place, start_of = [], [], {}
    t = 0.0
    for name, still, zdir in BEATS:
        speaker = SPEAKER[name]
        gap = KJV_GAP if is_scripture(speaker) else GAP
        vdur = LEAD + spoken[name] + gap
        a_start = t + LEAD
        audio_place.append((f"audio/{name}.mp3", a_start))
        start_of[name] = a_start
        timeline.append((name, still, zdir, vdur, a_start, speaker))
        t += vdur
    # the silent closing card follows the last spoken beat + its TAIL breath
    card_start = t
    total = t + CARD_DUR

    worst, worst_at, prev_end = 0.0, None, None
    for name, _s, _z, _v, a_start, _sp in timeline:
        if prev_end is not None and a_start - prev_end > worst:
            worst, worst_at = a_start - prev_end, name
        prev_end = a_start + spoken[name]
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min); "
          f"sacred holds after j1/j2/j3; silent card {CARD_DUR:.1f}s; "
          f"worst spoken gap {worst:.2f}s before {worst_at}", flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s before {worst_at}")

    n_beats = len(timeline)
    for i, (seg_id, still, zdir, vdur, _a, speaker) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, LEAD + spoken[seg_id],
                    TEXT[seg_id], speaker, first=(i == 0), last=(i == n_beats - 1))
    build_card(CARD_DUR, CARD_TEXT)

    with open(f"{S}/concat.txt", "w", encoding="utf-8") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # HUM PURGE (Cameron, 2026-07-16): NO synthetic music bed, ever.
    # Audio is NARRATION + INTENTIONAL SILENCE only.
    inputs, filters, labels = [], [], []
    for i, (path, start) in enumerate(audio_place):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    m = len(labels)
    filters.append("".join(labels) +
                   f"amix=inputs={m}:duration=longest:normalize=0,"
                   f"apad=whole_dur={total:.2f}[aout]")
    run([FF, "-y"] + inputs + ["-filter_complex", ";".join(filters),
        "-map", "[aout]", "-t", f"{total:.2f}", "-c:a", "aac", "-b:a", "160k",
        f"{S}/audio_mix.m4a"])

    probe = subprocess.run(
        [FF, "-i", f"{S}/audio_mix.m4a", "-af", "ebur128", "-f", "null", "-"],
        capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            try:
                lufs = float(line.split()[1])
            except ValueError:
                pass
    gain = max(-6.0, min(16.0, -15.0 - lufs)) if lufs is not None else 0.0
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    OUT = "mark-7_heart-far-from-me.mp4"
    A_KBPS, MUX = 96, 20
    vcap = min(2200, max(500, int(24.0 * 8000 / total) - A_KBPS - MUX))
    size, crf = 0.0, 20
    for crf in (20, 21, 22, 23, 24):
        run([FF, "-y", "-i", f"{S}/video_silent.mp4",
             "-i", f"{S}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
             "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", f"{A_KBPS}k", "-movflags", "+faststart", OUT])
        size = os.path.getsize(OUT) / 1e6
        if size <= 24.3:
            break
        print(f"  {size:.1f} MB at crf {crf} — over, stepping up", flush=True)
    print(f"DONE: {OUT}  {size:.1f} MB, {total:.1f}s (crf {crf}, vcap {vcap}k)",
          flush=True)


if __name__ == "__main__":
    main()
