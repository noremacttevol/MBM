#!/usr/bin/env python3
"""V2 beat map — row 89, build-89-last-supper (Luke 22:14-20; Mark 14:26).

COVERAGE: 16 pictures over 94.6 s = 5.9 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 22:14-20 KJV):
  v14   "when the hour was come, he SAT DOWN, and the TWELVE APOSTLES
        with him." — one table, an upper room (v12: "a large upper
        room furnished"), evening.
  v15   "With DESIRE I have desired to eat this passover with you
        BEFORE I SUFFER." — longing said out loud.
  v19   "he took BREAD, and GAVE THANKS, and BRAKE it, and GAVE unto
        them, saying, This is my body which is given for you: this do
        in REMEMBRANCE of me."
  v20   "Likewise also THE CUP after supper, saying, This cup is the
        NEW TESTAMENT in my blood, which is shed for you."
  v18   "I will not drink of the fruit of the vine, until the kingdom
        of God shall come." — the next-meal promise.
  Mark 14:26 "when they had SUNG AN HYMN, they went out into the mount
        of Olives." — they leave singing, into the night.

TIME OF DAY: lamplit NIGHT throughout — the Passover evening in the
upper room; the departure beat under the deep night sky. (Correct
story darkness, not the row-11 defect.)

CONTENT-CARE: no flags. The coming suffering is carried in tone and
steadiness only — no morbid imagery; Judas and the betrayal are NOT in
this narration and are not depicted; the mood is love, gift, and
promise.

CHANGING CONDITION (kept OUT of the locks): the meal — laid, eaten,
finished; the bread — whole, broken, given; the cup — poured, lifted,
passed; the room — full of friends, then left quiet with the bread
and cup remaining.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream. PETER and JOHN come from the shared CAST_LOCKS.
LOCKS = {
    "ROOM": (
        "ROOM LOCK: the upper room — a large furnished chamber up an "
        "outside stair: a LOW U-SHAPED TABLE with cushions where "
        "diners recline, clay oil lamps on the table and in wall "
        "niches, plastered walls, one shuttered window open on the "
        "night. The same table, lamps and walls throughout."
    ),
    "MEAL": (
        "MEAL LOCK: the Passover table — flat rounds of unleavened "
        "bread, a large two-handled CLAY CUP of dark wine, bowls of "
        "bitter herbs and fruit paste, a roasted portion; simple "
        "earthenware, nothing gilded."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r089-b01", "out": "s01-the-passover-had-come.jpeg", "seg": "n0a",
        "window": "0.40-2.07", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM", "MEAL"],
        "narration": "The Passover had come.",
        "must_show": "the eve — the upper room ready in lamplight: the low table laid with the Passover meal, cushions set, the night at the window; the hour arrived.",
        "must_not_show": "no halo, glare or rim-light; the room READY and empty of diners — the laid table waiting.",
        "scene": (
            "Up its outside stair the upper "
            "room stands ready in the "
            "lamplight: the low U-shaped "
            "table laid end to end with the "
            "old meal — flat bread in its "
            "rounds, the great clay cup "
            "filled dark, the bitter herbs "
            "in their bowls — cushions "
            "plumped and waiting, the little "
            "flames steady in their niches, "
            "and through the one open "
            "shutter the Passover night "
            "itself, arrived on schedule "
            "over the city. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r089-b02", "out": "s02-jesus-gathered-his-closest-friends.jpeg", "seg": "n0b",
        "window": "3.75-9.88", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "MEAL", "PETER", "JOHN"],
        "narration": (
            "Jesus gathered his closest friends around one table in an upper "
            "room, knowing the night would change everything."
        ),
        "must_show": "SCRIPTURE-EXACT: sat down with the twelve — the table ringed full: Jesus at its centre among his reclining friends, Peter and John near him; warmth over an undertone of weight.",
        "must_not_show": "no halo, glare or rim-light; NO empty Judas-seat drama — the betrayal is not this row's subject; the ring complete and warm.",
        "scene": (
            "The room fills, the camera at the wall behind the "
            "near couches' shoulders, with the people "
            "he chose: the table's ring "
            "complete in the lamplight, "
            "friends reclining shoulder to "
            "shoulder — Peter's broad frame "
            "close at one side, John young "
            "and attentive at the other — "
            "talk and passing bowls and the "
            "ease of men who have eaten a "
            "hundred roads together — and at "
            "the centre Jesus, warm among "
            "them, carrying alone the "
            "knowledge of what the night "
            "holds and choosing, first, this. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r089-b03", "out": "s03-with-desire-i-have-desired.jpeg", "seg": "jv15",
        "window": "11.54-16.42", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM"],
        "narration": (
            "With desire I have desired to eat this passover with you before "
            "I suffer."
        ),
        "must_show": "SCRIPTURE-EXACT: the longing spoken — close on Jesus saying it to the faces around him: open wanting in his face, the word SUFFER said steadily; love and weight in one sentence.",
        "must_not_show": "no halo, glare or rim-light; NO morbid imagery — the suffering only a word on a steady mouth.",
        "scene": (
            "Close on Jesus as he says the "
            "thing teachers do not usually "
            "admit: WITH DESIRE I HAVE "
            "DESIRED — the wanting open and "
            "unashamed in the warm brown "
            "eyes as they travel the "
            "lamplit faces — this meal, "
            "with these people, wanted "
            "badly — and the last word, "
            "BEFORE I SUFFER, laid down "
            "steady as a stone in a stream, "
            "grief and love sharing one "
            "breath without spoiling it. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r089-b04", "out": "s04-i-have-wanted-this-meal.jpeg", "seg": "n1",
        "window": "18.19-24.15", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "PETER", "JOHN"],
        "narration": (
            "I have wanted this meal with you, he told them — wanted it "
            "badly — before the hard thing happens."
        ),
        "must_show": "the words landing — the near faces taking it in: John's young brow folding, Peter stilled mid-motion; the sentence's two halves working on them.",
        "must_not_show": "no halo, glare or rim-light; the unease GENTLE — friends sensing weather they cannot name.",
        "scene": (
            "Around him the sentence does "
            "its double work: John's young "
            "face warming at the wanted-you "
            "half even as his brow folds at "
            "the rest, Peter gone still with "
            "a piece of bread forgotten "
            "halfway to his mouth, a cup "
            "set down slowly further along "
            "— the table's ease rippling "
            "like water under wind as "
            "twelve friends try to hold "
            "I-wanted-this and the-hard-"
            "thing in the same hands. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r089-b05", "out": "s05-he-knew-what-was-coming.jpeg", "seg": "n1",
        "window": "24.15-30.12", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "MEAL"],
        "narration": (
            "He knew what was coming that night, and what he wanted first "
            "was to sit down and eat with his friends."
        ),
        "must_show": "the choice made visible — the wide warm table at supper: Jesus fully present in the meal, passing bread, listening; foreknowledge choosing friendship first.",
        "must_not_show": "no halo, glare or rim-light; NOTHING ominous staged — the warmth itself is the point.",
        "scene": (
            "The wide frame holds what he "
            "chose to do with his last free "
            "evening: the lamplit table at "
            "full supper — bread passing "
            "hand to hand, a low laugh at "
            "one corner, bowls shared "
            "across the ring — and Jesus in "
            "the middle of it fully present, "
            "tearing bread for the man "
            "beside him, head tipped to "
            "another's story — a man who "
            "knows exactly what midnight "
            "holds, spending the evening "
            "entirely on his friends. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r089-b06", "out": "s06-then-he-took-the-bread.jpeg", "seg": "n2",
        "window": "31.82-35.86", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "MEAL"],
        "narration": (
            "Then he took the bread, gave thanks, broke it, and gave it to "
            "them."
        ),
        "must_show": "SCRIPTURE-EXACT: took, thanked, brake, gave — Jesus with the flat round lifted in thanks, then breaking it; the table hushing around the four verbs.",
        "must_not_show": "no halo, glare or rim-light; the sequence READable — the round lifted, the break beginning, hands stilling around the table.",
        "scene": (
            "The table hushes around four "
            "plain verbs: Jesus lifting the "
            "flat round in both hands with "
            "his eyes closed in thanks — "
            "then the bread BREAKING, the "
            "crust parting rough down its "
            "middle in the lamplight — and "
            "the pieces starting outward "
            "hand to hand around the ring, "
            "every conversation dead, every "
            "face turned in, supper turning "
            "into something none of them "
            "has a name for yet. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r089-b07", "out": "s07-this-is-my-body-which.jpeg", "seg": "j1",
        "window": "37.50-42.47", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MEAL"],
        "narration": (
            "This is my body which is given for you: this do in remembrance "
            "of me."
        ),
        "must_show": "SCRIPTURE-EXACT: the words over the bread — close on Jesus's hands holding the broken halves toward them, his steady face above; GIVEN FOR YOU said into their eyes.",
        "must_not_show": "no halo, glare or rim-light; the bread PLAIN broken bread — the weight in the words and face, not effects.",
        "scene": (
            "Close on the gift at the "
            "moment of naming: the two "
            "broken halves held out on "
            "Jesus's open hands into the "
            "lamplight, rough-edged and "
            "steaming faintly, and above "
            "them the steady face saying "
            "what the bread now is — GIVEN "
            "FOR YOU — the words passing "
            "into the circle of eyes with "
            "the terrible gentleness of a "
            "man handing over the only "
            "thing he owns outright. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r089-b08", "out": "s08-do-this-to-remember-me.jpeg", "seg": "n2b",
        "window": "44.12-45.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["MEAL"],
        "narration": "Do this to remember me.",
        "must_show": "the remembrance begun — close on disciples' hands receiving the broken pieces around the table: rough hands taking bread they will take for the rest of their lives.",
        "must_not_show": "no halo, glare or rim-light; the HANDS the picture — fishermen's and tax-collector's hands, receiving.",
        "scene": (
            "Close on the hands the "
            "remembrance starts with: "
            "fishermen's rope-scarred "
            "fingers closing carefully "
            "around their pieces, a younger "
            "smooth hand cupping its "
            "portion like water, an old "
            "workman's palm receiving the "
            "bread as gravely as wages — "
            "around the lamplit ring the "
            "first of ten thousand times "
            "these same hands will do "
            "exactly this, remembering. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r089-b09", "out": "s09-not-a-symbol-he-was.jpeg", "seg": "n2b",
        "window": "45.44-51.55", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "MEAL"],
        "narration": (
            "Not a symbol he was explaining — a gift he was handing over, "
            "piece by piece, into their hands."
        ),
        "must_show": "the handing-over — the wide table mid-distribution: Jesus placing bread directly into palm after palm around the ring; a gift travelling person to person.",
        "must_not_show": "no halo, glare or rim-light; the giving DIRECT — his hand to each hand, no plate between.",
        "scene": (
            "Around the ring, the camera down the table's length "
            "with the near backs in three-quarter, the gift "
            "travels the personal way: Jesus "
            "leaning to place a piece "
            "directly into each opened palm "
            "— pressing it in with a small "
            "closing touch, meeting each "
            "pair of eyes for its own "
            "moment — no dish passed along, "
            "no portion flung, every single "
            "man served skin to skin by the "
            "giver himself, piece by piece "
            "around the lamplit table until "
            "no hand is empty. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r089-b10", "out": "s10-after-the-meal-he-lifted.jpeg", "seg": "n3",
        "window": "53.23-56.07", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "MEAL"],
        "narration": "After the meal he lifted the cup, and gave it to them, too.",
        "must_show": "SCRIPTURE-EXACT: the cup after supper — Jesus lifting the great two-handled clay cup in both hands over the finished meal, the ring's eyes rising with it.",
        "must_not_show": "no halo, glare or rim-light; the meal visibly FINISHED — emptied bowls, broken bread remains; the cup the new centre.",
        "scene": (
            "The meal lies finished down the "
            "table — emptied bowls, the "
            "bread's scattered remains — and "
            "over it Jesus lifts the great "
            "two-handled clay cup in both "
            "hands, the dark wine tilting "
            "slow inside the fired earth, "
            "every face around the ring "
            "rising with it like grass "
            "following the sun — supper "
            "ended, and the second half of "
            "the gift beginning its round "
            "in the lamplight. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r089-b11", "out": "s11-this-cup-is-the-new.jpeg", "seg": "j2",
        "window": "57.79-61.69", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MEAL"],
        "narration": "This cup is the new testament in my blood, which is shed for you.",
        "must_show": "SCRIPTURE-EXACT: the covenant named — close on the held cup and Jesus's steady face over it; NEW TESTAMENT... FOR YOU, spoken like the signing it is.",
        "must_not_show": "no halo, glare or rim-light; the wine plain dark wine — the weight entirely in the naming.",
        "scene": (
            "Close on the covenant at its "
            "signing: the clay cup steady in "
            "his two hands, the dark wine "
            "still within it, and above the "
            "rim the face that means every "
            "word — THE NEW TESTAMENT, IN MY "
            "BLOOD, FOR YOU — an agreement "
            "older empires would carve in "
            "stone and seal in gold, "
            "executed instead in fired "
            "clay and a quiet voice, at a "
            "supper table, between friends. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r089-b12", "out": "s12-a-brand-new-promise-between.jpeg", "seg": "n3b",
        "window": "63.36-68.38", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "MEAL"],
        "narration": (
            "A brand new promise between God and people, and he was signing "
            "it with his own life."
        ),
        "must_show": "the covenant passing — the cup travelling hand to hand around the table, each man drinking in turn; the promise being countersigned around the ring.",
        "must_not_show": "no halo, glare or rim-light; the passing REVERENT — two hands on the cup at each station, eyes closing over the rim.",
        "scene": (
            "The promise makes its round, the camera at the "
            "table's side so the cup's travel reads in profile: "
            "the great cup passing hand to "
            "careful hand along the ring — "
            "each man taking it in both "
            "palms, drinking with his eyes "
            "closed, passing it on a shade "
            "more slowly than he received "
            "it — twelve countersignatures "
            "gathering on a covenant written "
            "in wine, while its author "
            "watches his friends drink what "
            "it will cost him to keep. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r089-b13", "out": "s13-for-i-say-unto-you.jpeg", "seg": "jv18",
        "window": "70.03-77.09", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MEAL"],
        "narration": (
            "For I say unto you, I will not drink of the fruit of the vine, "
            "until the kingdom of God shall come."
        ),
        "must_show": "SCRIPTURE-EXACT: the vow — Jesus setting his own cup DOWN, hand flat beside it, face lifted with the until-the-kingdom promise; abstinence with an appointment.",
        "must_not_show": "no halo, glare or rim-light; the cup set down FINAL — the vow visible in the gesture.",
        "scene": (
            "Jesus sets the cup down and "
            "does not lift it again: the "
            "clay base meeting the table "
            "with a soft final sound, his "
            "hand coming to rest flat beside "
            "it, and the face above lifted "
            "with the strange bright vow — "
            "NOT UNTIL THE KINGDOM COMES — "
            "a man scheduling his next "
            "drink for the other side of "
            "everything, and saying it like "
            "a fixed appointment he intends "
            "to keep. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r089-b14", "out": "s14-he-was-telling-them-this.jpeg", "seg": "n4",
        "window": "78.82-83.05", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "PETER", "JOHN"],
        "narration": (
            "He was telling them this was not goodbye — it was see you at "
            "the next meal."
        ),
        "must_show": "the promise's warmth — close on Jesus's face carrying the next-meal certainty to his friends; around him, faces easing at the hope in it.",
        "must_not_show": "no halo, glare or rim-light; HOPE the register — a parting reframed as a reservation.",
        "scene": (
            "Close on the reframing as it "
            "lands: Jesus's face warm with "
            "the certainty of the "
            "appointment — not farewell, "
            "RESERVATION — and around him "
            "the frightened edges easing: "
            "John's brow unknotting a "
            "degree, Peter's jaw loosening, "
            "the table absorbing the "
            "strange comfort of a man "
            "speaking about the far side of "
            "the worst night as casually as "
            "next week's supper. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r089-b15", "out": "s15-then-he-and-his-friends.jpeg", "seg": "n4",
        "window": "83.05-87.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM"],
        "narration": (
            "Then he and his friends sang together and walked out into the "
            "night."
        ),
        "must_show": "SCRIPTURE-EXACT: the hymn and the going (Mark 14:26) — the company on their feet singing, then filing down into the deep night; the room's lamplight behind, the dark ahead.",
        "must_not_show": "no halo, glare or rim-light; the singing REAL — open mouths, arms over shoulders; the night entered together.",
        "scene": (
            "The supper ends on its feet, the camera behind the "
            "rising company toward the door, and "
            "singing: the company risen "
            "around the table with the old "
            "psalm moving through them — "
            "arms over shoulders, Peter's "
            "big voice carrying, John's "
            "young one under it — and then "
            "the filing out, one by one "
            "down the outside stair into "
            "the deep Passover night, the "
            "lamplight warm at their backs "
            "and the dark of the olive "
            "groves ahead, entered together "
            "and in song. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r089-b16", "out": "s16-the-bread-and-the-cup.jpeg", "seg": "n5",
        "window": "88.66-93.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM", "MEAL"],
        "narration": (
            "The bread and the cup, still on the table — a gift to remember "
            "him by."
        ),
        "must_show": "the closing image — the emptied lamplit room: the broken bread's remains and the clay cup standing together on the quiet table; the gift, left for the world.",
        "must_not_show": "no halo, glare or rim-light; the room EMPTY of people — the two objects holding the whole meaning alone.",
        "scene": (
            "The room keeps the closing "
            "picture alone: cushions pushed "
            "back and empty, the lamps "
            "burning low over the quiet "
            "table, and at its centre the "
            "two things left on purpose — "
            "the broken round's remaining "
            "halves, and the great clay cup "
            "with its dark inch of wine — "
            "a gift sized for every table "
            "on earth, resting where twelve "
            "sets of hands learned it, "
            "while the singing fades down "
            "the stair outside. Every "
            "figure has two arms, two hands "
            "and one head."
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
