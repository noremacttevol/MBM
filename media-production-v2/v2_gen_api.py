#!/usr/bin/env python3
"""V2 picture engine — Gemini API, gemini-3-pro-image at native 2K.

HISTORY OF THE LAW (so no session ever guesses):
- 2026-07-28  Cameron lifted the money law mid-row-1; all 20 row-1 stills shot here.
              Row 1 APPROVED. Best-looking stills of the whole project.
- 2026-07-29  Prepaid credits ran out mid-row-2 (RESOURCE_EXHAUSTED). Cameron said
              "use flow only" and this file was retired.
- 2026-07-30  Cameron REVERSED it: *"the first ones you did were good becasue we used
              and api key from gemini. i want to use that fro all 200 just so i get
              this done and over with faster."*  THE API IS THE ENGINE FOR ALL 200.
              Flow's only remaining job is character reference sheets (CAST-V2-REF).

MONEY SAFETY — every paid run carries a hard ceiling:
- Each generated image appends a line to api-spend.jsonl (the cross-session meter).
- --ceiling N  refuses to start any image that would push the meter past $N.
- --dry-run    prices the work without spending a cent.
Top-ups happen ONLY in Cameron's Google AI Studio billing console — never here.

Usage:
    python3 v2_gen_api.py build-01-cloak --ceiling 25          # one build
    python3 v2_gen_api.py --all --ceiling 100                  # all builds, in row order
    python3 v2_gen_api.py --all --dry-run                      # price it, spend nothing
    python3 v2_gen_api.py build-02-prodigal --only b04 b10 --redo --ceiling 5

Character consistency is held by IMAGE, not wording (the CAST-BIBLE lesson):
- Jesus: JESUS-V2-REF face attached to every beat marked ref=True (as always).
- Recurring cast: when a beat's `locks` name a member of the CAST-V2 library
  (PETER, JOHN, MARY-MAGDALENE, ...) and the approved sheet exists in CAST-V2-REF/,
  both angles are attached automatically. Per-build REFS = {"NAME": path-or-[paths]}
  still works for one-off characters and overrides the library on a name clash.
- PLACES too (Cameron 2026-08-04, v2_stash.py): a build's PLACE_REFS dict maps a
  lock token to an approved plate in PLACE-REF/, and the plate is attached to every
  beat whose `locks` name that token. Wire with `v2_stash.py --wire <build>`; a
  wired-but-missing plate stops the run before any credit (--no-plates overrides).
"""
import argparse
import base64
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2_prompt import JESUS_REF, assemble, load_beats  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ENV_FILE = os.path.join(ROOT, ".env.mbm-media")
SPEND_LEDGER = os.path.join(HERE, "api-spend.jsonl")
CAST_DIR = os.path.join(HERE, "CAST-V2-REF")
API = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

MODEL = "gemini-3-pro-image"
IMAGE_SIZE = "2K"          # 1536 x 2752 at 9:16
COST_PER_IMAGE = 0.134     # USD (measured 2026-07-28; first paid batch re-verifies vs billing)
MAX_CHAR_REF_IMAGES = 6    # keep request size sane on crowded beats
MAX_PAYLOAD_B64 = 18_000_000   # chars; the API rejects requests near 20 MB

# The CAST-V2 library: lock token -> file stems in CAST-V2-REF/ (front + quarter).
# Only tokens listed here auto-attach; a build's own REFS dict wins on a name clash.
GLOBAL_CAST = {
    "PETER": "peter", "ANDREW": "andrew", "JAMES-Z": "james-z", "JOHN": "john",
    "PHILIP": "philip", "BARTHOLOMEW": "bartholomew", "THOMAS": "thomas",
    "MATTHEW": "matthew", "JAMES-A": "james-a", "THADDAEUS": "thaddaeus",
    "SIMON-Z": "simon-z", "JUDAS": "judas", "MARY-MOTHER": "mary-mother",
    "MARY-MAGDALENE": "mary-magdalene", "JOHN-BAPTIST": "john-baptist",
}

