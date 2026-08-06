#!/usr/bin/env python3
"""V2 beat map — row 72, build-72-calling-matthew (Matthew 9:9-13).

COVERAGE: 41 pictures over 231.2 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 9:9-13 KJV):
  v9    "a man, named MATTHEW, sitting AT THE RECEIPT OF CUSTOM: and he
        saith unto him, FOLLOW ME. And he AROSE, and followed him." —
        the toll booth by the Capernaum road; two words; five words of
        self-report with no hesitation recorded. The abandoned booth —
        coins, scales, ledgers left mid-count — is the row's monument.
  v10   "as Jesus sat at meat IN THE HOUSE, behold, many publicans and
        sinners came and sat down with him and his disciples" — the
        dinner: Matthew's kind of people filling a rich lonely house
        with its first real company; welcome on every unaccustomed face.
  v11   "Why eateth your Master with publicans and sinners?" — the
        Pharisees AT THE DOOR, too clean to enter; the question asked at
        the disciples, not at him.
  v12-13 "They that be WHOLE need not a PHYSICIAN, but they that are
        SICK ... I will have MERCY, and not sacrifice: for I am not come
        to call the righteous, but SINNERS to repentance." — the doctor
        logic; the door-standers' self-diagnosis as the only barrier.
  vNARR Matthew the ledger-writer becomes gospel-writer (b37): the pen
        repurposed; and the closing beats set the table for the viewer.

TIME OF DAY: bright working morning at the booth; the call at midday;
the dinner in warm lamplit evening (its whole second half); the
gospel-writing beat by night lamp years later; the closing invitation
in the same dinner-lamp warmth.

CONTENT-CARE: no flags. The Pharisees correct and cold, never cartoons;
the outcast guests dignified — joy on faces unaccustomed to invitations.

CHANGING CONDITION (kept OUT of the locks): Matthew's life — booth,
rising, feast, authorship; and the booth itself: manned, abandoned
mid-count, then empty behind him for good.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "MATTHEW": (
        "MATTHEW LOCK: Matthew is the same man in every shot — about "
        "forty, soft-handed and well-fed with the beginnings of a "
        "stoop from desk work, a neat black beard, guarded intelligent "
        "eyes that warm by stages through the row. He wears a costly "
        "DARK TEAL robe with a DEEP MUSTARD sash and good rings (the "
        "rings gone by the authorship beat) (never cream, never "
        "white). His face is shown clearly."
    ),
    "BOOTH": (
        "TOLL BOOTH LOCK: the receipt of custom — a plank table under "
        "a faded awning at the road's edge outside Capernaum, iron-"
        "bound money box, brass scales, wax ledger tablets in a rack, "
        "a stool worn to the sitter's shape, and the road's traffic "
        "passing. The same table, box, scales and rack throughout."
    ),
    "HOUSE": (
        "MATTHEW'S HOUSE LOCK: a prosperous but unloved town house — a "
        "fine dining room with a long low table, good lamps, costly "
        "but sparse furnishings that show no guests have used them, "
        "and a wide door to the street. It fills with light and people "
        "through the dinner beats."
    ),
    "GUESTS": (
        "OUTCAST GUESTS LOCK: Matthew's people — other tax men with "
        "their guarded faces, a weathered woman the town whispers "
        "about, a scarred ex-soldier, a young man too fond of wine, "
        "in mixed costly-and-worn DEEP colours: dark teal, deep "
        "russet, faded plum, dark olive (never cream, never white; "
        "only Jesus wears cream). Faces shown clearly — dignity and "
        "unaccustomed welcome."
    ),
    "PHARISEES": (
        "PHARISEES LOCK: the objectors are the same three men in "
        "every shot — fine NEAR-BLACK INDIGO robes, fringed shawls, "
        "correct cold faces (never cream, never white). They appear "
        "at the DOOR only, never inside. Faces shown clearly."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r072-b01", "out": "s01-there-was-one-job-in.jpeg", "seg": "n1",
        "window": "0.28-5.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["MATTHEW", "BOOTH"],
        "narration": (
            "There was one job in every Galilee town that made you a traitor to "
            "your own people. Tax collector."
        ),
        "must_show": "the job introduced — Matthew at his booth in the bright morning: the table, the box, the scales, and the road's traffic giving him its practised wide berth.",
        "must_not_show": "no halo, glare or rim-light; the wide berth visible — a working man socially quarantined at his own table.",
        "scene": (
            "At the road's edge under the faded awning "
            "Matthew sits at his plank table in the "
            "bright morning — money box at his elbow, "
            "brass scales balanced, wax tablets racked "
            "— while the road's traffic bends around "
            "his station in a long practised curve: "
            "farmers hugging the far verge, a mother "
            "steering her children wide, every passing "
            "back a verdict on the man at the table. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r072-b02", "out": "s02-you-worked-for-rome-the.jpeg", "seg": "n1",
        "window": "5.70-14.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["MATTHEW", "BOOTH"],
        "narration": (
            "You worked for Rome, the empire occupying your homeland, and you "
            "got rich taking money from your neighbors, most of it more than "
            "Rome even asked for."
        ),
        "must_show": "the machine at work — a farmer paying at the table, Roman authority implied by the sealed box; the over-count visible in the farmer's grieved face and Matthew's practised fingers.",
        "must_not_show": "no halo, glare or rim-light; the extraction procedural — no cartoon greed; a system, operating.",
        "scene": (
            "At the booth the machine runs: a lean "
            "farmer counts coins onto the plank one at "
            "a time, his jaw tight at the number — "
            "while Matthew's soft practised fingers "
            "walk the count into the iron-bound box "
            "with its blunt Roman seal, and the brass "
            "scales tip once more against somebody's "
            "margin — the empire's arithmetic and one "
            "local man's percentage, collected in the "
            "same motion. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b03", "out": "s03-matthew-had-that-job.jpeg", "seg": "n1",
        "window": "14.99-16.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["MATTHEW"],
        "narration": "Matthew had that job.",
        "must_show": "the man behind the table — a close portrait: intelligence, guardedness, and the specific loneliness of the well-paid despised.",
        "must_not_show": "no halo, glare or rim-light; no villainy — a capable man in a hated chair.",
        "scene": (
            "A close portrait at the booth: Matthew's "
            "intelligent guarded face above the neat "
            "black beard — eyes quick from years of "
            "counting and watchful from years of being "
            "watched, the beginnings of a desk-stoop "
            "in the good teal shoulders — the face of "
            "a man who chose money over belonging "
            "long enough ago that he has stopped "
            "letting himself do the arithmetic on the "
            "trade. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r072-b04", "out": "s04-so-matthew-had-money-and.jpeg", "seg": "n2",
        "window": "17.53-22.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["MATTHEW", "BOOTH"],
        "narration": (
            "So Matthew had money, and Matthew had no one. The devout would not "
            "touch him."
        ),
        "must_show": "the untouchability — a devout man dropping his toll onto the table from a height, avoiding all contact; coins touched, man never.",
        "must_not_show": "no halo, glare or rim-light; the avoidance precise — payment without one point of human contact.",
        "scene": (
            "At the booth a fringed devout man pays "
            "from a careful height — the coins dropped "
            "the last inch to the plank so his fingers "
            "share nothing with the table, his eyes "
            "fixed over Matthew's head, his sleeve "
            "gathered back — the toll rendered in "
            "full and the man behind the table "
            "rendered invisible, in one fastidious "
            "motion. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r072-b05", "out": "s05-his-old-friends-were-long.jpeg", "seg": "n2",
        "window": "22.15-30.66", "wide": True, "jesus": False, "ref": False,
        "locks": ["MATTHEW", "BOOTH"],
        "narration": (
            "His old friends were long gone. He sat at his booth by the road "
            "every day, counting silver, while the whole town walked a little "
            "wider around him."
        ),
        "must_show": "the daily exile — the booth at busy midday: the road full, the town's traffic curving wide, and Matthew counting alone at the still centre of the avoidance.",
        "must_not_show": "no halo, glare or rim-light; the width of the berth the measure — a man islanded by his own table.",
        "scene": (
            "At busy midday, the camera across the road taking "
            "booth and traffic from the side, the road runs full past "
            "the booth — carts, herds, market baskets, "
            "the town's whole traffic — and all of it "
            "bending in the same wide practised curve "
            "around the awning's shade, where Matthew "
            "sits counting silver into stacks with no "
            "company but the click of the coins: a "
            "man at the centre of a crowd's daily "
            "geometry, drawn around him like a moat. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r072-b06", "out": "s06-rich-and-completely-alone.jpeg", "seg": "n2",
        "window": "30.66-33.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["MATTHEW"],
        "narration": "Rich, and completely alone.",
        "must_show": "the sum — close: Matthew's ringed hands stacking silver high, and his eyes over the stacks following the town's turned backs; wealth counted against company.",
        "must_not_show": "no halo, glare or rim-light; both facts in one frame — full hands, empty gaze.",
        "scene": (
            "Close at the booth: Matthew's soft "
            "ringed hands stacking the morning's "
            "silver into neat towers — and above the "
            "growing wealth his guarded eyes have "
            "drifted, following a knot of old "
            "schoolmates passing on the far verge "
            "with their heads together and their "
            "backs to him — the day's two balances, "
            "one rising in metal, one long ago gone "
            "to nothing. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b07", "out": "s07-and-this-is-the-man.jpeg", "seg": "n3",
        "window": "33.76-36.92", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MATTHEW", "BOOTH"],
        "narration": "And this is the man Jesus walked up to. Not around.",
        "must_show": "SCRIPTURE-EXACT: the approach — Jesus walking STRAIGHT at the booth against the traffic's curve: the first trajectory in years aimed AT the table.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the geometry the beat — one straight line through a town of curves.",
        "scene": (
            "Against the road's practised curve, the camera behind "
            "the passing walkers' shoulders, one "
            "trajectory runs straight: Jesus walking "
            "directly at the toll booth through the "
            "midday traffic — not drifting wide, not "
            "hugging the verge, his line aimed at "
            "the plank table like a drawn string — "
            "and behind the scales Matthew's counting "
            "hands have stopped, his guarded eyes "
            "rising at the one approach his station "
            "has never once received. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b08", "out": "s08-past-everyone-who-would-have.jpeg", "seg": "n3",
        "window": "38.05-46.12", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MATTHEW", "BOOTH"],
        "narration": (
            "Past everyone who would have been a safer, more respectable "
            "choice, straight to the booth nobody else wanted to stand near."
        ),
        "must_show": "the passed-over — Jesus moving past respectable candidates (a scribe, a devout elder) visible in the frame, arriving at the booth's shade; the choice's scandal in the geography.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the safer choices real and passed — respectability watching itself be walked past.",
        "scene": (
            "Down the road's edge Jesus passes the "
            "town's better options one by one — a "
            "young scribe with his satchel of "
            "learning, a devout elder straightening "
            "hopefully as the teacher nears — and "
            "walks past both into the faded awning's "
            "shade, arriving at the one table in "
            "town with a moat around it, while the "
            "passed-over faces behind him do their "
            "own astonished arithmetic. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b09", "out": "s09-follow-me-two-words.jpeg", "seg": "j1 + n4",
        "window": "46.73-49.96", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MATTHEW", "BOOTH"],
        "narration": "Follow me. Two words.",
        "must_show": "SCRIPTURE-EXACT: the call — the two faces across the toll table: Jesus's open invitation, Matthew's guarded eyes cracking; two words landing on a whole life.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the economy absolute — no gesture beyond presence and the words' visible landing.",
        "scene": (
            "Across the coin-stacked plank the two "
            "faces meet: Jesus's warm and direct, the "
            "two words just given at conversational "
            "volume — and Matthew's guarded "
            "intelligence cracking open around them "
            "in real time, the counting-house eyes "
            "widening, the soft ringed hands gone "
            "still on the silver — the shortest "
            "job offer in history, arriving at the "
            "loneliest desk in town. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b10", "out": "s10-no-pay-it-all-back.jpeg", "seg": "n4",
        "window": "51.46-55.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOTH"],
        "narration": "No pay it all back first. No prove you have changed.",
        "must_show": "the absent conditions — the ledger rack close: the accounts of what everyone owes, and NO new tablet of terms for Matthew; the paperwork that never existed.",
        "must_not_show": "no halo, glare or rim-light; the rack full of everyone's debts and empty of his conditions — grace's missing document.",
        "scene": (
            "Close on the booth's tablet rack in the "
            "awning shade: row on row of wax "
            "ledgers, every neighbour's debt scored "
            "and filed in Matthew's neat hand — and "
            "nowhere in the rack, on the table, or "
            "anywhere under the awning, one tablet "
            "of terms for the man himself: the "
            "single unwritten document in a booth "
            "made entirely of accounts. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b11", "out": "s11-no-list-of-conditions-to.jpeg", "seg": "n4",
        "window": "55.63-60.78", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MATTHEW"],
        "narration": (
            "No list of conditions to clear before he was allowed to come. "
            "Just, come."
        ),
        "must_show": "the unconditional received — close on Matthew's face at the call's simplicity: a lifetime's braced defences finding no clause to brace against.",
        "must_not_show": "no halo, glare or rim-light; the defencelessness of grace — a negotiator with nothing to negotiate.",
        "scene": (
            "Close on Matthew's face in the awning "
            "shade: the professional negotiator's "
            "features scanning the offer for its "
            "terms — and finding none: no clawback, "
            "no probation, no schedule of proofs — "
            "the guarded eyes moving left and right "
            "across a contract one line long, and "
            "slowly, helplessly, beginning to shine. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r072-b12", "out": "s12-and-he-arose-and-followed.jpeg", "seg": "s9 + n5",
        "window": "61.33-66.50", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MATTHEW", "BOOTH"],
        "narration": "And he arose, and followed him. He got up, and he left it.",
        "must_show": "SCRIPTURE-EXACT: the rising — Matthew on his feet, the stool tipping back, already stepping around the table toward Jesus; the arising mid-motion.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the motion decisive — a life exiting its furniture without a backward glance.",
        "scene": (
            "The arising, mid-motion: Matthew on his "
            "feet with the worn stool tipping back "
            "behind his knees, one hand pushing off "
            "the coin-stacked plank as he steps "
            "around the table's end toward the "
            "waiting figure in cream — the teal robe "
            "swinging, the rings catching the light "
            "in their last professional hour — a man "
            "leaving a fortified position at a walk, "
            "without looking back at it once. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r072-b13", "out": "s13-the-coins-the-scales-the.jpeg", "seg": "n5",
        "window": "66.50-74.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOTH"],
        "narration": (
            "The coins, the scales, the ledgers, the whole profitable, lonely "
            "life, sitting right there on the table."
        ),
        "must_show": "the monument — the abandoned booth close: silver mid-stack, scales still settling, a ledger open at an unfinished line; everything left exactly mid-count.",
        "must_not_show": "no halo, glare or rim-light; the mid-count exactness the beat — a life interrupted at the comma.",
        "scene": (
            "The booth stands abandoned mid-count: "
            "silver towers with one stack half-built, "
            "the brass scales still swaying toward "
            "their settle, a wax ledger open at a "
            "line that ends mid-figure with the "
            "stylus laid across it, the stool on its "
            "back in the dust — the whole profitable "
            "lonely apparatus holding its breath "
            "under the awning, waiting for a man who "
            "is never coming back. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b14", "out": "s14-matthew-tells-his-own-story.jpeg", "seg": "n5",
        "window": "74.44-81.26", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Matthew tells his own story in five words and does not give "
            "himself a single one of them for hesitating."
        ),
        "must_show": "the five words as artifact — a close still: a gospel scroll's line, brief among fuller passages, the author's own calling in his own spare hand.",
        "must_not_show": "no halo, glare or rim-light; ancient script, no legible modern words — the brevity visible as a short line amid long ones.",
        "scene": (
            "A close still in lamplight: a gospel "
            "scroll's column where one line runs "
            "conspicuously short amid the full "
            "passages around it — a spare five-word "
            "entry in a careful bookkeeper's hand, "
            "unornamented, unexpanded — a man "
            "recording the hinge of his own life "
            "with less ink than he once spent on a "
            "cart of grain. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b15", "out": "s15-he-walked-away-from-all.jpeg", "seg": "n5",
        "window": "81.26-84.79", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MATTHEW", "BOOTH"],
        "narration": "He walked away from all of it that afternoon, and followed him.",
        "must_show": "the walk — the two figures going down the road together, the abandoned booth shrinking behind under its awning; the following begun in daylight.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the booth in the background the row's hinge — left, whole, unmissed.",
        "scene": (
            "Down the afternoon road the two walk "
            "together — Jesus and the teal-robed tax "
            "man falling into step beside him, "
            "Matthew's desk-stooped shoulders already "
            "straightening by degrees — while behind "
            "them under its faded awning the "
            "abandoned booth shrinks with distance, "
            "silver and scales and every unfinished "
            "account keeping each other company in "
            "the shade. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b16", "out": "s16-and-then-something-even-stranger.jpeg", "seg": "n6",
        "window": "85.37-89.97", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MATTHEW", "HOUSE"],
        "narration": (
            "And then something even stranger. Jesus went to Matthew's house "
            "for dinner."
        ),
        "must_show": "SCRIPTURE-EXACT: the arrival — Jesus stepping through Matthew's wide door into the fine unused dining room, Matthew lighting lamps with his own hands, joy fumbling at hospitality.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the house's unused-ness visible — costly rooms hosting their first real guest.",
        "scene": (
            "Through the wide street door Jesus "
            "steps into Matthew's fine dining room — "
            "and the host is everywhere at once: "
            "lighting the good lamps with his own "
            "ringed hands, dragging cushions to the "
            "long table's places, calling through "
            "the back door for food — a costly, "
            "guestless room being woken from years "
            "of furniture-sleep by the first visitor "
            "its owner ever actually wanted. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r072-b17", "out": "s17-and-the-room-filled-up.jpeg", "seg": "n6",
        "window": "89.97-95.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["MATTHEW", "GUESTS", "HOUSE"],
        "narration": (
            "And the room filled up with Matthew's kind of people. Other tax "
            "collectors. Outcasts."
        ),
        "must_show": "the filling — the outcast guests arriving through the door in twos and threes: tax men, the whispered-about woman, the scarred soldier; a room gaining its first congregation.",
        "must_not_show": "no halo, glare or rim-light; the arrivals' faces the beat — people entering somewhere they are wanted, on unfamiliar legs.",
        "scene": (
            "Through Matthew's door his people "
            "arrive in twos and threes: a fellow "
            "tax man still checking the invitation "
            "against his own disbelief, the "
            "weathered whispered-about woman with "
            "her chin defiantly up, the scarred "
            "ex-soldier ducking the lintel, the "
            "wine-fond young man scrubbed and "
            "nervous — the lamplit room filling "
            "with every face this town has "
            "practised not seeing, all of them "
            "here, all of them asked for. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r072-b18", "out": "s18-the-men-and-women-the.jpeg", "seg": "n6",
        "window": "95.83-102.74", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MATTHEW", "GUESTS", "HOUSE"],
        "narration": (
            "The men and women the rest of the town had quietly given up on. "
            "And he sat down in the middle of them and ate."
        ),
        "must_show": "SCRIPTURE-EXACT: the sitting among — Jesus at the table's MIDDLE, not its head: bread in hand, shoulder to shoulder with tax men and outcasts, eating.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the middle seat the doctrine — no space around him, the eating real.",
        "scene": (
            "At the long table's exact middle, the camera down the "
            "table's length with the near guests in three-quarter, "
            "Jesus "
            "sits shoulder to shoulder in the crowd "
            "of the given-up-on — bread torn in his "
            "hand, listening to the scarred "
            "soldier's story with his mouth full, "
            "the whispered-about woman refilling "
            "his cup unasked — no head seat taken, "
            "no space held around him, a guest "
            "fully inside the meal at the one "
            "table in town respectability abandoned "
            "to its own devices. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b19", "out": "s19-look-at-who-is-at.jpeg", "seg": "n7",
        "window": "103.32-106.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["GUESTS", "HOUSE"],
        "narration": "Look at who is at that table. Not the respectable.",
        "must_show": "the census — close along the table's faces: the guests one by one in the lamplight; the guest list as the gospel.",
        "must_not_show": "no halo, glare or rim-light; each face particular — a roll call of the unrolled.",
        "scene": (
            "Close along the lamplit table the "
            "census reads itself: the fellow tax "
            "man's guard finally down over his cup, "
            "the weathered woman laughing at "
            "something with her whole face, the "
            "ex-soldier's scar creased by an "
            "unpractised smile, the nervous young "
            "man reaching for bread like a citizen "
            "— the town's whole discard pile, "
            "revealed by lamplight to be people. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r072-b20", "out": "s20-not-the-qualified-the-people.jpeg", "seg": "n7",
        "window": "106.68-114.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["GUESTS", "HOUSE"],
        "narration": (
            "Not the qualified. The people who were used to being turned away "
            "at every door, finding themselves, for once, welcome."
        ),
        "must_show": "welcome landing — close on the whispered-about woman's face mid-meal: the specific disbelief of being wanted somewhere, melting by degrees.",
        "must_not_show": "no halo, glare or rim-light; the melting gradual — welcome believed one degree at a time.",
        "scene": (
            "Close on the weathered woman's face in "
            "the lamp warmth: the defiant chin "
            "lowered by degrees through the meal, "
            "the practised readiness-to-be-asked-"
            "to-leave dissolving out of her "
            "shoulders, her eyes coming up from her "
            "plate to the table's laughter and "
            "staying up — a lifetime's worth of "
            "doors closing, being outvoted by one "
            "evening of a door that didn't. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r072-b21", "out": "s21-you-can-see-it-on.jpeg", "seg": "n7",
        "window": "114.92-117.30", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MATTHEW", "GUESTS", "HOUSE"],
        "narration": "You can see it on their faces.",
        "must_show": "the room's weather — the whole table wide in the lamplight: belonging visible on every face at once, the host's most of all.",
        "must_not_show": "no halo, glare or rim-light; the joy general — a room-sized change of climate.",
        "scene": (
            "The whole long table sits warm in its "
            "lamplight: cups mid-raise, two "
            "conversations crossing, the ex-soldier "
            "demonstrating something with a bread "
            "loaf, Jesus laughing in the middle of "
            "it — and at the table's end Matthew "
            "surveys his own filled house with the "
            "stunned face of a man whose fine empty "
            "rooms have finally learned their "
            "purpose: the loneliest address in "
            "Capernaum, at capacity. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b22", "out": "s22-the-religious-men-could-not.jpeg", "seg": "n8",
        "window": "117.82-125.81", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEES", "HOUSE"],
        "narration": (
            "The religious men could not stand it. They stood at the door, too "
            "clean to come in, and asked his disciples the question that gave "
            "the whole thing away."
        ),
        "must_show": "SCRIPTURE-EXACT: the door-standers — the three dark-robed men at the threshold, inside visible and warm past them, their feet planted exactly at the line they will not cross.",
        "must_not_show": "no halo, glare or rim-light; the threshold their whole geography — cleanliness as a wall of their own masonry.",
        "scene": (
            "At the wide doorway, the camera inside the room "
            "behind the lamplit guests, the three fine-"
            "robed men stand planted exactly at the "
            "threshold line — the lamplit feast "
            "warm and loud a single step past "
            "their unhesitating feet — fringed "
            "shawls gathered close against the "
            "room's contamination, cold correct "
            "faces cataloguing the guest list over "
            "the disciples' shoulders: three men "
            "held out of a party by nothing on "
            "earth but their own hems. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b23", "out": "s23-why-eateth-your-master-with.jpeg", "seg": "s11",
        "window": "126.39-129.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEES"],
        "narration": "Why eateth your Master with publicans and sinners?",
        "must_show": "SCRIPTURE-EXACT: the question — close on the senior objector's face asking it past the door: genuine incomprehension wearing correctness.",
        "must_not_show": "no halo, glare or rim-light; the incomprehension real — a category error spoken aloud by its owner.",
        "scene": (
            "Close at the threshold: the senior "
            "objector's correct cold face mid-"
            "question, one fringed arm gesturing "
            "past the doorframe at the warm "
            "offending room — the words leaving him "
            "with the genuine bafflement of a man "
            "whose whole system has no shelf for "
            "what he is looking at: goodness, "
            "voluntarily seated among the "
            "disqualified. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b24", "out": "s24-why-does-your-teacher-eat.jpeg", "seg": "n8b",
        "window": "131.09-134.33", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEES", "HOUSE"],
        "narration": "Why does your teacher eat with tax collectors and sinners?",
        "must_show": "the question's target — from the doorway past the objectors' shoulders: the table's warmth framed by their dark silhouettes; the thing they cannot parse, in view.",
        "must_not_show": "no halo, glare or rim-light; the framing the argument — cold shoulders bracketing warm light.",
        "scene": (
            "From behind the door-standers the "
            "question's whole target shows: past "
            "their dark correct shoulders the "
            "lamplit table runs golden and loud — "
            "bread passing, the woman laughing, the "
            "teacher's cream sleeve among the teal "
            "and russet — the room's warmth framed "
            "between two near-black silhouettes "
            "like a hearth seen from a cold street. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r072-b25", "out": "s25-they-did-not-ask-it.jpeg", "seg": "n8b",
        "window": "134.33-141.96", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEES"],
        "narration": (
            "They did not ask it to learn anything. They asked it because they "
            "could not imagine why anyone good would want to be in that room."
        ),
        "must_show": "the failure of imagination — the three faces at the door surveying the joy with forensic incomprehension; goodness observed like a foreign script.",
        "must_not_show": "no halo, glare or rim-light; no malice needed — the blindness sincere, which is its tragedy.",
        "scene": (
            "The three faces at the threshold survey "
            "the feast like scholars over an "
            "untranslatable text: the senior's brows "
            "drawn in genuine study, the second "
            "taking silent inventory of every "
            "compromised guest, the third's lips "
            "moving faintly as if sounding out a "
            "word that will not resolve — three "
            "sincere men reading joy in a language "
            "their whole training never taught. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r072-b26", "out": "s26-they-that-be-whole-need.jpeg", "seg": "j2",
        "window": "142.51-146.51", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": "They that be whole need not a physician, but they that are sick.",
        "must_show": "SCRIPTURE-EXACT: the answer over the shoulder — Jesus turning from the table toward the door, the physician-line given mid-meal, easy and total.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the answer unruffled — a diagnosis delivered without leaving dinner.",
        "scene": (
            "From his place at the table's middle "
            "Jesus turns toward the doorway — bread "
            "still in one hand, the answer going "
            "out over his shoulder with the easy "
            "carry of a man not interrupting his "
            "own dinner for it — the physician-line "
            "crossing the room to the threshold at "
            "exactly the volume of its own common "
            "sense, while the table's noise dips "
            "once and resumes. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b27", "out": "s27-but-go-ye-and-learn.jpeg", "seg": "j2",
        "window": "146.51-157.42", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PHARISEES", "HOUSE"],
        "narration": (
            "But go ye and learn what that meaneth, I will have mercy, and not "
            "sacrifice: for I am not come to call the righteous, but sinners to "
            "repentance."
        ),
        "must_show": "SCRIPTURE-EXACT: the homework assigned — Jesus's gaze holding the door-standers full across the room: the mercy-verse given TO the correct as their assignment; the room's warmth unbroken around it.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no triumph — the assignment given kindly; the objectors' faces receiving an exam they did not expect.",
        "scene": (
            "Across the warm room Jesus's gaze holds "
            "the three at the threshold — the "
            "mercy-verse crossing to them measured "
            "and kind, homework assigned from a "
            "dinner table to the schooled — and on "
            "the correct cold faces something "
            "unexpected flickers: the sensation, "
            "rare and unwelcome, of standing at a "
            "door as the student — while behind the "
            "teacher the feast goes on undimmed. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r072-b28", "out": "s28-up-to.jpeg", "seg": "n3",
        "window": "36.92-38.05", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BOOTH"],
        "narration": "Up to.",
        "must_show": "the preposition made flesh — extreme close: Jesus's sandalled feet stopping in the booth's shade, planted at the table; arrival, not passage.",
        "must_not_show": "no halo, glare or rim-light; feet and dust and table-shadow — the whole gospel of approach in a stance.",
        "scene": (
            "Extreme close at the booth's shade-"
            "line: Jesus's worn sandalled feet "
            "coming to a full stop on the packed "
            "dust — planted square before the plank "
            "table's legs, the walking done, the "
            "toes pointed AT the booth and not past "
            "it — the rarest event in this "
            "particular patch of ground: an arrival, "
            "recorded at ankle height. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b29", "out": "s29-a-doctor-does-not-spend.jpeg", "seg": "n9",
        "window": "158.97-163.47", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "A doctor does not spend his day with the healthy. He goes where "
            "the sickness is."
        ),
        "must_show": "the physician logic — a village healer's vignette: a doctor kneeling at a sick man's mat in a poor doorway, his bag open; presence where the need is.",
        "must_not_show": "no halo, glare or rim-light; the analogy plain — medicine at the address of the ailment.",
        "scene": (
            "In a poor doorway's shade a village "
            "healer kneels at a sick man's mat — his "
            "worn remedy bag open at his knee, two "
            "fingers at the patient's wrist, his "
            "whole practice located exactly where "
            "the fever is — while up the lane the "
            "healthy go about their sunlit business "
            "unattended, requiring, as the saying "
            "goes, nothing from him at all. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r072-b30", "out": "s30-go-and-learn-what-this.jpeg", "seg": "n9",
        "window": "163.47-168.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEES"],
        "narration": (
            "Go and learn what this means, he told them — I want mercy, not "
            "sacrifice."
        ),
        "must_show": "the assignment walked home — the three objectors departing up the night street from the lit doorway, the verse following them; homework in retreating backs.",
        "must_not_show": "no halo, glare or rim-light; the retreat thoughtful, not routed — one of the three glancing back.",
        "scene": (
            "Up the dark street the three walk away "
            "from the lit doorway — robes gathered, "
            "pace stiff with unfinished dignity — "
            "and at the corner the youngest of them "
            "glances back once at the warm noise "
            "they declined: three scholars carrying "
            "home, against their will, a one-line "
            "assignment older than their whole "
            "training, with its answer still lit "
            "behind them. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b31", "out": "s31-that-was-his-whole-answer.jpeg", "seg": "n9",
        "window": "168.52-173.55", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": (
            "That was his whole answer. He did not come for the people who had "
            "it all together."
        ),
        "must_show": "the mission statement resting — Jesus back fully into the meal, the door forgotten, his attention returned whole to the guests; the answer complete and closed.",
        "must_not_show": "no halo, glare or rim-light; the return to table the punctuation — controversy outlived by dinner.",
        "scene": (
            "The doorway empty now, Jesus is back "
            "fully in the meal — turned to the "
            "ex-soldier's resumed story, his cup "
            "held out to the woman's pitcher, the "
            "whole controversy already behind him "
            "like weather passed — a mission "
            "statement delivered, defended and "
            "closed inside ten minutes, without the "
            "dinner going cold. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b32", "out": "s32-he-came-for-the-ones.jpeg", "seg": "n9 + n10",
        "window": "173.55-179.18", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MATTHEW", "HOUSE"],
        "narration": (
            "He came for the ones who knew that they did not. And that is the "
            "quiet turn in the story."
        ),
        "must_show": "the qualifying knowledge — Matthew's face at his own table: the man who KNEW his need, seated in the answer to it; self-knowledge as the only entry ticket.",
        "must_not_show": "no halo, glare or rim-light; the host's gratitude quiet — a man aware of exactly what found him.",
        "scene": (
            "At his own table's end Matthew watches "
            "the feast he never dreamed his rooms "
            "would hold — and his face carries the "
            "row's quiet turn: no triumph, only the "
            "settled gratitude of a man who knew "
            "precisely how sick he was, which "
            "turned out to be the entire admission "
            "requirement — the one qualification "
            "the door-standers lacked, worn like "
            "an heirloom. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b33", "out": "s33-the-outcasts-were-close-to.jpeg", "seg": "n10",
        "window": "179.18-183.19", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GUESTS", "HOUSE"],
        "narration": "The outcasts were close to him because they knew they needed him.",
        "must_show": "nearness as diagnosis — the table's seating close: the guests physically nearest Jesus, need translated directly into proximity.",
        "must_not_show": "no halo, glare or rim-light; the seating chart the sermon — closeness earned by admitted need.",
        "scene": (
            "Close on the table's geography: the "
            "guests packed nearest Jesus in "
            "unconscious order of their honesty — "
            "the whispered-about woman at his "
            "elbow, the nervous young man across, "
            "the scarred soldier leaning in — need "
            "seated by need in warm lamplight, the "
            "room's whole floor plan drawn by the "
            "one rule the door-standers never "
            "learned: knowing translates to near. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r072-b34", "out": "s34-the-religious-men-stood-outside.jpeg", "seg": "n10",
        "window": "183.19-189.00", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEES", "HOUSE"],
        "narration": (
            "The religious men stood outside, arms folded, because they were "
            "sure they did not."
        ),
        "must_show": "distance as diagnosis — the street view: the lit house warm behind, and the three at their remove in the dark, arms folded; certainty measured in paces from the door.",
        "must_not_show": "no halo, glare or rim-light; their exile self-administered — the door open behind their turned backs.",
        "scene": (
            "In the dark street, the camera behind the three "
            "watchers' dark shoulders toward the lit house, they stand at "
            "their chosen remove — arms folded into "
            "fringed shawls, backs half-turned to "
            "the lit doorway that never closed "
            "against them — the house's warmth "
            "reaching out across the paving to the "
            "exact line their certainty drew, and "
            "stopping there: three men quarantined "
            "from a feast by a clean bill of health "
            "they wrote themselves. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b35", "out": "s35-the-only-thing-that-kept.jpeg", "seg": "n10",
        "window": "189.00-194.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": (
            "The only thing that kept anyone from that table was believing they "
            "were already fine."
        ),
        "must_show": "the barrier named — the open doorway itself close: warm light, no bar, no lock, no keeper; the only obstacle invisible and self-supplied.",
        "must_not_show": "no halo, glare or rim-light; the door's total openness the evidence — nothing in the frame excludes anyone.",
        "scene": (
            "The doorway close in the night: wide "
            "open, warm-lit, unbarred — no keeper "
            "at the jamb, no list in any hand, the "
            "threshold stone worn smooth and "
            "inviting, the feast's gold spilling "
            "out across it unguarded — history's "
            "most accessible door, kept shut "
            "nightly, all over the world, entirely "
            "from the outside. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b36", "out": "s36-and-notice-what-is-missing.jpeg", "seg": "n4",
        "window": "49.96-51.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOOTH"],
        "narration": "And notice what is missing from them.",
        "must_show": "the missing conditions — the two words' aftermath at the booth: silence, stacked silver, and no contract anywhere; absence as content.",
        "must_not_show": "no halo, glare or rim-light; the frame deliberately spare — what is NOT there, on display.",
        "scene": (
            "The booth in the call's after-silence: "
            "the stacked silver, the balanced "
            "scales, the racked ledgers of every "
            "neighbour's obligation — a whole "
            "architecture of terms and conditions — "
            "and hanging in the air above all of "
            "it, two words with no paperwork "
            "attached: the only transaction this "
            "table ever hosted that came with "
            "nothing owing. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b37", "out": "s37-as-for-matthew-the-man.jpeg", "seg": "n11",
        "window": "194.91-211.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["MATTHEW"],
        "narration": (
            "As for Matthew, the man who had spent his life writing down what "
            "other people owed became a writer of a very different kind: one of "
            "the four accounts of the life of Jesus in your Bible has his name "
            "on it."
        ),
        "must_show": "the pen repurposed — years later: an older, ringless Matthew at a night lamp writing on a long scroll, the bookkeeper's precision serving a different ledger.",
        "must_not_show": "no halo, glare or rim-light; the same neat hand, the new subject — the transformation told through the writing posture.",
        "scene": (
            "Years on, by a single night lamp: an "
            "older Matthew — the rings gone, the "
            "teal faded to a plain workman's robe — "
            "bends over a long scroll in the exact "
            "desk-stooped posture of the old booth, "
            "the bookkeeper's neat hand laying down "
            "line after careful line — the same "
            "precision that once recorded a town's "
            "debts, spending its old skill on the "
            "one account where every debt reads "
            "PAID. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r072-b38", "out": "s38-that-is-what-the-call.jpeg", "seg": "n11",
        "window": "211.14-214.04", "wide": False, "jesus": False, "ref": False,
        "locks": ["MATTHEW"],
        "narration": "That is what the call did to him.",
        "must_show": "the before-and-after in one face — the older Matthew's face at his writing: the guarded booth eyes long gone; warmth resident where wariness lived.",
        "must_not_show": "no halo, glare or rim-light; the change complete and quiet — a renovated countenance.",
        "scene": (
            "Close on the older Matthew's face in "
            "the lamp's small gold: the guarded "
            "quick-counting eyes of the booth "
            "nowhere in it — warmth resident in "
            "their place, the intelligence turned "
            "open, the neat beard gone grey around "
            "a mouth at peace — a face renovated "
            "room by room across the years since "
            "two words found it at a toll table. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r072-b39", "out": "s39-and-the-table-he-sat.jpeg", "seg": "n12",
        "window": "214.62-217.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": "And the table he sat at is still set.",
        "must_show": "the standing feast — the long table set and lamplit, places laid, cushions ready; the dinner as permanent institution.",
        "must_not_show": "no halo, glare or rim-light; the readiness present-tense — a table that never closed.",
        "scene": (
            "The long table stands set in its "
            "lamplight — places laid down both "
            "sides, bread under cloths, cups "
            "upright, cushions plumped at every "
            "seat, the wide door open to the night "
            "street — Matthew's one great dinner "
            "party revealed as what it always was: "
            "not an evening but an institution, "
            "still open, still staffed, still "
            "seating. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b40", "out": "s40-the-same-door-is-still.jpeg", "seg": "n12",
        "window": "217.28-225.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": (
            "The same door is still open, the same welcome still held out to "
            "exactly the people who assume they would never be let in."
        ),
        "must_show": "the assumption answered — from the dark street: the open door's warmth, and on the threshold stone a lamp set out LIKE A SIGNAL to the hesitant; welcome, advertised.",
        "must_not_show": "no halo, glare or rim-light beyond the lamps' own; the set-out lamp the gesture — light placed for the unsure.",
        "scene": (
            "From the dark street the door stands "
            "open on its warmth — and on the "
            "threshold stone itself a small clay "
            "lamp has been set out, deliberately, "
            "its flame steady in the night air: a "
            "signal placed at exactly the eye-"
            "height of someone hanging back in the "
            "dark, by a host who knows from "
            "experience precisely how the hesitant "
            "read doorways. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r072-b41", "out": "s41-he-is-not-waiting-for.jpeg", "seg": "n12",
        "window": "225.71-230.97", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": (
            "He is not waiting for you to qualify. He is asking you to come and "
            "eat."
        ),
        "must_show": "the closing image — through the open door: Jesus at the lamplit table looking up toward the doorway — toward the viewer — one hand indicating the empty place beside him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the empty place and the direct look — the invitation aimed out of the frame.",
        "scene": (
            "Through the open doorway the table's "
            "warmth frames its center: Jesus looking "
            "up from the meal directly toward the "
            "door — toward whoever stands in the "
            "dark street looking in — his hand "
            "resting open beside the one empty "
            "place at his side, cushion plumped, "
            "cup filled, bread waiting — the whole "
            "row's welcome gathered into one look "
            "and one saved seat, held for exactly "
            "the person who assumes it isn't. Every "
            "figure has two arms, two hands and "
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
    "BOOTH": "PLACE-REF/booth.jpeg",  # build-72-calling-matthew s01-there-was-one-job-in (manual)
    "HOUSE": "PLACE-REF/house.jpeg",  # build-72-calling-matthew s16-and-then-something-even-stranger (manual)
}
# === end PLACE-PLATES ===
