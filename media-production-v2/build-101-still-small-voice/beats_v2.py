#!/usr/bin/env python3
"""V2 beat map — row 101, build-101-still-small-voice (1 Kings 19:1-18).

COVERAGE: 28 pictures over 161.1 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (1 Kings 19 KJV):
  v3-4  after Carmel's victory, one threat (Jezebel's) sends Elijah
        fleeing; "a day's journey into the wilderness... sat down
        under a JUNIPER TREE: and he requested for himself that he
        might DIE."
  v5-7  he sleeps; provision comes: "a CAKE BAKEN ON THE COALS, and a
        CRUSE OF WATER at his head" — TWICE; "the journey is too
        great for thee." (The narration keeps the provider unseen —
        NO angel is painted; the provision simply IS there.)
  v8    "went in the strength of that meat FORTY DAYS... unto HOREB
        the mount of God"; v9 "he came thither unto A CAVE, and
        lodged there."
  v9,13 the question, twice: "WHAT DOEST THOU HERE, ELIJAH?"
  v10,14 his answer, twice: "I, EVEN I ONLY, AM LEFT; and they seek
        my life."
  v11-12 the theophany: GREAT STRONG WIND rending mountains and
        breaking rocks — the LORD not in it; EARTHQUAKE — not in it;
        FIRE — not in it; "and after the fire A STILL SMALL VOICE."
  v13   "he WRAPPED HIS FACE IN HIS MANTLE, and went out, and stood
        in the entering in of the cave."
  v15-18 he is sent BACK with work and people; "I have left me SEVEN
        THOUSAND in Israel... which have not bowed unto Baal."

GOD RENDERING (CONTENT-CARE law): the LORD is NEVER embodied — no
figure, face, shape or silhouette in wind, quake, fire, or voice; the
forces are natural forces; the still small voice is carried entirely
by Elijah's listening. NO angel figure anywhere (provision passive).

TIME OF DAY ARC (intentional): harsh bright wilderness day for the
flight and the bush; the desert provision at dusk and dark; Horeb's
cave and theophany in cold grey mountain light; the whisper and the
sending in a clean still dawn. Correct story lighting, not the row-11
defect.

CHANGING CONDITION (kept OUT of the locks): Elijah — spent and
suicidal, fed, walking, hidden, drawn out, re-commissioned; the
mountain — torn, shaken, burned, then utterly still.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream (he does not appear in this row).
LOCKS = {
    "ELIJAH": (
        "ELIJAH LOCK: Elijah is the same man in every shot — about "
        "sixty, lean and weathered hard as driftwood, wild grey-"
        "streaked dark hair and beard, in a rough DARK CAMEL-BROWN "
        "hair MANTLE over a CHARCOAL tunic with a wide leather belt "
        "(never cream, never white); a prophet's intensity worn down "
        "to exhaustion and built back."
    ),
    "WILD": (
        "WILD LOCK: the southern wilderness — pale broken badlands "
        "under an enormous sky, drifted sand and shattered stone, "
        "one lone dark JUNIPER BUSH the only shade in miles. The "
        "same waste and bush throughout."
    ),
    "HOREB": (
        "HOREB LOCK: the mount of God — a high raw granite shoulder "
        "above the clouds' level, wind-scoured ledges, and ONE dark "
        "CAVE MOUTH opening onto a stone terrace; cold grey light. "
        "The same cave, terrace and crags throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r101-b01", "out": "s01-elijah-had-just-won-the.jpeg", "seg": "n1",
        "window": "0.28-3.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH"],
        "narration": "Elijah had just won the greatest victory of his life.",
        "must_show": "the victory's afterimage — Elijah on a height in dramatic light, mantle wind-whipped, the bearing of a man at his life's summit; triumph still on him.",
        "must_not_show": "no embodied divine figure; no halo, glare or rim-light; the triumph in POSTURE — fire and slaughter of Carmel NOT depicted.",
        "scene": (
            "On a high ridge in the wind "
            "the prophet stands at the top "
            "of his life: mantle snapping "
            "like a war banner, wild hair "
            "streaming, the lean weathered "
            "frame drawn up to its full "
            "height with the greatest day "
            "he will ever have still "
            "blazing in his face — a man "
            "who called down the answer "
            "in front of a nation and "
            "watched heaven take his side, "
            "standing one sunset from the "
            "bottom. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r101-b02", "out": "s02-and-then-a-single-threat.jpeg", "seg": "n1",
        "window": "3.23-12.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "WILD"],
        "narration": (
            "And then a single threat sent him running for the wilderness, "
            "until he sank down under a lone bush, worn out and afraid, and "
            "asked God to let him die."
        ),
        "must_show": "SCRIPTURE-EXACT: the collapse at the juniper — Elijah sunk under the lone bush in the vast pale waste, spent flat, the death-wish in his ruined posture.",
        "must_not_show": "no embodied divine figure, no halo; the collapse TOTAL and dignified — a great man emptied, not a coward cartooned.",
        "scene": (
            "The wilderness receives what "
            "the threat made of him: under "
            "the one dark juniper in miles "
            "of pale broken waste the "
            "prophet lies sunk against the "
            "sand, mantle dragged over "
            "him, the driftwood frame "
            "utterly spent — the man who "
            "outran a king's chariot "
            "yesterday asking today, into "
            "the dirt, for the one thing "
            "left he has strength to "
            "want: an end. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r101-b03", "out": "s03-god-did-not-scold-him.jpeg", "seg": "n2",
        "window": "13.06-14.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "WILD"],
        "narration": "God did not scold him.",
        "must_show": "the non-scolding — the sleeping prophet under the bush in gentling dusk light; the frame itself tender around his exhaustion; no rebuke anywhere in the world.",
        "must_not_show": "no embodied divine figure, no halo; the tenderness ATMOSPHERIC — light and stillness as mercy.",
        "scene": (
            "And the answer to the "
            "death-prayer is — sleep: the "
            "prophet under the juniper in "
            "the day's gentling dusk, "
            "breathing slow at last, the "
            "harsh light gone soft gold "
            "and rose across the waste — "
            "no thunder over the bush, no "
            "voice of correction, no "
            "ledger of his failure read "
            "into the evening — heaven's "
            "first response to a broken "
            "servant being simply to let "
            "him rest. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r101-b04", "out": "s04-twice-he-was-fed-and.jpeg", "seg": "n2",
        "window": "19.88-24.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "WILD"],
        "narration": (
            "Twice he was fed, and gently told the journey was too great "
            "for him to make alone."
        ),
        "must_show": "SCRIPTURE-EXACT: the second provision — Elijah risen on an elbow eating the coal-baked bread in the firelight-dark, the water cruse in hand; strength returning bite by bite.",
        "must_not_show": "ABSOLUTE: no angel or figure — the provision present, its bringer unseen; no halo.",
        "scene": (
            "In the desert dark he eats "
            "what keeps arriving: risen "
            "on one elbow under the "
            "juniper, tearing the warm "
            "coal-baked cake with his "
            "fingers, the clay cruse "
            "tipped to his cracked lips — "
            "the little coal-bed's ember "
            "light on a face coming back "
            "from the edge — fed twice "
            "by hands he never sees, on "
            "bread he never asked for, "
            "against a journey he does "
            "not yet know he is taking. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r101-b05", "out": "s05-while-he-slept-warm-bread.jpeg", "seg": "n2",
        "window": "14.62-19.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "WILD"],
        "narration": (
            "While he slept, warm bread was baked for him and a jar of "
            "water set by his head."
        ),
        "must_show": "SCRIPTURE-EXACT: cake on the coals, cruse at his head — close on the sleeping prophet's head, and beside it: the small coal-bed with its baking cake, the water jar set carefully near.",
        "must_not_show": "ABSOLUTE: no angel or figure anywhere — the provision simply THERE, steam rising, placed with unseen care; no halo.",
        "scene": (
            "Close on the miracle at its "
            "most domestic: the sleeping "
            "prophet's wild grey head "
            "heavy in the sand — and set "
            "by it, close enough to smell, "
            "a small bed of desert coals "
            "with a flat cake baking "
            "golden on the hot stones, "
            "steam curling into the dusk, "
            "and a clay jar of water "
            "placed carefully upright by "
            "his pillow of ground — "
            "supper, appearing in the "
            "wilderness the way dew does, "
            "from nowhere anyone saw. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r101-b06", "out": "s06-in-that-strength-he-walked.jpeg", "seg": "n3",
        "window": "25.27-34.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": (
            "In that strength he walked forty days across the wilderness, "
            "all the way to the mountain of God, and found a cave, and went "
            "in, and stayed there in the dark."
        ),
        "must_show": "SCRIPTURE-EXACT: forty days to Horeb — the tiny walking figure crossing vast country toward the high grey mountain; then the cave mouth taking him into its dark.",
        "must_not_show": "no embodied divine figure, no halo; the scale VAST — one small mantle-dark figure against mountain and waste.",
        "scene": (
            "The bread carries him further "
            "than despair ever could: a "
            "small mantle-dark figure "
            "crossing badland after "
            "badland toward the high raw "
            "granite of the mount of God, "
            "day folded on day in one "
            "walking frame — until the "
            "grey shoulder of Horeb "
            "receives him at last at a "
            "black cave mouth on a stone "
            "terrace, and the prophet "
            "steps out of the light and "
            "into the mountain's dark, "
            "and stays. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r101-b07", "out": "s07-what-doest-thou-here-elijah.jpeg", "seg": "jv9",
        "window": "34.70-36.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": "What doest thou here, Elijah?",
        "must_show": "SCRIPTURE-EXACT: the question in the dark — Elijah in the cave's blackness, head lifting sharply at a voice with no speaker; the question rendered entirely by his hearing.",
        "must_not_show": "ABSOLUTE: no figure, face, shape or light-form as the voice — the cave dark and empty around one listening man.",
        "scene": (
            "In the cave's absolute dark "
            "the question finds him: the "
            "prophet's wild grey head "
            "jerking up from his knees, "
            "eyes wide against blackness "
            "that holds nothing to see — "
            "WHAT DOEST THOU HERE, "
            "ELIJAH — a voice with no "
            "throat, no direction and no "
            "echo, arriving inside the "
            "mountain's silence the way "
            "his own name might, and the "
            "whole scene of it played on "
            "one lifted listening face. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r101-b08", "out": "s08-i-have-been-very-jealous.jpeg", "seg": "s10",
        "window": "38.14-53.32", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": (
            "I have been very jealous for the LORD God of hosts: for the "
            "children of Israel have forsaken thy covenant, thrown down "
            "thine altars, and slain thy prophets with the sword; and I, "
            "even I only, am left; and they seek my life, to take it away."
        ),
        "must_show": "SCRIPTURE-EXACT: the complaint poured out — Elijah at the cave mouth's grey half-light, the whole grievance leaving him: hands, face, body all argument.",
        "must_not_show": "no embodied divine figure, no halo; the pouring HONEST — bitterness, devotion and fear all in it.",
        "scene": (
            "It pours out of him at the "
            "cave mouth's grey edge: "
            "hands flying, the mantle "
            "shaken, the lean face "
            "working through every count "
            "of the indictment — jealous "
            "FOR THEE, the covenants "
            "forsaken, the altars down, "
            "the prophets dead — and "
            "then, arriving where every "
            "grievance was always headed, "
            "the sore heart of it: I, "
            "EVEN I ONLY, AM LEFT — a "
            "faithful man's whole "
            "loneliness, itemised into "
            "the listening dark. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r101-b09", "out": "s09-i-have-given-everything-for.jpeg", "seg": "n4",
        "window": "56.30-58.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH"],
        "narration": "I have given everything for you, he said.",
        "must_show": "the cost shown — close on Elijah's spent face and worn hands open before him: a life's whole expenditure held up as evidence.",
        "must_not_show": "no embodied divine figure, no halo; the claim TRUE — the wear on him is real and visible.",
        "scene": (
            "Close on the evidence he "
            "holds up: two worn hands "
            "open before a face that has "
            "spent itself to the walls — "
            "the sun-split knuckles, the "
            "fast-hollowed cheeks, the "
            "eyes that have carried a "
            "nation's apostasy alone for "
            "years — EVERYTHING, the "
            "hands say, and it is true, "
            "and it is the truest part "
            "of the complaint, and even "
            "true things can see only "
            "half the field. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r101-b10", "out": "s10-and-out-it-all-poured.jpeg", "seg": "n4",
        "window": "54.92-56.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": "And out it all poured.",
        "must_show": "the flood — Elijah mid-outpouring at the cave mouth, everything held for years leaving at once; grief given full permission.",
        "must_not_show": "no embodied divine figure, no halo; the outpouring PERMITTED — no interruption, the dark receiving all of it.",
        "scene": (
            "The dam gives way all at "
            "once: years of held-alone "
            "faithfulness leaving the "
            "prophet in one flood at the "
            "cave's grey mouth — voice "
            "cracking, fists knotting the "
            "mantle, the wild head "
            "bowing and rearing — and "
            "around the pouring, "
            "unhurried and unoffended, "
            "the mountain's great "
            "listening dark taking every "
            "word without once cutting "
            "him off — grief granted the "
            "full floor of Horeb. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r101-b11", "out": "s11-i-am-the-only-one.jpeg", "seg": "n4",
        "window": "58.91-62.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH"],
        "narration": "I am the only one left, and now they want me dead too.",
        "must_show": "the loneliness stated — close on the face at the complaint's core: ONLY ONE LEFT; isolation total in the eyes, the hunted look under it.",
        "must_not_show": "no embodied divine figure, no halo; the fear DIGNIFIED — a brave man's honest terror, not cowardice.",
        "scene": (
            "Close on the complaint's "
            "sore centre: the prophet's "
            "eyes as he says ONLY — the "
            "conviction absolute in "
            "them, a man certain he is "
            "the last light burning in a "
            "nation gone dark, and under "
            "the conviction the hunted "
            "animal flicker of someone "
            "who knows there is a price "
            "on the light — the loneliest "
            "sentence in the Old "
            "Testament, believed utterly "
            "by its speaker, and wrong. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r101-b12", "out": "s12-go-forth-and-stand-upon.jpeg", "seg": "jv11a",
        "window": "63.19-66.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": "Go forth, and stand upon the mount before the LORD.",
        "must_show": "SCRIPTURE-EXACT: the summons out — Elijah stepping from the cave's dark onto the wind-scoured terrace, mantle gathered, summoned to stand; the crags waiting.",
        "must_not_show": "ABSOLUTE: no figure or form as the LORD — the summons obeyed toward empty grey vastness; no halo.",
        "scene": (
            "The summons draws him out of "
            "the mountain: Elijah "
            "stepping from the cave's "
            "black onto the bare stone "
            "terrace, mantle gathered at "
            "his throat, grey light "
            "flooding his squint — GO "
            "FORTH, AND STAND — and "
            "before him nothing but the "
            "raw crags and the enormous "
            "cold sky of Horeb, empty to "
            "every horizon and about to "
            "be less empty than any "
            "ground he has ever stood "
            "on. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r101-b13", "out": "s13-and-behold-the-lord-passed.jpeg", "seg": "jv11c",
        "window": "68.12-77.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": (
            "And, behold, the LORD passed by, and a great and strong wind "
            "rent the mountains, and brake in pieces the rocks before the "
            "LORD; but the LORD was not in the wind:"
        ),
        "must_show": "SCRIPTURE-EXACT: the rending wind — the terrace scoured by a colossal wind: dust and grit sheeting, rocks splitting and tumbling from the crags, Elijah braced flat against the cave's lip.",
        "must_not_show": "ABSOLUTE: no figure, face or form in the wind — pure force; Elijah holding on, not blown into peril's cartoon.",
        "scene": (
            "The mountain meets a wind "
            "with hands: a colossal "
            "scouring blast sheeting the "
            "terrace with dust and "
            "driven grit, whole slabs "
            "splitting off the crags "
            "above and going down the "
            "slopes in thunder, the "
            "juniper-tough prophet "
            "braced flat against the "
            "cave's lip with his mantle "
            "cracking like a sail — a "
            "wind that tears mountains "
            "apart passing BY, and the "
            "One it announces, not in "
            "it. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r101-b14", "out": "s14-and-after-the-wind-an.jpeg", "seg": "jv11b",
        "window": "78.70-82.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": (
            "and after the wind an earthquake; but the LORD was not in the "
            "earthquake:"
        ),
        "must_show": "SCRIPTURE-EXACT: the earthquake — the terrace heaving: cracks running the stone, boulders dancing, dust jumping off every ledge; Elijah thrown to hands and knees.",
        "must_not_show": "ABSOLUTE: no figure or form in the quake — force only; Elijah down but unharmed.",
        "scene": (
            "The wind's wake is worse: "
            "the whole shoulder of Horeb "
            "HEAVES, cracks running live "
            "across the terrace stone, "
            "boulders jolting and "
            "walking, dust leaping off "
            "every ledge at once — the "
            "prophet thrown to hands and "
            "knees with the mountain "
            "bucking under his palms "
            "like a ship's deck — the "
            "earth itself shaken by the "
            "passing, and the One who "
            "passes, not in the "
            "shaking either. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r101-b15", "out": "s15-a-wind-strong-enough-to.jpeg", "seg": "n5",
        "window": "84.49-86.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOREB"],
        "narration": "A wind strong enough to tear the mountain apart.",
        "must_show": "the wind's work close — a great split boulder freshly torn, raw bright rock at the break, grit still streaming past; the aftermath testifying to the force.",
        "must_not_show": "ABSOLUTE: no figure in or behind the force; the evidence GEOLOGIC — broken stone, streaming dust.",
        "scene": (
            "Close on what the wind did "
            "to solid granite: a boulder "
            "the size of a house lying "
            "torn in two, the break's "
            "raw faces bright and "
            "unweathered against the old "
            "grey stone, grit still "
            "streaming sideways past the "
            "wound in long ribbons — "
            "the mountain's own flesh "
            "opened by moving air, left "
            "as evidence of how much "
            "power went past without "
            "carrying what it announced. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r101-b16", "out": "s16-then-an-earthquake-that-split.jpeg", "seg": "n5",
        "window": "86.71-92.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": (
            "Then an earthquake that split the rock under his feet. Then a "
            "fire sweeping across the stone."
        ),
        "must_show": "SCRIPTURE-EXACT: the fire — sheets of flame sweeping the broken terrace stone, orange light hammering the crags; Elijah shielded at the cave lip, lit and awed.",
        "must_not_show": "ABSOLUTE: no figure or form in the fire — natural flame across stone; Elijah safe at the cave's edge.",
        "scene": (
            "And after the shaking, "
            "burning: sheets of flame "
            "sweeping low and fast "
            "across the quake-cracked "
            "terrace, orange light "
            "hammering the raw crags "
            "and pouring into every new "
            "crack, heat-shimmer bending "
            "the cold air — the prophet "
            "pressed into the cave's lip "
            "with an arm flung up, face "
            "striped in firelight, "
            "watching the third and "
            "loudest herald sweep past "
            "as empty of God as the "
            "first two. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r101-b17", "out": "s17-surely-god-would-be-in.jpeg", "seg": "n5",
        "window": "92.40-97.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": (
            "Surely God would be in something that big. But he was not in "
            "any of them."
        ),
        "must_show": "the expectation failing — close on Elijah's fire-lit, dust-caked face searching the passing spectacle for a presence and not finding it; bafflement growing.",
        "must_not_show": "ABSOLUTE: no figure or form; the absence carried in HIS searching eyes.",
        "scene": (
            "Close on a prophet's theology "
            "coming up empty: the "
            "dust-caked, fire-lit face "
            "searching each colossus as "
            "it passes — the wind, "
            "surely; the quake, surely; "
            "the fire, SURELY — and "
            "finding in every one of "
            "them force and force and "
            "force and no one there — "
            "the bafflement of a man "
            "who has served thunder all "
            "his life, watching thunder "
            "turn out to be only the "
            "escort. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r101-b18", "out": "s18-and-after-the-fire-a.jpeg", "seg": "jv12",
        "window": "98.01-100.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": "And after the fire a still small voice.",
        "must_show": "SCRIPTURE-EXACT: the stillness — the terrace utterly quiet: smoke thinning, dust settling, the crags at rest; Elijah's head turning at something below hearing.",
        "must_not_show": "ABSOLUTE: no figure, form or visible source — the voice exists ONLY in his turned, arrested listening.",
        "scene": (
            "And then the mountain runs "
            "out of spectacle: smoke "
            "thinning off the blackened "
            "stone, the last dust "
            "sifting down, the crags "
            "standing spent in a silence "
            "deeper than before the wind "
            "— and into that emptied "
            "quiet, below hearing, "
            "beneath even the blood in "
            "his own ears, something — "
            "the prophet's head turning "
            "slow, arrested, every sense "
            "leaning toward a voice the "
            "air itself has to hold "
            "still to carry. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r101-b19", "out": "s19-after-all-the-noise-and.jpeg", "seg": "n6",
        "window": "101.95-108.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": (
            "After all the noise and power, everything went quiet. And in "
            "the quiet came a low, gentle whisper."
        ),
        "must_show": "the whisper heard — close on Elijah's listening face in the great stillness: awe of a new kind arriving, softer and heavier than any of the three storms.",
        "must_not_show": "ABSOLUTE: no visible source; the awe GENTLE — eyes wide, breath held, the face of a man being spoken to.",
        "scene": (
            "Close on the listening: the "
            "wild weathered face gone "
            "utterly still in the "
            "stillness, eyes wide at "
            "nothing visible, breath "
            "held so as not to trample "
            "one syllable — and over the "
            "features an awe unlike "
            "anything the wind or fire "
            "raised: softer, heavier, "
            "nearer — the look of a man "
            "discovering that the voice "
            "that made the storms "
            "prefers, when it has "
            "something to say, to "
            "whisper. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r101-b20", "out": "s20-that-was-where-god-was.jpeg", "seg": "n6",
        "window": "108.56-116.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": (
            "That was where God was. Elijah heard it, and wrapped his face "
            "in his cloak, and came to the mouth of the cave to listen."
        ),
        "must_show": "SCRIPTURE-EXACT: the mantle-wrapped standing — Elijah at the cave's entering-in, face wrapped in his dark mantle, standing bowed and reverent in the still grey light.",
        "must_not_show": "ABSOLUTE: no figure or form before him — he bows to empty stillness that is not empty; no halo.",
        "scene": (
            "He answers the whisper the "
            "way no storm could make "
            "him: drawing the rough "
            "camel-hair mantle up and "
            "over his face with both "
            "hands, and coming forward "
            "blind to stand in the "
            "entering-in of the cave — "
            "bowed, wrapped, unseeing by "
            "choice — a man who stood "
            "upright through wind and "
            "quake and fire, covering "
            "his eyes before a quietness, "
            "because THIS one is Him. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r101-b21", "out": "s21-the-whisper-did-not-shame.jpeg", "seg": "n7",
        "window": "117.37-119.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH"],
        "narration": "The whisper did not shame him for being afraid.",
        "must_show": "the no-shame — the mantle-wrapped prophet listening at the threshold: his bowed posture easing, not cringing; received, not rebuked.",
        "must_not_show": "ABSOLUTE: no visible source; his easing VISIBLE — shoulders coming down, the braced-for blow never landing.",
        "scene": (
            "Under the wrapped mantle the "
            "braced shoulders slowly "
            "come down: the prophet at "
            "the threshold waiting for "
            "the deserved thunder about "
            "his running, his despair, "
            "his death-wish under the "
            "bush — and the whisper "
            "spending not one syllable "
            "on any of it — no shame "
            "arriving, no ledger read, "
            "the blow he braced for "
            "simply never coming — a "
            "fear met the way the bread "
            "met his hunger: kindly, and "
            "first. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r101-b22", "out": "s22-it-asked-him-again-what.jpeg", "seg": "n7",
        "window": "119.73-127.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": (
            "It asked him again what troubled him, let him say it all a "
            "second time, and then quietly gave him work to do and people "
            "to go to."
        ),
        "must_show": "the second telling — Elijah at the cave mouth speaking again, calmer now, the mantle lowered from his face; being heard all the way out, then re-tasked.",
        "must_not_show": "ABSOLUTE: no visible source; the CHANGE from the first telling visible — the flood become a report.",
        "scene": (
            "He is allowed to say it all "
            "again: the mantle lowered "
            "now from a calmer face, the "
            "same grievance told a "
            "second time at the cave's "
            "grey mouth — but slower, "
            "steadier, a flood become a "
            "report — heard out to its "
            "last word by the patient "
            "stillness, and then, into "
            "the emptied quiet where the "
            "complaint used to live, "
            "something new arriving: "
            "names, roads, errands — "
            "work. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r101-b23", "out": "s23-he-was-being-sent-back.jpeg", "seg": "n7",
        "window": "127.05-130.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": "He was being sent back, steadied and not alone.",
        "must_show": "the re-commissioning — Elijah straightening at the cave mouth, mantle squared, facing DOWN the mountain the way he came; a man with a road again.",
        "must_not_show": "ABSOLUTE: no visible source; the steadiness NEW — same man, rebuilt bearing.",
        "scene": (
            "The prophet who crawled up "
            "this mountain straightens "
            "at its door: mantle squared "
            "across the driftwood "
            "shoulders, wild head up, "
            "face set DOWN the long way "
            "he came — the same worn "
            "man, rebuilt from the "
            "inside by bread, patience, "
            "a whisper and a job — "
            "turned around on Horeb's "
            "doorstep and aimed back at "
            "the world that scared him "
            "here, steadied, and no "
            "longer keeping his own "
            "count of the faithful. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r101-b24", "out": "s24-yet-i-have-left-me.jpeg", "seg": "jv18",
        "window": "130.95-140.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": (
            "Yet I have left me seven thousand in Israel, all the knees "
            "which have not bowed unto Baal, and every mouth which hath not "
            "kissed him."
        ),
        "must_show": "SCRIPTURE-EXACT: the seven thousand — Elijah at the terrace edge looking out over the vast hazed lands below, the correction landing: the country before him secretly full of the faithful.",
        "must_not_show": "ABSOLUTE: no visible source, no literal crowd conjured — the seven thousand live in the LANDSCAPE and his changed gaze.",
        "scene": (
            "The correction is the size "
            "of the view: from the "
            "terrace edge the whole "
            "hazed country falls away "
            "below him — valleys, far "
            "villages, threads of "
            "smoke — and over it the "
            "whisper lays its arithmetic: "
            "SEVEN THOUSAND — knees "
            "unbowed, mouths unkissed by "
            "the lie, scattered secret "
            "and faithful through every "
            "fold of the land he "
            "thought had emptied — the "
            "loneliest man in Israel "
            "looking out at a country "
            "quietly full of his own "
            "family. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r101-b25", "out": "s25-you-are-not-the-only.jpeg", "seg": "n8",
        "window": "141.84-143.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH"],
        "narration": "You are not the only one, God told him.",
        "must_show": "the sentence landing — close on Elijah's face as the only-one conviction breaks: relief and humility flooding in together.",
        "must_not_show": "ABSOLUTE: no visible source; the breaking GLAD — a wrong belief a man is relieved to lose.",
        "scene": (
            "Close on the gladdest "
            "correction of his life "
            "landing: the ONLY-ONE "
            "conviction — carried so "
            "long it fused to his bones "
            "— breaking up across the "
            "weathered face like ice "
            "off a spring river: relief "
            "flooding the deep eyes, "
            "humility right behind it, "
            "the mouth almost laughing "
            "at the size of his own "
            "miscount — seven thousand — "
            "a man never so happy to "
            "have been wrong. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r101-b26", "out": "s26-scattered-across-the-land-are.jpeg", "seg": "n8",
        "window": "143.77-148.09", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Scattered across the land are thousands who have never bent "
            "the knee to the lie."
        ),
        "must_show": "the hidden faithful — a warm village-evening frame in the land below: ordinary households at ordinary duties, small oil lamps in windows; faithfulness invisible and everywhere.",
        "must_not_show": "no halo or symbols on anyone — the faithful indistinguishable and ordinary; the lamps plain household lamps.",
        "scene": (
            "Down in the folded country, the camera above a "
            "lane's bend behind the evening walkers, "
            "the seven thousand keep "
            "their unmarked watch: a "
            "village at evening — a "
            "potter shutting his shed, a "
            "grandmother teaching a "
            "child its prayers by one "
            "small window lamp, a farmer "
            "walking home past a "
            "neighbour's untended Baal "
            "post without a nod — "
            "ordinary rooms, ordinary "
            "faces, and in house after "
            "scattered house, knees "
            "that have simply never "
            "bent. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r101-b27", "out": "s27-you-feel-alone-but-you.jpeg", "seg": "n8",
        "window": "148.09-150.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": "You feel alone, but you are not.",
        "must_show": "the truth held — Elijah quiet at the terrace edge in the clean dawn light, the vast peopled land below; solitude re-named company.",
        "must_not_show": "ABSOLUTE: no visible source; the frame PEACEFUL — a man and a horizon that no longer frightens him.",
        "scene": (
            "The prophet stands quiet at "
            "the edge of the height in "
            "the clean first light, the "
            "mantle still, the wild "
            "hair at rest — and below "
            "him the land unrolls with "
            "its hidden thousands "
            "sleeping in its folds — "
            "the same view that this "
            "morning meant exile now "
            "reading as a muster roll — "
            "feeling alone, and standing "
            "corrected, in the gentlest "
            "sense the words have ever "
            "had. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r101-b28", "out": "s28-that-is-how-god-answered.jpeg", "seg": "n8",
        "window": "150.88-160.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELIJAH", "HOREB"],
        "narration": (
            "That is how God answered a tired, frightened man — not with "
            "thunder, but with a whisper, and with the truth that he was "
            "never as alone as he feared."
        ),
        "must_show": "the closing image — Elijah walking down the mountain path in the dawn, steady and re-made, Horeb's cave small above him; the whisper's whole work, walking.",
        "must_not_show": "ABSOLUTE: no visible source, no halo; the descent PURPOSEFUL — a sent man, not a fleeing one.",
        "scene": (
            "The closing frame follows "
            "him down: the mantle-dark "
            "figure descending the "
            "mountain path in the clean "
            "dawn with a steady sent-"
            "man's stride, the cave "
            "mouth shrinking small on "
            "the grey shoulder above — "
            "fed when he wanted death, "
            "heard when he poured it "
            "out, whispered to when he "
            "braced for thunder, and "
            "walking back down into the "
            "world with work in his "
            "hands and seven thousand "
            "reasons he was never "
            "alone. Every figure has "
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
}
# === end PLACE-PLATES ===
