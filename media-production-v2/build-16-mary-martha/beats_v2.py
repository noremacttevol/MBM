#!/usr/bin/env python3
"""V2 beat map — row 16, build-16-mary-martha (Luke 10:38-42).

COVERAGE: 25 pictures against V1's 6, over 139.8 s = 5.6 s/picture.

⚠️ THE TWO WAYS THIS STORY GETS TOLD WRONG, both of which the narration
explicitly forbids, and both of which are the model's defaults:

  1. MARTHA AS A NAG. She is not. She is doing something genuinely honourable —
     the narration says hosting was "a real honor, and a great deal of work" and
     that Jesus "never scolded the serving". Every frame of her must read as a
     competent, generous woman being crushed by her own standards, never as a
     shrew. Her complaint at b13/b14 is a person at the end of her strength, not
     a scold.
  2. JESUS REBUKING HER. He does not. The narration is explicit: "not with a
     scolding, but with her own name, said twice, and said gently", and "He
     never scolded the serving. He worried about the worry." b16 and b17 are
     marked hard-fail if his face reads as correction rather than tenderness.

SCRIPTURE FACTS (Luke 10:38-42 KJV):
  v38  "a certain woman named MARTHA RECEIVED HIM into her house" — it is her
       house and her welcome; she is the host, and glad to be.
  v39  Mary "SAT AT JESUS' FEET, and heard his word" — the posture of a
       disciple, which is the point n6 makes.
  v40  "Martha was CUMBERED about much serving" — burdened, weighed down. She
       says it to HIM, not to her sister: "Lord, dost thou not care..."
  v41  "MARTHA, MARTHA" — the name twice. That doubling is tenderness, and the
       narration says so outright.
  v42  "Mary hath chosen that GOOD PART, which shall NOT BE TAKEN AWAY from her."

THE SISTERS MUST READ AS SISTERS — same colouring and bone structure, clearly
related, but plainly different people: Martha older, broader, capable; Mary
younger, slighter, still. Their locks fix that.

CONTENT-CARE: row 16 is GREEN.

TIME OF DAY: EVENING. The narration says "One evening", so the whole build is
warm interior lamplight and the blue dusk outside the door — small oil lamps,
firelight from the cooking hearth, deep shadow in the corners. No daylight
interiors anywhere in this build.
"""

LOCKS = {
    "MARTHA": (
        "MARTHA LOCK: Martha is the same woman in every shot — about thirty-five, "
        "the older sister, strong-boned and capable, broader through the shoulders, "
        "warm olive-brown skin, dark hair bound back tightly under a practical "
        "DARK-OCHRE headcloth with loose strands stuck to her damp forehead, level "
        "dark brows and a direct, intelligent face. She wears a hard-wearing DEEP "
        "RUSSET-BROWN wool dress with the sleeves pushed back and a work-stained "
        "apron-cloth at her waist (never cream, never white). Her hands are strong "
        "and red from work. Her face is shown clearly and is never shrewish."
    ),
    "MARY": (
        "MARY LOCK: Mary is the same woman in every shot — about twenty-eight, the "
        "younger sister, plainly related to Martha with the same warm olive-brown "
        "skin and the same dark brows, but slighter, narrower-featured and quieter. "
        "Her dark hair is loosely gathered and falling over one shoulder, uncovered. "
        "She wears a soft DUSTY-INDIGO wool dress with a plain sash (never cream, "
        "never white). Her face is shown clearly and is calm and absorbed."
    ),
    "HOUSE": (
        "BETHANY HOUSE LOCK: a comfortable village house of warm honey-coloured "
        "stone — one main room with a beaten earth floor and woven rush mats, a low "
        "cooking hearth with a fire and a hanging pot in one corner, a bread oven, "
        "shelves of clay jars and bowls, a low table with cushions around it, a "
        "doorway open to the blue dusk outside. IT IS EVENING: the room is lit "
        "warmly and unevenly by small clay oil lamps and the low fire, with deep "
        "shadow in the corners and the last blue light in the doorway."
    ),
    "GUESTS": (
        "GUESTS LOCK: the travellers with him are the same six or seven men "
        "throughout — working Galileans between twenty and forty, dusty from the "
        "road, sitting on mats and cushions around the low table. They wear wool "
        "tunics in SATURATED DEEP colours: rust-brown, deep russet, dark olive, "
        "blue-grey and dusty indigo. None wears off-white, ivory or any near-white "
        "cloth. Their faces are shown clearly."
    ),
}

