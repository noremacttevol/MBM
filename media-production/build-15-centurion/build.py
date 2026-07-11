#!/usr/bin/env python3
"""Assemble Story Video #15 — The Centurion's Servant (Matthew 8:5-13).

Full law stack per PRODUCTION-BIBLE.md + PREFLIGHT.md. Hybrid storybook:
12 painted 2K stills with Ken Burns drift + 2 Veo money-moment clips (the
centurion's street approach; the servant healed at a distance), edge-tts
narration (ear-checked 17/17), serif captions, KJV red-letter j1 (Matt 8:7),
j2 (8:10), j2b (8:11-12), j3 (8:13) — all exact against qc/matthew8-kjv.txt.
Closing question card on cream #F7F2E9, read aloud (Readable-Card Law).

Correction #18: the robed figure (the Lord) is shown ONLY from behind /
over-the-shoulder / at a distance in every still he appears in (s1,s4,s5,s6,
s8,s10) — his face is never in frame. Both clips are free of him.

Assembly Craft Laws: supersampled zoompan (anti-shimmer), RGBA caption fades,
crf-16 intermediates, veryslow crf step-up final, loudness toward -15 LUFS,
detuned-pair beds.

THE SOUND LAW OF THIS VIDEO (pack law): a warm bed opens and fades to FULL
SILENCE before the peak — "And Jesus marveled" (end of n6). j2 ("I have not
found so great faith") lands in true silence. A warm bed returns at n7 and is
fully out before the closing card, which is read in silence.

All offsets computed from MEASURED mp3 durations + measured trailing silence.

Output: matthew-8_centurion.mp4 (SCRIPTURE-NAME LAW), 1080x1920 H.264 30fps,
<25MB.
"""
import os
import subprocess

A = "assets"
S = "segs"
FPS = 30
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-capernaum.jpeg"
S2 = "s2-sick-servant.jpeg"
S3 = "s3-approach.jpeg"
S4 = "s4-the-plea.jpeg"
S5 = "s5-i-will-come.jpeg"
S6 = "s6-speak-the-word.jpeg"
S7 = "s7-authority.jpeg"
S8 = "s8-marvels.jpeg"
S9 = "s9-east-west.jpeg"
S10 = "s10-go-thy-way.jpeg"
S11 = "s11-healing.jpeg"
S12 = "s12-reunion.jpeg"
CLIP_APPROACH = "s3-approach-clip.mp4"
CLIP_HEALING = "s11-healing-clip.mp4"

