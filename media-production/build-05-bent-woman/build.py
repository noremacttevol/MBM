#!/usr/bin/env python3
"""Assemble Story Video #5 — The Bent-Over Woman (Luke 13:10-17, FULL story).

Full law stack per PRODUCTION-BIBLE.md + PREFLIGHT.md. Hybrid storybook:
10 painted stills with Ken Burns drift + 1 Veo money-moment clip (the
rising, 8s stretched to 8.4s), edge-tts narration (ear-checked 16/16),
serif captions, KJV red-letter lines, closing question card on cream
#F7F2E9. Assembly Craft Laws: supersampled zoompan (anti-shimmer), RGBA
caption fades, crf-16 intermediates, veryslow crf step-up final, loudness
toward -15 LUFS, detuned-pair music beds.

Two-Voice Law: narrator modern American; Jesus ONLY exact KJV (13:12b,
13:15b-16). Music fully out before BOTH red-letter lines AND before the
peak n5b ("she stood up straight") — the rising happens in sacred quiet.

FULL-STORY law: the ruler's objection (13:14), "glorified God" (13:13)
and the v17 ending (ashamed / all rejoiced) are all restored.

All offsets computed from MEASURED mp3 durations + measured trailing
silence (spoken end = start + dur - tail); breaths 0.8-1.2s, one
intentional ~4s held beat after "he had already decided." (n3).

Output: 1080x1920 H.264 30fps, <25MB, 278.0s.
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

S1 = "s1-eighteen-years.jpeg"
S2 = "s2-back-wall.jpeg"
S3 = "s3-he-stops.jpeg"
S4 = "s4-called-first.jpeg"
S5 = "s5-before-him.jpeg"
CLIP = "s6-she-rises.mp4"
S7 = "s7-glorified-god.jpeg"
S8 = "s8-ruler-objects.jpeg"
S9 = "s9-donkey-watering.jpeg"
S10 = "s10-daughter-of-abraham.jpeg"
S11 = "s11-rejoiced.jpeg"

# (id, kind, source, clip_start, duration_s, zoom_dir, caption, style)
# Boundaries: 0, 18.3, 38.0, 50.4, 67.5, 83.0, 88.4, 104.9, 113.3,
# 127.0, 154.9, 159.2, 181.9, 207.5, 243.6, 264.5, 278.0.
SEGMENTS = [
    # n0 — eighteen years (market, low view).
    ("n0a", "still", S1, 0, 9.1, "in",
     "There was a woman who had been bent\n"
     "over for eighteen years. She could not\n"
     "straighten up at all. Eighteen years\n"
     "of looking at the ground.", "n"),
    ("n0b", "still", S1, 0, 9.2, "out",
     "Eighteen years of knowing people by\n"
     "their sandals instead of their faces.\n"
     "And in all that time, no one had\n"
     "been able to help her.", "n"),
    # n1 — at the back wall.
    ("n1a", "still", S2, 0, 9.8, "in",
     "One sabbath day, Jesus was teaching in\n"
     "a synagogue, and she was there — at the\n"
     "back, by the wall, folded over her\n"
     "walking stick.", "n"),
    ("n1b", "still", S2, 0, 9.9, "out",
     "She had not come to ask him for\n"
     "anything. She was simply there, the way\n"
     "she had been there for years.\n"
     "Present, and unseen.", "n"),
    # n2 — he stops teaching. The frozen hush IS the beat.
    ("n2a", "still", S3, 0, 12.4, "in",
     "And in the middle of his teaching, Jesus\n"
     "stopped. He looked past every face in the\n"
     "room, all the way to the back wall.\n"
     "He saw her. And he called her over.", "n"),
    # n3 — called first. Held beat (~4s) after "already decided."
    ("n3a", "still", S4, 0, 8.5, "in",
     "Notice what did not happen. She did not\n"
     "push through a crowd. She did not call\n"
     "out to him. She did not ask.", "n"),
    ("n3b", "still", S4, 0, 8.6, "out",
     "He called her first. Before she said\n"
     "one word, he had already decided.", "n"),
    # n4 — before him. Sets up j1.
    ("n4a", "still", S5, 0, 7.7, "in",
     "She made her slow way up the middle of\n"
     "that room, her stick tapping the stone\n"
     "floor, every eye on her.", "n"),
    ("n4b", "still", S5, 0, 7.8, "out",
     "And when she finally stood in front of\n"
     "him — still bent, still staring at\n"
     "the ground — he said this.", "n"),
    # J1 — exact KJV Luke 13:12b (music already out).
    ("j1", "still", S5, 0, 5.4, "in",
     "\u201cWoman, thou art loosed\nfrom thine infirmity.\u201d", "kjv"),
    # n5a — the "loosed = untied" study gem.
    ("n5a1", "still", S5, 0, 8.2, "out",
     "Loosed. In their language it was an\n"
     "everyday word. It meant untied — the\n"
     "same word a farmer used when he untied\n"
     "his animal from its stall.", "n"),
    ("n5a2", "still", S5, 0, 8.3, "in",
     "Something that had been knotted\n"
     "for eighteen years was\n"
     "coming undone.", "n"),
    # THE PEAK — she rises. Veo clip, music dead, sacred quiet first.
    ("n5b", "clip", CLIP, 0, 8.4, None,
     "He laid his hands on her. And slowly —\n"
     "for the first time in eighteen years —\n"
     "she stood up straight.", "n"),
    # n6 — she glorified God (13:13, restored).
    ("n6a", "still", S7, 0, 6.8, "in",
     "The first thing she did with a straight\n"
     "back was praise God. Out loud, right\n"
     "there in the middle of the meeting.", "n"),
    ("n6b", "still", S7, 0, 6.9, "out",
     "Eighteen years of silence turned\n"
     "into worship that nobody\n"
     "could stop.", "n"),
    # n7 — the ruler objects (13:14, restored). The WHY of the conflict.
    ("n7a", "still", S8, 0, 9.3, "in",
     "But not everyone rejoiced. The ruler of\n"
     "the synagogue — the man in charge of\n"
     "that meeting — was angry.", "n"),
    ("n7b", "still", S8, 0, 9.3, "out",
     "In his mind, healing counted as work,\n"
     "and the sabbath was the day of rest.\n"
     "There are six working days, he told\n"
     "the crowd. Come and be healed\n"
     "on one of those.", "n"),
    ("n7c", "still", S8, 0, 9.3, "in",
     "As if her freedom could have waited\n"
     "one more day. As if it had not already\n"
     "waited eighteen years.", "n"),
    # n8 — setup j2; the bed dies under this line.
    ("n8", "still", S8, 0, 4.3, "out",
     "Jesus turned to him.\nAnd he did not soften it.", "n"),
    # J2 — exact KJV Luke 13:15b-16, over the donkey-watering still.
    ("j2", "still", S9, 0, 22.7, "in",
     "\u201cThou hypocrite, doth not each one of you\n"
     "on the sabbath loose his ox or his ass\n"
     "from the stall, and lead him away to\n"
     "watering? And ought not this woman, being\n"
     "a daughter of Abraham, whom Satan hath\n"
     "bound, lo, these eighteen years, be loosed\n"
     "from this bond on the sabbath day?\u201d", "kjv"),
    # n9 — their own custom, their own word.
    ("n9a", "still", S9, 0, 12.8, "out",
     "Every man in that room did exactly that\n"
     "on the sabbath. He untied his ox or his\n"
     "donkey and led it to water, and the rules\n"
     "allowed it — simple kindness to an animal\n"
     "was never against the day of rest.", "n"),
    ("n9b", "still", S9, 0, 12.8, "in",
     "So Jesus asked the only question left.\n"
     "If you will untie an animal on the\n"
     "sabbath, how could it be wrong\n"
     "to untie a daughter?", "n"),
    # n10 — daughter of Abraham: worth BEFORE healing (the Seed).
    ("n10a", "still", S10, 0, 12.0, "in",
     "And listen to what he called her.\n"
     "A daughter of Abraham. In that room,\n"
     "those words were a declaration — family\n"
     "of the covenant, a child of the promise.", "n"),
    ("n10b", "still", S10, 0, 12.0, "out",
     "For eighteen years she had been the bent\n"
     "woman, the one people stepped around.\n"
     "Now, in front of everyone, he gave her\n"
     "back her name.", "n"),
    ("n10c", "still", S10, 0, 12.1, "in",
     "And notice the order. He did not say she\n"
     "became a daughter by being healed. She\n"
     "was healed because of who she already\n"
     "was. Her worth came first. She belonged —\n"
     "she had always belonged.", "n"),
    # n11 — verse 17 ending, restored.
    ("n11a", "still", S11, 0, 10.4, "in",
     "Luke tells us how the day ended. The ones\n"
     "who had stood against Jesus were ashamed,\n"
     "and the whole crowd rejoiced at the\n"
     "glorious things he was doing.", "n"),
    ("n11b", "still", S11, 0, 10.5, "out",
     "And somewhere in that crowd stood a woman\n"
     "seeing faces instead of sandals — standing\n"
     "as straight as the truth he had just\n"
     "told about her.", "n"),
    # Card — held 13.5s AND read aloud (Readable-Card Law).
    ("card", "card", None, 0, 13.5, None,
     "Is there something you have\nbeen carrying so long\n"
     "that you have stopped\nexpecting it to change?\n\n"
     "He saw her at the back of the room.\nAnd he called her first.",
     "close"),
]

# narration placements: (audio file, absolute start seconds)
# measured dur/tail: n0 17.448/.421  n1 19.056/.406  n2 11.808/.445
#   n3 13.248/.439  n4 15.504/.455  j1 4.560/1.219  n5a 15.840/.389
#   n5b 7.584/.466  n6 13.128/.439  n7 27.000/.453  n8 3.840/.452
#   j2 22.632/1.172  n9 25.200/.433  n10 35.496/.442  n11 20.208/.440
#   n12 10.368/.460
# breaths 0.8-1.2s between SPOKEN ends; ~4s held beat after n3 (law);
# 1.5s sacred quiet before the PEAK n5b (bed2 fully out at 104.4);
# music dead before j1 (bed1 out 83.2) and j2 (bed3 out 154.6).
AUDIO = [
    ("audio/n0.mp3", 0.4),     # s1 0-18.3       eighteen years (sp 17.43)
    ("audio/n1.mp3", 18.5),    # s2 18.3-38.0    back wall (sp 37.15)
    ("audio/n2.mp3", 38.2),    # s3 38.0-50.4    he stopped (sp 49.56)
    ("audio/n3.mp3", 50.6),    # s4 50.4-67.5    called first (sp 63.41) + HELD BEAT
    ("audio/n4.mp3", 67.7),    # s5 67.5-83.0    before him (sp 82.75)
    ("audio/j1.mp3", 84.2),    # s5 83.0-88.4    KJV 13:12b (sp 87.54)
    ("audio/n5a.mp3", 88.6),   # s5 88.4-104.9   loosed = untied (sp 104.05)
    # 1.5s sacred quiet — bed2 fully out at 104.4, clip motion alone
    ("audio/n5b.mp3", 105.9),  # clip 104.9-113.3 THE PEAK (sp 113.02)
    ("audio/n6.mp3", 113.5),   # s7 113.3-127.0  glorified God (sp 126.19)
    ("audio/n7.mp3", 127.2),   # s8 127.0-154.9  ruler objects (sp 153.75)
    ("audio/n8.mp3", 155.1),   # s8 154.9-159.2  didn't soften it (sp 158.49)
    ("audio/j2.mp3", 159.4),   # s9 159.2-181.9  KJV 13:15b-16 (sp 180.86)
    ("audio/n9.mp3", 181.9),   # s9 181.9-207.5  untie a daughter (sp 206.67)
    ("audio/n10.mp3", 207.7),  # s10 207.5-243.6 daughter of Abraham (sp 242.75)
    ("audio/n11.mp3", 243.8),  # s11 243.6-264.5 ashamed / rejoiced (sp 263.57)
    ("audio/n12.mp3", 264.8),  # card 264.5-278.0 closing read (sp 274.71)
]

# Detuned-pair beds — fully out before j1, j2 AND the peak n5b.
# (start_s, end_s, style) — style "a" = fuller, "b" = quieter/warmer.
BEDS = [
    (0.0, 83.2, "a"),      # market/synagogue/called; out before J1 (84.2)
    (89.0, 104.4, "b"),    # under the untied gem; PEAK rises in SILENCE
    (113.6, 154.6, "b"),   # praise + ruler; dies under n8; J2 in quiet
    (182.4, 274.0, "b"),   # bridge/daughter/rejoiced/closing card
]


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:160], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


def caption_overlay(seg_id, dur, text, style):
    """Caption on its own transparent RGBA canvas, alpha-faded 0.5s in/out,
    gone 0.1s before the cut — captions never pop (Assembly Craft Laws)."""
    if not text:
        return None
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w") as f:
        f.write(text)
    if style == "kjv":
        font, size, color = SERIF_BI, 46, "0xFFF3DC"
    else:
        font, size, color = SERIF, 40, "white"
    fade_out = max(0.0, dur - 0.6)
    return (f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile={font}:textfile={tf}:fontsize={size}:"
            f"fontcolor={color}:line_spacing=14:x=(w-text_w)/2:y=h-460:"
            f"shadowcolor=black@0.85:shadowx=2:shadowy=2:"
            f"box=1:boxcolor=black@0.30:boxborderw=18,"
            f"fade=t=in:st=0:d=0.5:alpha=1,"
            f"fade=t=out:st={fade_out}:d=0.5:alpha=1[cap]")


def assemble_segment(seg_id, base_chain, dur, cap, style, tail=""):
    capf = caption_overlay(seg_id, dur, cap, style)
    if capf:
        fc = (f"{base_chain}[base];{capf};"
              f"[base][cap]overlay=format=auto{tail}[v]")
    else:
        fc = f"{base_chain}{tail}[v]"
    return fc


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
    if seg_id == "n0a":
        tail = ",fade=t=in:st=0:d=1.2"
    if seg_id == "n11b":
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    fc = assemble_segment(seg_id, base, dur, cap, style, tail)
    run(["ffmpeg", "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_clip(seg_id, src, start, dur, cap, style):
    """Veo clip stretched 1.05x (8s -> 8.4s) so the slow unbending of the
    spine carries the whole peak without a hard cut mid-motion."""
    base = (f"[0:v]setpts=1.05*PTS,scale=1080:1920:flags=lanczos,setsar=1,"
            f"fps={FPS},unsharp=5:5:0.35:5:5:0.0")
    fc = assemble_segment(seg_id, base, dur, cap, style)
    run(["ffmpeg", "-y", "-ss", str(start), "-i", f"{A}/{src}",
         "-t", str(dur + 1), "-filter_complex", fc, "-map", "[v]", "-t",
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

    for seg_id, kind, src, cstart, dur, zdir, cap, style in SEGMENTS:
        if kind == "still":
            build_still(seg_id, src, dur, zdir, cap, style)
        elif kind == "clip":
            build_clip(seg_id, src, cstart, dur, cap, style)
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
             "-c:v", "libx264", "-preset", "veryslow", "-crf", str(crf),
             "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
             "bent-woman-05.mp4"])
        size = os.path.getsize("bent-woman-05.mp4") / 1e6
        if size <= 24.5:
            break
        print(f"  {size:.1f} MB at crf {crf} — over budget, stepping up",
              flush=True)
    print(f"DONE: bent-woman-05.mp4  {size:.1f} MB, {total:.1f}s "
          f"(crf {crf}, vcap {vcap}k)", flush=True)


if __name__ == "__main__":
    main()
