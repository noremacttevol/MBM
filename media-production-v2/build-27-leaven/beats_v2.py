#!/usr/bin/env python3
"""V2 beat map — row 27, build-27-leaven (Matthew 13:33).

COVERAGE: 16 pictures over 91.6 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 13:33 KJV):
  v33   "Another parable spake he unto them; The kingdom of heaven is like
        unto LEAVEN, which a WOMAN took, and HID in THREE MEASURES of meal,
        till THE WHOLE was leavened."
        — the same seaside teaching day as rows 24-26 (Matthew 13:1-2).
          Those rows staged the boat from the hillside, the waterline,
          inside the boat, among the crowd, and in profile — so THIS
          build's single frame beat (b02) frames the distant boat BETWEEN
          two foreground listeners' shoulders. Sixth composition, no
          repeat.
        — the leaven is HID: worked deep in until invisible. The hiding
          and the waiting are the parable.
        — three measures (about an ephah) is an ENORMOUS batch — bread for
          a whole village gathering, kneaded in a large trough, not a bowl.
        — "till the whole was leavened" — total, quiet, inside-out change.

TIME OF DAY: the frame beat is bright morning at the sea. The kitchen arc
runs a real baker's clock: LATE AFTERNOON for mixing and kneading, warm
LAMPLIT EVENING for covering the trough, deep NIGHT for the quiet waiting
beat (correct, not a defect — 'she covers it and waits'), and clean MORNING
for the risen dough, the baking and the sharing.

CONTENT-CARE: row 27 has no flag in §3. Nothing sensitive.

CHANGING CONDITION (kept OUT of the locks): the dough — dry flour, shaggy
mass, smooth kneaded mound, covered trough, risen overflow, baked loaves —
changes beat to beat and is never locked. The woman's flour-dusted forearms
come and go with the work.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "BAKER": (
        "BAKER LOCK: the woman is the same woman in every shot — about "
        "fifty, sturdy and capable, with strong forearms, a broad kind "
        "deeply lined face, dark eyes and grey-streaked black hair bound "
        "back under a DARK RUST-RED head-cloth. She wears a DEEP "
        "INDIGO-BLUE wool dress with the sleeves rolled, a DARK UMBER apron "
        "and a woven belt (never cream, never white). Her face is shown "
        "clearly."
    ),
    "KITCHEN": (
        "KITCHEN LOCK: the courtyard kitchen of a village house — a low "
        "stone room open on one side to a small courtyard, a big scarred "
        "wooden kneading trough on a stout table, a domed clay bread oven "
        "in the courtyard corner, shelves of clay jars, hanging bunches of "
        "herbs, sacks of flour against the wall and a small deep-set window. "
        "The same trough, oven, shelves and window appear in every kitchen "
        "beat."
    ),
    "SHORE-PAIR": (
        "SHORE FRAME LOCK: the pebble beach of the Sea of Galilee seen from "
        "just behind two standing listeners — dressed in SATURATED DEEP "
        "earth colours: dark chocolate brown and dusty indigo wool (never "
        "cream, never white; only Jesus wears cream) — with the bright "
        "green-blue water beyond them and a small weathered wooden fishing "
        "boat floating a few boat-lengths off the beach. Bright morning "
        "light."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r027-b01", "out": "s01-jesus-said-the-kingdom-of.jpeg", "seg": "n1",
        "window": "0.28-6.55", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAKER", "KITCHEN"],
        "narration": (
            "Jesus said the kingdom of God is like something a woman does every "
            "week, in her own kitchen, with her own hands."
        ),
        "must_show": "the ordinary holy scene the parable lives in — the woman at her kneading trough in warm afternoon light, sleeves rolled, hands in the work.",
        "must_not_show": "no halo, glare or rim-light; utterly everyday — nothing staged or grand about the kitchen.",
        "scene": (
            "Warm late-afternoon light slants into the low courtyard "
            "kitchen: the sturdy woman stands at the big scarred kneading "
            "trough with her sleeves rolled to the elbow and both hands "
            "deep in the work, flour dusting her dark apron and forearms, "
            "her lined face easy with the familiarity of a task done every "
            "week of her life. Clay jars, hanging herbs and flour sacks "
            "stand about her, the domed oven waiting in the courtyard "
            "corner. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r027-b02", "out": "s02-another-parable-spake-he-unto.jpeg", "seg": "s33",
        "window": "7.20-9.57", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SHORE-PAIR"],
        "narration": "Another parable spake he unto them;",
        "must_show": "SCRIPTURE-EXACT: the teaching frame — the distant boat with the seated Jesus framed in the gap BETWEEN two foreground listeners' shoulders at the water's edge.",
        "must_not_show": "no halo, glare or rim-light on Jesus; he is seated in the boat; nobody stands on the water.",
        "scene": (
            "At the water's edge two listeners stand close in the near "
            "foreground, seen from behind at shoulder height, soft and "
            "dark at the frame's edges — and in the bright gap between "
            "their shoulders, sharp and small across the green-blue water, "
            "the little wooden boat rides with Jesus seated in it, hand "
            "lifted mid-word, the one bright point both silhouetted "
            "shoulders lean toward. Morning sun on the water. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r027-b03", "out": "s03-the-kingdom-of-heaven-is.jpeg", "seg": "j1",
        "window": "10.73-18.77", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAKER", "KITCHEN"],
        "narration": (
            "The kingdom of heaven is like unto leaven, which a woman took, and "
            "hid in three measures of meal, till the whole was leavened."
        ),
        "must_show": "SCRIPTURE-EXACT: the taking — the woman lifting the small lump of leaven from its clay keeping-jar, the great trough of flour waiting behind it.",
        "must_not_show": "no halo, glare or rim-light; the leaven is one small dull lump — modest in her strong hand against the huge waiting batch.",
        "scene": (
            "At the kitchen table the woman lifts a small pale lump of old "
            "dough from a squat clay keeping-jar with two fingers and a "
            "thumb, holding it up briefly to the warm afternoon light — "
            "and behind her hand, filling the rest of the frame, the big "
            "wooden trough stands heaped with pale flour, absurdly large "
            "against the little lump. Her eyes are on the leaven with a "
            "baker's plain confidence. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r027-b04", "out": "s04-leaven-is-just-a-little.jpeg", "seg": "n2",
        "window": "19.82-25.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAKER"],
        "narration": (
            "Leaven is just a little piece of old, living dough, what we would "
            "call a sourdough starter."
        ),
        "must_show": "a close shot of the leaven itself in her open palm — a small dull cream-grey lump, pocked with tiny bubbles, unmistakably alive but utterly plain.",
        "must_not_show": "no halo, glare or rim-light; nothing beautiful about it — plain, slightly sticky, ordinary.",
        "scene": (
            "A close shot of the woman's strong flour-dusted palm holding "
            "the small lump of old dough up in the window light: a dull "
            "grey-tan knob no bigger than a walnut, its surface pocked "
            "with tiny holes and one slow bubble, faintly glistening and "
            "sticky at its base — plain as a stone, and alive. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r027-b05", "out": "s05-small-plain.jpeg", "seg": "n2",
        "window": "25.10-27.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["KITCHEN"],
        "narration": "Small. Plain.",
        "must_show": "the lump set alone on the wide wooden table edge — a speck of dull dough on a great expanse of scarred wood.",
        "must_not_show": "no halo, glare or rim-light; emptiness around it — the frame is mostly bare table on purpose.",
        "scene": (
            "The small dull lump of leaven sits alone near the edge of the "
            "wide scarred wooden table, the worn grain of the empty wood "
            "stretching away around it in the soft window light, a knife "
            "mark and an old flour ring the only company in the frame. "
            "Small, plain, easy to miss. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r027-b06", "out": "s06-and-three-measures-of-meal.jpeg", "seg": "n3",
        "window": "29.29-36.07", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAKER", "KITCHEN"],
        "narration": (
            "And three measures of meal is not a small bowl. It is an enormous "
            "amount of flour, enough bread to feed a hundred people."
        ),
        "must_show": "SCRIPTURE-EXACT: the scale — the woman pouring the third great sackful of flour into the brimming trough, flour dust in the air, the batch plainly enormous.",
        "must_not_show": "no halo, glare or rim-light; the trough must read as HUGE — arm-span long, heaped high; never a mixing bowl.",
        "scene": (
            "The woman up-ends a heavy flour sack over the great wooden "
            "trough with both arms, the third of three — two emptied sacks "
            "already slumped against the table leg — and the pale flour "
            "mounds up over the trough's full arm-span length, a fine haze "
            "of flour dust hanging in the slanted afternoon light around "
            "her shoulders. The batch is plainly enough for a village. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r027-b07", "out": "s07-easy-to-overlook.jpeg", "seg": "n2",
        "window": "27.27-28.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["KITCHEN"],
        "narration": "Easy to overlook.",
        "must_show": "the lump nearly lost among the kitchen's clutter — jars, herbs, a cloth — the eye having to hunt for it.",
        "must_not_show": "no halo, glare or rim-light; genuinely easy to miss in the frame — but findable.",
        "scene": (
            "A still shot along the kitchen shelf in soft light: clay jars "
            "shoulder to shoulder, a folded cloth, a hanging bunch of dry "
            "herbs, a wooden scoop — and tucked at the shelf's edge among "
            "them, small and dull and almost invisible until the eye finds "
            "it, the little lump of leaven on its scrap of cloth. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r027-b08", "out": "s08-she-takes-that-tiny-bit.jpeg", "seg": "n4",
        "window": "36.72-44.66", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAKER", "KITCHEN"],
        "narration": (
            "She takes that tiny bit of leaven and works it down deep into the "
            "whole mass, hiding it, until you cannot even see where it went."
        ),
        "must_show": "SCRIPTURE-EXACT: the hiding — both her fists buried to the wrist in the great shaggy mass of dough, working the leaven down in; the lump itself already gone from sight.",
        "must_not_show": "no halo, glare or rim-light; the leaven is INVISIBLE in this frame — swallowed by the batch; her effort is real, shoulders in it.",
        "scene": (
            "The woman leans her whole weight over the great trough, both "
            "fists buried past the wrist in the shaggy pale mass of dough, "
            "shoulders rolling into the work, flour to her elbows and a "
            "strand of grey hair loose across her brow — and nowhere in "
            "the folded, turning mass is there any sign of the little lump "
            "she has already worked down deep. Warm late light through the "
            "window. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r027-b09", "out": "s09-then-she-covers-it-and.jpeg", "seg": "n5",
        "window": "45.25-51.79", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAKER", "KITCHEN"],
        "narration": (
            "Then she covers it and waits. Nothing looks like it is happening. "
            "No noise, no show, no spectacle."
        ),
        "must_show": "the covering — a heavy cloth spread over the trough by lamplight, the woman's day ending, the kitchen going quiet.",
        "must_not_show": "no halo, glare or rim-light; evening lamplight is correct here — the day is done; the covered trough is just a still shape.",
        "scene": (
            "Evening has come down on the kitchen and one clay lamp burns "
            "on the shelf: the woman spreads a heavy dark woollen cloth "
            "over the full length of the trough, smoothing it down at the "
            "corners with both hands, her work finished — the covered "
            "trough now just a long quiet shape on the table in the "
            "lamplight, promising nothing. The courtyard beyond the open "
            "side stands dusk-blue. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r027-b10", "out": "s10-just-quiet-hidden-time-but.jpeg", "seg": "n5 + n6",
        "window": "51.79-58.32", "wide": True, "jesus": False, "ref": False,
        "locks": ["KITCHEN"],
        "narration": (
            "Just quiet, hidden time. But inside, the leaven is spreading "
            "through every part of the dough."
        ),
        "must_show": "deep night — the empty kitchen, the covered trough alone in moonlight from the small window, nobody there; the working is all invisible.",
        "must_not_show": "no halo, glare or rim-light; NO person in frame; night lighting is correct — stillness is the whole picture.",
        "scene": (
            "Deep night in the empty kitchen: cool moonlight falls through "
            "the small deep-set window and lies in one pale square across "
            "the covered trough on its table, the dark cloth utterly "
            "still, the lamp out, the jars and hanging herbs gone to "
            "shadow along the walls. Nothing moves and no one is there — "
            "and under the cloth, unseen, everything is changing. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r027-b11", "out": "s11-and-by-morning-the-whole.jpeg", "seg": "n6",
        "window": "58.32-64.95", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAKER", "KITCHEN"],
        "narration": (
            "And by morning the whole heavy mass has risen, alive, changed all "
            "the way through."
        ),
        "must_show": "SCRIPTURE-EXACT: the reveal — morning light, the cloth drawn back, the dough risen high over the trough's rim, and the woman's glad unsurprised face over it.",
        "must_not_show": "no halo, glare or rim-light; the dough visibly OVERFILLS the trough — domed above the rim, pressing at the cloth's edges.",
        "scene": (
            "Clean morning light fills the kitchen as the woman draws the "
            "dark cloth back off the trough with both hands — and the "
            "dough beneath has risen into a great smooth living dome, "
            "swelled high above the wooden rim along its whole length, "
            "soft and full where last night lay a heavy flat mass. Her "
            "lined face above it is glad and entirely unsurprised — she "
            "has seen this every week of her life. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r027-b12", "out": "s12-that-jesus-said-is-how.jpeg", "seg": "n7",
        "window": "65.62-68.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAKER"],
        "narration": "That, Jesus said, is how the kingdom of God works.",
        "must_show": "a close shot of the risen dough with the woman's hand pressed gently into it — the springing life of it under her fingers.",
        "must_not_show": "no halo, glare or rim-light; the finger-press must read — soft dough yielding and springing, alive.",
        "scene": (
            "A close shot in morning light: the woman's strong hand pressed "
            "gently into the top of the risen dome of dough, her fingers "
            "sunk to the first knuckle in its soft swell, the surface "
            "around them tight and full of held air — the quiet, living "
            "spring of the whole batch answering her touch. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r027-b13", "out": "s13-not-by-force-not-by.jpeg", "seg": "n7",
        "window": "68.97-71.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["KITCHEN"],
        "narration": "Not by force. Not by noise.",
        "must_show": "the gentleness of the means — the little clay keeping-jar of leaven back on its shelf in soft light, lid ajar, its work done without a sound.",
        "must_not_show": "no halo, glare or rim-light; a still, quiet frame — no motion anywhere.",
        "scene": (
            "A quiet still shot of the squat clay keeping-jar back in its "
            "place on the shelf in soft morning light, its lid set ajar, a "
            "faint dusting of flour on the wood around it, the hanging "
            "herbs motionless above — the small plain thing that changed "
            "the whole batch, sitting silent as if nothing had happened. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r027-b14", "out": "s14-it-starts-small-and-hidden.jpeg", "seg": "n7",
        "window": "71.62-78.57", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAKER", "KITCHEN"],
        "narration": (
            "It starts small and hidden, and it quietly changes everything it "
            "touches, from the inside out."
        ),
        "must_show": "the change made whole — the woman shaping the risen dough into many round loaves down the table, the one batch becoming bread for many.",
        "must_not_show": "no halo, glare or rim-light; MANY loaves forming — the multiplication visible down the table's length.",
        "scene": (
            "Down the full length of the floured table the woman works in "
            "the bright morning light, shaping the risen dough into round "
            "loaves — a long row of them already formed and resting under "
            "her quick hands, eight, ten, more, with the great trough "
            "standing nearly emptied behind her. Flour hangs faint in the "
            "sunlit air of the doorway. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r027-b15", "out": "s15-that-is-how-good-he.jpeg", "seg": "n8",
        "window": "79.20-82.59", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAKER", "KITCHEN"],
        "narration": "That is how good he is. He does not overpower you.",
        "must_show": "warmth without force — the woman sliding loaves into the domed clay oven in the courtyard, the oven's soft firelight on her face and apron.",
        "must_not_show": "no halo, glare or rim-light; the oven's fire stays INSIDE the oven mouth — warm light, no flame spectacle.",
        "scene": (
            "In the courtyard corner the woman kneels at the domed clay "
            "oven, sliding a round loaf off a flat wooden peel into its "
            "warm-lit mouth, two loaves already baking within, the soft "
            "orange warmth from the oven door touching her forearms and "
            "the front of her dark apron. Morning light fills the rest of "
            "the little courtyard. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r027-b16", "out": "s16-he-works-gently-patiently-from.jpeg", "seg": "n8",
        "window": "82.59-91.18", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAKER", "KITCHEN"],
        "narration": (
            "He works gently, patiently, from within, until the whole of you is "
            "warmed and changed and made into something that can feed other "
            "people."
        ),
        "must_show": "the closing image — the woman at her courtyard gate handing warm loaves into the hands of neighbours and children, the bread going out to feed others.",
        "must_not_show": "no halo, glare or rim-light; generosity in motion — the loaves passing from her hands into theirs is the visible action.",
        "scene": (
            "At the low courtyard gate in warm mid-morning light the woman "
            "hands a round loaf, still steaming faintly, into the cupped "
            "hands of a young neighbour woman with a baby on her hip, "
            "while a small boy beside them already hugs his loaf to his "
            "chest and an old man waits smiling behind — a basket of warm "
            "loaves riding on the baker's arm, enough for all of them. "
            "Every figure has two arms, two hands and one head."
        ),
    },
]
