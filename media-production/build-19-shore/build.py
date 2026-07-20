#!/usr/bin/env python3
"""Assemble Story Video #19 — Breakfast on the Shore: Peter Restored
(John 21:1-17).

PHASE-1 STILLS-ONLY build (Law E): 7 painted 2K stills with slow Ken Burns
drift, narration, serif captions, KJV red-letter lines, closing card. NO motion
clips.

CAPTIONS ARE VERBATIM: every caption is the exact spoken text of its narration
segment (imported from make_narration.SEGMENTS and word-wrapped) — every word
spoken is on the screen. KJV (Jesus) lines render in cream italic.

Face-never (#18): the Lord is only ever shown from behind, hand-only (the hand
on Peter's shoulder), or at dawn distance — never his face. The charcoal fire is
the emotional key: the same kind of fire Peter denied him beside.

Timing is COMPUTED from the measured mp3 durations (no hand offsets to drift).
Music: a warm detuned-pair bed opens and fades to FULL SILENCE just before j1
("Simon, son of Jonas, lovest thou me?" — the peak), so the question lands in
true silence; a warm bed returns after and is out before the closing card.

Output: john-21_shore.mp4 (SCRIPTURE-NAME LAW), 1080x1920 H.264 30fps, <25MB.
"""
import os
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
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-denial.jpeg"
S2 = "s2-empty-net.jpeg"
S3 = "s3-figure-shore.jpeg"  # RETIRED from the timeline (STORY-COVERAGE-LAW)
S4 = "s4-charcoal-fire.jpeg"
S5 = "s5-do-you-love-me.jpeg"
S6 = "s6-feed-my-sheep.jpeg"
S7 = "s7-breaks-bread.jpeg"
# STORY-COVERAGE retrofit (Cameron, 2026-07-19): the dawn drama gets one still
# per beat instead of one still for seven beats.
S8 = "s8-call-shore.jpeg"
S9 = "s9-answer-nothing.jpeg"
S10 = "s10-cast-right.jpeg"
S11 = "s11-net-full.jpeg"
S12 = "s12-realization.jpeg"
S13 = "s13-peter-leap.jpeg"
S14 = "s14-swim.jpeg"
S15 = "s15-fire-close.jpeg"
S16 = "s16-breakfast.jpeg"

# Caption text = verbatim spoken text, keyed by segment name.
TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}
# SPEAKER-LAW: declared once in make_narration, so the caption colour
# and the narration voice can never drift apart.
SPEAKER = {s[0]: s[1] for s in make_narration.SEGMENTS}

# BEATS: (segment_name, still, zoom_dir). One still per story BEAT
# (STORY-COVERAGE-LAW, Cameron 2026-07-19). A still may be a LIST of
# (image, marker) pairs — the picture switches mid-segment at the timestamp
# where the marker words are spoken (matched against the TTS sentence timing):
# n5c: the cast flies (S10) -> "and it came up so full" (S11, the net FULL).
# n6:  "It is the Lord" realization (S12) -> "And Peter did not wait" (S13,
#      the leap) -> "and swam for shore" (S14, the swim, boat following).
BEATS = [
    ("n1", S1, "in"),
    ("n2", S1, "out"),
    ("n3", S2, "in"),
    ("n4", S2, "out"),
    ("n5", S8, "in"),
    ("j0a", S8, "out"),
    ("n5b", S9, "in"),
    ("j0b", S8, "in"),
    ("n5c", [(S10, None), (S11, "and it came up so full")], "in"),
    ("n6", [(S12, None), (S13, "And Peter did not wait"),
            (S14, "and swam for shore")], "in"),
    ("n7", S4, "in"),
    ("n8", S15, "in"),
    ("n9", S16, "in"),
    ("n10", S5, "in"),
    ("j1", S5, "out"),
    ("n11", S5, "in"),
    ("s16", S6, "in"),
    ("n12", S6, "out"),
    ("j2", S6, "in"),
    ("n13", S6, "out"),
    ("n14", S7, "in"),
]

LEAD = 0.28          # audio starts this long after its beat begins
GAP = 0.72           # trailing pad after spoken content on a normal beat
KJV_GAP = 1.15       # a longer, reverent pad around the Jesus lines
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


def wrapped(name):
    return "\n".join(textwrap.wrap(TEXT[name], width=34))


def marker_time(seg_id, marker):
    """Segment-local second at which the marker words are spoken, from the
    edge-tts sentence timing sidecar (STORY-COVERAGE-LAW mid-segment switch)."""
    import json
    import re
    with open(f"audio/{seg_id}.timing.json") as f:
        timing = json.load(f)

    def norm(x):
        return re.sub(r"[^a-z0-9 ]", "", x.lower()).strip()

    mk = norm(marker)
    for s in timing:
        nt = norm(s["text"])
        i = nt.find(mk)
        if i >= 0:
            return s["start"] + (s["end"] - s["start"]) * (i / max(1, len(nt)))
    raise SystemExit(f"STORY-COVERAGE: marker {marker!r} not found in {seg_id}.timing.json")


