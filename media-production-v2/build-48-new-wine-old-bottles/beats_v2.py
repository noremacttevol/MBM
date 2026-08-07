#!/usr/bin/env python3
"""V2 beat map — row 48, build-48-new-wine-old-bottles (Mark 2:18-22).

COVERAGE: 35 pictures over 197.4 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 2:18-22 KJV):
  v18   "Why do the disciples of John and of the Pharisees FAST, but thy
        disciples fast not?" — the questioners are SINCERE, not hostile
        (the narration insists: 'good men, going hungry to draw close to
        him'; 'a fair question, asked plainly'). Their faces are earnest
        throughout — this row has NO villains.
        Setting: Capernaum in the early ministry (the Levi's-feast
        context of Mark 2) — the frame is a bright town courtyard with
        the sounds of a feast nearby; a staging no earlier row has used.
  v19   "Can the children of the bridechamber fast, while the BRIDEGROOM
        is with them?" — the wedding vignette: a lamplit village wedding
        in full joy, the groom in the midst; fasting visibly absurd there.
  v20   "the days will come, when the bridegroom shall be TAKEN AWAY" —
        the cross foreshadowed ONLY in Jesus's face: a distance entering
        his eyes mid-joy; NO cross imagery, no shadow-play — one look.
  v21   the PATCH: new unshrunk cloth on an old garment — the tailor
        vignette, the tear made worse; homely, exact.
  v22   the WINESKINS: new wine still working needs a new soft skin; an
        old brittle skin bursts and both are lost. The wineskin vignettes
        are the row's centrepiece: fresh supple skin vs hard cracked one,
        the burst shown as SPILLED wine on stone (loss, not spectacle).
  vNARR the landing: 'not a patch on the old religion — a whole new
        thing'; the closing ask is 'a heart soft enough to hold it' —
        final beat returns to a new skin, filled and swelling safely.

TIME OF DAY: the frame beats are bright Capernaum morning. The wedding
vignette is warm lamplit night (a wedding's own hour). The tailor and
wineskin vignettes are workshop daylight. The closing beats are warm
late gold. All shifts stated and story-driven.

CONTENT-CARE: row 48 has no flag in §3. The questioners are honoured
throughout; the only casualty in the row is a wineskin.

CHANGING CONDITION (kept OUT of the locks): the wineskins' states — new
and supple, old and cracked, burst and spilled, filled and swelling —
are per-beat facts. The old coat's hole grows between its two beats.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "ASKERS": (
        "QUESTIONERS LOCK: the fasting men are the same three in every "
        "shot — an older man with a hollow-cheeked ascetic face and a "
        "long grey beard; a middle-aged man with earnest deep-set eyes; "
        "and a thin young disciple of John with sun-cracked lips. They "
        "wear plain DARK CHARCOAL and DEEP UMBER wool with simple rope "
        "belts, dusty from the road (never cream, never white). Faces "
        "shown clearly — sincere, hungry, honest; NEVER sneering."
    ),
    "COURTYARD": (
        "CAPERNAUM COURTYARD LOCK: a bright town courtyard off a "
        "Capernaum street — honey-stone walls, a fig tree's shade in "
        "one corner, a low stone bench, a doorway through which the "
        "warmth and noise of a feast can be sensed, and the lake's "
        "blue showing in a gap between houses. Bright morning light."
    ),
    "WEDDING": (
        "WEDDING LOCK: a village wedding at night — a lamplit courtyard "
        "strung with little oil lamps on cords, a long laden table, "
        "musicians with pipe and drum, dancing guests in deep festive "
        "colours, and the GROOM at the centre: a young man in a DARK "
        "WINE-RED festal robe with a myrtle circlet, his joy the "
        "room's engine (never cream, never white). Faces shown clearly."
    ),
    "WORKSHOP": (
        "WORKSHOP LOCK: a household work corner — a low table by a "
        "bright window, a wicker basket of mending, shears and bone "
        "needles, and on the wall pegs a row of garments. The same "
        "window, table and pegs for the patch beats."
    ),
    "CELLAR": (
        "WINE STORE LOCK: a cool stone wine store — a rack of "
        "full-bellied leather wineskins hanging from pegs, clay "
        "stoppers and cording on a shelf, a stone floor with a "
        "drain-channel, and one high window's slanted light. The same "
        "rack, shelf and floor for the wineskin beats."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r048-b01", "out": "s01-some-very-sincere-very-religious.jpeg", "seg": "n1",
        "window": "0.28-4.79", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ASKERS", "COURTYARD"],
        "narration": (
            "Some very sincere, very religious men came to him with an honest "
            "question."
        ),
        "must_show": "the frame — the three earnest fasting men approaching Jesus in the bright courtyard, their manner respectful, the feast's warmth audible through the doorway behind him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the askers HONOURED — earnest bearing, careful approach; no confrontation in the geometry.",
        "scene": (
            "In the bright morning courtyard, the camera at the "
            "wall's side taking the approach in profile, the three "
            "fasting men approach Jesus with the careful "
            "respect of serious people — the old ascetic "
            "leading with both hands folded, the earnest "
            "middle one a half-step back, the thin young "
            "disciple of John last — while behind Jesus the "
            "doorway spills the warmth and clatter of a "
            "feast in progress, the very sound their "
            "question is about. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b02", "out": "s02-why-do-the-disciples-of.jpeg", "seg": "s18",
        "window": "5.31-10.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKERS"],
        "narration": (
            "Why do the disciples of John and of the Pharisees fast, but thy "
            "disciples fast not?"
        ),
        "must_show": "SCRIPTURE-EXACT: the question asked — close on the old ascetic's hollow-cheeked face mid-question: honest puzzlement, hunger's discipline written on him.",
        "must_not_show": "no halo, glare or rim-light; the fast VISIBLE in the face — cheeks hollowed by devotion, not poverty; dignity absolute.",
        "scene": (
            "Close in the courtyard light: the old ascetic's "
            "face mid-question — cheeks hollowed by long "
            "chosen hunger, the grey beard neat over the "
            "plain charcoal wool, his deep eyes carrying "
            "real puzzlement and not one grain of malice — "
            "a man who has skipped a thousand meals for God "
            "asking, honestly, why this teacher's friends "
            "skip none. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r048-b03", "out": "s03-it-was-a-fair-question.jpeg", "seg": "n1b",
        "window": "12.21-14.49", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ASKERS", "COURTYARD"],
        "narration": "It was a fair question, asked plainly.",
        "must_show": "the question received — Jesus's face taking the question with visible respect: no defensiveness, the beginning of a warm answer.",
        "must_not_show": "no halo, glare or rim-light on Jesus; he honours the askers — attention full, expression open.",
        "scene": (
            "Close on Jesus in the morning light: the "
            "question just landed and his face receiving it "
            "the way good questions deserve — head slightly "
            "tipped, eyes warm on the old ascetic, nothing "
            "defensive anywhere in the features — a teacher "
            "visibly pleased to be asked plainly, already "
            "reaching for a picture instead of an argument. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r048-b04", "out": "s04-these-were-good-men-going.jpeg", "seg": "n2",
        "window": "18.13-21.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKERS"],
        "narration": "These were good men, going hungry to draw close to him.",
        "must_show": "the devotion honoured — the young disciple of John at private prayer at dawn, his untouched bread beside him; the fast's sincerity from the inside.",
        "must_not_show": "no halo, glare or rim-light; the hunger CHOSEN and aimed at God — devotion, not performance.",
        "scene": (
            "In grey dawn light the thin young disciple "
            "kneels at prayer in a bare corner, his lips "
            "moving, his sun-cracked hands folded hard — "
            "and beside him on the ledge his morning bread "
            "sits untouched under its cloth, pushed away "
            "before the prayer began — hunger volunteered "
            "as a message to heaven by a young man "
            "entirely in earnest. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b05", "out": "s05-and-here-were-his-disciples.jpeg", "seg": "n2",
        "window": "21.35-26.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["COURTYARD"],
        "narration": (
            "And here were his disciples, not fasting at all. It looked "
            "careless."
        ),
        "must_show": "the contrast — through the feast doorway: the disciples at table in full cheerful appetite, bread passing, cups raised; the apparent carelessness, painted honestly.",
        "must_not_show": "no halo, glare or rim-light; the eating JOYFUL and open — the offence real to a faster's eye, innocent in itself.",
        "scene": (
            "Through the courtyard doorway the feast shows "
            "warm and loud: the disciples at the crowded "
            "table in full appetite — bread torn and "
            "passed, a cup raised to somebody's toast, the "
            "big fisherman laughing with his mouth full — "
            "cheerful, unashamed eating in the middle of "
            "the morning, framed exactly as it must have "
            "looked to three hungry holy men standing in "
            "the bright courtyard. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b06", "out": "s06-can-the-children-of-the.jpeg", "seg": "jv19",
        "window": "29.53-34.28", "wide": True, "jesus": False, "ref": False,
        "locks": ["WEDDING"],
        "narration": (
            "Can the children of the bridechamber fast, while the bridegroom is "
            "with them?"
        ),
        "must_show": "SCRIPTURE-EXACT: the wedding invoked — the lamplit village wedding at full joy: the wine-red groom laughing at the centre, guests dancing, the laden table; fasting unthinkable in the frame.",
        "must_not_show": "no halo, glare or rim-light; total celebration — the question answers itself in lamplight.",
        "scene": (
            "The village wedding fills the night courtyard, the "
            "camera at its corner behind the nearest dancers' "
            "shoulders, "
            "with light and noise: little oil lamps strung "
            "on cords overhead, the pipe and drum driving a "
            "ring of dancers, the long table laden and "
            "raided — and at the centre of everything the "
            "young groom in his wine-red robe and myrtle "
            "circlet, head back, laughing, the whole "
            "night's joy turning around him like a wheel "
            "around its axle. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b07", "out": "s07-as-long-as-they-have.jpeg", "seg": "jv19",
        "window": "34.28-38.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["WEDDING"],
        "narration": "as long as they have the bridegroom with them, they cannot fast.",
        "must_show": "the impossibility — close at the wedding table: the groom himself pressing food and cup on a guest, both laughing; refusal literally impossible with the groom serving.",
        "must_not_show": "no halo, glare or rim-light; the groom SERVES — joy insisting on being shared; abstinence has nowhere to stand.",
        "scene": (
            "Close at the laden table: the wine-red groom "
            "himself leans across to press a torn piece of "
            "the wedding bread into a guest's hand and top "
            "his cup with the other, both men laughing in "
            "each other's faces — hospitality at wedding "
            "pressure, where turning down food would take "
            "more strength than the room contains. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b08", "out": "s08-he-points-them-at-a.jpeg", "seg": "n3",
        "window": "40.49-44.94", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ASKERS", "COURTYARD"],
        "narration": (
            "He points them at a wedding. Nobody starves themselves at a "
            "wedding feast."
        ),
        "must_show": "the picture handed over — Jesus in the courtyard mid-answer, hands open in the shape of the feast he is describing; the askers' faces beginning to work.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the answer as gift — a picture offered, not a rebuttal scored.",
        "scene": (
            "In the bright courtyard Jesus answers with both "
            "hands open and moving — sketching the feast, "
            "the lamps, the dance in the air between "
            "himself and the three fasting men — and their "
            "faces have begun to work at it: the old "
            "ascetic's brows drawing as the picture "
            "assembles, the young one's cracked lips "
            "parting — hungry men being handed, of all "
            "things, a wedding. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b09", "out": "s09-while-the-groom-is-right.jpeg", "seg": "n3",
        "window": "44.94-49.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["WEDDING"],
        "narration": (
            "While the groom is right there in the room, the only fitting thing "
            "to do is celebrate."
        ),
        "must_show": "presence as the reason — the wedding wide: every face in the courtyard oriented to the groom like plants to light; his presence the celebration's whole logic.",
        "must_not_show": "no halo, glare or rim-light; the orientation of joy — all lines of the composition converging on the wine-red figure.",
        "scene": (
            "The wedding courtyard from its corner: dancers, "
            "table, musicians, children on shoulders — and "
            "every face of the many turned, mid-laugh and "
            "mid-song, toward the wine-red groom at the "
            "centre of the floor as he spins somebody's "
            "grandmother in the dance — a room whose whole "
            "reason is standing in the middle of it, "
            "visibly, tonight. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b10", "out": "s10-and-that-was-the-quiet.jpeg", "seg": "n3",
        "window": "49.98-54.81", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COURTYARD"],
        "narration": (
            "And that was the quiet, staggering claim underneath it. The groom "
            "is here."
        ),
        "must_show": "the claim surfacing — close on Jesus's face as the metaphor's centre quietly names itself; the joy of the wedding resting on his own features.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the claim made by stillness — the groom of the picture, present in the courtyard.",
        "scene": (
            "Close on Jesus in the courtyard's bright "
            "morning: the wedding picture just given, and "
            "its centre quietly naming itself in his face — "
            "the warm eyes carrying the feast's whole joy "
            "without a lamp or a dance anywhere near, the "
            "faintest smile of a man describing his own "
            "wedding to guests who have not recognized the "
            "groom. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r048-b11", "out": "s11-but-the-days-will-come.jpeg", "seg": "jv20",
        "window": "57.44-64.82", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ASKERS", "COURTYARD"],
        "narration": (
            "But the days will come, when the bridegroom shall be taken away "
            "from them, and then shall they fast in those days."
        ),
        "must_show": "SCRIPTURE-EXACT: the shadowed verse — Jesus saying it with the joy stilling in his face, a farther distance entering his eyes; the askers sensing the change without understanding it.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NO cross imagery, no symbols — the foreshadow lives entirely in one face's weather.",
        "scene": (
            "The courtyard's brightness holds, but something "
            "in Jesus's face has changed latitude — the "
            "wedding joy stilled, the warm eyes gone a long "
            "way off mid-sentence, some far day standing "
            "briefly in them — and the three fasting men "
            "feel the shift without being able to name it, "
            "the old ascetic's head tilting at a grief he "
            "cannot see the shape of. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b12", "out": "s12-then-he-says-something-that.jpeg", "seg": "n4",
        "window": "66.35-68.82", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKERS"],
        "narration": "Then he says something that must have landed strangely.",
        "must_show": "the strangeness landing — the three askers' faces at the odd verse: puzzlement of a new kind, the question they came with forgotten.",
        "must_not_show": "no halo, glare or rim-light; three distinct puzzlements — the conversation has outgrown its own beginning.",
        "scene": (
            "Close on the three fasting men in the bright "
            "light: the old ascetic's puzzlement gone from "
            "doctrinal to human, the earnest middle one "
            "glancing at his companions to check they "
            "heard the same words, the thin young one "
            "staring at the teacher with his original "
            "question visibly mislaid somewhere behind "
            "him — three men who came about fasting, "
            "standing suddenly at the edge of something "
            "else. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r048-b13", "out": "s13-a-day-is-coming-when.jpeg", "seg": "n4",
        "window": "68.82-74.79", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COURTYARD"],
        "narration": (
            "A day is coming when the groom will be gone. He is looking "
            "straight past this moment to the cross."
        ),
        "must_show": "the look past — Jesus's profile gazing beyond the courtyard wall toward the south, the far day held steadily in his eyes; NO cross imagery anywhere.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the cross carried ONLY as distance in a gaze — nothing literal, nothing symbolic in frame.",
        "scene": (
            "In profile against the courtyard's honey "
            "stone, Jesus looks past the wall's edge toward "
            "the south where the roads leave town — the "
            "morning bright around him and his eyes "
            "somewhere years down one particular road, "
            "steady, unafraid and grave — a groom counting "
            "his own wedding's cost in the middle of "
            "describing the dance. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b14", "out": "s14-there-will-be-a-time.jpeg", "seg": "n4",
        "window": "74.79-78.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKERS"],
        "narration": "There will be a time to mourn, and a time to fast.",
        "must_show": "the fast's future honour — the old ascetic's face hearing his discipline PLACED, not dismissed: fasting given its coming hour.",
        "must_not_show": "no halo, glare or rim-light; vindication arriving gently — his life's practice granted a future, and a sadder one than he knew.",
        "scene": (
            "Close on the old ascetic's hollow face in the "
            "bright light: his life's discipline being "
            "handed back to him with a time and a place "
            "attached — the deep eyes steadying as fasting "
            "is honoured rather than waved away, and "
            "clouding slightly at the kind of day that "
            "will call for it — an old faster learning his "
            "hunger has an appointment he would never have "
            "chosen. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r048-b15", "out": "s15-but-not-now-not-while.jpeg", "seg": "n4 + n5",
        "window": "78.38-85.85", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ASKERS", "COURTYARD"],
        "narration": (
            "But not now, not while he is standing in front of them. Then he "
            "gives them two small pictures from everyday life."
        ),
        "must_show": "the pivot to pictures — Jesus brightening again in the courtyard, hands lifting to frame the first small picture; the heaviness set down, the teaching resumed with lightness.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the return of lightness — a teacher reaching for homely things.",
        "scene": (
            "The far day passes off Jesus's face like a "
            "cloud off water, and the courtyard's morning "
            "has him back — his hands lifting to frame "
            "something small and homely in the air, one "
            "eyebrow up, the teacher's pleasure returning — "
            "while the three fasting men, wrung through "
            "wedding and grief in five minutes, lean in "
            "for whatever ordinary object he is about to "
            "make dangerous. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b16", "out": "s16-the-first-one-is-about.jpeg", "seg": "n5",
        "window": "85.85-88.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["WORKSHOP"],
        "narration": "The first one is about mending clothes.",
        "must_show": "the homely stage — the workshop corner by its bright window: the mending basket, shears and needles, an old coat over the table's edge; domestic scale.",
        "must_not_show": "no halo, glare or rim-light; ordinary things at ordinary size — the parable's props laid out.",
        "scene": (
            "The work corner by the bright window: the "
            "wicker mending basket spilling its rolled "
            "cloths, bone needles in their clay cup, the "
            "iron shears on the table — and over the "
            "table's edge an old soft coat laid out with "
            "a worn hole showing at the elbow — the whole "
            "theatre of the first small picture, set with "
            "things from anybody's house. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b17", "out": "s17-you-do-not-sew-a.jpeg", "seg": "n5",
        "window": "88.26-94.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["WORKSHOP"],
        "narration": (
            "You do not sew a stiff, brand-new scrap onto a soft, worn-out old "
            "coat."
        ),
        "must_show": "the mismatch — close on two cloths held together in a woman's hands: the stiff bright new scrap against the soft faded old weave; wrongness visible in texture alone.",
        "must_not_show": "no halo, glare or rim-light; the textures carry it — new cloth's stiffness against old cloth's softness, side by side.",
        "scene": (
            "Close in the window light: a woman's practised "
            "hands hold the two cloths together over the "
            "old coat — a stiff bright new-woven scrap, "
            "dense and hard-edged, laid against the soft "
            "faded weave it is meant to mend — and even "
            "before the needle moves, the two fabrics "
            "refuse each other visibly, the new one "
            "standing off the old like bark on cloth. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r048-b18", "out": "s18-no-man-also-seweth-a.jpeg", "seg": "jv21",
        "window": "94.97-105.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["WORKSHOP"],
        "narration": (
            "No man also seweth a piece of new cloth on an old garment: else "
            "the new piece that filled it up taketh away from the old, and the "
            "rent is made worse."
        ),
        "must_show": "SCRIPTURE-EXACT: the rent made worse — the patched coat after washing: the stiff patch puckered tight and the old cloth torn wide around its every stitch; the repair as the new damage.",
        "must_not_show": "no halo, glare or rim-light; the tear visibly WORSE than the original hole — the stitches themselves the tearing points.",
        "scene": (
            "On the work table the mended coat lies opened "
            "to its disaster: the stiff new patch has "
            "shrunk and puckered into a hard knot, and "
            "around its every stitch the soft old cloth "
            "has torn in little rays, the original modest "
            "hole now a ragged openwork twice its size — "
            "a repair that harvested the garment, lying "
            "in the honest window light beside the shears "
            "that meant well. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b19", "out": "s19-his-answer-was-not-what.jpeg", "seg": "n2",
        "window": "26.20-28.91", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ASKERS", "COURTYARD"],
        "narration": "His answer was not what they expected.",
        "must_show": "expectation upended — the askers braced for a ruling, and Jesus's face already somewhere else entirely: the gap between question asked and answer coming.",
        "must_not_show": "no halo, glare or rim-light on Jesus; their braced formality against his unexpected warmth.",
        "scene": (
            "In the courtyard the three fasting men stand "
            "braced in the posture of men awaiting a "
            "ruling — feet set, hands folded, the young "
            "one already half-nodding toward whichever "
            "verdict comes — while Jesus's face, close in "
            "the frame's other half, has gone warm and "
            "faintly amused in a way that fits no ruling "
            "of any kind, an answer of a different species "
            "already on its way. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b20", "out": "s20-put-a-stiff-new-patch.jpeg", "seg": "n5b",
        "window": "106.96-115.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["WORKSHOP"],
        "narration": (
            "Put a stiff new patch on a worn-out coat and the new cloth pulls "
            "against the old, and it tears the hole wider than it was before "
            "you started."
        ),
        "must_show": "the physics — extreme close at the patch's edge: the pull caught in the cloth itself, old threads strained to breaking around one stitch.",
        "must_not_show": "no halo, glare or rim-light; thread-level truth — tension made visible at a single stitch.",
        "scene": (
            "Extreme close in the window light: one stitch "
            "at the patch's edge, and the war around it — "
            "the stiff new cloth hauling one way, the soft "
            "old threads strained taut and fraying around "
            "the needle's track, two fibres already "
            "snapped and curling — the whole doomed "
            "mechanics of the mismatch, legible in a "
            "thumbnail of fabric. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b21", "out": "s21-you-end-up-worse-off.jpeg", "seg": "n5b",
        "window": "115.40-119.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["WORKSHOP"],
        "narration": "You end up worse off for having tried to fix it that way.",
        "must_show": "the sum — the woman holding the ruined coat up to the window light, the worsened tear plain against the brightness, her face rueful.",
        "must_not_show": "no halo, glare or rim-light; rue without tragedy — a household loss, a lesson priced in wool.",
        "scene": (
            "The woman holds the old coat up against the "
            "bright window and the light itself does the "
            "arithmetic — pouring through the ragged "
            "openwork where a modest hole used to be, the "
            "hard puckered patch dark at its centre like a "
            "stone in a net — while her rueful face tips "
            "at it over the table: fixed once, ruined "
            "properly, a lesson now hanging in her hands. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r048-b22", "out": "s22-the-second-picture-is-about.jpeg", "seg": "n6",
        "window": "119.62-121.72", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELLAR"],
        "narration": "The second picture is about wine.",
        "must_show": "the second stage — the cool wine store: the rack of hanging skins in the slanted window light; the row's centrepiece props introduced.",
        "must_not_show": "no halo, glare or rim-light; the cellar's calm order — skins, stoppers, stone.",
        "scene": (
            "The cool stone wine store in its one slant of "
            "light: a rack of full-bellied leather "
            "wineskins hanging in a patient row from their "
            "pegs, clay stoppers and waxed cording ranged "
            "on the shelf, the drain-channel clean down "
            "the stone floor — a room built around the "
            "keeping of living things in leather, quiet as "
            "a library of wine. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b23", "out": "s23-in-that-world-you-kept.jpeg", "seg": "n6",
        "window": "121.72-129.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELLAR"],
        "narration": (
            "In that world you kept your wine in bottles made of leather, of "
            "whole animal skins. A fresh skin was soft and it could stretch."
        ),
        "must_show": "the fresh skin — close on a NEW wineskin in a keeper's hands: supple, pale, yielding visibly to his kneading thumbs; softness as capacity.",
        "must_not_show": "no halo, glare or rim-light; the suppleness demonstrated — leather answering the hands.",
        "scene": (
            "Close in the cellar light: a wine-keeper's "
            "hands work a brand-new skin — the pale supple "
            "leather denting and springing under his "
            "kneading thumbs, the whole bottle flexing "
            "easily in his grip like something half "
            "alive — soft, patient material with a year's "
            "worth of give folded into it, ready for wine "
            "that intends to grow. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b24", "out": "s24-but-an-old-skin-had.jpeg", "seg": "n6",
        "window": "129.73-137.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELLAR"],
        "narration": (
            "But an old skin had gone hard and brittle, and new wine, still "
            "working and giving off gas, needs room to swell."
        ),
        "must_show": "the old skin — close on a hard, dark, crack-glazed old skin beside the supple new one: rigidity visible, the surface craze-lined; and a jar of new wine still lively with fine bubbles.",
        "must_not_show": "no halo, glare or rim-light; the crack-glaze telling — leather gone to shell; the wine visibly alive.",
        "scene": (
            "On the cellar bench the two generations sit "
            "side by side: the old skin dark, stiff and "
            "glazed with a craze of fine cracks, holding "
            "its shape like pottery — and beside it the "
            "pale supple new one, slumped soft — while at "
            "the frame's edge a dipped clay jar of new "
            "wine works visibly, fine bubbles rising "
            "through the murk, a drink that has not "
            "finished becoming itself. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b25", "out": "s25-he-was-talking-about-himself.jpeg", "seg": "n3",
        "window": "54.81-56.88", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COURTYARD"],
        "narration": "He was talking about himself.",
        "must_show": "the referent named — a close return to Jesus's face in the courtyard: the groom, the wine, the newness — one man, quietly meant.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the claim carried in calm — self-identification without emphasis.",
        "scene": (
            "Close on Jesus in the bright courtyard: the "
            "morning light plain on the warm features, "
            "nothing raised, nothing pressed — and the "
            "whole morning's pictures quietly converging "
            "on the face that made them: the groom of the "
            "wedding, the wine of the skins, the new "
            "thing itself standing in sandals in a "
            "Capernaum courtyard answering questions "
            "about lunch. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r048-b26", "out": "s26-and-no-man-putteth-new.jpeg", "seg": "jv22",
        "window": "138.22-151.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELLAR"],
        "narration": (
            "And no man putteth new wine into old bottles: else the new wine "
            "doth burst the bottles, and the wine is spilled, and the bottles "
            "will be marred: but new wine must be put into new bottles."
        ),
        "must_show": "SCRIPTURE-EXACT: the burst, RESTRAINED — the aftermath on the cellar floor: the old skin split along its side, dark wine spread wide across the stone toward the drain; loss, not spectacle.",
        "must_not_show": "no halo, glare or rim-light; the burst already OVER — a split seam and spilled wine; nothing explosive depicted mid-action.",
        "scene": (
            "On the cellar floor the lesson lies spilled: "
            "the old skin split wide along its cracked "
            "side, collapsed in the pool of its failure, "
            "and the dark new wine spread far across the "
            "pale stone, reaching the drain-channel in a "
            "thin hurrying line — both treasures lost in "
            "one economy — while above on the rack the "
            "supple new skins hang untouched, the answer "
            "swinging gently on its pegs. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b27", "out": "s27-fasting-was-how-you-showed.jpeg", "seg": "n2",
        "window": "15.07-18.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKERS"],
        "narration": "Fasting was how you showed God you were serious.",
        "must_show": "the discipline's logic — the middle questioner declining offered bread in the market with a courteous hand, his seriousness legible to the whole street.",
        "must_not_show": "no halo, glare or rim-light; the refusal courteous and public — devotion's grammar, as that world read it.",
        "scene": (
            "In the busy market light a stall-keeper "
            "offers the earnest middle questioner a warm "
            "flat loaf across his boards — and the man "
            "declines it with a courteous flat hand and a "
            "small bow, his other hand touching his own "
            "chest in the gesture of a vow — seriousness "
            "spelled out in the one alphabet his whole "
            "street could read: hunger, chosen, for God. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r048-b28", "out": "s28-so-you-never-pour-fresh.jpeg", "seg": "n7",
        "window": "152.95-156.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELLAR"],
        "narration": "So you never pour fresh, living wine into a stiff old skin.",
        "must_show": "the rule enacted — the keeper's arm mid-pour arrested: the wine jar tipped toward the OLD skin and stopped, redirecting toward the new one; the near-mistake caught.",
        "must_not_show": "no halo, glare or rim-light; the redirect visible — a pour turning away from the wrong mouth.",
        "scene": (
            "In the slanted cellar light the keeper's pour "
            "is caught mid-correction — the heavy jar "
            "tipped and the first dark thread of new wine "
            "swinging away from the old skin's stiff "
            "cracked mouth toward the pale supple one "
            "held ready in his other hand — a rule of the "
            "craft executing itself in the wrist, "
            "centuries old and never once optional. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b29", "out": "s29-the-wine-keeps-growing-the.jpeg", "seg": "n7",
        "window": "156.91-164.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELLAR"],
        "narration": (
            "The wine keeps growing, the hard leather cannot give, and the "
            "whole thing tears open and everything is lost."
        ),
        "must_show": "the physics named — close on the old skin's crack-glazed side with the strain lines mapped across it; rigidity meeting growth, the failure legible before it happens.",
        "must_not_show": "no halo, glare or rim-light; the skin whole here — the fault lines shown, the verdict readable, the tear still future.",
        "scene": (
            "Close on the old skin's dark flank in the "
            "window light: the craze of fine cracks "
            "mapped across the glazed leather like a dry "
            "riverbed from the air, the seams drawn hard, "
            "the whole surface holding its shape with "
            "the brittle authority of things that have "
            "stopped listening — a container whose answer "
            "to growth is already written all over it. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r048-b30", "out": "s30-fresh-wine-belongs-in-a.jpeg", "seg": "n7",
        "window": "164.06-169.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELLAR"],
        "narration": (
            "Fresh wine belongs in a fresh skin, one that can stretch along "
            "with it."
        ),
        "must_show": "the right vessel filled — the new skin taking the pour: swelling gently as the wine goes in, the leather visibly accommodating; capacity in action.",
        "must_not_show": "no halo, glare or rim-light; the swelling gentle and safe — growth received, not resisted.",
        "scene": (
            "The pale new skin takes the pour in the "
            "keeper's steady hands — its supple sides "
            "swelling gently outward as the dark wine "
            "goes in, the leather easing and settling "
            "around its growing cargo like a sail taking "
            "wind — vessel and wine agreeing about the "
            "future, in the cellar's patient light. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r048-b31", "out": "s31-that-is-what-he-is.jpeg", "seg": "n7",
        "window": "169.12-176.91", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ASKERS", "COURTYARD"],
        "narration": (
            "That is what he is telling them. God is doing something so new and "
            "so alive that the old rigid forms simply cannot hold it."
        ),
        "must_show": "the meaning landed — the courtyard again: Jesus's open hands finishing the picture, and on the askers' faces the first cracks of a very large thought.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the askers not defeated — enlarged; their sincerity being offered a bigger room.",
        "scene": (
            "In the bright courtyard Jesus's open hands "
            "come to rest at the end of the second "
            "picture — and across the three sincere faces "
            "the size of it is arriving: the old "
            "ascetic's eyes widening by degrees, the "
            "earnest one's hand rising slowly to his "
            "beard, the young one looking down at his "
            "own fasting-thinned wrists and back up — "
            "three good men feeling their good question "
            "outgrown by its answer. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r048-b32", "out": "s32-not-a-patch-on-the.jpeg", "seg": "n7",
        "window": "176.91-180.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["WORKSHOP", "CELLAR"],
        "narration": "Not a patch on the old religion. A whole new thing.",
        "must_show": "the two pictures summed — one still frame: the ruined patched coat and the burst old skin set aside together, and beside them whole new cloth on its bolt and a new skin, waiting.",
        "must_not_show": "no halo, glare or rim-light; one continuous still (never panels) — the failed repairs retired, the new things ready.",
        "scene": (
            "On one bench in plain light the morning's "
            "evidence sits together: the torn patched "
            "coat folded aside with the split old skin "
            "laid across it — the museum of good "
            "intentions — and beside them, waiting in "
            "the same light, a whole bolt of new cloth "
            "and a pale supple new skin, unused and "
            "capable — the choice between mending the "
            "old and receiving the new, arranged on one "
            "board. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r048-b33", "out": "s33-that-is-the-good-news.jpeg", "seg": "n8",
        "window": "181.30-187.31", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COURTYARD"],
        "narration": (
            "That is the good news hiding inside a question about fasting. God "
            "was not tinkering with the old rules."
        ),
        "must_show": "the news' face — Jesus close in the courtyard, gladness fully surfaced: the answer's joy owning the features that carried the far-day shadow minutes ago.",
        "must_not_show": "no halo, glare or rim-light on Jesus; gladness plain — good news wearing its own expression.",
        "scene": (
            "Close on Jesus in the full morning light: the "
            "gladness that was banked all through the "
            "answer now fully surfaced — warm eyes bright, "
            "the smile arrived in the beard, the face of "
            "a man whose news is simply better than the "
            "question that fished for it — joy, standing "
            "in a courtyard, unmistakable at arm's "
            "length. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r048-b34", "out": "s34-he-was-pouring-out-something.jpeg", "seg": "n8",
        "window": "187.31-193.46", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ASKERS", "COURTYARD"],
        "narration": (
            "He was pouring out something brand new, full of life and joy, and "
            "he was standing right there to give it."
        ),
        "must_show": "the giver present — Jesus with both hands extended open toward the three fasting men, the gift's posture; the feast's warmth spilling from the doorway behind him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the extension TOWARD the askers — new wine offered first to the men most loyal to the old skins.",
        "scene": (
            "In the bright courtyard Jesus extends both "
            "hands open toward the three fasting men — "
            "the complete posture of giving, held easy — "
            "with the feast's noise and warmth spilling "
            "gold through the doorway behind him — the "
            "new thing itself, present-tense and "
            "offering, standing before three hungry "
            "faithful men with its hands already out. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r048-b35", "out": "s35-the-only-thing-he-asks.jpeg", "seg": "n8",
        "window": "193.46-197.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELLAR"],
        "narration": "The only thing he asks is a heart soft enough to hold it.",
        "must_show": "the closing image — the new skin filled and hanging at rest in the warm late light, gently swollen, holding its living cargo safely; softness as the whole requirement.",
        "must_not_show": "no halo, glare or rim-light; one vessel, one warm light — the ask made visible: supple, filled, safe.",
        "scene": (
            "In the last warm gold through the cellar "
            "window the new skin hangs at rest on its "
            "peg — gently swollen with its living wine, "
            "the supple leather eased full around the "
            "growth it was made for, the stopper snug, "
            "the whole vessel quietly at work holding "
            "what the old ones never could — softness, "
            "photographed doing the one job the whole "
            "morning asked of anyone. Every figure has "
            "two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "CELLAR": "PLACE-REF/cellar.jpeg",  # build-48-new-wine-old-bottles s22-the-second-picture-is-about (manual)
    "COURTYARD": "PLACE-REF/courtyard.jpeg",  # build-48-new-wine-old-bottles s01-some-very-sincere-very-religious (manual)
    "WEDDING": "PLACE-REF/wedding.jpeg",  # build-48-new-wine-old-bottles s06-can-the-children-of-the (manual)
    "WORKSHOP": "PLACE-REF/workshop.jpeg",  # build-48-new-wine-old-bottles s16-the-first-one-is-about (manual)
}
# === end PLACE-PLATES ===
