#!/usr/bin/env python3
"""V2 beat map — row 128, build-128-heart-far-from-me (Matthew 15:1-9; Mark 7:1-13).

COVERAGE: 16 pictures over 90.7 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (KJV):
  Matt 15:1-2 scribes and Pharisees from Jerusalem: "Why do thy
        disciples transgress the TRADITION OF THE ELDERS? for they
        wash not their hands when they eat bread." — a tradition
        added on top of the law, not the law itself.
  Matt 15:8 (Isaiah 29:13) "This people... honoureth me with their
        LIPS; but their HEART IS FAR FROM ME."
  Matt 15:9 "in VAIN they do worship me, teaching for doctrines the
        COMMANDMENTS OF MEN."
  Mark 7:8  "laying aside the commandment of God, ye hold the
        tradition of men."
  Mark 7:10-12 the CORBAN loophole: "Honour thy father and thy
        mother" cancelled by declaring one's money "Corban, that is
        to say, a gift" — freeing a man from helping his parents.
  Mark 7:13 "making the word of God OF NONE EFFECT through your
        tradition."

RENDERING LAWS:
  - THE LEADERS ARE NOT CARTOON VILLAINS (standing complaint-corpus
    law): they are earnest, dignified guardians of tradition —
    scandalized, certain, wrong. No sneering heavies.
  - The disciples' unwashed hands are WORKING HANDS at an honest
    meal — the "offense" must look as innocent as it was.
  - The corban beats (b11/b14) carry the row's moral weight: the
    labelled money pouch and the unhelped AGING PARENTS. The
    parents are rendered with full dignity (rows 44/74/75 class) —
    their need visible, never abject.
  - The scroll imagery (b09/b13) does the doctrine: God's
    commandment scroll SET ASIDE / COVERED by men's rule-scrolls.
    All script indistinct period writing — no readable text.
  - Jesus is calm and level throughout — never contemptuous; b12's
    "not impressed" is stillness, not a sneer.
  - The closing card is SILENT by design (no card.mp3 — CARD_TEXT
    constant in V1 build.py); nothing to ear-check there.

TIME OF DAY ARC (intentional): one clear bright Galilean day
throughout — the confrontation and vignettes in open daylight; the
b16 welcome in warm late gold.

CHANGING CONDITION (kept OUT of the locks): none material — a
single-day confrontation; the vignettes are illustrative asides.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "COURT": (
        "COURT LOCK: the meeting place — a broad flagstone courtyard "
        "by the synagogue, low stone steps, a fig tree at one "
        "corner, bright open daylight. The same courtyard "
        "throughout."
    ),
    "LEADERS": (
        "LEADERS LOCK: the delegation — five scribes and Pharisees "
        "from Jerusalem, dignified older men in fine DEEP BLUE and "
        "CHARCOAL robes with broad fringes and head coverings (no "
        "cream — only Jesus wears cream); earnest, certain, "
        "scandalized — never sneering caricatures. The same five "
        "men throughout."
    ),
    "MEAL": (
        "MEAL LOCK: the disciples' meal — a low table in the "
        "courtyard's shade with flat bread, olives and a water jug; "
        "the diners are weathered working men in earth-toned tunics "
        "of brown, rust and olive (no cream). The same table and "
        "diners throughout."
    ),
    "PARENTS": (
        "PARENTS LOCK: the aging parents — a stooped elderly father "
        "with a white beard and a small elderly mother with a "
        "head-shawl, in patched but clean DARK EARTH-BROWN clothes "
        "(no cream); rendered always with full dignity. The same "
        "couple throughout."
    ),
}

REF = True

# STALE-V1 fix (audio lane, 2026-08-11): the story was re-recorded (8 newer mp3s,
# −1.778s vs the old V1 mp4) but never re-rendered. Rebuild the track from the
# current V1 segment mp3s at the extract_beats offsets instead of copying the stale
# V1 mp4's AAC. Re-voices nothing ($0). The closing question card is SILENT (no
# card.mp3) — v2_assemble skips it and pads the tail. See QC.md.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r128-b01", "out": "s01-some-of-the-religious-leaders.jpeg", "seg": "n1",
        "window": "0.28-2.90", "wide": True, "jesus": True, "ref": REF,
        "locks": ["COURT", "LEADERS"],
        "narration": "Some of the religious leaders came to Jesus with a complaint.",
        "must_show": "the arrival — the five-man delegation crossing the courtyard toward Jesus with the complaint already on their faces; formal, earnest, certain.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the leaders DIGNIFIED — no sneers; exactly five of them.",
        "scene": (
            "The complaint arrives in formation, the camera "
            "looking past the delegation's robed backs as they "
            "cross the flagstones: five dignified men from "
            "Jerusalem — fine deep-blue robes, broad fringes, "
            "the unhurried walk of men who have never once been "
            "wrong in public — bearing down on Jesus where he "
            "stands in the courtyard's bright morning, the "
            "complaint already sitting on their earnest faces "
            "like a verdict that only needs reading out. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r128-b02", "out": "s02-they-had-seen-his-disciples.jpeg", "seg": "n1",
        "window": "2.90-11.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["COURT", "MEAL", "LEADERS"],
        "narration": (
            "They had seen his disciples eating with unwashed hands — "
            "breaking not God's law, but a tradition the elders had added on "
            "top of it."
        ),
        "must_show": "the offense observed — the disciples at their low table breaking bread with honest work-worn hands, at ease; at the courtyard's edge, two of the leaders watching with visible disapproval.",
        "must_not_show": "no halo; the meal INNOCENT — dusty working hands, good appetite, nothing furtive; the watchers earnest, not sneering.",
        "scene": (
            "The scandal, at the scene of the crime: around the "
            "low shaded table the disciples eat like the working "
            "men they are — flat bread torn and passed, olives "
            "by the handful, road dust still on their honest "
            "hands and nobody troubled about it — while at the "
            "courtyard's sunlit edge two of the fine-robed "
            "watchers stand very still, taking in the unwashed "
            "fingers on the bread with the pained attention of "
            "men watching a rule they love being cheerfully, "
            "innocently ignored. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r128-b03", "out": "s03-to-them-that-was-a.jpeg", "seg": "n1",
        "window": "11.37-13.84", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEADERS"],
        "narration": "To them, that was a scandal.",
        "must_show": "the scandal registered — close on one leader's genuinely appalled face, a hand half-raised toward the sight; sincere shock, not theatre.",
        "must_not_show": "no halo; the shock SINCERE — he truly believes the fence protects the law.",
        "scene": (
            "The offense lands on a sincere face: close on the "
            "eldest of the delegation, his brows drawn up in "
            "genuine appalled disbelief, one ringed hand "
            "half-risen toward the offending table as if to "
            "stop the bread mid-air — no theatre in it, no "
            "performance: a man watching what he honestly "
            "believes is a fence around God's law being "
            "climbed over at lunch, and hurting about it the "
            "way sincere men hurt. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r128-b04", "out": "s04-he-answered-them-with-words.jpeg", "seg": "n2",
        "window": "16.48-20.77", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COURT", "LEADERS"],
        "narration": "He answered them with words the prophet Isaiah had written long before.",
        "must_show": "the answer begun — Jesus calm before the delegation, beginning to speak; the authority of an old prophet's words gathering in the quiet.",
        "must_not_show": "no halo, glare or rim-light on Jesus; his calm ABSOLUTE — no heat, no contempt.",
        "scene": (
            "The answer reaches back seven centuries before it "
            "reaches them: Jesus stands calm in the bright "
            "courtyard facing the five, letting the pause do "
            "its work — and when he begins, the cadence that "
            "comes is not debate but recitation, the old "
            "prophet's words arriving through him with the "
            "weight of something written long before anyone "
            "present was born, aimed then, and landing now, on "
            "exactly the same address. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r128-b05", "out": "s05-this-people-honoureth-me-with.jpeg", "seg": "j1",
        "window": "21.35-25.65", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "This people honoureth me with their lips, but their heart is "
            "far from me."
        ),
        "must_show": "SCRIPTURE-EXACT: the verse pictured — a worshiper in fine robes praying grandly, lips moving with perfect words, while his eyes are cold and elsewhere; lips near, heart far, in one face.",
        "must_not_show": "no halo; the distance in the EYES — correct mouth, absent gaze; sincere-looking, hollow.",
        "scene": (
            "The verse has a portrait: a worshiper in fine "
            "robes stands at prayer in the temple court's "
            "light, hands lifted just so, lips moving through "
            "words polished by a lifetime of correct "
            "repetition — and above the flawless mouth, the "
            "eyes: cold, elsewhere, running some private "
            "ledger miles from the words — honour performed at "
            "the lips while the heart is out of the country, "
            "the whole diagnosis visible in the two inches "
            "between a man's mouth and his gaze. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r128-b06", "out": "s06-howbeit-in-vain-do-they.jpeg", "seg": "j1",
        "window": "25.65-31.85", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Howbeit in vain do they worship me, teaching for doctrines the "
            "commandments of men."
        ),
        "must_show": "SCRIPTURE-EXACT: the commandments of men — an elaborate array of ritual washing vessels, and hands performing the ceremonial pour with fastidious precision; the added rules in full pomp.",
        "must_not_show": "no halo; the vessels PERIOD-TRUE (stone and bronze); the precision fastidious, the frame beautiful and hollow.",
        "scene": (
            "The commandments of men gleam beautifully: an "
            "array of ritual washing vessels stands ranked on "
            "the stone ledge — stone jars, bronze cups, each "
            "for its prescribed stage — and over them a pair "
            "of hands performs the ceremonial pour with "
            "fastidious, practised precision, water measured "
            "to the knuckle, fingers angled by the book — "
            "except the book is men's: a liturgy of additions, "
            "performed immaculately, achieving exactly what "
            "the verse says such worship achieves. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r128-b07", "out": "s07-you-can-say-every-right.jpeg", "seg": "n3",
        "window": "33.37-38.83", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "You can say every right word and keep every custom and still be "
            "a thousand miles away on the inside."
        ),
        "must_show": "the interior distance — the grand worshiper again from b05, and through the colonnade behind him a vast far horizon; the thousand miles rendered as composition.",
        "must_not_show": "no halo; the SAME worshiper as b05 (face continuity); the far horizon doing the metaphor.",
        "scene": (
            "The distance gets measured in the frame itself: "
            "the fine-robed worshiper stands at his correct "
            "prayers in the near ground — and behind him, "
            "through the colonnade's open arches, the land "
            "runs out and out to a horizon so far it hazes, "
            "ridge after ridge into blue distance — a man "
            "standing two feet from the altar and a thousand "
            "visible miles from anywhere, the geography of the "
            "far heart laid out in plain air behind his "
            "faultless devotions. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r128-b08", "out": "s08-he-was-never-counting-the.jpeg", "seg": "n3",
        "window": "38.83-43.96", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COURT"],
        "narration": (
            "He was never counting the handwashing. He was looking for what "
            "stood behind it."
        ),
        "must_show": "the deeper look — close on Jesus, his gaze steady PAST raised ritual-washing hands in the near frame, to the man behind them; the true object of his attention unmistakable.",
        "must_not_show": "no halo, glare or rim-light on Jesus; his focus visibly BEYOND the hands — on the person.",
        "scene": (
            "His attention was always aimed past the ceremony: "
            "in the near frame a pair of hands performs the "
            "washing, correct to the last drop — and beyond "
            "them, in focus where the hands are not, Jesus's "
            "steady eyes look straight through the ritual to "
            "the man performing it — not counting rinses, "
            "never counting rinses — reading the heart that "
            "stands behind the hands with the level patience "
            "of someone who has only ever been interested in "
            "one thing about worship. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r128-b09", "out": "s09-for-laying-aside-the-commandment.jpeg", "seg": "j2",
        "window": "44.45-49.32", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "For laying aside the commandment of God, ye hold the tradition "
            "of men."
        ),
        "must_show": "SCRIPTURE-EXACT: the swap — a great worn Torah scroll SET ASIDE on a high shelf in shadow, while bright new rule-scrolls are held up and consulted in the light; the exchange in one frame.",
        "must_not_show": "no halo; all script INDISTINCT period writing; the old scroll dignified in its neglect.",
        "scene": (
            "The trade is displayed in shelf-space and light: "
            "high in the alcove's shadow the great worn "
            "commandment scroll lies SET ASIDE — venerable, "
            "heavy, dust beginning on its rollers — while down "
            "in the working light a cluster of hands holds up "
            "the bright new rule-scrolls, crisp and consulted "
            "and multiplying — the word of God laid respectfully "
            "out of reach and the traditions of men held close, "
            "the whole exchange conducted in the vocabulary of "
            "reverence. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r128-b10", "out": "s10-then-he-gave-them-an.jpeg", "seg": "n4",
        "window": "50.85-56.93", "wide": False, "jesus": False, "ref": False,
        "locks": ["PARENTS"],
        "narration": (
            "Then he gave them an example that exposed the whole game. God "
            "had said, Honour thy father and thy mother."
        ),
        "must_show": "the commandment's real content — the aging parents at their humble door in warm light, worn and dignified; what honouring was always about.",
        "must_not_show": "no halo; the parents' dignity TOTAL — worn clothes clean, faces kind; need visible, never abject.",
        "scene": (
            "The commandment in question has faces: at the "
            "door of a small worn house the aging couple stand "
            "in the warm light — the father stooped over his "
            "stick with a white beard and steady eyes, the "
            "mother small in her head-shawl, patched clothes "
            "clean, hands that raised children folded quiet — "
            "honour thy father and thy mother, God had said, "
            "and this is what the sentence was made of: two "
            "real people, growing old at a real door, owed. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r128-b11", "out": "s11-but-their-custom-let-a.jpeg", "seg": "n4",
        "window": "56.93-66.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["PARENTS"],
        "narration": (
            "But their custom let a man label his money a gift promised to "
            "the temple — and use that label as an excuse to give nothing to "
            "his own aging parents."
        ),
        "must_show": "the loophole enacted — a well-dressed man knotting a temple-token tag onto his fat money pouch, while at distance behind him his parents stand at their door, unhelped; the label and the cost in one frame.",
        "must_not_show": "no halo; ACTION-LOGIC — the tagging of the pouch unmistakable; the parents at far ground, dignity intact, visibly outside his attention.",
        "scene": (
            "The loophole is tied on with a neat knot: in the "
            "near ground a well-dressed man cinches a small "
            "temple-token tag onto the neck of his fat money "
            "pouch — dedicated, the label says; promised; "
            "untouchable — his face easy with the comfort of a "
            "technicality — while far up the lane behind him, "
            "small and unvisited at their worn door, the two "
            "old people the money was commanded toward stand "
            "in the same warm light as before, holding "
            "everything except help. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r128-b12", "out": "s12-jesus-was-not-impressed-by.jpeg", "seg": "n2",
        "window": "14.41-16.48", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COURT", "LEADERS"],
        "narration": "Jesus was not impressed by the show.",
        "must_show": "the stillness — Jesus regarding the delegation levelly, unmoved; their fine robes and certainty reflected in a gaze that goes straight through them.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NOT a sneer — level, quiet, entirely unimpressed stillness.",
        "scene": (
            "The show plays to its first unmoved audience: the "
            "five stand arranged in their fine fringes and "
            "certainty, the complaint delivered — and Jesus "
            "simply looks at them, level and quiet, nothing in "
            "his face rising to meet the performance — no "
            "anger, no scorn, just the particular stillness of "
            "a man watching a production whose every prop and "
            "line he can see past, waiting for the actors to "
            "finish so the truth can have the floor. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r128-b13", "out": "s13-making-the-word-of-god.jpeg", "seg": "j3",
        "window": "66.94-71.54", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Making the word of God of none effect through your tradition, "
            "which ye have delivered."
        ),
        "must_show": "SCRIPTURE-EXACT: the cancelling — the bright rule-scroll laid directly ON TOP of the great commandment scroll, covering its writing entirely; none effect, in one image.",
        "must_not_show": "no halo; script INDISTINCT both scrolls; the covering complete — not one line of the under-scroll readable.",
        "scene": (
            "The verdict is staged on a reading table: the "
            "great old commandment scroll lies open — and "
            "directly on top of it, unrolled with care, the "
            "men's bright rule-scroll lies covering it edge to "
            "edge, the new writing lying flat over the old "
            "until not one line beneath shows through — "
            "nothing burned, nothing torn, everything "
            "reverent: the word of God rendered of none "
            "effect by the simple weight of what men laid "
            "over it. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r128-b14", "out": "s14-they-had-used-a-rule.jpeg", "seg": "n5",
        "window": "73.04-78.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["PARENTS"],
        "narration": (
            "They had used a rule about God to cancel a command from God — "
            "turning devotion into a loophole."
        ),
        "must_show": "the cost in faces — close on the aging parents: dignity whole, need real, the empty doorstep where help never came; the loophole's price paid by the people God named.",
        "must_not_show": "no halo; NEVER abject — worn and unbroken; the emptiness of the doorstep telling the cost.",
        "scene": (
            "What a loophole costs is always paid by somebody: "
            "close on the two old faces at their door — the "
            "father's steady eyes gone patient the way eyes go "
            "when they have stopped watching the lane for a "
            "visitor, the mother's small hands folded around "
            "nothing — their doorstep swept, their dignity "
            "whole, their table thin — the exact two people a "
            "command from God had named, invoiced instead by a "
            "rule about God, and bearing it without one word "
            "of complaint. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r128-b15", "out": "s15-that-was-his-warning-never.jpeg", "seg": "n5",
        "window": "78.68-84.56", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "That was his warning: never let the outside of religion grow so "
            "loud that it drowns out the heart of it."
        ),
        "must_show": "outside vs heart — foreground: the gleaming ranked ritual vessels in full pomp; through a doorway beyond: a plain man quietly steadying his old father's arm; the loud and the true in one frame.",
        "must_not_show": "no halo; the quiet scene SMALL and warm through the doorway — the composition's whole argument.",
        "scene": (
            "The warning is composed in one deep frame: up "
            "front the outside of religion gleams at full "
            "volume — the ranked washing vessels, the polished "
            "bronze, the ceremony's beautiful loud hardware "
            "filling the foreground — while through the plain "
            "doorway beyond, small and easily missed, a man in "
            "a work tunic steadies his old father's arm over "
            "the threshold stone — the heart of the whole "
            "thing, no louder than it ever is, waiting to be "
            "noticed past the shine. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r128-b16", "out": "s16-he-would-always-rather-have.jpeg", "seg": "n5",
        "window": "84.56-90.36", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COURT"],
        "narration": (
            "He would always rather have an honest heart than a flawless "
            "performance. Come to him with the real one."
        ),
        "must_show": "the closing welcome — in warm late gold, Jesus receiving a plain dusty ordinary man with open warmth, hands clasped; the real heart welcomed exactly as it is.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the man ORDINARY — road dust, imperfect, entirely welcome.",
        "scene": (
            "What he always wanted walks up at the end of the "
            "day: a plain man, road-dusty and empty-handed, "
            "nothing correct about him except that he came — "
            "and Jesus receives him in the warm late gold with "
            "both hands clasping the offered one, the welcome "
            "on his face complete and immediate — no "
            "performance requested, no washing checked, the "
            "honest heart arriving in its work clothes and "
            "being taken, exactly as it is, which is the whole "
            "invitation of the whole story. Every figure has "
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
