#!/usr/bin/env python3
"""Assemble Story Video #18 — The Road to Emmaus (Luke 24:13-35).
Phase-1 STILLS-ONLY (Law E) + Face Law (#18). 8 painted stills; the risen Lord
is staged only from behind / over-the-shoulder / by his hands (the two never
recognize him until the breaking of bread, then he vanishes). KJV red-letter
j1 (Luke 24:25-26). Music goes fully silent for the recognition + vanishing.
Windows build: ffmpeg full path, Georgia serif fonts, UTF-8 captions.
Output: luke-24_emmaus.mp4, 1080x1920 H.264 30fps, <25MB, ~258s.
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

# (id, kind, src, dur, zoom_dir, caption, style)
SEGMENTS = [
    ("s1a", "still", "s1.jpeg", 12.3, "in",
     "It was the same Sunday. The tomb\nwas empty — and two of his\nfollowers had given up.", "n"),
    ("s1b", "still", "s1.jpeg", 12.4, "out",
     "They walked the seven miles to\nEmmaus, going over the arrest, the\ncross, the end of all their hope.", "n"),
    ("s2", "still", "s2.jpeg", 22.1, "in",
     "A stranger fell into step beside them.\nBut their eyes were held — it was\nJesus, and they had no idea.", "n"),
    ("s3a", "still", "s3.jpeg", 21.0, "in",
     "He asked why they were so heavy.\n“Are you the only one who doesn't\nknow what has happened?”", "n"),
    ("s3b", "still", "s3.jpeg", 21.1, "out",
     "“Jesus of Nazareth — we had hoped\nhe was the one to rescue Israel.\nNow the tomb is empty...”", "n"),
    ("s4a", "still", "s4.jpeg", 5.2, "in",
     "The stranger listened to all of it.\nThen he answered them:", "n"),
    ("s4b", "still", "s4.jpeg", 12.6, "out",
     "“O fools, and slow of heart to\nbelieve all that the prophets\nhave spoken...”", "kjv"),
    ("s4c", "still", "s4.jpeg", 23.2, "in",
     "Starting with Moses, he opened the\nscriptures — the cross was not the\ncollapse of the plan. It was the plan.", "n"),
    ("s5", "still", "s5.jpeg", 18.9, "in",
     "At Emmaus he made as if to go on.\n“Stay with us — it's nearly evening.”\nSo he went in.", "n"),
    ("s6a", "still", "s6.jpeg", 13.0, "in",
     "At the table, the guest did what only\nthe host should do. He took the bread,\nblessed it, and broke it.", "n"),
    ("s6b", "still", "s6.jpeg", 10.2, "out",
     "And their eyes were opened,\nand they knew him. It was Jesus.", "n"),
    ("s7a", "still", "s7.jpeg", 11.1, "in",
     "And in that instant — he was gone.\nVanished from the table.", "n"),
    ("s7b", "still", "s7.jpeg", 17.9, "out",
     "“Weren't our hearts burning within us,\nwhile he opened the scriptures\nto us on the road?”", "n"),
    ("s8a", "still", "s8.jpeg", 18.0, "in",
     "That same hour they ran the seven\ndark miles back to Jerusalem:\nthe Lord is risen. We have seen him.", "n"),
    ("s8b", "still", "s8.jpeg", 26.1, "out",
     "The risen Jesus spent that first\nafternoon walking with two people who\nhad quit — until they could see.", "n"),
    ("card", "card", None, 12.9, None,
     "He walked a long way with them\nbefore they knew who he was.\n\n"
     "Could he be walking with you —\nin a season you thought you\nwere walking alone?", "close"),
]

AUDIO = [
    ("audio/n0.mp3", 0.6), ("audio/n1.mp3", 24.7), ("audio/n2.mp3", 46.8),
    ("audio/n3.mp3", 63.8), ("audio/n4a.mp3", 88.9), ("audio/j1.mp3", 94.1),
    ("audio/n4b.mp3", 106.7), ("audio/n5.mp3", 129.9), ("audio/n6.mp3", 148.8),
    ("audio/n7.mp3", 161.8), ("audio/n8.mp3", 183.1), ("audio/n9.mp3", 201.0),
    ("audio/n10.mp3", 219.0), ("audio/n11.mp3", 245.1),
]

# warm bed under the road/grief, out before "the stranger answered" + j1; a
# quiet bed under the teaching + table setup; FULL SILENCE for the recognition
# and the vanishing (161.8-183); a warm bed swells under hearts-burning / the
# run back / the meaning, out before the closing card.
BEDS = [(0.0, 92.5, "a"), (107.0, 160.5, "b"), (184.0, 243.5, "a")]


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
    if seg_id == "s1a":
        tail = ",fade=t=in:st=0:d=1.2"
    if seg_id == "s8b":
        tail = f",fade=t=out:st={dur-1.0}:d=1.0"
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", assemble(seg_id, base, dur, cap, style, tail),
         "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(seg_id, dur, text):
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w", encoding="utf-8") as f:
        f.write(text)
    vf = (f"drawtext=fontfile='{SERIF}':textfile='{tf}':fontsize=48:"
          f"fontcolor={INK}:line_spacing=20:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run([FF, "-y", "-f", "lavfi", "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/{seg_id}.mp4"])


def bed_filter(idx, start, end, style):
    dur = end - start
    if style == "a":
        src = ("aevalsrc='0.020*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
               "+0.015*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))+0.010*sin(2*PI*220*t)'")
        eq = "lowpass=f=760,tremolo=f=0.12:d=0.3,aecho=0.7:0.4:311|429:0.24|0.17"
        fin, fout = 6, 6
    else:
        src = ("aevalsrc='0.014*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
               "+0.011*(sin(2*PI*146.83*t)+sin(2*PI*147.5*t))+0.009*sin(2*PI*196*t)'")
        eq = "lowpass=f=720,tremolo=f=0.10:d=0.3,aecho=0.7:0.4:317|443:0.24|0.17"
        fin, fout = 5, 7
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

    OUT = "luke-24_emmaus.mp4"
    vcap = max(300, int(24.5 * 8000 / total) - 145)
    size, crf = 0.0, 21
    for crf in (21, 22, 23, 24, 25):
        run([FF, "-y", "-i", f"{S}/video_silent.mp4", "-i", f"{S}/audio_mix.m4a",
             "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "medium",
             "-crf", str(crf), "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p", "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", OUT])
        size = os.path.getsize(OUT) / 1e6
        if size <= 24.5:
            break
    print(f"DONE: {OUT}  {size:.1f} MB, {total:.1f}s (crf {crf})", flush=True)


if __name__ == "__main__":
    main()
