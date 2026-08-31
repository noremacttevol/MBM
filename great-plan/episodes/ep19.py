#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 19: Thy Will Be Done.

Gethsemane and the cross: the council's sentence, now costing everything.
Includes the risen Lord's own firsthand account (D&C 19) and the justice-
and-mercy answer to "why couldn't God just forgive?"
Anchors: Luke 22:42-44; Mark 14:34; D&C 19:16-18; John 19:30; Alma 42.

Restraint laws: anguish is shown in faces and darkness, never gore; the
scourging is never depicted; the crucifixion is distant and reverent; the
withheld legions are shown as a still, empty sky.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 319
NUM = 19
SLUG = "thy-will-be-done"
TITLE = "Thy Will Be Done"
META = "Luke 22 · D&C 19 · John 19"

SEGMENTS = [
    ("n1", NARRATOR,
     "Every episode so far has been building toward a garden and a "
     "hill. This is the night the plan got paid for. Stay close. This "
     "is what the council was about."),
    ("n2", NARRATOR,
     "After the last supper, Jesus led his friends across the valley to "
     "an olive grove called Gethsemane — the oil press. And there, the "
     "weight began to come down."),
    ("j1", JESUS,
     "My soul is exceeding sorrowful unto death: tarry ye here, and "
     "watch."),
    ("n3", NARRATOR,
     "Then he went a stone's throw further, and knelt. And every sin, "
     "every grief, every shame, every lonely midnight of every child of "
     "Adam began to press down onto one sinless soul."),
    ("j2", JESUS,
     "Father, if thou be willing, remove this cup from me: nevertheless "
     "not my will, but thine, be done."),
    ("n4", NARRATOR,
     "There it is — the sentence from before the world, now costing "
     "everything. Thy will be done was easy to say in the council. In "
     "the garden, it bled."),
    ("s1", SCRIPTURE,
     "And being in an agony he prayed more earnestly: and his sweat was "
     "as it were great drops of blood falling down to the ground."),
    ("n5", NARRATOR,
     "Centuries later, the risen Lord described that night himself — "
     "the only firsthand account of an atonement ever given:"),
    ("j3", JESUS,
     "For behold, I, God, have suffered these things for all, that they "
     "might not suffer if they would repent."),
    ("j4", JESUS,
     "Which suffering caused myself, even God, the greatest of all, to "
     "tremble because of pain, and to bleed at every pore, and to "
     "suffer both body and spirit."),
    ("n6", NARRATOR,
     "God, the greatest of all — trembling. For you. So that if you "
     "repent, that pain never has to become yours."),
    ("n7", NARRATOR,
     "Then betrayal, with a kiss. A rigged midnight trial. And Rome's "
     "worst. Through all of it he said almost nothing — this is your "
     "hour, he told them, and the power of darkness. The devil threw "
     "everything at getting him to quit. Or to call the twelve legions "
     "of angels he actually had."),
    ("n8", NARRATOR,
     "He did not call them. Heaven held its armies parked behind the "
     "stars — because he asked it to. He was held to that cross by no "
     "nail. He was held there by the same will that spoke in the "
     "council. And when the debt was paid to the last breath:"),
    ("j5", JESUS,
     "It is finished."),
    ("n9", NARRATOR,
     "Finished. Not I am finished — IT is finished. The debt. The "
     "ransom. The distance between you and home. Lucifer's plan would "
     "have saved your body by erasing your soul. The Father's plan "
     "saved the whole person — and this hill is where the bill was "
     "paid."),
    ("n10", NARRATOR,
     "But why couldn't God just forgive — wave it off, skip the cross? "
     "Because justice is real, and mercy cannot rob it. So mercy paid "
     "it. Forgiveness was never God waiving the debt. It was God "
     "eating it."),
    ("n11", NARRATOR,
     "He was laid in a borrowed tomb before sundown, and a great stone "
     "sealed the door. And for about forty hours, the devil believed "
     "he had finally won. Remember that feeling of his. It is about to "
     "become the biggest miscalculation in history."),
]

CARD_SEG = ("card", NARRATOR,
            "Thy will be done was easy in the council. In the garden it "
            "bled. He said it anyway — for you.")

CARD_TEXT = ("He said it anyway.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Nineteen — Thy Will Be Done")

