#!/usr/bin/env python3
"""V2 beat map — row 90, build-90-washing-feet (John 13:1-15).

COVERAGE: 12 pictures over 69.6 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (John 13:1-15 KJV):
  v1-2  the last supper, evening, the upper room; "having loved his
        own... he loved them unto the end."
  v4-5  "He RISETH from supper, and LAID ASIDE HIS GARMENTS; and took
        a TOWEL, and GIRDED himself. After that he poureth WATER into
        a BASON, and began to WASH THE DISCIPLES' FEET, and to wipe
        them with the towel wherewith he was girded." — the exact
        servant's sequence.
  v6-8  Peter: "THOU SHALT NEVER WASH MY FEET." Jesus: "If I wash thee
        not, thou hast NO PART WITH ME."
  v12   "after he had washed their feet, and had TAKEN HIS GARMENTS,
        and was SET DOWN again, he said... Know ye what I have done
        to you?"
  v14   "If I then, your LORD AND MASTER, have washed your feet; ye
        also OUGHT to wash one another's feet."

SETTING: the SAME upper room and night as row 89 — the ROOM lock below
matches row 89's word for word.

TIME OF DAY: lamplit NIGHT throughout (the Passover evening). Correct
story darkness, not the row-11 defect.

CONTENT-CARE: no flags. Feet and washing rendered with dignity —
road-dusty feet, clean water, nothing grotesque; Peter's refusal is
love confused, never rebellion; the low job painted as majesty, which
is the row's whole point.

CHANGING CONDITION (kept OUT of the locks): Jesus's dress — robed at
table, then the outer garment laid aside and the towel girded, then
robed and seated again (v12); the basin water — clean, then grey with
road dust; the circuit — man to man around the ring.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream. PETER and JOHN come from the shared CAST_LOCKS.
LOCKS = {
    "ROOM": (
        "ROOM LOCK: the upper room — a large furnished chamber up an "
        "outside stair: a LOW U-SHAPED TABLE with cushions where "
        "diners recline, clay oil lamps on the table and in wall "
        "niches, plastered walls, one shuttered window open on the "
        "night. The same table, lamps and walls throughout."
    ),
    "BASIN": (
        "BASIN LOCK: the washing kit — a wide shallow CLAY BASIN, a "
        "tall clay water jar, and one long plain LINEN TOWEL; simple "
        "household things, the servant's kit kept by the door."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r090-b01", "out": "s01-at-that-last-supper-knowing.jpeg", "seg": "n0",
        "window": "0.28-7.25", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "PETER", "JOHN"],
        "narration": (
            "At that last supper, knowing he was about to leave the world, "
            "Jesus did something no master would ever do for his servants."
        ),
        "must_show": "the rising — the lamplit supper mid-meal, and Jesus rising from his place at the table while the talk continues; the act beginning before anyone understands.",
        "must_not_show": "no halo, glare or rim-light; the table's unawareness — conversation still going as he rises.",
        "scene": (
            "The lamplit supper murmurs on "
            "around the low table — bread "
            "passing, low talk, Peter mid-"
            "story with a crust in his hand "
            "— and in the middle of it, "
            "quietly, Jesus rises from his "
            "cushion: no announcement, no "
            "raised hand, just a man "
            "standing up from his own "
            "farewell meal with a purpose "
            "none of his friends has "
            "noticed yet, his eyes already "
            "on the servant's kit by the "
            "door. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r090-b02", "out": "s02-he-got-up-from-the.jpeg", "seg": "n1a",
        "window": "7.89-12.58", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BASIN"],
        "narration": (
            "He got up from the table, wrapped a towel around his waist, and "
            "poured water into a basin."
        ),
        "must_show": "SCRIPTURE-EXACT: the girding (v4-5) — close on the sequence: the outer garment laid aside, the long linen towel knotted at his waist, water arcing from the tall jar into the wide basin.",
        "must_not_show": "no halo, glare or rim-light; the sequence SERVILE and deliberate — a master dressing down to the lowest uniform in the house.",
        "scene": (
            "Close on the uniform change no "
            "master makes: the outer robe "
            "folded deliberately aside, the "
            "long linen towel wrapped and "
            "knotted at the waist the way "
            "every house slave in the city "
            "knots it, and then the water — "
            "poured steady from the tall "
            "clay jar into the wide shallow "
            "basin, the lamplight shivering "
            "in the rising water while the "
            "table behind him goes one "
            "conversation quieter. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r090-b03", "out": "s03-and-he-began-to-wash.jpeg", "seg": "n1b",
        "window": "13.18-16.66", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "BASIN"],
        "narration": "And he began to wash his disciples' feet — one by one.",
        "must_show": "SCRIPTURE-EXACT: the washing — Jesus kneeling with the basin at the first disciple's feet, water over road-dusty skin, the towel at work; the table stunned silent around him.",
        "must_not_show": "no halo, glare or rim-light; the feet HONEST — road-dusty, washed clean with real care; the room's shock visible.",
        "scene": (
            "The room stops breathing: at "
            "the ring's first place Jesus "
            "kneels on the floor with the "
            "basin, lifting a road-dusty "
            "foot with both hands into the "
            "water — washing it clean with "
            "the slow thorough care of a "
            "man who means it, drying it in "
            "the towel at his own waist — "
            "while down the table faces "
            "freeze mid-word, bread stops "
            "mid-pass, and the master of "
            "the feast works the floor like "
            "the lowest servant in Judea. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r090-b04", "out": "s04-when-he-came-to-peter.jpeg", "seg": "n2 + s8",
        "window": "17.32-22.09", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "BASIN", "PETER"],
        "narration": (
            "When he came to Peter, Peter pulled back. Thou shalt never wash "
            "my feet."
        ),
        "must_show": "SCRIPTURE-EXACT: the refusal — Peter recoiling, feet drawn up under him, both hands out in protest; Jesus kneeling before him with the basin, patient.",
        "must_not_show": "no halo, glare or rim-light; Peter's refusal LOVE-CONFUSED — horror at the indignity, not rebellion.",
        "scene": (
            "At Peter's place the circuit "
            "hits its wall: the big "
            "fisherman recoiling up his "
            "cushion with his feet drawn "
            "under him like a man saving "
            "them from fire, both broad "
            "hands out in protest — NEVER — "
            "the horror on his face the "
            "horror of love watching its "
            "Lord kneel in the floor-dust — "
            "while Jesus stays exactly "
            "where he knelt, basin waiting, "
            "patient as the water. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r090-b05", "out": "s05-not-you-not-for-me.jpeg", "seg": "n2b",
        "window": "23.61-29.36", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER"],
        "narration": (
            "Not you. Not for me, Peter said. And Jesus answered him gently, "
            "but he did not back down."
        ),
        "must_show": "the standoff — the two faces close: Peter's anguished stubbornness, Jesus's gentle immovability; love against love at short range.",
        "must_not_show": "no halo, glare or rim-light; NEITHER face hard — both loving, one confused, one certain.",
        "scene": (
            "Close between the two faces: "
            "Peter's all anguished granite — "
            "jaw set, eyes wet, the "
            "stubbornness of a man defending "
            "his Lord's honour against his "
            "Lord — and a hand-span away "
            "Jesus's face gentle and utterly "
            "immovable, the kindness in it "
            "not softening the refusal to "
            "be refused by one degree — two "
            "loves locked at short range, "
            "and only one of them "
            "understanding the stakes. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r090-b06", "out": "s06-if-i-wash-thee-not.jpeg", "seg": "j1",
        "window": "30.00-32.78", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BASIN", "PETER"],
        "narration": "If I wash thee not, thou hast no part with me.",
        "must_show": "SCRIPTURE-EXACT: the line drawn — Jesus speaking it quietly up at Peter from his knees, the basin between them; the gentlest ultimatum ever issued.",
        "must_not_show": "no halo, glare or rim-light; the words spoken FROM BELOW — authority kneeling, and absolute.",
        "scene": (
            "From his knees, over the basin's "
            "waiting water, Jesus says the "
            "quiet sentence that ends the "
            "argument: NO PART WITH ME — no "
            "raised voice, no rising from "
            "the floor, the ultimatum "
            "delivered from below with the "
            "full weight of everything Peter "
            "cannot bear to lose — and on "
            "the fisherman's face the "
            "granite starting to crack as "
            "the arithmetic lands. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r090-b07", "out": "s07-that-is-how-serious-this.jpeg", "seg": "n2c",
        "window": "34.30-39.32", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": (
            "That is how serious this is. Peter thought he was protecting "
            "Jesus's dignity."
        ),
        "must_show": "the misunderstanding — close on Peter's breaking face: the protective instinct visible, and beneath it the dawning that he has it backwards.",
        "must_not_show": "no halo, glare or rim-light; the crack HONEST — pride and love and confusion resolving in real time.",
        "scene": (
            "Close on Peter's face at the "
            "hinge: the protective granite "
            "still trying to hold — he was "
            "GUARDING something, he was "
            "sure of it — and underneath, "
            "spreading like water through a "
            "cracked hull, the dawning "
            "suspicion that he has been "
            "defending his Lord against his "
            "Lord's own love, and that the "
            "dignity he fought for was "
            "never the thing at risk. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r090-b08", "out": "s08-what-he-was-really-doing.jpeg", "seg": "n2c",
        "window": "39.32-42.85", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "BASIN", "PETER"],
        "narration": "What he was really doing was refusing to be loved.",
        "must_show": "the surrender — Peter's feet lowered at last into the basin, his big hands open in yielded defeat; Jesus washing them; love received.",
        "must_not_show": "no halo, glare or rim-light; the yielding COMPLETE — the proud feet in the water, the face undone and glad of it.",
        "scene": (
            "The wall comes down: Peter's "
            "road-worn feet lowering at last "
            "into the shallow water, his "
            "big hands falling open at his "
            "sides in total yielded defeat, "
            "the face above them undone — "
            "and Jesus washing the "
            "surrendered feet with the same "
            "unhurried thoroughness as all "
            "the rest, the water going grey "
            "with the day's road while a "
            "proud man learns the harder "
            "half of love: letting it be "
            "done to you. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r090-b09", "out": "s09-when-he-had-finished-he.jpeg", "seg": "n3",
        "window": "43.48-51.23", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "BASIN"],
        "narration": (
            "When he had finished, he dried their feet with the towel at his "
            "waist, sat back down, and asked if they understood what he had "
            "just done."
        ),
        "must_show": "SCRIPTURE-EXACT: garments taken, set down again (v12) — Jesus robed once more at his place, the used basin and damp towel by the door; the question in his face to the ring.",
        "must_not_show": "no halo, glare or rim-light; the basin's grey water and damp towel VISIBLE — the work done, the lesson pending.",
        "scene": (
            "The circuit done, the room "
            "reassembles: Jesus robed again "
            "and settled back at his place "
            "at the table, the wide basin "
            "standing by the door with its "
            "water gone grey from twelve "
            "roads, the damp towel folded "
            "over its rim — and around the "
            "ring twelve men with clean "
            "feet and turning minds, "
            "meeting the question in his "
            "quiet face: do you know what "
            "I have done to you? Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r090-b10", "out": "s10-if-i-then-your-lord.jpeg", "seg": "j2",
        "window": "51.88-58.01", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "PETER", "JOHN"],
        "narration": (
            "If I then, your Lord and Master, have washed your feet; ye also "
            "ought to wash one another's feet."
        ),
        "must_show": "SCRIPTURE-EXACT: the commission — Jesus at the table delivering the ye-also to the listening ring; his gesture linking his act to their future ones.",
        "must_not_show": "no halo, glare or rim-light; the logic VISIBLE in gesture — from himself, to them, to one another.",
        "scene": (
            "The lesson lands with its full "
            "hinge: Jesus's hand touching "
            "his own chest — IF I, YOUR "
            "LORD — then opening outward "
            "around the lamplit ring — YE "
            "ALSO, ONE ANOTHER'S — the "
            "gesture drawing the line every "
            "eye can follow, from the grey "
            "basin water by the door "
            "through himself to each of "
            "them and on to every servant "
            "any of them will ever kneel "
            "for — the low job, deeded to "
            "the whole family. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r090-b11", "out": "s11-whatever-he-just-did-for.jpeg", "seg": "n3b",
        "window": "59.69-63.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM", "BASIN", "PETER", "JOHN"],
        "narration": "Whatever he just did for them, they were to go do for each other.",
        "must_show": "the inheritance — disciples' eyes moving from the basin by the door to each other: the job being mentally accepted man to man.",
        "must_not_show": "no halo, glare or rim-light; the exchange of LOOKS the picture — the basin's future written in their faces.",
        "scene": (
            "Close along the ring as the "
            "inheritance settles: eyes "
            "travelling from the grey-"
            "watered basin by the door to "
            "each other's faces — Peter "
            "looking at John, John at the "
            "man beside him — each of them "
            "measuring the towel against "
            "his own waist for the first "
            "time, the room quietly filling "
            "with a job description none "
            "of them will ever again be "
            "too great for. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r090-b12", "out": "s12-the-greatest-one-in-the.jpeg", "seg": "n4",
        "window": "63.92-69.21", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "BASIN"],
        "narration": (
            "The greatest one in the room knelt at the dirtiest job in the "
            "house. That is the kind of king he is."
        ),
        "must_show": "the closing image — the remembered picture held: Jesus kneeling with basin and towel at a disciple's feet in the lamplight; kingship defined in one posture.",
        "must_not_show": "no halo, glare or rim-light; the posture the WHOLE statement — greatness at floor level, nothing added.",
        "scene": (
            "The closing frame keeps the "
            "picture the way the twelve "
            "kept it: the greatest one in "
            "the room down on the floor in "
            "the lamplight — kneeling over "
            "the basin with a road-dirty "
            "foot cradled in his two hands, "
            "the servant's towel knotted at "
            "his waist, the water grey with "
            "other men's miles — a king "
            "found at the dirtiest job in "
            "the house, doing it like it "
            "was the throne. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
]
