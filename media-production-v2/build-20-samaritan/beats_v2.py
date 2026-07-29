#!/usr/bin/env python3
"""V2 beat map — row 20, build-20-samaritan (Luke 10:25-37).

COVERAGE: 30 pictures against V1's 8, over 173.0 s = 5.8 s/picture.

⚠️ CONTENT-CARE — THE RESTRAINT LAW BINDS THIS BUILD even though row 20 is not
in the §3 flag table. v30 says the robbers "stripped him of his raiment, and
WOUNDED him, and departed, leaving him HALF DEAD". The violence is never the
picture:

  · THE ATTACK IS NEVER SHOWN. No robbers striking, no blows landing, no weapon
    in motion, no struggle. The story cuts straight from the road to the
    aftermath, exactly as the narration does.
  · NO GORE. Wounds are dust, bruising and dark stains on cloth — never open
    injuries in close-up, never pooled blood, never a lingering shot of damage.
  · MODESTY. "Stripped of his raiment" is shown as torn remains of a tunic, a
    cloak thrown over him, and framing that keeps him covered. He keeps his
    dignity in every frame he is in.
  · QC question for every frame of him: "would a parent let a 10-year-old see
    this?" If no, regenerate.

What carries the weight instead is what the law says it should: the FACES of the
people who pass, and the hands of the one who stops.

SCRIPTURE FACTS (Luke 10:25-37 KJV):
  v25  a LAWYER — a scholar of the law — stood up and TEMPTED him. He is not an
       honest questioner, and the narration says so ("It sounds humble. It was
       not.").
  v29  "willing to JUSTIFY HIMSELF" he asks "who is my neighbour?" — a request
       for a boundary, which is what n2 spells out.
  v30  the road from Jerusalem DOWN to Jericho — a real descent of about 3,300
       feet through bare rock gorges, notorious for robbers.
  v31-32 a PRIEST, then a LEVITE. Both SAW him and both "passed by on the OTHER
       SIDE" — the crossing-over is the action, and both frames must show it.
  v33  the SAMARITAN "had COMPASSION on him" — the hated outsider is the hero,
       which is the whole scandal of the parable.
  v34  "bound up his wounds, POURING IN OIL AND WINE, and set him on HIS OWN
       BEAST, and brought him to an inn."
  v35  "two pence" — about two days' wages — and an open-ended promise to cover
       whatever more it costs.
  v37  the lawyer cannot say the word "Samaritan"; he says "HE THAT SHEWED MERCY
       ON HIM". b27 is built on that evasion.

TIME OF DAY: the frame story with the lawyer is bright midday in a Judean town.
The parable runs from hard midday on the Jericho road, through late afternoon as
the Samaritan travels, to lamplit night at the inn and morning at the departure.
"""

