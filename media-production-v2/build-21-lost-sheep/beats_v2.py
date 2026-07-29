#!/usr/bin/env python3
"""V2 beat map — row 21, build-21-lost-sheep (Luke 15:1-7).

COVERAGE: 21 pictures against V1's 7, over 119.6 s = 5.7 s/picture.

SCRIPTURE FACTS (Luke 15:1-7 KJV):
  v1-2 "then drew near unto him ALL the publicans and sinners for to hear him.
       And the Pharisees and scribes MURMURED, saying, This man RECEIVETH
       SINNERS, AND EATETH WITH THEM." The frame story is a shared table, and the
       complaint is specifically about EATING with them.
  v4   "leave the ninety and nine IN THE WILDERNESS, and go after that which is
       lost, UNTIL HE FIND IT" — he abandons the ninety-nine in open country,
       which is reckless, and he does not stop searching.
  v5   "he layeth it ON HIS SHOULDERS, REJOICING" — the shepherd's carry, across
       both shoulders with the legs held at his chest, and the emotion is JOY,
       not relief and not irritation. The narration hammers that distinction in
       three separate one-line sentences, so it gets its own frame.
  v6   "Rejoice with me; for I have found MY SHEEP which was lost" — MY. The
       narration's point at n9b: it was his the whole time it was missing.
  v7   "joy shall be in HEAVEN over one sinner that repenteth."

⚠️ THE SAME FRAME-STORY OCCASION AS ROW 2 AND ROW 8. Luke 15 holds all three
parables — prodigal (row 2), lost coin (row 8) and this one — told at one sitting
to one audience. Rows 2 and 8 already staged that opening, so this build must NOT
repeat either composition: row 2 used a courtyard table with three standing
Pharisees; row 8 used Jesus seated on a low wall under a fig tree. This one is
staged INSIDE a house at a crowded meal, with the religious men out in the
doorway looking in and refusing to come through it. Same occasion, three
different rooms, no repeated picture across the library.

CONTENT-CARE: row 21 is GREEN. The sheep is frightened and tangled but never
injured — no blood, no wounds. v7's "joy in heaven" is NOT painted: no clouds,
no angels, no light in the sky. The party on the ground is what we show, exactly
as row 8 handled the same problem.

TIME OF DAY: the frame story is warm evening lamplight indoors. The parable runs
from late afternoon on the hills, through full night on the rocks during the
search, to the next evening's celebration by lamp and firelight.
"""

