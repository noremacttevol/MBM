#!/usr/bin/env python3
"""V2 beat map — row 111, build-111-lilies-and-sparrows (Matthew 6:25-34).

COVERAGE: 29 pictures over 162.5 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 6 KJV):
  v26   "Behold the FOWLS OF THE AIR: for they sow not, neither do
        they reap, nor gather into BARNS; yet your heavenly Father
        FEEDETH them. Are ye not MUCH BETTER than they?"
  v28-29 "Consider the LILIES OF THE FIELD, how they grow; they TOIL
        NOT, neither do they SPIN: And yet... even SOLOMON in all his
        glory was not arrayed like one of these." — pointing at real
        flowers at their feet.
  v30   "if God so clothe the GRASS of the field, which to day is,
        and to morrow is CAST INTO THE OVEN, shall he not much more
        clothe you, O YE OF LITTLE FAITH?"
  v33   "SEEK YE FIRST the kingdom of God, and his righteousness; and
        all these things shall be ADDED unto you."
  v34   "Take therefore NO THOUGHT FOR THE MORROW... Sufficient unto
        the day is the evil thereof."

STAGING: the same Sermon-hillside register as row 109 but its OWN
ground — a wildflower meadow slope with sparrows working it; Jesus
teaches by POINTING at what is actually there. Vignettes: sparrows
close, anemones close, a Solomon-glory contrast (rich robes recalled
in a market bolt of cloth, no throne scene), a worried-listener close.

TIME OF DAY: one soft bright late-spring morning throughout, warming
to gold at the close.

CONTENT-CARE: no flags. The worry rendered with dignity — real tired
people, never mocked; the oven-grass beat shows cut dry grass bundled
for fuel, nothing burning on screen.

CHANGING CONDITION (kept OUT of the locks): the listeners' hands —
knotted with worry early, open by the close; the teaching's pointer —
birds, then flowers, then the listeners themselves.
"""

