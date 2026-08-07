#!/usr/bin/env python3
"""V2 beat map — row 184, build-184-third-heaven (2 Corinthians 12:2-4,9 — Paul caught
up to the third heaven and into paradise, then the Lord's answer to his thorn: "My
grace is sufficient for thee: for my strength is made perfect in weakness.").

COVERAGE: 16 pictures over 66.687 s (card_start) = ~4.1 s/picture (lesson 12
movie-coverage). Two clearly-distinct places so every beat fits its moment: PAUL-ROOM
(Paul writing, holding his silence, pointing to his weakness, and the Lord answering
him) and the HEAVENLY-ASCENT (the vision of being caught up through radiant heights).
The "man in Christ" Paul speaks of in the third person IS Paul himself, so the one
caught up is PAUL. One establishing wide per place (b01 the room, b02 the ascent).

=====================================================================
OPEN CAMERON COMPLAINT (v2_outline.py 184): "only Jesus's words in red."
FIX (author-level, speaker law): the ONLY red-letter segment in this row is j1 — "My
grace is sufficient for thee: for my strength is made perfect in weakness." — which is
genuinely Jesus's own words (the Lord's answer to Paul), and it is placed on the risen
LORD JESUS speaking to Paul (b12/b13, jesus=True, RED caption). Paul's own written
account s1 ("I knew a man in Christ...") and s2 ("caught up into paradise...") are
SCRIPTURE → LIGHT-BLUE captions, NEVER red (they are Paul's words, not the Lord's).
Every narrator segment (n0-n3, card) is WHITE. So exactly one thing is red, and it is
Jesus's words. (make_narration.py already carries this map: only j1 = JESUS.) The
review card must tell Cameron: only Jesus's words are in red now.
=====================================================================

AUDIO: default AUDIO LOCK stream-copy (no flag). Board Audio = OK. Picture-only
rebuild — do NOT re-voice. card_start = 66.687 s; total with card = 75.415 s.

SPEAKER LAW (see make_narration.py):
  s1  2 Cor 12:2   Paul's account "I knew a man in Christ..."   SCRIPTURE → light-blue
  s2  2 Cor 12:4   "caught up into paradise... unspeakable..."  SCRIPTURE → light-blue
  j1  2 Cor 12:9   "My grace is sufficient for thee..."         JESUS → RED (on Jesus)
Everything else is the NARRATOR (white). Jesus appears (jesus=True + ref=True + LOCK)
ONLY on b12/b13 (the grace saying); only he wears cream.

**HARD GATE — THE VISION DOES NOT DEPICT GOD, PARADISE, OR THE UNSPEAKABLE WORDS.**
The ascent beats (b02-b08) show ONLY Paul borne up through radiant heights of light —
NEVER God the Father, a throne, any divine or heavenly figure or being, and NEVER the
contents of paradise or any picture/text of the "unspeakable words which it is not
lawful for a man to utter" (2 Cor 12:4 forbids uttering them, so they are NOT shown —
the surpassing light hides all it holds). Jesus is NOT in the ascent; he appears only
at the grace saying (b12/b13). No halo/ring/rim-light around anything (drift-word gate;
word the light radiant/luminous/brilliant in the heights, never a ring around a head).

CONTENT-CARE: reverent wonder throughout, no fear/horror. Paul's "weakness" is shown as
humility, not sickness or wounds (no thorn-in-the-flesh literalism, no gore). The Lord's
answer is gentle and warm.

PLACES / LOCKS:
  PAUL          person, byte-identical to builds 138/155/166/171 (cross-video same man).
  PAUL-ROOM     (NEW place, plate from the NON-Jesus b01) the humble room where Paul
                writes and where the Lord answers him (b01, b09, b10, b11, b12, b13,
                b14, b15, b16).
  HEAVENLY-ASCENT (NEW place, plate from b02) the vision of being caught up through
                radiant heights (b02-b08). No divine figure, no paradise contents.
NEW-place promote plan (runner): PAUL-ROOM from b01 (a NON-Jesus frame — never promote
a Jesus-bearing frame, lesson 11), HEAVENLY-ASCENT from b02. Steps in QC.md.
"""

