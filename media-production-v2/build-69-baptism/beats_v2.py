#!/usr/bin/env python3
"""V2 beat map — row 69, build-69-baptism (Matthew 3:1-17).

COVERAGE: 29 pictures over 165.1 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 3 KJV):
  v1-6  JOHN at the Jordan: "raiment of CAMEL'S HAIR, and a LEATHERN
        GIRDLE" — the wilderness prophet locked exactly so; the whole
        countryside walking out to him; sinners lined along the bank
        confessing and going under.
  v13   "Then cometh Jesus FROM GALILEE to Jordan ... TO BE BAPTIZED of
        him" — days on foot, on purpose; he JOINS THE LINE of confessing
        sinners: the queue beat is doctrine.
  v14   "John forbad him, saying, I HAVE NEED TO BE BAPTIZED OF THEE" —
        the wild man's one refusal; the reversal he cannot compute.
  v15   "SUFFER IT TO BE SO NOW: for thus it becometh us to fulfil all
        righteousness" — the reason for almost everything: first through
        every door he asks anyone to walk through.
  v16   "went up STRAIGHTWAY out of the water: and, lo, the heavens were
        OPENED ... the Spirit of God descending LIKE A DOVE, and lighting
        upon him" — the opened heaven painted as a great bright break in
        cloud (no rays, no figures); the Spirit as a REAL white dove
        descending and resting — a bird, painted plainly, per scripture.
  v17   "a VOICE from heaven, saying, This is my beloved Son, in whom I
        am well pleased" — THE VOICE NEVER EMBODIED: no form, no light-
        source; the words land on the riverbank's faces.
        The three-fold moment (b23-b26): Son in the water, Spirit
        descending, Father speaking — EACH DISTINCT, painted as three
        simultaneous real facts in one frame: man, bird, and heard
        words; nothing merged, nothing symbolized beyond the text.

TIME OF DAY: one bright morning at the Jordan throughout — clean river
light; the opened-heaven beats keep daylight logic (a cloud-break's
brightness, not supernatural glow). No sunset anywhere.

CONTENT-CARE: no flags. The confessing sinners painted with dignity;
John rough, never grotesque; the Godhead moment handled with exact
scriptural restraint.

CHANGING CONDITION (kept OUT of the locks): Jesus wet-robed after the
immersion; the sky — plain, then opened, then plain; the line's order —
sinners, then the sinless one in the same line.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "BAPTIST": (
        "JOHN THE BAPTIST LOCK: John is the same man in every shot — "
        "mid-thirties, lean and burned dark by the desert, with a great "
        "mane of sun-shot black hair and a wild beard, fierce clear "
        "eyes and a voice's force visible in his throat and stance. He "
        "wears the locked raiment: a rough coat of CAMEL'S HAIR bound "
        "with a wide LEATHER girdle, bare weathered arms (never cream, "
        "never white). His face is shown clearly."
    ),
    "JORDAN": (
        "JORDAN LOCK: the baptizing bend of the Jordan — a slow green "
        "river between reed-lined banks, a trodden entry slope of pale "
        "mud, tamarisk and willow shade on the far side, and the "
        "wilderness hills pale beyond. The same bend, slope and reeds "
        "in every river beat."
    ),
    "CROWD": (
        "BANK CROWD LOCK: the countryside come out — farmers, "
        "tradesmen, mothers, soldiers off-duty, tax men, elders, in "
        "SATURATED DEEP earth colours: dark browns, deep russet, dark "
        "olive, burnt ochre, dusty indigo (never cream, never white; "
        "only Jesus wears cream). Faces shown clearly — penitents with "
        "dignity."
    ),
    "DOVE": (
        "DOVE LOCK: the Spirit's descent is one REAL white dove — a "
        "plain rock dove, pure white, painted exactly as a living bird "
        "in flight and at rest; never radiant, never translucent, with "
        "no ring of light about it; its realism IS the reverence."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r069-b01", "out": "s01-down-at-the-jordan-river.jpeg", "seg": "n0",
        "window": "0.28-2.72", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAPTIST", "JORDAN", "CROWD"],
        "narration": "Down at the Jordan river, John was baptizing.",
        "must_show": "SCRIPTURE-EXACT: the scene at work — John waist-deep at the bend, a penitent going under his hands, the bank lined with waiting people; the ministry mid-stroke.",
        "must_not_show": "no halo, glare or rim-light; the baptizing practical and powerful — a working prophet in a working river.",
        "scene": (
            "At the green bend of the Jordan, the camera on the "
            "far bank taking bend and line from the side, the work is "
            "mid-stroke: John waist-deep in the slow "
            "water, his camel-hair coat dark to the "
            "chest, both hands lowering a penitent "
            "farmer back under the surface — while up "
            "the trodden mud slope the waiting line "
            "stretches along the reed-bank, and the "
            "wilderness hills stand pale behind the "
            "whole morning's business of beginning "
            "again. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r069-b02", "out": "s02-he-was-rough-as-the.jpeg", "seg": "n0",
        "window": "2.72-15.98", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAPTIST", "JORDAN", "CROWD"],
        "narration": (
            "He was rough as the desert he came from — a coat of camel's hair, "
            "a leather belt, a voice like a trumpet — and the whole countryside "
            "was walking out to him."
        ),
        "must_show": "SCRIPTURE-EXACT: the man and his magnetism — John preaching from a rock at the water's edge, mane flying, and the roads behind the bank alive with more people walking out.",
        "must_not_show": "no halo, glare or rim-light; the roughness exact — camel hair, leather, desert burn; the walking-out visible on the roads.",
        "scene": (
            "From a rock at the water's edge, the camera behind "
            "the listening crowd's shoulders, John "
            "preaches with his whole body — black mane "
            "flying, burned arm flung toward the hills, "
            "the trumpet of his voice visible in every "
            "craned neck along the bank — while behind "
            "the crowd the wilderness roads run dotted "
            "with more arrivals, family after family "
            "walking out from the whole countryside "
            "toward a man dressed like the desert's own "
            "opinion of comfort. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b03", "out": "s03-every-day-sinners-lined-the.jpeg", "seg": "n0",
        "window": "15.98-18.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD", "JORDAN"],
        "narration": "Every day, sinners lined the bank.",
        "must_show": "the line itself — along the trodden bank: the waiting penitents in their honest variety, heads bowed or lifted, a queue of admitted need.",
        "must_not_show": "no halo, glare or rim-light; the line dignified — soldiers and tax men and farmers equal in it; confession as posture.",
        "scene": (
            "Along the trodden mud of the bank the "
            "day's line waits: a soldier with his "
            "helmet under his arm and his eyes down, a "
            "tax man turning his rings, a farm couple "
            "holding hands, an old woman praying "
            "silently mid-queue — the countryside's "
            "honest variety standing in the one line "
            "that admits what every other line in the "
            "world conceals. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b04", "out": "s04-and-then-one-day-somebody.jpeg", "seg": "n0",
        "window": "18.55-22.52", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CROWD", "JORDAN"],
        "narration": (
            "And then one day, somebody joined the line who had nothing to "
            "confess."
        ),
        "must_show": "SCRIPTURE-DOCTRINE: the joining — Jesus taking his place at the END of the penitents' line, unannounced, road-dusty; the sinless one queueing with sinners.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NOTHING distinguishes him but the viewer's knowledge — same line, same dust, same waiting.",
        "scene": (
            "At the line's end, the camera along the queue so the "
            "waiting backs recede in profile, unannounced, a new "
            "arrival takes his place — road-dusty from "
            "Galilee, cream robe travel-stained, "
            "waiting behind the old praying woman like "
            "any other comer — no one on the bank "
            "turning, no gap opening around him: the "
            "one man in the queue with nothing to "
            "confess, standing in it exactly as if he "
            "belonged, because that is the point. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r069-b05", "out": "s05-jesus-walked-from-galilee-days.jpeg", "seg": "n1",
        "window": "23.12-28.34", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JORDAN"],
        "narration": (
            "Jesus walked from Galilee — days on foot — specifically to be "
            "baptized by John."
        ),
        "must_show": "the deliberate journey — Jesus alone on the wilderness road above the river valley, the Jordan's green thread below; days of walking aimed at one bend of water.",
        "must_not_show": "no halo, glare or rim-light on Jesus; purpose in the stride — a destination journey, not a wandering.",
        "scene": (
            "On the pale wilderness road above the "
            "valley Jesus walks alone in the morning "
            "light — staff in hand, days of Galilee "
            "dust on his hem — and below him the "
            "Jordan's green thread winds through the "
            "brown land toward the distant bend where "
            "tiny figures cluster at the water: a "
            "walk of days aimed, step by deliberate "
            "step, at one prophet and one river. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r069-b06", "out": "s06-and-john-the-wild-man.jpeg", "seg": "n1",
        "window": "28.69-33.24", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": (
            "And John, the wild man who was afraid of nobody, took one look and "
            "refused:"
        ),
        "must_show": "SCRIPTURE-EXACT: the refusal — Jesus arrived at the water's edge, and John backing a step in the shallows, both hands up; the fearless man's first and only balk.",
        "must_not_show": "no halo, glare or rim-light on Jesus; John's recognition total and staggering — the trumpet silenced, the wild man undone.",
        "scene": (
            "At the water's edge the impossible "
            "happens to John: Jesus stands before him "
            "in the shallows, asking — and the wild "
            "man who has thundered at soldiers and "
            "kings backs a full step through the "
            "water, both burned hands coming up, his "
            "fierce eyes wide with the first refusal "
            "of his ministry — recognition hitting a "
            "fearless man in the one place he had no "
            "armour. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r069-b07", "out": "s07-i-have-need-to-be.jpeg", "seg": "s14",
        "window": "33.82-37.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTIST"],
        "narration": "I have need to be baptized of thee, and comest thou to me?",
        "must_show": "SCRIPTURE-EXACT: the protest — close on John's staggered face: the desert prophet naming his own need aloud; humility from the loudest voice in Israel.",
        "must_not_show": "no halo, glare or rim-light; the humility fierce — need confessed at trumpet volume turned inward.",
        "scene": (
            "Close on John's staggered face in the "
            "river light: the wild mane framing "
            "features stripped of all their thunder — "
            "the fierce eyes suddenly a debtor's "
            "eyes, the trumpet throat working around "
            "a confession of his own — the man who "
            "calls all Israel to the water naming, "
            "out loud, the one baptism he cannot "
            "perform: his own. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b08", "out": "s08-the-one-who-needs-what.jpeg", "seg": "n1b",
        "window": "38.28-42.12", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BAPTIST"],
        "narration": (
            "I'm the one who needs what you have, he said — and you're coming "
            "to me?"
        ),
        "must_show": "the reversal held — the two faces close in the shallows: John's bafflement against Jesus's quiet insistence; the direction of grace, disputed by its own herald.",
        "must_not_show": "no halo, glare or rim-light on Jesus; both faces full — the argument tender and enormous.",
        "scene": (
            "The two faces close over the green water: "
            "John's burned and baffled, his head "
            "shaking slowly inside its mane — and "
            "Jesus's quiet and certain opposite it, "
            "the insistence gentle and immovable — "
            "the herald and the heralded standing in "
            "the same river arguing, with perfect "
            "love, about which of them should be on "
            "his knees. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b09", "out": "s09-and-john-was-right-it.jpeg", "seg": "n2",
        "window": "47.20-50.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": "And John was right — it did not make sense.",
        "must_show": "the sense honestly missing — John's hands still raised in protest over the water; the logic's gap held open and honoured before it resolves.",
        "must_not_show": "no halo, glare or rim-light; the bafflement legitimate — the narration sides with John's math before transcending it.",
        "scene": (
            "In the shallows John's protest holds its "
            "shape: both weathered hands still raised "
            "between himself and the request, the "
            "river sliding past his waist, his wild "
            "face working through arithmetic that "
            "will not close — the cleanest man in the "
            "line asking the muddiest river-work of "
            "the one prophet honest enough to say "
            "out loud that the sums are backwards. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r069-b10", "out": "s10-baptism-was-for-washing-sins.jpeg", "seg": "n2",
        "window": "50.13-54.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["JORDAN", "CROWD"],
        "narration": "Baptism was for washing sins away, and Jesus had none.",
        "must_show": "the institution stated — a penitent rising from the water mid-line, washed and weeping with relief; what the river is FOR, shown working.",
        "must_not_show": "no halo, glare or rim-light; the ordinary baptism honoured — relief real on a forgiven face.",
        "scene": (
            "Mid-line, the river does its appointed "
            "work: a grey tradesman comes up out of "
            "the water streaming, eyes shut, mouth "
            "open in the first breath of a man whose "
            "ledger has just been carried away "
            "downstream — relief breaking over his "
            "wet face while the line behind him "
            "shuffles one place forward — the "
            "institution of washing, functioning "
            "exactly as designed, one sinner before "
            "the exception arrives. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b11", "out": "s11-so-listen-carefully-to-the.jpeg", "seg": "n2",
        "window": "55.05-60.44", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": (
            "So listen carefully to the reason Jesus gives, because it tells "
            "you why he did almost everything:"
        ),
        "must_show": "the reason coming — close on Jesus's face gathering the answer: the whole ministry's logic about to be spoken in one sentence at a river.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gravity gentle — a key being handed over, not a ruling.",
        "scene": (
            "Close on Jesus's face in the clean river "
            "light: the answer gathering behind the "
            "warm eyes with the weight of everything "
            "it will explain — every future touch of "
            "lepers, every shared table, every road "
            "walked in other people's dust — the "
            "whole method of the ministry arriving at "
            "its first out-loud statement, at a "
            "muddy river, to one wild objector. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r069-b12", "out": "s12-suffer-it-to-be-so.jpeg", "seg": "j1",
        "window": "61.04-66.42", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BAPTIST"],
        "narration": (
            "Suffer it to be so now: for thus it becometh us to fulfil all "
            "righteousness."
        ),
        "must_show": "SCRIPTURE-EXACT: the sentence — Jesus's hand coming to rest on John's raised forearm, gently lowering the protest; the words and the touch together.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the lowering of the objection tender — consent being helped into being.",
        "scene": (
            "Over the green water Jesus's hand comes "
            "to rest on John's raised forearm — and "
            "gently, with the sentence, lowers it: "
            "the protest yielding under the touch, "
            "the wild man's hands sinking to the "
            "river's surface, his face beginning its "
            "surrender — permission being asked and "
            "granted in the same motion, between the "
            "only two men in Israel who understand "
            "what is about to happen. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b13", "out": "s13-let-it-happen-john-this.jpeg", "seg": "n3",
        "window": "67.56-72.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BAPTIST"],
        "narration": (
            "Let it happen, John — this is how we do everything right, "
            "together."
        ),
        "must_show": "the together — the two men squared to each other in the river, John's consent arriving; partnership across the impossible gap.",
        "must_not_show": "no halo, glare or rim-light on Jesus; 'together' the beat — herald and Lord as co-workers at one task.",
        "scene": (
            "In the slow green water the two men "
            "square to each other — John's consent "
            "arrived at last in his steadied "
            "shoulders and his hands rising now to "
            "their office, Jesus turning to stand "
            "ready before him — the desert's roughest "
            "prophet and Galilee's carpenter taking "
            "up, together, the first shared task of "
            "the new world: doing everything right. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r069-b14", "out": "s14-he-was-stepping-into-line.jpeg", "seg": "n3",
        "window": "75.04-77.11", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CROWD", "JORDAN"],
        "narration": "He was stepping into line with us.",
        "must_show": "the solidarity wide — Jesus in the water WITH the day's penitents visible up the bank behind him: the line he joined, kept in frame at his baptism.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the 'us' visible — his baptism composed as one of many, deliberately.",
        "scene": (
            "In the river Jesus stands where every "
            "penitent has stood all morning — the "
            "same trodden entry slope behind him, the "
            "same waiting line visible up the bank: "
            "the soldier, the tax man, the old "
            "praying woman, all of them in frame with "
            "him — one baptism composed among the "
            "day's many, exactly as its subject "
            "intended it to be seen. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b15", "out": "s15-if-baptism-is-the-doorway.jpeg", "seg": "n3",
        "window": "77.11-90.95", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JORDAN"],
        "narration": (
            "If baptism is the doorway God asks people to walk through, then "
            "Jesus would walk through it first — not because he needed it, but "
            "so that no one who ever walks through it after him walks through "
            "it alone."
        ),
        "must_show": "the doorway doctrine — Jesus at the water's deepest entry point, about to go under: the threshold crossed FIRST; the river as a door with him in its frame.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the first-through-the-door geometry — his body at the exact place every later body will be.",
        "scene": (
            "At the river's deep entry Jesus stands "
            "chest-deep at the exact spot worn by "
            "every morning's penitents — the water's "
            "threshold holding him in its frame like "
            "a doorway holds a man about to enter — "
            "his face calm toward the going-under, "
            "first in a line that will stretch out of "
            "this river across every continent and "
            "century, so that none of them, ever, "
            "goes through alone. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b16", "out": "s16-you-coming-to-me-makes.jpeg", "seg": "n1b",
        "window": "44.06-46.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTIST"],
        "narration": "You coming to ME makes no sense.",
        "must_show": "the protest's heart — extreme close on John's hand pressed flat to his own camel-hair chest: ME, the unworthy direction; the pronoun as gesture.",
        "must_not_show": "no halo, glare or rim-light; the self-indication the whole beat — a prophet pointing at his own need.",
        "scene": (
            "Extreme close in the river light: John's "
            "burned hand pressed flat against his own "
            "camel-hair chest — the ME of his protest "
            "made physical, fingers spread over the "
            "rough coat and the heart under it — a "
            "prophet indicating, with the desert's "
            "bluntness, the one address in Israel he "
            "is certain grace has better places to "
            "visit than. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b17", "out": "s17-he-never-leads-from-behind.jpeg", "seg": "n3 + n4",
        "window": "90.95-99.19", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": (
            "He never leads from behind. So John baptized him — lowered him "
            "under the water of the Jordan, and raised him up again."
        ),
        "must_show": "SCRIPTURE-EXACT: the baptism — John's hands lowering Jesus back beneath the green surface, the immersion mid-act; the Jordan closing over the cream robe.",
        "must_not_show": "no halo, glare or rim-light; the going-under real and complete — water doing what water does, over the one who never needed it.",
        "scene": (
            "In the slow green Jordan the act itself: "
            "John's weathered hands firm at shoulder "
            "and clasped wrists, lowering Jesus "
            "backward beneath the surface — the cream "
            "robe darkening as the water takes it, "
            "the face going under calm and open-eyed, "
            "the river folding over him the way it "
            "has folded over every sinner all morning "
            "— the doorway, entered first, all the "
            "way. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r069-b18", "out": "s18-and-as-jesus-came-straight.jpeg", "seg": "n4",
        "window": "99.19-104.24", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JORDAN"],
        "narration": (
            "And as Jesus came straight up out of the water, the sky itself "
            "broke open."
        ),
        "must_show": "SCRIPTURE-EXACT: the rising and the opening — Jesus coming straight up streaming, and above the valley the cloud deck breaking into a great bright rift of clear sky.",
        "must_not_show": "NO rays, NO beams, no figures in the rift — a magnificent NATURAL cloud-break's brightness; his rising and the sky's opening simultaneous.",
        "scene": (
            "Jesus comes straight up out of the "
            "river — water streaming from his hair "
            "and beard, the wet robe clinging, his "
            "face lifted — and above the whole "
            "valley the grey cloud deck is breaking "
            "open as he rises: a great rift of "
            "clean bright sky tearing wide from "
            "horizon to horizon, daylight doubling "
            "on the water — a man surfacing and a "
            "sky unsealing in one shared instant. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r069-b19", "out": "s19-it-should-be-the-other.jpeg", "seg": "n1b",
        "window": "42.12-44.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": "It should be the other way around.",
        "must_show": "the direction disputed — John's hand gesturing from himself toward Jesus and back: the flow of worthiness, drawn in the air the wrong way and the right way.",
        "must_not_show": "no halo, glare or rim-light; the gesture's two directions the whole grammar.",
        "scene": (
            "Over the green water John's hand draws "
            "the argument in the air — sweeping from "
            "his own chest toward the man before him, "
            "then reversing, palm up, baffled — the "
            "traffic of worthiness diagrammed by a "
            "desert hand that has never once been "
            "confused about anything until this "
            "morning, and is now confused in exactly "
            "the right direction. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b20", "out": "s20-the-spirit-of-god-came.jpeg", "seg": "n5",
        "window": "104.84-111.52", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DOVE", "JORDAN"],
        "narration": (
            "The Spirit of God came down through the opened heavens like a "
            "dove, gentle as falling light, and rested on him."
        ),
        "must_show": "SCRIPTURE-EXACT: the descent — the one white dove descending through the bright cloud-rift in a long gentle glide toward the standing Jesus; a real bird, unmistakable and plain.",
        "must_not_show": "the dove NEVER radiant, translucent or haloed — pure white feathers in real light; no rays following it; gentleness carried by the glide's angle.",
        "scene": (
            "Down through the great bright rift the "
            "white dove comes — a real bird in a "
            "long unhurried glide, wings set, "
            "descending the whole height of the "
            "opened sky toward the man standing "
            "streaming in the river — its whiteness "
            "plain feather-white in the doubled "
            "daylight, its path a single soft "
            "diagonal from heaven's tear to a wet "
            "human shoulder. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b21", "out": "s21-and-then-from-above-not.jpeg", "seg": "n5",
        "window": "111.52-118.63", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DOVE", "BAPTIST", "JORDAN", "CROWD"],
        "narration": (
            "And then, from above — not John, not anyone on the riverbank — the "
            "Father himself spoke."
        ),
        "must_show": "the voice's arrival — the dove at rest on Jesus's shoulder, and every face on the bank lifting at once toward the opened sky; the hearing painted, the speaker never.",
        "must_not_show": "NO source of the voice — no form, no light in the rift; the words exist ONLY in the upturned faces; no halo on the dove or anyone.",
        "scene": (
            "The dove has settled at rest on Jesus's "
            "wet shoulder — and along the whole "
            "riverbank every face lifts at once: "
            "John's mane falling back as his chin "
            "rises, the soldier's helmet sliding "
            "from under his arm, the old woman's "
            "prayer stopping open-mouthed — a "
            "hundred faces hearing the same thing "
            "from the same empty brightness, which "
            "the picture, rightly, shows as sky and "
            "nothing else. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b22", "out": "s22-and-lo-a-voice-from.jpeg", "seg": "s17 + jv1",
        "window": "119.25-126.46", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DOVE"],
        "narration": (
            "And lo a voice from heaven, saying, This is my beloved Son, in "
            "whom I am well pleased."
        ),
        "must_show": "SCRIPTURE-EXACT: the sentence landing on its subject — close on Jesus's face as the Father's words arrive: belovedness received, the dove white at his shoulder.",
        "must_not_show": "no halo, glare or rim-light; the reception the beat — a Son hearing his Father say it out loud, in front of everyone.",
        "scene": (
            "Close on Jesus's streaming face as the "
            "words arrive from the bright emptiness "
            "above: the warm eyes closing briefly, "
            "the wet beard's jaw steadying, something "
            "settling through the features like "
            "bread reaching the hungry — the dove's "
            "plain white at his shoulder — a Son "
            "being told, before one sermon or one "
            "miracle, in the hearing of a whole "
            "riverbank, exactly whose and exactly "
            "how loved. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b23", "out": "s23-stand-on-that-riverbank-for.jpeg", "seg": "n6",
        "window": "127.54-131.81", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DOVE", "JORDAN", "CROWD"],
        "narration": (
            "Stand on that riverbank for a second. The Son is standing in the "
            "water."
        ),
        "must_show": "the first Person located — the wide riverbank view a witness would have had: the Son plainly IN THE WATER, distinct, real, wet; the viewer placed on the bank.",
        "must_not_show": "no halo, glare or rim-light; the theology geographic — where each Person IS, beginning with the Son's river.",
        "scene": (
            "From the trodden bank the camera stands among the "
            "witnesses, behind their shoulders — the witness's own "
            "view: the river's green breadth, and "
            "standing in it — wet, real, distinct — "
            "the Son, cream robe dark with Jordan "
            "water, the settled dove white at his "
            "shoulder, John a pace off with his hands "
            "still half-raised — the first Person of "
            "the moment located exactly where a "
            "bystander's finger could point: there, "
            "in the water. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b24", "out": "s24-the-spirit-is-descending-upon.jpeg", "seg": "n6",
        "window": "131.81-136.48", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DOVE"],
        "narration": "The Spirit is descending upon him. The Father is speaking from heaven.",
        "must_show": "the second and third located — close: the DOVE distinctly at rest upon the Son's shoulder, and his face lifted toward the heard-but-unseen height; two more Persons, two more locations.",
        "must_not_show": "NO merging, no symbol-fusion — bird distinctly bird, voice distinctly absent from view; the distinctness IS the doctrine.",
        "scene": (
            "Close on the shoulder and the lifted "
            "face: the white dove wholly itself — "
            "feathers, folded wings, a bird's small "
            "weight visibly settled on wet cream "
            "wool — and above it the Son's face "
            "turned up toward a height the frame "
            "keeps empty and bright — Spirit resting, "
            "Father heard, Son standing: three "
            "locations, three realities, one moment, "
            "nothing blended. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b25", "out": "s25-he-was-not-washing-anything.jpeg", "seg": "n3",
        "window": "72.33-75.04", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JORDAN"],
        "narration": "He was not washing anything away.",
        "must_show": "the clean one in the water — close on Jesus's face just before immersion: nothing to shed, everything to begin; purpose without penitence.",
        "must_not_show": "no halo, glare or rim-light; the face confession-free and completely willing — obedience as its own reason.",
        "scene": (
            "Close on Jesus's face above the green "
            "water in the instant before the "
            "going-under: none of the morning's "
            "penitent weight anywhere in it — no "
            "ledger closing behind the eyes, no "
            "relief pre-gathering — only the calm "
            "forward willingness of a man entering "
            "a door because others will need it "
            "entered, carrying nothing to the water "
            "but obedience. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b26", "out": "s26-three-each-one-distinct-each.jpeg", "seg": "n6",
        "window": "136.48-150.88", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DOVE", "BAPTIST", "JORDAN", "CROWD"],
        "narration": (
            "Three — each one distinct, each one present, all in one moment — "
            "and what the Father chose to say, before Jesus had preached one "
            "sermon or healed one person, was: I love him, and I am pleased "
            "with him."
        ),
        "must_show": "SCRIPTURE-DOCTRINE: the whole moment in one frame — Son in the water, dove upon him, the bright opened sky above, the hearing bank around: three distinct Persons' evidence in a single true scene.",
        "must_not_show": "NO triangle symbols, no rays linking sky-bird-man, no merging — the scene painted as the witnesses saw it: a man, a bird, a heard sky.",
        "scene": (
            "One frame holds the whole moment, the camera at the "
            "bank's side taking water and watchers in profile, as the "
            "bank saw it: the Son standing wet and "
            "real in the green river, the white dove "
            "at rest upon his shoulder, the great "
            "bright rift standing open in the cloud "
            "above the valley — and around the water "
            "the hundred lifted faces of the "
            "witnesses, John foremost, hearing words "
            "the picture will not pretend to show — "
            "three Persons present to one riverbank, "
            "each exactly where scripture put them. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r069-b27", "out": "s27-approval-before-achievement.jpeg", "seg": "n6",
        "window": "150.88-153.36", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Approval before achievement.",
        "must_show": "the order as image — a close still: an unused carpenter's toolbag and an unopened scroll-satchel resting on the bank; the résumé still empty, the love already spoken.",
        "must_not_show": "no halo, glare or rim-light; the emptiness of the record the beat — nothing done yet, everything already loved.",
        "scene": (
            "A close still on the riverbank grass: a "
            "traveller's plain satchel resting "
            "unopened beside a folded outer cloak — "
            "no sermon notes, no lists of the "
            "healed, no record of anything yet done "
            "— the complete luggage of a ministry "
            "not one day old, lying on a bank where "
            "the owner has just been called beloved "
            "with the bag still shut. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r069-b28", "out": "s28-jesus-began-everything-from-that.jpeg", "seg": "n7",
        "window": "154.00-159.62", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JORDAN"],
        "narration": (
            "Jesus began everything from that sentence. Not working TOWARD "
            "being loved — working FROM it."
        ),
        "must_show": "the departure founded — Jesus walking up out of the river onto the far bank toward the wilderness, wet and resolute; a ministry leaving its launch point.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the direction forward — a man walking FROM a sentence into everything.",
        "scene": (
            "Up the far bank Jesus walks out of the "
            "Jordan — wet robe heavy, steps sure, "
            "his face set toward the pale wilderness "
            "hills where the next forty days wait — "
            "a man leaving the water with nothing "
            "proven and everything settled, walking "
            "not toward a verdict but away from "
            "one, already delivered, already his. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r069-b29", "out": "s29-and-the-doorway-he-walked.jpeg", "seg": "n7",
        "window": "159.62-164.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTIST", "JORDAN", "CROWD"],
        "narration": (
            "And the doorway he walked through that day, he left standing open "
            "behind him."
        ),
        "must_show": "the closing image — the river bend continuing its work: John baptizing the NEXT penitent in the same water, the line moving; the door open, in use, forever.",
        "must_not_show": "no halo, glare or rim-light; the continuation the point — the same entry slope, the next person, the open door working.",
        "scene": (
            "At the same green bend the door stands "
            "open and working: John waist-deep with "
            "the next penitent — the old praying "
            "woman, her face already breaking — the "
            "line moving down the trodden slope "
            "behind her, the river receiving as it "
            "will receive for twenty centuries — the "
            "water still stirred from the one who "
            "went through first, and the doorway he "
            "left open filling, person by person, "
            "behind him. Every figure has two arms, "
            "two hands and one head."
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
