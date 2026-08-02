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

# Lessons distilled from Cameron's retained review complaints. This is included
# byte-identically in every prompt so a good scene description cannot accidentally
# omit the basic continuity and physical-reality rules.
QUALITY_LOCK = (
    "CONTINUITY AND PHYSICAL-REALITY LOCK: every recurring person keeps the same "
    "face, age, build, hair, beard, and clothing colours from shot to shot. People "
    "remain at believable human scale relative to one another and the setting. Every "
    "visible person has one coherent body with exactly two arms and two legs, complete "
    "natural hands and feet, and clear joints. Limbs, clothing, and bodies remain "
    "outside solid wood, stone, furniture, boats, and other people. Feet and knees "
    "make correct contact with ground, deck, furniture, or water exactly as the story "
    "requires. Gaze, travel direction, object placement, cause and effect, and the "
    "number of named people must match the narrated moment. ROUGH-DRAFT CONTINUITY "
    "LAW: when an earlier story frame is supplied as the first reference, treat its "
    "camera angle, blocking, character positions, action, direction of travel and "
    "major objects as the approved rough draft. Improve photographic realism and "
    "repair named defects without reinventing the composition or staging. Reject any "
    "image that breaks these rules."
)

# DEFECT LOCK — added 2026-08-01 (Claude worker 8) after the reroll rate held at
# ~30% across builds 05/06/07/08/09/10 at a flat $0.134/image, i.e. $2-3 of pure
# waste per video. The SAME four defect families caused nearly every reroll:
#   1. the subject looking into the lens        (rows 9 s01/s09/s22/s28/s31, row 10 s01/s04/s31/s38)
#   2. a stray unlocked figure at the frame edge, usually in CREAM, i.e. a second
#      unlocked Jesus                            (row 9 s14, row 10 s22 x2, s26, s31)
#   3. uncountable quantities                    (row 8, the ten coins)
#   4. recurring cast drifting off their sheets  (row 9 s21: short-haired John)
#
# The wording below is PORTED, not invented — each sentence is the phrasing that
# measurably fixed the defect in the QC.md of the build named above. The key
# lesson, learned the expensive way on row 10 s22 (a bare prohibition failed
# TWICE, the geometry fixed it in one pass): state the GEOMETRY — where the
# camera sits relative to the eyeline and which frame edge the gaze exits
# through — instead of only forbidding "looking at the camera".
DEFECT_LOCK = (
    "CANDID-FRAME LOCK: this is a photograph of something happening, not a posed "
    "portrait. NOBODY IN THE PICTURE LOOKS INTO THE LENS. Every person's gaze is "
    "aimed at another person, an object, or a point off the frame, and exits the "
    "picture through a named edge — above, below, left or right of the camera — so "
    "no one's pupils are ever centred on the lens. When a figure faces the camera "
    "the head is turned off the camera axis and the eyes travel clearly past it. "
    "No one acknowledges being photographed, poses, or presents themselves to the "
    "viewer. "
    "CAST-CLOSURE LOCK: the frame contains only the people the scene actually calls "
    "for — the named figures plus any background people the scene itself describes, "
    "and nobody else. In particular no unexplained extra body, shoulder, arm, head, "
    "hair, headscarf or back crowds into the EDGES of the picture, in the foreground "
    "or the background, in focus or out of focus, and no blurred stranger passes "
    "through the frame. NO CREAM OR OFF-WHITE CLOTH APPEARS ON "
    "ANYONE BUT JESUS anywhere in the frame, including out-of-focus edges — a pale "
    "shoulder at the edge of a shot reads as a second, unlocked Jesus and fails the "
    "picture. "
    "COUNT-AS-GEOMETRY LOCK: any quantity the narration names must be literally "
    "COUNTABLE in the picture — laid out separated and individually visible, never "
    "a vague handful, heap or crowd standing in for a number. If the story says a "
    "number, the viewer must be able to count that exact number of objects or "
    "people, and no extra ones. "
    "ANCHOR-RESTATEMENT LOCK: every recurring person carries their own locked "
    "description into THIS frame — face, age, build, hair length, beard state and "
    "garment colour exactly as locked, even when they are small, distant, "
    "out of focus, or seen from behind. No locked character is ever redrawn as a "
    "generic bystander and no two of them are given the same face."
)

