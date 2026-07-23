#!/usr/bin/env python3
"""Assemble Story Video #93 — Barabbas Goes Free (Mark 15:6-15).

PHASE-1 STILLS-ONLY (Law E): seven painted stills, Ken Burns drift, narration,
serif captions (CAPTION v2 — bottom band only, long lines split and each chunk
timed to what the narrator is saying), cream-italic KJV verses, closing
invitation card with the Gospel Library pointer (MEMBER shelf). NO motion clips.

CONTENT-CARE: the substitution parable — guilty freed, innocent condemned.
No violence shown (Barabbas is a freed killer, but nothing violent is depicted;
the crowd is composed, not a mob spectacle). NO KJV cream-italic — the whole
build is narrator (Pilate trial, no Jesus line), so all captions are white
serif. FACE LAW v3: Jesus face-shown (master-locked, only he wears cream).

n1 gets a sacred hold before the crowd turns. n1 recorded in halves so the
seven beats fill the seven stills per the CAPTION LAW.

NO MUSIC BED of any kind (HUM PURGE law 2026-07-16): narration + silence only.

Linux build (Machine D/ASSEMBLY-D): DejaVu Serif + Italic copied to relative
paths in segs/. Output: mark-15_barabbas-goes-free.mp4,
1080x1920 H.264 30fps, <30MB.
"""
import os
import shutil
import subprocess
import textwrap

import make_narration
from mbm_caption_timing import caption_filter
from mbm_speakers import is_scripture

A = "assets"
S = "segs"
FPS = 30
FF = "ffmpeg"
FPROBE = "ffprobe"
SERIF = "segs/serif.ttf"
SERIF_BI = "segs/serif_bi.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

ST1 = "s1-two-men-before-the-crowd.jpeg"
ST2 = "s2-pilate-weighs-it.jpeg"
ST3 = "s3-the-innocent-one.jpeg"
ST4 = "s4-the-crowd-shouts.jpeg"
ST5 = "s5-chains-struck-off.jpeg"
ST6 = "s6-walking-away-free.jpeg"
ST7 = "s7-the-empty-shackles.jpeg"

TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}
KJV = set()  # narrator-only build (Pilate trial)

# MEMBER shelf: one-line Gospel Library pointer under the closing invitation.
GL_POINTER = "Learn more — Gospel Library: Atonement of Jesus Christ"

BEATS = [
    ("n0", ST1, "in"),
    ("n1a", ST2, "in"),
    ("s9", ST2, "out"),
    ("n1a2", ST2, "in"),
    ("n1b", ST3, "in"),
    ("n2", ST4, "in"),
    ("s13", ST4, "out"),
    ("n2b", ST4, "in"),
    ("s14", ST4, "out"),
    ("n2c", ST4, "in"),
    ("n3", ST5, "in"),
    ("n4", ST6, "in"),
    ("n5", ST7, "in"),
]

LEAD = 0.28
GAP = 0.65
KJV_GAP = 1.60
# Per-beat gap override: n1b = the draft's sacred hold before the crowd turns.
HOLD = {"n1b": 1.60}
# No-dead-air law: the video ends TAIL seconds after the last spoken
# word. Derived, never hand-set. Clears the card's 0.8s fade-out so
# the last word and the fade are never clipped.
TAIL = 1.5


def _ensure_fonts():
    os.makedirs(S, exist_ok=True)
    src = {SERIF: [r"C:\Windows\Fonts\georgia.ttf",
                   "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"],
           SERIF_BI: [r"C:\Windows\Fonts\georgiai.ttf",
                      "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
                      "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"]}
    for dest, cands in src.items():
        if os.path.exists(dest):
            continue
        for c in cands:
            if os.path.exists(c):
                shutil.copyfile(c, dest)
                break
        else:
            raise SystemExit(f"font not found for {dest}; tried {cands}")


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:130], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


