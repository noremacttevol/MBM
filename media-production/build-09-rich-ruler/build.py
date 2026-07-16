#!/usr/bin/env python3
"""Assemble Story Video #9 — The Rich Young Ruler (Mark 10:17-22).

Full law stack per PRODUCTION-BIBLE.md + PREFLIGHT.md. Hybrid storybook:
6 painted stills with Ken Burns drift + 2 Veo money-moment clips (the
undignified RUN, 8s stretched to 12.8s; the walk-away into dusk, 8s
stretched to 12.8s), edge-tts narration (ear-checked 9/9), serif
captions, KJV red-letter j1 (Mark 10:21 exact), closing question card on
cream #F7F2E9. Assembly Craft Laws: supersampled zoompan (anti-shimmer),
RGBA caption fades, crf-16 intermediates, veryslow crf step-up final,
loudness toward -15 LUFS, detuned-pair music beds.

Two-Voice Law: narrator modern American; Jesus ONLY exact KJV (10:21).
Music map (the pack's law): sparse beds under n0-n2, FULL SILENCE before
j1; a quiet bed may run under n3-n4; music DIES at the start of n5
("And Jesus let him go") and NEVER returns — s7, s8, and the card all
play in true silence under voice. The ending stays in sorrow.

All offsets computed from MEASURED mp3 durations + measured trailing
silence (spoken end = start + dur - tail); breaths 0.8-1.3s.

Output: 1080x1920 H.264 30fps, <25MB, 217.4s.
"""
import os
import subprocess

A = "assets"
S = "segs"
FPS = 30
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BI = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-the-run.jpeg"        # was a Veo clip — now a face-shown still (Law E)
S2 = "s2-kneeling-earnest.jpeg"
S3 = "s3-the-look.jpeg"
S4 = "s4-the-one-thing.jpeg"
S5 = "s5-words-land.jpeg"
S6 = "s6-walk-away.jpeg"       # was a Veo clip — now a face-shown still (Law E)
S7 = "s7-he-let-him-go.jpeg"
S8 = "s8-empty-road.jpeg"

