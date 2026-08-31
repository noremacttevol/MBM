#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 30: One Great Whole.

The dispensation of the fulness of times: every prior era's keys welded
into one kingdom that can never be lost again — Daniel's stone rolling,
and temples running the first rescue in history that goes BACKWARD.
Anchors: Ephesians 1:10; D&C 128:18; Daniel 2:44; 1 Peter 4:6.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 330
NUM = 30
SLUG = "one-great-whole"
TITLE = "One Great Whole"
META = "Ephesians 1 · D&C 128 · Daniel 2"

SEGMENTS = [
    ("n1", NARRATOR,
     "Every dispensation before ours ended in an ellipsis — keys given, "
     "keys lost, wait. Ours is different, on purpose. This one is the "
     "gathering-up of all of them."),
    ("s1", SCRIPTURE,
     "That in the dispensation of the fulness of times he might gather "
     "together in one all things in Christ, both which are in heaven, "
     "and which are on earth; even in him."),
    ("n2", NARRATOR,
     "The dispensation of the fulness of times — Paul's own name for our "
     "chapter. The era when God gathers together in one all things in "
     "Christ. Not another link in the chain. The welding of every "
     "link."),
    ("s2", SCRIPTURE,
     "It is necessary in the ushering in of the dispensation of the "
     "fulness of times, that a whole and complete and perfect union, "
     "and welding together of dispensations, and keys, and powers, and "
     "glories should take place."),
    ("n3", NARRATOR,
     "A welding together of dispensations, keys, powers, and glories. "
     "Adam's gospel. Enoch's Zion. Abraham's covenant. Moses' "
     "gathering. The apostles' keys. Elijah's sealing. All of it — one "
     "kingdom, one last time, never to be lost again."),
    ("n4", NARRATOR,
     "Daniel saw this exact thing from inside Babylon: a stone cut out "
     "of the mountain without hands — no army behind it, no empire — "
     "rolling until it fills the whole earth."),
    ("s3", SCRIPTURE,
     "And in the days of these kings shall the God of heaven set up a "
     "kingdom, which shall never be destroyed: and the kingdom shall "
     "not be left to other people, but it shall break in pieces and "
     "consume all these kingdoms, and it shall stand for ever."),
    ("n5", NARRATOR,
     "Never destroyed. Never left to other people. The old pattern — "
     "given, stolen, wait — is over. That is the whole point of the "
     "fulness of times. Last means last."),
    ("n6", NARRATOR,
     "And watch the stone roll. Six members in a farmhouse, eighteen "
     "thirty. Missionaries crossing oceans within the decade. Today — "
     "congregations across the nations, scripture in over a hundred "
     "languages, and temples: from one sparkling house in Kirtland to "
     "hundreds, on every inhabited continent."),
    ("n7", NARRATOR,
     "And the temples are the part the devil never saw coming. Because "
     "they do not only serve the living. You have heard this verse "
     "twice in this series. Hear where it lands:"),
    ("s4", SCRIPTURE,
     "For for this cause was the gospel preached also to them that are "
     "dead, that they might be judged according to men in the flesh, "
     "but live according to God in the spirit."),
    ("n8", NARRATOR,
     "In those houses, the living stand in for the dead — baptism, "
     "sealing, every ordinance — name, by name, by name. The famine's "
     "stolen centuries are being ministered to, person by person. "
     "Great-grandmothers who never heard a prophet's voice are hearing "
     "one now."),
    ("n9", NARRATOR,
     "Understand what that makes this work: the first rescue operation "
     "in history that runs backward. The devil's oldest victories — "
     "the drowned, the famine-born, the never-reached — are being "
     "un-won. Retroactively. On purpose. On a schedule."),
    ("n10", NARRATOR,
     "He has never faced anything like it. In every previous age, his "
     "losses stayed lost and his wins stayed won. Now nothing he ever "
     "won stays won. The stone is not just rolling forward. It is "
     "rolling back over everything he thought was settled."),
    ("n11", NARRATOR,
     "And you live inside that dispensation — the gathering of "
     "everything, forward and backward, into one. Whatever else your "
     "era gets wrong, know what it is FOR. The family is being welded "
     "whole. And a weld means forever."),
]

