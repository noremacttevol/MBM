#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 6: The Guarantee.

The terms of mortality: the veil (why God hides), the fall (why it was
survivable), and the Lamb chosen before the foundation of the world.
Anchors: 2 Corinthians 5:7; Ether 12:6; Revelation 13:8; 1 Peter 1:19-20.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, DEVIL = ("narrator", "jesus", "father",
                                             "scripture", "devil")

EP = 306
NUM = 6
SLUG = "the-guarantee"
TITLE = "The Guarantee"
META = "Revelation 13 · 1 Peter 1 · Ether 12"

SEGMENTS = [
    ("n1", NARRATOR,
     "Before you were born, you agreed to terms that should scare you. "
     "Forget everything. Walk blind. Risk sin, and pain, and death. Why "
     "would anyone sign that — and why would a loving Father offer it?"),
    ("n2", NARRATOR,
     "Start with the forgetting. A veil was drawn across your memory — "
     "heaven, the council, His face. Not as a punishment. As the whole "
     "point."),
    ("n3", NARRATOR,
     "Because the test could never work in plain sight. A God standing "
     "visibly in the room does not get chosen — He gets complied with. "
     "And compliance was Lucifer's plan."),
    ("n4", NARRATOR,
     "The veil is what makes your choices mean something. Down here you "
     "cannot lean on the memory of His face. You have to decide what you "
     "love — when love is all you have to go on."),
    ("s1", SCRIPTURE,
     "For we walk by faith, not by sight."),
    ("s2", SCRIPTURE,
     "Faith is things which are hoped for and not seen; wherefore, "
     "dispute not because ye see not, for ye receive no witness until "
     "after the trial of your faith."),
    ("n5", NARRATOR,
     "So the silence you sometimes feel is not absence. It is the exam "
     "room being kept honest. He is closer than the veil feels. And the "
     "veil is thinner than you think."),
    ("n6", NARRATOR,
     "But forgetting was the smaller risk. Here is the bigger one: down "
     "here, everyone sins. Everyone dies. If the story ended there, "
     "mortality would be a trap, not a school."),
    ("n7", NARRATOR,
     "So before the first breath was ever drawn — before Adam, before "
     "Eden, before the earth itself — the rescue was already signed."),
    ("s3", SCRIPTURE,
     "The Lamb slain from the foundation of the world."),
    ("s4", SCRIPTURE,
     "The precious blood of Christ, as of a lamb without blemish and "
     "without spot: who verily was foreordained before the foundation of "
     "the world, but was manifest in these last times for you."),
    ("n8", NARRATOR,
     "Foreordained before the foundation of the world. The Savior was "
     "never God's backup plan after Eden went wrong. He was the "
     "load-bearing beam of the original blueprint. The plan was never "
     "hope they don't fall. It was: they will fall — and I will catch "
     "every single one who lets me."),
    ("n9", NARRATOR,
     "That is why heaven let you take the risk at all. You did not go "
     "down uninsured. Your Father let you fall only because your Brother "
     "had already promised to catch you."),
    ("n10", NARRATOR,
     "So read the terms again. Forget — so your love can be real. Fall — "
     "with the rescue pre-paid. Walk blind — with a hand you cannot see "
     "holding the rail beside you the whole way down."),
    ("n11", NARRATOR,
     "You signed those terms once, with a shout of joy. Somewhere behind "
     "the veil, you knew exactly what you were doing."),
]

CARD_SEG = ("card", NARRATOR,
            "You did not come here uninsured. The rescue was signed "
            "before the risk began.")

