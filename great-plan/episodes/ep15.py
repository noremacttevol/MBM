#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 15: He Kept Sending.

A thousand years of forgetting answered by a God who rises early and sends
anyway — the prophet-relay, Carmel's fire, and the portrait of the Servant
the runners carried toward Bethlehem.
Anchors: 2 Chronicles 36:15; Amos 3:7; 1 Kings 18:38-39; Isaiah 53:5.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 315
NUM = 15
SLUG = "he-kept-sending"
TITLE = "He Kept Sending"
META = "2 Chronicles 36 · 1 Kings 18 · Isaiah 53"

SEGMENTS = [
    ("n1", NARRATOR,
     "If somebody ignored your calls a thousand times, how long before "
     "you stopped calling? Hold that answer. Now meet the God who never "
     "stopped."),
    ("n2", NARRATOR,
     "After Moses, Israel settled the promised land — and started a "
     "cycle. Forget God. Fall apart. Cry out. Be rescued. And forget "
     "again. For centuries."),
    ("n3", NARRATOR,
     "And here is the verse that shows you God's side of that "
     "millennium:"),
    ("s1", SCRIPTURE,
     "And the Lord God of their fathers sent to them by his messengers, "
     "rising up betimes, and sending; because he had compassion on his "
     "people, and on his dwelling place."),
    ("n4", NARRATOR,
     "Rising up betimes — that means early in the morning. Picture it: "
     "a God up at dawn, sending the next messenger. And the reason is "
     "right there in the verse. Not policy. Compassion."),
    ("n5", NARRATOR,
     "That is what a prophet is — God's early-morning messenger. And "
     "heaven is committed to the system:"),
    ("s2", SCRIPTURE,
     "Surely the Lord God will do nothing, but he revealeth his secret "
     "unto his servants the prophets."),
    ("n6", NARRATOR,
     "Nothing without prophets. That is standing policy. So when you "
     "hear the word prophet, do not picture a fortune-teller. Picture a "
     "relay runner — carrying one unchanging message through a "
     "forgetful thousand years."),
    ("n7", NARRATOR,
     "Sometimes the relay got loud. Mount Carmel: one prophet, Elijah, "
     "against four hundred and fifty priests of Baal. All day their god "
     "said nothing. Then Elijah drowned his own altar in water — and "
     "called."),
    ("s3", SCRIPTURE,
     "Then the fire of the Lord fell, and consumed the burnt sacrifice, "
     "and the wood, and the stones, and the dust, and licked up the "
     "water that was in the trench. And when all the people saw it, "
     "they fell on their faces: and they said, The Lord, he is the God; "
     "the Lord, he is the God."),
    ("n8", NARRATOR,
     "The Lord, He is the God. One demonstration, and a generation "
     "turned. But fire fades from memory faster than you would think — "
     "and the cycle rolled again. So God kept sending."),
    ("n9", NARRATOR,
     "And the messengers began carrying something new. Isaiah, seven "
     "hundred years early, described a Servant — despised, rejected, "
     "and wounded. The relay was no longer just carrying a message. It "
     "was carrying a portrait."),
    ("s4", SCRIPTURE,
     "But he was wounded for our transgressions, he was bruised for our "
     "iniquities: the chastisement of our peace was upon him; and with "
     "his stripes we are healed."),
    ("n10", NARRATOR,
     "Every prophet, whatever else he carried, carried Him. The whole "
     "relay was running toward one Person. And some of the runners were "
     "killed for the message — and the next one came anyway. That is "
     "what compassion does."),
    ("n11", NARRATOR,
     "So if you have ever wondered whether God gets tired of reaching "
     "for someone who keeps forgetting Him — you now hold a thousand "
     "years of receipts. He rises early. He keeps sending. And He has "
     "not stopped."),
]

CARD_SEG = ("card", NARRATOR,
            "A thousand years of forgetting. A thousand years of sending "
            "anyway. He has never stopped.")

CARD_TEXT = ("He rises early.\n"
             "He keeps sending.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Fifteen — He Kept Sending")

SPOKEN = {"betimes": "bee TIMES"}

ELIJAH = (
    "ELIJAH LOCK: the same man in every picture — the Tishbite: wiry and "
    "weather-hardened, deep tan skin, wild shoulder-length grey-streaked "
    "dark hair, a ragged full beard, wearing his rough camel-hair mantle "
    "over a plain tunic with a wide leather girdle at the waist. Eyes "
    "like struck flint. No halo, no glow.")

