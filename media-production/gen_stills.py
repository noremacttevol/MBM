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
# 3.1-flash, not Pro. The old note here said "flash only renders 768x1344, so Ken
# Burns would have to upscale" — that is true of gemini-2.5-flash-image (measured:
# 768x1344 even when asked for 2K) but NOT of gemini-3.1-flash-image, which returns
# the full 1536x2752 at 2K, same as Pro, for a third of the price and ~40% faster.
# Measured head-to-head on s13-ask-seek-knock, 2026-07-13:
#   gemini-3-pro-image      1536x2752  27s  $0.134
#   gemini-3.1-flash-image  1536x2752  16s  $0.045   ← same size, better prompt
#                                                       adherence on the light
#   gemini-2.5-flash-image   768x1344  11s  $0.039   ← too small, forbidden
# Re-measure before trusting any resolution claim about a new model.
DEFAULT_MODEL = "gemini-3.1-flash-image"
IMAGE_SIZE = "2K"

# THE STYLE ANCHOR (PRODUCTION-BIBLE §2: "use frames from approved clips as style
# anchors to hold consistency"). The locked Master Style Block was written against
# Google Flow; the same words land differently on Gemini (colder palette, and Pro
# likes to paint a cream paper border around the picture). Rather than add style
# words to the block — banned by §5b ban #2 — every generation is conditioned on a
# real APPROVED still from a delivered video. The block stays byte-identical and
# the look is held by Cameron's own art.
STYLE_ANCHOR = REPO / "media-production" / "build-20-samaritan" / "assets" / "s4-compassion.jpeg"
ANCHOR_TEXT = (
    "Match the exact art style, palette, brushwork, line quality and lighting of the "
    "attached reference painting. The image fills the entire frame edge to edge with "
    "no border, no frame, no paper margin, no vignette."
)

# THE CHARACTER LOCK (PRODUCTION-BIBLE: "Wardrobe and props lock and hold").
# Describing a character's clothes in words is not enough — across seven shots the
# widow's shawl came back charcoal, then grey-green, then pale grey, then blue-grey.
# So a shot can name earlier shots of the SAME build as character references with a
# "REF:" line in PROMPTS.md, e.g.
#     REF: s1-widow-alone
# Those already-generated stills are attached to the request, and the character must
# come back wearing the same face, hair, and clothes. Shots generate in file order,
# so a REF always points at a shot that already exists.
CHAR_TEXT = (
    "The additional attached image(s) are the CHARACTER LOCK for this story. Any "
    "character who appears in them must be painted here as the SAME person: identical "
    "face, identical hair, identical clothing in the identical colors. Do not restyle, "
    "recolor, or re-age them. Only their pose, action, and surroundings may change."
)
REF_RE = re.compile(r"^\s*REF:\s*(.+)$", re.I | re.M)

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
    # Pull any "REF: slug, slug" line out of the body — it is an instruction to the
    # generator, not prompt text, so it must never reach the model as words.
    out = []
    for s, b in shots:
        refs: list[str] = []
        m = REF_RE.search(b)
        if m:
            refs = [r.strip() for r in m.group(1).replace(",", " ").split() if r.strip()]
            b = REF_RE.sub("", b)
        b = " ".join(b.replace("[STILL STYLE BLOCK]", style).split())
        if b:
            out.append((s, b, refs))
    return style, out


def generate(key: str, model: str, prompt: str, anchor_b64: str | None,
             char_b64: list[str] | None = None, retries: int = 4) -> bytes:
    parts: list[dict] = []
    preamble = []
    if anchor_b64:
        parts.append({"inline_data": {"mime_type": "image/jpeg", "data": anchor_b64}})
        preamble.append(ANCHOR_TEXT)
    for c in char_b64 or []:
        parts.append({"inline_data": {"mime_type": "image/jpeg", "data": c}})
    if char_b64:
        preamble.append(CHAR_TEXT)
    text = ("\n\n".join(preamble) + "\n\n" + prompt) if preamble else prompt
    parts.append({"text": text})

    payload = json.dumps({
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": "9:16", "imageSize": IMAGE_SIZE},  # vertical, per §5 QC
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
    ap.add_argument("--no-anchor", action="store_true",
                    help="generate without the approved-art style anchor (style will drift)")
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
        for slug, body, refs in shots:
            lock = f"  [locked to {', '.join(refs)}]" if refs else ""
            print(f"  {slug}{lock}: {body[:80]}...")
        print("\n(dry run — nothing generated, nothing spent)")
        return

    key = load_key()
    # House convention across every build: assets/<slug>.jpeg (build.py reads these).
    art = build / "assets"
    art.mkdir(exist_ok=True)

    anchor_b64 = None
    if not args.no_anchor:
        if not STYLE_ANCHOR.exists():
            sys.exit(f"Style anchor missing: {STYLE_ANCHOR}")
        anchor_b64 = base64.b64encode(STYLE_ANCHOR.read_bytes()).decode()
        print(f"style anchor: {STYLE_ANCHOR.name}\n")

    made, failed = [], []
    for i, (slug, body, refs) in enumerate(shots, 1):
        out = art / f"{slug}.jpeg"
        char_b64 = []
        for r in refs:
            rp = art / f"{r}.jpeg"
            if not rp.exists():
                # A REF must point at a shot generated earlier in the file. If it is
                # missing, the character lock is silently lost — say so, do not shrug.
                print(f"      ⚠️  REF {r} not generated yet — character lock NOT applied")
                continue
            char_b64.append(base64.b64encode(rp.read_bytes()).decode())
        note = f" (locked to {', '.join(refs)})" if char_b64 else ""
        print(f"  [{i}/{len(shots)}] {slug}{note} ...", flush=True)
        try:
            out.write_bytes(generate(key, args.model, body, anchor_b64, char_b64))
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
