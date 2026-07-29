#!/usr/bin/env python3
"""V2 beat map — row 12, build-12-bartimaeus (Mark 10:46-52).

COVERAGE: 44 pictures against V1's 12, over 259.3 s = 5.9 s/picture — the band
rows 5-11 shipped at.

SCRIPTURE FACTS (Mark 10:46-52 KJV):
  v46  Jericho, "as he went OUT of Jericho with his disciples and a GREAT NUMBER
       of people". Passover pilgrim road, the last stop before the climb to
       Jerusalem. He sits BY THE HIGHWAY SIDE begging.
  v47  he cries "thou SON OF DAVID" — a messianic title, not "of Nazareth" which
       is what the crowd said. The blind man names him correctly; that is the
       point n2 makes.
  v48  "MANY charged him that he should hold his peace: but he cried the MORE a
       great deal."
  v49  "And Jesus STOOD STILL, and commanded him to be called."
  v50  "CASTING AWAY HIS GARMENT, rose, and came" — the cloak is a beggar's bed,
       coat and coin-catcher, and a blind man who throws it may never find it
       again. n7 spends 27 seconds on this; it gets five frames.
  v51  "What wilt thou that I should do unto thee?" — asked of an obviously
       blind man, because he wants the man's own voice.
  v52  "immediately he received his sight, and FOLLOWED JESUS IN THE WAY."

THE EYES CHANGE, so the BARTIMAEUS lock fixes face, build and clothing and says
NOTHING about his eyes — same reason row 5's lock said nothing about posture. Per
beat: clouded and unfocused through b36, clear and focused from b37 on.

THE CLOAK IS A PROP THAT MUST TRACK: on his lap catching coins (b04) -> thrown
back into the road (b28) -> left lying in the dust behind him (b30, b44). It must
never reappear on his shoulders after b28.

CONTENT-CARE: row 12 is GREEN. His blindness is never grotesque — clouded eyes
and a searching face, never a horror close-up.

TIME OF DAY: one bright dusty morning throughout. Hard sun, pale dust, the Judean
hills climbing away toward Jerusalem. No night, no sunset anywhere in this build.
"""

LOCKS = {
    "BART": (
        "BARTIMAEUS LOCK: the blind beggar is the same man in every shot — a Jewish "
        "man of about forty-five, lean and sinewy from hard living, deeply "
        "sun-weathered brown skin, a matted greying dark beard, unkempt dark hair "
        "going grey at the temples, and a strong bony face held slightly lifted and "
        "turned as though listening. He wears a filthy patched DARK BROWN beggar's "
        "tunic, frayed at the hem, with a rope belt and bare dusty feet (never cream, "
        "never white). His face is shown clearly."
    ),
    "CLOAK": (
        "CLOAK LOCK: the beggar's cloak is one particular object — a heavy, "
        "much-mended rectangle of coarse DARK RUSSET-BROWN wool, worn through and "
        "pale at the folds, its edges ragged and its corners darkened with years of "
        "handling. It is the only thing he owns."
    ),
    "ROAD-JERICHO": (
        "JERICHO ROAD LOCK: the wide dusty highway running out of Jericho — packed "
        "pale earth churned by thousands of feet, low mud-brick and stone walls along "
        "one side, date palms and thorn scrub, the flat green oasis behind and the "
        "bare stony Judean hills climbing away ahead toward Jerusalem. Bright hard "
        "morning sun, dust hanging in the air."
    ),
    "PILGRIMS": (
        "PILGRIM CROWD LOCK: a great Passover crowd on the road — hundreds of "
        "ordinary people of every age, families with bundles and children, men "
        "driving donkeys, women with baskets on their heads, pressing along the "
        "highway. They wear SATURATED DEEP earth colours — dark chocolate brown, deep "
        "russet, burnt ochre, dark olive, dusty indigo and faded plum wool. No one in "
        "the crowd wears off-white, ivory or any near-white cloth."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the disciples are the same group throughout — eight or nine "
        "working Galilean men between twenty and forty, dusty from the road with "
        "travel bags and staffs, in wool tunics of SATURATED DEEP colours: rust-brown, "
        "deep russet, dark olive, blue-grey and dusty indigo. None wears off-white, "
        "ivory or any near-white cloth. Their faces are shown clearly."
    ),
}

REF = True

