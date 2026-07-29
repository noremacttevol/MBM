#!/usr/bin/env python3
"""#2 AUDIO MAKER — voice the canonical transcripts from #1 (TRANSCRIPTS/*.json)
through ElevenLabs into each build's audio/ folder.

Runs at the media-production root and imports the root engine modules directly,
so it does NOT depend on the per-build make_narration.py copies. Reads the
{id, speaker, text} segments straight from the planner's JSON, which is the single
source of truth. Skips any build whose existing audio already matches the current
transcript (so re-runs only spend ElevenLabs characters on what actually changed).
"""
import argparse
import concurrent.futures as cf
import glob
import json
import os
import re
import shutil
import sys
import tempfile

from mbm_eleven import render_segment, eleven_spoken_text, _key
from corpus import canonical_builds

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "AUDIO-RENDER.log")


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", "", s.lower())).strip()


def build_map():
    """Map row -> the authoritative current build, never an archived duplicate."""
    return canonical_builds(HERE)


def audio_current(build, segments):
    """True iff every segment already has audio whose voiced text matches the
    current transcript (compared as the ElevenLabs spoken form)."""
    for seg in segments:
        tj = f"{build}/audio/{seg['id']}.timing.json"
        if not os.path.exists(tj):
            return False
        try:
            voiced = norm(" ".join(x["text"] for x in json.load(open(tj))))
        except Exception:
            return False
        if voiced != norm(eleven_spoken_text(seg["text"])):
            return False
    return True


BUILDS = build_map()


import subprocess


def _rate(f):
    try:
        return int(subprocess.run(
            ["ffprobe", "-v", "quiet", "-select_streams", "a:0",
             "-show_entries", "stream=sample_rate", "-of", "csv=p=0", f],
            capture_output=True, text=True).stdout.strip() or 0)
    except Exception:
        return 0


def voice_one(tf, *, key, force=False):
    """Render a complete canonical audio set, then swap it in atomically."""
    d = json.load(open(tf))
    row, segs = d["row"], d["segments"]
    build = BUILDS.get(row)
    if not build:
        return f"NOBUILD {os.path.basename(tf)}"
    marker = f"{build}/.audio-eleven-done"
    # A matching sample rate alone is not proof that the audio speaks the current
    # text.  Timing sidecars are the text receipt and must agree too.
    valid_existing = all(
        os.path.exists(f"{build}/audio/{s['id']}.mp3")
        and _rate(f"{build}/audio/{s['id']}.mp3") == 44100
        and os.path.getsize(f"{build}/audio/{s['id']}.mp3") >= 2000
        and os.path.exists(f"{build}/audio/{s['id']}.timing.json")
        for s in segs
    ) and audio_current(build, segs)
    if valid_existing and not force:
        open(marker, "w").close()
        return f"SKIP {build} (already 44100 ElevenLabs)"

    stage = tempfile.mkdtemp(prefix=".audio-stage-", dir=build)
    audio_dir = os.path.join(build, "audio")
    backup = os.path.join(build, f".audio-backup-{os.getpid()}")
    try:
        for seg in segs:
            out = os.path.join(stage, f"{seg['id']}.mp3")
            spoken = eleven_spoken_text(seg["text"])
            render_segment(spoken, seg["speaker"], out, key=key)
            r = _rate(out)
            sz = os.path.getsize(out)
            if r != 44100 or sz < 2000:
                return f"FAIL {build}  {seg['id']} bad audio rate={r} size={sz}"

        if os.path.exists(backup):
            shutil.rmtree(backup)
        if os.path.exists(audio_dir):
            os.replace(audio_dir, backup)
        try:
            os.replace(stage, audio_dir)
        except Exception:
            if os.path.exists(backup) and not os.path.exists(audio_dir):
                os.replace(backup, audio_dir)
            raise
        if os.path.exists(backup):
            shutil.rmtree(backup)
        open(marker, "w").close()
        return f"OK   {build}  {len(segs)} clips @44100"
    except Exception as e:
        return f"FAIL {build}  {str(e)[:90]}"
    finally:
        if os.path.exists(stage):
            shutil.rmtree(stage)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("transcripts", nargs="?", default="TRANSCRIPTS")
    parser.add_argument(
        "--rows",
        help="comma-separated row numbers; default is every transcript",
    )
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument(
        "--force",
        action="store_true",
        help="re-render selected rows even when existing text receipts match",
    )
    args = parser.parse_args()
    transcript_dir = (
        args.transcripts
        if os.path.isabs(args.transcripts)
        else os.path.join(HERE, args.transcripts)
    )
    selected = (
        {int(value) for value in args.rows.split(",") if value.strip()}
        if args.rows
        else None
    )
    tfs = []
    for tf in sorted(glob.glob(f"{transcript_dir}/*.json")):
        if selected is None:
            tfs.append(tf)
            continue
        try:
            if int(json.load(open(tf))["row"]) in selected:
                tfs.append(tf)
        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError):
            continue
    found_rows = {int(json.load(open(tf))["row"]) for tf in tfs}
    missing_rows = sorted((selected or set()) - found_rows)
    if missing_rows:
        print("missing transcript rows: " + ",".join(map(str, missing_rows)))
        raise SystemExit(2)

    key = _key()
    print(f"voicing {len(tfs)} transcripts -> build audio/ folders")
    ok = skip = fail = nob = 0
    with open(LOG, "a") as log:
        log.write(f"=== transcript voicing started ({len(tfs)} transcripts) ===\n")
        with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
            futures = [
                ex.submit(voice_one, tf, key=key, force=args.force) for tf in tfs
            ]
            for future in futures:
                res = future.result()
                print(res)
                log.write(res + "\n"); log.flush()
                k = res.split()[0]
                ok += k == "OK"; skip += k == "SKIP"; fail += k == "FAIL"; nob += k == "NOBUILD"
        log.write(f"=== voicing finished  OK={ok} SKIP={skip} FAIL={fail} NOBUILD={nob} ===\n")
    print(f"\nOK={ok} SKIP={skip} FAIL={fail} NOBUILD={nob}")
