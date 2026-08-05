#!/usr/bin/env python3
"""V2 beat map — row 143, build-143-i-am-the-door (John 10:1-9).

COVERAGE: 10 pictures over 54.9 s = 5.5 s/picture (matches the library density).

SCRIPTURE FACTS (John 10 KJV):
  10:1  "He that entereth not by the door into the sheepfold, but
        CLIMBETH UP SOME OTHER WAY, the same is a thief and a
        robber."
  10:7  "Verily, verily, I say unto you, I AM THE DOOR of the sheep."
  10:9  "I am the door: by me if any man enter in, he shall be
        SAVED, and shall GO IN AND OUT, and find PASTURE."
  The picture: a hill-country sheepfold has ONE opening and no
        gate — the shepherd himself lies across the gap at night;
        the shepherd IS the door.

RENDERING LAWS:
  - THE ILLUSTRATIVE SHEPHERD (b01/b02/b05/b06/b09/b10) is a plain
    hill shepherd, NOT jesus-locked — the parable's picture. Jesus
    appears as HIMSELF in the teaching beats (b03/b07); in b07 he
    stands framed in the fold's opening as he says the words.
  - THE WALL-CLIMBER (b04) is unease, never violence (the row-126
    wolf pattern): a dark figure slipping over the far wall, sheep
    stirring away; NO attack, NO struggle, ever.
  - The fold has exactly ONE opening and NO wooden gate — the
    open gap is the whole doctrine; never render a gate or bars.
  - Sheep pass IN at evening (b06) and OUT at morning (b08) — the
    two directions matter (in and out, free); direction law.
  - b10's close: the shepherd LYING ACROSS the opening under the
    stars, flock safe within — himself the door; tender, unposed.

TIME OF DAY ARC (intentional): the fold frames at deep-blue NIGHT
watch and violet evening BY DESIGN (a night-guard story); the
teaching beats in warm day; b08's going-out at bright morning; the
close under full stars.

CHANGING CONDITION (kept OUT of the locks): the flock — filing in
at dusk, streaming out at morning, folded safe at night; the
shepherd — seated watch, standing welcome, lying across the gap.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "FOLD": (
        "FOLD LOCK: the hill sheepfold — a dry-stone fold on a "
        "night hillside with exactly ONE opening in its wall and NO "
        "gate: an open gap the width of a man; cream-wool sheep "
        "within, deep-blue night or violet dusk, a small shepherd's "
        "fire by the gap. The same fold, wall and single opening "
        "throughout."
    ),
    "SHEPHERD": (
        "SHEPHERD LOCK: one working Judean shepherd of about THIRTY-FIVE — never "
        "old, never grey, never white-bearded. He is lean, broad-shouldered and "
        "weather-hardened, sun-darkened to a deep brown at the face, neck and "
        "forearms, with thick black hair to the jaw pushed back off his forehead and "
        "a short full black beard with no grey in it at all. He has a straight nose, "
        "a heavy brow and dark brown eyes set deep from squinting into distance. He "
        "wears a short knee-length tunic of coarse undyed DARK EARTH-BROWN wool, "
        "worn thin at the shoulder, with a wide folded rust-brown cloth sash knotted "
        "at the waist, a rolled coarse DARK UMBER-BROWN wool mantle slung across one "
        "shoulder, and hard-worn dark leather sandals. HE WEARS NO SHEEPSKIN, NO "
        "FLEECE-LINED GARMENT AND NOTHING PALE, WHITE OR CREAM-COLOURED ANYWHERE ON "
        "HIS BODY — every piece of cloth on him is dark brown or rust-brown. He carries a long "
        "hand-cut olivewood staff with a natural crook, its wood polished dark by his "
        "hands. HE IS NEVER IN CREAM, OFF-WHITE, IVORY OR ANY NEAR-WHITE CLOTH. He is "
        "the same man, same age, same black hair and beard, same brown tunic in every "
        "frame he appears in, near or far, sharp or blurred, front or back, and he is "
        "never aged, greyed, thinned, or replaced by another man. He is the "
        "SAME shepherd as build-21's (the lost-sheep parable) — one parable "
        "shepherd across both rows. He is the parable's shepherd, NOT Jesus."
    ),
    "HILLSIDE": (
        "HILLSIDE LOCK: the teaching hillside — a dry grazing slope "
        "in warm daylight where Jesus teaches, listeners seated on "
        "the rocks, the fold visible on the hill beyond. The same "
        "slope throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r143-b01", "out": "s01-jesus-used-a-picture-the.jpeg", "seg": "n0",
        "window": "0.28-7.49", "wide": True, "jesus": False, "ref": False,
        "locks": ["FOLD", "SHEPHERD"],
        "narration": (
            "Jesus used a picture the crowd knew well — a sheepfold with one "
            "opening, and a shepherd who guards it through the night."
        ),
        "must_show": "the picture — the stone fold on the night hillside, its ONE gateless opening, the shepherd seated on watch at the gap with his small fire; the whole parable in one frame.",
        "must_not_show": "ABSOLUTE: no gate, no bars — the open gap and the man; the night deliberate.",
        "scene": (
            "The picture everyone in the crowd grew up inside, "
            "the camera set low on the slope taking the fold "
            "from the side: the dry-stone ring stands on the "
            "night hillside with its single opening — a gap "
            "the width of a man, no gate, no bar, nothing "
            "across it at all except the shepherd himself, "
            "seated in the opening with his staff and his "
            "small fire, the cream-wool flock folded safe "
            "behind him — one wall, one way in, one man who "
            "IS the difference between inside and out. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r143-b02", "out": "s02-the-opening-is-where-danger.jpeg", "seg": "n0",
        "window": "7.49-11.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD", "SHEPHERD"],
        "narration": "The opening is where danger is stopped and every sheep is known.",
        "must_show": "the gap's two jobs — the shepherd at the opening, one hand firm on his staff (the stopping), the other resting on a passing sheep's head (the knowing).",
        "must_not_show": "no halo; both jobs READABLE — guard-firm staff, gentle knowing hand.",
        "scene": (
            "The gap does two jobs and his two hands show "
            "them: the shepherd stands in the opening with "
            "his staff planted firm against whatever the "
            "dark hillside might send — that is the first "
            "job — while his free hand rests on the head of "
            "a ewe pressing past his knee into the fold, "
            "fingers finding the notch in her ear he has "
            "known since she was a lamb — that is the "
            "second — danger stopped and every sheep known, "
            "both at once, at the one narrow place. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r143-b03", "out": "s03-verily-verily-i-say-unto.jpeg", "seg": "j1",
        "window": "11.86-15.72", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": "Verily, verily, I say unto you, I am the door of the sheep.",
        "must_show": "SCRIPTURE-EXACT: the claim — Jesus teaching on the day slope, the double-verily gravity on him; listeners still; the fold visible on the hill beyond.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the fold in the background linking claim to picture.",
        "scene": (
            "The double verily clears the air for the claim: "
            "Jesus on the warm day slope with his listeners "
            "settled on the rocks, the little stone fold "
            "visible on the hill beyond his shoulder — and "
            "the formula that always precedes his heaviest "
            "sentences laid down first: verily, VERILY — "
            "then the claim itself, calm as a landmark: I am "
            "the DOOR of the sheep — the picture on the "
            "hill and the man on the slope joined in one "
            "sentence. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r143-b04", "out": "s04-someone-who-sneaks-over-the.jpeg", "seg": "n1a",
        "window": "17.52-23.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD"],
        "narration": (
            "Someone who sneaks over the wall avoids the shepherd because he "
            "is there to take, not to care."
        ),
        "must_show": "the other way in — a dark figure slipping over the FAR wall at night, avoiding the lit opening; the sheep below stirring away; unease only, NO violence.",
        "must_not_show": "ABSOLUTE: no attack, no seizure — the climb and the flock's uneasy shift; the lit opening visibly avoided.",
        "scene": (
            "The wrong way in tells you everything about the "
            "visitor: at the fold's far dark side a figure "
            "eases himself over the stones — hooded, "
            "careful, choosing the wall precisely because "
            "the opening is lit and manned — and below him "
            "the nearest sheep are already stirring away "
            "into the flock's middle, wool pressing against "
            "wool — nothing has happened yet, and everything "
            "is already known: the ones who come to care "
            "use the door; the ones who avoid the shepherd "
            "have their reasons. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r143-b05", "out": "s05-but-the-door-is-not.jpeg", "seg": "n1b",
        "window": "24.25-26.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD", "SHEPHERD"],
        "narration": "But the door is not another trap or test.",
        "must_show": "the un-trap — the opening warm and easy: the shepherd seated relaxed at the gap, fire friendly, nothing barred or rigged; a way in that wants you in.",
        "must_not_show": "ABSOLUTE: no gate, no mechanism, no test apparatus — the ease of the opening the whole picture.",
        "scene": (
            "Look how untrapped the way in is: the opening "
            "stands warm in the fire's small light, the "
            "shepherd seated easy against the gap's stone "
            "shoulder with his staff across his knees — no "
            "gate to fumble, no latch to know, no toll, no "
            "riddle — a doorway that consists entirely of a "
            "person who wants the flock inside, the whole "
            "apparatus of entry reduced to being known by "
            "the one sitting there — which every sheep in "
            "the hills can manage. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r143-b06", "out": "s06-it-is-the-guarded-way.jpeg", "seg": "n1b",
        "window": "26.50-29.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD", "SHEPHERD"],
        "narration": "It is the guarded way the flock comes in safe.",
        "must_show": "the evening file — the flock filing IN through the opening at violet dusk, each passing under the shepherd's hand; safety as procession.",
        "must_not_show": "no halo; DIRECTION — inward through the gap at dusk; the touch on each passing back.",
        "scene": (
            "Safety files in one fleece at a time: at violet "
            "dusk the flock comes home through the single "
            "opening — a woolly procession pressing through "
            "the gap while the shepherd stands over them, "
            "his hand touching each passing back in the old "
            "evening count — in, in, in, known, known, "
            "known — the day's grazing behind them and the "
            "guarded dark ahead, every animal that passes "
            "under the hand sleeping tonight inside the "
            "only wall that matters. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r143-b07", "out": "s07-i-am-the-door-by.jpeg", "seg": "j2",
        "window": "30.20-38.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FOLD"],
        "narration": (
            "I am the door: by me if any man enter in, he shall be saved, "
            "and shall go in and out, and find pasture."
        ),
        "must_show": "SCRIPTURE-EXACT: the claim embodied — Jesus HIMSELF standing framed in the fold's single opening, arms open in welcome; the sentence and the picture become one.",
        "must_not_show": "no halo, glare or rim-light on Jesus; he FILLS the gap the shepherd kept — the door with a face.",
        "scene": (
            "For one frame the parable and its meaning trade "
            "places: Jesus himself stands framed in the "
            "fold's single opening — the gap the shepherd "
            "kept all night now filled by the one the "
            "picture was always about — his arms open in "
            "the welcome the words describe: by ME, enter, "
            "be saved, go in and out, find pasture — the "
            "door of the sheep standing in the doorway of "
            "the sheep, wearing a face, holding out its "
            "hands. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r143-b08", "out": "s08-through-him-you-come-in.jpeg", "seg": "n2",
        "window": "39.77-45.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD", "SHEPHERD"],
        "narration": "Through him you come in and you go out — free, fed, not trapped.",
        "must_show": "the going OUT — bright morning: the flock streaming freely out through the opening toward green pasture, the shepherd waving them past; liberty in both directions.",
        "must_not_show": "no halo; DIRECTION — outward at morning, unhurried and free; pasture green beyond.",
        "scene": (
            "The door works in both directions, which is the "
            "point: bright morning pours over the hillside "
            "and the flock pours out to meet it — streaming "
            "unhurried through the single opening past the "
            "shepherd's easy hand, fanning onto slopes gone "
            "green with pasture — no pen, no trap, no wall "
            "that only takes: in at dusk for safety, out at "
            "dawn for feeding, the gap swinging both ways "
            "on the hinge of one trustworthy man — free, "
            "fed, and back again by dark. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r143-b09", "out": "s09-notice-that-the-door-is.jpeg", "seg": "n2",
        "window": "45.28-49.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD", "SHEPHERD"],
        "narration": "Notice that the door is a person, not a score you must earn.",
        "must_show": "the relationship — close at the opening: a ewe nuzzling the shepherd's open hand, his face bent warm over her; entry as being-known, not qualifying.",
        "must_not_show": "no halo; NOTHING transactional in frame — no tally, no toll; the nuzzle and the bent face.",
        "scene": (
            "The entrance requirement, photographed up "
            "close: at the opening a ewe pushes her blunt "
            "head into the shepherd's open hand and he "
            "bends over her, thumb working the wool behind "
            "her ear, his weathered face gone soft — this "
            "is the whole toll, the entire examination: "
            "being his — no score kept anywhere on the "
            "hillside, no ledger in the fold, a door made "
            "of relationship and open to everything it "
            "knows by name. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r143-b10", "out": "s10-safety-and-pasture-begin-with.jpeg", "seg": "n2",
        "window": "49.52-54.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD", "SHEPHERD"],
        "narration": (
            "Safety and pasture begin with trusting the shepherd who put "
            "himself in the opening."
        ),
        "must_show": "the closing trust — full starry night: the shepherd LYING ACROSS the opening, mantle drawn, staff at hand, the flock folded asleep within; himself the door.",
        "must_not_show": "no halo; the lying-across UNMISTAKABLE — his body spanning the gap; the flock's sleep total; stars deep.",
        "scene": (
            "The last frame is the doctrine sleeping in the "
            "doorway: under a whole sky of stars the "
            "shepherd lies stretched across the fold's "
            "single opening — mantle drawn to his chin, "
            "staff loose in reach, his body spanning the "
            "gap from stone to stone — and behind him the "
            "flock sleeps in a woolly drift, safe by the "
            "simple arithmetic of the arrangement: nothing "
            "gets in except across him — the shepherd who "
            "put HIMSELF in the opening, which is where "
            "safety and pasture have always begun. Every "
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
    "FOLD": "PLACE-REF/fold.jpeg",  # build-21-lost-sheep v2-r021-b12
}
# === end PLACE-PLATES ===
