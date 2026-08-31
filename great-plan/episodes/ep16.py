#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 16: The Other Sheep.

Six hundred years before Bethlehem, God plants a second witness nation on
the far side of the world — because the devil corrupts records, and God
plants spares. Jesus's own line: other sheep I have.
Anchors: 1 Nephi 1-2; 2 Nephi 25:26; 2 Nephi 29:8; John 10:16.

Voice note: 2 Nephi 29:8 is the Lord — Jehovah — speaking, and Jehovah IS
the premortal Jesus, so it carries the JESUS voice and red caption. The
film quietly teaches that identity by the casting itself.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 316
NUM = 16
SLUG = "other-sheep"
TITLE = "The Other Sheep"
META = "1 Nephi 1-2 · John 10"

SEGMENTS = [
    ("n1", NARRATOR,
     "Six hundred years before Bethlehem, God did something nobody in "
     "Jerusalem knew about. It is the reason a second book of scripture "
     "exists."),
    ("n2", NARRATOR,
     "Jerusalem, six hundred years before Christ. Prophets warning of "
     "destruction; a city refusing to hear. One of those prophets was a "
     "wealthy man named Lehi — and the city planned to kill him."),
    ("n3", NARRATOR,
     "So God moved him. Family, tents, seeds, everything — out of the "
     "city, into the wilderness, and at last across the ocean to a new "
     "promised land on the far side of the world."),
    ("n4", NARRATOR,
     "Now think about what God was actually doing. The devil's long game "
     "was corrupting the RECORD — bending scripture through hostile "
     "centuries until the plain things went missing. So God quietly "
     "planted a second witness where the corrupters would never find "
     "it."),
    ("j1", JESUS,
     "Know ye not that the testimony of two nations is a witness unto "
     "you that I am God, that I remember one nation like unto another?"),
    ("n5", NARRATOR,
     "The testimony of two nations. Two records, two hemispheres, one "
     "God. While the old world's record passed through hostile hands, "
     "this one would pass prophet to prophet — and then be buried, "
     "whole, for the exact century it would be needed."),
    ("n6", NARRATOR,
     "Lehi's family grew into nations, and their thousand-year story "
     "became the Book of Mormon. And the constant thread through all of "
     "it: they knew Christ by name, centuries before the manger."),
    ("s1", SCRIPTURE,
     "And we talk of Christ, we rejoice in Christ, we preach of Christ, "
     "we prophesy of Christ, and we write according to our prophecies, "
     "that our children may know to what source they may look for a "
     "remission of their sins."),
    ("n7", NARRATOR,
     "Written six hundred years before Bethlehem, on the other side of "
     "the planet. That is not luck. That is a Father making certain no "
     "hemisphere and no century would be left without the testimony of "
     "His Son."),
    ("n8", NARRATOR,
     "And Jesus himself told the Jews about them — in one sentence they "
     "did not understand:"),
    ("j2", JESUS,
     "And other sheep I have, which are not of this fold: them also I "
     "must bring, and they shall hear my voice; and there shall be one "
     "fold, and one shepherd."),
    ("n9", NARRATOR,
     "Other sheep. That was never a metaphor. It was an address. And "
     "after his resurrection, he kept that promise in person — but that "
     "is episode twenty."),
    ("n10", NARRATOR,
     "Here is what the other sheep mean for you. God remembers nations "
     "nobody else remembers. He writes to children nobody else writes "
     "to. If you have ever felt like a forgotten branch of the family — "
     "off the main road, outside the famous story — you are exactly the "
     "kind of people He plants witnesses for."),
    ("n11", NARRATOR,
     "The devil corrupts records. God plants spares. And one of His "
     "spares was buried in a hillside — with your century's name on "
     "it."),
]

CARD_SEG = ("card", NARRATOR,
            "God remembers the sheep nobody else counts. He wrote a "
            "second witness to prove it.")

CARD_TEXT = ("He remembers the sheep\n"
             "nobody else counts.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Sixteen — The Other Sheep")

SPOKEN = {"Lehi": "LEE high"}

LEHI = (
    "LEHI LOCK: the same man in every picture — a wealthy Hebrew "
    "merchant-prophet in his sixties: warm olive skin, a full "
    "silver-streaked dark beard, silver-threaded dark hair under a fine "
    "striped head cloth, travel robes of quality blue-grey wool now "
    "road-worn, carrying himself like a man who left everything without "
    "looking back. No halo, no glow.")

