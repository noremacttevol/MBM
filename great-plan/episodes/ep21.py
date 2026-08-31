#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 21: Kill the Messengers.

The strategy after the empty tomb: hunt the keyholders. Stephen's two-
Person vision, the empire-wide hunt, Paul's written warnings, and the
arithmetic of keys leaving the earth.
Anchors: Acts 7:56; Acts 20:29-30; 2 Thessalonians 2:3.

Laws in force: SCREEN-SIDE (Stephen's vision — the Son at the Father's
right hand stands on the VIEWER'S LEFT, Cameron's row-179 rule, origin
case); LITERAL-DEATH (martyrs are plainly killed, never asleep; no impact
or gore is ever shown).
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 321
NUM = 21
SLUG = "kill-the-messengers"
TITLE = "Kill the Messengers"
META = "Acts 7 · Acts 20 · 2 Thessalonians 2"

SEGMENTS = [
    ("n1", NARRATOR,
     "The tomb is empty. Death is broken. So how do you fight a risen "
     "King? You cannot. But you can hunt down every man He authorized — "
     "and that is exactly what happened next."),
    ("n2", NARRATOR,
     "The apostles turned the world upside down. Thousands baptized. "
     "Congregations from Jerusalem to Rome. And the enemy's answer came "
     "fast."),
    ("n3", NARRATOR,
     "Stephen was first — dragged before the council for preaching "
     "Christ. And as they raged, he looked up, and told them exactly "
     "what he saw:"),
    ("s1", SCRIPTURE,
     "Behold, I see the heavens opened, and the Son of man standing on "
     "the right hand of God."),
    ("n4", NARRATOR,
     "Two Persons — the Son, standing at the Father's right hand — seen "
     "by a dying man and declared with his last breaths. They stoned him "
     "for saying it. Stephen was killed praying for his killers — while "
     "a young man named Saul stood watching the coats."),
    ("n5", NARRATOR,
     "Then James, by the sword. Then the hunt went empire-wide. Peter — "
     "crucified. Paul, the coat-watcher turned apostle — beheaded in "
     "Rome. John — exiled to a prison island. One by one, the men "
     "holding the keys were killed."),
    ("n6", NARRATOR,
     "And the apostles saw it coming. They said so, in writing. Paul, "
     "to the elders of Ephesus, through tears:"),
    ("s2", SCRIPTURE,
     "For I know this, that after my departing shall grievous wolves "
     "enter in among you, not sparing the flock. Also of your own "
     "selves shall men arise, speaking perverse things, to draw away "
     "disciples after them."),
    ("n7", NARRATOR,
     "Wolves from outside — and of your own selves, from inside. And to "
     "the saints waiting eagerly for Christ's return, Paul wrote a "
     "sentence the whole world should have underlined:"),
    ("s3", SCRIPTURE,
     "Let no man deceive you by any means: for that day shall not come, "
     "except there come a falling away first."),
    ("n8", NARRATOR,
     "A falling away — FIRST. Before the Lord returns: a departure. An "
     "apostasy. That is not a Latter-day Saint invention. That is Paul, "
     "in your own Bible, on the record."),
    ("n9", NARRATOR,
     "Now count with me, because this arithmetic is the whole tragedy. "
     "Ordaining an apostle takes an apostle. Kill them faster than they "
     "can ordain — and one day, somewhere in the empire, the last man "
     "holding the keys dies. No meeting. No headline. Just... gone."),
    ("n10", NARRATOR,
     "The believers stayed. The buildings stayed. Most of the "
     "scriptures stayed. But the authority — the priesthood keys Christ "
     "placed on living men — left the earth with the last of them. The "
     "devil could not kill the risen Christ. So he took the church "
     "instead."),
    ("n11", NARRATOR,
     "Which means: if heaven ever wanted that authority back on the "
     "earth, dead men would have to return to bring it. Hold that "
     "thought. For about seventeen hundred years."),
]

CARD_SEG = ("card", NARRATOR,
            "He could not kill the King. So he killed the men with the "
            "keys — and settled in to wait.")

CARD_TEXT = ("The keys left the earth\n"
             "with the last of them.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Twenty-One — Kill the Messengers")

SPOKEN = {}

STEPHEN = (
    "STEPHEN LOCK: the same young man in every picture — Stephen the "
    "deacon: mid-twenties, olive-skinned, short dark curled hair, a "
    "sparse young beard, plain grey-white tunic, and a face scripture "
    "says shone like an angel's: open, fearless, alight from within by "
    "expression alone — never by any light effect. No halo, no glow.")

