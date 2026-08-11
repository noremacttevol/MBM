#!/usr/bin/env python3
"""V2 beat map — row 122, build-122-mote-and-beam (Matthew 7:1-5).

COVERAGE: 27 pictures over 151.1 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 7 KJV):
  7:1   "JUDGE NOT, that ye be not judged."
  7:2   "For with what judgment ye judge, ye shall be judged: and
        WITH WHAT MEASURE YE METE, it shall be measured to you again."
  7:3   "why beholdest thou the MOTE that is in thy brother's eye,
        but considerest not the BEAM that is in thine own eye?"
  7:4   "Let me pull out the mote out of thine eye; and, behold, a
        beam is in thine own eye?"
  7:5   "THOU HYPOCRITE, FIRST cast out the beam out of thine own
        eye; and THEN shalt thou see clearly to cast out the mote
        out of thy brother's eye." — the speck still gets dealt
        with; the order is the teaching.
  Setting: the same Sermon on the Mount hillside as Matthew 5
  (row 121) — same slope, same lake, same kind of crowd.

RENDERING LAWS:
  - THE BEAM IS ABSURD, NEVER GRUESOME (the narration says Jesus
    "drew the picture out until it was absurd enough to make you
    laugh"): the wooden beam rides OVER the man's eye and brow,
    braced against his face and shoulder like a carried plank — NO
    wound, NO blood, NO penetration, ever. Painterly comedy. Any
    render that makes it an injury is an automatic reject.
  - ACTION-LOGIC (Cameron's law): the beam-man's every action must
    read at a glance — leaning in to pick a speck WHILE his own
    plank bumps and blocks; pulling the plank away with both hands;
    then gently helping. The MOTE is a sawdust speck, tiny, best
    carried by drifting sawdust in a sunbeam.
  - The workshop vignette pair are BROTHERS and the story ends in
    warmth — the fixer is earnest and sincere, never a villain; the
    brother patient, never mocking.
  - HILLSIDE and CROWD locks are BYTE-IDENTICAL to build-121 (same
    sermon, same slope, same congregation) — cross-video continuity.

TIME OF DAY ARC (intentional): the hillside in the same warm late-
afternoon gold as row 121 throughout; the workshop vignettes in
bright working daylight with sun through the door (the sunbeam
carries the sawdust motes); the closing hillside in golden last
light.

CHANGING CONDITION (kept OUT of the locks): the beam — on the
fixer's brow through the absurd beats, gripped in realization at
b19, cast down by b20/b22; the fixer's manner — confident meddler,
then humbled, then gentle helper.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "HILLSIDE": (
        "HILLSIDE LOCK: the teaching hillside — a green grassy slope "
        "above the Sea of Galilee, wildflowers in the grass, the "
        "blue lake and far hills below, warm late-afternoon light. "
        "The same slope and lake view throughout."
    ),
    "CROWD": (
        "CROWD LOCK: the listening crowd — ordinary Galileans seated "
        "on the grass: weathered fishermen, mothers with children, "
        "sun-browned farmers, a few elders; varied earth-toned robes "
        "of brown, rust, olive and slate (no cream — only Jesus "
        "wears cream), varied ages and faces, never uniform."
    ),
    "SHOP": (
        "SHOP LOCK: the carpenter's workshop — a small open-fronted "
        "stone workshop with a heavy wooden bench, saws and adzes on "
        "the wall, curled shavings on the floor, stacked planks, and "
        "one bright shaft of sunlight through the wide door. The "
        "same shop and bench throughout."
    ),
    "FIXER": (
        "FIXER LOCK: the would-be fixer is the same man in every "
        "shot — broad and bustling, about forty, a short black "
        "beard, in a DARK UMBER work tunic with a leather apron "
        "(never cream, never white); earnest and completely sincere, "
        "never a villain."
    ),
    "BROTHER": (
        "BROTHER LOCK: the brother is the same man in every shot — "
        "leaner and younger, a trimmed brown beard, in a DARK OLIVE "
        "tunic (never cream, never white); patient, mild, with dry "
        "good humour in his eyes."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r122-b01", "out": "s01-of-all-the-things-jesus.jpeg", "seg": "n1",
        "window": "0.28-8.96", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Of all the things Jesus taught on that hillside, one of them "
            "cuts straight to how we treat each other — and it starts with a "
            "warning we would rather skip."
        ),
        "must_show": "the same Sermon hillside — Jesus seated teaching on the green slope, the ordinary crowd on the grass, the lake below; the scene continuous with the salt-and-light sermon.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the crowd VARIED, every gaze on him.",
        "scene": (
            "The same hillside, the same congregation, the camera "
            "looking past the seated crowd's backs up the green "
            "slope: Jesus seated in the warm gold with the lake "
            "spread blue below, fishermen and mothers and farmers "
            "settled in the grass around him — and something in "
            "the teacher's leveled gaze telling the front rows "
            "that the next stretch of sermon is the kind that "
            "walks home with you and rearranges the furniture: a "
            "warning everyone needs and nobody orders. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b02", "out": "s02-judge-not-that-ye-be.jpeg", "seg": "jvA",
        "window": "9.45-11.73", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Judge not, that ye be not judged.",
        "must_show": "SCRIPTURE-EXACT: the warning — Jesus level and gentle, hand lowered palm-down in a stilling gesture; the crowd very quiet.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NO pointing finger — the gesture calms, never accuses.",
        "scene": (
            "Three words drop the hillside to silence: Jesus "
            "seated forward, one hand lowered palm-down in the "
            "quiet stilling gesture of a man settling water — "
            "judge not — the deep brown eyes moving along the "
            "front rows without singling anyone out, which is "
            "itself the sermon — and across the grass the small "
            "stillness of a crowd discovering that the warning "
            "they would rather skip has arrived, and is looking "
            "kindly at all of them at once. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b03", "out": "s03-for-with-what-judgment-ye.jpeg", "seg": "jvA",
        "window": "11.73-20.55", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "For with what judgment ye judge, ye shall be judged: and with "
            "what measure ye mete, it shall be measured to you again."
        ),
        "must_show": "SCRIPTURE-EXACT: the measure — work-worn hands levelling grain in a wooden measure with a straight-edge, a second sack waiting; the exact same measure about to come back.",
        "must_not_show": "no halo; period-true — wooden measure, grain, no modern objects.",
        "scene": (
            "The law of the verse works like market arithmetic: "
            "close on work-worn hands drawing a straight-edge "
            "across a wooden grain measure, striking it exactly "
            "level — not a kernel over — while beside the first "
            "sack a second stands open and waiting its turn — "
            "whatever line you scrape for another man is the line "
            "that will be scraped for you, the measure you mete "
            "already on its way back around the market to your "
            "own open mouth of a sack. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b04", "out": "s04-he-cannot-even-see-straight.jpeg", "seg": "n4",
        "window": "83.14-85.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER"],
        "narration": "He cannot even see straight.",
        "must_show": "the obstruction — the fixer tilting and craning his head absurdly, the long beam over his brow swinging and clipping the doorframe; half his world blocked.",
        "must_not_show": "ABSOLUTE: no wound, no blood — the beam RIDES over his eye and brow, braced to his shoulder; pure painterly comedy.",
        "scene": (
            "Basic navigation has become a performance: the fixer "
            "cranes and tilts his head, trying to line up his one "
            "unblocked eye with the world, while the long wooden "
            "beam riding over his brow swings wide and clips the "
            "doorframe with a knock that shakes dust from the "
            "lintel — half the workshop simply missing from his "
            "view behind timber — a man navigating his own shop "
            "in awkward sideways increments and genuinely unaware "
            "of why. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r122-b05", "out": "s05-set-yourself-up-as-the.jpeg", "seg": "n2",
        "window": "22.07-30.05", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Don't set yourself up as the judge, he said, because whatever "
            "standard you hold other people to is the one that will be held "
            "up to you."
        ),
        "must_show": "the teaching pressed home — Jesus with both open hands turned toward the crowd and then back toward himself, the standard reversing direction in one gesture.",
        "must_not_show": "no halo, glare or rim-light on Jesus; warmth throughout — counsel, not scolding.",
        "scene": (
            "The gesture teaches the boomerang in it: Jesus's open "
            "hands move out toward the crowd and then turn back "
            "toward his own chest — whatever you hold up for them "
            "comes back held up to YOU — the arc of it drawn slow "
            "and visible in the gold air, and along the slope the "
            "listeners follow the hands with the slightly "
            "unsettled attention of people watching their own "
            "yardstick change direction mid-air and start "
            "measuring back up the hill toward its owner. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b06", "out": "s06-and-we-are-experts-at.jpeg", "seg": "n2",
        "window": "30.05-34.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "And we are experts at spotting the small faults in someone else.",
        "must_show": "the habit caught live — in the crowd, one listener's knowing sideways glance toward a neighbour, an eyebrow raised at somebody else's flaw mid-sermon.",
        "must_not_show": "no halo; gentle comedy, not malice — the glance small, human, instantly recognizable.",
        "scene": (
            "The sermon catches its audience doing the thing: in "
            "the second row a listener's eyes slide sideways to a "
            "neighbour with one eyebrow lifted a knowing "
            "half-inch — the tiny silent verdict every human face "
            "knows how to pass — while the neighbour, oblivious, "
            "listens on — expertise on display, effortless and "
            "instant, the fault in someone else spotted from a "
            "seated position without missing a word of the sermon "
            "about not doing exactly that. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b07", "out": "s07-a-tiny-speck-a-mote.jpeg", "seg": "n2",
        "window": "34.53-40.86", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER", "BROTHER"],
        "narration": (
            "A tiny speck, a mote, in our brother's eye — and we cannot wait "
            "to point it out."
        ),
        "must_show": "the mote at true scale — sawdust drifting in the door's sun-shaft, one speck near the brother's blinking eye, and the fixer's eager pointing finger already up.",
        "must_not_show": "no halo; the speck TINY — dust-grain scale; the eagerness on the fixer, mild patience on the brother.",
        "scene": (
            "The offense, at actual size: in the bright shaft "
            "through the workshop door the sawdust hangs drifting, "
            "and somewhere in that golden traffic one speck has "
            "found the brother's eye — he blinks at it, mildly "
            "inconvenienced — while across the bench the fixer's "
            "finger is already up and aimed, his whole broad face "
            "lit with the eager helpfulness of a man who has "
            "found, in somebody else, a flaw the size of a grain "
            "of dust. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r122-b08", "out": "s08-so-he-asked-a-question.jpeg", "seg": "n2",
        "window": "40.86-42.60", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": "So he asked a question.",
        "must_show": "the question forming — close on Jesus's face, one brow lifting, the corner of the mouth carrying the beginning of the sermon's great absurdity.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the humour BEGINNING — warmth with a glint.",
        "scene": (
            "The best question in the sermon gathers on his face "
            "first: close on Jesus in the warm light, one brow "
            "lifting, a glint arriving in the deep brown eyes and "
            "the faintest forward lean of a teacher about to hand "
            "a crowd a picture they will never get out of their "
            "heads — the look of a man who knows the question is "
            "unanswerable and funny and aimed, gently, at every "
            "single person on the hill including the ones smiling "
            "already. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r122-b09", "out": "s09-and-why-beholdest-thou-the.jpeg", "seg": "jv3",
        "window": "43.19-50.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER", "BROTHER"],
        "narration": (
            "And why beholdest thou the mote that is in thy brother's eye, "
            "but considerest not the beam that is in thine own eye?"
        ),
        "must_show": "SCRIPTURE-EXACT: the full absurdity revealed — the fixer peering intently at the brother's speck WITH an entire wooden beam riding over his own eye and brow; both faults in one frame at their true ridiculous ratio.",
        "must_not_show": "ABSOLUTE: no wound, no blood, no penetration — the beam braced over brow and shoulder; painterly comedy, never injury.",
        "scene": (
            "The question paints itself in one impossible frame: "
            "the fixer leans across the bench, his one free eye "
            "narrowed in deep diagnostic focus on the speck in "
            "his brother's blinking eye — while over his OWN brow "
            "rides an entire wooden beam, long as a roof-timber, "
            "braced against his shoulder and jutting past the "
            "frame, casting its shadow over the very eye doing "
            "the inspecting — the two faults sharing the picture "
            "at their true ratio: a grain of dust, and lumber. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b10", "out": "s10-why-do-you-stare-at.jpeg", "seg": "n3",
        "window": "52.18-58.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER", "BROTHER"],
        "narration": (
            "Why do you stare at the speck of sawdust in your brother's eye, "
            "he asked, and never once notice the plank in your own?"
        ),
        "must_show": "the stare — close on the fixer's intent single visible eye fixed on the tiny speck, the plank's grain filling half his own face's frame, utterly unnoticed by him.",
        "must_not_show": "ABSOLUTE: no wound — the plank rides the brow; his obliviousness total and sincere.",
        "scene": (
            "The stare is a marvel of selective vision: close on "
            "the fixer's one visible eye, narrowed and intent as "
            "a jeweler's, locked on the dust-grain in his "
            "brother's lashes — while filling the whole other "
            "half of his face, inches from that busy eye, the "
            "raw wooden grain of his own plank sits in plain "
            "sight of everyone in the world except the man "
            "wearing it — a stare that can find a speck at arm's "
            "length and cannot find timber on its own forehead. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b11", "out": "s11-then-he-drew-the-picture.jpeg", "seg": "n3",
        "window": "58.95-63.05", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Then he drew the picture out until it was absurd enough to make "
            "you laugh."
        ),
        "must_show": "the laughter — Jesus mid-description with a slight smile, hands sketching the beam's length in the air; the crowd breaking into real laughter.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the laughter WARM and general — teaching through delight.",
        "scene": (
            "The sermon gets its laugh on purpose: Jesus's hands "
            "spread wide apart in the gold air, sketching the "
            "ridiculous length of the beam while his own mouth "
            "gives up its slight smile — and the hillside breaks: "
            "fishermen barking short laughs, a mother laughing "
            "into her child's hair, the old men's shoulders "
            "shaking — the picture drawn out exactly far enough "
            "that every laugher on the slope is laughing, without "
            "quite noticing yet, at himself. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b12", "out": "s12-and-then-if-we-are.jpeg", "seg": "n5",
        "window": "92.97-98.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER"],
        "narration": (
            "And then, if we are honest, the moment finally comes when we "
            "catch sight of the beam."
        ),
        "must_show": "the catching-sight — the fixer stooped over the still water of the workshop's basin, gone motionless: the beam's reflection looking back at him for the first time.",
        "must_not_show": "ABSOLUTE: no wound; the stillness TOTAL — the comedy stops here; honest shock, gently held.",
        "scene": (
            "The joke goes quiet in a basin of still water: the "
            "fixer stoops to rinse his hands and stops — the "
            "water's surface holding, steady and undeniable, a "
            "man with a full wooden beam riding over his eye — "
            "his reflection meeting him with the news everyone "
            "else always had — and the broad busy face goes "
            "still around the seeing, the eager finger's owner "
            "discovering at last what he has been pointing "
            "around all this time. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b13", "out": "s13-or-how-wilt-thou-say.jpeg", "seg": "jv4",
        "window": "63.60-71.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER", "BROTHER"],
        "narration": (
            "Or how wilt thou say to thy brother, Let me pull out the mote "
            "out of thine eye; and, behold, a beam is in thine own eye?"
        ),
        "must_show": "SCRIPTURE-EXACT: the offer — the fixer's careful fingers reaching for the brother's eye, mouth mid-'hold still', while his beam's far end bumps the brother's shoulder.",
        "must_not_show": "ABSOLUTE: no wound anywhere; the fingers NEVER touching the eye — reaching only; the bump readable at a glance.",
        "scene": (
            "The offer is made in perfect sincerity: the fixer "
            "leans in with two careful fingers poised toward his "
            "brother's eye, lips shaped around hold still, let me "
            "get that — while the far end of his own beam, "
            "travelling with his lean, arrives first and bumps "
            "the brother gently in the shoulder — the patient "
            "younger face taking the knock with one dry sidelong "
            "look at the timber, waiting to see how long charity "
            "must last. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r122-b14", "out": "s14-picture-it.jpeg", "seg": "n4",
        "window": "73.19-73.95", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Picture it.",
        "must_show": "the invitation — Jesus's open hand extended to the crowd, offering them the image; listeners leaning in, some already grinning.",
        "must_not_show": "no halo, glare or rim-light on Jesus; anticipation on the faces — the picture arriving.",
        "scene": (
            "Two words hand the crowd a paintbrush: Jesus's open "
            "hand extends toward them, palm up, offering the "
            "image the way you offer a gift you know is going to "
            "be enjoyed — picture it — and the slope leans in as "
            "one, fishermen elbowing, a grin already escaping "
            "here and there among the beards, the whole hillside "
            "assembling in its collective imagination one man, "
            "one speck, and one entirely unnoticed roof-timber. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b15", "out": "s15-a-man-leaning-in-saying.jpeg", "seg": "n4",
        "window": "73.95-83.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER", "BROTHER"],
        "narration": (
            "A man leaning in, saying hold still, let me get that little "
            "speck out for you — with an entire wooden beam sticking "
            "straight out of his own head."
        ),
        "must_show": "the full tableau — the whole workshop scene: fixer leaning in solicitously, fingers out, the enormous beam riding straight out from over his brow; the brother leaning back the same distance; absurdity complete.",
        "must_not_show": "ABSOLUTE: no wound, no blood — the beam braced over brow and shoulder, clearly carried, never embedded; the comedy painterly.",
        "scene": (
            "The whole absurd machine, assembled: in the sun-"
            "shafted shop the fixer leans solicitously in — "
            "fingers delicately out, face all tender helpfulness "
            "— while the enormous beam riding over his brow runs "
            "straight out ahead of him like a ship's bowsprit, "
            "its shadow lying across both men — and the brother "
            "leans exactly as far back as the timber advances, "
            "keeping his one dusty speck at a survivable "
            "distance from all that oncoming assistance. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b16", "out": "s16-the-beam-is-in-the.jpeg", "seg": "n4",
        "window": "85.08-87.72", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER"],
        "narration": "The beam is in the way of everything he does.",
        "must_show": "the obstruction everywhere — the beam's swing scattering tools from the bench and knocking a hanging saw swinging, shavings flying; his whole workday sabotaged by his own timber.",
        "must_not_show": "ABSOLUTE: no wound; nobody hurt by the chaos — pots and tools only; the comedy physical and readable.",
        "scene": (
            "Everything the man attempts, the timber attempts "
            "first: one ordinary turn toward the bench and the "
            "beam's far end sweeps a plane and two chisels "
            "clattering to the floor, sets the hanging saw "
            "swinging on its peg, and ploughs a wake through the "
            "curled shavings — the workshop rearranged by every "
            "gesture of a man who still believes his hands are "
            "doing fine detailed work today — his own beam ahead "
            "of him in everything, in the way of everything. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b17", "out": "s17-and-yet-he-is-completely.jpeg", "seg": "n4",
        "window": "87.72-92.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER", "BROTHER"],
        "narration": (
            "And yet he is completely sure that he is the one who ought to "
            "be fixing other people."
        ),
        "must_show": "the certainty — the fixer's earnest confident face (one eye timber-shadowed), finger raised in helpful authority; the brother's long patient dry look at the beam.",
        "must_not_show": "ABSOLUTE: no wound; the fixer NEVER a villain — sincerity total; the brother's look wry, not cruel.",
        "scene": (
            "His confidence has survived everything, including "
            "the evidence: the fixer stands in helpful authority, "
            "finger raised, face earnest and certain under the "
            "timber-shadow crossing it — absolutely sure that of "
            "the two men in this workshop, HE is the one "
            "qualified for delicate eye surgery — while the "
            "brother regards the beam's full length with the "
            "long, dry, patient look of a man mentally measuring "
            "it and saying nothing whatsoever. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b18", "out": "s18-not-his.jpeg", "seg": "n5",
        "window": "98.78-100.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "BROTHER"],
        "narration": "Not his.",
        "must_show": "the honest re-measure — close on the brother's mild face and its single tiny speck: small, ordinary, bearable; the fault that never was the story.",
        "must_not_show": "no halo; the speck barely-there — dust-grain scale; his expression mild and unaccusing.",
        "scene": (
            "Seen honestly, the brother's fault is almost "
            "nothing: close on the mild patient face, and there "
            "in the lashes the speck — a single grain of sawdust, "
            "the kind every eye in every workshop collects by "
            "noon and weeps out by supper — small, ordinary, "
            "bearable, real — a genuine fault and a tiny one, "
            "which was never for a single moment the actual "
            "story being told in this shop. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b19", "out": "s19-ours-the-one-we-had.jpeg", "seg": "n5",
        "window": "100.52-104.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER"],
        "narration": "Ours. The one we had been carrying the whole time.",
        "must_show": "the owning — the fixer's two hands closed around his own beam at last, head bowed against the timber; the carrying admitted.",
        "must_not_show": "ABSOLUTE: no wound; the moment humble and quiet, not despairing.",
        "scene": (
            "The hands finally find the right piece of wood: the "
            "fixer's two broad palms close around his own beam — "
            "the first time in the whole story he has touched it "
            "— and his head bows against the grain, eyes closed, "
            "the eager finger's owner standing quiet with his "
            "arms full of the thing he had been aiming around "
            "all this time — ours, the timber says under his "
            "hands; carried the whole time; mine. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b20", "out": "s20-thou-hypocrite-first-cast-out.jpeg", "seg": "jvB",
        "window": "104.87-112.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER"],
        "narration": (
            "Thou hypocrite, first cast out the beam out of thine own eye; "
            "and then shalt thou see clearly to cast out the mote out of thy "
            "brother's eye."
        ),
        "must_show": "SCRIPTURE-EXACT: the casting-out — the fixer hauling the beam away from his own brow with both arms, his whole face coming clear and unblocked into the light for the first time.",
        "must_not_show": "ABSOLUTE: no wound, no mark left — the beam simply lifted away; the clearing visible: both eyes open, whole face lit.",
        "scene": (
            "The order of operations is performed at last: with "
            "both arms and an honest heave the fixer hauls the "
            "beam up and away from his own brow — the timber "
            "swinging clear, the shadow leaving his face — and "
            "for the first time in the story both his eyes are "
            "open in the light at once, blinking at a workshop "
            "twice the size he remembered — FIRST the beam, the "
            "verse insists, and the man now holding his own "
            "lumber at arm's length has finally got the sequence "
            "right. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r122-b21", "out": "s21-notice-he-does-not-say.jpeg", "seg": "n6",
        "window": "114.50-117.04", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": "Notice he does not say ignore your brother's speck.",
        "must_show": "the clarification — close on Jesus, one gentle finger raised in precision, head slightly tilted; the sermon protecting the caring.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the finger CLARIFYING, not warning.",
        "scene": (
            "The clarification arrives before anyone can misuse "
            "the joke: close on Jesus with one finger gently "
            "raised — not warning, adjusting — his head tilted "
            "the small careful degree of a teacher closing a "
            "loophole: notice what was NOT said — nobody on this "
            "hill has been told to ignore a brother's hurt — the "
            "speck is real and it matters, the deep eyes say; we "
            "are only settling, permanently, who goes to the "
            "carpenter first. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r122-b22", "out": "s22-he-says-deal-with-your.jpeg", "seg": "n6",
        "window": "117.04-125.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER", "BROTHER"],
        "narration": (
            "He says deal with your own beam first — and then you will "
            "actually be able to help him, gently, instead of just "
            "condemning him."
        ),
        "must_show": "the healed help — the beam lying on the floor, and the clear-eyed fixer gently steadying the brother's chin, lifting the speck with a soft cloth corner; tenderness where meddling was.",
        "must_not_show": "ABSOLUTE: nothing touches the eyeball — the cloth corner near the lashes only; both faces calm and trusting.",
        "scene": (
            "The same help, run in the right order, has changed "
            "species: the beam lies retired on the floor among "
            "the shavings, and the fixer — both eyes clear, "
            "hands suddenly patient — steadies his brother's "
            "chin with one palm and brings a soft cloth corner "
            "carefully toward the lashes, no lecture in him "
            "anywhere — and the brother holds easily still, "
            "trusting the touch at his eye completely, now that "
            "the man behind it can see. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b23", "out": "s23-the-goal-was-never-to.jpeg", "seg": "n7",
        "window": "125.83-128.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER", "BROTHER"],
        "narration": "The goal was never to stop caring about each other.",
        "must_show": "the caring kept — the speck out, the two brothers with hands on each other's shoulders, faces warm; the whole point standing in one clasp.",
        "must_not_show": "no halo; warmth WITHOUT sentimentality — two workmen, one good moment.",
        "scene": (
            "What survives the sermon is the caring itself: the "
            "speck dealt with, the two brothers stand in the "
            "door's warm shaft with hands clasped to each "
            "other's shoulders — the fixer's grip grateful, the "
            "brother's easy — two workmen in a sawdust-scented "
            "shop having arrived, by way of one ridiculous "
            "timber, at the entire point: the eye was never the "
            "problem and the caring was never the target; only "
            "the order was ever wrong. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b24", "out": "s24-it-was-to-come-to.jpeg", "seg": "n7",
        "window": "128.19-137.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOP", "FIXER", "BROTHER"],
        "narration": (
            "It was to come to each other humble instead of superior — as "
            "one flawed person helping another, not a judge passing a "
            "sentence."
        ),
        "must_show": "the equality — the two seated side by side on the bench among the shavings, same level, sharing a water-skin; flawed and equal and easy together.",
        "must_not_show": "no halo; NOTHING elevated — same bench, same height, same light on both faces.",
        "scene": (
            "The new arrangement seats them at the same height: "
            "side by side on the workshop bench among the curled "
            "shavings, passing a water-skin between them, the "
            "retired beam serving under their feet as a footrest "
            "— no judge's seat anywhere in the room, no bench "
            "higher than the other — two flawed men at one "
            "level in one light, which turns out to be the only "
            "position from which help was ever going to work. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b25", "out": "s25-the-measure-you-use-is.jpeg", "seg": "n8",
        "window": "137.91-140.72", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "The measure you use is the measure you will get back.",
        "must_show": "the measure returned — the wooden grain measure again, this time heaped GENEROUS and running over into another's open sack; the same law, run on mercy.",
        "must_not_show": "no halo; the contrast with the earlier level-scraped measure exact — same measure, opposite fill.",
        "scene": (
            "The same measure from the sermon's start comes back "
            "changed: the wooden grain measure again in the "
            "work-worn hands — but heaped now, pressed down and "
            "running over, grain spilling in a bright hiss past "
            "the rim into another man's open sack — the identical "
            "law that scraped level earlier now paying out in "
            "the same coin it was fed — because the rule never "
            "changed, only the mercy that somebody finally put "
            "into the scoop. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r122-b26", "out": "s26-so-jesus-offers-a-better.jpeg", "seg": "n8",
        "window": "140.72-144.07", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": "So Jesus offers a better one: mercy.",
        "must_show": "the offer — close on Jesus, one open hand held out palm-up to the crowd, the gift-gesture; mercy extended, not demanded.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the palm OPEN and empty — the offer is the picture.",
        "scene": (
            "The better measure is offered on an open palm: "
            "close on Jesus with one hand extended palm-up "
            "toward the crowd, empty and open — the oldest "
            "gift-gesture there is — mercy, held out in the warm "
            "gold light not as a demand or a standard but as an "
            "exchange anyone on the hill can make today: hand "
            "over the scraping-level judgment, take this "
            "instead, and spend the rest of your life being "
            "measured by what you switched to. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r122-b27", "out": "s27-deal-honestly-with-yourself-and.jpeg", "seg": "n8",
        "window": "144.07-150.82", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Deal honestly with yourself, and you will be amazed how much "
            "patience you suddenly have for everyone else."
        ),
        "must_show": "the close — the golden hillside, the crowd easy and softened around the seated teacher, neighbours looking at each other more kindly; the sermon already working.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the kindness VISIBLE between listeners, not just toward the front.",
        "scene": (
            "The sermon's proof runs through the crowd before "
            "anyone stands up, the camera looking across the "
            "slope from the side, past the seated listeners' "
            "shoulders: the golden last light on the grass, the "
            "teacher seated easy at the crest — and between the "
            "listeners themselves the small new kindnesses "
            "already moving: the sideways-glancer of the early "
            "verses now sharing his water-skin with the "
            "neighbour he had measured, a fisherman shifting to "
            "give an old man more room — patience breaking out "
            "in every direction the moment the beams came down. "
            "Every figure has two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "HILLSIDE": "PLACE-REF/hillside.jpeg",  # build-122-mote-and-beam s01-of-all-the-things-jesus (manual)
    "SHOP": "PLACE-REF/shop.jpeg",  # build-122-mote-and-beam s07-a-tiny-speck-a-mote (manual)
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "FIXER": "CAST-REF-V2/fixer.jpeg",
    "BROTHER": "CAST-REF-V2/brother.jpeg",
}
