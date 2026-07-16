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

# Intermediate segments near-lossless (crf 16) so the final pass is the
# ONLY lossy generation the viewer sees (2026-07-09 quality pass).
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

STILL_LEAVING = "shot1-leaving.jpeg"
STILL_PIGPEN = "shot2-pig-pen.jpeg"
STILL_ROAD = "shot3-road-home.jpeg"
STILL_SEEN = "shot4-seen-far-off.jpeg"
STILL_RUNS = "Father_running_down_road_2K_202607111606.jpeg"  # was clip-father-runs.mp4 (Phase-1 stills-only)
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
    ("s05", "still", STILL_RUNS, 8.0, "in",
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
        z = f"1.001+0.12*on/{frames}"
    else:
        z = f"1.121-0.12*on/{frames}"
    base = (f"[0:v]scale=4320:7680,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ""
    if seg_id == "s00":
        tail = ",fade=t=in:st=0:d=1.2"
    if seg_id == "s12b":
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
    # 2026-07-09 quality pass: the old bed was four bare sine waves — thin
    # and synthetic. Each voice is now a slightly DETUNED pair (natural slow
    # beating, like real strings) run through a soft room echo. And the
    # second half no longer plays bone dry: a quieter, warmer bed sits under
    # the feast and the older brother (70.5-130.5), fading to full silence
    # before the father's final KJV answer so the last words land in the
    # same sacred quiet as "The father ran."
    # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
    bed1 = (f"aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
            f"+0*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))"
            f"+0*sin(2*PI*220*t)+0*sin(2*PI*329.63*t)'"
            f":s=44100:d={MUSIC_END},"
            f"lowpass=f=750,tremolo=f=0.13:d=0.3,"
            f"aecho=0.7:0.4:311|429:0.25|0.18,"
            f"afade=t=in:st=0:d=6,afade=t=out:st={MUSIC_END-5}:d=5[mus1]")
    filters.append(bed1)
    labels.append("[mus1]")
    m2_start, m2_dur = 70.5, 60.0  # out at 130.5, before j2a at 131.9
    # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
    bed2 = (f"aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
            f"+0*(sin(2*PI*138.59*t)+sin(2*PI*139.2*t))"
            f"+0*sin(2*PI*164.81*t)+0*sin(2*PI*220*t)'"
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

    # ---- loudness: measure the mix, lift to social-platform level ----
    # 2026-07-09 quality pass: quiet audio reads as amateur. Measure the
    # integrated loudness (EBU R128) and apply a static gain toward -15
    # LUFS with a true-peak limiter — no dynamics pumping, just level.
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

    # ---- final mux, best quality that fits the <25MB law ----
    # preset veryslow buys real quality at the same bitrate; start generous
    # and step crf up only if the size law demands it.
    for crf in (21, 22, 23, 24):
        run(["ffmpeg", "-y", "-i", f"{S}/video_silent.mp4",
             "-i", f"{S}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "veryslow", "-crf", str(crf),
             "-maxrate", "1200k", "-bufsize", "2400k", "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
             "luke-15_prodigal-son.mp4"])
        size = os.path.getsize("luke-15_prodigal-son.mp4") / 1e6
        if size <= 24.5:
            break
        print(f"  {size:.1f} MB at crf {crf} — over budget, stepping up")
    print(f"DONE: luke-15_prodigal-son.mp4  {size:.1f} MB, {total:.1f}s (crf {crf})")


if __name__ == "__main__":
    main()