CARD_SEG = ("card", NARRATOR,
            "The first rescue in history that runs backward. Nothing he "
            "ever won stays won.")

CARD_TEXT = ("The rescue runs backward.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Thirty — One Great Whole")

SPOKEN = {}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="modern")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The weld: at a forge in warm work-light, a smith holds two "
        "red-hot chain links overlapped on the anvil — his hammer at "
        "the top of its arc, sparks around the joint where two links "
        "are becoming ONE — the striking instant of union. The same "
        "craft that built strength in episode four, now joining "
        "instead of shaping.",
        "two red-hot chain links overlapped on an anvil under a "
        "raised hammer, sparks at the joining point",
        "modern welding torches, machines, faces to lens",
        era="ancient")),
    ("p02", "s1", _p(
        "Gathered in one: at golden harvest, work-hands bind a dozen "
        "cut wheat sheaves into ONE great standing sheaf — the cord "
        "pulled tight around the gathered waists of grain, loose "
        "stalks being pressed into the bundle, stubble-field and "
        "afternoon sky beyond. Paul's word, in straw.",
        "hands binding many sheaves into one great sheaf with a "
        "tightened cord at harvest",
        "machinery, faces, storm",
        era="first-century")),
    ("p03", "n3", _p(
        "Every link, spliced: the great rope coiled on plain boards in "
        "raking light — and down its length, SIX distinct long-splices "
        "visible, each old break woven back stronger, the line "
        "continuous from first coil to last. All the dispensations, "
        "in one object the series has carried. No people.",
        "a coiled rope with six visible long-splices down its "
        "continuous length in raking light",
        "frays, knives, hands, text",
        )),
    ("p04", "n4", _p(
        "Daniel in Babylon: the seer stands at a high palace window "
        "at night — the torch-lit ziggurats and hanging terraces of "
        "the empire spread below him — his back to the room's "
        "opulence, his face in profile lifted from the city toward "
        "the dark mountains beyond it, where the dream said the "
        "stone would come from.",
        "Daniel in profile at a high night window over torch-lit "
        "Babylon, gaze on the dark mountains beyond",
        "his eyes on the lens, courtiers, readable writing",
        era="ancient")),
    ("p05", "s3", _p(
        "Cut without hands: a great rounded stone mid-ROLL down a "
        "mountain's scree slope — dust bursting at each strike, its "
        "path visibly begun at a raw notch high on the peak behind "
        "it, and NO figure, machine or hand anywhere on the "
        "mountain. Momentum with no explanation. The kingdoms' "
        "valley waits below.",
        "a great stone mid-roll down a scree slope from a raw "
        "notch above, dust bursting, nobody anywhere",
        "hands, figures, machinery, cities crushed in frame",
        era="ancient", wide=True)),
    ("p06", "n6", _p(
        "The stone is people: two young missionaries walk a dirt "
        "road two-by-two at morning — satchels on shoulders, worn "
        "boots, the road running ahead through open 1830s farm "
        "country — seen from behind, mid-stride, unhurried and "
        "unstoppable. This is what rolling looks like.",
        "two satchel-bearing missionaries from behind walking a "
        "morning dirt road through farm country",
        "faces, wagons, name tags readable",
        era="america-1820")),
    ("p07", ("n6", 0.4), _p(
        "Crossing oceans within the decade: at a ship's rail in "
        "grey-gold dawn, two more stand with their satchels looking "
        "toward a coastline just rising from the sea — the water "
        "wide behind them, the new field ahead — seen from beside "
        "and behind at the rail. The stone, learning to swim.",
        "two missionaries at a ship's rail from behind-beside, a "
        "coastline rising ahead at dawn",
        "faces, steamships modern, flags readable",
        era="america-1820")),
    ("p08", ("n6", 0.7), _p(
        "Today: a bright modern chapel mid-hymn — a congregation of "
        "every ancestry on earth singing from shared hymnbooks, "
        "children on laps, an old islander grandmother and a young "
        "African father sharing one book's edge — every face down "
        "at the pages or up in song, none at the lens. One church, "
        "everywhere at once.",
        "a modern all-ancestries congregation mid-hymn sharing "
        "books, children on laps",
        "readable hymn text, faces to camera, brand marks",
        wide=True)),
    ("p09", ("n6", 0.9), _p(
        "Temples on every continent: a white temple at dusk among "
        "PALMS — tropical evening sky, warm doors lit, a family in "
        "white walking up from behind — the Kirtland pattern, "
        "twelve time zones from Kirtland. The houses, multiplied.",
        "a lit white temple at dusk among palms with a white-"
        "dressed family climbing from behind",
        "signage, cars, faces to camera",
        wide=True)),
    ("p10", "s4", _p(
        "For the dead: a temple baptistry — the great font resting "
        "on the backs of twelve sculpted oxen, water still and "
        "bright under soft light, white-dressed youth waiting at "
        "the rail with their backs to the camera — the verse from "
        "the flood episode, landing in its workroom.",
        "a still bright font on twelve sculpted oxen with white-"
        "dressed youth from behind at the rail",
        "faces, splashing, readable text",
        )),
    ("p11", "n8", _p(
        "Name by name: a young woman's hand carries a single small "
        "white card into the font-room's light — the printed name "
        "on it soft and unreadable, her white sleeve bright, the "
        "water's reflection moving on the wall beyond. One "
        "great-grandmother's turn, arriving.",
        "a hand carrying one small white card with unreadable "
        "print into font-room light",
        "readable names, faces, stacks of cards",
        )),
    ("p12", "n9", _p(
        "The rescue runs backward: a long line of unlit candles on "
        "a dark table — and the light is moving DOWN the line the "
        "wrong way: the candle nearest the window's sunrise is "
        "lighting its neighbor BEHIND it, which lights the one "
        "behind that, three flames already alive and travelling "
        "into the dark end of the line. Time, being repaid.",
        "a candle line lighting BACKWARD from the sunrise end into "
        "the dark end, three flames travelling",
        "hands, wax mess, text",
        )),
    ("p13", "n10", _p(
        "Nothing stays won: the cold dead fire-ring from the "
        "ancient camp — RELIT: a young flame standing up from new "
        "kindling inside the old blackened stones, night around "
        "it, sparks rising. A hearth the enemy counted as his, "
        "burning again. No people.",
        "a young flame relit inside an old blackened fire-ring at "
        "night, sparks rising",
        "figures, ruins, storm",
        era="ancient")),
    ("p14", ("n10", 0.6), _p(
        "The weld, cooled and proven: tongs hold the finished "
        "chain up to the light — the two links now ONE continuous "
        "joined link at the centre, the weld-seam smooth and "
        "thicker than the metal around it, work-light rimming "
        "nothing, just steel that will never come apart. Close.",
        "tongs holding a chain to the light with one smooth "
        "welded double-link at centre",
        "sparks now, hands bare, rust",
        era="ancient")),
    ("p15", "n11", _p(
        "You live here: a young family walks up wide temple steps "
        "into evening light — father, mother, a daughter holding "
        "each hand, all in Sunday white, seen from behind at the "
        "foot of the steps as the doors' warmth takes them in — "
        "the dispensation of gathering, at street level, tonight.",
        "a young family in white from behind climbing temple "
        "steps into warm door-light",
        "faces, signage, crowds",
        )),
    ("p16", ("n11", 0.7), _p(
        "The stone keeps rolling: sunrise over the curve of open "
        "rolling farmland — the light itself rolling down the "
        "hills field by field, waking the world westward, no end "
        "of it in sight. Where this is all headed. No people.",
        "sunrise light rolling westward down open farmland hills, "
        "no end in sight",
        "figures, buildings, drawn rays",
        wide=True)),
]