def dur_of(path):
    out = subprocess.run(
        [FPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(out.stdout.strip())


def spoken_of(path):
    tmp = f"{S}/_spoken.wav"
    run([FF, "-y", "-v", "error", "-i", path, "-af",
         "areverse,silenceremove=start_periods=1:start_threshold=-50dB:"
         "start_duration=0.02,areverse", "-c:a", "pcm_s16le", tmp])
    return dur_of(tmp)


def sentences(text):
    import re
    return [p for p in re.split(r"(?<=[.!?;:]) +", text) if p]


def chunk_caption(text, width, max_lines):
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
        else:
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


# --- MBM box-guard: strip Unicode line/paragraph separators + control chars that
# drawtext renders as tofu boxes at line ends (Cameron complaint 2026-07-23). ---
_MBM_SEP = {0x2028:0x20,0x2029:0x20,0x0085:0x20,0x000b:0x20,0x000c:0x20,0x000d:0x20}
for _c in list(range(0x00,0x09))+list(range(0x0e,0x20))+list(range(0x7f,0xa0)):
    _MBM_SEP[_c]=None
def _mbm_clean(_t):
    return _t.translate(_MBM_SEP)


def build_card(dur, text):
    tf = f"{S}/card.txt"
    with open(tf, "w", encoding="utf-8") as f:
        f.write("\n".join(textwrap.wrap(_mbm_clean(text), width=30)))
    pf = f"{S}/card_gl.txt"
    with open(pf, "w", encoding="utf-8") as f:
        f.write(GL_POINTER)
    vf = (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize=52:"
          f"fontcolor={INK}:line_spacing=24:x=(w-text_w)/2:y=(h-text_h)/2-70,"
          f"drawtext=fontfile={SERIF_BI}:textfile={pf}:fontsize=34:"
          f"fontcolor={INK}:x=(w-text_w)/2:y=h*0.80,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/card.mp4"])


def main():
    _ensure_fonts()

    spoken = {n: spoken_of(f"audio/{n}.mp3") for n, _, _ in BEATS}
    card_spoken = spoken_of("audio/card.mp3")

    timeline, audio_place, start_of = [], [], {}
    t = 0.0
    for name, still, zdir in BEATS:
        speaker = SPEAKER[name]
        gap = HOLD.get(name, KJV_GAP if is_scripture(speaker) else GAP)
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

    worst, worst_at, prev_end = 0.0, None, None
    for name, _s, _z, _v, a_start, _sp in timeline:
        if prev_end is not None and a_start - prev_end > worst:
            worst, worst_at = a_start - prev_end, name
        prev_end = a_start + spoken[name]
    gap_card = (card_start + LEAD) - prev_end
    worst, worst_at = max(worst, gap_card), (worst_at if worst > gap_card else "card")
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min)", flush=True)
    print(f"worst spoken gap: {worst:.2f}s before {worst_at} (<= 2.5s)", flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s gap before {worst_at}")
    if total < 60.5:
        raise SystemExit(f"TOO SHORT: {total:.1f}s — must run over 60s")
    print(f"sacred hold: n1b at {start_of['n1b']:.1f}s", flush=True)

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

    # Audio = narration + intentional silence ONLY (HUM PURGE law 2026-07-16).
    inputs, filters, labels = [], [], []
    for i, (path, start) in enumerate(audio_place):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(
            f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    m = len(labels)
    filters.append("".join(labels) +
                   f"amix=inputs={m}:duration=longest:normalize=0,"
                   f"apad=whole_dur={total:.2f}[aout]")
    run([FF, "-y"] + inputs + ["-filter_complex", ";".join(filters),
        "-map", "[aout]", "-t", f"{total:.2f}", "-c:a", "aac", "-b:a", "160k",
        f"{S}/audio_mix.m4a"])

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

    OUT = "mark-15_barabbas-goes-free.mp4"
    A_KBPS = 96
    MUX = 20
    vcap = int(24.0 * 8000 / total) - A_KBPS - MUX
    if vcap < 400:
        raise SystemExit(f"BITRATE STARVED: {vcap} kbps < 400 in the 30MB law")
    vcap = min(vcap, 2200)
    print(f"video budget: {vcap} kbps ({total:.0f}s)", flush=True)

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
