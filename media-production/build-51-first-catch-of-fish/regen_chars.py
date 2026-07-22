#!/usr/bin/env python3
"""Regenerate every still of #51 under CHARACTER LAW.

WHY (Cameron denial #51, 2026-07-22): "Characters dont match the new characters
we have made. neeeds updated pictures." This build predates the character sheets:
its prompts described Peter and the sons of Zebedee from imagination ("a strong
Galilean fisherman of about forty... in a plain undyed brown wool tunic"), which
is not the locked Peter at all — the sheet puts him in a BLUE-GREY tunic and in
his mid-thirties. character_ref_gate.py fails this build on james + john-beloved.

Every shot now pastes the locked spec text verbatim (pulled live from
CHARACTERS/, so it can never drift from the sheet) AND attaches that character's
three reference jpegs as --ref. Jesus stays TEXT-ONLY per the face-law playbook —
attaching his bust ref makes the model echo the portrait.

Usage: python3 regen_chars.py [--only s5-the-great-catch ...]
"""
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MP = HERE.parent
DRIVER = MP / "flow_driver.py"
ASSETS = HERE / "assets"
sys.path.insert(0, str(MP / "CHARACTERS"))
from character_refs import lock_text, refs  # noqa: E402

STYLE = ("Beautiful hand-painted 2D animation style, reverent and warm, like a classic "
         "illustrated storybook of scripture brought to life. Soft painterly brushstroke "
         "textures, glowing golden light, muted earth tones with warm gold highlights. "
         "First-century Galilee. Sacred, hushed tone. Not photorealistic. No text or "
         "captions in the image. Historically modest clothing: rough-woven wool and linen "
         "in undyed earth colors. No modern objects.")

PANEL = ("SINGLE UNIFIED ILLUSTRATION, one scene edge to edge, NOT a grid, NOT a triptych, "
         "NOT stacked panels, no dividing lines or seams anywhere, ONE picture only showing "
         "ONE moment, artwork fills the ENTIRE frame and bleeds to all four edges, no "
         "border, no vignette, one single tall upright vertical painting, horizon level.")

JESUS = ("JESUS LOCK v3: the SAME man in every picture — identical face, hair and beard: a "
         "Middle Eastern Jewish man of about thirty-three, warm tan olive-brown skin, "
         "shoulder-length dark brown-black wavy hair, a full dark beard, kind warm BROWN "
         "eyes, one plain undyed off-white cream wool robe (only he wears cream). No halo, "
         "no glow. Never caucasian, never pale, never blue-eyed, never blond.")

ANAT = ("Every figure has two arms, two hands, two legs and one head, every limb joined to "
        "the correct body. Each named person appears exactly once in the picture.")

# The brothers must be told apart on sight, every single frame.
BROTHERS = ("THE TWO BROTHERS MUST BE TELLABLE APART AT A GLANCE, in this and every other "
            "picture: JAMES is the one WITH the short dark beard; JOHN is the younger, "
            "CLEAN-SHAVEN one. Never swap these, never give John a beard, never shave James.")

