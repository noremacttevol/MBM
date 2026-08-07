#!/usr/bin/env python3
"""V2 beat map — row 162, build-162-keys-of-kingdom (Matthew 16:13-19).

COVERAGE: 24 pictures over 144.78 s = 6.0 s/picture (matches the library
density set by row 161's 24 pictures / 145.8 s).

OPEN CAMERON COMPLAINT: none on file (`v2_outline.py 162` shows no prior
review). This is a fresh authoring, so the job is the LEARNING/COST laws in
the positive: cover every beat, keep one locked place and one locked Peter,
and hand the runner a plate-promote plan so a NEW location does not drift.

SCRIPTURE FACTS (Matthew 16 KJV, the passage this row narrates):
  16:15 "He saith unto them, But whom say ye that I am?"          -> jv15
  16:16 "And Simon Peter answered and said, Thou art the Christ,
        the Son of the living God."                              -> s16 (PETER speaks)
  16:17 "flesh and blood hath not revealed it unto thee, but my
        Father which is in heaven."
  16:18 "And I say also unto thee, That thou art Peter, and upon
        this rock I will build my church; and the gates of hell
        shall not prevail against it."                           -> kv18
  16:19 "And I will give unto thee the keys of the kingdom of
        heaven: and whatsoever thou shalt bind on earth shall be
        bound in heaven: and whatsoever thou shalt loose on earth
        shall be loosed in heaven."                              -> kv19

ROW INTENT: the authority-is-given row (RESTORATION-adjacent, kept strictly
in the Bible's own frame). Christ builds his church on rock and places real
keys in a human hand — authority received, never seized. The close asks the
viewer whether they will trust that authority when they find it.

THE PLACE IS THE ARGUMENT. This whole exchange happens at Caesarea Philippi
in the far north below Mount Hermon, against a real towering rock cliff with
a cave and a cold spring at its foot. "Upon this rock I will build my church
and the gates of hell shall not prevail" is spoken with that immovable cliff
and its dark cave-mouth in view. So the cliff itself is a recurring, LOCKED
setting (CAESAREA-ROCK) and carries the theology — the rock endures the storm
(b13/b14), the church is built on it (b11), the keys are given before it.

SPEAKER LAW (the row-39 lesson): Peter's confession "Thou art the Christ,
the Son of the living God" (s16) is PETER speaking — it sits on PETER's face,
NOT on Jesus (jesus=False on b04). Jesus's own three red-letter lines
(jv15/kv18/kv19) sit on Jesus. Inside a Jesus red-letter segment the picture
may cut to what his words describe (the rock in b10, Peter receiving the keys
in b19) — the caption stays red by segment, the frame illustrates the words.

GOD / THE FATHER IS NEVER EMBODIED: at 16:17 "his Father in heaven" (b06),
the Father is warm light from above the top of the frame on Jesus's lifted
gaze — NO figure, NO dove, NO face in the sky, NO outline of light around
Jesus's head.

RENDERING LAWS:
  - Jesus is the locked V2 Jesus (LOCK v5 + REF on every jesus beat); only he
    wears cream. Ordinary-sized man, never enlarged (SCALE GATE, lesson 14).
  - PETER is the canonical-cast Peter, byte-identical across all 24 frames:
    same face, same iron-grey-streaked beard in EVERY frame (BEARD BOARD,
    lesson 13 — Peter is a repeat beard-drift offender across the library).
  - MOVIE COVERAGE (lesson 12): the establishing wide is b01 and ONLY b01;
    everything else is a single, a two-shot, or an insert. The disciples are a
    SMALL band, never the whole Twelve crowded in. Keys are two large ancient
    iron ward-keys, consistent object across b17-b24.
  - No modern objects, no pagan idol niches carved in the cliff, no invented
    scripture props, no cartoon — realistic biblical photography only (Law 14).

TIME OF DAY ARC (intentional): the arrival and confession in clear cool
northern morning; the "gates of hell / storms batter" beats (b10/b13) under a
darkened storm sky against the unmoved cliff; the giving of the keys and the
close in strengthening dawn-gold light breaking on the rock.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. PETER attaches from the global canonical cast by
# token; the shared JESUS lock + REF come from v2_prompt.py via jesus/ref.
LOCKS = {
    "CAESAREA-ROCK": (
        "CAESAREA-ROCK LOCK: the same place in every frame — the great rock "
        "of Caesarea Philippi in the far north beneath Mount Hermon: a "
        "towering pale limestone cliff face, sheer, seamed and weathered, "
        "with a wide dark cave-mouth low at its base where a cold spring "
        "wells out over moss-green stone and scattered fallen boulders; thin "
        "northern grass and a few terebinth trees at the foot; the snow-"
        "streaked shoulders of Mount Hermon distant behind. Cool clear "
        "northern light. The same cliff, cave and spring throughout — never a "
        "temple, never a built shrine, never carved idol niches, never a "
        "stone city."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: a small band of Galilean disciples — weathered "
        "fishermen and working men of varied ages, distinct sun-browned "
        "faces, dark hair and beards of differing lengths, plain undyed and "
        "earth-toned wool tunics of brown, rust, olive and grey (never cream "
        "— only Jesus wears cream); ordinary, dusty, real men, never twinned, "
        "never a cloned face, never a uniform crowd."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r162-b01", "out": "s01-at-caesarea-philippi.jpeg", "seg": "n1",
        "window": "0.280-7.594", "wide": True, "jesus": True, "ref": True,
        "locks": ["CAESAREA-ROCK", "DISCIPLES"],
        "narration": (
            "Far to the north, at a rocky place called Caesarea Philippi, "
            "Jesus stopped with his disciples and put a piercing question to them."
        ),
        "must_show": "the ONE establishing wide — camera on the northern path behind the small band's backs, looking past their shoulders up to the towering pale cliff with its dark cave-mouth and spring at the foot; Jesus among them turning to speak; the place readable as a real rock in the north.",
        "must_not_show": "not the whole Twelve crowded in — a SMALL band; no temple, city, or pagan shrine carved in the cliff; Jesus ordinary-sized, never a giant; no faces turned to pose at the lens.",
        "scene": (
            "A journey come to rest against something ancient and enormous: the "
            "camera stands on the dusty northern path a few steps behind the "
            "small band of disciples, looking north past their shoulders and "
            "backs to where the great pale limestone cliff of Caesarea Philippi "
            "rises sheer out of the grass, its dark cave-mouth and cold spring "
            "at the foot. Jesus has stopped among them and half-turned, a "
            "question already on him. The men's gazes travel away from the lens "
            "toward him and the rock beyond. Every figure has two arms, two "
            "hands and one head; all the men are of ordinary human height."
        ),
    },
    {
        "id": "v2-r162-b02", "out": "s02-who-do-you-say-that-i-am.jpeg", "seg": "n1",
        "window": "7.594-10.272", "wide": False, "jesus": True, "ref": True,
        "locks": ["CAESAREA-ROCK"],
        "narration": "Who do you say that I am?",
        "must_show": "a medium single on Jesus turned to the men, the question live on his face — steady, searching eyes, the pale cliff soft behind him.",
        "must_not_show": "no crowd; no light outlining his head; not a giant; the moment is his face asking, nothing else competing for it.",
        "scene": (
            "The question drawn as a face: a medium shot on Jesus turned toward "
            "his disciples at the foot of the rock, weight settled, warm brown "
            "eyes level and searching — the most personal thing he could ask "
            "them held quietly on his features, the seamed pale cliff falling "
            "out of focus behind. He has two hands and one head, an ordinary-"
            "sized man in cream wool."
        ),
    },
    {
        "id": "v2-r162-b03", "out": "s03-but-whom-say-ye-that-i-am.jpeg", "seg": "jv15",
        "window": "10.272-13.564", "wide": False, "jesus": True, "ref": True,
        "locks": ["CAESAREA-ROCK"],
        "narration": "But whom say ye that I am?",
        "must_show": "SCRIPTURE-EXACT (his red-letter line): a close on Jesus asking directly — a gentle, weighty press of the same question, eyes on the man before him.",
        "must_not_show": "no halo or light around his head; no crowd; the frame is only his asking face.",
        "scene": (
            "Closer now, the same question pressed home: Jesus's face fills the "
            "frame, the searching in his eyes softened into invitation, asking "
            "not the world's opinion but theirs — the cool northern light plain "
            "on his tanned skin, his dark hair and full beard, his cream robe "
            "at the shoulder. He has one head and warm brown eyes; nothing "
            "outlines or lights his head."
        ),
    },
    {
        "id": "v2-r162-b04", "out": "s04-thou-art-the-christ.jpeg", "seg": "s16",
        "window": "13.564-17.815", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "CAESAREA-ROCK"],
        "narration": "Thou art the Christ, the Son of the living God.",
        "must_show": "SCRIPTURE-EXACT, and it is PETER speaking: a close on Peter's face lit with sudden certainty, mouth mid-confession, eyes fixed off-frame on Jesus; the rock behind him.",
        "must_not_show": "NOT Jesus's face — the confession is Peter's; no other disciple crowding the shot; Peter's iron-grey-streaked beard present and unchanged.",
        "scene": (
            "The words belong to the man who says them: a close on Peter, the "
            "Galilean fisherman, his weathered face opening with a certainty "
            "that has just surprised him, lips parted on the confession, his "
            "eyes locked off-frame on the one he is naming — the pale cliff "
            "steady behind his shoulder. His iron-grey-streaked dark beard and "
            "sun-browned face are the same as in every frame. He has two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r162-b05", "out": "s05-simon-peter-answered-for-all.jpeg", "seg": "n2",
        "window": "17.815-20.868", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "DISCIPLES"],
        "narration": "It was Simon Peter, the fisherman, who answered for them all.",
        "must_show": "a tight two-shot: Peter forward having just spoken, one or two other disciples half-behind him looking to him — he answered on their behalf, and they know it.",
        "must_not_show": "not the full Twelve; the other men slightly out of focus behind Peter so the moment stays his; no cloned faces.",
        "scene": (
            "One man carried the answer for the rest: Peter stands a half-step "
            "forward of the small band, the words still on him, while one or "
            "two fellow disciples behind his shoulder turn their faces to him "
            "— the fisherman who spoke for men who could not find the words. "
            "The others are earth-toned and distinct, held soft behind him. "
            "Every figure has two hands and one head."
        ),
    },
    {
        "id": "v2-r162-b06", "out": "s06-flesh-and-blood-hath-not.jpeg", "seg": "n2",
        "window": "20.868-27.613", "wide": False, "jesus": True, "ref": True,
        "locks": ["PETER", "CAESAREA-ROCK"],
        "narration": (
            "And Jesus told him that flesh and blood had not revealed that to "
            "him; his Father in heaven had."
        ),
        "must_show": "an over-shoulder two-shot past Peter to Jesus, who lifts his gaze a little toward warm light coming down from above the top of the frame — the Father named, not shown; the giving of the insight is heaven's, not Peter's own.",
        "must_not_show": "the Father NEVER embodied — no figure, no face in the sky, no dove, no light outlining Jesus's head; only soft warm light from above the frame edge.",
        "scene": (
            "A truth traced back to its source: shot over Peter's shoulder to "
            "Jesus, who meets the fisherman's eyes and then lifts his own a "
            "little toward the warm light spilling down from above the top of "
            "the frame — telling him plainly that no man taught him this, that "
            "it came down from his Father in heaven. The light stays at the "
            "frame's upper edge and never becomes a figure or a shape. Jesus is "
            "an ordinary-sized man; both men have two hands and one head."
        ),
    },
    {
        "id": "v2-r162-b07", "out": "s07-something-to-change-his-life.jpeg", "seg": "n3",
        "window": "27.613-30.608", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "Then Jesus said something that would change Simon's life.",
        "must_show": "a close on Peter's face turned up in expectancy, caught in the held breath before the naming — he can feel that something is coming.",
        "must_not_show": "no action yet; not Jesus's face this beat; Peter's beard unchanged; nothing but his waiting face.",
        "scene": (
            "The hinge of a life, held on a face: a close on Peter, listening, "
            "his weathered features lifted and still, the smallest expectancy "
            "gathering in his eyes as if he half-senses that the next words are "
            "about to reach all the way down into who he is. The northern light "
            "is plain on his iron-grey-streaked beard. He has one head and two "
            "hands."
        ),
    },
    {
        "id": "v2-r162-b08", "out": "s08-he-gave-him-a-new-name.jpeg", "seg": "n3",
        "window": "30.608-41.994", "wide": False, "jesus": True, "ref": True,
        "locks": ["PETER", "CAESAREA-ROCK"],
        "narration": (
            "He gave him a new name — Peter, which means a rock — and told him "
            "that on rock like that, solid and sure, he would build something "
            "meant to outlast the ages."
        ),
        "must_show": "a two-shot at the cliff foot: Jesus close to Peter, one hand laid on Peter's shoulder, both turned so the great pale rock rises right behind them — the new name and the literal rock in the same frame, the meaning made visible.",
        "must_not_show": "no crowd; the rock unmistakably behind them; Jesus ordinary-sized beside Peter, neither enlarged; no light around Jesus's head.",
        "scene": (
            "A name and a rock set side by side so the eye can read the "
            "promise: Jesus stands close to Peter at the foot of the cliff, one "
            "hand laid on the fisherman's shoulder, both of them turned a "
            "little so the towering pale rock fills the frame behind them — the "
            "man newly called a rock standing against the very thing he is "
            "named for, solid and sure and older than any of them. Jesus in "
            "cream, Peter in earth-toned wool; both ordinary-sized, each with "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r162-b09", "out": "s09-upon-this-rock.jpeg", "seg": "kv18",
        "window": "41.994-47.600", "wide": False, "jesus": True, "ref": True,
        "locks": ["PETER", "CAESAREA-ROCK"],
        "narration": (
            "And I say also unto thee, That thou art Peter, and upon this rock "
            "I will build my church;"
        ),
        "must_show": "SCRIPTURE-EXACT (his red-letter line): Jesus speaking to Peter, one open hand gesturing from Peter toward the great cliff — 'thou art Peter, and upon this rock I will build my church' made as a gesture from the man to the stone.",
        "must_not_show": "no halo or light around Jesus's head; not a giant; the gesture clearly from Peter to the rock, not vague.",
        "scene": (
            "The declaration turned into a line the eye can follow: Jesus faces "
            "Peter and opens one hand from the fisherman toward the towering "
            "cliff behind them, drawing name and rock and church into a single "
            "motion — I will build my church here, on this. His face is steady "
            "and glad, the cool light plain on his cream robe. He is an "
            "ordinary-sized man with two hands and one head; nothing lights his "
            "head."
        ),
    },
    {
        "id": "v2-r162-b10", "out": "s10-gates-of-hell-shall-not-prevail.jpeg", "seg": "kv18",
        "window": "47.600-53.505", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAESAREA-ROCK"],
        "narration": "and the gates of hell shall not prevail against it.",
        "must_show": "an insert of the cliff itself — low angle up the immovable pale rock face to the wide dark cave-mouth at its base, cold spring water at the stone; the darkness of the cave standing for the gates of hell, dwarfed by the rock above it.",
        "must_not_show": "no figures needed (or tiny at the foot); no demons, no flames, no invented symbols; the cave a natural dark mouth in real stone, not a monster or a gate structure.",
        "scene": (
            "The promise carried by the stone alone: a low insert looking up "
            "the sheer, seamed pale rock to the wide dark cave-mouth low at its "
            "base, cold spring water sliding over the moss-green stones — the "
            "darkness of that mouth standing for the gates of death and hell, "
            "and the enormous immovable rock rising over it plainly unafraid. "
            "Real weathered limestone and real water, nothing invented, no "
            "figure larger than a man at the foot."
        ),
    },
    {
        "id": "v2-r162-b11", "out": "s11-his-gathered-people.jpeg", "seg": "n4",
        "window": "53.505-59.500", "wide": False, "jesus": True, "ref": True,
        "locks": ["CAESAREA-ROCK", "DISCIPLES"],
        "narration": (
            "His church, he called it — his own gathered people, built on a "
            "firm foundation,"
        ),
        "must_show": "a modest group two/three-shot: Jesus among a small handful of his people close at the foot of the rock, drawn in around him — the gathered church as a few real faces on solid stone, not a nation.",
        "must_not_show": "not a large crowd; the group SMALL and close; Jesus ordinary-sized among them; no light around his head; the rock foundation under and behind them.",
        "scene": (
            "The church shown at human scale: Jesus stands close among a small "
            "handful of his people at the foot of the great rock, their faces "
            "turned in toward him, shoulders nearly touching — his own gathered "
            "people, a few real weathered faces standing together on solid "
            "stone rather than a nameless multitude. The pale cliff is their "
            "floor and their wall. Jesus in cream among earth-toned wool, all "
            "ordinary-sized, each with two hands and one head."
        ),
    },
    {
        "id": "v2-r162-b12", "out": "s12-not-overpowered.jpeg", "seg": "n4",
        "window": "59.500-65.771", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAESAREA-ROCK"],
        "narration": (
            "and so strong that not even the gates of death and darkness could "
            "ever overpower it or shut it down."
        ),
        "must_show": "an insert of the rock enduring: the pale cliff standing firm under a sky beginning to darken and bruise with gathering storm — the stone unmoved while the weather turns against it.",
        "must_not_show": "no figures, or tiny; no lightning-as-spectacle, no invented symbols; the darkness is weather and shadow, the rock plainly winning by simply standing.",
        "scene": (
            "Strength drawn as weather against stone: the towering pale cliff "
            "holds the frame while the northern sky above it darkens and "
            "bruises with a gathering storm, wind dragging at the terebinth "
            "trees at its foot — and the rock does not move, does not crack, is "
            "not overpowered, the dark cave-mouth still small beneath its "
            "unshaken mass. Real stone and real storm light, nothing invented."
        ),
    },
    {
        "id": "v2-r162-b13", "out": "s13-storms-would-come.jpeg", "seg": "n5",
        "window": "65.771-73.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAESAREA-ROCK"],
        "narration": (
            "That is a staggering promise. Empires would fall, storms would "
            "come,"
        ),
        "must_show": "the storm at full weight on the cliff: rain and wind lashing the pale rock face, water sheeting off the stone, the sky low and iron-dark — the empires-fall, storms-come pressure made literal against the immovable rock.",
        "must_not_show": "no figures; no shipwreck or unrelated scenery; no fantasy; just severe real weather beating the real cliff, which holds.",
        "scene": (
            "The worst the world can throw, thrown: rain and hard wind lash the "
            "pale limestone cliff, water sheeting down the seamed face and off "
            "the boulders, the northern sky pressed low and iron-dark over Mount "
            "Hermon behind — everything that topples empires flung at the rock "
            "at once. The stone stands into it, streaming and unbroken. Real "
            "storm, real stone, nothing invented."
        ),
    },
    {
        "id": "v2-r162-b14", "out": "s14-still-it-would-stand.jpeg", "seg": "n5",
        "window": "73.000-80.978", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAESAREA-ROCK"],
        "narration": (
            "the powers of the grave itself would batter against it — and still "
            "it would stand, because its foundation was laid by God and not by "
            "men."
        ),
        "must_show": "the storm breaking: the same cliff now with the sky clearing and the first dawn-gold light striking the top of the pale rock, the deep foundation stones at its base solid and dry-lit — battered but standing, a foundation not laid by men.",
        "must_not_show": "no figures; no rainbow-as-symbol or invented sign; the change is only weather passing and light returning on the same real rock.",
        "scene": (
            "After everything, the rock is simply still there: the storm is "
            "pulling off the northern sky and the first dawn-gold light strikes "
            "the crown of the pale cliff and runs down its seamed face to the "
            "massive foundation stones at its base — battered by the powers of "
            "the grave and unmoved, standing because what it stands on was laid "
            "by God and not by men. The same real cliff, the same cave and "
            "spring, nothing invented."
        ),
    },
    {
        "id": "v2-r162-b15", "out": "s15-he-turned-to-peter.jpeg", "seg": "n6",
        "window": "80.978-85.192", "wide": False, "jesus": True, "ref": True,
        "locks": ["PETER", "CAESAREA-ROCK"],
        "narration": (
            "But Jesus was not finished. He would not leave his church without "
            "a way to be led."
        ),
        "must_show": "a two-shot: Jesus turning back to face Peter directly at the cliff foot, unfinished, purpose fresh on him — about to give something specific.",
        "must_not_show": "no crowd; no light around Jesus's head; both men ordinary-sized; the rock behind them the same cliff.",
        "scene": (
            "The scene is not over, and his face says so: Jesus turns back "
            "squarely to Peter at the foot of the rock, the glad steadiness "
            "sharpening into purpose — a leader who will not walk away leaving "
            "his people with no way to be led. Peter meets the turn. Jesus in "
            "cream, Peter in earth-toned wool, both ordinary-sized with two "
            "hands and one head, the pale cliff behind."
        ),
    },
    {
        "id": "v2-r162-b16", "out": "s16-real-authority.jpeg", "seg": "n6",
        "window": "85.192-92.623", "wide": False, "jesus": True, "ref": True,
        "locks": ["PETER"],
        "narration": (
            "So he turned to Peter and promised him something specific — real "
            "authority, handed down from heaven itself."
        ),
        "must_show": "a close two-shot, Jesus and Peter face to face, the gravity of a specific promise between them — Jesus's expression the weight of handing something real and heavenly into this man's keeping.",
        "must_not_show": "the keys not shown yet (they come next); no light around Jesus's head; faces close, ordinary-sized, no third figure crowding.",
        "scene": (
            "A promise made person to person: a close two-shot of Jesus and "
            "Peter face to face at the rock, the space between them charged with "
            "the seriousness of something specific about to be entrusted — real "
            "authority, come down from heaven, laid on the shoulders of one "
            "weathered fisherman. Nothing in their hands yet. Both ordinary-"
            "sized, each with two hands and one head; nothing lights Jesus's "
            "head."
        ),
    },
    {
        "id": "v2-r162-b17", "out": "s17-he-called-it-keys.jpeg", "seg": "n6",
        "window": "92.623-95.128", "wide": False, "jesus": True, "ref": True,
        "locks": ["PETER", "CAESAREA-ROCK"],
        "narration": "He called it keys.",
        "must_show": "an insert-scale two-shot on the hands: Jesus's hand extending two large ancient iron ward-keys toward Peter's opening hands — the abstract authority given a concrete shape, the keys named.",
        "must_not_show": "no modern keys; exactly TWO large iron ward-keys, the object that must stay consistent through the rest of the film; no light around anyone's head.",
        "scene": (
            "Authority given a thing you can hold: framed close on the hands at "
            "the cliff foot, Jesus's hand extends two large ancient iron ward-"
            "keys — long shafts, toothed bits, a worn ring at each bow — toward "
            "Peter's hands already beginning to open to receive them. A cream "
            "sleeve at Jesus's wrist, an earth-toned one at Peter's. Real iron, "
            "real weight, two keys, nothing invented; hands whole, five fingers "
            "each."
        ),
    },
    {
        "id": "v2-r162-b18", "out": "s18-i-will-give-thee-the-keys.jpeg", "seg": "kv19",
        "window": "95.128-102.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["PETER", "CAESAREA-ROCK"],
        "narration": (
            "And I will give unto thee the keys of the kingdom of heaven:"
        ),
        "must_show": "SCRIPTURE-EXACT (his red-letter line): Jesus in the two-shot giving the two iron keys to Peter, speaking the words, his face on Peter as the keys pass — the actual giving.",
        "must_not_show": "still exactly TWO iron keys, same as b17; no halo or light around Jesus's head; both ordinary-sized; Peter's beard unchanged.",
        "scene": (
            "The giving itself, spoken: Jesus holds out the two ancient iron "
            "keys and Peter's hands close under them, the transfer happening as "
            "the words are said — I will give unto thee the keys of the kingdom "
            "of heaven. Jesus's face is on Peter, glad and certain; the pale "
            "cliff steadies the frame behind. Both men ordinary-sized, cream on "
            "Jesus and earth-tone on Peter, hands whole; nothing lights Jesus's "
            "head."
        ),
    },
    {
        "id": "v2-r162-b19", "out": "s19-bind-and-loose.jpeg", "seg": "kv19",
        "window": "102.000-110.549", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": (
            "and whatsoever thou shalt bind on earth shall be bound in heaven: "
            "and whatsoever thou shalt loose on earth shall be loosed in heaven."
        ),
        "must_show": "a close on Peter now holding the two iron keys in both weathered hands, looking down at their weight then up — earth in his hands, heaven honouring it; the bind-and-loose authority settling on him.",
        "must_not_show": "NOT Jesus's face this beat (cut to the receiver); still exactly TWO iron keys; no split-panel earth/heaven diagram, no invented symbol; Peter's beard the same.",
        "scene": (
            "The weight of it lands on the man who now holds it: a close on "
            "Peter's two weathered hands closed around the two ancient iron "
            "keys, his eyes moving from the keys up toward the dawn-lit sky — "
            "what he binds and looses here will be honoured there, earth and "
            "heaven joined in the iron in his grip. His iron-grey-streaked "
            "beard and sun-browned face unchanged; hands whole, five fingers "
            "each, two keys."
        ),
    },
    {
        "id": "v2-r162-b20", "out": "s20-open-and-close.jpeg", "seg": "n7",
        "window": "110.549-115.890", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Keys open and close, lock and unlock, admit and secure.",
        "must_show": "an insert of one of the great iron keys in the lock of a heavy ancient wooden door — the toothed key turning the wooden ward-bolt, the door beginning to open; authority as a thing that actually opens and closes.",
        "must_not_show": "no modern lock or metal door; a period wooden door with a wooden/iron ward lock; no invented engraving or symbol on the door.",
        "scene": (
            "What a key is for, shown plainly: an insert of one large ancient "
            "iron ward-key turned in the lock of a heavy timber door, the "
            "wooden bolt sliding in its housing and the door easing open on a "
            "band of light — opening and closing, locking and unlocking, "
            "admitting and securing, the whole meaning of the office in one "
            "honest mechanism. Weathered oak, hand-forged iron, nothing modern, "
            "no invented mark. A hand on the key is whole, five fingers."
        ),
    },
    {
        "id": "v2-r162-b21", "out": "s21-real-authority-in-gods-name.jpeg", "seg": "n7",
        "window": "115.890-122.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": (
            "To hold the keys of the kingdom is to carry real authority to act "
            "in God's name,"
        ),
        "must_show": "Peter standing, the two iron keys held to his chest in both hands, the settled bearing of a man who now carries real authority — sober, not proud; the weight understood.",
        "must_not_show": "no crown, throne, or self-important posture — authority received, not seized; still two keys; Peter's beard unchanged; no light around his head.",
        "scene": (
            "Authority worn like a burden accepted: Peter stands holding the two "
            "ancient iron keys against his chest in both hands, his weathered "
            "face grave and steadied — a fisherman who now carries the right to "
            "act in God's name and plainly feels the size of it, sober rather "
            "than proud. Earth-toned wool, iron-grey-streaked beard, two hands "
            "and one head, two keys."
        ),
    },
    {
        "id": "v2-r162-b22", "out": "s22-honoured-in-heaven.jpeg", "seg": "n7",
        "window": "122.500-129.388", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "CAESAREA-ROCK"],
        "narration": (
            "so that what is done rightly on earth is honoured in heaven — not "
            "invented by men, but given by the Lord."
        ),
        "must_show": "Peter lifting his eyes upward at the foot of the rock, the two keys held, warm dawn light reaching down onto him from above the top of the frame — earth's right act honoured from heaven; the authority given, not invented.",
        "must_not_show": "the Lord/heaven NEVER embodied — no figure, no face in the sky, only warm light from above the frame edge; still two keys; no light outlining Peter's head.",
        "scene": (
            "The line back up to where it came from: Peter lifts his eyes at the "
            "foot of the pale cliff, the two iron keys held, and warm dawn light "
            "reaches down onto his upturned face from above the top of the frame "
            "— what he does rightly on earth answered and honoured from heaven, "
            "the authority given by the Lord and never invented by men. The "
            "light stays at the frame's edge and becomes no figure. Two hands, "
            "one head, two keys."
        ),
    },
    {
        "id": "v2-r162-b23", "out": "s23-built-on-rock-keys-in-hands.jpeg", "seg": "n8",
        "window": "129.388-136.633", "wide": False, "jesus": True, "ref": True,
        "locks": ["PETER", "CAESAREA-ROCK"],
        "narration": (
            "So Jesus did not leave his people leaderless, or his church "
            "without authority. He built it on rock and placed real keys in "
            "human hands."
        ),
        "must_show": "a closing two-shot: Jesus and Peter together at the foot of the great rock, the two iron keys now plainly in Peter's hands, Jesus's hand near his shoulder — church on rock, real keys in human hands, both held in one frame.",
        "must_not_show": "no crowd; both ordinary-sized; no light around Jesus's head; the same cliff, the same two keys.",
        "scene": (
            "The whole promise gathered into one steady frame: Jesus and Peter "
            "stand together at the foot of the towering pale rock, the two "
            "ancient iron keys resting now in Peter's own weathered hands, "
            "Jesus's hand near his shoulder — a church built on rock and real "
            "keys placed in human hands, nobody left leaderless, no authority "
            "left to chance. Jesus in cream, Peter in earth-tone, both ordinary-"
            "sized with two hands and one head."
        ),
    },
    {
        "id": "v2-r162-b24", "out": "s24-will-you-trust-it.jpeg", "seg": "n8",
        "window": "136.633-144.784", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "So the only question is a hopeful one. When you find that "
            "authority, given by him and not seized by men, will you trust it?"
        ),
        "must_show": "the closing invitation as an insert: the two ancient iron keys resting across an open, weathered human palm held gently toward the viewer in warm dawn light — authority offered, the question left open and hopeful.",
        "must_not_show": "no face needed; no grasping or clenched fist — an OPEN palm offering; still exactly two iron keys; no invented symbol or text; warm light from above, nothing embodied.",
        "scene": (
            "The film hands the question to the person watching: an insert of "
            "the two ancient iron keys lying across an open, weathered human "
            "palm held gently up toward the lens in warm dawn light — authority "
            "given by him and not seized by men, offered rather than forced, the "
            "hand open and unhurried. The only question left is a hopeful one. "
            "Real iron, a real open hand, five fingers, two keys, nothing "
            "invented."
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
