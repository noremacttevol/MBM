#!/usr/bin/env python3
"""V2 beat map — row 113, build-113-where-art-thou (Genesis 2-3).

COVERAGE: 26 pictures over 147.6 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Genesis 3 KJV):
  v8    "they heard THE VOICE of the LORD God WALKING IN THE GARDEN
        in the COOL OF THE DAY: and Adam and his wife HID THEMSELVES
        ... amongst the TREES."
  v9    "WHERE ART THOU?" — the Father's question, asked by One who
        knows the answer, so the hider can come out.
  v10   "I heard thy voice... and I WAS AFRAID, because I was naked;
        and I HID myself." — fear, not defiance.
  v12-13 the answers; "The serpent beguiled me, and I did eat."
  v21   "Unto Adam also and to his wife did the LORD God make COATS
        OF SKINS, and CLOTHED THEM." — the unexpected mercy.
  v23   the sending out — clothed, not alone, with the promise.

GOD RENDERING (Cameron's standing order, 2026-08-07 — REVERSES the old
"never embodied / light only" note that drew this complaint: "God has a
body, weve been through this... create a character for him... so his look
doesnt change much like Jesus"): the LORD is the SAME locked embodied
Father whenever he is in frame — see the GOD THE FATHER LOCK. He is SHOWN,
a real man with weight and footsteps, in every PRESENCE beat (walking with
them, coming through the garden, standing in the clearing to call, sending
them out, clothing them). He stays off-frame ONLY in tight reaction
close-ups on Adam or Eve — the same film grammar used for Jesus, never a
change in how he looks. No halo, glow or rim-light; his majesty is his
face and bearing, not an effect. Modesty for Adam and Eve is unchanged.

SERPENT: NEVER painted — it exists only in the woman's quoted words.

MODESTY + COVERING TIMELINE (absolute — Cameron's order, 2026-08-07,
against the live cut: "the first two thirds where they are wearing RAGS
needs to be changed; first they are wearing nothing — work the pictures
to only show their face or upper torso with eve's breasts covered by
eve's long hair, or random foliage — then when they eat of the tree and
feel naked have them wearing the LEAVES of trees, and then have the last
third stay the same where God makes them clothes"). There are exactly
THREE coverings in this whole story, in this order, and NOTHING else —
NEVER rags, tattered cloth, woven fabric, sackcloth, loincloths or animal
skins before the coats:
  1. BEFORE the fruit (b01-b04): NOTHING — they are unclothed as in Eden
     before the fall, rendered with COMPLETE modesty in the manner of
     reverent classical biblical painting: framed from the chest up,
     and/or the woman's very long hair and garden foliage falling across
     her so no bare chest or lower body is ever in frame. Discretion is
     by HAIR, FOLIAGE, DISTANCE and CHEST-UP FRAMING — not by clothing.
  2. AFTER they eat and feel naked (fig leaves made in b06, worn b06-b20):
     fresh GREEN FIG-LEAF girdles/aprons — real broad leaves threaded on
     vine, clearly leaves, never cloth and never rags.
  3. AFTER the sentence (b21, b23, b24): the well-made dark LEATHER COATS
     the Father makes them — Cameron approved these ("the last ones where
     he made them clothes those are good"): KEEP them exactly.
Nothing immodest in any frame; shame is carried by POSTURE and the eyes.

TIME OF DAY: the golden COOL OF THE DAY throughout — long warm
evening light in the garden; the exile beats at dusk with warmth kept
in the light. Correct story lighting.

CHANGING CONDITION (kept OUT of the identity locks — set per beat):
  covering — nothing (hair/foliage/chest-up framing) → fig leaves → coats
  of skins, per the timeline above; the garden — open peace, then hiding
  places, then behind them; the light — companion, then approaching, then
  following them out. Their FACES and BUILD never change (the locks); only
  the covering, per the beat.

GROUND (Cameron, 2026-08-07: "0:25 they are sitting on water, bad photo,
delete it and redo it a better way"): people are ALWAYS on solid ground —
earth, moss, grass or rock. NEVER seated, crouched or standing ON, IN or
over the stream/water so that they read as sitting on water. The stream
stays in the BACKGROUND only, never under a person.
"""

