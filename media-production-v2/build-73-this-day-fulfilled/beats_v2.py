#!/usr/bin/env python3
"""V2 beat map — row 73, build-73-this-day-fulfilled (Luke 4:16-21).

COVERAGE: 17 pictures over 102.6 s = 6.0 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 4:16-21 KJV):
  v16   "he came to NAZARETH, where he had been BROUGHT UP: and, AS HIS
        CUSTOM WAS, he went into the synagogue on the sabbath day, and
        stood up for to read" — the hometown room: small, familiar,
        full of faces that watched him grow; his entering is routine,
        which is the scene's whole tension-spring.
  v17   "there was DELIVERED unto him the book of the prophet ESAIAS.
        And when he had OPENED THE BOOK, he FOUND THE PLACE" — the
        scroll's handing, unrolling and deliberate finding are each
        beats: liturgy in real hands.
  v18-19 the Isaiah reading (Spirit... anointed... poor... broken-
        hearted... captives... blind... bruised... acceptable year) —
        read STANDING, aloud, over the hometown's bowed heads.
  v20   "he CLOSED the book, and he gave it again to the minister, and
        SAT DOWN. And the EYES of all them that were in the synagogue
        were FASTENED ON HIM." — the sitting (the teacher's posture)
        and the fastened eyes are the row's held breath.
  v21   "THIS DAY is this scripture fulfilled in your ears." — eight
        words; the centuries' promise located in the room, TODAY.

TIME OF DAY: one sabbath morning throughout — clear light through the
synagogue's small high windows; the closing TODAY beat in the same
plain daylight, deliberately ordinary.

CONTENT-CARE: no flags. The congregation's later anger (v28-29) is NOT
in this narration — the row ends inside the held breath and the
declaration; faces astonished, not yet hostile.

CHANGING CONDITION (kept OUT of the locks): the scroll — delivered
rolled, opened, the place found, read, closed, returned; and the room's
attention: routine, then fastened, then breathless.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "SYNAGOGUE": (
        "NAZARETH SYNAGOGUE LOCK: a small hometown synagogue — plain "
        "plastered walls, two rows of stone benches around a central "
        "reading platform with a wooden lectern, a carved wooden ark "
        "for the scrolls at the east wall, and small high windows "
        "throwing clear morning light in angled shafts. The same "
        "benches, platform, ark and windows throughout."
    ),
    "TOWNSFOLK": (
        "CONGREGATION LOCK: the hometown faces — Nazareth's farmers, "
        "builders, mothers, elders and children in their sabbath best "
        "of SATURATED DEEP earth colours: dark browns, deep russet, "
        "dark olive, dusty indigo, faded plum (never cream, never "
        "white; only Jesus wears cream). Among them one white-bearded "
        "ELDER on the front bench and the MINISTER (attendant) in a "
        "DARK PLUM robe who keeps the scrolls. Faces shown clearly — "
        "people who watched this reader grow up on their street."
    ),
    "SCROLL": (
        "ISAIAH SCROLL LOCK: the book of Esaias — a great old scroll "
        "on two dark wooden rollers, its parchment gone honey-amber "
        "with age, dense columns of hand-lettered script, kept in a "
        "faded linen wrapper in the ark. The same rollers and amber "
        "parchment in every scroll beat."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r073-b01", "out": "s01-he-came-back-to-nazareth.jpeg", "seg": "n0",
        "window": "0.28-6.74", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE", "TOWNSFOLK"],
        "narration": (
            "He came back to Nazareth — the town that raised him — and on the "
            "Sabbath he walked into the synagogue like he always had."
        ),
        "must_show": "SCRIPTURE-EXACT: the customary entering — Jesus stepping through the synagogue door among arriving neighbours, greeted as the hometown boy; routine wearing its last morning.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the familiarity total — nods, a shoulder-clasp; nobody expecting anything.",
        "scene": (
            "Through the synagogue's low door, the camera at the "
            "side aisle taking the entry in profile, Jesus "
            "enters with the sabbath-morning drift of "
            "his own town — an old builder clasping "
            "his shoulder in passing, a mother "
            "steering her children to the benches, "
            "the white-bearded elder nodding from the "
            "front row — the carpenter's son arriving "
            "the way he has arrived his whole life, "
            "into a room that thinks it knows "
            "everything about him. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r073-b02", "out": "s02-and-there-was-delivered-unto.jpeg", "seg": "s17",
        "window": "7.39-10.70", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE", "TOWNSFOLK", "SCROLL"],
        "narration": "And there was delivered unto him the book of the prophet Esaias.",
        "must_show": "SCRIPTURE-EXACT: the delivering — the plum-robed minister placing the wrapped Isaiah scroll into Jesus's hands at the platform; liturgy's ordinary handover.",
        "must_not_show": "no halo, glare or rim-light; the handover routine and reverent — a scroll passed as it is every sabbath.",
        "scene": (
            "At the central platform the plum-robed "
            "minister draws the great scroll from its "
            "faded linen wrapper and places it into "
            "Jesus's waiting hands — the old wooden "
            "rollers settling into his palms with the "
            "weight of centuries, the congregation "
            "settling onto their benches around the "
            "small routine of it — the most ordinary "
            "handover in the sabbath's order, "
            "occurring for the last ordinary time. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r073-b03", "out": "s03-and-when-he-had-opened.jpeg", "seg": "s17",
        "window": "11.19-14.64", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SCROLL"],
        "narration": (
            "And when he had opened the book, he found the place where it was "
            "written,"
        ),
        "must_show": "SCRIPTURE-EXACT: the finding — close on Jesus's hands working the rollers, the amber columns travelling, his eyes searching down the script for one place.",
        "must_not_show": "no halo, glare or rim-light; the search deliberate — a reader who knows exactly what he is looking for.",
        "scene": (
            "Close over the lectern: Jesus's carpenter "
            "hands work the two dark rollers in "
            "opposite turns, the honey-amber parchment "
            "travelling between them column by dense "
            "column — and his eyes run the script with "
            "a purpose the room cannot yet feel, "
            "passing prophecy after prophecy, hunting "
            "one particular place the way a man walks "
            "to one particular door in his own house. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r073-b04", "out": "s04-he-found-the-place-and.jpeg", "seg": "n1",
        "window": "17.92-20.87", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SCROLL"],
        "narration": "He found the place, and read it out loud.",
        "must_show": "the place found — Jesus's finger coming to rest at one column's head, the search ended; the reading's first breath being taken.",
        "must_not_show": "no halo, glare or rim-light; the finger's rest the beat — arrival at the appointed line.",
        "scene": (
            "The rollers still: Jesus's forefinger "
            "comes to rest at the head of one amber "
            "column — the place, found — and above the "
            "settled hand his chest fills for the "
            "reading's first breath, his eyes already "
            "holding the opening words — seven "
            "centuries of waiting ink about to be "
            "read aloud by the only voice with the "
            "right to add anything to it. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r073-b05", "out": "s05-they-handed-him-the-scroll.jpeg", "seg": "n1",
        "window": "16.09-17.92", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SCROLL", "SYNAGOGUE"],
        "narration": "They handed him the scroll of Isaiah.",
        "must_show": "the scroll itself honoured — close on the great amber scroll open across the lectern in the window light; the prophet's book at its full breadth.",
        "must_not_show": "no halo, glare or rim-light; the scroll the frame's subject — age, weight, authority in parchment.",
        "scene": (
            "The great scroll lies open across the "
            "worn lectern in a shaft of window light: "
            "honey-amber parchment stretched between "
            "its dark rollers, dense hand-lettered "
            "columns marching away to both edges, the "
            "surface crazed fine with seven hundred "
            "years of sabbaths — the prophet Esaias "
            "at full breadth, waiting under two "
            "steady hands for the morning that every "
            "line of him was written toward. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r073-b06", "out": "s06-the-spirit-of-the-lord.jpeg", "seg": "j1",
        "window": "21.51-42.83", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE", "TOWNSFOLK", "SCROLL"],
        "narration": (
            "The Spirit of the Lord is upon me, because he hath anointed me to "
            "preach the gospel to the poor; he hath sent me to heal the "
            "brokenhearted, to preach deliverance to the captives, and "
            "recovering of sight to the blind, to set at liberty them that are "
            "bruised, to preach the acceptable year of the Lord."
        ),
        "must_show": "SCRIPTURE-EXACT: the reading — Jesus STANDING at the lectern reading the great passage over the congregation: the room in sabbath stillness, the words moving over bowed and lifted heads.",
        "must_not_show": "no halo, glare or rim-light; the reading's power carried by stillness and the listeners' faces — liturgy, not performance.",
        "scene": (
            "Standing at the lectern, the camera behind the seated "
            "congregation's shoulders, in the angled "
            "morning shafts Jesus reads the great "
            "passage over his hometown — the words "
            "moving through the small plastered room "
            "across bowed heads and lifted faces: the "
            "old builder's eyes closing at 'the "
            "poor', a widow's hand rising to her "
            "mouth at 'brokenhearted', the elder "
            "nodding slow on the front bench — "
            "Isaiah's whole freight delivered in the "
            "reader's calm carrying voice, to people "
            "who have heard it read all their lives "
            "and never once like this. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r073-b07", "out": "s07-and-he-closed-the-book.jpeg", "seg": "s20",
        "window": "65.37-69.13", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE", "TOWNSFOLK", "SCROLL"],
        "narration": (
            "And he closed the book, and he gave it again to the minister, and "
            "sat down."
        ),
        "must_show": "SCRIPTURE-EXACT: the three motions — the scroll rolled closed, returned to the minister's hands, and Jesus SITTING DOWN on the platform bench; the teacher's posture taken.",
        "must_not_show": "no halo, glare or rim-light; the sitting the signal — in that room, sitting means the exposition is coming.",
        "scene": (
            "Three quiet motions in sequence hold the "
            "room: the great scroll rolled closed "
            "between its rollers, passed back into "
            "the plum-robed minister's careful hands "
            "— and then Jesus sits down on the "
            "platform bench, robes settling, hands at "
            "rest on his knees — the posture every "
            "synagogue knows: the reading is done, "
            "and the teaching is about to begin. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r073-b08", "out": "s08-and-the-room-held-its.jpeg", "seg": "n2",
        "window": "83.39-85.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["SYNAGOGUE", "TOWNSFOLK"],
        "narration": "And the room held its breath.",
        "must_show": "the held breath — the congregation wide: every body leaned fractionally forward, every face fixed one direction, the stillness total.",
        "must_not_show": "no halo, glare or rim-light; the lean the measure — a room's worth of suspended breathing.",
        "scene": (
            "The small room holds one breath "
            "together: every body on the stone "
            "benches leaned a fraction forward, a "
            "child gone still against his mother's "
            "side, the old builder's hands stopped "
            "mid-fold, dust motes hanging unhurried "
            "in the window shafts — a hometown "
            "congregation suspended between a "
            "reading they know by heart and whatever "
            "the carpenter's son is about to add to "
            "it. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r073-b09", "out": "s09-the-spirit-of-the-lord.jpeg", "seg": "n1b",
        "window": "44.36-60.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWNSFOLK"],
        "narration": (
            "The Spirit of the Lord is on me, he read, because he anointed me — "
            "to bring good news to the poor, to bind up the broken-hearted, to "
            "tell prisoners they are free and the blind that they will see, to "
            "lift up the crushed."
        ),
        "must_show": "the words landing severally — close along the benches: each clause finding its addressee — the poor man, the grieving widow, the burdened; Isaiah's list, seated in one room.",
        "must_not_show": "no halo, glare or rim-light; each face's need particular — the passage as a roll call of this town.",
        "scene": (
            "Close along the stone benches the "
            "clauses find their people: the "
            "day-labourer's patched knees under "
            "'good news to the poor', the young "
            "widow's black shawl at 'broken-"
            "hearted', an old man's clouded eyes "
            "lifting at 'the blind', a debt-worn "
            "farmer's crushed shoulders straightening "
            "a degree at 'the bruised' — seven "
            "centuries of promise reading out, name "
            "by unspoken name, down two rows of "
            "hometown benches. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r073-b10", "out": "s10-not-someday.jpeg", "seg": "n3",
        "window": "99.53-100.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["SYNAGOGUE"],
        "narration": "Not someday.",
        "must_show": "the tense collapsing — a close still: the morning's plain light lying across the platform's worn floorboards; the present tense as a place.",
        "must_not_show": "no halo, glare or rim-light; the ordinariness of NOW — this floor, this light, this morning.",
        "scene": (
            "A close still at the platform's edge: "
            "the morning's plain window light lying "
            "in its angled shaft across worn "
            "floorboards — the grain scrubbed pale "
            "by generations of sabbath feet, one "
            "knot-hole, the lectern's shadow — "
            "nothing in the frame but an ordinary "
            "now: this floor, this light, this "
            "particular unrepeatable morning, which "
            "is exactly where the promise just "
            "moved in. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r073-b11", "out": "s11-every-line-of-it-was.jpeg", "seg": "n1b",
        "window": "60.14-64.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["SCROLL"],
        "narration": (
            "Every line of it was a promise about somebody who had not come "
            "yet."
        ),
        "must_show": "the future-tense scroll — close on the amber columns themselves: prophecy's dense waiting script; seven hundred years of not-yet in ink.",
        "must_not_show": "no halo, glare or rim-light; ancient script only — the waiting visible as age.",
        "scene": (
            "Close on the open scroll's amber "
            "surface: the dense hand-lettered "
            "columns marching their centuries — ink "
            "gone brown with age, the parchment's "
            "fine crazing like drought-ground, "
            "generations of readers' thumb-wear soft "
            "at the column heads — seven hundred "
            "years of somebody-who-had-not-come-yet, "
            "held in patient ink that finished "
            "waiting this morning. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r073-b12", "out": "s12-and-the-eyes-of-all.jpeg", "seg": "s20",
        "window": "69.13-73.59", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE", "TOWNSFOLK"],
        "narration": (
            "And the eyes of all them that were in the synagogue were fastened "
            "on him."
        ),
        "must_show": "SCRIPTURE-EXACT: the fastened eyes — from behind the seated Jesus: the whole room's faces aimed at him in one converging gaze; the verse as composition.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the convergence total — every sight-line in the room ending at one seated figure.",
        "scene": (
            "The camera stands just behind the seated Jesus's "
            "shoulder the verse composes itself: the "
            "whole small room's faces aimed at him "
            "in one converging fan — the elder's "
            "deep-set stare, the builder's open "
            "mouth, the widow's wet fixed eyes, the "
            "children caught still as birds — every "
            "sight-line in Nazareth's synagogue "
            "fastened on one seated hometown man, "
            "waiting for his first word. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r073-b13", "out": "s13-then-he-rolled-the-scroll.jpeg", "seg": "n2",
        "window": "74.99-78.15", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SCROLL"],
        "narration": "Then he rolled the scroll up, handed it back, and sat down.",
        "must_show": "the deliberateness — close on the hands rolling the scroll closed: unhurried, exact; the calm before eight words.",
        "must_not_show": "no halo, glare or rim-light; the rolling's patience the tension — liturgy performed while a room holds its breath.",
        "scene": (
            "Close on the hands at the lectern: the "
            "great scroll rolling closed between "
            "them turn by unhurried turn, the amber "
            "columns disappearing into themselves, "
            "the linen wrapper drawn over and "
            "smoothed — carpenter's patience applied "
            "to parchment while a whole room's held "
            "breath leans on the back of his neck — "
            "the calm of a man in no hurry because "
            "the moment cannot start without him. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r073-b14", "out": "s14-every-eye-in-the-room.jpeg", "seg": "n2",
        "window": "78.15-83.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWNSFOLK"],
        "narration": (
            "Every eye in the room was fixed on him — this was the boy who grew "
            "up on their street."
        ),
        "must_show": "the hometown knowing — close on two front-bench faces: the elder who taught him letters, the builder who knew his father; recognition complicating awe.",
        "must_not_show": "no halo, glare or rim-light; the familiarity the friction — faces holding the boy and the reader in one look.",
        "scene": (
            "Close on the front bench: the white-"
            "bearded elder who heard this reader's "
            "boyhood recitations, and beside him the "
            "old builder who squared timber with "
            "the father — two faces working the "
            "impossible arithmetic of the morning: "
            "the boy from the street two doors down, "
            "and the voice that just read Isaiah "
            "like its owner — memory and awe "
            "grinding gears behind four fixed eyes. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r073-b15", "out": "s15-this-day-is-this-scripture.jpeg", "seg": "j2",
        "window": "86.02-89.09", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE", "TOWNSFOLK"],
        "narration": "This day is this scripture fulfilled in your ears.",
        "must_show": "SCRIPTURE-EXACT: THE declaration — Jesus seated, calm, the eight words going out into the fastened silence; the room's stillness at its absolute pitch.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the words at conversational volume — the largest claim in the town's history, made quietly, sitting down.",
        "scene": (
            "Seated on the platform bench in the "
            "plain morning light Jesus gives the "
            "room its eight words — quietly, at the "
            "volume of a man passing bread — and the "
            "fastened silence takes them whole: the "
            "elder's lips parting, the widow's hand "
            "closing on her shawl, the builder gone "
            "grey-still — seven hundred years "
            "arriving at their address in one "
            "sentence, delivered sitting down by the "
            "boy from two streets over. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r073-b16", "out": "s16-the-promise-israel-had-waited.jpeg", "seg": "n3",
        "window": "90.54-99.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE"],
        "narration": (
            "The promise Israel had waited on for centuries — the healing, the "
            "freedom, the good news for the poor — he said it was standing "
            "right in front of them."
        ),
        "must_show": "the standing-right-there — close on Jesus's seated presence in the plain light: the promise embodied, ordinary and present; carpenter's hands at rest on knees.",
        "must_not_show": "no halo, glare or rim-light; the embodiment carried by plainness — everything promised, sitting on a bench.",
        "scene": (
            "Close on the seated figure in the window "
            "shaft's plain light: the travel-worn "
            "cream robe, the carpenter's hands at "
            "rest on the knees, the warm familiar "
            "hometown face — nothing added, nothing "
            "shining — centuries of healing and "
            "freedom and good news for the poor, "
            "present in the room at the size of one "
            "seated man, close enough for the front "
            "bench to touch. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r073-b17", "out": "s17-today.jpeg", "seg": "n3",
        "window": "100.94-102.24", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE", "TOWNSFOLK"],
        "narration": "Today.",
        "must_show": "the closing image — the whole room in the one word's after-silence: the seated Jesus, the fastened faces, the morning light; TODAY hanging in ordinary air.",
        "must_not_show": "no halo, glare or rim-light; the word's weight carried by the room's total stillness in plain daylight.",
        "scene": (
            "The whole small room holds the one "
            "word's after-silence: Jesus seated calm "
            "on the platform, the congregation's "
            "faces fastened and unbreathing down "
            "both benches, the angled morning shafts "
            "standing in the quiet air — Nazareth's "
            "synagogue on an ordinary sabbath, "
            "holding in ordinary daylight the least "
            "ordinary word ever said in it: today. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
# SYNAGOGUE wiring REMOVED by the author 2026-08-05: the stash matched
# build-05's CAPERNAUM hall by token name, but this is the NAZARETH
# synagogue — Jesus's hometown, a different building (rows 52/55 rightly
# share Capernaum's; this row must not). Promote-first from b01, and the
# approved Nazareth hall must seed row 129 (nazareth-only-a-few).
PLACE_REFS = {}
# === end PLACE-PLATES ===
