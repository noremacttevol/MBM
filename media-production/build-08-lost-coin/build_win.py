#!/usr/bin/env python3
"""Assemble Story Video #8 — The Lost Coin (Luke 15:8-10). Phase-1 STILLS-ONLY.
Parable: no Jesus figure (his voice only). 6 painted stills, Ken Burns drift,
serif captions, KJV red-letter j1 (15:9) + j2 (15:10), closing card.
Windows build (Elli's laptop): ffmpeg full path, Georgia fonts, UTF-8 captions.
Output: luke-15_lost-coin.mp4, 1080x1920 H.264 30fps, ~66s.
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
    ("count-a", "still", "count.jpeg", 9.7, "in",
     "When Jesus wanted to show how\nGod feels about one lost soul,\nhe told this story.", "n"),
    ("count-b", "still", "count.jpeg", 4.0, "out",
     "A woman has ten coins.\nShe loses one.", "n"),
    ("lamp", "still", "lamp.jpeg", 4.0, "in",
     "She lights a lamp.\nShe sweeps the whole house.", "n"),
    ("sweep", "still", "sweep.jpeg", 3.3, "in",
     "She searches carefully —\nnot casually, carefully —", "n"),
    ("found1", "still", "found.jpeg", 3.4, "in",
     "— until she finds it.", "n"),
    ("door-a", "still", "door.jpeg", 4.2, "in",
     "Then she calls her neighbors\nand friends to celebrate.", "n"),
    ("door-b", "still", "door.jpeg", 6.2, "out",
     "“Rejoice with me; for I have found\nthe piece which I had lost.”", "kjv"),
    ("found2", "still", "found.jpeg", 7.3, "out",
     "One coin. Out of ten.\nThe joy is out of all proportion\nto the value of the coin.", "n"),
    ("stars-a", "still", "stars.jpeg", 10.4, "in",
     "“Likewise... there is joy in the\npresence of the angels of God\nover one sinner that repenteth.”", "kjv"),
    ("stars-b", "still", "stars.jpeg", 3.5, "out",
     "Over one.\nNot a crowd. One.", "n"),
    ("card", "card", None, 10.0, None,
     "Heaven throws a party\nover one soul found.\n\n"
     "Not a crowd. You —\nthe one he lights\nthe lamp for.", "close"),
]

AUDIO = [
    ("audio/n0.mp3", 0.5), ("audio/n1.mp3", 9.7), ("audio/n2a.mp3", 13.7),
    ("audio/n2b.mp3", 17.7), ("audio/n3.mp3", 24.4), ("audio/j1.mp3", 28.6),
    ("audio/n4.mp3", 34.8), ("audio/j2.mp3", 42.1), ("audio/n5.mp3", 52.5),
]

BEDS = [(0.0, 27.5, "a"), (34.6, 41.6, "b"), (52.0, 63.5, "a")]


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
    if seg_id == "count-a":
        tail = ",fade=t=in:st=0:d=1.0"
    if seg_id == "stars-b":
        tail = f",fade=t=out:st={dur-0.8}:d=0.8"
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
        src = ("aevalsrc='0*(sin(2*PI*220*t)+sin(2*PI*220.6*t))"
               "+0*(sin(2*PI*329.63*t)+sin(2*PI*330.5*t))+0*sin(2*PI*440*t)'")
        eq = "lowpass=f=900,tremolo=f=0.14:d=0.3,aecho=0.7:0.4:277|389:0.22|0.15"
        fin, fout = 3, 4
    else:
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*196*t)+sin(2*PI*196.5*t))"
               "+0*(sin(2*PI*261.63*t)+sin(2*PI*262.3*t))'")
        eq = "lowpass=f=820,tremolo=f=0.11:d=0.3,aecho=0.7:0.4:281|401:0.22|0.15"
        fin, fout = 2, 3
    if dur < fin + fout + 1:
        fin = fout = max(1, int((dur - 1) / 2))
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

    OUT = "luke-15_lost-coin.mp4"
    vcap = max(300, int(24.5 * 8000 / total) - 145)
    size, crf = 0.0, 20
    for crf in (20, 21, 22, 23):
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
