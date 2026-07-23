#!/usr/bin/env python3
"""Assemble Story Video #8 — The Lost Coin (Luke 15:8-10).
Hybrid storybook format per PRODUCTION-BIBLE.md: painted stills with Ken Burns
drift, narration (edge-tts), serif captions, closing question card on
cream #F7F2E9.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Converted from the old
template B: the 7-tuple SEGMENTS with hardcoded durations and a per-beat
`caption_style` is gone. Who is speaking is declared ONCE in make_narration.py and
decides BOTH the narration voice and the caption colour. Beat durations are derived
from the narration audio (LEAD + spoken + gap), never hand-set, and the video ends
TAIL seconds after the last spoken word.

Luke 15:8-10 is a parable, so a red-letter KJV inks the whole thing — including the
woman's own line inside it and Jesus's frame around her. j1 and j2 stay red, and two
more verses of the same parable that the video only paraphrased are lifted out and
join them in red: jv8 (Luke 15:8) and jv9a (Luke 15:9a). The woman in the parable is
NOT a `woman` beat — she is a character Jesus invented inside a story he is telling.

The card was silent text on cream; it is now narrated like every other build in the
library, so TAIL can be derived from it.

The caption look, the Ken Burns maths, the audio mix (narration and silence only —
this build has never carried a music bed) and the size ladder are unchanged.

All six visual assets approved by Leighton (QC'd for character lock, wardrobe
lock, nine coins, lamp continuity, visible coin) on 2026-07-08.
Output: 1080x1920 H.264, <25MB.
"""
import os
import textwrap
import shutil
import subprocess

import make_narration  # SEGMENTS -> verbatim caption text + speaker per segment
from mbm_caption_timing import caption_filter
from mbm_speakers import is_scripture

FF = shutil.which("ffmpeg") or "ffmpeg"
FPROBE = shutil.which("ffprobe") or "ffprobe"
A = "assets"
S = "segs"
FPS = 30
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BI = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "18",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

STILL_COUNT = "count.jpeg"
STILL_SWEEP = "lamp.jpeg"   # "She lights a lamp / sweeps" beat (caption-matched to build_win.py)
STILL_KNEEL = "sweep.jpeg"  # "She searches carefully" beat (caption-matched to build_win.py)
STILL_FOUND = "found.jpeg"  # stills-only (Law E): the former Veo "found flash" clip is now a still
STILL_DOOR = "door.jpeg"
STILL_STARS = "stars.jpeg"

TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}

# BEATS: (segment_name, still, zoom_dir). Zoom alternates in/out on a shared still.
BEATS = [
    ("n0", STILL_STARS, "out"),
    ("jv8", STILL_COUNT, "in"),
    ("n1", STILL_COUNT, "out"),
    ("n2a", STILL_SWEEP, "in"),
    ("n2b", STILL_KNEEL, "in"),
    ("jv9a", STILL_FOUND, "in"),
    ("j1", STILL_DOOR, "in"),
    ("n3", STILL_DOOR, "out"),
    ("n4", STILL_STARS, "in"),
    ("j2", STILL_STARS, "out"),
    ("n5", STILL_STARS, "in"),
]

# The closing card is narrated but is not a beat — build_card places it itself.
CARD = "card"
# PEAK: the first non-narrator line — Jesus opening the parable (Luke 15:8).
PEAK = "jv8"

LEAD = 0.28
GAP = 0.65
KJV_GAP = 1.60
# No-dead-air law: the video ends TAIL seconds after the last spoken
# word. Derived, never hand-set. Clears the card's 0.8s fade-out so
# the last word and the fade are never clipped.
TAIL = 1.5


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:160])
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


def build_still(seg_id, src, dur, zdir, spoken_end, cap_text, speaker,
                first, last):
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.12*on/{frames}"
    else:
        z = f"1.121-0.12*on/{frames}"
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ""
    if first:
        tail = ",fade=t=in:st=0:d=1.2"
    if last:
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    capf = caption_filter(seg_id, dur, spoken_end, cap_text, speaker)
    fc = f"{base}{capf}{tail}[v]"
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


