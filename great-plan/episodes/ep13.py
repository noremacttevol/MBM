#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 13: One Family for All Families.

The tale of two unities: Babel's tower for its own name, and the covenant
made in one desert tent to bless every family on earth — sealed on a
mountain that prefigured another Father and another beloved Son.
Anchors: Genesis 11:4; 12:2-3; 22:18; Abraham 1:2; Galatians 3:29.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 313
NUM = 13
SLUG = "one-family"
TITLE = "One Family for All Families"
META = "Genesis 11-22 · Abraham 1-2"

SEGMENTS = [
    ("n1", NARRATOR,
     "After the flood, mankind tried something God had to stop. And then "
     "God started something mankind is still living inside. This is the "
     "tale of two unities."),
    ("n2", NARRATOR,
     "On the plain of Shinar, the survivors' descendants gathered with "
     "one language and one plan:"),
    ("s1", SCRIPTURE,
     "Go to, let us build us a city and a tower, whose top may reach "
     "unto heaven; and let us make us a name, lest we be scattered "
     "abroad upon the face of the whole earth."),
    ("n3", NARRATOR,
     "Listen to the motive. Let us make US a name. Reach heaven by our "
     "own stack of bricks. It was unity, all right — unity aimed at "
     "glory without God. One language, one project, one tower of "
     "pride."),
    ("n4", NARRATOR,
     "God scattered it. Not because heaven fears tall buildings — "
     "because He had already seen where forced unity goes. One heart "
     "pointed wrong is Babel. One heart pointed right is Zion. The "
     "direction is everything."),
    ("n5", NARRATOR,
     "So God began His own unity project, and its blueprint was the "
     "exact opposite of a tower. One man. One family. One tent in the "
     "desert."),
    ("n6", NARRATOR,
     "Abram of Ur — Abraham — a man who wanted righteousness more than "
     "his father's idols. His own words about what he was looking for:"),
    ("s2", SCRIPTURE,
     "I sought for the blessings of the fathers, and the right "
     "whereunto I should be ordained to administer the same."),
    ("g1", FATHER,
     "And I will make of thee a great nation, and I will bless thee, "
     "and make thy name great; and thou shalt be a blessing: and in "
     "thee shall all families of the earth be blessed."),
    ("n7", NARRATOR,
     "Catch the reversal. Babel said: we will make us a name. God said: "
     "I will make thy name great — so that all families of the earth "
     "are blessed. That is not favoritism. It is a delivery system — "
     "one family, carrying priesthood and gospel to everybody."),
    ("n8", NARRATOR,
     "And to seal it, God asked Abraham for the hardest walk of his "
     "life — up a mountain, with his miracle son. At the last instant, "
     "heaven stayed his hand, and a ram in the thicket took Isaac's "
     "place. The whole scene was a picture, four thousand years early: "
     "another Father. Another beloved Son. Another hill — where no "
     "voice would stay the hand."),
    ("g2", FATHER,
     "And in thy seed shall all the nations of the earth be blessed; "
     "because thou hast obeyed my voice."),
    ("n9", NARRATOR,
     "From Abraham's tent came Israel. From Israel, the prophets. From "
     "the prophets, the records. And from that same family line, in a "
     "stable in Bethlehem — the Seed in whom every family on earth is "
     "blessed."),
    ("n10", NARRATOR,
     "And here is where you come in. The covenant never expired. "
     "Paul said it straight:"),
    ("s3", SCRIPTURE,
     "And if ye be Christ's, then are ye Abraham's seed, and heirs "
     "according to the promise."),
    ("n11", NARRATOR,
     "Two unities. One built a tower to make its own name great — and "
     "shattered. One followed a promise made to bless every name on "
     "earth — and it is still gathering. You are not asked to build "
     "the tower. You are invited into the tent."),
]

CARD_SEG = ("card", NARRATOR,
            "Babel built for its own name. Abraham was blessed for "
            "yours. You are invited into the tent.")

CARD_TEXT = ("You are invited\n"
             "into the tent.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Thirteen — One Family for All Families")

SPOKEN = {}

ABRAHAM = (
    "ABRAHAM LOCK: the same man as the attached reference in every "
    "picture — the great patriarch in strong old age: deep bronze "
    "desert-weathered skin, long silver-grey hair under a simple head "
    "cloth, a full silver-grey beard, tall and unbowed, wearing layered "
    "desert robes of undyed wool and faded indigo with a woven sash. "
    "Regal without a crown. No halo, no glow.")

