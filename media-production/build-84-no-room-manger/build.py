#!/usr/bin/env python3
"""Assemble Story Video #84 — No Room, the Manger (Luke 2:1-7).

PHASE-1 STILLS-ONLY (Law E): 12 painted stills, Ken Burns drift, narration, serif
captions, a cream-italic scripture verse card, closing question card. NO AI motion clips.

Stills are already generated in assets/<slug>.jpeg (Flow, $0). Narration is already
generated in audio/ (make_narration.SEGMENTS). CAPTIONS ARE VERBATIM.

FACE LAW: the newborn's face is never rendered anywhere; he is a swaddled bundle seen
from behind the parents / above / turned away per the prompt sheet (gate PASS). There is
no adult Jesus and no Jesus-speech line in this nativity.

ONE SACRED SILENCE (the music bed dies to true silence):
  v7   Luke 2:7   the birth verse ("...laid him in a manger; because there was no room")
This is scripture read reverently by the NARRATOR (no Jesus voice in a nativity), rendered
cream-italic like a verse card and given the sacred silence.

WINDOWS BUILD NOTE (Machine B): uses Windows serif fonts (Georgia regular + italic),
copied into segs/ so the ffmpeg drawtext fontfile= path is relative (no C: escaping).

SIZE: 30MB cap. crf 20 base, clamped bitrate.

Output: luke-2_no-room-the-manger.mp4, 1080x1920 H.264 30fps, <30MB.
"""
import os
import shutil
import subprocess
import textwrap

import make_narration

A = "assets"
S = "segs"
FPS = 30
FF = "ffmpeg"
FPROBE = "ffprobe"

WIN_FONTS = os.environ.get("WINDIR", "C:\\Windows") + "\\Fonts"
SERIF_SRC = os.path.join(WIN_FONTS, "georgia.ttf")
SERIF_BI_SRC = os.path.join(WIN_FONTS, "georgiai.ttf")
SERIF = f"{S}/serif.ttf"
SERIF_BI = f"{S}/serif_bi.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-the-decree.jpeg"
S2 = "s2-the-long-road.jpeg"
S3 = "s3-crowded-bethlehem.jpeg"
S4 = "s4-no-room.jpeg"
S5 = "s5-the-stable.jpeg"
S6 = "s6-the-birth.jpeg"
S7 = "s7-the-manger.jpeg"
S8 = "s8-the-wonder.jpeg"
S9 = "s9-the-humble-king.jpeg"
S10 = "s10-the-sleeping-town.jpeg"
S11 = "s11-the-one-light.jpeg"
S12 = "s12-there-is-room.jpeg"

TEXT = {s[0]: s[4] for s in make_narration.SEGMENTS}
KJV = {"v7"}   # cream-italic verse card + sacred silence (scripture, narrator-read)

BEATS = [
    ("n1", S1, "in"),
    ("n2", S2, "in"),
    ("n3", S3, "in"),
    ("n4", S4, "in"),
    ("n5", S5, "in"),
    ("n6", S6, "in"),
    ("v7", S7, "in"), ("n7", S7, "out"),         # SACRED SILENCE — the birth verse
    ("n8", S8, "in"),
    ("n9", S9, "in"),
    ("n10", S10, "in"),
    ("n11", S11, "in"),
    # s12 (dawn open-door) not generated: Chrome extension on Machine B dropped after
    # 11 stills. n12 (the closing invitation) holds on s11 — the glowing open stable,
    # which fits "the door is still open, there is room" — with an out-drift so it
    # breathes differently from n11. Swap in a dedicated s12 later if wanted.
    ("n12", S11, "out"),
]

LEAD = 0.28
GAP = 0.65
KJV_GAP = 1.60
CARD_HOLD = 4.2


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


def caption_overlay(seg_id, dur, text, kjv):
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w") as f:
        f.write(text)
    if kjv:
        font, size, color = SERIF_BI, 46, "0xFFF3DC"
    else:
        font, size, color = SERIF, 34, "white"
    fade_out = max(0.0, dur - 0.55)
    return (f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile={font}:textfile={tf}:fontsize={size}:"
            f"fontcolor={color}:line_spacing=13:x=(w-text_w)/2:"
            f"y=h-150-text_h:"
            f"shadowcolor=black@0.9:shadowx=2:shadowy=2:"
            f"box=1:boxcolor=black@0.58:boxborderw=22,"
            f"fade=t=in:st=0:d=0.5:alpha=1,"
            f"fade=t=out:st={fade_out}:d=0.5:alpha=1[cap]")


def build_still(seg_id, src, dur, zdir, cap_text, kjv, first):
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.09*on/{frames}"
    else:
        z = f"1.091-0.09*on/{frames}"
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    capf = caption_overlay(seg_id, dur, cap_text, kjv)
    tail = ",fade=t=in:st=0:d=1.0" if first else ""
    fc = f"{base}[b];{capf};[b][cap]overlay=format=auto{tail}[v]"
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(dur, text):
    tf = f"{S}/card.txt"
    with open(tf, "w") as f:
        f.write("\n".join(textwrap.wrap(text, width=30)))
    vf = (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize=52:"
          f"fontcolor={INK}:line_spacing=24:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
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
    shutil.copyfile(SERIF_SRC, SERIF)
    shutil.copyfile(SERIF_BI_SRC, SERIF_BI)

    spoken = {n: spoken_of(f"audio/{n}.mp3") for n, _, _ in BEATS}
    card_spoken = spoken_of("audio/card.mp3")

    timeline, audio_place, start_of = [], [], {}
    t = 0.0
    for name, still, zdir in BEATS:
        kjv = name in KJV
        gap = KJV_GAP if kjv else GAP
        vdur = LEAD + spoken[name] + gap
        a_start = t + LEAD
        audio_place.append((f"audio/{name}.mp3", a_start))
        start_of[name] = a_start
        timeline.append((name, still, zdir, vdur, a_start, kjv))
        t += vdur
    card_vdur = LEAD + card_spoken + CARD_HOLD
    card_start = t
    audio_place.append(("audio/card.mp3", card_start + LEAD))
    total = t + card_vdur

    worst, worst_at, prev_end = 0.0, None, None
    for name, _s, _z, _v, a_start, _k in timeline:
        if prev_end is not None and a_start - prev_end > worst:
            worst, worst_at = a_start - prev_end, name
        prev_end = a_start + spoken[name]
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min)", flush=True)
    print(f"worst spoken gap: {worst:.2f}s before {worst_at} (<= 2.5s)", flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s gap before {worst_at}")
    print(f"sacred silence (the birth verse): v7 at {start_of['v7']:.1f}s", flush=True)

    for i, (seg_id, still, zdir, vdur, _a, kjv) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, wrapped(seg_id), kjv, first=(i == 0))
    build_card(card_vdur, TEXT["card"])

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    p1_end = start_of["v7"] + spoken["v7"]
    beds = [
        (0.0, start_of["v7"] - 1.2, "b"),
        (p1_end + 1.0, card_start - 0.8, "a"),
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
    gain = max(-6.0, min(10.0, -15.0 - lufs)) if lufs is not None else 0.0
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    OUT = "luke-2_no-room-the-manger.mp4"
    A_KBPS, MUX = 96, 20
    vcap = int(29.5 * 8000 / total) - A_KBPS - MUX
    if vcap < 400:
        raise SystemExit(
            f"BITRATE STARVED even at 30MB: {total:.0f}s only leaves {vcap} kbps.")
    vcap = min(vcap, 2200)
    print(f"video budget: {vcap} kbps ({total:.0f}s, 30MB cap)", flush=True)

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
