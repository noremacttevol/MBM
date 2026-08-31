#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 4: Cast Down.

What the rebel lost, what he kept, and the answer to "why does God allow a
devil at all" — D&C 29:39, in God's own words. The devil is never shown:
his fall is a streak of dying light, his presence is darkness, his power is
a voice. Anchors: Isaiah 14:12; Luke 10:18; 2 Nephi 2:17-27; D&C 29:39;
Revelation 12:12.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, DEVIL = ("narrator", "jesus", "father",
                                             "scripture", "devil")

EP = 304
NUM = 4
SLUG = "cast-down"
TITLE = "Cast Down"
META = "Isaiah 14 · D&C 29 · 2 Nephi 2"

SEGMENTS = [
    ("n1", NARRATOR,
     "So the rebel fell. This is the story of what he lost, what he kept — "
     "and the question everyone asks sooner or later: why does God allow a "
     "devil at all?"),
    ("s1", SCRIPTURE,
     "How art thou fallen from heaven, O Lucifer, son of the morning! how "
     "art thou cut down to the ground, which didst weaken the nations!"),
    ("n2", NARRATOR,
     "Lucifer. The name means light-bearer. Son of the morning. This was "
     "not some monster crawling out of a pit — this was one of the family. "
     "Brilliant. Trusted. Standing in authority. Until he wanted the "
     "throne more than the family."),
    ("j1", JESUS,
     "I beheld Satan as lightning fall from heaven."),
    ("n3", NARRATOR,
     "Jesus said that as an eyewitness. He watched it happen. And notice "
     "what the fall cost: not existence — position. He lost the presence "
     "of the Father. He lost his glory. And he lost one thing forever "
     "that every single one of us has. He will never have a body."),
    ("n4", NARRATOR,
     "Every baby ever born receives the thing he forfeited. Remember that "
     "the next time he whispers that your body is shameful, or worthless, "
     "or a prison. He would trade anything for one."),
    ("s2", SCRIPTURE,
     "For he seeketh that all men might be miserable like unto himself."),
    ("n5", NARRATOR,
     "That is his entire business model, in one line. He cannot win "
     "anything anymore. No body. No future. No throne. So he plays for "
     "one outcome only — making your loss as total as his."),
    ("n6", NARRATOR,
     "Now the hard question. If God is all-powerful, and all-good — why "
     "keep a devil around? Why not just turn him off? God answered that "
     "question directly. Listen:"),
    ("g1", FATHER,
     "And it must needs be that the devil should tempt the children of "
     "men, or they could not be agents unto themselves; for if they never "
     "should have bitter they could not know the sweet."),
    ("n7", NARRATOR,
     "Or they could not be agents unto themselves. There it is, from "
     "God's own mouth. Freedom is not real if no is impossible. A world "
     "with no tempter is a world with no choice — and a world with no "
     "choice was the devil's plan. God refused to defeat him by becoming "
     "him."),
    ("n8", NARRATOR,
     "So hold this straight: God did not create evil. He created freedom "
     "— real freedom — knowing it could say no, knowing one of His "
     "brightest would say it first, and knowing exactly what the repair "
     "would cost. The Lamb was chosen before the devil ever fell."),
    ("s3", SCRIPTURE,
     "For it must needs be, that there is an opposition in all things."),
    ("n9", NARRATOR,
     "No opposition, no growth. No resistance, no strength. The road "
     "where you become like Jesus runs uphill on purpose — and the devil, "
     "without ever meaning to, is part of the incline. Every time you "
     "tell him no, you become more of what God sent you here to become."),
    ("s4", SCRIPTURE,
     "Woe to the inhabiters of the earth and of the sea! for the devil is "
     "come down unto you, having great wrath, because he knoweth that he "
     "hath but a short time."),
    ("n10", NARRATOR,
     "Having great wrath — because he knows he has but a short time. He "
     "is not winning. He has already lost twice, the war and the tomb, "
     "and he can hear the clock."),
    ("n11", NARRATOR,
     "So when temptation comes for you today, remember what is actually "
     "behind it. Not a rival god. A beaten, bodiless, desperate former "
     "brother whose only remaining power is a voice. And you have beaten "
     "his voice before."),
]

CARD_SEG = ("card", NARRATOR,
            "He has no body, no future, and no power over you but a "
            "voice. And you have beaten his voice before.")

CARD_TEXT = ("His only power\n"
             "is a voice.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Four — Cast Down")

