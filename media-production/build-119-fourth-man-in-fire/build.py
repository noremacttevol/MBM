#!/usr/bin/env python3
"""Assemble Video #119 — The Fourth Man in the Fire (Daniel 3).

PHASE-1 STILLS-ONLY (Law E): ten painted stills, slow Ken Burns drift, serif captions,
cream-italic KJV (the Lord's exact words), closing question card. NO motion clips.

Captions are CAPTION v2 (Cameron 2026-07-15): wide along the bottom, narrator <=2 lines,
KJV <=3, long segments split into synced chunks. Copied from the build-48 template.

No Jesus figure appears in this video; God is a voice. The Lord's exact-KJV lines are
in the scripture voice (Christopher) and render cream-italic; the narrator paraphrases.

ALL-NARRATOR video: Daniel 3 has no direct speech from God, so there is no scripture
(Christopher) voice and no cream-italic caption here. Every caption is white narrator text.
TWO MUSIC HUSHES (bed dies to true silence, but both beats are narrator-voiced):
  n3   Dan 3:17-18   the "but if not" confession
  n6   Dan 3:25      "...the form of the fourth is like the Son of God."
No-Dead-Air is unaffected: the narrator never stops, only the music does.

Output: daniel-3_fourth-man-in-fire.mp4, 1080x1920 H.264 30fps, <30MB.
"""
import os
import subprocess
import textwrap

import make_narration  # SEGMENTS -> verbatim caption text per segment
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

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-the-golden-image.jpeg"
S2 = "s2-before-the-king.jpeg"
S3 = "s3-our-god-is-able.jpeg"
S4 = "s4-the-furnace.jpeg"
S5 = "s5-cast-into-the-fire.jpeg"
S6 = "s6-the-fourth.jpeg"
S7 = "s7-walking-unharmed.jpeg"
S8 = "s8-come-forth.jpeg"
S9 = "s9-not-a-hair-singed.jpeg"
S10 = "s10-the-god-who-delivers.jpeg"

TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}
# No God-speech in Daniel 3 -> no cream-italic lines; every caption is white narrator text.
KJV = set()
# The two most sacred beats get a longer breath + a true music hush (still narrator-voiced).
SILENCE = {"n3", "n6"}

# BEATS: (segment_name, still, zoom_dir). Stills advance 1->10, never backward.
BEATS = [
    ("n1", S1, "in"),
    ("n2", S2, "in"),
    ("s315", S2, "out"),
    ("n2b", S2, "in"),
    ("s317", S3, "in"),
    ("n3", S3, "out"),
    ("n4", S4, "in"),
    ("n5", S5, "in"),
    ("n6", S6, "in"),
    ("s325", S6, "out"),
    ("n6b", S6, "in"),
    ("n7", S7, "in"),
    ("s326", S8, "in"),
    ("n8", S8, "out"),
    ("n9", S9, "in"),
    ("s328", S10, "in"),
    ("n10", S10, "out"),
]

LEAD = 0.28
GAP = 0.65
KJV_GAP = 1.60
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


# ---- CAPTION SYSTEM v2 (copied byte-for-behaviour from build-48) ----
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
    # #104 stills carry a painted storybook border; crop the outer ~6% to remove it
    # (uniform, no regeneration) before the Ken Burns drift.
    base = (f"[0:v]crop=iw*0.88:ih*0.88,scale=2160:3868,setsar=1,"
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
    # per-line drawtext (no '\n' textfile — see caption_layers note on the tofu bug)
    size = 52
    lh = int(size * 1.5)
    lines = textwrap.wrap(_mbm_clean(text), width=30)
    N = len(lines)
    layers = []
    for j, ln in enumerate(lines):
        tf = f"{S}/card_{j}.txt"
        with open(tf, "w") as f:
            f.write(ln)
        # vertically centered block: line j offset from center
        y = f"(h-{lh})/2+{(j - (N - 1) / 2) * lh:.0f}"
        layers.append(
            f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize={size}:"
            f"fontcolor={INK}:x=(w-text_w)/2:y={y}")
    vf = ",".join(layers) + f",fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8"
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/card.mp4"])


def bed_filter(idx, start, end, style):
    d = end - start
    if d <= 1.0:
        return None
    if style == "a":
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
               "+0*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))"
               "+0*sin(2*PI*220*t)+0*sin(2*PI*329.63*t)'")
        eq = "lowpass=f=760,tremolo=f=0.12:d=0.3,aecho=0.7:0.4:311|429:0.24|0.17"
        fin, fout = 6, 6
    else:
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
               "+0*(sin(2*PI*146.83*t)+sin(2*PI*147.4*t))"
               "+0*sin(2*PI*196*t)+0*sin(2*PI*220*t)'")
        eq = "lowpass=f=700,tremolo=f=0.10:d=0.3,aecho=0.7:0.4:317|443:0.24|0.17"
        fin, fout = 6, 7
    ms = int(start * 1000)
    delay = f",adelay={ms}|{ms}" if ms else ""
    fin = min(fin, d / 3)
    fout = min(fout, d / 3)
    return (f"{src}:s=44100:d={d:.3f},{eq},"
            f"afade=t=in:st=0:d={fin:.2f},afade=t=out:st={d-fout:.2f}:d={fout:.2f}"
            f"{delay}[mus{idx}]")


