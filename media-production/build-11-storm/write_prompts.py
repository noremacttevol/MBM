#!/usr/bin/env python3
"""Emit PROMPTS.md for #11 (Calming the Storm) with the CHARACTER-LAW locks
pasted verbatim from CHARACTERS/. Run it, don't hand-edit PROMPTS.md.

Rebuild 2026-07-21 (Machine A) after Cameron rejected the shipped cut: the
captions were the pre-CAPTION-LAW paragraph dumps, and the boat was full of
imagined strangers. The four men at the oars are Peter, Andrew, James and John
(Mark 1:16-20) and they now come off their locked sheets in every shot, so this
storm has the same faces as every other video they are in.

Two beats were also too long for one picture (STORY-COVERAGE law): n1 carried
the whole crew introduction on the wide fleet shot, and n2 carried the geography
AND the swamping on one storm shot. Each is split, each half gets its own still.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "CHARACTERS"))
from character_refs import lock_text  # noqa: E402

STYLE = ("Beautiful hand-painted 2D animation style, reverent and warm, like a classic "
         "illustrated storybook of scripture brought to life. Soft painterly brushstroke "
         "textures, muted earth tones under cool moonlight. First-century Judea. Sacred, "
         "hushed tone. Not photorealistic. No text or captions in the image. Historically "
         "modest clothing: rough-woven wool and linen in undyed earth colors. No modern "
         "objects.")

# Byte-identical to jesus_face_gate.LOCK_V3 — do not reword, the gate compares bytes.
JESUS = ("JESUS LOCK v3: the SAME man as the attached JESUS-MASTER-REF images — identical "
         "face, hair and beard in every picture: a Middle Eastern Jewish man of about "
         "thirty-three, warm tan olive-brown skin, shoulder-length dark brown-black wavy "
         "hair, a full dark beard, kind warm BROWN eyes, one plain undyed off-white cream "
         "wool robe (only he wears cream). No halo, no glow. Never caucasian, never pale, "
         "never blue-eyed, never blond.\nHe is bare-headed in every shot, NO hood, hair "
         "worn loose and uncovered.\nREF: jesus-master-ref")

BOAT = ("BOAT LOCK: one and the SAME large wooden Galilean fishing boat in every shot — a "
        "broad, heavy open boat about twenty-five feet long, a single tall wooden mast "
        "stepped just forward of center with a furled square sail on its yard, a high "
        "upswept curved prow and a matching high curved stern, weathered grey-brown planks, "
        "thick coiled ropes along both gunwales. Same boat, same size, same shape, same "
        "rigging, every time — big enough to hold thirteen men, never a smaller or "
        "different boat.")

CREW = ("CREW LOCK: the boat always holds the SAME full company — Jesus and his TWELVE "
        "disciples, THIRTEEN men aboard in all, no more and no fewer, crowding the big boat "
        "in every shot. Four of them are named and locked to their reference sheets — "
        "Peter, Andrew, James and John — and they keep the same faces, the same hair and "
        "the same tunic colours in every shot of this video and in every other video they "
        "appear in. The other eight are sturdy Galilean fishermen with weathered "
        "dark-bearded faces in soaked undyed wool tunics of brown, dun and deep olive "
        "(never cream). The number of men never changes from shot to shot. "
        "TUNIC COLOURS ARE NAME TAGS: the ONLY man in a BLUE-GREY tunic is Peter, the "
        "only man in OLIVE-DRAB is Andrew, the only man in DARK OCHRE-BROWN is James, "
        "the only man in FADED GREY-BLUE is John. No background disciple wears any of "
        "those four colours. Peter is NOT an old man — he is in his mid-thirties with "
        "thick DARK curly hair and a full DARK beard, no grey and no white anywhere in "
        "his hair or beard; never paint a grey-haired or white-bearded elder in the "
        "blue-grey tunic. John is the YOUNGEST man in the boat, clean-shaven, with DARK "
        "wavy hair to the jaw — never sandy, never light brown.")

QUALITY = ("CLEAN ART, NO GLITCHES: every person has correct human anatomy — one head, one "
           "neck, two arms, two hands with five fingers each, two legs — natural "
           "proportions, no extra/missing/fused limbs or fingers, no melted or distorted "
           "faces, every background face fully and cleanly drawn. Nobody is drawn as a "
           "giant beside the others — every man is normal human size next to every other "
           "man, correctly scaled to the boat he is standing in. Every object rests on a "
           "solid surface or is firmly gripped in a hand — NOTHING floats in mid-air. When "
           "anyone bails water it is with a SOLID WOODEN BUCKET or a glazed clay jar that "
           "actually holds water — never a woven basket, never cupped bare hands. No modern "
           "objects. One single continuous scene painted edge to edge, filling the entire "
           "frame with no border, no paper margin. 9:16 vertical.")

PANEL = ("SINGLE UNIFIED ILLUSTRATION, one scene edge to edge, NOT a grid, triptych, "
         "stacked panels or comic strip, no dividing lines, one picture only.")

# (slug, headline, [lock tokens], scene text)
SHOTS = [
    ("s1-evening-shore", "evening on the shore, the day of teaching done",
     ["JESUS", "BOAT", "CREW", "PETER SHEET", "ANDREW SHEET", "JAMES SHEET", "JOHN SHEET"],
     "The last gold light of evening fading to dusk on the pebbled shore of the Sea of "
     "Galilee. The one large wooden fishing boat is drawn up at the water's edge. Jesus "
     "stands beside it, worn and tired after a long day of teaching, his face shown clearly "
     "and gently as he turns to speak to his friends, warm brown eyes kind and weary, cream "
     "wool robe catching the last warm light. Nearest him and clearly recognisable stand "
     "the four fishermen: Peter in his blue-grey tunic on Jesus's right, his brother Andrew "
     "in olive-drab beside him, James in dark ochre-brown and clean-shaven young John in "
     "faded grey-blue behind them. The rest of the twelve stand in a loose group around "
     "them ready to push off — none of them in cream. The evening water is calm and wide "
     "behind them, first stars coming out."),

    ("s2-little-ships", "they took him, and other little ships followed",
     ["BOAT"],
     "Night falling on the Sea of Galilee, seen wide and from a distance. The one large "
     "fishing boat — crowded with its full company of thirteen men seated calmly, all of "
     "them small and far off, their faces not readable at this range — pushes out from the "
     "dark shore onto calm moonlit water, leading the way. Behind it several smaller wooden "
     "boats follow, the \"other little ships\" of the verse, their fishermen working oars "
     "and sails. Starlight and a low moon on the ripples, the hills a dark line behind. "
     "This is the ONE shot where other, smaller boats are correct — the big lead boat is "
     "still the same locked boat."),

    ("s2b-four-at-the-oars", "the four professional fishermen at the oars",
     ["JESUS", "BOAT", "CREW", "PETER SHEET", "ANDREW SHEET", "JAMES SHEET", "JOHN SHEET"],
     "Close inside the same big boat on calm moonlit water, early in the crossing, before "
     "any storm. The four professional fishermen are at the oars and the rigging, their "
     "faces clearly shown in the moonlight and lantern glow, working the boat they have "
     "worked their whole lives, easy and unafraid on dark water. Peter pulls the near oar "
     "in his blue-grey tunic, thick dark curly hair and full beard, strong rope-worn hands "
     "on the loom. His brother Andrew pulls the oar behind him in faded olive-drab, leaner, "
     "short dark beard, the same curly hair kept shorter. Across from them James braces a "
     "line in dark ochre-brown, short dark beard, solid and heavy-built. Beside James young "
     "clean-shaven John in faded grey-blue coils a rope, dark wavy hair to the jaw, bright "
     "attentive eyes. The other disciples sit quietly further back in the hull and Jesus is "
     "seated aft among them in cream. Calm night water, a low moon, the far shore ahead."),

    ("s3-the-storm", "the storm broke on them",
     ["JESUS", "BOAT", "CREW", "PETER SHEET", "ANDREW SHEET", "JAMES SHEET", "JOHN SHEET"],
     "Night on the Sea of Galilee, a violent storm breaking on them — driving rain, spray, "
     "lightning splitting the black sky, tall dark waves, cold wind pouring down off the "
     "black hills that ring the lake. The one big boat pitches hard on the water, crowded "
     "with all twelve disciples fighting the storm. James hauls on the wet rigging in his "
     "dark ochre-brown tunic and young clean-shaven John clings to the mast in faded "
     "grey-blue, both faces clearly shown and streaming with rain. Peter in blue-grey "
     "shouts orders from the near gunwale, Andrew in olive-drab beside him. In the high "
     "stern, Jesus lies asleep on the steersman's cushion, his face shown clearly, calm and "
     "peaceful amid the chaos, cream wool robe damp with spray. Waves break over the "
     "gunwale."),

    ("s3b-boat-filling", "the waves broke over the side and the boat was filling",
     ["JESUS", "BOAT", "CREW", "PETER SHEET", "ANDREW SHEET", "JAMES SHEET", "JOHN SHEET"],
     "Down low inside the same big boat at the worst of the night storm, water sloshing "
     "shin-deep over the planks and pouring in over the gunwale as another black wave "
     "breaks across the side. Peter in his soaked blue-grey tunic and his brother Andrew in "
     "olive-drab bail hard with SOLID WOODEN BUCKETS, one of them tipping a full bucket out "
     "over the rail, arms and shoulders straining, both faces clearly shown and openly "
     "afraid. James in dark ochre-brown drags at a swamped rope behind them and young "
     "clean-shaven John in faded grey-blue braces against the rising water, staring at how "
     "fast it is coming in. Other disciples bail and cling further down the hull. These are "
     "men who have survived a hundred storms and they look like men who believe this one is "
     "their last. Rain, spray, a lantern's weak light, no oil lamp loose on the water. "
     "Jesus is NOT awake and NOT standing in this picture — he is still asleep on the "
     "cushion in the high stern behind them, low and partly hidden by the men and the "
     "gunwale, eyes closed, a quiet cream shape in the dark while they fight the water."),

    ("s4-asleep-in-stern", "and Jesus was asleep",
     ["JESUS", "BOAT", "CREW", "JAMES SHEET", "JOHN SHEET"],
     "Night storm on the Sea of Galilee, the same big boat pitching on tall waves, rain and "
     "spray. In the STERN, closer now, Jesus lies fast asleep on the steersman's cushion, "
     "his face shown clearly, peaceful and unafraid, dark wavy hair against the cushion, "
     "cream wool robe damp with spray. James in dark ochre-brown with his short dark beard "
     "and young clean-shaven John in faded grey-blue are nearest him, both turned and "
     "staring in disbelief at the sleeping man, faces clearly shown. Behind them the rest of "
     "the twelve crowd the big boat, soaked — two bailing with solid wooden buckets, the "
     "others gripping the rigging and the rails. Coiled rope and wet planks underfoot."),

    ("s5-carest-thou-not", "so they woke him",
     ["JESUS", "BOAT", "CREW", "PETER SHEET", "JOHN SHEET"],
     "The storm at its worst, at night, waves breaking over the side of the same big boat. "
     "Peter, soaked through in his blue-grey tunic, thick dark curly hair plastered down and "
     "full beard streaming, reaches out with both hands and grips Jesus firmly by the "
     "shoulder to shake him awake, shouting over the wind, terror plain on his clearly-shown "
     "face. Young clean-shaven John in faded grey-blue leans in right behind him, calling "
     "too. Jesus is waking, sitting up in the stern, his face shown clearly and calmly, "
     "brown eyes opening, dark wavy hair, unafraid, cream wool robe wet with spray. The rest "
     "of the twelve crowd the big boat around them, drenched, clinging to the rigging and "
     "the rails."),

    ("s6-peace-be-still", "he stood in the stern and rebuked the wind",
     ["JESUS", "BOAT", "CREW", "PETER SHEET", "JOHN SHEET"],
     "Deep in the night storm, the same big boat riding tall black waves under lightning. "
     "Jesus stands upright and steady in the stern of the boat, both feet planted on the "
     "deck, normal human height for a man standing in a boat, his face shown clearly in "
     "three-quarter view, calm and commanding, one hand lifted toward the towering waves as "
     "he speaks to the storm, dark wavy hair and cream wool robe stirred by the last of the "
     "wind, bare-headed. All twelve disciples crowd low in the hull of the same big boat "
     "around him, soaked, looking up at him in fear and wonder — Peter in blue-grey nearest "
     "his feet, young clean-shaven John in faded grey-blue beside Peter, both faces clearly "
     "shown and lit by the lightning."),

    ("s7-great-calm", "and there was a great calm",
     ["JESUS", "BOAT", "CREW", "PETER SHEET", "ANDREW SHEET", "JAMES SHEET", "JOHN SHEET"],
     "A perfectly calm, glassy moonlit sea at night, the storm utterly gone, stars and a "
     "thin crescent moon reflected on water like glass. The same one big boat rests on the "
     "calm. Jesus stands quietly and steady near the mast in the middle of the boat among "
     "his seated disciples, both feet on the deck, correctly sized against the men around "
     "him, his face shown clearly in gentle profile as he looks out over the still water, "
     "peaceful, cream wool robe soft in the moonlight. All twelve disciples sit low around "
     "him inside the same big boat, gazing out at the sudden stillness in awe — Peter in "
     "blue-grey, Andrew in olive-drab, James in dark ochre-brown and young clean-shaven "
     "John in faded grey-blue all clearly recognisable in the front of the group. Water "
     "still dripping off the ropes. Peaceful, hushed."),

    ("s8-turned-to-them", "why are ye so fearful",
     ["JESUS", "BOAT", "CREW", "PETER SHEET", "ANDREW SHEET", "JAMES SHEET", "JOHN SHEET"],
     "Inside the same big boat on the now-calm moonlit sea. Jesus sits in the stern and has "
     "turned to face his friends, seated at the same level as the men around him and the "
     "same human size as them, his face shown clearly and gently, warm brown eyes full of "
     "tenderness, one hand open in a calm gesture as he asks them quietly why they were so "
     "afraid, cream wool robe damp, expression kind and not scolding. The twelve sit crowded "
     "close around him, soaked and shaken, faces clearly shown — awe and fear and relief — "
     "looking back at him. Peter in blue-grey is closest, still gripping a rope; Andrew in "
     "olive-drab, James in dark ochre-brown and young clean-shaven John in faded grey-blue "
     "are gathered right beside him."),

    ("s9-what-manner-of-man", "what manner of man is this",
     ["JESUS", "BOAT", "CREW", "PETER SHEET", "ANDREW SHEET", "JAMES SHEET", "JOHN SHEET"],
     "The calm moonlit sea, the same one big boat on glassy water. The disciples have turned "
     "to one another in amazement, faces clearly shown, marvelling and half-afraid, asking "
     "each other what kind of man this is — Peter in blue-grey turned to his brother Andrew "
     "in olive-drab, James in dark ochre-brown speaking low to young clean-shaven John in "
     "faded grey-blue, the rest leaning in. Jesus sits quietly and calmly in the middle of "
     "them, his face shown clearly in the moonlight, cream wool robe soft, at peace while "
     "the twelve around him wonder, no bigger than any other man in the boat. Stars fill the "
     "still sky."),
]

LOCKS = {
    "JESUS": JESUS,
    "BOAT": BOAT,
    "CREW": CREW,
    "PETER SHEET": lock_text("peter"),
    "ANDREW SHEET": lock_text("andrew"),
    "JAMES SHEET": lock_text("james"),
    "JOHN SHEET": lock_text("john-beloved"),
}

HEADER = f"""# FLOW PROMPTS — Story Video #11: Calming the Storm (mark-4_calming-the-storm)

