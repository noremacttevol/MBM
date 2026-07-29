#!/usr/bin/env python3
"""v2_prompt.py — the V2 prompt assembler. Shared by every V2 build.

WHY THIS EXISTS
---------------
V2-KICKOFF requires STYLE-V2 and JESUS LOCK v4 to appear **byte-identical** in
every prompt, and every character's description to stay byte-identical across all
of a video's prompts. Hand-copying a 900-character block into twenty prompts is
exactly how drift got into V1. Here the blocks are written ONCE and assembled
mechanically, so byte-identity is a property of the code instead of a thing QC
has to keep catching.

A build supplies a `beats_v2.py` next to itself with:

    BEATS = [ {id, out, seg, window, wide, jesus, locks, scene, model}, ... ]
    LOCKS = { "WOMAN": "...", ... }        # locks local to that video

and this module turns each beat into the full prompt string.

Usage:
    python3 v2_prompt.py <build-dir> --dump          # write ASSEMBLED-PROMPTS.txt
    python3 v2_prompt.py <build-dir> --check         # run the v4 checklist (step D)
    python3 v2_prompt.py <build-dir> --gen [--only b03 b04]   # generate via Flow
"""
import argparse
import importlib.util
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLOW_DRIVER = os.path.join(ROOT, "media-production", "flow_driver.py")
JESUS_REF = "media-production-v2/JESUS-V2-REF/jesus-v2-face.jpeg"

# ---------------------------------------------------------------- BLOCKS ----
# STYLE-V2 — byte-identical opener of EVERY image prompt (V2-KICKOFF).
STYLE_V2 = (
    "Cinematic biblical realism: a lifelike scene from first-century Judea, like a "
    "still frame from a reverent, masterfully photographed biblical film. Natural "
    "cinematic lighting, true depth of field, real physical scale. Realistic faces, "
    "eyes, hands and anatomy; real fabric weave, wood grain, stone, dust and skin "
    "texture. Historically credible clothing of rough-woven wool and linen in earth "
    "tones; authentic architecture and landscape. Emotionally warm, reverent, and "
    "spiritually serious. Not cartoon, not comic, not anime, not plastic CGI, not a "
    "painted illustration, not a copy of any painting or artist's style. No text, "
    "captions, borders, panels, watermarks, or modern objects anywhere in the image."
)

# JESUS LOCK v4 — byte-identical in every prompt where Jesus appears.
JESUS_LOCK_V4 = (
    "JESUS LOCK v4: the SAME man as the attached JESUS-V2-REF image — identical face, "
    "hair and beard in every picture: a Middle Eastern Jewish man of about thirty-three, "
    "warm olive-brown skin, strong kind weathered features, shoulder-length dark "
    "brown-black wavy hair, a full dark beard, striking natural GREEN eyes, one plain "
    "undyed off-white cream wool robe with a simple mantle and cloth sash (only he wears "
    "cream), leather sandals. No halo, no glow, no rim-light. Never Caucasian, never "
    "pale, never blue-eyed, never blond."
)

# Forced-wide defense line — required after STYLE-V2 on any WIDE or multi-figure
# shot that has a ref attached (the ref-echo failure, FLOW-BUILD-PLAYBOOK).
WIDE_DEFENSE = (
    "WIDE FULL-LENGTH SCENE with MULTIPLE PEOPLE — never a portrait, never a close-up "
    "of one face; the camera far enough back that the named figures are visible head "
    "to sandals."
)

# Anti-panel clause — mandatory on every wide multi-figure still (Standing Law e).
# V1's wording said "ILLUSTRATION"; V2 is photographic, so the noun changes and
# nothing else does.
ANTI_PANEL = (
    "SINGLE UNIFIED PHOTOGRAPHIC FRAME, one scene edge to edge, NOT a grid, triptych, "
    "stacked panels or comic strip, no dividing lines, one picture only."
)

CLOSER = "One single continuous scene edge to edge, no border. 9:16 vertical."

