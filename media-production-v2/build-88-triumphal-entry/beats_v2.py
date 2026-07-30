#!/usr/bin/env python3
"""V2 beat map — row 88, build-88-triumphal-entry (Matthew 21:1-11).

COVERAGE: 20 pictures over 111.6 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 21:1-11 KJV):
  v1-3  at Bethphage, Jesus sends TWO DISCIPLES: "ye shall find an ASS
        TIED, and a COLT with her: loose them, and bring them unto me.
        And if any man say ought... The Lord hath need of them."
  v4-5  the prophecy (Zech 9:9): "thy King cometh unto thee, MEEK, and
        SITTING UPON AN ASS, and a colt the foal of an ass."
  v6-7  "brought the ass, and the colt, and put on them their CLOTHES,
        and they set him thereon." — garments as the saddle.
  v8    "a very great multitude SPREAD THEIR GARMENTS in the way;
        others CUT DOWN BRANCHES from the trees, and strawed them in
        the way."
  v9    "Hosanna to the son of David: Blessed is he that cometh in the
        name of the Lord; Hosanna in the highest."
  v10-11 "all the city was MOVED, saying, WHO IS THIS? And the
        multitude said, This is Jesus the PROPHET OF NAZARETH of
        Galilee."

FRAME-STAGING: same occasion as row 83 (the weeping) — staged
DIFFERENTLY on purpose: no overlook-panorama compositions here; this
row lives in the Bethphage lane, on the branch-strewn road at crowd
level, and at the city gate and streets. Row 83 owns the vista.

TIME OF DAY: one bright spring morning throughout — Passover week,
clear sun.

CONTENT-CARE: no flags. The colt is handled gently everywhere; the
crowd's fervor joyful, never mob-like; Jesus's meekness the constant
against the noise.

CHANGING CONDITION (kept OUT of the locks): the colt — tied, loosed,
clothed with cloaks, ridden; the road — bare, then carpeted with
cloaks and branches; the city — settled, then stirred to asking.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "LANE": (
        "LANE LOCK: the Bethphage village lane — low stone houses, a "
        "wooden door-post ring where animals are tied, fig and olive "
        "trees over the walls, bright morning light. The same lane "
        "and post throughout."
    ),
    "COLT": (
        "COLT LOCK: the animals are one grey MOTHER DONKEY and her "
        "darker grey COLT — the colt small, young and never before "
        "ridden; both handled gently in every shot; the colt is the "
        "one ridden, dark cloaks laid over its back for a saddle."
    ),
    "TWO": (
        "TWO DISCIPLES LOCK: the errand pair are the same two men in "
        "every shot — one stocky with a short dark beard in a DARK "
        "OLIVE robe, one lean and younger in a DEEP SLATE-BLUE robe "
        "(never cream, never white)."
    ),
    "ROAD": (
        "ROAD LOCK: the entry road — a broad pale road descending "
        "between olive trees toward Jerusalem's great limestone GATE, "
        "the city wall high beside it, packed festival crowds along "
        "both edges. The same road, wall and gate throughout."
    ),
    "CROWD": (
        "CROWD LOCK: the festival crowd — pilgrims and families in "
        "DARK EARTH-BROWN, RUST, DEEP OLIVE and SLATE robes (never "
        "cream, never white), waving cut palm and olive branches, "
        "spreading their own dark cloaks on the road; joyful, loud, "
        "never menacing."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r088-b01", "out": "s01-as-jesus-came-near-jerusalem.jpeg", "seg": "n0a",
        "window": "0.28-5.76", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LANE", "TWO"],
        "narration": (
            "As Jesus came near Jerusalem, he sent two disciples ahead into "
            "the village with a strange errand."
        ),
        "must_show": "SCRIPTURE-EXACT: the sending — Jesus at the road's edge outside the village, hand directing the two disciples toward the lane's houses; the errand dispatched.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the two setting OFF — mid-turn toward the village, errand accepted though not understood.",
        "scene": (
            "At the roadside under the olive "
            "trees Jesus sends the errand: his "
            "hand pointing past the first low "
            "houses into the bright village "
            "lane, the two disciples — stocky "
            "olive-robed and lean slate-blue — "
            "already mid-turn to go, trading "
            "one puzzled glance between them "
            "on the way: sent to fetch, of "
            "all things in Passover week, "
            "somebody's donkey — and going "
            "anyway, because he said so. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r088-b02", "out": "s02-go-into-the-village-over.jpeg", "seg": "jv2",
        "window": "6.38-15.71", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TWO"],
        "narration": (
            "Go into the village over against you, and straightway ye shall "
            "find an ass tied, and a colt with her: loose them, and bring "
            "them unto me."
        ),
        "must_show": "SCRIPTURE-EXACT: the instruction — close on Jesus giving the errand's exact detail to the two listening faces: an ass tied, a colt with her; foreknowledge delivered like directions.",
        "must_not_show": "no halo, glare or rim-light; the detail CONFIDENT — a man describing what he has not seen as if reading it.",
        "scene": (
            "Close on the giving of "
            "directions that should be "
            "impossible: Jesus's calm face "
            "laying out the errand detail by "
            "detail — the village, the tied "
            "mother, the colt beside her — "
            "with the settled precision of a "
            "man reading a list off a page "
            "only he can see, while the two "
            "faces before him do their best "
            "to memorise a future their "
            "teacher apparently already "
            "walked through. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r088-b03", "out": "s03-untie-them-and-bring-them.jpeg", "seg": "n0a2",
        "window": "28.38-30.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["LANE", "COLT", "TWO"],
        "narration": "Untie them and bring them to me.",
        "must_show": "the untying — close in the lane: the stocky disciple's hands working the tether loose from the door-post ring, the mother donkey and small colt standing exactly as described.",
        "must_not_show": "no halo, glare or rim-light; the animals CALM under gentle hands — no tugging or startling.",
        "scene": (
            "Close at the worn door-post "
            "ring: the stocky disciple's "
            "fingers working the rope's knot "
            "loose while his partner strokes "
            "the grey mother's neck — and "
            "beside her, small and dark-grey "
            "and watching everything, the "
            "young colt that has never "
            "carried a man — the pair standing "
            "exactly where the directions put "
            "them, patient as if they had "
            "been told too. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r088-b04", "out": "s04-and-if-any-man-say.jpeg", "seg": "jv2",
        "window": "15.71-25.42", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TWO"],
        "narration": (
            "And if any man say ought unto you, ye shall say, The Lord hath "
            "need of them; and straightway he will send them."
        ),
        "must_show": "SCRIPTURE-EXACT: the password given — Jesus finishing the instruction, the two nodding it into memory; THE LORD HATH NEED OF THEM as the whole authorization.",
        "must_not_show": "no halo, glare or rim-light; the sentence's SUFFICIENCY the point — no purse offered, no letter, just words.",
        "scene": (
            "Jesus hands them the only "
            "credential the errand needs: one "
            "sentence — THE LORD HATH NEED OF "
            "THEM — no coin, no sealed letter, "
            "no name of a mutual friend, and "
            "the two disciples nodding it "
            "carefully into memory like men "
            "issued a key described as fitting "
            "a lock they have never seen — "
            "five words, guaranteed in advance "
            "to open a stranger's hand. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r088-b05", "out": "s05-go-into-the-village-he.jpeg", "seg": "n0a2",
        "window": "26.92-28.38", "wide": True, "jesus": False, "ref": False,
        "locks": ["LANE", "TWO"],
        "narration": "Go into the village, he told them.",
        "must_show": "the errand underway — the two disciples entering the bright lane between the low houses, purposeful; the village receiving its strange visitors.",
        "must_not_show": "no halo, glare or rim-light; the lane ORDINARY — wash lines, a woman at a doorway, daily life about to be interrupted by prophecy.",
        "scene": (
            "The two come up the bright lane "
            "between the low stone houses — "
            "wash strung wall to wall "
            "overhead, a woman pausing at "
            "her doorway to watch the "
            "strangers pass, a dog trotting "
            "a suspicious half-circle — two "
            "men walking into an ordinary "
            "village morning carrying "
            "directions written before the "
            "morning existed, their eyes "
            "already hunting the door-posts "
            "for a tied grey donkey. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r088-b06", "out": "s06-and-if-anyone-asks-why.jpeg", "seg": "n0a2",
        "window": "30.55-35.93", "wide": True, "jesus": False, "ref": False,
        "locks": ["LANE", "COLT", "TWO"],
        "narration": (
            "And if anyone asks why, just say the Lord needs them — and "
            "he'll let them go."
        ),
        "must_show": "SCRIPTURE-EXACT: the password working — the owner at his door, hand half-raised in question, already easing into consent as the sentence lands; the animals being led away.",
        "must_not_show": "no halo, glare or rim-light; the consent VISIBLE mid-happening — objection melting into a nod, exactly as promised.",
        "scene": (
            "It happens just as promised: the "
            "owner comes out with his hand "
            "half-raised in fair question — "
            "those are mine — and the "
            "sentence meets him mid-stride: "
            "THE LORD HATH NEED OF THEM — and "
            "the frame catches the exact "
            "instant the objection melts, "
            "the raised hand turning into a "
            "wave-on, the head beginning its "
            "nod, while the mother and colt "
            "are led past him out of his own "
            "gate. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r088-b07", "out": "s07-they-went-and-it-happened.jpeg", "seg": "n0b",
        "window": "36.58-39.14", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "COLT", "TWO"],
        "narration": "They went, and it happened exactly as he said.",
        "must_show": "the delivery — the two returning to Jesus with mother and colt in tow, cloaks already coming off shoulders to layer the colt's back; word for word fulfilled.",
        "must_not_show": "no halo, glare or rim-light; the CLOAKS as saddle (v7) — dark garments being laid over the young colt's back.",
        "scene": (
            "Back at the roadside the errand "
            "returns fulfilled to the letter: "
            "the two leading mother and colt "
            "up to Jesus, and already the "
            "cloaks coming off shoulders — "
            "dark olive and slate laid gently "
            "layer on layer over the young "
            "colt's back for a poor man's "
            "saddle — every clause of the "
            "strange instruction checked off, "
            "and the animals standing calm "
            "at the centre of it as if "
            "they had always known the "
            "appointment. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r088-b08", "out": "s08-and-all-of-it-was.jpeg", "seg": "n0b",
        "window": "39.14-42.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["COLT"],
        "narration": "And all of it was exactly as the old prophecy had said, too.",
        "must_show": "the prophecy's furniture — close on the colt under its layered cloaks, the mother near: the humble mount of Zechariah's promise, standing ready in the morning light.",
        "must_not_show": "no halo, glare or rim-light; NO scroll or text imagery — the fulfilment carried by the animals themselves.",
        "scene": (
            "Close on the prophecy's chosen "
            "furniture: the small dark-grey "
            "colt standing patient under its "
            "borrowed saddle of layered "
            "cloaks, ears turning, the grey "
            "mother's muzzle resting near — "
            "five hundred years of promise "
            "narrowing down to this: not a "
            "warhorse in bronze barding but "
            "a village borrowing, young and "
            "unridden, waiting in the "
            "morning light for the meekest "
            "king. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r088-b09", "out": "s09-tell-ye-the-daughter-of.jpeg", "seg": "s5",
        "window": "43.54-50.64", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "COLT"],
        "narration": (
            "Tell ye the daughter of Sion, Behold, thy King cometh unto "
            "thee, meek, and sitting upon an ass, and a colt the foal of an "
            "ass."
        ),
        "must_show": "SCRIPTURE-EXACT: the verse enacted — Jesus seated on the cloak-saddled colt beginning the descent toward the distant gate, the mother donkey alongside; MEEK visible in his whole bearing.",
        "must_not_show": "no halo, glare or rim-light; the meekness the composition — no raised fist, no banner, a king at a donkey's walking pace.",
        "scene": (
            "The verse takes the road: Jesus "
            "seated on the small colt over "
            "its layered cloaks, the grey "
            "mother pacing alongside, the "
            "pale road tilting down between "
            "the olives toward Jerusalem's "
            "high gate — a king arriving at "
            "exactly a donkey's unhurried "
            "walking pace, hands loose on "
            "the mane, meekness riding where "
            "armour was expected — the "
            "daughter of Sion's strange "
            "promise, keeping itself. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r088-b10", "out": "s10-the-king-was-coming-but.jpeg", "seg": "n1b",
        "window": "52.15-55.50", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COLT"],
        "narration": "The King was coming — but not the kind they expected.",
        "must_show": "the unexpected kind — close on Jesus on the colt: no crown, no sword, warm steady face; kingship redefined at close range.",
        "must_not_show": "no halo, glare or rim-light; NOTHING martial anywhere on him — empty hands, plain cream wool, gentleness.",
        "scene": (
            "Close on the king the road is "
            "getting: no circlet on the dark "
            "hair, no sword at the rope "
            "belt, no herald clearing the "
            "way — just the warm steady face "
            "above the colt's flicking ears, "
            "hands empty and easy, the plain "
            "cream wool moving at the pace "
            "of the smallest animal in the "
            "parade — royalty rebuilt from "
            "the ground up out of gentleness, "
            "arriving in person. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r088-b11", "out": "s11-the-crowds-spread-their-cloaks.jpeg", "seg": "n1a",
        "window": "56.13-61.20", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "COLT", "CROWD"],
        "narration": (
            "The crowds spread their cloaks on the road, and cut branches "
            "from the trees, and lined his path."
        ),
        "must_show": "SCRIPTURE-EXACT: the carpeting (v8) — cloaks swirling down onto the road ahead of the colt, men in the trees cutting branches, the path becoming a laid carpet of garments and green.",
        "must_not_show": "no halo, glare or rim-light; the action MID-HAPPENING — cloaks in the air, branches falling, the carpet growing ahead of the hooves.",
        "scene": (
            "The road dresses itself ahead of "
            "him: dark cloaks swirling off "
            "shoulders and settling flat on "
            "the dust, a boy up an olive "
            "tree sawing at a branch, green "
            "boughs raining onto the growing "
            "carpet, families running forward "
            "to lay their own garments in "
            "the next bare gap — a poor "
            "crowd paving a king's highway "
            "with the coats off their backs, "
            "faster than the little colt can "
            "walk it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r088-b12", "out": "s12-and-the-people-shouted-as.jpeg", "seg": "n2",
        "window": "61.72-63.86", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "COLT", "CROWD"],
        "narration": "And the people shouted as he rode in:",
        "must_show": "the roar rising — the packed road erupting around the riding Jesus: mouths open, branches high, children on shoulders; the shout as a physical wave.",
        "must_not_show": "no halo, glare or rim-light; the crowd's JOY — open faces, lifted arms, never a mob's menace.",
        "scene": (
            "The packed road erupts: branches "
            "shooting up along both edges, "
            "children swung onto shoulders, "
            "hundreds of mouths opening on "
            "the same rising word as the "
            "colt picks its way over the "
            "cloaks — the shout rolling down "
            "the descent ahead of him like "
            "water finding a channel, joy "
            "with lungs behind it, a whole "
            "road deciding at the top of "
            "its voice who is riding "
            "through. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r088-b13", "out": "s13-hosanna-to-the-son-of.jpeg", "seg": "j1",
        "window": "64.51-71.20", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "COLT", "CROWD"],
        "narration": (
            "Hosanna to the son of David: Blessed is he that cometh in the "
            "name of the Lord; Hosanna in the highest."
        ),
        "must_show": "SCRIPTURE-EXACT: the hosanna at full flood — the whole road one cry around the meek rider: branches waving in rhythm, cloaks still falling, the gate nearing behind.",
        "must_not_show": "no halo, glare or rim-light; Jesus UNCHANGED at the centre of it — receiving the roar with meekness, not waving triumph.",
        "scene": (
            "The cry crests over the whole "
            "descent — HOSANNA — branches "
            "beating time along both walls "
            "of the crowd, the word rolling "
            "wave on wave over the cloak-"
            "carpeted road toward the great "
            "gate — and at the centre of the "
            "flood the one still point: the "
            "meek rider on the small colt, "
            "steady amid a roar that would "
            "turn any other head in the "
            "city, taking the throne-shout "
            "at a walking pace. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r088-b14", "out": "s14-hosanna-means-save-us-now.jpeg", "seg": "n2b",
        "window": "72.69-78.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": (
            "Hosanna means save us now. They were calling him King out "
            "loud, in the street, where everyone could hear it."
        ),
        "must_show": "the word's weight — close on shouting faces in the crowd: need underneath the joy; SAVE US NOW written in eyes as much as mouths.",
        "must_not_show": "no halo, glare or rim-light; the need HONEST — taxed, tired, occupied people shouting their actual hope.",
        "scene": (
            "Close on the faces doing the "
            "shouting: a farmer's cracked "
            "voice at full stretch, a "
            "mother's eyes wet above her "
            "open mouth, an old man's fist "
            "and branch raised together — "
            "and under the joy of every face "
            "the word's real cargo: save us "
            "NOW — taxed and occupied and "
            "tired people spending the most "
            "dangerous sentence in the "
            "empire, out loud, in the open "
            "street. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r088-b15", "out": "s15-the-whole-city-was-stirred.jpeg", "seg": "n3",
        "window": "79.00-83.87", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD"],
        "narration": (
            "The whole city was stirred. When they asked who this was, the "
            "crowd answered plainly."
        ),
        "must_show": "SCRIPTURE-EXACT: the city moved (v10) — inside the gate: heads filling windows and rooftops, shopkeepers abandoning stalls, the commotion pulling the whole city toward the sound.",
        "must_not_show": "no halo, glare or rim-light; the stirring CITY-WIDE — every storey of the street reacting at once.",
        "scene": (
            "Inside the great gate the city "
            "stirs storey by storey: heads "
            "crowding the windows, women "
            "leaning from rooftops with wash "
            "still in hand, a shopkeeper "
            "abandoning his stall mid-sale, "
            "boys sprinting down stairways "
            "toward the swelling noise — the "
            "whole stone hive turning on its "
            "axis toward one question coming "
            "up the street with the roar: "
            "who IS this? Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r088-b16", "out": "s16-and-when-he-was-come.jpeg", "seg": "j2",
        "window": "84.51-89.35", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "COLT", "CROWD"],
        "narration": (
            "And when he was come into Jerusalem, all the city was moved, "
            "saying, Who is this?"
        ),
        "must_show": "SCRIPTURE-EXACT: the entry through the gate — the colt and rider passing under the massive gate arch with the procession pouring after; the city's faces asking from every side.",
        "must_not_show": "no halo, glare or rim-light; the gate's SCALE over the small mount — empire's stone, meekness passing through it.",
        "scene": (
            "Under the gate's massive arch "
            "the procession pours: the small "
            "colt and its meek rider passing "
            "through cool stone shadow into "
            "the city's roar, branches and "
            "cloaks flooding after, and on "
            "every side the asking faces — "
            "leaned from sills, pressed in "
            "doorways, mouthing the same "
            "question over the noise — a "
            "king entering his capital "
            "through its own bewilderment, "
            "one donkey-stride at a time. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r088-b17", "out": "s17-and-the-multitude-said-this.jpeg", "seg": "j2",
        "window": "89.35-94.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": (
            "And the multitude said, This is Jesus the prophet of Nazareth "
            "of Galilee."
        ),
        "must_show": "SCRIPTURE-EXACT: the answer — crowd faces calling it up to the windows, proud and plain: the prophet, from Nazareth, in Galilee; the introduction shouted person to person.",
        "must_not_show": "no halo, glare or rim-light; the pride HOMELY — Galileans naming their own to the capital.",
        "scene": (
            "The answer goes up from the "
            "road to the windows, passed "
            "proud and plain from mouth to "
            "mouth: a Galilean farmer "
            "cupping his hands to call it "
            "to a sill, a woman repeating it "
            "to her neighbour with her chin "
            "high — THIS IS JESUS, THE "
            "PROPHET — OF NAZARETH — country "
            "people introducing their own to "
            "the capital that always looked "
            "down the road at them, and "
            "enjoying every syllable. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r088-b18", "out": "s18-who-is-this-the-city.jpeg", "seg": "n3b",
        "window": "95.81-97.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROAD"],
        "narration": "Who is this? the city asked.",
        "must_show": "the question close — faces at a window and a doorway mid-ask: brows up, hands spread, the city's honest bewilderment in two or three faces.",
        "must_not_show": "no halo, glare or rim-light; the asking GENUINE — curiosity, not hostility.",
        "scene": (
            "Close on the city's honest "
            "bewilderment: an old man leaning "
            "from his window with both hands "
            "spread at the noise, a "
            "shopkeeper in his doorway "
            "asking his neighbour with his "
            "brows alone, a girl on the "
            "stairs asking her mother — the "
            "same three words moving through "
            "every face in the frame, a "
            "capital city admitting at "
            "festival volume that it does "
            "not know who just came through "
            "its gate. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r088-b19", "out": "s19-and-the-answer-came-back.jpeg", "seg": "n3b",
        "window": "97.52-103.94", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD", "CROWD"],
        "narration": (
            "And the answer came back from the road — this is Jesus, the "
            "prophet, out of Nazareth in Galilee."
        ),
        "must_show": "the answer travelling — the street wide: the name relaying up from the procession to windows and rooftops, hands cupped, heads nodding it upward level by level.",
        "must_not_show": "no halo, glare or rim-light; the relay VISIBLE — the name climbing the buildings like a stair.",
        "scene": (
            "The name climbs the street like "
            "a stair: shouted up from the "
            "branch-waving road to the first "
            "windows, repeated from sill to "
            "rooftop, nodded across alleys "
            "and down again — JESUS — THE "
            "PROPHET — NAZARETH — level by "
            "level the answer scales the "
            "stone city until the rooftops "
            "have it too, a name walking up "
            "the walls of Jerusalem while "
            "its owner rides quietly along "
            "the bottom. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r088-b20", "out": "s20-he-came-not-with-swords.jpeg", "seg": "n4",
        "window": "104.52-111.35", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "COLT", "CROWD"],
        "narration": (
            "He came not with swords but with peace — riding on a donkey, "
            "the humble King the scriptures had promised."
        ),
        "must_show": "the closing image — the whole entry held: the meek rider on the small colt amid the branch-waving crowd inside the gate; peace's king, exactly as promised, fully arrived.",
        "must_not_show": "no halo, glare or rim-light; NOTHING martial in the frame — no soldier prominent, no weapon; the promise kept in gentleness.",
        "scene": (
            "The closing frame keeps the "
            "whole promise in one look: the "
            "small grey colt picking its "
            "gentle way up the cloak-strewn "
            "street, the meek rider steady "
            "and empty-handed above it, "
            "branches arching green over "
            "the roar, the great gate "
            "standing behind — a capital "
            "entered without one sword "
            "drawn, one order shouted, one "
            "door forced — the humble King "
            "of the old promise, arrived at "
            "last, at peace's own pace. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
]
