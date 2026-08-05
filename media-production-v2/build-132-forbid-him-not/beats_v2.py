#!/usr/bin/env python3
"""V2 beat map — row 132, build-132-forbid-him-not (Mark 9:38-41).

COVERAGE: 14 pictures over 78.8 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 9 KJV):
  9:38  JOHN: "Master, we saw one casting out devils in thy name, and
        he followeth not us: and WE FORBAD HIM, because he followeth
        not us."
  9:39  "FORBID HIM NOT: for there is no man which shall do a miracle
        in my name, that can lightly speak evil of me."
  9:40  "For he that is NOT AGAINST US is ON OUR PART."
  9:41  "whosoever shall give you A CUP OF WATER to drink in my name,
        because ye belong to Christ... he shall NOT LOSE HIS REWARD."

RENDERING LAWS:
  - NO DEMONS ARE EVER DEPICTED. The stranger's deliverance work is
    shown ONLY as aftermath: a freed man rising in relief, a family
    amazed, the stranger's hands lifted from a calmed brow. Any
    render with a demon figure, contortion, or horror imagery is an
    automatic reject.
  - JOHN is the shared cast token (same face as every build). His
    error is PROTECTIVENESS, not malice — sincere gatekeeping,
    gently corrected; by b14 the lesson sits on him as wonder.
  - THE STRANGER is earnest and good — a plain man doing real works
    in the name he honours; never suspect, never shabby-sinister.
    His confused hurt at being stopped (b04) must be sympathetic.
  - Jesus never scolds — b05-b08 are level, warm correction; the
    staying hand of b07 LOWERS the forbidding, it does not wag.
  - The cup of water (b11/b13) is the row's smallest-kindness image:
    plain cup, plain giver, full dignity.

TIME OF DAY ARC (intentional): the deliverance and stopping
vignettes in bright working day; the report and teaching at the
roadside camp in late-afternoon gold; the closing camp frame at
warm dusk with the stranger's far lamp BY DESIGN.

CHANGING CONDITION (kept OUT of the locks): John — complaint-hot,
then listening, then widened; the stranger — at work, stopped,
then at work again and walking free.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags. JOHN comes from the
# shared CAST_LOCKS — do not redefine him here.
LOCKS = {
    "CAMP": (
        "CAMP LOCK: the roadside camp — a grassy verge off the "
        "highland road with a low cookfire ring of stones, bedrolls "
        "and packs, an olive tree leaning over, open hills beyond. "
        "The same camp throughout."
    ),
    "STREET": (
        "STREET LOCK: the village street — a short lane of pale "
        "stone houses with a communal cistern and two doorsteps in "
        "sun, bright working day. The same lane throughout."
    ),
    "STRANGER": (
        "STRANGER LOCK: the stranger is the same man in every "
        "shot — plain and sturdy, about thirty-five, a short brown "
        "beard, in a DARK BRICK-RED tunic with a rope belt (never "
        "cream, never white); earnest, warm-eyed, entirely good."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r132-b01", "out": "s01-master-we-saw-one-casting.jpeg", "seg": "s38",
        "window": "0.28-7.94", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMP"],
        "narration": (
            "Master, we saw one casting out devils in thy name, and he "
            "followeth not us: and we forbad him, because he followeth not "
            "us."
        ),
        "must_show": "SCRIPTURE-EXACT: the report — John mid-complaint before Jesus at the camp, arm flung back toward the road he came from; certainty of having done right on his young face.",
        "must_not_show": "no halo, glare or rim-light on Jesus; John's certainty SINCERE — reporting a job well done, not sneering.",
        "scene": (
            "The report is filed with full confidence: John "
            "stands before Jesus at the roadside camp, one arm "
            "flung back toward the road behind him — we SAW "
            "him, Master, using your name, and he is not one of "
            "us, and we STOPPED him — the young face bright "
            "with the certainty of a guard who has caught "
            "something at the gate, delivering what he is sure "
            "is good news to a listener whose quiet is already "
            "saying otherwise. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r132-b02", "out": "s02-john-came-to-jesus-with.jpeg", "seg": "n0",
        "window": "9.48-11.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMP"],
        "narration": "John came to Jesus with a complaint.",
        "must_show": "the complainer — close on John's earnest young face, the grievance carried like a duty; the beloved disciple at his most human.",
        "must_not_show": "no halo; sincerity total — the complaint is loyalty, misfiled.",
        "scene": (
            "The complaint wears the face of loyalty: close on "
            "John in the late gold light, young features set "
            "with the earnest gravity of a man discharging a "
            "duty — the grievance held carefully, like "
            "something carried a long way to be laid before "
            "the right authority — love for his Master and "
            "love of the inner circle so tangled together in "
            "the honest eyes that he cannot yet tell which "
            "one of them wrote the complaint. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r132-b03", "out": "s03-seen-someone-driving-out-demons.jpeg", "seg": "n0",
        "window": "11.35-17.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["STREET", "STRANGER"],
        "narration": (
            "They'd seen someone driving out demons using Jesus's name — and "
            "the man wasn't one of their group."
        ),
        "must_show": "the work witnessed — AFTERMATH ONLY: the stranger's hands lifting from a freed man's calmed brow as he rises in relief, family amazed at the doorstep; wholeness arriving. NO demons.",
        "must_not_show": "ABSOLUTE: no demon figures, no contortion, no horror — relief, wonder and rising; the stranger earnest.",
        "scene": (
            "What they saw was mercy working under license: in "
            "the bright lane the stranger's hands lift away "
            "from a young man's calmed brow — and the man "
            "RISES, steady, clear-eyed, free, his mother's "
            "hands flying to her mouth at the doorstep, a "
            "brother laughing out loud with relief — the hard "
            "thing already over, the wholeness arriving, and "
            "over all of it the name that did the work still "
            "hanging in the air where the plain man in "
            "brick-red spoke it. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r132-b04", "out": "s04-so-they-told-him-to.jpeg", "seg": "n0",
        "window": "17.20-19.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["STREET", "STRANGER"],
        "narration": "So they told him to stop.",
        "must_show": "the stopping — two disciples' halting palms raised at the stranger; his honest confused hurt, hands still warm from the good work.",
        "must_not_show": "no halo; the stranger SYMPATHETIC — bewildered, not defiant; the stoppers officious, not cruel.",
        "scene": (
            "The good work meets a checkpoint: two of the "
            "circle step in with palms raised flat at the "
            "stranger — stop; not one of us; not authorized — "
            "and the plain man in brick-red halts with his "
            "hands still warm from the freed boy's brow, his "
            "honest face folding into bewildered hurt: stopped "
            "by the followers of the very name that just "
            "worked through him, carrying papers no one told "
            "him he needed. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r132-b05", "out": "s05-the-man-with-them-so.jpeg", "seg": "n1 + n2",
        "window": "21.65-27.32", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMP"],
        "narration": (
            "The man wasn't with them, so he shouldn't be using the name. "
            "Jesus didn't take John's side."
        ),
        "must_show": "the withheld approval — John finishing his case, awaiting the nod; Jesus level and quiet, visibly NOT nodding; the pause doing the teaching.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no rebuke YET — just the absence of agreement on his face.",
        "scene": (
            "The nod John came for never arrives: the case "
            "finished, the young disciple waits with his chin "
            "slightly lifted for the approval that follows a "
            "duty done — and Jesus simply looks at him, level "
            "and quiet in the gold light, the agreement "
            "conspicuously absent from his face — not anger, "
            "not yet even correction: just a stillness where "
            "the taking-of-sides should be, long enough for "
            "John's certainty to feel its first draft of air. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r132-b06", "out": "s06-he-went-after-the-instinct.jpeg", "seg": "n2",
        "window": "27.32-30.17", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMP"],
        "narration": "He went after the instinct underneath the complaint.",
        "must_show": "the deeper aim — Jesus's gentle discerning gaze on John, one hand indicating the young man's own chest; the gatekeeping instinct itself being addressed.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gesture GENTLE — a teacher locating the real problem, with love.",
        "scene": (
            "The correction goes past the complaint to its "
            "engine room: Jesus's gaze settles on John with "
            "gentle precision, and one open hand turns toward "
            "the young man's own chest — not the stranger, "
            "the gesture says; not the rules; HERE — the "
            "instinct itself, the little gatekeeper that lives "
            "in every loyal heart and calls its fences "
            "faithfulness — located kindly, in front of its "
            "owner, by the one teacher who corrects the root "
            "instead of the leaf. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r132-b07", "out": "s07-forbid-him-not-for-there.jpeg", "seg": "j1",
        "window": "30.76-38.17", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMP"],
        "narration": (
            "Forbid him not: for there is no man which shall do a miracle in "
            "my name, that can lightly speak evil of me."
        ),
        "must_show": "SCRIPTURE-EXACT: the word — Jesus's open hand pressing gently DOWNWARD, lowering the forbidding itself; calm finality, full warmth.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hand LOWERS (never wags) — a barrier being set down.",
        "scene": (
            "The verdict lowers a barrier instead of raising "
            "one: Jesus's open hand presses gently downward "
            "through the air — forbid him NOT — the gesture "
            "itself taking the checkpoint down, palm easing "
            "the whole apparatus of stopping toward the "
            "ground — no man borrows my name for a miracle, "
            "the calm voice runs, and turns his mouth against "
            "me by nightfall — the logic of grace, dismantling "
            "a fence with one moving hand. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r132-b08", "out": "s08-for-he-that-is-not.jpeg", "seg": "j1 + n2b",
        "window": "38.17-44.88", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMP"],
        "narration": (
            "For he that is not against us is on our part. Don't stop him, "
            "He said."
        ),
        "must_show": "SCRIPTURE-EXACT: the widened side — Jesus's arm sweeping open toward the far road where the stranger's work continues; 'on our part' drawn as an including arc.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the arc INCLUDES — opening outward, not marking a line.",
        "scene": (
            "The team roster gets rewritten with one arm: "
            "Jesus's hand sweeps open toward the far road and "
            "the villages beyond it, where somewhere a man in "
            "brick-red is still doing wonders in a name he "
            "loves — on OUR part, the arc says, ours — the "
            "circle around the little camp expanding with the "
            "gesture until it takes in every honest worker "
            "the disciples have never met — not-against "
            "promoted to with, by the only authority entitled "
            "to set the boundary. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r132-b09", "out": "s09-nobody-works-a-miracle-in.jpeg", "seg": "n2b",
        "window": "44.88-49.74", "wide": False, "jesus": False, "ref": False,
        "locks": ["STREET", "STRANGER"],
        "narration": (
            "Nobody works a miracle in My name and then turns around and "
            "speaks against Me."
        ),
        "must_show": "the logic pictured — the stranger back at his good work: kneeling by an old sufferer's mat, speaking the name with reverence on his face; loyalty visible in the work itself. NO demons.",
        "must_not_show": "ABSOLUTE: no demon imagery — the sufferer weary, warm-skinned, dignified; the stranger's reverence the picture.",
        "scene": (
            "The proof of the logic is on the stranger's face "
            "while he works: kneeling by an old woman's mat in "
            "the lane's shade, his hands gentle at her "
            "shoulder, the name leaving his lips with the "
            "unmistakable reverence of a man speaking the "
            "dearest word he owns — no one, the logic runs, "
            "spends that name with this face and slanders it "
            "at supper — the loyalty legible in the very "
            "tenderness of the work, which is the only "
            "credential he ever carried. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r132-b10", "out": "s10-whoever-against-us-is-on.jpeg", "seg": "n2b",
        "window": "49.74-53.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["STREET", "STRANGER"],
        "narration": "Whoever isn't against us is on our side.",
        "must_show": "the one field — the disciples on the road and the stranger at his doorstep work framed together in a single deep composition; the same side, one kingdom's field.",
        "must_not_show": "no halo; NO line or barrier between the groups — the composition unites them.",
        "scene": (
            "The new arithmetic fits everyone in one frame: "
            "down the bright lane the little band of disciples "
            "walks the road, and at the near doorstep the "
            "stranger steadies the old woman onto her feet — "
            "two crews of the same kingdom working the same "
            "afternoon in the same light, no fence between "
            "them anywhere in the composition, the whole "
            "field one field — on our side, the frame says, "
            "having quietly deleted the line the complaint "
            "was built on. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r132-b11", "out": "s11-for-whosoever-shall-give-you.jpeg", "seg": "jv41",
        "window": "53.68-64.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["STREET"],
        "narration": (
            "For whosoever shall give you a cup of water to drink in my "
            "name, because ye belong to Christ, verily I say unto you, he "
            "shall not lose his reward."
        ),
        "must_show": "SCRIPTURE-EXACT: the cup of water — at the cistern, a villager pressing a plain clay cup of cool water into a dusty disciple's hands; the smallest kindness at full dignity.",
        "must_not_show": "no halo; the cup PLAIN clay, the water bright; both faces warm — the transaction tiny and eternal.",
        "scene": (
            "The kingdom's smallest denomination is minted at "
            "a cistern: a villager dips a plain clay cup and "
            "presses it, dripping and cool, into the dusty "
            "hands of a road-worn disciple — because of the "
            "name he travels under, nothing more — the whole "
            "exchange over in a breath, no witness but the "
            "lane — and the verse standing over it like a "
            "seal: this cup is now on eternal deposit, and "
            "heaven does not lose accounts. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r132-b12", "out": "s12-john-thought-he-was-protecting.jpeg", "seg": "n1",
        "window": "19.81-21.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMP"],
        "narration": "John thought he was protecting the cause.",
        "must_show": "the protective instinct — John with a fist held guarding at his chest, brows knit with sincere custodial worry; loyalty in its armour.",
        "must_not_show": "no halo; NOTHING villainous — the guarding sincere, almost touching.",
        "scene": (
            "The instinct he acted on was guarding something "
            "he loves: John with one fist drawn in against his "
            "chest like a man holding a small flame out of the "
            "wind, brows knit with completely sincere worry — "
            "the cause, the circle, the Master's name, all of "
            "it HIS to protect as he understands it — loyalty "
            "standing its post in armour it forged itself, "
            "guarding a fire that was never in danger from "
            "the man it stopped. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r132-b13", "out": "s13-whoever-gives-a-cup-of.jpeg", "seg": "n3a + n3b",
        "window": "65.74-73.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["STREET"],
        "narration": (
            "Whoever gives a cup of water in His name won't lose his reward. "
            "The work isn't about belonging to a team — it's about Him."
        ),
        "must_show": "the point distilled — close on the plain clay cup passing between two pairs of hands, water bright at the rim; the giver's simple face beyond; the name the only membership.",
        "must_not_show": "no halo; no badges, no team-marks anywhere — two pairs of ordinary hands and one cup.",
        "scene": (
            "The whole teaching fits between two pairs of "
            "hands: close on the plain clay cup mid-pass, "
            "water bright and trembling at the rim, the "
            "giver's rough fingers releasing as the "
            "traveller's close — and beyond the cup the "
            "giver's simple face, asking nothing, checking no "
            "credentials, belonging to no roster anyone keeps "
            "on earth — the work never was about the team; it "
            "was about Him, and a cup of water knows the way "
            "to Him from anywhere. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r132-b14", "out": "s14-john-learned-a-lesson-that.jpeg", "seg": "n4",
        "window": "74.14-78.45", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMP"],
        "narration": (
            "John learned a lesson that day: the kingdom is bigger than the "
            "inner circle."
        ),
        "must_show": "the widened kingdom — dusk at the camp: the camera behind the seated circle's backs around the low fire with Jesus among them, and out on the far road a single lamp moving — the stranger, still at work, still counted.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the far lamp SMALL and warm — one light on the road, inside the kingdom.",
        "scene": (
            "The lesson has a view at dusk, the camera set "
            "behind the seated circle's backs: the little band "
            "around the low fire with Jesus among them, John's "
            "young face quieted into wonder across the flames — "
            "and beyond the camp, far out on the darkening "
            "road, one small lamp moves steadily toward the "
            "next village: the stranger, still working, still "
            "uncredentialed, still counted — the inner circle "
            "warm around its fire, and the kingdom, visibly, "
            "bigger than the ring of light. Every figure has "
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
