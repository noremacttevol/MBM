#!/usr/bin/env python3
"""V2 beat map — row 44, build-44-two-debtors (Luke 7:36-50).

COVERAGE: 47 pictures over 258.6 s = 5.5 s/picture (library density).
Authored from scratch 2026-08-05 to lessons 11-12 + the complaint corpus.

SAME-EVENT LAW: this is the SAME dinner as build-74-woman-washed-his-feet
(Luke 7). WOMAN, SIMON, ROOM and JAR locks below are byte-identical
copies of build-74's — same actors, same room, both videos. The runner
must face-board this row against build-74's frames when both exist.

LESSON-12 SHAPE: three true wides with stated camera geometry — b01 (the
arrival, where Simon's withheld courtesies are PLANTED), b04 (the dining
room at her entrance), b34 (the triangle: Simon, Jesus, the woman,
side-on). Everything else is coverage. The woman's acts and the parable's
tearing-of-the-bills are frame-per-action ladders that mirror each other
on purpose: her weeping/wiping/pouring ↔ the debtors' bills torn/falling/
the heavy debtor's relief.

SCRIPTURE FACTS (Luke 7:36-50 KJV):
  v36   Simon the PHARISEE invites him; Jesus reclines ("sat at meat" =
        reclining, feet stretched away — that is how she reaches them).
  v37-38 the woman "which was a sinner" brings an ALABASTER box, stands
        AT HIS FEET BEHIND HIM weeping, washes with tears, wipes with
        her hair, kisses, anoints.
  v39   Simon speaks WITHIN HIMSELF — the judgment is a thought.
  v40-43 Jesus ANSWERS the thought: creditor, 500 pence vs 50, "when
        they had NOTHING TO PAY, he frankly forgave them both."
        Simon: "I suppose he to whom he forgave most." "Thou hast
        rightly judged."
  v44-46 the triple comparison — no water/her tears; no kiss/her
        kisses; no oil/her ointment. The ARRIVAL frame must plant the
        omissions (unused water jar at the threshold, no kiss given).
  v47-50 "her sins, WHICH ARE MANY, are forgiven; for she loved much" —
        and the narration's warning: she was not forgiven BECAUSE she
        loved; she loved because she was ALREADY forgiven. "Thy faith
        hath saved thee; go in peace."

TIME OF DAY: evening dinner — warm bronze lamplight in Simon's room;
the parable vignette in plain working daylight (a told story's clean
light); her exit into early night with the courtyard lamp lit.

CONTENT-CARE: the woman is shown with COMPLETE dignity — modest dark
clothing, grief and love, nothing sensual, nothing gaudy; her reputation
lives in the guests' faces, never on her. The foot-washing frames are
feet, hands, hair and tears — reverent, never glamorous.

CHANGING CONDITION (kept OUT of the locks): the JAR — sealed, opened,
pouring, empty on its side; her HAIR — bound at entrance, loosed at his
feet; the two BILLS — written, held, torn, falling. All per-beat.
"""

