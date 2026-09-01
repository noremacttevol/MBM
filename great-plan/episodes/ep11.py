#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 11: The God Who Weeps.

Enoch's Zion taken up — and the two faces of the war: the devil laughing
over the chain, and the God of heaven weeping over His children.
Anchors: Moses 7:18-37, 69.

Devil Law: the "great chain" is rendered as a serpentine band of formless
darkness veiling the earth — no holder, no figure, ever. The laugh lives in
the devil's VOICE domain only (narration); nothing laughs on screen.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 311
NUM = 11
SLUG = "god-who-weeps"
TITLE = "The God Who Weeps"
META = "Moses 7"

SEGMENTS = [
    ("n1", NARRATOR,
     "There is a scene in scripture where the devil laughs and God "
     "cries. If your picture of the universe has those two reversed — a "
     "cold heaven and a charming adversary — this episode turns it right "
     "side up."),
    ("n2", NARRATOR,
     "Enoch. Seventh from Adam. A slow-of-speech young man God called to "
     "preach to a world sliding into violence. And against everything, "
     "people listened."),
    ("n3", NARRATOR,
     "They listened so well that something happened which has only "
     "happened a handful of times in the history of this world. A whole "
     "city aligned itself with heaven."),
    ("s1", SCRIPTURE,
     "And the Lord called his people Zion, because they were of one "
     "heart and one mind, and dwelt in righteousness; and there was no "
     "poor among them."),
    ("n5", NARRATOR,
     "And that city grew so aligned that God did the astonishing thing. "
     "He took it. The whole city."),
    ("s2", SCRIPTURE,
     "And Enoch and all his people walked with God, and he dwelt in the "
     "midst of Zion; and it came to pass that Zion was not, for God "
     "received it up into his own bosom; and from thence went forth the "
     "saying, Zion is fled."),
    ("n6", NARRATOR,
     "Zion is fled. But before it left, Enoch was shown the rest of the "
     "world — and two faces of the war that he never forgot."),
    ("n7", NARRATOR,
     "First, the enemy's face. Scripture's own words:"),
    ("s3", SCRIPTURE,
     "And he beheld Satan; and he had a great chain in his hand, and it "
     "veiled the whole face of the earth with darkness; and he looked up "
     "and laughed, and his angels rejoiced."),
    ("n8", NARRATOR,
     "Laughing. At human misery. That is who he is when nobody dresses "
     "him up. Not a gentleman negotiator. Not a misunderstood rebel. A "
     "jailer — delighted by the chain."),
    ("n9", NARRATOR,
     "Then Enoch turned, and saw the other face. The God of heaven — the "
     "most powerful Being in existence — looking at the very same earth. "
     "And God was weeping."),
    ("s4", SCRIPTURE,
     "The God of heaven looked upon the residue of the people, and he "
     "wept; and Enoch bore record of it, saying: How is it that the "
     "heavens weep, and shed forth their tears as the rain upon the "
     "mountains?"),
    ("n10", NARRATOR,
     "Enoch was stunned. You? Weep? And God explained — in words that "
     "should end every cold theology forever:"),
    ("g1", FATHER,
     "Satan shall be their father, and misery shall be their doom; and "
     "the whole heavens shall weep over them, even all the workmanship "
     "of mine hands; wherefore should not the heavens weep, seeing these "
     "shall suffer?"),
    ("n11", NARRATOR,
     "A God who weeps is a God who feels what your choices cost you — a "
     "Father whose power never once numbed His heart. The devil laughs, "
     "because pain is his win condition. God weeps, because pain is His "
     "children hurting. Hear it and never forget it: you have never "
     "suffered unnoticed. Not once."),
]

CARD_SEG = ("card", NARRATOR,
            "The devil laughed at the chain. God wept over it. Never "
            "confuse the two again.")

CARD_TEXT = ("One laughed. One wept.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Eleven — The God Who Weeps")

SPOKEN = {}

ENOCH = (
    "ENOCH LOCK: the same man as the attached reference in every picture — "
    "a prophet in his vigorous middle years, warm brown skin, strong "
    "gentle features, black hair flecked with early silver falling to his "
    "shoulders, a full dark beard, wearing a plain undyed grey-brown wool "
    "mantle over a rough tunic, carrying a plain shepherd's staff. Humble, "
    "fearless, tender-eyed. No halo, no glow.")

