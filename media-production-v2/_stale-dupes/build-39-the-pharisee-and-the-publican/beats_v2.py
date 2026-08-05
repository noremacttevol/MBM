#!/usr/bin/env python3
"""V2 beat map — row 39, build-39-the-pharisee-and-the-publican (Luke 18:9-14).

COVERAGE: 42 pictures over 237.1 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 18:9-14 KJV):
  v9    "unto certain which TRUSTED IN THEMSELVES that they were righteous,
        and DESPISED OTHERS" — the frame beats (b01, b02, b30, b40-42)
        stage Jesus near the temple's outer gate addressing a knot of
        self-assured religious men with ordinary listeners at the edges —
        distinct from row 37's colonnade staging.
  v10   "Two men went UP INTO THE TEMPLE TO PRAY" — the hour of the daily
        sacrifice (bright mid-morning): incense smoke rising from the
        inner court is visible in the temple beats; the narration (b25)
        leans on the lamb being offered at that very hour, so the smoke
        column and the distant altar activity matter — but the sacrifice
        itself stays DISTANT and non-graphic (smoke, priests, never the
        act).
  v11-12 the Pharisee "STOOD and prayed thus WITH HIMSELF" — front and
        centre, hands lifted, eyes open, visible to everyone; his prayer
        is an inventory. HE IS NOT A FAKE (narration insists): his
        discipline beats (fasting, tithing herbs) are painted honestly
        and even admirably.
  v13   "the publican, STANDING AFAR OFF, would not lift up so much as
        his EYES unto heaven, but SMOTE UPON HIS BREAST" — the very back,
        eyes down, the mourner's fist on the chest.
  v14   "this man went down to his house JUSTIFIED rather than the other"
        — the descent-of-the-steps beat carries the whole reversal: one
        man goes down changed, the other is still up there.
  The closing beats (b40-42) carry the mercy: the story LETS THE GOOD MEN
  IN TOO — the door 'only closes from the inside.'

TIME OF DAY: all temple beats are bright mid-morning (the hour of the
Tamid sacrifice). The Pharisee's discipline beats are their own hours
(dawn fast-keeping, garden tithing at midday). The publican's homeward
beats are warm late-morning. The frame beats are the same bright morning
at the outer gate. No sunset anywhere in this row.

CONTENT-CARE: row 39 has no flag in §3. The Pharisee is painted honest
and admirable in his discipline — the row must NOT make him a cartoon;
his tragedy is certainty, not hypocrisy. The publican's shame is painted
with dignity.

CHANGING CONDITION (kept OUT of the locks): the publican's bearing — he
climbs the steps bowed and descends them upright; the Pharisee's never
changes. That asymmetry is the row's spine, stated per-beat.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "PHARISEE": (
        "PHARISEE LOCK: the Pharisee is the same man in every shot — about "
        "fifty, tall, spare and immaculate, with a long combed dark beard "
        "streaked silver, upright carriage and clear confident eyes. He "
        "wears finely woven DEEP INDIGO robes with wide DARK UMBER borders, "
        "a fringed prayer shawl of NEAR-BLACK blue wool, and phylacteries "
        "bound at brow and arm (never cream, never white). His face is "
        "shown clearly — earnest and certain, never sneering, never a "
        "cartoon."
    ),
    "PUBLICAN": (
        "PUBLICAN LOCK: the tax collector is the same man in every shot — "
        "about forty-five, thickset and prosperous-gone-heavy, with a "
        "short dark beard, a fleshy careworn face and eyes that avoid "
        "other eyes. He wears a good but gaudy DARK WINE-RED robe with a "
        "DARK MUSTARD sash and rings he keeps twisting (never cream, "
        "never white). His face is shown clearly — shame carried with "
        "dignity, never grovelling caricature."
    ),
    "TEMPLE": (
        "TEMPLE COURT LOCK: the temple's great court at mid-morning — "
        "vast pale limestone paving, high surrounding porticoes, the "
        "broad steps rising toward the inner gates, and beyond them a "
        "single straight column of pale sacrifice smoke standing up "
        "into the bright sky from the unseen altar. Worshippers "
        "scattered across the space wear SATURATED DEEP earth colours "
        "(never cream, never white; only Jesus wears cream)."
    ),
    "GATE": (
        "OUTER GATE LOCK: the temple mount's outer gate — a high arched "
        "gateway of massive pale stones with worn steps spilling down "
        "to the street, sellers of doves in the shade of the arch, and "
        "listeners gathered on the steps: fine-robed men in NEAR-BLACK "
        "INDIGO and DARK UMBER with fringed shawls near the front, "
        "ordinary listeners in worn earth tones around them (never "
        "cream, never white; only Jesus wears cream). Faces shown "
        "clearly."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r039-b01", "out": "s01-and-he-spake-this-parable.jpeg", "seg": "s9",
        "window": "0.28-6.60", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GATE"],
        "narration": (
            "And he spake this parable unto certain which trusted in themselves "
            "that they were righteous, and despised others."
        ),
        "must_show": "SCRIPTURE-EXACT: the frame — Jesus on the outer gate steps addressing a knot of confident fine-robed men whose chins are still high, ordinary listeners gathering at the edges.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the audience's self-assurance visible in posture — folded arms, lifted chins — before a word lands.",
        "scene": (
            "On the worn steps beneath the great arched gate Jesus "
            "stands mid-sentence in the bright morning, and before "
            "him a knot of tall fine-robed men listen with their "
            "chins high and their arms folded into their fringed "
            "shawls, certainty sitting on them like their clothes — "
            "while at the edges of the steps poorer listeners drift "
            "in close, and a dove-seller leans out of the arch's "
            "shade to hear. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r039-b02", "out": "s02-jesus-told-this-story-to.jpeg", "seg": "n1",
        "window": "8.27-10.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATE"],
        "narration": "Jesus told this story to a certain kind of man.",
        "must_show": "the kind itself — a close shot of one confident listener's face: decent, disciplined, absolutely sure; the story's true addressee.",
        "must_not_show": "no halo, glare or rim-light; the face must be LIKEABLE — the trap of the row is that this man is genuinely good.",
        "scene": (
            "A close portrait on the gate steps: one listener's "
            "face in the bright light — a decent, disciplined face "
            "with a well-kept beard and clear untroubled eyes, the "
            "face of a man who keeps every commitment he makes and "
            "knows it — listening to the story's opening with the "
            "mild interest of someone certain it is about somebody "
            "else. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r039-b03", "out": "s03-the-kind-who-was-sure.jpeg", "seg": "n1",
        "window": "10.69-15.94", "wide": True, "jesus": False, "ref": False,
        "locks": ["GATE"],
        "narration": (
            "The kind who was sure he was one of the good ones, and just as "
            "sure that other people were not."
        ),
        "must_show": "the despising made visible — on the gate steps, a fine-robed man drawing his hem aside from a passing labourer without even looking at him; contempt as reflex.",
        "must_not_show": "no halo, glare or rim-light; the gesture is small and habitual — the cruelty of it is its unconsciousness.",
        "scene": (
            "On the crowded gate steps a tall fine-robed man draws "
            "the hem of his indigo robe aside in one small habitual "
            "motion as a dusty labourer climbs past with a basket "
            "on his shoulder — the robed man's eyes never leaving "
            "his conversation partner, the labourer's face flat "
            "with long practice at being stepped around — contempt "
            "so old it has become posture. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b04", "out": "s04-two-men-went-up-into.jpeg", "seg": "jv10",
        "window": "16.51-22.22", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "PUBLICAN", "TEMPLE"],
        "narration": (
            "Two men went up into the temple to pray; the one a Pharisee, and "
            "the other a publican."
        ),
        "must_show": "SCRIPTURE-EXACT: the two ascents in one frame — the Pharisee climbing the broad steps upright and at home, the publican far behind and lower, climbing bowed.",
        "must_not_show": "no halo, glare or rim-light; the gap between them on the steps is the parable's first geometry — wide, deliberate.",
        "scene": (
            "The broad pale steps of the temple court in bright "
            "mid-morning: near the top the immaculate Pharisee "
            "climbs upright and unhurried, at home on every stone, "
            "his fringed shawl squared — and far below and behind "
            "him, small at the steps' foot, the thickset publican "
            "climbs slowly with his head down and his wine-red "
            "robe gathered, a man arriving somewhere he is not "
            "sure he is allowed. The smoke column stands straight "
            "beyond the inner gates. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b05", "out": "s05-the-other-was-a-tax.jpeg", "seg": "n2",
        "window": "23.96-25.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["PUBLICAN"],
        "narration": "The other was a tax collector.",
        "must_show": "the publican introduced — a close portrait: fleshy careworn face, gaudy good clothes, rings twisted on his fingers, eyes that don't meet the camera.",
        "must_not_show": "no halo, glare or rim-light; prosperity and shame in one face — the money shows and so does what it cost.",
        "scene": (
            "A close portrait in the morning light: the publican's "
            "fleshy careworn face above the gaudy wine-red robe, "
            "short dark beard, a good gold ring being twisted "
            "around one finger by the other hand — and his eyes "
            "angled down and aside, the practiced gaze of a man "
            "who long ago stopped checking faces for welcome. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b06", "out": "s06-and-to-anyone-watching-them.jpeg", "seg": "n2 + n3",
        "window": "25.47-33.92", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "PUBLICAN", "TEMPLE"],
        "narration": (
            "And to anyone watching them climb those steps, it was obvious "
            "which of the two God was pleased with. The Pharisee was not a "
            "fake."
        ),
        "must_show": "the crowd's verdict — worshippers on the steps bowing respectfully to the passing Pharisee while edging away from the publican; the world's scoreboard, plainly posted.",
        "must_not_show": "no halo, glare or rim-light; the respect for the Pharisee is GENUINE and earned — that is what makes the ending land.",
        "scene": (
            "On the wide steps the morning crowd parts two ways at "
            "once: toward the Pharisee, with an old man bowing as "
            "he passes and a mother turning her son to see a "
            "righteous man — and away from the publican, a subtle "
            "widening of space around the wine-red robe, a father "
            "drawing his daughter closer as he passes — one city's "
            "whole verdict rendered in three steps of pavement. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b07", "out": "s07-god-had-asked-for-one.jpeg", "seg": "n3",
        "window": "33.92-38.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEE"],
        "narration": (
            "God had asked for one fast a year, and this man fasted twice a "
            "week."
        ),
        "must_show": "the discipline honest — the Pharisee at dawn at his own plain table, the untouched bread pushed away, praying instead; real, costly devotion.",
        "must_not_show": "no halo, glare or rim-light; NO mockery — the fast is genuinely kept and genuinely hard; his devotion beats are painted admiringly.",
        "scene": (
            "In grey dawn light at a plain table the Pharisee sits "
            "with a round loaf and a cup pushed deliberately to "
            "arm's length, his hands folded on the bare wood where "
            "his meal would be, lips moving in quiet prayer — the "
            "hollow of real hunger in his cheeks and no audience "
            "anywhere — a hard discipline kept twice every week, "
            "alone, exactly as promised. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b08", "out": "s08-he-gave-away-a-tenth.jpeg", "seg": "n3",
        "window": "38.60-42.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEE"],
        "narration": (
            "He gave away a tenth of everything he owned, down to the herbs in "
            "his garden."
        ),
        "must_show": "the tithe of mint — a close shot of the Pharisee's careful hands counting out every tenth sprig from a small herb harvest into a temple basket.",
        "must_not_show": "no halo, glare or rim-light; the smallness of the herbs makes the thoroughness visible — meticulous, honest, complete.",
        "scene": (
            "A close shot over a garden bench at midday: the "
            "Pharisee's long careful fingers counting fresh-cut "
            "mint and dill into two piles — nine sprigs to the "
            "household cloth, the tenth laid precisely into a "
            "small temple basket — the counted rows exact, the "
            "fragrance almost visible, faithfulness carried down "
            "to the smallest green thing he owns. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b09", "out": "s09-ask-that-city-who-its.jpeg", "seg": "n3 + n4",
        "window": "42.81-51.84", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "PUBLICAN"],
        "narration": (
            "Ask that city who its best man was, and every finger would have "
            "pointed at him. The tax collector was exactly what everyone "
            "thought he was."
        ),
        "must_show": "the two reputations in one street — the Pharisee greeted warmly at the market's heart while, at the frame's other side, the publican sits alone at his toll table as people pay without looking at him.",
        "must_not_show": "no halo, glare or rim-light; both reputations DESERVED — the row's honesty depends on it.",
        "scene": (
            "One market street holds both lives: at its bright "
            "centre the Pharisee is warmly surrounded — an elder "
            "clasping his hand, a scribe deferring — while at the "
            "street's shaded edge the publican sits behind his "
            "toll table with its money box and scales, and a "
            "farmer drops coins on the wood without meeting his "
            "eyes, receiving his tally in silence. Both verdicts, "
            "both earned. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r039-b10", "out": "s10-he-worked-for-rome-the.jpeg", "seg": "n4",
        "window": "51.84-60.65", "wide": True, "jesus": False, "ref": False,
        "locks": ["PUBLICAN"],
        "narration": (
            "He worked for Rome, the empire occupying his own country, "
            "collecting from his own neighbors and keeping whatever extra he "
            "could squeeze out of them."
        ),
        "must_show": "SCRIPTURE-EXACT context — the toll table at the town gate: a Roman soldier idling behind the publican's shoulder as he counts a neighbour's coins, the man's family waiting thin-faced with their laden donkey.",
        "must_not_show": "no halo, glare or rim-light; the machinery of it — soldier, table, box — painted plainly; the publican does not enjoy it.",
        "scene": (
            "At the town gate's toll table the publican counts a "
            "thin farmer's coins into the iron-bound box, a bored "
            "Roman soldier leaning on his spear in the shade "
            "behind the table's authority — and beyond the bar, "
            "the farmer's wife and children wait beside their "
            "laden donkey with the particular stillness of people "
            "watching their margin disappear — while the "
            "publican's own face, bent over the count, is closed "
            "like a shutter. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r039-b11", "out": "s11-a-traitor-with-a-money.jpeg", "seg": "n4",
        "window": "60.65-62.62", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "A traitor with a money box.",
        "must_show": "the title object — a close still of the iron-bound money box on the toll table, a Roman seal stamped on its lid, neighbours' coins inside.",
        "must_not_show": "no halo, glare or rim-light; the box alone carries the accusation — no face needed.",
        "scene": (
            "A close still shot on the toll table's scarred wood: "
            "the iron-bound money box with its lid thrown back, "
            "half full of mixed worn coins, the stamped Roman "
            "seal blunt on the lid's inner face — and beside it "
            "the tally sticks and the small scales of a trade "
            "conducted in his own neighbours' bread money. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b12", "out": "s12-and-he-knew-it-the.jpeg", "seg": "n4 + n5",
        "window": "62.62-69.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "TEMPLE"],
        "narration": (
            "And he knew it. The Pharisee took his place out in the open, where "
            "he could be seen, and lifted his hands to pray."
        ),
        "must_show": "SCRIPTURE-EXACT: the stance — the Pharisee at the court's most visible point, front and centre before the inner gates, hands lifted high, eyes open, positioned for an audience.",
        "must_not_show": "no halo, glare or rim-light; the placement IS the tell — maximum visibility chosen as naturally as breathing.",
        "scene": (
            "In the great bright court the Pharisee has taken the "
            "most visible ground in it — front and centre before "
            "the inner gates, on the low step where the light "
            "falls full — and stands with both hands lifted high "
            "and wide, head back, eyes open toward the smoke "
            "column, his fringed shawl hanging in perfect folds — "
            "while around him the scattered worshippers keep "
            "respectfully to the margins his position assumes. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b13", "out": "s13-listen-to-who-his-prayer.jpeg", "seg": "n5",
        "window": "69.86-73.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "TEMPLE"],
        "narration": "Listen to who his prayer is really about.",
        "must_show": "a close shot of the praying Pharisee's face — eyes open, satisfied, a man enjoying his own performance in real time.",
        "must_not_show": "no halo, glare or rim-light; subtle — satisfaction, not villainy; he believes every word he is about to say.",
        "scene": (
            "A close shot of the Pharisee's upturned face in the "
            "full morning light, hands' shadows at the frame's "
            "edge: his eyes are open toward the sky and there is "
            "genuine devotion in them — and settled underneath "
            "it, smooth as oil, the deep contentment of a man "
            "listening to himself pray and finding the prayer "
            "excellent. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r039-b14", "out": "s14-god-i-thank-thee-that.jpeg", "seg": "j1",
        "window": "73.82-81.54", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "PUBLICAN", "TEMPLE"],
        "narration": (
            "God, I thank thee, that I am not as other men are, extortioners, "
            "unjust, adulterers, or even as this publican."
        ),
        "must_show": "SCRIPTURE-EXACT: 'even as this publican' — the Pharisee mid-prayer with his head half-turned, indicating the distant bowed figure at the court's far edge; a prayer with a pointing finger in it.",
        "must_not_show": "no halo, glare or rim-light; the half-turn and glance carry it — the publican far off, unaware, head down.",
        "scene": (
            "Mid-prayer the Pharisee's head has half-turned and "
            "his lifted hand tilted, indicating without quite "
            "pointing — and far across the sunlit paving, at the "
            "court's furthest margin by the portico shadow, the "
            "small bowed wine-red figure of the publican stands "
            "with his head down, unaware of having just been "
            "entered into another man's prayer as the closing "
            "example. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r039-b15", "out": "s15-i-fast-twice-in-the.jpeg", "seg": "j1",
        "window": "81.54-86.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "TEMPLE"],
        "narration": "I fast twice in the week, I give tithes of all that I possess.",
        "must_show": "SCRIPTURE-EXACT: the inventory — the Pharisee's fingers folding down one by one as he counts his merits aloud to heaven.",
        "must_not_show": "no halo, glare or rim-light; counting fingers ARE allowed here and are the point — a ledger recited in the temple.",
        "scene": (
            "Close on the Pharisee in the bright court: one lifted "
            "hand has become a ledger, its long fingers folding "
            "down one at a time as he counts his merits aloud — "
            "the fast, the tithe — his eyes closed now in "
            "concentration on the arithmetic, his fine head "
            "nodding slightly at each item like a merchant "
            "confirming stock. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r039-b16", "out": "s16-he-is-not-asking-god.jpeg", "seg": "n6",
        "window": "88.47-90.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "TEMPLE"],
        "narration": "He is not asking God for anything.",
        "must_show": "the empty transaction — the Pharisee's two lifted hands in close-up: open, upward, and carrying nothing and requesting nothing; hands making a delivery, not a plea.",
        "must_not_show": "no halo, glare or rim-light; hands only — the posture of giving a report, not receiving a gift.",
        "scene": (
            "A close shot of the Pharisee's two lifted hands "
            "against the bright sky over the court: fine, clean, "
            "steady hands held open and upward in the formal "
            "posture of prayer — and carrying, on inspection, "
            "nothing at all: no plea in the curve of them, no "
            "need in the tension of them, hands presenting a "
            "finished account to an auditor. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b17", "out": "s17-he-is-handing-god-a.jpeg", "seg": "n6",
        "window": "90.31-97.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "TEMPLE"],
        "narration": (
            "He is handing God a list of his own achievements. In one short "
            "prayer, he says the word I five times."
        ),
        "must_show": "the five I's — the Pharisee's confident mid-prayer face with his free hand spread, five fingers wide; the count made flesh.",
        "must_not_show": "no halo, glare or rim-light; the open five-fingered hand reads as the tally of I's — composition, not caption.",
        "scene": (
            "Close on the Pharisee mid-prayer: his face lifted "
            "and moving with confident speech, and beside it his "
            "free hand has spread itself wide, all five long "
            "fingers open against the bright court behind — an "
            "accidental tally, five of five, hanging in the air "
            "next to a prayer that is a list. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b18", "out": "s18-and-he-cannot-even-finish.jpeg", "seg": "n6",
        "window": "97.16-101.20", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "PUBLICAN", "TEMPLE"],
        "narration": (
            "And he cannot even finish it without stepping on the man behind "
            "him."
        ),
        "must_show": "the prayer's collateral — over the Pharisee's shoulder, the distant publican small in the frame exactly where the contemptuous glance lands.",
        "must_not_show": "no halo, glare or rim-light; the geometry of contempt — the eyeline from the praying man to the bowed man drawn straight across the court.",
        "scene": (
            "From close behind the Pharisee's shoulder, down his "
            "sight line: across the wide sunlit paving the "
            "publican stands small and bowed at the far margin, "
            "framed precisely in the gap between the Pharisee's "
            "lifted arm and his turned cheek — one man's worship "
            "using another man as its measuring stick, the whole "
            "distance between them fitting inside a glance. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b19", "out": "s19-and-the-publican-standing-afar.jpeg", "seg": "jv13a",
        "window": "101.78-109.63", "wide": True, "jesus": False, "ref": False,
        "locks": ["PUBLICAN", "TEMPLE"],
        "narration": (
            "And the publican, standing afar off, would not lift up so much as "
            "his eyes unto heaven, but smote upon his breast, saying,"
        ),
        "must_show": "SCRIPTURE-EXACT: afar off — the publican alone at the court's farthest edge against the portico shadow, head down, fist against his chest mid-blow.",
        "must_not_show": "no halo, glare or rim-light; the fist on the breast is the mourner's gesture — grief for himself; eyes never rise.",
        "scene": (
            "At the far margin of the great court, half into the "
            "portico's shadow, the thickset publican stands alone "
            "with his head bowed so low his beard touches his "
            "chest — and his right fist is caught mid-blow against "
            "his breastbone, the wine-red robe crumpled under it, "
            "the mourner's strike of a man grieving over his own "
            "life — the vast bright paving lying empty between "
            "him and everything holy. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b20", "out": "s20-the-tax-collector-did-not.jpeg", "seg": "n7",
        "window": "111.28-113.27", "wide": True, "jesus": False, "ref": False,
        "locks": ["PUBLICAN", "TEMPLE"],
        "narration": "The tax collector did not go up front.",
        "must_show": "the distance chosen — the whole court from behind the publican: the bright open ground he will not cross, the inner gates far away, him at the very threshold.",
        "must_not_show": "no halo, glare or rim-light; his BACK to the camera works here — the untaken distance is the picture.",
        "scene": (
            "From just behind the publican at the court's "
            "entrance: his broad wine-red back at the frame's "
            "edge, and beyond him the whole vast sunlit court he "
            "will not walk into — the scattered worshippers, the "
            "far bright steps, the inner gates and the straight "
            "smoke column all standing at a distance he has "
            "measured and declined — a man stopped at the border "
            "of his own welcome. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r039-b21", "out": "s21-he-stopped-at-the-very.jpeg", "seg": "n7",
        "window": "113.27-118.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["PUBLICAN", "TEMPLE"],
        "narration": (
            "He stopped at the very back, as far as a man could get and still "
            "be in the temple."
        ),
        "must_show": "the exact spot — the publican's sandalled feet just inside the court's threshold line, heels nearly on the joint of the outermost paving stones.",
        "must_not_show": "no halo, glare or rim-light; feet and threshold only — the geometry of 'barely in' told at ground level, upright and level frame.",
        "scene": (
            "A close shot at the court's threshold, upright and "
            "level with the paving at the bottom of the frame: "
            "the publican's worn sandalled feet planted just "
            "inside the outermost joint of the great paving "
            "stones, heels a hand's breadth from the line — the "
            "hem of the wine-red robe trembling slightly with the "
            "fist-blows landing above — a man occupying the last "
            "inch of holy ground that will have him. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b22", "out": "s22-he-could-not-bring-himself.jpeg", "seg": "n7",
        "window": "118.02-125.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["PUBLICAN"],
        "narration": (
            "He could not bring himself to lift his eyes. He struck his own "
            "chest, the way people do when someone has died."
        ),
        "must_show": "the grief close up — the publican's downturned face and the fist landing on his chest; a man at his own funeral.",
        "must_not_show": "no halo, glare or rim-light; dignity in the devastation — tears allowed, collapse not.",
        "scene": (
            "Close in the portico's half-shadow: the publican's "
            "fleshy face turned full down, eyes shut and streaming "
            "silently into his short beard, jaw trembling — and "
            "his heavy fist landing again on his breastbone with "
            "the dull weight of the mourner's blow, the ring on "
            "it catching one point of light — a man beating on "
            "the door of his own shut heart. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b23", "out": "s23-and-he-prayed-a-prayer.jpeg", "seg": "n7 + j2",
        "window": "125.10-130.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["PUBLICAN", "TEMPLE"],
        "narration": (
            "And he prayed a prayer of only seven words. God be merciful to me "
            "a sinner."
        ),
        "must_show": "SCRIPTURE-EXACT: the seven words leaving — the publican's cracked lips barely moving, fist stilled against his chest, the whole man reduced to one sentence.",
        "must_not_show": "no halo, glare or rim-light; the smallest prayer in scripture painted at its own scale — quiet, total.",
        "scene": (
            "Very close: the publican's bowed head in the soft "
            "shadow, lips barely parted and barely moving around "
            "the shortest prayer of his life, the fist gone still "
            "and flat against his chest as if holding something "
            "in — and on his wet face, under the shame, the first "
            "terrible hope of a man who has finally said the true "
            "thing out loud. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r039-b24", "out": "s24-there-is-more-in-that.jpeg", "seg": "n8a",
        "window": "132.27-134.38", "wide": True, "jesus": False, "ref": False,
        "locks": ["TEMPLE"],
        "narration": "There is more in that prayer than it sounds like.",
        "must_show": "the setting's depth — the court wide with the sacrifice smoke column rising beyond the inner gates, priests small on the far steps; the machinery of atonement at work behind the little prayer.",
        "must_not_show": "no halo, glare or rim-light; the sacrifice stays DISTANT — smoke and small far figures only, nothing graphic ever.",
        "scene": (
            "The great court wide in the full morning light: "
            "beyond the inner gates the straight pale column of "
            "sacrifice smoke climbs into the bright sky, tiny "
            "far figures of priests moving on the inner steps "
            "beneath it — the whole ancient machinery of "
            "atonement working at the heart of the frame while "
            "the scattered worshippers pray small across the "
            "vast paving. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r039-b25", "out": "s25-he-is-standing-in-the.jpeg", "seg": "n8a",
        "window": "134.38-145.19", "wide": True, "jesus": False, "ref": False,
        "locks": ["PUBLICAN", "TEMPLE"],
        "narration": (
            "He is standing in the temple at the hour of sacrifice, while a "
            "lamb is being killed for the sins of the whole nation, and he is "
            "asking God to let that sacrifice count for him."
        ),
        "must_show": "SCRIPTURE-EXACT: the prayer and the smoke in one frame — the bowed publican small at the court's edge, and above and beyond him the rising sacrifice smoke; his plea visually tied to the offering.",
        "must_not_show": "no halo, glare or rim-light; the tie is compositional — his bowed figure and the far smoke column in one vertical line; the sacrifice itself never shown.",
        "scene": (
            "From low at the court's margin: the bowed wine-red "
            "figure of the publican stands small in the near "
            "frame, fist to chest — and rising directly beyond "
            "and above him, framed in the same vertical, the pale "
            "smoke of the morning offering climbs from behind "
            "the inner gates into the wide sky, one man's seven "
            "words and one nation's lamb ascending in the same "
            "line. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r039-b26", "out": "s26-him-personally.jpeg", "seg": "n8a",
        "window": "145.19-147.04", "wide": False, "jesus": False, "ref": False,
        "locks": ["PUBLICAN"],
        "narration": "Him, personally.",
        "must_show": "the personal pronoun — an extreme close of the publican's hand flattened over his own chest: me, this one, this man.",
        "must_not_show": "no halo, glare or rim-light; one hand on one heart — the whole beat.",
        "scene": (
            "An extreme close shot in the soft shadow: the "
            "publican's heavy hand pressed flat over his own "
            "heart, fingers spread on the crumpled wine-red "
            "wool, the gold ring dull against it — no longer a "
            "fist, a claim: this chest, this ledger, this man — "
            "mercy requested by name for the one address he "
            "answers to. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r039-b27", "out": "s27-and-in-greek-he-does.jpeg", "seg": "n8b",
        "window": "147.69-152.04", "wide": False, "jesus": False, "ref": False,
        "locks": ["PUBLICAN", "TEMPLE"],
        "narration": (
            "And in Luke's Greek, he does not count himself as one guilty man "
            "among many."
        ),
        "must_show": "the singular — the publican utterly alone in his margin of the court, every other worshipper distant; a frame with one subject and much emptiness.",
        "must_not_show": "no halo, glare or rim-light; isolation composed deliberately — 'THE sinner' as one small figure in wide emptiness.",
        "scene": (
            "A wide-margined frame: the publican stands alone in "
            "the empty outer reach of the court, the nearest "
            "other worshipper a distant blur far across the "
            "sunlit paving, the portico's long shadow behind him "
            "— one bowed man in a great emptiness of pale stone, "
            "composed as if the whole building held only him and "
            "the one he is speaking to. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b28", "out": "s28-he-speaks-as-if-he.jpeg", "seg": "n8b + n9",
        "window": "152.04-157.33", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "PUBLICAN", "TEMPLE"],
        "narration": (
            "He speaks as if he were the only one in the building. Two men. The "
            "same temple."
        ),
        "must_show": "SCRIPTURE-EXACT: the diptych — one frame holding both: the Pharisee lifted and lit at the front, the publican bowed and shadowed at the back, the court's whole length between them.",
        "must_not_show": "no halo, glare or rim-light; ONE unified scene (never panels) — the two postures at the two ends of the same paving.",
        "scene": (
            "The whole court in one deep frame: near the bright "
            "inner steps the Pharisee stands tall with his hands "
            "raised, lit full by the morning — and far down the "
            "long perspective of paving, small against the "
            "portico shadow, the publican bows with his fist to "
            "his chest — two men, one house, the same light "
            "falling on both and landing differently, the whole "
            "length of the temple floor stretched between their "
            "two prayers. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r039-b29", "out": "s29-one-of-them-doing-all.jpeg", "seg": "n9",
        "window": "158.61-162.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "PUBLICAN"],
        "narration": "One of them doing all the talking, the other barely able to speak.",
        "must_show": "the two mouths — a paired close composition in ONE scene: the Pharisee's moving, confident mouth in profile near, the publican's pressed, trembling lips far beyond him in the same frame.",
        "must_not_show": "no halo, glare or rim-light; single continuous scene with deep focus — never a split panel.",
        "scene": (
            "A deep-focus close composition in one continuous "
            "scene: in the near foreground the Pharisee's profile "
            "mid-eloquence, mouth open and moving, beard wagging "
            "gently with the flow of words — and far beyond his "
            "shoulder, small and soft down the court's length, "
            "the publican's bowed head with lips pressed almost "
            "shut, barely moving around seven words — fluency and "
            "poverty of speech sharing one frame of morning air. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b30", "out": "s30-and-then-jesus-said-the.jpeg", "seg": "n9",
        "window": "162.47-167.83", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GATE"],
        "narration": (
            "And then Jesus said the sentence that would have stopped every man "
            "listening to him cold."
        ),
        "must_show": "back at the gate — Jesus pausing before the verdict, and the confident listeners' faces beginning, for the first time, to be unsure where this is going.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the pause painted — his stillness, their first flicker of doubt.",
        "scene": (
            "On the gate steps Jesus has gone still before the "
            "story's last sentence, his eyes moving slowly across "
            "the fine-robed listeners — and in that pause the "
            "certainty on their faces has developed its first "
            "hairline cracks: one man's folded arms loosening, "
            "another's chin coming down a degree, the crowd at "
            "the edges leaning in — a whole audience suspended "
            "between a story and its verdict. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b31", "out": "s31-i-tell-you-this-man.jpeg", "seg": "j3",
        "window": "168.39-179.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "PUBLICAN", "TEMPLE"],
        "narration": (
            "I tell you, this man went down to his house justified rather than "
            "the other: for every one that exalteth himself shall be abased; "
            "and he that humbleth himself shall be exalted."
        ),
        "must_show": "SCRIPTURE-EXACT: the reversal on the steps — the publican descending the temple steps UPRIGHT, face washed with peace, passing the level where the Pharisee still stands praying above.",
        "must_not_show": "no halo, glare or rim-light; the verdict is painted as posture — the bowed man now straight, the straight man unchanged; no light effects, only bearing.",
        "scene": (
            "On the broad steps in the high morning light the "
            "publican is coming DOWN — and he is upright: "
            "shoulders open, wet face lifted and washed with a "
            "peace it has plainly never worn before, one hand "
            "loose at his side where the fist was — while above "
            "and behind him on the court's edge the Pharisee "
            "still stands at his prayers, hands raised, exactly "
            "as he was and exactly as he will be. Two directions, "
            "one staircase. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r039-b32", "out": "s32-the-same-god.jpeg", "seg": "n9",
        "window": "157.33-158.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE"],
        "narration": "The same God.",
        "must_show": "the one address — the smoke column alone, rising straight into the bright sky above the inner gates; both prayers went here.",
        "must_not_show": "no halo, glare or rim-light; sky, smoke and gate stone only — the single destination of two very different letters.",
        "scene": (
            "A simple vertical frame: above the pale mass of the "
            "inner gates the single straight column of offering "
            "smoke climbs undisturbed into the wide bright "
            "morning sky, thinning as it rises — one column, one "
            "sky, one listener, receiving in the same minute the "
            "inventory and the seven words. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b33", "out": "s33-the-traitor-walked-home-right.jpeg", "seg": "n10",
        "window": "181.52-186.77", "wide": True, "jesus": False, "ref": False,
        "locks": ["PUBLICAN"],
        "narration": (
            "The traitor walked home right with God. The good man walked home "
            "exactly as he came."
        ),
        "must_show": "the walk home — the publican in the morning street moving like a man whose sentence was lifted an hour ago; lighter in every joint.",
        "must_not_show": "no halo, glare or rim-light; the change carried in gait and face only — the same street that shunned him, walked new.",
        "scene": (
            "Down the warm late-morning street the publican walks "
            "home through the same crowd that edged away from him "
            "at dawn — and everything about his body has changed "
            "weight: the step longer, the head level, one hand "
            "trailing along a sun-warmed wall as if touching "
            "things were new — a man walking home under a debt "
            "that no longer exists. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b34", "out": "s34-not-because-god-is-impressed.jpeg", "seg": "n10",
        "window": "186.77-194.19", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Not because God is impressed by failure, but because one of them "
            "came holding a list, and the other came holding nothing."
        ),
        "must_show": "the two hands of the row — one continuous close scene: a fine hand gripping a written merit-list scroll, and beside it a heavy empty hand open palm-up; list and nothing, side by side.",
        "must_not_show": "no halo, glare or rim-light; ONE scene, not panels — two hands on one table edge in one light.",
        "scene": (
            "A close still composition on a stone ledge in plain "
            "light: at one side a fine long-fingered hand grips a "
            "neat small scroll dense with written lines, knuckles "
            "pale with the holding — and beside it, inches away "
            "in the same light, a heavy ringed hand lies open and "
            "utterly empty, palm up, offering the only thing it "
            "has — nothing — to whoever will take it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b35", "out": "s35-only-one-of-them-was.jpeg", "seg": "n10",
        "window": "194.19-197.36", "wide": False, "jesus": False, "ref": False,
        "locks": ["PUBLICAN"],
        "narration": "Only one of them was actually asking for anything.",
        "must_show": "the asking face — a return to the publican's upturned face at the moment mercy was requested: need, made visible, the only prayer that was a prayer.",
        "must_not_show": "no halo, glare or rim-light; the face carries request — open, emptied, waiting; nothing performed.",
        "scene": (
            "Close in the portico shadow, the moment revisited: "
            "the publican's face lifted just barely for the first "
            "time, wet-eyed and open, every defence gone out of "
            "it — the naked asking face of a man with no list, no "
            "case and no fallback, holding up seven words and an "
            "empty hand. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r039-b36", "out": "s36-he-went-down-those-steps.jpeg", "seg": "n11",
        "window": "197.99-202.58", "wide": True, "jesus": False, "ref": False,
        "locks": ["PUBLICAN", "TEMPLE"],
        "narration": (
            "He went down those steps a different man, and he had not done one "
            "thing to earn it."
        ),
        "must_show": "the descent completed — the publican at the bottom of the temple steps looking back up once, wonder on his face, the whole height of what just happened above him.",
        "must_not_show": "no halo, glare or rim-light; the look back is gratitude, not disbelief-drama; the steps rise behind him like the size of the gift.",
        "scene": (
            "At the foot of the broad pale steps the publican has "
            "stopped and turned, looking back up the whole sunlit "
            "flight to the court's rim high above — one hand "
            "pressed flat over his heart again, but softly now — "
            "wonder moving over his heavy face at the size of a "
            "thing he was handed for free at the top of those "
            "stairs. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r039-b37", "out": "s37-he-had-nothing-to-offer.jpeg", "seg": "n11",
        "window": "202.58-208.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["PUBLICAN"],
        "narration": (
            "He had nothing to offer, and he knew it. That turned out to be the "
            "only thing he needed to get right."
        ),
        "must_show": "the paradox in close — the publican's two empty hands held open before him as he walks, examined like a treasure; the nothing that was enough.",
        "must_not_show": "no halo, glare or rim-light; empty hands studied with the face of a man holding riches.",
        "scene": (
            "Close in the warm street light: the publican has "
            "paused mid-street with his two empty hands held "
            "open before his own face, turning them slowly, "
            "studying their plain emptiness with the absorbed "
            "expression other men give to gold — the only "
            "offering that was ever accepted from him, still "
            "there, still nothing, still enough. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b38", "out": "s38-and-the-pharisee-he-is.jpeg", "seg": "n12",
        "window": "208.98-214.38", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "TEMPLE"],
        "narration": (
            "And the Pharisee? He is still standing there. Still praying. Still "
            "certain."
        ),
        "must_show": "the unmoved man — the court emptier now, the light shifted later, and the Pharisee in exactly his same spot and posture, unchanged by the hour.",
        "must_not_show": "no halo, glare or rim-light; the emptying court around his sameness — time moved, he did not.",
        "scene": (
            "The great court has thinned toward noon, worshippers "
            "drifted away, the shadows shortened under the "
            "porticoes — and at the same front-and-centre spot "
            "the Pharisee stands in the same lifted-hands posture "
            "with the same excellent composure, the last fixed "
            "point of the morning, praying on in a room that has "
            "quietly finished with the hour. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b39", "out": "s39-still-fine-that-is-the.jpeg", "seg": "n12",
        "window": "214.38-218.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEE"],
        "narration": "Still fine. That is the saddest part of it.",
        "must_show": "the sadness of fine — a last close portrait of the Pharisee's composed, contented, untouched face; nothing happened to him today, and that is the tragedy.",
        "must_not_show": "no halo, glare or rim-light; genuinely serene — the frame mourns what the face cannot feel.",
        "scene": (
            "A last close portrait in the flattening noon light: "
            "the Pharisee's fine composed face, eyes closed in "
            "serene devotion, every line of it contented and "
            "complete — a face nothing got into and nothing got "
            "out of, wearing the perfect calm of a man to whom, "
            "this morning in the temple, absolutely nothing "
            "happened. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r039-b40", "out": "s40-the-only-thing-keeping-that.jpeg", "seg": "n12 + n13",
        "window": "218.05-227.00", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GATE"],
        "narration": (
            "The only thing keeping that man out was how sure he was that he "
            "was already in. Jesus did not tell this story to shame the good "
            "men listening."
        ),
        "must_show": "the landing without shaming — Jesus stepping down TOWARD the fine-robed listeners, hand open to them, his face all invitation; their certainty shaken but their dignity intact.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no pointed finger, no triumph — he moves toward the men the story just undid.",
        "scene": (
            "On the gate steps Jesus has come down a step TOWARD "
            "the knot of fine-robed men, one hand open to them at "
            "waist height, his face warm and entirely without "
            "victory — and the men stand shaken but unshamed, one "
            "with his hand at his own chest where the story "
            "landed, another meeting Jesus's eyes with the first "
            "honest uncertainty of his adult life. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r039-b41", "out": "s41-he-told-it-to-let.jpeg", "seg": "n13",
        "window": "227.00-232.04", "wide": True, "jesus": False, "ref": False,
        "locks": ["TEMPLE"],
        "narration": (
            "He told it to let them in too. The door is not closed to people "
            "who have done wrong."
        ),
        "must_show": "the open way — the temple court's entrance from outside at warm midday, gates wide, threshold empty and waiting, the way in unbarred for anyone.",
        "must_not_show": "no halo, glare or rim-light; nobody gatekeeping the frame — an open threshold with light beyond it.",
        "scene": (
            "From the street below at warm midday: the temple "
            "court's outer entrance stands completely open, its "
            "great doors folded back against the pale stone, the "
            "worn threshold empty and lit, the bright court and "
            "the thin far smoke column visible through the "
            "opening — a way in with no one barring it, no line, "
            "no test, standing open in the middle of an ordinary "
            "day. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r039-b42", "out": "s42-it-only-closes-from-the.jpeg", "seg": "n13",
        "window": "232.04-236.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "PUBLICAN", "TEMPLE"],
        "narration": (
            "It only closes from the inside, by people convinced they do not "
            "need it."
        ),
        "must_show": "the closing image — the two men's final positions in one last wide frame: the publican gone small and light down the sunlit street below, the Pharisee fixed at his post above; the open gate between them.",
        "must_not_show": "no halo, glare or rim-light; both men held with compassion — one walking free, one standing captive to his certainty, and the door open between their two fates.",
        "scene": (
            "One last wide frame from the gate's arch: below, "
            "small in the bright street, the publican walks away "
            "light-footed into the ordinary noise of the city — "
            "above, through the open entrance, the Pharisee "
            "stands fixed at his prayers on the court's edge — "
            "and between the two of them the great gate stands "
            "wide open in the warm light, closing on no one, "
            "never having closed on anyone, waiting the way doors "
            "wait. Every figure has two arms, two hands and one "
            "head."
        ),
    },
]