# JESUS LOCK v4 — byte-identical in every prompt where Jesus appears.
# JESUS LOCK v5 — Cameron, 2026-07-30. Supersedes v4 once a face candidate is picked.
#
# His order: *"we need to make Jesus look more like the prince of peace 1 and 2 in MBM
# folder for examples and to mix that with what we know he might look like to detere
# the people who think he had to be middle eastern and to make sure that he has the
# 'his eyes as like a flame of fire'"*
#
# THIS REVERSES v4's own hard line ("Never Caucasian, never pale"), which Cameron wrote
# on 2026-07-15 and rejected finished work over. It is his call and it is recorded here
# so no future session "corrects" it back.
#
# ON THE TWO REFERENCE PAINTINGS: `Prince of peace 1.jpg` and `Prince of peace 2 .jpg`
# are Akiane Kramarik's paintings — the second is signed and watermarked. They are NOT
# attached as generation refs and the model is never told to match her work, because
# this ships in an app and that would make ~3,000 derivative copies of a living
# artist's paintings. What IS taken from them is a description of the QUALITIES
# Cameron is pointing at, which gets the same look without copying the paintings:
# longer tousled mid-brown hair with warm golden lights (not blue-black), a warm
# fair-olive complexion, pale luminous GREEN eyes, a straight noble nose, and above
# all a gentle, peaceful, unguarded expression rather than a grim reconstruction.
#
# ON "EYES AS A FLAME OF FIRE" (Revelation 1:14): that verse describes the GLORIFIED
# Christ in vision, and the no-halo/no-glow law still binds every mortal-ministry
# scene. So the fire is IN the iris — pale green shot through with amber and gold, lit
# from within, arresting — and the eyes do NOT emit light onto the face or surroundings.
# Literal glowing eyes across ~3,000 street-level scenes would read as horror, not
# reverence, and would break the anti-glow law on every frame.
JESUS_LOCK_V5 = (
    "JESUS LOCK v5: the SAME man as the attached JESUS-V2-REF image — identical face, "
    "hair and beard in every picture: a MIDDLE EASTERN JEWISH man of the first century "
    "about thirty-three years old, born and weathered in the Judean sun. His skin is "
    "WARM OLIVE-BROWN, sun-darkened and richly toned — clearly Middle Eastern, never "
    "fair, never pale, never European-looking. Strong Semitic features: a prominent "
    "aquiline nose, deep-set eyes under strong dark brows, high cheekbones, a broad "
    "weathered brow. Long thick tousled wavy hair to below the shoulders in DARK BROWN "
    "with warm sun-bleached bronze lights through it. A full dark brown beard. His "
    "EYES ARE THE FEATURE OF HIS FACE: large and deep-set, a LUMINOUS INDETERMINATE "
    "COLOUR you cannot quite name — green and amber and gold at once, lit from within "
    "like a flame of fire, piercing and alive and arresting, holding whoever meets "
    "them. The eyes themselves cast NO light onto his skin or surroundings. His "
    "expression is gentle, peaceful and unguarded — kindness and quiet strength, "
    "never stern, never grim. One plain undyed off-white cream wool robe with a simple "
    "mantle and cloth sash (only he wears cream), leather sandals. No halo, no glow, "
    "no rim-light, no light coming off him. Never Caucasian, never pale, never "
    "blue-eyed, never blond. "
    "HE IS DRY unless the narrated physical conditions actually wet him — rain, "
    "spray, immersion, washing, or another explicit water contact. In a dry scene his "
    "robe, hair and beard have no water droplets, drips, streams, runnels or wet "
    "strands. When he walks on water he is on TOP of it and therefore not wet; when "
    "he rides inside a boat through a breaking-wave storm, the spray correctly soaks "
    "him."
)

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

