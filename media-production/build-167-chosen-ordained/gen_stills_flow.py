#!/usr/bin/env python3
"""Generate #167's 8 stills via flow_driver.py (Nano Banana 2, 9:16, $0).
No Christ/God figure anywhere (the one who calls shown only as warm light from heaven, never
a dove), NO --ref. Shot bodies come from PROMPTS.md in order; outputs are build.py's S1..S8."""
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
    "s1-ordinary-lives.jpeg", "s2-chosen.jpeg", "s3-ordained.jpeg",
    "s4-sent-to-go.jpeg", "s5-bring-forth-fruit.jpeg", "s6-fruit-that-remains.jpeg",
    "s7-ask-and-receive.jpeg", "s8-called-by-name.jpeg",
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
print("ALL 167 STILLS GENERATED")
