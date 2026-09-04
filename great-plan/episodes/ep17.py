#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 17: The Condescension.

The King enters his own world unarmed: Mary's yes, a feed-trough throne,
shepherds and a hemisphere with no darkness — and the enemy answering a
baby with swords in Judea and mockery in America.
Anchors: Luke 1:38; 2:10-11; 3 Nephi 1:19; 1 Nephi 11:16-17.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 317
NUM = 17
SLUG = "condescension"
TITLE = "The Condescension"
META = "Luke 1-2 · 3 Nephi 1 · 1 Nephi 11"

SEGMENTS = [
    ("n1", NARRATOR,
     "The King of the universe is about to enter His own world. Watch "
     "HOW He arrives — the one way that leaves you free."),
    ("n2", NARRATOR,
     "Not a palace. Not a legion. Heaven ASKS — a hill-town girl "
     "engaged to a carpenter, free to refuse, says yes:"),
    ("w1", WOMAN,
     "Behold the handmaid of the Lord; be it unto me according to thy "
     "word."),
    ("n3", NARRATOR,
     "Nine months later, in a stable behind a full inn, the Creator of "
     "galaxies drew His first breath in a feed trough — announced not to "
     "kings, but to night-shift shepherds:"),
    ("s1", SCRIPTURE,
     "Fear not: for, behold, I bring you good tidings of great joy, "
     "which shall be to all people. For unto you is born this day in the "
     "city of David a Saviour, which is Christ the Lord."),
    ("n4", NARRATOR,
     "To ALL people — and heaven meant all. On the far side of the "
     "world, the other sheep received their own announcement, exactly as "
     "their prophets had promised:"),
    ("s2", SCRIPTURE,
     "And it came to pass that there was no darkness in all that night, "
     "but it was as light as though it was mid-day."),
    ("n5", NARRATOR,
     "One birth. Two hemispheres. Both notified. Nobody's children get "
     "left off God's announcement list."),
    ("n6", NARRATOR,
     "Now watch the enemy answer a baby. In Judea he moved a king to "
     "slaughter Bethlehem's infant sons. In America he flooded the land "
     "with a rumor — the signs meant nothing, believing was foolish. "
     "Swords on one side of the world, mockery on the other. Anything "
     "to smother the cradle."),
    ("n7", NARRATOR,
     "It did not work. It never works. Joseph was warned in a dream and "
     "carried the child to Egypt. The believers held through the bright "
     "night. The cradle outlived both attacks."),
    ("n8", NARRATOR,
     "There is a word for what God did in Bethlehem: condescension — "
     "the willing descent. Nephi was shown it centuries early, and an "
     "angel asked him the question of the ages:"),
    ("s3", SCRIPTURE,
     "Knowest thou the condescension of God? And I said unto him: I "
     "know that he loveth his children; nevertheless, I do not know the "
     "meaning of all things."),
    ("n9", NARRATOR,
     "I know that He loves His children — I do not know the meaning of "
     "all things. That answer is still the finest theology ever spoken. "
     "And the condescension means this: God did not send a "
     "representative. He came. Small enough to be held. Poor enough to "
     "be overlooked. Vulnerable enough to be hunted."),
    ("n10", NARRATOR,
     "The devil offers power that crushes. God arrived as weakness that "
     "saves. And a King who begins in a feed trough can meet you "
     "anywhere — there is no floor of your life lower than where He "
     "started."),
    ("n11", NARRATOR,
     "So when life makes you small, remember how He chose to enter. The "
     "manger is not quaint. It is the whole strategy — love that walks "
     "in the door unarmed."),
]

CARD_SEG = ("card", NARRATOR,
            "He did not send a representative. He came — small enough "
            "to be held.")

CARD_TEXT = ("Love walked in\n"
             "unarmed.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Seventeen — The Condescension")

SPOKEN = {}

MARY = (
    "MARY LOCK: the same young woman in every picture — Mary of "
    "Nazareth at about sixteen: warm olive skin, dark expressive brows, "
    "long dark hair beneath a blue-grey head mantle over a simple undyed "
    "dress, small work-worn hands. Quiet courage, deep stillness. No "
    "halo, no glow.")

JOSEPHC = (
    "JOSEPH-CARPENTER LOCK: the same man in every picture — Joseph the "
    "carpenter in his late twenties: sun-browned, strong forearms, short "
    "dark beard, plain brown work tunic and dusty travel cloak. Steady, "
    "watchful, gentle. No halo, no glow.")

