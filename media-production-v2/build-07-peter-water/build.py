#!/usr/bin/env python3
"""Assemble the V2 cut of Story Video #2 — The Prodigal Son (Luke 15:11-32).

V2 PICTURE REBUILD. The narration audio, the segment timing and the caption text
are the finished V1 assets, copied in and untouched — only the pictures are new.
Constants are THIS build's own values, read from the V1 build-02 build.py
(GAP 0.65 and KJV_GAP 1.60 differ from build-01 — never carried over).

Same STORY-COVERAGE-capable structure as the row-1 V2 assembler: a BEATS row may
list several stills for one narration segment, switching at the timestamp where
the marker words are actually spoken. 24 stills over 18 segments (V1 had 10).

Captions burn in over the new stills; caption law unchanged (bottom band only,
chunked in sync). NO music bed — narration and intentional silence only.

Output: matthew-14_peter-walks-on-water.mp4, 1080x1920 H.264 30fps, <25MB.
"""
import json
import os
import re
import subprocess
import textwrap

import make_narration
from mbm_caption_timing import caption_filter
from mbm_speakers import is_scripture

A = "assets"
S = "segs"
FPS = 30
FF = "ffmpeg"
FPROBE = "ffprobe"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S01 = "s01-he-sent-them-ahead.jpeg"
S02 = "s02-alone-up-the-hill.jpeg"
S03 = "s03-talking-with-his-father.jpeg"
S04 = "s04-the-wind-was-contrary.jpeg"
S05 = "s05-the-fourth-watch.jpeg"
S06 = "s06-something-out-there.jpeg"
S07 = "s07-on-top-of-the-water.jpeg"
S08 = "s08-they-cried-out.jpeg"
S09 = "s09-a-voice-they-knew.jpeg"
S10 = "s10-be-not-afraid.jpeg"
S11 = "s11-what-peter-wanted.jpeg"
S12 = "s12-bid-me-come.jpeg"
S13 = "s13-come.jpeg"
S14 = "s14-leg-over-the-side.jpeg"
S15 = "s15-stood-up-on-the-sea.jpeg"
S16 = "s16-step-after-step.jpeg"
S17 = "s17-where-only-god-can-walk.jpeg"
S18 = "s18-the-wind-tearing-at-him.jpeg"
S19 = "s19-he-looked-down.jpeg"
S20 = "s20-the-water-stopped-holding.jpeg"
S21 = "s21-down-to-his-waist.jpeg"
S22 = "s22-lord-save-me.jpeg"
S23 = "s23-and-jesus-caught-him.jpeg"
S24 = "s24-there-was-no-pause.jpeg"
S25 = "s25-holding-him-above-it.jpeg"
S26 = "s26-wherefore-didst-thou-doubt.jpeg"
S27 = "s27-not-from-the-shore.jpeg"
S28 = "s28-you-were-doing-it.jpeg"
S29 = "s29-back-to-the-boat-together.jpeg"
S30 = "s30-they-climbed-in.jpeg"
S31 = "s31-not-slowly.jpeg"
S32 = "s32-flat-under-the-stars.jpeg"
S33 = "s33-soaked-and-shaking.jpeg"
S34 = "s34-they-worshipped-him.jpeg"
S35 = "s35-thou-art-the-son-of-god.jpeg"
S36 = "s36-the-storm-taught-them.jpeg"
S37 = "s37-that-he-walked-and-was-caught.jpeg"

TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}

# (segment, [(still, zoom-dir-or-marker-words), ...], zoom-dir). The first pair
# carries the zoom direction; later pairs carry the MARKER WORDS at which the
# picture switches inside that segment (matched against the timing sidecar).
BEATS = [
    ("n0", [(S01, "in"), (S02, "He sent the crowds home."), (S03, "That is where the night")], "in"),
    ("n1", [(S04, "in"), (S05, "Matthew tells us it was")], "in"),
    ("n2", [(S06, "in"), (S07, "On top of the water."), (S08, "They cried out that it"), (S09, "But the voice that came")], "in"),
    ("j1", [(S10, "in")], "in"),
    ("n3", [(S11, "in")], "in"),
    ("s28", [(S12, "in")], "in"),
    ("j2", [(S13, "in")], "in"),
    ("n4", [(S14, "in"), (S15, "that pitching boat, and stood")], "in"),
    ("n4b", [(S16, "in"), (S17, "For a moment, an ordinary")], "in"),
    ("n5", [(S18, "in"), (S19, "He looked down at the")], "in"),
    ("n5b", [(S20, "in"), (S21, "He dropped to his waist,")], "in"),
    ("s30", [(S22, "in")], "in"),
    ("n6", [(S23, "in")], "in"),
    ("n7", [(S24, "in"), (S25, "And from that grip \u2014")], "in"),
    ("j3", [(S26, "in")], "in"),
    ("n8", [(S27, "in"), (S28, "It's a real question, from")], "in"),
    ("n9", [(S29, "in"), (S30, "And the moment they climbed")], "in"),
    ("n9b", [(S31, "in"), (S32, "The sea that had fought")], "in"),
    ("n10", [(S33, "in"), (S34, "he was a ghost \u2014")], "in"),
    ("s33", [(S35, "in")], "in"),
    ("n10b", [(S36, "in"), (S37, "Not that he sank.")], "in"),
]

