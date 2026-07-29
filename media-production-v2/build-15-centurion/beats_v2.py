#!/usr/bin/env python3
"""V2 beat map — row 15, build-15-centurion (Matthew 8:5-13).

COVERAGE: 42 pictures against V1's 12, over 240.8 s = 5.7 s/picture.

AUDIO NOTE: this row's segments are still edge-tts (en-US-AndrewNeural /
en-US-ChristopherNeural) — audio pre-Alexander, re-render after the revoice pass.
Built anyway; the word-anchored markers make the re-render automatic later.

SCRIPTURE FACTS (Matthew 8:5-13 KJV):
  v5   a CENTURION comes to him in Capernaum — an officer of the occupying army,
       coming to a Jewish teacher. Both facts have to be legible in every frame:
       he is unmistakably Roman, and he is unmistakably asking.
  v6   "my SERVANT lieth at home sick of the palsy, grievously TORMENTED" — a
       slave, not a son. The narration leans hard on that; a servant was property.
  v7   "I WILL COME and heal him" — Jesus offers to enter a Roman house with no
       hesitation at all. b19 must show him already moving.
  v8   "I am not worthy that thou shouldest come under my roof: but SPEAK THE
       WORD ONLY."
  v9   "For I am a man UNDER AUTHORITY ... I say to this man, Go, and he goeth."
       He argues from chain of command — the one thing a soldier understands.
  v10  "he MARVELLED" — one of the very few times the Gospels say anything
       surprised Jesus. b28 is that face and it must read as genuine astonishment.
  v11  "many shall come from the EAST AND WEST, and shall sit down with Abraham,
       and Isaac, and Jacob" — a table, and outsiders at it.
  v13  "as thou hast believed, so be it done unto thee. And his servant was
       healed in the SELFSAME HOUR."

THE DISTANCE IS THE WHOLE POINT OF THIS STORY, so the build is deliberately
built on a SPLIT LOCATION: the street where the two men talk, and the Roman
house across town where the servant lies. Jesus never goes there. b36-b38 happen
in that house with nobody present but the servant — no Jesus, no centurion, no
crowd. If Jesus appears in the healing frames the story is broken.

THE CENTURION MUST BE SYMPATHETIC. The model's default for a Roman officer is a
sneering occupier, and that reading destroys the story — this is a man who loves
a slave enough to beg an enemy teacher in public. Every frame of him specifies a
weathered, decent, worried face, and his humility is physical: helmet off and
carried under his arm from b13 onward, head bowed, never looming.

CONTENT-CARE: row 15 is GREEN. The servant's illness is shown as stillness,
grey exhaustion and pain on a face — no convulsions, no medical detail.

TIME OF DAY: one bright day throughout. No night, no sunset.
"""

