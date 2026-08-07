#!/usr/bin/env python3
"""V2 beat map — row 82, build-82-anointing-at-bethany (Mark 14:3-9).

COVERAGE: 25 pictures over 140.9 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 14:3-9 KJV):
  v3    "being in BETHANY in the house of SIMON THE LEPER, as he SAT AT
        MEAT, there came A WOMAN having an ALABASTER BOX of ointment of
        SPIKENARD very precious; and she BRAKE the box, and poured it
        ON HIS HEAD." — a supper; the jar BROKEN, not unstopped; the
        anointing on the HEAD; two days before Passover (v1).
  v4-5  "there were some that had INDIGNATION... Why was this waste of
        the ointment made? For it might have been sold for more than
        THREE HUNDRED PENCE... And they MURMURED AGAINST HER." — said
        where she could hear; she never speaks in the whole account.
  v6-7  "LET HER ALONE; why trouble ye her? she hath wrought a GOOD
        WORK on me. For ye have the poor with you always... but me ye
        have not always."
  v8    "She hath done WHAT SHE COULD: she is come AFOREHAND to anoint
        my body to THE BURYING."
  v9    "Wheresoever this gospel shall be preached throughout the whole
        world, this also that she hath done shall be spoken of FOR A
        MEMORIAL OF HER."

TIME OF DAY: one lamplit EVENING throughout — a supper two nights
before Passover; warm oil-lamp light in a shuttered room, deep shadow
at the walls. (Intentional interior night — not the row-11 defect.)

CONTENT-CARE: no flags. The woman's dignity absolute — she is silent
in the text, so her silence is played as strength, never cowering; the
critics indignant but human; the burial talk sober, no morbid imagery.

CHANGING CONDITION (kept OUT of the locks): the jar — whole, then
broken at the neck, then empty shards; the perfume — sealed, then
poured, then only its memory; the room — festive, then indignant, then
still.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "ROOM": (
        "ROOM LOCK: the supper room of a stone house in Bethany — a "
        "LOW TABLE with diners reclining around it on cushions, clay "
        "OIL LAMPS burning warm on the table and in wall niches, "
        "shuttered windows, deep shadow at the plastered walls. The "
        "same table, lamps and walls throughout."
    ),
    "WOMAN": (
        "WOMAN LOCK: the woman is the same in every shot — about "
        "thirty, dark hair under a DEEP OLIVE-GREEN shawl, a plain "
        "DARK OLIVE-GREEN dress (never cream, never white), steady "
        "dark eyes and composed, unhurried hands. She never speaks; "
        "her silence is strength, never cowering."
    ),
    "JAR": (
        "JAR LOCK: the perfume vessel is one small ALABASTER FLASK — "
        "pale veined translucent stone with a long sealed neck, small "
        "enough for two hands; when broken, it is snapped at the NECK, "
        "the body intact in her hands."
    ),
    "CRITICS": (
        "CRITICS LOCK: the indignant diners — men in DARK RUST-BROWN, "
        "CHARCOAL and DEEP SLATE robes (never cream, never white), "
        "sharp-gesturing and sure of their arithmetic; indignant but "
        "human, never cartooned."
    ),
}

REF = True

# AUDIO-FIX (AUDIO-FIX session, Machine A, 2026-08-06): the V1 mp4
# mark-14_anointing-at-bethany.mp4 is STALE vs this build's own narration — it
# fails BOTH tripwires in assert_v1_final_is_current (all 19 segment mp3s NEWER
# than the mp4 AND the mp4 runs ~+7s longer than the summed timeline, i.e. it
# carries old/deleted audio). Segment-ID parity with make_narration.py is exact
# (19/19), so rebuild the track from these segments at the extract offsets
# instead of copying the stale mp4. $0 — nothing re-voiced, nothing re-timed;
# V1 stays read-only. Same mechanism as the shipped row-69 fix.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r082-b01", "out": "s01-in-a-house-in-bethany.jpeg", "seg": "n0a",
        "window": "0.28-4.79", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "WOMAN"],
        "narration": (
            "In a house in Bethany, days before the end, a woman came to "
            "Jesus at the table."
        ),
        "must_show": "SCRIPTURE-EXACT: the supper and the approach — the lamplit table with Jesus reclining among the diners, and the olive-green woman entering the warm light toward him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the diners RECLINING at a low table (v3), not seated on chairs.",
        "scene": (
            "The lamplit supper room holds its evening, the camera "
            "at the side wall taking couches and door in profile: "
            "diners reclining on "
            "cushions around the low table, "
            "bread and cups in the small flames' "
            "light, Jesus among them at ease — "
            "and out of the deep shadow by the "
            "door a woman in olive-green comes "
            "quietly toward him along the "
            "table's edge, both hands carrying "
            "something small and pale, her "
            "steps the only movement the room "
            "has not yet noticed. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r082-b02", "out": "s02-she-carried-an-alabaster-jar.jpeg", "seg": "n0b",
        "window": "5.37-8.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "JAR"],
        "narration": "She carried an alabaster jar of pure, costly perfume.",
        "must_show": "SCRIPTURE-EXACT: the jar — close on the pale veined alabaster flask cradled in her two hands, its long neck still sealed; a year's wages in stone.",
        "must_not_show": "no halo, glare or rim-light; the flask SEALED and whole — the breaking not yet come.",
        "scene": (
            "Close on her two composed hands in "
            "the lamplight, cradling the small "
            "alabaster flask — pale veined "
            "stone with a faint translucence "
            "where the flame stands behind it, "
            "the long neck still sealed with "
            "its wax — a vessel the size of a "
            "dove holding a year of wages, "
            "carried through a crowded room "
            "the way you carry the one "
            "irreplaceable thing you own. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r082-b03", "out": "s03-and-poured-all-of-it.jpeg", "seg": "n1b",
        "window": "11.69-16.70", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "WOMAN", "JAR"],
        "narration": (
            "and poured all of it over his head — a year's wages, gone in a "
            "moment."
        ),
        "must_show": "SCRIPTURE-EXACT: the anointing ON HIS HEAD — the woman standing over the reclining Jesus, the broken-necked flask upended, the perfume running bright down his hair; the table turning to stare.",
        "must_not_show": "no halo, glare or rim-light; the pour COMPLETE — the flask fully upended, everything given; the perfume on the HEAD, not the feet.",
        "scene": (
            "She stands over him and gives it "
            "all: the broken-necked flask "
            "upended above Jesus's head, the "
            "precious oil running bright "
            "threads down the dark hair and "
            "into his beard in the lamplight — "
            "nothing held back, nothing saved "
            "for later, a year's wages leaving "
            "the stone in one unhurried pour — "
            "while around the low table the "
            "conversation dies and every "
            "reclining diner turns to stare. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r082-b04", "out": "s04-some-of-the-men-at.jpeg", "seg": "n2",
        "window": "17.27-21.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM", "CRITICS"],
        "narration": (
            "Some of the men at the table were furious. Mark writes down what "
            "they said:"
        ),
        "must_show": "SCRIPTURE-EXACT: the indignation — a knot of critics rearing up from their cushions: pointed fingers, hard faces, outrage breaking across the table.",
        "must_not_show": "no halo, glare or rim-light; the fury AT THE ACT — gestures toward the spent perfume, arithmetic on their faces.",
        "scene": (
            "The far side of the table rears "
            "up: critics pushing off their "
            "cushions, a rust-brown sleeve "
            "flung toward the dripping oil, a "
            "charcoal shoulder squared, faces "
            "hardening around the sum they are "
            "all computing at once — indignation "
            "travelling the table like a "
            "knocked cup spills — the room's "
            "warmth curdling in the little "
            "flames' light. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r082-b05", "out": "s05-why-was-this-waste-of.jpeg", "seg": "s4",
        "window": "22.47-30.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["CRITICS"],
        "narration": (
            "Why was this waste of the ointment made? For it might have been "
            "sold for more than three hundred pence, and have been given to "
            "the poor."
        ),
        "must_show": "SCRIPTURE-EXACT: the accounting — close on the lead critic mid-protest: fingers counting on fingers, the three hundred pence laid out in gesture; charity as a weapon.",
        "must_not_show": "no halo, glare or rim-light; the argument's SHAPE visible — counting hands, appeal to the room; sincerity and spite mixed.",
        "scene": (
            "Close on the lead critic in full "
            "protest: one hand counting off the "
            "other's fingers — three hundred "
            "pence, itemised in the air — his "
            "brows up in appeal to the whole "
            "table, the word WASTE still "
            "shaping his mouth — an argument "
            "with real arithmetic and real "
            "poor in it, swung all the same "
            "like a stick at a woman's bowed "
            "gift. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r082-b06", "out": "s06-and-mark-adds-one-more.jpeg", "seg": "n2b",
        "window": "32.10-35.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM", "CRITICS", "WOMAN"],
        "narration": "And Mark adds one more line: they murmured against her.",
        "must_show": "SCRIPTURE-EXACT: the murmuring — heads leaning together along the table, side-mouthed words aimed her way; the woman standing in the spill of it.",
        "must_not_show": "no halo, glare or rim-light; the murmur DIRECTED — glances cutting toward her as the words pass.",
        "scene": (
            "The protest drops to a murmur and "
            "gets meaner for it: heads leaning "
            "pair to pair along the table, "
            "words passed side-mouthed with "
            "glances that cut across the "
            "lamplight to where she stands — "
            "the empty flask still in her "
            "hands, the oil still bright in "
            "his hair — a room deciding "
            "against a woman in tones pitched "
            "exactly loud enough to reach her. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r082-b07", "out": "s07-they-said-it-where-she.jpeg", "seg": "n2b",
        "window": "35.27-39.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "They said it where she could hear it. She does not answer them.",
        "must_show": "her silence — close on the woman's composed face taking the murmur: steady dark eyes, no flinch, no reply forming; strength holding still.",
        "must_not_show": "no halo, glare or rim-light; NO cowering, NO tears — the silence chosen, her dignity untouched by the words landing on it.",
        "scene": (
            "Close on her face as the murmur "
            "reaches it: the steady dark eyes "
            "level under the olive shawl, the "
            "mouth at rest, not one muscle "
            "recruiting for a defence — the "
            "words landing on a composure that "
            "declines to be spent on them — a "
            "woman who emptied a year's wages "
            "without trembling, not about to "
            "tremble for table-talk. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r082-b08", "out": "s08-she-never-says-a-single.jpeg", "seg": "n2b + n3",
        "window": "39.01-45.28", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "WOMAN", "CRITICS"],
        "narration": (
            "She never says a single word in this whole story. Jesus stopped "
            "them cold, and defended her."
        ),
        "must_show": "the defence rising — Jesus pushing up from his recline, oil still bright in his hair, his raised hand cutting the murmur off; the room caught mid-word.",
        "must_not_show": "no halo, glare or rim-light; the murmur STOPPED — critics frozen mid-lean, the raised hand's authority instant.",
        "scene": (
            "Jesus comes up off his cushion "
            "with the perfume still bright in "
            "his hair — one hand rising into "
            "the murmur like a bar dropped "
            "across a road — and the table "
            "stops: leaning heads caught mid-"
            "lean, the lead critic's mouth "
            "open on half a word, the whole "
            "current of accusation dammed in "
            "an instant between the lamps — a "
            "silent woman about to be defended "
            "by the only voice that matters "
            "here. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r082-b09", "out": "s09-let-her-alone-why-trouble.jpeg", "seg": "j1",
        "window": "45.93-51.46", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "WOMAN", "CRITICS"],
        "narration": (
            "Let her alone; why trouble ye her? she hath wrought a good work "
            "on me."
        ),
        "must_show": "SCRIPTURE-EXACT: the shield — Jesus's words placed bodily between the critics and the woman: his gesture toward her honouring, toward them halting.",
        "must_not_show": "no halo, glare or rim-light; the defence WARM toward her, FIRM toward them — two tones in one posture.",
        "scene": (
            "The defence stands up between them, the camera at the "
            "table's side so the interposition reads in profile: "
            "Jesus half-turned so his "
            "halting palm faces the critics "
            "while his other hand opens toward "
            "the woman like a presentation — "
            "LET HER ALONE — the geometry of "
            "the room redrawn in one posture, "
            "her gift renamed from waste to "
            "GOOD WORK in front of the men "
            "still holding their arithmetic, "
            "the lamplight siding visibly with "
            "the accused. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r082-b10", "out": "s10-leave-her-alone-why-are.jpeg", "seg": "n3b",
        "window": "53.00-55.58", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CRITICS"],
        "narration": "Leave her alone. Why are you giving her a hard time?",
        "must_show": "the rebuke landing — close on the critics' faces taking it: indignation faltering, eyes dropping, the arithmetic suddenly not the point.",
        "must_not_show": "no halo, glare or rim-light; the faltering HUMAN — men rebuked, not destroyed; shame beginning, not theatrics.",
        "scene": (
            "Close on the critics as the "
            "rebuke lands: the lead man's "
            "counting hand sinking to the "
            "table, another's eyes dropping to "
            "his own cup, the fine indignation "
            "faltering face by face in the "
            "small flames' light — men who "
            "walked their argument out onto "
            "ice they were sure of, feeling "
            "it crack under the weight of one "
            "quiet question. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r082-b11", "out": "s11-she-has-done-a-beautiful.jpeg", "seg": "n3b",
        "window": "55.58-59.41", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": "She has done a beautiful thing for me. Not a wasteful thing.",
        "must_show": "the renaming — Jesus's face turned warm toward the woman, the verdict BEAUTIFUL passing directly to her; her steady eyes receiving it.",
        "must_not_show": "no halo, glare or rim-light; the exchange DIRECT — his face to hers, the word landing where the murmur had.",
        "scene": (
            "The frame holds the exchange that "
            "outweighs the table: Jesus's face "
            "turned full and warm toward the "
            "woman, the word BEAUTIFUL passing "
            "to her as directly as the murmur "
            "did, and her steady dark eyes "
            "receiving it without blinking — "
            "the same act, twice named in one "
            "evening, and only one of the "
            "names spoken by someone with the "
            "right to grade gifts given to "
            "himself. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r082-b12", "out": "s12-for-ye-have-the-poor.jpeg", "seg": "j1b",
        "window": "63.56-71.55", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "CRITICS"],
        "narration": (
            "For ye have the poor with you always, and whensoever ye will ye "
            "may do them good: but me ye have not always."
        ),
        "must_show": "SCRIPTURE-EXACT: the two clocks — Jesus speaking it soberly down the table; WHENSOEVER YE WILL laid against ME YE HAVE NOT ALWAYS; the shadow of the coming days in his steadiness.",
        "must_not_show": "no halo, glare or rim-light; NO morbid imagery — the not-always carried in tone and stillness only.",
        "scene": (
            "Jesus speaks it soberly down the "
            "length of the lamplit table — the "
            "poor always within reach of any "
            "day's kindness they choose, and "
            "himself, said evenly, NOT ALWAYS "
            "— and the sentence changes the "
            "room's temperature: cups going "
            "untouched, eyes lifting one by "
            "one to his steady face, the "
            "supper suddenly aware it is "
            "happening close to some edge "
            "nobody at the table can see over. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r082-b13", "out": "s13-and-then-he-answered-the.jpeg", "seg": "n4",
        "window": "60.08-62.91", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM"],
        "narration": "And then he answered the argument about the money directly:",
        "must_show": "the turn to the ledger — close on Jesus turning squarely toward the critics' side of the table, unafraid of their strongest point.",
        "must_not_show": "no halo, glare or rim-light; the turn DELIBERATE — a teacher walking toward the objection, not around it.",
        "scene": (
            "Close on Jesus turning squarely "
            "toward the critics' side of the "
            "table — not deflecting, not "
            "changing the subject, but walking "
            "straight at their strongest "
            "point, the three hundred pence "
            "and the poor — the warm eyes "
            "steady with the particular "
            "confidence of a man about to "
            "answer the best version of the "
            "argument against him. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r082-b14", "out": "s14-he-was-not-brushing-the.jpeg", "seg": "n4b",
        "window": "73.09-74.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM"],
        "narration": "He was not brushing the poor aside.",
        "must_show": "the poor honoured — a small true detail of the room: the door open to the dark lane where a beggar's bowl sits by the post; the poor real and near, not dismissed.",
        "must_not_show": "no halo, glare or rim-light; the beggar's presence DIGNIFIED — a fact of the street, not a prop of misery.",
        "scene": (
            "At the room's edge the open door "
            "frames the dark lane, and by its "
            "post in the spill of lamplight "
            "sits the small worn wooden bowl "
            "of the neighbourhood's beggar — "
            "ordinary, near, and permanent — "
            "the poor not banished from this "
            "story but standing quietly at its "
            "threshold, within reach of any "
            "evening's kindness, exactly as he "
            "said. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r082-b15", "out": "s15-he-was-telling-a-room.jpeg", "seg": "n4b",
        "window": "74.99-82.94", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "WOMAN", "CRITICS"],
        "narration": (
            "He was telling a room full of men that the window on this "
            "particular kindness was closing, and only one person in it had "
            "noticed."
        ),
        "must_show": "the one who noticed — the wide table: every male face turned to Jesus in confusion, and the woman apart in the lamplight, the only one whose face holds understanding.",
        "must_not_show": "no halo, glare or rim-light; the contrast in FACES — confusion around the table, comprehension on hers alone.",
        "scene": (
            "The wide room divides by what its faces know, the "
            "camera behind the near couches' shoulders: "
            "faces know: around the table the "
            "men look to Jesus in honest "
            "confusion — brows working, the "
            "closing window he speaks of "
            "invisible to every one of them — "
            "while apart in the warm lamplight "
            "the woman stands with the empty "
            "flask against her breast, her "
            "steady eyes the single pair in "
            "the room already looking at what "
            "is coming. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r082-b16", "out": "s16-she-hath-done-what-she.jpeg", "seg": "j2",
        "window": "83.47-88.81", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": (
            "She hath done what she could: she is come aforehand to anoint my "
            "body to the burying."
        ),
        "must_show": "SCRIPTURE-EXACT: the meaning revealed — close on Jesus speaking it gently, one hand indicating the oil in his own hair; the woman near, the word BURYING said without fear.",
        "must_not_show": "no halo, glare or rim-light; NO morbid imagery — the burying named in a calm face, the anointing already shining as its answer.",
        "scene": (
            "Close on Jesus as he gives the "
            "act its true name — one hand "
            "lifting to touch the oil still "
            "bright in his own hair — COME "
            "AFOREHAND, TO THE BURYING — the "
            "word spoken as calmly as a man "
            "names the next town on a road he "
            "has chosen, and beside him the "
            "woman's composed face bearing the "
            "meaning she paid a year's wages "
            "to say without words. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r082-b17", "out": "s17-she-did-what-she-was.jpeg", "seg": "n4c",
        "window": "90.29-95.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "JAR"],
        "narration": (
            "She did what she was able to do, he said. She has come ahead of "
            "time to prepare my body for burial."
        ),
        "must_show": "what she could — close on the woman's hands holding the broken empty flask: everything she was able to do, done; nothing withheld, nothing left.",
        "must_not_show": "no halo, glare or rim-light; the flask EMPTY and neck-broken — capability spent to its floor.",
        "scene": (
            "Close on her hands in the "
            "lamplight, holding what remains: "
            "the pale alabaster body empty to "
            "its last drop, the snapped neck's "
            "clean break catching the flame — "
            "the full inventory of what she "
            "was able to do, done — no second "
            "jar at home, no portion held "
            "back, a capability emptied all "
            "the way to its floor and resting "
            "there, complete. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r082-b18", "out": "s18-nobody-else-in-that-house.jpeg", "seg": "n4c",
        "window": "95.37-98.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM", "CRITICS"],
        "narration": "Nobody else in that house would even let him say the word.",
        "must_show": "the flinch — around the table, faces turning aside at the burial word: a wince, a shaken head, eyes finding the floor; a room refusing a truth.",
        "must_not_show": "no halo, glare or rim-light; the refusals SMALL and human — winces and averted eyes, not melodrama.",
        "scene": (
            "The word moves down the table and "
            "the table flinches from it: one "
            "man's head shaking a small "
            "involuntary NO, another's eyes "
            "dropping to the floorboards, a "
            "third turning his cup in his "
            "fingers as if the subject could "
            "be stirred away — a houseful of "
            "friends each privately declining "
            "the sentence their teacher keeps "
            "trying to hand them. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r082-b19", "out": "s19-whether-she-fully-knew-it.jpeg", "seg": "n5",
        "window": "99.16-104.78", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "WOMAN"],
        "narration": (
            "Whether she fully knew it or not, she was the only one in that "
            "room who had prepared him for what was coming."
        ),
        "must_show": "the preparation done — the anointed Jesus and the woman in one frame across the lamplit room: the deed finished and standing between them like a covenant.",
        "must_not_show": "no halo, glare or rim-light; the frame QUIET — the two connected by the completed act, the table's noise irrelevant to it.",
        "scene": (
            "Across the lamplit room the frame "
            "holds the two of them at once: "
            "Jesus with the burial oil bright "
            "in his hair, the woman with the "
            "emptied stone against her breast "
            "— the completed act stretched "
            "between them like a rope neither "
            "needs to name — the only two "
            "people at the supper standing on "
            "the same side of what is coming, "
            "one of them perhaps without "
            "fully knowing it. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r082-b20", "out": "s20-verily-i-say-unto-you.jpeg", "seg": "j3",
        "window": "105.41-116.28", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "WOMAN", "CRITICS"],
        "narration": (
            "Verily I say unto you, Wheresoever this gospel shall be preached "
            "throughout the whole world, this also that she hath done shall "
            "be spoken of for a memorial of her."
        ),
        "must_show": "SCRIPTURE-EXACT: the memorial decreed — Jesus proclaiming it to the whole room, hand open toward the woman: her deed bound to the gospel itself, forever.",
        "must_not_show": "no halo, glare or rim-light; the decree PUBLIC — spoken to everyone, the critics included, her honour set where no murmur can reach it.",
        "scene": (
            "Jesus raises the proclamation over the whole table, "
            "the camera at the room's side so speaker and hearers "
            "read in profile — "
            "the whole table — his open hand "
            "toward the woman in her olive-"
            "green, his voice taking in every "
            "critic and every friend at once: "
            "WHERESOEVER THIS GOSPEL SHALL BE "
            "PREACHED, THROUGHOUT THE WHOLE "
            "WORLD — a silent woman's evening "
            "deed welded to the good news "
            "itself in front of the men who "
            "called it waste, her memorial "
            "issued from the only bench there "
            "is no appealing. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r082-b21", "out": "s21-she-broke-the-jar-open.jpeg", "seg": "n1a",
        "window": "9.45-11.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "JAR"],
        "narration": "She broke the jar open,",
        "must_show": "SCRIPTURE-EXACT: the breaking — extreme close on her hands snapping the flask's sealed neck: the clean crack, the first bead of perfume at the break.",
        "must_not_show": "no halo, glare or rim-light; the break AT THE NECK, deliberate and final — a seal that can never be closed again.",
        "scene": (
            "Extreme close on the decision "
            "made irreversible: her two hands "
            "snapping the alabaster neck with "
            "one clean deliberate crack — the "
            "sealed stone giving way, the "
            "first bright bead of spikenard "
            "rising at the break — a container "
            "built to be opened once, opened "
            "— no stopper, no second "
            "thoughts, no way back from here "
            "but pouring. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r082-b22", "out": "s22-wherever-this-good-news-is.jpeg", "seg": "n6",
        "window": "117.83-125.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM", "WOMAN"],
        "narration": (
            "Wherever this good news is told, anywhere in the world, what she "
            "did today will be told with it, so she is remembered."
        ),
        "must_show": "the memorial begun — the woman by the lamplit table, the whole room's faces turned to her now in changed regard; the first telling of a story that never stops.",
        "must_not_show": "no halo, glare or rim-light; the regard CHANGED — the same faces that murmured now looking at her properly for the first time.",
        "scene": (
            "The room looks at her at last: "
            "around the low table the same "
            "faces that murmured an hour ago "
            "turn toward the woman in the "
            "lamplight with a new and "
            "unpractised regard — seeing, as "
            "if for the first time, the person "
            "who was there all along — the "
            "first audience of a story that "
            "from this supper onward will be "
            "told wherever the good news "
            "goes, without ever wearing out. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r082-b23", "out": "s23-she-gave-the-most-extravagant.jpeg", "seg": "n6",
        "window": "125.15-130.58", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": (
            "She gave the most extravagant thing she owned, and he received "
            "it as beautiful."
        ),
        "must_show": "the exchange summarized — the woman's composed face and Jesus's warm one in the lamplight: extravagance met with reception, giver and receiver at peace.",
        "must_not_show": "no halo, glare or rim-light; both faces at PEACE — the argument over, only the gift remaining between them.",
        "scene": (
            "The lamplight holds the two faces "
            "in their settled peace: hers "
            "composed under the olive shawl, "
            "the extravagance long gone from "
            "her hands and not one line of "
            "regret in her features — and his "
            "warm with the received gift, the "
            "oil still in his hair — giver and "
            "receiver resting on either side "
            "of a beautiful thing, the whole "
            "table's arithmetic quietly "
            "outspent. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r082-b24", "out": "s24-not-wasteful-worship.jpeg", "seg": "n6",
        "window": "130.58-133.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["JAR"],
        "narration": "Not wasteful — worship.",
        "must_show": "the verdict in an object — close on the broken alabaster pieces at rest on the table in the lamplight: emptiness as evidence of worship, not waste.",
        "must_not_show": "no halo, glare or rim-light; the shards HONOURED by the framing — laid like relics, not swept like trash.",
        "scene": (
            "Close on what the evening leaves "
            "on the table: the pale broken "
            "alabaster resting in the small "
            "flames' light — the emptied body, "
            "the snapped neck beside it — laid "
            "there like evidence in a case "
            "just decided: the same shards one "
            "verdict calls waste and the "
            "higher verdict calls worship, "
            "holding their emptiness the way "
            "an altar holds its ash. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r082-b25", "out": "s25-and-he-was-right-about.jpeg", "seg": "n6",
        "window": "133.49-140.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM", "WOMAN"],
        "narration": (
            "And he was right about the memorial: all these centuries later, "
            "here we are, telling her story."
        ),
        "must_show": "the closing image — the woman quietly leaving through the doorway into the night, the supper's lamplight behind her; a figure walking out of one evening and into every century.",
        "must_not_show": "no halo, glare or rim-light; the exit UNHURRIED and upright — remembered exactly as she left: composed, silent, complete.",
        "scene": (
            "The closing frame watches her go: "
            "the woman in olive-green passing "
            "out through the doorway into the "
            "soft dark of the Bethany night, "
            "upright and unhurried, the "
            "supper's warm lamplight laying "
            "one last gold stripe across her "
            "shoulder as she leaves — a figure "
            "stepping out of a single evening "
            "and into every century after it, "
            "her story already walking ahead "
            "of her. Every figure has two "
            "arms, two hands and one head."
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
