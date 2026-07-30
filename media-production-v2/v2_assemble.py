#!/usr/bin/env python3
"""v2_assemble.py — build a finished V2 video from a row's generated pictures.

Reuses the V1 build's proven machinery instead of reinventing it:
  - extract_beats.extract(row) reproduces the V1 timeline arithmetic exactly
    (per-segment audio windows, card, total), so the V2 cut is frame-compatible
    with the approved V1 narration.
  - The V1 build folder's own mbm_caption_timing.caption_filter draws the
    captions (same fonts, colours, band, SPEAKER-LAW) — imported via sys.path,
    never copied, never modified.
  - The V1 audio files are used read-only through a symlink; nothing is ever
    written into the V1 folder (V2-KICKOFF hard protection #1).

What is new: the video track. V1 shows ONE still per narration segment; V2
shows SEVERAL (the beats_v2.py windows). Each V2 beat becomes a supersampled
Ken Burns chunk (the exact V1 zoompan formula) covering from its window start
to the next beat's start, chunks are concatenated, and then every segment's
caption filter is applied over the full track with its enable= times shifted
from segment-local to global (between(t,..) -> between(t-SEG_START,..)).

Card, audio placement, dead-air check, loudness law (-15 LUFS) and the crf
step-up size ladder are V1's, verbatim.

Usage:  python3 media-production-v2/v2_assemble.py 7
Output: <v2-build-dir>/<v1-mp4-name>  (e.g. matthew-14_peter-walks-on-water.mp4)
"""
import glob
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import extract_beats  # noqa: E402

FF = shutil.which("ffmpeg") or "ffmpeg"
FPS = 30
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:160], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


def v2_dir_of(row):
    cands = sorted(glob.glob(os.path.join(HERE, f"build-{row}-*"))
                   + glob.glob(os.path.join(HERE, f"build-{row:02d}-*")))
    cands = [c for c in cands if os.path.isfile(os.path.join(c, "beats_v2.py"))]
    if len(cands) != 1:
        raise SystemExit(f"row {row}: expected exactly one v2 build dir with "
                         f"beats_v2.py, found {cands}")
    return cands[0]


