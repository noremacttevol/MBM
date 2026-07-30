#!/usr/bin/env python3
"""V2 beat map — row 107, build-107-john-baptist-doubt (Matthew 11:2-11).

COVERAGE: 25 pictures over 141.3 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 11 KJV):
  v2    "when John had heard IN THE PRISON the works of Christ, he
        sent TWO of his disciples" — the forerunner in a cell,
        doubting.
  v3    "ART THOU HE THAT SHOULD COME, or do we look for another?"
  v4-5  the answer is a SCENE, not an argument: "Go and SHEW John
        again those things which ye do HEAR AND SEE: The blind
        receive their sight, and the lame walk, the lepers are
        cleansed, and the deaf hear, the dead are raised up, and the
        POOR have the gospel preached to them."
  v6    "And blessed is he, whosoever shall NOT BE OFFENDED in me."
  v7-11 the moment the messengers leave, Jesus PRAISES John to the
        crowd — defending the doubter behind his back.

CONTENT-CARE: no flags, but John's coming death is NEVER depicted or
foreshadowed visually — the cell holds waiting, not execution; his
chains plain iron, his dignity absolute. Healing beats keep full
dignity for the healed (no grotesquerie); the raised-dead clause is
carried by joy around a risen figure, nothing morbid.

TIME OF DAY: the CELL in perpetual dimness with ONE high shaft of
daylight; the Jesus/healing scenes in bright open day; the peace
beat's cell shaft warmed to gold. Correct story lighting.

CHANGING CONDITION (kept OUT of the locks): John — doubting, asking,
then at peace; the messengers — sent, witnessing, returning; the
cell's shaft of light — pale, then gold.
"""

