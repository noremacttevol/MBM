#!/usr/bin/env python3
"""Assemble Story Video #124 — Gethsemane (Luke 22:39-46; Matthew 26:36-46).

PHASE-1 STILLS-ONLY build (Law E): twelve painted stills with slow Ken Burns drift,
narration, serif captions, cream-italic KJV lines, closing question card. NO AI motion
clips.

Stills live in assets/<slug>.jpeg (generated $0 in Google Flow, Nano Banana 2, 9:16).
build.py only reads the files. CAPTIONS ARE VERBATIM: every caption is the exact spoken
text of its narration segment (imported from make_narration.SEGMENTS and word-wrapped).
KJV (Jesus) lines render in cream italic.

FACE LAW v3 (2026-07-15 redo): Jesus's face IS shown in every still, the SAME face as
JESUS-MASTER-REF (attached as --ref at generation). Only Jesus wears cream. Captions are
CAPTION v2 — time-chunked along the wide bottom band, synced to the spoken audio.

CARE FLAGS: ARC, R, G (CONTENT-CARE #124).
  R — the agony frame (s7) shows only a few restrained dark drops on the pale stone,
  no wound, no gore. The arrest (s12) is only a distant line of torches, no violence.
  G — the grief is honored; the angel (s8) is the hope-beat and God's answer is presence.
  ARC — reverent restraint throughout.

TWO SACRED SILENCES (the music bed dies to true silence for both):
  jv42   Luke 22:42    "not my will, but thine, be done" — the surrender, the Seed
  jv46   Matthew 26:46 "Rise, let us be going" — the courage that carries him to the cross
A warm bed carries the story in, dies before the surrender, returns through the middle,
dies again before he rises, then returns for the final beat. No-Dead-Air is unaffected —
the narrator never stops; only the music does.

Timing is COMPUTED from measured mp3 durations, every beat timed off the SPOKEN end of
its audio (never the file end); the build RAISES on any spoken gap over 2.5s.

SIZE: 30MB cap (Cameron, 2026-07-14) — budget against a ~29.5MB container so the first
CRF pass lands in range with a real bitrate; never starve the video to hit the number.

Output: luke-22_gethsemane.mp4 (SCRIPTURE-NAME LAW), 1080x1920 H.264 30fps, <30MB.
"""
import os
import subprocess
import textwrap

import make_narration  # SEGMENTS -> verbatim caption text per segment

A = "assets"
S = "segs"
FPS = 30
# Bundled static ffmpeg lives at media-production/bin/ if present; else use system PATH.
# (Cross-platform, added by Machine B 2026-07-15 so this build rebuilds on Windows too.)
BIN = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "bin"))
def _tool(name):
    for cand in (os.path.join(BIN, name), os.path.join(BIN, name + ".exe")):
        if os.path.exists(cand):
            return cand
    return name  # fall back to system ffmpeg/ffprobe on PATH
FF = _tool("ffmpeg")
FPROBE = _tool("ffprobe")
# Serif fonts: Linux paths if present (Machine A); else Windows Georgia copied into
# segs/ at build time (relative path avoids ffmpeg drawtext choking on the C: colon).
_LINUX_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
_LINUX_SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
if os.path.exists(_LINUX_SERIF):
    SERIF, SERIF_BI = _LINUX_SERIF, _LINUX_SERIF_BI
else:
    SERIF, SERIF_BI = "segs/serif.ttf", "segs/serif_bi.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

S1 = "s1-arrival-garden.jpeg"
S2 = "s2-sit-ye-here.jpeg"
S3 = "s3-three-go-deeper.jpeg"
S4 = "s4-exceeding-sorrowful.jpeg"
S5 = "s5-stone-cast-kneeled.jpeg"
S6 = "s6-the-prayer-cup.jpeg"
S7 = "s7-agony-drops.jpeg"
S8 = "s8-the-angel.jpeg"
S9 = "s9-found-sleeping.jpeg"
S10 = "s10-watch-and-pray.jpeg"
S11 = "s11-third-prayer.jpeg"
S12 = "s12-rise-let-us-go.jpeg"

# Caption text = verbatim spoken text, keyed by segment name.
TEXT = {s[0]: s[4] for s in make_narration.SEGMENTS}
KJV = {"jv38", "jv42", "jv41", "jv46"}

