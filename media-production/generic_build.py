#!/usr/bin/env python3
"""
generic_build.py — assemble ANY MBM build folder into a finished video from its
stills + make_narration.py, with NO per-video hand-tuning.

Why this exists: the classic per-folder build.py (build-48 is the master) hard-codes a
BEATS map, KJV set, and music beds for each video. Since the HUM PURGE zeroed every
music bed (narration + silence only, PRODUCTION-BIBLE #5b 2026-07-16), the only thing
left that varied per video was the segment->still map and the KJV flags — both of which
can be DERIVED. This script derives them:

  * SEGMENTS come from the folder's make_narration.py (name, voice, rate, pitch, text).
  * The closing "card" segment renders as the cream invitation card (not a still).
  * All other segments are "content beats". Stills in assets/ (sorted s1..sN) are
    distributed across the content beats in order, proportional to each beat's spoken
    length, so a long narration beat shows more pictures and a short one shows fewer.
    Every still is used; every spoken word is captioned verbatim (caption-v2, wide
    bottom, KJV in cream italic).
  * A beat is KJV (Jesus, cream italic caption, longer reverent gap) iff its segment
    name starts with 'j'.

Laws honored: caption-v2 wide-bottom (<=2 narrator lines / <=3 KJV), verbatim captions,
No-Dead-Air (<=2.5s spoken gap, build RAISES otherwise), anti-shimmer supersampled
Ken Burns, scripture-name output when derivable, <25MB H.264 1080x1920. No music bed.

Usage:
    python3 ../generic_build.py            # run from inside a build-NN folder
    python3 generic_build.py <folder>      # or pass the folder path
"""
import os
import re
import sys
import glob
import subprocess
import textwrap
import importlib.util

FPS = 30
FF = "ffmpeg"
FPROBE = "ffprobe"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"

ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]

LEAD = 0.28
GAP = 0.65
KJV_GAP = 1.30
CARD_HOLD = 4.2


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:120], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


def dur_of(path):
    out = subprocess.run(
        [FPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(out.stdout.strip())


def spoken_of(path, seg_dir):
    tmp = f"{seg_dir}/_spoken.wav"
    run([FF, "-y", "-v", "error", "-i", path, "-af",
         "areverse,silenceremove=start_periods=1:start_threshold=-50dB:"
         "start_duration=0.02,areverse", "-c:a", "pcm_s16le", tmp])
    return dur_of(tmp)


def sentences(text):
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


def caption_layers(seg_dir, seg_id, dur, spoken_end, text, kjv):
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
        tf = f"{seg_dir}/{seg_id}_{i}.txt"
        with open(tf, "w") as f:
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


def build_beat(seg_dir, assets, beat_id, src, dur, zdir, spoken_end,
               cap_text, kjv, first):
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
    if cap_text and cap_text.strip():
        capf, labels = caption_layers(seg_dir, beat_id, dur, spoken_end, cap_text, kjv)
    else:
        capf, labels = [], []
    if labels:
        steps, cur = [], "b"
        for i, lab in enumerate(labels):
            last = (i == len(labels) - 1)
            nxt = "v" if last else f"b{i+1}"
            steps.append(f"[{cur}]{lab}overlay=format=auto"
                         + (tail if last else "") + f"[{nxt}]")
            cur = nxt
        fc = f"{base}[b];" + ";".join(capf) + ";" + ";".join(steps)
    else:
        # no caption on this still: just the Ken Burns base (+ optional first-fade)
        fc = f"{base}{tail}[v]"
    run([FF, "-y", "-loop", "1", "-i", f"{assets}/{src}", "-t", str(dur),
         "-filter_complex", fc, "-map", "[v]"] + ENC + [f"{seg_dir}/{beat_id}.mp4"])


def build_card(seg_dir, dur, text):
    tf = f"{seg_dir}/card.txt"
    with open(tf, "w") as f:
        f.write("\n".join(textwrap.wrap(text, width=30)))
    vf = (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize=52:"
          f"fontcolor={INK}:line_spacing=24:x=(w-text_w)/2:y=(h-text_h)/2,"
          f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8")
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur}",
         "-vf", vf] + ENC + [f"{seg_dir}/card.mp4"])


