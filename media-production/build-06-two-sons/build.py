#!/usr/bin/env python3
"""Assemble Story Video #6 — The Two Sons (Matthew 21:28-32).
Hybrid storybook format per PRODUCTION-BIBLE.md: painted stills with Ken Burns
drift + 1 animated money-moment clip (Shot 4 "He went"), narration (edge-tts),
serif captions, KJV red-letter lines, closing question card on cream #F7F2E9.

Two-Voice Law: narrator modern American; Jesus voice speaks ONLY exact KJV
(Matthew 21:31a — the question; Matthew 21:31b — the verdict, last spoken
words). Music fades to full silence BEFORE the crowd's answer ("the one who
first said no") so the peak lands in sacred quiet.

Opens with the "why Jesus told it" bookend (pattern Cameron approved on #8).

Shot 4 clip is the v2 retake: Cameron rejected v1 for sweat appearing
instantly when he wiped his head — looked AI. Fix per PRODUCTION-BIBLE 5b:
positive-only phrasing, no sweat/wipe beat at all, steady calm work only.

Output: 1080x1920 H.264, <25MB.
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

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "18",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

STILL_REFUSE = "shot1-i-will-not.jpeg"
STILL_FALSEYES = "shot2-false-yes.jpeg"
STILL_WALL = "shot3-stone-wall.jpeg"
CLIP_WENT = "Young_man_pruning_vineyard_rows_202607082152.mp4"  # v2 retake
STILL_EMPTY = "shot5-empty-row.jpeg"
STILL_PRIDE = "shot6-fathers-pride.jpeg"

# (id, kind, source, duration_s, zoom_dir, caption, caption_style)
SEGMENTS = [
    # Opening bookend — why Jesus told this story. Uses the vineyard
    # landscape the story lives in; it returns later as the empty row.
    ("s00", "still", STILL_EMPTY, 12.0, "out",
     "Jesus told this story to religious leaders —\n"
     "people who were sure they had already\nsaid yes to God.\n"
     "He told it so they would hear themselves in it.", "n"),
    ("s01", "still", STILL_REFUSE, 11.5, "in",
     "A father told his first son:\nGo work in the vineyard today.\n"
     "The son said, \u201cI will not.\u201d\n"
     "Later he changed his mind — and went.", "n"),
    ("s02", "still", STILL_FALSEYES, 9.5, "in",
     "The father told his second son the same thing.\n"
     "That son said, \u201cYes, I will go.\u201d\nAnd didn't.", "n"),
    # The no that couldn't let go. Was a silent beat — Cameron rejected the
    # first cut for 16 seconds of dead air here ("it just stops talking").
    # Narration now carries every scene. No silent stretches, ever.
    ("s03", "still", STILL_WALL, 9.0, "in",
     "The first son meant his no.\nBut it wouldn't leave him alone.\n"
     "All morning, the vineyard kept pulling at him.", "n"),
    # Money moment — he went.
    ("s04", "clip", CLIP_WENT, 8.0, None,
     "So he got up. And he went.\nNo announcement, no apology.\n"
     "He went back to the vineyard, and he worked.", "n"),
    ("s05", "still", STILL_EMPTY, 9.5, "in",
     "The row the second son promised to work\nstayed empty all day.\n"
     "Then Jesus asked the crowd a question.", "n"),
    ("s06a", "still", STILL_PRIDE, 5.5, "in",
     "\u201cWhether of them twain\ndid the will of his father?\u201d", "kjv"),
    # PEAK — the answer lands in full silence (music ends before this).
    # Narrator gives only the plain meaning — never re-quotes Jesus's KJV
    # (Cameron's rule, 2026-07-08).
    ("s06b", "still", STILL_PRIDE, 9.5, "out",
     "He was asking: which of the two\ndid what his father wanted?\n"
     "The crowd answered:\nthe one who first said no.", "n"),
    ("s06c", "still", STILL_PRIDE, 7.0, "in",
     "Then he turned to the religious leaders —\n"
     "the ones who were sure\nthey were the second son.", "n"),
    ("s06d", "still", STILL_FALSEYES, 9.5, "out",
     "\u201cVerily I say unto you, That the publicans\n"
     "and the harlots go into the kingdom of God\nbefore you.\u201d", "kjv"),
    # Held 13s AND read aloud by the narrator — the first cut ended too fast
    # to read (Cameron's catch, 2026-07-08).
    ("s07", "card", None, 13.0, None,
     "Have you ever said no to something —\nmaybe loudly — and found yourself\n"
     "moving toward it anyway because\npart of you couldn't let it go?", "close"),
]

# narration placements: (audio file, absolute start seconds)
AUDIO = [
    ("audio/n0.mp3", 0.5),    # s00 0-12     why Jesus told it (11.1s)
    ("audio/n1.mp3", 12.5),   # s01 12-23.5  first son: "I will not" (10.6s)
    ("audio/n2.mp3", 24.0),   # s02 23.5-33  second son: "Yes, I will go" (7.0s)
    ("audio/n2b.mp3", 31.6),  # s02          "And didn't." (1.2s)
    ("audio/n2c.mp3", 33.6),  # s03 33-42     the no that pulled at him (7.9s)
    ("audio/n2d.mp3", 42.0),  # s04 42-50     "So he got up..." (8.9s, tails 0.9s into s05)
    ("audio/n3.mp3", 51.4),   # s05 50-59.5   empty row + "Jesus asked" (7.6s)
    ("audio/j1.mp3", 60.0),   # s06a 59.5-65  KJV Matt 21:31a (4.2s)
    ("audio/n4.mp3", 65.7),   # s06b 65-74.5  plain meaning + the answer (8.4s) — PEAK
    ("audio/n5.mp3", 75.0),   # s06c 74.5-81.5 turned to the leaders (5.9s)
    ("audio/j2.mp3", 82.0),   # s06d 81.5-91  KJV Matt 21:31b (8.5s) — last words
    ("audio/n6.mp3", 91.8),   # s07 91-104    closing question read aloud (10.4s)
]

MUSIC_END = 65.5  # fully silent before the crowd's answer — the peak is quiet


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:160])
    subprocess.run(cmd, check=True, capture_output=True)


def caption_filter(seg_id, text, style):
    if not text:
        return None
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w") as f:
        f.write(text)
    if style == "kjv":
        font, size, color = SERIF_BI, 46, "0xFFF3DC"
    else:
        font, size, color = SERIF, 42, "white"
    return (f"drawtext=fontfile={font}:textfile={tf}:fontsize={size}:"
            f"fontcolor={color}:line_spacing=14:x=(w-text_w)/2:y=h-420:"
            f"shadowcolor=black@0.85:shadowx=2:shadowy=2:"
            f"box=1:boxcolor=black@0.30:boxborderw=18")


def build_still(seg_id, src, dur, zdir, cap, style):
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.12*on/{frames}"
    else:
        z = f"1.121-0.12*on/{frames}"
    vf = (f"scale=2160:3840,setsar=1,"
          f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
          f"d={frames}:s=1080x1920:fps={FPS}")
    capf = caption_filter(seg_id, cap, style)
    if capf:
        vf += "," + capf
    if seg_id == "s00":
        vf += ",fade=t=in:st=0:d=1.2"
    if seg_id == "s06d":
        vf += f",fade=t=out:st={dur-1.2}:d=1.2"
    run(["ffmpeg", "-y", "-loop", "1", "-i", f"{A}/{src}",
         "-t", str(dur), "-vf", vf] + ENC + [f"{S}/{seg_id}.mp4"])


def build_clip(seg_id, src, dur, cap, style):
    vf = f"scale=1080:1920:flags=lanczos,setsar=1,fps={FPS}"
    capf = caption_filter(seg_id, cap, style)
    if capf:
        vf += "," + capf
    run(["ffmpeg", "-y", "-i", f"{A}/{src}", "-t", str(dur),
         "-vf", vf] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(seg_id, dur, text, style):
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w") as f:
        f.write(text)
    font, size = SERIF, 50
    vf = (f"drawtext=fontfile={font}:textfile={tf}:fontsize={size}:"
          f"fontcolor={INK}:line_spacing=22:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run(["ffmpeg", "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/{seg_id}.mp4"])


def main():
    total = sum(s[3] for s in SEGMENTS)
    print(f"total runtime: {total:.1f}s")

    for seg_id, kind, src, dur, zdir, cap, style in SEGMENTS:
        if kind == "still":
            build_still(seg_id, src, dur, zdir, cap, style)
        elif kind == "clip":
            build_clip(seg_id, src, dur, cap, style)
        else:
            build_card(seg_id, dur, cap, style)

    with open(f"{S}/concat.txt", "w") as f:
        for seg in SEGMENTS:
            f.write(f"file '{seg[0]}.mp4'\n")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at absolute offsets + soft music bed ----
    inputs = []
    filters = []
    labels = []
    for i, (path, start) in enumerate(AUDIO):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    pad = (f"aevalsrc='0.028*sin(2*PI*110*t)+0.022*sin(2*PI*164.81*t)"
           f"+0.016*sin(2*PI*220*t)+0.010*sin(2*PI*329.63*t)':s=44100:d={MUSIC_END},"
           f"lowpass=f=800,tremolo=f=0.15:d=0.35,"
           f"afade=t=in:st=0:d=6,afade=t=out:st={MUSIC_END-5}:d=5[mus]")
    filters.append(pad)
    labels.append("[mus]")
    n = len(labels)
    filters.append("".join(labels) +
                   f"amix=inputs={n}:duration=longest:normalize=0,"
                   f"apad=whole_dur={total}[aout]")
    run(["ffmpeg", "-y"] + inputs + ["-filter_complex", ";".join(filters),
         "-map", "[aout]", "-t", str(total), "-c:a", "aac", "-b:a", "160k",
         f"{S}/audio_mix.m4a"])

    # ---- final mux, sized under 25MB ----
    run(["ffmpeg", "-y", "-i", f"{S}/video_silent.mp4", "-i", f"{S}/audio_mix.m4a",
         "-map", "0:v", "-map", "1:a",
         "-c:v", "libx264", "-preset", "slow", "-crf", "23",
         "-maxrate", "1500k", "-bufsize", "3000k", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
         "two-sons-06.mp4"])
    size = os.path.getsize("two-sons-06.mp4") / 1e6
    print(f"DONE: two-sons-06.mp4  {size:.1f} MB, {total:.1f}s")


if __name__ == "__main__":
    main()
