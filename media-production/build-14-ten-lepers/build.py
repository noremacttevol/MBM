#!/usr/bin/env python3
"""Assemble Story Video #14 — The Ten Lepers (Luke 17:11-19).

Full law stack per PRODUCTION-BIBLE.md + PREFLIGHT.md. Hybrid storybook:
12 painted stills (Correction #18 — Jesus's face never shown; the 5 Jesus
stills are staged from behind / over-the-shoulder) with Ken Burns drift,
+ 2 Veo money-moment clips (the healing mid-stride, 8s; the joyful return
run, 8s), each played STILL-first per Correction #10. edge-tts narration
(ear-checked), serif captions, KJV red-letter j1 (Luke 17:14), j2
(17:17-18), j3 (17:19) — exact against qc/luke17-kjv.txt. Closing question
card on cream #F7F2E9, read aloud (Readable-Card Law).

Assembly Craft Laws: supersampled zoompan (anti-shimmer), RGBA caption
fades, crf-16 intermediates, veryslow crf step-up final, loudness toward
-15 LUFS, detuned-pair beds.

THE SOUND LAW OF THIS VIDEO: a warm bed opens and FADES TO FULL SILENCE
before "and as they went" — the healing (n6) lands in sacred quiet, the
peak. A warm bed returns after and is fully out before the closing card,
which is read in silence.

Windows build (Elli's laptop): ffmpeg via full path, Georgia serif fonts.
Output: luke-17_ten-lepers.mp4 (SCRIPTURE-NAME LAW), 1080x1920 H.264 30fps.
"""
import os
import subprocess

FF = ("C:/Users/ellil/AppData/Local/Microsoft/WinGet/Packages/"
      "Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/"
      "ffmpeg-8.1.2-full_build/bin/ffmpeg.exe")
FFPROBE = FF.replace("ffmpeg.exe", "ffprobe.exe")

A = "assets"
S = "segs"
FPS = 30
# Windows fonts; the drive-letter colon must be escaped inside a filter.
SERIF = "C\\:/Windows/Fonts/georgia.ttf"
SERIF_BI = "C\\:/Windows/Fonts/georgiai.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

# (id, kind, source, stretch, duration_s, zoom_dir, caption, style)
SEGMENTS = [
    ("n0", "still", "s1.jpeg", None, 15.9, "in",
     "On the road to Jerusalem —\nthe borderland of\nSamaria and Galilee.", "n"),
    ("n1", "still", "s2.jpeg", None, 27.9, "out",
     "Ten men with leprosy,\nkept afar off by the Law.\nUntouched for years.", "n"),
    ("n2", "still", "s3.jpeg", None, 12.4, "in",
     "“Jesus, Master,\nhave mercy on us.”", "n"),
    ("n3", "still", "s4.jpeg", None, 12.1, "in",
     "He saw them, and gave\nnot a touch, but a word:", "n"),
    ("j1", "still", "s4.jpeg", None, 4.9, "out",
     "“Go shew yourselves\nunto the priests.”", "kjv"),
    ("n4", "still", "s5.jpeg", None, 23.8, "in",
     "The priest alone could\ncertify them clean.\nA promise, in disguise.", "n"),
    ("n5", "still", "s5.jpeg", None, 18.3, "out",
     "No healing yet.\nAnd they went anyway.", "n"),
    ("n6a", "still", "s6.jpeg", None, 3.2, "in",
     "And as they went —", "n"),
    ("n6b", "clip", "s6-heal-clip.mp4", None, 8.0, None,
     "— they were made clean.", "n"),
    ("n7", "still", "s7.jpeg", None, 17.6, "in",
     "Nine ran on.\nOne saw, and turned back.", "n"),
    ("n8a", "still", "s8.jpeg", None, 3.2, "in",
     "He came back —", "n"),
    ("n8b", "clip", "s8-run-clip.mp4", None, 8.0, None,
     "running, praising God aloud.", "n"),
    ("n9", "still", "s9.jpeg", None, 19.1, "in",
     "He fell at his feet.\nAnd he was a Samaritan —\nthe outsider.", "n"),
    ("n10", "still", "s10.jpeg", None, 6.8, "in",
     "He looked at the empty\nroad, and asked:", "n"),
    ("j2", "still", "s10.jpeg", None, 13.2, "out",
     "“Were there not ten cleansed?\nbut where are the nine?”", "kjv"),
    ("n11", "still", "s9.jpeg", None, 24.5, "in",
     "‘Save this stranger.’\nOnly the outsider\ncame back to the giver.", "n"),
    ("n12", "still", "s11.jpeg", None, 9.1, "in",
     "Then he lifted the man\nwith a word:", "n"),
    ("j3", "still", "s11.jpeg", None, 6.7, "out",
     "“Arise, go thy way: thy\nfaith hath made thee whole.”", "kjv"),
    ("n13", "still", "s12.jpeg", None, 18.1, "in",
     "All ten were cleansed.\nOnly one was made whole.", "n"),
    ("n14", "still", "s12.jpeg", None, 7.9, "out",
     "He walked home\na whole man.", "n"),
    ("card", "card", None, None, 13.3, None,
     "The healing happened while\nthey walked, before they\ncould see it.\n\n"
     "Have you ever had to move\nforward on nothing but a\nword — before there\n"
     "was any proof?", "close"),
]

