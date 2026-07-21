#!/usr/bin/env python3
"""Assemble Story Video #39 — The Pharisee and the Publican (Luke 18:9-14).

PHASE-1 STILLS-ONLY build (Law E): 14 painted stills with slow Ken Burns drift,
narration, serif captions, cream-italic KJV lines, closing question card. NO AI
motion clips.

Stills come from `gen_stills.py` (the official Gemini image API) and live in
assets/<slug>.jpeg — there is no browser and no Google Flow in this pipeline.

CAPTIONS ARE VERBATIM: every caption is the exact spoken text of its narration
segment (imported from make_narration.SEGMENTS and word-wrapped). KJV (Jesus)
lines render in cream italic.

Face-never (the #1 Law): Jesus appears in exactly two stills (s1, s9), both with
the camera directly behind him — the back of his head to us, face never rendered.
Verses 10-13 are the parable he is TELLING, so no divine figure appears in any of
the parable stills; the Pharisee, the publican and the crowd are ordinary people
with faces fully shown.

TWO SACRED SILENCES (the music bed dies to true silence for both):
  j2  "God be merciful to me a sinner."          — the seven words
  j3  "...went down to his house justified..."   — the verdict (Luke 18:14,
                                                   the verse-card line)
A warm bed swells back under n9 to carry us toward the verdict, then dies again
before j3 lands. No-Dead-Air is unaffected — the narrator never stops; only the
music does.

Timing is COMPUTED from measured mp3 durations (no hand offsets to drift).

Output: luke-18_pharisee-and-publican.mp4 (SCRIPTURE-NAME LAW),
1080x1920 H.264 30fps, <25MB.
"""
import os
import subprocess
import textwrap

import make_narration  # SEGMENTS -> verbatim caption text per segment
from mbm_caption_timing import caption_filter
from mbm_speakers import is_scripture

A = "assets"         # gen_stills.py writes <slug>.jpeg here
S = "segs"
FPS = 30
FF = "ffmpeg"
FPROBE = "ffprobe"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-the-certain-men.jpeg"
S2 = "s2-two-men-go-up.jpeg"
S3 = "s3-the-good-man.jpeg"
S4 = "s4-the-hated-man.jpeg"
S5 = "s5-pharisee-prays.jpeg"
S5B = "s5b-the-list.jpeg"
S6 = "s6-afar-off.jpeg"
S7 = "s7-be-merciful.jpeg"
S7B = "s7b-the-lamb.jpeg"
S8 = "s8-two-prayers.jpeg"
S9 = "s9-the-verdict.jpeg"
S10 = "s10-went-down-justified.jpeg"
S11 = "s11-still-standing.jpeg"
S12 = "s12-the-open-gate.jpeg"

# Caption text = verbatim spoken text, keyed by segment name.
TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}

# BEATS: (segment_name, still, zoom_dir). One still-drift beat per narration
# segment; every word of that segment is captioned on it. Zoom alternates so a
# still visited twice in a row never repeats the same move.
BEATS = [
    ("s9", S1, "in"),
    ("n1", S1, "out"),
    ("jv10", S2, "in"),
    ("n2", S2, "out"),
    ("n3", S3, "in"),
    ("n4", S4, "in"),
    ("n5", S5, "in"),
    ("j1", S5, "out"),
    ("n6", S5B, "in"),
    ("jv13a", S6, "in"),
    ("n7", S6, "out"),
    ("j2", S7, "in"),
    ("n8a", S7B, "in"),
    ("n8b", S8, "in"),
    ("n9", S8, "out"),
    ("j3", S9, "in"),
    ("n10", S9, "out"),
    ("n11", S10, "in"),
    ("n12", S11, "in"),
    ("n13", S12, "in"),
]

LEAD = 0.28          # audio starts this long after its beat begins
GAP = 0.72           # trailing pad after SPOKEN content on a normal beat
KJV_GAP = 1.75       # a longer, reverent pad after a Jesus line
# No-dead-air law: the video ends TAIL seconds after the last spoken
# word. Derived, never hand-set. Clears the card's 0.8s fade-out so
# the last word and the fade are never clipped.
TAIL = 1.5

# Every beat is timed from the SPOKEN end of its mp3, never the file end.
# The TTS files carry a silent tail — ~0.45s on the narrator, ~1.3s on the Jesus
# voice — and timing off the file end silently ADDS that tail to every pause. On
# the first cut of this video that pushed the pauses after j2 and j3 to 2.76s and
# 2.73s, breaking the No-Dead-Air law (>2.5s). This is the same defect the
# PRODUCTION-BIBLE records from video #2. Measured spoken length + explicit gap =
# the gap you actually hear.


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


def wrapped(name):
    return "\n".join(textwrap.wrap(TEXT[name], width=34))


def _cap_chunks(text, width, max_lines):
    words = text.split()
    chunks, cur = [], ""
    for w in words:
        cand = (cur + " " + w).strip()
        if len(textwrap.wrap(cand, width)) <= max_lines:
            cur = cand
        else:
            chunks.append(cur)
            cur = w
    if cur:
        chunks.append(cur)
    return chunks