def main():
    os.makedirs(S, exist_ok=True)

    spoken = {n: spoken_of(f"audio/{n}.mp3") for n, _, _ in BEATS}
    card_spoken = spoken_of("audio/card.mp3")

    timeline = []
    audio_place = []
    start_of = {}
    t = 0.0
    for name, still, zdir in BEATS:
        speaker = SPEAKER[name]
        gap = KJV_GAP if name in SILENCE else GAP
        vdur = LEAD + spoken[name] + gap
        a_start = t + LEAD
        audio_place.append((f"audio/{name}.mp3", a_start))
        start_of[name] = a_start
        timeline.append((name, still, zdir, vdur, a_start, speaker))
        t += vdur
    card_vdur = LEAD + card_spoken + TAIL
    card_start = t
    audio_place.append(("audio/card.mp3", card_start + LEAD))
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
    print(f"music hush 1 (the 'but if not' confession): n3 at {start_of['n3']:.1f}s", flush=True)
    print(f"music hush 2 (form of the fourth): n6 at {start_of['n6']:.1f}s", flush=True)

    for i, (seg_id, still, zdir, vdur, _a, speaker) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, LEAD + spoken[seg_id],
                    TEXT[seg_id], speaker, first=(i == 0))
    build_card(card_vdur, TEXT["card"])

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # n3 and n6 are the two sacred beats; the music bed dies to true silence across each,
    # and returns in between and after (up to the card). Both are narrator-voiced, so the
    # narrator carries through — only the music drops.
    h1_end = start_of["n3"] + spoken["n3"]
    h2_end = start_of["n6"] + spoken["n6"]
    beds = [
        (0.0, start_of["n3"] - 1.2, "b"),
        (h1_end + 1.0, start_of["n6"] - 1.2, "a"),
        (h2_end + 1.0, card_start - 0.8, "a"),
    ]
    print(f"music: bed out before n3 at {start_of['n3'] - 1.2:.1f}s (silence through n3, "
          f"ends {h1_end:.1f}s); returns; bed out before n6 at {start_of['n6'] - 1.2:.1f}s "
          f"(silence through n6, ends {h2_end:.1f}s); returns to the card", flush=True)

    inputs, filters, labels = [], [], []
    for i, (path, start) in enumerate(audio_place):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(
            f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    bi = 0
    for (bs, be, st) in beds:
        bf = bed_filter(bi, bs, be, st)
        if bf:
            filters.append(bf)
            labels.append(f"[mus{bi}]")
            bi += 1
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

    OUT = "daniel-3_fourth-man-in-fire.mp4"
    A_KBPS = 96
    MUX = 20
    vcap = int(24.0 * 8000 / total) - A_KBPS - MUX
    if vcap < 400:
        raise SystemExit(
            f"BITRATE STARVED: {total:.0f}s leaves only {vcap} kbps inside the 30MB "
            f"law (need >=400). Shorten the script — do not ship blocking.")
    print(f"video budget: {vcap} kbps ({total:.0f}s, {A_KBPS}k audio)", flush=True)

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
        if size <= 29.3:
            break
        print(f"  {size:.1f} MB at crf {crf} — over, stepping up", flush=True)
    print(f"DONE: {OUT}  {size:.1f} MB, {total:.1f}s (crf {crf}, vcap {vcap}k)", flush=True)


if __name__ == "__main__":
    main()