# (id, kind, source, stretch_or_none, duration_s, zoom_dir, caption, style)
SEGMENTS = [
    # n0 — Capernaum arrival (s1). Garrison-town setup.
    ("n0a", "still", S1, None, 13.6, "in",
     "Capernaum, a fishing town on the north\n"
     "shore of the Sea of Galilee. It was\n"
     "Jesus's home base — but it was also a\n"
     "garrison town: Roman soldiers on the\n"
     "streets of a Jewish village.", "n"),
    ("n0b", "still", S1, None, 13.7, "out",
     "Rome was the occupying power, the boot\n"
     "on the neck of everyone here. So when\n"
     "the man at the center of this story\n"
     "walks in — remember what uniform he is\n"
     "wearing.", "n"),
    # n1 — the sick servant (s2).
    ("n1a", "still", S2, None, 14.6, "in",
     "Across town, in a Roman officer's house,\n"
     "a young servant lay dying. The word the\n"
     "text uses is palsy — his body had seized\n"
     "up, paralyzed, and he was in constant\n"
     "pain.", "n"),
    ("n1b", "still", S2, None, 14.6, "out",
     "In that world a servant was property; a\n"
     "sick one could simply be replaced. But\n"
     "this officer set his armor aside and sat\n"
     "with the boy, trying to help.", "n"),
    # n2 — THE APPROACH (s3 STILL first per #10, THEN the clip, then still).
    ("n2a", "still", S3, None, 14.0, "in",
     "A centurion — the commander of a hundred\n"
     "soldiers, a hard career officer near the\n"
     "top of the local command. And he came\n"
     "himself, in armor, to a Jewish teacher.", "n"),
    ("n2b", "clip", CLIP_APPROACH, 1.6, 13.0, None,
     "Picture that street going silent as he\n"
     "walks it: the enemy's officer, moving\n"
     "through a village that had every reason\n"
     "to hate him.", "n"),
    ("n2c", "still", S3, None, 14.5, "out",
     "Another account says this Roman loved\n"
     "the Jewish people and had built their\n"
     "synagogue — a rare soldier. And he came\n"
     "for a servant. Not a son. A servant.", "n"),
    # n3 — the plea (s4, #18 over-the-shoulder).
    ("n3", "still", S4, None, 19.9, "in",
     "He reached the teacher, and this\n"
     "commander of a hundred men bowed his\n"
     "head. His servant was at home, he said —\n"
     "paralyzed, in agony. Could something be\n"
     "done? He asked it plainly, the way a\n"
     "soldier makes a report.", "n"),
    # J1 — exact KJV Matthew 8:7.
    ("j1", "still", S5, None, 4.0, "in",
     "“I will come and heal him.”", "kjv"),
    # n4 — not worthy / say the word (s6, #18 over-the-shoulder).
    ("n4a", "still", S6, None, 16.6, "in",
     "Jesus answered at once — he would come\n"
     "to the house himself. And that is where\n"
     "the Roman stopped him. Lord, he said, I\n"
     "am not worthy to have you come under my\n"
     "roof. Only say the word, and my servant\n"
     "will be healed.", "n"),
    ("n4b", "still", S6, None, 16.7, "out",
     "By custom, a Jew who stepped into a\n"
     "Gentile's house became unclean; the\n"
     "centurion knew it, and would not put\n"
     "that on him. But underneath the courtesy\n"
     "was something bigger.", "n"),
    # n5 — authority logic (s7, no robed figure).
    ("n5a", "still", S7, None, 18.8, "in",
     "He explained the faith behind it in the\n"
     "only language he knew — the chain of\n"
     "command. I am a man under authority\n"
     "myself, he said. I tell one soldier go,\n"
     "and he goes; another come, and he comes.", "n"),
    ("n5b", "still", S7, None, 18.8, "out",
     "I do not have to march them there. I\n"
     "speak, and it is done. He believed this\n"
     "teacher's word could cross a whole town\n"
     "and move a disease just as surely. He\n"
     "only needed him to speak.", "n"),
    # n6 — Jesus marvels (s8). THE PEAK — music dies to silence at the end.
    ("n6", "still", S8, None, 22.6, "in",
     "And Jesus marveled. Stop on that word.\n"
     "The Gospels almost never say Jesus was\n"
     "amazed by anyone — twice only: once at\n"
     "his own hometown, for how little they\n"
     "believed, and once here, for how much\n"
     "this outsider did. He turned to the\n"
     "crowd and said:", "n"),
    # J2 — exact KJV Matthew 8:10. Lands in sacred silence.
    ("j2", "still", S8, None, 9.2, "out",
     "“Verily I say unto you, I have not\n"
     "found so great faith, no, not in\n"
     "Israel.”", "kjv"),
    # n7 — bridge to the opened door (s9 vista). Warm bed returns here.
    ("n7", "still", S9, None, 20.1, "in",
     "Truly, he said — mark this. And he said\n"
     "it about a Roman officer, the enemy, a\n"
     "Gentile, in front of the very people\n"
     "certain that faith belonged to them\n"
     "alone. Then he opened the door wider than\n"
     "anyone there wanted it opened:", "n"),
    # J2b — exact KJV Matthew 8:11-12.
    ("j2b", "still", S9, None, 22.4, "out",
     "“Many shall come from the east and\n"
     "west, and shall sit down with Abraham,\n"
     "and Isaac, and Jacob, in the kingdom of\n"
     "heaven. But the children of the kingdom\n"
     "shall be cast out into outer darkness.”",
     "kjv"),
    # n8 — plain meaning (reuse s6, the centurion — "the centurion had it").
    ("n8", "still", S6, None, 24.3, "in",
     "He was saying people would come from\n"
     "every direction — every nation, every\n"
     "kind of outsider — and take their place\n"
     "at God's table. And that being born into\n"
     "the right family, the right religion, the\n"
     "right group, was never the thing that\n"
     "saved anyone. Faith was. The centurion\n"
     "had it.", "n"),
    # n9 — j3 setup (s10, #18 over-the-shoulder).
    ("n9", "still", S10, None, 7.2, "in",
     "Then Jesus turned back to the soldier and\n"
     "gave him the one thing he had asked for —\n"
     "a word.", "n"),
    # J3 — exact KJV Matthew 8:13a.
    ("j3", "still", S10, None, 6.0, "out",
     "“Go thy way; and as thou hast\n"
     "believed, so be it done unto thee.”",
     "kjv"),
    # n10 — the walk home + THE HEALING (s11 still first per #10, then clip).
    ("n10a", "still", S11, None, 14.0, "in",
     "Go home, he said — it is done, just as\n"
     "you believed. And there was no proof yet.\n"
     "The officer had to turn and walk the whole\n"
     "way back on nothing but that sentence.", "n"),
    ("n10b", "clip", CLIP_HEALING, 1.6, 13.0, None,
     "And in that same hour, across the town,\n"
     "in a room Jesus never entered, the young\n"
     "servant drew a sudden clean breath.", "n"),
    ("n10c", "still", S11, None, 14.6, "out",
     "The color came back into his face like\n"
     "dawn filling a room. He sat up, whole —\n"
     "and no one was there to see it. It\n"
     "happened on a word spoken half a town\n"
     "away.", "n"),
    # n11 — the reunion (s12).
    ("n11", "still", S12, None, 22.3, "in",
     "When the officer reached his door, his\n"
     "servant was on his feet to meet him —\n"
     "well, ordinary, alive. The hard-faced man\n"
     "who commanded a hundred soldiers put a\n"
     "hand over his mouth, and his composure\n"
     "quietly came apart. He had trusted a\n"
     "word, and the word had been enough.", "n"),
    # Card — pack card verbatim, held ~15s AND read aloud, in silence.
    ("card", "card", None, None, 15.0,  None,
     "“I am not worthy to have you under\n"
     "my roof — but say the word.”\n\n"
     "Which half of that sentence is\n"
     "easier for you to say?",
     "close"),
]

