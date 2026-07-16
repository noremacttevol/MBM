#!/usr/bin/env python3
"""Assemble Story Video #17 — The Raising of Lazarus (John 11:1-44).
Fresh build under BOTH current standards: Phase-1 STILLS-ONLY (Law E) and the
Face Law / Correction #18 (the Lord staged only from behind / over-the-shoulder
/ at a distance; face never shown; no glow). 9 painted stills, Ken Burns drift,
serif captions, KJV red-letter j1 (11:4), j2 (11:25-26), j3 (11:40), j4 (11:43),
j5 (11:44b). Music map: warm bed opens, then FULL SILENCE for "I am the
resurrection", for "Jesus wept", and for "Lazarus, come forth" + the raising;
a warm bed swells under the meaning, out before the card.

Two-Voice Law: narrator en-US-AndrewNeural; Jesus en-US-ChristopherNeural, exact
KJV only. Windows build: ffmpeg full path, Georgia serif fonts, UTF-8 captions,
supersample increase+crop for the 768x1376 sources.
Output: john-11_lazarus.mp4, 1080x1920 H.264 30fps, <25MB, ~371.7s.
"""
import os
import subprocess

FF = "/home/cameron-lovett/MBM/media-production/bin/ffmpeg"
A, S, FPS = "assets", "segs", 30
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
CREAM, INK = "0xF7F2E9", "0x3B2A1E"
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

# (id, kind, src, dur, zoom_dir, caption, style)
SEGMENTS = [
    ("s1a", "still", "s1.jpeg", 16.4, "in",
     "In Bethany lived two sisters —\nMartha and Mary — and their\nbrother Lazarus.", "n"),
    ("s1b", "still", "s1.jpeg", 16.5, "out",
     "Jesus loved this family.\nAnd now their brother\nwas dying.", "n"),
    ("s2a", "still", "s2.jpeg", 13.2, "in",
     "The sisters sent word:\n“Lord, the one you love\nis sick.”", "n"),
    ("s2b", "still", "s2.jpeg", 10.3, "out",
     "“This sickness is not unto\ndeath, but for the glory\nof God...”", "kjv"),
    ("s2c", "still", "s2.jpeg", 16.5, "in",
     "Yet he stayed where he was\ntwo more days.", "n"),
    ("s3a", "still", "s3.jpeg", 17.1, "in",
     "By the time he came, Lazarus\nhad been in the tomb\nfour days.", "n"),
    ("s3b", "still", "s3.jpeg", 17.5, "out",
     "Four days meant the door\nwas shut. No hope left.", "n"),
    ("s4a", "still", "s4.jpeg", 13.0, "in",
     "Martha ran to meet him:\n“If you had been here, my\nbrother would not have died.”", "n"),
    ("s4b", "still", "s4.jpeg", 12.6, "out",
     "“But even now, I know God\nwill give you whatever\nyou ask.”", "n"),
    ("s5a", "still", "s5.jpeg", 23.6, "in",
     "“Your brother will rise again.”\n“Yes — on the last day,\nI know.”", "n"),
    ("s5b", "still", "s5.jpeg", 17.9, "out",
     "“I am the resurrection, and\nthe life...\nBelievest thou this?”", "kjv"),
    ("s6a", "still", "s6.jpeg", 22.0, "in",
     "Then Mary came, and fell\nat his feet, weeping.", "n"),
    ("s6b", "still", "s6.jpeg", 18.0, "out",
     "And the shortest verse\nin the Bible:", "n"),
    ("s6c", "still", "s6.jpeg", 18.8, "in",
     "Jesus wept.\nHe did not skip the grief.\nHe entered it with them.", "n"),
    ("s7a", "still", "s7.jpeg", 19.1, "in",
     "“Take away the stone.”\n“Lord — it has been\nfour days.”", "n"),
    ("s7b", "still", "s7.jpeg", 9.4, "out",
     "“Said I not unto thee...\nthou shouldest see the\nglory of God?”", "kjv"),
    ("s7c", "still", "s7.jpeg", 9.4, "in",
     "So they rolled the great\nstone back, and the grave\nstood open.", "n"),
    ("s8a", "still", "s8.jpeg", 18.3, "in",
     "He prayed aloud, then\ncalled into the dark —", "n"),
    ("s8b", "still", "s8.jpeg", 4.3, "out",
     "“Lazarus, come forth.”", "kjv"),
    ("s8c", "still", "s8.jpeg", 20.1, "in",
     "And the dead man came out,\nbound hand and foot.\nNobody breathed.", "n"),
    ("s9a", "still", "s9.jpeg", 4.3, "in",
     "“Loose him, and let him go.”", "kjv"),
    ("s9b", "still", "s9.jpeg", 18.3, "out",
     "The last great sign before\nhis own cross — done in the\nopen, at a marked grave.", "n"),
    ("s9c", "still", "s9.jpeg", 19.3, "in",
     "He does not merely explain\nthe resurrection.\nHe is the resurrection.", "n"),
    ("card", "card", None, 15.8, None,
     "He wept at the grave —\neven though he was about\nto open it.\n\n"
     "What grief would he sit\ninside with you, before\nhe ever fixed it?", "close"),
]

AUDIO = [
    ("audio/n0.mp3", 0.5), ("audio/n1.mp3", 32.9), ("audio/j1.mp3", 46.1),
    ("audio/n1b.mp3", 56.4), ("audio/n2.mp3", 72.9), ("audio/n3.mp3", 107.5),
    ("audio/n4.mp3", 133.1), ("audio/j2.mp3", 156.7), ("audio/n5.mp3", 174.6),
    ("audio/n6.mp3", 196.6), ("audio/n7.mp3", 233.4), ("audio/j3.mp3", 252.5),
    ("audio/n7b.mp3", 261.9), ("audio/n8.mp3", 271.3), ("audio/j4.mp3", 289.6),
    ("audio/n9.mp3", 293.9), ("audio/j5.mp3", 314.0), ("audio/n10.mp3", 318.3),
    ("audio/n11.mp3", 355.9),
]

# warm bed opens; SILENCE for "I am the resurrection" (156-174); quiet bed under
# Mary/setup, out before "Jesus wept" (~214); low bed under the tomb tension,
# out before "Lazarus, come forth" (289.6); the command + the raising in silence;
# a warm bed swells under the meaning (n10), out before the card is read.
BEDS = [(0.0, 155.0, "a"), (175.0, 211.0, "b"), (234.0, 288.0, "b"),
        (296.0, 353.0, "a")]


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
    if seg_id == "s9c":
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
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
               "+0*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))+0*sin(2*PI*220*t)'")
        eq = "lowpass=f=760,tremolo=f=0.12:d=0.3,aecho=0.7:0.4:311|429:0.24|0.17"
        fin, fout = 6, 6
    else:
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
               "+0*(sin(2*PI*146.83*t)+sin(2*PI*147.5*t))+0*sin(2*PI*196*t)'")
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

    OUT = "john-11_lazarus.mp4"
    vcap = max(300, int(24.5 * 8000 / total) - 145)
    size, crf = 0.0, 21
    for crf in (21, 22, 23, 24, 25, 26):
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
