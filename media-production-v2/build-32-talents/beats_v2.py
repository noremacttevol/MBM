#!/usr/bin/env python3
"""V2 beat map — row 32, build-32-talents (Matthew 25:14-30).

COVERAGE: 25 pictures over 143.8 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 25:14-30 KJV):
  Setting of the telling: the Mount of Olives discourse continues (Matthew
  24:3) — the talents follows the ten virgins in the same private evening
  teaching. Row 31 staged Olivet as a seated circle at gold evening and a
  dusk lean-in; THIS build's one frame beat (b03) looks from BEHIND Jesus's
  shoulder over the disciples' faces with Jerusalem's dusk lights beyond —
  a different composition, no repeat.
  v14-15 "delivered unto them HIS goods ... to every man ACCORDING TO HIS
        SEVERAL ABILITY; and straightway took his journey" — trust
        proportioned, then real departure and real freedom.
  v16-17 the five and the two both "went and TRADED" and DOUBLED what they
        held. The narration adds: 'neither one played it safe.'
  v18   the one-talent servant "DIGGED IN THE EARTH, and HID his lord's
        money" — a night burial.
  v19-23 the reckoning: to BOTH faithful servants the identical words —
        "Well done, thou good and faithful servant ... ENTER THOU INTO THE
        JOY OF THY LORD." The master's joy is the row's emotional centre:
        he shares his own joy, he welcomes them deeper in.
  v24-25 "I KNEW THEE THAT THOU ART AN HARD MAN ... I WAS AFRAID" — the
        buried talent came from a LIE about the master's character. The
        narration hammers it (b20-b24): he was WRONG about him; God is not
        the hard man that servant imagined. So the MASTER is painted warm,
        generous and grieved — never cold, never cruel — in every beat
        including the reckoning.
  v30 (outer darkness) is NOT in this narration — no punishment beat is
        painted; the row ends on the master's longing to say 'well done.'

TIME OF DAY: the Olivet frame beat is deep blue dusk. The parable runs:
bright MORNING for the entrusting and departure; varied working DAYLIGHT
for the trading beats; full NIGHT for the burial (v18 — fear works in the
dark; correct, not a defect); clear DAY for the homecoming; warm LAMPLIT
EVENING for the reckoning hall and the feast of shared joy.

CONTENT-CARE: row 32 has no flag in §3. The fearful servant is never
mocked and never punished on screen.

CHANGING CONDITION (kept OUT of the locks): the money-bags — five, two,
one; clean or dirt-crusted; doubled into ten and four — move beat to beat.
The fearful servant's bag is the only one that ever appears dirty.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "MASTER": (
        "MASTER LOCK: the master is the same man in every shot — early "
        "fifties, broad-shouldered and open-faced, with a full dark beard "
        "streaked grey at the chin, warm creased eyes and an easy generous "
        "bearing. He wears a fine DEEP FOREST-GREEN wool robe with a DARK "
        "GOLD-THREADED border over a DARK BROWN under-tunic, and a wide "
        "leather travel belt (never cream, never white). His face is shown "
        "clearly and it defaults to warmth — even his grief is kind."
    ),
    "SERV5": (
        "FIVE-TALENT SERVANT LOCK: the first servant is the same man in "
        "every shot — about thirty-five, quick-eyed and energetic, with a "
        "short black beard and a ready grin. He wears a DEEP RUSSET tunic "
        "with a dark leather belt (never cream, never white). His face is "
        "shown clearly."
    ),
    "SERV2": (
        "TWO-TALENT SERVANT LOCK: the second servant is the same man in "
        "every shot — about forty-five, steady and thickset, with a heavy "
        "brown beard and calm deliberate hands. He wears a DARK OLIVE "
        "tunic with a rope belt (never cream, never white). His face is "
        "shown clearly."
    ),
    "SERV1": (
        "ONE-TALENT SERVANT LOCK: the third servant is the same man in "
        "every shot — late twenties, slight and tense, with a thin dark "
        "beard, hunched wary shoulders and eyes that never quite settle. "
        "He wears a DARK SLATE-GREY tunic with a frayed rope belt (never "
        "cream, never white). His face is shown clearly — anxious, never "
        "villainous."
    ),
    "ESTATE": (
        "ESTATE LOCK: the master's estate — a paved courtyard behind a "
        "stone gateway arch, a long colonnaded porch, a great hall with a "
        "heavy wooden table and iron-fitted strongbox, cypress trees along "
        "the outer wall, and an old olive orchard sloping away behind the "
        "buildings. The same arch, porch, hall and orchard throughout."
    ),
    "TRADE": (
        "TRADE LOCK: the town of the trading beats — a busy market street "
        "of stalls and awnings, a merchants' colonnade with scales and "
        "ledger tables, and a caravan yard where laden donkeys and bales "
        "stand for loading. Traders wear SATURATED DEEP earth colours "
        "(never cream, never white; only Jesus wears cream)."
    ),
    "OLIVET": (
        "MOUNT OF OLIVES LOCK: the western slope of the Mount of Olives "
        "at dusk — dry grass and grey stone between old gnarled olive "
        "trees, and across the dark Kidron valley the walls of Jerusalem "
        "with small warm lamps being lit along them under a deep blue "
        "evening sky."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r032-b01", "out": "s01-for-the-kingdom-of-heaven.jpeg", "seg": "j14",
        "window": "0.28-9.01", "wide": True, "jesus": False, "ref": False,
        "locks": ["MASTER", "SERV5", "SERV2", "SERV1", "ESTATE"],
        "narration": (
            "For the kingdom of heaven is as a man travelling into a far "
            "country, who called his own servants, and delivered unto them his "
            "goods."
        ),
        "must_show": "SCRIPTURE-EXACT: the entrusting — the master at his great hall table with the strongbox open, the three servants called in before him, heavy money-bags being set out.",
        "must_not_show": "no halo, glare or rim-light; the master's face is warm and confiding — this is trust, not a test set as a trap.",
        "scene": (
            "In the great hall in bright morning light the master "
            "stands at the heavy wooden table with the iron-fitted "
            "strongbox open before him, setting out fat leather "
            "money-bags in a row — and the three servants stand called "
            "in close across the table, the quick russet-clad one "
            "leaning eagerly in, the steady olive-clad one attentive, "
            "the slight grey-clad one at the end with his shoulders "
            "already tight. The master is looking at them with open "
            "confiding warmth. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r032-b02", "out": "s02-the-servant-with-two-bags.jpeg", "seg": "n4",
        "window": "39.89-43.81", "wide": True, "jesus": False, "ref": False,
        "locks": ["SERV2", "TRADE"],
        "narration": "The servant with two bags did the same, and doubled his as well.",
        "must_show": "the second servant's steady venture — at the merchants' colonnade closing a deal over bales, his two bags become a growing stack of goods and coin.",
        "must_not_show": "no halo, glare or rim-light; steadier and smaller-scale than the first servant's trading, but just as real — different style, same faithfulness.",
        "scene": (
            "Under the merchants' colonnade in plain working daylight "
            "the thickset olive-clad servant clasps forearms with a "
            "cloth trader over a table of folded woollen bales, his "
            "brass scales still swinging from the weighing — and at "
            "his elbow sit his two leather bags with a third pile of "
            "counted coins growing on the table beside them, gains "
            "made the slow, steady way. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r032-b03", "out": "s03-jesus-told-a-story-about.jpeg", "seg": "n1",
        "window": "10.08-16.58", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET"],
        "narration": (
            "Jesus told a story about a wealthy man who, before a long journey, "
            "entrusted his servants with his own fortune."
        ),
        "must_show": "the Olivet frame — from behind Jesus's shoulder, the listening disciples' dusk-lit faces, Jerusalem's first lamps across the dark valley beyond them.",
        "must_not_show": "no halo, glare or rim-light on Jesus; his shoulder and profile-edge only at the frame's side — the disciples' faces carry the light.",
        "scene": (
            "From just behind Jesus's shoulder on the dusk hillside: "
            "his profile a soft dark edge at the frame's side, and "
            "beyond it the faces of the four disciples ranged on the "
            "dry grass, lit faint blue-gold by the last sky, listening "
            "hard — while far behind them across the black valley the "
            "small warm lamps of Jerusalem prick on one by one along "
            "the walls. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r032-b04", "out": "s04-to-one-he-gave-five.jpeg", "seg": "n1",
        "window": "16.58-25.17", "wide": True, "jesus": False, "ref": False,
        "locks": ["MASTER", "SERV5", "SERV2", "SERV1", "ESTATE"],
        "narration": (
            "To one he gave five bags of silver, to another two, and to another "
            "one, each according to what he could handle."
        ),
        "must_show": "SCRIPTURE-EXACT: the proportion made visible — five bags in the first servant's arms, two in the second's, ONE held out to the third; the count must read at a glance.",
        "must_not_show": "no halo, glare or rim-light; the single bag is given with the SAME warmth as the five — no slight in the master's face.",
        "scene": (
            "Along the hall table the portions stand divided: the "
            "russet-clad servant already hugs an armload of FIVE fat "
            "leather bags, the olive-clad one holds his TWO stacked "
            "steady against his chest — and the master is placing the "
            "last single bag into the grey-clad servant's hesitant "
            "hands with both of his own, bending slightly to catch the "
            "young man's eye with unmistakable warmth as he gives it. "
            "Morning light down the hall. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r032-b05", "out": "s05-it-was-a-staggering-amount.jpeg", "seg": "n2",
        "window": "25.80-27.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["ESTATE"],
        "narration": "It was a staggering amount of trust.",
        "must_show": "a close shot of one opened bag — packed solid with ancient silver — beside the estate's iron keys lying surrendered on the table wood.",
        "must_not_show": "no halo, glare or rim-light; old dull silver, never bright modern coinage; the keys beside the bag say the whole house is handed over.",
        "scene": (
            "A close shot on the hall table in morning light: one "
            "leather bag untied and tipped open, packed solid with "
            "rough-struck ancient silver to its mouth — and lying "
            "surrendered on the scarred wood beside it, the estate's "
            "ring of heavy iron keys, left behind for other hands. "
            "Trust, in metal. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r032-b06", "out": "s06-he-handed-his-wealth-to.jpeg", "seg": "n2",
        "window": "27.76-31.65", "wide": True, "jesus": False, "ref": False,
        "locks": ["MASTER", "SERV5", "SERV2", "SERV1", "ESTATE"],
        "narration": "He handed his wealth to his servants and left them free to use it.",
        "must_show": "SCRIPTURE-EXACT: the departure — the master riding out through the gateway arch with his small travelling party, waving back easily; the three servants watching from the porch with the bags in their arms.",
        "must_not_show": "no halo, glare or rim-light; the master does NOT look back anxiously — the easy wave is the freedom he leaves them.",
        "scene": (
            "Through the stone gateway arch the master rides out on a "
            "laden mule with two pack-servants walking ahead, turning "
            "in the saddle to lift one easy unworried hand in farewell "
            "— while behind him on the colonnaded porch the three "
            "servants stand watching him go, bags held in their arms, "
            "the quick one already turning toward the gate, the "
            "grey-clad one holding his single bag like something that "
            "might bite. Bright morning over the cypress trees. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r032-b07", "out": "s07-the-servant-with-five-bags.jpeg", "seg": "n3",
        "window": "32.26-39.27", "wide": True, "jesus": False, "ref": False,
        "locks": ["SERV5", "TRADE"],
        "narration": (
            "The servant with five bags went straight to work, trading and "
            "investing, and doubled everything he had been given."
        ),
        "must_show": "SCRIPTURE-EXACT: the first servant in full trade — directing the loading of a caravan in the yard, coins changing hands, energy everywhere around him.",
        "must_not_show": "no halo, glare or rim-light; industry and risk in motion — goods, animals, deals all at once; his grin in the middle of it.",
        "scene": (
            "The caravan yard at busy midday: the quick russet-clad "
            "servant stands at its centre directing everything at once "
            "— one hand paying silver into a drover's palm, the other "
            "arm waving a loaded donkey into the departing line, bales "
            "and oil jars stacked around his feet, his short black "
            "beard split by a working grin. The whole yard turns "
            "around his energy. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r032-b08", "out": "s08-neither-one-played-it-safe.jpeg", "seg": "n4",
        "window": "43.81-46.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["SERV5", "TRADE"],
        "narration": "Neither one played it safe.",
        "must_show": "risk made visible — a close shot of the first servant's hand releasing a whole bag of silver across a deal table into a shipowner's waiting palm; committed, no way back.",
        "must_not_show": "no halo, glare or rim-light; the WHOLE bag leaves his hand — full commitment, not a cautious coin.",
        "scene": (
            "A close shot over a deal table in the colonnade light: "
            "the russet-clad servant's hand caught in the instant of "
            "releasing an entire tied bag of silver into the broad "
            "waiting palm of a weathered shipowner, the bag still in "
            "the air between grips — while on the table under their "
            "hands lies a merchant's tally of a cargo not yet sailed. "
            "Everything ventured. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r032-b09", "out": "s09-they-took-what-they-were.jpeg", "seg": "n4",
        "window": "46.09-49.41", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "They took what they were trusted with and made it grow.",
        "must_show": "the growth itself — a close shot of an open chest where doubled bags now stand in two rows, ten and four, plainly more than was given.",
        "must_not_show": "no halo, glare or rim-light; the doubling must COUNT at a glance — two neat rows, visibly twice the trust.",
        "scene": (
            "A close shot into an open iron-fitted chest in warm "
            "light: the leather money-bags stand packed in two neat "
            "rows — ten fat bags along one side, four along the other "
            "— each tied and full, twice what left the master's table, "
            "with a wax tablet of careful reckonings laid on top. "
            "Increase, counted and honest. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r032-b10", "out": "s10-so-he-dug-a-hole.jpeg", "seg": "n5",
        "window": "52.23-57.43", "wide": True, "jesus": False, "ref": False,
        "locks": ["SERV1", "ESTATE"],
        "narration": (
            "So he dug a hole in the ground, buried the silver, and did nothing "
            "with it at all."
        ),
        "must_show": "SCRIPTURE-EXACT: the burial — night in the olive orchard, the servant knee-deep at his hole lowering the bag in, spade beside him, checking over his shoulder.",
        "must_not_show": "no halo, glare or rim-light; full night is correct (fear works in the dark); furtive, sad, alone.",
        "scene": (
            "Deep night in the old olive orchard behind the estate, a "
            "low moon through the branches: the slight grey-clad "
            "servant kneels at the edge of a fresh knee-deep hole, "
            "lowering his single leather bag down into it with both "
            "hands, his spade stuck upright in the spoil heap beside "
            "him — and his face is turned back over his shoulder "
            "toward the dark buildings, wary of being seen doing "
            "nothing. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r032-b11", "out": "s11-when-the-master-came-home.jpeg", "seg": "n6",
        "window": "58.03-62.43", "wide": True, "jesus": False, "ref": False,
        "locks": ["MASTER", "SERV5", "SERV2", "ESTATE"],
        "narration": (
            "When the master came home, the first two servants showed him what "
            "they had made."
        ),
        "must_show": "SCRIPTURE-EXACT: the homecoming reckoning — the master back at his hall table, the two faithful servants presenting their doubled rows of bags, faces bright.",
        "must_not_show": "no halo, glare or rim-light; the two servants are EAGER to show — pride of faithful work, not fear of audit.",
        "scene": (
            "In the great hall by warm late-day light the master, "
            "travel cloak still over one shoulder, leans on the heavy "
            "table where the two servants are laying out their "
            "reckonings — the russet-clad one spreading his ten bags "
            "in a proud row, the olive-clad one setting his four down "
            "two at a time — both faces bright and eager as boys "
            "showing a father their catch. The master's eyes are "
            "already warming. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r032-b12", "out": "s12-and-he-was-overjoyed.jpeg", "seg": "n6",
        "window": "62.43-64.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["MASTER"],
        "narration": "And he was overjoyed.",
        "must_show": "a close portrait of the master's face breaking into full open joy — the warmest face in the row.",
        "must_not_show": "no halo, glare or rim-light; joy at THEM, not at the money — his eyes are on people, not bags.",
        "scene": (
            "A close portrait of the master's broad face in the warm "
            "hall light, caught at the instant of breaking open — "
            "creased eyes bright and wet, the grey-streaked beard "
            "parting over a laugh already coming, his gaze fixed past "
            "the camera on the men themselves and not once dropping "
            "to the silver. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r032-b13", "out": "s13-well-done-thou-good-and.jpeg", "seg": "j1",
        "window": "65.03-76.60", "wide": True, "jesus": False, "ref": False,
        "locks": ["MASTER", "SERV5", "SERV2", "ESTATE"],
        "narration": (
            "Well done, thou good and faithful servant: thou hast been faithful "
            "over a few things, I will make thee ruler over many things: enter "
            "thou into the joy of thy lord."
        ),
        "must_show": "SCRIPTURE-EXACT: the words embodied — the master gripping the first servant by both shoulders face to face, the second already being drawn in under his arm toward the lamplit inner doorway.",
        "must_not_show": "no halo, glare or rim-light; physical, fatherly delight — hands on shoulders, an arm around a back, a door opening INWARD to joy.",
        "scene": (
            "In the hall the master grips the russet-clad servant by "
            "both shoulders at arm's length, beaming full into his "
            "face as he says it — and his other arm is already "
            "reaching to gather the olive-clad servant in against his "
            "side, turning them both toward the inner doorway where "
            "warm lamplight and the sounds of a laid feast wait. The "
            "bags stand forgotten on the table behind them. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r032-b14", "out": "s14-but-the-servant-with-one.jpeg", "seg": "n5",
        "window": "50.05-52.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["SERV1"],
        "narration": "But the servant with one bag was afraid.",
        "must_show": "the fear itself — a close portrait of the third servant clutching his single bag to his chest with both arms, eyes wide and unsettled.",
        "must_not_show": "no halo, glare or rim-light; fear painted with sympathy — a young man out of his depth, not a fool to be laughed at.",
        "scene": (
            "A close portrait in fading evening light: the slight "
            "grey-clad servant stands with his single leather bag "
            "hugged tight to his chest in both arms like a child "
            "carried through a crowd, his thin-bearded face tight, "
            "eyes wide and moving, shoulders hunched up toward his "
            "ears — a man holding a trust he can only feel as a "
            "threat. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r032-b15", "out": "s15-he-did-not-just-reward.jpeg", "seg": "n7",
        "window": "77.67-83.80", "wide": True, "jesus": False, "ref": False,
        "locks": ["MASTER", "SERV5", "SERV2", "ESTATE"],
        "narration": (
            "He did not just reward them, he shared his own joy with them, and "
            "welcomed them deeper in."
        ),
        "must_show": "the shared table — master and both servants SEATED TOGETHER at the feast, servants in the seats of honour beside him, one table, one joy.",
        "must_not_show": "no halo, glare or rim-light; no serving-line between them — the servants SIT WITH him as companions; that is the whole beat.",
        "scene": (
            "In the lamplit inner room the feast is laid and the "
            "three men sit together at one table — the master at its "
            "head with a servant seated close on either hand in the "
            "places of honour, pouring the wine HIMSELF into the "
            "russet-clad man's cup while the olive-clad one laughs at "
            "something just said — bread broken, lamps warm, no line "
            "left anywhere between lord and servants. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r032-b16", "out": "s16-then-the-last-servant-came.jpeg", "seg": "n8",
        "window": "84.45-89.53", "wide": True, "jesus": False, "ref": False,
        "locks": ["MASTER", "SERV1", "ESTATE"],
        "narration": (
            "Then the last servant came, dug up his one buried bag, and handed "
            "it back untouched."
        ),
        "must_show": "SCRIPTURE-EXACT: the return of the buried thing — the servant setting the dirt-crusted bag on the clean table before the master, soil still falling from it.",
        "must_not_show": "no halo, glare or rim-light; the bag is visibly EARTH-STAINED against the clean table — the only dirty thing in the hall.",
        "scene": (
            "At the great hall table the grey-clad servant sets down "
            "his single bag before the seated master — the leather "
            "dark and crusted with dried orchard earth, a little "
            "soil crumbling off onto the clean scarred wood as it "
            "lands — and steps back with his eyes down and his hands "
            "working at his frayed belt. The master looks from the "
            "dirty bag up to the man, not yet speaking. Warm lamplight. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r032-b17", "out": "s17-lord-i-knew-thee-that.jpeg", "seg": "j24",
        "window": "92.67-100.89", "wide": True, "jesus": False, "ref": False,
        "locks": ["MASTER", "SERV1", "ESTATE"],
        "narration": (
            "Lord, I knew thee that thou art an hard man, reaping where thou "
            "hast not sown, and strawing where thou hast not strawed:"
        ),
        "must_show": "SCRIPTURE-EXACT: the accusation — the servant defending himself with sharp warding gestures, and the master's face showing not anger but open HURT at the description.",
        "must_not_show": "no halo, glare or rim-light; the master hears himself called hard and it WOUNDS him — grief in his face, never the coldness the servant describes.",
        "scene": (
            "The grey-clad servant stands rigid before the table, one "
            "hand flung up palm-out between himself and his master, "
            "the accusation coming fast and defensive — and across "
            "the table the master has gone very still, his warm "
            "creased face open with plain hurt, the face of a "
            "generous man hearing what a frightened one believed of "
            "him all along. The lamplight holds them both. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r032-b18", "out": "s18-and-listen-to-why-he.jpeg", "seg": "n8",
        "window": "89.53-92.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["ESTATE"],
        "narration": "And listen to why he had buried it.",
        "must_show": "a close still shot of the dirt-crusted bag alone on the clean table — untouched, unopened, exactly as it went into the ground.",
        "must_not_show": "no halo, glare or rim-light; nothing else in frame — the returned, wasted trust as a still life.",
        "scene": (
            "A close still shot in lamplight: the single leather bag "
            "alone on the great clean table, its sides caked with "
            "dried pale orchard earth, the tie-cord still in the "
            "same knot the master tied — unopened, untraded, "
            "untouched — with a thin scatter of crumbled soil on the "
            "wood around it. A trust returned exactly as given, which "
            "is to say wasted. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r032-b19", "out": "s19-and-i-was-afraid-and.jpeg", "seg": "j2",
        "window": "101.91-109.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["SERV1"],
        "narration": (
            "And I was afraid, and went and hid thy talent in the earth: lo, "
            "there thou hast that is thine."
        ),
        "must_show": "SCRIPTURE-EXACT: the confession — a close shot of the servant's face as the defense collapses into the truth: I was afraid; shame and fear together.",
        "must_not_show": "no halo, glare or rim-light; the face asks for pity and gets the viewer's — sympathy, not contempt.",
        "scene": (
            "A close portrait of the grey-clad servant in the "
            "lamplight, the defensive sharpness gone out of his thin "
            "face mid-sentence, leaving only the truth underneath — "
            "eyes dropped, mouth unsteady, the look of a young man "
            "admitting the fear that has run his whole life — his "
            "empty hands turned half-open at his sides. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r032-b20", "out": "s20-there-it-is-he-buried.jpeg", "seg": "n9",
        "window": "110.42-115.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["SERV1", "ESTATE"],
        "narration": (
            "There it is. He buried the gift because he believed his master was "
            "harsh and cruel."
        ),
        "must_show": "the lie at work — back in the night orchard, close on the servant's fearful face as he pats the earth down over the hole, burying trust because of what he wrongly believed.",
        "must_not_show": "no halo, glare or rim-light; night again is correct; his fear is real on his face — and aimed at a master who never earned it.",
        "scene": (
            "Close in the moonlit orchard night: the servant's thin "
            "face bent low over the refilled hole as his two hands "
            "pat the last earth flat, his eyes flicking up under his "
            "brows toward the dark shape of the great house between "
            "the olive trunks — burying silver the way other men bury "
            "a danger, all of it built on a face he has imagined "
            "wrongly. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r032-b21", "out": "s21-he-was-wrong-about-him.jpeg", "seg": "n9",
        "window": "115.34-123.38", "wide": True, "jesus": False, "ref": False,
        "locks": ["MASTER", "SERV1", "ESTATE"],
        "narration": (
            "He was wrong about him. His fear was built on a lie about who his "
            "master really was, and that lie cost him everything."
        ),
        "must_show": "the two truths facing each other — the master risen and come AROUND the table to stand near the servant, grief and warmth in him even now; the servant unable to lift his eyes to see it.",
        "must_not_show": "no halo, glare or rim-light; the master comes CLOSER, not further — even his sorrow moves toward the man; the tragedy is the servant cannot see the face in front of him.",
        "scene": (
            "The master has risen and come around the great table to "
            "stand close before the grey-clad servant, his warm "
            "grieved face bent toward him, one hand half-lifted as if "
            "it would rest on the young man's shoulder — and the "
            "servant stands with his head down and his eyes shut "
            "tight, unable even now to look up at the kindest face "
            "in the room. The dirty bag sits between them on the "
            "table's edge. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r032-b22", "out": "s22-that-is-the-real-tragedy.jpeg", "seg": "n10",
        "window": "124.01-126.33", "wide": False, "jesus": False, "ref": False,
        "locks": ["ESTATE"],
        "narration": "That is the real tragedy of the story.",
        "must_show": "the empty aftermath — the hall doorway to the lamplit feast standing open and warm, and the dirty bag still on the table in the foreground, its owner gone from the frame.",
        "must_not_show": "no halo, glare or rim-light; no one in frame — an open warm door that someone chose not to walk through.",
        "scene": (
            "A still frame in the quiet hall: in the foreground the "
            "earth-crusted bag sits abandoned on the table's corner, "
            "and beyond it the inner doorway stands open, deep warm "
            "lamplight and the soft noise of the feast spilling "
            "through it into the empty room — a door that was open "
            "the whole time, and a gift that never went in. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r032-b23", "out": "s23-not-that-he-had-little.jpeg", "seg": "n10",
        "window": "126.33-132.82", "wide": False, "jesus": False, "ref": False,
        "locks": ["MASTER"],
        "narration": (
            "Not that he had little, but that he so badly misjudged the heart "
            "of the one who trusted him."
        ),
        "must_show": "the misjudged heart — a close portrait of the master alone, the joy of the feast still on him but his eyes grieving toward the outer door.",
        "must_not_show": "no halo, glare or rim-light; both truths in one face — a man made for rejoicing, grieving over one who never knew it.",
        "scene": (
            "A close portrait of the master in the doorway light "
            "between feast and hall: the warmth of the celebration "
            "still lives in his broad creased face, but his eyes have "
            "gone past the camera toward the dark outer door, "
            "grieving quietly for the one servant who read that face "
            "wrong his whole life. The lamplight is gentle on the "
            "grey in his beard. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r032-b24", "out": "s24-god-is-not-the-hard.jpeg", "seg": "n10",
        "window": "132.82-136.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["MASTER", "ESTATE"],
        "narration": "God is not the hard man that servant imagined.",
        "must_show": "the refutation in one image — the master at his open strongbox freely setting MORE bags into a young house-servant's arms, generosity as his resting state.",
        "must_not_show": "no halo, glare or rim-light; giving is his DEFAULT — the frame catches him mid-generosity with no occasion required.",
        "scene": (
            "By the open iron-fitted strongbox in warm lamplight the "
            "master loads leather bags into the arms of a surprised "
            "young house-servant — two already stacked, a third "
            "being set on top — laughing at the boy's widening eyes, "
            "giving the way other men breathe. The hall behind him "
            "still carries the feast's warmth. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r032-b25", "out": "s25-he-trusts-you-with-something.jpeg", "seg": "n10",
        "window": "136.13-143.42", "wide": True, "jesus": False, "ref": False,
        "locks": ["MASTER", "ESTATE"],
        "narration": (
            "He trusts you with something real, and he is longing to say to "
            "you, well done, and to share his joy."
        ),
        "must_show": "the closing image — the master standing in the open feast doorway with both arms spread wide toward the camera itself, the welcome aimed straight out of the frame at the viewer.",
        "must_not_show": "no halo, glare or rim-light; the invitation is to the VIEWER — arms open, face alight, the feast warm behind him, nothing between him and the camera.",
        "scene": (
            "The master stands framed in the open inner doorway with "
            "the golden lamplit feast alive behind him, and both his "
            "arms are spread full wide toward the camera itself, his "
            "warm creased face alight with the exact look he gave his "
            "faithful servants — 'well done' already forming on it — "
            "with nothing and no one standing between him and the "
            "viewer's own place in the dark hall. Every figure has "
            "two arms, two hands and one head."
        ),
    },
]
