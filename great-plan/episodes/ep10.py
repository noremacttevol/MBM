#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 10: Master Mahan.

The first murder as a ceremony: Cain's covenant with darkness, the birth of
secret combinations, and how to tell covenants of light from covenants that
devour. Anchors: Moses 5:18-33; Helaman 6:26-30.

Restraint laws: Abel is shown plainly DEAD (never asleep) with no wounds,
blood or impact shown. The devil is a voice; Cain swears alone into empty
darkness.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 310
NUM = 10
SLUG = "master-mahan"
TITLE = "Master Mahan"
META = "Moses 5 · Helaman 6"

SEGMENTS = [
    ("n1", NARRATOR,
     "The first murder on earth was not a crime of passion. It was the "
     "devil's move — a ceremony. See him build it, and every dark "
     "headline since reads differently."),
    ("n2", NARRATOR,
     "Cain and Abel — sons of Adam, both raised on the first gospel. "
     "Abel offered the firstlings of his flock, as taught: a lamb, "
     "pointing to the Lamb. Cain brought an offering on his own terms — "
     "and scripture says he brought it at the devil's suggestion."),
    ("s1", SCRIPTURE,
     "But unto Cain, and to his offering, he had not respect. Now Satan "
     "knew this, and it pleased him."),
    ("n3", NARRATOR,
     "Why was Cain's offering refused? Not because God dislikes the work "
     "of a farmer's hands. Because the offering was the SIGN — the lamb "
     "pointed to Christ. Cain redesigned the ordinance, and then raged "
     "when heaven would not bless the redesign."),
    ("n4", NARRATOR,
     "And in that rage, Cain did something no one on earth had ever "
     "done. He made a deal."),
    ("d1", DEVIL,
     "Swear unto me by thy throat, and if thou tell it thou shalt die; "
     "and swear thy brethren by their heads, and by the living God, that "
     "they tell it not... and this day I will deliver thy brother Abel "
     "into thine hands."),
    ("n5", NARRATOR,
     "Secrecy, sworn on his own throat. Loyalty ranked above conscience. "
     "Murder, traded for advantage. And then the title — because Cain, "
     "God help him, was proud of the deal:"),
    ("s2", SCRIPTURE,
     "And Cain said: Truly I am Mahan, the master of this great secret, "
     "that I may murder and get gain."),
    ("n7", NARRATOR,
     "Abel died in a field, at his brother's hand. Scripture does not "
     "flinch, and neither will we: the first family buried a murdered "
     "son. And his blood cried to God from the ground."),
    ("n8", NARRATOR,
     "The combination Cain founded did not die with him. Scripture "
     "tracks it down the centuries — and names exactly what keeps it "
     "alive:"),
    ("s3", SCRIPTURE,
     "And behold, it is he who is the author of all sin. And behold, he "
     "doth carry on his works of darkness and secret murder, and doth "
     "hand down their plots, and their oaths, and their covenants, and "
     "their plans of awful wickedness, from generation to generation."),
    ("n10", NARRATOR,
     "Why show you something this dark? Because the war has structure on "
     "both sides. God builds covenants that exalt. The devil builds "
     "covenants that devour. And you can tell them apart with one "
     "question: does this bond ask me to hide — or does it let me stand "
     "in the light?"),
    ("n11", NARRATOR,
     "The family of Adam survived its darkest day, and kept the altar "
     "burning. So can yours. And every oath of darkness ever sworn is "
     "outranked by one drop of the blood the lamb was pointing to all "
     "along."),
]

CARD_SEG = ("card", NARRATOR,
            "Covenants of light exalt. Covenants of darkness devour. Know "
            "them apart by what they ask you to hide.")

CARD_TEXT = ("One asks you to hide.\n"
             "One lets you stand in light.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Ten — Master Mahan")

SPOKEN = {"Mahan": "mah HAHN"}

CAIN = (
    "CAIN LOCK: the same man in every picture — Adam's eldest son in his "
    "early thirties, heavy-browed and powerfully built, warm olive-brown "
    "skin like his father's, thick black hair cropped shorter than Adam's "
    "and a short dense black beard, wearing a farmer's rough dark-brown "
    "woven tunic. Intelligent, proud, storm-browed. No halo, no glow.")