def derive_output_name(folder, mod):
    """scripture-name law: book-chapter_story-name.mp4 when derivable from the docstring."""
    doc = (mod.__doc__ or "")
    m = re.search(r"\(([1-3]?\s?[A-Za-z]+)\s+(\d+)", doc)
    slug = re.sub(r"^build-\d+-", "", os.path.basename(folder.rstrip("/")))
    if m:
        book = m.group(1).lower().replace(" ", "")
        return f"{book}-{m.group(2)}_{slug}.mp4"
    return f"{slug}.mp4"


def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    folder = os.path.abspath(folder)
    os.chdir(folder)
    assets = "assets"
    seg_dir = "segs"
    os.makedirs(seg_dir, exist_ok=True)
    os.makedirs("audio", exist_ok=True)

    # load this folder's make_narration.py
    spec = importlib.util.spec_from_file_location("mn", "make_narration.py")
    mn = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mn)
    SEGMENTS = mn.SEGMENTS

    # generate narration audio (idempotent)
    import asyncio
    import edge_tts
    SPOKEN = getattr(mn, "SPOKEN", {})

    async def gen():
        for name, voice, rate, pitch, text in SEGMENTS:
            tts_text = SPOKEN.get(name, text)
            c = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
            await c.save(f"audio/{name}.mp3")
    asyncio.run(gen())

    text_of = {s[0]: s[4] for s in SEGMENTS}
    content = [s for s in SEGMENTS if s[0] != "card"]
    has_card = any(s[0] == "card" for s in SEGMENTS)

    stills = sorted(glob.glob(f"{assets}/*.jpeg") + glob.glob(f"{assets}/*.jpg")
                    + glob.glob(f"{assets}/*.png"))
    stills = [os.path.basename(s) for s in stills]
    if not stills:
        raise SystemExit(f"NO STILLS in {folder}/assets — cannot build")

    spoken = {s[0]: spoken_of(f"audio/{s[0]}.mp3", seg_dir) for s in SEGMENTS}

    # distribute stills across content segments proportional to spoken length
    total_spoken = sum(spoken[s[0]] for s in content) or 1.0
    alloc = {}
    remaining = len(stills)
    for i, s in enumerate(content):
        if i == len(content) - 1:
            alloc[s[0]] = remaining
        else:
            n = max(1, round(len(stills) * spoken[s[0]] / total_spoken))
            n = min(n, remaining - (len(content) - 1 - i))  # leave >=1 each
            n = max(1, n)
            alloc[s[0]] = n
            remaining -= n
    # safety: if allocation undershoots, dump extras on last
    used = sum(alloc.values())
    if used < len(stills):
        alloc[content[-1][0]] += len(stills) - used

    # build the timeline of beats (one per still)
    beats = []
    si = 0
    for s in content:
        name = s[0]
        kjv = name.startswith("j")
        n_stills = alloc[name]
        share = spoken[name] / n_stills
        for k in range(n_stills):
            beats.append({
                "beat_id": f"{name}_{k}",
                "seg": name,
                "still": stills[si],
                "kjv": kjv,
                "spoken": share,
                "first_of_seg": (k == 0),
                "caption": text_of[name] if k == 0 else "",  # caption on first still of seg
            })
            si += 1

    # timing
    t = 0.0
    worst, worst_at, prev_end = 0.0, None, None
    for i, b in enumerate(beats):
        kjv = b["kjv"]
        gap = (KJV_GAP if kjv else GAP) if b == beats[-1] or True else GAP
        # only add the segment gap after the LAST still of a segment
        is_last_of_seg = (i == len(beats) - 1) or (beats[i + 1]["seg"] != b["seg"])
        seg_gap = (KJV_GAP if kjv else GAP) if is_last_of_seg else 0.10
        vdur = LEAD + b["spoken"] + seg_gap
        a_start = t + LEAD
        b["vdur"] = vdur
        b["a_start"] = a_start
        b["zdir"] = "in" if i % 2 == 0 else "out"
        if b["first_of_seg"]:
            if prev_end is not None and a_start - prev_end > worst:
                worst, worst_at = a_start - prev_end, b["seg"]
            prev_end = a_start + spoken[b["seg"]]
        t += vdur

    card_vdur = 0.0
    card_start = t
    if has_card:
        card_spoken = spoken["card"]
        card_vdur = LEAD + card_spoken + CARD_HOLD
    total = t + card_vdur

    print(f"folder: {os.path.basename(folder)}", flush=True)
    print(f"stills: {len(stills)}  content-beats: {len(beats)}  "
          f"runtime: {total:.1f}s ({total/60:.2f} min)", flush=True)
    print(f"worst spoken gap: {worst:.2f}s before {worst_at} (law <=2.5s)", flush=True)
    if worst > 2.5:
        raise SystemExit(f"DEAD AIR: {worst:.2f}s before {worst_at} exceeds 2.5s law")

    # render beats
    audio_place = []
    seg_started = set()
    for i, b in enumerate(beats):
        cap = b["caption"]
        spoken_end = LEAD + b["spoken"]
        build_beat(seg_dir, assets, b["beat_id"], b["still"], b["vdur"],
                   b["zdir"], spoken_end, cap, b["kjv"], first=(i == 0))
        if b["seg"] not in seg_started:
            audio_place.append((f"audio/{b['seg']}.mp3", b["a_start"]))
            seg_started.add(b["seg"])
    if has_card:
        build_card(seg_dir, card_vdur, text_of["card"])
        audio_place.append(("audio/card.mp3", card_start + LEAD))

    # concat silent video
    with open(f"{seg_dir}/concat.txt", "w") as f:
        for b in beats:
            f.write(f"file '{b['beat_id']}.mp4'\n")
        if has_card:
            f.write("file 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", f"{seg_dir}/concat.txt",
         "-c", "copy", f"{seg_dir}/video_silent.mp4"])

    # audio: narration at offsets, no bed
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
        f"{seg_dir}/audio_mix.m4a"])

    # loudness toward -15 LUFS
    probe = subprocess.run(
        [FF, "-i", f"{seg_dir}/audio_mix.m4a", "-af", "ebur128", "-f", "null", "-"],
        capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            lufs = float(line.split()[1])
    gain = max(-6.0, min(10.0, -15.0 - lufs)) if lufs is not None else 0.0
    print(f"loudness: {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    # final mux, size-capped <25MB
    out = derive_output_name(folder, mn)
    A_KBPS = 96
    MUX = 20
    vcap = int(24.0 * 8000 / total) - A_KBPS - MUX
    if vcap < 400:
        raise SystemExit(f"BITRATE STARVED: {total:.0f}s leaves {vcap} kbps (<400).")
    size, crf = 0.0, 20
    for crf in (20, 21, 22, 23, 24):
        run([FF, "-y", "-i", f"{seg_dir}/video_silent.mp4",
             "-i", f"{seg_dir}/audio_mix.m4a", "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-preset", "slow", "-crf", str(crf),
             "-maxrate", f"{vcap}k", "-bufsize", f"{vcap*2}k",
             "-pix_fmt", "yuv420p",
             "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
             "-c:a", "aac", "-b:a", f"{A_KBPS}k", "-movflags", "+faststart", out])
        size = os.path.getsize(out) / 1e6
        if size <= 24.3:
            break
    print(f"DONE: {out}  {size:.1f} MB, {total:.1f}s (crf {crf}, vcap {vcap}k)",
          flush=True)


if __name__ == "__main__":
    main()
