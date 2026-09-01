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
        "DIRECTLY on a bare ancient wooden table or held in hands; "
        "venerable, precious, plainly important. The same scroll, "
        "cords and THREE seals throughout; its script always "
        "indistinct. NEVER add a leather case, bag, satchel, strap, "
        "buckle, clasp, box or rectangular carrier."
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
        "about forty, a broad kind working face with a FULL SHORT "
        "DARK BEARD (never clean-shaven, never mere stubble), thick "
        "dark hair, in a rough DARK RUST tunic (never cream, never "
        "white); his face, beard and build EXACTLY as the attached "
        "reference image; simple honesty, gentle; never mocked."
    ),
}

REF = True

# AUDIO-FIX 2026-08-13 (Machine A `Dev`, audio lane, $0): STALE-V1 (row-141 class,
# both tripwires). The V1 mp4 is genuinely stale (209.8s vs 173.9s current
# timeline) AND all 13 V1-dir mp3s voice-ID'd as ElevenLabs new-voice (44100 Hz /
# 128 k; audio-eleven.log confirms all 13 cast) are newer than it. Rebuild the
# track from the new-voice mp3s at extract_beats offsets — no re-voice, no still
# regen; the stale longer mp4 stream is never touched.
AUDIO_FROM_V1_SEGMENTS = True

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
        "must_show": "the centre — the sealed scroll DIRECTLY on the bare table's middle, exactly EIGHT varied Middle Eastern Jewish townspeople around it at a helpless remove; heaven's words present and inaccessible. Every person wears dark brown, rust, charcoal or muted blue woven clothing.",
        "must_not_show": "no halo; no cream, white, off-white or pale clothing; no leather case, bag, satchel, strap, buckle, clasp, box or rectangular carrier; the composition CENTRED on the sealed scroll itself — the ring's helplessness readable.",
        "scene": (
            "The seating chart says everything: the sealed "
            "scroll holds the table's exact centre — the "
            "place of honour, the place of bread — and "
            "around it exactly eight people sit at their helpless "
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
        "must_show": "the general helplessness — several varied hands in DARK brown, rust, charcoal and muted-blue sleeves hovering around the sealed scroll, none able to act; the locked-out community in hands alone.",
        "must_not_show": "no halo; no cream, white, off-white, pale-grey or beige sleeves; no case, bag, strap, buckle, clasp, box or carrier; the hands VARIED (old, young, worn, fine) and all equally stopped.",
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
        "must_show": "SCRIPTURE-EXACT: the whole verse staged at ORDINARY HUMAN SCALE — two standing deliverers and one seated learned man, all normal-sized adults, with the sealed scroll between them and the I-cannot on his honourable face; all THREE wax seals remain separately countable; the verse in one composition.",
        "must_not_show": "no halo; NO giant, oversized person, forced-perspective giant or distorted body; NO briefcase, suitcase, bag, satchel, leather wrap, leather strap, belt, buckle, metal fitting, extra case or rectangular container visible anywhere — show ONLY the sealed parchment itself resting directly on the bare wooden table; NO cream, white or off-white garment on any person in this Old Testament scene; every element present — two bringers, scholar, sealed scroll; the admission mid-word.",
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
            "human answer runs out. The three people "
            "share ordinary adult human scale and wear "
            "only dark earth-tone woven garments; the "
            "sealed parchment rests directly on the bare "
            "wooden table; its leather travel-wrap is outside "
            "the frame, so no bag, strap or buckle appears. Every figure has "
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
        "must_show": "the second try — ONLY the sealed scroll placed hopefully in the plain man's broad working hands; simple honesty given its turn.",
        "must_not_show": "no halo; no leather case, bag, satchel, strap, buckle, clasp, box or rectangular carrier anywhere; the plain man KIND and dignified — never mocked; his hands careful with the precious scroll.",
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
        "must_show": "the shared limit — scholar and plain man on either side of ONE completely CLOSED rolled parchment scroll, tightly bound by dark cords and exactly THREE separately visible wax seals, lying DIRECTLY on the bare ancient wooden table; both men honest, both stopped.",
        "must_not_show": "no halo; ABSOLUTELY no open, unrolled, partly unrolled or loose parchment page and no visible writing; no leather case, bag, satchel, strap, buckle, clasp, box or rectangular carrier; NEITHER man diminished — two honest limits, one completely sealed scroll between.",
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
        "must_show": "ONE single unified ancient ceremony scene — one dark-robed Middle Eastern man pours a measured stream of water from one small clay pitcher into one shallow clay basin while three other dark-robed worshippers bow with technically exact posture but absent, distracted faces; habit where heart was.",
        "must_not_show": "no halo; ABSOLUTELY ONE image and ONE room, no panels, collage, split screen, grid, sequence, montage or repeated figures; no cream, white or off-white clothing; the precision FASTIDIOUS and hollow — beautiful motion, nobody home.",
        "scene": (
            "The ceremony has outlived its cargo: in one "
            "continuous room, one man pours water from one "
            "small clay pitcher into one shallow clay basin "
            "with inherited exactness while three others bow "
            "without one error — and above the flawless "
            "motion the four faces have gone absent, "
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
        "must_show": "cleverness spent — ONLY ancient reed pens, clay scroll-weights, loose parchment scrolls and knotted comparison threads spread useless around the still-sealed scroll lying directly on the bare ancient table.",
        "must_not_show": "no halo; no glass, lens, magnifier or spectacles; no bound or codex book, printed page or readable text; no leather case, bag, satchel, strap, buckle, clasp, box or carrier; the seals unbothered.",
        "scene": (
            "Every tool the mind owns lies tried around "
            "the problem: the scholar's table spread with "
            "his full armory — reed pens, clay scroll-weights, "
            "loose parchment scrolls unrolled and weighted, "
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
        "locks": [],
        "narration": (
            "Not one more lecture from the learned, but an act of God that "
            "would open what men had sealed and reach hearts that had "
            "wandered."
        ),
        "must_show": "THE OPENING SHOWN AS RESULT — ONE parchment scroll now fully OPEN and unrolled FLAT DIRECTLY on bare ancient wooden tabletop in full morning light; loose dark cords and exactly THREE separate unbroken wax seals lie on the bare wood beside it; no hands, no mechanism — simply, marvellously, open.",
        "must_not_show": "ABSOLUTE: no sealed or rolled scroll; no hands, figure or opening mechanics; no readable letters, words, Hebrew-like characters or printed text — marks are faded, blurred and indistinct; no object beneath the parchment; no leather or cloth mat, wrap, case, bag, satchel, strap, loop, buckle, clasp, box, tray or carrier anywhere.",
        "scene": (
            "Between one frame and the next, the wonder "
            "has simply happened: the scroll lies OPEN "
            "across the table in the full clean morning — "
            "unrolled wide, the cords lying loose and "
            "unknotted beside their unbroken seals, the "
            "old faded blurred marks bared at last to the "
            "light that came for them — no hands in the "
            "frame, no instrument, no explanation the "
            "room can offer — opened the way sealed "
            "things open when God proceeds: entirely, "
            "quietly, and not by men. No people are in "
            "this frame."
        ),
    },
    {
        "id": "v2-r157-b29", "out": "s29-the-book-is-opened.jpeg", "seg": "kv18",
        "window": "140.19-144.50", "wide": False, "jesus": False, "ref": False,
        "locks": ['BOOK'],
        "narration": (
            "And in that day shall the deaf hear the words of the book, "
            "and the eyes of the blind shall see out of obscurity, and "
            "out of darkness."
        ),
        "must_show": (
            "SCRIPTURE-EXACT: the sealed scroll OPENED — the same scroll, "
            "dark cords LOOSED, the three wax seals hanging BROKEN from "
            "their cords, parchment unrolled across the bare ancient "
            "table, weathered plain hands spreading it flat in warm "
            "lamplight."
        ),
        "must_not_show": (
            "no rays, no shining; the seals are BROKEN AND HANGING, never "
            "intact; no modern book or codex — it is the same rolled "
            "parchment scroll; no faces needed in frame."
        ),
        "scene": (
            "The promise lands on the object itself: seen from just above "
            "the table's edge, the great scroll lies OPEN at last — the "
            "dark cords fallen slack, the three worn wax seals hanging "
            "broken at its edge, the parchment spread wide under warm "
            "lamplight while two weathered working hands smooth it flat. "
            "The same venerable scroll from before, transformed by one "
            "fact: it is open. ONE single continuous photograph from one "
            "camera — never a collage, never panels, never a split frame. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b30", "out": "s30-the-deaf-hear.jpeg", "seg": "kv18",
        "window": "144.50-148.85", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "…the deaf hear the words of the book, and the eyes of the "
            "blind see out of obscurity…"
        ),
        "must_show": (
            "an aged listener leaning INTO the reading — the cupped hand "
            "falling away from his ear, eyes coming up from darkness "
            "toward the lit page, wonder breaking across the old face."
        ),
        "must_not_show": (
            "no rays or shining; not a healing scene with any healer "
            "present — the wonder is HEARING and SEEING the words; "
            "dignity total."
        ),
        "scene": (
            "Close on the far end of the promise: an aged listener at the "
            "table's edge, the hand that has cupped his ear a lifetime "
            "falling slowly away, his head tipping INTO the sound of the "
            "words being read — eyes lifting out of long obscurity toward "
            "the warm light on the parchment, wonder arriving in deep-cut "
            "features like morning into a valley. ONE single continuous "
            "photograph from one camera — never a collage, never panels, "
            "never a split frame. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r157-b31", "out": "s31-the-reading-circle.jpeg", "seg": "n7b",
        "window": "149.13-154.43", "wide": False, "jesus": False, "ref": False,
        "locks": ['BOOK'],
        "narration": (
            "Hear what he promised. The same book nobody could read — the "
            "deaf hear its very words."
        ),
        "must_show": (
            "the reading circle at eye level ACROSS the table: the open "
            "scroll centre, a reader's finger moving under the line, "
            "plain listeners bent close around it, lamplit."
        ),
        "must_not_show": (
            "no rays; the scroll OPEN with broken seals visible; nobody "
            "shrugging or defeated — every face engaged; camera at eye "
            "level across the table, NOT overhead."
        ),
        "scene": (
            "Eye-level across the old table: the opened scroll holds the "
            "middle like bread at a meal, a reader's finger travelling "
            "slow beneath the line, and around it a circle of plain "
            "lamplit faces bent close — labourers' faces, mothers' faces "
            "— people hearing, at last, the very words that outlasted "
            "every expert who could not reach them. Camera level with the "
            "listeners, NOT the overhead framing of the opening shot. ONE "
            "single continuous photograph from one camera — never a "
            "collage, never panels, never a split frame. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b32", "out": "s32-the-seals-hang-broken.jpeg", "seg": "n7b",
        "window": "154.43-158.34", "wide": False, "jesus": False, "ref": False,
        "locks": ['BOOK'],
        "narration": (
            "The blind see. The sealed book does not stay sealed."
        ),
        "must_show": (
            "MACRO close on the scroll's edge: the three wax seals "
            "dangling BROKEN on their loosed dark cords, the parchment's "
            "edge curling open beyond them, lamplight warm on the wax."
        ),
        "must_not_show": (
            "no rays; seals BROKEN and hanging, never whole; no hands in "
            "this frame; a tight macro, NOT the wide table framing of the "
            "earlier shots."
        ),
        "scene": (
            "The row's whole argument in one square inch: the parchment "
            "lies FLAT AND OPEN, filling the lower frame edge to edge — "
            "NO rolled scroll anywhere in this picture. At its near edge "
            "the three wax seals hang VISIBLY SNAPPED — each broken in "
            "half, dangling by slack loosed dark cords OFF the open "
            "parchment's edge, wax crumbs scattered on the old wood "
            "beneath. Warm lamplight on the broken wax, the written lines "
            "running soft-focus into the distance. The hardware of "
            "impossibility, retired. A tight macro framing, deliberately "
            "unlike every earlier wide of the table. ONE single "
            "continuous photograph from one camera — never a collage, "
            "never panels, never a split frame. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b33", "out": "s33-the-plain-man-reads.jpeg", "seg": "n7b",
        "window": "158.34-164.10", "wide": False, "jesus": False, "ref": False,
        "locks": ['BOOK', 'PLAIN'],
        "narration": (
            "When God does the opening, the people everyone had given up "
            "on are the first to understand."
        ),
        "must_show": (
            "the SAME unschooled man from earlier — the locked PLAIN "
            "face, full short dark beard, dark rust tunic — now bent over "
            "the OPEN scroll, reading aloud, astonished joy breaking on "
            "the broad kind face."
        ),
        "must_not_show": (
            "no rays; he is READING and understanding, never shaking his "
            "head now; the same man as the earlier beats — never a "
            "different actor; scroll open with broken seals."
        ),
        "scene": (
            "The callback the whole video was built for: the plain "
            "unschooled man who once shook his head kindly now stands "
            "bent over the OPENED scroll, one broad hand flat on the "
            "parchment, his lips mid-word — reading aloud — while "
            "astonished joy climbs the honest face that once had to say "
            "it could not. Three-quarter view from across the table's "
            "corner, lamplight on the moving lips. ONE single continuous "
            "photograph from one camera — never a collage, never panels, "
            "never a split frame. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r157-b34", "out": "s34-the-erred-come-to-understanding.jpeg", "seg": "kv24",
        "window": "164.38-172.23", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "They also that erred in spirit shall come to understanding, "
            "and they that murmured shall learn doctrine."
        ),
        "must_show": (
            "SCRIPTURE-EXACT: listeners whose faces are CHANGING — "
            "furrowed, guarded faces at the reading easing into "
            "comprehension, heads beginning slow nods; reverse angle "
            "looking FROM the scroll toward the listeners."
        ),
        "must_not_show": (
            "no rays; no scowling caricatures — honest faces mid-thaw; "
            "reverse angle from behind the open scroll, NOT the eye-level "
            "circle framing."
        ),
        "scene": (
            "Reverse angle, shot from just behind the opened scroll "
            "looking outward: a bench of listeners whose faces arrived "
            "furrowed — the murmurers, the ones who wandered — caught "
            "mid-change, the guarded lines easing, one grey head "
            "beginning a slow nod, a younger man's eyes going still and "
            "clear. Understanding arriving not as argument won but as "
            "weather changing. ONE single continuous photograph from one "
            "camera — never a collage, never panels, never a split frame. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b35", "out": "s35-a-promise-with-a-date.jpeg", "seg": "n8",
        "window": "172.51-177.47", "wide": False, "jesus": False, "ref": False,
        "locks": ['BOOK'],
        "narration": (
            "So this was never a story about a book staying shut. It is a "
            "promise with a date on it."
        ),
        "must_show": (
            "the opened scroll on the bare table at MORNING — low raking "
            "gold light across the parchment, the broken seals resting in "
            "the light; the lamps out, the window bright."
        ),
        "must_not_show": (
            "no rays or beams; morning light natural through a window, "
            "lamps extinguished; low angle along the table, NOT overhead "
            "and NOT the macro."
        ),
        "scene": (
            "Morning finds the table: shot low along the wood's grain, "
            "the scroll lies fully UNROLLED end to end — NO rolled "
            "portion anywhere — its open written face stretching away in "
            "raking first-gold window light, every letter-row catching "
            "shadow. Beside it on the sunlit wood the three BROKEN SEAL "
            "HALVES lie detached and spent, cords slack. The lamps are "
            "out, the window bright, the sealed years over — the promise "
            "kept sitting plainly in the sun. ONE single continuous "
            "photograph from one camera — never a collage, never panels, "
            "never a split frame. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r157-b36", "out": "s36-light-reaches-the-room.jpeg", "seg": "n8",
        "window": "177.47-185.33", "wide": True, "jesus": False, "ref": False,
        "locks": ['BOOK', 'PLAIN'],
        "narration": (
            "God said he would do a marvellous work — open what the "
            "experts could not, and hand understanding to the very people "
            "who had wandered."
        ),
        "must_show": (
            "WIDE from the doorway: morning light entering the plain "
            "room, the table and opened scroll at centre, the plain man "
            "and a handful of listeners gathered in the brightness, faces "
            "lit and living."
        ),
        "must_not_show": (
            "no rays or visible beams — just a bright morning-lit room; "
            "the PLAIN man is the same locked face; nobody kneeling to "
            "the scroll — they read it, not worship it."
        ),
        "scene": (
            "Wide from the doorway, the morning walking in ahead of us: "
            "the plain room filled with clean early light, the old table "
            "at its centre carrying the opened scroll, and around it the "
            "small congregation of the given-up-on — the plain man with "
            "his hand on the parchment, an elder, a mother with her child "
            "leaned against her — every face lit the ordinary way a "
            "window lights a face, the whole room reading. The camera "
            "stands in the open doorway with no figure between it and "
            "the table — everyone in profile or three-quarter view, no "
            "figure's back fills the foreground. ONE single "
            "continuous photograph from one camera — never a collage, "
            "never panels, never a split frame. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r157-b37", "out": "s37-it-comes-from-him.jpeg", "seg": "n8",
        "window": "185.33-189.03", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Understanding does not come from the wise. It comes from "
            "him."
        ),
        "must_show": (
            "one face lifted FROM the page TOWARD the bright window — "
            "plain warm window light on the features, gratitude and "
            "comprehension together; nothing supernatural in the frame."
        ),
        "must_not_show": (
            "ABSOLUTE: no rays, no beams, no shining, nothing descending "
            "— ONLY a bright ordinary window and a lit face; not the "
            "plain man — an ordinary listener, so the truth lands on "
            "everyman."
        ),
        "scene": (
            "Close on an ordinary listener — a weathered everyman face — "
            "at the moment his eyes leave the parchment and lift toward "
            "the bright window, the plain daylight full on his features, "
            "and written in them the sentence the narrator is saying: "
            "this did not come from the scholars. Gratitude aimed past "
            "the glass, at the Giver. ONE single continuous photograph "
            "from one camera — never a collage, never panels, never a "
            "split frame. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r157-b38", "out": "s38-will-you-let-him.jpeg", "seg": "n8",
        "window": "189.03-195.58", "wide": False, "jesus": False, "ref": False,
        "locks": ['BOOK'],
        "narration": (
            "So the only question left is the hopeful one: when God "
            "offers to open the book, will you let him?"
        ),
        "must_show": (
            "the opened scroll turned TOWARD THE VIEWER across the near "
            "edge of the table, morning light, the broken seals nearest "
            "the camera — an offered, waiting invitation; no people in "
            "frame."
        ),
        "must_not_show": (
            "no rays; no hands and no people — the offer itself; frontal "
            "framing toward the viewer, NOT the low raking angle and NOT "
            "the macro."
        ),
        "scene": (
            "The last shot faces the audience: the opened scroll lies "
            "turned toward the viewer across the table's near edge, its "
            "unrolled parchment reaching toward the bottom of frame like "
            "an offered hand, broken seals nearest the camera, the "
            "morning light even and kind across the letters — the whole "
            "image one quiet question waiting for whoever is watching to "
            "answer it. ONE single continuous photograph from one camera "
            "— never a collage, never panels, never a split frame. Every "
            "figure has two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "BOOK": "PLACE-REF/book.jpeg",  # build-157-marvellous-work s03-imagine-a-precious-book-clasped (manual)
}
# === end PLACE-PLATES ===

REFS = {
    "PLAIN": "CAST-REF-V2/plain.jpeg",
}