Mark 4:35-41. **CHARACTER-LAW REBUILD 2026-07-21 (Machine A).** Cameron rejected the
shipped cut: the captions were the old pre-CAPTION-LAW paragraph dumps, and the men in
the boat were imagined strangers who changed shot to shot. Both are fixed here. The four
professional fishermen at the oars are **Peter, Andrew, James and John** (Mark 1:16-20),
and every still that shows them conditions on their LOCKED sheets — same faces, same
hair, same tunic colours as every other video they appear in.

STORY-COVERAGE: two beats were carrying too much story on one picture. `n1` (the crossing
plus the whole crew introduction) and `n2` (the geography plus the swamping) are each
split, and each half gets its own still — `s2b-four-at-the-oars` and `s3b-boat-filling`.
Eleven stills, one per beat.

FACE LAW v3: Jesus's face IS shown, identical in every picture, text-locked (no --ref —
an attached bust echoes). Only Jesus wears cream. BOAT LOCK + CREW LOCK: one same large
single-mast boat, Jesus + his twelve = thirteen men every shot. Every prompt carries the
anti-glitch clause, and — after complaints #83/#112/#157 on other videos — an explicit
"nobody is a giant" scale clause. Night throughout except s1 (last gold of evening).

This file is GENERATED by `write_prompts.py`. Edit that script, not this file.