LOCKS = {
    "LAWYER": (
        "LAWYER LOCK: the scholar of the law is the same man in every shot — about "
        "forty-five, well-groomed and self-assured, a neatly combed dark beard "
        "going grey at the edges, sharp intelligent eyes and a faintly superior set "
        "to the mouth. He wears a finely woven DEEP INDIGO robe with a woven "
        "dark-red border and a dark prayer shawl with dark fringe (never cream, "
        "never white). His face is shown clearly."
    ),
    "TRAVELLER": (
        "BEATEN TRAVELLER LOCK: the robbed man is the same person in every shot — "
        "about thirty-five, ordinary and unremarkable, warm olive skin, a short dark "
        "beard, dark hair. What remains of his clothing is a torn and dust-caked "
        "under-tunic in faded brown. He is shown with dust, bruising and dark "
        "staining on the cloth — NEVER open wounds, never blood pooling, never "
        "anything a child should not see — and he is kept covered and dignified in "
        "every frame."
    ),
    "PRIEST": (
        "PRIEST LOCK: the priest is the same man in every shot — about sixty, "
        "portly and dignified, a full well-kept white-grey beard, heavy brows. He "
        "wears a finely woven DARK PLUM robe with an embroidered border and a "
        "dark-striped shawl (never cream, never white), and carries a staff. His "
        "face is shown clearly and is troubled rather than cruel."
    ),
    "LEVITE": (
        "LEVITE LOCK: the temple assistant is the same man in every shot — about "
        "thirty-five, lean and brisk, a short trimmed dark beard, anxious darting "
        "eyes. He wears a good DARK TEAL-BLUE robe with a plain dark sash (never "
        "cream, never white) and carries a satchel. His face is shown clearly and is "
        "frightened rather than cruel."
    ),
    "SAMARITAN": (
        "SAMARITAN LOCK: the Samaritan is the same man in every shot — about forty, "
        "broad and weather-beaten from the road, sun-darkened skin, a thick "
        "untrimmed black beard, heavy calloused hands, and a plain steady face. He "
        "wears a hard-wearing DARK OCHRE-BROWN travelling robe with a rough "
        "striped mantle of a foreign weave and a wide leather belt (never cream, "
        "never white). He leads a patient grey donkey loaded with travelling packs. "
        "His face is shown clearly."
    ),
    "JERICHO-ROAD": (
        "JERICHO ROAD LOCK: the steep descending road from Jerusalem to Jericho — a "
        "narrow track of pale broken stone falling away through bare rock gorges and "
        "cliffs of tawny limestone, with deep ravines below, thorn scrub, caves and "
        "boulders crowding the edges, and no green anywhere. Harsh, dry and empty, "
        "with hard overhead sun and black shadow in the clefts."
    ),
    "INN": (
        "INN LOCK: a rough roadside inn — a low building of dry stone around a small "
        "courtyard, an arched entry, a stable end with straw and a water trough, "
        "plain rooms off the yard with rush mats and clay lamps, a well and a fig "
        "tree. Simple, working and unadorned."
    ),
    "CROWD": (
        "CROWD LOCK: the crowd listening are ordinary Judean working people of every "
        "age in SATURATED DEEP earth colours — dark chocolate brown, deep russet, "
        "burnt ochre, dark olive, dusty indigo and faded plum wool. No one in the "
        "crowd wears off-white, ivory or any near-white cloth. Their faces are shown "
        "clearly."
    ),
}

REF = True

