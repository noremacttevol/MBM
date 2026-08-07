#!/usr/bin/env python3
"""V2 beat map — row 183, build-183-sun-moon-and-stars (1 Corinthians 15:40-42 — Paul
answers "with what body do the dead rise?" by pointing at the sky: "There is one glory
of the sun, and another glory of the moon, and another glory of the stars... So also
is the resurrection of the dead. It is sown in corruption; it is raised in
incorruption.").

COVERAGE: 17 pictures over 64.419 s (card_start) = ~3.8 s/picture (lesson 12
movie-coverage). Three clearly-distinct threads so every beat fits its moment: PAUL
teaching (the frame), THE HEAVENS he points to (the sun's glory, the moon's glory, the
varied stars), and the RESURRECTION the sky illustrates (the dead raised whole into
the dawn light). One establishing wide per place (b01 Paul's court, b03 the night
heaven, b05 the day heaven, b11 the dawn field).

NO OPEN CAMERON COMPLAINT (v2_outline.py 183 shows none). Fresh authored map.

AUDIO: default AUDIO LOCK stream-copy (no flag). Board Audio = OK. Picture-only
rebuild — do NOT re-voice. card_start = 64.419 s; total with card = 72.286 s.

SPEAKER LAW (see make_narration.py — both s1 and s2 are marked SCRIPTURE):
  s1  1 Cor 15:41  "There is one glory of the sun, and another glory of the moon, and
      another glory of the stars: for one star differeth from another star in glory."
                                                                 SCRIPTURE → light-blue
  s2  1 Cor 15:42  "So also is the resurrection of the dead. It is sown in corruption;
      it is raised in incorruption:"                             SCRIPTURE → light-blue
This is Paul's epistle, quoted as his written argument ("when Paul wrote", "he said")
— so there is NO red-letter (Jesus is not speaking) and NO God-voice. Everything else
is the NARRATOR (white). NO Jesus and NO cream anywhere (New Testament epistle, no
Christophany in this passage).

**HARD GATE — GOD IS NEVER EMBODIED (default gate; no complaint asks otherwise here).**
"The same God who hung the sun, the moon, and every different star" (b17) is carried by
the heavens themselves — God is NEVER shown: no figure, face, hand, throne or
beam-being, and no halo/ring/rim-light around anything (the drift-word gate also bans
those literal words — word the light as radiant / luminous / brilliant / warm in the
sky, never a ring around a head).

CONTENT-CARE (the resurrection of the DEAD → restraint, rows 171/173): the risen are
WHOLE, solid, living, fully-clothed men and women, healthy and glad, rising into the
golden dawn — NEVER corpses, skeletons, bones, decaying flesh, zombies, translucent
ghosts or mist-figures, and never any gore. "Sown in corruption... raised in
incorruption" leans on Paul's OWN grain metaphor (1 Cor 15:37): a seed sown into dark
earth that breaks open and springs up as new living green toward the light — so the
"corruption" is shown as a spent seed/husk and dark earth, never a rotting body.

TIME OF DAY (intentional registers — each light in its own glory): the SUN beats are a
brilliant clear DAY sky; the MOON/STARS beats are a deep luminous NIGHT sky; the
RESURRECTION beats are the first golden break of DAWN. This is a deliberate day/night
split, so the SKY is NOT plate-locked (a single plate would bleed the wrong
time-of-day onto the others — the row-50/101 day/night lesson).

PLACES / LOCKS:
  PAUL          person, byte-identical to builds 138/155/166/171 (cross-video same man).
  PAUL-COURT    (NEW place, plate) an open Corinthian portico under the sky where Paul
                teaches and points up (b01, b02, b10). Runner promotes b01.
  HEAVENS-DAY   (TEXT-LOCK, NO plate — day sky) the sun in full glory (b05, b08).
  HEAVENS-NIGHT (TEXT-LOCK, NO plate — night sky) moon + varied stars, the plural
                glories/lights above (b03, b04, b06, b07, b09, b15, b16).
  RESURRECTION-DAWN (NEW place, plate) the dawn field where the dead rise whole into
                light (b11, b12, b13, b14, b17). Runner promotes b11.
  RISEN-ONES    (TEXT-LOCK) the whole living clothed people who rise (b11, b13, b14).
NEW-place promote plan (runner): PAUL-COURT from b01, RESURRECTION-DAWN from b11.
**IGNORE any --wire "NEW PLACE" suggestion for HEAVENS-DAY, HEAVENS-NIGHT or
RISEN-ONES — they are sky/people text-locks, NOT plate-able locations; do NOT promote
a plate for them (the sky varies day/night by design).**
"""

