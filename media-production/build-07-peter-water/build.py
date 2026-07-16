#!/usr/bin/env python3
"""Assemble Story Video #7 — Peter Walks on Water (Matthew 14:22-33, FULL).

Full law stack per PRODUCTION-BIBLE.md + PREFLIGHT.md. Hybrid storybook:
10 painted stills with Ken Burns drift + 2 Veo money-moment clips (the
walking, 8s stretched to 12.8s — Leighton's crown jewel; the sinking, 8s
stretched to 10.8s), edge-tts narration (ear-checked 15/15), serif
captions, KJV red-letter lines, closing question card on cream #F7F2E9.
Assembly Craft Laws: supersampled zoompan (anti-shimmer), RGBA caption
fades, crf-16 intermediates, veryslow crf step-up final, loudness toward
-15 LUFS, detuned-pair music beds.

Two-Voice Law: narrator modern American; Jesus ONLY exact KJV (14:27,
14:29a "Come.", 14:31b). Music fully out before j1, before j2 (the word
"Come" lands utterly alone in the dark — Leighton's crew call), and dies
on the narrator's "immediately" — dead through n7 + j3 + n8 bridge.

FULL-STORY law: v22-23 (praying alone — the WHY), v26 ("It is a spirit"),
and v32-33 (wind ceasing + "Of a truth thou art the Son of God") restored.

All offsets computed from MEASURED mp3 durations + measured trailing
silence (spoken end = start + dur - tail); breaths 0.8-1.2s; 1.6s dark
hold before "Come." and a 2.2s held breath after (No-Dead-Air <=2.5s).

Output: 1080x1920 H.264 30fps, <25MB, 256.0s.
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

# 2026-07-11 REDO (Machine C): pictures-only (no AI clips) + Jesus face NEVER shown,
# no glow, real Middle Eastern man from behind. All Jesus stills regenerated under
# The Standing Laws. The two former Veo clips (walking, sinking) are now stills.
S1 = "s1-mountain-prayer.jpeg"      # v3 face-shown: Jesus prays, face lifted, moonlit mountain
S2 = "s2-boat-storm.jpeg"           # disciples' boat in the storm (boat/crew lock)
S3 = "s3-figure-on-water.jpeg"      # Jesus distant on the water, terrified disciples in foreground
S4 = "s4-over-gunwale.jpeg"         # they cry "it is a spirit" — crew pointing (boat/crew lock)
WALK = "s5-walk.jpeg"               # v3 face-shown: Peter walks toward Jesus on the water
S6 = "s6-eyes-on-waves.jpeg"        # Peter doubts, faltering on the water
SINK = "s7-sink.jpeg"               # v3 face-shown: Peter sinks, Jesus reaches and grips his wrist
S8 = "s8-catch.jpeg"                # v3 face-shown: the catch, held above the water (distinct still)
S9 = "s9-walk-back.jpeg"            # v3 face-shown: Jesus & Peter walk back to the boat together
S10 = "s10-calm-sea.jpeg"           # wide calm moonlit sea, the boat at rest (boat/crew lock)
S11 = "s11-worship.jpeg"            # v3 face-shown: Jesus among the kneeling, worshipping disciples
S12 = "s12-worship.jpeg"            # v3 face-shown: closing worship, Jesus at the boat's center

# (id, kind, source, stretch_or_none, duration_s, zoom_dir, caption, style)
# Boundaries: 0, 26.7, 52.0, 78.9, 113.8, 126.6, 135.8, 146.6, 197.5,
# 206.3, 214.6, 228.4, 242.0, 256.0.
SEGMENTS = [
    # n0 — the sending + the mountain (v22-23, the restored WHY).
    ("n0a", "still", S1, None, 13.3, "in",
     "Jesus had just fed more than five thousand\n"
     "people with a few loaves of bread and two\n"
     "small fish. And when it was done, he told\n"
     "his disciples to take the boat and cross\n"
     "the lake ahead of him.", "n"),
    ("n0b", "still", S1, None, 13.4, "out",
     "He sent the crowds home. And then he\n"
     "climbed a mountain, alone, to pray. That\n"
     "is where the night found him. Not in the\n"
     "boat. On the mountain, talking with\n"
     "his Father.", "n"),
    # n1 — the storm + fourth-watch gem (v24-25).
    ("n1a", "still", S2, None, 12.6, "in",
     "Out on the water, the wind turned against\n"
     "the boat. The waves rose. The disciples —\n"
     "several of them fishermen who had worked\n"
     "this lake their whole lives — rowed\n"
     "against it for hours.", "n"),
    ("n1b", "still", S2, None, 12.7, "out",
     "Matthew tells us it was the fourth watch\n"
     "of the night when help came. That means\n"
     "between three and six in the morning.\n"
     "They had been fighting that sea\n"
     "nearly all night.", "n"),
    # n2 — the figure on the water; "It is a spirit" terror (v25-26).
    ("n2a", "still", S3, None, 10.7, "in",
     "And then, through the spray and the dark,\n"
     "they saw something that made grown\n"
     "fishermen scream. A figure. Walking\n"
     "toward them. On top of the water.", "n"),
    ("n2b", "still", S3, None, 10.8, "out",
     "They cried out that it was a ghost —\n"
     "because nobody walks on the sea.\n"
     "But the voice that came back across\n"
     "the water was one they knew.", "n"),
    # J1 — exact KJV Matthew 14:27 (music already out).
    ("j1", "still", S3, None, 5.4, "in",
     "\u201cBe of good cheer; it is I;\nbe not afraid.\u201d", "kjv"),
    # n3 — translation bridge + Peter's ask (v28).
    ("n3a", "still", S4, None, 11.4, "in",
     "Take heart. It's me. Don't be afraid.\n"
     "And Peter — impulsive, big-hearted\n"
     "Peter — called back across the storm:\n"
     "Lord, if it's really you, tell me to\n"
     "come to you on the water.", "n"),
    ("n3b", "still", S4, None, 11.9, "out",
     "Think about what he was asking for.\n"
     "Not for the storm to stop. To come\n"
     "out into it — to where Jesus stood.", "n"),
    # J2 — exact KJV Matthew 14:29a. One word, alone in the dark
    # (Leighton's crew call: held silence, long breath after).
    ("j2", "still", S4, None, 4.6, "in",
     "\u201cCome.\u201d", "kjv"),
    # n4a — the leg over the side (still): the decision.
    ("n4a", "still", S4, None, 7.0, "out",
     "One word. And Peter put his leg\n"
     "over the side of that pitching boat,\n"
     "and stood up on the sea.", "n"),
    # THE MONEY MOMENT — Peter walking on the sea. (Redo: still, Ken Burns.)
    ("n4b", "still", WALK, None, 12.8, "in",
     "And he was doing it. Step after step\n"
     "on the moving water, his eyes fixed\n"
     "on Jesus. For a moment, an ordinary\n"
     "fisherman walked where only God\n"
     "can walk.", "n"),
    # n5a — the turn (v30a).
    ("n5a", "still", S6, None, 9.2, "in",
     "Then he noticed the wind tearing at him.\n"
     "He looked down at the waves instead\n"
     "of ahead at Jesus.", "n"),
    # The sinking (v30b). (Redo: still, Ken Burns.)
    ("n5b", "still", SINK, None, 10.8, "out",
     "And the moment his eyes moved, the\n"
     "water stopped holding him. He dropped\n"
     "to his waist, mid-stride, and cried out\n"
     "the shortest prayer in the Bible:\n"
     "Lord, save me.", "n"),
    # n6 — THE CATCH (v31a). Music dies on "immediately."
    ("n6", "still", S8, None, 3.6, "in",
     "And Jesus caught him.\nImmediately.", "n"),
    # n7 — grip first, question second (in the silence).
    ("n7a", "still", S8, None, 10.0, "out",
     "Matthew uses that exact word. There was\n"
     "no pause. No lesson first. No letting him\n"
     "go under to teach him something.", "n"),
    ("n7b", "still", S8, None, 10.1, "in",
     "The hand was there before the prayer\n"
     "was finished. And from that grip —\n"
     "holding him above the water — Jesus\n"
     "asked him one question.", "n"),
    # J3 — exact KJV Matthew 14:31b. THE PEAK, in dead silence.
    ("j3", "still", S8, None, 5.0, "in",
     "\u201cO thou of little faith,\nwherefore didst thou doubt?\u201d", "kjv"),
    # n8 — translation bridge (still in silence).
    ("n8a", "still", S8, None, 11.0, "out",
     "Why did you doubt? Hear how he asked it.\n"
     "Not from the shore. Not after pulling him\n"
     "into the boat. From the hand already\n"
     "holding him.", "n"),
    ("n8b", "still", S8, None, 11.2, "in",
     "It isn't a scolding. It's a real question,\n"
     "from someone who had already caught\n"
     "him — as if to say: you were doing it.\n"
     "What made you stop trusting me?", "n"),
    # n9 — back to the boat, the wind ceases (v32).
    ("n9a", "still", S9, None, 8.8, "in",
     "The two of them came back to the boat\n"
     "across the water together. And the\n"
     "moment they climbed in, the wind\n"
     "stopped.", "n"),
    ("n9b", "still", S10, None, 8.3, "out",
     "Not slowly. Not eventually. The sea\n"
     "that had fought them all night simply\n"
     "lay down flat under the stars.", "n"),
    # n10 — the worship (v33).
    ("n10a", "still", S11, None, 13.8, "in",
     "And the men in that boat — the same men\n"
     "who minutes earlier had screamed that he\n"
     "was a ghost — knelt down where they sat,\n"
     "soaked and shaking, and worshipped him.", "n"),
    ("n10b", "still", S12, None, 13.6, "out",
     "You really are the Son of God, they said.\n"
     "The storm had taught them who he was.\n"
     "And notice what the story remembers\n"
     "about Peter. Not that he sank. That he\n"
     "walked. And that when he fell, he\n"
     "was caught.", "n"),
    # Card — held 14.0s AND read aloud (Readable-Card Law).
    ("card", "card", None, None, 14.0, None,
     "When your storm gets loud\nand your faith slips,\n"
     "look back up —\n\nthe same hand is already\nreaching for you.\n\n"
     "Keep your eyes on him.",
     "close"),
]

# narration placements: (audio file, absolute start seconds)
# measured dur/tail: n0 26.040/.441  n1 24.816/.422  n2 20.472/.384
#   j1 5.400/1.092  n3 23.328/.425  j2 2.040/1.219  n4 19.344/.435
#   n5 19.512/.404  n6 3.144/.407  n7 19.104/.414  j3 5.160/1.103
#   n8 21.672/.424  n9 16.632/.436  n10 26.856/.429  n11 10.056/.469
# breaths 0.8-1.2s between SPOKEN ends; 1.6s dark hold before j2 and a
# 2.2s held breath after it (No-Dead-Air <=2.5s); 1.4s dead quiet
# before the PEAK j3; music out before j1 (73.9), j2 (103.8), and dead
# from "immediately" (~149.0) through j3 + bridge.
AUDIO = [
    ("audio/n0.mp3", 0.4),     # s1 0-26.7        sending+mountain (sp 26.00)
    ("audio/n1.mp3", 26.9),    # s2 26.7-52.0     storm+fourth watch (sp 51.29)
    ("audio/n2.mp3", 52.2),    # s3 52.0-73.5     "It is a spirit" (sp 72.29)
    ("audio/j1.mp3", 73.9),    # s3 73.5-78.9     KJV 14:27 (sp 78.21)
    ("audio/n3.mp3", 79.1),    # s4 78.9-102.2    bridge+Peter's ask (sp 102.00)
    ("audio/j2.mp3", 103.8),   # s4 102.2-106.8   KJV "Come." (sp 104.62) + HELD BREATH
    ("audio/n4.mp3", 107.0),   # s4/clip 106.8-126.6  he was doing it (sp 125.91)
    ("audio/n5.mp3", 126.8),   # s6/clip 126.6-146.6  the turn + sinking (sp 145.91)
    ("audio/n6.mp3", 146.8),   # s8 146.6-150.2   caught. Immediately. (sp 149.54)
    ("audio/n7.mp3", 150.4),   # s8 150.2-170.3   grip first (sp 169.09)
    ("audio/j3.mp3", 170.5),   # s8 170.3-175.3   KJV 14:31b PEAK (sp 174.56)
    ("audio/n8.mp3", 175.5),   # s8 175.3-197.5   why did you doubt (sp 196.75)
    ("audio/n9.mp3", 197.7),   # s9/s10 197.5-214.6  wind ceased (sp 213.90)
    ("audio/n10.mp3", 214.8),  # s11/s12 214.6-242.0 worship (sp 241.23)
    ("audio/n11.mp3", 242.9),  # card 242.0-256.0 closing read (sp 252.49)
]

# Detuned-pair beds — fully out before j1 and j2; die on "immediately"
# (~149.0) and stay DEAD through n7 + j3 + n8 (the peak lives in silence).
# (start_s, end_s, style) — style "a" = fuller, "b" = quieter/warmer.
BEDS = [
    (0.0, 72.7, "a"),      # mountain/storm/spirit; out before J1 (73.9)
    (79.5, 102.6, "b"),    # under Peter's ask; "Come." lands utterly alone
    (107.5, 149.0, "b"),   # walking + sinking; dies on "immediately"
    (198.5, 254.5, "b"),   # calm/worship/closing card
]


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:160], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


import textwrap


# ---- CAPTION SYSTEM v2 (Cameron, 2026-07-15) — wide bottom, chunked ----
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
    text = " ".join(text.split())  # collapse the old manual line breaks
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
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ""
    if seg_id == "n0a":
        tail = ",fade=t=in:st=0:d=1.2"
    if seg_id == "n10b":
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


def build_clip(seg_id, src, stretch, dur, cap, style):
    """Veo clip stretched (8s -> dur) so the money motion carries its whole
    beat without a hard cut mid-motion. Walking = 1.6x (Leighton's crown
    jewel gets the long, slow treatment); sinking = 1.35x."""
    base = (f"[0:v]setpts={stretch}*PTS,scale=1080:1920:flags=lanczos,"
            f"setsar=1,fps={FPS},unsharp=5:5:0.35:5:5:0.0")
    fc = assemble_segment(seg_id, base, dur, cap, style)
    run(["ffmpeg", "-y", "-i", f"{A}/{src}",
         "-filter_complex", fc, "-map", "[v]", "-t",
         str(dur)] + ENC + [f"{S}/{seg_id}.mp4"])


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
        if kind == "still":
            build_still(seg_id, src, dur, zdir, cap, style)
        elif kind == "clip":
            build_clip(seg_id, src, stretch, dur, cap, style)
        else:
            build_card(seg_id, dur, cap)

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
             "-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
             "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
             "matthew-14_peter-walks-on-water.mp4"])
        size = os.path.getsize("matthew-14_peter-walks-on-water.mp4") / 1e6
        if size <= 24.5:
            break
        print(f"  {size:.1f} MB at crf {crf} — over budget, stepping up",
              flush=True)
    print(f"DONE: matthew-14_peter-walks-on-water.mp4  {size:.1f} MB, {total:.1f}s "
          f"(crf {crf}, vcap {vcap}k)", flush=True)


if __name__ == "__main__":
    main()
