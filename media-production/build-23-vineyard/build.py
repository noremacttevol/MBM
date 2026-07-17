#!/usr/bin/env python3
"""Assemble Story Video #23 — The Workers in the Vineyard (Matthew 20:1-16).

PHASE-1 STILLS-ONLY build (Law E): 8 painted 2K stills with slow Ken Burns
drift, narration, serif captions, KJV red-letter lines, closing card. NO motion
clips. Parable Jesus tells — NO Jesus figure on screen (voice + KJV only); every
character in the story is shown fully. Face gate trivially safe.

CAPTIONS ARE VERBATIM: every caption is the exact spoken text of its narration
segment (imported from make_narration.SEGMENTS and word-wrapped). KJV (Jesus)
lines render in cream italic.

Timing is COMPUTED from measured mp3 durations (no hand offsets to drift).
Music: a warm detuned-pair bed opens and fades to FULL SILENCE just before j1
(the householder's reply ending "Is thine eye evil, because I am good?" — the
heart of the parable), so that key question lands in true silence; a warm bed
returns under the explanation (n13), then fades out before j2 so the conclusion
("So the last shall be first...") and the close play in reverent quiet.

Output: matthew-20_vineyard-workers.mp4 (SCRIPTURE-NAME LAW), 1080x1920 H.264
30fps, <25MB.
"""
import os
import subprocess
import textwrap

import make_narration  # SEGMENTS -> verbatim caption text per segment

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

S1 = "s1-dawn-hire.jpeg"
S2 = "s2-marketplace-idle.jpeg"
S3 = "s3-eleventh-hour.jpeg"
S4 = "s4-evening-pay.jpeg"
S5 = "s5-last-paid.jpeg"
S6 = "s6-first-murmur.jpeg"
S7 = "s7-friend-reply.jpeg"
S8 = "s8-vineyard-dusk.jpeg"

# Caption text = verbatim spoken text, keyed by segment name.
TEXT = {s[0]: s[4] for s in make_narration.SEGMENTS}
KJV = {"j1", "j2"}   # Matthew 20:13-15 (j1), 20:16 (j2) — Jesus voice
PEAK = {"j1"}        # "Is thine eye evil, because I am good?" — silence lands here

# BEATS: (segment_name, still, zoom_dir). One still-drift beat per narration
# segment; every word of that segment is captioned on it. Zoom alternates.
BEATS = [
    ("n1", S1, "in"), ("n2", S1, "out"),
    ("n3", S2, "in"), ("n4", S2, "out"),
    ("n5", S3, "in"), ("n6", S3, "out"),
    ("n7", S4, "in"),
    ("n8", S5, "in"),
    ("n9", S6, "in"), ("n10", S6, "out"),
    ("n11", S7, "in"), ("j1", S7, "out"), ("n12", S7, "in"),
    ("n13", S8, "in"), ("j2", S8, "out"), ("n14", S8, "in"),
]

LEAD = 0.28          # audio starts this long after its beat begins
GAP = 0.72           # trailing pad after spoken content on a normal beat
KJV_GAP = 1.15       # a longer, reverent pad around the Jesus / peak lines
CARD_HOLD = 4.2      # extra seconds the card is held after it is read


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


