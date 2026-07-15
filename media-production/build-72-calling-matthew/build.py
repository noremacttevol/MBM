#!/usr/bin/env python3
"""Assemble Video #72 — Calling Matthew (Matthew 9:9-13). v3 REDO 2026-07-15.

PHASE-1 STILLS-ONLY build (Law E): twelve painted stills, Ken Burns drift, narration,
serif captions (CAPTION v2), cream-italic KJV, closing invitation card.

FACE LAW v3: Jesus's face IS shown in s3, s4, s6, s9, locked to JESUS-MASTER-REF
(attached as --ref at generation). His two KJV lines (j1 "Follow me"; j2 the physician /
mercy line) render in cream italic and are the two sacred silences. Only Jesus wears cream.

Windows-ready: ffmpeg/ffprobe on PATH; Georgia copied to a colon-free relative path
(segs/serif.ttf, serif_bi.ttf). Output: matthew-9_calling-matthew.mp4, 1080x1920, <30MB.
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
SERIF = "segs/serif.ttf"
SERIF_BI = "segs/serif_bi.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-the-customs-booth.jpeg"
S2 = "s2-the-isolated-man.jpeg"
S3 = "s3-he-sees-him.jpeg"
S4 = "s4-follow-me.jpeg"
S5 = "s5-he-arose.jpeg"
S6 = "s6-the-feast.jpeg"
S7 = "s7-the-welcomed.jpeg"
S8 = "s8-the-pharisees-object.jpeg"
S9 = "s9-the-physician.jpeg"
S10 = "s10-mercy-not-sacrifice.jpeg"
S11 = "s11-matthew-the-writer.jpeg"
S12 = "s12-the-open-door.jpeg"

TEXT = {s[0]: s[4] for s in make_narration.SEGMENTS}
KJV = {"j1", "j2"}

BEATS = [
    ("n1", S1, "in"),
    ("n2", S2, "in"),
    ("n3", S3, "in"),
    ("j1", S4, "in"), ("n4", S4, "out"),         # SACRED SILENCE 1 — the call
    ("n5", S5, "in"),
    ("n6", S6, "in"),
    ("n7", S7, "in"),
    ("n8", S8, "in"),
    ("j2", S9, "in"), ("n9", S9, "out"),         # SACRED SILENCE 2 — the heart line
    ("n10", S10, "in"),
    ("n11", S11, "in"),
    ("n12", S12, "in"),
]

LEAD = 0.28
GAP = 0.65
KJV_GAP = 1.60
CARD_HOLD = 4.2


def _ensure_fonts():
    os.makedirs(S, exist_ok=True)
    win = os.environ.get("WINDIR", r"C:\Windows")
    pairs = [(os.path.join(win, "Fonts", "georgia.ttf"), f"{S}/serif.ttf"),
             (os.path.join(win, "Fonts", "georgiai.ttf"), f"{S}/serif_bi.ttf")]
    for src, dst in pairs:
        if not os.path.exists(dst):
            shutil.copyfile(src, dst)


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


def caption_layers(seg_id, dur, spoken_end, text, kjv):
    if kjv:
        font, size, color, width, maxl = SERIF_BI, 46, "0xFFF3DC", 38, 3
    else:
        font, size, color, width, maxl = SERIF, 34, "white", 48, 2
    chunks = chunk_caption(text, width, maxl)
    total = sum(len(c) for c in chunks) or 1
    t0, t1 = 0.15, max(0.6, min(dur - 0.2, spoken_end + 0.35))
    filters, labels = [], []
    acc = 0
    for i, c in enumerate(chunks):
        cs = t0 + (t1 - t0) * acc / total
        acc += len(c)
        ce = t0 + (t1 - t0) * acc / total
        tf = f"{S}/{seg_id}_{i}.txt"
        with open(tf, "w", encoding="utf-8") as f:
            f.write("\n".join(textwrap.wrap(c, width)))
        fo = max(cs, ce - 0.35)
        filters.append(
            f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile={font}:textfile={tf}:fontsize={size}:"
            f"fontcolor={color}:line_spacing=13:x=(w-text_w)/2:"
            f"y=h-120-text_h:"
            f"shadowcolor=black@0.9:shadowx=2:shadowy=2:"
            f"box=1:boxcolor=black@0.58:boxborderw=22,"
            f"fade=t=in:st={cs:.2f}:d=0.35:alpha=1,"
            f"fade=t=out:st={fo:.2f}:d=0.35:alpha=1[cap{seg_id}{i}]")
        labels.append(f"[cap{seg_id}{i}]")
    return filters, labels


def build_still(seg_id, src, dur, zdir, spoken_end, cap_text, kjv, first):
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.09*on/{frames}"
    else:
        z = f"1.091-0.09*on/{frames}"
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    capf, labels = caption_layers(seg_id, dur, spoken_end, cap_text, kjv)
    tail = ",fade=t=in:st=0:d=1.0" if first else ""
    steps, cur = [], "b"
    for i, lab in enumerate(labels):
        last = (i == len(labels) - 1)
        nxt = "v" if last else f"b{i+1}"
        steps.append(f"[{cur}]{lab}overlay=format=auto"
                     + (tail if last else "") + f"[{nxt}]")
        cur = nxt
    fc = f"{base}[b];" + ";".join(capf) + ";" + ";".join(steps)
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(dur, text):
    tf = f"{S}/card.txt"
    with open(tf, "w", encoding="utf-8") as f:
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
        src = ("aevalsrc='0.020*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
               "+0.015*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))"
               "+0.011*sin(2*PI*220*t)+0.007*sin(2*PI*329.63*t)'")
        eq = "lowpass=f=760,tremolo=f=0.12:d=0.3,aecho=0.7:0.4:311|429:0.24|0.17"
        fin, fout = 6, 6
    else:
        src = ("aevalsrc='0.013*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
               "+0.010*(sin(2*PI*146.83*t)+sin(2*PI*147.4*t))"
               "+0.008*sin(2*PI*196*t)+0.006*sin(2*PI*220*t)'")
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
    _ensure_fonts()

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
    print(f"sacred silences: j1 at {start_of['j1']:.1f}s, j2 at {start_of['j2']:.1f}s",
          flush=True)

    for i, (seg_id, still, zdir, vdur, _a, kjv) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, LEAD + spoken[seg_id],
                    TEXT[seg_id], kjv, first=(i == 0))
    build_card(card_vdur, TEXT["card"])

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    p1_end = start_of["j1"] + spoken["j1"]
    p2_end = start_of["j2"] + spoken["j2"]
    beds = [
        (0.0, start_of["j1"] - 1.2, "b"),
        (p1_end + 1.0, start_of["j2"] - 1.0, "a"),
        (p2_end + 1.0, card_start - 0.8, "a"),
    ]
    print(f"music: silent through j1 (ends {p1_end:.1f}s) and j2 (ends {p2_end:.1f}s)",
          flush=True)

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
    gain = max(-6.0, min(10.0, -15.0 - lufs)) if lufs is not None else 0.0
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    OUT = "matthew-9_calling-matthew.mp4"
    A_KBPS = 96
    MUX = 20
    vcap = int(29.5 * 8000 / total) - A_KBPS - MUX
    if vcap < 400:
        raise SystemExit(f"BITRATE STARVED: {vcap} kbps < 400 in the 30MB law")
    print(f"video budget: {vcap} kbps ({total:.0f}s)", flush=True)

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