STILL STYLE BLOCK (prepended to every prompt, exactly):
{STYLE}

Every prompt is prefixed with: "{PANEL}"

[<NAME> SHEET] = the locked `CHARACTERS/<name>/` spec, substituted by
`gen_stills_flow.py` together with that character's reference jpegs as --ref.
The verbatim lock paragraphs (also here so `character_ref_gate.py` can see them):

"""


def main():
    out = [HEADER]
    for key in ("PETER SHEET", "ANDREW SHEET", "JAMES SHEET", "JOHN SHEET"):
        out.append(f"[{key}] = {LOCKS[key]}\n")
    out.append(f"[JESUS LOCK] = {JESUS}\n")
    out.append(f"[BOAT LOCK] = {BOAT}\n")
    out.append(f"[CREW LOCK] = {CREW}\n")
    out.append("---\n")
    for slug, head, locks, scene in SHOTS:
        out.append(f"\n## {slug} — Shot: {head}")
        for lk in locks:
            out.append(LOCKS[lk])
        out.append(f"{PANEL} [STILL STYLE BLOCK] {scene} {QUALITY}\n")
    out.append("""
### Closing card
Text on cream (#F7F2E9), spoken + captioned in assembly (an INVITATION, not a
fear-question): "The same Jesus is in your boat. Bring him your storm — and let him
speak his peace."
""")
    (HERE / "PROMPTS.md").write_text("\n".join(out), encoding="utf-8")
    print(f"wrote PROMPTS.md — {len(SHOTS)} shots")


if __name__ == "__main__":
    main()
