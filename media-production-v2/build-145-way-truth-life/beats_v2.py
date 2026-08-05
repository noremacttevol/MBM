#!/usr/bin/env python3
"""V2 beat map — row 145, build-145-way-truth-life (John 14:1-6).

COVERAGE: 10 pictures over 42.6 s = 4.3 s/picture (matches the library density).

SCRIPTURE FACTS (John 14 KJV):
  14:2  "In my Father's house are many mansions... I go to PREPARE A
        PLACE for you."
  14:5  THOMAS: "Lord, we know not whither thou goest; and how can
        we know the way?"
  14:6  "I AM THE WAY, THE TRUTH, AND THE LIFE: no man cometh unto
        the Father, but by me."
  Setting: the UPPER ROOM, the night before the cross — build-89's
        room (the last supper chamber), lamplit night.

RENDERING LAWS:
  - The ROOM lock is BYTE-IDENTICAL to build-89's (same upper room,
    same U-shaped table, same lamps) — one chamber across both rows.
  - THOMAS is the shared cast token (thomas sheets in CAST-V2-REF) —
    same face as every build; his question is honest confusion, not
    doubt-villainy; he asks what everyone is thinking.
  - The night is lamplit BY DESIGN (build-89's register): clay
    flames, warm on faces, the window open on deep night.
  - The way/truth/life triptych (b02/b05/b07/b08) lands on JESUS
    HIMSELF present in the room — the hand-at-chest I AM signature;
    "standing right there in the room with them" is literal.
  - b09/b10's map-vs-person: a rolled map/route-scroll set DOWN,
    and the following of a person — no readable text on any scroll.

TIME OF DAY ARC (intentional): one lamplit night throughout — the
upper room's warm flames against deep night; no other light.

CHANGING CONDITION (kept OUT of the locks): none material — one
room, one night, one conversation.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags. THOMAS comes from the
# shared CAST_LOCKS; ROOM is byte-identical to build-89.
LOCKS = {
    "ROOM": (
        "ROOM LOCK: the upper room — a large furnished chamber up an "
        "outside stair: a LOW U-SHAPED TABLE with cushions where "
        "diners recline, clay oil lamps on the table and in wall "
        "niches, plastered walls, one shuttered window open on the "
        "night. The same table, lamps and walls throughout."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the Eleven around the table — travel-worn "
        "men in earth-toned robes of brown, rust, olive and slate "
        "(no cream — only Jesus wears cream); varied faces warm in "
        "the lamplight, troubled and listening."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r145-b01", "out": "s01-in-the-upper-room-the.jpeg", "seg": "n0",
        "window": "0.40-7.23", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "DISCIPLES"],
        "narration": (
            "In the upper room, the night before the cross, Jesus told His "
            "disciples He was going to prepare a place for them."
        ),
        "must_show": "the room and the promise — the lamplit upper room, Jesus speaking at the U-shaped table, the Eleven troubled and listening; the going-to-prepare landing on worried faces.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the lamps physical; the disciples' trouble visible and dignified.",
        "scene": (
            "The hardest night begins with a promise about "
            "rooms, the camera looking up the lamplit table "
            "past the reclining disciples' backs: Jesus at "
            "the U-shaped table's head with the clay flames "
            "warm on his face, telling his troubled men about "
            "his Father's house and the place he goes to "
            "prepare — and around the low table the Eleven "
            "listen with the particular worry of men who can "
            "feel a goodbye inside a comfort — the night "
            "before the cross, furnished with lamplight and "
            "a promise. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r145-b02", "out": "s02-not-one-way-among-many.jpeg", "seg": "n2a",
        "window": "24.26-26.12", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM"],
        "narration": "Not one way among many.",
        "must_show": "the exclusivity held gently — close on Jesus, one finger raised in the singular; THE way, said with warmth, not narrowness.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the ONE gesture warm — a rescue's precision, not a gate slammed.",
        "scene": (
            "The article in the sentence is doing enormous "
            "work: close on Jesus in the lamplight with one "
            "finger gently raised — THE way, not A way — the "
            "singular held up with the warmth of a rescuer "
            "naming the one rope that reaches, not the "
            "narrowness of a gatekeeper — precision in the "
            "service of getting everyone home, spoken to "
            "men who will spend their lives walking exactly "
            "this claim into the world. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r145-b03", "out": "s03-thomas-spoke-up-lord-we.jpeg", "seg": "n1",
        "window": "8.75-13.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM", "DISCIPLES"],
        "narration": (
            "Thomas spoke up — Lord, we don't know where You're going, so "
            "how can we know the way?"
        ),
        "must_show": "SCRIPTURE-EXACT: the honest question — Thomas leaning in from the table, hands open in genuine confusion, asking what every face around him is thinking.",
        "must_not_show": "no halo; Thomas's question HONEST — no doubt-villainy; the other faces agreeing with it silently.",
        "scene": (
            "Somebody has to say what all of them are "
            "thinking, and it is Thomas: he leans in from "
            "his place at the low table with his hands open "
            "and his brow knotted honestly — Lord, we do not "
            "even know WHERE you are going; how can we know "
            "the way? — the question every other face around "
            "the lamps is silently seconding, asked out loud "
            "by the one disciple who would always rather "
            "look confused than pretend — and the room "
            "grateful to him for it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r145-b04", "out": "s04-i-am-the-way-the.jpeg", "seg": "j1a",
        "window": "14.92-17.61", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "DISCIPLES"],
        "narration": "I am the way, the truth, and the life:",
        "must_show": "SCRIPTURE-EXACT: the answer — Jesus's hand flat at his own chest, eyes on Thomas; the three great nouns landing in the lamplit hush.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the chest gesture exact (I AM signature); Thomas's face receiving.",
        "scene": (
            "The answer to where-is-the-map is a person "
            "touching his own chest: Jesus's hand lies flat "
            "over his heart, his eyes steady on Thomas "
            "across the lamps — I AM the way — and the "
            "truth — and the life — three enormous nouns "
            "arriving at one address, the hush around the "
            "low table deepening word by word as the "
            "question about geography is answered with an "
            "introduction. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r145-b05", "out": "s05-the-truth-itself.jpeg", "seg": "n2b",
        "window": "28.75-30.35", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM"],
        "narration": "The truth itself.",
        "must_show": "truth as a face — close on Jesus's steady clear eyes in the lamplight; nothing hidden anywhere in the gaze; the noun with a face.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the clarity of the GAZE the whole frame.",
        "scene": (
            "What truth looks like when it has a face: close "
            "on Jesus's eyes in the warm lamplight — steady, "
            "clear all the way down, nothing performed and "
            "nothing hidden in them anywhere — the kind of "
            "gaze that has never once needed to look away "
            "from anything it said — not a proposition to "
            "be checked but a person to be known, and "
            "knowable, holding still in the light so the "
            "whole table can read him. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r145-b06", "out": "s06-no-man-cometh-unto-the.jpeg", "seg": "j1b",
        "window": "19.63-22.32", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "DISCIPLES"],
        "narration": "no man cometh unto the Father, but by me.",
        "must_show": "SCRIPTURE-EXACT: the by-me — Jesus's open hand moving from the listening men toward himself, the route drawn through his own person; gravity and welcome together.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gesture a ROUTE (through him), not a barrier.",
        "scene": (
            "The route to the Father gets drawn in the air, "
            "and it passes through the speaker: Jesus's open "
            "hand moves from the circle of his listening men "
            "inward to his own chest — no man comes to the "
            "Father but BY ME — the preposition doing its "
            "quiet enormous work: not around, not past, "
            "THROUGH — a road with a heartbeat, offered at a "
            "supper table to everyone who will ever want to "
            "get home. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r145-b07", "out": "s07-the-way-itself.jpeg", "seg": "n2b",
        "window": "27.61-28.75", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM"],
        "narration": "The way itself.",
        "must_show": "way as a person — Jesus rising slightly / turned as one about to lead, hand beckoning gently; a road that walks ahead of you.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the beckon GENTLE — follow-me, in a room.",
        "scene": (
            "What a way looks like when it can walk: Jesus "
            "half-turned in the lamplight as one about to "
            "lead somewhere, his hand lifted in the small "
            "gentle beckon that started everything by the "
            "lake three years ago — follow — not a route "
            "inked on any scroll but a person who goes "
            "FIRST, through everything, all the way — the "
            "way itself, warm and breathing and already "
            "facing the door. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r145-b08", "out": "s08-the-life-itself-standing-right.jpeg", "seg": "n2b",
        "window": "30.35-34.67", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "DISCIPLES"],
        "narration": "The life itself — standing right there in the room with them.",
        "must_show": "the literal nearness — Jesus standing among the seated Eleven, fully present in the small lamplit room; the enormity of WHO, at arm's reach.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the ordinariness of the room against the enormity — no staging.",
        "scene": (
            "The largest fact in existence is standing on a "
            "rug: Jesus on his feet among the seated Eleven, "
            "close enough for any of them to touch his "
            "sleeve, the clay lamps throwing his ordinary "
            "warm shadow on the plastered wall — the LIFE "
            "itself, the narration insists, right there, in "
            "a rented room that smells of bread and lamp "
            "oil — eternity keeping supper-distance from "
            "eleven tired men, which is exactly where it "
            "has always preferred to stand. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r145-b09", "out": "s09-the-door-to-the-father.jpeg", "seg": "n3a",
        "window": "36.18-38.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM"],
        "narration": "The door to the Father isn't a map to find.",
        "must_show": "the map set down — a rolled route-scroll laid DOWN on the table by the lamps, unopened, retired; the wrong tool for this journey. No readable text.",
        "must_not_show": "no halo; the scroll's script indistinct; the setting-down gesture complete — the map not needed.",
        "scene": (
            "The tool everyone reaches for gets set down "
            "unopened: a rolled route-scroll lies on the "
            "table where a hand has just laid it aside, "
            "cords still tied, its distances and turnings "
            "unconsulted in the lamplight — the instinct of "
            "every traveller — find the map, plot the way — "
            "quietly retired at this table, because the "
            "journey in question has never once been "
            "navigable by directions, only by company. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r145-b10", "out": "s10-a-person-to-follow.jpeg", "seg": "n3b",
        "window": "40.03-41.51", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "DISCIPLES"],
        "narration": "It's a person to follow.",
        "must_show": "the closing follow — Jesus moving toward the room's door, hand in the gentle beckon, the Eleven beginning to rise; following as the whole answer.",
        "must_not_show": "no halo, glare or rim-light on Jesus; DIRECTION — he toward the door, they rising to follow.",
        "scene": (
            "The answer ends the way it began three years "
            "ago — with following: Jesus moves toward the "
            "room's door with his hand trailing the gentle "
            "beckon behind him, and around the low table "
            "the Eleven begin to rise — cushions pushed "
            "back, sandals found, eleven men standing up "
            "into the oldest instruction they know — not a "
            "map to find: a person to follow, through this "
            "night and the next day and everything after "
            "it, all the way to the Father's house. Every "
            "figure has two arms, two hands and one head."
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
