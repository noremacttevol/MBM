#!/usr/bin/env python3
"""V2 beat map — row 23, build-23-vineyard (Matthew 20:1-16).

COVERAGE: 30 pictures over 171.6 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 20:1-16 KJV):
  v1    "went out EARLY IN THE MORNING to hire labourers" — the first hire is
        at dawn, cold blue-gold first light.
  v2    "agreed with the labourers for A PENNY A DAY" — one denarius, a fair
        full day's wage, AGREED — the dawn crew has a contract.
  v3-5  "the THIRD hour ... standing IDLE in the MARKETPLACE ... SIXTH and
        NINTH hour, and did likewise" — repeated trips to the market through
        the climbing day.
  v6    "about the ELEVENTH hour he went out, and found others standing
        idle" — one hour of daylight left, low golden sun.
  v7    "Because NO MAN HATH HIRED US" — not lazy; passed over. The narration
        names it the wound: nobody had chosen them.
  v8    "when EVEN was come ... beginning from the LAST unto the first" —
        the payout is at dusk and the order is deliberately reversed.
  v9-10 every man receives the SAME one penny.
  v11-12 "they MURMURED against the goodman ... borne the burden and HEAT of
        the day" — the dawn crew is sun-scorched and resentful.
  v13   "FRIEND, I do thee no wrong" — the owner is never harsh; he answers
        one man, kindly, with questions.
  v15   "Is thine eye evil, because I am good?"
  v16   "So the last shall be first, and the first last."

⚠️ TIME-OF-DAY ARC IS THE ENGINE OF THIS ROW and it legitimately runs to
sunset and dusk: dawn hire (cold first light) → third hour (climbing morning)
→ noon (hard vertical light) → eleventh hour (LOW GOLDEN sun, long shadows)
→ the paying of wages at DUSK by lamplight. Golden-hour and dusk colouring in
the later beats is CORRECT per v8 "when even was come" — do not mistake it
for the row-11 storm defect. The Jesus frame beats (b01, b28) are morning and
evening respectively, matching where they fall in the telling.

CONTENT-CARE: row 23 has no flag in §3. The murmuring stays verbal — faces
and posture, never a raised fist; the owner is never mocked or threatened.

CHANGING CONDITION (kept OUT of the locks): light and wear — the dawn crew
starts fresh and ends sweat-soaked, dusty and sunburnt; the sky and shadows
move through the whole day. Locks carry faces and clothing colours only.

The penny: a single small rough-struck ancient silver coin (a denarius) —
always small, always silver, never gold, never modern.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "OWNER": (
        "OWNER LOCK: the vineyard owner is the same man in every shot — in his "
        "mid-fifties, solid and upright, with a neatly kept dark beard streaked "
        "iron-grey, warm deep-set brown eyes and a broad open face. He wears a "
        "good robe of DEEP MADDER-RED wool over a DARK UMBER under-tunic, a "
        "wide woven belt and sturdy sandals (never cream, never white). His "
        "face is shown clearly and it is kind even when it is firm."
    ),
    "STEWARD": (
        "STEWARD LOCK: the steward is the same man in every shot — about "
        "thirty, lean and brisk, close-cropped dark hair and a short dark "
        "beard. He wears a plain DARK OLIVE wool tunic with a leather belt "
        "carrying a heavy leather wage-bag and a wax tablet (never cream, "
        "never white). His face is shown clearly."
    ),
    "FIRSTMAN": (
        "FIRST-CREW SPOKESMAN LOCK: the spokesman of the dawn crew is the same "
        "man in every shot — early forties, big-shouldered and sun-scorched, "
        "with a heavy black beard, a sunburnt weathered face and strong scarred "
        "forearms. He wears a coarse DARK UMBER-BROWN work tunic, sweat-marked, "
        "with a rope belt and a rag of dusty cloth at his neck (never cream, "
        "never white). His face is shown clearly."
    ),
    "OLDMAN": (
        "PASSED-OVER MAN LOCK: the eleventh-hour man is the same man in every "
        "shot — nearing sixty, thin and slightly stooped, with a sparse grey "
        "beard, hollow temples and patient deep-lined eyes that expect nothing. "
        "He wears a threadbare DARK SLATE-GREY wool tunic, much patched, with a "
        "frayed rope belt (never cream, never white). His face is shown clearly."
    ),
    "VINEYARD": (
        "VINEYARD LOCK: a terraced hillside vineyard in full leaf and heavy "
        "with dark grape clusters — low stone terrace walls stepping up the "
        "slope, old gnarled vine rows, a beaten path up the middle, a stone "
        "watchtower at the crown of the hill, and a wide wooden gate in the "
        "low boundary wall by the road."
    ),
    "MARKET": (
        "MARKETPLACE LOCK: the village marketplace — a dusty open square of "
        "beaten earth ringed by honey-stone houses, awnings of faded cloth "
        "over traders' stalls, clay jars and baskets of produce, a stone well "
        "at the centre, and the open road leaving between the houses."
    ),
    "PAYYARD": (
        "PAY-YARD LOCK: the flat working yard before the vineyard gate — a "
        "beaten-earth threshing floor, a rough plank table, stacked harvest "
        "baskets of dark grapes along the wall, and two clay oil lamps set on "
        "the table's corners."
    ),
    "HILLSIDE": (
        "TEACHING HILLSIDE LOCK: an open grassy hillside above a road in "
        "Judean hill country — dry grass and scattered white limestone, a few "
        "low fig and olive trees, and terraced fields on the far slopes "
        "rolling away below."
    ),
    "WORKERS": (
        "WORKERS LOCK: the hired labourers are ordinary working men of mixed "
        "ages with dark hair and dark beards, dressed in SATURATED DEEP earth "
        "colours — dark chocolate brown, deep russet, dark olive, burnt ochre "
        "and dusty indigo wool, rope belts, worn sandals (never cream, never "
        "white; only Jesus wears cream). Their faces are shown clearly."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------------ n1/n2 — the dawn hire ----
    {
        "id": "v2-r023-b01", "out": "s01-jesus-said-the-kingdom-of.jpeg", "seg": "n1",
        "window": "0.28-5.99", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": (
            "Jesus said the kingdom of heaven is like a landowner who went out "
            "at first light to hire workers for his vineyard."
        ),
        "must_show": "Jesus seated on a limestone outcrop on the morning hillside, a handful of listeners on the grass around him, beginning the story.",
        "must_not_show": "no halo, glare or rim-light on Jesus; he is at the listeners' level, not raised above them on a height.",
        "scene": (
            "On an open grassy hillside in clear morning light, Jesus sits on a "
            "low white limestone outcrop with five or six listeners settled on "
            "the dry grass close around him, one hand lifted in the first "
            "gesture of a story. The terraced far slopes roll away soft behind "
            "them. Everyone leans slightly in. The camera stands back to hold "
            "the whole small gathering. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r023-b02", "out": "s02-he-agreed-with-the-first.jpeg", "seg": "n2",
        "window": "6.56-13.38", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "WORKERS", "MARKET"],
        "narration": (
            "He agreed with the first crew on a penny for the day — a full "
            "day's fair wage — and sent them out into the rows."
        ),
        "must_show": "SCRIPTURE-EXACT: dawn in the marketplace — the owner clasping forearms with the lead worker to seal the agreed wage, the rest of the crew shouldering tools behind him.",
        "must_not_show": "no halo, glare or rim-light; dawn light, cold and low — NOT golden afternoon; the agreement handclasp is the visible action.",
        "scene": (
            "The marketplace at first light, the square still in cold blue "
            "shadow with the first low gold just touching the rooftops. The "
            "owner in his deep madder-red robe clasps forearms with a broad "
            "sunweathered labourer, sealing the bargain, while behind them "
            "four more workers shoulder pruning hooks and empty baskets, "
            "breath faintly misting in the early chill. The camera holds the "
            "handclasp at the centre of the square. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b03", "out": "s03-a-few-hours-later-he.jpeg", "seg": "n3",
        "window": "14.03-18.69", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "WORKERS", "MARKET"],
        "narration": (
            "A few hours later he went back to the market and found more men "
            "just standing around with no work."
        ),
        "must_show": "SCRIPTURE-EXACT: the third hour — the owner re-entering the market and finding a loose knot of idle men by the well, hands empty, going nowhere.",
        "must_not_show": "no halo, glare or rim-light; the idle men are not lounging lazily — they wait with the restless emptiness of men nobody wanted.",
        "scene": (
            "Mid-morning light now fills the marketplace and the stalls are "
            "busy. The owner has stopped a few paces into the square, looking "
            "toward the stone well where four men stand in a loose knot with "
            "empty hands — one leaning on the well, one scanning the square, "
            "two talking low — men waiting for work that has not come. The "
            "camera looks past the owner's shoulder toward them. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b04", "out": "s04-he-sent-them-into-the.jpeg", "seg": "n3",
        "window": "18.69-23.27", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "WORKERS", "MARKET", "VINEYARD"],
        "narration": (
            "He sent them into the vineyard too, and promised to pay them what "
            "was right."
        ),
        "must_show": "the owner's arm extended toward the vineyard hill outside the village, the second crew already moving that way, faces lifted.",
        "must_not_show": "no halo, glare or rim-light; no coins change hands here — this crew goes on a promise.",
        "scene": (
            "At the edge of the marketplace the owner stands with one arm "
            "extended out along the road toward the terraced vineyard hill "
            "rising green beyond the last houses, its stone watchtower small "
            "at the crown. The four men are already in motion past him, tools "
            "gathered from a stall, the nearest turning back mid-stride to nod "
            "his thanks. Bright late-morning light. The camera holds the "
            "pointing owner and the road to the hill in one frame. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b05", "out": "s05-he-did-the-same-thing.jpeg", "seg": "n4",
        "window": "23.85-27.82", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "WORKERS", "MARKET"],
        "narration": (
            "He did the same thing again at noon, and again in the middle of "
            "the afternoon."
        ),
        "must_show": "SCRIPTURE-EXACT: noon — hard vertical light, short shadows, the owner beckoning yet another pair of idle men from the awning shade.",
        "must_not_show": "no halo, glare or rim-light; shadows must be SHORT and directly underfoot — it is noon.",
        "scene": (
            "The marketplace under hard noon sun, shadows pooled short and "
            "black directly beneath every figure and awning. The owner, back "
            "again, beckons with a raised hand to two men sheltering in the "
            "strip of shade under a faded cloth awning; both are already "
            "pushing off the wall toward him. Heat shimmers faintly off the "
            "beaten earth. The camera stands in the open glare of the square. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b06", "out": "s06-more-workers-the-same-promise.jpeg", "seg": "n4 + n5",
        "window": "27.82-37.22", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "OLDMAN", "WORKERS", "MARKET"],
        "narration": (
            "More workers, the same promise. Then, with only one hour of "
            "daylight left, he went out a final time and found still more men "
            "standing idle."
        ),
        "must_show": "SCRIPTURE-EXACT: the eleventh hour — LOW golden sun, long shadows across the emptying square, and the last few men still standing there, the stooped grey-bearded man among them.",
        "must_not_show": "no halo, glare or rim-light; the square is emptying out — stalls packing up; these men have waited ALL DAY.",
        "scene": (
            "The marketplace at the eleventh hour, the sun low and golden, "
            "shadows stretched long and thin across the beaten earth, traders "
            "folding their awnings and loading baskets. By the well three men "
            "still stand where they have stood all day — among them the thin "
            "stooped grey-bearded man in the patched slate-grey tunic — and "
            "the owner has stopped in front of them, taking them in. The "
            "camera looks down the long amber shadows toward the group. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b07", "out": "s07-why-stand-ye-here-all.jpeg", "seg": "j6",
        "window": "37.83-40.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER", "OLDMAN"],
        "narration": "Why stand ye here all the day idle?",
        "must_show": "SCRIPTURE-EXACT: a close shot of the owner asking — his face open and genuinely curious, not accusing — the old man's worn face before him.",
        "must_not_show": "no halo, glare or rim-light; the question is kind — no contempt anywhere in the owner's face.",
        "scene": (
            "A close two-shot in low golden light: the owner's broad kind face "
            "in three-quarter view, brows lifted in a genuine question, and "
            "facing him the thin grey-bearded man, stooped, holding his frayed "
            "rope belt with both hands, eyes just beginning to rise to meet "
            "the owner's. The warm amber light rakes both faces. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b08", "out": "s08-because-no-man-hath-hired.jpeg", "seg": "j7a",
        "window": "41.23-43.22", "wide": False, "jesus": False, "ref": False,
        "locks": ["OLDMAN"],
        "narration": "Because no man hath hired us.",
        "must_show": "SCRIPTURE-EXACT: a close shot of the old man answering — quiet shame and long patience in his face, empty open hands turned slightly out.",
        "must_not_show": "no halo, glare or rim-light; no self-pity or begging — plain worn dignity.",
        "scene": (
            "A close portrait of the thin grey-bearded man in the low golden "
            "light, his lined face lifted, quiet shame and long patience "
            "written together in it, his empty work-worn hands turned slightly "
            "outward at his sides as he answers. The emptying square is soft "
            "colour behind him. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r023-b09", "out": "s09-the-question-revealed-the-wound.jpeg", "seg": "n5b",
        "window": "44.35-49.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["OLDMAN"],
        "narration": (
            "The question revealed the wound: they had not refused work. Nobody "
            "had chosen them."
        ),
        "must_show": "a very close portrait of the old man's eyes — the ache of a whole day, a whole lifetime, of being looked past.",
        "must_not_show": "no halo, glare or rim-light; no tears streaming — the ache is held in, which is worse.",
        "scene": (
            "A very close portrait of the old man's face filling the frame in "
            "warm low light: hollow temples, sparse grey beard, and eyes that "
            "hold the dry, contained ache of a man who has watched every crew "
            "chosen around him since dawn — not weeping, just used to it. The "
            "long golden shadows of the square blur behind him. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b10", "out": "s10-go-ye-also-into-the.jpeg", "seg": "j7b",
        "window": "50.10-54.70", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "OLDMAN", "WORKERS", "MARKET", "VINEYARD"],
        "narration": (
            "Go ye also into the vineyard; and whatsoever is right, that shall "
            "ye receive."
        ),
        "must_show": "SCRIPTURE-EXACT: the owner's arm sweeping toward the vineyard hill, and the waiting men's faces LIGHTING — chosen at last; the old man already straightening.",
        "must_not_show": "no halo, glare or rim-light; the joy of being wanted must read at a glance on every one of the late men.",
        "scene": (
            "In the long golden light the owner stands with his arm swept wide "
            "toward the vineyard hill lit deep green-gold beyond the village"
            "road, and the three waiting men have come alive — the stooped "
            "grey-bearded man straightening his back, a younger man already "
            "half-turned toward the road, the third breaking into an unguarded "
            "grin. The camera catches the sweep of the arm and the lit faces "
            "together. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b11", "out": "s11-even-with-one-hour-of.jpeg", "seg": "n6",
        "window": "55.81-61.34", "wide": True, "jesus": False, "ref": False,
        "locks": ["OLDMAN", "WORKERS", "VINEYARD"],
        "narration": (
            "Even with one hour of daylight left, the owner was still looking "
            "for people others had passed over."
        ),
        "must_show": "the late crew hurrying in through the vineyard gate in the last low sunlight, the old man among them, the vine rows burning gold up the terraces.",
        "must_not_show": "no halo, glare or rim-light; the sun is nearly down the sky — this golden colouring is CORRECT for the eleventh hour.",
        "scene": (
            "The three late-hired men hurry in through the wide wooden gate of "
            "the vineyard in the last low sunlight, the grey-bearded man among "
            "them with a basket already on his shoulder, the terraced vine "
            "rows climbing away above them lit deep green-gold, the stone "
            "watchtower catching the last full sun at the crown of the hill. "
            "The camera stands inside the gate as they come through it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------ n7-n10 — the payout ----
    {
        "id": "v2-r023-b12", "out": "s12-when-evening-came-the-owner.jpeg", "seg": "n7",
        "window": "61.95-69.52", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "STEWARD", "WORKERS", "PAYYARD"],
        "narration": (
            "When evening came, the owner told his foreman to call the workers "
            "and pay them — starting, strangely, with the ones hired last."
        ),
        "must_show": "SCRIPTURE-EXACT: dusk in the pay-yard — the steward at the plank table with the wage-bag and lamps lit, the line of workers forming, and the owner quietly directing him.",
        "must_not_show": "no halo, glare or rim-light; dusk and lamplight are CORRECT here (v8 'when even was come').",
        "scene": (
            "The flat yard before the vineyard gate at dusk, the sky banded "
            "deep amber to blue, two clay lamps burning at the corners of the "
            "rough plank table. The steward stands behind the table opening "
            "the heavy leather wage-bag while the owner leans close to his "
            "ear, one finger indicating the BACK of the forming line — where "
            "the last-hired men stand — as the tired workers file in from the "
            "dark vine rows. The camera holds table, line and owner in one "
            "frame. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b13", "out": "s13-the-men-who-had-worked.jpeg", "seg": "n8",
        "window": "70.11-74.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["STEWARD", "OLDMAN", "PAYYARD"],
        "narration": (
            "The men who had worked a single hour came up first, and each of "
            "them was handed a full day's pay."
        ),
        "must_show": "SCRIPTURE-EXACT: the old man at the table, the steward pressing a single silver penny into his palm — and the old man staring at it, not yet able to close his hand.",
        "must_not_show": "no halo, glare or rim-light; ONE small silver coin — not a stack, not gold.",
        "scene": (
            "At the lamplit plank table the grey-bearded man stands with his "
            "palm open under the light, the steward's hand just withdrawing "
            "from placing a single small rough silver coin in it. The old man "
            "is staring down at the coin, lips parted, hand still flat open as "
            "if closing it might break the spell. Warm lamplight pools on the "
            "two figures against the deep blue dusk. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b14", "out": "s14-a-whole-penny-for-one.jpeg", "seg": "n8 + n9",
        "window": "74.86-81.48", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIRSTMAN", "WORKERS", "PAYYARD"],
        "narration": (
            "A whole penny, for one hour of work. You can guess what the men "
            "who had worked since dawn were thinking."
        ),
        "must_show": "the dawn crew at the back of the line craning to see the payment — heads together, eyebrows up, the arithmetic starting on their faces.",
        "must_not_show": "no halo, glare or rim-light; not yet angry — calculating, expectant, nudging each other.",
        "scene": (
            "At the back of the lamplit line the dawn crew stands sweat-soaked "
            "and dust-caked from the full day, craning past the shoulders "
            "ahead of them toward the pay table — the big black-bearded "
            "spokesman with his eyebrows climbing, the man beside him "
            "murmuring behind a hand, a third counting silently on nothing, "
            "all of them visibly running the same arithmetic. The lamplight "
            "reaches them faintly through the dusk. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b15", "out": "s15-if-the-crew-got-a.jpeg", "seg": "n9",
        "window": "81.48-85.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIRSTMAN"],
        "narration": "If the one-hour crew got a full penny, surely they would get more.",
        "must_show": "a close shot of the spokesman's sunburnt face lit with confident expectation — almost smiling, sure of a windfall.",
        "must_not_show": "no halo, glare or rim-light; confidence, not greed-caricature — a tired man certain he has earned more.",
        "scene": (
            "A close portrait of the big spokesman's sunburnt, dust-streaked "
            "face in the reaching lamplight, an almost-smile lifting one "
            "corner of his mouth inside the heavy black beard, his tired eyes "
            "bright with confident expectation — a man already spending the "
            "extra in his head. Deep blue dusk behind him. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b16", "out": "s16-but-when-their-turn-came.jpeg", "seg": "n10",
        "window": "86.56-91.21", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIRSTMAN", "STEWARD", "PAYYARD"],
        "narration": (
            "But when their turn came, they got the very same — one penny. And "
            "they were furious."
        ),
        "must_show": "SCRIPTURE-EXACT: the spokesman at the table staring down at the SAME single silver penny in his broad palm, his face darkening; the steward already reaching past him for the next man.",
        "must_not_show": "no halo, glare or rim-light; identical coin to the old man's beat — one small silver penny; fury gathering, no violence.",
        "scene": (
            "At the lamplit table the big spokesman stands rooted, his broad "
            "scarred palm open under the lamp with one small rough silver "
            "coin in it — exactly one — his brows crushing down and his jaw "
            "setting as he stares at it. The brisk steward is already leaning "
            "past him to beckon the next man forward. Behind, two more of the "
            "dawn crew push closer to see. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r023-b17", "out": "s17-these-last-have-wrought-but.jpeg", "seg": "j12",
        "window": "91.85-99.51", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIRSTMAN", "OWNER", "WORKERS", "PAYYARD"],
        "narration": (
            "These last have wrought but one hour, and thou hast made them "
            "equal unto us, which have borne the burden and heat of the day."
        ),
        "must_show": "SCRIPTURE-EXACT: the complaint — the spokesman confronting the owner, one arm flung back toward the late-hired men, the penny held up accusingly in his other hand.",
        "must_not_show": "no halo, glare or rim-light; heated words only — no raised fist at the owner, no shoving.",
        "scene": (
            "In the lamplit yard the spokesman stands square in front of the "
            "owner, his coin held up between finger and thumb like evidence, "
            "his other arm flung back toward the knot of late-hired men near "
            "the gate, his sunburnt face working with anger. The owner stands "
            "quite still, listening, hands folded. Around them the tired line "
            "has turned to watch. Lamplight and last dusk mix on the beaten "
            "earth. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b18", "out": "s18-their-anger-was-not-about.jpeg", "seg": "n10b",
        "window": "100.58-102.49", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Their anger was not about a broken agreement.",
        "must_show": "a close still shot of the single silver penny held up between a sunburnt finger and thumb against the dusk — the agreed wage, paid in full.",
        "must_not_show": "no halo, glare or rim-light; one coin only, sharp and small against the darkening sky.",
        "scene": (
            "A close shot of one small rough-struck silver coin held up "
            "between a sunburnt, dust-grimed finger and thumb, sharp against "
            "the deep amber-to-blue dusk sky. The coin is whole, honest and "
            "exactly what was agreed. Soft warm lamplight falls on one edge "
            "of the hand. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b19", "out": "s19-it-was-about-being-treated.jpeg", "seg": "n10b",
        "window": "102.49-107.50", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIRSTMAN", "OLDMAN", "WORKERS", "PAYYARD"],
        "narration": (
            "It was about being treated no better than men they considered less "
            "deserving."
        ),
        "must_show": "the two crews facing each other across the lamplit yard — the dawn crew's resentful stares, and the late-hired men's joy faltering under those stares, the old man's eyes dropping.",
        "must_not_show": "no halo, glare or rim-light; no confrontation of bodies — only looks across the space between the groups.",
        "scene": (
            "Across the lamplit yard the two groups face each other with an "
            "open strip of beaten earth between them: on one side the "
            "sweat-caked dawn crew, arms folded, staring hard; on the other "
            "the few late-hired men, coins in hand, their new joy faltering "
            "under those stares — the grey-bearded man's eyes dropping to the "
            "ground. Nobody moves. The camera holds the gap between them. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b20", "out": "s20-the-owner-turned-to-one.jpeg", "seg": "n11",
        "window": "108.16-113.03", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "FIRSTMAN", "PAYYARD"],
        "narration": (
            "The owner turned to one of them, and he was not harsh about it. He "
            "called him friend."
        ),
        "must_show": "the owner turning to the spokesman with an open, gentle posture — one hand extended palm-up, no anger anywhere in him.",
        "must_not_show": "no halo, glare or rim-light; the owner's gentleness is the whole beat — no pointing finger, no raised chin.",
        "scene": (
            "In the pool of lamplight the owner turns to the fuming spokesman "
            "with his whole body open — shoulders easy, head slightly "
            "inclined, one hand extended palm-up toward the man as if in "
            "invitation rather than rebuke. The spokesman's anger is met with "
            "a face that holds nothing but patient warmth. The watching line "
            "stands soft in the dusk behind them. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b21", "out": "s21-friend-i-do-thee-no.jpeg", "seg": "j1",
        "window": "113.66-118.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER", "FIRSTMAN"],
        "narration": (
            "Friend, I do thee no wrong: didst not thou agree with me for a "
            "penny?"
        ),
        "must_show": "SCRIPTURE-EXACT: a close two-shot — the owner's kind steady face asking his question, the spokesman's anger beginning to lose its footing.",
        "must_not_show": "no halo, glare or rim-light; the owner never mocks — the question is gentle and it lands.",
        "scene": (
            "A close lamplit two-shot in profile: the owner's kind, steady "
            "face turned fully to the spokesman, iron-grey-streaked beard "
            "warm in the lamplight, mid-question — and the spokesman's "
            "sunburnt face a foot away, the fury on it just beginning to "
            "falter into something unsteadier, his eyes flicking away from "
            "the owner's. Deep blue night gathers behind them. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b22", "out": "s22-take-that-thine-is-and.jpeg", "seg": "j1",
        "window": "118.45-125.26", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "FIRSTMAN", "OLDMAN", "PAYYARD"],
        "narration": (
            "Take that thine is, and go thy way: I will give unto the last, "
            "even as unto thee."
        ),
        "must_show": "SCRIPTURE-EXACT: the owner gently closing the spokesman's own fingers over the penny with both hands, while his glance goes across the yard to the late-hired men.",
        "must_not_show": "no halo, glare or rim-light; the closing of the hand is tender, not dismissive.",
        "scene": (
            "In the lamplight the owner has taken the spokesman's broad open "
            "hand in both of his and is gently folding the man's own fingers "
            "closed over the silver penny — an unhurried, almost fatherly "
            "gesture — while his gaze travels past him across the yard to "
            "where the grey-bearded man and the other late workers stand in "
            "the shadows. The spokesman looks down at his closed hand. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b23", "out": "s23-is-it-not-lawful-for.jpeg", "seg": "j1",
        "window": "125.26-129.76", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "PAYYARD", "VINEYARD"],
        "narration": "Is it not lawful for me to do what I will with mine own?",
        "must_show": "SCRIPTURE-EXACT: the owner with both arms opened wide over his own yard, gate, terraces and wage-bag — all of it his to give.",
        "must_not_show": "no halo, glare or rim-light; open arms of ownership and welcome, never a shrug of indifference.",
        "scene": (
            "The owner stands in the middle of his lamplit yard with both "
            "arms opened wide, taking in everything around him in one motion "
            "— the plank table with the open wage-bag, the loaded harvest "
            "baskets against the wall, the wide gate and the dark terraced "
            "rows climbing behind it under the first stars. His face is "
            "lifted, half-smiling, entirely at peace with what he has done. "
            "The camera stands back to hold the man and all that is his. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b24", "out": "s24-is-thine-eye-evil-because.jpeg", "seg": "j1",
        "window": "129.76-133.21", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER", "FIRSTMAN"],
        "narration": "Is thine eye evil, because I am good?",
        "must_show": "SCRIPTURE-EXACT: the question landing — a very close two-shot, the owner's gentle unwavering eyes on the spokesman, whose face is caught between shame and understanding.",
        "must_not_show": "no halo, glare or rim-light; this is the row's quietest frame — stillness, two faces, nothing else.",
        "scene": (
            "A very close two-shot filling the frame: the owner's deep-set "
            "eyes, gentle and absolutely steady, resting on the spokesman — "
            "and the spokesman's sunburnt face inches away caught in the "
            "middle of changing, anger draining, shame and the beginning of "
            "understanding moving in behind it, his eyes down. Lamplight "
            "warms the edge of both faces against the dark. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    # ---------------------------------------------- n12-n14 — the meaning ----
    {
        "id": "v2-r023-b25", "out": "s25-the-answer-exposed-the-real.jpeg", "seg": "n12",
        "window": "134.25-141.59", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIRSTMAN", "OLDMAN", "PAYYARD"],
        "narration": (
            "The owner's answer exposed the real grievance: generosity to the "
            "latecomers felt like theft to those who had arrived early."
        ),
        "must_show": "the spokesman looking across the yard at the old man — both holding the identical coin — the comparison itself, made visible.",
        "must_not_show": "no halo, glare or rim-light; the two coins must read as IDENTICAL; the old man does not gloat — he holds his coin like a treasure.",
        "scene": (
            "Across the lamplit yard the spokesman stands with his penny held "
            "loosely in his half-open hand, staring at the grey-bearded man "
            "near the gate — who holds an identical small silver penny "
            "pressed to his chest with both hands like something holy, "
            "unaware of being watched. The same lamplight touches both coins. "
            "The camera holds both men and the space between. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b26", "out": "s26-that-is-the-whole-point.jpeg", "seg": "n13",
        "window": "142.21-148.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIRSTMAN"],
        "narration": (
            "That is the whole point. The first men were not underpaid. They "
            "got everything they were promised."
        ),
        "must_show": "a close shot of the spokesman's opened palm with the full agreed penny — whole, honest, complete — and his face above it, working it out.",
        "must_not_show": "no halo, glare or rim-light; the coin is not diminished or dirty — it is a good, full, fair wage.",
        "scene": (
            "A close shot of the spokesman's broad scarred palm open in the "
            "lamplight, the single bright silver penny sitting whole and "
            "honest at its centre — and above it, softly out of focus, his "
            "tired face frowning down at the coin, working something out for "
            "the first time. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r023-b27", "out": "s27-what-stung-was-watching-someone.jpeg", "seg": "n13",
        "window": "148.08-152.80", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIRSTMAN", "OLDMAN", "WORKERS", "PAYYARD"],
        "narration": (
            "What stung was watching someone else receive grace they had not "
            "earned."
        ),
        "must_show": "foreground: the spokesman's bitter profile watching; background: the old man showing his penny to a younger late-hired man, both faces alight — joy that costs the watcher nothing, and stings anyway.",
        "must_not_show": "no halo, glare or rim-light; the joy in the background is innocent — never smug.",
        "scene": (
            "In the near foreground, sharp: the spokesman's profile, jaw "
            "tight, eyes fixed across the yard. Beyond him, softer in the "
            "lamplight by the gate: the grey-bearded man holding his penny "
            "out on his open palm to show a younger late-hired worker, both "
            "their faces open and alight, the young man gripping the old "
            "man's shoulder in shared delight. The night sky is fully dark "
            "above the wall. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r023-b28", "out": "s28-so-the-last-shall-be.jpeg", "seg": "j2",
        "window": "153.35-158.74", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": (
            "So the last shall be first, and the first last: for many be "
            "called, but few chosen."
        ),
        "must_show": "SCRIPTURE-EXACT: back to Jesus on the hillside — evening now, the story closing, his listeners very still.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the evening colouring matches the telling's end — correct, not a defect.",
        "scene": (
            "The open hillside again, now in soft evening light with the far "
            "terraced slopes going blue. Jesus sits forward on the limestone "
            "outcrop, hands loosely clasped, delivering the story's last line "
            "quietly; the five or six listeners on the grass are completely "
            "still, one with his chin on his drawn-up knees, another staring "
            "out at the darkening valley, the words settling on them. The "
            "camera holds the quiet circle from a few paces out. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r023-b29", "out": "s29-god-does-not-run-low.jpeg", "seg": "n14",
        "window": "159.80-166.44", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "STEWARD", "WORKERS", "PAYYARD"],
        "narration": (
            "God does not run low on generosity when he spends it on someone "
            "who came late. His goodness is never used up."
        ),
        "must_show": "the wage-bag still OPEN and heavy on the table as the owner presses a coin into the last worker's hands with both of his — abundance with no bottom to it.",
        "must_not_show": "no halo, glare or rim-light; the bag must look full, not scraped empty.",
        "scene": (
            "At the lamplit table the leather wage-bag stands open and still "
            "visibly heavy with silver, and beside it the owner presses a "
            "penny into a young worker's cupped hands using both of his own, "
            "unhurried, looking the man in the face as he does it. The "
            "steward waits with the wax tablet, and the lamps burn steady "
            "against the full night. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r023-b30", "out": "s30-there-is-a-full-welcome.jpeg", "seg": "n14",
        "window": "166.44-171.23", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "VINEYARD"],
        "narration": (
            "There is a full day's welcome waiting for you, no matter what hour "
            "you finally come in."
        ),
        "must_show": "the closing image — the vineyard's wide wooden gate standing OPEN in the night, warm lamplight spilling out through it onto the dark road, and the owner standing in the gateway looking OUT toward the road.",
        "must_not_show": "no halo, glare or rim-light; the gate must be unmistakably open and the light warm — an invitation, not a closed door.",
        "scene": (
            "Full night. The vineyard's wide wooden gate stands open in the "
            "low boundary wall, warm lamplight from the yard spilling through "
            "it in a long bright path across the dark empty road. In the "
            "gateway the owner stands looking out along the road into the "
            "dark, one hand resting on the open gate — a man still watching "
            "for anyone who might yet come. Above the wall the vine terraces "
            "rise as soft shapes under the stars. The camera stands out on "
            "the dark road, looking into the light. Every figure has two "
            "arms, two hands and one head."
        ),
    },
]
