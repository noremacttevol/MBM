#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 28: Hands on Heads.

Authority returns the only way it can — by the laying on of hands, from
the last men who held it: John the Baptist at the river, then Peter,
James and John. The apostasy's central theft, reversed by resurrected
messengers. Anchors: D&C 13; JS—History 1:68-72; Hebrews 5:4.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 328
NUM = 28
SLUG = "hands-on-heads"
TITLE = "Hands on Heads"
META = "D&C 13 · JS—History 1"

SEGMENTS = [
    ("n1", NARRATOR,
     "A book can carry testimony. It cannot carry keys. For those, "
     "heaven had to send hands — and this episode is about whose hands "
     "they sent."),
    ("n2", NARRATOR,
     "Remember the rule, older than the apostasy itself:"),
    ("s1", SCRIPTURE,
     "And no man taketh this honour unto himself, but he that is called "
     "of God, as was Aaron."),
    ("n3", NARRATOR,
     "Called of God, as was Aaron — and Aaron was called through a "
     "prophet, by the laying on of hands. Authority is never seized, "
     "studied into, or voted in. It is CONFERRED — hand to head, in an "
     "unbroken line. Which was exactly the line the apostasy cut."),
    ("n4", NARRATOR,
     "May fifteenth, eighteen twenty-nine. Joseph and his scribe Oliver, "
     "translating the book, hit a question about baptism — so they "
     "walked into the woods by the Susquehanna river and asked."),
    ("n5", NARRATOR,
     "And a messenger descended in light. He said his name was John — "
     "the same John who baptized Jesus in the Jordan. Herod's men had "
     "beheaded him eighteen centuries earlier. Death, it turns out, "
     "does not disqualify God's couriers. He laid his hands on their "
     "heads:"),
    ("s2", SCRIPTURE,
     "Upon you my fellow servants, in the name of Messiah, I confer the "
     "Priesthood of Aaron, which holds the keys of the ministering of "
     "angels, and of the gospel of repentance, and of baptism by "
     "immersion for the remission of sins."),
    ("n6", NARRATOR,
     "The Priesthood of Aaron — back on earth, from the hands of its "
     "last mortal holder. And the first use was immediate: Joseph and "
     "Oliver walked into the river and baptized each other — the "
     "ordinance restored to its full, buried-and-raised form."),
    ("n7", NARRATOR,
     "But Aaron's priesthood is the lesser of two. The higher — the "
     "Melchizedek Priesthood, the authority of the apostleship itself — "
     "required the men who held its keys last. And weeks later, they "
     "came: Peter. James. And John."),
    ("n8", NARRATOR,
     "Let that land. The fisherman crucified in Rome. The apostle "
     "Herod put to the sword. The beloved disciple. The First "
     "Presidency of the ancient church — sent back, to lay their hands "
     "on two young men's heads and return what the empire thought it "
     "had buried with them."),
    ("n9", NARRATOR,
     "This is the apostasy running in reverse. The devil's whole long "
     "theft assumed one thing: that dead men stay gone. But he plays "
     "against a God who raises the dead — and you cannot permanently "
     "steal keys from a Kingdom whose keyholders can be sent back."),
    ("n10", NARRATOR,
     "Understand what this claim means, and how easy it would be to "
     "check from heaven's side: either John the Baptist stood in those "
     "woods, or he did not. Either Peter, James and John returned, or "
     "they did not. The Restoration never asks you to admire it as a "
     "metaphor. It states events — and invites you to ask the God who "
     "was there."),
    ("n11", NARRATOR,
     "Sixteen centuries earlier, a boy watched the last apostle die and "
     "the keys leave the world. On a May morning by an American river, "
     "the line was spliced whole again — hand to head, exactly the way "
     "it was cut. The famine did not just end. It ended in order."),
]

CARD_SEG = ("card", NARRATOR,
            "You cannot steal keys from a Kingdom whose keyholders come "
            "back. Hand to head, the line was spliced whole.")

CARD_TEXT = ("The line was spliced whole.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Twenty-Eight — Hands on Heads")

SPOKEN = {"Susquehanna": "suss kwuh HAN uh",
          "Melchizedek": "mel KIZZ eh deck"}

OLIVER = (
    "OLIVER LOCK: the same man in every picture — Oliver Cowdery at "
    "twenty-two: slight scholarly build, dark neat hair, clean-shaven "
    "narrow earnest face, small round spectacles sometimes in hand, "
    "schoolteacher's dark coat over homespun. Quick-eyed, devoted. No "
    "halo, no glow.")

