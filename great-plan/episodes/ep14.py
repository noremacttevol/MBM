#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 14: Face to Face.

Moses learns the two treasures the famine later starved out of the world:
God has a face (Ex 33:11), and men have a title (Moses 1:13). Includes the
mission statement (Moses 1:39) and the devil's confrontation — a voice
against a man who knows who he is.
Anchors: Exodus 33:11; Moses 1:12-20, 39.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 314
NUM = 14
SLUG = "face-to-face"
TITLE = "Face to Face"
META = "Exodus 33 · Moses 1"

SEGMENTS = [
    ("n1", NARRATOR,
     "Fifteen hundred years before Christ, God pulled a shepherd off a "
     "mountainside and showed him who He is. What Moses learned up there "
     "is everything the famine would later starve out of the world."),
    ("n2", NARRATOR,
     "You know the story's shape. A bush that burned and was not "
     "consumed. Ten plagues. A sea standing on end, and a slave nation "
     "walking out of Egypt on dry ground."),
    ("s1", SCRIPTURE,
     "And the Lord spake unto Moses face to face, as a man speaketh unto "
     "his friend."),
    ("n3", NARRATOR,
     "Face to face. As a man speaks to his friend. Not a force. Not an "
     "abstraction. A Person — knowable, present, and shockingly "
     "personal."),
    ("n4", NARRATOR,
     "And in vision, God told Moses what all of it is FOR. One sentence. "
     "The mission statement of everything:"),
    ("g1", FATHER,
     "For behold, this is my work and my glory — to bring to pass the "
     "immortality and eternal life of man."),
    ("n5", NARRATOR,
     "His work and His glory — is your life. Not His ego. Not His "
     "applause. When someone asks why God wants worship, there is the "
     "answer: His glory is His children rising. Worship is scaffolding "
     "for us. It was never applause for Him."),
    ("n6", NARRATOR,
     "And Moses learned one more thing on that mountain. Because after "
     "the glory withdrew, another voice showed up."),
    ("d1", DEVIL,
     "Moses, son of man, worship me."),
    ("n7", NARRATOR,
     "Son of man. Hear the insult — God had just called him My Son. The "
     "devil's first move is always to shrink your title. Now watch what "
     "a man who knows who he is does with that:"),
    ("s2", SCRIPTURE,
     "Who art thou? For behold, I am a son of God, in the similitude of "
     "his Only Begotten; and where is thy glory, that I should worship "
     "thee?"),
    ("n8", NARRATOR,
     "Who art thou — for I am a son of God. That is the whole exchange. "
     "A man who has seen God's face and knows his own name cannot be "
     "bluffed. The voice raged and the ground shook — and Moses ended it "
     "with one sentence:"),
    ("s3", SCRIPTURE,
     "Depart from me, Satan, for this one God only will I worship, which "
     "is the God of glory."),
    ("n9", NARRATOR,
     "And he departed. He always does, eventually, before a child of God "
     "standing on their identity. That is not a Moses-only trick. That "
     "is the family defense."),
    ("n10", NARRATOR,
     "Israel walked out of Egypt with that God — fire by night, bread "
     "from the sky, water from rock — and still forgot Him within weeks, "
     "dancing around a golden calf. And God's answer, for the next "
     "thousand years? He kept sending. But that is the next episode."),
    ("n11", NARRATOR,
     "For now, keep Moses' two treasures. God has a face. And you have a "
     "title: child of God. His whole work and glory is raising you — and "
     "nothing that calls you smaller than that speaks for heaven."),
]

CARD_SEG = ("card", NARRATOR,
            "God has a face. You have a title — child of God. Never let "
            "anyone shrink either one.")

CARD_TEXT = ("Never let anyone\n"
             "shrink your title.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Fourteen — Face to Face")

SPOKEN = {}

MOSES = (
    "MOSES LOCK: the same man as the attached reference in every picture — "
    "the great lawgiver in vigorous old age: deep bronze sun-scorched "
    "skin, LONG loose white hair to mid-back, a massive white beard, "
    "heavy dark brows over piercing eyes, broad-shouldered, in a robe of "
    "rust-red and grey desert stripes with a rope belt, a tall shepherd's "
    "staff always in hand. Thunder and meekness in one face. No halo, no "
    "glow.")

