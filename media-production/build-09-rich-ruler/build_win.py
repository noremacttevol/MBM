#!/usr/bin/env python3
"""Assemble Story Video #9 — The Rich Young Ruler (Mark 10:17-22).
Phase-1 STILLS-ONLY (Law E) + Correction #18 rebuild on Elli's Windows laptop.

Both Veo clips removed: the RUN (s1-the-run.mp4 -> s1-run-anchor still) and
the WALK-AWAY (s6-walk-away.mp4 -> the regenerated s7 still). s7 regenerated
so the Lord is seen from DIRECTLY BEHIND (the old s7 leaked a profile cheek/
eye). Every other still kept: the rich young man's own face is allowed (he is
not the Lord). Durations, captions, narration offsets and music beds are
UNCHANGED from the approved cut — only the two clip beats became stills.

Two-Voice Law: narrator modern American; Jesus ONLY exact KJV (Mark 10:21).
Music: sparse beds, FULL SILENCE before j1, music DIES at n5 ("Jesus let him
go") and never returns — the ending stays in sorrow.

Windows build: ffmpeg full path, Georgia serif fonts, UTF-8 captions,
supersample increase+crop for the 9:16-ish sources.
Output: mark-10_rich-young-ruler.mp4, 1080x1920 H.264 30fps, <25MB, 217.4s.
"""
import os
import subprocess

FF = ("C:/Users/ellil/AppData/Local/Microsoft/WinGet/Packages/"
      "Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/"
      "ffmpeg-8.1.2-full_build/bin/ffmpeg.exe")
A, S, FPS = "assets", "segs", 30
SERIF = "C\\:/Windows/Fonts/georgia.ttf"
SERIF_BI = "C\\:/Windows/Fonts/georgiai.ttf"
CREAM, INK = "0xF7F2E9", "0x3B2A1E"
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1A = "s1-run-anchor.jpeg"          # run clip -> still
S2 = "s2-kneeling-earnest.jpeg"
S3 = "s3-the-look.jpeg"
S4 = "s4-the-one-thing.jpeg"
S5 = "s5-words-land.jpeg"
S7 = "s7-he-let-him-go.jpeg"        # regenerated fully-behind; also walk-away
S8 = "s8-empty-road.jpeg"

