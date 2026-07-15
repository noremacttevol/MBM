#!/usr/bin/env python3
"""Generate #151's 8 stills via flow_driver.py (Nano Banana 2, 9:16, $0).
No Christ/Jesus figure anywhere in #151 (God shown only as light), so NO --ref.
Shot bodies come from PROMPTS.md in order; output filenames are build.py's S1..S8."""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRIVER = HERE.parent / "flow_driver.py"
PROMPTS = HERE / "PROMPTS.md"
ASSETS = HERE / "assets"
ASSETS.mkdir(exist_ok=True)

STYLE = (
    "Beautiful hand-painted 2D animation style, reverent and warm, like a classic "
    "illustrated storybook of scripture brought to life. Soft painterly brushstroke "
    "textures, glowing golden light, muted earth tones with warm gold highlights. "
    "First-century Judea. Sacred, hushed tone. Not photorealistic. No text or captions "
    "in the image. Historically modest clothing: rough-woven wool and linen in undyed "
    "earth colors. No modern objects."
)

FILENAMES = [
    "s1-lacking-wisdom.jpeg", "s2-many-voices.jpeg", "s3-the-quiet-place.jpeg",
    "s4-kneeling-to-ask.jpeg", "s5-given-liberally.jpeg", "s6-upbraideth-not.jpeg",
    "s7-ask-in-faith.jpeg", "s8-it-shall-be-given.jpeg",
]

text = PROMPTS.read_text(encoding="utf-8")
blocks = re.findall(r"^## [^\n]+\n(.+?)(?=\n## |\Z)", text, re.S | re.M)
bodies = [" ".join(b.replace("[STILL STYLE BLOCK]", STYLE).split()) for b in blocks]
assert len(bodies) == 8, f"expected 8 shots, got {len(bodies)}"

failed = []
for fn, body in zip(FILENAMES, bodies):
    out = ASSETS / fn
    if out.exists() and out.stat().st_size > 10000:
        print(f"skip {fn} (exists)", flush=True)
        continue
    print(f"=== generating {fn} ===", flush=True)
    r = subprocess.run(["python3", str(DRIVER), "gen", "--prompt", body, "--out", str(out)])
    if not (r.returncode == 0 and out.exists()):
        failed.append(fn)
        print(f"  FAILED {fn}", flush=True)
if failed:
    sys.exit("FAILED: " + ", ".join(failed))
print("ALL 151 STILLS GENERATED")
