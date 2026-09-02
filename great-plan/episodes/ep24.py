#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 24: Moroni Alone.

The western hemisphere's fall: two centuries of Zion, the collapse, Cumorah
— and the last covenant keeper finishing a record by firelight, seeing US
across seventeen centuries, and planting the second witness like a seed.
Anchors: 4 Nephi 1:16; Mormon 8:3-5, 35; Moroni 10:27.

Restraint: Cumorah is aftermath at distance — fallen banners and broken
shields, never fields of dead. Mormon's death is a covered form and a
kneeling son (literal-death law: plainly dead, no wounds).
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 324
NUM = 24
SLUG = "moroni-alone"
TITLE = "Moroni Alone"
META = "4 Nephi · Mormon 8 · Moroni 10"

SEGMENTS = [
    ("n1", NARRATOR,
     "While the old world drifted into its long twilight, the other "
     "hemisphere fell off a cliff. This is the loneliest chapter in "
     "scripture — and one of the bravest."),
    ("n2", NARRATOR,
     "Remember what the Nephites had. The risen Christ had walked their "
     "streets. And after he left came two hundred years of actual Zion — "
     "no poor, no classes, no war, all things common among them."),
    ("s1", SCRIPTURE,
     "And surely there could not be a happier people among all the "
     "people who had been created by the hand of God."),
    ("n3", NARRATOR,
     "Two centuries of the happiest people God ever made. And then pride "
     "crept back. Fine clothes. Classes. Old grudges, renamed. And out "
     "of the dark, within living memory of paradise, the secret "
     "combinations came back."),
    ("n4", NARRATOR,
     "It ended at a hill called Cumorah — the last battle of a "
     "thousand-year civilization. Hundreds of thousands fell, and the "
     "prophet-general Mormon fell with them. When the smoke cleared, "
     "one covenant keeper was left standing on the continent."),
    ("s2", SCRIPTURE,
     "And my father also was killed by them, and I even remain alone to "
     "write the sad tale of the destruction of my people."),
    ("s3", SCRIPTURE,
     "I have not friends nor whither to go; and how long the Lord will "
     "suffer that I may live I know not."),
    ("n5", NARRATOR,
     "Moroni. Son of Mormon. The last believer of a dead nation — "
     "hunted, homeless, and carrying the thousand-year record of God's "
     "dealings with his people."),
    ("n6", NARRATOR,
     "And what does the loneliest man in history do with the record of "
     "the people who broke his heart? He does not burn it. He finishes "
     "it. Alone, for years, he abridges, copies in his father's "
     "letters, and writes his farewell."),
    ("n7", NARRATOR,
     "And in that farewell he does something astonishing. He writes to "
     "US — and explains how he can:"),
    ("s4", SCRIPTURE,
     "Behold, I speak unto you as if ye were present, and yet ye are "
     "not. But behold, Jesus Christ hath shown you unto me, and I know "
     "your doing."),
    ("n9", NARRATOR,
     "Then he sealed the record, carried the plates to a hill the Lord "
     "showed him, and buried them in a stone box. The second witness — "
     "planted like a seed with a timer, addressed to a world that would "
     "one day need proof the heavens were never closed."),
    ("n10", NARRATOR,
     "The devil, watching, believed he now held both hemispheres. Keys "
     "gone in the east. A dead church, a dead nation, and a book in the "
     "ground in the west. Say his miscalculation with me one more time: "
     "a buried record is not a corpse. It is a seed."),
    ("n11", NARRATOR,
     "And Moroni's last written words to you, before the dirt closed "
     "over the box, were an appointment:"),
    ("s5", SCRIPTURE,
     "Ye shall see me at the bar of God; and the Lord God will say unto "
     "you: Did I not declare my words unto you, which were written by "
     "this man?"),
]

CARD_SEG = ("card", NARRATOR,
            "The last man of a dead nation wrote to you by firelight — "
            "and buried the letter where you would find it.")

CARD_TEXT = ("He saw you.\n"
             "He wrote to you.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Twenty-Four — Moroni Alone")

SPOKEN = {"US": "us"}

MORONI = (
    "MORONI LOCK: the same man as the attached reference in every "
    "picture — the last Nephite: mid-forties and weathered far older, "
    "deep bronze skin, black hair grey-shocked at the temples pulled "
    "back, a short war-worn beard, battered bronze-scaled armor pieces "
    "under a heavy travel-stained grey-green cloak, a plain sword kept "
    "but never drawn. Grief carried like armor; eyes that have seen "
    "everything end and still believe. No halo, no glow.")

