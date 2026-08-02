#!/usr/bin/env python3
"""V2 beat map — row 14, build-14-ten-lepers (Luke 17:11-19).

COVERAGE: 35 pictures against V1's 12, over 197.7 s = 5.6 s/picture.

⚠️ THIS ROW HAS A NAMED V1 DEFECT IN THE FIX QUEUE (Cameron): "~0:55 the ten
lepers look like GIANTS next to Jesus and the disciples; fix the scale."

That is a PERSPECTIVE failure and it happens for a reason: the text puts the ten
"afar off", every prompt says so, and the model paints them at full size anyway
because they are the subject of the sentence. Prose like "in the distance" does
not fix it. So every frame containing both the ten and Jesus states the scale
RELATIONALLY and in pixels-on-the-page terms:

    the ten are FAR SMALLER IN THE FRAME than Jesus and the disciples — each of
    them roughly HALF the height of the nearer figures, small with distance.

That sentence, or its equivalent, is in b03, b04, b06, b07, b09, b12 and b13 —
every frame where the gap exists. If a generated frame has a leper anywhere near
the height of a foreground figure, it is a hard fail and gets rerolled.

SCRIPTURE FACTS (Luke 17:11-19 KJV):
  v11  "he passed through the MIDST of Samaria and Galilee" — the borderland
       seam, which is why v16's punchline lands.
  v12  "ten men that were lepers, which STOOD AFAR OFF" — the distance is legal,
       not shyness (Lev 13:46), and n1 says so.
  v13  "they LIFTED UP THEIR VOICES" — they have to shout across a gap.
  v14  "Go shew yourselves unto the priests. And it came to pass, that, AS THEY
       WENT, they were cleansed." Nothing happens at the meeting. He does not
       touch them, does not announce it, and the healing lands on the ROAD,
       mid-obedience, with him nowhere in sight. b16-b18 must have no Jesus.
  v15  "when he SAW that he was healed, turned back, and with a LOUD VOICE
       glorified God"
  v16  "fell down on his face at his feet ... AND HE WAS A SAMARITAN."
  v17-18 "where are the nine? ... save this STRANGER."
  v19  "Arise, go thy way: thy faith hath made thee whole."

THE WRAPPINGS ARE A PROP THAT MUST TRACK: bound over hands and forearms and
across the lower face (b03-b15) -> loosening and falling on the road (b16-b17)
-> gone, with clean new skin (b18 on) -> left lying in the road behind him in the
final frame (b35). The narration names that last image outright.

CONTENT-CARE: row 14 is GREEN, but the RESTRAINT principle is applied anyway.
Leprosy is shown ONLY as grey linen wrappings, covered hands, and the distance
other people keep. There are NO lesions, NO wounds, NO deformity and no medical
close-up anywhere in this build. What the disease costs is carried by the EMPTY
GROUND around them, not by their bodies.

TIME OF DAY: one bright day, morning into afternoon. No night, no sunset.
"""

LOCKS = {
    "LEPERS": (
        "TEN LEPERS LOCK: the ten are the same men in every shot — a mixed group of "
        "ages from about twenty to sixty, gaunt and sun-darkened, in ragged "
        "DUST-GREY and faded brown wool. Their hands, forearms and the lower half of "
        "their faces are bound in strips of dull GREY LINEN, worn and travel-stained, "
        "and several lean on rough staffs. No sores, wounds or deformity are ever "
        "visible — the wrappings and the distance carry everything. They keep close "
        "together as a group. None of them wears off-white, ivory or any near-white "
        "cloth."
    ),
    # He is one of the ten, so this lock adds identity only — never a second
    # description of the wrappings, which would fight the LEPERS lock.
    "SAMARITAN": (
        "SAMARITAN LOCK: the one who returns is the same man in every shot — about "
        "forty, wiry and weather-beaten, a strong bony face with deep-set dark eyes "
        "and heavy black brows, and a rough black beard going grey at the chin. He is "
        "the one wearing a faded DEEP-TEAL cloth knotted at his shoulder over the "
        "grey. His face is shown clearly."
    ),
    "BORDERLAND": (
        "BORDERLAND LOCK: the open country on the seam between Samaria and Galilee — "
        "a dusty road running between low dry-stone walls, stony hillsides of thin "
        "grass and thorn scrub, scattered olive trees, a small village of "
        "honey-coloured stone houses on a rise in the middle distance, and bare "
        "ridges rolling away. Hard bright daylight, pale dust."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the disciples are the same group throughout — eight or nine "
        "working Galilean men between twenty and forty, dusty from the road with "
        "travel bags and staffs, in wool tunics of SATURATED DEEP colours: "
        "rust-brown, deep russet, dark olive, blue-grey and dusty indigo. None wears "
        "off-white, ivory or any near-white cloth. Their faces are shown clearly."
    ),
}

OUTPUT_ASSET_DIR = "assets-realistic"
OUTPUT_VIDEO_NAME = "luke-17_ten-lepers-realistic-v2.mp4"

REF = True
# The relational scale sentence, used verbatim in every frame that holds both the
# ten and the travellers. See the header note on the V1 giants defect.
FAR = ("The ten are FAR SMALLER IN THE FRAME than the figures in the foreground — "
       "each of them roughly half the height of the nearer men, small with distance "
       "across the empty ground.")