BEATS = [
    # ---------------------------------------------------- n0 — the roadside ----
    {
        "id": "v2-r012-b01", "out": "s01-the-road-out-of-jericho.jpeg", "seg": "n0 p1",
        "window": "0.28-3.11", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD-JERICHO", "PILGRIMS"],
        "narration": "The road out of Jericho, on a loud and dusty day.",
        "must_show": "the wide highway crowded with travellers, dust hanging gold in hard morning sun, the hills climbing away beyond.",
        "must_not_show": "no principal characters yet; this is the place.",
        "scene": (
            "A wide view down the packed dusty highway leading out of Jericho, thick "
            "with travellers moving in both directions — families, loaded donkeys, "
            "men with bundles — dust hanging in the hard bright morning light above "
            "them. Date palms stand along the walls on one side and the bare stony "
            "hills climb away toward the horizon ahead. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b02", "out": "s02-half-the-country.jpeg", "seg": "n0 p2",
        "window": "3.11-10.83", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD-JERICHO", "PILGRIMS"],
        "narration": ("Jericho was the last stop before the climb up to Jerusalem, and "
                      "with the Passover feast coming, that road carried half the "
                      "country."),
        "must_show": "the sheer scale of the Passover crowd — the road packed solid with people as far as the eye can follow it, climbing toward the hills.",
        "must_not_show": "no principal characters; the crowd is the subject.",
        "scene": (
            "A high wide view along the highway as it runs out of the green oasis and "
            "begins to climb into the bare hills. The road is packed solid with "
            "people, an unbroken river of travellers stretching away into the "
            "distance and dust — hundreds of them, whole families, pack animals, "
            "bundles on heads. Hard morning sun, a haze of pale dust over everything. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b03", "out": "s03-crowds-meant-coins.jpeg", "seg": "n0 p3",
        "window": "10.83-13.48", "wide": False, "jesus": False, "ref": False,
        "locks": ["CLOAK", "ROAD-JERICHO"],
        "narration": "For a beggar, crowds meant coins.",
        "must_show": "close and low: the spread cloak on the ground with two or three small worn coins lying on it, and passing feet beyond.",
        "must_not_show": "no faces needed; an upright vertical photograph with the ground at the bottom and the horizon level — the picture is the right way up.",
        "scene": (
            "An upright vertical photograph from a low viewpoint, the ground at the "
            "bottom of the frame and the road beyond at the top, the horizon level — "
            "the picture is the right way up. Close on the worn dark russet cloak "
            "spread out on the dust, its mended folds catching hard sunlight, with "
            "two or three small dull worn coins lying on the cloth. Just past it the "
            "dusty sandalled feet of the passing crowd move by in a blur of dust."
        ),
    },
    {
        "id": "v2-r012-b04", "out": "s04-where-he-always-sat.jpeg", "seg": "n0 p4",
        "window": "13.48-25.29", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "CLOAK", "ROAD-JERICHO", "PILGRIMS"],
        "narration": ("And so a blind man named Bartimaeus sat where he always sat — at "
                      "the edge of the highway, his ragged cloak spread across his lap "
                      "to catch whatever fell, listening to a thousand feet walk past "
                      "him."),
        "must_show": "him seated against the wall at the road's edge, the cloak spread across his lap, the crowd streaming past without looking at him.",
        "must_not_show": "his eyes are CLOUDED and unfocused, not looking at anything; nobody in the crowd is interacting with him.",
        "scene": (
            "Bartimaeus sits cross-legged in the dust against a low stone wall at the "
            "very edge of the highway, his heavy dark russet cloak spread open across "
            "his lap and knees to catch whatever falls. His head is lifted and turned "
            "slightly to one side, listening, and his eyes are CLOUDED grey and "
            "unfocused, aimed at nothing. Past him the Passover crowd streams by in a "
            "wall of legs and dust, not one of them looking down at him. Hard morning "
            "sun. The camera is back far enough to hold him and the passing crowd. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b05", "out": "s05-he-knew-the-road-by-sound.jpeg", "seg": "n0 p5-p6",
        "window": "25.29-29.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART"],
        "narration": "Listening was his whole life. He knew the road by its sounds.",
        "must_show": "close on his face doing the one thing he can do — head tilted, ear turned to the road, absolute concentration, clouded eyes half closed.",
        "must_not_show": "not vacant or pitiable — this is a man working hard at his only sense.",
        "scene": (
            "Close on Bartimaeus's weathered face. His head is tilted and turned so "
            "one ear leads toward the road, his chin lifted, his clouded grey eyes "
            "half closed and unfocused, and every line of his face is drawn tight with "
            "concentration — a man reading the whole world through his ears. Dust on "
            "his beard and eyelashes, hard sunlight across his cheekbone. The blurred "
            "movement of the crowd is soft behind him."
        ),
    },
    # ------------------------------------------------- n1 — a name in the noise ----
    {
        "id": "v2-r012-b06", "out": "s06-this-day-was-different.jpeg", "seg": "n1 p1",
        "window": "30.16-31.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART"],
        "narration": "But this day the sound was different.",
        "must_show": "his head snapping round toward the city, whole body gone alert — something in the noise has changed.",
        "must_not_show": "he is not standing yet; the alertness is all in the head and shoulders.",
        "scene": (
            "Close on Bartimaeus, caught in the instant his head snaps around toward "
            "the sound. His chin has come up and around, his clouded eyes are wide "
            "open now though still unfocused, his mouth has parted, and one hand has "
            "come off his knee and gone flat to the ground as he braces. Every muscle "
            "in his face is listening. Bright dust and blurred movement behind him."
        ),
    },
    {
        "id": "v2-r012-b07", "out": "s07-a-moving-wall-of-voices.jpeg", "seg": "n1 p2",
        "window": "31.76-38.75", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "PILGRIMS", "ROAD-JERICHO"],
        "narration": ("A procession was coming out of the city — a moving wall of "
                      "voices — and inside the noise he caught a name."),
        "must_show": "a dense procession coming out of the city gate toward the camera, and small at the road's edge the seated beggar with his head turned to it.",
        "must_not_show": "Jesus is not identifiable in the crowd at this distance; do not attach a Jesus lock or ref.",
        "scene": (
            "A large noisy procession is coming out through the Jericho gate and down "
            "the highway — a dense press of people filling the road from wall to wall, "
            "talking and calling, kicking up a wall of dust ahead of them, faces "
            "indistinct in the crowd. At the near edge of the road, small against all "
            "of it, Bartimaeus sits with his head turned and lifted toward the "
            "oncoming noise. Hard morning sun, thick dust. The camera is back far "
            "enough to hold the procession and the seated man. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b08", "out": "s08-jesus-of-nazareth-passing.jpeg", "seg": "n1 p3-p4",
        "window": "38.75-48.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART"],
        "narration": ("Jesus of Nazareth was passing by. He had heard the stories "
                      "everyone had heard: a teacher who opened deaf ears, who made "
                      "lepers clean."),
        "must_show": "the name landing on him — his whole face changing, recognition and hope arriving at once.",
        "must_not_show": "do not put Jesus in this frame; the moment belongs to the beggar's face.",
        "scene": (
            "Very close on Bartimaeus's face as the name reaches him. His clouded eyes "
            "have gone wide, his eyebrows have shot up, and his mouth has fallen open "
            "— the whole weathered face transformed in an instant from listening to "
            "something like hope. One hand has come up half way to his chest. Hard "
            "sunlight, dust hanging in the air around him, the blurred crowd behind."
        ),
    },
    {
        "id": "v2-r012-b09", "out": "s09-passing-by-and-never-again.jpeg", "seg": "n1 p5-p6",
        "window": "48.26-53.27", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "PILGRIMS", "ROAD-JERICHO"],
        "narration": ("Passing by, and never again. A blind man cannot chase a crowd."),
        "must_show": "the cruelty of his position: he is up on his knees now, the crowd already sweeping past him, and he cannot follow it.",
        "must_not_show": "he must not be running or moving with the crowd — he is stuck at the roadside, which is the point.",
        "scene": (
            "Bartimaeus has come up onto his knees at the road's edge, one hand "
            "braced on the wall behind him and the other reaching uselessly out toward "
            "the road, his face turned to follow the sound. In front of him the "
            "procession is already sweeping past and away down the highway, a solid "
            "moving mass of backs and dust, and he cannot follow it. The gap between "
            "his outstretched hand and the moving crowd is clear. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b10", "out": "s10-all-he-had-was-his-voice.jpeg", "seg": "n1 p7",
        "window": "53.27-55.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART"],
        "narration": "All he had was his voice.",
        "must_show": "close on his chest and throat as he hauls in a huge breath — the whole body becoming an instrument.",
        "must_not_show": "he has not shouted yet; this is the breath before it.",
        "scene": (
            "Close on Bartimaeus from the chest up as he drags in an enormous breath. "
            "His ribs and chest have expanded hard under the filthy brown tunic, his "
            "throat is stretched, his head has gone back and his chin up, and both "
            "fists have clenched at his sides. His mouth is opening. Every part of him "
            "is being loaded like a drawn bow. Hard sunlight and dust."
        ),
    },
    {
        "id": "v2-r012-b11", "out": "s11-son-of-david.jpeg", "seg": "s47",
        "window": "56.21-58.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "PILGRIMS", "ROAD-JERICHO"],
        "narration": "Jesus, thou Son of David, have mercy on me. (Mark 10:47)",
        "must_show": "THE SHOUT — up on his knees, head back, mouth wide, both arms out, roaring over the crowd; nearby heads snapping round.",
        "must_not_show": "nothing dignified about it; this is a man screaming in the road.",
        "scene": (
            "Bartimaeus is up on his knees in the dust with his head thrown back and "
            "his mouth wide open, roaring at the top of his lungs, the cords standing "
            "out in his neck, both arms flung out and open toward the road. All around "
            "him the nearest travellers' heads have snapped round and people are "
            "stopping and staring at him. Dust hangs in the hard light. The camera is "
            "back far enough to see him and the reacting crowd. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    # ---------------------------------------------------- n2 — catch that title ----
    {
        "id": "v2-r012-b12", "out": "s12-so-he-used-it.jpeg", "seg": "n2 p1-p2",
        "window": "60.42-65.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART"],
        "narration": ("So he used it. He pulled in all the air his body would hold and "
                      "shouted: Catch that title."),
        "must_show": "close on the shout itself — the face contorted with the effort of being heard over hundreds of people.",
        "must_not_show": "no crowd needed in this frame; it is all in the face.",
        "scene": (
            "Very close on Bartimaeus's face mid-shout, filling the frame. His mouth "
            "is stretched wide, his eyes are screwed shut, every tendon in his neck is "
            "standing out and the veins show at his temple — the entire face given "
            "over to the physical work of being heard. Spit and dust in the hard "
            "sunlight around his mouth. Nothing else is in focus."
        ),
    },
    {
        "id": "v2-r012-b13", "out": "s13-the-crowd-said-nazareth.jpeg", "seg": "n2 p3",
        "window": "65.61-69.63", "wide": True, "jesus": False, "ref": False,
        "locks": ["PILGRIMS", "ROAD-JERICHO"],
        "narration": ("The crowd called him Jesus of Nazareth — the man from up north."),
        "must_show": "ordinary faces in the crowd talking about him casually — mildly interested, unimpressed, a famous teacher passing through.",
        "must_not_show": "do not put Jesus in this frame; nobody in it is excited or reverent.",
        "scene": (
            "Close among the pilgrim crowd on the road: three or four ordinary "
            "travellers walking along talking to each other about the man ahead — one "
            "gesturing forward with his chin, another shrugging with his mouth turned "
            "down, a woman with a basket on her head only half listening. Their faces "
            "are mildly curious and entirely unimpressed. Dust and hard sun. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b14", "out": "s14-the-name-of-the-king.jpeg", "seg": "n2 p4",
        "window": "69.63-75.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART"],
        "narration": ("Son of David was something else entirely: it was the name "
                      "reserved for the promised King, the Messiah."),
        "must_show": "close on Bartimaeus mid-shout again, but held — the face of a man who knows exactly what word he is using.",
        "must_not_show": "no crowd; the certainty in his face is the whole frame.",
        "scene": (
            "Close on Bartimaeus's face, still shouting but caught between breaths, "
            "his head up and turned toward the road. Beneath the strain there is "
            "something deliberate and certain in his expression — jaw set, brows "
            "drawn, a man who has chosen his words and means every one of them. Dust "
            "on his skin, hard morning light across him."
        ),
    },
    {
        "id": "v2-r012-b15", "out": "s15-the-blind-man-saw-it.jpeg", "seg": "n2 p5-p6",
        "window": "75.99-83.04", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "PILGRIMS", "ROAD-JERICHO"],
        "narration": ("Everyone with working eyes saw a traveling teacher. The blind "
                      "man was the one who saw who was actually walking past."),
        "must_show": "THE IRONY IN ONE FRAME: a crowd of seeing people looking bored and irritated, and one blind man among them with his face blazing with certainty.",
        "must_not_show": "do not put Jesus in this frame; the contrast between the crowd's faces and his is the whole picture.",
        "scene": (
            "A frame holding both at once: in the near ground Bartimaeus kneels with "
            "his clouded unseeing eyes and his face lifted and blazing with "
            "conviction, mouth open — and behind and around him a dozen travellers "
            "with perfectly good eyes look bored, irritated or faintly embarrassed, "
            "glancing at him sideways and moving on. Not one of their faces has "
            "anything in it. Hard sun, thick dust. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    # ------------------------------------------------- n3 — hush him ----
    {
        "id": "v2-r012-b16", "out": "s16-the-crowd-turned-on-him.jpeg", "seg": "n3 p1",
        "window": "83.57-85.23", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "PILGRIMS"],
        "narration": "And the crowd turned on him.",
        "must_show": "people rounding on him — a hand thrust out palm-first to silence him, faces turned down at him hard.",
        "must_not_show": "nobody strikes him; it is scolding and shoving-back, not violence.",
        "scene": (
            "Several travellers have rounded on Bartimaeus where he kneels. One has "
            "thrust a flat palm down toward his face in a hard shushing gesture, "
            "another is bent over him with a finger pointed and his mouth open "
            "scolding, a third has a hand on his shoulder pushing him back down. "
            "Bartimaeus's face is turned up among them, mouth still open. Nobody is "
            "striking him. Dust and hard sun. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r012-b17", "out": "s17-many-voices.jpeg", "seg": "n3 p2",
        "window": "85.23-91.35", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "PILGRIMS"],
        "narration": ("Many voices — Mark says many — told one desperate man to be "
                      "quiet."),
        "must_show": "SCRIPTURE-EXACT: MANY of them, not two or three — a ring of a dozen or more people all hushing one man on the ground.",
        "must_not_show": "the number must read as many; a small group loses v48's word.",
        "scene": (
            "Seen from slightly above: a ring of a dozen or more travellers has closed "
            "in around Bartimaeus where he kneels in the dust at the road's edge, all "
            "of them turned down toward him at once — hands raised in shushing "
            "gestures, fingers pointed, mouths open, heads shaking. He is small at the "
            "bottom of the ring with his face still lifted. The crowd continues to "
            "flow past behind them. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b18", "out": "s18-an-embarrassment.jpeg", "seg": "n3 p3-p4",
        "window": "91.35-104.66", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "PILGRIMS"],
        "narration": ("Understand why: to them, a beggar screaming at a famous rabbi "
                      "was an embarrassment, noise that needed hushing. Respectable "
                      "people, telling a man in the dust that his need was bad manners."),
        "must_show": "the class of it — well-dressed respectable travellers looking down at a filthy man in the dust with distaste, not anger.",
        "must_not_show": "not cartoon villains; ordinary decent people who find him embarrassing, which is worse.",
        "scene": (
            "Two or three well-kept travellers in good clean dark robes stand over "
            "Bartimaeus looking down at him. Their faces are not angry — they are "
            "faintly disgusted and impatient, mouths pulled tight, one glancing away "
            "up the road as if hoping nobody important noticed, another brushing dust "
            "off his sleeve. Below them Bartimaeus kneels filthy in the dirt with his "
            "face lifted toward them. The gap between their clothes and his is plain. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b19", "out": "s19-he-shouted-louder.jpeg", "seg": "n4",
        "window": "105.21-106.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART"],
        "narration": "He shouted louder.",
        "must_show": "everything given to one more shout — head back, body arched, louder than before, straight through the hands trying to quiet him.",
        "must_not_show": "no hesitation and no fear of the crowd anywhere in the frame.",
        "scene": (
            "Very close on Bartimaeus, arched back on his knees with his head thrown "
            "right back and his mouth open wider than before, roaring straight up past "
            "the hands reaching down at him. His whole face is red with effort and "
            "screwed shut, his arms flung wide and low, his chest heaving. A blurred "
            "hand is still coming down toward his shoulder at the frame's edge and he "
            "is ignoring it completely. Hard sun, dust."
        ),
    },
    # ------------------------------------------------ n5 — Jesus stood still ----
    {
        "id": "v2-r012-b20", "out": "s20-and-jesus-stood-still.jpeg", "seg": "n5 p1",
        "window": "107.06-108.36", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "ROAD-JERICHO"],
        "narration": "And Jesus stood still.",
        "must_show": "him stopped dead in the middle of the moving road, head turning back toward the sound, while the procession is still moving around him.",
        "must_not_show": "no halo, glare or rim-light; the crowd around him has NOT stopped yet — he stops first, they pile up after.",
        "scene": (
            "In the middle of the crowded highway Jesus has stopped dead and stands "
            "completely still, his head and shoulders turned back and around toward "
            "the shouting behind him, his face intent. All around him the procession "
            "is still moving forward and people are beginning to bump and jostle "
            "against his stillness, faces turning in confusion. He is the only "
            "motionless thing in the frame. Dust and hard sun. The camera is back far "
            "enough to see him head to sandals in the crowd. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b21", "out": "s21-the-procession-stopped.jpeg", "seg": "n5 p2",
        "window": "108.36-113.95", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "PILGRIMS", "ROAD-JERICHO"],
        "narration": ("The whole procession stopped around him — hundreds of feet going "
                      "quiet in the dust."),
        "must_show": "the whole enormous crowd halted and silent, the dust settling around hundreds of stopped people.",
        "must_not_show": "no halo, glare or rim-light; nobody is still walking — the stop must be total.",
        "scene": (
            "A wide high view of the highway with the entire procession halted. "
            "Hundreds of people stand stopped in the road in every direction, turned "
            "and looking toward one point, and the great cloud of dust they were "
            "kicking up is settling slowly around their legs in the hard sunlight. "
            "Jesus stands still in the middle of them with the disciples close around "
            "him. Nothing in the frame is moving. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r012-b22", "out": "s22-what-he-was-carrying.jpeg", "seg": "n5 p3-p4",
        "window": "113.95-121.64", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD-JERICHO"],
        "narration": ("Remember where this road was taking him: up to Jerusalem, into "
                      "the last week of his life. He was carrying all of that."),
        "must_show": "him standing in the road with the climb to Jerusalem opening away behind him — the weight of where he is going visible on his face.",
        "must_not_show": "no halo, glare or rim-light; no cross and nothing symbolic — the weight is in the face and the road.",
        "scene": (
            "Jesus stands in the stopped road, and beyond his shoulder the highway "
            "climbs away into the bare stony hills toward Jerusalem, long and dusty "
            "and rising. His face carries something heavy and far away for a moment — "
            "the eyes of a man who knows exactly what is at the top of that road — "
            "even as his head is turned back toward the shouting. Hard morning light "
            "on the hills. The camera is back far enough to hold him and the climbing "
            "road. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b23", "out": "s23-one-voice-stopped-him.jpeg", "seg": "n5 p5-p6",
        "window": "121.64-130.74", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BART", "DISCIPLES", "PILGRIMS", "ROAD-JERICHO"],
        "narration": ("And one blind beggar's voice — the voice everyone else was "
                      "trying to shut off — stopped him in the road. He told them: "
                      "call him over."),
        "must_show": "the two ends of it in one frame: Jesus in the road giving the order with his hand out toward the roadside, and far off at the edge the small kneeling beggar.",
        "must_not_show": "no halo, glare or rim-light; Jesus must not have moved toward him yet — he sends others.",
        "scene": (
            "A wide frame holding both ends of the road. In the middle ground Jesus "
            "stands in the halted crowd with one hand lifted and pointing out toward "
            "the roadside, speaking to the men around him — sending them. Far over at "
            "the road's edge, small and low against the wall, Bartimaeus kneels in the "
            "dust with his face still turned up. Between them the parted, staring "
            "crowd. Hard sun and settling dust. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r012-b24", "out": "s24-he-calleth-thee.jpeg", "seg": "s49",
        "window": "131.30-133.67", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "PILGRIMS"],
        "narration": "Be of good comfort, rise; he calleth thee. (Mark 10:49)",
        "must_show": "people crouching to him now — a hand under his elbow, faces close and urgent and suddenly kind.",
        "must_not_show": "do not put Jesus in this frame; the same people who hushed him are the ones helping.",
        "scene": (
            "Two or three travellers have crouched right down to Bartimaeus in the "
            "dust. One has a hand under his elbow lifting, another is close to his ear "
            "with a hand on his shoulder speaking urgently, a third is gesturing back "
            "up the road. Their faces have changed completely — bright, urgent, almost "
            "excited. Bartimaeus's clouded eyes are wide and his mouth is open. Hard "
            "sun and dust. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b25", "out": "s25-the-same-voices.jpeg", "seg": "n6 p1-p2",
        "window": "134.23-143.55", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "PILGRIMS"],
        "narration": ("What happened next is one small verse, and it holds the whole "
                      "man. The same voices that had been hushing him now crowded in "
                      "with: take heart — get up!"),
        "must_show": "THE INVERSE OF b17: the same ring of people around him, but every hand now reaching to HELP him up instead of pushing him down.",
        "must_not_show": "the composition must plainly answer the hushing frame — same ring, opposite gesture.",
        "scene": (
            "Seen from slightly above again: the same ring of a dozen travellers has "
            "closed around Bartimaeus where he kneels — but now every hand is reaching "
            "DOWN TO LIFT HIM, palms up and open under his arms and elbows, faces "
            "bright and mouths open calling encouragement, several of them beckoning "
            "back up the road. He is coming up off his knees in the middle of them. "
            "Hard sun, settling dust. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r012-b26", "out": "s26-he-is-calling-for-you.jpeg", "seg": "n6 p3",
        "window": "143.55-145.36", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART"],
        "narration": "He is calling for you.",
        "must_show": "close on his face as the words arrive — disbelief cracking open into something enormous.",
        "must_not_show": "do not put Jesus in this frame.",
        "scene": (
            "Very close on Bartimaeus's face. His clouded eyes are wide and streaming "
            "at the corners, his mouth has come open, and his whole weathered face is "
            "breaking apart with disbelief turning into joy — the look of a man who "
            "has just been told the one thing he never expected to hear. Dust on his "
            "cheeks, hard sunlight across him."
        ),
    },
    # ---------------------------------------------------- n7 — the cloak ----
    {
        "id": "v2-r012-b27", "out": "s27-one-small-verse.jpeg", "seg": "n7 p1",
        "window": "145.95-150.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART", "CLOAK"],
        "narration": ("What happened next is one small verse, and it holds the whole "
                      "man."),
        "must_show": "his hands finding and gathering the cloak off his lap — the object about to be thrown away, held one last time.",
        "must_not_show": "he has not thrown it yet; this is the grip before the release.",
        "scene": (
            "Close on Bartimaeus's rough hands closing into the heavy dark russet "
            "cloak bunched across his lap, gathering fistfuls of the worn mended wool. "
            "A few small coins are still lying in its folds. His knuckles are white "
            "and the cloth is dragged tight in his grip. Hard sunlight across the wool "
            "and the dust on his wrists. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r012-b28", "out": "s28-he-threw-off-his-cloak.jpeg", "seg": "n7 p2",
        "window": "150.11-153.32", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "CLOAK", "ROAD-JERICHO"],
        "narration": "He threw off his cloak, jumped up, and came.",
        "must_show": "THE THROW caught mid-air — the cloak flung back and away behind him, coins scattering out of it, as he comes up off the ground.",
        "must_not_show": "the cloak must be plainly LEAVING him, airborne and behind — from this frame on it is never on his shoulders again.",
        "scene": (
            "Caught mid-movement: Bartimaeus is surging up off his knees and the heavy "
            "dark russet cloak is flying backwards away from him through the air, "
            "spread open and turning, small coins scattering out of its folds and "
            "spinning in the sunlight. His arms are still extended from the throw and "
            "his body is already twisting forward toward the road. Dust bursts off the "
            "ground under his feet. The camera is back far enough to hold him and the "
            "airborne cloak. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b29", "out": "s29-a-beggars-entire-world.jpeg", "seg": "n7 p3",
        "window": "153.32-161.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["CLOAK"],
        "narration": ("That cloak was a beggar's entire world — his coat, his bed at "
                      "night, the very thing he spread out to catch the coins he lived "
                      "on."),
        "must_show": "the cloak alone on the ground where it landed, coins scattered around it in the dust — everything he owned, lying in the road.",
        "must_not_show": "no people in this frame at all; the abandoned object is the picture.",
        "scene": (
            "The heavy dark russet cloak lies crumpled and spread where it fell in the "
            "dust of the roadside, its mended folds and frayed corners thrown open, "
            "with half a dozen small dull coins scattered around and half buried in "
            "the dirt beside it. Hard sunlight rakes across the worn wool and the "
            "trodden ground. There is not a single person in the frame. It is "
            "everything a man owned, lying in a road."
        ),
    },
    {
        "id": "v2-r012-b30", "out": "s30-may-never-find-it-again.jpeg", "seg": "n7 p4",
        "window": "161.92-166.27", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "CLOAK", "PILGRIMS"],
        "narration": ("A blind man who throws his cloak behind him may never find it "
                      "again."),
        "must_show": "the distance already opening: the cloak small in the dust behind him while he moves away from it, unable to see where it fell.",
        "must_not_show": "he does not look back and could not find it if he did; nobody picks it up.",
        "scene": (
            "A frame holding both: in the near ground the abandoned cloak lies "
            "crumpled in the dust with its scattered coins, and beyond it Bartimaeus "
            "is already several paces away and moving off, his back to it, hands "
            "reaching forward into the crowd. Between them is nothing but trodden "
            "ground and the feet of the surrounding people. He has no way of knowing "
            "where it is. Hard sun and dust. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r012-b31", "out": "s31-he-threw-it-anyway.jpeg", "seg": "n7 p5-p6",
        "window": "166.27-173.07", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART"],
        "narration": ("He threw it anyway, coins and all. He spent everything he owned "
                      "on the chance that the shout had been heard."),
        "must_show": "his face going forward — no backward glance, no hesitation, nothing held back.",
        "must_not_show": "no regret and no calculation anywhere in the face.",
        "scene": (
            "Close on Bartimaeus's face and shoulders as he pushes forward, his chin "
            "up and his blank clouded eyes aimed straight ahead, his mouth set, his "
            "hands out in front of him feeling the way. There is not a trace of "
            "hesitation or backward thought in his expression — a man who has spent "
            "everything and is not thinking about it. Dust and hard light around him."
        ),
    },
    # ------------------------------------------------- n8 / j1 — the question ----
    {
        "id": "v2-r012-b32", "out": "s32-a-corridor-of-staring-people.jpeg", "seg": "n8 p1",
        "window": "173.69-181.51", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BART", "PILGRIMS", "ROAD-JERICHO"],
        "narration": ("So he came, hands out in front of him, through a corridor of "
                      "staring people, and stood breathing hard in front of the man he "
                      "could not see."),
        "must_show": "the crowd parted into an open lane, Bartimaeus coming down it with both hands out feeling the air, everyone staring, Jesus waiting at the far end.",
        "must_not_show": "no halo, glare or rim-light; nobody is leading him by the hand — he comes himself.",
        "scene": (
            "The crowd has opened into a clear lane down the middle of the road, walled "
            "on both sides by rows of staring silent faces. Down the middle of it "
            "Bartimaeus comes alone, both hands stretched out in front of him feeling "
            "the empty air, his chin up and his clouded eyes aimed at nothing, filthy "
            "and barefoot and without his cloak. At the far end of the lane Jesus "
            "stands waiting for him, watching him come. Hard sun, hanging dust. The "
            "camera is back far enough to hold the whole lane. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b33", "out": "s33-standing-in-front-of-him.jpeg", "seg": "n8 p2",
        "window": "182.02-183.96", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BART"],
        "narration": "And Jesus asked him one question:",
        "must_show": "the two of them face to face and close — the beggar breathing hard, eyes aimed slightly off from Jesus's face because he cannot find it.",
        "must_not_show": "no halo, glare or rim-light; his blind eyes must NOT be looking straight into Jesus's — that detail is the whole poignancy.",
        "scene": (
            "The two men stand face to face, close enough to touch. Bartimaeus is "
            "breathing hard, chest heaving, dust and sweat streaked on his face, his "
            "hands still half raised in front of him — and his clouded eyes are aimed "
            "slightly off to one side of Jesus's face, searching, not quite finding "
            "it. Jesus stands looking directly at him, entirely calm and attentive. "
            "The hushed crowd is soft behind them. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r012-b34", "out": "s34-what-wilt-thou.jpeg", "seg": "j1",
        "window": "184.56-186.41", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("What wilt thou that I should do unto thee? (Mark 10:51)"),
        "must_show": "close on Jesus asking — genuinely asking, unhurried, giving the man the floor.",
        "must_not_show": "no halo, glare or rim-light; nothing knowing or rhetorical in the face — the question is real.",
        "scene": (
            "Close on Jesus's face in the hard morning light, speaking. His head is "
            "inclined slightly toward the man in front of him, his eyes are warm and "
            "steady and completely attentive, and his expression is genuinely "
            "questioning and unhurried — a man who has stopped a road of hundreds to "
            "wait for one person's answer. One hand has come open at his side. The "
            "dusty crowd is soft behind him."
        ),
    },
    # ---------------------------------------------------- n9 — his own voice ----
    {
        "id": "v2-r012-b35", "out": "s35-as-if-it-werent-obvious.jpeg", "seg": "n9 p1-p2",
        "window": "187.97-192.66", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "PILGRIMS"],
        "narration": ("As if it weren't obvious. A blind man, standing in a beggar's "
                      "tunic."),
        "must_show": "the obviousness: him standing there filthy and blind in front of everyone, and a few faces in the crowd exchanging looks at the question.",
        "must_not_show": "do not put Jesus in this frame; the crowd's mild puzzlement carries it.",
        "scene": (
            "Bartimaeus stands alone in the open lane in his filthy patched brown "
            "tunic, barefoot, dust to the knees, his clouded eyes unfocused and his "
            "hands hanging half raised — plainly, obviously blind and plainly a "
            "beggar. In the watching crowd behind him two or three people have glanced "
            "at each other with their brows up at the question that was just asked. "
            "Hard sun and dust. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b36", "out": "s36-he-wanted-the-mans-own-voice.jpeg", "seg": "n9 p3-p4",
        "window": "192.66-203.21", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BART"],
        "narration": ("But he asked anyway — because he wanted the man's own voice, not "
                      "the crowd's guess about him. Nobody had asked Bartimaeus what he "
                      "wanted in a very long time."),
        "must_show": "Jesus waiting, and the beggar's face working — a man who has to reach a long way back to remember how to want something out loud.",
        "must_not_show": "no halo, glare or rim-light; nobody in the crowd answers for him.",
        "scene": (
            "Close on the two of them together. Jesus waits, silent and unhurried, "
            "eyes on him. Bartimaeus's face has changed — his mouth opens and closes "
            "once with nothing coming out, his brows have drawn together and his "
            "clouded eyes are moving, as if he is reaching a very long way back for "
            "something he has not been asked in years. His hands have come half open "
            "in front of him. Hard sun. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r012-b37", "out": "s37-i-want-to-see.jpeg", "seg": "n9 p5",
        "window": "203.21-208.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART"],
        "narration": "His answer came out in a breath: Rabbi — I want to see.",
        "must_show": "close on his face saying it — everything he has, said quietly, in one breath.",
        "must_not_show": "not shouted; after all that noise this comes out small; do not put Jesus in this frame.",
        "scene": (
            "Very close on Bartimaeus's face as he answers. His mouth is barely open "
            "on the words, his chin has come down, and his clouded eyes are wet and "
            "aimed at nothing — the whole ferocity of the shouting gone, replaced by "
            "something small and naked and quiet. A tear has cut a clean line through "
            "the dust on his cheek. Hard sunlight across him."
        ),
    },
    {
        "id": "v2-r012-b38", "out": "s38-that-i-might-receive-my-sight.jpeg", "seg": "s51",
        "window": "209.16-211.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART"],
        "narration": "Lord, that I might receive my sight. (Mark 10:51)",
        "must_show": "his hands having come up toward his own clouded eyes as he says it — naming the thing.",
        "must_not_show": "do not put Jesus in this frame; his eyes are still clouded here.",
        "scene": (
            "Close on Bartimaeus, both rough hands come up open near his own face, "
            "fingertips almost touching his temples, as he says what he wants. His "
            "clouded grey eyes are open and unfocused between his raised hands and his "
            "mouth is still shaping the words. Dust, sunlight, and the blurred silent "
            "crowd behind. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r012-b39", "out": "s39-thy-faith-hath-made-thee-whole.jpeg", "seg": "j2",
        "window": "212.81-215.42", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Go thy way; thy faith hath made thee whole. (Mark 10:52)"),
        "must_show": "close on Jesus saying it — warm and glad, one hand open, and no touch: this healing is done with words only.",
        "must_not_show": "no halo, glare or rim-light; NO hand on the man's eyes and nothing supernatural in the air — Mark records no touch here.",
        "scene": (
            "Close on Jesus's face and one open hand, speaking. His expression is warm "
            "and openly glad, eyes bright and steady, the beginning of a smile at his "
            "mouth. His hand is open and lifted a little but is NOT touching anything "
            "— it stays in the air between them. Nothing is happening in the air. Hard "
            "morning light and the hushed dusty crowd behind him. His hand has five "
            "fingers."
        ),
    },
    # --------------------------------------------------- n10 — he saw ----
    {
        "id": "v2-r012-b40", "out": "s40-and-immediately-he-saw.jpeg", "seg": "n10 p1",
        "window": "216.92-219.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["BART"],
        "narration": "And immediately, Mark says, he saw.",
        "must_show": "⚠️ THE TURN: very close on his eyes, now CLEAR and dark and FOCUSED for the first time — the clouding gone.",
        "must_not_show": "no light coming out of his eyes and nothing supernatural — just clear healthy eyes where clouded ones were; do not put Jesus in this frame.",
        "scene": (
            "Extremely close on Bartimaeus's eyes and the upper half of his face. The "
            "grey clouding is GONE — both eyes are clear, dark brown, wet and wide "
            "open, and for the first time they are FOCUSED, pinned on something "
            "directly in front of him. The skin around them is crumpling with shock. "
            "Nothing is coming out of them and there is no light on them but ordinary "
            "hard morning sun. Dust on his lashes."
        ),
    },
    {
        "id": "v2-r012-b41", "out": "s41-daylight-on-the-road-ahead.jpeg", "seg": "n10 p2",
        "window": "219.81-227.79", "wide": True, "jesus": False, "ref": False,
        "locks": ["BART", "ROAD-JERICHO", "PILGRIMS"],
        "narration": ("The clouds in his eyes cleared like silt settling out of water, "
                      "and the first thing those new eyes ever held was daylight on the "
                      "road ahead."),
        "must_show": "what he is seeing — the bright dusty road, the hills, the crowd — with him in frame staring at it, overwhelmed.",
        "must_not_show": "do not put Jesus in this frame; no glare or halo — ordinary daylight is the miracle here.",
        "scene": (
            "Bartimaeus stands in the open lane with his clear focused eyes wide and "
            "moving, taking in the world — and around and beyond him the road opens "
            "out in hard bright daylight: the pale dusty highway climbing into the "
            "stony hills, the date palms, the hundreds of staring faces, the enormous "
            "washed sky. His face is stunned and streaming. The camera is back far "
            "enough to hold him and the sunlit road he is looking at. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b42", "out": "s42-you-are-free.jpeg", "seg": "n10 p3-p4",
        "window": "227.79-235.12", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BART"],
        "narration": ("Notice what Jesus told him: your trust did this — and you are "
                      "free. Free to go anywhere."),
        "must_show": "THE PAYOFF OF b33: the two of them face to face again, and now his eyes are locked directly on Jesus's — he has finally found the face.",
        "must_not_show": "no halo, glare or rim-light; nobody is holding him or directing him — Jesus is releasing him, not recruiting him.",
        "scene": (
            "The two men face to face again, close, exactly as before — but now "
            "Bartimaeus's clear dark eyes are locked directly and unmistakably onto "
            "Jesus's face, seeing him, and his own face is coming apart with it. "
            "Jesus is looking back at him with warm open gladness, one hand lifted "
            "loosely toward the open road in a gesture of release rather than "
            "invitation. Nobody is touching him. Hard sun and dust. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    # --------------------------------------------------- n11 — he followed ----
    {
        "id": "v2-r012-b43", "out": "s43-he-picked-his-road.jpeg", "seg": "n11 p1-p2",
        "window": "235.70-246.11", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BART", "CLOAK", "ROAD-JERICHO", "PILGRIMS"],
        "narration": ("And here is the ending Mark wants you to catch. Free to go "
                      "anywhere, with brand new eyes and no cloak to go back for, he "
                      "picked his road — the one Jesus was walking."),
        "must_show": "the choice, visible: the open road back to Jericho behind him with his cloak still lying in the dust on it, and him turning instead toward the climb where Jesus is going.",
        "must_not_show": "no halo, glare or rim-light; he must NOT be going back for the cloak — leaving it is the point.",
        "scene": (
            "A wide frame with both roads in it. Behind Bartimaeus the highway runs "
            "back down toward Jericho and the green oasis, and the crumpled dark "
            "russet cloak still lies abandoned in the dust of it with its scattered "
            "coins. He has turned his back on all of that and is stepping the other "
            "way, toward the climb into the stony hills where Jesus and the crowd are "
            "already moving off. His clear eyes are on the road ahead, not behind. "
            "Hard sun. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r012-b44", "out": "s44-in-the-middle-of-the-procession.jpeg", "seg": "n11 p3-p4",
        "window": "246.11-259.01", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BART", "PILGRIMS", "ROAD-JERICHO"],
        "narration": ("He followed him, up the climb toward Jerusalem, staring at "
                      "everything: the hills, the faces, his own two hands. The man who "
                      "had been told to keep quiet walked in the middle of the "
                      "procession that had hushed him."),
        "must_show": "the closing frame: him walking IN the middle of the crowd — not at its edge — staring at his own open hands, with Jesus just ahead and the climb to Jerusalem beyond.",
        "must_not_show": "no halo, glare or rim-light; he must NOT be at the roadside or trailing behind — being inside the procession is the ending.",
        "scene": (
            "The procession is moving again up the climbing highway toward Jerusalem, "
            "and Bartimaeus walks in the middle of it, surrounded on all sides by the "
            "same travellers who tried to silence him — one of them now walking beside "
            "him with a hand on his shoulder. He is holding both of his own rough "
            "hands up in front of his face and staring at them as he walks, his clear "
            "eyes wide, his head turning to take in the hills and the faces around "
            "him. Jesus walks a little ahead in the same crowd. The road climbs into "
            "the bare sunlit hills beyond. The camera is back far enough to hold the "
            "procession head to sandals. Every figure has two arms, two hands and one "
            "head."
        ),
    },
]
