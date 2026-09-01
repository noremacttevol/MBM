#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 9: The First Gospel.

Adam receives the whole gospel immediately — sacrifice as similitude, the
angel's explanation, Adam's baptism — and Satan opens his counterfeit
ministry: "I am also a son of God... believe it not."
Anchors: Moses 5:4-13; Moses 6:64-65.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 309
NUM = 9
SLUG = "first-gospel"
TITLE = "The First Gospel"
META = "Moses 5-6"

SEGMENTS = [
    ("n1", NARRATOR,
     "What happens to a family cut off from Eden? Watch what God does in "
     "the very first chapter after the gate closes — because it destroys "
     "the picture of an abandoning God forever."),
    ("n2", NARRATOR,
     "Adam and Eve built a life in the fallen world. And they prayed. And "
     "heaven answered. The veil kept them from His presence — but He "
     "never once went silent."),
    ("s1", SCRIPTURE,
     "And after many days an angel of the Lord appeared unto Adam, "
     "saying: Why dost thou offer sacrifices unto the Lord? And Adam said "
     "unto him: I know not, save the Lord commanded me."),
    ("n3", NARRATOR,
     "Stop on that answer. I know not, save the Lord commanded me. Adam "
     "had been offering the firstlings of his flock for years without "
     "knowing why. Pure trust, ahead of understanding. And because he "
     "obeyed first, the explanation came:"),
    ("s2", SCRIPTURE,
     "This thing is a similitude of the sacrifice of the Only Begotten "
     "of the Father, which is full of grace and truth."),
    ("n4", NARRATOR,
     "A similitude. Every lamb on every altar was a picture — pointing "
     "four thousand years forward, to the Lamb. Adam and Eve knew about "
     "Jesus Christ. The first family on earth had His gospel: faith, "
     "repentance, baptism, the Holy Ghost."),
    ("s3", SCRIPTURE,
     "Adam cried unto the Lord, and he was caught away by the Spirit of "
     "the Lord, and was carried down into the water, and was laid under "
     "the water, and was brought forth out of the water."),
    ("n5", NARRATOR,
     "Baptized. The first man on this earth was baptized — same "
     "ordinance, same gospel, same Christ that saves anybody today. The "
     "gospel is not an invention of the meridian of time. It is older "
     "than the world."),
    ("n6", NARRATOR,
     "And now watch the enemy's response, because it defines his playbook "
     "for the rest of history."),
    ("d1", DEVIL,
     "I am also a son of God. Believe it not."),
    ("n7", NARRATOR,
     "That is his first recorded sermon on earth. Notice what he did not "
     "say. He did not say there is no God. He said I am ALSO a son of God "
     "— a counterfeit claim to authority — and then: believe it not. "
     "Doubt, preached as doctrine. He has never fought religion. He "
     "manufactures his own."),
    ("n9", NARRATOR,
     "Some of Adam's children listened to the angel. Some loved the "
     "counterfeit. And that split, right down the middle of the first "
     "family, is the war — running through every family since."),
    ("n10", NARRATOR,
     "But keep the headline. God did not wait one generation to preach "
     "Christ. The gospel came to Adam whole, immediate, and free. Nobody "
     "in the history of this world was ever born too early for Jesus."),
    ("n11", NARRATOR,
     "So when someone tells you the gospel started two thousand years "
     "ago — or that God leaves His children in the dark — tell them "
     "about the first altar. He taught the first family. He will "
     "certainly teach yours."),
]

CARD_SEG = ("card", NARRATOR,
            "The gospel is older than the world. And nobody was born too "
            "early for Christ.")