LOCKS = {"ELIJAH": ELIJAH}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="ancient")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The unanswered call: a lone watchman stands on a city wall at "
        "coldest pre-dawn, wrapped in his cloak, looking out over dark "
        "silent country where no answer comes — seen from behind on "
        "the parapet walk, one small horn-lamp burning at his feet. "
        "The posture of waiting that has lasted years.",
        "a cloaked watchman from behind on a pre-dawn wall over dark "
        "silent country, one small lamp at his feet",
        "his face, armies, dawn yet, torches on the wall",
        )),
    ("p02", "n2", _p(
        "The forgetting: at the edge of a harvest-fat village, a "
        "little roadside shrine crowded with small carved idols — "
        "fresh offerings of grapes, oil and coins heaped before them, "
        "a garland still green — while in the soft background the "
        "village feasts under lamplight. Prosperity, mid-drift.",
        "a tended roadside idol-shrine heaped with fresh offerings, "
        "feasting village soft behind",
        "worshippers close, faces, grotesque idols, darkness",
        )),
    ("p03", ("n2", 0.6), _p(
        "The falling apart: the same country under a smoke-smudged "
        "sky — a farm family hurrying up a ridge-path away from the "
        "camera with bundles on their backs, the youngest looking "
        "back from a father's arms toward a distant column of black "
        "smoke rising off their valley. History's oldest bill, come "
        "due.",
        "a burdened family from behind hurrying up a ridge under a "
        "distant smoke column, small child looking back over a "
        "shoulder",
        "raiders visible, flames close, wounds, faces to camera",
        wide=True)),
    ("p04", "s1", _p(
        "Rising up betimes: an old prophet steps out of his stone "
        "doorway at the exact crack of dawn — staff in hand, worn "
        "satchel across his chest, the door still swinging behind "
        "him — seen from behind as he takes the long pale road that "
        "runs from his threshold to the horizon. The first light is "
        "barely up. He is already out in it.",
        "an old prophet from behind leaving his door at first light "
        "onto a long pale road, staff and satchel",
        "his face, companions, cities, darkness",
        wide=True)),
    ("p05", "n4", _p(
        "Compassion, weathered: the prophet's face in close profile "
        "against the dawn — deep-lined, wind-burned, and utterly "
        "tender in the set of the mouth, the eyes fixed on the road "
        "ahead with the softness of a man carrying someone else's "
        "rescue in his satchel.",
        "an old messenger's close profile, deep-lined and tender, "
        "eyes on the unseen road",
        "his eyes on the lens, tears, harshness, halo",
        )),
    ("p06", "s2", _p(
        "The secret revealed: a prophet on a flat rooftop at deep "
        "night, kneeling upright among the sleeping town's rooflines, "
        "face lifted to a sky crowded with stars, both hands open on "
        "his thighs — the receiving posture, held in complete "
        "stillness. One window burns dim in the town below.",
        "a prophet kneeling upright on a night rooftop, face lifted "
        "to dense stars, open hands, one dim window below",
        "his face close, angels, light descending, text",
        )),
    ("p07", "n6", _p(
        "The relay: in warm darkness, one burning clay oil lamp "
        "passes between two pairs of hands — an old spotted hand "
        "releasing it, a young calloused hand receiving underneath — "
        "the flame steady through the exchange, nothing else in "
        "frame but the hands, the lamp, and the dark it holds off.",
        "a burning oil lamp mid-pass between an old hand and a "
        "young hand in warm darkness",
        "faces, sleeves modern, wind on the flame, text",
        )),
    ("p08", "n7", _p(
        "Carmel, drenched: Elijah upends the last water-jar over an "
        "altar of stacked stones and cut wood — the water sheeting "
        "off the sacrifice, the trench around the base brimming and "
        "spilling — while behind him on the summit's far side the "
        "exhausted priests of Baal sprawl among their silent altar's "
        "smoke-less stones. Grey afternoon; one man, soaked "
        "confidence.",
        "Elijah pouring the last jar over a drenched altar with a "
        "brimming trench, exhausted rival priests sprawled far "
        "behind",
        "fire yet, blood, self-cutting shown, faces to camera",
        wide=True, locks=["ELIJAH"])),
    ("p09", "s3", _p(
        "THE FIRE FALLS: a blinding column of white fire strikes "
        "down from the low cloud straight onto the drenched altar — "
        "stones and water flashing to steam at its foot, the light "
        "of it hurled across the whole summit, the nearest "
        "onlookers flung back with arms across their faces — the "
        "column vertical, singular, and absolute. Elijah stands "
        "unmoved at its edge, small against the blaze.",
        "one vertical column of white fire striking the altar, "
        "steam-flash, onlookers flung back shielding, Elijah "
        "small and unmoved",
        "lightning bolts branching, faces to camera, the fire "
        "spreading",
        wide=True, locks=["ELIJAH"])),
    ("p10", ("s3", 0.6), _p(
        "The verdict: the whole multitude prostrate down the "
        "summit's slope — hundreds of backs and pressed-down faces "
        "flat to the stony ground in every direction — and one "
        "figure still standing among them: Elijah, mantle scorched "
        "with light, facing the smoking altar-scar against the "
        "torn sky. Seen from low within the prostrate crowd.",
        "a prostrate multitude flat to the ground with Elijah "
        "alone standing against the smoking altar-scar",
        "faces visible, cheering, the fire still falling",
        wide=True, locks=["ELIJAH"])),
    ("p11", "n8", _p(
        "Fire fades: the same summit a generation later — the "
        "altar's stones scattered and half-buried, thorn and "
        "yellow weed grown through the old trench-line, wind "
        "moving the grass under a plain grey sky. Nobody "
        "remembers. Nothing marks it.",
        "the scattered overgrown altar stones and weed-filled "
        "trench under plain grey sky",
        "people, monuments, drama, text",
        )),
    ("p12", "n9", _p(
        "The portrait begins: Isaiah at his writing-table by lamp, "
        "reed pen stopped mid-stroke on the scroll, his other hand "
        "pressed over his mouth and his eyes bright with tears at "
        "what he is being shown — the words beneath his pen soft "
        "and unreadable. The Servant, arriving in ink.",
        "Isaiah stopped mid-stroke, hand over mouth, wet bright "
        "eyes, unreadable scroll beneath the lamp",
        "readable words, his eyes on the lens, visions shown",
        )),
    ("p13", "s4", _p(
        "With his stripes: a shepherd sits on a stone holding a "
        "hurt lamb wrapped in a strip of his own torn mantle "
        "against his chest — the lamb's head resting under his "
        "chin, his eyes closed, one big hand covering the small "
        "bandaged flank. Isaiah's portrait, in the only language "
        "the centuries had. Close and still.",
        "a shepherd cradling a cloth-wrapped hurt lamb under his "
        "chin, eyes closed, hand over the bandaged flank",
        "blood visible, distress in the lamb, faces to camera",
        )),
    ("p14", "n10", _p(
        "The cost of carrying it: a prophet's dropped staff and "
        "spilled scroll-satchel lying on a stony road at dusk — "
        "the scrolls fanned loose in the dust, one sandal on its "
        "side a stride away, the road empty in both directions. "
        "The frame states it plainly: the runner did not drop "
        "these on purpose. No body is shown; nothing about it "
        "reads as rest.",
        "a dropped staff, spilled scrolls and one overturned "
        "sandal on an empty dusk road",
        "a body, blood, attackers, peaceful arrangement",
        )),
    ("p15", ("n10", 0.55), _p(
        "The next one came anyway: the same stony road at the "
        "next dawn — and a NEW messenger walking through the "
        "frame past the fallen satchel, caught mid-stride from "
        "the side, his jaw set, his own satchel on his chest, "
        "not stopping, eyes on the horizon ahead. The relay, "
        "refusing to end.",
        "a new messenger mid-stride past the fallen satchel at "
        "dawn, jaw set, eyes ahead",
        "his eyes on the lens, mourning pause, crowds",
        )),
    ("p16", "n11", _p(
        "A thousand years of receipts: a stone wall-niche stacked "
        "deep with worn scroll-cases and rolled parchments — "
        "leather ties frayed, edges gone velvet with handling, "
        "one lamp lighting the hoard of messages — every word "
        "soft and unreadable, every scroll a morning God rose "
        "early. Close.",
        "a lamplit niche stacked deep with worn unreadable "
        "scrolls and cases",
        "readable text, faces, dust of neglect",
        )),
    ("p17", ("n11", 0.5), _p(
        "He still does: sunrise through a present-day kitchen "
        "window falling across an open well-worn book of "
        "scripture and a steaming mug on the table — the light "
        "laying a bright path across the unreadable pages, chairs "
        "empty, the house just waking. The morning message, "
        "still delivered daily.",
        "sunrise across an open worn scripture book and steaming "
        "mug on a kitchen table",
        "readable text, people, phone, brand marks",
        era="modern")),
    ("p18", ("n11", 0.8), _p(
        "The road, forever: a pale dawn road running dead "
        "straight to the horizon between dew-grey fields — and "
        "far down it, one small figure with a staff walking away "
        "into the light, unhurried, constant. The last frame of "
        "a messenger who has never once stopped.",
        "one small staff-bearing figure far down a straight dawn "
        "road walking into the light",
        "his face, vehicles, wires, text",
        wide=True)),
]
