#!/usr/bin/env python3
"""#2 AUDIO MAKER — voice the canonical transcripts from #1 (TRANSCRIPTS/*.json)
through ElevenLabs into each build's audio/ folder.

Runs at the media-production root and imports the root engine modules directly,
so it does NOT depend on the per-build make_narration.py copies. Reads the
{id, speaker, text} segments straight from the planner's JSON, which is the single
source of truth. Skips any build whose existing audio already matches the current
transcript (so re-runs only spend ElevenLabs characters on what actually changed).
"""
import concurrent.futures as cf
import glob
import json
import os
import re
import sys

from mbm_eleven import render_segment, eleven_spoken_text, _key

TDIR = sys.argv[1] if len(sys.argv) > 1 else "TRANSCRIPTS"
LOG = "AUDIO-RENDER.log"


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", "", s.lower())).strip()


def build_map():
    m = {}
    for d in glob.glob("build-*/"):
        mm = re.match(r"build-(\d+)-", d)
        if mm:
            m[int(mm.group(1))] = d.rstrip("/")
    return m


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


KEY = _key()
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


def voice_one(tf):
    """ALWAYS re-render from canonical. No text-match skipping — the only proof of
    a real ElevenLabs voice is 44100 Hz audio, so every clip is verified after."""
    d = json.load(open(tf))
    row, segs = d["row"], d["segments"]
    build = BUILDS.get(row)
    if not build:
        return f"NOBUILD {os.path.basename(tf)}"
    marker = f"{build}/.audio-eleven-done"
    # SKIP only if the build ALREADY has real ElevenLabs audio (every clip 44100 Hz,
    # non-trivial size) matching the current transcript. This is the credit-saver:
    # it is gated on actual sample rate, never on text alone.
    if all(os.path.exists(f"{build}/audio/{s['id']}.mp3")
           and _rate(f"{build}/audio/{s['id']}.mp3") == 44100
           and os.path.getsize(f"{build}/audio/{s['id']}.mp3") >= 2000
           and os.path.exists(f"{build}/audio/{s['id']}.timing.json")
           for s in segs):
        open(marker, "w").close()
        return f"SKIP {build} (already 44100 ElevenLabs)"
    if os.path.exists(marker):
        os.remove(marker)
    os.makedirs(f"{build}/audio", exist_ok=True)
    for f in glob.glob(f"{build}/audio/*"):
        os.remove(f)
    try:
        for seg in segs:
            out = f"{build}/audio/{seg['id']}.mp3"
            spoken = eleven_spoken_text(seg["text"])
            render_segment(spoken, seg["speaker"], out, key=KEY)
            r = _rate(out)
            sz = os.path.getsize(out)
            if r != 44100 or sz < 2000:
                return f"FAIL {build}  {seg['id']} bad audio rate={r} size={sz}"
        open(marker, "w").close()
        return f"OK   {build}  {len(segs)} clips @44100"
    except Exception as e:
        return f"FAIL {build}  {str(e)[:90]}"


if __name__ == "__main__":
    tfs = sorted(glob.glob(f"{TDIR}/*.json"))
    print(f"voicing {len(tfs)} transcripts -> build audio/ folders")
    ok = skip = fail = nob = 0
    with open(LOG, "a") as log:
        log.write(f"=== transcript voicing started ({len(tfs)} transcripts) ===\n")
        with cf.ThreadPoolExecutor(max_workers=6) as ex:
            for res in ex.map(voice_one, tfs):
                print(res)
                log.write(res + "\n"); log.flush()
                k = res.split()[0]
                ok += k == "OK"; skip += k == "SKIP"; fail += k == "FAIL"; nob += k == "NOBUILD"
        log.write(f"=== voicing finished  OK={ok} SKIP={skip} FAIL={fail} NOBUILD={nob} ===\n")
    print(f"\nOK={ok} SKIP={skip} FAIL={fail} NOBUILD={nob}")
