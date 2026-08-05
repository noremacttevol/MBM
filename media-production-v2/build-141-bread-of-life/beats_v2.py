#!/usr/bin/env python3
"""V2 beat map — row 141, build-141-bread-of-life (John 6:26-51).

COVERAGE: 10 pictures over 53.9 s = 5.4 s/picture (matches the library density).

SCRIPTURE FACTS (John 6 KJV):
  6:26  the crowd followed after the loaves: "ye seek me... because
        ye did eat of the loaves, and were filled."
  6:35  "I AM THE BREAD OF LIFE: he that cometh to me shall NEVER
        HUNGER; and he that believeth on me shall NEVER THIRST."
  6:48-49 "I am that bread of life. Your fathers did eat MANNA in
        the wilderness, and are dead."
  6:51  "I am the LIVING BREAD which came down from heaven... the
        bread that I will give is MY FLESH, which I will give for
        the LIFE OF THE WORLD."
  Setting: the Capernaum lakeshore, the day after the feeding of
        the five thousand; the crowd has crossed the lake to find
        him.

RENDERING LAWS (first of the I AM rows, 141-146):
  - THE GIVEN-FLESH FORESHADOW (b08/b10) is carried by BROKEN BREAD
    ONLY — Jesus's hands slowly breaking one loaf. No cross imagery,
    no wounds, nothing of the passion depicted (that belongs to
    rows 94-96 at their merciful distance).
  - The MANNA vignette (b06) is the gathering morning only —
    robed ancestors gathering the white flakes at dawn; the "and
    are dead" is carried by narration, never by graves.
  - The crowd's appetite is HUMAN, not mocked — hungry ordinary
    people who ate well yesterday and want that again; the misaim
    is gentle.
  - Bread is rendered lovingly everywhere — real torn barley
    loaves, crumb and crust; the literal kind must look GOOD so
    the deeper kind means more.
  - b09's deeper hunger: a fed man at a full table with searching
    eyes — the emptiness interior, dignified, never caricature.

TIME OF DAY ARC (intentional): warm morning on the lakeshore
through the teaching; the manna vignette at pale desert dawn BY
DESIGN; the close in bakery-warm gold.

CHANGING CONDITION (kept OUT of the locks): one loaf — whole in the
early frames, broken open from b08 on.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "SHORE": (
        "SHORE LOCK: the Capernaum lakeshore — a pebbled shore with "
        "beached fishing boats and drying nets, the blue lake "
        "behind, low stone houses of the town beginning up the "
        "bank; warm morning light. The same shore throughout."
    ),
    "CROWD": (
        "CROWD LOCK: the following crowd — ordinary Galileans who "
        "crossed the lake: fishermen, labourers, mothers, boys; "
        "earth-toned robes of brown, rust, olive and slate (no "
        "cream — only Jesus wears cream); varied faces, eager and "
        "hungry, never mocked."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r141-b01", "out": "s01-a-crowd-had-followed-jesus.jpeg", "seg": "n0",
        "window": "0.28-4.53", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SHORE", "CROWD"],
        "narration": "A crowd had followed Jesus after He fed thousands with a few loaves.",
        "must_show": "the pursuit — boats freshly beached, the crowd streaming up the shore toward Jesus; yesterday's miracle still on their faces.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the crowd EAGER, not mobbing; boats and nets true to the shore.",
        "scene": (
            "Yesterday's miracle has a following, the camera "
            "looking up the pebbled shore past the crowd's "
            "hurrying backs: boats freshly beached at every "
            "angle, still dripping, and the people pouring off "
            "them toward Jesus where he stands above the "
            "waterline — fishermen and mothers and boys who "
            "rowed a whole lake overnight on the strength of "
            "one supper — a congregation recruited by bread, "
            "arriving hungry for more of whatever that was. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r141-b02", "out": "s02-he-gave-them-something-deeper.jpeg", "seg": "n0",
        "window": "5.95-7.94", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SHORE"],
        "narration": "He gave them something deeper.",
        "must_show": "the turn to the gift — Jesus turning to face the arriving crowd, gravity and warmth gathering; a giver about to out-give the request.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gravity WARM — a better gift coming, not a rebuke.",
        "scene": (
            "The request is about to be out-given: Jesus turns "
            "to face the crowd coming up the stones, and "
            "something gathers in the deep brown eyes that is "
            "bigger than the breakfast they came for — the "
            "particular warmth of a giver holding a gift the "
            "askers have not thought to ask — they want the "
            "loaves again; he has decided, this morning, on "
            "this shore, to offer them the Baker. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r141-b03", "out": "s03-i-am-the-bread-of.jpeg", "seg": "j1",
        "window": "8.60-16.26", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SHORE", "CROWD"],
        "narration": (
            "I am the bread of life: he that cometh to me shall never "
            "hunger; and he that believeth on me shall never thirst."
        ),
        "must_show": "SCRIPTURE-EXACT: the declaration — Jesus with arms open to the crowd, the great I AM landing on hungry faces; warm gold morning light.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the crowd's hunger VISIBLE and dignified — the words meeting it head-on.",
        "scene": (
            "The greatest menu ever announced has one item: "
            "Jesus with his arms open to the shore-crowd, the "
            "morning gold on his face as the sentence lands — "
            "I AM the bread of life — never hunger, never "
            "thirst, the two oldest aches in the human body "
            "spoken to directly — and along the pebbles the "
            "eager faces still smelling of yesterday's barley "
            "go quiet one by one, hearing their stomachs' "
            "vocabulary borrowed for something underneath "
            "their stomachs. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r141-b04", "out": "s04-not-the-kind-you-chew.jpeg", "seg": "n1",
        "window": "17.93-19.36", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Not the kind you chew.",
        "must_show": "the literal kind — a beautiful torn barley loaf close on a plain board: crust and warm crumb, steam; the good ordinary bread that is NOT the subject.",
        "must_not_show": "no halo; the bread LOVELY — real crust, real crumb; its goodness makes the deeper kind mean more.",
        "scene": (
            "Here is the kind he did NOT mean, at its most "
            "persuasive: a barley loaf torn open on a plain "
            "board, crust crackled brown, the warm crumb "
            "steaming faintly in the morning air, flour still "
            "dusting the board around it — bread at its full "
            "honest glory, the kind that fed five thousand "
            "and would gladly feed them again — good, "
            "necessary, delicious, and not once in its "
            "history able to reach the part of a person that "
            "stays hungry after seconds. No people are "
            "needed in this frame."
        ),
    },
    {
        "id": "v2-r141-b05", "out": "s05-i-am-that-bread-of.jpeg", "seg": "j2",
        "window": "23.60-25.28", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SHORE"],
        "narration": "I am that bread of life.",
        "must_show": "SCRIPTURE-EXACT: the identification — close on Jesus, his hand flat at his own chest; the claim personal and total.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hand at the CHEST — I, myself; nothing else in the claim.",
        "scene": (
            "The claim gets its address: close on Jesus in "
            "the warm light with his hand laid flat at his "
            "own chest — I am THAT bread — the sentence "
            "walking the whole metaphor home to one "
            "standing, breathing man — not a doctrine about "
            "bread, not a ritual of bread: a person, "
            "presenting himself to the hungry as the supply "
            "itself, with the calm of someone stating his "
            "occupation. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r141-b06", "out": "s06-the-bread-their-ancestors-ate.jpeg", "seg": "n2",
        "window": "26.85-33.08", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The bread their ancestors ate in the wilderness didn't keep "
            "them alive forever. But the bread Jesus gives does."
        ),
        "must_show": "the manna morning — robed ancestors gathering white manna flakes off the desert ground at pale dawn, baskets filling; the wilderness miracle remembered. NO graves.",
        "must_not_show": "ABSOLUTE: no graves, no death imagery — the gathering morning only; the mortality is narration's alone.",
        "scene": (
            "The old bread had its own miracle mornings: at "
            "pale desert dawn the robed ancestors move "
            "stooping across the ground, gathering the "
            "white manna flakes off the stones into their "
            "baskets — mothers and elders and children "
            "filling their omers as the light comes up rose "
            "over the wilderness camp — heaven's daily "
            "bread, faithful every morning for forty years, "
            "and able, for all its wonder, to do only what "
            "bread does: carry them to the next hunger. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r141-b07", "out": "s07-they-wanted-more-bread.jpeg", "seg": "n0",
        "window": "4.53-5.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHORE", "CROWD"],
        "narration": "They wanted more bread.",
        "must_show": "the misaimed appetite — eager crowd faces close, a few hands half-extended; yesterday's loaves in their eyes; human, hungry, gently drawn.",
        "must_not_show": "no halo; the hunger DIGNIFIED — no mockery, no greed-caricature; ordinary people wanting supper.",
        "scene": (
            "What they crossed the lake for is written "
            "plainly on them: close along the front of the "
            "crowd — a fisherman's eyes bright with "
            "yesterday's memory, a mother's hand half-"
            "extended out of pure reflex, a boy craning for "
            "the baskets that must surely be somewhere — "
            "honest stomachs voting for the one candidate "
            "they understand — more of that bread, master; "
            "more of yesterday — the right man found, for "
            "the smaller of the two reasons. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r141-b08", "out": "s08-i-am-the-living-bread.jpeg", "seg": "j3",
        "window": "33.79-46.65", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SHORE", "CROWD"],
        "narration": (
            "I am the living bread which came down from heaven: if any man "
            "eat of this bread, he shall live forever: and the bread that I "
            "will give is my flesh, which I will give for the life of the "
            "world."
        ),
        "must_show": "SCRIPTURE-EXACT: the living bread — Jesus slowly BREAKING one loaf in his two hands as he speaks, the crowd hushed; the given-flesh carried by the breaking bread ONLY.",
        "must_not_show": "ABSOLUTE: no cross imagery, no wounds, nothing of the passion — the slow breaking of bread carries the whole foreshadow.",
        "scene": (
            "The hardest sentence of the morning is "
            "illustrated by his own two hands: as the words "
            "come — living bread, my FLESH, given for the "
            "life of the world — Jesus slowly breaks one "
            "barley loaf between his carpenter's hands, the "
            "crust parting, the warm crumb opening — the "
            "crowd gone entirely still around the small "
            "tearing sound — a man foretelling the gift of "
            "himself in the only language the shore owns: "
            "bread, broken open, held out. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r141-b09", "out": "s09-the-kind-that-satisfies-the.jpeg", "seg": "n1",
        "window": "19.36-22.99", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "The kind that satisfies the part of you food can't reach.",
        "must_show": "the deeper hunger — a man at a FULL table, fed and comfortable, whose eyes search the middle distance; the interior emptiness dignified and recognizable.",
        "must_not_show": "no halo; the emptiness INTERIOR — no theatrical despair; a full table and searching eyes.",
        "scene": (
            "The part food cannot reach shows best at a "
            "full table: a man sits back from a good "
            "supper — bread broken, bowl scraped, cup "
            "poured, everything a body could ask within "
            "arm's reach — and his eyes are away in the "
            "middle distance, searching a horizon the room "
            "does not contain — fed to the collarbone and "
            "hungry somewhere underneath it, in the "
            "unfurnished room every person carries that no "
            "harvest has ever entered. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r141-b10", "out": "s10-he-was-speaking-of-himself.jpeg", "seg": "n3",
        "window": "48.14-53.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SHORE", "CROWD"],
        "narration": (
            "He was speaking of Himself — given, like bread broken, so the "
            "world could have life."
        ),
        "must_show": "the closing offer — the broken loaf open in Jesus's two extended hands toward the crowd; the gift held out; bakery-warm gold light.",
        "must_not_show": "ABSOLUTE: no passion imagery — the extended broken loaf IS the sentence; his face warm and resolved.",
        "scene": (
            "The sermon ends held out at arm's length: the "
            "broken loaf lies open across Jesus's two "
            "extended hands, offered forward to the crowd "
            "and the shore and the whole hungry world "
            "beyond them — the crumb warm, the halves "
            "parted, the gift's shape already chosen — "
            "himself, given, like bread broken — and on his "
            "face above the offering, the warm settled "
            "resolve of a man who knows exactly what the "
            "metaphor will cost him, and holds it out "
            "anyway. Every figure has two arms, two hands "
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
