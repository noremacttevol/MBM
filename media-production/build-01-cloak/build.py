#!/usr/bin/env python3
"""Assemble Story Video #1 — The Woman Who Touched His Cloak (Mark 5:25-34). v2.
Hybrid storybook format per PRODUCTION-BIBLE.md: painted stills with Ken Burns
drift + 2 animated money-moment clips, narration (edge-tts), serif captions,
KJV verse card, closing question card on cream #F7F2E9.

v2 changes (Cameron, 2026-07-07):
- Jesus voice is AMERICAN (en-US-ChristopherNeural), never British. Permanent.
- Fuller story: Jairus backstory (on his way to a dying twelve-year-old girl),
  he FELT power go out of him, KJV Mark 5:30 "Who touched my clothes?",
  disciples questioning him, he ignored them and kept looking.
- Sequencing fixes: redundant tassel-touch still removed (the animated hem clip
  carries that beat alone); the walking-away still moved to the backstory beat
  where walking away makes sense; new disciples still added.
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

# (id, kind, source, duration_s, zoom_dir, caption, caption_style)
SEGMENTS = [
    ("s01", "still", "Woman_sits_in_dim_room_202607072313.jpeg", 6.0, "in",
     "There was a woman who had been\nsuffering for twelve years.", "n"),
    ("s02", "still", "Woman's_hands_holding_empty_purse_202607072310.jpeg", 13.0, "out",
     "She had spent everything on doctors.\nNothing helped. She was exhausted,\ndesperate — and by the rules of her time,\nconsidered untouchable.", "n"),
    ("s03", "still", "Man_walking_in_crowd_2K_202607111552.jpeg", 10.5, "in",
     "That day, Jesus was already on his way\nto save someone else — a ruler's daughter,\ntwelve years old, and dying.", "n"),
    ("s04", "still", "Robed_figures_on_stone_street_202607072302.jpeg", 8.5, "in",
     "The crowd pressed around him on every side.\nAlmost no one would have noticed\none more sick woman at its edge.", "n"),
    ("s05", "still", "Woman_gathering_shawl_at_doorway_202607072309.jpeg", 7.5, "in",
     "She heard Jesus was nearby.\nShe did not ask permission.\nShe did not make a speech.", "n"),
    ("s06", "still", "Veiled_woman_in_crowd_2K_202607072304.jpeg", 6.0, "in",
     "She pressed through the crowd\nand reached out to touch\nthe edge of his cloak.", "n"),
    ("s07", "still", "Woman's_hand_touching_cloak_tassels_202607072306.jpeg", 8.0, "in",
     None, "n"),
    ("s08", "still", "Feet_on_dusty_stone_street_202607072306.jpeg", 11.0, "in",
     "He stopped. He had felt it — power had\ngone out of him. The healing was already\nhers, given the moment she touched him.", "n"),
    ("s09", "still", "Man_looking_at_kneeling_woman_202607111557.jpeg", 7.5, "in",
     "\u201cWho touched my clothes?\u201d", "kjv"),
    ("s10", "still", "DISCIPLES_STILL", 16.0, "out",
     "His disciples thought the question made\nno sense — the whole crowd was pressing\nagainst him. He ignored them.\nHe was already needed somewhere else,\nand he stopped anyway.", "n"),
    ("s11", "still", "Woman_kneeling_looking_upward_2K_202607072303.jpeg", 14.5, "in",
     "\u201cDaughter, thy faith hath made thee whole;\ngo in peace, and be whole of thy plague.\u201d", "kjv"),
    ("s12", "still", "Woman_kneeling_with_tears_2K_202607072303.jpeg", 5.0, "out",
     "\u201cBe whole of thy plague\u201d — be free of\nwhat has been hurting you.", "n"),
    ("s13", "still", "Woman_standing_in_street_2K_202607072302.jpeg", 4.5, "in",
     "Twelve years of it.\nOver, in a sentence.", "n"),
    ("s14", "still", "Woman_standing_on_stone_street_202607072301.jpeg", 5.0, "out",
     "And the first word he chose\nwas daughter.", "n"),
    ("s15", "card", None, 5.5, None,
     "\u201cDaughter, thy faith hath made\nthee whole; go in peace, and be\nwhole of thy plague.\u201d\n\nMark 5:34", "verse"),
    ("s16", "card", None, 6.0, None,
     "Have you ever been that desperate\nfor something in your life to change —\neven if you had no words for it yet?", "close"),
]

# narration placements: (audio file, absolute start seconds)
AUDIO = [
    ("audio/n1.mp3", 0.8),     # s01 0-6
    ("audio/n2.mp3", 6.5),     # s02 6-19
    ("audio/n2b.mp3", 19.6),   # s03 19-29.5 + s04 29.5-38
    ("audio/n3a.mp3", 38.5),   # s05 38-45.5
    ("audio/n3b.mp3", 45.9),   # s06 45.5-51.5   (s07 hem clip 51.5-59.5 silent)
    ("audio/n4a.mp3", 60.2),   # s08 59.5-70.5
    ("audio/j0.mp3", 71.5),    # s09 turn clip 70.5-78 — KJV Mark 5:30
    ("audio/n4c.mp3", 78.6),   # s10 78-94
    ("audio/n4b.mp3", 94.5),   # s11 94-108.5, then sacred pause
    ("audio/j1.mp3", 100.4),   # KJV Mark 5:34 — music silent long before this
    ("audio/n5.mp3", 109.0),   # s12-s14 108.5-123
]

MUSIC_END = 96.0  # pad fully silent before the sacred lines


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
    if seg_id == "s01":
        vf += ",fade=t=in:st=0:d=1.2"
    if seg_id == "s14":
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
    if style == "verse":
        font, size = SERIF_BI, 52
    else:
        font, size = SERIF, 50
    vf = (f"drawtext=fontfile={font}:textfile={tf}:fontsize={size}:"
          f"fontcolor={INK}:line_spacing=22:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run(["ffmpeg", "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/{seg_id}.mp4"])


def main():
    # resolve the disciples still (any filename starting with a known prefix)
    disc = [f for f in os.listdir(A)
            if "isciple" in f or "uzzled" in f or "onfusion" in f]
    if not disc:
        raise SystemExit("disciples still not found in assets/ — download it first")
    segments = [list(s) for s in SEGMENTS]
    for s in segments:
        if s[2] == "DISCIPLES_STILL":
            s[2] = disc[0]

    total = sum(s[3] for s in segments)
    print(f"total runtime: {total:.1f}s")

    for seg_id, kind, src, dur, zdir, cap, style in segments:
        if kind == "still":
            build_still(seg_id, src, dur, zdir, cap, style)
        elif kind == "clip":
            build_clip(seg_id, src, dur, cap, style)
        else:
            build_card(seg_id, dur, cap, style)

    with open(f"{S}/concat.txt", "w") as f:
        for seg in segments:
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
         "cloak-01-prototype.mp4"])
    size = os.path.getsize("cloak-01-prototype.mp4") / 1e6
    print(f"DONE: cloak-01-prototype.mp4  {size:.1f} MB, {total:.1f}s")


if __name__ == "__main__":
    main()
