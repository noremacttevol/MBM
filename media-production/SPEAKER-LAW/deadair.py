#!/usr/bin/env python3
"""Trailing dead air per delivered mp4 (silencedetect, audio-only).

Trailing dead air = video duration minus the moment the last audible sound stops.
The final silencedetect interval runs to EOF, so we detect that case explicitly.
"""
import concurrent.futures as cf
import glob
import json
import os
import re
import statistics
import subprocess

MP = os.path.expanduser("~/Desktop/MBM/media-production")


def measure(d, name=None):
    """Measure one build's output. `name` pins WHICH mp4 — four builds carry a
    stale second one and picking by glob order watches the wrong file."""
    if name:
        p = os.path.join(d, name)
        if not os.path.exists(p):
            return None
    else:
        v = sorted(glob.glob(os.path.join(d, "*.mp4")))
        if not v:
            return None
        p = v[0]
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", p], capture_output=True, text=True)
    try:
        total = float(r.stdout.strip())
    except ValueError:
        return None
    s = subprocess.run(["ffmpeg", "-v", "info", "-nostats", "-vn", "-i", p, "-af",
                        "silencedetect=noise=-50dB:d=0.6", "-f", "null", "-"],
                       capture_output=True, text=True)
    starts = [float(m) for m in re.findall(r"silence_start: ([0-9.]+)", s.stderr)]
    ends = [float(m) for m in re.findall(r"silence_end: ([0-9.]+)", s.stderr)]
    trailing = 0.0
    if starts:
        last_s = starts[-1]
        last_e = ends[-1] if ends else None
        # the final silence runs to EOF if nothing ends after it, or it ends at EOF
        if last_e is None or last_e < last_s or (total - last_e) < 0.20:
            trailing = total - last_s
    return dict(build=os.path.basename(d), mp4=os.path.basename(p),
                total=round(total, 2), trailing=round(trailing, 2))


def main():
    dirs = [d for d in sorted(glob.glob(f"{MP}/build-*"))
            if os.path.isfile(os.path.join(d, "build.py"))]
    res = []
    with cf.ThreadPoolExecutor(max_workers=3) as ex:
        for r in ex.map(measure, dirs):
            if r:
                res.append(r)
    tmp = "deadair.json.tmp"
    with open(tmp, "w") as f:
        json.dump(res, f, indent=1)
    os.replace(tmp, "deadair.json")

    o3 = [r for r in res if r["trailing"] > 3.0]
    o15 = [r for r in res if 1.5 < r["trailing"] <= 3.0]
    ok = [r for r in res if r["trailing"] <= 1.5]
    print(f"measured {len(res)} videos")
    print(f"  >3.0s   MUST FIX    : {len(o3)}")
    print(f"  1.5-3.0s tolerance  : {len(o15)}")
    print(f"  <=1.5s  leave alone : {len(ok)}")
    print(f"  median trailing     : {statistics.median(r['trailing'] for r in res):.2f}s")
    print(f"  total runtime       : {sum(r['total'] for r in res)/60:.0f} min across 200")
    print("\nworst 20:")
    for r in sorted(res, key=lambda x: -x["trailing"])[:20]:
        print(f"  {r['trailing']:6.2f}s of {r['total']:6.1f}s   {r['build']}")


if __name__ == "__main__":
    main()
