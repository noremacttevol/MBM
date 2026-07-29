#!/usr/bin/env python3
"""FIND what's newly made and needs redoing. For every build, compare — ON
origin/main (what the reviewer serves) — the newest commit time of its INPUTS
(assets/ stills from #3, audio/ from #2, PROMPTS.md + make_narration.py from #1)
against the commit time of its finished .mp4. If any input is newer than the
video, the video on the board is STALE and #4 must rebuild it.

Run `git fetch origin` first. Usage:
  python3 media-production/stale_videos.py          # human summary
  python3 media-production/stale_videos.py --nums   # just the stale build numbers
"""
import glob, os, re, subprocess, sys

MP = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(MP)
REF = "origin/main"

def ctime(path):
    """last commit unix-time of a path on REF (0 if not tracked there)."""
    out = subprocess.run(["git", "log", "-1", "--format=%ct", REF, "--", path],
                         cwd=REPO, capture_output=True, text=True).stdout.strip()
    return int(out) if out else 0

def newest_ctime(paths):
    return max([ctime(p) for p in paths] + [0])

# list build dirs as they exist on origin (not just local)
tree = subprocess.run(["git", "ls-tree", "-r", "--name-only", REF, "--", "media-production"],
                      cwd=REPO, capture_output=True, text=True).stdout.splitlines()
builds = {}   # num -> {dir, mp4}
for path in tree:
    m = re.match(r"(media-production/build-(\d+)-[^/]+)/[0-9a-z]+-\d+_[^/]+\.mp4$", path)
    if m and "/segs/" not in path and "/assets/" not in path and "/archive/" not in path:
        builds.setdefault(int(m.group(2)), {})["mp4"] = path
        builds[int(m.group(2))]["dir"] = m.group(1)

stale = []
for num in sorted(builds):
    b = builds[num]
    d, mp4 = b.get("dir"), b.get("mp4")
    if not mp4: continue
    vid_t = ctime(mp4)
    in_t = newest_ctime([f"{d}/assets", f"{d}/audio", f"{d}/PROMPTS.md", f"{d}/make_narration.py"])
    if in_t > vid_t:
        stale.append((num, d, in_t - vid_t))

if "--nums" in sys.argv:
    print(" ".join(str(n) for n, _, _ in stale)); sys.exit(0)

print(f"STALE videos (inputs newer than the video on the board): {len(stale)}\n")
for num, d, lag in sorted(stale, key=lambda x: -x[2]):
    days = lag / 86400
    print(f"  #{num:<3} {os.path.basename(d):40} inputs {days:5.1f} days newer than the video")
print(f"\nThese {len(stale)} need #4 to rebuild + ship so the board shows the current work.")
