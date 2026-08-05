#!/usr/bin/env python3
"""V2 beat map — row 137, build-137-one-as-we-are-one (John 17:20-23).

COVERAGE: 13 pictures over 74.7 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (John 17 KJV):
  17:20 "Neither pray I for these alone, but for them also WHICH
        SHALL BELIEVE ON ME THROUGH THEIR WORD" — the prayer reaches
        every future believer, including the viewer.
  17:21 "that they all may be ONE; AS thou, Father, art in me, and I
        in thee, that they also may be one IN US."
  17:22 "the GLORY which thou gavest me I HAVE GIVEN THEM; that they
        may be one, EVEN AS WE ARE ONE."
  Setting: the night before the crucifixion, after the supper, on
        the way to the garden — a moonlit olive grove above the
        Kidron, the city's lights behind.

RENDERING LAWS (doctrine row — handle exactly):
  - THE FATHER IS NOT EMBODIED IN THIS ROW: John 17 shows Jesus
    PRAYING to him — the communion is carried by Jesus's upturned
    face, the deep night sky, and warmth in the light; no figure
    ever (scripture-hides class; the row-113 body-order applies
    only where scripture shows him).
  - THE ONENESS IS UNITY OF DISTINCT PERSONS, never fusion: b07/b08
    must show crowds/groups of utterly DISTINCT faces — no merging,
    no blending, no composite-face imagery, ever. The unity images
    are period-true pairs in one work: two oxen in ONE yoke (b09),
    father and son hauling one net in matched stroke (b11).
  - The future believers appear as far warm WINDOW-LIGHTS across
    the night valley (b03/b13) — countless, individual, each its
    own light; never a faceless mass.
  - Night throughout is DELIBERATE (the row-11 storm defect does
    not apply): moonlight, a small watch-fire, the city's lamps —
    every light physical.
  - Jesus's prayer posture: standing with arms open and face
    lifted, or kneeling — reverent, strong, never collapsed (this
    is John 17's confident intercession, not Gethsemane's agony).

TIME OF DAY ARC (intentional): one moonlit night throughout — deep
blue, silver olives, warm small fire, far warm windows; the unity
vignettes (b09/b11) in golden late-afternoon memory-light BY DESIGN
(they are illustrations, not the night's events).

CHANGING CONDITION (kept OUT of the locks): none material — one
night, one prayer, two illustrative asides.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "GROVE": (
        "GROVE LOCK: the night grove — silver-leaved olive trees on "
        "a moonlit slope above the Kidron valley, the city's warm "
        "lamplit walls and windows across the dark valley behind, "
        "a small low watch-fire; deep blue night, every light "
        "physical. The same slope and view throughout."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the disciples — a small knot of the "
        "Eleven a few steps behind, travel-cloaked in earth-toned "
        "robes of brown, rust, olive and slate (no cream — only "
        "Jesus wears cream), faces warm in the low firelight; "
        "varied, quiet, listening."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r137-b01", "out": "s01-the-night-before-he-died.jpeg", "seg": "n0",
        "window": "0.28-2.74", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "DISCIPLES"],
        "narration": "The night before he died, Jesus stopped to pray.",
        "must_show": "the stopping — the moonlit grove above the valley, Jesus stepped a few paces ahead and stilled into prayer, the disciples pausing behind; the night holding its breath.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the night DELIBERATE — moon, watch-fire, far city lamps only.",
        "scene": (
            "The last night finds him praying first, the camera "
            "set low behind the disciples' cloaked backs: on "
            "the moonlit slope among the silver olives Jesus "
            "has stepped a few paces ahead and stopped — face "
            "lifting, shoulders squaring into prayer — while "
            "the little knot of the Eleven halts behind him in "
            "the blue dark, the city's warm windows scattered "
            "across the valley at their backs — the night "
            "before the cross, being spent the way he spent "
            "every crisis: talking to his Father first. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r137-b02", "out": "s02-that-includes-you.jpeg", "seg": "n0",
        "window": "9.02-10.45", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "That includes you.",
        "must_show": "the inclusion — close on Jesus's praying face, warm and certain, the prayer's reach wider than the night; intimacy aimed forward through time.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the warmth PERSONAL — a prayer that knows its addressees by heart.",
        "scene": (
            "Three words close the distance of twenty "
            "centuries: close on Jesus's face in the "
            "moonlight, mid-prayer — and the warmth in it is "
            "not general: it is the particular certainty of "
            "a man naming people he can already see, "
            "believers not yet born, readers not yet "
            "reading, the whole future company folded "
            "personally into the petition — that includes "
            "YOU, the face says, and has always said, since "
            "the night it first said it. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r137-b03", "out": "s03-and-in-that-prayer-he.jpeg", "seg": "n0",
        "window": "2.74-9.02", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "And in that prayer, he prayed for someone you might not expect "
            "— for everyone who would ever believe."
        ),
        "must_show": "the prayer's reach — over Jesus's praying shoulder, the night valley scattered with countless far warm window-lights; every future believer a light of its own.",
        "must_not_show": "no halo; the lights INDIVIDUAL — countless distinct warm windows, never a glow-mass; each its own.",
        "scene": (
            "The prayer's mailing list is visible over his "
            "shoulder: past the praying profile the dark "
            "valley falls away scattered with warm window-"
            "lights — dozens near, hundreds far, pricking on "
            "toward the horizon until they grain into the "
            "dark — each one a household, a lamp, a life — "
            "and the prayer moving out over all of them and "
            "onward, to windows not yet built and believers "
            "not yet born, everyone who would ever believe, "
            "one light at a time. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r137-b04", "out": "s04-neither-pray-i-for-these.jpeg", "seg": "j1",
        "window": "10.99-26.55", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE", "DISCIPLES"],
        "narration": (
            "Neither pray I for these alone, but for them also which shall "
            "believe on me through their word; that they all may be one; as "
            "thou, Father, art in me, and I in thee, that they also may be "
            "one in us."
        ),
        "must_show": "SCRIPTURE-EXACT: the great intercession — Jesus standing with arms open and face lifted to the deep night sky, the disciples listening beyond the small fire; confident intercession, not agony.",
        "must_not_show": "ABSOLUTE: no figure in the sky — the Father unseen; Jesus's posture STRONG and open, never collapsed.",
        "scene": (
            "The great intercession is prayed standing, like "
            "a son at ease in his father's house: Jesus with "
            "his arms open and his face lifted full to the "
            "deep star-strewn night, the words moving "
            "unhurried through the grove — not for these "
            "ALONE, but for all who will ever believe "
            "through their word — while beyond the low "
            "watch-fire the Eleven listen with the "
            "stillness of men hearing themselves prayed "
            "over — the longest reach of any prayer ever "
            "prayed, launched calm into the listening dark. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r137-b05", "out": "s05-listen-to-how-he-asks.jpeg", "seg": "n1",
        "window": "28.07-29.37", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "Listen to how he asks.",
        "must_show": "the how — very close on the praying face: the precision and intimacy of the asking; a son speaking to a father he knows completely.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the intimacy the whole frame — moonlit features, moving lips.",
        "scene": (
            "The grammar of the prayer is on his face: very "
            "close in the moonlight, the lips moving with "
            "unhurried precision, the brows easy, the eyes "
            "lifted with the confidence of a son who has "
            "never once been refused — no formula in it, no "
            "performance, no strain — asking the way you ask "
            "someone whose heart you have known from before "
            "the world was: exactly, warmly, and certain of "
            "the answer's character in advance. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r137-b06", "out": "s06-he-prays-that-his-followers.jpeg", "seg": "n1",
        "window": "29.37-34.34", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE", "DISCIPLES"],
        "narration": (
            "He prays that his followers will be one — the same way he and "
            "his Father are one."
        ),
        "must_show": "the model named — Jesus's upturned communing face, and his open hand turned back toward the listening disciples: the AS...SO of the prayer in one composition.",
        "must_not_show": "ABSOLUTE: no figure in the sky; the hand's gesture linking sky-ward communion to the men behind him.",
        "scene": (
            "The prayer draws its great AS-SO in the night "
            "air: Jesus's face holds its upward communion — "
            "the oneness he lives in, Father and Son, older "
            "than light — while his open hand turns back "
            "toward the fire-lit knot of his followers: AS "
            "we are one, the gesture runs, SO let them be — "
            "the highest friendship in existence held up as "
            "the pattern for eleven tired men and every "
            "believer after them, one hand linking the sky "
            "to the fire. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r137-b07", "out": "s07-if-that-oneness-meant-one.jpeg", "seg": "n2",
        "window": "34.89-41.86", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "If that oneness meant one single being, this prayer would be "
            "asking millions of believers to melt into one person."
        ),
        "must_show": "the reductio pictured RIGHT — a great gathering of utterly DISTINCT faces filling a sunlit slope: every age, every feature unique and crisp; what the prayer does NOT ask made visible by its opposite.",
        "must_not_show": "ABSOLUTE: no merging, no blending, no composite faces, no blur between persons — every face individual and clear.",
        "scene": (
            "Run the wrong reading and look at what it would "
            "cost: a whole slope of believers gathered in "
            "warm daylight — old women and young men, "
            "children on shoulders, faces round and lean and "
            "lined and bright, every single one crisply "
            "itself, no two alike from front row to ridge — "
            "millions of exactly THESE, distinct to the last "
            "eyelash — which is precisely what a melted-"
            "together oneness would erase, and precisely "
            "what the prayer never asks. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r137-b08", "out": "s08-it-ask-that.jpeg", "seg": "n2",
        "window": "41.86-43.42", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "It doesn't ask that.",
        "must_show": "the distinctness close — four believers side by side, shoulder to shoulder, each face utterly individual; unity of persons, persons intact.",
        "must_not_show": "ABSOLUTE: no blending — four distinct faces, four distinct persons, one warm line.",
        "scene": (
            "Four faces answer the misreading at close "
            "range: an old fisherman, a young mother, a "
            "grey scribe, a girl of twelve — shoulder to "
            "shoulder in the warm light, arms linked down "
            "the little line — and every face entirely, "
            "unmistakably its own: four histories, four "
            "voices, four pairs of once-in-creation eyes — "
            "standing close enough to share one breath and "
            "remaining, gloriously, four — which is the only "
            "oneness the prayer ever wanted. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r137-b09", "out": "s09-it-asks-for-perfect-unity.jpeg", "seg": "n2",
        "window": "43.42-46.87", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "It asks for perfect unity between distinct persons.",
        "must_show": "the period image of unity — TWO distinct oxen in ONE yoke drawing one straight furrow in golden light; different animals, one work, one line.",
        "must_not_show": "no halo; the oxen visibly DIFFERENT (one darker, one lighter); the furrow dead straight — the unity in the work.",
        "scene": (
            "The farm has always known what the theologians "
            "argue about: two oxen — one dark, one dun, "
            "different beasts entirely — walk the field in "
            "ONE wooden yoke, and behind them the furrow "
            "runs dead straight through the golden "
            "afternoon — two strengths, two wills, two "
            "hearts beating out of step and pulling in "
            "perfect step — distinct persons, one work, one "
            "line across the world: unity, as every farmer "
            "and every Father defines it. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r137-b10", "out": "s10-and-the-glory-which-thou.jpeg", "seg": "j2",
        "window": "47.45-59.98", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE", "DISCIPLES"],
        "narration": (
            "And the glory which thou gavest me I have given them; that they "
            "may be one, even as we are one: I in them, and thou in me, that "
            "they may be made perfect in one."
        ),
        "must_show": "SCRIPTURE-EXACT: the glory given DOWNWARD — Jesus's open hands turning from the sky toward the disciples, whose faces are lit warm by the fire; the passing-on of glory as gesture and firelight.",
        "must_not_show": "ABSOLUTE: no light effects, no shining — the fire's physical warmth on the disciples' faces carries 'glory given'; no figure in the sky.",
        "scene": (
            "The richest transfer in the prayer moves "
            "downhill: Jesus's open hands turn from the "
            "night sky toward his men — the GLORY thou "
            "gavest me, I have GIVEN them — and around the "
            "low watch-fire the Eleven's faces sit lit in "
            "honest physical warmth, fishermen and tax-men "
            "gilded ordinary gold by flame — the inheritance "
            "of heaven handed down the slope in a gesture, "
            "toward faces that do not yet know what they "
            "are holding — that they may be made perfect in "
            "one. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r137-b11", "out": "s11-two-persons-one-heart.jpeg", "seg": "n3",
        "window": "67.58-69.94", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Two persons, one heart.",
        "must_show": "the human picture — an old father and grown son hauling ONE net in perfectly matched stroke on a golden shore; two distinct silhouettes, one motion.",
        "must_not_show": "no halo; the two CLEARLY distinct (age, build); the matched pull the picture.",
        "scene": (
            "The lakeshore stages the doctrine at sunset: an "
            "old father and his grown son lean back on ONE "
            "net-rope in perfectly matched stroke — grey "
            "beard and dark, bent back and straight, two "
            "unmistakably different men — and the net comes "
            "up the shingle in one smooth run because their "
            "four hands pull as two: rhythm learned over "
            "ten thousand hauls until the wills merged and "
            "the persons never did — two persons, one "
            "heart, and a full net to show for it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r137-b12", "out": "s12-the-father-and-the-son.jpeg", "seg": "n3",
        "window": "61.57-67.58", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "The Father and the Son are perfectly one — one in purpose, one "
            "in love, one in glory."
        ),
        "must_show": "the communion itself — Jesus's face in perfect peace mid-prayer, the night sky above rich and warm-toned around the moon; the oneness carried by his complete at-homeness; NO figure.",
        "must_not_show": "ABSOLUTE: no figure in the sky, no light effects — the at-homeness of the praying face is the doctrine.",
        "scene": (
            "What perfect oneness looks like from the Son's "
            "side of it: Jesus's face in the moonlight has "
            "gone entirely to peace — not the peace of "
            "finishing but of BELONGING, a man at home in a "
            "conversation older than the stars over him — "
            "the deep sky rich and warm around the moon as "
            "if the night itself leaned closer — one in "
            "purpose, one in love, one in glory, and all of "
            "it readable in the perfect unguarded ease of a "
            "face turned toward its Father. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r137-b13", "out": "s13-and-jesus-prayed-that-you.jpeg", "seg": "n3",
        "window": "69.94-74.39", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE", "DISCIPLES"],
        "narration": "And Jesus prayed that you would be brought into that same oneness.",
        "must_show": "the closing arc — Jesus's open hand sweeping from the sleeping-close disciples out over the valley's countless warm windows; everyone gathered into the same prayer's circle.",
        "must_not_show": "no halo; the arc INCLUDES — fire-lit disciples near, individual far windows beyond; the reach personal to the viewer's side of the frame.",
        "scene": (
            "The prayer's last arc gathers everybody it can "
            "reach: Jesus's open hand sweeps from the "
            "Eleven drowsing warm by the fire, out across "
            "the dark valley where the window-lights burn "
            "one by one to the horizon — the same motion "
            "taking in fishermen and far households and "
            "futures unbuilt, every distinct light invited "
            "into the same oneness the Son has with the "
            "Father — a circle drawn at night on a "
            "hillside, still open, still gathering, with "
            "room in its sweep for you. Every figure has "
            "two arms, two hands and one head."
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
