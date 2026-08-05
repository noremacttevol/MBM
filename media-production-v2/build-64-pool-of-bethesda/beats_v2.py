#!/usr/bin/env python3
"""V2 beat map — row 64, build-64-pool-of-bethesda (John 5:1-15).

COVERAGE: 41 pictures over 231.5 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (John 5:1-15 KJV):
  v2    "a pool ... called BETHESDA, having FIVE PORCHES" — by the sheep
        gate: a colonnaded pool complex, five covered porches ringing the
        water, crowded with "a great multitude of impotent folk, of
        blind, halt, withered" — the suffering crowd painted with FULL
        dignity: real people waiting, never a horror tableau.
  v3-4  the troubled-water LEGEND — the narration debunks it ('No angel.
        No water. No race. The pool had nothing to do with it'): NO
        angel is ever painted; the water's stirring appears only as the
        crowd's watching hope toward an ordinary surface.
  v5    "an infirmity THIRTY AND EIGHT YEARS" — longer than most
        lifespans of that world; his mat and spot are his whole
        identity. Painted with dignity: a strong-faced man wasted by
        years, never grotesque.
  v6    "Jesus ... KNEW that he had been now a long time in that case,
        he saith, WILT THOU BE MADE WHOLE?" — the question the row turns
        on: asked kindly and meaning it.
  v7    "Sir, I HAVE NO MAN..." — he answers with the system, not with
        yes; the narration flags it.
  v8-9  "RISE, take up thy bed, and WALK. And IMMEDIATELY the man was
        made whole" — the healing without water, race or ritual; the
        standing-up beat is the row's summit.
  v10-13 the sabbath rule-keepers and the mat; "he that was healed WIST
        NOT WHO IT WAS" — grace preceding even identification.
  v14   "Jesus FINDETH him in the temple ... sin no more" — the second
        finding; counsel, not threat.
  v15   "the man departed, and TOLD the Jews that it was Jesus."

TIME OF DAY: one day — bright morning at the porches, midday for the
healing and the sabbath challenge, warm afternoon for the temple
finding and the telling. The porch scenes are shaded colonnaide light
against the pool's open glare.

CONTENT-CARE: healing dignity laws — the multitude's suffering shown as
waiting and hoping humans, no medical horror; the healed man's atrophy
told in the narration, not rendered grotesquely; the rule-keepers hard
and correct, not cartoons.

CHANGING CONDITION (kept OUT of the locks): the man's state — lying,
questioned, STANDING, walking, carrying the mat, found in the temple.
The mat migrates: bed → burden → rolled bundle under a walking arm.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "SICKMAN": (
        "SICK MAN LOCK: the man is the same in every shot — about sixty, "
        "once-strong and long-wasted, with a lined grey-bearded face, "
        "watchful defeated eyes that learned patience the hard way, and "
        "big-knuckled hands. He wears a threadbare DARK MOSS-GREY tunic "
        "with a frayed DARK BROWN blanket-cloak (never cream, never "
        "white). His mat is a worn reed-and-cloth pallet, its edges "
        "shiny with thirty-eight years of the same hands. His face is "
        "shown clearly and with full dignity in every state."
    ),
    "BETHESDA": (
        "BETHESDA LOCK: the pool complex by the sheep gate — a broad "
        "sunken rectangular pool of still green water with stone steps "
        "down one side, ringed by FIVE covered porches on stout "
        "columns, their shade crowded with the waiting sick on mats and "
        "pallets. The same pool, steps, columns and porches throughout. "
        "The waiting people wear worn SATURATED DEEP earth colours "
        "(never cream, never white; only Jesus wears cream); their "
        "faces are shown clearly and with dignity."
    ),
    "KEEPERS": (
        "RULE-KEEPERS LOCK: the sabbath authorities are the same two "
        "men in every shot — a tall dry senior with a narrow face and "
        "a precise clipped grey beard, and a broad younger one with "
        "heavy brows. They wear fine NEAR-BLACK INDIGO robes with "
        "fringed shawls (never cream, never white). Faces shown "
        "clearly — correct men, not cartoons."
    ),
    "TEMPLE": (
        "TEMPLE COURT LOCK: a quieter side court of the temple — pale "
        "limestone paving, a colonnade's shade along one side, a few "
        "worshippers passing, warm afternoon light. The same court for "
        "the finding beats."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r064-b01", "out": "s01-by-the-sheep-gate-in.jpeg", "seg": "n0",
        "window": "0.28-6.52", "wide": True, "jesus": False, "ref": False,
        "locks": ["BETHESDA"],
        "narration": (
            "By the sheep gate in Jerusalem there was a pool called Bethesda, "
            "ringed by five covered porches."
        ),
        "must_show": "SCRIPTURE-EXACT: the place — the sunken green pool with its stone steps, and the FIVE covered porches ringing it, their shade already peopled; the whole complex in one establishing frame.",
        "must_not_show": "no halo, glare or rim-light; five porches countable; the water still and ordinary.",
        "scene": (
            "In the bright morning by the sheep gate, the camera "
            "on a porch roof taking the whole complex from the "
            "side, the "
            "pool complex lies open to the sky: the broad "
            "sunken rectangle of still green water with "
            "its worn stone steps descending one side, "
            "and around it the five covered porches on "
            "their stout columns, each strip of shade "
            "lined with the low shapes of mats and their "
            "waiting owners — a whole architecture built "
            "around hope in water. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b02", "out": "s02-rise-take-up-thy-bed.jpeg", "seg": "j2",
        "window": "112.06-114.34", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKMAN", "BETHESDA"],
        "narration": "Rise, take up thy bed, and walk.",
        "must_show": "SCRIPTURE-EXACT: the command — close on Jesus's face giving the three imperatives down to the lying man: quiet, total authority without one raised tone.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the command CALM — three words changing thirty-eight years, delivered like directions.",
        "scene": (
            "Close in the porch shade: Jesus's face bent "
            "toward the lying man, giving the three "
            "commands with the unhurried plainness of a "
            "man telling a neighbour the way to the "
            "market — no gesture, no raised voice, "
            "nothing in the frame but quiet certainty "
            "meeting a lifetime of lying down — while "
            "below, at the frame's edge, the man's "
            "startled eyes are already wide on him. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r064-b03", "out": "s03-and-those-porches-were-full.jpeg", "seg": "n0",
        "window": "6.52-22.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["BETHESDA"],
        "narration": (
            "And those porches were full of the city's most hopeless people — "
            "the blind, the lame, the paralyzed — all waiting on a legend: "
            "every so often, the story went, the water would stir, and the "
            "first one in would be healed."
        ),
        "must_show": "SCRIPTURE-EXACT: the multitude and the legend — the porches close: rows of waiting people, every face angled toward the still water; hope aimed at a surface.",
        "must_not_show": "no halo, glare or rim-light; NO angel, NO stirring shown — the water plain; the WATCHING is the legend's whole visible life; the sick painted with dignity.",
        "scene": (
            "Along the shaded porches the waiting city "
            "lies in its rows — a blind elder with his "
            "face tuned to the sounds of the water, a "
            "young paralysed man propped on his side by "
            "his mother, a withered-armed weaver with "
            "his useless shuttle beside him — dozens of "
            "them, each on a worn mat, and every face "
            "in the shade angled the same direction: "
            "toward the flat green unmoving surface "
            "that owes them, by legend, one stirring "
            "and one winner. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b04", "out": "s04-no-angel.jpeg", "seg": "n4",
        "window": "118.53-119.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["BETHESDA"],
        "narration": "No angel.",
        "must_show": "the debunking — the pool's surface alone, flat, green, utterly still and ordinary; the legend's stage, empty.",
        "must_not_show": "no halo, glare or rim-light, NO figure, NO ripple — dead-calm ordinary water; the two words made of stillness.",
        "scene": (
            "The pool's surface fills the frame, flat "
            "and utterly still — green-tinged water "
            "holding the porches' reflected columns "
            "without one ripple, a single leaf sitting "
            "motionless on it — ordinary water in an "
            "ordinary basin, photographed at the exact "
            "moment the story requires it to be nothing "
            "more than that. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b05", "out": "s05-imagine-the-math-of-that.jpeg", "seg": "n0",
        "window": "22.75-26.99", "wide": True, "jesus": False, "ref": False,
        "locks": ["BETHESDA"],
        "narration": "Imagine the math of that place. Hundreds waiting.",
        "must_show": "the arithmetic — the widest porch view: mats beyond counting down the colonnades' whole length; the denominator of the cruellest fraction in Jerusalem.",
        "must_not_show": "no halo, glare or rim-light; the number felt — rows receding past focus; dignity held at scale.",
        "scene": (
            "Down the longest porch, the camera low behind the "
            "nearest mats, the rows recede "
            "past counting — row behind row of the "
            "waiting sick along the colonnade's whole "
            "shaded length, water jars and bundles "
            "between them, families camped beside their "
            "own — the arithmetic of the place laid out "
            "in reed pallets: hundreds of entrants, "
            "every day, for a race with one prize. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r064-b06", "out": "s06-and-the-fastest-one-wins.jpeg", "seg": "n0 + n1",
        "window": "28.20-35.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN", "BETHESDA"],
        "narration": (
            "And the fastest one wins a race for the people who can't run. One "
            "man had been lying there thirty-eight years."
        ),
        "must_show": "the protagonist found — the camera arriving at ONE mat among the many: the grey-bearded man on his shiny-edged pallet in his long-held spot, introduced out of the multitude.",
        "must_not_show": "no halo, glare or rim-light; his spot visibly ANCIENT — the worn stone, the polished mat edge; one man emerging from the crowd's arithmetic.",
        "scene": (
            "Among the porch's many mats the frame "
            "settles on one: the grey-bearded man lying "
            "on a pallet whose edges shine with decades "
            "of the same hands, in a spot where the "
            "stone floor itself is worn into the shallow "
            "map of one body's years — his watchful "
            "defeated eyes on the water like all the "
            "rest, but older at it than anyone under "
            "these roofs. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b07", "out": "s07-let-that-number-land-that.jpeg", "seg": "n1",
        "window": "35.25-41.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN"],
        "narration": (
            "Let that number land. That was longer than most people in that "
            "world even got to be alive."
        ),
        "must_show": "the number's weight — close on the man's lined face and grey beard: thirty-eight years legible as geology; a lifespan spent horizontal.",
        "must_not_show": "no halo, glare or rim-light; the years in the face, not in wretchedness — time's work, dignified.",
        "scene": (
            "Close on the man's face in the porch "
            "shade: the grey beard, the deep lines "
            "rayed from the watchful eyes, skin gone "
            "the colour of the shade itself — "
            "thirty-eight years laid down in a face "
            "like strata in a cut bank, a whole "
            "human lifespan's worth of mornings spent "
            "on one mat watching one unmoving surface. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r064-b08", "out": "s08-whole-generations-had-grown-up.jpeg", "seg": "n1",
        "window": "41.14-49.03", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN", "BETHESDA"],
        "narration": (
            "Whole generations had grown up and grown old while he lay on that "
            "mat, watching the water, losing the same race every time."
        ),
        "must_show": "time passing around stillness — the man on his mat exactly as ever, while around him the porch's traffic blurs with implied years: children, adults, elders passing his fixed point.",
        "must_not_show": "no halo, glare or rim-light; his stillness against their motion — one continuous scene, the passage of years as passing people.",
        "scene": (
            "The man lies in his worn spot exactly as "
            "always — and around his stillness the "
            "porch moves: a child chasing a hoop past "
            "his feet, a young couple stepping around "
            "his mat, an old woman who was surely once "
            "that child shuffling by along the same "
            "route — the world's generations flowing "
            "past one fixed grey point that has "
            "watched the water outlast them all. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r064-b09", "out": "s09-one-winner.jpeg", "seg": "n0",
        "window": "26.99-28.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["BETHESDA"],
        "narration": "One winner.",
        "must_show": "the fraction's numerator — the pool steps close: ONE person's wet footprints climbing out of the water up the stone; everyone else's morning, decided.",
        "must_not_show": "no halo, glare or rim-light; footprints only — the winner already gone; the economy of the place in wet marks on stone.",
        "scene": (
            "Close on the pool's worn stone steps in "
            "the morning light: one set of wet "
            "footprints climbs them out of the water — "
            "small, bare, already drying at the edges — "
            "and no other mark on the pale stone "
            "anywhere: the day's entire dividend, "
            "walked away before the frame arrived, "
            "leaving hundreds of watchers back in the "
            "shade with tomorrow. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b10", "out": "s10-by-now-being-the-sick.jpeg", "seg": "n1",
        "window": "49.03-55.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN"],
        "narration": (
            "By now, being the sick man by the pool was not just his condition. "
            "It was his whole identity."
        ),
        "must_show": "identity as address — the man's whole small world in one close frame: the mat, the bowl, the folded spare cloth, the wall-corner he owns; a self, furnished.",
        "must_not_show": "no halo, glare or rim-light; the kit complete and orderly — a life administered from four square feet.",
        "scene": (
            "Close on the man's corner of the porch: "
            "the shiny-edged mat squared to the wall, "
            "the drinking bowl at its exact reach, a "
            "spare cloth folded at the head, a cord "
            "strung on two pegs holding his few "
            "things — four square feet of colonnade "
            "administered with the neatness of "
            "decades — less a sick man's spot than a "
            "citizen's entire address. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b11", "out": "s11-jesus-walked-those-porches-past.jpeg", "seg": "n2",
        "window": "55.80-61.48", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKMAN", "BETHESDA"],
        "narration": (
            "Jesus walked those porches, past hundreds of the suffering, and "
            "stopped at this one man."
        ),
        "must_show": "SCRIPTURE-EXACT: the stopping — Jesus mid-stride among the mats coming to a halt at the grey man's spot; one chosen stillness in a walked line.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the stop itself the beat — momentum ending at one particular mat.",
        "scene": (
            "Down the crowded porch Jesus comes walking "
            "between the rows of mats — and stops: his "
            "stride ending exactly at the grey-bearded "
            "man's worn corner, his cream robe settling "
            "with the halt, his face turning down to "
            "the lying figure with full attention — "
            "hundreds of mats behind him and hundreds "
            "ahead, and the whole walk narrowing to "
            "this one. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r064-b12", "out": "s12-john-says-he-knew-knew.jpeg", "seg": "n2",
        "window": "61.48-65.98", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKMAN"],
        "narration": "John says he knew — knew he had been there a long time.",
        "must_show": "the knowing — close on Jesus's face reading the man below: the years understood at a glance, the whole history received before a word.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the knowledge in the gaze — comprehension without inquiry.",
        "scene": (
            "Close on Jesus's face looking down at the "
            "lying man: the warm eyes moving once over "
            "the shiny mat-edge, the hollowed stone, "
            "the ancient neatness of the little corner "
            "— and coming to rest on the man's face "
            "with the settled comprehension of someone "
            "who has just read a whole thirty-eight "
            "year ledger in four square feet of porch. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r064-b13", "out": "s13-and-then-he-asked-him.jpeg", "seg": "n2 + j1",
        "window": "66.40-73.67", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKMAN"],
        "narration": (
            "And then he asked him a question that sounds almost unkind, until "
            "you sit with it: Wilt thou be made whole?"
        ),
        "must_show": "SCRIPTURE-EXACT: the question — Jesus crouched to the man's level asking it; the man's face taking a question nobody has asked him in decades.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the question kind and real — and landing like something long-forgotten.",
        "scene": (
            "Jesus has come down into a crouch beside "
            "the mat, his face level with the lying "
            "man's, and the question passes between "
            "them — and on the man's grey face the "
            "strange work of receiving it: eyes "
            "narrowing, then widening, the expression "
            "of someone being asked, after decades of "
            "'how long' and 'whose fault', the one "
            "question that was never once on offer: "
            "what do you WANT. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b14", "out": "s14-do-you-want-to-be.jpeg", "seg": "n3",
        "window": "74.81-79.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN"],
        "narration": (
            "Do you want to be made well? After thirty-eight years, that is a "
            "real question."
        ),
        "must_show": "the question's teeth — the man's face alone, working: want, fear, habit and hope contending over features that stopped practising wanting years ago.",
        "must_not_show": "no halo, glare or rim-light; the contention honest — a real question meeting a man out of practice at answering it.",
        "scene": (
            "Close on the man's face alone in the porch "
            "shade, the question working in it: want "
            "surfacing and flinching back, hope "
            "checking itself against thirty-eight "
            "years of evidence, the watchful eyes "
            "flickering between the crouched stranger "
            "and the old familiar water — a man "
            "discovering that the muscle for wanting, "
            "like his legs, has not been used in a "
            "very long time. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b15", "out": "s15-healing-would-mean-a-new.jpeg", "seg": "n3",
        "window": "79.50-85.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN", "BETHESDA"],
        "narration": (
            "Healing would mean a new name, new work, a whole new life — and no "
            "more excuse."
        ),
        "must_show": "the cost of yes — the man's gaze travelling OUT of the porch toward the bright working city beyond the columns: porters, builders, the market's noise; the terrifying world of the well.",
        "must_not_show": "no halo, glare or rim-light; the city bright and demanding — whole life visible as work; the porch shade safe behind.",
        "scene": (
            "From the man's low vantage the view runs "
            "out between the columns into the bright "
            "working city — porters under loads on the "
            "gate road, a builder's scaffold loud with "
            "hammers, market awnings and hurrying "
            "feet — the whole strenuous country of the "
            "well people, lit hard and asking "
            "everything, while the porch's kind grey "
            "shade holds him back from its edge like "
            "an old blanket. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b16", "out": "s16-and-notice-the-man-does.jpeg", "seg": "n3",
        "window": "85.46-91.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN"],
        "narration": (
            "And notice: the man does not answer yes. He does not answer at "
            "all."
        ),
        "must_show": "the non-answer — the man's mouth opening and producing not-yes: eyes sliding away toward the pool, the deflection beginning.",
        "must_not_show": "no halo, glare or rim-light; the slide of the eyes the tell — away from the asker, toward the system.",
        "scene": (
            "Close on the man mid-reply: his mouth "
            "open, but his eyes already gone — slid "
            "away from the crouched questioner toward "
            "the old green water, one big-knuckled "
            "hand rising to gesture at the steps — a "
            "yes-shaped question being answered, out "
            "of decades of habit, with the address of "
            "the problem instead. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b17", "out": "s17-he-answers-with-the-obstacle.jpeg", "seg": "n3",
        "window": "91.82-93.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN", "BETHESDA"],
        "narration": "He answers with the obstacle:",
        "must_show": "the obstacle indicated — the man's arm extended toward the pool steps, the explaining gesture; his case, presented for the ten-thousandth time.",
        "must_not_show": "no halo, glare or rim-light; the gesture practised — an argument worn smooth as the mat's edge.",
        "scene": (
            "From beside the mat: the man's arm "
            "extended full toward the pool's distant "
            "steps, fingers spread in the old "
            "explaining gesture, his grey face turned "
            "up to the listener with the practised "
            "reasonableness of a man presenting a "
            "case he has made ten thousand times to "
            "anyone who would pause — the obstacle, "
            "exhibited; the want, still unanswered. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r064-b18", "out": "s18-sir-i-have-no-man.jpeg", "seg": "s7",
        "window": "94.31-101.75", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKMAN", "BETHESDA"],
        "narration": (
            "Sir, I have no man, when the water is troubled, to put me into the "
            "pool: but while I am coming, another steppeth down before me."
        ),
        "must_show": "SCRIPTURE-EXACT: the system explained — the man's account playing out in his gesture toward pool and crowd: no helper, always another first; Jesus listening with unmoved kindness.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the explanation honoured — real grief in it; and Jesus's attention resting on the MAN, not the system.",
        "scene": (
            "The man's whole account fills his corner "
            "of the porch — one hand at the empty air "
            "beside him where a helper has never "
            "stood, the other sweeping toward the "
            "steps where the faster ones go down — "
            "grief and administration mixed in his "
            "lined face — while Jesus, still crouched, "
            "listens with complete kindness and "
            "complete disinterest in the entire "
            "mechanism being described. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b19", "out": "s19-while-dragging-myself-toward-it.jpeg", "seg": "n3b",
        "window": "102.95-106.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN", "BETHESDA"],
        "narration": (
            "While I'm dragging myself toward it, somebody else always gets "
            "down there first."
        ),
        "must_show": "the lost race remembered — the man's memory rendered: himself mid-drag on the stones toward the steps, and past him another's feet already splashing down; the perennial defeat.",
        "must_not_show": "no halo, glare or rim-light; the drag dignified — effort total, defeat structural; one remembered scene, not a montage.",
        "scene": (
            "The old race replays: the man mid-drag "
            "across the sun-hot stones toward the "
            "steps — elbows planted, the mat left "
            "behind, his whole strength in three feet "
            "of progress — while past his straining "
            "shoulder another man's quick legs are "
            "already splashing down into the water "
            "ahead of him, the day's one prize gone "
            "again while he watches from the paving. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r064-b20", "out": "s20-he-was-explaining-the-system.jpeg", "seg": "n3b",
        "window": "106.76-111.45", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKMAN"],
        "narration": (
            "He was explaining the system. Jesus had not asked him about the "
            "system."
        ),
        "must_show": "the mismatch — the two faces close: the man still explaining toward the pool; Jesus's steady gaze fixed only on him, waiting past the system for the person.",
        "must_not_show": "no halo, glare or rim-light on Jesus; two attentions aimed differently — one at machinery, one at a man.",
        "scene": (
            "Close on the two faces in the porch "
            "shade: the man's still angled away toward "
            "his pool, hand mid-gesture, deep in the "
            "system's grammar — and Jesus's face "
            "aimed entirely at him, steady, unmoved by "
            "a single word of the mechanism, waiting "
            "at the person's own door while the person "
            "gives directions to a different address. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r064-b21", "out": "s21-get-up-pick-up-your.jpeg", "seg": "n4",
        "window": "115.47-118.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKMAN", "BETHESDA"],
        "narration": "Get up. Pick up your mat. Walk.",
        "must_show": "the commands landing — the man's body already ANSWERING: shoulders coming off the mat, one arm bracing, the impossible obedience beginning mid-frame.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the rising STARTED — caught between lying and sitting; power arriving as motion.",
        "scene": (
            "The three commands are still in the air "
            "and the man's body is already answering "
            "them: shoulders lifting off the ancient "
            "mat, one big-knuckled hand braced flat on "
            "the stone, the tendons of a working arm "
            "remembering their trade mid-motion — "
            "thirty-eight years of horizontal ending "
            "in real time while Jesus stands over him, "
            "watching what his sentence is doing. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r064-b22", "out": "s22-no-water-no-race-the.jpeg", "seg": "n4",
        "window": "119.69-124.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN", "BETHESDA"],
        "narration": "No water. No race. The pool had nothing to do with it.",
        "must_show": "the legend bypassed — the man RISING to his feet with the pool behind him, DRY, untouched, out of the story; healing happening with its back to the water.",
        "must_not_show": "no halo, glare or rim-light; the pool visibly irrelevant — behind him, unentered; his rising faced AWAY from it.",
        "scene": (
            "The man comes up onto his feet in the "
            "porch — swaying once, then steadying, his "
            "arms out finding a balance his body last "
            "held as a young man — and behind his "
            "back, flat and green and completely "
            "unconsulted, the famous pool lies exactly "
            "as still as ever: the whole legend "
            "standing in its basin, dry of any part "
            "in what is happening three steps away "
            "from it. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r064-b23", "out": "s23-and-immediately-the-man-was.jpeg", "seg": "n4",
        "window": "124.53-131.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN"],
        "narration": (
            "And immediately the man was made whole — thirty-eight years of "
            "atrophy gone between one breath and the next."
        ),
        "must_show": "the wholeness — close on the standing man's legs and planted feet: bearing full weight, steady on the stone; the impossible verticality, plain.",
        "must_not_show": "no halo, glare or rim-light; no transformation effects — legs simply working; the miracle told as posture.",
        "scene": (
            "Close at the man's planted feet and "
            "standing legs in the porch light: bare "
            "soles set flat and firm on the worn "
            "stone, the long muscles of the calves "
            "carrying full weight with the plain "
            "competence of a market porter's — "
            "thirty-eight years of wasting reversed "
            "somewhere between one breath and the "
            "next, and visible now only as the most "
            "ordinary sight in the world: a man "
            "standing up. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b24", "out": "s24-legs-that-had-forgotten-what.jpeg", "seg": "n4",
        "window": "131.27-135.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN"],
        "narration": "Legs that had forgotten what weight felt like took his weight.",
        "must_show": "the reunion — the man's face looking DOWN at his own standing legs: wonder aimed at his own body, hands hovering over his thighs.",
        "must_not_show": "no halo, glare or rim-light; the astonishment self-directed — a man meeting his own legs.",
        "scene": (
            "The man stands looking down at his own "
            "legs with his hands hovering above his "
            "thighs, not quite daring to touch — his "
            "grey face folded into pure wonder aimed "
            "at his own anatomy, shifting his weight "
            "left and right in small experimental "
            "sways like a man testing new ground — "
            "the oldest acquaintance of his life, met "
            "again after thirty-eight years, holding "
            "him up. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r064-b25", "out": "s25-he-stood-up-rolled-up.jpeg", "seg": "n4",
        "window": "135.16-139.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN", "BETHESDA"],
        "narration": (
            "He stood up, rolled up the mat that had been his whole world, and "
            "walked."
        ),
        "must_show": "SCRIPTURE-EXACT: the mat rolled — the man rolling his ancient pallet with strong sure hands, tucking it under one arm, first steps down the porch; the world becoming luggage.",
        "must_not_show": "no halo, glare or rim-light; the roll decisive — a whole identity packed in one motion; the walking already begun.",
        "scene": (
            "The man rolls his ancient shiny-edged mat "
            "with two strong turns of his big hands — "
            "thirty-eight years of address becoming a "
            "bundle — tucks it up under one arm and "
            "walks: first steps down the porch's "
            "length, uneven then evening out, past "
            "mats whose owners are rising on their "
            "elbows all along the colonnade to watch "
            "him go. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r064-b26", "out": "s26-it-was-the-sabbath-so.jpeg", "seg": "n5",
        "window": "140.28-146.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN", "KEEPERS"],
        "narration": (
            "It was the sabbath, so the rule-keepers stopped him at once — not "
            "to celebrate him, but to tell him:"
        ),
        "must_show": "SCRIPTURE-EXACT: the stopping — the two dark-robed keepers intercepting the walking man in the street, the senior's flat hand raised at the rolled mat; procedure meeting miracle.",
        "must_not_show": "no halo, glare or rim-light; their focus visibly on the MAT, sliding past the standing miracle carrying it.",
        "scene": (
            "In the bright street beyond the porches "
            "the two dark-robed keepers have stepped "
            "into the walking man's path — the tall "
            "dry senior's flat hand raised, his narrow "
            "eyes fixed not on the impossibly upright "
            "figure but on the rolled mat under its "
            "arm — a man's first walk in thirty-eight "
            "years being processed, at its third "
            "minute, as a carrying violation. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r064-b27", "out": "s27-it-is-the-sabbath-day.jpeg", "seg": "s10",
        "window": "146.85-151.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["KEEPERS"],
        "narration": "It is the sabbath day: it is not lawful for thee to carry thy bed.",
        "must_show": "SCRIPTURE-EXACT: the citation — close on the senior keeper delivering the rule: precise, correct, and blind; the regulation recited at a miracle.",
        "must_not_show": "no halo, glare or rim-light; correctness without cartoon — a man being exactly right about exactly the wrong thing.",
        "scene": (
            "Close on the tall senior keeper mid-"
            "citation: the clipped grey beard moving "
            "around the precise words, one long finger "
            "indicating the offending bundle, his "
            "narrow face wearing the settled assurance "
            "of a man upholding what must be upheld — "
            "the rule delivered accurately, completely, "
            "and at the one moment in its history when "
            "it has managed to miss everything. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r064-b28", "out": "s28-the-sabbath-not-allowed-to.jpeg", "seg": "n5b",
        "window": "152.42-155.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN"],
        "narration": "It's the sabbath. You're not allowed to carry that mat.",
        "must_show": "the absurdity received — the healed man's face hearing it: blinking between his own new legs and the objection; the mat hugged unconsciously closer.",
        "must_not_show": "no halo, glare or rim-light; bewilderment gentle — a man translating between two worlds that don't share a language.",
        "scene": (
            "Close on the healed man's face between "
            "his interceptors: blinking, glancing down "
            "once at his own standing legs and back "
            "up at the citation being read over them, "
            "the rolled mat hugged unconsciously "
            "tighter under his arm — a man fresh from "
            "the far side of the impossible, being "
            "asked to account for his luggage. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r064-b29", "out": "s29-a-man-walks-for-the.jpeg", "seg": "n5b",
        "window": "155.39-160.91", "wide": True, "jesus": False, "ref": False,
        "locks": ["SICKMAN", "KEEPERS"],
        "narration": (
            "A man walks for the first time in thirty-eight years and the first "
            "thing anybody says to him is about the mat."
        ),
        "must_show": "the scene's whole comedy and grief — wide: the standing miracle flanked by two men pointing at a bundle; the street's passers-by slowing at the strangeness.",
        "must_not_show": "no halo, glare or rim-light; the composition's irony structural — all official attention on four pounds of rolled reeds.",
        "scene": (
            "Wide in the bright street, the camera at the wall "
            "taking all three in profile: the healed "
            "man upright at the centre — a walking "
            "wonder on legs the whole quarter knows "
            "have not worked in a generation — and "
            "flanking him the two dark-robed keepers, "
            "both oriented entirely toward the rolled "
            "reed mat under his arm, one mid-citation, "
            "one taking notes — while along the "
            "street's edge passers-by slow and stare "
            "at everything the officials are managing "
            "not to see. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b30", "out": "s30-and-here-is-the-astonishing.jpeg", "seg": "n5b",
        "window": "160.91-168.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN", "KEEPERS"],
        "narration": (
            "And here is the astonishing part: when they asked who had healed "
            "him, he did not know. He had never asked the name."
        ),
        "must_show": "the unknown benefactor — the man's honest empty shrug under the keepers' questioning: palms up, name absent; healed by someone he cannot identify.",
        "must_not_show": "no halo, glare or rim-light; the shrug genuine — no evasion; a gift received before its giver was known.",
        "scene": (
            "Under the two keepers' bent questioning "
            "the healed man's hands come up in an "
            "honest empty shrug — palms open, brows "
            "up, mouth making the shape of not-"
            "knowing — the most important name of his "
            "entire life simply absent from him, the "
            "healing having outrun the introduction — "
            "while the stocky keeper's stylus hovers "
            "over a tablet with nothing to write. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r064-b31", "out": "s31-jesus-had-healed-a-man.jpeg", "seg": "n5b",
        "window": "168.61-175.86", "wide": True, "jesus": True, "ref": REF,
        "locks": ["BETHESDA"],
        "narration": (
            "Jesus had healed a man who could not identify him, had not "
            "followed him, and had not even clearly said yes."
        ),
        "must_show": "the giver gone — back at the porches: Jesus already moving away down the colonnade amid the crowd, unmarked, anonymous; the grace's author leaving without credit.",
        "must_not_show": "no halo, glare or rim-light on Jesus; his anonymity the beat — one figure among many, departing unthanked.",
        "scene": (
            "Down the crowded colonnade, the camera behind the "
            "porch crowd's shoulders, Jesus moves "
            "away with the porch's ordinary traffic — "
            "unremarked, unfollowed, one figure "
            "among the many between the columns — "
            "passing out of the story he just "
            "rewrote while its beneficiary, somewhere "
            "behind, cannot so much as name him: "
            "grace walking away with its collar up, "
            "credit left lying where it fell. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r064-b32", "out": "s32-grace-came-first-everything-else.jpeg", "seg": "n5b",
        "window": "175.86-179.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN"],
        "narration": "Grace came first. Everything else came after.",
        "must_show": "the order of things — the man walking the street with his mat, whole and nameless-graced: the fact of him as the doctrine; sequence made flesh.",
        "must_not_show": "no halo, glare or rim-light; the walking itself the sermon — healed first, everything else pending.",
        "scene": (
            "The healed man walks the bright street "
            "with his rolled mat under his arm and "
            "his new legs finding their old childhood "
            "rhythm — whole, upright, and unable to "
            "name the reason — a living sequence "
            "diagram moving through the crowd: the "
            "gift first, entire and unearned; the "
            "understanding, the believing, even the "
            "introduction, all still somewhere up the "
            "road. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r064-b33", "out": "s33-later-jesus-found-him-in.jpeg", "seg": "n6",
        "window": "180.19-187.39", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKMAN", "TEMPLE"],
        "narration": (
            "Later, Jesus found him in the temple — found him, again, the way "
            "he found the man born blind — and said to him:"
        ),
        "must_show": "SCRIPTURE-EXACT: the finding — the temple side court: the man standing in worship for the first time in decades, and Jesus arriving toward him; the second finding of the section.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the man IN the temple — where his legs have finally carried him; the finder finding.",
        "scene": (
            "In the temple's quiet side court the "
            "healed man stands in the warm afternoon "
            "light — upright among the worshippers "
            "for the first time in thirty-eight "
            "years, his rolled mat set at his feet — "
            "and across the pale paving Jesus comes "
            "toward him with the same unhurried "
            "purpose as before: the healer arriving, "
            "again, to finish an introduction the "
            "healing had skipped. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b34", "out": "s34-behold-thou-art-made-whole.jpeg", "seg": "j14",
        "window": "188.01-194.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKMAN", "TEMPLE"],
        "narration": (
            "Behold, thou art made whole: sin no more, lest a worse thing come "
            "unto thee."
        ),
        "must_show": "SCRIPTURE-EXACT: the counsel — the two close in the colonnade shade: Jesus's hand on the man's shoulder, the words given as care; the man receiving them as care.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NO threat in the delivery — a giver protecting his gift.",
        "scene": (
            "In the colonnade's warm shade the two "
            "stand close: Jesus's hand resting on the "
            "man's shoulder, his face gentle and "
            "grave with the counsel — and the man "
            "receiving it with his grey head slightly "
            "bowed, not as a warning from an "
            "authority but as what it is: the maker "
            "of his new legs asking him, carefully, "
            "to be careful where he walks them. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r064-b35", "out": "s35-look-at-you-you-are.jpeg", "seg": "n6b",
        "window": "195.11-197.34", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKMAN"],
        "narration": "Look at you — you are whole.",
        "must_show": "the delight — close on Jesus's face taking the standing man in, head to foot: a craftsman's open pleasure in the finished work.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the pleasure warm and personal — joy in the man himself.",
        "scene": (
            "Close on Jesus's face in the warm court "
            "light, taking the standing man in from "
            "head to foot with open delight — the "
            "warm eyes travelling down to the planted "
            "feet and back up with a craftsman's "
            "unhidden pleasure in a finished piece, "
            "the smile arriving whole in the beard — "
            "the maker enjoying the made, to his "
            "face. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r064-b36", "out": "s36-now-go-back-to-the.jpeg", "seg": "n6b",
        "window": "197.34-202.31", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKMAN"],
        "narration": (
            "Now don't go back to the things that were destroying you. It is "
            "not a threat."
        ),
        "must_show": "the counsel's heart — the two faces close: earnest care meeting earnest listening; a course being set, not a penalty read.",
        "must_not_show": "no halo, glare or rim-light on Jesus; tenderness explicit — the narration's 'not a threat' visible in both faces.",
        "scene": (
            "The two faces close in the warm shade: "
            "Jesus's earnest and utterly kind, the "
            "counsel leaving him with the weight of "
            "care rather than command — and the "
            "man's lined face bent toward it, "
            "listening the way he once watched "
            "water: completely — an old life being "
            "gently closed behind a man, and a new "
            "road pointed out ahead of him. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r064-b37", "out": "s37-it-is-a-man-who.jpeg", "seg": "n6b",
        "window": "202.31-208.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN"],
        "narration": (
            "It is a man who has just given you your legs back asking you not "
            "to walk them into a ditch."
        ),
        "must_show": "the image literal-adjacent — close on the man's two renewed legs standing firm on the temple paving, his own hand resting protectively on one thigh; the gift, owned and guarded.",
        "must_not_show": "no halo, glare or rim-light; the protective hand the beat — a man agreeing to take care of what he was given.",
        "scene": (
            "Close in the warm light: the man's two "
            "renewed legs planted firm on the pale "
            "temple paving — and his own big hand "
            "come down to rest flat on one thigh, "
            "half in wonder, half in vow — the "
            "posture of a man receiving custody of "
            "a treasure and signing, with one "
            "unconscious gesture, for its keeping. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r064-b38", "out": "s38-and-only-then-did-the.jpeg", "seg": "n6b",
        "window": "208.16-212.98", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKMAN"],
        "narration": (
            "And only then did the man learn the name of the one who had given "
            "him his life."
        ),
        "must_show": "the introduction — the name finally passing between them: the man's face receiving it with the weight of everything it now explains.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the name's arrival visible — a word landing on a whole rebuilt life at once.",
        "scene": (
            "Close between the two faces as the name "
            "finally crosses: Jesus giving it simply, "
            "and the man's grey face receiving it "
            "with visible re-computation — the porch, "
            "the question, the three commands, the "
            "standing up, all of it acquiring its "
            "author at once — a man learning, last "
            "of everything, what to call the reason "
            "he is vertical. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b39", "out": "s39-he-went-and-told-everyone.jpeg", "seg": "n6b + n7",
        "window": "212.98-218.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN", "TEMPLE"],
        "narration": (
            "He went and told everyone: it was Jesus. Thirty-eight years, and "
            "one question."
        ),
        "must_show": "SCRIPTURE-EXACT: the telling — the man animated among a gathering knot in the temple court, the name given out with both hands; witness as his first vocation.",
        "must_not_show": "no halo, glare or rim-light; the telling joyful and free — a name spent as fast as it was learned.",
        "scene": (
            "In the temple court the man has gathered "
            "a knot of listeners and is spending his "
            "new name with both hands — pointing back "
            "toward the colonnade, slapping his own "
            "thigh, walking two paces and back to "
            "prove it — an old porch fixture turned "
            "evangelist inside an afternoon, giving "
            "out the only fact he has ever owned "
            "outright: who. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r064-b40", "out": "s40-not-why-are-you-still.jpeg", "seg": "n7",
        "window": "218.76-226.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["SICKMAN"],
        "narration": (
            "Not: why are you still here. Not: whose fault is this. Just — do "
            "you want to be whole?"
        ),
        "must_show": "the question enshrined — the man's face at rest in the warm light, the question that changed everything still visibly resident in it.",
        "must_not_show": "no halo, glare or rim-light; the face changed for good — want, finally practised, at home in the features.",
        "scene": (
            "Close on the man's face at rest in the "
            "day's warm end: the watchful defeat gone "
            "out of the eyes and something practised "
            "and awake living there instead — the "
            "face of a man who was asked one real "
            "question after thirty-eight years of "
            "rhetorical ones, and has been answering "
            "it with his whole body ever since noon. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r064-b41", "out": "s41-the-pool-never-healed-anybody.jpeg", "seg": "n7",
        "window": "226.02-231.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["BETHESDA"],
        "narration": (
            "The pool never healed anybody. The person standing next to that "
            "man did."
        ),
        "must_show": "the closing image — the pool at evening: still, green, unchanged, the porches quieting — and in the worn spot by the wall, the man's old corner standing EMPTY, mat gone.",
        "must_not_show": "no halo, glare or rim-light; the empty corner the whole coda — the legend still in its basin, one customer permanently lost.",
        "scene": (
            "Evening settles over Bethesda: the pool "
            "flat and green and exactly as it has "
            "always been, the porches quieting into "
            "their night shapes — and by the wall, "
            "in the shallow body-worn hollow of "
            "thirty-eight years, the man's old corner "
            "stands empty: no mat, no bowl, no "
            "waiting — one space in the shade given "
            "back for good, by something the water "
            "never had. Every figure has two arms, "
            "two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "TEMPLE": "PLACE-REF/temple.jpeg",  # build-06-two-sons v2-r006-b21
}
# === end PLACE-PLATES ===
