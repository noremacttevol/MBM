#!/usr/bin/env python3
"""V2 beat map — row 81, build-81-render-unto-caesar (Mark 12:13-17).

COVERAGE: 16 pictures over 91.3 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 12:13-17 KJV):
  v13   "they send unto him certain of the PHARISEES and of the
        HERODIANS, to CATCH HIM IN HIS WORDS" — a mixed delegation,
        enemies allied for one trap; temple week, temple courts.
  v14   the flattery first: "Master, we know that thou art true..." —
        then the trap: "Is it lawful to give tribute to Caesar, or
        not? Shall we give, or shall we not give?"
  v15   "he, KNOWING THEIR HYPOCRISY, said... Why tempt ye me? BRING
        ME A PENNY, that I may see it." — he does not carry the coin;
        THEY produce it.
  v16   "And they brought it. And he saith unto them, Whose is this
        IMAGE and SUPERSCRIPTION? And they said unto him, Caesar's."
        — a silver denarius: stamped profile head, lettering round
        the rim.
  v17   "Render to Caesar the things that are Caesar's, and to God
        the things that are God's. And they MARVELLED at him."

FRAME-STAGING: a temple-court confrontation row — DISTINCT from the
widow's-mite treasury (row 77) and other temple rows: staged along a
sunlit colonnade with the trap-delegation as the moving piece, no
offering chests in frame.

TIME OF DAY: one bright temple-week morning throughout — hard clear
light in the colonnaded court.

CONTENT-CARE: no flags. The questioners are painted sharp but human —
schemers, not cartoons; the closing beats carry the turn from trap to
truth: the image on the coin, the image on the man.

CHANGING CONDITION (kept OUT of the locks): the coin — absent, then
demanded, then produced, then held high; and the delegation's manner —
oiled flattery, then cornered silence, then marvelling.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "COURT": (
        "COURT LOCK: a sunlit temple court along a great colonnade — "
        "massive pale limestone columns, wide worn paving, deep shade "
        "under the portico, hard clear morning light. The same "
        "columns and paving throughout."
    ),
    "OFFICIALS": (
        "OFFICIALS LOCK: the trap-delegation — Pharisees in DEEP "
        "CHARCOAL and DARK SLATE-BLUE robes with broad fringes, and "
        "smoother court men in DARK WINE-RED with fine belts (never "
        "cream, never white); sharp watchful faces, human not "
        "cartooned."
    ),
    "COIN": (
        "COIN LOCK: the tribute coin is one small SILVER DENARIUS — a "
        "stamped emperor's profile head on its face and a ring of "
        "Latin lettering round the rim; the same worn silver piece "
        "whenever a coin is shown."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r081-b01", "out": "s01-some-officials-came-to-jesus.jpeg", "seg": "n0",
        "window": "0.28-6.69", "wide": True, "jesus": True, "ref": REF,
        "locks": ["COURT", "OFFICIALS"],
        "narration": (
            "Some officials came to Jesus with a question built to trap him — "
            "flattering him first, so he'd let his guard down."
        ),
        "must_show": "SCRIPTURE-EXACT: the delegation arriving — the mixed group of dark-robed officials converging on Jesus in the sunlit court, smiles arranged on their faces, the trap walking in dressed as respect.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the smiles VISIBLY arranged — courtesy worn like a tool.",
        "scene": (
            "Across the wide sunlit paving the "
            "delegation converges on Jesus — "
            "charcoal and slate-blue fringes "
            "beside smooth wine-red court robes, "
            "an alliance that agrees on nothing "
            "except this errand — their smiles "
            "already arranged, their bows "
            "already measured, respect worn the "
            "way a snare wears grass — while "
            "Jesus stands in the hard clear "
            "light and watches them arrive. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r081-b02", "out": "s02-say-yes-and-the-crowd.jpeg", "seg": "n1",
        "window": "27.76-30.16", "wide": True, "jesus": False, "ref": False,
        "locks": ["COURT"],
        "narration": "Say yes, and the crowd turns on you.",
        "must_show": "the first jaw of the trap — the listening crowd's faces hardening at the thought: taxed men, Rome-weary, ready to turn; the danger on the YES side.",
        "must_not_show": "no halo, glare or rim-light; anger banked, not rioting — jaws set, eyes narrowed, a crowd's love one word from curdling.",
        "scene": (
            "The listening crowd fills the "
            "colonnade's edge — farmers and "
            "tradesmen who count Rome's tax out "
            "of thin purses every season — and "
            "across their faces the first jaw "
            "of the trap gleams: jaws setting, "
            "eyes narrowing, shoulders squaring "
            "at the mere hovering of a YES — a "
            "crowd's devotion standing one "
            "word from turning, and every "
            "schemer in the court counting on "
            "it. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r081-b03", "out": "s03-master-we-know-that-thou.jpeg", "seg": "s14",
        "window": "7.37-20.18", "wide": True, "jesus": True, "ref": REF,
        "locks": ["COURT", "OFFICIALS"],
        "narration": (
            "Master, we know that thou art true, and carest for no man: for "
            "thou regardest not the person of men, but teachest the way of "
            "God in truth: Is it lawful to give tribute to Caesar, or not?"
        ),
        "must_show": "SCRIPTURE-EXACT: the flattery delivered — the lead official bowing low before Jesus, palms spread in oiled praise, the others fanned behind; honey poured before the hook.",
        "must_not_show": "no halo, glare or rim-light; the bow TOO deep, the praise TOO polished — hypocrisy legible in the performance.",
        "scene": (
            "The lead official bows a shade too "
            "deep in the hard light — palms "
            "spread, voice-oil almost visible in "
            "the air — MASTER, WE KNOW THOU ART "
            "TRUE — the praise laid down thick "
            "as paving while the rest fan out "
            "behind him with lawyers' patience, "
            "and the hook glints at the honey's "
            "end: is it LAWFUL — the word "
            "chosen the way a hunter chooses "
            "ground. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r081-b04", "out": "s04-shall-we-give-or-shall.jpeg", "seg": "s14",
        "window": "20.18-23.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["OFFICIALS"],
        "narration": "Shall we give, or shall we not give?",
        "must_show": "the fork pressed — close on the questioner's face: brows up in mock sincerity, the either-or held out like two closing doors.",
        "must_not_show": "no halo, glare or rim-light; the mock sincerity readable — a man offering two doors and owning both.",
        "scene": (
            "Close on the questioner's face at "
            "the moment the fork is pressed: "
            "brows lifted in beautifully "
            "manufactured sincerity, head "
            "tilted, hands opening to either "
            "side as if honestly weighing — "
            "shall we GIVE, shall we NOT — two "
            "doors held courteously open by a "
            "man who has personally locked "
            "whatever lies behind both of them. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r081-b05", "out": "s05-is-it-lawful-to-pay.jpeg", "seg": "n1",
        "window": "24.68-27.76", "wide": True, "jesus": True, "ref": REF,
        "locks": ["COURT", "OFFICIALS"],
        "narration": "Is it lawful to pay taxes to Caesar, or not?",
        "must_show": "the trap sprung open — the whole tableau: questioners waiting, crowd leaning in, Jesus at the centre of the silence the question made.",
        "must_not_show": "no halo, glare or rim-light; the SILENCE the subject — every face in the court stopped on him.",
        "scene": (
            "The question hangs and the whole "
            "court stops around it: the "
            "delegation motionless with their "
            "patience out like knives, the "
            "crowd's lean frozen mid-lean, even "
            "the pigeons on the architrave "
            "seeming to hold — and at the "
            "centre of all that aimed silence "
            "Jesus stands unhurried in the "
            "clear light, the only person "
            "present not waiting for his own "
            "answer. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r081-b06", "out": "s06-say-no-and-rome-arrests.jpeg", "seg": "n1",
        "window": "30.16-34.85", "wide": True, "jesus": False, "ref": False,
        "locks": ["COURT"],
        "narration": "Say no, and Rome arrests you. There was no safe answer.",
        "must_show": "the second jaw — at the court's far edge, a pair of Roman soldiers in dark iron and leather standing their watch; the NO side's consequence, present and armed.",
        "must_not_show": "no halo, glare or rim-light; the soldiers at their ordinary watch — menace by presence, no drawn weapons, no violence.",
        "scene": (
            "At the court's far edge, framed "
            "small between two limestone "
            "columns, the second jaw of the "
            "trap stands its ordinary watch: a "
            "pair of Roman soldiers in dark "
            "iron and oxblood leather, spears "
            "grounded, bored and permanent — "
            "the empire's answer to every NO "
            "ever spoken in this province, "
            "requiring nothing today but to be "
            "visible from where the question "
            "was asked. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r081-b07", "out": "s07-jesus-saw-straight-through-it.jpeg", "seg": "n2 + s15",
        "window": "35.45-40.86", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OFFICIALS"],
        "narration": (
            "Jesus saw straight through it. But he, knowing their hypocrisy, "
            "said unto them,"
        ),
        "must_show": "SCRIPTURE-EXACT: knowing their hypocrisy — close on Jesus's level, unfooled gaze meeting the lead questioner's; the flattery dead on arrival.",
        "must_not_show": "no halo, glare or rim-light; NO anger on Jesus — clear-eyed knowledge, calm as arithmetic.",
        "scene": (
            "Close between the two faces: the "
            "questioner's practised sincerity "
            "still holding its shape, and "
            "Jesus's level gaze already all the "
            "way through it — no anger in the "
            "warm brown eyes, no offence, just "
            "the calm complete knowledge of a "
            "man reading a ledger held upside "
            "down by its owner — the flattery "
            "standing there, dead on arrival "
            "and not yet informed. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r081-b08", "out": "s08-why-tempt-ye-me-bring.jpeg", "seg": "j1",
        "window": "42.33-45.91", "wide": True, "jesus": True, "ref": REF,
        "locks": ["COURT", "OFFICIALS"],
        "narration": "Why tempt ye me? bring me a penny, that I may see it.",
        "must_show": "SCRIPTURE-EXACT: the counter-move — Jesus's open empty hand held out toward the delegation: BRING me a penny; the request itself the first reversal — he carries none.",
        "must_not_show": "no halo, glare or rim-light; Jesus's hand EMPTY and open — the coin must come from THEIR purse, and the officials already reaching.",
        "scene": (
            "Jesus's open hand extends into the "
            "space between them — empty, palm "
            "up, unhurried — BRING ME A PENNY — "
            "and the reversal begins in that "
            "small gesture: the man they came "
            "to trap owns no tribute coin, and "
            "already a wine-red sleeve is "
            "dipping into its own purse to "
            "supply one, the delegation funding "
            "the demonstration that will undo "
            "them. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r081-b09", "out": "s09-they-brought-one-a-small.jpeg", "seg": "n3",
        "window": "47.30-50.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["OFFICIALS", "COIN"],
        "narration": "They brought one — a small silver Roman coin.",
        "must_show": "SCRIPTURE-EXACT: the coin produced — close on the official's fingers holding out the small silver denarius; the stamped profile catching the light.",
        "must_not_show": "no halo, glare or rim-light; the coin SMALL — one worn silver piece between finger and thumb, handed over a shade reluctantly.",
        "scene": (
            "Close on the handover: the "
            "official's ringed fingers holding "
            "out the small worn denarius, the "
            "stamped emperor's profile and its "
            "rim of Latin catching the hard "
            "morning light as it crosses the "
            "gap — one little disc of silver, "
            "produced from the questioner's own "
            "purse with a shade of reluctance, "
            "as if some part of him already "
            "suspects what it is about to "
            "testify. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r081-b10", "out": "s10-he-held-it-up-where.jpeg", "seg": "n3 + j2",
        "window": "50.41-55.88", "wide": True, "jesus": True, "ref": REF,
        "locks": ["COURT", "COIN"],
        "narration": (
            "He held it up where everyone could see. Whose is this image and "
            "superscription?"
        ),
        "must_show": "SCRIPTURE-EXACT: the coin held high — Jesus lifting the denarius up in the light for the whole court, the stamped face outward; the question aimed at everyone.",
        "must_not_show": "no halo, glare or rim-light; the coin raised so the COURT sees it — a public exhibit, every eye pulled to the little silver disc.",
        "scene": (
            "Jesus lifts the little coin high "
            "into the clear light — arm up, the "
            "stamped profile turned outward for "
            "the whole court — and every eye in "
            "the colonnade converges on a disc "
            "of silver smaller than a fig: the "
            "crowd craning, the delegation "
            "stiffening, one small piece of "
            "Rome held up like evidence at "
            "trial while the question circles "
            "the court — whose image, whose "
            "name. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r081-b11", "out": "s11-and-they-said-unto-him.jpeg", "seg": "s16 + n4",
        "window": "57.30-63.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["OFFICIALS", "COIN"],
        "narration": (
            "And they said unto him, Caesar's. Whose face is this, he asked "
            "them, and whose name."
        ),
        "must_show": "SCRIPTURE-EXACT: the forced answer — close on the officials' faces conceding the word: lips shaping CAESAR'S, eyes on the raised coin, the admission dragged out by daylight.",
        "must_not_show": "no halo, glare or rim-light; the concession UNWILLING — men answering a question they suddenly wish had not been asked.",
        "scene": (
            "Close on the delegation's faces as "
            "the word is dragged out of them by "
            "plain daylight: lips shaping "
            "CAESAR'S with the enthusiasm of "
            "men signing against themselves, "
            "eyes fixed on the raised silver "
            "they supplied, each schemer "
            "hearing his own voice concede the "
            "one small fact the whole trap "
            "needed to reverse its hinges. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r081-b12", "out": "s12-they-said-it-was-and.jpeg", "seg": "n4",
        "window": "63.95-70.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["COURT", "OFFICIALS"],
        "narration": (
            "They said it was Caesar's. And with that, the trap they had "
            "built swung shut on them instead."
        ),
        "must_show": "the reversal wide — the tableau flipped: the delegation now the cornered ones, exchanging glances, feet shifting; Jesus calm at the centre with the coin.",
        "must_not_show": "no halo, glare or rim-light; NO gloating on Jesus — the reversal carried entirely by the schemers' body language.",
        "scene": (
            "The court's geometry quietly "
            "flips: the delegation that walked "
            "in as hunters now stands cornered "
            "in its own snare — sidelong "
            "glances ricocheting between them, "
            "feet shifting on the paving, the "
            "arranged smiles nowhere to be "
            "found — while Jesus stands calm at "
            "the centre with their coin in his "
            "fingers, no triumph on him at all, "
            "which somehow makes it worse. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r081-b13", "out": "s13-and-jesus-answering-said-unto.jpeg", "seg": "s17",
        "window": "70.70-73.07", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COIN"],
        "narration": "And Jesus answering said unto them,",
        "must_show": "the breath before the verdict — close on Jesus, the coin held easily between finger and thumb, the court's whole attention on his opening mouth.",
        "must_not_show": "no halo, glare or rim-light; the stillness total — the sentence everyone will quote for two thousand years, one breath away.",
        "scene": (
            "Close on Jesus in the hush before "
            "the verdict: the little denarius "
            "held easily between finger and "
            "thumb, the warm eyes moving once "
            "across the cornered questioners "
            "and the craning crowd, the breath "
            "drawn — a whole colonnade of "
            "enemies and listeners leaning "
            "into the pause before a sentence "
            "that will outlive the empire "
            "stamped on the silver. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r081-b14", "out": "s14-render-to-caesar-the-things.jpeg", "seg": "j3",
        "window": "74.50-79.24", "wide": True, "jesus": True, "ref": REF,
        "locks": ["COURT", "OFFICIALS", "COIN"],
        "narration": (
            "Render to Caesar the things that are Caesar's, and to God the "
            "things that are God's."
        ),
        "must_show": "SCRIPTURE-EXACT: the verdict — Jesus handing the coin BACK toward its owner with one hand, the other hand opening upward; both renderings in one body; the court marvelling.",
        "must_not_show": "no halo, glare or rim-light; the coin RETURNED, not kept — Caesar's silver going back to Caesar's man while the open hand points past it.",
        "scene": (
            "The verdict lands with both hands "
            "at once: one returning the little "
            "silver coin toward its owner's "
            "chest — Caesar's stamp going home "
            "to Caesar's purse — while the "
            "other opens upward, easy and "
            "unanswerable, toward everything "
            "the stamp never touched — and "
            "across the court the faces that "
            "came to catch him settle into "
            "open marvelling, the trap's iron "
            "melted into a sentence too true "
            "to argue with. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r081-b15", "out": "s15-the-coin-bore-image-so.jpeg", "seg": "n5",
        "window": "80.66-84.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["COIN", "OFFICIALS"],
        "narration": "The coin bore Caesar's image, so give it back to Caesar.",
        "must_show": "the first half of the logic — close on the coin back in the official's palm: the stamped profile face-up; the owed thing returned to its image.",
        "must_not_show": "no halo, glare or rim-light; the coin small and settled in the palm — case closed on the silver's side.",
        "scene": (
            "Close on the official's open palm "
            "with the denarius settled back in "
            "it — the stamped profile face-up "
            "in the hard light, the rim of "
            "Latin naming its owner as plainly "
            "as a signature — the first half "
            "of the logic closed and lying "
            "there: metal marked with a man's "
            "image, gone home to that man's "
            "treasury, owing nothing further "
            "to anyone. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r081-b16", "out": "s16-but-you-bear-image-so.jpeg", "seg": "n5",
        "window": "84.15-90.93", "wide": True, "jesus": False, "ref": False,
        "locks": ["COURT"],
        "narration": (
            "But you bear God's image — so the real question is what you owe "
            "to the One whose face you carry."
        ),
        "must_show": "the closing image — the court's ordinary faces wide in the clear light: crowd, questioners, soldiers, every human face in frame; the other image, everywhere you look.",
        "must_not_show": "no halo, glare or rim-light; NO text, symbol or mark on anyone — the point carried by the sheer number of human faces filling the frame.",
        "scene": (
            "The closing frame fills with faces "
            "in the clear morning light — the "
            "farmer's, the questioner's, the "
            "bored soldier's, the child's on "
            "its mother's hip, old and young "
            "and friend and schemer crowding "
            "the colonnade — every one of them "
            "stamped, rim to rim, with the "
            "image no emperor minted — the "
            "court suddenly legible as a "
            "treasury of another kind, every "
            "coin in it owed home. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
]
