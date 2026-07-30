#!/usr/bin/env python3
"""V2 beat map — row 63, build-63-man-born-blind (John 9).

COVERAGE: 43 pictures over 242.5 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (John 9 KJV):
  v1    "a man which was BLIND FROM HIS BIRTH" — his begging spot is a
        fixed daily place near the temple approach; his blindness is
        painted with complete dignity: milk-pale unseeing eyes, a
        listening face, practised hands. NEVER pitiable caricature.
  v2    "Master, who did sin, this man, or his parents?" — the disciples'
        question asked IN FRONT of the man, who hears everything; his
        hearing of it is a beat.
  v3    "NEITHER ... but that the works of God should be made manifest in
        him" — the equation thrown out; Jesus's answer dignifies before
        it heals.
  v6    "he SPAT on the ground, and made CLAY of the spittle, and he
        ANOINTED the eyes of the blind man with the clay" — Genesis echo
        (dust of the ground): the kneeling, the making, the gentle
        spreading — the maker finishing his work with the first
        material. Painted tender and unhurried.
  v7    "Go, WASH in the pool of SILOAM" — the mud-eyed walk across
        Jerusalem is the faith: one wall, one step at a time. The
        washing and FIRST SIGHT: light rendered as WHAT HE SEES (water,
        hands, sky, colour), never as glow or rays.
  v8-34 the neighbours' dispute; TWO interrogations; the parents' fear;
        "WHEREAS I WAS BLIND, NOW I SEE"; cast out of the synagogue.
        The leaders are hard, correct men — not cartoons.
  v35-38 "Jesus HEARD that they had cast him out; and when he had FOUND
        him" — the finding is the row's heart; "Who is he, Lord, that I
        might believe?" — the first face he ever studied is his healer's;
        "Lord, I believe. And he WORSHIPPED him" — in the public street.

TIME OF DAY: one long day — bright morning at the begging spot, midday
for the clay and the walk, early afternoon at Siloam and the return,
interior light for the interrogations, and warm late-gold for the
finding, the belief and the street worship. All one narrative day's arc.

CONTENT-CARE: healing dignity laws apply — the man's blindness and his
healed state are both painted with full personhood; no grotesquerie, no
medical detail beyond the clay and the pale eyes; the clay-making shown
as craft, the spittle implied not depicted.

CHANGING CONDITION (kept OUT of the locks): THE EYES — milk-pale and
unseeing through the first half; clay-covered for the walk; clear deep
brown after Siloam. Also his social state: beggar, celebrity, defendant,
outcast, worshipper. All per-beat.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "BLINDMAN": (
        "BORN-BLIND MAN LOCK: the man is the same in every shot — about "
        "thirty-five, lean and alert, with a strong intelligent face, "
        "unruly black hair, a short dark beard and quick expressive "
        "hands that read the world. He wears a patched DARK RUST-BROWN "
        "tunic with a rope belt and a worn DARK GREY shoulder cloth "
        "(never cream, never white). His face is shown clearly and "
        "with full dignity in every state — the EYES are per-beat: "
        "milk-pale before Siloam, clear deep brown after."
    ),
    "LEADERS": (
        "INQUISITORS LOCK: the religious examiners are the same three "
        "men in every shot — a tall cold senior with a long iron-grey "
        "beard; a stocky precise one with a scribe's squint; a younger "
        "zealous one with a thin dark beard. They wear finely woven "
        "NEAR-BLACK INDIGO and DARK UMBER robes with fringed shawls "
        "(never cream, never white). Faces shown clearly — hard, "
        "correct men, never cartoons."
    ),
    "SPOT": (
        "BEGGING SPOT LOCK: the man's daily place — a worn hollow in "
        "the dust beside a pale stone wall on the temple approach "
        "street, a folded mat, a wooden begging bowl, and the passing "
        "feet of Jerusalem. The same wall, hollow, mat and bowl in "
        "every begging beat."
    ),
    "STREETS": (
        "JERUSALEM STREETS LOCK: the walking route — stepped stone "
        "lanes descending the city, walls close on both sides, "
        "doorways and market noise, stone stairs worn hollow, down "
        "and down toward the pool. The same descending character in "
        "every walk beat."
    ),
    "SILOAM": (
        "POOL OF SILOAM LOCK: the pool — broad stone steps descending "
        "into clear green-tinged water at the city's lowest corner, "
        "pale walls around three sides, washing jars at the top step, "
        "open sky above. The same steps, water and walls throughout."
    ),
    "HALL": (
        "EXAMINATION HALL LOCK: the synagogue's council room — a "
        "stone chamber with a bench for the examiners along one wall, "
        "high slit windows, a scribe's table with ink and tablets, "
        "and a heavy door to the street. The same bench, windows and "
        "door for both interrogations."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r063-b01", "out": "s01-in-jerusalem-there-was-a.jpeg", "seg": "n0",
        "window": "0.28-6.42", "wide": True, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "SPOT"],
        "narration": (
            "In Jerusalem there was a man who begged at his same spot every "
            "day, because he had been sightless from birth."
        ),
        "must_show": "the man and his spot — the blind man seated in his worn dust-hollow by the pale wall, bowl before him, face lifted and listening to the street; his eyes milk-pale, his dignity complete.",
        "must_not_show": "no halo, glare or rim-light; NO pitiable caricature — an intelligent man at his fixed post, reading the world by ear.",
        "scene": (
            "In the bright morning on the temple approach "
            "the man sits in his worn hollow beside the "
            "pale wall — mat folded under him, wooden bowl "
            "set at the exact reach of long habit — his "
            "strong face lifted and turning slightly with "
            "the street's sounds, milk-pale eyes open on "
            "nothing, quick hands at rest on his knees: a "
            "fixture of the street, known to every foot "
            "that passes and looked at by almost none. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r063-b02", "out": "s02-he-had-never-seen-his.jpeg", "seg": "n0",
        "window": "6.42-10.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "SPOT"],
        "narration": "He had never seen his mother's face. Never seen morning.",
        "must_show": "the deprivation's size — close on his face turned toward the morning sun he can feel and not see: warmth on the skin, nothing in the pale eyes.",
        "must_not_show": "no halo, glare or rim-light; the sun FELT, not seen — his face reading warmth the only way it can.",
        "scene": (
            "Close on the man's face turned full into the "
            "morning sun: the warmth plainly landing on "
            "his skin — brow eased, head tipped like a "
            "man listening to light — while the milk-pale "
            "eyes beneath stay open and empty of every "
            "one of the thirty-five mornings that have "
            "crossed them: a daily appointment with a sun "
            "he knows only as weather on his face. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b03", "out": "s03-and-as-jesus-and-his.jpeg", "seg": "n0",
        "window": "10.59-15.14", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN", "SPOT"],
        "narration": "And as Jesus and his disciples passed by, the disciples asked him:",
        "must_show": "SCRIPTURE-EXACT: the passing — Jesus and the disciples coming along the street, the disciples' heads already turning toward the seated beggar as the question forms.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the man IN EARSHOT — the geometry that makes the question cruel.",
        "scene": (
            "Along the bright approach street Jesus walks "
            "with four disciples — and their heads are "
            "already turned toward the seated blind man "
            "as they come, one leaning to another with "
            "the question visibly forming, close enough "
            "that every word will land in the beggar's "
            "listening ears — while Jesus's own gaze goes "
            "to the man himself, not to the puzzle of "
            "him. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r063-b04", "out": "s04-master-who-did-sin-this.jpeg", "seg": "s2",
        "window": "15.77-20.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "SPOT"],
        "narration": (
            "Master, who did sin, this man, or his parents, that he was born "
            "blind?"
        ),
        "must_show": "the question heard — close on the blind man's face as the old question lands AGAIN: the faint practised flinch of a man who has been a theology example all his life.",
        "must_not_show": "no halo, glare or rim-light; his hearing of it the beat — weariness, not anger; a lifetime of being discussed.",
        "scene": (
            "Close on the man's face in the street's "
            "brightness as the question floats down to "
            "him: the faint, practised stillness of a man "
            "hearing his own life debated over his head "
            "one more time — jaw setting slightly, pale "
            "eyes steady, hands quiet on his knees — a "
            "human being listening, for the thousandth "
            "time, to strangers asking whose fault he is. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r063-b05", "out": "s05-notice-they-did-not-ask.jpeg", "seg": "n0b",
        "window": "21.80-25.98", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Notice they did not ask whether somebody was at fault. They asked "
            "which one."
        ),
        "must_show": "the assumption exposed — the disciples' earnest faces mid-question: good men inside a bad equation, genuinely curious, blind to the cruelty.",
        "must_not_show": "no halo, glare or rim-light; no malice — the question honest and the honesty the problem.",
        "scene": (
            "Close on two disciples' faces in the bright "
            "street: earnest, furrowed, genuinely "
            "curious — one hand half-raised in the "
            "posture of theological inquiry, both faces "
            "wholly unaware that the subject of the "
            "seminar sits listening three feet below "
            "them — good men operating faithfully inside "
            "an equation nobody has ever asked them to "
            "check. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r063-b06", "out": "s06-it-was-the-standard-theology.jpeg", "seg": "n1",
        "window": "30.55-36.17", "wide": True, "jesus": False, "ref": False,
        "locks": ["SPOT"],
        "narration": (
            "It was the standard theology of the day: if you are suffering, "
            "somebody must have earned it."
        ),
        "must_show": "the equation at street scale — passers-by giving the beggar the whole spectrum of the doctrine: averted eyes, a coin dropped at arm's length, a pitying head-shake.",
        "must_not_show": "no halo, glare or rim-light; the doctrine in body language — distance, judgment, charity with tongs.",
        "scene": (
            "The street passes its verdicts in the bright "
            "light: a robed man giving the begging spot a "
            "careful wide berth, a woman dropping her "
            "coin into the bowl at the fullest stretch "
            "of her arm, an elder pausing to shake his "
            "head with grave pity before moving on — "
            "the standard theology walking past in "
            "sandals, each foot writing the same "
            "sentence: somebody earned this. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b07", "out": "s07-people-still-run-that-math.jpeg", "seg": "n1",
        "window": "36.17-39.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["BLINDMAN"],
        "narration": "People still run that math on themselves today.",
        "must_show": "the math internalized — the blind man's own face running it: the old private question 'what did I do?' resting in the set of his features.",
        "must_not_show": "no halo, glare or rim-light; self-accusation quiet — a lifetime's arithmetic done in a face.",
        "scene": (
            "Close on the man alone at his spot in the "
            "midday light, the street briefly empty: his "
            "strong face fallen into its private "
            "resting question — brows drawn faintly, "
            "mouth set, the look of a man running a "
            "lifetime's audit for the sin that would "
            "explain him and finding, as always, no "
            "entry — the cruellest math in the world, "
            "done nightly, on oneself. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b08", "out": "s08-jesus-threw-the-whole-equation.jpeg", "seg": "n1",
        "window": "39.30-42.48", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SPOT"],
        "narration": "Jesus threw the whole equation out.",
        "must_show": "the equation refused — Jesus's face turning from the disciples' question with visible refusal, his attention descending fully to the seated man instead.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the pivot of attention — from puzzle to person, painted in one head-turn.",
        "scene": (
            "Close on Jesus in the bright street: the "
            "disciples' question still hanging behind "
            "him, and his face already turning from it — "
            "the refusal visible in the movement itself — "
            "his warm eyes descending to the seated man "
            "at the wall with the complete attention one "
            "gives a person rather than a problem, the "
            "whole standard theology dismissed by the "
            "direction of one gaze. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b09", "out": "s09-neither-hath-this-man-sinned.jpeg", "seg": "j1",
        "window": "43.00-49.69", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN", "SPOT"],
        "narration": (
            "Neither hath this man sinned, nor his parents: but that the works "
            "of God should be made manifest in him."
        ),
        "must_show": "SCRIPTURE-EXACT: the acquittal — Jesus speaking it OVER the seated man so he hears every word: the first public 'not guilty' of his life landing on his lifted face.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the man's RECEIPT of the words the beat — a verdict thirty-five years late arriving.",
        "scene": (
            "Jesus stands close over the seated man and "
            "gives the answer aloud to the street — and "
            "below him the blind man's lifted face is "
            "taking it in like rain on dry ground: the "
            "practised stillness cracking, lips parting, "
            "the first NOT GUILTY of his entire life "
            "arriving from a stranger's voice in front "
            "of witnesses — acquitted at his own begging "
            "spot before he is ever healed. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b10", "out": "s10-fault-not-a-punishment.jpeg", "seg": "n2",
        "window": "50.79-53.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["BLINDMAN"],
        "narration": "Nobody's fault. Not a punishment.",
        "must_show": "the verdict absorbed — extreme close on the man's face as the two sentences settle: a lifetime's weight visibly beginning to shift.",
        "must_not_show": "no halo, glare or rim-light; the shift subtle — an audit closing, an old debt zeroed on a face.",
        "scene": (
            "Extreme close on the man's face in the "
            "street light: the two short sentences "
            "settling through him in real time — the "
            "drawn brows easing a degree, the set mouth "
            "loosening, a long-held breath going out "
            "through the beard — thirty-five years of "
            "silent self-arithmetic being zeroed by "
            "eleven words from a voice he has never "
            "seen. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r063-b11", "out": "s11-jesus-refused-to-explain-the.jpeg", "seg": "n2",
        "window": "53.13-62.18", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN", "SPOT"],
        "narration": (
            "Jesus refused to explain the man's suffering — and instead "
            "announced what it was about to become: a place where God's work "
            "would be seen."
        ),
        "must_show": "the reframe — Jesus crouching down to the man's level at the wall, face to face with him for the first time; explanation declined, encounter begun.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the descent to eye level — the theology of the crouch.",
        "scene": (
            "Jesus has come down into a crouch before the "
            "seated man — robe hem in the street dust, "
            "forearms on his knees, his face level with "
            "the pale unseeing eyes for the first time — "
            "closer than charity ever comes, near enough "
            "that the man's quick hands could find his "
            "face — a question the whole street asked "
            "from above being answered from directly in "
            "front. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r063-b12", "out": "s12-then-he-knelt-down-made.jpeg", "seg": "n2",
        "window": "62.18-70.67", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN", "SPOT"],
        "narration": (
            "Then he knelt down, made soft clay with the dust of the ground, "
            "and gently spread it over the blind man's eyes with his own hands."
        ),
        "must_show": "SCRIPTURE-EXACT: the clay — Jesus kneeling, working street dust to soft clay in his palm, then two fingers spreading it with complete gentleness over the closed pale eyes.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the spittle implied, never depicted — dust becoming clay in a working palm; the anointing tender as a craftsman's touch.",
        "scene": (
            "Kneeling in the street dust Jesus works a "
            "little of the ground itself to soft clay in "
            "the cup of one palm — and then, with two "
            "fingers and the unhurried gentleness of a "
            "potter at fine work, spreads it across the "
            "man's closed eyes, one and then the other, "
            "his other hand steadying the bearded jaw — "
            "the man holding utterly still under the "
            "touch, hands open on his knees, being "
            "worked on by his maker in front of the "
            "morning traffic. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b13", "out": "s13-why-clay.jpeg", "seg": "n3",
        "window": "71.37-72.48", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Why clay?",
        "must_show": "the question as image — extreme close of the clay itself in a palm: wet earth, worked and ready; the strangest medicine in scripture.",
        "must_not_show": "no halo, glare or rim-light; clay as clay — dark, wet, utterly ordinary earth.",
        "scene": (
            "An extreme close still: a small worked knob "
            "of wet clay resting in the hollow of a "
            "work-lined palm — dark street earth kneaded "
            "soft, its surface carrying the print of the "
            "fingers that made it — the least promising "
            "medicine ever prescribed, photographed at "
            "the scale of the question it raises. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r063-b14", "out": "s14-bible-students-hear-an-echo.jpeg", "seg": "n3",
        "window": "72.48-79.04", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Bible students hear an echo: in the beginning, God formed man from "
            "the dust of the ground."
        ),
        "must_show": "the echo — a Genesis-toned image: ancient hands forming a human shape from riverbank clay in primal morning light; the first workshop, recalled.",
        "must_not_show": "no halo, glare or rim-light; the creation evoked through HANDS and clay only — no face on the formed figure, no divine figure shown.",
        "scene": (
            "In a primal gold morning by a riverbank, "
            "strong ancient hands work wet clay on the "
            "earth — a human form half-emerged beneath "
            "them, faceless and unfinished, shoulders "
            "and arm rising out of the riverbank's own "
            "material — the first workshop of the world "
            "recalled in one frame: dust, hands, and "
            "intention, before there was anything else. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r063-b15", "out": "s15-whatever-had-been-left-unfinished.jpeg", "seg": "n3",
        "window": "79.04-87.26", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN"],
        "narration": (
            "Whatever had been left unfinished in those eyes from birth, the "
            "maker was finishing it now, with the same material he started "
            "with."
        ),
        "must_show": "the finishing — close on the clay-anointed eyes and Jesus's steadying hand: the workshop reopened at a Jerusalem wall; maker and work, resumed.",
        "must_not_show": "no halo, glare or rim-light on Jesus; craft, not spectacle — the potter's concentration completing an old piece.",
        "scene": (
            "Close on the man's face with both eyes "
            "sealed under their smooth clay — and "
            "Jesus's hand still resting steady along "
            "the bearded jaw, his own face bent near in "
            "a craftsman's absorbed attention — the "
            "original workshop quietly reopened beside "
            "a begging bowl, the same material meeting "
            "the same hands across the whole distance "
            "from the first morning to this one. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r063-b16", "out": "s16-then-he-gave-the-man.jpeg", "seg": "n3",
        "window": "87.74-90.31", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN", "SPOT"],
        "narration": "Then he gave the man one simple instruction:",
        "must_show": "the instruction's intimacy — Jesus's mouth near the man's ear, the words passing privately; the clay-eyed man nodding once.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the instruction QUIET — given to him alone, not performed for the street.",
        "scene": (
            "Jesus leans in so his words go to the man "
            "alone — mouth near the ear, one hand on the "
            "rust-brown shoulder — and the clay-eyed "
            "man's face tips attentively toward the "
            "voice, then nods once, slowly: a private "
            "instruction passing between two men at a "
            "public wall, the whole miracle now folded "
            "inside a sentence and a pair of willing "
            "feet. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r063-b17", "out": "s17-go-wash-in-the-pool.jpeg", "seg": "j2 + n4",
        "window": "90.94-96.22", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN", "SPOT", "STREETS"],
        "narration": "Go, wash in the pool of Siloam. Understand what was asked of him.",
        "must_show": "SCRIPTURE-EXACT: the rising — the clay-eyed man getting to his feet at the wall, staff found, orienting himself toward the descending streets; the ask's size standing up with him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the man rises HIMSELF — helped by no one; the journey his own from the first step.",
        "scene": (
            "At the wall the man rises to his feet — clay "
            "sealing both eyes, one hand finding his "
            "staff, the other reading the familiar "
            "stones a last time — and turns himself "
            "toward the long descent of the streets with "
            "the deliberate orientation of a man who "
            "navigates by memory — while Jesus stands "
            "back and lets him go, the whole command "
            "already walking away on its own two feet. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r063-b18", "out": "s18-it-was-the-question-everyone.jpeg", "seg": "n0b",
        "window": "25.98-29.93", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "It was the question everyone in that world assumed had an answer.",
        "must_show": "the assumption's furniture — a scribe's table with an opened scroll and a reckoning tablet beside it: suffering entered in a ledger's columns; the worldview as stationery.",
        "must_not_show": "no halo, glare or rim-light; the ledger metaphor quiet — columns, entries, the bookkeeping of blame.",
        "scene": (
            "A close still on a scribe's table in window "
            "light: an opened scroll of the Law beside a "
            "wax reckoning tablet ruled into neat "
            "columns, a stylus laid straight between "
            "them — the era's whole instinct in one desk: "
            "somewhere, the assumption ran, suffering "
            "had columns, and every affliction was an "
            "entry with a name against it. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b19", "out": "s19-a-blind-man-eyes-packed.jpeg", "seg": "n4",
        "window": "96.22-108.11", "wide": True, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "STREETS"],
        "narration": (
            "A blind man, eyes packed with mud, feeling his way across "
            "Jerusalem, one wall and one step at a time, holding nothing but "
            "the instruction of a man whose face he had never seen."
        ),
        "must_show": "SCRIPTURE-EXACT: the walk — the clay-eyed man descending the stepped lanes alone: staff sweeping, free hand reading the wall, feet finding each worn stair; the city moving around his concentration.",
        "must_not_show": "no halo, glare or rim-light; the walk's difficulty honest — but his competence absolute; faith rendered as navigation.",
        "scene": (
            "Down the stepped stone lane the clay-eyed "
            "man makes his way alone — staff sweeping "
            "its practised arc, free hand trailing the "
            "wall's cool stone, each foot finding the "
            "hollow of the next worn stair — market "
            "noise parting around his concentration, a "
            "water-carrier stepping aside, a child "
            "staring — one man walking across Jerusalem "
            "on nothing but a stranger's sentence, one "
            "wall at a time. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b20", "out": "s20-he-went-that-walk-was.jpeg", "seg": "n4",
        "window": "108.11-111.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "STREETS"],
        "narration": "He went. That walk was the faith.",
        "must_show": "faith at foot level — close on the man's feet and staff-tip finding the next worn step; obedience measured in stairs.",
        "must_not_show": "no halo, glare or rim-light; feet, staff, stone — the whole doctrine of the row in one careful step.",
        "scene": (
            "Close at foot level on the descending "
            "stair: the man's worn sandal settling onto "
            "the next hollow-worn step while the "
            "staff-tip taps the one below it, his other "
            "foot already lifting — the small precise "
            "machinery of a blind man's progress, "
            "repeated the length of a city, each step "
            "an article of a creed no one had written "
            "down yet. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r063-b21", "out": "s21-he-knelt-at-the-pool.jpeg", "seg": "n5",
        "window": "111.74-114.96", "wide": True, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "SILOAM"],
        "narration": "He knelt at the pool of Siloam and washed the clay away.",
        "must_show": "SCRIPTURE-EXACT: the washing — the man kneeling on the lowest step, both hands bringing pool water up to his clay-sealed eyes, the water running dark with washed clay.",
        "must_not_show": "no halo, glare or rim-light; the washing plain — hands, water, dissolving clay; the instant of sight NOT yet arrived.",
        "scene": (
            "On the lowest broad step of the pool the "
            "man kneels at the clear green-tinged "
            "water, both hands cupping it up over his "
            "sealed eyes — the clay running from his "
            "cheekbones in dark rivulets, dropping and "
            "clouding away in the pool — his face bent "
            "low over his own unseen reflection, "
            "washing on instruction, one handful from "
            "the edge of everything. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b22", "out": "s22-and-light-came-pouring-in.jpeg", "seg": "n5",
        "window": "114.96-123.30", "wide": True, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "SILOAM"],
        "narration": (
            "And light came pouring in where there had never been light — "
            "color, water, sky, his own two hands."
        ),
        "must_show": "SCRIPTURE-EXACT: first sight — the man frozen on the step, water still dripping, his NEW clear brown eyes wide on his own two raised trembling hands; the world arriving as things seen.",
        "must_not_show": "no halo, glare or rim-light, NO light-effects — sight rendered as WHAT HE SEES: hands, water, sky, colour; the eyes now clear deep brown.",
        "scene": (
            "On the pool step the man has gone rigid "
            "mid-motion — water still dripping from his "
            "beard, and his eyes, clear deep brown for "
            "the first time in their existence, stretched "
            "wide on his own two hands held trembling "
            "before his face — beyond them the "
            "green-tinged water, the pale walls, the "
            "open blue sky all standing in their "
            "colours — a man meeting the visible world "
            "at thirty-five, beginning with his own "
            "fingers. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r063-b23", "out": "s23-the-first-things-he-ever.jpeg", "seg": "n5",
        "window": "123.30-127.80", "wide": True, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "STREETS"],
        "narration": "The first things he ever saw. He came back seeing.",
        "must_show": "the return — the man climbing BACK up the stepped lanes at a half-run, staff forgotten in his hand, head swinging at everything: doorways, faces, sky; drunk on the visible.",
        "must_not_show": "no halo, glare or rim-light; the staff now redundant baggage — carried, not used; the seeing walk against the earlier blind one.",
        "scene": (
            "Up the same stepped lanes the man comes "
            "back at a stumbling half-run — the staff "
            "carried crosswise and forgotten in one "
            "fist, his head swinging side to side at "
            "everything: a red cloth over a doorway, a "
            "woman's startled face, the strip of sky "
            "between the walls — taking the stairs his "
            "feet know by a route his eyes have never "
            "seen, laughing at walls. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b24", "out": "s24-the-neighbors-argued-about-whether.jpeg", "seg": "n6",
        "window": "129.85-133.22", "wide": True, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "SPOT"],
        "narration": "The neighbors argued about whether he was even the same man.",
        "must_show": "SCRIPTURE-EXACT: the dispute — the man at his old spot surrounded by arguing neighbours: pointing at his eyes, at the empty begging hollow, at each other; identity on trial in the street.",
        "must_not_show": "no halo, glare or rim-light; the comedy of it — a man having to prove he is himself, standing next to his own begging bowl.",
        "scene": (
            "At the old wall the neighbours have him "
            "surrounded and are arguing across him — one "
            "pointing at his clear eyes, another "
            "gesturing at the worn begging hollow and "
            "the abandoned bowl, two more disputing "
            "with each other over his shoulder — while "
            "the man himself stands in the middle "
            "tapping his own chest with the flat of his "
            "hand, a citizen reduced to testifying that "
            "he exists. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r063-b25", "out": "s25-the-religious-leaders-hauled-him.jpeg", "seg": "n6",
        "window": "133.22-141.56", "wide": True, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "LEADERS", "HALL"],
        "narration": (
            "The religious leaders hauled him in for questioning — twice — "
            "because the healing had happened on the sabbath, and that broke "
            "their rules."
        ),
        "must_show": "SCRIPTURE-EXACT: the examination — the man standing alone before the three seated examiners in the council room, the scribe recording; one healed beggar against a bench of authority.",
        "must_not_show": "no halo, glare or rim-light; the leaders hard and correct, not grotesque — procedure as weapon.",
        "scene": (
            "In the stone council room the man stands "
            "alone on the floor before the examiners' "
            "bench — the tall cold senior at its centre, "
            "the stocky one squinting over a tablet, "
            "the young zealous one leaning forward — "
            "high slit windows striping the floor "
            "between them, the scribe's stylus "
            "scratching — one day-old pair of eyes "
            "being processed by men whose rules the "
            "miracle inconvenienced. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b26", "out": "s26-they-pressed-him-to-call.jpeg", "seg": "n6",
        "window": "141.56-148.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "LEADERS", "HALL"],
        "narration": (
            "They pressed him to call Jesus a sinner. And he gave them one of "
            "the greatest answers anybody ever gave:"
        ),
        "must_show": "the pressing — the senior examiner leaning down at the man, finger extended for the demanded words; and the man's face gathering its answer instead.",
        "must_not_show": "no halo, glare or rim-light; pressure applied and about to fail — the gathering visible in the man's steadying jaw.",
        "scene": (
            "Close in the striped hall light: the tall "
            "senior examiner leans down from the bench "
            "with one long finger extended, the demanded "
            "denunciation hanging in the air — and below "
            "him the man's face is doing something "
            "else entirely: jaw steadying, clear new "
            "eyes coming level, a beggar's lifetime of "
            "practised deference visibly stepping aside "
            "for what he is about to say. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b27", "out": "s27-and-then-the-trouble-started.jpeg", "seg": "n6",
        "window": "128.46-129.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["SPOT"],
        "narration": "And then the trouble started.",
        "must_show": "trouble's overture — the abandoned begging spot: empty hollow, folded mat, the bowl with its few coins unclaimed; a life outgrown and about to be litigated.",
        "must_not_show": "no halo, glare or rim-light; the empty spot as hinge — the old life vacated, the new one already in dispute.",
        "scene": (
            "The begging spot stands empty in the "
            "afternoon light: the worn dust-hollow "
            "holding the shape of thirty years of "
            "sitting, the mat folded where he left it, "
            "the wooden bowl with its morning's few "
            "coins unclaimed by an owner who no longer "
            "needs them — a vacancy the whole street "
            "notices, and the authorities are already "
            "asking about. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b28", "out": "s28-whether-he-be-a-sinner.jpeg", "seg": "s25",
        "window": "148.84-155.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "HALL"],
        "narration": (
            "Whether he be a sinner or no, I know not: one thing I know, that, "
            "whereas I was blind, now I see."
        ),
        "must_show": "SCRIPTURE-EXACT: the answer — close on the man delivering it: unshakeable, plain, his hand touching his own eyelid at 'now I see'; testimony against theology, winning.",
        "must_not_show": "no halo, glare or rim-light; no defiance-theatrics — the calm of a man holding one fact nobody in the room can take.",
        "scene": (
            "Close on the man in the hall's striped "
            "light, mid-answer: his voice's plainness "
            "written in his level face, one finger "
            "risen to touch lightly beside his own "
            "clear brown eye at the words that end the "
            "argument — a man with no training and one "
            "fact, laying it down in front of experts "
            "like a stone too heavy for any of them to "
            "lift. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r063-b29", "out": "s29-he-would-not-argue-theology.jpeg", "seg": "n6b",
        "window": "156.75-165.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEADERS", "HALL"],
        "narration": (
            "He would not argue theology with trained men. He just told them "
            "the one thing that had happened to him, and there was nothing they "
            "could do with it."
        ),
        "must_show": "the fact's immovability — the three examiners' faces at a loss: the senior's cold stare, the scribe's stylus stopped, the young one's frustration; expertise defeated by testimony.",
        "must_not_show": "no halo, glare or rim-light; their defeat procedural — men reaching for a rule and finding none that covers a healed man.",
        "scene": (
            "Along the examiners' bench the answer has "
            "landed and stuck: the tall senior's cold "
            "stare gone glassy with the effort of "
            "finding a category, the stocky scribe's "
            "stylus stopped dead above the tablet, the "
            "young zealot's hands opening and closing "
            "on nothing — three trained men holding "
            "procedures, rules and precedents, and not "
            "one instrument among them that works on "
            "'now I see'. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b30", "out": "s30-tell-me-so-i-can.jpeg", "seg": "n8b",
        "window": "201.74-203.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["BLINDMAN"],
        "narration": "Tell me, so I can believe in him.",
        "must_show": "the readiness — close on the man's face asking for the name: leaning toward the answer, faith with its hands already out.",
        "must_not_show": "no halo, glare or rim-light; eagerness pure — a man asking directions to his own belief.",
        "scene": (
            "Close in the warm late light: the man's "
            "face leaning toward the voice before him, "
            "clear new eyes searching the speaker's "
            "features, brows lifted around the asking — "
            "the posture of a man holding out both "
            "hands for a name he intends, the moment he "
            "has it, to give himself to entirely. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r063-b31", "out": "s31-they-could-not-shake-him.jpeg", "seg": "n7",
        "window": "165.78-173.89", "wide": True, "jesus": False, "ref": False,
        "locks": ["BLINDMAN", "LEADERS", "HALL"],
        "narration": (
            "They could not shake him, so they threw him out — cast out of the "
            "synagogue, cut off from the whole religious life of his people."
        ),
        "must_show": "SCRIPTURE-EXACT: the casting out — the heavy hall door and the man put through it: the senior's arm extended in expulsion, the man stepping out into the street light with his back straight.",
        "must_not_show": "no halo, glare or rim-light; no manhandling — the sentence formal, the exit upright; his dignity leaves WITH him.",
        "scene": (
            "At the hall's heavy street door the "
            "sentence executes: the tall senior's arm "
            "extended full-length in formal expulsion, "
            "the young zealot holding the door wide — "
            "and the man stepping out through it into "
            "the street's bright light with his back "
            "straight and his new eyes level, expelled "
            "from the religion of his whole people "
            "eight hours into the best day of his life. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r063-b32", "out": "s32-healed-and-homeless-in-the.jpeg", "seg": "n7",
        "window": "173.89-183.42", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN", "STREETS"],
        "narration": (
            "Healed, and homeless in the same week. And here is the part to "
            "remember: when Jesus heard they had thrown him out, he went and "
            "FOUND him."
        ),
        "must_show": "SCRIPTURE-EXACT: the finding — the man alone on a street bench in late gold, and Jesus arriving down the lane TOWARD him, purpose in the stride; the seeker sought.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the DIRECTION the beat — Jesus travelling to him; the found man not yet aware.",
        "scene": (
            "In the warm late gold the man sits alone on "
            "a low stone bench at the lane's edge — cast "
            "out, healed, belonging nowhere — and down "
            "the lane toward him Jesus comes walking "
            "with unmistakable purpose, not passing "
            "through but ARRIVING, his eyes already on "
            "the seated figure — heaven's answer to an "
            "excommunication, closing the distance on "
            "foot. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r063-b33", "out": "s33-the-man-had-never-actually.jpeg", "seg": "n7",
        "window": "183.42-186.32", "wide": False, "jesus": False, "ref": False,
        "locks": ["BLINDMAN"],
        "narration": "The man had never actually seen the one who healed him.",
        "must_show": "the strange gap — close on the man's face lifting to the approaching stranger: a voice he knows arriving inside a face he has never seen.",
        "must_not_show": "no halo, glare or rim-light; recognition SUSPENDED — familiarity of voice, unfamiliarity of face, held together.",
        "scene": (
            "Close on the man's face as the stranger "
            "nears: his clear new eyes reading the "
            "approaching features with careful "
            "unfamiliarity — and then the first word of "
            "greeting landing in his ears, and something "
            "older than sight moving through his whole "
            "expression: a face he has never seen, "
            "speaking in the voice that remade him. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r063-b34", "out": "s34-jesus-asked-him-dost-thou.jpeg", "seg": "n7 + j3",
        "window": "187.07-191.23", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN"],
        "narration": "Jesus asked him: Dost thou believe on the Son of God?",
        "must_show": "SCRIPTURE-EXACT: the question — the two seated close on the bench, Jesus's face gentle and direct with the greatest question, the man's whole attention on him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the question offered, never pressed — the gentlest interrogation of the man's long day.",
        "scene": (
            "On the low bench in the deep gold the two "
            "sit close — Jesus turned toward him, "
            "forearms on knees, his face gentle and "
            "utterly direct as the question comes — and "
            "the man's clear eyes fixed on this new "
            "face with the complete attention of "
            "someone whose day has held two "
            "interrogations already and can tell, "
            "instantly, that this one is nothing like "
            "them. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r063-b35", "out": "s35-and-the-man-who-wants.jpeg", "seg": "n8",
        "window": "192.34-196.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["BLINDMAN"],
        "narration": (
            "And the man — who wants to, and does not know who that is — "
            "answers:"
        ),
        "must_show": "the wanting — the man's open face mid-answer: willingness complete, information lacking; faith waiting only on a name.",
        "must_not_show": "no halo, glare or rim-light; the gap honest — yes already decided, addressed to whom still unknown.",
        "scene": (
            "Close on the man's open face in the warm "
            "light, mid-answer: everything in it "
            "already consented — the leaning posture, "
            "the parted lips, the eyes searching the "
            "stranger's face for the missing piece — a "
            "completed yes circling the sky like a dove "
            "with nowhere yet to land, waiting on one "
            "name. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r063-b36", "out": "s36-who-is-he-lord-that.jpeg", "seg": "s36 + n8b",
        "window": "197.14-201.74", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN"],
        "narration": "Who is he, Lord, that I might believe on him? Who is he, sir?",
        "must_show": "SCRIPTURE-EXACT: the question of questions — the man's hand half-reached toward Jesus's forearm, the asking at its most naked; the answer seated within touching distance.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the dramatic irony tender — the sought one listening to himself being sought.",
        "scene": (
            "In the gold light the man's hand has "
            "half-reached toward Jesus's forearm as the "
            "question leaves him — 'who is he?' asked "
            "at touching distance of its own answer — "
            "and Jesus receives it with a stillness "
            "that is almost a smile, the sought one "
            "sitting quietly inside the seeking, one "
            "sentence away from being found. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r063-b37", "out": "s37-he-is-not-stalling-he.jpeg", "seg": "n8b",
        "window": "203.88-208.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["BLINDMAN"],
        "narration": (
            "He is not stalling. He is asking for a name so he can give himself "
            "to it."
        ),
        "must_show": "the intention — close on the man's two open hands turned up between the two figures: the self, being readied for handing over.",
        "must_not_show": "no halo, glare or rim-light; the open hands the whole grammar — surrender pre-approved, awaiting its addressee.",
        "scene": (
            "Close between the two seated figures: the "
            "man's two hands open and turned up in the "
            "space between them — work-worn beggar's "
            "hands that have held bowls and walls and "
            "staffs all their life, now emptied and "
            "offered forward — a self being readied for "
            "handing over, complete, the instant its "
            "recipient is named. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b38", "out": "s38-and-jesus-said-thou-hast.jpeg", "seg": "n8b + j4",
        "window": "209.00-214.52", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN"],
        "narration": (
            "And Jesus said: Thou hast both seen him, and it is he that talketh "
            "with thee."
        ),
        "must_show": "SCRIPTURE-EXACT: the revelation — Jesus's hand coming to rest on his own chest at 'it is he', his face open to be seen; the name arriving as presence.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the self-naming quiet — a hand on a chest, a face offered to new eyes.",
        "scene": (
            "Jesus's hand comes to rest flat on his own "
            "chest as the words arrive — 'it is he' — "
            "his face held open and still toward the "
            "man's brand-new eyes, offering itself to "
            "be seen the way other men offer their "
            "names — the whole search of the whole day "
            "ending one arm's length from where it "
            "started, in the face of the one who "
            "started it. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r063-b39", "out": "s39-you-have-seen-him-and.jpeg", "seg": "n9",
        "window": "215.57-219.25", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN"],
        "narration": "You have seen him — and he is the one talking with you right now.",
        "must_show": "the landing — the man's face as the sentence completes: recognition, wonder and the day's whole meaning arriving at once on features built for exactly this moment.",
        "must_not_show": "no halo, glare or rim-light; the arrival total — a face doing what it was healed for.",
        "scene": (
            "Close on the man's face as the sentence "
            "finishes in him: the clear new eyes going "
            "wide and then wet, the strong features "
            "moving through recognition into wonder "
            "into something with no smaller name — the "
            "first face he ever studied revealing "
            "itself as the maker of the eyes studying "
            "it — a man's whole story handed back to "
            "him in one look. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r063-b40", "out": "s40-the-first-face-this-man.jpeg", "seg": "n9",
        "window": "219.25-225.29", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN"],
        "narration": (
            "The first face this man ever truly studied was the face of the one "
            "who gave him his eyes."
        ),
        "must_show": "the study — the two faces close in profile: the man's new eyes moving slowly over Jesus's features, learning the first face of his life, line by line.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the studying slow and unashamed — a first face being memorized.",
        "scene": (
            "The two faces close in the deep gold, in "
            "profile: the man's brand-new eyes moving "
            "slowly, deliberately over Jesus's features "
            "— brow, eyes, the lines of the beard — "
            "memorizing the first face of his life with "
            "the unashamed thoroughness of a man who "
            "knows exactly what he is looking at and "
            "exactly who gave him the looking. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r063-b41", "out": "s41-and-he-said-lord-i.jpeg", "seg": "n9 + s38",
        "window": "225.63-228.54", "wide": False, "jesus": False, "ref": False,
        "locks": ["BLINDMAN"],
        "narration": "And he said: Lord, I believe.",
        "must_show": "SCRIPTURE-EXACT: the three words — close on the man's face giving them: the completed yes landing on its name at last; tears free, voice visibly steady.",
        "must_not_show": "no halo, glare or rim-light; the belief plain-spoken — three words with a whole life behind them.",
        "scene": (
            "Close on the man's face in the last warm "
            "light as the three words leave him — tears "
            "running free and his voice visibly steady "
            "beneath them, the strong jaw firm around "
            "the sentence — the morning's beggar, the "
            "afternoon's defendant, the evening's "
            "outcast, arriving at the only title he "
            "will answer to from now on: believer. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r063-b42", "out": "s42-and-he-worshipped-him-right.jpeg", "seg": "n9b",
        "window": "229.62-234.52", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN", "STREETS"],
        "narration": (
            "And he worshipped him, right there in the street the religious "
            "world had just thrown him out of."
        ),
        "must_show": "SCRIPTURE-EXACT: the worship — the man down on his knees before Jesus in the open lane, passers-by turning; the synagogue's outcast holding church in the street.",
        "must_not_show": "no halo, glare or rim-light on Jesus; public and unashamed — the street itself the sanctuary; Jesus receiving it with grave gentleness.",
        "scene": (
            "In the open lane in the day's last gold "
            "the man goes down on both knees before "
            "Jesus — head bowing over his folded hands, "
            "the staff laid aside on the stones — "
            "passers-by slowing and turning at the "
            "sight — while Jesus stands still and "
            "receives it with grave gentleness, one "
            "hand coming to rest on the bowed head: an "
            "outcast and his healer, holding church on "
            "the pavement between two walls. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r063-b43", "out": "s43-the-question-of-whose-fault.jpeg", "seg": "n9b",
        "window": "234.52-242.16", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN", "STREETS"],
        "narration": (
            "The question of whose fault it was never got an answer that day. "
            "The man got something better. He got found."
        ),
        "must_show": "the closing image — the two walking away together down the lane into the warm dusk, side by side, the man's staff left leaning against the wall behind them.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the abandoned staff the quiet coda — the old navigation no longer needed; found, and keeping company with the finder.",
        "scene": (
            "Down the lane into the warm dusk the two "
            "walk away side by side — the man's head "
            "still turning at the world's endless "
            "visible surprises, Jesus's hand briefly on "
            "his shoulder at something said between "
            "them — and behind them at the wall, "
            "leaning where it was set down and forgot, "
            "the worn staff stays behind with the "
            "begging bowl and the whole first "
            "thirty-five years: everything the found "
            "man no longer needs to feel his way "
            "through. Every figure has two arms, two "
            "hands and one head."
        ),
    },
]