CARD_TEXT = ("The rescue was signed\n"
             "before the risk began.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Six — The Guarantee")

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
        "The threshold of forgetting: a lone white-robed spirit stands "
        "seen from directly behind before an immense soft WALL OF WHITE "
        "MIST that fills the frame's whole far half — featureless, "
        "gently moving, lit from within by warm light, hiding "
        "everything beyond it. The luminous court stone runs to the "
        "mist's edge. The figure's hands hang open at their sides: "
        "about to walk through.",
        "a spirit from directly behind facing an immense soft glowing-"
        "from-within wall of white mist across the frame",
        "the figure's face, shapes inside the mist, doors, text",
        era="heaven", locks=["COURT", "HOSTS"])),
    ("p02", "n2", _p(
        "The memory closing: an extreme close of a young spirit's face "
        "in the warm light, eyes CLOSING — lashes just meeting — with "
        "perfect trust in the features, like a child agreeing to sleep. "
        "Soft white mist begins to cross the frame's edges.",
        "a serene close face with eyes just closing in warm light, "
        "mist entering the frame edges",
        "fear, tears, eyes open to the lens, halo",
        era="heaven", locks=["HOSTS"])),
    ("p03", "n3", _p(
        "Why He must hide: a man shields his whole face with a raised "
        "forearm against a brilliance that fills the frame's left — "
        "seen from behind his right shoulder, his body turned away, "
        "unable to stand square to what he plainly cannot disobey. "
        "The brilliance is pure white environmental light with no "
        "figure in it.",
        "a man from behind-shoulder shielding his face and turning "
        "from an overwhelming brilliance filling the left frame",
        "any figure inside the light, his face visible, drawn rays",
        era="heaven")),
    ("p04", "n4", _p(
        "Choosing in the dark: at full night a traveller stands at a "
        "fork in a forest path holding a small clay oil lamp — its "
        "little pool of warm light reaching only a few steps down "
        "either way, the trees black beyond — seen from behind at "
        "lamp height, the choice lit exactly as far as faith reaches.",
        "a traveller from behind at a night path fork, a clay lamp's "
        "small pool of light on both openings",
        "his face, torches blazing, moonbeams, any figure ahead",
        )),
    ("p05", "s1", _p(
        "Walking by faith, literally: bare weathered feet mid-step on "
        "wet stepping stones crossing dark night water, the small "
        "warm edge of lamplight from out of frame catching just the "
        "next stone and no further — extreme close at ground level, "
        "the far bank invisible.",
        "bare feet mid-step on lamplit stepping stones over dark "
        "water, next stone barely lit",
        "faces, the far bank visible, moon reflections, text",
        )),
    ("p06", "s2", _p(
        "The trial before the witness: a climber's chalkless bare "
        "hand gripping a cold rock edge in blue pre-dawn dark, "
        "forearm taut, breath-fog crossing the frame — and high "
        "above, out of focus at the frame's top, the first faint "
        "warm light touching the summit he cannot yet see. Close on "
        "the grip.",
        "a bare straining hand gripping dark rock at pre-dawn, faint "
        "summit warmth far above out of focus",
        "faces, ropes and gear prominent, daylight, text",
        )),
    ("p07", "n5", _p(
        "The thin veil: an autumn field at early morning under soft "
        "fog — and behind the fog, the sun standing as a gentle "
        "white-gold disc, its warmth plainly FELT through the veil "
        "that hides its edge — long grass beaded wet, one row of "
        "trees ghosted in the brightness. Presence, through "
        "thinness. No people.",
        "a soft fogged field with the sun a warm disc plainly felt "
        "behind the veil, beaded grass",
        "harsh rays, figures, buildings, text",
        )),
    ("p08", "n6", _p(
        "The stakes: at dusk on a ridgeline, a small ancient funeral "
        "procession crosses in silhouette-soft profile — six bearers "
        "with a wrapped bier on their shoulders, mourners behind, "
        "all in dignified dark shapes against the last amber sky, "
        "far enough that no face reads. Quiet, universal, true.",
        "a small distant funeral procession in profile on a dusk "
        "ridge, bearers and bier against amber sky",
        "faces readable, wailing gestures, graves, text",
        wide=True)),
    ("p09", "n7", _p(
        "Already signed: in the council court's brightest light the "
        "Son stands calm with his right hand raised to the square — "
        "the ancient gesture of covenant — his face in steady "
        "three-quarter aimed past the camera's left toward the "
        "unseen Father, cream robe still, the hosts a soft warm "
        "blur beyond. A promise being made before the world.",
        "Jesus with right hand raised to the square in covenant, "
        "steady three-quarter gaze past the lens, hosts blurred "
        "beyond",
        "his eyes on the lens, halo, documents, anyone else sharp",
        era="heaven", jesus=True, ref=True, locks=["COURT", "HOSTS"])),
    ("p10", "s3", _p(
        "The Lamb: a shepherd carries a pure white lamb across his "
        "shoulders at first light, both hands holding its legs "
        "steady at his chest, walking a stony path toward the "
        "sunrise — seen from the side in warm profile, the lamb "
        "calm, the man's stride sure. Foreshadowing carried "
        "gently.",
        "a shepherd in profile carrying a calm white lamb on his "
        "shoulders toward sunrise",
        "blood, altars, distress in the lamb, faces to camera",
        )),
    ("p11", "s4", _p(
        "Foreordained: the Son's face close in the court's warm "
        "light — utterly calm, the resolve of someone volunteering "
        "for a price fixed before time, his gaze level past the "
        "camera's right shoulder into the depth where the world "
        "will be. Peace with iron under it.",
        "Jesus's close calm face, covenant resolve, level gaze "
        "past the lens",
        "his eyes on the lens, tears, halo, grimness",
        era="heaven", jesus=True, ref=True, locks=["COURT"])),
    ("p12", "n8", _p(
        "The load-bearing beam: ancient builders lower a massive "
        "carved KEYSTONE into the crown of a stone arch — two men "
        "guiding it by rope from above, one steadying from the "
        "scaffold, the stone caught mid-descent a hand's width "
        "from its seat — every eye on the stone, the arch's two "
        "halves waiting to become one strength. Golden work-light.",
        "a keystone caught mid-lowering into a waiting arch, "
        "ropes taut, every eye on the stone",
        "faces to camera, cranes, iron machinery, text",
        )),
    ("p13", ("n8", 0.55), _p(
        "The blueprint holds: the finished arch standing under "
        "full load — a laden cart passing beneath it, children "
        "running through, the keystone tight in its crown — seen "
        "from low and beside so the whole curve reads at once in "
        "morning light. What was planned first, carries "
        "everything.",
        "a finished stone arch carrying traffic beneath it, "
        "keystone visible in the crown, low side view",
        "cracks, scaffolding remaining, faces to camera",
        )),
    ("p14", "n9", _p(
        "The promised catch: a laughing child leaps from a low "
        "courtyard wall into a father's already-open arms — caught "
        "at the top of the arc, mid-air, arms out, the father's "
        "braced stance and rising hands under him, both faces in "
        "profile — total trust, zero doubt about the landing. "
        "Golden late light.",
        "a child mid-air leaping from a wall into a father's "
        "waiting braced arms, both profiles, joy",
        "fear on either face, faces to camera, hard shadows",
        )),
    ("p15", "n10", _p(
        "The unseen hand on the rail: narrow stone steps cut down "
        "a cliff face at night, a taut rope rail running down "
        "them, and a cloaked traveller descending with one hand "
        "firm on the rope — seen from behind and above so the "
        "rope's line leads the eye down into the dark where the "
        "steps vanish. The rope holds; the bottom is not visible.",
        "a traveller from behind descending night cliff steps, "
        "one hand firm on a taut rope rail vanishing into dark",
        "his face, torches, the bottom visible, any figure below",
        )),
    ("p16", ("n10", 0.55), _p(
        "The way down was safe: dawn at the cliff's foot — the "
        "same traveller now small in the frame, stepping off the "
        "last stair into a wide valley washed in first light, the "
        "rope rail slack behind him, the night above and behind. "
        "Arrival, intact.",
        "the traveller small at the stair's foot stepping into a "
        "dawn-washed valley, rope rail behind",
        "his face, other people, drawn rays",
        wide=True)),
    ("p17", "n11", _p(
        "The shout, remembered: one young face in the council's "
        "warm gold — mid-shout of pure joy, eyes bright and wet, "
        "fists half-raised — the exact instant of signing on with "
        "everything, gaze aimed up past the camera's left at the "
        "announcement. The joy of someone who knows the terms.",
        "one close face mid-shout of joy, wet bright eyes aimed "
        "up past the lens, fists half-raised",
        "eyes on the lens, fear, wings, halo",
        era="heaven", locks=["HOSTS"])),
    ("p18", ("n11", 0.55), _p(
        "Terms begun: an extreme close of a newborn's eye opening "
        "for the first time — the lid lifting on a deep dark "
        "iris catching its first warm lamplight, lashes wet, skin "
        "new — the veil complete, the adventure started. Nothing "
        "else in frame.",
        "a newborn's eye mid-first-opening, warm light in a new "
        "dark iris, extreme close",
        "distress, clinical surroundings, adult hands prominent",
        )),
    ("p19", ("n11", 0.82), _p(
        "The veil, thinning: morning fog parting over a green "
        "valley as the sun finally breaks it — the disc becoming "
        "true light, the field's colours arriving, the trees "
        "stepping out of the white — the closing promise that "
        "hidden was never gone. No people.",
        "fog parting as the sun breaks through onto a waking "
        "green valley",
        "figures, buildings, drawn rays, text",
        wide=True)),
]