def _zoompan(zd, frames):
    if zd == "in":
        z = f"1.001+0.09*on/{frames}"
    else:
        z = f"1.091-0.09*on/{frames}"
    return (f"scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")


def build_still(seg_id, src, dur, zdir, cap_text, speaker, first, last):
    cap = caption_filter(seg_id, dur, dur, cap_text, speaker)
    tail = ",fade=t=in:st=0:d=1.0" if first else ""
    if not isinstance(src, list):
        fc = f"[0:v]{_zoompan(zdir, int(dur * FPS))}{cap}{tail}[v]"
        run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
             "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])
        return
    # STORY-COVERAGE-LAW: several stills inside one narration segment, switching
    # at the timestamps where the words turn. Render each sub-still, concat,
    # then draw the segment's captions over the joined clip.
    cuts = [0.0] + [LEAD + marker_time(seg_id, m) for _s, m in src[1:]] + [dur]
    subs = []
    for i, (img, _m) in enumerate(src):
        d = cuts[i + 1] - cuts[i]
        if d <= 0:
            raise SystemExit(f"STORY-COVERAGE: switch times out of order in {seg_id}")
        zd = zdir if i % 2 == 0 else ("out" if zdir == "in" else "in")
        out = f"{S}/{seg_id}_p{i}.mp4"
        run([FF, "-y", "-loop", "1", "-i", f"{A}/{img}", "-t", f"{d:.3f}",
             "-filter_complex", f"[0:v]{_zoompan(zd, max(1, int(d * FPS)))}[v]",
             "-map", "[v]"] + ENC + [out])
        subs.append(out)
    lst = f"{S}/{seg_id}_parts.txt"
    with open(lst, "w") as f:
        for p in subs:
            f.write(f"file '{os.path.basename(p)}'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", lst,
         "-filter_complex", f"[0:v]null{cap}{tail}[v]",
         "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(dur, text):
    tf = f"{S}/card.txt"
    with open(tf, "w") as f:
        f.write("\n".join(textwrap.wrap(text, width=30)))
    vf = (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize=52:"
          f"fontcolor={INK}:line_spacing=24:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{S}/card.mp4"])


def bed_filter(idx, start, end, style):
    d = end - start
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

    # ---- compute the timeline from measured audio ----
    audio_dur = {n: dur_of(f"audio/{n}.mp3") for n, _, _ in BEATS}
    card_dur = dur_of("audio/card.mp3")

    timeline = []   # (seg_id, still, zoom, video_dur, audio_start, speaker)
    t = 0.0
    audio_place = []  # (mp3, start)
    j1_start = None
    for name, still, zdir in BEATS:
        speaker = SPEAKER[name]
        gap = KJV_GAP if is_scripture(speaker) else GAP
        vdur = LEAD + audio_dur[name] + gap
        a_start = t + LEAD
        audio_place.append((f"audio/{name}.mp3", a_start))
        if name == "j1":
            j1_start = a_start
        timeline.append((name, still, zdir, vdur, a_start, speaker))
        t += vdur
    # closing card
    card_vdur = LEAD + card_dur + TAIL
    card_start = t
    audio_place.append(("audio/card.mp3", card_start + LEAD))
    total = t + card_vdur

    print(f"total runtime: {total:.1f}s ({total/60:.2f} min); "
          f"j1 (peak silence) at {j1_start:.1f}s", flush=True)

    # ---- render every still beat ----
    n = len(timeline)
    for i, (seg_id, still, zdir, vdur, _a, speaker) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, wrapped(seg_id), speaker,
                    first=(i == 0), last=(i == n - 1))
    build_card(card_vdur, TEXT["card"])

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at computed offsets + warm beds (silence at j1) ----
    beds = [
        (0.0, j1_start - 1.2, "b"),          # out just before j1 (the question)
        (j1_start + audio_dur["j1"] + 1.0, total - 10.0, "a"),  # returns after
    ]
    inputs, filters, labels = [], [], []
    for i, (path, start) in enumerate(audio_place):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(
            f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    bi = 0
    for (bs, be, st) in beds:
        filters.append(bed_filter(bi, bs, be, st))
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
    gain = max(-6.0, min(10.0, -15.0 - lufs)) if lufs is not None else 0.0
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    # ---- final mux: slow, runtime-computed rate cap, crf step-up ----
    OUT = "john-21_shore.mp4"
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
