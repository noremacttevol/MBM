#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 22: The Changed Ordinances.

How you lose a church without anyone noticing: baptism shrinks, authority
gets assumed, the nature of God goes to committee — a form of godliness
with the power drained out. The drifters are honored as sincere; the
tragedy is missing keys, not evil men.
Anchors: Isaiah 24:5; 2 Timothy 3:5.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 322
NUM = 22
SLUG = "changed-ordinances"
TITLE = "The Changed Ordinances"
META = "Isaiah 24 · 2 Timothy 3"

SEGMENTS = [
    ("n1", NARRATOR,
     "Nobody voted to end the church of Jesus Christ. It drifted — one "
     "sincere renovation at a time. The devil's quietest move: a "
     "church lost without anyone noticing."),
    ("n2", NARRATOR,
     "With the apostles gone, the local shepherds did their best. But "
     "their best now had no revelation behind it — and the culture "
     "around them had opinions."),
    ("n3", NARRATOR,
     "Baptism changed first. Immersion — the burial and rebirth Jesus "
     "chose in the Jordan — shrank to a sprinkle. And infants "
     "replaced believers at the font, driven there by inherited "
     "guilt — a baptism nobody chooses, for a sin nobody committed. "
     "Episode eight told you what God thinks of that."),
    ("n4", NARRATOR,
     "Authority changed next. Offices Christ had filled by revelation "
     "began to be filled by election, by purchase, by politics. Men "
     "assumed the titles. But nobody left on earth could confer the "
     "keys."),
    ("n5", NARRATOR,
     "Then God's very nature went to committee. Councils of good men, "
     "doing philosophy under an emperor's impatience, voted the "
     "Father and Son into an abstraction no child could recognize — "
     "and you cannot freely choose a Father you cannot know. Stephen "
     "SAW them."),
    ("s1", SCRIPTURE,
     "The earth also is defiled under the inhabitants thereof; because "
     "they have transgressed the laws, changed the ordinance, broken "
     "the everlasting covenant."),
    ("n6", NARRATOR,
     "Isaiah called every beat of it, seven centuries in advance. Laws "
     "transgressed. The ordinance — changed. The everlasting covenant — "
     "broken."),
    ("n7", NARRATOR,
     "And Paul named the mechanism:"),
    ("s2", SCRIPTURE,
     "Having a form of godliness, but denying the power thereof: from "
     "such turn away."),
    ("n8", NARRATOR,
     "A form of godliness. The shape stayed — buildings, vestments, "
     "vocabulary. The power — priesthood, revelation, the gifts — is "
     "what drained out. Understand the devil's masterpiece here: it was "
     "never persecution. Persecution grew the church. His masterpiece "
     "was renovation."),
    ("n9", NARRATOR,
     "Now be careful how you hold this. The people inside that drift "
     "were not villains. They were mostly believers, doing their best "
     "in the dark — and God loves every one of them. The tragedy is "
     "not that men were evil. It is that the keys were gone, and "
     "sincerity cannot replace them."),
    ("n10", NARRATOR,
     "By the time the drift settled, the church OF Jesus Christ — "
     "apostles, revelation, ordinances as he gave them — had become "
     "churches ABOUT Jesus Christ. Good ones, many of them. But the "
     "organization heaven built was gone from the earth."),
    ("n11", NARRATOR,
     "So hold the difference that decides everything ahead: reformation "
     "repairs what men broke. Only restoration returns what heaven took "
     "back. That difference is why episode twenty-six happens in a "
     "grove — and not in a seminary."),
]

CARD_SEG = ("card", NARRATOR,
            "The shape stayed. The power left. That is how you lose a "
            "church without noticing.")

CARD_TEXT = ("The shape stayed.\n"
             "The power left.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Twenty-Two — The Changed Ordinances")

