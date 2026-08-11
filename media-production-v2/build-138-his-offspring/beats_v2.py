#!/usr/bin/env python3
"""V2 beat map — row 138, build-138-his-offspring (Acts 17:22-31).

COVERAGE: 10 pictures over 46.7 s = 4.7 s/picture (matches the library density).

SCRIPTURE FACTS (Acts 17 KJV):
  17:16 Athens "wholly given to idolatry" — statues everywhere.
  17:23 "I found an altar with this inscription, TO THE UNKNOWN GOD.
        Whom therefore ye ignorantly worship, him declare I unto you."
  17:24-27 the God that made the world... "he be NOT FAR from every
        one of us."
  17:28 "For IN HIM WE LIVE, AND MOVE, AND HAVE OUR BEING; as
        certain also of YOUR OWN POETS have said, For we are also
        HIS OFFSPRING."
  17:30 "the times of this ignorance God WINKED AT; but now
        commandeth all men every where to REPENT."
  Setting: the Athens agora and the AREOPAGUS (Mars Hill), marble
        and idols, philosophers and passers-by.

RENDERING LAWS:
  - THE ALTAR INSCRIPTION IS NEVER LEGIBLE TEXT: worn Greek letters
    suggested and weathered past reading (the no-readable-text law);
    the narration carries the words. The altar itself is PLAIN and
    small against the ornate idols — its humility is the picture.
  - The idols/statues are classical marble — beautiful, cold,
    varied; never grotesque; the contrast is warm-living vs
    cold-stone, not good-vs-monster.
  - PAUL: one locked look (traditional): compact and wiry, balding
    with a fringe of dark hair, full pointed dark beard, keen deep
    eyes — a tentmaker's strong hands.
  - The Athenians are curious, cultured, divided — some leaning in,
    some smiling in polite scorn (per Acts 17:32); never a mob,
    never cartoon pagans.
  - b05's in-him-we-live is ORDINARY LIFE in the agora — walking,
    trading, children running — everyday motion as the sermon.

TIME OF DAY ARC (intentional): bright Attic marble-light morning
through the sermon; the closing pair in warm golden late light —
the nearness rendered as light lying close on everything.

CHANGING CONDITION (kept OUT of the locks): the listeners —
gathering, then divided (some scoffing, some drawn); the altar —
overlooked in shadow early, warm-lit at the close.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row).
LOCKS = {
    "ATHENS": (
        "ATHENS LOCK: the Athens agora below the Areopagus — pale "
        "marble colonnades and steps, classical statues of many "
        "gods on plinths, the rocky Mars Hill rising with the "
        "Acropolis beyond; bright Attic light. The same stones and "
        "skyline throughout."
    ),
    "PAUL": (
        "PAUL LOCK: Paul is the same man in every shot — compact "
        "and wiry, about fifty, balding with a fringe of dark hair, "
        "a full pointed dark beard, keen deep-set eyes, in a plain "
        "DARK RUST-BROWN travel robe (never cream, never white); a "
        "tentmaker's strong hands; earnest fire without anger."
    ),
    "ALTAR": (
        "ALTAR LOCK: the unknown-god altar — a small PLAIN "
        "weathered stone altar on a worn plinth, its short "
        "inscription eroded to illegible Greek traces, standing "
        "modest among the ornate statues. The same altar "
        "throughout."
    ),
    "ATHENIANS": (
        "ATHENIANS LOCK: the listeners — cultured Athenians in "
        "draped himations of grey, ochre and deep blue (no cream), "
        "philosophers with staffs, merchants, a few women and "
        "children at the edges; curious, varied faces, never "
        "uniform, never a mob."
    ),
}

REF = True

# STALE-V1 fix (audio lane, 2026-08-11): rebuild the audio track from the V1
# segment mp3s at the extract_beats offsets instead of copying the stale V1
# mp4's AAC (which fails assert_v1_final_is_current). Re-voices nothing ($0).
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r138-b01", "out": "s01-paul-stood-in-the-middle.jpeg", "seg": "n0a",
        "window": "0.28-5.37", "wide": True, "jesus": False, "ref": False,
        "locks": ["ATHENS", "PAUL"],
        "narration": (
            "Paul stood in the middle of Athens, surrounded by statues to "
            "every god they could think of —"
        ),
        "must_show": "the forest of gods — Paul small at the agora's centre, ringed by marble statues on plinths in every direction; one warm living man amid cold beautiful stone.",
        "must_not_show": "no halo; the statues CLASSICAL and varied, beautiful not grotesque; Paul's aliveness the contrast.",
        "scene": (
            "One warm body stands in a forest of cold ones, "
            "the camera looking past the statues' marble backs "
            "into the square: Paul at the agora's centre, "
            "compact and travel-worn, turning slowly on his "
            "heel — and in every direction the marble "
            "population watches back: gods of war and grain "
            "and sea and hearth, beautiful, blank-eyed, "
            "plinth after plinth to the colonnades — a city "
            "that answered every question with a statue, "
            "being paced off by the one man in it carrying "
            "an answer that breathes. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r138-b02", "out": "s02-and-one-altar-that-simply.jpeg", "seg": "n0b",
        "window": "5.95-9.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["ALTAR", "ATHENS"],
        "narration": "and one altar that simply said, To the unknown God.",
        "must_show": "the humble altar — the small plain weathered altar in the shadow of ornate statues, its inscription eroded to ILLEGIBLE traces; the city's one honest confession.",
        "must_not_show": "ABSOLUTE: no legible text — worn Greek traces only; the altar's plainness against the marble pomp.",
        "scene": (
            "The most honest monument in Athens is the "
            "humblest: tucked in the shadow between two "
            "ornate plinths stands a small plain altar of "
            "weathered stone — no gilding, no sculpture, its "
            "short inscription worn down to faint illegible "
            "traces of Greek — the city's one open admission, "
            "carved and then half-forgotten: that after "
            "naming every god they could imagine, something "
            "real remained that no statue had managed to "
            "hold. No people are needed in this frame."
        ),
    },
    {
        "id": "v2-r138-b03", "out": "s03-he-told-them-they-were.jpeg", "seg": "n1",
        "window": "9.84-12.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["ATHENS", "PAUL", "ATHENIANS"],
        "narration": "He told them they were already closer than they knew.",
        "must_show": "the opening — Paul's open hand toward the altar, face warm toward the gathering listeners; the sermon starting from THEIR monument, not against it.",
        "must_not_show": "no halo; nothing combative — Paul building on their own stone; the listeners curious.",
        "scene": (
            "The sermon starts by agreeing with them: Paul's "
            "open hand extends toward the little weathered "
            "altar while his face turns warm to the gathering "
            "Athenians — closer than you KNOW, the gesture "
            "says: your own hands carved the doorway — no "
            "torch taken to their city, no statue toppled, "
            "just a travelling tentmaker picking up the one "
            "stone Athens got right and holding it where its "
            "carvers could finally see what they had built. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r138-b04", "out": "s04-the-god-left-unnamed-made.jpeg", "seg": "n1",
        "window": "12.78-17.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["ATHENS", "PAUL"],
        "narration": (
            "The God they'd left unnamed made the whole world, and He is not "
            "far from any of us."
        ),
        "must_show": "the scale claim — Paul's arm sweeping up past the Acropolis to the whole sky and horizon; the unnamed God's workmanship overarching the man-made marble.",
        "must_not_show": "no halo, no figure in the sky — the sweep from marble to sky carries the claim.",
        "scene": (
            "The résumé of the unnamed God is hanging over "
            "the city: Paul's arm sweeps up past the "
            "colonnades, past the Acropolis crown, to the "
            "whole enormous sky and the sea-line beyond the "
            "hills — THIS is his workmanship, the arc says, "
            "the light, the air, the turning world your "
            "marble stands on — and then the arm comes down "
            "gently toward the listeners themselves: and he "
            "is not far — not far from any single one of "
            "you. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r138-b05", "out": "s05-in-him-paul-said-we.jpeg", "seg": "n2",
        "window": "18.03-21.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["ATHENS", "ATHENIANS"],
        "narration": "In Him, Paul said, we live and move and have our being.",
        "must_show": "the verse as ordinary life — the agora in full motion: traders trading, children running, water carried, elders talking; everyday aliveness as the sermon's evidence.",
        "must_not_show": "no halo; nothing staged — the ordinary morning itself; varied faces, no clones.",
        "scene": (
            "The proof-text is the morning itself: the agora "
            "runs at full ordinary tilt — a trader's arms "
            "wide over his olives, two children chasing "
            "between the plinths, a woman balancing her "
            "water-jar through the crowd, old men laughing "
            "on the steps — living, moving, being, every "
            "verb of the verse performed unawares by a "
            "square full of people doing Tuesday — all of it "
            "held, said the tentmaker, IN HIM, like fish "
            "discussing whether water exists. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r138-b06", "out": "s06-he-even-quoted-their-own.jpeg", "seg": "n2",
        "window": "21.59-24.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["ATHENS", "PAUL", "ATHENIANS"],
        "narration": "He even quoted their own poets: we are His children.",
        "must_show": "the meeting-them — Paul's hand open toward a startled philosopher-listener, honouring the man's own tradition; the poet's line handed back as gospel.",
        "must_not_show": "no halo; the philosopher's surprise RESPECTFUL — his own books quoted rightly; no mockery either way.",
        "scene": (
            "The preacher reaches into their own library: "
            "Paul's hand opens toward a grey philosopher at "
            "the ring's edge — YOUR poets, he says, your "
            "own — and gives the man's own hexameters back "
            "to him with the meaning lit: we are his "
            "OFFSPRING — the philosopher's staff going still, "
            "his practiced skepticism caught off guard by "
            "the strange courtesy of a Jew from Tarsus "
            "quoting Aratus rightly, and aiming the line "
            "closer to home than its author ever dared. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r138-b07", "out": "s07-for-in-him-we-live.jpeg", "seg": "p1",
        "window": "25.56-33.22", "wide": False, "jesus": False, "ref": False,
        "locks": ["ATHENS", "PAUL", "ATHENIANS"],
        "narration": (
            "For in him we live, and move, and have our being; as certain "
            "also of your own poets have said, For we are also his "
            "offspring."
        ),
        "must_show": "SCRIPTURE-EXACT: the oration's height — Paul on the Areopagus rock, arms wide, the listeners ringed below on the steps; the sermon at full sail.",
        "must_not_show": "no halo; his fire EARNEST, never angry; the ring varied — leaners-in and polite skeptics both.",
        "scene": (
            "Mars Hill gets the sermon it will be named for: "
            "Paul on the bare rock outcrop with his arms "
            "spread wide, the rust-brown robe taking the "
            "wind, the words rolling down over the ringed "
            "listeners on the steps below — in him we LIVE, "
            "and MOVE, and have our BEING — the little "
            "tentmaker at full sail above the marble city, "
            "preaching its own poets back to it with the "
            "missing Name restored, while the Acropolis "
            "listens over his shoulder. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r138-b08", "out": "s08-the-unknown-god-was-never.jpeg", "seg": "n4",
        "window": "42.12-44.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["ALTAR"],
        "narration": "The unknown God was never unknown to Him.",
        "must_show": "the altar transfigured by light — the same plain altar now in warm golden late light, its shadow-corner bright; known all along.",
        "must_not_show": "ABSOLUTE: no legible text still; the CHANGE is the light — same stone, same traces, warm now.",
        "scene": (
            "The little altar gets the day's best light: the "
            "same plain weathered stone that stood in shadow "
            "all morning now takes the warm gold of late "
            "afternoon full on its face — the eroded traces "
            "soft in the raking light, the humble plinth "
            "gilded like an honoured guest — unknown, said "
            "the carving, and the light lying on it answers "
            "what Paul answered: unknown only from one "
            "side; from the other side, known, named, and "
            "never once out of sight. No people are needed "
            "in this frame."
        ),
    },
    {
        "id": "v2-r138-b09", "out": "s09-god-overlooked-the-times-of.jpeg", "seg": "n3",
        "window": "34.75-41.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["ATHENS", "PAUL", "ATHENIANS"],
        "narration": (
            "God overlooked the times of ignorance before, Paul said — but "
            "now He commands all men everywhere to repent."
        ),
        "must_show": "the turn to earnest — Paul's gentle raised finger, gravity arriving; the ring DIVIDED per Acts: some leaning in changed, others smiling polite scorn and turning away.",
        "must_not_show": "no halo; the division HONEST — scorners polite, not cartoonish; the drawn ones genuinely drawn.",
        "scene": (
            "The comfortable lecture turns into a summons: "
            "Paul's finger rises gently and the gravity "
            "arrives — the winking at ignorance is OVER; "
            "now, all men, everywhere: repent — and the ring "
            "divides where every such ring divides: two "
            "philosophers exchanging their thin amused "
            "smiles and gathering their himations to go, "
            "while nearer the rock a young man and an older "
            "woman lean in with the unmistakable stillness "
            "of people who have just heard their own name "
            "called. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r138-b10", "out": "s10-he-had-been-near-the.jpeg", "seg": "n4",
        "window": "44.47-46.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["ATHENS"],
        "narration": "He had been near the whole time.",
        "must_show": "the closing nearness — the whole marble city in warm close golden light, every stone and street and far figure lying inside the same nearness; light as presence.",
        "must_not_show": "no halo, no figure — the closeness of the LIGHT carries the sentence.",
        "scene": (
            "The sermon's last word is written in the light "
            "over the city: golden evening lies close on "
            "everything — on the colonnades and the "
            "statue-crowded square, on the little plain "
            "altar, on the far small figures crossing for "
            "home — not a distant light but a NEAR one, "
            "resting on every surface like a hand that was "
            "never lifted away — the unknown God's oldest "
            "habit, visible at last for what it always was: "
            "presence, near, the whole time. No people are "
            "distinguishable in this frame."
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
