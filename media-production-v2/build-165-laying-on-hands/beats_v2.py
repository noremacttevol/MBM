#!/usr/bin/env python3
"""V2 beat map — row 165, build-165-laying-on-hands (Acts 8:14-17).

COVERAGE: 25 pictures over 119.61 s = ~4.8 s/picture (matches rows 161-164
library density; lesson-12 movie coverage).

OPEN CAMERON COMPLAINT: none on file (`v2_outline.py 165` shows no prior
review). Fresh authoring — LEARNING/COST laws in the positive.

SCRIPTURE FACTS (Acts 8 KJV, the passage this row narrates):
  8:14  "Now when the apostles which were at Jerusalem heard that Samaria
        had received the word of God, they sent unto them Peter and John:"  -> kv14
  8:15  "Who, when they were come down, prayed for them, that they might
        receive the Holy Ghost:"                                            -> s15
  8:16  "For as yet he was fallen upon none of them: only they were
        baptized in the name of the Lord Jesus."                            -> s16
  8:17  "Then laid they their hands on them, and they received the
        Holy Ghost."                                                        -> kv17

SPEAKER LAW (the row-39 lesson): this is Luke's narration of the book of Acts —
there is NO Jesus red-letter line in the passage. kv14, s15, s16 and kv17 are
ALL the SCRIPTURE voice (light blue), sitting on the apostles/believers the
verse describes. Jesus is NAMED once ("baptized in the name of the Lord Jesus",
s16) but is NOT present in the Acts 8 scene — so there is NO Jesus beat in this
row at all (jesus=False, ref=False on every beat). Nobody wears cream.

ROW INTENT: RESTORATION-leaning milk, kept strictly inside the Bible's own
frame and NEVER naming any church. The Samaritans truly believed and were truly
baptized — yet the gift of the Holy Ghost still waited on the laying on of hands
by those God had given authority. Order and gift belong together. The close
offers the viewer that same gift by that same pattern.

THE HOLY GHOST IS NEVER EMBODIED (lesson 8 / CONTENT-CARE, treated like the
Father): where the gift is "received" (b18, b19) and where it "came" (b18) it is
warm light coming down from above the top of the frame onto the believers'
upturned faces, and their faces filled with joy — NEVER a dove, NEVER a figure,
NEVER tongues of flame (that is Pentecost, a different event — do not import it
and do not invent a symbol). DRIFT_WORDS glow/halo/rim-light are banned and the
scene text avoids them; nothing rings anyone's head.

CAST (locked): PETER and JOHN are the canonical global cast (attach by token);
same faces and beards in every frame they appear in (BEARD BOARD, lesson 13 —
Peter is a repeat drift offender). The Samaritan BELIEVERS and the Jerusalem
APOSTLES council are build-local people locks. Philip (who first preached and
baptized Samaria) is NOT given a locked face — the baptisms (b02/b12) are shot
on the WATER and the BELIEVER, the baptizer seen only as hands/back, so no extra
face has to be boarded.

MOVIE COVERAGE (lesson 12): the establishing wide is b01 and ONLY b01;
everything else is a single, a two-shot, or an insert. The believing crowd is
always a SMALL group of distinct faces, never a stadium multitude. The laying
on of hands (b16-b19) is covered as a SEQUENCE — the apostles stepping in, the
hands laid on a head, the gift coming, the verse's plain statement — never one
frame standing in for all four.

TWO NEW PLACES (the runner promotes from a first good frame, lesson 11):
SAMARIA-HILL (the Samaritan hill town — most beats) and JERUSALEM-ROOM (the
apostles' council, b06/b07). Steps in QC.md.

TIME OF DAY ARC: the believing, baptizing and joy of Samaria in bright warm
morning; the waiting/"fallen upon none" beats in cooler, held light; the laying
on of hands and the gift coming in strengthening warm light from above; the
close in settled warm daylight.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. PETER and JOHN attach from the global canonical cast
# by token and are NOT redefined here.
LOCKS = {
    "SAMARIA-HILL": (
        "SAMARIA-HILL LOCK: the same Samaritan town in every frame — a modest "
        "first-century hill town of pale dressed-stone and mud-brick houses "
        "with flat roofs, set on a green Samarian hillside with olive terraces "
        "and a low stone water-channel and well below; warm clear daylight. "
        "The same town, houses and hillside throughout — never Jerusalem's "
        "temple, never a walled palace, never a pagan shrine, never a modern "
        "structure."
    ),
    "JERUSALEM-ROOM": (
        "JERUSALEM-ROOM LOCK: the same upper meeting room in Jerusalem in "
        "every frame — a plain first-century room of dressed stone and heavy "
        "timber ceiling beams, a low table, clay oil lamps, woven earth-toned "
        "hangings, a doorway opening onto a stone stair; steady warm lamplight. "
        "The same room throughout — never a synagogue ark, never the temple "
        "sanctuary, never modern glass or metal."
    ),
    "BELIEVERS": (
        "BELIEVERS LOCK: the Samaritan believers — first-century Samaritan men "
        "and women of varied ages, distinct real sun-browned faces, dark hair "
        "and beards of differing lengths, plain earth-toned wool of brown, "
        "rust, ochre, olive and grey (never cream — only Jesus wears cream), "
        "their faces bright and glad with new faith; distinct individuals, "
        "never twinned, never a cloned face, never a uniform crowd."
    ),
    "APOSTLES-JERUSALEM": (
        "APOSTLES-JERUSALEM LOCK: the council of apostles at Jerusalem — a "
        "small group of dignified first-century men of varied ages, some elder "
        "and grey-bearded, some steady and middle-aged, plain earth-toned robes "
        "of brown, umber and undyed grey (never cream); distinct real "
        "individuals gathered in counsel, NOT posed as a named roster, never "
        "twinned, never a cloned face."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r165-b01", "out": "s01-samaria-believes.jpeg", "seg": "n1",
        "window": "0.280-4.500", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARIA-HILL", "BELIEVERS"],
        "narration": "A wave of faith had swept through Samaria.",
        "must_show": "the ONE establishing wide — camera on the hillside behind and to the side of a small Samaritan crowd, looking past their shoulders toward a preacher gesturing before the pale hill town; the crowd's faces turning toward the good news, a real town on a real hillside.",
        "must_not_show": "not a stadium multitude — a modest gathering; no temple or palace; distinct faces, not a uniform crowd; no faces posed to the lens; no panel, border or text.",
        "scene": (
            "A whole town turning: the camera stands on the green Samarian "
            "hillside a little behind and to the side of a modest crowd of "
            "townspeople, looking past their shoulders toward a plain preacher "
            "who gestures before the pale flat-roofed hill town, olive terraces "
            "stepping down to a well below. The people's faces are turned away "
            "from the lens toward him, lit with the first stir of belief. "
            "Distinct sun-browned men and women of ordinary height, each with "
            "two hands and one head, in bright warm morning light."
        ),
    },
    {
        "id": "v2-r165-b02", "out": "s02-baptized-in-water.jpeg", "seg": "n1",
        "window": "4.500-9.310", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS", "SAMARIA-HILL"],
        "narration": (
            "Whole crowds had heard the good news, believed it with glad "
            "hearts, and been baptized in water."
        ),
        "must_show": "a believer being baptized in the town's water channel or pool — the believer waist-deep, eyes closed in gladness, a baptizer's hands steadying him at the moment of immersion; the water and the believer are the subject.",
        "must_not_show": "the baptizer shown only as hands and back, no locked face needed; no font or modern pool — a natural stone water-channel or pool; distinct believer face; no cream; no panel or text.",
        "scene": (
            "Belief carried into the water: a Samaritan believer stands "
            "waist-deep in the town's stone-lined water-channel, head tipped "
            "back and eyes closed in glad surrender, while a baptizer — seen "
            "only as steadying hands and a turned back — lowers him at the "
            "moment of baptism, water sheeting off his shoulders. Other "
            "believers wait at the water's edge, faces bright. Real stone and "
            "real water, warm morning light; the believer is an ordinary man "
            "with two hands and one head."
        ),
    },
    {
        "id": "v2-r165-b03", "out": "s03-joyful-among-them.jpeg", "seg": "n1",
        "window": "9.310-13.468", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": "Something real and joyful was happening among them.",
        "must_show": "a close on two or three Samaritan believers' faces lit with real joy — a woman laughing through tears, a man gripping a friend's arm — genuine gladness spreading among them.",
        "must_not_show": "not a crowd; distinct real faces, never twinned; no cream; no staged smiling at the lens; no panel or text.",
        "scene": (
            "The joy shown up close: two or three Samaritan believers stand "
            "together, a woman laughing with tears bright on her cheeks, a man "
            "gripping his friend's forearm in wordless gladness, another with "
            "eyes shut and face lifted — something real and joyful moving "
            "through them. Their faces are distinct and sun-browned, their wool "
            "earth-toned, the light warm; each has two hands and one head, none "
            "looking at the camera."
        ),
    },
    {
        "id": "v2-r165-b04", "out": "s04-not-a-letter.jpeg", "seg": "n2",
        "window": "13.468-18.190", "wide": False, "jesus": False, "ref": False,
        "locks": ["APOSTLES-JERUSALEM", "JERUSALEM-ROOM"],
        "narration": (
            "And notice their response: they did not simply send a letter of "
            "congratulations."
        ),
        "must_show": "the apostles' council in the Jerusalem room deciding — a small group of grave, considering men leaning in over a low table, a set-aside scroll and lamp; a weightier response than a letter is being formed.",
        "must_not_show": "not a crowd or a full twelve-man roster line-up; distinct faces; no cream; no modern paper or print; no panel or text.",
        "scene": (
            "A response too serious for a note: in the plain Jerusalem upper "
            "room, a small council of apostles leans in around the low table by "
            "lamplight, faces grave and weighing something — a written scroll "
            "set aside on the table as if congratulation were not enough. The "
            "men are distinct, of varied ages, in plain earth-toned robes, each "
            "with two hands and one head. Warm steady lamplight, timber beams "
            "above; nothing legible or modern on the scroll."
        ),
    },
    {
        "id": "v2-r165-b05", "out": "s05-sent-peter-and-john.jpeg", "seg": "n2",
        "window": "18.190-23.789", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN"],
        "narration": (
            "They sent two of their own number, Peter and John, to go down in "
            "person."
        ),
        "must_show": "a two-shot of Peter and John setting out on the road, staffs in hand, turned to descend toward Samaria — the two apostles sent in person, purpose on their faces.",
        "must_not_show": "not a crowd; Peter and John distinct and recognizable, beards consistent; no cream; travel direction clear (setting out/descending); no panel or text.",
        "scene": (
            "The two who were sent: Peter and John stand together at the head of "
            "a descending road, travelling staffs in hand and cloaks gathered, "
            "already turned to go down toward Samaria in the distance below. "
            "Peter is the sturdier, iron-grey-streaked fisherman; John the "
            "younger, clearer-featured apostle — both recognizable, both grave "
            "with purpose, plain earth-toned robes, two hands and one head each, "
            "in warm morning light."
        ),
    },
    {
        "id": "v2-r165-b06", "out": "s06-apostles-heard.jpeg", "seg": "kv14",
        "window": "23.789-28.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["APOSTLES-JERUSALEM", "JERUSALEM-ROOM"],
        "narration": (
            "Now when the apostles which were at Jerusalem heard that Samaria "
            "had received the word of God,"
        ),
        "must_show": "SCRIPTURE-EXACT — the Jerusalem apostles receiving the news: a messenger just arrived at the door of the room, the council turning toward him as they hear that Samaria has received the word of God.",
        "must_not_show": "not a crowd; distinct faces; no cream; no modern objects; no panel or text.",
        "scene": (
            "News reaching the council: a road-dusted messenger stands just "
            "inside the doorway of the Jerusalem upper room, and the small "
            "group of apostles turns toward him from the low table, faces "
            "lifting with the report that Samaria has received the word of God. "
            "Lamplight warm on distinct earth-toned men of varied ages, each "
            "with two hands and one head; timber beams above, nothing modern."
        ),
    },
    {
        "id": "v2-r165-b07", "out": "s07-they-sent-them.jpeg", "seg": "kv14",
        "window": "28.500-33.311", "wide": False, "jesus": False, "ref": False,
        "locks": ["APOSTLES-JERUSALEM", "PETER", "JOHN"],
        "narration": "they sent unto them Peter and John:",
        "must_show": "SCRIPTURE-EXACT — the council sending Peter and John: an elder apostle's hand on Peter's shoulder as Peter and John, staffs in hand, turn toward the doorway to go; the sending made plain.",
        "must_not_show": "Peter and John distinct and recognizable, beards consistent with b05; not a crowd; no cream; no panel or text.",
        "scene": (
            "The sending itself: in the Jerusalem room an elder apostle lays a "
            "hand on Peter's shoulder while Peter and John, staffs gathered and "
            "cloaks on, turn toward the open doorway and the stair beyond — the "
            "two of their number sent to Samaria. Peter the iron-grey-streaked "
            "fisherman and John the younger apostle are clearly the same men as "
            "before; the council behind them are distinct earth-toned figures. "
            "Warm lamplight, two hands and one head each."
        ),
    },
    {
        "id": "v2-r165-b08", "out": "s08-they-prayed.jpeg", "seg": "s15",
        "window": "33.311-39.520", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN", "BELIEVERS", "SAMARIA-HILL"],
        "narration": (
            "Who, when they were come down, prayed for them, that they might "
            "receive the Holy Ghost:"
        ),
        "must_show": "SCRIPTURE-EXACT — Peter and John, now come down to Samaria, standing before the kneeling believers with heads bowed and hands lifted in prayer for them; the apostles interceding, not yet touching.",
        "must_not_show": "no Holy Ghost embodied yet (they are only praying); the believers kneeling and distinct; no cream; Peter and John consistent; no panel or text.",
        "scene": (
            "Prayer before the gift: Peter and John, arrived in the Samaritan "
            "town, stand before a small group of kneeling believers with their "
            "heads bowed and hands lifted, praying earnestly that these people "
            "might receive the Holy Ghost. No hands are laid yet and nothing "
            "comes down yet — only intercession. The believers kneel with "
            "upturned, waiting faces, distinct and earth-toned; the two apostles "
            "recognizable, two hands and one head each, in warm daylight before "
            "the pale hill town."
        ),
    },
    {
        "id": "v2-r165-b09", "out": "s09-already-believed.jpeg", "seg": "n3",
        "window": "39.520-44.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": (
            "And here is the surprising part: even though these people already "
            "believed, and had already been baptized,"
        ),
        "must_show": "a close on a few Samaritan believers, still damp from baptism, faces sincere and expectant — genuine, already-baptized believers, the point being that their faith and baptism were real.",
        "must_not_show": "not a crowd; distinct sincere faces; no cream; no panel or text; nothing yet coming down on them.",
        "scene": (
            "Real believers, plainly sincere: a close grouping of Samaritan "
            "believers, hair and shoulders still damp from the water, their "
            "faces open and honest and expectant — people who have already "
            "believed and already been baptized, waiting for what they have been "
            "told is still to come. Distinct sun-browned faces, earth-toned "
            "wool, warm even light; each has two hands and one head, none "
            "looking at the lens."
        ),
    },
    {
        "id": "v2-r165-b10", "out": "s10-gift-not-yet-come.jpeg", "seg": "n3",
        "window": "44.500-49.582", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": (
            "the gift had not yet come to a single one of them."
        ),
        "must_show": "a believer looking upward and inward, waiting — a plain, held stillness with nothing yet come down; the space above the believers empty and ordinary, the gift not yet arrived.",
        "must_not_show": "NO light coming down and NO Holy Ghost of any kind yet (that is the whole point of this beat); no dove, no flame, no figure; distinct waiting face; no cream; no panel.",
        "scene": (
            "The waiting emphasized by absence: a Samaritan believer looks "
            "upward and inward in the ordinary daylight, quiet and expectant, "
            "and the air above and around him is plain and empty — nothing has "
            "yet come to him or to any of them. The stillness of not-yet is the "
            "subject. A distinct sun-browned face, earth-toned wool, even "
            "natural light with nothing coming down; two hands and one head."
        ),
    },
    {
        "id": "v2-r165-b11", "out": "s11-fallen-upon-none.jpeg", "seg": "s16",
        "window": "49.582-53.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": "For as yet he was fallen upon none of them:",
        "must_show": "SCRIPTURE-EXACT — the small group of believers together, upturned and waiting, and the space above them plainly empty; the Spirit has fallen upon none of them yet.",
        "must_not_show": "NO Spirit, dove, flame, figure or descending light anywhere (the verse says none yet); distinct faces; no cream; no panel or text.",
        "scene": (
            "The verse of the empty air: the small group of Samaritan believers "
            "stand and kneel together with faces upturned and waiting, and the "
            "sky and air above them is entirely plain and empty — the promised "
            "gift has fallen upon none of them yet. Their distinct earth-toned "
            "faces are patient and hopeful in ordinary daylight; nothing "
            "descends. Two hands and one head each, none posed at the lens."
        ),
    },
    {
        "id": "v2-r165-b12", "out": "s12-baptized-in-his-name.jpeg", "seg": "s16",
        "window": "53.500-57.711", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS", "SAMARIA-HILL"],
        "narration": "only they were baptized in the name of the Lord Jesus.",
        "must_show": "SCRIPTURE-EXACT — an insert-scale baptism moment at the town water: a believer rising from the water, the baptizer's hands (only) supporting him, water streaming — they had been truly baptized, and only that, so far.",
        "must_not_show": "the baptizer shown only as hands/back, no locked face; no font or modern pool; no light coming down (only baptism, not yet the gift); no cream; no panel.",
        "scene": (
            "Baptism, and so far only baptism: an insert-scale moment at the "
            "town's stone water-channel — a Samaritan believer rising up out of "
            "the water with eyes still closed, the baptizer's supporting hands "
            "and turned shoulder the only part of him in frame, water streaming "
            "from the believer's hair and beard. Real stone, real water, warm "
            "light; the believer is a distinct ordinary man with two hands and "
            "one head. Nothing yet comes down from above."
        ),
    },
    {
        "id": "v2-r165-b13", "out": "s13-water-not-enough.jpeg", "seg": "n4",
        "window": "57.711-62.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": "So the water alone had not been enough.",
        "must_show": "an insert of a believer's wet hands or dripping hair against the plain empty air — the water real and finished, yet by itself not the whole of what was promised; a held, incomplete quiet.",
        "must_not_show": "no light or Spirit descending; no dove or flame; no cream; no invented symbol; no panel or text.",
        "scene": (
            "Water that was real but not the whole: an insert on a believer's "
            "still-wet hands and dripping hair caught in ordinary daylight, the "
            "water plainly real and the baptism plainly finished — and yet the "
            "air around him stays empty, the moment unfinished, the water alone "
            "not enough for what was promised. A distinct sun-browned man in "
            "earth-toned wool, two whole hands, one head; nothing comes down."
        ),
    },
    {
        "id": "v2-r165-b14", "out": "s14-faith-sincere.jpeg", "seg": "n4",
        "window": "62.000-66.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": (
            "Their faith was sincere and their baptism was real, yet the "
            "promised gift of the Spirit still waited"
        ),
        "must_show": "a close on a sincere believer's waiting face, honest and patient — real faith, real baptism, and a real, held waiting for the gift still to come.",
        "must_not_show": "no Spirit, light or symbol descending; distinct honest face; no cream; no panel or text.",
        "scene": (
            "Sincerity held in the waiting: a close on a Samaritan believer's "
            "honest, patient face, damp from the water, eyes lifted and quiet — "
            "his faith plainly sincere and his baptism plainly real, and still "
            "he waits, because the promised gift of the Spirit has not yet come. "
            "A distinct sun-browned face in earth-toned wool, warm even light, "
            "two hands and one head; the air above stays plain."
        ),
    },
    {
        "id": "v2-r165-b15", "out": "s15-on-the-hands-of-authority.jpeg", "seg": "n4",
        "window": "66.500-71.064", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN"],
        "narration": (
            "on something more — on the hands of those God had given authority."
        ),
        "must_show": "an insert on Peter's and John's hands — weathered, open, ready — held slightly forward, the plain human hands of the men God had given authority, the thing the gift was waiting on.",
        "must_not_show": "no light around the hands, no halo, no glow; ordinary human hands, whole with five fingers; no cream sleeve; no panel or text.",
        "scene": (
            "The answer shown as hands: an insert on the weathered, open hands "
            "of Peter and John held a little forward and ready — plain human "
            "hands, one pair broad and work-scarred, the other steadier and "
            "younger, the hands of the men God had given authority. The gift "
            "was waiting on exactly these. Earth-toned sleeves at the wrists, "
            "the hands whole with five fingers each, in warm ordinary light "
            "with nothing ringing them."
        ),
    },
    {
        "id": "v2-r165-b16", "out": "s16-they-stepped-forward.jpeg", "seg": "n5",
        "window": "71.064-76.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN", "BELIEVERS"],
        "narration": (
            "Then Peter and John did the simple, deliberate thing Luke records "
            "so plainly."
        ),
        "must_show": "a two-shot of Peter and John stepping in toward the kneeling believers, hands beginning to rise toward them — the simple, deliberate act about to happen; unhurried purpose.",
        "must_not_show": "hands not laid yet this beat; Peter and John consistent; no light descending; no cream; distinct kneeling believers; no panel.",
        "scene": (
            "The deliberate act beginning: Peter and John step in close toward "
            "the small group of kneeling Samaritan believers, their hands "
            "beginning to lift toward the nearest bowed heads — the simple, "
            "unhurried thing they had come to do, purpose plain on both faces. "
            "The apostles are recognizable and consistent, the believers "
            "distinct and expectant; warm daylight before the pale town, two "
            "hands and one head each, nothing yet coming down."
        ),
    },
    {
        "id": "v2-r165-b17", "out": "s17-laid-hands-on-each.jpeg", "seg": "n5",
        "window": "76.500-80.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN", "BELIEVERS"],
        "narration": "They laid their hands on each believer.",
        "must_show": "an insert-scale two-shot of the act itself — an apostle's weathered hands laid firmly on a kneeling believer's bowed head, the believer's eyes closed; the plain physical laying on of hands.",
        "must_not_show": "no light or Spirit descending yet in this beat (the gift comes next); ordinary hands, five fingers; no cream; no halo; no panel or text.",
        "scene": (
            "The laying on of hands, close and plain: an apostle's weathered "
            "hands are laid firmly on the bowed head of a kneeling Samaritan "
            "believer, fingers spread over the crown, the believer's eyes shut "
            "and face still — the simple physical act Luke records. The hands "
            "and the head fill the frame; a second apostle's hands reach to the "
            "next believer beside them. Real hands whole with five fingers, "
            "earth-toned sleeves, warm daylight; nothing yet descends."
        ),
    },
    {
        "id": "v2-r165-b18", "out": "s18-the-gift-came.jpeg", "seg": "n5",
        "window": "80.000-82.883", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS", "PETER"],
        "narration": "And in that moment, under that authority, the gift finally came.",
        "must_show": "the believer under the apostle's hands lifting a face filled with sudden joy and awe as warm light comes down onto him from above the top of the frame — the gift arriving at the moment of the laying on of hands.",
        "must_not_show": "the Holy Ghost NEVER embodied — no dove, no figure, no tongues of flame; ONLY warm light from above the frame edge; no halo or light ringing the head; no cream; no panel or text.",
        "scene": (
            "The gift arriving: still under the apostle's laid-on hands, a "
            "Samaritan believer lifts a face suddenly filled with joy and awe "
            "as warm light comes down onto him from above the top of the frame "
            "— the promised gift come at last in the moment of the laying on of "
            "hands. The light stays at the frame's upper edge and never becomes "
            "a dove, a flame, a figure or a ring around his head. A distinct "
            "radiant face, earth-toned wool, an ordinary man with two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r165-b19", "out": "s19-received-the-holy-ghost.jpeg", "seg": "kv17",
        "window": "82.883-88.106", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN", "BELIEVERS"],
        "narration": (
            "Then laid they their hands on them, and they received the "
            "Holy Ghost."
        ),
        "must_show": "SCRIPTURE-EXACT — the fuller two-shot: Peter and John with hands laid on the bowed believers, and the believers' upturned faces filled with light and joy as warm light rests down from above — the verse in one frame, hands and gift together.",
        "must_not_show": "the Holy Ghost NEVER a dove, flame or figure — only warm light from above the frame edge; no light ringing anyone's head; Peter and John consistent; no cream; no panel or text.",
        "scene": (
            "The whole verse in one steady frame: Peter and John stand with "
            "their hands laid on the heads of the kneeling Samaritan believers, "
            "and the believers' upturned faces are lit with joy and awe as warm "
            "light rests down over them from above the top of the frame — they "
            "have received the Holy Ghost. The light comes only from the upper "
            "edge and becomes no dove, flame or figure. The apostles are "
            "recognizable and consistent; distinct radiant believer faces, "
            "earth-toned wool, two hands and one head each."
        ),
    },
    {
        "id": "v2-r165-b20", "out": "s20-the-study-gem.jpeg", "seg": "n6",
        "window": "88.106-93.500", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Here is the quiet study gem. The gift of the Holy Ghost did not "
            "arrive by sincerity alone, or by baptism alone."
        ),
        "must_show": "a quiet study insert — an open first-century scroll of the book of Acts lit by a small clay oil lamp, a reader's hand resting on the lines; the turn to careful reading of what just happened.",
        "must_not_show": "no modern book, paper or print; NO legible modern letters or numbers on the scroll; warm lamp light, nothing ringing anything; no panel, border or text overlay.",
        "scene": (
            "The turn to close reading: an insert looking down at an open "
            "first-century papyrus scroll on a plain wooden table, a small clay "
            "oil lamp beside it laying warm low light across the lines, and a "
            "reader's weathered hand resting quietly on the words as if pausing "
            "on something just noticed. The room is still and dim around the "
            "lamp. The scroll bears only plain ancient ink strokes, nothing "
            "legible or modern; the hand is whole with five fingers."
        ),
    },
    {
        "id": "v2-r165-b21", "out": "s21-travelled-by-authority.jpeg", "seg": "n6",
        "window": "93.500-99.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "BELIEVERS"],
        "narration": (
            "It travelled by authority — conferred through the laying on of "
            "hands by those God had sent."
        ),
        "must_show": "a clean insert-scale reprise of the laying on of hands — an apostle's authoritative hands on a believer's head with warm light resting from above — stating plainly that the gift travelled through that authority.",
        "must_not_show": "the Holy Ghost never a dove, flame or figure — warm light from above only; ordinary hands, five fingers; no cream; no light ringing the head; no panel.",
        "scene": (
            "The channel of the gift, restated: a clean close on an apostle's "
            "weathered, authoritative hands laid firmly on a believer's bowed "
            "head, warm light resting down from above the top of the frame onto "
            "the believer's calm face — the gift travelling by authority, "
            "conferred through the laying on of hands of those God had sent. The "
            "light stays at the upper edge and becomes no figure. Real hands "
            "whole with five fingers, earth-toned sleeve, a distinct believer "
            "face, two hands and one head."
        ),
    },
    {
        "id": "v2-r165-b22", "out": "s22-order-and-gift.jpeg", "seg": "n6",
        "window": "99.500-105.242", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN", "BELIEVERS", "SAMARIA-HILL"],
        "narration": "Order and gift belong together.",
        "must_show": "a settled two/three-shot: the apostles Peter and John standing with the newly-filled believers around them, hands still near shoulders, warm daylight over the town — authority and gift held together in one calm frame.",
        "must_not_show": "not a crowd; no Spirit embodied; Peter and John consistent; no cream; distinct faces; no panel or text.",
        "scene": (
            "Authority and gift resting together: Peter and John stand among the "
            "newly-filled Samaritan believers before the pale hill town, a hand "
            "of each still near a believer's shoulder, every face settled and "
            "glad in the warm daylight — the order that carried the gift and the "
            "gift itself held together in one calm frame. The apostles are "
            "recognizable and consistent; the believers distinct and "
            "earth-toned, each with two hands and one head."
        ),
    },
    {
        "id": "v2-r165-b23", "out": "s23-offered-to-you.jpeg", "seg": "n7",
        "window": "105.242-110.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": (
            "And that same gift is still offered to you, by that same pattern."
        ),
        "must_show": "a single believer — the viewer's stand-in — kneeling with an upturned, open face, the room quiet around him, ready; the same gift offered by the same pattern, now to the one watching.",
        "must_not_show": "no Spirit descending yet in this beat; distinct open face; no cream; no halo; no panel or text.",
        "scene": (
            "The pattern turned toward the viewer: a single believer kneels with "
            "his face upturned and open, hands loose at his sides, the warm room "
            "quiet around him — the viewer's own place in the story, someone "
            "offered the same gift by the same pattern. His face is honest and "
            "ready in warm light; a distinct ordinary man with two hands and one "
            "head, none of the air yet stirring."
        ),
    },
    {
        "id": "v2-r165-b24", "out": "s24-the-comforter-given.jpeg", "seg": "n7",
        "window": "110.000-115.810", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": (
            "Faith and baptism open the door, and then, by the hands of those "
            "with authority, the Comforter is given to be with you."
        ),
        "must_show": "the kneeling believer now under authoritative laid-on hands with warm light resting from above onto his peaceful face — faith and baptism having opened the door, the Comforter given to be with him.",
        "must_not_show": "the Comforter NEVER a dove, flame or figure — warm light from above only; ordinary hands, five fingers; no cream; no light ringing the head; no panel.",
        "scene": (
            "The promise completed on the viewer's stand-in: the kneeling "
            "believer is now under a pair of authoritative laid-on hands, and "
            "warm light rests down onto his peaceful, lifted face from above the "
            "top of the frame — faith and baptism having opened the door, the "
            "Comforter given to be with him. The light stays at the upper edge "
            "and becomes no dove, flame or figure. A distinct calm face, "
            "earth-toned wool, whole hands, one head."
        ),
    },
    {
        "id": "v2-r165-b25", "out": "s25-will-you-receive-it.jpeg", "seg": "n7",
        "window": "115.810-119.606", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": "When that gift is offered to you, will you receive it?",
        "must_show": "the closing invitation — a close on the believer's open, upturned face and slightly opened hands, warm light gentle on him, the question left hopeful and unhurried: will you receive it?",
        "must_not_show": "no grasping or clenched hands — open and receiving; no dove, flame or figure; no light ringing the head; no cream; no panel or text.",
        "scene": (
            "The film hands the question across: a close on the believer's open, "
            "upturned face and hands loosening at his sides as if ready to "
            "receive, warm daylight gentle on him and the quiet town behind — "
            "the same gift offered, the question left hopeful and unhurried. "
            "Nothing is grasped; the hands are open. A distinct ordinary face, "
            "earth-toned wool, two whole hands and one head, no figure and "
            "nothing ringing his head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# EMPTY BY DESIGN. SAMARIA-HILL and JERUSALEM-ROOM are NEW recurring places with
# no stash match, so there is no plate to wire at author time. The runner
# promotes each from this build's first good frame: promote b01 (or the calmer
# b22) for SAMARIA-HILL, and b04 for JERUSALEM-ROOM, then generate the rest with
# the plates attached. No beat in this row bears Jesus, so any frame is safe to
# promote. Full steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===
