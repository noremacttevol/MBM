#!/usr/bin/env python3
"""Assemble Story Video #13 — Through the Roof (Mark 2:1-12).

Full law stack per PRODUCTION-BIBLE.md + PREFLIGHT.md. Hybrid storybook:
10 painted 2K stills with Ken Burns drift + 2 Veo money-moment clips
(CLIP A the lowering through the roof, 8s stretched to 12.8s; CLIP B the
rise and first steps, 8s stretched to 12.8s), edge-tts narration
(ear-checked 16/16), serif captions, KJV red-letter j1 (Mark 2:5),
j2 (Mark 2:9), j3 (Mark 2:11) — all exact against qc/mark2-kjv.txt.
Closing question card on cream #F7F2E9, read aloud (Readable-Card Law).

Assembly Craft Laws: supersampled zoompan (anti-shimmer), RGBA caption
fades, crf-16 intermediates, veryslow crf step-up final, loudness toward
-15 LUFS, detuned-pair beds.

THE SOUND LAW OF THIS VIDEO (per PREFLIGHT): a warm bed opens and dies to
FULL SILENCE just before j1 ("Son, thy sins be forgiven thee") — the
sacred pause of this film; the forgiveness beat (j1 + n6) plays in true
silence; quiet resumes under the scribes (n7) and builds gently through
the rise; out before the closing card, which is read in silence.

All offsets computed from MEASURED mp3 durations + measured trailing
silence (spoken end = start + last_silence_start); breaths 0.8-1.6s,
~1.5s held quiet before j1, j2, j3.

Output: mark-2_man-through-the-roof.mp4 (SCRIPTURE-NAME LAW),
1080x1920 H.264 30fps, <25MB, 334.0s.
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

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-carried.jpeg"
S2 = "s2-no-way-through.jpeg"
S3 = "s3-digging.jpeg"
S4 = "s4-lowered.jpeg"
S5 = "s5-their-faith.jpeg"
S6 = "s6-deepest-wound.jpeg"
S7 = "s7-scribes.jpeg"
S8 = "s8-answered-thoughts.jpeg"
S9 = "s9-arise.jpeg"
S9B = "s9b-holding-mat.jpeg"
S10 = "s10-out-the-door.jpeg"
CLIP_LOWER = "s4-lowering-clip.mp4"
CLIP_RISE = "s9-rise-clip.mp4"

# (id, kind, source, stretch_or_none, duration_s, zoom_dir, caption, style)
# Boundaries: 0, 14.0, 28.0, 40.0, 52.0, 67.0, 82.0, 93.8, 106.6, 119.1,
# 131.6, 145.1, 149.4, 164.4, 179.4, 191.3, 203.2, 215.6, 228.4, 241.5,
# 254.6, 263.4, 271.2, 284.0, 298.0, 312.0, 334.0.
SEGMENTS = [
    # n0 — carried through the streets (s1). v1-3.
    ("n0a", "still", S1, None, 14.0, "in",
     "Capernaum, on the north shore of the\n"
     "Sea of Galilee. Jesus was home — and\n"
     "the word got out. Four men came up the\n"
     "street carrying their friend on a\n"
     "sleeping mat, one at each corner.", "n"),
    ("n0b", "still", S1, None, 14.0, "out",
     "The man on the mat was paralyzed. He\n"
     "could not walk to Jesus. So the people\n"
     "who loved him decided he would get\n"
     "there anyway.", "n"),
    # n1 — no way through (s2). v2 + v4a.
    ("n1a", "still", S2, None, 12.0, "in",
     "But the doorway was a wall of backs.\n"
     "People packed the room, packed the\n"
     "doorway, spilled into the street — no\n"
     "one was giving up a spot, not even for\n"
     "a man on a mat.", "n"),
    ("n1b", "still", S2, None, 12.0, "out",
     "Four friends stood there breathing\n"
     "hard, holding their friend, staring at\n"
     "an impossible crowd. And then one of\n"
     "them looked up. At the roof.", "n"),
    # n2 — digging through (s3). v4 + roof study-gem.
    ("n2a", "still", S3, None, 15.0, "in",
     "Houses there had flat roofs of packed\n"
     "clay over reeds and beams, with a\n"
     "stairway up the outside wall. You\n"
     "could dig through one with your hands\n"
     "in a few minutes — and patch it in a\n"
     "day.", "n"),
    ("n2b", "still", S3, None, 15.0, "out",
     "Which is exactly what they did. Four\n"
     "men on a stranger's roof, tearing\n"
     "through the clay, coughing in the\n"
     "dust, grinning at each other like men\n"
     "doing something magnificent and\n"
     "slightly insane.", "n"),
    # n3 — THE LOWERING (s4 STILL first per Correction #10, THEN the clip).
    ("n3a", "still", S4, None, 11.8, "in",
     "Below them, in the middle of the\n"
     "sermon, the ceiling cracked open.\n"
     "Daylight poured into the dark room\n"
     "through falling dust and straw.", "n"),
    # PHASE-1 STILLS-ONLY (Cameron, 2026-07-11, LAW E): the lowering money-shot
    # was a Veo clip; replaced with the banked s4 still on the opposite drift so
    # the peak beat holds and slowly moves while the narration lands. Phase 2 may
    # restore CLIP_LOWER here.
    ("n3b", "still", S4, None, 12.8, "out",
     "And down through that column of\n"
     "light, swaying on four ropes, lowered\n"
     "with enormous care, came a man on a\n"
     "mat — landing right at the feet of\n"
     "Jesus.", "n"),
    # n4 — THEIR faith (s5). v5a — the Seed's hinge.
    ("n4a", "still", S5, None, 12.5, "in",
     "Now listen to what the story says\n"
     "next, because it is easy to miss.\n"
     "When Jesus saw their faith — theirs.\n"
     "The friends'. The four sweat-streaked\n"
     "faces ringing the hole in the roof.", "n"),
    ("n4b", "still", S5, None, 12.5, "out",
     "The man on the mat hadn't said a\n"
     "word. His friends' faith counted for\n"
     "him. He was carried there — and\n"
     "heaven honored the carrying.", "n"),
    # n5 — setup for j1 (s6). Music dies to silence at the end of this.
    ("n5", "still", S6, None, 13.5, "in",
     "And Jesus looked at the man lying in\n"
     "the dusty light — a man braced for\n"
     "words about his legs — and the first\n"
     "thing he said was not about his legs\n"
     "at all.", "n"),
    # J1 — exact KJV Mark 2:5, spoken into TRUE SILENCE.
    ("j1", "still", S6, None, 4.3, "out",
     "\u201cSon, thy sins be\nforgiven thee.\u201d", "kjv"),
    # n6 — the deepest wound first (s6), still in silence.
    ("n6a", "still", S6, None, 15.0, "in",
     "The first word was son. Not a\n"
     "diagnosis. Not a lecture about his\n"
     "legs. Son — and then forgiveness. In\n"
     "that world, everyone assumed a body\n"
     "like his was the proof of some hidden\n"
     "guilt —", "n"),
    ("n6b", "still", S6, None, 15.0, "out",
     "he had carried the shame along with\n"
     "the paralysis his whole life. Jesus\n"
     "went to the deepest wound first. His\n"
     "legs had not moved yet. And it was\n"
     "already the miracle.", "n"),
    # n7 — the scribes (s7). v6-7. Quiet bed resumes here.
    ("n7a", "still", S7, None, 11.9, "in",
     "But in the corner sat the scribes —\n"
     "the religious experts — and nothing\n"
     "about this made them glad. They\n"
     "didn't say a word out loud.", "n"),
    ("n7b", "still", S7, None, 11.9, "out",
     "They reasoned it in their hearts:\n"
     "this is blasphemy. No one can forgive\n"
     "sins but God alone. And on the logic,\n"
     "they were exactly right. That was the\n"
     "point they refused to see.", "n"),
    # n8 — he answered their thoughts (s8, over-the-shoulder, law #11).
    ("n8", "still", S8, None, 12.4, "in",
     "And then came the strangest moment\n"
     "in that room — stranger than the\n"
     "ceiling. Jesus knew what they were\n"
     "thinking. They had said nothing, and\n"
     "he answered them anyway:", "n"),
    # J2 — exact KJV Mark 2:9.
    ("j2", "still", S8, None, 12.8, "out",
     "\u201cWhether is it easier to say to the\n"
     "sick of the palsy, Thy sins be\n"
     "forgiven thee; or to say, Arise, and\n"
     "take up thy bed, and walk?\u201d", "kjv"),
    # n9 — translation bridge + v10 reason (s8).
    ("n9a", "still", S8, None, 13.1, "in",
     "He was asking them: which is easier\n"
     "to say? Anyone can announce that sins\n"
     "are forgiven — no one can check. But\n"
     "tell a paralyzed man to stand, and\n"
     "everyone in the room finds out in a\n"
     "second what your words are worth.", "n"),
    ("n9b", "still", S8, None, 13.1, "out",
     "So — he said — so that you will know\n"
     "the forgiveness was real, watch this.\n"
     "He turned back to the man on the mat:", "n"),
    # J3 — exact KJV Mark 2:11, over the mat-man still.
    ("j3", "still", S6, None, 8.8, "in",
     "\u201cI say unto thee, Arise, and take up\n"
     "thy bed, and go thy way into thine\n"
     "house.\u201d", "kjv"),
    # n10 — ARISE (s9 STILL first per Correction #10, THEN the clip).
    ("n10a", "still", S9, None, 7.8, "in",
     "And immediately, he did. He stood —\n"
     "on legs trembling like a newborn\n"
     "colt's — while the crowd pulled back\n"
     "and the dust floated in the light.", "n"),
    # n10b — mat carried (s9b STILL). The botched Veo rise/mat-roll clip was
    # cut (2026-07-11, Cameron: mat rolled without touching + feet under it);
    # the roll happens in the cut, which this line narrates. Clean still only.
    ("n10b", "still", S9B, None, 12.8, "out",
     "Then he bent down, rolled up his mat,\n"
     "and tucked it under his arm. The bed\n"
     "that had carried him, he carried\n"
     "home.", "n"),
    # n11 — out before them all (s10). v12.
    ("n11a", "still", S10, None, 14.0, "in",
     "He walked out the door in front of\n"
     "everyone — through the same crowd\n"
     "that had no room for him an hour\n"
     "before. They made room now.", "n"),
    ("n11b", "still", S10, None, 14.0, "out",
     "Mark says they were all amazed, and\n"
     "gave the glory to God, and said to\n"
     "each other: we have never seen\n"
     "anything like this. And up on the\n"
     "roofline, four filthy, grinning\n"
     "friends pounded each other's\n"
     "shoulders and laughed toward heaven.", "n"),
    # Card — pack card verbatim, held 22.0s AND read aloud, in silence.
    ("card", "card", None, None, 22.0, None,
     "Four people tore a roof open\n"
     "because their friend could not\n"
     "get there alone.\n\n"
     "His faith didn't carry him that\n"
     "day — theirs did, and heaven\n"
     "counted it.\n\n"
     "So here is the question this story\n"
     "leaves behind: where do you find\n"
     "yourself in that room?\n\n"
     "On the mat — or holding a rope?",
     "close"),
]

# narration placements: (audio file, absolute start seconds)
# measured dur/last_silence_start: n0 26.784/26.40  n1 23.184/22.75
#   n2 29.160/28.70  n3 23.688/23.23  n4 24.408/23.93  n5 12.096/11.64
#   j1 4.488/3.19  n6 29.184/28.74  n7 22.920/22.53  n8 11.496/11.10
#   j2 12.744/11.50  n9 25.584/25.13  j3 8.760/7.53  n10 19.752/19.33
#   n11 27.240/26.77  n12 20.784/20.31
# breaths 0.8-1.6s between SPOKEN ends; ~1.5s held quiet before j1/j2/j3.
AUDIO = [
    ("audio/n0.mp3", 0.6),     # s1 0-28.0       carried (sp end 27.00)
    ("audio/n1.mp3", 28.4),    # s2 28.0-52.0    wall of backs (sp 51.15)
    ("audio/n2.mp3", 52.4),    # s3 52.0-82.0    digging (sp 81.10)
    ("audio/n3.mp3", 82.4),    # s4+clip 82.0-106.6  THE LOWERING (sp 105.63)
    ("audio/n4.mp3", 107.0),   # s5 106.6-131.6  their faith (sp 130.93)
    ("audio/n5.mp3", 132.0),   # s6 131.6-145.1  braced (sp 143.64)
    ("audio/j1.mp3", 145.5),   # s6 145.1-149.4  KJV Mark 2:5 (sp 148.69)
    ("audio/n6.mp3", 149.9),   # s6 149.4-179.4  deepest wound (sp 178.64)
    ("audio/n7.mp3", 179.8),   # s7 179.4-203.2  scribes (sp 202.33)
    ("audio/n8.mp3", 203.6),   # s8 203.2-215.6  answered (sp 214.70)
    ("audio/j2.mp3", 216.2),   # s8 215.6-228.4  KJV Mark 2:9 (sp 227.70)
    ("audio/n9.mp3", 228.8),   # s8 228.4-254.6  the bridge (sp 253.93)
    ("audio/j3.mp3", 255.4),   # s6 254.6-263.4  KJV Mark 2:11 (sp 262.93)
    ("audio/n10.mp3", 263.9),  # s9+clip 263.4-284.0  he rose (sp 283.23)
    ("audio/n11.mp3", 284.4),  # s10 284.0-312.0 out the door (sp 311.17)
    ("audio/n12.mp3", 312.6),  # card 312.0-334.0 closing read (sp 332.91)
]

# Detuned-pair beds. Warm bed opens and dies to FULL SILENCE before j1
# (145.5); silence holds through the forgiveness (j1+n6); quiet bed
# resumes at the scribes and is out before the card.
# (start_s, end_s, style) — "a" = fuller, "b" = quieter/warmer.
BEDS = [
    (0.0, 144.6, "b"),       # opening -> dies just before j1
    (179.4, 308.5, "a"),     # scribes -> rise -> celebration; out pre-card
]


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:160], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


def caption_overlay(seg_id, dur, text, style):
    """Caption on its own transparent RGBA canvas, alpha-faded 0.5s in/out,
    gone before the cut — captions never pop (Assembly Craft Laws)."""
    if not text:
        return None
    tf = f"{S}/{seg_id}.txt"
    with open(tf, "w") as f:
        f.write(text)
    if style == "kjv":
        font, size, color = SERIF_BI, 46, "0xFFF3DC"
    else:
        font, size, color = SERIF, 40, "white"
    fade_out = max(0.0, dur - 0.6)
    return (f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile={font}:textfile={tf}:fontsize={size}:"
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
    base = (f"[0:v]scale=4320:7680,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ""
    if seg_id == "n0a":
        tail = ",fade=t=in:st=0:d=1.2"
    if seg_id == "n11b":
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    fc = assemble_segment(seg_id, base, dur, cap, style, tail)
    run(["ffmpeg", "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_clip(seg_id, src, stretch, dur, cap, style):
    """Veo clip stretched (8s -> 12.8s) so the money motion carries its
    beat without a hard cut mid-motion."""
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
    vf = (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize=50:"
          f"fontcolor={INK}:line_spacing=22:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run(["ffmpeg", "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
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
            build_clip(seg_id, src, stretch, dur, cap, style)
        else:
            build_card(seg_id, dur, cap)

    with open(f"{S}/concat.txt", "w") as f:
        for seg in SEGMENTS:
            f.write(f"file '{seg[0]}.mp4'\n")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at absolute offsets + beds ----
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
    n = len(labels)
    filters.append("".join(labels) +
                   f"amix=inputs={n}:duration=longest:normalize=0,"
                   f"apad=whole_dur={total}[aout]")
    run(["ffmpeg", "-y"] + inputs + ["-filter_complex", ";".join(filters),
         "-map", "[aout]", "-t", str(total), "-c:a", "aac", "-b:a", "160k",
         f"{S}/audio_mix.m4a"])

    # ---- loudness law: measure EBU R128, lift toward -15 LUFS ----
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
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    # ---- final mux: veryslow, runtime-computed rate cap, crf step-up ----
    OUT = "mark-2_man-through-the-roof.mp4"   # SCRIPTURE-NAME LAW
    vcap = max(300, int(24.5 * 8000 / total) - 145)
    size = 0.0
    crf = 21
    for crf in (21, 22, 23, 24, 25):
        run(["ffmpeg", "-y", "-i", f"{S}/video_silent.mp4",
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
