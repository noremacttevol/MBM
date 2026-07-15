#!/usr/bin/env python3
"""gen_shots.py — generate specific stills of a build via flow_driver.py ($0 Flow).

Reads a build's PROMPTS.md, prepends the Master Style Block, and generates the named
shots. Attaches the Jesus master face as --ref for every shot listed in --jesus.
Skips shots whose jpeg already exists (unless --force). QCs nothing — YOU still Read
each saved jpeg to verify face-match, only-Jesus-cream, single-frame (no triptych),
and portrait 768x1376 (a ~421KB jpeg identical to jesus-face.jpeg means the ref got
downloaded instead of the scene — reroll).

Usage (from repo root):
  python media-production/gen_shots.py --dir media-production/build-NN-slug \\
      --shots s3-slug,s4-slug,... [--jesus s3-slug,s4-slug] [--force]

The --ref master face is media-production/JESUS-MASTER-REF/jesus-face.jpeg.
Windows: python is `python`. Flow must be logged in (flow_driver.py check).
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRIVER = HERE / "flow_driver.py"
REF = HERE / "JESUS-MASTER-REF" / "jesus-face.jpeg"

STYLE = ("Beautiful hand-painted 2D animation style, reverent and warm, like a classic "
         "illustrated storybook of scripture brought to life. Soft painterly brushstroke "
         "textures, glowing golden light, muted earth tones with warm gold highlights. "
         "First-century Judea. Sacred, hushed tone. Not photorealistic. No text or captions "
         "in the image. Historically modest clothing: rough-woven wool and linen in undyed "
         "earth colors. No modern objects. ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--shots", required=True, help="comma-separated slugs (## headers)")
    ap.add_argument("--jesus", default="", help="comma-separated slugs to attach --ref")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    build = Path(a.dir)
    text = (build / "PROMPTS.md").read_text(encoding="utf-8")
    blocks = re.split(r"^## ", text, flags=re.M)[1:]
    prompts = {}
    for b in blocks:
        slug = b.splitlines()[0].split(" —")[0].strip()
        line = next((l for l in b.splitlines()
                     if l.startswith("[STILL STYLE BLOCK]")), None)
        if line:
            prompts[slug] = STYLE + line.replace("[STILL STYLE BLOCK] ", "")

    want = [s.strip() for s in a.shots.split(",") if s.strip()]
    jesus = {s.strip() for s in a.jesus.split(",") if s.strip()}
    for slug in want:
        if slug not in prompts:
            print(f"!! {slug} not found in PROMPTS.md — skipping"); continue
        out = build / "assets" / f"{slug}.jpeg"
        if out.exists() and not a.force:
            print(f"skip {slug} (exists)"); continue
        if out.exists():
            out.unlink()
        cmd = [sys.executable, str(DRIVER), "gen", "--prompt", prompts[slug],
               "--out", str(out)]
        if slug in jesus:
            cmd += ["--ref", str(REF)]
        print(f"\n##### {slug} ({'JESUS +ref' if slug in jesus else 'no ref'}) #####",
              flush=True)
        for attempt in range(1, 4):
            r = subprocess.run(cmd)
            if r.returncode == 0 and out.exists():
                print(f"##### {slug} OK ({out.stat().st_size//1024}KB) #####", flush=True)
                break
            print(f"##### {slug} attempt {attempt} failed #####", flush=True)
        else:
            print(f"##### {slug} GAVE UP #####", flush=True)
    print("\nGEN_SHOTS DONE", flush=True)


if __name__ == "__main__":
    main()
