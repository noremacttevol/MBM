#!/usr/bin/env python3
"""Assemble Story Video #173 — "The dead shall hear the voice of the
Son of God" (John 5:25).

PHASE-1 STILLS-ONLY (Law E): 8 painted stills, Ken Burns drift, narration,
serif captions (caption-v2: bottom band only, long lines CHUNKED and synced to
the spoken words — CAPTION LAW 2026-07-17), cream closing card. NO AI motion
clips. NO music bed of any kind (HUM PURGE 2026-07-16): audio is narration +
intentional silence only.

Two-voice: narrator en-US-AndrewNeural, Jesus en-US-ChristopherNeural
(FACE-SHOWN, master-locked) speaking ONLY exact KJV (John 5:25). The verse
is delivered as ONE continuous utterance split across three stills (j1a s2,
j1b s4, j1c s5) — j1a/j1b flow with a normal gap, j1c holds with the sacred
gap; the sacred pause the pack marks comes BEFORE the verse (n1 carries it).
CONTENT-CARE: no corpses/gore — the grave is light only (s4).

Bright daylight video: caption box black@0.60 (brightest-frame rule, #40).

Output: john-5_dead-shall-hear.mp4, 1080x1920 H.264 30fps, <25MB.
"""
import os
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
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"
BOX_ALPHA = 0.60   # daylight story — tuned to the brightest frame

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-speaking-to-the-crowd.jpeg"
S2 = "s2-verily-verily.jpeg"
S3 = "s3-faces-turning.jpeg"
S4 = "s4-light-summoned.jpeg"
S5 = "s5-the-calling-hand.jpeg"
S6 = "s6-hope-dawning.jpeg"
S7 = "s7-the-promise-of-life.jpeg"

TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}
KJV = {"j1a", "j1b", "j1c"}   # cream-italic verse (John 5:25)
FLOW = {"j1a", "j1b"}         # verse-internal joins: tight flow gap
SACRED = {"n1", "j1c"}        # sacred pause before the verse + hold at verse end
CARD_TEXT = ("He speaks, and death loses its grip. Lean in and listen — "
             "and live.")

BEATS = [
    ("n0", S1, "in"),
    ("n1", S3, "in"),
    ("j1a", S2, "in"),
    ("j1b", S4, "in"),
    ("j1c", S5, "in"),
    ("n2a", S6, "in"),
    ("j2", S6, "in"),
    ("n2c", S6, "out"),
    ("n2b", S7, "out"),
]

LEAD = 0.40
GAP = 1.65        # narration holds (measured silence stays ~2.3s, under the 2.5s law)
FLOW_GAP = 0.55   # verse-internal joins (j1a->j1b->j1c flow as one utterance)
SACRED_GAP = 1.65  # pre-verse pause (after n1) and verse-end hold (after j1c)
# No-dead-air law: the video ends TAIL seconds after the last spoken
# word. Derived, never hand-set. Clears the card's 0.8s fade-out so
# the last word and the fade are never clipped.
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


def sentences(text):
    import re
    return [p for p in re.split(r"(?<=[.!?;:]) +", text) if p]


def chunk_caption(text, width, max_lines):
    out, cur = [], ""
    for s in sentences(text):
        cand = (cur + " " + s).strip()
        if len(textwrap.wrap(cand, width)) <= max_lines:
            cur = cand
            continue
        if cur:
            out.append(cur)
        if len(textwrap.wrap(s, width)) <= max_lines:
            cur = s
        else:
            piece = ""
            for frag in s.split(", "):
                cand2 = (piece + ", " + frag).strip(", ").strip()
                if len(textwrap.wrap(cand2, width)) <= max_lines:
                    piece = cand2
                else:
                    if piece:
                        out.append(piece)
                    piece = frag
            cur = piece
    if cur:
        out.append(cur)
    return out


def build_still(seg_id, src, dur, zdir, spoken_end, cap_text, speaker, first):
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.09*on/{frames}"
    else:
        z = f"1.091-0.09*on/{frames}"
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    cap = caption_filter(seg_id, dur, spoken_end, cap_text, speaker)
    tail = ",fade=t=in:st=0:d=1.0" if first else ""
    fc = f"{base}{cap}{tail}[v]"
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


# --- MBM box-guard: strip Unicode line/paragraph separators + control chars that
# drawtext renders as tofu boxes at line ends (Cameron complaint 2026-07-23). ---
_MBM_SEP = {0x2028:0x20,0x2029:0x20,0x0085:0x20,0x000b:0x20,0x000c:0x20,0x000d:0x20}
for _c in list(range(0x00,0x09))+list(range(0x0e,0x20))+list(range(0x7f,0xa0)):
    _MBM_SEP[_c]=None
def _mbm_clean(_t):
    return _t.translate(_MBM_SEP)


def build_card(dur, text):
    tf = f"{S}/card.txt"
    with open(tf, "w") as f:
        f.write("\n".join(textwrap.wrap(_mbm_clean(text), width=30)))
    vf = (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize=50:"
          f"fontcolor={INK}:line_spacing=24:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/card.mp4"])


def main():
    os.makedirs(S, exist_ok=True)

    spoken = {n: spoken_of(f"audio/{n}.mp3") for n, _, _ in BEATS}
    card_dur = dur_of("audio/card.mp3")

    timeline = []
    t = 0.0
    audio_place = []
    j1_start = j2_start = None
    for name, still, zdir in BEATS:
        speaker = SPEAKER[name]
        if name in FLOW:
            gap = FLOW_GAP
        elif name in SACRED:
            gap = SACRED_GAP
        else:
            gap = GAP
        vdur = LEAD + spoken[name] + gap
        a_start = t + LEAD
        audio_place.append((f"audio/{name}.mp3", a_start))
        if name == "j1a":
            j1_start = a_start
        elif name == "j1c":
            j2_start = a_start
        timeline.append((name, still, zdir, vdur, a_start, speaker))
        t += vdur
    card_vdur = LEAD + card_dur + TAIL
    card_start = t
    audio_place.append(("audio/card.mp3", card_start + LEAD))
    total = t + card_vdur

    worst, worst_at, prev_end = 0.0, None, None
    for name, _s, _z, _v, a_start, _sp in timeline:
        if prev_end is not None and a_start - prev_end > worst:
            worst, worst_at = a_start - prev_end, name
        prev_end = a_start + spoken[name]
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min); "
          f"KJV verse {j1_start:.1f}s-{j2_start:.1f}s; "
          f"worst spoken gap {worst:.2f}s before {worst_at}", flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s before {worst_at}")

    for i, (seg_id, still, zdir, vdur, _a, speaker) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, LEAD + spoken[seg_id],
                    TEXT[seg_id], speaker, first=(i == 0))
    build_card(card_vdur, CARD_TEXT)

    with open(f"{S}/concat.txt", "w") as f:
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
            lufs = float(line.split()[1])
    gain = max(-6.0, min(16.0, -15.0 - lufs)) if lufs is not None else 0.0
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    OUT = "john-5_dead-shall-hear.mp4"
    A_KBPS, MUX = 96, 20
    vcap = max(500, int(24.0 * 8000 / total) - A_KBPS - MUX)
    vcap = min(vcap, 2200)
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