# The closing question card is narrated by n8 in this build (V1: CARD = "n8").
CARD = "n11"

# Constants read from the V1 build-02-prodigal/build.py — this build's own values.
LEAD = 0.28
GAP = 0.65
KJV_GAP = 1.60
TAIL = 1.5


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:130], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


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
    sentence timing sidecar (STORY-COVERAGE-LAW mid-segment switch)."""
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
    if zd == "in":
        z = f"1.001+0.10*on/{frames}"
    else:
        z = f"1.101-0.10*on/{frames}"
    # Anti-shimmer law: supersample 4320x7680 -> zoompan at 2160x3840 ->
    # lanczos down to 1080x1920 so every zoom step lands on a quarter-pixel.
    return (f"scale=4320:7680,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")


def build_still(seg_id, src, dur, zdir, spoken_end, cap_text, speaker, first, last):
    tail = ""
    if first:
        tail = ",fade=t=in:st=0:d=1.2"
    if last:
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    cap = caption_filter(seg_id, dur, spoken_end, cap_text, speaker)
    if len(src) == 1:
        img = src[0][0]
        fc = f"[0:v]{_zoompan(zdir, int(dur * FPS))}{cap}{tail}[v]"
        run([FF, "-y", "-loop", "1", "-i", f"{A}/{img}", "-t", str(dur),
             "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])
        return
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


# --- MBM box-guard: strip Unicode separators/control chars that drawtext
# renders as tofu boxes at line ends. ---
_MBM_SEP = {0x2028: 0x20, 0x2029: 0x20, 0x0085: 0x20, 0x000b: 0x20,
            0x000c: 0x20, 0x000d: 0x20}
for _c in list(range(0x00, 0x09)) + list(range(0x0e, 0x20)) + list(range(0x7f, 0xa0)):
    _MBM_SEP[_c] = None


def _mbm_clean(_t):
    return _t.translate(_MBM_SEP)


def build_card(dur, text):
    # AUTO-WRAP CARD LAW: re-wrap every paragraph; one textfile + drawtext per
    # line (a newline inside a textfile is the tofu bug).
    size = 50
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

    missing = [img for _s, src, _z in BEATS for img, _m in src
               if not os.path.exists(f"{A}/{img}")]
    if missing:
        raise SystemExit("missing stills: " + ", ".join(sorted(set(missing))))

    spoken = {n: spoken_of(f"audio/{n}.mp3") for n, _, _ in BEATS}
    card_dur = dur_of(f"audio/{CARD}.mp3")

    timeline = []
    t = 0.0
    audio_place = []
    for name, src, zdir in BEATS:
        speaker = SPEAKER[name]
        gap = KJV_GAP if is_scripture(speaker) else GAP
        vdur = LEAD + spoken[name] + gap
        a_start = t + LEAD
        audio_place.append((f"audio/{name}.mp3", a_start))
        timeline.append((name, src, zdir, vdur, a_start, speaker))
        t += vdur
    card_vdur = LEAD + card_dur + TAIL
    card_start = t
    audio_place.append((f"audio/{CARD}.mp3", card_start + LEAD))
    total = t + card_vdur

    # no-dead-air check
    worst, worst_at, prev_end = 0.0, None, None
    for name, _s, _z, _v, a_start, _sp in timeline:
        if prev_end is not None and a_start - prev_end > worst:
            worst, worst_at = a_start - prev_end, name
        prev_end = a_start + spoken[name]
    stills = sum(len(src) for _n, src, _z in BEATS)
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min); {stills} still-slots "
          f"over {len(BEATS)} segments; worst spoken gap {worst:.2f}s before {worst_at}",
          flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s before {worst_at}")

    n = len(timeline)
    for i, (seg_id, src, zdir, vdur, _a, speaker) in enumerate(timeline):
        build_still(seg_id, src, vdur, zdir, LEAD + spoken[seg_id],
                    TEXT[seg_id], speaker, first=(i == 0), last=(i == n - 1))
    build_card(card_vdur, TEXT[CARD])

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # NO music bed — narration and intentional silence only.
    inputs, filters, labels = [], [], []
    for i, (path, start) in enumerate(audio_place):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    filters.append("".join(labels) +
                   f"amix=inputs={len(labels)}:duration=longest:normalize=0,"
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
            lufs = float(line.split()[1])
    gain = max(-6.0, min(16.0, -15.0 - lufs)) if lufs is not None else 0.0
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    OUT = "matthew-14_peter-walks-on-water.mp4"
    A_KBPS, MUX = 96, 20
    vcap = max(500, int(24.0 * 8000 / total) - A_KBPS - MUX)
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