LOCKS = {"ABRAHAM-GP": ABRAHAM}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="ancient")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The tower rising: on a dusty river plain, a colossal stepped "
        "ziggurat under construction climbs into the haze — ramps "
        "crawling with distant workers, brick-smoke drifting, the "
        "structure already dwarfing the city knotted around its base. "
        "Seen from far across the plain in hard afternoon light.",
        "a colossal half-built stepped tower crawling with distant "
        "workers over a knotted city",
        "readable banners, cranes, faces, storm sky yet",
        wide=True)),
    ("p02", "s1", _p(
        "One language, one obsession: a brick-line of workers passing "
        "moulded mud bricks hand to hand up a ramp — dozens of backs "
        "and shoulders in rhythm, dust in the low sun, an overseer's "
        "raised arm setting the pace at the top — the camera in the "
        "line shooting up the ramp past the workers' backs.",
        "a hand-to-hand brick line up a ramp seen past workers' "
        "backs, overseer's arm at the top",
        "whips, faces to camera, cruelty shown",
        )),
    ("p03", "n3", _p(
        "Make us a name: the tower's unfinished summit wrapped in "
        "cloud-haze — and being hauled up its final ramp, a great "
        "GILDED CREST, a sun-disc of beaten gold meant to crown the "
        "top, ropes taut, tiny figures straining — man's glory "
        "climbing toward heaven's address. Low camera looking up the "
        "ramps.",
        "a gilded sun-crest being hauled up the tower's summit ramp "
        "into cloud-haze",
        "lightning, gods' statues, readable symbols, faces",
        )),
    ("p04", "n4", _p(
        "The scattering: the tower stands ABANDONED at half-height "
        "under a clearing sky, ramps empty, scaffold poles bare — and "
        "across the whole plain below, long thin lines of people "
        "stream AWAY from it in every direction like spokes, herds "
        "and carts and dust-trails diverging toward every horizon. "
        "Quiet, total, irreversible.",
        "the abandoned half-built tower with thin lines of people "
        "streaming away in every direction",
        "destruction, fire, lightning, collapse",
        wide=True)),
    ("p05", "n5", _p(
        "The counter-blueprint: one black goat-hair tent alone on an "
        "immense dusk desert, a single warm lamp burning inside its "
        "open flap, the sky above going to deep violet with the "
        "first stars — smaller than anything Babel built, and "
        "already holding more future. No people visible.",
        "one lamplit desert tent alone under a violet first-star "
        "sky",
        "cities, towers, camels yet, figures",
        wide=True)),
    ("p06", "n6", _p(
        "The seeker: Abraham stands at the edge of the firelight "
        "outside Ur's distant shine, his back to the city, face "
        "lifted to the night — the look of a man who has already "
        "chosen against the idols behind him and doesn't yet know "
        "what he has chosen toward. Seen in three-quarter from "
        "beside the fire.",
        "Abraham in three-quarter at night, back to a distant "
        "city-glow, face lifted seeking",
        "idols in frame, his eyes on the lens, halo",
        locks=["ABRAHAM-GP"])),
    ("p07", "s2", _p(
        "Seeking the fathers' blessing: Abraham kneels at a small "
        "rough stone altar at grey dawn, both hands flat on its "
        "top stone, head bowed between his arms — the posture of a "
        "man asking for a RIGHT, not a favour — his staff laid on "
        "the ground beside him, the desert silent around.",
        "Abraham kneeling with both hands flat on a small altar at "
        "grey dawn, head bowed between his arms",
        "fire on the altar, sacrifice, his face to camera",
        locks=["ABRAHAM-GP"])),
    ("p08", "g1", _p(
        "The covenant given: Abraham stands beneath the full "
        "immensity of the desert night sky — the milky way's arch "
        "burning from horizon to horizon — seen from directly "
        "behind, his arms lifted slightly from his sides, palms "
        "forward, head back: a man being SHOWN his seed in the "
        "stars. His tent burns small and warm at the frame's "
        "bottom edge.",
        "Abraham from directly behind under the full milky way "
        "arch, arms slightly lifted, tent-glow small below",
        "his face, meteors, drawn light, text",
        wide=True, locks=["ABRAHAM-GP"])),
    ("p09", "n7", _p(
        "The delivery system moves: Abraham's caravan sets out at "
        "dawn — laden camels in a swaying line, herds flowing "
        "alongside, family and servants walking — all crossing the "
        "frame in profile from left to right through low gold "
        "light and rising dust, the promise on the road.",
        "a dawn caravan of camels, herds and walking family "
        "crossing in profile through gold dust",
        "faces to camera, armed guards prominent, cities",
        wide=True, locks=["ABRAHAM-GP"])),
    ("p10", ("n7", 0.5), _p(
        "Blessing in action: at a foreign village well, Abraham's "
        "servants lift full waterskins and round loaves down from "
        "a kneeling camel into the arms of village women and "
        "children — both peoples mingled at the well-stones, every "
        "face on the exchange, morning light broad on the scene.",
        "servants passing bread and waterskins down to village "
        "women and children at a well, faces on the exchange",
        "coins, bowing, faces to camera",
        )),
    ("p11", "n8", _p(
        "The hardest walk: Abraham and young Isaac climb a bare "
        "mountain shoulder at grey first light, seen from behind "
        "and below — the boy ahead with the bundle of wood roped "
        "across his shoulders, the old man behind carrying the "
        "small fire-pot, both leaning into the slope — nothing "
        "else on the mountain but stone and morning.",
        "old man and boy from behind climbing bare stone at grey "
        "dawn, wood on the boy's shoulders, fire-pot in the "
        "man's hand",
        "an altar, a knife, faces, tears yet",
        wide=True, locks=["ABRAHAM-GP"])),
    ("p12", ("n8", 0.5), _p(
        "The stayed hand: Abraham's face alone, close — anguish "
        "breaking OPEN into shuddering relief, eyes flung up "
        "toward a voice above the frame, mouth halfway between a "
        "sob and a laugh, tears cutting the dust on his cheeks. "
        "No knife, no altar, no boy in frame — just the exact "
        "second mercy lands.",
        "Abraham's close face breaking from anguish into "
        "shuddering relief, eyes up at an unseen voice",
        "knife, altar, Isaac, his eyes on the lens",
        locks=["ABRAHAM-GP"])),
    ("p13", ("n8", 0.78), _p(
        "The substitute: a strong ram caught fast by both horns in "
        "a dense mountain thicket, pulling once against the "
        "tangle, morning sun bright on its wool — provided, "
        "waiting, exactly where it needed to be. Close, from the "
        "side.",
        "a ram caught by the horns in a thicket in morning sun",
        "blood, ropes, people, distress overdone",
        )),
    ("p14", "n9", _p(
        "The Seed arrives: night over the sleeping hills of "
        "Bethlehem — terraced slopes, a few lamplit windows in "
        "the little town, shepherd fires dotted on the dark "
        "pasture — and one star over it all, larger and stiller "
        "than the rest. The covenant, twenty generations on, "
        "keeping its appointment.",
        "sleeping terraced Bethlehem under one large still star, "
        "shepherd fires on the dark pasture",
        "angels visible, drawn rays, the stable shown",
        wide=True, era="first-century")),
    ("p15", "s3", _p(
        "Grafted in: an ancient olive trunk, gnarled and grey — "
        "and bound into a cut in its side with clean wrapping, a "
        "young green branch, its new leaves bright against the "
        "old bark, the graft-union tight and healing. Paul's own "
        "picture of you, in extreme close-up.",
        "a young green branch grafted and bound into an ancient "
        "olive trunk, extreme close",
        "hands, orchards wide, text",
        era="first-century")),
    ("p16", ("s3", 0.6), _p(
        "Heirs, now: in the present day, a young family — father "
        "carrying a sleeping toddler, mother beside him — steps "
        "through a warm-lit front door out of the evening dark, "
        "seen from behind at the walk's end, the doorway's gold "
        "spilling around their silhouettes. Coming in, wanted.",
        "a young modern family from behind entering a warm-lit "
        "front door out of evening dark",
        "faces, house numbers, brand marks",
        era="modern")),
    ("p17", "n11", _p(
        "Two unities, one frame: far across the dusk plain, the "
        "broken tower-stump stands abandoned against the last "
        "grey light — while in the near foreground Abraham's "
        "lamplit tent stands warm with figures gathering toward "
        "its open flap, travellers' silhouettes converging out of "
        "the dark toward the light. The thesis of the episode in "
        "a single look.",
        "the distant broken tower-stump and the near lamplit "
        "tent with travellers converging toward its open flap",
        "faces readable, the tower intact, drawn rays",
        wide=True)),
    ("p18", ("n11", 0.6), _p(
        "Into the tent: at the tent's open flap Abraham holds "
        "the goat-hair curtain wide with one arm and extends "
        "the other palm-up toward a dusty traveller seen from "
        "behind in the near frame — the lamp-gold interior, "
        "spread carpets and waiting bread visible past the "
        "patriarch's welcome. The oldest invitation on earth.",
        "Abraham holding the tent flap wide, palm-up welcome to "
        "a traveller seen from behind, gold interior beyond",
        "Abraham's eyes on the lens, guards, coins",
        locks=["ABRAHAM-GP"])),
    ("p19", ("n11", 0.85), _p(
        "The promise sky: dawn over the open desert — the tent "
        "small and dark against a horizon going gold, and above "
        "it the last stars still burning in the brightening "
        "blue, countless, patient, named. No people; the "
        "covenant itself, at rest.",
        "the small dark tent under a dawn sky still holding its "
        "last countless stars",
        "figures, caravans, text, drawn rays",
        wide=True)),
]
