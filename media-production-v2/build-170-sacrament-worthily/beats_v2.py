#!/usr/bin/env python3
"""V2 beat map — row 170, build-170-sacrament-worthily (1 Corinthians 11:23-28).

COVERAGE: 24 pictures over 119.40 s (card_start) = ~5.0 s/picture (matches the
library density; lesson 12 movie-coverage — every turn its own frame, the two
elements each their own inserts).

OPEN CAMERON COMPLAINT: none on file (`v2_outline.py 170` shows no prior
review). Fresh authoring — the job is the LEARNING/COST laws in the positive.

TWO REGISTERS (the narration itself splits the video in half):
  A) THE INSTITUTION at the Last Supper (b01-b09): Paul recounts the night Jesus
     took the bread and the cup. The upper room, at NIGHT, lamplit; Jesus (the
     Master) present with his locked face; a few friends reclining (not the whole
     Twelve crowded in — movie coverage). ROOM + MEAL locks BYTE-IDENTICAL to
     row 89 (build-89-last-supper) for cross-video consistency of the room.
  B) THE ONGOING ORDINANCE + INVITATION (b10-b24): "ever since, his people have
     taken that same bread and cup." Later first-century believers at a plain
     GATHERING table, remembering, examining themselves, renewing the covenant,
     and the place kept open for "you." NO Jesus in register B (jesus=False).

SPEAKER LAW (important, and NOT the usual red-letter): this is PAUL'S EPISTLE
recounting the supper. kv24 and kv25 quote Jesus's institution words ("Take,
eat: this is my body…" / "This cup is the new testament in my blood…"), BUT
beats.json marks them the SCRIPTURE voice (Paul handing it on), so their CAPTIONS
are LIGHT-BLUE, not red. The PICTURES still show Jesus (jesus=True, ref=True,
cream) because the event is the Last Supper and he is physically there — the
jesus flag drives the picture, the segment speaker drives the caption colour.
s26 and s28 are likewise SCRIPTURE (blue) and sit on the believers, not Jesus.
There is NO Jesus-red and NO God-voice anywhere in this row.

TIME OF DAY: register A is NIGHT (the upper room, lamplit — NIGHT-LAMPLIGHT).
Register B is a warm quiet indoor light (small clay lamps / one window), reverent
and timeless. No sunset anywhere.

CONTENT-CARE: row 170 is GREEN (not in the flag table). One restraint applies by
spirit: "remembering a sacrifice already made" (b15) is a believer's REMEMBERING
FACE with the bread and cup — NEVER a crucifixion / wound / gore image.

NEW places (runner promotes each from its first good frame; lesson 11):
  ROOM       promote b01 (upper room, night) — wire the register-A beats
  GATHERING  promote b10 (believers' room)   — wire the register-B beats
ELEMENTS is a small-object lock (loaf + clay cup), carried by text for
consistency across both registers — no plate needed. Steps in QC.md.
"""

