#!/usr/bin/env python3
"""V2 beat map — row 59, build-59-feeding-4000 (Mark 8:1-9; Matt 15:32-38).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 27 pictures over 154.5 s narration = 5.7 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Mark 8:1-9 KJV):
  v1   the multitude being VERY GREAT, and having NOTHING TO EAT — this is
       the Decapolis side (Mark 7:31): remote, RUGGED, rocky country, NOT
       the green hillside of row 58; the two feedings must not look alike.
  v2   "I have compassion on the multitude, because they have now been with
       me THREE DAYS, and have nothing to eat." (jv2) — a three-day
       encampment: bedrolls, cold fire rings, settled family clusters.
  v3   "if I send them away fasting... they will FAINT BY THE WAY: for
       DIVERS OF THEM CAME FROM FAR." (j3) — HE raises it; nobody asked
       him. The noticing is the Seed (b09).
  v4   the disciples: "From whence can a man satisfy these men with bread
       here in the WILDERNESS?" (s4) — asked in front of the man who fed
       five thousand; the irony is staged in b13.
  v5   "How many loaves have ye?" "SEVEN." (j5/s5) — plus A FEW small
       fishes (v7). COUNT DISCIPLINE: seven loaves, and at the end SEVEN
       baskets (v8) — both must be countable in their frames.
  v6   he commanded the people to SIT DOWN ON THE GROUND (no grass here);
       took the seven loaves, GAVE THANKS, BRAKE, gave to his disciples to
       set before them.
  v8   they did eat, and WERE FILLED: they took up of the broken meat that
       was left SEVEN BASKETS.
  v9   they that had eaten were ABOUT FOUR THOUSAND: and HE SENT THEM AWAY
       — the sending is cared-for, not dismissal (b26).

CONTENT-CARE: row 59 is not in the §3 flag table = GREEN.

TIME-OF-DAY ARC: day three of the encampment — hard bright mid-morning for
the compassion beats, high dry noon for the loaves and the feeding, then
late-afternoon into golden evening for the baskets, the count and the
sending home.

CAST-REF NOTE: no named cast beyond Jesus; the disciples are kept generic.
If one disciple face recurs strongly at QC, lock it as
CAST-REF-V2/disciple-a-ref.jpeg and add "char_refs" to his later beats.
Text locks alone do not hold a face.
"""

LOCKS = {
    "WILDS": (
        "WILDERNESS LOCK: remote rugged Decapolis country east of the "
        "lake — broken rocky slopes, pale dust, grey stone outcrops and "
        "thorn scrub under a hard bright sky, the Sea of Galilee a far "
        "silver line to the west; NO green meadow, NO town, NO road but "
        "faint goat-tracks. Nothing about the place feeds anybody — "
        "that is its sentence in every frame."
    ),
    "CROWD": (
        "CROWD LOCK: the multitude is a three-day encampment of "
        "ordinary families from far places — bedrolls and travel "
        "bundles, cold fire rings, sleeping mats between the rocks — "
        "all of them in SATURATED DEEP earth colours: dark chocolate "
        "brown, deep russet, burnt ochre, dark olive and dusty indigo "
        "wool, dusty from three days of ground and sun; every garment "
        "plainly darker than the pale rock; no one in the crowd wears "
        "cream, off-white, ivory or any pale near-white cloth."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the disciples wear plain work tunics in the "
        "same deep saturated earth wools as the crowd — dark "
        "charcoal-brown, deep russet, dark olive, dusty indigo — with "
        "plain leather or rope belts; none of them wears cream, "
        "off-white or any pale near-white cloth."
    ),
    "BREAD": (
        "BREAD LOCK: the food is EXACTLY SEVEN flat round loaves — "
        "coarse dark wheat bread, each the size of two spread hands — "
        "and a few small dried fish, carried in one worn leather "
        "provision sack. At the gathering, the leftovers fill EXACTLY "
        "SEVEN large woven rope-handled baskets, each heaped over the "
        "brim. Seven is countable wherever loaves or baskets appear."
    ),
}

REF = True

