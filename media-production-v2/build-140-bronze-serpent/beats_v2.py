#!/usr/bin/env python3
"""V2 beat map — row 140, build-140-bronze-serpent (Numbers 21:4-9 + John 3:14-15).

COVERAGE: 24 pictures over 139.4 s = 5.8 s/picture (matches the library density).

Authored 2026-08-13 as the REPLACEMENT for the archived Naaman build (Cameron
rejected Naaman's "way back / come home" moral as a duplicate of #2 Prodigal
Son). The Bronze Serpent is the wilderness event Jesus HIMSELF chose to explain
his cross (John 3:14). Moral: look in faith to God's provision and live.

SCRIPTURE FACTS (Numbers 21 KJV):
  21:4  journeyed from mount Hor by the way of the Red sea, to compass
        Edom; "the soul of the people was much discouraged because of the way."
  21:5  they "spake against God, and against Moses" — no bread, no water,
        "our soul loatheth this light bread" (the manna).
  21:6  "the LORD sent FIERY SERPENTS among the people, and they bit the
        people; and much people of Israel died."
  21:7  the people confess: "We have sinned... pray unto the LORD, that he
        take away the serpents." "And Moses prayed for the people."
  21:8  the LORD: "Make thee a fiery serpent, and set it upon a POLE... every
        one that is bitten, when he LOOKETH upon it, shall live."
  21:9  "Moses made a serpent of BRASS, and put it upon a pole... when he
        BEHELD the serpent of brass, he lived."
  John 3:14-15  "as Moses lifted up the serpent in the wilderness, even so
        must the Son of man be lifted up: That whosoever believeth in him
        should not perish, but have eternal life."

RENDERING LAWS (CONTENT-CARE, strictly):
  - THE FIERY SERPENTS are REAL desert vipers in a real camp — natural,
    never monstrous, never lunging at the camera, never coiled around a
    person in horror. Show the danger by people recoiling and by a snake
    moving through the ground, not by attack detail.
  - THE BITTEN AND DYING are shown with TOTAL DIGNITY: fear, weakness,
    being carried and tended, a cloth bound at a leg. NEVER a wound,
    NEVER blood, NEVER gore, NEVER a corpse. The healing is WHOLENESS and
    WONDER — the same man risen and strong, no before-gore contrast.
  - NO DIVINE FIGURE IS EVER SHOWN (OT era). The LORD (g1) is HEARD, not
    seen — where his voice comes, word it as brilliant/luminous warm light
    in the SKY with NO figure and NO ring-around-a-head. Jesus (j1) is
    HEARD, not seen — his beats hold on the lifted serpent / cross-form,
    never on a person. No halo, glow, or rim-light anywhere.
  - THE BRONZE SERPENT ON THE POLE is the visual anchor and the cross
    foreshadow — a plain straight pole so its silhouette reads as an
    upright cross-form against the sky. It is the payoff of the whole film.

MOVIE COVERAGE (lesson 12): only the people a moment is about are in frame —
singles, two-shots, inserts. The camp is established wide AT MOST once (b01);
everything after is coverage. Every wide states camera position and where each
gaze/travel exits the frame (row-14 law). The look-and-live SEQUENCE gets a
frame per action: the bitten man TURNS to look (b18) -> he is made whole (b19)
-> the whole camp lifts their faces (b20).

TIME OF DAY ARC (intentional): the discouraged march and murmuring in hard
bright desert day; the plague at a lowering, ominous late-afternoon light;
Moses' prayer and the LORD's command at dusk; the pole raised and the looking
into a clean dawn; the John 3 close in a wide luminous morning sky — the OT
type opening toward the gospel it foreshadows.

CHANGING CONDITIONS (kept OUT of the locks): the bitten man's weakness (fevered
when struck, whole after he looks); the camp's mood (weary -> angry -> terrified
-> broken -> looking up).
"""

