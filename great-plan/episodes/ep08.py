#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 8: Not Damned for Adam.

The turning point most of Christianity lost: the Fall opens the plan, no baby
is born guilty, and Christ answers for Adam's transgression for everyone.
Anchors: 2 Nephi 2:22-25; Moses 5:10-11; Articles of Faith 2; Moroni 8:8.

Sacred-voice law: NARRATOR modern; Adam and Lehi = SCRIPTURE (light blue);
Eve = WOMAN (pink); the Lord's words in Moroni 8:8 = JESUS (red).
"""

NARRATOR, JESUS, SCRIPTURE, WOMAN, DEVIL = ("narrator", "jesus", "scripture",
                                            "woman", "devil")

EP = 308
NUM = 8
SLUG = "not-damned-for-adam"
TITLE = "Not Damned for Adam"
META = "2 Nephi 2 · Moses 5 · Moroni 8"

SEGMENTS = [
    ("n1", NARRATOR,
     "If you have ever been told that you were born guilty — that a baby "
     "arrives in this world already condemned for something a man did in a "
     "garden — this one is for you."),
    ("n2", NARRATOR,
     "Adam and Eve took the fruit, and everything changed. The gate closed "
     "behind them. Death entered the world. And heaven watched it happen — "
     "without panic."),
    ("n3", NARRATOR,
     "Because the Fall was not the plan breaking. It was the plan "
     "beginning."),
    ("n4", NARRATOR,
     "Outside Eden the ground fought them. Thorns. Sweat. Loss. And also — "
     "for the first time — children. Morning laughter. Work worth doing. "
     "Choices that actually meant something."),
    ("s1", SCRIPTURE,
     "Blessed be the name of God: for because of my transgression my eyes "
     "are opened, and in this life I shall have joy."),
    ("n5", NARRATOR,
     "That is Adam — the man the whole mess gets blamed on — praising God "
     "for what the Fall opened up. And Eve saw it first, and saw it whole:"),
    ("w1", WOMAN,
     "Were it not for our transgression we never should have had seed, and "
     "never should have known good and evil, and the joy of our redemption."),
    ("n6", NARRATOR,
     "Seed. Knowledge. Redemption. No children without the Fall. No growth "
     "without a real dark to choose against. And no need for a Savior — no "
     "Savior given."),
    ("s2", SCRIPTURE,
     "Adam fell that men might be; and men are, that they might have joy."),
    ("n7", NARRATOR,
     "So what about the guilt? Who pays for Eden? Here is what God actually "
     "says about that."),
    ("s3", SCRIPTURE,
     "We believe that men will be punished for their own sins, and not for "
     "Adam's transgression."),
    ("n8", NARRATOR,
     "Not for Adam's transgression. You will answer for what you choose. "
     "You will never answer for what Adam chose. There is no inherited "
     "guilt. There is no baby born condemned."),
    ("j1", JESUS,
     "Little children are whole, for they are not capable of committing "
     "sin; wherefore the curse of Adam is taken from them in me."),
    ("n9", NARRATOR,
     "The curse of Adam is taken from them in me. Every baby ever born "
     "arrives clean — already covered, already paid for, before their "
     "first breath."),
    ("n10", NARRATOR,
     "The devil has spent centuries teaching the world to fear God over "
     "Eden — a God who condemns infants, a guilt you carry for another "
     "man's choice. Now you know. That was never your Father."),
    ("n11", NARRATOR,
     "The Fall brought death — and Christ answers death, for everyone, "
     "free. The Fall brought sin — and you answer only for yours, with a "
     "Redeemer standing by. Adam fell that men might be. And men are, that "
     "they might have joy."),
]

CARD_SEG = ("card", NARRATOR,
            "You were not born guilty. You were born wanted — into a plan "
            "built to bring you joy.")

CARD_TEXT = ("You were not born guilty.\n"
             "You were born wanted.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Eight — Not Damned for Adam")

SPOKEN = {}

ADAM = (
    "ADAM LOCK: the same man as the attached reference in every picture — the "
    "first man, in his strong mid-thirties, warm olive-brown sun-weathered "
    "skin, thick shoulder-length near-black hair and a full dark beard, broad "
    "workman's build, wearing a simple garment of rough earth-brown woven "
    "cloth over one shoulder. Kind, intelligent, weathered. No halo, no glow.")

EVE = (
    "EVE LOCK: the same woman as the attached reference in every picture — "
    "the first woman, mid-thirties, warm olive-brown skin, very long dark "
    "wavy hair, strong gentle intelligent features, wearing a simple woven "
    "dress in muted sage-and-earth tones. Wise, warm, fearless. No halo, no "
    "glow.")

LOCKS = {"ADAM": ADAM, "EVE": EVE}

REFS = {}

def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="ancient")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "A newborn baby asleep in its mother's arms inside a dim ancient "
        "dwelling, lamplight warm on the tiny face; the mother's head is "
        "bowed over the child so her face shows only in soft downturned "
        "profile. The frame is close and tender — swaddling cloth of rough "
        "weave, the baby's small fist curled at its cheek.",
        "a sleeping newborn close in its mother's arms, warm clay-lamp "
        "light, rough swaddling cloth",
        "the mother looking at the camera, any text, modern cloth, glow")),
    ("p02", ("n1", 0.55), _p(
        "Extreme close detail: the newborn's tiny hand wrapped tight around "
        "one adult finger, warm light raking across the small knuckles and "
        "the parent's work-rough skin. Nothing else in focus.",
        "a newborn's hand gripping one adult finger, close and warm",
        "faces, text, jewellery, modern objects")),
    ("p03", "n2", _p(
        "Adam and Eve walk away from Eden: seen full-length from behind as "
        "they cross a rocky threshold out of towering green abundance into "
        "open wild grassland under a great morning sky. The camera stands "
        "behind them and shoots past their backs toward the wide unknown "
        "land ahead; neither face is visible. Eden's edge rises behind and "
        "beside the frame as a wall of deep living green.",
        "the first couple from directly behind, leaving a wall of garden "
        "green and stepping into open wild country",
        "faces visible, anyone turned to camera, angels, swords, glow",
        wide=True, era="eden", locks=["ADAM", "EVE"])),
    ("p04", ("n2", 0.58), _p(
        "Looking back the way they came: far across the rocky ground, the "
        "garden stands sealed — a distant line of impossible green beneath "
        "brooding bright cloud, and at its single gap a thin vertical line "
        "of white flame turning slowly, small with distance. In the near "
        "foreground, out of focus at the frame's edge, Eve's shoulder and "
        "dark hair as she looks back; her face is turned away from the "
        "camera toward the garden.",
        "the sealed garden far away with one thin turning line of flame at "
        "its gap, Eve's out-of-focus shoulder near the lens looking back",
        "any angel figure, faces to camera, a sword shape, halo, beams",
        era="eden", locks=["EVE"])),
    ("p05", "n3", _p(
        "Dawn over the fallen world, immense and hopeful: from a high "
        "ridge, wild untouched country rolls to the horizon under a sunrise "
        "of gold and rose, and far below, two tiny figures walk together "
        "into it, side by side — the camera looks down past them from high "
        "behind so only their backs are seen, walking away from the lens. The land is hard and "
        "beautiful at once — stone, scrub, a bright thread of river.",
        "a vast sunrise wilderness with two tiny figures walking into it "
        "from high behind, a river thread below",
        "faces, ruins, buildings, roads, anyone facing the camera",
        wide=True, era="eden", locks=["ADAM", "EVE"])),
    ("p06", "n4", _p(
        "Adam at hard labour: driving a fire-hardened wooden digging stick "
        "into stony soil, caught mid-strain from a low three-quarter side "
        "angle, sweat lining his face and forearms, thorn-scrub and broken "
        "ground around him, harsh midday light. His gaze is down on his "
        "work; the effort is real and heavy.",
        "Adam straining a wooden digging stick into stony thorn-scrubbed "
        "ground, sweat visible, gaze down on the work",
        "metal tools, his eyes on the lens, tidy farmland, glow",
        locks=["ADAM"])),
    ("p07", ("n4", 0.48), _p(
        "Eve outside a shelter of branches and hides, caught mid-laugh as "
        "two small children run to her, the nearer child leaping for her "
        "opening arms — all three seen from a three-quarter side angle, "
        "faces lit by late-afternoon gold, nobody toward the lens. Motion "
        "and joy: her hair swinging, the children's bare feet off the "
        "ground mid-stride.",
        "Eve mid-laugh catching a leaping child, a second child running "
        "in, branch-and-hide shelter behind, golden light",
        "anyone facing the lens, modern clothing, tidy buildings",
        locks=["EVE"])),
    ("p08", ("n4", 0.78), _p(
        "Night, the first family around a wood fire: Adam mid-story with "
        "both hands raised in a shape only storytellers make, Eve beside "
        "him with the youngest asleep against her, three older children "
        "cross-legged and rapt, every face lit only by moving firelight "
        "and every gaze on Adam or the flames — none on the camera, which "
        "watches from just outside the circle past a child's shoulder.",
        "a firelit family circle, Adam mid-gesture telling, children "
        "rapt, camera outside the circle past a shoulder",
        "anyone facing the lens, lanterns, buildings, moonbeams",
        locks=["ADAM", "EVE"])),
    ("p09", "s1", _p(
        "Adam's praise at dawn: he stands on high open ground facing the "
        "sunrise with his arms spread low and palms open, head lifted, "
        "seen in three-quarter from behind his left shoulder so the light "
        "falls on the visible edge of his upturned face — gratitude in "
        "the whole posture. Below and beyond, the wild land he now works "
        "rolls into morning mist.",
        "Adam from three-quarter behind, arms spread low to a sunrise, "
        "upturned profile edge visible, misted wild land below",
        "his eyes on the lens, halo, beams of light, any altar yet",
        locks=["ADAM"])),
    ("p10", "n5", _p(
        "Eve steps to Adam's side on the dawn ridge and lays her hand on "
        "his arm; he turns his head toward her. Both in three-quarter "
        "profile facing each other — her face lit with a knowing, settled "
        "understanding that outruns his wonder. The sunrise builds beyond "
        "them.",
        "Eve's hand on Adam's arm on the ridge, two three-quarter "
        "profiles facing each other, sunrise beyond",
        "either face toward the lens, embrace, halo, tears",
        locks=["ADAM", "EVE"])),
    ("p11", "w1", _p(
        "Close on Eve as she speaks the greatest sentence of the early "
        "world: her face in strong three-quarter view turned toward Adam "
        "off the right frame edge, morning light full on her features — "
        "fierce joy, clear eyes, the look of the first person to "
        "understand the plan from inside it. Her long dark hair moves "
        "slightly in the dawn wind.",
        "Eve's face close in three-quarter, fierce joyful clarity, "
        "gaze off right frame edge",
        "her eyes on the lens, tears, halo, softness that reads as "
        "weakness",
        locks=["EVE"])),
    ("p12", "n6", _p(
        "The seed of Eve, wide: a busy morning encampment of hide tents "
        "and woven windbreaks alive with children of every age — toddlers "
        "stacking stones, girls carrying water jars, boys driving goats, "
        "a grandmother grinding grain — the camera standing behind a near "
        "tent line and shooting past it into the camp so every figure is "
        "seen from the side or behind, absorbed in living. Smoke threads "
        "up into early light.",
        "an encampment full of children and work seen past a near tent "
        "line, every figure absorbed, none facing the lens",
        "anyone facing the camera, modern objects, stone buildings",
        wide=True)),
    ("p13", "s2", _p(
        "Pure joy in one frame: a young father tosses his small child "
        "high against the bright morning sky and the child's arms fly "
        "wide mid-air, both laughing — seen from the side at a low angle "
        "so both faces show in profile against the sky, neither toward "
        "the lens. Grass and light; nothing else.",
        "a father mid-toss, child mid-air arms wide, both laughing in "
        "profile against bright sky",
        "either face toward the lens, danger in the pose, buildings",
        )),
    ("p14", "n7", _p(
        "The question made visible: night inside a dwelling of stone and "
        "timber, a father and mother kneeling over their newborn's "
        "sleeping basket, their faces in soft lamplit profile bent "
        "toward the child — love shadowed by a question. The clay lamp's "
        "small flame is the only light; the parents' hands rest on the "
        "basket edge.",
        "two parents bent over a sleeping newborn's basket by clay-lamp "
        "light, love with a question in it",
        "faces to camera, tears streaming, any dark presence, glow",
        )),
    ("p15", "s3", _p(
        "A man kneels alone in an open morning field, back straight, "
        "face lifted to the sky with his eyes closed, hands open on his "
        "knees — the posture of someone who answers for himself to God "
        "and no one else. Seen from a three-quarter side angle at a "
        "respectful distance; dew on the grass, clean early light.",
        "one man kneeling upright in a morning field, face lifted, "
        "eyes closed, hands open",
        "his eyes on the lens, a crowd, any altar or priest, beams",
        )),
    ("p16", "n8", _p(
        "An infant asleep on its father's bare chest, the father's one "
        "broad hand covering the whole of the baby's back, his bearded "
        "chin resting lightly on the small head, eyes closed — total "
        "safety in one close frame, warm low light, rough-woven blanket "
        "around them both.",
        "a sleeping infant on a father's chest under one covering hand, "
        "warm close safety",
        "faces to camera, open eyes on the lens, modern cloth",
        )),
    ("p17", "j1", _p(
        "Jesus among the mothers and little children: seated on a low "
        "stone wall in cream, a baby cradled in the bend of his left arm "
        "and his right hand resting gently on the head of a toddler who "
        "grips his knee, three mothers and their children gathered close "
        "around — every adult and child face turned toward Jesus or the "
        "baby, none toward the lens; the camera stands beside the group "
        "at shoulder height and shoots past the nearest mother's "
        "shoulder. Soft courtyard morning light.",
        "Jesus seated holding a baby in his left arm, right hand on a "
        "toddler's head, mothers gathered, all gazes on him or the baby",
        "anyone facing the lens, halo, glow, cream on anyone else, "
        "extra unexplained figures",
        era="first-century", jesus=True, ref=True, wide=True)),
    ("p18", ("j1", 0.55), _p(
        "Close: the baby in the bend of Jesus's arm, utterly at peace, "
        "one tiny hand resting open against the cream wool of his robe; "
        "Jesus's face above in soft three-quarter looking down at the "
        "child with complete tenderness. His right hand supports the "
        "baby's body; every finger natural and accounted for.",
        "the baby at peace in his arm, tiny open hand on cream wool, "
        "his three-quarter face looking down in tenderness",
        "his eyes on the lens, halo, glow, malformed hands, a second "
        "cream garment",
        era="first-century", jesus=True, ref=True)),
    ("p19", "n9", _p(
        "First breath: in a lamplit birth room, a midwife's two strong "
        "hands lift a newborn — glistening, fists clenched, mid-cry — "
        "toward the light of the doorway, the mother's reaching arms "
        "soft in the foreground blur. The frame says one thing: this "
        "child arrives wanted and clean.",
        "a midwife's hands lifting a crying newborn toward doorway "
        "light, mother's arms reaching in soft blur",
        "graphic detail, faces to camera, modern objects, glow",
        )),
    ("p20", "n10", _p(
        "The old lie leaves the room: morning light floods through a "
        "small deep-set window into a stone nursery corner where a "
        "carved wooden cradle stands — and the last of a cold grey "
        "shadow-stain slides off the cradle and down the wall away from "
        "the light, formless, like night draining out of the room. The "
        "cradle and swaddled child in it lie fully in the warm light; "
        "the retreating dimness is empty of any shape.",
        "warm window light flooding a cradle while a formless cold "
        "shadow-stain drains off it and away down the wall",
        "ANY figure, face, eyes or shape in the shadow, smoke, horns, "
        "a frightened child",
        devil=True)),
    ("p21", "n11", _p(
        "The family walks into morning: father, mother and three "
        "children hand in hand, seen full-length from directly behind, "
        "walking away from the camera up a grassy rise into broad "
        "sunrise light, the smallest child riding the father's "
        "shoulders. The camera stays low behind them; no face turns "
        "back.",
        "a family of five from directly behind walking up into "
        "sunrise, smallest child on the father's shoulders",
        "any face turned back to the lens, buildings, roads, beams",
        wide=True)),
    ("p22", ("n11", 0.62), _p(
        "Bookend: the newborn's tiny hand again, wrapped around its "
        "parent's finger — but now in full golden morning light, the "
        "grip strong, the small knuckles bright. Close, warm, final.",
        "a newborn's hand gripping a parent's finger in full golden "
        "morning light, close",
        "faces, text, jewellery, modern objects",
        )),
]
