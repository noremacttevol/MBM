#!/usr/bin/env python3
"""Assemble Story Video #11 — Calming the Storm (Mark 4:35-41).

Full law stack per PRODUCTION-BIBLE.md + PREFLIGHT.md. Hybrid storybook:
9 painted 2K stills with Ken Burns drift + 2 Veo money-moment clips (the
storm tossing the boat, 8s stretched to 12.8s; the sea falling flat at
"Peace, be still", 8s stretched to 12.8s), edge-tts narration
(ear-checked 14/14), serif captions, KJV red-letter j0 (Mark 4:35), j1
(Mark 4:39), j2 (Mark 4:40) — all exact against qc/mark4-kjv.txt.
Closing question card on cream #F7F2E9, read aloud (Readable-Card Law).

Assembly Craft Laws: supersampled zoompan (anti-shimmer), RGBA caption
fades, crf-16 intermediates, veryslow crf step-up final, loudness toward
-15 LUFS, detuned-pair beds.

THE SOUND LAW OF THIS VIDEO (pack law): an evening bed opens, fades out
before the storm; brown-noise storm ambience builds under s3-s6 and ALL
SOUND CUTS TO SILENCE exactly at j1's last spoken word (139.41s). The
great calm (clip tail + s7) plays in TRUE silence under n6. A warm bed
returns at n7 and is fully out before the closing card, which is read
in silence.

All offsets computed from MEASURED mp3 durations + measured trailing
silence (spoken end = start + last_silence_start); breaths 0.8-1.6s,
1.5s held quiet before j1 and j2.

Output: mark-4_calming-the-storm.mp4 (SCRIPTURE-NAME LAW),
1080x1920 H.264 30fps, <25MB, 264.0s.
"""
import os
import subprocess
FF = r"C:/Users/ellil/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1.2-full_build/bin/ffmpeg.exe"

A = "assets"
S = "segs"
FPS = 30
SERIF = "C\:/Windows/Fonts/georgia.ttf"
SERIF_BI = "C\:/Windows/Fonts/georgiai.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-evening-shore.jpeg"
S2 = "s2-little-ships.jpeg"
S3 = "s3-the-storm.jpeg"
S4 = "s4-asleep-in-stern.jpeg"
S5 = "s5-carest-thou-not.jpeg"
S6 = "s6-peace-be-still.jpeg"
S7 = "s7-great-calm.jpeg"
S8 = "s8-why-fearful-ots.jpeg"
S9 = "s9-what-manner-of-man.jpeg"
CLIP_STORM = "s3-storm-clip.mp4"
CLIP_CALM = "s6-calm-clip.mp4"

