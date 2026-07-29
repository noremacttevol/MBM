#!/usr/bin/env python3
"""Assemble the V2 cut of Story Video #1 — The Woman Who Touched His Cloak (Mark 5:25-34).

V2 PICTURE REBUILD. The narration audio, the segment timing and the caption text are
the finished V1 assets, copied in and untouched — only the pictures are new. Every
constant below is read from THAT build's V1 build.py (LEAD/GAP/KJV_GAP/TAIL vary per
build and are never carried over from another one).

Structure follows build-10-well's build.py, which is the STORY-COVERAGE-LAW-capable
version: a BEATS row may list SEVERAL stills for one narration segment, switching at
the timestamp where the marker words are actually spoken (`marker_time`, read from
the edge-tts sentence sidecars). That is what lets 20 pictures hang on 13 segments.

Captions are burned in, so they re-render with the new stills — caption law unchanged:
bottom band only, chunked in sync with the narration, never over the art.
NO music bed: narration and intentional silence only (PRODUCTION-BIBLE §5b).

Output: mark-5_woman-touches-his-cloak.mp4, 1080x1920 H.264 30fps, <25MB.
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

S01 = "s01-twelve-years.jpeg"
S02 = "s02-physicians.jpeg"
S03 = "s03-untouchable.jpeg"
S04 = "s04-jairus-urging.jpeg"
S05 = "s05-crowd-pressing.jpeg"
S06 = "s06-woman-at-edge.jpeg"
S07 = "s07-she-hears.jpeg"
S08 = "s08-she-says-it.jpeg"
S09 = "s09-her-plan.jpeg"
S10 = "s10-pressing-through.jpeg"
S11 = "s11-touches-hem.jpeg"
S12 = "s12-he-stops.jpeg"
S13 = "s13-healed-in-her-body.jpeg"
S14 = "s14-who-touched.jpeg"
S15 = "s15-disciples-protest.jpeg"
S16 = "s16-searching.jpeg"
S17 = "s17-found-her.jpeg"
S18 = "s18-daughter.jpeg"
S19 = "s19-it-lands.jpeg"
S20 = "s20-goes-in-peace.jpeg"

TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}

# (segment, [(still, zoom-dir-or-marker-words), ...], zoom-dir)
# The FIRST pair carries the zoom direction; every later pair carries the MARKER
# WORDS at which the picture switches inside that segment.
BEATS = [
    ("n1",  [(S01, "in")], "in"),
    ("n2",  [(S02, "in"), (S03, "she was exhausted")], "in"),
    ("n2b", [(S04, "in"), (S05, "the crowd pressed"),
             (S06, "almost no one")], "in"),
    ("n3a", [(S07, "in")], "in"),
    ("w28", [(S08, "out")], "out"),
    ("n3b", [(S09, "in"), (S10, "she pressed through the crowd"),
             (S11, "and reached out to touch")], "in"),
    ("n4a", [(S12, "in"), (S13, "the healing was already hers")], "in"),
    ("j0",  [(S14, "out")], "out"),
    ("s31", [(S15, "in")], "in"),
    ("n4c", [(S15, "out"), (S16, "he ignored them")], "out"),
    ("n4b", [(S17, "in")], "in"),
    ("j1",  [(S18, "in")], "in"),
    ("n5",  [(S19, "in"), (S20, "over in a sentence")], "in"),
]

# Constants read from the V1 build-01-cloak/build.py — this build's own values.
LEAD = 0.28
GAP = 0.72
KJV_GAP = 1.30
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
    # Several stills inside one narration segment: render each, concat, then draw
    # the segment's captions over the joined clip so caption timing is untouched.
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
# drawtext renders as tofu boxes at line ends. ---
_MBM_SEP = {0x2028: 0x20, 0x2029: 0x20, 0x0085: 0x20, 0x000b: 0x20,
            0x000c: 0x20, 0x000d: 0x20}
for _c in list(range(0x00, 0x09)) + list(range(0x0e, 0x20)) + list(range(0x7f, 0xa0)):
    _MBM_SEP[_c] = None


def _mbm_clean(_t):
    return _t.translate(_MBM_SEP)


def build_card(dur, text):
    # AUTO-WRAP CARD LAW: never trust the line breaks the narration text carries.
    # Every paragraph is re-wrapped to fit 1080px and each line gets its OWN
    # textfile + drawtext (a newline inside a textfile is the tofu bug).
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
    card_dur = dur_of("audio/card.mp3")

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
    audio_place.append(("audio/card.mp3", card_start + LEAD))
    total = t + card_vdur

    # no-dead-air check
    worst, worst_at, prev_end = 0.0, None, None
    for name, _s, _z, _v, a_start, _sp in timeline:
        if prev_end is not None and a_start - prev_end > worst:
            worst, worst_at = a_start - prev_end, name
        prev_end = a_start + spoken[name]
    stills = sum(len(src) for _n, src, _z in BEATS)
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min); {stills} stills over "
          f"{len(BEATS)} segments; worst spoken gap {worst:.2f}s before {worst_at}",
          flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s before {worst_at}")

    n = len(timeline)
    for i, (seg_id, src, zdir, vdur, _a, speaker) in enumerate(timeline):
        build_still(seg_id, src, vdur, zdir, LEAD + spoken[seg_id],
                    TEXT[seg_id], speaker, first=(i == 0), last=(i == n - 1))
    build_card(card_vdur, TEXT["card"])

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

    OUT = "mark-5_woman-touches-his-cloak.mp4"
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
