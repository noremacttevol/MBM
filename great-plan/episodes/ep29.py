#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 29: Elijah Came.

April 6, 1830 — the church, back as a fact. April 3, 1836 — Kirtland: the
Lord accepts His house, then Moses, Elias, and Elijah return their keys:
gathering, covenant, and the sealing power that welds families past the
grave. Anchors: D&C 110; Malachi 4:5-6.

Continuity payoffs: Moses wears MOSES-GP's face (ep14); Elijah wears the
ELIJAH face from Carmel (ep15) — glorified. Jesus keeps his locked face in
every appearance; scripture's glory-description rides in the caption.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 329
NUM = 29
SLUG = "elijah-came"
TITLE = "Elijah Came"
META = "D&C 110 · Malachi 4"

SEGMENTS = [
    ("n1", NARRATOR,
     "Keys restore a church. More keys turn it into a kingdom death "
     "cannot break up. This episode is about the visitors who brought "
     "the rest."),
    ("n2", NARRATOR,
     "April sixth, eighteen thirty. In a log farmhouse in Fayette, New "
     "York, the Church of Christ was formally organized on the earth "
     "again — same name, same offices, same authority as Galilee. Six "
     "members on the paperwork. A whole gathering on the calendar."),
    ("n3", NARRATOR,
     "Six years later, the young church finished its first temple, at "
     "Kirtland, Ohio — built at crushing sacrifice by people who mostly "
     "lived in cabins. The women even crushed their china into the "
     "plaster so the walls would catch the light. They wanted a house "
     "fit for visitors."),
    ("n4", NARRATOR,
     "They got them. April third, eighteen thirty-six — Easter week. "
     "After the sacrament, Joseph and Oliver bowed behind the pulpit "
     "veils in solemn prayer... and the veil of the visions opened. "
     "First came the Lord himself:"),
    ("j1", JESUS,
     "For behold, I have accepted this house, and my name shall be "
     "here; and I will manifest myself to my people in mercy in this "
     "house."),
    ("n5", NARRATOR,
     "Their written description reads like Ezekiel and John shaking "
     "hands:"),
    ("s1", SCRIPTURE,
     "His eyes were as a flame of fire; the hair of his head was white "
     "like the pure snow; his countenance shone above the brightness of "
     "the sun; and his voice was as the sound of the rushing of great "
     "waters, even the voice of Jehovah."),
    ("n6", NARRATOR,
     "Then, one after another, the department heads returned with their "
     "portfolios. Moses — the same Moses — committed the keys of the "
     "gathering of Israel: authority to bring the family home from the "
     "ends of the earth."),
    ("n7", NARRATOR,
     "Then Elias, committing the dispensation of the gospel of Abraham "
     "— the covenant of the tent, folded whole into the restored "
     "church."),
    ("n8", NARRATOR,
     "And last, the visitor Malachi had promised in the closing words "
     "of the Old Testament — the last prophecy most Bibles print:"),
    ("s2", SCRIPTURE,
     "Behold, I will send you Elijah the prophet before the coming of "
     "the great and dreadful day of the Lord: and he shall turn the "
     "heart of the fathers to the children, and the heart of the "
     "children to their fathers, lest I come and smite the earth with a "
     "curse."),
    ("n9", NARRATOR,
     "Elijah — the Carmel prophet, the fire-caller — stood in the "
     "Kirtland temple and handed over the sealing power: authority to "
     "bind on earth and have it bound in heaven. Marriages that outlast "
     "death. Families welded past the grave. The dead — reachable."),
    ("n10", NARRATOR,
     "Feel what that last one means. The devil's version of death rips "
     "every family apart forever — every till-death-do-you-part is his "
     "fine print. Elijah's keys tear the fine print up. And the hearts "
     "of the children turning to their fathers? Look around: the whole "
     "world caught family-history fever within a few generations of "
     "that afternoon. The pull is real. It started somewhere."),
    ("n11", NARRATOR,
     "So: the church came back on April sixth. But after April third, "
     "eighteen thirty-six, it was more than a church — a kingdom with "
     "gathering orders, Abraham's covenant, and death-proof glue. The "
     "devil spent seventeen centuries taking things off the earth. "
     "Heaven had just spent six years putting every one of them back."),
]

CARD_SEG = ("card", NARRATOR,
            "Till death do you part was the devil's fine print. Elijah "
            "tore it up.")

CARD_TEXT = ("Families, welded\n"
             "past the grave.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Twenty-Nine — Elijah Came")

SPOKEN = {"Kirtland": "KURT lund", "Fayette": "fay ETT"}

