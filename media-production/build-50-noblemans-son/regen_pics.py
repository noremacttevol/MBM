#!/usr/bin/env python3
"""Regenerate the four pictures Cameron named in denial #50 (2026-07-22).

His words: "Pictures : 57: Jesus too big, 1:17 both caharacters jesus and the
noble man look bad just redo that picture, 2:10 the character went grey when he
was brown haired and young looking, same for the next picture but the at 2:59 he
went back to brown and that looks good."

Verified frame by frame before touching anything:
  0:57 s5  — Jesus dwarfs the kneeling nobleman (scale break)
  1:17 s6  — Jesus is off-model (light BROWN wavy hair, not dark brown-black) and
             the nobleman reads grey and haggard
  2:10 s9  — the nobleman on the road has GREY-WHITE hair
  2:2x s10 — same grey man carries into the next picture
  2:59 s11 — CORRECT: dark brown hair, dark beard, teal robe. Cropped to
             assets/NOBLEMAN-REF.jpeg and used as the lock for all four re-rolls.

The nobleman is not on the character roster, so he is locked the same way the
well and the Samaritan were: by attaching a reference image cut from the frame
Cameron himself approved.
"""
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRIVER = HERE.parent / "flow_driver.py"
ASSETS = HERE / "assets"
REF = ASSETS / "NOBLEMAN-REF.jpeg"

PANEL = ("SINGLE UNIFIED ILLUSTRATION, one scene edge to edge, NOT a grid, NOT a triptych, "
         "no dividing lines or seams, ONE picture only, artwork fills the ENTIRE frame and "
         "bleeds to all four edges, no border, no vignette, one single tall upright vertical "
         "painting, horizon level.")

STYLE = ("Beautiful hand-painted 2D animation style, reverent and warm, like a classic "
         "illustrated storybook of scripture brought to life. Soft painterly brushstroke "
         "textures, glowing golden light, muted earth tones with warm gold highlights. "
         "First-century Galilee. Sacred, hushed tone. Not photorealistic. No text or captions "
         "in the image. Historically modest clothing. No modern objects.")

JESUS = ("JESUS LOCK v3: the SAME man in every picture — identical face, hair and beard: a "
         "Middle Eastern Jewish man of about thirty-three, warm tan olive-brown skin, "
         "shoulder-length DARK BROWN-BLACK wavy hair (never light brown, never chestnut, "
         "never auburn), a full DARK beard, kind warm BROWN eyes, one plain undyed off-white "
         "cream wool robe (only he wears cream). No halo, no glow. Never caucasian, never "
         "pale, never blue-eyed, never blond.")

NOBLE = ("NOBLEMAN LOCK — COPY HIM EXACTLY FROM THE ATTACHED REFERENCE IMAGE: a Galilean "
         "court official of about FORTY, DARK BROWN hair and a full DARK BROWN beard, warm "
         "olive skin, an unlined vigorous face — a man in his prime. He wears a teal "
         "blue-green robe with a brown belt over a grey-green undertunic. HIS HAIR AND BEARD "
         "ARE DARK BROWN, NEVER GREY, NEVER WHITE, NEVER SILVER; he is NOT elderly, NOT "
         "frail, NOT stooped, and his face is NOT deeply lined. He is the same man in every "
         "picture of this story.")

SCALE = ("SCALE LAW — every person in this picture is a normal adult human of the SAME size. "
         "Jesus is an ordinary-sized man standing on the same ground as everyone else: he is "
         "NOT larger than the others, NOT towering, NOT giant, and his head is NOT oversized. "
         "If one figure kneels and another stands, their proportions must still read as two "
         "ordinary men on one shared floor plane in correct perspective.")

ANAT = ("Every figure has two arms, two hands, two legs and one head, every limb joined to the "
        "correct body. Each named person appears exactly once.")

SHOTS = {
    "s5-signs-and-wonders":
        "Outside a sunlit stone house in Cana. The NOBLEMAN kneels on one knee before Jesus in "
        "the dust of the courtyard, hands open, begging him to come down and heal his son. "
        "Jesus stands facing him, speaking gently — 'except ye see signs and wonders, ye will "
        "not believe' — one hand open, his face kind and searching, not harsh. A few villagers "
        "watch quietly from the shaded archway behind. Warm midday light.",
    "s6-my-child-die":
        "Close on the two men outside the stone house. The NOBLEMAN, desperate, presses his "
        "clasped hands to his chest and looks up into Jesus's face, pleading — 'Sir, come down "
        "ere my child die.' Jesus looks back at him with steady compassion, listening, about to "
        "answer. Both faces clearly and warmly painted, neither distorted. A few villagers stand "
        "further back in the archway, out of focus. Warm midday light.",
    "s9-servants-meet-him":
        "The dusty road home to Capernaum at golden late afternoon, rolling Galilean hills and "
        "scattered olive trees, a village in the distance. The NOBLEMAN walks along the road "
        "seen from behind and to one side, and ahead of him two of his household servants come "
        "running toward him up the road with both arms raised, their faces bright with good "
        "news. All three are moving toward each other on the same road. Long golden shadows.",
    "s10-the-seventh-hour":
        "On the road at golden late afternoon. The NOBLEMAN has stopped still, facing the two "
        "servants who have just reached him; one servant gestures back toward the village as he "
        "tells the hour the fever left the boy. The nobleman's face is opening into "
        "astonishment and relief as he realises it was the very hour Jesus spoke. Warm low "
        "sunlight, the road and hills behind them.",
}


def gen(slug, body):
    out = ASSETS / f"{slug}.jpeg"
    jesus = JESUS if slug in ("s5-signs-and-wonders", "s6-my-child-die") else ""
    scale = SCALE if slug in ("s5-signs-and-wonders", "s6-my-child-die") else ""
    prompt = f"{PANEL} {STYLE} {body} {NOBLE} {jesus} {scale} {ANAT}"
    print(f"=== {slug}", flush=True)
    r = subprocess.run([sys.executable, str(DRIVER), "gen", "--prompt", prompt,
                        "--out", str(out), "--ref", str(REF)])
    ok = r.returncode == 0 and out.exists()
    print(("OK   " if ok else "FAIL ") + slug, flush=True)
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    todo = a.only or list(SHOTS)
    failed = [s for s in todo if not gen(s, SHOTS[s])]
    print("FAILED: " + ", ".join(failed) if failed else "ALL #50 PICTURES REGENERATED")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