# Recurring cast — copied byte-identical from media-production/CAST-REF/CAST-BIBLE.md,
# which wins over CHARACTER-LAW.md where they disagree (V2-KICKOFF).
CAST_LOCKS = {
    "PETER": (
        "PETER LOCK: Peter is the same man in every shot — a sturdy Galilean fisherman "
        "in his late thirties, broad and strong, thick dark curly hair going a little "
        "wild, a full dark beard, weathered warm-olive skin, deep brown eyes, heavy "
        "honest features. He wears a dusty BLUE-GREY wool tunic with a plain rope belt "
        "(never cream). His face is shown clearly."
    ),
    "ANDREW": (
        "ANDREW LOCK: Andrew is the same man in every shot — Peter's younger brother, "
        "early thirties, similar sturdy build but leaner, short dark curly hair, a "
        "shorter rounded dark beard, warm-olive skin, open kind eyes. He wears a "
        "RUST-BROWN wool tunic with a cord belt (never cream). His face is shown clearly."
    ),
    "JOHN": (
        "JOHN LOCK: John is the same man in every shot — the youngest disciple, early "
        "twenties, smooth-featured and gentle, wavy chestnut-brown hair to the jaw, only "
        "a soft light beard, warm tan skin, large calm dark eyes. He wears a SAND / "
        "warm-tan wool tunic with a woven sash (never cream). His face is shown clearly."
    ),
    "JAMES-Z": (
        "JAMES-Z LOCK: James is the same man in every shot — tall and strong, mid "
        "thirties, dark hair pulled back off the face, a thick full black beard, "
        "deep-olive skin, a steady bold gaze. He wears a DEEP-OLIVE (forest brown-green) "
        "wool tunic with a leather belt (never cream). His face is shown clearly."
    ),
}

# Words that mean the wrong Jesus. Any of these in a prompt fails the checklist.
DRIFT_WORDS = ["caucasian", "pale skin", "blue-eyed", "blue eyes", "blond", "blonde",
               "halo", "glow", "glowing", "rim-light", "rim light", "backlit halo"]


