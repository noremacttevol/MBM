#!/usr/bin/env python3
"""V2 beat map — row 186, build-186-joint-heirs (Romans 8:16-17 — "The Spirit itself
beareth witness with our spirit, that we are the children of God: And if children, then
heirs; heirs of God, and joint-heirs with Christ; if so be that we suffer with him, that
we may be also glorified together.").

COVERAGE: 12 pictures over 52.276 s (card_start) = ~4.4 s/picture (lesson 12
movie-coverage). A single representative BELIEVER (the "you" of the letter) is the human
spine so the abstract doctrine reads as a real person's story: Paul writing to Rome →
the Spirit witnessing to the believer that he is a child of God → the believer welcomed
into the family home as a child → shown he is an HEIR at the doorway of the inheritance →
standing as a JOINT-HEIR beside Christ → walking a hard road WITH Christ toward a shared
dawn → the family inheritance belonging to him → the honest terms of the road → received
by belonging, not earned → heirs together with the Son at the dawn. Three places so
every beat fits its moment: PAUL-ROOM (b01, reused byte-identical from build-184),
INHERITANCE-HOME (the family household where a child belongs, b02-b06, b08, b09, b11), and
DAWN-ROAD (the country road that climbs through hardship into a radiant dawn, b07, b10,
b12). One establishing wide per place (b01 room, b02 home, b10 road).

=====================================================================
OPEN CAMERON COMPLAINT (v2_outline.py 186): NONE. COMPLAINT LEDGER in QC.md is empty.
=====================================================================

SPEAKER LAW (see make_narration.py — a PAUL EPISTLE, so NO red-letter and NO God-voice):
  s1  Rom 8:16   "The Spirit itself beareth witness..."   SCRIPTURE → light-blue
  s2  Rom 8:17   "And if children, then heirs..."          SCRIPTURE → light-blue
Every other segment (n0, n0b, n1, n2, n3a, n3b, card) is the NARRATOR → white.
There is NO Jesus-red-letter and NO God-voice anywhere in this row. Jesus (the Son) is
PICTURED (jesus=True + ref=True + LOCK) on the three Christ beats — b06 "joint-heirs with
Christ", b07 "suffer with him... glorified together", and b12 "heirs together with the
Son" — but those captions stay SCRIPTURE-blue (b06/b07) and narrator-white (b12): the
jesus flag drives the PICTURE, the segment speaker drives the CAPTION (build-170 lesson).
Only Jesus wears cream.

**HARD GATE — GOD / THE FATHER IS NEVER EMBODIED (default gate — no Cameron instruction
to depict the Father in this row).** "children of God" (s1), "heirs of God" (s2) and
"what the Father has belongs to the family" (n1) are carried by the warm light and the
family HOME itself and by the believer being welcomed — NEVER by any figure, face, hand,
throne, beam or rays standing in for God or the Father. No dove, triangle, all-seeing
eye or Trinitarian symbol anywhere. The only embodied divine person is the risen Son,
Jesus, on b06/b07/b12. No halo, ring or rim-light around anyone (drift-word gate — word
light as warm/radiant/golden, never a ring around a head).

CONTENT-CARE: "suffer with him" is shown as quiet SOLIDARITY on a hard uphill road — a
steep grey climb walked shoulder to shoulder with Christ, dignity and resolve — NEVER
wounds, blood, gore, a cross, or any literal torment. "Glory" / "glorified together" is
the warm radiant DAWN at the crest of the road, never a halo. Reverent hope throughout.

TIME-OF-DAY: PAUL-ROOM and INHERITANCE-HOME are in warm plain daylight throughout. The
DAWN-ROAD lower stretch is cool grey pre-dawn shadow; the crest and sky burn warm gold
with the rising sun — the two registers are DELIBERATE (the road climbs from hardship
into shared glory), not a lighting drift.

PLACES / LOCKS:
  PAUL             person, byte-identical to builds 138/155/166/171/184 (cross-video
                   same man).
  PAUL-ROOM        place, byte-identical to build-184 (cross-video same room). b01.
  BELIEVER         person, build-local — the representative believer/heir ("you"), the
                   same man in every frame he appears (face + beard board).
  INHERITANCE-HOME (NEW place) the warm first-century family household where a child
                   belongs — b02, b03, b04, b05, b06, b08, b09, b11.
  DAWN-ROAD        (NEW place) the steep country road climbing through grey hardship
                   into a radiant dawn — b07, b10, b12.
NEW-place promote plan (runner): promote INHERITANCE-HOME from b02 (a NON-Jesus frame),
and DAWN-ROAD from b10 (a NON-Jesus frame) — NEVER promote a Jesus-bearing frame
(lesson 11). PAUL-ROOM's plate may be reused from build-184 once that row is built, or
promoted fresh from b01. Steps in QC.md.

AUDIO: default AUDIO LOCK stream-copy (no flag). Board Audio = OK. Picture-only build —
do NOT re-voice. card_start = 52.276 s; total with card = 58.679 s.
"""

