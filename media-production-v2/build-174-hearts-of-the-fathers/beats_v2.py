#!/usr/bin/env python3
"""V2 beat map — row 174, build-174-hearts-of-the-fathers (Malachi 4:5-6, "Behold,
I will send you Elijah the prophet... and he shall turn the heart of the fathers
to the children, and the heart of the children to their fathers").

COVERAGE: 12 pictures over 57.23 s (card_start) = ~4.75 s/picture (lesson 12
movie-coverage). ONE establishing wide per place (b01 the wilderness road, b07 the
family home); every other beat is a single, a close or a two-shot.

NO OPEN CAMERON COMPLAINT — `v2_outline.py 174` shows none. Fresh V2 picture map
on the already-authored SPEAKER-LAW narration (audio OK).

SPEAKER LAW: Malachi — s1a and s1b are the GOD voice → GREEN captions (God himself
speaking the promise). HARD GATE (same as rows 165/166/168/169's God/Holy-Ghost
gate): **GOD IS NEVER EMBODIED** — no figure, no face, no hand, no beam, rays or
shaft from heaven, no divine being anywhere in any frame; his words land on the
prophet, the land and the people, shown as ordinary natural light. On the two GOD
beats that picture Elijah (b02/b03) he is STANDING/RECEIVING with his mouth CLOSED
— he is the one God is *sending*, not the one speaking, so it never reads as Elijah
mouthing God's words. The narrator beats are WHITE. NO Jesus and NO cream anywhere
in this row (Elijah/John/the family are OT and NT figures, none of them Jesus).

CONTENT-CARE: "lest I come and smite the earth with a curse" (end of s1b, in b08's
caption) is NOT pictured as smiting, disaster, fire or a cursed earth — b08 shows
the reconciliation the promise is FOR (a grown child turning to the aged father).
Elijah's errand is "to mend, not to thunder": he is peaceable and empty-handed,
a staff not a weapon, never calling down fire here.

PLACES:
  WILDERNESS-ROAD (NEW build-local)  Elijah sent ahead + John preparing the way,
                                     under the wide open sky of the promise
                                     (b01-b06, b10)
  FAMILY-HOME (NEW build-local)      the hearts turning — three generations of one
                                     family made whole (b07-b09, b11, b12)
NEW places (runner promotes each from its first good frame, lesson 11):
  WILDERNESS-ROAD  promote b01
  FAMILY-HOME      promote b07 (its establishing wide)
Steps in QC.md.
"""