REF = True

BEATS = [
    # ---------------------------------------------------- n1 — the welcome ----
    {
        "id": "v2-r016-b01", "out": "s01-bethany-at-evening.jpeg", "seg": "n1 p1",
        "window": "0.28-3.63", "wide": True, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": "This is the little village of Bethany, just outside Jerusalem.",
        "must_show": "the small village on its hillside at dusk, lamps beginning to show in doorways, Jerusalem's walls distant beyond.",
        "must_not_show": "no people needed; establish the place and the hour.",
        "scene": (
            "A wide view of a small village of honey-coloured stone houses on a "
            "hillside at dusk, olive trees and terraces around it, the sky gone deep "
            "blue with the last light low behind the ridge. Warm orange lamplight is "
            "beginning to show in one or two low doorways. Far off across the valley "
            "the walls and rooftops of Jerusalem stand dark against the last of the "
            "light. Quiet and settling into night."
            " The camera looks down over the terraces from the hillside above and behind the village, so the houses are seen from their backs and roofs and the valley falls away past them; nobody stands near the lens. "
        ),
    },
    {
        "id": "v2-r016-b02", "out": "s02-martha-welcomed-him-in.jpeg", "seg": "n1 p2",
        "window": "3.63-11.76", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "GUESTS", "HOUSE"],
        "narration": ("One evening, Jesus came here to the home of two sisters, Martha "
                      "and Mary, and Martha gladly welcomed him in."),
        "must_show": "⚠️ MARTHA GLAD: her in the lamplit doorway with both arms out in welcome, genuinely delighted, ushering him and the travellers in.",
        "must_not_show": "no halo, glare or rim-light; there must be no strain or resentment on her face here at all — she is happy, and the frame has to establish it.",
        "scene": (
            "Martha stands in the open doorway of the house in the blue dusk with warm "
            "lamplight spilling out around her, both arms opened wide in welcome and "
            "her whole face lit up with genuine delight. Jesus is stepping in past her "
            "with the dusty travellers coming up the path behind him, and she is "
            "already turning to usher the next one through. There is nothing strained "
            "about her at all. The camera is back far enough to hold the doorway and "
            "the arriving group. Every figure has two arms, two hands and one head."
            " THE CAMERA STANDS BEHIND THE ARRIVING TRAVELLERS ON THE PATH AND SHOOTS PAST THEM toward the doorway: their backs and shoulders fill the near frame, dark against the lamplight, and not one of their faces is turned toward the lens; Martha in the doorway is in three-quarter and her eyes go to the men in front of her, exiting the frame past the camera's left. "
        ),
    },
    # -------------------------------------------------- n2 — the honour of it ----
    {
        "id": "v2-r016-b03", "out": "s03-an-honor-and-a-great-deal-of-work.jpeg", "seg": "n2",
        "window": "11.76-20.97", "wide": True, "jesus": False, "ref": False,
        "locks": ["MARTHA", "HOUSE"],
        "narration": ("In that day, hosting a guest like this was a real honor, and a "
                      "great deal of work. There was a meal to cook, water to carry, and "
                      "a whole house to ready. Martha took all of it onto herself."),
        "must_show": "the scale of the job laid out — the hearth going, dough waiting, empty water jars, bowls to fill — and Martha alone in the middle of all of it.",
        "must_not_show": "she is not resentful yet; she is rolling her sleeves up with purpose. Do not put Jesus in this frame.",
        "scene": (
            "The lamplit kitchen end of the room, and there is a great deal to do: a "
            "pot hanging over the low fire, a slab of dough waiting on the board, two "
            "big empty water jars by the door, a stack of bowls, greens and fish "
            "unprepared on the table, cushions still to be laid out. Martha stands in "
            "the middle of it alone, pushing her sleeves back up her forearms with her "
            "chin set — sizing up the work and taking it on. Firelight and lamplight "
            "across her. The camera is back far enough to hold her and the whole task. "
            "She has two arms, two hands and one head."
            " The camera stands behind Martha's shoulder and a little to the side, so her back and three-quarter profile are in the near frame and the whole task lies out beyond her; her gaze travels down and left across the work, well past the lens. "
        ),
    },
    {
        "id": "v2-r016-b03b", "out": "s03b-she-took-it-all-on-herself.jpeg", "seg": "n2 p3",
        "window": "20.97-25.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA", "HOUSE"],
        "narration": "Martha took all of it onto herself.",
        "must_show": "Martha alone with the weight of the whole evening on her — both water jars hoisted, nobody helping her, the doorway to the crowded main room behind her.",
        "must_not_show": "no other worker, servant, child or helper anywhere in the frame; no resentment yet, only resolve; do not put Jesus in this frame.",
        "scene": (
            "A waist-up shot of Martha in the lamplit kitchen end of the room, "
            "photographed from her side so her face is in three-quarter profile and her "
            "eyes travel down and past the camera to the load in her arms. She carries a "
            "heavy clay water jar braced against her hip with one arm and steadies a "
            "second on the shelf with the other, shoulders taking the weight, jaw set, "
            "damp strands stuck to her forehead. Behind her, softly out of focus through "
            "the doorway, the warm light of the main room where the guests are. Nobody "
            "else is in the kitchen with her — she is doing all of it alone. Low warm "
            "firelight from below and one small oil lamp above. She has two arms, two "
            "hands and one head."
        ),
    },
    # ------------------------------------------------- n3 — she threw herself in ----
    {
        "id": "v2-r016-b04", "out": "s04-she-threw-herself-in.jpeg", "seg": "n3 p1",
        "window": "25.14-27.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA"],
        "narration": "So Martha threw herself into the serving.",
        "must_show": "her hands working fast and well — competent, practised, good at this.",
        "must_not_show": "no faces needed; the competence is the point.",
        "scene": (
            "Close on Martha's strong reddened hands working fast in the warm "
            "lamplight — one turning a round of dough over on the board while the "
            "other sweeps flour aside, quick and practised and completely assured. "
            "Flour on her forearms and the edge of her russet sleeve. The firelight "
            "moves across her knuckles. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r016-b05", "out": "s05-moving-without-a-pause.jpeg", "seg": "n3 p2",
        "window": "27.17-36.12", "wide": True, "jesus": False, "ref": False,
        "locks": ["MARTHA", "GUESTS", "HOUSE"],
        "narration": ("Stirring, carrying, cleaning, fixing, moving without a pause, "
                      "giving this guest everything she thought he deserved."),
        "must_show": "Martha in motion across the room — mid-stride with a full water jar on her hip, the room full of half-done tasks around her.",
        "must_not_show": "do not put Jesus in this frame; she must look like she is moving fast, not standing still.",
        "scene": (
            "Martha crosses the lamplit room mid-stride with a heavy full water jar "
            "braced on one hip and a folded cloth over her shoulder, her skirt swinging "
            "with the speed of her. Around her the room is a field of half-finished "
            "work — the pot needing stirring on the fire, bowls half filled on the "
            "table, cushions part laid. The seated travellers are visible in the warm "
            "background listening to someone out of frame. She is the only thing "
            "moving. Every figure has two arms, two hands and one head."
            " The camera stands beside and slightly behind her line of travel, so she crosses the frame in profile moving away from the lens; the seated travellers behind her are seen from behind, and not one face is turned toward the camera. "
        ),
    },
    # ------------------------------------------- n4 — the joy gets buried ----
    {
        "id": "v2-r016-b06", "out": "s06-the-joy-got-buried.jpeg", "seg": "n4 p1",
        "window": "36.12-41.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA"],
        "narration": ("But little by little, the joy of having him there got buried under "
                      "the weight of getting it all just right."),
        "must_show": "the change in her face — the delight from the doorway gone, replaced by tight concentration and a small frown.",
        "must_not_show": "not angry yet; this is the joy draining out, not temper arriving.",
        "scene": (
            "Close on Martha's face in the firelight as she works. The open delight "
            "that was there at the door has gone out of it — her brows have drawn "
            "together, her mouth has gone flat and tight, her eyes are down and fixed "
            "on the task in front of her, and a strand of damp hair has come loose "
            "across her cheek. She is not angry; she is somewhere far inside the work. "
            "Warm uneven lamplight. She has one head."
        ),
    },
    {
        "id": "v2-r016-b07", "out": "s07-winding-tighter.jpeg", "seg": "n4 p2",
        "window": "41.52-47.51", "wide": True, "jesus": False, "ref": False,
        "locks": ["MARTHA", "MARY", "HOUSE"],
        "narration": ("Her hands stayed busy while, inside, she wound tighter and "
                      "tighter."),
        "must_show": "her hands still working while her head is turned — a glance thrown across the room toward her sister, the first crack.",
        "must_not_show": "no glare or venom yet; one short look, and back to the work. Do not put Jesus in this frame.",
        "scene": (
            "Martha stands at the table with her hands still moving over the food, but "
            "her head has turned and she is looking away across the lamplit room "
            "toward the far side where her sister is sitting on the floor. Her jaw has "
            "tightened and her chin is slightly lowered. It is one short look, and her "
            "hands have not stopped. The warm room, the fire and the seated shapes are "
            "between them. Every figure has two arms, two hands and one head."
            " The camera stands behind Martha's shoulder at the table and shoots past her back across the room toward her sister, so we follow her look; the seated men between them are seen from behind, and not one face is turned toward the lens. "
        ),
    },
    # -------------------------------------------------- n5/n6 — Mary's choice ----
    {
        "id": "v2-r016-b08", "out": "s08-a-different-choice.jpeg", "seg": "n5 p1",
        "window": "47.51-50.23", "wide": True, "jesus": False, "ref": False,
        "locks": ["MARY", "HOUSE"],
        "narration": "Her sister Mary had made a completely different choice.",
        "must_show": "Mary on the floor amid the room's unfinished work — sitting still while everything around her waits to be done.",
        "must_not_show": "she is not lazy or smug; she is absorbed. Do not put Jesus in this frame.",
        "scene": (
            "Mary sits on a rush mat on the floor in the warm lamplight, her indigo "
            "skirt gathered around her, completely still. Around and behind her the "
            "room's unfinished work is visible — the waiting bowls, the folded "
            "cushions, a cloth dropped over a stool. She is not looking at any of it. "
            "Her stillness is the only stillness in the room. The camera is back far "
            "enough to hold her and the waiting work. She has two arms, two hands and "
            "one head."
            " The camera stands behind and to the side of the seated men and shoots past their backs toward Mary; she is in three-quarter with her gaze up and off past the left edge, and not one face is turned toward the lens. "
        ),
    },
    {
        "id": "v2-r016-b09", "out": "s09-at-his-feet-listening.jpeg", "seg": "n5 p2",
        "window": "50.23-57.32", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARY", "GUESTS", "HOUSE"],
        "narration": ("She sat down on the floor at Jesus's feet, and she simply "
                      "listened to every word he said."),
        "must_show": "SCRIPTURE-EXACT (v39): Mary seated on the floor AT HIS FEET, closer than anyone, face turned up and completely absorbed.",
        "must_not_show": "no halo, glare or rim-light; she is on the FLOOR at his feet, not on a cushion or bench beside him.",
        "scene": (
            "Jesus sits low on a cushion by the wall talking, one hand open, and Mary "
            "is seated on the floor right at his feet, closer in than anyone else in "
            "the room, her hands in her lap and her face turned up to him, entirely "
            "absorbed. The other travellers sit further back around the low table "
            "listening. Warm lamplight and firelight across all of them, deep shadow "
            "behind. The camera is back far enough to hold Jesus, Mary and the seated "
            "group. Every figure has two arms, two hands and one head."
            " The camera stands behind the outer ring of seated travellers and shoots past their backs and shoulders toward Jesus and Mary; Mary is seen from behind and to the side, Jesus is in three-quarter with his eyes on the men he is speaking to, and not one face is turned toward the lens. "
        ),
    },
    {
        "id": "v2-r016-b10", "out": "s10-the-place-a-student-sat.jpeg", "seg": "n6 p1-p2",
        "window": "57.32-66.06", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARY", "GUESTS"],
        "narration": ("Back then, sitting at a teacher's feet was the place a student "
                      "sat, and it was not a place people expected a woman to take. Mary "
                      "took it anyway."),
        "must_show": "her position among the men made visible — Mary in the disciple's place on the floor, the male students around her, a couple registering it.",
        "must_not_show": "no halo, glare or rim-light; nobody is objecting or moving her — a glance or two, nothing more.",
        "scene": (
            "The lamplit room from a little back: Mary sits on the floor at Jesus's "
            "feet in the student's place, and the circle of men sits around and behind "
            "her in exactly the same posture. One or two of them have their eyes on "
            "her rather than on Jesus, a fraction thrown by where she has put herself, "
            "but nobody has moved and nobody is objecting. She is not looking at any "
            "of them. Warm firelight, deep shadows. Every figure has two arms, two "
            "hands and one head."
            " The camera stands behind the circle of seated men and shoots past their backs toward Jesus; the men are seen from behind or in profile, Mary from behind in three-quarter, and not one face is turned toward the lens. "
        ),
    },
    {
        "id": "v2-r016-b11", "out": "s11-nearer-than-anything.jpeg", "seg": "n6 p3",
        "window": "66.06-71.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": "She wanted to be near him more than anything else that night.",
        "must_show": "close on Mary's face — lit warm, utterly still, everything else in the world switched off.",
        "must_not_show": "no piety-performance; simple absorbed attention. Do not put Jesus in this frame.",
        "scene": (
            "Close on Mary's face turned upward in the warm lamplight, completely "
            "still. Her lips are slightly parted, her dark eyes are wide and steady "
            "and fixed on something above and beyond the frame, and every line of her "
            "face has gone soft with attention. A loose strand of dark hair lies "
            "across her shoulder. There is no performance in it at all. She has one "
            "head."
        ),
    },
    # ---------------------------------------------- n7/n8 — the breaking point ----
    {
        "id": "v2-r016-b12", "out": "s12-worn-thin.jpeg", "seg": "n7 p1",
        "window": "71.27-75.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA"],
        "narration": "Meanwhile Martha, worn thin, finally reached her breaking point.",
        "must_show": "close on Martha stopped for the first time — both hands braced on the table, head down, exhausted.",
        "must_not_show": "⚠️ sympathy, not shrewishness — this is a woman at the end of her strength; do not put Jesus in this frame.",
        "scene": (
            "Close on Martha stopped dead at the table for the first time all evening, "
            "both reddened hands braced flat on the wood and her head hanging down "
            "between her shoulders, chest rising. Damp hair has come loose all around "
            "her face and there is flour and sweat on her forearms. It is the posture "
            "of someone who has run out. Firelight from one side. She has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r016-b13", "out": "s13-in-front-of-everyone.jpeg", "seg": "n7 p2",
        "window": "75.23-83.50", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "MARY", "GUESTS", "HOUSE"],
        "narration": ("She stopped, looked at her sister just sitting there, and said out "
                      "loud, in front of everyone, exactly what she was feeling."),
        "must_show": "Martha crossing the room and speaking into the middle of the gathering — the whole seated circle turning to her.",
        "must_not_show": "no halo, glare or rim-light; she is not shrieking — she is a tired person who has stopped being able to hold it in.",
        "scene": (
            "Martha has come out of the kitchen end into the middle of the lamplit "
            "room with the cloth still in one hand, and she is speaking. Her other "
            "hand is out toward her sister on the floor and her face is flushed and "
            "tight with exhaustion rather than rage. All around the low table the "
            "seated men have turned toward her, conversation stopped. Jesus has turned "
            "his head to her too. Mary is looking up. Warm firelight, deep shadows. "
            " The camera is back far enough to hold the whole room. Every figure has "
            "two arms, two hands and one head."
            " The camera stands behind and beside the seated men and shoots past their backs and turned heads toward Martha; she is in three-quarter, her gaze going down to her sister and out past the lower left of the frame, and not one face is turned toward the lens. "
        ),
    },
    {
        "id": "v2-r016-b14", "out": "s14-dont-you-care.jpeg", "seg": "n8 p1",
        "window": "83.50-87.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA"],
        "narration": ("Lord, don't you care that my sister has left me to do all of this "
                      "work by myself?"),
        "must_show": "close on Martha's face asking it — hurt showing through the anger, eyes bright, on the edge of tears.",
        "must_not_show": "⚠️ NOT a shrew. The hurt has to be plainly underneath the complaint. Do not put Jesus in this frame.",
        "scene": (
            "Close on Martha's face in the firelight as she says it. Her jaw is tight "
            "and her brows are down, but her eyes are bright and swimming and her chin "
            "has the faintest tremble in it — the anger is sitting on top of something "
            "much more like being hurt and unseen. Damp hair sticks to her temple. She "
            "has one head."
        ),
    },
    {
        "id": "v2-r016-b15", "out": "s15-tell-her-to-help-me.jpeg", "seg": "n8 p2",
        "window": "87.98-91.32", "wide": True, "jesus": False, "ref": False,
        "locks": ["MARTHA", "MARY", "GUESTS"],
        "narration": "Tell her to get up and help me.",
        "must_show": "her hand pointing at her sister and the room caught in it — Mary looking up from the floor, the guests frozen and awkward.",
        "must_not_show": "do not put Jesus in this frame; nobody knows where to look, which is the truth of the moment.",
        "scene": (
            "Martha's arm is extended and her finger is pointing down at Mary on the "
            "floor. Mary has turned and is looking up at her sister with her mouth "
            "slightly open, saying nothing. Around them the seated travellers have "
            "gone rigid with awkwardness — one is staring hard at the floor, another "
            "has become very interested in his cup, a third is glancing sideways at "
            "his neighbour. Nobody knows where to look. Warm lamplight. Every figure "
            "has two arms, two hands and one head."
            " The camera stands behind Martha's shoulder and shoots past her back and her pointing arm down toward Mary; the travellers are seen in profile and from behind, and not one face is turned toward the lens. "
        ),
    },
    # ---------------------------------------------------- n9 / j1 — her name ----
    {
        "id": "v2-r016-b16", "out": "s16-the-room-went-quiet.jpeg", "seg": "n9 p1",
        "window": "91.32-92.76", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "MARY", "GUESTS", "HOUSE"],
        "narration": "The whole room went quiet.",
        "must_show": "total stillness in the lamplit room — nobody moving, the fire the only thing alive in the frame.",
        "must_not_show": "no halo, glare or rim-light; nobody has spoken yet.",
        "scene": (
            "The whole lamplit room has gone completely still. Martha stands with her "
            "arm still half out, Mary sits on the floor looking up, the travellers are "
            "frozen around the low table, and not one person is moving or speaking. "
            "The only movement anywhere in the frame is the low fire in the hearth. "
            "Jesus is turned toward Martha. Deep shadow in the corners, warm uneven "
            "light. The camera holds the whole room. Every figure has two arms, two "
            "hands and one head."
            " The camera stands well back behind the seated travellers and shoots past their backs across the still room; every person is seen from behind, in profile or in three-quarter, and not one face is turned toward the lens. "
        ),
    },
    {
        "id": "v2-r016-b17", "out": "s17-not-a-scolding.jpeg", "seg": "n9 p2",
        "window": "92.76-100.53", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("And Jesus answered her, not with a scolding, but with her own "
                      "name, said twice, and said gently."),
        "must_show": "⚠️ HARD FAIL IF WRONG. Close on Jesus's face: warm, fond, unhurried, looking up at her with real affection. This is tenderness, not correction.",
        "must_not_show": "NOT stern, NOT disappointed, NOT patient-with-a-difficult-person, NOT a raised eyebrow. The narration says outright he did not scold her. If this face reads as correction the video's whole point is lost. No halo or rim-light.",
        "scene": (
            "Close on Jesus's face in the warm lamplight, looking up at the woman "
            "standing over him. His expression is completely fond — his eyes soft and "
            "crinkled slightly at the corners, his brows lifted gently in the middle, "
            "the beginning of a warm affectionate smile at his mouth, his head tilted "
            "a little toward her. He is about to say somebody's name the way you say "
            "the name of a person you love. There is no correction anywhere in it. "
            "Firelight moving across his face."
        ),
    },
    {
        "id": "v2-r016-b18", "out": "s18-martha-martha.jpeg", "seg": "j1 a",
        "window": "100.53-106.13", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARTHA"],
        "narration": ("Martha, Martha, thou art careful and troubled about many things: "
                      "(Luke 10:41)"),
        "must_show": "the two of them — him speaking her name up at her, and the tightness beginning to come out of her face as she hears it.",
        "must_not_show": "no halo, glare or rim-light; she must not look scolded — she looks caught, and then disarmed.",
        "scene": (
            "Jesus, still seated low, has turned fully to Martha and is speaking up at "
            "her, one hand come open toward her. Martha stands over him with the cloth "
            "hanging forgotten in her hand, and her face has begun to change — the "
            "tightness going out of her jaw, her pointing arm coming down, her eyes "
            "widening slightly. She looks disarmed rather than corrected. Warm "
            "lamplight between them. The camera is back far enough to hold both. Every "
            "figure has two arms, two hands and one head."
            " The camera stands low behind and beside Martha, shooting past her back and hip toward Jesus seated below her; his face is in three-quarter with his eyes up on her and travelling out past the camera's right, and not one face is turned toward the lens. "
        ),
    },
    {
        "id": "v2-r016-b19", "out": "s19-that-good-part.jpeg", "seg": "j1 b",
        "window": "106.13-115.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "MARY"],
        "narration": ("But one thing is needful: and Mary hath chosen that good part, "
                      "which shall not be taken away from her. (Luke 10:42)"),
        "must_show": "his open hand indicating Mary at his feet while his eyes stay on Martha — naming one sister while looking at the other.",
        "must_not_show": "no halo, glare or rim-light; Mary must not look triumphant, and Martha must not look shamed.",
        "scene": (
            "Jesus's near hand has turned open toward Mary seated on the floor beside "
            "him — but his face and his eyes are still turned up to Martha, warm and "
            "steady on her. Mary is looking down, not triumphant at all, faintly "
            "uncomfortable at being named. Martha's face is working as she takes it "
            "in. Warm firelight, the quiet room behind. The camera holds all three. "
            "Every figure has two arms, two hands and one head."
            " The camera stands behind Mary's shoulder and shoots past her back toward Jesus and, beyond him, Martha; the faces are in three-quarter and every gaze travels between the people or past the lens, never into it. "
        ),
    },
    # ---------------------------------------------- n10 — what troubled him ----
    {
        "id": "v2-r016-b20", "out": "s20-he-never-scolded-the-serving.jpeg", "seg": "n10 p1",
        "window": "115.04-119.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA"],
        "narration": ("He did not scold her for serving, and he was never upset that she "
                      "worked so hard."),
        "must_show": "close on Martha's working hands, still floury, held loosely now — the work itself is honoured, not criticised.",
        "must_not_show": "nothing negative about the hands or the work; do not put Jesus in this frame.",
        "scene": (
            "Close on Martha's two strong reddened hands, hanging loosely open in front "
            "of her now, the cloth slipped between her fingers, flour still on the "
            "knuckles and along one forearm. They are good hands and they have worked "
            "hard all evening. Warm firelight across them. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r016-b21", "out": "s21-the-worry-underneath.jpeg", "seg": "n10 p2",
        "window": "119.53-125.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA"],
        "narration": ("What troubled him was the worry underneath it, the anxiety that "
                      "was pulling her apart."),
        "must_show": "close on Martha's face as the defence gives way — the exhaustion and the fear of not being enough coming to the surface.",
        "must_not_show": "do not put Jesus in this frame; not sobbing — the first crack, not the flood.",
        "scene": (
            "Close on Martha's face as everything holding it together gives way. Her "
            "brows have come up in the middle, her mouth has softened out of its hard "
            "line, and her eyes have filled — and underneath the exhaustion there is "
            "something frightened and very tired, the look of a person who has been "
            "trying to be enough all evening. One tear has started. Warm firelight. "
            "She has one head."
        ),
    },
    {
        "id": "v2-r016-b22", "out": "s22-not-taken-away.jpeg", "seg": "n10 p3",
        "window": "125.11-132.94", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARY"],
        "narration": ("And the quiet thing Mary had chosen, just being with him, he "
                      "promised no one would ever take away from her."),
        "must_show": "Mary back in her place at his feet, unmoved and unmoved-on — the thing she chose left exactly where it was.",
        "must_not_show": "no halo, glare or rim-light; nobody has made her get up.",
        "scene": (
            "Mary is still seated on the floor at Jesus's feet exactly where she was, "
            "her hands in her lap and her face turned up, and nobody has made her move. "
            "Jesus sits above her, one hand resting easily on his knee, talking on. The "
            "warm lamplight holds the two of them in a small quiet pocket of the room. "
            "Nothing has been taken from her. The camera is back far enough to hold "
            "both. Every figure has two arms, two hands and one head."
            " The camera stands behind and to the side of the seated travellers and shoots past their backs toward the two of them; Mary is seen from behind in three-quarter, Jesus in profile, and not one face is turned toward the lens. "
        ),
    },
    # ------------------------------------------------- n11/n12 — the point ----
    {
        "id": "v2-r016-b23", "out": "s23-not-picking-one-sister.jpeg", "seg": "n11 p1-p2",
        "window": "132.94-141.66", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "MARY"],
        "narration": ("He was not picking one sister over the other. He was telling a "
                      "woman he loved that she did not have to earn her place near him "
                      "by working herself ragged."),
        "must_show": "⚠️ his hand reaching UP to Martha — inviting her down, not sending her away; both sisters in frame and neither preferred.",
        "must_not_show": "no halo, glare or rim-light; Mary is not being held up as the better one — the gesture is toward MARTHA.",
        "scene": (
            "Jesus, still seated low, has stretched his near hand UP and open toward "
            "Martha where she stands — plainly inviting her to come down and sit, not "
            "dismissing her. Mary sits at his feet on one side, and the open floor "
            "beside her is clear and waiting. Martha is looking at the offered hand. "
            "Neither sister is favoured in the framing; both are held equally in the "
            "warm light. The camera is back far enough for all three. Every figure has "
            "two arms, two hands and one head."
            " The camera stands behind and beside Martha, shooting past her back and her lowered arm toward Jesus and Mary below her; the faces are three-quarter and every gaze exits the frame past the lens. "
        ),
    },
    {
        "id": "v2-r016-b24", "out": "s24-she-was-allowed-to-stop.jpeg", "seg": "n11 p3",
        "window": "141.66-148.93", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "MARY", "HOUSE"],
        "narration": ("She was allowed to stop, and sit, and simply be with him, the "
                      "same as her sister."),
        "must_show": "⚠️ THE RESOLUTION: Martha sitting down on the floor beside Mary — the cloth set aside, the work left, both sisters together at his feet.",
        "must_not_show": "no halo, glare or rim-light; she is not collapsing in defeat — she is being let off, and her face should show relief.",
        "scene": (
            "Martha has lowered herself down onto the rush mat beside her sister at "
            "Jesus's feet, her work cloth set down on the floor beside her and her red "
            "hands finally still in her lap. Her face is tired and wet and enormously "
            "relieved. Mary has turned and put a hand over her sister's. Behind them "
            "the unfinished work sits on the table in the shadows and nobody is doing "
            "anything about it. Jesus sits above them talking on. Warm firelight. "
            "Every figure has two arms, two hands and one head."
            " The camera sits low behind Mary's shoulder and shoots past her back toward Martha's three-quarter profile and Jesus beyond them; every gaze travels between the three of them and past the lens, never into it. "
        ),
    },
    {
        "id": "v2-r016-b25", "out": "s25-he-worried-about-the-worry.jpeg", "seg": "n12",
        "window": "148.93-155.79", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "MARY", "GUESTS", "HOUSE"],
        "narration": ("He never scolded the serving. He worried about the worry. That is "
                      "the kind of God he is."),
        "must_show": "the closing frame: the whole warm room settled — both sisters on the floor, the guests listening, the half-done work forgotten in the shadows.",
        "must_not_show": "no halo, glare or rim-light; nothing tense left anywhere in the frame.",
        "scene": (
            "A wide final view of the whole lamplit room, settled and warm. Both "
            "sisters sit together on the floor at Jesus's feet, the travellers are "
            "seated easily around the low table, and Jesus is mid-sentence with one "
            "hand open, every face in the room turned toward him. Off in the shadows "
            "the half-finished food and the empty bowls sit exactly where they were "
            "left, and nobody is looking at them. The fire burns low and the blue "
            "night stands in the open doorway. Every figure has two arms, two hands "
            "and one head."
            " The camera stands behind the seated travellers at the back of the room and shoots past their backs and shoulders toward Jesus; the near figures are seen from behind, and because every face in the room is turned to him, not one is turned toward the lens. "
        ),
    },
]