# (id, kind, src, dur, zoom_dir, caption, style)
SEGMENTS = [
    ("n0a", "still", S1A, 12.8, "in",
     "Jesus was setting out on a journey when\n"
     "a young man came running down the road\n"
     "after him. Running. You need to\n"
     "understand what that looked like.", "n"),
    ("n0b", "still", S2, 15.2, "in",
     "This man was wealthy — fine robes, gold\n"
     "rings, a name people knew. Men like that\n"
     "did not run in public. It was beneath\n"
     "them. He ran anyway, in front of everyone,\n"
     "and dropped to his knees in the dust\n"
     "at Jesus's feet.", "n"),
    ("n1a", "still", S2, 18.4, "out",
     "He asked the question he had been\n"
     "carrying, maybe his whole life. Good\n"
     "teacher — what do I have to do to live\n"
     "forever with God? Jesus pointed him to\n"
     "the commandments. Don't cheat anyone.\n"
     "Don't steal. Don't lie. Honor your\n"
     "father and your mother.", "n"),
    ("n1b", "still", S2, 19.2, "in",
     "And the young man answered: Teacher,\n"
     "I have kept every one of them since I\n"
     "was a boy. And here is the thing. He\n"
     "meant it. This was not a proud man\n"
     "showing off. This was a student who had\n"
     "done all the homework, kneeling in the\n"
     "dirt, asking if it was enough.", "n"),
    ("n2a", "still", S3, 13.4, "in",
     "Mark writes what happened next in five\n"
     "words. Jesus, looking at him, loved him.\n"
     "Of all the people in Mark's story, this\n"
     "is the one he says it about, straight out.", "n"),
    ("n2b", "still", S3, 13.8, "out",
     "Jesus looked at this man — his sincerity,\n"
     "his gold rings, his hope — and loved him.\n"
     "And then, with love in his voice, he said\n"
     "the hardest sentence in the book.", "n"),
    ("j1a", "still", S4, 7.8, "in",
     "“One thing thou lackest: go thy way,\n"
     "sell whatsoever thou hast,\nand give to the poor,”", "kjv"),
    ("j1b", "still", S4, 8.0, "out",
     "“and thou shalt have treasure in heaven:\n"
     "and come, take up the cross,\nand follow me.”", "kjv"),
    ("n3a", "still", S4, 16.0, "in",
     "You're missing one thing. Not one more\n"
     "rule. One thing standing between you\n"
     "and God. Sell what you have. Give it to\n"
     "the people who have nothing. And then —\n"
     "come, follow me.", "n"),
    ("n3b", "still", S3, 16.6, "out",
     "Hear that last part. It was an invitation.\n"
     "The same words Jesus used to call Peter,\n"
     "and Andrew, and James, and John. He was\n"
     "being invited into the inner circle. It\n"
     "just came wrapped in the one thing this\n"
     "man could not put down.", "n"),
    ("n4a", "still", S5, 12.8, "in",
     "His face fell. And he walked away\n"
     "grieved — because he was very rich.\n"
     "Notice what the text does not say. It\n"
     "does not say he stopped believing. It\n"
     "does not say he argued.", "n"),
    ("n4b", "still", S7, 12.8, "in",
     "He grieved — because he believed every\n"
     "word, and the price was the thing he\n"
     "loved most. He turned around, and he\n"
     "walked back down that road toward\n"
     "everything he owned.", "n"),
    ("n5", "still", S7, 16.6, "out",
     "And Jesus let him go. He did not lower\n"
     "the bar. He did not soften the terms.\n"
     "He did not chase him down the road.\n"
     "He stood there, and he watched him walk\n"
     "away — and he loved him the whole time.", "n"),
    ("n6a", "still", S8, 10.0, "out",
     "The road emptied. The sun went down.\n"
     "And the story just ends there — Mark\n"
     "leaves it exactly that sad, on purpose.", "n"),
    ("n6b", "still", S8, 10.4, "in",
     "Sit with it. A love that will not force\n"
     "you. Is that weakness — or is it the\n"
     "deepest respect you have ever been\n"
     "shown?", "n"),
    ("card", "card", None, 13.6, None,
     "Is there something\nyou already know — quietly —\n\n"
     "that stands between you\nand fully following\n"
     "what you believe?", "close"),
]

AUDIO = [
    ("audio/n0.mp3", 0.4), ("audio/n1.mp3", 28.2), ("audio/n2.mp3", 65.8),
    ("audio/j1.mp3", 93.5), ("audio/n3.mp3", 109.0), ("audio/n4.mp3", 141.4),
    ("audio/n5.mp3", 168.0), ("audio/n6.mp3", 184.4), ("audio/n7.mp3", 205.0),
]

# sparse beds; FULL SILENCE before j1; music dies at n5 (168.0) and never returns.
BEDS = [(0.0, 91.3, "a"), (109.5, 167.3, "b")]


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("FFMPEG ERROR:\n", r.stderr[-1600:], flush=True)
        raise SystemExit(1)


def caption_overlay(seg_id, dur, text, style):
    if not text:
        return None
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w", encoding="utf-8") as f:
        f.write(text)
    if style == "kjv":
        font, size, color = SERIF_BI, 46, "0xFFF3DC"
    else:
        font, size, color = SERIF, 40, "white"
    fo = max(0.0, dur - 0.6)
    return (f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile='{font}':textfile='{tf}':fontsize={size}:"
            f"fontcolor={color}:line_spacing=14:x=(w-text_w)/2:"
            f"y=min(h-460\\,h-150-text_h):shadowcolor=black@0.85:shadowx=2:shadowy=2:"
            f"box=1:boxcolor=black@0.34:boxborderw=18,"
            f"fade=t=in:st=0:d=0.5:alpha=1,fade=t=out:st={fo}:d=0.5:alpha=1[cap]")


def assemble(seg_id, base, dur, cap, style, tail=""):
    capf = caption_overlay(seg_id, dur, cap, style)
    if capf:
        return f"{base}[base];{capf};[base][cap]overlay=format=auto{tail}[v]"
    return f"{base}{tail}[v]"


