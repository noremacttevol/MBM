#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 12: The Flood and the Bow.

The hardest story, stood inside until it makes sense: a world with no good
option left, a grieving (not raging) God, a 120-year open invitation, death
that ended nobody's chances, and a war-bow hung in the sky as a promise.
Anchors: Genesis 6:5-13; 9:13; 1 Peter 4:6.

Restraint: no drowning is ever shown. The flood is the ark alone on great
seas. Humility law: we say plainly what is not revealed.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 312
NUM = 12
SLUG = "flood-and-bow"
TITLE = "The Flood and the Bow"
META = "Genesis 6-9 · 1 Peter 4"

SEGMENTS = [
    ("n1", NARRATOR,
     "This is the hardest story people throw at God. So we will not "
     "soften it. We will stand inside it until it makes sense."),
    ("n2", NARRATOR,
     "Ten generations after Adam, the earth was drowning before a single "
     "drop of rain fell. Here is scripture's diagnosis:"),
    ("s1", SCRIPTURE,
     "The earth also was corrupt before God, and the earth was filled "
     "with violence."),
    ("s2", SCRIPTURE,
     "And God saw that the wickedness of man was great in the earth, and "
     "that every imagination of the thoughts of his heart was only evil "
     "continually."),
    ("n4", NARRATOR,
     "Understand what that means for the plan. This world exists so "
     "children can be raised free to choose God. The devil had built a "
     "world with no good option left — every child born into violence, "
     "trained to violence. Not a school anymore. The plan itself was "
     "bleeding out."),
    ("s3", SCRIPTURE,
     "And it repented the Lord that he had made man on the earth, and it "
     "grieved him at his heart."),
    ("n5", NARRATOR,
     "Grieved him at his heart. Not rage. Grief. The same God who wept "
     "with Enoch, looking at the same darkness — one generation "
     "further gone."),
    ("n6", NARRATOR,
     "So He preserved what could still live. Noah — a preacher of "
     "righteousness who spent a hundred and twenty years warning, "
     "pleading, and building the way out in plain sight. An ark is an "
     "invitation with a door on it. It stood open to anyone who would "
     "turn around."),
    ("n7", NARRATOR,
     "Nobody turned. A century of preaching — and eight souls walked up "
     "the ramp."),
    ("n8", NARRATOR,
     "Then the flood came. And here is the truth that softens nothing "
     "but changes everything: death did not end a single story. Every "
     "person the water took woke on the other side of the veil — and "
     "Peter says what happened there:"),
    ("s4", SCRIPTURE,
     "For for this cause was the gospel preached also to them that are "
     "dead, that they might be judged according to men in the flesh, but "
     "live according to God in the spirit."),
    ("n9", NARRATOR,
     "Hold both truths at once. The flood was terrible. And the flood "
     "was a Father stopping a machine that was grinding up His "
     "children's freedom — while refusing to let death end anyone's "
     "chances. We do not claim to know everything about those days. "
     "But we know Him. And that is enough to trust the parts we cannot "
     "see."),
    ("n10", NARRATOR,
     "Then the water went down — and God did something brand new. He "
     "took the shape of a weapon of war, a battle bow — and hung it in "
     "the sky, unstrung, pointed at nothing."),
    ("s5", SCRIPTURE,
     "I do set my bow in the cloud, and it shall be for a token of a "
     "covenant between me and the earth."),
    ("n11", NARRATOR,
     "Every rainbow since is that same sentence, repeated: never again "
     "this way. The next time the world is saved, it will not be by "
     "water. It will be by blood — one Lamb's worth — and by a boat "
     "with room for every soul alive. You have seen God's bow your "
     "whole life. You have never once seen it aimed at you."),
]

CARD_SEG = ("card", NARRATOR,
            "The rainbow is a weapon hung up forever. His bow is never "
            "aimed at you.")

CARD_TEXT = ("His bow is never\n"
             "aimed at you.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Twelve — The Flood and the Bow")

SPOKEN = {}

NOAH = (
    "NOAH LOCK: the same man as the attached reference in every picture — "
    "a mighty patriarch of great age worn strong: deep brown weathered "
    "skin, long white hair bound back, a full white beard, heavy "
    "shipwright's shoulders, wearing a rough pitch-stained grey-brown "
    "work robe with a wide leather belt. Grave, unbreakable, kind. No "
    "halo, no glow.")