BEATS = [
    # ------------------------------------------------------ n0 — the seam ----
    {
        "id": "v2-r014-b01", "out": "s01-the-borderland.jpeg", "seg": "n0 p1",
        "window": "0.28-7.97", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "BORDERLAND"],
        "narration": ("On the way to Jerusalem, Jesus walked the borderland between "
                      "Samaria and Galilee — the seam between two peoples who despised "
                      "each other."),
        "must_show": "Jesus and the disciples walking a dusty road through open borderland country, hills rolling away on both sides.",
        "must_not_show": "no halo, glare or rim-light; no lepers yet.",
        "scene": (
            "Jesus walks a dusty road through open borderland country with the "
            "disciples strung out along it behind and beside him, bags on shoulders "
            "and staffs in hand. Low dry-stone walls run along the road, stony "
            "hillsides of thin grass and thorn scrub rise on both sides, and bare "
            "ridges roll away to the horizon. Hard bright morning light and pale dust. "
            "THE CAMERA STANDS OFF THE SIDE OF THE ROAD, low and well to their "
            "left, and they walk ACROSS the frame from right to left rather than "
            "toward the lens — every man is seen in three-quarter or full profile, "
            "chins turned along the road ahead of them, and every pair of eyes "
            "travels out of the picture through the LEFT edge, far off the camera "
            "axis. Nobody's face is squared to the lens and nobody looks back at "
            "it. The camera is back far enough to see them head to sandals on the "
            "open road. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r014-b02", "out": "s02-keep-that-seam-in-mind.jpeg", "seg": "n0 p2-p3",
        "window": "7.97-12.81", "wide": True, "jesus": False, "ref": False,
        "locks": ["BORDERLAND"],
        "narration": "Keep that seam in mind. It matters at the end of this story.",
        "must_show": "the border itself as landscape — the road running along a ridge with different country falling away on either side.",
        "must_not_show": "no people at all in this frame; the land is the subject.",
        "scene": (
            "A wide empty landscape: the dusty road runs along the spine of a low "
            "ridge, and the country falls away differently on either side of it — "
            "terraced olive slopes and green fields on one hand, dry stony scrubland "
            "on the other — two kinds of ground meeting along one line. A boundary "
            "cairn of piled stones stands beside the road. There is not a single "
            "person in the frame. Hard bright daylight."
        ),
    },
    # -------------------------------------------------- n1 — ten, afar off ----
    {
        "id": "v2-r014-b03", "out": "s03-ten-men-afar-off.jpeg", "seg": "n1 p1-p2",
        "window": "12.81-21.15", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LEPERS", "DISCIPLES", "BORDERLAND"],
        "narration": ("As he reached a village, ten men met him — but they stopped far "
                      "off, strung along a rise, and came no closer. They were lepers."),
        "must_show": "⚠️ SCALE: Jesus and the disciples LARGE in the near foreground; the ten small and distant on a rise across open ground, strung in a line.",
        "must_not_show": "⚠️ HARD FAIL if any leper approaches the height of a foreground figure. They are far away and must be painted far away. No halo or rim-light.",
        "scene": (
            "Jesus and the disciples stand large in the near foreground at the edge of "
            "the road, stopped, looking across a wide stretch of empty stony ground. "
            "Beyond that gap, strung out in a ragged line along a low rise, stand ten "
            "small figures in grey wrappings, keeping together and coming no nearer. "
            + FAR +
            " The village of honey-coloured stone stands further off behind them. Hard "
            "bright daylight, pale dust. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r014-b04", "out": "s04-the-gap-was-the-law.jpeg", "seg": "n1 p3-p5",
        "window": "21.15-33.49", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LEPERS", "DISCIPLES", "BORDERLAND"],
        "narration": ("The Law of Moses required them to live outside the town and to "
                      "warn everyone away. That gap of empty ground between them and "
                      "the road was not shyness. It was the law."),
        "must_show": "⚠️ THE GAP ITSELF as the subject — a wide expanse of empty stony ground with the travellers on one side and the small distant ten on the other, nothing in between.",
        "must_not_show": "⚠️ HARD FAIL on leper scale. Nobody is crossing the gap; the emptiness must dominate the frame. No halo or rim-light.",
        "scene": (
            "THE CAMERA STANDS BEHIND JESUS AND THE DISCIPLES AND SHOOTS PAST THEM: "
            "their BACKS and the backs of their heads fill the near left and right "
            "of the frame, large and out of focus, so not one face is turned toward "
            "the lens and no eyes are visible at all on the near side. Beyond their "
            "shoulders opens a broad expanse of bare stony ground with nothing in it "
            "at all, and on the far side, up on the rise, the ten stand in their "
            "line. The whole width of empty dust and stone lies between them. Every "
            "garment on the near side is a saturated earth colour — rust, russet, "
            "olive, blue-grey, indigo — and the only cream cloth anywhere in the "
            "frame is on Jesus. "
            + FAR +
            " Nothing and nobody occupies the ground between. Hard bright daylight. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r014-b05", "out": "s05-no-one-had-touched-them.jpeg", "seg": "n1 p6",
        "window": "33.49-37.59", "wide": True, "jesus": False, "ref": False,
        "locks": ["LEPERS", "BORDERLAND"],
        "narration": "These were ten men no one had touched in years.",
        "must_show": "the ten alone on their rise, close enough now to read their faces above the grey wrappings — worn, tired, holding together.",
        "must_not_show": "CONTENT-CARE — no sores, wounds or deformity anywhere; the wrappings and their isolation carry it. Do not put Jesus in this frame.",
        "scene": (
            "The ten stand together on the stony rise with nobody else anywhere near "
            "them, seen from their own side now. Their hands and forearms are bound in "
            "worn grey linen and cloth is drawn across the lower half of every face, "
            "and above the wrappings their eyes are tired and watchful. Several lean "
            "on rough staffs. THE CAMERA IS OFF TO ONE SIDE OF THEM AT SHOULDER "
            "HEIGHT and every one of them is turned away from it, looking out across "
            "the empty ground toward the road, so their eyes leave the picture "
            "through the RIGHT edge and nobody's face is squared to the lens. They "
            "stand close in a loose knot, shoulder to shoulder — "
            "the only people any of them are allowed near. Empty ground falls away on "
            "every side. Hard bright daylight. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r014-b06", "out": "s06-have-mercy-on-us.jpeg", "seg": "s13",
        "window": "37.59-41.35", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LEPERS", "DISCIPLES", "BORDERLAND"],
        "narration": "Jesus, Master, have mercy on us. (Luke 17:13)",
        "must_show": "⚠️ SCALE: the ten small and distant on their rise with arms raised and heads back, shouting across the gap toward the large foreground figures.",
        "must_not_show": "⚠️ HARD FAIL on leper scale. They do not step forward. No halo or rim-light.",
        "scene": (
            "Across the empty ground the ten have raised their bound arms and thrown "
            "their heads back, shouting together toward the road. In the near "
            "foreground Jesus stands large in the frame with the disciples, turned "
            "toward them and listening. "
            + FAR +
            " Not one of the ten has stepped off the rise. Hard bright daylight, dust "
            "hanging in the gap between them. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r014-b07", "out": "s07-the-only-thing-left.jpeg", "seg": "n2",
        "window": "41.35-48.13", "wide": True, "jesus": False, "ref": False,
        "locks": ["LEPERS", "SAMARITAN", "BORDERLAND"],
        "narration": ("So they did the only thing the distance left them. They lifted "
                      "up their voices together and called across the gap:"),
        "must_show": "close on the ten shouting together — mouths open above the wrappings, arms up, all calling at once; the Samaritan in his teal cloth among them.",
        "must_not_show": "do not put Jesus in this frame; this is their side of the gap.",
        "scene": (
            "Close on the group of ten on their rise, all of them calling at once — "
            "heads back, mouths open above the grey face wrappings, bound arms lifted "
            "and waving, several with both hands up. Among them near the middle is the "
            "wiry black-bearded man with the faded deep-teal cloth knotted at his "
            "shoulder, shouting with the rest. Behind them nothing but empty stony "
            "ground and sky. Hard daylight. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    # ------------------------------------------------ n3 / j1 — the instruction ----
    {
        "id": "v2-r014-b08", "out": "s08-he-did-not-close-the-distance.jpeg", "seg": "n3 p1-p2",
        "window": "48.13-54.87", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LEPERS", "DISCIPLES", "BORDERLAND"],
        "narration": ("When he saw them, he did not close the distance. He did not "
                      "touch them, and he did not announce that they were healed."),
        "must_show": "⚠️ SCALE + the gap preserved: Jesus stays exactly where he is, not one step taken; the ten still small and distant.",
        "must_not_show": "⚠️ HARD FAIL if he has moved toward them or if the gap has shrunk. No touching, no reaching. No halo or rim-light.",
        "scene": (
            "THE CAMERA STANDS BEHIND AND BESIDE JESUS at shoulder height, so he is "
            "seen from behind and in quarter profile at the near edge of the frame "
            "and his eyes travel away up the picture toward the rise, never toward "
            "the lens. He stands still at the road's edge, feet planted, having "
            "taken no step at all toward the rise; his hands are at his sides and he "
            "is not reaching out. HE IS THE ONLY MAN IN CREAM ANYWHERE IN THE FRAME "
            "AND THE ONLY MAN WITH LONG LOOSE HAIR AND AN UNCOVERED FACE. Across the "
            "wide expanse of empty stony ground the ten still stand in their line "
            "exactly where they were: TEN men and no eleventh, every single one of "
            "them in dust-grey rags with a strip of grey linen drawn across the "
            "lower half of his face and a head-cloth over his hair, so not one face "
            "in that far line is bare. "
            + FAR +
            " The distance between them is unchanged. Hard bright daylight. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r014-b09", "out": "s09-he-gave-an-instruction.jpeg", "seg": "n3 p3",
        "window": "54.87-57.53", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "He simply gave them an instruction:",
        "must_show": "close on Jesus calling across the distance — one hand lifted and pointing off toward the road to the city, matter of fact.",
        "must_not_show": "no halo, glare or rim-light; nothing ceremonial — this is a practical instruction given at a shout.",
        "scene": (
            "Close on Jesus in hard daylight, calling out across the open ground with "
            "one hand lifted and pointing away off toward the road that leads to the "
            "city. His face is plain and matter of fact, his mouth open on the words, "
            "his eyes on the distant men. There is nothing ceremonial about the "
            "gesture at all. Dust and bright empty country soft behind him. His hand "
            "has five fingers."
        ),
    },
    {
        "id": "v2-r014-b10", "out": "s10-shew-yourselves-to-the-priests.jpeg", "seg": "j1",
        "window": "57.53-61.35", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LEPERS", "BORDERLAND"],
        "narration": "Go shew yourselves unto the priests. (Luke 17:14)",
        "must_show": "⚠️ SCALE: the instruction crossing the gap — Jesus's pointing arm in the near frame, the small distant ten receiving it and turning to look at each other.",
        "must_not_show": "⚠️ HARD FAIL on leper scale. Nothing has changed about their bodies. No halo or rim-light.",
        "scene": (
            "Jesus stands large at the frame's near edge with his arm still extended, "
            "pointing away toward the road to the city. Far across the empty ground "
            "the ten have lowered their raised arms and are turning to look at one "
            "another, several heads swinging toward the direction he is pointing. "
            + FAR +
            " Their wrappings are exactly as they were. Hard bright daylight. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    # ---------------------------------------------- n4 — why a priest ----
    {
        "id": "v2-r014-b11", "out": "s11-why-a-priest.jpeg", "seg": "n4 p1-p2",
        "window": "61.35-71.00", "wide": True, "jesus": False, "ref": False,
        "locks": ["BORDERLAND"],
        "narration": ("Now, why send them to a priest? Because in Israel the priest was "
                      "the only inspector who could certify a leper clean and let him "
                      "back into his family, his work, his worship."),
        "must_show": "what is at the end of that road — the distant city on its hill, the destination, with the long road running toward it.",
        "must_not_show": "no principal characters; this frame explains the errand.",
        "scene": (
            "A wide view along the dusty road as it runs away across the dry country "
            "toward a walled city standing on a distant hill, its stone gate and "
            "rooftops small and pale in the haze of the horizon. The road is long, "
            "empty and clearly a full day's walk. Hard bright daylight, heat shimmer "
            "over the stony ground."
        ),
    },
    {
        "id": "v2-r014-b12", "out": "s12-a-promise-in-disguise.jpeg", "seg": "n4 p3-p4",
        "window": "71.00-79.75", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LEPERS", "BORDERLAND"],
        "narration": ("Sending them was a promise in disguise. That errand only made "
                      "sense one way: if they would be clean by the time they arrived."),
        "must_show": "⚠️ SCALE: Jesus watching from the near frame as the small distant ten stand on their rise working out what the instruction implies.",
        "must_not_show": "⚠️ HARD FAIL on leper scale. Nothing supernatural; no halo or rim-light.",
        "scene": (
            "THE CAMERA STANDS BEHIND JESUS'S RIGHT SHOULDER, close, so he is seen "
            "from behind in quarter profile at the near left of the frame — the back "
            "of his head and one cheekbone — and his gaze goes away from the camera, "
            "out across the ground and off through the TOP RIGHT of the picture. His "
            "face is never squared to the lens and his eyes are never on it. His arm "
            "is lowered now and his stance is quiet and waiting. Far off on the rise "
            "the ten are standing very still in a knot, plainly working something out "
            "— heads turned to each other, one gesturing off toward the city road, "
            "another looking down at his own bound hands. "
            + FAR +
            " Hard daylight over the empty ground between. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    # ------------------------------------------- n5 — nothing had changed ----
    {
        "id": "v2-r014-b13", "out": "s13-nothing-had-changed-yet.jpeg", "seg": "n5 p1",
        "window": "79.75-81.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEPERS"],
        "narration": "But nothing had changed yet.",
        "must_show": "close on bound hands held up and turned over — the grey linen exactly as it was, nothing altered.",
        "must_not_show": "CONTENT-CARE — no skin, sores or wounds visible; only the wrappings. Do not put Jesus in this frame.",
        "scene": (
            "Close on a pair of bound hands held up and being turned over slowly in "
            "the hard daylight — the worn grey linen strips wound around the palms, "
            "the fingers and the wrists exactly as they have been for years, "
            "travel-stained and unchanged. Nothing of the skin beneath is visible. The "
            "blurred grey shapes of the other men are behind. Each hand has five "
            "fingers."
        ),
    },
    {
        "id": "v2-r014-b14", "out": "s14-no-proof-of-welcome.jpeg", "seg": "n5 p2",
        "window": "81.13-88.78", "wide": True, "jesus": False, "ref": False,
        "locks": ["LEPERS", "SAMARITAN", "BORDERLAND"],
        "narration": ("They looked at each other, at their own still-bandaged hands, at "
                      "the long road to a city they had no proof they would be welcome "
                      "in."),
        "must_show": "the ten looking between each other, their own hands, and the long empty road to the distant city — the whole calculation on their faces.",
        "must_not_show": "do not put Jesus in this frame; nobody has started walking yet.",
        "scene": (
            "The ten stand on the rise looking in three directions at once — two are "
            "facing each other with their eyes locked, one has his bound hands turned "
            "up in front of him staring down at them, and three more have turned to "
            "look away down the long dusty road that runs off toward the far walled "
            "city. Nobody has taken a step. The Samaritan with the deep-teal cloth "
            "stands among them looking at the road. Hard daylight. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r014-b15", "out": "s15-they-started-walking-anyway.jpeg", "seg": "n5 p3",
        "window": "88.78-93.20", "wide": True, "jesus": False, "ref": False,
        "locks": ["LEPERS", "SAMARITAN", "BORDERLAND"],
        "narration": "And then, one by one, they turned and started walking anyway.",
        "must_show": "the group breaking into movement — turning away toward the city road, first one, then others following, still wrapped, nothing healed.",
        "must_not_show": "their wrappings are still on and nothing has changed; do not put Jesus in this frame.",
        "scene": (
            "The knot of ten is breaking apart into movement on the rise. The nearest "
            "man has turned fully away and taken the first step toward the city road, "
            "two more are mid-turn behind him, and the rest are shifting to follow, "
            "staffs coming up. Every hand and face is still bound in grey linen and "
            "nothing about any of them has changed. Dust lifts under the first "
            "footfalls. Hard daylight, the long road ahead. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    # ------------------------------------------------ n6/n7 — as they went ----
    {
        "id": "v2-r014-b16", "out": "s16-as-they-went.jpeg", "seg": "n6 a",
        "window": "93.20-97.93", "wide": True, "jesus": False, "ref": False,
        "locks": ["LEPERS", "BORDERLAND"],
        "narration": ("And as they went — on the road, mid-step, in the middle of "
                      "obeying,"),
        "must_show": "SCRIPTURE-EXACT (v14): the ten walking the open road ALONE, well away from where they met him, mid-journey — and Jesus nowhere in the frame.",
        "must_not_show": "⚠️ Jesus must NOT appear in this frame or the next two — the healing happens on the road with him out of sight, and that is the point.",
        "scene": (
            "The ten walk together up the long dusty road across open country, well "
            "away now from where they stopped, strung out in a loose group with their "
            "staffs and their bound hands, heads down against the glare. The land "
            "around them is empty in every direction and there is nobody else "
            "anywhere in the frame. Hard bright daylight, dust rising off their feet. "
            "The camera is back far enough to see them head to sandals. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r014-b17", "out": "s17-they-were-made-clean.jpeg", "seg": "n6 b",
        "window": "97.93-102.15", "wide": True, "jesus": False, "ref": False,
        "locks": ["LEPERS", "BORDERLAND"],
        "narration": "before there was one thing to see — they were made clean.",
        "must_show": "the moment mid-stride — men stopping dead in the road, looking down at themselves, one grabbing another's arm.",
        "must_not_show": "nothing supernatural in the air, no light, no glare; Jesus is not in this frame.",
        "scene": (
            "On the open road the group has stopped dead in mid-stride. One man has "
            "frozen with his foot still lifted and is staring down at his own hands; "
            "another has seized the arm of the man beside him; a third has stumbled "
            "half round to face the others with his mouth open. Their staffs are "
            "dropping. Nothing whatever is happening in the air around them — it is an "
            "ordinary dusty road in ordinary sunlight. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r014-b18", "out": "s18-the-linen-fell.jpeg", "seg": "n7 p1-p2",
        "window": "102.15-105.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEPERS"],
        "narration": "The linen loosened and fell. New skin underneath.",
        "must_show": "⚠️ THE TURN: grey wrappings unwinding and dropping off a forearm and hand, and CLEAN WHOLE SKIN beneath — healthy, unmarked, ordinary.",
        "must_not_show": "no light, glow or shimmer anywhere; the new skin is simply normal skin. Do not put Jesus in this frame.",
        "scene": (
            "Close on a man's forearm and hand in hard daylight as the strips of worn "
            "grey linen unwind and fall away from it, one length already dropping "
            "loose toward the ground. The skin underneath is CLEAN, whole and "
            "completely ordinary — healthy sun-browned skin with normal creases at "
            "the knuckles, entirely unmarked. His other hand is pulling the last strip "
            "free. Nothing is shining. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r014-b19", "out": "s19-nine-ran-on.jpeg", "seg": "n7 p3",
        "window": "105.73-112.03", "wide": True, "jesus": False, "ref": False,
        "locks": ["LEPERS", "BORDERLAND"],
        "narration": ("Nine of them ran on toward the city, toward the priests, toward "
                      "their old lives handed back."),
        "must_show": "nine men running hard up the road away from the camera toward the distant city, bare-handed and unwrapped, fallen linen scattered on the road behind them.",
        "must_not_show": "they are not doing anything wrong — this is joy; do not put Jesus in this frame.",
        "scene": (
            "THE CAMERA STANDS ON THE ROAD BEHIND THEM AND THEY ARE ALL RUNNING "
            "DIRECTLY AWAY FROM IT: the viewer sees NINE BACKS — nine sets of "
            "shoulders, nine heads of hair, the soles of lifted feet kicking up "
            "toward the lens — and NOT ONE FACE, because not one man has turned "
            "round. They are running flat out up the dusty road toward the distant "
            "walled city ahead of them, which stands small on its hill at the top of "
            "the frame. Count them: exactly nine men, separated on the open road so "
            "each one can be counted, and nobody else. Their hands are bare and "
            "clean, and their discarded grey linen strips lie scattered in the dust "
            "in the near foreground between the camera and their heels. Hard bright "
            "daylight. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r014-b20", "out": "s20-but-one-of-them-stopped.jpeg", "seg": "n7 p4",
        "window": "112.03-116.72", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "BORDERLAND"],
        # image anchor: b21 came back as the right man, b20 as a different,
        # younger, black-bearded one. Text alone did not hold him.
        "char_refs": ["assets-realistic/s21-he-turned-around.jpeg"],
        "narration": ("But one of them, when he saw what had happened to him, stopped "
                      "in the road."),
        "must_show": "the one man standing motionless in the middle of the road staring at his own bare hands, with the nine already small in the distance ahead of him.",
        "must_not_show": "do not put Jesus in this frame; the distance between him and the nine must be visible and growing.",
        "scene": (
            "One man stands completely motionless in the middle of the empty dusty "
            "road, both bare hands held up open in front of his face, staring down at "
            "them so his eyes leave the picture through the BOTTOM edge, well below "
            "the camera. HE IS THE MAN IN THE ATTACHED REFERENCE PHOTOGRAPH — the "
            "same weather-beaten face about forty, the same strong bony features and "
            "deep-set dark eyes under heavy black brows, the same rough black beard "
            "gone grey at the chin, the same thinning dark hair, the same faded "
            "deep-teal cloth knotted at his shoulder. Far up the road "
            "ahead of him the nine are already small with distance, still running "
            "away toward the city and not looking back. Discarded grey linen lies in "
            "the dust around his feet. Hard daylight. He has two arms, two hands and "
            "one head."
        ),
    },
    # ---------------------------------------------------- n8 — he came back ----
    {
        "id": "v2-r014-b21", "out": "s21-he-turned-around.jpeg", "seg": "n8 p1",
        "window": "116.72-117.72", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAMARITAN"],
        "narration": "And he turned around.",
        "must_show": "close on him mid-turn — head and shoulders coming round, away from the city and back the way he came.",
        "must_not_show": "do not put Jesus in this frame; the turn must be unmistakable.",
        "scene": (
            "Close on the Samaritan caught mid-turn in the road, his head and "
            "shoulders swinging round and his weight already shifting onto the back "
            "foot, his bare hands still half raised. His face is coming round toward "
            "the camera with something enormous arriving on it. The blurred empty road "
            "and the distant city are behind him. He has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r014-b22", "out": "s22-running-and-praising.jpeg", "seg": "n8 p2",
        "window": "117.72-125.03", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "BORDERLAND"],
        "narration": ("He came back the way he came, running, praising God at the top "
                      "of his voice — the whole road hearing it."),
        "must_show": "him running BACK toward the camera down the road, arms up, head back, shouting — running the opposite way from the nine.",
        "must_not_show": "do not put Jesus in this frame; his direction must plainly be the reverse of b19.",
        "scene": (
            "The Samaritan runs hard back down the dusty road TOWARD the camera, both "
            "bare arms flung up above his head, his head thrown back and his mouth "
            "wide open shouting at the sky as he runs. The deep-teal cloth streams off "
            "his shoulder. Far behind him in the opposite direction the road runs away "
            "empty toward the distant city where the others went. Dust bursts up "
            "behind his heels. Hard daylight. He has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------- n9 — at his feet ----
    {
        "id": "v2-r014-b23", "out": "s23-face-down-at-his-feet.jpeg", "seg": "n9 p1",
        "window": "125.03-129.21", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SAMARITAN", "DISCIPLES", "BORDERLAND"],
        "narration": ("He threw himself face-down in the dust at Jesus's feet and poured "
                      "out his thanks."),
        "must_show": "SCRIPTURE-EXACT (v16): FACE DOWN, full length in the dust at Jesus's feet — and note this is the first time anyone has come close to him.",
        "must_not_show": "no halo, glare or rim-light; nobody is pulling him back or keeping distance from him now.",
        "scene": (
            "The Samaritan has thrown himself full length FACE DOWN in the dust of the "
            "road at Jesus's feet, arms stretched out ahead of him, his forehead "
            "against the ground, his shoulders shaking. Jesus stands over him looking "
            "down, and the disciples have gathered round in a ring, close, none of "
            "them keeping any distance at all. Dust hangs in the hard bright light "
            "around them. The camera is back far enough to see the prostrate man and "
            "Jesus head to sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r014-b24", "out": "s24-he-was-a-samaritan.jpeg", "seg": "n9 p2",
        "window": "129.21-135.38", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "DISCIPLES"],
        "narration": ("And Luke adds one detail that would have stunned everyone "
                      "listening: he was a Samaritan."),
        "must_show": "the detail landing on the watching disciples — recognition on their faces that the man in the dust is a Samaritan.",
        "must_not_show": "nobody is hostile to him; it is surprise, not contempt. Do not put Jesus in this frame.",
        "scene": (
            "Close on the faces of three or four disciples standing in the ring, "
            "looking down at the man prostrate in the dust. Recognition is moving "
            "across them — one's eyebrows have gone up and his lips parted, another "
            "has turned to look at the man beside him, a third's head has tilted as "
            "something reorders itself behind his eyes. None of them looks hostile; "
            "they look rearranged. The teal-clothed shoulder of the man on the ground "
            "is at the frame's lower edge. Hard daylight. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        # NEW (2026-08-01 re-time audit): n9 p3-p4 had no picture of its own —
        # b24 was holding one frame across 11.9 s of narration.
        "id": "v2-r014-b24b", "out": "s24b-the-one-who-did-not-belong.jpeg",
        "seg": "n9 p3-p4",
        "window": "135.38-141.14", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "DISCIPLES"],
        "narration": ("The outsider. The one the religion of the day said did not "
                      "belong."),
        "must_show": "the outsider alone on the ground — one man face-down in the dust with the ring of Galilean men standing over him, the difference between him and them plain.",
        "must_not_show": "nobody is sneering or turning away; do not put Jesus in this frame.",
        "scene": (
            "The camera stands behind and just above the shoulders of two disciples "
            "at the near edge of the ring, looking steeply DOWN past them at the "
            "Samaritan lying full length face-down in the pale dust of the road, the "
            "faded deep-teal cloth across his back, his arms stretched out ahead of "
            "him. The disciples' faces are turned down toward him and their eyes exit "
            "the picture through the bottom edge, well below the camera. He is small "
            "on the wide bare ground and completely alone in the middle of the open "
            "circle they have left around him. Hard bright afternoon daylight, long "
            "shadows across the dust, shallow depth of field on the near shoulders. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    # --------------------------------------------------- n10 / j2 — the nine ----
    {
        "id": "v2-r014-b25", "out": "s25-the-empty-road.jpeg", "seg": "n10",
        "window": "141.14-145.54", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BORDERLAND"],
        "narration": ("Jesus looked at the empty road where the other nine had gone, "
                      "and asked:"),
        "must_show": "Jesus looking away up the long EMPTY road toward the city — nobody on it at all.",
        "must_not_show": "no halo, glare or rim-light; the road must be completely empty — the absence is the picture.",
        "scene": (
            "Jesus has turned his head and is looking away up the long dusty road that "
            "runs off toward the distant walled city. The road is completely empty — "
            "not one figure anywhere along its whole length, only dust, stones and the "
            "scattered grey linen strips lying where they fell. His face is quiet and "
            "something in it has gone sad. The camera is behind and beside him so both "
            "his face and the empty road are in frame. He has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r014-b26", "out": "s26-where-are-the-nine.jpeg", "seg": "j2 p1-p2",
        "window": "145.54-149.06", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Were there not ten cleansed? but where are the nine? "
                      "(Luke 17:17)"),
        "must_show": "⚠️ close on Jesus asking — the question is GRIEF, not anger. Puzzled, sad, wanting them there.",
        "must_not_show": "NOT indignant, NOT wounded pride, NOT a rebuke. The narration says outright it is grief and the nine did nothing wrong. If this face reads as offended, regenerate. No halo or rim-light.",
        "scene": (
            "Close on Jesus in the hard daylight as he asks. THE CAMERA IS SET WELL "
            "OFF HIS EYELINE — low and to his right — and his head is turned three "
            "quarters away from it, so his eyes are searching far up the empty road "
            "and travel out of the picture through the UPPER LEFT edge, passing well "
            "clear of the lens; his pupils are never centred on the camera and he "
            "never acknowledges it. His brows are drawn up in the middle rather than "
            "down, his eyes are soft, and his mouth is open on the question with "
            "nothing hard in it at all. It is the face of someone who wanted the "
            "others there and is sorry they are not — plain grief, no offence "
            "anywhere in it. The empty road is soft behind him."
        ),
    },
    {
        "id": "v2-r014-b27", "out": "s27-save-this-stranger.jpeg", "seg": "j2 p3",
        "window": "149.06-156.30", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SAMARITAN", "DISCIPLES"],
        "narration": ("There are not found that returned to give glory to God, save this "
                      "stranger. (Luke 17:18)"),
        "must_show": "Jesus's open hand indicating the man still on the ground as he names him — presenting him to the watching disciples.",
        "must_not_show": "no halo, glare or rim-light; the word 'stranger' must be said warmly, not dismissively.",
        "scene": (
            "Jesus has turned back and his open hand is extended down toward the "
            "Samaritan still lying in the dust at his feet, presenting him to the men "
            "standing around. His face is warm as he speaks. The disciples' eyes "
            "follow his hand down to the man on the ground. Hard daylight, dust "
            "hanging. The camera is back far enough to hold Jesus, the prostrate man "
            "and the near disciples. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------- n11 — grief not scolding ----
    {
        "id": "v2-r014-b28", "out": "s28-this-outsider.jpeg", "seg": "n11 p1-p2",
        "window": "156.30-159.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAMARITAN"],
        "narration": "Except this stranger. This outsider.",
        "must_show": "close on the Samaritan's face lifted from the dust — wet, dirty, wide open with gratitude.",
        "must_not_show": "do not put Jesus in this frame.",
        "scene": (
            "Close on the Samaritan's face as he raises it from the ground. It is "
            "streaked with dust and running with tears, his black brows drawn up, his "
            "mouth open and working, his deep-set dark eyes fixed upward and blazing "
            "with gratitude. Grit is stuck to his forehead and cheek. Hard daylight "
            "full on him. He has one head."
        ),
    },
    {
        "id": "v2-r014-b29", "out": "s29-the-nine-did-nothing-wrong.jpeg", "seg": "n11 p3-p4",
        "window": "159.08-166.28", "wide": True, "jesus": False, "ref": False,
        "locks": ["LEPERS", "BORDERLAND"],
        "narration": ("This is not wounded pride — the nine did nothing wrong. They "
                      "obeyed, and they were healed, every one of them."),
        "must_show": "the nine far away arriving at the city gate — happy, obedient, doing exactly what they were told; they are not villains.",
        "must_not_show": "nothing sinister about them at all; they must look glad and innocent. Do not put Jesus in this frame.",
        "scene": (
            "THE CAMERA STANDS ON THE ROAD OUTSIDE THE CITY, WELL BACK, AND THE NINE "
            "ARE BETWEEN IT AND THE GATE, MOVING AWAY FROM IT AND IN THROUGH THE "
            "ARCHWAY: the viewer sees them from behind, backs and shoulders and the "
            "soles of their sandals, the leading two already under the shadow of the "
            "stone arch and the last still in the sunlight on the road. Not one of "
            "them has turned round, so no face is toward the lens. They are "
            "clean-handed and unwrapped and plainly delighted — one has his arms up, "
            "another has a hand on a companion's back — doing exactly what they were "
            "told to do. The great pale wall and the open gateway fill the top of the "
            "frame above them. Hard afternoon light on the stone. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r014-b30", "out": "s30-they-missed-the-giver.jpeg", "seg": "n11 p5",
        "window": "166.28-173.33", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BORDERLAND"],
        "narration": ("His question is grief, not a scolding: they got the gift and kept "
                      "walking, and they missed the giver."),
        "must_show": "⚠️ SCALE + direction: Jesus large in the near foreground with his back three-quarters to the camera, and the nine already tiny far up the road, walking AWAY and not one of them looking back.",
        "must_not_show": "⚠️ HARD FAIL if any of the nine is near the height of Jesus in the frame, or if any of them is facing back toward him. No halo, glare or rim-light.",
        "scene": (
            "The camera stands behind and to one side of Jesus at shoulder height, so "
            "he fills the near left of the frame from waist to head with his back "
            "three-quarters turned, and the long dusty road runs away past him into "
            "the distance. Far up that road the nine are TINY — each of them no taller "
            "in the frame than the width of Jesus's hand, small specks with distance — "
            "walking away toward the far walled city with their backs to him, not one "
            "head turned round. His face is in quarter profile, his eyes following "
            "them up the road and out of the picture through the far edge, past the "
            "camera and well to the side of it. Discarded grey linen strips lie in the "
            "dust in the near foreground. Hard bright afternoon light, heat shimmer "
            "over the empty ground. Every figure has two arms, two hands and one head."
        ),
    },
    {
        # NEW (2026-08-01 re-time audit): n11 p6 had no picture of its own —
        # b30 was holding one frame across 11.5 s of narration.
        "id": "v2-r014-b30b", "out": "s30b-came-back-to-find-him.jpeg", "seg": "n11 p6",
        "window": "173.33-177.80", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SAMARITAN", "BORDERLAND"],
        "narration": ("Only the one everyone counted out came back to find him."),
        "must_show": "the two of them together on the empty road — the one man who came back and the man he came back to, with the whole empty distance behind them.",
        "must_not_show": "no halo, glare or rim-light; nothing triumphant — it is quiet.",
        "scene": (
            "Jesus stands on the empty dusty road with the Samaritan kneeling up in "
            "front of him now, the two of them alone in the middle of a wide empty "
            "landscape, and the long road runs away behind them toward the far city "
            "with nobody on it. The disciples stand back a little at the frame's edge. "
            "It is quiet and small and there is nothing triumphant about it. Hard "
            "afternoon light. The camera is back far enough to hold both men head to "
            "sandals and the empty road beyond. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    # -------------------------------------------------- n12 / j3 — arise ----
    {
        "id": "v2-r014-b31", "out": "s31-he-reached-down.jpeg", "seg": "n12",
        "window": "177.80-183.26", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SAMARITAN"],
        "narration": ("Then Jesus reached down to the man still trembling at his feet, "
                      "and lifted him with a word:"),
        "must_show": "⚠️ TOUCH — Jesus's hand taking hold of the man's bare hand and forearm to lift him; the first hand that has touched him in years.",
        "must_not_show": "no halo, glare or rim-light; the touch must be firm and ordinary, skin on skin — the significance is that it happens at all.",
        "scene": (
            "Close on two hands and forearms meeting in hard daylight. Jesus has "
            "reached right down and closed his hand firmly around the Samaritan's bare "
            "hand and wrist, gripping to lift him, and the man's other hand has come "
            "up to clutch at Jesus's forearm. The grip is solid and completely "
            "ordinary — plain skin on plain skin, dust on both. Nothing is happening "
            "in the air. The kneeling man's dusty shoulder and the teal cloth are just "
            "in frame. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r014-b32", "out": "s32-thy-faith-hath-made-thee-whole.jpeg", "seg": "j3",
        "window": "183.26-188.62", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SAMARITAN"],
        "narration": ("Arise, go thy way: thy faith hath made thee whole. (Luke 17:19)"),
        "must_show": "the man coming up onto his feet with Jesus's hand still holding him — the two of them face to face and level.",
        "must_not_show": "no halo, glare or rim-light; he is not kneeling any more — the word 'arise' has to be visible in the frame.",
        "scene": (
            "The Samaritan has come up onto his feet with Jesus's hand still holding "
            "his, and the two men stand face to face and level with each other on the "
            "dusty road, close. Jesus is speaking, his face warm and glad. The man's "
            "dirty tear-streaked face is turned up to his, mouth open. Their joined "
            "hands are between them. Hard afternoon light. The camera is back far "
            "enough to see both men head to sandals. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    # ------------------------------------------ n13 — cleansed vs whole ----
    {
        "id": "v2-r014-b33", "out": "s33-all-ten-were-cleansed.jpeg", "seg": "n13 p1-p2",
        "window": "188.62-194.37", "wide": True, "jesus": False, "ref": False,
        "locks": ["BORDERLAND"],
        "narration": ("Hear the two different words. All ten were cleansed — out on the "
                      "road, before any of them said thank you."),
        "must_show": "the stretch of road where it happened, empty now, with the discarded grey linen strips lying scattered in the dust — ten men's worth.",
        "must_not_show": "no people at all; the abandoned wrappings tell it. Do not put Jesus in this frame.",
        "scene": (
            "A wide view of the empty stretch of dusty road where they were walking. "
            "Scattered all across it lie the discarded strips of worn grey linen — "
            "many of them, from many hands, some caught on stones, one lifting a "
            "little in the breeze, a dropped staff among them. There is not a single "
            "person anywhere in the frame. Hard afternoon light and long dust."
        ),
    },
    {
        "id": "v2-r014-b34", "out": "s34-cleansed-and-whole.jpeg", "seg": "n13 p3-p5",
        "window": "194.37-203.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAMARITAN"],
        "narration": ("But only this one, the one who came back, was made whole. "
                      "Cleansed happened to his skin. Whole happened to all of him."),
        "must_show": "close on the Samaritan's face — the difference is entirely in it: settled, unburdened, present, a man put back together.",
        "must_not_show": "do not put Jesus in this frame; nothing about his skin is the subject now — his face is.",
        "scene": (
            "Close on the Samaritan's face in warm afternoon light. The tears have "
            "stopped and something has settled in him completely — his shoulders have "
            "come down, his jaw has loosened, his deep-set dark eyes are clear and "
            "steady and entirely present. It is the face of a man who has been put "
            "back together rather than merely repaired. Dust still on his skin and "
            "beard. The open country is soft behind him."
        ),
    },
    {
        "id": "v2-r014-b35", "out": "s35-he-walked-home-a-whole-man.jpeg", "seg": "n14",
        "window": "203.85-209.51", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "BORDERLAND"],
        "narration": ("And he rose and walked home a whole man, the old wrappings left "
                      "behind him in the road."),
        "must_show": "the closing frame: him walking away up the road with his back straight and his hands bare and swinging free, and his grey wrappings lying in the dust behind him.",
        "must_not_show": "do not put Jesus in this frame; the wrappings must be plainly visible behind him and plainly abandoned.",
        "scene": (
            "SHOT FROM BEHIND AND BESIDE HIM: the Samaritan walks away up the dusty "
            "road into the open country, his back straight, his head up, both bare "
            "hands swinging free and empty at his sides. On the road in the near "
            "foreground behind him lie his discarded strips of grey linen, crumpled in "
            "the dust where he left them, with his dropped staff beside them. The road "
            "ahead of him runs on into warm afternoon light and low hills. He has two "
            "arms, two hands and one head."
        ),
    },
]