# WIDE-SHOT CAMERA GEOMETRY — promoted into the shared recipe 2026-08-01 from row 14
# (ten lepers), where 5 of 9 rerolls were this ONE failure: b01 b04 b05 b12 b26 all
# came back as a posed line of men facing the lens. The DEFECT_LOCK does NOT beat it,
# because the scene text says the figures "stand large in the near foreground" and the
# model resolves that phrasing as a group portrait. What fixed it in ONE pass every
# time was naming where the camera sits relative to the subjects' BACKS. The sentences
# below are PORTED byte-for-byte from the accepted row 14 prompts (b04, b19, b29) —
# nothing here is newly invented wording.
#
# Beat authors: this block is the floor, not a substitute. On any wide multi-figure
# beat you STILL state the camera-to-back geometry in the scene text itself
# ("THE CAMERA STANDS BEHIND <them> AND SHOOTS PAST THEM: their BACKS fill the near
# frame ... not one face is turned toward the lens"), and for travel beats name which
# way the backs face so the direction of travel cannot reverse. `--check` warns when a
# wide beat's scene never names the camera's position.
WIDE_GEOMETRY_LOCK = (
    "WIDE-SHOT CAMERA-GEOMETRY LOCK: this group is not arranged for the camera. The "
    "camera stands behind or beside the near figures and shoots PAST them, so the "
    "near figures are seen from behind, from the side, or in three-quarter from "
    "behind — never squared up to the lens, and NOT ONE FACE IS TURNED TOWARD THE "
    "LENS. The people are never lined up shoulder to shoulder presenting themselves "
    "to the viewer, and anyone walking or running is seen from the side or from "
    "directly behind, moving across the frame or away from it, never advancing into "
    "the camera."
)

# POSITIVE-INVENTORY — promoted 2026-08-01 from row 14 b08, where a SECOND, UNLOCKED
# JESUS (long loose hair, bare face, pale robe) appeared standing inside the line of
# ten lepers. Prohibitions had not stopped it; stating identity and headcount as an
# inventory of what IS in the frame fixed it in one pass. Ported from that prompt.
POSITIVE_INVENTORY_LOCK = (
    "POSITIVE-INVENTORY LOCK: identity and headcount are stated as what IS in the "
    "frame, not as what is forbidden. Every figure carries the garment colour, head "
    "covering and hair locked to him. When the narration names a number, exactly that "
    "many people stand in the frame and no additional one — ten men and no eleventh — "
    "each separated far enough to be counted individually."
)

# The identity half of the same lesson. Only added where Jesus is actually in the
# beat, so it can never pull him into a frame he does not belong in. Kept to the
# clause that is true in EVERY story — row 14 also added "the only man with long
# loose hair and an uncovered face", which was true there because the ten had their
# faces wrapped; that half stays a per-beat line, not a shared one.
JESUS_INVENTORY_LOCK = (
    "HE IS THE ONLY MAN IN CREAM ANYWHERE IN THE FRAME."
)

# Anti-panel clause — mandatory on every wide multi-figure still (Standing Law e).
# V1's wording said "ILLUSTRATION"; V2 is photographic, so the noun changes and
# nothing else does.
ANTI_PANEL = (
    "SINGLE UNIFIED PHOTOGRAPHIC FRAME, one scene edge to edge, NOT a grid, triptych, "
    "stacked panels or comic strip, no dividing lines, one picture only."
)

CLOSER = "One single continuous scene edge to edge, no border. 9:16 vertical."