CARD_TEXT = ("Nobody was born too early\n"
             "for Christ.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Nine — The First Gospel")

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
        "The first altar at dawn: a simple platform of unhewn stacked "
        "stones on a bare hilltop above the wild valley, morning mist "
        "below, the light just reaching the stones — empty, waiting, "
        "already sacred. No people yet.",
        "a rough unhewn stone altar alone on a dawn hilltop over mist",
        "carvings, tools, fire yet, people, drawn rays",
        wide=True)),
    ("p02", "n2", _p(
        "The family that kept praying: Adam and Eve kneel side by side "
        "outside their timber-and-stone dwelling in evening light, "
        "heads bowed, his hand over hers on the earth between them — "
        "seen from the side at a respectful distance, smoke from a "
        "cook-fire rising thin behind the roofline.",
        "the first couple kneeling side by side at evening, his hand "
        "over hers on the ground, side view",
        "faces to camera, tears, an altar in this frame",
        locks=["ADAM", "EVE"])),
    ("p03", ("n2", 0.55), _p(
        "Heaven answers: both faces lift together — Adam's and Eve's "
        "profiles caught at the instant of hearing, eyes opening "
        "toward the evening sky, wonder without fear — the wind "
        "moving her long hair and the fire's smoke sideways in the "
        "same gust.",
        "two lifted listening profiles, wind moving hair and smoke "
        "the same direction, wonder",
        "any figure in the sky, faces to camera, drawn light",
        locks=["ADAM", "EVE"])),
    ("p04", "s1", _p(
        "The angel's question: beside the hilltop altar a radiant "
        "MESSENGER — a glorified man in a bright white robe, both feet "
        "planted on the ground — stands facing Adam across the "
        "smoking altar stones, mid-question with one open hand toward "
        "the offering; Adam faces him in worn work-clothes, straight-"
        "backed, honest. Both in profile to the camera, morning light "
        "hard and clean on the hilltop.",
        "a wingless white-robed messenger and Adam in facing profiles "
        "across a smoking stone altar",
        "wings, halo, hovering, Adam kneeling in fear, faces to "
        "camera",
        locks=["ADAM"])),
    ("p05", ("s1", 0.62), _p(
        "The honest answer: Adam's face close in three-quarter, "
        "mid-sentence — the plain unashamed look of a man saying I "
        "don't know, but He commanded — weathered features open, no "
        "performance, morning light on the honesty itself.",
        "Adam's close three-quarter mid-answer, plain unashamed "
        "honesty",
        "his eyes on the lens, shame, tears, the angel in frame",
        locks=["ADAM"])),
    ("p06", "s2", _p(
        "The similitude lands: sharp in the foreground, the white "
        "firstling lamb lying bound and still upon the altar wood; "
        "soft beyond it, Adam's face coming up with widening eyes as "
        "the meaning arrives — the lamb and the understanding in one "
        "frame, the smoke rising thin and straight between them.",
        "the bound white lamb sharp on the altar, Adam's soft-focus "
        "widening understanding beyond",
        "blood, knife, distress in the lamb, faces to camera",
        locks=["ADAM"])),
    ("p07", "n4", _p(
        "The first congregation: the family kneels in a half-circle "
        "before the hilltop altar at full morning — Adam, Eve, and "
        "seven children from grown sons to a toddler on a sister's "
        "hip — all seen from behind and beside, every head toward "
        "the straight-rising smoke, the wild world enormous beyond "
        "the hill.",
        "the whole first family kneeling from behind before the "
        "altar's straight smoke, wild world beyond",
        "faces to camera, buildings, drawn rays",
        wide=True, locks=["ADAM", "EVE"])),
    ("p08", ("n4", 0.55), _p(
        "Eve the teacher: firelight inside the dwelling — Eve "
        "mid-story with both hands shaping something in the air, "
        "four children cross-legged before her, the nearest boy's "
        "mouth open, every young gaze on her hands — the gospel "
        "passing to the second generation in the oldest classroom "
        "there is.",
        "Eve mid-story by firelight, hands shaping the air, rapt "
        "children before her",
        "faces to camera, scrolls, books, sadness",
        locks=["EVE"])),
    ("p09", "s3", _p(
        "The first baptism: Adam BURSTS up out of a clear river "
        "pool at dawn — caught at the exact instant of emerging, "
        "water sheeting off his head and beard, arms rising, face "
        "heavenward with closed eyes — alone in the water, carried "
        "there by a power the frame does not show. The pool's far "
        "bank is stone and young green; the light is first gold.",
        "Adam mid-burst from the river pool, water sheeting, face "
        "heavenward, alone in frame",
        "an officiator visible, swimmers' strokes, his eyes on "
        "the lens, cold colours",
        locks=["ADAM"])),
    ("p10", ("s3", 0.6), _p(
        "New: Adam stands waist-deep and still in the pool, "
        "streaming, his face carrying the unmistakable look of a "
        "man made new — and on the near bank Eve stands with both "
        "hands pressed over her mouth, joy running over. Both in "
        "profile, dawn gold on the water between them.",
        "Adam waist-deep made-new and Eve on the bank with hands "
        "over her mouth, joy, dawn water between",
        "faces to camera, towels, crowd, tears of grief",
        locks=["ADAM", "EVE"])),
    ("p11", "n5", _p(
        "The same gospel, today: a river baptism in the present "
        "day — a man in white being lowered back toward the water "
        "by a baptizer's braced arms, both figures seen from "
        "behind and beside at a distance, a small family group "
        "watching from the grassy bank, morning light broad on "
        "the river. Faces away or in profile; timeless.",
        "a present-day river baptism from behind-beside, braced "
        "arms mid-lowering, small family watching from the bank",
        "faces to camera, church buildings, signage, brand marks",
        era="modern", wide=True)),
    ("p12", "n6", _p(
        "The turn: the family camp at dusk — and at its edge, "
        "past the last tent, one cold unlit fire-ring of blackened "
        "stones where nobody sits, the warm lit fires and moving "
        "figures soft in the background. Something has started to "
        "pull at the edges — and the cold ring sits empty.",
        "a cold unlit fire-ring at the camp's dusk edge, warm "
        "living fires soft beyond",
        "any figure at the cold ring, smoke from it, faces "
        "readable",
        devil=True)),
    ("p13", "d1", _p(
        "The counterfeit sermon: night — a loose crowd of Adam's "
        "younger kin gathered at the camp's edge, every face lit "
        "faintly by the distant family fires BEHIND them while "
        "they stand turned the other way, listening intently "
        "toward the empty darkness beyond the camp — heads "
        "tilted, some nodding slowly, fascination dulling their "
        "faces. The darkness they attend to is EMPTY: open night, "
        "no speaker, no shape.",
        "a night crowd turned away from the warm fires, listening "
        "raptly toward empty open darkness",
        "ANY figure, silhouette or shape in the darkness they "
        "face; anyone facing the lens; torches among them",
        devil=True)),
    ("p14", "n7", _p(
        "Doubt as doctrine: one strong young man stands with his "
        "back deliberately turned to the distant altar hill — "
        "arms folded hard, jaw set, seen in profile against the "
        "morning light that still reaches him from the hill he "
        "refuses — the first posture of a very long tradition.",
        "a young man in profile, arms folded, back turned to the "
        "distant lit altar hill",
        "sneering, his eyes on the lens, weapons, darkness on "
        "him",
        )),
    ("p15", "n9", _p(
        "The imitation church: a big night feast-fire down in the "
        "valley — figures laughing too loudly around it, wine "
        "skins lifted, a whole roast dripping, someone dancing "
        "with a thrown-back head — appetite worshipped, seen from "
        "just outside the fire's ring so every face is toward the "
        "flames or each other, none toward the lens. Shot kept "
        "modest: revelry, not depravity.",
        "a loud firelit feast of appetite — lifted wine skins, "
        "dripping roast, thrown-back laughter — none facing the "
        "lens",
        "nudity, violence, anyone facing the lens, modern "
        "objects",
        )),
    ("p16", ("n9", 0.55), _p(
        "The split: at a fork in the camp trail at dusk, two "
        "grown brothers part — one walking up-trail toward the "
        "altar hill's evening light, one walking down toward the "
        "feast-fire's flicker in the valley — both seen from "
        "directly behind at the fork, their shoulders already a "
        "world apart. The camera stays low between the two "
        "paths.",
        "two brothers from behind parting at a fork — one toward "
        "the lit hill, one toward the valley fire-flicker",
        "faces or profiles, weapons, anyone else in frame",
        wide=True)),
    ("p17", "n10", _p(
        "The headline restated: the altar hill at full sunrise — "
        "the family gathered close around the burning offering, "
        "the smoke rising straight into a sky gone entirely "
        "gold, every figure from behind or profile in the "
        "half-circle — the first church on earth, complete and "
        "glorious and small against the enormous morning.",
        "the family half-circle around the burning altar under a "
        "full-gold sunrise, smoke straight up",
        "faces to camera, drawn rays, any darkness",
        wide=True, locks=["ADAM", "EVE"])),
    ("p18", ("n10", 0.55), _p(
        "The next generation reaches: close — a baby in Eve's "
        "arms at the altar's edge, one tiny arm stretched out "
        "toward the bright smoke and morning light, Eve's cheek "
        "against the small head, both faces soft in profile.",
        "a baby in Eve's arms reaching one arm toward altar "
        "smoke and light, profiles",
        "faces to camera, distress, harsh light on the child",
        locks=["EVE"])),
    ("p19", "n11", _p(
        "Your family's turn: a present-day family — parents and "
        "two kids — leans over open scriptures together at a "
        "kitchen table in warm evening lamplight, every face "
        "turned down toward the pages, a small child's finger on "
        "a line — seen from across the table at seated height. "
        "The same gospel, still arriving at tables.",
        "a modern family bent together over open scriptures in "
        "lamplight, a child's finger on the page",
        "readable text on the page, faces to camera, screens, "
        "brand marks",
        era="modern")),
    ("p20", ("n11", 0.7), _p(
        "Peace over the first altar: the hilltop at early light, "
        "empty again — the stones dark with old fire, a pair of "
        "doves lifting off into the brightening sky, mist "
        "thinning in the valley below. What began here has never "
        "stopped.",
        "the empty ancient altar at early light with two doves "
        "lifting into the sky",
        "people, fire burning, drawn rays, text",
        )),
]