SPOKEN = {}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="heaven")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The emptied cold end of the council court in the quiet after "
        "the war: bare luminous terraces stretching away with no one on "
        "them, the warm dawn light lying long and low across the vacant "
        "stone, one abandoned white mantle crumpled small on the floor "
        "in the middle distance. Stillness like a held breath. No "
        "people.",
        "vacant bright terraces after the departure, one small crumpled "
        "white mantle far off, no people",
        "any figure, darkness remaining, wings, text",
        wide=True, locks=["COURT"])),
    ("p02", "s1", _p(
        "The fall itself, seen as heaven saw it: against the deep "
        "indigo above the court's dawn horizon, ONE brilliant "
        "star-point of light streaks DOWNWARD in a long dying arc, its "
        "trail already fading behind it — light itself falling, no "
        "figure, no body, no shape inside the brightness. The court's "
        "balustrade edges the frame's bottom, empty.",
        "one brilliant point of light streaking down a long dying arc "
        "through indigo sky, empty balustrade below",
        "ANY figure, body, wings or silhouette in or around the light; "
        "a comet with a face; lightning bolts",
        devil=True, locks=["COURT"])),
    ("p03", "n2", _p(
        "What he was: at the foot of the dais steps, a place of honour "
        "stands conspicuously VACANT — a gap in the arc of noble "
        "positions where the light still pools on empty stone — and "
        "the white-robed spirits nearest it stand angled away from the "
        "gap, not looking at it, the way people avoid a fresh grave. "
        "Seen from beside the arc in three-quarter; no face to the "
        "lens.",
        "a conspicuously empty place of honour near the dais, "
        "neighbours angled away from the gap",
        "any figure in the gap, thrones, crowns, faces to camera",
        locks=["COURT", "HOSTS"])),
    ("p04", "j1", _p(
        "The eyewitness: Jesus at the balustrade in his cream robe, "
        "seen in close three-quarter profile, watching the dying "
        "streak of light go down beyond the rail — grief without "
        "surprise on his face, the fall reflected as a faint moving "
        "brightness in his eyes. His hands rest still on the stone "
        "rail.",
        "Jesus in close three-quarter at the rail watching a falling "
        "light beyond, grief without surprise, hands still on stone",
        "his eyes on the lens, halo, tears streaming, any figure in "
        "the falling light",
        jesus=True, ref=True, locks=["COURT"])),
    ("p05", "n3", _p(
        "The loss, complete: far below the court's rim, the last spark "
        "of the falling light dwindles into the black deep — a "
        "pin-point of brightness being swallowed by distance and dark, "
        "the vast indigo emptiness holding nothing else. The stone rim "
        "cuts the frame's top corner; the rest is depth.",
        "a single dwindling pin-point of light deep in black-indigo "
        "emptiness below the court's rim",
        "any shape or figure in the dark, flames, an impact, a pit "
        "with fire",
        devil=True, locks=["COURT"])),
    ("p06", "n4", _p(
        "The inheritance he forfeited: a newborn's whole tiny hand "
        "gripping one adult finger in warm morning window light, the "
        "small knuckles flushed and REAL — flesh and bone, close "
        "enough to see the fine creases. Nothing else in the frame.",
        "a newborn's hand gripping an adult finger in warm light, "
        "skin texture close and real",
        "faces, jewellery, text, modern hospital equipment",
        era="modern")),
    ("p07", "s2", _p(
        "Misery's neighbourhood: an empty night alley in the present "
        "day — wet asphalt, one cold flickering wall-light, and "
        "darkness pooling FORMLESS in the deep end where the light "
        "fails, no figure standing in it, nothing but cold and "
        "absence. A tipped-over trash can spills at the edge of the "
        "lit ground.",
        "a cold empty night alley with formless darkness pooling in "
        "its deep end, one failing wall-light",
        "ANY figure, eyes, shape or silhouette in the dark; graffiti "
        "words; rats swarming",
        era="modern", devil=True)),
    ("p08", "n5", _p(
        "Total loss made visible: a great stone hearth long cold — "
        "deep grey ash where a fire lived, one charred beam-end, a "
        "fine drift of ash-dust across the hearthstone in the pale "
        "light of a doorway out of frame. The warmth is not dimmed; "
        "it is gone. No people.",
        "a long-cold great hearth of grey ash and one charred "
        "beam-end in pale sidelight",
        "embers still lit, smoke, any figure, cobwebs overdone",
        era="old-world")),
    ("p09", "n6", _p(
        "The asker: in the present day a woman stands at a dark "
        "apartment window at night, seen from behind her shoulder, "
        "the city's scattered lights far below and her faint "
        "reflection unreadable in the glass — the posture of someone "
        "holding a question too big for the room.",
        "a woman from behind at a night window over scattered city "
        "lights, reflection unreadable",
        "her face identifiable, readable signs below, screens, "
        "brand marks",
        era="modern")),
    ("p10", "g1", _p(
        "God's answer, drawn in terrain: a high mountain trail forks "
        "in first light — one path climbing steep and stony toward "
        "the sunrise ridge, the other falling easy and smooth into a "
        "shadowed valley still holding night — the fork itself worn "
        "bare by every traveller who ever stood deciding. No one on "
        "the trail; the choice is the subject.",
        "a worn trail forking between a steep sunrise climb and an "
        "easy shadowed descent, empty of people",
        "signposts with words, any figure, drawn light rays",
        era="ancient", wide=True)),
    ("p11", "n7", _p(
        "The door He would not lock: a heavy wooden door in a stone "
        "wall standing wide OPEN, warm daylight flooding through it "
        "across the threshold stones, the bar that could seal it "
        "leaning unused against the wall — nobody in the doorway, "
        "nobody forced through, the way out and the way in both "
        "free. Close, plain, charged.",
        "a heavy door standing wide open with its unused bar leaning "
        "beside it, warm light across the empty threshold",
        "chains, locks engaged, any figure, text",
        era="ancient")),
    ("p12", "n8", _p(
        "Chosen before the fall: Jesus standing COMPLETELY ALONE in the "
        "court's full dawn light in his cream robe — not one other "
        "person anywhere in the frame, the bright terraces empty to "
        "their far edges — calm and resolute, his gaze levelled far "
        "out toward the dark horizon-line where the light fell, seen "
        "from beside him at a reverent distance, his profile steady, "
        "the whole posture of someone who has already accepted a "
        "price.",
        "Jesus in profile in full court light, calm resolve aimed at "
        "the far dark horizon",
        "his eyes on the lens, halo, grief overdone, any figure on "
        "the horizon",
        jesus=True, ref=True, locks=["COURT"])),
    ("p13", "s3", _p(
        "Opposition in all things, in one image: a single green "
        "shoot stands upright through a split in weathered grey "
        "stone, morning light on its two small leaves, the crack's "
        "edges sharp and hard around the softness that beat them. "
        "Extreme close; nothing else.",
        "a green shoot standing through split grey stone in morning "
        "light, extreme close",
        "flowers in bloom, gardens, hands, text",
        era="ancient")),
    ("p14", "n9", _p(
        "Resistance building strength: an ancient smith mid-strike — "
        "hammer high at the top of its arc, red-hot iron bar on the "
        "anvil throwing sparks, his forearm corded, face lit from "
        "below by the forge's open fire, eyes locked on the metal — "
        "caught from the side so the whole working line of arm, "
        "hammer and iron reads at a glance.",
        "a smith caught at the top of a hammer-strike over bright "
        "red-hot iron, sparks, forge-lit focus",
        "his eyes on the lens, modern tools, machined metal, the "
        "word glow anywhere in the metal's look",
        era="ancient")),
    ("p15", ("n9", 0.6), _p(
        "What the resistance made: the smith plunges the finished "
        "bright blade into the quench-trough — steam bursting up "
        "around his steady hand and forearm, his face behind the "
        "rising veil watchful and satisfied. The steel holds its "
        "shape because the fire and the hammer opposed it.",
        "a blade quenched in a burst of steam, steady hand and "
        "watchful face behind the veil",
        "his eyes on the lens, modern equipment, dramatic embers "
        "filling the air",
        era="ancient")),
    ("p16", "s4", _p(
        "His short time: a vast storm front rolls across open plains "
        "toward the camera — a wall of bruised cloud with lightning "
        "flickering INSIDE it, its underside dragging rain — and "
        "ahead of it, the land still lies in gold evening light, "
        "fenceless and empty. The front is weather, pure and "
        "shapeless: no face, no figure, no reaching forms in the "
        "cloud.",
        "a shapeless storm wall with interior lightning advancing "
        "over gold-lit empty plains",
        "ANY face, figure, claw or reaching shape in the clouds; "
        "tornadoes; buildings",
        era="ancient", devil=True, wide=True)),
    ("p17", "n10", _p(
        "Already lost twice: the great round stone of a garden tomb "
        "stands rolled ASIDE in its channel, and low dawn light "
        "pours through the open doorway into the empty chamber, "
        "laying a bright doorway-shaped panel on the hewn floor "
        "where nothing lies. No people; the emptiness is the "
        "victory.",
        "a rolled-aside tomb stone and dawn light filling an empty "
        "hewn chamber",
        "guards, angels, grave clothes prominent, any figure",
        era="first-century")),
    ("p18", "n11", _p(
        "Beating the voice today: a young man crosses a city street "
        "out of the shadowed side into the full sunlit side — caught "
        "mid-stride from behind at the moment the light takes his "
        "shoulders, the dark half of the street flat and cold behind "
        "him, the bright half alive with morning ahead.",
        "a man from behind crossing mid-stride out of street shadow "
        "into full morning sun",
        "his face, readable signs, brand marks, traffic danger",
        era="modern")),
    ("p19", ("n11", 0.65), _p(
        "Free: close on a face in full sunlight — eyes closed, "
        "breathing out, the peace of somebody who just said no and "
        "meant it — warm light across ordinary features, in the "
        "present day.",
        "a close sunlit face, eyes closed, exhaling peace",
        "eyes open on the lens, tears, halo effects",
        era="modern")),
    ("p20", ("n11", 0.85), _p(
        "The long view: dawn breaking over the curve of the earth "
        "from high above — the terminator line burning gold across "
        "oceans and cloud, night retreating westward off the frame — "
        "the contested world, still beautiful, still turning toward "
        "light. No figures.",
        "dawn's gold line crossing the curved earth from high above, "
        "night retreating",
        "any figure, satellites, text, country outlines "
        "recognizable",
        )),
]