def caption_overlay(seg_id, dur, text, kjv):
    # CAPTION LAW (Cameron, 2026-07-17): a caption may occupy only the bottom
    # band of the frame — narrator <=2 lines, KJV <=3 lines per chunk; a longer
    # segment is SPLIT into chunks shown in sync with the narration (each chunk
    # holds for its share of the spoken time). Never shrink the font to cram.
    # One drawtext per LINE: this box's ffmpeg draws a textfile newline as a
    # tofu box, so a newline never enters a textfile.
    text = " ".join(text.split())
    if kjv:
        font, size, color, width, maxl = SERIF_BI, 46, "0xFFF3DC", 38, 3
    else:
        font, size, color, width, maxl = SERIF, 34, "white", 48, 2
    lh = int(size * 1.34)
    gap = KJV_GAP if kjv else GAP
    chunks = _cap_chunks(text, width, maxl)
    total = sum(len(c) for c in chunks) or 1
    t0 = 0.15
    t1 = max(t0 + 0.4, min(dur - 0.2, (dur - gap) + 0.35))
    chain = f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba"
    acc = 0
    for i, c in enumerate(chunks):
        cs = t0 + (t1 - t0) * acc / total
        acc += len(c)
        ce = t0 + (t1 - t0) * acc / total
        lines = textwrap.wrap(c, width)
        L = len(lines)
        for j, ln in enumerate(lines):
            tf = f"{S}/{seg_id}_c{i}_{j}.txt"
            with open(tf, "w", encoding="utf-8") as f:
                f.write(ln)
            y = f"h-120-text_h-{(L - 1 - j) * lh}"
            chain += (
                f",drawtext=fontfile='{font}':textfile='{tf}':fontsize={size}:"
                f"fontcolor={color}:x=(w-text_w)/2:y={y}:"
                f"shadowcolor=black@0.9:shadowx=2:shadowy=2:"
                f"box=1:boxcolor=black@0.58:boxborderw=22:"
                f"enable='between(t,{cs:.2f},{ce:.2f})'"
            )
    return chain + "[cap]"


def build_still(seg_id, src, dur, zdir, cap_text, kjv, first, last):
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.09*on/{frames}"
    else:
        z = f"1.091-0.09*on/{frames}"
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    capf = caption_overlay(seg_id, dur, cap_text, kjv)
    tail = ""
    if first:
        tail = ",fade=t=in:st=0:d=1.0"
    fc = f"{base}[b];{capf};[b][cap]overlay=format=auto{tail}[v]"
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


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

    timeline = []   # (seg_id, still, zoom, video_dur, audio_start, kjv)
    t = 0.0
    audio_place = []  # (mp3, start)
    peak_start = None
    n13_start = None
    j2_start = None
    for name, still, zdir in BEATS:
        reverent = name in KJV or name in PEAK
        gap = KJV_GAP if reverent else GAP
        vdur = LEAD + audio_dur[name] + gap
        a_start = t + LEAD
        audio_place.append((f"audio/{name}.mp3", a_start))
        if name == "j1":
            peak_start = a_start
        if name == "n13":
            n13_start = a_start
        if name == "j2":
            j2_start = a_start
        timeline.append((name, still, zdir, vdur, a_start, name in KJV))
        t += vdur
    # closing card
    card_vdur = LEAD + card_dur + CARD_HOLD
    card_start = t
    audio_place.append(("audio/card.mp3", card_start + LEAD))
    total = t + card_vdur

    print(f"total runtime: {total:.1f}s ({total/60:.2f} min); "
          f"peak (key question — silence) at {peak_start:.1f}s; "
          f"j2 (quiet conclusion) at {j2_start:.1f}s", flush=True)

    # ---- render every still beat ----
    n = len(timeline)
    for i, (seg_id, still, zdir, vdur, _a, kjv) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, wrapped(seg_id), kjv,
                    first=(i == 0), last=(i == n - 1))
    build_card(card_vdur, TEXT["card"])

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at computed offsets + warm beds ----
    #   bed a : opening -> fades out just before the key question (j1), so the
    #           reply ending "Is thine eye evil, because I am good?" lands in a
    #           reverent hush.
    #   bed b : returns just after j1 and runs warm UNDER everything that follows
    #           (n12, n13, j2 "the last shall be first", n10), fading out only
    #           before the closing card. No-Dead-Air: the only silences >2.5s are
    #           the hush around the key question and the card's tail.
    beds = [
        (0.0, peak_start - 1.2, "a"),
        (peak_start + audio_dur["j1"] + 1.0, card_start - 0.8, "b"),
    ]
    _ = (n13_start, j2_start)  # (kept for the timeline print above)
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
    OUT = "matthew-20_vineyard-workers.mp4"
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