def build_still(seg_id, src, dur, zdir, cap, style):
    frames = int(dur * FPS)
    z = f"1.001+0.09*on/{frames}" if zdir == "in" else f"1.091-0.09*on/{frames}"
    base = (f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,"
            f"crop=2160:3840,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},scale=1080:1920:flags=lanczos")
    tail = ""
    if seg_id == "n0a":
        tail = ",fade=t=in:st=0:d=1.2"
    if seg_id == "n6b":
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", assemble(seg_id, base, dur, cap, style, tail),
         "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(seg_id, dur, text):
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w", encoding="utf-8") as f:
        f.write(text)
    vf = (f"drawtext=fontfile='{SERIF}':textfile='{tf}':fontsize=50:"
          f"fontcolor={INK}:line_spacing=22:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run([FF, "-y", "-f", "lavfi", "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/{seg_id}.mp4"])


def bed_filter(idx, start, end, style):
    dur = end - start
    if style == "a":
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
               "+0*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))"
               "+0*sin(2*PI*220*t)+0*sin(2*PI*329.63*t)'")
        eq = "lowpass=f=750,tremolo=f=0.13:d=0.3,aecho=0.7:0.4:311|429:0.25|0.18"
        fin, fout = 6, 5
    else:
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
               "+0*(sin(2*PI*138.59*t)+sin(2*PI*139.2*t))"
               "+0*sin(2*PI*164.81*t)+0*sin(2*PI*220*t)'")
        eq = "lowpass=f=700,tremolo=f=0.11:d=0.3,aecho=0.7:0.4:317|443:0.25|0.18"
        fin, fout = 5, 6
    if dur < fin + fout + 2:
        fin = fout = max(2, int((dur - 2) / 2))
    ms = int(start * 1000)
    delay = f",adelay={ms}|{ms}" if ms else ""
    return (f"{src}:s=44100:d={dur},{eq},afade=t=in:st=0:d={fin},"
            f"afade=t=out:st={dur-fout}:d={fout}{delay}[mus{idx}]")


def main():
    os.makedirs(S, exist_ok=True)
    total = sum(s[3] for s in SEGMENTS)
    print(f"total runtime: {total:.1f}s", flush=True)
    for seg_id, kind, src, dur, zdir, cap, style in SEGMENTS:
        if kind == "still":
            build_still(seg_id, src, dur, zdir, cap, style)
        else:
            build_card(seg_id, dur, cap)
    with open(f"{S}/concat.txt", "w", encoding="utf-8") as f:
        for seg in SEGMENTS:
            f.write(f"file '{seg[0]}.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    inputs, filters, labels = [], [], []
    for i, (path, start) in enumerate(AUDIO):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    for bi, (bs, be, st) in enumerate(BEDS):
        filters.append(bed_filter(bi, bs, be, st))
        labels.append(f"[mus{bi}]")
    n = len(labels)
    filters.append("".join(labels) + f"amix=inputs={n}:duration=longest:normalize=0,"
                   f"apad=whole_dur={total}[aout]")
    run([FF, "-y"] + inputs + ["-filter_complex", ";".join(filters),
        "-map", "[aout]", "-t", str(total), "-c:a", "aac", "-b:a", "160k",
        f"{S}/audio_mix.m4a"])

    probe = subprocess.run([FF, "-i", f"{S}/audio_mix.m4a", "-af", "ebur128",
                            "-f", "null", "-"], capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            try:
                lufs = float(line.split()[1])
            except ValueError:
                pass
    gain = 0.0 if lufs is None else max(-6.0, min(12.0, -15.0 - lufs))
    print(f"loudness: {lufs} LUFS, gain {gain:+.1f} dB", flush=True)

    OUT = "mark-10_rich-young-ruler.mp4"
    vcap = max(300, int(24.5 * 8000 / total) - 145)
    size, crf = 0.0, 21
    for crf in (21, 22, 23, 24, 25):
        run([FF, "-y", "-i", f"{S}/video_silent.mp4", "-i", f"{S}/audio_mix.m4a",
             "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "veryslow",
             "-crf", str(crf), "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p", "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", OUT])
        size = os.path.getsize(OUT) / 1e6
        if size <= 24.5:
            break
    print(f"DONE: {OUT}  {size:.1f} MB, {total:.1f}s (crf {crf})", flush=True)


if __name__ == "__main__":
    main()
