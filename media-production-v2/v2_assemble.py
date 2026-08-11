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



def _speaker_overrides(v2dir):
    """SPEAKER_OVERRIDES from a build's beats_v2.py, if it declares any."""
    spec = importlib.util.spec_from_file_location(
        "beats_v2_spk", os.path.join(v2dir, "beats_v2.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return dict(getattr(mod, "SPEAKER_OVERRIDES", {}))


def _text_overrides(v2dir):
    """TEXT_OVERRIDES from a build's beats_v2.py, if it declares any.

    Captions are drawn from the V1 narration SCRIPT, but on some rows that script
    was rewritten AFTER the voices were cut and no longer matches the mp3s that
    actually ship (row 20: a programmatic rewrite stripped the plain-English
    retellings out of n1b / n12 / n14 / n15, all four of which are audibly present
    in the approved audio — confirmed by transcribing the real files). Using the
    stale text prints words nobody says and throws that segment's caption timing
    off as well, because the windows are matched character-by-character against the
    timing sidecar. A build may declare TEXT_OVERRIDES = {"n12": "...", ...} with
    the text that is genuinely spoken. V1 is never edited (hard protection #1).
    """
    spec = importlib.util.spec_from_file_location(
        "beats_v2_text", os.path.join(v2dir, "beats_v2.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return dict(getattr(mod, "TEXT_OVERRIDES", {}))


def _audio_from_segments(v2dir):
    """AUDIO_FROM_V1_SEGMENTS flag from a build's beats_v2.py.

    WHY THIS EXISTS (2026-08-02, row 25 — wheat and tares). The AUDIO LOCK copies
    the finished V1 MP4's AAC stream, which is right whenever that MP4 is the
    current render of the current narration. On row 25 it is NOT: the MP4 was
    rendered 2026-07-22, the ElevenLabs re-voice ran 2026-07-23, and the
    echo-delete sweep then removed `n1` (a narrator echo of j24's own KJV line,
    "the kingdom of heaven … sowed good seed in his field") and trimmed "So let
    them both grow" out of n9 (an echo of j1). The mp3 set on disk carries all of
    that; the MP4 carries none of it and runs 229.033 s against the real 166.8 s
    timeline. Copying it would ship pre-REDO-ALL voices, re-insert the echoes the
    sweep deleted, and throw every caption 60+ s adrift.

    V1 stays read-only (hard protection #1), so instead of re-rendering the V1
    build, a V2 build may declare AUDIO_FROM_V1_SEGMENTS = True. The finished
    audio is then assembled from the V1 build's OWN mp3 files, placed at exactly
    the offsets extract_beats computes from that build's own constants — the same
    arithmetic V1's build.py performs. Nothing is re-voiced, re-timed, gained per
    segment, or resynthesised: each mp3 is delayed and summed, byte-for-byte the
    source the V1 build would have used had it been re-rendered.
    """
    spec = importlib.util.spec_from_file_location(
        "beats_v2_audio", os.path.join(v2dir, "beats_v2.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return bool(getattr(mod, "AUDIO_FROM_V1_SEGMENTS", False))


def rebuild_audio_from_segments(v1dir, segs, data):
    """Render the authoritative narration track from the V1 build's own mp3s.

    Mirrors V1 build.py's audio stage: every segment delayed to its computed
    audio_start, summed with amix(normalize=0), padded to the full runtime, then
    loudness-trimmed toward -15 LUFS exactly as V1 does. The 'music beds' V1 still
    lists are amplitude-zeroed (HUM PURGE, 2026-07-16) and therefore contribute
    nothing, so they are simply not built — narration + silence only.
    """
    total = data["total"]
    places = [(os.path.join(v1dir, "audio", f"{b['seg']}.mp3"), b["audio_start"])
              for b in data["beats"] if b["speaker"] != "silence"]
    # A SILENT question card (beats.json "silent": true → seg=None, audio_start=None,
    # e.g. row 128) has no spoken mp3; it contributes no audio and the apad below
    # pads the track through its on-screen duration. Only place a card that has one.
    if data["card"].get("seg") is not None:
        places.append((os.path.join(v1dir, "audio", f"{data['card']['seg']}.mp3"),
                       data["card"]["audio_start"]))
    inputs, filters, labels = [], [], []
    for i, (path, start) in enumerate(places):
        if not os.path.isfile(path):
            raise SystemExit(f"AUDIO REBUILD: missing V1 segment audio {path}")
        inputs += ["-i", path]
        ms = int(start * 1000)
        filters.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},volume=1.0[a{i}]")
        labels.append(f"[a{i}]")
    filters.append("".join(labels) +
                   f"amix=inputs={len(labels)}:duration=longest:normalize=0,"
                   f"apad=whole_dur={total:.2f}[aout]")
    mix = os.path.join(segs, "audio_v1_rebuilt.m4a")
    run([FF, "-y"] + inputs + ["-filter_complex", ";".join(filters),
         "-map", "[aout]", "-t", f"{total:.2f}",
         "-c:a", "aac", "-b:a", "160k", mix])

    probe = subprocess.run([FF, "-i", mix, "-af", "ebur128", "-f", "null", "-"],
                           capture_output=True, text=True)
    lufs = None
    for line in probe.stderr.splitlines():
        line = line.strip()
        if line.startswith("I:") and "LUFS" in line:
            lufs = float(line.split()[1])
    gain = max(-6.0, min(16.0, -15.0 - lufs)) if lufs is not None else 0.0
    final = os.path.join(segs, "audio_v1_final.m4a")
    run([FF, "-y", "-i", mix,
         "-af", f"volume={gain:.1f}dB,alimiter=limit=0.95",
         "-c:a", "aac", "-b:a", "128k", "-t", f"{total:.6f}", final])
    print(f"AUDIO REBUILT from {len(places)} V1 segment mp3s "
          f"({lufs} LUFS -> {gain:+.1f} dB), {duration_of(final):.3f}s", flush=True)
    return final


def content_time(path):
    """When this file's CONTENT was last changed, in epoch seconds.

    Filesystem mtime alone is worthless here: this repo is cloned and pulled on
    four machines, so a checkout stamps every file with the checkout time and a
    2026-07-22 render ends up looking newer than the 2026-07-24 re-voice it
    predates. For a tracked, clean file the honest answer is the commit that last
    changed it. Only when the file is untracked or dirty in the working tree does
    mtime carry information, and then it is the later of the two.
    """
    rel = os.path.relpath(path, ROOT)
    def _git(args):
        return subprocess.run(["git", "-C", ROOT] + args,
                              capture_output=True, text=True)
    try:
        tracked = _git(["ls-files", "--error-unmatch", "--", rel]).returncode == 0
    except OSError:
        tracked = False
    mtime = os.path.getmtime(path)
    if not tracked:
        return mtime
    out = _git(["log", "-1", "--format=%ct", "--", rel]).stdout.strip()
    if not out:
        return mtime
    committed = int(out)
    dirty = _git(["diff", "--quiet", "--", rel]).returncode != 0
    return max(committed, mtime) if dirty else committed


def assert_v1_final_is_current(row, v1dir, locked_final, data, total,
                               locked_duration):
    """STALE-V1-FINAL GUARD — refuse the AUDIO LOCK on an out-of-date V1 MP4.

    WHY THIS EXISTS (2026-08-02, audit after row 25). The AUDIO LOCK copies the
    finished V1 MP4's AAC stream packet-for-packet. That is exactly right while
    the MP4 is the current render of the current narration — and silently,
    catastrophically wrong when it is not. Row 25's MP4 was rendered 2026-07-22;
    the ElevenLabs re-voice landed 2026-07-24 and the echo-delete sweep then
    removed `n1` and trimmed `n9`. Copying that stream would have shipped
    pre-REDO-ALL voices, re-inserted deliberately deleted narrator echoes, and
    thrown every caption 60+ s adrift — on a cut labelled done in the reviewer.

    Two independent tripwires, because either can fire alone:

      1. RECENCY. If any mp3 this build actually places was changed AFTER the
         MP4 was rendered, the MP4 cannot contain it. This catches a re-voice or
         a text trim that happens to leave the runtime nearly unchanged, which
         no duration check would ever see.
      2. RUNTIME. If the MP4's stream runs longer than the timeline summed from
         the mp3s on disk, it is carrying audio that is no longer in the build —
         deleted segments, an older longer take. A shortfall is treated more
         loosely (V1 finals routinely land a few tenths under the recomputed
         timeline because of trailing-silence trimming), but an EXCESS means
         extra words.

    The fix is never to re-render or edit V1 (hard protection #1): the build
    declares AUDIO_FROM_V1_SEGMENTS = True and the track is rebuilt from that
    build's own mp3s at the extract_beats offsets. The error says so.
    """
    fix = ("FIX: add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py. "
           "The narration is then rendered from the V1 build's OWN mp3s at the "
           "extract_beats offsets — nothing re-voiced, nothing re-timed, and V1 "
           "stays read-only.")
    final_t = content_time(locked_final)
    placed = [b["seg"] for b in data["beats"] if b["speaker"] != "silence"]
    placed.append(data["card"]["seg"])
    newer = []
    for seg in placed:
        mp3 = os.path.join(v1dir, "audio", f"{seg}.mp3")
        if not os.path.isfile(mp3):
            continue
        t = content_time(mp3)
        if t > final_t + 1.0:
            newer.append((seg, t))
    if newer:
        import datetime
        stamp = lambda t: datetime.datetime.fromtimestamp(t).isoformat(" ", "seconds")
        listed = ", ".join(f"{s} ({stamp(t)})" for s, t in sorted(
            newer, key=lambda x: -x[1])[:6])
        raise SystemExit(
            f"STALE V1 FINAL: row {row}'s {os.path.basename(locked_final)} was "
            f"rendered {stamp(final_t)}, but {len(newer)} of the {len(placed)} "
            f"mp3s it would be locking to are NEWER than that: {listed}. "
            f"Its audio stream predates the current narration, so copying it "
            f"would ship stale voices and/or deleted segments. {fix}")
    excess = locked_duration - total
    if excess > 0.75:
        raise SystemExit(
            f"STALE V1 FINAL: row {row}'s {os.path.basename(locked_final)} runs "
            f"{locked_duration:.3f}s but the timeline summed from the mp3s on "
            f"disk is {total:.3f}s — {excess:.3f}s of audio in that stream is not "
            f"in this build any more. {fix}")


def mbm_speakers_names(v1dir):
    """The speaker constants this build's own mbm_speakers module knows."""
    spec = importlib.util.spec_from_file_location(
        "mbm_speakers_probe", os.path.join(v1dir, "mbm_speakers.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return tuple(mod.ALL)


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

    # LEGACY SPEAKER MAP (2026-08-01). Builds made before the SPEAKER SYSTEM
    # (mbm_speakers) put the raw edge-tts VOICE NAME in SEGMENTS instead of a
    # speaker constant, so caption_filter's colour lookup raises KeyError on
    # them (row 15 died on 'en-US-AndrewNeural'). A V2 beat map may declare
    # SPEAKER_OVERRIDES = {"j1": "jesus", ...} to say who is actually talking;
    # anything else that is not already a known speaker falls back to narrator.
    overrides = _speaker_overrides(v2dir)
    text_fixes = _text_overrides(v2dir)
    known = set(mbm_speakers_names(v1dir))
    for b in data["beats"] + [data["card"]]:
        spk = b.get("speaker")
        if b["seg"] in overrides:
            b["speaker"] = overrides[b["seg"]]
        elif spk not in known and spk != "silence":
            b["speaker"] = "narrator"
        if b["seg"] in text_fixes:
            print(f"TEXT OVERRIDE {b['seg']}: caption text taken from the build's "
                  f"beats_v2.py (the V1 script disagrees with the shipped audio)")
            b["text"] = text_fixes[b["seg"]]
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
    # BACKUP CUTS ARE NOT THE AUTHORITY (2026-08-02, row 22). Three V1 builds keep
    # a pre-fix backup beside the shipped cut — build-22 has both
    # `matthew-18_unmerciful-servant.mp4` (225.033 s, the cut extract_beats
    # reproduces to the millisecond) and `...orig.mp4` (245.000 s, a stale earlier
    # render). Globbing every .mp4 made the AUDIO LOCK refuse to run at all. A
    # `.orig.mp4` / `.bak.mp4` / `.old.mp4` sibling is a backup by definition, so it
    # is excluded here rather than deleted — V1 stays read-only.
    if _audio_from_segments(v2dir):
        # STALE-V1-FINAL PATH (row 25). The V1 MP4 predates this build's current
        # narration, so the authoritative audio is rebuilt from the V1 mp3s at the
        # extract_beats offsets. See _audio_from_segments for why.
        locked_v1_name = None
        for f in sorted(os.listdir(v1dir)):
            if f.endswith(".mp4") and not f.endswith(
                    (".orig.mp4", ".bak.mp4", ".old.mp4", ".prev.mp4")):
                locked_v1_name = f
                break
        out_name = configured_output_name or locked_v1_name
        track = rebuild_audio_from_segments(v1dir, segs, data)
        locked_duration = duration_of(track)
        if abs(total - locked_duration) > 0.5:
            raise SystemExit(
                f"AUDIO REBUILD: timeline {total:.3f}s vs rebuilt track "
                f"{locked_duration:.3f}s")
        vcap = max(300, int(24.5 * 8000 / locked_duration) - 145)
        run([FF, "-y", "-i", os.path.join(segs, "video_silent.mp4"),
             "-i", track, "-map", "0:v:0", "-map", "1:a:0",
             "-c:v", "libx264", "-preset", "medium", "-crf", "19",
             "-maxrate", f"{vcap}k", "-bufsize", f"{2*vcap}k",
             "-pix_fmt", "yuv420p", "-r", str(FPS),
             "-c:a", "copy", "-movflags", "+faststart",
             "-t", f"{locked_duration:.6f}", out_name])
        if audio_stream_hash(out_name) != audio_stream_hash(track):
            raise SystemExit("AUDIO REBUILD: muxed track does not match the "
                             "rebuilt narration bit-for-bit")
        size = os.path.getsize(out_name) / 1e6
        print(f"AUDIO REBUILD PASS: {audio_stream_hash(out_name)}", flush=True)
        print(f"DONE {out_name}  {size:.1f} MB  {locked_duration:.1f}s", flush=True)
        return

    _BACKUP_MARKERS = (".orig.mp4", ".bak.mp4", ".old.mp4", ".prev.mp4")
    v1_mp4 = [f for f in os.listdir(v1dir)
              if f.endswith(".mp4") and not f.endswith(_BACKUP_MARKERS)]
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
            f"authoritative V1 final is {locked_duration:.3f}s. If the V1 MP4 is "
            f"simply out of date, set AUDIO_FROM_V1_SEGMENTS = True in this "
            f"row's beats_v2.py and the track is rebuilt from the V1 mp3s.")
    assert_v1_final_is_current(row, v1dir, locked_final, data, total,
                               locked_duration)
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