LOCKS = {"ENOCH-GP": ENOCH}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="ancient")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The two moods of one world: from a high ridge, a great valley "
        "half-covered by the hard shadow of an unseen cloud bank and "
        "half in full warm morning light — the boundary between them a "
        "single soft line moving across the fields. No figures; the "
        "frame itself is the question of the episode.",
        "one valley split between hard cloud-shadow and warm light by "
        "a single soft moving boundary",
        "storms, lightning, figures, any shape in the shadow",
        wide=True)),
    ("p02", "n2", _p(
        "The call: Enoch stands ankle-deep at a river ford at first "
        "light, staff in one hand, his other hand pressed flat over "
        "his chest, face lifted in three-quarter toward the brightening "
        "sky — the posture of a man hearing his name and doubting his "
        "own tongue. Willows and mist behind him.",
        "Enoch at a misted ford, hand flat on chest, lifted "
        "three-quarter face, staff in hand",
        "his eyes on the lens, halo, scrolls, crowds",
        locks=["ENOCH-GP"])),
    ("p03", ("n2", 0.6), _p(
        "And they listened: Enoch preaching from a rock shelf above a "
        "gathered crowd — his arm sweeping wide mid-sentence, mantle "
        "lifting in the wind — seen from behind and among the crowd's "
        "heads and shoulders so his small commanding figure holds the "
        "frame's top, every listening head aimed up at him.",
        "Enoch mid-gesture on a rock shelf seen past the crowd's "
        "heads, every head aimed up at him",
        "faces to camera, banners, weapons among the crowd",
        wide=True, locks=["ENOCH-GP"])),
    ("p04", "n3", _p(
        "A city aligning with heaven: a walled hill-city at golden "
        "hour with its gates thrown open — streams of people moving IN "
        "together carrying shared harvest baskets, herds funnelling "
        "peacefully, cook-smoke rising from a hundred roofs into the "
        "gold — abundance flowing toward each other, not away. Seen "
        "from the fields below the gate road.",
        "an open-gated golden hill-city with people streaming in "
        "carrying shared harvest",
        "guards, weapons, beggars at the gate, faces to camera",
        wide=True)),
    ("p05", "s1", _p(
        "No poor among them: in the city's market square, a richly-"
        "dressed older merchant lays two round loaves and a wrapped "
        "cheese into the arms of a young mother whose small daughter "
        "grips her skirt — and BOTH adults are smiling in profile, "
        "equals in the exchange, no bow, no shame, morning light "
        "across the stalls.",
        "a merchant laying bread into a young mother's arms, both "
        "profiles smiling as equals, child at her skirt",
        "grovelling, coins, faces to camera, pity theatrics",
        )),
    ("p06", ("s1", 0.6), _p(
        "One heart, one evening: a lamplit courtyard filled with "
        "three generations — old men and small children on the same "
        "benches, mothers with babies, young men — every face turned "
        "to the centre where unseen singing rises, mouths open in the "
        "same song, warm light on every different face. Camera at the "
        "courtyard's edge past a shoulder.",
        "a lamplit courtyard of all generations singing together, "
        "every face into the shared centre",
        "instruments prominent, faces to camera, revelry",
        )),
    ("p07", "s2", _p(
        "Zion received: the whole hill-city stands wrapped in a "
        "column of brilliance reaching from its walls up beyond the "
        "top of the frame — the light EVEN and vast, the city's "
        "towers and roofs still visible inside it like shapes in "
        "bright mist, the fields below rolling with ground-fog away "
        "from the hill. Witnessed from the far fields; no figures "
        "near the camera.",
        "the entire hill-city standing inside one vast even column "
        "of brightness, ground-fog rolling from the hill",
        "the city tilting or flying, people visible rising, drawn "
        "rays, beams with hard edges",
        wide=True)),
    ("p08", "n6", _p(
        "Zion is fled: the hilltop the morning after — empty clean "
        "terraces where streets were, doorstone thresholds opening "
        "onto nothing, dew bright on the bare foundations, a flight "
        "of birds circling the crown of the hill where the temple "
        "square stood. Absence shaped exactly like a city. No "
        "people.",
        "an empty terraced hilltop of clean thresholds and "
        "foundations shaped like a vanished city, circling birds",
        "ruins, burn marks, collapse, any figure",
        wide=True)),
    ("p09", ("n6", 0.55), _p(
        "Enoch shown the world: Enoch stands on a bare mountain "
        "summit at the edge of an immense drop, seen from behind, "
        "his mantle streaming — and before him the whole curve of "
        "the world lies open under moving cloud and light, kingdoms "
        "of distance in one look. The vision's vantage.",
        "Enoch from behind on a summit edge before the open curving "
        "world",
        "his face, angels, drawn light, text",
        wide=True, locks=["ENOCH-GP"])),
    ("p10", "s3", _p(
        "The chain: from the summit vantage, the world below being "
        "VEILED — a vast serpentine BAND of darkness winding across "
        "the lands like a chain laid over the earth, link-thick and "
        "creeping, its darkness formless within, no holder, no hand, "
        "no figure anywhere — only the lit lands ahead of it and the "
        "swallowed lands behind it.",
        "a vast chain-like serpentine band of formless darkness "
        "winding across the world below",
        "ANY hand, arm, figure or face at or in the band; metal "
        "links literal; lightning",
        wide=True, devil=True)),
    ("p11", ("s3", 0.6), _p(
        "Hearing the laugh: Enoch's face close in three-quarter, "
        "lit cold from the darkened world below the frame — horror "
        "and grief fighting in his features, his knuckles white on "
        "the staff, eyes fixed down on what the frame does not "
        "show.",
        "Enoch's close three-quarter face in cold uplight of grief "
        "and horror, white-knuckled on his staff",
        "his eyes on the lens, tears yet, any dark shape in frame",
        devil=True, locks=["ENOCH-GP"])),
    ("p12", "n8", _p(
        "The jailer's delight: closer on the world below — the dark "
        "band tightening around one small lamplit village in a "
        "valley, its warm windows the last bright thing as the "
        "formless dark closes the ring — no figure in the darkness, "
        "only the shrinking warmth and the creeping cold.",
        "a ring of formless darkness tightening around one lamplit "
        "village's last warm windows",
        "any figure, eyes or mouth in the dark; flames; screaming "
        "people",
        devil=True)),
    ("p13", "n9", _p(
        "The turn: Enoch turns from the dark vista toward a warmth "
        "flooding from the frame's other side — caught mid-turn in "
        "profile, the cold light dying on one side of his face as "
        "the warm takes the other, his eyes widening at what waits "
        "in the brightness the camera does not yet show.",
        "Enoch mid-turn in profile between cold light and arriving "
        "warmth, eyes widening",
        "his eyes on the lens, any figure visible yet, halo",
        locks=["ENOCH-GP"])),
    ("p14", "s4", _p(
        "God weeps: the Father's face, close and majestic, gazing "
        "down past the frame's lower edge at the veiled world — and "
        "TEARS on His cheeks: two bright unhidden lines running "
        "into the silver beard, His features holding all their "
        "sovereign steadiness while the tears fall anyway. Silent. "
        "Immense. The frame of the whole episode.",
        "the Father's close majestic face with unhidden tear-lines "
        "running into the silver beard, gaze down past frame",
        "His eyes on the lens, sobbing distortion, halo, red "
        "eyes overdone",
        era="heaven", locks=["FATHER"])),
    ("p15", ("s4", 0.6), _p(
        "The heavens weep: grey rain falling in slow silver sheets "
        "across dark shouldered mountains, soft light moving inside "
        "the fall of it, valleys hushed below — the scripture's own "
        "image, filling the frame. No figures.",
        "silver sheeted rain over dark mountains with soft light "
        "moving inside it",
        "lightning, floods, figures, text",
        wide=True)),
    ("p16", "n10", _p(
        "You? Weep?: Enoch's stunned upturned face — the anger and "
        "horror gone, replaced by an astonishment close to breaking, "
        "his own eyes brimming as he looks up past the camera at "
        "the weeping he cannot fathom, lips parted around the "
        "question.",
        "Enoch's stunned brimming upturned face, lips parted in "
        "question, gaze past the lens",
        "his eyes on the lens, full weeping yet, any figure",
        locks=["ENOCH-GP"])),
    ("p17", "g1", _p(
        "The answer: the Father and Enoch in one profile frame — "
        "the Father's arm extended out over the vista below, open "
        "palm down in sorrowing indication of the darkened world, "
        "Enoch beside and slightly below Him listening with his "
        "head bowed — the two of them lit warm against the grey "
        "rain-light beyond.",
        "the Father's sorrowing open-palm indication over the "
        "world with bowed listening Enoch beside him, both in "
        "profile",
        "faces to camera, halo, the dark band in this frame",
        era="heaven", locks=["FATHER", "ENOCH-GP"])),
    ("p18", "n11", _p(
        "Never unnoticed: the present day — a young woman sits "
        "curled on the floor beside her bed at night, head down on "
        "her folded arms, and across her and the floorboards lies "
        "one long warm panel of light from the window, resting on "
        "her like a hand — seen from across the dim room, her face "
        "hidden in her arms.",
        "a grieving young woman curled by her bed with one warm "
        "window-light panel resting across her, face hidden",
        "her face visible, phone, brand marks, anyone else",
        era="modern")),
    ("p19", ("n11", 0.62), _p(
        "After the weeping: the same mountains as the rain passes — "
        "the sheets thinning to bright threads, sun breaking behind "
        "them, the wet slopes beginning to shine, mist rising like "
        "released breath from the valleys. Grief that ends in "
        "light. No figures.",
        "rain thinning to bright threads over shining wet "
        "mountains, mist rising, sun breaking",
        "rainbows, figures, drawn rays, text",
        wide=True)),
]