BAPTIST = (
    "JOHN-BAPTIST LOCK: the same man in every picture — John the "
    "Baptist glorified: lean and weather-forged, deep tan skin, thick "
    "untamed dark hair and beard remembered from the wilderness now "
    "washed with light, a robe of exquisite whiteness where once was "
    "camel hair, feet bare in the air. Fierce joy, a herald's bearing. "
    "No wings, no halo, no aura outline.")

LOCKS = {"OLIVER-C": OLIVER, "JOHN-B-GP": BAPTIST}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="america-1820")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "What a book cannot carry: the thick new book lies closed on a "
        "plain table beside a cast-iron door-lock with NO key in it — "
        "morning light across both objects, the keyhole a small dark "
        "waiting mouth. Testimony and the still-missing thing, side by "
        "side. No people.",
        "the closed thick book beside a keyless iron lock, keyhole "
        "dark and waiting, morning light",
        "a key present, readable title, hands",
        )),
    ("p02", "s1", _p(
        "As was Aaron: ancient flashback — Moses' hands pressed on "
        "kneeling Aaron's head before the tabernacle hangings, oil "
        "vessel beside them, Aaron's eyes closed under the weight of "
        "the conferral — the original pattern, hand to head, in warm "
        "lamp-and-daylight. Seen from beside the two men.",
        "Moses' hands on kneeling Aaron's head by the tabernacle "
        "hangings, oil vessel near",
        "crowds, halo, faces to camera",
        era="ancient", locks=["MOSES-GP"])),
    ("p03", "n3", _p(
        "The line, cut: a heavy ship's rope pulled taut across the "
        "frame — SEVERED in the middle, the two ends frayed a "
        "hand-span apart, unable to reach each other, grey light on "
        "the parted fibres. The apostasy in one object. No people.",
        "a taut heavy rope severed mid-frame, frayed ends a "
        "hand-span apart",
        "knives, hands, ships, text",
        )),
    ("p04", "n4", _p(
        "The question that walked: Joseph and Oliver walking away "
        "from a small cabin into spring woods, Joseph a stride "
        "ahead, Oliver still carrying his quill absent-mindedly — "
        "both from behind on the leaf-lit path toward the unseen "
        "river, two men taking a translation problem to the only "
        "Authority left.",
        "Joseph and Oliver from behind on a spring woods path, "
        "quill still in Oliver's hand",
        "faces, the river yet, buildings beyond the cabin",
        locks=["JOSEPH-SMITH", "OLIVER-C"])),
    ("p05", "n5", _p(
        "The herald descends: in a river-bank clearing the two young "
        "men kneel, faces lifted — and above them in a column of "
        "morning-bright air stands the glorified Baptist, bare feet "
        "off the ground, wilderness-forged face blazing with a "
        "herald's joy, his hands already reaching toward their "
        "heads. The Jordan's voice, at the Susquehanna.",
        "the glorified Baptist in bright air above two kneeling "
        "young men, hands reaching toward their heads",
        "wings, halo, aura outline, feet on ground, faces to "
        "lens",
        locks=["JOHN-B-GP", "JOSEPH-SMITH", "OLIVER-C"])),
    ("p06", "s2", _p(
        "THE CONFERRAL: close on the moment itself — the "
        "messenger's two strong hands resting FULL on Joseph's "
        "bowed head, Oliver kneeling beside awaiting his turn, "
        "Joseph's face beneath the hands wet-eyed and still — "
        "authority flowing the only way it ever has, hand to head. "
        "The frame of the episode.",
        "glorified hands resting full on Joseph's bowed head, "
        "Oliver awaiting beside, wet-eyed stillness",
        "light beams from the hands, halo, faces to lens",
        locks=["JOHN-B-GP", "JOSEPH-SMITH", "OLIVER-C"])),
    ("p07", "n6", _p(
        "First use, immediate: in the Susquehanna's bright shallows, "
        "Joseph lowers Oliver fully backward beneath the surface — "
        "the water closing over the scholar's chest, Joseph's "
        "braced arm and called-of-God grip doing what a font of "
        "sprinkled drops never could — spring current combing "
        "around their legs, morning on the water.",
        "Joseph lowering Oliver fully backward beneath the bright "
        "river surface, braced grip, spring current",
        "crowds, doves, halo, faces to lens",
        locks=["JOSEPH-SMITH", "OLIVER-C"])),
    ("p08", ("n6", 0.6), _p(
        "Up out of the water: Oliver BURSTS back up mid-gasp, "
        "water sheeting off his dark hair, his narrow scholar's "
        "face split with disbelieving joy — Joseph's steadying "
        "grip still on his forearm, both men soaked and laughing "
        "toward each other in the current. The ordinance, home in "
        "its river.",
        "Oliver bursting up soaked and joy-split, Joseph's grip "
        "on his forearm, both laughing toward each other",
        "faces to lens, crowds, towels, halo",
        locks=["JOSEPH-SMITH", "OLIVER-C"])),
    ("p09", "n7", _p(
        "The higher keys required higher men: dusk on a wilderness "
        "road between Harmony and Colesville — Joseph and Oliver "
        "walking from behind — and ahead of them on the darkening "
        "track, a growing brightness around the bend that neither "
        "has seen yet, lighting the underside of the trees. "
        "Someone is waiting on the road.",
        "two walkers from behind on a dusk track with unexplained "
        "brightness growing around the bend ahead",
        "the messengers visible yet, lanterns, faces",
        locks=["JOSEPH-SMITH", "OLIVER-C"])),
    ("p10", "n8", _p(
        "Peter, James and John: THREE glorified men stand in the "
        "bright air of the road's bend — the broad grey-bearded "
        "fisherman at the centre with keys' authority in his "
        "bearing, the sword-slain apostle at his right, the "
        "beloved disciple at his left — three faces of blazing "
        "calm above the two kneeling young men at the frame's "
        "bottom edge. The First Presidency of the ancient church, "
        "reporting back to work.",
        "three distinct glorified men in bright air above two "
        "kneeling young men — broad fisherman centred, all calm "
        "blazing",
        "wings, halos, aura outlines, feet on ground, faces to "
        "lens",
        locks=["JOSEPH-SMITH", "OLIVER-C"])),
    ("p11", ("n8", 0.6), _p(
        "The apostleship returns: six glorified hands rest "
        "together on the two bowed young heads — the fisherman's "
        "scarred knuckles foremost — ordination at the highest "
        "register earth knows, on a dirt road in the dark, with "
        "the light of the messengers washing the kneeling men's "
        "homespun gold.",
        "six glorified hands on two bowed heads, scarred "
        "knuckles foremost, homespun washed gold",
        "faces of the kneeling men, beams, halo",
        )),
    ("p12", "n9", _p(
        "The theft, reversed: the severed rope from before — now "
        "SPLICED: the two frayed ends woven back through each "
        "other in a tight, seamanlike long-splice, the join "
        "thicker and stronger than the line around it, morning "
        "light on the mended fibres. No people. The episode's "
        "object, healed.",
        "the severed rope now long-spliced whole, the join "
        "thicker than the line, morning light",
        "knives, hands, fray remaining, text",
        )),
    ("p13", "n10", _p(
        "Checkable, either way: the river-bank clearing today — "
        "spring woods, bright shallows, an utterly ordinary "
        "beautiful stretch of the Susquehanna where either "
        "something happened or it did not — no marker in frame, "
        "no shrine, just the place and the light and the "
        "question. No people.",
        "the ordinary bright river-bank clearing, unmarked, "
        "holding its question",
        "monuments, plaques, figures, text",
        )),
    ("p14", "n11", _p(
        "Spliced in order: the two young men walk back out of "
        "the woods toward the cabin in full morning — soaked "
        "hems, springing steps, Oliver's hand on Joseph's "
        "shoulder mid-laugh — seen from behind, the path bright "
        "ahead of them, carrying between them everything the "
        "famine lost. The line, walking home whole.",
        "the two from behind walking home soak-hemmed and "
        "laughing, hand on shoulder, bright path",
        "faces, crowds, the messengers, halo",
        locks=["JOSEPH-SMITH", "OLIVER-C"])),
    ("p15", ("n11", 0.6), _p(
        "The keyhole, answered: the iron lock from the opening "
        "frame — and now a hand-forged KEY seated home in its "
        "keyhole, turned a quarter, the bolt caught mid-throw — "
        "morning light down the shank. Beside it, the thick "
        "book still lies closed, its work done. No people.",
        "a forged key seated and quarter-turned in the iron "
        "lock, bolt mid-throw, the book beside",
        "hands, readable title, chains",
        )),
]
