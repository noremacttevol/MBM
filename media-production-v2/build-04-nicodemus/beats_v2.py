#!/usr/bin/env python3
"""V2 beat map — row 4, build-04-nicodemus (John 3:1-21, 7:50-51, 19:39-40).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE (STORY-COVERAGE-LAW): 30 pictures over 327s = ~10.9s of narration per
picture, which is LESS dense than row 3 (8.5s). The story is more than twice row 2's
length and spans three separate occasions months apart. The narration decided the
count.

THE VISUAL SPINE — this is the whole point of the episode and the pictures carry it:
**Nicodemus begins in the DARK and ends in broad DAYLIGHT.** The narration says it
outright ("you won't always have to come at night" / "was starting to speak in the
light" / "gave him a king's burial in the open"). So the lighting is not decoration
here, it is the argument:
  b04-b28  NIGHT — lamplight, deep shadow, a single flame, the dark street
  b28      DAWN  — the hinge; he leaves as the first grey light comes
  b29-b34  FULL DAYLIGHT — the council, and the tomb. No lamps, nothing hidden.
Never light a night beat like day, and never put a lamp in the daylight beats.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (KJV):
  3:1    a man of the PHARISEES, a RULER OF THE JEWS — Sanhedrin, wealth, standing.
  3:2    the same came to Jesus BY NIGHT. "Rabbi, WE know" — plural, deliberate.
  3:3    Except a man be BORN AGAIN, he cannot SEE the kingdom of God.
  3:4    How can a man be born WHEN HE IS OLD? He is an old man; show it.
  3:8    the WIND bloweth where it listeth, and thou HEAREST THE SOUND thereof, but
         canst not TELL WHENCE it cometh. Wind is invisible — never draw the wind.
         Show only what it MOVES: the flame leaning, the curtain, the trees.
  3:9    How can these things be?
  3:16-17 said to ONE MAN IN A ROOM, not to a crowd. Never stage it as preaching.
  3:19-21 light and darkness — spoken TO a man who came in the dark. Not a rebuke.
  7:50-51 he speaks up in the COUNCIL, in session, in daylight.
  19:39-40 he brought MYRRH AND ALOES, ABOUT AN HUNDRED POUND WEIGHT — an enormous,
         visibly heavy quantity, fit for a king. It must READ as a huge amount.

CONTENT-CARE: row 4 is not in the §3 flag table = GREEN. Restraint applied anyway:
the burial is handled with reverence and distance — wrapped linen and spices, no
wounds, no body shown in detail, nothing dwelt on.

CAMERA LAW (row 2 paid for this): every travelling / watching / arriving beat states
where the lens is and which way the figure faces, or the model composes hero-shots
facing the camera and the geography inverts.
"""

