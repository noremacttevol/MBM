#!/usr/bin/env python3
"""V2 beat map — row 93, build-93-barabbas-goes-free (Mark 15:6-15; Matt 27).

COVERAGE: 15 pictures over 83.7 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 15:6-15 KJV):
  v6-7  "at that feast he RELEASED unto them ONE PRISONER, whomsoever
        they desired. And there was one named BARABBAS... who had
        committed MURDER in the insurrection."
  v9    Pilate: "Will ye that I release unto you the KING OF THE
        JEWS?" — v10 "he KNEW that the chief priests had delivered
        him for ENVY."
  v11   "the CHIEF PRIESTS MOVED THE PEOPLE, that he should rather
        release Barabbas."
  v13-14 "they cried out again, CRUCIFY HIM. Then Pilate said, WHY,
        WHAT EVIL HATH HE DONE? And they cried out the more."
  v15   "Pilate, willing to content the people, released Barabbas...
        and delivered Jesus." — the swap: guilty freed, innocent
        handed over.

TIME OF DAY: early MORNING throughout — cold clear light on the
governor's pavement.

CONTENT-CARE: no row flags, but strict custody law — Jesus bound with
rope only, NO scourging, wounds, bruises or violence anywhere in any
frame (v15's scourging is off-screen and not in the narration). The
crowd's cry is loud, not riotous — no thrown objects, no fists on
anyone. Barabbas is rendered human — hard-worn, stunned by grace —
never a monster; the closing beats carry the mercy IN the text: the
swap as the gospel's shape.

CHANGING CONDITION (kept OUT of the locks): Barabbas's chains — on,
then struck off; the crowd — listening, worked, roaring; Pilate —
offering, bewildered, capitulating.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "PAVEMENT": (
        "PAVEMENT LOCK: the governor's judgment court — a broad "
        "stone-paved yard before the praetorium: a raised TRIBUNAL "
        "PLATFORM with a judgment seat up a short flight of steps, "
        "dark iron-clad guards at its edges, the packed crowd yard "
        "below, cold clear morning light. The same platform, steps "
        "and yard throughout."
    ),
    "PILATE": (
        "PILATE LOCK: Pilate is the same man in every shot — Roman, "
        "about fifty, clean-shaven with short iron-grey hair, in a "
        "dark bronze breastplate under a DEEP CRIMSON commander's "
        "mantle (never cream, never white); shrewd, uneasy, a "
        "politician's face over a soldier's frame."
    ),
    "BARABBAS": (
        "BARABBAS LOCK: Barabbas is the same man in every shot — "
        "about forty, heavy-built and hard-worn, matted dark hair "
        "and beard, a scar through one eyebrow, in torn DARK "
        "RUST-BROWN prison rags (never cream, never white); human "
        "and stunned, never a cartoon monster."
    ),
    "PRIESTS": (
        "PRIESTS LOCK: the chief priests — older men in DEEP "
        "CHARCOAL and DARK WINE robes with broad fringes (never "
        "cream, never white), moving through the crowd with "
        "practised urging hands and hard certain faces."
    ),
    "CROWD": (
        "CROWD LOCK: the yard crowd — city men in DARK EARTH-BROWN, "
        "RUST and SLATE robes (never cream, never white); loud and "
        "swayable, shouting with raised arms, never striking anyone "
        "or throwing anything."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r093-b01", "out": "s01-it-was-the-custom-at.jpeg", "seg": "n0",
        "window": "0.28-5.49", "wide": True, "jesus": False, "ref": False,
        "locks": ["PAVEMENT", "CROWD"],
        "narration": (
            "It was the custom at Passover for the governor to release one "
            "prisoner the crowd chose."
        ),
        "must_show": "the custom's stage — the judgment yard filling in the cold morning light: crowd gathering below the empty tribunal platform, guards taking their places; the annual choice assembling.",
        "must_not_show": "no halo, glare or rim-light; the yard EXPECTANT — a known yearly ritual, not yet a storm.",
        "scene": (
            "The cold morning fills the "
            "governor's yard for the yearly "
            "ritual: city men streaming in "
            "between the iron-clad guards, "
            "gathering below the raised "
            "tribunal with its empty "
            "judgment seat, voices trading "
            "guesses about names — the "
            "Passover custom assembling "
            "itself on schedule, one "
            "prisoner's freedom to be "
            "handed out like festival "
            "bread, to whoever the crowd "
            "calls loudest for. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r093-b02", "out": "s02-pilate-had-two-men-jesus.jpeg", "seg": "n0",
        "window": "5.49-10.17", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PAVEMENT", "PILATE", "BARABBAS"],
        "narration": "Pilate had two men: Jesus, and a killer named Barabbas.",
        "must_show": "SCRIPTURE-EXACT: the two — on the platform's edge, the pair presented: Jesus rope-bound and calm; Barabbas chained, heavy, hard-worn; Pilate between and behind them.",
        "must_not_show": "ABSOLUTE: no wounds or bruises on Jesus — rope binding only; Barabbas in chains, human not monstrous.",
        "scene": (
            "On the platform the morning's "
            "two names stand in the cold "
            "light: at one side Jesus, "
            "hands bound before him with "
            "plain rope, still and calm in "
            "his cream wool; at the other "
            "Barabbas, heavy in his chains "
            "and rust-brown rags, scarred "
            "brow lowered like a bull's — "
            "and behind them Pilate in his "
            "crimson, looking from one to "
            "the other with the easy "
            "confidence of a man holding a "
            "choice no crowd could "
            "possibly get wrong. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r093-b03", "out": "s03-pilate-could-see-jesus-had.jpeg", "seg": "n1a",
        "window": "10.79-16.17", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PILATE"],
        "narration": (
            "Pilate could see Jesus had done nothing worth death. So he put "
            "the choice to the crowd himself."
        ),
        "must_show": "SCRIPTURE-EXACT: he knew (v10) — close on Pilate studying Jesus's calm face: the verdict of innocence forming visibly in the governor's shrewd eyes.",
        "must_not_show": "no halo, glare or rim-light; Pilate's knowing UNEASY — a judge who sees the truth and is already planning around it.",
        "scene": (
            "Close on the governor reading "
            "his prisoner: the shrewd "
            "iron-grey eyes travelling the "
            "calm bound man before him and "
            "finding nothing — no sedition "
            "in the steady face, no blood "
            "on the rope-tied hands, "
            "nothing anywhere worth a "
            "Roman nail — and behind the "
            "reading, already, the "
            "politician's uneasy "
            "arithmetic: how to acquit a "
            "man without spending anything "
            "to do it. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r093-b04", "out": "s04-will-ye-that-i-release.jpeg", "seg": "s9 + n1a2",
        "window": "16.70-23.30", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PAVEMENT", "PILATE", "CROWD"],
        "narration": (
            "Will ye that I release unto you the King of the Jews? He was "
            "almost offering it to them."
        ),
        "must_show": "SCRIPTURE-EXACT: the offer — Pilate at the platform's edge, arm extended toward Jesus, the question rolled out over the upturned crowd; release dangled.",
        "must_not_show": "no halo, glare or rim-light; the offer ALMOST generous — Pilate selling the easy answer.",
        "scene": (
            "From the platform's edge "
            "Pilate makes it easy for "
            "them: his arm sweeping back "
            "toward the calm bound figure "
            "— WILL YE THAT I RELEASE UNTO "
            "YOU — the title pitched loud "
            "over the upturned faces, THE "
            "KING OF THE JEWS — the "
            "question dangled like a gift "
            "already wrapped, a governor "
            "all but handing the crowd "
            "the verdict he wants and "
            "waiting for the obvious to "
            "come rolling back. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r093-b05", "out": "s05-he-thought-the-crowd-would.jpeg", "seg": "n1b",
        "window": "23.87-26.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["PILATE"],
        "narration": "He thought the crowd would surely pick the innocent one.",
        "must_show": "the miscalculation — close on Pilate's confident half-smile as he waits; certainty about to be corrected.",
        "must_not_show": "no halo, glare or rim-light; the confidence REAL — the surprise not yet arrived.",
        "scene": (
            "Close on a man certain of his "
            "own cleverness: Pilate's "
            "half-smile as he waits out "
            "the crowd's murmur, arms "
            "folding over the bronze "
            "breastplate, the case as good "
            "as closed in his mind — an "
            "innocent healer against a "
            "convicted killer, a choice so "
            "lopsided no mob in the "
            "empire could miss it — the "
            "last easy breath of a "
            "governor who has not yet "
            "heard the answer. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r093-b06", "out": "s06-but-the-chief-priests-worked.jpeg", "seg": "n2",
        "window": "27.46-32.24", "wide": True, "jesus": False, "ref": False,
        "locks": ["PAVEMENT", "PRIESTS", "CROWD"],
        "narration": (
            "But the chief priests worked the crowd, and they shouted for "
            "Barabbas instead."
        ),
        "must_show": "SCRIPTURE-EXACT: moved the people (v11) — the priests threading the crowd, urging hands at shoulders, words in ears; the yard's cry turning to BARABBAS.",
        "must_not_show": "no halo, glare or rim-light; the working VISIBLE — persuasion travelling man to man ahead of the shout.",
        "scene": (
            "Through the packed yard the "
            "dark-robed priests work their "
            "trade: a hand pressing one "
            "man's shoulder, a word laid "
            "quick in another's ear, "
            "urging fingers pointing the "
            "chant like men setting "
            "fires down a dry hedgerow — "
            "and behind them the crowd "
            "catches, row by row, until "
            "the yard is roaring one "
            "name at the platform, and it "
            "is the wrong one: BARABBAS. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r093-b07", "out": "s07-pilate-asked-them-what-he.jpeg", "seg": "n2",
        "window": "32.24-38.09", "wide": True, "jesus": False, "ref": False,
        "locks": ["PAVEMENT", "PILATE", "CROWD"],
        "narration": (
            "Pilate asked them what he should do with Jesus, then — and "
            "they answered with one word."
        ),
        "must_show": "the second question — Pilate stunned at the rail, palms out asking what-then; the crowd's arms rising as the one-word answer gathers.",
        "must_not_show": "no halo, glare or rim-light; Pilate's composure CRACKING — the script gone wrong in his hands.",
        "scene": (
            "The governor's script comes "
            "apart at the rail: Pilate "
            "leaning out with both palms "
            "open — WHAT THEN, what shall "
            "I do with him — the question "
            "of a man suddenly following "
            "instead of leading — and "
            "below him the yard's arms "
            "rising in one motion, "
            "hundreds of mouths drawing "
            "the same breath for the same "
            "single word, the morning "
            "tipping past anywhere he "
            "planned for it to go. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r093-b08", "out": "s08-crucify-him-crucify-him-that.jpeg", "seg": "s13 + n2b",
        "window": "38.63-44.34", "wide": True, "jesus": False, "ref": False,
        "locks": ["PAVEMENT", "CROWD", "PRIESTS"],
        "narration": "Crucify him. Crucify him. That was it. That was the answer.",
        "must_show": "SCRIPTURE-EXACT: the cry — the yard at full roar, fists and arms up, the word visibly on every mouth; the priests satisfied at the edges.",
        "must_not_show": "no halo, glare or rim-light; loud but NOT riotous — no objects thrown, no one struck; the horror is the word itself.",
        "scene": (
            "The answer comes back with "
            "one terrible voice: the whole "
            "yard roaring the same word, "
            "arms and fists in the cold "
            "morning air, the syllables "
            "readable on every open "
            "mouth — CRUCIFY — while at "
            "the crowd's edges the "
            "dark-robed priests stand "
            "quiet at last, their work "
            "finished and shouting for "
            "itself — no stone thrown, "
            "no blow struck, nothing but "
            "a word, and the word enough. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r093-b09", "out": "s09-and-pilate-could-not-make.jpeg", "seg": "n2b + s14",
        "window": "44.34-48.74", "wide": False, "jesus": False, "ref": False,
        "locks": ["PILATE"],
        "narration": (
            "And Pilate could not make sense of it. Why, what evil hath he "
            "done?"
        ),
        "must_show": "SCRIPTURE-EXACT: the why — close on Pilate's baffled face over the roar, palms spread: a judge asking a mob for a charge and getting volume.",
        "must_not_show": "no halo, glare or rim-light; the bafflement GENUINE — reason arguing with a wave.",
        "scene": (
            "Close on reason losing to "
            "volume: Pilate's face over "
            "the rail, genuinely baffled, "
            "palms spread at the roaring "
            "yard — WHY, WHAT EVIL HATH HE "
            "DONE — a Roman judge asking "
            "for one chargeable fact, one "
            "witness, one line for the "
            "record, and receiving only "
            "the word again, louder — the "
            "machinery of law discovering "
            "it has no gear that meshes "
            "with a crowd. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r093-b10", "out": "s10-why-he-asked-them-what.jpeg", "seg": "n2c",
        "window": "50.35-53.28", "wide": True, "jesus": False, "ref": False,
        "locks": ["PAVEMENT", "PILATE", "CROWD"],
        "narration": "Why? he asked them. What has he actually done?",
        "must_show": "the unanswered question — the wide yard: Pilate's asking posture against the wall of roaring faces; no answer anywhere in the crowd, only the cry again.",
        "must_not_show": "no halo, glare or rim-light; the crowd's NON-ANSWER the picture — not one face explaining, every face shouting.",
        "scene": (
            "The wide frame holds the "
            "question and its non-answer "
            "together: on the platform the "
            "crimson-mantled governor with "
            "his arms open, still asking "
            "for a reason — and below him "
            "the sea of faces giving back "
            "none: not one mouth shaping "
            "an accusation, not one "
            "finger listing a crime, just "
            "the cry again and again "
            "rolling off the stone walls — "
            "WHY, asked into a wind that "
            "only knows one word. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r093-b11", "out": "s11-the-man-holding-all-the.jpeg", "seg": "n2c",
        "window": "53.28-59.87", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PAVEMENT", "PILATE"],
        "narration": (
            "The man holding all the power in that courtyard said out loud "
            "that there was no case — and then handed him over anyway."
        ),
        "must_show": "SCRIPTURE-EXACT: the capitulation (v15) — Pilate turning away from the rail with a surrendering wave toward Jesus; power folding to noise; Jesus calm as the order passes.",
        "must_not_show": "ABSOLUTE: no scourging, wounds or violence — the handing-over is a GESTURE only; Jesus unmarked and steady.",
        "scene": (
            "The capitulation takes one "
            "small gesture: Pilate turning "
            "from the rail with a flat "
            "backhanded wave toward the "
            "bound prisoner — take him — "
            "the man holding every sword "
            "in the province folding to "
            "plain noise, his own no-case "
            "verdict still hanging in the "
            "cold air — while Jesus "
            "receives the little wave that "
            "outweighs the world with the "
            "same calm he brought up the "
            "steps. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r093-b12", "out": "s12-so-the-guilty-man-walked.jpeg", "seg": "n3",
        "window": "60.41-65.01", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PAVEMENT", "BARABBAS"],
        "narration": (
            "So the guilty man walked free, and the innocent one was handed "
            "over in his place."
        ),
        "must_show": "SCRIPTURE-EXACT: the swap — both motions in one frame: Barabbas's chains being struck off as he stumbles free down the steps, Jesus led the other way under escort; the exchange visible.",
        "must_not_show": "ABSOLUTE: no wounds on Jesus, escort by rope and guard only; Barabbas's freedom STUNNED, not gloating.",
        "scene": (
            "One frame holds the whole "
            "swap: at the steps a guard's "
            "hammer knocks the chains off "
            "Barabbas's wrists and the "
            "big man stumbles down into "
            "the crowd hardly believing "
            "his own feet — while across "
            "the platform, the other way, "
            "the innocent one is led off "
            "under rope and escort toward "
            "the praetorium's dark door — "
            "two men passing out of the "
            "same morning through "
            "opposite gates, wearing each "
            "other's verdicts. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r093-b13", "out": "s13-think-about-what-barabbas-got.jpeg", "seg": "n4",
        "window": "65.65-71.32", "wide": False, "jesus": False, "ref": False,
        "locks": ["BARABBAS"],
        "narration": (
            "Think about what Barabbas got: he was condemned, and then "
            "someone else took his exact sentence."
        ),
        "must_show": "the received grace — close on Barabbas in the street: staring at his own freed wrists, the chain-marks still on them; a condemned man doing the math of his morning.",
        "must_not_show": "no halo, glare or rim-light; the wonder HUMAN — a hard face genuinely undone by unearned release.",
        "scene": (
            "Close on the freed man "
            "failing to understand his own "
            "hands: Barabbas in the "
            "street, staring at his freed "
            "wrists where the chain-marks "
            "still press red — a man who "
            "woke condemned, rehearsing "
            "his own execution, now "
            "standing unowned in the "
            "morning traffic while "
            "somewhere behind him another "
            "man walks under his exact "
            "sentence — the hard scarred "
            "face undone entirely by "
            "arithmetic. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r093-b14", "out": "s14-he-walked-out-free-because.jpeg", "seg": "n4 + n5",
        "window": "71.32-77.04", "wide": True, "jesus": False, "ref": False,
        "locks": ["BARABBAS"],
        "narration": (
            "He walked out free because Jesus took his cross. That's not "
            "just Barabbas's story."
        ),
        "must_show": "the freedom walked — Barabbas moving off down the waking street into ordinary life, looking back once over his shoulder toward the praetorium; the not-just-his hanging in the look.",
        "must_not_show": "no halo, glare or rim-light; the look back WEIGHTED — the free man knowing exactly who is paying.",
        "scene": (
            "Down the waking street the "
            "freed man walks into an "
            "ordinary day he did nothing "
            "to deserve — market stalls "
            "opening, children underfoot, "
            "the world handed back whole — "
            "and at the corner he stops "
            "and looks back once at the "
            "praetorium's walls, the whole "
            "trade legible in his heavy "
            "face: somebody is in there "
            "carrying mine — a look every "
            "reader of this story is "
            "meant to recognise from the "
            "inside. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r093-b15", "out": "s15-the-whole-gospel-in-one.jpeg", "seg": "n5",
        "window": "77.04-83.35", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PAVEMENT", "BARABBAS"],
        "narration": (
            "That's the whole gospel in one swap — the innocent for the "
            "guilty, so the guilty could go free."
        ),
        "must_show": "the closing image — the swap held as emblem: the two diverging figures small in the cold morning — one walking free into the light, one led away bound and calm; the gospel's shape in one frame.",
        "must_not_show": "ABSOLUTE: no wounds on Jesus; the composition BALANCED — two paths, one price, the meaning in the geometry.",
        "scene": (
            "The closing frame draws the "
            "gospel as a diagram of two "
            "roads: on one side the freed "
            "man walking out small into "
            "the bright open street, "
            "unchained and undeserving — "
            "on the other the innocent "
            "one led away bound and calm "
            "toward the dark doorway, "
            "carrying the sentence that "
            "was never his — one morning, "
            "one swap, the whole good "
            "news standing in the cold "
            "light with its arms out in "
            "both directions. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
]
