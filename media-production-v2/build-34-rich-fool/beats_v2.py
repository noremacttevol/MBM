#!/usr/bin/env python3
"""V2 beat map — row 34, build-34-rich-fool (Luke 12:13-21).

COVERAGE: 21 pictures over 119.3 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 12:13-21 KJV):
  v13-15 the parable is told to a CROWD on the road ("one of the company
        said unto him...") — the frame beats (b01, b17) put Jesus among a
        roadside crowd in open country, a staging no earlier row has used.
  v16   "the ground of a certain rich man brought forth PLENTIFULLY" — the
        harvest itself is honest and good; the narration protects this
        ('there is nothing wrong with a good harvest').
  v17-18 "he THOUGHT WITHIN HIMSELF ... I will pull down my barns, and
        build greater" — the planning happens ALONE; every planning frame
        shows him with no other person in it. That solitude is the row's
        quiet visual thesis: every plan was about himself.
  v19   "Soul, thou hast much goods laid up for many years; take thine
        ease, eat, drink, and be merry" — the imagined future gets one
        lamplit fantasy-feast beat, and even the imagined table is set
        for ONE.
  v20   "Thou fool, THIS NIGHT thy soul shall be required of thee" —
        ⚑ Flag J (CONTENT-CARE §3 row 34): God calls him fool FOR THE
        BARNS, not for existing. GOD IS NEVER PAINTED and no voice-source
        is shown — the beat is the man alone in the dark, sitting up,
        listening. The DEATH IS NEVER SHOWN: no body, no deathbed — the
        morning-after beat is an empty chair, a burned-out lamp and the
        tally sticks still on the table.
  v21   "So is he that layeth up treasure for himself, and is not rich
        toward God" — the closing contrast beat answers the empty barn
        with an ordinary family rich in the only way that lasts.

TIME OF DAY: frame beats are bright open-country morning. The parable:
gold harvest DAY → planning at EVENING lamplight (alone) → the imagined
feast in warm lamplight (alone) → deep NIGHT for v20 (required — 'this
night') → grey DAWN for the morning-after and inheritance beats → warm
evening for the closing family contrast. All shifts scripture-driven.

CHANGING CONDITION (kept OUT of the locks): the barns — old and bursting,
torn down, new and huge, full and unvisited — change across the row and
are described per-beat, never locked.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "RICHMAN": (
        "RICH MAN LOCK: the rich man is the same man in every shot — about "
        "fifty-five, heavy-set and well-fed, with a round satisfied face, "
        "a carefully trimmed dark beard going grey at the corners, and "
        "small quick acquisitive eyes. He wears a fine DEEP PLUM wool robe "
        "with a DARK GOLD-STITCHED collar over a DARK CHESTNUT under-tunic, "
        "a broad soft belt and good sandals (never cream, never white). "
        "His face is shown clearly — self-satisfied, not evil."
    ),
    "FARM": (
        "ESTATE LOCK: the rich man's farm — wide golden grain fields "
        "rolling to a low hill, a fine stone house with a shaded porch, a "
        "working yard with two OLD weathered timber barns (replaced by "
        "one great NEW pale-timber barn in the later beats, per the "
        "beat), a fig tree by the gate and a low stone boundary wall. The "
        "same house, yard, tree and wall throughout."
    ),
    "ROADSIDE": (
        "ROADSIDE LOCK: open rolling country where a dirt road crests a "
        "low rise — dry grass, scattered field stones, a single broad "
        "terebinth tree giving shade, and a listening crowd of ordinary "
        "people in SATURATED DEEP earth colours: dark browns, deep "
        "russet, dark olive, dusty indigo, faded plum (never cream, "
        "never white; only Jesus wears cream). Faces shown clearly."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r034-b01", "out": "s01-jesus-told-a-story-about.jpeg", "seg": "n0",
        "window": "0.28-3.67", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROADSIDE"],
        "narration": "Jesus told a story about a rich man who had a very good year.",
        "must_show": "the frame — Jesus in the shade of the roadside terebinth with the crowd gathered close on the dry grass around him, mid-story.",
        "must_not_show": "no halo, glare or rim-light on Jesus; open country, ordinary people, morning light.",
        "scene": (
            "Under the broad terebinth tree at the crest of the dirt "
            "road, in bright open morning light, Jesus stands "
            "mid-story with one hand raised, and the crowd is settled "
            "close around him on the dry grass and field stones — a "
            "farmer still holding his mattock, two women with market "
            "baskets set down, a boy bellied out flat on the grass in "
            "front. The rolling gold country runs away behind them. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r034-b02", "out": "s02-his-fields-produced-an-enormous.jpeg", "seg": "n1",
        "window": "4.21-10.34", "wide": True, "jesus": False, "ref": False,
        "locks": ["RICHMAN", "FARM"],
        "narration": (
            "His fields produced an enormous harvest — more grain and fruit "
            "than he had ever gathered in his life."
        ),
        "must_show": "SCRIPTURE-EXACT: the plentiful ground — the rich man standing in his field among a harvest visibly beyond all expectation, sheaves and loaded carts everywhere.",
        "must_not_show": "no halo, glare or rim-light; the harvest is GOOD and honestly won — golden abundance, nothing sinister in the frame.",
        "scene": (
            "Under a high gold harvest sun the rich man stands "
            "waist-deep in his own standing grain with his arms "
            "spread, laughing at the size of it — around him the "
            "field is a sea of heavy bowed heads, sheaves already "
            "stand stooked in rows to the boundary wall, and two "
            "carts by the gate are loaded past their rails with "
            "grain sacks and baskets of figs and grapes. Hired "
            "reapers work the far edge. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r034-b03", "out": "s03-in-fact-he-had-so.jpeg", "seg": "n2",
        "window": "10.82-14.49", "wide": True, "jesus": False, "ref": False,
        "locks": ["RICHMAN", "FARM"],
        "narration": "In fact, he had so much that he ran out of room to store it all.",
        "must_show": "the overflow — the two old barns bursting, doors wedged open by the pile, sacks stacked outside under the eaves, and the rich man surveying the problem.",
        "must_not_show": "no halo, glare or rim-light; the barns are visibly TOO SMALL — grain spilling at the jambs, sacks out in the open air.",
        "scene": (
            "In the working yard the two old weathered barns stand "
            "crammed past shutting — one door wedged open by the "
            "grain pile behind it, loose barley spilling over the "
            "threshold, sacks stacked shoulder-high outside under "
            "the eaves with a cloth thrown over them — and the rich "
            "man stands in the middle of the yard with his fists on "
            "his hips, surveying the beautiful problem, the fig "
            "tree throwing late-day shade across the sacks. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r034-b04", "out": "s04-this-will-i-do-i.jpeg", "seg": "j3",
        "window": "15.06-23.10", "wide": True, "jesus": False, "ref": False,
        "locks": ["RICHMAN", "FARM"],
        "narration": (
            "This will I do: I will pull down my barns, and build greater; and "
            "there will I bestow all my fruits and my goods."
        ),
        "must_show": "SCRIPTURE-EXACT: the plan conceived — the rich man ALONE on his porch at evening, gesturing his vision over the yard toward the old barns, no other soul in frame.",
        "must_not_show": "no halo, glare or rim-light; ALONE is the law of this beat — he plans to an audience of nobody.",
        "scene": (
            "On the shaded porch in warm evening light the rich man "
            "stands utterly alone, one arm sweeping a grand arc over "
            "his yard toward the two old bursting barns as though "
            "presenting the future to an audience — but the yard is "
            "empty, the workers gone home, and his great gesture "
            "falls on nothing but the sacks and the fig tree in the "
            "long amber shadows. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r034-b05", "out": "s05-so-he-thought-to-himself.jpeg", "seg": "n3",
        "window": "24.61-26.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["RICHMAN"],
        "narration": "So he thought to himself: What should I do?",
        "must_show": "the thinking — a close shot of the rich man at his lamplit table, chin on his fist, eyes moving over tally sticks and a scratched slate of figures.",
        "must_not_show": "no halo, glare or rim-light; a pleasant problem — his face is enjoying the arithmetic; still alone.",
        "scene": (
            "A close shot at the lamplit table inside the fine house: "
            "the rich man's round face rests on his fist in the warm "
            "lamplight, eyes narrowed happily over a spread of tally "
            "sticks, a scratched slate of figures and a little heap "
            "of sample grain — a man savouring the pleasantest "
            "problem of his life, with no chair but his own drawn up "
            "to the table. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r034-b06", "out": "s06-i-know-i-will-tear.jpeg", "seg": "n3",
        "window": "26.92-31.06", "wide": True, "jesus": False, "ref": False,
        "locks": ["RICHMAN", "FARM"],
        "narration": "I know — I will tear down my barns and build bigger ones.",
        "must_show": "the tearing down — the old barns half-dismantled, workers stripping timbers, and the rich man directing with evident delight.",
        "must_not_show": "no halo, glare or rim-light; demolition as ambition — orderly work, no destruction-drama.",
        "scene": (
            "In bright working daylight the two old barns are coming "
            "down — one already a skeleton of stripped grey timbers "
            "with two workers walking a beam down a ramp, the other "
            "losing its roof plank by plank — while the rich man "
            "strides the yard between them pointing men to their "
            "tasks, robe hem tucked up, delighted with his own "
            "decisiveness. The grain sacks wait in the open under "
            "cloths. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r034-b07", "out": "s07-and-i-will-say-to.jpeg", "seg": "j4",
        "window": "35.40-44.08", "wide": True, "jesus": False, "ref": False,
        "locks": ["RICHMAN"],
        "narration": (
            "And I will say to my soul, Soul, thou hast much goods laid up for "
            "many years; take thine ease, eat, drink, and be merry."
        ),
        "must_show": "SCRIPTURE-EXACT: the imagined ease — the rich man's lamplit fantasy: himself reclining at a laden feast table... set for ONE; the emptiness of the dream visible inside its warmth.",
        "must_not_show": "no halo, glare or rim-light; the table is abundant and the seats around it are EMPTY — one cup, one couch used, many bare places.",
        "scene": (
            "In deep warm lamplight the rich man reclines alone on a "
            "cushioned couch at a long feast table laden end to end — "
            "roast fowl, figs, bread towers, a brimming cup in his "
            "raised hand — and down both sides of the abundance the "
            "other couches stand empty and the other places bare, "
            "not one cup poured but his own, his contented face the "
            "only face in a room built for thirty. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r034-b08", "out": "s08-there-i-will-store-up.jpeg", "seg": "n4",
        "window": "31.65-34.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["RICHMAN", "FARM"],
        "narration": "There I will store up all my grain and all my goods.",
        "must_show": "the great new barn rising — pale new timber towering over the yard, huge against the old footprint stones, the rich man gazing up at it.",
        "must_not_show": "no halo, glare or rim-light; the new barn DWARFS everything — house, tree and man; scale is the message.",
        "scene": (
            "The great new barn stands nearly finished in the yard, "
            "its pale fresh timber walls and high roofline towering "
            "over the stone house and the fig tree together, wide "
            "doors tall as two men — and the rich man stands small "
            "at its foot with his head tipped all the way back, "
            "hands clasped behind him, gazing up at the size of what "
            "he has built for himself. Old foundation stones of the "
            "torn-down barns edge the yard. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r034-b09", "out": "s09-and-then-i-will-say.jpeg", "seg": "n5",
        "window": "45.61-50.74", "wide": True, "jesus": False, "ref": False,
        "locks": ["RICHMAN", "FARM"],
        "narration": (
            "And then I will say to myself: You have plenty saved up for years "
            "to come. Relax."
        ),
        "must_show": "the ease taken — the rich man leaning back against his full new barn's door in the late sun, arms folded in satisfaction, the future all salted away behind the timber at his back.",
        "must_not_show": "no halo, glare or rim-light; complete self-satisfaction — and still not another soul in the frame.",
        "scene": (
            "In the low late-afternoon sun the rich man leans his "
            "back and one raised foot against the closed doors of "
            "the great new barn, arms folded high on his chest, eyes "
            "half-shut with satisfaction — the whole towering wall "
            "of pale timber behind him packed to the roof with his "
            "years to come, the yard empty, the long shadows his "
            "only company. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r034-b10", "out": "s10-eat-drink-and-enjoy-your.jpeg", "seg": "n5 + n6",
        "window": "50.74-54.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["RICHMAN"],
        "narration": "Eat, drink, and enjoy your life. He had it all figured out.",
        "must_show": "a close portrait of the rich man's face at maximum contentment — eyes closed, small smile, the face of a man whose plan has no hole in it.",
        "must_not_show": "no halo, glare or rim-light; genuine peace on the face — the audience knows what he doesn't; the picture must not.",
        "scene": (
            "A close portrait in the warm gold of the day's end: the "
            "rich man's round well-fed face utterly at rest, eyes "
            "closed, the trimmed beard framing a small deep smile of "
            "total arrival — every year accounted for, every sack "
            "counted, nothing left in the world to worry about. The "
            "warm blur of his estate behind him. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r034-b11", "out": "s11-every-single-plan-was-about.jpeg", "seg": "n6 + n7",
        "window": "54.57-62.55", "wide": True, "jesus": False, "ref": False,
        "locks": ["RICHMAN", "FARM"],
        "narration": (
            "Every single plan was about himself — his barns, his goods, his "
            "own comfort. But there was one thing he had never planned for."
        ),
        "must_show": "the solitude summed — dusk falling on the whole estate, one lamp burning in one window of the big house, the great barn dark, no other person anywhere.",
        "must_not_show": "no halo, glare or rim-light; dusk is deliberate — a wide lonely frame; one small lit window is the only warmth.",
        "scene": (
            "Dusk settles over the whole estate in one wide frame: "
            "the great new barn a dark mass against the last "
            "green-gold of the sky, the harvested fields grey and "
            "empty to the boundary wall, the road bare — and in the "
            "fine stone house a single small window holds the only "
            "lamp, one man's light in all that gathered plenty. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r034-b12", "out": "s12-and-that-very-night-god.jpeg", "seg": "n7",
        "window": "62.55-65.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["RICHMAN"],
        "narration": "And that very night, God spoke to him.",
        "must_show": "⚑ Flag J: the man alone in the dark, sitting bolt upright, listening — GOD IS NOT PAINTED, no light-source voice, no figure; only the man and the night.",
        "must_not_show": "no halo, glare or rim-light; NOTHING visible speaks — no beam, no figure, no glowing anything; the man's arrested face carries the whole beat.",
        "scene": (
            "Deep night in the dark bedchamber: the rich man sits "
            "bolt upright on the edge of his bed in his night tunic, "
            "utterly still, his head lifted and turned as a man "
            "turns toward a voice — eyes wide in the dimness, one "
            "hand gripping the bed frame — and around him the room "
            "holds nothing but shadow, a cold unlit lamp on the "
            "chest, and the deep blue of the window. Whatever speaks "
            "is not in the picture. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r034-b13", "out": "s13-thou-fool-this-night-thy.jpeg", "seg": "j1",
        "window": "65.74-73.31", "wide": True, "jesus": False, "ref": False,
        "locks": ["RICHMAN", "FARM"],
        "narration": (
            "Thou fool, this night thy soul shall be required of thee: then "
            "whose shall those things be, which thou hast provided?"
        ),
        "must_show": "SCRIPTURE-EXACT, ⚑ Flag J: the question landing — the man at his dark window looking out at the great barn's silhouette, everything he provided standing in the night with the question hanging over it.",
        "must_not_show": "no halo, glare or rim-light; no voice-source painted, no death painted — the man, the window, and the dark shape of everything he cannot keep.",
        "scene": (
            "From inside the dark room: the rich man stands at the "
            "deep window in his night tunic, both hands on the "
            "sill, looking out at the huge black silhouette of his "
            "new barn against the star-thin sky — all of it, sacks "
            "and grain and years of ease, standing out there in the "
            "night on the wrong side of the question he has just "
            "been asked. His reflection-less face is lit only by "
            "the faint night sky. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r034-b14", "out": "s14-that-night-his-life-was.jpeg", "seg": "n8",
        "window": "74.87-76.56", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "That night, his life was over.",
        "must_show": "⚑ Flag J RESTRAINED: no body, no deathbed — grey dawn light on his empty chair at the table, the lamp burned out, the tally sticks exactly where he left them.",
        "must_not_show": "no halo, glare or rim-light; NO corpse, no mourners, nothing morbid — absence told entirely through objects.",
        "scene": (
            "First grey dawn light through the window falls on the "
            "table where he planned it all: his chair stands empty "
            "and pushed back, the clay lamp beside the tally sticks "
            "has burned dry with a dead black wick, the scratched "
            "slate of figures waits mid-calculation, and the little "
            "heap of sample grain sits untouched — everything "
            "exactly where a man left it who thought he was coming "
            "back. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r034-b15", "out": "s15-and-everything-he-had-piled.jpeg", "seg": "n8",
        "window": "76.56-83.74", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARM"],
        "narration": (
            "And everything he had piled up — the barns, the grain, all of it — "
            "would simply pass to someone else."
        ),
        "must_show": "SCRIPTURE-EXACT: whose shall those things be — strangers in the yard at morning: an assessor with a slate counting sacks, relatives pointing at the barn, dividing what he provided.",
        "must_not_show": "no halo, glare or rim-light; nothing ghoulish — brisk, ordinary inheritance business, which is exactly the deflation the verse intends.",
        "scene": (
            "Bright ordinary morning in the yard: the great barn "
            "doors stand open on the mountain of sacks while "
            "unfamiliar people move through the estate — a lean "
            "assessor tapping a slate as he counts down the rows, "
            "two well-dressed relatives arguing quietly with their "
            "arms out over the yard, a servant leading away the "
            "first laden cart — the whole gathered plenty changing "
            "hands in a single businesslike hour. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r034-b16", "out": "s16-he-had-planned-for-everything.jpeg", "seg": "n9",
        "window": "84.30-90.71", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "He had planned for everything except the one thing that was "
            "certain: that one day he would stand before God."
        ),
        "must_show": "the unplanned-for certainty — a close still shot of the dead lamp and the slate of figures, and beside them, unmarked on any tally, the first shaft of morning sun crossing the table.",
        "must_not_show": "no halo, glare or rim-light; no judgment imagery — the plain sunbeam across the unfinished arithmetic says it.",
        "scene": (
            "A close still shot on the table in the quiet house: the "
            "burned-out lamp, the slate dense with careful figures, "
            "the tally sticks bundled and ready for years that will "
            "not come — and cutting straight across all of it, "
            "entered in no column, the first clean shaft of morning "
            "sun through the window, the one certainty he never "
            "wrote down. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r034-b17", "out": "s17-and-jesus-ended-the-story.jpeg", "seg": "n10",
        "window": "91.27-93.83", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROADSIDE"],
        "narration": "And Jesus ended the story with these words.",
        "must_show": "back at the roadside — a close shot of Jesus, the story's gravity in his face, the hushed crowd soft around him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; gentle gravity — a warning given out of love.",
        "scene": (
            "A close shot of Jesus under the terebinth shade, the "
            "bright country light behind him, his face grave and "
            "kind as he lets the story settle before its last "
            "sentence — and around the frame's soft edges the "
            "hushed listeners have gone very still, the farmer's "
            "mattock forgotten on his shoulder. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r034-b18", "out": "s18-so-is-he-that-layeth.jpeg", "seg": "j2",
        "window": "94.36-99.33", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARM"],
        "narration": (
            "So is he that layeth up treasure for himself, and is not rich "
            "toward God."
        ),
        "must_show": "SCRIPTURE-EXACT: the verdict as a picture — the great barn standing full and magnificent in perfect light, and utterly unvisited; wealth with nobody home.",
        "must_not_show": "no halo, glare or rim-light; no figures at all — a monument shot of the barn, beautiful and pointless.",
        "scene": (
            "The great new barn in flawless mid-morning light, shot "
            "like a monument: pale timber walls immaculate, the "
            "huge doors closed and barred, the mountain of wealth "
            "sealed inside — and not one living soul anywhere in "
            "the wide frame, the yard swept and silent, the fig "
            "tree's shadow the only thing that moves across the "
            "boards. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r034-b19", "out": "s19-his-barns-were-full-but.jpeg", "seg": "n11",
        "window": "100.85-107.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARM"],
        "narration": (
            "His barns were full, but his soul was empty. He was rich in things "
            "— and poor in the only wealth that lasts."
        ),
        "must_show": "the two riches side by side — through the barn's cracked-open door, the golden mountain of grain inside; in the foreground, the single dusty place at the long outdoor table where one man always ate alone.",
        "must_not_show": "no halo, glare or rim-light; fullness behind, emptiness in front — one cup, one plate, one bench end worn.",
        "scene": (
            "In warm late light the barn door stands cracked open "
            "just enough to show the golden mountain of grain "
            "climbing into the dark inside — and in the near "
            "foreground the long outdoor table under the fig tree "
            "holds a single dusty clay cup and plate at its head, "
            "one bench-end worn smooth, the rest of the long boards "
            "bare and unsat-upon down all their length. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r034-b20", "out": "s20-there-is-nothing-wrong-with.jpeg", "seg": "n12",
        "window": "108.14-110.17", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": "There is nothing wrong with a good harvest.",
        "must_show": "harvest honoured — a different, ordinary farm family bringing in their sheaves together at golden evening, the goodness of plenty shared in the work.",
        "must_not_show": "no halo, glare or rim-light; joy and TOGETHERNESS in the same golden abundance the rich man had alone.",
        "scene": (
            "On a small ordinary farm in deep golden evening a "
            "family brings the harvest in together — the father "
            "swinging a sheaf up onto the cart to his laughing "
            "son, the mother and daughter walking behind with "
            "gleaned armfuls, a grandfather leading the ox — the "
            "same golden plenty as the great estate, carried in "
            "many hands at once. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r034-b21", "out": "s21-the-real-question-is-quieter.jpeg", "seg": "n12",
        "window": "110.17-119.01", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The real question is quieter than that: are you only storing up "
            "for yourself — or are you storing up a life that is rich with God?"
        ),
        "must_show": "the closing contrast — the farm family's small lamplit table crowded shoulder to shoulder over simple food, a neighbour welcomed in at the door; the wealth that lasts.",
        "must_not_show": "no halo, glare or rim-light; the food is SIMPLE and the table is FULL of people — the exact inverse of the rich man's laden empty room.",
        "scene": (
            "Inside the small farmhouse at night the one table is "
            "crowded shoulder to shoulder in the lamplight — "
            "children wedged between grandparents, the father "
            "breaking a plain loaf down the line, bowls of lentils "
            "passing hand to hand — while at the open door the "
            "mother draws a hesitating neighbour in by the wrist "
            "toward the last squeezed-in place on the bench. Simple "
            "food, no empty seat. Every figure has two arms, two "
            "hands and one head."
        ),
    },
]