# LOCKS: one entry per recurring person / setting / prop. Setting locks must
# NEVER name a character. Only Jesus wears cream (he is not shown in this row).
LOCKS = {
    "MOSES": (
        "MOSES LOCK: Moses is the same man in every shot — a weathered "
        "Hebrew elder of about eighty, long grey-white hair and a full "
        "flowing grey-white beard, deep-set steady dark eyes, in a plain "
        "undyed EARTH-BROWN robe and a coarse dark-brown mantle (never "
        "cream, never white — cream is reserved), a simple worn wooden "
        "staff; grave, strong, unshaken. Same face, build and clothing "
        "throughout."
    ),
    "BITTEN-MAN": (
        "BITTEN-MAN LOCK: the one bitten man the story follows — a young "
        "Hebrew father of about thirty, short dark hair and a short dark "
        "beard, in a dust RED-BROWN tunic, a strip of pale cloth bound "
        "around his lower leg where the serpent struck; fevered and weak "
        "when bitten, then whole, upright and astonished after he looks. "
        "Same face throughout. NO wound, blood, or bite injury ever shown "
        "— only the bound cloth and his weakness carry it."
    ),
    "WILDERNESS-CAMP": (
        "WILDERNESS-CAMP LOCK: the Israelite camp in the wilderness of "
        "Edom — a vast scatter of low dun goat-hair tents on cracked tan "
        "desert floor among red-brown rock ridges and sparse dry scrub, "
        "under hard bright desert sky; dust, low cook-fires, bundles and "
        "waterskins. The same barren terrain and tents throughout. A "
        "worn, weary, first-century multitude — never a person named here."
    ),
    "SERPENT-POLE": (
        "SERPENT-POLE LOCK: the bronze serpent Moses raised — a single "
        "serpent cast in dark burnished BRONZE, its body wound once and "
        "its head lifted, fixed upright at the very top of a TALL, BARE, "
        "STRAIGHT wooden pole planted in the open camp ground; the pole "
        "plain and vertical with one short crosspiece lashed near the top "
        "to hold the serpent, so the whole silhouette reads as an upright "
        "CROSS-FORM against the open sky. The same serpent and pole in "
        "every shot it appears. Never a live snake, never a person on it."
    ),
}

REF = True