# (id, kind, source, stretch_or_none, duration_s, zoom_dir, caption, style)
# Boundaries: 0, 12.8, 28.0, 46.4, 65.6, 79.0, 92.8, 100.6, 108.6, 124.6,
# 141.2, 154.0, 166.8, 183.4, 193.4, 203.8, 217.4.
SEGMENTS = [
    # n0 — the run (v17 + the WHY-gem). Face-shown still (Law E) opens it.
    ("n0a", "still", S1, None, 12.8, "in",
     "Jesus was setting out on a journey when\n"
     "a young man came running down the road\n"
     "after him. Running. You need to\n"
     "understand what that looked like.", "n"),
    ("n0b", "still", S2, None, 15.2, "in",
     "This man was wealthy — fine robes, gold\n"
     "rings, a name people knew. Men like that\n"
     "did not run in public. It was beneath\n"
     "them. He ran anyway, in front of everyone,\n"
     "and dropped to his knees in the dust\n"
     "at Jesus's feet.", "n"),
    # n1 — the question + the record (v17b, v19-20 modern).
    ("n1a", "still", S2, None, 18.4, "out",
     "He asked the question he had been\n"
     "carrying, maybe his whole life. Good\n"
     "teacher — what do I have to do to live\n"
     "forever with God? Jesus pointed him to\n"
     "the commandments. Don't cheat anyone.\n"
     "Don't steal. Don't lie. Honor your\n"
     "father and your mother.", "n"),
    ("n1b", "still", S2, None, 19.2, "in",
     "And the young man answered: Teacher,\n"
     "I have kept every one of them since I\n"
     "was a boy. And here is the thing. He\n"
     "meant it. This was not a proud man\n"
     "showing off. This was a student who had\n"
     "done all the homework, kneeling in the\n"
     "dirt, asking if it was enough.", "n"),
    # n2 — the look (v21a). The money beat; music thins under this.
    ("n2a", "still", S3, None, 13.4, "in",
     "Mark writes what happened next in five\n"
     "words. Jesus, looking at him, loved him.\n"
     "Of all the people in Mark's story, this\n"
     "is the one he says it about, straight out.", "n"),
    ("n2b", "still", S3, None, 13.8, "out",
     "Jesus looked at this man — his sincerity,\n"
     "his gold rings, his hope — and loved him.\n"
     "And then, with love in his voice, he said\n"
     "the hardest sentence in the book.", "n"),
    # J1 — exact KJV Mark 10:21, slow and warm, in FULL SILENCE.
    ("j1a", "still", S4, None, 7.8, "in",
     "\u201cOne thing thou lackest: go thy way,\n"
     "sell whatsoever thou hast,\nand give to the poor,\u201d", "kjv"),
    ("j1b", "still", S4, None, 8.0, "out",
     "\u201cand thou shalt have treasure in heaven:\n"
     "and come, take up the cross,\nand follow me.\u201d", "kjv"),
    # n3 — translation bridge (Translation Law: modern meaning only).
    ("n3a", "still", S4, None, 16.0, "in",
     "You're missing one thing. Not one more\n"
     "rule. One thing standing between you\n"
     "and God. Sell what you have. Give it to\n"
     "the people who have nothing. And then —\n"
     "come, follow me.", "n"),
    ("n3b", "still", S3, None, 16.6, "out",
     "Hear that last part. It was an invitation.\n"
     "The same words Jesus used to call Peter,\n"
     "and Andrew, and James, and John. He was\n"
     "being invited into the inner circle. It\n"
     "just came wrapped in the one thing this\n"
     "man could not put down.", "n"),
    # n4 — the turn (s5) + the walk away (s6 clip). v22.
    ("n4a", "still", S5, None, 12.8, "in",
     "His face fell. And he walked away\n"
     "grieved — because he was very rich.\n"
     "Notice what the text does not say. It\n"
     "does not say he stopped believing. It\n"
     "does not say he argued.", "n"),
    ("n4b", "still", S6, None, 12.8, "out",
     "He grieved — because he believed every\n"
     "word, and the price was the thing he\n"
     "loved most. He turned around, and he\n"
     "walked back down that road toward\n"
     "everything he owned.", "n"),
    # n5 — THE PEAK (s7). Music dies HERE and never returns.
    ("n5", "still", S7, None, 16.6, "in",
     "And Jesus let him go. He did not lower\n"
     "the bar. He did not soften the terms.\n"
     "He did not chase him down the road.\n"
     "He stood there, and he watched him walk\n"
     "away — and he loved him the whole time.", "n"),
    # n6 — the coda, in true silence (s8).
    ("n6a", "still", S8, None, 10.0, "out",
     "The road emptied. The sun went down.\n"
     "And the story just ends there — Mark\n"
     "leaves it exactly that sad, on purpose.", "n"),
    ("n6b", "still", S8, None, 10.4, "in",
     "Sit with it. A love that will not force\n"
     "you. Is that weakness — or is it the\n"
     "deepest respect you have ever been\n"
     "shown?", "n"),
    # Card — held 13.6s AND read aloud (Readable-Card Law). In silence.
    ("card", "card", None, None, 13.6, None,
     "Is there something\nyou already know — quietly —\n\n"
     "that stands between you\nand fully following\n"
     "what you believe?",
     "close"),
]

