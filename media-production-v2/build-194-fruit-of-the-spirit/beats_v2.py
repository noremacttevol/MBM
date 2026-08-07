#!/usr/bin/env python3
"""V2 beat map — row 194, build-194-fruit-of-the-spirit (Galatians 5:22-23 — "But the fruit
of the Spirit is love, joy, peace, longsuffering, gentleness, goodness, faith, meekness,
temperance: against such there is no law.").

COVERAGE: 12 pictures over 44.420 s (card_start) = ~3.70 s/picture (lesson 12
movie-coverage). Three places: PAUL-ROOM (Paul writing the letter — the epistle source),
the ORCHARD (the harvest of character the Spirit grows — a fruitful vineyard/orchard heavy
with ripe fruit), and the VILLAGE (where a representative BELIEVER lives the fruit out among
neighbours). Human spine: ONE BELIEVER through whom the fruit grows — each virtue shown as a
real human act, not a symbol; PAUL frames it.

=====================================================================
No open Cameron complaint (v2_outline.py 194). Fresh V2 beat map; Board Audio = OK.
=====================================================================

SPEAKER LAW (Paul's epistle):
  s1  Galatians 5:22-23  "But the fruit of the Spirit is love, joy... temperance:
      against such there is no law."  = SCRIPTURE → LIGHT-BLUE caption.
Every other segment (n0, n1a, n1b, n2, n3, n4, card) is the NARRATOR → white. There is NO
red-letter and NO God-voice in this row: **every beat jesus=False and NO ONE wears cream or
white** (cream is reserved for Jesus, who is absent — this is an epistle).

**HARD GATE — GOD / THE SPIRIT IS NEVER EMBODIED.** "God's Spirit lives in a person" and the
"fruit of the Spirit" are NEVER shown as a figure, face, dove, beam, hand-from-sky or symbol.
The Spirit's work is shown ONLY as real human character lived out (love, patience, gentleness
in ordinary acts) and as a real, natural fruit harvest — ripe grapes, figs and olives on the
vine and tree. No supernatural light, no halo, no ring or beam around anyone; the harvest is
ordinary ripe fruit, not a shining sign. Drift-word gate: no halo / glow / rim-light / beam.

CONTENT-CARE: every virtue is a warm, ordinary, dignified human moment — no staged tableau
of symbols, no one posing. "Peace that doesn't depend on circumstances" and "self-control
that masters the storms inside" are shown as calm steadiness in a real hard moment, never as
a mystical trance or a supernatural sign.

TIME-OF-DAY: warm ordinary daylight throughout (PAUL-ROOM soft daylight; ORCHARD and VILLAGE
bright day). No night, no divine light.

PLACES / LOCKS:
  PAUL-ROOM  Paul's writing room (b01) — reused BYTE-IDENTICAL to build-184/186 (recurring
             place); runner may --wire the existing build-184/186 PAUL-ROOM plate.
  ORCHARD    the fruitful vineyard/orchard — the Spirit's harvest of character (b02/b04/b12).
             NEW build-local place; runner promotes from b02.
  VILLAGE    the everyday village where the believer lives the fruit out (b03/b05/b06/b07/
             b08/b09/b10/b11). NEW build-local place; runner promotes from b03.
People locks: PAUL (BYTE-IDENTICAL to build-184/186 — recurring cast), BELIEVER (the
representative person the Spirit lives in — recurring across the virtue frames), VILLAGERS
(the neighbours the believer loves, bears with and serves). None wear cream or white.

AUDIO: default AUDIO LOCK stream-copy (no re-voice; no open complaint). Board Audio = OK.
card_start = 44.420 s. Picture-only — do NOT re-voice.
"""

