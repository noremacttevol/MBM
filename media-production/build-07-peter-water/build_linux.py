#!/usr/bin/env python3
"""Assemble Story Video #7 — Peter Walks on Water (Matthew 14:22-33).
Phase-1 STILLS-ONLY (Law E) + Face Law / #18. Windows rebuild on Elli's laptop
with Cameron's 3 picture fixes (2026-07-11):
  1. WALK (s5) regenerated: Peter seen from BEHIND walking away toward a distant
     Jesus (Peter's face not shown; the Lord far enough to face them unseen).
  2. The sinking beat (n5b) now uses a NEW "Peter sinking ALONE" still (no
     rescuing hand) so the hand-grab no longer appears during the sinking
     narration — the catch still (s7-sink-anchor-v5, only the Lord's hand+sleeve)
     is held back until "And Jesus caught him." (more time in the water first).
  3. S9 walk-back regenerated with the rest of the disciples visible in the boat.
Everything else (durations, captions, narration offsets, music beds) is
unchanged from Machine C's stills-only cut.

Two-Voice Law: narrator Andrew; Jesus Christopher, exact KJV (14:27, 14:29a
"Come.", 14:31b). Music out before j1/j2 and dead from "immediately" through
the peak. Windows: ffmpeg full path, Georgia fonts, UTF-8 captions.
Output: matthew-14_peter-walks-on-water.mp4, 1080x1920, <25MB, 256.0s.
"""
import os
import shutil
import subprocess

# portable ffmpeg: the checked-in bin/ffmpeg on Cameron's box if present, else
# ffmpeg on PATH (2026-07-13: added so this rebuilds on any dev box for the s3
# black-void→moonlit-man fix).
_BIN_FF = "/home/cameron-lovett/MBM/media-production/bin/ffmpeg"
FF = _BIN_FF if os.path.exists(_BIN_FF) else (shutil.which("ffmpeg") or "ffmpeg")
A, S, FPS = "assets", "segs", 30
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
CREAM, INK = "0xF7F2E9", "0x3B2A1E"
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-mountain-prayer-v2.jpeg"
S2 = "s2-boat-storm.jpeg"
S3 = "s3-figure-on-water-v2.jpeg"
S4 = "s4-over-gunwale.jpeg"
WALK = "s5-walk-anchor-v5.jpeg"      # FIX 1: Peter from behind toward distant Jesus
S6 = "s6-eyes-on-waves.jpeg"
SINK_ALONE = "s7-sink-alone.jpeg"    # FIX 2: Peter sinking ALONE, no rescuing hand
CATCH = "s7-sink-anchor-v5.jpeg"     # the CATCH (only the Lord's hand+sleeve) — held to n6+
S9 = "s9-walk-back-v3.jpeg"          # FIX 3: walk-back with disciples in the boat
S10 = "s10-calm-sea.jpeg"
S11 = "s11-worship-v3.jpeg"
S12 = "s12-worship-v2.jpeg"

