#!/usr/bin/env python3
"""v2_gen_api.py — generate V2 stills through the Gemini image API at 2K.

WHY THIS EXISTS (2026-07-28)
----------------------------
Cameron lifted the paid-API ban: *"ignore the money law … I already paid for it …
there shouldn't be any limitations on the money. Make it how it's supposed to be."*
(FACTORY-ORDERS.md MONEY RULE #1.) That unlocks the one thing Flow could not give V2:

  Flow            768 x 1376   — below the 1080x1920 delivery size, so every Ken
                                 Burns move upscales, which the anti-shimmer law
                                 is written against
  gemini-3-pro-image 2K   1536 x 2752   — 4x the pixels and real headroom to
                                 supersample the drift

It also removes the Flow ceiling (~20 generations/hour, one browser at a time) and
never touches Cameron's screen — no stolen mouse, no announced bursts.

This is deliberately NOT gen_stills.py. That script is V1: its ANCHOR_TEXT and
CHAR_TEXT tell the model to match a *reference painting* and to *paint* the
characters, which is the exact style V2 retired. V2 needs photographic wording, so
the request is built here and V1's script is left untouched.

Usage:
    python3 media-production-v2/v2_gen_api.py <build-dir> [--only b03 b05] [--redo]
    python3 media-production-v2/v2_gen_api.py <build-dir> --dry-run
"""
import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2_prompt import JESUS_REF, assemble, load_beats  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_FILE = os.path.join(ROOT, ".env.mbm-media")
API = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

MODEL = "gemini-3-pro-image"
IMAGE_SIZE = "2K"          # 1536 x 2752 at 9:16
COST_PER_IMAGE = 0.134     # USD, from gen_stills.py's measured table

# V2 character-lock wording. Photographic, never "painted" — the V1 anchor text
# would drag the retired illustration style straight back in.
FACE_LOCK_TEXT = (
    "The FIRST attached photograph is the FACE LOCK for Jesus. He must appear in this "
    "image as the SAME person: identical face, identical bone structure, identical "
    "eyes and eye colour, identical hair length and beard. Do not restyle him, do not "
    "re-age him, do not change his colouring. Only his pose, expression, action, "
    "clothing drape and surroundings may change. Compose the scene that is described "
    "below — do NOT reproduce the framing, crop or background of the attached "
    "photograph."
)

# Character consistency across a video is held by IMAGE, not by wording — that is the
# whole lesson of CAST-BIBLE.md. Flow got this for Jesus via --ref and got nothing for
# anyone else; the API can carry several, so a build may name a reference picture per
# character in a REFS dict and every shot that character appears in gets it attached.
CHAR_LOCK_TEXT = (
    "The remaining attached photograph(s) are CHARACTER LOCKS for the other named "
    "people in this scene. Each of them must appear here as the SAME person: identical "
    "face, identical hair, identical garment in the identical colours. Do not restyle, "
    "recolour or re-age them. Only their pose, action and surroundings may change, and "
    "the framing and background of the attached photographs must NOT be copied."
)


def load_key():
    if not os.path.exists(ENV_FILE):
        raise SystemExit(
            f"No key file at {ENV_FILE}. Put GEMINI_API_KEY=... in it (it is gitignored).")
    for line in open(ENV_FILE):
        line = line.strip()
        if line.startswith("GEMINI_API_KEY"):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit(f"GEMINI_API_KEY not found in {ENV_FILE}")


def generate(key, prompt, face_b64=None, char_b64=None, retries=4):
    parts = []
    preamble = []
    if face_b64:
        parts.append({"inline_data": {"mime_type": "image/jpeg", "data": face_b64}})
        preamble.append(FACE_LOCK_TEXT)
    for c in char_b64 or []:
        parts.append({"inline_data": {"mime_type": "image/jpeg", "data": c}})
    if char_b64:
        preamble.append(CHAR_LOCK_TEXT)
    text = ("\n\n".join(preamble) + "\n\n" + prompt) if preamble else prompt
    parts.append({"text": text})
    payload = json.dumps({
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": "9:16", "imageSize": IMAGE_SIZE},
        },
    }).encode()

    delay = 5
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(
            API.format(model=MODEL) + f"?key={key}",
            data=payload, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.load(resp)
            for part in data["candidates"][0]["content"]["parts"]:
                if "inlineData" in part:
                    return base64.b64decode(part["inlineData"]["data"])
            raise RuntimeError("no image in response (model returned text only)")
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")[:300]
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("build_dir")
    ap.add_argument("--only", nargs="*", default=None)
    ap.add_argument("--redo", action="store_true",
                    help="regenerate even if the file already exists")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    bdir = os.path.abspath(a.build_dir)
    mod = load_beats(bdir)
    assets = os.path.join(bdir, "assets")
    os.makedirs(assets, exist_ok=True)

    todo = []
    for beat in mod.BEATS:
        if a.only and not any(o in beat["id"] for o in a.only):
            continue
        dest = os.path.join(assets, beat["out"])
        if not a.redo and os.path.exists(dest) and os.path.getsize(dest) > 50000:
            continue
        todo.append((beat, dest))

    print(f"{len(todo)} shot(s) · model {MODEL} · {IMAGE_SIZE} · "
          f"est ${len(todo) * COST_PER_IMAGE:.2f}")
    if a.dry_run:
        for beat, _d in todo:
            print(f"  {beat['id']} -> {beat['out']}"
                  f"{'  [face lock]' if beat.get('ref') else ''}")
        print("(dry run — nothing generated, nothing spent)")
        return

    key = load_key()
    face_b64 = base64.b64encode(
        open(os.path.join(ROOT, JESUS_REF), "rb").read()).decode()

    # Optional per-character reference pictures, declared by the build as
    # REFS = {"WOMAN": "refs/woman.jpeg", ...} relative to the build folder.
    refs = getattr(mod, "REFS", {}) or {}
    char_cache = {}
    for name, rel in refs.items():
        p = rel if os.path.isabs(rel) else os.path.join(bdir, rel)
        if os.path.exists(p):
            char_cache[name] = base64.b64encode(open(p, "rb").read()).decode()
            print(f"  character lock available: {name} -> {rel}")
        else:
            print(f"  character lock MISSING (skipped): {name} -> {rel}")

    made = 0
    for beat, dest in todo:
        chars = [char_cache[n] for n in beat.get("locks", []) if n in char_cache]
        print(f"=== {beat['id']} -> {beat['out']} ==="
              f"{'  [+' + str(len(chars)) + ' char lock]' if chars else ''}", flush=True)
        try:
            img = generate(key, assemble(beat, mod.LOCKS),
                           face_b64 if beat.get("ref") else None, chars)
        except Exception as e:
            print(f"    FAILED: {e}", flush=True)
            continue
        with open(dest, "wb") as f:
            f.write(img)
        made += 1
        print(f"    saved {beat['out']} ({os.path.getsize(dest)//1024} KB)", flush=True)
    print(f"DONE: {made}/{len(todo)} generated · spent ~${made * COST_PER_IMAGE:.2f}")


if __name__ == "__main__":
    main()
