#!/usr/bin/env python3
"""picture_render_status.py — is every repainted still actually inside its video yet?

Cameron, 2026-07-28: "there is another session fixing the voices so we need to make sure
we have all the newest versions of pictures for the session to work on the correct videos
that are most updated."

Two lanes run at once. The PICTURE lane repaints stills. The VOICE / REDO-ALL lane
re-renders each video with the new narration — and a re-render is also the only thing that
carries a repainted still into the movie. So the lanes must not cross:

  * a still repainted BEFORE its video is re-rendered  -> free ride, the sweep carries it
  * a still repainted AFTER  its video is re-rendered  -> STRANDED, needs a deliberate
    rebuild or Cameron keeps seeing the old picture

This reports which case every still is in. It reads GIT HISTORY, never file mtimes —
mtimes are reset by every checkout, so on a second machine they are meaningless.

It also splits on whether the still is WIRED into build.py. An unwired still (new coverage
art, `sNb-...`) will not appear even if you do rebuild; it needs the assembly session to
add it to BEATS first. Reporting those as "stranded fixes" would send someone rebuilding
for nothing.

Usage:
  python3 picture_render_status.py            # full report
  python3 picture_render_status.py --strict   # exit 1 if any WIRED fix is stranded
"""
import argparse
import glob
import os
import re
import subprocess
import sys


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True).stdout.strip()


def last_commit(paths):
    return git("log", "-1", "--format=%H", "--", *paths)


def strictly_after(a, b):
    """True if commit a comes after commit b in this (linear, rebase-based) history.
    Ancestry, not dates: a rebase rewrites committer dates but never reorders."""
    if not a or not b or a == b:
        return False
    return subprocess.run(["git", "merge-base", "--is-ancestor", b, a],
                          capture_output=True).returncode == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any wired fix is stranded")
    args = ap.parse_args()

    redone = {int(n) for n in re.findall(
        r"REDO #(\d+)", git("log", "--format=%s", "--grep=^REDO #"))}

    wired_ok, wired_stranded, unwired = [], [], []
    for d in sorted(glob.glob("build-*")):
        mp4 = glob.glob(os.path.join(d, "*.mp4"))
        bp = os.path.join(d, "build.py")
        if not mp4 or not os.path.exists(bp):
            continue
        src = open(bp, encoding="utf-8", errors="ignore").read()
        mp4_commit = last_commit(mp4)
        m = re.match(r"build-(\d+)", d)
        num = int(m.group(1)) if m else -1
        for f in sorted(glob.glob(os.path.join(d, "assets", "*.jpeg"))
                        + glob.glob(os.path.join(d, "assets", "*.jpg"))):
            if not strictly_after(last_commit([f]), mp4_commit):
                continue
            slug = os.path.splitext(os.path.basename(f))[0]
            row = (d, slug)
            if slug not in src:
                unwired.append(row + (num in redone,))
            elif num in redone:
                wired_stranded.append(row)
            else:
                wired_ok.append(row)

    def dump(title, rows, note):
        print(f"\n{title}\n{'-' * len(title)}")
        if not rows:
            print("  (none)")
        by = {}
        for r in rows:
            by.setdefault(r[0], []).append(r[1])
        for d in sorted(by):
            print(f"  {d:<42} {', '.join(sorted(by[d]))}")
        if rows:
            print(f"  -> {len(rows)} still(s) in {len(by)} video(s). {note}")

    dump("A. FIXES THAT WILL LAND BY THEMSELVES", wired_ok,
         "The voice/REDO sweep has not reached these videos yet; when it renders them "
         "it carries these pictures in. Do nothing.")
    dump("B. STRANDED FIXES — REBUILD REQUIRED", wired_stranded,
         "The sweep ALREADY re-rendered these videos, so these pictures will never appear "
         "on their own. Someone must run build.py on each.")
    dump("C. NEW ART NOT WIRED INTO build.py", [(d, s) for d, s, _ in unwired],
         "Rebuilding will NOT show these — the assembly session must add them to BEATS "
         "first. Not a picture-lane problem.")

    print("\n" + "=" * 72)
    print(f"stranded fixes needing a deliberate rebuild: {len(wired_stranded)}")
    print("NOTE for whoever is rendering: `git pull --rebase` immediately before each "
          "build, not once at the start of the batch. The picture lane pushes fixes "
          "continuously, and a stale checkout re-renders the OLD picture and silently "
          "re-strands it.")
    return 1 if (args.strict and wired_stranded) else 0


if __name__ == "__main__":
    sys.exit(main())
