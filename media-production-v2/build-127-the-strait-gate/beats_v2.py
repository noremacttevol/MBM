#!/usr/bin/env python3
"""V2 beat map — row 127, build-127-the-strait-gate (Matthew 7:13-14).

COVERAGE: 10 pictures over 59.3 s = 5.9 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 7 KJV):
  7:13  "Enter ye in at the STRAIT GATE: for WIDE is the gate, and
        BROAD is the way, that leadeth to destruction, and MANY there
        be which go in thereat."
  7:14  "Because STRAIT is the gate, and NARROW is the way, which
        leadeth unto LIFE, and FEW there be that find it."
  Setting: the Sermon on the Mount hillside — same as rows 121-126.

RENDERING LAWS (content-care):
  - DESTRUCTION IS NEVER DEPICTED. The broad road is genuinely
    pleasant — smooth, level, popular — and simply runs out into a
    flat featureless haze at its far end. NO cliff edge, NO fire, NO
    doom imagery, NO falling figures, ever. The narration's weight
    lives in the choice, not in a horror at the end.
  - The narrow way's payoff IS depicted (b09): high green living
    country — springs, trees, morning light. The row's visual
    argument: the hard gate is the one that opens onto LIFE.
  - Nobody on the broad road is a villain — ordinary cheerful
    travellers; the "many" are simply many.
  - Both gates stand OPEN in every frame (b10 says so out loud) —
    neither is ever barred, chained, or guarded.
  - The GATES landscape is ONE consistent place: the two gates a
    stone's throw apart at a road fork — same gates, same fork,
    every landscape frame.
  - HILLSIDE and CROWD locks are BYTE-IDENTICAL to builds 121-126.

TIME OF DAY ARC (intentional): the hillside in the sermon's warm
late-afternoon gold; the gates landscape in clear bright morning
throughout (the choice is lit fairly — neither road gets gloomy
weather); b09's high country in full clean morning light.

CHANGING CONDITION (kept OUT of the locks): the chooser at the fork
— considering at b08, mid-step toward the narrow gate at b10.
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
    "GATES": (
        "GATES LOCK: the two gates — at a road fork on open country: "
        "on one side a WIDE handsome stone gateway opening onto a "
        "BROAD smooth level road; a stone's throw away a NARROW low "
        "stone gate opening onto a TIGHT climbing footpath into the "
        "hills. Both gates always standing OPEN, neither barred nor "
        "guarded. The same fork, gates and roads throughout, in "
        "clear bright morning light."
    ),
}

REF = True

# STALE-V1 fix (audio lane, 2026-08-11): rebuild the audio track from the V1
# segment mp3s at the extract_beats offsets instead of copying the stale V1
# mp4's AAC (which fails assert_v1_final_is_current). Re-voices nothing ($0).
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r127-b01", "out": "s01-jesus-stood-before-the-crowd.jpeg", "seg": "n0",
        "window": "0.28-6.60", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Jesus stood before the crowd and described two roads — two ways "
            "that every person gets to choose."
        ),
        "must_show": "the teaching — Jesus STANDING now before the seated crowd, both arms out describing two diverging ways; the sermon nearing its great choice.",
        "must_not_show": "no halo, glare or rim-light on Jesus; his two arms tracing two DIRECTIONS — the gesture readable.",
        "scene": (
            "For the choosing he stands up, the camera looking "
            "past the seated crowd's backs up the gold slope: "
            "Jesus on his feet before them now, both arms "
            "extended in two diverging lines — this way, and "
            "that way — the whole sermon narrowing toward the "
            "fork every listener will walk to sooner or later, "
            "and the crowd very still under the two open arms, "
            "understanding without being told that the map being "
            "drawn in the air is of their own lives. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r127-b02", "out": "s02-a-narrow-gate-that-leads.jpeg", "seg": "n3b",
        "window": "45.39-49.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATES"],
        "narration": "A narrow gate that leads to life, found by the few who choose it.",
        "must_show": "the narrow gate — the low stone gate open onto the tight climbing path, and above it the hills greening toward high living country; one small figure already climbing.",
        "must_not_show": "no halo; the gate OPEN and inviting in its plainness; the green height visibly worth it.",
        "scene": (
            "The harder gate keeps the better secret: the low "
            "narrow stone gate stands open on its climbing "
            "footpath, plain as a shepherd's doorway — and above "
            "and beyond it the hills green upward toward high "
            "country where trees stand and light pools, the "
            "path's destination visible over its own steepness — "
            "one small figure already climbing the tight way, "
            "the few's whole reward spread out above the "
            "unassuming gate that leads to it. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r127-b03", "out": "s03-enter-ye-in-at-the.jpeg", "seg": "j1",
        "window": "7.20-18.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATES"],
        "narration": (
            "Enter ye in at the strait gate: for wide is the gate, and broad "
            "is the way, that leadeth to destruction, and many there be "
            "which go in thereat:"
        ),
        "must_show": "SCRIPTURE-EXACT: the wide gate — the handsome stone gateway thronged with cheerful travellers streaming onto the broad level road, whose far end dissolves into flat featureless haze; nothing sinister depicted.",
        "must_not_show": "ABSOLUTE: no cliff, no fire, no doom at the road's end — flat haze only; the travellers ordinary and cheerful, never villains.",
        "scene": (
            "The popular gate earns its popularity honestly: the "
            "wide stone gateway stands handsome and open, and "
            "through it the travellers stream in easy cheerful "
            "numbers — families, traders, friends in "
            "conversation — onto a road that is everything a "
            "road should be: broad, smooth, level, kind to feet "
            "— running out ahead of them across the plain until "
            "it simply dissolves into a flat pale haze that "
            "shows nothing at all, which is exactly the "
            "trouble with it. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r127-b04", "out": "s04-one-road-looks-easy.jpeg", "seg": "n1",
        "window": "19.44-20.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATES"],
        "narration": "One road looks easy.",
        "must_show": "the ease itself — the broad road surface close: smooth-packed, level, generous, worn comfortable by many feet; pure invitation.",
        "must_not_show": "no halo; genuinely INVITING — no hidden menace planted; the ease honest.",
        "scene": (
            "The easy road's argument is its surface: close "
            "along the broad way — smooth-packed earth wide "
            "enough for five abreast, level as a threshing "
            "floor, worn kind and comfortable by generations of "
            "feet, not a stone to stub on in a day's walking — "
            "everything about it saying what easy roads have "
            "always said: no hurry, no climb, plenty of "
            "company — an honest pleasure of a road, asking "
            "only that nobody look too far down it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r127-b05", "out": "s05-because-strait-is-the-gate.jpeg", "seg": "j2",
        "window": "25.52-33.32", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATES"],
        "narration": (
            "Because strait is the gate, and narrow is the way, which "
            "leadeth unto life, and few there be that find it."
        ),
        "must_show": "SCRIPTURE-EXACT: the strait gate close — one traveller stooping to pass through the low narrow opening, staff and bundle drawn in tight; the way beyond tight between rocks, climbing.",
        "must_not_show": "no halo; the stoop REAL — the gate asks something of the body; the climb visible beyond.",
        "scene": (
            "The other gate asks something at the threshold: "
            "close on the low narrow opening as a single "
            "traveller stoops to pass — head bent, staff drawn "
            "in, bundle pulled tight against the chest to fit "
            "the squeeze of stone — and beyond the gate the "
            "way itself stays true to its word, a tight path "
            "climbing between shoulders of rock with room for "
            "one deliberate walker at a time — a door and a "
            "road that cost something at every step, priced "
            "exactly like the life they lead to. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r127-b06", "out": "s06-the-gate-is-wide-the.jpeg", "seg": "n1",
        "window": "20.80-24.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATES"],
        "narration": "The gate is wide, the path is broad, and a lot of people walk that way.",
        "must_show": "the many — the broad road carrying its easy crowd into the distance, spaced comfortable and cheerful; the popularity itself the picture.",
        "must_not_show": "no halo; the walkers VARIED and ordinary (no clone faces); nothing ominous in the frame.",
        "scene": (
            "The count on the broad way speaks for itself: down "
            "the generous road the walkers go in their easy "
            "numbers — knots of friends, a laden donkey, "
            "children weaving between the grown-ups, travellers "
            "spaced comfortable all the way to where the "
            "distance pales — nobody marching, nobody driven, "
            "everybody simply going the way that most feet go "
            "for the oldest reason in the world: because most "
            "feet go that way. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r127-b07", "out": "s07-the-other-road-looks-harder.jpeg", "seg": "n2",
        "window": "34.84-40.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATES"],
        "narration": (
            "The other road looks harder. The gate is narrow, the path is "
            "tight, and far fewer find it."
        ),
        "must_show": "the few — the tight climbing path with two or three walkers spaced far apart on its switchbacks; sparseness against the broad road's plenty.",
        "must_not_show": "no halo; the walkers RESOLUTE, not grim — the fewness the picture, not misery.",
        "scene": (
            "The narrow way's census is quickly taken: on the "
            "tight path's climbing switchbacks just three "
            "figures show — one high near the rocks' shoulder, "
            "one midway leaning into the grade, one only now "
            "clearing the low gate — spaced far apart, each "
            "walking the single-file way at their own steady "
            "cost — not grim, not sorry, just few: a road "
            "whose whole traffic for the morning can be "
            "counted on one hand, and is climbing. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r127-b08", "out": "s08-he-describing-geography-he-was.jpeg", "seg": "n3a",
        "window": "40.75-44.74", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATES"],
        "narration": "He wasn't describing geography. He was describing a decision.",
        "must_show": "the decision — a single traveller standing at the fork between the two open gates, weight not yet committed either way; the choosing itself pictured.",
        "must_not_show": "no halo; the stance NEUTRAL — feet at the fork, face weighing; both gates equally open before him.",
        "scene": (
            "The map was always a portrait: at the fork between "
            "the two open gates a single traveller stands with "
            "his weight on neither foot — the wide handsome "
            "gateway breathing ease on his left, the low narrow "
            "gate holding its climb on his right, both standing "
            "open, neither pressing — and on his face the "
            "unhurried gravity of a man who has understood that "
            "the crossroads is not in the landscape at all: it "
            "is in him, and it is today. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r127-b09", "out": "s09-he-never-said-the-narrow.jpeg", "seg": "n4",
        "window": "49.73-53.68", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "He never said the narrow way would be crowded. He said it leads "
            "to life."
        ),
        "must_show": "the payoff — the narrow path cresting into HIGH LIVING COUNTRY: green upland with a spring, trees, birds, clean morning light; a walker arriving into it.",
        "must_not_show": "no halo; the life ABUNDANT and specific — water, green, shade, light; the arrival's relief visible.",
        "scene": (
            "The narrow way keeps its one promise at the top: "
            "the tight path crests its last rocks and opens "
            "without warning into high living country — an "
            "upland meadow deep in green, a spring running "
            "bright over stones, trees standing in their own "
            "shade, swifts cutting the clean morning air — and "
            "a single walker arriving into all of it with the "
            "climb still in his breathing, standing where the "
            "road's whole quiet advertisement finally pays out: "
            "life, exactly as stated. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r127-b10", "out": "s10-both-gates-are-standing-open.jpeg", "seg": "n4",
        "window": "53.68-58.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATES"],
        "narration": (
            "Both gates are standing open right now, and nobody walks "
            "through either one by accident."
        ),
        "must_show": "the closing frame — both gates OPEN in one composition, and the fork's traveller caught MID-STEP, deliberately, toward the narrow gate; choice as motion.",
        "must_not_show": "no halo; DIRECTION LAW — the step toward the NARROW gate unmistakable; both gates open, neither barred.",
        "scene": (
            "The last frame holds both doors and one decision: "
            "the wide gateway and the narrow gate share the "
            "morning in a single composition, both standing "
            "open as they always have, neither barred, neither "
            "guarded — and between them the traveller from the "
            "fork is caught mid-step, weight committed, sandal "
            "lifted and falling unmistakably TOWARD the low "
            "narrow gate — no drift in it, no accident "
            "possible: a whole life turning on one deliberate "
            "footfall, taken in the open, with both roads "
            "watching. Every figure has two arms, two hands "
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