# LOCKS: WOMAN, SIMON, ROOM, JAR are byte-identical to build-74. Setting
# locks never name a character. Only Jesus wears cream.
LOCKS = {
    "WOMAN": (
        "WOMAN LOCK: the woman is the same in every shot — mid-thirties, "
        "worn by a hard life but strong-featured, with deep dark eyes "
        "red-rimmed from weeping, and long dark hair bound up at her "
        "entrance, loosed at his feet. She wears MODEST dark clothing: a "
        "DEEP WINE-DARK dress and a DARK GREY shawl, plain and clean "
        "(never cream, never white; NOTHING immodest, nothing gaudy — "
        "her reputation lives in other faces, never on her). Her face is "
        "shown clearly and with complete dignity."
    ),
    "SIMON": (
        "SIMON LOCK: the host is the same man in every shot — about "
        "fifty-five, precise and spare, with a clipped grey beard, "
        "careful measuring eyes and immaculate grooming. He wears fine "
        "NEAR-BLACK INDIGO robes with a fringed shawl, exactly draped "
        "(never cream, never white). His face is shown clearly — "
        "correctness first, coldness under it, and a crack coming."
    ),
    "ROOM": (
        "DINING ROOM LOCK: Simon's careful dining room — a spotless "
        "stone-floored room with a low U-shaped table, reclining couches "
        "with the guests' FEET STRETCHED AWAY from the table, two bronze "
        "lampstands, precise appointments, and a doorway to the darker "
        "courtyard through which the uninvited may enter. The same "
        "table, couches, lamps and door throughout."
    ),
    "JAR": (
        "ALABASTER JAR LOCK: the ointment jar is the same in every shot "
        "— a small pale alabaster flask, translucent-shouldered, with a "
        "sealed narrow neck made to be broken; costly plainness. Sealed, "
        "opened, poured and empty per-beat."
    ),
    "GUESTS": (
        "GUESTS LOCK: the other diners are the same four distinct "
        "important men throughout — a heavy elder with a full white "
        "beard, a thin sharp-faced scribe, a prosperous middle-aged man "
        "with rings, and a younger earnest Pharisee — in fine DEEP "
        "wool: dark umber, grey-indigo, deep russet, near-black (never "
        "cream, never white). No two share a face."
    ),
    "CREDITOR": (
        "CREDITOR LOCK: the money-lender of the parable is the same man "
        "in every vignette shot — about sixty, round and shrewd-kind, "
        "with a short white-shot beard, in a good DARK TAWNY-BROWN robe "
        "(never cream, never white). His face is shown clearly — a "
        "businessman capable of an astonishing kindness."
    ),
    "DEBTOR-HEAVY": (
        "HEAVY DEBTOR LOCK: the greater debtor is the same man in every "
        "vignette shot — about forty-five, gaunt and stooped under his "
        "trouble, hollow-cheeked with a ragged dark beard, in a patched "
        "DUSTY CHARCOAL tunic (never cream, never white). His face is "
        "shown clearly."
    ),
    "DEBTOR-LIGHT": (
        "LIGHT DEBTOR LOCK: the lesser debtor is the same man in every "
        "vignette shot — about thirty, trim and uneasy, with a neat "
        "short black beard, in a plain DARK OLIVE tunic (never cream, "
        "never white). His face is shown clearly."
    ),
    "LENDER-ROOM": (
        "LENDER'S ROOM LOCK: the parable's counting room — a plain "
        "daylit room with one sturdy table, a bench, a wall shelf of "
        "rolled documents, an ink pot and reed pens, and one bright "
        "window lighting the tabletop. The same table, shelf and window "
        "in every vignette beat."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r044-b01", "out": "s01-a-pharisee-named-simon.jpeg", "seg": "n1",
        "window": "0.28-2.97", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SIMON", "ROOM"],
        "narration": "A Pharisee named Simon invited Jesus to dinner.",
        "must_show": "the arrival WITH the omissions planted — Simon receiving Jesus at the doorway with a stiff correct nod: NO kiss of greeting, NO basin brought, the water jar standing UNUSED by the threshold.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the coldness is in what does NOT happen — no servant kneels, no basin moves, no embrace.",
        "scene": (
            "At the dining room's doorway, the camera off at "
            "the wall's side taking the greeting in profile: "
            "Simon receives Jesus with a stiff, exactly "
            "correct nod, hands folded into his fringed shawl "
            "— no kiss of greeting offered, no embrace — and "
            "beside the threshold the tall water jar and its "
            "empty basin stand conspicuously untouched, no "
            "servant kneeling, while Jesus's road-dusted feet "
            "pass them by into the lamplit room. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b02", "out": "s02-it-was-a-careful-respectable.jpeg", "seg": "n1",
        "window": "2.97-9.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON", "GUESTS", "ROOM"],
        "narration": (
            "It was a careful, respectable house, and having a well-known "
            "teacher at your table made you look good."
        ),
        "must_show": "the motive — Simon presiding proud among his important guests, the room immaculate; hospitality as display.",
        "must_not_show": "no halo, glare or rim-light; polish without warmth — every appointment exact, no joy in it.",
        "scene": (
            "In the bronze lamplight Simon stands at the head "
            "of his spotless room with one hand indicating the "
            "laid table to his arriving guests — the white-"
            "bearded elder easing onto a couch, the ringed "
            "merchant admiring the appointments — a host "
            "collecting his evening's real dish, which is the "
            "room's opinion of him. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b03", "out": "s03-so-jesus-came-and-took.jpeg", "seg": "n1",
        "window": "9.20-14.12", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GUESTS", "ROOM"],
        "narration": (
            "So Jesus came, and took his place at the low table with the other "
            "guests."
        ),
        "must_show": "the reclining — Jesus settling onto a couch at the low table, propped on one elbow, his feet stretched AWAY from the table behind him; the staging the whole story depends on.",
        "must_not_show": "no halo, glare or rim-light on Jesus; feet BEHIND him and reachable from the room — never tucked under the table.",
        "scene": (
            "Jesus reclines onto the couch at the low table, "
            "settling onto one elbow among the other guests, "
            "his sandalled feet stretched out away from the "
            "table's edge behind him toward the open floor — "
            "the ordinary dinner posture of the age, holding "
            "his place in the lamplight like any invited man, "
            "the dust of the road still on his ankles. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b04", "out": "s04-then-the-door-opened-and.jpeg", "seg": "n2",
        "window": "14.69-18.01", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SIMON", "GUESTS", "ROOM"],
        "narration": "Then the door opened, and a woman came in who did not belong there.",
        "must_show": "SCRIPTURE-EXACT: the entrance — the whole room in one frame as the courtyard door opens: the woman at the threshold clutching the small jar, and every head at the table beginning to turn.",
        "must_not_show": "no halo, glare or rim-light; her dignity total — modest, afraid, resolved; the room's geometry clear: door, table, couches.",
        "scene": (
            "The camera stands at the room's far corner and "
            "takes the whole scene from the side: the courtyard "
            "door swung open on the darker night, the woman "
            "standing in it small and resolute with the little "
            "alabaster flask held against her, her hair bound "
            "and her dark shawl drawn close — and down the "
            "lamplit length of the U-shaped table the heads "
            "are beginning to turn toward her, Simon's first. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r044-b05", "out": "s05-everyone-in-that-town-knew.jpeg", "seg": "n2",
        "window": "18.01-20.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["GUESTS", "ROOM"],
        "narration": "Everyone in that town knew what she was.",
        "must_show": "the reputation — close on a knot of guests' faces: recognition, disdain, the story of her told entirely in their expressions.",
        "must_not_show": "no halo, glare or rim-light; HER reputation lives on THEIR faces — nothing about her own appearance signals it.",
        "scene": (
            "Close along the table's edge: the thin scribe's "
            "lip already curling, the ringed merchant leaning "
            "to murmur behind his hand to the white-bearded "
            "elder, whose brows have climbed — three faces "
            "doing the whole town's talking in perfect "
            "silence, the lamplight catching the small cruel "
            "comfort of men watching someone else be the "
            "scandal. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r044-b06", "out": "s06-she-had-lived-a-life.jpeg", "seg": "n2",
        "window": "20.66-29.09", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "ROOM"],
        "narration": (
            "She had lived a life the whole village whispered about, and she "
            "walked into a Pharisee's house carrying a small alabaster jar of "
            "costly perfume."
        ),
        "must_show": "the walk — the woman crossing the room through the gauntlet of stares, eyes down, the jar held with both hands; moving toward Jesus's couch at the frame's far side.",
        "must_not_show": "no halo, glare or rim-light; her travel direction unmistakable — TOWARD his couch, which is in frame; she looks at no one.",
        "scene": (
            "In medium-full from the side the woman crosses "
            "the spotless floor with her eyes down and the "
            "small pale flask held in both hands against her "
            "dark dress — walking a straight quiet line past "
            "the staring table toward the couch at the frame's "
            "far side where Jesus reclines, his stretched-out "
            "feet the visible end of her whole journey. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b07", "out": "s07-she-went-straight-to-his.jpeg", "seg": "n3",
        "window": "29.64-31.12", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "ROOM"],
        "narration": "She went straight to his feet.",
        "must_show": "SCRIPTURE-EXACT: arriving at his feet BEHIND him — the woman sinking to her knees at the couch's end where his feet rest; his reclining form beyond.",
        "must_not_show": "no halo, glare or rim-light; the geometry exact — she is behind the couch at his feet, never across the table.",
        "scene": (
            "At the couch's end the woman sinks to her knees "
            "on the stone floor where his feet rest stretched "
            "away from the table — her dark skirts settling, "
            "the flask set carefully beside her, her head "
            "bowing over his road-dusted feet while beyond "
            "her, up the couch's length, the dinner's "
            "lamplight and murmur carry on a world away. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r044-b08", "out": "s08-and-there-in-front-of.jpeg", "seg": "n3",
        "window": "31.12-35.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": (
            "And there, in front of every important man in the room, she broke."
        ),
        "must_show": "the breaking — close on her face as the composure goes: grief and love arriving together, the first tears falling.",
        "must_not_show": "no halo, glare or rim-light; complete dignity in the breaking — real weeping, nothing performed.",
        "scene": (
            "Close on the woman's bowed face in the warm "
            "lamplight: the held line of her mouth giving "
            "way, her red-rimmed eyes flooding past their "
            "guard, the first tears dropping bright off her "
            "cheeks — a woman coming apart on purpose in the "
            "one room in town most guaranteed to despise her "
            "for it. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r044-b09", "out": "s09-she-wept-until-her-tears.jpeg", "seg": "n3",
        "window": "35.27-40.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": (
            "She wept until her tears fell on his feet, and she wiped them away "
            "with her own hair,"
        ),
        "must_show": "SCRIPTURE-EXACT: tears and hair — close at his feet: her tears falling on them, her hair now LOOSED and drawn across them, wiping the road dust in clean streaks.",
        "must_not_show": "no halo, glare or rim-light; reverent close of feet, hands, hair, tears — nothing else; her hair visibly loosed from its binding.",
        "scene": (
            "Close at his feet on the couch's end: her tears "
            "fall and land bright on the dusty skin, and her "
            "long dark hair, loosed now from its binding, is "
            "drawn gently across them in her two hands, "
            "wiping the wet through the road dust in clean "
            "streaks — the humblest towel in the world doing "
            "its work in the lamplight. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b10", "out": "s10-and-kissed-them-and-poured.jpeg", "seg": "n3",
        "window": "40.00-44.03", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "JAR"],
        "narration": "and kissed them, and poured the perfume out over them.",
        "must_show": "SCRIPTURE-EXACT: the pouring — the small alabaster flask OPEN and tipped in her hands, the costly ointment running over his feet; her lips just lifted from a kiss.",
        "must_not_show": "no halo, glare or rim-light; the jar recognizably the locked flask, neck opened; the pour generous — everything she has, going out.",
        "scene": (
            "The little pale flask tips in her two hands, its "
            "sealed neck broken open, and the ointment runs "
            "down in a thin bright thread over his feet, its "
            "sheen catching the lamplight — her head still "
            "bowed close from the kiss just given, her loosed "
            "hair falling around the pouring — a life's "
            "savings emptying itself without hesitation. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b11", "out": "s11-simon-watched-and-said-nothing.jpeg", "seg": "n4",
        "window": "44.61-49.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON", "ROOM"],
        "narration": (
            "Simon watched, and said nothing out loud. But inside, he had "
            "already made up his mind."
        ),
        "must_show": "the silent verdict — close on Simon's face watching (the scene off-frame): the correct host's mask with the cold conclusion sealing behind it.",
        "must_not_show": "no halo, glare or rim-light; nothing said, nothing moved — the judgment happens entirely behind the eyes.",
        "scene": (
            "Close on Simon at the table's head: his face "
            "perfectly composed, wine cup motionless in his "
            "hand, eyes fixed down the room on what is "
            "happening at the far couch — and behind the "
            "correct stillness the verdict visibly closing "
            "like a ledger, a man finishing a sum he started "
            "the moment the door opened. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b12", "out": "s12-if-this-man-were-really.jpeg", "seg": "n4",
        "window": "49.23-56.82", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "WOMAN", "ROOM"],
        "narration": (
            "If this man were really a prophet, he thought, he would know what "
            "kind of woman is touching him, and he would never let her near."
        ),
        "must_show": "the thought's view — over Simon's shoulder: his POV down the room of Jesus reclining unmoved while the woman tends his feet; the scene that condemns them both in his ledger.",
        "must_not_show": "no halo, glare or rim-light on Jesus; Jesus visibly NOT recoiling — his calm is the scandal Simon is reading.",
        "scene": (
            "Over Simon's dark shoulder the room runs away in "
            "lamplight to the far couch: Jesus reclined and "
            "utterly unmoved, one arm at rest, while at his "
            "feet the kneeling woman's bowed head and loosed "
            "hair keep their gentle work — the whole tableau "
            "framed between the host's rigid shoulder and the "
            "doorpost, exactly as his verdict sees it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b13", "out": "s13-simon-i-have-somewhat-to.jpeg", "seg": "j1",
        "window": "57.35-59.63", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM"],
        "narration": "Simon, I have somewhat to say unto thee.",
        "must_show": "SCRIPTURE-EXACT: the thought answered — close on Jesus, head turned toward Simon, calm and direct; the conversation nobody heard, joined.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no accusation in the face — courtesy with absolute aim.",
        "scene": (
            "Close on Jesus in the lamplight, his head turned "
            "from the room toward his host, his remarkable "
            "eyes level and unhurried — the mild opening words "
            "of a man who has heard a sentence spoken in "
            "another man's silence and intends, gently, to "
            "answer it out loud. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b14", "out": "s14-master-say-on.jpeg", "seg": "s40",
        "window": "61.15-62.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON"],
        "narration": "Master, say on.",
        "must_show": "SCRIPTURE-EXACT: the careful consent — close on Simon: the polite formula, and behind it the first flicker of a man wondering what is coming.",
        "must_not_show": "no halo, glare or rim-light; courtesy intact, certainty no longer.",
        "scene": (
            "Close on Simon's precise face as he grants the "
            "courtesy: the clipped grey beard dipping in a "
            "small correct bow, the words shaped smoothly — "
            "and in the careful measuring eyes, just for a "
            "flicker, the unease of a man who suspects the "
            "teacher is holding his own thought up to the "
            "light. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r044-b15", "out": "s15-he-had-been-thinking-it.jpeg", "seg": "n4b",
        "window": "64.18-74.21", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "ROOM"],
        "narration": (
            "Simon, there is something I want to say to you. Say it, teacher, "
            "Simon answered. He had been thinking it, not saying it, and Jesus "
            "answered the thought."
        ),
        "must_show": "the exchange — a two-shot across the table's corner: Jesus and Simon regarding each other; Simon's realization that his unspoken thought has been heard.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the table between them; Simon's composure holding but working at it.",
        "scene": (
            "A two-shot across the table's corner in the "
            "bronze light: Jesus propped easy on his elbow, "
            "regard steady and mild — and Simon upright on "
            "his couch opposite, cup set down now, meeting "
            "the look with his correctness while something "
            "behind his face quietly re-counts everything he "
            "was sure of a minute ago. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b16", "out": "s16-and-instead-of-scolding-anyone.jpeg", "seg": "n5",
        "window": "74.74-78.19", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM"],
        "narration": "And instead of scolding anyone, Jesus told him a small story.",
        "must_show": "the story begun — medium on Jesus settling into the telling, one hand opening; a kindness where the rebuke was expected.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no sternness — a storyteller's ease with a surgeon's purpose.",
        "scene": (
            "A medium shot in the lamplight: Jesus eases up "
            "slightly on the couch and his free hand opens "
            "palm-up into the story's first gesture, his face "
            "gone warm and unhurried — the whole table's "
            "braced expectation of a scolding dissolving into "
            "the older, stranger disarmament of a tale "
            "beginning. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r044-b17", "out": "s17-there-was-a-man-who.jpeg", "seg": "n5",
        "window": "78.19-81.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREDITOR", "LENDER-ROOM"],
        "narration": "There was a man who lent money, and two people owed him.",
        "must_show": "the vignette opens — the money-lender at his daylit counting table, documents on the shelf, the plain honest room of the trade.",
        "must_not_show": "no halo, glare or rim-light; clean working daylight — a told story's plain light, distinct from the dinner's lamplight.",
        "scene": (
            "In plain bright daylight the round shrewd-faced "
            "lender sits at his sturdy table by the window, a "
            "rolled document open under one hand, the wall "
            "shelf behind him ranked with the neighbourhood's "
            "debts — an ordinary honest room where the "
            "arithmetic of owing lives. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b18", "out": "s18-there-was-a-certain-creditor.jpeg", "seg": "j2",
        "window": "82.33-88.32", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREDITOR", "DEBTOR-HEAVY", "DEBTOR-LIGHT", "LENDER-ROOM"],
        "narration": (
            "There was a certain creditor which had two debtors: the one owed "
            "five hundred pence, and the other fifty."
        ),
        "must_show": "SCRIPTURE-EXACT: the two debtors before the table — the gaunt heavy debtor and the trim light one standing before the seated lender; TWO written bills on the table, one long and crowded, one short.",
        "must_not_show": "no halo, glare or rim-light; exactly two debtors, exactly two bills; the difference in the bills' lengths readable at a glance.",
        "scene": (
            "Before the lender's table the two debtors stand "
            "in the window light — the gaunt stooped man in "
            "patched charcoal and the trim uneasy younger one "
            "in dark olive — and on the tabletop between them "
            "lie their two hand-inked bills side by side, one "
            "long and crowded to its foot with entries, the "
            "other a few brief lines, the two unequal weights "
            "written down in plain ink. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b19", "out": "s19-one-of-them-owed-about.jpeg", "seg": "n6",
        "window": "89.77-94.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["LENDER-ROOM"],
        "narration": (
            "One of them owed about two years of wages. The other owed a couple "
            "of months."
        ),
        "must_show": "the weights compared — a close insert of the two bills alone: the long crowded one beside the short one, a coin set on each as a marker; the arithmetic visible.",
        "must_not_show": "no halo, glare or rim-light; no people in frame; dense hand-inked entries, nothing legible as modern text.",
        "scene": (
            "A close insert on the sunlit tabletop: the two "
            "parchment bills lying side by side — the first "
            "crowded top to bottom with cramped hand-inked "
            "entries, its foot nearly black with the sum, the "
            "second carrying its few brief lines and clean "
            "space below — one worn coin set on each as a "
            "marker, two very different weights at rest on "
            "one table. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r044-b20", "out": "s20-very-different-weights-around-their.jpeg", "seg": "n6",
        "window": "94.17-96.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEBTOR-HEAVY", "DEBTOR-LIGHT", "LENDER-ROOM"],
        "narration": "Very different weights around their necks.",
        "must_show": "the weights worn — a two-shot of the debtors: the heavy one bowed as if physically loaded, the light one uneasy but upright; the same trouble at two sizes.",
        "must_not_show": "no halo, glare or rim-light; posture tells the whole difference — no literal weights, nothing theatrical.",
        "scene": (
            "A two-shot in the window light: the gaunt elder "
            "debtor stands bowed under his sum as under a "
            "loaded yoke, hollow eyes down on the table's "
            "edge — while beside him the younger man holds "
            "himself upright but keeps turning his cap in his "
            "hands, uneasy — the same trouble worn at two "
            "utterly different sizes. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b21", "out": "s21-but-the-same-problem-neither.jpeg", "seg": "n6",
        "window": "96.71-102.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEBTOR-HEAVY", "DEBTOR-LIGHT"],
        "narration": (
            "But the same problem: neither of them had a single coin left to "
            "pay it back."
        ),
        "must_show": "the emptiness — a close insert: both debtors' hands opened empty over the table, four bare palms; nothing in them at all.",
        "must_not_show": "no halo, glare or rim-light; hands only carry the beat — four empty palms, no coins anywhere near them.",
        "scene": (
            "Close over the table's edge: two pairs of hands "
            "opened palm-up in the window light — the gaunt "
            "man's cracked and work-hardened, the young man's "
            "smoother but just as bare — four empty palms "
            "held out over the written sums, the one answer "
            "both bills get, offered in the only currency "
            "left. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r044-b22", "out": "s22-and-when-they-had-nothing.jpeg", "seg": "j3",
        "window": "103.14-107.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREDITOR", "DEBTOR-HEAVY", "DEBTOR-LIGHT", "LENDER-ROOM"],
        "narration": "And when they had nothing to pay, he frankly forgave them both.",
        "must_show": "SCRIPTURE-EXACT: the tearing — the lender TEARING the two bills across in his own hands before the two stunned debtors; the debt dying in daylight.",
        "must_not_show": "no halo, glare or rim-light; the tear mid-act, both bills; the lender's face kind and matter-of-fact, not theatrical.",
        "scene": (
            "At his table the round lender has taken up both "
            "bills together and is tearing them across in his "
            "own two hands — the parchment halves parting "
            "mid-frame in the window light — while before the "
            "table the two debtors stand caught in the first "
            "instant of not believing it, the gaunt man's "
            "mouth opening, the young one gone perfectly "
            "still. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r044-b23", "out": "s23-tell-me-therefore-which-of.jpeg", "seg": "j3",
        "window": "107.00-111.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM"],
        "narration": "Tell me therefore, which of them will love him most?",
        "must_show": "back at the dinner — close on Jesus putting the question to Simon, one brow lifted, the story become a mirror mid-sentence.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the question friendly on its surface and inescapable underneath.",
        "scene": (
            "Back in the bronze lamplight of the dining room: "
            "Jesus turns the story's end toward his host with "
            "one brow lifted and his open hand tipping the "
            "question across the table — a riddle so mild and "
            "so aimed that the room's murmur dies around it "
            "while it hangs. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r044-b24", "out": "s24-i-suppose-that-he-to.jpeg", "seg": "s43",
        "window": "112.73-115.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON"],
        "narration": "I suppose that he, to whom he forgave most.",
        "must_show": "SCRIPTURE-EXACT: the careful answer — close on Simon giving it slowly, hearing the trap close gently as he says it.",
        "must_not_show": "no halo, glare or rim-light; reluctance in the correctness — a man answering rightly against his own position.",
        "scene": (
            "Close on Simon in the lamplight: the answer "
            "coming out of him slowly and correctly, each "
            "word placed like a man stepping on stones he "
            "suspects are loose — and in the careful eyes, "
            "arriving exactly as he finishes, the first "
            "understanding of what he has just agreed to. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r044-b25", "out": "s25-thou-hast-rightly-judged.jpeg", "seg": "j3b",
        "window": "116.97-118.73", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM"],
        "narration": "Thou hast rightly judged.",
        "must_show": "SCRIPTURE-EXACT: the verdict returned — close on Jesus's small nod; the judge judged correctly by his own mouth.",
        "must_not_show": "no halo, glare or rim-light on Jesus; warmth, not triumph — the nod of a teacher whose pupil has just graded himself.",
        "scene": (
            "Close on Jesus's face as he gives the small "
            "nod: no triumph anywhere in it, only a warm "
            "level acknowledgment with the whole rest of the "
            "lesson standing quietly behind his eyes, "
            "waiting — a teacher receiving the right answer "
            "from a man who does not yet know the question "
            "was about him. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r044-b26", "out": "s26-to-forgive-them-frankly-meant.jpeg", "seg": "n7",
        "window": "120.25-127.72", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREDITOR", "DEBTOR-HEAVY", "LENDER-ROOM"],
        "narration": (
            "To forgive them frankly meant he simply let it go. He did not "
            "lower the payments. He tore both debts up and asked for nothing "
            "back."
        ),
        "must_show": "the release landed — the vignette again: the torn halves falling to the floor, and the HEAVY debtor's face breaking into stunned tearful relief; the parable's mirror of the woman.",
        "must_not_show": "no halo, glare or rim-light; the heavy debtor's relief mirrors the woman's weeping ON PURPOSE — real tears welcome here.",
        "scene": (
            "In the window light the torn parchment halves "
            "flutter loose from the lender's opening hands "
            "toward the floor — and past them the gaunt "
            "heavy debtor's hollow face is coming apart with "
            "relief, tears starting down the worn cheeks, "
            "his knees half-buckling as two years of weight "
            "leave him in one breath — the same breaking, in "
            "another room, that is happening at a couch "
            "across town. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r044-b27", "out": "s27-and-simon-answered-a-little.jpeg", "seg": "n7",
        "window": "127.72-133.72", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "ROOM"],
        "narration": (
            "And Simon answered, a little carefully: I suppose the one who was "
            "let off the most."
        ),
        "must_show": "the answer's echo — the table two-shot again: Simon's guarded face having answered, Jesus listening with the lesson poised.",
        "must_not_show": "no halo, glare or rim-light on Jesus; Simon's care visible — a man aware he is walking into something.",
        "scene": (
            "The two-shot across the table's corner holds: "
            "Simon settled back a careful half-inch with his "
            "answer given, hands folded exactly, watching to "
            "see what it bought — and Jesus regarding him "
            "with the poised stillness of a man holding the "
            "door open on the far side of a bridge his host "
            "has just finished crossing. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b28", "out": "s28-the-one-who-was-carrying.jpeg", "seg": "n7",
        "window": "133.72-139.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEBTOR-HEAVY", "CREDITOR", "LENDER-ROOM"],
        "narration": (
            "The one who was carrying the heavier weight is the one who walks "
            "away loving the most."
        ),
        "must_show": "the love born — the vignette's last frame: the heavy debtor gripping the lender's hand in both of his at the door, unable to speak; gratitude the size of the debt.",
        "must_not_show": "no halo, glare or rim-light; the light debtor may be gone already — this frame belongs to the heavy one's overflowing thanks.",
        "scene": (
            "At the counting room's door the gaunt debtor "
            "has taken the lender's hand in both of his own "
            "and stands bowed over the grip, unable to say "
            "anything at all — the shrewd round face above "
            "the clasped hands gone soft with surprise at "
            "the size of what his tearing made — a man "
            "walking out owing nothing and loving much. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r044-b29", "out": "s29-seest-thou-this-woman.jpeg", "seg": "jv44",
        "window": "139.66-141.09", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "ROOM"],
        "narration": "Seest thou this woman?",
        "must_show": "SCRIPTURE-EXACT: the question with the gesture — Jesus's open hand extended toward the kneeling woman while his face stays on Simon (off-frame); the gesture line unmistakable.",
        "must_not_show": "no halo, glare or rim-light on Jesus; his hand points at HER, his eyes go to the host — the two directions are the beat.",
        "scene": (
            "Jesus's open hand extends toward the woman "
            "kneeling at his feet — the gesture line running "
            "clean from his palm to her bowed head — while "
            "his face is turned the other way up the table "
            "toward his host, asking the question of a man "
            "who has looked at her all evening and never once "
            "seen her. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r044-b30", "out": "s30-thou-gavest-me-no-water.jpeg", "seg": "jv44",
        "window": "141.09-152.43", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": (
            "I entered into thine house, thou gavest me no water for my feet: "
            "but she hath washed my feet with tears, and did wipe them with the "
            "hairs of her head."
        ),
        "must_show": "SCRIPTURE-EXACT: the comparison's evidence — close on his feet: washed clean in streaks by tears and hair where the road dust was; her hair still resting across them.",
        "must_not_show": "no halo, glare or rim-light; the CLEANED feet are the proof — dust gone in tear-washed streaks; reverent, feet and hair only.",
        "scene": (
            "Close on his feet at the couch's end in the "
            "lamplight: the road's grey dust washed away in "
            "long clean streaks, the skin still bright with "
            "tears, her dark loosed hair lying soft across "
            "the ankles where it dried them — the unhired "
            "basin, the unoffered towel, both answered in "
            "full by someone who owned neither. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b31", "out": "s31-thou-gavest-me-no-kiss.jpeg", "seg": "jv44",
        "window": "152.43-160.84", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": (
            "Thou gavest me no kiss: but this woman since the time I came in "
            "hath not ceased to kiss my feet."
        ),
        "must_show": "SCRIPTURE-EXACT: the unceasing kiss — her bowed head pressing a kiss to his foot, reverent and unashamed; the greeting the doorway never gave.",
        "must_not_show": "no halo, glare or rim-light; complete reverence — a penitent's kiss, nothing else; her dignity absolute.",
        "scene": (
            "Her bowed head dips in the lamplight and her "
            "lips press once more to the top of his foot — "
            "the loosed dark hair curtaining her wet face, "
            "her two hands cradling the heel as something "
            "precious — the kiss of greeting this house "
            "withheld at its door, being paid at its floor, "
            "over and over, by the only person in the room "
            "who knows what he is worth. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b32", "out": "s32-my-head-with-oil-thou.jpeg", "seg": "jv44",
        "window": "160.84-167.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["JAR"],
        "narration": (
            "My head with oil thou didst not anoint: but this woman hath "
            "anointed my feet with ointment."
        ),
        "must_show": "SCRIPTURE-EXACT: the emptied jar — a close insert: the small alabaster flask lying open and empty on its side by his feet, the last of the ointment's sheen on the stone.",
        "must_not_show": "no halo, glare or rim-light; no people in frame — the spent jar alone carries the beat; recognizably the locked flask.",
        "scene": (
            "A close insert on the lamplit stone floor: the "
            "small pale alabaster flask lying on its side, "
            "opened neck dark and empty, one last bead of "
            "ointment gathering at its lip — and around it "
            "on the flagstone the faint bright sheen of "
            "everything it held, all of it gone where she "
            "poured it — a bottle-shaped hole where a life's "
            "savings used to be. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b33", "out": "s33-then-jesus-turned-and-looked.jpeg", "seg": "n8",
        "window": "169.26-175.59", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "ROOM"],
        "narration": (
            "Then Jesus turned and looked at the woman, but he kept speaking to "
            "Simon. He set the two of them side by side."
        ),
        "must_show": "THE LOOK — Jesus's face and body turned fully toward the woman, warm, while his words visibly still travel the other way; her face beginning to lift toward his.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the split is the beat — gaze to her, speech to him; her eyes rising for the first time.",
        "scene": (
            "Jesus has turned on the couch to face the "
            "kneeling woman fully, his face gone warm and "
            "wholly hers even as his voice carries on up the "
            "table — and under that look her face is lifting "
            "for the first time since the door, tear-streaked "
            "and disbelieving, like a debtor watching a bill "
            "come apart in a lender's hands. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b34", "out": "s34-simon-had-given-him-no.jpeg", "seg": "n8",
        "window": "175.59-185.89", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SIMON", "GUESTS", "ROOM"],
        "narration": (
            "Simon had given him no water for his feet; she had washed them "
            "with her tears. Simon had given him no greeting; she had not "
            "stopped kissing his feet since she came in."
        ),
        "must_show": "the triangle — one wide frame holding all three: Simon rigid at the table's head, Jesus reclined between, the woman at his feet; the two hospitalities side by side.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the geometry moral — host at one end, penitent at the other, Jesus the measure between them.",
        "scene": (
            "The camera stands at the room's side wall and "
            "holds the whole triangle in profile: Simon "
            "upright and rigid at the table's head with his "
            "correctness around him like armour, Jesus "
            "reclined at the frame's centre, and at the far "
            "couch-end the woman low at his feet with her "
            "loosed hair down — the room's two hospitalities "
            "laid side by side in one look, with every "
            "guest's eyes moving between them. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b35", "out": "s35-her-sins-which-are-many.jpeg", "seg": "j4",
        "window": "186.47-194.08", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM"],
        "narration": (
            "Her sins, which are many, are forgiven; for she loved much: but to "
            "whom little is forgiven, the same loveth little."
        ),
        "must_show": "SCRIPTURE-EXACT: the saying — close on Jesus delivering the verse with full warmth and full authority; the room's centre of gravity.",
        "must_not_show": "no halo, glare or rim-light on Jesus; both halves live in his face — mercy toward her, the quiet edge toward the table.",
        "scene": (
            "Close on Jesus in the bronze light as the great "
            "sentence comes: warmth filling the first half of "
            "it, his eyes soft toward the floor where she "
            "kneels — and then the quiet edge arriving with "
            "the second half, his gaze lifting level toward "
            "the table's correctness, mercy and diagnosis "
            "delivered in one unhurried breath. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b36", "out": "s36-she-was-not-forgiven-because.jpeg", "seg": "n9",
        "window": "195.58-202.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": (
            "Read that slowly, because it is easy to turn it backwards. She was "
            "not forgiven because she loved so much."
        ),
        "must_show": "the order corrected — close on the woman's lifted face: the peace ALREADY in it beneath the tears; forgiveness as the cause, not the prize.",
        "must_not_show": "no halo, glare or rim-light; her face changed from the entrance — same features, the fear gone out of them.",
        "scene": (
            "Close on the woman's lifted face in the "
            "lamplight: the tears still bright on it, but "
            "beneath them the terrible tension of the doorway "
            "has gone — something already settled living "
            "quietly under the weeping, the look of a woman "
            "whose debt was torn up before she ever crossed "
            "this room, and who came because of it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b37", "out": "s37-the-tears-were-not-the.jpeg", "seg": "n9",
        "window": "202.76-208.34", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": (
            "She loved so much because she had already been forgiven. The tears "
            "were not the payment."
        ),
        "must_show": "the tears re-read — at his feet again: her hands resting quiet now on the washed feet, the weeping easing into stillness; gratitude, not purchase.",
        "must_not_show": "no halo, glare or rim-light; the storm passing — quieter hands, slower tears; nothing transactional in the frame.",
        "scene": (
            "At the couch's end her two hands have gone "
            "quiet, resting lightly on the washed feet, and "
            "the weeping has eased into long slow breaths — "
            "the storm of it passing through her into "
            "stillness, the way sobbing ends when the news "
            "is finally believed — payment nowhere in the "
            "picture, only thanks with nowhere big enough to "
            "put itself. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r044-b38", "out": "s38-they-were-what-it-looks.jpeg", "seg": "n9",
        "window": "208.34-213.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["LENDER-ROOM"],
        "narration": (
            "They were what it looks like when a debt you could never repay is "
            "torn up right in front of you."
        ),
        "must_show": "the visual rhyme — the vignette's insert one last time: the torn halves of the LONG bill lying on the counting-room floor in the window light.",
        "must_not_show": "no halo, glare or rim-light; no people — the torn long bill alone; its crowded entries visibly cancelled by the tear.",
        "scene": (
            "A quiet insert in the counting room's window "
            "light: the two torn halves of the long crowded "
            "bill lying where they fell on the plank floor, "
            "the dense entries sheared mid-line by the tear, "
            "a little dust already settling on them — paper "
            "that owned a man this morning, litter by noon. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r044-b39", "out": "s39-simon-loved-little-because-he.jpeg", "seg": "n9",
        "window": "213.01-216.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON", "ROOM"],
        "narration": "Simon loved little, because he believed he owed little.",
        "must_show": "the small accounting — close on Simon's face gone inward: not villainy, the sealed self-sufficiency of a man sure his own bill is short.",
        "must_not_show": "no halo, glare or rim-light; no sneer — the quiet tragedy of small arithmetic; his correctness intact and costing him everything.",
        "scene": (
            "Close on Simon in the lamplight: the correct "
            "face gone inward and still, the measuring eyes "
            "for once measuring their owner — and finding, "
            "visibly, only a short bill, a small sum, "
            "nothing worth weeping over — a man armoured in "
            "the smallness of what he thinks he owes, "
            "loving exactly that much. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b40", "out": "s40-thy-sins-are-forgiven.jpeg", "seg": "jv48",
        "window": "217.40-219.07", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "ROOM"],
        "narration": "Thy sins are forgiven.",
        "must_show": "SCRIPTURE-EXACT: said TO HER — a two-shot: Jesus speaking it directly to the woman's lifted face, plain and public.",
        "must_not_show": "no halo, glare or rim-light on Jesus; directness — his words to her, not about her, for the first time in the room.",
        "scene": (
            "A close two-shot in the lamplight: Jesus's face "
            "turned full upon the woman's lifted one, the "
            "three words leaving him plainly, unhurried, "
            "spoken not over her head to the table but "
            "straight into her eyes — the first sentence "
            "anyone in this town has aimed at her, rather "
            "than at what she was. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b41", "out": "s41-he-said-it-out-loud.jpeg", "seg": "n9b",
        "window": "220.61-229.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON", "GUESTS", "ROOM"],
        "narration": (
            "He said it out loud, at a full table, in front of every important "
            "man in that town, to the one person in the room everybody there "
            "had already written off."
        ),
        "must_show": "the room's shock — the guests' faces around the table: cups stopped mid-air, the murmur beginning ('who is this?'); Simon's face caught between offense and the crack.",
        "must_not_show": "no halo, glare or rim-light; varied real reactions — offense, astonishment, one thoughtful face; never a uniform row of gasps.",
        "scene": (
            "Along the lamplit table the sentence detonates "
            "quietly: the white-bearded elder's cup stopped "
            "halfway to his mouth, the sharp scribe already "
            "leaning to his neighbour with the first hot "
            "whisper, the ringed merchant's brows in his "
            "hairline — and at the table's head Simon's "
            "correct face holding very still around "
            "something newly and deeply unsettled. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b42", "out": "s42-thy-faith-hath-saved-thee.jpeg", "seg": "j5",
        "window": "230.31-233.01", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "ROOM"],
        "narration": "Thy faith hath saved thee; go in peace.",
        "must_show": "SCRIPTURE-EXACT: the sending — close on Jesus giving her the dismissal-blessing, his hand open toward the door she came in by; permission to leave whole.",
        "must_not_show": "no halo, glare or rim-light on Jesus; 'go in peace' is a gift, not a dismissal — full warmth, the open hand gentle.",
        "scene": (
            "Close on Jesus as the blessing comes, his open "
            "hand turning gently toward the courtyard door "
            "at the room's end — the same door she entered "
            "by — his face holding hers with the settled "
            "warmth of a finished gift: saved already, at "
            "peace already, free now to walk out through "
            "the very room that watched her crawl in. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b43", "out": "s43-she-came-in-as-the.jpeg", "seg": "n10",
        "window": "234.53-240.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "GUESTS", "ROOM"],
        "narration": (
            "She came in as the woman everybody had already judged. She walked "
            "out saved, and at peace, and loved."
        ),
        "must_show": "the exit — from behind her: the woman walking upright toward the open courtyard door, the staring table to her side unable to touch her now; the empty jar left behind at the couch.",
        "must_not_show": "no halo, glare or rim-light; she walks TOWARD the door which is in frame; upright, unhurried — changed posture from her entrance.",
        "scene": (
            "From behind her the camera watches the woman "
            "cross the room the other way: spine straight "
            "now, steps unhurried, her shawl settled evenly "
            "on both shoulders, walking toward the open "
            "courtyard door at the frame's end while the "
            "table's stares slide off her like rain — and "
            "back at the couch's foot, small in the "
            "lamplight, the empty alabaster flask stays "
            "where her old life set it down. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b44", "out": "s44-and-here-is-the-quiet.jpeg", "seg": "n10",
        "window": "240.73-249.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON", "ROOM"],
        "narration": (
            "And here is the quiet danger in Simon's seat at the table. If you "
            "are sure you are only a small sinner, you will only ever be a "
            "small lover of God."
        ),
        "must_show": "the danger seated — Simon alone at his correct table's head after her exit, the untouched water jar and basin still visible by the threshold; everything in order, everything small.",
        "must_not_show": "no halo, glare or rim-light; the unused jar and basin MUST be in frame — the evening's whole indictment standing quietly by the door.",
        "scene": (
            "Simon sits at the head of his immaculate table "
            "in the settling lamplight, hands folded, "
            "everything about the evening still perfectly in "
            "order — and past his shoulder, by the doorway, "
            "the tall water jar and its clean dry basin "
            "stand exactly where they stood all night, "
            "untouched, unoffered, unneeded in a house where "
            "nothing was ever supposed to be owed. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b45", "out": "s45-but-let-yourself-be-the.jpeg", "seg": "n10",
        "window": "249.67-255.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": (
            "But let yourself be the one forgiven much, and you get to be the "
            "one who loves much."
        ),
        "must_show": "the alternative walking — the woman outside in the early night, the courtyard lamp behind her, walking home light; the first easy breath of the forgiven-much.",
        "must_not_show": "no halo, glare or rim-light; night, one warm courtyard lamp — natural light only; her face at peace, not ecstatic.",
        "scene": (
            "Outside in the blue early night the woman walks "
            "away from the house's warm courtyard lamp, her "
            "face lifted into the cool air with her eyes "
            "half-closing over the first entirely easy "
            "breath she has taken in years — a debtor on "
            "the road home from a torn-up bill, carrying "
            "nothing at all, and rich. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r044-b46", "out": "s46-that-was-never-the-punishment.jpeg", "seg": "n10",
        "window": "255.01-258.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["JAR", "ROOM"],
        "narration": "That was never the punishment. That is the gift.",
        "must_show": "the closing image — the empty alabaster jar alone in the lamplight where she left it at the couch's foot; the poured-out gift, at rest.",
        "must_not_show": "no halo, glare or rim-light; no people in frame; the locked flask, open and empty, its faint sheen the last light in the story.",
        "scene": (
            "A last quiet insert at the couch's foot: the "
            "small pale alabaster flask standing empty in "
            "the low lamplight, its broken-open neck dark, "
            "the faint sheen of the poured ointment still "
            "warming the stone around it — everything it "
            "held given away, everything it meant left "
            "standing in the quiet room like a small "
            "monument to the mathematics of much. Every "
            "figure has two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
}
# === end PLACE-PLATES ===
