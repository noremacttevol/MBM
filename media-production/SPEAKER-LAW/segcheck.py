#!/usr/bin/env python3
"""Per-SEGMENT color verification — exact, no timeline math.

verify_colors.py probes the final mp4 at times computed from a model of the
build's pacing; builds with custom holds drift and false-alarm. But every build
keeps its per-segment renders in segs/<id>.mp4, and the caption color is baked
into those. So: for every non-narrator segment in the plan, scan THAT segment's
own file for its declared color. A miss here is a real violation, not drift.

Usage: python3 segcheck.py [build ...]   (default: every shipped build in batch-log)
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MP = os.path.dirname(HERE)

TARGET = {
    "jesus":     (0xEE, 0x33, 0x22),
    "god":       (0x5B, 0xE3, 0x8B),
    "scripture": (0x8F, 0xDC, 0xFF),
    "woman":     (0xFF, 0x9E, 0xC7),
}


def seg_has_color(path, tgt, tol=40, need=300):
    from PIL import Image
    try:
        d = float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip())
    except ValueError:
        return None, "unreadable"
    t, best = 0.35, 0
    while t < d:
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.2f}",
                        "-i", path, "-frames:v", "1", "/tmp/_segchk.png"],
                       capture_output=True)
        try:
            im = Image.open("/tmp/_segchk.png").convert("RGB")
        except Exception:
            t += 0.6
            continue
        w, h = im.size
        band = im.crop((0, int(h * 0.72), w, h))
        hits = sum(1 for p in band.getdata()
                   if all(abs(a - b) <= tol for a, b in zip(p, tgt)))
        best = max(best, hits)
        if best >= need:
            return True, best
        t += 0.6
    return False, best


def check(build):
    plan_p = os.path.join(HERE, "plans", f"{build}.json")
    if not os.path.exists(plan_p):
        return None
    plan = json.load(open(plan_p))
    misses = []
    for s in plan["segments"]:
        sp = s["speaker"]
        if sp == "narrator" or not s.get("text", "").strip():
            continue
        segdir = os.path.join(MP, build, "segs")
        segf = os.path.join(segdir, f"{s['id']}.mp4")
        if os.path.exists(segf):
            parts = [segf]
        else:
            # a beat spanning several stills renders as <id>a.mp4, <id>b.mp4, ...
            parts = sorted(
                os.path.join(segdir, f) for f in os.listdir(segdir)
                if f.endswith(".mp4") and f[:-4].rstrip("abcdefgh") == s["id"]
                and f[:-4] != s["id"])
        if not parts:
            misses.append((s["id"], sp, "NO-SEG-FILE"))
            continue
        for pf in parts:
            ok, detail = seg_has_color(pf, TARGET[sp])
            if not ok:
                misses.append((s["id"], sp,
                               f"{os.path.basename(pf)} max-hits={detail}"))
    return misses


def main():
    names = sys.argv[1:]
    if not names:
        d = json.load(open(os.path.join(HERE, "batch-log.json")))
        names = sorted(k for k, v in d.items() if v.get("status") == "shipped")
    bad = 0
    for b in names:
        m = check(b)
        if m is None:
            print(f"{b}: no plan — skipped")
            continue
        if m:
            bad += 1
            print(f"{b}: VIOLATION — {m}")
        else:
            print(f"{b}: ok")
    print(f"\n{len(names) - bad}/{len(names)} builds pass per-segment color check")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
