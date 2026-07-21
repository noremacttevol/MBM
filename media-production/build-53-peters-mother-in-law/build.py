#!/usr/bin/env python3
"""Assemble Video #53 — Peter's Mother-in-Law (Mark 1:29-31).

PHASE-1 STILLS-ONLY build (Law E): eight painted stills with slow Ken Burns drift,
narration, serif captions (CAPTION v2), closing invitation card. NO AI motion clips.

FACE LAW v3: Jesus's face IS shown, locked to JESUS-MASTER-REF (attached as --ref at
generation). He appears in s1, s2, s4-s8; s3 (the sickbed, before he is told) has no
divine figure. Captions are VERBATIM spoken text from make_narration.SEGMENTS. Jesus
speaks NO words in this passage, so there is NO cream-italic KJV line; the ONE sacred
silence (the music bed dies) lands on the moment he takes her by the hand (n5).

CARE FLAGS: none — GREEN. A gentle, intimate healing; the fever is only flushed weariness,
never gruesome. The hope-beat is the healed woman risen and serving (s7).

Windows-ready: ffmpeg/ffprobe on PATH; Georgia copied to a colon-free relative path
(segs/serif.ttf, serif_bi.ttf) so drawtext's filter parser does not choke on 'C:'.

Output: mark-1_peters-mother-in-law.mp4 (SCRIPTURE-NAME LAW), 1080x1920 H.264 30fps, <30MB.
"""
import os
import shutil
import subprocess
import textwrap

import make_narration  # SEGMENTS -> verbatim caption text per segment
from mbm_caption_timing import caption_filter
from mbm_speakers import is_scripture

A = "assets"
S = "segs"
FPS = 30
FF = "ffmpeg"
FPROBE = "ffprobe"
# Set by _ensure_fonts() to colon-free RELATIVE paths (Windows drawtext parser).
SERIF = "segs/serif.ttf"
SERIF_BI = "segs/serif_bi.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-home-from-synagogue.jpeg"
S2 = "s2-the-house.jpeg"
S3 = "s3-sick-with-fever.jpeg"
S4 = "s4-they-tell-him.jpeg"
S5 = "s5-took-her-by-the-hand.jpeg"
S6 = "s6-the-fever-left-her.jpeg"
S7 = "s7-she-ministered.jpeg"
S8 = "s8-the-quiet-house.jpeg"

# Caption text = verbatim spoken text, keyed by segment name.
TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}
# Jesus speaks no KJV line in this passage -> no cream-italic captions.
KJV = set()
# The reverent beat (music dies, longer breath) is the healing touch, though it is
# narrator text, not a red-letter line.
PAUSE = {"n5"}

# BEATS: (segment_name, still, zoom_dir). Consecutive beats on the SAME still alternate
# in/out so the drift never jumps.
BEATS = [
    ("n1", S1, "in"),
    ("n2", S2, "in"),
    ("n3", S3, "in"),
    ("n4", S4, "in"),
    ("n5", S5, "in"),
    ("s31", S5, "out"),
    ("n6", S6, "in"),
    ("n7", S7, "in"),
    ("n8", S8, "in"),
]

LEAD = 0.28
GAP = 0.65
KJV_GAP = 1.60
# No-dead-air law: the video ends TAIL seconds after the last spoken
# word. Derived, never hand-set. Clears the card's 0.8s fade-out so
# the last word and the fade are never clipped.
TAIL = 1.5


def _ensure_fonts():
    """Copy Georgia to colon-free relative paths for ffmpeg drawtext on Windows."""
    os.makedirs(S, exist_ok=True)
    win = os.environ.get("WINDIR", r"C:\Windows")
    pairs = [(os.path.join(win, "Fonts", "georgia.ttf"), f"{S}/serif.ttf"),
             (os.path.join(win, "Fonts", "georgiai.ttf"), f"{S}/serif_bi.ttf")]
    # Linux fallback: no C:\Windows\Fonts on this box (build-84 precedent).
    _lin = ["/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"]
    for (src, dst), lsrc in zip(pairs, _lin):
        if not os.path.exists(dst):
            shutil.copyfile(src if os.path.exists(src) else lsrc, dst)


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:130], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


