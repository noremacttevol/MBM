#!/usr/bin/env python3
"""Regenerate every people-shot of #19 under CHARACTER LAW.

Cameron denial #19 (2026-07-22): "pictures for peters meeting are out of order
and look like compltetely differnt people this al needs to be redone with better
ways of matching the characters, the ones who are in other stories, peter and
Jesus and the new people the other men in the boat need to be the same in every
frame and that needs to be a laaaw."

Verified before touching anything: Peter here is in a rust-brown robe, but his
locked sheet puts him in a BLUE-GREY tunic — so he does not match the Peter in
#7, #51 or any other story. The boat crew also drifts, and one of them is an
elderly white-bearded man, which no one at John 21 should be (the seven were
Peter, Thomas, Nathanael, James, John and two more — all working-age men).

Fix: every shot pastes the locked spec for Peter, John and Thomas straight from
CHARACTERS/ (read live, so it cannot drift) and attaches their reference jpegs.
The BOAT CREW is fixed to those three so the same faces ride through every frame.
Jesus stays TEXT-ONLY per the face-law playbook.

Usage: python3 regen_chars.py [--only s13-peter-leap ...]
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

CREW = ["peter", "john-beloved", "thomas"]

PANEL = ("SINGLE UNIFIED ILLUSTRATION, one scene edge to edge, NOT a grid, NOT a triptych, "
         "no dividing lines or seams, ONE picture only, artwork fills the ENTIRE frame and "
         "bleeds to all four edges, no border, no vignette, one single tall upright vertical "
         "painting, horizon level.")

STYLE = ("Beautiful hand-painted 2D animation style, reverent and warm, like a classic "
         "illustrated storybook of scripture brought to life. Soft painterly brushstroke "
         "textures, glowing golden light, muted earth tones with warm gold highlights. "
         "First-century Galilee, the Sea of Tiberias at dawn. Sacred, hushed tone. Not "
         "photorealistic. No text or captions in the image. No modern objects.")

JESUS = ("JESUS LOCK v3: the SAME man in every picture — identical face, hair and beard: a "
         "Middle Eastern Jewish man of about thirty-three, warm tan olive-brown skin, "
         "shoulder-length dark brown-black wavy hair, a full dark beard, kind warm BROWN "
         "eyes, one plain undyed off-white cream wool robe (only he wears cream). No halo, "
         "no glow. Never caucasian, never pale, never blue-eyed, never blond.")

# The single rule Cameron asked to be made law.
SAME = ("SAME-MEN LAW: the men in this boat are the SAME THREE MEN in every single picture of "
        "this story — Peter, John and Thomas, exactly as described and exactly as shown in the "
        "attached reference images. No extra disciples appear, nobody is swapped out between "
        "pictures, and there is NO elderly white-haired or white-bearded man anywhere in this "
        "story — all three are working-age fishermen.")

ANAT = ("Every figure has two arms, two hands, two legs and one head, every limb joined to the "
        "correct body. Each named person appears exactly once in the picture.")

SHOTS = {
    "s2-empty-net": (
        "Grey pre-dawn on the flat calm Sea of Tiberias. PETER, JOHN and THOMAS sit slumped in "
        "the open fishing boat after a whole night of catching nothing — the empty net hangs "
        "slack over the gunwale, dripping. Peter stares out over the water, tired and hollow; "
        "the other two rest on the oars. Cold blue-grey light, mist on the water, no fish "
        "anywhere.", False),
    "s8-call-shore": (
        "First pale gold of sunrise on the water. In the boat PETER, JOHN and THOMAS turn "
        "together to look toward the distant shore, where a lone figure stands small and far "
        "off beside a thin thread of smoke, calling out across the water to them. The three of "
        "them are caught mid-turn, listening. The figure on the shore is DISTANT and SMALL, "
        "seen at a distance, his face not readable at this range.", False),
    "s9-answer-nothing": (
        "Early gold light on the still water. In the boat PETER answers the far-off voice with "
        "one hand half-raised — having to say it out loud to a stranger: no, nothing, all "
        "night. JOHN holds up the empty net so its slack mesh hangs plainly visible; THOMAS "
        "looks toward the shore. The distant figure remains small and far off on the beach.",
        False),
    "s10-cast-right": (
        "Morning light on the lake. PETER and JOHN heave the long fishing net up and out over "
        "the RIGHT side of the boat, the mesh spreading in the air above the water as it flies; "
        "THOMAS leans on the oar watching it go. Their faces are doubtful but obeying. The wide "
        "bright water all around, the shore a thin gold line behind.", False),
    "s11-net-full": (
        "Brilliant morning light. The net comes up so full of silver fish that PETER and JOHN "
        "cannot haul it in — it bulges and strains over the side, fish flashing and boiling in "
        "the mesh, water sheeting off it. THOMAS grabs the gunwale to steady the boat as it "
        "heels. All three faces are astonished.", False),
    "s12-realization": (
        "Bright gold morning. In the laden boat JOHN goes very still, one hand on Peter's arm, "
        "and says quietly that it is the Lord — his face full of recognition. PETER turns "
        "sharply to look toward the distant shore, understanding breaking over him. THOMAS "
        "stares between them. The small far figure still stands on the beach by the smoke.",
        False),
    "s13-peter-leap": (
        "Bright morning on the water. PETER throws himself off the bow of the boat into the sea "
        "— caught mid-leap above the water, arms out, his belt fastened, absolutely committed. "
        "Behind him in the boat JOHN and THOMAS look up startled, the heavy net of fish still "
        "hanging over the side. The shore is ahead of him in the distance.", False),
    "s14-swim": (
        "Morning light on the shallows. PETER swims hard for the shore, cutting through the "
        "gold-lit water with one arm reaching forward, his face set and eager, hair and beard "
        "streaming wet. Behind him the boat follows slowly, JOHN and THOMAS dragging the "
        "loaded net through the water toward the beach. The thin smoke of a fire rises on the "
        "sand ahead.", False),
    "s16-breakfast": (
        "Warm full sunrise on the beach. Jesus kneels at the small charcoal fire and hands a "
        "piece of bread to PETER, who kneels facing him, soaked through from the swim, his face "
        "open and undone. JOHN and THOMAS sit close by on the sand, quiet and watching. Fish "
        "lie on the coals and the loaded net rests at the water's edge behind them. Only Jesus "
        "wears cream. Nobody speaks.", True),
}


def gen(slug, body, with_jesus):
    out = ASSETS / f"{slug}.jpeg"
    locks = " ".join(lock_text(c) for c in CREW)
    prompt = f"{PANEL} {STYLE} {body} {locks} {SAME} {JESUS if with_jesus else ''} {ANAT}"
    ref_args = []
    for c in CREW:
        for r in refs(c):
            ref_args += ["--ref", str(r)]
    print(f"=== {slug}", flush=True)
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
    print("FAILED: " + ", ".join(failed) if failed else "ALL #19 PEOPLE-SHOTS REGENERATED")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
