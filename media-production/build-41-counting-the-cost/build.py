#!/usr/bin/env python3
"""Assemble Story Video #41 — Counting the Cost (Luke 14:25-35).

PHASE-1 STILLS-ONLY (Law E): 16 painted stills, Ken Burns drift, narration, serif
captions, cream-italic KJV lines, closing question card. NO AI motion clips.

Stills are already generated in assets/<slug>.jpeg (Flow, $0). Narration is already
generated in audio/ (make_narration.SEGMENTS). CAPTIONS ARE VERBATIM: every caption
is the exact spoken text of its segment. KJV (Jesus) lines render cream italic.

Face-never (the #1 Law): no divine face is ever rendered; where Jesus appears he is
staged from behind / over-the-shoulder per the prompt sheet (gate PASS).

TWO SACRED SILENCES (the music bed dies to true silence for both):
  j1   Luke 14:26   the hard saying ("hate not his father...") — reverent space
  j7   Luke 14:33   THE VERDICT ("forsaketh not all... cannot be my disciple")
A warm bed carries the story in, dies before the hard saying, returns to carry the
middle, dies again before the verdict, then returns for the turn and the invitation.

SIZE: 25MB cap (Cameron, 2026-07-14) — long stories keep every word at full quality
rather than being trimmed or starved. The honest video budget is computed against a
~29.5MB container so the first CRF pass lands in range with a real bitrate.

Output: luke-14_counting-the-cost.mp4, 1080x1920 H.264 30fps, <30MB.
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

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-the-great-multitude.jpeg"
S2 = "s2-he-turned.jpeg"
S3 = "s3-the-crowd-goes-quiet.jpeg"
S4 = "s4-the-hand-on-the-sleeve.jpeg"
S5 = "s5-the-road-to-jerusalem.jpeg"
S6 = "s6-he-sits-down-first.jpeg"
S7 = "s7-the-half-built-tower.jpeg"
S8 = "s8-the-king-counts.jpeg"
S9 = "s9-the-ambassage.jpeg"
S10 = "s10-so-likewise.jpeg"
S11 = "s11-the-crowd-thins.jpeg"
S12 = "s12-the-savourless-salt.jpeg"
S13 = "s13-why-he-did-it.jpeg"
S14 = "s14-the-finished-tower.jpeg"
S15 = "s15-toward-jerusalem.jpeg"
S16 = "s16-the-open-road.jpeg"

TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}

BEATS = [
    ("n1", S1, "in"),
    ("s25", S2, "in"),
    ("n2", S2, "out"),
    ("j1", S2, "in"),
    ("n3", S3, "in"),
    ("n4", S4, "in"),
    ("j2", S5, "in"),
    ("n5", S5, "out"),
    ("j3", S6, "in"),
    ("n6", S6, "out"),
    ("jv29", S7, "in"),
    ("n7", S7, "out"),
    ("j5", S8, "in"),
    ("n8", S8, "out"),
    ("j6", S9, "in"),
    ("n9", S9, "out"),
    ("j7", S10, "in"),
    ("n10", S10, "out"),
    ("n11", S11, "in"),
    ("j8", S12, "in"),
    ("n12", S12, "out"),
    ("n13a", S13, "in"),
    ("n13b", S13, "out"),
    ("n14", S14, "in"),
    ("n15", S15, "in"),
    ("n16", S16, "in"),
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


def wrapped(name):
    return "\n".join(textwrap.wrap(TEXT[name], width=34))


def _cap_chunks(text, width, max_lines):
    words = text.split()
    chunks, cur = [], ""
    for w in words:
        cand = (cur + " " + w).strip()
        if len(textwrap.wrap(cand, width)) <= max_lines:
            cur = cand
        else:
            chunks.append(cur)
            cur = w
    if cur:
        chunks.append(cur)
    return chunks


def build_still(seg_id, src, dur, zdir, cap_text, speaker, first):
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.09*on/{frames}"
    else:
        z = f"1.091-0.09*on/{frames}"
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    cap = caption_filter(seg_id, dur, dur, cap_text, speaker)
    tail = ",fade=t=in:st=0:d=1.0" if first else ""
    fc = f"{base}{cap}{tail}[v]"
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(dur, text):
    # One drawtext per LINE (2026-07-17, #7 end-card rejection): this box's
    # ffmpeg renders a textfile newline as a tofu box, so a newline never
    # enters a textfile — each wrapped line gets its own textfile + drawtext,
    # centered as a block.
    lines = textwrap.wrap(text, width=30)
    lh = 52 + 24                       # fontsize + line spacing
    L = len(lines)
    vf = ""
    for j, ln in enumerate(lines):
        tf = f"{S}/card_{j}.txt"
        with open(tf, "w", encoding="utf-8") as f:
            f.write(ln)
        y = f"(h-{L * lh})/2+{j * lh}"
        vf += (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize=52:"
               f"fontcolor={INK}:x=(w-text_w)/2:y={y},")
    vf += f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8"
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
    card_vdur = LEAD + card_spoken + TAIL
    card_start = t
    audio_place.append(("audio/card.mp3", card_start + LEAD))
    total = t + card_vdur

    worst, worst_at, prev_end = 0.0, None, None
    for name, _s, _z, _v, a_start, _sp in timeline:
        if prev_end is not None and a_start - prev_end > worst:
            worst, worst_at = a_start - prev_end, name
        prev_end = a_start + spoken[name]
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min)", flush=True)
    print(f"worst spoken gap: {worst:.2f}s before {worst_at} (<= 2.5s)", flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s gap before {worst_at}")
    print(f"sacred silence 1 (hard saying): j1 at {start_of['j1']:.1f}s", flush=True)
    print(f"sacred silence 2 (the verdict): j7 at {start_of['j7']:.1f}s", flush=True)

    for i, (seg_id, still, zdir, vdur, _a, speaker) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, wrapped(seg_id), speaker, first=(i == 0))
    build_card(card_vdur, TEXT["card"])

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    p1_end = start_of["j1"] + spoken["j1"]
    p2_end = start_of["j7"] + spoken["j7"]
    beds = [
        (0.0, start_of["j1"] - 1.2, "b"),
        (p1_end + 1.0, start_of["j7"] - 1.0, "a"),
        (p2_end + 1.0, card_start - 0.8, "a"),
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

    # 25MB cap (Cameron 2026-07-14): budget against a ~29.5MB container so long
    # stories keep every word at a real bitrate instead of being trimmed/starved.
    OUT = "luke-14_counting-the-cost.mp4"
    A_KBPS, MUX = 96, 20
    vcap = int(24.0 * 8000 / total) - A_KBPS - MUX
    if vcap < 400:
        raise SystemExit(
            f"BITRATE STARVED even at 25MB: {total:.0f}s only leaves {vcap} kbps "
            f"(need >=400). This story is too long even for the raised cap.")
    print(f"video budget: {vcap} kbps ({total:.0f}s, 25MB cap)", flush=True)

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
        if size <= 29.5:
            break
        print(f"  {size:.1f} MB at crf {crf} — over, stepping up", flush=True)
    print(f"DONE: {OUT}  {size:.1f} MB, {total:.1f}s (crf {crf}, vcap {vcap}k)",
          flush=True)


if __name__ == "__main__":
    main()
