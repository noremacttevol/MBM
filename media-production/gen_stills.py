#!/usr/bin/env python3
"""
gen_stills.py — generate a build's painted stills through the official Gemini
image API, replacing the manual Google Flow browser burst.

Why this exists: Flow has no API and driving it in Chrome steals Cameron's mouse
(PRODUCTION-BIBLE §0 Law C) and cannot run unattended. The Gemini image API is
the same Google image models behind a real key, so the whole pipeline can run
headless. Phase 1 is stills-only (Law E), so images are all we need.

Reads a build folder's PROMPTS.md, generates one PNG per shot, and writes a
cost/receipt log. Refuses to spend a cent until the face gate passes.

Usage:
    python3 gen_stills.py --dir media-production/build-38-persistent-widow
    python3 gen_stills.py --dir <dir> --only s1-widow-alone   # regenerate one shot
    python3 gen_stills.py --dir <dir> --model gemini-3-pro-image
    python3 gen_stills.py --dir <dir> --dry-run               # parse only, spend nothing
"""

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ENV_FILE = REPO / ".env.mbm-media"
GATE = REPO / "media-production" / "jesus_face_gate.py"
API = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

# Cost per generated image, USD. Used only for the receipt line so Cameron always
# knows what a build cost (PRODUCTION-BIBLE §6: report spend every session).
COST = {
    "gemini-2.5-flash-image": 0.039,
    "gemini-3.1-flash-image": 0.045,
    "gemini-3-pro-image": 0.134,
}
DEFAULT_MODEL = "gemini-2.5-flash-image"

# A shot heading looks like:  ## s1-widow-alone — Shot 1: a widow, wronged and alone
SHOT_RE = re.compile(r"^##\s+([a-z0-9][a-z0-9\-_]*)\s*[—–-]", re.I)
STYLE_RE = re.compile(r"^STILL STYLE BLOCK[^\n]*\n(.*?)(?=\n\n)", re.S | re.M)


def load_key() -> str:
    if not ENV_FILE.exists():
        sys.exit(f"No key file at {ENV_FILE}. Put GEMINI_API_KEY=... in it (it is gitignored).")
    for line in ENV_FILE.read_text().splitlines():
        if line.startswith("GEMINI_API_KEY="):
            return line.split("=", 1)[1].strip()
    sys.exit(f"GEMINI_API_KEY not found in {ENV_FILE}")


def face_gate(build_dir: Path) -> None:
    """The #1 law. No Flow/Gemini credit is spent until this exits 0."""
    r = subprocess.run(
        [sys.executable, str(GATE), "--dir", str(build_dir)],
        capture_output=True, text=True,
    )
    sys.stdout.write(r.stdout)
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        sys.exit("🛑 FACE GATE FAILED — not generating. Fix the prompts and re-run.")


def parse_prompts(md: str) -> tuple[str, list[tuple[str, str]]]:
    """Return (style_block, [(slug, prompt_body), ...]) from a PROMPTS.md."""
    m = STYLE_RE.search(md)
    style = " ".join(m.group(1).split()) if m else ""

    shots: list[tuple[str, str]] = []
    slug = None
    body: list[str] = []
    for line in md.splitlines():
        hit = SHOT_RE.match(line)
        if hit:
            if slug:
                shots.append((slug, "\n".join(body).strip()))
            slug, body = hit.group(1), []
        elif slug is not None:
            body.append(line)
    if slug:
        shots.append((slug, "\n".join(body).strip()))

    # Expand the [STILL STYLE BLOCK] placeholder into the literal locked text.
    # PRODUCTION-BIBLE §5b ban #2: byte-identical, zero added style words.
    out = []
    for s, b in shots:
        b = " ".join(b.replace("[STILL STYLE BLOCK]", style).split())
        if b:
            out.append((s, b))
    return style, out


def generate(key: str, model: str, prompt: str, retries: int = 4) -> bytes:
    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": "9:16"},  # vertical, per §5 QC
        },
    }).encode()

    delay = 5
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(
            API.format(model=model) + f"?key={key}",
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = json.load(resp)
            for part in data["candidates"][0]["content"]["parts"]:
                if "inlineData" in part:
                    return base64.b64decode(part["inlineData"]["data"])
            raise RuntimeError("no image in response (model returned text only)")
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")[:300]
            # 429 = rate limit, 5xx = transient. Back off and keep going.
            if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                print(f"      HTTP {e.code}, retry {attempt}/{retries} in {delay}s")
                time.sleep(delay)
                delay *= 2
                continue
            raise RuntimeError(f"HTTP {e.code}: {detail}") from None
        except Exception as e:
            if attempt < retries:
                print(f"      {e}, retry {attempt}/{retries} in {delay}s")
                time.sleep(delay)
                delay *= 2
                continue
            raise
    raise RuntimeError("exhausted retries")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="build folder containing PROMPTS.md")
    ap.add_argument("--model", default=DEFAULT_MODEL, choices=sorted(COST))
    ap.add_argument("--only", help="regenerate a single shot slug")
    ap.add_argument("--dry-run", action="store_true", help="parse and gate only; spend nothing")
    args = ap.parse_args()

    build = Path(args.dir)
    if not build.is_absolute():
        build = REPO / build
    prompts_md = build / "PROMPTS.md"
    if not prompts_md.exists():
        sys.exit(f"No PROMPTS.md in {build}")

    face_gate(build)

    _, shots = parse_prompts(prompts_md.read_text())
    if args.only:
        shots = [s for s in shots if s[0] == args.only]
        if not shots:
            sys.exit(f"No shot named {args.only!r} in {prompts_md}")

    print(f"\n{len(shots)} shot(s) · model {args.model} · "
          f"est ${len(shots) * COST[args.model]:.2f}\n")
    if args.dry_run:
        for slug, body in shots:
            print(f"  {slug}: {body[:90]}...")
        print("\n(dry run — nothing generated, nothing spent)")
        return

    key = load_key()
    art = build / "art"
    art.mkdir(exist_ok=True)

    made, failed = [], []
    for i, (slug, body) in enumerate(shots, 1):
        out = art / f"{slug}.png"
        print(f"  [{i}/{len(shots)}] {slug} ...", flush=True)
        try:
            out.write_bytes(generate(key, args.model, body))
            print(f"      ✅ {out.relative_to(REPO)} ({out.stat().st_size // 1024} KB)")
            made.append(slug)
        except Exception as e:
            print(f"      ❌ {e}")
            failed.append(slug)

    spent = len(made) * COST[args.model]
    receipt = {
        "model": args.model,
        "generated": made,
        "failed": failed,
        "images": len(made),
        "usd": round(spent, 3),
    }
    (build / "art-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")

    print(f"\n  {len(made)} generated, {len(failed)} failed · spent ~${spent:.2f}")
    if failed:
        sys.exit(f"🛑 {len(failed)} shot(s) failed: {', '.join(failed)}")


if __name__ == "__main__":
    main()