# (id, kind, source, stretch_or_none, duration_s, zoom_dir, caption, style)
# Boundaries: 0, 11.0, 20.2, 24.0, 37.6, 51.2, 63.0, 75.8, 84.6, 93.2,
# 101.8, 112.1, 122.4, 129.5, 136.6, 140.2, 153.0, 166.6, 175.9, 183.0,
# 195.6, 208.2, 226.1, 244.0, 264.0.
SEGMENTS = [
    # n0 — evening shore (s1). Worn through from teaching all day.
    ("n0a", "still", S1, None, 11.0, "in",
     "Evening, on the Sea of Galilee. Jesus\n"
     "had been teaching crowds on the shore\n"
     "all day — story after story, until the\n"
     "light was going and his voice was\n"
     "nearly gone with it.", "n"),
    ("n0b", "still", S1, None, 9.2, "out",
     "He was worn through. And when the last\n"
     "story was told, he said to his friends:", "n"),
    # J0 — exact KJV Mark 4:35.
    ("j0", "still", S1, None, 3.8, "in",
     "\u201cLet us pass over unto\nthe other side.\u201d", "kjv"),
    # n1 — even as he was; other little ships (s2). v36 gems.
    ("n1a", "still", S2, None, 13.6, "in",
     "So they took him, Mark says, even as he\n"
     "was — no rest, no supper, straight from\n"
     "the last word into the boat. Other\n"
     "little boats followed them out.", "n"),
    ("n1b", "still", S2, None, 13.6, "out",
     "And here is something worth knowing\n"
     "about the men at the oars: at least four\n"
     "of them were professional fishermen.\n"
     "This lake was their workplace. They had\n"
     "crossed it at night their whole lives.\n"
     "Nothing about dark water scared them.", "n"),
    # n2 — THE STORM (s3 STILL first per Correction #10, THEN the clip).
    ("n2a", "still", S3, None, 11.8, "in",
     "Then the lake turned on them. The Sea\n"
     "of Galilee lies seven hundred feet\n"
     "below sea level, in a bowl of hills —\n"
     "when cold wind spills down those\n"
     "slopes, calm water can turn violent\n"
     "in minutes.", "n"),
    ("n2b", "still", S3, None, 12.8, "out",
     "This storm was savage even by that\n"
     "lake's standard. Waves broke over the\n"
     "side faster than the men could bail.\n"
     "The boat was filling.", "n"),
    ("n2c", "still", S3, None, 8.8, "out",
     "And the fishermen who had survived a\n"
     "hundred storms looked at this one — and\n"
     "believed it was going to be their last.", "n"),
    # n3 — asleep on the cushion (s4). v38a.
    ("n3a", "still", S4, None, 8.6, "in",
     "And Jesus was asleep. In the stern, on\n"
     "the steersman's cushion, soaked with\n"
     "spray, rising and falling with the\n"
     "pitching deck — asleep.", "n"),
    ("n3b", "still", S4, None, 8.6, "out",
     "Not because he didn't know what was\n"
     "happening. Because he wasn't afraid\n"
     "of it.", "n"),
    # n4 — don't you care? (s5). They doubted his heart, not his power.
    ("n4a", "still", S5, None, 10.3, "in",
     "So they woke him. Rough hands on his\n"
     "shoulder, screaming over the wind the\n"
     "question people have been asking in\n"
     "storms ever since: Teacher — don't you\n"
     "care that we are going down?", "n"),
    ("n4b", "still", S5, None, 10.3, "out",
     "Listen to what they were really saying.\n"
     "They never doubted his power. They\n"
     "doubted his heart.", "n"),
    # n5 — he stood up (s6 still). The ambience dies at j1's last word.
    ("n5a", "still", S6, None, 7.1, "in",
     "He got up. He stood in the stern of a\n"
     "sinking boat, in the middle of the worst\n"
     "storm those fishermen had ever seen.", "n"),
    ("n5b", "still", S6, None, 7.1, "out",
     "And he did not speak to the men.\n"
     "He spoke to the storm.", "n"),
    # J1 — exact KJV Mark 4:39, on the held still; ALL sound cuts to
    # silence at the last word (139.41s).
    ("j1", "still", S6, None, 3.6, "in",
     "\u201cPeace, be still.\u201d", "kjv"),
    # n6 — the calm clip pays off the still (Correction #10), in TRUE
    # silence; n6 narration begins over it.
    ("n6a", "still", S7, None, 12.8, "in",
     "And the wind quit. The sea fell flat —\n"
     "glass flat — with stars where the storm\n"
     "had been,", "n"),
    ("n6b", "still", S7, None, 13.6, "in",
     "and the only sound left was water\n"
     "dripping off the ropes. Sailors will\n"
     "tell you the waves keep rolling for\n"
     "hours after a wind dies. These didn't.\n"
     "The lake did not calm down. It obeyed.", "n"),
    # n7 — he turned to them (s8, textbook over-the-shoulder, law #11).
    ("n7", "still", S8, None, 9.3, "in",
     "Then he turned to his friends — soaked,\n"
     "shaking, still gripping the ropes — and\n"
     "he asked them, gently:", "n"),
    # J2 — exact KJV Mark 4:40.
    ("j2", "still", S8, None, 7.1, "out",
     "\u201cWhy are ye so fearful? how is it\n"
     "that ye have no faith?\u201d", "kjv"),
    # n8 — translation bridge (Translation Law: modern meaning only).
    ("n8a", "still", S8, None, 12.6, "in",
     "Hear where he asked that from. Standing\n"
     "in their boat, on the sea he had just\n"
     "flattened to save them. He didn't ask\n"
     "it from the shore. He came through the\n"
     "storm with them —", "n"),
    ("n8b", "still", S8, None, 12.6, "out",
     "and then he asked why the fear had\n"
     "gotten so much bigger than their trust.\n"
     "He never said the storm wasn't real. He\n"
     "never scolded them for waking him. He\n"
     "was simply bigger than it.", "n"),
    # n9 — what manner of man (s9). v41 + the psalm gem.
    ("n9a", "still", S9, None, 17.9, "in",
     "And then a strange thing happened: the\n"
     "fear didn't leave the boat — it changed\n"
     "direction. Mark says they feared\n"
     "exceedingly — more awe after the calm\n"
     "than in the storm — and they asked each\n"
     "other: what kind of man is this, that\n"
     "even the wind and the sea do what he\n"
     "says?", "n"),
    ("n9b", "still", S9, None, 17.9, "out",
     "These men knew their scriptures. They\n"
     "knew the old psalm that says it is God\n"
     "who stills the storm to a whisper. And\n"
     "now they were staring at a man in\n"
     "dripping clothes who had just done it.", "n"),
    # Card — pack card verbatim, held 20.0s AND read aloud, in silence.
    ("card", "card", None, None, 20.0, None,
     "Don't you care that we are drowning?\n"
     "Have you ever asked that question —\n"
     "or wanted to?\n\n"
     "He never denied the storm was real.\n\n"
     "So here is the question this story\n"
     "leaves behind: is God the author of\n"
     "your storm — or the one standing up\n"
     "in your boat?",
     "close"),
]

