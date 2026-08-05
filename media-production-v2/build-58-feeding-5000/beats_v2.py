#!/usr/bin/env python3
"""V2 beat map — row 58, build-58-feeding-5000 (John 6:1-14).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 24 pictures over 135.5 s narration = 5.6 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (John 6:1-14 KJV; Matt 14:21 for
the count "besides women and children"):
  v2   a GREAT MULTITUDE followed him, because they saw his miracles on
       them that were diseased.
  v3   he went up into A MOUNTAIN beside the sea of Galilee and sat with
       his disciples. v10: there was MUCH GRASS in the place — a green
       spring hillside, not brown desert.
  v5   Jesus LIFTED UP HIS EYES and saw a great company COME UNTO HIM —
       he asks PHILIP: "Whence shall we buy bread, that these may eat?"
  v6   he said this TO PROVE HIM: "for he himself KNEW WHAT HE WOULD DO."
       The knowing face (b07) is doctrine, not decoration.
  v8-9 ANDREW, Simon Peter's brother, brings the LAD: "five BARLEY loaves,
       and two SMALL fishes: but what are they among so many?" Barley =
       the poor man's bread; the smallness is the point.
  v10  "Make the men sit down." They sat, ABOUT FIVE THOUSAND men (besides
       women and children — Matt 14:21); Mark 6:39-40 adds: in GROUPS on
       the GREEN grass.
  v11  he took the loaves; when he had GIVEN THANKS, he distributed to the
       disciples, and the disciples to them that were set down — the food
       travels through the disciples' hands; the multiplying is never
       shown as an effect, only as abundance that keeps arriving.
  v12  "Gather up the fragments that remain, that nothing be lost."
  v13  TWELVE BASKETS with the fragments — more at the end than the start.
  v14  "This is of a truth that prophet that should come into the world."

CONTENT-CARE: row 58 is not in the §3 flag table = GREEN.

TIME-OF-DAY ARC: the text fixes it — a full day of teaching, then "when
even was come" the feeding: bright afternoon for b01-b02, the sun visibly
sinking from b03, the feeding and gathering in golden evening light, the
closing at dusk. Never full night.

CAST-REF NOTE: when the first still with the boy's face is ACCEPTED at QC,
copy it to CAST-REF-V2/lad-ref.jpeg and add
"char_refs": ["CAST-REF-V2/lad-ref.jpeg"] to b09-b11 and b22. Same for
Andrew (andrew-ref.jpeg) and Philip (philip-ref.jpeg). Text locks alone do
not hold a face.
"""

LOCKS = {
    "ANDREW": (
        "ANDREW LOCK: Andrew is the same man in every shot — about "
        "thirty, lean and wiry, olive-brown weathered skin, straight "
        "dark hair, a short trimmed dark beard, a ready open face. He "
        "wears a DARK SEA-GREEN-GREY wool tunic with a plain leather "
        "belt; never cream, never white. His face is shown clearly."
    ),
    "PHILIP": (
        "PHILIP LOCK: Philip is the same man in every shot — about "
        "thirty, round-faced and earnest, short dark curly hair and a "
        "close dark beard, the careful brow of a man who counts things. "
        "He wears a DARK WALNUT-BROWN wool tunic with a rope belt; never "
        "cream, never white. His face is shown clearly."
    ),
    "LAD": (
        "LAD LOCK: the boy is the same child in every shot — about ten, "
        "skinny and quick, sun-browned, a mop of dark curls, bright dark "
        "eyes. He wears a small patched DARK OCHRE-BROWN wool tunic with "
        "a rope belt, barefoot, and carries a small woven rush basket "
        "holding FIVE small flat round barley loaves — coarse, dark, "
        "poor man's bread — and TWO small dried fish. Never cream, "
        "never white. His face is shown clearly."
    ),
    "HILLSIDE": (
        "HILLSIDE LOCK: a broad GREEN grassy hillside sloping down to "
        "the Sea of Galilee — spring grass thick underfoot, grey "
        "outcrops, the blue lake below and dry hills across the water; "
        "no town anywhere in sight. The multitude are ordinary Galilean "
        "families in SATURATED DEEP earth colours — dark chocolate "
        "brown, deep russet, burnt ochre, dark olive and dusty indigo "
        "wool — every garment plainly darker than the bright grass and "
        "sky; no one in the crowd wears cream, off-white, ivory or any "
        "pale near-white cloth."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the disciples moving through the crowd wear "
        "plain work tunics in the same deep saturated earth wools as "
        "the crowd — dark charcoal-brown, deep russet, dark olive, "
        "dusty indigo — with plain leather or rope belts; none of them "
        "wears cream, off-white or any pale near-white cloth."
    ),
}

