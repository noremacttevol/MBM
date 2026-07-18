#!/usr/bin/env python3
"""Assemble Story Video #17 — The Raising of Lazarus (John 11:1-44).
Phase-1 STILLS-ONLY (Law E) and the Face Law / Correction #18 (the Lord staged
only from behind / over-the-shoulder / at a distance; face never shown; no glow).
9 painted stills, Ken Burns drift, serif captions. Music map: warm bed opens,
goes FULL SILENCE across the sacred seal, then a warm bed swells under the
meaning and is out before the card.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Converted from the old
template B: the 7-tuple SEGMENTS with hardcoded durations and a per-beat
`caption_style` is gone. Who is speaking is declared ONCE in make_narration.py and
decides BOTH the narration voice and the caption colour. Beat durations are derived
from the narration audio (LEAD + spoken + gap), never hand-set, and the video ends
TAIL seconds after the last spoken word.

The caption look, the Ken Burns maths, the audio mix, the loudness pass and the
size ladder are unchanged.

Output: john-11_lazarus.mp4, 1080x1920 H.264 30fps, <25MB.
"""
import os
import shutil
import subprocess

import make_narration  # SEGMENTS -> verbatim caption text + speaker per segment
from mbm_caption_timing import caption_filter
from mbm_speakers import is_scripture

FF = shutil.which("ffmpeg") or "ffmpeg"
FPROBE = shutil.which("ffprobe") or "ffprobe"
A, S, FPS = "assets", "segs", 30
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
CREAM, INK = "0xF7F2E9", "0x3B2A1E"
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1.jpeg"
S2 = "s2.jpeg"
S3 = "s3.jpeg"
S4 = "s4.jpeg"
S5 = "s5.jpeg"
S6 = "s6.jpeg"
S7 = "s7.jpeg"
S8 = "s8.jpeg"
S9 = "s9.jpeg"

TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}

# BEATS: (segment_name, still, zoom_dir). Zoom alternates in/out on a shared still.
BEATS = [
    ("n0", S1, "in"),
    ("w3", S2, "in"),
    ("n1", S2, "out"),
    ("j1", S2, "in"),
    ("n1b", S2, "out"),
    ("n2", S3, "in"),
    ("w21", S4, "in"),
    ("n3", S4, "out"),
    ("n4", S5, "in"),
    ("j2", S5, "out"),
    ("w27", S5, "in"),
    ("n5", S6, "in"),
    ("w32", S6, "out"),
    ("n6", S6, "in"),
    ("n7", S7, "in"),
    ("w39", S7, "out"),
    ("j3", S7, "in"),
    ("n7b", S7, "out"),
    ("n8", S8, "in"),
    ("j4", S8, "out"),
    ("n9", S8, "in"),
    ("j5", S9, "in"),
    ("n10", S9, "out"),
]

# The closing card is narrated but is not a beat — build_card places it itself.
CARD = "n11"
# PEAK: the beat the music bed dies for — the first non-narrator voice in the story.
PEAK = "w3"

LEAD = 0.28
GAP = 0.65
KJV_GAP = 1.60
# No-dead-air law: the video ends TAIL seconds after the last spoken
# word. Derived, never hand-set. Clears the card's 0.8s fade-out so
# the last word and the fade are never clipped.
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


