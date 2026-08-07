#!/usr/bin/env python3
"""V2 beat map — row 74, build-74-woman-washed-his-feet (Luke 7:36-50).

COVERAGE: 36 pictures over 207.9 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 7:36-50 KJV):
  v36   "one of the Pharisees desired him that he would eat with him" —
        SIMON's careful respectable house; guests RECLINE, feet stretched
        away from the table (the narration teaches this; the geometry
        makes the whole scene possible).
  v37   "a woman in the city, WHICH WAS A SINNER ... brought an ALABASTER
        BOX of ointment" — HER DIGNITY IS ABSOLUTE: she is painted as a
        grieving, loving woman in modest dark clothing; her reputation
        exists ONLY in others' faces, NEVER in her dress or bearing. No
        lurid coding of any kind, ever.
  v38   "stood at his feet BEHIND him weeping, and began to wash his feet
        with TEARS, and did wipe them with the HAIRS of her head, and
        KISSED his feet, and ANOINTED them with the ointment" — each act
        its own tender beat; the loosed hair is an act of costly humility,
        painted reverent.
  v39   Simon's UNSPOKEN thought ("he spake WITHIN HIMSELF") — the
        judgment interior; his face the only text.
  v40-43 the two debtors (500/50); "Tell me therefore, which of them will
        love him most?"; Simon's careful answer.
  v44-46 "SEEST THOU THIS WOMAN?" — the turned-toward-her-speaking-to-him
        geometry; the host's omissions itemized (no water, no kiss, no
        oil) against her everything.
  v47-48 "Her sins, which are many, are forgiven; for she loved much" —
        and TO HER: "Thy sins are forgiven."
  v49-50 the table's murmur; "Thy faith hath saved thee; GO IN PEACE" —
        the final beat carries V1's HUSH: after the words, a silent
        breath on the empty jar and the open door to the night.

TIME OF DAY: one lamplit evening throughout — Simon's dining room in
warm careful lamplight; the woman's entrance from the darker courtyard;
the HUSH's open door showing deep night beyond. No other hours.

CONTENT-CARE: the woman's story-dignity is the row's law — grief, love
and courage, never shame-coding; Simon correct and cold, not a cartoon;
the anointing intimate and utterly reverent.

CHANGING CONDITION (kept OUT of the locks): the jar — sealed, opened,
poured, EMPTY; the woman's bearing — braced at entry, broken at his
feet, sent in peace, straightened; Simon's certainty — intact, cracked,
schooled.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "WOMAN": (
        "WOMAN LOCK: the woman is the same in every shot — mid-thirties, "
        "worn by a hard life but strong-featured, with deep dark eyes "
        "red-rimmed from weeping, and long dark hair bound up at her "
        "entrance, loosed at his feet. She wears MODEST dark clothing: "
        "a DEEP WINE-DARK dress and a DARK GREY shawl, plain and clean "
        "(never cream, never white; NOTHING immodest, nothing gaudy — "
        "her reputation lives in other faces, never on her). Her face "
        "is shown clearly and with complete dignity."
    ),
    "SIMON": (
        "SIMON LOCK: the host is the same man in every shot — about "
        "fifty-five, precise and spare, with a clipped grey beard, "
        "careful measuring eyes and immaculate grooming. He wears fine "
        "NEAR-BLACK INDIGO robes with a fringed shawl, exactly draped "
        "(never cream, never white). His face is shown clearly — "
        "correctness first, coldness under it, and a crack coming."
    ),
    "ROOM": (
        "DINING ROOM LOCK: Simon's careful dining room — a spotless "
        "stone-floored room with a low U-shaped table, reclining "
        "couches with the guests' FEET STRETCHED AWAY from the table, "
        "two bronze lampstands, precise appointments, and a doorway to "
        "the darker courtyard through which the uninvited may enter. "
        "The same table, couches, lamps and door throughout."
    ),
    "JAR": (
        "ALABASTER JAR LOCK: the ointment jar is the same in every "
        "shot — a small pale alabaster flask, translucent-shouldered, "
        "with a sealed narrow neck made to be broken; costly plainness. "
        "Sealed, opened, poured and empty per-beat."
    ),
}

REF = True

# AUDIO-FIX (A-auto 2026-08-06): the V1 mp4 luke-7_woman-washed-his-feet.mp4
# (171.67s, committed 2026-07-24) is STALE — all 19/19 narration mp3s are newer
# and the extract_beats timeline is 184.57s (mp4 12.9s short). Rebuild the track
# from this build's own 19 SPEAKER-LAW segment mp3s at the extract offsets
# instead of copying the stale mp4. Verified 19/19 segment-ID parity + new voices.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r074-b01", "out": "s01-a-pharisee-named-simon-invited.jpeg", "seg": "n0",
        "window": "0-3.024", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SIMON", "ROOM"],
        "narration": "A Pharisee named Simon invited Jesus to dinner.",
        "must_show": "SCRIPTURE-EXACT: the invitation kept — Jesus reclining at Simon's careful table, the host presiding with precise courtesy; a correct dinner, correctly begun.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the room's carefulness visible — everything measured, including the welcome.",
        "scene": (
            "In the spotless lamplit dining room, the camera at the "
            "side wall taking couches and host from the side, the "
            "dinner proceeds correctly: Jesus reclining "
            "at the low table among Simon's chosen "
            "guests, feet stretched away on the couch, "
            "and the precise grey-bearded host "
            "presiding from his place with measured "
            "courtesy — dishes exact, lamps trimmed, "
            "conversation at approved volume — a "
            "careful house doing a careful thing, one "
            "interruption away from mattering forever. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r074-b02", "out": "s02-it-was-a-careful-respectable.jpeg", "seg": "n0",
        "window": "3.024-7.287", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON", "ROOM"],
        "narration": (
            "It was a careful, respectable house — and it was about to be "
            "interrupted."
        ),
        "must_show": "the carefulness itemized — the room's precision close: exact settings, folded cloths, the courtyard door standing open to the dark; order, with its one unguarded entrance.",
        "must_not_show": "no halo, glare or rim-light; the open door the hinge — respectability's single permeable point.",
        "scene": (
            "Close on the room's precision: bronze "
            "dishes set at exact intervals, folded "
            "cloths squared at each place, the "
            "lampstands' flames trimmed level — and at "
            "the frame's edge, past all the order, the "
            "courtyard doorway standing open on the "
            "night's dark, curtainless and unwatched — "
            "a careful house's one unguarded entrance, "
            "about to be used. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b03", "out": "s03-a-woman-from-the-town.jpeg", "seg": "n1",
        "window": "7.287-14.838", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "SIMON", "ROOM"],
        "narration": (
            "A woman from the town — a woman everyone in that room knew by her "
            "reputation — came in uninvited."
        ),
        "must_show": "SCRIPTURE-EXACT: the entrance — the woman stepping through the courtyard door into the lamplight, braced and resolved; the ROOM's faces carrying her reputation, her own carrying only grief and courage.",
        "must_not_show": "NOTHING lurid on her, ever — modest dark dress, bound hair; the recognition happens entirely in the guests' stiffening faces.",
        "scene": (
            "Through the courtyard door, the camera at the room's "
            "far corner taking door and table from the side, the woman "
            "steps into the lamplight — modest in her "
            "wine-dark dress and grey shawl, hair "
            "bound, the alabaster flask held against "
            "her with both hands, her red-rimmed eyes "
            "fixed on one reclining figure — and the "
            "room does the recognizing for her: "
            "Simon's fork stopped mid-air, a guest's "
            "brows climbing, a whisper starting down "
            "the couch — her whole reputation present "
            "in every face but her own. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b04", "out": "s04-she-carried-an-alabaster-jar.jpeg", "seg": "n1",
        "window": "14.838-18.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "JAR"],
        "narration": "She carried an alabaster jar of costly perfume.",
        "must_show": "SCRIPTURE-EXACT: the jar — close on the pale alabaster flask in her two hands: sealed, costly, everything she has; the offering before the offering.",
        "must_not_show": "no halo, glare or rim-light; the flask's costliness quiet — translucent stone in work-worn hands.",
        "scene": (
            "Close on her two hands in the lamplight: "
            "the small pale alabaster flask held "
            "against her chest — translucent at its "
            "shoulders where the lamp comes through, "
            "the narrow neck still sealed, the stone "
            "worth more than everything else she owns "
            "together — a life's savings in perfume, "
            "carried through a hostile door by hands "
            "that have already decided. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b05", "out": "s05-she-stood-behind-him-at.jpeg", "seg": "n2",
        "window": "18.31-27.979", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "ROOM"],
        "narration": (
            "She stood behind him at his feet — guests reclined at meals like "
            "this, their feet stretched away from the table — and she was "
            "weeping."
        ),
        "must_show": "SCRIPTURE-EXACT: the position — the reclining geometry plain: Jesus's feet stretched away from the table, and the woman standing behind at them, weeping; the scene's whole mechanics visible.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the geography taught by the frame — couch, feet, her place behind; her weeping silent and shaking.",
        "scene": (
            "The reclining geometry holds the moment, the camera in "
            "profile along the couch: "
            "Jesus stretched on the couch with his "
            "feet away from the table's edge — and "
            "behind them, at the couch's foot, the "
            "woman stands with the flask clutched to "
            "her, weeping without sound, her shoulders "
            "shaking under the grey shawl, tears "
            "already falling free — the whole room's "
            "conversation dying couch by couch as the "
            "silence spreads toward the host. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r074-b06", "out": "s06-her-tears-fell-on-his.jpeg", "seg": "n2",
        "window": "27.979-29.991", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": "Her tears fell on his feet.",
        "must_show": "SCRIPTURE-EXACT: the tears — extreme close: her tears falling onto his travel-dusty feet, the drops cutting clean tracks in the dust; grief as water.",
        "must_not_show": "no halo, glare or rim-light; the dust the detail — the road's grime and her tears meeting; the host's omission already visible.",
        "scene": (
            "Extreme close at the couch's foot: her "
            "tears falling one after another onto his "
            "bare feet — the drops landing in the "
            "road's dry dust still on them and cutting "
            "small clean tracks through it — the "
            "washing no servant offered, beginning "
            "involuntarily, from a standing woman's "
            "breaking heart onto an unwashed guest's "
            "feet. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r074-b07", "out": "s07-she-wiped-them-with-her.jpeg", "seg": "n2",
        "window": "29.991-34.577", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "JAR"],
        "narration": (
            "She wiped them with her hair, kissed them, and poured out the "
            "perfume."
        ),
        "must_show": "SCRIPTURE-EXACT: the three acts — the woman kneeling now: her loosed dark hair wiping his feet, the kiss, and the flask's neck broken, the ointment pouring; humility's whole liturgy.",
        "must_not_show": "no halo, glare or rim-light; the loosed hair painted as costly humility, utterly reverent — nothing else; the pour generous and final.",
        "scene": (
            "Kneeling now at the couch's foot the "
            "woman performs her whole liturgy: the "
            "dark hair loosed from its binding and "
            "drawn like a cloth across his wet feet, "
            "her lips pressed once to the arch in a "
            "kiss of pure reverence — and the "
            "alabaster neck broken with a small snap, "
            "the ointment pouring in a thin costly "
            "stream over his feet until the room "
            "floods with its fragrance — everything "
            "she has, in three motions, at the lowest "
            "place in the room. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b08", "out": "s08-this-man-if-he-were.jpeg", "seg": "s39",
        "window": "34.577-43.285", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON"],
        "narration": (
            "This man, if he were a prophet, would have known who and what "
            "manner of woman this is that toucheth him: for she is a sinner."
        ),
        "must_show": "SCRIPTURE-EXACT: the unspoken thought — close on Simon's face THINKING it: the judgment fully legible and the lips fully closed; interior verdict, exterior correctness.",
        "must_not_show": "no halo, glare or rim-light; the mouth sealed, the eyes doing all the speaking — the thought's whole text in a look.",
        "scene": (
            "Close on Simon's precise face in the "
            "lamplight: the lips pressed correct and "
            "closed, and behind them the whole verdict "
            "running legible through the measuring "
            "eyes — the glance flicking from the "
            "kneeling woman to the untroubled guest "
            "and back, the syllogism assembling itself "
            "behind an immaculate beard — a man "
            "thinking at full volume in a silent "
            "room. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r074-b09", "out": "s09-simon-i-have-somewhat-to.jpeg", "seg": "j40",
        "window": "43.285-56.534", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON"],
        "narration": "Simon, I have somewhat to say unto thee.",
        "must_show": "SCRIPTURE-EXACT: the thought answered — Jesus's face turned to Simon, mild and direct; the host's startle at being addressed at the exact pitch of his silence.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the mildness the power — an unspoken thought being replied to by name.",
        "scene": (
            "Across the table Jesus's face turns to "
            "the host — mild, direct, and precisely "
            "timed — and Simon's startle betrays "
            "everything: the measuring eyes widening "
            "a fraction, the correct spine "
            "straightening, a man discovering that "
            "the silence he thought private has been "
            "audited — addressed, by name, at the "
            "exact pitch of what he never said. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r074-b10", "out": "s10-simon-thought-to-himself-if.jpeg", "seg": "n3",
        "window": "56.534-56.584", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SIMON", "ROOM"],
        "narration": (
            "Simon thought to himself: if this man were really a prophet, he "
            "would know what kind of woman is touching him."
        ),
        "must_show": "the triangle — the room's three points in one frame: the kneeling woman at the feet, the untroubled Jesus, and Simon's silent judgment watching both; the scene's whole logic in geometry.",
        "must_not_show": "no halo, glare or rim-light; the three attentions distinct — devotion down, peace level, judgment across.",
        "scene": (
            "One frame holds the room's triangle, the camera at the "
            "side wall so all three points read in profile: at "
            "the couch's foot the woman bent over her "
            "anointing, hair loosed, wholly given — "
            "on the couch Jesus at perfect peace "
            "under her touch, his face untroubled as "
            "morning — and across the table Simon "
            "watching both with his sealed-lipped "
            "verdict — three attentions in three "
            "directions, and only one of them "
            "correctly reading the room. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b11", "out": "s11-he-never-said-a-word.jpeg", "seg": "n3",
        "window": "56.584-56.634", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON"],
        "narration": "He never said a word of it out loud.",
        "must_show": "the silence kept — Simon's composed exterior at the table: hands folded, face correct; the verdict locked behind perfect manners.",
        "must_not_show": "no halo, glare or rim-light; the composure complete — judgment in formal dress.",
        "scene": (
            "Simon at his place, the picture of a "
            "host: hands folded precisely on the "
            "table's edge, fringed shawl squared, "
            "face arranged into attentive courtesy — "
            "every word of the verdict locked behind "
            "manners so complete they could pass any "
            "inspection except the one, at this "
            "table, currently underway. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b12", "out": "s12-master-say-on.jpeg", "seg": "s40",
        "window": "56.634-59.252", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON"],
        "narration": "Master, say on.",
        "must_show": "SCRIPTURE-EXACT: the consent — Simon's careful permission granted: a slight bow of the head, courtesy covering wariness.",
        "must_not_show": "no halo, glare or rim-light; the courtesy armored — a man granting an audience he suddenly wishes he could decline.",
        "scene": (
            "Simon inclines his head in careful "
            "permission — the slight precise bow of a "
            "man granting an audience, palms opening "
            "a measured inch — while behind the "
            "courtesy his eyes have gone watchful: a "
            "host suddenly aware that the guest he "
            "invited for examination has somehow "
            "taken the examiner's chair. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b13", "out": "s13-there-was-a-certain-creditor.jpeg", "seg": "j41",
        "window": "59.252-67.388", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "There was a certain creditor which had two debtors: the one owed "
            "five hundred pence, and the other fifty."
        ),
        "must_show": "SCRIPTURE-EXACT: the little story's props — a moneylender's table: two debt-bills side by side, one long, one short; five hundred against fifty in tally-strokes.",
        "must_not_show": "no halo, glare or rim-light; ancient tallies, no modern numerals; the disproportion visible at a glance.",
        "scene": (
            "On a moneylender's worn table two "
            "debt-bills lie side by side in lamplight: "
            "one a long scroll dense with tally-"
            "strokes running column after column — "
            "five hundred — the other a modest single "
            "row — fifty — the same seal at each foot, "
            "the same ruin implicit in both, ten times "
            "apart: the little story's whole "
            "furniture, laid out in ink. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b14", "out": "s14-and-when-they-had-nothing.jpeg", "seg": "j41",
        "window": "67.388-72.202", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "And when they had nothing to pay, he frankly forgave them both.",
        "must_show": "SCRIPTURE-EXACT: the frank forgiving — the creditor's hands tearing BOTH bills across in one motion; the two debts ending together.",
        "must_not_show": "no halo, glare or rim-light; both torn in ONE act — the frankness the beat; no ceremony, no conditions.",
        "scene": (
            "Over the lender's table two strong "
            "hands tear both bills across in a single "
            "unceremonious motion — the long scroll "
            "and the short one ripped together, the "
            "halves dropping to the boards — five "
            "hundred and fifty cancelled in the same "
            "second by the same frank decision, with "
            "no speech attached and nothing asked "
            "back. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r074-b15", "out": "s15-tell-me-therefore-which-of.jpeg", "seg": "j41",
        "window": "72.202-76.183", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON"],
        "narration": "Tell me therefore, which of them will love him most?",
        "must_show": "SCRIPTURE-EXACT: the question aimed — Jesus's mild face putting it to Simon; the trap's door open and courteous.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the mildness merciless — a question with only one exit.",
        "scene": (
            "Across the lamplit table Jesus puts the "
            "question to his host — face mild, tone "
            "visible in its gentleness, one eyebrow "
            "slightly raised in genuine invitation — "
            "the little story's single courteous "
            "door standing open before Simon, who "
            "can already see, from where he "
            "reclines, exactly what room it opens "
            "into. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r074-b16", "out": "s16-i-suppose-that-he-to.jpeg", "seg": "s43",
        "window": "76.183-80.473", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON"],
        "narration": "I suppose that he, to whom he forgave most.",
        "must_show": "SCRIPTURE-EXACT: the careful answer — Simon answering with visible reluctance: the 'I suppose' in his hedging face; correctness walking into its own conclusion.",
        "must_not_show": "no halo, glare or rim-light; the hedge the beat — a right answer given at arm's length.",
        "scene": (
            "Simon gives the answer the way men hand "
            "over contraband — slowly, at arm's "
            "length, the 'I suppose' visible in his "
            "hedging brows and half-turned head — a "
            "trained mind seeing the conclusion three "
            "moves away and finding no honest path "
            "around it, surrendering the point with "
            "all the enthusiasm of a man signing his "
            "own audit. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b17", "out": "s17-jesus-answered-the-thought-simon.jpeg", "seg": "n4",
        "window": "80.473-86.461", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON"],
        "narration": (
            "Jesus answered the thought Simon never said out loud — with a "
            "small story."
        ),
        "must_show": "the method named — the two faces across the table: the story-teller's gentle precision meeting the thinker's dawning exposure.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the exposure gradual — Simon realizing his silence was never private.",
        "scene": (
            "The two faces hold across the lamplit "
            "table: Jesus's carrying the story's "
            "gentle precision, unhurried as a "
            "craftsman's measuring — and Simon's "
            "undergoing its slow exposure, the "
            "correct features loosening degree by "
            "degree as the arithmetic closes in — a "
            "private thought being answered so "
            "courteously its owner cannot even "
            "protest the trespass. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b18", "out": "s18-two-men-were-in-debt.jpeg", "seg": "n4",
        "window": "86.461-88.1", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Two men were in debt.",
        "must_show": "the two debtors — a simple vignette: two men waiting at the lender's door, one grey with the weight of much, one uneasy with little; debt in two sizes.",
        "must_not_show": "no halo, glare or rim-light; both men sympathetic — the sizes differ, the helplessness doesn't.",
        "scene": (
            "At the moneylender's door two debtors "
            "wait in the same worn light: one aged "
            "grey and stooped under the weight of "
            "his five hundred, hat crushed in both "
            "hands — the other young and fidgeting "
            "over his fifty, shifting foot to foot — "
            "two different sizes of the same "
            "helplessness, standing in the same "
            "line, owing what neither can pay. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r074-b19", "out": "s19-one-owed-ten-times-what.jpeg", "seg": "n4",
        "window": "88.1-96.21", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "One owed ten times what the other did, and neither of them could "
            "pay a penny of it, so the lender wiped out both debts."
        ),
        "must_show": "the wiping out received — the two debtors' faces at the tearing: the heavy one's disbelieving collapse into joy, the light one's quick relief; forgiveness landing at two depths.",
        "must_not_show": "no halo, glare or rim-light; the two joys visibly different SIZES — the row's whole doctrine previewed in two faces.",
        "scene": (
            "At the lender's table the tearing lands "
            "at two depths: the grey heavy debtor "
            "gone to his knees with both hands over "
            "his face, shoulders heaving — and the "
            "young light one grinning his quick "
            "relief, already straightening his coat — "
            "the same mercy, received by a drowning "
            "man and a splashed one, in the same "
            "second, at very different depths. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r074-b20", "out": "s20-which-one-will-love-him.jpeg", "seg": "n4",
        "window": "96.21-97.962", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Which one will love him more?",
        "must_show": "the answer visible — the heavy debtor gripping the lender's hand in both of his, forehead bowed to it; love already answering the question.",
        "must_not_show": "no halo, glare or rim-light; gratitude at its full depth — the question answered before anyone speaks.",
        "scene": (
            "At the table the answer performs "
            "itself: the grey debtor gripping the "
            "lender's hand in both of his own, his "
            "forehead bowed down onto the knuckles, "
            "tears falling on the torn halves of his "
            "five hundred — while the fifty's owner "
            "waves cheerfully from the door, already "
            "leaving — the question's whole answer, "
            "visible from across any room. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r074-b21", "out": "s21-and-he-was-right-he.jpeg", "seg": "n4",
        "window": "97.962-107.777", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "SIMON", "ROOM"],
        "narration": (
            "And he was right — he just had not noticed he was talking about "
            "the woman on the floor."
        ),
        "must_show": "the unnoticed connection — Simon's correct answer still on his face, and beyond his shoulder, in his own line of sight, the kneeling woman: the story's answer, in the room.",
        "must_not_show": "no halo, glare or rim-light; the composition's joke gentle — the answer and its illustration in one glance he hasn't taken.",
        "scene": (
            "Simon holds his correct answer like a "
            "man holding a receipt — and past his "
            "own shoulder, exactly in the line his "
            "eyes refuse, the woman kneels at the "
            "couch's foot with the empty flask "
            "beside her and her hair loosed over "
            "the anointed feet — the five-hundred "
            "debtor of his own supposing, three "
            "couches away, demonstrating his answer "
            "while he looks anywhere else. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r074-b22", "out": "s22-seest-thou-this-woman.jpeg", "seg": "j44",
        "window": "107.777-110.828", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SIMON", "ROOM"],
        "narration": "Seest thou this woman?",
        "must_show": "SCRIPTURE-EXACT: the turn — Jesus turned bodily TOWARD the woman while his words go to Simon: the geometry of the verse exact; Simon made to look.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the double direction the beat — face to her, question to him.",
        "scene": (
            "Jesus turns on the couch — bodily, fully, "
            "toward the kneeling woman — while his "
            "question travels the other way to the "
            "host: SEEST THOU THIS WOMAN — and the "
            "room's every eye is dragged with his "
            "turning to the person it has spent the "
            "whole evening looking around — Simon "
            "compelled at last to aim his correct "
            "eyes at the floor he filed her under. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r074-b23", "out": "s23-i-entered-into-thine-house.jpeg", "seg": "j44",
        "window": "110.828-120.564", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SIMON", "ROOM"],
        "narration": (
            "I entered into thine house, thou gavest me no water for my feet: "
            "but she hath washed my feet with tears, and wiped them with the "
            "hairs of her head."
        ),
        "must_show": "SCRIPTURE-EXACT: the audit — the itemized contrast in one frame: the dry unused foot-basin by the door, and the woman's tear-washed work at the couch; omission and devotion side by side.",
        "must_not_show": "no halo, glare or rim-light; the empty basin the evidence — hospitality's checklist, graded in view of the whole table.",
        "scene": (
            "The audit hangs visible in the room, the camera from "
            "the side holding both its poles: by "
            "the entrance the guest-basin stands dry "
            "and unused where no servant brought "
            "water, the folded towel still squared "
            "on its rim — and across the room at the "
            "couch's foot, the woman's finished work: "
            "the feet washed with tears and dried "
            "with loosed hair, the empty flask lying "
            "on its side — a host's omission and a "
            "sinner's liturgy, entered side by side "
            "into the evening's record. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b24", "out": "s24-simon-gave-the-only-answer.jpeg", "seg": "n4",
        "window": "120.564-120.614", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON"],
        "narration": (
            "Simon gave the only answer there was: the one who was forgiven "
            "more."
        ),
        "must_show": "the concession — Simon's face completing the answer: the reluctance and the rightness together; a careful man cornered by arithmetic.",
        "must_not_show": "no halo, glare or rim-light; the cornering courteous — he was walked here, and knows it.",
        "scene": (
            "Close on Simon's face at the "
            "concession's end: the answer given "
            "whole, the reluctance still draining "
            "from the careful features — and "
            "underneath both, arriving like weather, "
            "the first suspicion of where this "
            "courteous little story has walked him: "
            "a man checking the door of a room he "
            "has just been reasoned into. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r074-b25", "out": "s25-then-he-turned-toward-the.jpeg", "seg": "n5",
        "window": "120.614-124.945", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": "Then he turned toward the woman — but kept talking to Simon.",
        "must_show": "the facing — close: Jesus's face fully toward the woman now, honouring her with his attention while his words still travel past her; her first received look of the evening.",
        "must_not_show": "no halo, glare or rim-light on Jesus; HER receiving of the look the beat — seen, at last, by the room's one seeing person.",
        "scene": (
            "Close between the two faces: Jesus's "
            "turned fully to the kneeling woman — the "
            "first face all evening to point itself "
            "AT her rather than around her — and "
            "hers rising slowly to the unfamiliar "
            "sensation of being looked at without "
            "verdict: red-rimmed eyes lifting, "
            "hardly daring, into an attention that "
            "holds nothing but honour. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b26", "out": "s26-look-at-her-he-said.jpeg", "seg": "n5",
        "window": "124.945-126.444", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SIMON", "ROOM"],
        "narration": "Look at her, he said.",
        "must_show": "the command to see — the whole table's eyes redirected onto the woman by his word: she at the centre of attention for the first time as an honour, not a scandal.",
        "must_not_show": "no halo, glare or rim-light; the redirection total — a room full of gazes, changed in kind by one instruction.",
        "scene": (
            "At his word the whole room looks — "
            "every face down both arms of the table "
            "turned onto the kneeling woman at once — "
            "but the instruction has changed the "
            "looking's kind: where the evening's "
            "glances slid and judged, these are made "
            "to SEE — the loosed hair, the spent "
            "flask, the finished devotion — a scandal "
            "being republished, by its witness, as "
            "an example. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b27", "out": "s27-she-has-done-nothing-else.jpeg", "seg": "n5",
        "window": "126.444-135.519", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "She has done nothing else since she came in.",
        "must_show": "the constancy — the woman still at her devotion: unchanged, unbroken through everything said above her; love that never once looked up to check the room.",
        "must_not_show": "no halo, glare or rim-light; her focus absolute — the debate irrelevant to her worship.",
        "scene": (
            "Through everything said above her the "
            "woman has not moved from her devotion: "
            "still kneeling at the couch's foot, "
            "still bent over the anointed feet, her "
            "loosed hair fallen forward, one hand "
            "resting light as breath on the arch — a "
            "love that has not once looked up to "
            "check the room's opinion, because it "
            "did not come for the room. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b28", "out": "s28-her-sins-which-are-many.jpeg", "seg": "j1",
        "window": "135.519-145.074", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SIMON", "ROOM"],
        "narration": (
            "Her sins, which are many, are forgiven; for she loved much: but to "
            "whom little is forgiven, the same loveth little."
        ),
        "must_show": "SCRIPTURE-EXACT: the verdict published — Jesus speaking it over the woman to the whole table: her many-and-forgiven read aloud as her honour; Simon's little-loving named without cruelty.",
        "must_not_show": "no halo, glare or rim-light on Jesus; both halves gentle — her acquittal glorious, his diagnosis kind.",
        "scene": (
            "Over the kneeling woman the verdict "
            "goes out to the whole listening table: "
            "her many sins and their full forgiveness "
            "published in one breath as the reason "
            "for the room's most beautiful hour — "
            "her shoulders beginning to shake again "
            "at the words, differently now — while "
            "down the table the diagnosis's second "
            "half settles onto the host's correct "
            "face like dust onto polish. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r074-b29", "out": "s29-when-i-walked-into-your.jpeg", "seg": "n5",
        "window": "145.074-145.124", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON", "ROOM"],
        "narration": (
            "When I walked into your house, you offered me no water for my "
            "feet, no welcome, no oil."
        ),
        "must_show": "the omissions itemized — the three absences as still-life: the dry basin, the ungreeted threshold, the stoppered oil cruet on its shelf; hospitality's untouched instruments.",
        "must_not_show": "no halo, glare or rim-light; the three items each legible — an indictment in household objects.",
        "scene": (
            "The evening's three omissions stand "
            "where they were left: the guest-basin "
            "dry by the door with its squared towel, "
            "the threshold stone unattended where no "
            "kiss of welcome was given, and on its "
            "shelf the little oil cruet still "
            "stoppered, its anointing unpoured — "
            "three small courtesies, cheap as water, "
            "withheld in a house that measured "
            "everything except its own warmth. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r074-b30", "out": "s30-her-sins-are-many-he.jpeg", "seg": "n5b",
        "window": "145.124-149.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": (
            "Her sins are many, he said, and they are forgiven — and that is "
            "exactly why she loves like this."
        ),
        "must_show": "love's mechanism — the woman's tear-bright face lifted at last: forgiveness and love visibly the same current in her; the doctrine as a face.",
        "must_not_show": "no halo, glare or rim-light; the joy breaking through grief — much-forgiven, much-loving, one expression.",
        "scene": (
            "The woman's face lifts at last into "
            "the lamplight — tear-bright, "
            "grief-worn, and breaking open with "
            "something the evening has no other "
            "word for than joy: the much-forgiven "
            "loving much, the whole doctrine "
            "running as one visible current up "
            "through a face that came in braced for "
            "scorn and is leaving with a verdict of "
            "honour. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r074-b31", "out": "s31-the-one-who-thinks-he.jpeg", "seg": "n5b",
        "window": "149.97-152.297", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON"],
        "narration": "The one who thinks he has been forgiven little, loves little.",
        "must_show": "the mirror held — Simon's face receiving the diagnosis: little-loving traced to little-forgiveness-believed; the crack in the correctness finally visible.",
        "must_not_show": "no halo, glare or rim-light; the crack small and real — self-knowledge beginning at dinner.",
        "scene": (
            "Close on Simon's face as the mirror "
            "arrives: the measuring eyes gone "
            "inward for the first time all evening, "
            "the correct features holding a "
            "hairline crack — a man hearing his own "
            "thin love traced back to its source in "
            "the small forgiveness he ever believed "
            "he needed, and finding, behind his "
            "immaculate ledger, an unexamined debt. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r074-b32", "out": "s32-simon-had-been-sitting-there.jpeg", "seg": "n5b",
        "window": "152.297-155.091", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "SIMON", "ROOM"],
        "narration": (
            "Simon had been sitting there the whole meal, certain he was the "
            "clean one."
        ),
        "must_show": "the reversal wide — the room re-read: the woman at the couch now the evening's honoured figure, and Simon at his correct place its poorest; positions traded without anyone moving.",
        "must_not_show": "no halo, glare or rim-light; the reversal compositional — same seats, changed standings.",
        "scene": (
            "The room re-reads itself in the "
            "lamplight: at the couch's foot the "
            "woman kneels crowned by the evening's "
            "verdict, the honoured figure of the "
            "house — and at the table's best place "
            "the host sits suddenly poorest in the "
            "room, his cleanness revealed as the "
            "only empty vessel present — every seat "
            "exactly where it was, and every "
            "standing traded. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b33", "out": "s33-thy-sins-are-forgiven.jpeg", "seg": "j2",
        "window": "155.091-157.893", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": "Thy sins are forgiven.",
        "must_show": "SCRIPTURE-EXACT: the absolution TO HER — the words given directly into the woman's lifted face; the evening's whole freight in three words, first-person addressed.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the address direct — her name-less absolution, delivered eye to eye.",
        "scene": (
            "Eye to eye at last: Jesus gives the "
            "three words directly into the woman's "
            "lifted face — not over her to the "
            "table, not about her to the host, but "
            "TO her, first-person, at the distance "
            "of family — and the words land the way "
            "keys land in a lock that has waited "
            "years: her eyes closing, her whole "
            "kneeling frame going quiet around the "
            "absolution. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b34", "out": "s34-who-is-this-that-forgiveth.jpeg", "seg": "s49 + n6",
        "window": "157.893-162.504", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM"],
        "narration": (
            "Who is this that forgiveth sins also? The table stirred — who is "
            "this, who even forgives sins?"
        ),
        "must_show": "SCRIPTURE-EXACT: the stir — the table's guests leaning to each other in scandalized murmur; the question moving couch to couch while the frame's edge holds the untroubled centre.",
        "must_not_show": "no halo, glare or rim-light; the murmur's energy real — theology cracking open over dinner.",
        "scene": (
            "The table stirs down both arms: guests "
            "leaning head to head in urgent murmur, "
            "a hand covering a mouth, an elder's "
            "brows at his hairline, the question "
            "running couch to couch like spilled "
            "water — WHO IS THIS — while at the "
            "frame's calm edge the answer reclines "
            "untroubled, still looking at the "
            "forgiven woman, letting the room ask "
            "itself toward the only conclusion "
            "available. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r074-b35", "out": "s35-he-did-not-answer-them.jpeg", "seg": "n6",
        "window": "162.504-169.584", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": "He did not answer them. He was still looking at her.",
        "must_show": "the priority — the murmur ignored: Jesus's attention entirely on the woman while the theology-storm runs behind him; one person outweighing a room.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the ignoring gentle and total — his focus the sermon.",
        "scene": (
            "Behind him the murmur runs its "
            "scandalized circuit — and none of it "
            "reaches him: Jesus's whole attention "
            "rests on the kneeling woman as if the "
            "table had emptied, his face unhurried "
            "and unfinished with her — a room's "
            "worth of urgent theology outweighed, "
            "publicly and without apology, by one "
            "forgiven person still being seen. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r074-b36", "out": "s36-thy-faith-hath-saved-thee.jpeg", "seg": "j3 + HUSH",
        "window": "169.584-176.738", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "ROOM", "JAR"],
        "narration": "Thy faith hath saved thee; go in peace.",
        "must_show": "SCRIPTURE-EXACT + the HUSH: the sending — the woman risen and turning to go through the courtyard door, straighter than she entered; and the held silent breath after: the EMPTY jar on the floor, the open door to the night.",
        "must_not_show": "no halo, glare or rim-light; the HUSH honoured — the final composition resting on the spent flask and the dark open doorway; peace as exit and stillness.",
        "scene": (
            "The sending and the hush share the "
            "frame: the woman risen and moving "
            "toward the courtyard door — shawl "
            "gathered, spine straighter than the "
            "one she entered with, going in the "
            "peace she was given — and behind her "
            "on the lamplit floor the evening's two "
            "quiet monuments hold the silence: the "
            "empty alabaster jar on its side, spent "
            "to the last drop, and the open door's "
            "deep night receiving her — a saved "
            "woman walking out, and the room's "
            "held breath after. Every figure has "
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
}
# === end PLACE-PLATES ===
