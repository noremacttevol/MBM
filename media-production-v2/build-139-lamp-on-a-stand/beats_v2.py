#!/usr/bin/env python3
"""V2 beat map — row 139, build-139-lamp-on-a-stand (Matthew 5:14-16).

COVERAGE: 10 pictures over 48.0 s = 4.8 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 5 KJV):
  5:14  "Ye are the LIGHT of the world. A CITY THAT IS SET ON AN
        HILL cannot be hid."
  5:15  "Neither do men light a candle, and put it UNDER A BUSHEL,
        but ON A CANDLESTICK; and it giveth light unto ALL THAT ARE
        IN THE HOUSE."
  5:16  "LET YOUR LIGHT SO SHINE before men, that they may see your
        good works, and GLORIFY YOUR FATHER which is in heaven."
  Setting: the Sermon on the Mount hillside — the SAME sermon as
        row 121 (salt-and-light); this row is the lamp verses at
        devotional pace.

RENDERING LAWS:
  - HILLSIDE, CROWD, LAMPHOUSE and HILLTOWN locks are BYTE-IDENTICAL
    to build-121 — same sermon, same slope, same one-room house,
    same far town. Share plates with 121 when promoted.
  - ALL LIGHT IS PHYSICAL (doubly binding in a light row): sun,
    clay-lamp flame, dusk windows. Any light effect ON a person is
    an automatic reject; never the drift words.
  - The identity-before-assignment order (b06) governs Jesus's
    register: he NAMES them before he sends them — warmth first.
  - Anti-vanity law (b07/b08, rows 121/122 class): doers look at the
    WORK; the drawn gaze travels PAST the doer to God.
  - b10's close is INTENTION: a careful hand placing the lamp
    deliberately on the high stand — lit on purpose, placed on
    purpose.

TIME OF DAY ARC (intentional): the hillside in the sermon's warm
late-afternoon gold; the lamp-house frames at evening lamp-time BY
DESIGN; the hill town at dusk lamplighting BY DESIGN; the close in
warm lamplit evening.

CHANGING CONDITION (kept OUT of the locks): the lamp — lit, raised,
deliberately placed.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "HILLSIDE": (
        "HILLSIDE LOCK: the teaching hillside — a green grassy slope "
        "above the Sea of Galilee, wildflowers in the grass, the "
        "blue lake and far hills below, warm late-afternoon light. "
        "The same slope and lake view throughout."
    ),
    "CROWD": (
        "CROWD LOCK: the listening crowd — ordinary Galileans seated "
        "on the grass: weathered fishermen, mothers with children, "
        "sun-browned farmers, a few elders; varied earth-toned robes "
        "of brown, rust, olive and slate (no cream — only Jesus "
        "wears cream), varied ages and faces, never uniform."
    ),
    "LAMPHOUSE": (
        "LAMPHOUSE LOCK: the one-room home at evening — mudbrick "
        "walls, a low table, sleeping mats, a wooden LAMPSTAND, a "
        "woven BUSHEL BASKET by the wall, one small clay oil lamp "
        "with a real flame. The same room and furnishings throughout."
    ),
    "HILLTOWN": (
        "HILLTOWN LOCK: the far town set on a hill — pale stone "
        "houses stacked up a ridge above the lake, visible for "
        "miles. The same town and ridge throughout."
    ),
}

REF = True

# STALE-V1 fix (audio lane, 2026-08-11): rebuild the audio track from the V1
# segment mp3s at the extract_beats offsets instead of copying the stale V1
# mp4's AAC (which fails assert_v1_final_is_current). Re-voices nothing ($0).
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r139-b01", "out": "s01-jesus-was-teaching-a-crowd.jpeg", "seg": "n0",
        "window": "0.28-2.73", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Jesus was teaching a crowd on a mountainside.",
        "must_show": "the sermon setting — Jesus seated teaching on the green slope, the ordinary crowd on the grass, the lake below; continuous with the salt-and-light sermon.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the crowd VARIED, every gaze on him.",
        "scene": (
            "The same green pulpit above the lake, the camera "
            "looking past the seated crowd's backs up the "
            "slope: Jesus seated in the warm gold with the "
            "fishermen and mothers and farmers settled thick "
            "on the grass around him — the wildflowers "
            "leaning, the blue water bright below — the "
            "mountainside congregation gathered close for the "
            "sentences that will follow their descendants "
            "into every century: the ones about light. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r139-b02", "out": "s02-ye-are-the-light-of.jpeg", "seg": "j1",
        "window": "6.56-8.55", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Ye are the light of the world.",
        "must_show": "SCRIPTURE-EXACT: the name given — Jesus's hand rising toward the bright sky as the title lands on the ordinary faces; plain daylight the only light.",
        "must_not_show": "no halo, glare or rim-light on Jesus or anyone — the LIGHT in frame is the sun's alone.",
        "scene": (
            "The biggest name anyone ever gave them arrives "
            "in five words: Jesus's open hand rises toward "
            "the wide bright afternoon sky — ye are the "
            "LIGHT of the world — and the fishermen and "
            "mothers on the grass blink up into plain "
            "daylight while the title settles over them, "
            "each ordinary face worth the comparison in the "
            "teacher's un-ironic eyes — the world's light, "
            "currently seated on a hillside in work clothes, "
            "being informed of itself. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r139-b03", "out": "s03-a-city-that-is-set.jpeg", "seg": "j1 + n1",
        "window": "8.55-15.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLTOWN"],
        "narration": (
            "A city that is set on an hill cannot be hid. Nobody lights a "
            "lamp and then hides it under a bowl."
        ),
        "must_show": "SCRIPTURE-EXACT: the unhideable city — the hilltop town at dusk lamplighting, warm windows pricking on across the ridge, visible for miles; INTENTIONAL DUSK.",
        "must_not_show": "no halo; the dusk DELIBERATE — warm windows against blue evening; no people distinguishable at distance.",
        "scene": (
            "The illustration lights itself every evening on "
            "the ridge: dusk comes down blue over the lake "
            "country and the hilltop town answers window by "
            "window — warm lamplight pricking on up the "
            "stacked stone houses until the whole hill wears "
            "its little constellation, readable from every "
            "road and boat and farm for miles around — a "
            "city doing the one thing hill-set cities cannot "
            "help doing, which is exactly the thing the "
            "sermon is about. No people are distinguishable "
            "at this distance."
        ),
    },
    {
        "id": "v2-r139-b04", "out": "s04-you-put-it-up-where.jpeg", "seg": "n1",
        "window": "15.76-18.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAMPHOUSE"],
        "narration": "You put it up where it can light the whole room.",
        "must_show": "the lamp raised — the small clay lamp lifted high onto the wooden stand, warm flame-light reaching every corner, the family's faces bright around it.",
        "must_not_show": "no halo; the light PHYSICAL from the flame only; the whole room served.",
        "scene": (
            "Common sense runs the household liturgy: the "
            "small clay lamp goes up onto its wooden stand — "
            "lifted high, settled firm — and the one-room "
            "house fills to its corners with warm working "
            "light: the low table found, the sleeping mats, "
            "the children's faces tipping up bright, the "
            "doorway's shadow pushed back — one little flame "
            "doing for the whole room what it was kindled "
            "for, from the high place every housewife in "
            "Galilee knows it belongs. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r139-b05", "out": "s05-neither-do-men-light-a.jpeg", "seg": "j2",
        "window": "19.00-26.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAMPHOUSE"],
        "narration": (
            "Neither do men light a candle, and put it under a bushel, but "
            "on a candlestick; and it giveth light unto all that are in the "
            "house."
        ),
        "must_show": "SCRIPTURE-EXACT: the verse staged — the lit lamp ON the stand giving light to ALL in the house; the bushel basket idle by the wall, visibly unemployed.",
        "must_not_show": "no halo; the basket VISIBLE and UNUSED — the absurd alternative present and declined.",
        "scene": (
            "The verse is a photograph of any sensible "
            "evening: the lamp burns high on its stand and "
            "every person in the house sits inside its "
            "reach — the grandmother's mending lit, the "
            "father's bread, the children's game of stones "
            "in the corner — while against the wall the "
            "woven bushel basket sits at its proper grain-"
            "measuring idleness, employed by no one, ever, "
            "in the history of houses, for the smothering "
            "of light — exactly as the verse observes. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r139-b06", "out": "s06-he-told-them-who-they.jpeg", "seg": "n0",
        "window": "2.73-5.90", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "He told them who they were before He told them what to do.",
        "must_show": "identity before assignment — Jesus's warm open-handed address to the crowd, conferring rather than commanding; the order of grace visible in his manner.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NOTHING of command in the gesture yet — naming, not tasking.",
        "scene": (
            "Notice the order the sermon runs in: Jesus's "
            "hands open toward the crowd in the manner of a "
            "man conferring something, not assigning it — "
            "who you ARE, first; what to do, after — the "
            "warm gold light on faces being told their "
            "identity before their errand, given the noun "
            "before the verb — the whole grammar of grace "
            "in the sequence of one afternoon's sentences, "
            "and the crowd sitting up straighter under the "
            "naming. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r139-b07", "out": "s07-not-to-be-noticed-he.jpeg", "seg": "n2",
        "window": "27.62-30.57", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Not to be noticed — he was never after applause.",
        "must_show": "the anti-vanity — in a lamplit evening lane, a woman quietly leaving bread at a widow's doorstep, her eyes on the task, already turning away; no audience sought.",
        "must_not_show": "no halo; NO posing — her attention on the giving and the going; nobody watching.",
        "scene": (
            "The shining he meant looks nothing like a "
            "stage: in the lamplit lane a woman sets a "
            "wrapped loaf quietly on the widow's doorstep — "
            "eyes on the placing, shawl already gathering "
            "for the walk home, gone before any door can "
            "open — no bow taken, no witness counted, the "
            "good work done and LEFT, lit only by the "
            "doorway's spill — light that has never once "
            "checked whether anyone is watching it shine. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r139-b08", "out": "s08-the-point-was-that-people.jpeg", "seg": "n2",
        "window": "30.57-36.42", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The point was that people would see something good in a life "
            "and be drawn to the God behind it."
        ),
        "must_show": "the drawn gaze — the widow at her opened door, bread in hand, looking up PAST the departing helper toward the evening sky; gratitude travelling through the doer to God.",
        "must_not_show": "no halo; nothing IN the sky — the upward-past gaze itself the doctrine.",
        "scene": (
            "Where the seeing was always meant to travel: "
            "the widow stands at her opened door with the "
            "warm loaf found in her hands, and her eyes go "
            "up — past the small departing figure in the "
            "lane, past the rooflines, to the deepening "
            "evening sky — the thanks skipping the "
            "middlewoman entirely, exactly as designed — a "
            "good work seen, and the gaze it drew travelling "
            "clean through the doer to the Father the "
            "shining was always about. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r139-b09", "out": "s09-let-your-light-so-shine.jpeg", "seg": "j3",
        "window": "36.97-42.95", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Let your light so shine before men, that they may see your good "
            "works, and glorify your Father which is in heaven."
        ),
        "must_show": "SCRIPTURE-EXACT: the commission — Jesus with both arms open over the crowd in the late gold, the charge given as a sending; the crowd receiving it.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gold is the SUN's, on everyone equally.",
        "scene": (
            "The commission goes out with both arms: Jesus "
            "open-armed over the seated crowd in the last "
            "warm gold, the charge rolling down the slope — "
            "let it SHINE, so the seeing runs past you to "
            "your Father — and along the grass the ordinary "
            "faces take it like marching orders written as "
            "a blessing, fishermen and mothers and farmers "
            "already half-turned toward the villages where "
            "the shining will actually have to happen, "
            "lamps being sent home to their stands. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r139-b10", "out": "s10-you-were-lit-on-purpose.jpeg", "seg": "n3",
        "window": "44.36-47.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAMPHOUSE"],
        "narration": "You were lit on purpose. You were put on the stand on purpose.",
        "must_show": "the closing intention — close on a careful hand placing the lit lamp DELIBERATELY onto the high stand, settling it true; purpose in the placement itself.",
        "must_not_show": "no halo; the deliberateness readable — the hand unhurried, the setting exact; the flame steady.",
        "scene": (
            "The last frame is the whole sermon in one "
            "careful motion: a hand carries the lit clay "
            "lamp up to the wooden stand and PLACES it — "
            "unhurried, exact, settling the base true and "
            "withdrawing slow so the flame stands steady — "
            "nothing accidental anywhere in the gesture: "
            "chosen, carried, positioned — because that is "
            "how you got where you are, says the narration "
            "over the settling light: lit on purpose, "
            "placed on purpose, and meant to burn exactly "
            "here. Every figure has two arms, two hands "
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