# --- MBM box-guard: strip Unicode line/paragraph separators + control chars that
# drawtext renders as tofu boxes at line ends (Cameron complaint 2026-07-23). ---
_MBM_SEP = {0x2028:0x20,0x2029:0x20,0x0085:0x20,0x000b:0x20,0x000c:0x20,0x000d:0x20}
for _c in list(range(0x00,0x09))+list(range(0x0e,0x20))+list(range(0x7f,0xa0)):
    _MBM_SEP[_c]=None
def _mbm_clean(_t):
    return _t.translate(_MBM_SEP)


def build_card(seg_id, dur, text, style):
    # AUTO-WRAP CARD LAW (2026-07-21, Cameron): the closing-question card ran
    # off-frame in 16 builds because this function trusted whatever line breaks
    # the narration text happened to carry. It no longer trusts the text: every
    # paragraph is re-wrapped to fit 1080px, and each line gets its OWN textfile
    # + drawtext (a newline never enters a textfile — the tofu bug). Rewriting
    # narration/card text can never break the card again.
    size = 50
    lh = size + 22
    lines = [w for para in text.split("\n")
             for w in (textwrap.wrap(para, width=30) or [""])]
    L = len(lines)
    vf = ""
    for j, ln in enumerate(lines):
        if not ln.strip():
            continue                   # blank line = vertical gap only
        tf = f"{S}/{seg_id}_{j}.txt"
        with open(tf, "w", encoding="utf-8") as f:
            f.write(ln)
        y = f"(h-{L * lh})/2+{j * lh}"
        vf += (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize={size}:"
               f"fontcolor={INK}:x=(w-text_w)/2:y={y},")
    vf += f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8"
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/{seg_id}.mp4"])


def main():
    os.makedirs(S, exist_ok=True)

    spoken = {n: spoken_of(f"audio/{n}.mp3") for n, _, _ in BEATS}
    card_spoken = spoken_of(f"audio/{CARD}.mp3")

    timeline = []
    audio_place = []
    start_of = {}
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
    card_vdur = LEAD + card_spoken + TAIL
    card_start = t
    audio_place.append((f"audio/{CARD}.mp3", card_start + LEAD))
    total = t + card_vdur

    worst, worst_at = 0.0, None
    prev_end = None
    for name, _s, _z, _v, a_start, _sp in timeline:
        if prev_end is not None and a_start - prev_end > worst:
            worst, worst_at = a_start - prev_end, name
        prev_end = a_start + spoken[name]
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min)", flush=True)
    print(f"worst spoken gap: {worst:.2f}s before {worst_at} (must be <= 2.5s)", flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s gap before {worst_at} exceeds 2.5s")
    print(f"sacred silence: {PEAK} at {start_of[PEAK]:.1f}s "
          f"(card at {card_start:.1f}s)", flush=True)

    n_beats = len(timeline)
    for i, (seg_id, still, zdir, vdur, _a, speaker) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, LEAD + spoken[seg_id],
                    TEXT[seg_id], speaker, first=(i == 0),
                    last=(i == n_beats - 1))
    build_card(CARD, card_vdur, TEXT[CARD], "close")

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write(f"file '{CARD}.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at derived offsets, NO synthetic bed ----
    # (Cameron, 2026-07-16: the sine-wave "music bed" reads as a background
    # hum and was rejected — narration and silence only.)
    inputs = []
    filters = []
    labels = []
    for i, (path, start) in enumerate(audio_place):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    n = len(labels)
    filters.append("".join(labels) +
                   f"amix=inputs={n}:duration=longest:normalize=0,"
                   f"apad=whole_dur={total:.2f}[aout]")
    run([FF, "-y"] + inputs + ["-filter_complex", ";".join(filters),
         "-map", "[aout]", "-t", f"{total:.2f}", "-c:a", "aac", "-b:a", "160k",
         f"{S}/audio_mix.m4a"])

    # ---- final mux, sized under 25MB ----
    run([FF, "-y", "-i", f"{S}/video_silent.mp4", "-i", f"{S}/audio_mix.m4a",
         "-map", "0:v", "-map", "1:a",
         "-c:v", "libx264", "-preset", "slow", "-crf", "23",
         "-maxrate", "1500k", "-bufsize", "3000k", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
         "luke-15_lost-coin.mp4"])
    size = os.path.getsize("luke-15_lost-coin.mp4") / 1e6
    print(f"DONE: luke-15_lost-coin.mp4  {size:.1f} MB, {total:.1f}s")


if __name__ == "__main__":
    main()