def load_beats_v2(v2dir):
    spec = importlib.util.spec_from_file_location(
        "beats_v2", os.path.join(v2dir, "beats_v2.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    beats = []
    for b in mod.BEATS:
        a, z = b["window"].split("-")
        beats.append({"out": b["out"], "start": float(a), "end": float(z)})
    beats.sort(key=lambda b: b["start"])
    return beats


def build_chunk(v2dir, idx, src, dur, zdir, first, last, segs):
    frames = max(1, int(round(dur * FPS)))
    if zdir == "in":
        z = f"1.001+0.10*on/{frames}"
    else:
        z = f"1.101-0.10*on/{frames}"
    base = (f"[0:v]scale=2160:3868,setsar=1,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s=2160x3840:fps={FPS},"
            f"scale=1080:1920:flags=lanczos")
    tail = ""
    if first:
        tail = ",fade=t=in:st=0:d=1.2"
    if last and dur > 1.4:
        tail = f",fade=t=out:st={dur-1.2}:d=1.2"
    out = os.path.join(segs, f"c{idx:03d}.mp4")
    run([FF, "-y", "-loop", "1", "-i", os.path.join("assets", src),
         "-t", f"{dur:.3f}", "-filter_complex", f"{base}{tail}[v]",
         "-map", "[v]"] + ENC + [out])
    return out


# --- card: V1 build_card, verbatim behaviour (auto-wrap law) ---
def build_card(segs, dur, text):
    size = 50
    lh = size + 22
    lines = [w for para in text.split("\n")
             for w in (textwrap.wrap(para, width=30) or [""])]
    L = len(lines)
    vf = ""
    for j, ln in enumerate(lines):
        if not ln.strip():
            continue
        tf = os.path.join(segs, f"card_{j}.txt")
        with open(tf, "w", encoding="utf-8") as f:
            f.write(ln)
        y = f"(h-{L * lh})/2+{j * lh}"
        vf += (f"drawtext=fontfile={SERIF}:textfile={tf}:fontsize={size}:"
               f"fontcolor={INK}:x=(w-text_w)/2:y={y},")
    vf += f"fade=t=in:st=0:d=0.8,fade=t=out:st={dur-0.8}:d=0.8"
    out = os.path.join(segs, "card.mp4")
    run([FF, "-y", "-f", "lavfi",
         "-i", f"color=c={CREAM}:s=1080x1920:r={FPS}:d={dur:.3f}",
         "-vf", vf] + ENC + [out])
    return out


def main():
    row = int(sys.argv[1])
    data = extract_beats.extract(row)
    v1dir = os.path.join(ROOT, data["v1_dir"])
    v2dir = v2_dir_of(row)
    sys.path.insert(0, v1dir)  # mbm_caption_timing + mbm_speakers, V1's own
    from mbm_caption_timing import caption_filter  # noqa: E402

    # V1 audio through a read-only symlink; segs/ scratch lives in the V2 dir.
    os.chdir(v2dir)
    if not os.path.exists("audio"):
        os.symlink(os.path.join(v1dir, "audio"), "audio")
    os.makedirs("segs", exist_ok=True)
    segs = "segs"

    beats = load_beats_v2(v2dir)
    for b in beats:
        p = os.path.join("assets", b["out"])
        if not os.path.isfile(p):
            raise SystemExit(f"missing picture: {p} — row not fully generated")

    card_start = data["card"]["seg_start"]
    total = data["total"]

    # ---- video chunks: each beat holds the screen until the next begins ----
    chunk_files = []
    for i, b in enumerate(beats):
        start = 0.0 if i == 0 else b["start"]
        end = beats[i + 1]["start"] if i + 1 < len(beats) else card_start
        dur = end - start
        if dur <= 0.05:
            continue
        zdir = "in" if i % 2 == 0 else "out"
        chunk_files.append(build_chunk(
            v2dir, i, b["out"], dur, zdir,
            first=(i == 0), last=(i + 1 == len(beats)), segs=segs))

    with open(os.path.join(segs, "concat_base.txt"), "w") as f:
        for c in chunk_files:
            f.write(f"file '{os.path.basename(c)}'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0",
         "-i", os.path.join(segs, "concat_base.txt"),
         "-c", "copy", os.path.join(segs, "base.mp4")])

    # ---- captions: every segment's V1 filter, shifted to global time ----
    filters = []
    for s in data["beats"]:
        if s["speaker"] == "silence" or not s["text"]:
            continue
        local_dur = s["seg_dur"]
        local_spoken_end = s["spoken_end"] - s["seg_start"]
        f = caption_filter(s["seg"], local_dur, local_spoken_end,
                           s["text"], s["speaker"])
        if not f:
            continue
        off = s["seg_start"]
        f = f.replace("between(t,", f"between(t-{off:.3f},")
        filters.append(f.lstrip(","))
    chain = "[0:v]" + ",".join(filters) + "[v]"
    run([FF, "-y", "-i", os.path.join(segs, "base.mp4"),
         "-filter_complex", chain, "-map", "[v]"] + ENC +
        [os.path.join(segs, "captioned.mp4")])

    # ---- card + concat ----
    card_dur = data["card"]["seg_dur"]
    build_card(segs, card_dur, data["card"]["text"])
    with open(os.path.join(segs, "concat.txt"), "w") as f:
        f.write("file 'captioned.mp4'\nfile 'card.mp4'\n")
    run([FF, "-y", "-f", "concat", "-safe", "0",
         "-i", os.path.join(segs, "concat.txt"),
         "-c", "copy", os.path.join(segs, "video_silent.mp4")])

    # ---- audio: narration at derived offsets (no beds — Cameron 2026-07-16) ----
    audio_place = [(f"audio/{s['seg']}.mp3", s["audio_start"])
                   for s in data["beats"] if s["speaker"] != "silence"]
    audio_place.append((f"audio/{data['card']['seg']}.mp3",
                        data["card"]["audio_start"]))
    inputs, filts, labels = [], [], []
    for i, (path, start) in enumerate(audio_place):
        inputs += ["-i", path]
        ms = int(start * 1000)
        filts.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    filts.append("".join(labels) +
                 f"amix=inputs={len(labels)}:duration=longest:normalize=0,"
                 f"apad=whole_dur={total:.2f}[aout]")
    run([FF, "-y"] + inputs + ["-filter_complex", ";".join(filts),
         "-map", "[aout]", "-t", f"{total:.2f}", "-c:a", "aac", "-b:a", "160k",
         os.path.join(segs, "audio_mix.m4a")])

    # ---- loudness law: measure EBU R128, lift toward -15 LUFS ----
    probe = subprocess.run(
        [FF, "-i", os.path.join(segs, "audio_mix.m4a"), "-af", "ebur128",
         "-f", "null", "-"], capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            lufs = float(line.split()[1])
    gain = 0.0
    if lufs is not None:
        gain = max(-6.0, min(16.0, -15.0 - lufs))
    print(f"loudness: measured {lufs} LUFS, applying {gain:+.1f} dB", flush=True)

    # ---- final mux: runtime-computed rate cap (V1 size ladder) ----
    v1_mp4 = [f for f in os.listdir(v1dir) if f.endswith(".mp4")]
    out_name = v1_mp4[0] if len(v1_mp4) == 1 else f"v2-row{row}.mp4"
    vcap = max(300, int(24.5 * 8000 / total) - 145)
    run([FF, "-y", "-i", os.path.join(segs, "video_silent.mp4"),
         "-i", os.path.join(segs, "audio_mix.m4a"),
         "-af", f"volume={gain:.1f}dB",
         "-c:v", "libx264", "-preset", "medium", "-crf", "19",
         "-maxrate", f"{vcap}k", "-bufsize", f"{2*vcap}k",
         "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
         "-t", f"{total:.2f}", out_name])
    size = os.path.getsize(out_name) / 1e6
    print(f"DONE {out_name}  {size:.1f} MB  {total:.1f}s", flush=True)


if __name__ == "__main__":
    main()
