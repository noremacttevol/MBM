#!/usr/bin/env python3
"""V2 beat map — row 102, build-102-jacobs-ladder (Genesis 28:10-22).

COVERAGE: 28 pictures over 160.2 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Genesis 28 KJV):
  v10-11 Jacob flees Beersheba toward Haran; "the SUN WAS SET; and he
        took of the STONES of that place, and put them for his
        PILLOWS, and lay down."
  v12   the dream: "a LADDER set up on the EARTH, and the top of it
        reached to HEAVEN: and behold the ANGELS OF GOD ASCENDING AND
        DESCENDING on it." — traffic both ways, rooted in his ground.
  v13   "the LORD stood ABOVE it" — the embodied Father SHOWN standing
        in the opening of heaven at the summit (see GOD-rendering note).
  v13-14 the Abrahamic promise: the land, the seed "as the DUST OF
        THE EARTH."
  v15   "I AM WITH THEE, and will KEEP THEE in all places whither
        thou goest... I will NOT LEAVE THEE."
  v16-17 waking: "Surely the LORD is IN THIS PLACE; and I KNEW IT
        NOT... this is none other but the HOUSE OF GOD, and this is
        the GATE OF HEAVEN."
  v18-19 the pillow stone STOOD UP as a PILLAR, OIL poured on its
        top; the place named BETHEL.
  v20-22 he goes on his way — same road, changed man.

ANGEL RENDERING (CONTENT-CARE law): the ladder's angels are real,
plain-robed figures in PALE SILVER-GREY — NO wings, no rings of
light, nothing outlining bodies; they climb and descend on foot.

GOD IS EMBODIED HERE (Cameron's OPEN complaint, 2026-08-07: "0:24
looks like a UFO, no God coming to him in a dream" — REVERSES the
old "God is never embodied / light only" note that made the summit
read as a UFO disc). Genesis 28:13 is scripture-exact: "behold, the
LORD stood ABOVE it." So wherever the heaven-opening at the stair's
summit is in frame, the LORD is SHOWN as the same locked embodied
person (the GOD lock + god.jpeg face sheet, byte-identical to the
Father shown in build-113 — his look does not change), standing in
the opening above the stair. NEVER a UFO, disc, saucer, ring, orb,
craft, portal or metallic object; NEVER a shapeless blob of light and
NEVER a halo/glow/rim-light around him. The opening of heaven is a
natural break in the night sky filled with warm light, with the
standing Father in it. The Jacob-face close-ups (b08/b11/b13) keep
God off-frame — correct grammar, a reaction shot — but every summit
beat shows him. (Jehovah-vs-Father doctrine flag for Cameron in QC:
OT "LORD" may read as the premortal Christ; god.jpeg keeps one
consistent divine look per his standing order — non-blocking.)

TIME OF DAY ARC (intentional): sunset for the flight's end; deep
starry NIGHT for the camp; the DREAM in night lit by the stair's own
brilliance; waking in grey first light; the pillar and the road in
clean morning gold. Correct story lighting, not the row-11 defect.

CHANGING CONDITION (kept OUT of the locks): the stone — pillow, then
standing pillar, then oiled; the sky — sunset, stars, opened, closed,
dawn; Jacob — running, sleeping, dreaming, shaken, changed.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream (he does not appear in this row).
LOCKS = {
    "JACOB": (
        "JACOB LOCK: Jacob is the same man in every shot — about "
        "thirty, smooth-cheeked with only a short sparse dark beard, "
        "quick clever eyes now shadowed with fear, in a travel-worn "
        "DARK OCHRE-BROWN robe with a CHARCOAL head cloth (never "
        "cream, never white), carrying one thin traveller's staff "
        "and nothing else."
    ),
    "WASTE": (
        "WASTE LOCK: the stony camp country — a bare upland of "
        "scattered grey stones and thin scrub, low ridges all "
        "around, no tree, no wall, no light of any house anywhere. "
        "The same stones and ridges throughout."
    ),
    "STAIR": (
        "STAIR LOCK: the dream stairway — a GREAT STONE STAIRWAY "
        "rising from the camp's very ground, broad as a road, "
        "climbing in long flights up through the night air to a "
        "high OPENING IN HEAVEN — a natural break in the night sky "
        "filled with warm light (NEVER a UFO, disc, saucer, ring, "
        "orb, portal or metal craft); the same stair and opening in "
        "every dream shot."
    ),
    "ANGELS": (
        "ANGELS LOCK: the stair's angels — real human figures in "
        "plain PALE SILVER-GREY robes, walking UP and DOWN the "
        "stair's flights on foot — NO wings, no rings of light, "
        "nothing outlining any body; calm, strong, purposeful."
    ),
    "GOD": (
        "GOD THE FATHER LOCK (Cameron's standing order: God has a body "
        "and one locked look, like Jesus): the Father is the same "
        "glorified embodied man in every shot — majestic and ageless-"
        "strong, flowing white hair and a full white beard, a warm "
        "noble deeply kind face, in a robe of BRILLIANT PURE WHITE (he "
        "alone wears pure white; only Jesus wears cream). Real weight, "
        "real footsteps, radiant dignity WITHOUT any halo or light "
        "effects. His face is shown clearly and is never stern."
    ),
}

REF = True

# Per-story face sheets — identity carried by IMAGE, not wording (lesson 2/10).
# JACOB was previously unwired (prose-only), a cause of the row-102 beard drift
# in lesson 13; wiring jacob.jpeg holds his face across the row. GOD attaches
# god.jpeg (byte-identical to build-113's Father) on every beat whose locks name
# GOD, so his look does not change (Cameron's standing order).
REFS = {
    "JACOB": "CAST-REF-V2/jacob.jpeg",
    "GOD": "CAST-REF-V2/god.jpeg",
}

BEATS = [
    {
        "id": "v2-r102-b01", "out": "s01-jacob-was-running.jpeg", "seg": "n1",
        "window": "0.28-1.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE"],
        "narration": "Jacob was running.",
        "must_show": "the flight — Jacob alone at a hard traveling pace across the stony upland in late low light, glancing back over his shoulder; a man running FROM, not to.",
        "must_not_show": "no halo, glare or rim-light; the pace DESPERATE — nothing of the pilgrim in it yet.",
        "scene": (
            "One figure moves fast across "
            "the emptiness: Jacob at a "
            "hard scrambling pace over "
            "the scattered stones, staff "
            "swinging, robe hitched, one "
            "more backward glance thrown "
            "over his shoulder at the "
            "skyline behind — the stride "
            "of a man running FROM "
            "something, with no idea at "
            "all that he is also running "
            "TOWARD something, and that "
            "the second thing is waiting "
            "up ahead in the dark. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r102-b02", "out": "s02-when-the-sun-went-down.jpeg", "seg": "n2",
        "window": "10.37-12.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE"],
        "narration": "When the sun went down he was in the middle of nowhere.",
        "must_show": "the sun set on nowhere — the last red band dying on the ridge line, Jacob a small halted figure in the vast darkening stone country; night catching him in the open.",
        "must_not_show": "no halo, glare or rim-light; NOWHERE total — no light, roof or wall in any direction.",
        "scene": (
            "The sun goes down and takes "
            "the world's edges with it: "
            "the last red band dying "
            "along the western ridge, "
            "the stone country going "
            "blue-dark ridge by ridge, "
            "and in the middle of all "
            "that gathering nothing, one "
            "small halted figure turning "
            "a slow circle — no roof, no "
            "wall, no lamp of any house "
            "to any horizon — night "
            "closing over a runaway with "
            "nowhere left to run today. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r102-b03", "out": "s03-no-home-no-bed-no.jpeg", "seg": "n2",
        "window": "12.68-15.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE"],
        "narration": "No home, no bed, no welcome.",
        "must_show": "the inventory of nothing — close on Jacob at his stopping place in the dusk: empty hands, one staff, cold stones; homelessness itemised.",
        "must_not_show": "no halo, glare or rim-light; the poverty of the moment TOTAL — nothing softens the campsite.",
        "scene": (
            "Close on what the favourite "
            "son has left: two empty "
            "hands in the failing light, "
            "one thin staff leaned "
            "against a rock, the cold "
            "grey stones of nowhere for "
            "furniture — the boy who "
            "grew up smelling his "
            "mother's cooking through "
            "goat-hair walls taking "
            "inventory at dusk and "
            "arriving at three items: "
            "no home, no bed, no one "
            "anywhere glad he is coming. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r102-b04", "out": "s04-he-took-a-stone-put.jpeg", "seg": "n2",
        "window": "15.60-21.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE"],
        "narration": (
            "He took a stone, put it under his head for a pillow, and lay "
            "down in the dark to sleep."
        ),
        "must_show": "SCRIPTURE-EXACT: the stone pillow — Jacob settling his head onto the flat stone under the first stars, robe drawn over him; the hardest bed in Genesis.",
        "must_not_show": "no halo, glare or rim-light; the bed HONEST — stone and dirt and a tired man, nothing romanticized.",
        "scene": (
            "The bed is made in one "
            "motion: a flat stone dragged "
            "into place, the head cloth "
            "folded once across it, and "
            "Jacob lowering his cheek "
            "onto rock still warm from "
            "the dead sun — knees drawn "
            "up under the ochre robe, "
            "staff in reach, the first "
            "stars coming out hard and "
            "cold above a man whose "
            "pillow tonight is the "
            "planet itself — and sleep "
            "taking him anyway, because "
            "running is heavy work. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r102-b05", "out": "s05-and-there-in-the-last.jpeg", "seg": "n3",
        "window": "21.80-26.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE", "GOD"],
        "narration": (
            "And there, in the last place he would have expected it, God "
            "came to him in a dream."
        ),
        "must_show": "SCRIPTURE-EXACT: God came to him — the sleeping figure small under the immense starfield, and high above the little camp the night sky broken OPEN into an opening of heaven filled with warm light, and STANDING in that opening the embodied Father (per the GOD lock): a real man of radiant dignity in brilliant white, white hair and full white beard, looking down toward the sleeper — God visibly come to him.",
        "must_not_show": "NEVER a UFO, disc, saucer, ring, orb, portal, craft or metal object in the sky; no halo, glow or rim-light around the Father; nothing outlines his head; the opening a NATURAL break in the night sky, not a hovering machine.",
        "scene": (
            "Over the sleeping runaway "
            "the night breaks open: high "
            "above the little camp, among "
            "the hard cold stars, the "
            "sky parts into an opening of "
            "heaven filled with warm "
            "light — and standing IN that "
            "opening, looking down toward "
            "the stone where a cheat and "
            "fugitive lies dreaming, the "
            "Father himself, a real man "
            "of radiant dignity in "
            "brilliant white, white hair "
            "and a full white beard — God "
            "come, in person, to the last "
            "address in the world anyone "
            "would expect heaven to call "
            "on. The opening is a natural "
            "break in the night sky, never "
            "a disc or craft; no light "
            "rings his head. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r102-b06", "out": "s06-he-saw-a-great-stairway.jpeg", "seg": "n3",
        "window": "26.44-32.80", "wide": True, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE", "STAIR", "GOD"],
        "narration": (
            "He saw a great stairway rising from the very ground where he "
            "lay, all the way up into an opening in heaven."
        ),
        "must_show": "SCRIPTURE-EXACT: the ladder set up on the earth — the great stone stairway rooted beside the sleeper, climbing flight over flight into the high opening of heaven; at the top of it, standing in the opening, the embodied Father (per the GOD lock) small with distance but clearly a white-robed, white-bearded man; earth and heaven joined by the stair and by him.",
        "must_not_show": "NEVER a UFO, disc, saucer, ring or craft at the summit; no halo/glow/rim-light around the Father; the opening a natural break in the sky; the stair's FOOT in his campground dirt — the connection literal.",
        "scene": (
            "The dream stands, the camera at the camp's edge "
            "behind the sleeper's still form, the "
            "impossible up in the dark: "
            "a great stone stairway "
            "rooted in the campground "
            "dirt an arm's reach from "
            "the sleeper's stone — broad "
            "as a road, real as masonry "
            "— climbing flight over "
            "flight up through the night "
            "air, past the stars' level, "
            "into a high opening of "
            "heaven filled with warm "
            "light — and at the very top, "
            "standing in that opening, "
            "small with the distance but "
            "unmistakably a man in "
            "brilliant white with white "
            "hair and full white beard, "
            "the Father himself — the top "
            "of it in heaven and its "
            "bottom, deliberately, in the "
            "dust of exactly nowhere. The "
            "opening is a natural break in "
            "the night sky, never a disc "
            "or craft. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r102-b07", "out": "s07-and-on-it-the-angels.jpeg", "seg": "n4",
        "window": "33.38-41.08", "wide": True, "jesus": False, "ref": False,
        "locks": ["JACOB", "STAIR", "ANGELS"],
        "narration": (
            "And on it the angels of God were going up and coming down, "
            "moving between heaven and this lonely patch of dirt where a "
            "runaway lay sleeping."
        ),
        "must_show": "SCRIPTURE-EXACT: ascending AND descending — silver-grey figures walking the flights both directions, some near the ground, some high and small; working traffic, not pageant.",
        "must_not_show": "ABSOLUTE: no wings, no rings of light, no outlines; BOTH directions clearly happening.",
        "scene": (
            "And the stairway is BUSY, the camera off its flank "
            "so both travel directions read in profile: "
            "plain silver-grey figures "
            "walking its flights in both "
            "directions — two descending "
            "past three climbing, one "
            "nearly to the brilliant "
            "opening, another stepping "
            "off the lowest stair onto "
            "the campground dirt itself — "
            "unhurried working traffic, "
            "errands running day and "
            "night between heaven and a "
            "patch of stones where a "
            "runaway sleeps — the "
            "commute of the universe, "
            "routed through nowhere. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r102-b08", "out": "s08-heaven-was-not-far-off.jpeg", "seg": "n4",
        "window": "41.08-42.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "STAIR"],
        "narration": "Heaven was not far off.",
        "must_show": "the nearness — the stair's lowest steps close beside the sleeping face: heaven's road beginning within touching distance of his stone pillow.",
        "must_not_show": "ABSOLUTE: no figure in frame's brilliance; the LOWEST step the subject — near enough to touch.",
        "scene": (
            "Close on the correction of "
            "every map: the stairway's "
            "lowest step planted in the "
            "dirt scarcely an arm's "
            "reach from the sleeping "
            "face on its stone — worn "
            "campground gravel meeting "
            "the first stair of heaven "
            "with no gap, no border, no "
            "distance at all — the far "
            "country turning out to "
            "begin exactly where the "
            "runaway's breath stirs the "
            "dust. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r102-b09", "out": "s09-i-am-the-lord-god.jpeg", "seg": "jv13",
        "window": "45.53-57.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "STAIR", "GOD"],
        "narration": (
            "I am the LORD God of Abraham thy father, and the God of Isaac: "
            "the land whereon thou liest, to thee will I give it, and to thy "
            "seed."
        ),
        "must_show": "SCRIPTURE-EXACT (Genesis 28:13, 'the LORD stood above it'): the LORD above the stair — the embodied Father (per the GOD lock) standing at the summit in the opening of heaven, a real white-robed white-bearded man of radiant dignity, looking down and speaking toward the sleeper below; the stair descending from his feet to the campground.",
        "must_not_show": "NEVER light-only, no shapeless brilliance standing in for him — he is a SHOWN embodied person; NEVER a UFO, disc, ring or craft; no halo/glow/rim-light around him.",
        "scene": (
            "From the summit opening the "
            "Father himself speaks: he "
            "stands ABOVE the stair in "
            "the opening of heaven — a "
            "real man of radiant dignity "
            "in brilliant white, white "
            "hair and full white beard, "
            "looking down the long "
            "flights toward the sleeping "
            "runaway — I AM THE LORD GOD "
            "OF ABRAHAM THY FATHER — his "
            "words carrying down the "
            "stair, deeding the very dirt "
            "under the runaway's back to "
            "him and to seed he cannot "
            "imagine. No light rings his "
            "head; the opening is a "
            "natural break in the night "
            "sky, never a disc or craft. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r102-b10", "out": "s10-he-had-lied-to-his.jpeg", "seg": "n1",
        "window": "1.17-9.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB"],
        "narration": (
            "He had lied to his blind father and cheated his own brother, "
            "and now he was fleeing for his life, alone, with everything he "
            "knew behind him."
        ),
        "must_show": "the guilt carried — close on the fleeing face: fear and shame ridden together; a man who knows exactly why he is running.",
        "must_not_show": "no halo, glare or rim-light; the guilt HONEST — no villain's face, a man ashamed.",
        "scene": (
            "Close on the face of a man "
            "who cannot outrun the "
            "reason: the quick clever "
            "eyes shadowed and darting, "
            "shame riding fear riding "
            "exhaustion — his father's "
            "blind trusting hands still "
            "on his skin, his brother's "
            "roar still in his ears — "
            "everything he knew behind "
            "him by his own doing, and "
            "the road ahead owing him "
            "exactly nothing. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r102-b11", "out": "s11-god-did-not-scold-him.jpeg", "seg": "n5",
        "window": "59.18-61.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "STAIR"],
        "narration": "God did not scold him for what he had done.",
        "must_show": "the no-scolding — the sleeping dreamer's face under the stair's warm light: peace on features that braced for wrath; mercy's tone rendered in light.",
        "must_not_show": "ABSOLUTE: no figure in the light; the face UNCLENCHING in sleep — the ledger never read.",
        "scene": (
            "Close on the face in the "
            "stairlight, and what is NOT "
            "arriving on it: no recital "
            "of the stolen blessing, no "
            "accounting of the lie in "
            "the dark tent, no wrath "
            "descending any flight of "
            "the shining stairs — the "
            "sleeping features slowly "
            "unclenching instead, the "
            "shame-knots loosening one "
            "by one under a light that "
            "reads like the opposite of "
            "a sentence — a guilty man "
            "braced for court, receiving "
            "welcome. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r102-b12", "out": "s12-he-stood-above-the-stairway.jpeg", "seg": "n5",
        "window": "61.27-67.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["STAIR", "JACOB", "GOD"],
        "narration": (
            "He stood above the stairway and made him a promise — the same "
            "promise he had made to his grandfather Abraham."
        ),
        "must_show": "SCRIPTURE-EXACT: he STOOD above the stairway — the embodied Father (per the GOD lock) standing at the stair's crown in the opening of heaven, a white-robed white-bearded man, the covenant spoken down the flights over the sleeper; the walkers paused on the steps.",
        "must_not_show": "NEVER light-only in place of him — he is SHOWN standing above; NEVER a UFO, disc or craft; no halo/glow/rim-light around him.",
        "scene": (
            "The whole dream holds still "
            "for the covenant: the great "
            "stair climbing flight over "
            "flight to its crown, and "
            "standing there above it in "
            "the opening of heaven the "
            "Father himself — a real man "
            "in brilliant white, white "
            "hair and full white beard — "
            "the silver-grey "
            "walkers pausing on the "
            "steps mid-errand, and down "
            "from him the "
            "old promise descending "
            "word by word — Abraham's "
            "promise, his grandfather's "
            "inheritance, re-spoken "
            "whole over a runaway on a "
            "stone — the family deed "
            "read aloud from above the "
            "top stair by the light "
            "that owns the house. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r102-b13", "out": "s13-this-wanderer-with-nothing-would.jpeg", "seg": "n5",
        "window": "67.34-72.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE"],
        "narration": (
            "This wanderer with nothing would become a family as many as "
            "the dust of the earth."
        ),
        "must_show": "the dust promise — close on the campground dust beside the sleeper, stirred and drifting in the stairlight: numberless grains, the family's census.",
        "must_not_show": "ABSOLUTE: no figure; the dust ITSELF the image — countless motes catching the light.",
        "scene": (
            "Close on the census of the "
            "promise: the campground "
            "dust beside his sleeping "
            "hand, stirred by the "
            "night's small wind and "
            "drifting through the "
            "stairlight in numberless "
            "shining grains — every mote "
            "a life, every drift a "
            "generation — the family of "
            "a man who tonight owns one "
            "staff and one stone, "
            "counted out for him in the "
            "only arithmetic big enough: "
            "the dust of the earth, "
            "which no one has ever "
            "finished counting. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r102-b14", "out": "s14-it-was-open-right-above.jpeg", "seg": "n4",
        "window": "42.97-44.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "STAIR", "GOD"],
        "narration": "It was open, right above him.",
        "must_show": "the opening overhead — from low beside the sleeper looking straight up the stair's flights to the opening of heaven directly above the camp, and standing in that opening at the top the embodied Father (per the GOD lock), small with the height but a clear white-robed white-bearded man; vertical truth, heaven open and the LORD in it.",
        "must_not_show": "NEVER a UFO, disc, ring or craft overhead; no halo/glow/rim-light around the Father; the opening a natural break in the sky; the vertical alignment EXACT — opening, stair, sleeper in one plumb line.",
        "scene": (
            "The frame lies down beside "
            "him and looks straight up: "
            "the stair's flights "
            "telescoping away overhead, "
            "rail over rail of climbing "
            "stone, silver walkers "
            "small and smaller on them — "
            "and at the very top, "
            "plumb-line true above the "
            "runaway's stone pillow, "
            "the opening of heaven "
            "standing open, and in it "
            "the Father himself, small "
            "with the height but a real "
            "man in brilliant white with "
            "white hair and full white "
            "beard, directly "
            "over the one spot on earth "
            "he chose because it was "
            "nowhere. The opening is a "
            "natural break in the sky, "
            "never a disc or craft; no "
            "light rings his head. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r102-b15", "out": "s15-and-behold-i-am-with.jpeg", "seg": "jv15",
        "window": "72.66-88.77", "wide": True, "jesus": False, "ref": False,
        "locks": ["JACOB", "STAIR", "WASTE", "GOD"],
        "narration": (
            "And, behold, I am with thee, and will keep thee in all places "
            "whither thou goest, and will bring thee again into this land; "
            "for I will not leave thee, until I have done that which I have "
            "spoken to thee of."
        ),
        "must_show": "SCRIPTURE-EXACT: the with-thee promise — the whole night scene held gently: sleeper, stone, stair, and at the stair's crown in the opening of heaven the embodied Father (per the GOD lock) standing and speaking down over all of it; the promise covering everything the frame holds.",
        "must_not_show": "NEVER light-only in place of the Father — he is SHOWN standing at the summit; NEVER a UFO, disc or craft; no halo/glow/rim-light around him.",
        "scene": (
            "The promise settles, the camera far off taking "
            "sleeper, stone and stair from the side, over the "
            "whole night like a second "
            "sky: the sleeping man on "
            "his stone, the staff, the "
            "cold scattered rocks of "
            "nowhere, the great stair "
            "with its patient walkers, "
            "and at its crown in the "
            "opening of heaven the "
            "Father himself standing — a "
            "real man in brilliant white, "
            "white hair and full white "
            "beard — speaking down over "
            "it all: "
            "I AM WITH THEE — IN ALL "
            "PLACES — I WILL NOT LEAVE "
            "THEE — words wide enough "
            "to roof every road the "
            "runaway will ever take, "
            "spoken over him while he "
            "is too asleep to earn or "
            "doubt them. The opening is a "
            "natural break in the sky, "
            "never a disc or craft. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r102-b16", "out": "s16-i-am-with-thee.jpeg", "seg": "n6",
        "window": "90.23-91.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB"],
        "narration": "I am with thee.",
        "must_show": "the first clause held — extreme close on the sleeping face bathed in the warm stairlight: WITH, made visible as nearness of light on skin.",
        "must_not_show": "ABSOLUTE: no figure; the light's NEARNESS the whole image.",
        "scene": (
            "Extreme close on three "
            "words made light: the "
            "sleeping face on its stone, "
            "and the stair's warm "
            "brightness lying against "
            "the skin of it — on the "
            "closed lids, in the sparse "
            "young beard, along the "
            "worry-lines gone slack — "
            "nearness itself, resting on "
            "him the way a hand rests — "
            "WITH THEE, spelled in "
            "light on the face of a "
            "man who fell asleep "
            "certain he was alone. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r102-b17", "out": "s17-i-will-keep-thee.jpeg", "seg": "n6",
        "window": "91.06-92.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE"],
        "narration": "I will keep thee.",
        "must_show": "the keeping — the camp seen guarded: the sleeper small and safe at the stair's foot, the vast dangerous dark held OFF all around the lit ground.",
        "must_not_show": "ABSOLUTE: no figure; the safety SPATIAL — lit ground, held-back dark.",
        "scene": (
            "The second clause draws a "
            "boundary: the little camp "
            "lying lit and quiet at the "
            "stair's foot — sleeper, "
            "stone, staff inside a "
            "circle of warm ground — "
            "and all around it the "
            "upland's enormous dangerous "
            "dark standing exactly "
            "where it is, held off like "
            "tide against a sea-wall — "
            "KEPT, drawn on the night "
            "in the oldest way: a "
            "guarded brightness with a "
            "man asleep in the middle "
            "of it. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r102-b18", "out": "s18-to-a-man-who-had.jpeg", "seg": "n6",
        "window": "93.64-103.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "STAIR", "WASTE"],
        "narration": (
            "To a man who had just thrown his whole life away and run, God "
            "promised to go with him, everywhere, and never let go. He had "
            "done nothing to earn it."
        ),
        "must_show": "grace's shape — the whole scene once more: the unworthy sleeper under the open heaven; the unearned-ness carried by everything visible about him.",
        "must_not_show": "ABSOLUTE: no figure in the light; his POVERTY plain in frame — stone pillow, single staff, nothing else.",
        "scene": (
            "The frame audits the "
            "recipient one more time: a "
            "liar asleep on a rock, "
            "assets one staff, prospects "
            "none, references his "
            "furious brother — and over "
            "this exact man, heaven "
            "standing open with its "
            "stair run down to his "
            "dirt and its promise "
            "signed EVERYWHERE and "
            "NEVER — grace shaped the "
            "way it always is: "
            "magnificent, specific, and "
            "aimed at someone who "
            "earned none of it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r102-b19", "out": "s19-surely-the-lord-is-in.jpeg", "seg": "s16",
        "window": "104.30-109.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE"],
        "narration": (
            "Surely the LORD is in this place; and I knew it not. How "
            "dreadful is this place!"
        ),
        "must_show": "SCRIPTURE-EXACT: the waking words — Jacob bolt upright on his stone in grey first light, hand pressed to his chest, the awe wild in his face; the ordinary stones around him re-seen.",
        "must_not_show": "no stair or brilliance now — the plain grey morning waste; the holiness carried in HIS shaken face.",
        "scene": (
            "He wakes like a man surfacing "
            "from deep water: bolt "
            "upright on the stone in the "
            "grey first light, hand "
            "pressed hard to his "
            "hammering chest, wild eyes "
            "sweeping the ordinary "
            "stones and thin scrub of "
            "the most unremarkable "
            "campsite in the world — "
            "SURELY THE LORD IS IN THIS "
            "PLACE — AND I KNEW IT NOT — "
            "the same dirt as last "
            "night, and never the same "
            "dirt again. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r102-b20", "out": "s20-this-is-none-other-but.jpeg", "seg": "s16",
        "window": "109.60-113.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE"],
        "narration": (
            "this is none other but the house of God, and this is the gate "
            "of heaven."
        ),
        "must_show": "SCRIPTURE-EXACT: the naming — Jacob on his feet turning in the grey-gold dawn, arms half-raised at the empty holy ground: HOUSE OF GOD, GATE OF HEAVEN, said over bare stones.",
        "must_not_show": "no stair visible — the gate invisible now and believed anyway; his awe reverent, not fearful-cowering.",
        "scene": (
            "On his feet in the first "
            "gold-grey he turns a slow "
            "full circle with his arms "
            "half-raised, naming what "
            "only he can see: bare "
            "stones, thin scrub, empty "
            "sky — THE HOUSE OF GOD — "
            "the very air over the "
            "campground consecrated by "
            "what stood in it — THIS IS "
            "THE GATE OF HEAVEN — a "
            "man reading the invisible "
            "address off a patch of "
            "nowhere, and correct. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r102-b21", "out": "s21-jacob-woke-with-a-start.jpeg", "seg": "n7",
        "window": "115.44-120.74", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB"],
        "narration": (
            "Jacob woke with a start, shaken to his core. This is nothing "
            "less than the house of God."
        ),
        "must_show": "the shaken core — close on the waking face: sleep torn away, the dream's size still all over the features; a man changed while unconscious.",
        "must_not_show": "no halo, glare or rim-light; the shaking AWE, not terror-panic.",
        "scene": (
            "Close on a face the dream "
            "would not release: sleep "
            "torn off it in one gasp, "
            "the eyes enormous with "
            "something still filling "
            "them from the inside, "
            "breath ragged, the sparse "
            "beard trembling — not "
            "fear's shaking but the "
            "deeper kind, the tremor of "
            "a man who has been "
            "somewhere while lying "
            "still and come back "
            "resized — changed in his "
            "sleep, and knowing it. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r102-b22", "out": "s22-this-is-the-gate-of.jpeg", "seg": "n7",
        "window": "120.74-124.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE"],
        "narration": "This is the gate of heaven — and I nearly slept through it.",
        "must_show": "the near-miss — Jacob looking down at his own stone pillow in the dawn light, wonder and rue together: the gate he almost snored past.",
        "must_not_show": "no halo, glare or rim-light; the rue GENTLE — half a laugh in the awe.",
        "scene": (
            "He looks down at his own "
            "bed and almost laughs: the "
            "flat grey stone, dented "
            "dirt where his hip lay, "
            "the ordinary pillow of an "
            "ordinary desperate night — "
            "at the foot of heaven's "
            "own gate — the wonder on "
            "his face shot through with "
            "rue: he chose this spot "
            "for nothing, slept on the "
            "doorstep of the universe, "
            "and but for a dream would "
            "have risen and walked off "
            "none the wiser. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r102-b23", "out": "s23-so-he-took-the-stone.jpeg", "seg": "n8",
        "window": "125.17-132.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE"],
        "narration": (
            "So he took the stone that had been his pillow and stood it up "
            "on end as a pillar, a marker of the place where heaven had "
            "opened over him."
        ),
        "must_show": "SCRIPTURE-EXACT: the pillar raised — Jacob heaving the pillow stone upright on its end in the morning gold, bracing it with smaller stones; the first monument.",
        "must_not_show": "no halo, glare or rim-light; the work REAL — effort in the lifting, the stone plainly the same pillow stone.",
        "scene": (
            "The pillow becomes the "
            "monument: Jacob heaving the "
            "flat stone up on its end "
            "in the morning gold — back "
            "straining, breath loud, "
            "smaller rocks kicked into "
            "place around its base to "
            "brace it — until the thing "
            "his head slept on stands "
            "upright against the "
            "sunrise like a finger "
            "marking a page: HERE — the "
            "first altar of a man who "
            "woke up owning a "
            "before-and-after. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r102-b24", "out": "s24-and-he-poured-oil-over.jpeg", "seg": "n8b",
        "window": "133.17-140.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE"],
        "narration": (
            "And he poured oil over the top of it to set it apart as holy, "
            "and he called that place Bethel — the house of God."
        ),
        "must_show": "SCRIPTURE-EXACT: the anointing — close on the oil arcing from his travel flask over the standing stone's crown, running bright down its faces in the morning sun; BETHEL named.",
        "must_not_show": "no halo, glare or rim-light; the oil the trail-flask's LITTLE — a poor man's whole libation.",
        "scene": (
            "Close on the consecration: "
            "the last of his travel "
            "flask's oil arcing thin and "
            "bright over the standing "
            "stone's crown, running down "
            "the grey faces in shining "
            "threads that catch the "
            "morning sun — a poor man's "
            "whole libation, poured to "
            "the drop — and his lips "
            "moving over the new name "
            "as the oil finds every "
            "crack: BETHEL — house of "
            "God — an address given to "
            "nowhere, forever. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r102-b25", "out": "s25-i-will-not-leave-thee.jpeg", "seg": "n6",
        "window": "92.13-93.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB"],
        "narration": "I will not leave thee.",
        "must_show": "the third clause — the sleeping hand open beside the stone in the stairlight, the light lying IN the palm; the not-leaving as light that stays.",
        "must_not_show": "ABSOLUTE: no figure; the image SMALL and total — an open hand, held light.",
        "scene": (
            "Extreme close on the "
            "promise's third clause: the "
            "runaway's open hand lying "
            "palm-up in the dirt beside "
            "his stone, and the stair's "
            "warm light resting IN it — "
            "pooled in the palm's cup "
            "like water that refuses to "
            "drain — NOT LEAVE THEE — "
            "the whole covenant scaled "
            "down to one sleeping hand "
            "that cannot close on "
            "anything, being held "
            "anyway. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r102-b26", "out": "s26-then-he-went-on-his.jpeg", "seg": "n9",
        "window": "141.13-147.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB", "WASTE"],
        "narration": (
            "Then he went on his way — the same road, the same troubles "
            "waiting ahead, but a different man."
        ),
        "must_show": "the same road, changed — Jacob walking on east in the clean morning, the oiled pillar behind him; the stride remade: upright, unhunted.",
        "must_not_show": "no halo, glare or rim-light; the CHANGE in the walk — compare b01's flight: no backward glance now.",
        "scene": (
            "The same road takes a "
            "different man: Jacob "
            "walking east into the "
            "clean morning with the "
            "oiled pillar shrinking "
            "behind him — the staff "
            "swinging easy now, the "
            "spine straight, and not "
            "one backward glance over "
            "either shoulder — the "
            "same stones, the same "
            "uncle's tricks and "
            "brother's anger waiting "
            "in the far country ahead, "
            "and a traveller walking "
            "toward all of it like a "
            "man with company. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r102-b27", "out": "s27-not-because-he-had-fixed.jpeg", "seg": "n9",
        "window": "147.40-153.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["JACOB"],
        "narration": (
            "Not because he had fixed himself, but because he finally knew "
            "he was not walking alone."
        ),
        "must_show": "the unfixed, accompanied man — close on Jacob's walking face in morning light: the old flaws still there, and over them a settled unafraid peace.",
        "must_not_show": "no halo, glare or rim-light; NO transformation-glamour — same flawed face, new peace.",
        "scene": (
            "Close on the honest miracle: "
            "the same face — the quick "
            "scheming eyes not one "
            "shade purer, the flaws all "
            "present and accounted for, "
            "a heel's face still — and "
            "over it, settled like "
            "morning light on old "
            "stone, a peace that has "
            "nothing to do with being "
            "fixed and everything to do "
            "with being accompanied: "
            "the look of a man who "
            "knows, now, who else is on "
            "the road. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r102-b28", "out": "s28-that-is-how-god-still.jpeg", "seg": "n9",
        "window": "153.16-159.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["WASTE"],
        "narration": (
            "That is how God still meets people: not at their best, but "
            "wherever they happen to lie down in the dark."
        ),
        "must_show": "the closing image — the empty campsite in full morning: the oiled standing pillar alone among the stones, the road running on past it; the meeting place, marked and open.",
        "must_not_show": "no halo, glare or rim-light; the frame PEOPLE-EMPTY — the pillar and the road carrying the meaning for whoever comes next.",
        "scene": (
            "The closing frame keeps the "
            "place after its man has "
            "gone: the anointed stone "
            "standing alone among the "
            "scattered grey rocks in "
            "full morning light, oil "
            "still dark down its faces, "
            "the road running past it "
            "east and west toward "
            "everyone who has ever run "
            "out of daylight in the "
            "middle of nowhere — a "
            "marker left standing at "
            "the spot where the bottom "
            "turned out to be a "
            "doorstep. Every figure "
            "has two arms, two hands "
            "and one head."
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