def build_still(seg_id, src, dur, zdir, spoken_end, cap_text, speaker, first, last):
    frames = int(dur * FPS)
    z = f"1.001+0.09*on/{frames}" if zdir == "in" else f"1.091-0.09*on/{frames}"
    base = (f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,"
            f"crop=2160:3840,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},scale=1080:1920:flags=lanczos")
    cap = caption_filter(seg_id, dur, spoken_end, cap_text, speaker)
    tail = ""
    if first:
        tail = ",fade=t=in:st=0:d=1.2"
    if last:
        tail = f",fade=t=out:st={dur-1.0}:d=1.0"
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", f"{base}{cap}{tail}[v]",
         "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(seg_id, dur, text):
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w", encoding="utf-8") as f:
        f.write(text)
    vf = (f"drawtext=fontfile='{SERIF}':textfile='{tf}':fontsize=48:"
          f"fontcolor={INK}:line_spacing=20:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run([FF, "-y", "-f", "lavfi", "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/{seg_id}.mp4"])


def bed_filter(idx, start, end, style):
    dur = end - start
    if dur <= 1.0:
        return None
    if style == "a":
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
               "+0*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))+0*sin(2*PI*220*t)'")
        eq = "lowpass=f=760,tremolo=f=0.12:d=0.3,aecho=0.7:0.4:311|429:0.24|0.17"
        fin, fout = 6, 6
    else:
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
               "+0*(sin(2*PI*146.83*t)+sin(2*PI*147.5*t))+0*sin(2*PI*196*t)'")
        eq = "lowpass=f=720,tremolo=f=0.10:d=0.3,aecho=0.7:0.4:317|443:0.24|0.17"
        fin, fout = 5, 7
    if dur < fin + fout + 2:
        fin = fout = max(2, int((dur - 2) / 2))
    ms = int(start * 1000)
    delay = f",adelay={ms}|{ms}" if ms else ""
    return (f"{src}:s=44100:d={dur},{eq},afade=t=in:st=0:d={fin},"
            f"afade=t=out:st={dur-fout}:d={fout}{delay}[mus{idx}]")


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
    print(f"sacred silence: {PEAK} at {start_of[PEAK]:.1f}s", flush=True)

    n_beats = len(timeline)
    for i, (seg_id, still, zdir, vdur, _a, speaker) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, LEAD + spoken[seg_id],
                    TEXT[seg_id], speaker, first=(i == 0), last=(i == n_beats - 1))
    build_card(CARD, card_vdur, TEXT[CARD])

    with open(f"{S}/concat.txt", "w", encoding="utf-8") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write(f"file '{CARD}.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # gentle drones; go SILENT under the sacred seal
    peak_end = start_of[PEAK] + spoken[PEAK]
    beds = [
        (0.0, start_of[PEAK] - 1.2, "a"),
        (peak_end + 1.0, card_start - 0.8, "b"),
    ]

    inputs, filters, labels = [], [], []
    for i, (path, start) in enumerate(audio_place):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    bi = 0
    for (bs, be, st) in beds:
        bf = bed_filter(bi, bs, be, st)
        if bf:
            filters.append(bf)
            labels.append(f"[mus{bi}]")
            bi += 1
    n = len(labels)
    filters.append("".join(labels) + f"amix=inputs={n}:duration=longest:normalize=0,"
                   f"apad=whole_dur={total:.2f}[aout]")
    run([FF, "-y"] + inputs + ["-filter_complex", ";".join(filters),
        "-map", "[aout]", "-t", f"{total:.2f}", "-c:a", "aac", "-b:a", "160k",
        f"{S}/audio_mix.m4a"])

    probe = subprocess.run([FF, "-i", f"{S}/audio_mix.m4a", "-af", "ebur128",
                            "-f", "null", "-"], capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            try:
                lufs = float(line.split()[1])
            except ValueError:
                pass
    gain = 0.0 if lufs is None else max(-6.0, min(12.0, -15.0 - lufs))
    print(f"loudness: {lufs} LUFS, gain {gain:+.1f} dB", flush=True)

    OUT = "john-11_lazarus.mp4"
    vcap = max(300, int(24.5 * 8000 / total) - 145)
    size, crf = 0.0, 21
    for crf in (21, 22, 23, 24, 25, 26):
        run([FF, "-y", "-i", f"{S}/video_silent.mp4", "-i", f"{S}/audio_mix.m4a",
             "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "veryslow",
             "-crf", str(crf), "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p", "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", OUT])
        size = os.path.getsize(OUT) / 1e6
        if size <= 24.5:
            break
    print(f"DONE: {OUT}  {size:.1f} MB, {total:.1f}s (crf {crf})", flush=True)


if __name__ == "__main__":
    main()