LOCKS = {"NOAH-GP": NOAH}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="ancient")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "A hard opening: black-green storm ocean to the horizon under a "
        "sky of iron, the swells huge and slow, spray tearing off their "
        "crests, one break of cold light far off where the clouds "
        "thin. No land, no ship, no figures — the weight of the "
        "subject itself.",
        "mountainous dark ocean under iron sky with one far cold "
        "light-break",
        "ships, land, figures, lightning bolts",
        wide=True)),
    ("p02", "s1", _p(
        "One single photographic scene, one light source logic: a "
        "fleeing family fills the frame's lower two-thirds, close — "
        "father mid-stride carrying a child, mother pulling another "
        "by the hand, all in three-quarter-from-behind climbing a "
        "dusk trail — and beyond and BELOW them, far off and small "
        "and soft-focus, ONE burning village burns orange in the "
        "valley they left, its smoke rising into a single level "
        "dusk sky. Depth reads continuously from their heels to the "
        "far fire; nothing pasted, no second fire anywhere.",
        "a close fleeing family climbing away up a dusk trail, one "
        "distant soft burning village below behind them",
        "two separate fire zones, collage or panel feel, weapons, "
        "wounds, attackers, faces to camera",
        wide=True)),
    ("p03", ("s1", 0.6), _p(
        "The cost, close: a small child's face pressed sideways "
        "against a father's shoulder mid-flight — eyes wide and "
        "wet, small fist gripping the rough cloth, lit only by "
        "plain fading dusk light. NO fire anywhere in this frame: "
        "no flames, no embers, no orange light, no bokeh points — "
        "just the child, the shoulder, and soft dusk. Nothing "
        "else in focus.",
        "a frightened child's face against a fleeing father's "
        "shoulder in plain dusk light, nothing burning in frame",
        "any flame, ember, fire-glow or orange bokeh anywhere, "
        "blood, wounds, faces to camera",
        )),
    ("p04", "s2", _p(
        "Only evil continually: a raiders' night camp — stacked "
        "spears against a cart of plundered goods, men crouched "
        "over dice and loot in cruel firelight, one dragging a "
        "struggling goat by the horns, laughter with no warmth in "
        "it — seen from beyond the firelight's edge, every face "
        "toward the game or the goods.",
        "a raiders' camp of stacked spears, dice, plunder and "
        "cruel firelight, seen from the dark edge",
        "captives shown, violence in progress, faces to camera",
        )),
    ("p05", "s3", _p(
        "Grief before judgment: the first heavy raindrops striking "
        "dry cracked earth — dark coins of wet blooming on the "
        "dust, one drop caught mid-fall, the light low and grey — "
        "heaven beginning to weep before it begins to work. "
        "Extreme close on the cracked ground.",
        "first heavy raindrops blooming dark on cracked dry earth, "
        "extreme close",
        "floods, figures, lightning, text",
        )),
    ("p06", "n6", _p(
        "The invitation, built in plain sight: Noah stands high on "
        "the ark's timber scaffold, one arm flung wide in "
        "mid-plea toward the crowd gathered below — some jeering "
        "with cupped hands, some laughing, one man turned to walk "
        "away — the great pitch-black hull towering behind the "
        "prophet like a wooden cliff. Camera among the crowd's "
        "shoulders, shooting up past their heads.",
        "Noah pleading from the ark's scaffold over a jeering "
        "dispersing crowd, the huge hull behind him",
        "faces to camera, thrown objects, rain yet",
        wide=True, locks=["NOAH-GP"])),
    ("p07", ("n6", 0.5), _p(
        "The door: the ark's great side-door standing OPEN at the "
        "head of its earthen ramp — warm lamplight spilling from "
        "the timber dark inside onto the boards, the grey day "
        "cold around it — an open mouth of refuge with nobody on "
        "the ramp. The frame waits.",
        "the ark's open door spilling warm lamplight down an "
        "empty ramp into a cold grey day",
        "crowds, animals yet, rain, guards",
        )),
    ("p08", "n7", _p(
        "Eight souls: the small family climbs the ramp toward the "
        "lit doorway — Noah last, his hand on the rail, all eight "
        "seen from behind at the ramp's foot — while in the near "
        "foreground the market crowd flows past the camera "
        "UNBOTHERED, backs and shoulders blurred, not one head "
        "turned toward the ark. Indifference as tragedy.",
        "eight figures from behind climbing to the lit door while "
        "a blurred foreground crowd flows past unbothered",
        "jeering now, faces to camera, rain",
        wide=True, locks=["NOAH-GP"])),
    ("p09", ("n7", 0.6), _p(
        "The closing: the massive timber door swings toward its "
        "frame — caught half-shut, the warm interior light "
        "narrowing to a blade across the ramp boards, the grey "
        "world reflected dull on the wet pitch of the hull. No "
        "figures visible; the narrowing light is the whole "
        "story.",
        "the great door half-shut, interior light narrowed to a "
        "blade on the ramp",
        "hands, figures, rain, darkness total yet",
        )),
    ("p10", "n8", _p(
        "The flood, at the limit of what we show: the ark utterly "
        "alone on mountainous grey-black seas, rain in driven "
        "sheets, the hull climbing a swell twice its height with "
        "spray bursting from its bow — no land, no other thing "
        "alive in frame, the world reduced to water and one "
        "wooden promise.",
        "the lone ark climbing a huge grey swell in driven rain",
        "people in the water, drowning, lightning striking, "
        "wreckage",
        wide=True)),
    ("p11", ("n8", 0.5), _p(
        "Hope kept burning: close on the ark's single small "
        "porthole in the streaming pitch-black planking — one "
        "warm lamp burning steady behind the thick glass while "
        "rain sheets across the timber — a coal of light the "
        "storm cannot reach.",
        "one warm lamplit porthole in streaming black planking, "
        "close",
        "faces at the glass, cracks, water inside",
        )),
    ("p12", "s4", _p(
        "The other side of the veil: a vast quiet assembly of men "
        "and women of every age and ancestry in soft grey-white "
        "light, seen from high behind their heads — all facing a "
        "single distant BRIGHT messenger whose arm is raised "
        "mid-declaration, the space itself calm, dimensionless, "
        "neither night nor day. The gospel reaching the drowned.",
        "a vast calm assembly from high behind, all faced toward "
        "one distant bright declaring messenger",
        "wings, halos, clouds, faces to camera, gloom",
        era="heaven", wide=True)),
    ("p13", "n9", _p(
        "Both truths in one face: Noah at the ark's rail in the "
        "easing rain — his grief and his trust in the same "
        "upturned features, water running off his white beard, "
        "one heavy hand gripping the rail, his eyes lifted into "
        "the grey. A man who obeyed and still feels the weight.",
        "Noah's upturned rain-washed face at the rail carrying "
        "grief and trust together",
        "his eyes on the lens, despair alone, sunshine yet",
        locks=["NOAH-GP"])),
    ("p14", "n10", _p(
        "The water went down: a bright washed morning — green "
        "hilltops standing fresh out of the last broad shining "
        "sheets of retreating water, sunlight breaking through "
        "clearing clouds onto wet new grass, streams silvering "
        "down every slope back toward the shrinking flood. The "
        "world handed back, clean and warm. Hopeful golden light, "
        "not gloom.",
        "green hilltops fresh out of retreating shining water "
        "under breaking warm sunlight",
        "gloom, grey murk, fog banks, the ark, rainbows yet, "
        "figures, doves",
        wide=True)),
    ("p15", ("n10", 0.55), _p(
        "Landfall: the family leads animals down the ramp onto "
        "green-muddy new ground — goats skittering, a pair of "
        "oxen ponderous, children running ahead — sun breaking "
        "through fast-moving clouds, everyone's face toward the "
        "land and the light, none toward the lens.",
        "family and animals descending the ramp onto muddy green "
        "ground under breaking sun",
        "faces to camera, crowds, rainbows yet",
        wide=True, locks=["NOAH-GP"])),
    ("p16", "s5", _p(
        "THE BOW: exactly ONE rainbow band in the whole sky — a "
        "lone real PRIMARY ARC as an actual photograph catches it, "
        "red outer edge fading to violet inside, softly "
        "translucent against washed blue-grey rain-light, one end "
        "grounding in the far hills — standing over the washed "
        "green world; the ark small and beached on its ridge, the "
        "family tiny in the meadow below with arms lifted toward "
        "the arc, everything rain-bright and new. The sky above "
        "and around the single arc is PLAIN washed grey-blue "
        "cloud only — count the coloured bands' arcs: exactly "
        "ONE; there is NO fainter second bow anywhere above or "
        "beside it, no reflection bow, no concentric double.",
        "ONE single physically real rainbow arc over the new "
        "green world, tiny family with lifted arms, beached ark",
        "two or more rainbows, crossing or intersecting arcs, "
        "rainbow fragments at odd angles, ribbon streaks, "
        "oversaturated candy colours, faces readable, drawn "
        "rays, text",
        wide=True, locks=["NOAH-GP"])),
    ("p17", ("s5", 0.6), _p(
        "Thanks: the family kneels around a new stone altar, its "
        "first smoke rising straight into the washed sky, the "
        "rainbow's foot still faint on the far hills — all seen "
        "from behind the kneeling half-circle. The oldest "
        "response to grace: an altar and a straight column of "
        "smoke.",
        "the family kneeling from behind at a smoking altar "
        "under a faint far rainbow-foot",
        "faces to camera, sacrifice visible, drawn rays",
        locks=["NOAH-GP"])),
    ("p18", "n11", _p(
        "Never aimed at you: from behind and beside a small girl "
        "of the new world in the washed green meadow — her "
        "upturned profile at the frame's LOWER LEFT corner, kept "
        "small, and the sky she looks into filling the frame's "
        "whole upper two-thirds, where ONE realistic rainbow "
        "stands COMPLETE and unmistakable — its full arc entirely "
        "INSIDE the frame, both ends visible reaching the far "
        "green hills, soft and translucent as a real photograph "
        "catches one; ordinary warm daylight, her mouth open in "
        "plain wonder.",
        "a small girl low in the corner under ONE complete "
        "rainbow arc fully inside the frame, both ends visible",
        "rainbow colours, prism bands or coloured light on her "
        "face, skin or clothes; more than one rainbow; her eyes "
        "on the lens, tears, adults in frame",
        )),
    ("p19", ("n11", 0.7), _p(
        "Peace, signed: a dead-calm COMPLETELY EMPTY sea at dawn "
        "under a clean sky — long gold light on gentle water, the "
        "storm's last clouds burning out pink at the horizon, one "
        "line of birds crossing far off. NO vessel of any kind — "
        "no ship, boat, sail or ark — anywhere on the water. The "
        "world, promised.",
        "a dead-calm dawn sea, storm remnants burning out pink, "
        "far birds",
        "ships, figures, rainbows, text",
        wide=True)),
]