REF = True

# Identity law: pin the named disciples to the global sheets (token
# names never auto-attach — the Lazarus trap).
REFS = {
    "ANDREW": ["../CAST-V2-REF/andrew-front.jpeg", "../CAST-V2-REF/andrew-quarter.jpeg"],
    "PHILIP": ["../CAST-V2-REF/philip-front.jpeg", "../CAST-V2-REF/philip-quarter.jpeg"],
}

BEATS = [
    {
        "id": "v2-r058-b01", "out": "s01-the-crowd-followed.jpeg", "seg": "n1 p1",
        "window": "0.28-7.32", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": ("A huge crowd had followed Jesus to a lonely green "
                      "hillside beside the lake, hungry to hear him and "
                      "to be healed."),
        "must_show": "v2-v3 — the scale: the multitude streaming up the green slope from every side toward Jesus.",
        "must_not_show": "no halo/glow; the crowd's convergence on him is the composition.",
        "scene": (
            "Across the broad green hillside above the blue lake, the "
            "camera high on the shoulder of the slope behind the "
            "climbing streams, "
            "the multitude comes streaming up the slope in long "
            "moving lines — families with bundles, men carrying "
            "their sick on litters, children running ahead through "
            "the spring grass — all of the lines converging on the "
            "one place where Jesus stands among his disciples on a "
            "grey outcrop, waiting for them. Bright afternoon over "
            "the water. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r058-b02", "out": "s02-he-cared-for-them-all-day.jpeg", "seg": "n1 p2a",
        "window": "7.32-11.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": "He taught them and cared for them all day,",
        "must_show": "the long day's work — Jesus teaching seated among the packed hillside, a healed child on a father's shoulders nearby.",
        "must_not_show": "he is IN the crowd, at their level on the grass, not above them.",
        "scene": (
            "Jesus sits on the grass in the thick of the seated "
            "multitude, mid-teaching, one hand moving with the "
            "words — the nearest families cross-legged an arm's "
            "length away, an old woman leaning in with her hand "
            "cupped at her ear, a father just behind him hoisting a "
            "laughing child who was carried up the hill this "
            "morning — the whole slope packed with listening people "
            "in deep russet, olive and indigo wool. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r058-b03", "out": "s03-the-sun-began-to-sink.jpeg", "seg": "n1 p2b",
        "window": "11.00-15.59", "wide": True, "jesus": False, "ref": False,
        "locks": ["HILLSIDE"],
        "narration": ("until the sun began to sink and they were a long "
                      "way from any town or food."),
        "must_show": "the problem arriving with the light — the sun low over the lake, the vast crowd shadowed long, no town anywhere.",
        "must_not_show": "the emptiness of the horizon matters — no roofs, no smoke, nothing to eat for miles.",
        "scene": (
            "The sun stands low and golden over the Sea of Galilee, "
            "the camera taking the shadowed slope from the side, "
            "and the whole vast seated multitude throws long shadows "
            "up the green slope — thousands of small dark figures "
            "spread across the hillside in the honeyed light — and "
            "in every direction beyond them the land rolls away "
            "empty: no town, no road, no smoke, just grass, rock, "
            "water and evening coming. An upright vertical "
            "photograph, the ground at the bottom of the frame and "
            "the sky at the top, the horizon level — the picture is "
            "the right way up."
        ),
    },
    {
        "id": "v2-r058-b04", "out": "s04-the-disciples-grew-anxious.jpeg", "seg": "n2 p1",
        "window": "15.59-17.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANDREW", "PHILIP", "DISCIPLES"],
        "narration": "His disciples grew anxious as the light went.",
        "must_show": "the worry conference — disciples' heads together, glances at the sun, at the crowd, at each other.",
        "must_not_show": "practical men doing grim arithmetic — not panic, but no answer either.",
        "scene": (
            "A knot of disciples stands a little apart in the "
            "golden light, heads bent together — Philip counting "
            "something out on his fingers with a grim mouth, Andrew "
            "glancing from the sinking sun to the endless seated "
            "crowd and back, another scrubbing a hand through his "
            "beard — working men running out of daylight and "
            "arithmetic at the same time. Exactly four people are "
            "in the frame; each has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r058-b05", "out": "s05-he-turned-it-back-on-them.jpeg", "seg": "n2 p2-p3",
        "window": "17.99-24.01", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PHILIP", "HILLSIDE"],
        "narration": ("But Jesus turned it back on them. He looked up at "
                      "the crowd coming toward him and asked Philip:"),
        "must_show": "v5 — Jesus lifting his eyes to the still-arriving crowd, turning to Philip with the question forming.",
        "must_not_show": "more people are STILL coming up the hill — the problem is visibly growing as he asks.",
        "scene": (
            "Jesus has risen and stands looking out over the slope, "
            "where late-coming families are still climbing toward "
            "them out of the golden light in twos and threes — and "
            "he turns his head to Philip beside him, the beginning "
            "of the question on his face, one hand tipping open "
            "toward the arriving thousands, while Philip follows "
            "the gesture with visibly sinking heart. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r058-b06", "out": "s06-whence-shall-we-buy-bread.jpeg", "seg": "j5",
        "window": "24.01-28.20", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PHILIP"],
        "narration": ("Whence shall we buy bread, that these may eat? "
                      "(John 6:5)"),
        "must_show": "the question at close range — Jesus asking Philip directly; Philip's staggered face doing sums with no answer.",
        "must_not_show": "no worry anywhere on Jesus's face — the contrast between the two faces is the frame.",
        "scene": (
            "A close two-shot in the low gold light: Jesus asks it "
            "with his eyes steady on Philip and something almost "
            "playful resting behind the gravity of his face — and "
            "Philip stares back aghast, mouth half-open, a man being "
            "asked to price an impossibility, his hands starting to "
            "spread in helpless calculation. Exactly two people are "
            "in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r058-b07", "out": "s07-he-already-knew.jpeg", "seg": "n2b",
        "window": "28.20-36.69", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("He was not worried. John tells us plainly that he "
                      "already knew exactly what he was going to do — he "
                      "asked to see what Philip would say."),
        "must_show": "v6 — the knowing face alone: calm certainty with warmth in it; the teacher's patience while the student flounders.",
        "must_not_show": "no smugness — the knowing is kind; he is teaching, not toying.",
        "scene": (
            "Close on Jesus's face in the golden evening light: "
            "utterly untroubled, his warm eyes resting on the "
            "flustered man before him with the patient, faintly "
            "smiling steadiness of a teacher who has already "
            "prepared the lesson's answer and is letting the "
            "question do its work — certainty and kindness in the "
            "same expression. Exactly one person is in the frame, "
            "with one head."
        ),
    },
    {
        "id": "v2-r058-b08", "out": "s08-one-lunch.jpeg", "seg": "n3 p1",
        "window": "36.69-38.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAD", "HILLSIDE"],
        "narration": "There was only one lunch in the whole crowd.",
        "must_show": "the boy and his basket — small, clutched, the only food on a hillside of thousands.",
        "must_not_show": "he holds it the way a poor child holds food — close and carefully.",
        "scene": (
            "The skinny boy sits cross-legged in the grass amid the "
            "sea of grown-ups, his small rush basket held close "
            "against his chest with both arms — the five coarse "
            "dark barley loaves and two small dried fish just "
            "visible under the woven lid he keeps half-open, "
            "checking on his treasure — one small careful lunch on "
            "a hillside of thousands of empty hands. Golden light. "
            "Exactly one person is in the frame in focus, with two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r058-b09", "out": "s09-andrew-brought-him.jpeg", "seg": "n3 p2",
        "window": "38.79-45.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ANDREW", "LAD", "HILLSIDE"],
        "narration": ("Andrew, Simon Peter's brother, brought a boy to "
                      "Jesus, almost embarrassed to mention it."),
        "must_show": "v8 — the bringing: Andrew steering the boy through to Jesus with a hand on his shoulder, apology already on his face.",
        "must_not_show": "the boy is not shy — Andrew is the embarrassed one; the boy holds his basket up ready.",
        "scene": (
            "Andrew steers the small boy through the seated crowd "
            "toward Jesus with one hand on the child's shoulder, "
            "his own face already half-apologizing for the "
            "smallness of what he brings — while the boy marches "
            "ahead of him entirely unembarrassed, chin up, holding "
            "his little rush basket out in front of him with both "
            "hands like a gift he has decided to give. Golden "
            "evening light. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r058-b10", "out": "s10-five-loaves-two-fishes.jpeg", "seg": "s9",
        "window": "45.27-53.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ANDREW", "LAD"],
        "narration": ("There is a lad here, which hath five barley "
                      "loaves, and two small fishes: but what are they "
                      "among so many? (John 6:9)"),
        "must_show": "v9 — the presentation: the basket held open toward Jesus, Andrew's helpless shrug, Jesus looking at the offering with full seriousness.",
        "must_not_show": "Jesus receives the small gift with the gravity of a great one — no amusement at its size.",
        "scene": (
            "The boy holds his basket open up toward Jesus — five "
            "flat dark barley loaves and two small dried fish plain "
            "to see — while Andrew beside him spreads one hand at "
            "the seated thousands in a helpless shrug, the question "
            "on his face — and Jesus bends toward the basket and "
            "the boy with complete unhurried seriousness, receiving "
            "the smallest lunch in Galilee like a treasury. Exactly "
            "three people are in the frame; each has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r058-b11", "out": "s11-the-poor-mans-bread.jpeg", "seg": "n3b",
        "window": "53.27-61.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAD"],
        "narration": ("Barley was the poor man's bread. It was the "
                      "smallest, cheapest lunch on that whole hillside, "
                      "and it was the only thing anybody offered."),
        "must_show": "the offering itself close — the five coarse loaves and two small fish in the boy's hands; poverty and generosity in one image.",
        "must_not_show": "the bread is coarse, dark, small — honest barley, nothing appetizing about it but the giving.",
        "scene": (
            "Close down into the rush basket held in the boy's "
            "small brown hands: five flat round barley loaves, "
            "coarse and dark and no bigger than his palms, and two "
            "small stiff dried fish tucked beside them — the whole "
            "wealth of a poor family's child, held out steadily in "
            "the golden light by the only person on the hillside "
            "who offered anything at all. Exactly one person is in "
            "the frame; each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r058-b12", "out": "s12-not-troubled-by-little.jpeg", "seg": "n4 p1-p2",
        "window": "61.57-66.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LAD"],
        "narration": ("Jesus was not troubled by how little there was. "
                      "He said simply:"),
        "must_show": "Jesus receiving the basket from the boy's hands into his own — the transfer, both sets of hands on it.",
        "must_not_show": "he takes it like an abundance; the boy's face at giving it away is part of the frame.",
        "scene": (
            "The handover: Jesus takes the little basket from the "
            "boy's lifted hands into his own two hands, bending so "
            "their eyes meet over it — the child's face bright and "
            "serious at once, watching his whole lunch leave his "
            "keeping — and Jesus's face above the basket wears "
            "plain unworried gladness, a man being handed exactly "
            "enough. Exactly two people are in the frame; each "
            "visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r058-b13", "out": "s13-make-the-men-sit-down.jpeg", "seg": "j10",
        "window": "66.27-69.52", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "HILLSIDE"],
        "narration": "Make the men sit down. (John 6:10)",
        "must_show": "the order going out — Jesus with the basket, disciples turning to fan out across the slope with the instruction.",
        "must_not_show": "the disciples obey without understanding — their faces still carry the question.",
        "scene": (
            "Jesus stands with the small basket held easily in one "
            "arm and gives the instruction, his free hand sweeping "
            "the slope — and the disciples are already turning out "
            "of the huddle to obey, Andrew and Philip and the "
            "others fanning off in different directions across the "
            "hillside, arms rising to signal the crowd down into "
            "the grass, obedience running ahead of comprehension "
            "on every face. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r058-b14", "out": "s14-they-sat-in-groups.jpeg", "seg": "n4b",
        "window": "69.52-77.67", "wide": True, "jesus": False, "ref": False,
        "locks": ["HILLSIDE"],
        "narration": ("And they settled in groups on the green grass, "
                      "five thousand men, besides women and children, "
                      "waiting to see what he would do."),
        "must_show": "v10 / Mark 6:40 — the ordering of the multitude: distinct settled groups patterning the green slope in the low gold light.",
        "must_not_show": "groups, not one mass — the crowd resolves into ordered companies; expectant faces toward one point.",
        "scene": (
            "The whole hillside settles, the camera above the slope "
            "behind the nearest seated ranks: the multitude arranges "
            "itself into distinct seated companies across the deep "
            "green grass — group after group after group, patterned "
            "up the slope like beds in a vast garden, russet and "
            "olive and indigo wool in the low golden light — "
            "thousands of faces all turned expectantly toward the "
            "one small standing figure with a basket, waiting. An "
            "upright vertical photograph, the ground at the bottom "
            "of the frame and the sky at the top, the horizon "
            "level — the picture is the right way up."
        ),
    },
    {
        "id": "v2-r058-b15", "out": "s15-he-blessed-and-brake.jpeg", "seg": "nbless",
        "window": "77.67-84.42", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Then he took the five loaves and the two fish, "
                      "and looking up to heaven, he gave thanks, and "
                      "broke the bread."),
        "must_show": "v11 — THE picture of the build: the loaves lifted in his hands, his face raised to heaven in thanks, the first loaf breaking.",
        "must_not_show": "no light effect, no multiplication shown — thanksgiving and breaking, nothing else; the sky is plain evening sky.",
        "scene": (
            "Jesus stands against the deepening gold of the evening "
            "sky with the coarse barley loaves gathered up in both "
            "hands, his face lifted fully to heaven, eyes closed "
            "mid-thanks — and his thumbs are already breaking the "
            "first small dark loaf open at its middle — a man "
            "giving thanks over almost nothing as though it were "
            "everything, the little basket with the fish at his "
            "feet in the grass. Exactly one person is in the frame, "
            "with two arms, two hands of five fingers each and one "
            "head."
        ),
    },
    {
        "id": "v2-r058-b16", "out": "s16-it-did-not-run-out.jpeg", "seg": "n5 p1",
        "window": "84.42-85.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["DISCIPLES"],
        "narration": "And the food did not run out.",
        "must_show": "the first astonishment — a disciple's basket being loaded again, his face failing to keep up with what his hands keep receiving.",
        "must_not_show": "no effect at the bread — the abundance shows only in the arithmetic of full hands.",
        "scene": (
            "Close on a disciple's wide flat basket as broken bread "
            "and fish are heaped into it yet again — his "
            "rope-scarred hands steadying under a weight that "
            "should have ended long ago — and above the basket his "
            "bearded face is caught mid-glance backward, disbelief "
            "wrestling arithmetic, a working man's mind refusing "
            "the evidence of his own forearms. Exactly two people "
            "are in the frame; each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r058-b17", "out": "s17-carried-through-the-crowd.jpeg", "seg": "n5 p2a",
        "window": "85.83-91.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["DISCIPLES", "HILLSIDE"],
        "narration": ("The disciples carried it through the crowd, and "
                      "it kept coming, bread and fish, more and more,"),
        "must_show": "v11 — the distribution: disciples moving between the seated groups with heaped baskets, hands reaching up from the grass.",
        "must_not_show": "the food travels through human hands — basket to hand to hand; no other mechanism visible.",
        "scene": (
            "The disciples move through the seated companies with "
            "heaped baskets on hips and shoulders — Andrew crouching "
            "to fill an old woman's held-out shawl, Philip passing "
            "loaves down a chain of lifted hands, children reaching "
            "up from the grass — lanes of distribution threading "
            "the patterned multitude in the low golden light, and "
            "every basket still heaped no matter how much leaves "
            "it. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r058-b18", "out": "s18-all-were-filled.jpeg", "seg": "n5 p2b",
        "window": "91.00-97.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE"],
        "narration": ("until every single person there had eaten as much "
                      "as they wanted, and was full."),
        "must_show": "the satisfaction — families eating their fill in the golden dusk; ease and plenty where anxiety was.",
        "must_not_show": "contentment, not gluttony — bread in every hand, unhurried; the evening finally kind.",
        "scene": (
            "Across the darkening gold of the hillside the "
            "multitude eats in peace: a family passing fish along "
            "their row, a father tearing bread for the small hands "
            "around him, an old man chewing slow with his eyes on "
            "the sunset water, a mother wiping her toddler's "
            "chin — thousands fed to the brim on a hillside that "
            "held one lunch an hour ago. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r058-b19", "out": "s19-gather-the-fragments.jpeg", "seg": "jv12",
        "window": "97.63-102.94", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "HILLSIDE"],
        "narration": ("Gather up the fragments that remain, that nothing "
                      "be lost. (John 6:12)"),
        "must_show": "v12 — the instruction: Jesus directing the disciples out over the fed crowd, empty baskets being taken up.",
        "must_not_show": "the God of abundance is also the God of no waste — the care in the command must read.",
        "scene": (
            "Jesus stands among the fed and resting crowd in the "
            "last gold of the light, one hand sweeping the "
            "scattered slope as he gives the instruction — and the "
            "disciples are taking up empty baskets and moving out "
            "over the hillside, bending already to the first "
            "broken pieces in the grass, stewards sent to honour "
            "the abundance down to its crumbs. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r058-b20", "out": "s20-every-scrap.jpeg", "seg": "n6 p1-p2",
        "window": "102.94-107.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["DISCIPLES", "HILLSIDE"],
        "narration": ("Pick up every scrap that's left, he said. Let "
                      "nothing go to waste."),
        "must_show": "the gleaning — disciples stooped among the seated groups, baskets filling with broken pieces; families handing up their leftovers.",
        "must_not_show": "the crowd helps — leftovers passed hand to hand into the baskets; nothing ordered, everything given.",
        "scene": (
            "In the blue-gold dusk the disciples work stooped "
            "through the companies, baskets on their arms filling "
            "with broken bread — a woman leaning over to add her "
            "family's uneaten pieces, a child solemnly carrying "
            "one crust to the nearest basket, Andrew laughing at "
            "the weight already on his arm — a whole hillside "
            "honouring its miracle by keeping its crumbs. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r058-b21", "out": "s21-twelve-baskets.jpeg", "seg": "n6 p3",
        "window": "107.92-114.21", "wide": True, "jesus": False, "ref": False,
        "locks": ["DISCIPLES", "HILLSIDE"],
        "narration": ("So they went through the crowd and gathered what "
                      "was left, and filled twelve baskets with the "
                      "broken pieces."),
        "must_show": "v13 — the count made visible: EXACTLY TWELVE baskets, heaped full, set in a line on the grass in the dusk.",
        "must_not_show": "count discipline: twelve baskets, no more, no fewer — the row must be countable at a glance.",
        "scene": (
            "On the trampled grass in the deep-gold dusk, the camera "
            "low along the line so all twelve read in profile, the "
            "harvest stands in a line: EXACTLY TWELVE woven baskets "
            "set side by side, every one heaped over its brim with "
            "broken barley bread — and behind the row the disciples "
            "stand looking down at what their own arms just "
            "carried, one of them slowly shaking his head, the fed "
            "multitude soft and settled up the slope beyond. "
            "Exactly twelve baskets are in the row. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r058-b22", "out": "s22-more-than-they-started-with.jpeg", "seg": "n6 p4-p5",
        "window": "114.21-122.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAD"],
        "narration": ("They ended with far more than they had started "
                      "with. The little lunch, placed in his hands, had "
                      "become a feast."),
        "must_show": "the build's arithmetic in one image — the boy standing before the twelve heaped baskets, his own small empty basket in his hands.",
        "must_not_show": "his face is the caption: what happens to a small gift placed in the right hands.",
        "scene": (
            "The small boy stands in front of the long row of "
            "twelve heaped baskets in the dusk, his own little rush "
            "basket hanging empty from one hand — his eyes moving "
            "slowly down the line of abundance that used to be his "
            "lunch, his mouth open, doing a child's arithmetic and "
            "getting heaven for an answer. The nearest heaped "
            "basket stands taller than his knees. Exactly one "
            "person is in the frame, with two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r058-b23", "out": "s23-that-prophet.jpeg", "seg": "n7 + s14",
        "window": "122.12-131.41", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": ("When the people saw the sign, they were amazed, "
                      "and began to say: This is of a truth that prophet "
                      "that should come into the world. (John 6:14)"),
        "must_show": "v14 — the recognition rippling: the crowd rising to its feet in waves, faces and gestures turning toward Jesus.",
        "must_not_show": "awe cresting toward something hungrier — they will try to make him king; the energy is real and slightly too much.",
        "scene": (
            "Across the dusk hillside, the camera behind the nearest "
            "rising backs, the multitude is rising to "
            "its feet in spreading waves — arms lifting, neighbours "
            "gripping each other, faces alight and hungry with "
            "recognition, the word passing visibly from group to "
            "group — and every line of the surging crowd bends "
            "toward Jesus, who stands quiet near the twelve "
            "baskets, watching the crest of it come with something "
            "unreadable and knowing in his face. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r058-b24", "out": "s24-he-fed-them-all.jpeg", "seg": "n7b",
        "window": "131.41-135.22", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": ("He had taken almost nothing, given thanks for it, "
                      "and fed them all."),
        "must_show": "the closing frame — Jesus small against the last light and the fed thousands scattered across the whole dusky slope; quiet after abundance.",
        "must_not_show": "no halo/glow; the composition alone says who did this.",
        "scene": (
            "A last wide frame in the blue-and-ember dusk, the "
            "camera far down the slope behind the scattered "
            "groups: the "
            "hillside falls away covered with the fed multitude — "
            "thousands settled and murmuring in the failing light, "
            "small fires beginning here and there — and on the "
            "outcrop stands the single figure of Jesus with the "
            "twelve heaped baskets in a line at his feet, the lake "
            "burning quietly with the last of the sun below. An "
            "upright vertical photograph, the ground at the bottom "
            "of the frame and the sky at the top, the horizon "
            "level — the picture is the right way up."
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