SPOKEN = {"Gethsemane": "geth SEM uh nee"}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="first-century")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The night of nights begins: a narrow path descending among "
        "black olive trunks under a full passover moon, the city's "
        "walls and one or two lamps high behind, the grove ahead "
        "utterly dark and waiting. No figures yet; the path itself "
        "leads the eye down into it.",
        "a moonlit path descending into a black olive grove, city "
        "lamps high behind",
        "figures, torches, stars drawn, text",
        wide=True)),
    ("p02", "n2", _p(
        "Into the press: Jesus at the grove's low gate with eight "
        "shadowed disciples behind him, one lantern among them — his "
        "hand on the gatepost, his face already elsewhere, the olive "
        "dark opening before him. Every face lantern-lit and turned "
        "to him or the trees; none to the lens.",
        "Jesus at the grove gate with lantern-lit disciples behind, "
        "his hand on the post, face already burdened",
        "faces to camera, swords visible, halo",
        jesus=True, ref=True)),
    ("p03", "j1", _p(
        "Sorrowful unto death: Jesus's face close in the lantern's "
        "edge-light — a heaviness on it no frame of this series has "
        "shown before, the eyes dark with an arriving weight, the "
        "mouth steady by will alone. Grief without panic; the face "
        "of a man walking toward the press on purpose.",
        "Jesus's close face carrying unprecedented heaviness with "
        "willed steadiness",
        "tears yet, blood, halo, his eyes on the lens",
        jesus=True, ref=True)),
    ("p04", "n3", _p(
        "A stone's cast further: deeper in the grove, Jesus kneels "
        "alone at a flat shelf of rock in the dark — seen from a "
        "distance through the black trunks, his cream robe the only "
        "light-holding thing in the frame, his friends' lantern a "
        "far spark behind. The world's weight, arriving in an "
        "olive press.",
        "Jesus kneeling alone at a rock shelf seen distantly "
        "through black trunks, robe holding the only light",
        "angels, light from above, his face close",
        jesus=True, ref=True, wide=True)),
    ("p05", "j2", _p(
        "The prayer: Jesus's face upturned in the dark — anguish "
        "fully arrived now, brows drawn upward, eyes wet and open "
        "toward the unseen Father, both hands pressed flat on the "
        "rock shelf before him — agony and surrender in the same "
        "features, with nothing graphic anywhere: the cost is all "
        "in the face.",
        "Jesus's upturned anguished surrendered face, wet open "
        "eyes, hands flat on the rock",
        "blood shown, sweat drops visible, halo, angels",
        jesus=True, ref=True)),
    ("p06", "s1", _p(
        "As it were great drops: extreme close on the night "
        "ground beside the rock — dark heavy droplets striking "
        "the dust and pooling small among the olive roots, each "
        "impact caught in the lantern's far edge-light, the "
        "darkness of the drops ambiguous and terrible. Nothing "
        "else in frame.",
        "dark heavy droplets striking dust and pooling among "
        "olive roots in edge-light, extreme close",
        "wounds, his body, bright red colour, rain",
        )),
    ("p07", "j3", _p(
        "The one firsthand account: the risen Jesus — whole, "
        "calm, glorified — seated on a stone bench in soft "
        "morning light, speaking steadily toward listeners below "
        "the frame, his open hands resting palm-up on his knees "
        "with the small healed marks just visible in each. "
        "Telling, from the other side of it.",
        "the risen Jesus seated calm in soft light, open palm-up "
        "hands with small healed marks, mid-telling",
        "gore at the marks, halo, listeners in frame, his eyes "
        "on the lens",
        jesus=True, ref=True)),
    ("p08", "n7", _p(
        "The kiss: torchlight chaos at the grove's edge — Judas "
        "gripping Jesus's shoulders, his kiss landing on the "
        "cheek, Jesus's face past him already calm and looking "
        "at what comes next; behind them a wall of soldiers' "
        "torches and spear-points crowding the dark. Both "
        "principals in profile; betrayal at its exact instant.",
        "Judas's kiss landing on Jesus's cheek in torchlight, "
        "spear-points crowding behind, Jesus's calm seeing "
        "past him",
        "swords swinging, blood, Peter's ear moment, faces to "
        "camera",
        jesus=True, ref=True)),
    ("p09", ("n7", 0.4), _p(
        "The rigged midnight: Jesus stands bound with cords "
        "before a torch-lit council — seen from behind his "
        "shoulders so the accusers' pointing hands and leaning "
        "shadowed faces fill the frame beyond him, the high "
        "priest's seat above them all. One man silent; a room "
        "of theatre.",
        "bound Jesus from behind facing pointing hands and "
        "leaning shadowed accusers below a high seat",
        "spitting, striking, faces to camera, daylight",
        jesus=True, ref=True)),
    ("p10", ("n7", 0.7), _p(
        "Your hour: Roman soldiers lead him away down a night "
        "street — the file of armored backs and spear-shafts "
        "swallowing the cream-robed figure at their centre, one "
        "torch throwing their long shadows up the shut houses. "
        "All backs to the camera; the darkness has its hour.",
        "a file of soldiers' backs leading the cream-robed "
        "figure away down a torch-shadowed night street",
        "whips, blood, faces, crowds jeering yet",
        jesus=True, ref=True, wide=True)),
    ("p11", "n8", _p(
        "The armies that did not come: straight up into the "
        "night sky over the hill — a vast field of still, "
        "waiting stars, utterly silent, utterly motionless, not "
        "one point of light descending. Twelve legions, parked "
        "behind the stars because the Son asked it. The most "
        "restrained frame in the series.",
        "a vast still star-field over the hill with nothing "
        "descending — heaven's restraint made visible",
        "angels, light shafts, clouds, meteors",
        )),
    ("p12", ("n8", 0.5), _p(
        "The beam: Jesus beneath the rough crossbeam in the "
        "packed street, caught in profile mid-step — the thorn "
        "crown dark on his brow, dust and spent blood-dark "
        "smears kept indistinct, his eyes ahead on the hill — "
        "while the crowd's faces along the walls hold every "
        "human thing: grief, hunger, mockery, awe. None toward "
        "the lens.",
        "Jesus in profile under the crossbeam, thorn crown dark "
        "on his brow, crowd faces of grief and mockery along "
        "the walls",
        "graphic wounds, falling shown, soldiers' whips, faces "
        "to camera",
        jesus=True, ref=True, wide=True)),
    ("p13", ("n8", 0.8), _p(
        "The hill, from far: three crosses raised small against "
        "a bruised storm-lit sky on the bare rise, the two "
        "outer angled slightly toward the centre one, the "
        "watching crowd a dark scatter well down the slope, the "
        "city's walls grey beyond. Distance as reverence; the "
        "event, witnessed the way the sky witnessed it.",
        "three small crosses on a bare rise against bruised "
        "storm light, outer two angled toward the centre, crowd "
        "scattered below",
        "close wounds, faces readable, lightning striking, "
        "titles readable",
        wide=True)),
    ("p14", "j5", _p(
        "It is finished: Jesus's face in profile against the "
        "dark sky — the thorn crown, the upturned last-breath "
        "stillness, the work complete in the features: not "
        "defeat, COMPLETION, the face of a man setting down "
        "something he carried all the way. No wounds in frame; "
        "the sky behind holds its darkest grey.",
        "his thorn-crowned profile upturned in last-breath "
        "completion against darkest grey",
        "blood, the cross beams dominant, mockers, lightning",
        jesus=True, ref=True)),
    ("p15", "n9", _p(
        "The veil tears: inside the temple's holy place, the "
        "great woven veil — floor to ceiling, blue and purple "
        "and scarlet — RIPS from its top downward, the tear "
        "running like lightning through the cloth, two priests "
        "recoiling with lamps in hand as the forbidden inner "
        "dark opens before them. Access, thrown open from "
        "God's side.",
        "the great temple veil tearing from the TOP downward, "
        "recoiling lamp-lit priests, the inner dark opening",
        "hands tearing it, fire, collapse, faces to camera",
        )),
    ("p16", ("n9", 0.6), _p(
        "Beneath the cross: at the rise's foot, Mary and the "
        "young disciple hold each other — her face buried in "
        "his shoulder, his arm locked around her and his "
        "grief-lit face raised toward the cross above the "
        "frame's top edge — the cost counted in the two people "
        "who loved him most. Seen from beside them; the cross "
        "itself stays out of frame.",
        "Mary buried in the young disciple's shoulder, his "
        "raised grieving face, the cross above the frame",
        "the cross in frame, blood, soldiers, faces to camera",
        )),
    ("p17", "n10", _p(
        "The bill, paid: the empty cross at dusk — a leaning "
        "ladder against the upright, the linen sindon draped "
        "soft over the crossbeam's arm, the crowd gone, the "
        "storm rinsed out of a quieting sky. The instrument, "
        "already becoming a relic; the debt, already eaten.",
        "the empty cross at dusk with leaning ladder and draped "
        "linen, crowd gone, sky quieting",
        "bodies, blood, soldiers, mourners",
        )),
    ("p18", "n11", _p(
        "The borrowed tomb: bearers carry the linen-wrapped "
        "form through the low hewn doorway of a garden tomb in "
        "failing light — four men's backs bent under the "
        "gentle weight, myrrh-cloths in a basket by the door, "
        "the rich man's garden dark around. Tender, hurried, "
        "before-sundown.",
        "bearers' backs carrying the linen-wrapped form into a "
        "hewn tomb doorway at dusk, spice basket by the door",
        "the face visible, wailing, soldiers yet",
        )),
    ("p19", ("n11", 0.5), _p(
        "The stone: the great disc of stone rolls the last "
        "hand-width into its channel across the tomb's mouth — "
        "caught at the instant before it seats, the doorway's "
        "last sliver of interior dark disappearing, two "
        "straining shoulders at the stone's edge — the "
        "darkest door-close of the whole series.",
        "the disc stone a hand-width from sealing the tomb "
        "mouth, straining shoulders at its edge, the last "
        "sliver of dark",
        "faces, guards yet, torches, seals",
        )),
    ("p20", ("n11", 0.8), _p(
        "Forty hours: the sealed tomb small in its dark garden "
        "under the night — the stone flush and final, the "
        "olive leaves unmoving, and one cold white star "
        "standing alone over the rise. Stillness that thinks "
        "it is victory. Stillness that is a held breath.",
        "the sealed tomb small in the dark garden under one "
        "cold lone star",
        "guards, light from the tomb, dawn, figures",
        wide=True)),
]