# The committed V1 mark-8_feeding-4000.mp4 is a STALE render (173.533s) longer
# than the re-voiced segment mp3s actually sum to (172.529s timeline). Per the
# assembler's prescribed in-file fix (documented in v2_assemble.py; used on rows
# 53/56), rebuild the authoritative track from the verified V1 segment mp3s at
# the extract_beats offsets and hash-verify. Nothing is re-voiced; V1 read-only.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r059-b01", "out": "s01-a-remote-rugged-place.jpeg", "seg": "n1 p1",
        "window": "0.28-6.48", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WILDS", "CROWD"],
        "narration": ("Another huge crowd had come to Jesus, this time in "
                      "a remote and rugged place far from any town."),
        "must_show": "the setting stated — the vast crowd camped through broken rocky country around Jesus; no town, no green, no road.",
        "must_not_show": "this must NOT look like the 5000's green hillside — rock, dust and thorn are the palette.",
        "scene": (
            "Across a broken rocky slope under a hard bright sky, "
            "the camera high on an outcrop behind the camp's near "
            "edge, the "
            "great crowd spreads camped among the boulders and thorn "
            "scrub — family clusters wedged into the lee of outcrops, "
            "bundles and bedrolls, paths of trodden dust winding "
            "between them — and at the heart of the encampment Jesus "
            "stands teaching on a flat grey stone, the far silver "
            "line of the lake the only water in the world. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r059-b02", "out": "s02-three-whole-days.jpeg", "seg": "n1 p2a",
        "window": "6.48-11.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WILDS", "CROWD"],
        "narration": ("They had been with him three whole days, listening "
                      "and being healed,"),
        "must_show": "the duration made visible — a settled camp: cold fire rings, laundry on thorn bushes, a healed man's abandoned crutch; and still they listen.",
        "must_not_show": "three days of wear on everyone — dust, sun, tiredness — and not one family packing to leave.",
        "scene": (
            "The camp wears its three days: cold ash rings between "
            "the rocks, a child asleep on a bedroll in the shade of "
            "a propped cloak, a crutch lying abandoned beside a man "
            "who no longer needs it — and all around, the dusty "
            "sun-worn families still sit turned toward Jesus where "
            "he moves among them, listening on day three as though "
            "it were hour one. Hard morning light. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r059-b03", "out": "s03-the-food-was-gone.jpeg", "seg": "n1 p2b",
        "window": "11.00-16.04", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": ("and now their food was completely gone, and they "
                      "were a long way from home."),
        "must_show": "the empty larder — a mother shaking out an empty provision sack; the last crumbs shared between children.",
        "must_not_show": "quiet want, not misery-spectacle — patient people simply out of food.",
        "scene": (
            "In the shade of a boulder a mother holds her family's "
            "provision sack upside down and shakes it — nothing "
            "falls — while her two children watch the sack with the "
            "steady serious eyes of the hungry, and the youngest "
            "chews the last heel of bread broken into thirds. Around "
            "them other families' sacks lie already flat and empty "
            "on the rocks. Hard late-morning light. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r059-b04", "out": "s04-he-called-them-over.jpeg", "seg": "n1 p3",
        "window": "16.04-19.52", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "WILDS"],
        "narration": "And Jesus called his disciples over and said:",
        "must_show": "the summons — Jesus beckoning the disciples in to himself, away from the crowd's edge; something is on his mind.",
        "must_not_show": "the disciples come not knowing why — no anxiety yet on their faces, only attention.",
        "scene": (
            "Jesus stands a little apart on the rocky slope with one "
            "hand raised in a small beckoning gesture, his eyes still "
            "resting out over the camped multitude — and the "
            "disciples converge on him from their scattered places "
            "among the crowd, stepping over rocks and bedrolls, "
            "faces open and unsuspecting, gathering in around a "
            "teacher who has visibly been watching something they "
            "have not seen yet. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r059-b05", "out": "s05-i-have-compassion.jpeg", "seg": "jv2",
        "window": "19.52-27.92", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("I have compassion on the multitude, because they "
                      "have now been with me three days, and have nothing "
                      "to eat. (Mark 8:2)"),
        "must_show": "the compassion stated — close on Jesus's face turned toward the unseen crowd, the feeling plain and specific in it.",
        "must_not_show": "no grief-face — this is warm, practical compassion: love that has already counted the days and the miles.",
        "scene": (
            "Close on Jesus's face in the hard bright light, turned "
            "out toward the camped thousands beyond the frame: his "
            "warm eyes move slowly across them while he speaks, "
            "resting here and there on particular families, and the "
            "compassion in his face is not a mood but an "
            "inventory — a man who has been keeping count of three "
            "days, every empty sack, and every mile between these "
            "people and their homes. Exactly one person is in the "
            "frame, with one head."
        ),
    },
    {
        "id": "v2-r059-b06", "out": "s06-faint-by-the-way.jpeg", "seg": "j3",
        "window": "27.92-37.45", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "WILDS", "CROWD"],
        "narration": ("And if I send them away fasting to their own "
                      "houses, they will faint by the way: for divers of "
                      "them came from far. (Mark 8:3)"),
        "must_show": "v3 — the far roads: Jesus's arm sweeping toward the empty distances the crowd would have to cross; the disciples following the gesture.",
        "must_not_show": "the horizon does the arguing — nothing but rock and haze in the direction he points.",
        "scene": (
            "Jesus stands among his disciples, the camera at the "
            "group's side so the sweeping arm crosses in profile "
            "toward the empty distances, one arm swept "
            "out toward the vast empty country beyond the camp — "
            "ridge after pale ridge dissolving into heat-haze with "
            "not a roof or well among them — and the disciples' "
            "eyes follow the gesture out into all that distance and "
            "come back uneasy, the arithmetic of hungry miles "
            "starting up behind their faces. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r059-b07", "out": "s07-he-saw-them-one-by-one.jpeg", "seg": "n1b p1-p2",
        "window": "37.45-43.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": ("I feel for these people, he said. They have been "
                      "with me three days and they have nothing left to "
                      "eat."),
        "must_show": "what his eyes were resting on — the particular people: an old man dozing upright, a listless child in a mother's lap.",
        "must_not_show": "no crowd-as-mass in this frame — three or four specific, seen human beings.",
        "scene": (
            "The particulars of the multitude, close: an old man "
            "asleep sitting upright against a boulder with his "
            "staff still in his fist, sun-scorched; beside him a "
            "small girl lying listless across her mother's lap, "
            "cheek on the folded shawl, while the mother fans her "
            "with the flat of her hand — a few of the four thousand "
            "reasons, seen one at a time the way he saw them. Hard "
            "noon light softened in the boulder's shade. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r059-b08", "out": "s08-some-came-from-far.jpeg", "seg": "n1b p3",
        "window": "43.15-49.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": ("And if I send them home hungry they will collapse "
                      "on the way — some of them have come a very long "
                      "distance."),
        "must_show": "the miles made visible — worn-through sandals, road-cracked feet, a travel staff worn smooth; the cost of the coming.",
        "must_not_show": "no faces needed — feet and gear tell the distance.",
        "scene": (
            "Close along the ground at the camp's edge: a row of "
            "travellers' feet and gear in the dust — sandals worn "
            "through at the heel and mended with cord, feet "
            "road-cracked and grey with miles, a walking staff worn "
            "glass-smooth at the grip, an empty water-skin flat as "
            "cloth — the long way here written on everything, with "
            "the long way home still owed. Hard noon light raking "
            "the dust."
        ),
    },
    {
        "id": "v2-r059-b09", "out": "s09-he-was-the-one-who-noticed.jpeg", "seg": "n1b p4-p5",
        "window": "49.59-54.09", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Nobody had raised it with him. He was the one who "
                      "noticed."),
        "must_show": "the Seed of the build — Jesus's watching face: attention as love; the noticing itself.",
        "must_not_show": "nothing dramatic — quiet, sustained, deliberate attention; the frame must feel like watching, not posing.",
        "scene": (
            "Close on Jesus in profile against the pale rock, "
            "perfectly still, his eyes moving over the camp with "
            "unhurried, deliberate attention — the look of someone "
            "reading faces the way other men read weather, missing "
            "nothing, asked for nothing, already resolved — the "
            "first heart on that whole mountainside to feel the "
            "hunger of the other four thousand. Exactly one person "
            "is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r059-b10", "out": "s10-the-disciples-were-baffled.jpeg", "seg": "n2 p1-p2",
        "window": "54.09-59.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["DISCIPLES"],
        "narration": ("He would not just send them off. So he turned to "
                      "his disciples; but they were baffled."),
        "must_show": "the bafflement — the disciples' huddle: spread hands, exchanged looks, the problem too big to hold.",
        "must_not_show": "not stupidity — honest men honestly out of their depth.",
        "scene": (
            "The disciples stand in a loose ring on the rocks, "
            "bafflement running around it — one with both hands "
            "spread empty, one scrubbing the back of his neck and "
            "squinting at the horizon, two exchanging the sidelong "
            "look of men hoping the other has an idea — good "
            "practical men handed a problem with no practical "
            "bottom. Hard bright light. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r059-b11", "out": "s11-whence-in-the-wilderness.jpeg", "seg": "s4",
        "window": "59.23-65.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["DISCIPLES", "WILDS"],
        "narration": ("From whence can a man satisfy these men with bread "
                      "here in the wilderness? (Mark 8:4)"),
        "must_show": "v4 — the question thrown at the landscape: a disciple's arms flung wide at the barren rock in every direction.",
        "must_not_show": "the land answers him — nothing but stone, thorn and haze wherever the gesture points.",
        "scene": (
            "One disciple has thrown both arms out wide at the "
            "wilderness itself, mid-protest, turning as he gestures "
            "— and everything his arms take in agrees with him: "
            "broken rock, grey thorn, pale dust shimmering off to "
            "ridges with nothing behind them, a country that could "
            "not feed forty, let alone four thousand. The other "
            "disciples watch the sweep of his arms in glum "
            "agreement. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r059-b12", "out": "s12-doing-the-arithmetic.jpeg", "seg": "n2b p1",
        "window": "65.02-69.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["DISCIPLES"],
        "narration": ("Where out here, they said, could anybody get "
                      "enough bread to fill a crowd this size?"),
        "must_show": "the counting — a disciple tallying on his fingers against the visible size of the camp; the sums failing.",
        "must_not_show": "his face does the math and loses — furrowed, moving lips, a shake of the head.",
        "scene": (
            "Close on one earnest round-faced disciple counting on "
            "his fingers, lips moving through the figures, brow "
            "buckled — his eyes flicking up past his own hands to "
            "the camped thousands spread over the slope behind, "
            "then back down as the count collapses, finishing with "
            "a slow hopeless shake of the head at his own fingers. "
            "Exactly one person is in the frame in focus, with two "
            "hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r059-b13", "out": "s13-standing-right-in-front-of-them.jpeg", "seg": "n2b p2",
        "window": "69.98-78.66", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "WILDS"],
        "narration": ("They were standing in a wilderness doing the "
                      "arithmetic, with the man who had already fed five "
                      "thousand standing right in front of them."),
        "must_show": "the irony staged — the fretting huddle in the foreground, and Jesus standing plainly before them, calm, waiting to be remembered.",
        "must_not_show": "Jesus is IN their line of sight and out of their thoughts — the composition must carry that.",
        "scene": (
            "The disciples' huddle fills the near frame — bent "
            "heads, counting hands, worry passing around the ring — "
            "and directly in front of them, plainly visible over "
            "their bowed shoulders, Jesus stands quiet on the rocks "
            "with his hands at rest, watching them work the "
            "impossible sum while the answer to it waits three "
            "paces away with the patience of a mountain. Hard "
            "bright light. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r059-b14", "out": "s14-he-did-not-scold-them.jpeg", "seg": "n3 p1-p2",
        "window": "78.66-83.64", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Jesus did not scold them for it. He just asked "
                      "them what they already had."),
        "must_show": "the patience — close on Jesus's face: no reproach anywhere in it, only the gentle redirection beginning.",
        "must_not_show": "no sigh, no disappointment — the same kind knowing as the fed-five-thousand day.",
        "scene": (
            "Close on Jesus's face as he turns to the worried "
            "huddle: nothing in it scolds — the brow is smooth, "
            "the eyes warm with something close to humour held "
            "kindly back — the face of a teacher stepping past a "
            "wrong answer without grinding it in, already asking "
            "the smaller, better question. Exactly one person is "
            "in the frame, with one head."
        ),
    },
    {
        "id": "v2-r059-b15", "out": "s15-how-many-loaves.jpeg", "seg": "j5 + s5",
        "window": "83.64-89.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["DISCIPLES", "BREAD"],
        "narration": "How many loaves have ye? (Mark 8:5) / Seven.",
        "must_show": "v5 — the inventory: a disciple holding the provision sack open, seven flat loaves visible; the answer on his face.",
        "must_not_show": "COUNT DISCIPLINE: exactly seven loaves, countable in the open sack.",
        "scene": (
            "A disciple crouches with the worn leather provision "
            "sack pulled open on a flat rock, tipping it to the "
            "light — inside, EXACTLY SEVEN flat round loaves of "
            "coarse dark bread and a few small dried fish — and he "
            "looks up from the count with the number on his face, "
            "half-ashamed of its smallness, holding the sack's "
            "mouth wide so the others can see for themselves. "
            "Exactly two people are in the frame; each has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r059-b16", "out": "s16-seven-and-a-few-fish.jpeg", "seg": "n3b p1-p2",
        "window": "89.12-94.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["BREAD"],
        "narration": ("How many loaves do you have, he asked. Seven, they "
                      "said — and a few small fish."),
        "must_show": "the whole supply laid out — seven loaves in a row on the rock, the few small fish beside; everything there is.",
        "must_not_show": "exactly seven loaves in the row — the count is the caption.",
        "scene": (
            "Laid out in a row on the flat grey rock in the hard "
            "noon light: EXACTLY SEVEN coarse dark loaves, side by "
            "side, and beside them a small handful of dried fish — "
            "the entire food supply of a camp of four thousand, "
            "photographed plainly like an inventory, the empty "
            "leather sack crumpled at the row's end. Nothing else "
            "is on the rock."
        ),
    },
    {
        "id": "v2-r059-b17", "out": "s17-he-took-it-gladly.jpeg", "seg": "n3b p3-p4",
        "window": "94.49-102.09", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BREAD"],
        "narration": ("It was almost nothing against so great a need. "
                      "But he took it gladly; in his hands, it was more "
                      "than enough."),
        "must_show": "the acceptance — Jesus gathering the seven loaves up into his arms with visible gladness; smallness received as plenty.",
        "must_not_show": "no irony in his face — genuine glad sufficiency; his hands full of exactly enough.",
        "scene": (
            "Jesus gathers the seven dark loaves up against his "
            "chest with both arms, the way a man carries firewood, "
            "and there is plain gladness in his face as he takes "
            "them — no appraisal, no weighing, the settled "
            "satisfaction of someone whose hands now hold more "
            "than enough — while a disciple stands by with the few "
            "fish cupped in his two hands, watching. Exactly two "
            "people are in the frame; each has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r059-b18", "out": "s18-sit-down-on-the-ground.jpeg", "seg": "nbless p1",
        "window": "102.09-104.02", "wide": True, "jesus": False, "ref": False,
        "locks": ["CROWD", "WILDS"],
        "narration": "He had the people sit down on the ground.",
        "must_show": "v6 — the multitude settling onto the bare rocky ground (no grass here); order arriving over the camp.",
        "must_not_show": "GROUND, not grass — dust and stone under every family; the contrast with row 58 held.",
        "scene": (
            "Across the rocky slope, the camera above the nearest "
            "seated backs, the multitude settles down "
            "onto the bare ground — families folding onto spread "
            "cloaks over the dust, old men eased down onto flat "
            "stones, children pulled into laps — the restless camp "
            "resolving into thousands seated on stone and dust "
            "under the high sun, every face beginning to turn one "
            "way. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r059-b19", "out": "s19-gave-thanks-and-brake.jpeg", "seg": "nbless p2",
        "window": "104.02-111.55", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "BREAD"],
        "narration": ("Then he took the seven loaves, and gave thanks, "
                      "and broke them, and gave them to his disciples to "
                      "set before the crowd."),
        "must_show": "v6 — the thanksgiving and breaking: loaves lifted, face to heaven, the first loaf breaking; disciples' baskets already held out.",
        "must_not_show": "no light effect, no multiplication shown — thanks, breaking, and human hands receiving.",
        "scene": (
            "Against the hard bright sky Jesus lifts the seven "
            "loaves stacked between his two hands, face raised to "
            "heaven, eyes closed in thanks — and his thumbs break "
            "the topmost dark loaf cleanly open — while below his "
            "hands the disciples hold their wide baskets in "
            "close, first receivers of a supply that has just "
            "quietly stopped being seven. Exactly three people are "
            "in the frame; each has two arms, two hands of five "
            "fingers each and one head."
        ),
    },
    {
        "id": "v2-r059-b20", "out": "s20-once-again-it-kept-coming.jpeg", "seg": "n4 p1",
        "window": "111.55-113.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["DISCIPLES", "BREAD"],
        "narration": "And once again the food did not run out.",
        "must_show": "the refill astonishment — a basket heaped again mid-round; the carrying disciple's face doing the impossible math.",
        "must_not_show": "abundance shown only as arithmetic in human hands — never as an effect at the bread.",
        "scene": (
            "Close on a wide rope-handled basket riding on a "
            "disciple's hip, heaped over the brim with broken dark "
            "bread and fish though he has been emptying it down "
            "the rows since he set out — his forearm braced under "
            "a weight that keeps not diminishing, and his face "
            "above it half laugh, half awe, a man catching heaven "
            "red-handed in his own basket. Exactly one person is "
            "in the frame in focus, with two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r059-b21", "out": "s21-through-the-whole-multitude.jpeg", "seg": "n4 p2a",
        "window": "113.63-119.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["DISCIPLES", "CROWD", "WILDS"],
        "narration": ("The disciples carried bread and fish through the "
                      "whole multitude,"),
        "must_show": "the distribution across the rocks — disciples threading the seated thousands, bread passing down rows of lifted hands.",
        "must_not_show": "the food moves hand to hand to hand — the human chain is the mechanism on display.",
        "scene": (
            "The disciples thread the seated multitude across the "
            "rocky slope with their heaped baskets — one crouching "
            "to load an old woman's spread shawl, another passing "
            "loaves down a whole row of raised hands that relay "
            "them family to family over the dust — lanes of "
            "passing bread crisscrossing the camp in the "
            "afternoon light, and no basket emptying. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r059-b22", "out": "s22-completely-satisfied.jpeg", "seg": "n4 p2b",
        "window": "119.00-125.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD", "WILDS"],
        "narration": ("and everyone ate until they were completely "
                      "satisfied, thousands of people, fed from almost "
                      "nothing."),
        "must_show": "the satisfaction on stony ground — families eating their fill among the rocks; the listless child from b07 eating.",
        "must_not_show": "call back b07 if possible — the listless girl now sitting up eating; continuity of mercy.",
        "scene": (
            "Among the boulders the multitude eats its fill in the "
            "warm afternoon light: the small girl who lay listless "
            "across her mother's lap now sits up against her "
            "shoulder working through a piece of bread with both "
            "hands, the old man with the staff chews with his eyes "
            "shut in something like prayer, families lean back "
            "against the rocks with the ease of the fed — want "
            "gone out of a whole camp between noon and afternoon. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r059-b23", "out": "s23-seven-large-baskets.jpeg", "seg": "n5 p1",
        "window": "125.06-130.13", "wide": True, "jesus": False, "ref": False,
        "locks": ["DISCIPLES", "BREAD", "WILDS"],
        "narration": ("When they gathered up what was left over, they "
                      "filled seven large baskets with the broken "
                      "pieces."),
        "must_show": "v8 — the count: EXACTLY SEVEN large baskets heaped with fragments, lined up on the rock in late light.",
        "must_not_show": "COUNT DISCIPLINE: seven baskets, countable at a glance — no more, no fewer.",
        "scene": (
            "On a shelf of flat rock in the late-afternoon light, "
            "the camera low along the line so all seven read in "
            "profile, "
            "stand EXACTLY SEVEN large rope-handled baskets in a "
            "row, every one heaped over its brim with broken dark "
            "bread — and behind the row two disciples set the "
            "last one down and straighten up, looking at the line "
            "of them, one wiping his hands slowly on his tunic as "
            "if to be sure they are real. Exactly seven baskets "
            "are in the row. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r059-b24", "out": "s24-more-at-the-end.jpeg", "seg": "n5 p2",
        "window": "130.13-134.32", "wide": False, "jesus": False, "ref": False,
        "locks": ["BREAD"],
        "narration": ("There was far more at the end than there had been "
                      "at the start."),
        "must_show": "the arithmetic in one image — the empty leather sack that held seven loaves lying beside the seven heaped baskets.",
        "must_not_show": "start and end in the same frame: the little flat sack against the towering leftovers.",
        "scene": (
            "Close on the ground in the golden light: the worn "
            "leather provision sack — the one that carried all "
            "seven loaves this morning — lies flat and empty in "
            "the dust at the foot of the seven heaped baskets, "
            "small as a dropped glove against the wall of "
            "abundance standing over it; the whole day's "
            "arithmetic in one patch of rock."
        ),
    },
    {
        "id": "v2-r059-b25", "out": "s25-four-thousand-went-home-full.jpeg", "seg": "n6 p1",
        "window": "134.32-139.25", "wide": True, "jesus": False, "ref": False,
        "locks": ["CROWD", "WILDS"],
        "narration": ("About four thousand people were there that day, "
                      "and every single one of them went home full."),
        "must_show": "v9 — the departure beginning: long streams of families setting out from the camp in every homeward direction in the golden evening.",
        "must_not_show": "they leave STRONG — upright walkers, children riding shoulders; the faint-by-the-way fear answered.",
        "scene": (
            "In the golden evening, the camera behind the emptying "
            "camp, the whole slope breaks up into long "
            "homeward streams — families filing out along the "
            "goat-tracks in every direction, bundles reslung, "
            "children riding high on fathers' shoulders, old men "
            "swinging their staffs with fed strength — thousands "
            "walking off into the gold-lit distances that were "
            "going to defeat them this morning. An upright "
            "vertical photograph, the ground at the bottom of the "
            "frame and the sky at the top, the horizon level — "
            "the picture is the right way up. Every figure has "
            "two arms, two legs and one head."
        ),
    },
    {
        "id": "v2-r059-b26", "out": "s26-sent-away-cared-for.jpeg", "seg": "n6 p2",
        "window": "139.25-144.16", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CROWD", "WILDS"],
        "narration": ("Then he sent them away, cared for, in body and in "
                      "soul."),
        "must_show": "the sending as blessing — Jesus among the departing families, a hand raised in farewell, faces turned back to him as they go.",
        "must_not_show": "not a dismissal — a shepherd seeing the flock onto the road; warmth both directions.",
        "scene": (
            "Jesus stands at the camp's edge in the low gold light "
            "as the families file past and away — one hand lifted "
            "in steady farewell, a last word given to a mother as "
            "she passes, a small girl waving back at him from her "
            "father's shoulder until the track bends — the sender "
            "standing planted while the sent stream homeward "
            "around him like water parting at a stone. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r059-b27", "out": "s27-that-is-who-he-is.jpeg", "seg": "n7",
        "window": "144.16-154.24", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WILDS", "BREAD"],
        "narration": ("He did not owe them a meal. But he saw tired, "
                      "hungry people a long way from home, and he could "
                      "not bear to send them away empty. That is simply "
                      "who he is."),
        "must_show": "the closing frame — the emptied camp at dusk: Jesus alone among the cold fire rings and the seven baskets, the last homeward streams far off.",
        "must_not_show": "no halo/glow; the quiet after mercy — an empty wilderness that was, for one day, a banquet hall.",
        "scene": (
            "The slope at dusk, emptied: cold fire rings and "
            "trodden dust where four thousand sat, the seven "
            "heaped baskets in their row on the rock shelf, and "
            "Jesus standing alone among the traces in the last "
            "ember light, watching the far-off homeward lines "
            "dwindle into the blue distances — the host of a "
            "banquet hall made of rocks, closing it down. An "
            "upright vertical photograph, the ground at the "
            "bottom of the frame and the sky at the top, the "
            "horizon level — the picture is the right way up. "
            "Exactly one person is in the frame, with two arms, "
            "two legs and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "WILDS": "PLACE-REF/wilds.jpeg",  # build-59-feeding-4000 s01-a-remote-rugged-place (manual)
}
# === end PLACE-PLATES ===
