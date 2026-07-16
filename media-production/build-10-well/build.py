#!/usr/bin/env python3
"""Assemble Story Video #10 — The Woman at the Well (John 4:4-30, 39-42).

Full law stack per PRODUCTION-BIBLE.md + PREFLIGHT.md. Hybrid storybook:
9 painted stills with Ken Burns drift + 2 Veo money-moment clips (the
conversation — her face moving from guarded to undone, 8s stretched to
12.8s; the jar left behind — she runs toward the town, 8s stretched to
12.8s), edge-tts narration (ear-checked 13/13), serif captions, KJV
red-letter j1 (John 4:13-14 exact) and j2 (John 4:26 exact), closing
question card on cream #F7F2E9. Assembly Craft Laws: supersampled
zoompan (anti-shimmer), RGBA caption fades, crf-16 intermediates,
veryslow crf step-up final, loudness toward -15 LUFS, detuned-pair beds.

Two-Voice Law: narrator modern American; Jesus ONLY exact KJV.
Music map (the pack's law): beds under n0-n3, FULL SILENCE before j1;
a quiet bed under the bridge and early conversation that DIES before
"he did not turn away" (~164s); j2 "I am he" in true silence; a warm
bed returns for the disciples / the run / the harvest (216-295) and is
fully out before the closing card, which is read in silence.

All offsets computed from MEASURED mp3 durations + measured trailing
silence (spoken end = start + last_silence_start); breaths 0.8-1.6s.

Output: john-4_woman-at-the-well.mp4 (SCRIPTURE-NAME LAW),
1080x1920 H.264 30fps, <25MB, 311.0s.
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

S1 = "s1-noon-path.jpeg"
S2 = "s2-traveler.jpeg"
S3 = "s3-disbelief.jpeg"
S4 = "s4-living-water.jpeg"
S5 = "s5-conversation-anchor.jpeg"
S6 = "s6-disciples.jpeg"
S7 = "s7-jar-left-anchor.jpeg"
S8 = "s8-come-and-see.jpeg"
S9 = "s9-road-filling.jpeg"
CLIP_CONV = "s5-conversation.mp4"
CLIP_JAR = "s7-jar-run.mp4"

# (id, kind, source, stretch_or_none, duration_s, zoom_dir, caption, style)
# Boundaries: 0, 15.5, 31.0, 45.3, 59.6, 76.6, 93.4, 110.0, 118.5, 127.0,
# 142.6, 155.4, 179.8, 195.3, 210.8, 215.8, 230.2, 244.6, 257.4, 268.4,
# 282.4, 297.0, 311.0.
SEGMENTS = [
    # n0 — noon, alone on purpose (s1). The WHY-gem about the hour.
    ("n0a", "still", S1, None, 15.5, "in",
     "A woman walked out to a well at noon —\n"
     "the hottest, emptiest hour of the day.\n"
     "You need to understand what that hour\n"
     "means. Women drew their water in the\n"
     "cool of the morning, together. It was\n"
     "where the talk happened.", "n"),
    ("n0b", "still", S1, None, 15.5, "out",
     "She came at noon because of the talk.\n"
     "Five marriages behind her, living now\n"
     "with a man who wasn't her husband — and\n"
     "the whole town knew every chapter. Noon\n"
     "was the hour with nobody in it. She\n"
     "chose it on purpose.", "n"),
    # n1 — the traveler (s2). Seven hundred years of contempt.
    ("n1a", "still", S2, None, 14.3, "in",
     "But this day, somebody was there. A\n"
     "traveler sat by the well, worn out from\n"
     "the road — a Jewish man, resting in\n"
     "Samaria. That detail matters more than\n"
     "it sounds.", "n"),
    ("n1b", "still", S2, None, 14.3, "out",
     "Jews and Samaritans had despised each\n"
     "other for seven hundred years. They\n"
     "didn't share roads if they could help\n"
     "it, didn't share tables, and certainly\n"
     "didn't share water. Everything in her\n"
     "body said: turn around.", "n"),
    # n2 — he asked HER (s3). The double wall broken in one sentence.
    ("n2a", "still", S3, None, 17.0, "in",
     "Then he spoke to her. He asked her for\n"
     "a drink. Understand how impossible that\n"
     "sentence was. A rabbi did not speak to\n"
     "an unknown woman in public — and no Jew\n"
     "asked a Samaritan for anything.", "n"),
    ("n2b", "still", S3, None, 16.8, "out",
     "He broke both walls at once, and he did\n"
     "it by needing her help. She almost\n"
     "laughed. How is it that you, a Jew,\n"
     "would ask me for water? And he answered\n"
     "that if she knew who was asking, she\n"
     "would have asked him — and he would\n"
     "have given her living water.", "n"),
    # n3 — setup for the KJV line (s4). Music thins to silence under this.
    ("n3", "still", S4, None, 16.6, "in",
     "She pointed out the obvious — the well\n"
     "is deep, sir, and you don't even have a\n"
     "rope. This well came from Jacob himself.\n"
     "Are you greater than Jacob? She meant it\n"
     "as a corner. He stepped right into it.", "n"),
    # J1 — exact KJV John 4:13-14. Slow, warm, in FULL SILENCE.
    ("j1a", "still", S4, None, 8.5, "in",
     "\u201cWhosoever drinketh of this water\n"
     "shall thirst again: But whosoever\n"
     "drinketh of the water that I shall give\n"
     "him shall never thirst;\u201d", "kjv"),
    ("j1b", "still", S4, None, 8.5, "out",
     "\u201cbut the water that I shall give him\n"
     "shall be in him a well of water\n"
     "springing up into everlasting life.\u201d", "kjv"),
    # n4 — translation bridge (Translation Law: modern meaning only).
    ("n4", "still", S4, None, 15.6, "out",
     "A well inside you — springing up, not\n"
     "running dry. He wasn't talking about\n"
     "the water in the jar. He was talking\n"
     "about the thirst underneath the thirst.\n"
     "The one you can't carry a jar big\n"
     "enough for.", "n"),
    # n5 — her whole life, and he stayed (s5 clip — THE PEAK).
    # Music dies before "he did not turn away."
    ("n5a", "still", S5, None, 12.8, "in",
     "Then he said: go get your husband. And\n"
     "the whole conversation changed. I have\n"
     "no husband, she said. And he agreed\n"
     "with her — gently, and completely.", "n"),
    ("n5b", "still", S5, None, 24.4, "in",
     "Five husbands, he said. And the man you\n"
     "have now is not one. He already knew.\n"
     "All of it. Every chapter the town\n"
     "whispered about — he said it out loud,\n"
     "to her face. And he did not turn away.\n"
     "He stayed in the conversation. She came\n"
     "for water, and found herself fully\n"
     "known — and still spoken to with respect.", "n"),
    # n6 — worship summary + Messiah setup (s5 tail).
    ("n6a", "still", S5, None, 15.5, "out",
     "She called him a prophet. She asked him\n"
     "her people's oldest question — which\n"
     "mountain is the right one to worship\n"
     "on — and he told her the day was coming\n"
     "when the question itself would be old\n"
     "news:", "n"),
    ("n6b", "still", S5, None, 15.5, "in",
     "God is spirit, and what he wants is the\n"
     "heart. Then she said, almost to herself:\n"
     "I know the Messiah is coming. When he\n"
     "comes, he'll explain everything. And the\n"
     "tired traveler at the well said:", "n"),
    # J2 — exact KJV John 4:26, in true silence.
    ("j2", "still", S5, None, 5.0, "out",
     "\u201cI that speak unto thee am he.\u201d", "kjv"),
    # n7 — who he told first (s6 — disciples return, marveling).
    ("n7a", "still", S6, None, 14.4, "in",
     "The first person Jesus ever told plainly\n"
     "that he was the Messiah — not a king,\n"
     "not a priest, not even one of his\n"
     "twelve — a Samaritan woman with five\n"
     "marriages behind her, at the bottom of\n"
     "every list her world kept.", "n"),
    ("n7b", "still", S6, None, 14.4, "out",
     "Right then his followers came back from\n"
     "town, and stopped short — stunned that\n"
     "he was talking with her at all. Nobody\n"
     "dared say a word.", "n"),
    # n8 — the jar left behind. STILL FIRST to sell the moment, THEN the
    # motion clip that pays it off (Cameron's Correction #10, 2026-07-10).
    ("n8a", "still", S7, None, 11.0, "in",
     "And look what she did. She left the jar.\n"
     "The thing she walked all that way in\n"
     "the heat to fill — she left it standing\n"
     "at the well, and she ran.", "n"),
    ("n8b", "still", S8, None, 12.8, "in",
     "Ran toward the town she had spent years\n"
     "avoiding, to the very people she came\n"
     "out at noon to miss, shouting: come see\n"
     "a man who told me everything I ever did.", "n"),
    # n9 — the harvest (s8 -> s9). vv30, 39-42 in modern words.
    ("n9a", "still", S9, None, 14.0, "in",
     "And they came. The town that whispered\n"
     "about her followed her up the road to\n"
     "see for themselves. Many believed\n"
     "because of her word —", "n"),
    ("n9b", "still", S9, None, 14.6, "out",
     "the woman who wouldn't meet their eyes\n"
     "at sunrise became the first missionary\n"
     "in that gospel by sundown. They asked\n"
     "him to stay, and he stayed two days —\n"
     "with Samaritans. And they told her: now\n"
     "we've heard him ourselves. We know.", "n"),
    # Card — held 14.0s AND read aloud (Readable-Card Law). In silence.
    ("card", "card", None, None, 14.0, None,
     "She came for one thing,\nand found out she was thirsty\n"
     "for something much deeper.\n\n"
     "Have you ever been searching\nfor something — and realized later\n"
     "it was deeper than what you\nthought you wanted?",
     "close"),
]

# narration placements: (audio file, absolute start seconds)
# measured dur/last_silence_start: n0 30.552/30.12  n1 27.888/27.45
#   n2 33.024/32.57  n3 15.432/15.00  j1 16.872/15.63  n4 14.880/14.44
#   n5 36.240/35.80  n6 30.288/29.84  j2 3.720/2.50  n7 27.888/27.45
#   n8 22.464/22.05  n9 27.432/27.01  n10 12.960/12.52
# breaths 0.8-1.6s between SPOKEN ends; 1.5s held quiet before j1 and j2.
AUDIO = [
    ("audio/n0.mp3", 0.4),     # s1 0-31.0        noon alone (sp end 30.52)
    ("audio/n1.mp3", 31.4),    # s2 31.0-59.6     the traveler (sp 58.85)
    ("audio/n2.mp3", 60.0),    # s3 59.6-93.4     he asked HER (sp 92.57)
    ("audio/n3.mp3", 93.8),    # s4 93.4-110.0    Jacob's well (sp 108.80)
    ("audio/j1.mp3", 110.3),   # s4 110.0-127.0   KJV John 4:13-14 (sp 125.93)
    ("audio/n4.mp3", 127.2),   # s4 127.0-142.6   translation bridge (sp 141.64)
    ("audio/n5.mp3", 142.8),   # clip+s5 142.6-179.8  THE PEAK (sp 178.60)
    ("audio/n6.mp3", 180.0),   # s5 179.8-210.8   worship+Messiah (sp 209.84)
    ("audio/j2.mp3", 211.6),   # s5 210.8-215.8   KJV John 4:26 (sp 214.10)
    ("audio/n7.mp3", 216.0),   # s6 215.8-244.6   who he told first (sp 243.45)
    ("audio/n8.mp3", 244.8),   # clip+s7 244.6-268.4  the jar left (sp 266.85)
    ("audio/n9.mp3", 268.6),   # s8/s9 268.4-297.0    the harvest (sp 295.61)
    ("audio/n10.mp3", 297.8),  # card 297.0-311.0     closing read (sp 310.32)
]

# Detuned-pair beds. FULL SILENCE before j1 (110.3). Quiet bed under the
# bridge + early conversation, DEAD before "he did not turn away" (~164.3
# in n5b). j2 in silence. A warm bed returns for disciples/run/harvest and
# is fully out before the card is read.
# (start_s, end_s, style) — style "a" = fuller, "b" = quieter/warmer.
BEDS = [
    (0.0, 108.0, "a"),       # noon/traveler/asked-her; fully out before j1
    (127.5, 164.0, "b"),     # bridge + conversation; dies before the peak line
    (216.0, 295.0, "a"),     # disciples/the run/the harvest; out before card
]


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:160], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


import textwrap


# ---- CAPTION SYSTEM v2 (Cameron, 2026-07-15) — wide bottom, chunked ----
# Captions sit low (y=h-120-text_h) in a strong shadow box, split into short
# timed chunks so a long narration line never crams the frame.
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
    if seg_id == "n9b":       # fade to black into the closing card
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
        src = ("aevalsrc='0.022*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
               "+0.016*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))"
               "+0.012*sin(2*PI*220*t)+0.008*sin(2*PI*329.63*t)'")
        eq = "lowpass=f=750,tremolo=f=0.13:d=0.3,aecho=0.7:0.4:311|429:0.25|0.18"
        fin, fout = 6, 5
    else:
        src = ("aevalsrc='0.014*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
               "+0.011*(sin(2*PI*138.59*t)+sin(2*PI*139.2*t))"
               "+0.009*sin(2*PI*164.81*t)+0.006*sin(2*PI*220*t)'")
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
    OUT = "john-4_woman-at-the-well.mp4"   # SCRIPTURE-NAME LAW
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
             OUT])
        size = os.path.getsize(OUT) / 1e6
        if size <= 24.5:
            break
        print(f"  {size:.1f} MB at crf {crf} — over budget, stepping up",
              flush=True)
    print(f"DONE: {OUT}  {size:.1f} MB, {total:.1f}s "
          f"(crf {crf}, vcap {vcap}k)", flush=True)


if __name__ == "__main__":
    main()