LOCKS = {
    "CENTURION": (
        "CENTURION LOCK: the Roman officer is the same man in every shot — about "
        "forty-five, powerfully built and weathered by twenty years of campaigning, "
        "close-cropped iron-grey hair, a clean-shaven square face lined at the eyes, "
        "a pale old scar along one forearm, and steady tired grey eyes. He wears "
        "Roman officer's kit: a segmented iron cuirass over a short DEEP-RED wool "
        "tunic, a red cloak pinned at the shoulder, a wide studded leather belt, "
        "hobnailed boots, and a transverse-crested iron helmet. His face is decent, "
        "worried and entirely without arrogance, and is shown clearly."
    ),
    "SERVANT": (
        "SERVANT LOCK: the sick young man is the same person in every shot — about "
        "eighteen, slight and thin, warm olive-brown skin gone grey and waxy with "
        "illness, dark curling hair damp at the forehead, a smooth young face with "
        "dark shadows under the eyes. He wears a simple undyed sand-brown wool "
        "servant's tunic (never cream, never white). His face is shown clearly. No "
        "wounds, sores or medical detail are ever visible."
    ),
    "CAPERNAUM": (
        "CAPERNAUM LOCK: the fishing town on the Sea of Galilee — narrow lanes and "
        "low flat-roofed houses of rough dark basalt stone, fishing nets on frames, "
        "boats drawn up on the shingle, the flat blue lake and the far hills beyond. "
        "The townspeople are ordinary Galilean working folk in SATURATED DEEP earth "
        "colours: dark chocolate brown, deep russet, burnt ochre, dark olive and "
        "dusty indigo wool. No townsperson wears off-white, ivory or any near-white "
        "cloth."
    ),
    "ROMAN-HOUSE": (
        "ROMAN HOUSE LOCK: the officer's quarters in the town — a plastered room with "
        "a red-tiled floor, a shuttered window throwing bars of hard daylight, a low "
        "wooden bed with a straw mattress and a folded blanket, a plain military "
        "chest, a lamp stand, a sword and belt hung on a peg. Spare, ordered and "
        "soldierly, with no luxury in it."
    ),
    "SOLDIERS": (
        "SOLDIERS LOCK: the Roman soldiers of the garrison are the same troops "
        "throughout — hard-faced men in iron helmets and segmented armour over short "
        "red tunics, with spears, oval shields and hobnailed boots, standing in "
        "disciplined pairs. They are watchful and impassive, never leering or cruel."
    ),
    "CROWD": (
        "CROWD LOCK: the Galilean crowd following Jesus — ordinary working people of "
        "every age, fishermen, women with children, old men, in SATURATED DEEP earth "
        "colours: dark chocolate brown, deep russet, burnt ochre, dark olive, dusty "
        "indigo and faded plum wool. No one in the crowd wears off-white, ivory or "
        "any near-white cloth. Their faces are shown clearly."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------------- n1/n2 — occupied town ----
    {
        "id": "v2-r015-b01", "out": "s01-capernaum-occupied.jpeg", "seg": "n1",
        "window": "0.28-12.77", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAPERNAUM", "SOLDIERS"],
        "narration": ("This is Capernaum, a fishing town on the Sea of Galilee, where "
                      "Jesus often stayed and taught. It was also filled with Roman "
                      "soldiers — the army that had conquered these people and now "
                      "ruled them by force."),
        "must_show": "the fishing town with Roman soldiers standing in it — armed pairs on the lanes, local people working around them.",
        "must_not_show": "no violence and no abuse; the occupation reads as armed presence and everyone's careful distance.",
        "scene": (
            "A wide view of the basalt fishing town along the lake shore in bright "
            "morning — nets on frames, boats on the shingle, people carrying baskets "
            "up the lanes. Standing among all of it are pairs of Roman soldiers in "
            "iron helmets and armour with spears grounded, watching the street. The "
            "townspeople move around them without looking at them. Nothing violent is "
            "happening; the armour is simply everywhere. The camera is back far enough "
            "to hold the lane and the lake. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r015-b02", "out": "s02-every-reason-to-hate-rome.jpeg", "seg": "n2 p1",
        "window": "13.81-16.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAPERNAUM", "SOLDIERS"],
        "narration": "So the Jews here had every reason to hate Rome.",
        "must_show": "a Galilean man's face as he passes armoured soldiers — eyes down, jaw tight, resentment held in.",
        "must_not_show": "no confrontation; the hatred is swallowed, not spoken.",
        "scene": (
            "Close on a middle-aged Galilean fisherman carrying a folded net past two "
            "Roman soldiers in the lane. His eyes are cast down and away from them, "
            "his jaw is set hard and a muscle is working in it, and his shoulders are "
            "turned very slightly to give them room. The blurred iron and red of the "
            "soldiers fills the frame behind him. Nothing is said. Hard morning light. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b03", "out": "s03-this-man-wears-the-uniform.jpeg", "seg": "n2 p2",
        "window": "16.27-20.73", "wide": True, "jesus": False, "ref": False,
        "locks": ["CENTURION", "CAPERNAUM"],
        "narration": ("Hold on to that, because the man this story is about wears a "
                      "Roman uniform."),
        "must_show": "the centurion introduced in full kit — crested helmet on, cuirass, red cloak — unmistakably the occupier, standing in the town.",
        "must_not_show": "he is NOT sneering, swaggering or cruel; a serious professional soldier, nothing more.",
        "scene": (
            "The centurion stands in the basalt lane in full kit — segmented iron "
            "cuirass over the deep-red tunic, red cloak pinned at the shoulder, the "
            "transverse-crested helmet on his head, hobnailed boots — unmistakably a "
            "Roman officer. He is looking off down the street with a serious, "
            "preoccupied expression, not at anyone. There is nothing swaggering or "
            "cruel about him. Townspeople give him a wide berth in the background. "
            "Hard morning light on the iron. The camera is back far enough to see him "
            "head to boots. He has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------- n3/n4 — the servant ----
    {
        "id": "v2-r015-b04", "out": "s04-a-servant-was-dying.jpeg", "seg": "n3",
        "window": "21.80-29.28", "wide": True, "jesus": False, "ref": False,
        "locks": ["SERVANT", "ROMAN-HOUSE"],
        "narration": ("In one of those Roman houses, a young servant was dying. His body "
                      "had gone stiff and useless, and he was in terrible pain."),
        "must_show": "the young man on the low bed in the spare Roman room — grey, still, his body rigid, pain plain on his face.",
        "must_not_show": "CONTENT-CARE — no convulsions, no medical detail, nothing grotesque; stillness and a grey face carry it.",
        "scene": (
            "In the spare plastered room, the young servant lies on the low wooden bed "
            "under bars of hard daylight from the shuttered window. His body is rigid "
            "and unnaturally still, one arm locked awkwardly across his chest, his "
            "hands drawn in. His face is grey and waxy and sheened with sweat, his "
            "eyes closed and his brows drawn tight with pain. A cup of water sits "
            "untouched beside the bed. There is nobody else in the room. The camera is "
            "back far enough to see him and the room. He has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r015-b05", "out": "s05-treated-as-property.jpeg", "seg": "n4 p1-p2",
        "window": "30.39-36.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["SERVANT"],
        "narration": ("A servant in those days was treated as property. If he died, "
                      "most masters would simply replace him."),
        "must_show": "close on the young servant's face — a boy, and plainly nobody important to the world.",
        "must_not_show": "no pity-mongering; the frame is plain and the narration does the work.",
        "scene": (
            "Close on the young servant's face on the folded blanket. He is very young "
            "— smooth-cheeked, dark curls damp on his forehead, deep shadows under "
            "closed eyes, his mouth slightly open as he breathes shallowly. His plain "
            "undyed servant's tunic is worn thin at the collar. Bars of hard daylight "
            "fall across him. He has one head."
        ),
    },
    {
        "id": "v2-r015-b06", "out": "s06-he-could-not-walk-away.jpeg", "seg": "n4 p3",
        "window": "36.31-39.77", "wide": True, "jesus": False, "ref": False,
        "locks": ["CENTURION", "SERVANT", "ROMAN-HOUSE"],
        "narration": "But this master could not bring himself to walk away.",
        "must_show": "⚠️ THE FRAME THE WHOLE STORY RESTS ON: the officer sitting at the slave's bedside, helmet set aside, watching him — an armoured man keeping vigil over property.",
        "must_not_show": "no sentimentality and no weeping; it is a hard man sitting still in a chair for hours.",
        "scene": (
            "The centurion sits on a low stool pulled up beside the servant's bed, "
            "still in his cuirass and red cloak, his crested helmet set down on the "
            "tiled floor at his feet. He is leaning forward with his forearms on his "
            "knees, hands loosely clasped, simply watching the boy's face. His "
            "expression is worn out and worried and completely unguarded. He has "
            "plainly been sitting there a long time. Bars of daylight cross the room. "
            "The camera is back far enough to hold both men. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    # ------------------------------------------------- n5/n6 — he goes ----
    {
        "id": "v2-r015-b07", "out": "s07-a-hundred-soldiers.jpeg", "seg": "n5",
        "window": "40.84-49.06", "wide": True, "jesus": False, "ref": False,
        "locks": ["CENTURION", "SOLDIERS"],
        "narration": ("The master was a centurion — a Roman officer in command of a "
                      "hundred soldiers. A powerful man, and to the Jews, the enemy."),
        "must_show": "his rank made visible — the centurion at the head of a formed body of troops, men waiting on his word.",
        "must_not_show": "no brutality; discipline and authority, nothing else.",
        "scene": (
            "The centurion stands at the head of a formed block of Roman soldiers on "
            "the packed ground outside the garrison — ranks of iron helmets, oval "
            "shields and grounded spears drawn up behind him, every man still and "
            "facing forward, waiting. He is half turned, giving an order over his "
            "shoulder. The scale of what obeys him is plain. Hard morning light on "
            "iron and red wool. The camera is back far enough to hold him and the "
            "formation. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b08", "out": "s08-he-went-straight-to-jesus.jpeg", "seg": "n6 p1",
        "window": "50.12-54.59", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CENTURION", "CROWD", "CAPERNAUM"],
        "narration": ("Yet he left his house and went straight to Jesus, a Jewish "
                      "teacher, to beg for help."),
        "must_show": "the officer walking alone into a Galilean crowd toward Jesus — armour among unarmoured people, every head turning.",
        "must_not_show": "no halo, glare or rim-light; he brings NO soldiers with him, which the frame must make obvious.",
        "scene": (
            "The centurion walks alone up the basalt lane into a crowd of Galileans "
            "gathered around Jesus — one man in iron and red among a press of people "
            "in brown and ochre wool, and not a single soldier with him. Heads are "
            "turning all through the crowd as he comes, faces going wary and hard, and "
            "people are drawing back to let him through. Ahead of him Jesus has turned "
            "to face him. Hard morning light. The camera is back far enough to hold "
            "the lane. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b09", "out": "s09-not-even-his-own-son.jpeg", "seg": "n6 p2-p4",
        "window": "54.59-59.22", "wide": False, "jesus": False, "ref": False,
        "locks": ["CENTURION", "CROWD"],
        "narration": "Not for himself. Not even for his own son. For a servant.",
        "must_show": "close on the centurion's face in the hostile crowd — set, humbled, going through with it anyway.",
        "must_not_show": "no arrogance and no fear; grim determination on behalf of somebody else.",
        "scene": (
            "Close on the centurion's weathered face as he moves through the crowd. "
            "His jaw is set, his grey eyes are fixed ahead on one point, and there is "
            "no arrogance in his expression at all — only a hard, tired resolve, the "
            "face of a man who has decided to do something humiliating and is doing "
            "it. The blurred wary faces of Galileans press close on both sides. Hard "
            "light on the iron at his shoulder. He has one head."
        ),
    },
    # ---------------------------------------------------- n7 — the plea ----
    {
        "id": "v2-r015-b10", "out": "s10-he-came-humbly.jpeg", "seg": "n7 p1",
        "window": "60.28-67.85", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CENTURION", "CROWD"],
        "narration": ("He came humbly, head bowed, and told Jesus the plain truth: his "
                      "servant was at home, unable to move, in agony."),
        "must_show": "⚠️ THE HELMET COMES OFF: the centurion standing before Jesus with his crested helmet OFF and held under his arm, head bowed, speaking.",
        "must_not_show": "no halo, glare or rim-light; he must NOT loom over Jesus — his posture is lowered from here to the end of the scene.",
        "scene": (
            "The centurion stands in front of Jesus in the lane with his crested "
            "helmet OFF and clamped under one arm, his close-cropped grey head bare "
            "and bowed, his shoulders come down. He is speaking, one hand open in "
            "front of him, his eyes lowered rather than meeting Jesus's. Jesus stands "
            "listening with his head slightly inclined. All around them the crowd has "
            "gone silent and is staring. Hard morning light. The camera is back far "
            "enough to see both men head to feet. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r015-b11", "out": "s11-could-you-help-him.jpeg", "seg": "n7 p2",
        "window": "67.85-69.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["CENTURION"],
        "narration": "Could Jesus help him?",
        "must_show": "close on the officer's face asking — a commander of a hundred men asking for something he cannot order.",
        "must_not_show": "do not put Jesus in this frame.",
        "scene": (
            "Close on the centurion's bare grey head and weathered face as he asks. "
            "His eyes have come up now and are fixed and open and asking, his mouth "
            "shut after the question, his throat working once. The helmet is a dark "
            "shape under his arm at the frame's edge. It is the face of a man who "
            "gives orders for a living and has nothing to order here. Hard light on "
            "his scarred jaw. He has one head."
        ),
    },
    # ----------------------------------------------- n8 / j1 — I will come ----
    {
        "id": "v2-r015-b12", "out": "s12-not-a-moments-hesitation.jpeg", "seg": "n8",
        "window": "70.74-75.34", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CENTURION", "CROWD"],
        "narration": ("Jesus did not hesitate for a moment. He answered that he would go "
                      "to the house himself."),
        "must_show": "Jesus already turning and stepping toward the Roman quarter — the answer given with his feet, and the crowd reacting to it.",
        "must_not_show": "no halo, glare or rim-light; no pause or deliberation in his posture — the speed is the beat.",
        "scene": (
            "Jesus has already turned his body and taken a step in the direction of "
            "the Roman quarter, one hand lifted toward the centurion in a plain "
            "'come on then' gesture, his face open and matter of fact. There is no "
            "hesitation anywhere in the movement. Behind him the crowd has broken into "
            "startled reaction — heads turning to each other, one man's arm half "
            "raised in protest, mouths open. The centurion stands holding his helmet. "
            "Hard morning light. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b13", "out": "s13-i-will-come-and-heal-him.jpeg", "seg": "j1",
        "window": "76.42-77.72", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "I will come and heal him. (Matthew 8:7)",
        "must_show": "close on Jesus saying it — simple, warm, entirely without calculation.",
        "must_not_show": "no halo, glare or rim-light; nothing weighty about it — it is said as easily as agreeing to help a neighbour.",
        "scene": (
            "Close on Jesus's face in the bright lane, speaking. His expression is warm "
            "and completely straightforward — level eyes, an easy mouth, a small nod "
            "already starting — a man agreeing to something without weighing it at "
            "all. His hand is open and lifted at his side. The blurred crowd and dark "
            "basalt wall are soft behind him."
        ),
    },
    {
        "id": "v2-r015-b14", "out": "s14-into-the-enemys-house.jpeg", "seg": "n9 p1-p2",
        "window": "78.78-88.34", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CENTURION", "CROWD", "CAPERNAUM"],
        "narration": ("Stop and see what that means. Jesus was willing to walk into the "
                      "home of a Roman — the enemy — for the sake of one dying servant "
                      "nobody else valued."),
        "must_show": "the crowd's shock at where he is willing to go — faces disturbed, a couple looking at each other, one shaking his head.",
        "must_not_show": "no halo, glare or rim-light; nobody physically stops him.",
        "scene": (
            "Jesus is walking toward the Roman quarter with the centurion beside him, "
            "and the Galilean crowd is coming apart behind them — two men have turned "
            "to each other with their hands out in disbelief, an older man is shaking "
            "his head hard, a woman has stopped dead with her hand to her mouth. "
            "Nobody moves to block him. Ahead the plastered Roman buildings and a "
            "standing soldier are visible at the end of the lane. Hard light. The "
            "camera is back far enough to hold the walkers and the reacting crowd. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b15", "out": "s15-that-is-who-jesus-is.jpeg", "seg": "n9 p3",
        "window": "88.34-90.34", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "That is who Jesus is.",
        "must_show": "close on Jesus walking — untroubled, unhurried, going where he said he would go.",
        "must_not_show": "no halo, glare or rim-light; no defiance or drama in the face.",
        "scene": (
            "Close on Jesus in profile as he walks, his face calm and untroubled and "
            "faintly warm, his eyes on the road ahead. There is no defiance in it and "
            "no drama — he is simply going where he said he would go, and it costs him "
            "nothing. Hard morning light along his cheek and the blurred lane behind."
        ),
    },
    # ------------------------------------------- n10/n11 — speak the word ----
    {
        "id": "v2-r015-b16", "out": "s16-but-the-officer-stopped-him.jpeg", "seg": "n10 p1",
        "window": "91.39-92.77", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CENTURION"],
        "narration": "But the officer stopped him.",
        "must_show": "the centurion's hand coming up to halt Jesus — stopping the very thing he came to ask for.",
        "must_not_show": "no halo, glare or rim-light; the gesture is respectful, not commanding.",
        "scene": (
            "The centurion has stepped in front of Jesus and put one open hand up "
            "between them, palm out, checking him — a stopping gesture made "
            "respectfully, low and open rather than raised in command. Jesus has "
            "halted mid-stride and is looking at him. The helmet is still under the "
            "officer's other arm. Hard light in the lane. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b17", "out": "s17-i-am-not-worthy.jpeg", "seg": "n10 p2",
        "window": "92.77-97.00", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CENTURION", "CROWD"],
        "narration": ("Lord, he said, I am not worthy to have you come into my home."),
        "must_show": "⚠️ THE INVERSION: the Roman officer lowering himself before a Galilean carpenter — head down, shoulders bowed, in front of a whole street.",
        "must_not_show": "no halo, glare or rim-light; the crowd's reaction is astonishment, not triumph.",
        "scene": (
            "The centurion has bowed his head right down in front of Jesus in the "
            "middle of the lane, his bare grey head lowered, his shoulders come "
            "forward, the helmet held against his chest with both hands now — an "
            "officer of the occupying army making himself small in front of a Galilean "
            "teacher, in public. Jesus stands quietly in front of him. All around, the "
            "watching crowd has gone completely still with astonishment. Hard morning "
            "light. The camera is back far enough to hold both men and the near crowd. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b18", "out": "s18-only-speak-the-word.jpeg", "seg": "n10 p3",
        "window": "97.00-100.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["CENTURION"],
        "narration": ("Only speak the word, and my servant will be healed."),
        "must_show": "close on the officer's face saying it — absolute certainty, no doubt anywhere in it.",
        "must_not_show": "do not put Jesus in this frame; no pleading — this is a statement of fact.",
        "scene": (
            "Close on the centurion's face, head still lowered but his grey eyes come "
            "up under his brows and fixed steadily on the man in front of him. His "
            "expression is not pleading at all — it is flat, certain conviction, the "
            "look of a professional stating something he knows to be true. His mouth "
            "shapes the words plainly. Hard light on his scarred cheek. He has one head."
        ),
    },
    {
        "id": "v2-r015-b19", "out": "s19-his-word-was-enough.jpeg", "seg": "n11",
        "window": "101.39-110.17", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CENTURION", "CROWD"],
        "narration": ("He was not just being polite. He truly believed Jesus did not "
                      "need to be there at all. He believed that Jesus's word, by "
                      "itself, was enough."),
        "must_show": "the two of them facing each other in the lane, the officer's whole bearing saying he means it, Jesus beginning to register something.",
        "must_not_show": "no halo, glare or rim-light; Jesus's astonishment has not fully arrived yet — it is only starting.",
        "scene": (
            "The centurion and Jesus stand facing each other in the sunlit lane, the "
            "officer bare-headed with his helmet against his chest and his whole "
            "bearing plain and certain, and Jesus looking at him with an expression "
            "that has just begun to change — his head coming up a fraction, his brows "
            "starting to lift. The silent crowd rings them at a distance. Hard morning "
            "light on iron and stone. The camera is back far enough to see both head to "
            "feet. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------- n12/n13 — authority ----
    {
        "id": "v2-r015-b20", "out": "s20-a-man-under-authority.jpeg", "seg": "n12 p1-p2",
        "window": "111.22-116.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["CENTURION"],
        "narration": ("And he explained why, in the only language a soldier knows. I am "
                      "a man under authority, he said."),
        "must_show": "the officer explaining with a soldier's plainness — one hand flat, laying out a chain of command.",
        "must_not_show": "do not put Jesus in this frame; nothing eloquent — he is explaining the way he would brief a junior officer.",
        "scene": (
            "Close on the centurion mid-explanation, one broad scarred hand held flat "
            "and level in front of him as if laying something out on a table. His face "
            "is plain and practical and slightly earnest — a soldier explaining how "
            "his own world works, using the only argument he has. Hard light on his "
            "cuirass and bare grey head. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r015-b21", "out": "s21-i-say-go-and-he-goeth.jpeg", "seg": "n12 p3-p4",
        "window": "116.77-123.48", "wide": True, "jesus": False, "ref": False,
        "locks": ["SOLDIERS", "CAPERNAUM"],
        "narration": ("I tell one soldier, Go, and he goes. I tell another, Come, and he "
                      "comes."),
        "must_show": "the thing he is describing, shown: a soldier turning away on an order and another stepping forward at the same moment — obedience at a distance.",
        "must_not_show": "the centurion need not be in this frame; do not put Jesus in it.",
        "scene": (
            "In the packed ground outside the garrison, two Roman soldiers are caught "
            "in the middle of opposite movements — one has turned on his heel and is "
            "striding away toward the gate with his spear shouldered, the other is "
            "stepping forward toward the camera to attention, chin up. Neither is "
            "looking at anyone. Behind them the ranks stand unmoving. Hard daylight on "
            "iron. The camera is back far enough to see both men head to boots. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b22", "out": "s22-his-word-crosses-the-camp.jpeg", "seg": "n13 p1",
        "window": "124.59-129.10", "wide": True, "jesus": False, "ref": False,
        "locks": ["SOLDIERS"],
        "narration": ("He never has to go himself; his word alone carries his power "
                      "across the whole camp."),
        "must_show": "the whole camp working — men moving, posts changing, orders being carried out — with no officer anywhere in the frame.",
        "must_not_show": "the centurion must NOT appear; his absence is the entire idea. Do not put Jesus in it.",
        "scene": (
            "A wide view across the Roman camp with everything in motion — a sentry "
            "pair marching to relieve another at the gate, men falling into a line, a "
            "soldier running a message between buildings, shields being shifted on a "
            "rack. Every man is doing something he was told to do. There is no officer "
            "anywhere in the frame at all. Hard bright daylight on iron and packed "
            "earth. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b23", "out": "s23-it-could-reach-across-the-town.jpeg", "seg": "n13 p2",
        "window": "129.10-135.27", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CENTURION", "CAPERNAUM"],
        "narration": ("He was certain Jesus's word worked the same way — that it could "
                      "reach across the town and heal on its own."),
        "must_show": "the officer's hand pointing away across the rooftops toward his own house — naming the distance the word has to cross.",
        "must_not_show": "no halo, glare or rim-light; the distance he points across must be visible in the frame.",
        "scene": (
            "The centurion has turned and is pointing away over the flat basalt "
            "rooftops of the town toward the plastered Roman quarter in the distance, "
            "his arm fully extended, looking back at Jesus as he points. Between his "
            "hand and the far buildings lies the whole width of the town — lanes, "
            "roofs, the lake beyond. Jesus follows the line of his arm. Hard midday "
            "light. The camera is back far enough to hold both men and the distance "
            "they are looking across. Every figure has two arms, two hands and one head."
        ),
    },
    # -------------------------------------------------- n14 / j2 — he marvelled ----
    {
        "id": "v2-r015-b24", "out": "s24-and-this-amazed-jesus.jpeg", "seg": "n14 p1-p2",
        "window": "136.39-144.09", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("And this amazed Jesus. The Gospels almost never say that anyone "
                      "surprised him, yet the faith of this Roman outsider stopped him."),
        "must_show": "⚠️ GENUINE ASTONISHMENT — close on Jesus's face actually surprised: brows up, a startled breath of a laugh starting, delighted.",
        "must_not_show": "NOT serene, NOT knowing, NOT a gentle smile. v10 says he MARVELLED, and a composed face throws away one of the rarest moments in the Gospels. No halo or rim-light.",
        "scene": (
            "Very close on Jesus's face, genuinely astonished. His eyebrows have shot "
            "up, his eyes have widened and gone bright, his head has come back a "
            "little, and a startled breath of a laugh is breaking across his mouth — "
            "the completely unguarded face of someone who has just been surprised and "
            "is delighted by it. There is nothing composed or knowing in it. Hard "
            "midday light, the blurred lane behind."
        ),
    },
    {
        "id": "v2-r015-b25", "out": "s25-he-turned-to-the-crowd.jpeg", "seg": "n14 p3",
        "window": "144.53-146.15", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CROWD", "CENTURION"],
        "narration": "He turned to the crowd and said:",
        "must_show": "Jesus turning away from the officer to address the watching Galileans, arm sweeping toward them.",
        "must_not_show": "no halo, glare or rim-light; the centurion stays where he is, bare-headed.",
        "scene": (
            "Jesus has turned away from the centurion to face the crowd of Galileans "
            "in the lane, one arm sweeping out toward them, his face still lit with "
            "that surprise. The people nearest have straightened up and gone quiet, "
            "heads coming round. The centurion stands behind him bare-headed with his "
            "helmet at his chest. Hard midday light. The camera is back far enough to "
            "hold Jesus, the crowd and the officer. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r015-b26", "out": "s26-not-in-israel.jpeg", "seg": "j2",
        "window": "147.27-151.49", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CROWD", "CENTURION"],
        "narration": ("Verily I say unto you, I have not found so great faith, no, not "
                      "in Israel. (Matthew 8:10)"),
        "must_show": "the sentence landing on the Galilean crowd — faces turning to look at the Roman standing behind him, expressions reordering.",
        "must_not_show": "no halo, glare or rim-light; nobody is being humiliated — they are being rearranged.",
        "scene": (
            "Jesus speaks to the crowd with one hand gesturing back toward the "
            "centurion behind him, and the sentence is landing — faces all through the "
            "crowd are swinging round to look at the Roman officer, mouths opening, "
            "two men turning to each other, an old man's brows drawn together as he "
            "works at it. Nobody looks shamed; they look reordered. The centurion "
            "stands bare-headed under all those eyes. Hard midday light. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b27", "out": "s27-no-one-among-his-own-people.jpeg", "seg": "n15",
        "window": "152.51-161.34", "wide": True, "jesus": False, "ref": False,
        "locks": ["CROWD", "CENTURION"],
        "narration": ("In plain words: no one among his own people, the ones who should "
                      "have known God best, had ever trusted him the way this outsider "
                      "just had."),
        "must_show": "the two groups in one frame — a crowd of Galileans looking at one Roman, and the space between them.",
        "must_not_show": "do not put Jesus in this frame; nobody is hostile now, which is the change.",
        "scene": (
            "A frame holding both: on one side the crowd of Galileans, dozens of them "
            "in brown and ochre wool, all facing the same way; on the other, alone, "
            "the centurion in iron and red with his bare grey head and his helmet held "
            "against his chest. The ground between them is open. Not one face in the "
            "crowd is hostile any more — they are studying him. Hard midday light. The "
            "camera is back far enough to hold both. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    # ------------------------------------------------ n16 / j2b — east and west ----
    {
        "id": "v2-r015-b28", "out": "s28-wider-than-expected.jpeg", "seg": "n16",
        "window": "162.42-165.67", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Then Jesus opened heaven wider than anyone listening expected:"),
        "must_show": "close on Jesus about to say something large — both hands beginning to open outward.",
        "must_not_show": "no halo, glare or rim-light; nothing in the sky.",
        "scene": (
            "Close on Jesus in the bright lane, both hands beginning to come open and "
            "outward in front of him, his face lifting and his eyes going wide and "
            "warm — a man opening up to say something much bigger than the question he "
            "was asked. There is nothing at all in the sky above him. Hard midday "
            "light. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r015-b29", "out": "s29-from-east-and-west.jpeg", "seg": "j2b a",
        "window": "166.72-170.7", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CROWD", "CAPERNAUM"],
        "narration": ("And I say unto you, That many shall come from the east and west, "
                      "(Matthew 8:11)"),
        "must_show": "his arms flung wide to both horizons as he says it, the crowd following the sweep of them.",
        "must_not_show": "no halo, glare or rim-light; do not paint heaven, angels or light in the sky.",
        "scene": (
            "Jesus stands with both arms flung wide to either side, pointing away to "
            "opposite horizons — one hand toward the hills inland, the other out over "
            "the lake — his head back and his face open. The crowd around him has "
            "turned to follow the sweep of his arms, some looking one way and some the "
            "other. The sky above is an ordinary bright midday sky with nothing in it. "
            "The camera is back far enough to see him head to sandals with both "
            "horizons in frame. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b30", "out": "s30-sit-down-with-abraham.jpeg", "seg": "j2b b",
        "window": "170.7-174.76", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": ("and shall sit down with Abraham, and Isaac, and Jacob, in the "
                      "kingdom of heaven. (Matthew 8:11)"),
        "must_show": "the IMAGE HE USED — a long welcoming table set under the open sky with places laid and empty, seats waiting.",
        "must_not_show": "do NOT paint heaven, clouds, angels, light or the patriarchs themselves — an ordinary table with empty places says it. Do not put Jesus in this frame.",
        "scene": (
            "A long low table stands set out in the open under a wide bright sky, "
            "spread with a plain cloth, bread, olives, figs and clay cups, with "
            "cushions and benches all along both sides — and every single place at it "
            "is EMPTY and waiting, more places than could be counted, the table "
            "running away out of the frame. Warm daylight across the cloth. There are "
            "no people in the frame and nothing whatever in the sky."
        ),
    },
    {
        "id": "v2-r015-b31", "out": "s31-every-nation-welcomed.jpeg", "seg": "n17 p1",
        "window": "175.78-179.50", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": ("He meant that people from every nation on earth would be welcomed "
                      "to God's table."),
        "must_show": "the same table now filling with people of visibly different nations and skin tones, eating together.",
        "must_not_show": "nothing heavenly, no light, no angels; ordinary people at an ordinary meal. Do not put Jesus in this frame.",
        "scene": (
            "The same long table under the open sky, now filling up — people of many "
            "nations sitting shoulder to shoulder along both sides, plainly from "
            "different parts of the world in different dress and with different skin "
            "tones, passing bread to each other, talking, a child on a woman's knee, "
            "an old man laughing. Nothing about the scene is heavenly; it is a very "
            "good meal. Warm daylight. The camera is back far enough to hold the "
            "length of the table. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b32", "out": "s32-it-is-whether-you-trust-him.jpeg", "seg": "n17 p2-p3",
        "window": "179.50-186.37", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CENTURION", "CROWD"],
        "narration": ("What brings you in is not where you were born, or which group you "
                      "belong to. It is whether you trust him."),
        "must_show": "back in the lane: Jesus, the Roman and the Galileans in one frame with nobody separated from anybody.",
        "must_not_show": "no halo, glare or rim-light; the crowd and the officer must no longer be in two separate blocks.",
        "scene": (
            "Back in the sunlit basalt lane. Jesus stands with the centurion beside "
            "him now rather than in front of him, and the Galilean crowd has closed in "
            "around both of them so that there is no gap and no two sides any more — "
            "brown wool and iron armour standing shoulder to shoulder, everyone facing "
            "the same way. Hard midday light. The camera is back far enough to hold "
            "the whole group. Every figure has two arms, two hands and one head."
        ),
    },
    # ---------------------------------------------- n18 / j3 — go thy way ----
    {
        "id": "v2-r015-b33", "out": "s33-he-turned-back-to-the-soldier.jpeg", "seg": "n18",
        "window": "187.45-192.83", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CENTURION"],
        "narration": ("Then Jesus turned back to the soldier and gave him the one thing "
                      "he had asked for — a single word."),
        "must_show": "the two of them face to face and close, Jesus turning his full attention back onto the officer.",
        "must_not_show": "no halo, glare or rim-light; no touch — the whole point is that nothing physical happens.",
        "scene": (
            "Jesus has turned back and the two men stand face to face and close in the "
            "lane, the centurion bare-headed with the helmet held at his chest, Jesus "
            "looking directly at him with his whole attention. Neither is touching the "
            "other and there is a clear space between them. The crowd is soft and "
            "quiet behind. Hard midday light. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r015-b34", "out": "s34-as-thou-hast-believed.jpeg", "seg": "j3",
        "window": "193.95-197.57", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Go thy way; and as thou hast believed, so be it done unto thee. "
                      "(Matthew 8:13)"),
        "must_show": "close on Jesus saying it — warm, certain, and completely undramatic; the word is doing all the work.",
        "must_not_show": "no halo, glare or rim-light; NO raised hand toward the distance, no gesture of power, nothing in the air. He simply says it.",
        "scene": (
            "Close on Jesus's face in the bright lane, speaking quietly to the man in "
            "front of him. His expression is warm and completely certain and entirely "
            "undramatic — steady eyes, an easy mouth, the faintest smile. His hands "
            "are down at his sides and he is making no gesture of any kind. Nothing is "
            "happening in the air around him. Hard midday light on his face."
        ),
    },
    {
        "id": "v2-r015-b35", "out": "s35-no-touch-no-visit.jpeg", "seg": "n19",
        "window": "198.58-206.24", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CENTURION", "CAPERNAUM"],
        "narration": ("Go home; it has already happened, just as you trusted it would. "
                      "No touch, no visit — only his word, sent across the town."),
        "must_show": "the two men standing apart with clear air between them and the rooftops of the far Roman quarter visible beyond — nothing has crossed the space but a sentence.",
        "must_not_show": "no halo, glare or rim-light, and NOTHING travelling through the air — no light, no shimmer, no line. The emptiness between them is the picture.",
        "scene": (
            "A wide view of the lane with Jesus and the centurion standing a clear "
            "pace apart, neither touching the other, and beyond them over the basalt "
            "rooftops the plastered buildings of the Roman quarter are visible far "
            "across the town. The air between the two men and the air over the roofs "
            "is completely ordinary and completely empty — nothing is moving through "
            "it. Hard midday light. The camera is back far enough to hold both men and "
            "the distant quarter. Every figure has two arms, two hands and one head."
        ),
    },
    # -------------------------------------------------- n20/n21 — the house ----
    {
        "id": "v2-r015-b36", "out": "s36-a-deep-clean-breath.jpeg", "seg": "n20 p1",
        "window": "207.34-213.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["SERVANT", "ROMAN-HOUSE"],
        "narration": ("And in that very hour, far away in the Roman house, the young "
                      "servant drew a deep, clean breath."),
        "must_show": "⚠️ NO JESUS IN THIS FRAME. Close on the boy alone on the bed as his chest rises in a full deep breath for the first time.",
        "must_not_show": "no Jesus, no centurion, nobody else in the room; no light, glow or shimmer — an ordinary room and one breath.",
        "scene": (
            "Close on the young servant lying alone on the low bed in the quiet room. "
            "His chest has risen in a deep full breath, his shoulders easing back into "
            "the mattress, and his mouth has come open as the air goes all the way in "
            "— the first unrestricted breath in a long time. His eyes are still closed. "
            "Bars of hard ordinary daylight lie across the blanket from the shuttered "
            "window. Nothing else is happening in the room. He has one head."
        ),
    },
    {
        "id": "v2-r015-b37", "out": "s37-he-sat-up-completely-well.jpeg", "seg": "n20 p2",
        "window": "213.18-219.13", "wide": True, "jesus": False, "ref": False,
        "locks": ["SERVANT", "ROMAN-HOUSE"],
        "narration": ("The color flowed back into his face, his body loosened, and he "
                      "sat up, completely well."),
        "must_show": "him sitting up on the edge of the bed on his own — rigid limbs loosened, colour back in his face, looking at his own hands.",
        "must_not_show": "still nobody else in the room; nothing supernatural anywhere in the frame.",
        "scene": (
            "The young servant has pushed himself upright and is sitting on the edge "
            "of the low bed with his bare feet on the red tiles, one hand still "
            "braced on the mattress. The rigid drawn-in look has gone out of his limbs "
            "entirely, warm colour has come back into his face, and he is staring down "
            "at his own opening and closing hands with his mouth open. The room around "
            "him is empty and ordinary. Bars of daylight from the shutter. The camera "
            "is back far enough to see him and the whole room. He has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r015-b38", "out": "s38-no-one-was-in-the-room.jpeg", "seg": "n21",
        "window": "220.24-226.18", "wide": True, "jesus": False, "ref": False,
        "locks": ["SERVANT", "ROMAN-HOUSE"],
        "narration": ("No one was in the room with him. He was made whole by nothing but "
                      "the word of a man he had never even met."),
        "must_show": "⚠️ THE EMPTY ROOM — a wide frame proving he is completely alone: the door shut, the stool empty, nobody there.",
        "must_not_show": "absolutely nobody but the servant; no Jesus, no centurion, no shadow, no figure in the doorway. The aloneness is the entire beat.",
        "scene": (
            "A wide view of the whole plastered room. The young servant sits alone on "
            "the edge of the bed looking around him, and the room is completely empty "
            "of anyone else — the low stool beside the bed is vacant, the wooden door "
            "is shut, the corners are plain and bare, the sword hangs untouched on its "
            "peg. There is no other person and no shadow of one anywhere in the frame. "
            "Hard ordinary daylight comes through the shutter in bars. He has two "
            "arms, two hands and one head."
        ),
    },
    # ------------------------------------------------------ n22 — the reunion ----
    {
        "id": "v2-r015-b39", "out": "s39-he-rose-to-meet-him.jpeg", "seg": "n22 p1",
        "window": "227.23-232.64", "wide": True, "jesus": False, "ref": False,
        "locks": ["CENTURION", "SERVANT", "ROMAN-HOUSE"],
        "narration": ("When the officer reached home, his servant rose to meet him at "
                      "the door, alive and well."),
        "must_show": "the boy standing in the doorway on his own legs as the officer arrives — the master stopped dead on the threshold.",
        "must_not_show": "do not put Jesus in this frame; the boy is STANDING, not in bed.",
        "scene": (
            "The centurion has come in through the outer door and stopped dead on the "
            "threshold, still in his cuirass with the helmet under his arm — and the "
            "young servant is standing upright in the inner doorway on his own legs, "
            "colour in his face, one hand on the frame, coming toward him. The "
            "officer's whole body has frozen mid-step. Hard afternoon daylight across "
            "the tiles between them. The camera is back far enough to see both men "
            "head to feet. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r015-b40", "out": "s40-the-soldier-came-apart.jpeg", "seg": "n22 p2",
        "window": "232.64-236.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["CENTURION"],
        "narration": ("This hardened soldier, who commanded a hundred men, came apart."),
        "must_show": "close on the officer's face breaking — twenty years of discipline collapsing all at once.",
        "must_not_show": "do not put Jesus in this frame; this is not dignified weeping — it is a hard man losing hold of himself.",
        "scene": (
            "Very close on the centurion's weathered face as it comes apart "
            "completely. His mouth has pulled down and open, his eyes have screwed "
            "shut and tears are running freely down the scarred cheeks, his chin is "
            "shaking — twenty years of discipline gone in one second. The helmet has "
            "slipped and he is gripping the doorframe with his other hand. Hard "
            "afternoon light on his face. He has one head."
        ),
    },
    {
        "id": "v2-r015-b41", "out": "s41-the-word-had-been-enough.jpeg", "seg": "n22 p3",
        "window": "236.28-240.00", "wide": True, "jesus": False, "ref": False,
        "locks": ["CENTURION", "SERVANT", "ROMAN-HOUSE"],
        "narration": ("He had trusted Jesus's word, and the word had been enough."),
        "must_show": "the closing frame: the officer holding the boy — an armoured Roman with both arms around a slave.",
        "must_not_show": "do not put Jesus in this frame; nobody else is present. The whole story ends with the two people it was about.",
        "scene": (
            "The centurion has crossed the room and taken the young servant in both "
            "arms, the dropped helmet lying on the tiles behind him, one iron-clad arm "
            "around the boy's thin shoulders and his other hand cupped behind his head. "
            "The boy's arms have come up around him. An officer of the occupying army "
            "holding a slave, in an empty room, with nobody watching and nobody to "
            "perform it for. Warm afternoon light through the shutter. The camera is "
            "back far enough to hold both of them and the quiet room. Every figure has "
            "two arms, two hands and one head."
        ),
    },
]
