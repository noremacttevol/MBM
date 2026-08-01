#!/usr/bin/env python3
"""v2_assemble.py — build a finished V2 video from a row's generated pictures.

Reuses the V1 build's proven machinery instead of reinventing it:
  - extract_beats.extract(row) reproduces the V1 timeline arithmetic exactly
    (per-segment audio windows, card, total), so the V2 cut is frame-compatible
    with the approved V1 narration.
  - The V1 build folder's own mbm_caption_timing.caption_filter draws the
    captions (same fonts, colours, band, SPEAKER-LAW) — imported via sys.path,
    never copied, never modified.
  - Captions are timed from the V1 audio files read-only; nothing is ever
    written into the V1 folder (V2-KICKOFF hard protection #1).
  - The finished V1 MP4's AAC stream is copied packet-for-packet into V2.
    V2 never regenerates, re-times, mixes, gains, shortens, or re-encodes audio.

What is new: the video track. V1 shows ONE still per narration segment; V2
shows SEVERAL (the beats_v2.py windows). Each V2 beat becomes a supersampled
Ken Burns chunk (the exact V1 zoompan formula) covering from its window start
to the next beat's start, chunks are concatenated, and then every segment's
caption filter is applied over the full track with its enable= times shifted
from segment-local to global (between(t,..) -> between(t-SEG_START,..)).

The closing card and visual duration follow V1. The final audio hash must equal
V1 exactly or the build fails.

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
import tempfile
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import extract_beats  # noqa: E402

FF = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"
FPS = 30
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
CREAM = "0xF7F2E9"
INK = "0x3B2A1E"
ENC = ["-c:v", "libx264", "-preset", "medium", "-crf", "16",
       "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]


def run(cmd):
    print(">>", " ".join(str(c) for c in cmd)[:160], flush=True)
    subprocess.run(cmd, check=True, capture_output=True)


def duration_of(path):
    probe = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path],
        capture_output=True, text=True, check=True)
    return float(probe.stdout.strip())


def audio_stream_hash(path):
    """Hash encoded audio packets, independent of the MP4 container."""
    probe = subprocess.run(
        [FF, "-v", "error", "-i", path, "-map", "0:a:0", "-c", "copy",
         "-f", "hash", "-hash", "sha256", "-"],
        capture_output=True, text=True, check=True)
    return probe.stdout.strip()


def v2_dir_of(row):
    cands = sorted(set(
        glob.glob(os.path.join(HERE, f"build-{row}-*"))
        + glob.glob(os.path.join(HERE, f"build-{row:02d}-*"))
    ))
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
    return (
        beats,
        getattr(mod, "OUTPUT_ASSET_DIR", "assets"),
        getattr(mod, "OUTPUT_VIDEO_NAME", None),
    )


def build_chunk(v2dir, assets_dir, idx, src, dur, zdir, first, last, segs):
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
    run([FF, "-y", "-loop", "1", "-i", os.path.join(assets_dir, src),
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
    resume_base = "--resume-base" in sys.argv[2:]
    base_only = "--base-only" in sys.argv[2:]
    prepare_only = "--prepare-only" in sys.argv[2:]
    data = extract_beats.extract(row)
    v1dir = os.path.join(ROOT, data["v1_dir"])
    v2dir = v2_dir_of(row)
    sys.path.insert(0, v1dir)  # mbm_caption_timing + mbm_speakers, V1's own
    from mbm_caption_timing import caption_filter  # noqa: E402

    # segs/ scratch lives in the V2 dir.  Do not trust a build-local audio/
    # directory: older V2 attempts may contain stale narration files.  Caption
    # timing gets an isolated, read-only view of the authoritative V1 audio
    # below, while the finished AAC is still copied from the V1 final MP4.
    os.chdir(v2dir)
    os.makedirs("segs", exist_ok=True)
    segs = "segs"

    beats, assets_dir, configured_output_name = load_beats_v2(v2dir)
    for b in beats:
        p = os.path.join(assets_dir, b["out"])
        if not os.path.isfile(p):
            raise SystemExit(f"missing picture: {p} — row not fully generated")

    card_start = data["card"]["seg_start"]
    total = data["total"]

    # ---- video chunks: each beat holds the screen until the next begins ----
    base_path = os.path.join(segs, "base.mp4")
    if resume_base:
        if not os.path.isfile(base_path):
            raise SystemExit("--resume-base requested but segs/base.mp4 is missing")
        print(f"RESUME BASE: {base_path}", flush=True)
    else:
        chunk_files = []
        for i, b in enumerate(beats):
            start = 0.0 if i == 0 else b["start"]
            end = beats[i + 1]["start"] if i + 1 < len(beats) else card_start
            dur = end - start
            if dur <= 0.05:
                continue
            zdir = "in" if i % 2 == 0 else "out"
            chunk_files.append(build_chunk(
                v2dir, assets_dir, i, b["out"], dur, zdir,
                first=(i == 0), last=(i + 1 == len(beats)), segs=segs))

        with open(os.path.join(segs, "concat_base.txt"), "w") as f:
            for c in chunk_files:
                f.write(f"file '{os.path.basename(c)}'\n")
        run([FF, "-y", "-f", "concat", "-safe", "0",
             "-i", os.path.join(segs, "concat_base.txt"),
             "-c", "copy", base_path])

    if base_only:
        print("BASE ONLY: motion master is ready", flush=True)
        return

    # ---- captions: every segment's V1 filter, shifted to global time ----
    filters = []
    with tempfile.TemporaryDirectory(prefix=".caption-context-", dir=v2dir) as ctx:
        os.symlink(os.path.join(v1dir, "audio"), os.path.join(ctx, "audio"))
        os.symlink(os.path.join(v2dir, segs), os.path.join(ctx, "segs"))
        prior_cwd = os.getcwd()
        os.chdir(ctx)
        try:
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
        finally:
            os.chdir(prior_cwd)
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

    if prepare_only:
        print("PREPARE ONLY: silent master is ready", flush=True)
        return

    # ---- final mux: pictures change; the finished V1 audio cannot ----
    v1_mp4 = [f for f in os.listdir(v1dir) if f.endswith(".mp4")]
    if len(v1_mp4) != 1:
        raise SystemExit(
            f"AUDIO LOCK: row {row} needs exactly one authoritative V1 MP4, "
            f"found {v1_mp4}")
    locked_v1_name = v1_mp4[0]
    out_name = configured_output_name or locked_v1_name
    locked_final = os.path.join(v1dir, locked_v1_name)
    locked_duration = duration_of(locked_final)
    if abs(total - locked_duration) > 1.0:
        raise SystemExit(
            f"AUDIO LOCK: extracted timeline is {total:.3f}s but the "
            f"authoritative V1 final is {locked_duration:.3f}s")
    locked_hash = audio_stream_hash(locked_final)
    vcap = max(300, int(24.5 * 8000 / locked_duration) - 145)
    run([FF, "-y", "-i", os.path.join(segs, "video_silent.mp4"),
         "-i", locked_final, "-map", "0:v:0", "-map", "1:a:0",
         "-c:v", "libx264", "-preset", "medium", "-crf", "19",
         "-maxrate", f"{vcap}k", "-bufsize", f"{2*vcap}k",
         "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "copy", "-movflags", "+faststart",
         "-t", f"{locked_duration:.6f}", out_name])
    rebuilt_hash = audio_stream_hash(out_name)
    if rebuilt_hash != locked_hash:
        raise SystemExit(
            f"AUDIO LOCK FAILED: V1 {locked_hash}, V2 {rebuilt_hash}")
    size = os.path.getsize(out_name) / 1e6
    print(f"AUDIO LOCK PASS: {rebuilt_hash}", flush=True)
    print(f"DONE {out_name}  {size:.1f} MB  {locked_duration:.1f}s", flush=True)


if __name__ == "__main__":
    main()
