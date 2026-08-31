#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 5: The Proving Ground.

Creation as a deliberate school: the Son organizes the world under the
Father, the proving is for OUR becoming (a gym, not a quiz), and we say
plainly what God has and has not revealed about the how.
Anchors: Abraham 3:24-26; John 1:3; Abraham 4.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, DEVIL = ("narrator", "jesus", "father",
                                             "scripture", "devil")

EP = 305
NUM = 5
SLUG = "proving-ground"
TITLE = "The Proving Ground"
META = "Abraham 3 · John 1"

SEGMENTS = [
    ("n1", NARRATOR,
     "Between the war and your birth, something enormous had to be built. "
     "A world. This one. And who built it — and what for — changes how it "
     "feels to live in it."),
    ("s1", SCRIPTURE,
     "And there stood one among them that was like unto God, and he said "
     "unto those who were with him: We will go down, for there is space "
     "there, and we will take of these materials, and we will make an "
     "earth whereon these may dwell."),
    ("n2", NARRATOR,
     "One like unto God. That is Jehovah — the premortal Jesus. Under the "
     "Father's direction, the Son led the building of this world. John "
     "says it flat out:"),
    ("s2", SCRIPTURE,
     "All things were made by him; and without him was not any thing made "
     "that was made."),
    ("n3", NARRATOR,
     "And notice the wording Abraham heard. Not conjure. Not wish. We will "
     "take of these materials. Eternal stuff, organized with intent — a "
     "Builder with a blueprint, and a family moving in."),
    ("n4", NARRATOR,
     "And what was the building for? The very next sentence of the "
     "blueprint:"),
    ("g1", FATHER,
     "And we will prove them herewith, to see if they will do all things "
     "whatsoever the Lord their God shall command them."),
    ("n5", NARRATOR,
     "We will prove them. This world is a proving ground. But be careful "
     "with that word — it does not mean what fear tells you it means."),
    ("n6", NARRATOR,
     "God is not grading you to find out if you're good enough. He knew "
     "you before the womb — He already knows His children perfectly. The "
     "proving was never for His information. It is for your becoming."),
    ("n7", NARRATOR,
     "A test can be a trap, or it can be training. A quiz measures what "
     "you were. Training builds what you will be. Mountains. Hunger. "
     "Distance. Gravity. Resistance everywhere you look — because "
     "resistance is how children of God grow."),
    ("g2", FATHER,
     "And they who keep their first estate shall be added upon; and they "
     "who keep their second estate shall have glory added upon their heads "
     "for ever and ever."),
    ("n8", NARRATOR,
     "Added upon. That is the family word for what this planet is for. "
     "You kept your first estate — you are here, and that is the proof. "
     "The second estate runs the same play at heavier weight: keep "
     "choosing Him, and glory gets added. Forever."),
    ("n9", NARRATOR,
     "Now the honest part. How long did creation take? What processes did "
     "He use? How does the science fit in? God has not told us everything "
     "— and we will not pretend He has. What He revealed is who built it, "
     "and why. And that is the part that changes your Monday."),
    ("n10", NARRATOR,
     "Because if this world is an accident, so are you, and nothing means "
     "anything. But if every sunrise is architecture — if the whole planet "
     "is a classroom built by Someone who intends His children to "
     "graduate — then your hardest day here is not chaos. It is "
     "curriculum."),
    ("n11", NARRATOR,
     "The devil calls this earth his kingdom. Do not believe him. He "
     "never built anything. You are standing in your Father's school, on "
     "your Brother's handiwork — and they put you here to grow."),
]

CARD_SEG = ("card", NARRATOR,
            "This world is not an accident. It is a classroom — and you "
            "were meant to graduate.")

CARD_TEXT = ("Every sunrise\n"
             "is architecture.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Five — The Proving Ground")