LOCKS = {"MOSES-GP": MOSES}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="ancient")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "Sinai wilderness at dawn: red granite ramparts climbing out of "
        "grey scree into a sky of cold fire, one high summit still "
        "holding a torn banner of cloud, the valleys black and silent "
        "below. Immense, severe, waiting. No people.",
        "red granite Sinai ramparts at cold-fire dawn, one cloud-torn "
        "summit",
        "figures, camps, drawn rays, text",
        wide=True)),
    ("p02", "n2", _p(
        "The bush that burns and is not consumed: on the rocky slope a "
        "desert thorn-bush stands wrapped in living flame — every leaf "
        "green and whole inside the fire — and Moses approaches from "
        "the frame's near side, seen from behind, caught mid-motion "
        "pulling the sandal from his second foot, staff laid on the "
        "ground. The flame lights the rocks; nothing chars.",
        "a green unburnt bush wrapped in flame and Moses from behind "
        "removing his second sandal, staff laid down",
        "smoke, charring, any figure in the flame, his face",
        locks=["MOSES-GP"])),
    ("p03", ("n2", 0.5), _p(
        "The sea on end: the dry seabed corridor at night lit by a "
        "pillar of fire's warm firelight off-frame — two towering walls of "
        "dark green water standing sheer on either side, fish shadows "
        "moving inside them — and the freed multitude streaming away "
        "from the camera down the corridor, families, herds, laden "
        "shoulders, all seen from behind at the corridor's mouth.",
        "a walking multitude from behind crossing dry seabed between "
        "two standing water walls",
        "faces to camera, chariots yet, lightning, drawn rays",
        wide=True)),
    ("p04", "s1", _p(
        "Face to face: at the door of the meeting tent on the "
        "mountain, Moses STANDS — not prostrate, not cowering — before "
        "a column of brilliant white-gold light that fills the tent "
        "door and the frame's left half, his posture easy and open "
        "like a man in a doorway with an old friend, his face lit "
        "full by the brilliance he faces. No figure is visible inside "
        "the light.",
        "Moses standing at ease in a tent doorway facing a brilliant "
        "columned light, friend's posture, face fully lit",
        "any figure inside the light, cowering, drawn rays, his "
        "eyes on the lens",
        locks=["MOSES-GP"])),
    ("p05", "n3", _p(
        "The friend's face: Moses close in three-quarter, washed in "
        "the warm brilliance from off-frame left — and his expression "
        "is the whole doctrine: calm, familiar awe, the beginnings of "
        "a smile inside the white beard, the eyes of a man TALKING "
        "WITH someone, not surviving something.",
        "Moses' close three-quarter face in warm light with familiar "
        "awe and a beginning smile",
        "terror, tears, his eyes on the lens, halo",
        locks=["MOSES-GP"])),
    ("p06", "g1", _p(
        "The mission statement's vantage: Moses stands small on a "
        "summit shelf, seen from behind, and before him the vision "
        "opens — near hills falling away into an ocean of cloud, "
        "and above, the deep blue of high daylight shading toward "
        "space, faint FIELDS OF STARS beginning in its darkest "
        "reaches — creation's sheer depth shown to one man. His "
        "staff and hair stream in the vision's wind. The sky holds "
        "NO moon and NO planets — only deepening blue and faint "
        "stars.",
        "Moses small from behind on a summit before deep daylight "
        "blue shading to faint star-fields, cloud-ocean below",
        "any moon, crescent, planet or sphere in the sky, his "
        "face, drawn rays",
        wide=True, locks=["MOSES-GP"])),
    ("p07", "n5", _p(
        "His glory is children rising: dawn in the Israelite camp — "
        "three fathers in the near frame lifting small children high "
        "onto shoulders against the sunrise, mothers laughing beside, "
        "tents and morning smoke behind — every face toward a child "
        "or the light, none toward the lens. Joy as doctrine.",
        "fathers swinging children onto shoulders at sunrise in a "
        "tent camp, mothers laughing, faces on children and light",
        "faces to camera, golden calf, misery",
        )),
    ("p08", "n6", _p(
        "The glory withdraws: the summit gone grey and ordinary — "
        "cloud dragging past bare rock, wind flattening the scrub — "
        "and Moses sagged against a boulder, one hand braced on it, "
        "head hanging, a man emptied by glory and left mortal-weak. "
        "Seen from the side at a distance; small, drained, human.",
        "Moses sagged weak against a boulder on a grey wind-dragged "
        "summit",
        "his face close, tears, any dark presence yet",
        locks=["MOSES-GP"])),
    ("p09", "d1", _p(
        "The other voice: Moses stands square on the slope facing a "
        "WALL of formless darkness that has swallowed the downhill "
        "half of the frame — a cold black absence with no shape, no "
        "eyes, no edges that mean anything — his staff planted, his "
        "weakness gone rigid with attention. Seen from his side: "
        "man on the right in grey light, empty dark filling the "
        "left.",
        "Moses square and planted facing a formless wall of dark "
        "filling half the frame",
        "ANY figure, face, eyes or shape in the dark; lightning; "
        "his eyes on the lens",
        devil=True, locks=["MOSES-GP"])),
    ("p10", "s2", _p(
        "WHO ART THOU: Moses' face close, mid-declaration into the "
        "cold off-frame dark — brows like storm-fronts, eyes blazing "
        "certainty, the words visibly leaving him with the force of "
        "a thrown spear — and warm light beginning to win back the "
        "edge of his face as he speaks.",
        "Moses' close face mid-declaration, storm brows, certainty "
        "blazing, warmth returning at the edge",
        "fear, his eyes on the lens, spittle, caricature rage",
        devil=True, locks=["MOSES-GP"])),
    ("p11", ("s2", 0.6), _p(
        "A son of God, standing: Moses full-length, feet planted "
        "wide on the rock, staff grounded like a boundary-stake, "
        "free hand open at his side — and the darkness before him "
        "RECOILED to the frame's edge, thinned, its smooth boundary "
        "pushed back from his planted staff. The claim, held.",
        "Moses planted full-length with grounded staff, the "
        "formless dark recoiled thin at the frame's edge",
        "any shape in the dark, wind drama, his face to camera",
        devil=True, locks=["MOSES-GP"])),
    ("p12", "s3", _p(
        "DEPART: the darkness TEARS off the mountainside — draining "
        "down-slope over the scree like a ripped-away tide, its last "
        "formless mass sliding below the frame's bottom edge — while "
        "grey daylight floods back across the rocks from above, and "
        "Moses stands small and unmoved at the frame's top with his "
        "staff still planted.",
        "formless darkness draining down-slope off the mountain "
        "while daylight floods back, Moses small and unmoved above",
        "any figure or wings in the dark, lightning, fire",
        wide=True, devil=True, locks=["MOSES-GP"])),
    ("p13", "n9", _p(
        "After: the summit quiet in returned light, and Moses "
        "sitting on the boulder now — shoulders down, face lifted, "
        "eyes closed, breathing like a man after deep water — the "
        "wind gone gentle in his white hair. Survived, and more "
        "than survived.",
        "Moses seated and breathing, face lifted with closed eyes "
        "in gentle returned light",
        "his eyes on the lens, wounds, any dark remnant",
        locks=["MOSES-GP"])),
    ("p14", "n10", _p(
        "The forgetting: from high on the mountain's shoulder, the "
        "camp far below — a ring of thousands circling something "
        "small that GLINTS gold at the centre, threads of smoke, "
        "the faint chaos of revelry readable in the swirl of the "
        "crowd even at this distance. Seen past a near rock edge; "
        "grief built into the vantage itself.",
        "a distant camp circling a small gold glint, revel-swirl "
        "readable from the mountain's high vantage",
        "the calf detailed, nudity, faces, fire large",
        wide=True)),
    ("p15", ("n10", 0.5), _p(
        "The weight coming down: Moses descending the slope with "
        "the two stone tablets held against his chest, caught in "
        "profile mid-stride — his face set between fury and "
        "heartbreak, the camp's smoke rising soft in the depth "
        "below him. The tablets' surfaces stay turned from the "
        "camera, unreadable.",
        "Moses in profile descending with two stone tablets "
        "against his chest, fury and heartbreak set together",
        "readable writing, his eyes on the lens, the calf",
        locks=["MOSES-GP"])),
    ("p16", "n11", _p(
        "The title, worn today: a young man stands at the edge of "
        "a sunrise field in the present day, seen in profile, chin "
        "level, shoulders open, hands easy at his sides — the "
        "plain unbowed posture of somebody who knows what he is "
        "called and by Whom. Long gold light across the grass.",
        "a young man's unbowed level-chinned profile at a sunrise "
        "field edge",
        "his eyes on the lens, phone, brand marks, slouch",
        era="modern")),
    ("p17", ("n11", 0.5), _p(
        "God has a face: Jesus close in warm three-quarter — the "
        "Face the whole third movement is walking toward — gentle, "
        "alive, looking off past the camera's left shoulder with "
        "the warmth of someone who knows your name. The bridge to "
        "everything that comes next.",
        "Jesus's warm close three-quarter face, gaze past the "
        "lens, alive and knowing",
        "his eyes on the lens, halo, glow, grimness",
        era="first-century", jesus=True, ref=True)),
    ("p18", ("n11", 0.8), _p(
        "Sinai at peace: the granite ramparts at full soft "
        "morning — the severity washed gold, the high summit "
        "clear of cloud, a pair of desert larks crossing the "
        "immense quiet. The mountain that held the meetings, "
        "at rest. No people.",
        "golden peaceful Sinai ramparts, clear summit, two larks "
        "crossing",
        "figures, camps, drawn rays, text",
        wide=True)),
]
