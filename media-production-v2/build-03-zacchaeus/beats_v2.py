#!/usr/bin/env python3
"""V2 beat map — row 3, build-03-zacchaeus (Luke 19:1-10).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE (STORY-COVERAGE-LAW): 26 pictures over 222s, against V1's 11. That is above
the 10-20 band, and the runtime is why: 222s at 26 pictures is 8.5s of narration per
picture, which is LESS dense than row 2 (158s / 24 = 6.6s). The band assumes a
~100-150s story; this one is 40% longer than row 2 and every added picture answers a
beat the narration actually states. The narration decided the count, not a quota.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Luke 19 KJV):
  v1-2   Jesus entered and PASSED THROUGH Jericho; Zacchaeus was CHIEF among the
         publicans, and he was RICH. Chief = he ran the office, others under him.
  v3     he sought to see Jesus WHO HE WAS; and COULD NOT FOR THE PRESS, BECAUSE
         HE WAS LITTLE OF STATURE. The crowd is a physical wall; his shortness is
         stated by scripture, so it must READ in the pictures — he is visibly the
         smallest adult in every crowd frame.
  v4     he RAN BEFORE, and climbed up into a SYCOMORE TREE to see him: FOR HE WAS
         TO PASS THAT WAY. He gets ahead of the route first, then climbs.
  v5     Jesus LOOKED UP, and SAW him, and said, Zacchaeus, MAKE HASTE, and come
         down; for TO DAY I MUST ABIDE AT THY HOUSE. Jesus speaks first, uses his
         NAME, and invites himself — before any repentance.
  v6     he MADE HASTE, and came down, and received him JOYFULLY.
  v7     they ALL MURMURED, That he was gone to be guest with a man that is a sinner.
  v8     Zacchaeus STOOD, and said unto the LORD; Behold, LORD, the HALF of my goods
         I give to the poor; and if I have taken ANY THING from any man by FALSE
         ACCUSATION, I restore him FOURFOLD. He stands — this is public, at table.
  v9     This day is SALVATION come to this house, forsomuch as HE ALSO IS A SON OF
         ABRAHAM.
  v10    For the SON OF MAN IS COME TO SEEK AND TO SAVE that which was lost.

ORDER OF EVENTS THAT MUST NOT BE INVERTED: the giving in v8 comes AFTER the
invitation in v5 and after Jesus is already in the house. Never show Zacchaeus
giving money away before Jesus calls him — that reverses the entire meaning of the
story ("Jesus moves first", n5).

CONTENT-CARE: row 3 is not in the §3 flag table = GREEN. Restraint applied anyway:
the crowd's contempt is shown as turned backs, shut doors and hard faces — never
mockery played for comedy, and never a man being jostled or struck.

TIME-OF-DAY ARC (self-consistent; Luke states none):
  tax office / the town's contempt = hard bright morning · the crowd and the run
  and the tree = full midday sun · the call and coming down = midday · walking to
  the house = late afternoon · the table, the vow, salvation = warm evening
  lamplight · closing "seek and save" = dusk over Jericho.

CAMERA LAW (row 2 paid for this): every travelling / watching / arriving beat states
where the lens is and which way the figure faces. Without it the model composes
hero-shots facing the camera and the geography inverts.
"""

OUTPUT_ASSET_DIR = "assets-realistic-v3"
OUTPUT_VIDEO_NAME = "luke-19_zacchaeus-realistic-v3.mp4"