def dur_of(path):
    out = subprocess.run(
        [FPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(out.stdout.strip())


def spoken_of(path):
    """Duration of `path` up to its LAST spoken sound (trailing silence removed)."""
    tmp = f"{S}/_spoken.wav"
    run([FF, "-y", "-v", "error", "-i", path, "-af",
         "areverse,silenceremove=start_periods=1:start_threshold=-50dB:"
         "start_duration=0.02,areverse", "-c:a", "pcm_s16le", tmp])
    return dur_of(tmp)


# ---- CAPTION SYSTEM v2 (Cameron, 2026-07-15) ----
def sentences(text):
    import re
    return [p for p in re.split(r"(?<=[.!?;:]) +", text) if p]


def chunk_caption(text, width, max_lines):
    """Split text into pieces whose wrapped form is <= max_lines each."""
    out, cur = [], ""
    for s in sentences(text):
        cand = (cur + " " + s).strip()
        if len(textwrap.wrap(cand, width)) <= max_lines:
            cur = cand
            continue
        if cur:
            out.append(cur)
        if len(textwrap.wrap(s, width)) <= max_lines:
            cur = s
        else:  # one long sentence: split on commas
            piece = ""
            for frag in s.split(", "):
                cand2 = (piece + ", " + frag).strip(", ").strip()
                if len(textwrap.wrap(cand2, width)) <= max_lines:
                    piece = cand2
                else:
                    if piece:
                        out.append(piece)
                    piece = frag
            cur = piece
    if cur:
        out.append(cur)
    return out


def build_still(seg_id, src, dur, zdir, spoken_end, cap_text, speaker, first):
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.09*on/{frames}"
    else:
        z = f"1.091-0.09*on/{frames}"
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    cap = caption_filter(seg_id, dur, spoken_end, cap_text, speaker)
    tail = ",fade=t=in:st=0:d=1.0" if first else ""
    fc = f"{base}{cap}{tail}[v]"
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(dur, text):
    tf = f"{S}/card.txt"
    # UTF-8 so ffmpeg drawtext reads any em-dash correctly (Windows open() defaults to
    # cp1252, which renders "—" as a tofu box).
    with open(tf, "w", encoding="utf-8") as f:
        f.write("\n".join(textwrap.wrap(text, width=30)))
    vf = (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize=52:"
          f"fontcolor={INK}:line_spacing=24:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/card.mp4"])


def bed_filter(idx, start, end, style):
    d = end - start
    if d <= 1.0:
        return None
    if style == "a":
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.6*t))"
               "+0*(sin(2*PI*164.81*t)+sin(2*PI*165.5*t))"
               "+0*sin(2*PI*220*t)+0*sin(2*PI*329.63*t)'")
        eq = "lowpass=f=760,tremolo=f=0.12:d=0.3,aecho=0.7:0.4:311|429:0.24|0.17"
        fin, fout = 6, 6
    else:
        # HUM PURGE (Cameron, 2026-07-16): the sine 'music bed' reads as a background hum in every video — amplitudes zeroed. Do not restore; narration + silence only (PRODUCTION-BIBLE #5b 2026-07-16).
        src = ("aevalsrc='0*(sin(2*PI*110*t)+sin(2*PI*110.5*t))"
               "+0*(sin(2*PI*146.83*t)+sin(2*PI*147.4*t))"
               "+0*sin(2*PI*196*t)+0*sin(2*PI*220*t)'")
        eq = "lowpass=f=700,tremolo=f=0.10:d=0.3,aecho=0.7:0.4:317|443:0.24|0.17"
        fin, fout = 6, 7
    ms = int(start * 1000)
    delay = f",adelay={ms}|{ms}" if ms else ""
    fin = min(fin, d / 3)
    fout = min(fout, d / 3)
    return (f"{src}:s=44100:d={d:.3f},{eq},"
            f"afade=t=in:st=0:d={fin:.2f},afade=t=out:st={d-fout:.2f}:d={fout:.2f}"
            f"{delay}[mus{idx}]")


