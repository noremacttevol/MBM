#!/usr/bin/env python3
"""V2 beat map — row 108, build-108-my-sheep-hear-my-voice (John 10:1-28).

COVERAGE: 23 pictures over 132.8 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (John 10 KJV):
  v3    "the sheep HEAR HIS VOICE: and he calleth his own sheep BY
        NAME, and LEADETH THEM OUT." — a Near-East shepherd LEADS
        from the front; sheep follow the known voice.
  v4-5  "he goeth BEFORE them... a STRANGER will they not follow" —
        several flocks shared one fold; each answered only its own
        shepherd's call.
  v11   "I AM THE GOOD SHEPHERD: the good shepherd GIVETH HIS LIFE
        for the sheep."
  v27   "MY sheep hear MY voice, and I KNOW them, and they FOLLOW
        me."
  v28   "I give unto them ETERNAL LIFE; and they shall NEVER PERISH,
        neither shall any man PLUCK THEM OUT OF MY HAND."

STAGING: the cultural beats (b01-b03, b17) use a GENERIC dark-robed
shepherd — the custom explained; from the I-AM beats onward the
shepherd IS Jesus (cream robe, jesus=True + REF) with the flock. The
sheep-are-people turn (b14-b15) blends flock and human faces in the
same warm light.

TIME OF DAY ARC (intentional): dawn at the shared fold; bright green
day in the pasture beats; golden EVENING for the homecoming count
and close. Correct story lighting, not the row-11 defect.

CONTENT-CARE: no flags. The giveth-his-life beat carried by tone and
posture only — no cross imagery in this pastoral row.

CHANGING CONDITION (kept OUT of the locks): the light — dawn, day,
gold evening; the flock — folded, led out, resting, carried,
gathered home; the voice — the row's invisible constant.
"""

