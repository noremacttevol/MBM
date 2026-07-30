#!/usr/bin/env python3
"""V2 beat map — row 33, build-33-sheep-goats (Matthew 25:31-46).

COVERAGE: 29 pictures over 168.1 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 25:31-46 KJV):
  Setting of the telling: still the Mount of Olives discourse (Matthew
  24:3) — rows 31 and 32 staged Olivet as a wide circle and a
  behind-the-shoulder view, so THIS build's frame beat (b01) is a CLOSE
  side profile of Jesus speaking with the disciples soft beyond him, deep
  dusk. No repeated composition.
  v31-32 "the Son of man ... then shall he sit upon the throne of his
        glory: and before him shall be gathered ALL NATIONS" — THE KING IS
        JESUS. He is painted with the one locked face and the cream robe
        (only Jesus wears cream), seated on a SIMPLE raised stone seat on
        an open dawn plain — majesty carried by scale and light placement,
        NEVER by halo, glow or rim-light.
  v32-33 "as a shepherd divideth his sheep from the goats" — the metaphor
        gets its own literal beats: a real shepherd at evening quietly
        dividing a real flock.
  v34-36 "Come, ye blessed of my Father ... I was an hungred, and ye gave
        me meat" — the six mercies (fed, drink, stranger, clothed, sick,
        prison) are painted as ORDINARY human vignettes, the heart of the
        row.
  v37-39 the righteous are CONFUSED — they don't remember doing anything
        special. Their confusion beats are warm and puzzled, never proud.
  v40   "Inasmuch as ye have done it unto one of the LEAST of these my
        brethren, ye have done it unto ME." — ⚑ Flag J (CONTENT-CARE §3
        row 33): 'the King was IN the hungry and the stranger all along.'
        The disguise is NEVER painted literally (no Jesus-faced beggars —
        the one-locked-face law and reverence both forbid it); the
        nearest visual is the King drawing the least-looking person to
        his side at the throne.
  v41-46 the narration OMITS the everlasting-punishment sentence; the
        'others missed him' beats are painted as GRIEF and missed
        encounters — walking past him — never fire, never doom imagery.

TIME OF DAY: Olivet frame is deep blue dusk. The judgment scene is a
great clean DAWN over the plain (the last day breaking — deliberate).
The shepherd metaphor is gold EVENING (v32's own image). The mercy
vignettes vary by their nature: bread at midday, a sickroom by lamplight,
a dim stone cell, a doorway at dusk, a cold grey street — each stated in
its beat. All shifts are scripture- or story-driven.

CHANGING CONDITION (kept OUT of the locks): the needy people of the
vignettes are DIFFERENT individuals per beat (hungry man, thirsty child,
stranger woman, cold old man, sick young man, prisoner) — deliberately
unlocked, because the point is 'whoever was in front of them.'
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "SHEPHERD": (
        "SHEPHERD LOCK: the shepherd of the metaphor beats is the same man "
        "in every shot — about fifty, lean and weathered, with a rough "
        "grey-streaked beard and calm sure movements. He wears a coarse "
        "DARK BROWN wool tunic under a sleeveless sheepskin, a wide "
        "leather belt and a long crooked staff (never cream, never "
        "white). His face is shown clearly."
    ),
    "FLOCK": (
        "FLOCK LOCK: the mixed flock — broad-backed cream-fleeced sheep "
        "with dark legs and faces, and lean short-haired goats in dark "
        "brown and black with small curved horns. The two kinds are "
        "always tellable at a glance by fleece against hair."
    ),
    "PLAIN": (
        "JUDGMENT PLAIN LOCK: a vast open grass plain at first light — "
        "short pale grass running to the horizon on every side, a low "
        "natural rise at its centre crowned by a simple seat of great "
        "unhewn stones, and a clean dawn sky banded gold to deep blue. "
        "No architecture, no clouds-and-rays imagery — earth, grass, "
        "stone and sky only."
    ),
    "NATIONS": (
        "NATIONS LOCK: the gathered multitude is people of every age and "
        "kind — men, women, children, the old and the young, shepherds "
        "and merchants and mothers with infants — dressed in SATURATED "
        "DEEP colours of every earth shade: dark browns, deep russet, "
        "dark olive, burnt ochre, dusty indigo, faded plum, dark "
        "madder-red (never cream, never white; only Jesus wears cream). "
        "Faces are shown clearly."
    ),
    "OLIVET": (
        "MOUNT OF OLIVES LOCK: the western slope of the Mount of Olives "
        "at deep dusk — dry grass and grey stone between old gnarled "
        "olive trees, the dark Kidron valley below, and the walls of "
        "Jerusalem beyond with small warm lamps lit along them under "
        "the last deep blue of the sky."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r033-b01", "out": "s01-near-the-end-jesus-told.jpeg", "seg": "n1",
        "window": "0.28-4.12", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OLIVET"],
        "narration": (
            "Near the end, Jesus told his friends what the last day would "
            "really be like."
        ),
        "must_show": "the frame — a close side profile of Jesus speaking in the deep dusk, the disciples' listening shapes soft beyond his shoulder, Jerusalem's small lamps far below.",
        "must_not_show": "no halo, glare or rim-light on Jesus; intimacy and gravity — the last teachings of the last week.",
        "scene": (
            "A close side profile of Jesus in the deep blue dusk on "
            "the hillside, his face lit faintly by the last of the "
            "west, mid-word, grave and very gentle — and beyond his "
            "shoulder, soft in the failing light, the seated shapes of "
            "the disciples lean in, with the tiny warm lamps of "
            "Jerusalem's walls scattered far below in the dark valley. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b02", "out": "s02-he-said-the-king-would.jpeg", "seg": "n1",
        "window": "4.12-9.94", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PLAIN", "NATIONS"],
        "narration": (
            "He said the King would gather all the nations in front of him and "
            "separate them into two groups."
        ),
        "must_show": "SCRIPTURE-EXACT: the great gathering — the vast dawn plain filled to the horizon with people of every kind, and at its centre the King seated on the simple stone seat, small but unmistakably the still point.",
        "must_not_show": "no halo, glare or rim-light on the King; majesty from SCALE and dawn light only — no rays, no clouds parting, no floating.",
        "scene": (
            "From high over the vast plain at first light: a sea of "
            "people stretches away to the pale horizon in every "
            "direction, thousands upon thousands in every deep earth "
            "colour, all faced inward — and at the centre, on the low "
            "grass rise, the King sits on the simple seat of great "
            "unhewn stones in his plain cream robe, the one still "
            "point the whole world is turned toward, the dawn banding "
            "gold behind the far edge of the earth. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b03", "out": "s03-and-before-him-shall-be.jpeg", "seg": "j32",
        "window": "10.70-20.45", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PLAIN", "NATIONS"],
        "narration": (
            "And before him shall be gathered all nations: and he shall "
            "separate them one from another, as a shepherd divideth his sheep "
            "from the goats:"
        ),
        "must_show": "SCRIPTURE-EXACT: the separating begun — the King risen from the seat, one arm extended gently to his right hand and the other to his left, the near ranks of the multitude beginning to move two ways.",
        "must_not_show": "no halo, glare or rim-light on the King; the gesture is a shepherd's guiding motion, calm and unhurried — never a commander's chop.",
        "scene": (
            "On the low rise the King stands before the stone seat "
            "with both arms opened low and wide, one toward his right "
            "hand and one toward his left, the motion gentle as a man "
            "parting water — and through the near ranks of the "
            "multitude the movement has begun, streams of people "
            "turning and flowing slowly to the two sides across the "
            "dawn-lit grass, faces lifted to him as they go. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b04", "out": "s04-you-fed-me-when-i.jpeg", "seg": "n4",
        "window": "63.86-66.19", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "You fed me when I was hungry, he said.",
        "must_show": "the first mercy — a close shot of a woman's hands breaking her own round loaf and giving the larger half to a gaunt hungry man's cupped hands.",
        "must_not_show": "no halo, glare or rim-light; the LARGER half goes to him — ordinary costly kindness, nobody watching.",
        "scene": (
            "A close shot in plain midday light at a street corner: a "
            "woman's work-worn hands break her one round loaf in two "
            "and press the larger half down into the cupped, dirt "
            "-lined hands of a gaunt hungry man seated against the "
            "wall — his face lifting in the frame's soft edge, hers "
            "bent toward him, the bread still warm enough to steam "
            "faintly. Nobody else is watching. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b05", "out": "s05-like-a-shepherd-at-evening.jpeg", "seg": "n2",
        "window": "21.75-27.76", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "FLOCK"],
        "narration": (
            "Like a shepherd at evening quietly dividing his flock, the sheep "
            "to one side and the goats to the other."
        ),
        "must_show": "SCRIPTURE-EXACT: the metaphor literal — the shepherd at the fold gate in gold evening light, staff guiding sheep through to one pen while the goats turn to the other side.",
        "must_not_show": "no halo, glare or rim-light; calm nightly routine — no fear in the animals, no drama; fleece and hair plainly different.",
        "scene": (
            "At a stone sheepfold in deep gold evening light the "
            "weathered shepherd stands at the gate with his long "
            "crooked staff laid gently across the stream of animals, "
            "turning the cream-fleeced sheep in through the opening "
            "one by one while the dark short-haired goats flow "
            "quietly to his other side toward a brush pen — an "
            "evening's calm, practised sorting he has done all his "
            "life, dust warm in the low sun around the animals' legs. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b06", "out": "s06-and-what-decided-which-side.jpeg", "seg": "n2",
        "window": "27.76-32.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["NATIONS"],
        "narration": (
            "And what decided which side you were on was not at all what people "
            "expect."
        ),
        "must_show": "the surprise set up — close along the front rank of gathered faces at dawn, every kind of person side by side, nothing visible marking anyone out.",
        "must_not_show": "no halo, glare or rim-light; no visible badge of difference anywhere — rich beside poor, old beside young, indistinguishable in what matters.",
        "scene": (
            "Close along the front rank of the multitude in the level "
            "dawn light: a prosperous merchant in deep plum stands "
            "shoulder to shoulder with a barefoot shepherd boy, an "
            "old woman leaning on her daughter's arm beside a broad "
            "young stonemason, a mother with an infant wrapped "
            "against her — every face waiting in the same light, and "
            "nothing anywhere on any of them to say which way they "
            "will go. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r033-b07", "out": "s07-to-the-first-group-the.jpeg", "seg": "n3",
        "window": "33.29-37.19", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PLAIN", "NATIONS"],
        "narration": "To the first group, the ones he welcomed in, the King said this.",
        "must_show": "the welcome side — the King turned fully toward the group at his right hand, his face already warm, they uncertain and hopeful before him.",
        "must_not_show": "no halo, glare or rim-light on the King; his warmth arrives BEFORE his words — the group's faces are ordinary and amazed.",
        "scene": (
            "On the rise the King has turned his whole body toward "
            "the great group gathered at his right hand, his face "
            "already open and warm before a word is spoken — and the "
            "front of the group stands in the strengthening dawn "
            "light with the look of people summoned somewhere they "
            "are not sure they belong: a stooped old field-hand "
            "turning his cap in his hands, a young mother hushing "
            "her child, all eyes on the King's face. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b08", "out": "s08-or-thirsty-and-gave-thee.jpeg", "seg": "j37",
        "window": "76.51-79.07", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "or thirsty, and gave thee drink?",
        "must_show": "the second mercy remembered — a close shot of a clay cup of water held steady to a parched child's lips by an old man's careful hands.",
        "must_not_show": "no halo, glare or rim-light; the care is in the steadiness of the hands — small, complete kindness.",
        "scene": (
            "A close shot in hard dusty afternoon light by a road: an "
            "old man's careful sun-spotted hands hold a dripping clay "
            "cup steady at the lips of a small parched child, his "
            "other hand cupped behind the small head, the water's "
            "wet line running from the cup's rim down the child's "
            "chin as it drinks with both small hands wrapped over "
            "the old fingers. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r033-b09", "out": "s09-come-ye-blessed-of-my.jpeg", "seg": "j1",
        "window": "37.87-62.85", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PLAIN", "NATIONS"],
        "narration": (
            "Come, ye blessed of my Father, inherit the kingdom prepared for "
            "you from the foundation of the world: For I was an hungred, and ye "
            "gave me meat: I was thirsty, and ye gave me drink: I was a "
            "stranger, and ye took me in: Naked, and ye clothed me: I was sick, "
            "and ye visited me: I was in prison, and ye came unto me."
        ),
        "must_show": "SCRIPTURE-EXACT: the great welcome — the King stepping DOWN from the rise into the right-hand group with both arms spread wide, the crowd's amazement breaking into joy around him.",
        "must_not_show": "no halo, glare or rim-light on the King; he comes DOWN to them — never beckoning from above; joy spreading outward through the faces like ripples.",
        "scene": (
            "The King has come down off the low rise into the very "
            "front of the right-hand multitude, both arms spread "
            "full wide in the strengthening morning light, his cream "
            "robe bright among their deep colours — and the welcome "
            "is landing in rings around him: the old field-hand's "
            "face breaking open, the young mother laughing and "
            "crying at once, a boy pushing forward to be nearer, "
            "amazement turning to joy as far back as faces can be "
            "seen. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r033-b10", "out": "s10-or-when-saw-we-thee.jpeg", "seg": "j37",
        "window": "85.12-89.56", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Or when saw we thee sick, or in prison, and came unto thee?",
        "must_show": "the last two mercies remembered — a young woman seated at a sick man's bedside by lamplight, sponging his brow; the visit itself.",
        "must_not_show": "no halo, glare or rim-light; the sickroom is humble and dim — presence is the gift; nothing clinical, nothing graphic.",
        "scene": (
            "A dim humble room by the light of one clay lamp: a "
            "young woman sits close on a stool at a low bed, wringing "
            "a cloth over a bowl with one hand while the other rests "
            "flat and calm on the fevered brow of a gaunt young man "
            "whose eyes have found her face — the long patient hours "
            "of simply having come and stayed written in the folds "
            "of her shawl slipping down. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b11", "out": "s11-the-good-people-are-confused.jpeg", "seg": "n5",
        "window": "91.94-94.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["NATIONS"],
        "narration": "The good people are confused.",
        "must_show": "the confusion — close on three faces in the right-hand group looking at one another, brows up, genuinely unable to place what they are being thanked for.",
        "must_not_show": "no halo, glare or rim-light; real puzzlement, warm and humble — no false modesty.",
        "scene": (
            "Close on three faces in the morning light of the "
            "right-hand group: the stooped old field-hand looking "
            "sideways at his neighbour with his brows climbed high, "
            "the neighbour's mouth half-open on a question, a "
            "grey-shawled woman between them searching her own "
            "memory with her eyes lifted — three people being "
            "thanked by a King for something they cannot for the "
            "life of them remember doing. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b12", "out": "s12-you-clothed-me-you-sat.jpeg", "seg": "n4",
        "window": "66.19-72.08", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "You clothed me, you sat with me when I was sick, you came to me "
            "when I was locked away."
        ),
        "must_show": "the mercies in one street — a passer-by wrapping his own heavy cloak around a shivering old man's shoulders on a cold grey day.",
        "must_not_show": "no halo, glare or rim-light; HIS OWN cloak — the giver walks on colder; cold grey light is correct here.",
        "scene": (
            "On a cold grey street under a flat winter sky a broad "
            "workman swings his own heavy dark cloak off his "
            "shoulders and down around a shivering white-bearded old "
            "man huddled on a doorstep, pulling it closed at the old "
            "man's throat with both hands — the giver left in his "
            "thin tunic with the wind moving it, already turning to "
            "go on his way. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r033-b13", "out": "s13-lord-when-saw-we-thee.jpeg", "seg": "j37",
        "window": "72.70-76.51", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PLAIN", "NATIONS"],
        "narration": "Lord, when saw we thee an hungred, and fed thee?",
        "must_show": "SCRIPTURE-EXACT: the question asked — an old man in the right-hand group asking it to the King's face, open-handed and baffled; the King's answering smile beginning.",
        "must_not_show": "no halo, glare or rim-light on the King; the asker is genuinely baffled — and the King is already delighted by the question.",
        "scene": (
            "Close in the morning light: the stooped old field-hand "
            "stands before the King with both hands open at his "
            "sides, his weathered face tipped up in honest "
            "bafflement as he asks — and the King looks down at him "
            "from a half-pace away with the beginning of a deep "
            "delighted smile, the smile of someone about to give "
            "away the best secret he has. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b14", "out": "s14-when-saw-we-thee-a.jpeg", "seg": "j37",
        "window": "79.07-82.85", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "When saw we thee a stranger, and took thee in?",
        "must_show": "the third mercy remembered — a family's doorway at dusk opened wide to a road-worn stranger woman, the table lamp already burning behind them.",
        "must_not_show": "no halo, glare or rim-light; the door opens WIDE, not a crack — welcome without suspicion.",
        "scene": (
            "At a low stone doorway in blue dusk a father holds the "
            "door wide with his whole arm while his wife reaches "
            "her hand out to a road-worn stranger woman standing "
            "with her bundle in the last light — behind them the "
            "family table already burns warm with its lamp and "
            "steams with the evening meal, and a child peers welcome "
            "from beside the doorpost. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b15", "out": "s15-or-naked-and-clothed-thee.jpeg", "seg": "j37",
        "window": "82.85-85.12", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "or naked, and clothed thee?",
        "must_show": "the fourth mercy remembered — close on a folded warm garment passing from one pair of hands into another pair, threadbare sleeves receiving it.",
        "must_not_show": "no halo, glare or rim-light; hands and cloth fill the frame — the exchange itself, dignity preserved.",
        "scene": (
            "A close shot in soft grey daylight: a thick folded wool "
            "garment in deep russet passes from a giver's two steady "
            "hands into the receiving hands of another — the "
            "receiver's sleeves threadbare and thin at the wrists, "
            "fingers closing over the heavy warm cloth with "
            "involuntary care — nothing in the frame but the two "
            "pairs of hands and the gift between them. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b16", "out": "s16-and-here-is-the-beautiful.jpeg", "seg": "n5",
        "window": "90.62-91.94", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PLAIN"],
        "narration": "And here is the beautiful part.",
        "must_show": "a close shot of the King's face at the edge of telling the secret — warmth banked and about to break.",
        "must_not_show": "no halo, glare or rim-light on the King; the face alone carries the beat — nothing else in frame.",
        "scene": (
            "A close portrait of the King's face in the clear "
            "morning light of the plain, the locked warm features "
            "at the very edge of a smile, eyes bright and steady on "
            "the unseen questioners — a man holding the best part "
            "of the story one breath longer before giving it away. "
            "The pale grass and dawn sky stand soft behind him. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b17", "out": "s17-they-say-lord-when-did.jpeg", "seg": "n5",
        "window": "94.01-99.28", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PLAIN", "NATIONS"],
        "narration": (
            "They say, Lord, when did we ever see you hungry, or thirsty, or "
            "sick, or in prison?"
        ),
        "must_show": "the question multiplied — a handful of the right-hand group all asking at once, hands open, heads shaking, the King listening to every one of them with delight.",
        "must_not_show": "no halo, glare or rim-light on the King; overlapping honest bafflement — a chorus of the same question.",
        "scene": (
            "Around the King in the morning light a half-circle of "
            "the right-hand group presses gently in, all asking at "
            "once — the old field-hand with his palms turned up, "
            "the young mother shaking her head slowly, the "
            "stonemason spreading his big empty hands, a girl "
            "looking from face to face for anyone who remembers — "
            "while the King stands in the middle of the chorus "
            "listening to every one of them with open delight. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b18", "out": "s18-they-do-not-even-remember.jpeg", "seg": "n5",
        "window": "99.28-104.97", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "They do not even remember doing anything special. They just helped "
            "whoever was in front of them."
        ),
        "must_show": "unremembered kindness — a woman passing bread to a beggar with one hand WHILE her attention is on the market ahead; kindness so habitual it doesn't interrupt her stride.",
        "must_not_show": "no halo, glare or rim-light; the giving happens at the EDGE of her attention — reflex, not occasion; the beggar's face registers it fully.",
        "scene": (
            "In a busy midday market lane a woman with a full basket "
            "on her hip passes a small loaf down into a seated "
            "beggar's bowl with her free hand without breaking "
            "stride, her face already turned ahead to the stalls, "
            "the gift given the way other people brush past — while "
            "below her the old beggar's upturned face holds the "
            "loaf's arrival like a sunrise. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b19", "out": "s19-they-were-not-keeping-score.jpeg", "seg": "n6",
        "window": "105.65-109.60", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "They were not keeping score. They were not trying to earn anything.",
        "must_show": "no ledger anywhere — a man quietly leaving a filled water jar and bread at a sleeping stranger's side and walking away unseen.",
        "must_not_show": "no halo, glare or rim-light; the giver is LEAVING the frame — no witness, no thanks, no record; that is the whole picture.",
        "scene": (
            "In the deep shade of a wall at hot midday a traveller "
            "lies asleep with his head on his pack — and beside him "
            "a full water jar and a wrapped loaf have just been set "
            "down by a man already three paces gone, walking away "
            "up the lane without looking back, his shadow passing "
            "out of the frame's edge. No one sees. Nothing is "
            "counted. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r033-b20", "out": "s20-kindness-was-simply-their-reflex.jpeg", "seg": "n6",
        "window": "109.60-116.01", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PLAIN", "NATIONS"],
        "narration": (
            "Kindness was simply their reflex. And then the King tells them the "
            "secret behind all of it."
        ),
        "must_show": "the secret about to land — the King gathering the nearest of the right-hand group close with a hand on the old man's shoulder, bending in as if to confide.",
        "must_not_show": "no halo, glare or rim-light on the King; the posture of confiding — bent head, gathered circle — before the greatest sentence.",
        "scene": (
            "In the bright morning the King draws the nearest of "
            "the group in close — one hand laid on the old "
            "field-hand's shoulder, his head bent toward the small "
            "gathered half-circle of faces like a man about to "
            "confide the secret of his whole kingdom — and they "
            "lean in around him, the mother's child reaching up "
            "unnoticed to touch the cream sleeve. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b21", "out": "s21-verily-i-say-unto-you.jpeg", "seg": "j2",
        "window": "116.58-124.85", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PLAIN", "NATIONS"],
        "narration": (
            "Verily I say unto you, Inasmuch as ye have done it unto one of the "
            "least of these my brethren, ye have done it unto me."
        ),
        "must_show": "SCRIPTURE-EXACT and ⚑ Flag J: the secret embodied — the King drawing a ragged, least-looking beggar man forward BESIDE himself at the seat, presenting him to the group as his own brother.",
        "must_not_show": "no halo, glare or rim-light on the King; the beggar keeps his own ordinary face (never Jesus-faced); the King's arm around him makes the identification — nearness, not likeness.",
        "scene": (
            "At the stone seat the King stands with his arm wrapped "
            "full around the shoulders of a ragged, road-worn "
            "beggar man — dust-grey clothes, bewildered ordinary "
            "face — drawing him firmly forward to stand BESIDE "
            "himself before the whole multitude, presenting him the "
            "way a man presents his own brother, his other hand "
            "open toward the group as the sentence lands on them. "
            "Morning light on both faces alike. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b22", "out": "s22-he-was-in-them-the.jpeg", "seg": "n7",
        "window": "125.91-127.37", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "He was in them the whole time.",
        "must_show": "the realization — close on the old field-hand's face as it lands, his eyes going back through a lifetime of small kindnesses, undone.",
        "must_not_show": "no halo, glare or rim-light; one face, one lifetime recalculating — tears allowed, spectacle not.",
        "scene": (
            "A close portrait of the old field-hand's weathered face "
            "in the morning light at the instant the sentence "
            "lands: his eyes gone still and far away, back through "
            "every bowl of soup and borrowed coat of a long plain "
            "life, his chin beginning to tremble under the white "
            "stubble — a man discovering who it was he had been "
            "feeding all along. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r033-b23", "out": "s23-every-hungry-person-every-stranger.jpeg", "seg": "n7",
        "window": "127.37-136.31", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Every hungry person, every stranger, every sick and forgotten and "
            "locked-away person, was him, wearing a disguise."
        ),
        "must_show": "the least of these, gathered in one frame — a line of the row's needy figures (hungry man, thirsty child, stranger woman, cold old man, sick young man) standing together in plain dignity, facing the camera.",
        "must_not_show": "no halo, glare or rim-light; their own ordinary faces, never Jesus-faced — the dignity of the framing does the revealing.",
        "scene": (
            "Against a plain warm wall in level golden light they "
            "stand together in one quiet line facing the camera — "
            "the gaunt man who was hungry, the small child who was "
            "thirsty, the road-worn stranger woman with her bundle, "
            "the white-bearded old man in the borrowed cloak, the "
            "young man still pale from his sickbed — each utterly "
            "ordinary, each framed with the unhurried dignity of a "
            "royal portrait. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r033-b24", "out": "s24-the-others-missed-him-for.jpeg", "seg": "n8",
        "window": "136.88-139.10", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "The others missed him for the very same reason.",
        "must_show": "⚑ Flag J, grief not doom — a well-dressed man walking briskly PAST a huddled beggar, eyes fixed ahead, the miss itself in one frame.",
        "must_not_show": "no halo, glare or rim-light; NO doom imagery, no darkness closing in — just the quiet tragedy of a man walking past; the passer-by is hurried, not monstrous.",
        "scene": (
            "On a handsome stone street in ordinary afternoon light "
            "a well-dressed man in deep plum strides briskly past a "
            "huddled beggar without a flicker of his eyes, his gaze "
            "fixed ahead on some appointment, robes swinging — and "
            "the beggar's half-raised hand is already sinking back "
            "to his knee, used to it — two men a footstep apart, "
            "and a whole kingdom missed in the space between them. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b25", "out": "s25-they-were-waiting-to-serve.jpeg", "seg": "n8",
        "window": "139.10-146.68", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "They were waiting to serve a King on a throne, and they walked "
            "right past him a hundred times, because he did not look like a "
            "King."
        ),
        "must_show": "the hundred misses — a busy street where fine-robed men hurry in every direction, and at its centre, unseen by all of them, one needy figure sits with his bowl.",
        "must_not_show": "no halo, glare or rim-light; the passers-by are respectable, devout-looking people — the miss is not villainy but blindness.",
        "scene": (
            "A busy street in bright day: fine-robed, respectable "
            "men and women stream through in every direction — one "
            "consulting a scroll as he walks, two deep in earnest "
            "religious talk, a woman directing servants with "
            "parcels — and at the exact centre of all the moving "
            "colour a thin man sits motionless against a post with "
            "his empty bowl, occupying the one spot every eye in "
            "the frame has learned not to land on. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b26", "out": "s26-he-looked-like-someone-who.jpeg", "seg": "n8",
        "window": "146.68-149.47", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "He looked like someone who needed help.",
        "must_show": "a close portrait of that thin man by his post — an ordinary, tired, needful face, held with complete dignity by the frame.",
        "must_not_show": "no halo, glare or rim-light; his own face, never Jesus-faced — but the portrait is framed with the reverence usually spent on kings.",
        "scene": (
            "A close portrait of the thin man against his post in "
            "the bright street light: an ordinary tired face, "
            "sun-cracked lips, eyes patient and a little far away, "
            "a mended shawl at his neck — painted with the full "
            "unhurried reverence of a royal portrait, filling the "
            "frame the way kings fill coins, while the crowd's "
            "colours blur past behind him. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b27", "out": "s27-that-is-how-good-he.jpeg", "seg": "n9",
        "window": "150.00-154.93", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OLIVET"],
        "narration": (
            "That is how good he is. He did not hide himself behind something "
            "impressive."
        ),
        "must_show": "back on the dusk hillside — a close shot of Jesus saying it to his friends, the teller and the King the same face.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the quiet joke of it in his eyes — the King telling them where he hides.",
        "scene": (
            "Close on Jesus's face on the dark hillside, the deep "
            "dusk blue behind him and the faint warmth of "
            "Jerusalem's far lamps below: the same face the "
            "multitude saw on the dawn plain, here plain and tired "
            "and near, with something almost amused resting in the "
            "warm brown eyes — a King telling his friends exactly "
            "where he intends to hide. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b28", "out": "s28-he-hid-in-the-people.jpeg", "seg": "n9",
        "window": "154.93-161.25", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "He hid in the people easiest to overlook, so that plain, ordinary "
            "kindness would always reach him."
        ),
        "must_show": "the hiding places — a dusk street where the overlooked are visible in every corner: the beggar by the wall, the old woman at the well, the stranger at the gate; every one of them a door to him.",
        "must_not_show": "no halo, glare or rim-light; nothing marks them out except the composition quietly finding each one — the eye taught to see.",
        "scene": (
            "A village street at warm dusk, lamps beginning in the "
            "windows: and the composition quietly finds them all — "
            "the beggar folded small by the wall, the bent old "
            "woman resting her jar on the well's rim, the "
            "road-stained stranger hesitating at the gate's edge, a "
            "thin child watching from a doorway — each one set at a "
            "point where the light falls kindly, a street full of "
            "hiding places for a King. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r033-b29", "out": "s29-so-when-someone-small-and.jpeg", "seg": "n9",
        "window": "161.25-167.74", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "So when someone small and needy stands in front of you, that is "
            "not an interruption. It might be him."
        ),
        "must_show": "the closing image — from over a viewer-like shoulder, a small needy child standing directly in front, hand half-raised, eyes up into the camera's own face.",
        "must_not_show": "no halo, glare or rim-light; the child looks INTO the camera — the frame puts the viewer in the story's last seat; tender, not sentimental.",
        "scene": (
            "From just over an anonymous shoulder at the frame's "
            "dark edge, in the warm last light of the day: a small "
            "thin child stands directly in front, one hand "
            "half-raised in the smallest possible asking, dusty "
            "feet planted, and the wide dark eyes looking straight "
            "up past the shoulder into the camera itself — the "
            "question of the whole story standing four feet tall "
            "and waiting for an answer. Every figure has two arms, "
            "two hands and one head."
        ),
    },
]
