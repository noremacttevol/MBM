#!/usr/bin/env python3
"""Surgical card-only rebuild: run the build's own main(), but skip ffmpeg
calls whose output is an already-rendered segs/*.mp4 — EXCEPT the card seg
and video_silent.mp4, which must re-render. Everything else (timing math,
audio mix, loudness, final mux) runs exactly as the build.py defines it."""
import importlib.util, os, sys

bdir = sys.argv[1]
os.chdir(bdir)
sys.path.insert(0, bdir)

spec = importlib.util.spec_from_file_location("bm", os.path.join(bdir, "build.py"))
bm = importlib.util.module_from_spec(spec)
# prevent __main__ guard from firing; we call main() ourselves
spec.loader.exec_module(bm)

S = bm.S
card_out = f"{S}/{bm.CARD}.mp4"
never_skip = {card_out, f"{S}/video_silent.mp4"}
real_run = bm.run
skipped = rendered = 0

def run_skip(cmd, *a, **kw):
    global skipped, rendered
    out = cmd[-1] if isinstance(cmd, (list, tuple)) else ""
    if (isinstance(out, str) and out.startswith(f"{S}/") and out.endswith(".mp4")
            and out not in never_skip and os.path.exists(out)):
        skipped += 1
        return
    rendered += 1
    return real_run(cmd, *a, **kw)

bm.run = run_skip
bm.main()
print(f"SURGICAL OK: {os.path.basename(bdir)} skipped={skipped} rendered={rendered}")
