#!/usr/bin/env python3
"""V2 beat map — row 26, build-26-mustard-seed (Matthew 13:31-32).

COVERAGE: 14 pictures over 79.4 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 13:31-32 KJV):
  v31   "Another parable put he forth unto them" — the SAME seaside teaching
        day as rows 24 and 25 (Matthew 13:1-2, Jesus in the boat, crowd on
        the shore). Rows 24 and 25 staged it from the hillside, the
        waterline and from inside the boat — so THIS build stages the frame
        from IN AMONG THE CROWD, looking over heads toward the boat, and
        (for the second frame beat) from low along the water with the boat
        in profile. Same occasion, fourth and fifth compositions, no
        repeated picture across the library.
  v31   "a grain of mustard seed, which a MAN took, and SOWED IN HIS FIELD"
        — one man, one deliberate planting.
  v32   "the LEAST of all seeds: but when it is grown, it is the GREATEST
        among herbs, and becometh a TREE, so that the BIRDS OF THE AIR come
        and LODGE IN THE BRANCHES thereof" — the scale contrast is the whole
        parable: a speck in a palm → a tree with nesting birds.

TIME OF DAY: the frame beats at the sea are bright morning. The parable's
growth arc moves through days on purpose — morning planting, fresh days of
young growth, and the full-grown tree in warm late-afternoon gold for the
sheltering-birds beats. The interpretation vignette (b13) is a dim lamplit
interior at night — a deliberate small-and-quiet frame, not a defect.

CONTENT-CARE: row 26 has no flag in §3. Nothing sensitive.

CHANGING CONDITION (kept OUT of the locks): the plant itself — seed, first
sprout, waist-high sapling, full spreading tree — changes beat to beat and
is never locked. The GARDEN lock carries only the unchanging ground.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "PLANTER": (
        "PLANTER LOCK: the man who sows the seed is the same man in every "
        "shot — mid-forties, medium build, with a short black beard, heavy "
        "dark brows and careful deliberate hands. He wears a DARK OLIVE-BROWN "
        "wool tunic with a plain leather belt and worn sandals (never cream, "
        "never white). His face is shown clearly."
    ),
    "GARDEN": (
        "GARDEN LOCK: a small walled garden-field on the edge of a village — "
        "a rectangle of dark tended earth inside a low honey-stone wall, a "
        "wooden gate in one corner, rows of low herbs along the far side, a "
        "clay water jar by the gatepost, and the village's flat rooftops and "
        "one distant hill visible beyond the wall. The same wall, gate, jar "
        "and hill appear in every garden beat."
    ),
    "SHORE-CROWD": (
        "SHORE CROWD LOCK: the crowded curve of a pebble beach on the Sea of "
        "Galilee seen from within the multitude — listeners of every age "
        "packed close, dressed in SATURATED DEEP earth colours: dark "
        "chocolate brown, deep russet, dark olive, burnt ochre, dusty indigo "
        "and faded plum wool (never cream, never white; only Jesus wears "
        "cream) — and beyond them the bright green-blue water with a small "
        "weathered wooden fishing boat floating a few boat-lengths off the "
        "beach. Bright morning light."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r026-b01", "out": "s01-jesus-told-a-story-about.jpeg", "seg": "n0",
        "window": "0.28-3.44", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SHORE-CROWD"],
        "narration": "Jesus told a story about the smallest seed a farmer knew.",
        "must_show": "SCRIPTURE-EXACT: from IN AMONG the shore crowd, over shoulders and heads, the small boat on the bright water with Jesus seated in it teaching — the listener's own view.",
        "must_not_show": "no halo, glare or rim-light on Jesus; he is seated in the boat; nobody stands on the water.",
        "scene": (
            "From inside the standing crowd on the beach, the camera at "
            "shoulder height among them: the dark-clothed backs and turned "
            "heads of listeners frame a channel of bright green-blue water, "
            "and out on it the small wooden boat rides at anchor with Jesus "
            "seated in it, one hand lifted mid-story, small but unmistakably "
            "the point every face is fixed on. Morning sun scatters light "
            "across the water between. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r026-b02", "out": "s02-it-was-a-mustard-seed.jpeg", "seg": "n1",
        "window": "4.01-8.93", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLANTER"],
        "narration": (
            "It was a mustard seed — so tiny it could be lost in the palm of "
            "your hand."
        ),
        "must_show": "SCRIPTURE-EXACT: a very close shot of one single mustard seed — a near-invisible speck — resting in the deep creases of an open work-worn palm.",
        "must_not_show": "no halo, glare or rim-light; ONE seed only, genuinely tiny against the whole hand — never a pile.",
        "scene": (
            "A very close shot of a man's open work-worn palm filling the "
            "frame in clear morning light: at its centre, almost lost in "
            "the creases of the skin, sits one single round mustard seed — "
            "a pale-brown speck smaller than the smallest crease is wide. "
            "The scale between hand and seed is the whole picture. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r026-b03", "out": "s03-of-all-the-seeds-he.jpeg", "seg": "n3",
        "window": "13.45-17.91", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Of all the seeds he could have sown, it was just about the "
            "smallest of them all."
        ),
        "must_show": "the comparison — the one mustard seed lying beside visibly larger seeds (wheat, lentil, bean) on rough cloth; smallest by far.",
        "must_not_show": "no halo, glare or rim-light; the mustard seed must be OBVIOUSLY the smallest thing on the cloth.",
        "scene": (
            "A close still shot on a square of rough dark cloth in morning "
            "light: a short row of seeds laid out side by side — a broad "
            "bean, a lentil, a plump grain of wheat, a barley corn — and at "
            "the row's end, dwarfed by every one of them, the single round "
            "mustard seed, small as a pinhead beside the rest. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r026-b04", "out": "s04-a-man-took-that-one.jpeg", "seg": "n2",
        "window": "9.47-12.91", "wide": True, "jesus": False, "ref": False,
        "locks": ["PLANTER", "GARDEN"],
        "narration": "A man took that one little seed and planted it in his field.",
        "must_show": "SCRIPTURE-EXACT: the deliberate planting — the man kneeling in his walled garden, pressing the seed into a small opened pocket of dark earth with one fingertip.",
        "must_not_show": "no halo, glare or rim-light; one seed, one small hole — an act of intention, not broadcast sowing.",
        "scene": (
            "In the small walled garden in clear morning light the man "
            "kneels over a patch of freshly turned dark earth, pressing his "
            "single tiny seed down into a small fingertip hole, his other "
            "hand cupped beside it against the breeze, his heavy brows bent "
            "in complete attention on the speck. The low stone wall, the "
            "wooden gate and the clay jar stand quiet around him, the "
            "village rooftops beyond. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r026-b05", "out": "s05-the-kingdom-of-heaven-is.jpeg", "seg": "j1",
        "window": "18.47-27.85", "wide": True, "jesus": False, "ref": False,
        "locks": ["PLANTER", "GARDEN"],
        "narration": (
            "The kingdom of heaven is like to a grain of mustard seed, which a "
            "man took, and sowed in his field: which indeed is the least of all "
            "seeds:"
        ),
        "must_show": "SCRIPTURE-EXACT: the planting completed — the man smoothing the earth flat over the buried seed with his palm, the spot now indistinguishable from the rest of the ground.",
        "must_not_show": "no halo, glare or rim-light; the covered spot must look like NOTHING — bare smoothed earth, the least promising picture in the row.",
        "scene": (
            "The man kneels back on his heels in the walled garden, one "
            "palm smoothing the last of the dark earth flat over the buried "
            "seed — and the spot he has planted is now nothing at all, a "
            "hand's width of bare smoothed soil identical to every other "
            "hand's width around it. He looks down at the unmarked ground "
            "with quiet certainty. Morning light lies plain on the empty "
            "earth. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r026-b06", "out": "s06-but-that-tiny-seed-did.jpeg", "seg": "n4",
        "window": "41.52-43.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "But that tiny seed did not stay small.",
        "must_show": "the first sprout — two small green seed-leaves just broken through the bare earth at the planted spot, dew on them, morning light.",
        "must_not_show": "no halo, glare or rim-light; the sprout is tiny — a thumb-height pair of leaves, nothing more yet.",
        "scene": (
            "A close shot at soil level, upright and level, the dark earth "
            "at the bottom of the frame: at the once-bare spot a single "
            "tiny sprout has broken through — a thin pale-green stem no "
            "taller than a thumb carrying two small round seed-leaves, dew "
            "beaded on their edges, throwing one thread of shadow in the "
            "low fresh morning light. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r026-b07", "out": "s07-but-when-it-is-grown.jpeg", "seg": "j1b",
        "window": "29.39-40.07", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": (
            "but when it is grown, it is the greatest among herbs, and becometh "
            "a tree, so that the birds of the air come and lodge in the "
            "branches thereof."
        ),
        "must_show": "SCRIPTURE-EXACT: the full promise in one frame — the mustard tree grown broad and tall over the garden wall, birds arriving and settled through its spreading branches.",
        "must_not_show": "no halo, glare or rim-light; the tree must dominate the walled garden that once dwarfed the seed — taller than the wall, wider than the herb rows.",
        "scene": (
            "The walled garden transformed in warm afternoon light: a great "
            "spreading mustard tree stands where the bare spot was, its "
            "trunk thick as a man's arm and its broad branching crown "
            "reaching well above the low stone wall and out over the herb "
            "rows — and birds are everywhere in it, three gliding in on "
            "spread wings, others already perched deep among the green "
            "branches. The little wooden gate and clay jar sit tiny beneath "
            "it. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r026-b08", "out": "s08-quietly-slowly-it-began-to.jpeg", "seg": "n4",
        "window": "43.85-46.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLANTER", "GARDEN"],
        "narration": "Quietly, slowly, it began to grow.",
        "must_show": "the young plant now knee-high and leafing out, and the man crouched beside it, watering it from a cupped hand — patient tending.",
        "must_not_show": "no halo, glare or rim-light; knee-high stage only — clearly between sprout and tree.",
        "scene": (
            "In soft bright daylight the young mustard plant stands "
            "knee-high at its spot, a slender green stem with its first "
            "true spreading leaves — and the man crouches on his heels "
            "beside it, pouring a thin stream of water from his cupped "
            "hand at its base, the clay jar tipped ready in his other arm, "
            "his face bent close and patient over the small green thing. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r026-b09", "out": "s09-up-out-of-the-ground.jpeg", "seg": "n5",
        "window": "47.11-54.31", "wide": True, "jesus": False, "ref": False,
        "locks": ["PLANTER", "GARDEN"],
        "narration": (
            "Up out of the ground, higher and higher, until it became the "
            "largest plant in the whole garden — a tall, spreading tree."
        ),
        "must_show": "the scale reversal — the man standing UNDER his own plant now, looking up into branches over his head, the herb rows small below it.",
        "must_not_show": "no halo, glare or rim-light; the man must be visibly smaller than the tree — the seed that fit his palm now roofs him.",
        "scene": (
            "In warm late-day light the man stands at the foot of the "
            "grown mustard tree with his head tipped fully back, one hand "
            "resting on its trunk, looking up into the broad green crown "
            "spreading above him higher than the garden wall — the whole "
            "rows of lesser herbs lying low and small across the garden "
            "floor around its shade. The camera stands back to hold man "
            "and tree in one frame, him small beneath it. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r026-b10", "out": "s10-and-the-wild-birds-came.jpeg", "seg": "n6",
        "window": "54.84-59.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": (
            "And the wild birds came and built their nests in its broad, "
            "sheltering branches."
        ),
        "must_show": "SCRIPTURE-EXACT: close inside the branches — a finished woven nest lodged in a fork with a small bird settled on it, others perched near, deep green shelter all around.",
        "must_not_show": "no halo, glare or rim-light; the nest is complete and OCCUPIED — home, not just a perch.",
        "scene": (
            "Close inside the mustard tree's crown in warm dappled "
            "afternoon light: a neat woven nest of grass and twigs sits "
            "lodged in the fork of two branches with a small brown-and-buff "
            "bird settled down into it, while two more birds perch on the "
            "surrounding limbs among the broad green leaves — a whole "
            "sheltered world inside the branches. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r026-b11", "out": "s11-that-jesus-said-is-what.jpeg", "seg": "n7",
        "window": "60.00-63.16", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SHORE-CROWD"],
        "narration": "That, Jesus said, is what God's kingdom is like.",
        "must_show": "back at the sea — the boat in profile low along the bright water, Jesus seated and easy, the crowded shore curving beyond; a fresh angle on the teaching frame.",
        "must_not_show": "no halo, glare or rim-light on Jesus; seated in the boat; nobody stands on the water.",
        "scene": (
            "From low along the water off the boat's side: the small "
            "weathered fishing boat in full profile on the bright "
            "green-blue sea, Jesus seated amidships with one hand resting "
            "open on the gunwale, finishing the story — and beyond the "
            "boat the whole curved beach of listeners and the grassy "
            "hillside above it, faces small and turned toward him. Morning "
            "light lies in a moving band across the water between. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r026-b12", "out": "s12-it-almost-never-begins-big.jpeg", "seg": "n8",
        "window": "63.65-65.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "It almost never begins big.",
        "must_show": "the truth restated small — the tiny sprout again at soil level, dwarfed this time by an ordinary sandalled foot passing on the path beside it, unnoticed.",
        "must_not_show": "no halo, glare or rim-light; the foot passes BY the sprout, never over or onto it — overlooked, not endangered.",
        "scene": (
            "A close shot at soil level, upright and level: the tiny "
            "two-leafed mustard sprout standing in the dark earth at the "
            "frame's centre — and passing on the packed path beside it, "
            "blurred with motion and huge by comparison, a man's worn "
            "sandalled foot mid-stride, its owner walking on unaware. The "
            "sprout stands unnoticed and unharmed in the morning light. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r026-b13", "out": "s13-it-begins-small-a-whispered.jpeg", "seg": "n8",
        "window": "65.30-71.96", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "It begins small — a whispered prayer, a single kind act, one quiet "
            "change of heart."
        ),
        "must_show": "the smallest human beginning — an old woman kneeling alone at night by one small clay lamp, head bowed over folded hands in whispered prayer.",
        "must_not_show": "no halo, glare or rim-light; one small lamp flame is the only light and it stays small — an intimate dim room, not a radiant scene.",
        "scene": (
            "A small dim room at night: an old woman in a dark madder-red "
            "shawl kneels on a rush mat beside her low bed, her grey head "
            "bowed low over tightly folded hands, lips just parted in a "
            "whispered prayer — and the room's only light is one small "
            "clay oil lamp on the floor beside her, its single steady "
            "flame warming her face and hands and leaving all the corners "
            "dark. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r026-b14", "out": "s14-but-god-takes-that-smallest.jpeg", "seg": "n9",
        "window": "72.51-79.15", "wide": True, "jesus": False, "ref": False,
        "locks": ["PLANTER", "GARDEN"],
        "narration": (
            "But God takes that smallest beginning and grows it into something "
            "far greater than anyone could have imagined."
        ),
        "must_show": "the closing frame — the great tree in warm golden late light with birds through its crown, the man resting in its shade with children from the village, shelter for many from one seed.",
        "must_not_show": "no halo, glare or rim-light; the tree shelters PEOPLE now too — the frame is generous, full and warm.",
        "scene": (
            "Warm golden late afternoon: the great mustard tree fills the "
            "walled garden with broad shade, birds perched and gliding "
            "through its high branches — and beneath it the man sits "
            "resting against the trunk while two village children crouch "
            "in the cool shade nearby watching the birds above, the wooden "
            "gate standing open behind them. The low sun lays long warm "
            "light across the wall and the herb rows. The camera stands "
            "back to hold the whole sheltering tree and everyone under "
            "it. Every figure has two arms, two hands and one head."
        ),
    },
]
