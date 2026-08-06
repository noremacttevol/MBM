#!/usr/bin/env python3
"""V2 beat map — row 46, build-46-seed-growing (Mark 4:26-29).

COVERAGE: 32 pictures over 180.8 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 4:26-29 KJV):
  v26   "as if a man should CAST SEED into the ground" — the Mark 4
        seaside teaching day. Rows 24-27 staged the boat from five angles;
        THIS row's single frame beat (b01) is Jesus at REST against the
        beached boat at evening — the restful frame for the restful
        parable; no repeat.
  v27   "and should SLEEP, and RISE night and day, and the seed should
        spring and grow up, HE KNOWETH NOT HOW" — the farmer's ordinary
        life IS the parable: sleeping, rising, weeks passing. The
        underground beats show the seed working in the dark soil where
        he cannot see — cross-soil close-ups are correct and wanted.
  v28   "the earth bringeth forth fruit OF HERSELF; first the BLADE, then
        the EAR, after that the FULL CORN in the ear" — the three growth
        stages each get their own beat, in order, unrushed.
  v29   "when the fruit is brought forth, immediately he putteth in the
        SICKLE, because the HARVEST is come" — the joyful ending; the
        sickle is a harvest tool in glad hands, nothing else.
  The narration's pastoral point: the growing was never the farmer's job
  — rest is the row's whole temperature. No tension anywhere; the
  gentlest row in the section.

TIME OF DAY: the frame beat is warm dusk at the shore. The parable runs
real farm time — sowing morning, home at evening, NIGHT for the sleeping
beats (deep, peaceful night — correct), fresh mornings for the rising,
soft days for the growth stages, full gold for the harvest. The
underground beats are dark soil with the faint warmth of life, never a
light source in the ground.

CONTENT-CARE: row 46 has no flag in §3. Nothing sensitive anywhere.

CHANGING CONDITION (kept OUT of the locks): the field's season — bare
tilth, first blades, green ears, full gold — and the farmer's rhythm of
sleep and rising. All stated per-beat.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "FARMER": (
        "FARMER LOCK: the farmer is the same man in every shot — about "
        "fifty-five, comfortable and settled, with a round weathered "
        "face, a thick grey-brown beard, easy eyes and unhurried "
        "movements. He wears a soft DARK BARLEY-BROWN tunic with a "
        "wide cloth belt and worn boots (never cream, never white). "
        "His face is shown clearly — rest is its natural setting."
    ),
    "FIELD": (
        "FIELD LOCK: one modest sloping barley field behind the "
        "farmer's house — a low thorn hedge on two sides, a footpath "
        "along the upper edge, a single flat sitting-stone at the "
        "corner, and low hills beyond. The same hedge, path, stone and "
        "hills in every field beat, whatever the season."
    ),
    "HOUSE": (
        "FARMHOUSE LOCK: the farmer's small stone house at the field's "
        "edge — one warm-lit doorway, a bench against the south wall, "
        "a fig tree by the corner, and a low bedroom window that looks "
        "out over the field. The same door, bench, tree and window "
        "throughout."
    ),
    "SHORE": (
        "EVENING SHORE LOCK: the Sea of Galilee beach at dusk — the "
        "fishing boat drawn up on the pebbles with its hull dark and "
        "keel-line tilted, nets spread to dry, the water lying calm "
        "and pewter-pink, and the day's crowd gone home. Deep warm "
        "dusk light."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r046-b01", "out": "s01-this-might-be-the-most.jpeg", "seg": "n1",
        "window": "0.28-2.92", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SHORE"],
        "narration": "This might be the most restful thing he ever said.",
        "must_show": "the restful frame — Jesus at ease against the beached boat's hull at dusk, the crowd gone, the water calm; rest embodied before the parable of rest.",
        "must_not_show": "no halo, glare or rim-light on Jesus; genuine ease — shoulders down, the day's teaching done.",
        "scene": (
            "In the deep warm dusk on the empty beach Jesus "
            "sits at ease on the pebbles with his back "
            "against the beached boat's dark hull, knees "
            "drawn loosely up, hands at rest — the drying "
            "nets spread beside him, the water lying calm "
            "and pewter-pink to the far hills, the day's "
            "thousands gone home — a teacher resting against "
            "wood, about to describe how the whole kingdom "
            "rests too. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r046-b02", "out": "s02-it-is-about-a-farmer.jpeg", "seg": "n1",
        "window": "2.92-11.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER", "FIELD", "HOUSE"],
        "narration": (
            "It is about a farmer, and a field, and the one part of the whole "
            "process that is never, not for one second, up to you."
        ),
        "must_show": "the whole cast introduced — the farmer at his field's edge in morning light, the bare tilled slope before him, his small house behind; man, field, and the invisible third party.",
        "must_not_show": "no halo, glare or rim-light; the field bare and expectant — the story's stage before its first seed.",
        "scene": (
            "In fresh morning light the round-faced farmer "
            "stands at his field's upper path with his "
            "thumbs in his cloth belt, surveying the bare "
            "tilled slope that runs down from his boots to "
            "the thorn hedge — his small stone house and its "
            "fig tree at his back, the seed bag waiting on "
            "the flat sitting-stone at the corner — a man, a "
            "field, and somewhere in the arrangement a third "
            "party the picture cannot show. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b03", "out": "s03-so-is-the-kingdom-of.jpeg", "seg": "jv26",
        "window": "12.26-17.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER", "FIELD"],
        "narration": (
            "So is the kingdom of God, as if a man should cast seed into the "
            "ground;"
        ),
        "must_show": "SCRIPTURE-EXACT: the cast — the farmer mid-fling down the slope, the seed's wide fan in the air, morning light behind the falling grain.",
        "must_not_show": "no halo, glare or rim-light; the classic broadcast throw — easy, practised, unlaboured.",
        "scene": (
            "Down the tilled slope the farmer walks mid-"
            "fling, his arm swept out and a wide fan of "
            "barley seed hanging in the morning air ahead of "
            "him, the grains catching the low light as they "
            "fall to the worked earth — his stride easy, his "
            "round face content, the seed bag riding his hip "
            "— a man doing his whole share of a miracle in "
            "one unhurried motion. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b04", "out": "s04-a-man-walks-out-and.jpeg", "seg": "n2",
        "window": "18.99-23.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER", "FIELD"],
        "narration": (
            "A man walks out and scatters seed across his field. That is his "
            "job."
        ),
        "must_show": "the job's whole size — close on the farmer's hand releasing seed, the grains leaving his fingers; everything he can do, done.",
        "must_not_show": "no halo, glare or rim-light; the release itself — fingers open, grain going, job complete in the letting go.",
        "scene": (
            "Close in the morning light: the farmer's thick "
            "weathered hand at the top of its swing, fingers "
            "just opened, a spray of barley grains leaving "
            "them mid-air — each seed distinct against the "
            "soft-focus field beyond, the hand already "
            "empty, the job already over the instant it "
            "looks most like work. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b05", "out": "s05-he-does-it-well-he.jpeg", "seg": "n2",
        "window": "23.66-30.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER", "FIELD", "HOUSE"],
        "narration": (
            "He does it well, he does it by hand, and then, and this is the "
            "part that matters, he goes home."
        ),
        "must_show": "SCRIPTURE-EXACT in spirit: the going home — the farmer walking off his sown field toward the house at dusk, seed bag empty and folded under his arm, done.",
        "must_not_show": "no halo, glare or rim-light; the walk AWAY from the work — no backward glance, no lingering; the day's most theological act.",
        "scene": (
            "In the warm dusk the farmer walks up off his "
            "sown field toward the house's lit doorway, the "
            "emptied seed bag folded flat under one arm, his "
            "boots leaving the field's soft dark for the "
            "path's hard pale — and he does not look back at "
            "the slope he has just entrusted to the ground, "
            "not once, the fig tree and the bench and supper "
            "ahead of him and the miracle behind him, filed. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r046-b06", "out": "s06-and-then-he-lives-his.jpeg", "seg": "n3",
        "window": "39.58-41.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER", "HOUSE"],
        "narration": "And then he lives his life.",
        "must_show": "ordinary life resumed — the farmer at his bench against the south wall mending a sandal strap in the evening light; the parable's most radical act: normalcy.",
        "must_not_show": "no halo, glare or rim-light; complete unconcern — a man whose field does not appear once in his evening.",
        "scene": (
            "On the bench against the house's warm south "
            "wall the farmer sits mending a sandal strap in "
            "the last of the light, awl and cord working "
            "slow, a cup of something at his elbow and the "
            "fig tree's shade across his knees — the sown "
            "field lying out of frame and plainly out of "
            "mind, an evening spent entirely on a strap, by "
            "a man whose biggest project is out of his "
            "hands. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r046-b07", "out": "s07-and-should-sleep-and-rise.jpeg", "seg": "jv27",
        "window": "31.00-38.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER", "HOUSE", "FIELD"],
        "narration": (
            "And should sleep, and rise night and day, and the seed should "
            "spring and grow up, he knoweth not how."
        ),
        "must_show": "SCRIPTURE-EXACT: the sleeping and the field in one frame — night: the farmer asleep past his low window, and beyond the glass the moonlit sown field lying dark and working.",
        "must_not_show": "no halo, glare or rim-light; deep peaceful night — the sleeper and the field both at their proper work.",
        "scene": (
            "Deep night: through the house's low bedroom "
            "window the farmer lies soundly asleep under his "
            "blanket, one arm flung easy over the edge of "
            "the bed — and beyond the window's frame the "
            "sown field lies out under the moon, dark, "
            "silent, and secretly employed — two kinds of "
            "faithful work proceeding in one frame, and only "
            "one of them conscious. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b08", "out": "s08-he-sleeps-at-night-and.jpeg", "seg": "n3",
        "window": "41.20-46.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER", "HOUSE"],
        "narration": (
            "He sleeps at night and gets up in the morning. Ordinary weeks go "
            "by."
        ),
        "must_show": "the rhythm — morning: the farmer stretching in his doorway with the sun coming up, an ordinary day beginning like the last and the next.",
        "must_not_show": "no halo, glare or rim-light; routine as blessing — a stretch, a yawn, a day; nothing checked, nothing worried.",
        "scene": (
            "In the fresh gold of sunrise the farmer stands "
            "in his open doorway mid-stretch — arms up, back "
            "arching, face screwed into a mighty yawn — the "
            "morning arriving over the hills exactly as it "
            "did yesterday and will tomorrow, a water jar "
            "waiting by the step, a bird on the fig tree, "
            "ordinary time doing its deep quiet work on a "
            "man who lets it. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r046-b09", "out": "s09-and-the-whole-time-down.jpeg", "seg": "n3",
        "window": "46.09-55.25", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "And the whole time, down in the dark soil where he cannot see and "
            "cannot help, the seed is doing the one thing he could never make "
            "it do."
        ),
        "must_show": "the underground work — a cross-soil close-up: one barley seed in the dark earth, its case split, the first pale root gone down and the first pale shoot bent upward.",
        "must_not_show": "no halo, glare or rim-light; NO light source in the soil — dark earth, pale seed, the work visible by its own contrast.",
        "scene": (
            "In the dark of the soil, seen close as through "
            "a cut bank: one barley seed lies swollen and "
            "split in the black crumb, its first pale root "
            "already threaded down between the grains of "
            "earth and a bent white shoot elbowing upward "
            "toward a surface it has never seen — the whole "
            "secret machinery running in full dark, on "
            "nobody's instructions, witnessed by no one. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r046-b10", "out": "s10-it-is-growing.jpeg", "seg": "n3",
        "window": "55.25-56.86", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": "It is growing.",
        "must_show": "the first surfacing — at soil level in dawn light: the first green shoot tips just breaking the field's crust, dew on them.",
        "must_not_show": "no halo, glare or rim-light; the smallest possible triumph — a few green tips and a level horizon.",
        "scene": (
            "At soil level in the first grey-gold of dawn, "
            "upright and level with the earth at the bottom "
            "of the frame: the field's crust has broken in a "
            "dozen tiny places, and the first green shoot "
            "tips stand a finger's width into the air with "
            "the dew heavy on them — the underground work "
            "surfacing at last, quietly, before anyone in "
            "the house is awake to see it. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b11", "out": "s11-notice-what-he-is-not.jpeg", "seg": "n4",
        "window": "57.41-62.82", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD", "HOUSE"],
        "narration": (
            "Notice what he is not doing. He is not out there at midnight "
            "pulling on the shoots to stretch them longer."
        ),
        "must_show": "the absurdity absent — the moonlit field EMPTY of any farmer, shoots standing small and unmolested; the house dark and asleep behind.",
        "must_not_show": "no halo, glare or rim-light; the emptiness is the joke and the point — nobody out there, thank God.",
        "scene": (
            "The field at midnight under a high moon: the "
            "young shoots stand in their small silver rows, "
            "utterly unattended — no lantern moving among "
            "them, no crouched figure tugging at the green, "
            "no interference of any kind from the dark and "
            "sleeping house beyond the hedge — a field being "
            "loved correctly, which tonight means being left "
            "magnificently alone. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b12", "out": "s12-he-is-not-standing-over.jpeg", "seg": "n4",
        "window": "62.82-67.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER", "FIELD"],
        "narration": (
            "He is not standing over the dirt, worried it forgot how. He "
            "planted."
        ),
        "must_show": "trust's posture — the farmer passing his field on the path with a wave of one hand at it, mid-errand, not even slowing down.",
        "must_not_show": "no halo, glare or rim-light; the wave almost comic — a greeting, not an inspection.",
        "scene": (
            "On the upper path in bright mid-morning the "
            "farmer passes his own greening field mid-errand "
            "— a coil of rope over one shoulder, bound "
            "somewhere else entirely — and gives the young "
            "rows a single easy wave of his free hand as he "
            "goes, the way a man greets a neighbour whose "
            "business is going fine without him. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b13", "out": "s13-now-he-trusts-the-growing.jpeg", "seg": "n4",
        "window": "67.97-71.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER", "FIELD"],
        "narration": "Now he trusts. The growing was never his job.",
        "must_show": "rest at the field's edge — the farmer seated on the flat sitting-stone at the corner, hands loose, watching his green rows with plain unanxious pleasure.",
        "must_not_show": "no halo, glare or rim-light; watching as enjoyment, never surveillance — hands conspicuously idle.",
        "scene": (
            "On the flat sitting-stone at the field's corner "
            "the farmer sits in the late afternoon with his "
            "hands hanging loose between his knees, watching "
            "the wind move through his young green rows — "
            "not counting them, not measuring them, just "
            "watching the way men watch water — a spectator "
            "at his own field, enjoying work he is not "
            "doing. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r046-b14", "out": "s14-and-the-gentlest-words-in.jpeg", "seg": "n5",
        "window": "72.27-78.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER"],
        "narration": (
            "And the gentlest words in the whole story are about that. He does "
            "not even grasp the miracle he is leaning on."
        ),
        "must_show": "unknowing at peace — close on the farmer's face turning a sprouted seedling gently in his fingers, wonder without comprehension, and no distress about the gap.",
        "must_not_show": "no halo, glare or rim-light; the shrug of happy ignorance — mystery held comfortably in a working hand.",
        "scene": (
            "Close in the soft light: the farmer holds a "
            "single uprooted seedling gently between his "
            "thick fingers, turning it — the pale root, the "
            "green blade, the spent seed case still clinging "
            "— his round face bent over it in frank friendly "
            "incomprehension, eyebrows up, mouth pursed in a "
            "silent 'well, there it is' — a man examining a "
            "miracle he runs his whole livelihood on and "
            "cannot explain one inch of. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b15", "out": "s15-he-does-not-have-to.jpeg", "seg": "n5",
        "window": "78.69-83.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER", "FIELD"],
        "narration": "He does not have to. It works whether he understands it or not.",
        "must_show": "the working proof — the field visibly further on: ankle-high green over the whole slope, the farmer replanting his seedling at its edge with a pat.",
        "must_not_show": "no halo, glare or rim-light; the little pat of the replant — comedy and reverence in one gesture.",
        "scene": (
            "The whole slope stands ankle-high in young green "
            "now, moving in the light wind — and at its "
            "near edge the farmer kneels to press his "
            "examined seedling back into the earth where he "
            "took it from, firming the soil around it with "
            "two pats of his palm and a small apologetic "
            "nod, returning the miracle to its work "
            "undamaged by his curiosity. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b16", "out": "s16-for-the-earth-bringeth-forth.jpeg", "seg": "jv28",
        "window": "83.74-92.29", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": (
            "For the earth bringeth forth fruit of herself; first the blade, "
            "then the ear, after that the full corn in the ear."
        ),
        "must_show": "SCRIPTURE-EXACT: the three stages in one frame — the field's slope carrying its own history: near rows in tender blade, the middle in green ear, the far crown turning gold; time as geography.",
        "must_not_show": "no halo, glare or rim-light; one continuous field (never panels) — the gradient of growth reading up the slope.",
        "scene": (
            "Up the field's long slope the season lies "
            "written in one sweep: the near rows tender and "
            "blade-green at the hedge, the middle ground "
            "thickened into soft green ears that hold the "
            "light, and the far crown of the field already "
            "turning its first pale gold against the hills — "
            "first the blade, then the ear, then the "
            "fullness, laid out in order on one hillside "
            "like a sentence diagrammed in barley. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b17", "out": "s17-and-it-comes-in-its.jpeg", "seg": "n6",
        "window": "93.84-97.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": "And it comes in its own order, on its own clock.",
        "must_show": "the clock nobody set — close on one barley head half-formed: green scales building in perfect spiral order, unfinished and unhurried.",
        "must_not_show": "no halo, glare or rim-light; the head HALF-done — order visible mid-assembly; patience in macro.",
        "scene": (
            "Very close in soft daylight: a single barley "
            "head caught halfway through its own building — "
            "the lower scales full and green in their "
            "perfect spiral, the upper rows still tight and "
            "unformed, one thin awn lifting away like a "
            "clock hand — architecture assembling itself in "
            "the open air at precisely the speed it intends "
            "to, and no other. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b18", "out": "s18-the-first-tender-shoots-then.jpeg", "seg": "n6",
        "window": "97.02-100.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": "The first tender shoots. Then the heads of grain.",
        "must_show": "the stages honoured — a close pairing in one scene: a tender young blade and, beside it deeper in the frame, a formed green ear; the sequence in one glance.",
        "must_not_show": "no halo, glare or rim-light; one continuous close scene, both stages genuinely present.",
        "scene": (
            "Close among the rows where the field's ages "
            "meet: in the near focus a tender young blade "
            "still soft enough to bend under a dewdrop, and "
            "a hand's depth beyond it a fully formed green "
            "ear standing armoured in its neat scales — "
            "youth and readiness sharing one square foot of "
            "field, one ahead of the other on the same "
            "unhurried road. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r046-b19", "out": "s19-then-the-whole-field-heavy.jpeg", "seg": "n6",
        "window": "100.49-107.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD", "HOUSE"],
        "narration": (
            "Then the whole field heavy and golden and ready, all in its time, "
            "none of it rushed, none of it forced."
        ),
        "must_show": "the fullness — the entire field deep gold and heavy-headed under a ripe evening sky, bowing in one slow wind; the house small and warm at its edge.",
        "must_not_show": "no halo, glare or rim-light; harvest-eve gold is correct — the season's own colour at the season's own hour.",
        "scene": (
            "The whole field stands deep gold in the ripe "
            "evening light, every head full and bowed, the "
            "one slow wind moving through it in long "
            "breathing waves from hedge to crown — and at "
            "its edge the small stone house sits with its "
            "doorway warm and its fig tree black against "
            "the sky, the two of them, field and house, "
            "arrived together at the exact hour neither of "
            "them hurried. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r046-b20", "out": "s20-you-cannot-hurry-a-field.jpeg", "seg": "n7",
        "window": "108.42-112.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": (
            "You cannot hurry a field. You cannot argue a seed into sprouting "
            "faster."
        ),
        "must_show": "the unbudgeable clock — a quiet still: one unsprouted seed lying on the soil beside a fully golden head fallen from above; the whole timetable in two objects.",
        "must_not_show": "no halo, glare or rim-light; two stages side by side without tension — the field's terms, accepted.",
        "scene": (
            "A quiet close still on the field's warm earth: "
            "a single unsprouted barley corn lying on the "
            "soil's crumb, smooth and shut and biding — and "
            "fallen beside it from the ripe canopy above, a "
            "full golden head heavy with forty of its "
            "grandchildren — the beginning and the end of "
            "the whole patient argument lying an inch apart, "
            "neither one negotiable. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b21", "out": "s21-everything-good-that-has-ever.jpeg", "seg": "n7",
        "window": "112.83-120.17", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Everything good that has ever grown in your life grew like this, "
            "quietly, underground, on a timetable you did not set."
        ),
        "must_show": "the parable universalized — a human vignette: two old friends at a gate whose friendship visibly took years; long-grown good, harvested in a greeting.",
        "must_not_show": "no halo, glare or rim-light; the growth INVISIBLE and its fruit plain — decades in a handshake.",
        "scene": (
            "At a village gate in warm evening light two "
            "old men meet — the handclasp turning into a "
            "forearm grip, the grip into a half-embrace, "
            "both grey heads laughing at something needing "
            "no words — a friendship whose roots went down "
            "through forty unrecorded years of small "
            "seasons, bearing in one greeting the kind of "
            "fruit nothing fast has ever grown. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b22", "out": "s22-so-if-you-planted-something.jpeg", "seg": "n8",
        "window": "120.66-125.77", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "So if you planted something good and you still cannot see it, this "
            "is the story for you."
        ),
        "must_show": "the discouraged planter — a young woman at a windowsill herb pot that shows only bare soil, her chin on her hand; the row's one ache, gently held.",
        "must_not_show": "no halo, glare or rim-light; tender discouragement — the pot bare, the watering cup faithful beside it.",
        "scene": (
            "At a small window in soft grey light a young "
            "woman rests her chin on her folded arms beside "
            "a clay herb pot that shows nothing but bare "
            "watered soil — her small watering cup standing "
            "faithful beside it, the seed packet's empty "
            "twist of cloth still on the sill — a planter "
            "in the hard middle weeks, looking at dirt that "
            "is keeping its promise where she cannot see. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r046-b23", "out": "s23-hidden-is-not-the-same.jpeg", "seg": "n8",
        "window": "125.77-130.27", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Hidden is not the same as dead. Slow is not the same as stopped.",
        "must_show": "the truth beneath her sill — the same herb pot in cross-soil view: below the bare surface, the seed split and rooting, well on its way.",
        "must_not_show": "no halo, glare or rim-light; the pot's secret shown to the viewer alone — dramatic irony as comfort.",
        "scene": (
            "The same clay pot seen as through its own cut "
            "side: above, the bare soil surface she watches "
            "— and below it, hidden in the dark crumb, the "
            "herb seed already split wide, its root a "
            "finger-joint deep and branching, its pale "
            "shoot two days from daylight — the whole "
            "answer to the window's ache proceeding "
            "steadily one inch beneath it. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b24", "out": "s24-under-the-surface-where-you.jpeg", "seg": "n8",
        "window": "130.27-135.38", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Under the surface, where you cannot watch it, it is already on its "
            "way up."
        ),
        "must_show": "the way up — the herb pot days later: the first green crook of the seedling just breaking the soil into the window light.",
        "must_not_show": "no halo, glare or rim-light; the surfacing small and certain — dawn light on one green crook.",
        "scene": (
            "Morning light through the small window: in the "
            "clay pot the soil's surface has broken at "
            "last, and the seedling's first green crook "
            "stands bent above it like a tiny drawn bow, "
            "soil crumbs still balanced on its rising back "
            "— arrival, at the exact appointed hour of a "
            "timetable nobody at the window ever saw. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b25", "out": "s25-but-when-the-fruit-is.jpeg", "seg": "jv29",
        "window": "135.88-142.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER", "FIELD"],
        "narration": (
            "But when the fruit is brought forth, immediately he putteth in the "
            "sickle, because the harvest is come."
        ),
        "must_show": "SCRIPTURE-EXACT: the sickle in — the farmer sweeping the first cut through the gold in morning light, the harvest begun with joy and energy.",
        "must_not_show": "no halo, glare or rim-light; the sickle a HARVEST tool in glad hands — energy, gold, gathering.",
        "scene": (
            "In the clean gold of harvest morning the farmer "
            "makes the first long sweep of his sickle "
            "through the standing barley — the cut swath "
            "falling neat across his free arm, chaff "
            "sparking up into the light, his round face "
            "split with the particular grin of a man "
            "cashing a promise — the whole heavy field "
            "waiting its turn behind the blade's happy "
            "arc. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r046-b26", "out": "s26-you-do-your-small-faithful.jpeg", "seg": "n10",
        "window": "162.89-165.20", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "You do your small, faithful part.",
        "must_show": "the part's true size — a close still: one hand placing one seed into one small hole; the entire human share of the kingdom's economy.",
        "must_not_show": "no halo, glare or rim-light; deliberately tiny — one seed, one hole, one hand.",
        "scene": (
            "A close still in soft light: a single hand "
            "places a single seed into a single thumb-deep "
            "hole in dark worked earth — no field in frame, "
            "no harvest, no scale at all — the complete "
            "human half of the whole arrangement, performed "
            "in an area smaller than a footprint, finished "
            "in a second, and sufficient. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b27", "out": "s27-and-then-one-morning-it.jpeg", "seg": "n9",
        "window": "143.74-152.65", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARMER", "FIELD", "HOUSE"],
        "narration": (
            "And then one morning it is ready, and the waiting is over, and "
            "there is nothing left to do but go out with joy and bring it in. "
            "The harvest comes."
        ),
        "must_show": "the joy general — the harvest in full swing: the farmer and neighbours binding sheaves, children carrying gleanings, the wagon filling by the hedge; gladness at field scale.",
        "must_not_show": "no halo, glare or rim-light; community joy — the harvest as festival; the long waiting visibly repaid.",
        "scene": (
            "The field rings with harvest, the camera down the "
            "slope taking the rows from the side so every swing "
            "and binding crosses in profile: the farmer and "
            "two neighbours swinging and binding down the "
            "rows, sheaves standing stooked behind them, a "
            "boy staggering happily under gleanings bigger "
            "than himself, the wagon by the hedge filling "
            "gold above its rails — and the farmer "
            "straightening mid-row to laugh at something "
            "across the field, the whole slope's long quiet "
            "year cashing out in one loud bright morning. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r046-b28", "out": "s28-that-was-never-the-part.jpeg", "seg": "n9 + n10",
        "window": "152.65-158.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER"],
        "narration": (
            "That was never the part in doubt. Here is the rest he is holding "
            "out to you."
        ),
        "must_show": "certainty's face — the farmer leaning on his sickle amid the stooks, wiping his brow, his expression that of a man whose harvest never once surprised him.",
        "must_not_show": "no halo, glare or rim-light; satisfaction WITHOUT relief — he never doubted; that absence is the beat.",
        "scene": (
            "Amid the standing stooks the farmer leans on "
            "his sickle's handle and wipes his brow with "
            "the back of one wrist — and his round face "
            "holds satisfaction with no relief in it "
            "anywhere: no 'thank goodness', no unclenching, "
            "just the easy pleasure of a man collecting on "
            "an arrangement he trusted the whole way "
            "through — rest, wearing harvest dust. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b29", "out": "s29-the-kingdom-of-god-is.jpeg", "seg": "n10",
        "window": "158.00-162.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": (
            "The kingdom of God is not a thing you have to force into the world "
            "by sheer effort."
        ),
        "must_show": "force's absence — the harvested field at evening peace: neat stubble rows, stooks standing quiet, nothing strained anywhere in the frame.",
        "must_not_show": "no halo, glare or rim-light; the field's calm as the doctrine — order that effort did not force.",
        "scene": (
            "The harvested field lies at peace in the warm "
            "evening: clean stubble rows running their "
            "quiet parallels down the slope, the sheaves "
            "stooked in their unhurried ranks, one late "
            "bird crossing to the hedge — a whole year's "
            "abundance standing in an order no one "
            "strained for, made almost entirely of things "
            "nobody watched happen. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b30", "out": "s30-you-plant-and-god-does.jpeg", "seg": "n10",
        "window": "165.20-170.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER"],
        "narration": (
            "You plant. And God does the part you were never strong enough to "
            "do anyway."
        ),
        "must_show": "the division of labour — the farmer's open palm holding seed toward the camera, and beyond it the whole golden field soft in the background: his part, and the other part.",
        "must_not_show": "no halo, glare or rim-light; the seed sharp, the harvest soft — one hand's worth against a field's worth.",
        "scene": (
            "Close in the gold light: the farmer's open "
            "palm held toward the camera with a small "
            "measure of seed in it — a spoonful, sharp in "
            "focus — and beyond the hand, filling the whole "
            "soft background, the harvested field's gold "
            "and its stooks and its plenty: the entire "
            "visible difference between what a man can "
            "hold and what he gets back. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b31", "out": "s31-he-makes-it-grow-so.jpeg", "seg": "n10 + n11",
        "window": "170.05-173.84", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER", "HOUSE"],
        "narration": "He makes it grow. So you can actually sleep tonight.",
        "must_show": "the applied gospel — night again: the farmer asleep in deep peace past the low window, the harvest stooks standing outside under the moon; rest earned by trust, not effort.",
        "must_not_show": "no halo, glare or rim-light; the mirror of the earlier sleeping beat — the same peace, now vindicated.",
        "scene": (
            "Night at the little house once more: through "
            "the low window the farmer sleeps his same deep "
            "unbothered sleep, blanket rising slow — and "
            "beyond the glass the moon stands over a field "
            "of finished stooks instead of buried seed, the "
            "whole silver slope keeping quiet watch over "
            "the one man in the story who understood from "
            "the start whose job the growing was. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r046-b32", "out": "s32-the-seed-is-not-waiting.jpeg", "seg": "n11",
        "window": "173.84-180.49", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The seed is not waiting on your worry. It is doing, down in the "
            "dark, exactly what he promised it would."
        ),
        "must_show": "the closing image — the cross-soil view one last time: a seed at work in the dark earth, root down, shoot rising, moonlit surface far above; the promise, in progress, tonight.",
        "must_not_show": "no halo, glare or rim-light; no light in the soil — only the thin silver line of the moonlit surface at the frame's top; the dark full of kept promises.",
        "scene": (
            "The dark of the soil a final time, close and "
            "quiet: a seed split and working in the black "
            "crumb — root gone deep, pale shoot climbing — "
            "and far above it at the frame's top edge, the "
            "thin silver line of the moonlit surface like a "
            "distant shore — the night's whole worry-proof "
            "economy running silently in the dark, keeping "
            "a promise no one is awake to watch. Every "
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
    "FIELD": "PLACE-REF/field.jpeg",  # build-28-hidden-treasure v2-r028-b02
    "HOUSE": "PLACE-REF/house.jpeg",  # build-46-seed-growing s02-it-is-about-a-farmer (manual)
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "FARMER": "CAST-REF-V2/farmer.jpeg",
}