# Recurring cast comes from the one canonical CHARACTER LAW source.  The old
# V2 dictionary described only four apostles and contradicted the approved
# sheets (for example: it gave clean-shaven John a beard and changed Andrew's
# locked olive-drab tunic to rust).  A group scene must never invent the other
# eight men as generic bearded fishermen.
def _canonical_cast_locks():
    path = os.path.join(
        ROOT, "media-production", "CHARACTERS", "character_refs.py"
    )
    spec = importlib.util.spec_from_file_location("mbm_character_refs", path)
    refs_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(refs_mod)

    key_to_slug = {
        "PETER": "peter",
        "ANDREW": "andrew",
        "JAMES-Z": "james",
        "JOHN": "john-beloved",
        "PHILIP": "philip",
        "BARTHOLOMEW": "bartholomew",
        "MATTHEW": "matthew",
        "THOMAS": "thomas",
        "JAMES-A": "james-son-of-alphaeus",
        "THADDAEUS": "thaddaeus",
        "SIMON-Z": "simon-the-zealot",
        "JUDAS-I": "judas-iscariot",
    }
    locks = {
        key: refs_mod.lock_text(slug) for key, slug in key_to_slug.items()
    }
    roster = " ".join(locks[key] for key in key_to_slug)
    locks["TWELVE-CANONICAL"] = (
        "TWELVE CANONICAL-CAST LOCK: the companions are exactly the Twelve in "
        "their approved gospel order. Every named man below keeps his own locked "
        "face, age, build, hair, beard state and tunic; no two are interchangeable, "
        "no face is cloned, and clean-shaven John never grows a beard. " + roster
    )
    return locks


CAST_LOCKS = _canonical_cast_locks()

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
    parts = [STYLE_V2, QUALITY_LOCK, DEFECT_LOCK, POSITIVE_INVENTORY_LOCK]
    if beat.get("wide"):
        parts.append(WIDE_DEFENSE)
        parts.append(WIDE_GEOMETRY_LOCK)
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
        # LOCK v5 is the live lock (Cameron picked face E, 2026-07-30).
        # This line said V4 while v5 sat unused above it, so every prompt
        # kept describing the OLD face and fought the new reference image.
        parts.append(JESUS_LOCK_V5)
        parts.append(JESUS_INVENTORY_LOCK)
    if beat.get("must_show"):
        parts.append("STORY MUST SHOW: " + beat["must_show"])
    if beat.get("must_not_show"):
        parts.append("HARD REJECTION CONDITIONS: " + beat["must_not_show"])
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
            if JESUS_LOCK_V5 not in p:
                fails.append(f"{beat['id']}: Jesus shot missing byte-identical LOCK v4")
            if not beat.get("ref"):
                fails.append(f"{beat['id']}: Jesus shot missing the REF line")
        for field in ("must_show", "must_not_show"):
            value = str(beat.get(field, "")).strip()
            if not value or "TODO" in value:
                fails.append(f"{beat['id']}: {field} is missing or unfinished")
        for w in DRIFT_WORDS:
            # Negative terms are lawful in must_not_show. Drift words in the scene
            # itself still fail because scene prose is what the model depicts.
            if w in beat["scene"].lower():
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
        # Row 14 lesson: on a wide multi-figure beat the shared blocks are not enough —
        # the SCENE text itself has to say where the camera stands relative to the
        # subjects' backs, or the model composes a posed line facing the lens.
        if beat.get("wide"):
            scene_low = beat["scene"].lower()
            if not any(k in scene_low for k in ("camera", "lens", "shot on")) or not any(
                k in scene_low for k in ("behind", "past them", "backs", "from the side",
                                         "profile", "three-quarter", "away from the")
            ):
                warns.append(
                    f"{beat['id']}: wide beat does not state camera-to-back geometry "
                    "in its own scene text (row 14: 5 of 9 rerolls were this)"
                )
        # A char_ref that does not exist must fail HERE, not after a credit is spent.
        for cref in beat.get("char_refs", []):
            path = cref if os.path.isabs(cref) else os.path.join(build_dir, cref)
            if not os.path.isfile(path):
                fails.append(f"{beat['id']}: char_ref missing on disk: {cref}")
        rough_ref = beat.get("rough_ref")
        if rough_ref:
            path = rough_ref if os.path.isabs(rough_ref) \
                else os.path.join(build_dir, rough_ref)
            if not os.path.isfile(path):
                fails.append(f"{beat['id']}: rough_ref missing on disk: {rough_ref}")
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
                    f"{'  ROUGH-REF ' + beat['rough_ref'] if beat.get('rough_ref') else ''}"
                    f"{''.join('  CHAR-REF ' + c for c in beat.get('char_refs', []))}\n")
            f.write(assemble(beat, mod.LOCKS) + "\n\n")
    print(f"wrote {out} ({len(mod.BEATS)} prompts)")