# narration placements: (audio file, absolute start seconds)
# measured dur/last_silence_start: n0 19.128/18.69  j0 4.272/3.06
#   n1 26.544/26.14  n2 32.664/32.20  n3 16.536/16.07  n4 19.944/19.51
#   n5 13.344/12.89  j1 3.384/2.11  n6 22.752/22.30  n7 8.808/8.38
#   j2 6.648/5.41  n8 24.720/24.26  n9 34.704/34.26  n10 18.048/17.59
# breaths 0.8-1.6s between SPOKEN ends; 1.5s held quiet before j1 and j2.
AUDIO = [
    ("audio/n0.mp3", 0.6),     # s1 0-20.2       evening (sp end 19.29)
    ("audio/j0.mp3", 20.3),    # s1 20.2-24.0    KJV Mark 4:35 (sp 23.36)
    ("audio/n1.mp3", 24.4),    # s2 24.0-51.2    even as he was (sp 50.54)
    ("audio/n2.mp3", 51.6),    # s3+clip 51.2-84.6  THE STORM (sp 83.80)
    ("audio/n3.mp3", 85.0),    # s4 84.6-101.8   asleep (sp 101.07)
    ("audio/n4.mp3", 102.2),   # s5 101.8-122.4  don't you care (sp 121.71)
    ("audio/n5.mp3", 122.9),   # s6 122.4-136.6  he stood up (sp 135.79)
    ("audio/j1.mp3", 137.3),   # s6 136.6-140.2  KJV Mark 4:39 (sp 139.41)
    ("audio/n6.mp3", 143.5),   # clip+s7 140.2-166.6  the calm (sp 165.80)
    ("audio/n7.mp3", 167.0),   # s8 166.6-175.9  he turned (sp 175.38)
    ("audio/j2.mp3", 176.9),   # s8 175.9-183.0  KJV Mark 4:40 (sp 182.31)
    ("audio/n8.mp3", 183.5),   # s8 183.0-208.2  the bridge (sp 207.76)
    ("audio/n9.mp3", 208.9),   # s9 208.2-244.0  what manner (sp 243.16)
    ("audio/n10.mp3", 244.6),  # card 244.0-264.0  closing read (sp 262.19)
]

# The calm cut: every non-voice sound is gone at j1's last word.
CALM_CUT = 139.41

# Detuned-pair beds. Evening bed out before the storm; warm bed returns
# at n7 and is fully out before the card. s7 and the card in silence.
# (start_s, end_s, style) — style "a" = fuller, "b" = quieter/warmer.
BEDS = [
    (0.0, 48.0, "b"),        # evening departure; out before the lake turns
    (167.0, 240.0, "a"),     # he turned to them -> awe; out before the card
]

# Storm ambience: brown noise shaped into wind/waves, building under
# s3-s6 and dying EXACTLY at CALM_CUT.
AMB_START = 48.5


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:160], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