# LOCKS: one entry per recurring person and per setting. Clothing changes
# across the row and stays OUT of these locks. Only Jesus wears cream (he
# does not appear in this row).
LOCKS = {
    "GARDEN": (
        "GARDEN LOCK: Eden — a deep lush garden in long golden "
        "evening light: great old trees with low sweeping branches, "
        "flowering thickets, a clear stream over smooth stones, "
        "fruit heavy everywhere. The same trees, stream and light "
        "throughout."
    ),
    "ADAM": (
        "ADAM LOCK: the man is the same in every shot — young, "
        "strong and unlined, warm tan skin, shoulder-length dark "
        "hair and a short dark beard; always framed with complete "
        "modesty. His ONLY coverings in the whole story are, in order, "
        "nothing (chest-up framing / foliage), then fig leaves, then "
        "the dark leather coat at the end — NEVER rags, tattered cloth, "
        "woven fabric, sackcloth or a loincloth."
    ),
    "EVE": (
        "EVE LOCK: the woman is the same in every shot — young and "
        "unlined, warm tan skin, very long thick dark hair falling "
        "past her waist; always framed with complete modesty, her long "
        "hair and garden foliage covering her. Her ONLY coverings in the "
        "whole story are, in order, nothing (chest-up framing, her hair "
        "and foliage across her), then fig leaves, then the dark leather "
        "coat at the end — NEVER rags, tattered cloth, woven fabric, "
        "sackcloth or a loincloth."
    ),
    "GOD": (
        "GOD THE FATHER LOCK (Cameron's standing order: God has a body "
        "and one locked look, like Jesus): the Father is the same "
        "glorified embodied man in every shot — majestic and ageless-"
        "strong, flowing white hair and a full white beard, a warm "
        "noble deeply kind face, in a robe of BRILLIANT PURE WHITE (he "
        "alone wears pure white; only Jesus wears cream). Real weight, "
        "real footsteps, radiant dignity WITHOUT any halo or light "
        "effects. His face is shown clearly and is never stern."
    ),
}

REF = True

