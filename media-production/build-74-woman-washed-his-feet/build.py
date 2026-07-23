#!/usr/bin/env python3
"""Assemble Story Video #74 — The Woman Who Washed His Feet (Luke 7:36-50).

PHASE-1 STILLS-ONLY, face-shown Jesus locked to the master ref (FACE LAW v3).
Caption-v2 (wide bottom band, chunked and synced to the narration — CAPTION LAW).
Two-voice: narrator en-US-AndrewNeural, KJV en-US-ChristopherNeural
(Luke 7:47, 7:48, 7:50 — exact KJV). "tears" SPOKEN-respelled (homograph law).
NO music bed of any kind (HUM PURGE 2026-07-16): narration + intentional silence only.
CONTENT-CARE: her reputation named once in plain words, never depicted; no shame
framing; mercy spoken out loud in the KJV lines.

SPLIT BEAT: n2 (weeping / hair / pouring) plays over THREE stills — s3, s4, s5 —
cut at caption-chunk boundaries so the caption always matches what is being said.
j1 (to Simon) sits on s7-out; j2 on s8 (the [SILENCE] shot); j3 on s8-out, then a
short SILENT HUSH on s9 (the empty jar, the open door to the night) breathes before
the closing card — the hush stays inside the 2.5s dead-air law.

Caption box black@0.55 — warm lamplit interiors, verified on the lightest frame.

Output: luke-7_woman-washed-his-feet.mp4, 1080x1920 H.264 30fps, <30MB.
"""
import os
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
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"
BOX_ALPHA = "0.55"   # warm lamplit interiors — verify on the lightest frame

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-dinner-at-simons.jpeg"
S2 = "s2-the-doorway.jpeg"
S3 = "s3-at-his-feet.jpeg"
S4 = "s4-hair-and-tears.jpeg"
S5 = "s5-the-pouring.jpeg"
S6 = "s6-simons-face.jpeg"
S7 = "s7-two-debtors.jpeg"
S8 = "s8-thy-sins-are-forgiven.jpeg"
S9 = "s9-go-in-peace.jpeg"

TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}
CARD_TEXT = TEXT["card"]

# (audio_name, [(still, zdir), ...], gap_override) — more than one still = split
# beat: the audio plays once, the picture cuts at caption-chunk boundaries.
# name "HUSH" = a short SILENT still (no audio, no caption); its gap field is its
# full duration — kept short enough that the dead-air law still holds.
BEATS = [
    ("n0", [(S1, "in")], None),
    ("n1", [(S2, "in")], None),
    ("n2", [(S3, "in"), (S4, "in"), (S5, "in")], 1.5),
    ("s39", [(S6, "in")], None),
    ("n3", [(S6, "in")], None),
    ("j40", [(S7, "in")], None),
    ("s40", [(S7, "in")], None),
    ("j41", [(S7, "in")], None),
    ("s43", [(S7, "in")], None),
    ("n4", [(S7, "in")], None),
    ("j44", [(S3, "out")], None),
    ("n5", [(S3, "out")], None),
    ("j1", [(S7, "out")], None),
    ("n5b", [(S7, "out")], None),
    ("j2", [(S8, "in")], None),
    ("s49", [(S1, "out")], None),
    ("n6", [(S1, "out")], None),
    ("j3", [(S8, "out")], 0.4),
    ("HUSH", [(S9, "in")], 1.6),
]

LEAD = 0.28
GAP = 0.72
KJV_GAP = 1.50
# No-dead-air law: the video ends TAIL seconds after the last spoken
# word. Derived, never hand-set. Clears the card's 0.8s fade-out so
# the last word and the fade are never clipped.
TAIL = 1.5


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


