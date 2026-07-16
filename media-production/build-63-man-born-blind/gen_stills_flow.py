#!/usr/bin/env python3
"""Generate #63's 10 stills via flow_driver.py (Nano Banana 2, 9:16, $0).
FACE LAW v3 TEXT-ONLY: JESUS LOCK v3 stays in the prompt text, the REF: line is
dropped and NO --ref is attached (the attached portrait echoes — playbook). Shot
bodies from PROMPTS.md in order; skips stills already on disk so it resumes."""
import glob
import os
import re
import subprocess
import sys
from pathlib import Path

PROFILE = Path.home() / ".mbm-flow-profile"


def clear_stale_lock():
    """Chrome leaves Singleton* symlinks behind after exit; a stale lock aborts the
    next launch. Remove them only when no live process is using the profile."""
    for cmdline in glob.glob("/proc/[0-9]*/cmdline"):
        try:
            if b"mbm-flow-profile" in open(cmdline, "rb").read():
                return
        except OSError:
            continue
    for f in PROFILE.glob("Singleton*"):
        f.unlink(missing_ok=True)

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

text = PROMPTS.read_text(encoding="utf-8")

locks = {}
for name in ("BLIND-MAN LOCK", "JERUSALEM-SETTING LOCK"):
    m = re.search(r"\[" + re.escape(name) + r"\] = (.+?)(?=\n\n)", text, re.S)
    assert m, f"lock {name} not found"
    locks[name] = " ".join(m.group(1).split())

shots = re.findall(r"^## (s\d+-[A-Za-z0-9-]+)[^\n]*\n(.+?)(?=\n## |\n### |\Z)", text, re.S | re.M)
assert len(shots) == 10, f"expected 10 shots, got {len(shots)}"

failed = []
only = sys.argv[1] if len(sys.argv) > 1 else None
for slug, body in shots:
    fn = f"{slug}.jpeg"
    if only and only not in fn:
        continue
    out = ASSETS / fn
    if out.exists() and out.stat().st_size > 10000:
        print(f"skip {fn} (exists)", flush=True)
        continue
    body = re.sub(r"^REF: .*$", "", body, flags=re.M)
    body = body.replace("[STILL STYLE BLOCK]", STYLE)
    for name, val in locks.items():
        body = body.replace(f"[{name}]", val)
    body = " ".join(body.split())
    print(f"=== generating {fn} ===", flush=True)
    clear_stale_lock()
    r = subprocess.run(["python3", str(DRIVER), "gen", "--prompt", body, "--out", str(out)])
    if not (r.returncode == 0 and out.exists()):
        failed.append(fn)
        print(f"  FAILED {fn}", flush=True)
if failed:
    sys.exit("FAILED: " + ", ".join(failed))
print("ALL 63 STILLS GENERATED")