# No divine figure and no reference face is attached anywhere in this OT-era
# row: the LORD (g1) and the Son of man (j1) are heard, never shown, so every
# beat is jesus=False, ref=False. Guard against a stray-Jesus / stray-God frame.
BEATS = [
    {
        "id": "v2-r140-b01", "out": "s01-out-of-egypt-on-a-miracle.jpeg", "seg": "n0",
        "window": "0.28-6.50", "wide": True, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP"],
        "narration": "Israel had walked out of Egypt on a miracle.",
        "must_show": "ESTABLISH (once): a high wide of the vast Israelite multitude strung out in a long dusty column across the barren red-rock wilderness, moving away from camera toward a hazed horizon on the right; tents, flocks and bundles, a whole nation on the march under hard bright sky.",
        "must_not_show": "no halo, glow or rim-light; no divine figure; no modern objects; not cartoon — realistic biblical photography; nobody's face large — this is the establishing wide only.",
        "scene": (
            "The camera looks down from a ridge onto the whole "
            "nation on the move: a long dust-hazed column of "
            "tens of thousands — families, laden donkeys, herded "
            "goats, rolled goat-hair tents — winding LEFT-to-RIGHT "
            "across a cracked tan valley floor between red-brown "
            "rock walls, all of it trudging away toward a bleached "
            "horizon on the right, the hard desert light flattening "
            "everything to dust and heat. A people who left Egypt on "
            "miracles, small under an enormous empty sky. THE CAMERA "
            "STANDS HIGH AND BEHIND the column and shoots PAST them: "
            "the marchers are seen from behind, their backs to the "
            "lens, not one face turned toward the camera as they trudge "
            "away toward the right. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b02", "out": "s02-patience-wore-through.jpeg", "seg": "n0",
        "window": "6.50-12.48", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP"],
        "narration": "But the wilderness was long, and their patience wore through.",
        "must_show": "the weariness up close — a single worn Hebrew family trudging the desert road, a mother with a heavy bundle and a sunburnt child, faces drawn with exhaustion and heat; the long road told on their bodies.",
        "must_not_show": "no halo; no divine figure; no gore; no modern objects; not cartoon; keep it to one small tired family — do not crowd the frame.",
        "scene": (
            "A tight, low travelling shot on one exhausted family in "
            "the column: a sun-darkened mother shifting a heavy "
            "rolled bundle on her back, a small child clinging to her "
            "hip with cracked lips, a grandfather leaning on a staff a "
            "step behind — all of them squinting into a wind of "
            "grit, sandals worn thin, the endless red waste blurred "
            "behind them; the kind of tiredness that finally curdles "
            "hope into complaint. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r140-b03", "out": "s03-they-turned-on-god.jpeg", "seg": "n1",
        "window": "12.48-19.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "MOSES"],
        "narration": (
            "On the hard road around Edom, tired and discouraged, they "
            "turned on the very God who had rescued them, and on Moses."
        ),
        "must_show": "the turn against Moses — a knot of hard-faced Israelite men rounding on Moses with angry gestures, jabbing fingers toward him; Moses stands grave and steady among them, not flinching; the crowd's anger aimed RIGHT-to-LEFT at him.",
        "must_not_show": "no halo; no divine figure; no violence or blows — anger and accusation only; keep it to Moses and the few accusers, not the whole camp.",
        "scene": (
            "An over-shoulder two-shot from behind the accusers: three "
            "or four dust-caked men crowd in from the right, faces "
            "twisted with grievance, hands thrown out and fingers "
            "stabbing toward Moses — who stands at frame left, an old "
            "man in earth-brown with his wooden staff, weathered and "
            "unshaken, absorbing the blame without a step back. The "
            "quarrel is all aimed one way, at him. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b04", "out": "s04-wherefore-brought-us-up.jpeg", "seg": "p1",
        "window": "19.92-25.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP"],
        "narration": (
            "Wherefore have ye brought us up out of Egypt to die in the "
            "wilderness? for there is no bread, neither is there any water"
        ),
        "must_show": "SCRIPTURE-EXACT: the accusation — one furious Hebrew man mid-shout, arm flung back toward the horizon (toward Egypt), his other hand open at the empty waste around him; the grievance of no bread and no water on his face.",
        "must_not_show": "no halo; no divine figure; keep to the one shouting man and a couple behind — a single, not a mob; not cartoon.",
        "scene": (
            "A close low shot on one man at the height of the "
            "murmuring: bearded, sun-scorched, mouth open in a shout, "
            "one arm flung back over his shoulder toward the far "
            "horizon they came from, the other sweeping across the "
            "waterless red waste around him as if to say LOOK — nothing "
            "here; two more angry faces blurred behind him. All "
            "grievance and heat, no fear yet. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b05", "out": "s05-loatheth-this-light-bread.jpeg", "seg": "p1",
        "window": "25.40-30.64", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "and our soul loatheth this light bread.",
        "must_show": "INSERT: the despised manna — a shallow clay bowl of pale, small round manna flakes being shoved away or spilled onto the dust by a scornful hand; the bread from heaven treated as garbage.",
        "must_not_show": "no halo; no divine figure; no face needed — hands and the bowl carry it; no modern dishware; not cartoon.",
        "scene": (
            "A tight insert on hands and a bowl: a shallow rough clay "
            "dish heaped with pale, delicate, coriander-seed-sized "
            "manna flakes, and a calloused hand tipping it contemptuously "
            "so the little pale grains spill and scatter across the "
            "cracked dust — heaven's bread thrown to the ground as "
            "worthless. Warm hard daylight, the grains pale and bright "
            "against the dark earth. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r140-b06", "out": "s06-bread-called-worthless.jpeg", "seg": "n2",
        "window": "30.64-35.60", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "They had bread from heaven every morning — and called it worthless."
        ),
        "must_show": "the manna at dawn — the same pale manna lying thick and untouched like dew-frost across the desert floor and scrub at first light, a gift ignored; no people, or only a distant unheeding back.",
        "must_not_show": "no halo; no divine figure; no modern objects; keep it quiet and empty — the ignored provision; not cartoon.",
        "scene": (
            "A low, still ground-level shot at grey dawn: a fine layer "
            "of pale manna lying like frost over the cracked earth and "
            "the dry scrub, every small round flake beaded with dawn "
            "light, stretching untouched to a few dim tents — a daily "
            "miracle nobody bends to gather, provision lying scorned in "
            "the dirt while the camp sleeps off its anger. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b07", "out": "s07-a-real-danger.jpeg", "seg": "n2",
        "window": "35.60-40.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP"],
        "narration": (
            "And the wilderness was about to show them what a real danger "
            "looked like."
        ),
        "must_show": "the first hint of the danger — a single desert viper sliding low through the dry scrub and rocks at the edge of the camp, unnoticed, moving toward the tents; ominous lowering afternoon light.",
        "must_not_show": "no halo; no divine figure; the snake is a NATURAL desert viper, not monstrous, not lunging, not reared at camera; no gore; not cartoon.",
        "scene": (
            "A low, tense shot into the scrub at the camp's edge as the "
            "afternoon light goes hard and coppery: a single sand-"
            "coloured desert viper threads silently between the stones "
            "and dry thornbush, its body a natural muscular curve, head "
            "low, moving in toward the unsuspecting tents just visible "
            "beyond — the wilderness itself turning on the people, still "
            "unseen by them. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r140-b08", "out": "s08-fiery-serpents-sent.jpeg", "seg": "s1",
        "window": "40.28-43.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP"],
        "narration": "And the LORD sent fiery serpents among the people,",
        "must_show": "SCRIPTURE-EXACT: serpents among the camp — several desert vipers moving across the open ground between the tents while people scramble back and up onto rocks in alarm, snatching children away; terror without gore.",
        "must_not_show": "no halo; no divine figure; snakes natural, not monstrous; NO bites shown in close detail, no blood, no wounds; fear and flight carry it; not cartoon.",
        "scene": (
            "A wider camp-floor shot in hard copper light: two or three "
            "sand-coloured vipers wind across the packed dirt between "
            "the goat-hair tents while people recoil in every direction "
            "— a mother snatching a toddler up onto a boulder, men "
            "backing away with arms flung wide to hold others off, a "
            "waterskin dropped and forgotten — the whole camp jolting "
            "from complaint into real fear. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b09", "out": "s09-they-bit-the-people.jpeg", "seg": "s1",
        "window": "43.10-45.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["BITTEN-MAN"],
        "narration": "and they bit the people;",
        "must_show": "the bitten man caught — the young Hebrew father (BITTEN-MAN) sinking to one knee, gripping his lower leg where a strip of cloth is being wound, his face going grey with fever-shock; a companion catching him under the arms; dignity, no gore.",
        "must_not_show": "no halo; no divine figure; NO visible wound, NO blood, NO snake on his body — only the bound cloth and his sudden weakness; not cartoon.",
        "scene": (
            "A close two-shot low to the ground: the young father buckles "
            "onto one knee clutching his lower leg where a friend is "
            "hurriedly binding a strip of pale cloth, his face draining "
            "to a grey sweat as the venom takes him, eyes wide with the "
            "shock of it; the friend braces him under one arm, half "
            "catching him from the dust. The injury is entirely told by "
            "the bound cloth and his collapse — nothing gruesome. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b10", "out": "s10-much-people-died.jpeg", "seg": "s1",
        "window": "45.40-47.82", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP"],
        "narration": "and much people of Israel died.",
        "must_show": "the toll, with restraint — rows of the fevered sick lying on mats in the tent shade being tended by grieving family, a woman bowed weeping over a still form wrapped in cloth; sorrow, never gore or exposed death.",
        "must_not_show": "no halo; no divine figure; NO corpses exposed, no blood, no wounds, no death detail — wrapped forms and grief only; not cartoon.",
        "scene": (
            "A quiet, sorrowful shot along the shaded edge of the tents "
            "in failing light: fevered men and women lie on woven mats "
            "while kin kneel to press water to their lips, and at the "
            "near end a woman is bowed low, face in her hands, over a "
            "still form gently wrapped head-to-foot in pale cloth — the "
            "cost of the plague shown as loss and mourning, restrained "
            "and reverent, no horror. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r140-b11", "out": "s11-running-to-moses.jpeg", "seg": "n3",
        "window": "47.82-54.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "WILDERNESS-CAMP"],
        "narration": (
            "The bites spread through the camp. And the same people who had "
            "cursed God came running back to Moses, broken."
        ),
        "must_show": "the people rushing to Moses — desperate Israelites hurrying toward Moses' tent from frame right, hands reaching out to him, the same anger now turned to pleading; Moses at frame left turning to receive them.",
        "must_not_show": "no halo; no divine figure; no violence; keep it to a handful of desperate people and Moses, not the whole nation; not cartoon.",
        "scene": (
            "A medium shot as dusk comes on: a cluster of stricken people "
            "surges toward Moses' tent from the right — a man half-"
            "carrying his fevered brother, a woman with her arms flung "
            "out, faces broken open with fear and shame — reaching "
            "toward the old man in earth-brown who turns at frame left, "
            "staff in hand, to meet them; the very crowd that cursed him "
            "now running to him for help. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r140-b12", "out": "s12-we-have-sinned.jpeg", "seg": "p2",
        "window": "54.52-63.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES"],
        "narration": (
            "We have sinned, for we have spoken against the LORD, and against "
            "thee; pray unto the LORD, that he take away the serpents from us."
        ),
        "must_show": "SCRIPTURE-EXACT: the confession — an Israelite elder on his knees before Moses, hands lifted open in plea and confession, head bowed; Moses standing over him grave and moved, listening.",
        "must_not_show": "no halo; no divine figure; keep it to the kneeling man and Moses (one or two others behind at most); not cartoon.",
        "scene": (
            "A close, quiet two-shot at dusk: a grey-bearded Israelite "
            "kneels in the dust before Moses, both hands raised open and "
            "trembling in confession, his face tipped down and streaked "
            "with dust and tears, saying the words that turn everything "
            "— we have sinned; behind him one more bows his head. Moses "
            "stands close over him in earth-brown, staff in hand, grave "
            "and stirred, taking in the plea. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b13", "out": "s13-moses-prayed.jpeg", "seg": "n4",
        "window": "63.42-70.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "WILDERNESS-CAMP"],
        "narration": (
            "So Moses prayed for the people who had just turned on him. And "
            "the LORD answered — but not the way anyone expected."
        ),
        "must_show": "Moses interceding — Moses alone, apart from the camp at dusk, standing with his staff and both arms lifted, face raised to the darkening sky in prayer for the people; the quiet toll of the camp small behind him.",
        "must_not_show": "no halo, glow or rim-light; NO figure in the sky (the LORD is not shown here); no modern objects; Moses alone, not crowded; not cartoon.",
        "scene": (
            "A reverent wide-ish shot of Moses set apart on a low rise as "
            "the last daylight drains from a deep-blue sky: the old man "
            "stands with his staff planted and both weathered arms lifted, "
            "face turned up into the dusk, praying for the very people who "
            "cursed him — the dim, sorrowing camp and its cook-fires far "
            "below and behind him. The sky is empty and darkening; no "
            "figure, only a man and his God. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b14", "out": "s14-make-thee-a-fiery-serpent.jpeg", "seg": "g1",
        "window": "70.50-77.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES"],
        "narration": (
            "Make thee a fiery serpent, and set it upon a pole:"
        ),
        "must_show": "SCRIPTURE-EXACT: Moses receiving the command — Moses' face and upper body, eyes lifted and attentive to a brilliant warm light breaking in the night sky above frame, listening; no figure in the light, only radiance and Moses' listening face.",
        "must_not_show": "no halo, glow, or rim-light around his head; NO figure, disc, orb, ring, beam or UFO in the sky — only formless brilliant warm light; not cartoon.",
        "scene": (
            "A close low shot on Moses at night, lit from above by a break "
            "of brilliant warm light spilling down out of the dark sky: "
            "his lined face is tipped up into it, eyes open and steady, "
            "lips parted as he takes in an instruction that makes no sense "
            "to a soldier — the light itself formless and pure, no shape "
            "in it, casting a warm wash over his grey beard and the "
            "earth-brown of his mantle. He listens the way a man listens "
            "when he has stopped arguing. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r140-b15", "out": "s15-when-he-looketh-shall-live.jpeg", "seg": "g1",
        "window": "77.20-83.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES"],
        "narration": (
            "and it shall come to pass, that every one that is bitten, when "
            "he looketh upon it, shall live."
        ),
        "must_show": "the promise landing — Moses lowering his eyes from the light with dawning resolve, one hand rising to his beard or heart as he grasps the strange mercy of it: a look will be enough; quiet wonder, not doubt.",
        "must_not_show": "no halo or glow; no figure in the sky; keep to Moses alone; not cartoon.",
        "scene": (
            "A held close-up on Moses as the warm light dims to a faint "
            "wash at the edge of frame: he lowers his face from the sky, eyes "
            "distant and wide with the weight of what he has just been "
            "given — that the dying will not have to climb, or pay, or "
            "fight, only LOOK — one weathered hand lifting to his chest, "
            "his mouth set with the resolve of a man about to obey a thing "
            "he could never have invented. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r140-b16", "out": "s16-a-serpent-of-bronze.jpeg", "seg": "n5",
        "window": "83.11-88.90", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "No cure to brew. No ritual to perform. No strength left to "
            "muster. Just a shape of bronze lifted on a pole,"
        ),
        "must_show": "INSERT: the making — hands working a small bright forge-fire at night, hammering and coiling a length of glowing bronze into the form of a serpent; sparks, tongs, the serpent-shape taking form; no faces needed.",
        "must_not_show": "no halo or glow around a head; no divine figure; no modern tools; the bronze is worked metal, not a live snake; not cartoon.",
        "scene": (
            "A tight, warm insert on working hands at a small night forge: "
            "a coil of bronze burning amber-orange gripped in iron tongs "
            "over red-hot coals, a hammer caught mid-strike throwing a "
            "spray of sparks, the metal already bent into the unmistakable "
            "wound curve and lifted head of a serpent — plain craft, no "
            "ceremony, the humble object on which everything will hang "
            "taking shape in firelight. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r140-b17", "out": "s17-lifted-on-a-pole.jpeg", "seg": "n5",
        "window": "88.90-94.25", "wide": True, "jesus": False, "ref": False,
        "locks": ["SERPENT-POLE", "WILDERNESS-CAMP"],
        "narration": "and one thing left to do — look.",
        "must_show": "THE ANCHOR: the bronze serpent-pole raised upright in the middle of the camp at first light, Moses steadying its base, the plain straight pole with the bronze serpent at top reading as a clear CROSS-FORM against a clean dawn sky; a few stricken people at its foot beginning to lift their faces.",
        "must_not_show": "no halo, glow or rim-light; the pole is bare and plain so the silhouette reads as a cross; no divine figure; the serpent is bronze, never alive; not cartoon.",
        "scene": (
            "A low, wide hero shot into a clean pale-gold dawn: the tall "
            "bare pole stands planted in the open heart of the camp, the "
            "dark bronze serpent fixed and gleaming at its very top on a "
            "short crosspiece so the whole thing stands against the "
            "brightening sky as an unmistakable upright cross-form; Moses "
            "braces its foot in earth-brown, and around the base a few "
            "fevered people, propped by kin, are just beginning to raise "
            "their eyes toward it. The camera looks up past them to the "
            "serpent and the open sky. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r140-b18", "out": "s18-when-he-beheld-he-turned.jpeg", "seg": "s2",
        "window": "94.25-98.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["BITTEN-MAN", "SERPENT-POLE"],
        "narration": (
            "And Moses made a serpent of brass, and put it upon a pole, and "
            "it came to pass,"
        ),
        "must_show": "SCRIPTURE-EXACT (the look, action 1 of 3): the bitten young father (BITTEN-MAN), grey and weak on the ground, TURNING his head and lifting his eyes up toward the bronze serpent on the pole above him; the effortful turn of a dying man to look.",
        "must_not_show": "no halo or glow; no wound or gore; the serpent bronze not alive; keep to the one man and the pole above; not cartoon.",
        "scene": (
            "A low over-the-shoulder from beside the bitten father: he is "
            "down on the dust, propped on one failing arm, his face grey "
            "and sheened with fever and the bound cloth at his leg — and "
            "with the last of his strength he TURNS his head and lifts "
            "his eyes upward, past his own trembling shoulder, to the "
            "dark bronze serpent lifted small and bright against the dawn "
            "at the top of its pole. The whole shot is the act of looking. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b19", "out": "s19-when-he-beheld-he-lived.jpeg", "seg": "s2",
        "window": "98.80-102.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["BITTEN-MAN"],
        "narration": (
            "that if a serpent had bitten any man, when he beheld the serpent "
            "of brass,"
        ),
        "must_show": "SCRIPTURE-EXACT (action 2 of 3): the healing as WHOLENESS — the same young father rising up onto his knees then his feet, the grey gone from his face, colour and strength flooding back, wonder breaking over him as he keeps his eyes upward; the bound cloth loose.",
        "must_not_show": "no halo or glow; no before-gore contrast; wholeness and wonder carry it; the cloth loosening, no wound beneath; not cartoon.",
        "scene": (
            "A rising medium shot on the same father a heartbeat later: "
            "the grey has drained out of his face and warm living colour "
            "has rushed back into it, his eyes still fixed upward and "
            "flooding with astonishment as he pushes up from the dust "
            "onto his knees and rises — strength visibly returning to a "
            "body that was dying seconds ago, the pale binding-cloth "
            "slipping loose and forgotten at his healed leg. Life, plain "
            "and total, from a single look. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b20", "out": "s20-the-whole-camp-looked-up.jpeg", "seg": "s2",
        "window": "102.40-105.92", "wide": True, "jesus": False, "ref": False,
        "locks": ["SERPENT-POLE", "WILDERNESS-CAMP"],
        "narration": "he lived.",
        "must_show": "the whole camp looking — a wide of the bronze serpent-pole high in the dawn with people all across the camp turning and lifting their faces up toward it, the sick being propped and turned to see; the cross-form high against the open sky over a people looking up.",
        "must_not_show": "no halo, glow or rim-light; no divine figure; the pole plain, the serpent bronze; not cartoon.",
        "scene": (
            "A wide low shot back across the waking camp into the gold "
            "dawn: the tall pole and its bronze serpent rise as a clear "
            "cross-form over the tents, and everywhere below, people are "
            "turning their faces up to it — the strong lifting the "
            "fevered so they can see, mothers tilting children's chins "
            "skyward, a whole stricken multitude doing the one simple "
            "thing and living for it. THE CAMERA STANDS BEHIND AND BELOW "
            "the crowd and shoots PAST them up the pole: the people are "
            "seen from behind, their backs to the lens and their faces "
            "lifted away toward the serpent, not one face turned toward "
            "the camera. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b21", "out": "s21-only-had-to-lift-his-eyes.jpeg", "seg": "n6",
        "window": "105.92-113.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["SERPENT-POLE"],
        "narration": (
            "A dying man didn't have to earn it, or explain it, or even "
            "understand it. He only had to trust it enough to lift his eyes "
            "toward it."
        ),
        "must_show": "the simple act, close — a weak, sweat-beaded face and one trembling upraised hand, eyes lifting toward the bronze serpent (soft-focused above); faith reduced to a single upward look, nothing earned, nothing understood.",
        "must_not_show": "no halo or glow; no wound; keep it to the one lifted face and hand; not cartoon.",
        "scene": (
            "A very tight close-up on a fevered face tipped upward at "
            "dawn — cracked lips, exhausted eyes filling with fragile "
            "hope, one weathered hand rising unsteadily toward the sky — "
            "and, thrown soft and bright above and behind, the shape of "
            "the bronze serpent on its pole; the whole image is the "
            "smallest possible act of faith, a look given by someone with "
            "nothing left to give. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r140-b22", "out": "s22-reached-back-to-the-cross.jpeg", "seg": "n7",
        "window": "113.56-119.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["SERPENT-POLE"],
        "narration": (
            "Fourteen hundred years later, Jesus reached back and picked this "
            "exact moment to explain his own cross."
        ),
        "must_show": "the bridge — the bronze serpent-pole in near silhouette against a wide brightening sky, its plain vertical pole and crosspiece read unmistakably as a CROSS on the horizon; empty wilderness around it, the type quietly becoming the foreshadow.",
        "must_not_show": "no halo, glow or rim-light; NO Jesus figure, NO cross of wood with a body, NO anachronism — only the bronze serpent-pole whose SHAPE is the cross; not cartoon.",
        "scene": (
            "A still, wide silhouette shot: the tall bare pole with the "
            "bronze serpent stands alone against an enormous brightening "
            "dawn sky over the empty red wilderness, its vertical line and "
            "single crosspiece reading plainly as a cross on the horizon "
            "— the same lifted-up thing, fourteen centuries early, holding "
            "the shape of the cross it was always pointing to. Reverent, "
            "spare, luminous. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r140-b23", "out": "s23-son-of-man-lifted-up.jpeg", "seg": "j1",
        "window": "119.83-126.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["SERPENT-POLE"],
        "narration": (
            "And as Moses lifted up the serpent in the wilderness, even so "
            "must the Son of man be lifted up:"
        ),
        "must_show": "SCRIPTURE-EXACT (Jesus's own words, HEARD not shown): a low reverent shot up the serpent-pole to the bronze serpent lifted high against a radiant morning sky, the cross-form filling the frame; NO person, the lifted-up type standing for the lifted-up Son of man.",
        "must_not_show": "no halo, glow or rim-light; NO Jesus figure and NO God figure (he is heard, never shown); no wooden cross with a body; only the bronze serpent-pole; not cartoon.",
        "scene": (
            "A low, worshipful shot looking straight up the length of the "
            "bare pole to the dark bronze serpent fixed at its top, held "
            "against a wide radiant morning sky pouring clean warm light "
            "down around it — the lifted-up serpent alone in frame, its "
            "cross-form unmistakable, standing in for the One whose words "
            "these are. No figure, only the sign lifted up and the light. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b24", "out": "s24-whosoever-believeth.jpeg", "seg": "j1",
        "window": "126.20-131.10", "wide": True, "jesus": False, "ref": False,
        "locks": ["SERPENT-POLE", "WILDERNESS-CAMP"],
        "narration": (
            "That whosoever believeth in him should not perish, but have "
            "eternal life."
        ),
        "must_show": "the promise wide — the serpent-pole cross-form on its rise catching the full morning light over the wilderness, healed people small at its foot with faces still lifted; open luminous sky filling most of the frame; hope, life, no perishing.",
        "must_not_show": "no halo or rim-light around a head; no divine figure; the pole plain; not cartoon; nobody's face large — this is the closing wide.",
        "scene": (
            "A wide closing shot into a vast luminous morning: the bronze "
            "serpent on its tall pole stands as a cross-form on the low "
            "rise, washed in clean warm light, and at its foot the "
            "healed — whole and upright now — stand small with their "
            "faces still turned up to it; the enormous bright sky opens "
            "above them all, the wilderness behind them, the whole frame "
            "tipped toward life instead of death. THE CAMERA STANDS "
            "BEHIND the healed and shoots PAST their backs toward the "
            "pole and sky: they are seen from behind, backs to the lens, "
            "faces lifted away toward the cross-form, no face turned "
            "toward the camera. Every figure has two "
            "arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (new places — no stash plate exists yet; promote-first) ===
# WILDERNESS-CAMP and SERPENT-POLE are NEW settings with no plate in the stash.
# RUNNER: promote the first good frame of each so the rest of the build copies
# its look (v2_stash.py --promote):
#   WILDERNESS-CAMP  -> promote from b01 (the establishing wide) before b02/b03/
#                       b07/b08/b10/b11/b13/b17/b20/b24.
#   SERPENT-POLE     -> promote from b17 (the raised-pole hero) before b18/b20/
#                       b22/b23/b24 so the pole + bronze serpent stay identical.
# The two follow people (MOSES, BITTEN-MAN) are locked by text here and by the
# per-story face board at assembly; no Jesus/God reference is attached anywhere.
PLACE_REFS = {}
