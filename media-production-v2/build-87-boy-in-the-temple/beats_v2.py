#!/usr/bin/env python3
"""V2 beat map — row 87, build-87-boy-in-the-temple (Luke 2:41-52).

COVERAGE: 15 pictures over 86.0 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 2:41-52 KJV):
  v41-42 the family goes to Jerusalem EVERY YEAR at Passover; this
        year he is TWELVE.
  v43-45 returning, they suppose him "in the company" a day's journey,
        then turn back; v46 "after THREE DAYS they found him IN THE
        TEMPLE, sitting in the midst of the DOCTORS, both HEARING
        them, and ASKING THEM QUESTIONS."
  v47   "all that heard him were ASTONISHED at his understanding."
  v48   Mary: "Son, why hast thou thus dealt with us? behold, thy
        father and I have sought thee SORROWING."
  v49   "How is it that ye sought me? wist ye not that I must be about
        my FATHER'S BUSINESS?"
  v50   "they understood not the saying."
  v51-52 he went down with them to Nazareth, and was SUBJECT unto
        them; he "increased in wisdom and stature, and in favour with
        God and man."

JESUS AGE NOTE: Jesus is TWELVE — the adult JESUS LOCK v4 and face ref
do NOT apply; every beat runs jesus=False and the boy is carried by
the local BOY lock below (the look standard scaled to twelve; he alone
wears the undyed cream wool).

TIME OF DAY: bright spring daylight throughout — festival roads and
sunlit temple courts; the finding and dialogue in the temple porch's
clear morning light.

CONTENT-CARE: no flags. Mary's sorrow rendered with dignity — three
days of a mother's fear, never hysteria; the boy's answer painted as
genuine innocence, NEVER smugness (the narration insists).

CHANGING CONDITION (kept OUT of the locks): the family's state —
festival ease, then missing-child dread, then the found relief; and
the direction of travel — homeward, back, then homeward again,
together.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream, and in this row Jesus is the BOY below.
LOCKS = {
    "BOY": (
        "BOY LOCK: Jesus at twelve is the same boy in every shot — "
        "warm tan olive-brown skin, shoulder-length dark brown-black "
        "wavy hair, warm brown eyes, a boy's smooth face, in ONE "
        "plain undyed OFF-WHITE/CREAM wool robe (he alone wears "
        "cream). Bright, earnest, entirely without smugness. No "
        "ring of light, nothing outlining him."
    ),
    "MARY": (
        "MARY LOCK: Mary is the same woman in every shot — about "
        "thirty, a gentle worn face with warm brown eyes, dark hair "
        "under a DEEP INDIGO-BLUE veil, a plain DEEP INDIGO-BLUE "
        "dress (never cream, never white). Her fear and relief are "
        "a mother's, carried with dignity."
    ),
    "JOSEPH": (
        "JOSEPH LOCK: Joseph is the same man in every shot — about "
        "forty-five, a carpenter's broad hands, short dark beard "
        "going grey, sun-browned face, in a DARK RUSSET-BROWN robe "
        "with a CHARCOAL-GREY head cloth (never cream, never white)."
    ),
    "PORCH": (
        "PORCH LOCK: the temple teaching porch — a sunlit colonnade "
        "court off the temple's outer court: massive pale limestone "
        "columns, broad steps where circles of listeners sit, scroll "
        "chests and low benches for the teachers. The same columns "
        "and steps throughout."
    ),
    "DOCTORS": (
        "DOCTORS LOCK: the teachers of the law — old scholars in "
        "DEEP CHARCOAL, DARK SLATE-BLUE and DARK WINE robes with "
        "broad fringes and grey beards (never cream, never white); "
        "learned, grave, and genuinely astonished, never mocking."
    ),
    "ROAD": (
        "ROAD LOCK: the pilgrim road between Jerusalem and Galilee — "
        "a broad dusty highway through terraced hills, walked by "
        "strings of festival families with donkeys and bundles. The "
        "same road and hills throughout."
    ),
}

REF = True

# STALE-V1-FINAL fix (AUDIO-FIX 2026-08-06, Machine A): timeline 94.422s vs V1 mp4
# 93.000s (|Δ|=1.422s > 1.0 shortfall), so the packet-copy AUDIO LOCK refuses.
# Rebuild the track from this build's own 12 mp3 segments — nothing re-voiced, $0.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r087-b01", "out": "s01-every-year-family-went-to.jpeg", "seg": "n0a",
        "window": "0.28-6.87", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD", "MARY", "JOSEPH", "BOY"],
        "narration": (
            "Every year Jesus's family went to Jerusalem for the Passover. "
            "When he was twelve, they made the trip as usual."
        ),
        "must_show": "SCRIPTURE-EXACT: the annual pilgrimage — the family walking the crowded festival road among other pilgrim families, the boy between his parents, Jerusalem's hill far ahead.",
        "must_not_show": "no ring of light on anyone; the trip ORDINARY — one family among many, festival ease.",
        "scene": (
            "The spring road streams, the camera off the verge "
            "taking the festival flow in profile, with "
            "Passover families — donkeys and "
            "bundles, cousins calling between "
            "groups, dust golden in the "
            "morning light — and among them "
            "one family walks as usual: Joseph "
            "with the pack rope over his "
            "shoulder, Mary with the bread "
            "bag, and between them the twelve-"
            "year-old in his plain cream wool, "
            "keeping stride with his father "
            "and drinking the whole road in "
            "with bright brown eyes. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r087-b02", "out": "s02-on-the-way-home-they.jpeg", "seg": "n0b",
        "window": "7.52-10.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROAD", "MARY", "JOSEPH"],
        "narration": "On the way home, they realized he wasn't with them.",
        "must_show": "SCRIPTURE-EXACT: the realization — evening on the homeward road: Mary and Joseph moving urgently between pilgrim campfires and family groups, scanning; the boy nowhere.",
        "must_not_show": "no ring of light; the dread BEGINNING — urgency in the search of faces, panic not yet full.",
        "scene": (
            "At the first evening camp the "
            "counting comes up wrong: Mary "
            "moving quick between the pilgrim "
            "fires with her veil pressed to "
            "her mouth, checking each circle "
            "of cousins' children, Joseph "
            "striding the road's edge scanning "
            "back along the darkening highway "
            "— every family has its boy except "
            "theirs, and the easy festival "
            "evening curdles around two "
            "parents doing arithmetic no "
            "parent wants. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r087-b03", "out": "s03-they-turned-back-searching-for.jpeg", "seg": "n1a + n1b",
        "window": "10.73-18.48", "wide": True, "jesus": False, "ref": False,
        "locks": ["PORCH", "BOY", "DOCTORS", "MARY", "JOSEPH"],
        "narration": (
            "They turned back, searching for three days. And they found him "
            "in the temple, sitting among the teachers, listening,"
        ),
        "must_show": "SCRIPTURE-EXACT: the finding (v46) — the parents arriving at the porch's edge, haggard, and before them: the boy seated IN THE MIDST of the circle of grey-bearded doctors, listening.",
        "must_not_show": "no ring of light; the boy IN THE MIDST — inside the scholars' circle, not at its edge; the parents' three days visible on their faces.",
        "scene": (
            "Three days end at a colonnade, the camera behind the "
            "arriving parents' shoulders toward the seated circle: "
            "Mary and Joseph coming up the "
            "temple steps hollow-eyed and "
            "road-worn — and stopping dead, "
            "because there he is: the boy in "
            "cream wool seated in the very "
            "midst of a circle of grey-bearded "
            "doctors on their benches, head "
            "tilted, listening to an old man's "
            "point with his whole body — safe, "
            "absorbed, and completely at home "
            "in the one place they looked "
            "last. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r087-b04", "out": "s04-and-asking-questions-that-amazed.jpeg", "seg": "n1c + n2",
        "window": "19.15-23.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["PORCH", "BOY", "DOCTORS"],
        "narration": (
            "and asking questions that amazed everyone. His mother was the "
            "one who spoke."
        ),
        "must_show": "SCRIPTURE-EXACT: the astonishment (v47) — the boy mid-question, hand raised in an earnest point; the old scholars' faces around him openly amazed, one leaning in, one stroking his beard stunned.",
        "must_not_show": "no ring of light; the amazement GENUINE on the doctors — respect, not amusement; the boy earnest, never showing off.",
        "scene": (
            "Close in the circle: the boy "
            "mid-question with one hand raised "
            "in an earnest open point, brown "
            "eyes alight with the honest want "
            "of the answer — and around him "
            "the old faces coming undone with "
            "astonishment: one doctor leaning "
            "halfway off his bench, another's "
            "hand stopped in his grey beard, a "
            "third looking at his colleagues "
            "to confirm they heard it too — "
            "a twelve-year-old asking the "
            "questions they saved for each "
            "other. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r087-b05", "out": "s05-relieved-and-frightened-and-hurt.jpeg", "seg": "n2",
        "window": "24.21-27.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": "Relieved, and frightened, and hurt, Mary said this:",
        "must_show": "the three feelings — close on Mary's face at the circle's edge: relief, fear and hurt all present at once as she finds her voice.",
        "must_not_show": "no ring of light; ALL THREE legible — wet-eyed relief, the residue of dread, the sting of hurt; dignity throughout.",
        "scene": (
            "Close on Mary at the circle's "
            "edge as her voice comes back: "
            "three days written all over her "
            "face at once — the flooding "
            "relief that loosens her knees, "
            "the fear still cold at the back "
            "of her eyes, and over both the "
            "plain human hurt of a mother who "
            "was not spared — her hand "
            "pressed flat to her chest, "
            "holding all three in place long "
            "enough to speak. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r087-b06", "out": "s06-son-why-hast-thou-thus.jpeg", "seg": "w48",
        "window": "27.93-34.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["PORCH", "BOY", "MARY", "JOSEPH", "DOCTORS"],
        "narration": (
            "Son, why hast thou thus dealt with us? behold, thy father and I "
            "have sought thee sorrowing."
        ),
        "must_show": "SCRIPTURE-EXACT: the words — Mary bent to the boy in the hushed circle, hands on his shoulders, the question pouring out; Joseph behind her, the doctors gone quiet.",
        "must_not_show": "no ring of light; NO scolding posture — the hands on his shoulders holding, not shaking; sorrow, not anger.",
        "scene": (
            "Mary crosses the circle and "
            "takes her son by both shoulders "
            "— not shaking, holding, the way "
            "you grip what you thought was "
            "lost — SON, WHY HAST THOU THUS "
            "DEALT WITH US — the words "
            "spilling with three days behind "
            "them while Joseph stands close "
            "at her back and the ring of "
            "doctors goes respectfully still "
            "around a scene older than all "
            "their scrolls: a found child, "
            "and a mother's spent heart "
            "talking. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r087-b07", "out": "s07-she-said-your-father-and.jpeg", "seg": "n2b",
        "window": "36.26-40.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY", "JOSEPH"],
        "narration": (
            "she said. Your father and I have been looking for you, sick "
            "with worry."
        ),
        "must_show": "the cost close — Mary's and Joseph's faces together: the sleepless grime of three searching days; worry made physical on both.",
        "must_not_show": "no ring of light; the exhaustion HONEST — red-rimmed eyes, road dust, no tidying.",
        "scene": (
            "Close on the two faces the "
            "search spent: Mary's eyes red-"
            "rimmed above cheeks hollowed by "
            "three days of not eating "
            "properly, Joseph's jaw rough "
            "with unshaved grey, road dust in "
            "the creases of both — the plain "
            "physical bill of looking for one "
            "boy through a festival city of "
            "thousands, presented without a "
            "word by the faces themselves. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r087-b08", "out": "s08-listen-to-the-word-luke.jpeg", "seg": "n2b",
        "window": "40.76-45.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": "Listen to the word Luke gives her — sorrowing. Not annoyed.",
        "must_show": "the word dwelt on — Mary's face held close and still: sorrow's depth distinguished from irritation; grief that assumed the worst.",
        "must_not_show": "no ring of light; NOTHING of the annoyed parent in the face — the deeper thing only.",
        "scene": (
            "The frame holds Mary's face and "
            "lets the word prove itself: "
            "nothing in it of the parent "
            "merely put out — no pursed "
            "irritation, no tapping-foot anger "
            "— only the deep-water grief of a "
            "mother who spent three nights "
            "trading terrible pictures with "
            "the dark, aged by them, standing "
            "now in the sunlight with sorrow "
            "still draining slowly out of her "
            "features. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r087-b09", "out": "s09-grieving-three-days-of-a.jpeg", "seg": "n2b",
        "window": "45.56-52.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["PORCH", "BOY", "MARY"],
        "narration": (
            "Grieving. Three days of a mother assuming the worst. And he "
            "answered her with a question of his own."
        ),
        "must_show": "the turn to his answer — the boy looking up at his mother in the quiet circle, face open and gentle, his own question arriving; the exchange at its hinge.",
        "must_not_show": "no ring of light; the boy's face WARM toward her — no defiance, no smart-aleck tilt.",
        "scene": (
            "In the hushed circle the boy "
            "looks up into his mother's spent "
            "face — and there is nothing in "
            "his own but warmth and a genuine, "
            "gentle puzzlement, the look of a "
            "child who loves her completely "
            "and truly cannot find the "
            "problem — the hinge of the whole "
            "scene turning quietly as his own "
            "question gathers behind the "
            "bright brown eyes. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r087-b10", "out": "s10-how-is-it-that-ye.jpeg", "seg": "j1",
        "window": "53.12-58.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["PORCH", "BOY", "MARY", "JOSEPH"],
        "narration": (
            "How is it that ye sought me? wist ye not that I must be about "
            "my Father's business?"
        ),
        "must_show": "SCRIPTURE-EXACT: the answer — the boy speaking it earnestly, one small hand opening toward the temple courts around them; MY FATHER'S business, said in the Father's house.",
        "must_not_show": "no ring of light; the gesture toward the TEMPLE ITSELF — the courts as the self-evident address; innocence absolute.",
        "scene": (
            "The boy answers with his whole "
            "honest bafflement: HOW IS IT THAT "
            "YE SOUGHT ME — and his small hand "
            "opens outward at the sunlit "
            "courts and columns all around "
            "them, presenting the temple the "
            "way a child presents his own "
            "front door — WIST YE NOT — the "
            "words earnest and unanswerable, "
            "a twelve-year-old standing in "
            "his Father's house, mildly amazed "
            "that anyone checked anywhere "
            "else first. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r087-b11", "out": "s11-why-were-you-out-looking.jpeg", "seg": "n2c",
        "window": "60.36-62.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOY"],
        "narration": "Why were you out looking for me? he said.",
        "must_show": "the question's innocence — close on the boy's open face: honest asking, zero challenge; a child's real question.",
        "must_not_show": "no ring of light; NO eyebrow of defiance, no smirk — pure inquiry.",
        "scene": (
            "Close on the boy's face in the "
            "clear porch light: brows lifted "
            "in plain honest asking, the "
            "brown eyes going softly between "
            "his mother's and his father's, "
            "not one grain of challenge "
            "anywhere in the young features — "
            "a question asked the way "
            "children ask why the sky is "
            "blue: because he actually wants "
            "to understand how they lost "
            "track of the obvious. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r087-b12", "out": "s12-you-know-i-had-to.jpeg", "seg": "n2c",
        "window": "62.68-69.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["PORCH", "BOY"],
        "narration": (
            "Didn't you know I had to be in my Father's house, about my "
            "Father's work? He was twelve years old."
        ),
        "must_show": "the boy in the Father's house — the small cream-robed figure at home amid the great columns and courts; twelve years old, and belonging visibly to the place.",
        "must_not_show": "no ring of light; the SCALE the picture — a boy small under massive stone, and utterly unintimidated.",
        "scene": (
            "The wide porch gives the sentence "
            "its picture: the great pale "
            "columns rising storey over storey "
            "into the light, courts opening "
            "beyond courts — and small in the "
            "middle of all that majesty, the "
            "boy in his plain cream wool, "
            "standing where he belongs with "
            "the unforced ease of a son in "
            "his father's workshop — twelve "
            "years old, dwarfed by the stone "
            "and at home over all of it. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r087-b13", "out": "s13-he-was-not-being-smart.jpeg", "seg": "n2c",
        "window": "69.24-75.54", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOY", "MARY"],
        "narration": (
            "He was not being smart with his mother. He genuinely could not "
            "imagine where else they thought he would be."
        ),
        "must_show": "the sincerity sealed — the boy's hand slipping into his mother's, face tipped up to hers, guileless; love and puzzlement without a drop of sass.",
        "must_not_show": "no ring of light; the touch TENDER — the answer ends in affection, not victory.",
        "scene": (
            "The exchange ends the way it was "
            "always going to: the boy's hand "
            "slipping small and certain into "
            "his mother's, his face tipped up "
            "to hers with open guileless "
            "love, the puzzlement already "
            "dissolving into gladness at "
            "simply being found by her — no "
            "point scored, no distance taken, "
            "a son folding himself back into "
            "his mother's keeping without "
            "leaving his Father's. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r087-b14", "out": "s14-they-fully-understand.jpeg", "seg": "n3",
        "window": "76.23-77.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY", "JOSEPH"],
        "narration": "They didn't fully understand.",
        "must_show": "SCRIPTURE-EXACT: understood not (v50) — Mary's and Joseph's faces exchanging a look over the boy's head: love intact, comprehension incomplete.",
        "must_not_show": "no ring of light; the not-understanding GENTLE — a shared glance of parents out of their depth, still all in.",
        "scene": (
            "Over the boy's dark head the two "
            "parents trade one long look: "
            "Joseph's brows asking Mary "
            "whether she followed that, "
            "Mary's small headshake admitting "
            "she didn't either — two good "
            "plain people holding between "
            "them a child whose sentences "
            "keep opening onto rooms they "
            "cannot see into, and holding him "
            "anyway, with everything they "
            "have. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r087-b15", "out": "s15-but-he-went-home-with.jpeg", "seg": "n3",
        "window": "77.53-85.61", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD", "BOY", "MARY", "JOSEPH"],
        "narration": (
            "But he went home with them and obeyed them — and he kept "
            "growing in wisdom, in stature, and in favor with God and "
            "people."
        ),
        "must_show": "SCRIPTURE-EXACT: subject unto them (v51) — the closing image: the three walking the homeward road together in warm light, the boy between his parents, content; obedience and growing, both visible.",
        "must_not_show": "no ring of light; the walk HOMEWARD and happy — the family whole, the boy willingly in step.",
        "scene": (
            "The closing frame takes the road home, the camera "
            "behind the three as they walk away down it: "
            "home: the three of them small on "
            "the broad highway north in the "
            "warm late light — Joseph's hand "
            "resting easy on the boy's "
            "shoulder, Mary's veil turned to "
            "her son's chatter, the boy in "
            "cream keeping step between them "
            "by his own glad choice — the one "
            "who amazed the doctors walking "
            "obediently home to a carpenter's "
            "house, with all the growing "
            "still ahead of him. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "ROAD": "PLACE-REF/road.jpeg",  # build-79-the-seventy-sent v2-r079-b08
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "BOY": "CAST-REF-V2/boy.jpeg",
    "JOSEPH": "CAST-REF-V2/joseph.jpeg",
}
