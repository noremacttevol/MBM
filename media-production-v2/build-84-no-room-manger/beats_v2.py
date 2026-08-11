#!/usr/bin/env python3
"""V2 beat map — row 84, build-84-no-room-manger (Luke 2:1-7).

COVERAGE: 34 pictures over 191.0 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 2:1-7 KJV):
  v1    "a decree from CAESAR AUGUSTUS, that all the world should be
        taxed" — an imperial order, issued far away, reaching Nazareth.
  v4    "Joseph also went up from Galilee, out of the city of NAZARETH
        ... unto the city of David, which is called BETHLEHEM" — ~90
        miles of hill country, on foot and by donkey.
  v5    "with MARY his espoused wife, being GREAT WITH CHILD."
  v7    "she brought forth her firstborn son, and WRAPPED HIM IN
        SWADDLING CLOTHES, and LAID HIM IN A MANGER; because there was
        NO ROOM for them in the inn." — the manger a wooden
        feed-trough; the shelter a rough stable (rendered here as the
        traditional limestone cave-stable).

JESUS FLAG NOTE: the child in this row is a NEWBORN — the adult JESUS
LOCK v4 face and jesus-v2-face.jpeg ref do NOT apply; every beat runs
jesus=False and the baby is painted per scene (swaddled infant, face
peaceful, no halo).

TIME OF DAY ARC (intentional): the decree and journey beats in
daylight; arrival at Bethlehem at DUSK; the door-search in lamplit
NIGHT; the birth and everything after in DEEP NIGHT — the stable lit
by one small clay lamp and bright starlight through the door, one
brilliant star high over the town. Correct story darkness, not the
row-11 defect.

CONTENT-CARE: no flags. Birth itself never depicted — the row cuts
from the shelter to the already-swaddled child; Mary post-birth is
serene and modest, exhaustion dignified. "Heaven filled with light"
(b31) is rendered as the brilliant star and deep starfield only — NO
angels (narration does not demand them), no halos on anyone.

CHANGING CONDITION (kept OUT of the locks): Mary's condition — great
with child on the road, then delivered, cradling the newborn; the
light — day, dusk, lamplit night, deep night; the manger — empty
straw, then holding the child.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream (and the adult Jesus does not appear in this row).
LOCKS = {
    "MARY": (
        "MARY LOCK: Mary is the same young woman in every shot — "
        "about eighteen, a gentle open face with warm brown eyes, "
        "dark hair under a DEEP INDIGO-BLUE veil, a plain DEEP "
        "INDIGO-BLUE dress (never cream, never white). Weary, "
        "serene, and dignified in every frame."
    ),
    "JOSEPH": (
        "JOSEPH LOCK: Joseph is the same man in every shot — about "
        "thirty, a carpenter's broad hands, short dark beard, "
        "sun-browned face, in a DARK RUSSET-BROWN robe with a "
        "CHARCOAL-GREY head cloth (never cream, never white). "
        "Steady, protective, tired."
    ),
    "STABLE": (
        "STABLE LOCK: the stable is a rough LIMESTONE CAVE at the "
        "town's edge — uneven rock walls, clean straw on the floor, "
        "a WOODEN FEED-TROUGH manger on legs, a patient OX and a "
        "grey DONKEY tethered at the wall, one small clay oil lamp, "
        "and the door opening to the deep starry night. The same "
        "cave, trough and animals throughout."
    ),
    "TOWN": (
        "TOWN LOCK: Bethlehem — a small limestone hill town packed "
        "for the census: narrow stepped lanes, flat-roofed houses "
        "crowded together, warm lamplight in low doorways and "
        "windows. The same lanes and rooflines throughout."
    ),
}

REF = True

# TEXT_OVERRIDES (QC-FIX 2026-08-11): the V1 make_narration script was tightened
# AFTER the ElevenLabs voices were cut, so extract_beats' caption text for n1/n6/n7
# no longer matches the shipped mp3s (transcription-confirmed). Caption the words
# that are GENUINELY SPOKEN (audio byte-identical; V1 never edited).
TEXT_OVERRIDES = {
    "n1": 'In those days a decree went out from Caesar Augustus, the emperor in far-off Rome, that the whole known world should be counted and taxed. And so every family in the land had to pack up and travel to the town their ancestors came from, to be registered.',
    "n6": 'And there, in the quiet, with no midwife and no crowd, Mary gave birth to her first son. She wrapped him tightly in strips of cloth, the way every mother there wrapped a newborn, and she looked into the face of God. Luke tells it in one sentence, and he does not raise his voice for any of it:',
    "n7": "She had her first son, wrapped him up, and laid him in a feed trough, because there was no room for them anywhere else. Read that again slowly. The one who made the stars had nowhere to lay his head the very night he arrived. The hands that shaped the mountains were small enough to curl around a mother's finger. He did not come down halfway. He came all the way down, to the bottom, to the people the world had no space for.",
}

BEATS = [
    {
        "id": "v2-r084-b01", "out": "s01-and-it-came-to-pass.jpeg", "seg": "sv1",
        "window": "0.000-7.992", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "And it came to pass in those days, that there went out a decree "
            "from Caesar Augustus, that all the world should be taxed."
        ),
        "must_show": "SCRIPTURE-EXACT: the decree — a Roman clerk's hall in hard daylight: officials sealing and stacking scrolls, couriers taking them out; an empire's paperwork setting the world in motion.",
        "must_not_show": "no halo, glare or rim-light; no emperor's face needed — the DECREE itself is the actor: scrolls, seals, couriers.",
        "scene": (
            "In a marble-cool imperial hall, the camera behind the "
            "waiting petitioners' shoulders, the "
            "decree goes out into the world: "
            "clerks at long tables pressing "
            "seals into wax, scroll after "
            "scroll stacked and bound, couriers "
            "in dark travel cloaks taking their "
            "satchels and striding for the "
            "bright doorway — the whole "
            "machinery of an empire counting "
            "its people, one order copying "
            "itself outward toward every "
            "village it has never heard of. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b02", "out": "s02-and-his-mother-and-the.jpeg", "seg": "n8",
        "window": "143.995-148.359", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "MARY", "JOSEPH"],
        "narration": (
            "And his mother and the man who would raise him knelt in the "
            "straw and simply looked at him."
        ),
        "must_show": "the beholding — Mary and Joseph kneeling in the straw on either side of the manger, both faces bent to the swaddled newborn in the small lamp's light; nothing else asked of the moment.",
        "must_not_show": "no halo on the child or anyone; the looking UNHURRIED — two exhausted people doing nothing but seeing him.",
        "scene": (
            "In the small lamp's warm light "
            "the two of them kneel in the "
            "straw on either side of the "
            "wooden trough — Mary's tired face "
            "and Joseph's rough one bent close "
            "over the swaddled child sleeping "
            "between them — doing the only "
            "thing the moment asks: looking, "
            "and going on looking, while the "
            "ox breathes slow in the dark "
            "behind them and the night stands "
            "still around the three of them. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b03", "out": "s03-a-command-issued-in-a.jpeg", "seg": "n1",
        "window": "7.992-23.929", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "MARY"],
        "narration": (
            "A command issued in a distant palace reached all the way into "
            "two ordinary lives in Nazareth."
        ),
        "must_show": "the reach — Nazareth: a herald reading the census order in the little market square, and among the listeners Joseph and the expectant Mary hearing their lives change.",
        "must_not_show": "no halo, glare or rim-light; the couple ORDINARY in the crowd — the decree finding them, not framing them.",
        "scene": (
            "In Nazareth's small dusty square "
            "a herald reads the order from his "
            "unrolled scroll — every family, "
            "to its own city, to be counted — "
            "and among the gathered villagers "
            "the words find their mark: Joseph "
            "listening with his carpenter's "
            "hands going still, Mary beside "
            "him great with child, one palm "
            "coming to rest on the curve of "
            "her belly as a palace a world "
            "away rearranges their winter. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b04", "out": "s04-for-a-young-woman-named.jpeg", "seg": "n2",
        "window": "23.929-30.271", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY", "JOSEPH"],
        "narration": (
            "For a young woman named Mary and a carpenter named Joseph, that "
            "meant a long, hard road."
        ),
        "must_show": "the setting out — the two leaving Nazareth at morning: Mary settled on the grey donkey, Joseph leading it, the hill road unrolling south ahead of them.",
        "must_not_show": "no halo, glare or rim-light; the leave-taking PLAIN — a poor couple's minimal packing, one donkey, one road.",
        "scene": (
            "At the village's edge in the "
            "morning light the journey begins "
            "plainly: Mary settled sideways on "
            "the grey donkey with a rolled "
            "blanket behind her, Joseph at the "
            "halter with his few tools and "
            "their bread in one shoulder bag — "
            "and past them the hill road "
            "unrolls south, ridge behind "
            "ridge into the haze, every mile "
            "of it to be earned on foot and "
            "hoof. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r084-b05", "out": "s05-ninety-miles-of-hill-country.jpeg", "seg": "n2",
        "window": "30.271-38.433", "wide": True, "jesus": False, "ref": False,
        "locks": ["MARY", "JOSEPH"],
        "narration": (
            "Ninety miles of hill country, on foot and by donkey, from "
            "Nazareth down to Bethlehem, the town of King David."
        ),
        "must_show": "the distance — the tiny travelling pair on a switchback road through big empty hill country; scale doing the talking: two small figures, ninety long miles.",
        "must_not_show": "no halo, glare or rim-light; the country VAST and the figures small — effort measured in landscape.",
        "scene": (
            "The wide frame gives the journey its true size, the "
            "camera far across the valley taking the switchback in "
            "profile: "
            "its true size: dry Judean hill "
            "country ridged to the horizon "
            "under the travelling sun, the "
            "pale road switchbacking down "
            "through it — and small upon it, "
            "halfway down one long grade, the "
            "donkey and the walking man and "
            "the wrapped young woman, three "
            "little figures working their way "
            "through a landscape that hands "
            "out its miles one at a time. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b06", "out": "s06-and-mary-was-not-travelling.jpeg", "seg": "n2",
        "window": "38.433-40.770", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": "And Mary was not travelling light.",
        "must_show": "her burden — close on Mary on the donkey: great with child, one hand steadying her belly at a jolt, weariness carried with grace.",
        "must_not_show": "no halo, glare or rim-light; the weariness DIGNIFIED — discomfort real, complaint absent.",
        "scene": (
            "Close on Mary as the donkey "
            "takes a stony step: her hand "
            "moving to the round fullness "
            "under the indigo dress, her eyes "
            "closing one slow moment against "
            "the jolt, the road's dust pale "
            "on the hem of her veil — a "
            "young woman carrying the "
            "heaviest and most patient cargo "
            "on that whole imperial highway, "
            "mile after mile, without a word. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b07", "out": "s07-when-they-finally-reached-bethlehem.jpeg", "seg": "n3",
        "window": "43.329-46.893", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN", "MARY", "JOSEPH"],
        "narration": "When they finally reached Bethlehem, the little town was bursting.",
        "must_show": "the arrival at dusk — the couple and donkey at the town's edge: lanes jammed with census travellers, loaded animals, luggage in doorways; a small town over capacity.",
        "must_not_show": "no halo, glare or rim-light; the crowding FESTIVE-CHAOTIC, not hostile — too many relatives, not enemies.",
        "scene": (
            "At dusk the little town takes "
            "them in at the eyes only: from "
            "the road's rise Joseph and the "
            "donkey-borne Mary look down "
            "lanes jammed wall to wall — "
            "census families unloading "
            "bundles, tethered animals at "
            "every post, children asleep on "
            "luggage in doorways, lamplight "
            "and cooking smoke crowding out "
            "of every low window — Bethlehem "
            "bursting at its small seams with "
            "everyone who ever came from it. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b08", "out": "s08-everyone-with-roots-there-had.jpeg", "seg": "n3",
        "window": "46.893-55.246", "wide": True, "jesus": False, "ref": False,
        "locks": ["TOWN"],
        "narration": (
            "Everyone with roots there had come back for the same count, and "
            "every house, every spare room, every corner was already taken."
        ),
        "must_show": "the fullness itemised — down a lamplit lane: bedrolls on a roof, a family camped under a stair, guests packed visible through a window; every corner spoken for.",
        "must_not_show": "no halo, glare or rim-light; the occupancy TOTAL — no visible empty space anywhere the eye lands.",
        "scene": (
            "The lamplit lane itemises its own fullness, the "
            "camera at the lane's side so the campers read in "
            "profile: "
            "fullness: bedrolls laid out along "
            "a flat roof's parapet, a family "
            "of five camped in the triangle "
            "under an outdoor stair, a window "
            "showing a room packed shoulder "
            "to shoulder with relatives at "
            "supper, even the well's ledge "
            "claimed by a sleeping traveller "
            "— David's town counted to the "
            "rafters, every corner of it "
            "already someone's for the night. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b09", "out": "s09-there-was-simply-nowhere-left.jpeg", "seg": "n3",
        "window": "55.246-57.584", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN", "MARY", "JOSEPH"],
        "narration": "There was simply nowhere left.",
        "must_show": "the fact landing — the couple paused in the lane between full doorways: Joseph's tired scan of the packed houses, Mary heavy on the donkey; nowhere, visibly true.",
        "must_not_show": "no halo, glare or rim-light; NO villain in frame — just fullness and two tired faces doing the arithmetic.",
        "scene": (
            "In the middle of the packed lane "
            "the two of them stand still a "
            "moment: Joseph turning a slow "
            "tired circle, scanning doorway "
            "after warm lamplit doorway "
            "already jammed with guests, Mary "
            "swaying heavy on the patient "
            "donkey — and the simple fact "
            "assembling itself around them "
            "without any villain to blame: a "
            "whole town of open doors, and "
            "not one empty space behind any "
            "of them. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r084-b10", "out": "s10-not-out-of-cruelty-the.jpeg", "seg": "n4",
        "window": "60.242-63.638", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN", "JOSEPH"],
        "narration": "Not out of cruelty. The town was just full.",
        "must_show": "the kindly no — at a doorway: a genuinely sorry householder, palms open in apology, his packed room visible behind him; regret, not rejection.",
        "must_not_show": "no halo, glare or rim-light; the householder's face SORRY — no coldness, no slammed door.",
        "scene": (
            "At one more doorway the no comes "
            "kindly: the householder in the "
            "lamplight with his palms turned "
            "honestly open, his face full of "
            "real regret, and behind his "
            "shoulder the proof — a room "
            "wall-to-wall with sleeping kin, "
            "an aunt's feet at the threshold "
            "itself — while Joseph nods his "
            "understanding, too tired to "
            "argue with the truth: not "
            "cruelty anywhere, only fullness. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b11", "out": "s11-and-somewhere-in-that-search.jpeg", "seg": "n4",
        "window": "63.638-73.591", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN", "MARY", "JOSEPH"],
        "narration": (
            "And somewhere in that search, a tired householder, sorry that he "
            "had no space, pointed them to the only shelter left, the place "
            "where he kept his animals."
        ),
        "must_show": "the pointing — the householder's arm extended down the dark lane toward the town's edge; Joseph following the line of it; the last option offered with apology.",
        "must_not_show": "no halo, glare or rim-light; the offer HUMBLE and genuine — the best a full house had left to give.",
        "scene": (
            "The tired householder steps out "
            "into the lane and points — his "
            "arm lining past the last houses "
            "toward the dark rise at the "
            "town's edge where a low cave "
            "mouth sits behind a brushwood "
            "gate — an apology and an offer "
            "in one gesture, the place where "
            "he keeps his animals held out "
            "like the last coin in a poor "
            "man's hand — and Joseph's eyes "
            "follow the pointing arm and "
            "accept. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r084-b12", "out": "s12-so-the-king-of-all.jpeg", "seg": "n5",
        "window": "73.591-76.146", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "MARY", "JOSEPH"],
        "narration": "So the King of all creation was born in a stable.",
        "must_show": "the arrival at the cave — Joseph leading Mary and the donkey in through the stable's mouth under the deep starry sky; the lowly shelter received.",
        "must_not_show": "no halo, glare or rim-light; the birth NOT shown — this is the arrival at the shelter, night deep above.",
        "scene": (
            "Under the deep star-thick night "
            "Joseph leads the donkey the last "
            "few steps to the cave's low "
            "mouth — one hand on the halter, "
            "one steadying Mary as she leans "
            "into a wave of her hour — the "
            "rough limestone shelter opening "
            "before them with its clean straw "
            "and animal warmth, the smallest "
            "door in Bethlehem receiving the "
            "arrival every palace in the "
            "world was built hoping for. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b13", "out": "s13-a-cave-of-rough-stone.jpeg", "seg": "n5",
        "window": "76.146-84.421", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE"],
        "narration": (
            "A cave of rough stone, straw on the floor, an ox and a donkey "
            "for company, and a wooden feed-trough standing in the corner."
        ),
        "must_show": "SCRIPTURE-EXACT: the inventory — the stable interior itemised in the small lamp's light: rock walls, straw, the ox and donkey, and the empty wooden manger in its corner.",
        "must_not_show": "no halo, glare or rim-light; the manger EMPTY still — straw-lined, waiting, ordinary.",
        "scene": (
            "The small clay lamp takes the "
            "room's plain inventory: uneven "
            "limestone walls close overhead, "
            "clean straw drifted deep on the "
            "floor, the ox's great patient "
            "flank and the grey donkey "
            "settling at the wall — and in "
            "the corner on its worn legs the "
            "wooden feed-trough, straw-lined "
            "and empty, the most ordinary "
            "furniture in the world standing "
            "one hour from its place in every "
            "painting ever made. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r084-b14", "out": "s14-it-was-the-lowest-room.jpeg", "seg": "n5",
        "window": "84.421-87.180", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "TOWN"],
        "narration": "It was the lowest room in the whole town.",
        "must_show": "the lowness — from the cave's mouth looking back UP at the lamplit town stacked above on its hill; the shelter physically beneath every roof in Bethlehem.",
        "must_not_show": "no halo, glare or rim-light; the geometry literal — the town ABOVE, the cave BELOW, night sky over both.",
        "scene": (
            "From the cave's dark mouth the "
            "view runs upward: Bethlehem "
            "stacked on its hill against the "
            "stars, terrace over terrace of "
            "full lamplit houses climbing "
            "away overhead, every window of "
            "the crowded town physically "
            "higher than the straw this "
            "night will use — the lowest "
            "room in the whole town measured "
            "in honest feet and inches, at "
            "the bottom of everyone. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r084-b15", "out": "s15-and-it-was-the-only.jpeg", "seg": "n5",
        "window": "87.180-89.765", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE"],
        "narration": "And it was the only one with space.",
        "must_show": "the space — the stable's open floor in the lamp's light: room to lie down, room to breathe, straw unclaimed; the town's one emptiness, kept here.",
        "must_not_show": "no halo, glare or rim-light; the emptiness WELCOMING — warm animal quiet, not bleakness.",
        "scene": (
            "The lamp's small light shows the "
            "one thing no house in town could "
            "offer: space — a whole unclaimed "
            "floor of deep straw, room for a "
            "woman to lie down and a man to "
            "kneel and a birth to happen, "
            "warmed by the slow breathing of "
            "the ox — the only vacancy in "
            "Bethlehem, held open all along "
            "in the last place anyone would "
            "look, which is where God was "
            "sending his address. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r084-b16", "out": "s16-luke-records-the-moment-without.jpeg", "seg": "n6",
        "window": "89.765-108.757", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "MARY", "JOSEPH"],
        "narration": (
            "Luke records the moment without spectacle, in a single quiet "
            "sentence:"
        ),
        "must_show": "the hush before the sentence — the lamplit stable settled and quiet: Mary resting against the wall, Joseph banking the straw; the night holding its breath.",
        "must_not_show": "no halo, glare or rim-light; the birth NOT depicted — the beat is the quiet immediately around it.",
        "scene": (
            "The stable settles into its "
            "waiting quiet: Mary resting back "
            "against the rock wall with her "
            "eyes closed between the waves, "
            "Joseph on his knees banking the "
            "clean straw deeper beside her, "
            "the lamp steady, the animals "
            "still — a night narrowing down "
            "to one small room and one plain "
            "sentence that a physician will "
            "write with no spectacle in it "
            "at all, because none was there. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b17", "out": "s17-and-she-brought-forth-her.jpeg", "seg": "v7",
        "window": "108.757-118.225", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "MARY"],
        "narration": (
            "And she brought forth her firstborn son, and wrapped him in "
            "swaddling clothes, and laid him in a manger; because there was "
            "no room for them in the inn."
        ),
        "must_show": "SCRIPTURE-EXACT: the verse itself — Mary lowering the tightly swaddled newborn into the straw-lined manger with both hands; the sentence made visible, complete.",
        "must_not_show": "no halo on the child; the swaddling TIGHT and complete per the verse; the laying gentle, mid-motion.",
        "scene": (
            "The verse happens in the lamp's "
            "warm circle: Mary, spent and "
            "luminous with exhaustion, "
            "lowering the tightly swaddled "
            "newborn into the straw-lined "
            "wooden trough with both careful "
            "hands — the small wrapped weight "
            "settling into the manger exactly "
            "as the sentence says, while "
            "Joseph steadies the worn wood — "
            "and the reason stands all around "
            "them in the rock and straw: no "
            "room, anywhere else on earth. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b18", "out": "s18-read-that-again-slowly.jpeg", "seg": "n7",
        "window": "118.225-120.306", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE"],
        "narration": "Read that again slowly.",
        "must_show": "the dwelling — close on the manger holding the swaddled child in the lamplight: the image the narration asks us to look at twice.",
        "must_not_show": "no halo on the child; the frame STILL — one steady look at the wooden trough and its sleeping cargo.",
        "scene": (
            "The frame does what the words "
            "ask and simply looks again: the "
            "wooden feed-trough on its worn "
            "legs in the lamp's amber circle, "
            "the tightly swaddled child "
            "asleep in its straw, one tiny "
            "fist worked free of the wrapping "
            "— a feeding box for animals, "
            "holding the newborn the verse "
            "just named — the picture given "
            "a second, slower reading in "
            "perfect stillness. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r084-b19", "out": "s19-the-one-who-made-the.jpeg", "seg": "n7",
        "window": "120.306-133.050", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "MARY"],
        "narration": (
            "The one who made the stars had nowhere to lay his head the very "
            "night he arrived. The hands that shaped the mountains were small "
            "enough to curl around one of his mother's fingers."
        ),
        "must_show": "the paradox in one detail — extreme close: the newborn's tiny hand curled around Mary's single finger; through the cave mouth beyond, the deep field of stars.",
        "must_not_show": "no halo; the stars through the DOOR, the hand in the LAMP'S light — maker and made in one frame, no supernatural effects.",
        "scene": (
            "Extreme close in the lamp's "
            "warmth: the newborn's tiny hand "
            "curled entire around one of "
            "Mary's fingers, five miniature "
            "fingers gripping with their "
            "blind sleeping strength — and "
            "past them, framed small in the "
            "cave's dark mouth, the deep "
            "spangled field of stars standing "
            "over Bethlehem — the whole "
            "paradox held in one focus pull: "
            "the grip of a baby, the sky it "
            "made. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r084-b20", "out": "s20-he-did-not-come-down.jpeg", "seg": "n7",
        "window": "133.050-136.250", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE"],
        "narration": "He did not come down halfway.",
        "must_show": "no halfway — the manger low against the straw and rock floor: the actual bottom of the actual room; descent measured to the floor.",
        "must_not_show": "no halo; the framing LOW — camera height at the trough's legs, the floor's straw and stone dominant.",
        "scene": (
            "The frame drops to the room's "
            "true floor: the manger's worn "
            "wooden legs standing in straw "
            "and packed earth, the rock wall "
            "rough behind, the ox's great "
            "hoof at rest a yard away — the "
            "very bottom of the lowest room "
            "of the small town at the edge "
            "of the occupied province — and "
            "the swaddled child laid exactly "
            "there, not one inch of the "
            "distance down left untravelled. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b21", "out": "s21-he-came-all-the-way.jpeg", "seg": "n7",
        "window": "136.250-143.995", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "MARY", "JOSEPH"],
        "narration": (
            "He came all the way down, to the bottom, to the people the world "
            "had no space for."
        ),
        "must_show": "the company at the bottom — the whole humble scene: the road-worn couple, the animals, the manger child; the no-space people, and him among them.",
        "must_not_show": "no halo; the dignity of poverty absolute — worn clothes, tired faces, complete belonging.",
        "scene": (
            "The lamp's circle holds the whole "
            "company the world had no space "
            "for: a road-worn carpenter, a "
            "spent young mother, a borrowed "
            "donkey, an ox that belongs to "
            "someone else, straw that came "
            "with the cave — and in the "
            "middle of them, wrapped and "
            "sleeping in the feed-trough, the "
            "one who chose this exact company "
            "over every throne room on the "
            "planet, all the way down and "
            "home. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r084-b22", "out": "s22-no-trumpets-no-palace.jpeg", "seg": "n8",
        "window": "148.359-151.038", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE"],
        "narration": "No trumpets. No palace.",
        "must_show": "the anti-spectacle — the stable's plainness stated flat: rock, straw, lamp, trough; the frame empty of any grandeur to find.",
        "must_not_show": "no halo, no beams of light, no rich props — the plainness IS the picture.",
        "scene": (
            "The frame states the plain "
            "inventory one more time and "
            "finds it complete: rough rock, "
            "deep straw, one small clay lamp "
            "burning its honest flame, a "
            "wooden trough — no column, no "
            "banner, no herald, no gold "
            "anywhere in the picture, and "
            "nothing missing — the room "
            "history bent toward furnished "
            "with less than a poor man's "
            "kitchen, and enough. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r084-b23", "out": "s23-just-two-ordinary-exhausted-overjoyed.jpeg", "seg": "n8",
        "window": "151.038-161.711", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "MARY", "JOSEPH"],
        "narration": (
            "Just two ordinary, exhausted, overjoyed people, and a baby, and "
            "more love in that cold little room than the whole full town "
            "could hold."
        ),
        "must_show": "the fullness that counts — Mary and Joseph close together at the manger, exhaustion and joy on both faces at once; the small room brimming with the one thing the town ran out of room for.",
        "must_not_show": "no halo; BOTH truths on the faces — bone-tiredness and lit joy together, neither erased.",
        "scene": (
            "The two of them lean together at "
            "the trough's edge in the lamp's "
            "warmth — Joseph's arm around "
            "Mary's shoulders, her head "
            "tipping toward his, both faces "
            "carrying exhaustion and joy in "
            "the same breath, laughing once, "
            "quietly, at the smallness of "
            "everything — and the cold little "
            "room holds it easily: more love "
            "in one lamplit cave than the "
            "whole counted, crowded town "
            "above them could shelter. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r084-b24", "out": "s24-she-was-days-away-from.jpeg", "seg": "n2",
        "window": "40.770-43.329", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY", "JOSEPH"],
        "narration": "She was days away from giving birth.",
        "must_show": "the clock — evening on the road: Mary's profile heavy and inward-listening, Joseph's worried glance back at her; time running ahead of the miles.",
        "must_not_show": "no halo, glare or rim-light; the urgency TENDER — a husband's watchfulness, not panic.",
        "scene": (
            "In the road's evening light the "
            "clock shows in both their faces: "
            "Mary's profile gone inward, "
            "listening to her own body the "
            "way you listen for weather, both "
            "hands cradling the low-carried "
            "fullness — and Joseph glancing "
            "back at her from the halter, "
            "again, the third time in a mile, "
            "measuring the ridgeline against "
            "the days and finding the "
            "arithmetic close. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r084-b25", "out": "s25-that-is-the-scandal-and.jpeg", "seg": "n9",
        "window": "161.711-169.047", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "TOWN"],
        "narration": (
            "That is the scandal and the sweetness of it. The King everyone "
            "was too busy to make room for did not force his way in."
        ),
        "must_show": "the unforced entry — the cave lamplit-warm at the town's dark edge, its brushwood gate standing OPEN; above, the full town's shut doors; no door broken, one door open.",
        "must_not_show": "no halo, glare or rim-light; NO force anywhere — every town door intact and shut, the cave's small gate simply open.",
        "scene": (
            "The night frame sets the two "
            "kinds of door side by side: up "
            "the hill the counted town, every "
            "house door shut snug on its "
            "fullness — and below at the "
            "rocky edge the cave's brushwood "
            "gate standing open to the night, "
            "warm lamplight spilling gently "
            "out onto the stones — a King "
            "arrived without one hinge "
            "forced, one lock picked, one "
            "door so much as knocked on "
            "twice. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r084-b26", "out": "s26-he-came-small-and-quiet.jpeg", "seg": "n9",
        "window": "169.047-178.385", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE"],
        "narration": (
            "He came small, and quiet, and poor, and laid himself down among "
            "the animals, close enough for anyone at all to come near."
        ),
        "must_show": "the approachability — the manger child at eye level with the ox's gentle lowered head, the donkey near; the least guarded king who ever slept; anyone could walk in.",
        "must_not_show": "no halo; NO guard, barrier or distance — the child at touching height, the animals' gentleness the only sentries.",
        "scene": (
            "At the trough the kingdom's "
            "whole security detail stands "
            "watch: the ox's great head "
            "lowered gentle over the sleeping "
            "swaddled child, the grey donkey "
            "dozing a step away, the open "
            "cave mouth unguarded to the "
            "night — a king asleep at "
            "touching height in a feed box, "
            "small and quiet and poor, "
            "reachable by shepherd, stranger, "
            "child or sinner without one "
            "gate between. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r084-b27", "out": "s27-and-the-town-slept-on.jpeg", "seg": "n10",
        "window": "178.385-180.551", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN"],
        "narration": "And the town slept on, not knowing.",
        "must_show": "the sleeping town — Bethlehem's rooftops dark and still under the stars, windows gone black one by one; a whole town asleep beside history.",
        "must_not_show": "no halo, glare or rim-light; the town at PEACE — innocent unknowing, not guilt.",
        "scene": (
            "Bethlehem sleeps its ordinary "
            "sleep under the deep stars: "
            "rooftop after flat rooftop dark "
            "and still on the hill, the last "
            "lamplit window going black, a "
            "dog curled in a doorway, smoke "
            "standing thin and straight from "
            "a banked fire — a whole counted "
            "town breathing slow in its beds, "
            "innocently missing the one "
            "night none of its generations "
            "will ever be allowed to forget. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b28", "out": "s28-door-after-door-the-answer.jpeg", "seg": "n4",
        "window": "57.584-60.242", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN", "MARY", "JOSEPH"],
        "narration": "Door after door, the answer was the same.",
        "must_show": "the search — the couple working down the lamplit lane doorway to doorway: one door mid-apology, one already closing, the next waiting; repetition made visible.",
        "must_not_show": "no halo, glare or rim-light; every refusal REGRETFUL — shaken heads and open palms, no anger at any door.",
        "scene": (
            "The lane strings the search out "
            "door by lamplit door: at the "
            "nearest, a woman shaking her "
            "head with real sorrow, palms "
            "open; at the last, a door "
            "already easing shut on its "
            "apology; ahead, the next "
            "doorway's lamp waiting to say "
            "the same thing — Joseph leading "
            "the tired donkey down the middle "
            "of it all, collecting the one "
            "answer Bethlehem had left in "
            "stock. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r084-b29", "out": "s29-every-crowded-house-with-no.jpeg", "seg": "n10",
        "window": "180.551-191.905", "wide": True, "jesus": False, "ref": False,
        "locks": ["TOWN", "STABLE"],
        "narration": (
            "Every crowded house with no room, every window dark, while a few "
            "streets over the most important thing in the history of the "
            "world had just happened in their animal shed."
        ),
        "must_show": "the two facts in one frame — the dark sleeping town above, and at its edge the one small warm-lit cave mouth; history's address, marked by a single humble light.",
        "must_not_show": "no halo, glare or rim-light effects — the cave's light is one honest lamp through a door, the only lit thing in the night.",
        "scene": (
            "One frame holds both facts, the camera on the far "
            "slope taking hill and cave from the side, of "
            "the night: the hill of dark "
            "crowded houses stacked asleep "
            "under the stars, window after "
            "black window of people who "
            "almost made room — and below at "
            "the rock's edge, small as a "
            "held match, the cave mouth's "
            "single warm lamplight, the only "
            "waking light in Bethlehem, "
            "quietly marking the address "
            "where the history of the world "
            "just turned over in its straw. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r084-b30", "out": "s30-there-is-something-in-that.jpeg", "seg": "n11",
        "window": "191.905-193.864", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE"],
        "narration": "There is something in that you were meant to see.",
        "must_show": "the invitation to look — the manger scene framed through the open cave mouth from outside in the night: the viewer placed at the threshold, welcome to enter.",
        "must_not_show": "no halo; the threshold EMPTY and open — the composition itself an unbarred door.",
        "scene": (
            "From just outside in the night "
            "the open cave mouth frames the "
            "whole scene like a picture hung "
            "in darkness: the lamp's amber "
            "room, the couple bent at the "
            "trough, the animals' patient "
            "shapes — and between the viewer "
            "and all of it, nothing: no "
            "gate, no step, no keeper — a "
            "threshold left deliberately "
            "empty, the way you leave a door "
            "open for someone you are hoping "
            "will come. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r084-b31", "out": "s31-the-room-the-world-would.jpeg", "seg": "n11",
        "window": "193.864-203.416", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE"],
        "narration": (
            "The room the world would not give him, heaven filled with "
            "light. He was turned away at every door, so that no one who "
            "comes to him would ever have to be."
        ),
        "must_show": "heaven's answer — the cave under a sky brilliant with stars, one great bright star standing high over it; the sky itself furnishing what the town withheld; NO angels.",
        "must_not_show": "ABSOLUTE: no angels, no figures in the sky, no beams or halos — the light is stars and one brilliant star only, natural and vast.",
        "scene": (
            "Over the little cave the sky "
            "answers the town: a night "
            "brilliant to its far edges with "
            "stars, thick as spilled grain, "
            "and one great bright star "
            "standing high and steady over "
            "the rock shelter — heaven "
            "furnishing the turned-away child "
            "a ceiling grander than every "
            "roof that had no room, and "
            "hanging its lamp where anyone "
            "walking any road at all could "
            "steer by it. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r084-b32", "out": "s32-because-that-is-the-whole.jpeg", "seg": "n12",
        "window": "203.415-206.654", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE"],
        "narration": "Because that is the whole reason he came down so low.",
        "must_show": "the reason restated — the sleeping manger child close in the lamp's steadiness; lowness as love's chosen altitude.",
        "must_not_show": "no halo; the frame SIMPLE — the child, the straw, the wood, nothing else needed.",
        "scene": (
            "Close and simple in the steady "
            "lamp: the swaddled child asleep "
            "in the straw-lined trough, the "
            "small chest rising and falling, "
            "the worn wood holding him the "
            "way it has held barley for "
            "generations of oxen — the whole "
            "reason resting there at the "
            "bottom of everything: an "
            "altitude chosen on purpose, low "
            "enough that no life on earth "
            "would ever have to climb to "
            "reach him. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r084-b33", "out": "s33-there-was-no-room-for.jpeg", "seg": "n12",
        "window": "206.654-211.552", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "MARY"],
        "narration": (
            "There was no room for him, once, so that there would always be "
            "room for you."
        ),
        "must_show": "the exchange stated — Mary lifting the child from the manger to her shoulder, the trough's straw left holding his shape; the no-room absorbed, the room opened.",
        "must_not_show": "no halo; the empty straw's imprint gentle and legible — a place made, and vacated toward us.",
        "scene": (
            "Mary gathers the child up out "
            "of the manger to her shoulder — "
            "the small wrapped weight "
            "settling against her neck — and "
            "the lamp's light falls on what "
            "he leaves behind: the straw "
            "holding the pressed shape of "
            "him, a child-sized hollow in a "
            "feed-trough — the once of "
            "no-room taken and kept, and in "
            "its place, standing open in the "
            "straw, room. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r084-b34", "out": "s34-the-door-of-that-stable.jpeg", "seg": "n12",
        "window": "211.552-217.408", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE"],
        "narration": (
            "The door of that stable is still open. He is still the easiest "
            "person in the world to reach."
        ),
        "must_show": "the closing image — the cave mouth standing open in the deep starry night, warm lamplight across its threshold, the path to it plain; an open door, held.",
        "must_not_show": "no halo, glare or rim-light; the door OPEN to the last frame — no figure barring it, the path unobstructed.",
        "scene": (
            "The closing frame rests on the "
            "open door: the cave mouth in the "
            "deep star-hung night, its "
            "brushwood gate swung wide and "
            "staying wide, the lamp's warm "
            "light laid out across the "
            "threshold stones like a carpet "
            "put down for whoever comes — a "
            "plain dirt path running up to "
            "it from the dark, unbarred, "
            "unwatched, unpriced — the "
            "easiest door on earth, still "
            "standing open. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "TOWN": "PLACE-REF/town.jpeg",  # build-38-persistent-widow v2-r038-b46
}
# === end PLACE-PLATES ===