# BEATS: (segment_name, still, zoom_dir). Within a run on the SAME still the zoom
# alternates in/out so consecutive beats on one image never jump.
BEATS = [
    ("n1", S1, "in"),
    ("n2", S2, "in"),
    ("n3", S3, "in"),
    ("jv38", S4, "in"),
    ("n4", S4, "out"),
    ("n5", S5, "in"),
    ("jv42", S6, "in"),                         # SURRENDER — full silence
    ("n6", S6, "out"),
    ("n7", S7, "in"),
    ("n8", S8, "in"),                           # the angel — hope beat
    ("n9", S9, "in"),
    ("jv41", S10, "in"),
    ("n10", S10, "out"),
    ("n11", S11, "in"),
    ("jv46", S12, "in"),                        # he rises — full silence
    ("n12", S12, "out"),
]

LEAD = 0.28
GAP = 0.65
KJV_GAP = 1.60
CARD_HOLD = 4.2


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


def caption_layers(seg_id, dur, spoken_end, text, kjv):
    # CAPTION v2: time-chunked captions along the wide bottom band, synced to the spoken
    # audio (narrator <=2 lines, KJV cream-italic <=3). Every frame is a dark night scene,
    # so a semi-opaque box keeps white/cream text legible while the scene reads above it.
    if kjv:
        font, size, color, width, maxl = SERIF_BI, 46, "0xFFF3DC", 38, 3
    else:
        font, size, color, width, maxl = SERIF, 34, "white", 48, 2
    chunks = chunk_caption(text, width, maxl)
    total = sum(len(c) for c in chunks) or 1
    t0, t1 = 0.15, max(0.6, min(dur - 0.2, spoken_end + 0.35))
    filters, labels = [], []
    acc = 0
    for i, c in enumerate(chunks):
        cs = t0 + (t1 - t0) * acc / total
        acc += len(c)
        ce = t0 + (t1 - t0) * acc / total
        tf = f"{S}/{seg_id}_{i}.txt"
        with open(tf, "w", encoding="utf-8") as f:
            f.write("\n".join(textwrap.wrap(c, width)))
        fo = max(cs, ce - 0.35)
        filters.append(
            f"color=c=black@0.0:s=1080x1920:r={FPS}:d={dur},format=rgba,"
            f"drawtext=fontfile={font}:textfile={tf}:fontsize={size}:"
            f"fontcolor={color}:line_spacing=13:x=(w-text_w)/2:"
            f"y=h-120-text_h:"
            f"shadowcolor=black@0.9:shadowx=2:shadowy=2:"
            f"box=1:boxcolor=black@0.58:boxborderw=22,"
            f"fade=t=in:st={cs:.2f}:d=0.35:alpha=1,"
            f"fade=t=out:st={fo:.2f}:d=0.35:alpha=1[cap{seg_id}{i}]")
        labels.append(f"[cap{seg_id}{i}]")
    return filters, labels


def build_still(seg_id, src, dur, zdir, spoken_end, cap_text, kjv, first):
    # ANTI-SHIMMER: drift rendered supersampled (2160 wide), lanczos'd to 1080.
    frames = int(dur * FPS)
    if zdir == "in":
        z = f"1.001+0.09*on/{frames}"
    else:
        z = f"1.091-0.09*on/{frames}"
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    capf, labels = caption_layers(seg_id, dur, spoken_end, cap_text, kjv)
    tail = ",fade=t=in:st=0:d=1.0" if first else ""
    steps, cur = [], "b"
    for i, lab in enumerate(labels):
        last = (i == len(labels) - 1)
        nxt = "v" if last else f"b{i+1}"
        steps.append(f"[{cur}]{lab}overlay=format=auto"
                     + (tail if last else "") + f"[{nxt}]")
        cur = nxt
    fc = f"{base}[b];" + ";".join(capf) + ";" + ";".join(steps)
    run([FF, "-y", "-loop", "1", "-i", f"{A}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{S}/{seg_id}.mp4"])