def main():
    _ensure_fonts()

    spoken = {n: spoken_of(f"audio/{n}.mp3") for n, _, _ in BEATS}
    card_spoken = spoken_of("audio/card.mp3")

    timeline = []
    audio_place = []
    start_of = {}
    t = 0.0
    for name, still, zdir in BEATS:
        speaker = SPEAKER[name]
        gap = KJV_GAP if (is_scripture(speaker) or name in PAUSE) else GAP
        vdur = LEAD + spoken[name] + gap
        a_start = t + LEAD
        audio_place.append((f"audio/{name}.mp3", a_start))
        start_of[name] = a_start
        timeline.append((name, still, zdir, vdur, a_start, speaker))
        t += vdur
    card_vdur = LEAD + card_spoken + TAIL
    card_start = t
    audio_place.append(("audio/card.mp3", card_start + LEAD))
    total = t + card_vdur

    # ---- on-paper silence map: prove no spoken gap exceeds 2.5s BEFORE mixing ----
    worst, worst_at = 0.0, None
    prev_end = None
    for name, _s, _z, _v, a_start, _sp in timeline:
        if prev_end is not None and a_start - prev_end > worst:
            worst, worst_at = a_start - prev_end, name
        prev_end = a_start + spoken[name]
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min)", flush=True)
    print(f"worst spoken gap: {worst:.2f}s before {worst_at} "
          f"(No-Dead-Air law: must be <= 2.5s)", flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s gap before {worst_at} "
                         f"exceeds the 2.5s law")
    print(f"sacred silence (took her by the hand): n5 at {start_of['n5']:.1f}s", flush=True)

    # ---- render every still beat ----
    for i, (seg_id, still, zdir, vdur, _a, speaker) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, LEAD + spoken[seg_id],
                    TEXT[seg_id], speaker, first=(i == 0))
    build_card(card_vdur, TEXT["card"])

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at computed offsets + a warm bed that dies through the one
    #      sacred silence (n5, the healing touch) and returns after it ----
    p1_end = start_of["n5"] + spoken["n5"]
    beds = [
        (0.0, start_of["n5"] - 1.2, "b"),
        (p1_end + 1.0, card_start - 0.8, "a"),
    ]
    print(f"music: bed out before n5 (ends {p1_end:.1f}s); returns after the touch",
          flush=True)

    inputs, filters, labels = [], [], []
    for i, (path, start) in enumerate(audio_place):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(
            f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    bi = 0
    for (bs, be, st) in beds:
        bf = bed_filter(bi, bs, be, st)
        if bf:
            filters.append(bf)
            labels.append(f"[mus{bi}]")
            bi += 1
    m = len(labels)
    filters.append("".join(labels) +
                   f"amix=inputs={m}:duration=longest:normalize=0,"
                   f"apad=whole_dur={total:.2f}[aout]")
    run([FF, "-y"] + inputs + ["-filter_complex", ";".join(filters),
        "-map", "[aout]", "-t", f"{total:.2f}", "-c:a", "aac", "-b:a", "160k",
        f"{S}/audio_mix.m4a"])

    # ---- loudness toward -15 LUFS ----
    probe = subprocess.run(
        [FF, "-i", f"{S}/audio_mix.m4a", "-af", "ebur128", "-f", "null", "-"],
        capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            lufs = float(line.split()[1])
    gain = max(-6.0, min(16.0, -15.0 - lufs)) if lufs is not None else 0.0
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    # ---- final mux: the ONLY lossy generation. Never starve the bitrate. 25MB cap. ----
    OUT = "mark-1_peters-mother-in-law.mp4"
    A_KBPS = 96
    MUX = 20
    vcap = int(24.0 * 8000 / total) - A_KBPS - MUX
    if vcap < 400:
        raise SystemExit(
            f"BITRATE STARVED: {total:.0f}s only leaves {vcap} kbps of video inside "
            f"the 30MB law (need >=400). Shorten the script — do not ship blocking.")
    print(f"video budget: {vcap} kbps ({total:.0f}s, {A_KBPS}k audio)", flush=True)

    size, crf = 0.0, 20
    for crf in (20, 21, 22, 23, 24):
        run([FF, "-y", "-i", f"{S}/video_silent.mp4",
             "-i", f"{S}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
             "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", f"{A_KBPS}k", "-movflags", "+faststart", OUT])
        size = os.path.getsize(OUT) / 1e6
        if size <= 29.5:
            break
        print(f"  {size:.1f} MB at crf {crf} — over, stepping up", flush=True)
    print(f"DONE: {OUT}  {size:.1f} MB, {total:.1f}s (crf {crf}, vcap {vcap}k)",
          flush=True)


if __name__ == "__main__":
    main()
