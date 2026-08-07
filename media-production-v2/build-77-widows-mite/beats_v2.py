#!/usr/bin/env python3
"""V2 beat map — row 77, build-77-widows-mite (Mark 12:41-44).

COVERAGE: 16 pictures over 92.2 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 12:41-44 KJV):
  v41   "Jesus SAT over against the treasury, and BEHELD HOW the people
        cast money in" — the watching is the scene: he studies the HOW,
        not the how-much. The treasury: the Court of the Women's
        trumpet-mouthed offering chests; the rich casting in much, the
        coins' noise part of the theatre.
  v42   "a certain POOR WIDOW ... threw in TWO MITES, which make a
        farthing" — two tiny copper lepta; she says nothing; nobody
        looks up. Her dignity absolute: small, worn, unnoticed, upright.
  v43   "he CALLED unto him his disciples" — the summons: the day's most
        important thing just happened and only he saw it.
  v43-44 "this poor widow hath cast MORE IN, than ALL they ... they did
        cast in of their ABUNDANCE; but she of her WANT did cast in ALL
        THAT SHE HAD, even ALL HER LIVING." — heaven's mathematics; the
        two coins as the treasury's largest gift.

TIME OF DAY: one bright temple morning throughout — hard clean light in
the treasury court; the closing beats in the same light, re-read.

CONTENT-CARE: the widow's poverty dignified — patched, clean, upright;
the rich givers not cartooned — public generosity as custom, its
theatre observed rather than mocked.

CHANGING CONDITION (kept OUT of the locks): the coins — handfuls
ringing, then two small mites; and the noticing — nobody's, then his,
then the disciples' summoned attention.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "WIDOW": (
        "WIDOW LOCK: the widow is the same woman in every shot — about "
        "seventy, very small and thin, with a lined gentle face, "
        "far-sighted pale-brown eyes and careful slow hands. She wears "
        "mourning's DEEP CHARCOAL-BLACK dress and shawl, patched at the "
        "elbow, scrupulously clean, and worn flat sandals (never cream, "
        "never white). Her back is straight. Her face is shown clearly "
        "and with complete dignity."
    ),
    "TREASURY": (
        "TREASURY LOCK: the temple's treasury court — a paved court "
        "along a colonnade wall where THIRTEEN trumpet-mouthed bronze "
        "offering chests stand in their row, each with its flaring "
        "metal funnel throat; a low stone bench opposite where a "
        "watcher may sit; hard clean morning light. The same chests, "
        "bench and light throughout."
    ),
    "GIVERS": (
        "RICH GIVERS LOCK: the wealthy donors — fine-robed men in DEEP "
        "PLUM, DARK TEAL and NEAR-BLACK INDIGO with gold clasps and "
        "attended servants, casting handfuls of silver with practised "
        "public grace (never cream, never white). Faces shown clearly "
        "— custom and performance, not cartoons."
    ),
}

REF = True

# STALE-V1 audio-lock clear (Machine A `Dev`, 2026-08-07, Fable-5 author lane):
# v2_assemble's AUDIO LOCK gate rejected the delivery because the extract_beats
# timeline (98.846 s) ran 1.74 s longer than the V1 final m4a (97.106 s) — over the
# abs>1.0 s tolerance — while newer_mp3s=0, so it is a duration drift, not a recency
# stale. Rebuilding the track from the V1 segment mp3s makes the audio match the
# extract_beats timeline exactly, so the stills (16, present) sit on the right words.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r077-b01", "out": "s01-jesus-sat-down-across-from.jpeg", "seg": "n0",
        "window": "0.28-4.97", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TREASURY"],
        "narration": (
            "Jesus sat down across from the temple treasury and just watched "
            "people give."
        ),
        "must_show": "SCRIPTURE-EXACT: the watching post — Jesus seated on the stone bench opposite the row of trumpet-mouthed chests, still and attentive; the study begun.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the watching unhurried — a man auditing a courtyard with his eyes.",
        "scene": (
            "On the low stone bench across the paved court, the "
            "camera at his side so bench and chest-row read in "
            "profile, "
            "court Jesus sits in the hard clean "
            "morning light — still, forearms on knees, "
            "his gaze resting on the row of thirteen "
            "trumpet-mouthed bronze chests along the "
            "colonnade wall — the traffic of givers "
            "passing between him and the flaring "
            "funnels, a watcher settled in for the "
            "long study of the one thing this court "
            "was built to make visible: how people "
            "give. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r077-b02", "out": "s02-and-jesus-sat-over-against.jpeg", "seg": "s41",
        "window": "5.54-13.90", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TREASURY", "GIVERS"],
        "narration": (
            "And Jesus sat over against the treasury, and beheld how the people "
            "cast money into the treasury: and many that were rich cast in "
            "much."
        ),
        "must_show": "SCRIPTURE-EXACT: the much — a rich donor mid-cast: the handful of silver arcing into a funnel mouth, his servant with the purse behind him, the court's attention following the gift.",
        "must_not_show": "no halo, glare or rim-light; the casting graceful and PUBLIC — generosity performed with real polish.",
        "scene": (
            "At the nearest trumpet-mouth a plum-robed "
            "donor casts with practised public grace — "
            "the handful of silver arcing bright into "
            "the flaring bronze throat, his servant a "
            "step behind with the opened purse, two "
            "passers-by pausing to watch the wealth go "
            "in — a gift performed fluently at the "
            "court's centre stage, while on the far "
            "bench the seated watcher takes his quiet "
            "notes with his eyes. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r077-b03", "out": "s03-he-sat-down-facing-the.jpeg", "seg": "n1a",
        "window": "15.41-19.52", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TREASURY"],
        "narration": (
            "He sat down facing the collection boxes and watched how people put "
            "their money in."
        ),
        "must_show": "the HOW studied — close on Jesus's watching face: attention tuned past amounts to manner; an examiner of gestures.",
        "must_not_show": "no halo, glare or rim-light; the gaze's object the HOW — reading hands and faces, not counting coins.",
        "scene": (
            "Close on Jesus's face in the court's "
            "clean light: the warm eyes tracking not "
            "the silver but the hands that release "
            "it — the pause before a cast, the "
            "glance a giver throws sideways for "
            "witnesses, the wrist's flourish or its "
            "privacy — an examiner of manner, "
            "auditing the courtyard's one honest "
            "ledger: how. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r077-b04", "out": "s04-and-the-rich-came-through.jpeg", "seg": "n1a",
        "window": "19.52-22.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["TREASURY", "GIVERS"],
        "narration": "And the rich came through and put in large amounts.",
        "must_show": "the procession — the wealthy in easy sequence at the chests: one casting, one waiting his turn, servants and purses; giving as morning traffic.",
        "must_not_show": "no halo, glare or rim-light; the sequence customary — abundance flowing at its usual public rate.",
        "scene": (
            "The morning's procession moves along the "
            "chest row: a teal-robed merchant mid-"
            "cast at one funnel, an indigo elder "
            "waiting his turn with his purse-bearer, "
            "a third already leaving with the "
            "unburdened stride of duty done — silver "
            "going into bronze throats at the steady "
            "customary rate of a temple morning, "
            "abundance making its rounds. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r077-b05", "out": "s05-you-could-hear-the-coins.jpeg", "seg": "n1b",
        "window": "23.40-26.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["TREASURY"],
        "narration": "You could hear the coins land, and everyone noticed.",
        "must_show": "the sound made visible — extreme close at a trumpet mouth: a cascade of silver mid-fall into the bronze throat; the ring and rattle implied in the metal's motion.",
        "must_not_show": "no halo, glare or rim-light; the noise the gift's advertisement — bronze built to broadcast.",
        "scene": (
            "Extreme close at the flaring bronze "
            "mouth: a cascade of silver caught "
            "mid-fall into the funnel's throat — "
            "coins tumbling over each other down the "
            "metal, the whole instrument shaped "
            "exactly like what it is: a trumpet, "
            "built to make generosity audible across "
            "a courtyard — wealth announcing its own "
            "arrival in the one language every head "
            "turns for. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r077-b06", "out": "s06-and-there-came-a-certain.jpeg", "seg": "s42",
        "window": "30.60-35.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["WIDOW", "TREASURY"],
        "narration": (
            "And there came a certain poor widow, and she threw in two mites, "
            "which make a farthing."
        ),
        "must_show": "SCRIPTURE-EXACT: her arrival and gift — the small charcoal-clad widow at the chest, her two tiny coins going in; the court's traffic flowing around her unnoticing.",
        "must_not_show": "no halo, glare or rim-light; her unnoticedness the frame — the crowd's eyes elsewhere while the row's whole point occurs.",
        "scene": (
            "Through the court's flowing traffic the "
            "small widow arrives at the funnel — "
            "charcoal-black and patched-clean, "
            "straight-backed at her slow pace — and "
            "her careful hand releases two tiny "
            "copper coins into the great bronze "
            "throat — while around her the morning "
            "streams on unnoticing: the rich at "
            "their casting, the watchers watching "
            "them, and nobody's eyes but one seated "
            "pair on the largest gift the treasury "
            "will receive today. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r077-b07", "out": "s07-she-put-in-two-tiny.jpeg", "seg": "n2b",
        "window": "37.11-41.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["WIDOW"],
        "narration": (
            "She put in two tiny copper coins — together worth less than a "
            "penny."
        ),
        "must_show": "SCRIPTURE-EXACT: the mites — extreme close: the two thin worn copper lepta in her lined palm, small as buttons; everything, at its actual size.",
        "must_not_show": "no halo, glare or rim-light; the coins genuinely TINY and worn thin — poverty's smallest denomination, held like treasure.",
        "scene": (
            "Extreme close in the hard light: the "
            "widow's lined palm open with its whole "
            "fortune — two thin copper lepta, worn "
            "nearly smooth, small as buttons and "
            "green-dark with age, together worth "
            "less than one of the morning's ringing "
            "silver pieces — all the money there is, "
            "resting in a hand that has counted it "
            "many times on the way here. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r077-b08", "out": "s08-that-is-the-whole-of.jpeg", "seg": "n2b",
        "window": "41.78-44.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["WIDOW", "TREASURY"],
        "narration": "That is the whole of what Mark records about her.",
        "must_show": "the record's brevity — the widow already turning away from the chest, gift given, story over by the world's accounting; her small back in the big court.",
        "must_not_show": "no halo, glare or rim-light; the turning-away modest — no lingering, no glance for witnesses.",
        "scene": (
            "The gift given, the widow is already "
            "turning away — her small charcoal back "
            "straight in the court's bright "
            "expanse, her slow careful steps taking "
            "her toward the colonnade with no "
            "lingering at the chest, no glance "
            "around for witnesses, no residue of "
            "the transaction at all — a whole "
            "recorded life entering scripture at "
            "the length of one sentence, and "
            "leaving the stage without a bow. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r077-b09", "out": "s09-she-does-not-say-a.jpeg", "seg": "n2b",
        "window": "44.75-48.67", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WIDOW", "TREASURY", "GIVERS"],
        "narration": "She does not say a word, and nobody in that courtyard looks up.",
        "must_show": "the unnoticing wide — the whole court mid-morning: the widow's small departing figure, and every other eye aimed at wealth; ONE gaze — from the bench — following her.",
        "must_not_show": "no halo, glare or rim-light; the single tracking gaze the beat — one seated watcher against a courtyard's inattention.",
        "scene": (
            "The wide court does its unnoticing, the camera high "
            "behind the chest-row so her small departing back "
            "crosses the frame: the "
            "rich mid-cast at the funnels with "
            "their small audiences, servants "
            "counting, officials passing — every "
            "eye in the morning aimed at silver — "
            "and crossing the pavement between them "
            "all, small and already forgotten, the "
            "widow's departing figure — tracked by "
            "exactly one gaze in the courtyard: the "
            "seated man on the far bench, watching "
            "her go like the only news of the day. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r077-b10", "out": "s10-then-a-poor-widow-came.jpeg", "seg": "n2a",
        "window": "27.05-29.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["WIDOW"],
        "narration": "Then a poor widow came, small and unnoticed.",
        "must_show": "her introduction — the widow's face in the crowd's edge: gentle, lined, far-sighted eyes; dignity at its quietest volume.",
        "must_not_show": "no halo, glare or rim-light; the smallness physical only — presence complete.",
        "scene": (
            "At the crowd's bright edge the widow's "
            "face comes into its close-up: about "
            "seventy, gentle and deeply lined, the "
            "pale-brown far-sighted eyes steady "
            "under the charcoal shawl's edge — a "
            "face nobody in the court has looked at "
            "directly in years, carrying its "
            "errand toward the chests with the "
            "unhurried completeness of someone whose "
            "whole living fits in one closed hand. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r077-b11", "out": "s11-jesus-called-his-disciples-over.jpeg", "seg": "n3",
        "window": "49.26-54.28", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "JOHN", "TREASURY"],
        "narration": (
            "Jesus called his disciples over, like he had just seen the most "
            "important thing all day."
        ),
        "must_show": "SCRIPTURE-EXACT: the summons — Jesus's raised beckoning hand, the disciples hurrying over to the bench; urgency about something none of them saw.",
        "must_not_show": "no halo, glare or rim-light; the disciples scanning the court in confusion — the important thing already gone from it.",
        "scene": (
            "From the bench Jesus's hand rises in a "
            "quick beckon and the disciples come "
            "hurrying — Peter first with his brows "
            "already asking, John scanning the "
            "court for whatever it was — and finding "
            "only the ordinary morning: rich men at "
            "bronze funnels, silver ringing, "
            "nothing anywhere worth a summons — the "
            "most important thing of the day having "
            "already left by the colonnade, at a "
            "small woman's careful pace. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r077-b12", "out": "s12-verily-i-say-unto-you.jpeg", "seg": "j1",
        "window": "54.90-71.94", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "JOHN", "WIDOW", "TREASURY"],
        "narration": (
            "Verily I say unto you, That this poor widow hath cast more in, "
            "than all they which have cast into the treasury: for all they did "
            "cast in of their abundance; but she of her want did cast in all "
            "that she had, even all her living."
        ),
        "must_show": "SCRIPTURE-EXACT: the verdict — Jesus indicating the widow's distant departing figure to the gathered disciples: heaven's mathematics announced with her still in view.",
        "must_not_show": "no halo, glare or rim-light; the indication reverent — a teacher pointing out the day's true headline before it turns the corner.",
        "scene": (
            "With the disciples gathered close, the camera behind "
            "their shoulders following his pointing line, Jesus "
            "turns them bodily toward the colonnade — "
            "his hand indicating the small charcoal "
            "figure just reaching its shadowed arch — "
            "and gives the verdict while she is "
            "still in view: MORE than all of them — "
            "the fishermen's faces swinging from the "
            "ringing funnels to the tiny departing "
            "widow and back, heaven's arithmetic "
            "landing on them like a reversed "
            "ledger — the treasury's records "
            "corrected from a stone bench, just in "
            "time. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r077-b13", "out": "s13-telling-you-the-truth-he.jpeg", "seg": "n4a",
        "window": "73.41-78.95", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER"],
        "narration": (
            "I'm telling you the truth, he said — this poor widow has put in "
            "more than every one of them."
        ),
        "must_show": "the truth insisted — close on Jesus's earnest face and Peter's struggling one: the MORE genuinely meant, and genuinely hard to compute.",
        "must_not_show": "no halo, glare or rim-light; Peter's honest struggle — a fisherman's practical mind wrestling impossible arithmetic.",
        "scene": (
            "Close between the two faces: Jesus's "
            "earnest and unequivocating — the MORE "
            "meant at full literal weight — and "
            "Peter's working at it like a knot: the "
            "practical fisherman's eyes going from "
            "his teacher toward the funnels' "
            "remembered silver, the sum refusing to "
            "balance in any book he has ever kept — "
            "truth insisting, arithmetic "
            "surrendering. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r077-b14", "out": "s14-they-gave-out-of-what.jpeg", "seg": "n4a",
        "window": "78.95-81.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["GIVERS"],
        "narration": "They gave out of what they had spare.",
        "must_show": "abundance's remainder — a rich giver's purse after his gift: still fat, cords drawn on plenty; the cast silver's untouched hinterland.",
        "must_not_show": "no halo, glare or rim-light; the purse's remaining weight the measure — generosity's unfelt cost.",
        "scene": (
            "Close at a rich giver's belt as he "
            "leaves the chest: the purse settling "
            "back against his hip still visibly fat "
            "— cords drawn over a remaining plenty "
            "that hardly registers the morning's "
            "gift, coins shifting comfortably in "
            "their leather dark — the handful that "
            "rang so bright in the bronze, revealed "
            "at the hip as what it was: the spare. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r077-b15", "out": "s15-she-gave-out-of-what.jpeg", "seg": "n4a",
        "window": "81.08-86.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["WIDOW"],
        "narration": (
            "She gave out of what she did not have. Everyone else gave from "
            "what they had left over."
        ),
        "must_show": "want's remainder — the widow's hand after her gift: open, empty, nothing left in it or behind it; all-her-living, given.",
        "must_not_show": "no halo, glare or rim-light; the emptiness total and calm — her hand at peace with its nothing.",
        "scene": (
            "Close in the colonnade's shade: the "
            "widow's lined hand hanging open at her "
            "side as she walks — empty now to its "
            "creases, no purse at her waist, no "
            "second pocket, nothing behind the gift "
            "and nothing left of it — and the hand "
            "hangs easy, unclenched, at peace with "
            "its own nothing in a way no fat purse "
            "in the courtyard could purchase. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r077-b16", "out": "s16-she-gave-from-what-she.jpeg", "seg": "n4a + n4b",
        "window": "86.69-91.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["WIDOW", "TREASURY"],
        "narration": (
            "She gave from what she needed. Heaven does the math differently "
            "than we do."
        ),
        "must_show": "the closing image — the two scales in one frame: the great bronze chest with the morning's silver mass implied, and resting atop the frame's attention, the two small mites; heaven's ledger, illustrated.",
        "must_not_show": "no halo, glare or rim-light; the mites the frame's true weight — small copper outweighing bronze and silver by the only mathematics that lasts.",
        "scene": (
            "The closing frame weighs the morning: "
            "the great bronze chest standing in the "
            "hard light with the day's silver "
            "heavy inside its throat — and held in "
            "the frame's closest attention, tiny "
            "against all that metal, the two worn "
            "copper mites where they came to rest — "
            "less than a penny, and more than the "
            "treasury, by the arithmetic of the "
            "only Auditor whose books balance in "
            "love: what it cost. Every figure has "
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
    "TREASURY": "PLACE-REF/treasury.jpeg",  # build-06-two-sons v2-r006-b21 (manual)
}
# === end PLACE-PLATES ===
