#!/usr/bin/env python3
"""Assemble Story Video #4 — Nicodemus at Night (John 3; arc to 7:50-51, 19:39).

Full law stack per PRODUCTION-BIBLE.md + PREFLIGHT.md. Hybrid storybook:
10 painted stills with Ken Burns drift + 1 Veo money-moment clip (the
street hesitation, stretched 8->8.4s), edge-tts narration (ear-checked
18/18), serif captions, KJV red-letter lines, closing question card on
cream #F7F2E9. Assembly Craft Laws: supersampled zoompan (anti-shimmer),
RGBA caption fades, crf-16 intermediates, veryslow crf step-up final,
loudness toward -15 LUFS, detuned-pair music beds.

Two-Voice Law: narrator modern American; Jesus ONLY exact KJV (3:3, 3:8,
3:16-17). Music fully out before EVERY red-letter line; THE PEAK (3:16-17)
lands after 2.1s of sacred quiet with no bed anywhere near it.

FULL-STORY law: the arc runs past John 3 to the council defense (7:50-51)
and the hundred-pound royal burial (19:39) — the invented "walks home
changed" ending from the 60s pack is gone.

All offsets computed from MEASURED mp3 durations + measured trailing
silence (spoken end = start + dur - tail); breaths 0.8-1.2s, one
intentional 6.3s held beat on "So he came at night." (the pack's law).

Output: 1080x1920 H.264 30fps, <25MB, 366.6s.
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

S1 = "s1-chamber.jpeg"
STILL_STREET = "Elderly_man_walks_Jerusalem_street_202607111625.jpeg"  # was s2-street.mp4 (Phase-1 stills-only)
S3 = "s3-threshold.jpeg"
S4 = "s4-conversation.jpeg"
S5 = "s5-womb-question.jpeg"
S6 = "s6-wind.jpeg"
S7 = "s7-face.jpeg"
S8 = "s8-lamplight-wide.jpeg"
S9 = "s9-leaving.jpeg"
S10 = "s10-council.jpeg"
S11 = "s11-spices.jpeg"

# (id, kind, source, clip_start, duration_s, zoom_dir, caption, style)
# Boundaries: 0, 27.2, 35.6, 68.9, 84.4, 94.0, 105.0, 116.0, 129.0,
# 142.0, 155.2, 172.1, 181.65, 191.2, 197.1, 218.6, 228.8, 242.0, 255.2,
# 272.9, 290.75, 308.6, 325.3, 342.0, 353.1, 366.6.
SEGMENTS = [
    # n0 — who he was, and WHY he had everything to lose.
    ("n0a", "still", S1, 0, 13.6, "in",
     "In Jerusalem there was a man named\n"
     "Nicodemus. He was a Pharisee, and more\n"
     "than that — a ruler of the Jews, a member\n"
     "of the great council that governed\n"
     "the nation's faith.", "n"),
    ("n0b", "still", S1, 0, 13.6, "out",
     "Educated. Respected. Listened to.\n"
     "A man like that had everything to lose\n"
     "by being seen with a controversial\n"
     "teacher from Galilee. His seat,\n"
     "his standing, his name.", "n"),
    # MONEY MOMENT — the night street. Held beat (the pack's own law).
    ("n1", "still", STILL_STREET, 0, 8.4, "in",
     "So he came at night.", "n"),
    # n2 — the knock; the "we know" study gem.
    ("n2a", "still", S3, 0, 16.65, "in",
     "He knocked on the door in the dark, and\n"
     "the first thing he said was this: Teacher,\n"
     "we know you have come from God, because\n"
     "no one could do what you do unless\n"
     "God were with him.", "n"),
    ("n2b", "still", S3, 0, 16.65, "out",
     "Bible students notice one small word\n"
     "there — we. Not I. We know. Nicodemus had\n"
     "been talking with other rulers, quietly,\n"
     "behind closed doors. Some of the very men\n"
     "who opposed Jesus in public already\n"
     "believed it in private. He just\n"
     "couldn't say it in daylight.", "n"),
    # n3a — Jesus doesn't shame the night.
    ("n3a", "still", S4, 0, 15.5, "in",
     "And Jesus didn't turn him away for coming\n"
     "at night. He didn't point out the fear.\n"
     "He skipped past the compliment entirely,\n"
     "and answered the real question\n"
     "underneath — the one Nicodemus\n"
     "hadn't dared to ask.", "n"),
    # J1 — exact KJV John 3:3 (music already out).
    ("j1", "still", S4, 0, 9.6, "out",
     "\u201cVerily, verily, I say unto thee,\n"
     "Except a man be born again, he cannot\n"
     "see the kingdom of God.\u201d", "kjv"),
    # n3b — origin of "born again", said to the most religious man.
    ("n3ba", "still", S4, 0, 11.0, "in",
     "That's where the phrase comes from —\n"
     "this conversation, this night. And notice\n"
     "who heard it first. Not a hardened sinner.\n"
     "The most religious man in the country.", "n"),
    ("n3bb", "still", S4, 0, 11.0, "out",
     "Jesus was telling him that all his\n"
     "learning and all his rule-keeping could\n"
     "not do it. Everyone has to start over.\n"
     "Everyone.", "n"),
    # n4 — the womb question; Jesus doesn't mock him.
    ("n4a", "still", S5, 0, 13.0, "in",
     "Nicodemus took it literally. How can a\n"
     "man be born when he is old, he asked —\n"
     "can he enter a second time into his\n"
     "mother's womb? Here was a master of\n"
     "the scriptures, completely lost.", "n"),
    ("n4b", "still", S5, 0, 13.0, "out",
     "And Jesus didn't laugh at him. He didn't\n"
     "shame him for not getting it. He reached\n"
     "for something Nicodemus could feel —\n"
     "the night wind moving outside the window.", "n"),
    # J2 — exact KJV John 3:8, over the wind through the window.
    ("j2", "still", S6, 0, 13.2, "in",
     "\u201cThe wind bloweth where it listeth, and\n"
     "thou hearest the sound thereof, but canst\n"
     "not tell whence it cometh, and whither it\n"
     "goeth: so is every one that is born\n"
     "of the Spirit.\u201d", "kjv"),
    # n5 — you can't see wind, only what it moves.
    ("n5", "still", S6, 0, 16.9, "out",
     "You can't see the wind. You only see what\n"
     "it moves — the trees bending, the flame\n"
     "leaning. That, Jesus said, is how God\n"
     "changes a person. You may not be able to\n"
     "explain it. But you can watch a life bend.", "n"),
    # n6 — "How can these things be?"
    ("n6a", "still", S7, 0, 9.55, "in",
     "And something in Nicodemus gave way.\n"
     "How can these things be, he asked.", "n"),
    ("n6b", "still", S7, 0, 9.55, "out",
     "Three words at a time, the formal\n"
     "questions of a scholar were falling\n"
     "away — until what was left was just a man,\n"
     "in the lamplight, finally asking what\n"
     "he actually wanted to know.", "n"),
    # n7a — peak setup; the bed is fading to nothing under this line.
    ("n7a", "still", S8, 0, 5.9, "in",
     "And then Jesus said the words. The ones\n"
     "the whole world would come to know.", "n"),
    # J3 — exact KJV John 3:16-17. THE PEAK. Full sacred silence.
    ("j3", "still", S8, 0, 21.5, "out",
     "\u201cFor God so loved the world, that he gave\n"
     "his only begotten Son, that whosoever\n"
     "believeth in him should not perish, but\n"
     "have everlasting life. For God sent not\n"
     "his Son into the world to condemn the\n"
     "world; but that the world through him\n"
     "might be saved.\u201d", "kjv"),
    # n7b — not preached to a stadium.
    ("n7b", "still", S8, 0, 10.2, "in",
     "Those words weren't preached to a\n"
     "stadium. They were said quietly, at\n"
     "night, to one scared man who came\n"
     "with questions.", "n"),
    # n8 — light/darkness: an invitation, not a jab.
    ("n8a", "still", S9, 0, 13.2, "in",
     "Then Jesus spoke about light and\n"
     "darkness — how people hide in the dark\n"
     "when they're afraid of what the light\n"
     "will show, but whoever lives by the truth\n"
     "steps into the light gladly.", "n"),
    ("n8b", "still", S9, 0, 13.2, "out",
     "Think about who he was saying that to.\n"
     "A man who had crept to his door under\n"
     "cover of darkness. It wasn't a jab. It was\n"
     "an invitation: you won't always have\n"
     "to come at night.", "n"),
    # n9 — John's tag: watch what happens to him.
    ("n9", "still", S9, 0, 17.7, "in",
     "Every time John's gospel mentions\n"
     "Nicodemus again, it adds the same tag —\n"
     "the one who came to Jesus by night.\n"
     "John wants you to remember how he\n"
     "started. Because he wants you to watch\n"
     "what happened to him.", "n"),
    # n10 — John 7:50-51: first daylight courage.
    ("n10a", "still", S10, 0, 17.85, "in",
     "Months later, the council met in broad\n"
     "daylight, furious, ready to condemn Jesus\n"
     "without a hearing. And one voice rose to\n"
     "stop them. Nicodemus. Does our law judge\n"
     "a man, he asked, before it hears him?", "n"),
    ("n10b", "still", S10, 0, 17.85, "out",
     "It sounds mild. It wasn't. He was\n"
     "defending Jesus to the most powerful men\n"
     "in the nation — the very room he had\n"
     "everything to lose in. They turned on him\n"
     "for it. The man who once came at night\n"
     "was starting to speak in the light.", "n"),
    # n11 — John 19:39: the hundred-pound burial in the open.
    ("n11a", "still", S11, 0, 16.7, "in",
     "And then came the darkest day. Jesus was\n"
     "dead. His own apostles were hiding behind\n"
     "locked doors. And Nicodemus came —\n"
     "openly, in the daylight, when believing\n"
     "could no longer gain anyone anything —", "n"),
    ("n11b", "still", S11, 0, 16.7, "out",
     "carrying a hundred pounds of myrrh and\n"
     "aloes for the burial. A hundred pounds.\n"
     "That was a quantity fit for royalty. The\n"
     "man who had crept to Jesus in the dark\n"
     "gave him a king's burial in the open.", "n"),
    # n12 first half — the closing reflection, on the s11 hold.
    ("n12a", "still", S11, 0, 11.1, "in",
     "Jesus never shamed the fear, and never\n"
     "shamed the night. He just answered the\n"
     "real question underneath — and let the\n"
     "courage grow on its own.", "n"),
    # Card — held 13.5s AND read aloud (Readable-Card Law).
    ("card", "card", None, 0, 13.5, None,
     "Have you ever felt drawn\ntoward something —\n"
     "and been afraid to let\nanyone else see it?", "close"),
]

# narration placements: (audio file, absolute start seconds)
# measured dur/tail: n0 26.520/.390  n1 1.776/.522  n2 32.496/.426
#   n3a 15.144/.420  j1 9.696/1.160  n3b 21.480/.399  n4 25.560/.394
#   j2 13.488/1.142  n5 16.416/.450  n6 18.744/.407  n7a 5.424/.407
#   j3 20.352/1.134  n7b 9.600/.456  n8 26.016/.422  n9 17.232/.401
#   n10 35.280/.438  n11 32.952/.417  n12 17.280/.512
# breaths 0.8-1.2s between SPOKEN ends; 6.3s held beat after n1 (law);
# 2.1s sacred quiet before j3 (bed3 fully out at 196.0, j3 at 198.5).
AUDIO = [
    ("audio/n0.mp3", 0.4),     # s1 0-27.2       who he was (sp end 26.53)
    ("audio/n1.mp3", 28.4),    # clip 27.2-35.6  came at night (sp 29.65) + HELD BEAT
    ("audio/n2.mp3", 35.9),    # s3 35.6-68.9    the knock, "we" gem (sp 67.97)
    ("audio/n3a.mp3", 69.1),   # s4 68.9-84.4    answered underneath (sp 83.82)
    ("audio/j1.mp3", 84.7),    # s4 84.4-94.0    KJV 3:3 (sp 93.24)
    ("audio/n3b.mp3", 94.2),   # s4 94.0-116.0   born-again origin (sp 115.28)
    ("audio/n4.mp3", 116.1),   # s5 116.0-142.0  womb question (sp 141.27)
    ("audio/j2.mp3", 142.2),   # s6 142.0-155.2  KJV 3:8 (sp 154.55)
    ("audio/n5.mp3", 155.4),   # s6 155.2-172.1  watch a life bend (sp 171.37)
    ("audio/n6.mp3", 172.2),   # s7 172.1-191.2  how can these things be (sp 190.54)
    ("audio/n7a.mp3", 191.4),  # s8 191.2-197.1  peak setup (sp 196.42)
    # 2.1s sacred quiet — bed3 fully out at 196.0
    ("audio/j3.mp3", 198.5),   # s8 197.1-218.6  KJV 3:16-17 PEAK (sp 217.72)
    ("audio/n7b.mp3", 218.9),  # s8 218.6-228.8  not a stadium (sp 228.04)
    ("audio/n8.mp3", 228.9),   # s9 228.8-255.2  light/darkness (sp 254.49)
    ("audio/n9.mp3", 255.3),   # s9 255.2-272.9  John's tag (sp 272.13)
    ("audio/n10.mp3", 273.0),  # s10 272.9-308.6 council defense (sp 307.84)
    ("audio/n11.mp3", 308.7),  # s11 308.6-342.0 hundred pounds (sp 341.24)
    ("audio/n12.mp3", 342.1),  # s11 hold + card 342.0-366.6 (sp 358.87)
]

# Detuned-pair beds — every one fully out before its red-letter line.
# (start_s, end_s, style) — style "a" = fuller, "b" = quieter/warmer.
BEDS = [
    (0.0, 83.6, "a"),      # setup + street + knock; out before J1 (84.7)
    (94.0, 141.2, "b"),    # born-again + womb beats; out before J2 (142.2)
    (155.2, 196.0, "b"),   # wind bridge + face; dies under n7a; J3 in SILENCE
    (229.0, 360.0, "b"),   # the arc: leaving/council/burial/closing
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
    if seg_id == "n12a":
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    fc = assemble_segment(seg_id, base, dur, cap, style, tail)
    run(["ffmpeg", "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_clip(seg_id, src, start, dur, cap, style):
    """Veo clip stretched 1.05x (8s -> 8.4s) so the doorway hesitation
    holds through the whole held beat without a hard cut mid-motion."""
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
    # 24.5MB over 366.6s = 534kbps total budget; audio 128k -> video ~390k.
    vcap = max(300, int(24.5 * 8000 / total) - 145)
    for crf in (21, 22, 23, 24, 25):
        run(["ffmpeg", "-y", "-i", f"{S}/video_silent.mp4",
             "-i", f"{S}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "veryslow", "-crf", str(crf),
             "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
             "nicodemus-04.mp4"])
        size = os.path.getsize("nicodemus-04.mp4") / 1e6
        if size <= 24.5:
            break
        print(f"  {size:.1f} MB at crf {crf} — over budget, stepping up",
              flush=True)
    print(f"DONE: nicodemus-04.mp4  {size:.1f} MB, {total:.1f}s "
          f"(crf {crf}, vcap {vcap}k)", flush=True)


if __name__ == "__main__":
    main()