# narration placements: (audio file, absolute start seconds).
# measured dur / last_silence_start (the SPOKEN end):
#   n0 26.86/26.40  n1 28.87/28.43  n2 41.28/40.84  n3 19.36/18.92
#   j1 3.12/1.95    n4 32.83/32.40  n5 37.27/36.85  n6 22.20/21.76
#   j2 8.95/7.71    n7 19.70/19.25  j2b 22.06/20.91 n8 23.92/23.48
#   n9 7.00/6.57    j3 6.69/5.47    n10 41.13/40.72 n11 21.88/21.42
#   n12 8.49/8.08
AUDIO = [
    ("audio/n0.mp3", 0.6),      # s1     0.0-27.3
    ("audio/n1.mp3", 27.8),     # s2     27.3-56.5
    ("audio/n2.mp3", 57.0),     # s3+clip 56.5-98.0
    ("audio/n3.mp3", 98.5),     # s4     98.0-117.9
    ("audio/j1.mp3", 118.4),    # s5     117.9-121.9  KJV 8:7
    ("audio/n4.mp3", 122.4),    # s6     121.9-155.2
    ("audio/n5.mp3", 155.7),    # s7     155.2-192.8
    ("audio/n6.mp3", 193.3),    # s8     192.8-215.4  PEAK; bed dies ~215
    ("audio/j2.mp3", 216.0),    # s8     215.4-224.6  KJV 8:10 in SILENCE
    ("audio/n7.mp3", 225.1),    # s9     224.6-244.7  bed returns
    ("audio/j2b.mp3", 245.3),   # s9     244.7-267.1  KJV 8:11-12
    ("audio/n8.mp3", 267.6),    # s6r    267.1-291.4
    ("audio/n9.mp3", 291.9),    # s10    291.4-298.6
    ("audio/j3.mp3", 298.9),    # s10    298.6-304.6  KJV 8:13
    ("audio/n10.mp3", 305.0),   # s11+clip 304.6-346.2
    ("audio/n11.mp3", 346.7),   # s12    346.2-368.5
    ("audio/n12.mp3", 369.2),   # card   368.5-383.5  read in silence
]

# Two detuned-pair warm beds with a SILENCE GAP over the marvel + j2 (the
# pack's peak). Bed 1 fades out before "And Jesus marveled" lands (~215s);
# j2 in silence; bed 2 returns at n7 and is out before the card.
BEDS = [
    (0.0, 213.0, "b"),     # warm; out before the marvel peak
    (225.0, 360.0, "a"),   # returns at n7; out before the card
]


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:150], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


