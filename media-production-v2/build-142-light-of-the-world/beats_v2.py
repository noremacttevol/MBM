#!/usr/bin/env python3
"""V2 beat map — row 142, build-142-light-of-the-world (John 8:12; John 9).

COVERAGE: 10 pictures over 52.7 s = 5.3 s/picture (matches the library density).

SCRIPTURE FACTS (KJV):
  John 8:12 (in the temple treasury, the feast's great lamps near):
        "I AM THE LIGHT OF THE WORLD: he that followeth me shall not
        walk in darkness, but shall have the LIGHT OF LIFE."
  John 9:5 (before healing the man born blind): "As long as I am in
        the world, I am the light of the world."
  John 9:34-35 the healed man CAST OUT by the leaders — "and when
        Jesus HEARD that they had cast him out... he FOUND HIM."
  Setting: the temple courts (the build-06 family), then the streets
        of Jerusalem for the John 9 thread.

RENDERING LAWS:
  - ALL LIGHT IS PHYSICAL (a light row, doubly binding): the temple's
    great festival lampstands with real flames, lanterns, sunrise —
    never a light effect on any person; never the drift words.
  - THE BORN-BLIND MAN IS ROW 63's MAN — his lock below is
    BYTE-IDENTICAL to build-63's BLINDMAN (same face, same patched
    rust-brown tunic; eyes milk-pale before, clear deep brown
    after). Face-board against build-63.
  - The John 9 clay-anointing (b08) is DISCREET like row 136's
    moistening: posture only — Jesus's fingers at the closed lids,
    earth-dust on his fingertips; nothing clinical.
  - The casting-out (b09) is cold dismissal, not violence — turned
    backs and a pushed-away gesture; and the frame's WEIGHT is
    Jesus arriving to find him.
  - The night frames (b05/b06) keep the dark REAL — the light does
    not pretend the night is harmless; the road genuinely dark
    beyond the lantern's reach.

TIME OF DAY ARC (intentional): the temple declaration in bright
day with the great lamps burning (festival lamps, deliberate); the
guttering-lamp and walking-light vignettes at TRUE NIGHT by design;
the John 9 thread in day; the close at sunrise — the healed man's
first.

CHANGING CONDITION (kept OUT of the locks): the blind man's eyes —
milk-pale, then clear deep brown; the night road — dark, then
walked through.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags. BLINDMAN is
# byte-identical to build-63.
LOCKS = {
    "TEMPLE": (
        "TEMPLE LOCK: the temple courts — broad pale limestone "
        "courts with great columned porticoes, wide steps, morning "
        "light on honey-coloured stone; in the treasury court, the "
        "great golden festival LAMPSTANDS with real burning flames. "
        "The same courts throughout."
    ),
    "BLINDMAN": (
        "BORN-BLIND MAN LOCK: the man is the same in every shot — about "
        "thirty-five, lean and alert, with a strong intelligent face, "
        "unruly black hair, a short dark beard and quick expressive "
        "hands that read the world. He wears a patched DARK RUST-BROWN "
        "tunic with a rope belt and a worn DARK GREY shoulder cloth "
        "(never cream, never white). His face is shown clearly and "
        "with full dignity in every state — the EYES are per-beat: "
        "milk-pale before Siloam, clear deep brown after."
    ),
    "NIGHTROAD": (
        "NIGHTROAD LOCK: the night road — a dark country road under "
        "deep blue night, dry-stone walls, the dark real and thick "
        "beyond any lantern's reach; every light physical. The same "
        "road throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r142-b01", "out": "s01-jesus-stood-among-the-temple.jpeg", "seg": "n0",
        "window": "0.28-6.77", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TEMPLE"],
        "narration": (
            "Jesus stood among the temple courts and spoke into the noise of "
            "the crowd. He did not offer another rule for finding God."
        ),
        "must_show": "the setting — Jesus standing in the busy treasury court, the crowd's noise and motion around him, the great festival lampstands burning; one still point in the din.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the lamps' flames PHYSICAL; the crowd varied and busy.",
        "scene": (
            "One still voice sets up in the loudest court, the "
            "camera looking past the moving crowd's backs into "
            "the treasury: pilgrims streaming, money changing, "
            "voices ringing off the honey stone — and amid the "
            "din Jesus stands still beside the great golden "
            "festival lampstands with their real crowns of "
            "flame, waiting for the noise to make room — a "
            "teacher carrying no new rule, no added scroll, no "
            "extra step for finding God: carrying, instead, "
            "only himself. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r142-b02", "out": "s02-he-offered-himself.jpeg", "seg": "n0",
        "window": "6.77-8.64", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE"],
        "narration": "He offered himself.",
        "must_show": "the offer — close on Jesus, hand flat at his own chest; the offer personal and total; the lamp-flames warm behind.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hand at the CHEST — himself, nothing else.",
        "scene": (
            "The offer on the table is the speaker: close on "
            "Jesus with his hand laid flat at his own chest, "
            "the great lamps' warm flames standing behind him "
            "in the court — not a method, not a map, not a "
            "membership: HIMSELF, extended to a crowd that "
            "came shopping for rules — the oldest exchange "
            "in the gospel offered again in the treasury, of "
            "all courts: everything, for everyone, at the "
            "price of following. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r142-b03", "out": "s03-i-am-the-light-of.jpeg", "seg": "j1",
        "window": "9.54-16.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE"],
        "narration": (
            "I am the light of the world: he that followeth me shall not "
            "walk in darkness, but shall have the light of life."
        ),
        "must_show": "SCRIPTURE-EXACT: the declaration — Jesus beside the great burning lampstands, arms opening as the I AM lands; the festival lamps his visual aid, their flames physical.",
        "must_not_show": "ABSOLUTE: no light effect on him — the lamps burn beside him, not from him; the claim carried by words and stance.",
        "scene": (
            "He makes the claim standing next to the runner-"
            "up: beside the treasury's great golden "
            "lampstands — the festival's pride, flames "
            "crowning their branches — Jesus opens his arms "
            "and takes the title past them: I am the light "
            "OF THE WORLD — not of one feast, one court, one "
            "night of celebration: of the world, and of "
            "life — the great lamps burning on gamely beside "
            "a man who has just, in one sentence, outshone "
            "the entire lighting budget of the temple. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r142-b04", "out": "s04-not-a-lamp-that-burns.jpeg", "seg": "n1",
        "window": "17.84-19.37", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Not a lamp that burns out.",
        "must_show": "the contrast object — a clay lamp guttering to its end: flame down to a blue-edged flicker, wick smoking; the kind of light that fails.",
        "must_not_show": "no halo; the dying flame HONEST — oil spent, night pressing at the frame's edges.",
        "scene": (
            "Every other light has this in its future: a "
            "clay lamp on a shelf guttering down to the end "
            "of its oil — the flame shrunk to a blue-edged "
            "flicker, the wick beginning its thin line of "
            "smoke, the room's corners already returning to "
            "dark — the honest limitation of every lamp, "
            "lantern, and festival candelabrum ever lit: "
            "they are all of them borrowed light, and the "
            "loan always comes due before morning. No "
            "people are needed in this frame."
        ),
    },
    {
        "id": "v2-r142-b05", "out": "s05-a-light-that-walks-with.jpeg", "seg": "n1",
        "window": "19.37-26.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["NIGHTROAD"],
        "narration": (
            "A light that walks with you, so you're never feeling your way "
            "blind. It does not pretend the night is harmless."
        ),
        "must_show": "the walking light — on the truly dark road, a lantern-bearer walking BESIDE a traveller, their two figures sharing the lantern's ring; the dark REAL beyond it.",
        "must_not_show": "no halo; the dark genuinely DARK past the ring — the light does not deny the night; the two walk together.",
        "scene": (
            "The better kind of light has legs: on the deep "
            "blue night road two figures walk inside one "
            "lantern's warm ring — the bearer holding it low "
            "and steady, the traveller matching his stride, "
            "their shadows swinging together on the walls — "
            "and past the ring's edge the night stands thick "
            "and real, un-pretended, full of everything "
            "night is full of — the light making no speech "
            "about the dark being harmless: just walking "
            "through it, beside you, lit. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r142-b06", "out": "s06-it-gives-you-someone-to.jpeg", "seg": "n1",
        "window": "26.38-28.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["NIGHTROAD"],
        "narration": "It gives you someone to follow through it.",
        "must_show": "the following — the lantern-bearer a few steps AHEAD now on the dark road, the follower stepping exactly into his lit footprints; followable light.",
        "must_not_show": "no halo; DIRECTION — the bearer ahead, the follower's feet in the light he leaves.",
        "scene": (
            "Through the worst stretches the light goes "
            "first: the bearer moves a few steps ahead on "
            "the night road now, lantern swung low so its "
            "ring falls where the next feet must land — and "
            "the follower comes on behind, stepping exactly "
            "into the lit ground the leader leaves, trusting "
            "the road only where the light has already "
            "touched it — not a lamp carried in your own "
            "hand: SOMEONE, ahead, findable, lighting the "
            "next step from the front. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r142-b07", "out": "s07-later-as-he-met-a.jpeg", "seg": "n2 + j2",
        "window": "29.59-38.02", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN"],
        "narration": (
            "Later, as he met a man who had never seen a face or a sunrise, "
            "he said it again. As long as I am in the world, I am the light "
            "of the world."
        ),
        "must_show": "SCRIPTURE-EXACT: the meeting — Jesus stopped before the born-blind beggar (row 63's man, eyes milk-pale), the claim repeated over the one man it will mean most to.",
        "must_not_show": "no halo; the man's DIGNITY total — alert, intelligent, reading the voice; eyes milk-pale (pre-healing).",
        "scene": (
            "The claim finds its ultimate test case sitting "
            "by the road: Jesus stops before the born-blind "
            "man — lean, alert, the strong intelligent face "
            "tilted to read the approaching voice, the eyes "
            "milk-pale that have never once held a face or "
            "a sunrise — and says it again over him, "
            "personally: as long as I am in the world, I AM "
            "the light of it — the world's light, "
            "introducing himself to the one man in "
            "Jerusalem who has been waiting his whole life "
            "to meet exactly that. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r142-b08", "out": "s08-he-did-not-leave-the.jpeg", "seg": "n3",
        "window": "39.83-41.88", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN"],
        "narration": "He did not leave the claim floating in the air.",
        "must_show": "the claim acted — Jesus kneeling to the man, fingertips (earth-dusted) gently at the closed lids; the anointing DISCREET, posture only, like row 136.",
        "must_not_show": "ABSOLUTE: nothing clinical or fluid — earth-dust on the fingertips and the tender posture carry the act.",
        "scene": (
            "The sentence gets hands within the minute: Jesus "
            "kneels to the seated man, and his fingertips — "
            "dusted with the road's earth — come gently to "
            "rest on the closed lids, his head bent close, "
            "the whole act quiet as a blessing at bedtime — "
            "no ceremony assembled, no crowd addressed: a "
            "claim about light backing itself, on the spot, "
            "with touch — the maker's fingers at the one "
            "pair of shutters they have come to open. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r142-b09", "out": "s09-he-opened-the-eyes-then.jpeg", "seg": "n3",
        "window": "41.88-45.71", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN"],
        "narration": (
            "He opened the man's eyes, then stayed with him when the crowd "
            "pushed him away."
        ),
        "must_show": "the staying — the healed man (eyes now clear deep brown) cast out: cold turned backs behind him — and Jesus ARRIVING at his side; found, not abandoned.",
        "must_not_show": "no halo; the casting-out COLD, not violent — turned backs and a dismissing gesture at distance; Jesus's arrival the frame's weight.",
        "scene": (
            "The miracle cost him his congregation and "
            "gained him its maker: the healed man stands in "
            "the street with his new deep-brown eyes wide, "
            "the cold backs of his dismissers already turned "
            "and receding behind him — cast out of the only "
            "community he ever begged beside — and arriving "
            "at his shoulder through the thinning crowd, "
            "unhurried and deliberate, Jesus — who heard, "
            "and came, and stays: the light of the world "
            "doing the light's second job, which is not "
            "leaving. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r142-b10", "out": "s10-the-sign-became-an-invitation.jpeg", "seg": "n3",
        "window": "45.71-52.05", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN"],
        "narration": (
            "The sign became an invitation: let Jesus show you what is "
            "true, then keep walking with him."
        ),
        "must_show": "the closing walk — the healed man walking WITH Jesus into the SUNRISE down the road; the man's first sunrise, seen beside its maker; invitation as companionship.",
        "must_not_show": "no halo, no light effects on either — the sunrise real ahead of them; the walking-together the sentence.",
        "scene": (
            "The last frame is the man's first sunrise: down "
            "the eastern road the two walk together — Jesus "
            "and the man who had never seen a face until "
            "today, his new eyes drinking the horizon where "
            "the sun comes up gold over the hills — the "
            "first dawn of his life, watched from beside "
            "the one who made both the eyes and the "
            "morning — the sign fully spent into its "
            "invitation: see what is true, and then keep "
            "walking, with him, into all the light there "
            "is. Every figure has two arms, two hands and "
            "one head."
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