def build_still(seg_id, src, dur, zdir, cap_text, speaker, first):
    # ANTI-SHIMMER: the drift is rendered supersampled (2160 wide) and lanczos'd
    # down to 1080, so zoompan's whole-pixel crop stepping lands on quarter-pixels
    # instead of showing as slideshow jitter.
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.09*on/{frames}"
    else:
        z = f"1.091-0.09*on/{frames}"
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    cap = caption_filter(seg_id, dur, dur, cap_text, speaker)
    tail = ",fade=t=in:st=0:d=1.0" if first else ""
    fc = f"{base}{cap}{tail}[v]"
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(dur, text):
    # per-line card (2026-07-17, #7 end-card tofu fix): this box renders a
    # textfile newline as a tofu box, so each wrapped card line gets its own
    # textfile + drawtext, block-centered. Visuals/audio unchanged.
    _clines = textwrap.wrap(text, width=30)
    _clh = 52 + 24
    _cL = len(_clines)
    _cdt = ""
    for _cj, _cln in enumerate(_clines):
        _ctf = f"{S}/card_{_cj}.txt"
        with open(_ctf, "w", encoding="utf-8") as _cf:
            _cf.write(_cln)
        _cy = f"(h-{_cL * _clh})/2+{_cj * _clh}"
        _cdt += (f"drawtext=fontfile={SERIF}:textfile={_ctf}:"
                 f"fontsize=52:fontcolor={INK}:x=(w-text_w)/2:y={_cy},")
    vf = _cdt + f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8"
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/card.mp4"])


def bed_filter(idx, start, end, style):
    # No bare sine waves: every voice is a slightly detuned PAIR (natural slow
    # beating) through a soft room echo.
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
    os.makedirs(S, exist_ok=True)

    # ---- compute the timeline from MEASURED audio (never estimates) ----
    # The mp3 still plays in full; its silent tail simply overlaps the next beat's
    # lead-in, which is harmless. Only the TIMING is driven by the spoken end.
    spoken = {n: spoken_of(f"audio/{n}.mp3") for n, _, _ in BEATS}
    card_spoken = spoken_of("audio/card.mp3")

    timeline = []     # (seg_id, still, zoom, video_dur, audio_start, speaker)
    audio_place = []  # (mp3, start)
    start_of = {}     # seg_id -> audio start, for scheduling the music beds
    t = 0.0
    for name, still, zdir in BEATS:
        speaker = SPEAKER[name]
        gap = KJV_GAP if is_scripture(speaker) else GAP
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

    # ---- on-paper silence map: prove no spoken gap exceeds 2.5s BEFORE mixing --
    worst = 0.0
    prev_end = None
    for name, _s, _z, _v, a_start, _sp in timeline:
        if prev_end is not None:
            worst = max(worst, a_start - prev_end)
        prev_end = a_start + spoken[name]
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min)", flush=True)
    print(f"worst spoken gap: {worst:.2f}s (No-Dead-Air law: must be <= 2.5s)",
          flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s gap exceeds the 2.5s law")
    print(f"sacred silence 1: j2 at {start_of['j2']:.1f}s", flush=True)
    print(f"sacred silence 2: j3 at {start_of['j3']:.1f}s", flush=True)

    # ---- render every still beat ----
    for i, (seg_id, still, zdir, vdur, _a, speaker) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, wrapped(seg_id), speaker,
                    first=(i == 0))
    build_card(card_vdur, TEXT["card"])

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at computed offsets + warm beds around two silences --
    j2_end = start_of["j2"] + spoken["j2"]
    j3_end = start_of["j3"] + spoken["j3"]
    beds = [
        # opens the story, out before the seven words
        (0.0, start_of["j2"] - 1.2, "b"),
        # swells back under n9 and dies again before the verdict
        (start_of["n9"] - 0.5, start_of["j3"] - 1.0, "a"),
        # returns after the verdict, gone before the closing card
        (j3_end + 1.0, card_start - 0.8, "a"),
    ]
    print(f"music: bed out {start_of['j2'] - 1.2:.1f}s, silent through j2 "
          f"(ends {j2_end:.1f}s) and n8a/n8b; returns under n9; silent again "
          f"through j3 (ends {j3_end:.1f}s)", flush=True)

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

    # ---- loudness toward -15 LUFS (quiet audio reads as amateur) ----
    probe = subprocess.run(
        [FF, "-i", f"{S}/audio_mix.m4a", "-af", "ebur128", "-f", "null", "-"],
        capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            lufs = float(line.split()[1])
    gain = max(-6.0, min(10.0, -15.0 - lufs)) if lufs is not None else 0.0
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    # ---- final mux: the ONLY lossy generation. Never starve the bitrate. ----
    OUT = "luke-18_pharisee-and-publican.mp4"
    vcap = max(500, int(24.3 * 8000 / total) - 130)
    size, crf = 0.0, 20
    for crf in (20, 21, 22, 23, 24):
        run([FF, "-y", "-i", f"{S}/video_silent.mp4",
             "-i", f"{S}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
             "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", OUT])
        size = os.path.getsize(OUT) / 1e6
        if size <= 24.3:
            break
        print(f"  {size:.1f} MB at crf {crf} — over, stepping up", flush=True)
    print(f"DONE: {OUT}  {size:.1f} MB, {total:.1f}s (crf {crf}, vcap {vcap}k)",
          flush=True)


if __name__ == "__main__":
    main()
