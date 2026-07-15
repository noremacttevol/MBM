#!/usr/bin/env python3
"""Generate #159's 8 stills via flow_driver.py (Nano Banana 2, 9:16, $0).
Jesus IS shown (Good Shepherd). Shots whose body carries the JESUS LOCK v3 paragraph
are generated WITH the master face attached as --ref (JESUS-MASTER-REF/jesus-face.jpeg);
the 'REF: jesus-master-ref' marker line is stripped before the prompt is sent to Flow.
The two 'other fold' shots (s5, s6) have no Jesus and no --ref.
Optional arg: a substring; only shots whose filename contains it are generated."""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRIVER = HERE.parent / "flow_driver.py"
PROMPTS = HERE / "PROMPTS.md"
ASSETS = HERE / "assets"
REF = HERE.parent / "JESUS-MASTER-REF" / "jesus-face.jpeg"
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
    "s1-the-good-shepherd.jpeg", "s2-he-knows-his-sheep.jpeg", "s3-known-of-mine.jpeg",
    "s4-not-all-my-sheep.jpeg", "s5-a-far-off-fold.jpeg", "s6-they-shall-hear.jpeg",
    "s7-other-sheep.jpeg", "s8-one-fold-one-shepherd.jpeg",
]

only = sys.argv[1] if len(sys.argv) > 1 else None
text = PROMPTS.read_text(encoding="utf-8")
blocks = re.findall(r"^## [^\n]+\n(.+?)(?=\n## |\Z)", text, re.S | re.M)
assert len(blocks) == 8, f"expected 8 shots, got {len(blocks)}"

failed = []
for fn, raw in zip(FILENAMES, blocks):
    if only and only not in fn:
        continue
    out = ASSETS / fn
    if out.exists() and out.stat().st_size > 10000:
        print(f"skip {fn} (exists)", flush=True)
        continue
    is_jesus = "JESUS LOCK v3" in raw
    # strip the REF marker line(s) before sending to Flow
    body = "\n".join(ln for ln in raw.splitlines() if not ln.strip().lower().startswith("ref:"))
    body = " ".join(body.replace("[STILL STYLE BLOCK]", STYLE).split())
    cmd = ["python3", str(DRIVER), "gen", "--prompt", body, "--out", str(out)]
    if is_jesus:
        cmd += ["--ref", str(REF)]
    print(f"=== generating {fn} ({'JESUS+ref' if is_jesus else 'no-ref'}) ===", flush=True)
    r = subprocess.run(cmd)
    if not (r.returncode == 0 and out.exists()):
        failed.append(fn)
        print(f"  FAILED {fn}", flush=True)
if failed:
    sys.exit("FAILED: " + ", ".join(failed))
print("DONE (requested shots generated)")
