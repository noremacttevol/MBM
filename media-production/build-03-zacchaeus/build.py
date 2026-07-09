#!/usr/bin/env python3
"""Assemble Story Video #3 — Zacchaeus (Luke 19:1-10) — V2 REBUILD.

Cameron rejected v1 (2026-07-09): confusing, point unexplained, no study
gems, Matthew mix-up unaddressed, Zacchaeus didn't read as SHORT. This v2
build follows the rewritten 18-segment script (CLARITY/WHY-LAW + STUDY-GEM
TIDBITS, Bible section 4b) and all-new stills under the RELATIVE-PHYSICALITY
LOCK — every Zacchaeus frame has a taller adult for scale.

Hybrid storybook format per PRODUCTION-BIBLE.md: painted stills with Ken
Burns drift + 1 animated money-moment clip (the look up, stretched 8->8.4s),
narration (edge-tts), serif captions, KJV red-letter lines, closing question
card on cream #F7F2E9. Assembly Craft Laws throughout: supersampled zoompan,
RGBA caption fades, crf-16 intermediates, veryslow crf step-up final,
loudness lifted toward -15 LUFS, detuned-pair music beds.

Two-Voice Law: narrator modern American; Jesus speaks ONLY exact KJV
(Luke 19:5b split at its semicolon; 19:9b; 19:10). Music fully out before
the look up (bed1 ends 91.9) and before 19:9-10 (bed2 ends 194.5) so both
peaks land in sacred quiet.

All offsets computed from MEASURED mp3 durations after the ear-check
(all 18 segments passed; j1a re-taken at -22% after failing both models).

Output: 1080x1920 H.264, <25MB, 249.0s.
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
STILL_BOOTH = "shot1b-booth.jpeg"
STILL_BLOCKED = "shot2-blocked.jpeg"
STILL_RUN = "shot3-run.jpeg"
STILL_CLIMB = "shot4-climb.jpeg"
CLIP_LOOKUP = "clip-looked-up.mp4"
STILL_LIT = "shot5-lit.jpeg"
STILL_DOORWAY = "shot-doorway.jpeg"
STILL_COMEDOWN = "shot6-comedown.jpeg"
STILL_TABLE = "shot7-table.jpeg"
STILL_SALVATION = "shot8-salvation.jpeg"
STILL_SEEK = "shot9-seek.jpeg"

# (id, kind, source, clip_start, duration_s, zoom_dir, caption, style)
# Boundaries: 0, 11.7, 23.0, 33.6, 44.3, 53.2, 62.0, 72.5, 83.3, 94.0,
# 102.4, 107.4, 111.6, 122.9, 134.6, 144.9, 155.2, 165.1, 177.2, 189.1,
# 195.9, 203.9, 209.8, 220.2, 235.0, 249.0.  Long narration beats split
# into in/out zoom halves on the same still (zoom continuity chains).
SEGMENTS = [
    # n0 — the Matthew mix-up tidbit, up front (Cameron asked directly).
    ("n0a", "still", STILL_DESPISED, 0, 11.7, "in",
     "In Jericho lived a man named Zacchaeus.\n"
     "If you're thinking of Matthew — the tax\n"
     "collector who became an apostle — that's\n"
     "a different man. It's one of the most\n"
     "common mix-ups in the Bible.", "n"),
    ("n0b", "still", STILL_DESPISED, 0, 11.3, "out",
     "Matthew worked a tax booth up in Galilee.\n"
     "Zacchaeus ran the whole tax office\n"
     "in Jericho. And he was rich.", "n"),
    # n1 — WHY he was hated (new booth scene).
    ("n1a", "still", STILL_BOOTH, 0, 10.6, "in",
     "Here's why that mattered. Tax collectors\n"
     "worked for Rome — the empire occupying\n"
     "their own people — and got rich by\n"
     "charging extra and keeping the difference.", "n"),
    ("n1b", "still", STILL_BOOTH, 0, 10.7, "out",
     "So to his neighbors, Zacchaeus wasn't\n"
     "just a cheat. He was a traitor.\n"
     "No one greeted him. No one wanted\n"
     "him at their table.", "n"),
    # n2 — short, and the crowd is a wall.
    ("n2a", "still", STILL_BLOCKED, 0, 8.9, "in",
     "When Jesus came to Jericho, the whole\n"
     "city pressed into the street to see him.\n"
     "And Zacchaeus had a problem.", "n"),
    ("n2b", "still", STILL_BLOCKED, 0, 8.8, "out",
     "He was a short man — the scripture goes\n"
     "out of its way to mention it — and the\n"
     "crowd stood like a wall. Not one\n"
     "person made room for him.", "n"),
    # n3a — the run.
    ("n3a", "still", STILL_RUN, 0, 10.5, "in",
     "So this small, wealthy man did something\n"
     "no respectable person would ever do.\n"
     "He gathered up his fine robes, and he ran.", "n"),
    # n3b — the climb + dignity study gem.
    ("n3ba", "still", STILL_CLIMB, 0, 10.8, "in",
     "And he climbed a sycamore tree, like a\n"
     "child. Bible students love this detail:\n"
     "in that world, a grown man running\n"
     "and climbing was humiliating.", "n"),
    ("n3bb", "still", STILL_CLIMB, 0, 10.7, "out",
     "Zacchaeus traded the last of his dignity\n"
     "for one glimpse of Jesus — from a\n"
     "distance. He would have settled for that.", "n"),
    # MONEY MOMENT — the look up. bed1 fully out at 91.9; sacred quiet.
    # 8s Veo clip stretched to 8.4s (setpts 1.05) to bridge to j1a.
    ("n4", "clip", CLIP_LOOKUP, 0, 8.4, None,
     "He got far more. Jesus stopped — under\n"
     "that exact tree — looked up,\n"
     "and called him by name.", "n"),
    # Exact KJV Luke 19:5b split at its semicolon (Two-Voice Law).
    ("j1a", "still", STILL_LIT, 0, 5.0, "in",
     "\u201cZacchaeus, make haste,\nand come down;\u201d", "kjv"),
    ("j1b", "still", STILL_LIT, 0, 4.2, "out",
     "\u201cfor to day I must abide\nat thy house.\u201d", "kjv"),
    # n5 — WHY the meal was shocking (new doorway scene).
    ("n5a", "still", STILL_DOORWAY, 0, 11.3, "in",
     "Now — why would Jesus do that?\n"
     "Understand what a meal meant back then:\n"
     "to eat at a man's house was\n"
     "to publicly accept him.", "n"),
    ("n5b", "still", STILL_DOORWAY, 0, 11.7, "out",
     "Jesus didn't tell him to clean up his\n"
     "life first. He invited himself in —\n"
     "before Zacchaeus had changed a single\n"
     "thing. That is the point of the whole\n"
     "story. Jesus moves first.", "n"),
    # n6 — joy, and WHY the crowd grumbled (Full-Story law).
    ("n6a", "still", STILL_COMEDOWN, 0, 10.3, "in",
     "Zacchaeus came down faster than he had\n"
     "climbed up, and welcomed him with joy.\n"
     "But the crowd was appalled, and\n"
     "grumbled out loud —", "n"),
    ("n6b", "still", STILL_COMEDOWN, 0, 10.3, "out",
     "of every house in Jericho, he had chosen\n"
     "the worst man's. In their rules, you\n"
     "earned your way back before anyone\n"
     "sat at your table.", "n"),
    # n7 — the standing gift + the fourfold study gem.
    ("n7a", "still", STILL_TABLE, 0, 9.9, "in",
     "Then, at that table, it happened.\n"
     "Zacchaeus stood up in front of everyone:\n"
     "half of everything I own goes to the poor.", "n"),
    ("n7ba", "still", STILL_TABLE, 0, 12.1, "out",
     "And anyone I have cheated, I will pay\n"
     "back four times over. That number is a\n"
     "study gem: the law of Moses required\n"
     "fourfold repayment only for outright theft.", "n"),
    ("n7bb", "still", STILL_TABLE, 0, 11.9, "in",
     "Zacchaeus was judging himself by the\n"
     "harshest standard — and paying it gladly.\n"
     "Nobody demanded it. Being loved first\n"
     "is what changed him.", "n"),
    ("n7c", "still", STILL_TABLE, 0, 6.8, "out",
     "And Jesus answered him with the words\n"
     "this story was written to keep.", "n"),
    # Exact KJV Luke 19:9b and 19:10 — the TRUE last story words, in
    # sacred quiet (bed2 out at 194.5, j2a at 196.0).
    ("j2a", "still", STILL_SALVATION, 0, 8.0, "in",
     "\u201cThis day is salvation come to this house,\n"
     "forsomuch as he also is a son of Abraham.\u201d", "kjv"),
    ("j2b", "still", STILL_SALVATION, 0, 5.9, "out",
     "\u201cFor the Son of man is come to seek and\n"
     "to save that which was lost.\u201d", "kjv"),
    # n8 — WHY "son of Abraham" matters (3-word commentary precedent).
    ("n8", "still", STILL_SALVATION, 0, 10.4, "in",
     "A son of Abraham — with those words,\n"
     "Jesus gave him back his place in the\n"
     "family his whole city said he had forfeited.", "n"),
    # n9 — he was seeking (new road scene), fade to the card.
    ("n9", "still", STILL_SEEK, 0, 14.8, "in",
     "Jesus was not stuck in that crowd by\n"
     "accident. He was seeking. The man\n"
     "everyone stepped in front of was\n"
     "the one he came to find.", "n"),
    # Held 14.0s AND read aloud (Readable-Card Law); lines <=31 chars.
    ("card", "card", None, 0, 14.0, None,
     "Jesus called him by name\nbefore he changed anything.\n"
     "What would it mean to you —\nto be wanted like that,\n"
     "exactly as you are right now?", "close"),
]

# narration placements: (audio file, absolute start seconds)
# measured dur/tail: n0 22.128/.414  n1 20.736/.427  n2 17.184/.430
#   n3a 9.936/.397  n3b 20.184/.486  n4 7.704/.525  j1a 4.632/1.135
#   j1b 4.248/1.215  n5 22.392/.467  n6 19.944/.431  n7a 9.288/.438
#   n7b 23.376/.451  n7c 5.136/.560  j2a 8.016/1.232  j2b 5.928/1.187
#   n8 9.792/.466  n9 13.512/.458  n10 10.224/.424
# gaps computed from SPOKEN ends (dur - tail); all breaths 0.95-1.22s,
# sacred quiet 2.20s before n4 and 2.22s before j2a (planned).
AUDIO = [
    ("audio/n0.mp3", 0.4),     # shot1 0-23.0    Matthew mix-up (sp end 22.11)
    ("audio/n1.mp3", 23.1),    # booth 23.0-44.3 why hated (sp 43.41)
    ("audio/n2.mp3", 44.4),    # shot2 44.3-62.0 the wall (sp 61.15)
    ("audio/n3a.mp3", 62.1),   # shot3 62.0-72.5 the run (sp 71.64)
    ("audio/n3b.mp3", 72.6),   # shot4 72.5-94.0 the climb gem (sp 92.30)
    # 2.20s sacred quiet — bed1 fully out at 91.9
    ("audio/n4.mp3", 94.5),    # clip 94.0-102.4 the look up (sp 101.68)
    ("audio/j1a.mp3", 102.9),  # shot5 102.4-107.4 KJV 19:5b pt1 (sp 106.40)
    ("audio/j1b.mp3", 107.5),  # shot5 107.4-111.6 KJV 19:5b pt2 (sp 110.53)
    ("audio/n5.mp3", 111.7),   # doorway 111.6-134.6 meal = acceptance (sp 133.63)
    ("audio/n6.mp3", 134.7),   # shot6 134.6-155.2 joy + grumbling (sp 154.21)
    ("audio/n7a.mp3", 155.3),  # shot7 155.2-165.1 half to the poor (sp 164.15)
    ("audio/n7b.mp3", 165.2),  # shot7 165.1-189.1 fourfold gem (sp 188.13)
    ("audio/n7c.mp3", 189.2),  # shot7 189.1-195.9 bridge (sp 193.78)
    # 2.22s sacred quiet — bed2 fully out at 194.5
    ("audio/j2a.mp3", 196.0),  # shot8 195.9-203.9 KJV 19:9b (sp 202.78)
    ("audio/j2b.mp3", 204.0),  # shot8 203.9-209.8 KJV 19:10 (sp 208.74)
    ("audio/n8.mp3", 209.9),   # shot8 209.8-220.2 son of Abraham (sp 219.23)
    ("audio/n9.mp3", 220.3),   # shot9 220.2-235.0 he was seeking (sp 233.35)
    ("audio/n10.mp3", 235.5),  # card 235.0-249.0 read aloud (sp 245.30)
]

BED1_END = 91.9              # fully silent before the look up
BED2_START, BED2_END = 134.0, 194.5  # out before KJV 19:9-10


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
    if seg_id == "n9":
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    fc = assemble_segment(seg_id, base, dur, cap, style, tail)
    run(["ffmpeg", "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_clip(seg_id, src, start, dur, cap, style):
    """Veo clip segment, stretched 1.05x (8s source -> 8.4s) so the look-up
    holds through the whole n4 line without a hard cut mid-motion."""
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
    # bed1 under the setup (0-91.9), fully out before the look up.
    bed1 = (f"aevalsrc='0.022*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
            f"+0.016*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))"
            f"+0.012*sin(2*PI*220*t)+0.008*sin(2*PI*329.63*t)'"
            f":s=44100:d={BED1_END},"
            f"lowpass=f=750,tremolo=f=0.13:d=0.3,"
            f"aecho=0.7:0.4:311|429:0.25|0.18,"
            f"afade=t=in:st=0:d=6,afade=t=out:st={BED1_END-5}:d=5[mus1]")
    filters.append(bed1)
    labels.append("[mus1]")
    # bed2 warm and quieter under the coming-down + table section
    # (134.0-194.5), fully out before KJV 19:9-10 at 196.0.
    m2_dur = BED2_END - BED2_START
    bed2 = (f"aevalsrc='0.014*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
            f"+0.011*(sin(2*PI*138.59*t)+sin(2*PI*139.2*t))"
            f"+0.009*sin(2*PI*164.81*t)+0.006*sin(2*PI*220*t)'"
            f":s=44100:d={m2_dur},"
            f"lowpass=f=700,tremolo=f=0.11:d=0.3,"
            f"aecho=0.7:0.4:317|443:0.25|0.18,"
            f"afade=t=in:st=0:d=5,afade=t=out:st={m2_dur-6}:d=6,"
            f"adelay={int(BED2_START*1000)}|{int(BED2_START*1000)}[mus2]")
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
    # 249s runtime: 24.5MB/249s = 787kbps total budget, so the video cap
    # must be ~640k (v1's 1200k cap fit only because v1 was 131s).
    for crf in (21, 22, 23, 24):
        run(["ffmpeg", "-y", "-i", f"{S}/video_silent.mp4",
             "-i", f"{S}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "veryslow", "-crf", str(crf),
             "-maxrate", "640k", "-bufsize", "1280k", "-pix_fmt", "yuv420p",
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