def caption_overlay(seg_id, dur, text, style):
    """Caption on its own transparent RGBA canvas, alpha-faded 0.5s in/out,
    gone before the cut — captions never pop (Assembly Craft Laws)."""
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
            f"drawtext=fontfile='{font}':textfile={tf}:fontsize={size}:"
            f"fontcolor={color}:line_spacing=14:x=(w-text_w)/2:y=min(h-460\\,h-160-text_h):"
            f"shadowcolor=black@0.85:shadowx=2:shadowy=2:"
            f"box=1:boxcolor=black@0.34:boxborderw=18,"
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
    # lanczos down to 1080x1920.
    base = (f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ""
    if seg_id == "n0a":
        tail = ",fade=t=in:st=0:d=1.2"
    if seg_id == "n9b":
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    fc = assemble_segment(seg_id, base, dur, cap, style, tail)
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_clip(seg_id, src, stretch, dur, cap, style):
    """Veo clip stretched (8s -> 12.8s) so the money motion carries its
    beat without a hard cut mid-motion."""
    base = (f"[0:v]setpts={stretch}*PTS,scale=1080:1920:flags=lanczos,"
            f"setsar=1,fps={FPS},unsharp=5:5:0.35:5:5:0.0")
    fc = assemble_segment(seg_id, base, dur, cap, style, "")
    run([FF, "-y", "-i", f"{A}/{src}",
         "-filter_complex", fc, "-map", "[v]", "-t",
         str(dur)] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(seg_id, dur, text):
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w", encoding="utf-8") as f:
        f.write(text)
    vf = (f"drawtext=fontfile='{SERIF}':textfile={tf}:fontsize=50:"
          f"fontcolor={INK}:line_spacing=22:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
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
    return (f"{src}:s=44100:d={dur},{eq},"
            f"afade=t=in:st=0:d={fin},afade=t=out:st={dur-fout}:d={fout}"
            f"{delay}[mus{idx}]")


def storm_ambience_filter(idx):
    """Brown-noise wind/waves from AMB_START, building slowly, dying with
    a fast 0.25s fade that ends EXACTLY at CALM_CUT (the pack's all-sound-
    cuts-to-silence law)."""
    dur = CALM_CUT - AMB_START
    ms = int(AMB_START * 1000)
    return (f"anoisesrc=color=brown:amplitude=0.22:r=44100:d={dur:.2f},"
            f"lowpass=f=450,tremolo=f=0.24:d=0.55,volume=0.42,"
            f"afade=t=in:st=0:d=6,"
            f"afade=t=out:st={dur-0.25:.2f}:d=0.25,"
            f"adelay={ms}|{ms}[mus{idx}]")


def main():
    os.makedirs(S, exist_ok=True)
    total = sum(s[4] for s in SEGMENTS)
    print(f"total runtime: {total:.1f}s", flush=True)

    for seg_id, kind, src, stretch, dur, zdir, cap, style in SEGMENTS:
        if kind == "still":
            build_still(seg_id, src, dur, zdir, cap, style)
        elif kind == "clip":
            build_clip(seg_id, src, stretch, dur, cap, style)
        else:
            build_card(seg_id, dur, cap)

    with open(f"{S}/concat.txt", "w") as f:
        for seg in SEGMENTS:
            f.write(f"file '{seg[0]}.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at absolute offsets + beds + storm ambience ----
    inputs = []
    filters = []
    labels = []
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
    filters.append(storm_ambience_filter(bi))
    labels.append(f"[mus{bi}]")
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
            lufs = float(line.split()[1])
    gain = 0.0
    if lufs is not None:
        gain = max(-6.0, min(10.0, -15.0 - lufs))
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    # ---- final mux: veryslow, runtime-computed rate cap, crf step-up ----
    OUT = "mark-4_calming-the-storm.mp4"   # SCRIPTURE-NAME LAW
    vcap = max(300, int(24.5 * 8000 / total) - 145)
    size = 0.0
    crf = 21
    for crf in (21, 22, 23, 24, 25):
        run([FF, "-y", "-i", f"{S}/video_silent.mp4",
             "-i", f"{S}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "veryslow", "-crf", str(crf),
             "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
             OUT])
        size = os.path.getsize(OUT) / 1e6
        if size <= 24.5:
            break
        print(f"  {size:.1f} MB at crf {crf} — over budget, stepping up",
              flush=True)
    print(f"DONE: {OUT}  {size:.1f} MB, {total:.1f}s "
          f"(crf {crf}, vcap {vcap}k)", flush=True)


if __name__ == "__main__":
    main()
