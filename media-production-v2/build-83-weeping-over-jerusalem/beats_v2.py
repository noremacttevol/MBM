#!/usr/bin/env python3
"""V2 beat map — row 83, build-83-weeping-over-jerusalem (Luke 19:41-44).

COVERAGE: 14 pictures over 78.2 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 19:41-44 KJV):
  v37   context: the DESCENT OF THE MOUNT OF OLIVES, the triumphal-
        entry crowd around him — pilgrims, spread garments, praise.
  v41   "And when he was come near, he BEHELD THE CITY, and WEPT over
        it." — the city opens below from the descent road: walls,
        gates, and the temple gleaming across the Kidron valley.
  v42   "If thou hadst known, even thou, at least in THIS THY DAY, the
        things which belong unto THY PEACE! but now they are HID from
        thine eyes." — he addresses the CITY itself, tenderly.
  v43-44 the coming siege — NEVER PAINTED (city-destruction-off-screen
        law): the ruin exists only as foreknowledge in his face; the
        city itself is shown intact, sunlit, beautiful and unaware.

TIME OF DAY: one bright spring morning throughout — the Passover-week
entry; clear sun on the limestone city and the temple.

CONTENT-CARE: no row flags. City destruction OFF-SCREEN throughout —
no armies, siegeworks, fire or rubble in any frame; the grief is
love's, carried in his wet eyes over an intact and shining city.
Jesus's weeping shown with full dignity — silent tears on a composed
face, never contorted.

CHANGING CONDITION (kept OUT of the locks): the procession's noise —
full-throated behind him, then hushing as he stops; and his face —
travelling, then halted, then wet.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "OVERLOOK": (
        "OVERLOOK LOCK: the descent road of the Mount of Olives — a "
        "pale dirt road curving down between grey-green olive trees, "
        "and below across the Kidron valley the whole city of "
        "Jerusalem opened out: pale limestone walls and gates, packed "
        "rooftops, and the great temple with its gold trim shining at "
        "the centre. The same road, trees and skyline throughout."
    ),
    "CROWD": (
        "CROWD LOCK: the festival procession — pilgrims in DARK "
        "EARTH-BROWN, RUST and DEEP OLIVE robes (never cream, never "
        "white), carrying cut palm branches, some with cloaks over "
        "their arms from spreading them on the road; joyful, dusty, "
        "many."
    ),
}

REF = True

# AUDIO-FIX (AUDIO-FIX session, Machine A, 2026-08-06): the V1 mp4
# luke-19_weeping-over-jerusalem.mp4 is out of date vs this build's narration —
# assert_v1_final_is_current's runtime tripwire fires (|Δ| ~2.2s between the mp4
# and the summed segment timeline), so the AUDIO LOCK refuses to copy the stale
# stream. Segment-ID parity with make_narration.py is exact (10/10: n0,n1a,n1b,
# s41,n2,n2b,n3a,n3b,j1,card), so rebuild the track from these segments at the
# extract offsets instead of copying the stale mp4. $0 — nothing re-voiced,
# nothing re-timed; V1 stays read-only. Same mechanism as the shipped row-69 fix.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r083-b01", "out": "s01-as-jesus-came-over-the.jpeg", "seg": "n0",
        "window": "0.40-8.25", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK", "CROWD"],
        "narration": (
            "As Jesus came over the hill and the whole city of Jerusalem "
            "opened up in front of him, he did something the crowds didn't "
            "expect."
        ),
        "must_show": "SCRIPTURE-EXACT: the reveal — Jesus cresting the descent road with the singing procession, and the whole sunlit city opening below: walls, gates, the shining temple.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the city INTACT and beautiful — no hint of ruin anywhere in the panorama.",
        "scene": (
            "The road crests between the olive trees, the camera "
            "beside the road behind the procession's shoulders so "
            "every walker moves AWAY from the lens TOWARD the "
            "revealed city, "
            "trees and the world opens: below "
            "the descending procession the "
            "whole city spreads sunlit in the "
            "spring morning — pale walls and "
            "crowded rooftops, gates streaming "
            "with festival traffic, the temple "
            "burning gold-trimmed white at the "
            "centre of it all — while around "
            "Jesus the palm-waving crowd sings "
            "on, not yet noticing what has "
            "begun to happen to his face. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r083-b02", "out": "s02-he-stopped.jpeg", "seg": "n1a",
        "window": "9.90-10.57", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK", "CROWD"],
        "narration": "He stopped.",
        "must_show": "the halt — Jesus stopped dead in the road at the overlook, the procession bunching and stumbling around his stillness; motion breaking against a stationary man.",
        "must_not_show": "no halo, glare or rim-light; the stop ABRUPT — bodies still flowing past and around him, branches lowering in confusion.",
        "scene": (
            "In the middle of the moving "
            "celebration Jesus stops dead — "
            "planted in the pale road with the "
            "city below him — and the "
            "procession breaks around his "
            "stillness like water round a "
            "stone: pilgrims stumbling half a "
            "step, palm branches faltering "
            "mid-wave, the song fraying at its "
            "edges as row after row discovers "
            "that the man they are escorting "
            "into the city is no longer "
            "walking toward it. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r083-b03", "out": "s03-luke-writes-it-in-one.jpeg", "seg": "n1a",
        "window": "11.13-13.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK"],
        "narration": "Luke writes it in one plain sentence:",
        "must_show": "the hush before the sentence — close on Jesus in profile against the distant sunlit city, still and beholding; the moment the record keeps.",
        "must_not_show": "no halo, glare or rim-light; the profile QUIET — a man and a city regarding each other across a valley.",
        "scene": (
            "Close on Jesus in profile at the "
            "road's edge, the sunlit city laid "
            "out small and shining beyond him "
            "— a man and the city of his "
            "people regarding each other "
            "across the Kidron's air, the "
            "festival noise dropping away "
            "behind his stillness — the exact "
            "wordless moment a physician "
            "writing years later would set "
            "down in one plain line. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r083-b04", "out": "s04-and-when-he-was-come.jpeg", "seg": "s41",
        "window": "15.04-18.71", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK"],
        "narration": "And when he was come near, he beheld the city, and wept over it.",
        "must_show": "SCRIPTURE-EXACT: the weeping — close on Jesus's face: silent tears running into his beard, eyes open and fixed on the city; grief with complete dignity.",
        "must_not_show": "no halo, glare or rim-light; the face COMPOSED — wet eyes and running tears on steady features, never contorted or theatrical.",
        "scene": (
            "Close on his face as the record "
            "says it happened: the warm brown "
            "eyes open and fixed on the "
            "shining city, and the tears "
            "simply coming — running silent "
            "down the cheekbones into the "
            "dark beard, one after another, on "
            "features that do not crumple — "
            "the composed weeping of a strong "
            "man who is not surprised by his "
            "own grief, on the happiest road "
            "of the happiest week his friends "
            "could remember. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r083-b05", "out": "s05-not-for-himself.jpeg", "seg": "n1b",
        "window": "23.05-24.45", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK"],
        "narration": "Not for himself.",
        "must_show": "the direction of the grief — his wet eyes aimed OUTWARD at the city, nothing inward in the face; sorrow pointed entirely away from its own bearer.",
        "must_not_show": "no halo, glare or rim-light; NO self-pity readable anywhere — the gaze outbound, the grief spent on others.",
        "scene": (
            "The frame stays on the wet eyes "
            "and follows where they aim: "
            "outward, wholly outward, across "
            "the valley to the walls and the "
            "rooftops and the gold-trimmed "
            "temple — nothing in the face bent "
            "back toward its own coming week, "
            "though he knows that too — every "
            "tear on it posted outbound, spent "
            "on a city that has not asked for "
            "them and does not know they are "
            "falling. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r083-b06", "out": "s06-the-peace-they-had-been.jpeg", "seg": "n2",
        "window": "27.09-33.17", "wide": True, "jesus": False, "ref": False,
        "locks": ["OVERLOOK"],
        "narration": (
            "The peace they had been aching for had walked right up to their "
            "gates — and the city was too busy to see it."
        ),
        "must_show": "the blindness — the city's gate below at full boil: merchants, pilgrims, soldiers, loads and animals streaming through; every head down in its business, none turned to the hill.",
        "must_not_show": "no halo, glare or rim-light; NOBODY at the gate looking up toward the Mount — busyness as the whole tragedy.",
        "scene": (
            "Down at the great gate, the camera high on the "
            "overlook so the gate traffic crosses in profile far "
            "below, the city "
            "boils with its morning: merchants "
            "hauling festival goods, pilgrims "
            "pressing in with lambs and "
            "bundles, a bored soldier waving "
            "the traffic through, donkeys and "
            "handcarts and hurry — hundreds of "
            "heads and every one of them down "
            "in its business, not one face "
            "turned up toward the olive-green "
            "hill where the peace they pray "
            "for weekly stands weeping at the "
            "view of them. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r083-b07", "out": "s07-if-thou-hadst-known-even.jpeg", "seg": "j1",
        "window": "34.80-42.09", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK"],
        "narration": (
            "If thou hadst known, even thou, at least in this thy day, the "
            "things which belong unto thy peace!"
        ),
        "must_show": "SCRIPTURE-EXACT: the address — Jesus speaking TO the city across the valley, a hand lifted toward it; a person spoken to, not a landscape described.",
        "must_not_show": "no halo, glare or rim-light; the address TENDER — the reach of the hand pleading, never accusing.",
        "scene": (
            "Jesus speaks across the valley to "
            "the city as to a person — IF THOU "
            "HADST KNOWN, EVEN THOU — one hand "
            "lifting toward the sunlit walls "
            "in the reaching half-open way you "
            "extend a hand to someone loved "
            "and leaving — the wet eyes and "
            "the pleading palm holding the "
            "whole skyline like a face between "
            "two hands, this thy day passing "
            "through the morning light even as "
            "he names it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r083-b08", "out": "s08-but-now-they-are-hid.jpeg", "seg": "j1",
        "window": "42.09-45.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["OVERLOOK"],
        "narration": "but now they are hid from thine eyes.",
        "must_show": "SCRIPTURE-EXACT: the hiddenness — a rooftop detail of the busy city: faces mid-task, mid-argument, mid-errand; the great thing on the hill outside every field of view.",
        "must_not_show": "no halo, glare or rim-light; nothing supernatural about the hiding — just ordinary attention aimed everywhere else.",
        "scene": (
            "On a crowded rooftop inside the "
            "walls the morning does its "
            "hiding in plain sight: a woman "
            "pinning wash with her back to the "
            "east, two men arguing over a "
            "ledger, a boy chasing pigeons "
            "along the parapet — every field "
            "of view in the city angled a few "
            "degrees away from the one hill "
            "that matters this morning — "
            "nothing veiled, nothing dimmed, "
            "only attention, spent elsewhere "
            "down to the last pair of eyes. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r083-b09", "out": "s09-he-came-close-he-looked.jpeg", "seg": "n1b",
        "window": "20.34-23.05", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK", "CROWD"],
        "narration": "He came close, he looked at the city, and he cried over it.",
        "must_show": "the whole tableau — Jesus at the overlook weeping over the panorama, the halted procession hushed behind him, palm branches lowered; celebration turned vigil.",
        "must_not_show": "no halo, glare or rim-light; the crowd's hush VISIBLE — branches down, faces uncertain, joy suspended around his tears.",
        "scene": (
            "The wide road holds the strange "
            "tableau: Jesus at the overlook's "
            "edge with the tears bright on his "
            "face and the whole sunlit city "
            "below him — and behind him the "
            "celebration standing suspended, "
            "palm branches lowered to trail in "
            "the dust, pilgrims exchanging "
            "uncertain looks over the sudden "
            "quiet — a parade discovering that "
            "its king has stopped to weep at "
            "the view of everything they "
            "thought he was coming to take. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r083-b10", "out": "s10-if-only-you-had-known.jpeg", "seg": "n2b",
        "window": "46.78-54.85", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK"],
        "narration": (
            "If only you had known — even you, even today — what would have "
            "brought you peace. He is not scolding the city."
        ),
        "must_show": "the tone made visible — close on his face mid-address: tenderness through the tears, nothing of the scold in brow or mouth; longing, not lecture.",
        "must_not_show": "no halo, glare or rim-light; NO anger lines, no pointed finger — the face grieving FOR, never at.",
        "scene": (
            "Close on the speaking face: the "
            "tears still coming, and through "
            "them not one line of the scold — "
            "no hardened brow, no jut of "
            "accusation — only the aching "
            "tenderness of the words even "
            "thou, even today, shaped by a "
            "mouth that would rather be "
            "blessing — a face grieving FOR "
            "its beloved and not once at her, "
            "though it knows everything. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r083-b11", "out": "s11-he-is-talking-to-it.jpeg", "seg": "n2b",
        "window": "54.85-62.06", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK"],
        "narration": (
            "He is talking to it the way you talk to someone you love who is "
            "about to walk past the one thing that would have saved them."
        ),
        "must_show": "the love made spatial — Jesus and the city held in one frame across the valley's air: the reaching figure on the hill, the beautiful oblivious city; nearness and missing in one image.",
        "must_not_show": "no halo, glare or rim-light; the composition INTIMATE despite the distance — the valley's gap the whole heartbreak.",
        "scene": (
            "The frame holds both of them at once, the camera off "
            "to the side so the man in profile faces the far city "
            "across the whole valley, "
            "once across the valley's bright "
            "air: on the hill the single "
            "reaching figure with wet eyes and "
            "an open hand, and beyond the gap "
            "the city entire — gorgeous, "
            "gold-crowned, streaming with its "
            "own morning — the two of them "
            "closer than they have ever been "
            "and the little valley between "
            "them wide as the missing itself: "
            "love within sight of its answer, "
            "walking past. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r083-b12", "out": "s12-for-them.jpeg", "seg": "n1b",
        "window": "24.45-25.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["OVERLOOK"],
        "narration": "For them.",
        "must_show": "the them — a warm close detail inside the city: children playing on a stair, a grandmother at a doorway, ordinary faces in the sun; the people the tears are for.",
        "must_not_show": "no halo, glare or rim-light; the people utterly ORDINARY and endearing — the preciousness of the wept-for made visible.",
        "scene": (
            "Inside the walls, close and warm: "
            "two children racing up a worn "
            "stone stair with a hoop, a "
            "grandmother shelling beans in her "
            "doorway's sun, a young father "
            "lifting his daughter to see over "
            "the festival crowd — the them of "
            "the tears, going about their "
            "sweet unremarkable morning, each "
            "face exactly the kind a man on a "
            "far hill might weep over without "
            "their ever knowing. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r083-b13", "out": "s13-he-could-see-what-was.jpeg", "seg": "n3a",
        "window": "63.73-69.72", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK"],
        "narration": (
            "He could see what was coming for the city he loved — armies and "
            "ruin, a generation away."
        ),
        "must_show": "the foreknowledge — close on his eyes over the INTACT sunlit city: the seeing carried entirely in the grieved gaze; nothing of the ruin painted anywhere.",
        "must_not_show": "ABSOLUTE (off-screen law): no armies, siegeworks, fire, smoke or rubble in any part of the frame — the city whole and shining; the future exists only in his face.",
        "scene": (
            "Close on the eyes that see "
            "further than the view: below "
            "them the city lies whole and "
            "shining in the spring sun — "
            "walls unbroken, temple blazing "
            "white and gold, rooftops full of "
            "ordinary morning — and in the "
            "wet steady gaze above it, and "
            "nowhere else, the weight of what "
            "a generation will bring rests "
            "like a stone held silently, the "
            "grief of a man reading the last "
            "chapter over the heads of people "
            "still living in the first. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r083-b14", "out": "s14-his-tears-anger-they-were.jpeg", "seg": "n3b",
        "window": "71.42-76.85", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK", "CROWD"],
        "narration": (
            "His tears weren't anger. They were the grief of love that sees "
            "exactly what could have been."
        ),
        "must_show": "the closing image — the full scene at rest: the weeping Jesus above the radiant city, the hushed procession behind, the morning beautiful and unbroken; love's grief in its whole landscape.",
        "must_not_show": "no halo, glare or rim-light; the city STILL radiant to the last frame — what could have been, shining in plain sight.",
        "scene": (
            "The closing frame widens, the camera behind the "
            "halted procession's backs, over the "
            "whole morning: the weeping figure "
            "small at the overlook, the hushed "
            "palm-bearing crowd banked behind "
            "him on the pale road, and below "
            "them all the city radiant in the "
            "spring light — gates streaming, "
            "temple shining, every stone of "
            "what could have been standing "
            "beautiful and within reach — and "
            "over it the tears of the one "
            "person present who can see both "
            "endings from here. Every figure "
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
}
# === end PLACE-PLATES ===