# narration mp3 placed at absolute start seconds (continuous track).
AUDIO = [
    ("audio/n0.mp3", 0.6),
    ("audio/n1.mp3", 16.2),
    ("audio/n2.mp3", 44.1),
    ("audio/n3.mp3", 56.5),
    ("audio/j1.mp3", 69.3),
    ("audio/n4.mp3", 73.5),
    ("audio/n5.mp3", 97.3),
    ("audio/n6.mp3", 115.6),
    ("audio/n7.mp3", 126.8),
    ("audio/n8.mp3", 144.4),
    ("audio/n9.mp3", 155.6),
    ("audio/n10.mp3", 174.7),
    ("audio/j2.mp3", 182.2),
    ("audio/n11.mp3", 194.7),
    ("audio/n12.mp3", 219.2),
    ("audio/j3.mp3", 229.0),
    ("audio/n13.mp3", 235.0),
    ("audio/n14.mp3", 253.1),
    ("audio/n15.mp3", 261.0),
]

# Warm detuned-pair beds. Out before the healing (peak silence), back
# after, fully out before the card. (start_s, end_s, style)
BEDS = [
    (0.0, 113.5, "b"),      # journey/instruction; out before "as they went"
    (155.0, 258.0, "a"),    # the return + question; out before the card
]


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:150], flush=True)
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
    fade_out = max(0.0, dur - 0.6)
    return (f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile='{font}':textfile='{tf}':fontsize={size}:"
            f"fontcolor={color}:line_spacing=14:x=(w-text_w)/2:"
            f"y=min(h-460\\,h-160-text_h):"
            f"shadowcolor=black@0.85:shadowx=2:shadowy=2:"
            f"box=1:boxcolor=black@0.34:boxborderw=18,"
            f"fade=t=in:st=0:d=0.5:alpha=1,"
            f"fade=t=out:st={fade_out}:d=0.5:alpha=1[cap]")


def assemble_segment(seg_id, base_chain, dur, cap, style, tail=""):
    capf = caption_overlay(seg_id, dur, cap, style)
    if capf:
        return (f"{base_chain}[base];{capf};"
                f"[base][cap]overlay=format=auto{tail}[v]")
    return f"{base_chain}{tail}[v]"