# LOCKS: one entry per recurring person and per setting. Clothing colours
# stated POSITIVELY and dark — only Jesus wears cream.
LOCKS = {
    "FOLD": (
        "FOLD LOCK: the sheepfold — a round DRY-STONE enclosure on a "
        "hillside with ONE gap-gate in its wall, worn smooth by "
        "generations of wool; the same walls and gate throughout."
    ),
    "HILLS": (
        "HILLS LOCK: the pasture country — green terraced hills with "
        "outcrops of pale stone, a STILL POOL fed by a quiet stream "
        "in a hollow, olives on the ridges. The same hills and water "
        "throughout."
    ),
    "SHEP": (
        "SHEP LOCK: the generic shepherd of the custom-beats is the "
        "same man in every such shot — about forty, weathered, short "
        "dark beard, in a DARK OLIVE mantle with a CHARCOAL head "
        "cloth (never cream, never white), a long crook in hand."
    ),
    "FLOCK": (
        "FLOCK LOCK: the sheep — a modest mixed flock of grey-white "
        "and brown-black sheep with several lambs; woolly, real, "
        "individually varied so single sheep can be recognized."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r108-b01", "out": "s01-in-that-world-a-shepherd.jpeg", "seg": "n1",
        "window": "0.28-3.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLS", "SHEP", "FLOCK"],
        "narration": "In that world, a shepherd did not drive his sheep from behind.",
        "must_show": "the not-driving — the custom stated by contrast: the olive-mantled shepherd walking AHEAD on the hill path, no rod raised behind the flock; the arrangement itself.",
        "must_not_show": "no halo; NO driving imagery — no one behind the flock, no raised stick.",
        "scene": (
            "The old arrangement walks "
            "across the green morning "
            "hill: the shepherd out in "
            "FRONT on the worn path, "
            "crook swinging easy at his "
            "side, his back to the "
            "flock — and behind him, "
            "unforced and undriven, the "
            "sheep strung along in his "
            "footsteps with no rod at "
            "their heels and nothing "
            "herding them but the sound "
            "of him ahead — leadership "
            "from the front, old as "
            "the hills it crosses. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r108-b02", "out": "s02-he-walked-out-in-front.jpeg", "seg": "n1",
        "window": "3.39-10.08", "wide": True, "jesus": False, "ref": False,
        "locks": ["HILLS", "SHEP", "FLOCK"],
        "narration": (
            "He walked out in front of them, and they followed — not "
            "because they were forced, but because they knew his voice."
        ),
        "must_show": "the voice-following — the shepherd calling back over his shoulder as he walks, and the flock's heads UP and moving to the sound; the invisible leash of a known voice.",
        "must_not_show": "no halo; the following VOLUNTARY — ears turned, heads lifted, no fence or rope anywhere.",
        "scene": (
            "The invisible leash shows itself, the camera beside "
            "the path taking man and strung flock in one profile: "
            "the shepherd "
            "calling back over his "
            "shoulder as he walks — a "
            "low easy singsong worn "
            "smooth by years — and "
            "along the path behind him "
            "every woolly head coming "
            "UP at the sound, ears "
            "swiveling, hooves picking "
            "up their pace toward the "
            "voice and nothing but the "
            "voice — no rope on any "
            "neck, no fence on either "
            "side, a whole flock held "
            "to one man by sound and "
            "trust alone. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r108-b03", "out": "s03-several-flocks-might-share-one.jpeg", "seg": "n2",
        "window": "10.64-13.45", "wide": True, "jesus": False, "ref": False,
        "locks": ["FOLD", "FLOCK"],
        "narration": "Several flocks might share one fold overnight.",
        "must_show": "SCRIPTURE-EXACT: the shared fold — dusk at the stone enclosure: two or three flocks mingled inside the walls, indistinguishable; shepherds' fires outside the one gate.",
        "must_not_show": "no halo; the MINGLING total — no visible sorting, one woolly crowd.",
        "scene": (
            "At dusk, the camera on the slope behind the arriving "
            "flocks' woolly backs, the stone circle "
            "takes in everyone's wool: "
            "two flocks, three, filing "
            "through the single gap-"
            "gate and mingling inside "
            "the dry-stone walls into "
            "one indistinguishable "
            "grey-and-brown sea of "
            "backs — no brands legible "
            "in the fading light, no "
            "sorting possible to any "
            "human eye — while outside "
            "the gate the shepherds' "
            "small fires wink on, "
            "owners of a mixed "
            "multitude only morning "
            "voices will be able to "
            "divide. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r108-b04", "out": "s04-they-could-tell-his-voice.jpeg", "seg": "n2",
        "window": "18.93-24.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD", "FLOCK", "SHEP"],
        "narration": (
            "They could tell his voice from a stranger's. That is the "
            "picture Jesus reaches for."
        ),
        "must_show": "the discrimination close — at the morning gate: sheep streaming to the olive-mantled caller while ignoring another man calling nearby; the known voice winning.",
        "must_not_show": "no halo; BOTH callers visible — one answered, one comprehensively ignored.",
        "scene": (
            "Close at the gate, the "
            "morning's quiet miracle of "
            "discrimination: two men "
            "calling across each other — "
            "a stranger's perfectly "
            "good voice going out over "
            "the wool and landing on "
            "nothing, not one ear "
            "turning — while at the "
            "olive-mantled shepherd's "
            "first low note the right "
            "heads lift out of the "
            "mixed sea and come, "
            "threading through the "
            "other flocks straight to "
            "their own voice — known, "
            "against all others. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r108-b05", "out": "s05-he-knows-them-one-at.jpeg", "seg": "n3",
        "window": "24.69-26.29", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FLOCK"],
        "narration": "He knows them one at a time.",
        "must_show": "the knowing begins with HIM — close: Jesus's hand on one particular sheep's face, eye to eye with it; singular attention, the shepherd now himself.",
        "must_not_show": "no halo, glare or rim-light; ONE sheep the subject — known singly, not scanned as herd.",
        "scene": (
            "The picture finds its true "
            "shepherd: Jesus down on "
            "one knee with a single "
            "ewe's face cupped in his "
            "hand — eye to eye with "
            "this one, the torn ear "
            "known, the old limp "
            "remembered, the particular "
            "stubbornness smiled at — "
            "one animal out of the "
            "many, held in the kind of "
            "attention that has never "
            "once in its life counted "
            "by tens. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r108-b06", "out": "s06-not-a-nameless-herd-each.jpeg", "seg": "n3",
        "window": "26.29-35.56", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLS", "FLOCK"],
        "narration": (
            "Not a nameless herd — each one, called by its own name, "
            "gently, personally. And knowing his voice, they come to him "
            "and follow."
        ),
        "must_show": "SCRIPTURE-EXACT: by name — Jesus on the green hill calling individuals out: one sheep trotting to him, others lifting heads in turn; the flock resolving into persons.",
        "must_not_show": "no halo, glare or rim-light; the CALLING serial — one name at a time, one responder at a time visible.",
        "scene": (
            "The herd dissolves into names, the camera at the "
            "hillside's flank so caller and trotting called read "
            "in profile: "
            "names on the green hill: "
            "Jesus calling low and one "
            "at a time — and one at a "
            "time they answer: a brown "
            "ewe already trotting to "
            "his knee, a grey one "
            "lifting her head mid-"
            "graze at her own sound, a "
            "lamb wheeling from its "
            "game — each called gently, "
            "each coming singly, the "
            "anonymous woolly crowd "
            "turning out to be persons "
            "all the way down, every "
            "one of them known first "
            "and followed after. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r108-b07", "out": "s07-the-sheep-hear-his-voice.jpeg", "seg": "jv3",
        "window": "36.16-41.96", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FOLD", "FLOCK"],
        "narration": (
            "The sheep hear his voice: and he calleth his own sheep by "
            "name, and leadeth them out."
        ),
        "must_show": "SCRIPTURE-EXACT: leadeth them out — Jesus at the fold's gate in morning light, his own streaming out to him from the mixed flocks within; the leading-out mid-happening.",
        "must_not_show": "no halo, glare or rim-light; his own SORTING THEMSELVES out of the mix at the voice — the gate the verse's hinge.",
        "scene": (
            "The verse happens at the "
            "gap in the stones: Jesus "
            "standing in the morning "
            "light at the fold's one "
            "gate, calling — and out "
            "of the mixed grey-brown "
            "sea inside, his own "
            "come: threading between "
            "strangers' flanks, "
            "funnelling through the "
            "gate past his knees one "
            "and two and three at a "
            "time, sorting themselves "
            "by nothing but the sound "
            "of him — called by name, "
            "led out, the day begun. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r108-b08", "out": "s08-my-sheep-hear-my-voice.jpeg", "seg": "jv27",
        "window": "43.40-46.65", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FLOCK"],
        "narration": "My sheep hear my voice, and I know them, and they follow me:",
        "must_show": "SCRIPTURE-EXACT: the claim close — Jesus's warm face over the flock pressing near: MY sheep; possession as tenderness, the following at his heels.",
        "must_not_show": "no halo, glare or rim-light; the MY affectionate — ownership indistinguishable from love.",
        "scene": (
            "Close on the possessive "
            "that sounds like love: "
            "Jesus's warm face above "
            "the wool pressing in "
            "around his knees — MY "
            "sheep — the word carrying "
            "no deed-of-purchase "
            "hardness at all, only the "
            "way a mother says my in "
            "the dark — I KNOW THEM — "
            "and the flock's trusting "
            "crowding at his legs "
            "answering the sentence's "
            "last clause before he "
            "says it: they follow. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r108-b09", "out": "s09-he-leads-them-to-green.jpeg", "seg": "n4",
        "window": "48.16-52.83", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLS", "FLOCK"],
        "narration": (
            "He leads them to green places and still water, to rest and to "
            "plenty."
        ),
        "must_show": "the green and the still — the hollow's pool: flock spread grazing the deep green, some drinking at the still water, Jesus at rest on a stone among them; psalm-peace.",
        "must_not_show": "no halo, glare or rim-light; the water STILL — mirror-calm; rest total across the frame.",
        "scene": (
            "The old psalm gets its "
            "picture: the hollow deep "
            "green in the day's soft "
            "light, the pool lying "
            "mirror-still under its "
            "quiet stream, the flock "
            "spread wide and easy — "
            "some grazing belly-deep "
            "in the good grass, some "
            "drinking at the unmoving "
            "water, lambs flat out "
            "asleep in the warmth — "
            "and on a pale stone among "
            "them the shepherd at "
            "rest, the whole hollow "
            "breathing at the pace he "
            "set for it: plenty, and "
            "peace. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r108-b10", "out": "s10-and-when-one-is-small.jpeg", "seg": "n4",
        "window": "52.83-61.12", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLS", "FLOCK"],
        "narration": (
            "And when one is small or tired or hurt, he does not scold it "
            "for falling behind — he lifts it up and carries it."
        ),
        "must_show": "the carrying — Jesus with a spent lamb draped across his shoulders on the climbing path, his hands steadying its legs; no scolding, all carriage.",
        "must_not_show": "no halo, glare or rim-light; the lamb LIMP-relaxed on his shoulders — safe, not struggling.",
        "scene": (
            "The one that couldn't make "
            "the hill rides home: a "
            "spent lamb draped limp "
            "and easy across Jesus's "
            "shoulders, his two hands "
            "steadying the small legs "
            "against his chest as he "
            "climbs the path — no "
            "scolding spent on it, no "
            "lesson about keeping up — "
            "just the oldest solution "
            "in the shepherd's whole "
            "art: what cannot walk "
            "gets carried, on the "
            "same shoulders that "
            "carry everything. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r108-b11", "out": "s11-led-not-driven.jpeg", "seg": "n7b",
        "window": "120.07-122.24", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLS", "FLOCK"],
        "narration": "Led, not driven.",
        "must_show": "the summary image — the evening path: Jesus ahead, flock following free and willing; the row's whole grammar in one silhouette-warm frame.",
        "must_not_show": "no halo, glare or rim-light; NOTHING behind the flock — the following pure.",
        "scene": (
            "The whole teaching walks "
            "in one evening line: the "
            "shepherd out ahead on the "
            "gold-lit ridge path, and "
            "the flock strung willing "
            "and easy behind him — "
            "nothing at their heels "
            "but their own choosing, "
            "nothing pulling but the "
            "voice up front — led, "
            "not driven, drawn, not "
            "pushed, the grammar of "
            "the whole kingdom "
            "written in wool against "
            "the evening sky. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r108-b12", "out": "s12-i-am-the-good-shepherd.jpeg", "seg": "jv11 + n4b",
        "window": "61.65-70.24", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FLOCK"],
        "narration": (
            "I am the good shepherd: the good shepherd giveth his life for "
            "the sheep. That is what he was willing to spend to keep them."
        ),
        "must_show": "SCRIPTURE-EXACT: the cost named — close on Jesus's face over the flock as he says GIVETH HIS LIFE: the sentence's full weight carried in steady eyes; no cross imagery.",
        "must_not_show": "ABSOLUTE: no cross or passion imagery — the price entirely in tone and the steady face; no halo.",
        "scene": (
            "Close on the price being "
            "named in a green field: "
            "I AM THE GOOD SHEPHERD — "
            "the warm face steady over "
            "the grazing wool — THE "
            "GOOD SHEPHERD GIVETH HIS "
            "LIFE — and for one beat "
            "the eyes carry the whole "
            "cost of the job "
            "description, known and "
            "accepted long ago: not "
            "wages, not wool, but "
            "everything — said quietly "
            "over the heads of the "
            "flock it will be spent "
            "on, none of whom will "
            "ever fully know. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r108-b13", "out": "s13-that-is-what-he-was.jpeg", "seg": "n4b",
        "window": "70.24-73.37", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FLOCK"],
        "narration": "That is what he was willing to spend to keep you.",
        "must_show": "the you — Jesus's direct gaze lifted from the flock toward the viewer, one hand resting on wool; the price's beneficiary addressed.",
        "must_not_show": "no halo, glare or rim-light; the gaze DIRECT to camera — the sentence finds its address.",
        "scene": (
            "The sentence turns and "
            "finds its address: Jesus's "
            "gaze lifting from the "
            "wool under his hand, "
            "straight out of the frame "
            "to whoever is watching — "
            "the warm brown eyes "
            "carrying the arithmetic "
            "personally now: that "
            "price, willingly, for "
            "YOU — one hand still "
            "resting on a grazing "
            "back, the other open at "
            "his side, the flock's "
            "newest name already known "
            "before it answers. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r108-b14", "out": "s14-and-here-is-the-turn.jpeg", "seg": "n5",
        "window": "73.96-77.78", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLS"],
        "narration": "And here is the turn: the sheep are people. You.",
        "must_show": "the turn — the pasture's composition echoed with PEOPLE: ordinary men, women and children gathered on the green slope around Jesus exactly as the flock was.",
        "must_not_show": "no halo, glare or rim-light; the ECHO deliberate — same hill, same arrangement, human faces now.",
        "scene": (
            "The parable takes off its "
            "wool: the same green "
            "slope, the same easy "
            "gathered arrangement — but "
            "people now: a tired "
            "laborer sitting where the "
            "brown ewe grazed, a "
            "mother and her children "
            "resting by the still "
            "water, an old man leaning "
            "on his stick at the "
            "path's edge — the flock "
            "of the whole teaching "
            "standing revealed around "
            "its shepherd, ordinary "
            "and beloved, and every "
            "face in it somebody's "
            "yours. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r108-b15", "out": "s15-tired-wandering-easily-lost-people.jpeg", "seg": "n5",
        "window": "77.78-86.82", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLS"],
        "narration": (
            "Tired, wandering, easily lost people, whom he knows by name "
            "and leads with his voice and gathers close and will not lose."
        ),
        "must_show": "the human flock tended — Jesus moving among the gathered people as he did the sheep: a hand to the tired man, a word to the wanderer at the edge, the gathering visible.",
        "must_not_show": "no halo, glare or rim-light; the SAME gestures as the sheep beats — hand, voice, gathering; the rhyme exact.",
        "scene": (
            "He tends them, the camera behind the gathered "
            "people's shoulders, exactly as "
            "he tended wool: crossing "
            "the slope to crouch at "
            "the tired laborer's side "
            "with a hand on his "
            "shoulder, calling gently "
            "up the hill to the "
            "restless young man "
            "drifting toward the "
            "ridge — who stops, and "
            "turns — drawing the "
            "mother's straggling "
            "littlest one back into "
            "the circle with two "
            "fingers and a smile — "
            "name by name, voice and "
            "hand, the easily lost "
            "being visibly kept. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r108-b16", "out": "s16-and-i-give-unto-them.jpeg", "seg": "jv28",
        "window": "87.32-95.03", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": (
            "And I give unto them eternal life; and they shall never "
            "perish, neither shall any man pluck them out of my hand."
        ),
        "must_show": "SCRIPTURE-EXACT: the hand — close on Jesus's strong open hand held out, steady as bedrock; the never-pluck promise carried by the hand itself.",
        "must_not_show": "no halo, glare or rim-light; the hand CALM and open — security shown as steadiness, not gripping.",
        "scene": (
            "Close on the safest place "
            "in the universe: one "
            "strong sun-browned hand "
            "held open and steady in "
            "the warm light — calloused "
            "from work, scarred from "
            "living, calm as bedrock — "
            "not clenched around its "
            "keeping but open beneath "
            "it, the way a hand holds "
            "water it will not spill — "
            "NEVER PERISH — NEITHER "
            "SHALL ANY — a grip made "
            "not of pressure but of "
            "faithfulness, from which "
            "nothing has ever been "
            "successfully stolen. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r108-b17", "out": "s17-but-in-the-morning-when.jpeg", "seg": "n2",
        "window": "13.45-18.93", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD", "FLOCK", "SHEP"],
        "narration": (
            "But in the morning, when a shepherd called, only his own sheep "
            "lifted their heads and came."
        ),
        "must_show": "SCRIPTURE-EXACT: the morning sorting — dawn at the fold: the olive-mantled shepherd calling at the gate, HIS sheep's heads up and moving through the mixed crowd; the rest grazing on.",
        "must_not_show": "no halo; the SELECTIVITY plain — responders and non-responders both visible in one frame.",
        "scene": (
            "Dawn solves what the dark "
            "mixed up: at the gap-gate "
            "the shepherd's morning "
            "call goes out over the "
            "crowded wool — and the "
            "fold divides itself by "
            "hearing: here and there "
            "through the mixed sea, "
            "particular heads come UP "
            "and start threading "
            "toward the voice, while "
            "all around them other "
            "flocks graze on unmoved, "
            "the call passing through "
            "them like weather — his "
            "own, and only his own, "
            "answering. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r108-b18", "out": "s18-once-you-are-in-his.jpeg", "seg": "n6",
        "window": "96.52-102.49", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FLOCK"],
        "narration": (
            "Once you are in his hand, it is over — for the fear, that is. "
            "Never be snatched away."
        ),
        "must_show": "the fear ended — a lamb settled wholly at ease in the crook of Jesus's arm: limpness of total safety; fear visibly over.",
        "must_not_show": "no halo, glare or rim-light; the ease ABSOLUTE — no vigilance left in the carried creature.",
        "scene": (
            "Close on what the end of "
            "fear looks like: a lamb "
            "settled into the crook of "
            "his arm with its whole "
            "weight surrendered — legs "
            "folded any way they fell, "
            "eyes half-lidded, the "
            "little ribs rising slow — "
            "not one fibre of it "
            "keeping watch anymore, "
            "every alarm it was born "
            "with switched off in the "
            "one place on earth where "
            "vigilance has nothing "
            "left to do — in the "
            "hand, and done being "
            "afraid. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r108-b19", "out": "s19-not-by-your-failures-not.jpeg", "seg": "n6",
        "window": "102.49-111.66", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLS", "FLOCK"],
        "narration": (
            "Not by your failures, not by your enemies, not by death "
            "itself. His grip on you does not depend on how tightly you can "
            "hold on to him."
        ),
        "must_show": "the grip's direction — Jesus carrying a lamb through rough weather on the ridge: wind and dark cloud beyond, the lamb held fast though it holds nothing; the security one-directional.",
        "must_not_show": "no halo, glare or rim-light; the lamb's hooves GRIP NOTHING — all the holding is his; the storm distant, the carry calm.",
        "scene": (
            "The direction of the grip "
            "settles everything: on the "
            "high ridge with the wind "
            "up and dark weather "
            "standing off beyond the "
            "hills, Jesus carries the "
            "lamb fast against his "
            "chest — and the lamb "
            "holds nothing: no grip in "
            "the small hooves, no "
            "strength in the tired "
            "neck, its whole safety "
            "resting one hundred "
            "percent in arms that do "
            "not tire — failures, "
            "enemies, death itself "
            "welcome to try those "
            "arms, none of them ever "
            "having won. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r108-b20", "out": "s20-he-leads-them-home-in.jpeg", "seg": "n7",
        "window": "112.23-117.67", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FOLD", "FLOCK"],
        "narration": (
            "He leads them home in the evening to the safe fold, and counts "
            "them in, and none are missing."
        ),
        "must_show": "the evening count — golden dusk at the fold: the flock filing in through the gate under Jesus's touching hand, each counted by contact; none missing.",
        "must_not_show": "no halo, glare or rim-light; the counting BY HAND — his palm brushing each back at the gate.",
        "scene": (
            "The day ends the way good "
            "days do, counted: golden "
            "dusk at the stone circle, "
            "the flock filing one by "
            "one through the gap-gate — "
            "and at the gate the "
            "shepherd's hand touching "
            "every back as it passes: "
            "this one, this one, this "
            "one, the census taken by "
            "palm and not by number — "
            "until the last lamb is "
            "brushed through into "
            "safety and the tally "
            "stands where it stands "
            "every single night: all "
            "of them; none missing. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r108-b21", "out": "s21-that-is-the-shepherd-he.jpeg", "seg": "n7b",
        "window": "118.19-120.07", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FOLD"],
        "narration": "That is the shepherd he is.",
        "must_show": "the shepherd summarized — Jesus at the fold gate in the last gold light, crook in hand, at rest and on watch at once; the identity plain.",
        "must_not_show": "no halo, glare or rim-light; rest AND watch in one posture — settled at the gate, facing the night.",
        "scene": (
            "Close at the gate on the "
            "whole job description in "
            "one posture: Jesus settled "
            "against the fold's stone "
            "gap with the crook loose "
            "in his hand, the flock "
            "safe and murmuring at his "
            "back, his face turned "
            "easy toward the coming "
            "night — at rest and on "
            "watch in the same body, "
            "the door of the sheep "
            "made flesh and leaning "
            "in its own frame — that "
            "shepherd; that one, "
            "exactly. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r108-b22", "out": "s22-known-not-counted-held-and.jpeg", "seg": "n7b",
        "window": "122.24-126.07", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FLOCK"],
        "narration": "Known, not counted. Held, and never let go.",
        "must_show": "the two clauses in one frame — Jesus's face bent close to one sheep held against him in the dusk: knowledge and grip, tenderness and permanence together.",
        "must_not_show": "no halo, glare or rim-light; the hold GENTLE-UNBREAKABLE — both qualities legible.",
        "scene": (
            "Close in the dusk on the "
            "two clauses at once: "
            "Jesus's face bent down "
            "beside one particular "
            "woolly head held against "
            "his chest — the knowing "
            "in his eyes personal as "
            "a name, the arm around "
            "the warm body gentle as "
            "evening and permanent as "
            "stone — known, not "
            "counted; held, and the "
            "letting-go simply not "
            "among the things those "
            "arms know how to do. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r108-b23", "out": "s23-and-even-now-he-is.jpeg", "seg": "n7b",
        "window": "126.07-132.54", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FOLD", "HILLS", "FLOCK"],
        "narration": (
            "And even now he is calling, gently, past the flock, to whoever "
            "is still outside."
        ),
        "must_show": "the closing image — night settling: the fold warm and full behind, and Jesus at the gate turned OUTWARD toward the dark hills, calling gently into them; the gate open behind him.",
        "must_not_show": "no halo, glare or rim-light; the call OUTBOUND — past the frame toward the still-outside; the gate visibly open.",
        "scene": (
            "The closing frame faces the "
            "dark with an open gate: "
            "the fold warm and full "
            "behind him, safe wool "
            "murmuring inside the "
            "stones — and Jesus turned "
            "the other way at the gap, "
            "out toward the night "
            "hills where somebody is "
            "always still out there — "
            "calling, low and patient "
            "and unhurried, past every "
            "sheep he already has, "
            "into the dark that still "
            "holds one more name he "
            "knows — the gate open "
            "behind him, and staying "
            "open. Every figure has "
            "two arms, two hands and "
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
    "FOLD": "PLACE-REF/fold.jpeg",  # build-21-lost-sheep v2-r021-b09
}
# === end PLACE-PLATES ===