# narration placements: (audio file, absolute start seconds)
# measured dur/tail: n0 27.144/.44  n1 37.128/.57  n2 26.616/.43
#   j1 15.528/1.22  n3 31.752/.42  n4 25.776/.45  n5 14.496/.43
#   n6 18.984/.43  n7 8.688/.45
# breaths 0.8-1.3s between SPOKEN ends; 1.5s held quiet before j1
# (music already fully out); 1.3s held beat before the PEAK n5.
AUDIO = [
    ("audio/n0.mp3", 0.4),     # clip+s2 0-28.0    the run (sp end 27.10)
    ("audio/n1.mp3", 28.2),    # s2 28.0-65.6      question+record (sp 64.76)
    ("audio/n2.mp3", 65.8),    # s3 65.6-92.8      the look (sp 91.99)
    ("audio/j1.mp3", 93.5),    # s4 92.8-108.6     KJV Mark 10:21 (sp 107.81)
    ("audio/n3.mp3", 109.0),   # s4/s3 108.6-141.2 translation bridge (sp 140.33)
    ("audio/n4.mp3", 141.4),   # s5/clip 141.2-166.8 the turn+walk away (sp 166.73)
    ("audio/n5.mp3", 168.0),   # s7 166.8-183.4    PEAK: he let him go (sp 182.07)
    ("audio/n6.mp3", 184.4),   # s8 183.4-203.8    coda in silence (sp 202.95)
    ("audio/n7.mp3", 205.0),   # card 203.8-217.4  closing read (sp 213.24)
]

# Detuned-pair beds — sparse. FULL SILENCE before j1 (93.5). A quiet bed
# under n3-n4 only. Music dies at the start of n5 (168.0) and NEVER
# returns — the pack's law: the ending stays in sorrow, in true silence.
# (start_s, end_s, style) — style "a" = fuller, "b" = quieter/warmer.
BEDS = [
    (0.0, 91.3, "a"),      # run/question/the look; fully out before j1
    (109.5, 167.3, "b"),   # under the bridge + walk away; dies at n5
]


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:160], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


import textwrap


# ---- CAPTION SYSTEM v2 (Cameron, 2026-07-15) — wide bottom, chunked ----
# Captions sit low (y=h-120-text_h) in a strong shadow box and are split
# into short timed chunks so a long narration line never crams the frame.
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


def caption_layers(seg_id, dur, text, style):
    if not text:
        return [], []
    text = " ".join(text.split())
    if style == "kjv":
        font, size, color, width, maxl = SERIF_BI, 46, "0xFFF3DC", 38, 3
    else:
        font, size, color, width, maxl = SERIF, 34, "white", 48, 2
    spoken_end = max(0.6, dur - 0.5)
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
        with open(tf, "w") as f:
            f.write("\n".join(textwrap.wrap(c, width)))
        fo = max(cs, ce - 0.35)
        filters.append(
            f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile={font}:textfile={tf}:fontsize={size}:"
            f"fontcolor={color}:line_spacing=13:x=(w-text_w)/2:"
            f"y=h-120-text_h:"
            f"shadowcolor=black@0.9:shadowx=2:shadowy=2:"
            f"box=1:boxcolor=black@0.55:boxborderw=22,"
            f"fade=t=in:st={cs:.2f}:d=0.35:alpha=1,"
            f"fade=t=out:st={fo:.2f}:d=0.35:alpha=1[cap{seg_id}{i}]")
        labels.append(f"[cap{seg_id}{i}]")
    return filters, labels