LOCKS = {"STEPHEN": STEPHEN}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="first-century")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The church exploding: a river at midday crowded with joy — "
        "three baptisms happening at once in the shallows, white-clad "
        "converts being lowered and raised, dozens more waiting on the "
        "banks with families, singing readable in the open mouths — "
        "seen wide from the far bank. The problem the enemy has to "
        "solve.",
        "three simultaneous river baptisms with singing crowds "
        "waiting on the banks",
        "faces to camera, soldiers, storm, halo",
        wide=True)),
    ("p02", "n2", _p(
        "Upside down: an apostle preaching from the temple portico "
        "steps to a packed and growing crowd — his arms wide "
        "mid-proclamation, listeners pressing in from the colonnades, "
        "new arrivals running at the frame's edges — the camera deep "
        "in the crowd shooting past heads and shoulders. Momentum "
        "nothing human can stop.",
        "an apostle proclaiming from portico steps over a packed "
        "growing crowd, runners arriving at the edges",
        "faces to camera, soldiers yet, banners",
        wide=True)),
    ("p03", "n3", _p(
        "Seized: Stephen gripped by both arms before the shadowed "
        "council — his young face the only lit and PEACEFUL thing in "
        "the frame, alight with something none of his captors can "
        "see, while robed accusers lean and point around him. His "
        "peace is the provocation.",
        "Stephen gripped before leaning pointing accusers, his "
        "young face peaceful and alight by expression alone",
        "any light effect on his face, wounds, faces to camera",
        locks=["STEPHEN"])),
    ("p04", "s1", _p(
        "What Stephen saw: the heavens OPENED — a great breach of "
        "light above, and standing in it, TWO glorified Persons in "
        "the air: the Son in his familiar cream STANDING at the "
        "Father's right hand, which places the Son on the VIEWER'S "
        "LEFT and the Father in radiant white on the VIEWER'S RIGHT "
        "— never reversed. Both faces turned down with open warmth "
        "toward the unseen martyr below the frame. Open air beneath "
        "their feet; no outline or aura edges their bodies.",
        "the Son in cream STANDING on the viewer's LEFT at the "
        "right hand of the Father in white on the viewer's RIGHT, "
        "both in opened heavens looking down with warmth",
        "sides reversed, wings, halos, aura outlines, thrones, "
        "either gaze at the lens",
        jesus=True, ref=True, wide=True, locks=["FATHER"])),
    ("p05", ("s1", 0.5), _p(
        "The council's answer: the accusers erupt — elders clapping "
        "hands over their ears, faces contorted, robes swirling as "
        "the whole room surges forward in a wave of rage — seen "
        "from behind Stephen's calm shoulder so the human storm "
        "breaks toward the camera's anchor of peace. Not one face "
        "toward the lens.",
        "elders stopping their ears and surging in rage, seen past "
        "Stephen's calm near shoulder",
        "stones yet, violence, faces to camera",
        locks=["STEPHEN"])),
    ("p06", "n4", _p(
        "While he prayed: outside the walls, Stephen kneels upright "
        "in the stony hollow with his face lifted and lips moving "
        "in prayer — serene, fully alight — while around him the "
        "ring of men stands frozen at the edge of violence, arms "
        "drawn back, faces hard — the frame holding the instant "
        "BEFORE, forever. No stone flies; no impact is ever "
        "shown.",
        "Stephen kneeling upright in serene prayer inside a ring "
        "of men frozen at the edge of violence",
        "impact, flying stones, blood, wounds, faces to camera",
        locks=["STEPHEN"])),
    ("p07", ("n4", 0.6), _p(
        "The coats: young Saul stands over the heaped cloaks of "
        "the throwers, his arms folded, his intelligent face "
        "looking down toward the frame's lower corner where the "
        "aftermath lies out of view except for one still, open "
        "hand at rest on the stones — plainly beyond sleep. "
        "Saul's face carries the first faint crack of what will "
        "one day become Damascus.",
        "Saul over the heaped coats, arms folded, gaze down at "
        "one still open hand at the frame's corner",
        "the body shown, blood, wounds, faces to camera",
        )),
    ("p08", "n5", _p(
        "The machine: a Roman detachment marches a torch-lit "
        "night street in hard formation — spear-shafts in rhythm, "
        "armor throwing back the flame-light, a scatter of "
        "believers pressing into doorways as the column passes — "
        "all backs and profiles, the hunt as infrastructure.",
        "a torch-lit Roman column marching in rhythm past "
        "believers pressed into doorways",
        "arrests shown, violence, faces to camera",
        wide=True)),
    ("p09", ("n5", 0.4), _p(
        "Peter, led: the old fisherman-apostle walks in chains "
        "along a stone quay between guards at grey dawn — his "
        "back straight, his step unhurried, the chains carried "
        "like they weigh nothing — seen from behind and beside, "
        "a following gull low over the harbor water. Tradition "
        "says he asked for harder than his Lord's death; the "
        "frame keeps his dignity and shows nothing more.",
        "chained Peter walking straight-backed between guards "
        "along a dawn quay, unhurried",
        "crosses, execution site, wounds, faces to camera",
        )),
    ("p10", ("n5", 0.7), _p(
        "Paul, gone: a Roman cell after — the door standing open, "
        "a folded travel cloak on the plank bed, a stack of "
        "finished letters bound with cord on the small table, "
        "the stylus laid across the last one, morning light "
        "through the high grate. The occupant is not coming "
        "back; the letters are already on their way to forever.",
        "an open empty cell with folded cloak, corded letter "
        "stack and laid-down stylus in high grate-light",
        "blood, chains broken, a body, guards",
        )),
    ("p11", "s2", _p(
        "Through tears at Miletus: Paul grips the forearms of "
        "two weeping elders on the shore — his own eyes wet and "
        "fierce with warning, the other elders crowded close "
        "with bowed heads, and the waiting ship's rigging dark "
        "against the grey sea behind. A goodbye that knows what "
        "is coming.",
        "Paul gripping weeping elders' forearms on the shore, "
        "wet fierce warning eyes, waiting ship behind",
        "faces to camera, scrolls readable, calm cheer",
        )),
    ("p12", "s3", _p(
        "On the record: Paul writing by lamp in a rented room — "
        "the reed pen mid-stroke, his scarred face set in "
        "resolute grief, the sentence beneath his hand soft and "
        "unreadable — a warning underlined by history, being "
        "mailed to the future.",
        "Paul mid-stroke by lamplight, scarred resolute grieving "
        "face, unreadable letter",
        "readable words, his eyes on the lens, chains",
        )),
    ("p13", "n9", _p(
        "The arithmetic: an upper room at evening — TWELVE low "
        "stools around the long table, and only TWO of them "
        "occupied, by two grey old men bent together over the "
        "bread — the other ten stools empty in the guttering "
        "lamplight, each one a account settled by the empire. "
        "The count, falling.",
        "twelve stools with only two old men remaining at the "
        "lamplit table, ten empty",
        "ghosts, name markers, faces to camera",
        )),
    ("p14", ("n9", 0.6), _p(
        "The last one: one ancient man alone at the same table — "
        "eleven empty stools around him, one lamp, his hand "
        "moving steadily across a page he will not finish "
        "distributing — the room's shadows deep and patient "
        "around the final holder of the keys. Nothing dramatic "
        "left to show; that is the tragedy.",
        "one ancient man writing alone among eleven empty "
        "stools by a single lamp",
        "angels, light effects, tears, faces to camera",
        )),
    ("p15", "n10", _p(
        "Just... gone: the same upper room at grey morning, "
        "empty — twelve stools in their places, the lamp cold "
        "on the table, dust beginning its long tenancy in the "
        "window light — the exact room the famine episode will "
        "find again, centuries deep in silence. No people, "
        "ever again.",
        "the empty upper room at grey morning — twelve vacant "
        "stools, cold lamp, first dust in the light",
        "figures, cobwebs heavy, decay dramatic",
        )),
    ("p16", ("n10", 0.5), _p(
        "The believers stayed: a small congregation kneels close "
        "together in a candlelit catacomb chamber — a dozen "
        "faces of every age bowed or lifted in earnest prayer "
        "around two candles, painted symbols soft and "
        "unreadable on the tufa walls — faith, holding on in "
        "the dark with everything except the keys.",
        "a dozen catacomb believers kneeling close around two "
        "candles, earnest bowed and lifted faces",
        "readable inscriptions, fear theatrics, soldiers, "
        "faces to camera",
        )),
    ("p17", "n11", _p(
        "Hold that thought: the night sky immense over the dark "
        "Judean hills — the stars in their silent thousands, "
        "patient as arithmetic, over a world that does not yet "
        "know what it lost — the long wait, beginning. No "
        "figures.",
        "an immense patient star-field over dark silent hills",
        "meteors, angels, dawn, text",
        wide=True)),
    ("p18", ("n11", 0.7), _p(
        "Elegy: a fisherman's net folded with terrible neatness "
        "on the stones of an empty shore at dusk — the floats "
        "still, the mended places visible in the weave, the "
        "grey sea quiet beyond. A trade laid down; a work "
        "interrupted; a promise waiting for hands again.",
        "a neatly folded fishing net with visible mends on "
        "empty dusk shore stones",
        "boats burning, bodies, birds, text",
        )),
]