def build_still(seg_id, src, dur, zdir, cap, style):
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.09*on/{frames}"
    else:
        z = f"1.091-0.09*on/{frames}"
    # Anti-shimmer: supersample -> zoompan at 2160x3840 -> lanczos to 1080.
    base = (f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,"
            f"crop=2160:3840,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ""
    if seg_id == "n0":
        tail = ",fade=t=in:st=0:d=1.2"
    if seg_id == "n14":
        tail = f",fade=t=out:st={dur-1.0}:d=1.0"
    fc = assemble_segment(seg_id, base, dur, cap, style, tail)
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_clip(seg_id, src, dur, cap, style):
    base = (f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,"
            f"crop=1080:1920,setsar=1,fps={FPS},"
            f"unsharp=5:5:0.30:5:5:0.0")
    fc = assemble_segment(seg_id, base, dur, cap, style, "")
    run([FF, "-y", "-i", f"{A}/{src}", "-filter_complex", fc,
         "-map", "[v]", "-t", str(dur)] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(seg_id, dur, text):
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w", encoding="utf-8") as f:
        f.write(text)
    vf = (f"drawtext=fontfile='{SERIF}':textfile='{tf}':fontsize=48:"
          f"fontcolor={INK}:line_spacing=20:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/{seg_id}.mp4"])


def bed_filter(idx, start, end, style):
    dur = end - start
    if style == "a":
        src = ("aevalsrc='0.020*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
               "+0.015*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))"
               "+0.010*sin(2*PI*220*t)+0.007*sin(2*PI*329.63*t)'")
        eq = "lowpass=f=760,tremolo=f=0.12:d=0.3,aecho=0.7:0.4:311|429:0.24|0.17"
        fin, fout = 6, 6
    else:
        src = ("aevalsrc='0.014*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
               "+0.011*(sin(2*PI*146.83*t)+sin(2*PI*147.5*t))"
               "+0.009*sin(2*PI*196*t)+0.006*sin(2*PI*220*t)'")
        eq = "lowpass=f=720,tremolo=f=0.10:d=0.3,aecho=0.7:0.4:317|443:0.24|0.17"
        fin, fout = 5, 7
    if dur < fin + fout + 2:
        fin = fout = max(2, int((dur - 2) / 2))
    ms = int(start * 1000)
    delay = f",adelay={ms}|{ms}" if ms else ""
    return (f"{src}:s=44100:d={dur},{eq},"
            f"afade=t=in:st=0:d={fin},afade=t=out:st={dur-fout}:d={fout}"
            f"{delay}[mus{idx}]")


def main():
    os.makedirs(S, exist_ok=True)
    total = sum(s[4] for s in SEGMENTS)
    print(f"total runtime: {total:.1f}s", flush=True)

    for seg_id, kind, src, stretch, dur, zdir, cap, style in SEGMENTS:
        if kind == "still":
            build_still(seg_id, src, dur, zdir, cap, style)
        elif kind == "clip":
            build_clip(seg_id, src, dur, cap, style)
        else:
            build_card(seg_id, dur, cap)

    with open(f"{S}/concat.txt", "w", encoding="utf-8") as f:
        for seg in SEGMENTS:
            f.write(f"file '{seg[0]}.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at absolute offsets + warm beds ----
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
    filters.append("".join(labels) +
                   f"amix=inputs={n}:duration=longest:normalize=0,"
                   f"apad=whole_dur={total}[aout]")
    run([FF, "-y"] + inputs + ["-filter_complex", ";".join(filters),
        "-map", "[aout]", "-t", str(total), "-c:a", "aac", "-b:a", "160k",
        f"{S}/audio_mix.m4a"])

    # ---- loudness law: measure EBU R128, lift toward -15 LUFS ----
    probe = subprocess.run(
        [FF, "-i", f"{S}/audio_mix.m4a", "-af", "ebur128", "-f", "null", "-"],
        capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            try:
                lufs = float(line.split()[1])
            except ValueError:
                pass
    gain = 0.0 if lufs is None else max(-6.0, min(12.0, -15.0 - lufs))
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    # ---- final mux: veryslow, runtime-computed rate cap, crf step-up ----
    OUT = "luke-17_ten-lepers.mp4"   # SCRIPTURE-NAME LAW
    vcap = max(300, int(24.5 * 8000 / total) - 145)
    size, crf = 0.0, 21
    for crf in (21, 22, 23, 24, 25):
        run([FF, "-y", "-i", f"{S}/video_silent.mp4",
             "-i", f"{S}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "veryslow", "-crf", str(crf),
             "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", OUT])
        size = os.path.getsize(OUT) / 1e6
        if size <= 24.5:
            break
        print(f"  {size:.1f} MB at crf {crf} — over, stepping up", flush=True)
    print(f"DONE: {OUT}  {size:.1f} MB, {total:.1f}s (crf {crf}, vcap {vcap}k)",
          flush=True)


if __name__ == "__main__":
    main()