FACE_LOCK_TEXT = (
    "The FIRST attached photograph is the FACE LOCK for Jesus. He must appear in this "
    "image as the SAME person: identical face, identical bone structure, identical "
    "eyes and eye colour, identical hair length and beard. Do not restyle him, do not "
    "re-age him, do not change his colouring. Only his pose, expression, action, "
    "clothing drape and surroundings may change. Compose the scene that is described "
    "below — do NOT reproduce the framing, crop or background of the attached "
    "photograph."
)
CHAR_LOCK_TEXT = (
    "Attached photograph(s) {idx} are CHARACTER LOCKS for the other named "
    "people in this scene. Each of them must appear here as the SAME person: identical "
    "face, identical hair, identical garment in the identical colours. Do not restyle, "
    "recolour or re-age them. Only their pose, action and surroundings may change, and "
    "the framing and background of the attached photographs must NOT be copied."
)
# PLACE plates (v2_stash.py, Cameron 2026-08-04: "use the stash ... copy the
# pictures it already has"). A plate carries PLACE IDENTITY only — the prompt
# text keeps authority over light, weather, time of day and who is present.
PLACE_LOCK_TEXT = (
    "Attached photograph(s) {idx} are PLACE LOCKS for the setting of this scene. The "
    "scene described below happens in the SAME PLACE shown in those photograph(s): "
    "keep its architecture, built structures, terrain, materials, colours and physical "
    "scale exactly, so a viewer recognises the same location from picture to picture. "
    "Do NOT copy a place photograph's framing, crop or camera angle; any people or "
    "animals visible in a place photograph are NOT part of this scene unless the text "
    "below names them; and the time of day, light and weather come ONLY from the text "
    "below, never from the photograph."
)
ROUGH_DRAFT_TEXT = (
    "The LAST attached photograph is a ROUGH COMPOSITION DRAFT of this exact shot. "
    "Keep its camera angle, blocking, character positions, actions and directions of "
    "travel — they are approved. Rebuild it as the fully realistic photograph the text "
    "below describes: true directional light, real lens depth of field, candid "
    "mid-action feel. Every person's face and identity comes from the FACE and "
    "CHARACTER lock photographs and the written locks, NEVER from this draft, and the "
    "draft's style must not be copied."
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


def spent_so_far():
    total = 0.0
    if os.path.exists(SPEND_LEDGER):
        for line in open(SPEND_LEDGER):
            line = line.strip()
            if line:
                try:
                    total += float(json.loads(line).get("est_cost", 0))
                except json.JSONDecodeError:
                    pass
    return total


def record_spend(build, beat_id, out):
    with open(SPEND_LEDGER, "a") as f:
        f.write(json.dumps({
            "ts": time.strftime("%Y-%m-%d %H:%M:%S"),
            "build": build, "beat": beat_id, "out": out,
            "model": MODEL, "size": IMAGE_SIZE, "est_cost": COST_PER_IMAGE,
        }) + "\n")


def b64_file(path):
    return base64.b64encode(open(path, "rb").read()).decode()


def _idx_range(start, n):
    return str(start) if n == 1 else f"{start}-{start + n - 1}"


def generate(key, prompt, face_b64=None, char_b64=None, place_b64=None,
             rough_b64=None, retries=4):
    parts = []
    preamble = []
    pos = 1
    if face_b64:
        parts.append({"inline_data": {"mime_type": "image/jpeg", "data": face_b64}})
        preamble.append(FACE_LOCK_TEXT)
        pos += 1
    for c in (char_b64 or []):
        parts.append({"inline_data": {"mime_type": "image/jpeg", "data": c}})
    if char_b64:
        preamble.append(CHAR_LOCK_TEXT.format(idx=_idx_range(pos, len(char_b64))))
        pos += len(char_b64)
    for p in (place_b64 or []):
        parts.append({"inline_data": {"mime_type": "image/jpeg", "data": p}})
    if place_b64:
        preamble.append(PLACE_LOCK_TEXT.format(idx=_idx_range(pos, len(place_b64))))
        pos += len(place_b64)
    if rough_b64:
        # Attached LAST so the face/character/place locks keep their stated positions.
        parts.append({"inline_data": {"mime_type": "image/jpeg", "data": rough_b64}})
        preamble.append(ROUGH_DRAFT_TEXT)
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
            if "RESOURCE_EXHAUSTED" in detail or "prepayment" in detail.lower():
                raise SystemExit(
                    f"OUT OF MONEY at the API: {detail}\n"
                    "Cameron tops up in Google AI Studio billing; then re-run — "
                    "the runner resumes exactly where it stopped.")
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


def cast_refs_for(beat, build_refs_cache):
    """Reference b64 images for this beat: build-local REFS first, then the
    CAST-V2 library for any lock token it names. Returns (list_of_b64, labels)."""
    out, labels = [], []
    for name in beat.get("locks", []):
        if name in build_refs_cache:
            for b in build_refs_cache[name]:
                out.append(b)
                labels.append(name)
        elif name in GLOBAL_CAST:
            stem = GLOBAL_CAST[name]
            for angle in ("front", "quarter"):
                p = os.path.join(CAST_DIR, f"{stem}-{angle}.jpeg")
                if os.path.exists(p) and os.path.getsize(p) > 50000:
                    out.append(b64_file(p))
                    labels.append(f"{name}:{angle}")
    if len(out) > MAX_CHAR_REF_IMAGES:
        print(f"      (capping character refs {len(out)} -> {MAX_CHAR_REF_IMAGES})")
        out = out[:MAX_CHAR_REF_IMAGES]
        labels = labels[:MAX_CHAR_REF_IMAGES]
    return out, labels


def build_todo(bdir, only, redo):
    mod = load_beats(bdir)
    # Honour the build's own OUTPUT_ASSET_DIR (v2_prompt.gen and v2_assemble
    # already do). A realistic rebuild keeps its rejected-look roughs in
    # `assets/` as ROUGH-DRAFT refs and generates into `assets-realistic/`;
    # hardcoding "assets" here made the API runner skip every beat whose old
    # rough existed and could silently overwrite the rough refs on --redo.
    assets = os.path.join(bdir, getattr(mod, "OUTPUT_ASSET_DIR", "assets"))
    os.makedirs(assets, exist_ok=True)
    todo = []
    for beat in mod.BEATS:
        if only and not any(o in beat["id"] for o in only):
            continue
        dest = os.path.join(assets, beat["out"])
        if not redo and os.path.exists(dest) and os.path.getsize(dest) > 50000:
            continue
        todo.append((mod, beat, dest))
    return todo


def place_plates_for(mod, no_plates):
    """token -> b64 plate for a build's PLACE_REFS (wired by v2_stash.py).
    A wired-but-missing plate stops the run BEFORE any credit: silently
    generating without it is exactly the drift the plate exists to prevent."""
    if no_plates:
        return {}
    plates = {}
    for tok, rel in (getattr(mod, "PLACE_REFS", {}) or {}).items():
        full = rel if os.path.isabs(rel) else os.path.join(mod.__bdir__, rel)
        if not os.path.isfile(full):
            raise SystemExit(
                f"place plate MISSING: {tok} -> {rel}\n"
                f"Run: python3 media-production-v2/v2_stash.py --wire "
                f"{os.path.basename(mod.__bdir__)}\n"
                "(or pass --no-plates to knowingly generate without place locks)")
        plates[tok] = b64_file(full)
    return plates


def run(todo, ceiling, dry_run, no_plates=False):
    est = len(todo) * COST_PER_IMAGE
    already = spent_so_far()
    print(f"{len(todo)} shot(s) · {MODEL} · {IMAGE_SIZE} · est ${est:.2f} this run · "
          f"meter ${already:.2f} spent so far"
          + (f" · ceiling ${ceiling:.2f}" if ceiling else ""))
    if dry_run:
        for mod, beat, _d in todo:
            wired = getattr(mod, "PLACE_REFS", {}) or {}
            ptoks = [t for t in beat.get("locks", []) if t in wired]
            marks = ("[face]" if beat.get("ref") else "") + (
                "[" + ",".join(n for n in beat.get("locks", [])
                               if n in GLOBAL_CAST) + "]"
                if any(n in GLOBAL_CAST for n in beat.get("locks", [])) else "") + (
                "[place:" + ",".join(ptoks) + "]" if ptoks else "")
            print(f"  {os.path.basename(os.path.dirname(os.path.dirname(_d)))}"
                  f" {beat['id']} -> {beat['out']} {marks}")
        print("(dry run — nothing generated, nothing spent)")
        return

    key = load_key()
    face_b64 = b64_file(os.path.join(ROOT, JESUS_REF))
    made = 0
    refs_cache_by_mod = {}
    plates_by_mod = {}
    for mod, _beat, _dest in todo:
        if id(mod) not in plates_by_mod:
            plates_by_mod[id(mod)] = place_plates_for(mod, no_plates)
    for mod, beat, dest in todo:
        if ceiling and spent_so_far() + COST_PER_IMAGE > ceiling:
            print(f"CEILING ${ceiling:.2f} reached (meter ${spent_so_far():.2f}). "
                  f"Stopping cleanly — re-run with a higher --ceiling to continue.")
            break
        if id(mod) not in refs_cache_by_mod:
            cache = {}
            for name, rel in (getattr(mod, "REFS", {}) or {}).items():
                paths = rel if isinstance(rel, (list, tuple)) else [rel]
                blobs = []
                for p in paths:
                    full = p if os.path.isabs(p) else os.path.join(mod.__bdir__, p)
                    if os.path.exists(full):
                        blobs.append(b64_file(full))
                    else:
                        print(f"  character lock MISSING (skipped): {name} -> {p}")
                if blobs:
                    cache[name] = blobs
            refs_cache_by_mod[id(mod)] = cache
        chars, labels = cast_refs_for(beat, refs_cache_by_mod[id(mod)])
        plates = plates_by_mod[id(mod)]
        ptoks = [t for t in beat.get("locks", []) if t in plates]
        places = [plates[t] for t in ptoks]
        rough_b64 = None
        rough = beat.get("rough_ref")
        if rough:
            rpath = rough if os.path.isabs(rough) else os.path.join(mod.__bdir__, rough)
            if os.path.isfile(rpath):
                rough_b64 = b64_file(rpath)
        # Request-size guard: drop plates first (they help, the others are law),
        # then surplus character angles. Never silently — every drop is printed.
        used = (len(face_b64) if beat.get("ref") else 0) + sum(map(len, chars)) \
            + sum(map(len, places)) + (len(rough_b64) if rough_b64 else 0)
        while used > MAX_PAYLOAD_B64 and places:
            used -= len(places.pop())
            print(f"      (payload cap: dropping place plate {ptoks.pop()})")
        while used > MAX_PAYLOAD_B64 and len(chars) > 2:
            used -= len(chars.pop())
            print(f"      (payload cap: dropping char ref {labels.pop()})")
        bname = os.path.basename(os.path.dirname(os.path.dirname(dest)))
        print(f"=== {bname} {beat['id']} -> {beat['out']} ==="
              + (f"  [face lock]" if beat.get("ref") else "")
              + (f"  [+{len(labels)} char ref: {', '.join(labels)}]" if labels else "")
              + (f"  [+{len(ptoks)} place: {', '.join(ptoks)}]" if ptoks else "")
              + ("  [rough draft]" if rough_b64 else ""),
              flush=True)
        try:
            img = generate(key, assemble(beat, mod.LOCKS),
                           face_b64 if beat.get("ref") else None, chars, places,
                           rough_b64)
        except SystemExit:
            raise
        except Exception as e:
            print(f"    FAILED: {e}", flush=True)
            continue
        with open(dest, "wb") as f:
            f.write(img)
        record_spend(bname, beat["id"], beat["out"])
        made += 1
        print(f"    saved {beat['out']} ({os.path.getsize(dest)//1024} KB)", flush=True)
    print(f"DONE: {made}/{len(todo)} generated · ~${made * COST_PER_IMAGE:.2f} this run "
          f"· meter now ${spent_so_far():.2f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("build_dir", nargs="?", default=None,
                    help="one build folder; or use --all")
    ap.add_argument("--all", action="store_true",
                    help="every build with a beats_v2.py, lowest row first")
    ap.add_argument("--only", nargs="*", default=None)
    ap.add_argument("--redo", action="store_true",
                    help="regenerate even if the file already exists")
    ap.add_argument("--ceiling", type=float, default=None,
                    help="hard dollar cap on the cross-session meter (api-spend.jsonl)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-plates", action="store_true",
                    help="generate WITHOUT wired place plates (loud, deliberate — "
                         "for a machine that lacks the source stills)")
    a = ap.parse_args()

    if bool(a.build_dir) == a.all:
        raise SystemExit("Pass exactly one of: <build_dir> or --all")
    if not a.dry_run and a.ceiling is None:
        raise SystemExit("Paid runs require --ceiling N (dollars). "
                         "Use --dry-run to price without spending.")

    dirs = []
    if a.all:
        def row_of(d):
            m = re.match(r"build-(\d+)", os.path.basename(d))
            return int(m.group(1)) if m else 10**9
        for d in sorted(glob.glob(os.path.join(HERE, "build-*")), key=row_of):
            if os.path.exists(os.path.join(d, "beats_v2.py")):
                dirs.append(d)
    else:
        d = os.path.abspath(a.build_dir)
        if not os.path.exists(os.path.join(d, "beats_v2.py")):
            raise SystemExit(f"No beats_v2.py in {d}")
        dirs.append(d)

    todo = []
    for d in dirs:
        try:
            for mod, beat, dest in build_todo(d, a.only, a.redo):
                mod.__bdir__ = d
                todo.append((mod, beat, dest))
        except Exception as e:
            print(f"SKIP {os.path.basename(d)}: beats load failed: {e}")
    run(todo, a.ceiling, a.dry_run, a.no_plates)


if __name__ == "__main__":
    main()