# LOCKS: all build-local except PAUL (byte-identical global cast). Jesus is injected by
# the assembler on jesus=True beats; only Jesus wears cream.
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
    "HEAVENLY-ASCENT": (
        "HEAVENLY-ASCENT LOCK: the same vision-realm in every frame — vast radiant "
        "heights of brilliant ascending light rising far above the everyday world, "
        "layer beyond layer of surpassing warm brightness climbing into an immense "
        "luminous heaven, the ordinary earth falling far away below. Reverent, "
        "boundless, overwhelming. There is NO God, NO throne, NO divine or heavenly "
        "figure or being of any kind, and NOTHING of paradise's contents is shown; the "
        "surpassing light hides all that it holds. Nothing is written anywhere. The "
        "same radiant ascending heights throughout."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r184-b01", "out": "s01-paul-wrote-of-a-man.jpeg", "seg": "n0",
        "window": "0.400-6.445", "wide": True, "jesus": False, "ref": False,
        "locks": ["PAUL-ROOM", "PAUL"],
        "narration": "Paul wrote of a man he knew — caught up, in a single moment, far beyond the everyday world.",
        "must_show": "the ONE establishing wide of Paul's room — Paul at his low writing table, pen paused over the parchment, his face lifted in quiet wonder as he writes of a man he knew who was caught up in a single moment far beyond the everyday world.",
        "must_not_show": "no God figure; no Jesus, no cream; no halo, ring or rim-light; no legible or rendered writing; no modern object; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "A wide of the humble writing room seen from behind and to the side of "
            "Paul, his back three-quarters to the camera as he sits at the low table, "
            "reed pen paused over a blank parchment and his lined face lifted in quiet "
            "wonder toward the soft window light. He is setting down the account of a "
            "man he knew, caught up in a single moment far beyond the everyday world. "
            "Camera behind and beside him looking past him to the table and window; "
            "ordinary-sized, one head; nothing legible is written on the parchment."
        ),
    },
    {
        "id": "v2-r184-b02", "out": "s02-i-knew-a-man-in-christ.jpeg", "seg": "s1",
        "window": "6.445-10.500", "wide": True, "jesus": False, "ref": False,
        "locks": ["HEAVENLY-ASCENT", "PAUL"],
        "narration": "I knew a man in Christ above fourteen years ago,",
        "must_show": "SCRIPTURE, light-blue caption — the ONE establishing wide of the ascent: the man (Paul himself) beginning to be caught up, borne upward from the everyday world into the first radiant heights, the ordinary earth already falling away far below him.",
        "must_not_show": "no God figure, throne or divine being; no paradise contents; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "A vast establishing wide of the man caught up, seen from below and behind "
            "so his back is three-quarters to the camera as he is borne upward away "
            "from the ordinary earth that falls far below, into the first radiant "
            "heights of warm ascending light. Weightless, overwhelmed, small against "
            "the immense brightness above him. Camera set below and behind him looking "
            "up past him into the heights; ordinary-sized; no figure but him anywhere; "
            "nothing written and no ring of light rings his head."
        ),
    },
    {
        "id": "v2-r184-b03", "out": "s03-in-body-or-out.jpeg", "seg": "s1",
        "window": "10.500-15.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENLY-ASCENT", "PAUL"],
        "narration": "(whether in the body, I cannot tell; or whether out of the body, I cannot tell: God knoweth;)",
        "must_show": "SCRIPTURE, light-blue caption — Paul borne higher through the radiant light, dreamlike and weightless, so caught up that he cannot tell whether he is in the body or out of it; only God knows.",
        "must_not_show": "no God figure or being; no paradise contents; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closer view of the man borne higher through veils of warm radiant light, "
            "weightless and dreamlike, his robe and hair drifting as if gravity has "
            "loosed him — so caught up that whether he is in the body or out of it "
            "cannot be told. Awe and surrender on his face. Ordinary-sized, one head, "
            "gaze up into the brightness and not to the camera; no other figure; "
            "nothing written and no ring of light rings his head."
        ),
    },
    {
        "id": "v2-r184-b04", "out": "s04-third-heaven.jpeg", "seg": "s1",
        "window": "15.500-20.040", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENLY-ASCENT", "PAUL"],
        "narration": "such an one caught up to the third heaven.",
        "must_show": "SCRIPTURE, light-blue caption — the man carried up into the great radiant heights, far above, small against layer upon layer of surpassing brightness climbing into the immense heaven — caught up to the third heaven.",
        "must_not_show": "no God figure, throne or being; no paradise contents; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A soaring view of the man carried far up into the great radiant heights, "
            "small against layer upon layer of surpassing warm brightness rising into "
            "the boundless luminous heaven high above the fallen-away earth. Immense, "
            "reverent, overwhelming. Ordinary-sized and small in the vastness, one "
            "head, borne upward; no other figure anywhere; nothing written and no ring "
            "of light rings his head."
        ),
    },
    {
        "id": "v2-r184-b05", "out": "s05-could-not-say.jpeg", "seg": "n1",
        "window": "20.040-23.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENLY-ASCENT", "PAUL"],
        "narration": "Whether in the body or out of it, Paul could not say;",
        "must_show": "a close on Paul in the radiant heights, utterly in awe, unable to say whether he is in the body or out of it — lost in wonder in the brightness.",
        "must_not_show": "no God figure or being; no paradise contents; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Paul suspended in the warm radiant heights, eyes wide and lips "
            "parted in speechless awe, so lost in wonder that he cannot say whether he "
            "is in the body or out of it. The surpassing light is all around him. "
            "Ordinary-sized, one head, gaze into the brightness and not to the camera; "
            "no other figure; nothing written and no ring of light rings his head."
        ),
    },
    {
        "id": "v2-r184-b06", "out": "s06-carried-further-still.jpeg", "seg": "n1",
        "window": "23.500-26.600", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENLY-ASCENT", "PAUL"],
        "narration": "And from that height, he was carried further still.",
        "must_show": "Paul carried further and deeper into the radiance, from the great height onward into even more surpassing light, drawn on beyond where he already was.",
        "must_not_show": "no God figure, throne or being; no paradise contents; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "Paul is drawn further still from that great height, borne onward and deeper "
            "into an even more surpassing warmth of radiant light, the brightness "
            "swelling around him as he is carried beyond where he already was. Ever "
            "upward and inward. Ordinary-sized, one head, borne on into the light and "
            "not to the camera; no other figure; nothing written and no ring of light "
            "rings his head."
        ),
    },
    {
        "id": "v2-r184-b07", "out": "s07-into-paradise.jpeg", "seg": "s2",
        "window": "26.600-30.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENLY-ASCENT", "PAUL"],
        "narration": "How that he was caught up into paradise,",
        "must_show": "SCRIPTURE, light-blue caption — Paul drawn to the very threshold of paradise: a boundary of surpassing radiant light before him that hides all it holds, its contents unseen inside the brilliance; he is caught up to its edge.",
        "must_not_show": "the contents of paradise are NEVER shown — no God, throne, being, gate, garden, city or any interior; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "Paul is drawn to the very threshold of paradise — before him a boundary of "
            "surpassing radiant light so bright it hides all that lies within, its "
            "contents unseen inside the pure brilliance. He is caught up to its edge, "
            "small and reverent before the overwhelming warm light. Ordinary-sized, one "
            "head, gaze into the brightness and not to the camera; nothing of what lies "
            "within is shown; nothing written and no ring of light rings his head."
        ),
    },
    {
        "id": "v2-r184-b08", "out": "s08-unspeakable-words.jpeg", "seg": "s2",
        "window": "30.500-34.636", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEAVENLY-ASCENT", "PAUL"],
        "narration": "and heard unspeakable words, which it is not lawful for a man to utter.",
        "must_show": "SCRIPTURE, light-blue caption — Paul overcome as he HEARS unspeakable words: a close on his listening, awestruck face bathed in radiant light, one hand near his heart — the words themselves never shown, for it is not lawful to utter them.",
        "must_not_show": "NO depiction of the words — no text, letters, symbols, scenes, visions of God or paradise's contents, no figure or being; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written anywhere; not a cartoon.",
        "scene": (
            "A close on Paul's listening face in the surpassing radiant light, eyes "
            "closed or half-closed and one hand near his heart, utterly overcome as he "
            "hears words no man is permitted to utter. What he hears is never shown — "
            "only the light and his awestruck listening. Ordinary-sized, one head, "
            "rapt and reverent, not to the camera; no other figure, no text or symbol "
            "anywhere; no ring of light rings his head."
        ),
    },
    {
        "id": "v2-r184-b09", "out": "s09-not-allowed-to-repeat.jpeg", "seg": "n2",
        "window": "34.636-40.580", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL-ROOM", "PAUL"],
        "narration": "He heard things he was not allowed to repeat — words a person is not permitted to say out loud.",
        "must_show": "back in his humble room, Paul keeping the silence — sitting quiet at his table with a hand resting over his heart, holding what he heard and is not permitted to repeat.",
        "must_not_show": "no God figure; no vision or its contents; no Jesus, no cream; no halo, ring or rim-light; no legible writing; no modern object; not a cartoon.",
        "scene": (
            "Back in the humble writing room in plain daylight, Paul sits quiet at his "
            "table, one hand resting over his heart, his face thoughtful and reverent — "
            "keeping the silence, holding within him the things he heard and is not "
            "permitted to say out loud. Ordinary-sized, one head, gaze inward and not "
            "to the camera; nothing legible is written on the parchment."
        ),
    },
    {
        "id": "v2-r184-b10", "out": "s10-he-had-the-credentials.jpeg", "seg": "n2",
        "window": "40.580-43.560", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL-ROOM", "PAUL"],
        "narration": "He could have boasted. He had the credentials.",
        "must_show": "Paul with the tokens of his standing at hand — a stack of his rolled letters and a traveller's worn cloak on the table beside him, the credentials he could have boasted of; he looks at them without pride.",
        "must_not_show": "no God figure; no Jesus, no cream; no halo, ring or rim-light; no legible or rendered writing on the scrolls; no modern object; not a cartoon.",
        "scene": (
            "A close on Paul at his table beside the tokens of his standing — a small "
            "stack of his rolled letters and a worn traveller's cloak — the credentials "
            "he could easily have boasted of. He looks at them steadily and without "
            "pride. Ordinary-sized, one head; the rolled parchments carry no legible or "
            "rendered writing; nothing else is written anywhere."
        ),
    },
    {
        "id": "v2-r184-b11", "out": "s11-pointed-to-his-weakness.jpeg", "seg": "n2",
        "window": "43.560-48.347", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL-ROOM", "PAUL"],
        "narration": "Instead he pointed to his weakness — because of what the Lord had told him.",
        "must_show": "Paul setting the credentials aside and humbling himself — turning from the rolled letters with open, empty hands, pointing instead to his own weakness, moved by what the Lord had told him.",
        "must_not_show": "no God figure; no Jesus yet, no cream; no halo, ring or rim-light; no wound, sore or gore (weakness = humility, not sickness); no legible writing; no modern object; not a cartoon.",
        "scene": (
            "Paul turns away from the rolled letters and the cloak with open, empty "
            "hands and a humbled, softened face — laying his credentials aside and "
            "pointing instead to his own weakness, moved by what the Lord had told "
            "him. Quiet and unashamed. Ordinary-sized, one head, gaze lowered and "
            "peaceful, not to the camera; nothing legible is written anywhere."
        ),
    },
    {
        "id": "v2-r184-b12", "out": "s12-my-grace-is-sufficient.jpeg", "seg": "j1",
        "window": "48.347-51.800", "wide": False, "jesus": True, "ref": True,
        "locks": ["PAUL-ROOM", "PAUL"],
        "narration": "My grace is sufficient for thee:",
        "must_show": "RED caption (Jesus's own words) — the risen Lord Jesus present with Paul in the room, speaking gently to him: 'My grace is sufficient for thee.' Jesus in his cream robe, warm and kind; Paul turned to him, listening.",
        "must_not_show": "no God the Father; no halo, ring, rim-light or glow around Jesus; no one but Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "The risen Lord Jesus stands warmly with Paul in the humble room, turned to "
            "him and speaking gently and kindly, his hand open toward Paul in "
            "reassurance — only he wears the plain cream robe. Paul is turned toward "
            "him, humbled and listening, receiving the word that grace is enough. Soft "
            "plain daylight fills the room. Ordinary-sized men on one floor, two heads; "
            "warm light rests on them, not around their heads; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r184-b13", "out": "s13-strength-in-weakness.jpeg", "seg": "j1",
        "window": "51.800-55.184", "wide": False, "jesus": True, "ref": True,
        "locks": ["PAUL-ROOM", "PAUL"],
        "narration": "for my strength is made perfect in weakness.",
        "must_show": "RED caption (Jesus's own words) — a closer two-shot of the Lord Jesus finishing the promise to Paul: 'for my strength is made perfect in weakness.' Jesus warm and steady in his cream robe; Paul receiving it, comforted.",
        "must_not_show": "no God the Father; no halo, ring, rim-light or glow around Jesus; no one but Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closer two-shot of the Lord Jesus and Paul in the room, Jesus warm and "
            "steady as he finishes the promise — that his strength is made perfect in "
            "weakness — only he in the plain cream robe, his gaze kind and sure. Paul "
            "receives it with a comforted, humbled face. Ordinary-sized men, two "
            "heads, on one floor; the warm daylight rests on them, not around their "
            "heads; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r184-b14", "out": "s14-what-i-give-is-enough.jpeg", "seg": "n3",
        "window": "55.184-57.730", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL-ROOM", "PAUL"],
        "narration": "What I give you is enough, the Lord told him.",
        "must_show": "Paul alone now, comforted, holding the Lord's assurance close — his face at peace in the warm room, the promise that what the Lord gives is enough settling on him; the Lord's presence felt as warmth, not shown.",
        "must_not_show": "no God or Jesus figure now (the Lord's presence is warmth only); no halo, ring or rim-light; no cream on anyone; no legible writing; no modern object; not a cartoon.",
        "scene": (
            "Paul alone in the warm plain daylight of his room, his face eased into "
            "peace and gratitude, one hand at his chest as he holds the Lord's "
            "assurance close — that what the Lord gives is enough. The Lord's presence "
            "is felt as warmth in the room, not shown. Ordinary-sized, one head, gaze "
            "soft and peaceful, not to the camera; nothing is written anywhere and no "
            "ring of light rings his head."
        ),
    },
    {
        "id": "v2-r184-b15", "out": "s15-strength-in-weak-places.jpeg", "seg": "n3",
        "window": "57.730-61.400", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL-ROOM", "PAUL"],
        "narration": "My strength does its best work in the places where you are weakest.",
        "must_show": "Paul quietly strengthened in his very weakness — sitting humble and steady, a new quiet strength on his face precisely where he had felt weakest, the paradox of the Lord's word taking hold in him.",
        "must_not_show": "no God or Jesus figure; no halo, ring or rim-light; no cream; no wound or sore; no legible writing; no modern object; not a cartoon.",
        "scene": (
            "Paul sits humble and steady in the warm room, a new quiet strength "
            "settling on his face in the very place he had felt weakest — the Lord's "
            "strength doing its best work in his weakness. Calm, resolved, unproud. "
            "Ordinary-sized, one head, gaze steady and peaceful, not to the camera; "
            "nothing is written anywhere and no ring of light rings his head."
        ),
    },
    {
        "id": "v2-r184-b16", "out": "s16-still-pointed-to-grace.jpeg", "seg": "n3",
        "window": "61.400-66.687", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL-ROOM", "PAUL"],
        "narration": "Paul was shown more than words can carry — and still pointed back to grace.",
        "must_show": "Paul back at his letter, having seen more than words can carry, yet setting it all aside to point once more to grace — his open hand resting on the parchment, his face humble and at peace, choosing grace over any boast.",
        "must_not_show": "no God or Jesus figure; no vision contents; no halo, ring or rim-light; no cream; no legible or rendered writing; no modern object; not a cartoon.",
        "scene": (
            "Paul is back at his low writing table in the warm daylight, his reed pen in "
            "hand and one open hand resting on the parchment — having been shown more "
            "than words can carry, he sets it all aside and points once more to grace, "
            "his humbled face at peace, choosing grace over any boast. Ordinary-sized, "
            "one head, gaze warm and settled, not to the camera; nothing legible is "
            "written on the parchment and no ring of light rings his head."
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
# 138/155/166/171). Jesus is injected by the assembler on b12/b13 (jesus=True,
# ref=True). Only Jesus wears cream.
REFS = {
}
