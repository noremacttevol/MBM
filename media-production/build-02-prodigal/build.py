#!/usr/bin/env python3
"""Assemble Story Video #2 — The Prodigal Son (Luke 15:11-32).
Hybrid storybook format per PRODUCTION-BIBLE.md: painted stills with Ken Burns
drift + 1 animated money-moment clip (s05 THE FATHER RUNS), narration
(edge-tts), serif captions, KJV red-letter line, closing question card on
cream #F7F2E9.

Built via the section 4b RIGHT-FIRST-TIME PRE-FLIGHT (see PREFLIGHT.md) —
plan checked on paper before any generation. All offsets below computed from
MEASURED mp3 durations after the ear-check (all 11 segments matched 1.00).

Two-Voice Law: narrator modern American; Jesus voice speaks ONLY exact KJV
(Luke 15:24 at the feast; Luke 15:31-32 to the older brother — the TRUE last
story words). Music fades to full silence BEFORE "The father ran." so the
peak lands in sacred quiet.

2026-07-09: Cameron caught that the first cut told only HALF the parable —
it ended at the feast and omitted the older brother (Luke 15:25-32), the half
aimed at the religious men the story answers. Second half added: the brother
outside, the father's second going-out, the complaint, and the father's
answer as the closing KJV. Full-Story check added to Bible section 4b.

Opens with the "why Jesus told it" bookend (pattern Cameron approved on #8/#6).
Closing card held 14.5s AND read aloud (Readable-Card Law).

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

STILL_LEAVING = "shot1-leaving.jpeg"
STILL_PIGPEN = "shot2-pig-pen.jpeg"
STILL_ROAD = "shot3-road-home.jpeg"
STILL_SEEN = "shot4-seen-far-off.jpeg"
CLIP_RUNS = "clip-father-runs.mp4"
STILL_EMBRACE = "shot6-embrace.jpeg"
STILL_FEAST = "shot7-feast.jpeg"
STILL_BROTHER = "shot8-brother-outside.jpeg"
STILL_ENTREAT = "shot9-father-entreats.jpeg"

# (id, kind, source, duration_s, zoom_dir, caption, caption_style)
SEGMENTS = [
    # Opening bookend — why Jesus told this story. Reuses the shot-4 road
    # landscape (the road the whole story travels), slow zoom out.
    ("s00", "still", STILL_SEEN, 12.4, "out",
     "When religious men complained that Jesus\n"
     "spent his time with sinners, he didn't argue.\n"
     "He answered with a story, about a father\nand his two sons.", "n"),
    ("s01", "still", STILL_LEAVING, 12.5, "in",
     "The younger son asked for his inheritance\n"
     "early — as if to say he wished his father\n"
     "were already dead. Then he left, and poured\n"
     "it all out on a life that emptied him.", "n"),
    ("s02", "still", STILL_PIGPEN, 12.8, "in",
     "When the money was gone, a famine came.\n"
     "He ended up feeding pigs, so hungry he\n"
     "would have eaten what they ate. And there,\n"
     "in the mud, he came to his senses.", "n"),
    ("s03", "still", STILL_ROAD, 10.7, "in",
     "So he started walking home, rehearsing\n"
     "a speech the whole way. Father, I am not\n"
     "worthy to be called your son.\n"
     "Make me one of your servants.", "n"),
    # The held breath before the run.
    ("s04", "still", STILL_SEEN, 5.1, "in",
     "He was still a long way off...\nwhen his father saw him.", "n"),
    # MONEY MOMENT — the father runs. Music has already cut to full
    # silence before "The father ran." lands (peak per pack).
    ("s05", "clip", CLIP_RUNS, 8.0, None,
     "The father ran.\nOld men in that world did not run.\n"
     "It was beneath their dignity.\nHe ran anyway.", "n"),
    # Stillness after motion lands harder — the embrace, held long.
    ("s06", "still", STILL_EMBRACE, 9.0, "in",
     "He didn't wait for the speech.\nHe wrapped his arms around his son\n"
     "before a single word was said.", "n"),
    ("s07a", "still", STILL_FEAST, 10.5, "in",
     "That night the father dressed him in the\n"
     "finest robe, put a ring on his hand, and\n"
     "called for a feast — and he told\neveryone why.", "n"),
    # Exact KJV Luke 15:24. Narrator never re-quotes or echoes this line
    # after it (Translation Law).
    ("s07b", "still", STILL_FEAST, 7.4, "out",
     "\u201cFor this my son was dead,\nand is alive again;\n"
     "he was lost, and is found.\u201d", "kjv"),
    # ---- SECOND HALF: the older brother (Luke 15:25-32), 2026-07-09 ----
    ("s08", "still", STILL_BROTHER, 17.0, "in",
     "But Jesus wasn't finished. The older son\n"
     "was still out in the field, like always.\n"
     "When he heard the music, a servant told him:\n"
     "your brother is home. And he was so angry,\nhe refused to go in.", "n"),
    ("s09", "still", STILL_ENTREAT, 7.5, "in",
     "So the father left his own feast,\nand went out again — this time\n"
     "to the son who had never left.", "n"),
    ("s10", "still", STILL_ENTREAT, 11.7, "out",
     "The older son's hurt poured out.\nAll these years I have served you.\n"
     "I never disobeyed you. And you never gave me\n"
     "even a young goat, to celebrate with my friends.", "n"),
    ("s11", "still", STILL_BROTHER, 6.9, "out",
     "The father didn't argue with him, either.\n"
     "Jesus gave him the last words of the story.", "n"),
    # Exact KJV Luke 15:31-32 — the TRUE last spoken story words.
    ("s12a", "still", STILL_ENTREAT, 5.7, "in",
     "\u201cSon, thou art ever with me,\nand all that I have is thine.\u201d",
     "kjv"),
    ("s12b", "still", STILL_ENTREAT, 11.1, "out",
     "\u201cIt was meet that we should make merry,\n"
     "and be glad: for this thy brother was dead,\n"
     "and is alive again; and was lost,\nand is found.\u201d", "kjv"),
    # Held 14.5s AND read aloud, gently (Readable-Card Law; n8 runs 11.6s
    # so the hold is stretched past 13.0 to keep speech clear of the fade).
    # Lines kept ≤31 chars — the first break clipped at both edges at 50pt
    # (caption-crop QC caught it, 2026-07-09).
    ("s13", "card", None, 14.5, None,
     "Which one feels closest to\nwhere you are right now —\n"
     "the son who left,\nthe father who ran to meet him,\n"
     "or the brother who stayed,\nand felt unseen?", "close"),
]

# narration placements: (audio file, absolute start seconds)
# measured durations: n0 11.784  n1 12.096  n2 12.336  n3 10.272  n4 4.080
#                     n5a 1.536  n5b 6.672  n6 6.864   n7 12.024
#                     j1 7.848   n8 6.648
AUDIO = [
    ("audio/n0.mp3", 0.4),    # s00 0-12.4    why Jesus told it (ends 12.184)
    ("audio/n1.mp3", 12.5),   # s01 12.4-24.9 the leaving (ends 24.596)
    ("audio/n2.mp3", 25.0),   # s02 24.9-37.7 pig pen (ends 37.336)
    ("audio/n3.mp3", 37.8),   # s03 37.7-48.4 road home (ends 48.072)
    ("audio/n4.mp3", 48.5),   # s04 48.4-53.5 seen far off (ends 52.580)
    # planned 1.52s silent breath — music already fully out (MUSIC_END 53.2)
    ("audio/n5a.mp3", 54.1),  # s05 53.5-61.5 "The father ran." (ends 55.636)
    ("audio/n5b.mp3", 56.4),  # s05           dignity/ran anyway (ends 63.072)
    ("audio/n6.mp3", 63.5),   # s06 61.5-70.5 the embrace (ends 70.364)
    # All gaps below computed from SPOKEN ends (dur minus measured internal
    # tail; Jesus-voice files carry ~1.15s tails — j1 1.16, j2a 1.12, j2b 1.17)
    ("audio/n7.mp3", 70.7),    # s07a 70.5-81.0  feast (10.008, spoken end 80.32)
    ("audio/j1.mp3", 81.2),    # s07b 81.0-88.4  KJV 15:24 (spoken end 87.88)
    ("audio/n9.mp3", 88.4),    # s08 88.4-105.4  brother outside (16.752, sp 104.74)
    ("audio/n10a.mp3", 105.5), # s09 105.4-112.9 father goes out (7.368, sp 112.40)
    ("audio/n10b.mp3", 113.0), # s10 112.9-124.6 the complaint (11.592, sp 124.14)
    ("audio/n11.mp3", 124.7),  # s11 124.6-131.5 bridge to answer (6.744, sp 131.01)
    ("audio/j2a.mp3", 131.9),  # s12a 131.5-137.2 KJV 15:31 (5.904, sp 136.69)
    ("audio/j2b.mp3", 137.4),  # s12b 137.2-148.3 KJV 15:32 (11.400, sp 147.63)
    # planned ~2.3s breath before the closing question (from j2b SPOKEN end)
    ("audio/n8.mp3", 149.5),   # s13 148.3-162.8 card read aloud (11.568, sp 160.64)
                               # 149.9 measured a 2.50s gap at -38dB — right at the
                               # No-Dead-Air limit; pulled to 149.5 (2026-07-09).
]

MUSIC_END = 53.2  # fully silent before "The father ran." — the peak is quiet


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
    if seg_id == "s12b":
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
    os.makedirs(S, exist_ok=True)
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
         # 162.8s runtime: 1050k video + 128k audio ≈ 24MB ceiling — under 25MB.
         "-c:v", "libx264", "-preset", "slow", "-crf", "24",
         "-maxrate", "1050k", "-bufsize", "2100k", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
         "prodigal-02.mp4"])
    size = os.path.getsize("prodigal-02.mp4") / 1e6
    print(f"DONE: prodigal-02.mp4  {size:.1f} MB, {total:.1f}s")


if __name__ == "__main__":
    main()