LOCKS = {"CAIN": CAIN}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="ancient")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "A grain field before dawn, uneasy: standing barley moving in a "
        "low wind under a grey-violet sky, mist lying between the rows, "
        "the light not yet decided — beautiful and wrong at once, like "
        "held breath. No people.",
        "a pre-dawn barley field in low wind and lying mist, uneasy "
        "stillness",
        "figures, birds, buildings, storm drama",
        wide=True)),
    ("p02", "n2", _p(
        "Two altars, two smokes: on the offering hill, Abel's altar "
        "burns clean — its smoke rising in one straight bright column — "
        "while a stone's throw away Cain's altar of heaped produce "
        "smoulders, its smoke crawling low and sideways along the "
        "ground. The two smoke behaviours share one frame, morning "
        "light hard between them. The brothers stand small, each by "
        "his own altar, faces away.",
        "one straight bright smoke column and one low crawling smoke "
        "in the same frame, a small figure by each altar",
        "faces readable, flames huge, darkness overhead",
        wide=True, locks=["CAIN"])),
    ("p03", ("n2", 0.6), _p(
        "Jealousy hardening: Cain's face in close three-quarter, lit "
        "from the side by his brother's distant bright fire while his "
        "own smoke drags grey across the frame's lower edge — his eyes "
        "fixed off-frame on the straight column he did not get, the "
        "muscles of his jaw setting like mortar.",
        "Cain's close three-quarter face hardening, lit by a distant "
        "brightness he stares at off-frame",
        "his eyes on the lens, tears, snarling, any figure behind "
        "him",
        locks=["CAIN"])),
    ("p04", "s1", _p(
        "The refusal, felt: Cain kneels before his cold smouldering "
        "altar with both fists pressed on his knees, head dropped — "
        "and beyond him, out of focus, Abel's column still climbs "
        "bright and untroubled. The frame's far corner holds a faint "
        "COLD tinge in the air, formless, pleased. Camera at his "
        "side; his face is hidden by the drop of his head.",
        "Cain fist-kneeling before cold smoulder, Abel's bright "
        "column soft beyond, a faint formless cold tinge at one "
        "corner",
        "any shape in the cold tinge, his face visible, lightning",
        devil=True, locks=["CAIN"])),
    ("p05", "n4", _p(
        "Toward the voice: Cain walks alone into the mouth of a dark "
        "ravine at dusk, seen full-length from directly behind, his "
        "figure small between rising rock walls that swallow the "
        "evening light ahead of him — the darkness he walks toward "
        "empty and total, without any shape in it.",
        "Cain from directly behind entering a dark empty ravine "
        "mouth at dusk",
        "any figure or eyes in the dark ahead, his face, torches",
        devil=True, locks=["CAIN"])),
    ("p06", "d1", _p(
        "The oath: deep in the ravine dark, Cain's own right hand is "
        "pressed flat against his own throat — the literal gesture of "
        "the words — his face half-swallowed by shadow, the visible "
        "half hollow-eyed and lit only by the last grey light from "
        "above, his gaze aimed into the empty blackness before him "
        "where no one stands.",
        "Cain's hand flat on his own throat, half-shadowed hollow "
        "face aimed into empty blackness",
        "any second figure, eyes or shape in the black; underlight "
        "from below; his eyes on the lens",
        devil=True, locks=["CAIN"])),
    ("p07", "n5", _p(
        "Mahan walks out: Cain strides out of the ravine mouth in "
        "hard profile, changed — spine straight, jaw set, eyes "
        "forward and cold, the dusk behind him and his shadow thrown "
        "long ahead of him across the stones by the risen moon.",
        "Cain in hard profile striding from the ravine, long "
        "moon-shadow thrown ahead",
        "his eyes on the lens, weapons, any figure behind",
        locks=["CAIN"])),
    ("p08", "s2", _p(
        "The franchise opens: at a small night fire away from the "
        "camp, Cain leans in with his right hand raised in a "
        "teaching oath-gesture toward two younger kinsmen who lean "
        "close, firelight on three conspiring faces, every gaze "
        "locked on Cain's raised hand — the first initiation. "
        "Camera outside the huddle; no face toward the lens.",
        "Cain's raised oath-hand over a leaning firelit huddle of "
        "two initiates, camera outside the circle",
        "faces to camera, knives visible, documents",
        locks=["CAIN"])),
    ("p09", ("s2", 0.55), _p(
        "The dark mirror: in a night hollow below the bluffs, nine "
        "men kneel in a silent ring around one low red fire, heads "
        "bowed in wrong-sacred order, their shadows spoking outward "
        "up the hollow's walls — organized, reverent, and aimed at "
        "nothing holy. Seen from the hollow's rim looking down; "
        "every head bowed, no face visible.",
        "nine men kneeling in a ring around one low red fire in a "
        "night hollow, shadows spoking outward, seen from the rim",
        "faces visible, torches, animal masks, any non-human "
        "shape",
        wide=True)),
    ("p10", "n7", _p(
        "The field, after: wide at dusk — Abel lies UNMOVING in the "
        "trampled barley, one arm outflung, his herdsman's staff "
        "fallen a stride away, his face turned from the camera into "
        "the stalks; near him a single dropped fieldstone, dark "
        "side down. Crows lift from the far rows into a bruised "
        "sky. No wound or blood is visible — and nothing about the "
        "stillness reads as sleep: this man is gone.",
        "Abel plainly dead in trampled grain — outflung arm, "
        "fallen staff, dropped stone, lifting crows — no wounds "
        "shown",
        "blood, wounds, Cain in frame, a peaceful sleeping pose",
        wide=True)),
    ("p11", ("n7", 0.5), _p(
        "The first grave: Adam and Eve at a fresh stone-covered "
        "mound at sundown — Eve collapsed sideways into Adam's "
        "chest, her fist gripping his tunic, his arms locked around "
        "her and his broken face lifted to the sky — both in "
        "profile, the mound small and terrible before them.",
        "Eve collapsed into Adam at a fresh stone mound, his "
        "broken face lifted, profiles at sundown",
        "faces to camera, the body, wailing crowds",
        locks=["ADAM", "EVE"])),
    ("p12", ("n7", 0.8), _p(
        "Heaven answers the ground: rain begins over the fresh "
        "mound in near-darkness — the first heavy drops striking "
        "the stacked stones and the raw earth, bouncing bright in "
        "what little light is left, the field blurred grey beyond. "
        "The sky itself weeping onto the grave. No people.",
        "first heavy raindrops striking a fresh stone mound in "
        "near-dark, sky weeping",
        "figures, lightning, flowers, text",
        )),
    ("p13", "n8", _p(
        "Handed down: by a guttering lamp in a mud-walled room, an "
        "old man leans to whisper into a young man's ear — the "
        "elder's hand pressing a small heavy pouch into the young "
        "one's palm between them — both faces in shadowed profile, "
        "the young man's eyes wide with the weight of what he is "
        "receiving.",
        "an elder whispering into a young man's ear over a pressed "
        "pouch, shadowed profiles, guttering lamp",
        "faces to camera, knives, readable marks",
        )),
    ("p14", "s3", _p(
        "The franchise, centuries on: cloaked men stand in a torch-"
        "lit slot canyon at night, right hands raised together over "
        "a low fire in a sworn ring — a dozen of them, faces "
        "shadowed under drawn cowls or turned to the fire, the "
        "canyon walls climbing black above the torchlight. Ancient "
        "American robber-band iron and leather; nothing modern.",
        "a torch-lit ring of cloaked men with right hands raised "
        "in oath over a low fire in a slot canyon",
        "faces clearly visible, banners, readable symbols, any "
        "non-human shape",
        wide=True)),
    ("p15", ("s3", 0.6), _p(
        "The same franchise, today: a dark modern back room — neat "
        "banded stacks of unmarked cash on a steel table beside a "
        "matte-black handgun and a burner phone, one hard task-lamp "
        "throwing them into relief, the rest of the room falling to "
        "black. No people; the tools say everything.",
        "banded cash, a handgun and a phone under one hard lamp on "
        "a steel table, room falling to black",
        "any person, brand marks, readable serials or screens, "
        "drugs",
        era="modern")),
    ("p16", "n10", _p(
        "Covenants of light: two work-worn hands clasped over an "
        "open family book of scripture at a bright wooden table, "
        "morning window light across the pages and the joined "
        "hands — a bond with nothing to hide, close and warm. The "
        "page's print stays soft and unreadable.",
        "two clasped hands over open scripture in bright morning "
        "window light",
        "readable text, faces, jewellery prominent, dimness",
        )),
    ("p17", ("n10", 0.55), _p(
        "Leaving the hidden thing: a man steps out of a dim "
        "doorway into full daylight on a present-day street, seen "
        "from behind at the threshold — the room behind him "
        "falling to shadow, the street ahead ordinary and bright, "
        "his shoulders dropping with the first free breath.",
        "a man from behind stepping from a dim doorway into "
        "ordinary bright daylight",
        "his face, signage, brand marks, anyone else",
        era="modern")),
    ("p18", "n11", _p(
        "The altar still burns: the first family gathered at the "
        "hilltop altar in morning light again — fewer, and "
        "wounded, and STANDING: Adam's arm around Eve, the "
        "children close, the offering smoke rising straight — "
        "seen from behind the family half-circle, the valley "
        "bright beyond.",
        "the smaller family standing close at the burning altar, "
        "straight smoke, seen from behind",
        "faces to camera, graves in frame, darkness",
        wide=True, locks=["ADAM", "EVE"])),
    ("p19", ("n11", 0.6), _p(
        "What it all pointed to: a living lamb standing calm in "
        "morning light beside the altar stones, wool bright, dark "
        "eyes gentle — close, quiet, and completely at peace. The "
        "answer to every oath of darkness, breathing.",
        "a calm living lamb close beside altar stones in morning "
        "light",
        "ropes, blood, distress, people",
        )),
]