def _below_2k(path):
    """True if a still is smaller than Flow's 2K (1536x2752) 9:16 download.

    Checked from the JPEG header directly so it works with no Pillow dependency and
    costs nothing. A `.size` marker beside the file (written by flow_driver when it
    falls back) counts too, in case a file is unreadable.
    """
    if os.path.exists(os.path.splitext(path)[0] + ".size"):
        return True
    try:
        with open(path, "rb") as fh:
            data = fh.read(200000)
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            m = data[i + 1]
            if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                     0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                w = int.from_bytes(data[i + 7:i + 9], "big")
                return w < 1536
            if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
                i += 2
                continue
            i += 2 + int.from_bytes(data[i + 2:i + 4], "big")
    except Exception:
        return False
    return False


def gen(build_dir, mod, only, redo=False):
    assets = os.path.join(
        build_dir, getattr(mod, "OUTPUT_ASSET_DIR", "assets")
    )
    os.makedirs(assets, exist_ok=True)
    for beat in mod.BEATS:
        if only and beat["id"] not in only:
            continue
        dest = os.path.join(assets, beat["out"])
        if not redo and os.path.exists(dest) and os.path.getsize(dest) > 50000 \
                and not _below_2k(dest):
            print(f"= {beat['id']} already present, skipping")
            continue
        if os.path.exists(dest) and _below_2k(dest):
            # A 1K still counts as MISSING, not as done. flow_driver falls back to
            # the 1K original when Flow's upscaler is down and drops a .size marker
            # so "a later pass can re-pull it" — but no later pass existed, so 159
            # of the first 424 pictures (rows 10-13 entirely) sat at 768x1376,
            # BELOW the 1080x1920 delivery size. That is the exact upscaling the
            # anti-shimmer law forbids. Treating sub-2K as missing makes every
            # runner lap re-pull them automatically until they come back at 2K.
            print(f"~ {beat['id']} is BELOW 2K — re-pulling", flush=True)
        prompt = assemble(beat, mod.LOCKS)
        if redo and beat.get("redo_prompt"):
            prompt += (
                " CORRECTION PASS: Preserve every part of the supplied current "
                "production frame that is not explicitly changed below. "
                + beat["redo_prompt"]
            )
        cmd = [sys.executable, FLOW_DRIVER, "gen",
               "--size", "2K",
               "--model", beat.get("model", "Nano Banana Pro"),
               "--prompt", prompt,
               "--out", dest]
        # The prior still is the approved rough-draft composition.  Attach it
        # first so a realism rebuild improves the picture instead of inventing
        # unrelated blocking and boat mechanics.
        redo_source = beat.get("redo_source", "current") if redo else "rough"
        if redo and redo_source == "current" and os.path.isfile(dest):
            cmd += ["--ref", dest]
        elif redo_source == "rough" and beat.get("rough_ref"):
            path = beat["rough_ref"] if os.path.isabs(beat["rough_ref"]) \
                else os.path.join(build_dir, beat["rough_ref"])
            cmd += ["--ref", path]
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
    ap.add_argument(
        "--redo", action="store_true",
        help="regenerate selected existing outputs, using each beat's correction note",
    )
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
        gen(bdir, mod, a.only, redo=a.redo)


if __name__ == "__main__":
    main()
