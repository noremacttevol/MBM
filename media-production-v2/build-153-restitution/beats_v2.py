#!/usr/bin/env python3
"""V2 beat map — row 153, build-153-restitution (Acts 3:1-21).

COVERAGE: 26 pictures over 148.1 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Acts 3 KJV):
  3:2   "a certain man LAME FROM HIS MOTHER'S WOMB... laid daily at
        the gate of the temple which is called BEAUTIFUL."
  3:6   "SILVER AND GOLD HAVE I NONE; but such as I have give I
        thee: In the name of Jesus Christ of Nazareth RISE UP AND
        WALK."
  3:7   "he took him BY THE RIGHT HAND, and lifted him up: and
        immediately his feet and ancle bones received strength."
  3:19  "REPENT ye therefore, and be converted... when the TIMES OF
        REFRESHING shall come from the presence of the Lord."
  3:21  "Whom the heaven must receive until the TIMES OF RESTITUTION
        OF ALL THINGS, which God hath spoken by the mouth of ALL HIS
        HOLY PROPHETS since the world began."

ROW INTENT: the restitution-of-all-things row — repentance's
refreshing now, the great putting-right promised, the prophets'
unbroken relay. BRIDGE tone toward Restoration; everything stays in
Acts' own frame.

RENDERING LAWS:
  - PETER is the shared cast token (peter sheets in CAST-V2-REF) —
    same face as every build; fisherman's build, preacher's fire.
  - THE LAME MAN with full dignity (row-15 class): lame from birth —
    carried, seated, thin-legged; NEVER grotesque; his healing shows
    strong feet and first steps, wonder not spectacle.
  - The TEMPLE is the build-06 b21 family anchor (same as rows
    43/75/131/142) — architecture only.
  - The prophets' relay (b19) is a timeless line of varied robed
    messenger figures passing the same scroll down a ridge —
    indistinct faces, no named prophet depicted.
  - b20's heaven-must-receive: sky over the temple only — vast,
    waiting; NO figure, no ascension depicted.
  - The refreshing imagery (b10/b11/b26) is REAL rain on dry land —
    physical, welcome, faces lifted to it.
  - b26's turn is the 117/133 reversal rhyme: a figure fully TURNED
    on the road toward the bright valley.

TIME OF DAY ARC (intentional): the gate healing and sermon in
bright temple morning; the dry-ground frames at parched noon; the
rain arriving in silver curtains; the kept-gift at lamplight; the
prophets' relay at ridge-line dusk; the close in freshening
storm-light turning bright.

CHANGING CONDITIONS (kept OUT of the locks): the lame man — seated
at the gate, lifted, standing, leaping; the dry land — cracked,
then rained on; the road — dusk-falling, then bending bright.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row). PETER
# comes from the shared CAST_LOCKS — do not redefine him here.
LOCKS = {
    "TEMPLE": (
        "TEMPLE LOCK: the temple courts — broad pale limestone "
        "courts with great columned porticoes, wide steps, morning "
        "light on honey-coloured stone; the gate called Beautiful "
        "with its worked bronze doors. The same courts throughout."
    ),
    "LAMEMAN": (
        "LAMEMAN LOCK: the healed man is the same in every shot — "
        "about forty, lame from birth: thin wasted legs before the "
        "healing, a strong open weathered face, in a patched DARK "
        "GREY-BROWN tunic (never cream, never white); full dignity "
        "always — begging with a held-out bowl, never abject; "
        "after the healing his legs and ankles are strong."
    ),
    "CROWD": (
        "CROWD LOCK: the temple crowd — pilgrims and townsfolk in "
        "varied earth-toned and fine dark robes (no cream — only "
        "Jesus wears cream), varied ages and faces, amazed and "
        "pressing close, never uniform."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r153-b01", "out": "s01-after-a-lame-man-was.jpeg", "seg": "n1",
        "window": "0.28-4.73", "wide": True, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "LAMEMAN", "CROWD"],
        "narration": (
            "After a lame man was healed at the temple gate, a crowd came "
            "running, amazed."
        ),
        "must_show": "the amazement — the healed man STANDING at the Beautiful gate, and the crowd running in from across the court toward him; the miracle's first minutes.",
        "must_not_show": "no halo; the man's legs STRONG now; the runners amazed, not mobbing.",
        "scene": (
            "The court's foot traffic reverses all at once, "
            "the camera looking across the flagstones past "
            "the runners' backs: at the Beautiful gate the "
            "man who has begged there for forty years is "
            "STANDING — upright on strong new legs, one hand "
            "braced on the bronze door in disbelief at his "
            "own height — and from every corner of the "
            "morning court the crowd comes running toward "
            "him, prayers abandoned mid-word, amazement "
            "outracing understanding across the honey "
            "stone. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r153-b02", "out": "s02-and-peter-a-fisherman-turned.jpeg", "seg": "n1",
        "window": "4.73-10.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "CROWD"],
        "narration": (
            "And Peter, a fisherman turned preacher, stood up among them to "
            "explain what they had really just seen."
        ),
        "must_show": "Peter rising — the fisherman's broad frame standing up above the pressing crowd on the porch steps, the preacher's moment taken; the cast-token face exact.",
        "must_not_show": "no halo; PETER per the cast sheets — fisherman's build, weathered; the crowd's attention converging.",
        "scene": (
            "The explanation stands up wearing a fisherman's "
            "shoulders: Peter rises on the porch steps above "
            "the pressing crowd — the broad net-hauling "
            "frame, the weathered face that three years of "
            "following and one terrible weekend remade — "
            "and the amazed voices fall away toward him "
            "row by row, a congregation assembling itself "
            "around a man who was mending nets the year "
            "before last and is about to explain a "
            "miracle. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r153-b03", "out": "s03-silver-and-gold-have-i.jpeg", "seg": "s6",
        "window": "11.19-18.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "LAMEMAN"],
        "narration": (
            "Silver and gold have I none; but such as I have give I thee: "
            "In the name of Jesus Christ of Nazareth rise up and walk."
        ),
        "must_show": "SCRIPTURE-EXACT: the moment itself — Peter's two EMPTY open hands turned out before the seated lame beggar; the poorest offer and the richest, mid-sentence.",
        "must_not_show": "no halo; the hands visibly EMPTY; the beggar's bowl still out; dignity both sides.",
        "scene": (
            "The transaction opens with a disclosure of "
            "poverty: Peter's two hands turn out empty "
            "before the seated beggar — no coin anywhere in "
            "them, nothing to drop in the held-out bowl — "
            "silver and gold have I NONE — and the beggar's "
            "practiced disappointment barely forms before "
            "the sentence swerves into the richest offer "
            "ever made at that gate: but such as I HAVE — "
            "in the name of Jesus Christ of Nazareth — "
            "RISE UP, and WALK. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r153-b04", "out": "s04-i-have-no-money-peter.jpeg", "seg": "n1b",
        "window": "19.85-21.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAMEMAN"],
        "narration": "I have no money, Peter told him.",
        "must_show": "the empty hands close — Peter's open worn palms filling the frame, nothing in them; poverty stated plainly.",
        "must_not_show": "no halo; the EMPTINESS exact — two worn palms, no coin.",
        "scene": (
            "The offer's opening inventory, at close range: "
            "Peter's two palms open in the morning light — "
            "rope-scarred, salt-cracked, and completely "
            "empty — not one coin between them, not a "
            "purse at the belt they extend from — the "
            "plainest financial statement in scripture, "
            "made without embarrassment by a man who is "
            "about to out-give every treasury in the "
            "city. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r153-b05", "out": "s05-and-in-the-name-of.jpeg", "seg": "n1b",
        "window": "21.60-26.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "LAMEMAN"],
        "narration": (
            "And in the name of Jesus Christ of Nazareth, he told a man who "
            "had never walked to stand up."
        ),
        "must_show": "SCRIPTURE-EXACT: the lift — Peter's grip locked on the man's RIGHT hand, the lift mid-motion, the thin legs taking weight for the first time in forty years.",
        "must_not_show": "no halo; the RIGHT hand exact; the legs' strengthening carried by the rising posture, never grotesque.",
        "scene": (
            "The command comes with a grip attached: "
            "Peter's hand locks around the beggar's RIGHT "
            "hand and PULLS — the lift already mid-motion, "
            "the man rising off his mat with his eyes "
            "blown wide, the thin unused legs coming under "
            "him and TAKING THE WEIGHT — forty years of "
            "never-walked ending between one heartbeat and "
            "the next, on the strength of a name spoken by "
            "a man with empty pockets. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r153-b06", "out": "s06-he-had-nothing-in-his.jpeg", "seg": "n1b",
        "window": "26.64-31.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "LAMEMAN"],
        "narration": (
            "He had nothing in his pockets, and he gave away the only thing "
            "he had that was worth anything."
        ),
        "must_show": "the gift's result — the healed man's first STEPS, strong feet and ankles on the flagstones, joy breaking; Peter's open giving posture behind.",
        "must_not_show": "no halo; the steps REAL and new — a first-time walker's wonder; strong ankles per the verse.",
        "scene": (
            "What the empty-pocketed man gave away is "
            "currently learning to walk: the healed "
            "beggar takes his first steps ever across the "
            "flagstones — feet planting wide and "
            "wondering, ankles holding, each stride an "
            "experiment that keeps succeeding — joy "
            "breaking over his face with every yard of "
            "the court he claims — while behind him Peter "
            "stands in the open posture of a man who has "
            "just given away the only treasure he had, "
            "and watched it start walking. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r153-b07", "out": "s07-turn-back-to-god-he.jpeg", "seg": "n2",
        "window": "34.60-36.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "CROWD"],
        "narration": "Turn back to God, he said.",
        "must_show": "the sermon's core — Peter's arm sweeping a full turning ARC before the crowd; repentance drawn as a change of direction.",
        "must_not_show": "no halo; the arc READABLE — a turn, not a wag; the crowd tracking it.",
        "scene": (
            "The whole sermon fits in one drawn arc: "
            "Peter's arm sweeps a slow half-circle before "
            "the crowd — from the direction they have been "
            "walking, around, to face the other way — TURN "
            "BACK — repentance rendered in the oldest "
            "gesture there is, no shame in it anywhere, "
            "just a course correction offered to a court "
            "full of people the way you redirect "
            "travellers who are wanted at home. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r153-b08", "out": "s08-change-your-direction-let-your.jpeg", "seg": "n2",
        "window": "36.45-47.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "CROWD"],
        "narration": (
            "Change your direction, let your wrongs be wiped away, and "
            "something good will follow — not someday far off, but seasons "
            "of relief, sent from God himself."
        ),
        "must_show": "the relief landing — along the listening faces, burdens visibly easing: shoulders dropping, breath released, hope arriving in real time.",
        "must_not_show": "no halo; the easing HONEST — no rapture-faces; ordinary relief on ordinary people.",
        "scene": (
            "The offer does its work on the faces while he "
            "speaks: down the listening rows the easing "
            "runs — a trader's clenched shoulders coming "
            "down from his ears, an old woman's held "
            "breath leaving in one long release, a young "
            "man's guarded face opening by degrees — "
            "wrongs wiped AWAY, seasons of RELIEF, from "
            "God HIMSELF — the words doing on the crowd "
            "exactly what the promise says the turning "
            "does: unburdening, visibly, in real time. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r153-b09", "out": "s09-picture-that-word-refreshing.jpeg", "seg": "n3",
        "window": "47.94-49.88", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Picture that word: refreshing.",
        "must_show": "the word's threshold — parched cracked earth under heat, and the FIRST fat raindrops beginning to strike dark spots on it; refreshing at its first instant.",
        "must_not_show": "no halo; the FIRST drops exact — dark coins on cracked dust; person-free.",
        "scene": (
            "The word arrives the way it always arrives — "
            "one dark coin at a time: the parched ground "
            "lies cracked and pale under the heat, and "
            "onto it the first fat raindrops begin to "
            "strike — dark spreading spots on the dust, "
            "one, three, a dozen, the dry smell rising — "
            "REFRESHING, at the exact instant it starts: "
            "the oldest relief there is, beginning on the "
            "thirstiest ground in the frame. No people are "
            "in this frame."
        ),
    },
    {
        "id": "v2-r153-b10", "out": "s10-like-cool-rain-on-cracked.jpeg", "seg": "n3",
        "window": "49.88-54.88", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Like cool rain on cracked ground, like a deep breath after a "
            "long, hard road."
        ),
        "must_show": "the two likes — the rain now falling full on the drinking ground; and a road-worn traveller stopped, chest lifted in one deep held breath; relief in land and lungs.",
        "must_not_show": "no halo; both images READABLE — soaking ground, the deep-breath posture.",
        "scene": (
            "Both of the sermon's pictures happen at once: "
            "the rain comes down full now, the cracked "
            "ground drinking it in darkening sheets, "
            "runnels finding the old seams — and at the "
            "road's edge a travel-worn figure has stopped "
            "and straightened, chest lifting in one deep "
            "enormous breath, eyes closed, the long hard "
            "road behind him for a moment simply gone — "
            "cool rain and a full breath: the body's own "
            "two words for what God sends the turning. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r153-b11", "out": "s11-that-is-what-god-longs.jpeg", "seg": "n3",
        "window": "54.88-59.88", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "That is what God longs to pour out on people who simply turn "
            "back toward him."
        ),
        "must_show": "the pouring-out — the silver rain-curtains sweeping the wide land, and people in the fields lifting their FACES to it, arms easing open; welcome, not shelter-running.",
        "must_not_show": "no halo; NOBODY running for cover — faces lifted, the rain received as gift.",
        "scene": (
            "Watch what the people in the fields do with "
            "the rain, and learn the theology: nobody "
            "runs — across the wide land the silver "
            "curtains sweep in and the field-workers "
            "stop, straighten, and lift their FACES to "
            "it — arms easing open at their sides, dust "
            "washing off the backs of their necks, "
            "somebody laughing out loud in the wet — "
            "poured out, says the sermon: this is what "
            "God has been WANTING to do, held back only "
            "by which way his people were facing. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r153-b12", "out": "s12-repent-ye-therefore-and-be.jpeg", "seg": "kv19",
        "window": "60.43-68.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "CROWD"],
        "narration": (
            "Repent ye therefore, and be converted, that your sins may be "
            "blotted out, when the times of refreshing shall come from the "
            "presence of the Lord;"
        ),
        "must_show": "SCRIPTURE-EXACT: the sermon's summit — Peter arms-wide on the steps, the verse at full strength over the crowd; the fisherman at full preacher's sail.",
        "must_not_show": "no halo; Peter's fire EARNEST, never angry; the crowd held.",
        "scene": (
            "The fisherman reaches full sail on the temple "
            "steps: Peter's arms spread wide over the "
            "crowd, the words rolling out with a "
            "deck-voice built for storms — REPENT ye "
            "therefore — and be CONVERTED — that your sins "
            "may be BLOTTED OUT — each clause pitched to "
            "reach the court's far colonnade, the times "
            "of refreshing offered from the presence of "
            "the Lord to every upturned face on the "
            "stones — a net cast wider than any he ever "
            "threw at sea. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r153-b13", "out": "s13-but-peter-pointed-to-something.jpeg", "seg": "n4",
        "window": "69.58-73.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "LAMEMAN", "CROWD"],
        "narration": "But Peter pointed to something even larger than one person's fresh start.",
        "must_show": "the widening — Peter's arm lifting FROM the healed leaping man TO the whole court, city and sky beyond; one healing as sample of all.",
        "must_not_show": "no halo; the arc FROM the man TO everything — the scale-jump readable.",
        "scene": (
            "The healed man turns out to be a free sample: "
            "Peter's arm lifts from the leaping newly-"
            "walking beggar — one man, one morning, one "
            "gate — and sweeps up and out across the "
            "whole court, over the colonnades, toward the "
            "city and the wide sky beyond it — FROM this, "
            "the arc says, TO all of it — one restored "
            "pair of ankles offered to the crowd as the "
            "advance evidence of a restoration with "
            "everything on its list. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r153-b14", "out": "s14-he-spoke-of-a-day.jpeg", "seg": "n4",
        "window": "73.66-81.83", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "He spoke of a day when everything that has gone wrong with the "
            "world would finally be set right — a healing not only of "
            "people, but of all things."
        ),
        "must_show": "the all-things healing — one frame half-and-half: a ruined dry terrace on one side RESTORED into green blossoming abundance on the other; the world itself mid-mending.",
        "must_not_show": "no halo; the restoration READABLE left-to-right — ruin becoming whole in one continuous landscape.",
        "scene": (
            "The promised day has a landscape and it is "
            "mid-repair: one continuous terrace runs "
            "across the frame — entering as ruin: tumbled "
            "walls, dead grey orchard stumps, cracked "
            "cistern — and emerging, along the same "
            "unbroken slope, as restoration: the walls "
            "re-laid true, the orchard in full white "
            "blossom, water bright in the mended channel — "
            "not two places but ONE, healing left to "
            "right — a world with everything wrong in it "
            "being set, physically, right. No people are "
            "in this frame."
        ),
    },
    {
        "id": "v2-r153-b15", "out": "s15-his-message-was-not-complicated.jpeg", "seg": "n2",
        "window": "32.31-34.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE"],
        "narration": "His message was not complicated.",
        "must_show": "the plainness — close on Peter's plain direct face mid-sermon: a fisherman's simplicity carrying heaven's content.",
        "must_not_show": "no halo; NOTHING ornate — the plain face and plain words.",
        "scene": (
            "The sermon's vocabulary comes off a fishing "
            "boat: close on Peter's face mid-sentence — "
            "direct, weathered, utterly without ornament — "
            "no scholar's hedges in the eyes, no "
            "rhetorical machinery anywhere in the honest "
            "jaw — turn around; be washed; relief is "
            "coming — the deepest news in the world "
            "travelling in the plainest crate available, "
            "which has always been how it ships best. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r153-b16", "out": "s16-until-that-day-he-said.jpeg", "seg": "n5",
        "window": "82.43-90.86", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Until that day, he said, heaven itself is keeping the promise "
            "safe, the way you hold back the best gift for exactly the "
            "right moment."
        ),
        "must_show": "the kept gift — a wrapped, corded gift bundle set high on a shelf in warm lamplight, deliberately held back; safekeeping as tenderness.",
        "must_not_show": "no halo; the bundle PLAIN and precious — high, safe, waiting; nothing opened.",
        "scene": (
            "Every family knows the shelf where the best "
            "gift waits: in the warm lamplight the wrapped "
            "bundle sits high on its board — corded neat, "
            "kept clear of the daily reaching, positioned "
            "where the household's eyes can find it and "
            "its hands cannot — not withheld out of "
            "meanness but TIMED out of love, the way the "
            "best givers hold the best things for exactly "
            "the right morning — heaven's own shelf-"
            "keeping, in one lamplit corner. No people "
            "are needed in this frame."
        ),
    },
    {
        "id": "v2-r153-b17", "out": "s17-it-is-coming-but-at.jpeg", "seg": "n5",
        "window": "90.86-94.97", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "It is coming, but at the appointed time, and not a moment before.",
        "must_show": "the appointed time — a threshold sundial-stone with its shadow line approaching (not yet touching) the deep-cut mark; the schedule visible, the moment not yet.",
        "must_not_show": "no halo; the shadow NEAR the mark, not on it — approaching exactness.",
        "scene": (
            "The schedule is cut in stone and the shadow "
            "keeps it: on the worn threshold-stone the "
            "old sun-line creeps toward the deep-cut "
            "mark — a finger's width away now, moving at "
            "the sky's own unhurried pace, ignoring every "
            "impatience ever aimed at it — coming, "
            "certainly coming, and not one moment before "
            "the mark is touched — the appointed time "
            "doing what appointed times do: arriving "
            "exactly, and only, on time. No people are "
            "in this frame."
        ),
    },
    {
        "id": "v2-r153-b18", "out": "s18-and-this-was-not-some.jpeg", "seg": "n6",
        "window": "95.55-98.47", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "And this was not some new idea Peter dreamed up.",
        "must_show": "the old paper — a stack of ancient worn scrolls, their rollers dark with age; the doctrine's paperwork long predating the preacher. Script indistinct.",
        "must_not_show": "no halo; no readable text — age carried by wear and rollers.",
        "scene": (
            "The idea has paperwork older than every "
            "kingdom in earshot: the scrolls lie stacked "
            "in their worn age — rollers polished dark by "
            "centuries of hands, edges soft, cords "
            "replaced and re-replaced — the promise's "
            "long paper trail, filed and copied and "
            "carried through exiles and empires — nothing "
            "in Peter's sermon invented this morning; "
            "every clause of it on deposit for "
            "centuries, waiting for a fisherman to read "
            "the balance out loud. No people are needed "
            "in this frame."
        ),
    },
    {
        "id": "v2-r153-b19", "out": "s19-every-true-prophet-all-the.jpeg", "seg": "n6",
        "window": "98.47-108.87", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Every true prophet, all the way back to the beginning, had "
            "promised the very same thing: a great restoring, a "
            "putting-right of everything, spoken of since the world began."
        ),
        "must_show": "the relay — a timeless dusk ridge-line with a long spaced line of varied robed messenger figures, each passing ONE scroll to the next down the ages; faces indistinct, no named prophet.",
        "must_not_show": "ABSOLUTE: no named/depicted prophet — indistinct varied silhouettes; ONE scroll travelling the whole line.",
        "scene": (
            "The promise travelled by relay and the relay "
            "was never broken: along the dusk ridge-line "
            "a spaced procession of robed figures stands "
            "against the sky — old and young, staff and "
            "mantle, each one different and none of them "
            "named by the light — and down the whole "
            "line, hand to hand to hand, travels ONE "
            "scroll — the same word, the same great "
            "restoring, passed from the world's beginning "
            "toward its putting-right without one dropped "
            "hand in all the centuries. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r153-b20", "out": "s20-whom-the-heaven-must-receive.jpeg", "seg": "kv21",
        "window": "109.42-118.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE"],
        "narration": (
            "Whom the heaven must receive until the times of restitution of "
            "all things, which God hath spoken by the mouth of all his holy "
            "prophets since the world began."
        ),
        "must_show": "SCRIPTURE-EXACT: heaven holding — the vast waiting sky over the temple courts, deep and expectant; the received One carried by the sky's held vastness ALONE; no figure.",
        "must_not_show": "ABSOLUTE: no figure, no ascension depicted — the enormous waiting sky over the temple carries the verse.",
        "scene": (
            "The verse's subject is currently held in the "
            "largest keeping there is: over the temple's "
            "honey courts the sky stands enormous and "
            "deep — high clean blue climbing to its "
            "zenith, a waiting quality in the very scale "
            "of it — WHOM THE HEAVEN MUST RECEIVE, until "
            "the times of restitution of ALL things — the "
            "holding not pictured but felt, in a sky "
            "that seems, this morning, less like weather "
            "than like custody. No people are "
            "distinguishable in this frame."
        ),
    },
    {
        "id": "v2-r153-b21", "out": "s21-so-the-only-question-is.jpeg", "seg": "n8",
        "window": "142.16-144.39", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "So the only question is a hopeful one.",
        "must_show": "the hopeful question — a bright expectant face lifted toward the freshening sky, the first rain-smell arriving; hope as expression.",
        "must_not_show": "no halo; the expectancy WARM — bright, not anxious.",
        "scene": (
            "The row's last question wears its answer "
            "already: a single upturned face in the "
            "freshening light — eyes bright, the first "
            "cool rain-smell arriving on the moving air, "
            "the corners of the mouth already lifting — "
            "expectancy without one flicker of dread in "
            "it — the look people wear on platforms and "
            "at harbours when what is coming is GOOD and "
            "the schedule says soon. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r153-b22", "out": "s22-restitution-means-giving-back-what.jpeg", "seg": "n7",
        "window": "119.62-126.97", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Restitution means giving back what was lost, restoring what "
            "was broken to the way it was always meant to be."
        ),
        "must_show": "the word enacted — a finder placing a lost ewe back into an old shepherd's arms at his gate; the giving-BACK exact and warm.",
        "must_not_show": "no halo; the RETURN readable — finder's arms releasing, owner's receiving; joy quiet.",
        "scene": (
            "The word has a doorstep demonstration: at the "
            "old shepherd's gate a finder sets the lost "
            "ewe back into the arms that raised her — the "
            "young man's grip releasing as the old man's "
            "closes, the animal pressing home into the "
            "remembered chest — given BACK: not replaced, "
            "not compensated, the very one restored to "
            "the very arms — restitution, performed at "
            "the scale of one gate, one ewe, and one old "
            "man's undone face. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r153-b23", "out": "s23-not-patched-up-not-almost.jpeg", "seg": "n7",
        "window": "126.97-131.59", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Not patched up, not almost — made whole, made new, every part of it.",
        "must_show": "whole-not-patched — a potter's finished NEW vessel gleaming on the wheel, and beside the bench the old cracked shards retired in a basket; newness, not repair.",
        "must_not_show": "no halo; the new vessel FLAWLESS and the shards visibly retired — no glued patchwork anywhere.",
        "scene": (
            "The standard is set at the potter's bench: on "
            "the stilled wheel the finished vessel stands "
            "gleaming — new clay, true curve, not a seam "
            "or mend-line anywhere on it — while beside "
            "the bench the old cracked shards sit retired "
            "in their basket, honourably done — not "
            "patched, not glued, not almost: made NEW — "
            "restitution's actual standard, which never "
            "meant repair and always meant the wheel. No "
            "people are needed in this frame."
        ),
    },
    {
        "id": "v2-r153-b24", "out": "s24-so-this-verse-is-a.jpeg", "seg": "n8",
        "window": "132.08-135.59", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "So this verse is a promise you can lean your full weight on.",
        "must_show": "the leaning — a traveller leaning FULL weight on a solid stone parapet/bridge rail that visibly holds; trust as physics.",
        "must_not_show": "no halo; the lean REAL — full weight committed, the stone unmoved.",
        "scene": (
            "Test the promise the way you test a bridge "
            "rail: the traveller leans his FULL weight "
            "onto the stone parapet — both forearms down, "
            "chest committed, feet easy off their guard — "
            "and the old stone holds the way it has held "
            "every leaner for a hundred years: without "
            "a tremor — a verse you can put your whole "
            "weight on, demonstrated by a man putting his "
            "whole weight on, over the long drop of "
            "everything he cannot control. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r153-b25", "out": "s25-the-world-is-not-just.jpeg", "seg": "n8",
        "window": "135.59-142.16", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The world is not just sliding into ruin; it is heading toward "
            "a restoration God has planned from the very start."
        ),
        "must_show": "the road's true direction — a road that drops toward dusk in the near ground but BENDS visibly toward a bright green valley beyond; the world's heading corrected.",
        "must_not_show": "no halo; the bend READABLE — near dusk, far brightness, one continuous road.",
        "scene": (
            "Stand at the right vantage and the road's "
            "reputation is wrong: in the near ground it "
            "does what everyone says — drops away toward "
            "dusk, losing light with every yard — but "
            "follow it with your eye and the road BENDS: "
            "curving out of the shadowed descent and "
            "running on, unmistakably, toward a far "
            "valley standing in full bright green — one "
            "continuous road, badly reported — not "
            "sliding into ruin: routed, from the very "
            "start, toward restoration. No people are in "
            "this frame."
        ),
    },
    {
        "id": "v2-r153-b26", "out": "s26-will-you-turn-and-be.jpeg", "seg": "n8",
        "window": "144.39-147.85", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Will you turn, and be part of the refreshing when it comes?",
        "must_show": "the closing turn — a figure on the road FULLY TURNED toward the bright valley, first rain freshening ahead of them; the 117/133 reversal rhyme; invitation in motion.",
        "must_not_show": "no halo; the turn COMPLETE — feet, shoulders and face all committed toward the brightness.",
        "scene": (
            "The last frame is a body answering the "
            "question: on the road a figure stands FULLY "
            "turned — feet, shoulders, face, all of them "
            "swung round and committed toward the far "
            "bright valley where the first silver rain is "
            "already freshening the green — the old "
            "direction abandoned behind them without a "
            "backward glance — turned, the way the whole "
            "sermon asked, in time for the refreshing, "
            "with room on the road for whoever turns "
            "next. Every figure has two arms, two hands "
            "and one head."
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