def load_beats(build_dir):
    path = os.path.join(build_dir, "beats_v2.py")
    if not os.path.isfile(path):
        raise SystemExit(f"no beats_v2.py in {build_dir}")
    spec = importlib.util.spec_from_file_location("beats_v2", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["beats_v2"] = mod
    spec.loader.exec_module(mod)
    return mod


def assemble(beat, local_locks):
    """Build the full prompt string for one beat."""
    parts = [STYLE_V2]
    if beat.get("wide"):
        parts.append(WIDE_DEFENSE)
    # ANTI-PANEL ON EVERY BEAT, not just wide ones (row 2, b18). It used to ride
    # along with the wide defense line, so tight shots got no panel protection —
    # and b18, a tight shot, came back with a landscape pasted in above the wall
    # like a second panel. A panel artifact is not a wide-shot problem.
    parts.append(ANTI_PANEL)
    for name in beat.get("locks", []):
        block = local_locks.get(name) or CAST_LOCKS.get(name)
        if block is None:
            raise SystemExit(f"{beat['id']}: unknown lock {name!r}")
        parts.append(block)
    if beat.get("jesus"):
        parts.append(JESUS_LOCK_V4)
    parts.append(beat["scene"])
    parts.append(CLOSER)
    return " ".join(" ".join(p.split()) for p in parts)


def check(build_dir, mod):
    """Step D — the v4 checklist that replaces the retired v3 gate."""
    fails, warns = [], []
    for beat in mod.BEATS:
        p = assemble(beat, mod.LOCKS)
        low = p.lower()
        if not p.startswith(STYLE_V2):
            fails.append(f"{beat['id']}: prompt does not open with STYLE-V2")
        if beat.get("jesus"):
            if JESUS_LOCK_V4 not in p:
                fails.append(f"{beat['id']}: Jesus shot missing byte-identical LOCK v4")
            if not beat.get("ref"):
                fails.append(f"{beat['id']}: Jesus shot missing the REF line")
        for w in DRIFT_WORDS:
            # "never blue-eyed / never pale" inside the lock are the lock's own
            # negations, not drift — only flag them outside the lock text.
            outside = p.replace(JESUS_LOCK_V4, "").lower()
            if w in outside:
                fails.append(f"{beat['id']}: drift word {w!r} in the scene text")
        if "cream" in low:
            for line in beat["scene"].split(". "):
                ll = line.lower()
                if "cream" in ll and "jesus" not in ll and "he " not in ll \
                        and "his " not in ll and "only he" not in ll:
                    warns.append(f"{beat['id']}: check cream usage — {line.strip()[:70]}")
        if "NEGATIVE" in beat["scene"].upper() or "negative prompt" in low:
            fails.append(f"{beat['id']}: NEGATIVE-PROMPT list is banned in V2")
        if beat.get("wide") and ANTI_PANEL not in p:
            fails.append(f"{beat['id']}: wide shot missing the anti-panel clause")
        # A char_ref that does not exist must fail HERE, not after a credit is spent.
        for cref in beat.get("char_refs", []):
            path = cref if os.path.isabs(cref) else os.path.join(build_dir, cref)
            if not os.path.isfile(path):
                fails.append(f"{beat['id']}: char_ref missing on disk: {cref}")
    print(f"checked {len(mod.BEATS)} beats in {os.path.basename(build_dir)}")
    for w in warns:
        print(f"  WARN  {w}")
    for f in fails:
        print(f"  FAIL  {f}")
    if fails:
        sys.exit(1)
    print("  v4 checklist: PASS")


def dump(build_dir, mod):
    out = os.path.join(build_dir, "ASSEMBLED-PROMPTS.txt")
    with open(out, "w") as f:
        for beat in mod.BEATS:
            f.write(f"### {beat['id']}  ->  {beat['out']}\n")
            f.write(f"# window {beat['window']}  seg {beat['seg']}  "
                    f"model {beat.get('model', 'Nano Banana Pro')}"
                    f"{'  REF ' + JESUS_REF if beat.get('ref') else ''}"
                    f"{''.join('  CHAR-REF ' + c for c in beat.get('char_refs', []))}\n")
            f.write(assemble(beat, mod.LOCKS) + "\n\n")
    print(f"wrote {out} ({len(mod.BEATS)} prompts)")


def gen(build_dir, mod, only, redo_suffix=""):
    assets = os.path.join(build_dir, "assets")
    os.makedirs(assets, exist_ok=True)
    for beat in mod.BEATS:
        if only and beat["id"] not in only:
            continue
        dest = os.path.join(assets, beat["out"])
        if not redo_suffix and os.path.exists(dest) and os.path.getsize(dest) > 50000:
            print(f"= {beat['id']} already present, skipping")
            continue
        cmd = [sys.executable, FLOW_DRIVER, "gen",
               "--size", "2K",
               "--model", beat.get("model", "Nano Banana Pro"),
               "--prompt", assemble(beat, mod.LOCKS),
               "--out", dest]
        if beat.get("ref"):
            cmd += ["--ref", os.path.join(ROOT, JESUS_REF)]
        # Character locks by IMAGE (CAST-BIBLE principle). Text locks alone did NOT
        # hold the elder son across row 2 (s16/s17/s18 came back as three different
        # men), so a build may point each recurring character at an ACCEPTED still of
        # its own and every later shot of that character gets it attached.
        for cref in beat.get("char_refs", []):
            path = cref if os.path.isabs(cref) else os.path.join(build_dir, cref)
            if not os.path.isfile(path):
                raise SystemExit(f"{beat['id']}: char_ref not found: {path}")
            cmd += ["--ref", path]
        print(f"=== {beat['id']} -> {beat['out']} ===", flush=True)
        r = subprocess.run(cmd, cwd=ROOT)
        print(f"=== {beat['id']} exit={r.returncode} ===", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("build_dir")
    ap.add_argument("--dump", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--gen", action="store_true")
    ap.add_argument("--only", nargs="*", default=None)
    a = ap.parse_args()
    bdir = os.path.abspath(a.build_dir)
    mod = load_beats(bdir)
    if a.check or not (a.dump or a.gen):
        check(bdir, mod)
    if a.dump:
        dump(bdir, mod)
    if a.gen:
        check(bdir, mod)
        gen(bdir, mod, a.only)


if __name__ == "__main__":
    main()
