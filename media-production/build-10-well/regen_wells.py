#!/usr/bin/env python3
"""Regenerate every shot of build-10-well that contains the well, conditioning
each one on assets/WELL-REF.jpeg.

WHY THIS EXISTS (Cameron, 2026-07-21 night): "the wells posts and reel thing was
change completely 8 times in every picture and some not even functional at all."
Two rounds of TEXT-ONLY well descriptions failed to hold the structure together —
the model re-invented the posts/beam/rope in every shot. Character faces solved
exactly this problem by attaching a locked reference IMAGE, so the well now gets
the same treatment: WELL-REF.jpeg rides as --ref on every well shot.

Usage:  python3 regen_wells.py [--only s3-disbelief ...]
"""
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRIVER = HERE.parent / "flow_driver.py"
ASSETS = HERE / "assets"
WELL_REF = ASSETS / "WELL-REF.jpeg"

STYLE = ("Beautiful hand-painted 2D animation style, reverent and warm, like a classic "
         "illustrated storybook of scripture brought to life. Soft painterly brushstroke "
         "textures, glowing golden light, muted earth tones with warm gold highlights. "
         "First-century Samaria. Sacred, hushed tone. Not photorealistic. No text or "
         "captions in the image. Historically modest clothing: rough-woven wool and linen "
         "in undyed earth colors. No modern objects.")

PANEL = ("SINGLE UNIFIED ILLUSTRATION, one scene edge to edge, NOT a grid, NOT a triptych, "
         "NOT stacked panels, no dividing lines or seams anywhere, ONE picture only showing "
         "ONE moment, artwork fills the ENTIRE frame and bleeds to all four edges, no "
         "border, no vignette, one single tall upright vertical painting, horizon level.")

# The whole point of this script: the well is COPIED from the reference image.
WELL = ("WELL LOCK — COPY THE WELL EXACTLY FROM THE ATTACHED REFERENCE IMAGE. The well in "
        "this picture must be the SAME PHYSICAL OBJECT as the attached reference, piece for "
        "piece: the same low round rim of rough pale limestone blocks, the same TWO upright "
        "wooden posts, the same ONE horizontal wooden roller resting in the notched post "
        "tops, the same bent wooden crank handle pegged to one end of that roller, the same "
        "rope wound around the middle of the roller and dropping straight down into the "
        "shaft, the same single wooden bucket on the rope's end. Do NOT redesign it, do NOT "
        "add a second beam or crossbar, do NOT add a pulley wheel, a roof, a canopy, metal "
        "or chain, do NOT remove the crank handle, do NOT change how many posts there are. "
        "It must remain a WORKING windlass where the posts hold the roller, the roller holds "
        "the rope, and the rope holds the bucket. Only the camera angle and the distance may "
        "change between pictures — the well itself never changes.")

JESUS = ("JESUS LOCK v3: the SAME man in every picture — identical face, hair and beard: a "
         "Middle Eastern Jewish man of about thirty-three, warm tan olive-brown skin, "
         "shoulder-length dark brown-black wavy hair, a full dark beard, kind warm BROWN "
         "eyes, one plain undyed off-white cream wool robe (only he wears cream). No halo, "
         "no glow. Never caucasian, never pale, never blue-eyed, never blond.")

WOMAN = ("WOMAN LOCK: the SAME Samaritan woman in every picture — a Middle Eastern woman of "
         "about thirty-five, warm olive skin, dark brown hair partly covered by a simple "
         "dark-red head shawl, wearing a plain terracotta-and-brown robe. Weary but "
         "dignified, expressive dark eyes. Same face and same clothing in every shot.")

SEATED = ("SEATED CONVERSATION (Cameron, 2026-07-21): these two are simply SITTING AND "
          "TALKING like two real people having a long honest conversation in the heat — "
          "relaxed natural body language, hands resting or gesturing easily. They are NOT "
          "posed standing stiffly around the well, NOT leaning on it. Jesus sits on the "
          "stone rim; she sits facing him on a low flat rock a comfortable few feet away, "
          "her clay water jar SET DOWN on the ground beside her. The well stands OFF TO ONE "
          "SIDE as quiet background furniture — never between them, never centered, never "
          "the subject.")