def caption_overlay(seg_id, dur, text, style):
    if not text:
        return None
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w") as f:
        f.write(text)
    if style == "kjv":
        font, size, color = SERIF_BI, 46, "0xFFF3DC"
    else:
        font, size, color = SERIF, 38, "white"
    fade_out = max(0.0, dur - 0.6)
    return (f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile={font}:textfile={tf}:fontsize={size}:"
            f"fontcolor={color}:line_spacing=14:x=(w-text_w)/2:"
            f"y=min(h-500\\,h-170-text_h):"
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
    # Anti-shimmer: zoompan OUTPUTS at 2x delivery (2160x3840) then lanczos
    # down to 1080x1920 so crop-rounding lands on half-pixels. Input pre-scaled
    # to 2160 wide (lighter than 4x) to keep the drift smooth without the very
    # heavy 4320x7680 per-frame cost.
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ""
    if seg_id == "n0a":
        tail = ",fade=t=in:st=0:d=1.2"
    if seg_id == "n11":
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    fc = assemble_segment(seg_id, base, dur, cap, style, tail)
    run(["ffmpeg", "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_clip(seg_id, src, stretch, dur, cap, style):
    base = (f"[0:v]setpts={stretch}*PTS,scale=1080:1920:flags=lanczos,"
            f"setsar=1,fps={FPS},unsharp=5:5:0.35:5:5:0.0")
    fc = assemble_segment(seg_id, base, dur, cap, style, "")
    run(["ffmpeg", "-y", "-i", f"{A}/{src}",
         "-filter_complex", fc, "-map", "[v]", "-t",
         str(dur)] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(seg_id, dur, text):
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w") as f:
        f.write(text)
    vf = (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize=52:"
          f"fontcolor={INK}:line_spacing=22:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run(["ffmpeg", "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/{seg_id}.mp4"])


def bed_filter(idx, start, end, style):
    dur = end - start
    if style == "a":
        src = ("aevalsrc='0.020*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
               "+0.015*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))"
               "+0.011*sin(2*PI*220*t)+0.007*sin(2*PI*329.63*t)'")
        eq = "lowpass=f=760,tremolo=f=0.12:d=0.3,aecho=0.7:0.4:311|429:0.24|0.17"
        fin, fout = 6, 6
    else:
        src = ("aevalsrc='0.013*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
               "+0.010*(sin(2*PI*146.83*t)+sin(2*PI*147.4*t))"
               "+0.008*sin(2*PI*196*t)+0.006*sin(2*PI*220*t)'")
        eq = "lowpass=f=700,tremolo=f=0.10:d=0.3,aecho=0.7:0.4:317|443:0.24|0.17"
        fin, fout = 6, 7
    ms = int(start * 1000)
    delay = f",adelay={ms}|{ms}" if ms else ""
    return (f"{src}:s=44100:d={dur},{eq},"
            f"afade=t=in:st=0:d={fin},afade=t=out:st={dur-fout}:d={fout}"
            f"{delay}[mus{idx}]")


def main():
    os.makedirs(S, exist_ok=True)
    total = sum(s[4] for s in SEGMENTS)
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min)", flush=True)

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
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i",
         f"{S}/concat.txt", "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at absolute offsets + warm beds ----
    inputs = []
    filters = []
    labels = []
    for i, (path, start) in enumerate(AUDIO):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(
            f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
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
    run(["ffmpeg", "-y"] + inputs + ["-filter_complex", ";".join(filters),
         "-map", "[aout]", "-t", str(total), "-c:a", "aac", "-b:a", "160k",
         f"{S}/audio_mix.m4a"])

    # ---- loudness law: measure EBU R128, lift toward -15 LUFS ----
    probe = subprocess.run(
        ["ffmpeg", "-i", f"{S}/audio_mix.m4a", "-af", "ebur128",
         "-f", "null", "-"], capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            lufs = float(line.split()[1])
    gain = 0.0
    if lufs is not None:
        gain = max(-6.0, min(10.0, -15.0 - lufs))
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB",
          flush=True)

    # ---- final mux: veryslow, runtime-computed rate cap, crf step-up ----
    OUT = "matthew-8_centurion.mp4"   # SCRIPTURE-NAME LAW
    vcap = max(300, int(24.5 * 8000 / total) - 120)
    size = 0.0
    crf = 21
    for crf in (21, 22, 23, 24, 25):
        run(["ffmpeg", "-y", "-i", f"{S}/video_silent.mp4",
             "-i", f"{S}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
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