LOCKS = {
    # Zacchaeus's clothing does NOT change until the table, and even there it only
    # gets disarrayed, so his lock CAN carry his garment — unlike the prodigal.
    # His SHORTNESS is scripture (v3) and is therefore in the lock, stated as a
    # comparison so it survives into every crowd frame.
    # HEIGHT BUG, fixed 2026-07-30 after Cameron: *"the 03 zacchaeus story that flow
    # made was trash because it kept making zacchaeus too short and everything weird."*
    # He is right and it was my prompt, not Flow. v1 of this lock said he was "a full
    # head shorter than every other adult around him ... always the smallest grown man
    # in the frame" — inside the LOCK, so it applied to close-ups and solo shots where
    # there is nobody to be shorter THAN. The model resolved "always the smallest" the
    # only way it could: by making him dwarfish in every frame.
    # SAME LESSON AS THE PRODIGAL'S CLOTHING: a lock may only carry what is true in
    # EVERY frame. Height is a property of him (short, slight); height RELATIVE TO A
    # CROWD is a fact about certain frames, so it now lives in those beats only —
    # b07 (v3, the crowd as a wall), b08 (nobody makes room) and b18 (the welcome).
    "ZAC": (
        "ZACCHAEUS LOCK: Zacchaeus is the same man in every shot — a Middle Eastern "
        "Jewish man of about forty-five, a SHORT and slightly built man of small "
        "stature with normal adult proportions. Neatly trimmed dark beard going grey at the "
        "chin, receding dark hair, quick intelligent eyes, a soft well-fed face. He "
        "wears an EXPENSIVE DEEP WINE-BURGUNDY wool robe with a woven gold-thread "
        "border and a wide embroidered sash, fine leather sandals and a heavy gold "
        "ring — visibly the richest clothing in any crowd, and never cream, never "
        "off-white, never pale. His face is shown clearly."
    ),
    # A setting lock NEVER names a character (the STRAY-JESUS defect, row 1).
    "JERICHO": (
        "JERICHO LOCK: a prosperous walled town in the Jordan valley — warm "
        "honey-coloured stone streets, date palms and balsam gardens, dusty paving, "
        "flat roofs, an arched gateway, dry hills far beyond. The townspeople are "
        "ordinary working men and women in SATURATED DEEP earth colours: dark "
        "chocolate brown, deep russet, burnt ochre, dark olive and dusty indigo "
        "wool, every garment plainly DARKER than the sunlit stone behind them. No "
        "villager wears cream, off-white, ivory or any pale near-white cloth."
    ),
    "SYCOMORE": (
        "SYCOMORE LOCK: a broad old sycomore fig tree standing beside the road — a "
        "thick pale grey-brown trunk that divides low into heavy horizontal limbs "
        "wide enough for a man to sit on, dense dark-green leathery leaves, clusters "
        "of small figs on the bark, its low branches within reach of the ground."
    ),
    "HOUSE": (
        "HOUSE LOCK: Zacchaeus's own house — the largest and finest in the street, "
        "dressed stone with a carved lintel and a heavy studded door, inside a warm "
        "lamplit hall with a long low table, imported pottery, patterned cushions "
        "and hanging oil lamps, wealth plainly on display but not gaudy. The "
        "household servants wear plain dark earth-brown and grey-brown wool; no one "
        "in the household wears cream, off-white or any pale near-white cloth."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r003-b01", "out": "s01-the-tax-office.jpeg", "seg": "n0 p1",
        "window": "0.28-10.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["ZAC", "JERICHO"],
        "narration": "In Jericho there lived a man named Zacchaeus.",
        "must_show": "v1-2 — Zacchaeus at work in the Jericho tax house, plainly the man in charge.",
        "must_not_show": "no Roman soldier yet; no violence; he is not yet sympathetic.",
        "scene": (
            "In hard bright morning light in the Jericho tax house, Zacchaeus sits "
            "behind a heavy wooden table stacked with coin, weights and rolled "
            "ledgers, one hand flat on an open ledger, taking a payment from a "
            "weathered farmer who stands before him with his eyes down. Zacchaeus "
            "is calm and entirely at ease; he is clearly the man in charge of the "
            "room. Every figure has two arms, two hands of five fingers each and "
            "one head."
        ),
    },
    {
        "id": "v2-r003-b02", "out": "s02-chief-and-rich.jpeg", "seg": "n0 p2",
        "window": "10.0-20.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["ZAC", "JERICHO"],
        "narration": ("Zacchaeus ran the whole tax office in Jericho. And he was "
                      "rich."),
        "must_show": "v2 CHIEF among the publicans and RICH — other collectors working under him; his wealth visible.",
        "must_not_show": "he is not gloating; this is ordinary business for him.",
        "scene": (
            "A wider view of the same tax house in hard morning light: two younger "
            "tax collectors in plain dark brown wool work at their own smaller "
            "tables counting coin into stacks, and Zacchaeus stands among them "
            "looking over one man's ledger, the shortest man in the room by a full "
            "head and unmistakably the master of it. Behind him an iron-bound "
            "strongbox stands open on a shelf, heavy with silver. Exactly three "
            "people are in the frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b03", "out": "s03-working-for-rome.jpeg", "seg": "n1 p1",
        "window": "21.0-28.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["ZAC", "JERICHO"],
        "narration": ("Tax collectors worked for Rome — the empire occupying their "
                      "own people."),
        "must_show": "the collaboration made visible — a Roman soldier standing at his shoulder in the street.",
        "must_not_show": "no one is being struck or dragged; the menace is presence, not violence.",
        "scene": (
            "In the sunlit Jericho street a Roman soldier in iron and leather stands "
            "at ease just behind Zacchaeus's shoulder while Zacchaeus takes coins "
            "from a poor woman's hand into his palm, her basket of figs at her feet. "
            "Zacchaeus does not look at her face. The soldier's presence is the "
            "reason she is paying. Exactly three people are in the frame; each has "
            "two arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r003-b04", "out": "s04-no-one-greeted-him.jpeg", "seg": "n1 p2",
        "window": "28.0-34.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["ZAC", "JERICHO"],
        "narration": "So to his neighbors, Zacchaeus wasn't just a cheat. He was a traitor. No one greeted him.",
        "must_show": "the whole street turning away from him at once — the town's verdict.",
        "must_not_show": "nobody shouts or throws anything; it is colder than that.",
        "scene": (
            "Zacchaeus walks alone down the middle of the crowded Jericho market "
            "street in bright morning light, and everyone he passes has turned "
            "away — a woman lifting her basket and stepping behind a stall, two men "
            "breaking off their conversation to face the wall, a shopkeeper pulling "
            "his door half shut. A clear ring of empty dust travels with him. His "
            "chin is up and his face is carefully blank. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b05", "out": "s05-no-table.jpeg", "seg": "n1 p3",
        "window": "34.0-39.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["ZAC", "HOUSE"],
        "narration": "No one wanted him at their table.",
        "must_show": "the cost of it — the richest table in Jericho with exactly one man at it.",
        "must_not_show": "no self-pity performed; he simply eats alone.",
        "scene": (
            "Inside his own fine house, Zacchaeus sits alone at the head of a long "
            "table laid with good food and imported pottery, in the flat light of "
            "midday through a high window. Every other place along the table is "
            "empty, the cushions undented. He eats without looking up. Exactly one "
            "person is in the frame, with two arms, two hands of five fingers each "
            "and one head."
        ),
    },
    {
        "id": "v2-r003-b06", "out": "s06-the-city-pressed-in.jpeg", "seg": "n2 p1",
        "window": "40.34-46.0", "wide": True, "jesus": True, "ref": REF,
        "locks": ["JERICHO"],
        "narration": "When Jesus came to Jericho, the whole city pressed into the street to see him.",
        "must_show": "v1 — Jesus moving through a packed Jericho street, every face turned toward him.",
        "must_not_show": "no halo, glow or rim-light; Zacchaeus is NOT in this frame yet.",
        "scene": (
            "The Jericho street is packed wall to wall with townspeople in the hard "
            "light of midday, and Jesus is walking through the middle of them, "
            "unhurried, at their level, speaking with the people nearest him as he "
            "goes. Every face in the street is turned toward him and the whole crowd "
            "leans his way. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b07", "out": "s07-little-of-stature.jpeg", "seg": "n2 p2",
        "window": "46.0-51.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["ZAC", "JERICHO"],
        "narration": ("And Zacchaeus had a problem. He was a short man — the "
                      "scripture goes out of its way to mention it."),
        "must_show": "v3 — his shortness as the obstacle; he is behind a wall of taller backs.",
        "must_not_show": "he is not being mocked here; nobody has noticed him at all.",
        "scene": (
            "SHOT FROM BEHIND AND ABOVE ZACCHAEUS, looking over his shoulder at a "
            "solid wall of taller backs and shoulders blocking the street ahead of "
            "him. He is stranded at the back of the crowd in his deep wine-burgundy "
            "robe, up on the balls of his feet with one hand on a stranger's "
            "shoulder for balance, straining to see past them, and the tallest of "
            "them stand a full head above him. Hard midday sun. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b08", "out": "s08-not-one-made-room.jpeg", "seg": "n2 p3",
        "window": "51.0-54.65", "wide": True, "jesus": False, "ref": False,
        "locks": ["ZAC", "JERICHO"],
        "narration": "and the crowd stood like a wall. Not one person made room for him.",
        "must_show": "the refusal — the people nearest him closing shoulder to shoulder against him on purpose.",
        "must_not_show": "no shoving or laughter; a deliberate, silent, closed line.",
        "scene": (
            "Two townsmen at the back of the crowd have deliberately closed shoulder "
            "to shoulder to shut Zacchaeus out, one glancing back at him with flat "
            "dislike as he does it, and Zacchaeus stands stopped in front of them, "
            "the smallest man there, his hand still half-raised from asking. Hard "
            "midday sun on the honey-coloured street. Exactly three people are in "
            "the foreground; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b09", "out": "s09-he-ran.jpeg", "seg": "n3a",
        "window": "55.65-62.73", "wide": True, "jesus": False, "ref": False,
        "locks": ["ZAC", "JERICHO"],
        "narration": ("So this small, wealthy man did something no respectable "
                      "person would ever do. He gathered up his fine robes, and he ran."),
        "must_show": "v4 — a rich man of standing RUNNING, robes hitched in his fists, ahead of the crowd.",
        "must_not_show": "not a dignified jog — an undignified, all-out run.",
        "scene": (
            "SHOT FROM THE SIDE OF THE STREET with the camera low, so Zacchaeus runs "
            "ACROSS the frame from right to left, getting out ahead of the crowd. He "
            "has his expensive wine-burgundy robe hitched up in both fists above his "
            "knees, sandals kicking dust, his face set and undignified and "
            "determined, caught mid-stride with both feet clear of the ground. "
            "Behind him townspeople have turned to stare at the sight of a rich man "
            "running. Hard midday sun. Every figure has two arms, two hands, two "
            "legs and one head."
        ),
    },
    {
        "id": "v2-r003-b10", "out": "s10-climbs-the-tree.jpeg", "seg": "n3b p1",
        "window": "63.73-70.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["ZAC", "SYCOMORE", "JERICHO"],
        "narration": "And he climbed a sycamore tree, like a child.",
        "must_show": "v4 — the climb in progress, a middle-aged rich man hauling himself into the low limbs.",
        "must_not_show": "he is not gracefully seated yet; this is the effort of it.",
        "scene": (
            "Zacchaeus is halfway up into the sycomore fig tree beside the road, one "
            "knee hooked over a low horizontal limb and both arms hauling his weight "
            "up, his fine wine-burgundy robe rucked and snagged, one sandal dangling "
            "off his heel, dust and bark on his hands. It is plainly hard work for a "
            "soft middle-aged man. Hard midday sun through the leaves. Exactly one "
            "person is in the frame, with two arms, two hands of five fingers each, "
            "two legs and one head."
        ),
    },
    {
        "id": "v2-r003-b11", "out": "s11-traded-his-dignity.jpeg", "seg": "n3b p2",
        "window": "70.0-81.22", "wide": True, "jesus": False, "ref": False,
        "locks": ["ZAC", "SYCOMORE", "JERICHO"],
        "narration": ("Zacchaeus traded the last of his dignity for one glimpse of "
                      "Jesus — from a distance. He would have settled for that."),
        "must_show": "the price paid — him settled in the branches while the people below see him up there.",
        "must_not_show": "no cruel caricature; the townspeople's faces are scornful, not comic.",
        "scene": (
            "Zacchaeus sits astride a heavy limb of the sycomore well above the "
            "road, leaves around him, gripping the branch with both hands and "
            "craning down the road toward the coming crowd with open, undefended "
            "hope on his face. On the ground below, three townspeople have stopped "
            "to look up at the sight of the richest man in Jericho in a tree, their "
            "faces hard with scorn. Hard midday sun. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r003-b12", "out": "s12-jesus-stopped.jpeg", "seg": "n4 p1",
        "window": "82.22-86.0", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ZAC", "SYCOMORE", "JERICHO"],
        "narration": "He got far more. Jesus stopped — under that exact tree —",
        "must_show": "v5 — Jesus halted directly beneath the sycomore; the whole moving crowd stopping with him.",
        "must_not_show": "he has not looked up yet; the crowd does not know why he stopped.",
        "scene": (
            "Jesus has stopped dead in the middle of the road directly beneath the "
            "sycomore fig tree, and the crowd walking with him has bunched to a halt "
            "around him, some still moving, several turning to see why he stopped. "
            "He is standing quite still, head beginning to tilt back. High in the "
            "branches above and behind him Zacchaeus is small among the leaves, and "
            "nobody on the ground has noticed him. Hard midday sun. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b13", "out": "s13-looked-up.jpeg", "seg": "n4 p2",
        "window": "86.0-88.77", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ZAC", "SYCOMORE"],
        "narration": "looked up, and called him by name.",
        "must_show": "v5 — the eyeline: Jesus looking straight up into the branches, finding him.",
        "must_not_show": "no halo/glow; the crowd is out of focus behind — this is between the two of them.",
        "scene": (
            "SHOT FROM LOW AND BESIDE JESUS so his upturned face is seen clearly in "
            "profile and the line of his gaze runs straight up into the sycomore's "
            "branches. He is looking directly up at Zacchaeus with warm recognition, "
            "his face open and unhurried, speaking — and up in the leaves Zacchaeus "
            "has gone completely still, caught, staring back down at him. The two "
            "gazes meet on a single line through the frame. Hard midday sun through "
            "the leaves. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b14", "out": "s14-make-haste-come-down.jpeg", "seg": "j1a",
        "window": "89.77-91.86", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SYCOMORE"],
        "narration": "Zacchaeus, make haste, and come down; (Luke 19:5)",
        "must_show": "close on Jesus calling up into the tree — the moment he uses the man's NAME.",
        "must_not_show": "no rebuke on his face; this is gladness, an invitation.",
        "scene": (
            "Close on Jesus from slightly below, his face tilted up toward the "
            "branches and lit by hard midday sun, mid-word, one hand lifted and open "
            "toward the tree in an unmistakable come-down gesture. His expression is "
            "warm and glad and certain, as if calling a friend he had come to find. "
            "Sycomore leaves fill the top of the frame above him. Exactly one person "
            "is in the frame, with two arms, two hands of five fingers each and one "
            "head."
        ),
    },
    {
        "id": "v2-r003-b15", "out": "s15-abide-at-thy-house.jpeg", "seg": "j1b",
        "window": "93.34-95.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["ZAC", "SYCOMORE"],
        "narration": "for to day I must abide at thy house. (Luke 19:5)",
        "must_show": "Zacchaeus's face receiving it — a man who expected a glimpse and has been invited instead.",
        "must_not_show": "no tears streaming; astonishment first, joy arriving behind it.",
        "scene": (
            "Close on Zacchaeus up in the sycomore, both hands still gripping the "
            "branch, his face turned down toward the road and broken wide open with "
            "astonishment — his mouth slightly parted, his careful blankness gone "
            "completely, joy arriving behind the shock as he understands what has "
            "just been said to him. Leaves and hard midday light around him. Exactly "
            "one person is in the frame, with two arms, two hands of five fingers "
            "each and one head."
        ),
    },
    {
        "id": "v2-r003-b16", "out": "s16-what-a-meal-meant.jpeg", "seg": "n5 p1",
        "window": "97.10-108.0", "wide": True, "jesus": True, "ref": REF,
        "locks": ["JERICHO"],
        "narration": ("Understand what a meal meant back then. To eat at a man's "
                      "house was to publicly accept him."),
        "must_show": "the crowd hearing it — the public nature of the invitation registering on their faces.",
        "must_not_show": "Zacchaeus is still up the tree and NOT in this frame; the crowd is the subject.",
        "scene": (
            "The packed Jericho crowd in the road has heard what was said, and it is "
            "going through them — men turning to each other, a woman's hand at her "
            "mouth, faces stiffening all down the street. In the middle of them "
            "Jesus stands calm and unbothered, still turned toward the tree, "
            "entirely unconcerned with what the street thinks. Hard midday sun. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b17", "out": "s17-jesus-moves-first.jpeg", "seg": "n5 p2",
        "window": "108.0-118.13", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ZAC", "SYCOMORE", "JERICHO"],
        "narration": ("Jesus didn't tell him to clean up his life first. He invited "
                      "himself in — before Zacchaeus had changed a single thing. "
                      "That is the point of the whole story. Jesus moves first."),
        "must_show": "the offered hand — Jesus waiting at the foot of the tree for a man who has changed nothing yet.",
        "must_not_show": "no money, no restitution, no repentance anywhere in this frame — that all comes later.",
        "scene": (
            "Jesus stands at the foot of the sycomore with one hand held out and "
            "open toward the branches, waiting, his face patient and glad — and "
            "Zacchaeus is above him swinging a leg down off the limb, still in his "
            "rich robe, still exactly the man the whole street despises, reaching "
            "for the offered hand. Nothing about him has changed yet. The crowd "
            "stands back watching. Hard midday sun. Every figure has two arms, two "
            "hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r003-b18", "out": "s18-received-him-joyfully.jpeg", "seg": "n6 p1",
        "window": "119.13-123.0", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ZAC", "SYCOMORE", "JERICHO"],
        "narration": "Zacchaeus came down faster than he had climbed up, and welcomed him with joy.",
        "must_show": "v6 — down on the road, receiving him JOYFULLY; the first open happiness on his face.",
        "must_not_show": "not kneeling or grovelling — he is welcoming a guest.",
        "scene": (
            "Down on the road at the foot of the tree, Zacchaeus has both hands "
            "clasped around one of Jesus's hands and is beaming up at him, bark dust "
            "still on his robe and his sash crooked from the climb, his whole face "
            "lit with undisguised joy as he welcomes him — and Jesus is smiling back "
            "down at him, unhurried. Zacchaeus is a full head shorter than him. Hard "
            "midday sun. Every figure has two arms, two hands of five fingers each "
            "and one head."
        ),
    },
    {
        "id": "v2-r003-b19", "out": "s19-they-all-murmured.jpeg", "seg": "n6 p2 + s7",
        "window": "123.0-129.68", "wide": True, "jesus": False, "ref": False,
        "locks": ["JERICHO"],
        "narration": ("But the crowd was appalled. / That he was gone to be guest "
                      "with a man that is a sinner. (Luke 19:7)"),
        "must_show": "v7 — they ALL murmured; the whole street's disapproval, heads together.",
        "must_not_show": "no fists or stones; this is muttering, not a mob. Jesus is NOT in this frame.",
        "scene": (
            "The Jericho street has turned into knots of muttering townspeople — "
            "heads bent together, sidelong looks thrown the same direction, a man "
            "with folded arms shaking his head, an older woman's mouth tight with "
            "disgust as she says something to her neighbour. Every one of them is an "
            "ordinary villager. Hard midday sun on the honey-coloured stone. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b20", "out": "s20-to-the-worst-mans-house.jpeg", "seg": "n6b",
        "window": "131.16-138.29", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ZAC", "JERICHO", "HOUSE"],
        "narration": ("Of every house in Jericho, he had chosen the worst man's. In "
                      "their rules, you earned your way back before anyone sat with you."),
        "must_show": "the walk to the door — the two of them going in together while the street watches.",
        "must_not_show": "no triumph on either face; they are simply walking to a meal.",
        "scene": (
            "SHOT FROM BEHIND AND TO THE SIDE OF THE WATCHING CROWD, looking past "
            "their shoulders down the street: Jesus and Zacchaeus are walking away "
            "from the camera side by side toward the fine studded door of "
            "Zacchaeus's house, talking as they go, Zacchaeus a head shorter and "
            "half-turned up toward him. The townspeople in the foreground stand "
            "still and watch them go. Late afternoon light, long shadows down the "
            "street. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b21", "out": "s21-zacchaeus-stood.jpeg", "seg": "n7a",
        "window": "139.29-143.10", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ZAC", "HOUSE"],
        "narration": "Then, at that table, it happened. Zacchaeus stood up in front of everyone.",
        "must_show": "v8 — he STOOD; a full table of guests, and the host on his feet.",
        "must_not_show": "he has not spoken yet; the room is only just turning to him.",
        "scene": (
            "In the warm lamplit hall of his house, at a long low table crowded with "
            "guests at their food, Zacchaeus has pushed himself to his feet beside "
            "his own chair — the shortest man in the room, standing while everyone "
            "else reclines — and the whole table is turning toward him mid-meal. "
            "Jesus is seated among them, already looking up at him. Warm oil-lamp "
            "light. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b22", "out": "s22-the-half-of-my-goods.jpeg", "seg": "s8",
        "window": "144.10-152.81", "wide": True, "jesus": False, "ref": False,
        "locks": ["ZAC", "HOUSE"],
        "narration": ("Behold, Lord, the half of my goods I give to the poor; and if "
                      "I have taken any thing from any man by false accusation, I "
                      "restore him fourfold. (Luke 19:8)"),
        "must_show": "the vow itself — spoken standing, in public, to the whole room.",
        "must_not_show": "no money being handed over yet; this is the promise, not the act.",
        "scene": (
            "Zacchaeus stands at his own table in the warm lamplight mid-sentence, "
            "one hand pressed flat against his chest and the other open toward the "
            "door and the town beyond it, his face fierce and wet-eyed and utterly "
            "in earnest. The guests around the table have stopped eating entirely, "
            "several staring at him. Every figure has two arms, two hands of five "
            "fingers each and one head."
        ),
    },
    {
        "id": "v2-r003-b23", "out": "s23-restores-fourfold.jpeg", "seg": "n7b",
        "window": "154.28-176.58", "wide": True, "jesus": False, "ref": False,
        "locks": ["ZAC", "HOUSE"],
        "narration": ("Half of everything I own goes to the poor, he said — and "
                      "anyone I have cheated, I will pay back four times over."),
        "must_show": "the act following the vow — the strongbox open, coin actually leaving his hands.",
        "must_not_show": "this comes AFTER the invitation, never before it.",
        "scene": (
            "Zacchaeus kneels beside his own iron-bound strongbox on the lamplit "
            "floor with the lid thrown back, counting heavy silver coins out of it "
            "into a leather bag held open by a servant in dark earth-brown wool, "
            "while a second servant carries a full bag toward the door. Zacchaeus is "
            "not looking at the money; he is looking toward the table behind him. "
            "Warm oil-lamp light. Exactly three people are in the frame; each has "
            "two arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r003-b24", "out": "s24-salvation-this-house.jpeg", "seg": "n7c + j2a",
        "window": "177.58-187.21", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ZAC", "HOUSE"],
        "narration": ("And Jesus answered him with the words this story was written "
                      "to keep. / This day is salvation come to this house, "
                      "forsomuch as he also is a son of Abraham. (Luke 19:9)"),
        "must_show": "v9 — Jesus answering, and the room hearing a despised man called a son of Abraham.",
        "must_not_show": "no halo/glow; the room is the witness this verse needs.",
        "scene": (
            "Jesus has risen at the table in the warm lamplight and is speaking "
            "directly to Zacchaeus, one hand extended toward him and the other open "
            "to the whole room, his face steady and glad. Zacchaeus stands facing "
            "him with his hands loose at his sides, undone. Every guest at the table "
            "is looking at the two of them. Warm oil-lamp light. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b25", "out": "s25-seek-and-to-save.jpeg", "seg": "j2b + n8",
        "window": "188.69-200.52", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ZAC", "HOUSE"],
        "narration": ("For the Son of man is come to seek and to save that which was "
                      "lost. (Luke 19:10)"),
        "must_show": "v10 — the sentence the whole story exists to keep, spoken to the room.",
        "must_not_show": "not a private aside; he says it to everyone.",
        "scene": (
            "A wider view of the lamplit hall: Jesus stands at the head of the table "
            "speaking to the whole room, and every face at that table is turned to "
            "him — including two guests whose expressions have changed from "
            "disapproval to something unsettled. Zacchaeus stands close at his side "
            "in his wine-burgundy robe, restored to his own house. Warm oil-lamp "
            "light. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r003-b26", "out": "s26-he-was-seeking.jpeg", "seg": "n9",
        "window": "201.52-211.56", "wide": True, "jesus": True, "ref": REF,
        "locks": ["JERICHO"],
        "narration": ("Jesus was not stuck in that crowd by accident. He was "
                      "seeking."),
        "must_show": "the closing image — Jesus out under the dusk sky over Jericho, having come on purpose.",
        "must_not_show": "no halo/glow; he is alone with the town below him, not posed heroically.",
        "scene": (
            "SHOT FROM BEHIND AND SLIGHTLY BESIDE JESUS in the blue-gold light of "
            "dusk, standing in the open doorway of the house looking out over the "
            "rooftops and date palms of Jericho as the first lamps come on in the "
            "windows below. His face is seen in three-quarter profile, thoughtful "
            "and purposeful, already looking down the road out of the town. Exactly "
            "one person is in the frame, with two arms, two hands and one head."
        ),
    },
]
