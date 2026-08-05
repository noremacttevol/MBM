#!/usr/bin/env python3
"""V2 beat map — row 79, build-79-the-seventy-sent (Luke 10:1-20).

COVERAGE: 19 pictures over 110.6 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 10:1-20 KJV):
  v1    "the Lord appointed other SEVENTY also, and sent them TWO AND
        TWO before his face into every city and place, whither he
        himself would come" — pairs, sent AHEAD of him.
  v2    "The harvest truly is great, but the labourers are few: pray ye
        therefore the Lord of the harvest, that he would send forth
        labourers into his harvest." — spoken over REAL ripe fields.
  v4    "Carry neither purse, nor scrip, nor shoes" — they travel with
        nothing: no bag, no spare sandals, no money.
  v9    "heal the sick that are therein, and say unto them, The kingdom
        of God is come nigh unto you." — the whole message.
  v17   "the seventy RETURNED AGAIN WITH JOY, saying, Lord, even the
        devils are subject unto us through thy name."
  v20   "rejoice not, that the spirits are subject unto you; but rather
        rejoice, because your NAMES ARE WRITTEN IN HEAVEN."

CONTENT-CARE: no row flags, but the v17 report falls under the
no-embodied-devils law — the REPORT is painted (thrilled faces,
animated telling), never any spirit, shadow-figure or symbolic demon.
Healing beats keep full dignity for the sick.

TIME OF DAY ARC (intentional — journeys frame the row): the sending in
clear EARLY MORNING light; the roads and harvest sayings under bright
morning sun over ripe barley; the village welcome at midday; the
return and the names-in-heaven close in warm LATE-AFTERNOON gold.
These are correct story sunlights, not the row-11 defect.

CHANGING CONDITION (kept OUT of the locks): the direction of travel —
outward at morning, homeward at evening; and the joy — power-thrill at
the return, redirected to the deeper gladness by the close.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "PAIR": (
        "PAIR LOCK: the two followers we track are the same two men in "
        "every shot — an older one, about fifty, grey-streaked dark "
        "beard, in a DARK EARTH-BROWN robe; and a younger one, about "
        "twenty-five, clean dark beard, in a CHARCOAL-GREY robe (never "
        "cream, never white). They carry NOTHING: no bag, no purse, no "
        "bundle, no staff — empty-handed on every road."
    ),
    "ROADS": (
        "ROADS LOCK: the Galilean sending country — pale sun-baked dirt "
        "roads threading between RIPE GOLDEN BARLEY FIELDS heavy for "
        "harvest, low dry-stone walls, olive trees, and small "
        "flat-roofed stone villages on the hills. The same ripe "
        "country throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r079-b01", "out": "s01-jesus-picked-seventy-of-his.jpeg", "seg": "n0",
        "window": "0.28-7.43", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROADS"],
        "narration": (
            "Jesus picked seventy of his followers and sent them out two by "
            "two, ahead of him, into every town he was about to visit."
        ),
        "must_show": "SCRIPTURE-EXACT: the sending — Jesus at a road-fork in early morning light, pairs of followers peeling away down the different roads, two and two; a crowd becoming couriers.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the pairs clearly TWOS — never solo walkers, never clumps.",
        "scene": (
            "At the pale road-fork, the camera behind Jesus's "
            "shoulder so the departing pairs walk away from the "
            "lens down every branch, in the clear "
            "early morning Jesus stands sending — "
            "his hand assigning each pair its "
            "road — and the crowd resolves into "
            "twos before him: couples of plain-"
            "robed followers already stepping "
            "away down the different dirt roads "
            "between the ripe barley, two and "
            "two and two, spreading out ahead of "
            "him across the whole gold country "
            "like sparks off a struck flint. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r079-b02", "out": "s02-he-send-them-with-much.jpeg", "seg": "n1",
        "window": "8.03-12.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAIR", "ROADS"],
        "narration": (
            "He didn't send them with much — no extra bag, no spare sandals, "
            "no backup plan."
        ),
        "must_show": "SCRIPTURE-EXACT: the nothing (v4) — close on the tracked pair setting out: empty hands, no bag on either shoulder, no purse at either belt; travellers stripped to the errand.",
        "must_not_show": "no halo, glare or rim-light; NO luggage of any kind in frame — the emptiness is the picture.",
        "scene": (
            "Close on the two as they set out in "
            "the morning light — the older man's "
            "shoulders bare of any bag, the "
            "younger's belt without a purse, "
            "four empty hands swinging free on "
            "the pale road — travellers stripped "
            "to sandals, robes and an errand, "
            "carrying less than any beggar on "
            "that road and walking like men "
            "provisioned for a year. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r079-b03", "out": "s03-just-each-other-and-a.jpeg", "seg": "n1",
        "window": "12.89-15.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAIR", "ROADS"],
        "narration": "Just each other, and a message.",
        "must_show": "the provision — the pair small on the long road through the ripe fields, shoulder to shoulder; two men and their words, sufficient.",
        "must_not_show": "no halo, glare or rim-light; the road LONG and the two of them its only traffic — companionship as the whole kit.",
        "scene": (
            "The wide morning road runs long and "
            "empty through the heavy gold barley "
            "— and on it, small and shoulder to "
            "shoulder, the two walk into the "
            "distance in step, the older's head "
            "inclined toward the younger's as "
            "they talk — no bag between them, no "
            "coin between them, the entire "
            "inventory of the expedition visible "
            "at a glance: each other, and the "
            "sentence they carry. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r079-b04", "out": "s04-the-harvest-truly-is-great.jpeg", "seg": "j1",
        "window": "16.10-26.64", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROADS"],
        "narration": (
            "The harvest truly is great, but the labourers are few: pray ye "
            "therefore the Lord of the harvest, that he would send forth "
            "labourers into his harvest."
        ),
        "must_show": "SCRIPTURE-EXACT: the saying over real fields — Jesus with followers at a field's edge, his arm sweeping the vast ripe barley; in all that gold, only two or three distant reapers.",
        "must_not_show": "no halo, glare or rim-light; the field VAST and the workers FEW — the arithmetic visible in one frame.",
        "scene": (
            "At the field's dry-stone edge Jesus "
            "speaks with his arm swept out over "
            "the barley — a sea of ripe gold "
            "rolling away to the hills, heavy-"
            "headed and ready — and in all that "
            "abundance the morning light finds "
            "exactly two distant reapers bent at "
            "their sickles, tiny against the "
            "acreage — the whole sermon standing "
            "in the landscape: a harvest great, "
            "labourers few, and the listening "
            "followers counting both. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r079-b05", "out": "s05-notice-what-he-did-not.jpeg", "seg": "n1b",
        "window": "36.03-38.15", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROADS"],
        "narration": "Notice what he did not say.",
        "must_show": "the pause — close on Jesus at the field's edge, the sweeping arm come to rest, his look inviting the listeners to re-hear the sentence.",
        "must_not_show": "no halo, glare or rim-light; the beat QUIET — a teacher letting a sentence sit.",
        "scene": (
            "Close on Jesus at the wall's edge, "
            "the sweeping arm come to rest at "
            "his side, the warm brown eyes "
            "moving over his listeners with the "
            "particular stillness of a teacher "
            "letting a sentence sit where he "
            "laid it — the gold field breathing "
            "behind him, the words already said, "
            "and the more important thing being "
            "what was not. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r079-b06", "out": "s06-there-is-so-much-to.jpeg", "seg": "n1b",
        "window": "28.43-36.03", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROADS"],
        "narration": (
            "There is so much to bring in, he told them, and hardly anyone to "
            "do it — so ask the owner of the harvest to send out more workers."
        ),
        "must_show": "the plea illustrated — the two distant reapers at work in the vast gold: sheaves standing bound behind them, unreaped acres before them; honest labour outmatched by abundance.",
        "must_not_show": "no halo, glare or rim-light; the reapers DIGNIFIED and working hard — the shortage is numbers, not effort.",
        "scene": (
            "Deep in the gold the two reapers "
            "work their line — sickles swinging, "
            "a modest row of bound sheaves "
            "standing behind them, and before "
            "them acre upon heavy acre still "
            "untouched, rolling to the hills — "
            "two honest backs bent against an "
            "abundance that laughs at their "
            "arithmetic, the field itself making "
            "the case for the prayer: more "
            "workers, Lord of the harvest. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r079-b07", "out": "s07-he-did-not-say-the.jpeg", "seg": "n1b",
        "window": "38.15-40.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROADS"],
        "narration": "He did not say the fields were empty.",
        "must_show": "the fullness close — heavy ripe barley heads filling the frame, bowed with grain; nothing empty anywhere in it.",
        "must_not_show": "no halo, glare or rim-light; the grain HEAVY and bowed — ripeness at its maximum, the opposite of empty.",
        "scene": (
            "The frame fills wall to wall with "
            "the standing crop: heavy barley "
            "heads bowed on their stalks with "
            "the weight of their own grain, gold "
            "on gold to every edge in the bright "
            "morning, each head fat and ready "
            "and nodding in the field's small "
            "wind — not one empty stem in the "
            "picture, not one bare patch — a "
            "fullness pressing at the borders of "
            "the frame. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r079-b08", "out": "s08-he-said-the-fields-were.jpeg", "seg": "n1b",
        "window": "40.59-44.18", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROADS"],
        "narration": "He said the fields were full, and the crew was short.",
        "must_show": "the whole equation wide — the vast full field under the bright sky, and its entire workforce: the two small reapers; fullness and shortage in one look.",
        "must_not_show": "no halo, glare or rim-light; the disproportion the composition — gold to the horizon, workers you must hunt for.",
        "scene": (
            "The widest look at the equation, the camera high on "
            "the field's rise with the two reapers' backs far "
            "below: "
            "ripe gold running unbroken to the "
            "hill-line under the high bright "
            "sky, dry-stone walls drowned in it, "
            "olive trees islanded in it — and "
            "somewhere in the middle distance, "
            "small enough to hunt for, the "
            "field's entire crew of two, bent "
            "and reaping — a country-sized "
            "fullness attended by a rowboat's "
            "worth of hands. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r079-b09", "out": "s09-wherever-they-were-welcomed-they.jpeg", "seg": "n2 + j2",
        "window": "44.77-52.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAIR"],
        "narration": (
            "Wherever they were welcomed, they were to heal the sick and say "
            "the same simple thing. The kingdom of God is come nigh unto you."
        ),
        "must_show": "SCRIPTURE-EXACT: the welcome and the work (v8-9) — the pair received at a village doorway at midday: the older bending gently to a sick man seated against the wall, the younger speaking the message to the household; healing with full dignity.",
        "must_not_show": "no halo, glare or rim-light; the sick man DIGNIFIED — weary and hollow-cheeked, never grotesque; the healing a gentle laying of hands.",
        "scene": (
            "At a village doorway in the flat "
            "midday light the two are welcomed "
            "in — and go straight to work: the "
            "older kneeling to a hollow-cheeked "
            "man seated weary against the wall, "
            "taking his hand with a workman's "
            "gentleness, while the younger "
            "stands speaking the one sentence to "
            "the gathered household at the door "
            "— healing and announcement arriving "
            "together, the kingdom come near "
            "enough to touch a sick man's hand. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r079-b10", "out": "s10-that-was-the-whole-message.jpeg", "seg": "n2b",
        "window": "54.12-55.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAIR"],
        "narration": "That was the whole message.",
        "must_show": "the message's smallness — close on the younger man's plain speaking face at the doorway: one sentence, delivered simply; no scroll, no props.",
        "must_not_show": "no halo, glare or rim-light; NO scroll, book or prop — the message carried entirely in a plain man's mouth.",
        "scene": (
            "Close on the younger man's face at "
            "the doorway as he says it — plainly, "
            "without flourish, the way you tell "
            "a neighbour the well is full — no "
            "scroll in his hands, no rehearsed "
            "thunder in his voice, the entire "
            "cargo of the expedition delivered "
            "in the time it takes to say one "
            "sentence, and the listening faces "
            "in the door's shade realising it "
            "was addressed to them. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r079-b11", "out": "s11-not-a-warning-not-a.jpeg", "seg": "n2b",
        "window": "55.57-63.82", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAIR"],
        "narration": (
            "Not a warning, not a threat — an announcement that the thing "
            "everyone had been waiting for had just walked into their town."
        ),
        "must_show": "the announcement landing — the village street at midday: faces turning from wells and doorways toward the two messengers; wonder spreading, nobody afraid.",
        "must_not_show": "no halo, glare or rim-light; NO fear anywhere in the street — brightening faces, doors opening wider, good news behaving like good news.",
        "scene": (
            "The village street turns toward the "
            "news: a woman straightening from "
            "the well with her jar half-drawn, "
            "an old man rising off his bench, "
            "children stopping mid-game, doors "
            "opening wider along the lane — "
            "every face swinging toward the two "
            "dusty messengers not in alarm but "
            "in the particular brightening of "
            "people hearing that the long-"
            "awaited thing has finally arrived, "
            "and arrived HERE. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r079-b12", "out": "s12-and-they-came-back-with.jpeg", "seg": "n3",
        "window": "64.49-69.18", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROADS"],
        "narration": (
            "And they came back with joy, amazed at what had happened when "
            "they used his name:"
        ),
        "must_show": "SCRIPTURE-EXACT: the return WITH JOY (v17) — pairs streaming back up the golden late-afternoon roads toward Jesus, waving, hurrying, calling out; homecoming at a run.",
        "must_not_show": "no halo, glare or rim-light; the joy PHYSICAL — quickened steps, raised arms, faces alight with news to tell.",
        "scene": (
            "Down every pale road, the camera at the fork taking "
            "the converging returns in profile, in the warm "
            "late-afternoon gold the pairs come "
            "streaming home — two and two and "
            "two converging on Jesus at the "
            "road-fork, some at a flat run, arms "
            "up, voices carrying ahead of them "
            "across the fields — seventy "
            "travellers who left empty-handed "
            "returning loaded with the one cargo "
            "nobody assigned them: news too big "
            "to walk with. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r079-b13", "out": "s13-lord-even-the-devils-are.jpeg", "seg": "s17",
        "window": "69.78-73.40", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PAIR"],
        "narration": "Lord, even the devils are subject unto us through thy name.",
        "must_show": "SCRIPTURE-EXACT: the report — the tracked pair breathless before Jesus, the younger mid-telling with hands wide, the older nodding hard; the amazement of the words, NOTHING of their subject painted.",
        "must_not_show": "ABSOLUTE: no devil, demon, spirit, shadow-figure or symbolic darkness anywhere — the REPORT is the picture; no halo, glare or rim-light.",
        "scene": (
            "The two arrive breathless before "
            "Jesus in the low gold light — the "
            "younger mid-report with his hands "
            "thrown wide at the size of what "
            "happened, the older nodding hard "
            "behind him, both faces lit with "
            "road-dust and astonishment — men "
            "telling their commander that the "
            "weapon he lent them turned out to "
            "outrank everything they met — and "
            "Jesus receiving it with a listening "
            "warmth. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r079-b14", "out": "s14-lord-even-the-evil-spirits.jpeg", "seg": "n3b",
        "window": "74.89-81.24", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROADS"],
        "narration": (
            "Lord, even the evil spirits obey us when we use your name. They "
            "were thrilled, and they had every right to be."
        ),
        "must_show": "the thrill shared — the wider returned company around Jesus: animated retellings rippling through the group, hands re-enacting, laughter; earned exhilaration, spirits NEVER shown.",
        "must_not_show": "ABSOLUTE: no spirit, demon or dark figure in any retelling gesture's direction — only joyful people; no halo, glare or rim-light.",
        "scene": (
            "Around Jesus in the warm gold the "
            "returned company boils with "
            "retellings — knots of travellers "
            "re-enacting their road stories with "
            "flying hands, one man laughing with "
            "his head back, two women gripping "
            "each other's arms at some detail, "
            "the joy jumping pair to pair like "
            "wind through the barley — seventy "
            "ordinary people discovering what "
            "his name weighed in their mouths, "
            "and rightly thrilled. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r079-b15", "out": "s15-and-then-jesus-told-them.jpeg", "seg": "n3b",
        "window": "81.24-84.51", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROADS"],
        "narration": "And then Jesus told them what to actually celebrate.",
        "must_show": "the redirect begun — close on Jesus raising a gentle hand into the celebration, warm and smiling but gathering their attention for a correction of aim.",
        "must_not_show": "no halo, glare or rim-light; NO scolding — the hand gentle, the smile real; joy being steered, not stopped.",
        "scene": (
            "Close on Jesus in the midst of the "
            "celebration, one hand rising gently "
            "into the noise — the smile on him "
            "real and warm, nothing of the "
            "scold in it, but the eyes already "
            "steadying into the look of a "
            "teacher about to move the target — "
            "joy he has no intention of ending, "
            "and every intention of aiming at "
            "something that will outlast the "
            "trip. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r079-b16", "out": "s16-notwithstanding-in-this-rejoice-not.jpeg", "seg": "j3",
        "window": "85.12-93.90", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROADS"],
        "narration": (
            "Notwithstanding in this rejoice not, that the spirits are subject "
            "unto you; but rather rejoice, because your names are written in "
            "heaven."
        ),
        "must_show": "SCRIPTURE-EXACT: the true cause for joy — Jesus speaking to the quieted seventy in the deepening gold, his hand lifted toward the evening sky; faces tilting up with him.",
        "must_not_show": "no halo, glare or rim-light; no visible writing, book or letters in the sky — the heaven plain evening sky; the certainty carried in his face.",
        "scene": (
            "The company quiets around him, the camera low behind "
            "the seated seventy's near backs, in "
            "the deepening gold as Jesus speaks "
            "the correction — his hand lifting "
            "easily toward the high clear "
            "evening sky, and seventy dusty "
            "faces tilting up after it — rejoice "
            "THERE, in a ledger none of them can "
            "see and none of them can lose, "
            "where each of their plain names is "
            "already entered — the biggest news "
            "of the whole expedition saved for "
            "the homecoming. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r079-b17", "out": "s17-be-glad-about-that-he.jpeg", "seg": "n3c",
        "window": "95.38-99.87", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PAIR"],
        "narration": (
            "Don't be glad about that, he said. Don't let the power be the "
            "thing that thrills you."
        ),
        "must_show": "the thrill re-aimed — close on the tracked pair's faces as it lands: the road-exhilaration settling into something quieter and deeper; Jesus's steady face near.",
        "must_not_show": "no halo, glare or rim-light; the settling NOT deflation — excitement maturing, not dying.",
        "scene": (
            "Close on the two travellers' faces "
            "as the correction lands — the "
            "younger's road-fever settling by "
            "visible degrees into something "
            "stiller and heavier, the older's "
            "eyes going from Jesus's steady face "
            "up to the evening sky and back — "
            "not deflated men, but men watching "
            "their best day get quietly "
            "outranked by a better fact. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r079-b18", "out": "s18-be-glad-about-this-instead.jpeg", "seg": "n3c",
        "window": "99.87-105.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAIR"],
        "narration": (
            "Be glad about this instead: The power was temporary and it was "
            "never really theirs."
        ),
        "must_show": "the borrowed thing — close on the pair's open empty hands in the gold light: the same hands that worked wonders on the road, plain again; power returned to its lender.",
        "must_not_show": "no halo, glare or rim-light; the hands ORDINARY — calloused, dusty, empty; nothing clinging to them.",
        "scene": (
            "Close in the low gold on the two "
            "men's open hands — calloused, road-"
            "dusty, utterly ordinary — the same "
            "four hands that healed the sick and "
            "carried his name through the "
            "villages, empty again exactly as "
            "they left — the power passed "
            "through them like water through a "
            "channel and returned to its owner, "
            "leaving the hands what they always "
            "were: borrowed tools, briefly "
            "trusted. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r079-b19", "out": "s19-the-name-in-the-book.jpeg", "seg": "n3c",
        "window": "105.45-110.38", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROADS"],
        "narration": (
            "The name in the book was permanent, and it was theirs before "
            "they ever left on the trip."
        ),
        "must_show": "the closing image — the whole seventy at rest around Jesus in the last warm light, faces settled and sky-turned; joy of the permanent kind, already possessed.",
        "must_not_show": "no halo, glare or rim-light; no visible book or writing — the permanence carried in the settled faces and the wide calm sky.",
        "scene": (
            "The closing frame settles over the "
            "whole company at rest around Jesus "
            "in the last warm light — seventy "
            "travellers seated on the walls and "
            "the road's edge with the day's "
            "dust still on them, faces calm and "
            "sky-turned above the darkening "
            "gold fields — holding the one "
            "possession that predates the whole "
            "expedition and outlasts every road: "
            "their plain names, already written, "
            "already home. Every figure has two "
            "arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "ROADS": "PLACE-REF/roads.jpeg",  # build-38-persistent-widow v2-r038-b39
}
# === end PLACE-PLATES ===
