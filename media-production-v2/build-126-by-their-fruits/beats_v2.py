#!/usr/bin/env python3
"""V2 beat map — row 126, build-126-by-their-fruits (Matthew 7:15-20).

COVERAGE: 17 pictures over 96.5 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 7 KJV):
  7:15  "Beware of FALSE PROPHETS, which come to you in SHEEP'S
        CLOTHING, but inwardly they are RAVENING WOLVES."
  7:16  "Ye shall KNOW THEM BY THEIR FRUITS. Do men gather GRAPES of
        THORNS, or FIGS of THISTLES?"
  7:17  "every good tree bringeth forth good fruit; but a corrupt
        tree bringeth forth evil fruit."
  7:18  "A good tree CANNOT bring forth evil fruit, neither can a
        corrupt tree bring forth good fruit." — cannot, not will not.
  7:19  "Every tree that bringeth not forth good fruit is HEWN DOWN,
        and CAST INTO THE FIRE." — ordinary orchard-keeping.
  7:20  "Wherefore by their fruits ye shall know them."
  Setting: the Sermon on the Mount hillside — same as rows 121-125.

RENDERING LAWS:
  - THE WOLF FRAMES (b02/b04) are UNEASE, never violence: the
    fleece-draped wolf stands at the fold's edge among unharmed
    sheep; the false-shepherd figure's stance is subtly wrong and
    the sheep edge away. NO attack, NO blood, NO bared-fang lunge,
    ever. The wrongness must read at a glance without any gore.
  - THE FIRE (b14) is ORCHARD WORK, not judgment imagery: a
    farmer's ordinary branch-fire smoking in the orchard while the
    barren trunk is felled — agricultural, daylight, matter-of-fact.
    No hellfire framing, no figures near flames.
  - The two trees carry the doctrine: ONE laden good fig tree and
    ONE blighted barren tree, the same two trees in every orchard
    frame — prop-board them like characters.
  - Action-logic (Cameron's law): the thorn-reach (b06/b08) shows an
    empty scratched hand withdrawn — the failure of the harvest
    readable instantly; the axe (b14) swings at the BARREN tree
    only.
  - HILLSIDE and CROWD locks are BYTE-IDENTICAL to builds 121-125.

TIME OF DAY ARC (intentional): the hillside in the sermon's warm
late-afternoon gold; the fold frames at DUSK by design (the hour
wolves test a flock); the orchard frames in bright working day; the
market test-frame in day; the close in golden last light.

CHANGING CONDITION (kept OUT of the locks): the barren tree —
standing, then hewn and down; the baskets — empty at the thorns,
full under the fig.
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
    "FOLD": (
        "FOLD LOCK: the sheepfold — a dry-stone fold on a dusky "
        "hillside, a wooden gate, a scatter of cream-wool sheep "
        "grazing inside and near the walls, low violet dusk light. "
        "The same fold and walls throughout."
    ),
    "ORCHARD": (
        "ORCHARD LOCK: the orchard — a terraced hillside orchard "
        "holding TWO particular trees a few paces apart: a broad "
        "LADEN FIG TREE, deep green and heavy with ripe figs, and a "
        "gaunt BLIGHTED TREE with sparse grey leaves and shriveled "
        "dark fruit; thorn bushes and thistles along the terrace "
        "edge; bright working day. The same two trees throughout."
    ),
    "FARMER": (
        "FARMER LOCK: the orchard farmer is the same man in every "
        "shot — sturdy, about fifty-five, sun-browned with a short "
        "white-flecked beard, in a DARK OLIVE work tunic with a "
        "rope belt (never cream, never white); practical, unhurried, "
        "good-humoured."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r126-b01", "out": "s01-jesus-taught-how-to-tell.jpeg", "seg": "n0",
        "window": "0.28-4.51", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Jesus taught how to tell what is true — look at what grows from it.",
        "must_show": "the lesson opened — Jesus seated teaching on the hillside, one arm gesturing out toward the terraced orchards visible down the slope; the test located in the growing world.",
        "must_not_show": "no halo, glare or rim-light on Jesus; DIRECTION — faces following his gesture toward the orchards.",
        "scene": (
            "The test he is about to give grows on the next "
            "terrace, the camera looking past the seated crowd's "
            "backs up the gold slope: Jesus seated above the "
            "blue lake with one arm swept out toward the "
            "terraced orchards stepping down toward the shore — "
            "fig and olive and vine in their working rows — and "
            "the crowd's faces turning with the gesture toward "
            "trees they have picked all their lives, about to "
            "learn that they have also been looking at the "
            "world's most reliable instrument for telling true "
            "from false. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r126-b02", "out": "s02-beware-of-false-prophets-which.jpeg", "seg": "j1a",
        "window": "5.04-12.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD"],
        "narration": (
            "Beware of false prophets, which come to you in sheep's "
            "clothing, but inwardly they are ravening wolves."
        ),
        "must_show": "SCRIPTURE-EXACT: the image itself — at the dusk fold's edge, a wolf draped in a sheep's fleece standing among the unharmed grazing sheep; the wrongness readable, no attack.",
        "must_not_show": "ABSOLUTE: no attack, no blood, no bared-fang lunge — the sheep unharmed; the danger is the DISGUISE, told by stance and eyes.",
        "scene": (
            "The verse's picture stands at the fold gate in the "
            "violet dusk: among the cream-wool backs of the "
            "grazing flock, one shape wears its fleece wrong — "
            "draped, not grown — and under the borrowed wool the "
            "long grey frame of a wolf holds perfectly still, "
            "amber eyes level above a sheep's soft coat — no "
            "lunge, no snarl, nothing yet but the standing "
            "wrongness of it — the oldest disguise in the world, "
            "photographed calmly at the hour it prefers. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r126-b03", "out": "s03-watch-out-he-said.jpeg", "seg": "j1b",
        "window": "13.55-14.68", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": "Watch out, he said.",
        "must_show": "the warning — close on Jesus, alert and protective, the shepherd's watchfulness in his face; guarding, not frightening.",
        "must_not_show": "no halo, glare or rim-light on Jesus; PROTECTIVE alertness — a shepherd's face, not an alarmist's.",
        "scene": (
            "The warning is given the way a shepherd gives it: "
            "close on Jesus in the warm light with his face "
            "gone watchful — not alarmed, GUARDING — the deep "
            "eyes steady on his people with the particular "
            "alertness of a man who knows exactly what "
            "sometimes walks in wearing wool, and loves the "
            "flock too much to let the evening pass without "
            "saying so — two words, spoken low, worth the whole "
            "fold. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r126-b04", "out": "s04-some-of-them-will-come.jpeg", "seg": "j1b",
        "window": "14.68-22.93", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD"],
        "narration": (
            "Some of them will come to you looking like part of the flock — "
            "gentle, harmless, one of your own. Inside, they are wolves."
        ),
        "must_show": "the human version — at the fold, a stranger in shepherd's clothes whose stance is subtly wrong, the nearest sheep edging away from him; unease without any violence.",
        "must_not_show": "ABSOLUTE: no attack, no menace-pose — the wrongness SUBTLE: the sheep's edging, the too-still stance; he looks almost right.",
        "scene": (
            "The human edition is harder to spot: at the fold "
            "gate stands a man dressed exactly like a shepherd "
            "— staff, mantle, easy smile — and almost "
            "everything about him is right except what the "
            "sheep already know: the nearest ewes have drifted "
            "quietly to the far wall, lambs tucked behind them, "
            "leaving a moat of empty dusk around a stranger "
            "whose stillness watches the flock the way no "
            "shepherd's ever does — gentle, harmless-looking, "
            "and read correctly only by the innocent. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r126-b05", "out": "s05-a-tree-shows-what-it.jpeg", "seg": "n1",
        "window": "23.49-28.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD", "FARMER"],
        "narration": (
            "A tree shows what it is by what it bears. You don't guess at a "
            "tree by its bark."
        ),
        "must_show": "the better instrument — the farmer with one hand on a tree's bark but his eyes UP in the branches where the fruit is; the test relocated from surface to yield.",
        "must_not_show": "no halo; his gaze UNMISTAKABLY on the branches, not the trunk — the point in one look.",
        "scene": (
            "The farmer demonstrates where the truth of a tree "
            "keeps its office: one broad hand resting flat on "
            "the trunk's bark — which tells him nothing and he "
            "knows it — while his eyes are all the way UP in "
            "the branches, reading the yield: what hangs there, "
            "what ripens there, what the tree has actually "
            "done with its year — bark being the tree's "
            "clothing and fruit being its testimony, and no "
            "orchard man alive confusing which one is admissible. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r126-b06", "out": "s06-ye-shall-know-them-by.jpeg", "seg": "j2",
        "window": "29.09-34.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD", "FARMER"],
        "narration": (
            "Ye shall know them by their fruits. Do men gather grapes of "
            "thorns, or figs of thistles?"
        ),
        "must_show": "SCRIPTURE-EXACT: the absurd harvest attempted — the farmer's hand reaching into a thorn bush at the terrace edge, basket empty at his feet, thistles bristling beside; the impossibility live.",
        "must_not_show": "no halo; the reach REAL and the basket EMPTY — the question answered by the picture.",
        "scene": (
            "The rhetorical question is staged at the terrace "
            "edge: the farmer's arm reaches carefully into a "
            "thorn bush the way you would reach for grapes — "
            "and finds what thorn bushes have always kept in "
            "stock — while at his feet the harvest basket "
            "stands perfectly empty and a stand of purple-"
            "headed thistles bristles beside it, offering no "
            "figs from any angle — the whole botanical economy "
            "declining, as it has since the beginning, to "
            "yield one thing from the nature of another. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r126-b07", "out": "s07-even-so-every-good-tree.jpeg", "seg": "j2",
        "window": "34.81-42.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD"],
        "narration": (
            "Even so every good tree bringeth forth good fruit; but a "
            "corrupt tree bringeth forth evil fruit."
        ),
        "must_show": "SCRIPTURE-EXACT: the two trees — the laden fig tree deep green and heavy beside the gaunt blighted tree with its shriveled dark fruit; both natures in one frame.",
        "must_not_show": "no halo; the contrast HONEST — the blighted tree pitiable, not monstrous; same soil, same sun, different natures.",
        "scene": (
            "The doctrine grows a few paces apart in the same "
            "soil: on the left the laden fig tree, deep green "
            "and bowed with ripe fruit, bees busy at the "
            "windfalls — on the right the blighted tree, gaunt "
            "and grey-leaved, its sparse fruit hanging dark and "
            "shriveled on the twig — the same terrace, the same "
            "sun, the same rain on both root systems, and each "
            "tree publishing its inward nature in the only "
            "language trees have ever spoken: what they bear. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r126-b08", "out": "s08-nobody-picks-grapes-off-a.jpeg", "seg": "n2",
        "window": "43.91-45.86", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD", "FARMER"],
        "narration": "Nobody picks grapes off a thorn bush.",
        "must_show": "the empty hand — close on the farmer's hand withdrawn from the thorns, lightly scratched and holding nothing; the lesson at skin level.",
        "must_not_show": "no halo; scratches LIGHT (no gore) — the emptiness of the hand the point.",
        "scene": (
            "The experiment returns its result at skin level: "
            "close on the farmer's hand withdrawn from the "
            "thorn bush — lightly scratched across the "
            "knuckles, fingers open, holding exactly nothing — "
            "the thorn's whole harvest displayed on an empty "
            "palm — while behind the hand the bush keeps its "
            "spikes and its nature, having given the only "
            "thing it had, which was the answer. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r126-b09", "out": "s09-nobody-gathers-figs-off-a.jpeg", "seg": "n2",
        "window": "45.86-53.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD", "FARMER"],
        "narration": (
            "Nobody gathers figs off a thistle. You already know how this "
            "works — a good tree gives good fruit, and a bad one gives bad "
            "fruit."
        ),
        "must_show": "the working knowledge — the farmer under the laden fig tree now, basket FULL of ripe figs, one hand pulling another from the branch; the ordinary reliable law.",
        "must_not_show": "no halo; the fullness of THIS basket against b06/b08's emptiness — the same basket.",
        "scene": (
            "Where the knowledge everyone already has does its "
            "shopping: the farmer stands under the laden fig "
            "tree with the same harvest basket now heaped full "
            "— ripe figs stacked purple-brown to the rim — one "
            "hand easing yet another from the low branch with "
            "the unthinking confidence of a man consulting a "
            "law that has never once failed him: good tree, "
            "good fruit, every season, every time, no surprises "
            "in either direction since the world began. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r126-b10", "out": "s10-cannot.jpeg", "seg": "n2b",
        "window": "62.28-63.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD"],
        "narration": "Cannot.",
        "must_show": "the single word pictured — extreme close on the blighted branch and its shriveled dark fruit; the nature's hard limit in one twig.",
        "must_not_show": "no halo; nothing added — one branch, one truth.",
        "scene": (
            "One word gets one twig: extreme close on the "
            "blighted tree's branch — grey bark split and dry, "
            "two shriveled dark fruits hanging where sweetness "
            "was supposed to be — no bee visiting, no bird "
            "interested — a branch doing everything a branch "
            "does, budding and bearing and ripening, and "
            "producing at the end of all that honest effort "
            "exactly what its nature had in stock: this. The "
            "limit is not stubbornness; it is CANNOT. No people "
            "in this frame."
        ),
    },
    {
        "id": "v2-r126-b11", "out": "s11-a-good-tree-cannot-bring.jpeg", "seg": "jv18",
        "window": "54.49-60.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD"],
        "narration": (
            "A good tree cannot bring forth evil fruit, neither can a "
            "corrupt tree bring forth good fruit."
        ),
        "must_show": "SCRIPTURE-EXACT: the law of natures — both trees again, each bearing strictly its own: bright figs on the green boughs, dark shriveled fruit on the grey; no exceptions visible anywhere.",
        "must_not_show": "no halo; NOT ONE good fig on the blighted tree, not one bad one on the laden — the absoluteness is the verse.",
        "scene": (
            "The law admits no exceptions and the frame shows "
            "none: the two trees stand in their few paces of "
            "shared terrace, and every single fruit is filed "
            "under its own nature — the green boughs carrying "
            "nothing but bright ripe figs to their outermost "
            "twig, the grey branches carrying nothing but "
            "shriveled dark fruit to theirs — not one straggler "
            "on either side, not one exception in the whole "
            "canopy, the word CANNOT spelled out in botany "
            "across both trees at once. No people in this "
            "frame."
        ),
    },
    {
        "id": "v2-r126-b12", "out": "s12-not-will-not-cannot-the.jpeg", "seg": "n2b",
        "window": "63.16-68.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD", "FARMER"],
        "narration": "Not will not — cannot. The good and the rotten cannot switch places.",
        "must_show": "the two fruits in two hands — the farmer holding a bright ripe fig in one palm and a shriveled dark one in the other, the unbridgeable difference at arm's width.",
        "must_not_show": "no halo; both fruits CLEAR and true to their trees; his face matter-of-fact.",
        "scene": (
            "The whole doctrine fits in two open palms: the "
            "farmer holds a bright ripe fig in one hand and "
            "the blighted tree's shriveled dark fruit in the "
            "other, arms a little apart, weighing nothing — "
            "there is nothing to weigh — just the flat "
            "unbridgeable difference between two natures laid "
            "out at arm's width, no road running from one palm "
            "to the other, no season that turns the dark one "
            "sweet or the sweet one dark — not will not: "
            "cannot. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r126-b13", "out": "s13-what-is-inside-comes-out.jpeg", "seg": "n2b",
        "window": "68.47-72.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD"],
        "narration": "What is inside comes out in the open, given long enough.",
        "must_show": "the inside surfacing — the blighted trunk where the bark has split, the grey inner rot visible through the seam; time as the revealer.",
        "must_not_show": "no halo; decay HONEST, not grotesque — a split seam of grey heartwood, no more.",
        "scene": (
            "Time runs the only audit that never misses: on the "
            "blighted trunk the bark has split along a hand's-"
            "length seam, and through the gap the inside has "
            "surfaced — grey punky heartwood where sound grain "
            "should be, the tree's private nature gone public "
            "at last through its own skin — nothing dramatic, "
            "no storm required, just enough seasons for what "
            "was always inside to finish its slow trip to the "
            "open, the way it always, always does. No people "
            "in this frame."
        ),
    },
    {
        "id": "v2-r126-b14", "out": "s14-every-tree-that-bringeth-not.jpeg", "seg": "j3",
        "window": "72.75-78.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD", "FARMER"],
        "narration": (
            "Every tree that bringeth not forth good fruit is hewn down, and "
            "cast into the fire."
        ),
        "must_show": "SCRIPTURE-EXACT as ORCHARD WORK — the farmer's axe mid-swing at the barren trunk, and an ordinary branch-fire smoking farther down the terrace; agriculture, not judgment imagery.",
        "must_not_show": "ABSOLUTE: no hellfire framing — daylight, a small workmanlike burn pile at distance; the axe aimed at the BARREN tree only.",
        "scene": (
            "The orchard keeps itself the way orchards always "
            "have: the farmer's axe swings mid-arc into the "
            "barren trunk — chips bright at the cut, the gaunt "
            "grey canopy shivering overhead — while farther "
            "down the terrace an ordinary branch-fire smokes "
            "its thin workmanlike column into the afternoon, "
            "yesterday's prunings becoming ash on schedule — "
            "no drama and no ceremony: ground is expensive, "
            "seasons are short, and a tree that feeds nobody "
            "is firewood by every orchard's oldest arithmetic. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r126-b15", "out": "s15-wherefore-by-their-fruits-ye.jpeg", "seg": "j3 + n3",
        "window": "78.44-86.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["ORCHARD", "FARMER"],
        "narration": (
            "Wherefore by their fruits ye shall know them. A tree that never "
            "gives anything worth eating gets cut down."
        ),
        "must_show": "the aftermath — the fresh stump where the barren tree stood, the felled wood stacked neat, the laden fig tree still flourishing beside the cleared space.",
        "must_not_show": "no halo; the scene TIDY and unmournful — orchard order restored; the good tree's abundance unmissable beside the stump.",
        "scene": (
            "The terrace reads plainly the morning after: a "
            "fresh pale stump where the blighted tree stood, "
            "its wood stacked neat and useful against the "
            "terrace wall — and beside the cleared ground, "
            "unbothered and magnificent, the laden fig tree "
            "goes on with its year, boughs heavy, bees busy — "
            "the orchard's verdict rendered and filed with no "
            "malice in it anywhere: known by its fruit, "
            "found empty, and returned to usefulness the only "
            "way barren wood can be. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r126-b16", "out": "s16-so-watch-the-fruit-not.jpeg", "seg": "n3",
        "window": "86.39-92.75", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "So watch the fruit. Not the clothes, not the confidence, not "
            "the words — the fruit."
        ),
        "must_show": "the test applied to people — a market stall: a finely-robed confident seller, and the buyer's eyes down on the SCALE and the short measure, not the robe; where honest attention goes.",
        "must_not_show": "no halo; the seller not a cartoon — fine and confident; the buyer's gaze on the MEASURE the whole picture.",
        "scene": (
            "The orchard's method transfers to the market "
            "without modification: at the awning stall a "
            "finely-robed seller talks with easy confidence, "
            "rings on the gesturing hand — and the buyer "
            "before him is not watching the robe or the rings "
            "or the fluent mouth at all: her eyes are down on "
            "the SCALE, on the measure being scraped a "
            "half-knuckle short, on the actual fruit of the "
            "man — clothes and confidence being bark, and the "
            "measure being the harvest. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r126-b17", "out": "s17-that-is-the-whole-test.jpeg", "seg": "n3",
        "window": "92.75-96.24", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "That is the whole test, and anybody can run it.",
        "must_show": "the close — Jesus on the golden hillside holding up one ripe fig toward the crowd, the whole examination in one piece of fruit; warmth and finality.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the fig ORDINARY and real — the test handed over, complete.",
        "scene": (
            "The entire examination fits between a thumb and "
            "two fingers: Jesus holds up a single ripe fig in "
            "the golden last light, turning it once so the "
            "whole hillside can see the completeness of the "
            "test — no scrolls required, no experts, no "
            "credentials checked at any door — one piece of "
            "fruit, readable by fishermen, mothers, farmers "
            "and children alike — that is the whole test, his "
            "easy face says, and every person on this grass "
            "is already qualified to run it. Every figure has "
            "two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    # FOLD: build-21 b09 auto-match REJECTED — the fold itself matches, but
    # the frame contains build-21's SHEPHERD standing in the flock; b02 needs
    # no man (wolf) and b04 a different stranger. Promote-first from b02.
    # ORCHARD --take from build-32 also REJECTED (blue-grey dusk estate frame,
    # not the bright-day two-tree orchard) — promote-first from b07.
}
# === end PLACE-PLATES ===