def split_long(s, width, max_lines):
    """Split one over-long sentence on its natural seams (', ' and ' — '),
    keeping every character verbatim — the caption shows the exact spoken words."""
    import re
    parts = [p for p in re.split(r"(?<=, )|(?<= — )", s) if p]
    out, acc = [], ""
    for p in parts:
        cand = acc + p
        if len(textwrap.wrap(cand, width)) <= max_lines:
            acc = cand
        else:
            if acc.strip():
                out.append(acc.strip())
            acc = p
    if acc.strip():
        out.append(acc.strip())
    return out


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
            pieces = split_long(s, width, max_lines)
            out.extend(pieces[:-1])
            cur = pieces[-1]
    if cur:
        out.append(cur)
    return out


def timed_chunks(text, spoken_end, dur, scripture):
    """CAPTION LAW v2: chunk the caption and time each chunk proportionally
    across the spoken audio, so the words on screen match the words being said."""
    if scripture:
        width, maxl = 38, 3
    else:
        width, maxl = 48, 2
    chunks = chunk_caption(text, width, maxl)
    total = sum(len(c) for c in chunks) or 1
    t0, t1 = 0.15, max(0.6, min(dur - 0.2, spoken_end + 0.35))
    out, acc = [], 0
    for c in chunks:
        cs = t0 + (t1 - t0) * acc / total
        acc += len(c)
        ce = t0 + (t1 - t0) * acc / total
        out.append((c, cs, ce))
    return out


def caption_filters(seg_id, dur, chunks, scripture):
    if scripture:
        font, size, color, width = SERIF_BI, 46, "0xFFF3DC", 38
    else:
        font, size, color, width = SERIF, 34, "white", 48
    filters, labels = [], []
    for i, (c, cs, ce) in enumerate(chunks):
        tf = f"{S}/{seg_id}_{i}.txt"
        with open(tf, "w") as f:
            f.write("\n".join(textwrap.wrap(c, width)))
        fo = max(cs, ce - 0.35)
        filters.append(
            f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile={font}:textfile={tf}:fontsize={size}:"
            f"fontcolor={color}:line_spacing=13:x=(w-text_w)/2:"
            f"y=h-120-text_h:"
            f"shadowcolor=black@0.9:shadowx=2:shadowy=2:"
            f"box=1:boxcolor=black@{BOX_ALPHA}:boxborderw=22,"
            f"fade=t=in:st={cs:.2f}:d=0.35:alpha=1,"
            f"fade=t=out:st={fo:.2f}:d=0.35:alpha=1[cap{seg_id}{i}]")
        labels.append(f"[cap{seg_id}{i}]")
    return filters, labels


def build_still(seg_id, src, dur, zdir, chunks, speaker, first):
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.09*on/{frames}"
    else:
        z = f"1.091-0.09*on/{frames}"
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ",fade=t=in:st=0:d=1.0" if first else ""
    _cap_txt = " ".join(
        (c[0] if isinstance(c, (list, tuple)) else c) for c in chunks
    ) if isinstance(chunks, (list, tuple)) else (chunks or "")
    _cap_txt = " ".join(_cap_txt.split())
    capf = caption_filter(seg_id, dur, dur, _cap_txt, speaker) if _cap_txt else ""
    fc = f"{base}{capf}{tail}[v]"
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
    with open(tf, "w") as f:
        f.write("\n".join(textwrap.wrap(_mbm_clean(text), width=30)))
    vf = (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize=50:"
          f"fontcolor={INK}:line_spacing=24:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/card.mp4"])


