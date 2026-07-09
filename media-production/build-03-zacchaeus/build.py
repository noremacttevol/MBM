#!/usr/bin/env python3
"""Assemble Story Video #3 — Zacchaeus (Luke 19:1-10).
Hybrid storybook format per PRODUCTION-BIBLE.md: painted stills with Ken Burns
drift + 1 animated money-moment clip (the look up), narration (edge-tts),
serif captions, KJV red-letter lines, closing question card on cream #F7F2E9.

Built under the section 4b RIGHT-FIRST-TIME PRE-FLIGHT (see PREFLIGHT.md) and
the Assembly Craft Laws (2026-07-09) from the very first frame: supersampled
zoompan, RGBA caption fades, crf-16 intermediates, veryslow crf step-up final,
loudness lifted toward -15 LUFS, detuned-pair music beds.

FULL-STORY law: all ten verses covered. The pack had stopped at v6 and marked
v10 "optional" — caught on paper (see PREFLIGHT.md FINDING). The TRUE last
story words are KJV 19:9-10 in the Jesus voice.

Two-Voice Law: narrator modern American; Jesus speaks ONLY exact KJV
(Luke 19:5b split at its semicolon across the clip and a still; 19:9b; 19:10).
Music fully silent BEFORE "Jesus stopped, right under that tree." so the peak
(grace notices you) lands in sacred quiet — and out again before 19:9-10.

All offsets computed from MEASURED mp3 durations after the ear-check
(all 16 segments passed; j1a via the medium.en tie-break law).

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

# Intermediate segments near-lossless (crf 16) so the final pass is the
# ONLY lossy generation the viewer sees (Assembly Craft Laws).
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

STILL_DESPISED = "shot1-despised.jpeg"
STILL_BLOCKED = "shot2-blocked.jpeg"
STILL_RUN = "shot3-run.jpeg"
STILL_CLIMB = "shot4-climb.jpeg"
CLIP_LOOKUP = "clip-looked-up.mp4"
STILL_LIT = "shot5-lit.jpeg"
STILL_COMEDOWN = "shot6-comedown.jpeg"
STILL_TABLE = "shot7-table.jpeg"
STILL_SALVATION = "shot8-salvation.jpeg"

# (id, kind, source, clip_start, duration_s, zoom_dir, caption, caption_style)
SEGMENTS = [
    ("s00", "still", STILL_DESPISED, 0, 14.6, "in",
     "Zacchaeus was a tax collector — which in\n"
     "his time meant he worked for the occupying\n"
     "empire, and got rich doing it. In Jericho\n"
     "everyone knew his name, and no one\nwanted him at their table.", "n"),
    ("s01", "still", STILL_BLOCKED, 0, 11.7, "in",
     "When Jesus came through town, Zacchaeus\n"
     "wanted to see him. But he was short, and\n"
     "the crowd was a wall. Nobody makes room\n"
     "for the man they all despise.", "n"),
    ("s02", "still", STILL_RUN, 0, 8.7, "in",
     "So he ran ahead. A grown man. A rich man.\n"
     "Robes flapping, rings and dignity forgotten.", "n"),
    ("s03", "still", STILL_CLIMB, 0, 9.0, "in",
     "And he climbed a tree — just to catch\n"
     "a glimpse from a distance. He would\n"
     "have settled for that. A glimpse.", "n"),
    # MONEY MOMENT — Jesus stops and looks up. Music already fully silent
    # (MUSIC_END 43.5) so the peak lands in sacred quiet.
    ("s04a", "clip", CLIP_LOOKUP, 0, 5.0, None,
     "Jesus stopped, right under that tree.\nAnd looked up.", "n"),
    # Exact KJV Luke 19:5b, first half — the clip holds through the words.
    ("s04b", "clip", CLIP_LOOKUP, 5.0, 3.0, None,
     "\u201cZacchaeus, make haste,\nand come down;\u201d", "kjv"),
    # KJV second half carried by the lit-in-the-tree still.
    ("s05", "still", STILL_LIT, 0, 4.9, "in",
     "\u201cfor to day I must abide\nat thy house.\u201d", "kjv"),
    # Pack-approved bridge — quotes only the two words (Translation Law).
    ("s06", "still", STILL_LIT, 0, 10.5, "out",
     "'I must' — not 'I might.' Out of everyone\n"
     "in that crowd, staying with the man everyone\n"
     "hated wasn't a detour. It was the plan.", "n"),
    # v6-7: the joyful coming down AND the murmuring crowd (Full-Story law).
    ("s07", "still", STILL_COMEDOWN, 0, 12.8, "in",
     "Zacchaeus half-fell out of that tree with joy.\n"
     "And the crowd couldn't believe it. Of every\n"
     "house in Jericho, he chose the cheat's.\n"
     "They grumbled about it, out loud.", "n"),
    # v8: the standing gift, three caption-sized beats; the Seed line alone.
    ("s08a", "still", STILL_TABLE, 0, 5.4, "in",
     "Nobody demanded anything. But grace\nhad already gotten there first.",
     "n"),
    ("s08b", "still", STILL_TABLE, 0, 10.6, "out",
     "Zacchaeus stood up at his own table:\n"
     "half of everything I own goes to the poor —\n"
     "and anyone I cheated, I will pay back\nfour times over.", "n"),
    ("s08c", "still", STILL_TABLE, 0, 3.8, "in",
     "He changed because Jesus came first.", "n"),
    ("s09a", "still", STILL_SALVATION, 0, 3.8, "in",
     "And Jesus gave the story its last words.", "n"),
    # Exact KJV Luke 19:9b and 19:10 — the TRUE last story words, in the
    # same sacred quiet as the look up (bed2 out at 103.0, j2a at 104.2).
    ("s09b", "still", STILL_SALVATION, 0, 7.6, "out",
     "\u201cThis day is salvation come to this house,\n"
     "forsomuch as he also is a son of Abraham.\u201d", "kjv"),
    ("s09c", "still", STILL_SALVATION, 0, 5.9, "in",
     "\u201cFor the Son of man is come to seek and\n"
     "to save that which was lost.\u201d", "kjv"),
    # Held 14.0s AND read aloud (Readable-Card Law); lines <=31 chars.
    ("s10", "card", None, 0, 14.0,
     None,
     "Have you ever done something —\nmaybe something a little\n"
     "embarrassing — just to get\na look at something you\n"
     "thought might be real?", "close"),
]

# narration placements: (audio file, absolute start seconds)
# measured dur/tail: n0 14.184/.424  n1 11.496/.445  n2 8.352/.406
#   n3 7.608/.450  n4 4.320/.453  j1a 4.512/1.033  j1b 4.248/1.111
#   n5 10.056/.401  n6 12.768/.422  n7a 5.040/.445  n7b 10.392/.428
#   n7c 3.360/.451  n8 3.720/.459  j2a 8.016/1.133  j2b 5.928/1.108
#   n9 8.016/.418   (gaps computed from SPOKEN ends = dur - tail)
AUDIO = [
    ("audio/n0.mp3", 0.4),    # s00 0-14.6     despised+rich (sp end 14.16)
    ("audio/n1.mp3", 14.9),   # s01 14.6-26.3  the wall (sp 25.95)
    ("audio/n2.mp3", 26.6),   # s02 26.3-35.0  the run (sp 34.55)
    ("audio/n3.mp3", 35.2),   # s03 35.0-44.0  the climb (sp 42.36)
    # 2.04s sacred breath — music fully out by 43.5
    ("audio/n4.mp3", 44.4),   # s04a 44.0-49.0 the look up (sp 48.27)
    ("audio/j1a.mp3", 49.1),  # s04b 49.0-52.0 KJV 19:5b pt1 (sp 52.58)
    ("audio/j1b.mp3", 53.3),  # s05 52.0-56.9  KJV 19:5b pt2 (sp 56.44)
    ("audio/n5.mp3", 57.3),   # s06 56.9-67.4  the I-must bridge (sp 66.96)
    ("audio/n6.mp3", 67.6),   # s07 67.4-80.2  down with joy + murmurs (sp 79.95)
    ("audio/n7a.mp3", 80.6),  # s08a 80.2-85.6 grace got there first (sp 85.20)
    ("audio/n7b.mp3", 85.8),  # s08b 85.6-96.2 the standing gift (sp 95.76)
    ("audio/n7c.mp3", 96.5),  # s08c 96.2-100.0 the Seed line (sp 99.41)
    ("audio/n8.mp3", 100.1),  # s09a 100.0-103.8 setup (sp 103.36)
    ("audio/j2a.mp3", 104.2), # s09b 103.8-111.4 KJV 19:9b (sp 111.08)
    ("audio/j2b.mp3", 111.8), # s09c 111.4-117.3 KJV 19:10 (sp 116.62)
    # 2.18s breath before the closing question
    ("audio/n9.mp3", 118.8),  # s10 117.3-131.3 card read aloud (sp 126.40)
]

MUSIC_END = 43.5  # fully silent before the look up — the peak is quiet


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:160])
    subprocess.run(cmd, check=True, capture_output=True)


def caption_overlay(seg_id, dur, text, style):
    """Caption rendered on its own transparent RGBA canvas (text + box +
    shadow as one layer) and alpha-faded 0.5s in/out, gone 0.1s before the
    cut — captions never pop (Assembly Craft Laws)."""
    if not text:
        return None
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w") as f:
        f.write(text)
    if style == "kjv":
        font, size, color = SERIF_BI, 46, "0xFFF3DC"
    else:
        font, size, color = SERIF, 42, "white"
    fade_out = max(0.0, dur - 0.6)
    return (f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile={font}:textfile={tf}:fontsize={size}:"
            f"fontcolor={color}:line_spacing=14:x=(w-text_w)/2:y=h-420:"
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
        z = f"1.001+0.12*on/{frames}"
    else:
        z = f"1.121-0.12*on/{frames}"
    # Anti-shimmer law: supersample 4320x7680 -> zoompan at 2160x3840 ->
    # lanczos down to 1080x1920 so every zoom step lands on a quarter-pixel.
    base = (f"[0:v]scale=4320:7680,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ""
    if seg_id == "s00":
        tail = ",fade=t=in:st=0:d=1.2"
    if seg_id == "s09c":
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    fc = assemble_segment(seg_id, base, dur, cap, style, tail)
    run(["ffmpeg", "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_clip(seg_id, src, start, dur, cap, style):
    """Veo clip segment. `start` trims into the source so one 8s clip can
    carry two caption beats (s04a = 0-5s look up, s04b = 5-8s KJV hold)."""
    base = (f"[0:v]scale=1080:1920:flags=lanczos,setsar=1,fps={FPS},"
            f"unsharp=5:5:0.35:5:5:0.0")
    fc = assemble_segment(seg_id, base, dur, cap, style)
    run(["ffmpeg", "-y", "-ss", str(start), "-i", f"{A}/{src}",
         "-t", str(dur), "-filter_complex", fc, "-map", "[v]"]
        + ENC + [f"{S}/{seg_id}.mp4"])


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


def main():
    os.makedirs(S, exist_ok=True)
    total = sum(s[4] for s in SEGMENTS)
    print(f"total runtime: {total:.1f}s")

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

    # ---- audio: narration at absolute offsets + detuned-pair music beds ----
    inputs = []
    filters = []
    labels = []
    for i, (path, start) in enumerate(AUDIO):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    # bed1 under the setup (0-43.5), fully out before the look up.
    bed1 = (f"aevalsrc='0.022*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
            f"+0.016*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))"
            f"+0.012*sin(2*PI*220*t)+0.008*sin(2*PI*329.63*t)'"
            f":s=44100:d={MUSIC_END},"
            f"lowpass=f=750,tremolo=f=0.13:d=0.3,"
            f"aecho=0.7:0.4:311|429:0.25|0.18,"
            f"afade=t=in:st=0:d=6,afade=t=out:st={MUSIC_END-5}:d=5[mus1]")
    filters.append(bed1)
    labels.append("[mus1]")
    # bed2 warm and quieter under the coming-down + table section
    # (67.4-103.0), fully out before the final KJV at 104.2 so 19:9-10
    # land in sacred quiet.
    m2_start, m2_dur = 67.4, 35.6
    bed2 = (f"aevalsrc='0.014*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
            f"+0.011*(sin(2*PI*138.59*t)+sin(2*PI*139.2*t))"
            f"+0.009*sin(2*PI*164.81*t)+0.006*sin(2*PI*220*t)'"
            f":s=44100:d={m2_dur},"
            f"lowpass=f=700,tremolo=f=0.11:d=0.3,"
            f"aecho=0.7:0.4:317|443:0.25|0.18,"
            f"afade=t=in:st=0:d=5,afade=t=out:st={m2_dur-6}:d=6,"
            f"adelay={int(m2_start*1000)}|{int(m2_start*1000)}[mus2]")
    filters.append(bed2)
    labels.append("[mus2]")
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
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB")

    # ---- final mux: preset veryslow, crf step-up until <=24.5MB ----
    for crf in (21, 22, 23, 24):
        run(["ffmpeg", "-y", "-i", f"{S}/video_silent.mp4",
             "-i", f"{S}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "veryslow", "-crf", str(crf),
             "-maxrate", "1200k", "-bufsize", "2400k", "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
             "zacchaeus-03.mp4"])
        size = os.path.getsize("zacchaeus-03.mp4") / 1e6
        if size <= 24.5:
            break
        print(f"  {size:.1f} MB at crf {crf} — over budget, stepping up")
    print(f"DONE: zacchaeus-03.mp4  {size:.1f} MB, {total:.1f}s (crf {crf})")


if __name__ == "__main__":
    main()