# LOCKS: all build-local except PAUL (byte-identical global cast). No Jesus / no cream
# (NT epistle). State clothing colours POSITIVELY and never cream/white-fine.
LOCKS = {
    "PAUL": (
        "PAUL LOCK: Paul is the same man in every shot — compact and wiry, about "
        "fifty, balding with a fringe of dark hair, a full pointed dark beard, keen "
        "deep-set eyes, in a plain DARK RUST-BROWN travel robe (never cream, never "
        "white); a tentmaker's strong hands; earnest fire without anger."
    ),
    "PAUL-COURT": (
        "PAUL-COURT LOCK: the same place in every frame — an open colonnaded portico "
        "and courtyard of a first-century Greek city (Corinth) in clear daytime: plain "
        "dressed pale-stone columns and a paved court open to the bright sky above, so "
        "a teacher standing in it can point straight up to the heavens. A few plain "
        "listeners in muted first-century Greek and Judean dress. Sunlit, ancient, "
        "real; no modern object anywhere; nothing is written anywhere. The same portico "
        "and daylight throughout."
    ),
    "HEAVENS-DAY": (
        "HEAVENS-DAY LOCK: the vast daytime heaven in every frame it is named — a deep "
        "clear blue sky filled with the brilliant radiant light of the sun in its full "
        "glory, luminous and warm. NO building, NO ground detail, NO person and NO "
        "figure of any kind; the sun is a natural blazing light, never a face or "
        "ringed disc. Nothing is written anywhere."
    ),
    "HEAVENS-NIGHT": (
        "HEAVENS-NIGHT LOCK: the vast night heaven in every frame it is named — a deep "
        "luminous night sky with a bright silver moon and countless stars of clearly "
        "DIFFERING brightness and size, some blazing and near, some faint and far, no "
        "two burning quite alike — the plural glories of the lights above. NO building, "
        "NO ground detail, NO person and NO figure of any kind; the moon and stars are "
        "natural lights, never faces or ringed discs. Nothing is written anywhere."
    ),
    "RESURRECTION-DAWN": (
        "RESURRECTION-DAWN LOCK: the same place in every frame — a peaceful open field "
        "and low hillside of the ancient near east at the first golden break of dawn, "
        "a few plain ancient stone grave-markers and patches of dark tilled earth "
        "among the grass, the warm radiant light of sunrise spreading low across the "
        "land. Hopeful, warm, reverent — the place where the dead are raised whole into "
        "the morning light. No modern object anywhere; nothing is written anywhere. "
        "The same dawn field and warm sunrise light throughout."
    ),
    "RISEN-ONES": (
        "RISEN-ONES LOCK: the people who rise are WHOLE, solid, living, fully-clothed "
        "men and women of the ancient near east in plain muted robes, healthy and "
        "radiant with new life, rising up or standing in the golden dawn light with "
        "quiet joy and wonder. They are NEVER corpses, skeletons, bones, decaying or "
        "wounded flesh, zombies, translucent ghosts or mist-figures. Distinct "
        "individual faces, ordinary-sized, on one ground plane; no gore, no fear."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r183-b01", "out": "s01-what-body-would-rise.jpeg", "seg": "n0",
        "window": "0.400-5.640", "wide": True, "jesus": False, "ref": False,
        "locks": ["PAUL-COURT", "PAUL"],
        "narration": "When Paul wrote about the resurrection, people asked him what kind of body the dead could possibly rise with.",
        "must_show": "the ONE establishing wide of Paul's court — Paul teaching in the sunlit portico as a few listeners press him with the honest question: with what kind of body could the dead possibly rise? Their faces are questioning, turned to him.",
        "must_not_show": "no God figure; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "A wide of the sunlit Corinthian portico seen from behind and beside the "
            "small group of listeners, their backs three-quarters to the camera as they "
            "sit and stand facing Paul, who stands teaching among the pale stone "
            "columns. Their postures are questioning — they have just asked with what "
            "kind of body the dead could possibly rise. Camera set behind the "
            "listeners looking past them to Paul; ordinary-sized people on one paved "
            "floor; nothing written anywhere."
        ),
    },
    {
        "id": "v2-r183-b02", "out": "s02-he-pointed-at-the-sky.jpeg", "seg": "n0",
        "window": "5.640-8.286", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL-COURT", "PAUL"],
        "narration": "He answered by pointing at the sky.",
        "must_show": "a close on Paul answering not with argument but with a gesture — lifting his hand and eyes straight up toward the open bright sky above the court, pointing them to the heavens for his answer.",
        "must_not_show": "no God figure or beam-being in the sky; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Paul in the sunlit portico, his lined earnest face lifted and "
            "one strong hand raised plainly toward the bright open sky above the "
            "columns — answering the question by pointing them upward to the heavens. "
            "Certain and warm. Ordinary-sized, one head, gaze and hand toward the sky "
            "and not to the camera; no figure in the sky; nothing written anywhere."
        ),
    },
    {
        "id": "v2-r183-b03", "out": "s03-look-up-not-all-alike.jpeg", "seg": "n1",
        "window": "8.286-12.530", "wide": True, "jesus": False, "ref": False,
        "locks": ["HEAVENS-NIGHT"],
        "narration": "Look up, he said. Not everything that shines shines the same way.",
        "must_show": "the ONE establishing wide of the night heaven — a vast deep night sky full of lights that plainly do NOT shine the same way: a bright moon and stars of many different brightnesses scattered across the dark, some blazing, some faint.",
        "must_not_show": "no God figure or beam-being; no person; no Jesus, no cream; no halo, ring or rim-light; no faces in the stars; no modern object; nothing written; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "A vast establishing wide looking straight up into the deep night heaven, "
            "the camera tilted up away from the earth so no one's face or back is "
            "toward the lens — a bright silver moon and countless stars of clearly "
            "differing brightness spread across the dark, plainly not all shining the "
            "same way. Reverent and immense. No figure of any kind; nothing written "
            "anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r183-b04", "out": "s04-different-kinds-of-glory.jpeg", "seg": "n1",
        "window": "12.530-16.365", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENS-NIGHT"],
        "narration": "There are different kinds of bodies, and different kinds of glory.",
        "must_show": "a closer view into the night sky showing the variety plainly — near, blazing stars beside faint distant ones, the moon apart in its own soft light: different kinds of lights, different kinds of glory.",
        "must_not_show": "no God figure; no person; no Jesus, no cream; no halo, ring or rim-light; no faces in the stars; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closer view into the night heaven where the variety is plain — great "
            "near stars burning bright beside faint far ones, and the soft silver moon "
            "apart in its own kind of light — clearly different kinds of lights and "
            "different kinds of glory in one sky. No figure of any kind; nothing "
            "written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r183-b05", "out": "s05-glory-of-the-sun.jpeg", "seg": "s1",
        "window": "16.365-19.800", "wide": True, "jesus": False, "ref": False,
        "locks": ["HEAVENS-DAY"],
        "narration": "There is one glory of the sun,",
        "must_show": "SCRIPTURE, light-blue caption — the ONE establishing wide of the day heaven: the sun in its full radiant glory blazing in a deep clear blue sky, warm and overwhelming, its own kind of brightness.",
        "must_not_show": "no God figure or beam-being; the sun is a natural blazing light, not a face or ringed disc; no person; no Jesus, no cream; no halo, ring or rim-light around anything; no modern object; nothing written; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "A vast establishing wide of the daytime heaven, the camera tilted up away "
            "from the earth so no one's face or back is toward the lens — the sun "
            "blazing in its full radiant glory high in a deep clear blue sky, warm and "
            "overwhelming, filling the frame with its own kind of brightness. No figure "
            "of any kind; nothing written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r183-b06", "out": "s06-glory-of-the-moon.jpeg", "seg": "s1",
        "window": "19.800-22.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENS-NIGHT"],
        "narration": "and another glory of the moon,",
        "must_show": "SCRIPTURE, light-blue caption — the moon in its own softer glory: a bright luminous full moon high in the night sky, its cool silver light quite different from the sun's, its own kind of glory.",
        "must_not_show": "no God figure; the moon is a natural light, not a face or ringed disc; no person; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A view up to the bright full moon riding high in the deep night sky, its "
            "cool luminous silver light spreading softly among the stars — a glory "
            "quite different from the sun's, its own gentler kind of brightness. No "
            "figure of any kind; nothing written anywhere and no ring of light rings "
            "anything."
        ),
    },
    {
        "id": "v2-r183-b07", "out": "s07-star-differeth-from-star.jpeg", "seg": "s1",
        "window": "22.800-26.561", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENS-NIGHT"],
        "narration": "and another glory of the stars: for one star differeth from another star in glory.",
        "must_show": "SCRIPTURE, light-blue caption — the stars in their many glories: a field of countless stars where one plainly differs from another, great bright ones beside faint far ones, each burning with its own glory.",
        "must_not_show": "no God figure; no faces in the stars; no person; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A deep view into a field of countless stars where one plainly differs from "
            "another in glory — great near stars blazing bright beside faint distant "
            "ones, a whole heaven of lights each burning with its own kind of "
            "brightness. No figure of any kind; nothing written anywhere and no ring of "
            "light rings anything."
        ),
    },
    {
        "id": "v2-r183-b08", "out": "s08-sun-its-own-brightness.jpeg", "seg": "n2",
        "window": "26.561-28.370", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENS-DAY"],
        "narration": "The sun has its own brightness.",
        "must_show": "a return to the day heaven — the sun blazing with its own singular brightness in the clear blue sky, unmistakably its own kind of light.",
        "must_not_show": "no God figure; the sun is a natural light, not a face or ringed disc; no person; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A radiant view of the sun blazing with its own singular brightness high in "
            "the deep clear blue day sky, warm light pouring across the heaven — "
            "unmistakably its own kind of light. No figure of any kind; nothing written "
            "anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r183-b09", "out": "s09-no-two-stars-alike.jpeg", "seg": "n2",
        "window": "28.370-30.640", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENS-NIGHT"],
        "narration": "And no two stars burn quite alike.",
        "must_show": "a close into the starfield underscoring that no two stars burn alike — each star a slightly different size, colour and brilliance, a heaven of individual lights.",
        "must_not_show": "no God figure; no faces in the stars; no person; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close into the starfield where every star burns a little differently — "
            "warm and cool tones, larger and smaller, brighter and fainter — no two "
            "quite alike, a heaven of individual lights. No figure of any kind; nothing "
            "written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r183-b10", "out": "s10-the-astonishing-part.jpeg", "seg": "n2",
        "window": "30.640-33.586", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL-COURT", "PAUL"],
        "narration": "Then Paul said the astonishing part.",
        "must_show": "a close on Paul in the sunlit court, turning from the sky back to his listeners with a lit, earnest face, about to say the astonishing thing the whole illustration was for.",
        "must_not_show": "no God figure; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Paul in the sunlit portico turning his gaze from the sky back "
            "to his listeners, his earnest face alight, one hand still half-raised — on "
            "the edge of saying the astonishing thing the whole picture of the heavens "
            "was leading to. Ordinary-sized, one head, gaze toward his hearers and not "
            "to the camera; nothing written anywhere."
        ),
    },
    {
        "id": "v2-r183-b11", "out": "s11-resurrection-of-the-dead.jpeg", "seg": "s2",
        "window": "33.586-36.520", "wide": True, "jesus": False, "ref": False,
        "locks": ["RESURRECTION-DAWN", "RISEN-ONES"],
        "narration": "So also is the resurrection of the dead.",
        "must_show": "SCRIPTURE, light-blue caption — the ONE establishing wide of the dawn field: the resurrection of the dead — whole, living, clothed men and women rising and standing up into the first golden light of sunrise across the field of ancient graves, glad and unafraid.",
        "must_not_show": "no corpses, skeletons, bones, decaying or wounded flesh, zombies, translucent ghosts or mist-figures; no gore; no God figure; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "A wide of the open dawn field seen from behind and to the side of the "
            "rising people, their backs three-quarters to the camera as they rise and "
            "stand up whole and living into the first golden light of sunrise among the "
            "plain ancient grave-markers and grass. They are solid, clothed, healthy "
            "men and women, glad and unafraid — the resurrection of the dead. Camera "
            "behind and beside them looking past them into the sunrise; ordinary-sized "
            "on one ground plane; nothing written anywhere."
        ),
    },
    {
        "id": "v2-r183-b12", "out": "s12-sown-raised.jpeg", "seg": "s2",
        "window": "36.520-41.291", "wide": False, "jesus": False, "ref": False,
        "locks": ["RESURRECTION-DAWN"],
        "narration": "It is sown in corruption; it is raised in incorruption:",
        "must_show": "SCRIPTURE, light-blue caption — Paul's own seed picture: a single spent seed sown deep in dark broken earth below, and from it a strong new living green shoot springing up into the warm golden dawn light above — sown in corruption, raised in incorruption.",
        "must_not_show": "no rotting or decaying body; no corpse, skeleton, bones or gore; no God figure; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A reverent close low to the dawn ground: down in the dark broken earth a "
            "single spent seed has split open (the sown, corruptible thing passing "
            "away), and up out of it a strong fresh green shoot rises into the warm "
            "golden light of sunrise — a living picture of what is sown in corruption "
            "being raised in incorruption. Warm, hopeful; no rotting flesh anywhere. "
            "Nothing written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r183-b13", "out": "s13-what-rising-is-like.jpeg", "seg": "n3",
        "window": "41.291-43.770", "wide": False, "jesus": False, "ref": False,
        "locks": ["RESURRECTION-DAWN", "RISEN-ONES"],
        "narration": "That is what rising is like, he said.",
        "must_show": "a whole risen person standing up radiant and alive in the golden dawn — that is what rising is like: a living, clothed man or woman fully restored, wonder on their face in the sunrise light.",
        "must_not_show": "no corpse, skeleton, bones, decaying flesh, zombie, ghost or mist-figure; no gore; no God figure; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on one risen person standing up whole and radiant in the golden "
            "dawn of the field — a living, clothed man or woman fully restored, wonder "
            "and quiet joy on their face as the sunrise light warms them. This is what "
            "rising is like. Ordinary-sized, one head, gaze lifted into the morning and "
            "not to the camera; the warm light rests on them, not around their head; "
            "nothing written anywhere."
        ),
    },
    {
        "id": "v2-r183-b14", "out": "s14-never-corrupt-again.jpeg", "seg": "n3",
        "window": "43.770-48.900", "wide": False, "jesus": False, "ref": False,
        "locks": ["RESURRECTION-DAWN", "RISEN-ONES"],
        "narration": "What goes into the ground breaks down; what comes back out never will again.",
        "must_show": "the contrast made plain — the dark broken earth and spent husk below (what went in and broke down) beneath the whole, living, incorruptible risen person standing full in the dawn light above (what comes back, never to break down again).",
        "must_not_show": "no corpse, skeleton, bones, decaying or wounded flesh, zombie, ghost or mist-figure; no gore; no God figure; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A view of the dawn field showing the contrast plainly: dark broken earth "
            "and a spent empty husk low in the foreground (what went into the ground "
            "and broke down), and above it a whole, living, clothed person standing "
            "full and strong in the golden sunrise (what comes back out, never to break "
            "down again). Hopeful, warm; no decaying flesh anywhere. Ordinary-sized on "
            "one ground plane; nothing written anywhere and no ring of light rings "
            "anything."
        ),
    },
    {
        "id": "v2-r183-b15", "out": "s15-not-one-flat-outcome.jpeg", "seg": "n3",
        "window": "48.900-51.530", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENS-NIGHT"],
        "narration": "The resurrection isn't one flat outcome.",
        "must_show": "back to the varied heaven — the night sky of many different lights, showing that the resurrection is not one flat sameness but many differing glories, like the differing stars.",
        "must_not_show": "no God figure; no faces in the stars; no person; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A return to the deep night heaven of many differing lights — great bright "
            "stars, faint far ones and the moon apart — a sky that is plainly not one "
            "flat sameness but many different glories, the very picture of a "
            "resurrection that is not one flat outcome. No figure of any kind; nothing "
            "written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r183-b16", "out": "s16-glories-plural-gift-of-light.jpeg", "seg": "n3",
        "window": "51.530-58.630", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENS-NIGHT"],
        "narration": "Like the lights above, there are glories — plural — and every one of them is a gift of light.",
        "must_show": "the whole glory-filled heaven together — the moon and the countless differing stars all shining across the night sky, many glories, plural, and every single one of them plainly a gift of light.",
        "must_not_show": "no God figure; no faces in the stars; no person; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A sweeping view of the whole night heaven together — the silver moon and "
            "countless differing stars all shining across the deep sky, many separate "
            "glories in one heaven, and every single light plainly a gift of light "
            "given. Immense, generous, glad. No figure of any kind; nothing written "
            "anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r183-b17", "out": "s17-a-brightness-for-you.jpeg", "seg": "n4",
        "window": "58.630-64.419", "wide": False, "jesus": False, "ref": False,
        "locks": ["RESURRECTION-DAWN"],
        "narration": "The same God who hung the sun, the moon, and every different star is preparing a brightness for you.",
        "must_show": "the promise brought home — a single hopeful living person standing in the dawn field looking up at the sky where the last stars fade and the sunrise glory spreads; the same God who hung all those lights is preparing a brightness for them, the Giver never shown.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam-being; no corpse or ghost; no Jesus, no cream; no halo, ring or rim-light around anything; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A warm close from behind and beside one hopeful living person standing in "
            "the golden dawn field, their back three-quarters to the camera as they "
            "look up at the wide sky where the last stars still fade and the radiant "
            "sunrise glory spreads across the heaven. The same God who hung the sun, "
            "the moon and every differing star is quietly preparing a brightness for "
            "them; the Giver Himself is never shown. Ordinary-sized, one head, gaze "
            "lifted to the sky and not to the camera; nothing written anywhere and no "
            "ring of light rings anything."
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

# No image REFS: PAUL is carried by a byte-identical text lock (same as builds
# 138/155/166/171). NO Jesus and NO cream in this row.
REFS = {
}