# LOCKS: all build-local. ELIJAH and JOHN-BAPTIST are distinct tokens; NOTE the
# global "JOHN" token is John the APOSTLE (one of the Twelve) and must NOT be used
# for the Baptist — hence "JOHN-BAPTIST". No cream on anyone (only Jesus wears
# cream, and Jesus is not in this row).
LOCKS = {
    "WILDERNESS-ROAD": (
        "WILDERNESS-ROAD LOCK: the same place in every frame — a dry "
        "first-century road winding through open wilderness country, pale stony "
        "ground and low scrub, bare brown hills rolling back to a far horizon "
        "under a wide, high, open sky. The same road, hills and sky throughout — "
        "never modern surfacing, wire, pole, sign, fixture or vehicle, and no "
        "rendered writing of any kind."
    ),
    "FAMILY-HOME": (
        "FAMILY-HOME LOCK: the same place in every frame — the plain courtyard of "
        "a modest first-century household, walls of rough mud-brick and dressed "
        "stone, a beaten-earth floor, a low doorway and a few simple clay vessels, "
        "warm domestic daylight falling in. The same courtyard, walls and doorway "
        "throughout — never modern masonry, glass, metal, fixture or sign, and no "
        "rendered writing of any kind."
    ),
    "ELIJAH": (
        "ELIJAH LOCK: the prophet Elijah is the same man in every shot — an aged "
        "Hebrew prophet, tall and gaunt, weathered sun-darkened face, long "
        "iron-grey hair and a full grey beard, in a rough dark mantle of coarse "
        "haircloth worn over a plain earth-toned tunic and bound with a wide "
        "leather girdle (never cream, never white), a plain wooden staff in his "
        "hand and travel-worn sandals; grave, peaceable and unarmed. The SAME man "
        "throughout, never twinned, never a cloned face."
    ),
    "JOHN-BAPTIST": (
        "JOHN-BAPTIST LOCK: John the Baptist is a lean, weathered young man of "
        "about thirty, straight dark near-black hair to the shoulder and a short "
        "dark beard, in a rough garment of coarse camel-hair worn over one "
        "shoulder and bound at the waist with a wide leather girdle (never cream), "
        "sun-browned and wilderness-lean. He is a DIFFERENT man from the aged "
        "grey prophet Elijah. The SAME man in every frame he appears."
    ),
    "FAMILY-THREE": (
        "FAMILY-THREE LOCK: three generations of one ordinary first-century "
        "family, the same faces in every family frame. THE ELDER: an aged "
        "grandfather, white-bearded, lined and gentle, in sober deep-toned wool. "
        "THE FATHER: a grown man of about thirty-five, dark hair and a short dark "
        "beard, a plain earth-toned tunic. THE CHILD: a young child of about six, "
        "dark-haired, in a simple earth-toned smock. None of them in cream. Each "
        "is a distinct, ordinary-sized person, never twinned, never a cloned face."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r174-b01", "out": "s01-a-messenger-sent-ahead.jpeg", "seg": "n0",
        "window": "0.400-6.583", "wide": True, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-ROAD", "ELIJAH"],
        "narration": "Before the great day, a messenger would come first — Elijah, the prophet, sent ahead.",
        "must_show": "the ONE establishing wide of the road — the camera looks down the wilderness road from behind and to the side of Elijah as he walks it alone, sent ahead under a wide open sky; a messenger going before.",
        "must_not_show": "no God figure, face, hand or beam anywhere; no Jesus and no cream; no halo, glare or rim-light; no weapon or army; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "The camera stands to the side and a little behind Elijah and looks "
            "down a dry wilderness road: the aged grey prophet in his rough "
            "haircloth mantle and leather girdle walks it alone, staff in hand, "
            "bare hills rolling back under a wide high sky — a messenger sent on "
            "ahead of a great day. Pale stony ground and low scrub lie around him. "
            "An ordinary-sized man with two hands and one head, not in cream, his "
            "face set down the road and not to the camera; nothing is written "
            "anywhere and no light rings his head."
        ),
    },
    {
        "id": "v2-r174-b02", "out": "s02-i-will-send-elijah.jpeg", "seg": "s1a",
        "window": "6.583-11.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-ROAD", "ELIJAH"],
        "narration": "Behold, I will send you Elijah the prophet before the coming of the great and dreadful day of the LORD:",
        "must_show": "GOD-VOICE (green caption) — Elijah standing still on the road under the wide open sky, receiving his errand, his mouth closed; the prophet God is sending, shown while God himself speaks (God unseen).",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand, beam, rays or shaft from heaven, no divine being; Elijah is NOT mid-speech (mouth closed) so it never reads as him speaking; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Elijah stands still on the wilderness road beneath a wide, high, open "
            "sky, his staff planted and his weathered face lifted and quiet, "
            "receiving an errand rather than speaking it — his lips closed. Bare "
            "brown hills and pale stony ground run back around him; the sky above "
            "is only clear natural daylight, no shape and no figure in it. An "
            "ordinary-sized man with two hands and one head, not in cream, his "
            "gaze lifted past the camera and not to it; nothing is written "
            "anywhere and no light rings his head."
        ),
    },
    {
        "id": "v2-r174-b03", "out": "s03-the-prophet-receives.jpeg", "seg": "s1a",
        "window": "11.500-15.573", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-ROAD", "ELIJAH"],
        "narration": "before the coming of the great and dreadful day of the LORD:",
        "must_show": "GOD-VOICE (green) — a close on Elijah's weathered face, grave and steady as he takes in the weight of the day that is coming; mouth closed, receiving.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam; no disaster, fire or cursed-earth imagery; Elijah's mouth closed; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "A close on Elijah's weathered, sun-darkened face beneath the open "
            "sky, iron-grey hair and full beard, his eyes grave and steady as he "
            "takes in the weight of the great day that is coming — quiet, "
            "resolute, his lips closed. The bare hills sit soft behind him, the "
            "sky only clean daylight. An ordinary-sized man with two hands and "
            "one head, not in cream, his gaze off past the camera and not to it; "
            "nothing is written anywhere and no light rings his head."
        ),
    },
    {
        "id": "v2-r174-b04", "out": "s04-god-himself-promising.jpeg", "seg": "n0b",
        "window": "15.573-20.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-ROAD"],
        "narration": "Listen to who is talking there. That is God himself, making a promise out loud:",
        "must_show": "the promise over the land — a quiet wide of the empty wilderness road and hills under the great open sky, the whole earth held under a spoken promise; God himself unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand, beam, rays or shaft from heaven, no shape or being in the sky; no Jesus and no cream; no halo or glare; no scroll, writing or panel; no modern object.",
        "scene": (
            "A quiet, still view of the empty wilderness road winding away between "
            "bare brown hills under a great, high, open sky — the whole land held "
            "in the hush of a promise being spoken over it. The sky is only clear "
            "natural daylight, wide and bright, with no shape, figure or beam in "
            "it. Nothing is written anywhere and no light rings anything — only "
            "the open road, the hills and the sky."
        ),
    },
    {
        "id": "v2-r174-b05", "out": "s05-sending-elijah-back.jpeg", "seg": "n0b",
        "window": "20.000-24.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-ROAD", "ELIJAH"],
        "narration": "before the last great day arrives, I am sending Elijah back.",
        "must_show": "Elijah coming — the prophet walking forward along the road toward the camera's side, returning to his people; sent back before the last great day.",
        "must_not_show": "no God figure, face, hand or beam; no Jesus and no cream; no halo, glare or rim-light; no weapon or army; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Elijah walks forward along the wilderness road, his rough mantle "
            "moving, staff in hand, his weathered face set and purposeful as he "
            "comes back toward his people. Bare hills and pale ground run back "
            "under the open sky. An ordinary-sized man with two hands and one "
            "head, not in cream, his gaze down the road and not to the camera; "
            "nothing is written anywhere and no light rings his head."
        ),
    },
    {
        "id": "v2-r174-b06", "out": "s06-not-an-army.jpeg", "seg": "n0b",
        "window": "24.500-28.900", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-ROAD", "ELIJAH"],
        "narration": "Not an army. Not a warning shot.",
        "must_show": "the peaceable messenger — a close on Elijah, open empty hands and only a plain wooden staff, no weapon, his face gentle; not an army, not a threat.",
        "must_not_show": "NO army, soldier, sword, spear, weapon, fire from heaven or destruction of any kind; no God figure or beam; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "A close on Elijah on the road, his hands open and empty but for the "
            "plain wooden staff, his weathered face gentle and unhurried — a "
            "messenger who carries no weapon and threatens no one. Bare hills and "
            "open sky sit soft behind. An ordinary-sized man with two hands and "
            "one head, not in cream, his gaze mild and off past the camera and not "
            "to it; nothing is written anywhere and no light rings his head."
        ),
    },
    {
        "id": "v2-r174-b07", "out": "s07-hearts-of-the-fathers.jpeg", "seg": "s1b",
        "window": "28.900-34.500", "wide": True, "jesus": False, "ref": False,
        "locks": ["FAMILY-HOME", "FAMILY-THREE"],
        "narration": "And he shall turn the heart of the fathers to the children,",
        "must_show": "GOD-VOICE (green) — the ONE establishing wide of the family home: the camera in the courtyard looks past the aged grandfather toward the father kneeling to turn to his young child, three generations under one roof; a father's heart turning to his children.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no posed line to the lens.",
        "scene": (
            "In the plain courtyard of a modest household the camera stands "
            "behind and past the shoulder of the aged white-bearded grandfather "
            "and looks "
            "toward the father — a grown man of about thirty-five — who has knelt "
            "down to turn toward his young child with an open, tender face, warm "
            "domestic daylight falling across the beaten-earth floor. Three "
            "generations stand in one room, a father's heart turning to his "
            "children. Ordinary-sized, distinct people with two hands and one head "
            "each, none in cream and none turned to the camera; nothing is written "
            "anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r174-b08", "out": "s08-children-to-their-fathers.jpeg", "seg": "s1b",
        "window": "34.500-39.973", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY-HOME", "FAMILY-THREE"],
        "narration": "and the heart of the children to their fathers, lest I come and smite the earth with a curse.",
        "must_show": "GOD-VOICE (green) — close on the reconciliation the promise is FOR: the grown father turning to embrace the aged grandfather, the child's hand reaching too; the children's hearts turning back to their fathers.",
        "must_not_show": "the caption names a curse, but PICTURE NO smiting, disaster, fire, ruin or cursed earth — only the reconciliation; GOD IS NEVER SHOWN (no figure, face, hand or beam); no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Close in the warm courtyard light: the grown father turns to fold the "
            "aged white-bearded grandfather into a quiet embrace, the young child "
            "reaching a small hand to join them — three generations drawn back "
            "together, the children's hearts turned to their fathers. The plain "
            "mud-brick wall and low doorway sit soft behind. Ordinary-sized, "
            "distinct people with two hands and one head each, none in cream, "
            "their eyes on one another and not the camera; nothing is written "
            "anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r174-b09", "out": "s09-not-to-thunder-but-to-mend.jpeg", "seg": "n1",
        "window": "39.973-44.303", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY-HOME", "ELIJAH", "FAMILY-THREE"],
        "narration": "His work was not to thunder, but to mend.",
        "must_show": "Elijah the mender — Elijah in the family courtyard gently bringing the father's and grandfather's hands together, his own face calm; his work is to mend, not to thunder.",
        "must_not_show": "NO thunder, lightning, storm, fire from heaven or destruction; no God figure or beam; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "In the household courtyard Elijah, the aged grey prophet in his rough "
            "mantle, stands with the family and gently guides the grown father's "
            "hand toward the old grandfather's, his weathered face calm and kind — "
            "the work of mending done quietly, not with thunder. The young child "
            "watches close by; warm daylight falls across the earth floor. "
            "Ordinary-sized, distinct people with two hands and one head each, "
            "none in cream, their eyes on the joined hands and not the camera; "
            "nothing is written anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r174-b10", "out": "s10-the-same-spirit-on-john.jpeg", "seg": "n3",
        "window": "44.303-49.172", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-ROAD", "JOHN-BAPTIST"],
        "narration": "The same spirit would later rest on John, preparing the way.",
        "must_show": "John the Baptist in the wilderness — the lean young Baptist in his rough camel-hair garment standing on the same road, an open hand pointing down it, preparing the way; the same errand, a later man.",
        "must_not_show": "John is the lean DARK-haired young Baptist, NOT the aged grey Elijah; no God figure, dove or beam; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "On the same wilderness road John the Baptist — a lean, sun-browned "
            "young man in a rough camel-hair garment and leather girdle, dark hair "
            "to the shoulder — stands and points an open hand away down the road, "
            "his face earnest, preparing the way for one who comes after. Bare "
            "hills and open sky run back around him. An ordinary-sized man with "
            "two hands and one head, not in cream, his gaze down the road and not "
            "to the camera; nothing is written anywhere and no light rings his "
            "head."
        ),
    },
    {
        "id": "v2-r174-b11", "out": "s11-families-would-be-ready.jpeg", "seg": "n2a",
        "window": "49.172-53.954", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY-HOME", "FAMILY-THREE"],
        "narration": "So that when the Lord came, families would be ready.",
        "must_show": "the family ready — the three generations standing together at the low doorway of the home, looking out down the road in quiet expectation; ready for the Lord's coming.",
        "must_not_show": "no God figure or beam; no Jesus figure in this frame and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no posed line to the lens.",
        "scene": (
            "At the low doorway of the household the three generations stand "
            "together — the aged grandfather, the grown father, the young child — "
            "looking out down the road in quiet, hopeful expectation, the warm "
            "day beyond the threshold. The plain courtyard sits soft behind them. "
            "Ordinary-sized, distinct people with two hands and one head each, none "
            "in cream, their eyes out down the road and not to the camera; nothing "
            "is written anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r174-b12", "out": "s12-not-divided-but-whole.jpeg", "seg": "n2b",
        "window": "53.954-57.228", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY-HOME", "FAMILY-THREE"],
        "narration": "Not divided, but whole.",
        "must_show": "the family made whole — a close on the three generations drawn close together, the child held between father and grandfather, all at peace; not divided, but whole.",
        "must_not_show": "no God figure or beam; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "A warm close on the three generations of the family drawn close in "
            "the courtyard light — the young child held between the grown father "
            "and the aged grandfather, all three faces easy and at peace, one "
            "family whole and undivided. The plain wall sits soft behind. "
            "Ordinary-sized, distinct people with two hands and one head each, none "
            "in cream, their eyes on one another and not the camera; nothing is "
            "written anywhere and no light rings any head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: every person is carried by a byte-identical text lock (no face
# sheets exist for these figures). NO Jesus in this row.
REFS = {
}