SPOKEN = {}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="old-world")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "Drift, made visible: a mason's plumb line hangs dead straight "
        "in the foreground — and behind it, sharp enough to judge, a "
        "stone wall leans visibly out of true, its courses wandering "
        "from the line's verdict. Close, quiet, damning. No people.",
        "a dead-straight plumb line against a visibly leaning stone "
        "wall",
        "collapse, ruins, people, text",
        )),
    ("p02", "n2", _p(
        "Their best, without keys: a young earnest presbyter teaches a "
        "packed plain room of villagers by window light — his hands "
        "open mid-explanation, faces attentive on benches, a child on "
        "a mother's knee — sincerity filling every corner of a room "
        "that revelation has quietly left. Warm, honest, human.",
        "an earnest young teacher mid-explanation to attentive "
        "villagers in a plain bright room",
        "vestments rich, mockery, faces to camera",
        )),
    ("p03", "n3", _p(
        "What baptism became: at a small carved stone font, an elderly "
        "priest tips a shell of water over a swaddled infant's brow — "
        "three drops catching the window light mid-fall — the parents "
        "close and anxious, everyone's gaze on the tiny face. Tender, "
        "sincere, and a world away from a river.",
        "three drops falling from a shell onto a swaddled infant at "
        "a stone font, anxious tender parents",
        "crying theatrics, mockery, faces to camera",
        )),
    ("p04", ("n3", 0.5), _p(
        "What baptism was — UPRIGHT VERTICAL FRAME, horizon level and "
        "LOW across the frame's lower third: the composition is "
        "anchored on the BAPTIZER STANDING FULL-HEIGHT mid-river, "
        "filling the frame's vertical, his braced arms angling DOWN "
        "toward the frame's bottom corner where the believer arcs "
        "backward into the closing water — green banks and standing "
        "witnesses rising behind the baptizer's shoulders into the "
        "frame's top. The whole-body covenant the font forgot.",
        "a grown believer being fully lowered backward into river "
        "water by braced arms, witnesses around",
        "faces to camera, crowds modern, doves",
        era="first-century")),
    ("p05", "n4", _p(
        "Authority, purchased: across a polished table in lamplight, "
        "a heavy purse of coins slides from one ringed hand toward "
        "another hand that rests beside a bishop's seal and staff of "
        "office — the exchange caught mid-slide, faces out of frame, "
        "the transaction the entire subject.",
        "a coin purse mid-slide across a table toward a hand by a "
        "bishop's seal and staff, faces out of frame",
        "faces, documents readable, church interior grand",
        )),
    ("p06", ("n4", 0.5), _p(
        "Titles, assumed: a new bishop is seated on a high carved "
        "chair by court officials in fine robes — one adjusts the "
        "vestment on his shoulders, another presents the staff — "
        "PLENTY of ceremony and not one kneeling ordination, not one "
        "hand laid on his head. Seen from the hall floor below the "
        "dais; every face on the pageant.",
        "officials seating and robing a new bishop with pageantry — "
        "no hands laid on his head anywhere",
        "an actual ordination, mockery, faces to camera",
        )),
    ("p07", "n5", _p(
        "God, by committee: a great council hall mid-vote — rows of "
        "robed churchmen with hands raised, clerks counting, and "
        "above them in a gilded box an emperor leaning forward "
        "impatiently with his chin on his fist — the divine nature "
        "waiting on the tally. Seen from behind the last row of "
        "raised arms.",
        "a hall of raised voting hands with clerks counting under "
        "an impatient emperor's gilded box",
        "faces to camera, violence, readable documents",
        wide=True)),
    ("p08", ("n5", 0.6), _p(
        "The covering: two workmen on scaffolding spread fresh "
        "plaster over an old wall-painting of a shepherd carrying a "
        "lamb — the warm simple fresco half-vanished under their "
        "sweeping trowels, only the lamb and the carrying arms "
        "still showing — while below, a geometric gold mosaic "
        "pattern waits stacked in trays to replace it. Nobody is "
        "angry; that is the horror.",
        "workmen's trowels half-covering a warm shepherd-and-lamb "
        "fresco, gold geometric mosaic trays waiting below",
        "faces to camera, smashing, torches, mockery",
        )),
    ("p09", "s1", _p(
        "Isaiah, seven centuries early: the prophet at his table by "
        "lamplight, pen stopped, his face turned toward the dark "
        "window as if watching the far future do exactly what he "
        "is writing — grief and certainty in the same lined "
        "features, the scroll's words soft and unreadable.",
        "Isaiah's pen stopped, face turned to the dark window in "
        "grieving certainty, unreadable scroll",
        "readable words, his eyes on the lens, visions shown",
        era="ancient")),
    ("p10", "s2", _p(
        "A form of godliness: a magnificent vestment displayed on a "
        "wooden stand in a dim sacristy — gold-threaded cope, "
        "jewelled mitre above it, gloves pinned at the sleeves — "
        "lamplight loving every thread, and NOBODY INSIDE IT: the "
        "shape of a shepherd, standing empty. Nothing else in "
        "frame.",
        "a jewelled empty vestment and mitre on a stand in "
        "lamplight, nobody inside it",
        "a person wearing it, mockery, decay",
        )),
    ("p11", "n8", _p(
        "The renovation: inside a church, scaffolding surrounds the "
        "chancel where workmen hoist a towering gilded altarpiece "
        "into place — and in the near foreground, carried out feet-"
        "first by two laborers, the original: a plain wooden table, "
        "small enough for a family meal, its surface worn by "
        "decades of simple bread. The trade, in one frame.",
        "a gilded altarpiece being hoisted behind while a plain "
        "worn wooden table is carried out feet-first in front",
        "faces to camera, destruction, mockery",
        wide=True)),
    ("p12", "n9", _p(
        "The sincere, honored: a village priest kneels alone at "
        "night before his little chapel's plain altar — patched "
        "cassock, work-rough hands clasped, head bowed in "
        "completely honest prayer, one candle. God hears this man. "
        "The warm light on his clasped hands says so.",
        "a patched-cassock priest kneeling alone in honest "
        "candlelit prayer, warm light on his hands",
        "his eyes to the lens, wealth, irony of any kind",
        )),
    ("p13", ("n9", 0.5), _p(
        "God loves them: candlelit faces of ordinary worshippers in "
        "the pews — an old woman's moving lips, a laborer's bowed "
        "head, a girl holding her mother's arm — devotion utterly "
        "real in every face, painted warm by the candle each "
        "holds. The famine's saints again, one era earlier.",
        "candlelit rows of sincere worshipping faces, each warm "
        "over their own flame",
        "faces to camera, gloom, caricature",
        )),
    ("p14", "n10", _p(
        "Churches ABOUT him: a city skyline at dusk crowded with "
        "differing spires and bell-towers — a dozen silhouettes of "
        "a dozen architectures against the amber sky, each one "
        "sincere, each one different, none of them the "
        "organization heaven drew. Beautiful and scattered.",
        "a dusk skyline of many differing sincere spires and "
        "towers",
        "modern buildings, signage, mockery",
        wide=True)),
    ("p15", "n11", _p(
        "Reformation's limit: a locksmith's workbench in window "
        "light — a great broken lock, disassembled, its plates "
        "polished bright and every part laid out with obvious "
        "care and skill — and NO KEY anywhere on the bench. The "
        "workman's honest tools can mend the case. They cannot "
        "cut what was never left behind.",
        "a broken lock lovingly disassembled and polished on a "
        "bench with NO key anywhere",
        "a key present, rust, hands, text",
        )),
    ("p16", ("n11", 0.5), _p(
        "Where the answer is buried: the wooded drumlin hill once "
        "more — SPRING now, new green over its slopes at first "
        "light, mist in the young orchards below — the same "
        "waiting hill, one era closer to its morning. No people, "
        "no marks.",
        "the drumlin hill in new spring green at first light, "
        "mist below, unmarked",
        "figures, paths, monuments, text",
        wide=True, era="america-1820")),
    ("p17", ("n11", 0.8), _p(
        "The bookend: the plumb line again — hanging beside a "
        "NEW wall this time, whose fresh courses run perfectly "
        "true to the string, morning light raking the honest "
        "joints. Somebody, somewhere, is going to build it "
        "straight again. Close, quiet, promised.",
        "the plumb line against a new perfectly true wall in "
        "raking morning light",
        "people, trowels, text",
        )),
]
