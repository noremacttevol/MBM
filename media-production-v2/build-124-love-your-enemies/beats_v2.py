#!/usr/bin/env python3
"""V2 beat map — row 124, build-124-love-your-enemies (Matthew 5:43-46).

COVERAGE: 30 pictures over 171.8 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 5 KJV):
  5:43  "Ye have heard that it hath been said, Thou shalt love thy
        neighbour, and HATE THINE ENEMY."
  5:44  "But I say unto you, LOVE your enemies, BLESS them that curse
        you, DO GOOD to them that hate you, and PRAY for them which
        despitefully use you" — four verbs, all outbound.
  5:45  "That ye may be the CHILDREN of your Father... for he maketh
        his SUN to rise on the EVIL and on the GOOD, and sendeth RAIN
        on the JUST and on the UNJUST." — the family resemblance.
  5:46  "For if ye love them which love you, what reward have ye? do
        not even the PUBLICANS the same?"
  Setting: the same Sermon on the Mount hillside as rows 121-123 —
  same slope, same lake, same congregation.

RENDERING LAWS:
  - HILLSIDE and CROWD locks are BYTE-IDENTICAL to builds 121-123
    (same sermon, same slope, same congregation) — cross-video
    continuity.
  - The teaching is carried by ONE vignette arc: two farmers across
    one stone wall — grievance, cold standoff, the quiet help when
    the wall falls, the named prayer at night, the unowed gift, and
    the wall become a meeting place. Same two men, same wall, every
    vignette beat — face-board them hard.
  - NEITHER farmer is a villain: the neighbour wronged him, but he
    is rendered as a guarded ordinary man, never a sneering heavy.
    The change in him arrives as SURPRISE, then softening.
  - The sun/rain beats are the doctrine in landscape: ONE light and
    ONE rain lying equally on BOTH farms — the equality must be
    visible (no brighter field, no favored side).
  - Action-logic (Cameron's law): b15's help must read instantly —
    the wronged man lifting the NEIGHBOUR'S stones on the
    neighbour's side of the line; b17-b18 pray FOR, not about —
    openness in the hands and face, no clenched grievance.

TIME OF DAY ARC (intentional): the hillside in the same warm late-
afternoon gold as rows 121-123; the grievance and standoff vignettes
under flat bright day; the wall-mending after GREY RAIN; the prayer
beats at LAMPLIT NIGHT by design; the sun/rain doctrine frames at
morning and in silver rain; the closing wall-meeting at golden
evening.

CHANGING CONDITIONS (kept OUT of the locks): the stone wall — whole,
rain-collapsed at one section, then rebuilt; the two men — cold
backs, then side by side; the light between the farms — divided by
shadow early, one equal light late.
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
    "FARMS": (
        "FARMS LOCK: the two farmsteads — two modest stone "
        "farmhouses on facing slopes of one shallow valley, divided "
        "by a single long DRY-STONE WALL running between their "
        "fields, a shared well near the wall's low point, olive "
        "trees behind each house. The same two houses, wall and "
        "well throughout."
    ),
    "FARMER": (
        "FARMER LOCK: the wronged farmer is the same man in every "
        "shot — about fifty, lean and weather-lined, a short "
        "grey-flecked beard, in a DEEP RUST-BROWN tunic with a dark "
        "cloth belt (never cream, never white); guarded at first, "
        "quietly resolute after."
    ),
    "NEIGHBOUR": (
        "NEIGHBOUR LOCK: the neighbour is the same man in every "
        "shot — heavier-set, about fifty, a full dark beard, in a "
        "DARK SLATE-GREY tunic (never cream, never white); an "
        "ordinary guarded man, never a sneering villain; surprise "
        "and slow softening as the story turns."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r124-b01", "out": "s01-on-a-green-hillside-above.jpeg", "seg": "n1",
        "window": "0.28-7.59", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "On a green hillside above the Sea of Galilee, Jesus sat down to "
            "teach, and a whole countryside climbed up to listen."
        ),
        "must_show": "the gathering — Jesus seated on the slope, the crowd settled thick on the grass and MORE still climbing the paths from below; a countryside converging.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the climbers on the paths headed UP toward him — direction clear.",
        "scene": (
            "The whole countryside is still arriving, the camera "
            "looking past the seated crowd's backs up the green "
            "slope: Jesus seated at the crest in the warm gold "
            "above the blue lake, the grass already thick with "
            "fishermen and families — and below them, dotted up "
            "the worn paths from the shore villages, latecomers "
            "still climbing with children on shoulders and elders "
            "on sticks, every one of them headed up toward the "
            "seated figure the entire valley has rearranged its "
            "day to hear. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r124-b02", "out": "s02-it-felt-fair.jpeg", "seg": "n2",
        "window": "29.75-30.84", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "It felt fair.",
        "must_show": "the agreement — crowd faces nodding along with the old rule: love your own, guard against the rest; comfort in the arithmetic.",
        "must_not_show": "no halo; the nodding EASY and unashamed — this is everyone's default, not villainy.",
        "scene": (
            "The old rule polls well on the hillside: along the "
            "seated rows the heads nod easily — a fisherman's "
            "slow agreeing tilt, an elder's grunt of assent, a "
            "mother pulling her child a half-inch closer at the "
            "word enemy — love your own, keep your guard up "
            "against the rest — arithmetic so old and so "
            "comfortable that nobody on the grass has ever once "
            "audited it, and every nodding face says the books "
            "balance fine. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r124-b03", "out": "s03-he-was-walking-through-the.jpeg", "seg": "n1",
        "window": "7.59-17.42", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "He was walking through the old sayings one at a time — you have "
            "heard it said — and then he came to the hardest one of all: "
            "what to do with an enemy."
        ),
        "must_show": "the working-through — Jesus teaching with fingers counting off the old sayings one at a time, the crowd tracking; the hardest one arriving.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the counting gesture PLAIN — a teacher's tally, one at a time.",
        "scene": (
            "The sermon works down its list in plain sight: Jesus "
            "counting the old sayings off on his fingers one at a "
            "time — ye have heard... ye have heard — each familiar "
            "rule raised and turned over like a coin checked for "
            "true weight, the crowd tracking the tally hand — and "
            "then the counting stops, the hand stilling on the "
            "next finger, the teacher's face changing by one "
            "degree into the gravity of a man arriving at the "
            "hardest saying anyone ever inherited. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b04", "out": "s04-ye-have-heard-that-it.jpeg", "seg": "jv43",
        "window": "18.02-23.26", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Ye have heard that it hath been said, Thou shalt love thy "
            "neighbour, and hate thine enemy."
        ),
        "must_show": "SCRIPTURE-EXACT: the old saying recited — Jesus's hand held flat and level like a man quoting the received line; listeners nodding along with what they have always heard.",
        "must_not_show": "no halo, glare or rim-light on Jesus; his face NEUTRAL in the reciting — the correction not yet arrived.",
        "scene": (
            "The received version is read into the record: Jesus "
            "with one hand held flat and level, palm down — the "
            "posture of a man quoting, not yet teaching — the old "
            "line laid out exactly as everyone learned it at "
            "their father's table, love the neighbour, hate the "
            "enemy — and along the rows the comfortable nods "
            "resume, listeners settling into a saying that has "
            "never once cost any of them anything, while the "
            "teacher's level hand waits to turn. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b05", "out": "s05-everyone-on-that-hillside-knew.jpeg", "seg": "n2",
        "window": "24.77-29.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS", "FARMER", "NEIGHBOUR"],
        "narration": (
            "Everyone on that hillside knew that old arithmetic. Keep your "
            "guard up against the ones who don't."
        ),
        "must_show": "the arithmetic lived — the two farms and the long stone wall between them, the two farmers working their own sides with backs half-turned to each other; guardedness as landscape.",
        "must_not_show": "no halo; neither man a villain — two ordinary guarded men and one dividing wall.",
        "scene": (
            "The old arithmetic has a landscape: two stone "
            "farmhouses on facing slopes of one shallow valley, "
            "and running between their fields the long dry-stone "
            "wall that does their talking for them — on one side "
            "the lean farmer in rust-brown bent to his rows, on "
            "the other the heavier neighbour in slate-grey at his "
            "olives, each with his back half-turned to the wall "
            "and the man beyond it — guard kept, ledger balanced, "
            "not one word crossing the stones. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b06", "out": "s06-it-felt-safe-and-then.jpeg", "seg": "n2",
        "window": "30.84-34.20", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "It felt safe. And then Jesus said this.",
        "must_show": "the turn coming — Jesus drawing the breath before the hard sentence, the crowd's nodding stilled by something in his face.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the pause VISIBLE — the hillside caught between sayings.",
        "scene": (
            "The comfortable nodding runs out of road: Jesus "
            "pauses with the breath for the next sentence "
            "visibly taken and held, his gaze moving once along "
            "the settled rows — and the hillside's easy motion "
            "stills row by row, nods dying mid-tilt, a crowd "
            "reading in the teacher's face that the safe old "
            "arithmetic they have been agreeing with is about to "
            "be reopened, audited, and turned entirely inside "
            "out. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r124-b07", "out": "s07-not-tolerate-them.jpeg", "seg": "n3",
        "window": "47.55-48.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS", "FARMER", "NEIGHBOUR"],
        "narration": "Not tolerate them.",
        "must_show": "what the command is NOT — the two farmers at the shared well managing a stiff, minimal, civil nod; bare tolerance shown as the insufficient thing.",
        "must_not_show": "no halo; the nod COLD and correct — no warmth anywhere yet; this frame is the bar being cleared, not the goal.",
        "scene": (
            "What the sentence does NOT mean is already on offer "
            "at the well: the two farmers arriving from their own "
            "sides for water, exchanging the stiff quarter-nod of "
            "men being civil at the minimum legal rate — eyes "
            "sliding past each other, buckets kept between them, "
            "not one degree of warmth spent — tolerance, the "
            "polished cold coin everyone already pays — which is "
            "exactly the thing the new command just declined to "
            "accept as payment. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r124-b08", "out": "s08-but-i-say-unto-you.jpeg", "seg": "jvA",
        "window": "34.77-46.01", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "But I say unto you, Love your enemies, bless them that curse "
            "you, do good to them that hate you, and pray for them which "
            "despitefully use you, and persecute you;"
        ),
        "must_show": "SCRIPTURE-EXACT: the command — Jesus with both arms opening wide as the four verbs land; the crowd visibly stunned, some mouths open.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the stun REAL — disbelief on the faces, nobody nodding now.",
        "scene": (
            "The audit lands with four verbs and no exemptions: "
            "Jesus's arms open wide over the crowd — LOVE them, "
            "BLESS them, DO GOOD to them, PRAY for them — each "
            "verb aimed precisely at the people who have earned "
            "the opposite, and the hillside takes it like weather "
            "changing: mouths open along the rows, a fisherman's "
            "head rocking slowly back, the mother's hand still on "
            "her child — nobody nodding anymore, everybody doing "
            "the new arithmetic and finding it costs everything "
            "they were saving. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r124-b09", "out": "s09-not-stay-out-of-their.jpeg", "seg": "n3",
        "window": "48.81-51.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS", "FARMER", "NEIGHBOUR"],
        "narration": "Not stay out of their way. Bless.",
        "must_show": "the first verb enacted small — at the well, the farmer's hand lifting in an actual greeting toward the neighbour, who looks up startled; the first crack in years of cold.",
        "must_not_show": "no halo; the greeting SMALL and costly — one raised hand, not an embrace; the neighbour's surprise honest.",
        "scene": (
            "The first verb crosses the well in one raised hand: "
            "the farmer, bucket set down, lifts his hand toward "
            "the neighbour in an actual greeting — small, "
            "deliberate, unmistakably aimed — and the heavier man "
            "looks up from his rope startled, caught mid-draw by "
            "the first warm signal to cross that water in years — "
            "not avoidance perfected, but blessing begun, at the "
            "modest exchange rate of one hand raised on purpose "
            "toward a man who has earned none of it. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b10", "out": "s10-do-good-pray.jpeg", "seg": "n3",
        "window": "51.67-53.86", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Do good. Pray.",
        "must_show": "the verbs sinking in — close along stunned crowd faces working through what was just asked: disbelief, calculation, the first dawning seriousness.",
        "must_not_show": "no halo; the faces WORKING — not outrage, but the heavy arithmetic of an actual demand.",
        "scene": (
            "Two more verbs land on faces already reeling: close "
            "along the front rows as the words sink — the young "
            "farmer's brow knotted over the mathematics of doing "
            "GOOD to the man who hates him, an old woman's lips "
            "repeating pray for them as if testing whether the "
            "words will hold weight, a fisherman staring at his "
            "own scarred hands — nobody dismissing it, everybody "
            "measuring it, the whole hillside quietly discovering "
            "the command was meant literally. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b11", "out": "s11-every-one-of-those-is.jpeg", "seg": "n3",
        "window": "53.86-60.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS", "FARMER"],
        "narration": (
            "Every one of those is something you go and do — aimed straight "
            "at the person who has earned none of it."
        ),
        "must_show": "the going-and-doing — the farmer walking deliberately along the wall TOWARD the neighbour's side with tools over his shoulder; love as direction and freight.",
        "must_not_show": "no halo; DIRECTION LAW — his stride unmistakably toward the neighbour's land, tools for work, not confrontation.",
        "scene": (
            "The verbs turn out to have legs: the farmer walks "
            "the wall-line with his mattock and a coil of rope "
            "over one shoulder, stride set deliberately TOWARD "
            "the neighbour's side of the valley — not drifting, "
            "not detouring, freight aimed straight at the one "
            "address in the world that has earned none of it — "
            "love travelling the way the sentence orders it to "
            "travel: on foot, carrying tools, in the direction "
            "everyone said was closed. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b12", "out": "s12-picture-a-farmer-whose-neighbor.jpeg", "seg": "n3",
        "window": "60.52-69.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS", "FARMER", "NEIGHBOUR"],
        "narration": (
            "Picture a farmer whose neighbor has wronged him: the fence "
            "knocked down, the insult at the well, years of cold looks "
            "across one stone wall."
        ),
        "must_show": "the grievance mapped — the wall with one old knocked-gap in it, the well between the farms, and the two men exchanging the practiced cold look across the stones; years in one frame.",
        "must_not_show": "no halo; the history told by the GAP and the look — no violence enacted, no shouting.",
        "scene": (
            "The whole case file fits in one valley frame: there "
            "in the wall the old knocked-down gap, mended crooked "
            "and never forgiven; there the shared well where the "
            "insult was said and has been re-heard every drawing "
            "since; and there, across the stones, the look — the "
            "farmer and the neighbour catching each other's eyes "
            "for the cold half-second that has been their entire "
            "correspondence for years — the wrong, the word, and "
            "the wall, all still doing business. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b13", "out": "s13-he-has-every-right-to.jpeg", "seg": "n4",
        "window": "70.50-73.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS", "FARMER", "NEIGHBOUR"],
        "narration": "He has every right to answer coldness with coldness.",
        "must_show": "the entitled cold — the standoff at its most correct: both men drawing water in turn with backs fully turned, the space between them exact and legal.",
        "must_not_show": "no halo; nothing cruel ENACTED — just two backs and measured distance; the rightness of it the point.",
        "scene": (
            "Nobody could fault the arrangement: at the well the "
            "two men take their water in strict turn, backs "
            "fully turned, the distance between them measured "
            "out to the exact width of the wrong — every motion "
            "correct, every right reserved, the whole cold "
            "protocol executed to the letter of the old "
            "arithmetic — a peace with no war and no warmth in "
            "it, defensible in any court in the valley and "
            "getting neither man one stone closer to anything. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b14", "out": "s14-that-is-the-old-arithmetic.jpeg", "seg": "n4",
        "window": "73.66-77.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS"],
        "narration": "That is the old arithmetic, and nobody would blame him for it.",
        "must_show": "the village's shrug — elders at the well shrugging mildly at the familiar standoff; the coldness normalized, unremarkable, blameless.",
        "must_not_show": "no halo; the shrug MILD — no gossip circle, no mockery; this is just how it is.",
        "scene": (
            "The valley has long since filed the feud under "
            "normal: two elders resting at the well give the "
            "familiar standoff the mildest of shrugs — one tilt "
            "of a grey head, one puff of breath — the way men "
            "acknowledge weather that has always been there — "
            "nobody blames, nobody intervenes, nobody even "
            "gossips anymore — the old arithmetic so universally "
            "accepted that its cold sum draws less attention in "
            "the village than a change of wind. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b15", "out": "s15-instead-when-his-wall-gives.jpeg", "seg": "n4",
        "window": "77.30-83.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS", "FARMER", "NEIGHBOUR"],
        "narration": (
            "Instead, when his neighbor's wall gives way in the rains, he "
            "walks over quietly and starts lifting stones."
        ),
        "must_show": "SCENE-CRITICAL: the quiet help — the rain-collapsed wall section on the NEIGHBOUR'S stretch, the wronged farmer already lifting the fallen stones back into place, the neighbour stopped at distance in open surprise.",
        "must_not_show": "no halo; ACTION-LOGIC — the farmer lifting stones INTO the wall (rebuilding, unmistakably), on the neighbour's side; grey after-rain light.",
        "scene": (
            "The new arithmetic starts work without an "
            "announcement: along the neighbour's stretch the "
            "rains have taken the wall down in a tumbled scatter "
            "— and there in the grey after-rain light stands the "
            "wronged farmer, sleeves wet, lifting the fallen "
            "stones one by one back INTO their courses on the "
            "other man's boundary — while up the slope the "
            "neighbour has stopped dead with his sack half-"
            "shouldered, staring at the impossible sight of his "
            "coldest debt working in his own field for free. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b16", "out": "s16-and-at-night-when-the.jpeg", "seg": "n5",
        "window": "84.12-91.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS", "FARMER"],
        "narration": (
            "And at night, when the work is done and no one is watching, he "
            "does the thing Jesus asked that no one ever sees."
        ),
        "must_show": "the unseen hour — the farmer's stone house at night, one small lamplit window in the dark valley; the private obedience beginning. INTENTIONAL NIGHT.",
        "must_not_show": "no halo; the night DELIBERATE — one warm window, the rest of the valley dark and asleep.",
        "scene": (
            "The hardest verb waits for the hour with no "
            "witnesses: the valley gone fully dark, both farms "
            "asleep under the ridge — except for one small "
            "window in the farmer's stone house holding its "
            "steady lamp-warmth against the night — the work "
            "done, the tools hung, the village unconscious — and "
            "inside that one lit square, the part of the "
            "commandment that has no audience, no credit, and "
            "no way to be seen, getting itself kept anyway. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b17", "out": "s17-by-the-light-of-his.jpeg", "seg": "n5",
        "window": "91.34-96.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER"],
        "narration": (
            "By the light of his lamp, he prays for the man across the wall "
            "— not about him."
        ),
        "must_show": "the prayer — the farmer kneeling by his clay lamp, hands OPEN palm-up, face lifted and unclenched; intercession, not complaint.",
        "must_not_show": "no halo; the hands OPEN (never fists), the face free of grievance — FOR him, visibly, not about him.",
        "scene": (
            "The prayer's grammar is visible in the hands: the "
            "farmer kneels on the swept floor by his one clay "
            "lamp, and his hands are OPEN — palms up, fingers "
            "loose, nothing clenched anywhere in him — the face "
            "above them lifted and unknotted, working through "
            "words that ask things FOR the man across the wall: "
            "his harvest, his household, his good — not one "
            "syllable spent reporting him to heaven — the "
            "lamplight steady on a man interceding, not "
            "prosecuting. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r124-b18", "out": "s18-for-him-by-name.jpeg", "seg": "n5",
        "window": "96.90-99.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMER"],
        "narration": "For him. By name.",
        "must_show": "the name — close on the praying face in lamplight, lips mid-word around a name; the tenderest, costliest syllables in the whole row.",
        "must_not_show": "no halo; the tenderness EARNED — traces of the old hurt still in the face, the name spoken anyway.",
        "scene": (
            "The costliest word in the prayer is a name: close "
            "on the farmer's lamplit face, eyes closed, lips "
            "caught mid-syllable around the one word he has "
            "spent years not saying — the neighbour's own name, "
            "spoken gently, on purpose, to God — the old hurt "
            "still visible in the lines around the eyes and the "
            "name crossing them anyway, the way a bridge crosses "
            "a river that has not stopped running. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b19", "out": "s19-he-was-not-pretending-enemies.jpeg", "seg": "n6",
        "window": "102.78-109.91", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": (
            "He was not pretending enemies don't hurt. He gave his reason on "
            "the same hillside, and the reason changes everything."
        ),
        "must_show": "the honesty — close on Jesus grave and warm at once: a teacher who knows exactly what enemies cost, holding the reason ready.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NOTHING breezy — the gravity of a man acquainted with the price.",
        "scene": (
            "The command comes from a face that knows its price: "
            "close on Jesus in the late gold, and there is "
            "nothing breezy in him — the eyes grave with full "
            "acquaintance of what enemies cost, what curses "
            "weigh, how despiteful use actually feels — no "
            "pretending anywhere in the features — and underneath "
            "the gravity, gathering like light under a door, the "
            "reason he is about to give: the one that moves the "
            "whole commandment from unreasonable to inevitable. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b20", "out": "s20-why-would-jesus-ask-for.jpeg", "seg": "n6",
        "window": "99.88-102.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Why would Jesus ask for something this unreasonable?",
        "must_show": "the question in the crowd — faces openly questioning: furrowed brows, an open-handed shrug mid-murmur, neighbours consulting each other.",
        "must_not_show": "no halo; honest bafflement, not rebellion — the question sincere on every face.",
        "scene": (
            "The hillside asks the obvious question with its "
            "whole body: brows furrowed down the rows, one man's "
            "hands opening in the universal shrug of but-why, "
            "neighbours turning to consult each other's equally "
            "baffled faces — no rebellion in it, just the honest "
            "arithmetic protest of ordinary people being asked "
            "for the one payment nobody budgets: warmth, on "
            "demand, for the accounts that owe THEM — the "
            "question hanging over the grass, waiting for its "
            "answer. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r124-b21", "out": "s21-that-ye-may-be-the.jpeg", "seg": "jvB",
        "window": "110.47-121.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS"],
        "narration": (
            "That ye may be the children of your Father which is in heaven: "
            "for he maketh his sun to rise on the evil and on the good, and "
            "sendeth rain on the just and on the unjust."
        ),
        "must_show": "SCRIPTURE-EXACT: the impartial sun — sunrise flooding the whole valley EQUALLY: both farms, both fields, both sides of the wall in one identical light; the Father's evenhandedness as landscape.",
        "must_not_show": "no halo; ABSOLUTE equality of light — no brighter field, no favoured slope; the wall's shadow thin and irrelevant.",
        "scene": (
            "The reason rises over the ridge like it does every "
            "morning: one sun flooding the shallow valley edge "
            "to edge — the farmer's rows and the neighbour's "
            "olives taking the identical gold at the identical "
            "instant, the long wall between them reduced to one "
            "thin irrelevant thread of shadow — not a degree of "
            "warmth withheld from either slope, the whole "
            "valley's worth of light spent on the just and the "
            "unjust at exactly the same rate, the way the Father "
            "spends it everywhere, daily, on everyone. No people "
            "are needed in this frame."
        ),
    },
    {
        "id": "v2-r124-b22", "out": "s22-look-at-the-sky-he.jpeg", "seg": "n7",
        "window": "122.69-124.73", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Look at the sky, he was saying.",
        "must_show": "the pointing up — Jesus's arm sweeping up toward the open sky, the crowd's faces lifting together; the answer located overhead.",
        "must_not_show": "no halo, glare or rim-light on Jesus; DIRECTION LAW — every face follows the arm upward.",
        "scene": (
            "The answer was overhead the whole time: Jesus's arm "
            "sweeps up toward the wide bright sky above the "
            "lake, and the hillside's faces lift together with "
            "the gesture — fishermen shading their eyes, "
            "children tipping all the way back in the grass — "
            "the whole baffled congregation redirected in one "
            "motion from their ledgers to the sun that has been "
            "paying out on every account in the valley, evil and "
            "good alike, since before any of their grievances "
            "were born. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r124-b23", "out": "s23-your-sun-came-up-this.jpeg", "seg": "n7",
        "window": "124.73-131.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS"],
        "narration": (
            "Your Father's sun came up this morning over every field in the "
            "valley — the kind man's and the cruel man's alike."
        ),
        "must_show": "the doctrine at field level — morning light lying identical on both farms' crops, both houses' walls; kindness and cruelty invoiced nothing either way.",
        "must_not_show": "no halo; the equality EXACT — same warmth, same gold, both slopes.",
        "scene": (
            "At field level the evenhandedness is even plainer: "
            "the morning lies identical on both slopes — the "
            "same gold on the farmer's young barley and the "
            "neighbour's olive rows, the same warmth soaking "
            "both stone houses' eastern walls, dew burning off "
            "both fields at the same unhurried rate — the "
            "valley's entire daily allowance of light delivered "
            "without one glance at anybody's conduct, the kind "
            "man's acres and the cruel man's acres invoiced "
            "exactly nothing, alike. No people are needed in "
            "this frame."
        ),
    },
    {
        "id": "v2-r124-b24", "out": "s24-his-rain-waters-both-loving.jpeg", "seg": "n7",
        "window": "131.63-136.22", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS"],
        "narration": "His rain waters both. Loving an enemy is not unnatural.",
        "must_show": "the impartial rain — silver rain falling across the whole valley at once, both farms drinking it, both fields green under it.",
        "must_not_show": "no halo; the rain GENTLE and general — no storm, no favoured field.",
        "scene": (
            "The rain keeps the same books as the sun: a silver "
            "curtain of it drifting the valley's full width, "
            "falling without preference on barley and olives, on "
            "this roof and that roof, both fields drinking, both "
            "cisterns filling, the wall between the farms "
            "gleaming wet along its whole length like a seam "
            "being quietly soaked away — heaven's own habit of "
            "loving the undeserving demonstrated from above at "
            "scale, daily, and called weather. No people are "
            "needed in this frame."
        ),
    },
    {
        "id": "v2-r124-b25", "out": "s25-in-this-family-it-is.jpeg", "seg": "n7",
        "window": "136.22-142.25", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "In this family, it is the resemblance. And then he asked the "
            "question that leaves none of us out."
        ),
        "must_show": "the family resemblance — Jesus with his hand moving from the sky down toward the crowd's own chests: like Father, like children; the next question gathering.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gesture WARM — an inheritance being pointed out, not a duty assigned.",
        "scene": (
            "The point of the weather turns out to be family: "
            "Jesus's hand comes down from the sky in one slow "
            "line to rest, open, toward the crowd's own chests — "
            "the sun's habit, the rain's habit, offered to them "
            "as the family trait: love that does not check "
            "deserving first — in this house, the gesture says, "
            "that is simply what the children look like — and "
            "then the head tilts, and the hillside braces for "
            "the question that will leave nobody out of it. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b26", "out": "s26-for-if-ye-love-them.jpeg", "seg": "jv46",
        "window": "142.77-149.36", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "For if ye love them which love you, what reward have ye? do not "
            "even the publicans the same?"
        ),
        "must_show": "SCRIPTURE-EXACT: the question — Jesus with brows lifted in the gentle challenge, a half-smile at its edge; the crowd caught by a question with no exits.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the challenge PLAYFUL-SERIOUS — the smile disarms, the question lands.",
        "scene": (
            "The question comes with a raised eyebrow and no "
            "exits: Jesus tilts his head, brows lifted, the "
            "faint beginning of a smile at the mouth's corner — "
            "if you only love the ones who love you, what "
            "exactly is the achievement? — the gentlest possible "
            "delivery of a question that pickpockets every "
            "listener's last excuse, offered with the warmth of "
            "a teacher who intends to leave nobody, including "
            "the best people on this hillside, anywhere to "
            "hide. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r124-b27", "out": "s27-if-you-only-love-the.jpeg", "seg": "n8",
        "window": "150.91-155.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "If you only love the people who love you back, he asked, what "
            "credit is that?"
        ),
        "must_show": "the self-recognition — crowd faces caught out: a rueful half-smile, a slow exhale, eyes dropping; everyone privately convicted, gently.",
        "must_not_show": "no halo; the conviction GENTLE — wry self-recognition, no shame-faces.",
        "scene": (
            "The question finds everyone home: along the rows "
            "the faces do the small honest arithmetic and come "
            "up short — a fisherman's rueful half-smile breaking "
            "as he catches himself, an elder's long slow exhale, "
            "a young mother's eyes dropping to her child with "
            "the private admission that her love has mostly "
            "stayed inside her own walls — nobody wounded, "
            "everybody caught, the whole hillside gently "
            "pickpocketed of its credit at once. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b28", "out": "s28-even-the-tax-collectors-manage.jpeg", "seg": "n8",
        "window": "155.45-158.31", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Even the tax collectors manage that much.",
        "must_show": "the comparison — a publican's courtyard table: tax collectors dining warmly among their OWN circle only, laughter inside the ring, the gate closed to the street.",
        "must_not_show": "no halo; the publicans HUMAN and convivial — the point is the closed circle, not villainy.",
        "scene": (
            "The bar being cleared is set in a courtyard: around "
            "a publican's low table the tax collectors dine "
            "warmly — wine passed, laughter easy, hands on "
            "shoulders — every bit of it genuine and every bit "
            "of it spent strictly inside their own ring, the "
            "courtyard gate shut comfortably against the street "
            "— love flowing exactly as far as love comes back, "
            "and not one cubit farther — the same-love-for-same "
            "that even this table, says the question, manages "
            "without any sermon at all. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r124-b29", "out": "s29-the-love-that-marks-you.jpeg", "seg": "n8",
        "window": "158.31-162.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS", "FARMER", "NEIGHBOUR"],
        "narration": (
            "The love that marks you as your Father's child is the love that "
            "is not owed."
        ),
        "must_show": "the unowed gift — over the rebuilt wall, the farmer handing across a basket of bread and early figs to the neighbour, who receives it with both hands, undone.",
        "must_not_show": "no halo; the handoff OVER the wall — the boundary still there, the love crossing it anyway; the neighbour's face moved, not grovelling.",
        "scene": (
            "The family trait crosses the wall in a basket: over "
            "the rebuilt stones the farmer passes a woven basket "
            "of bread and early figs across to the neighbour — "
            "unasked, unowed, unaccountable under the old "
            "arithmetic — and the heavier man receives it with "
            "both hands like something too fragile for its "
            "weight, his guarded face undone one degree at a "
            "time — the boundary still standing, and the love "
            "simply crossing above it, the way the sun has been "
            "doing all along. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r124-b30", "out": "s30-and-sometimes-slowly-it-wins.jpeg", "seg": "n8",
        "window": "162.67-171.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["FARMS", "FARMER", "NEIGHBOUR"],
        "narration": (
            "And sometimes, slowly, it wins what coldness never could: the "
            "wall between two houses becomes the place where they meet."
        ),
        "must_show": "the closing image — golden evening: the two farmers SEATED TOGETHER on the rebuilt wall, sharing bread, tools leaned side by side; the boundary become the bench.",
        "must_not_show": "no halo; the seating ON the wall unmistakable — the dividing line repurposed as the meeting place; both men easy.",
        "scene": (
            "The wall gets a new job at golden evening: the two "
            "farmers sit ON it, side by side at its low point by "
            "the well — bread broken between them, a water-skin "
            "passing, their mattocks leaned together against the "
            "stones like old friends' — the long line that spent "
            "years dividing the valley now holding both men up "
            "at once — coldness never won an inch of this, and "
            "the unowed love has quietly taken the whole wall: "
            "the border, become the bench. Every figure has two "
            "arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "FARMS": "PLACE-REF/farms.jpeg",  # build-124-love-your-enemies s05-everyone-on-that-hillside-knew (manual)
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "FARMER": "CAST-REF-V2/farmer.jpeg",
    "NEIGHBOUR": "CAST-REF-V2/neighbour.jpeg",
}