LAND = ("Dry Samaria landscape: low bare hills, a few olive trees, the small stone town of "
        "Sychar on a hill in the far distance, hard bright noon light, bleached warm colors.")

ANAT = ("Every figure has two arms, two hands, two legs and one head, every limb joined to "
        "the correct body. Each person appears exactly once.")

SHOTS = {
    "s1-noon-path":
        "A lone Samaritan woman seen from a THREE-QUARTER REAR ANGLE, walking AWAY from the "
        "camera down a dusty path at blazing noon — we look past her back and shoulder at the "
        "well AHEAD of her in the middle distance, the destination she is walking toward. Her "
        "clay water jar rides on her shoulder. The small stone town of Sychar sits on a hill "
        "FAR BEHIND HER, at her back. She is NOT walking toward the camera. "
        + WOMAN + " " + WELL + " " + LAND,

    "s2-traveler":
        "A tired traveler resting alone at the well in the blazing noon: JESUS sits by himself "
        "on the stone rim, worn out from the road, one hand resting on his knee, looking off "
        "toward the path with quiet patience — a Jewish man resting alone in Samaria. In the "
        "middle distance the Samaritan woman is just arriving down the path, carrying her clay "
        "water jar, still far from him. "
        + JESUS + " " + WOMAN + " " + WELL + " " + LAND + " " + ANAT,

    "s3-disbelief":
        "The moment she answers him, guarded and surprised: JESUS sits on the stone rim having "
        "just asked her for a drink, one hand open in an easy friendly gesture; the Samaritan "
        "woman sits facing him on a low flat rock, leaning back very slightly with her eyebrows "
        "raised in frank disbelief that a Jewish man would speak to her at all — wary, not yet "
        "softened, mid-sentence. "
        + SEATED + " " + JESUS + " " + WOMAN + " " + WELL + " " + LAND + " " + ANAT,

    "s4-living-water":
        "The living-water promise: JESUS sits on the stone rim leaning slightly forward toward "
        "her, both hands open and warm as he describes a spring of water rising up inside a "
        "person forever; the Samaritan woman sits facing him on a low flat rock, her guard "
        "beginning to drop — head tilted, listening hard, puzzled and drawn in at once. "
        + SEATED + " " + JESUS + " " + WOMAN + " " + WELL + " " + LAND + " " + ANAT,

    "s5-conversation-anchor":
        "The heart of the conversation: JESUS sits on the stone rim, quiet and steady, telling "
        "her plainly who he is, one hand resting open on his knee; the Samaritan woman sits "
        "facing him on a low flat rock, utterly still, one hand come up to her chest, her eyes "
        "fixed on his face as recognition breaks over her — fully known and still spoken to "
        "with respect. "
        + SEATED + " " + JESUS + " " + WOMAN + " " + WELL + " " + LAND + " " + ANAT,

    "s6-disciples":
        "His followers come back and stop short: JESUS and the Samaritan woman still sit "
        "talking quietly in the foreground, unbothered; in the MIDDLE DISTANCE behind them a "
        "group of five Jewish disciples carrying bread and provisions has halted on the path, "
        "standing still and staring, visibly stunned that he is talking with her — surprised, "
        "not angry, and none of them says a word. The disciples are clearly smaller and "
        "further away than the two seated figures, on the same ground plane. "
        + SEATED + " " + JESUS + " " + WOMAN + " " + WELL + " " + LAND + " " + ANAT,

    "s7-jar-left-anchor":
        "She leaves her jar behind: JESUS sits alone on the stone rim in the foreground, "
        "watching her go with quiet warmth; her clay water jar stands ABANDONED on the flat top "
        "of the well rim right beside him, clearly left behind. In the middle distance the "
        "Samaritan woman hurries AWAY from the camera up the path toward the town of Sychar, "
        "seen from behind, her hands EMPTY — she carries nothing at all. "
        + JESUS + " " + WOMAN + " " + WELL + " " + LAND + " " + ANAT,

    "s9-road-filling":
        "The whole town comes out to meet him. STRICT GEOMETRY: the camera stands BEHIND the "
        "crowd, low on the road, so we look PAST their backs and shoulders UP the path AWAY "
        "from the viewer. The Samaritan woman is at the FRONT of the group, seen from BEHIND at "
        "three-quarter rear — her back to the camera — striding AWAY from us up the road, one "
        "arm raised pointing AHEAD toward the well on the rise where JESUS waits, her face "
        "turned in profile back over her shoulder to call the townspeople on. HER HANDS ARE "
        "EMPTY: she carries NO water jar — the jar has been left behind and is visible resting "
        "on the well rim beside Jesus in the distance. Behind her a crowd of Samaritan townsmen "
        "and women of all ages follow her up the same road, ALL moving AWAY from the camera in "
        "the SAME direction she is, toward the well — nobody walks toward the viewer. Jesus is "
        "small in the distance ahead, seated at the well, waiting. "
        + JESUS + " " + WOMAN + " " + WELL + " " + LAND + " " + ANAT,

    "s3b-he-asked-her-for-a-drink":
        "The impossible sentence, the moment before she answers: JESUS sits on the stone rim "
        "in the blazing noon, tired and completely at ease, and he has just held out one open "
        "hand toward her clay water jar and asked her for a drink — his hand is plainly "
        "extended, palm up and empty, and there is no cup and no bucket in it. The Samaritan "
        "woman has stopped a few paces short of the well with the jar still on her shoulder "
        "and both her hands on it, not yet set down, not yet seated; she is looking straight "
        "at him, motionless, her mouth just parted, caught completely off guard that he spoke "
        "to her at all. She has NOT yet answered. Nobody else is anywhere in the picture. "
        + JESUS + " " + WOMAN + " " + WELL + " " + LAND + " " + ANAT,

    "s6b-the-disciples-stop-short":
        "THE RETURNING DISCIPLES, halted dead on the dusty path at noon, and EVERY ONE OF "
        "THEM IS LOOKING IN THE SAME DIRECTION AT THE SAME THING. STRICT GEOMETRY: the five "
        "disciples stand together in the RIGHT HALF of the frame, close to the camera and "
        "large; the well with JESUS and the Samaritan woman seated and talking beside it "
        "stands in the LEFT HALF, in the middle distance and clearly smaller, on the same "
        "ground plane. Every single disciple has his head and body turned toward that seated "
        "pair on the left, so that every gaze in the picture converges on them — not one of "
        "them looks at the camera, at the ground, or off in any other direction. They are "
        "stopped mid-step, not walking. Five Jewish men in rough wool tunics of dun, faded "
        "brown, olive and grey-blue, all with SHORT hair or head-cloths, and not one of them "
        "in cream or off-white: a broad bearded man with a cloth-wrapped bundle of bread "
        "half-lowered and forgotten in his hands, a younger man beside him, a man gripping a "
        "water-skin, and two more behind. Every one of their faces is painted fully and "
        "clearly, astonished but not angry, and not one of them says a word. "
        + JESUS + " " + WOMAN + " " + WELL + " " + LAND + " " + ANAT,
}


def gen(slug, body):
    out = ASSETS / f"{slug}.jpeg"
    prompt = f"{PANEL} {STYLE} {body}"
    print(f"=== {slug} ===", flush=True)
    r = subprocess.run([sys.executable, str(DRIVER), "gen", "--prompt", prompt,
                        "--out", str(out), "--ref", str(WELL_REF)])
    ok = r.returncode == 0 and out.exists()
    print(("OK   " if ok else "FAIL ") + slug, flush=True)
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    if not WELL_REF.exists():
        sys.exit(f"missing reference: {WELL_REF}")
    todo = a.only or list(SHOTS)
    failed = [s for s in todo if not gen(s, SHOTS[s])]
    print("FAILED: " + ", ".join(failed) if failed else "ALL WELL SHOTS REGENERATED")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