# LOCKS: one entry per recurring person and per setting. Clothing colours
# stated POSITIVELY and dark — only Jesus wears cream.
LOCKS = {
    "CELL": (
        "CELL LOCK: the fortress prison cell — rough dark stone, a "
        "packed-earth floor with straw, heavy iron chain to a wall "
        "ring, a thick wooden door with a small grate, and ONE high "
        "narrow slit window dropping a single shaft of daylight. The "
        "same cell, ring and shaft throughout."
    ),
    "JOHNB": (
        "JOHNB LOCK: John the Baptist is the same man in every shot "
        "— about thirty-five, gaunt and weather-hardened, wild long "
        "dark hair and beard, deep burning eyes, in his rough DARK "
        "CAMEL-HAIR garment with a wide LEATHER belt (never cream, "
        "never white); iron at his wrist, dignity untouched."
    ),
    "TWO": (
        "TWO LOCK: John's two messengers are the same pair in every "
        "shot — an older lean one in DARK UMBER-BROWN and a younger "
        "broad one in DEEP SLATE-GREY (never cream, never white); "
        "loyal, road-worn, carrying their teacher's question like a "
        "weight."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r107-b01", "out": "s01-john-the-baptist-had-spent.jpeg", "seg": "n1",
        "window": "0.28-7.61", "wide": True, "jesus": False, "ref": False,
        "locks": ["JOHNB"],
        "narration": (
            "John the Baptist had spent his whole life preparing the way. "
            "He had pointed to Jesus and said, behold, the Lamb of God."
        ),
        "must_show": "the remembered height — the riverside memory: John mid-river in his strength, arm flung out pointing past the crowd; the pointer at his life's work.",
        "must_not_show": "no halo, glare or rim-light; Jesus NOT in this frame — the pointing arm and the crowd's turning heads carry him.",
        "scene": (
            "The memory stands at full "
            "strength: John thigh-deep in "
            "the brown river with the "
            "crowd banked along both "
            "banks, wild hair flying, "
            "the whole gaunt frame "
            "turned into one pointing "
            "arm flung upstream — BEHOLD "
            "— every head on both banks "
            "swinging to follow the "
            "line of it — a life spent "
            "entirely on being a "
            "signpost, at the moment "
            "of its proudest pointing. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r107-b02", "out": "s02-and-now-he-sat-in.jpeg", "seg": "n1",
        "window": "7.61-12.77", "wide": True, "jesus": False, "ref": False,
        "locks": ["CELL", "JOHNB"],
        "narration": (
            "And now he sat in a prison cell, waiting to die, and the "
            "doubts crept in."
        ),
        "must_show": "SCRIPTURE-EXACT: in the prison — the cell's dimness: John seated against the wall in his chains under the one pale shaft, the wild strength caged; doubt's weather on him.",
        "must_not_show": "no execution imagery or foreshadowing; the chains PLAIN iron; his dignity whole inside the confinement.",
        "scene": (
            "And now the signpost sits in "
            "the dark: John against the "
            "rough stone wall with the "
            "iron chain slack from his "
            "wrist to its ring, straw "
            "and shadow around him, the "
            "one narrow shaft of pale "
            "day standing in the "
            "gloom — the river's wild "
            "voice folded small in a "
            "fortress box, the burning "
            "eyes banked low, and into "
            "the long silence of "
            "waiting, quiet as damp, "
            "the doubts coming in "
            "through the stone. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r107-b03", "out": "s03-if-jesus-really-was-the.jpeg", "seg": "n2",
        "window": "13.33-17.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELL", "JOHNB"],
        "narration": (
            "If Jesus really was the promised one, why was John still in "
            "chains?"
        ),
        "must_show": "the question forming — close on John's face over the iron at his wrist: the honest arithmetic of chains versus promise working in the burning eyes.",
        "must_not_show": "no halo, glare or rim-light; the doubt HONEST — a faithful man's real question, not bitterness.",
        "scene": (
            "Close on faith doing honest "
            "arithmetic: John's deep "
            "burning eyes moving from "
            "the iron on his own wrist "
            "to the pale shaft of light "
            "and back — if he is who I "
            "said he is, then WHY is "
            "this iron still here — the "
            "question turning in the "
            "gaunt face without one "
            "grain of bitterness in it: "
            "just the aching honest "
            "math of a true man whose "
            "sums have stopped adding, "
            "in the dark. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r107-b04", "out": "s04-where-was-the-rescue-so.jpeg", "seg": "n2",
        "window": "17.94-21.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELL", "JOHNB"],
        "narration": "Where was the rescue? So he did something honest and brave.",
        "must_show": "the brave decision — John risen to his feet in the shaft's light, resolve replacing brooding: the question will be SENT, not swallowed.",
        "must_not_show": "no halo, glare or rim-light; the bravery in the CHOICE — asking out loud instead of rotting quietly.",
        "scene": (
            "The brooding ends on his "
            "feet: John up in the "
            "shaft's pale light with "
            "the chain hanging its "
            "slack, the wild head "
            "lifted, resolve setting "
            "the gaunt features — the "
            "bravest thing a doubting "
            "man can do taking shape in "
            "him: not to swallow the "
            "question and let it turn "
            "to poison in the dark, "
            "but to send it — straight, "
            "out loud, to the only one "
            "who can answer it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r107-b05", "out": "s05-he-sent-two-of-his.jpeg", "seg": "n2 + nq",
        "window": "21.89-28.97", "wide": True, "jesus": False, "ref": False,
        "locks": ["CELL", "JOHNB", "TWO"],
        "narration": (
            "He sent two of his followers to ask Jesus directly. Art thou "
            "he that should come, or do we look for another?"
        ),
        "must_show": "SCRIPTURE-EXACT: the sending — the two messengers at the cell door's grate receiving the exact question from John's lips; the errand loaded word by word.",
        "must_not_show": "no halo, glare or rim-light; the question ENTRUSTED — the two receiving it like something fragile and heavy.",
        "scene": (
            "Through the door's small "
            "iron grate the errand is "
            "loaded: John's gaunt face "
            "close to the bars, giving "
            "the two loyal shapes in "
            "the corridor his exact "
            "words — ART THOU HE THAT "
            "SHOULD COME — the older "
            "messenger's lips moving as "
            "he stores each syllable, "
            "the younger's jaw set — OR "
            "DO WE LOOK FOR ANOTHER — "
            "a lifetime's question "
            "folded into one sentence "
            "and handed through iron "
            "into two men's keeping. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r107-b06", "out": "s06-it-is-one-of-the.jpeg", "seg": "n3",
        "window": "30.51-33.31", "wide": True, "jesus": False, "ref": False,
        "locks": ["TWO"],
        "narration": "It is one of the most human questions in the whole Bible.",
        "must_show": "the question travelling — the two messengers on the long road from the fortress toward Galilee, the question's weight in their silent striding.",
        "must_not_show": "no halo, glare or rim-light; the road LONG — fortress crag behind, green country far ahead.",
        "scene": (
            "The most human question in "
            "the Book takes the road: "
            "the two messengers striding "
            "silent and grim down from "
            "the fortress crag, dark "
            "robes snapping, the dead "
            "sea's haze behind them and "
            "Galilee's far green ahead — "
            "neither man speaking, both "
            "carrying it the way you "
            "carry your father's "
            "question to the doctor: "
            "careful, dreading, "
            "needing the answer more "
            "than they can say. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r107-b07", "out": "s07-are-you-really-who-i.jpeg", "seg": "n3",
        "window": "33.31-38.81", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TWO"],
        "narration": (
            "Are you really who I hoped you were? And notice — Jesus was "
            "not offended."
        ),
        "must_show": "SCRIPTURE-EXACT: the asking — the two before Jesus amid his day's work, the question delivered; HIS face utterly unoffended — warm, receiving it gently.",
        "must_not_show": "no halo, glare or rim-light; NOT ONE line of offense on Jesus — the question honored in the hearing.",
        "scene": (
            "The question arrives at its "
            "address: the two travel-"
            "worn messengers standing "
            "before Jesus in the bright "
            "working day, the sentence "
            "delivered word for careful "
            "word — are you really he — "
            "and on the face receiving "
            "it, watched anxiously by "
            "both couriers, not one "
            "flicker of offense: no "
            "stiffening, no hurt, only "
            "a warmth that seems, "
            "impossibly, to honor the "
            "asking — doubt, handled "
            "like something precious. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r107-b08", "out": "s08-he-did-not-scold-john.jpeg", "seg": "n3 + s4a",
        "window": "38.81-44.25", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TWO"],
        "narration": (
            "He did not scold John for asking. Jesus answered and said unto "
            "them,"
        ),
        "must_show": "the answer beginning — close on Jesus turning to the two with gentle purpose, hand rising to direct their eyes outward at his work; no scolding anywhere.",
        "must_not_show": "no halo, glare or rim-light; the gesture OUTWARD — look, not listen; the answer will be shown.",
        "scene": (
            "Close on the answer choosing "
            "its form: Jesus's face "
            "gentle over the two "
            "waiting couriers, and his "
            "hand rising — not to "
            "lecture, not to defend, "
            "but to turn them bodily "
            "outward toward the bright "
            "working day behind him — "
            "the reply to a chained "
            "man's doubt beginning not "
            "with a sentence but with "
            "a direction: look — and "
            "the two turning along his "
            "arm to see. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r107-b09", "out": "s09-go-and-tell-john-what.jpeg", "seg": "n4",
        "window": "65.56-70.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TWO"],
        "narration": "Go and tell John what you see happening — right here, right now.",
        "must_show": "the commission — Jesus's hands on the two messengers' shoulders, aiming them home: eyewitnesses commissioned, the report already burning in their faces.",
        "must_not_show": "no halo, glare or rim-light; their faces CHANGED — men who came with a question, leaving with a scene.",
        "scene": (
            "The commissioning of two "
            "eyewitnesses: Jesus's hands "
            "warm on their shoulders, "
            "turning them back toward "
            "the fortress road — GO AND "
            "TELL JOHN WHAT YOU SEE — "
            "and the two faces already "
            "carrying it: eyes still "
            "full of what the morning "
            "showed them, mouths "
            "rehearsing, the grim "
            "couriers of a doubt "
            "converted into couriers "
            "of a scene too big for "
            "the sentence they brought. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r107-b10", "out": "s10-go-and-shew-john-again.jpeg", "seg": "jv4",
        "window": "45.80-61.08", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TWO"],
        "narration": (
            "Go and shew John again those things which ye do hear and see: "
            "The blind receive their sight, and the lame walk, the lepers "
            "are cleansed, and the deaf hear, the dead are raised up, and "
            "the poor have the gospel preached to them."
        ),
        "must_show": "SCRIPTURE-EXACT: the living answer — the wide working scene around Jesus: a blind man's opening eyes, a lame man mid-first-step, joy around a risen figure, poor families close and taught; the verse happening.",
        "must_not_show": "no halo, glare or rim-light; every healed person DIGNIFIED — no grotesquerie; nothing morbid at the raised-up corner.",
        "scene": (
            "The answer is a landscape "
            "at work: near Jesus a "
            "blind man's face tips "
            "into the light with his "
            "eyes flooding open and "
            "his hands flying to his "
            "own cheeks; past him a "
            "lame man takes a wobbling "
            "glorious first step off "
            "his mat into his "
            "brother's arms; further, "
            "a family weeps for joy "
            "around a young woman "
            "sitting up alive and "
            "warm; and everywhere "
            "between, the poor packed "
            "close and being taught "
            "like they matter — the "
            "whole verse, happening at "
            "once, while the two "
            "messengers stare. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r107-b11", "out": "s11-not-overthrowing-an-empire.jpeg", "seg": "n5",
        "window": "78.74-80.34", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Not overthrowing an empire.",
        "must_show": "the not-that — a distant cold glimpse of empire untouched: a Roman watchtower on its hill, eagle standard, business as usual; the revolution happening elsewhere.",
        "must_not_show": "no halo; no battle, no siege — the tower BORED and standing; the point is what is NOT being attacked.",
        "scene": (
            "The frame glances at what "
            "is not on fire: a Roman "
            "watchtower standing bored "
            "on its hill in the haze, "
            "the eagle standard "
            "unruffled, a sentry "
            "leaning on the parapet "
            "with nothing to report — "
            "the empire entirely "
            "unassaulted, its roads "
            "and taxes running on "
            "schedule — while somewhere "
            "below in the green, out "
            "of this frame's cold "
            "reach, the actual "
            "revolution is busy giving "
            "a blind man his morning. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r107-b12", "out": "s12-he-did-not-send-back.jpeg", "seg": "n4",
        "window": "62.59-65.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["TWO"],
        "narration": "He did not send back an argument. He sent back a scene.",
        "must_show": "the scene received — close on the two messengers' faces watching the healings: argument-proof wonder; eyes doing the receiving.",
        "must_not_show": "no halo, glare or rim-light; their WATCHING the picture — witnesses being filled.",
        "scene": (
            "Close on two faces being "
            "loaded with the answer: "
            "the older messenger's lean "
            "features gone soft with "
            "unguarded wonder, the "
            "younger's mouth open on a "
            "word he never finds — "
            "both pairs of eyes "
            "tracking miracle after "
            "miracle across the bright "
            "day like men trying to "
            "memorize rain — no "
            "syllogism to carry home "
            "in their satchels, just "
            "this: what they are "
            "seeing, burned in deep "
            "enough to survive the "
            "road. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r107-b13", "out": "s13-the-blind-seeing-the-broken.jpeg", "seg": "n4",
        "window": "70.53-73.55", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "The blind seeing. The broken mended.",
        "must_show": "the mending close — one healed detail full-frame: an old blind woman's just-opened eyes finding her grandchild's face for the first time; sight arriving.",
        "must_not_show": "no halo, glare or rim-light; the moment INTIMATE — one healing, fully felt.",
        "scene": (
            "One mending, close enough "
            "to feel: an old woman's "
            "eyes — milky a minute ago, "
            "clear now — finding and "
            "focusing for the first "
            "time on the small "
            "grandchild she has only "
            "ever held in the dark, "
            "her trembling hands "
            "rising to frame the little "
            "face while tears cut "
            "bright tracks down her "
            "own — the word HEALED "
            "translated into its native "
            "language: one particular "
            "person, seeing one "
            "particular beloved face. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r107-b14", "out": "s14-the-poorest-people-being-treated.jpeg", "seg": "n4",
        "window": "73.55-78.14", "wide": True, "jesus": True, "ref": REF,
        "locks": [],
        "narration": (
            "The poorest people being treated like they matter. This is "
            "what I am doing."
        ),
        "must_show": "the poor mattering — Jesus seated low among the poorest: ragged families gathered close, his full attention on them; dignity conferred by attention.",
        "must_not_show": "no halo, glare or rim-light; the poverty REAL and the welcome realer — no one held at distance.",
        "scene": (
            "The kingdom's headline act, "
            "in full: Jesus seated on "
            "the ground among the "
            "poorest of the district — "
            "patched families, a "
            "day-laborer still dusty, "
            "a widow with her two "
            "children pulled close — "
            "and his whole attention "
            "given down to them like "
            "wealth: listening to the "
            "laborer finish, laughing "
            "with the widow's youngest, "
            "nobody herded back, "
            "nobody beneath notice — "
            "the poor, being treated "
            "like the treasury. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r107-b15", "out": "s15-not-breaking-open-a-prison.jpeg", "seg": "n5",
        "window": "80.34-86.88", "wide": True, "jesus": True, "ref": REF,
        "locks": [],
        "narration": (
            "Not breaking open a prison. But healing, one by one, the "
            "people everyone else stepped over."
        ),
        "must_show": "the one-by-one — Jesus moving down a line of the stepped-over at a village edge: a beggar, a bent woman, a scarred man; each receiving him singly, in turn.",
        "must_not_show": "no halo, glare or rim-light; the LINE personal — each healing its own meeting, no crowd-blur.",
        "scene": (
            "The method shows itself in "
            "single file: along the "
            "village's low wall the "
            "stepped-over wait in their "
            "line — the beggar the "
            "street walks around, the "
            "bent woman nobody's eyes "
            "meet, the scarred man who "
            "eats alone — and Jesus "
            "working down the line one "
            "whole person at a time: "
            "kneeling to the first, "
            "both hands for the "
            "second, unhurried at each "
            "as if the line behind "
            "did not exist — no prison "
            "stormed; a hundred "
            "invisible doors opened, "
            "one by one. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r107-b16", "out": "s16-that-was-the-answer-to.jpeg", "seg": "n5",
        "window": "86.88-89.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["TWO"],
        "narration": "That was the answer to give a doubting man.",
        "must_show": "the answer packed — the two messengers turning for home at day's end, faces resolved and full; the scene stowed for the cell.",
        "must_not_show": "no halo, glare or rim-light; their resolve GLAD — couriers finally carrying good freight.",
        "scene": (
            "At the golden end of the "
            "day the couriers turn for "
            "home carrying different "
            "freight: the grim question "
            "they walked in with "
            "traded for a scene that "
            "keeps replaying behind "
            "both pairs of eyes — the "
            "older man's face resolved "
            "and quiet, the younger "
            "already half-smiling at "
            "the telling to come — two "
            "men aimed at a fortress "
            "cell with the only answer "
            "sized for a doubting "
            "prophet: not proof; "
            "spectacle of love. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r107-b17", "out": "s17-look-at-the-love-look.jpeg", "seg": "n5",
        "window": "89.64-94.25", "wide": True, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "Look at the love. Look at what it is actually doing.",
        "must_show": "love at work wide — the healing day's whole warm panorama once more: every corner of the frame an act of care in progress; the instruction LOOK obeyed by the composition.",
        "must_not_show": "no halo, glare or rim-light; EVERY visible interaction kind — the frame saturated with care.",
        "scene": (
            "The instruction is obeyed by "
            "the whole frame: everywhere "
            "the eye lands, love caught "
            "in the act — here a healed "
            "boy hoisted laughing onto "
            "his father's shoulders, "
            "there Jesus steadying an "
            "old man's first unaided "
            "walk in years, beyond them "
            "women sharing out bread "
            "to strangers' children — "
            "not one cold corner in "
            "the composition, the "
            "afternoon packed edge to "
            "edge with what the love "
            "is actually doing. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r107-b18", "out": "s18-and-blessed-is-he-whosoever.jpeg", "seg": "jv6 + n6",
        "window": "94.79-102.38", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TWO"],
        "narration": (
            "And blessed is he, whosoever shall not be offended in me. It "
            "was tender, not sharp."
        ),
        "must_show": "SCRIPTURE-EXACT: the tender blessing — close on Jesus giving the final word to the departing two: gentleness saturating the sentence meant for John's cell.",
        "must_not_show": "no halo, glare or rim-light; NOTHING sharp in the delivery — a message wrapped soft for a hurting friend.",
        "scene": (
            "The last line goes into the "
            "couriers' keeping wrapped "
            "soft: Jesus's face close "
            "and gentle as he gives it "
            "— BLESSED IS HE, WHOSOEVER "
            "SHALL NOT BE OFFENDED IN "
            "ME — every word chosen "
            "the way you choose words "
            "for a wounded friend's "
            "bedside, no edge anywhere "
            "on the sentence, a "
            "blessing aimed through "
            "two memories and one "
            "iron grate at a doubter "
            "he loves. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r107-b19", "out": "s19-blessed-is-the-one-who.jpeg", "seg": "n6",
        "window": "102.38-107.25", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": (
            "Blessed is the one who does not give up on me when I do not "
            "look the way he expected."
        ),
        "must_show": "the meaning held — Jesus's steady warm face in the late light: the unexpected shape of him offered as itself, trust invited.",
        "must_not_show": "no halo, glare or rim-light; the face UNAPOLOGETIC and kind — this is what the Promised One looks like.",
        "scene": (
            "Close on the unexpected "
            "shape of the answer to "
            "every prayer: no armored "
            "conqueror, no lightning "
            "in either hand — a "
            "sun-browned face in the "
            "late light, kind past "
            "measuring and utterly "
            "unapologetic about the "
            "form love took — offered "
            "as itself to everyone "
            "whose rescue is running "
            "late and whose picture "
            "of God is having to "
            "grow: blessed, blessed "
            "is the one who stays. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r107-b20", "out": "s20-and-then-the-moment-the.jpeg", "seg": "n6",
        "window": "107.25-116.17", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TWO"],
        "narration": (
            "And then, the moment the messengers left, Jesus turned to the "
            "crowd and praised John — defending his doubting friend to his "
            "face."
        ),
        "must_show": "SCRIPTURE-EXACT: the defense (v7-11) — the two messengers small on the road out, and Jesus turned to the big crowd mid-praise, arm raised high for the absent John; loyalty public.",
        "must_not_show": "no halo, glare or rim-light; the TIMING visible — the couriers barely gone, the praise already at full voice.",
        "scene": (
            "The couriers are barely "
            "forty paces gone when the "
            "loyalty starts: Jesus "
            "turned full to the great "
            "crowd with his arm raised "
            "high, voice carrying — "
            "praise for the man in the "
            "fortress rolling out over "
            "the heads: no reed shaken "
            "by wind, no soft courtier "
            "— a PROPHET, and more — "
            "the doubter defended at "
            "full volume behind his "
            "back, by the very one he "
            "doubted, while his "
            "question is still warm. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r107-b21", "out": "s21-the-answer-came-back-to.jpeg", "seg": "n7",
        "window": "116.72-119.71", "wide": True, "jesus": False, "ref": False,
        "locks": ["CELL", "JOHNB", "TWO"],
        "narration": "The answer came back to the cell, and John was at peace.",
        "must_show": "the report delivered — the two at the cell grate mid-telling, and John listening within: the scene pouring through the iron bars into the dimness.",
        "must_not_show": "no halo, glare or rim-light; the telling ANIMATED through the grate — hands shaping healings in the corridor's torchlight.",
        "scene": (
            "The scene comes home "
            "through iron: the two "
            "messengers crowded at the "
            "little grate with the "
            "telling spilling out of "
            "them — hands shaping the "
            "opened eyes, the first "
            "steps, the risen girl, "
            "the poor gathered close — "
            "and inside the dimness "
            "John's wild head bowed "
            "near the bars, drinking "
            "it down word by word, "
            "the answer arriving in "
            "his cell the only way "
            "it ever needed to: as "
            "witnessed love, retold. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r107-b22", "out": "s22-not-rescued-but-no-longer.jpeg", "seg": "n7",
        "window": "119.71-126.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELL", "JOHNB"],
        "narration": (
            "Not rescued — but no longer alone in the dark, and no longer "
            "afraid that he had been wrong."
        ),
        "must_show": "the peace without rescue — John settled back against his wall, chains unchanged, the shaft of light warmed gold on his quieted face; peace inside the unopened cell.",
        "must_not_show": "no rescue imagery, no opened door — the chains STAY; the change is entirely in his face and the light's warmth.",
        "scene": (
            "Nothing about the cell has "
            "changed, and everything "
            "has: the same iron at the "
            "same wrist, the same "
            "stone, the same waiting — "
            "but the shaft from the "
            "high slit falls warm gold "
            "now across a face gone "
            "quiet at last: the "
            "burning eyes banked to a "
            "steady peace, the wild "
            "head resting back against "
            "the wall almost easily — "
            "not rescued, and not "
            "wrong, and it turns out "
            "the second one was the "
            "rescue he needed. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r107-b23", "out": "s23-sometimes-the-answer-to-our.jpeg", "seg": "n7b",
        "window": "126.61-129.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELL"],
        "narration": "Sometimes the answer to our doubt is not the thing we asked for.",
        "must_show": "the answered-otherwise — the cell's gold shaft falling on the straw where the question was born: the space itself quieted; asked-for absent, given-instead present.",
        "must_not_show": "no figure needed — the lit empty corner speaks; no halo.",
        "scene": (
            "The frame rests where the "
            "question was born: the "
            "corner of straw and stone "
            "under the high slit, the "
            "gold shaft lying across "
            "it like a hand — no "
            "shattered door in the "
            "picture, no struck-off "
            "chains, none of the "
            "things the asking asked "
            "for — and the little "
            "space quieted anyway, "
            "holding the older truth: "
            "that answers come more "
            "often as presence than "
            "as rescue, and are "
            "somehow enough. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r107-b24", "out": "s24-it-is-simply-quietly-look.jpeg", "seg": "n7b",
        "window": "129.73-136.20", "wide": True, "jesus": True, "ref": REF,
        "locks": [],
        "narration": (
            "It is simply, quietly: look at the love. It is real, and it is "
            "for you."
        ),
        "must_show": "the look-at-the-love — Jesus amid the day's mercy once more, but the composition turned slightly outward: the love's warmth angled toward the viewer's position.",
        "must_not_show": "no halo, glare or rim-light; the FOR YOU spatial — an open place in the scene nearest the frame.",
        "scene": (
            "One more time, the answer: "
            "Jesus in the middle of "
            "the day's mercy — a child "
            "on his knee, the healed "
            "and the fed everywhere in "
            "the warm light — but the "
            "whole scene angled gently "
            "outward now, an open "
            "space in the grass at the "
            "frame's near edge, room "
            "at the front of the "
            "crowd left deliberately "
            "unfilled — the love real, "
            "and visibly, spatially, "
            "held open for whoever is "
            "looking at it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r107-b25", "out": "s25-do-not-be-offended-only.jpeg", "seg": "n7b",
        "window": "136.20-141.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["CELL", "JOHNB"],
        "narration": "Do not be offended — only trust, and be at peace.",
        "must_show": "the closing image — John at peace in the gold shaft, eyes closed, the iron forgotten on his wrist; a doubter's rest, complete.",
        "must_not_show": "no rescue, no door, no foreshadowing — only the rested face in the warm light, trust visible as sleep comes.",
        "scene": (
            "The closing frame keeps the "
            "doubter at rest: John "
            "settled in the gold shaft "
            "with his eyes closed and "
            "his breathing long, the "
            "iron lying forgotten on a "
            "wrist gone loose, the "
            "wild face smoothed into "
            "something very near a "
            "smile — a man who asked "
            "his worst question out "
            "loud, got back a scene "
            "full of love, and fell "
            "asleep in his chains "
            "trusting the one he "
            "doubted — at peace, all "
            "the way down. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
]