ELIJAH_GLORIFIED = (
    "ELIJAH GLORIFIED LOCK: the same man as Carmel — wiry and weather-"
    "forged, deep tan skin, wild shoulder-length grey-streaked dark hair "
    "and ragged full beard, eyes like struck flint — now glorified: the "
    "camel-hair mantle become a robe of exquisite whiteness, the "
    "fierceness become blazing joy, feet bare in the air where the scene "
    "says so. No wings, no halo, no aura outline.")

LOCKS = {"ELIJAH": ELIJAH_GLORIFIED}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="america-1820")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "April sixth: a log farmhouse main room packed shoulder to "
        "shoulder — plain-dressed believers on benches and standing "
        "along the walls, Joseph at the front table with the thick new "
        "book and a paper before him, spring light through small "
        "panes — a church being organized in a living room, formal as "
        "a founding, warm as a family. Camera from the back corner "
        "past shoulders.",
        "a packed farmhouse room with Joseph at a front table, book "
        "and paper before him, seen past shoulders",
        "readable documents, vestments, faces to camera",
        locks=["JOSEPH-SMITH"])),
    ("p02", ("n2", 0.55), _p(
        "Sustained: every hand in the crowded room RAISED at once — a "
        "forest of work-rough right hands up in the window light, "
        "faces earnest beneath them, the unanimous arm of common "
        "consent — seen from the front corner across the raised "
        "field. No face toward the lens.",
        "a room of simultaneously raised work-rough right hands, "
        "earnest faces beneath",
        "ballots, applause, faces to camera",
        )),
    ("p03", "n3", _p(
        "Built at sacrifice: on the Kirtland scaffolds at golden "
        "evening, men haul dressed stone while below, at a plank "
        "table, women CRUSH their own china teacups and plates with "
        "wooden mallets into a glittering bowl — the fragments "
        "destined for the plaster — one woman pausing over a painted "
        "cup a heartbeat before breaking it. Devotion, measured in "
        "heirlooms.",
        "women mallet-crushing their own china into a glittering "
        "bowl below temple scaffolds, one pausing over a painted "
        "cup",
        "sadness played as misery, faces to camera, modern tools",
        wide=True)),
    ("p04", ("n3", 0.6), _p(
        "The house, ready: the finished Kirtland temple at dawn — "
        "the tall gothic-windowed white house on its rise, its "
        "china-flecked plaster walls catching the first sun in a "
        "fine mineral sparkle, dew on the grass slope, the young "
        "settlement's cabins small and humble beyond. A house "
        "waiting for its visitors.",
        "the finished white temple at dawn, plaster subtly "
        "sparkling, humble cabins beyond",
        "crowds, halo effects, modern buildings",
        wide=True)),
    ("p05", "n4", _p(
        "Behind the veils: inside, at the west pulpits, the white "
        "curtain-veils are lowered around the upper stand — and "
        "through the gauze, the shapes of two men bowed in prayer, "
        "heads down, utterly still — the assembly room's tall "
        "windows flooding spring light across the empty curved "
        "benches. Solemnity you can hear.",
        "two bowed praying shapes behind lowered pulpit veils in a "
        "light-flooded empty assembly room",
        "congregation, faces, the vision yet",
        locks=["JOSEPH-SMITH", "OLIVER-C"])),
    ("p06", "j1", _p(
        "The Lord accepts His house: Jesus stands IN THE AIR above "
        "the pulpit's breastwork — feet plainly off the woodwork, "
        "the cream robe still, his familiar face blazing with a "
        "gladness the frame can barely hold — while below him the "
        "two men have fallen back from their knees in awe, the "
        "veils stirred by no wind of earth. The house, worth every "
        "teacup.",
        "Jesus in the air above the pulpit breastwork, face blazing "
        "glad, two men fallen back in awe below",
        "wings, halo, aura outline, white hair, feet on the "
        "woodwork",
        jesus=True, ref=True, locks=["JOSEPH-SMITH", "OLIVER-C"])),
    ("p07", "s1", _p(
        "The rushing of great waters: Jesus's face close in the "
        "vision's brilliance — the locked features alight with "
        "sovereign joy, eyes carrying that flame-of-fire intensity "
        "the two men wrote down with shaking hands, gaze angled "
        "down toward the unseen witnesses below the frame. Glory, "
        "worn by the same face.",
        "Jesus's close alight face, flame-intense eyes angled down "
        "toward unseen witnesses",
        "his eyes on the lens, halo, white hair, lightning",
        jesus=True, ref=True)),
    ("p08", "n6", _p(
        "Moses returns: the great lawgiver stands glorified in the "
        "temple light — the SAME face from Sinai: long white hair, "
        "massive beard, heavy brows — the striped desert robe "
        "become exquisite white, his staff-hand now extended in "
        "bestowal over the two bowed heads below the frame's edge. "
        "The gathering keys, coming home.",
        "glorified Moses with his exact Sinai face extending a "
        "bestowing hand, robe now white",
        "wings, halo, aura outline, the staff, faces to lens",
        locks=["MOSES-GP"])),
    ("p09", "n7", _p(
        "Elias, and the covenant of the tent: a glorified patriarch "
        "in the temple light with his hands spread wide in the "
        "ancient gesture of covenant-blessing — dignified, "
        "silver-bearded, desert-born — and faint through the "
        "brightness behind him, the suggestion of open tent-cloth "
        "folds in the light's own drapery. Abraham's dispensation, "
        "folding in.",
        "a glorified silver-bearded patriarch with covenant-"
        "blessing hands spread wide in bright drapery-light",
        "wings, halo, camels, literal tents, faces to lens",
        )),
    ("p10", "n8", _p(
        "The promised one: ELIJAH stands glorified in the temple "
        "light — the SAME struck-flint eyes and wild grey-streaked "
        "hair from Carmel, the ragged fierceness transfigured to "
        "blazing joy, the camel-hair mantle become whitest cloth — "
        "the last Old Testament promise, standing in an Ohio "
        "temple with his hands already lifting. Malachi's "
        "postscript, delivered.",
        "glorified Elijah with his exact Carmel face and struck-"
        "flint eyes, fierceness become joy, hands lifting",
        "wings, halo, aura outline, fire, faces to lens",
        locks=["ELIJAH"])),
    ("p11", "n9", _p(
        "The sealing power, pictured: over a simple altar, FOUR "
        "generations of hands rest stacked — a child's small hand, "
        "a father's, a grandmother's spotted knuckles, a great-"
        "grandfather's paper-skinned fingers beneath — one warm "
        "column of family flesh in window light. Bound on earth; "
        "the frame implies the rest.",
        "four generations of hands stacked in one column over a "
        "simple altar in window light",
        "rings prominent, faces, documents",
        )),
    ("p12", "n10", _p(
        "The fine print, torn up: an elderly couple's clasped "
        "weathered hands close-up — her thin ring gone loose with "
        "the years, his thumb moving once across her knuckles — "
        "evening lamplight warm on sixty years of hold. A grip "
        "with no expiration clause left in it.",
        "an elderly couple's clasped weathered hands, loose thin "
        "ring, thumb mid-caress, lamplight",
        "faces, hospital context, tears",
        era="modern")),
    ("p13", ("n10", 0.5), _p(
        "The fever: a present-day kitchen table drifted deep in "
        "the past — old photographs fanned out, a magnifying "
        "glass over one faded face, handwritten letters in "
        "unreadable ink, a shoebox of more — and two hands "
        "sorting them with collector's care under the lamp. The "
        "pull Elijah started, at one more table.",
        "old photos, unreadable letters and a magnifier being "
        "sorted by two careful hands under a lamp",
        "readable writing, screens, faces in frame sharp",
        era="modern")),
    ("p14", ("n10", 0.8), _p(
        "Hearts turned: a grandfather's finger rests on one face "
        "in an old family portrait while a small girl beside him "
        "leans in, her own finger rising to the same face, her "
        "mouth open mid-question — two generations meeting a "
        "third on paper, warm evening light. The portrait's "
        "faces stay soft and unreadable.",
        "grandfather's and granddaughter's fingers meeting on one "
        "soft-focus portrait face, her mouth mid-question",
        "readable faces in the photo, screens, sadness",
        era="modern")),
    ("p15", "n11", _p(
        "The kingdom's houses: a white temple at dusk in the "
        "present day — tall lit spire against a violet sky, warm "
        "doors open at the top of the steps, and families in "
        "Sunday best walking up toward the light from behind, a "
        "father carrying a sleepy child. Elijah's keys, at "
        "working hours.",
        "a lit white temple spire at dusk with families from "
        "behind climbing toward open warm doors",
        "signage readable, cars, faces to camera",
        era="modern", wide=True)),
    ("p16", ("n11", 0.6), _p(
        "Everything back on the table: on plain wood in morning "
        "light — the thick book, the iron lock with its key "
        "seated and turned, and the spliced rope coiled beside "
        "them: testimony, authority, and the mended line, one "
        "still life. The devil's seventeen centuries, undone in "
        "six years. No people.",
        "the book, the keyed lock and the spliced rope together "
        "in one morning still life",
        "readable title, hands, clutter",
        )),
    ("p17", ("n11", 0.85), _p(
        "The house that got its visitors: Kirtland at full "
        "sunrise — the white walls sparkling faint with their "
        "china, the gothic windows burning gold with morning, "
        "the spring sky clean above the spire. A building that "
        "kept its appointment. No people.",
        "the Kirtland temple at full sunrise, walls faintly "
        "sparkling, windows gold",
        "crowds, halo effects, drawn rays",
        wide=True)),
]