BEATS = [
    # -------------------------------------------------- n1 — the test ----
    {
        "id": "v2-r020-b01", "out": "s01-a-scholar-stood-up.jpeg", "seg": "n1",
        "window": "0.28-4.46", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LAWYER", "CROWD"],
        "narration": ("A scholar of the law stood up to test Jesus, and asked him a "
                      "question."),
        "must_show": "the lawyer standing up out of a seated crowd to put a question — confident, performing slightly for the room.",
        "must_not_show": "no halo, glare or rim-light; he is not hostile on the surface, he is polished.",
        "scene": (
            "In a sunlit town square with a crowd seated on the ground and on low "
            "walls around Jesus, one well-dressed man has risen to his feet among "
            "them. He stands with his chin up and one hand lifted in a practised "
            "rhetorical gesture, addressing Jesus, plainly aware of the room watching "
            "him. Jesus is seated, looking up at him calmly. Bright midday light. The "
            "camera is back far enough to hold the standing man, Jesus and the near "
            "crowd. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r020-b02", "out": "s02-what-shall-i-do.jpeg", "seg": "s25",
        "window": "5.09-8.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAWYER"],
        "narration": ("Master, what shall I do to inherit eternal life? (Luke 10:25)"),
        "must_show": "close on the lawyer asking — smooth, assured, watching Jesus's face for the answer he expects.",
        "must_not_show": "do not put Jesus in this frame; the question is a test and the face should carry a trace of that.",
        "scene": (
            "Close on the scholar's face as he asks. His expression is smooth and "
            "assured with the faintest edge of challenge under the courtesy — his "
            "brows slightly raised, his eyes steady and evaluating, one corner of his "
            "mouth just short of a smile. He is watching for a reaction. Bright "
            "daylight on his combed beard and indigo collar. He has one head."
        ),
    },
    {
        "id": "v2-r020-b03", "out": "s03-what-does-the-law-say.jpeg", "seg": "n1b p1",
        "window": "9.21-12.83", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Jesus turned it straight back on him — what does the law say?"),
        "must_show": "close on Jesus returning the question — one hand open toward the man, unbothered, faintly amused.",
        "must_not_show": "no halo, glare or rim-light; no defensiveness — he is handing it back easily.",
        "scene": (
            "Close on Jesus seated in the bright square, turning the question back with "
            "one hand come open and gestured toward the man standing over him. His "
            "face is relaxed and faintly amused, eyebrows lifted, entirely unbothered "
            "at being tested. Bright midday light and the blurred crowd behind. His "
            "hand has five fingers."
        ),
    },
    {
        "id": "v2-r020-b04", "out": "s04-he-answered-it-well.jpeg", "seg": "n1b p2",
        "window": "12.83-19.02", "wide": True, "jesus": False, "ref": False,
        "locks": ["LAWYER", "CROWD"],
        "narration": ("And the man answered it well: love God with everything you are, "
                      "and love your neighbor as yourself."),
        "must_show": "the lawyer answering fluently to the whole crowd — he genuinely knows this, and heads nod.",
        "must_not_show": "he is not wrong and not foolish here; do not put Jesus in this frame.",
        "scene": (
            "The scholar has turned slightly to take in the whole crowd as he answers, "
            "reciting fluently with one hand marking the beats of it, entirely in "
            "command of the material. Around him seated people are nodding along, one "
            "old man's lips moving with the familiar words. He knows this perfectly "
            "well. Bright midday light in the square. The camera is back far enough to "
            "hold him and the near crowd. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r020-b05", "out": "s05-it-was-not-humble.jpeg", "seg": "n1b p3-p5",
        "window": "19.02-23.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAWYER"],
        "narration": ("Then he asked one more question. It sounds humble. It was not."),
        "must_show": "close on the lawyer as the second question comes — the polish thinning, something self-protective underneath it.",
        "must_not_show": "not a sneer; v29 says he wanted to justify himself, so the tell is defensiveness, not malice.",
        "scene": (
            "Close on the scholar's face as he frames his second question. The easy "
            "confidence has thinned — his eyes have narrowed very slightly and moved "
            "off Jesus's face for an instant, his chin has come up a fraction, and "
            "there is something careful and self-protective under the polished "
            "surface. He is defending something. Bright daylight. He has one head."
        ),
    },
    {
        "id": "v2-r020-b06", "out": "s06-who-is-my-neighbour.jpeg", "seg": "s29",
        "window": "24.37-25.81", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LAWYER", "CROWD"],
        "narration": "And who is my neighbour? (Luke 10:29)",
        "must_show": "the question put across the open ground to Jesus, the crowd quiet and watching to see how he handles it.",
        "must_not_show": "no halo, glare or rim-light.",
        "scene": (
            "The scholar stands over the seated Jesus with both hands turned open in "
            "front of him, mid-question, and the crowd around them has gone quiet and "
            "still, heads turning between the two men to see what happens. Jesus looks "
            "up at him steadily. Bright midday light across the square. The camera is "
            "back far enough to hold both men and the watching crowd. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r020-b07", "out": "s07-hoping-for-limits.jpeg", "seg": "n2 p1",
        "window": "26.87-30.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAWYER"],
        "narration": ("It was the kind of question you ask when you are hoping the "
                      "answer has limits."),
        "must_show": "close on the lawyer waiting for the answer — hoping for a boundary, a little tense about it.",
        "must_not_show": "do not put Jesus in this frame.",
        "scene": (
            "Close on the scholar's face waiting. His jaw has tightened and his eyes "
            "are fixed and expectant, and there is a small anxious readiness in the "
            "expression — a man hoping very much that the reply will contain a line he "
            "can stand behind. Bright daylight on his indigo shoulder. He has one head."
        ),
    },
    {
        "id": "v2-r020-b08", "out": "s08-who-he-could-ignore.jpeg", "seg": "n2 p2",
        "window": "30.73-35.88", "wide": True, "jesus": False, "ref": False,
        "locks": ["LAWYER", "CROWD"],
        "narration": ("He wanted a line drawn, so he could know exactly who he was "
                      "allowed to ignore."),
        "must_show": "the lawyer standing apart from the ordinary crowd — well-dressed among working people, the distance already drawn without a word.",
        "must_not_show": "nobody is being unkind; the separation is his, and it is visible in clothing and posture. Do not put Jesus in this frame.",
        "scene": (
            "In the sunlit square the scholar stands upright and immaculate in his "
            "deep indigo robe with a clear space around him, and the crowd seated on "
            "the dust nearby are labourers and women and old men in worn brown and "
            "ochre wool. Nobody has moved away from him and nobody has spoken — the "
            "gap is simply there, in the cloth and in how he holds himself. Bright "
            "midday light. The camera is back far enough to hold him and the seated "
            "crowd. Every figure has two arms, two hands and one head."
        ),
    },
    # ---------------------------------------------- n3/n4 — the road ----
    {
        "id": "v2-r020-b09", "out": "s09-he-answered-with-a-story.jpeg", "seg": "n3 p1",
        "window": "36.50-38.15", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CROWD"],
        "narration": "Jesus answered with a story.",
        "must_show": "Jesus beginning the parable — an open storyteller's hand, the crowd leaning in.",
        "must_not_show": "no halo, glare or rim-light.",
        "scene": (
            "Jesus has shifted forward where he sits and lifted one hand in the easy "
            "open gesture of a man beginning a story, his face warm. All around him "
            "the seated crowd has leaned in, faces turning to him, a child pulled onto "
            "a knee. Bright midday light in the square. The camera is back far enough "
            "to hold Jesus and the near crowd. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r020-b10", "out": "s10-the-way-of-blood.jpeg", "seg": "n3 p2",
        "window": "38.15-46.62", "wide": True, "jesus": False, "ref": False,
        "locks": ["TRAVELLER", "JERICHO-ROAD"],
        "narration": ("A man was traveling the steep, lonely road down to Jericho, a "
                      "road so full of robbers that people called it the Way of Blood."),
        "must_show": "the road's real character — a single traveller tiny on a narrow track descending through bare rock gorges, boulders and caves crowding it.",
        "must_not_show": "no robbers visible yet and no violence; the menace is the landscape itself.",
        "scene": (
            "A wide high view of the Jericho road — a narrow pale track falling steeply "
            "away through bare tawny rock gorges, hemmed by boulders, black cave "
            "mouths and thorn scrub, with deep ravines dropping below it and no green "
            "anywhere. One lone traveller walks it, small against all that stone, "
            "utterly alone. Hard overhead sun and black shadow in the clefts. He has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r020-b11", "out": "s11-robbers-were-what-he-found.jpeg", "seg": "n4 p1",
        "window": "47.23-49.18", "wide": True, "jesus": False, "ref": False,
        "locks": ["JERICHO-ROAD"],
        "narration": "Robbers were exactly what he found.",
        "must_show": "⚠️ RESTRAINT LAW: the attack is NOT shown. Only the empty road at the moment after — dust still hanging, a dropped satchel, figures already gone over the ridge.",
        "must_not_show": "NO robbers striking, NO blows, NO weapons in motion, NO struggle, NO victim in this frame. The cut away from the violence is the whole point.",
        "scene": (
            "A stretch of the narrow rock road with the dust of a scuffle still hanging "
            "in the hard air above it. A traveller's satchel lies burst open on the "
            "stones with its contents scattered, a broken staff beside it, and a "
            "sandal thrown clear. Far up on the ridge above, three small figures are "
            "disappearing over the skyline with bundles on their shoulders, already "
            "almost gone. There is no one else in the frame and nothing violent is "
            "happening in it. Hard overhead sun."
        ),
    },
    {
        "id": "v2-r020-b12", "out": "s12-half-dead-beside-the-road.jpeg", "seg": "n4 p2",
        "window": "49.18-54.33", "wide": True, "jesus": False, "ref": False,
        "locks": ["TRAVELLER", "JERICHO-ROAD"],
        "narration": ("They stripped him, beat him, and left him half dead in the dust "
                      "beside the road."),
        "must_show": "⚠️ RESTRAINT + MODESTY: the aftermath only — the man lying still in the dust at the road's edge, seen from a respectful distance, covered by what is left of his tunic.",
        "must_not_show": "NO open wounds, NO blood pooling, NO close-up of damage, NOTHING exposed. Dust, stillness and the empty road carry it. Would a parent let a 10-year-old see this frame?",
        "scene": (
            "Seen from some way off along the road: a man lies motionless on his side "
            "in the dust at the edge of the track, half in the black shadow of a "
            "boulder. What is left of his torn brown under-tunic still covers him, "
            "grey with dust, and one arm is flung out across the stones. Nothing about "
            "his injuries is visible from this distance — only that he is not moving. "
            "The empty road runs away above and below him through the bare rock. Hard "
            "overhead sun. He has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------ n5/n6 — passing by ----
    {
        "id": "v2-r020-b13", "out": "s13-the-priest-crossed-over.jpeg", "seg": "n5 p1",
        "window": "54.98-58.98", "wide": True, "jesus": False, "ref": False,
        "locks": ["PRIEST", "TRAVELLER", "JERICHO-ROAD"],
        "narration": ("A priest came down that same road, saw the man, and crossed to "
                      "the far side."),
        "must_show": "SCRIPTURE-EXACT (v31): he SEES him — head turned, eyes on the body — and is walking on the FAR side of the track, the crossing-over unmistakable.",
        "must_not_show": "he must not simply fail to notice; the seeing and the crossing must both be visible. He is troubled, not cruel.",
        "scene": (
            "The priest walks down the rock road hard against the far edge of the "
            "track, as far from the near side as the road allows, his plum robe "
            "gathered up in one hand and his staff in the other. His head is turned "
            "and his eyes are plainly on the man lying in the dust across the road "
            "from him — he has seen him. His face is troubled and unhappy and he does "
            "not slow down. The gap of open road between them is clear. Hard sun. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r020-b14", "out": "s14-the-levite-also.jpeg", "seg": "n5 p2",
        "window": "58.98-63.43", "wide": True, "jesus": False, "ref": False,
        "locks": ["LEVITE", "TRAVELLER", "JERICHO-ROAD"],
        "narration": ("Then a temple assistant came, looked, and also crossed over."),
        "must_show": "the same staging repeated with the Levite — looking, then crossing to the far side — so the pattern reads.",
        "must_not_show": "he is frightened rather than callous; nobody sneers at the man on the ground.",
        "scene": (
            "The Levite comes down the same stretch of road and has moved across to "
            "the far edge, his teal robe pulled close and his satchel clutched against "
            "his chest. He has stopped for a half-step and is looking directly across "
            "at the still figure in the dust, his eyes wide and his mouth tight with "
            "fear — and then he is moving on, shoulder already turning away. The same "
            "gap of open road lies between them. Hard sun and black shadow. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r020-b15", "out": "s15-the-men-who-knew-the-law.jpeg", "seg": "n6 p1-p2",
        "window": "64.08-71.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["PRIEST"],
        "narration": ("These were the religious professionals, the men who knew the law "
                      "best. Maybe they feared a bloody body would make them unclean for "
                      "the temple."),
        "must_show": "close on the priest's face as he passes — genuinely conflicted, calculating a rule, not enjoying it.",
        "must_not_show": "not a villain's face; the tragedy is that he is a decent man following a rule. Do not show the injured man in this frame.",
        "scene": (
            "Close on the priest's face in profile as he walks on past. His brows are "
            "drawn together and his eyes are fixed hard on the road ahead of him, his "
            "mouth pressed thin — the face of a man working through a rule in his head "
            "and not enjoying where it lands. There is real discomfort in it and no "
            "cruelty at all. Hard sun on his white-grey beard. He has one head."
        ),
    },
    {
        "id": "v2-r020-b16", "out": "s16-they-kept-their-distance.jpeg", "seg": "n6 p3",
        "window": "71.00-73.42", "wide": True, "jesus": False, "ref": False,
        "locks": ["TRAVELLER", "JERICHO-ROAD"],
        "narration": "Either way, they kept their distance.",
        "must_show": "the man alone again on the empty road, two small figures already far away down the track — the distance made literal.",
        "must_not_show": "no gore; keep him at a respectful distance and covered.",
        "scene": (
            "The man lies where he was in the dust at the road's edge, alone. Far down "
            "the descending track two small robed figures are walking away and are "
            "nearly out of sight around the rock. Between them and him is nothing but "
            "empty stone road. Hard overhead sun, deep black shadow in the gorge "
            "below. He has two arms, two hands and one head."
        ),
    },
    # --------------------------------------------------- n7/n8 — the Samaritan ----
    {
        "id": "v2-r020-b17", "out": "s17-then-a-samaritan-came.jpeg", "seg": "n7 p1",
        "window": "74.03-75.84", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "JERICHO-ROAD"],
        "narration": "Then a Samaritan came down the road.",
        "must_show": "the Samaritan coming down the track with his loaded donkey — visibly a foreigner by his mantle, an ordinary traveller.",
        "must_not_show": "nothing heroic in his bearing yet; he is just a man on a road.",
        "scene": (
            "A broad weather-beaten man comes down the rock road leading a patient grey "
            "donkey loaded with travelling packs, his rough striped mantle of foreign "
            "weave marking him out as not from here. He is walking steadily, watching "
            "his footing on the loose stone, entirely ordinary. The bare gorge rises "
            "around him. Hard afternoon sun. The camera is back far enough to see him "
            "and the animal head to hoof. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r020-b18", "out": "s18-an-old-hatred.jpeg", "seg": "n7 p2-p3",
        "window": "75.84-85.55", "wide": True, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": ("And the crowd listening to Jesus was raised to despise Samaritans. "
                      "Different blood, wrong worship, an old hatred hundreds of years "
                      "deep."),
        "must_show": "back in the square: the crowd's faces changing at the word — mouths tightening, someone shaking his head, the temperature dropping.",
        "must_not_show": "do not put Jesus in this frame; nobody shouts — it is a room going cold.",
        "scene": (
            "Back in the sunlit square, the listening crowd's faces have all changed at "
            "once. A man's mouth has pulled down hard, a woman has drawn back with her "
            "brows up, an older man is shaking his head slowly, and two men have "
            "glanced at each other. Nobody has said anything, but the warmth has gone "
            "straight out of the gathering. Bright midday light. The camera is back "
            "far enough to hold a dozen faces. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r020-b19", "out": "s19-the-last-man-expected.jpeg", "seg": "n8",
        "window": "86.12-91.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LAWYER", "CROWD"],
        "narration": ("A Samaritan was the last man in the world they expected to be the "
                      "hero of the story."),
        "must_show": "Jesus telling it straight into that cold room, and the lawyer's face beginning to work out where this is going.",
        "must_not_show": "no halo, glare or rim-light; Jesus is not provoking them for sport — he is warm and steady.",
        "scene": (
            "Jesus goes on with the story into the cooled room, his face warm and "
            "unhurried, one hand still moving with the telling. In the crowd the "
            "scholar of the law is standing very still now with his eyes narrowed and "
            "fixed, and something has begun to work behind them as he sees the shape "
            "of where this is going. The other faces are guarded. Bright midday light. "
            "The camera holds Jesus, the lawyer and the near crowd. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r020-b20", "out": "s20-moved-with-compassion.jpeg", "seg": "n9",
        "window": "91.60-96.15", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "TRAVELLER", "JERICHO-ROAD"],
        "narration": ("He saw the beaten stranger. And the text says he was moved with "
                      "compassion."),
        "must_show": "⚠️ THE INVERSE OF b13/b14: he has stopped dead in the road and is COMING TOWARD the man, not crossing away — the donkey's reins dropped.",
        "must_not_show": "no gore; the injured man stays covered and at a respectful angle. The direction of movement is the whole beat.",
        "scene": (
            "The Samaritan has stopped dead in the middle of the road and is already "
            "moving TOWARD the man in the dust, the donkey's lead rope dropped and "
            "trailing on the stones behind him. His face has come open with plain "
            "shock and pity, one hand already reaching out ahead of him. He is "
            "crossing the road in exactly the opposite direction from the two who came "
            "before. The injured man lies covered in his torn tunic at the road's "
            "edge. Hard afternoon sun. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    # ------------------------------------------------ n10 — the care ----
    {
        "id": "v2-r020-b21", "out": "s21-he-knelt-in-the-dirt.jpeg", "seg": "n10 p1",
        "window": "96.81-100.35", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "TRAVELLER", "JERICHO-ROAD"],
        "narration": ("He knelt down in the dirt beside a man his people were supposed "
                      "to hate."),
        "must_show": "him down on both knees in the dust right beside the man, close enough to touch — no distance left at all.",
        "must_not_show": "no gore; frame from above and to the side so the injured man reads as covered and dignified.",
        "scene": (
            "The Samaritan is down on both knees in the dust of the road right beside "
            "the injured man, his ochre robe already filthy at the knees, leaning over "
            "him with one hand braced on the stones and the other going to his "
            "shoulder. There is no gap between them at all. The injured man's torn "
            "tunic covers him and the framing is from above and to the side. His "
            "loaded donkey stands waiting behind. Hard afternoon sun. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r020-b22", "out": "s22-oil-and-wine.jpeg", "seg": "n10 p2a",
        "window": "100.35-103.3", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAMARITAN"],
        "narration": "He cleaned and bound the wounds,",
        "must_show": "SCRIPTURE-EXACT (v34): his hands pouring from a small flask and tearing his own cloth into a bandage — the practical work of it.",
        "must_not_show": "⚠️ NO wound visible in this frame at all. Show only the hands, the flask and the cloth. That is the restraint law.",
        "scene": (
            "Close on the Samaritan's heavy calloused hands at work — one tipping a "
            "small clay flask so a thin stream of oil runs out of it, the other holding "
            "a strip of pale cloth he has torn from his own mantle, its ragged edge "
            "still trailing. A second flask stands open on the stone beside his knee. "
            "Only his hands, the flasks and the cloth are in frame; no injury is "
            "visible. Hard sunlight on dust and skin. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r020-b23", "out": "s23-on-his-own-animal.jpeg", "seg": "n10 p2b",
        "window": "103.3-106.23", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "TRAVELLER", "JERICHO-ROAD"],
        "narration": ("lifted him onto his own animal, and walked beside him on foot."),
        "must_show": "SCRIPTURE-EXACT: the injured man up on the donkey wrapped in the Samaritan's own mantle, and the Samaritan WALKING on foot beside him.",
        "must_not_show": "the Samaritan must NOT be riding — giving up his own place is the point; no gore, the man is wrapped and covered.",
        "scene": (
            "The injured man is up on the grey donkey, slumped forward over its neck "
            "and wrapped around the shoulders in the Samaritan's own striped mantle, "
            "held steady by a hand at his back. The Samaritan walks on foot beside the "
            "animal, leading it by the halter down the descending road, his own packs "
            "shifted to his shoulders to make room. He is not riding. The bare gorge "
            "and the long road stretch ahead in late afternoon light. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------ n11 / j35 — the inn ----
    {
        "id": "v2-r020-b24", "out": "s24-cared-for-him-through-the-night.jpeg", "seg": "n11 p1",
        "window": "106.80-109.51", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "TRAVELLER", "INN"],
        "narration": ("He brought him to an inn and cared for him through the night."),
        "must_show": "the lamplit inn room at night — the man asleep on a mat, the Samaritan still awake beside him, having stayed.",
        "must_not_show": "no gore; the man is covered by a blanket. The staying-all-night is the beat.",
        "scene": (
            "A small lamplit room off the inn courtyard at night. The injured man lies "
            "asleep on a rush mat under a rough blanket, his face washed and quiet. "
            "The Samaritan sits on the floor beside him with his back against the wall, "
            "awake, a cup of water in his hand and his head tipped back against the "
            "stone, watching him. A clay lamp burns low. He has not left. Warm uneven "
            "lamplight, deep shadow. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r020-b25", "out": "s25-two-silver-coins.jpeg", "seg": "n11 p2",
        "window": "109.51-117.30", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "INN"],
        "narration": ("In the morning he pressed two silver coins into the innkeeper's "
                      "hand, about two days wages, and said, take care of him."),
        "must_show": "two countable silver coins being pressed into the innkeeper's palm in the morning courtyard, the Samaritan's hand closing the man's fingers over them.",
        "must_not_show": "the coins must be countable — two — not a vague handful.",
        "scene": (
            "In the inn courtyard in early morning light, the Samaritan has taken the "
            "innkeeper's hand in both of his and pressed TWO small silver coins into "
            "the open palm, folding the man's fingers closed over them. The innkeeper, "
            "a stout aproned man, is looking down at his hand and then up at him with "
            "his eyebrows raised. The loaded donkey waits at the arch behind. Warm low "
            "morning light. The camera is close enough to count the coins. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r020-b26", "out": "s26-i-will-repay-thee.jpeg", "seg": "j35",
        "window": "117.92-124.70", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "INN"],
        "narration": ("Take care of him; and whatsoever thou spendest more, when I come "
                      "again, I will repay thee. (Luke 10:35)"),
        "must_show": "the open-ended promise being made — the Samaritan's hand on the innkeeper's shoulder, looking back toward the room where the man is.",
        "must_not_show": "do not put Jesus in this frame; this is not a transaction being closed but one being left open.",
        "scene": (
            "The Samaritan has one hand on the innkeeper's shoulder and is speaking to "
            "him seriously, his other hand gesturing back across the courtyard toward "
            "the doorway of the room where the injured man is lying. The innkeeper is "
            "nodding slowly, holding the coins. The Samaritan's face is plain and "
            "committed — he is promising something without a limit on it. Early morning "
            "light in the yard. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r020-b27", "out": "s27-he-tied-his-own-name-to-it.jpeg", "seg": "n12",
        "window": "125.75-130.35", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "INN"],
        "narration": ("He did not just help and move on. He tied his own name to a "
                      "stranger's recovery."),
        "must_show": "him leaving with a backward look toward the room — the departure of a man who is coming back.",
        "must_not_show": "do not put Jesus in this frame; he is not slipping away, he is leaving and returning.",
        "scene": (
            "The Samaritan leads his donkey out under the arch of the inn courtyard "
            "into the morning, and he has turned back at the gateway for one long look "
            "across the yard at the doorway of the room where he left the man. His "
            "hand rests on the animal's neck. It is the pause of someone who intends "
            "to come back. Long low morning light through the arch. He has two arms, "
            "two hands and one head."
        ),
    },
    # ---------------------------------------------- n13 / j1 / s37 — turned back ----
    {
        "id": "v2-r020-b28", "out": "s28-which-was-the-neighbour.jpeg", "seg": "n13 + j1",
        "window": "131.00-143.94", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LAWYER", "CROWD"],
        "narration": ("Then Jesus turned the scholar's own question back on him, and "
                      "asked which of the three men had been the neighbor. — Which now "
                      "of these three, thinkest thou, was neighbour unto him that fell "
                      "among the thieves? (Luke 10:36)"),
        "must_show": "Jesus putting the question straight back to the lawyer, and the whole crowd turning to watch the man answer.",
        "must_not_show": "no halo, glare or rim-light; nothing gloating in Jesus's face — the question is genuine.",
        "scene": (
            "Jesus has turned fully to the scholar with one hand open toward him, "
            "putting the question back. Every face in the seated crowd has swung round "
            "to the standing man to watch him answer, and he is caught in all of it. "
            "Jesus's expression is warm and open with nothing triumphant in it. Bright "
            "midday light in the square. The camera is back far enough to hold Jesus, "
            "the lawyer and the crowd. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r020-b29", "out": "s29-he-that-shewed-mercy.jpeg", "seg": "s37 + n14 p1",
        "window": "145.01-151.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAWYER"],
        "narration": ("He that shewed mercy on him. (Luke 10:37) — The scholar could not "
                      "even bring himself to name the Samaritan."),
        "must_show": "⚠️ THE EVASION ON HIS FACE: close on the lawyer answering — the word 'Samaritan' visibly avoided, his mouth working around it.",
        "must_not_show": "do not put Jesus in this frame; he is not defiant — he is cornered and choosing his words.",
        "scene": (
            "Close on the scholar's face as he answers. His jaw has tightened and his "
            "eyes have dropped away, and his mouth moves carefully around the sentence "
            "— a man selecting a phrase precisely so as not to have to say a "
            "particular word out loud. There is no defiance in it, only discomfort and "
            "a kind of defeat. Bright midday light. He has one head."
        ),
    },
    {
        "id": "v2-r020-b30", "out": "s30-go-and-do-thou-likewise.jpeg", "seg": "n14 p2 + j2 + n15",
        "window": "151.02-172.63", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LAWYER", "CROWD"],
        "narration": ("neighbor is not a category to define; it is mercy given to the "
                      "person in front of you. — Go, and do thou likewise. (Luke 10:37) "
                      "— The lesson ends in motion, not admiration. Mercy is something "
                      "to practice. That is how good he is. He will not even let you "
                      "keep score."),
        "must_show": "the closing frame: Jesus's open hand sending him off — not a verdict but a shove into motion — and the lawyer with nowhere to hide.",
        "must_not_show": "no halo, glare or rim-light; the scholar is not humiliated, he is sent. The gesture is outward, toward the road, not down at him.",
        "scene": (
            "Jesus has risen and his hand is extended outward past the scholar toward "
            "the open road leading out of the square, sending him — a gesture of motion "
            "rather than judgement — and his face is warm and entirely serious. The "
            "scholar stands in front of him with his arms down at his sides, his "
            "practised composure gone, looking at the road he is being pointed toward. "
            "The crowd is on its feet around them. Bright midday light, the town gate "
            "and the road beyond. The camera is back far enough to hold both men and "
            "the open road. Every figure has two arms, two hands and one head."
        ),
    },
]
