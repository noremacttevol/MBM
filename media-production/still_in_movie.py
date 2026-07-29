#!/usr/bin/env python3
"""still_in_movie.py — is this repainted still ACTUALLY inside the finished video?

Answers the question by LOOKING AT THE VIDEO, not by trusting git.

Why this exists (2026-07-28, and it is the whole point):
`picture_render_status.py` compared the commit that last touched the mp4 against the
commit that last touched the still, and reported "0 stranded". That was WRONG. Video #112
was re-rendered and committed at 02:10, well after the 01:28 picture fix — so by commit
order the fix was in. Extracting the actual frame showed the movie still carried the
07-23 version of that still: FIVE DAYS and TWO fixes stale. The rendering machine had
pulled once at the start of its batch, so its working tree was old even though its commit
was new. **A commit timestamp tells you when a file was recorded, never what was on disk
when ffmpeg ran.** Only the pixels are evidence.

Method: sample frames across the video, reduce each to a coarse colour signature, and ask
whether the still's own signature matches any sampled frame. Signatures are HSV histograms
plus a heavily downsampled greyscale, both of which survive the Ken Burns zoom/pan that
makes exact frame matching useless. A still that appears in the movie scores high against
the frames covering its beat; a still that was replaced scores low against every frame.

Usage:
  python3 still_in_movie.py --dir build-112-beatitudes          # one build, all wired stills
  python3 still_in_movie.py --dir build-112-beatitudes --shot s10-the-upside-down-kingdom
  python3 still_in_movie.py --builds build-90-washing-feet,build-112-beatitudes
  python3 still_in_movie.py --at-risk    # every build whose stills are newer than its mp4
"""
import argparse
import glob
import os
import re
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image

STEP = 2.0        # seconds between sampled frames
MATCH = 0.86      # correlation above which we call it the same picture

# Calibrated on build-112, where the movie provably carried an OLD version of s10:
#   colour-histogram signature -> present stills 0.954-0.994, the ABSENT one 0.937.
#     A 0.017 margin. Useless: every still in this library is "cream robe, earth-toned
#     crowd, golden hour", so colour says almost nothing about which picture it is.
#   grey composition signature -> present stills 0.899-0.990, the ABSENT one 0.792.
#     A 0.107 margin, because it keys on WHERE the figures are, which is what actually
#     differs between two versions of the same shot.
# Hence greyscale only. Colour histograms were removed, not merely down-weighted.


def sh(*a):
    return subprocess.run(a, capture_output=True, text=True).stdout.strip()


def duration(mp4):
    out = sh("ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", mp4)
    try:
        return float(out)
    except ValueError:
        return 0.0


def signature(img, n=24):
    """Zero-mean, L2-normalised low-res greyscale — a layout fingerprint.

    Zero-mean kills the overall brightness difference the Ken Burns fade introduces;
    the low resolution absorbs its zoom and pan. What survives is roughly where the
    dark and light masses sit, which is exactly what changes when a shot is repainted.
    """
    g = np.asarray(img.convert("L").resize((n, int(n * 1.78)), Image.BILINEAR),
                   dtype=np.float32)
    v = (g - g.mean()).ravel()
    norm = np.linalg.norm(v)
    return v / norm if norm else v


def frame_sigs(mp4, tmp):
    """One signature per sampled second-offset. Single ffmpeg pass, fps filter."""
    dur = duration(mp4)
    if dur <= 0:
        return [], 0.0
    pat = os.path.join(tmp, "f%05d.jpg")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp4,
                    "-vf", f"fps=1/{STEP},scale=160:-1", "-q:v", "6", pat],
                   capture_output=True)
    out = []
    for f in sorted(glob.glob(os.path.join(tmp, "f*.jpg"))):
        try:
            out.append(signature(Image.open(f)))
        except Exception:
            pass
    return out, dur


def check(build, only_shot=None):
    mp4s = glob.glob(os.path.join(build, "*.mp4"))
    bp = os.path.join(build, "build.py")
    if not mp4s or not os.path.exists(bp):
        return []
    src = open(bp, encoding="utf-8", errors="ignore").read()
    stills = sorted(glob.glob(os.path.join(build, "assets", "*.jpeg"))
                    + glob.glob(os.path.join(build, "assets", "*.jpg")))
    wanted = []
    for f in stills:
        slug = os.path.splitext(os.path.basename(f))[0]
        if slug not in src:
            continue                      # not wired into BEATS; cannot appear
        if only_shot and slug != only_shot:
            continue
        wanted.append((slug, f))
    if not wanted:
        return []

    with tempfile.TemporaryDirectory() as tmp:
        fsigs, dur = frame_sigs(mp4s[0], tmp)
        if not fsigs:
            return []
        F = np.stack(fsigs)
        rows = []
        for slug, path in wanted:
            try:
                s = signature(Image.open(path))
            except Exception:
                continue
            scores = F @ s
            best = float(scores.max())
            rows.append((slug, best, best >= MATCH, float(scores.argmax()) * STEP, dur))
    return rows


def at_risk_builds():
    """Builds where a wired still's last commit is after the mp4's — the candidates."""
    def lastc(paths):
        return sh("git", "log", "-1", "--format=%H", "--", *paths)
    out = []
    for d in sorted(glob.glob("build-*")):
        mp4 = glob.glob(os.path.join(d, "*.mp4"))
        bp = os.path.join(d, "build.py")
        if not mp4 or not os.path.exists(bp):
            continue
        mc = lastc(mp4)
        src = open(bp, encoding="utf-8", errors="ignore").read()
        for f in glob.glob(os.path.join(d, "assets", "*.jpeg")):
            slug = os.path.splitext(os.path.basename(f))[0]
            if slug not in src:
                continue
            ac = lastc([f])
            if ac and mc and ac != mc and subprocess.run(
                    ["git", "merge-base", "--is-ancestor", mc, ac],
                    capture_output=True).returncode == 0:
                out.append(d)
                break
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir")
    ap.add_argument("--builds")
    ap.add_argument("--shot")
    ap.add_argument("--at-risk", action="store_true")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    if args.dir:
        builds = [args.dir]
    elif args.builds:
        builds = args.builds.split(",")
    elif args.at_risk:
        builds = at_risk_builds()
        print(f"{len(builds)} build(s) whose stills are newer than their mp4 by git; "
              f"now checking the PIXELS\n")
    elif args.all:
        builds = sorted(d for d in glob.glob("build-*") if os.path.isdir(d))
    else:
        ap.error("give --dir, --builds, --at-risk or --all")

    missing = []
    for b in builds:
        rows = check(b, args.shot)
        if not rows:
            continue
        bad = [r for r in rows if not r[2]]
        tag = "OK" if not bad else f"{len(bad)} STALE"
        print(f"{b:<42} {tag}")
        for slug, score, ok, at, dur in rows:
            if not ok:
                print(f"    NOT IN MOVIE  {slug:<34} best match {score:.2f}")
                missing.append((b, slug))
    print("\n" + "=" * 72)
    if missing:
        print(f"{len(missing)} repainted still(s) are NOT in their finished video.")
        print("Each needs its build re-rendered (coordinate first — never render a build "
              "another machine is rendering):")
        for b, s in missing:
            print(f"  cd {b} && python3 build.py     # {s}")
    else:
        print("Every wired still was found in its movie.")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