SHOTS = {
    "s1-crowds-at-the-lake": (
        ["peter"],
        "Early grey-gold dawn over the wide Lake of Gennesaret, still water catching the first "
        "pale light, low mist lifting off the surface. Along the pebbled shore in the lower half "
        "of the frame two empty wooden fishing boats are drawn up at the water's edge. In the "
        "foreground PETER kneels at the water wringing out a heavy net, tired after a long empty "
        "night. A crowd of ordinary Galilean villagers of every age in earth-toned brown, russet "
        "and olive wool gathers along the shore, pressing gently forward, faces turned "
        "expectantly toward the boats. Nobody in the crowd wears cream or off-white."),
    "s2-teaching-from-the-boat": (
        ["peter"],
        "Soft golden early-morning light over the calm lake. Jesus sits in the stern of PETER's "
        "wooden fishing boat, pushed out a little way from the pebbled shore, teaching the crowd "
        "gathered along the water's edge — leaning forward gently, one hand open in a quiet "
        "gesture. Near the oar PETER sits quietly listening. On the shore behind, the crowd of "
        "villagers in brown, russet and olive wool sits and stands along the pebbles, faces "
        "lifted toward the boat. Only Jesus wears cream. " + JESUS),
    "s3-launch-out-into-the-deep": (
        ["peter"],
        "Bright clear morning on the open lake, the shore now small behind them. Jesus, seated in "
        "the wooden boat, turns to PETER and lifts a hand toward the deeper water further out, "
        "bidding him launch out into the deep and let down the nets. PETER listens with a tired, "
        "doubtful yet respectful face, one hand resting on the wooden gunwale, the empty folded "
        "net heaped at their feet. The two of them alone in the boat on wide sunlit water. Only "
        "Jesus wears cream. " + JESUS),
    "s4-toiled-all-night": (
        ["peter"],
        "Full clear morning light on the open lake. PETER leans far over the side of the wooden "
        "boat and lets the long fishing net down into the deep blue-green water with both hands, "
        "his face weary and unconvinced after a whole night of catching nothing, yet obeying "
        "anyway. The heavy wet folds of net slide over the gunwale into the water. He is alone at "
        "the rail; the wide bright lake stretches empty around the boat."),
    "s5-the-great-catch": (
        ["peter", "john-beloved"],
        "Dazzling mid-morning light on the lake. PETER and JOHN haul with all their strength at "
        "the fishing net, which is bursting with an enormous silver multitude of fishes — the net "
        "bulging and beginning to break, fish spilling and flashing over the side into the boat, "
        "water sheeting everywhere. Peter leans back against the huge weight, his weary face "
        "breaking open into astonishment; JOHN, the younger clean-shaven brother, pulls hard "
        "beside him. The catch is so great the net tears. " + BROTHERS),
    "s6-both-boats-sinking": (
        ["peter", "james", "john-beloved"],
        "Bright morning on the lake. Two wooden fishing boats sit low and heavy in the water, both "
        "loaded to the brim with a vast catch of silver fish, gunwales nearly awash. In the first "
        "boat PETER beckons urgently with one raised arm to his partners in the second boat close "
        "by; JAMES and JOHN, the two sons of Zebedee, row hard toward him to help. Great heaps of "
        "fish glint in both boats; the strained nets hang over the sides. " + BROTHERS),
    "s7-at-his-knees": (
        ["peter", "james", "john-beloved"],
        "Bright morning light in the laden fishing boat, heaped silver fish shining all around. "
        "PETER has fallen on his knees before Jesus in the boat, bowing low at his feet with one "
        "hand pressed to his own chest, overwhelmed and undone. Jesus stands calm and kind above "
        "him, looking down at Peter with gentle compassion, not reproach. At the edge of the boat "
        "JAMES and JOHN stand back in quiet awe. Only Jesus wears cream. "
        + BROTHERS + " " + JESUS),
    "s8-fear-not": (
        ["peter", "james", "john-beloved"],
        "Tender bright morning light in the boat on the calm lake. Jesus bends slightly toward the "
        "kneeling PETER and reaches out one reassuring hand toward him, his face warm and steady, "
        "telling him not to be afraid — that from henceforth he will catch men. PETER looks up at "
        "him with wonder and dawning hope, heaps of silver fish around them. Just behind, JAMES "
        "and JOHN watch quietly. Only Jesus wears cream. " + BROTHERS + " " + JESUS),
    "s9-forsook-all": (
        ["peter", "james", "john-beloved"],
        "Warm late-morning light on the pebbled lakeshore. The two wooden fishing boats lie drawn "
        "up on the shore behind, still heaped with the great catch and the mended nets, left just "
        "where they rest. Walking AWAY from the boats up the rising shore path, seen from a little "
        "behind and to one side, go Jesus and the three fishermen who follow him — PETER, JAMES "
        "and JOHN — having left everything behind. Jesus walks ahead, leading them gently up from "
        "the water. All four move in the SAME direction, away from the camera and away from the "
        "boats. Only Jesus wears cream. " + BROTHERS + " " + JESUS),
}


def gen(slug, chars, body):
    out = ASSETS / f"{slug}.jpeg"
    locks = " ".join(lock_text(c) for c in chars)
    prompt = f"{PANEL} {STYLE} {body} {locks} {ANAT}"
    ref_args = []
    for c in chars:
        for r in refs(c):
            ref_args += ["--ref", str(r)]
    print(f"=== {slug}  [{', '.join(chars)}]", flush=True)
    r = subprocess.run([sys.executable, str(DRIVER), "gen", "--prompt", prompt,
                        "--out", str(out)] + ref_args)
    ok = r.returncode == 0 and out.exists()
    print(("OK   " if ok else "FAIL ") + slug, flush=True)
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    todo = a.only or list(SHOTS)
    failed = [s for s in todo if not gen(s, *SHOTS[s])]
    print("FAILED: " + ", ".join(failed) if failed else "ALL #51 STILLS REGENERATED")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