# LOCKS: PAUL + PAUL-ROOM are byte-identical cross-video reuses; BELIEVER,
# INHERITANCE-HOME and DAWN-ROAD are build-local. Setting locks never name a
# character (STRAY-JESUS defect). Only Jesus wears cream; Jesus is injected by the
# assembler on jesus=True beats.
LOCKS = {
    "PAUL": (
        "PAUL LOCK: Paul is the same man in every shot — compact and wiry, about "
        "fifty, balding with a fringe of dark hair, a full pointed dark beard, keen "
        "deep-set eyes, in a plain DARK RUST-BROWN travel robe (never cream, never "
        "white); a tentmaker's strong hands; earnest fire without anger."
    ),
    "PAUL-ROOM": (
        "PAUL-ROOM LOCK: the same place in every frame — a humble first-century room "
        "where Paul writes his letters: plain lime-plastered stone walls, a low wooden "
        "writing table with a sheet of parchment, a reed pen and a small clay oil lamp, "
        "a simple stool and a floor mat, and one plain rectangular window opening to "
        "soft daylight. Ancient, spare, real; no modern object anywhere; any parchment "
        "is blank with no legible or rendered writing. The same room and warm plain "
        "daylight throughout."
    ),
    "BELIEVER": (
        "BELIEVER LOCK: the same man in every frame he appears — a first-century "
        "believer of about thirty, warm olive-brown skin, short dark hair, a neat short "
        "dark beard, keen dark eyes, in a plain undyed brown-grey wool tunic and mantle "
        "(never cream, never white); an ordinary working man, humble and awake with "
        "quiet wonder. The same face, beard, build and clothing throughout — he is the "
        "'you' the letter speaks to."
    ),
    "INHERITANCE-HOME": (
        "INHERITANCE-HOME LOCK: the same place in every frame — a warm, generous "
        "first-century family household where a child plainly belongs: a broad open "
        "courtyard paved in honey-coloured dressed stone, a wide timber doorway opening "
        "into the shaded interior of the home, plain lime-plastered walls, an old olive "
        "tree, a low stone well, and worn stone steps, all in warm plain daylight. It "
        "reads as a family's settled ancestral home — spacious, welcoming, lived-in, "
        "not a palace and not a temple. Ancient and real; no modern object anywhere; "
        "nothing legible or rendered is written on any surface. The same household and "
        "warm daylight throughout."
    ),
    "DAWN-ROAD": (
        "DAWN-ROAD LOCK: the same place in every frame — a steep stony road of the open "
        "country climbing toward a high crest, bare hills and scattered rocks to either "
        "side, the crest ahead opening onto a wide radiant dawn sky over distant land. "
        "The lower road lies in cool grey pre-dawn shadow; the crest and the sky above "
        "it burn warm gold with the rising sun. Ancient and real; no building, no modern "
        "object, and nothing written anywhere. The same country road and climbing dawn "
        "throughout."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r186-b01", "out": "s01-paul-wrote-to-rome.jpeg", "seg": "n0",
        "window": "0.000-6.601", "wide": True, "jesus": False, "ref": False,
        "locks": ["PAUL-ROOM", "PAUL"],
        "narration": "Paul wrote to the believers in Rome about who they really were — not strangers, not outsiders.",
        "must_show": "the ONE establishing wide of Paul's room — Paul at his low writing table, reed pen to the parchment, his face earnest and warm as he writes to the believers in Rome about who they really are: not strangers, not outsiders.",
        "must_not_show": "no God or Father figure; no Jesus, no cream; no halo, glare or rim-light; no legible or rendered writing on the parchment; no modern object; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "A wide of the humble writing room seen from behind and to the side of Paul, "
            "his back three-quarters to the camera as he sits at the low table, reed pen "
            "moving over a blank parchment, his lined face earnest and warm in the soft "
            "window light as he writes to the believers in Rome. Camera set behind and "
            "beside him looking past him to the table and the window; ordinary-sized, "
            "one head; nothing legible is written on the parchment."
        ),
    },
    {
        "id": "v2-r186-b02", "out": "s02-spirit-beareth-witness.jpeg", "seg": "s1",
        "window": "6.601-12.735", "wide": True, "jesus": False, "ref": False,
        "locks": ["INHERITANCE-HOME", "BELIEVER"],
        "narration": "The Spirit itself beareth witness with our spirit, that we are the children of God:",
        "must_show": "SCRIPTURE, light-blue caption — the ONE establishing wide of the family home: the believer standing in the warm courtyard as gentle warm light from above settles over him, an inner witness assuring him he is a child of God; his face lifting in quiet recognition.",
        "must_not_show": "no God or Father figure, throne, hand or beam standing in for God; the witnessing is warm light only; no Jesus, no cream; no dove or Trinitarian symbol; no halo, ring or rim-light; no modern object; nothing written; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "An establishing wide of the warm family courtyard seen from behind and to "
            "the side of the believer, his back three-quarters to the camera as he stands "
            "in the open honey-stone yard before the wide timber doorway, his face lifting "
            "toward a gentle warm daylight that settles over him from above like an inner "
            "witness — the quiet assurance that he is a child of this house. Camera behind "
            "and beside him looking past him to the doorway and the home; ordinary-sized, "
            "one head; the light rests on him, not around his head; nothing is written "
            "anywhere and no figure stands in for God."
        ),
    },
    {
        "id": "v2-r186-b03", "out": "s03-spirit-tells-your-spirit.jpeg", "seg": "n0b",
        "window": "12.735-15.825", "wide": False, "jesus": False, "ref": False,
        "locks": ["INHERITANCE-HOME", "BELIEVER"],
        "narration": "God's own Spirit tells your spirit the truth about you.",
        "must_show": "a close on the believer receiving the inner truth about himself — his hand coming to rest over his own heart, his eyes softening as the warm assurance reaches deep within him.",
        "must_not_show": "no God or Father figure; the Spirit is warm light only, no dove or symbol; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on the believer in the warm courtyard, one hand coming to rest over "
            "his own heart, his eyes softening and his breath caught as the inner truth "
            "about himself reaches deep within him. Warm daylight on his face. "
            "Ordinary-sized, one head, gaze inward and not to the camera; nothing is "
            "written anywhere and no light rings his head."
        ),
    },
    {
        "id": "v2-r186-b04", "out": "s04-you-are-a-child.jpeg", "seg": "n0b",
        "window": "15.825-22.985", "wide": False, "jesus": False, "ref": False,
        "locks": ["INHERITANCE-HOME", "BELIEVER"],
        "narration": "Not a rumour, not a hope — a witness, given straight to you: you are a child of God.",
        "must_show": "the believer welcomed into the family home as a child — an older woman and a couple of the household reaching to draw him in warmly through the wide doorway, hands on his shoulders, receiving him as one of their own; his face moved and belonging.",
        "must_not_show": "no God or Father figure among the household; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon; the household are ordinary distinct people, not twins.",
        "scene": (
            "A warm two- or three-shot at the wide doorway of the home: members of the "
            "household — an older woman and another of the family, distinct ordinary "
            "faces — reach to draw the believer in through the doorway with hands on his "
            "shoulders, receiving him plainly as one of their own. His face is moved and "
            "belonging as he is welcomed inside. Warm daylight from the courtyard behind "
            "them. Ordinary-sized people sharing one floor, one head each; no one stands "
            "in for God; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r186-b05", "out": "s05-then-heirs.jpeg", "seg": "s2",
        "window": "22.985-26.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["INHERITANCE-HOME", "BELIEVER"],
        "narration": "And if children, then heirs; heirs of God,",
        "must_show": "SCRIPTURE, light-blue caption — the believer shown he is an HEIR: standing at the threshold of the home's inner rooms, an elder of the household opening a hand to show him the family's inheritance laid out beyond — the estate is his to inherit because he is a child.",
        "must_not_show": "no God or Father figure (the inheritance is the HOME, shown by the household, never by a divine figure); no Jesus, no cream; no halo, ring or rim-light; no modern object; no legible or rendered writing on any deed or wall; not a cartoon.",
        "scene": (
            "A two-shot at the inner threshold of the home: a grey-bearded elder of the "
            "household stands beside the believer and opens a hand to show him the warm "
            "lived-in rooms and stores of the family beyond the doorway — the inheritance "
            "that is his because he is a child of the house. The believer looks in with "
            "quiet astonishment. Warm daylight through the openings. Ordinary-sized men "
            "on one floor, one head each; no figure stands in for God; nothing legible "
            "is written on any surface."
        ),
    },
    {
        "id": "v2-r186-b06", "out": "s06-joint-heirs-with-christ.jpeg", "seg": "s2",
        "window": "26.500-29.700", "wide": False, "jesus": True, "ref": True,
        "locks": ["INHERITANCE-HOME", "BELIEVER"],
        "narration": "and joint-heirs with Christ;",
        "must_show": "SCRIPTURE, light-blue caption — the risen Lord Jesus standing WITH the believer in the family home as a JOINT-HEIR beside him: Jesus in his cream robe, warm and kind, one hand on the believer's shoulder as an equal brother sharing the same inheritance; the believer humbled and glad at his side.",
        "must_not_show": "no God the Father; no halo, ring, rim-light or glow around Jesus; no one but Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A warm two-shot inside the family home: the risen Lord Jesus stands beside "
            "the believer as a brother and fellow heir, his hand resting on the "
            "believer's shoulder, turned toward him with steady kindness — only Jesus "
            "wears the plain cream robe. The believer stands humbled and glad at his "
            "side, the two of them sharing the same inheritance of the house. Warm "
            "daylight fills the room. Ordinary-sized men on one floor, two heads; the "
            "warm light rests on them, not around their heads; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r186-b07", "out": "s07-suffer-and-glorified.jpeg", "seg": "s2",
        "window": "29.700-33.688", "wide": False, "jesus": True, "ref": True,
        "locks": ["DAWN-ROAD", "BELIEVER"],
        "narration": "if so be that we suffer with him, that we may be also glorified together.",
        "must_show": "SCRIPTURE, light-blue caption — Jesus and the believer walking a hard steep road together, shoulder to shoulder up the grey climb, the crest ahead brightening toward a radiant dawn: they suffer the road together now, to be glorified together at the top.",
        "must_not_show": "no wounds, blood, gore, cross or literal torment (suffering is the hard uphill road, shown as quiet solidarity); no God the Father; no halo, ring, rim-light or glow around Jesus; no one but Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "Jesus and the believer climb a steep stony road together, shoulder to "
            "shoulder, backs three-quarters to the camera as they labour up the cool grey "
            "lower stretch toward a crest that opens onto a warm radiant dawn — only "
            "Jesus wears the plain cream robe. Their heads are bowed to the hard climb "
            "but set toward the brightening crest, sharing the road now to share the "
            "glory above. Camera set below and behind them looking up the road past their "
            "backs; ordinary-sized men on one ground, two heads; the dawn light is in the "
            "sky ahead, not ringing their heads; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r186-b08", "out": "s08-children-first-inheritors.jpeg", "seg": "n1",
        "window": "33.688-37.033", "wide": False, "jesus": False, "ref": False,
        "locks": ["INHERITANCE-HOME", "BELIEVER"],
        "narration": "Children first — and because children, inheritors.",
        "must_show": "the believer back in the family home settled plainly as a child of the house first — seated at ease at the family's low table with the household around him — and therefore an inheritor of all it holds.",
        "must_not_show": "no God or Father figure; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon; the household are distinct ordinary people.",
        "scene": (
            "The believer sits at ease at the family's low table in the warm home, at "
            "home as a child of the house first of all, the ordinary distinct members of "
            "the household near him — his place among them is settled, and because he "
            "belongs he inherits. Warm daylight through the openings. Ordinary-sized "
            "people on one floor, one head each; no figure stands in for God; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r186-b09", "out": "s09-belongs-to-the-family.jpeg", "seg": "n1",
        "window": "37.033-41.533", "wide": False, "jesus": False, "ref": False,
        "locks": ["INHERITANCE-HOME", "BELIEVER"],
        "narration": "What the Father has belongs to the family, and the family includes you.",
        "must_show": "the warm household gathered together in the home, the believer plainly one of them — everything of the family's estate around them belongs to the whole family, and he is included in it; a hand of the family resting on him.",
        "must_not_show": "the Father is NEVER shown — no God figure, throne, hand or beam; the Father's having is shown by the HOME and the family; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A warm grouped shot of the household together in the family home, the "
            "believer plainly one of them with a family member's hand resting on his "
            "shoulder, the lived-in stores and rooms of the estate around them all — what "
            "belongs to the house belongs to the whole family, and he is included. Warm "
            "daylight fills the room. Distinct ordinary faces, ordinary-sized on one "
            "floor, one head each; no figure stands in for the Father; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r186-b10", "out": "s10-the-honest-terms.jpeg", "seg": "n2",
        "window": "41.533-46.587", "wide": True, "jesus": False, "ref": False,
        "locks": ["DAWN-ROAD", "BELIEVER"],
        "narration": "The terms were honest: share in his suffering, and you will share in his glory too.",
        "must_show": "the ONE establishing wide of the DAWN-ROAD — the believer alone at the foot of the steep grey road, looking up its hard climb toward the radiant dawn at the crest: the honest terms laid plainly before him, the cost of the road and the glory beyond it both in view.",
        "must_not_show": "no wounds or gore; no God or Father figure; no Jesus, no cream (he is not in this frame); no halo, ring or rim-light; no modern object; nothing written; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "An establishing wide of the steep country road seen from behind and below "
            "the believer, his back three-quarters to the camera as he stands alone at "
            "the foot of the cool grey climb and looks up its hard length toward the warm "
            "radiant dawn breaking over the crest — the honest terms plain before him, "
            "the cost of the road and the shared glory beyond it both in his view. Camera "
            "set below and behind him looking up the road past his back; ordinary-sized, "
            "one head; the dawn light is in the sky at the crest, not around his head; "
            "nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r186-b11", "out": "s11-received-by-belonging.jpeg", "seg": "n3a",
        "window": "46.587-49.893", "wide": False, "jesus": False, "ref": False,
        "locks": ["INHERITANCE-HOME", "BELIEVER"],
        "narration": "Not earned by effort. Received by belonging.",
        "must_show": "the believer received at the family doorway with open empty hands — not laboring or paying his way in, but welcomed simply because he belongs; a member of the household drawing him in, his hands open and unearning.",
        "must_not_show": "no wages, coins, tools of labour or payment; no God or Father figure; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on the believer at the wide family doorway, his hands open and empty "
            "at his sides — not working or paying his way in but simply received, drawn "
            "gently in by a member of the household because he belongs to the family. His "
            "face is easy and grateful. Warm daylight from the courtyard. Ordinary-sized, "
            "one head, gaze soft and not to the camera; nothing is written anywhere and "
            "no light rings his head."
        ),
    },
    {
        "id": "v2-r186-b12", "out": "s12-heirs-with-the-son.jpeg", "seg": "n3b",
        "window": "49.893-52.276", "wide": False, "jesus": True, "ref": True,
        "locks": ["DAWN-ROAD", "BELIEVER"],
        "narration": "Heirs together with the Son.",
        "must_show": "the closing image — the risen Lord Jesus and the believer standing together at the crest of the road in the full radiant dawn, side by side as heirs together: Jesus in his cream robe, the believer beside him, both looking out over the bright land they inherit together.",
        "must_not_show": "no God the Father; no halo, ring, rim-light or glow around Jesus; no one but Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "The risen Lord Jesus and the believer stand together at the crest of the "
            "road in the full warm radiant dawn, side by side and backs three-quarters to "
            "the camera as they look out over the bright land spread below — heirs "
            "together, the Son and the one he calls brother — only Jesus wears the plain "
            "cream robe. Camera set behind and beside them looking past their backs into "
            "the dawn; ordinary-sized men on one ground, two heads; the dawn light fills "
            "the sky before them, not ringing their heads; nothing is written anywhere."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# INHERITANCE-HOME and DAWN-ROAD are NEW places — no committed plate yet; the runner
# promotes each from its first NON-Jesus frame (INHERITANCE-HOME from b02, DAWN-ROAD
# from b10) before generating the rest of that place. PAUL-ROOM may reuse build-184's
# plate once that row is built, or be promoted fresh from b01. Steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: PAUL and BELIEVER are carried by byte-identical/build-local text
# locks. Jesus is injected by the assembler on b06/b07/b12 (jesus=True, ref=True).
# Only Jesus wears cream.
REFS = {
}
