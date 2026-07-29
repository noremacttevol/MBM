#!/usr/bin/env python3
"""Build small review proxies so the whole library can actually reach the board.

The masters are ~20 MB each. 199 of them is 3.3 GB, and `firebase deploy` dies on
that with "retries exhausted ... Converting circular structure to JSON". A 601 MB
deploy of 30 videos succeeds, so the limit is payload size, not the mechanism.

These proxies are 608x1080 / CRF 33 / 56k audio — about 4 MB each, ~800 MB for the
set. Verified on a real frame: the caption stays crisp and the speaker colour
reads true, which is the entire point of the review board. The masters in
media-production/ are untouched and remain what actually ships.

Runs niced and in parallel so it does not starve the render queue.
"""
import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MP = os.path.dirname(HERE)
REPO = os.path.dirname(MP)
DEST = os.path.join(REPO, "site", "story-videos")
sys.path.insert(0, HERE)
import migrate  # noqa: E402

WIDTH, CRF, ABR = 608, 33, "56k"


def row_of(build):
    m = re.match(r"build-(\d+)-", build)
    return int(m.group(1)) if m else None


def one(job):
    build, row = job
    name = migrate.output_mp4(os.path.join(MP, build))
    if not name:
        return (row, None, "no mp4")
    src = os.path.join(MP, build, name)
    dst = os.path.join(DEST, f"{row}.mp4")
    # Deliberately NOT an mtime check. The destination may already hold a
    # full-size master that was copied here earlier, and a copy's mtime is NEWER
    # than the source it came from — an mtime test calls that "current" and
    # leaves a 20MB file in the one folder that has to fit inside a deploy.
    # Size is the honest test: anything much over the proxy budget is not a proxy.
    if os.path.exists(dst) and os.path.getsize(dst) < 8_000_000:
        return (row, os.path.getsize(dst), "current")
    tmp = dst + ".tmp.mp4"
    r = subprocess.run(
        ["nice", "-n", "15", "ffmpeg", "-y", "-v", "error", "-i", src,
         "-vf", f"scale={WIDTH}:-2", "-c:v", "libx264", "-preset", "veryfast",
         "-crf", str(CRF), "-c:a", "aac", "-b:a", ABR,
         "-movflags", "+faststart", tmp], capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(tmp):
        return (row, None, (r.stderr or "")[-120:])
    os.replace(tmp, dst)          # atomic: a half-encoded file is never served
    return (row, os.path.getsize(dst), "built")


def main():
    log = json.load(open(os.path.join(HERE, "batch-log.json")))
    jobs = []
    for b, v in sorted(log.items()):
        if v.get("status") != "shipped":
            continue
        row = row_of(b)
        if row:
            jobs.append((b, row))
    os.makedirs(DEST, exist_ok=True)
    print(f"{len(jobs)} proxies to build", flush=True)

    built = fail = 0
    total = 0
    rows = []
    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        for row, size, note in ex.map(one, jobs):
            if size is None:
                fail += 1
                print(f"  FAIL row {row}: {note}", flush=True)
                continue
            rows.append(row)
            total += size
            if note == "built":
                built += 1
                if built % 25 == 0:
                    print(f"  {built} built ({total/1e6:.0f} MB so far)", flush=True)

    listp = os.path.join(DEST, "SERVE-LOCAL.txt")
    header = ["# Served from Firebase because the git push is blocked "
              "(38GB repo -> HTTP 500).",
              "# These are REVIEW PROXIES (608px, ~4MB). Masters stay in "
              "media-production/.",
              "# Remove a number once its commit lands on GitHub."]
    tmp = listp + ".tmp"
    with open(tmp, "w") as f:
        f.write("\n".join(header + [str(n) for n in sorted(set(rows))]) + "\n")
    os.replace(tmp, listp)

    print(f"\nbuilt {built}, reused {len(rows)-built}, failed {fail}")
    print(f"folder total: {total/1e9:.2f} GB across {len(rows)} videos")


if __name__ == "__main__":
    main()
