#!/usr/bin/env python3
"""Assemble Story Video #8 — The Lost Coin (Luke 15:8-10).
Hybrid storybook format per PRODUCTION-BIBLE.md: painted stills with Ken Burns
drift + 1 animated money-moment clip (the FOUND flash), narration (edge-tts),
serif captions, KJV red-letter lines, closing question card on cream #F7F2E9.

Two-Voice Law: narrator modern American; Jesus voice speaks ONLY exact KJV
(Luke 15:9 over the doorway, Luke 15:10 over the starry pull-back). Music cuts
to full silence before the angels line so the peak lands in sacred quiet.

All six visual assets approved by Leighton (QC'd for character lock, wardrobe
lock, nine coins, lamp continuity, visible coin) on 2026-07-08.
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

STILL_COUNT = "Woman_counting_silver_coins_2K_202607081706.jpeg"
STILL_SWEEP = "Woman_searching_for_lost_coin_202607081705.jpeg"
STILL_KNEEL = "Woman_searching_for_lost_coin_202607081707.jpeg"
CLIP_FOUND = "Woman_finding_single_coin_202607082018.mp4"  # v4 FINAL: ONE coin in every frame, floor bare after pickup, positive-only phrasing per PRODUCTION-BIBLE 5b (Cameron's two-coins fix). v3 negative-prompt attempt rejected (cartoon drift); v2 left a second coin on the floor.
STILL_DOOR = "Woman_holding_silver_coin_joyfully_202607081704.jpeg"
STILL_STARS = "Village_under_starry_sky_2K_202607081703.jpeg"

# (id, kind, source, duration_s, zoom_dir, caption, caption_style)
SEGMENTS = [
    # Opening frame: WHY Jesus told this story — Heaven's excitement over one
    # soul found. Starts on the same starry sky the video ends on, so the
    # whole story is bookended by Heaven's point of view (Cameron/Leighton
    # request, 2026-07-08 pt.11).
    ("s00", "still", STILL_STARS, 10.5, "out",
     "When Jesus wanted to show\nhow God feels about one lost soul,\n"
     "he didn't talk about crowds.\nHe told this story.", "n"),
    ("s01", "still", STILL_COUNT, 6.5, "in",
     "A woman has ten coins.\nShe loses one.", "n"),
    ("s02", "still", STILL_SWEEP, 6.5, "in",
     "She lights a lamp.\nShe sweeps the whole house.", "n"),
    ("s03", "still", STILL_KNEEL, 8.5, "in",
     "She searches carefully —\nnot casually, carefully —\nuntil she finds it.", "n"),
    ("s04", "clip", CLIP_FOUND, 8.0, None,
     None, "n"),
    ("s05a", "still", STILL_DOOR, 4.5, "in",
     "Then she calls her neighbors\nand friends to celebrate.", "n"),
    ("s05b", "still", STILL_DOOR, 6.5, "out",
     "\u201cRejoice with me; for I have found\nthe piece which I had lost.\u201d", "kjv"),
    ("s06a", "still", STILL_STARS, 7.0, "in",
     "One coin. Out of ten.\nThe joy is disproportionate\nto the value of the coin.", "n"),
    ("s06b", "still", STILL_STARS, 11.0, "out",
     "\u201cLikewise, I say unto you, there is joy\nin the presence of the angels of God\nover one sinner that repenteth.\u201d", "kjv"),
    ("s06c", "still", STILL_STARS, 5.0, "in",
     "Over one. Not a crowd. One.", "n"),
    ("s07", "card", None, 6.0, None,
     "Have you ever felt like\nthe thing that got lost\nrather than the one\ndoing the searching?", "close"),
]

# narration placements: (audio file, absolute start seconds)
AUDIO = [
    ("audio/n0.mp3", 0.8),    # s00 0-10.5 — why Jesus told it (9.1s)
    ("audio/n1.mp3", 11.3),   # s01 10.5-17
    ("audio/n2a.mp3", 17.5),  # s02 17-23.5
    ("audio/n2b.mp3", 24.0),  # s03 23.5-32   (s04 found clip 32-40 silent)
    ("audio/n3.mp3", 40.4),   # s05a 40-44.5
    ("audio/j1.mp3", 45.1),   # s05b 44.5-51 — KJV Luke 15:9
    ("audio/n4.mp3", 51.5),   # s06a 51-58
    ("audio/j2.mp3", 58.8),   # s06b 58-69 — KJV Luke 15:10, music silent
    ("audio/n5.mp3", 69.5),   # s06c 69-74 — "Over one. Not a crowd. One."
]

MUSIC_END = 57.5  # fully silent before the angels line — the peak is quiet


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
    if seg_id == "s06c":
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
         "lost-coin-08.mp4"])
    size = os.path.getsize("lost-coin-08.mp4") / 1e6
    print(f"DONE: lost-coin-08.mp4  {size:.1f} MB, {total:.1f}s")


if __name__ == "__main__":
    main()