LOCKS = {
    # Nicodemus ages slightly across months but must stay the SAME man; his lock
    # carries face and build, and each beat states the garment, because the story
    # moves him from a night cloak to council robes to working clothes at the tomb.
    "NICO": (
        "NICODEMUS LOCK: Nicodemus is the same man in every shot — a Middle Eastern "
        "Jewish man of about sixty-five, tall and spare with a scholar's stoop, a "
        "long well-kept grey-white beard, deep-set intelligent tired eyes, a high "
        "lined forehead and thinning white hair. A dignified, careful, weary face. "
        "He is a wealthy man and his clothing is always finely woven and DEEPLY "
        "DYED — never cream, never off-white, never pale. His face is shown clearly."
    ),
    "NIGHTROOM": (
        "NIGHT ROOM LOCK: a plain upper room in Jerusalem at night — bare plastered "
        "stone walls, a low wooden table, a woven floor mat, a single small clay oil "
        "lamp giving all the light in the room so that the corners stay in deep "
        "shadow, and one open window with a dark blue night sky and rooftops beyond "
        "it. The room is modest and quiet. It is unmistakably the middle of the "
        "night."
    ),
    # A setting lock NEVER names a character (the STRAY-JESUS defect, row 1).
    "COUNCIL": (
        "COUNCIL LOCK: the chamber of the ruling council in Jerusalem in full "
        "daylight — a half-round of tiered stone benches under a high beamed "
        "ceiling, tall windows pouring hard bright daylight across the floor, no "
        "lamps lit anywhere. The councillors are elderly and middle-aged men in "
        "SATURATED DEEP scholarly robes — dark charcoal, deep umber, dark indigo "
        "and near-black wool with dark-toned fringed prayer shawls, every garment "
        "plainly DARKER than the sunlit stone walls behind them. No councillor "
        "wears cream, off-white, ivory or any pale near-white cloth."
    ),
    "JERUSALEM": (
        "JERUSALEM LOCK: the old city — narrow stepped streets of pale dressed "
        "limestone, heavy wooden doors, flat roofs and low parapets, the great "
        "temple platform rising beyond the rooftops, dry hills past the walls."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r004-b01", "out": "s01-a-ruler-of-the-jews.jpeg", "seg": "n0 p1",
        "window": "0.28-9.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["NICO", "COUNCIL"],
        "narration": ("In Jerusalem there was a man named Nicodemus. He was a "
                      "Pharisee, and more than that — a ruler of the Jews,"),
        "must_show": "3:1 — Nicodemus seated among the ruling council in daylight, plainly one of its senior men.",
        "must_not_show": "no night, no lamps — this is his public daytime world; nothing furtive yet.",
        "scene": (
            "In the council chamber in hard bright daylight, Nicodemus sits high on "
            "the tiered stone benches among the other councillors in a fine DEEP "
            "INDIGO robe with a dark woven border, an unrolled scroll across his "
            "knees, listening to the debate with the settled authority of a man who "
            "has sat in that seat for thirty years. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r004-b02", "out": "s02-educated-respected.jpeg", "seg": "n0 p2",
        "window": "9.0-16.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["NICO", "COUNCIL"],
        "narration": "a member of the great council that governed the nation's faith. Educated. Respected. Listened to.",
        "must_show": "the room deferring to him — he speaks and the others attend.",
        "must_not_show": "no arrogance; this is earned, quiet standing.",
        "scene": (
            "Nicodemus is on his feet in the sunlit council chamber, one hand raised "
            "in a measured scholar's gesture, mid-argument — and every councillor on "
            "the benches around him has turned toward him and gone quiet to listen, "
            "several nodding. He is entirely at home here. Hard bright daylight from "
            "the tall windows. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b03", "out": "s03-everything-to-lose.jpeg", "seg": "n0 p3",
        "window": "16.0-23.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["NICO", "JERUSALEM"],
        "narration": ("A man like that had everything to lose by being seen with a "
                      "controversial teacher from Galilee. His seat, his standing, "
                      "his name."),
        "must_show": "the private weighing of the cost — alone, thinking, at the end of the day.",
        "must_not_show": "nobody else in the frame; this is the decision forming.",
        "scene": (
            "Close on Nicodemus standing alone at a window in the last orange light "
            "of evening, still in his fine deep indigo robe, looking out over the "
            "Jerusalem rooftops with his brow drawn and his jaw set — a careful man "
            "doing arithmetic he does not like the answer to. Exactly one person is "
            "in the frame, with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b04", "out": "s04-so-he-came-at-night.jpeg", "seg": "n1",
        "window": "24.18-25.25", "wide": True, "jesus": False, "ref": False,
        "locks": ["NICO", "JERUSALEM"],
        "narration": "So he came at night.",
        "must_show": "3:2 — a lone hooded figure moving through the dark city; the whole point is the dark.",
        "must_not_show": "his face is mostly hidden here; no moon bright enough to expose him.",
        "scene": (
            "SHOT FROM BEHIND AND ABOVE, looking down a narrow stepped Jerusalem "
            "street deep in night: one solitary figure in a heavy dark hooded cloak "
            "walks away from the camera down the middle of the empty street, his "
            "back to us and his face hidden, keeping close to the wall. A single "
            "shuttered window leaks a thin line of lamplight across the stones. "
            "Everything else is deep blue-black shadow. Exactly one person is in the "
            "frame, with two arms, two legs and one head."
        ),
    },
    {
        "id": "v2-r004-b05", "out": "s05-knocked-in-the-dark.jpeg", "seg": "n2",
        "window": "26.25-30.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["NICO", "JERUSALEM"],
        "narration": "He knocked on the door in the dark, and the first thing he said was this.",
        "must_show": "the knock — his hand on a heavy door at night, hood back just enough to show the old face.",
        "must_not_show": "the door is still shut; nobody has answered yet.",
        "scene": (
            "Close on Nicodemus at a heavy wooden door at night, his hood pushed "
            "back just far enough to show his grey-white beard and his deep-set "
            "eyes, one fist raised against the timber mid-knock, the other hand "
            "gathering his dark cloak at his throat. He is glancing back over his "
            "shoulder down the empty street. The only light is a thin warm line of "
            "lamplight leaking from the crack under the door. Exactly one person is "
            "in the frame, with "
            "two arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r004-b06", "out": "s06-rabbi-we-know.jpeg", "seg": "s2",
        "window": "31.14-38.50", "wide": True, "jesus": True, "ref": REF,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("Rabbi, we know that thou art a teacher come from God: for no "
                      "man can do these miracles that thou doest, except God be with "
                      "him. (John 3:2)"),
        "must_show": "3:2 — the two men meeting at last, by lamplight; the careful opening speech.",
        "must_not_show": "no halo, glow or rim-light; the lamp is the only light source.",
        "scene": (
            "Inside the small upper room by the light of the single clay lamp, "
            "Nicodemus stands just inside the doorway with his dark hood pushed back "
            "onto his shoulders, speaking his careful opening words with one hand "
            "half-raised — and Jesus stands facing him a few feet away, listening "
            "without any hurry, entirely unsurprised to have a councillor at his "
            "door at midnight. Deep shadow in the corners of the room. Exactly two "
            "people are in the frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b07", "out": "s07-we-not-i.jpeg", "seg": "n2b p1",
        "window": "39.98-49.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["COUNCIL"],
        "narration": ("Bible students notice one small word there — we. Not I. We "
                      "know. Nicodemus had been talking with other rulers, quietly, "
                      "behind closed doors."),
        "must_show": "the private conversations the word 'we' implies — rulers talking low, apart, out of the public eye.",
        "must_not_show": "Nicodemus is NOT in this frame; these are the others. No night-room lamp — this is a shuttered daytime room.",
        "scene": (
            "In a shuttered side room off the council chamber, three elderly "
            "councillors stand close together in the barred stripes of daylight "
            "coming through the shutters, heads bent in low urgent conversation, one "
            "with a hand raised for quiet and another glancing at the closed door. "
            "Everyone in this frame is an ordinary member of the council. Exactly "
            "three people are in the frame; each has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r004-b08", "out": "s08-not-in-daylight.jpeg", "seg": "n2b p2",
        "window": "49.0-58.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("Some of the very men who opposed Jesus in public already "
                      "believed it in private. He just couldn't say it in daylight."),
        "must_show": "the cost of that on his face — belief he cannot afford to own publicly.",
        "must_not_show": "no shame played big; it is quieter and sadder than that.",
        "scene": (
            "Close on Nicodemus's face in the small upper room, lit from below and "
            "to one side by the single clay lamp so that half of him stays in "
            "shadow, his eyes lowered and his mouth set — an old man who knows "
            "exactly what he believes and exactly what it would cost him to say so "
            "in the street. Exactly one person is in the frame, with two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r004-b09", "out": "s09-he-didnt-turn-him-away.jpeg", "seg": "n3a",
        "window": "59.88-71.63", "wide": True, "jesus": True, "ref": REF,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("And Jesus didn't turn him away for coming at night. He didn't "
                      "point out the fear."),
        "must_show": "welcome — Jesus gesturing him to sit, treating a midnight visit as entirely normal.",
        "must_not_show": "no reproach whatsoever in his posture or face.",
        "scene": (
            "By the single lamp in the upper room, Jesus has turned and is gesturing "
            "with an open hand toward the mat and the low table, inviting the old man "
            "to sit down, his face easy and welcoming — and Nicodemus is just "
            "beginning to lower himself onto the mat, still holding his dark cloak "
            "around him, watching Jesus with cautious surprise at being received so "
            "simply. Deep shadow beyond the lamplight. Exactly two people are in the "
            "frame; each has two arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r004-b10", "out": "s10-born-again.jpeg", "seg": "j1",
        "window": "72.63-78.98", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NIGHTROOM"],
        "narration": ("Verily, verily, I say unto thee, Except a man be born again, "
                      "he cannot see the kingdom of God. (John 3:3)"),
        "must_show": "3:3 — Jesus saying the sentence; complete directness, no hedging.",
        "must_not_show": "no halo/glow; warm lamplight on one side of his face only.",
        "scene": (
            "Close on Jesus seated at the low table in the upper room, lit warmly "
            "from one side by the single clay lamp, looking directly across at his "
            "guest and speaking with quiet absolute certainty, one hand resting open "
            "on the table between them. His face is serious and kind. The rest of "
            "the room falls away into darkness. Exactly one person is in the frame, "
            "with two arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r004-b11", "out": "s11-the-words-land.jpeg", "seg": "n3b p1",
        "window": "80.46-91.0", "wide": False, "jesus": False, "ref": False,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("And notice who heard it first. Not a hardened sinner. The "
                      "most religious man in the country."),
        "must_show": "the sentence landing on the one man who assumed it could not be aimed at him.",
        "must_not_show": "not offence — bewilderment.",
        "scene": (
            "Close on Nicodemus across the low table in the lamplight, absolutely "
            "still, his careful scholar's composure faltering — brows drawn, eyes "
            "searching the middle distance as he turns the sentence over and finds "
            "no place to put it. Exactly one person is in the frame, with two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b12", "out": "s12-everyone-starts-over.jpeg", "seg": "n3b p2",
        "window": "91.0-101.18", "wide": True, "jesus": True, "ref": REF,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("Jesus was telling him that all his learning and all his "
                      "rule-keeping could not do it. Everyone has to start over. "
                      "Everyone."),
        "must_show": "the two of them level with each other across the table — a scholar and a carpenter, no platform.",
        "must_not_show": "Jesus is not standing over him or lecturing; they are seated at the same height.",
        "scene": (
            "A wider view of the small upper room: the two men sit facing each other "
            "across the low table at exactly the same height, the single clay lamp "
            "burning between them, the whole rest of the room in deep night shadow. "
            "Jesus is speaking quietly with one open hand turned upward; Nicodemus "
            "listens with his hands loose in his lap and his scrolls forgotten "
            "beside him. Exactly two people are in the frame; each has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r004-b13", "out": "s13-took-it-literally.jpeg", "seg": "n4",
        "window": "102.18-103.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": "Nicodemus took it literally.",
        "must_show": "the moment of literal-minded confusion on an old scholar's face.",
        "must_not_show": "he is not stupid; he is a specialist hitting a wall.",
        "scene": (
            "Very close on Nicodemus in the lamplight, head tipped slightly, one "
            "hand lifted mid-thought with the fingers half-curled, his mouth open on "
            "the beginning of an objection — the face of a lifelong expert who has "
            "just been handed something that will not fit his categories. Exactly "
            "one person is in the frame, with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b14", "out": "s14-when-he-is-old.jpeg", "seg": "s4",
        "window": "104.45-110.83", "wide": True, "jesus": False, "ref": False,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("How can a man be born when he is old? can he enter the second "
                      "time into his mother's womb, and be born? (John 3:4)"),
        "must_show": "3:4 — the question asked out loud, both palms open; his own age is the point of it.",
        "must_not_show": "no mockery in his tone; he genuinely wants an answer.",
        "scene": (
            "Nicodemus leans forward into the lamplight with both weathered old "
            "hands turned open in front of him, mid-question, his grey-white beard "
            "and lined face fully lit — an old man asking, quite sincerely, how a "
            "man his age could possibly begin again. Deep shadow behind him. Exactly "
            "one person is in the frame, with two arms, two hands of five fingers "
            "each and one head."
        ),
    },
    {
        "id": "v2-r004-b15", "out": "s15-he-didnt-shame-him.jpeg", "seg": "n4b",
        "window": "112.31-124.86", "wide": True, "jesus": True, "ref": REF,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("And Jesus didn't laugh at him. He didn't shame him for not "
                      "getting it. He reached for something Nicodemus could feel — "
                      "the night wind moving outside the window."),
        "must_show": "Jesus turning toward the open window to reach for the illustration; patience, not correction.",
        "must_not_show": "no wind drawn as swirls or streaks — wind is invisible; only its effects.",
        "scene": (
            "In the lamplit upper room Jesus has half-turned on the mat toward the "
            "open window, one hand lifted toward the dark outside, his face warm and "
            "unhurried as he reaches for something simpler to explain it with — and "
            "Nicodemus follows his gesture, turning to look at the window too. "
            "Through it: night sky and rooftops. Exactly two people are in the "
            "frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b16", "out": "s16-the-wind-bloweth.jpeg", "seg": "j2",
        "window": "125.86-136.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["NIGHTROOM"],
        "narration": ("The wind bloweth where it listeth, and thou hearest the sound "
                      "thereof, but canst not tell whence it cometh, and whither it "
                      "goeth: so is every one that is born of the Spirit. (John 3:8)"),
        "must_show": "3:8 — ONLY what the wind moves: the lamp flame leaning, the curtain lifting, leaves stirring outside.",
        "must_not_show": "NEVER draw the wind itself — no swirls, streaks, spirals or visible gusts. No people in this frame.",
        "scene": (
            "A quiet close view of the open window of the upper room at night with "
            "no person in the frame at all: a plain woven curtain lifts and bellies "
            "inward off the sill, the small clay lamp on the table beside it has its "
            "flame bent hard sideways, and beyond the window the black silhouettes "
            "of olive branches lean all one way against a deep blue night sky. "
            "Nothing else moves. The air itself is completely invisible."
        ),
    },
    {
        "id": "v2-r004-b17", "out": "s17-you-can-watch-a-life-bend.jpeg", "seg": "n5",
        "window": "138.35-152.62", "wide": True, "jesus": True, "ref": REF,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("You can't see the wind. You only see what it moves. That, "
                      "Jesus said, is how God changes a person. But you can watch a "
                      "life bend."),
        "must_show": "the illustration landing — Nicodemus looking from the leaning flame back to Jesus.",
        "must_not_show": "no visible wind; the flame and curtain do all the work.",
        "scene": (
            "In the upper room the lamp flame is still leaning from the draught, and "
            "Nicodemus has turned back from the window to look at Jesus with "
            "something opening in his face — the first crack in sixty-five years of "
            "certainty. Jesus watches him steadily across the low table, saying "
            "nothing more, letting it work. Exactly two people are in the frame; "
            "each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b18", "out": "s18-something-gave-way.jpeg", "seg": "n6",
        "window": "153.62-167.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("And something in Nicodemus gave way. The formal questions of "
                      "a scholar were falling away — until what was left was just a "
                      "man in the lamplight."),
        "must_show": "the defences coming down — posture loosening, the official gone, a tired old man left.",
        "must_not_show": "no weeping; this is quieter — the moment a man stops arguing.",
        "scene": (
            "Close on Nicodemus in the lamplight with his shoulders come down out of "
            "their careful set, his dark cloak slipped off one shoulder and forgotten "
            "and his hands loose and open on his knees, looking across the table with "
            "nothing left in his face but plain want. He looks his full age here. "
            "Exactly one person is in the frame, with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b19", "out": "s19-how-can-these-things-be.jpeg", "seg": "s9",
        "window": "168.50-169.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": "How can these things be? (John 3:9)",
        "must_show": "3:9 — the shortest, most honest question in the conversation.",
        "must_not_show": "no gesture, no scholarship; just a face asking.",
        "scene": (
            "A tight shot of Nicodemus's face in the warm lamplight, mid-word, "
            "looking directly across at the man opposite him with his brows raised "
            "and his eyes tired and completely undefended — an old man asking a "
            "simple question with nothing behind it but wanting to know. Exactly one "
            "person is in the frame, with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b20", "out": "s20-a-tired-honest-man.jpeg", "seg": "n6b",
        "window": "171.28-178.13", "wide": True, "jesus": True, "ref": REF,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("No title on it. No argument behind it. Just a tired, honest "
                      "man finally asking what he actually wanted to know."),
        "must_show": "the two of them close in the small ring of lamplight; every title gone.",
        "must_not_show": "no scrolls, no props of office left in play.",
        "scene": (
            "A quiet wide view of the upper room from across the low table: the two "
            "men sit close together inside the small ring of light the single clay "
            "lamp throws, everything beyond them lost in night, Nicodemus's fine "
            "robe crumpled and his posture ordinary. Jesus leans in a little toward "
            "him. It looks like two men talking, not a rabbi and a ruler. Exactly "
            "two people are in the frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b21", "out": "s21-and-then-jesus-said.jpeg", "seg": "n7a",
        "window": "179.13-183.58", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NIGHTROOM"],
        "narration": "And then Jesus said the words. The ones the whole world would come to know.",
        "must_show": "the breath before the most quoted sentence in the Bible.",
        "must_not_show": "nothing grand; he is about to say it to one man in a small room.",
        "scene": (
            "Close on Jesus in the lamplight, quite still, his eyes steady on the man "
            "across the table and his lips just parting to speak. His expression is "
            "grave and full of tenderness. The dark room is silent around him. "
            "Exactly one person is in the frame, with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b22", "out": "s22-for-god-so-loved.jpeg", "seg": "j3 p1",
        "window": "184.58-194.0", "wide": True, "jesus": True, "ref": REF,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("For God so loved the world, that he gave his only begotten "
                      "Son, that whosoever believeth in him should not perish, but "
                      "have everlasting life. (John 3:16)"),
        "must_show": "3:16 — said across a table to one man, by one lamp. The intimacy IS the point.",
        "must_not_show": "no crowd, no platform, no preaching posture, no halo/glow.",
        "scene": (
            "The two men face each other across the low table in the small ring of "
            "lamplight, Jesus speaking with both hands open and low in front of him "
            "and his whole attention on the one man opposite, Nicodemus utterly "
            "still with his eyes fixed on him. Deep night shadow presses in on every "
            "side of the little pool of light. Exactly two people are in the frame; "
            "each has two arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r004-b23", "out": "s23-not-to-condemn.jpeg", "seg": "j3 p2",
        "window": "194.0-203.62", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NIGHTROOM"],
        "narration": ("For God sent not his Son into the world to condemn the world; "
                      "but that the world through him might be saved. (John 3:17)"),
        "must_show": "3:17 — the sentence that takes the threat out of it; open hands, no judgement.",
        "must_not_show": "no pointing finger, nothing forensic in the gesture.",
        "scene": (
            "Close on Jesus at the low table in warm lamplight, both hands turned "
            "palm-upward and open in front of him, his face earnest and free of any "
            "severity at all as he says it — the look of a man clearing away a "
            "misunderstanding that has hurt people for a long time. Exactly one "
            "person is in the frame, with two arms, two hands of five fingers each "
            "and one head."
        ),
    },
    {
        "id": "v2-r004-b24", "out": "s24-one-scared-man.jpeg", "seg": "n7b",
        "window": "205.10-211.30", "wide": True, "jesus": True, "ref": REF,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("Those words weren't preached to a stadium. They were said "
                      "quietly, at night, to one scared man who came with questions."),
        "must_show": "the smallness of the room — the scale of the setting against the size of the words.",
        "must_not_show": "no grandeur anywhere; a bare little room and one lamp.",
        "scene": (
            "SHOT FROM THE FAR DARK CORNER OF THE ROOM, wide, so the whole plain "
            "little upper room is visible with its bare plaster walls and empty "
            "floor — and the two seated men and their single clay lamp are a small "
            "warm island of light in the middle of all that darkness. The window "
            "shows black night beyond. Exactly two people are in the frame; each has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b25", "out": "s25-light-and-darkness.jpeg", "seg": "n8 p1",
        "window": "212.30-223.0", "wide": True, "jesus": True, "ref": REF,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("Then Jesus spoke about light and darkness — how people hide "
                      "in the dark when they're afraid of what the light will show."),
        "must_show": "the lamp made the subject; the man who came in the dark sitting inside its light.",
        "must_not_show": "not accusatory — the narration insists it was not a jab.",
        "scene": (
            "In the upper room Jesus has turned his open hand toward the small clay "
            "lamp burning on the table between them, speaking gently — and Nicodemus "
            "sits inside the warm circle it throws, his own dark hood lying "
            "discarded behind him, the deep shadow he walked in still filling the "
            "doorway at his back. Exactly two people are in the frame; each has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b26", "out": "s26-an-invitation.jpeg", "seg": "n8 p2",
        "window": "223.0-233.21", "wide": False, "jesus": False, "ref": False,
        "locks": ["NICO", "NIGHTROOM"],
        "narration": ("It wasn't a jab. It was an invitation: you won't always have "
                      "to come at night."),
        "must_show": "the promise landing on his face — hope, not rebuke; lamplight full on him.",
        "must_not_show": "no shame; the light is kind to him here.",
        "scene": (
            "Close on Nicodemus with the lamplight full and warm on his face for the "
            "first time in the whole conversation — no hood, no shadow across his "
            "eyes, his head lifted and his expression caught somewhere between "
            "disbelief and hope as he understands what has just been offered to him. "
            "Exactly one person is in the frame, with two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r004-b27", "out": "s27-came-by-night.jpeg", "seg": "n9",
        "window": "234.21-249.97", "wide": True, "jesus": False, "ref": False,
        "locks": ["NICO", "JERUSALEM"],
        "narration": ("Every time John's gospel mentions Nicodemus again, it adds "
                      "the same tag — the one who came to Jesus by night. John wants "
                      "you to remember how he started."),
        "must_show": "THE HINGE OF THE WHOLE EPISODE — he leaves as the first grey light comes; the dark is ending.",
        "must_not_show": "not full daylight yet, and no longer full night; this is the turn between them.",
        "scene": (
            "SHOT FROM BEHIND NICODEMUS, looking past his shoulder down the stepped "
            "Jerusalem street as he walks away from the camera in the first cold "
            "grey light before sunrise. His dark hood is DOWN on his shoulders and "
            "his grey-white head is bare — he is not hiding his face any more. The "
            "sky above the rooftops ahead of him is beginning to pale. Exactly one "
            "person is in the frame, with two arms, two legs and one head."
        ),
    },
    {
        "id": "v2-r004-b28", "out": "s28-one-voice-rose.jpeg", "seg": "n10",
        "window": "250.97-261.65", "wide": True, "jesus": False, "ref": False,
        "locks": ["NICO", "COUNCIL"],
        "narration": ("Months later, the council met in broad daylight, furious, "
                      "ready to condemn Jesus without a hearing. And one voice rose "
                      "to stop them. Nicodemus."),
        "must_show": "7:50 — the same chamber as b01, now in uproar, and the one old man on his feet against it.",
        "must_not_show": "no lamps anywhere — this is broad daylight, and that is the point.",
        "scene": (
            "The council chamber in hard bright daylight is in uproar, councillors "
            "half out of their seats and shouting each other down — and in the "
            "middle of it Nicodemus has risen alone to his feet in his deep indigo "
            "robe, standing straight, one hand raised, facing the angriest of them. "
            "The tall windows pour daylight over all of it and no lamp is lit "
            "anywhere. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b29", "out": "s29-doth-our-law-judge.jpeg", "seg": "s51",
        "window": "262.65-266.50", "wide": True, "jesus": False, "ref": False,
        "locks": ["NICO", "COUNCIL"],
        "narration": ("Doth our law judge any man, before it hear him, and know what "
                      "he doeth? (John 7:51)"),
        "must_show": "7:51 — the question put to the room; hostile faces turning on him for it.",
        "must_not_show": "he is not shouting; the courage is in the steadiness.",
        "scene": (
            "Nicodemus stands among the tiered benches in the sunlit chamber, "
            "speaking levelly with one open hand extended toward the council, his "
            "old face calm and set — and the councillors nearest him have rounded on "
            "him, one leaning in with his face twisted in anger, two others "
            "exchanging a cold look. Hard bright daylight. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r004-b30", "out": "s30-a-kings-burial-in-the-open.jpeg", "seg": "n11",
        "window": "282.94-311.64", "wide": True, "jesus": False, "ref": False,
        "locks": ["NICO", "JERUSALEM"],
        "narration": ("And Nicodemus came — openly, in the daylight — carrying a "
                      "hundred pounds of myrrh and aloes for the burial. The man who "
                      "had crept to Jesus in the dark gave him a king's burial in "
                      "the open."),
        "must_show": "19:39 — an ENORMOUS quantity of spices, in full daylight, carried openly where everyone can see.",
        "must_not_show": "reverence and distance at the tomb — no body, no wounds, nothing dwelt on. No hood, no hiding, no lamp.",
        "scene": (
            "In full hard daylight outside a rock-cut tomb in a garden, Nicodemus "
            "walks openly at the head of two servants who carry between them large "
            "heavy sealed clay jars and bulging linen sacks of burial spices — a "
            "visibly enormous quantity, far more than any ordinary burial. His "
            "grey-white head is bare and lifted, his fine deep indigo robe plain to "
            "see, and he does not glance around to check who is watching. Bundles of "
            "clean white burial linen are carried folded in his own arms. Exactly "
            "three people are in the frame; each has two arms, two hands and one "
            "head."
        ),
    },
]