def main():
    os.makedirs(S, exist_ok=True)

    names = [b[0] for b in BEATS if b[0] != "HUSH"]
    spoken = {n: spoken_of(f"audio/{n}.mp3") for n in names}
    card_spoken = spoken_of("audio/card.mp3")

    # Timeline: each beat may be one or more video segments; audio plays once.
    segments = []          # (seg_id, still, zdir, dur, chunks, speaker, first)
    audio_place = []
    t = 0.0
    start_of = {}
    for bi, (name, stills, gap_over) in enumerate(BEATS):
        if name == "HUSH":
            still, zdir = stills[0]
            segments.append((f"hush{bi}", still, zdir, gap_over, [], False, False))
            t += gap_over
            continue
        speaker = SPEAKER[name]
        gap = gap_over if gap_over is not None else (KJV_GAP if is_scripture(speaker) else GAP)
        vdur = LEAD + spoken[name] + gap
        spoken_end = LEAD + spoken[name]
        a_start = t + LEAD
        audio_place.append((f"audio/{name}.mp3", a_start))
        start_of[name] = a_start
        chunks = timed_chunks(TEXT[name], spoken_end, vdur, is_scripture(speaker))
        if len(stills) == 1:
            still, zdir = stills[0]
            segments.append((name, still, zdir, vdur, chunks, speaker, bi == 0))
        else:
            # Split beat: cut at caption-chunk boundaries nearest the even split
            # points, so no caption straddles a picture cut.
            n = len(stills)
            if len(chunks) < n:
                raise SystemExit(f"split beat {name}: {len(chunks)} chunks < "
                                 f"{n} stills")
            cuts, prev = [], 0.0
            for k in range(1, n):
                target = vdur * k / n
                cands = [c[2] for c in chunks[:-1] if c[2] > prev + 0.2]
                if not cands:
                    raise SystemExit(f"split beat {name}: no cut candidate {k}")
                tcut = min(cands, key=lambda b: abs(b - target))
                cuts.append(tcut)
                prev = tcut
            edges = [0.0] + cuts + [vdur]
            for si, (still, zdir) in enumerate(stills):
                lo, hi = edges[si], edges[si + 1]
                sub = [(c, cs - lo, ce - lo) for (c, cs, ce) in chunks
                       if cs >= lo - 1e-6 and ce <= hi + 1e-6]
                segments.append((f"{name}{chr(97+si)}", still, zdir, hi - lo,
                                 sub, speaker, bi == 0 and si == 0))
            print(f"split {name}: cuts at {[f'{c:.2f}' for c in cuts]} of "
                  f"{vdur:.2f}s", flush=True)
        t += vdur
    card_vdur = LEAD + card_spoken + TAIL
    card_start = t
    audio_place.append(("audio/card.mp3", card_start + LEAD))
    total = t + card_vdur

    # No-Dead-Air Law: enforce in code, timed off the SPOKEN end —
    # including across HUSH beats and into the card.
    worst, worst_at, prev_end = 0.0, None, None
    for name in names:
        a_start = start_of[name]
        if prev_end is not None and a_start - prev_end > worst:
            worst, worst_at = a_start - prev_end, name
        prev_end = a_start + spoken[name]
    card_gap = (card_start + LEAD) - prev_end
    if card_gap > worst:
        worst, worst_at = card_gap, "card"
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min)", flush=True)
    print(f"worst spoken gap: {worst:.2f}s before {worst_at}", flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s before {worst_at}")
    if total < 60:
        raise SystemExit(f"TOO SHORT: {total:.1f}s (< 60s law)")
    for j in ("j1", "j2", "j3"):
        print(f"sacred silence after {j} at "
              f"{start_of[j]+spoken[j]:.1f}s", flush=True)

    for seg_id, still, zdir, dur, chunks, speaker, first in segments:
        build_still(seg_id, still, dur, zdir, chunks, speaker, first)
    build_card(card_vdur, CARD_TEXT)

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in segments:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # HUM PURGE (Cameron, 2026-07-16): NO synthetic music bed, ever.
    # Audio is NARRATION + INTENTIONAL SILENCE only.
    inputs, filters, labels = [], [], []
    for i, (path, start) in enumerate(audio_place):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
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

    OUT = "luke-7_woman-washed-his-feet.mp4"
    A_KBPS, MUX = 96, 20
    vcap = int(24.0 * 8000 / total) - A_KBPS - MUX
    if vcap < 400:
        raise SystemExit(f"BITRATE STARVED at 25MB: {vcap} kbps for {total:.0f}s")
    vcap = min(vcap, 2200)
    print(f"video budget: {vcap} kbps ({total:.0f}s, 25MB cap)", flush=True)

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
