#!/usr/bin/env python3
"""v2_prep_row.py — mechanical step B for any row. No judgment, no browser.

Cameron, 2026-07-29: *"just make all 3000 pictures don't worry about the making the
videos"* / *"dont stop do that to all 200 stories"*.

Authoring a beat map is judgment work and stays with the model. Everything AROUND it
is mechanical and was being redone by hand every row, which wasted the one resource
that actually matters here — time when Flow could be generating. This does the
mechanical half for one row or for a range:

  * make media-production-v2/build-NN-slug/
  * extract the V1 beat truth to beats.json (V1 stays read-only)
  * COPY (never move) the V1 audio/ plus the narration + caption scripts
  * report whether beats_v2.py still needs authoring

Usage:
    python3 media-production-v2/v2_prep_row.py 4
    python3 media-production-v2/v2_prep_row.py 4 40          # inclusive range
    python3 media-production-v2/v2_prep_row.py --status       # what still needs beats
"""
import argparse
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
V1 = os.path.join(ROOT, "media-production")
V2 = os.path.join(ROOT, "media-production-v2")
SCRIPTS = ("make_narration.py", "mbm_caption_timing.py", "mbm_speakers.py",
           "mbm_pronounce.py")


def v1_dir_for(row):
    """The V1 build folder for a row number, by its NN- prefix.

    Dup-numbered rows (128 famine/heart etc.) must resolve to the CANONICAL
    build, same as extract_beats.py — sorted()[0] silently picked the RETIRED
    story for row 128 (caught 2026-08-05)."""
    pre = f"build-{row:02d}-"
    hits = sorted(d for d in os.listdir(V1)
                  if d.startswith(pre) and os.path.isdir(os.path.join(V1, d)))
    if len(hits) > 1:
        from extract_beats import CANONICAL_BUILD_SLUGS
        want = CANONICAL_BUILD_SLUGS.get(row)
        if want:
            hits = [h for h in hits if h == f"{pre}{want}"] or hits
    return os.path.join(V1, hits[0]) if hits else None


def prep(row):
    src = v1_dir_for(row)
    if not src:
        return row, None, "no V1 build folder"
    slug = os.path.basename(src)
    dst = os.path.join(V2, slug)
    os.makedirs(dst, exist_ok=True)

    # Audio is COPIED, never moved — V1 is read-only and that is a hard protection.
    if not os.path.isdir(os.path.join(dst, "audio")):
        if not os.path.isdir(os.path.join(src, "audio")):
            return row, slug, "V1 build has no audio/"
        shutil.copytree(os.path.join(src, "audio"), os.path.join(dst, "audio"))
    for s in SCRIPTS:
        a, b = os.path.join(src, s), os.path.join(dst, s)
        if os.path.exists(a) and not os.path.exists(b):
            shutil.copy2(a, b)

    beats_json = os.path.join(dst, "beats.json")
    if not os.path.exists(beats_json):
        r = subprocess.run(
            [sys.executable, os.path.join(HERE, "extract_beats.py"),
             str(row), "--json", beats_json],
            capture_output=True, text=True)
        if r.returncode != 0:
            tail = (r.stderr or r.stdout).strip().splitlines()[-1:] or ["failed"]
            return row, slug, f"extract_beats failed: {tail[0][:90]}"

    has_beats = os.path.exists(os.path.join(dst, "beats_v2.py"))
    n = len([f for f in os.listdir(os.path.join(dst, "assets"))
             if f.endswith(".jpeg")]) if os.path.isdir(os.path.join(dst, "assets")) else 0
    return row, slug, ("READY" if has_beats else "NEEDS beats_v2.py") + f" · {n} stills"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("first", nargs="?", type=int)
    ap.add_argument("last", nargs="?", type=int)
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args()

    if a.status or a.first is None:
        rows = range(1, 212)
        need, ready, missing = [], [], []
        for row in rows:
            src = v1_dir_for(row)
            if not src:
                continue
            slug = os.path.basename(src)
            d = os.path.join(V2, slug)
            if not os.path.isdir(d):
                missing.append(row)
            elif os.path.exists(os.path.join(d, "beats_v2.py")):
                ready.append(row)
            else:
                need.append(row)
        print(f"prepped + authored (READY to generate): {len(ready)}  {ready[:20]}")
        print(f"prepped, still NEEDS beats_v2.py:       {len(need)}  {need[:20]}")
        print(f"not prepped yet:                        {len(missing)}")
        return

    last = a.last or a.first
    for row in range(a.first, last + 1):
        r, slug, msg = prep(row)
        print(f"row {r:3d}  {slug or '-':32s}  {msg}", flush=True)


if __name__ == "__main__":
    main()
