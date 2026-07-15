#!/usr/bin/env python3
"""Generate #157's 8 stills via flow_driver.py (Nano Banana 2, 9:16, $0).
No Christ/Jesus figure anywhere (God's marvellous work shown as light), NO --ref.
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
    "s1-isaiah-prophesies.jpeg", "s2-the-sealed-book.jpeg", "s3-the-learned-cannot.jpeg",
    "s4-the-unlearned.jpeg", "s5-hearts-far-off.jpeg", "s6-wisdom-runs-dry.jpeg",
    "s7-a-marvellous-work.jpeg", "s8-the-wonder-received.jpeg",
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
print("ALL 157 STILLS GENERATED")