# LOCKS: one entry per recurring person and per setting. Clothing colours
# stated POSITIVELY and dark — only Jesus wears cream.
LOCKS = {
    "MEADOW": (
        "MEADOW LOCK: the teaching meadow — a green late-spring "
        "slope thick with RED ANEMONES and white daisies among tall "
        "grasses, a few grey field stones, the lake a far blue line "
        "below; SPARROWS working the seed heads. The same slope, "
        "flowers and lake-line throughout."
    ),
    "RING": (
        "RING LOCK: the listeners — ordinary Galileans seated in the "
        "grass in DARK EARTH-BROWN, RUST, DEEP OLIVE and SLATE robes "
        "(never cream, never white): a worn farmer, a young mother "
        "with a baby, an old man with a stick, a thin day-laborer. "
        "The same faces throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r111-b01", "out": "s01-he-was-talking-to-people.jpeg", "seg": "n1",
        "window": "0.28-2.94", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MEADOW", "RING"],
        "narration": "He was talking to people who knew what it was to worry.",
        "must_show": "the worried audience — the ring in the flowered grass around Jesus: worry legible in knotted hands and tight shoulders; the teacher who can see it.",
        "must_not_show": "no halo, glare or rim-light; the worry REAL — working people's anxiety, not theatrical despair.",
        "scene": (
            "The meadow holds a ring of "
            "people who know what worry "
            "weighs: the farmer's hands "
            "knotted around his own "
            "wrists, the young mother's "
            "arm too tight around her "
            "baby, the thin laborer "
            "chewing the inside of his "
            "cheek — seated in flowers "
            "none of them have noticed, "
            "around a teacher who has "
            "noticed everything: the "
            "flowers, the sparrows, and "
            "exactly what is knotting "
            "every pair of hands. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r111-b02", "out": "s02-whether-there-would-be-enough.jpeg", "seg": "n1",
        "window": "5.00-6.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["RING"],
        "narration": "Whether there would be enough.",
        "must_show": "the enough-question — close on the farmer's face doing lean-year arithmetic: eyes far away, jaw working; scarcity's private math.",
        "must_not_show": "no halo; the arithmetic INTERNAL — a face counting invisible sacks.",
        "scene": (
            "Close on the oldest "
            "arithmetic in the world: "
            "the worn farmer's eyes gone "
            "far past the meadow to "
            "some private granary, "
            "counting — the jaw working "
            "slowly, the brows drawn, "
            "sacks and mouths and "
            "months tallied and "
            "re-tallied behind the "
            "weathered face — ENOUGH, "
            "the one word every lean "
            "winter carved into him, "
            "asked again into the "
            "spring air that is trying "
            "to answer it. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r111-b03", "out": "s03-behold-the-fowls-of-the.jpeg", "seg": "jv26",
        "window": "12.01-22.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MEADOW", "RING"],
        "narration": (
            "Behold the fowls of the air: for they sow not, neither do they "
            "reap, nor gather into barns; yet your heavenly Father feedeth "
            "them."
        ),
        "must_show": "SCRIPTURE-EXACT: BEHOLD — Jesus's arm directing every eye to sparrows busy in the near grass; the ring's heads turned; the sermon's first exhibit alive and feeding.",
        "must_not_show": "no halo, glare or rim-light; the sparrows NEAR and real — feeding, not decorative.",
        "scene": (
            "The sermon's first exhibit "
            "is already on stage: "
            "Jesus's arm sweeps low "
            "toward the near grass — "
            "BEHOLD — where a scatter of "
            "brown sparrows works the "
            "seed heads, hopping, "
            "pecking, thriving, owning "
            "not one barn between them "
            "— and the ring's worried "
            "heads turn as one along "
            "his arm, arithmetic "
            "interrupted mid-sum by "
            "the sight of the best-fed "
            "creatures on the hillside "
            "doing no accounting at "
            "all. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r111-b04", "out": "s04-no-barns.jpeg", "seg": "n2",
        "window": "28.33-29.48", "wide": False, "jesus": False, "ref": False,
        "locks": ["MEADOW"],
        "narration": "No barns.",
        "must_show": "the no-barns close — one sparrow perched on a seed head, fat and unbothered, owning nothing; the two-word sermon in one bird.",
        "must_not_show": "no halo; ONE bird the frame — sleek, fed, storage-free.",
        "scene": (
            "One bird carries the whole "
            "two-word sermon: a single "
            "sparrow perched on a "
            "bending seed head in the "
            "soft light — sleek, "
            "round-fed, entirely "
            "unbothered — its total "
            "worldly holdings visible "
            "in one glance: the seed in "
            "its beak and the air "
            "under it — no barn, no "
            "storehouse, no ledger "
            "anywhere in its tiny "
            "prosperous life, and not "
            "one feather out of place "
            "for the lack. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r111-b05", "out": "s05-are-ye-not-much-better.jpeg", "seg": "jv26",
        "window": "22.04-24.92", "wide": False, "jesus": True, "ref": REF,
        "locks": ["RING"],
        "narration": "Are ye not much better than they?",
        "must_show": "SCRIPTURE-EXACT: the question turned on them — Jesus's warm face asking it directly into the ring; worth being assigned, faces receiving it.",
        "must_not_show": "no halo, glare or rim-light; the MUCH BETTER landing — surprise at their own valuation.",
        "scene": (
            "The question turns from the "
            "grass to the people: "
            "Jesus's warm face direct "
            "into the ring — ARE YE NOT "
            "MUCH BETTER THAN THEY — "
            "and the valuation lands "
            "visibly: the thin laborer "
            "blinking at being priced "
            "above anything at all, the "
            "young mother's arm easing "
            "on her baby, the farmer's "
            "far-off eyes coming home — "
            "worth, assigned out loud "
            "by the only appraiser "
            "whose numbers hold. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r111-b06", "out": "s06-no-savings.jpeg", "seg": "n2",
        "window": "29.48-30.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["MEADOW"],
        "narration": "No savings.",
        "must_show": "the no-savings beat — sparrows dust-bathing carefree in the path's dry earth; wealthlessness at play.",
        "must_not_show": "no halo; the play REAL sparrow behavior — dust flying, complete unconcern.",
        "scene": (
            "The exhibit continues its "
            "argument by playing: two "
            "sparrows down in the dry "
            "path-dust, bathing — wings "
            "flinging little fountains "
            "of earth, feathers "
            "scandalously ruffled, the "
            "whole performance costing "
            "nothing and worth watching "
            "— creatures with no "
            "savings, no stores, no "
            "hedge against any winter, "
            "spending the middle of a "
            "workday on a dust bath, "
            "richer somehow than "
            "anyone watching them. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r111-b07", "out": "s07-and-not-one-of-them.jpeg", "seg": "n2",
        "window": "32.36-37.34", "wide": True, "jesus": False, "ref": False,
        "locks": ["MEADOW"],
        "narration": (
            "And not one of them goes uncared for, because the Father feeds "
            "them."
        ),
        "must_show": "the feeding seen — the meadow's provision wide: sparrows finding seed everywhere in the grass-heads, the slope itself one spread table.",
        "must_not_show": "no halo, no embodied provider — the provision IS the seeded landscape.",
        "scene": (
            "The wide frame shows the "
            "kitchen: the whole slope "
            "one spread table — seed "
            "heads bending heavy over "
            "every foot of grass, "
            "sparrows dropping onto "
            "them at will, eating "
            "where they land, the "
            "supply running unbroken "
            "from the ring's feet to "
            "the far blue lake — a "
            "feeding so woven into the "
            "landscape that no bird in "
            "it has ever once seen "
            "the Hand that keeps "
            "setting it. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r111-b08", "out": "s08-and-you-you-are-worth.jpeg", "seg": "n2",
        "window": "37.34-42.20", "wide": False, "jesus": True, "ref": REF,
        "locks": ["RING"],
        "narration": "And you — you are worth so much more to him than a sparrow.",
        "must_show": "the worth made personal — Jesus's hand resting on the thin laborer's shoulder, the YOU direct; a man being told his price.",
        "must_not_show": "no halo, glare or rim-light; the laborer's disbelief-then-receiving readable.",
        "scene": (
            "The valuation gets a "
            "shoulder to land on: "
            "Jesus's hand resting warm "
            "on the thin day-laborer — "
            "the least-fed, worst-paid "
            "man on the hillside — AND "
            "YOU — the words aimed "
            "singular and direct while "
            "the man's face does its "
            "unpracticed work: "
            "disbelief first, the old "
            "reflex of the unpriced, "
            "and then, slowly, the "
            "receiving — worth more, "
            "said the Appraiser, than "
            "every bird on the slope "
            "together. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r111-b09", "out": "s09-where-the-next-meal-would.jpeg", "seg": "n1",
        "window": "2.94-5.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["RING"],
        "narration": "Where the next meal would come from.",
        "must_show": "the meal-worry — the young mother's face over her baby: tomorrow's bread already costing her tonight's peace.",
        "must_not_show": "no halo; the worry TENDER — love and fear in the same look down.",
        "scene": (
            "Close on worry wearing its "
            "most tender face: the "
            "young mother looking down "
            "at the baby asleep against "
            "her — and through all the "
            "love in the look, the "
            "question running underneath "
            "like cold water: what do I "
            "feed you when the jar "
            "empties — tomorrow's meal "
            "already collecting its "
            "toll from tonight's "
            "peace, the way it does in "
            "every house that counts "
            "its flour. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r111-b10", "out": "s10-consider-the-lilies-of-the.jpeg", "seg": "jv2829",
        "window": "47.06-61.69", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MEADOW", "RING"],
        "narration": (
            "Consider the lilies of the field, how they grow; they toil not, "
            "neither do they spin: And yet I say unto you, That even Solomon "
            "in all his glory was not arrayed like one of these."
        ),
        "must_show": "SCRIPTURE-EXACT: CONSIDER — Jesus crouched with a red anemone lifted gently in his fingers, the ring bent in around the small flower; Solomon outdressed by it.",
        "must_not_show": "no halo, glare or rim-light; the flower UNPICKED if possible — tilted up on its stem, honored.",
        "scene": (
            "The second exhibit is "
            "smaller and wins bigger: "
            "Jesus crouched in the "
            "grass with one red anemone "
            "tilted gently up on its "
            "stem between his fingers — "
            "CONSIDER — and the whole "
            "ring bending in around "
            "one flower: the scarlet "
            "silk of petals no loom "
            "ever touched, the gold "
            "dust at its heart — while "
            "the words hang the "
            "greatest king in history "
            "beside it, in all his "
            "robes, and quietly hand "
            "the flower the crown. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r111-b11", "out": "s11-and-instead-of-an-argument.jpeg", "seg": "n1",
        "window": "6.75-11.43", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MEADOW", "RING"],
        "narration": (
            "And instead of an argument, Jesus simply pointed at the world "
            "around them."
        ),
        "must_show": "the method — Jesus's open arm sweeping the living meadow itself: flowers, grass, birds, lake; creation as the whole lecture.",
        "must_not_show": "no halo, glare or rim-light; NO scroll or debate posture — the world itself the text.",
        "scene": (
            "The teacher's whole method "
            "in one gesture: no scroll "
            "opened, no argument "
            "mounted — just Jesus's arm "
            "sweeping wide across "
            "everything already there: "
            "the anemones burning red "
            "through the grass, the "
            "sparrows working the seed, "
            "the far lake laid blue and "
            "calm under the morning — "
            "the oldest lecture hall "
            "on earth, in session "
            "since creation, pointed "
            "at by the one Teacher who "
            "was present when it was "
            "furnished. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r111-b12", "out": "s12-these-flowers-do-not-work.jpeg", "seg": "n4",
        "window": "63.20-65.29", "wide": False, "jesus": False, "ref": False,
        "locks": ["MEADOW"],
        "narration": "These flowers do not work a single day.",
        "must_show": "the unworking flowers — anemones close in the breeze: brilliant, effortless, idle; splendor with no labor behind it.",
        "must_not_show": "no halo; the close LUXURIANT — petals at their scarlet best.",
        "scene": (
            "Close on the idlest "
            "splendor in Galilee: a "
            "stand of red anemones "
            "swaying easy in the "
            "morning breeze — petals at "
            "their scarlet best, black "
            "hearts dusted gold, silk "
            "no worm spun and no hand "
            "wove — and behind the "
            "brilliance, a work history "
            "of exactly nothing: no "
            "sowing, no spinning, no "
            "single day's labor ever "
            "logged by anything in the "
            "frame — glory, running "
            "entirely on gift. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r111-b13", "out": "s13-look-at-the-little-sparrows.jpeg", "seg": "n2",
        "window": "26.46-28.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MEADOW"],
        "narration": "Look at the little sparrows, he says.",
        "must_show": "the look-instruction — Jesus's profile and pointing hand guiding the gaze to the near birds; teaching by direction of attention.",
        "must_not_show": "no halo, glare or rim-light; his delight in the birds VISIBLE — the teacher enjoys his exhibits.",
        "scene": (
            "Close on a teacher who "
            "likes his visual aids: "
            "Jesus in profile, hand "
            "extended toward the "
            "sparrows in the grass, and "
            "on his face — plain as "
            "the morning — delight: the "
            "warm eyes crinkled at the "
            "dust-bathing, the half-"
            "smile of a maker watching "
            "small things he is fond "
            "of — LOOK, the hand says, "
            "and means it: attention, "
            "redirected from worry to "
            "wonder, one bird at a "
            "time. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r111-b14", "out": "s14-and-yet-the-richest-king.jpeg", "seg": "n4",
        "window": "67.61-78.34", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "And yet the richest king who ever lived, in all his robes, was "
            "never dressed as beautifully as one ordinary wildflower that "
            "God simply decided to clothe."
        ),
        "must_show": "the Solomon contrast — a market vignette: a merchant's costliest bolt of purple-gold cloth beside one wild anemone laid on it; the flower winning.",
        "must_not_show": "no halo; no throne scene — the contrast staged small: cloth versus flower, and the flower finer.",
        "scene": (
            "The contest is staged on a "
            "market table: a merchant's "
            "costliest bolt unrolled — "
            "deep purple shot with gold "
            "thread, king's cloth, a "
            "year's wages a yard — and "
            "laid across it, dropped "
            "by some passing child, one "
            "ordinary red anemone — "
            "and the cloth loses: the "
            "petal's living silk making "
            "the weave look coarse, "
            "the flower's careless "
            "scarlet outshining the "
            "loom's whole year — "
            "Solomon, outdressed by a "
            "weed. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r111-b15", "out": "s15-no-plans-for-next-winter.jpeg", "seg": "n2",
        "window": "30.43-32.36", "wide": False, "jesus": False, "ref": False,
        "locks": ["MEADOW"],
        "narration": "No plans for next winter.",
        "must_show": "the planless birds — a sparrow feeding its fledglings on a stone in the open: next generation provided for, no plan anywhere.",
        "must_not_show": "no halo; the feeding TENDER — provision happening in real time.",
        "scene": (
            "The most reckless budget "
            "on the hillside, thriving: "
            "a mother sparrow on a "
            "grey field stone stuffing "
            "seed into two gaping "
            "fledglings — mouths she "
            "cannot possibly guarantee "
            "against the winter she "
            "has made no plans for — "
            "and the seed keeps "
            "coming, beakful after "
            "beakful, out of a supply "
            "she has never audited — "
            "provision arriving in "
            "real time, on no "
            "schedule but the "
            "Father's. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r111-b16", "out": "s16-wherefore-if-god-so-clothe.jpeg", "seg": "jv30",
        "window": "78.84-90.41", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MEADOW", "RING"],
        "narration": (
            "Wherefore, if God so clothe the grass of the field, which "
            "today is, and tomorrow is cast into the oven, shall he not "
            "much more clothe you, O ye of little faith?"
        ),
        "must_show": "SCRIPTURE-EXACT: the a-fortiori — Jesus with a handful of cut dry grass lifted beside the living flowers, the how-much-more argument in his two hands; the ring following.",
        "must_not_show": "no halo, glare or rim-light; NOTHING burning on screen — the dry bundle only implies the oven.",
        "scene": (
            "The argument goes into his "
            "two hands: in one, a "
            "handful of cut dry grass "
            "from someone's fuel "
            "bundle — today's glory, "
            "tomorrow's oven — and the "
            "other open toward the "
            "living scarlet still "
            "burning through the "
            "meadow around them — IF "
            "GOD SO CLOTHE THE GRASS — "
            "the two fists of the "
            "how-much-more held up "
            "where the whole ring can "
            "weigh them, with the "
            "gentle charge landing "
            "last: O YE OF LITTLE "
            "FAITH. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r111-b17", "out": "s17-then-he-reaches-down-to.jpeg", "seg": "n3",
        "window": "42.74-46.55", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MEADOW"],
        "narration": (
            "Then he reaches down to the wildflowers scattered through the "
            "grass at their feet."
        ),
        "must_show": "the reach — Jesus's hand descending gently into the flowered grass at the listeners' feet; the sermon literally at ground level.",
        "must_not_show": "no halo, glare or rim-light; the reach SLOW and gentle — reverence for small things.",
        "scene": (
            "The sermon bends down to "
            "the ground it stands on: "
            "Jesus's hand descending "
            "slow and gentle into the "
            "grass right at the ring's "
            "feet — where the anemones "
            "have been burning scarlet "
            "all morning, unnoticed at "
            "the exact eye-level of "
            "everyone's worry — the "
            "next exhibit chosen not "
            "from far off but from "
            "the two square feet of "
            "creation nearest their "
            "own sandals. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r111-b18", "out": "s18-here-is-his-point-gentle.jpeg", "seg": "n5",
        "window": "92.12-102.15", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MEADOW", "RING"],
        "narration": (
            "Here is his point, gentle and steady: if God feeds the birds "
            "and dresses the grass that is here today and gone tomorrow, "
            "how much more will he take care of you?"
        ),
        "must_show": "the point landing — the whole scene at rest: teacher, ring, birds and flowers in one warm frame; the logic settled over everyone like the morning light.",
        "must_not_show": "no halo, glare or rim-light; the ring's faces EASING — the argument doing its work visibly.",
        "scene": (
            "The whole classroom rests "
            "inside its own conclusion: "
            "teacher and ring seated "
            "together in the flowered "
            "grass, sparrows still "
            "working the seed heads "
            "around them, anemones "
            "still wearing their "
            "unearned scarlet — and "
            "across the listening "
            "faces the logic settling "
            "like the light: fed "
            "birds, dressed grass, "
            "and between them, worth "
            "more than both, "
            "themselves — the how-much-"
            "more finding its home in "
            "every eased shoulder. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r111-b19", "out": "s19-take-therefore-no-thought-for.jpeg", "seg": "jv34",
        "window": "102.68-108.65", "wide": False, "jesus": True, "ref": REF,
        "locks": ["RING"],
        "narration": (
            "Take therefore no thought for the morrow: for the morrow shall "
            "take thought for the things of itself."
        ),
        "must_show": "SCRIPTURE-EXACT: the morrow released — Jesus's two hands making a gentle setting-down motion before the ring; tomorrow laid out of their grip.",
        "must_not_show": "no halo, glare or rim-light; the gesture a LAYING DOWN — burden physically released.",
        "scene": (
            "The command comes with its "
            "own choreography: Jesus's "
            "two hands, palms down, "
            "making the slow gentle "
            "motion of a man setting a "
            "heavy jar off his "
            "shoulders onto the "
            "ground — THERE — take no "
            "thought for the morrow, "
            "the morrow is carrying "
            "itself — and around the "
            "ring, hands that came "
            "knotted this morning "
            "beginning, awkwardly, to "
            "copy the motion: worry, "
            "being taught how to put "
            "things down. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r111-b20", "out": "s20-sufficient-unto-the-day-is.jpeg", "seg": "jv34",
        "window": "108.65-113.13", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MEADOW"],
        "narration": "Sufficient unto the day is the evil thereof.",
        "must_show": "SCRIPTURE-EXACT: the day-sized portion — Jesus's steady face with the one-day-at-a-time verdict; the morning around him exactly one day big.",
        "must_not_show": "no halo, glare or rim-light; the register CALM — a boundary drawn kindly around today.",
        "scene": (
            "Close on the kindest fence "
            "ever built: Jesus's steady "
            "face delivering the "
            "day-sized verdict — "
            "SUFFICIENT UNTO THE DAY — "
            "the words drawing a quiet "
            "boundary around this one "
            "morning: its own bread, "
            "its own troubles, its own "
            "grace, and nothing "
            "borrowed from tomorrow's "
            "account — life handed "
            "back to them in the only "
            "portion human shoulders "
            "were ever built for: one "
            "day. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r111-b21", "out": "s21-go-out-to-meet-tomorrow.jpeg", "seg": "n5b",
        "window": "114.64-116.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["RING"],
        "narration": "Don't go out to meet tomorrow.",
        "must_show": "the not-yet — a listener's face caught mid-release: the forward-straining posture easing back into the present moment.",
        "must_not_show": "no halo; the easing PHYSICAL — shoulders coming back, breath returning.",
        "scene": (
            "Close on a body coming "
            "back from tomorrow: the "
            "old man with the stick, "
            "who has spent the whole "
            "morning leaned forward "
            "into some dreaded "
            "next-month — and now, "
            "under the teaching, the "
            "forward strain easing out "
            "of him by degrees: "
            "shoulders settling back, "
            "the grip on the stick "
            "loosening, breath "
            "arriving where bracing "
            "used to live — a man "
            "called home to the only "
            "day he actually has. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r111-b22", "out": "s22-tomorrow-will-look-after-itself.jpeg", "seg": "n5b",
        "window": "116.09-125.37", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MEADOW", "RING"],
        "narration": (
            "Tomorrow will look after itself, and today has enough in it "
            "already. Your anxious tomorrow is not something you have to "
            "carry alone."
        ),
        "must_show": "the shared carry — Jesus among the ring, a hand on the farmer's bowed shoulder; the alone-ness of worry ended in company.",
        "must_not_show": "no halo, glare or rim-light; the NOT-ALONE physical — presence beside the worrier.",
        "scene": (
            "The last weight gets a "
            "second shoulder: Jesus "
            "moved in beside the worn "
            "farmer whose arithmetic "
            "started the morning, one "
            "hand resting steady on "
            "the bowed back — today "
            "has enough in it, and "
            "you were never meant to "
            "haul next winter through "
            "it single-handed — the "
            "meadow bright and "
            "unbothered around two "
            "men, one of whom is "
            "learning that his anxious "
            "tomorrow has company for "
            "the road. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r111-b23", "out": "s23-he-is-not-scolding-the.jpeg", "seg": "n6",
        "window": "125.92-129.94", "wide": False, "jesus": True, "ref": REF,
        "locks": ["RING"],
        "narration": (
            "He is not scolding the worry. He knows life is hard and needs "
            "are real."
        ),
        "must_show": "the no-scold — close on Jesus's face toward the worriers: complete understanding, zero rebuke; hardship acknowledged as real.",
        "must_not_show": "no halo, glare or rim-light; NO minimizing in the face — the needs honored even as the fear is lifted.",
        "scene": (
            "Close on the difference "
            "between a scold and a "
            "physician: Jesus's face "
            "toward the worried ring "
            "carrying not one line of "
            "rebuke — the eyes that "
            "know exactly what an "
            "empty flour jar sounds "
            "like when you scrape it, "
            "what a lean winter does "
            "to a father's sleep — "
            "hardship taken seriously "
            "to the last measure, and "
            "only the fear, never the "
            "need, being gently "
            "carried off. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r111-b24", "out": "s24-they-just-grow-where-they.jpeg", "seg": "n4",
        "window": "65.29-67.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["MEADOW"],
        "narration": "They just grow where they are planted.",
        "must_show": "the growing-in-place — anemones rooted bright in a rocky seam: thriving exactly where they were set, no striving anywhere.",
        "must_not_show": "no halo; the rooting VISIBLE — flowers rising from a hard place, easily.",
        "scene": (
            "Close on contentment with "
            "an address: a cluster of "
            "anemones rooted in the "
            "seam of a grey field "
            "stone — scarlet blazing "
            "up out of a crack an "
            "inch wide, thriving "
            "exactly where the wind "
            "set them down — no "
            "reaching for better soil, "
            "no envy of the deep "
            "meadow a yard away, just "
            "the whole assignment "
            "accepted and bloomed in "
            "place — planted, and "
            "growing, and that being "
            "the entire plan. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r111-b25", "out": "s25-he-is-gently-loosening-your.jpeg", "seg": "n6",
        "window": "129.94-139.30", "wide": False, "jesus": True, "ref": REF,
        "locks": ["RING"],
        "narration": (
            "He is gently loosening your grip, one finger at a time, and "
            "offering to carry it with you, as a Father who already knows "
            "exactly what you need."
        ),
        "must_show": "the loosening — close on hands: Jesus's hands gently opening the farmer's white-knuckled fist, finger by finger; the grip released into a shared hold.",
        "must_not_show": "no halo, glare or rim-light; the opening TENDER and unforced — help, not prying.",
        "scene": (
            "Close on the gentlest "
            "rescue on the hillside: "
            "the farmer's fist — "
            "white-knuckled around "
            "nothing, clenched from "
            "years of holding on — and "
            "Jesus's hands around it, "
            "easing the fingers open "
            "one patient finger at a "
            "time, never prying, only "
            "warming them loose — "
            "until the empty palm lies "
            "open in his, and what "
            "the fist was guarding "
            "turns out to be carried "
            "now by two. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r111-b26", "out": "s26-but-seek-ye-first-the.jpeg", "seg": "jv33",
        "window": "139.84-147.22", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MEADOW", "RING"],
        "narration": (
            "But seek ye first the kingdom of God, and his righteousness; "
            "and all these things shall be added unto you."
        ),
        "must_show": "SCRIPTURE-EXACT: the reordering — Jesus's hand lifted FIRST toward the sky's kingdom-height, then opening down over the meadow's provisions; the order taught in one motion.",
        "must_not_show": "no halo, glare or rim-light; the SEQUENCE readable — first up, then everything else added below.",
        "scene": (
            "The whole economy is "
            "reordered in one motion: "
            "Jesus's hand rising FIRST "
            "— up toward the high "
            "morning sky, the kingdom's "
            "direction, the one thing "
            "sought before all things — "
            "and then opening slowly "
            "downward over the meadow "
            "and everything in it: "
            "seed, birds, flowers, "
            "bread, tomorrow — ALL "
            "THESE THINGS, added, "
            "following the first thing "
            "the way the wake follows "
            "the boat. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r111-b27", "out": "s27-put-him-first-he-says.jpeg", "seg": "n7",
        "window": "148.68-153.36", "wide": False, "jesus": True, "ref": REF,
        "locks": ["RING"],
        "narration": (
            "Put him first, he says, and stop bracing against tomorrow all "
            "by yourself."
        ),
        "must_show": "the unbracing — the ring's postures transformed from the opening beat: hands open in laps, shoulders down, faces present; the before-and-after in bodies.",
        "must_not_show": "no halo, glare or rim-light; the CONTRAST with b01 deliberate — same people, unknotted.",
        "scene": (
            "The same ring, unknotted: "
            "where the morning began "
            "with wrung hands and "
            "braced shoulders, the "
            "grass now holds different "
            "bodies — the farmer's "
            "palms open on his knees, "
            "the mother's arm easy "
            "around her waking baby, "
            "the laborer leaned back "
            "on his elbows watching "
            "sparrows — the identical "
            "people carrying identical "
            "lives, minus the one "
            "load that was never "
            "theirs to lift alone. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r111-b28", "out": "s28-the-same-father-who-has.jpeg", "seg": "n7",
        "window": "153.36-159.10", "wide": True, "jesus": False, "ref": False,
        "locks": ["MEADOW"],
        "narration": (
            "The same Father who has not forgotten a single sparrow has "
            "certainly not forgotten you."
        ),
        "must_show": "the remembered world — the meadow wide and cared-for in warming gold: every bird fed, every flower dressed; a landscape with no forgotten corner.",
        "must_not_show": "no halo, no embodied provider — the care legible in the thriving itself.",
        "scene": (
            "The wide gold light takes "
            "inventory and finds "
            "nothing missed: every "
            "seed head on the slope "
            "bending with grain, every "
            "sparrow on it fed round, "
            "every anemone dressed "
            "past Solomon down to the "
            "ones blooming where no "
            "eye but heaven's will "
            "ever pass — a landscape "
            "without one forgotten "
            "corner in it, hung like "
            "a signed promise over "
            "everyone the meadow has "
            "been preaching to all "
            "morning. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r111-b29", "out": "s29-you-can-breathe-you-are.jpeg", "seg": "n7",
        "window": "159.10-162.24", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MEADOW", "RING"],
        "narration": "You can breathe. You are cared for.",
        "must_show": "the closing image — the ring at deep ease around Jesus in the gold: a hillside actually breathing; care as the settled fact of the frame.",
        "must_not_show": "no halo, glare or rim-light; the PEACE total — the row ends exhaled.",
        "scene": (
            "The closing frame simply "
            "breathes: the ring at "
            "deep ease around their "
            "teacher in the day's "
            "warmest gold — the baby "
            "asleep, the old man's "
            "eyes closed in the sun, "
            "sparrows dust-bathing "
            "unafraid a yard from "
            "human hands — a hillside "
            "full of people who "
            "arrived carrying next "
            "winter and are leaving "
            "carrying today — cared "
            "for, and finally, "
            "visibly, breathing like "
            "it. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
]
