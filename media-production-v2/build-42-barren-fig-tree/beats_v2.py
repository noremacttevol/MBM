#!/usr/bin/env python3
"""V2 beat map — row 42, build-42-barren-fig-tree (Luke 13:6-9).

COVERAGE: 35 pictures over 200.3 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 13:6-9 KJV):
  v6    "A certain man had a fig tree planted IN HIS VINEYARD; and he came
        and sought fruit thereon, and found none" — the tree holds the
        BEST ground on the property: worked soil, the grapes' water, the
        wall, full sun. Its privilege is painted before its failure.
  v7    "these THREE YEARS I come seeking fruit ... CUT IT DOWN; why
        cumbereth it the ground?" — the owner is FAIR, not cruel: three
        seasons of empty hands; any farmer would nod. The axe order is
        plain sense, and the pictures honour that.
  v8    "Lord, let it alone THIS YEAR ALSO, till I shall DIG about it,
        and DUNG it" — the gardener STEPS BETWEEN sentence and tree, and
        volunteers his own labour: the lowest job on the farm, done by
        hand for a tree that gave him nothing. The intercession beats
        are the row's heart.
  v9    "And if it bear fruit, well: and if not, then after that thou
        shalt cut it down" — THE ENDING IS OPEN. The final beats stay
        inside the granted year: the tree still standing, the work done
        at its roots, no resolution shown — mercy still at work.
  Mercy law (CONTENT-CARE §: 'the fig tree given one more year' is the
  named example): the row's whole tone is the kindness of extra time.
  The axe appears but NEVER strikes; no felling is depicted.

TIME OF DAY: the frame beats are bright open morning. The parable runs
in seasons: the owner's empty-handed visits in LATE-SUMMER fig-season
light (three variations); the axe conversation in the same hard noon;
the gardener's digging and feeding in soft AUTUMN light; the open
ending at the next spring's first light, buds unproven. All shifts are
the story's own calendar.

CONTENT-CARE: nothing sensitive; the axe is carried and set down, never
swung. The dung beat is earthy but clean — baskets and worked soil.

CHANGING CONDITION (kept OUT of the locks): the tree's dressing — bare
summer barrenness, the dug ring of autumn, the dark fed soil, the first
spring buds — moves per-beat. The tree itself (shape, place) is locked.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "OWNER": (
        "OWNER LOCK: the vineyard's owner is the same man in every shot — "
        "about sixty, square and weathered, with a clipped grey beard, "
        "a farmer's flat practical gaze and heavy capable hands. He "
        "wears a good plain DARK WALNUT-BROWN robe with a wide leather "
        "belt and dusty boots (never cream, never white). His face is "
        "shown clearly — fair-minded, unsentimental, never cruel."
    ),
    "GARDENER": (
        "GARDENER LOCK: the vine-dresser is the same man in every shot — "
        "about forty, lean and quiet-faced, with a soft dark beard, "
        "deep-set patient eyes and soil worked permanently into the "
        "creases of his hands. He wears a rough DARK MOSS-GREEN work "
        "tunic kilted up, with a rope belt and a pruning knife slung at "
        "it (never cream, never white). His face is shown clearly — "
        "gentleness with a spine."
    ),
    "FIGTREE": (
        "FIG TREE LOCK: the fig tree is the same tree in every shot — "
        "a broad low fig with a forked grey trunk, wide rough leaves, "
        "standing alone in its own circle of ground at the vineyard's "
        "sunniest corner, a low dry-stone wall two paces behind it and "
        "staked vine rows running away downhill beyond. The same fork, "
        "wall and rows in every tree beat."
    ),
    "SQUARE": (
        "VILLAGE SQUARE LOCK: a small village square at the olive "
        "press — a beaten-earth open space with the great stone press "
        "under its lean-to roof, low house fronts, a couple of market "
        "baskets, and listeners of every age in SATURATED DEEP earth "
        "colours: dark browns, deep russet, dark olive, dusty indigo "
        "(never cream, never white; only Jesus wears cream). Faces "
        "shown clearly."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r042-b01", "out": "s01-he-told-them-a-short.jpeg", "seg": "n1",
        "window": "0.28-5.77", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SQUARE"],
        "narration": (
            "He told them a short story about a tree that was not doing its "
            "job. It sounds at first like a warning."
        ),
        "must_show": "the frame — Jesus in the village square by the olive press, the gathered listeners' faces braced for a hard word.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the listeners' wariness visible — a crowd expecting judgment.",
        "scene": (
            "In the bright morning square Jesus stands by the "
            "great stone olive press with the villagers gathered "
            "in close — a grey farmer with his arms folded tight, "
            "a woman gone still over her basket, two young men "
            "trading a wary glance — every face set the way "
            "faces set for bad news, while he begins the story "
            "with the calm of a man carrying better news than "
            "they expect. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r042-b02", "out": "s02-stay-with-it-because-it.jpeg", "seg": "n1",
        "window": "5.77-11.98", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SQUARE"],
        "narration": (
            "Stay with it, because it turns into one of the kindest things he "
            "ever said about being given more time."
        ),
        "must_show": "the promise under the warning — close on Jesus's face: gravity on the surface, and unmistakable kindness banked underneath it.",
        "must_not_show": "no halo, glare or rim-light on Jesus; both layers in one face — the story's whole arc previewed in an expression.",
        "scene": (
            "Close on Jesus's face in the square's morning "
            "light: the brows grave, the mouth set for a hard "
            "telling — and in the warm brown eyes, plainly "
            "visible beneath the gravity, a banked kindness "
            "waiting its turn, like a man delivering a stern "
            "letter he knows ends well. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b03", "out": "s03-he-spake-also-this-parable.jpeg", "seg": "s6a",
        "window": "12.52-14.56", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SQUARE"],
        "narration": "He spake also this parable;",
        "must_show": "the telling begun — Jesus seated now on the press's stone base, the circle settling, a story taking the square.",
        "must_not_show": "no halo, glare or rim-light on Jesus; village-scale intimacy — a town settling onto its heels to listen.",
        "scene": (
            "Jesus has seated himself on the olive press's broad "
            "stone base and the square is settling around him — "
            "men easing down onto their heels, the woman "
            "setting her basket at her feet, a boy worming "
            "through to the front — the morning's business "
            "suspended all around the beaten earth as one story "
            "takes the whole village square for its room. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b04", "out": "s04-a-certain-man-had-a.jpeg", "seg": "jv6",
        "window": "16.09-23.20", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "FIGTREE"],
        "narration": (
            "A certain man had a fig tree planted in his vineyard; and he came "
            "and sought fruit thereon, and found none."
        ),
        "must_show": "SCRIPTURE-EXACT: the seeking — the owner at the fig tree in late-summer light, one hand turning over the broad leaves, finding bare wood beneath every one.",
        "must_not_show": "no halo, glare or rim-light; the search genuine — leaves parted hopefully, nothing under them.",
        "scene": (
            "At the vineyard's sunny corner the square grey-"
            "bearded owner stands in under the fig tree's broad "
            "canopy, one heavy hand turning the wide rough "
            "leaves over one after another — and under every "
            "leaf, bare grey wood: no swelling fruit, not one — "
            "while the staked vine rows behind him hang heavy "
            "with their own honest crop in the late-summer "
            "light. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r042-b05", "out": "s05-a-fig-tree-in-a.jpeg", "seg": "n2",
        "window": "24.75-27.87", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIGTREE"],
        "narration": "A fig tree in a vineyard had the best spot on the whole property.",
        "must_show": "the privilege mapped — the tree in its prime corner: full sun, the wall's shelter, the vine rows' watered slope below it; real estate any tree would envy.",
        "must_not_show": "no halo, glare or rim-light; the spot's excellence readable at a glance — sun, shelter, water, position.",
        "scene": (
            "The fig tree stands in the best ground of the whole "
            "hillside: full morning sun on its crown, the "
            "dry-stone wall breaking the wind two paces behind "
            "it, the watered vine terraces stepping away "
            "downhill below — its own private circle of deep "
            "worked earth at the exact warm corner where any "
            "grower would have put his favourite — a tree "
            "living, by every visible measure, better than the "
            "vines that pay the rent. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b06", "out": "s06-deep-worked-soil-water-meant.jpeg", "seg": "n2",
        "window": "27.87-33.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIGTREE"],
        "narration": (
            "Deep worked soil, water meant for the grapes, a wall around it, "
            "full sun."
        ),
        "must_show": "the inventory of advantages — close at the tree's foot: dark crumbled soil, the irrigation channel running to its ring, the wall's shadow-shelter, sun on the trunk.",
        "must_not_show": "no halo, glare or rim-light; the four gifts each visible — soil, water, wall, sun — in one close frame.",
        "scene": (
            "Close at the fig tree's foot in the morning light: "
            "the soil of its ring dark and crumbled from old "
            "working, a narrow stone irrigation channel bringing "
            "the vines' water right to its circle, the low wall "
            "standing windbreak behind, and full sun lying warm "
            "up the forked grey trunk — four privileges an "
            "auditor could list, gathered at the foot of one "
            "tree. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r042-b07", "out": "s07-everything-a-tree-could-want.jpeg", "seg": "n2",
        "window": "33.99-40.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIGTREE"],
        "narration": (
            "Everything a tree could want was already handed to it. All it had "
            "to do was grow figs."
        ),
        "must_show": "the one job — close up into the healthy leafy canopy: vigorous leaves everywhere, and nowhere among them a single fig.",
        "must_not_show": "no halo, glare or rim-light; health without fruit — the leaves' very vigour is the indictment.",
        "scene": (
            "Looking up into the fig tree's canopy against the "
            "bright sky: broad healthy leaves in their "
            "thousands, glossy and vigorous, layered deep on "
            "every branch — a picture of pure thriving — and in "
            "all that green wealth, from fork to crown, not one "
            "fig anywhere: a tree that has spent everything it "
            "was given on looking magnificent. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b08", "out": "s08-so-the-owner-came-out.jpeg", "seg": "n3",
        "window": "41.01-45.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER", "FIGTREE"],
        "narration": (
            "So the owner came out to pick a few, the way you would. And there "
            "was nothing on it."
        ),
        "must_show": "the ordinary expectation — the owner arrived with a small empty basket on his arm, standing before the tree; the basket says everything about what should have happened.",
        "must_not_show": "no halo, glare or rim-light; the empty basket is the beat — brought in good faith, going home the same way.",
        "scene": (
            "The owner stands before the fig tree with a small "
            "woven picking-basket hanging from one forearm — "
            "brought out the way a man brings a basket to a "
            "tree in fig season, without a second thought — and "
            "the basket hangs exactly as empty as it arrived, "
            "while his flat practical gaze moves over the "
            "fruitless green above it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b09", "out": "s09-not-a-small-crop-not.jpeg", "seg": "n3",
        "window": "45.43-48.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIGTREE"],
        "narration": "Not a small crop. Not a late one.",
        "must_show": "the absoluteness — extreme close along one branch: leaf after leaf lifted aside by a thumb, bare smooth wood at every node where figs form.",
        "must_not_show": "no halo, glare or rim-light; the fig-nodes BARE — the botanical proof of total nothing.",
        "scene": (
            "An extreme close shot along one grey branch in the "
            "bright light: a weathered thumb lifts the broad "
            "leaves aside one by one, and at every node where "
            "this year's figs would sit the wood is smooth and "
            "bare — node after node after node down the "
            "branch's whole length — not few, not late, not "
            "small: none. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r042-b10", "out": "s10-and-this-was-not-the.jpeg", "seg": "n4",
        "window": "51.73-53.40", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "FIGTREE"],
        "narration": "And this was not the first time.",
        "must_show": "the pattern — the owner walking AWAY from the tree with the empty basket, seen from behind, in a light subtly different from the arrival: another year, same walk.",
        "must_not_show": "no halo, glare or rim-light; the walk away, repeated — the composition should feel like déjà vu.",
        "scene": (
            "From behind, in the amber of a fig-season evening: "
            "the owner walks away from the tree down the vine "
            "terrace path, the small basket swinging light and "
            "empty from his arm, his square shoulders carrying "
            "the particular patience of a man doing a walk he "
            "has done before — the fig tree standing full-leafed "
            "and fruitless behind him against the warm sky. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b11", "out": "s11-coming-up-on-three-seasons.jpeg", "seg": "n4",
        "window": "53.40-61.30", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "FIGTREE"],
        "narration": (
            "Coming up on three seasons now he had walked out to that same tree "
            "expecting figs, and walked back with empty hands every time."
        ),
        "must_show": "three years in one frame — the owner at the tree once more, and this time his empty hands held OPEN at his sides, the basket not even brought; hope reduced to habit.",
        "must_not_show": "no halo, glare or rim-light; no basket this year — the small escalation that says three seasons without a word.",
        "scene": (
            "At the fig tree in yet another season's light the "
            "owner stands with no basket at all this time, his "
            "heavy hands hanging open and empty at his sides, "
            "looking up into the same magnificent fruitless "
            "green — a man who has stopped bringing the basket "
            "but not yet stopped coming, three years of empty "
            "walks standing in his patient, hardening face. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r042-b12", "out": "s12-a-fig-tree-gets-a.jpeg", "seg": "n4",
        "window": "61.30-65.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIGTREE"],
        "narration": "A fig tree gets a fair trial, and this one had had a long one.",
        "must_show": "the trial's length made visible — the tree's trunk close: three seasons' growth rings of pruning scars and care marks; years of chances written on the bark.",
        "must_not_show": "no halo, glare or rim-light; the care marks matter — this tree was TENDED through its trial, not neglected.",
        "scene": (
            "Close on the forked grey trunk in even light: the "
            "bark carries its history — old pruning scars healed "
            "over, the neat cuts of three seasons' careful "
            "shaping, a support stake's worn rubbing mark, the "
            "soil ring below dark from years of watering — the "
            "full record of a long, patient, well-resourced "
            "trial, written on the body of the defendant. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b13", "out": "s13-then-said-he-unto-the.jpeg", "seg": "jv7",
        "window": "66.22-79.73", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "GARDENER", "FIGTREE"],
        "narration": (
            "Then said he unto the dresser of his vineyard, Behold, these three "
            "years I come seeking fruit on this fig tree, and find none: cut it "
            "down; why cumbereth it the ground?"
        ),
        "must_show": "SCRIPTURE-EXACT: the order given — the owner speaking to the gardener at the tree, one hand gesturing flat at it, and an axe standing ready against the wall; the sentence pronounced, not executed.",
        "must_not_show": "no halo, glare or rim-light; the axe LEANS, unlifted — present as verdict, never in motion.",
        "scene": (
            "At the tree's foot the owner faces his lean "
            "moss-green-clad gardener, one heavy hand chopping "
            "flat through the air toward the fruitless canopy "
            "as he gives the order — and against the dry-stone "
            "wall behind them a long-handled axe stands leaned "
            "and waiting, brought but not lifted — while the "
            "gardener's soil-creased hands have gone still at "
            "his sides and his patient eyes move from master "
            "to tree. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r042-b14", "out": "s14-bare-leaves-and-no-fruit.jpeg", "seg": "n3",
        "window": "48.24-51.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER", "FIGTREE"],
        "narration": "Bare leaves, and no fruit at all.",
        "must_show": "the verdict's evidence — the owner's open empty palm held up beneath a laden-looking branch; the hand that should be full.",
        "must_not_show": "no halo, glare or rim-light; the empty palm under abundant leaves — promise above, nothing delivered into the hand.",
        "scene": (
            "Close beneath the canopy: the owner's broad "
            "weathered palm held open and upward directly "
            "beneath a branch heavy with magnificent leaves — "
            "the exact gesture of a man catching fruit — and "
            "nothing in the palm, nothing coming, the green "
            "above it all foliage and no gift, the oldest "
            "disappointment in farming resting in one empty "
            "hand. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r042-b15", "out": "s15-and-you-can-hear-that.jpeg", "seg": "n5",
        "window": "81.22-86.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER"],
        "narration": (
            "And you can hear that he is not being cruel. His last words are "
            "just plain sense."
        ),
        "must_show": "the owner's fairness — a close portrait: a reasonable man's face, tired of waiting, without a flicker of malice anywhere in it.",
        "must_not_show": "no halo, glare or rim-light; no villainy — the row NEEDS his fairness; weariness and sense, nothing darker.",
        "scene": (
            "A close portrait of the owner in the clear light: "
            "the clipped grey beard, the flat practical gaze, "
            "the weather-lines of sixty seasons — and in the "
            "whole face nothing but a fair man's tiredness: no "
            "spite, no heat, only the settled reasonableness of "
            "someone who has waited three years past hoping and "
            "is now speaking plain arithmetic about ground. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b16", "out": "s16-the-tree-is-holding-a.jpeg", "seg": "n5",
        "window": "86.35-92.84", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIGTREE"],
        "narration": (
            "The tree is holding a place a fruitful one could be using, and any "
            "farmer in that crowd would have nodded."
        ),
        "must_show": "the opportunity cost — beside the barren tree's corner, a young potted fig sapling waiting on the path with its roots balled; the replacement, ready.",
        "must_not_show": "no halo, glare or rim-light; the sapling small and hopeful — the ground's other possible future, standing by.",
        "scene": (
            "On the terrace path beside the barren tree's prime "
            "corner a young fig sapling stands waiting, its "
            "roots balled in sacking, two bright first leaves "
            "up — small, unproven and ready — while above it the "
            "great fruitless tree holds the best ground on the "
            "hill with its magnificent useless green: the whole "
            "economics of the verdict standing in one frame. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b17", "out": "s17-it-was-a-fair-call.jpeg", "seg": "n5",
        "window": "92.84-94.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["SQUARE"],
        "narration": "It was a fair call.",
        "must_show": "the crowd's agreement — close on two farmer faces in the square nodding slowly; the audience siding with the axe.",
        "must_not_show": "no halo, glare or rim-light; honest agreement — these listeners know ground and seasons; their nod is expertise.",
        "scene": (
            "Close in the listening square: two old farmers "
            "side by side nodding slowly at the story's verdict "
            "— one with his lips pursed in professional "
            "agreement, the other's calloused hand tipping "
            "briefly palm-up in the universal gesture of "
            "fair-is-fair — the sentence seconded by every man "
            "present who has ever cleared a fruitless tree "
            "himself. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r042-b18", "out": "s18-and-he-answering-said-unto.jpeg", "seg": "jv8",
        "window": "95.04-102.42", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "GARDENER", "FIGTREE"],
        "narration": (
            "And he answering said unto him, Lord, let it alone this year also, "
            "till I shall dig about it, and dung it:"
        ),
        "must_show": "SCRIPTURE-EXACT: the intercession — the gardener physically STEPPED BETWEEN the owner and the tree, one soil-creased hand raised gently, asking for the year.",
        "must_not_show": "no halo, glare or rim-light; his body between sentence and tree is the composition's law — gentle, unshakable.",
        "scene": (
            "In the hard noon light the lean gardener has "
            "stepped quietly into the space between his master "
            "and the condemned tree — his back almost brushing "
            "the grey trunk, his soil-dark hand raised gently "
            "palm-out toward the owner, his patient deep-set "
            "eyes making the request his low voice carries — a "
            "working man spending his standing with his master "
            "on a tree that has never paid him anything. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b19", "out": "s19-the-gardener-steps-between-the.jpeg", "seg": "n6",
        "window": "103.87-110.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDENER"],
        "narration": (
            "The gardener steps between the sentence and the tree. He does not "
            "deny the failure; he volunteers his own labor."
        ),
        "must_show": "the offer's shape — close on the gardener's two opened soil-creased hands, offered forward: not an argument, a volunteering.",
        "must_not_show": "no halo, glare or rim-light; the hands ARE the plea — labour offered where excuses were owed.",
        "scene": (
            "Close in the noon light: the gardener's two hands "
            "held open and forward, palms up — soil worked so "
            "deep into their creases that the lines read like "
            "dark script, old vine-thorn scars across the "
            "knuckles — offered the way other men offer "
            "arguments: here is my labour, take it instead — "
            "the only currency he owns, all of it on the table. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b20", "out": "s20-and-look-at-what-he.jpeg", "seg": "n7",
        "window": "110.95-113.23", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDENER", "FIGTREE"],
        "narration": "And look at what he offers to do with that year.",
        "must_show": "the year's plan begun — the gardener down on his knees at the tree's foot with his mattock laid ready, rolling up his sleeves; the work about to start.",
        "must_not_show": "no halo, glare or rim-light; intention becoming labour — sleeves, knees, tools; autumn's softer light beginning.",
        "scene": (
            "In the soft gold of early autumn the gardener "
            "kneels down at the fig tree's foot, pushing his "
            "moss-green sleeves above his elbows, his short "
            "mattock and a woven basket set ready on the ground "
            "beside him — the granted year beginning not with a "
            "speech but with a man getting down onto his knees "
            "in the dirt of someone else's second chance. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b21", "out": "s21-get-down-and-break-up.jpeg", "seg": "n7",
        "window": "113.23-120.95", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDENER", "FIGTREE"],
        "narration": (
            "Get down and break up the hard, packed earth around the roots, so "
            "the tree can finally breathe and drink. Not scold the tree."
        ),
        "must_show": "SCRIPTURE-EXACT: the digging — the gardener working the mattock through the packed ring, broken dark clods turning up around the trunk in a widening worked circle.",
        "must_not_show": "no halo, glare or rim-light; real labour — sweat, turned earth, the ring visibly half-broken; care shown as effort, not sentiment.",
        "scene": (
            "The gardener works on his knees around the trunk, "
            "the short mattock swinging in tight strokes, the "
            "hard grey crust of the tree's ring breaking up "
            "into dark turned clods behind his hands — half the "
            "circle already worked open and breathing, sweat "
            "darkening the back of his tunic, the roots' first "
            "pale shoulders showing in the opened earth — a "
            "scolding's opposite, delivered by mattock. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b22", "out": "s22-work-the-soil-and-then.jpeg", "seg": "n7 + n8",
        "window": "120.95-124.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDENER", "FIGTREE"],
        "narration": "Work the soil. And then feed it.",
        "must_show": "the feeding — the gardener tipping a basket of dark dung and straw into the dug ring, working it in with bare hands.",
        "must_not_show": "no halo, glare or rim-light; earthy and clean — baskets and worked soil; the humility of the job unhidden.",
        "scene": (
            "Close at the dug ring in the autumn light: the "
            "gardener tips a heavy basket of dark dung and "
            "straw down into the broken earth and works it in "
            "with his bare hands, folding the feed deep along "
            "the pale roots, his forearms dark to the elbow — "
            "the richest gift a farm knows, delivered by hand "
            "into the ground of a tree still owing everything. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b23", "out": "s23-the-lowest-messiest-job-on.jpeg", "seg": "n8",
        "window": "124.12-131.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDENER"],
        "narration": (
            "The lowest, messiest job on the whole farm, done by hand at the "
            "foot of a tree that has given him nothing back."
        ),
        "must_show": "the cost on the man — close on the gardener's dirt-dark forearms and quiet face mid-labour: no audience, no complaint, no reward in sight.",
        "must_not_show": "no halo, glare or rim-light; dignity in the dirt — his face content in work nobody thanks.",
        "scene": (
            "Close on the gardener mid-labour in the soft "
            "light: forearms black to the elbow with worked "
            "dung and soil, a smear across one cheekbone where "
            "he pushed his hair back, his soft-bearded face "
            "bent to the ring in complete unhurried absorption "
            "— a man doing the farm's lowest work with the "
            "quality of attention most men save for their own "
            "harvest. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r042-b24", "out": "s24-he-is-not-asking-for.jpeg", "seg": "n8",
        "window": "131.24-137.72", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDENER", "FIGTREE"],
        "narration": (
            "He is not asking for time so he can wait and watch. He is asking "
            "for time so he can go to work."
        ),
        "must_show": "the year as labour — the finished ring: the tree's whole circle dug, fed and watered dark, tools shouldered, the gardener looking up into the branches with working hope.",
        "must_not_show": "no halo, glare or rim-light; the COMPLETED ring is the proof — a year's argument made of turned earth.",
        "scene": (
            "In the low gold of the autumn afternoon the work "
            "stands finished: the fig tree's whole ring dug "
            "wide, fed dark and watered to a deep wet brown, "
            "the channel cleared to it, the earth's circle as "
            "tended as a garden bed — and the gardener stands "
            "back with the mattock over his shoulder, looking "
            "up into the bare autumn branches with the level, "
            "working hope of a man whose asking is done in "
            "dirt. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r042-b25", "out": "s25-and-if-it-bear-fruit.jpeg", "seg": "jv9",
        "window": "138.24-143.81", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "GARDENER", "FIGTREE"],
        "narration": (
            "And if it bear fruit, well: and if not, then after that thou shalt "
            "cut it down."
        ),
        "must_show": "SCRIPTURE-EXACT: the terms accepted — the owner and gardener at the tended tree, the owner's slow nod given, the axe being carried AWAY toward the shed.",
        "must_not_show": "no halo, glare or rim-light; the axe leaves the frame's future — carried off, not destroyed; the year is real and so are its terms.",
        "scene": (
            "At the tree's tended ring the owner gives his slow "
            "single nod, arms folded, the terms set — and the "
            "gardener is already walking the long-handled axe "
            "away down the terrace path toward the tool shed, "
            "carrying it out of the tree's year — behind them "
            "the freshly worked circle lies dark and ready "
            "under the bare branches, holding twelve months in "
            "its earth. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r042-b26", "out": "s26-the-ending-is-deliberately-unfinished.jpeg", "seg": "n9",
        "window": "145.34-147.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIGTREE"],
        "narration": "The ending is deliberately unfinished.",
        "must_show": "the open ending — the tree at winter's edge under a wide grey-gold sky, ring tended, branches bare, everything waiting; no resolution anywhere.",
        "must_not_show": "no halo, glare or rim-light; suspension as composition — a held breath of a frame.",
        "scene": (
            "The fig tree stands bare-branched at the edge of "
            "winter under a wide grey-gold evening sky, its "
            "dark tended ring the only worked ground on the "
            "sleeping hillside, the vine rows pruned back to "
            "stumps beyond — everything on the hill paused "
            "between verdicts, one tree's whole future folded "
            "invisibly inside grey twigs, and the picture "
            "refusing, on purpose, to say. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b27", "out": "s27-jesus-leaves-his-listeners-inside.jpeg", "seg": "n9 + n10",
        "window": "147.34-154.65", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SQUARE"],
        "narration": (
            "Jesus leaves his listeners inside that extra year, while mercy is "
            "still at work. Here is the part worth sitting with."
        ),
        "must_show": "the story stopped short — Jesus in the square with his hands folded closed, the tale visibly ended mid-air, the listeners left leaning toward an ending that doesn't come.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the crowd's suspended lean — an audience left inside the granted year with the tree.",
        "scene": (
            "In the square Jesus has folded his hands closed "
            "in his lap — the story stopped, plainly and "
            "deliberately, one sentence before its ending — and "
            "the whole listening circle hangs leaned forward "
            "into the silence: the boy at the front with his "
            "mouth open, the grey farmer's brows up waiting "
            "for the verdict, every face suspended inside the "
            "extra year with the tree, exactly where the "
            "teller wants them living. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b28", "out": "s28-the-tree-had-not-changed.jpeg", "seg": "n10",
        "window": "154.65-160.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIGTREE"],
        "narration": (
            "The tree had not changed. It had not turned itself around or grown "
            "a single fig overnight."
        ),
        "must_show": "the unchanged defendant — the bare tree exactly as it was, no fruit, no transformation; only the worked ground beneath it is different.",
        "must_not_show": "no halo, glare or rim-light; NO figs, no buds yet — the mercy preceded every improvement.",
        "scene": (
            "Close on the fig tree in the flat winter light: "
            "the same forked grey trunk, the same bare "
            "fruitless branches against the pale sky, not one "
            "bud broken, not one thing about the tree itself "
            "different from the day the axe was ordered — and "
            "below it, the only change in the picture: the "
            "ring of dark, fed, worked earth somebody else put "
            "there. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r042-b29", "out": "s29-it-got-its-extra-year.jpeg", "seg": "n10",
        "window": "160.35-167.44", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDENER", "FIGTREE"],
        "narration": (
            "It got its extra year for one reason only. Someone who cared for "
            "it stood between it and the axe and asked."
        ),
        "must_show": "the reason reprised — the intercession image again at its purest: the gardener standing quietly at the tree's trunk, one hand resting on the bark; guardian and ward.",
        "must_not_show": "no halo, glare or rim-light; the hand on the bark — ownership of the risk; tenderness with a spine.",
        "scene": (
            "In the still winter light the gardener stands "
            "close in at the fig tree's trunk with one "
            "soil-creased hand resting flat on the grey bark, "
            "the way a man rests a hand on a younger brother's "
            "shoulder before a magistrate — his patient face "
            "turned outward, toward whatever comes down the "
            "path — the whole granted year standing in one "
            "unspectacular posture: between. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b30", "out": "s30-that-is-the-whole-picture.jpeg", "seg": "n10b",
        "window": "167.95-171.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIGTREE"],
        "narration": "That is the whole picture. Not a tree earning its keep.",
        "must_show": "unearned time — the bare tree with its rich tended ring, and lying at the ring's edge, the gardener's mattock at rest: the labour was never the tree's.",
        "must_not_show": "no halo, glare or rim-light; the tools at the TREE'S foot but never the tree's — grace's arithmetic in still life.",
        "scene": (
            "A quiet frame at the tree's foot: the bare "
            "fruitless branches above, the dark expensively "
            "tended ring below — and resting at the ring's "
            "edge, the gardener's worn mattock and emptied "
            "basket, another man's tools at the foot of a tree "
            "that has never lifted anything — the entire "
            "economy of the granted year lying in plain sight "
            "on the ground. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r042-b31", "out": "s31-a-gardener-buying-it-time.jpeg", "seg": "n10b + n11",
        "window": "171.69-178.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDENER"],
        "narration": (
            "A gardener buying it time it could never have bought for itself. "
            "He never tells us who the gardener is."
        ),
        "must_show": "the unnamed intercessor — a close portrait of the gardener's quiet face, half-turned from the camera toward his tree; identity withheld, character complete.",
        "must_not_show": "no halo, glare or rim-light; the half-turn keeps the mystery — the face readable, the naming left undone.",
        "scene": (
            "A close portrait in the soft light: the gardener's "
            "quiet soft-bearded face in three-quarter turn away "
            "toward his tree, deep-set eyes steady on it, soil "
            "on his cheekbone — near enough to know completely, "
            "turned enough to leave unnamed — the story's "
            "deliberate blank, wearing a working man's face. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r042-b32", "out": "s32-he-does-not-have-to.jpeg", "seg": "n11",
        "window": "178.00-182.92", "wide": True, "jesus": False, "ref": False,
        "locks": ["SQUARE"],
        "narration": (
            "He does not have to. Everyone listening knew what it felt like to "
            "be the barren tree."
        ),
        "must_show": "the self-recognition — the square's faces gone inward: each listener quietly somewhere else, seeing their own bare branches.",
        "must_not_show": "no halo, glare or rim-light; inwardness on every face — a crowd of people privately identified.",
        "scene": (
            "Around the square the story has gone inside "
            "people: the grey farmer's eyes fixed on the "
            "ground between his feet, the woman's hand stilled "
            "on her basket rim, the young man's jaw working at "
            "something years old, even the boy at the front "
            "gone thoughtful — a crowd of separate silences, "
            "every one of them standing privately in the same "
            "unfruitful orchard. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b33", "out": "s33-and-every-one-of-them.jpeg", "seg": "n11",
        "window": "182.92-189.85", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SQUARE"],
        "narration": (
            "And every one of them just heard that there is Someone in the "
            "vineyard whose first move is to ask for more time on your behalf."
        ),
        "must_show": "the news landing as relief — faces lifting around the square; and Jesus watching the relief arrive with quiet purpose: this was the point.",
        "must_not_show": "no halo, glare or rim-light on Jesus; relief spreading like warmth — the warning fully turned into kindness.",
        "scene": (
            "The faces are lifting around the square — the "
            "farmer's head coming up with something eased in "
            "it, the woman's breath visibly let go, the young "
            "man blinking fast — and on the press's stone base "
            "Jesus watches the relief move through them with "
            "the quiet, satisfied purpose of a man whose hard "
            "story has just delivered its true cargo. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r042-b34", "out": "s34-so-the-story-he-told.jpeg", "seg": "n12",
        "window": "190.39-193.74", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SQUARE"],
        "narration": (
            "So the story he told to warn them turns out to be the story that "
            "saves them."
        ),
        "must_show": "the reversal complete — close on Jesus's face, the banked kindness from the second beat now fully out in the open.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the bookend face — gravity spent, warmth revealed.",
        "scene": (
            "Close on Jesus's face in the square's late-morning "
            "light: the gravity of the telling has lifted away "
            "and the kindness that was banked beneath it in the "
            "story's first minute now stands fully in the open "
            "— warm brown eyes resting on his listeners, the "
            "faintest smile inside the beard — the warning's "
            "whole journey to mercy completed in one face. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r042-b35", "out": "s35-the-owner-had-every-right.jpeg", "seg": "n12",
        "window": "193.74-200.00", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIGTREE"],
        "narration": (
            "The owner had every right to the axe. The gardener asked for the "
            "year. And the tree is still standing."
        ),
        "must_show": "the closing image — the fig tree at the NEXT spring's first light: still standing in its tended ring, and along one grey branch, the first small green buds just broken.",
        "must_not_show": "no halo, glare or rim-light; buds only — no figs, no proof, just the year being USED; hope exactly the story's size.",
        "scene": (
            "First light of the new spring on the vineyard "
            "hill: the fig tree stands in its dark tended ring "
            "with the mist still in the vine rows below — and "
            "along one low grey branch, small and new and "
            "unproven, the first green buds have broken, a "
            "sparse scatter of beginnings no bigger than "
            "barley corns — no figs yet, no verdict yet, just "
            "a tree still standing in its bought year, "
            "starting. Every figure has two arms, two hands "
            "and one head."
        ),
    },
]
