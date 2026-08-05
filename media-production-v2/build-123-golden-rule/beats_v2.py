#!/usr/bin/env python3
"""V2 beat map — row 123, build-123-golden-rule (Matthew 7:12; Luke 6:38).

COVERAGE: 23 pictures over 129.8 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (KJV):
  Matt 7:12 "Therefore ALL THINGS WHATSOEVER ye would that men should
        do to you, DO YE EVEN SO TO THEM: for THIS IS THE LAW AND THE
        PROPHETS." — the whole law in one sentence.
  Luke 6:38 "GIVE, and it shall be given unto you; GOOD MEASURE,
        PRESSED DOWN, and SHAKEN TOGETHER, and RUNNING OVER, shall
        men give INTO YOUR BOSOM." — the bosom is the gathered
        lap-fold of a robe, the period way of carrying grain.
  Setting: the same Sermon on the Mount hillside as rows 121-122 —
  same slope, same lake, same congregation.

RENDERING LAWS:
  - HILLSIDE and CROWD locks are BYTE-IDENTICAL to builds 121/122
    (same sermon, same slope, same congregation) — cross-video
    continuity.
  - The rule is illustrated by KINDNESS VIGNETTES in one village and
    on one road — each vignette is the wish and the deed in the same
    frame: bread handed at the door, the drink held out unasked,
    forgiveness given, the stumbled man lifted. Every action must
    read at a glance (Cameron's action-logic law); givers look at
    the RECEIVER, never at any audience.
  - Luke's measure is rendered PERIOD-TRUE: grain poured into the
    gathered lap-fold ("bosom") of a receiver's robe — pressed down,
    shaken, running over. It rhymes with row 122's measure beats.
  - The vignette people are ordinary and varied — no clone faces
    (rows 90/107); nobody is a costume villain; the passer-by who
    stops was never shown sneering.

TIME OF DAY ARC (intentional): the hillside in the same warm late-
afternoon gold as rows 121-122 throughout; the village and road
vignettes in bright working day; the village-carrying-one-another
beat at warm lamplit evening BY DESIGN; the close in golden last
light.

CHANGING CONDITION (kept OUT of the locks): the measure — level
wish in the teaching, running-over into the lap-fold in the giving
beats; the stumbled man — down in the dust, then lifted and
re-shouldered.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "HILLSIDE": (
        "HILLSIDE LOCK: the teaching hillside — a green grassy slope "
        "above the Sea of Galilee, wildflowers in the grass, the "
        "blue lake and far hills below, warm late-afternoon light. "
        "The same slope and lake view throughout."
    ),
    "CROWD": (
        "CROWD LOCK: the listening crowd — ordinary Galileans seated "
        "on the grass: weathered fishermen, mothers with children, "
        "sun-browned farmers, a few elders; varied earth-toned robes "
        "of brown, rust, olive and slate (no cream — only Jesus "
        "wears cream), varied ages and faces, never uniform."
    ),
    "VILLAGE": (
        "VILLAGE LOCK: the village — a lane of stone-and-mudbrick "
        "houses with wooden doors and low walls, fig trees between "
        "rooflines, a communal well at the lane's head. The same "
        "lane, doors and well throughout."
    ),
    "ROAD": (
        "ROAD LOCK: the country road — a pale dusty track between "
        "dry-stone walls and olive terraces under bright sky, far "
        "hills beyond. The same track and walls throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r123-b01", "out": "s01-to-be-seen-when-we.jpeg", "seg": "n2",
        "window": "34.36-36.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE"],
        "narration": "To be seen when we are tired.",
        "must_show": "the longing pictured — a weary woman sunk onto a doorstep with her water jars, and a neighbour crouched down to her level, simply seeing her; attention as kindness.",
        "must_not_show": "no halo; nothing given but ATTENTION — no bread or coin in this frame; the seeing is the gift.",
        "scene": (
            "The first longing is only to be noticed: a woman sunk "
            "onto the worn doorstep with her two water jars still "
            "yoked, eyes closed against the long day — and a "
            "neighbour who has stopped, crouched down to her level "
            "with nothing in his hands at all, his whole face "
            "simply finding hers — no coin, no bread, no advice, "
            "just the oldest kindness in the world: somebody "
            "tired, being seen by somebody who stopped. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b02", "out": "s02-of-everything-jesus-taught-on.jpeg", "seg": "n1",
        "window": "0.28-11.66", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Of everything Jesus taught on that hillside, he gave the whole "
            "law of how to treat each other in a single sentence — one so "
            "simple a child can live it, and so deep it holds up everything "
            "else."
        ),
        "must_show": "the same Sermon hillside — Jesus seated teaching, the ordinary crowd on the grass, a child near the front listening as easily as the elders; the one-sentence law about to be given.",
        "must_not_show": "no halo, glare or rim-light on Jesus; a CHILD visible and at ease near the front — the simplicity embodied.",
        "scene": (
            "The same hillside holds its simplest hour, the camera "
            "looking past the seated crowd's backs up the slope: "
            "Jesus seated in the warm gold above the blue lake, the "
            "fishermen and mothers and farmers settled in the "
            "grass — and near the front, cross-legged and entirely "
            "unintimidated, a small child listening as easily as "
            "the elders around her — the right audience arrangement "
            "for a law so simple a child can live it and so deep "
            "it will hold up everything else ever asked of them. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b03", "out": "s03-therefore-all-things-whatsoever-ye.jpeg", "seg": "jvA",
        "window": "12.22-20.95", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Therefore all things whatsoever ye would that men should do to "
            "you, do ye even so to them: for this is the law and the "
            "prophets."
        ),
        "must_show": "SCRIPTURE-EXACT: the sentence given — Jesus with one hand at his own chest and the other open toward the crowd, the rule's two directions in one gesture; the crowd very still.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gesture SIMPLE — chest to crowd, nothing ornate.",
        "scene": (
            "The whole law crosses the air in one gesture: Jesus "
            "with one hand resting at his own chest — whatsoever "
            "ye would for YOU — and the other opening out toward "
            "the crowd — do even so for THEM — the two directions "
            "of the entire law and prophets travelling between "
            "his hands in the gold light, while the hillside "
            "holds the particular stillness of people receiving "
            "something they can tell, already, they will be "
            "repeating for the rest of their lives. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b04", "out": "s04-that-is-the-law-and.jpeg", "seg": "n2",
        "window": "27.20-31.04", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "That is the law and the prophets, the whole of it, in one line.",
        "must_show": "the compression — a synagogue niche of many heavy law scrolls, and lying before them one small strip of parchment with a single written line; the whole shelf in one sentence.",
        "must_not_show": "no halo; NO readable modern lettering — the writing indistinct period script; the contrast of scale carries it.",
        "scene": (
            "The comparison sits on one shelf: a synagogue niche "
            "stacked deep with the law's heavy scrolls — leather "
            "and wood and years of careful ink, a lifetime's "
            "reading in rolled thunder — and laid on the sill "
            "before them a single narrow strip of parchment "
            "bearing one short line of indistinct script — the "
            "whole towering shelf compressed into a sentence a "
            "child can carry — the entire library and its summary "
            "sharing the same quiet lamplight. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b05", "out": "s05-however-you-wish-people-would.jpeg", "seg": "n2",
        "window": "22.70-27.20", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "However you wish people would treat you, he said — go and treat "
            "them that way."
        ),
        "must_show": "the rule restated — over the shoulders of front-row listeners, Jesus leaning toward them, the sentence landing on near faces.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the framing INTIMATE — teacher to near listeners.",
        "scene": (
            "The restatement comes in close, over the shoulders "
            "of the front row: Jesus leaning toward his nearest "
            "listeners with the sentence in its plainest clothes "
            "— however you WISH they would treat you, go treat "
            "them exactly that way — the deep brown eyes moving "
            "from face to face as if fitting the rule to each "
            "one personally, and the fishermen and mothers "
            "nearest him receiving it the way people receive "
            "directions to somewhere they have always wanted to "
            "go. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r123-b06", "out": "s06-and-every-one-of-us.jpeg", "seg": "n2",
        "window": "31.04-34.36", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "And every one of us already knows how we long to be treated.",
        "must_show": "the knowing — along the crowd, faces gone briefly inward: eyes down or distant, each privately consulting their own longing; the shared secret visible.",
        "must_not_show": "no halo; the inwardness QUIET — no tears, no drama; a row of people remembering.",
        "scene": (
            "The sermon pauses while everyone checks the answer "
            "they already own: along the seated rows the faces "
            "go briefly inward — a fisherman's eyes dropping to "
            "his scarred hands, an old woman looking through the "
            "lake to somewhere years away, a young man's jaw "
            "working — every listener privately consulting the "
            "one subject on which each of them is the world's "
            "leading expert: exactly, precisely how they long to "
            "be treated. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r123-b07", "out": "s07-to-be-fed-when-we.jpeg", "seg": "n2",
        "window": "36.50-38.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE"],
        "narration": "To be fed when we are hungry.",
        "must_show": "the longing pictured — a travel-worn man at a table being served a full bowl and bread, the relief plain on him; hunger met simply.",
        "must_not_show": "no halo; the meal PLAIN — bread, stew, water; the dignity in being served, not in the food.",
        "scene": (
            "The second longing sits down at a table: a travel-"
            "worn man with the dust still on his shoulders, and "
            "sliding in front of him a full clay bowl and a round "
            "loaf broken open, steam rising in the doorway light — "
            "his two hands coming up around the warm bowl with "
            "the unguarded relief that only the genuinely hungry "
            "ever show — fed, simply fed, the plainest of all the "
            "wishes and the easiest one in the world to grant. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b08", "out": "s08-that-longing-is-not-selfish.jpeg", "seg": "n2",
        "window": "40.65-45.03", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "That longing is not selfish — it is the measuring line.",
        "must_show": "the measuring line literal — a builder's marked cord pulled taut between two work-worn hands over stone; the longing repurposed as the standard.",
        "must_not_show": "no halo; period-true — a knotted/marked cord, no modern tape or tools.",
        "scene": (
            "What the longing is FOR gets shown in a builder's "
            "hands: a marked measuring cord pulled taut between "
            "two work-worn fists over a course of cut stone, the "
            "knots spaced true, the line straight as a sunbeam — "
            "not a thing to be ashamed of but a TOOL: the "
            "standard you check every stone against — the heart's "
            "own longing, pulled tight and honest, becoming the "
            "line every kindness in the village gets measured "
            "with. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r123-b09", "out": "s09-so-jesus-turns-it-outward.jpeg", "seg": "n3",
        "window": "45.66-47.30", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": "So Jesus turns it outward.",
        "must_show": "the turn — Jesus's hand arcing from his own chest outward toward the world beyond the crowd; the longing redirected in one motion.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the arc READABLE — chest to horizon, one clean motion.",
        "scene": (
            "One motion turns the whole subject inside out: "
            "Jesus's hand starts flat at his own chest — where "
            "every longing lives — and arcs open outward past "
            "the crowd toward the villages and roads below the "
            "hill, the fingers opening as they go — the same "
            "wanting, aimed the other direction — and the eyes "
            "of the listeners follow the hand out over their own "
            "shoulders toward every door and stranger the arc "
            "just included. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r123-b10", "out": "s10-the-bread-you-wish-someone.jpeg", "seg": "n3",
        "window": "47.30-54.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE"],
        "narration": (
            "The bread you wish someone would hand you when you are empty — "
            "hand it to the next person you find standing at your door with "
            "nothing."
        ),
        "must_show": "the deed — at the wooden door, a householder pressing a round loaf into the hands of a ragged man who came with nothing; the giver's eyes on the receiver's face.",
        "must_not_show": "no halo; the giver looks at the MAN, never around for witnesses; the receiver's dignity whole.",
        "scene": (
            "The wish becomes a deed at a wooden door: the "
            "householder presses a round loaf, still warm, into "
            "the cupped hands of the ragged man who knocked with "
            "nothing — and the giving is done the way the giver "
            "would want it done to him: quickly, warmly, the "
            "giver's whole gaze on the receiver's face and not "
            "one glance spent on the street, the bread passing "
            "from hand to hand like something owed rather than "
            "spared — the golden rule, cash on delivery. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b11", "out": "s11-the-cool-drink-you-would.jpeg", "seg": "n4",
        "window": "55.21-63.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROAD"],
        "narration": (
            "The cool drink you would want on a long, dusty road — be the "
            "one who holds it out to the stranger before he even thinks to "
            "ask."
        ),
        "must_show": "the unasked gift — on the bright dusty road, a villager already holding out a dripping water-skin to a parched stranger whose hand has not yet risen to ask; the beating-to-it visible.",
        "must_not_show": "no halo; the TIMING is the picture — the stranger's surprise, the drink arriving before the request.",
        "scene": (
            "The kindness arrives before the request can: on the "
            "pale dusty track a villager stands already holding "
            "out a dripping water-skin — arm extended, offer "
            "complete — while the parched stranger's own hand has "
            "not yet even risen to ask, his cracked lips still "
            "parting around the question he no longer needs — "
            "beaten to it, the wish met a full sentence early by "
            "somebody who knew the road's thirst from the inside "
            "and refused to make a tired man say it out loud. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b12", "out": "s12-to-be-forgiven-when-we.jpeg", "seg": "n2",
        "window": "38.49-40.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE"],
        "narration": "To be forgiven when we have failed.",
        "must_show": "the longing pictured — a young man with head bowed in honest shame, and an elder's hand already resting warm on his shoulder; forgiveness ahead of the apology's end.",
        "must_not_show": "no halo; no grovelling — the shame honest, the hand warmer than the failure was heavy.",
        "scene": (
            "The third longing is the hardest to say out loud: a "
            "young man stands with his head bowed in the lane, "
            "the apology still unfinished in his mouth — and "
            "already, before the sentence can even land, the "
            "elder's hand has come to rest warm and heavy on his "
            "shoulder, the old face above it holding no ledger "
            "at all — forgiveness arriving the way everyone "
            "aches for it to arrive: early, full, and without "
            "the interest charged. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b13", "out": "s13-and-the-mercy-you-would.jpeg", "seg": "n5",
        "window": "63.89-72.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE"],
        "narration": (
            "And the mercy you would ache for if it were your own mistake "
            "laid bare — give that first, and give it fully, to the person "
            "who wronged you."
        ),
        "must_show": "the mercy given — amid a toppled cart and broken oil jars, the WRONGED owner reaching a hand down to lift the ashamed spiller to his feet; mercy moving first.",
        "must_not_show": "no halo; ACTION-LOGIC — the owner's hand lifts UP the wrongdoer, unmistakably help, never seizure; both faces readable.",
        "scene": (
            "The mercy moves before the excuse can form: between "
            "them the toppled handcart and two broken oil jars "
            "darkening the lane's dust — the mistake laid bare "
            "for the whole street — and the man whose oil it was "
            "is already bending with his hand held DOWN to the "
            "ashamed spiller crouched in the wreckage, palm open, "
            "lifting him up out of his own accident — the wronged "
            "party giving first and giving fully the exact mercy "
            "he would ache for if the jars had been the other "
            "man's. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r123-b14", "out": "s14-when-someone-stumbles-on-the.jpeg", "seg": "n6",
        "window": "72.89-76.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROAD"],
        "narration": "When someone stumbles on the road ahead of you, do not step around him.",
        "must_show": "the choice — a man down on his knees in the road dust with his load scattered, and behind him a traveller stopped mid-stride, turning TOWARD him; the not-stepping-around caught live.",
        "must_not_show": "no halo; DIRECTION LAW — the traveller's turn toward the fallen man unmistakable; nobody sneering, nobody posed.",
        "scene": (
            "The road offers its daily fork: ahead on the track a "
            "man is down on his knees in the dust, his shoulder-"
            "load burst and scattered — figs and bundles across "
            "the stones — and behind him a traveller has stopped "
            "mid-stride, his whole body caught in the turn "
            "TOWARD the fallen man, the easy space for stepping "
            "around lying open and unused at the road's edge — "
            "the choice every road serves, being made the right "
            "way in plain view. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r123-b15", "out": "s15-lift-him-the-way-you.jpeg", "seg": "n6",
        "window": "76.46-80.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROAD"],
        "narration": (
            "Lift him the way you would want to be lifted if it were your "
            "own knees in the dust."
        ),
        "must_show": "the lift — the traveller's forearm gripped with the fallen man's, hauling him honestly to his feet, the scattered load already half-regathered between them.",
        "must_not_show": "no halo; ACTION-LOGIC — a real workman's forearm-to-forearm grip; the lift's effort visible and kind.",
        "scene": (
            "The lift is done the way the lifter would want it: "
            "forearm locked to forearm in the honest workman's "
            "grip, the traveller hauls the fallen man up out of "
            "the dust with his own weight thrown back into it — "
            "no dainty fingertips, a real lift for a real fall — "
            "while between them the scattered figs and bundles "
            "are already half-regathered into the mended load, "
            "two men briefly one machine, doing for each other "
            "what knees in the dust always hope for. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b16", "out": "s16-give-and-it-shall-be.jpeg", "seg": "jvB",
        "window": "81.49-92.03", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE"],
        "narration": (
            "Give, and it shall be given unto you; good measure, pressed "
            "down, and shaken together, and running over, shall men give "
            "into your bosom."
        ),
        "must_show": "SCRIPTURE-EXACT: the bosom-measure — grain poured generous into the gathered lap-fold of a receiver's robe: pressed down, shaken together, running over the fold's edges; the period image exact.",
        "must_not_show": "no halo; the BOSOM is the robe's gathered lap-fold (period-true), grain overflowing it; joy on both faces.",
        "scene": (
            "The verse is paid out in period coin: the receiver "
            "holds the front of his robe gathered into the deep "
            "lap-fold his grandfathers called the bosom, and "
            "into it the giver pours grain in a bright rush — "
            "then presses it down with a flat palm, shakes the "
            "fold to settle it, and pours AGAIN until the wheat "
            "runs live over the edges and down the robe — good "
            "measure by the full ritual, both faces laughing at "
            "the arithmetic of a generosity that will not stop "
            "at level. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r123-b17", "out": "s17-the-golden-rule-is-not.jpeg", "seg": "n8",
        "window": "117.67-120.06", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": "The golden rule is not a weight Jesus laid on us.",
        "must_show": "the lightness — close on Jesus, hands open and visibly empty and unburdened, turned palm-up; nothing heavy anywhere in the frame.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hands EMPTY — no scroll, no yoke, nothing carried.",
        "scene": (
            "What he laid on them weighs nothing at all: close on "
            "Jesus with both hands open and turned palm-up in the "
            "warm light — visibly empty, visibly light, nothing "
            "in them to lift and nothing to carry — the face "
            "above the open hands easy and unburdened as the "
            "gesture — a teacher showing his people the actual "
            "heft of the rule he just gave them, which is the "
            "heft of a sentence, and lighter than any single "
            "thing the law ever asked before it. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b18", "out": "s18-give-he-said-and-it.jpeg", "seg": "n7",
        "window": "93.55-104.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE"],
        "narration": (
            "Give, he said, and it will be given back to you — a full "
            "measure, packed down, shaken together to make room for more, "
            "and spilling over the sides into your lap."
        ),
        "must_show": "the return — the earlier GIVER now the receiver: his own robe-fold filling with grain from a neighbour's measure, spilling over; the circle closing on him laughing.",
        "must_not_show": "no halo; the same man who gave in the earlier beats RECEIVING now — continuity of face and robe.",
        "scene": (
            "The circle comes back around to the man who started "
            "it: the householder who handed bread at his door "
            "now stands with his OWN robe gathered into a lap-"
            "fold while a neighbour's wooden measure tips grain "
            "into it — packed down with a palm, shaken to make "
            "room, topped again until it spills bright over the "
            "sides — the giver receiving by the same extravagant "
            "ritual he gave by, laughing at how exactly the "
            "sentence kept its word. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b19", "out": "s19-that-is-the-quiet-secret.jpeg", "seg": "n7",
        "window": "104.92-107.28", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": "That is the quiet secret of it.",
        "must_show": "the secret's keeper — close on Jesus with the slight knowing warmth of a man sharing the mechanism; gentle, almost confidential.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the warmth CONFIDENTIAL — a secret shared, not proclaimed.",
        "scene": (
            "The mechanism gets confided rather than announced: "
            "close on Jesus with the slight warmth of a man "
            "leaning into a secret worth keeping and worth "
            "telling — the deep eyes carrying the quiet amusement "
            "of somebody who designed the machine and has watched "
            "it run: give, and it comes back; pour, and it "
            "refills — the whole economy of heaven folded into a "
            "confidence passed along a hillside at the volume of "
            "a friend. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r123-b20", "out": "s20-a-life-poured-out-in.jpeg", "seg": "n7",
        "window": "107.28-110.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE"],
        "narration": "A life poured out in kindness does not run dry.",
        "must_show": "the unfailing pitcher — at a shared table, a clay pitcher pouring water into cup after held-out cup, still running; abundance in the ordinary.",
        "must_not_show": "no halo; nothing miraculous DEPICTED — a full pitcher generously used, the doctrine in the pouring.",
        "scene": (
            "The secret, demonstrated at an ordinary table: a "
            "clay pitcher travels down the row of held-out cups, "
            "pouring and pouring — water bright in the doorway "
            "light, cup after cup filled and no bottom of the "
            "jug in evidence — the hand that tips it easy and "
            "unhurried, unworried about running out in the way "
            "of hands that have learned the household secret: "
            "poured-out is somehow always the fullest state the "
            "pitcher knows. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r123-b21", "out": "s21-it-comes-back-around-table.jpeg", "seg": "n7",
        "window": "110.85-117.14", "wide": True, "jesus": False, "ref": False,
        "locks": ["VILLAGE"],
        "narration": (
            "It comes back around — table to table, neighbor to neighbor — "
            "until a whole village is carrying one another."
        ),
        "must_show": "the village carrying itself — the lamplit lane at evening: covered dishes carried between doors, neighbours at each other's tables through open doorways, the chain of kindness visible down the street. INTENTIONAL EVENING.",
        "must_not_show": "no halo; the evening DELIBERATE — warm doorways against dusk; every carried dish travelling TOWARD a neighbour's door.",
        "scene": (
            "The rule at full circulation looks like a village at "
            "supper, the camera low down the lane taking the "
            "doorways from the side: warm lamplight standing in "
            "every open door against the blue evening, a woman "
            "crossing the lane with a covered dish for the house "
            "opposite, a boy carrying bread the other way, "
            "neighbours visible at each other's tables through "
            "the doorways — kindness moving table to table down "
            "the whole street like water finding its level — a "
            "village quietly carrying itself. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b22", "out": "s22-it-is-the-shortest-way.jpeg", "seg": "n8",
        "window": "120.06-123.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE"],
        "narration": "It is the shortest way to everything the law was ever trying to teach.",
        "must_show": "the shortest way embodied — a small child carrying bread up the lane to a neighbour's door, passing beneath the synagogue's doorway of heavy scrolls; the law lived at child height.",
        "must_not_show": "no halo; the child SAFE and purposeful; the scrolls visible through the synagogue door, unconsulted.",
        "scene": (
            "The shortest way to the whole law is child-sized: up "
            "the morning lane a small girl carries a round loaf "
            "with both arms, purposeful as a courier, bound for "
            "the widow's door at the top — and her path takes her "
            "right past the open synagogue doorway where the "
            "law's heavy scrolls stand shelved in their niche, "
            "every commandment she is currently keeping rolled up "
            "inside them — the library and the shortcut, side by "
            "side, and the shortcut is winning at a walk. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r123-b23", "out": "s23-treat-others-the-way-you.jpeg", "seg": "n8",
        "window": "123.81-129.56", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Treat others the way you long to be treated, and you will have "
            "kept nearly all of it at once."
        ),
        "must_show": "the close — the golden hillside, the crowd beginning to rise and turn toward their villages carrying the sentence; Jesus seated watching them go.",
        "must_not_show": "no halo, glare or rim-light on Jesus; DIRECTION LAW — the rising listeners turn AWAY downhill toward the villages.",
        "scene": (
            "The sentence leaves the hill inside its hearers, the "
            "camera looking down the slope from behind Jesus's "
            "shoulder: in the golden last light the crowd begins "
            "to rise from the grass and turn away downhill — "
            "fishermen toward the shore, families toward the "
            "lanes, the child skipping ahead of her mother — "
            "every back carrying one sentence home to every "
            "table below, the shortest law ever given walking "
            "out to be kept — while the teacher stays seated on "
            "the crest, watching the whole of it go. Every "
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
    # ROAD: build-38 b39 auto-match REJECTED (a road seen THROUGH a doorway
    # — the doorway dominates; not a road plate) — promote-first from b11.
    # VILLAGE: build-38 b46 auto-match REJECTED (single doorway corner, no
    # well, no fig trees — too weak for 10 riding beats) — promote-first from b01.
}
# === end PLACE-PLATES ===