# (id, kind, src, dur, zoom_dir, caption, style)
SEGMENTS = [
    ("n0a", "still", S1, 13.3, "in",
     "Jesus had just fed more than five thousand\n"
     "people with a few loaves of bread and two\n"
     "small fish. And when it was done, he told\n"
     "his disciples to take the boat and cross\n"
     "the lake ahead of him.", "n"),
    ("n0b", "still", S1, 13.4, "out",
     "He sent the crowds home. And then he\n"
     "climbed a mountain, alone, to pray. That\n"
     "is where the night found him. Not in the\n"
     "boat. On the mountain, talking with\n"
     "his Father.", "n"),
    ("n1a", "still", S2, 12.6, "in",
     "Out on the water, the wind turned against\n"
     "the boat. The waves rose. The disciples —\n"
     "several of them fishermen who had worked\n"
     "this lake their whole lives — rowed\n"
     "against it for hours.", "n"),
    ("n1b", "still", S2, 12.7, "out",
     "Matthew tells us it was the fourth watch\n"
     "of the night when help came. That means\n"
     "between three and six in the morning.\n"
     "They had been fighting that sea\n"
     "nearly all night.", "n"),
    ("n2a", "still", S3, 10.7, "in",
     "And then, through the spray and the dark,\n"
     "they saw something that made grown\n"
     "fishermen scream. A figure. Walking\n"
     "toward them. On top of the water.", "n"),
    ("n2b", "still", S3, 10.8, "out",
     "They cried out that it was a ghost —\n"
     "because nobody walks on the sea.\n"
     "But the voice that came back across\n"
     "the water was one they knew.", "n"),
    ("j1", "still", S3, 5.4, "in",
     "“Be of good cheer; it is I;\nbe not afraid.”", "kjv"),
    ("n3a", "still", S4, 11.4, "in",
     "Take heart. It's me. Don't be afraid.\n"
     "And Peter — impulsive, big-hearted\n"
     "Peter — called back across the storm:\n"
     "Lord, if it's really you, tell me to\n"
     "come to you on the water.", "n"),
    ("n3b", "still", S4, 11.9, "out",
     "Think about what he was asking for.\n"
     "Not for the storm to stop. To come\n"
     "out into it — to where Jesus stood.", "n"),
    ("j2", "still", S4, 4.6, "in",
     "“Come.”", "kjv"),
    ("n4a", "still", S4, 7.0, "out",
     "One word. And Peter put his leg\n"
     "over the side of that pitching boat,\n"
     "and stood up on the sea.", "n"),
    ("n4b", "still", WALK, 12.8, "in",
     "And he was doing it. Step after step\n"
     "on the moving water, his eyes fixed\n"
     "on Jesus. For a moment, an ordinary\n"
     "fisherman walked where only God\n"
     "can walk.", "n"),
    ("n5a", "still", S6, 9.2, "in",
     "Then he noticed the wind tearing at him.\n"
     "He looked down at the waves instead\n"
     "of ahead at Jesus.", "n"),
    ("n5b", "still", SINK_ALONE, 10.8, "out",
     "And the moment his eyes moved, the\n"
     "water stopped holding him. He dropped\n"
     "to his waist, mid-stride, and cried out\n"
     "the shortest prayer in the Bible:\n"
     "Lord, save me.", "n"),
    ("n6", "still", CATCH, 3.6, "in",
     "And Jesus caught him.\nImmediately.", "n"),
    ("n7a", "still", CATCH, 10.0, "out",
     "Matthew uses that exact word. There was\n"
     "no pause. No lesson first. No letting him\n"
     "go under to teach him something.", "n"),
    ("n7b", "still", CATCH, 10.1, "in",
     "The hand was there before the prayer\n"
     "was finished. And from that grip —\n"
     "holding him above the water — Jesus\n"
     "asked him one question.", "n"),
    ("j3", "still", CATCH, 5.0, "in",
     "“O thou of little faith,\nwherefore didst thou doubt?”", "kjv"),
    ("n8a", "still", CATCH, 11.0, "out",
     "Why did you doubt? Hear how he asked it.\n"
     "Not from the shore. Not after pulling him\n"
     "into the boat. From the hand already\n"
     "holding him.", "n"),
    ("n8b", "still", CATCH, 11.2, "in",
     "It isn't a scolding. It's a real question,\n"
     "from someone who had already caught\n"
     "him — as if to say: you were doing it.\n"
     "What made you stop trusting me?", "n"),
    ("n9a", "still", S9, 8.8, "in",
     "The two of them came back to the boat\n"
     "across the water together. And the\n"
     "moment they climbed in, the wind\n"
     "stopped.", "n"),
    ("n9b", "still", S10, 8.3, "out",
     "Not slowly. Not eventually. The sea\n"
     "that had fought them all night simply\n"
     "lay down flat under the stars.", "n"),
    ("n10a", "still", S11, 13.8, "in",
     "And the men in that boat — the same men\n"
     "who minutes earlier had screamed that he\n"
     "was a ghost — knelt down where they sat,\n"
     "soaked and shaking, and worshipped him.", "n"),
    ("n10b", "still", S12, 13.6, "out",
     "You really are the Son of God, they said.\n"
     "The storm had taught them who he was.\n"
     "And notice what the story remembers\n"
     "about Peter. Not that he sank. That he\n"
     "walked. And that when he fell, he\n"
     "was caught.", "n"),
    ("card", "card", None, 14.0, None,
     "Have you ever had something real —\na moment of faith, a sense\n"
     "of something true —\n\nand then watched it slip\n"
     "when the storm got loud?\n\n"
     "He caught him before\nthe prayer was finished.", "close"),
]

AUDIO = [
    ("audio/n0.mp3", 0.4), ("audio/n1.mp3", 26.9), ("audio/n2.mp3", 52.2),
    ("audio/j1.mp3", 73.9), ("audio/n3.mp3", 79.1), ("audio/j2.mp3", 103.8),
    ("audio/n4.mp3", 107.0), ("audio/n5.mp3", 126.8), ("audio/n6.mp3", 146.8),
    ("audio/n7.mp3", 150.4), ("audio/j3.mp3", 170.5), ("audio/n8.mp3", 175.5),
    ("audio/n9.mp3", 197.7), ("audio/n10.mp3", 214.8), ("audio/n11.mp3", 242.9),
]

BEDS = [(0.0, 72.7, "a"), (79.5, 102.6, "b"), (107.5, 149.0, "b"),
        (198.5, 254.5, "b")]


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
            f"box=1:boxcolor=black@0.32:boxborderw=18,"
            f"fade=t=in:st=0:d=0.5:alpha=1,fade=t=out:st={fo}:d=0.5:alpha=1[cap]")


def assemble(seg_id, base, dur, cap, style, tail=""):
    capf = caption_overlay(seg_id, dur, cap, style)
    if capf:
        return f"{base}[base];{capf};[base][cap]overlay=format=auto{tail}[v]"
    return f"{base}{tail}[v]"


def build_still(seg_id, src, dur, zdir, cap, style):
    frames = int(dur * FPS)
    z = f"1.001+0.10*on/{frames}" if zdir == "in" else f"1.101-0.10*on/{frames}"
    base = (f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,"
            f"crop=2160:3840,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},scale=1080:1920:flags=lanczos")
    tail = ""
    if seg_id == "n0a":
        tail = ",fade=t=in:st=0:d=1.2"
    if seg_id == "n10b":
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", assemble(seg_id, base, dur, cap, style, tail),
         "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(seg_id, dur, text):
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w", encoding="utf-8") as f:
        f.write(text)
    vf = (f"drawtext=fontfile='{SERIF}':textfile='{tf}':fontsize=48:"
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
    bi = 0
    for (bs, be, st) in BEDS:
        filters.append(bed_filter(bi, bs, be, st))
        labels.append(f"[mus{bi}]")
        bi += 1
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

    OUT = "matthew-14_peter-walks-on-water.mp4"
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
