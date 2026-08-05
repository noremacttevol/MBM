#!/usr/bin/env python3
"""V2 beat map — row 146, build-146-vine-and-branches (John 15:1-5).

COVERAGE: 14 pictures over 79.5 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (John 15 KJV):
  15:4  "ABIDE IN ME, and I in you. As the branch cannot bear fruit
        of itself, except it abide in the vine; no more can ye,
        except ye abide in me."
  15:5  "I AM THE VINE, YE ARE THE BRANCHES: He that abideth in me,
        and I in him, the same bringeth forth MUCH FRUIT: for
        WITHOUT ME YE CAN DO NOTHING."
  Setting: the night walk from the upper room toward the garden —
        a moonlit vineyard beside the way; the vignette frames in
        the vineyard's golden day (illustration light).

RENDERING LAWS:
  - The VINEYARD is the build-23 family (rows 41/45 wire from it) —
    accept the family plate if offered and it matches; ONE great
    OLD VINE is this row's protagonist-plant: same gnarled trunk,
    same trained branches, every vineyard frame.
  - THE BRANCH NEVER STRAINS (the row's doctrine): no effort
    imagery on any branch — laden branches REST on the trunk's
    supply; b05/b06 are ease made visible.
  - The cut-branch pair (b11/b12) is the same branch twice: freshly
    cut and still green-strong, then withered dry beside the
    flourishing vine — time's verdict, not violence (the cutting
    itself is never shown).
  - Jesus's night beats keep the moonlit walking register (the
    row-137 grove night, every light physical); the day vignettes
    are golden vineyard light BY DESIGN.
  - b08's hired hands leave at dusk with their tools — ordinary
    workers, not villains; the contrast is belonging, not virtue.

TIME OF DAY ARC (intentional): the Jesus beats at moonlit night
(the upper-room walk); the vineyard vignettes in warm golden day;
b12's withering under flat dry noon; the close back at night with
the moon on the old vine.

CHANGING CONDITION (kept OUT of the locks): the cut branch — green,
then withered; the clusters — forming, then heavy.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "VINEYARD": (
        "VINEYARD LOCK: the vineyard — trained rows of grapevines "
        "on low stone terraces with a dry-stone wall and a watch "
        "booth, far hills beyond. At the head row stands ONE GREAT "
        "OLD VINE: a thick gnarled trunk with wide-trained fruiting "
        "branches. The same rows, wall and old vine throughout."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the Eleven on the night walk — travel-"
        "cloaked men in earth-toned robes of brown, rust, olive and "
        "slate (no cream — only Jesus wears cream); varied faces "
        "silver in the moonlight, listening close."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r146-b01", "out": "s01-jesus-used-a-picture-his.jpeg", "seg": "n0a + n0b",
        "window": "0.40-6.96", "wide": True, "jesus": True, "ref": REF,
        "locks": ["VINEYARD", "DISCIPLES"],
        "narration": (
            "Jesus used a picture His friends would know — a vine, and the "
            "branches that grow from it."
        ),
        "must_show": "the picture found — the moonlit vineyard beside the night road, Jesus stopping his walking disciples at the great old vine; the teaching about to grow on a real plant.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the night moonlit and physical; the old vine unmistakable at the head row.",
        "scene": (
            "The lesson is growing beside the road they are "
            "walking, the camera set behind the disciples' "
            "cloaked backs at the wall: the moonlit vineyard "
            "steps away in silver rows, and at the head of "
            "them the great old vine stands gnarled and "
            "wide-armed in the night — Jesus stopped beside "
            "it with his hand lifting toward the trained "
            "branches, eleven tired men gathering at the "
            "dry-stone wall — the last parable before the "
            "garden, taught off a living visual aid at "
            "midnight. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r146-b02", "out": "s02-abide-in-me-and-i.jpeg", "seg": "j0",
        "window": "8.43-10.85", "wide": False, "jesus": True, "ref": REF,
        "locks": ["VINEYARD"],
        "narration": "Abide in me, and I in you.",
        "must_show": "SCRIPTURE-EXACT: the abide — Jesus's hand resting on the old vine's gnarled trunk as he says it; indwelling spoken with his palm on living wood.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hand ON the trunk — the word and the wood together.",
        "scene": (
            "The word is spoken with his palm on the "
            "evidence: Jesus's hand rests flat against the "
            "old vine's gnarled moonlit trunk — abide in ME, "
            "and I in YOU — the doubled indwelling laid out "
            "in six words while the living wood under his "
            "palm does exactly that with every branch it "
            "holds: remains, and is remained in — the "
            "deepest mutual sentence in the gospel, taught "
            "against bark. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r146-b03", "out": "s03-as-the-branch-cannot-bear.jpeg", "seg": "j0",
        "window": "10.85-20.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": (
            "As the branch cannot bear fruit of itself, except it abide in "
            "the vine; no more can ye, except ye abide in me."
        ),
        "must_show": "SCRIPTURE-EXACT: the junction — close on a healthy branch flowing OUT of the old trunk, young grape clusters forming along it; the dependence visible in the joined wood.",
        "must_not_show": "no halo; the joint SEAMLESS — one wood; the young fruit on the branch's far reach.",
        "scene": (
            "The whole verse is visible at one joint: close "
            "on the place where a healthy branch flows out "
            "of the old trunk — bark grown into bark, one "
            "wood without a seam — and along the branch's "
            "reach the young clusters forming green and "
            "certain toward the light — every grape on it "
            "funded entirely through that joint, not one "
            "produced by the branch's own account — the "
            "arithmetic of abiding, written in wood and "
            "fruit. No people are needed in this frame."
        ),
    },
    {
        "id": "v2-r146-b04", "out": "s04-you-are-the-branches.jpeg", "seg": "n0c",
        "window": "39.26-40.65", "wide": False, "jesus": True, "ref": REF,
        "locks": ["VINEYARD", "DISCIPLES"],
        "narration": "You are the branches.",
        "must_show": "the naming — Jesus's hand moving from the trained branches to the listening disciples' faces; the identification direct.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gesture's ARC readable — branches to men.",
        "scene": (
            "The metaphor gets its casting call: Jesus's "
            "hand traces from the moonlit trained branches "
            "across to the eleven faces at the wall — YOU — "
            "the arc of the gesture joining wood to men "
            "mid-air — are the branches — fishermen and "
            "tax-men and brothers assigned their place in "
            "the living system on the spot, every one of "
            "them now part of a plant whose trunk is "
            "standing beside them wearing sandals. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r146-b05", "out": "s05-stay-in-me-he-said.jpeg", "seg": "n0d",
        "window": "22.85-27.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": (
            "Stay in me, he said, and I will stay in you. It has never once "
            "done it."
        ),
        "must_show": "the no-strain doctrine — a laden branch RESTING easy along its trellis in golden day, heavy with grapes it never strained for; effort absent from the whole frame.",
        "must_not_show": "ABSOLUTE: no strain imagery — the branch at rest, supported, supplied; the ease is the doctrine.",
        "scene": (
            "Consider how hard the branch is working: the "
            "laden branch lies easy along its trellis wire "
            "in the golden afternoon, heavy clusters "
            "hanging ripe beneath it, leaves turned "
            "unhurried to the sun — and nowhere in the "
            "whole frame one fiber of strain: no reaching, "
            "no producing, no anxious pushing of grapes "
            "into being — a branch that has never once "
            "borne fruit by effort, resting on a supply "
            "that never once asked it to. No people are "
            "needed in this frame."
        ),
    },
    {
        "id": "v2-r146-b06", "out": "s06-all-it-does-is-stay.jpeg", "seg": "n0d",
        "window": "27.88-32.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": "All it does is stay attached, and the life of the vine does the rest.",
        "must_show": "the whole job — extreme close on the branch-trunk joint: bark grown together, one continuous wood; attachment as the entire assignment.",
        "must_not_show": "no halo; NOTHING else in frame — the joint is the sermon.",
        "scene": (
            "The branch's complete job description, "
            "photographed: extreme close on the joint where "
            "branch meets trunk — bark grown seamlessly "
            "into bark, grain running unbroken from the old "
            "wood into the young, sap-line invisible and "
            "total — the entire assignment visible in one "
            "grown-together place: stay attached — that is "
            "the whole list — and up out of frame, funded "
            "by this joint alone, the fruit is already "
            "hanging. No people are needed in this frame."
        ),
    },
    {
        "id": "v2-r146-b07", "out": "s07-i-am-the-vine-ye.jpeg", "seg": "j1a + n0c",
        "window": "33.64-39.26", "wide": False, "jesus": True, "ref": REF,
        "locks": ["VINEYARD", "DISCIPLES"],
        "narration": "I am the vine, ye are the branches: I am the vine, he said.",
        "must_show": "SCRIPTURE-EXACT: the I AM — Jesus beside the old trunk, one arm laid along a trained branch toward the disciples standing among the rows; vine, branches and men in one frame.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the composition JOINS him to trunk and them to branches.",
        "scene": (
            "The sentence is staged on the living plant: "
            "Jesus stands at the great old trunk with one "
            "arm laid along a trained branch, and the "
            "branch's line runs on past his hand to where "
            "the disciples stand among the moonlit rows — "
            "I am the VINE — the trunk at his back — ye "
            "are the BRANCHES — the wood between them "
            "carrying the sentence from his arm to their "
            "shoulders — the whole organism assembled in "
            "one frame: source, supply, and the eleven "
            "living reaches of it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r146-b08", "out": "s08-not-visitors-not-hired-hands.jpeg", "seg": "n0c",
        "window": "40.65-43.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": "Not visitors. Not hired hands.",
        "must_show": "the contrast — at golden dusk, hired workers shouldering their tools and leaving through the vineyard gate, while the vine and its branches REMAIN; belonging vs employment.",
        "must_not_show": "no halo; the workers ORDINARY, not villains — they simply go home; the vine stays.",
        "scene": (
            "At quitting time the difference walks out the "
            "gate: the hired hands shoulder their pruning "
            "hooks and baskets in the golden dusk and file "
            "out through the vineyard gate toward the "
            "village — honest workers, done for the day, "
            "owed their wage — while behind them the rows "
            "stand on in the fading light, branches staying "
            "where branches live — the difference between "
            "working IN a vineyard and being PART of one, "
            "told entirely by who goes home at dark. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r146-b09", "out": "s09-branches-part-of-the-same.jpeg", "seg": "n0c",
        "window": "43.17-46.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD", "DISCIPLES"],
        "narration": "Branches — part of the same living thing.",
        "must_show": "the belonging — disciples' hands resting on the trained branches among the moonlit rows, men and vine one continuous composition; membership in a living thing.",
        "must_not_show": "no halo; the hands GENTLE on the wood — belonging, not grasping.",
        "scene": (
            "The new membership is taken up by hand: along "
            "the moonlit row the disciples' hands come to "
            "rest on the trained branches — a fisherman's "
            "scarred palm on the smooth young wood, an old "
            "tax-man's fingers under a leaf — men touching "
            "the thing they have just been named into, one "
            "continuous line of trunk and branch and hand "
            "and man down the silver row — not an audience "
            "around a plant: parts, of the same living "
            "thing. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r146-b10", "out": "s10-he-that-abideth-in-me.jpeg", "seg": "j1b",
        "window": "48.11-56.29", "wide": False, "jesus": True, "ref": REF,
        "locks": ["VINEYARD"],
        "narration": (
            "He that abideth in me, and I in him, the same bringeth forth "
            "much fruit: for without me ye can do nothing."
        ),
        "must_show": "SCRIPTURE-EXACT: much fruit — Jesus lifting a heavy ripe cluster in his open palm, the weight of it visible; abundance as evidence.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the cluster HEAVY and real in the palm — much fruit, literally.",
        "scene": (
            "The promise gets weighed in his open hand: "
            "Jesus lifts a heavy ripe cluster from the "
            "laden branch and lets its full weight rest in "
            "his palm — dark grapes crowding the stem, "
            "dusted and dense, more in one bunch than a "
            "strained branch could fake in a season — MUCH "
            "fruit, the hand says, this is what abiding "
            "yields — and the sentence's other half stands "
            "quiet under it: without me, nothing; with me, "
            "this. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r146-b11", "out": "s11-a-branch-cut-off-from.jpeg", "seg": "n1",
        "window": "58.25-61.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": "A branch cut off from the vine doesn't dry up because it's weak.",
        "must_show": "the cut branch FRESH — lying on the terrace stones, still green and strong-looking, leaves unfaded; nothing weak about it yet; the cutting itself never shown.",
        "must_not_show": "ABSOLUTE: no cutting depicted — the branch simply lies separate; visibly still strong.",
        "scene": (
            "The branch on the ground looks perfectly fine: "
            "it lies across the terrace stones in the flat "
            "bright light, freshly separate, leaves still "
            "green and firm, young fruit still set along "
            "it — nothing weak anywhere in its grain, "
            "nothing sickly — a strong branch by every "
            "visible measure, minus exactly one thing that "
            "does not photograph: the joint — and the "
            "verdict on that one missing thing is already "
            "travelling up its veins. No people are needed "
            "in this frame."
        ),
    },
    {
        "id": "v2-r146-b12", "out": "s12-it-dries-up-because-disconnected.jpeg", "seg": "n1",
        "window": "61.64-64.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": "It dries up because it's disconnected.",
        "must_show": "the same branch LATER — withered grey-brown and curled on the same stones, while the connected rows flourish green just beyond; time's verdict on disconnection.",
        "must_not_show": "no halo; the SAME branch as b11 (position rhyme); the flourishing vine sharp in the background contrast.",
        "scene": (
            "Time files its report on the same stones: the "
            "branch lies where it lay — but grey-brown now, "
            "leaves curled to paper, the set fruit shrunk "
            "to hard beads — dried out not by weakness, "
            "not by weather, not by any flaw in its wood, "
            "but by the one subtraction that decides "
            "everything — while a few feet beyond it the "
            "connected rows stand deep green and heavy, "
            "running on the joint it lost. No people are "
            "needed in this frame."
        ),
    },
    {
        "id": "v2-r146-b13", "out": "s13-stay-joined-to-him-and.jpeg", "seg": "n2",
        "window": "65.92-72.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": (
            "Stay joined to Him, and the life flows. Try to bear fruit on "
            "your own, and there's nothing there."
        ),
        "must_show": "the two outcomes in one frame — the joined branch heavy with ripe clusters above, the withered detached one on the stones below; the whole teaching in one composition.",
        "must_not_show": "no halo; both outcomes SHARP — laden above, withered below, the joint the only difference.",
        "scene": (
            "Both endings share one frame at the head row: "
            "above, the joined branch hangs heavy off the "
            "old trunk, clusters ripe and crowding — the "
            "life flowing visibly into weight — and on the "
            "stones below it the withered branch lies "
            "grey and finished, its try-it-alone experiment "
            "complete — the same species, the same "
            "vineyard, the same sun on both, and between "
            "their two endings exactly one variable: "
            "joined, or not. No people are needed in this "
            "frame."
        ),
    },
    {
        "id": "v2-r146-b14", "out": "s14-he-asking-for-effort-he.jpeg", "seg": "n3a + n3b",
        "window": "73.68-78.39", "wide": False, "jesus": True, "ref": REF,
        "locks": ["VINEYARD", "DISCIPLES"],
        "narration": "He wasn't asking for effort. He was offering connection.",
        "must_show": "the closing offer — night again: Jesus's hand clasping a disciple's hand gently against the old vine's trunk; connection offered skin to bark to skin.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the clasp GENTLE — an offer taken, not a demand; the moon on the old vine.",
        "scene": (
            "The last frame is a handclasp against old "
            "wood: back in the moonlight Jesus takes a "
            "disciple's hand and lays it with his own "
            "against the great vine's gnarled trunk — skin "
            "on bark on skin, the three of them joined in "
            "one quiet stack — nothing demanded in the "
            "gesture, nothing to achieve, no effort "
            "requested anywhere in it: only the offer the "
            "whole night walk was about — stay connected, "
            "and let the life do what life does. Every "
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
    "VINEYARD": "PLACE-REF/vineyard.jpeg",  # build-23-vineyard v2-r023-b03
}
# === end PLACE-PLATES ===