# LOCKS: ROOM + MEAL are BYTE-IDENTICAL to row 89 (cross-video Last-Supper room).
# ELEMENTS + GATHERING are build-local. Setting locks NEVER name a character;
# only Jesus wears cream.
LOCKS = {
    "ROOM": (
        "ROOM LOCK: the upper room — a large furnished chamber up an "
        "outside stair: a LOW U-SHAPED TABLE with cushions where "
        "diners recline, clay oil lamps on the table and in wall "
        "niches, plastered walls, one shuttered window open on the "
        "night. The same table, lamps and walls throughout."
    ),
    "MEAL": (
        "MEAL LOCK: the Passover table — flat rounds of unleavened "
        "bread, a large two-handled CLAY CUP of dark wine, bowls of "
        "bitter herbs and fruit paste, a roasted portion; simple "
        "earthenware, nothing gilded."
    ),
    "ELEMENTS": (
        "ELEMENTS LOCK: the bread and the cup of the ordinance — one "
        "flat round of unleavened bread and one large two-handled CLAY "
        "CUP of dark red wine, plain earthenware on a plain wooden "
        "surface; the same loaf and the same cup in every close frame, "
        "nothing gilded, never a modern tray, glass, plate or metal "
        "vessel."
    ),
    "GATHERING": (
        "GATHERING LOCK: the same plain first-century room in every "
        "frame where later believers meet to remember — bare "
        "pale-plastered walls, a low plain wooden table, floor cushions "
        "and hand-woven mats, one or two small clay oil lamps giving a "
        "warm quiet light, one plain square window opening; simple and "
        "reverent, nothing gilded, never a chair, glass, hanging "
        "fixture or any modern object. The same modest room throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r170-b01", "out": "s01-the-upper-room.jpeg", "seg": "n1",
        "window": "0.280-4.000", "wide": True, "jesus": True, "ref": True,
        "locks": ["ROOM", "MEAL", "BACKGROUND-CAST"],
        "narration": "Paul was handing on something sacred that he had received himself:",
        "must_show": "the ONE establishing wide of the upper room at night — the camera in the doorway shooting past the backs of the near diners: the low U-shaped table laid with the Passover meal in lamplight, a few friends reclining, Jesus among them at his place; an intimate supper, not a crowded portrait.",
        "must_not_show": "no halo, glare or rim-light; only Jesus in cream; Jesus ordinary-sized among the reclining friends (SCALE GATE); no posed line facing the lens; no modern object; no panel, border or text.",
        "scene": (
            "From the head of its outside stair the camera stands in the doorway "
            "of the upper room and looks in past the backs and shoulders of the "
            "near diners: the low U-shaped table is laid end to end with the old "
            "meal — flat rounds of bread, the great clay cup filled dark, the "
            "bitter herbs in their bowls — clay lamps burning warm on the table "
            "and in the wall niches, one shuttered window open on the night. A "
            "few friends recline along the cushions, and among them at his place "
            "sits Jesus in his plain cream robe, an ordinary-sized man no larger "
            "than those beside him. Faces are on one another and the meal, not "
            "the camera; no light rings any head."
        ),
    },
    {
        "id": "v2-r170-b02", "out": "s02-the-night-he-was-betrayed.jpeg", "seg": "n1",
        "window": "4.000-8.500", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM", "MEAL", "BACKGROUND-CAST"],
        "narration": "on the very night he was betrayed, at supper with his friends,",
        "must_show": "closer, intimate — a two- or three-shot: Jesus reclining at the low table with a couple of friends close beside him in the lamplight; the tenderness of the last supper among those who loved him.",
        "must_not_show": "no halo, glare or rim-light; only Jesus in cream; distinct friends' faces, not twins; Jesus ordinary-sized; no face posed to the lens; no modern object; no panel or text.",
        "scene": (
            "Closer at the low table in the warm lamplight: Jesus reclines on the "
            "cushions with two friends near beside him, the clay cup and the flat "
            "bread on the board before them, the night quiet at the shuttered "
            "window. The friends lean in, distinct men of ordinary build in deep "
            "earth-toned wool, listening; Jesus in plain cream is calm and warm "
            "among them, ordinary-sized. The single lamps light the fronts of "
            "their faces and leave the tops of their heads soft in the dark. "
            "Their eyes are on each other and the meal, not the camera; no light "
            "rings any head."
        ),
    },
    {
        "id": "v2-r170-b03", "out": "s03-took-a-loaf-of-bread.jpeg", "seg": "n1",
        "window": "8.500-12.623", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM", "ELEMENTS"],
        "narration": "the Master took a simple loaf of bread into his hands and gave thanks over it.",
        "must_show": "Jesus taking the loaf — a close on his two hands lifting the flat round of unleavened bread, his head bowed a little in thanks over it; the giving of thanks.",
        "must_not_show": "no halo, glare or rim-light; only Jesus in cream; whole hands, natural grip on the bread; no modern object; no face posed to the lens; no panel or text.",
        "scene": (
            "Close in the lamplight: Jesus lifts the simple flat round of "
            "unleavened bread in both hands over the low table, his head bowed a "
            "little and his eyes lowered in thanks, the warm lamp catching the "
            "bread and his fingers and the front of his cream robe. The clay cup "
            "waits on the board beside it. His hands are whole and natural on the "
            "loaf, his face quiet and downcast in gratitude, not toward the "
            "camera; no light rings his head."
        ),
    },
    {
        "id": "v2-r170-b04", "out": "s04-he-brake-it.jpeg", "seg": "kv24",
        "window": "12.623-16.800", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM", "ELEMENTS"],
        "narration": "And when he had given thanks, he brake it, and said, Take, eat:",
        "must_show": "SCRIPTURE-EXACT (Paul recounting — light-blue caption) — Jesus breaking the loaf in his two hands and beginning to offer it; the breaking, mid-act.",
        "must_not_show": "no halo, glare or rim-light; only Jesus in cream; caption is scripture light-blue, NOT red; whole hands; no modern object; no panel or text.",
        "scene": (
            "In the warm lamplight Jesus breaks the flat loaf in his two hands "
            "over the table — the round parting between his fingers — and turns "
            "the broken bread a little outward to offer it, his face lifting "
            "toward the friends beside him. The clay cup stands near on the "
            "board. His hands are whole and sure on the bread, his eyes on the "
            "one he offers it to, not the camera; the lamps leave the top of his "
            "head soft in the dark, and no light rings it."
        ),
    },
    {
        "id": "v2-r170-b05", "out": "s05-this-is-my-body.jpeg", "seg": "kv24",
        "window": "16.800-22.819", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM", "ELEMENTS"],
        "narration": "this is my body, which is broken for you: this do in remembrance of me.",
        "must_show": "SCRIPTURE-EXACT — a close insert: the broken half-loaf held out in Jesus's hand toward a friend's opening hand; the bread given, remembrance asked.",
        "must_not_show": "no halo, glare or rim-light; only Jesus in cream; caption scripture light-blue; whole hands, natural pass of the bread; no modern object; no panel or text.",
        "scene": (
            "A close insert over the low table in the lamplight: the broken piece "
            "of unleavened bread resting in Jesus's open hand, held out toward a "
            "friend's cupped hand rising to receive it — the pass of the bread "
            "mid-gift, the front of the cream robe and both men's hands warm in "
            "the lamp's light. Jesus's face beyond is quiet and giving. All hands "
            "whole and natural, nobody turned to the camera; no light rings any "
            "head."
        ),
    },
    {
        "id": "v2-r170-b06", "out": "s06-then-he-lifted-the-cup.jpeg", "seg": "n2",
        "window": "22.819-27.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM", "ELEMENTS"],
        "narration": "Then he lifted the cup. This one, he said, was the sign of a new covenant —",
        "must_show": "Jesus lifting the cup — his two hands raising the large two-handled clay cup of dark wine from the table, presenting it; the sign of the new covenant.",
        "must_not_show": "no halo, glare or rim-light; only Jesus in cream; whole hands, natural grip on the two handles; no modern vessel; no face posed to the lens; no panel or text.",
        "scene": (
            "In the lamplight Jesus lifts the large two-handled clay cup of dark "
            "red wine from the low table in both hands and raises it a little to "
            "present it, his face turning to the friends as he names what it "
            "means. The broken bread lies on the board beside it. His hands are "
            "whole and sure on the two handles, the warm lamp on the cup and the "
            "front of his cream robe, his eyes on those he speaks to, not the "
            "camera; no light rings his head."
        ),
    },
    {
        "id": "v2-r170-b07", "out": "s07-offered-freely-to-them.jpeg", "seg": "n2",
        "window": "27.000-32.906", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM", "ELEMENTS", "BACKGROUND-CAST"],
        "narration": "a solemn promise sealed between God and his people, and offered freely to them.",
        "must_show": "the cup offered — Jesus extending the clay cup toward a friend across the table, the friend leaning in to take it; a promise handed over freely.",
        "must_not_show": "no halo, glare or rim-light; only Jesus in cream; distinct friends' faces; whole hands; no modern object; no face posed to the lens; no panel or text.",
        "scene": (
            "Across the low table Jesus extends the two-handled clay cup toward a "
            "friend who leans in to take it, both their hands on the vessel for "
            "the moment of the pass, the dark wine catching the lamplight — a "
            "promise offered freely and received. Other friends beside them "
            "watch, distinct men in deep earth-toned wool. Jesus in cream is warm "
            "and unhurried, ordinary-sized; all hands whole and natural, eyes on "
            "the cup and each other, not the camera; no light rings any head."
        ),
    },
    {
        "id": "v2-r170-b08", "out": "s08-after-the-same-manner.jpeg", "seg": "kv25",
        "window": "32.906-38.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM", "ELEMENTS"],
        "narration": "After the same manner also he took the cup, when he had supped, saying,",
        "must_show": "SCRIPTURE-EXACT (Paul recounting — light-blue) — Jesus holding the clay cup after the meal, drawing breath to speak the words over it; the moment before the saying.",
        "must_not_show": "no halo, glare or rim-light; only Jesus in cream; caption scripture light-blue, NOT red; whole hands; no modern object; no panel or text.",
        "scene": (
            "The supper mostly done, Jesus holds the two-handled clay cup steady "
            "before him in the lamplight, his face lifting and steadying as he "
            "draws breath to speak the words over it. The emptied dishes and the "
            "broken bread lie along the low table. His hands are whole on the "
            "handles, the warm lamp on the wine and the front of his cream robe, "
            "his gaze toward the friends, not the camera; the top of his head is "
            "soft in the dark and no light rings it."
        ),
    },
    {
        "id": "v2-r170-b09", "out": "s09-the-new-testament-in-my-blood.jpeg", "seg": "kv25",
        "window": "38.000-44.586", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM", "ELEMENTS"],
        "narration": "This cup is the new testament in my blood: this do ye, as oft as ye drink it, in remembrance of me.",
        "must_show": "SCRIPTURE-EXACT — a close on the raised clay cup in Jesus's hands with his warm face beyond speaking the words; the covenant of the cup, remembrance asked.",
        "must_not_show": "no halo, glare or rim-light; only Jesus in cream; caption scripture light-blue; NO blood or wound imagery — only the cup of dark wine; whole hands; no modern object; no panel or text.",
        "scene": (
            "A close on the two-handled clay cup raised in Jesus's hands, the "
            "dark red wine still in it, and his warm face beyond speaking the "
            "words gently over it in the lamplight — the covenant of the cup "
            "named for those who will drink it in remembrance ever after. His "
            "hands are whole on the handles, the front of his cream robe lit warm "
            "by the lamp, his eyes on the friends, not the camera; no light rings "
            "his head."
        ),
    },
    {
        "id": "v2-r170-b10", "out": "s10-that-same-bread-and-cup.jpeg", "seg": "n3",
        "window": "44.586-50.000", "wide": True, "jesus": False, "ref": False,
        "locks": ["GATHERING", "ELEMENTS", "BACKGROUND-CAST"],
        "narration": "Ever since, his people have taken that same bread and that same cup together,",
        "must_show": "the ONE establishing wide of register B — the camera behind the near believers' shoulders: a plain first-century room where later believers are gathered around a low table with the same loaf and clay cup, sharing it together; the ongoing ordinance.",
        "must_not_show": "no Jesus and no cream here; no halo, glare or rim-light; distinct believers' faces, not a posed line to the lens; nothing modern (no chair, glass, tray); no panel or text.",
        "scene": (
            "The film shifts to a plain first-century room: the camera stands "
            "back behind the shoulders of the near believers and looks across a "
            "low plain wooden table where a small company is gathered on floor "
            "cushions in a warm quiet lamplight — the same flat loaf and the same "
            "two-handled clay cup passing among them, hands receiving and giving. "
            "They are ordinary people of honest variety in deep earth-toned wool, "
            "distinct faces, none in cream and none turned to the camera; one "
            "plain window opens on soft light. No light rings any head, nothing "
            "modern anywhere."
        ),
    },
    {
        "id": "v2-r170-b11", "out": "s11-a-holy-act-of-remembering.jpeg", "seg": "n3",
        "window": "50.000-55.400", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "ELEMENTS"],
        "narration": "quietly, reverently — a small, holy act of remembering the One who gave everything for them.",
        "must_show": "a close on believers' hands receiving the broken bread, or a bowed reverent face over the cup; the small holy act of remembering, tender and quiet.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; NO crucifixion or wound imagery; whole hands; nothing modern; no face posed to the lens; no panel or text.",
        "scene": (
            "A close in the warm lamplight: a believer's cupped hands receive the "
            "broken piece of unleavened bread from another's hand, both faces "
            "bowed and still in reverence, the two-handled clay cup waiting on "
            "the low table beside them — a small, holy act of remembering carried "
            "out quietly. The hands are whole and gentle, the people ordinary and "
            "earth-toned, their eyes lowered and inward, not the camera; no light "
            "rings any head."
        ),
    },
    {
        "id": "v2-r170-b12", "out": "s12-shew-the-lords-death.jpeg", "seg": "s26",
        "window": "55.400-61.975", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "ELEMENTS"],
        "narration": "For as often as ye eat this bread, and drink this cup, ye do shew the Lord's death till he come.",
        "must_show": "SCRIPTURE-EXACT (light-blue) — believers partaking together, the bread eaten and the cup drunk, solemn and hopeful; the ordinance that proclaims his death until he comes.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; NO death, cross or wound shown — only the reverent partaking; nothing modern; no face posed to the lens; no panel or text.",
        "scene": (
            "In the quiet lamplight a believer lifts the two-handled clay cup to "
            "drink while another holds the broken bread, the small company still "
            "and solemn around the low table — the plain act by which, again and "
            "again, they proclaim the Lord's death until he comes. They are "
            "ordinary earth-toned people, whole hands on the cup and bread, their "
            "faces grave and hopeful, eyes lowered, not the camera; nothing "
            "modern, no light rings any head."
        ),
    },
    {
        "id": "v2-r170-b13", "out": "s13-two-directions-at-once.jpeg", "seg": "n4",
        "window": "61.975-64.110", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "ELEMENTS"],
        "narration": "And it looks in two directions at once.",
        "must_show": "a believer pausing with the bread in hand, thoughtful — the ordinance holding two directions; a quiet reflective beat.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; nothing modern; no face posed to the lens; no panel or text.",
        "scene": (
            "A close on one believer pausing in the lamplight, the broken piece "
            "of bread held still in an open hand, the face thoughtful and quiet "
            "as if the moment reaches both backward and forward at once. The "
            "two-handled clay cup rests on the low table beside. An ordinary "
            "earth-toned person, whole hand on the bread, eyes lowered in "
            "thought, not the camera; nothing modern, no light rings the head."
        ),
    },
    {
        "id": "v2-r170-b14", "out": "s14-a-sacrifice-already-made.jpeg", "seg": "n4",
        "window": "64.110-68.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "ELEMENTS"],
        "narration": "Every time we take it, we are remembering a sacrifice already made,",
        "must_show": "the REMEMBERING face — a believer with eyes closed or lowered over the bread and cup, holding the memory of a sacrifice already made; the weight of it on the human face, never on any wound.",
        "must_not_show": "no Jesus and no cream; NO crucifixion, cross, blood or wound imagery of any kind (restraint law); no halo, glare or rim-light; nothing modern; no panel or text.",
        "scene": (
            "A close on a believer's remembering face in the warm lamplight — "
            "eyes closed, head bowed a little over the broken bread and the clay "
            "cup on the low table — the whole weight of a sacrifice already made "
            "held quietly in the features, carried on the human face alone. An "
            "ordinary earth-toned person, hands still and whole, no wound and no "
            "cross anywhere in the frame, eyes shut and inward, not the camera; "
            "no light rings the head."
        ),
    },
    {
        "id": "v2-r170-b15", "out": "s15-looking-forward-in-hope.jpeg", "seg": "n4",
        "window": "68.500-72.988", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING"],
        "narration": "and we are looking forward, in hope, to the day he returns.",
        "must_show": "the forward direction — a believer's face lifting toward the plain window and its soft light, hopeful; looking forward to the day he returns.",
        "must_not_show": "no Jesus and no cream; NO figure or vision in the window — only soft natural light; no halo, glare or rim-light; nothing modern; no panel or text.",
        "scene": (
            "A believer lifts a quiet hopeful face toward the plain square window "
            "of the room, where soft daylight comes in beyond the warm lamps — "
            "the look of someone remembering forward, toward a day still to come. "
            "The low table with the bread and cup sits below in the room. An "
            "ordinary earth-toned person, an ordinary window with only soft light "
            "in it and no figure, eyes lifted and forward, not the camera; no "
            "light rings the head."
        ),
    },
    {
        "id": "v2-r170-b16", "out": "s16-let-a-man-examine-himself.jpeg", "seg": "s28",
        "window": "72.988-79.180", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "ELEMENTS"],
        "narration": "But let a man examine himself, and so let him eat of that bread, and drink of that cup.",
        "must_show": "SCRIPTURE-EXACT (light-blue) — a believer examining his own heart before he partakes: seated over the bread and cup, a hand on his own chest, head bowed in an honest, quiet self-searching.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; the examining honest and gentle, never fearful or shamed; nothing modern; no panel or text.",
        "scene": (
            "A close in the lamplight: a believer sits over the low table with "
            "the broken bread and the clay cup before him, one hand laid on his "
            "own chest and his head bowed — an honest, quiet looking into his own "
            "heart before he eats and drinks. An ordinary earth-toned person, "
            "whole hands, the face searching but at peace, not fearful; eyes "
            "lowered and inward, not the camera; nothing modern, no light rings "
            "the head."
        ),
    },
    {
        "id": "v2-r170-b17", "out": "s17-paul-asked-gently.jpeg", "seg": "n5",
        "window": "79.180-83.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "ELEMENTS"],
        "narration": "Paul asked for just one thing beforehand, and he asked it gently:",
        "must_show": "the gentleness — a believer pausing before the table, calm and unhurried, the one gentle asking of Paul; nothing stern about it.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; no sternness or fear; nothing modern; no face posed to the lens; no panel or text.",
        "scene": (
            "A quiet close in the lamplight: a believer sits back a little before "
            "the low table with the bread and cup, hands loose and open, the face "
            "calm and unhurried — the mood of a gentle asking, not a stern rule. "
            "An ordinary earth-toned person, whole open hands, eyes soft and "
            "lowered, not the camera; nothing modern, no light rings the head."
        ),
    },
    {
        "id": "v2-r170-b18", "out": "s18-look-honestly-into-his-heart.jpeg", "seg": "n5",
        "window": "83.500-87.830", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING"],
        "narration": "that each person pause and look honestly into his own heart, and come sincerely.",
        "must_show": "a sincere bowed face — one believer looking honestly inward, come sincerely; the pause before partaking, tender and real.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; nothing modern; no face posed to the lens; no panel or text.",
        "scene": (
            "A close on a sincere face in the warm lamplight — a believer with "
            "head bowed and eyes closed, looking honestly inward, the quiet of a "
            "person who has come to the table in earnest. An ordinary earth-toned "
            "person, the features open and tender, hands still, eyes shut, not "
            "the camera; nothing modern, no light rings the head."
        ),
    },
    {
        "id": "v2-r170-b19", "out": "s19-not-to-keep-anyone-away.jpeg", "seg": "n5",
        "window": "87.830-93.228", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "ELEMENTS", "BACKGROUND-CAST"],
        "narration": "Not to keep anyone away, but so the moment stays real and tender.",
        "must_show": "the welcome — one believer gently drawing another in toward the table with a hand, warm and unhurried; nobody kept away, the moment kept tender.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; no barring or gatekeeping gesture; nothing modern; no face posed to the lens; no panel or text.",
        "scene": (
            "In the warm lamplight one believer turns and lays a welcoming hand "
            "on the arm of another beside them, drawing them gently in toward the "
            "low table where the bread and cup wait — an open, unhurried welcome, "
            "the moment kept real and tender. They are ordinary earth-toned "
            "people, distinct faces, whole hands, warm and glad, their eyes on "
            "each other, not the camera; nothing modern, no light rings any head."
        ),
    },
    {
        "id": "v2-r170-b20", "out": "s20-again-and-again.jpeg", "seg": "n6",
        "window": "93.228-98.710", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "ELEMENTS"],
        "narration": "Here is the quiet study gem. This is why it is done again and again, and never just once.",
        "must_show": "the repetition — the low table set once more with the fresh loaf and the filled cup, believers gathering to it again; done week after week, never just once.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; nothing modern; no face posed to the lens; no panel or text.",
        "scene": (
            "The low table set again in the quiet lamplight: a fresh flat loaf "
            "and the two-handled clay cup filled anew, and believers settling to "
            "the cushions around it once more — the ordinance taken up again as "
            "it is taken up week after week, never a single closed event. "
            "Ordinary earth-toned people, distinct and unhurried, whole hands, "
            "eyes on the table and each other, not the camera; nothing modern, no "
            "light rings any head."
        ),
    },
    {
        "id": "v2-r170-b21", "out": "s21-a-covenant-renewed.jpeg", "seg": "n6",
        "window": "98.710-106.995", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "ELEMENTS"],
        "narration": "It is a covenant renewed — week after week, a fresh chance to be made clean, to set down the past and begin again.",
        "must_show": "renewal — a believer receiving the cup with a face eased and at peace, the past set down; a fresh chance to begin again, quiet relief.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; nothing modern; no face posed to the lens; no panel or text.",
        "scene": (
            "A close in the warm lamplight: a believer takes the two-handled clay "
            "cup in both hands, the face eased and at peace, the shoulders "
            "settling — the look of a covenant renewed, the past set down, a "
            "fresh chance to begin again. An ordinary earth-toned person, whole "
            "hands on the cup, the features quiet and relieved, eyes lowered, not "
            "the camera; nothing modern, no light rings the head."
        ),
    },
    {
        "id": "v2-r170-b22", "out": "s22-a-place-kept-for-you.jpeg", "seg": "n7",
        "window": "106.995-109.150", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "ELEMENTS"],
        "narration": "And a place at that table is kept for you.",
        "must_show": "the open place — the low table with the bread and cup and one empty cushion plainly kept open; a place waiting for the one watching.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; nothing modern; no panel or text.",
        "scene": (
            "A quiet frame on the low table in the warm lamplight: the flat loaf "
            "and the two-handled clay cup set ready, and beside them one empty "
            "floor cushion plainly kept open — a place at the table waiting, held "
            "for someone not yet seated. The plain room is soft around it, one "
            "window giving gentle light. No person in the open place, nothing "
            "modern, no light rings anything — only the kept seat and the bread "
            "and cup."
        ),
    },
    {
        "id": "v2-r170-b23", "out": "s23-not-for-the-perfect.jpeg", "seg": "n7",
        "window": "109.150-114.740", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "BACKGROUND-CAST"],
        "narration": "Not for the perfect, but for the sincere — for anyone willing to come and remember.",
        "must_show": "an ordinary, imperfect, sincere person being welcomed toward the table — plain and unremarkable, gladly received; the table is for the willing, not the flawless.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; no gatekeeping; nothing modern; no face posed to the lens; no panel or text.",
        "scene": (
            "In the warm lamplight an ordinary, work-worn person steps toward the "
            "low table and a seated believer turns with a glad open hand to "
            "welcome them to the empty cushion — a plain, imperfect, sincere "
            "comer gladly received, no test at the door. Both are ordinary "
            "earth-toned people, distinct faces, whole hands, warm and unhurried, "
            "their eyes on each other, not the camera; nothing modern, no light "
            "rings any head."
        ),
    },
    {
        "id": "v2-r170-b24", "out": "s24-will-you-come-to-the-table.jpeg", "seg": "n7",
        "window": "114.740-119.402", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "ELEMENTS"],
        "narration": "When the bread and the cup are offered to you, will you come to the table?",
        "must_show": "the invitation handed over — from behind the viewer's stand-in, the bread and cup offered forward across the table toward them; the open cushion waiting, the question left open and warm.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; not posed to the lens; nothing modern; no panel or text.",
        "scene": (
            "The camera sits just behind the shoulder of an ordinary person at "
            "the edge of the low table, seen from behind, as a seated believer "
            "across the table holds out the broken bread and the two-handled clay "
            "cup toward them — the elements offered forward, the open cushion "
            "plain beside, the choice handed gently across. The plain room is "
            "warm around them, one window soft with light. Ordinary earth-toned "
            "people, whole hands, the near one's gaze on the offered bread and "
            "cup, not the camera; nothing modern, no light rings any head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# EMPTY BY DESIGN. Both recurring places are NEW; the runner PROMOTES each from
# this build's first good frame (lesson 11):
#   ROOM       promote b01 (upper room, night), wire the register-A beats
#   GATHERING  promote b10 (believers' room),   wire the register-B beats
# ELEMENTS is a small-object lock carried by text (loaf + clay cup) — no plate.
# Full steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===