LOCKS = {"MORONI-GP": MORONI}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="ancient")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The other hemisphere darkens: a storm front swallowing the "
        "jungle-green hills behind a stepped stone temple city at dusk — "
        "the first rain-curtains dragging across the far pyramids, the "
        "plaza lamps guttering below, the light failing from the east "
        "inward. The same skyline the risen Christ once filled, going "
        "dark. No close figures.",
        "a storm front swallowing a stepped temple city's hills at "
        "dusk, plaza lamps guttering",
        "lightning bolts, battle, crowds close, ruins yet",
        wide=True)),
    ("p02", "n2", _p(
        "Zion, two centuries of it: the temple plaza at golden evening "
        "filled with LONG COMMON TABLES — families of every age sharing "
        "heaped food, children weaving between benches, an old man "
        "laughing with a toddler on his knee, baskets passing hand to "
        "hand down the boards — abundance with no head seat anywhere. "
        "Camera at table height past shoulders.",
        "long common tables of shared abundance in a golden temple "
        "plaza, all ages mingled, baskets passing",
        "beggars, guards, coins, faces to camera",
        wide=True)),
    ("p03", "s1", _p(
        "The happiest people: at dusk in the plaza, children dance in a "
        "ring around a fire while the old people clap the rhythm from "
        "benches — bare feet mid-skip, braids flying, wide toothless "
        "grins among the clappers, firelight warm on every joined "
        "generation. Joy with no asterisk.",
        "children mid-dance around a fire ringed by clapping elders at "
        "dusk, joy unqualified",
        "performers, idols, wine, faces to camera",
        )),
    ("p04", "n3", _p(
        "Pride creeps back: a market lane split down its middle — on "
        "one side, a group in embroidered robes and feathered "
        "ornaments walking with chins lifted, eyes forward; on the "
        "other, patched-tunic families drawing aside with lowered "
        "heads to let them pass. The first daylight between neighbors "
        "in two hundred years, visible as body language alone.",
        "fine-robed chins-up group passing patched families who draw "
        "aside with lowered heads, a lane dividing",
        "violence, coins, sneering theatrics, faces to camera",
        )),
    ("p05", ("n3", 0.6), _p(
        "The franchise returns: in a night hollow below the city "
        "walls, men kneel again in a silent ring around one low red "
        "fire — the same wrong-sacred order from the days of Cain, "
        "shadows spoking up the hollow's sides, heads bowed, no face "
        "visible. Seen from the hollow's rim. The oldest business, "
        "reopening.",
        "a kneeling night ring around one low red fire in a hollow, "
        "shadows spoking, seen from the rim",
        "faces visible, torches, masks, any non-human shape",
        wide=True)),
    ("p06", "n4", _p(
        "Cumorah, after: the great hill at dusk under a smoke-hazed "
        "sky — and scattered small across its darkening slopes, the "
        "END of a civilization told in objects: fallen banners "
        "leaning, broken round shields face-down, a war-drum on its "
        "side — no bodies visible at this reverent distance, carrion "
        "birds turning high and far. Stillness where a nation "
        "stood.",
        "the dusk hill scattered with fallen banners, face-down "
        "shields and a tipped war-drum, high distant birds — no "
        "bodies",
        "corpses, blood, weapons in hands, fire",
        wide=True)),
    ("p07", ("n4", 0.6), _p(
        "The general falls: Moroni kneels beside a form covered "
        "completely by a commander's mantle — his father, plainly "
        "beyond waking beneath the cloth — the son's head bowed onto "
        "one fist, his other hand resting on the covered shoulder, "
        "his battered armor dark in the failing light. No wound, no "
        "face, no doubt.",
        "Moroni kneeling head-on-fist beside a fully mantle-covered "
        "form, hand on the covered shoulder",
        "any visible body part, blood, weapons drawn, his face "
        "clear",
        locks=["MORONI-GP"])),
    ("p08", "s2", _p(
        "I even remain alone: Moroni stands on the emptied slope at "
        "grey dawn, seen full-length from behind — the field of "
        "fallen banners running away below him into the mist, his "
        "cloak pulling in the wind, the last upright figure of a "
        "thousand-year story. Nothing else moves.",
        "Moroni from behind, the lone upright figure over a misted "
        "slope of fallen banners at grey dawn",
        "bodies, birds close, his face, fires",
        wide=True, locks=["MORONI-GP"])),
    ("p09", "s3", _p(
        "Nor whither to go: high wilderness — Moroni walks a bare "
        "ridge line small against enormous peaks, the wrapped bundle "
        "of plates roped high on his back, walking away from the "
        "camera into country with no roads and no one left to meet. "
        "Grand, cold, and utterly alone.",
        "tiny Moroni from behind on a bare ridge with the wrapped "
        "bundle high on his back, enormous empty peaks",
        "trails, smoke, animals, any other figure",
        wide=True, locks=["MORONI-GP"])),
    ("p10", "n6", _p(
        "He finishes it: deep in a dry cave by firelight, Moroni "
        "bends over the plates on a flat stone — stylus mid-stroke, "
        "his armor stacked neatly against the wall behind him, his "
        "beard longer and greyer than the battle left it — a son "
        "keeping his father's table through the years alone. The "
        "strokes on the metal stay unreadable.",
        "Moroni mid-engraving by cave firelight, armor stacked "
        "behind, visibly aged, unreadable strokes",
        "readable characters, his eyes on the lens, treasure",
        locks=["MORONI-GP"])),
    ("p11", ("n6", 0.5), _p(
        "The years pass: the same cave mouth from outside in deep "
        "winter — snow banked on the ledge, bare trees cracking "
        "under frost, and from the dark opening one faint warm "
        "breath of firelight. Time, doing its slow work around a "
        "man who will not stop writing. No figure visible.",
        "the snow-banked cave mouth in winter with one faint warm "
        "fire-breath from the dark",
        "footprints fresh, smoke column, figures",
        )),
    ("p12", "s4", _p(
        "He sees us: Moroni's face lifts from the plates in the "
        "firelight — eyes gone wide and bright, looking clean "
        "through the cave wall and seventeen centuries, the stylus "
        "forgotten in his hand — the expression of a man being "
        "shown the faces of the people he is writing to. Gaze past "
        "the camera's shoulder, never at it.",
        "Moroni's lifted firelit face seeing through time, stylus "
        "forgotten, gaze past the lens",
        "his eyes on the lens, visions in frame, tears yet",
        locks=["MORONI-GP"])),
    ("p13", ("s4", 0.6), _p(
        "What he was shown: a present-day crosswalk in long golden "
        "light — the stream of ordinary people mid-stride, faces "
        "away and in profile, bags and jackets and hurry — the "
        "exact people a dying nation's last man was allowed to "
        "see. Us, from his side of the fire.",
        "an ordinary golden-hour crosswalk stream, faces away and "
        "in profile",
        "anyone facing the lens, readable signs, brand marks",
        era="modern", wide=True)),
    ("p14", ("n7", 0.5), _p(
        "Writing to you: extreme close on the stylus point moving "
        "across the metal — and one bright tear striking the "
        "plate's engraved surface beside the working hand, "
        "catching the firelight as it lands among the unreadable "
        "characters. A letter, salted the way real ones are.",
        "a stylus mid-stroke and one tear landing bright on the "
        "engraved plate, extreme close",
        "readable characters, blood, faces",
        )),
    ("p15", "n9", _p(
        "The seed, planted: the fitted stone lid SLIDES closed "
        "over the ring-bound plates in their buried box — caught "
        "at the last hand-width of gleam before the dark takes "
        "them, Moroni's two hands guiding the stone, tree roots "
        "at the cut earth's edge. The same box, the same hill, "
        "the timer set.",
        "a stone lid at the last hand-width of closing over the "
        "gleaming plates, two guiding hands, rooted earth",
        "faces, treasure, angels, light from the box",
        locks=["MORONI-GP"])),
    ("p16", ("n9", 0.6), _p(
        "The ground closes: Moroni's hands press the last of the "
        "dark soil over the spot and lay wild leaf-litter across "
        "it — the hillside made seamless again under his careful "
        "palms, indistinguishable from every other yard of "
        "forest floor. Hidden in plain earth for exactly as long "
        "as it takes.",
        "hands pressing soil and laying leaf-litter over the "
        "hidden spot, seamless forest floor",
        "markers, mounds, tools, faces",
        locks=["MORONI-GP"])),
    ("p17", "n10", _p(
        "The miscalculation: on that same forest floor, seasons "
        "later — a single green SHOOT stands up through the "
        "leaf-litter exactly where the palms pressed, morning "
        "light finding it through the canopy, dew on its two "
        "small leaves. A seed, doing what seeds do. No people.",
        "one green shoot through leaf-litter in found morning "
        "light, dew on two leaves",
        "the box visible, markers, figures, drawn rays",
        )),
    ("p18", "s5", _p(
        "The appointment: Moroni aged and at peace stands at the "
        "cave mouth in first light — hands empty now, the bundle "
        "gone from his back, his face lifted into the morning "
        "with the settled look of a man whose work is delivered "
        "and whose appointment is made. The wilderness beyond "
        "him is just wilderness again.",
        "aged Moroni empty-handed at the cave mouth, face lifted "
        "and at peace in first light",
        "plates, sword drawn, his eyes on the lens, angels",
        locks=["MORONI-GP"])),
    ("p19", ("s5", 0.7), _p(
        "The hill keeps the appointment: the wooded drumlin hill "
        "under a vast night of stars once more — the seed below, "
        "the timer running, the same patient sky that has watched "
        "every era of this story lean toward morning. No people, "
        "no marks.",
        "the drumlin hill under a vast star field, patient and "
        "unmarked",
        "figures, lights, meteors, text",
        wide=True, era="america-1820")),
]
