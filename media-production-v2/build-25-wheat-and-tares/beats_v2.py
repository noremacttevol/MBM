#!/usr/bin/env python3
"""V2 beat map — row 25, build-25-wheat-and-tares (Matthew 13:24-30, 36-43).

COVERAGE: 28 pictures over 161.0 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 13:24-30, 36-43 KJV):
  v24   "Another parable put he forth unto them" — same seaside teaching day
        as the sower (Matthew 13:1-2): Jesus in the boat, crowd on the shore.
        Row 24 already staged that occasion from the hillside and waterline,
        so THIS build stages it from INSIDE the boat looking past Jesus to
        the crowd — same occasion, different picture (library no-repeat).
  v25   "while men SLEPT, his ENEMY came and sowed tares among the wheat,
        and went his way" — full NIGHT, moonlight, one furtive figure.
  v26   "when the blade was sprung up, and brought forth fruit, THEN
        appeared the tares also" — the tares (darnel) are indistinguishable
        from young wheat until the heads form.
  v27-28 the servants come asking; "An enemy hath done this."
  v29   "NAY; lest while ye gather up the tares, ye ROOT UP ALSO THE WHEAT
        with them" — ⚑ Flag J (CONTENT-CARE §3 row 25): the mercy is that
        judgment is DELAYED to protect the wheat. The refusal beat and the
        waiting beats are the heart of the row.
  v30   "Let both grow together until the harvest ... Gather ye together
        first the tares, and bind them in bundles to burn them: but gather
        the wheat into my barn." — the BURN is handled RESTRAINED: bound
        bundles and a thin distant smoke, never a fire spectacle, never
        anything or anyone in flames close-up. The wheat coming safely home
        is the frame that dominates.
  v36   "Jesus sent the multitude away, and went INTO THE HOUSE: and his
        disciples came unto him" — the explanation beat is indoors, with
        the disciples, by afternoon window light.
  v43   "Then shall the RIGHTEOUS SHINE FORTH AS THE SUN" — painted as
        harvest workers in brilliant clean sunrise light, faces lit by the
        actual risen sun. NEVER as light coming from people, never halos.

TIME OF DAY: frame beat b01 is bright morning at the sea. The parable runs:
day sowing → FULL NIGHT for the enemy (v25 requires it — moonlight, correct,
not a defect) → bright green growing-season days → warm gold harvest →
evening barn light. The house-explanation beat (b24) is warm afternoon
window light. The shine-as-the-sun beats (b26-b28 imagery) use a clean
brilliant SUNRISE — scripture-driven, not the row-11 defect.

CHANGING CONDITION (kept OUT of the locks): the field's season — bare turned
earth, young green blades, headed summer growth, ripe harvest, cut stubble —
moves beat by beat and is never locked.

The tares are darnel: in the young beats identical to wheat; at maturity
their heads are thin, stiff and upright with small dark seeds, standing
straight while true wheat bows heavy and gold.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "FARMER": (
        "FARMER LOCK: the field's owner is the same man in every shot — late "
        "fifties, tall and lean, with a silver-streaked black beard kept "
        "short, calm deep-set dark eyes and an unhurried, deliberate bearing. "
        "He wears a DEEP CHARCOAL-GREY wool tunic under a DARK WALNUT-BROWN "
        "mantle with a plain leather belt (never cream, never white). His "
        "face is shown clearly and its resting state is patience."
    ),
    "ENEMY": (
        "ENEMY LOCK: the enemy is the same man in every shot — gaunt, about "
        "forty-five, with a thin dark beard, sharp watchful eyes and a "
        "tight-drawn mouth. He wears a DARK CHARCOAL-BLACK wool cloak over a "
        "NEAR-BLACK DEEP-INDIGO tunic, and carries a small rough sack (never "
        "cream, never white). His face is visible in the moonlight — a man, "
        "not a shadow or a faceless shape."
    ),
    "WORKERS": (
        "FARM WORKERS LOCK: the farm servants are ordinary working men of "
        "mixed ages with dark hair and dark beards, in SATURATED DEEP earth "
        "colours — dark chocolate brown, deep russet, dark olive and burnt "
        "ochre wool tunics with rope belts and worn sandals (never cream, "
        "never white; only Jesus wears cream). Their faces are shown clearly."
    ),
    "WHEATFIELD": (
        "WHEAT FIELD LOCK: one broad gently sloping field bounded by a low "
        "dry-stone wall, a single old olive tree standing at its near "
        "corner, a cart track along one side, and low blue hills on the far "
        "horizon. The same wall, tree and hills appear in every field beat."
    ),
    "FARMYARD": (
        "FARMYARD LOCK: the farm's working yard — a stout stone barn with a "
        "wide plank door standing open, a beaten-earth threshing floor "
        "before it, wooden pitchforks and rakes against the wall, and a low "
        "stone trough by the gate."
    ),
    "BOAT-SHORE": (
        "BOAT AND SHORE LOCK: the view from inside a small weathered wooden "
        "fishing boat floating a few boat-lengths off a curved pebble "
        "beach on the Sea of Galilee — worn planks and a single mast, clear "
        "green-blue water between boat and land, and the beach and grassy "
        "hillside beyond crowded with listeners. Bright morning light."
    ),
    "HOUSE": (
        "HOUSE LOCK: the main room of a Capernaum house — thick "
        "honey-stone walls, one deep-set window throwing a broad slant of "
        "warm afternoon light across a beaten-earth floor, rush mats and "
        "low cushions, a water jar by the door and a shelf of clay vessels "
        "in shadow."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------------ b01 — the boat, again ----
    {
        "id": "v2-r025-b01", "out": "s01-another-parable-put-he-forth.jpeg", "seg": "s24 + j24",
        "window": "0.28-7.88", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BOAT-SHORE"],
        "narration": (
            "Another parable put he forth unto them, saying, The kingdom of "
            "heaven is likened unto a man which sowed good seed in his field:"
        ),
        "must_show": "SCRIPTURE-EXACT: from INSIDE the boat, past Jesus's shoulder, the whole crowded shore he is teaching — a fresh composition of the Matthew 13 boat scene, not row 24's angles.",
        "must_not_show": "no halo, glare or rim-light on Jesus; he is seated; nobody stands on the water.",
        "scene": (
            "From inside the small fishing boat, low over its worn planks, "
            "looking past Jesus — seated in the bow, seen from behind at "
            "three-quarter, one hand lifted mid-word — across the strip of "
            "bright green-blue water to the curved beach packed with "
            "listening people and the grassy hillside rising crowded behind "
            "them. The morning sun lays moving light between boat and land. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b02", "out": "s02-now-anyone-could-see-the.jpeg", "seg": "n5",
        "window": "50.34-53.35", "wide": True, "jesus": False, "ref": False,
        "locks": ["WHEATFIELD"],
        "narration": "Now anyone could see the field was full of both.",
        "must_show": "the headed summer field where the difference now reads plainly — bowed golden wheat interrupted everywhere by stiff upright dark-seeded tare heads.",
        "must_not_show": "no halo, glare or rim-light; the two plants must be tellable at a glance — bowing gold against stiff dark-headed stalks.",
        "scene": (
            "The broad field in high summer light, seen from the cart track: "
            "a full stand of grain where the difference has finally "
            "declared itself — heavy golden wheat heads bowing everywhere, "
            "and threaded thickly through them, standing stiff and dead "
            "straight, the thin dark-seeded heads of the tares, spiky and "
            "upright against the bowed gold. The old olive tree and the "
            "stone wall hold the corner of the frame. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b03", "out": "s03-the-kingdom-of-heaven-he.jpeg", "seg": "n1",
        "window": "9.00-16.46", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARMER", "WHEATFIELD"],
        "narration": (
            "The kingdom of heaven, he said, is like a farmer who sowed good "
            "seed all across his field."
        ),
        "must_show": "the farmer broadcast-sowing his field in clean daylight — the wide arc of seed leaving his hand, the whole bare turned field around him.",
        "must_not_show": "no halo, glare or rim-light; hand-sowing from a bag — no equipment.",
        "scene": (
            "Bright clear morning over the freshly turned field: the tall "
            "lean farmer walks the dark earth mid-fling, a wide fan of pale "
            "seed leaving his open hand and hanging in the air, a canvas "
            "seed-bag at his hip. The low dry-stone wall runs along the "
            "slope behind him and the single old olive tree stands at the "
            "corner, the far hills pale blue. The camera stands side-on to "
            "the throw. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b04", "out": "s04-it-was-clean-good-wheat.jpeg", "seg": "n2",
        "window": "17.07-21.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER"],
        "narration": (
            "It was clean, good wheat seed. He wanted a good harvest, and he "
            "did everything right."
        ),
        "must_show": "a close shot of the farmer's cupped hands full of clean, plump, uniform wheat seed — quality you can see; his calm face soft-focus above.",
        "must_not_show": "no halo, glare or rim-light; the seed is visibly clean and uniform — no dark or odd grains mixed in.",
        "scene": (
            "A close shot of the farmer's two cupped hands held into the "
            "morning light, brimming with clean plump wheat seed of one "
            "even pale gold, not a dark grain among them — and above the "
            "hands, softly out of focus, his lean patient face looking down "
            "at what he is about to give the ground. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b05", "out": "s05-but-while-men-slept-his.jpeg", "seg": "j25",
        "window": "22.31-26.58", "wide": True, "jesus": False, "ref": False,
        "locks": ["ENEMY", "WHEATFIELD"],
        "narration": (
            "But while men slept, his enemy came and sowed tares among the "
            "wheat, and went his way."
        ),
        "must_show": "SCRIPTURE-EXACT: full night, moonlight — the enemy alone in the middle of the sown field, flinging seed from his sack, hunched and hurried.",
        "must_not_show": "no halo, glare or rim-light; night lighting is CORRECT here (v25 'while men slept') — moon and deep blue darkness, never dusk colouring; his face visible, not a faceless shape.",
        "scene": (
            "Deep night under a high half-moon, the field a sea of "
            "silver-blue shadow: alone in the middle of the sown earth the "
            "gaunt man in the charcoal-black cloak moves at a hurried "
            "crouch, his arm mid-swing scattering seed from the rough sack "
            "clutched against his chest, his sharp face caught pale in the "
            "moonlight, glancing back over his shoulder toward the dark "
            "farm buildings as he sows. The stone wall lies as a black line "
            "behind him. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b06", "out": "s06-but-that-night-while-everyone.jpeg", "seg": "n3",
        "window": "27.65-34.54", "wide": True, "jesus": False, "ref": False,
        "locks": ["ENEMY", "WHEATFIELD"],
        "narration": (
            "But that night, while everyone was asleep, an enemy of his crept "
            "into the field and scattered weed seeds all through the wheat."
        ),
        "must_show": "the burst continues — the enemy climbing OVER the low stone wall into the field, one leg across, sack in hand, the sleeping farm dark in the distance.",
        "must_not_show": "no halo, glare or rim-light; still full night; the trespass itself — the wall being crossed — is the visible action.",
        "scene": (
            "In the deep moonlit night the gaunt cloaked man is caught "
            "halfway over the low dry-stone wall, one leg swung across, one "
            "hand flat on the capstones and the other gripping his rough "
            "sack, his face turned toward the distant farmhouse where no "
            "lamp burns. The moon-silvered field of young sown earth waits "
            "beyond him. The camera stands inside the field watching the "
            "wall being crossed. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r025-b07", "out": "s07-then-he-slipped-away-and.jpeg", "seg": "n3 + n4",
        "window": "34.54-41.39", "wide": True, "jesus": False, "ref": False,
        "locks": ["ENEMY", "WHEATFIELD"],
        "narration": (
            "Then he slipped away, and no one saw. The weed he chose looks "
            "almost exactly like young wheat."
        ),
        "must_show": "the enemy already small and leaving along the dark cart track, the empty sack loose in his hand — and the field left looking utterly undisturbed behind him.",
        "must_not_show": "no halo, glare or rim-light; the field must show NO visible trace — the crime is invisible; still night.",
        "scene": (
            "The moonlit field lies smooth and utterly undisturbed, dark "
            "seeded earth in even silver-blue rows — and far along the pale "
            "cart track at its edge the cloaked figure is already small and "
            "going, the emptied sack swinging loose from one hand, his "
            "shape passing the last corner of the stone wall into the dark. "
            "Nothing in the field betrays that he was ever in it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b08", "out": "s08-you-cannot-tell-them-apart.jpeg", "seg": "n4",
        "window": "41.39-44.93", "wide": False, "jesus": False, "ref": False,
        "locks": ["WHEATFIELD"],
        "narration": (
            "You cannot tell them apart until they grow up and the heads "
            "appear."
        ),
        "must_show": "a close shot of young green blades — dozens of identical seedlings in morning light, with NO way to tell wheat from tare.",
        "must_not_show": "no halo, glare or rim-light; the seedlings must be genuinely identical — no visual hint marking any as different.",
        "scene": (
            "A close shot low over the field in fresh morning light, upright "
            "and level with the earth at the bottom of the frame: dozens of "
            "slender young green blades standing in loose rows out of the "
            "dark soil, dew still on them — every seedling identical to its "
            "neighbour, leaf for leaf, with nothing anywhere to tell one "
            "kind from the other. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r025-b09", "out": "s09-so-the-wheat-came-up.jpeg", "seg": "n5",
        "window": "45.59-50.34", "wide": True, "jesus": False, "ref": False,
        "locks": ["WHEATFIELD"],
        "narration": (
            "So the wheat came up green and strong, and right in the middle of "
            "it, so did the weeds."
        ),
        "must_show": "the field waist-high and green under a bright sky — vigorous, promising, and (to the eye) still perfectly clean.",
        "must_not_show": "no halo, glare or rim-light; no visible difference yet between the plants — the betrayal is still hidden.",
        "scene": (
            "The broad field now waist-high in strong green growth under a "
            "bright late-spring sky, the whole stand moving together in the "
            "wind like one healthy crop, dense and even from the stone wall "
            "to the cart track — nothing to any eye but a good field coming "
            "on well. The old olive tree stands in full leaf at the corner. "
            "The camera looks across the green from the track. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------ n6-n8 — the servants ----
    {
        "id": "v2-r025-b10", "out": "s10-sir-didst-thou-not-sow.jpeg", "seg": "j27",
        "window": "53.91-58.37", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARMER", "WORKERS", "WHEATFIELD"],
        "narration": (
            "Sir, didst thou not sow good seed in thy field? from whence then "
            "hath it tares?"
        ),
        "must_show": "SCRIPTURE-EXACT: the servants at the field's edge with the farmer — one holding up a pulled tare stalk with its dark stiff head as the evidence, faces troubled.",
        "must_not_show": "no halo, glare or rim-light; the pulled stalk is a TARE (stiff, dark-seeded head) — not bowed golden wheat.",
        "scene": (
            "At the field's edge by the stone wall, in high summer light, "
            "three troubled farm servants stand before the tall farmer — "
            "the foremost holding up at arm's length a single pulled stalk "
            "with a thin stiff dark-seeded head, roots and soil still "
            "hanging from it, his other hand flung out toward the infested "
            "field behind them where the upright dark heads bristle through "
            "the bowing gold. The farmer regards the stalk calmly. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b11", "out": "s11-the-workers-were-upset-they.jpeg", "seg": "n6",
        "window": "59.48-64.22", "wide": False, "jesus": False, "ref": False,
        "locks": ["WORKERS"],
        "narration": (
            "The workers were upset. They came to the farmer and said, did you "
            "not plant good seed?"
        ),
        "must_show": "a close shot of the servants' faces — indignation and hurt on the crop's behalf; men who did the work and can't understand the result.",
        "must_not_show": "no halo, glare or rim-light; upset FOR the field, not mutinous — loyalty in the anger.",
        "scene": (
            "A close shot of the three servants' faces in the bright field "
            "light — the eldest with his jaw working and hurt disbelief in "
            "his eyes, the young one behind him flushed and frowning, the "
            "third staring past the camera at the ruined-looking stand — "
            "the faces of men who ploughed and sowed this ground themselves "
            "and cannot understand what it has come up with. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b12", "out": "s12-where-did-all-these-weeds.jpeg", "seg": "n6 + n7",
        "window": "64.22-69.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARMER", "WORKERS", "WHEATFIELD"],
        "narration": (
            "Where did all these weeds come from? He told them, an enemy has "
            "done this."
        ),
        "must_show": "SCRIPTURE-EXACT: the farmer answering — calm, certain, one hand laid on the shoulder of the nearest servant, the words landing gravely on the group.",
        "must_not_show": "no halo, glare or rim-light; the farmer shows no panic and no rage — he already understands what happened.",
        "scene": (
            "The tall farmer stands among his three servants at the field's "
            "edge, one hand laid steady on the eldest servant's shoulder, "
            "his lean face grave and certain as he gives them the answer; "
            "the men have gone still around him, the pulled tare stalk "
            "hanging forgotten from the foremost's hand. Behind them the "
            "infested field moves in the summer wind. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b13", "out": "s13-and-they-asked-do-you.jpeg", "seg": "n7",
        "window": "69.86-73.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARMER", "WORKERS", "WHEATFIELD"],
        "narration": (
            "And they asked, do you want us to go and pull all the weeds out "
            "right now?"
        ),
        "must_show": "the servants' eager offer — the young one already half-turned toward the field with his sleeves pushed up, hands open, ready to start tearing.",
        "must_not_show": "no halo, glare or rim-light; eagerness to serve, and the danger in it — bodies already leaning toward the field.",
        "scene": (
            "The young servant has already half-turned toward the field with "
            "his sleeves pushed above his elbows and both hands open, one "
            "foot in the crop's first row, looking back at the farmer for "
            "the word; the second servant is stooping toward a stiff dark "
            "tare head beside the wall, fingers spread to grip it. The "
            "farmer watches them both, still and unhurried. Summer light "
            "over everything. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r025-b14", "out": "s14-and-here-is-where-you.jpeg", "seg": "n8",
        "window": "74.59-79.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER"],
        "narration": (
            "And here is where you see what kind of man he is. He did not send "
            "them tearing through the field."
        ),
        "must_show": "a close portrait of the farmer — the patience itself; a slow measuring gaze out over the crop, a man weighing what he loves against what invades it.",
        "must_not_show": "no halo, glare or rim-light; no anger — the row's whole meaning rests in this calm.",
        "scene": (
            "A close portrait of the farmer in warm field light, his "
            "silver-streaked beard and deep-set eyes in three-quarter view, "
            "gazing slowly out over the unseen crop with the measuring calm "
            "of a man weighing what he loves against what has invaded it — "
            "no anger anywhere in the face, only long patience settling "
            "into a decision. The green field lies soft behind him. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b15", "out": "s15-he-said-no-nay-lest.jpeg", "seg": "n8 + j1",
        "window": "79.92-85.90", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARMER", "WORKERS", "WHEATFIELD"],
        "narration": (
            "He said, no. Nay; lest while ye gather up the tares, ye root up "
            "also the wheat with them."
        ),
        "must_show": "SCRIPTURE-EXACT: the refusal — the farmer's raised open hand stopping the eager servants, the young one checked mid-step at the field's edge.",
        "must_not_show": "no halo, glare or rim-light; the raised hand is gentle restraint, not command-and-control — protection, visible.",
        "scene": (
            "The farmer's arm is extended with his open palm raised toward "
            "his servants in a gentle, absolute stop — and the young one "
            "checks mid-step at the crop's first row, one foot still "
            "lifted, while the stooping servant straightens with his "
            "fingers empty. The farmer's face holds nothing but calm "
            "certainty. The threatened green field breathes behind them in "
            "the summer wind. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r025-b16", "out": "s16-let-both-grow-together-until.jpeg", "seg": "j1",
        "window": "85.90-88.65", "wide": True, "jesus": False, "ref": False,
        "locks": ["WHEATFIELD"],
        "narration": "Let both grow together until the harvest.",
        "must_show": "SCRIPTURE-EXACT: the field left in peace — wheat and tares standing together untouched under a wide summer sky, nobody in the frame.",
        "must_not_show": "no halo, glare or rim-light; no figures — the spared field itself is the picture.",
        "scene": (
            "The whole field under a wide high-summer sky, empty of any "
            "person: bowed golden-green wheat and stiff upright tare heads "
            "standing together untouched from the stone wall to the cart "
            "track, moving as one in the wind, the old olive tree in full "
            "leaf at the corner and the low blue hills beyond. A field left "
            "alone on purpose. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r025-b17", "out": "s17-in-other-words-if-you.jpeg", "seg": "n9",
        "window": "89.63-97.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["WHEATFIELD"],
        "narration": (
            "In other words: if you rip the weeds out now, their roots are "
            "tangled around the wheat, and you will tear up the good plants "
            "along with them."
        ),
        "must_show": "the reason made visible — a close shot at the soil line where a tare stem and a wheat stem rise a finger's width apart, their exposed roots interlocked in one knot of earth.",
        "must_not_show": "no halo, glare or rim-light; the roots must be visibly TANGLED TOGETHER — one cannot come out without the other.",
        "scene": (
            "A very close shot at the soil line, upright and level: two "
            "stems rising a finger's width apart — one wheat, one tare — "
            "and below them, where a crumb of the dark earth has fallen "
            "away, their pale roots plainly wound and knotted through each "
            "other in a single inseparable tangle. Warm light rakes low "
            "across the soil. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r025-b18", "out": "s18-he-would-rather-wait-than.jpeg", "seg": "n9 + n10",
        "window": "97.00-102.15", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARMER", "WHEATFIELD"],
        "narration": (
            "He would rather wait than lose a single stalk of wheat. So the "
            "farmer waited."
        ),
        "must_show": "the waiting begun — the farmer standing alone at the wall in evening light, hands at rest on the capstones, watching over the mixed field.",
        "must_not_show": "no halo, glare or rim-light; evening colouring is correct here — a day ending with the decision made; his posture is guardianship, not defeat.",
        "scene": (
            "In soft evening light the farmer stands alone at the low "
            "dry-stone wall, both hands at rest on the capstones, watching "
            "out over his mixed field as the day goes — shoulders easy, "
            "head up, a guard rather than a mourner. The wheat and tares "
            "stand shadowed together in the last warmth, and one early "
            "star shows over the far hills. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r025-b19", "out": "s19-all-season-long-the-wheat.jpeg", "seg": "n10",
        "window": "102.15-109.82", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARMER", "WHEATFIELD"],
        "narration": (
            "All season long the wheat and the weeds grew up side by side, and "
            "he let them, because his patience was protecting the crop he "
            "loved."
        ),
        "must_show": "the long season in one frame — the field turning from green toward gold, and the farmer walking its edge as he has clearly done a hundred times, letting it be.",
        "must_not_show": "no halo, glare or rim-light; the crop is visibly further on than the refusal beats — colour turning, heads filling.",
        "scene": (
            "The field caught mid-turn from green to gold under a warm "
            "late-summer sky, the wheat heads filling and beginning to "
            "bow, the stiff tare heads darkening among them — and along "
            "the cart track at its edge the farmer walks his slow "
            "customary round, hands clasped behind his back, passing the "
            "old olive tree without stopping, letting the field be. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    # -------------------------------------------------- v30 — the harvest ----
    {
        "id": "v2-r025-b20", "out": "s20-gather-ye-together-first-the.jpeg", "seg": "j30",
        "window": "110.46-116.77", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARMER", "WORKERS", "WHEATFIELD"],
        "narration": (
            "Gather ye together first the tares, and bind them in bundles to "
            "burn them: but gather the wheat into my barn."
        ),
        "must_show": "SCRIPTURE-EXACT and ⚑ Flag J RESTRAINED: harvest morning orders — the farmer directing his reapers, tied tare bundles stacked by the wall, sickles ready over the ripe field; NO fire in this frame.",
        "must_not_show": "no halo, glare or rim-light; NO flames, NO burning close-up anywhere in the row — bundles bound and set aside is the whole of it here.",
        "scene": (
            "Warm gold harvest morning over the fully ripe field: the "
            "farmer stands among four reapers with sickles in hand, one arm "
            "sweeping his instructions across the standing grain, while by "
            "the stone wall the first few bundles of stiff dark-headed "
            "tares lie already cut and tightly bound with cord, set apart "
            "by themselves. The bowed golden wheat waits untouched and "
            "fully ripe in the morning light. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b21", "out": "s21-then-harvest-came-and-at.jpeg", "seg": "n11",
        "window": "117.81-121.88", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Then harvest came. And at harvest, the two are finally easy to "
            "tell apart."
        ),
        "must_show": "a close shot of a reaper's two fists holding the two kinds side by side — heavy bowed gold wheat in one hand, stiff thin dark-seeded tares in the other; the difference, finally undeniable.",
        "must_not_show": "no halo, glare or rim-light; the two handfuls must be unmistakably different at a glance.",
        "scene": (
            "A close shot of a reaper's two weathered fists held up side by "
            "side into the warm harvest light: in one, a sheaf-thick "
            "handful of heavy wheat stalks, their full gold heads bowing "
            "over his knuckles; in the other, a handful of thin stiff tare "
            "stalks standing dead straight, their sparse dark seed-heads "
            "spiky and mean beside the gold. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b22", "out": "s22-the-reapers-gathered-the-weeds.jpeg", "seg": "n11",
        "window": "121.88-127.93", "wide": True, "jesus": False, "ref": False,
        "locks": ["WORKERS", "WHEATFIELD", "FARMYARD"],
        "narration": (
            "The reapers gathered the weeds and bundled them away, and then "
            "gathered all the good wheat safely into the barn."
        ),
        "must_show": "⚑ Flag J RESTRAINED: the two motions in one frame — bound tare bundles carried off toward a thin distant smoke at the far field corner, and great gold sheaves carried the OTHER way in through the open barn door; the wheat's homecoming dominates.",
        "must_not_show": "no halo, glare or rim-light; the smoke is thin, DISTANT and incidental — no visible flames, nothing burning close-up; the barn side of the frame carries the warmth and the eye.",
        "scene": (
            "Harvest afternoon: in the near half of the frame two reapers "
            "carry great golden sheaves of wheat in their arms through the "
            "stout barn's wide-open plank door, where stacked sheaves "
            "already rise warm in the interior shadow — while far across "
            "the cut stubble field behind them, small with distance, a "
            "single worker walks away with dark bound bundles on a "
            "shoulder-pole toward the far corner, where one thin grey line "
            "of smoke stands up faint against the hills. The barn and the "
            "gold fill the picture. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r025-b23", "out": "s23-nothing-good-was-lost-everything.jpeg", "seg": "n12",
        "window": "128.55-133.66", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARMER", "FARMYARD"],
        "narration": (
            "Nothing good was lost. Everything the farmer had waited and hoped "
            "for came safely home."
        ),
        "must_show": "inside the barn — the farmer standing in the doorway light before the full stacked harvest, one hand resting on the nearest sheaf; safety, completed.",
        "must_not_show": "no halo, glare or rim-light; the barn is FULL — abundance, not a scraped-in remnant.",
        "scene": (
            "Inside the stone barn, warm evening light falling through the "
            "wide doorway: golden wheat sheaves stacked full and high up "
            "both walls, dust drifting slow in the doorway light, and the "
            "tall farmer standing among them with one hand resting on the "
            "nearest sheaf as a man rests a hand on a child's head — quiet, "
            "finished, everything he waited for safely in. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    # ----------------------------------------------- n13-n14 — the meaning ----
    {
        "id": "v2-r025-b24", "out": "s24-jesus-said-that-is-how.jpeg", "seg": "n13",
        "window": "134.29-136.81", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": "Jesus said that is how God works with the world.",
        "must_show": "SCRIPTURE-EXACT (v36 — into the house): Jesus seated in the warm house interior, the disciples close around him, giving the parable's meaning.",
        "must_not_show": "no halo, glare or rim-light on Jesus; an intimate indoor circle, not a crowd scene.",
        "scene": (
            "The main room of the house in warm afternoon window light: "
            "Jesus sits on a low cushion with his back near the thick "
            "honey-stone wall, and five disciples sit close in around him "
            "on the rush mats, one leaning forward with his elbows on his "
            "knees, another with his chin in his hand — the private "
            "explanation after the crowds. The broad slant of window light "
            "falls across the circle. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r025-b25", "out": "s25-he-is-not-quick-to.jpeg", "seg": "n13",
        "window": "136.81-143.58", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARMER", "WHEATFIELD"],
        "narration": (
            "He is not quick to rip things up. He gives time, because his "
            "patience is mercy. And in the end,"
        ),
        "must_show": "the patience beat reprised as meaning — the farmer's open empty hands held over the growing mixed field, withholding, in warm light.",
        "must_not_show": "no halo, glare or rim-light; the hands do NOT touch or pull anything — mercy shown as restraint.",
        "scene": (
            "In warm late light at the field's edge the farmer stands over "
            "the mixed green-gold stand with both hands held open and "
            "empty above the heads of the grain — near enough to touch, "
            "touching nothing — his patient face looking down the rows he "
            "is choosing, again, to spare. The wind moves the wheat and "
            "tares together under his still hands. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b26", "out": "s26-then-shall-the-righteous-shine.jpeg", "seg": "j2",
        "window": "144.26-150.07", "wide": True, "jesus": False, "ref": False,
        "locks": ["WORKERS", "WHEATFIELD"],
        "narration": (
            "Then shall the righteous shine forth as the sun in the kingdom of "
            "their Father. Who hath ears to hear, let him hear."
        ),
        "must_show": "SCRIPTURE-EXACT, painted through the parable: harvest workers at SUNRISE, the risen sun full on their lifted faces and on the gathered gold around them — lit BY the sun, never radiating light themselves.",
        "must_not_show": "no halo, glare or rim-light; no light emanating from any person — the sun itself is the only source, and it is in the sky, not behind anyone's head.",
        "scene": (
            "Clean brilliant sunrise over the harvested farm: the reapers "
            "stand resting among the last stacked sheaves with their faces "
            "lifted into the full morning sun climbing clear of the far "
            "hills to one side of the frame, every face and every stacked "
            "head of gold grain lit strong and warm by it, long fresh "
            "shadows running from their feet across the clean stubble. The "
            "sun stands well clear of every figure. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b27", "out": "s27-the-people-who-belong-to.jpeg", "seg": "n14",
        "window": "151.16-155.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["WORKERS"],
        "narration": (
            "The people who belong to him will shine like the sun. That is how "
            "good he is."
        ),
        "must_show": "a close shot of one reaper's face full in the sunrise — eyes closed, sun directly on the skin, at peace; sunlight received, not emitted.",
        "must_not_show": "no halo, glare or rim-light; the light source is plainly the off-frame sun — nothing luminous about the person himself.",
        "scene": (
            "A close portrait of one weathered reaper's face turned full "
            "into the risen morning sun from one side, eyes closed, the "
            "warm light strong on his brow and cheek and lighting the "
            "grain-dust on his beard, his expression open and utterly at "
            "peace — a tired man standing in sunlight he did nothing to "
            "earn. Soft gold stubble-field colour behind him. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r025-b28", "out": "s28-he-is-patient-enough-to.jpeg", "seg": "n14",
        "window": "155.46-160.63", "wide": True, "jesus": False, "ref": False,
        "locks": ["FARMER", "WHEATFIELD"],
        "narration": (
            "He is patient enough to wait for you, and he will not let one good "
            "stalk be lost."
        ),
        "must_show": "the closing image — the farmer in the sunrise stubble carrying the last single sheaf home in his arms, held close like something precious, the open barn warm behind him.",
        "must_not_show": "no halo, glare or rim-light; ONE last sheaf, carried personally — not thrown on a cart; tenderness, not labour.",
        "scene": (
            "In the low clean light of sunrise the farmer walks alone "
            "across the cut stubble toward the camera carrying the last "
            "single sheaf of wheat upright in both arms, held close "
            "against his chest the way a man carries something he will "
            "not risk dropping, his patient face bent slightly over it. "
            "Behind him the barn's wide door stands open and warm with "
            "stacked gold, and his long shadow runs home ahead of him "
            "across the field. Every figure has two arms, two hands and "
            "one head."
        ),
    },
]
