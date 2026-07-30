#!/usr/bin/env python3
"""V2 beat map — row 75, build-75-woman-taken-in-adultery (John 8:1-11).

COVERAGE: 21 pictures over 119.5 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (John 8:1-11 KJV):
  v2    "EARLY IN THE MORNING he came again into the temple, and all the
        people came unto him; and he SAT DOWN, and taught them" — the
        seated morning teaching interrupted.
  v3    "the scribes and Pharisees BROUGHT unto him a woman taken in
        adultery; and when they had SET HER IN THE MIDST" —
        ⚑ MAXIMUM-DIGNITY LAW: the woman is FULLY and modestly clothed
        in every frame — dishevelled, clutching her mantle closed,
        shamed by POSTURE only; the bringing is gripped arms and her
        stumbling, nothing rougher, nothing lurid, ever. Her exposure is
        social, rendered as the circle of staring; never physical.
  v5-6  the trap stated ("Moses ... commanded us, that such should be
        STONED: but what sayest thou?"), "TEMPTING him" — stones already
        in hands; the dilemma's two blades named by the narration.
  v6,8  "Jesus STOOPED DOWN, and with his finger WROTE ON THE GROUND" —
        twice; the writing never legible (scripture keeps its secret; so
        do we — abstract marks in dust only).
  v7    "He that is WITHOUT SIN among you, let him FIRST CAST A STONE" —
        the sentence that reverses the court.
  v9    "CONVICTED by their own conscience, went out ONE BY ONE,
        BEGINNING AT THE ELDEST" — the eldest-first exodus and the
        dropped stones are locked visual facts.
  v10-11 the empty court: "Woman, where are those thine accusers?" — "No
        man, Lord." — standing, in an empty courtyard, to the one person
        who had not walked away. "NEITHER DO I CONDEMN THEE: go, and sin
        no more." + the HUSH: a held silent breath after — the dropped
        stones on the empty pavement in the morning light.

TIME OF DAY: early morning throughout — the temple court's long low
light; the final beats in the same clean morning, the court emptied.

CONTENT-CARE: the row's entire handling is dignity — hers absolute, the
accusers' departure painted as conscience not rout, Jesus's writing
posture (down, not staring at her) itself mercy. Nothing about the sin
is depicted or hinted beyond the accusation's words.

CHANGING CONDITION (kept OUT of the locks): the stones — gripped, then
loosening, then DROPPED one by one on the pavement; the circle — dense,
thinning eldest-first, gone; the woman — dragged and huddled, then
standing, then sent.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "WOMAN": (
        "WOMAN LOCK: the woman is the same in every shot — late twenties, "
        "with a strong young face hollowed by terror, dark eyes that "
        "expect death, and dark hair fallen loose from its pins. She is "
        "FULLY, MODESTLY CLOTHED throughout: a rumpled DEEP RUST-RED "
        "dress and a DARK BROWN mantle she clutches closed at her "
        "throat with one fist in every early beat (never cream, never "
        "white; NOTHING immodest, nothing torn revealingly — her "
        "dishevelment is hair and rumpling only). Her face is shown "
        "clearly and with absolute dignity."
    ),
    "ACCUSERS": (
        "ACCUSERS LOCK: the scribes and Pharisees — a dense knot of "
        "eight to ten men in fine NEAR-BLACK INDIGO and DARK UMBER "
        "robes with fringed shawls, several with fist-sized stones "
        "already gripped, led by one tall WHITE-BEARDED ELDEST whose "
        "departure begins the exodus (never cream, never white). Faces "
        "shown clearly — righteous certainty, then conscience, never "
        "cartoons."
    ),
    "COURT": (
        "TEMPLE COURT LOCK: a paved corner of the temple's outer court "
        "in early morning — pale flagstones with wind-drifted DUST "
        "gathered along their seams (the writing surface), a low step "
        "where a teacher sits, columns behind, and long low morning "
        "light raking the pavement. The same flagstones, dust, step "
        "and light throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r075-b01", "out": "s01-early-morning-at-the-temple.jpeg", "seg": "n0",
        "window": "0.28-9.75", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "ACCUSERS", "COURT"],
        "narration": (
            "Early morning at the temple, Jesus was teaching a crowd, when a "
            "knot of religious leaders shoved their way through — dragging a "
            "woman with them."
        ),
        "must_show": "SCRIPTURE-EXACT: the interruption — the seated morning teaching split open by the accusers' knot pushing through, the woman gripped by the arms between them, stumbling, mantle clutched closed.",
        "must_not_show": "⚑ NOTHING rough beyond gripped arms and her stumble; fully clothed, mantle held shut; the crowd parting in dismay, not appetite.",
        "scene": (
            "The long low morning light rakes the "
            "temple court where Jesus sits teaching on "
            "the low step — and the lesson splits open: "
            "a dense knot of fine-robed men shoves "
            "through the parting crowd with the woman "
            "gripped by both arms between them, her "
            "feet stumbling to keep their pace, her "
            "free fist clutching her dark mantle closed "
            "at her throat, her loose hair fallen "
            "across a face hollowed with terror — "
            "morning instruction becoming, in ten "
            "steps, a tribunal. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r075-b02", "out": "s02-they-stood-her-in-the.jpeg", "seg": "n1",
        "window": "10.41-14.18", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "ACCUSERS", "COURT"],
        "narration": (
            "They stood her in the middle of everyone, where no one could look "
            "away."
        ),
        "must_show": "SCRIPTURE-EXACT: set in the midst — the woman placed alone at the circle's centre, the staring ring closed around her; exposure as geometry, her body huddled and covered.",
        "must_not_show": "⚑ the exposure SOCIAL only — the circle of eyes the whole violence; she covered, hunched, dignity intact under shame's posture.",
        "scene": (
            "In the court's centre the circle closes: "
            "the woman placed alone on the pale "
            "flagstones with the staring ring shutting "
            "around her — accusers at the front with "
            "their stones, the morning crowd pressed "
            "behind — and she stands hunched into "
            "herself at the middle of all of it, "
            "mantle fisted shut, eyes down at the "
            "dust, one woman being punished first "
            "with geometry: the midst, where no one "
            "can not look. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r075-b03", "out": "s03-they-had-caught-her-they.jpeg", "seg": "n1",
        "window": "14.18-17.33", "wide": False, "jesus": False, "ref": False,
        "locks": ["ACCUSERS"],
        "narration": "They had caught her, they said, in the act itself.",
        "must_show": "the accusation's relish — close on the lead accuser mid-declaration: the charge delivered loud, one arm flung at her; prosecution enjoying its case.",
        "must_not_show": "no halo, glare or rim-light; the relish subtle — certainty pleased with itself; nothing about the act depicted or gestured.",
        "scene": (
            "Close on the lead accuser mid-"
            "declaration: the charge going out at "
            "public volume, one arm flung back toward "
            "the huddled woman, his fine-robed chest "
            "expanded with the case's strength — and "
            "in the corners of the correct face, "
            "unhidden, the small relish of a "
            "prosecutor holding what he believes is a "
            "winning hand in a game the woman was "
            "only ever the board for. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r075-b04", "out": "s04-and-then-they-turned-to.jpeg", "seg": "n1",
        "window": "17.33-23.65", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "ACCUSERS", "COURT"],
        "narration": (
            "And then they turned to Jesus, put the law of Moses on the table "
            "between them, and made him answer for it."
        ),
        "must_show": "the trap aimed — the accusers' faces pivoting from the woman to Jesus as one; the true target revealed by the synchronized turn.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the pivot the tell — her ordeal instrumental, his answer the actual quarry.",
        "scene": (
            "As one the accusers' faces pivot — off "
            "the huddled woman and onto the seated "
            "teacher — the whole knot's attention "
            "swinging like a weathervane to its true "
            "north: stones still gripped, the charge "
            "still echoing, but every eye now on "
            "Jesus and every posture waiting on HIS "
            "next word — a woman's life reduced, in "
            "one synchronized turn, to the bait in a "
            "question. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r075-b05", "out": "s05-master-this-woman-was-taken.jpeg", "seg": "s4",
        "window": "24.21-27.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "ACCUSERS"],
        "narration": "Master, this woman was taken in adultery, in the very act.",
        "must_show": "SCRIPTURE-EXACT: the charge formal — the accuser's declaring face and pointing arm, and beyond the point, the woman flinching at each public word; the sentence as stones already.",
        "must_not_show": "⚑ nothing of the act evoked visually — the words land on her bowed head as blows of sound only.",
        "scene": (
            "The formal charge goes out word by "
            "public word — the accuser's arm rigid "
            "toward her, his voice's volume visible "
            "in the cords of his neck — and at the "
            "point's far end the woman flinches "
            "minutely at each landing syllable, "
            "shoulders tightening under the mantle, "
            "eyes shut now, a person being described "
            "at maximum volume to a crowd, in the "
            "third person, three feet from her own "
            "ears. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r075-b06", "out": "s06-now-moses-in-the-law.jpeg", "seg": "s4",
        "window": "27.62-34.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["ACCUSERS"],
        "narration": (
            "Now Moses in the law commanded us, that such should be stoned: but "
            "what sayest thou?"
        ),
        "must_show": "SCRIPTURE-EXACT: the law tabled — a gripped stone lifted slightly with the citation, Moses invoked with rock in hand; the question's teeth bared courteously.",
        "must_not_show": "no halo, glare or rim-light; the stone's small lift the punctuation — law and lethality in one fist.",
        "scene": (
            "With the citation the evidence rises: a "
            "fist-sized stone lifted slightly in a "
            "fine-sleeved grip as Moses is invoked — "
            "the law's name and the rock's weight "
            "presented together, courteous as a "
            "contract — while around the speaker "
            "other stones shift in other hands, a "
            "whole legal argument standing in the "
            "morning light with its verdict already "
            "distributed among its knuckles. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r075-b07", "out": "s07-it-was-a-trap.jpeg", "seg": "n2",
        "window": "35.53-36.47", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "It was a trap.",
        "must_show": "the trap as object — a close still: a hunter's snare staked in dust, jaws set and waiting; the question's true architecture.",
        "must_not_show": "no halo, glare or rim-light; the metaphor spare — one set snare, nothing caught yet.",
        "scene": (
            "A close still in the raking light: a "
            "hunter's simple snare staked in the "
            "dust — the loop set, the trigger-stick "
            "balanced, the whole patient geometry of "
            "capture waiting in plain view for "
            "anything that answers its one question "
            "either way — a small machine built, "
            "like the morning's, so that every "
            "possible move springs it. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r075-b08", "out": "s08-say-stone-her-and-just.jpeg", "seg": "n2 + n3",
        "window": "39.04-45.15", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COURT"],
        "narration": (
            "Say stone her, and he's just another man with a rock. Jesus said "
            "nothing at first."
        ),
        "must_show": "the first silence — Jesus seated, saying nothing, the question hanging; his stillness against the court's coiled waiting.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the nothing deliberate — silence as the trap's first unspringing.",
        "scene": (
            "The question hangs and Jesus gives it "
            "nothing: seated on the low step in the "
            "long light, hands loose, face quiet, the "
            "silence stretching one breath past "
            "comfortable and then another — the "
            "accusers' coiled waiting beginning to "
            "shift its weight, a trap discovering "
            "that its trigger requires an answer, and "
            "that the answer is in no hurry to exist. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r075-b09", "out": "s09-he-bent-down-and-wrote.jpeg", "seg": "n3",
        "window": "45.15-49.32", "wide": True, "jesus": True, "ref": REF,
        "locks": ["COURT"],
        "narration": (
            "He bent down and wrote in the dust with his finger. Then he "
            "straightened up."
        ),
        "must_show": "SCRIPTURE-EXACT: the writing — Jesus stooped, finger tracing marks in the seam-drifted dust; the marks ABSTRACT, never legible; the court craning despite itself.",
        "must_not_show": "the writing's content NEVER readable — abstract strokes only (scripture keeps the secret); no halo, glare or rim-light.",
        "scene": (
            "Jesus stoops from the step and writes: "
            "one finger tracing slow deliberate marks "
            "in the wind-drifted dust along the "
            "flagstone seams — strokes the frame "
            "keeps as strokes, abstract and private "
            "as scripture left them — while around "
            "the stooped figure the whole court "
            "cranes despite itself, accusers and "
            "crowd together, their tribunal's "
            "momentum leaking away into curiosity "
            "about a patch of dust. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r075-b10", "out": "s10-he-that-is-without-sin.jpeg", "seg": "j1",
        "window": "49.90-54.68", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "ACCUSERS", "COURT"],
        "narration": (
            "He that is without sin among you, let him first cast a stone at "
            "her."
        ),
        "must_show": "SCRIPTURE-EXACT: THE sentence — Jesus risen to his feet giving it level across the stones' whole arsenal; the words arriving on each gripped fist like a weight.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the sentence at law-court calm — one condition, universally disqualifying, delivered standing.",
        "scene": (
            "Risen now to his feet Jesus gives the "
            "sentence level across the court — one "
            "condition, spoken at the calm of "
            "settled law — and it lands on the "
            "arsenal fist by fist: the lifted stone "
            "sinking an inch, a grip loosening at "
            "the third row, the lead accuser's arm "
            "lowering as the qualification audits "
            "every hand in the circle at once and "
            "finds, in the whole morning, not one "
            "eligible thrower. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r075-b11", "out": "s11-whichever-one-of-you-has.jpeg", "seg": "n4a",
        "window": "56.07-63.10", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ACCUSERS"],
        "narration": (
            "Whichever one of you has never sinned, he said — you go first. He "
            "did not argue the law with them."
        ),
        "must_show": "the non-argument — Jesus's open hand indicating the woman's direction: the throw formally invited; the law un-argued, the queue simply reordered.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the invitation genuine in form — proceed, on the one condition; no one moving.",
        "scene": (
            "Jesus's open hand turns in the formal "
            "gesture of invitation — the direction "
            "clear, the floor yielded, the first "
            "throw officially available to any "
            "qualified applicant — and the knot of "
            "accusers stands in the long light "
            "holding its stones like men suddenly "
            "asked for credentials at a door they "
            "built themselves: the law un-argued, "
            "untouched, and entirely out of their "
            "reach. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r075-b12", "out": "s12-he-just-handed-the-first.jpeg", "seg": "n4a",
        "window": "63.10-67.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["ACCUSERS"],
        "narration": (
            "He just handed the first stone to anybody who had earned the right "
            "to throw it."
        ),
        "must_show": "the stone's new weight — extreme close: one gripped stone in a fine-sleeved fist, the knuckles' certainty visibly failing around it.",
        "must_not_show": "no halo, glare or rim-light; the loosening grip the whole beat — conviction draining through fingers.",
        "scene": (
            "Extreme close in the raking light: one "
            "fist-sized stone in a fine-sleeved "
            "grip — and the grip failing by degrees, "
            "the white knuckles pinking as they "
            "loosen, the stone's weight doubling in "
            "a hand that arrived certain — a rock "
            "discovering, in real time, that it has "
            "no thrower, held by fingers doing "
            "arithmetic on their own history. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r075-b13", "out": "s13-say-let-her-go-and.jpeg", "seg": "n2",
        "window": "36.47-39.04", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Say let her go, and he breaks the law.",
        "must_show": "the trap's other blade — the snare still-life's counterpart: an opened scroll of the law beside the staked snare; both jaws of the dilemma in one frame.",
        "must_not_show": "no halo, glare or rim-light; the two objects the two blades — rock's law, mercy's cost.",
        "scene": (
            "The still-life completes its trap: "
            "beside the staked snare in the dust an "
            "opened scroll of the law lies weighted "
            "flat, its dense columns holding the "
            "commandment — the dilemma's two jaws "
            "arranged in one frame: cite the scroll "
            "and become the stone's accomplice, "
            "spare the woman and stand against the "
            "ink — a question engineered so both "
            "answers close on the answerer. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r075-b14", "out": "s14-and-they-which-heard-it.jpeg", "seg": "s9",
        "window": "67.67-80.07", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "ACCUSERS", "COURT"],
        "narration": (
            "And they which heard it, being convicted by their own conscience, "
            "went out one by one, beginning at the eldest, even unto the last: "
            "and Jesus was left alone, and the woman standing in the midst."
        ),
        "must_show": "SCRIPTURE-EXACT: the exodus — the WHITE-BEARDED ELDEST turning away FIRST, his stone left on the pavement; behind him the one-by-one departure beginning; conscience as procession.",
        "must_not_show": "no halo, glare or rim-light; the departure conscience, not rout — heads bowed, stones set down not flung; eldest first exactly.",
        "scene": (
            "The exodus begins where scripture says: "
            "the tall white-bearded eldest turns away "
            "first — his stone set down on the "
            "flagstones with an old man's care, his "
            "head bowed under sixty years of "
            "remembered ledger — and behind him the "
            "procession forms one by one, each man's "
            "rock left on the pavement, each face "
            "aged by its own audit, the circle "
            "thinning from its greyest edge inward "
            "while the woman stands unstoned in the "
            "midst. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r075-b15", "out": "s15-and-he-bent-down-and.jpeg", "seg": "n4",
        "window": "81.42-83.14", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COURT"],
        "narration": "And he bent down and wrote again.",
        "must_show": "SCRIPTURE-EXACT: the second writing — Jesus stooped again to the dust, finger moving; his down-turned attention giving the departing men their privacy and the woman her first unstared-at moment.",
        "must_not_show": "the marks still never legible; no halo, glare or rim-light; the mercy OF the posture — eyes down while consciences work.",
        "scene": (
            "Jesus stoops to the dust a second time — "
            "finger tracing its private strokes along "
            "the flagstone seam, his face turned "
            "down and away from everyone — and the "
            "posture does its double mercy: the "
            "departing men leave unwatched, spared "
            "an audience for their conviction, and "
            "the woman stands for the first time all "
            "morning inside nobody's stare — a court "
            "emptied gently, by a man looking at "
            "dust. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r075-b16", "out": "s16-they-dropped-their-stones-and.jpeg", "seg": "n4",
        "window": "83.14-90.29", "wide": True, "jesus": False, "ref": False,
        "locks": ["COURT"],
        "narration": (
            "They dropped their stones and walked away, one by one — the oldest "
            "first — until it was only the two of them."
        ),
        "must_show": "the stones' testament — the emptying court: the scatter of dropped stones across the pavement where each man stood, the last robed backs going; the arsenal, abandoned in place.",
        "must_not_show": "no halo, glare or rim-light; each stone WHERE its holder stood — a map of departed consciences on flagstone.",
        "scene": (
            "The court empties to its evidence: "
            "across the pale flagstones the dropped "
            "stones lie scattered each where its "
            "holder stood — a rough circle of "
            "abandoned verdicts mapping the vanished "
            "crowd — while at the colonnade's far "
            "shadow the last two robed backs pass "
            "out of the morning, and the long light "
            "rakes an arsenal that lost its whole "
            "army to one sentence. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r075-b17", "out": "s17-woman-where-are-those-thine.jpeg", "seg": "j2",
        "window": "90.93-95.34", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "COURT"],
        "narration": "Woman, where are those thine accusers? hath no man condemned thee?",
        "must_show": "SCRIPTURE-EXACT: the two alone — Jesus risen, addressing her across the emptied court with the morning's first gentle question; the vast cleared space around the two of them.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the emptiness the miracle's stage — acres of vacated judgment around one question.",
        "scene": (
            "In the emptied court the two stand in "
            "acres of morning light: the woman still "
            "at the midst where they set her, mantle "
            "fisted, hardly believing the silence — "
            "and Jesus risen from his writing, "
            "asking her the day's first gentle "
            "question across the scattered stones — "
            "the space around them enormous with "
            "departed accusers, a tribunal reduced "
            "to two people and the wind. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r075-b18", "out": "s18-no-man-lord-where-are.jpeg", "seg": "w11 + n5",
        "window": "96.80-101.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "No man, Lord. Where are the ones accusing you, he asked her.",
        "must_show": "SCRIPTURE-EXACT: her three words — close on the woman's face lifting to answer: 'No man, Lord' — the first words the morning has allowed her, spoken STANDING.",
        "must_not_show": "no halo, glare or rim-light; the standing the dignity — a defendant discovering the court has dissolved and her voice still works.",
        "scene": (
            "Close on the woman's face as it lifts "
            "for the first time: the terror-hollowed "
            "features finding, in the emptied "
            "morning, that her voice still works — "
            "the three words leaving her small and "
            "steadying, 'No man, Lord' — spoken "
            "standing, upright at the midst that "
            "was built for her execution, to the "
            "one person in Jerusalem who stayed. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r075-b19", "out": "s19-has-no-one-condemned-you.jpeg", "seg": "n5",
        "window": "101.77-103.32", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": "Has no one condemned you?",
        "must_show": "the question's kindness — the two faces at conversing distance: his gentle inquiry, her dawning comprehension that the answer is actually no.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the comprehension arriving — condemnation counted and found absent.",
        "scene": (
            "At conversing distance the two faces "
            "hold: his carrying the question with "
            "the gentleness of a man helping "
            "someone count survivors — and hers "
            "doing the count: the circle gone, the "
            "stones grounded, the sentence "
            "unexecuted — comprehension arriving by "
            "slow degrees that the arithmetic of "
            "the morning has come out, impossibly, "
            "at zero. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r075-b20", "out": "s20-three-words-the-only-three.jpeg", "seg": "n5",
        "window": "103.32-113.66", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "COURT"],
        "narration": (
            "Three words — the only three the Bible gives her, and she got to "
            "say them standing up, in an empty courtyard, to the one person who "
            "had not walked away."
        ),
        "must_show": "the standing honoured — the woman at her full height now in the emptied court, mantle settled, facing the one who stayed; her uprightness the beat's whole content.",
        "must_not_show": "no halo, glare or rim-light; the transformation postural — dragged in bent, standing straight; the empty court her courtroom won.",
        "scene": (
            "The woman stands at her full height in "
            "the morning court — the hunch gone out "
            "of her shoulders, the mantle settled "
            "and released from her fist, her loose "
            "hair pushed back from a face still wet "
            "but level — upright at the exact centre "
            "where they set her to be broken, in an "
            "emptied courtyard, before the one "
            "person of the whole morning's hundreds "
            "who did not walk away. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r075-b21", "out": "s21-neither-do-i-condemn-thee.jpeg", "seg": "j3 + HUSH",
        "window": "114.27-118.47", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "COURT"],
        "narration": "Neither do I condemn thee: go, and sin no more.",
        "must_show": "SCRIPTURE-EXACT + the HUSH: the release — the words given, the woman turning free toward the colonnade's morning; and the held silent breath after: the dropped stones scattered on the empty sunlit pavement.",
        "must_not_show": "no halo, glare or rim-light; the HUSH honoured — the final stillness resting on the abandoned stones in the long light; mercy's aftermath, unnarrated.",
        "scene": (
            "The sending and the hush hold the last "
            "frame together: the woman turning free "
            "toward the colonnade with the words "
            "still settling over her — go, and sin "
            "no more — her step new and her spine "
            "carrying the morning's impossible "
            "verdict — and after her, in the held "
            "silent breath, the court's testament "
            "lies where conscience left it: the "
            "scattered stones on the empty sunlit "
            "pavement, each one still exactly as "
            "heavy as a sinless hand. Every figure "
            "has two arms, two hands and one head."
        ),
    },
]
