#!/usr/bin/env python3
"""gen_candidates.py — generate the 3 Jesus master-face candidate portraits.

BOOTSTRAP helper (FACTORY-ORDERS). Reads the three prompt paragraphs from
JESUS-MASTER-REF/candidates/CANDIDATE-PROMPTS.md and generates one bust portrait
each via flow_driver.py (Nano Banana 2, $0). No --ref: these DEFINE the face.

Preflight: `python media-production/flow_driver.py check` must print logged_in=True.
Run from repo root:  python media-production/gen_candidates.py
Then push, and ask Cameron to pick 1, 2 or 3.
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANDIR = HERE / "JESUS-MASTER-REF" / "candidates"
PROMPTS_MD = CANDIR / "CANDIDATE-PROMPTS.md"
DRIVER = HERE / "flow_driver.py"

prompts = [ln.strip() for ln in PROMPTS_MD.read_text(encoding="utf-8").splitlines()
           if ln.startswith("Beautiful hand-painted 2D animation style")]
if len(prompts) != 3:
    sys.exit(f"expected 3 candidate prompts, found {len(prompts)} in {PROMPTS_MD}")

for i, prompt in enumerate(prompts, 1):
    out = CANDIR / f"candidate-{i}-bust.jpeg"
    print(f"\n=== candidate {i} -> {out} ===")
    r = subprocess.run([sys.executable, str(DRIVER), "gen",
                        "--prompt", prompt, "--out", str(out)])
    if r.returncode != 0:
        sys.exit(f"candidate {i} failed (flow_driver exit {r.returncode})")
print("\nAll 3 candidates generated. Push, then ask Cameron to pick 1, 2 or 3.")
