#!/usr/bin/env python3
"""Generate #170's 8 stills via flow_driver.py (Nano Banana 2, 9:16, $0).
No Christ/God figure anywhere (his presence at the table shown only as warm light; the bread
and cup are the emblems), NO --ref. Shot bodies from PROMPTS.md in order; outputs = build.py's S1..S8."""
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
    "s1-upper-room.jpeg", "s2-the-bread.jpeg", "s3-the-cup.jpeg",
    "s4-in-remembrance.jpeg", "s5-till-he-come.jpeg", "s6-examine-yourself.jpeg",
    "s7-covenant-renewed.jpeg", "s8-a-place-for-you.jpeg",
]

text = PROMPTS.read_text(encoding="utf-8")
blocks = re.findall(r"^## [^\n]+\n(.+?)(?=\n## |\Z)", text, re.S | re.M)
bodies = [" ".join(b.replace("[STILL STYLE BLOCK]", STYLE).split()) for b in blocks]
assert len(bodies) == 8, f"expected 8 shots, got {len(bodies)}"

only = sys.argv[1] if len(sys.argv) > 1 else None
failed = []
for fn, body in zip(FILENAMES, bodies):
    if only and only not in fn:
        continue
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
print("ALL 170 STILLS GENERATED")