def build_card(dur, text):
    tf = f"{S}/card.txt"
    # UTF-8 so ffmpeg drawtext reads the em-dash correctly; Windows open() would default
    # to cp1252 and render "—" as a tofu box (matches caption_layers, build-72).
    with open(tf, "w", encoding="utf-8") as f:
        f.write("\n".join(textwrap.wrap(text, width=30)))
    vf = (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize=50:"
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
    os.makedirs(S, exist_ok=True)
    if not os.path.exists(_LINUX_SERIF):  # Windows: stage Georgia into segs/
        import shutil
        _wf = os.environ.get("WINDIR", "C:\\Windows") + "\\Fonts"
        shutil.copyfile(os.path.join(_wf, "georgia.ttf"), SERIF)
        shutil.copyfile(os.path.join(_wf, "georgiai.ttf"), SERIF_BI)

    spoken = {n: spoken_of(f"audio/{n}.mp3") for n, _, _ in BEATS}
    card_spoken = spoken_of("audio/card.mp3")

    timeline = []
    audio_place = []
    start_of = {}
    t = 0.0
    for name, still, zdir in BEATS:
        kjv = name in KJV
        gap = KJV_GAP if kjv else GAP
        vdur = LEAD + spoken[name] + gap
        a_start = t + LEAD
        audio_place.append((f"audio/{name}.mp3", a_start))
        start_of[name] = a_start
        timeline.append((name, still, zdir, vdur, a_start, kjv))
        t += vdur
    card_vdur = LEAD + card_spoken + CARD_HOLD
    card_start = t
    audio_place.append(("audio/card.mp3", card_start + LEAD))
    total = t + card_vdur

    # ---- on-paper silence map: prove no spoken gap exceeds 2.5s BEFORE mixing ----
    worst, worst_at = 0.0, None
    prev_end = None
    for name, _s, _z, _v, a_start, _k in timeline:
        if prev_end is not None and a_start - prev_end > worst:
            worst, worst_at = a_start - prev_end, name
        prev_end = a_start + spoken[name]
    print(f"total runtime: {total:.1f}s ({total/60:.2f} min)", flush=True)
    print(f"worst spoken gap: {worst:.2f}s before {worst_at} "
          f"(No-Dead-Air law: must be <= 2.5s)", flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s gap before {worst_at} "
                         f"exceeds the 2.5s law")
    print(f"sacred silence 1 (surrender): jv42 at {start_of['jv42']:.1f}s", flush=True)
    print(f"sacred silence 2 (he rises): jv46 at {start_of['jv46']:.1f}s", flush=True)

    # ---- render every still beat ----
    for i, (seg_id, still, zdir, vdur, _a, kjv) in enumerate(timeline):
        build_still(seg_id, still, vdur, zdir, LEAD + spoken[seg_id],
                    TEXT[seg_id], kjv, first=(i == 0))
    build_card(card_vdur, TEXT["card"])

    with open(f"{S}/concat.txt", "w") as f:
        for seg_id, *_ in timeline:
            f.write(f"file '{seg_id}.mp4'\n")
        f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{S}/concat.txt",
         "-c", "copy", f"{S}/video_silent.mp4"])

    # ---- audio: narration at computed offsets + warm beds around two silences ----
    p1_end = start_of["jv42"] + spoken["jv42"]
    p2_end = start_of["jv46"] + spoken["jv46"]
    beds = [
        (0.0, start_of["jv42"] - 1.2, "b"),
        (p1_end + 1.0, start_of["jv46"] - 1.0, "a"),
        (p2_end + 1.0, card_start - 0.8, "a"),
    ]
    print(f"music: bed out at {start_of['jv42'] - 1.2:.1f}s, silent through jv42 "
          f"(ends {p1_end:.1f}s); returns; silent again through jv46 "
          f"(ends {p2_end:.1f}s)", flush=True)

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
    gain = max(-6.0, min(10.0, -15.0 - lufs)) if lufs is not None else 0.0
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    # ---- final mux: the ONLY lossy generation. 30MB cap; never starve the bitrate. ----
    OUT = "luke-22_gethsemane.mp4"
    A_KBPS, MUX = 96, 20
    vcap = int(29.5 * 8000 / total) - A_KBPS - MUX
    if vcap < 400:
        raise SystemExit(
            f"BITRATE STARVED even at 30MB: {total:.0f}s only leaves {vcap} kbps "
            f"of video (need >=400). Shorten the script — do not ship blocking.")
    print(f"video budget: {vcap} kbps ({total:.0f}s, 30MB cap)", flush=True)

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
