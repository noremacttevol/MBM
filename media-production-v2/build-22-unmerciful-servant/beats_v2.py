#!/usr/bin/env python3
"""V2 beat map — row 22, build-22-unmerciful-servant (Matthew 18:21-35).

COVERAGE: 38 pictures over 216.1 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 18:21-35 KJV):
  v21   "Then came PETER to him" — the frame story is Peter's own question,
        asked privately-ish among the disciples. Matthew 18 opens in Capernaum,
        in a house (Mark 9:33), so the frame is staged in a Capernaum house
        courtyard, late golden afternoon.
  v22   "I say not unto thee, Until seven times: but, Until seventy times
        seven" — the answer is a number meant to end counting.
  v23   "a certain KING, which would take account of his servants" — a royal
        audience hall, a reckoning with written accounts.
  v24   "one was brought unto him, which OWED HIM ten thousand talents" —
        BROUGHT, not walking in freely; the debt is beyond all paying.
  v25   "he had not to pay ... commanded him TO BE SOLD, and his wife, and
        children, and all that he had" — the family is present in that beat.
  v26   "the servant therefore FELL DOWN, and WORSHIPPED him, saying, Lord,
        have patience with me, and I will pay thee all."
  v27   "the lord of that servant was MOVED WITH COMPASSION, and loosed him,
        and FORGAVE HIM THE DEBT" — compassion FIRST, total cancellation,
        more than the man even asked for. ⚑ Flag J: the king forgave FIRST,
        at unasked scale — the compassion beats are the biggest, warmest
        frames in the row.
  v28   "the same servant WENT OUT, and found one of his fellowservants,
        which owed him an hundred pence: and he LAID HANDS ON HIM, and TOOK
        HIM BY THE THROAT" — outside, immediately after, a hundred pence.
  v29   "his fellowservant FELL DOWN AT HIS FEET, and besought him" — a
        deliberate visual MIRROR of v26; the compositions echo on purpose.
  v30   "he would not: and went and CAST HIM INTO PRISON."
  v31   "his fellowservants SAW what was done, and THEY WERE VERY SORRY, and
        came and TOLD unto their lord."
  v32-33 "O thou wicked servant..." — the king's own summary of the row.
  v34   "delivered him to the tormentors, till he should pay all" —
        ⚑ Flag J (CONTENT-CARE §3 row 22): shown RESTRAINED — guards leading
        him away through a dark doorway; no instruments, no violence, no
        blood, nothing graphic. The grief of it, not the mechanics.
  v35   "So likewise shall my heavenly Father do also unto you, if ye from
        your hearts forgive not every one his brother their trespasses."

TIME OF DAY: frame story is late golden afternoon in the Capernaum courtyard,
sliding toward warm dusk by the closing beats. The parable is one continuous
day: bright midday shafts in the audience hall, hard sunlight in the outer
palace courtyard for the choking, dim barred shadow for the prison, and the
same hall (afternoon light, lower and graver) for the second summons.

CHANGING CONDITION (kept OUT of the locks): the debtor's STATE changes —
dragged and desperate → forgiven and light → snarling → condemned. His
clothing never changes; only posture and face carry the arc.

CONTENT-CARE: row 22 flag J (above). The choking beats show a fist gripping
the collar and throat of a tunic — fear and force, but no injury, no blood,
no bulging agony. The selling-the-family beat is a guard's hand on a
shoulder and a huddled family, nothing worse.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream. PETER comes from the shared CAST_LOCKS in v2_prompt.py.
LOCKS = {
    "KING": (
        "KING LOCK: the king is the same man in every shot — in his sixties, "
        "tall and broad through the shoulders, with a full silver-white beard, "
        "deep-set dark eyes and a face capable of both great warmth and great "
        "severity. He wears a floor-length robe of DEEP CRIMSON wool with wide "
        "borders of dark gold embroidery over a DARK PURPLE under-tunic, a "
        "heavy gold chain across his chest and a gold signet ring (never cream, "
        "never white). His face is shown clearly."
    ),
    "DEBTOR": (
        "DEBTOR LOCK: the forgiven servant is the same man in every shot — "
        "about forty, wiry and hollow-cheeked, with a thin black beard, cropped "
        "dark hair and quick anxious dark eyes. He wears a DARK OLIVE-GREY wool "
        "tunic under a frayed RUST-BROWN mantle, a worn leather belt and dusty "
        "sandals (never cream, never white). His clothing never changes across "
        "the story. His face is shown clearly."
    ),
    "FELLOW": (
        "FELLOW-SERVANT LOCK: the fellow servant is the same man in every shot "
        "— mid-twenties, slight and mild-faced, with a short dark beard and "
        "gentle dark eyes. He wears a patched DUSTY INDIGO wool tunic with a "
        "plain rope belt and worn sandals (never cream, never white). His face "
        "is shown clearly."
    ),
    "HALL": (
        "AUDIENCE HALL LOCK: a great stone audience hall — pale honey-stone "
        "columns down both sides, high clerestory windows throwing long slanted "
        "shafts of daylight across a polished stone floor, a raised stone dais "
        "with a heavy carved wooden seat, patterned dark rugs on the steps, "
        "bronze lampstands, and low scribes' tables to one side stacked with "
        "rolled account scrolls, ink pots and a bronze balance scale."
    ),
    "PALACE-YARD": (
        "PALACE COURTYARD LOCK: the sunlit outer courtyard of the palace — wide "
        "worn flagstones, a shaded colonnade along one side, a great arched "
        "gate to the street, clay jars and bundled sacks by the walls, and hard "
        "bright daylight with sharp column shadows across the stones."
    ),
    "PRISON": (
        "PRISON LOCK: a low stone gatehouse cell at the courtyard's far corner "
        "— a heavy door of dark iron-strapped timber with a small barred "
        "opening, rough shadowed stone, and one narrow slot of daylight. No "
        "instruments of any kind are visible, only stone, timber and iron bars."
    ),
    "COURTYARD": (
        "CAPERNAUM COURTYARD LOCK: the small courtyard of a Capernaum house — "
        "honey-coloured stone walls, a low doorway into the dark cool of the "
        "house, a spreading fig tree throwing dappled shade, low stone benches "
        "and a rolled fishing net over one wall, in warm late-afternoon golden "
        "light."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the listening disciples are weathered working "
        "Galilean men of various ages with dark hair and full dark beards, "
        "dressed in SATURATED DEEP earth colours — dark chocolate brown, deep "
        "russet, dark olive, burnt ochre and dusty indigo wool (never cream, "
        "never white; only Jesus wears cream). Their faces are shown clearly."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------- n0/s21 — Peter's question ----
    {
        "id": "v2-r022-b01", "out": "s01-one-day-peter-came-to.jpeg", "seg": "n0",
        "window": "0.28-4.82", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "COURTYARD"],
        "narration": (
            "One day Peter came to Jesus with a question that had been sitting "
            "heavy on his heart."
        ),
        "must_show": "Peter crossing the courtyard TOWARD Jesus, who sits on a low stone bench in the fig-tree shade — Peter mid-stride, purposeful, something clearly on his mind.",
        "must_not_show": "no halo, glare or rim-light on Jesus; Peter is not angry — burdened, not hostile.",
        "scene": (
            "In the warm golden late afternoon of the small courtyard, Jesus sits "
            "on a low stone bench in the dappled shade of the fig tree, two other "
            "disciples seated on the ground near him in quiet conversation. Peter "
            "is crossing the flagstones toward him, caught mid-stride, his brow "
            "drawn and his mouth set — a man carrying a question he has turned "
            "over too many times. Jesus is already looking up at him. The camera "
            "stands back far enough to hold the whole courtyard. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b02", "out": "s02-it-was-about-forgiveness-and.jpeg", "seg": "n0",
        "window": "4.82-9.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "It was about forgiveness — and about someone who kept hurting him.",
        "must_show": "a close portrait of Peter's weathered face — hurt and frustration held under control, eyes down and away, jaw tight.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no rage or theatrics — this is old, worn hurt, not fresh fury.",
        "scene": (
            "A close head-and-shoulders portrait of Peter in warm late-afternoon "
            "light, his eyes lowered and fixed on nothing, his jaw tight beneath "
            "the dark beard, the fine creases around his eyes deepened. It is the "
            "face of a man who has forgiven the same person before and is tired. "
            "Soft golden courtyard stone out of focus behind him. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b03", "out": "s03-lord-how-oft-shall-my.jpeg", "seg": "s21",
        "window": "10.03-13.45", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "COURTYARD"],
        "narration": "Lord, how oft shall my brother sin against me, and I forgive him?",
        "must_show": "SCRIPTURE-EXACT: Peter standing before the seated Jesus, asking — hands open in question, leaning slightly in; Jesus's full attention on him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; Peter does not kneel — he stands and asks, man to master.",
        "scene": (
            "Peter stands before Jesus in the golden courtyard, bent slightly "
            "toward him with both hands open at his waist, palms up, in the "
            "middle of his question. Jesus sits on the low stone bench looking "
            "up into Peter's face with complete, unhurried attention, his hands "
            "at rest in his lap. The fig-tree shade dapples the stones between "
            "them. The camera holds both men in profile, close enough to read "
            "both faces. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b04", "out": "s04-peter-must-have-thought-he.jpeg", "seg": "n1",
        "window": "16.59-19.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "Peter must have thought he was being generous.",
        "must_show": "a close shot of Peter's face with the faint self-satisfaction of a man who believes his offer is a big one — chin slightly lifted, a small expectant almost-smile.",
        "must_not_show": "no halo, glare or rim-light on Jesus; not smug or unlikeable — earnest, expecting approval.",
        "scene": (
            "A close portrait of Peter in the warm afternoon light, his chin "
            "lifted a little and one eyebrow slightly raised, the smallest "
            "expectant almost-smile inside his beard — the look of an earnest "
            "man who has just offered what he believes is a generous number and "
            "is waiting to be told so. Soft courtyard colour behind him. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b05", "out": "s05-in-other-words-stop-counting.jpeg", "seg": "n2",
        "window": "26.89-28.45", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "In other words, stop counting.",
        "must_show": "a close, calm portrait of Jesus — steady warm eyes on Peter, the gentle gravity of a teacher resetting the whole question.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no sternness — kindness with weight.",
        "scene": (
            "A close head-and-shoulders portrait of Jesus in the warm dappled "
            "light beneath the fig tree, his warm brown eyes level and steady on "
            "someone just past the camera, his expression gentle and utterly "
            "unhurried — the calm of a teacher about to move the whole question "
            "somewhere larger. Soft golden stone and green leaf shadow behind "
            "him. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b06", "out": "s06-real-forgiveness-keep-a-ledger.jpeg", "seg": "n2",
        "window": "28.45-35.11", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "COURTYARD"],
        "narration": (
            "Real forgiveness doesn't keep a ledger. And then, to show them "
            "what he meant, Jesus told a story."
        ),
        "must_show": "the disciples settling in around the seated Jesus as he begins the story — Peter now seated too, the whole group leaning in.",
        "must_not_show": "no halo, glare or rim-light on Jesus; he must not be set apart on a height — same level, close circle.",
        "scene": (
            "In the golden courtyard the disciples have gathered close around "
            "Jesus — Peter now seated on the flagstones near his feet, four "
            "others on benches and on the ground, all leaning in. Jesus sits "
            "forward on the low bench, one hand lifted mid-gesture, in the first "
            "words of a story. The late light is turning deeper gold on the "
            "honey stone. The camera stands back to hold the whole circle. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    # --------------------------------------------- n3-n5 — the great reckoning ----
    {
        "id": "v2-r022-b07", "out": "s07-there-was-once-a-king.jpeg", "seg": "n3",
        "window": "35.66-38.44", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "HALL"],
        "narration": "There was once a king who decided to settle his accounts.",
        "must_show": "the king seated on the carved seat of the dais in the great hall, scribes at their scroll-stacked tables — a reckoning being prepared.",
        "must_not_show": "no halo, glare or rim-light; the king is not cruel-faced — grave, sovereign, composed.",
        "scene": (
            "The great audience hall in bright midday, long shafts of daylight "
            "slanting from the high windows across the polished floor. The king "
            "sits upright on the heavy carved seat of the dais, both hands on "
            "its arms, grave and composed, while at the low tables to one side "
            "two scribes unroll account scrolls and set out the bronze balance "
            "scale. The camera stands at the far end of the hall, holding the "
            "dais and the columns in one frame. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r022-b08", "out": "s08-one-by-one-his-servants.jpeg", "seg": "n3",
        "window": "38.44-43.28", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "HALL"],
        "narration": (
            "One by one, his servants were brought in to answer for what they "
            "owed him."
        ),
        "must_show": "a line of servants waiting down the length of the hall while one stands before the dais answering, a scribe reading from a scroll.",
        "must_not_show": "no halo, glare or rim-light; the waiting men are anxious but orderly — no chains on these ordinary debtors.",
        "scene": (
            "Down the length of the sunlit hall a line of half a dozen servants "
            "in dark work-worn tunics waits between the columns, heads down, "
            "hands clasped, while at the front one man stands alone before the "
            "dais. A scribe beside the steps reads aloud from an unrolled "
            "scroll, and the king listens from the carved seat, chin on his "
            "fist. The camera looks down the line toward the dais. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b09", "out": "s09-one-man-was-dragged-forward.jpeg", "seg": "n4",
        "window": "43.85-53.95", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "DEBTOR", "HALL"],
        "narration": (
            "One man was dragged forward who owed the king ten thousand "
            "talents. It was a staggering fortune — more money than a working "
            "man could earn in ten thousand lifetimes."
        ),
        "must_show": "SCRIPTURE-EXACT: the debtor BROUGHT — two guards gripping his arms, hauling him stumbling before the dais; he does not walk in freely.",
        "must_not_show": "no halo, glare or rim-light; force but no violence — gripped arms, not blows; no blood.",
        "scene": (
            "Two broad palace guards in dark leather over deep-red tunics haul "
            "the debtor up the centre of the hall, one gripping each of his "
            "arms, his sandalled feet stumbling and dragging on the polished "
            "stone, his rust-brown mantle slipping from one shoulder. On the "
            "dais ahead the king rises half out of the carved seat to look at "
            "him. Long midday shafts cut across their path. The camera moves "
            "with them, low and close to the stumbling man but upright and "
            "level — the floor at the bottom of the frame, the hall rising to "
            "the top, the horizon level and the picture the right way up. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b10", "out": "s10-a-debt-like-that-could.jpeg", "seg": "n4",
        "window": "53.95-57.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": "A debt like that could never, ever be repaid.",
        "must_show": "a close shot of the account scroll unrolled to an impossible length — a scribe's finger at the total, entries beyond counting.",
        "must_not_show": "no halo, glare or rim-light; no legible modern numerals or modern writing — dense ancient script marks only.",
        "scene": (
            "A close shot over a scribe's shoulder: an account scroll unrolled "
            "so far it spills off the low table and curls onto the stone floor, "
            "crowded from edge to edge with dense columns of small dark "
            "handwritten entries. The scribe's ink-stained finger rests at the "
            "final line. Beside the scroll one pan of the bronze balance scale "
            "sits weighted down flat with tally-stones. Slanted daylight rakes "
            "the parchment. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b11", "out": "s11-the-man-had-nothing-to.jpeg", "seg": "n5",
        "window": "58.14-59.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEBTOR"],
        "narration": "The man had nothing to pay with.",
        "must_show": "a close shot of the debtor's two empty hands held open before him, palms up, work-scarred and utterly empty; his stricken face above them.",
        "must_not_show": "no halo, glare or rim-light; the hands hold NOTHING — no coins, no pouch.",
        "scene": (
            "A close shot of the debtor's two open hands held out before his "
            "chest, palms up, work-scarred, calloused and completely empty — "
            "and above them, softly out of focus, his hollow-cheeked face gone "
            "grey with fear. A shaft of hall daylight falls across the empty "
            "palms. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b12", "out": "s12-so-the-king-ordered-that.jpeg", "seg": "n5",
        "window": "59.66-67.84", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "DEBTOR", "HALL"],
        "narration": (
            "So the king ordered that he be sold — his wife, his children, "
            "everything he owned — to recover even a fraction of it."
        ),
        "must_show": "SCRIPTURE-EXACT: the sentence pronounced — the king's arm extended in command; near the columns the debtor's wife and two children huddled together, a guard's hand on the wife's shoulder.",
        "must_not_show": "no halo, glare or rim-light; RESTRAINED — no weeping chaos, no rough handling of the children, no chains; one guard's hand on a shoulder is the whole force shown.",
        "scene": (
            "The king stands before the carved seat with one arm extended in "
            "formal command toward the debtor, who has gone rigid in the grip "
            "of the two guards. By the columns at the hall's edge a woman in a "
            "dark madder-red mantle draws two small children in against her "
            "skirts, a single guard's hand resting on her shoulder, her face "
            "turned toward her husband across the wide sunlit floor. The "
            "camera stands to the side, holding the sentence and the family in "
            "one frame with the long shafts of daylight between them. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    # --------------------------------------------- n6-n8 — mercy at full scale ----
    {
        "id": "v2-r022-b13", "out": "s13-the-servant-threw-himself-down.jpeg", "seg": "n6",
        "window": "68.31-75.74", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "DEBTOR", "HALL"],
        "narration": (
            "The servant threw himself down on the ground and begged. Please, "
            "he cried, be patient with me, and I will pay back everything!"
        ),
        "must_show": "SCRIPTURE-EXACT: the debtor flat down on the stone at the foot of the dais steps, arms outstretched toward the king above him — full prostration, not kneeling.",
        "must_not_show": "no halo, glare or rim-light; the guards have released him — he throws HIMSELF down.",
        "scene": (
            "The debtor lies thrown flat on the polished stone at the foot of "
            "the dais steps, his whole body stretched out, both arms flung "
            "forward up the steps toward the king, his face lifted just off the "
            "floor, mouth open mid-cry. The two guards have stepped back a "
            "pace. Above him the king stands very still before the carved "
            "seat, looking down. A single shaft of midday light falls across "
            "the prostrate man. The camera is level and upright, the floor at "
            "the bottom of the frame and the dais rising to the top. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b14", "out": "s14-lord-have-patience-with-me.jpeg", "seg": "j3",
        "window": "76.30-79.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEBTOR"],
        "narration": "Lord, have patience with me, and I will pay thee all.",
        "must_show": "SCRIPTURE-EXACT: a close shot of the debtor's upturned pleading face, hands clasped and raised, tears standing in his eyes.",
        "must_not_show": "no halo, glare or rim-light; desperate but dignified — a man begging for his family's life.",
        "scene": (
            "A close shot from just above: the debtor's upturned face, tears "
            "standing in his dark eyes, brows knotted, lips parted in the "
            "middle of his plea, both hands clasped together and raised before "
            "his chin. The hall's daylight falls on his face; the blurred edge "
            "of the dais steps rises behind him. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b15", "out": "s15-and-the-king-looked-at.jpeg", "seg": "n7",
        "window": "80.67-86.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": (
            "And the king looked at this desperate man crumpled before him — "
            "and his heart broke with compassion."
        ),
        "must_show": "a close portrait of the king's face as severity breaks into compassion — eyes suddenly soft and wet, the hard line of his mouth undone.",
        "must_not_show": "no halo, glare or rim-light; not pity from a height — genuine grief for the man; this is the warmest face in the row.",
        "scene": (
            "A close portrait of the king looking down past the camera, the "
            "moment severity gives way: his deep-set eyes gone soft and "
            "glistening, silver brows drawn together in grief rather than "
            "anger, the hard line of his mouth undone behind the white beard. "
            "The gold chain catches the hall light at his chest. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b16", "out": "s16-he-did-something-no-one.jpeg", "seg": "n7 + n8",
        "window": "86.26-91.16", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "DEBTOR", "HALL"],
        "narration": (
            "He did something no one expected. He didn't just give him more "
            "time."
        ),
        "must_show": "the king COMING DOWN the dais steps toward the prostrate man — descending to him, robe gathering on the steps, guards astonished.",
        "must_not_show": "no halo, glare or rim-light; the king does not summon the man up — HE comes down; that is the whole beat.",
        "scene": (
            "The king is descending the dais steps toward the man still "
            "prostrate on the stone below, his crimson robe gathering behind "
            "him on the steps, one hand already reaching down. The two guards "
            "have turned to each other, mouths open. The scribes have stopped, "
            "quills lifted. Midday shafts cross the space between the "
            "descending king and the man on the floor. The camera holds the "
            "whole descent from the side. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r022-b17", "out": "s17-he-cancelled-the-whole-debt.jpeg", "seg": "n8",
        "window": "91.16-98.96", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "DEBTOR", "HALL"],
        "narration": (
            "He cancelled the whole debt. Every last coin of that impossible "
            "fortune — forgiven, wiped away, gone."
        ),
        "must_show": "SCRIPTURE-EXACT: the cancellation made visible — the king with the great account scroll TORN THROUGH in his two hands, the debtor risen to his knees staring in disbelief.",
        "must_not_show": "no halo, glare or rim-light; the debtor's face is disbelief and dawning joy, not composure.",
        "scene": (
            "At the foot of the dais the king stands over the kneeling debtor "
            "holding the long account scroll torn clean through, one ragged "
            "half in each hand, the dense-written parchment hanging in ribbons. "
            "The debtor has risen onto his knees, sitting back on his heels, "
            "staring up at the torn halves with his mouth open and both hands "
            "loose at his sides — disbelief just turning to joy. A scribe "
            "behind them presses both hands to his head. Bright shafts of "
            "midday light fall over the torn parchment. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b18", "out": "s18-the-man-was-free.jpeg", "seg": "n8",
        "window": "98.96-100.84", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEBTOR", "HALL"],
        "narration": "The man was free.",
        "must_show": "the debtor alone, standing, unburdened — shoulders dropped, face lifted into the light, a man given his life back.",
        "must_not_show": "no halo, glare or rim-light; joy and lightness, not triumph.",
        "scene": (
            "The debtor stands alone in one of the long shafts of daylight in "
            "the hall, his face lifted into the light with his eyes closed, "
            "shoulders fallen loose, both hands open at his sides — a man "
            "feeling the whole weight go. The columns and the bright doorway "
            "to the courtyard stand soft behind him. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    # ------------------------------------- n9-n13 — the hundred pence, the mirror ----
    {
        "id": "v2-r022-b19", "out": "s19-but-then-that-same-servant.jpeg", "seg": "n9",
        "window": "101.44-109.72", "wide": True, "jesus": False, "ref": False,
        "locks": ["DEBTOR", "FELLOW", "PALACE-YARD"],
        "narration": (
            "But then that same servant walked outside. And there he found one "
            "of his fellow servants — a man who owed him a hundred silver "
            "coins."
        ),
        "must_show": "SCRIPTURE-EXACT: the forgiven man just OUTSIDE in the hard sunlight, catching sight of the fellow servant across the courtyard — the moment of spotting him, face already changing.",
        "must_not_show": "no halo, glare or rim-light; the change must read at a glance — relief curdling into calculation.",
        "scene": (
            "In the hard bright sunlight of the outer palace courtyard the "
            "forgiven debtor has stopped mid-stride on the flagstones, his head "
            "turned sharply toward the colonnade where the young fellow servant "
            "in the patched indigo tunic is crossing with a clay jar on his "
            "shoulder, unaware. The debtor's eyes have narrowed and his relief "
            "has curdled into something colder. Sharp column shadows cut the "
            "stones between them. The camera holds both men and the distance "
            "between them. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b20", "out": "s20-a-few-months-wages.jpeg", "seg": "n9",
        "window": "109.72-111.42", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "A few months' wages.",
        "must_show": "a close still shot of a small worn leather pouch with a modest scatter of ancient silver coins — small, countable, ordinary.",
        "must_not_show": "no halo, glare or rim-light; the pile must look SMALL — a handful, nothing like a fortune; no modern coins.",
        "scene": (
            "A close still shot on sun-warmed flagstone: a small worn leather "
            "pouch tipped on its side with a modest scatter of rough-struck "
            "ancient silver coins spilled beside it — a countable little "
            "handful, no more. Hard courtyard daylight throws each small coin's "
            "shadow across the stone. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r022-b21", "out": "s21-real-money-yes-but-nothing.jpeg", "seg": "n9 + n10",
        "window": "111.42-119.58", "wide": True, "jesus": False, "ref": False,
        "locks": ["DEBTOR", "FELLOW", "PALACE-YARD"],
        "narration": (
            "Real money, yes — but nothing next to the ocean he'd just been "
            "forgiven. He grabbed the man by the throat and started to choke "
            "him."
        ),
        "must_show": "SCRIPTURE-EXACT: the seizing — the debtor's fist twisted into the collar of the fellow servant's tunic at the throat, the clay jar shattered on the stones, the smaller man bent backward.",
        "must_not_show": "no halo, glare or rim-light; force without gore — a fist in the gathered collar, the young man's hands gripping that wrist; no blood, no injury.",
        "scene": (
            "In the hard sunlight the debtor has seized the young fellow "
            "servant, his right fist twisted deep into the gathered collar of "
            "the indigo tunic at the throat, driving him bent backward over "
            "the flagstones; the clay jar lies shattered around their feet in "
            "a dark splash of water. The young man's both hands clamp the "
            "gripping wrist, his face shocked. The camera stands close and "
            "level with the struggle. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r022-b22", "out": "s22-pay-me-what-you-owe.jpeg", "seg": "n10",
        "window": "119.58-122.03", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEBTOR"],
        "narration": "Pay me what you owe me! he snarled.",
        "must_show": "a tight close-up of the debtor's snarling face — teeth bared, the same face that wept on the floor now twisted with fury.",
        "must_not_show": "no halo, glare or rim-light; recognisably the SAME man as the pleading close-up — the mirror is the point.",
        "scene": (
            "A tight close-up of the debtor's face in the hard courtyard light, "
            "teeth bared inside the thin black beard, brows crushed down, "
            "spittle at the corner of his shouting mouth — the same "
            "hollow-cheeked face that was upturned and weeping an hour before, "
            "now twisted with fury. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r022-b23", "out": "s23-pay-me-that-thou-owest.jpeg", "seg": "j4",
        "window": "124.10-125.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEBTOR", "FELLOW"],
        "narration": "Pay me that thou owest.",
        "must_show": "SCRIPTURE-EXACT: the two faces inches apart — the debtor's fist still in the collar, the young man pinned back against a column, fear against fury in profile.",
        "must_not_show": "no halo, glare or rim-light; no blows struck, no blood — the grip and the faces carry it all.",
        "scene": (
            "A close two-shot in profile: the young fellow servant pinned back "
            "against a courtyard column, and the debtor's furious face pushed "
            "to within inches of his, fist still knotted in the indigo collar "
            "at his throat. The young man's eyes are wide, his chin turned "
            "away. Hard sunlight rakes across both faces. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b24", "out": "s24-his-fellow-servant-fell-down.jpeg", "seg": "n11",
        "window": "127.36-137.30", "wide": True, "jesus": False, "ref": False,
        "locks": ["DEBTOR", "FELLOW", "PALACE-YARD"],
        "narration": (
            "His fellow servant fell down at his feet and begged him with the "
            "very same words he himself had used only moments before: Please, "
            "be patient with me, and I will pay you back!"
        ),
        "must_show": "SCRIPTURE-EXACT: the deliberate MIRROR of the throne-room plea — the young man thrown down flat at the debtor's feet on the flagstones, arms stretched toward him, exactly the posture the debtor himself held.",
        "must_not_show": "no halo, glare or rim-light; the composition must visibly echo the earlier prostration beat — same pose, meaner setting.",
        "scene": (
            "On the sunlit flagstones the young fellow servant lies thrown "
            "flat at the debtor's feet, his whole body stretched out, both "
            "arms flung forward toward the man's dusty sandals, face lifted "
            "just off the stone, pleading — precisely the posture of the "
            "throne-room floor, replayed in a courtyard. The debtor stands "
            "over him, arms folded, looking down. Sharp column shadows bar the "
            "stones. The camera is level and upright, the flagstones at the "
            "bottom of the frame and the colonnade rising to the top. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b25", "out": "s25-but-he-refused-he-would.jpeg", "seg": "n12",
        "window": "137.82-139.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEBTOR"],
        "narration": "But he refused. He would not listen.",
        "must_show": "the debtor with his face deliberately TURNED AWAY from the unseen pleading below, arms crossed hard, jaw set — refusal made visible.",
        "must_not_show": "no halo, glare or rim-light; cold refusal, not rage — the fury has settled into something worse.",
        "scene": (
            "A close three-quarter shot of the debtor standing in the hard "
            "light, arms crossed hard over the rust-brown mantle, his face "
            "deliberately turned away and his eyes fixed on the far wall — "
            "cold, shut, finished listening — while at the very bottom edge of "
            "the frame two pleading hands reach up toward him out of focus. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b26", "out": "s26-he-had-the-man-thrown.jpeg", "seg": "n12 + n13",
        "window": "139.95-148.76", "wide": True, "jesus": False, "ref": False,
        "locks": ["DEBTOR", "FELLOW", "PRISON", "PALACE-YARD"],
        "narration": (
            "He had the man thrown into prison until he could pay back every "
            "penny. The other servants saw the whole thing, and it grieved them "
            "deeply."
        ),
        "must_show": "SCRIPTURE-EXACT: the young man pushed in at the dark gatehouse cell door by a warder while the debtor points the order — and to the side a knot of other servants watching, stricken.",
        "must_not_show": "no halo, glare or rim-light; RESTRAINED — a hand on the shoulder pushing him through the doorway, no beating, no chains, no blood.",
        "scene": (
            "At the shadowed corner of the courtyard a thick-set warder pushes "
            "the young fellow servant through the heavy iron-strapped cell "
            "door, one hand flat between his shoulders, the young man's head "
            "bowed as the darkness takes him. The debtor stands a few paces "
            "off with his arm still extended in the order. To the side, three "
            "other servants in dark work tunics have stopped their carrying "
            "and stand close together, faces fallen, one woman's hand pressed "
            "over her mouth. Hard light outside, deep shadow in the doorway. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b27", "out": "s27-they-went-and-told-the.jpeg", "seg": "n13 + n14",
        "window": "148.76-153.89", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "HALL"],
        "narration": (
            "They went and told the king everything that had happened. The king "
            "summoned him back."
        ),
        "must_show": "SCRIPTURE-EXACT: the grieved servants before the dais, mid-report — one gesturing back toward the courtyard — and the king rising from the seat, his face darkening.",
        "must_not_show": "no halo, glare or rim-light; the servants report in grief, not gossip — earnest, distressed faces.",
        "scene": (
            "In the hall, now lit by lower afternoon shafts, three servants in "
            "dark work tunics stand close together before the dais, one man "
            "mid-sentence with his arm flung back toward the courtyard door, "
            "the woman beside him with her hands knotted at her chest. The "
            "king has risen from the carved seat and stands at the top of the "
            "steps, gripping the seat's arm, his face darkening as he "
            "listens. The camera holds the reporting group and the rising king "
            "in one frame. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b28", "out": "s28-he-said-you-have-shown.jpeg", "seg": "n14",
        "window": "153.89-159.34", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "DEBTOR", "HALL"],
        "narration": (
            "he said. Shouldn't you have shown the same mercy to your fellow "
            "servant that I showed to you?"
        ),
        "must_show": "the debtor back before the dais — alone, shrunken — and the king pointing down at him in grieved accusation.",
        "must_not_show": "no halo, glare or rim-light; the king's anger carries GRIEF in it — betrayed mercy, not mere rage.",
        "scene": (
            "The debtor stands alone and shrunken at the foot of the dais, "
            "shoulders curled, eyes on the floor, while above him the king "
            "stands at the top of the steps pointing down at him, silver brows "
            "drawn in an anger that is half grief. The scribes at their tables "
            "keep their heads bowed. The low afternoon shafts fall long and "
            "amber across the stone between them. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b29", "out": "s29-pay-me-now.jpeg", "seg": "n10",
        "window": "122.03-123.52", "wide": True, "jesus": False, "ref": False,
        "locks": ["DEBTOR", "FELLOW", "PALACE-YARD"],
        "narration": "Pay me now!",
        "must_show": "the burst continues — the debtor SHAKING the young man by the gripped collar, the smaller man's feet staggering, heels dragging on the stones.",
        "must_not_show": "no halo, glare or rim-light; violent motion but no injury — no blows, no blood.",
        "scene": (
            "Mid-shake: the debtor hauls the gripped collar so hard that the "
            "young fellow servant staggers sideways across the flagstones, "
            "heels scraping, one arm flailing out for balance, the indigo "
            "tunic wrenched tight at his throat. The debtor's shoulders are "
            "thrown into the pull, mouth open in a shout. Shards of the broken "
            "jar scatter the wet stones at their feet. The camera is close, "
            "level and upright. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r022-b30", "out": "s30-o-thou-wicked-servant-i.jpeg", "seg": "j5",
        "window": "159.95-172.53", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "DEBTOR", "HALL"],
        "narration": (
            "O thou wicked servant, I forgave thee all that debt, because thou "
            "desiredst me: Shouldest not thou also have had compassion on thy "
            "fellowservant, even as I had pity on thee?"
        ),
        "must_show": "SCRIPTURE-EXACT: the king's full judgment — he has come DOWN the steps to stand over the debtor, holding up the two torn halves of the cancelled scroll between them as the evidence of what was given.",
        "must_not_show": "no halo, glare or rim-light; the torn scroll halves must match the earlier cancellation beat — same ragged tear.",
        "scene": (
            "The king has come down the dais steps and stands over the "
            "cowering debtor, holding up before his face the two ragged torn "
            "halves of the great account scroll — the same tear, the ribboned "
            "parchment — his eyes blazing and wet at once above the white "
            "beard. The debtor has half-turned his face away, hands raised "
            "uselessly. Behind them the carved seat stands empty in the amber "
            "afternoon shafts. The camera is close and level on the two men "
            "and the torn parchment between them. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b31", "out": "s31-till-seven-times.jpeg", "seg": "s21",
        "window": "13.45-15.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "till seven times?",
        "must_show": "a close shot of Peter finishing the question — both hands lifted open before his chest, palms up, offering his number, eyebrows raised expectantly.",
        "must_not_show": "no halo, glare or rim-light on Jesus; do NOT show counted fingers or a specific number of raised fingers — open offering hands only.",
        "scene": (
            "A close shot of Peter in the golden courtyard light, both hands "
            "lifted open before his chest, palms up as though offering "
            "something weighed and settled, his eyebrows raised and his head "
            "tipped slightly — a man naming a figure he believes is generous "
            "and waiting for the verdict. Warm dappled fig-tree shade behind "
            "him. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b32", "out": "s32-and-in-his-anger-the.jpeg", "seg": "n15",
        "window": "174.05-182.22", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "DEBTOR", "HALL"],
        "narration": (
            "And in his anger the king handed him over to be punished until he "
            "should pay back all that he owed. Then Jesus turned the story "
            "toward every one of us."
        ),
        "must_show": "⚑ Flag J, RESTRAINED: the two guards leading the debtor away toward a dark doorway at the hall's edge — his head bowed, the king turned away toward the carved seat, grief in the set of his shoulders.",
        "must_not_show": "no halo, glare or rim-light; NOTHING graphic — no instruments, no chains, no violence, no visible cell; a man led away through a dark door, nothing more.",
        "scene": (
            "The two guards walk the debtor away across the long amber-lit "
            "floor toward a dark narrow doorway at the far edge of the hall, "
            "one at each arm, his head hanging and his feet heavy. In the "
            "foreground the king has turned his back on the departure, one "
            "hand braced on the arm of the carved seat, his silver head bowed "
            "— anger and grief together in the set of his shoulders. The low "
            "shafts stretch the three walking shadows long across the stone. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b33", "out": "s33-so-likewise-shall-my-heavenly.jpeg", "seg": "j2",
        "window": "182.81-191.78", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "COURTYARD"],
        "narration": (
            "So likewise shall my heavenly Father do also unto you, if ye from "
            "your hearts forgive not every one his brother their trespasses."
        ),
        "must_show": "SCRIPTURE-EXACT: back in the courtyard — Jesus delivering the story's point to the circle, grave and tender at once; the disciples utterly still, Peter's eyes locked on him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no wagging finger — gravity carried in stillness and the faces.",
        "scene": (
            "The courtyard light has deepened toward dusk-gold. Jesus sits "
            "forward on the low bench, elbows on knees, hands loosely joined, "
            "his face grave and very gentle as he finishes the story's point. "
            "The circle of disciples is utterly still around him — no one "
            "moves — and Peter, seated on the flagstones, watches him without "
            "blinking. The fig leaves hang motionless overhead. The camera "
            "holds the quiet circle from just outside it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b34", "out": "s34-i-say-not-unto-thee.jpeg", "seg": "j1",
        "window": "19.62-25.38", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "COURTYARD"],
        "narration": (
            "I say not unto thee, Until seven times: but, Until seventy times "
            "seven."
        ),
        "must_show": "SCRIPTURE-EXACT: Jesus answering Peter — a slight warmth at the corner of his mouth, one hand lifted in easy emphasis; Peter's expectant face beginning to fall into astonishment.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no counted fingers anywhere in the frame.",
        "scene": (
            "In the golden courtyard Jesus looks up at the standing Peter with "
            "the faintest warmth at the corner of his mouth, one hand lifted "
            "palm-open in easy emphasis as he answers. Peter's expectant "
            "expression is just beginning to fall open into astonishment, his "
            "offering hands sinking. The two are close, in profile, the "
            "fig-tree shade dappling the stones around the bench. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------ n16/n17 — the two debts ----
    {
        "id": "v2-r022-b35", "out": "s35-here-is-the-whole-point.jpeg", "seg": "n16",
        "window": "193.47-197.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": (
            "Here is the whole point of the story. Look at the two debts side "
            "by side."
        ),
        "must_show": "a close still-life: the two torn halves of the immense account scroll laid on the scribes' table, and beside them the one small pouch with its little scatter of silver — the two debts literally side by side.",
        "must_not_show": "no halo, glare or rim-light; the scale contrast must be unmistakable — a vast written fortune against a child-sized handful.",
        "scene": (
            "A close still-life on the scribes' low table in a slant of amber "
            "light: the two ragged torn halves of the immense account scroll "
            "laid out flat, dense dark entries running off both torn edges — "
            "and set beside them, small enough to sit in one palm, the worn "
            "leather pouch with its modest scatter of rough silver coins. "
            "Nothing else on the table. The contrast in scale tells the whole "
            "story at a glance. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r022-b36", "out": "s36-the-mountain-that-was-forgiven.jpeg", "seg": "n16",
        "window": "197.76-204.25", "wide": True, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": (
            "The mountain that was forgiven us, and the small handful we're "
            "asked to forgive each other. They aren't even close."
        ),
        "must_show": "the same contrast at full width — the torn scroll's halves unrolled RIGHT ACROSS the floor of the hall, yards of dense entries, and the tiny pouch of coins sitting alone at its edge.",
        "must_not_show": "no halo, glare or rim-light; no figures needed — let the two objects and the empty hall carry it.",
        "scene": (
            "The empty audience hall in low amber light: the torn account "
            "scroll unrolled in two great ragged lengths right across the "
            "polished floor between the columns, yard after yard of dense dark "
            "entries running away toward the dais — and beside the near edge, "
            "tiny against the stone, the single worn pouch with its little "
            "spill of silver coins. The carved seat stands empty in the "
            "distance. The camera looks down the length of the unrolled "
            "fortune. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b37", "out": "s37-we-forgive-the-small-things.jpeg", "seg": "n17",
        "window": "204.83-208.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER"],
        "narration": (
            "We forgive the small things because of the mountain we've been "
            "forgiven."
        ),
        "must_show": "a close two-shot in the dusk-gold courtyard — Peter's face changed, softened, the tiredness gone out of it, and Jesus beside him watching him kindly.",
        "must_not_show": "no halo, glare or rim-light on Jesus; Peter's change must read at a glance — the burden from the opening portrait visibly lifted.",
        "scene": (
            "A close two-shot in the last dusk-gold light: Peter's weathered "
            "face turned slightly down and inward, softened and unknotted — "
            "the worn hurt from the day's first question visibly gone out of "
            "it — and beside him Jesus watching him with quiet kindness, "
            "saying nothing. The courtyard stone behind them holds the day's "
            "last warmth. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r022-b38", "out": "s38-to-be-handed-an-ocean.jpeg", "seg": "n17",
        "window": "208.27-215.79", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "COURTYARD"],
        "narration": (
            "To be handed an ocean of mercy, and then choke someone over a cup "
            "of it — that is the one thing this King cannot bear."
        ),
        "must_show": "the closing frame — the quiet circle in the dusk courtyard, Jesus at rest among them, and Peter looking down at his own two open hands in his lap.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no sky imagery, no ocean painted literally — the courtyard and the hands carry the line.",
        "scene": (
            "The courtyard at deep dusk-gold, the first cool blue gathering in "
            "the corners. The circle of disciples sits quiet and unmoving "
            "around Jesus, who is at rest on the low bench, the story told. In "
            "the foreground Peter sits on the flagstones looking down at his "
            "own two open hands cupped together in his lap, as though weighing "
            "what has been put into them. The fig tree stands black against "
            "the last warm light on the wall. The camera holds the whole still "
            "circle. Every figure has two arms, two hands and one head."
        ),
    },
]