# AUDIO_FROM_V1_SEGMENTS (2026-08-07, AUDIO-FIX Machine A Dev): STALE-V1-FINAL park.
# The V1 final MP4 (193.3s, 07-29) predates the 15 re-voiced mp3s (163.1s), so the
# recency/duration gate refuses the plain AUDIO LOCK. Rebuild the narration track from
# the V1 mp3s at the extract_beats offsets. Verified: rebuilt track = 163.079s ==
# extract_beats total to the ms (gate PASS). Stills reusable, no regen, $0 audio.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r113-b01", "out": "s01-in-the-beginning-there-was.jpeg", "seg": "n1",
        "window": "0.28-3.96", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "In the beginning there was a garden, and in the garden, peace.",
        "must_show": "the garden at peace — Eden wide in golden evening light: great trees, the stream, fruit heavy, no person in frame yet; peace as a place.",
        "must_not_show": "no figures yet; no halo; the peace TOTAL — nothing in the frame afraid of anything.",
        "scene": (
            "Before everything else, the camera drifting high "
            "along the stream from the side, the "
            "place: a garden deep in "
            "golden evening light — "
            "great trees sweeping their "
            "branches low over flowering "
            "thickets, a clear stream "
            "running easy over smooth "
            "stones, fruit hanging "
            "heavy and unguarded on "
            "every side — and over all "
            "of it a peace so complete "
            "that nothing in the frame "
            "has ever once needed to "
            "hide from anything: the "
            "world as it was meant, "
            "resting in its first "
            "evening light. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b02", "out": "s02-people-and-god-walking-together.jpeg", "seg": "n1",
        "window": "3.96-9.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE", "GOD"],
        "narration": (
            "People and God walking together in the cool of the day, with "
            "nothing to hide and nothing to fear."
        ),
        "must_show": "the walking-together — the man and woman at ease strolling the garden path at distance amid deep foliage, UNCLOTHED as before the fall but shown with complete discretion (far distance, deep foliage across them, her long hair down her back), and WALKING WITH THEM the embodied Father (per the GOD lock): companionship you can see, three friends on an evening walk.",
        "must_not_show": "no halo, glow or rim-light on the Father; the couple wear NOTHING yet (this is before the fall) — NO rags, no cloth, no loincloths, no garments of any kind; modesty entirely by distance, foliage and hair; nothing immodest; nobody on or over the water.",
        "scene": (
            "Down the evening path the "
            "first friendship takes its "
            "walk: the man and woman "
            "strolling far off through "
            "the deep green, easy and "
            "unhurried, her long dark "
            "hair swaying to her waist "
            "— and walking BESIDE them, "
            "keeping their unhurried "
            "pace, the Father himself, "
            "a real man of radiant "
            "dignity in brilliant white, "
            "white hair and full white "
            "beard — "
            "three walking together in "
            "the cool of the day, "
            "nothing hidden anywhere "
            "in the garden and nothing "
            "afraid. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b03", "out": "s03-there-was-only-one-thing.jpeg", "seg": "n2",
        "window": "10.23-13.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "There was only one thing they were asked not to do.",
        "must_show": "the one tree — a single distinct fruit tree standing apart in its own light: beautiful, unfenced, its fruit unlike the others; the one boundary, unwalled.",
        "must_not_show": "no serpent anywhere; no fence — trust the only barrier.",
        "scene": (
            "In its own clearing the one "
            "boundary of paradise "
            "stands unfenced: a single "
            "tree unlike its brothers — "
            "taller, stranger, its "
            "fruit catching the evening "
            "light with a beauty that "
            "asks to be looked at — no "
            "wall around it, no thorn "
            "hedge, no guard: nothing "
            "keeping the whole garden's "
            "abundance and this one "
            "withheld thing apart "
            "except a single trusted "
            "word. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b04", "out": "s04-and-as-people-do-they.jpeg", "seg": "n2",
        "window": "13.41-21.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "EVE"],
        "narration": (
            "And, as people do, they did it anyway — reaching for the one "
            "thing that was not theirs, hoping it would make them more than "
            "they were."
        ),
        "must_show": "the reach — close through foliage: the woman's hand closing on the fruit, the man's hand near hers; the taking at its instant; faces intent, framed chest-up and discreetly by leaves.",
        "must_not_show": "ABSOLUTE: no serpent; the couple wear NOTHING yet (still before the fall) — NO rags, cloth or garments; modesty total, hands, faces and leaf-framed shoulders only.",
        "scene": (
            "Through the leaves the "
            "oldest mistake happens in "
            "close-up: her hand closing "
            "around the strange fruit's "
            "weight, his reaching in "
            "beside hers a breath "
            "behind — two faces framed "
            "in foliage, intent and "
            "hungry for something no "
            "fruit contains: to be "
            "MORE, to be as gods, to "
            "be other than the beloved "
            "creatures they already "
            "were — the twig bending, "
            "the stem giving, and "
            "everything, everything "
            "changing at the snap. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b05", "out": "s05-and-everything-changed-for-the.jpeg", "seg": "n3",
        "window": "22.29-25.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE"],
        "narration": "And everything changed. For the first time they felt shame.",
        "must_show": "shame's arrival — the two crouched on solid mossy earth in the thicket's shadow, turned from each other, arms wrapped around themselves, her long hair pulled forward across her like a cloak, heads down; the first shame as pure posture, framed chest-up and discreet.",
        "must_not_show": "GROUND FIX (Cameron 0:25 'sitting on water'): they are on solid earth/moss, NEVER seated, crouched or standing on, in or over the stream — no water under them, the stream only in the far background if at all. They wear NOTHING yet (fig leaves are not made until the next beat) — covering is her hair, shadow and foliage; NO rags, cloth or leaves here; nothing immodest.",
        "scene": (
            "The change arrives in "
            "their bodies first: deep "
            "in the thicket's shadow "
            "the two turn AWAY from "
            "each other for the first "
            "time in their lives — "
            "arms wrapping their own "
            "shoulders, spines "
            "curling, her hair pulled "
            "forward like a cloak, "
            "his head down — two "
            "people who an hour ago "
            "had nothing to hide, "
            "discovering the terrible "
            "new instinct of the "
            "covered: the first shame, "
            "learning its first "
            "posture. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b06", "out": "s06-they-saw-themselves-and-did.jpeg", "seg": "n3",
        "window": "25.73-31.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE"],
        "narration": (
            "They saw themselves, and did not like what they saw, and "
            "scrambled to cover up, hiding from each other."
        ),
        "must_show": "SCRIPTURE-EXACT: the fig leaves — the two on solid ground hurriedly working fresh BROAD GREEN FIG LEAVES into rough girdles in the shadow, backs half-turned, fingers clumsy with haste; the covering is clearly real green leaves; self-covering as panic.",
        "must_not_show": "the covering is GREEN FIG LEAVES, never rags, cloth or fabric; they are on solid earth, never on or over the stream; modesty total — the leaf-work framed close on hands and bowed profiles; nothing immodest.",
        "scene": (
            "The first clothing is made "
            "in a panic: broad fig "
            "leaves torn down in "
            "handfuls, clumsy fingers "
            "threading them onto "
            "twisted vine, the two "
            "working fast with their "
            "backs half-turned to each "
            "other in the green shadow "
            "— the man's jaw tight, "
            "the woman's hands "
            "shaking on the stems — "
            "humanity's first craft "
            "project, invented in "
            "shame, worn in haste, "
            "hiding them from the "
            "one person each was made "
            "for. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r113-b07", "out": "s07-and-then-they-heard-him.jpeg", "seg": "n4",
        "window": "32.38-39.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "GOD"],
        "narration": (
            "And then they heard him coming — the warm presence of God "
            "moving through the garden in the cool of the evening, the way "
            "he always had."
        ),
        "must_show": "SCRIPTURE-EXACT: the LORD coming — the embodied Father (per the GOD lock) walking the garden path toward them in the cool of the evening, unhurried and familiar, the way he always had; leaves stirring at his passing.",
        "must_not_show": "no halo, glow, shape-shifting or rim-light — a real man walking, majesty in the face and bearing only; nothing immodest.",
        "scene": (
            "Down the evening path he comes himself, as he has "
            "come every evening of their lives: the Father "
            "walking the garden in the cool of the day, robed in "
            "brilliant white, white hair and full white beard, "
            "unhurried among his trees, leaves "
            "stirring at his passing, the low gold light warm "
            "on the noble kind face that has never once been "
            "something to hide from — until tonight. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b08", "out": "s08-and-this-time-they-ran.jpeg", "seg": "n4 + jv9",
        "window": "39.89-45.07", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE", "GOD"],
        "narration": (
            "And this time, they ran and hid themselves among the trees. "
            "Where art thou?"
        ),
        "must_show": "SCRIPTURE-EXACT: the hiding and the question — the leaf-girdled two pressed behind a great trunk in shadow in the foreground, and beyond them in the clearing the embodied Father (per the GOD lock) standing and calling, the question filling the garden.",
        "must_not_show": "no halo, glow or rim-light on the Father; the couple wear GREEN FIG-LEAF girdles (they made them last beat) — never rags, cloth or fabric; on solid ground, never on water; the couple's hiding FEARFUL, faces visible around the trunk's edge; modesty held.",
        "scene": (
            "For the first time in the "
            "world, someone hides from "
            "God: the two pressed "
            "flat behind a great "
            "trunk's shadow, leaf-"
            "girdled and trembling, "
            "her face buried against "
            "his shoulder, his eyes "
            "squeezed shut around the "
            "edge of the bark — while "
            "out in the clearing the "
            "Father himself stands, "
            "white-robed and unhurried, "
            "and the question "
            "moves through every leaf "
            "of the garden, gentle "
            "and enormous: WHERE ART "
            "THOU. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b09", "out": "s09-where-are-you-not-what.jpeg", "seg": "n5",
        "window": "46.58-49.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "Where are you. Not, what have you done.",
        "must_show": "the question's shape — the still golden clearing holding the question: warm light waiting, not searching-angry; the wording's mercy as atmosphere.",
        "must_not_show": "ABSOLUTE: no figure; NOTHING accusatory in the light — patience visible as stillness.",
        "scene": (
            "The frame rests inside the "
            "question's wording: the "
            "golden light standing "
            "patient in the clearing — "
            "not sweeping the thickets "
            "like a search party, not "
            "flaring with any anger, "
            "just waiting, warm and "
            "still, in the place where "
            "the walk always started — "
            "a question built with no "
            "accusation in it anywhere: "
            "not WHAT HAVE YOU DONE, "
            "which corners; but WHERE "
            "ARE YOU, which invites. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b10", "out": "s10-where-are-you-the-cry.jpeg", "seg": "n5",
        "window": "50.77-56.02", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE", "GOD"],
        "narration": (
            "Where are you — the cry of a Father looking for a child who is "
            "hiding."
        ),
        "must_show": "the Father-and-hiding-child shape — the wide garden: the small hidden two behind their tree, and standing patient in the clearing the embodied Father (per the GOD lock) calling toward them; the geometry of every parent's evening search.",
        "must_not_show": "no halo, glow or rim-light on the Father; the couple wear GREEN FIG-LEAF girdles — never rags or cloth; on solid ground, never on water; the composition TENDER — hide-and-seek gone wrong, love still seeking.",
        "scene": (
            "The wide frame holds, the camera at the clearing's "
            "side so hider and seeker share one profile, the "
            "oldest family scene there "
            "is: somewhere in the "
            "darkening green, two "
            "small frightened people "
            "pressed behind a tree — "
            "and standing patient in the "
            "clearing they can no longer face, "
            "the Father himself at evening, "
            "white-robed and unhurried, calling "
            "a child's name into the "
            "garden — the same "
            "geometry as every parent "
            "who ever stood in a "
            "doorway at dusk calling "
            "toward the trees, wanting "
            "only the coming-out. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b11", "out": "s11-he-knew-exactly-where-they.jpeg", "seg": "n5",
        "window": "56.02-63.29", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE", "GOD"],
        "narration": (
            "He knew exactly where they were. He asked so they would come "
            "out. And, trembling, the man answered."
        ),
        "must_show": "the coming-out beginning — the man stepping trembling from behind the trunk toward the embodied Father (per the GOD lock) waiting in the clearing, leaf-girdled, the woman close behind his shoulder; the hardest first step.",
        "must_not_show": "no halo, glow or rim-light on the Father; the couple wear GREEN FIG-LEAF girdles — never rags or cloth; on solid ground, never on water; the step VOLUNTARY — drawn out by the question, not dragged.",
        "scene": (
            "The question does its "
            "work: from behind the "
            "great trunk the man steps "
            "trembling toward the "
            "waiting white-robed Father — leaf-girdled, "
            "arms half-crossed over "
            "himself, every muscle "
            "wanting the shadow back — "
            "and the woman close "
            "behind his shoulder, her "
            "hair drawn around her "
            "like a mantle — two "
            "hiders coming out not "
            "because they were found, "
            "but because they were "
            "asked, which is the whole "
            "reason the question was a "
            "question. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r113-b12", "out": "s12-i-heard-thy-voice-in.jpeg", "seg": "s10",
        "window": "63.84-68.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["ADAM"],
        "narration": (
            "I heard thy voice in the garden, and I was afraid, because I "
            "was naked; and I hid myself."
        ),
        "must_show": "SCRIPTURE-EXACT: the confession — close on the man's trembling face in the gold light saying it: fear owned out loud; the first honest sentence after the fall.",
        "must_not_show": "ABSOLUTE: no figure of God; if his shoulders/chest show he wears a GREEN FIG-LEAF girdle — never rags or cloth; the face AFRAID and honest — dignity kept through the trembling.",
        "scene": (
            "Close on the first "
            "confession ever made: the "
            "man's face in the golden "
            "light, trembling and "
            "bare of every excuse he "
            "will think of later — I "
            "HEARD THY VOICE — the "
            "words shaking loose one "
            "at a time — I WAS AFRAID "
            "— the whole broken "
            "morning owned in one "
            "breath — AND I HID "
            "MYSELF — a man telling "
            "God the truth about "
            "fear while still inside "
            "it, which is the bravest "
            "sentence fear allows. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b13", "out": "s13-that-is-the-whole-of.jpeg", "seg": "n5b",
        "window": "70.19-73.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["ADAM", "EVE"],
        "narration": "That is the whole of it. Not defiance — fear.",
        "must_show": "fear not defiance — the two standing small in the light's edge: nothing rebellious anywhere in their postures, only frightened children before a parent.",
        "must_not_show": "no figure of God; the two wear GREEN FIG-LEAF girdles — never rags or cloth; on solid ground, never on water; NO fists, no jutted chins — the diagnosis visible: afraid, not defiant.",
        "scene": (
            "The frame checks them for "
            "rebellion and finds none: "
            "two small figures at the "
            "light's edge with nothing "
            "defiant anywhere on them — "
            "no jutted chin, no "
            "clenched fist, no turned "
            "back — just the hunched "
            "shoulders and downcast "
            "faces of children who "
            "broke the one thing and "
            "are standing in front of "
            "the parent — the fall's "
            "true anatomy on display: "
            "not a rebellion that "
            "needs crushing, a fear "
            "that needs finding. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b14", "out": "s14-shame-has-never-once-made.jpeg", "seg": "n5b",
        "window": "73.64-80.07", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": (
            "Shame has never once made a person run toward God. It makes "
            "them run behind a tree."
        ),
        "must_show": "the law of shame — the great hiding tree itself in the evening light: the trampled ground behind it where hiders pressed; the universal hiding place, humanity-sized.",
        "must_not_show": "no figures needed — the tree and its worn hiding-shadow carry the sentence.",
        "scene": (
            "The frame studies "
            "humanity's oldest piece "
            "of furniture: the great "
            "tree itself in the "
            "failing gold, and behind "
            "its trunk the pressed "
            "grass and scuffed earth "
            "of the hiding place — "
            "the exact shadow every "
            "generation since has "
            "found its own version "
            "of: the bottle, the "
            "busyness, the locked "
            "room, the long silence — "
            "shame's one unchanging "
            "instinct, standing rooted "
            "in the first garden: not "
            "toward him; behind "
            "something. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r113-b15", "out": "s15-what-is-this-that-thou.jpeg", "seg": "jv13",
        "window": "80.62-82.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["EVE"],
        "narration": "What is this that thou hast done?",
        "must_show": "SCRIPTURE-EXACT: the question to the woman — her face in the gold light receiving it: sorrow, not interrogation-terror; the gentle asking that draws truth.",
        "must_not_show": "ABSOLUTE: no figure of God; her long hair and a GREEN FIG-LEAF girdle cover her if the torso shows — never rags or cloth; her dignity held — a woman about to tell the truth.",
        "scene": (
            "The question comes to her "
            "gently and lands with all "
            "its weight: the woman's "
            "face in the golden light, "
            "her long hair drawn "
            "around her like a "
            "mantle, eyes wet and "
            "level — WHAT IS THIS "
            "THAT THOU HAST DONE — "
            "not a prosecutor's trap "
            "but a Father's sorrowing "
            "invitation to say it "
            "herself, out loud, the "
            "way truth heals only "
            "when it comes from the "
            "one who hid it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b16", "out": "s16-the-serpent-beguiled-me-and.jpeg", "seg": "w13 + n6",
        "window": "84.27-90.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["EVE"],
        "narration": (
            "The serpent beguiled me, and I did eat. I was deceived, she "
            "said, and I ate."
        ),
        "must_show": "SCRIPTURE-EXACT: her confession — close on the woman speaking it plainly: deceived, and owning her part anyway; the truth said whole; NO serpent shown.",
        "must_not_show": "ABSOLUTE: no serpent anywhere in frame — it lives only in her words; her long hair and a GREEN FIG-LEAF girdle cover her if the torso shows — never rags or cloth; her face honest, unbroken.",
        "scene": (
            "Close on the second "
            "confession: the woman's "
            "face steadying as she "
            "says it whole — I WAS "
            "DECEIVED — the truth of "
            "that real and said — AND "
            "I DID EAT — her own part "
            "owned right beside it, "
            "not hidden behind the "
            "deceiving — a woman "
            "standing in the gold "
            "light telling the whole "
            "shape of what happened, "
            "the lie that came to "
            "her and the hand that "
            "was still hers — truth, "
            "complete at last. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b17", "out": "s17-no-excuses-left-just-the.jpeg", "seg": "n6",
        "window": "90.69-95.07", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE", "GOD"],
        "narration": "No excuses left — just the truth, spoken out loud at last.",
        "must_show": "the emptied-out honesty — the two standing plainly before the embodied Father (per the GOD lock) in the clearing, everything told; the strange relief of no more hiding visible in their loosened postures.",
        "must_not_show": "no halo, glow or rim-light on the Father; the two wear GREEN FIG-LEAF girdles — never rags or cloth; on solid ground, never on water; the relief SUBTLE — spent, honest, lighter.",
        "scene": (
            "When the last excuse is "
            "spent, something almost "
            "like rest arrives: the two "
            "standing plainly in the "
            "clearing's gold, nothing "
            "left untold, hands empty "
            "at their sides at last — "
            "and in the loosened "
            "shoulders, under all the "
            "fear of what must come, "
            "the strange lightness "
            "known to everyone who "
            "has ever finally said "
            "the whole thing out "
            "loud: the hiding was "
            "heavier than the truth "
            "turned out to be. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b18", "out": "s18-there-were-consequences-there-always.jpeg", "seg": "n6",
        "window": "95.07-103.08", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE"],
        "narration": (
            "There were consequences; there always are. The easy garden was "
            "behind them now, and a hard world lay ahead."
        ),
        "must_show": "the two worlds — from the garden's edge: behind, the deep green ease; ahead through the gap, the harder dusk country of thorn and stone; the couple between them.",
        "must_not_show": "ABSOLUTE: no figure of God, no flaming sword — the hard world stated by landscape alone; the couple wear GREEN FIG-LEAF girdles — never rags or cloth (they are not clothed in the leather coats until after this).",
        "scene": (
            "From the garden's edge, the camera behind the two "
            "standing figures at the gap, the "
            "two geographies of the "
            "sentence face each other: "
            "at their backs the deep "
            "green ease of everything "
            "they knew — fruit heavy, "
            "stream running, evening "
            "gold — and ahead through "
            "the gap in the trees, "
            "the other country at "
            "dusk: stony ground "
            "climbing away, thorn "
            "scrub, a wind with an "
            "edge in it — and between "
            "the two worlds, small "
            "and holding hands, the "
            "people who traded one "
            "for the other. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b19", "out": "s19-they-stood-there-ashamed-waiting.jpeg", "seg": "n6",
        "window": "103.08-107.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["ADAM", "EVE"],
        "narration": "They stood there, ashamed, waiting for the end of everything.",
        "must_show": "the braced-for-ending — the two with heads bowed and eyes shut in the dusk light, hands gripped together, braced for annihilation.",
        "must_not_show": "ABSOLUTE: no figure of God; the two wear GREEN FIG-LEAF girdles — never rags or cloth; on solid ground, never on water; the bracing TOTAL — two people expecting the worst sentence there is.",
        "scene": (
            "They stand braced for the "
            "end of the world they "
            "broke: heads bowed in the "
            "dusk light, eyes shut, "
            "her hand gripped white "
            "inside his — two small "
            "people who have heard "
            "the consequences and are "
            "now waiting, trembling, "
            "for the only thing shame "
            "can imagine coming next: "
            "the unmaking, the wrath, "
            "the end of everything — "
            "certain of it, braced "
            "for it, and about to be "
            "wrong. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b20", "out": "s20-and-instead-god-did-something.jpeg", "seg": "n7",
        "window": "108.20-112.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "GOD"],
        "narration": (
            "And instead, God did something they never expected. He made "
            "them clothes."
        ),
        "must_show": "SCRIPTURE-EXACT: the mercy — the embodied Father (per the GOD lock) holding out two well-made coats of soft dark leather to the couple, warm evening light on the garments; kindness where a sentence was expected.",
        "must_not_show": "no halo, glow or rim-light on the Father; the couple still wear their GREEN FIG-LEAF girdles here (they receive the leather coats in the next beats) — never rags or cloth; nothing immodest; the gesture GENTLE — a father clothing his children.",
        "scene": (
            "What waits for them is not "
            "the end: the Father himself, "
            "white-robed, white-haired and "
            "full-bearded, stands "
            "in the last warm light and "
            "holds out to them two garments — "
            "coats of soft dark "
            "leather, well made, "
            "man-sized and woman-"
            "sized, measured for "
            "their wearers exactly — "
            "the mercy plain on his "
            "kind face, resting in the "
            "gold like a sentence "
            "commuted: clothing, "
            "where annihilation was "
            "expected. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r113-b21", "out": "s21-with-his-own-care-he.jpeg", "seg": "n7",
        "window": "112.24-123.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["ADAM", "EVE"],
        "narration": (
            "With his own care he covered their shame — better coverings "
            "than the leaves they had grabbed for themselves — because they "
            "could not fix what they had broken, but he could cover them in "
            "it."
        ),
        "must_show": "the clothing received — the two now dressed in the dark leather coats, the wilted fig leaves discarded at their feet; her face undone by the kindness; covered, by him.",
        "must_not_show": "ABSOLUTE: no figure of God; the CONTRAST at their feet — crushed leaves versus true garments.",
        "scene": (
            "They put on what was made "
            "for them: the dark soft "
            "coats settling over their "
            "shoulders like a kept "
            "promise, fitting exactly — "
            "and at their feet, "
            "discarded, the pitiful "
            "wilted fig-leaf girdles "
            "of their own panicked "
            "making — the woman's face "
            "undone entirely by the "
            "kindness of it, the man "
            "smoothing the leather "
            "with a trembling hand — "
            "covered, not by their "
            "scrambling, but by the "
            "very One they hid from. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b22", "out": "s22-not-how-dare-you.jpeg", "seg": "n5",
        "window": "49.42-50.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "Not, how dare you.",
        "must_show": "the withheld thunder — the garden's light holding gentle in the clearing where wrath would stand: the question's tone as weather; nothing scorched anywhere.",
        "must_not_show": "ABSOLUTE: no figure; NO storm, no darkening — gentleness where thunder was earned.",
        "scene": (
            "The frame listens for "
            "thunder and hears none: "
            "the clearing where wrath "
            "had every right to stand "
            "holds only the gentle "
            "gold of the usual "
            "evening — no darkening "
            "sky, no scorched grass, "
            "no wind bent in anger — "
            "the first sin in the "
            "history of the world, "
            "answered not with HOW "
            "DARE YOU but with a "
            "question soft enough "
            "for a hiding child to "
            "answer — mercy, setting "
            "its tone before its "
            "terms. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b23", "out": "s23-then-he-sent-them-out.jpeg", "seg": "n8",
        "window": "123.69-129.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE", "GOD"],
        "narration": (
            "Then he sent them out into the wide world — but not naked, and "
            "not alone, and not without a promise."
        ),
        "must_show": "SCRIPTURE-EXACT: the sending — the leather-clothed two walking out through the garden's gap into the dusk country hand in hand, and at the gap behind them the embodied Father (per the GOD lock) watching them go, a hand raised toward them in blessing.",
        "must_not_show": "no halo, glow, rim-light or flaming sword; the exile's mercy carried by the watching Father and the held hands.",
        "scene": (
            "The exile leaves like a "
            "sending, not a casting "
            "out: the two walking "
            "through the gap in the "
            "trees into the stony dusk "
            "country hand in hand — "
            "clothed in the coats he "
            "made, provisioned with a "
            "promise neither fully "
            "understands — and at the "
            "gap behind them, white-"
            "robed in the garden's warm "
            "light, the Father himself "
            "watching his children go, "
            "one hand lifted after them "
            "in blessing. "
            "Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b24", "out": "s24-clothed-by-the-very-one.jpeg", "seg": "n8 + n9",
        "window": "129.83-135.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["ADAM", "EVE"],
        "narration": (
            "Clothed by the very One they had run from. That is the God of "
            "the very first story."
        ),
        "must_show": "the summary held — close on the two walking in their made coats, faces forward into the dusk: fear replaced by a chastened, held steadiness; the first story's God legible on them.",
        "must_not_show": "ABSOLUTE: no figure of God; their steadiness NEW — sobered, covered, not crushed.",
        "scene": (
            "Close on what the first "
            "story leaves its people "
            "wearing: the two walking "
            "forward into the dusk in "
            "coats cut by the hands "
            "they hid from — faces "
            "sobered and steady, fear "
            "traded for something "
            "harder-won: the knowledge "
            "of being covered by the "
            "One they wronged — every "
            "step in leather that "
            "preaches better than "
            "words what kind of God "
            "wrote the opening chapter: "
            "one who clothes his "
            "runaways for the road. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b25", "out": "s25-not-one-who-waits-for.jpeg", "seg": "n9",
        "window": "135.35-139.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "Not one who waits for you to clean yourself up and come find him.",
        "must_show": "the not-waiting — an empty landscape beat: the garden path itself at evening, open and unbarred, running out through the gap toward the thorn-country; the road as the visual of a God who travels toward you, not one who waits.",
        "must_not_show": "no figure here (a pure path/landscape beat before the closing figure); no halo or personified light-as-God — just the open evening road.",
        "scene": (
            "The path settles the "
            "doctrine by its shape: "
            "the garden way at "
            "evening, open and "
            "unbarred — the road not "
            "ending at some far gate "
            "for the cleaned-up to "
            "reach, "
            "but running OUTWARD along "
            "the stones, through the "
            "gap, out into the "
            "thorn-country where the "
            "hiders went — the road "
            "itself drawn as a "
            "direction: not the "
            "destination of the "
            "worthy, but the way a "
            "God takes toward the "
            "lost. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b26", "out": "s26-one-who-comes-walking-through.jpeg", "seg": "n9",
        "window": "139.24-147.40", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN", "GOD"],
        "narration": (
            "One who comes walking through the garden in the cool of the "
            "evening, calling, still calling — where are you? — because he "
            "wants you back."
        ),
        "must_show": "the closing image — the garden in the cool of evening with the embodied Father (per the GOD lock) walking down the path toward the viewer's side of the frame, leaves stirring; the question still going out; the seeking God shown as a real man who comes.",
        "must_not_show": "no halo, glow, shape-shifting or rim-light — a real man walking to the last frame; the call aimed OUT of the picture.",
        "scene": (
            "The closing frame is still happening, the camera at "
            "the path's side taking his walk in profile: the garden "
            "in the cool of the evening, and down its path the "
            "white-robed Father comes walking as he always "
            "has, leaves stirring at his passing, his kind "
            "face turned along the way ahead — still walking, "
            "still asking the oldest question in love: WHERE "
            "ART THOU. "
            "you back. Every figure "
            "has two arms, two hands "
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
    "GARDEN": "PLACE-REF/garden.jpeg",  # build-113-where-art-thou s01-in-the-beginning-there-was (manual)
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "ADAM": "CAST-REF-V2/adam.jpeg",
    "EVE": "CAST-REF-V2/eve.jpeg",
    "GOD": "CAST-REF-V2/god.jpeg",
}