LOCKS = {
    "SHEPHERD": (
        "SHEPHERD LOCK: the shepherd is the same man in every shot — about forty, "
        "lean and hard-used, deeply sun-darkened skin, a rough dark beard, and "
        "creased weather-worn eyes. He wears a coarse DARK BROWN wool tunic under a "
        "heavy sleeveless sheepskin over one shoulder, a wide leather belt with a "
        "slung water skin, and worn sandals (never cream, never white). He carries a "
        "long crooked staff. His face is shown clearly."
    ),
    "SHEEP": (
        "SHEEP LOCK: the lost sheep is one particular animal — a smallish "
        "cream-fleeced ewe, its wool matted and dirty grey with dust and burrs, dark "
        "legs and a dark face, long ears, and wide dark frightened eyes. It is never "
        "injured, bleeding or wounded — only dirty, tangled and exhausted."
    ),
    "HILLS": (
        "HILL COUNTRY LOCK: the rough grazing country of Judea — steep stony "
        "hillsides of thin dry grass and thorn scrub, outcrops of pale limestone, "
        "narrow sheep tracks, boulder fields and deep shadowed ravines cutting down "
        "between the ridges. Bare, empty and hard walking, with distant ridgelines "
        "rolling away."
    ),
    "HOUSE": (
        "HOUSE LOCK: a modest village house — one main room with a beaten earth "
        "floor, a low table set with bread, olives, fish and clay cups, rush mats and "
        "cushions around it, a cooking hearth in the corner and shelves of clay jars, "
        "and a low doorway open to the evening. Lit warmly and unevenly by clay oil "
        "lamps and the low fire, with deep shadow in the corners."
    ),
    "GUESTS": (
        "GUESTS LOCK: the people at the table are ordinary working folk and tax "
        "collectors of every age — labourers, a fisherman, two women, an old man, a "
        "young tax collector still in his good belt — crowded shoulder to shoulder on "
        "the mats. They wear SATURATED DEEP earth colours: dark chocolate brown, deep "
        "russet, burnt ochre, dark olive, dusty indigo and faded plum wool. None "
        "wears off-white, ivory or any near-white cloth. Their faces are shown clearly."
    ),
    "RELIGIOUS": (
        "RELIGIOUS MEN LOCK: the scribes and Pharisees are the same three men in "
        "every shot — older, with long carefully combed grey and iron-grey beards and "
        "watchful disapproving eyes. They wear finely woven, DEEPLY DYED robes of "
        "NEAR-BLACK indigo and DARK UMBER with woven dark-red borders, and prayer "
        "shawls of that SAME saturated near-black and dark-indigo wool with dark "
        "stripes and dark fringe. Their faces are shown clearly."
    ),
    "VILLAGE": (
        "VILLAGE LOCK: a small hill village of honey-coloured stone — low flat-roofed "
        "houses around a beaten-earth yard, a stone sheepfold with a brush-topped "
        "wall, a well, a fig tree, and the dark hills rising beyond the rooftops."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------------ n1/n2 — the murmuring ----
    {
        "id": "v2-r021-b01", "out": "s01-they-crowded-in-close.jpeg", "seg": "n1",
        "window": "0.28-7.71", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GUESTS", "HOUSE"],
        "narration": ("The people everyone else had written off — the cheats, the "
                      "outcasts, the ones with a past — kept crowding in close to hear "
                      "Jesus."),
        "must_show": "a crowded lamplit house with Jesus AT the table among ordinary people and tax collectors, everyone pressed in close to him.",
        "must_not_show": "no halo, glare or rim-light; he must NOT be set apart or given space — the crowding is the point.",
        "scene": (
            "Inside a small warm lamplit house, a low table is crowded on every side "
            "with ordinary people eating together — a labourer with his sleeves rolled, "
            "a young tax collector, two women, an old man, more sitting behind on the "
            "floor. Jesus sits in among them at the same level with a cup in his hand, "
            "leaning in to listen to the man beside him, and there is no space "
            "whatever around him. Every face nearby is turned his way. Warm uneven "
            "lamplight, deep shadow at the walls. The camera is back far enough to "
            "hold the whole table. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r021-b02", "out": "s02-they-muttered-in-the-doorway.jpeg", "seg": "n2",
        "window": "8.36-10.45", "wide": True, "jesus": False, "ref": False,
        "locks": ["RELIGIOUS", "HOUSE"],
        "narration": "And the religious men muttered about it.",
        "must_show": "the three religious men standing OUTSIDE the low doorway looking in — refusing to cross the threshold, heads together.",
        "must_not_show": "they must NOT be inside the room or at the table; the doorway they will not step through is the whole composition. Do not put Jesus in this frame.",
        "scene": (
            "Seen from inside the warm room looking out: three men in near-black robes "
            "stand OUTSIDE the low doorway in the blue evening, framed by the opening "
            "and lit only along one edge by the lamplight spilling out to them. Their "
            "heads are inclined together and one is speaking behind his hand, all three "
            "looking past the camera into the crowded room. Not one of them has "
            "stepped over the threshold. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r021-b03", "out": "s03-he-eateth-with-them.jpeg", "seg": "s2 + n2b",
        "window": "11.09-18.59", "wide": True, "jesus": True, "ref": REF,
        "locks": ["RELIGIOUS", "GUESTS", "HOUSE"],
        "narration": ("This man receiveth sinners, and eateth with them. (Luke 15:2) — "
                      "This man welcomes sinners, they said, and even eats with them."),
        "must_show": "SCRIPTURE-EXACT: the specific offence — Jesus sharing FOOD, bread passing from his hand to a tax collector's, with the dark shapes in the doorway watching it.",
        "must_not_show": "no halo, glare or rim-light; the complaint is about eating, so the food must be the visible action.",
        "scene": (
            "At the crowded table Jesus is handing a torn piece of bread directly into "
            "the hand of the young tax collector beside him, the two hands meeting over "
            "the cups, both men mid-conversation and easy with each other. Beyond them "
            "through the low doorway the three dark-robed figures stand in the blue "
            "evening watching that exchange, faces tight. Warm lamplight on the table, "
            "cold dusk in the door. The camera holds the table and the doorway in one "
            "frame. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r021-b04", "out": "s04-so-he-told-them-a-story.jpeg", "seg": "n3",
        "window": "19.26-23.53", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GUESTS", "HOUSE"],
        "narration": ("So Jesus told them a story about how heaven really feels about "
                      "one lost person."),
        "must_show": "Jesus setting down his cup and beginning the story, the room quieting and turning to him.",
        "must_not_show": "no halo, glare or rim-light; he is not answering angrily — he is answering with a story.",
        "scene": (
            "Jesus has set his cup down on the low table and lifted one hand in the "
            "open gesture of a man beginning a story, his face warm and unhurried. All "
            "around the table the talking has stopped and faces are turning in toward "
            "him, one woman shushing a child, the tax collector leaning forward on his "
            "elbows. Warm lamplight, deep shadow beyond. The camera is back far enough "
            "to hold the table and Jesus. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    # ------------------------------------------------- j1/n4 — the question ----
    {
        "id": "v2-r021-b05", "out": "s05-an-hundred-sheep.jpeg", "seg": "j1 a",
        "window": "24.21-29.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "HILLS"],
        "narration": ("What man of you, having an hundred sheep, if he lose one of them, "
                      "(Luke 15:4)"),
        "must_show": "the whole flock on the hillside in late afternoon light — a big scattered flock, the shepherd small among them.",
        "must_not_show": "nothing wrong yet; this is the flock intact. Do not put Jesus in this frame.",
        "scene": (
            "A wide view of a large flock of sheep spread out grazing across a steep "
            "stony hillside in low late-afternoon light — a hundred animals scattered "
            "over the thin grass and rock, and the shepherd standing among them leaning "
            "on his long crooked staff, small against the size of the country. The bare "
            "ridges roll away behind. Warm sideways light and long shadows. He has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r021-b06", "out": "s06-one-of-them-is-gone.jpeg", "seg": "j1 b",
        "window": "29.0-33.54", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "HILLS"],
        "narration": ("doth not leave the ninety and nine in the wilderness, and go "
                      "after that which is lost, until he find it? (Luke 15:4)"),
        "must_show": "the shepherd counting and stopping — his hand halted mid-count, his head coming up, the flock around him.",
        "must_not_show": "do not put Jesus in this frame; the moment of realisation is the beat.",
        "scene": (
            "Close on the shepherd standing among his flock with one hand halted "
            "mid-count in the air and his head come up sharply, his eyes moving fast "
            "across the hillside. His mouth has stopped on a number. The sheep press "
            "around his knees, unbothered. Low warm afternoon light on his weathered "
            "face. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r021-b07", "out": "s07-would-you-not-go.jpeg", "seg": "n4",
        "window": "34.55-42.95", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GUESTS", "RELIGIOUS", "HOUSE"],
        "narration": ("Which of you, he asks, with a hundred sheep, would not leave the "
                      "ninety-nine behind to go after the one that wandered off, and "
                      "keep searching until you found it?"),
        "must_show": "back in the room: Jesus putting the question to the whole table — and the men in the doorway included in it by his open hand.",
        "must_not_show": "no halo, glare or rim-light; the question is warm and genuinely put to everyone, including the three outside.",
        "scene": (
            "Jesus has turned slightly and opened his hand in a question that takes in "
            "the whole crowded table — and the gesture carries on past them toward the "
            "low doorway where the three dark-robed men are still standing outside. "
            "Faces around the table are nodding; every shepherd in the room knows the "
            "answer. The men in the doorway have not moved. Warm lamplight. The camera "
            "holds the table, Jesus and the doorway. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    # -------------------------------------------- n5 — he leaves the ninety-nine ----
    {
        "id": "v2-r021-b08", "out": "s08-not-counting-what-he-has.jpeg", "seg": "n5 p1",
        "window": "43.62-46.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD"],
        "narration": "He does not stand there counting what he still has.",
        "must_show": "close on the shepherd's face turned away from the flock entirely, already scanning the ravines — the ninety-nine forgotten behind him.",
        "must_not_show": "do not put Jesus in this frame; he is not weighing it up.",
        "scene": (
            "Close on the shepherd's weathered face, turned completely away from the "
            "flock and looking off and down across the broken country, his eyes "
            "narrowed and searching the ravines, his jaw set. The blurred woolly backs "
            "of the sheep fill the bottom edge of the frame behind him and he is not "
            "looking at a single one of them. Low warm light. He has one head."
        ),
    },
    {
        "id": "v2-r021-b09", "out": "s09-he-leaves-them-behind.jpeg", "seg": "n5 p2",
        "window": "46.08-50.08", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "HILLS"],
        "narration": ("He leaves the ninety-nine behind to go out after the one that is "
                      "gone."),
        "must_show": "SCRIPTURE-EXACT (v4): him walking AWAY from the whole flock into the empty broken country — the ninety-nine left in the open wilderness behind him.",
        "must_not_show": "he does not pen them or hand them to anyone — v4 leaves them in the wilderness, which is reckless and is the point.",
        "scene": (
            "SHOT FROM BEHIND THE FLOCK: the ninety-nine sheep are spread out grazing "
            "across the open hillside in the foreground with no fold and nobody "
            "watching them, and beyond them the shepherd is already some way off, "
            "striding away down into the broken stony country with his staff, his back "
            "to every one of them. He is not looking round. Long low light, the "
            "ravines going into shadow ahead of him. He has two arms, two hands and "
            "one head."
        ),
    },
    # ---------------------------------------------------- n6 — the search ----
    {
        "id": "v2-r021-b10", "out": "s10-over-the-rocks-and-ravines.jpeg", "seg": "n6 p1a",
        "window": "50.74-54.5", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "HILLS"],
        "narration": ("He searches through the night, over the rocks and the ravines,"),
        "must_show": "the shepherd climbing down through boulders and a black ravine at night, tiny against the country, working hard.",
        "must_not_show": "this must look genuinely difficult and dangerous; no gentle stroll. Do not put Jesus in this frame.",
        "scene": (
            "Night on the hills. The shepherd is picking his way down through a field "
            "of boulders into a black ravine, one hand braced on rock and his staff "
            "out for balance, his body low and working hard at the descent. He is small "
            "against the enormous broken country. Cold moonlight silvers the stone and "
            "the ravine below him is pure black. He has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r021-b11", "out": "s11-calling-into-the-dark.jpeg", "seg": "n6 p1b",
        "window": "54.5-58.15", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "HILLS"],
        "narration": ("calling into the dark, because to him that one is not a loss he "
                      "can shrug off."),
        "must_show": "him stopped on a ridge with his head back and his hands cupped at his mouth, calling out across black empty country.",
        "must_not_show": "no answer visible anywhere; the emptiness he is calling into is the beat.",
        "scene": (
            "The shepherd stands on a bare ridge in the dark with his head thrown back "
            "and both hands cupped around his mouth, calling out across the country. "
            "Below and around him the ravines and hillsides are black and completely "
            "empty, ridge after ridge fading away under a cold sky of stars. Nothing "
            "answers. His breath shows in the night air. The camera is well back so "
            "the emptiness dominates. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r021-b12", "out": "s12-that-one-is-his.jpeg", "seg": "n6 p2",
        "window": "58.15-59.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD"],
        "narration": "That one is his.",
        "must_show": "close on the shepherd's face in the dark — exhausted, scratched, and completely unwilling to stop.",
        "must_not_show": "no despair; stubborn love. Do not put Jesus in this frame.",
        "scene": (
            "Very close on the shepherd's face at night, lit cold and low by "
            "moonlight. He is filthy and worn out, a thorn scratch across one cheek, "
            "his hair damp with the effort — and his eyes are hard and absolutely set. "
            "There is no give in the expression at all. He is not going to stop. Black "
            "rock behind him. He has one head."
        ),
    },
    # --------------------------------------------------- n7/j2 — he finds it ----
    {
        "id": "v2-r021-b13", "out": "s13-tangled-in-the-thorns.jpeg", "seg": "n7 a",
        "window": "60.42-65.0", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEEP", "HILLS"],
        "narration": ("And when he finds it — frightened, tangled in the thorns, too "
                      "worn out to walk —"),
        "must_show": "the sheep caught in a thorn thicket in the dark — matted, burr-covered, wide-eyed with fear, too spent to struggle.",
        "must_not_show": "CONTENT-CARE — the animal is dirty and exhausted but NEVER injured: no blood, no wounds. Do not put Jesus in this frame.",
        "scene": (
            "Close on the lost ewe in the dark, wedged down among the roots of a thorn "
            "thicket with dry branches closed over its back, its cream fleece matted "
            "grey with dust and thick with burrs and twigs. Its dark face is turned up "
            "and its eyes are wide and frightened, and it has stopped struggling "
            "entirely — too worn out to move. There is no injury on it anywhere. Cold "
            "moonlight through the thorns."
        ),
    },
    {
        "id": "v2-r021-b14", "out": "s14-he-does-not-scold-it.jpeg", "seg": "n7 b",
        "window": "65.0-69.34", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "SHEEP", "HILLS"],
        "narration": "he does not scold it, and he does not leave it there.",
        "must_show": "him down on his knees in the thorns working the branches back off the animal with bare hands, his face gentle.",
        "must_not_show": "no anger and no roughness anywhere; he is taking thorns to get it out. Do not put Jesus in this frame.",
        "scene": (
            "The shepherd is down on both knees in the dark thicket, forcing the thorn "
            "branches back and away from the trapped ewe with his bare hands, careless "
            "of what they are doing to his forearms. His face bent over the animal is "
            "entirely gentle — no anger in it at all — and he is saying something to it "
            "as he works. Cold moonlight on the tangle. The camera is close enough to "
            "hold both. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r021-b15", "out": "s15-on-his-shoulders-rejoicing.jpeg", "seg": "j2",
        "window": "70.00-72.97", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "SHEEP", "HILLS"],
        "narration": ("And when he hath found it, he layeth it on his shoulders, "
                      "rejoicing. (Luke 15:5)"),
        "must_show": "SCRIPTURE-EXACT: the shepherd's carry — the ewe laid ACROSS BOTH SHOULDERS behind his neck with its legs gathered and held at his chest.",
        "must_not_show": "not cradled in his arms and not slung over one shoulder — across both, the way a shepherd actually carries. Do not put Jesus in this frame.",
        "scene": (
            "The shepherd is straightening up out of the thicket with the ewe laid "
            "ACROSS BOTH HIS SHOULDERS behind his neck, its four legs gathered "
            "together and gripped in his two hands at his chest, its head hanging "
            "beside his own. His staff is caught up under one arm. He is taking the "
            "full weight of the animal and beginning to climb. Cold moonlight on the "
            "rock and the dirty fleece. The camera is back far enough to see him head "
            "to sandals. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r021-b16", "out": "s16-not-relieved-rejoicing.jpeg", "seg": "n8",
        "window": "74.06-83.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "SHEEP"],
        "narration": ("He lifts it up, lays it across his own shoulders, and carries it "
                      "the whole way home, rejoicing. Not relieved. Not annoyed at the "
                      "trouble. Rejoicing."),
        "must_show": "⚠️ THE FACE THE NARRATION SPENDS THREE SENTENCES ON: close on the shepherd carrying — openly, helplessly HAPPY. Grinning, laughing, delighted.",
        "must_not_show": "NOT relief (no blown-out breath, no closed eyes), NOT irritation, NOT weary duty. If this face reads as anything but joy the beat has failed. Do not put Jesus in this frame.",
        "scene": (
            "Close on the shepherd's face as he climbs with the ewe across his "
            "shoulders. He is openly, helplessly delighted — a broad unguarded grin "
            "splitting his filthy scratched face, his eyes bright and creased at the "
            "corners, his head tipped back a little as he laughs out loud into the "
            "night air. He is filthy, bleeding from thorns and carrying a heavy animal "
            "uphill, and he could not be happier. The ewe's head hangs beside his. "
            "Cold moonlight, first grey of dawn behind. He has one head."
        ),
    },
    # ------------------------------------------------- n9 / j3 — the party ----
    {
        "id": "v2-r021-b17", "out": "s17-he-calls-everyone-together.jpeg", "seg": "n9",
        "window": "84.58-90.34", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "SHEEP", "VILLAGE"],
        "narration": ("Then he calls everyone together — friends, neighbors, the whole "
                      "village — and throws a celebration."),
        "must_show": "him arriving in the village yard with the sheep still on his shoulders, shouting for everyone, people already coming out of doorways.",
        "must_not_show": "he has not put the sheep down yet — he wants them to SEE it. Do not put Jesus in this frame.",
        "scene": (
            "The shepherd strides into the beaten-earth yard of the hill village with "
            "the ewe still across his shoulders, one arm flung up and his head back, "
            "shouting for the whole place at once. All around, people are coming out "
            "of the low doorways — a woman with a child on her hip, two men from the "
            "sheepfold wall, an old man rising off a bench — heads turning toward him. "
            "Early evening light on the honey-coloured stone. The camera is back far "
            "enough to hold the yard. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r021-b18", "out": "s18-rejoice-with-me.jpeg", "seg": "j3 + n9b p1",
        "window": "91.01-96.43", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "SHEEP", "VILLAGE"],
        "narration": ("Rejoice with me; for I have found my sheep which was lost. "
                      "(Luke 15:6) — Be glad with me, he tells them."),
        "must_show": "the celebration underway in the lamplit yard — neighbours crowded round him, food coming out, the dirty ewe set down in the middle of all of it.",
        "must_not_show": "the party must look far too big for one animal — that mismatch is the parable. Do not put Jesus in this frame.",
        "scene": (
            "The village yard is full. Twenty neighbours have crowded in around the "
            "shepherd, laughing and gripping his shoulders, and bread and a jug are "
            "already coming out of a doorway; a lamp has been hung on the fig tree. In "
            "the middle of all of it the one dirty burr-matted ewe stands on the packed "
            "earth being fussed over by two children. It is a whole village's worth of "
            "joy over one animal. Warm lamplight and last daylight. The camera holds "
            "the crowded yard. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r021-b19", "out": "s19-it-was-his-the-whole-time.jpeg", "seg": "n9b p2-p3",
        "window": "96.43-100.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "SHEEP"],
        "narration": ("Not, I got my property back. It was his the whole time it was "
                      "missing."),
        "must_show": "close on the shepherd's hands in the dirty fleece and his face bent to the animal — ownership as affection, not accounting.",
        "must_not_show": "nothing transactional in the frame — no counting, no inspecting. Do not put Jesus in this frame.",
        "scene": (
            "Close on the shepherd crouched down to the ewe in the lamplit yard, both "
            "scratched hands buried in the matted wool of its neck and his forehead "
            "come down almost to its head, his eyes shut and a smile on his mouth. He "
            "is not inspecting the animal or checking it over; he is just holding on "
            "to it. Warm lamplight on dirty fleece and worn hands. Each hand has five "
            "fingers."
        ),
    },
    # ----------------------------------------------------- j4 / n10 — heaven ----
    {
        "id": "v2-r021-b20", "out": "s20-joy-over-one-sinner.jpeg", "seg": "j4",
        "window": "101.61-110.57", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GUESTS", "RELIGIOUS", "HOUSE"],
        "narration": ("I say unto you, that likewise joy shall be in heaven over one "
                      "sinner that repenteth, more than over ninety and nine just "
                      "persons, which need no repentance. (Luke 15:7)"),
        "must_show": "back in the lamplit room, Jesus finishing the story — glad, and looking toward the doorway as he says it.",
        "must_not_show": "CONTENT-CARE — do NOT paint heaven, angels, clouds or light in the sky. Nothing supernatural in the frame. No halo or rim-light on Jesus.",
        "scene": (
            "Back at the crowded table in the warm lamplit room, Jesus is finishing the "
            "story with both hands open, his face openly glad — and his eyes have gone "
            "past the table to the low doorway where the three men in near-black robes "
            "are still standing outside in the dark, listening. The people at the table "
            "are watching him. There is nothing in the sky and nothing supernatural "
            "anywhere in the frame. Warm uneven lamplight. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r021-b21", "out": "s21-not-a-lecture-joy.jpeg", "seg": "n10",
        "window": "111.48-119.19", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GUESTS", "RELIGIOUS", "HOUSE"],
        "narration": ("That is how good he is. Heaven throws a party over one person "
                      "turning back. Not a lecture. Not a grudge. Joy."),
        "must_show": "the closing frame: the warm crowded table going on, and ONE of the three men in the doorway having taken a single step over the threshold.",
        "must_not_show": "no halo, glare or rim-light; do not resolve it — only one man, only one step, the other two still outside. The parable leaves it open.",
        "scene": (
            "A final wide view of the warm lamplit room. The table is loud and glad "
            "again, food going round, Jesus among them laughing at something the tax "
            "collector has said. And at the low doorway one of the three dark-robed men "
            "has taken a single step INSIDE the threshold and stopped there, half in "
            "the lamplight and half in the dark, his face uncertain — while the other "
            "two remain outside in the blue evening behind him. Nothing is resolved. "
            "Warm light, cold doorway. The camera holds the room and the door. Every "
            "figure has two arms, two hands and one head."
        ),
    },
]
