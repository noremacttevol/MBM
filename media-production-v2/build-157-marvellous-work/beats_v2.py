#!/usr/bin/env python3
"""V2 beat map — row 157, build-157-marvellous-work (Isaiah 29:11-14).

COVERAGE: 28 pictures over 159.3 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Isaiah 29 KJV):
  29:11 "the vision of all is become unto you as the words of A BOOK
        THAT IS SEALED, which men deliver to one that is LEARNED,
        saying, Read this, I pray thee: and he saith, I CANNOT; FOR
        IT IS SEALED."
  29:12 "And the book is delivered to him that is NOT LEARNED,
        saying, Read this, I pray thee: and he saith, I am not
        learned."
  29:13 "this people draw near me with their MOUTH, and with their
        LIPS do honour me, but have REMOVED THEIR HEART FAR from me,
        and their fear toward me is TAUGHT BY THE PRECEPT OF MEN."
  29:14 "Therefore, behold, I will proceed to do A MARVELLOUS WORK
        among this people, even a marvellous work AND A WONDER: for
        the wisdom of their wise men shall perish."

ROW INTENT: the sealed-book row (BRIDGE) — human learning at its
limit, hearts drifted to habit, and God promising to act HIMSELF.
Kept entirely in Isaiah's own frame.

RENDERING LAWS:
  - THE BOOK is a SEALED SCROLL (period-true): heavy rolled
    parchment bound with cords and WAX SEALS, clasped in a worn
    leather case — one object, the same in every frame; its state
    is per-beat (sealed until b24; OPEN from b24). Script
    indistinct always.
  - THE OPENING (b23/b24) is GOD'S ACT SHOWN AS LIGHT AND RESULT
    ONLY: no hands open it, no mechanism depicted — sealed in
    strengthening dawn (b23), then simply OPEN in morning light
    (b24). No figure, ever.
  - THE SCHOLAR and THE PLAIN MAN are both honest and sympathetic —
    the learned man's "I cannot" is honorable admission; the plain
    man's refusal is kind. No fools, no villains.
  - The lips/heart beats (b14/b17) are the row-128 register: correct
    mouths, absent eyes, precise hollow ceremony.
  - GOD IS NEVER EMBODIED (b16/b21): the word arrives as listening
    and light.
  - ISAIAH is a courtly elder prophet — distinct from 152's Amos.

TIME OF DAY ARC (intentional): Isaiah's frames at lamplit evening
gravity; the sealed-book scenes in cool interior day; the scholar's
defeat at guttering candle night; the promise (b21) at first dawn
through the window; the opened book in full clean morning; the
close in that same morning, kneeling.

CHANGING CONDITIONS (kept OUT of the locks): the scroll — sealed,
dawn-lit, OPEN; the light — lamp, night, dawn, morning.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row).
LOCKS = {
    "ISAIAH": (
        "ISAIAH LOCK: Isaiah is the same man in every shot — a "
        "courtly elder prophet of about sixty-five: silver hair and "
        "a long silver beard, fine deep-lined features, in a DEEP "
        "INDIGO robe with a dark mantle (never cream, never white); "
        "grief and vision sharing the noble old face."
    ),
    "BOOK": (
        "BOOK LOCK: the sealed book — ONE heavy rolled parchment "
        "scroll bound with dark cords and THREE WAX SEALS, resting "
        "in a worn open leather case; venerable, precious, plainly "
        "important. The same scroll, cords, seals and case "
        "throughout; its script always indistinct."
    ),
    "SCHOLAR": (
        "SCHOLAR LOCK: the learned man is the same in every shot — "
        "about fifty-five, precise and dignified, a trimmed grey "
        "beard, in fine DARK CHARCOAL robes with a scholar's sash "
        "(never cream, never white); honest, honourable, at his "
        "limit — never a fool."
    ),
    "PLAIN": (
        "PLAIN LOCK: the unschooled man is the same in every shot — "
        "about forty, a broad kind working face, in a rough DARK "
        "RUST tunic (never cream, never white); simple honesty, "
        "gentle; never mocked."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r157-b01", "out": "s01-the-prophet-isaiah-painted-a.jpeg", "seg": "n1",
        "window": "0.28-4.56", "wide": True, "jesus": False, "ref": False,
        "locks": ["ISAIAH"],
        "narration": "The prophet Isaiah painted a strange, almost sad picture of his people.",
        "must_show": "the prophet's grief — Isaiah at his lamplit evening window over the city's rooftops, the sad strange picture gathering in the noble old face.",
        "must_not_show": "no halo; the sadness NOBLE — a seer grieving what he sees; the city's lamps below.",
        "scene": (
            "The picture he is about to paint costs him "
            "something, the camera set in the room behind his "
            "robed back at the window: Isaiah at the lamplit "
            "sill with the city's rooftops falling away below "
            "in their little scattered lights — the silver "
            "head bowed a degree, the deep-lined face working "
            "over a sorrow the people down there do not know "
            "they are the subject of — a courtly old seer "
            "composing the saddest metaphor of his book about "
            "the congregation he loves. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b02", "out": "s02-the-truth-of-god-he.jpeg", "seg": "n1",
        "window": "4.56-13.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK"],
        "narration": (
            "The truth of God, he said, had become to them like a book that "
            "is sealed shut — right there in their hands, and yet closed, "
            "its meaning locked away."
        ),
        "must_show": "the image itself — hands HOLDING the sealed scroll: possessed and locked at once; the cords and wax seals plain; nearness without access.",
        "must_not_show": "no halo; the holding REAL — in the hands, and closed; seals unbroken.",
        "scene": (
            "The tragedy fits in two hands: the sealed "
            "scroll lies across open palms — actually held, "
            "actually theirs, the heavy parchment warm "
            "against the skin — and closed: the dark cords "
            "crossed and knotted, the three wax seals "
            "sitting unbroken over the rolled edge — the "
            "truth of God at a distance of zero inches and "
            "locked all the same, which is the strangest "
            "kind of far away there is. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b03", "out": "s03-imagine-a-precious-book-clasped.jpeg", "seg": "n2",
        "window": "13.99-18.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK"],
        "narration": "Imagine a precious book, clasped and sealed, that no one around can open.",
        "must_show": "the seals close — the three wax seals and crossed cords in detail, the worn leather case; preciousness and closedness in one object.",
        "must_not_show": "no halo; the seals UNBROKEN and old; script indistinct at the roll's visible edge.",
        "scene": (
            "Study the hardware of the problem: close on "
            "the scroll's three wax seals — old, "
            "thumb-pressed, unbroken, their devices worn "
            "smooth — the dark cords crossed beneath them "
            "with a binder's care, the leather case "
            "polished by generations of reverent carrying — "
            "everything about the object saying PRECIOUS, "
            "and everything about its fastenings saying "
            "NOT YET — a treasure engineered, for now, to "
            "stay one. No people are needed in this "
            "frame."
        ),
    },
    {
        "id": "v2-r157-b04", "out": "s04-everyone-senses-it-matters.jpeg", "seg": "n2",
        "window": "18.67-20.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK"],
        "narration": "Everyone senses it matters.",
        "must_show": "the sensed weight — varied faces ringed around the sealed scroll, reverent and puzzled; importance felt through the seals.",
        "must_not_show": "no halo; the reverence HONEST — drawn faces, careful distance.",
        "scene": (
            "Nobody in the room can read it and nobody "
            "doubts it: around the table's sealed scroll "
            "the faces ring in reverent puzzlement — an "
            "elder leaning close without touching, a "
            "young woman's hand half-lifted and withdrawn, "
            "a boy peering between shoulders — every "
            "instinct in the room agreeing on the one "
            "thing the seals cannot lock in: that "
            "whatever sleeps inside this parchment "
            "MATTERS, and matters to them. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b05", "out": "s05-the-words-of-heaven-sitting.jpeg", "seg": "n2",
        "window": "22.01-25.72", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK"],
        "narration": "The words of heaven, sitting sealed in the middle of them.",
        "must_show": "the centre — the sealed scroll alone at the table's middle, the ring of people around it at a helpless remove; heaven's words present and inaccessible.",
        "must_not_show": "no halo; the composition CENTRED on the sealed thing — the ring's helplessness readable.",
        "scene": (
            "The seating chart says everything: the sealed "
            "scroll holds the table's exact centre — the "
            "place of honour, the place of bread — and "
            "around it the household sits at its helpless "
            "remove, hands in laps, eyes on the cords — "
            "the words of heaven physically among them, "
            "at the middle of their table and their town "
            "and their whole aching life, sealed — a "
            "guest of honour nobody can hear. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r157-b06", "out": "s06-so-they-carry-it-to.jpeg", "seg": "n3",
        "window": "26.24-34.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK", "SCHOLAR"],
        "narration": (
            "So they carry it to their most educated man, the scholar "
            "everyone respects, and they say, please, read this for us."
        ),
        "must_show": "the delivery — the sealed scroll presented with hope to the dignified scholar in his study of shelved scrolls; respect on every side.",
        "must_not_show": "no halo; the scholar HONOURABLE — receiving with care; the bringers hopeful.",
        "scene": (
            "They take the problem to the best mind they "
            "know: into the scholar's study — shelves "
            "ranked with scroll-ends like honeycomb, the "
            "tools of a careful life ordered on the "
            "table — the household delivers the sealed "
            "scroll with both hands and all their hope: "
            "read this, please, FOR us — and the grey-"
            "bearded man receives it with the reverence "
            "of his calling, turning to the light, "
            "everyone in the room certain that learning "
            "this deep must surely hold the key. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r157-b07", "out": "s07-he-turns-it-over-in.jpeg", "seg": "n3",
        "window": "34.18-39.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK", "SCHOLAR"],
        "narration": (
            "He turns it over in his hands, and has to admit the plain "
            "truth: he cannot."
        ),
        "must_show": "the honest limit — the scholar turning the sealed scroll in careful hands, then meeting the bringers' eyes with honourable admission; defeat with dignity.",
        "must_not_show": "no halo; the admission HONOURABLE — no shame theatre; the seals unbroken in his careful grip.",
        "scene": (
            "The best mind in town gives the honest "
            "verdict: the scholar turns the sealed scroll "
            "slowly in his careful hands — testing the "
            "cords' knots with a fingertip, tilting the "
            "seals to the window light, bringing forty "
            "years of letters to bear on the fastenings — "
            "and then lifts his eyes to the hopeful "
            "faces and gives them the truth his honour "
            "requires: he cannot — the plainest sentence "
            "his learning ever produced, and the most "
            "honest. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r157-b08", "out": "s08-no-one-can-get-inside.jpeg", "seg": "n2",
        "window": "20.40-22.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK"],
        "narration": "No one can get inside it.",
        "must_show": "the general helplessness — several varied hands hovering around the sealed scroll, none able to act; the locked-out community in hands alone.",
        "must_not_show": "no halo; the hands VARIED (old, young, worn, fine) and all equally stopped.",
        "scene": (
            "Every kind of hand has tried and hovered "
            "back: around the sealed scroll the hands "
            "hang in the air at their small helpless "
            "distances — a grandmother's knotted fingers, "
            "a scribe's ink-stained ones, a farmer's "
            "blunt strength, a child's small reach — "
            "every grip the town owns, and not one with "
            "anything to do: the seals answer to none of "
            "them — inside, for now, is nobody's "
            "country. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r157-b09", "out": "s09-and-the-vision-of-all.jpeg", "seg": "kv11",
        "window": "40.72-52.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK", "SCHOLAR"],
        "narration": (
            "And the vision of all is become unto you as the words of a "
            "book that is sealed, which men deliver to one that is learned, "
            "saying, Read this, I pray thee: and he saith, I cannot; for it "
            "is sealed:"
        ),
        "must_show": "SCRIPTURE-EXACT: the whole verse staged — the deliverers, the learned man, the sealed scroll between them, the I-cannot on his honourable face; the verse in one composition.",
        "must_not_show": "no halo; every element present — bringers, scholar, sealed scroll; the admission mid-word.",
        "scene": (
            "The verse stands complete in one study: the "
            "bringers on one side with their hope still "
            "half-alive, the learned man on the other "
            "with the sealed scroll held out between "
            "them like a verdict — READ this, I pray "
            "thee, their posture still asks — and his "
            "honourable face mid-sentence on the only "
            "answer his integrity permits: I CANNOT — "
            "for it is SEALED — Isaiah's picture, "
            "photographed at the exact moment the best "
            "human answer runs out. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b10", "out": "s10-it-is-sealed.jpeg", "seg": "n3",
        "window": "39.37-40.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK"],
        "narration": "It is sealed.",
        "must_show": "the three words — extreme close on one unbroken wax seal; absolute, brief, final for now.",
        "must_not_show": "no halo; ONE seal filling the frame — unbroken.",
        "scene": (
            "Three words, one image: a single wax seal "
            "fills the frame — old, thumb-pressed, its "
            "worn device catching the window light along "
            "one edge, the dark cord vanishing beneath "
            "it — unbroken, unanswerable, the entire "
            "state of things pressed into a coin's-width "
            "of wax — sealed: for now, the last word on "
            "the subject, and everyone in the town knows "
            "it. No people are in this frame."
        ),
    },
    {
        "id": "v2-r157-b11", "out": "s11-then-they-hand-it-to.jpeg", "seg": "n4",
        "window": "54.13-60.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK", "PLAIN"],
        "narration": (
            "Then they hand it to a plain, unschooled man, hoping simple "
            "honesty might succeed where learning failed."
        ),
        "must_show": "the second try — the sealed scroll placed hopefully in the plain man's broad working hands; simple honesty given its turn.",
        "must_not_show": "no halo; the plain man KIND and dignified — never mocked; his hands careful with the precious thing.",
        "scene": (
            "The town tries the opposite kind of hands: "
            "into the plain man's broad working grip the "
            "sealed scroll is set with new hope — maybe "
            "learning was the obstacle; maybe simple "
            "honesty is the key — and he holds it with "
            "the enormous care of a man more used to "
            "plough-handles, turning it gently in the "
            "light, wanting with his whole kind face to "
            "be the answer they need. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b12", "out": "s12-neither-the-wise-nor-the.jpeg", "seg": "n4",
        "window": "62.30-65.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK", "SCHOLAR", "PLAIN"],
        "narration": "Neither the wise nor the simple can open it on their own.",
        "must_show": "the shared limit — scholar and plain man on either side of the sealed scroll, both honest, both stopped; human capacity's full range, equally short.",
        "must_not_show": "no halo; NEITHER man diminished — two honest limits, one sealed scroll between.",
        "scene": (
            "The whole range of human ability flanks the "
            "problem and neither end reaches: the scholar "
            "on one side with his lifetime of letters, "
            "the plain man on the other with his lifetime "
            "of honest work — two good faces, two kinds "
            "of capable hands, and between them the "
            "sealed scroll exactly as sealed as before "
            "either tried — wise and simple measured "
            "against the same cords and found, without "
            "shame, the same length short. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b13", "out": "s13-but-he-only-shakes-his.jpeg", "seg": "n4",
        "window": "60.24-62.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": "But he only shakes his head kindly.",
        "must_show": "the kind refusal — close on the plain man's gentle head-shake, the honest regret in the broad face; simplicity's honourable I-am-not-learned.",
        "must_not_show": "no halo; the kindness EXACT — regret without shame; never mocked.",
        "scene": (
            "His refusal is as gentle as everything else "
            "about him: close on the plain man's broad "
            "kind face as the head shakes slowly — regret "
            "honest in the eyes, the big careful hands "
            "already offering the scroll back — I am not "
            "learned, the whole posture says, and wishes "
            "it were otherwise for their sakes — "
            "simplicity meeting its limit with the same "
            "honour the scholar met his: truthfully. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r157-b14", "out": "s14-forasmuch-as-this-people-draw.jpeg", "seg": "kv13b",
        "window": "69.23-82.55", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Forasmuch as this people draw near me with their mouth, and "
            "with their lips do honour me, but have removed their heart far "
            "from me, and their fear toward me is taught by the precept of "
            "men:"
        ),
        "must_show": "SCRIPTURE-EXACT: the lips/heart diagnosis — the row-128 register: a fine-robed worshiper's correct moving lips and absent, elsewhere eyes; nearness of mouth, distance of heart.",
        "must_not_show": "no halo; the distance in the EYES — correct mouth, absent gaze; sincere-looking, hollow.",
        "scene": (
            "The diagnosis has a portrait, and Isaiah "
            "hangs it here: the fine-robed worshiper at "
            "his prayers — hands placed just so, the lips "
            "moving through honours polished by lifelong "
            "repetition — and above the flawless mouth, "
            "the eyes: cold, elsewhere, running private "
            "sums miles from the words — drawing near "
            "with the mouth while the heart stands at "
            "its far remove, schooled in reverence by "
            "the precepts of men and by nothing warmer. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r157-b15", "out": "s15-isaiah-saw-the-deeper-trouble.jpeg", "seg": "n5",
        "window": "84.04-86.33", "wide": False, "jesus": False, "ref": False,
        "locks": ["ISAIAH"],
        "narration": "Isaiah saw the deeper trouble underneath.",
        "must_show": "the seer's depth — close on Isaiah's grave discerning face; the surface problem (seals) and the real one (hearts) both in his old eyes.",
        "must_not_show": "no halo; the discernment READABLE — sorrow with precision.",
        "scene": (
            "The old seer's eyes go down through the "
            "problem's floor: close on Isaiah's deep-"
            "lined face in the lamp gravity — and the "
            "look in it is a diagnostician's: past the "
            "sealed scroll everyone frets over, down to "
            "the quieter sealing underneath — hearts "
            "shut by drift and habit, worship gone to "
            "recitation — the trouble beneath the "
            "trouble, seen whole by a man whose calling "
            "is exactly this kind of seeing, and grieved "
            "with precision. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b16", "out": "s16-wherefore-the-lord-said.jpeg", "seg": "kv13a",
        "window": "66.23-67.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["ISAIAH"],
        "narration": "Wherefore the Lord said,",
        "must_show": "the word arriving — Isaiah stilled into the listening posture, head tipped, the divine word beginning; GOD NEVER EMBODIED.",
        "must_not_show": "ABSOLUTE: no figure, no visualized voice — the arrested listening carries it.",
        "scene": (
            "The prophet's trade has a posture and he "
            "takes it: Isaiah goes still mid-thought — "
            "the silver head tipping into the old "
            "listening angle, the lamplit room's small "
            "sounds falling away from around him — the "
            "LORD, saying — the word arriving to its "
            "appointed listener with no shape and no "
            "sound the frame can carry, only the "
            "stillness of the man receiving it, which "
            "has always been evidence enough. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r157-b17", "out": "s17-the-people-still-said-the.jpeg", "seg": "n5",
        "window": "86.33-97.36", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The people still said the right words and kept the outward "
            "forms, honouring God with their lips — but their hearts had "
            "quietly drifted far away, and their worship had shrunk to "
            "habits taught by men."
        ),
        "must_show": "the shrunken worship — precise ceremonial motions performed by rote (the 128 vessels register): exact hands, absent faces; habit where heart was.",
        "must_not_show": "no halo; the precision FASTIDIOUS and hollow — beautiful motions, nobody home.",
        "scene": (
            "The ceremony has outlived its cargo: along "
            "the rite's stations the hands perform their "
            "inherited exactness — the pour measured to "
            "the knuckle, the bow timed to the syllable, "
            "the vessels handled in the taught order "
            "without one error — and above the flawless "
            "choreography the faces have gone absent, "
            "eyes elsewhere, hearts at their quiet "
            "removed distance — worship shrunk to the "
            "habits men can teach, which are exactly the "
            "parts that were never the point. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r157-b18", "out": "s18-and-no-amount-of-human.jpeg", "seg": "n6",
        "window": "97.90-101.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK", "SCHOLAR"],
        "narration": "And no amount of human cleverness was going to fix that.",
        "must_show": "cleverness spent — the scholar's full toolkit (styluses, lexicon scrolls, scroll-weights, lenses of the era) spread useless around the still-sealed scroll.",
        "must_not_show": "no halo; the tools PERIOD-TRUE and exhausted-looking in arrangement; the seals unbothered.",
        "scene": (
            "Every tool the mind owns lies tried around "
            "the problem: the scholar's table spread with "
            "his full armory — styluses and reed pens, "
            "the lexicon scrolls unrolled and weighted, "
            "comparison texts flagged with threads, every "
            "instrument of a careful life deployed — and "
            "at the centre of all that spent cleverness "
            "the sealed scroll sits exactly as it "
            "arrived, cords crossed, seals whole, "
            "unbothered by the siege — some locks are "
            "not addressed to the mind. No people are "
            "needed in this frame."
        ),
    },
    {
        "id": "v2-r157-b19", "out": "s19-the-wisdom-of-the-wise.jpeg", "seg": "n6",
        "window": "101.19-104.54", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK", "SCHOLAR"],
        "narration": "The wisdom of the wise had run to the very end of itself.",
        "must_show": "the end of wisdom — the scholar at night, head in his hands over the sealed scroll, candle burned to a stub; the honest exhaustion of human light.",
        "must_not_show": "no halo; the exhaustion HONOURABLE — spent, not broken; candle nearly out.",
        "scene": (
            "Wisdom's candle burns to its honest end: deep "
            "in the night the scholar sits with his head "
            "down in both hands over the sealed scroll, "
            "the candle beside him guttered to a "
            "thumb's-width stub — every argument run, "
            "every authority consulted, every hour spent — "
            "the wisdom of the wise arriving where all "
            "human light arrives eventually: at the end "
            "of its wick, with the real dark still "
            "unbroken in front of it. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b20", "out": "s20-the-experts-had-no-key.jpeg", "seg": "n6",
        "window": "104.54-109.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK"],
        "narration": "The experts had no key for a sealed book, or for a heart that had wandered off.",
        "must_show": "the keyless lock — a great iron ring of many keys hung beside the sealed scroll, every key the wrong shape for wax and cord; the toolless problem.",
        "must_not_show": "no halo; the mismatch READABLE — keys for locks, and this is not a lock keys know.",
        "scene": (
            "The key ring is heavy and completely beside "
            "the point: the great iron ring hangs on its "
            "peg beside the sealed scroll — keys for "
            "doors, keys for chests, keys for every lock "
            "the town's smiths ever cut — and not one of "
            "them shaped for wax and knotted cord, let "
            "alone for the quieter sealing in the "
            "people's chests — the experts' whole "
            "jangling inventory, hanging there fluent in "
            "the wrong language. No people are needed in "
            "this frame."
        ),
    },
    {
        "id": "v2-r157-b21", "out": "s21-therefore-behold-i-will-proceed.jpeg", "seg": "kv14",
        "window": "109.75-125.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK"],
        "narration": (
            "Therefore, behold, I will proceed to do a marvellous work "
            "among this people, even a marvellous work and a wonder: for "
            "the wisdom of their wise men shall perish, and the "
            "understanding of their prudent men shall be hid."
        ),
        "must_show": "SCRIPTURE-EXACT: the promise — FIRST DAWN breaking through the window directly onto the sealed scroll; God's act beginning as light; no figure, no hands.",
        "must_not_show": "ABSOLUTE: no figure, no opening mechanics yet — the dawn's first light on the still-sealed scroll carries the THEREFORE.",
        "scene": (
            "Heaven answers the spent candle with a "
            "sunrise: through the study's east window the "
            "first dawn comes in one long shaft and lands "
            "directly on the sealed scroll — the wax "
            "seals warming from grey to honey, the cords' "
            "shadows going long and soft, the guttered "
            "stub beside it made irrelevant by the "
            "arriving scale of light — THEREFORE, behold: "
            "I will proceed — a marvellous work and a "
            "wonder, beginning the way God's work "
            "begins: with morning, aimed. No people are "
            "in this frame."
        ),
    },
    {
        "id": "v2-r157-b22", "out": "s22-so-the-only-question-is.jpeg", "seg": "n8",
        "window": "152.80-155.22", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "So the only question is a hopeful one.",
        "must_show": "the hopeful pivot — a listening face brightening in morning light; the question's warmth arriving.",
        "must_not_show": "no halo; the brightening subtle and real.",
        "scene": (
            "The question arrives wearing morning: a "
            "listening face in the clean early light, "
            "and across it the slow warming — the "
            "guarded lines easing, the eyes lifting "
            "with something between memory and "
            "appetite — a person who has heard the whole "
            "sealed-book story and caught, at its turn, "
            "the scent of the hopeful part: that the "
            "wonder is God's to do, and he has said he "
            "will. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r157-b23", "out": "s23-so-god-promised-to-step.jpeg", "seg": "n7",
        "window": "126.72-131.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK"],
        "narration": (
            "So God promised to step in himself and do something marvellous "
            "— a genuine wonder."
        ),
        "must_show": "the promise held — the sealed scroll in full strengthening dawn, the light now broad on seals and cords; the act imminent, nothing yet opened; no figure.",
        "must_not_show": "ABSOLUTE: still SEALED; no figure, no hands — the light's strength is the promise.",
        "scene": (
            "The light on the seals keeps strengthening "
            "like a word being kept: the scroll lies in "
            "the now-broad dawn — every cord distinct in "
            "the warm gold, the three seals lit like "
            "small suns of wax, the leather case warm-lit at "
            "its worn edges — nothing opened yet, "
            "nothing touched — but the whole object "
            "standing inside an arriving intention the "
            "way a field stands inside the hour before "
            "harvest: promised, imminent, and not by any "
            "hand in the room. No people are in this "
            "frame."
        ),
    },
    {
        "id": "v2-r157-b24", "out": "s24-not-one-more-lecture-from.jpeg", "seg": "n7",
        "window": "131.78-139.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK"],
        "narration": (
            "Not one more lecture from the learned, but an act of God that "
            "would open what men had sealed and reach hearts that had "
            "wandered."
        ),
        "must_show": "THE OPENING SHOWN AS RESULT — the scroll now OPEN in full morning light, unrolled across the table, its indistinct lines revealed; no hands, no mechanism — simply, marvellously, open.",
        "must_not_show": "ABSOLUTE: no hands, no figure, no opening mechanics — the OPEN state itself the wonder; script indistinct.",
        "scene": (
            "Between one frame and the next, the wonder "
            "has simply happened: the scroll lies OPEN "
            "across the table in the full clean morning — "
            "unrolled wide, the cords lying loose and "
            "unknotted beside their unbroken seals, the "
            "old indistinct lines bared at last to the "
            "light that came for them — no hands in the "
            "frame, no instrument, no explanation the "
            "room can offer — opened the way sealed "
            "things open when God proceeds: entirely, "
            "quietly, and not by men. No people are in "
            "this frame."
        ),
    },
    {
        "id": "v2-r157-b25", "out": "s25-that-is-the-beautiful-turn.jpeg", "seg": "n8",
        "window": "140.19-142.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["ISAIAH"],
        "narration": "That is the beautiful turn in this verse.",
        "must_show": "the turn on the seer — Isaiah's face turning from its grief to wonder, the old eyes lit; the prophecy's beauty reaching its own prophet.",
        "must_not_show": "no halo; the turn READABLE — grief to wonder across the noble old face.",
        "scene": (
            "The sad picture's painter gets to see the "
            "turn: on Isaiah's deep-lined face the grief "
            "that opened the row gives way — the silver "
            "brows lifting, the far-seeing eyes going "
            "bright, something like a young man's wonder "
            "arriving in the old features — because the "
            "vision ran past the sealing to the OPENING, "
            "past the drifted hearts to the wonder that "
            "reaches them — and the prophet of the "
            "sealed book turns out to be the prophet of "
            "its marvellous unsealing. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b26", "out": "s26-when-human-wisdom-hits-its.jpeg", "seg": "n8",
        "window": "142.80-146.75", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "When human wisdom hits its limit, God is only getting started.",
        "must_show": "the two lights — the scholar's dead candle-stub in near frame, and through the window the SUN fully risen; man's light ended where God's begins.",
        "must_not_show": "no halo; the contrast exact — spent stub, risen sun, one window between.",
        "scene": (
            "Compare the two light sources and take the "
            "point: on the near sill the scholar's candle "
            "stands burned to its dead stub — a finger of "
            "cold wax, honest and finished — and through "
            "the window beyond it the sun stands fully "
            "risen over the hills, pouring more light "
            "into the room in one minute than the candle "
            "managed in its whole faithful night — human "
            "wisdom's end and God's beginning, "
            "photographed on one windowsill. No people "
            "are in this frame."
        ),
    },
    {
        "id": "v2-r157-b27", "out": "s27-he-is-fond-of-marvellous.jpeg", "seg": "n8",
        "window": "146.75-152.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK"],
        "narration": (
            "He is fond of marvellous works and wonders — the very things "
            "the experts said could not happen."
        ),
        "must_show": "the wonder enjoyed — the OPEN scroll at the table's centre with the whole ring of faces lit in astonishment around it: scholar, plain man, household, all wondering together.",
        "must_not_show": "no halo; every face ASTONISHED-GLAD — scholar and plain man equally; the open scroll central.",
        "scene": (
            "The impossible thing sits open on the table "
            "and the room adjusts: around the unrolled "
            "scroll the faces ring in lit astonishment — "
            "the scholar's careful composure gone to "
            "open-mouthed wonder, the plain man laughing "
            "under his breath, the grandmother's hands "
            "pressed together, the boy up on his toes — "
            "every expert opinion in the room happily "
            "overturned at once — because the God of the "
            "sealed book is FOND of this: marvellous "
            "works, wonders, the exact items the wise "
            "had crossed off the list. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b28", "out": "s28-when-the-wonder-comes-will.jpeg", "seg": "n8",
        "window": "155.22-159.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOK"],
        "narration": "When the wonder comes, will you be humble enough to receive it?",
        "must_show": "the closing receiving — kneeling open hands lifted, and the open scroll being lowered gently INTO them; humility's posture completing the row.",
        "must_not_show": "no halo; the lowering hands above frame-edge anonymous; the kneeling hands OPEN — receiving, not grasping.",
        "scene": (
            "The row ends in the posture the wonder "
            "waits for: a pair of open hands lifted from "
            "kneeling height, palms up and empty — and "
            "into them, lowered gently from above the "
            "frame's edge, comes the open scroll: the "
            "unsealed words settling onto humility the "
            "way bread settles into the hands at a "
            "table — not grasped, not argued into, "
            "RECEIVED — which was, from the first seal "
            "to the last wonder, the only opening "
            "anybody was ever asked to perform. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    # PLAIN: build-38 b46 auto-match REJECTED — PLAIN here is a PERSON token
    # (the unschooled man), not a place; the doorway frame is doubly wrong.
}
# === end PLACE-PLATES ===