def build_still(seg_id, src, dur, zdir, cap, style):
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.10*on/{frames}"
    else:
        z = f"1.101-0.10*on/{frames}"
    # Anti-shimmer law: supersample 4320x7680 -> zoompan at 2160x3840 ->
    # lanczos down to 1080x1920 so every zoom step lands on a quarter-pixel.
    base = (f"[0:v]scale=4320:7680,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ""
    if seg_id == "n0a":       # gentle fade-up to open the video
        tail = ",fade=t=in:st=0:d=1.2"
    if seg_id == "n6b":       # fade to black into the closing card
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    capf, labels = caption_layers(seg_id, dur, cap, style)
    if labels:
        steps, cur = [], "b"
        for i, lab in enumerate(labels):
            last = (i == len(labels) - 1)
            nxt = "v" if last else f"b{i+1}"
            steps.append(f"[{cur}]{lab}overlay=format=auto"
                         + (tail if last else "") + f"[{nxt}]")
            cur = nxt
        fc = f"{base}[b];" + ";".join(capf) + ";" + ";".join(steps)
    else:
        fc = f"{base}{tail}[v]"
    run(["ffmpeg", "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(seg_id, dur, text):
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w") as f:
        f.write(text)
    vf = (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize=50:"
          f"fontcolor={INK}:line_spacing=22:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run(["ffmpeg", "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/{seg_id}.mp4"])


def bed_filter(idx, start, end, style):
    dur = end - start
    if style == "a":
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
               "+0*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))"
               "+0*sin(2*PI*220*t)+0*sin(2*PI*329.63*t)'")
        eq = "lowpass=f=750,tremolo=f=0.13:d=0.3,aecho=0.7:0.4:311|429:0.25|0.18"
        fin, fout = 6, 5
    else:
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
               "+0*(sin(2*PI*138.59*t)+sin(2*PI*139.2*t))"
               "+0*sin(2*PI*164.81*t)+0*sin(2*PI*220*t)'")
        eq = "lowpass=f=700,tremolo=f=0.11:d=0.3,aecho=0.7:0.4:317|443:0.25|0.18"
        fin, fout = 5, 6
    if dur < fin + fout + 2:
        fin = fout = max(2, int((dur - 2) / 2))
    ms = int(start * 1000)
    delay = f",adelay={ms}|{ms}" if ms else ""
    return (f"{src}:s=44100:d={dur},{eq},"
            f"afade=t=in:st=0:d={fin},afade=t=out:st={dur-fout}:d={fout}"
            f"{delay}[mus{idx}]")


def main():
    os.makedirs(S, exist_ok=True)
    total = sum(s[4] for s in SEGMENTS)
    print(f"total runtime: {total:.1f}s", flush=True)

    for seg_id, kind, src, stretch, dur, zdir, cap, style in SEGMENTS:
        if kind == "card":
            build_card(seg_id, dur, cap)
        else:               # stills-only (Law E): every scene is a still now
            build_still(seg_id, src, dur, zdir, cap, style)

    with open(f"{S}/concat.txt", "w") as f:
        for seg in SEGMENTS:
            f.write(f"file '{seg[0]}.mp4'\n")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at absolute offsets + detuned-pair beds ----
    inputs = []
    filters = []
    labels = []
    for i, (path, start) in enumerate(AUDIO):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    for bi, (bs, be, st) in enumerate(BEDS):
        filters.append(bed_filter(bi, bs, be, st))
        labels.append(f"[mus{bi}]")
    n = len(labels)
    filters.append("".join(labels) +
                   f"amix=inputs={n}:duration=longest:normalize=0,"
                   f"apad=whole_dur={total}[aout]")
    run(["ffmpeg", "-y"] + inputs + ["-filter_complex", ";".join(filters),
         "-map", "[aout]", "-t", str(total), "-c:a", "aac", "-b:a", "160k",
         f"{S}/audio_mix.m4a"])

    # ---- loudness law: measure EBU R128, lift toward -15 LUFS ----
    probe = subprocess.run(
        ["ffmpeg", "-i", f"{S}/audio_mix.m4a", "-af", "ebur128", "-f", "null", "-"],
        capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            lufs = float(line.split()[1])
    gain = 0.0
    if lufs is not None:
        gain = max(-6.0, min(10.0, -15.0 - lufs))
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    # ---- final mux: veryslow, runtime-computed rate cap, crf step-up ----
    vcap = max(300, int(24.5 * 8000 / total) - 145)
    size = 0.0
    crf = 21
    for crf in (21, 22, 23, 24, 25):
        run(["ffmpeg", "-y", "-i", f"{S}/video_silent.mp4",
             "-i", f"{S}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "veryslow", "-crf", str(crf),
             "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
             "mark-10_rich-ruler.mp4"])
        size = os.path.getsize("mark-10_rich-ruler.mp4") / 1e6
        if size <= 24.5:
            break
        print(f"  {size:.1f} MB at crf {crf} — over budget, stepping up",
              flush=True)
    print(f"DONE: mark-10_rich-ruler.mp4  {size:.1f} MB, {total:.1f}s "
          f"(crf {crf}, vcap {vcap}k)", flush=True)


if __name__ == "__main__":
    main()
