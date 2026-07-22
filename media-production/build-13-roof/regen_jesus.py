#!/usr/bin/env python3
"""Bring Jesus's FACE into #13 (Cameron denial #13, 2026-07-22).

His words: "This is old and needs to be updated to the version where we can use
Jesus' face."

Verified before touching anything: this build was made under the retired
face-never law. Jesus is either absent from the frame entirely or shown as the
back of a head — s8's own prompt header still reads "Face Law: his face is never
shown". In the three beats where Jesus is the one acting, he simply is not there:
the forgiveness beat is the paralysed man alone on his mat, and "Arise" is the
man standing up with nobody speaking to him.

Per the amended rule (face-shown via the master reference is correct), these
three beats are regenerated with Jesus present and his face shown, on-model to
JESUS LOCK v3. The lock is applied TEXT-ONLY per the face-law playbook —
attaching the bust reference makes the model echo the portrait.

The two men keep continuity with the rest of the build: the paralysed man is the
thin man in his early thirties with short dark curly hair and a sparse young
beard in an undyed flax-linen tunic, exactly as in s6/s9/s10 already.

Usage: python3 regen_jesus.py [--only s8-answered-thoughts ...]
"""
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRIVER = HERE.parent / "flow_driver.py"
ASSETS = HERE / "assets"

PANEL = ("SINGLE UNIFIED ILLUSTRATION, one scene edge to edge, NOT a grid, NOT a triptych, "
         "no dividing lines or seams, ONE picture only, artwork fills the ENTIRE frame and "
         "bleeds to all four edges, no border, no vignette, one single tall upright vertical "
         "painting.")

STYLE = ("Beautiful hand-painted 2D animation style, reverent and warm, like a classic "
         "illustrated storybook of scripture brought to life. Soft painterly brushstroke "
         "textures, glowing golden light, muted earth tones with warm gold highlights. "
         "First-century Capernaum, the dim packed room of a stone house with a broken clay "
         "roof overhead and a soft column of dusty daylight falling through it. Sacred, hushed "
         "tone. Not photorealistic. No text or captions in the image. No modern objects.")

# FACE SHOWN — the amended rule. His face is painted, on-model, and never hidden.
JESUS = ("JESUS LOCK v3, FACE SHOWN: a Middle Eastern Jewish man of about thirty-three, warm "
         "tan olive-brown skin, shoulder-length dark brown-black wavy hair, a full dark beard, "
         "kind warm BROWN eyes, one plain undyed off-white cream wool robe (only he wears "
         "cream). His face IS shown, clearly and warmly painted, turned toward the person he is "
         "speaking to — not hidden, not turned away, not seen from behind, not in shadow, not "
         "a silhouette. No halo, no glow, no ring of light, no rim-light around his head. Never "
         "caucasian, never pale, never blue-eyed, never blond.")

MAN = ("THE HEALED MAN: a thin man in his early thirties, short dark curly hair, a sparse young "
       "beard, olive skin, hollow cheeks, wearing a plain undyed flax-linen tunic — the same "
       "man as every other picture in this story.")

ANAT = ("Every figure has two arms, two hands, two legs and one head, every limb joined to the "
        "correct body. Each named person appears exactly once.")

SHOTS = {
    "s6-deepest-wound":
        "The forgiveness beat. The thin paralysed man lies on his back on the woven reed mat on "
        "the earthen floor, inside the soft column of dusty daylight from the broken roof. "
        "JESUS has crouched down low beside him on one knee, close, leaning in with one hand "
        "resting gently near the man's shoulder, and speaks quietly to him — telling him his "
        "sins are forgiven. Their eyes meet. The crowded room presses around them in the dim "
        "background, faces watching. The moment is tender and completely unhurried.",
    "s8-answered-thoughts":
        "Jesus answers what the scribes were only thinking. JESUS stands turned toward a row of "
        "seated scribes in pale robes along the wall of the dim room, his face calm and steady "
        "as he speaks straight to the objection they never said out loud, one hand open in a "
        "quiet unanswerable gesture. The scribes lean back, caught out — one presses his "
        "fingers to his beard, another glances at the man beside him. The paralysed man still "
        "lies on his mat in the column of light behind them. No confrontation, no anger, only "
        "quiet authority.",
    "s9-arise":
        "The command and the moment it lands. JESUS stands in the column of dusty daylight with "
        "one hand extended toward the mat, speaking the word — arise, take up thy bed and walk. "
        "In front of him THE HEALED MAN is rising to his feet off the woven reed mat, caught "
        "halfway up, one foot flat on the earthen floor and the other pushing off, arms spread "
        "slightly for balance, his legs unsteady like a newborn colt's, his face breaking open "
        "in disbelief. The packed room reacts all around them, hands to mouths. Warm daylight "
        "from the broken roof falls over both men.",
}


def gen(slug, body):
    out = ASSETS / f"{slug}.jpeg"
    prompt = f"{PANEL} {STYLE} {body} {JESUS} {MAN} {ANAT}"
    print(f"=== {slug}", flush=True)
    r = subprocess.run([sys.executable, str(DRIVER), "gen", "--prompt", prompt, "--out", str(out)])
    ok = r.returncode == 0 and out.exists()
    print(("OK   " if ok else "FAIL ") + slug, flush=True)
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    todo = a.only or list(SHOTS)
    failed = [s for s in todo if not gen(s, SHOTS[s])]
    print("FAILED: " + ", ".join(failed) if failed else "ALL #13 JESUS SHOTS REGENERATED")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