SPOKEN = {}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="ancient")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The unfinished world from high above: a half-made planet of "
        "dark new ocean and raw stone continents under slow spirals of "
        "white cloud, morning light flooding across its curve out of "
        "black space — construction at planetary scale, beautiful and "
        "in progress. No figures.",
        "a half-built world of new ocean and raw stone under morning "
        "light from space",
        "any figure, modern continent shapes, text, satellites",
        era="heaven")),
    ("p02", "s1", _p(
        "We will go down: at the court's balustrade the Son stands in "
        "his cream robe with a small council of a dozen noble spirits "
        "around him, his arm extended out over the rail toward the "
        "deep where the unmade world waits — every face turned to "
        "follow the line of his arm, none toward the camera, which "
        "stands behind the group's shoulders shooting past them into "
        "the bright depth.",
        "the Son's extended arm aiming a small council's gazes out "
        "over the balustrade into bright depth, seen from behind the "
        "group",
        "faces to camera, halo, wings, blueprints or scrolls",
        era="heaven", jesus=True, ref=True, wide=True,
        locks=["COURT", "HOSTS"])),
    ("p03", "n2", _p(
        "The Builder's coastline: from very high, a young rugged "
        "coast where a dark ocean carves white surf against new "
        "mountains — long shadows of early morning, mist in the "
        "valleys, the land raw and unworn. Order arriving out of "
        "material. No figures, no life yet.",
        "a raw new coastline of surf, stone and valley mist from "
        "high above",
        "trees, animals, boats, buildings, figures",
        )),
    ("p04", "s2", _p(
        "Light over the deep: a dark primal sea from near the water, "
        "and across the whole horizon the first full dawn breaking — "
        "gold light running toward the camera down the swells, cloud "
        "banks burning slow above. The oldest morning. No land, no "
        "figures.",
        "first dawn light running down dark ocean swells toward the "
        "camera",
        "land, ships, birds, figures, drawn rays",
        )),
    ("p05", "n3", _p(
        "Organized material: the sheer face of a great canyon wall in "
        "evening light — hundreds of rock strata stacked level and "
        "true like coursed masonry, a river threading the gorge floor "
        "far below. Stone that reads as MASONRY at a planetary scale. "
        "No people.",
        "level stacked strata in a vast canyon wall like coursed "
        "masonry, river far below",
        "climbers, rails, text, buildings",
        wide=True)),
    ("p06", "n4", _p(
        "The finished classroom: a pristine green valley from a high "
        "shoulder — river loops, meadow, herds of deer grazing "
        "unafraid, morning mist burning off — a world set like a "
        "table before anyone arrives to sit down. No people.",
        "a pristine green valley with grazing herds and burning-off "
        "mist, no people",
        "fences, fields, smoke, buildings, people",
        wide=True)),
    ("p07", "g1", _p(
        "The course, laid out: a bare footpath switchbacking up a "
        "great mountain shoulder into high light — worn into the "
        "stone as if waiting for its first walker, climbing out of "
        "green into granite into sky. Empty. The test visible as "
        "terrain.",
        "an empty switchback path climbing a mountain from green to "
        "granite to sky",
        "signs, people, ropes, buildings",
        wide=True)),
    ("p08", "n5", _p(
        "Weather over the range: rain curtains dragging across "
        "distant peaks while near slopes stand in sun — the "
        "proving-ground climate, hard and bright in the same frame, "
        "an eagle riding the wind between. Dramatic without menace.",
        "sun and dragging rain sharing one mountain range, an eagle "
        "riding between",
        "lightning striking, tornado, darkness dominating, figures",
        wide=True)),
    ("p09", "n6", _p(
        "Known perfectly: the Father at the court's rail, seen in "
        "tender near-profile, looking down toward the small bright "
        "new world far below in the deep — the expression of a "
        "parent watching a nursery being finished. Warm light on "
        "His face; the world a soft blue-white brightness beyond "
        "the rail.",
        "the Father's tender near-profile at the rail over the "
        "small bright new world below",
        "His eyes on the lens, halo, tears, wings",
        era="heaven", locks=["FATHER", "COURT"])),
    ("p10", "n7", _p(
        "Resistance as design: a wild ibex mid-leap on a near-"
        "vertical cliff face, hooves finding an impossible ledge, "
        "the void yawning below — gravity and mastery in one "
        "frame, morning light raking the rock. The gym, in use.",
        "an ibex mid-leap on a near-vertical cliff over deep air",
        "falling, blood, people, text",
        )),
    ("p11", ("n7", 0.55), _p(
        "Human resistance: an ancient farmer building a terrace "
        "wall on a steep hillside — mid-lift with a heavy stone at "
        "his waist, forearms corded, completed courses of wall "
        "stepping down the slope behind him, terraced green "
        "already growing where he has finished. Seen from the "
        "side; his gaze is on the wall.",
        "a farmer mid-lift setting a heavy stone on a steep "
        "hillside terrace, finished courses behind",
        "his eyes on the lens, machinery, metal scaffolding",
        )),
    ("p12", "g2", _p(
        "Added upon: a lone shepherd cresting a high ridge line at "
        "sunrise, staff in hand, seen full-length from directly "
        "behind at the exact moment the rising light breaks over "
        "the ridge onto him — the climb behind him falling away "
        "into shadowed valley, the light ahead taking his "
        "shoulders. The camera stays low on the trail behind him.",
        "a shepherd from directly behind cresting a sunrise ridge, "
        "light breaking onto him, valley shadow below",
        "his face, drawn rays, halo, other people",
        wide=True)),
    ("p13", "n8", _p(
        "The same play at heavier weight, today: on a steep modern "
        "mountain trail, one hiker leans back to grip the forearm "
        "of another and pull them up a rock step — both seen from "
        "the side, faces turned to the rock and each other, "
        "daypacks and worn boots, valley air behind. Effort and "
        "help in one motion.",
        "one hiker pulling another up a rock step by the forearm, "
        "side view, faces on the rock and each other",
        "faces to camera, brand logos, readable gear text",
        era="modern")),
    ("p14", "n9", _p(
        "The unanswered how: a spiral ammonite fossil the size of "
        "a wheel embedded in a cliff face, evening light raking "
        "its ridges — deep time written in stone, beautiful and "
        "unexplained, a fingertip's distance from the camera. No "
        "people, no text.",
        "a great spiral fossil embedded in raking evening light, "
        "extreme close",
        "museum settings, labels, hands, text",
        )),
    ("p15", ("n9", 0.55), _p(
        "Deep time at dusk: banded canyon strata burning amber "
        "and rose in the last light, each layer a page nobody has "
        "fully read, the river's sound implied far below in the "
        "purple shadow. Reverent, unhurried. No people.",
        "banded canyon walls in amber dusk light over purple "
        "shadow",
        "climbers, rails, text, drawn rays",
        wide=True)),
    ("p16", "n10", _p(
        "Curriculum: a lone wind-bent tree on an exposed ridge in "
        "the full lash of a rainstorm — trunk leaning hard, every "
        "branch streaming one direction, roots gripping split "
        "rock — and holding. Grey driving weather, one unbroken "
        "living thing.",
        "a wind-lashed lone tree holding its ridge in driving "
        "rain",
        "lightning striking it, broken limbs falling, people",
        )),
    ("p17", ("n10", 0.55), _p(
        "After the lesson: the same ridge in clean washed morning "
        "light — the tree upright and green, rain steaming off "
        "its bark and the split rock, the storm's last clouds "
        "bright and breaking up behind it. Stronger where it "
        "bent.",
        "the same lone tree green and steaming in washed morning "
        "light, storm breaking up behind",
        "damage, people, rainbows, text",
        )),
    ("p18", "n11", _p(
        "Not his: the whole earth, blue and white and immense, "
        "hanging in black space with its day side in full "
        "brilliance — oceans burning turquoise at the sun-line, "
        "cloud systems wheeling slow — unowned by any thief, "
        "signed by its Builder. No figures, no text.",
        "the whole brilliant blue-white earth in black space, "
        "day side full",
        "figures, satellites, text, country outlines",
        )),
    ("p19", ("n11", 0.5), _p(
        "Your Father's school: a golden wheat-field path in low "
        "evening light, and far down it a family — father, "
        "mother, three children — walking away from the camera "
        "toward the bright end of the path, the smallest child's "
        "hand up in the father's. The camera stays low at the "
        "path's mouth behind them.",
        "a family of five from behind walking down a golden "
        "field path into low light",
        "faces turned back, buildings, wires, modern clothing "
        "details",
        era="ancient", wide=True)),
    ("p20", ("n11", 0.8), _p(
        "Architecture, signed: sunrise breaking over a great "
        "mountain rampart — the first light hitting the summit "
        "towers and pouring down the faces in gold while the "
        "valleys hold their blue — vast, deliberate, and "
        "beautiful. The closer's frame. No people.",
        "sunrise hitting mountain summit towers and pouring "
        "gold down their faces over blue valleys",
        "drawn rays, halo shapes, people, text",
        wide=True)),
]