LOCKS = {"MARY-N": MARY, "JOSEPH-C": JOSEPHC}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="first-century")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The arrival vector: the earth from high space, its dawn line "
        "burning gold across dark oceans and cloud — the whole waiting "
        "world turning slowly into light, seen the way heaven saw it "
        "the week the King went down. No figures, no text.",
        "the earth's gold dawn line from high space, the world "
        "turning into light",
        "satellites, country outlines prominent, text, figures",
        )),
    ("p02", "n2", _p(
        "The unlikely address: Nazareth in morning light — a small "
        "huddle of flat-roofed limestone houses on a Galilean "
        "hillside, terraced olives, smoke from cook-fires, washing on "
        "a line, a donkey in a lane. Utterly ordinary; about to be "
        "the most famous village on earth.",
        "small ordinary hillside Nazareth in morning light — flat "
        "roofs, olives, wash lines",
        "crowds, palaces, temples, figures close",
        wide=True)),
    ("p03", "w1", _p(
        "The yes: young Mary stands in her small stone room flooded "
        "from one high window by extraordinary morning brilliance — "
        "her face lifted into the light in three-quarter, one hand "
        "flat over her heart, the other open at her side — the "
        "stillness of a girl saying the bravest yes in history. No "
        "figure appears in the light.",
        "young Mary's lifted three-quarter face in window "
        "brilliance, hand flat on heart, open palm",
        "any figure in the light, wings, halo, her eyes on the "
        "lens",
        locks=["MARY-N"])),
    ("p04", "n3", _p(
        "The road heavy: Joseph leads the donkey bearing Mary along "
        "a stony dusk road toward distant Bethlehem's lamplit "
        "terraces — both seen from behind, his hand tight on the "
        "halter, her mantle wrapped close, the last light dying "
        "violet over the hills ahead.",
        "Joseph leading the donkey with Mary from behind on a dusk "
        "road toward lamplit Bethlehem",
        "faces, snow, crowds, drawn star yet",
        wide=True, locks=["MARY-N", "JOSEPH-C"])),
    ("p05", ("n3", 0.5), _p(
        "No room: an inn's heavy door swings shut from within — the "
        "warm lamplight narrowing to a thread across the worn "
        "threshold stone, a innkeeper's arm barely visible on the "
        "closing edge — the oldest closed door in the world's most "
        "repeated story. Close on the narrowing light.",
        "an inn door closing, lamplight narrowing to a thread "
        "across the threshold",
        "faces, argument, the holy family in frame",
        )),
    ("p06", ("n3", 0.75), _p(
        "The throne: inside the stable's lantern-warmth, Mary "
        "cradles the newborn against her cheek, Joseph kneeling "
        "close with one protective hand on the manger's edge, the "
        "ox and donkey dim shapes of warmth beyond — every face "
        "bent to the child, the child's small face at peace. "
        "Reverent, close, golden.",
        "Mary's cheek at the newborn's head, Joseph kneeling with "
        "hand on the manger, animals dim beyond, all faces on the "
        "child",
        "halos, visible breath of God effects, kings yet, faces "
        "to camera",
        locks=["MARY-N", "JOSEPH-C"])),
    ("p07", "s1", _p(
        "The announcement: on the night hillside the shepherds are "
        "caught mid-recoil — one thrown back on his elbow, one "
        "shielding his eyes, one already on his knees — as immense "
        "brilliance floods down on them from above the frame's top "
        "edge, their flock scattering bright at the edges. The "
        "light's source stays above the frame; their faces hold "
        "terror turning to joy.",
        "shepherds mid-recoil in flooding brilliance from above "
        "the frame, terror turning joy, flock scattering",
        "any figure in the light, wings, halo, drawn rays",
        wide=True)),
    ("p08", ("s1", 0.6), _p(
        "The run: the shepherds sprint downhill toward the town's "
        "lamplit terraces — staffs in hand, cloaks streaming, one "
        "laughing aloud mid-stride — seen from the side in the "
        "strange bright night, joy at a dead run.",
        "shepherds sprinting downhill toward lamplit terraces, "
        "cloaks streaming, joy",
        "faces to camera, the light source shown, drawn star",
        )),
    ("p09", "n4", _p(
        "The other hemisphere's sign: a new-world stone city at "
        "midnight lit exactly like noon — streets and stepped "
        "temple bright as day under a deep-blue star-pricked sky "
        "with NO sun anywhere, people standing motionless in the "
        "streets staring upward, shadows soft and sourceless. "
        "Beautiful and impossible.",
        "a stone city at midnight lit like noon under a sunless "
        "star-pricked sky, people staring up",
        "a sun or moon in frame, panic, fires, drawn rays",
        wide=True, era="ancient")),
    ("p10", "s2", _p(
        "As light as mid-day: on a flat rooftop in the bright "
        "night, a Nephite family stands amazed — the father's arm "
        "around the mother, and their small daughter pointing "
        "straight up at the blazing sunless sky, her mouth open — "
        "every face upturned and washed in the impossible light.",
        "a rooftop family in the bright sunless night, small "
        "daughter pointing straight up, faces washed in light",
        "a sun, faces to camera, fear",
        era="ancient")),
    ("p11", "n5", _p(
        "One sky for both: the new star standing over sleeping "
        "Bethlehem — larger and stiller than every other light in "
        "the deep-blue field, the town's terraces silver beneath "
        "it, one lamp still burning somewhere low. The same sky "
        "that blazed over the other sheep. Quiet as a kept "
        "promise.",
        "one large still star over sleeping silver Bethlehem "
        "terraces",
        "drawn rays off the star, angels, figures",
        wide=True)),
    ("p12", "n6", _p(
        "The enemy moves a king: torch-lit palace hall — Herod "
        "leaning forward off his throne mid-command, his arm "
        "thrust toward the door, face knotted with fear wearing "
        "anger — and a file of soldiers already turning away to "
        "obey, spears swinging toward the exit, their faces grim "
        "and shadowed. The order is the whole frame; nothing that "
        "follows is ever shown.",
        "Herod mid-command off his throne, soldiers turning to "
        "leave with grim shadowed faces",
        "violence, children, mothers, blood, streets",
        )),
    ("p13", ("n6", 0.5), _p(
        "The enemy floods a rumor: around a night fire, new-world "
        "scoffers laugh too loudly — one mimicking a stargazer "
        "with waggling fingers at the sky, another doubled over, "
        "wine cups loose — mockery as strategy, every face lit "
        "cruel-bright by the flames, none toward the camera.",
        "firelit scoffers mid-mockery, one mimicking a stargazer "
        "at the sky, cruel bright laughter",
        "faces to camera, weapons, believers in frame",
        era="ancient")),
    ("p14", "n7", _p(
        "The dream obeyed: under deep stars Joseph leads the "
        "donkey away at speed — Mary's mantled shape curved "
        "around the bundled child on its back — both seen from "
        "behind on a desert track running toward Egypt's flat "
        "dark horizon, Bethlehem's faint lights already far "
        "behind the frame's edge.",
        "Joseph hurrying the donkey with mantled Mary and child "
        "from behind under deep stars toward a flat horizon",
        "pursuers, faces, city close behind, dawn",
        wide=True, locks=["MARY-N", "JOSEPH-C"])),
    ("p15", ("n7", 0.5), _p(
        "The believers hold: in the impossible bright night, a "
        "circle of new-world believers kneels together in a "
        "courtyard — faces steady and lifted, hands joined or "
        "pressed to hearts, the mockers' distant fire a small "
        "red point far beyond the wall. Faith, holding its "
        "ground in the light.",
        "kneeling believers with steady lifted faces in the "
        "bright night, mockers' fire a far red point",
        "fear, faces to camera, weapons",
        era="ancient")),
    ("p16", "s3", _p(
        "Nephi's answer: young Nephi kneels on a high place in "
        "vision-light, face lifted to an unseen questioner above "
        "the frame — his expression the exact mixture the verse "
        "holds: certain love, honest unknowing — strong young "
        "features open and unashamed under the question.",
        "young Nephi's lifted face holding certain love and "
        "honest unknowing together",
        "the angel shown, his eyes on the lens, halo",
        era="ancient")),
    ("p17", "n9", _p(
        "He came: the newborn's whole hand wrapped around Mary's "
        "finger in the lantern light — the grip strong, the "
        "small knuckles new — the same image every episode of "
        "this series has carried, now holding the finger of his "
        "own mother in the world he made. Extreme close.",
        "the newborn's hand gripping Mary's finger in lantern "
        "light, extreme close",
        "faces, halo, jewellery, text",
        locks=["MARY-N"])),
    ("p18", "n10", _p(
        "No lower floor: the manger itself, close — rough-adzed "
        "wood packed with straw, the sleeping newborn swaddled "
        "in plain cloth within it, lantern warmth raking the "
        "wood grain and the small still face. The throne the "
        "strategy chose. Nothing else in frame.",
        "the swaddled sleeping newborn close in the rough straw-"
        "packed manger, lantern warmth",
        "halos, gifts, figures, animals close",
        )),
    ("p19", ("n11", 0.5), _p(
        "The strategy at rest: the star over the sleeping town "
        "once more, wider — the hills silver, the stable's one "
        "faint lamp low on the slope, the immense quiet of a "
        "world that does not yet know what just arrived. No "
        "figures.",
        "the still star over silver hills and the stable's one "
        "faint low lamp",
        "angels, drawn rays, figures, text",
        wide=True)),
]
