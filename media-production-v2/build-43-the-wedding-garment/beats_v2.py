#!/usr/bin/env python3
"""V2 beat map — row 43, build-43-the-wedding-garment (Matthew 22:1-14).

COVERAGE: 48 pictures over 273.2 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 22:1-14 KJV):
  Context: taught IN THE TEMPLE during the last week, with the chief
  priests and elders who were hunting him standing in front of him
  (Matthew 21:23, 45-46) — the frame beats stage Jesus in the temple's
  columned court facing hostile fine-robed men, ordinary listeners
  around; distinct from every earlier frame staging.
  v2-3  a king's marriage feast for HIS SON; the invited "WOULD NOT COME"
        — they had accepted long before (the double-invitation custom):
        their refusal is a broken yes.
  v4    "my oxen and my fatlings are killed, and ALL THINGS ARE READY" —
        readiness painted lavish and waiting.
  v5-6  "they MADE LIGHT of it ... one to his farm, another to his
        merchandise: and the remnant took his servants, and entreated
        them spitefully, and slew them."
        ⚑ RESTRAINED (CONTENT-CARE 'destruction OFF-SCREEN' rule): the
        violence is shown as a returned servant with a torn robe and a
        bruised messenger helped through the palace door — NO killing on
        screen; the city's judgment (v7) is NOT depicted at all — only
        the king's grieved, hardening face at the news.
  v8-10 "GO YE THEREFORE INTO THE HIGHWAYS ... both BAD and GOOD: and
        the wedding was furnished with guests."
        ⚑ Flags J,L (CONTENT-CARE §3 row 43): 'invited freely off the
        highways FIRST' — the open-invitation beats are the row's engine
        and get its warmest frames.
  vNARR the garment custom: the clean festival robe was THE KING'S GIFT,
        handed to every guest at the door — nobody owned one; everyone
        in the hall wears something the king put on them. The robe-chest
        at the door is a locked visual.
  v11-13 the robeless man: called "FRIEND", questioned gently, "and he
        was SPEECHLESS." The outer darkness is DARKNESS ONLY — the man
        escorted out of the light into the plain dark, the doorway's
        warmth behind him; no pit, no flames, no screaming, ever.
  v14   "many are called, but few chosen" — the closing beats give the
        narration's resolution: everyone invited; the chosen are simply
        those who came and LET the King dress them.

TIME OF DAY: the temple frame is bright late-morning. The parable:
preparation in golden afternoon; the refusals in plain working
daylight; the highways sweep at DUSK into lamplit NIGHT (the feast is
an evening feast — lamplight throughout the hall beats); the outer
darkness beat is full night by contrast with the door's warmth; the
closing invitation beats return to the lit door.

CHANGING CONDITION (kept OUT of the locks): the hall — empty and
waiting, filling, full; and the guests' dress — road rags at the door,
gold festival robes inside. The one robeless man keeps his dusty road
clothes in every beat he appears.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "KING": (
        "KING LOCK: the king is the same man in every shot — about "
        "sixty, tall and broad, with a full silver-and-black beard, "
        "great warm heavy-browed eyes and a bearing of absolute unhurried "
        "authority. He wears a DEEP ROYAL-BLUE robe with wide DARK GOLD "
        "embroidered borders, a heavy gold chain, and a plain gold "
        "circlet (never cream, never white). His face is shown clearly "
        "— joy is its resting state; grief and gravity visit it."
    ),
    "STEWARD": (
        "DOOR STEWARD LOCK: the steward of the robes is the same man in "
        "every shot — about fifty, neat and quick, with a short grey "
        "beard and kind practised hands. He wears a DARK PLUM tunic "
        "with a DEEP GOLD sash of office (never cream, never white). "
        "His face is shown clearly."
    ),
    "GUEST": (
        "ROBELESS MAN LOCK: the man without the garment is the same man "
        "in every shot — about forty, lean and proud-faced, with a "
        "short dark beard, a high chin and guarded eyes. He wears "
        "road-dusty SLATE-GREY travelling clothes with a frayed DARK "
        "IRON-BROWN cloak, unchanged in every beat (never cream, never "
        "white). His face is shown clearly — pride, never poverty, is "
        "his story."
    ),
    "HALL": (
        "WEDDING HALL LOCK: the king's wedding hall at night — a long "
        "high stone hall strung with hanging oil lamps, garlands of "
        "myrtle down the pillars, long tables laden end to end, a "
        "musicians' corner, and at its entrance a wide doorway with a "
        "great carved ROBE CHEST beside it, stacked with folded DARK "
        "GOLD festival robes. The same lamps, tables, doorway and "
        "chest throughout."
    ),
    "ROADS": (
        "HIGHWAYS LOCK: the roads at dusk — a crossroads outside the "
        "city walls where three dirt highways meet at a boundary "
        "stone, hedges and ditches along them, and the travelling "
        "poor moving or resting there: day labourers, beggars, "
        "footsore families, in worn SATURATED DEEP earth colours "
        "(never cream, never white; only Jesus wears cream). Faces "
        "shown clearly."
    ),
    "TEMPLE": (
        "TEMPLE COURT LOCK: a columned court of the temple in bright "
        "late-morning light — vast pale limestone paving, high "
        "porticoes, and before the speaker a front rank of hostile "
        "fine-robed men in NEAR-BLACK INDIGO and DARK UMBER with "
        "fringed shawls, ordinary listeners gathered behind and "
        "around them in worn earth tones (never cream, never white; "
        "only Jesus wears cream). Faces shown clearly."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r043-b01", "out": "s01-and-jesus-answered-and-spake.jpeg", "seg": "s1",
        "window": "0.28-4.37", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TEMPLE"],
        "narration": (
            "And Jesus answered and spake unto them again by parables, and "
            "said,"
        ),
        "must_show": "SCRIPTURE-EXACT: the frame — Jesus in the temple court facing the front rank of hostile robed men, ordinary listeners banked behind them; a story told into enemy faces.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hostility in the front rank visible but controlled — men taking notes with their eyes.",
        "scene": (
            "In the bright columned court, the camera just behind "
            "Jesus's shoulder so the confrontation opens away "
            "from the lens, Jesus stands facing a "
            "front rank of fine-robed men whose stillness is "
            "the stillness of hunters — arms folded into "
            "fringed shawls, eyes flat and gathering evidence — "
            "while behind and around them the ordinary crowd "
            "banks up between the columns, and he begins the "
            "story anyway, calm, straight into the faces that "
            "are measuring him for a charge. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b02", "out": "s02-he-was-teaching-in-the.jpeg", "seg": "n1",
        "window": "5.94-11.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE"],
        "narration": (
            "He was teaching in the temple, and the men who were hunting for a "
            "way to arrest him were standing right in front of him."
        ),
        "must_show": "the danger named — close past Jesus's shoulder at two hostile faces in the front rank: intelligent, patient, predatory attention.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hunters humanized — dangerous by intelligence, not caricature.",
        "scene": (
            "Close past the edge of Jesus's shoulder: two faces "
            "in the hostile front rank fill the frame — an "
            "older man with a silver-streaked beard and eyes "
            "of cold patient appraisal, a younger one beside "
            "him with a scribe's quick gaze flicking to catch "
            "every word — two intelligent men listening the "
            "way trappers watch a trail, in the bright "
            "temple light. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r043-b03", "out": "s03-so-he-told-them-a.jpeg", "seg": "n1",
        "window": "11.53-19.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE"],
        "narration": (
            "So he told them a story: about a king, a wedding, and an "
            "invitation that almost nobody took."
        ),
        "must_show": "the story raised — Jesus lifting one hand to begin, the whole court quieting, even the hostile rank leaning in despite themselves.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the involuntary lean of enemies — a story too good not to hear.",
        "scene": (
            "Jesus lifts one hand and the whole court quiets "
            "around the gesture — the ordinary listeners "
            "pressing in, a child hoisted to a shoulder — and "
            "even along the hostile front rank the bodies "
            "betray their owners, one man's head tilting in "
            "against his will, another's folded arms loosening "
            "a degree, enemies leaning into a story because "
            "stories do not check credentials. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b04", "out": "s04-the-kingdom-of-heaven-is.jpeg", "seg": "jv2",
        "window": "19.84-25.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING", "HALL"],
        "narration": (
            "The kingdom of heaven is like unto a certain king, which made a "
            "marriage for his son,"
        ),
        "must_show": "SCRIPTURE-EXACT: the occasion — the king in his hall directing the wedding preparations, joy all over him; a father throwing his son's feast.",
        "must_not_show": "no halo, glare or rim-light; paternal joy is the king's baseline — this feast is love, not protocol.",
        "scene": (
            "In the great hall by warm lamplight the tall king "
            "moves through his son's wedding preparations like "
            "weather — one arm directing the garland-hangers "
            "up the pillars, the other hand tasting from a "
            "steward's offered spoon, his great bearded face "
            "alight with a father's unguarded joy — the whole "
            "hall being built around one evening of his son's "
            "happiness. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r043-b05", "out": "s05-a-king-was-giving-a.jpeg", "seg": "n2",
        "window": "26.68-29.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": "A king was giving a wedding feast for his son.",
        "must_show": "the father's heart — close on the king's face watching (off-frame) his son, all the feast's meaning in the look.",
        "must_not_show": "no halo, glare or rim-light; the feast personalized — one face full of one boy.",
        "scene": (
            "A close portrait of the king in the lamplight, "
            "looking past the camera with his whole face "
            "softened — the heavy brows lifted, the "
            "silver-and-black beard parted over the beginning "
            "of a smile, great warm eyes fixed on an unseen "
            "young man across the hall — every table and lamp "
            "and garland in the building explained in one "
            "father's expression. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b06", "out": "s06-the-oxen-were-prepared-the.jpeg", "seg": "n2",
        "window": "29.10-34.11", "wide": True, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": (
            "The oxen were prepared, the tables were loaded, the hall was full "
            "of light."
        ),
        "must_show": "SCRIPTURE-EXACT: all things ready — the hall at full readiness: lamps all lit, tables laden end to end, roast oxen carried steaming from the kitchens, no guest yet arrived.",
        "must_not_show": "no halo, glare or rim-light; lavish readiness AND emptiness — every place set, every seat vacant.",
        "scene": (
            "The wedding hall stands at the summit of readiness, "
            "the camera at the great door looking down its "
            "length, the kitchen men crossing in profile: "
            "every hanging lamp lit down the long ceiling, the "
            "tables laden end to end with bread towers and "
            "fruit and wine, two kitchen men carrying in a "
            "steaming quarter of roast ox on a plank between "
            "them — and down the whole golden lamplit length, "
            "not one guest: cushions plumped, cups filled, "
            "seats empty from the door to the musicians' "
            "corner. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r043-b07", "out": "s07-and-the-guests-had-been.jpeg", "seg": "n2",
        "window": "34.11-39.31", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "And the guests had been invited long before. They had already said "
            "they would come."
        ),
        "must_show": "the broken yes foreshadowed — a close still of the invitation tokens: fine carved acceptance tablets returned long ago, stacked and kept by the door; promises in wood.",
        "must_not_show": "no halo, glare or rim-light; the tokens formal and old — yeses given at leisure, waiting to be honoured.",
        "scene": (
            "A close still by the hall door's lamplight: a "
            "shallow tray holding the guests' acceptance "
            "tokens — small fine tablets of carved wood, each "
            "marked with a family's sign, returned months ago "
            "and kept in honour — two dozen formal yeses "
            "stacked in neat rows beside the door they were "
            "promised to walk through tonight. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b08", "out": "s08-and-sent-forth-his-servants.jpeg", "seg": "jv3",
        "window": "39.90-45.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING", "HALL"],
        "narration": (
            "And sent forth his servants to call them that were bidden to the "
            "wedding: and they would not come."
        ),
        "must_show": "SCRIPTURE-EXACT: the calling sent — servants dispatched from the hall door into the evening with lanterns, the king watching them go from the lit threshold.",
        "must_not_show": "no halo, glare or rim-light; ceremony and confidence — nobody yet knows the yeses are dead.",
        "scene": (
            "From the hall's wide lit doorway four servants "
            "set out into the blue evening with lanterns "
            "raised, sashes straightened, carrying the glad "
            "summons to houses that answered yes months ago — "
            "and behind them in the doorway the king stands "
            "framed in his own feast's light, one hand lifted "
            "in easy confidence, sending joy out into a city "
            "he has no reason to doubt. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b09", "out": "s09-so-when-the-day-arrived.jpeg", "seg": "n3",
        "window": "47.20-50.97", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "So when the day arrived, the king sent his servants to go and "
            "bring them in."
        ),
        "must_show": "the summons at a fine door — a servant with his lantern at a prosperous house's entrance, formal and glad, the errand still innocent.",
        "must_not_show": "no halo, glare or rim-light; the last innocent moment — courtesy meeting courtesy, in theory.",
        "scene": (
            "At the carved door of a prosperous townhouse in "
            "the early evening a royal servant stands with his "
            "lantern lifted and his head bowed in formal "
            "gladness, the summons spoken — the door's fine "
            "bronze fittings catching his light, a house that "
            "said yes in the spring being called, with all "
            "courtesy, to keep an autumn promise. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b10", "out": "s10-behold-i-have-prepared-my.jpeg", "seg": "jv4",
        "window": "51.57-59.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": (
            "Behold, I have prepared my dinner: my oxen and my fatlings are "
            "killed, and all things are ready: come unto the marriage."
        ),
        "must_show": "SCRIPTURE-EXACT: the readiness itemized — the laden hall again at its peak, steam still rising, the words' whole inventory visible and waiting.",
        "must_not_show": "no halo, glare or rim-light; abundance with a clock on it — hot food and empty seats; the waiting has begun to show.",
        "scene": (
            "Down the hall's golden length the feast stands at "
            "its perfect hour — steam still curling off the "
            "carved ox, the bread's warmth visible in its "
            "sheen, wine breathing in the mixing bowls — and "
            "along the tables the emptiness has begun to "
            "acquire weight: a steward straightening an "
            "already straight cushion, a musician silencing a "
            "string he tuned an hour ago, readiness starting, "
            "very quietly, to wait. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b11", "out": "s11-and-they-would-not-come.jpeg", "seg": "n4",
        "window": "61.54-62.84", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "And they would not come.",
        "must_show": "the refusal at the door — the fine townhouse door closing on the servant's lantern light, unhurried and final.",
        "must_not_show": "no halo, glare or rim-light; a polite, terrible closing — no anger needed, just the door.",
        "scene": (
            "At the prosperous townhouse the carved door "
            "swings quietly closed against the servant's "
            "lantern light — a well-mannered hand just visible "
            "withdrawing at its edge, the bronze fittings "
            "turning away the summons with perfect courtesy — "
            "and the servant's lit face left in the narrowing "
            "wedge of the evening, holding a lantern and a "
            "dead yes. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r043-b12", "out": "s12-not-one-of-them-they.jpeg", "seg": "n4",
        "window": "62.84-71.25", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Not one of them. They had said yes, and now, with everything ready "
            "and waiting, they simply would not walk over."
        ),
        "must_show": "the refusals compounding — a street of fine houses at evening, three royal servants at three doors, every door shut or shutting; a whole class declining at once.",
        "must_not_show": "no halo, glare or rim-light; the pattern visible in one street — synchronized, casual, complete.",
        "scene": (
            "Down a handsome evening street of fine houses, the "
            "camera behind the servants so all three doors face "
            "away from the lens, the "
            "pattern shows itself whole: three royal servants "
            "at three separate doors, and every door failing "
            "them at once — one already shut, one closing on a "
            "polite raised palm, one opened only by a "
            "houseboy shaking his head — three lanterns "
            "burning in the dusk outside three warm houses "
            "that all said yes in the spring. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b13", "out": "s13-out-to-the-roads.jpeg", "seg": "n8",
        "window": "125.87-126.87", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROADS"],
        "narration": "Out to the roads.",
        "must_show": "the new direction — the crossroads at dusk: three highways meeting at the boundary stone, the travelling poor upon them; the feast's next guest list.",
        "must_not_show": "no halo, glare or rim-light; the roads as they are — worn people, real dusk, the whole unlisted world.",
        "scene": (
            "At the crossroads outside the walls, the camera beside "
            "the boundary stone taking the junction from the side, "
            "the dusk "
            "gathers over three meeting highways: a footsore "
            "family resting against the boundary stone, two "
            "day labourers walking home with their tools, an "
            "old beggar settling into the hedge's shelter for "
            "the night, a peddler's tired donkey — the whole "
            "unlisted world of the roads, going about its "
            "evening with no idea what is coming for it. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r043-b14", "out": "s14-but-they-made-light-of.jpeg", "seg": "jv5_6",
        "window": "71.80-82.90", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "But they made light of it, and went their ways, one to his farm, "
            "another to his merchandise: And the remnant took his servants, and "
            "entreated them spitefully, and slew them."
        ),
        "must_show": "SCRIPTURE-EXACT, RESTRAINED: the making light and the violence off-screen — one invited man riding to his farm laughing over his shoulder, another turning to his shop ledgers; and at the frame's far edge a royal servant being SHOVED from a doorway, his lantern falling — nothing worse shown.",
        "must_not_show": "no halo, glare or rim-light; NO killing depicted — the shove and the falling lantern are the utmost; the words carry the rest.",
        "scene": (
            "The refusals go their ways in the last light, the "
            "camera holding the street from the side so every "
            "travel crosses the frame in profile: in "
            "the near frame a prosperous man rides out his "
            "gate toward his farm, waving the summons off "
            "over his shoulder with a laugh, while through a "
            "shop's doorway another bends already to his "
            "ledgers — and at the street's far end, small and "
            "terrible, a royal servant staggers from a "
            "doorway's shove, his lantern falling in an arc "
            "of spilled light toward the stones. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b15", "out": "s15-they-all-had-something-else.jpeg", "seg": "n5",
        "window": "84.39-85.87", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "They all had something else.",
        "must_show": "the something-elses — a close still: a farm ledger, a merchant's scales and a house key laid on a table over the king's unopened summons scroll.",
        "must_not_show": "no halo, glare or rim-light; good ordinary things — the crime is only their placement on top of the invitation.",
        "scene": (
            "A close still on a fine table in lamplight: a "
            "farm's harvest ledger, a merchant's small brass "
            "scales and a heavy house key laid carelessly "
            "across one another — and beneath the pile, its "
            "royal seal unbroken, the king's summons scroll "
            "flattened at one corner, buried under three "
            "perfectly reasonable lives. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b16", "out": "s16-a-field-to-go-look.jpeg", "seg": "n5",
        "window": "85.87-88.93", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "A field to go look at. A shop to keep.",
        "must_show": "the rival loves — the invited man standing in his beautiful dusk field, content, the city's faint feast-light behind him unnoticed.",
        "must_not_show": "no halo, glare or rim-light; the field genuinely lovely — a good thing, fully attended, at the wrong hour.",
        "scene": (
            "In the deep dusk the invited man stands in his "
            "own beautiful field, boots planted in the turned "
            "earth, surveying his land's dark richness with "
            "complete contentment — while far behind his back, "
            "small on the city's hill, the faint warm points "
            "of the feast-hall's lamps burn unnoticed at the "
            "edge of his ownership. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b17", "out": "s17-the-own-guests-looked-at.jpeg", "seg": "n5 + n6",
        "window": "88.93-95.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": (
            "The king's own guests looked at his son's wedding and decided they "
            "had better things to do. And some of them did worse."
        ),
        "must_show": "the insult landing — the king at the hall door receiving the first news, the acceptance tokens tray in his hand, his joy beginning to crack.",
        "must_not_show": "no halo, glare or rim-light; the crack in the joy — hurt arriving in a face built for delight.",
        "scene": (
            "At the hall's lit threshold the king stands with "
            "the tray of acceptance tokens still in one great "
            "hand, the first returned servant before him with "
            "empty hands and lowered eyes — and across the "
            "king's broad glad face the news is arriving in "
            "real time: the heavy brows drawing, the smile's "
            "architecture failing joint by joint, a father's "
            "joy cracking along lines hurt always finds "
            "first. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r043-b18", "out": "s18-they-turned-on-the-servants.jpeg", "seg": "n6",
        "window": "95.87-104.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING", "HALL"],
        "narration": (
            "They turned on the servants who came to invite them. It was the "
            "kind of insult a kingdom does not survive, and that city did not "
            "survive it."
        ),
        "must_show": "⚑ RESTRAINED (off-screen rule): the aftermath only — a bruised servant with a torn robe helped in through the hall door by two others, and the king's face gone from grief to iron; NO violence, NO city judgment depicted.",
        "must_not_show": "no halo, glare or rim-light; NOTHING burns, no one dies on screen — the torn robe, the bruise, and the king's changed face carry the entire weight.",
        "scene": (
            "Through the hall's doorway two servants help in a "
            "third — his robe torn at the shoulder, a bruise "
            "darkening his cheekbone, his lantern gone — and "
            "the king has come down the hall to meet them, "
            "one great hand cupping the hurt man's face with "
            "terrible gentleness while above it his own face "
            "finishes its journey from grief to iron: a "
            "father's hurt cooling into a king's verdict, "
            "with not one flame anywhere in the frame. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b19", "out": "s19-but-the-feast-was-still.jpeg", "seg": "n7",
        "window": "104.98-108.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": "But the feast was still ready. The food was still hot.",
        "must_show": "readiness surviving the insult — close along a laden table: steam still rising off the dishes, lamps steady; the feast refusing to die.",
        "must_not_show": "no halo, glare or rim-light; warmth persisting — the food's steam as quiet defiance.",
        "scene": (
            "Close along the laden table in the steady "
            "lamplight: steam still climbs off the carved ox "
            "and the spiced lentils, the bread's crust still "
            "holds its warmth-sheen, the wine still breathes "
            "in its bowls — a feast built for joy sitting "
            "wounded but alive in an empty hall, keeping "
            "itself hot for guests that now do not exist. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r043-b20", "out": "s20-and-a-hall-built-for.jpeg", "seg": "n7",
        "window": "108.27-113.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING", "HALL"],
        "narration": (
            "And a hall built for a wedding was standing empty. So the king "
            "made a decision."
        ),
        "must_show": "the decision forming — the king alone in the middle of his lamplit empty hall, turning slowly to face the open door and the night beyond it.",
        "must_not_show": "no halo, glare or rim-light; the turn toward the DOOR is the decision — grief pivoting into wider welcome.",
        "scene": (
            "The king stands alone in the exact centre of his "
            "golden empty hall, the laden tables running away "
            "on either side of him — and he is turning, "
            "slowly, deliberately, away from the empty seats "
            "and toward the wide open doorway where the night "
            "and the roads begin, his heavy face setting "
            "around an idea the original guest list would "
            "never have survived. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b21", "out": "s21-the-wedding-is-ready-but.jpeg", "seg": "jv8_9",
        "window": "113.82-117.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": "The wedding is ready, but they which were bidden were not worthy.",
        "must_show": "SCRIPTURE-EXACT: the verdict on the list — the king's hand setting the tray of acceptance tokens down, done with it; the list retired.",
        "must_not_show": "no halo, glare or rim-light; the set-down tray is the whole sentence — a guest list laid to rest.",
        "scene": (
            "Close in the lamplight: the king's great ringed "
            "hand sets the tray of carved acceptance tokens "
            "down on a side table with the finality of a "
            "closing book — two dozen family signs, two dozen "
            "kept-then-broken yeses, retired in one quiet "
            "motion — and his hand is already lifting away "
            "toward the door and the roads and whatever "
            "guests the night actually holds. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b22", "out": "s22-go-ye-therefore-into-the.jpeg", "seg": "jv8_9",
        "window": "117.57-124.36", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "HALL"],
        "narration": (
            "Go ye therefore into the highways, and as many as ye shall find, "
            "bid to the marriage."
        ),
        "must_show": "SCRIPTURE-EXACT and ⚑ Flag J,L: THE great command — the king at the door sending every servant out at once toward the dark roads, both arms flung wide: as many as ye shall find.",
        "must_not_show": "no halo, glare or rim-light; the widest gesture in the row — a guest list torn up and replaced with everyone.",
        "scene": (
            "At the hall's wide doorway, the camera off to the side "
            "of the steps with the king in three-quarter, he sends his "
            "whole household out at once — both great arms "
            "flung open toward the dark highways beyond the "
            "city, servants already running past him down the "
            "steps with fresh lanterns kindling as they go — "
            "the grandest gesture his arms have made all "
            "night, wide enough to mean every soul on every "
            "road in the dark. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r043-b23", "out": "s23-not-the-guest-list-the.jpeg", "seg": "n8",
        "window": "126.87-128.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROADS"],
        "narration": "Not the guest list. The roads.",
        "must_show": "the contrast compact — a servant's lantern arriving at the crossroads boundary stone, its light falling on the resting poor; the new list, meeting its first names.",
        "must_not_show": "no halo, glare or rim-light; the lantern's circle finding faces — astonishment beginning at its edge.",
        "scene": (
            "At the dark crossroads the first royal lantern "
            "arrives, its warm circle sliding across the "
            "boundary stone and up onto the faces of the "
            "resting poor — the footsore mother's eyes "
            "lifting, the old beggar's head turning from the "
            "hedge, the labourers stopping mid-stride — the "
            "kingdom's new guest list looking up, one face at "
            "a time, into the light that has come out looking "
            "for exactly them. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r043-b24", "out": "s24-the-day-laborers-the-beggars.jpeg", "seg": "n8",
        "window": "130.58-135.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROADS"],
        "narration": (
            "The day laborers, the beggars, the people nobody ever puts on a "
            "list."
        ),
        "must_show": "the unlisted honoured — close on three roads faces in the lantern light: the labourer, the beggar, the footsore mother; a portrait row of the never-invited.",
        "must_not_show": "no halo, glare or rim-light; each face dignified and distinct — the camera's respect IS the king's.",
        "scene": (
            "Three faces close in the lantern's warm light at "
            "the crossroads: a day labourer with lime dust "
            "still in his beard, an old beggar whose eyes "
            "have not been met in years meeting the light "
            "directly, a young mother with the road's whole "
            "weariness on her and a sleeping child at her "
            "shoulder — three people no list ever carried, "
            "framed one by one like nobility. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b25", "out": "s25-so-those-servants-went-out.jpeg", "seg": "jv10",
        "window": "135.63-146.22", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROADS", "HALL"],
        "narration": (
            "So those servants went out into the highways, and gathered "
            "together all as many as they found, both bad and good: and the "
            "wedding was furnished with guests."
        ),
        "must_show": "SCRIPTURE-EXACT: the gathering — the lamplit road TO the hall filling with the walking poor, servants shepherding them toward the great lit doorway on the hill.",
        "must_not_show": "no halo, glare or rim-light; a river of the unlisted flowing toward the light — wonder and hesitation mixed in the walkers.",
        "scene": (
            "Up the dark road toward the hall's great lit doorway, "
            "the camera beside the road so the climb passes in "
            "profile toward the light, "
            "doorway a new procession climbs — the crossroads' "
            "whole population walking in the servants' "
            "lantern-light: the labourers still carrying "
            "their tools, the mother with her waking child, "
            "the old beggar helped along by a servant's arm, "
            "more shapes joining from every hedge and ditch — "
            "a guest list assembling itself out of the night, "
            "heading for the light on the hill. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b26", "out": "s26-whoever-happened-to-be-out.jpeg", "seg": "n8",
        "window": "128.90-130.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROADS"],
        "narration": "Whoever happened to be out there.",
        "must_show": "the randomness sanctified — a servant's hand extended down to a startled stranger rising from the ditch-side; chosen by location, nothing else.",
        "must_not_show": "no halo, glare or rim-light; no qualification visible anywhere — the man's only credential is being there.",
        "scene": (
            "At the ditch's edge in the lantern light a royal "
            "servant's hand reaches down to a startled "
            "traveller half-risen from his night's shelter in "
            "the hedge — straw in his hair, disbelief on his "
            "face, one hand pointing at his own chest in the "
            "universal question — a man being invited to a "
            "royal wedding for the sole recorded reason that "
            "he happened to be out there. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b27", "out": "s27-they-brought-in-everyone-they.jpeg", "seg": "n9",
        "window": "147.74-151.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["STEWARD", "HALL"],
        "narration": (
            "They brought in everyone they could find. The story does not clean "
            "it up."
        ),
        "must_show": "the door receiving everyone — the roads people arriving at the hall's threshold where the steward welcomes them in exactly as they are: dusty, ragged, astonished.",
        "must_not_show": "no halo, glare or rim-light; as-they-are entry — no cleaning up at the threshold; the welcome precedes everything.",
        "scene": (
            "At the hall's wide threshold the roads arrive as "
            "they are: the labourer hesitating with his dusty "
            "tools still on his shoulder, the mother stopped "
            "dead by the lamplight's warmth on her face, the "
            "beggar's bare feet on the smooth stone — and the "
            "plum-clad steward welcomes each one inward with "
            "a full formal bow, dust and rags and all, "
            "exactly as the roads delivered them. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b28", "out": "s28-it-says-both-the-bad.jpeg", "seg": "n9 + n10",
        "window": "151.85-159.10", "wide": True, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": (
            "It says both the bad and the good, and the wedding hall filled "
            "right up. And here is the part almost everyone misses."
        ),
        "must_show": "the hall FULL — the tables lined end to end with the roads' people in golden robes, the feast finally doing what it was built for.",
        "must_not_show": "no halo, glare or rim-light; the full hall in festival gold — the transformation visible: road faces above royal robes.",
        "scene": (
            "The wedding hall runs full at last, the camera at the "
            "musicians' corner looking back down the length, the "
            "near guests in three-quarter from behind — full from door to "
            "musicians' corner: the roads' people seated "
            "shoulder to shoulder down the laden tables, "
            "every one of them wrapped in a deep gold "
            "festival robe over their road-worn frames — the "
            "labourer laughing with his cup, the old beggar "
            "blinking in the lamplight like a man in a dream, "
            "the child asleep on a cushion of royal cloth — "
            "the feast, finally, being a feast. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b29", "out": "s29-nobody-dragged-in-off-the.jpeg", "seg": "n10",
        "window": "159.10-162.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROADS"],
        "narration": "Nobody dragged in off the street owned wedding clothes.",
        "must_show": "the impossibility stated — a close shot of a roads guest's actual clothes at the door: patched, road-stained, honest rags; what they all arrived in.",
        "must_not_show": "no halo, glare or rim-light; the rags without shame — simply the truth of the roads, held up plainly.",
        "scene": (
            "Close at the hall's threshold in the doorway "
            "light: the old beggar's actual clothing as the "
            "roads made it — a tunic more patch than cloth, "
            "the hems frayed to fringe, road dust worked "
            "grey into every fold, a knotted cord for a belt "
            "— held in the frame without one grain of shame: "
            "the honest uniform of everyone the king just "
            "invited. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r043-b30", "out": "s30-at-a-feast-the-clean.jpeg", "seg": "n10",
        "window": "162.55-169.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["STEWARD", "HALL"],
        "narration": (
            "At a king's feast, the clean festival robe was the king's to give, "
            "handed to every guest at the door."
        ),
        "must_show": "SCRIPTURE-CONTEXT: the robe chest — the steward at the great carved chest beside the door, lifting folded gold robes out one after another into arriving guests' arms.",
        "must_not_show": "no halo, glare or rim-light; the chest DEEP with robes — provision that cannot run out; the handing gracious and quick.",
        "scene": (
            "Beside the doorway the great carved robe chest "
            "stands open and deep — folded gold festival "
            "robes stacked past its rim — and the steward "
            "works it with practised joy, shaking each robe "
            "out of its fold and laying it into the next "
            "guest's astonished arms: the labourer receiving "
            "his like a man being paid in advance, the "
            "mother's hand testing the cloth's unbelievable "
            "weight. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r043-b31", "out": "s31-every-person-in-that-hall.jpeg", "seg": "n10 + n11",
        "window": "169.53-176.04", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "HALL"],
        "narration": (
            "Every person in that hall was wearing something the king had put "
            "on them. Then the king came in to meet his guests."
        ),
        "must_show": "SCRIPTURE-EXACT: the king entering — the hall rising to its feet in a golden wave as the king comes in among his roads-born guests, delight restored to his face.",
        "must_not_show": "no halo, glare or rim-light; the rising wave of gold — a hall of the poor standing dressed like princes as the giver walks in.",
        "scene": (
            "The hall rises as the king enters, the camera mid-hall "
            "behind the standing guests' shoulders — a wave of "
            "deep gold robes standing up table by table down "
            "the lamplit length — and he walks in among them "
            "with his arms half-open, his great bearded face "
            "restored fully to its native delight, gripping "
            "the labourer's shoulder, bending to the old "
            "beggar's bow to raise him back up — a king "
            "meeting a hall full of people wearing his own "
            "generosity. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r043-b32", "out": "s32-and-he-found-one-man.jpeg", "seg": "n11",
        "window": "176.04-181.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING", "GUEST", "HALL"],
        "narration": (
            "And he found one man still in his own dusty road clothes. Not "
            "because he was too poor."
        ),
        "must_show": "SCRIPTURE-EXACT: the exception — amid the sea of gold, one man in slate-grey road clothes at the table, chin high; the king stopped before him.",
        "must_not_show": "no halo, glare or rim-light; the grey against the gold is the composition — and the man's chin is UP: pride, not poverty.",
        "scene": (
            "Down the golden hall the king has stopped: at "
            "the table before him, alone in the sea of "
            "festival gold, one lean man sits in his own "
            "dusty slate-grey road clothes with his frayed "
            "cloak still on his shoulders and his chin "
            "carried high — not shrinking, not ashamed, "
            "wearing his own clothes at a king's feast the "
            "way other men wear a flag. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b33", "out": "s33-everyone-there-was-too-poor.jpeg", "seg": "n11",
        "window": "181.49-188.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["GUEST", "STEWARD", "HALL"],
        "narration": (
            "Everyone there was too poor. Because he had been handed a robe at "
            "the door, and had said no to it."
        ),
        "must_show": "the refusal remembered — the flashback beat at the door: the steward offering the folded gold robe, and the grey man's flat palm declining it, walking past.",
        "must_not_show": "no halo, glare or rim-light; the declining palm — the one gesture the whole judgment rests on, shown plainly.",
        "scene": (
            "At the doorway's robe chest the moment replays: "
            "the steward holds the folded gold robe out in "
            "both hands, half-shaken from its fold — and the "
            "lean grey-clad man is already walking past it, "
            "one flat palm raised sideways in refusal, his "
            "high chin leading him into the hall in his own "
            "clothes — the only no spoken at a door that "
            "asked nothing else of anyone. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b34", "out": "s34-friend-how-camest-thou-in.jpeg", "seg": "jv12",
        "window": "188.84-192.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING", "GUEST"],
        "narration": "Friend, how camest thou in hither not having a wedding garment?",
        "must_show": "SCRIPTURE-EXACT: the gentle question — close on the king's face asking it, and the word 'Friend' visibly in it: sorrow, openness, a door still ajar.",
        "must_not_show": "no halo, glare or rim-light; NO rage — the question genuinely open; the king wants an answer that saves the man.",
        "scene": (
            "A close two-shot in the lamplight: the king bent "
            "slightly toward the seated grey-clad man, his "
            "great face carrying the question with more "
            "sorrow than anger — brows lifted, eyes open and "
            "waiting, the word 'Friend' still shaping his "
            "mouth — a judge offering the defendant the pen "
            "to write his own pardon. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b35", "out": "s35-friend-that-is-what-the.jpeg", "seg": "n12",
        "window": "194.03-198.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": "Friend. That is what the king called him. Not intruder.",
        "must_show": "the word weighed — the king's face alone, the kindness of 'Friend' held in it against everything the man deserved to be called.",
        "must_not_show": "no halo, glare or rim-light; the mercy IN the address — one word's worth of open door on one face.",
        "scene": (
            "The king's face alone in the warm light, close: "
            "the heavy brows gentled, the deep eyes resting "
            "on the unseen man with a patience that has "
            "outlived its own hurt twice tonight already — "
            "the face of a host who has been refused by a "
            "city and betrayed by a guest list, still "
            "choosing, on the last insult of the evening, "
            "the word 'Friend'. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b36", "out": "s36-not-thief-friend-and-a.jpeg", "seg": "n12",
        "window": "198.94-205.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING", "GUEST"],
        "narration": (
            "Not thief. Friend, and a question, and every chance in the world "
            "to answer."
        ),
        "must_show": "the chance extended — the space between the two men held open: the king waiting, hand slightly lifted; the pause where any answer would have been heard.",
        "must_not_show": "no halo, glare or rim-light; the WAIT painted — a genuinely open moment, its emptiness the man's own choice.",
        "scene": (
            "The frame holds the space between them: the king "
            "standing with one hand slightly lifted and open, "
            "palm loose — the posture of a man still ready to "
            "receive anything — and across the small lamplit "
            "gap the grey-clad man with his eyes fixed "
            "forward and his mouth a flat proud line, "
            "spending the widest chance of his life on "
            "silence. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r043-b37", "out": "s37-and-the-man-had-nothing.jpeg", "seg": "n12",
        "window": "205.80-208.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["GUEST"],
        "narration": "And the man had nothing to say.",
        "must_show": "SCRIPTURE-EXACT: speechless — close on the grey man's face: the pride holding, the mouth shut, the emptiness behind the eyes where an answer should be.",
        "must_not_show": "no halo, glare or rim-light; speechlessness as CHOICE — the shut mouth of pride, not the failure of wit.",
        "scene": (
            "Close on the lean man's face in the lamplight: "
            "the chin still high, the short dark beard "
            "framing a mouth pressed shut and staying shut, "
            "the guarded eyes aimed past the king at nothing "
            "— and behind them, visible through the pride "
            "like stones through clear water, no answer at "
            "all: a silence he is choosing with every second "
            "it lasts. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r043-b38", "out": "s38-he-had-come-to-the.jpeg", "seg": "n13",
        "window": "208.69-214.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["GUEST", "HALL"],
        "narration": (
            "He had come to the feast and refused the one thing that made him a "
            "guest. So he ended up where he had chosen to be."
        ),
        "must_show": "the logic of the exit — the grey man rising from the table on his own stiff dignity as two servants approach; around him the gold hall he refused to join.",
        "must_not_show": "no halo, glare or rim-light; he rises HIMSELF — the choice completing itself; the servants escort, they do not drag.",
        "scene": (
            "The grey-clad man rises from the bench on his "
            "own stiff dignity as two servants come quietly "
            "along the table — his chin still high, his "
            "frayed cloak gathered around him like a "
            "verdict he wrote himself — and on every side "
            "the golden hall he sat inside and never joined "
            "goes on shining around his grey, self-chosen "
            "island. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r043-b39", "out": "s39-back-outside-in-the-dark.jpeg", "seg": "n13",
        "window": "214.97-220.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["GUEST", "HALL"],
        "narration": (
            "Back outside, in the dark, away from a light that had been "
            "standing wide open for him."
        ),
        "must_show": "⚑ Flags J,L: DARKNESS ONLY — the man standing outside in the plain night, and behind him the hall's doorway still WIDE OPEN and warm; the darkness is only distance from a light that never shut.",
        "must_not_show": "no halo, glare or rim-light; NO pit, NO flames, NO chains emphasized — night, grass, and an open warm door at his back; grief, not horror.",
        "scene": (
            "Outside on the dark hillside grass the grey-clad "
            "man stands alone in the plain night, arms "
            "folded, face turned away into the dark — and "
            "behind him, casting its long warm rectangle of "
            "light down the steps and across the grass to "
            "the very edge of his shadow, the hall's great "
            "doorway stands exactly as open as it stood all "
            "evening — the darkness around him nothing but "
            "the distance he keeps from it. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b40", "out": "s40-bind-him-hand-and-foot.jpeg", "seg": "jv13",
        "window": "221.48-226.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["GUEST", "HALL"],
        "narration": (
            "Bind him hand and foot, and take him away, and cast him into outer "
            "darkness."
        ),
        "must_show": "SCRIPTURE-EXACT, RESTRAINED: the sentence executed as sorrow — the two servants walking the man away down the dark slope, his wrists loosely corded, their heads bowed; the door's light shrinking behind.",
        "must_not_show": "no halo, glare or rim-light; the cord LOOSE, the escort GRIEVED, the darkness ONLY darkness — no violence, no struggle, no pit.",
        "scene": (
            "Down the dark slope away from the light the two "
            "servants walk the grey-clad man between them, "
            "his wrists loosely corded before him, all three "
            "heads bowed — the escort's grief as plain as "
            "the prisoner's pride — while behind and above "
            "them the hall's warm doorway shrinks to a "
            "bright small rectangle in the night, still "
            "open, growing only farther. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b41", "out": "s41-the-men-listening-knew-exactly.jpeg", "seg": "n14",
        "window": "228.45-231.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE"],
        "narration": "The men listening knew exactly who the story was about.",
        "must_show": "the recognition — close on the hostile front rank's faces: the story landed, the parallel understood, fury and fear moving under the composure.",
        "must_not_show": "no halo, glare or rim-light; controlled faces cracking — recognition as a weather front behind the eyes.",
        "scene": (
            "Close along the hostile front rank in the temple "
            "light: the older man's cold appraisal has gone "
            "rigid, a muscle standing in his jaw; the young "
            "scribe's quick eyes have stopped moving "
            "entirely; a third man's hand has closed slowly "
            "on the fringe of his own shawl — three composed "
            "faces holding still while the story finds its "
            "addresses inside them. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b42", "out": "s42-they-were-the-invited-guests.jpeg", "seg": "n14",
        "window": "231.19-238.26", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE"],
        "narration": (
            "They were the invited guests, the ones who had said yes for a "
            "lifetime and would not come when the King actually arrived."
        ),
        "must_show": "the parallel drawn — Jesus and the robed men facing one another across the temple paving: the King arrived, the invited declining, the parable standing live in the room.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the geometry repeats the story — invitation standing in front of refusal.",
        "scene": (
            "Across the bright temple paving the parable "
            "stands enacted: Jesus facing the rank of "
            "fine-robed men — a lifetime of yeses arrayed in "
            "fringed shawls, declining in real time the King "
            "standing in front of them — while at the "
            "edges the ordinary crowd, the roads-people of "
            "this telling, press closer to him than the "
            "invited will ever come. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b43", "out": "s43-but-do-not-miss-what.jpeg", "seg": "n14 + jv14",
        "window": "238.26-244.11", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE"],
        "narration": (
            "But do not miss what the story is really doing. For many are "
            "called, but few are chosen."
        ),
        "must_show": "the saying given — close on Jesus delivering the closing line quietly, the weight of it meant for everyone in earshot including the hunters.",
        "must_not_show": "no halo, glare or rim-light on Jesus; quiet delivery — a line placed gently on every hearer alike.",
        "scene": (
            "Close on Jesus in the temple light as the "
            "closing line goes out quietly — his voice "
            "visibly lowered in the set of his mouth, his "
            "gaze travelling without hurry across hostile "
            "rank and ordinary crowd alike, placing the same "
            "sentence gently on every hearer in the court, "
            "hunters included — a line offered, not thrown. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r043-b44", "out": "s44-everyone-is-invited-that-is.jpeg", "seg": "n15",
        "window": "245.63-248.49", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROADS", "HALL"],
        "narration": "Everyone is invited. That is the whole world.",
        "must_show": "⚑ Flag J,L: the universal call — the widest frame: lantern-bearing servants spreading out along ALL THREE highways into the night, lights strung to the horizon.",
        "must_not_show": "no halo, glare or rim-light; the lights going EVERYWHERE — invitation as geography.",
        "scene": (
            "From above the crossroads at night the camera takes in "
            "the whole errand, lantern strings moving away from "
            "the junction: the whole "
            "errand shows itself: strings of servants' "
            "lanterns moving out along all three dark "
            "highways at once, warm points spreading toward "
            "the horizon in every direction the world has, "
            "pausing at every hedge and ditch and mile-stone "
            "where anyone at all might be — an invitation "
            "with the shape of a map of everywhere. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b45", "out": "s45-the-ones-who-end-up.jpeg", "seg": "n15",
        "window": "248.49-255.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["STEWARD", "HALL"],
        "narration": (
            "The ones who end up at the table are simply the ones who came, and "
            "who let the King put the clean clothes on them."
        ),
        "must_show": "the whole gospel at a doorway — a roads guest standing with arms out as the steward settles the gold robe onto his shoulders; consent, dressing, entry in one motion.",
        "must_not_show": "no halo, glare or rim-light; the guest's arms OUT — the one act asked of anyone: letting it be put on.",
        "scene": (
            "At the robe chest in the doorway light a "
            "road-worn guest stands with his arms held "
            "slightly out from his sides — the universal "
            "posture of being dressed — as the steward "
            "settles the deep gold robe onto his shoulders "
            "from behind and draws it closed over the dust "
            "and the patches — a man doing the only thing "
            "the whole feast ever required of him: standing "
            "still and letting it be put on. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b46", "out": "s46-you-do-not-have-to.jpeg", "seg": "n16",
        "window": "255.89-261.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": (
            "You do not have to make yourself presentable first. Nobody in that "
            "hall could have, and neither can you."
        ),
        "must_show": "the levelling — beneath a table's edge in the golden hall: bare cracked feet and road-worn sandals side by side under royal robes' hems; what everyone still is, underneath.",
        "must_not_show": "no halo, glare or rim-light; the feet unwashed and unashamed — grace covering, not erasing.",
        "scene": (
            "Low beneath the table's edge in the lamplit "
            "hall: a row of feet beneath the golden hems — "
            "bare cracked heels, a labourer's split sandals, "
            "an old man's road-bent toes — every pair still "
            "exactly what the highways made them, resting "
            "easy on the king's smooth stone beneath the "
            "robes he threw over all of it. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b47", "out": "s47-the-invitation-is-free-the.jpeg", "seg": "n16",
        "window": "261.73-269.22", "wide": False, "jesus": False, "ref": False,
        "locks": ["STEWARD", "HALL"],
        "narration": (
            "The invitation is free, the door is open, and the clean clothes "
            "are already bought and folded and waiting inside."
        ),
        "must_show": "the standing offer — the hall doorway wide open to the night, the steward at his chest of folded robes beside it, one robe already lifted and ready; everything prepared, nobody yet arrived.",
        "must_not_show": "no halo, glare or rim-light; the readiness aimed at the VIEWER's dark — door, light, robe, waiting.",
        "scene": (
            "The great doorway stands wide open to the dark "
            "night, its warm light laid down the steps like "
            "a path — and just inside, the plum-clad steward "
            "waits beside the deep carved chest with one "
            "gold robe already lifted free of its fold, "
            "held ready across both arms, his kind face "
            "turned toward the darkness outside where "
            "footsteps might come from — everything bought, "
            "everything folded, everything on. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r043-b48", "out": "s48-all-you-have-to-do.jpeg", "seg": "n16",
        "window": "269.22-272.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": "All you have to do is come in, and let him dress you.",
        "must_show": "the closing image — from OUTSIDE in the dark, the open doorway's warm light, the robe held out toward the threshold, and one empty step at the bottom, waiting for a foot.",
        "must_not_show": "no halo, glare or rim-light; the viewer's own position in the dark, the first step lit — the whole gospel one pace wide.",
        "scene": (
            "From out in the night looking in: the wedding "
            "hall's doorway burns warm and open at the top "
            "of its worn steps, the steward's held-out gold "
            "robe just visible within, the feast's light and "
            "noise soft behind it — and at the bottom of the "
            "steps, lit by the door's long reach into the "
            "dark, the first stone stands empty and waiting, "
            "exactly one footstep away from where the "
            "picture is seen. Every figure has two arms, two "
            "hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "HALL": "PLACE-REF/hall.jpeg",  # build-22-unmerciful-servant v2-r022-b16 (manual)
    "ROADS": "PLACE-REF/roads.jpeg",  # build-31-ten-virgins v2-r031-b11
    "TEMPLE": "PLACE-REF/temple.jpeg",  # build-06-two-sons v2-r006-b21
}
# === end PLACE-PLATES ===
