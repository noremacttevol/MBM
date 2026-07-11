#!/usr/bin/env python3
"""Assemble Story Video #10 — The Woman at the Well (John 4:4-30, 39-42).
Phase-1 STILLS-ONLY (Law E) rebuild on Elli's Windows laptop.

The approved V3 cut used 2 Veo clips (the conversation, the jar-run). Law E:
both removed and replaced with their existing anchor stills — the conversation
(s5-conversation-anchor) and the jar left behind (s7-jar-left-anchor). Zoom
directions alternate across the long well conversation so the drift never
resets flat. Correction #18 re-audit PASSED with no regeneration: the Lord is
shown only from behind (s2) and over-the-shoulder (s5, s6) — no face, no glow.
Durations, captions, narration offsets and music beds are UNCHANGED from V3.

Two-Voice Law: narrator modern American; Jesus ONLY exact KJV (John 4:13-14,
4:26). Music: beds die before "he did not turn away"; j2 "I am he" in silence;
warm bed for the run/harvest, out before the card.

Windows build: ffmpeg full path, Georgia serif fonts, UTF-8 captions,
supersample increase+crop. Output: john-4_woman-at-the-well.mp4, 311.0s, <25MB.
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

S1 = "s1-noon-path.jpeg"
S2 = "s2-traveler.jpeg"
S3 = "s3-disbelief.jpeg"
S4 = "s4-living-water.jpeg"
S5 = "s5-conversation-anchor.jpeg"   # conversation clip -> still
S6 = "s6-disciples.jpeg"
S7 = "s7-jar-left-anchor.jpeg"       # jar-run clip -> still
S8 = "s8-come-and-see.jpeg"
S9 = "s9-road-filling.jpeg"

# (id, kind, src, dur, zoom_dir, caption, style)
SEGMENTS = [
    ("n0a", "still", S1, 15.5, "in",
     "A woman walked out to a well at noon —\n"
     "the hottest, emptiest hour of the day.\n"
     "You need to understand what that hour\n"
     "means. Women drew their water in the\n"
     "cool of the morning, together. It was\n"
     "where the talk happened.", "n"),
    ("n0b", "still", S1, 15.5, "out",
     "She came at noon because of the talk.\n"
     "Five marriages behind her, living now\n"
     "with a man who wasn't her husband — and\n"
     "the whole town knew every chapter. Noon\n"
     "was the hour with nobody in it. She\n"
     "chose it on purpose.", "n"),
    ("n1a", "still", S2, 14.3, "in",
     "But this day, somebody was there. A\n"
     "traveler sat by the well, worn out from\n"
     "the road — a Jewish man, resting in\n"
     "Samaria. That detail matters more than\n"
     "it sounds.", "n"),
    ("n1b", "still", S2, 14.3, "out",
     "Jews and Samaritans had despised each\n"
     "other for seven hundred years. They\n"
     "didn't share roads if they could help\n"
     "it, didn't share tables, and certainly\n"
     "didn't share water. Everything in her\n"
     "body said: turn around.", "n"),
    ("n2a", "still", S3, 17.0, "in",
     "Then he spoke to her. He asked her for\n"
     "a drink. Understand how impossible that\n"
     "sentence was. A rabbi did not speak to\n"
     "an unknown woman in public — and no Jew\n"
     "asked a Samaritan for anything.", "n"),
    ("n2b", "still", S3, 16.8, "out",
     "He broke both walls at once, and he did\n"
     "it by needing her help. She almost\n"
     "laughed. How is it that you, a Jew,\n"
     "would ask me for water? And he answered\n"
     "that if she knew who was asking, she\n"
     "would have asked him — and he would\n"
     "have given her living water.", "n"),
    ("n3", "still", S4, 16.6, "in",
     "She pointed out the obvious — the well\n"
     "is deep, sir, and you don't even have a\n"
     "rope. This well came from Jacob himself.\n"
     "Are you greater than Jacob? She meant it\n"
     "as a corner. He stepped right into it.", "n"),
    ("j1a", "still", S4, 8.5, "in",
     "“Whosoever drinketh of this water\n"
     "shall thirst again: But whosoever\n"
     "drinketh of the water that I shall give\n"
     "him shall never thirst;”", "kjv"),
    ("j1b", "still", S4, 8.5, "out",
     "“but the water that I shall give him\n"
     "shall be in him a well of water\n"
     "springing up into everlasting life.”", "kjv"),
    ("n4", "still", S4, 15.6, "out",
     "A well inside you — springing up, not\n"
     "running dry. He wasn't talking about\n"
     "the water in the jar. He was talking\n"
     "about the thirst underneath the thirst.\n"
     "The one you can't carry a jar big\n"
     "enough for.", "n"),
    ("n5a", "still", S5, 12.8, "out",
     "Then he said: go get your husband. And\n"
     "the whole conversation changed. I have\n"
     "no husband, she said. And he agreed\n"
     "with her — gently, and completely.", "n"),
    ("n5b", "still", S5, 24.4, "in",
     "Five husbands, he said. And the man you\n"
     "have now is not one. He already knew.\n"
     "All of it. Every chapter the town\n"
     "whispered about — he said it out loud,\n"
     "to her face. And he did not turn away.\n"
     "He stayed in the conversation. She came\n"
     "for water, and found herself fully\n"
     "known — and still spoken to with respect.", "n"),
    ("n6a", "still", S5, 15.5, "out",
     "She called him a prophet. She asked him\n"
     "her people's oldest question — which\n"
     "mountain is the right one to worship\n"
     "on — and he told her the day was coming\n"
     "when the question itself would be old\n"
     "news:", "n"),
    ("n6b", "still", S5, 15.5, "in",
     "God is spirit, and what he wants is the\n"
     "heart. Then she said, almost to herself:\n"
     "I know the Messiah is coming. When he\n"
     "comes, he'll explain everything. And the\n"
     "tired traveler at the well said:", "n"),
    ("j2", "still", S5, 5.0, "out",
     "“I that speak unto thee am he.”", "kjv"),
    ("n7a", "still", S6, 14.4, "in",
     "The first person Jesus ever told plainly\n"
     "that he was the Messiah — not a king,\n"
     "not a priest, not even one of his\n"
     "twelve — a Samaritan woman with five\n"
     "marriages behind her, at the bottom of\n"
     "every list her world kept.", "n"),
    ("n7b", "still", S6, 14.4, "out",
     "Right then his followers came back from\n"
     "town, and stopped short — stunned that\n"
     "he was talking with her at all. Nobody\n"
     "dared say a word.", "n"),
    ("n8a", "still", S7, 11.0, "in",
     "And look what she did. She left the jar.\n"
     "The thing she walked all that way in\n"
     "the heat to fill — she left it standing\n"
     "at the well, and she ran.", "n"),
    ("n8b", "still", S7, 12.8, "out",
     "Ran toward the town she had spent years\n"
     "avoiding, to the very people she came\n"
     "out at noon to miss, shouting: come see\n"
     "a man who told me everything I ever did.", "n"),
    ("n9a", "still", S8, 14.0, "in",
     "And they came. The town that whispered\n"
     "about her followed her up the road to\n"
     "see for themselves. Many believed\n"
     "because of her word —", "n"),
    ("n9b", "still", S9, 14.6, "out",
     "the woman who wouldn't meet their eyes\n"
     "at sunrise became the first missionary\n"
     "in that gospel by sundown. They asked\n"
     "him to stay, and he stayed two days —\n"
     "with Samaritans. And they told her: now\n"
     "we've heard him ourselves. We know.", "n"),
    ("card", "card", None, 14.0, None,
     "She came for one thing,\nand found out she was thirsty\n"
     "for something much deeper.\n\n"
     "Have you ever been searching\nfor something — and realized later\n"
     "it was deeper than what you\nthought you wanted?", "close"),
]

AUDIO = [
    ("audio/n0.mp3", 0.4), ("audio/n1.mp3", 31.4), ("audio/n2.mp3", 60.0),
    ("audio/n3.mp3", 93.8), ("audio/j1.mp3", 110.3), ("audio/n4.mp3", 127.2),
    ("audio/n5.mp3", 142.8), ("audio/n6.mp3", 180.0), ("audio/j2.mp3", 211.6),
    ("audio/n7.mp3", 216.0), ("audio/n8.mp3", 244.8), ("audio/n9.mp3", 268.6),
    ("audio/n10.mp3", 297.8),
]

BEDS = [(0.0, 108.0, "a"), (127.5, 164.0, "b"), (216.0, 295.0, "a")]


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
    if seg_id == "n9b":
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

    OUT = "john-4_woman-at-the-well.mp4"
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
