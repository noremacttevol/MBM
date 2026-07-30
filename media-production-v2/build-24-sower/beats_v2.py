#!/usr/bin/env python3
"""V2 beat map — row 24, build-24-sower (Matthew 13:1-23).

COVERAGE: 25 pictures over 140.8 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 13:1-23 KJV):
  v1-2  "sat BY THE SEA SIDE. And great multitudes were gathered together
        unto him, so that HE WENT INTO A SHIP, AND SAT; and the whole
        multitude stood ON THE SHORE." — the frame is the Sea of Galilee:
        Jesus SEATED in a small boat a little way off the beach, the crowd
        standing on the shore and rising hillside. He sits to teach; he does
        not stand in the boat.
  v3    "Behold, a sower went forth to sow" — broadcast sowing from a seed
        bag, flung by hand in wide arcs; never modern equipment.
  v4    "some seeds fell by the WAY SIDE, and the FOWLS came and devoured
        them" — a packed footpath along the field's edge; birds eat the seed.
  v5-6  "STONY PLACES, where they had not much earth; and forthwith they
        sprung up ... and when the SUN was up, they were SCORCHED" — thin
        soil over rock: fast green shoots, then withering under hot sun.
  v7    "some fell among THORNS; and the thorns sprung up, and CHOKED them."
  v8    "GOOD ground ... some an hundredfold, some sixtyfold, some
        thirtyfold" — full heavy harvest.
  v19-23 the interpretation: the grounds are HEARTS. The narration's
        interpretation beats stay in the parable's imagery — no literal
        painted hearts, ever.

TIME OF DAY: the frame story (shore + boat) is bright mid-morning on the Sea
of Galilee, constant across its beats. Inside the parable the light serves
the meaning: sowing in fresh morning light; the scorching beat under HARD
HOT MIDDAY sun (v6 requires it); the thorn beat in flat overcast-bright
light; the good-ground harvest in warm late-golden light; the closing
keep-sowing beat at fresh morning again — the sower goes out again. These
shifts are scripture-driven, not the row-11 defect.

CONTENT-CARE: row 24 has no flag in §3. Nothing sensitive; birds eat seed,
plants wither — no animal or human harm.

CHANGING CONDITION (kept OUT of the locks): the state of the plants — seed,
young shoots, withered stems, choked stalks, full heavy heads of grain — is
per-beat and never locked.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "SOWER": (
        "SOWER LOCK: the sower is the same man in every shot — a broad "
        "Galilean farmer of about fifty, thick through the chest, with a heavy "
        "grey-streaked dark beard, deep sun-creases at his eyes and big "
        "gentle work-hardened hands. He wears a coarse DARK RUSSET-BROWN wool "
        "tunic kilted up through a wide leather belt, with a large canvas "
        "seed-bag slung across his chest on a strap (never cream, never "
        "white). His face is shown clearly."
    ),
    "FIELD": (
        "FIELD LOCK: one Galilean hillside field seen across the row — a "
        "long strip of open ploughed earth on a gentle slope, bounded on one "
        "side by a pale hard-packed footpath, with a shelf of grey limestone "
        "breaking the soil in one corner, a tangle of dark thorn bushes along "
        "the low stone boundary wall, and the deep soft brown of good "
        "ploughed ground through the middle. Distant blue hills beyond."
    ),
    "SHORE": (
        "SHORE LOCK: a curved pebble-and-sand beach on the Sea of Galilee — "
        "clear green-blue water, a small weathered wooden fishing boat with "
        "a single mast floating a few boat-lengths off the beach, and behind "
        "the beach a grassy hillside rising in a natural bowl. Bright "
        "mid-morning light with small broken clouds."
    ),
    "CROWD": (
        "CROWD LOCK: the listening multitude is ordinary Galilean men, women "
        "and children of every age, dressed in SATURATED DEEP earth colours "
        "— dark chocolate brown, deep russet, dark olive, burnt ochre, dusty "
        "indigo and faded plum wool (never cream, never white; only Jesus "
        "wears cream). Their faces are shown clearly."
    ),
}

REF = True

BEATS = [
    # --------------------------------------------- n1/n2/s3 — boat and shore ----
    {
        "id": "v2-r024-b01", "out": "s01-so-many-people-crowded-the.jpeg", "seg": "n1",
        "window": "0.28-9.29", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CROWD", "SHORE"],
        "narration": (
            "So many people crowded the shore to hear Jesus that he pushed a "
            "small boat out onto the water and taught them from there, the "
            "whole hillside listening."
        ),
        "must_show": "SCRIPTURE-EXACT: Jesus SEATED in the small boat a little way off the beach, and the crowd filling the shore and the rising hillside behind — the whole natural amphitheatre in one frame.",
        "must_not_show": "no halo, glare or rim-light on Jesus; he SITS in the boat (v2 'he went into a ship, and sat') — never standing; nobody stands on the water.",
        "scene": (
            "From high on the hillside looking down: the curved beach packed "
            "with hundreds of people standing shoulder to shoulder, more "
            "seated up the grassy slope in the foreground, and out on the "
            "clear green-blue water, a few boat-lengths off the beach, the "
            "small wooden fishing boat with Jesus seated in its stern facing "
            "the land, one hand raised mid-word. Every face on the shore is "
            "turned toward the boat. Bright mid-morning light, small broken "
            "clouds. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b02", "out": "s02-and-ground-can-change.jpeg", "seg": "n12",
        "window": "129.16-130.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": "And ground can change.",
        "must_show": "a close shot of one strong green shoot pushing up through broken, crumbled crust — ground that WAS hard, opening.",
        "must_not_show": "no halo, glare or rim-light; the crust around the shoot is visibly broken up, not smooth soil.",
        "scene": (
            "A close shot at soil level, upright and level, the ground at the "
            "bottom of the frame and the soft sky at the top: one strong "
            "young green shoot standing up through a patch of pale packed "
            "crust that has been broken open, the cracked crumbs of the old "
            "hard surface pushed aside around its stem, fresh dark earth "
            "showing in the break. Warm morning light. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b03", "out": "s03-and-he-told-them-a.jpeg", "seg": "n2",
        "window": "9.95-14.22", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CROWD", "SHORE"],
        "narration": "And he told them a story about a farmer, and four kinds of ground.",
        "must_show": "closer on the boat — Jesus seated, easy and unhurried, beginning the story; the front of the crowd at the waterline listening.",
        "must_not_show": "no halo, glare or rim-light on Jesus; he remains seated in the boat.",
        "scene": (
            "Closer now, from just above the waterline at the edge of the "
            "crowd: Jesus seated in the gently rocking boat, forearms resting "
            "on his knees, leaning slightly toward the shore as he begins the "
            "story, the water throwing moving light up onto the hull. In the "
            "near foreground the front rank of listeners stands ankle-deep "
            "and dry-shod at the water's edge — a fisherman, a mother with a "
            "child on her hip, an old man leaning on a staff — all still. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b04", "out": "s04-behold-a-sower-went-forth.jpeg", "seg": "j1",
        "window": "19.06-21.15", "wide": True, "jesus": False, "ref": False,
        "locks": ["SOWER", "FIELD"],
        "narration": "Behold, a sower went forth to sow;",
        "must_show": "SCRIPTURE-EXACT: the parable opens — the sower walking out onto his field in fresh morning light, seed-bag full at his chest, the whole strip of ground before him.",
        "must_not_show": "no halo, glare or rim-light; hand-sowing from a bag — no tools or equipment beyond bag and hand.",
        "scene": (
            "Fresh clear morning over the hillside field: the broad farmer "
            "walks out along the edge of the ploughed strip with his full "
            "canvas seed-bag riding at his chest, one hand already dipped "
            "into it, dew still darkening the earth and long cool shadows "
            "running off the low sun. The pale footpath, the grey limestone "
            "shelf, the dark thorn tangle and the deep brown ploughed middle "
            "of the field all lie ahead of him. The camera stands in the "
            "field watching him come. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r024-b05", "out": "s05-a-farmer-went-out-to.jpeg", "seg": "n3",
        "window": "22.22-26.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["SOWER"],
        "narration": (
            "A farmer went out to scatter his seed. He did not measure it out "
            "grain by grain."
        ),
        "must_show": "a close shot of the sower's big hand coming up FULL of grain out of the open seed-bag — abundance in one fist.",
        "must_not_show": "no halo, glare or rim-light; the hand is full to overflowing — a few grains already spilling; never a careful pinch.",
        "scene": (
            "A close shot of the farmer's thick sun-browned hand rising out "
            "of the open canvas seed-bag heaped with pale gold grain, his "
            "fist packed full, several kernels already spilling over his "
            "fingers and falling. The rough russet wool of his tunic and the "
            "worn leather strap fill the background softly. Fresh morning "
            "light picks out every falling grain. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b06", "out": "s06-he-flung-it-wide-across.jpeg", "seg": "n3",
        "window": "26.56-31.51", "wide": True, "jesus": False, "ref": False,
        "locks": ["SOWER", "FIELD"],
        "narration": (
            "He flung it wide, across every kind of ground, hoping all of it "
            "would grow."
        ),
        "must_show": "SCRIPTURE-EXACT: the fling itself — the sower mid-stride, arm swept full out, an arc of grain hanging in the air across the field.",
        "must_not_show": "no halo, glare or rim-light; the grain arc must read as thrown seed in flight, not rain or dust.",
        "scene": (
            "The farmer strides along the ploughed strip caught at the top "
            "of his throw — his right arm swept out level with his shoulder, "
            "a wide fan of pale grain hanging in the morning air ahead of "
            "him, scattering toward path, stones and open earth alike. His "
            "tunic swings with the stride and his eyes follow the flight of "
            "the seed. The camera stands side-on to catch the whole arc "
            "against the field and far blue hills. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    # ------------------------------------------------ v4-v7 — the four grounds ----
    {
        "id": "v2-r024-b07", "out": "s07-and-when-he-sowed-some.jpeg", "seg": "j4",
        "window": "32.21-37.04", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": (
            "And when he sowed, some seeds fell by the way side, and the fowls "
            "came and devoured them up:"
        ),
        "must_show": "SCRIPTURE-EXACT: scattered grain lying ON TOP of the pale packed footpath, and dark birds already dropping in and pecking it up.",
        "must_not_show": "no halo, glare or rim-light; the seed sits ON the surface — none of it buried; the birds are ordinary dark field birds.",
        "scene": (
            "The hard pale footpath along the field's edge, its surface "
            "packed smooth and cracked, with pale gold grains lying scattered "
            "openly on top of it — and half a dozen dark birds already down "
            "among them, heads stabbing, two more braking out of the air "
            "with wings spread to land. Fresh morning light throws the "
            "birds' quick shadows on the path. The camera is low but level "
            "and upright, the path at the bottom of the frame and the field "
            "and sky above. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r024-b08", "out": "s08-some-fell-on-the-hard.jpeg", "seg": "n4",
        "window": "38.02-46.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": (
            "Some fell on the hard path, packed down by every foot that had "
            "ever walked it. It never sank in, and the birds came and ate it."
        ),
        "must_show": "a close shot of the path surface itself — grain sitting on sealed, foot-polished crust it cannot enter, one bird's beak closing on a kernel.",
        "must_not_show": "no halo, glare or rim-light; no soft or broken earth in frame — this ground is shut.",
        "scene": (
            "A close shot of the footpath's surface: crust polished smooth "
            "and hard by years of bare feet, hairline cracks running "
            "through it, and a dozen gold grains lying loose on top like "
            "beads on a table — nothing sunk in. At the frame's edge one "
            "dark bird's head is down, beak closing on a kernel. Hard clear "
            "morning light. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r024-b09", "out": "s09-that-he-said-is-a.jpeg", "seg": "n5",
        "window": "46.92-53.42", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": (
            "That, he said, is a heart so hardened that the word never gets "
            "below the surface before it is snatched away."
        ),
        "must_show": "the path stripped BARE — the birds lifting away with the last of the seed, the hard ground left exactly as it was, nothing changed.",
        "must_not_show": "no halo, glare or rim-light; no literal heart imagery — the parable's own picture carries the interpretation.",
        "scene": (
            "The pale packed footpath now stripped bare, not one grain left "
            "on its polished crust, while the flock of dark birds lifts away "
            "together into the morning sky, wings beating, the last of the "
            "seed gone with them. The path runs on unchanged between the "
            "grass edges, exactly as it was before the sowing. The camera "
            "looks along its empty length toward the rising birds. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b10", "out": "s10-some-fell-on-thin-soil.jpeg", "seg": "n6",
        "window": "54.06-56.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": "Some fell on thin soil over rock.",
        "must_show": "SCRIPTURE-EXACT: the stony corner — a skin of soil barely covering the grey limestone shelf, grains lodged in the shallow dust, rock showing through everywhere.",
        "must_not_show": "no halo, glare or rim-light; the rock beneath must be visible through the thin soil — the shallowness is the point.",
        "scene": (
            "A close shot of the field's stony corner: the grey limestone "
            "shelf lying just under a thin dusty skin of soil, the bare rock "
            "breaking through in worn patches, and pale gold grains lodged "
            "in the shallow pockets of dust between the stone. A little "
            "green moss darkens the rock's shaded seams. Clear morning "
            "light, upright and level, ground at the bottom of the frame. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b11", "out": "s11-it-sprang-up-fast-green.jpeg", "seg": "n6",
        "window": "56.14-62.74", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": (
            "It sprang up fast, green and hopeful, but it had no root, and when "
            "the sun grew hot it withered."
        ),
        "must_show": "SCRIPTURE-EXACT: the two truths in one frame — bright young shoots standing over the rock shelf, and beside them the first stems already flagging and yellowing under a HARD HOT midday sun.",
        "must_not_show": "no halo, glare or rim-light; the light here is harsh vertical noon (v6 'when the sun was up') — that heat is correct, not a colour defect.",
        "scene": (
            "The stony corner under hard vertical noon light, heat-pale sky "
            "above: a stand of young green shoots has sprung tall and thin "
            "from the shallow soil over the rock shelf — but the nearest "
            "stems have already gone limp, their blades yellowing and "
            "curling, drooping against the hot stone, while the ones behind "
            "still stand briefly green. Short black shadows pool at their "
            "bases. The camera is close over the shelf, upright and level. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b12", "out": "s12-that-is-the-heart-that.jpeg", "seg": "n7",
        "window": "63.39-69.48", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": (
            "That is the heart that says yes with joy, but has nothing "
            "underneath to hold it when things get hard."
        ),
        "must_show": "the rootlessness itself — one withered stem lifted clean out of the dust, its base bare of any root, the rock shelf beneath.",
        "must_not_show": "no halo, glare or rim-light; no hand pulling it in frame if a hand risks confusion — the bare rootless base is the whole message.",
        "scene": (
            "A very close shot in hard noon light: one withered stem lying "
            "across the thin dusty soil where the heat has felled it, its "
            "base bare and rootless — a smooth pale stub with nothing "
            "beneath it — and under the shallow dust the unbroken grey "
            "limestone shelf that stopped every root. The wilted blades curl "
            "dry against the stone. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r024-b13", "out": "s13-some-fell-among-thorns.jpeg", "seg": "n8",
        "window": "70.12-71.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": "Some fell among thorns.",
        "must_show": "SCRIPTURE-EXACT: grains fallen down among the dark tangle of thorn bushes at the boundary wall — seed in hostile company.",
        "must_not_show": "no halo, glare or rim-light; the thorns are a dense living tangle, not a dead hedge.",
        "scene": (
            "A close shot into the dark tangle of thorn bushes along the low "
            "stone boundary wall: springy interlaced branches armed with "
            "long pale thorns, small hard green leaves — and down among "
            "their shadowed roots, a scatter of pale gold grains resting on "
            "the dim earth where they fell. Flat bright light filters "
            "through the tangle in broken pieces. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b14", "out": "s14-the-seed-grew-but-so.jpeg", "seg": "n8",
        "window": "71.50-78.90", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": (
            "The seed grew, but so did the weeds, and the worries and wants of "
            "this life crowded in and choked it before it could bear anything."
        ),
        "must_show": "SCRIPTURE-EXACT: the choking — thin pale grain stalks strangled inside the risen thorns, bent and empty-headed, the tangle towering over them.",
        "must_not_show": "no halo, glare or rim-light; the grain stalks bear NO heads of grain — choked before fruit; the thorns visibly wrap and cross them.",
        "scene": (
            "At the boundary wall the thorn tangle has risen head-high and "
            "closed over: inside it a few thin pale grain stalks stand "
            "trapped, bent at odd angles where the crossing thorn branches "
            "lean on them, their tips empty of any head of grain, starved "
            "pale against the aggressive dark green of the thorns. Flat "
            "bright overcast light, no warmth. The camera looks into the "
            "tangle at standing height. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r024-b15", "out": "s15-but-other-fell-into-good.jpeg", "seg": "j8",
        "window": "79.55-85.44", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": (
            "But other fell into good ground, and brought forth fruit, some an "
            "hundredfold, some sixtyfold, some thirtyfold."
        ),
        "must_show": "SCRIPTURE-EXACT: the turn — the deep brown ploughed middle of the field carrying a broad stand of tall grain, heads full and heavy, in warm late-golden light.",
        "must_not_show": "no halo, glare or rim-light; the golden-hour warmth here is the harvest's own light, correct for this beat.",
        "scene": (
            "The wide middle of the field in warm late-golden light: a broad "
            "standing sea of tall ripe grain risen from the deep brown "
            "ploughed earth, every stalk crowned with a full heavy head "
            "bowing under its own weight, moving together in a low wind. "
            "Beyond it the pale path, the rock shelf and the dark thorn "
            "corner sit small and spent at the field's edges. The far hills "
            "lie blue. The camera looks across the whole golden stand. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b16", "out": "s16-but-some-fell-on-good.jpeg", "seg": "n9",
        "window": "86.48-89.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": "But some fell on good ground, open and soft and ready.",
        "must_show": "a close shot of grain lying in open, soft, freshly turned dark earth — kernels half-sunk in crumbled soil that receives them.",
        "must_not_show": "no halo, glare or rim-light; the contrast with the sealed path must be obvious — this earth is broken open and takes the seed in.",
        "scene": (
            "A close shot of deep brown freshly turned earth, its surface "
            "soft, crumbled and open, still dark with moisture in the "
            "furrow shadows — and pale gold grains lying half-sunk into it, "
            "the loose soil already crumbled in around their edges, taken "
            "in rather than resting on top. Warm low light rakes the "
            "furrows. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b17", "out": "s17-it-took-root-and-grew.jpeg", "seg": "n9",
        "window": "89.90-93.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["SOWER", "FIELD"],
        "narration": "It took root, and grew, and gave back a harvest many times over.",
        "must_show": "the harvest received — the sower standing IN the tall ripe grain, one heavy full head held gently in his hand, his sun-creased face glad.",
        "must_not_show": "no halo, glare or rim-light; gladness and gratitude in his face, not triumph.",
        "scene": (
            "The broad farmer stands waist-deep in the tall golden grain in "
            "warm late light, cradling one heavy bowed head of grain gently "
            "in his open palm without breaking it from the stalk, looking "
            "down at it with the deep sun-creases at his eyes folded in a "
            "quiet glad smile. The full stand sways around him to the "
            "field's edge. The camera is close, at his level, upright. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b18", "out": "s18-but-he-that-received-seed.jpeg", "seg": "j3",
        "window": "94.51-106.30", "wide": True, "jesus": False, "ref": False,
        "locks": ["SOWER", "FIELD"],
        "narration": (
            "But he that received seed into the good ground is he that heareth "
            "the word, and understandeth it; which also beareth fruit, and "
            "bringeth forth, some an hundredfold, some sixty, some thirty."
        ),
        "must_show": "SCRIPTURE-EXACT: the full yield made visible — the sower pouring threshed grain in a thick stream from his two cupped hands into a brimming basket, more filled baskets beside it.",
        "must_not_show": "no halo, glare or rim-light; the returned grain must visibly OUT-SCALE the seed-bag — many baskets from one bag.",
        "scene": (
            "At the field's edge in warm golden light the farmer kneels "
            "upright pouring a thick stream of clean threshed grain from his "
            "two cupped hands into a wide basket already brimming over, and "
            "ranged beside it stand four more baskets heaped full — while "
            "his old canvas seed-bag hangs flat and empty from its strap on "
            "a fence post behind him, its work multiplied many times over "
            "in front of it. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r024-b19", "out": "s19-and-he-spake-many-things.jpeg", "seg": "s3",
        "window": "14.92-17.89", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SHORE"],
        "narration": "And he spake many things unto them in parables, saying,",
        "must_show": "SCRIPTURE-EXACT: a close shot of Jesus seated in the boat, mid-word, the water's moving light on his face, land out of focus beyond.",
        "must_not_show": "no halo, glare or rim-light on Jesus; seated, easy, unhurried.",
        "scene": (
            "A close shot of Jesus seated on the boat's worn wooden thwart, "
            "turned toward the unseen shore, one hand lifted in an easy "
            "open gesture mid-word, the bright moving reflections off the "
            "water playing over the boat's planks. The crowded beach lies "
            "soft and out of focus beyond the gunwale. Bright mid-morning "
            "light. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b20", "out": "s20-the-good-ground-is-simply.jpeg", "seg": "n10",
        "window": "107.32-111.65", "wide": True, "jesus": False, "ref": False,
        "locks": ["CROWD", "SHORE"],
        "narration": (
            "The good ground is simply the heart that hears him, takes it in, "
            "and holds on."
        ),
        "must_show": "the listening faces on the shore — a handful of hearers close-up, each visibly taking the story in; the hearing itself, painted.",
        "must_not_show": "no halo, glare or rim-light; no literal heart imagery — the faces do the work; do not put Jesus in this frame.",
        "scene": (
            "Close along the front of the shore crowd in bright morning "
            "light: a row of listening faces at the water's edge — an old "
            "fisherman with the story working behind his eyes, a young "
            "woman with her lips slightly parted, a boy gone completely "
            "still, a grey-bearded man nodding slowly to himself — each one "
            "holding onto the words in a different way, all eyes fixed out "
            "toward the water past the camera. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b21", "out": "s21-and-it-gives-back-far.jpeg", "seg": "n10 + n11",
        "window": "111.65-118.89", "wide": True, "jesus": False, "ref": False,
        "locks": ["SOWER", "FIELD"],
        "narration": (
            "And it gives back far more than was ever put in. Notice the farmer "
            "did not skip the hard path or the rocky places."
        ),
        "must_show": "the whole field in one wide frame — path, rock shelf, thorn corner AND golden middle — with the sower's fresh footprints and scattered seed running across ALL of them without a gap.",
        "must_not_show": "no halo, glare or rim-light; the seed-line must visibly cross every kind of ground — no skipped stretch.",
        "scene": (
            "A wide frame taking in the entire strip of field in warm light: "
            "the pale packed path along one side, the grey rock shelf in its "
            "corner, the dark thorn tangle at the wall, and the deep brown "
            "good earth through the middle — and running unbroken across "
            "all four, a single line of the sower's footprints with pale "
            "grain scattered evenly the whole way, no ground passed over. "
            "The farmer himself walks on at the line's far end, still "
            "flinging. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b22", "out": "s22-he-threw-seed-everywhere-on.jpeg", "seg": "n11",
        "window": "118.89-122.35", "wide": True, "jesus": False, "ref": False,
        "locks": ["SOWER", "FIELD"],
        "narration": "He threw seed everywhere, on every heart, hoping.",
        "must_show": "the sower from behind at three-quarter, mid-fling over ground both good and bad at once, his face turned enough to show the hope in it.",
        "must_not_show": "no halo, glare or rim-light; his expression is hope, not calculation — he throws to the bad ground exactly as to the good.",
        "scene": (
            "From behind at three-quarter angle: the farmer mid-stride and "
            "mid-fling, a fan of grain leaving his open hand and drifting "
            "down together over the edge of the pale path AND the dark good "
            "earth beside it in the same throw, his bearded face turned "
            "enough into the light to show it lifted and hopeful, following "
            "the seed. Warm morning light down the field. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b23", "out": "s23-that-is-how-generous-god.jpeg", "seg": "n11 + j2",
        "window": "122.35-128.12", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CROWD", "SHORE"],
        "narration": (
            "That is how generous God is with his word. Who hath ears to hear, "
            "let him hear."
        ),
        "must_show": "SCRIPTURE-EXACT: back to the boat — Jesus seated, both arms opened wide toward the whole shore and hillside of people, the invitation thrown as wide as the sower's seed.",
        "must_not_show": "no halo, glare or rim-light on Jesus; seated still; the wide-open arms mirror the sowing gesture.",
        "scene": (
            "From the water behind the boat's stern quarter: Jesus seated, "
            "both arms opened wide toward the land, taking in the whole "
            "crowded beach and the hillside above it in one embracing "
            "gesture — the same shape as a sower's throw. The hundreds of "
            "faces on the shore look back at him across the bright water. "
            "Mid-morning light, small clouds, the green-blue sea gently "
            "moving under the hull. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r024-b24", "out": "s24-a-hard-path-can-be.jpeg", "seg": "n12",
        "window": "130.40-134.48", "wide": True, "jesus": False, "ref": False,
        "locks": ["SOWER", "FIELD"],
        "narration": "A hard path can be broken up. Rocky soil can be cleared.",
        "must_show": "the farmer WORKING the bad ground — mattock swung into the packed path breaking its crust, and beside him a pile of stones already lifted out of the shallow corner.",
        "must_not_show": "no halo, glare or rim-light; real labour — the crust visibly breaking, the stone pile visibly grown.",
        "scene": (
            "In fresh morning light the farmer works the pale packed path "
            "with a heavy wooden-handled mattock, caught at the bottom of a "
            "swing with the blade bitten deep and a slab of the hard crust "
            "levering up dark and broken — and behind him at the rocky "
            "corner stands a knee-high pile of grey stones he has already "
            "carried out of the thin soil, the cleared patch beside it "
            "turned deep brown. Sweat darkens the back of his tunic. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r024-b25", "out": "s25-that-is-how-good-he.jpeg", "seg": "n12",
        "window": "134.48-140.40", "wide": True, "jesus": False, "ref": False,
        "locks": ["SOWER", "FIELD"],
        "narration": (
            "That is how good he is. He keeps sowing, and he never stops hoping "
            "your heart will be the good ground."
        ),
        "must_show": "the closing image — a NEW morning, the sower walking out again with the seed-bag refilled, beginning the fling over ground broken open and waiting.",
        "must_not_show": "no halo, glare or rim-light; the field shows the mended places — broken-open path, cleared corner — ready this time.",
        "scene": (
            "A new clear morning, low fresh light and long cool shadows: "
            "the farmer walks out onto the field once more with the canvas "
            "seed-bag full again at his chest, his arm just beginning the "
            "first wide throw of the day — and the ground ahead of him lies "
            "changed, the old path broken open into dark turned earth, the "
            "rocky corner cleared beside its stone pile, all of it soft and "
            "waiting. The far hills stand pale blue and the sky is washed "
            "clean. The camera looks up the field into the morning as he "
            "comes. Every figure has two arms, two hands and one head."
        ),
    },
]