LOCKS = {"LEHI": LEHI}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="ancient")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "Jerusalem at dusk, six centuries before Christ: the walled "
        "city on its ridges under a bruised gold sky — the temple "
        "court's lamps beginning to burn, smoke of evening fires, the "
        "Kidron valley falling into shadow below the walls. Beautiful, "
        "doomed, unaware. No close figures.",
        "walled Jerusalem on its ridges at bruised-gold dusk, temple "
        "lamps beginning",
        "modern skyline, banners, armies, text",
        wide=True)),
    ("p02", "n2", _p(
        "The unwanted warning: Lehi stands on the steps inside a city "
        "gate, one arm raised mid-warning — and the market crowd "
        "turns on him: fists clenched, faces twisted with anger, one "
        "man stooping for a stone, two elders turning their backs — "
        "every hostile face aimed at the prophet, none at the camera, "
        "which shoots past the crowd's shoulders.",
        "Lehi mid-warning on the gate steps, a turning hostile crowd "
        "— clenched fists, one man stooping for a stone",
        "stones thrown, blood, faces to camera",
        wide=True, locks=["LEHI"])),
    ("p03", "n3", _p(
        "Everything, left: the family caravan leaves at first light — "
        "laden camels, sons driving pack animals, a wife wrapped "
        "against the dawn cold — all seen from behind as the road "
        "bends away from the city walls into the wilderness hills, "
        "nobody looking back but one youngest son, whose head is "
        "half-turned toward home.",
        "a family caravan from behind leaving city walls into dawn "
        "hills, one boy's head half-turned back",
        "faces to camera, soldiers pursuing, tears shown",
        wide=True, locks=["LEHI"])),
    ("p04", ("n3", 0.5), _p(
        "The crossing: a hand-built wooden ship — curved timbers, "
        "single broad sail — running before the wind on a vast open "
        "ocean, spray off the bow, tiny figures working the deck, no "
        "land in any direction. Eight years of desert behind them; "
        "half a planet of water ahead.",
        "a hand-built single-sail wooden ship running on open ocean, "
        "tiny deck figures, no land",
        "modern rigging, other ships, storms, faces",
        wide=True)),
    ("p05", ("n3", 0.8), _p(
        "Landfall: the family kneels on a green new-world shore just "
        "above the tide line — a dozen figures from behind, heads "
        "bowed toward the forested hills of the promised land, the "
        "beached ship's prow at the frame's edge, morning light "
        "running down the water behind them.",
        "a family kneeling from behind on a green new-world shore, "
        "ship's prow at the edge, morning light",
        "faces to camera, buildings, natives, banners",
        wide=True, locks=["LEHI"])),
    ("p06", "n4", _p(
        "The spare copy begins: by lamplight, strong young hands "
        "engrave characters onto a thin metal plate with a bronze "
        "stylus — the finished plates stacked and bound with rings "
        "beside the work, the strokes fine and completely "
        "unreadable, the lamp flame steady. A record the corrupters "
        "will never touch.",
        "hands engraving an unreadable metal plate by lamplight, "
        "ring-bound stack beside",
        "readable characters, faces, gold treasure look",
        )),
    ("p07", "j1", _p(
        "Two witnesses: on a plain wooden table, side by side in "
        "raking lamplight — a worn leather scroll-roll, cracked and "
        "beloved, and a stack of thin bound metal plates, gleaming "
        "quietly — two records, two roads through history, one "
        "testimony. Nothing else in frame; all writing soft and "
        "unreadable.",
        "a worn scroll and a bound metal-plate stack side by side "
        "in raking lamplight",
        "readable text, hands, jewels, coins",
        )),
    ("p08", "n5", _p(
        "Prophet to prophet: two pairs of hands in warm light — an "
        "aged spotted pair passing the ring-bound plates DOWN into "
        "a younger steadier pair rising to receive them — the "
        "exchange caught at the moment both pairs hold the record "
        "together. The relay, in metal.",
        "old hands passing ring-bound plates into young hands, "
        "both holding at the exchange moment",
        "faces, readable text, ceremony crowds",
        )),
    ("p09", "n6", _p(
        "A thousand years in one man: an aged warrior-historian "
        "seated at a camp table by night — battle-scarred armor "
        "still on his shoulders, white beard over the breastplate — "
        "engraving steadily onto a plate while watch-fires burn "
        "soft in the dark behind him. A general, saving the story "
        "while the world falls.",
        "an old armored historian engraving plates by night camp "
        "firelight",
        "readable text, battle in progress, his eyes on lens",
        )),
    ("p10", "s1", _p(
        "We talk of Christ, centuries early: a new-world family at "
        "evening lamp — the father's hand lifted mid-teaching "
        "toward the small carved wooden likeness of nothing at "
        "all — pointing UPWARD, open-palmed — the mother with the "
        "youngest on her lap, three children rapt, every face on "
        "the father or the upward hand. Believers in a Christ "
        "still six centuries away.",
        "a lamplit new-world family, father's open hand lifted "
        "upward mid-teaching, children rapt",
        "idols, readable text, faces to camera",
        )),
    ("p11", "n7", _p(
        "No hemisphere left out: a new-world temple at dawn — "
        "clean-lined stone terraces rising from jungle-green "
        "hills, morning smoke of offerings, white-clad figures "
        "small on its stairs — the same worship, an ocean away "
        "from Jerusalem. Distinct architecture: stepped stone, "
        "not Judean.",
        "a stepped new-world stone temple at dawn with small "
        "white-clad figures and offering smoke",
        "Old-world architecture, idols, crowds close, text",
        wide=True)),
    ("p12", "n8", _p(
        "One sentence they did not understand: Jesus teaching in a "
        "Jerusalem courtyard — seated among listeners on low "
        "steps, mid-word, his hand open toward them — faces "
        "puzzled at something just said, an elder frowning, a "
        "young man leaning forward — every face on the teacher, "
        "none on the camera.",
        "Jesus teaching on courtyard steps, open hand, puzzled "
        "leaning listeners",
        "faces to camera, halo, scrolls readable",
        era="first-century", jesus=True, ref=True, wide=True)),
    ("p13", "j2", _p(
        "Other sheep I have: Jesus's face close in three-quarter — "
        "the gaze gone long and warm past the camera's left, over "
        "the heads of his hearers, over the sea, to a people no "
        "one else in the courtyard can see — the look of a "
        "shepherd counting sheep beyond the horizon.",
        "Jesus's close three-quarter face with a long warm gaze "
        "past the lens toward something far beyond",
        "his eyes on the lens, halo, sadness, crowd sharp",
        era="first-century", jesus=True, ref=True)),
    ("p14", "n9", _p(
        "The promise, waiting: from a new-world headland, the "
        "open ocean at dawn — the water's horizon clean and "
        "empty, light building behind far clouds, surf patient "
        "on the rocks below. The direction the Shepherd will "
        "come from. No figures.",
        "an empty dawn ocean horizon from a green new-world "
        "headland, building light",
        "ships, figures, birds in flocks, text",
        wide=True)),
    ("p15", "n10", _p(
        "The forgotten branch: in the present day, far out on "
        "dark evening plains, one small white chapel with its "
        "windows lit — a single warm point in an immensity of "
        "dusk grass and sky, one pickup truck parked outside. "
        "Off every main road. Fully remembered.",
        "one small lit chapel alone on vast dusk plains, single "
        "truck outside",
        "signage readable, crowds, storm, brand marks",
        era="modern", wide=True)),
    ("p16", ("n10", 0.55), _p(
        "He writes to them: close on weathered working hands "
        "holding a small thick well-used book open on a kitchen "
        "table — cover plain and unreadable, pages soft-edged "
        "with years, morning light across the hands and paper. "
        "A letter from God to people off the main road.",
        "weathered hands holding a small thick worn book open "
        "in morning light, all print unreadable",
        "readable title or text, faces, jewellery",
        era="modern")),
    ("p17", "n11", _p(
        "The spare, planted: strong hands lower the ring-bound "
        "plate stack into a stone box set in dark hillside "
        "earth — the box's fitted lid leaning ready, tree roots "
        "at the cut's edge, the metal catching one last gleam "
        "of grey daylight before the ground closes over it. "
        "Buried mail, addressed four centuries ahead.",
        "hands lowering bound plates into a fitted stone box in "
        "hillside earth, lid ready",
        "faces, treasure hoard look, readable text",
        )),
    ("p18", ("n11", 0.7), _p(
        "The hill keeps the secret: the wooded drumlin hill at "
        "sunset — the same quiet hill the famine episode ended "
        "on — its canopy gone amber, the young world's evening "
        "settling over the buried witness. Patience, again. No "
        "people.",
        "the wooded drumlin hill in amber sunset, quiet and "
        "unmarked",
        "figures, monuments, paths, text",
        wide=True, era="america-1820")),
]