# PAUL + PAUL-ROOM are reused BYTE-IDENTICAL to build-184/186 (recurring cast/place). ORCHARD
# and VILLAGE are NEW build-local places the runner promotes. Jesus is absent (every beat
# jesus=False); no image REFS; only text locks. No one wears cream/white; the Spirit is
# never embodied.
LOCKS = {
    "PAUL-ROOM": (
        "PAUL-ROOM LOCK: the same place in every frame — a humble first-century room "
        "where Paul writes his letters: plain lime-plastered stone walls, a low wooden "
        "writing table with a sheet of parchment, a reed pen and a small clay oil lamp, "
        "a simple stool and a floor mat, and one plain rectangular window opening to "
        "soft daylight. Ancient, spare, real; no modern object anywhere; any parchment "
        "is blank with no legible or rendered writing. The same room and warm plain "
        "daylight throughout."
    ),
    "ORCHARD": (
        "ORCHARD LOCK: the same place in every frame — a fruitful first-century "
        "vineyard and orchard on a warm hillside: rows of grapevines heavy with ripe "
        "purple clusters, fig and olive trees bearing fruit, low stone terrace walls and "
        "woven harvest baskets. The fruit is real, ripe and natural — an ordinary "
        "abundant harvest, never a shining or supernatural sign. Ancient and real; no "
        "modern object anywhere, and nothing written. The same fruitful hillside "
        "throughout, in warm daylight."
    ),
    "VILLAGE": (
        "VILLAGE LOCK: the same place in every frame — an ordinary first-century village: "
        "dusty lanes between low stone and mud-brick houses, dark doorways, a well-head, a "
        "few market stalls and worn steps, everyday life going on. Ancient and real; no "
        "modern object anywhere, and nothing legible or rendered is written on any "
        "surface. The same village lanes throughout, in warm daylight."
    ),
    "PAUL": (
        "PAUL LOCK: Paul is the same man in every shot — compact and wiry, about "
        "fifty, balding with a fringe of dark hair, a full pointed dark beard, keen "
        "deep-set eyes, in a plain DARK RUST-BROWN travel robe (never cream, never "
        "white); a tentmaker's strong hands; earnest fire without anger."
    ),
    "BELIEVER": (
        "BELIEVER LOCK: the same person in every frame they appear — a representative "
        "first-century villager of about thirty-five in whom the Spirit lives, warm "
        "olive-brown skin, dark hair, a short dark beard, kind steady eyes, in a plain "
        "muted blue-and-brown wool tunic and mantle (never cream, never white). Through "
        "this one ordinary life the fruit is shown — loving, patient, gentle, "
        "self-possessed. The same face and clothing throughout."
    ),
    "VILLAGERS": (
        "VILLAGERS LOCK: the neighbours of the village — a mixed group of ordinary "
        "first-century men, women and children in plain earth-toned wool (never cream, "
        "never white); the ones the believer loves, bears with, is gentle to and serves. "
        "Distinct individual faces, not twins. The same kind of people throughout."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r194-b01", "out": "s01-paul-writes.jpeg", "seg": "n0",
        "window": "0.000-3.400", "wide": True, "jesus": False, "ref": False,
        "locks": ["PAUL-ROOM", "PAUL"],
        "narration": "Paul wrote that when God's Spirit lives in a person, a harvest grows —",
        "must_show": "the establishing frame, NON-Jesus (the PAUL-ROOM plate) — Paul at his low writing table in soft daylight, reed pen over a blank parchment, writing earnestly to the churches.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Spirit figure, dove or beam; no legible or rendered writing on the parchment; no halo, glare or rim-light; no modern object; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing shot of Paul's humble writing room in soft daylight, camera "
            "set low and behind Paul's shoulder looking past him to the sunlit window, so "
            "his back is three-quarters to the lens and his gaze goes down onto the "
            "parchment and out to the window, never to the camera: Paul — compact, "
            "dark-bearded, in a dark rust-brown travel robe (not cream) — sits at his low "
            "table, reed pen over a blank parchment, writing earnestly. A small clay lamp "
            "and the plain window. Ancient and spare; the parchment carries nothing "
            "legible; warm daylight rests on him, not around his head; nothing is written "
            "anywhere; no divine or Spirit figure."
        ),
    },
    {
        "id": "v2-r194-b02", "out": "s02-a-harvest-of-character.jpeg", "seg": "n0",
        "window": "3.400-6.769", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD", "BELIEVER"],
        "narration": "not crops, but character.",
        "must_show": "the ORCHARD plate (NON-Jesus) — the believer among the fruitful vines, a basket of ripe grapes and figs gathered; the harvest the Spirit grows is real ripe fruit standing for character, not a supernatural sign.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Spirit figure, dove or beam; no shining or supernatural fruit; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A medium in the fruitful vineyard in warm daylight: the believer (muted "
            "blue-and-brown wool, not cream) stands among grapevines heavy with ripe "
            "purple clusters, a woven basket of grapes and figs in his arms — the harvest "
            "of character the Spirit grows. The fruit is ordinary and ripe, never shining "
            "or supernatural. Ordinary-sized, one head, gaze over the fruit and vines, not "
            "to the camera; warm daylight on the harvest, not around his head; nothing is "
            "written anywhere; no divine or Spirit figure."
        ),
    },
    {
        "id": "v2-r194-b03", "out": "s03-love.jpeg", "seg": "s1",
        "window": "6.769-10.900", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE", "BELIEVER", "VILLAGERS"],
        "narration": "But the fruit of the Spirit is love, joy, peace,",
        "must_show": "BLUE caption (SCRIPTURE) — the fruit begun in a life: the believer showing love in the village, an arm around a grieving neighbour, warmth and gladness between them. The Spirit is NOT shown.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Spirit figure, dove or beam; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot in the village lane in warm daylight: the believer (not cream) draws "
            "an arm around a grieving neighbour, meeting their eyes with real love and "
            "warmth; another villager nearby lightens with gladness. Ordinary human "
            "kindness, no figure stands in for the Spirit. Ordinary-sized people, one head "
            "each, gazes meeting between them, not to the camera; warm daylight on them, "
            "not around any head; nothing is written anywhere; no divine or Spirit figure."
        ),
    },
    {
        "id": "v2-r194-b04", "out": "s04-fruit-on-the-vine.jpeg", "seg": "s1",
        "window": "10.900-14.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD"],
        "narration": "longsuffering, gentleness, goodness, faith,",
        "must_show": "BLUE caption (SCRIPTURE) — an insert of the ripe fruit itself on the vine and tree — grapes, figs and olives heavy and ready — the many kinds of fruit the one Spirit grows. The Spirit is NOT shown.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Spirit figure, dove or beam; no shining or supernatural fruit; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A tight insert in the orchard in warm daylight on ripe fruit hanging heavy — "
            "purple grape clusters on the vine, dark figs and olives on the branch, ready "
            "for harvest: the many kinds of fruit the one Spirit grows. Natural, ordinary "
            "ripe fruit, never shining. Warm daylight on the fruit, not a ring of light "
            "anywhere; nothing is written; no divine or Spirit figure."
        ),
    },
    {
        "id": "v2-r194-b05", "out": "s05-no-law-against.jpeg", "seg": "s1",
        "window": "14.800-18.610", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE", "BELIEVER"],
        "narration": "meekness, temperance: against such there is no law.",
        "must_show": "BLUE caption (SCRIPTURE) — the believer walking free and unhurried down the open village lane, at peace — against such fruit there is no law, nothing to forbid it. The Spirit is NOT shown.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Spirit figure, dove or beam; no chains or written law; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of the believer (not cream) walking free and unhurried down an open, "
            "sunlit village lane, calm and at peace — a life against which there is no law "
            "and nothing to forbid. Ordinary-sized, one head, gaze ahead down the open "
            "lane, not to the camera; warm daylight on him, not around his head; nothing "
            "is written anywhere; no divine or Spirit figure."
        ),
    },
    {
        "id": "v2-r194-b06", "out": "s06-love-then-joy.jpeg", "seg": "n1a",
        "window": "18.610-20.889", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE", "BELIEVER", "VILLAGERS"],
        "narration": "First, love. Then joy.",
        "must_show": "love turning to joy — the believer lifting a child or clasping a friend, real gladness breaking across both their faces.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Spirit figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close two-shot in the village in warm daylight: the believer (not cream) "
            "lifts a laughing child or clasps a friend, real joy breaking across both "
            "their faces — love turned to gladness. Ordinary-sized, one head each, gazes "
            "meeting in delight, not to the camera; warm daylight on them, not around any "
            "head; nothing is written anywhere; no divine or Spirit figure."
        ),
    },
    {
        "id": "v2-r194-b07", "out": "s07-peace.jpeg", "seg": "n1b",
        "window": "20.889-25.230", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE", "BELIEVER"],
        "narration": "Then peace — the kind that doesn't depend on circumstances.",
        "must_show": "peace that doesn't depend on circumstances — the believer calm and steady in the middle of a hard, unsettled moment around him, quiet and unshaken.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Spirit figure; no mystical trance or supernatural sign; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot in the village in warm daylight: around the believer a hard, "
            "unsettled moment — anxious neighbours, an overturned load, worry on faces — "
            "yet he stands calm and steady in the middle of it, quiet and unshaken. Not a "
            "trance, just settled peace. Ordinary-sized people, one head each; the "
            "believer's gaze level and calm, not to the camera; warm daylight, not around "
            "any head; nothing is written anywhere; no divine or Spirit figure."
        ),
    },
    {
        "id": "v2-r194-b08", "out": "s08-longsuffering.jpeg", "seg": "n2",
        "window": "25.230-29.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE", "BELIEVER", "VILLAGERS"],
        "narration": "Longsuffering next — patience that doesn't quit.",
        "must_show": "longsuffering — the believer patiently, kindly bearing with a difficult or slow neighbour, not giving up on them, steady and unangered.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Spirit figure; no anger; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot in the village in warm daylight: the believer (not cream) patiently "
            "and kindly bears with a difficult, struggling neighbour — a steadying hand, "
            "an unangered face, staying with them rather than giving up. Patience that "
            "doesn't quit. Ordinary-sized people, one head each, gazes between them, not "
            "to the camera; warm daylight on them, not around any head; nothing is written "
            "anywhere; no divine or Spirit figure."
        ),
    },
    {
        "id": "v2-r194-b09", "out": "s09-gentleness-goodness-faith.jpeg", "seg": "n2",
        "window": "29.500-33.855", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE", "BELIEVER", "VILLAGERS"],
        "narration": "Then gentleness, and goodness, and faith that holds.",
        "must_show": "gentleness, goodness and faith joined in one act — the believer gently helping a frail or poor neighbour with a good, faithful steadiness they can rely on.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Spirit figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot in the village in warm daylight: the believer (not cream) gently "
            "steadies a frail elderly neighbour by the arm and hands them bread or helps "
            "them along — gentleness, goodness and a steady, faithful kindness they can "
            "lean on. Ordinary-sized people, one head each, gazes meeting in trust, not to "
            "the camera; warm daylight on them, not around any head; nothing is written "
            "anywhere; no divine or Spirit figure."
        ),
    },
    {
        "id": "v2-r194-b10", "out": "s10-meekness-temperance.jpeg", "seg": "n3",
        "window": "33.855-39.080", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE", "BELIEVER"],
        "narration": "Meekness, and temperance — self-control that masters the storms inside.",
        "must_show": "meekness and temperance — the believer, provoked or wronged, holding himself in check with humble strength, mastering the storm inside rather than striking back.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Spirit figure; no violence or striking; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on the believer (not cream) in the village daylight, provoked or "
            "wronged by another, yet holding himself in check with humble, quiet strength "
            "— jaw set, hand unclenched, mastering the storm inside rather than striking "
            "back. Meekness and self-control. Ordinary-sized, one head, gaze steady and "
            "restrained, not to the camera; warm daylight on his face, not around his "
            "head; nothing is written anywhere; no divine or Spirit figure."
        ),
    },
    {
        "id": "v2-r194-b11", "out": "s11-no-law-forbids.jpeg", "seg": "n4",
        "window": "39.080-41.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE", "BELIEVER", "VILLAGERS"],
        "narration": "And no law anywhere forbids any of it.",
        "must_show": "the freedom of it — the believer welcomed and at ease among his neighbours, nothing anywhere to forbid such a life; open, unburdened, glad.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Spirit figure; no chains or written law; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot in the sunlit village square: the believer (not cream) welcomed and at "
            "ease among his neighbours, open-handed and unburdened — a life nothing "
            "anywhere forbids. Ordinary-sized people on one lane, one head each, gazes "
            "warm between them, not to the camera; warm daylight on them, not around any "
            "head; nothing is written anywhere; no divine or Spirit figure."
        ),
    },
    {
        "id": "v2-r194-b12", "out": "s12-cant-be-overdone.jpeg", "seg": "n4",
        "window": "41.800-44.420", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD", "BELIEVER", "VILLAGERS"],
        "narration": "These are the things that can't be overdone.",
        "must_show": "the closing image — the orchard at full harvest, the believer and neighbours gathering baskets brimming with ripe fruit, more is only better; the things that can't be overdone.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Spirit figure, dove or beam; no shining or supernatural fruit; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closing shot in the fruitful orchard in warm daylight: the believer and his "
            "neighbours (none cream) gather baskets brimming with ripe grapes, figs and "
            "olives at full harvest, glad and unhurried — fruit that can only ever be "
            "more, never overdone. Ordinary ripe fruit, never shining. Ordinary-sized "
            "people, one head each, gazes over the plenty and to one another, not to the "
            "camera; warm daylight on the harvest, not around any head; nothing is written "
            "anywhere; no divine or Spirit figure."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# PAUL-ROOM is reused byte-identical to build-184/186 — the runner may --wire that existing
# plate. ORCHARD and VILLAGE are NEW places with no committed plate yet; the runner promotes
# ORCHARD from b02 and VILLAGE from b03 (all frames here are NON-Jesus). Steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: all places and people are carried by the build-local text locks above (PAUL
# and PAUL-ROOM byte-identical to build-184/186). Jesus does not appear in this row (every
# beat jesus=False); no one wears cream or white; God/the Spirit is never embodied.
REFS = {
}
