#!/usr/bin/env python3
"""V2 beat map — row 28, build-28-hidden-treasure (Matthew 13:44).

COVERAGE: 16 pictures over 90.2 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 13:44 KJV):
  v44   "Again, the kingdom of heaven is like unto TREASURE HID IN A FIELD;
        the which when a man hath FOUND, he HIDETH, and FOR JOY THEREOF
        goeth and SELLETH ALL THAT HE HATH, and BUYETH THAT FIELD."
        — this parable was spoken IN THE HOUSE to the disciples (Matthew
          13:36 'Jesus went into the house: and his disciples came unto
          him'; v44 follows). Row 25 staged that room wide from outside the
          circle, so THIS build's frame beat (b01) is a CLOSE shot of Jesus
          in the same kind of room, framed past a disciple's shoulder —
          different composition, no repeat.
        — the finder HIDES it again before buying: covering it back over is
          a beat, done quickly and quietly.
        — the selling is FOR JOY — the narration hammers it (b15/b16): he
          does not grieve what he sells. Every selling face is glad.
        — he buys THE FIELD (not the treasure directly): the purchase beat
          is coins for a field, sealed properly before witnesses.

TIME OF DAY: the frame beat is warm afternoon window light (the Matthew 13
house). The parable runs a clean day-arc: ordinary bright MORNING for the
digging and the find; MIDDAY for the hurry home and the selling; LATE
AFTERNOON for the purchase of the field; and warm SUNSET GOLD for the
final joy beats — a day that ends with everything given and everything
gained. The sunset colouring in b14-b16 is deliberate and correct.

CONTENT-CARE: row 28 has no flag in §3. Nothing sensitive. The treasure is
an old buried pottery jar and wooden chest of ancient coins — no modern
objects.

CHANGING CONDITION (kept OUT of the locks): the man's possessions — tools,
cloak-bundle, house goods — leave him beat by beat, and his state moves
from work-weary to lit-up joy. Neither is locked.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "DIGGER": (
        "DIGGER LOCK: the hired worker is the same man in every shot — "
        "early thirties, lean and strong, with short curly black hair, a "
        "close-cropped dark beard, quick bright dark eyes and sun-browned "
        "skin. He wears a plain DARK OLIVE-GREY work tunic kilted to the "
        "knee with a rope belt, and worn sandals (never cream, never "
        "white). His face is shown clearly."
    ),
    "TREASURE": (
        "TREASURE LOCK: the treasure is the same in every shot — a small "
        "iron-banded wooden chest, its lid split with age, packed with old "
        "coins of dull gold and dark silver, a few strings of carnelian "
        "and blue stone beads, and one broken-lidded clay jar of more "
        "coins beside it. Old, buried things — dusty, dull-metalled, "
        "ancient; never bright modern gold."
    ),
    "FIELD": (
        "FIELD LOCK: a plain rectangular field on the edge of village land "
        "— rough half-cleared earth with thistle patches, a single broken "
        "olive stump near its middle, a low boundary bank of stones and "
        "dry grass on two sides, and a worn footpath passing along one "
        "edge toward the village's flat rooftops in the distance."
    ),
    "VILLAGE": (
        "VILLAGE LOCK: the village street — packed dry earth between "
        "honey-stone houses with low doorways, awnings of faded cloth, a "
        "communal well at the widening of the street, and workshop "
        "benches under the eaves. The same street, well and awnings in "
        "every village beat."
    ),
    "HOUSE-ROOM": (
        "HOUSE ROOM LOCK: the main room of a Capernaum house — thick "
        "honey-stone walls, one deep-set window throwing a broad slant of "
        "warm afternoon light, rush mats and low cushions on a "
        "beaten-earth floor, and a shelf of clay vessels in shadow."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r028-b01", "out": "s01-jesus-once-told-a-very.jpeg", "seg": "n0",
        "window": "0.28-4.83", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE-ROOM"],
        "narration": "Jesus once told a very short story — about a man, and a field.",
        "must_show": "SCRIPTURE-EXACT (v36 — in the house): a close shot of Jesus seated in the warm room, framed past the dark shoulder of a listening disciple, beginning the story.",
        "must_not_show": "no halo, glare or rim-light on Jesus; intimate and close — this is the private house teaching, not a crowd.",
        "scene": (
            "Inside the warm stone room, close: past the soft dark "
            "shoulder of a disciple seated in the near foreground, Jesus "
            "sits in the broad slant of afternoon window light, leaning "
            "forward with his forearms on his knees, hands open, his face "
            "warm with the particular pleasure of a storyteller who knows "
            "the story is a good one. The honey-stone wall behind him "
            "holds the light. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r028-b02", "out": "s02-he-was-a-hired-worker.jpeg", "seg": "n1",
        "window": "5.42-9.51", "wide": True, "jesus": False, "ref": False,
        "locks": ["DIGGER", "FIELD"],
        "narration": (
            "He was a hired worker, out digging in a field that wasn't even his "
            "own."
        ),
        "must_show": "the ordinary labour — the worker alone in the rough field in plain morning light, spade in the ground, half a trench already dug behind him.",
        "must_not_show": "no halo, glare or rim-light; nothing special anywhere — the most ordinary working picture in the row.",
        "scene": (
            "Plain bright morning over the rough half-cleared field: the "
            "lean young worker drives his wooden-handled iron spade into "
            "the stony earth with one foot on its shoulder, a shallow "
            "trench running crooked behind him past the broken olive "
            "stump, his water-skin and folded cloak dropped on the "
            "boundary bank. The village rooftops sit small and far along "
            "the footpath. An ordinary man on an ordinary day. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r028-b03", "out": "s03-and-on-one-ordinary-day.jpeg", "seg": "n2 + n3",
        "window": "10.14-17.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["DIGGER", "TREASURE", "FIELD"],
        "narration": (
            "And on one ordinary day, his spade struck something hard, buried "
            "in the ground. He cleared away the dirt — and there it was."
        ),
        "must_show": "SCRIPTURE-EXACT: the strike and the clearing — the worker on his knees in the trench, both hands sweeping soil off the just-showing iron-banded chest lid.",
        "must_not_show": "no halo, glare or rim-light; only the LID showing yet — the chest still mostly buried; his face arrested mid-motion.",
        "scene": (
            "The worker is down on both knees in his shallow trench, the "
            "spade dropped flat beside him, both hands frozen mid-sweep "
            "in the loose earth — where the dirt has just come away from "
            "a flat, hard, iron-banded wooden lid, one dark corner of it "
            "bared under his fingers, the rest still buried. His eyes are "
            "locked on it, lips parted, everything about him stopped. "
            "Bright plain morning light overhead. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r028-b04", "out": "s04-a-treasure-hidden-forgotten-and.jpeg", "seg": "n3",
        "window": "17.86-24.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["DIGGER", "TREASURE"],
        "narration": (
            "A treasure. Hidden, forgotten, and worth more than he had ever "
            "seen in his life."
        ),
        "must_show": "SCRIPTURE-EXACT: the open chest in the earth — old dull-gold and dark-silver coins, bead strings, the broken jar beside it — and the worker's stunned face lit from below-frame attention, not light.",
        "must_not_show": "no halo, glare or rim-light; the coins are OLD and dull-metalled, not bright modern gold; his face is shock, not greed.",
        "scene": (
            "Close down into the trench: the split lid levered back on "
            "the small iron-banded chest, and inside it a packed mass of "
            "old coins in dull gold and darkened silver, strings of "
            "carnelian and blue stone beads slumped across them, the "
            "broken-lidded clay jar tipped beside it spilling more — and "
            "above the open chest the worker's stunned young face, "
            "staring down, one earth-stained hand gripping the trench "
            "edge. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r028-b05", "out": "s05-his-heart-pounded-quickly-quietly.jpeg", "seg": "n4",
        "window": "24.55-29.94", "wide": True, "jesus": False, "ref": False,
        "locks": ["DIGGER", "FIELD"],
        "narration": (
            "His heart pounded. Quickly, quietly, he covered it back over — and "
            "told no one."
        ),
        "must_show": "SCRIPTURE-EXACT: the re-hiding — earth being pushed back over the buried spot with both forearms, his head up and checking the empty footpath.",
        "must_not_show": "no halo, glare or rim-light; the chest is already fully covered or nearly so — secrecy, urgency, no one anywhere in sight.",
        "scene": (
            "The worker kneels low over the trench sweeping loose earth "
            "back across the buried spot with both forearms at once, the "
            "ground already levelled over the chest, his head turned up "
            "and sideways mid-motion to check the footpath along the "
            "field's edge — which runs empty to the far village under the "
            "plain morning sky. Urgency in every line of him, and no "
            "witness but the broken olive stump. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r028-b06", "out": "s06-his-house.jpeg", "seg": "n6",
        "window": "51.07-51.71", "wide": True, "jesus": False, "ref": False,
        "locks": ["DIGGER", "VILLAGE"],
        "narration": "His house.",
        "must_show": "the house being given over — the worker pressing his door key-peg into a buyer's hand at the low doorway of a small house, GLAD-faced.",
        "must_not_show": "no halo, glare or rim-light; his face carries no grief — bright, decided gladness; the buyer is the puzzled one.",
        "scene": (
            "At the low doorway of a small honey-stone house on the "
            "village street the worker presses the wooden key-peg of his "
            "own door into the hands of an older buyer, holding the man's "
            "hands closed over it with both of his — and the seller is "
            "the one beaming, bright and decided, while the buyer's face "
            "is caught between satisfaction and puzzlement at such an "
            "eager bargain. Midday light down the street. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r028-b07", "out": "s07-again-the-kingdom-of-heaven.jpeg", "seg": "j1",
        "window": "30.50-37.93", "wide": True, "jesus": False, "ref": False,
        "locks": ["DIGGER", "FIELD"],
        "narration": (
            "Again, the kingdom of heaven is like unto treasure hid in a field; "
            "the which when a man hath found, he hideth,"
        ),
        "must_show": "SCRIPTURE-EXACT: the hidden spot made ordinary again — the worker standing OVER the smoothed ground, pressing it flat underfoot, the field looking like nothing at all around him.",
        "must_not_show": "no halo, glare or rim-light; no visible trace of the chest — the frame's secret is that the best thing in it cannot be seen.",
        "scene": (
            "The worker stands over the smoothed patch of earth in the "
            "middle of the rough field, pressing it flat with one "
            "sandalled foot, spade over his shoulder, casual to any "
            "passing eye — while everything in his lowered glance says he "
            "knows exactly what is under the sole of his foot. Around "
            "him the field lies plain and thistled and worthless-looking "
            "in the late morning light. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r028-b08", "out": "s08-and-for-joy-thereof-goeth.jpeg", "seg": "j1b",
        "window": "39.57-44.96", "wide": True, "jesus": False, "ref": False,
        "locks": ["DIGGER", "FIELD"],
        "narration": (
            "and for joy thereof goeth and selleth all that he hath, and buyeth "
            "that field."
        ),
        "must_show": "SCRIPTURE-EXACT: FOR JOY — the worker running full-stride down the footpath toward the village, spade abandoned against the stump, arms pumping, face alight.",
        "must_not_show": "no halo, glare or rim-light; a full RUN, not a walk — joy in motion; the spade left behind tells the story.",
        "scene": (
            "The worker runs flat-out along the worn footpath toward the "
            "distant village rooftops, knees high and arms pumping, his "
            "kilted tunic flying, his face split wide with laughing "
            "disbelieving joy — and back in the field behind him his "
            "spade stands abandoned against the broken olive stump beside "
            "the smoothed, secret ground. Bright midday light down the "
            "whole path. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r028-b09", "out": "s09-did-you-catch-what-he.jpeg", "seg": "n5",
        "window": "46.48-50.52", "wide": True, "jesus": False, "ref": False,
        "locks": ["DIGGER", "VILLAGE"],
        "narration": (
            "Did you catch what he did? He went home and sold everything he "
            "owned."
        ),
        "must_show": "the selling begun — the worker's few possessions spread on a cloth in the street, neighbours gathering, him waving them closer with both arms.",
        "must_not_show": "no halo, glare or rim-light; his goods are FEW and humble — a poor man's whole life on one cloth; his energy is the picture.",
        "scene": (
            "On a spread cloth in the village street lie the worker's "
            "whole life's goods — a sleeping mat, a stack of clay bowls, "
            "an oil lamp, a folded winter cloak, a coil of rope — and he "
            "stands over them waving both arms to beckon the gathering "
            "neighbours in from their doorways and the well, selling "
            "everything at once with the urgency of a man who cannot do "
            "it fast enough. Midday light under the faded awnings. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r028-b10", "out": "s10-his-tools-all-of-it.jpeg", "seg": "n6",
        "window": "51.71-55.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["DIGGER", "VILLAGE"],
        "narration": "His tools. All of it — gladly, without a second thought.",
        "must_show": "the last and hardest sale made easy — his spade, mattock and adze passing into another workman's hands, the seller's face wholly glad.",
        "must_not_show": "no halo, glare or rim-light; a workman selling his TOOLS is selling his living — and his face must show zero hesitation.",
        "scene": (
            "Close at a workshop bench under the eaves: the worker lays "
            "his spade, his mattock and a worn adze into the accepting "
            "arms of a broad older workman, and his own face above the "
            "handover is open, bright and utterly unhesitating — a man "
            "handing away his living with the lightness of someone "
            "shedding a coat in spring. A few dark coins already sit "
            "counted on the bench. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r028-b11", "out": "s11-and-with-every-coin-he.jpeg", "seg": "n7 + n8",
        "window": "56.13-62.91", "wide": True, "jesus": False, "ref": False,
        "locks": ["DIGGER", "VILLAGE"],
        "narration": (
            "And with every coin he had, he bought that one field for himself. "
            "Because he knew what was waiting under the soil."
        ),
        "must_show": "SCRIPTURE-EXACT: the purchase — the whole small fortune of coins poured from his cloth bundle into the landowner's held-out lap-fold, elders witnessing, the deal sealed.",
        "must_not_show": "no halo, glare or rim-light; EVERY coin goes — the emptied cloth shaken out; a proper public purchase with witnesses, not a whisper deal.",
        "scene": (
            "By the village well in late-afternoon light the worker "
            "up-ends his knotted cloth bundle so that his whole small "
            "fortune of dark coins pours into the held-out lap-fold of a "
            "prosperous landowner's robe, the cloth shaken empty to its "
            "last corner — while two grey-bearded elders stand as "
            "witnesses beside them and a boy cranes to watch. The "
            "landowner's face is amused at the bargain; the worker's is "
            "certain as sunrise. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r028-b12", "out": "s12-that-field-was-worth-more.jpeg", "seg": "n8",
        "window": "62.91-67.27", "wide": True, "jesus": False, "ref": False,
        "locks": ["DIGGER", "FIELD"],
        "narration": (
            "That field was worth more than everything else he owned, put "
            "together."
        ),
        "must_show": "the new owner entering his field — the worker stepping over the low boundary bank onto his own ground for the first time, empty-handed and rich.",
        "must_not_show": "no halo, glare or rim-light; he owns NOTHING now but this field — no bundle, no tools, no cloak; and he steps in like a king.",
        "scene": (
            "In the long amber light of late afternoon the worker steps "
            "over the low stone boundary bank into the rough thistled "
            "field, both hands empty at his sides, nothing left to his "
            "name but the ground under his sandals — and he enters it "
            "with his back straight and his chin up, a poor man walking "
            "into his kingdom. The broken olive stump and the smoothed "
            "secret spot wait in the middle distance. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r028-b13", "out": "s13-that-jesus-said-is-what.jpeg", "seg": "n9 + n10",
        "window": "67.87-73.83", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": (
            "That, Jesus said, is what God's kingdom is like. At first it can "
            "look like an ordinary field."
        ),
        "must_show": "the field at its plainest — wide, empty, thistled, unremarkable under a flat sky; the point is how little it appears to be.",
        "must_not_show": "no halo, glare or rim-light; NO figures, no hint of the treasure — deliberately the dullest frame in the row.",
        "scene": (
            "The field alone under a flat plain sky: rough half-cleared "
            "earth, scattered thistle patches, the broken olive stump, "
            "the low stone bank and the worn footpath running past to "
            "the distant flat rooftops — nothing in the frame that any "
            "passer-by would look at twice, and nothing visible of what "
            "makes it the most valuable ground in the village. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r028-b14", "out": "s14-but-once-you-catch-sight.jpeg", "seg": "n10",
        "window": "73.83-81.53", "wide": True, "jesus": False, "ref": False,
        "locks": ["DIGGER", "TREASURE", "FIELD"],
        "narration": (
            "But once you catch sight of the treasure in it — once you truly "
            "see who Jesus is — nothing else even compares."
        ),
        "must_show": "the treasure seen again, rightly — the worker kneeling at the reopened chest in warm sunset gold, lifting a string of old coins in both hands, awe in his face.",
        "must_not_show": "no halo, glare or rim-light; awe and love in the face, not appetite; the coins stay old and dull-metalled even in the warm light.",
        "scene": (
            "At the reopened trench in warm sunset gold the worker "
            "kneels over the small iron-banded chest, lifting a heavy "
            "string of old dull coins across both open palms and looking "
            "down at it the way a man looks at something he still cannot "
            "believe is his — awe, not appetite. The long amber light "
            "lies across the turned earth and the field around him has "
            "gone soft and warm. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r028-b15", "out": "s15-and-you-give-everything-up.jpeg", "seg": "n11",
        "window": "82.11-84.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["DIGGER"],
        "narration": "And you don't give everything up sadly.",
        "must_show": "a close portrait of the worker's face in the warm last light — and there is not one line of loss anywhere in it; only settled, brimming gladness.",
        "must_not_show": "no halo, glare or rim-light; scan the face for grief and find none — that absence is the beat.",
        "scene": (
            "A close portrait of the worker's young face in the warm "
            "last light of the day, earth still dusting one cheekbone: "
            "his dark eyes are wet and bright at once, the corners of "
            "his mouth pulled into a slow involuntary smile, and nowhere "
            "in the face — brow, eyes, mouth — is there a single line "
            "of regret for everything he no longer owns. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r028-b16", "out": "s16-you-do-it-out-of.jpeg", "seg": "n11",
        "window": "84.25-89.92", "wide": True, "jesus": False, "ref": False,
        "locks": ["DIGGER", "FIELD"],
        "narration": (
            "You do it out of pure joy — because you've found the one thing "
            "worth having everything else."
        ),
        "must_show": "the closing image — the worker alone in the middle of HIS field at sunset, arms flung wide, head thrown back, laughing at the sky.",
        "must_not_show": "no halo, glare or rim-light; the sun is low IN THE SKY at the frame's side, never behind his head; pure unguarded joy.",
        "scene": (
            "In the middle of his own rough field the worker stands with "
            "both arms flung wide and his head thrown back, laughing "
            "full out at the deepening gold sky, his shadow running long "
            "across the thistled earth — a man with nothing left in the "
            "world and everything in it. The low sun sits at the frame's "
            "far side over the boundary bank, the village rooftops warm "
            "in the distance. Every figure has two arms, two hands and "
            "one head."
        ),
    },
]
