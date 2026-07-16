#!/usr/bin/env python3
"""Generate #169's 8 stills via flow_driver.py (Nano Banana 2, 9:16, $0).
FACE-SHOWN: Jesus is depicted (s1-s7), locked by the byte-identical JESUS LOCK v3 TEXT in
each shot body. TEXT-ONLY lock — the 'REF: jesus-master-ref' marker line is stripped and NO
--ref is attached (attaching the master portrait makes Nano Banana echo the bust; the LOCK v3
text alone gives a face matching the master — QC each Jesus face against JESUS-MASTER-REF).
s8 has no Jesus figure. Optional arg: a filename substring to (re)generate just that shot."""
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
    "s1-comes-to-jordan.jpeg", "s2-john-hesitates.jpeg", "s3-fulfil-righteousness.jpeg",
    "s4-the-baptism.jpeg", "s5-heavens-open-dove.jpeg", "s6-voice-from-heaven.jpeg",
    "s7-godhead-distinct.jpeg", "s8-the-way-for-you.jpeg",
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
    # strip the REF marker line(s); TEXT-ONLY lock, never attach --ref
    body = "\n".join(ln for ln in raw.splitlines() if not ln.strip().lower().startswith("ref:"))
    body = " ".join(body.replace("[STILL STYLE BLOCK]", STYLE).split())
    print(f"=== generating {fn} ({'JESUS text-lock' if is_jesus else 'no-figure'}) ===", flush=True)
    r = subprocess.run(["python3", str(DRIVER), "gen", "--prompt", body, "--out", str(out)])
    if not (r.returncode == 0 and out.exists()):
        failed.append(fn)
        print(f"  FAILED {fn}", flush=True)
if failed:
    sys.exit("FAILED: " + ", ".join(failed))
print("ALL 169 STILLS GENERATED")
