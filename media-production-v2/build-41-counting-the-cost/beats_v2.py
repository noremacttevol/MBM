#!/usr/bin/env python3
"""V2 beat map — row 41, build-41-counting-the-cost (Luke 14:25-35).

COVERAGE: 58 pictures over 333.1 s = 5.7 s/picture (matches the library density).

LESSON-12 PASS (2026-08-05): this row is a crowd-and-landscape epic, so more
true wides survive than usual — each now states camera-to-back geometry in
its own scene text: b01 b02 b03 b06 b16 b17 b22 b23 b26 b32 b34 b40 b49
b55 b57. Nine former wides were re-covered as tighter shots (b05 b15 b18
b20 b27 b30 b36 b41 b52). b57/b58 were also brought inside the shared
CANDID-FRAME lock: the closing invitation looks a breath PAST the lens,
never into it — the old scene text ordered a direct lens gaze, which the
shared lock forbids on every beat and which would have fought every render.

SCRIPTURE FACTS (Luke 14:25-35 KJV):
  v25   "there went GREAT MULTITUDES with him: and he TURNED, and said" —
        the frame IS the story: an enormous crowd on the open road, and
        Jesus stopping and turning to face them. The turn is a beat.
  v26   "If any man come to me, and HATE not his father..." — the
        narration explains the Semitic idiom (love-less/loved-more; Jacob
        and Leah; Matthew's plain parallel). Family beats are warm and
        good — the point is FIRST PLACE, not hatred.
  v27   "whosoever doth not BEAR HIS CROSS" — RESTRAINED RENDERING: Rome's
        crosses along the highways appear ONLY as distant EMPTY upright
        posts on a rise (no bodies, no gore, ever); the condemned man
        carrying his beam is shown bent under the timber, no wounds.
  v28-30 the tower: "SITTETH NOT DOWN FIRST, and COUNTETH the cost" — the
        sitting-down-to-count is the row's central image, painted twice.
        The half-built tower with weeds is the failure monument.
  v31-32 the two kings: arithmetic, not courage — ten thousand against
        twenty thousand; the embassy sent "while the other is yet a great
        way off." Armies stay DISTANT — massed spear-lines on far slopes,
        never battle, never violence.
  v33   "forsaketh not ALL that he hath" — rendered as release of claim
        (open hands over one's own goods), not confiscation.
  v34-35 salt that lost its savour — Dead Sea salt leached to useless
        look-alike powder; still lifes.
  vNARR the crowd THINS on purpose and he does not lower the price; and
        the teller had already counted HIS own cost — walking to
        Jerusalem while he said it. The closing beats are Jesus walking
        on toward the city at dusk, resolute, and turning at the road's
        start to tell the viewer the truth.

TIME OF DAY: the road frame is one long bright AFTERNOON thinning toward
DUSK as the crowd thins (deliberate arc). The tower vignettes are working
daylight; the kings' council is lamplit tent-evening; the salt still
lifes are flat grey light; the family beats warm domestic light; the
final Jerusalem-road beats are deep dusk with the city far off — all
story-driven.

CONTENT-CARE: row 41 carries the cross-context beats — handled RESTRAINED
as above (empty posts, beam-carrier unharmed, nothing graphic). The
thinning crowd is painted as sober choice, never shame.

CHANGING CONDITION (kept OUT of the locks): the crowd's SIZE — enormous,
then visibly fewer, then a remnant — falls across the row per-beat; and
the light ages from afternoon to dusk with it.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "ROAD": (
        "HIGHWAY LOCK: a broad dirt highway winding south through open "
        "Galilean country — low stone field-walls, olive groves and "
        "terraced slopes to either side, milestone stones at the verge, "
        "and far ahead on the horizon a pale hill-line where the road "
        "goes. The same road, walls and horizon in every road beat."
    ),
    "CROWD": (
        "MULTITUDE LOCK: the crowd on the road is ordinary people of "
        "every age — farmers with staffs, mothers with children, young "
        "men in twos and threes, old couples, tradesmen with packs — in "
        "SATURATED DEEP earth colours: dark browns, deep russet, dark "
        "olive, burnt ochre, dusty indigo, faded plum (never cream, "
        "never white; only Jesus wears cream). Faces shown clearly."
    ),
    "BUILDER": (
        "BUILDER LOCK: the tower builder is the same man in every shot — "
        "about forty-five, stocky and capable, with a short sandy-brown "
        "beard, a broad patient face and lime-dusted forearms. He wears "
        "a DARK TAN work tunic with a leather apron and a cord-wound "
        "measuring reed at his belt (never cream, never white). His "
        "face is shown clearly."
    ),
    "VINEYARD": (
        "VINEYARD SITE LOCK: a hillside vineyard with a cleared corner "
        "for the tower — staked vine rows, a stack of quarried pale "
        "stones, a mortar trough, a laid square foundation course, and "
        "a low spoil heap. The same rows, stone stack and corner "
        "throughout the tower beats."
    ),
    "KING": (
        "KING LOCK: the deliberating king is the same man in every shot "
        "— about fifty, compact and grave, with a close dark beard "
        "shot with grey and a weighing, unhurried gaze. He wears a "
        "DARK SEA-GREEN war tunic under a DEEP BRONZE-BROWN cloak with "
        "a plain iron circlet (never cream, never white). His face is "
        "shown clearly — a counter, not a coward."
    ),
    "WARTENT": (
        "WAR TENT LOCK: the king's council tent at evening — dark "
        "goat-hair walls, a plank table with a sand-map of ridges and "
        "counters of stone, two oil lamps, camp stools, and through "
        "the open flap a dusk valley where distant campfires speck the "
        "far slope. The same table, map and flap view throughout."
    ),
    "FAMILY": (
        "FAMILY LOCK: the family of the first-place beats — a "
        "grey-bearded father, a warm broad mother in a DARK MADDER-RED "
        "dress, a young wife with an infant, and two half-grown "
        "children, all in deep earth-tone wool (never cream, never "
        "white; only Jesus wears cream). Faces shown clearly, painted "
        "warm — they are goods, not rivals."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r041-b01", "out": "s01-by-now-the-crowd-walking.jpeg", "seg": "n1",
        "window": "0.28-2.86", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "CROWD"],
        "narration": "By now the crowd walking with him was enormous.",
        "must_show": "the scale — the broad highway filled shoulder to shoulder as far as it bends, Jesus a small cream point moving at its head.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the crowd's size is the subject — the road full out of sight.",
        "scene": (
            "From a rise beside the highway in bright afternoon "
            "light, the camera taking the column from the side: "
            "the broad dirt road runs full from verge to "
            "verge with walking people — hundreds visible before "
            "the first bend and the dust of hundreds more beyond "
            "it — and far up at the column's head one small "
            "cream-clad figure walks steadily south, the whole "
            "river of the crowd flowing after him between the "
            "stone field-walls. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r041-b02", "out": "s02-thousands-filling-the-road-more.jpeg", "seg": "n1",
        "window": "4.38-8.37", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD", "CROWD"],
        "narration": "Thousands, filling the road, more joining at every village.",
        "must_show": "the swelling — at a village junction, new families hurrying down a side lane to fold into the passing multitude, bread still in hand.",
        "must_not_show": "no halo, glare or rim-light; momentum and festival energy — joining is effortless, which is the setup for what follows.",
        "scene": (
            "Where a village lane meets the highway the crowd is "
            "swelling in real time, the camera on the far verge "
            "taking the junction from the side: a family hurries down the "
            "lane still tying bundles, a potter abandons his "
            "wheel in the doorway wiping clay on his apron, two "
            "boys run the wall-top to catch up — all folding "
            "into the great passing column with the easy "
            "excitement of people joining a festival that asks "
            "nothing at the gate. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r041-b03", "out": "s03-and-there-went-great-multitudes.jpeg", "seg": "s25",
        "window": "12.06-16.80", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "CROWD"],
        "narration": (
            "And there went great multitudes with him: and he turned, and said "
            "unto them,"
        ),
        "must_show": "SCRIPTURE-EXACT: THE TURN — Jesus stopped and fully turned to face the oncoming thousands, the front of the crowd compressing to a halt around him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the turn against the flow is the whole composition — one man facing a river.",
        "scene": (
            "In the middle of the broad road Jesus has stopped "
            "and turned completely around, the camera just "
            "behind his shoulder facing back into the "
            "oncoming multitude with him — and the crowd's front rank "
            "piles gently to a halt around him, those behind "
            "still pressing forward, heads craning, the whole "
            "vast column compressing like water against a stone "
            "— one still figure facing thousands in the bright "
            "afternoon. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r041-b04", "out": "s04-and-then-he-turned-around.jpeg", "seg": "n2",
        "window": "18.38-19.52", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": "And then he turned around.",
        "must_show": "the turn close — Jesus's face coming around toward the camera-crowd, grave and deliberate; the moment the festival meets the truth.",
        "must_not_show": "no halo, glare or rim-light on Jesus; gravity without anger — a man about to be honest with people he loves.",
        "scene": (
            "Close in the road's bright light: Jesus's face caught "
            "mid-turn, coming around toward the halted crowd with "
            "the dust of the stop still drifting past his "
            "shoulder — his warm brown eyes grave and utterly "
            "deliberate, the face of a man who has decided that "
            "the kindest thing he can do to a parade is tell it "
            "the truth. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r041-b05", "out": "s05-he-started-talking-them-out.jpeg", "seg": "n2",
        "window": "23.63-25.77", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD", "CROWD"],
        "narration": "He started talking them out of it.",
        "must_show": "the anti-recruitment — past the front rank's shoulders onto Jesus mid-sentence, one hand raised; the nearest faces at the frame's edges registering the first shock.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the crowd's surprise is the subject — festival faces meeting a price list.",
        "scene": (
            "Past the shoulders of the front rank: Jesus stands "
            "mid-sentence with one hand raised — and at the "
            "frame's near edges the festival is dying on the "
            "faces: a young man's grin fading half-formed, a "
            "mother's brows drawing together, an old farmer "
            "leaning in as if he misheard — the first ripple of "
            "a crowd discovering that the man they are following "
            "has started raising the price. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b06", "out": "s06-if-any-man-come-to.jpeg", "seg": "j1",
        "window": "26.26-38.56", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "CROWD"],
        "narration": (
            "If any man come to me, and hate not his father, and mother, and "
            "wife, and children, and brethren, and sisters, yea, and his own "
            "life also, he cannot be my disciple."
        ),
        "must_show": "SCRIPTURE-EXACT: the hard saying delivered whole — Jesus speaking it steadily down the crowded road, families in the crowd instinctively drawing closer together as it lands.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the instinctive clutch of families is the visual echo — husbands' arms around wives, children pulled in.",
        "scene": (
            "Down the length of the halted crowd the sentence "
            "lands visibly, the camera looking along the column "
            "from beside Jesus, the nearest families in "
            "three-quarter: a husband's arm comes around his "
            "wife's shoulders without his knowing it, a mother's "
            "hand finds the top of her boy's head, an old man "
            "reaches for his brother's sleeve — the whole road "
            "quietly clutching the very loves being named — while "
            "Jesus speaks on steadily at the front, sparing them "
            "nothing. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r041-b07", "out": "s07-second-picture-higher-stakes.jpeg", "seg": "n8",
        "window": "160.81-162.88", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "WARTENT"],
        "narration": "Second picture, higher stakes.",
        "must_show": "the second parable opens — the war tent at evening: the king at his sand-map table, lamps lit, the weighing begun.",
        "must_not_show": "no halo, glare or rim-light; council calm — stakes carried by the map and the counters, not by drama.",
        "scene": (
            "Inside the dark goat-hair tent at evening, the "
            "camera holding the council from the side wall, the "
            "compact grey-shot king stands over the plank table "
            "where a sand-map of ridges is laid out, stone "
            "counters standing in two unequal clusters on its "
            "slopes — two oil lamps burning at the table's "
            "corners and, through the open flap behind him, the "
            "dusk valley pricked with the distant campfires of "
            "somebody else's larger army. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b08", "out": "s08-that-word-stops-people-cold.jpeg", "seg": "n3",
        "window": "40.09-42.03", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD", "ROAD"],
        "narration": "That word stops people cold.",
        "must_show": "the word landing — a close shot of three stopped faces in the crowd, the word 'hate' visibly caught in them like a thorn.",
        "must_not_show": "no halo, glare or rim-light; shock without melodrama — faces doing arithmetic they don't like.",
        "scene": (
            "Close along the front of the halted crowd: three "
            "faces in the bright afternoon, each stopped cold in "
            "its own way — a young husband gone rigid with his "
            "jaw dropped a fraction, an old woman's eyes "
            "narrowed hard, a teenage boy looking quickly from "
            "face to face to see if the others heard what he "
            "heard. One word, lodged. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b09", "out": "s09-you-said-hate-and-everybody.jpeg", "seg": "n3",
        "window": "46.51-49.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY"],
        "narration": "You said hate, and everybody heard a comparison.",
        "must_show": "the idiom's true shape — the warm family at their table, and one place of honour at its head standing empty and waiting: first place, held open.",
        "must_not_show": "no halo, glare or rim-light; nothing dark in the frame — a loving family and one seat that outranks even them.",
        "scene": (
            "In warm lamplight the family sits gathered at their "
            "supper table — the grey father, the broad warm "
            "mother, the young wife rocking her infant, the "
            "children shoulder to shoulder — a picture of "
            "everything good — and at the table's head one seat "
            "of honour stands deliberately empty, cup set, bread "
            "laid, kept open for whoever is to be loved first. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b10", "out": "s10-jacob-hated-leah-and-it.jpeg", "seg": "n3",
        "window": "49.85-54.63", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Jacob hated Leah, and it only ever meant he loved Rachel more.",
        "must_show": "the old idiom's witness — a patriarch-era vignette: a tent doorway where a man's attention turns to one of two women drawing water, both dignified; the comparison, not cruelty.",
        "must_not_show": "no halo, glare or rim-light; NEITHER woman demeaned — both painted with dignity; only the direction of the man's step tells the idiom.",
        "scene": (
            "In the bronze light of an older age, before a "
            "goat-hair tent: two dignified women in deep-dyed "
            "wool draw water at a stone well — and the "
            "robed man crossing the camp has turned toward one "
            "of them mid-stride, his whole body's direction "
            "choosing, while the other woman stands equally tall "
            "in the same light, unlessened — an ancient word "
            "meaning nothing more than the angle of a man's "
            "step. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r041-b11", "out": "s11-matthew-wrote-the-same-teaching.jpeg", "seg": "n3",
        "window": "54.63-60.67", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Matthew wrote the same teaching plainly: anyone who loves father "
            "or mother more than me."
        ),
        "must_show": "the parallel text — a close still of two open scroll columns side by side on a copyist's table, a reed pen resting between them; the same teaching in two hands.",
        "must_not_show": "no halo, glare or rim-light; dense ancient script only, no legible modern words; the two-columns-one-truth composition carries it.",
        "scene": (
            "A close still shot on a copyist's table in window "
            "light: two parchment scrolls lie open side by side, "
            "their dense hand-lettered columns running parallel, "
            "a reed pen and ink pot resting in the valley "
            "between them, one column's margin bearing a small "
            "worn thumb-mark where readers have returned to the "
            "same line for a lifetime. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b12", "out": "s12-he-is-asking-for-first.jpeg", "seg": "n3 + n4",
        "window": "63.21-67.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY"],
        "narration": "He is asking for first place. And he was not softening it.",
        "must_show": "first place literal — the family's table again, closer: the empty seat of honour at the head, and every other full seat visibly SECOND to it.",
        "must_not_show": "no halo, glare or rim-light; the geometry of precedence — one head seat, all else ranked after; warm, not cold.",
        "scene": (
            "Closer on the lamplit table: the empty seat of "
            "honour at the head with its set cup catching the "
            "light — and the whole warm ring of the family "
            "arranged down-table from it, the grey father "
            "himself seated at its right hand rather than in it, "
            "his own place voluntarily second — a household "
            "whose order is its confession. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b13", "out": "s13-first-place-is-the-one.jpeg", "seg": "n4",
        "window": "67.77-75.59", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "First place is the one seat you cannot give to two people. For "
            "most of us, what keeps us from him is not some sin."
        ),
        "must_show": "the single seat — a close still of one carved chair alone in clean light; one seat, by nature un-shareable.",
        "must_not_show": "no halo, glare or rim-light; one chair, one light, nothing else — the frame as a syllogism.",
        "scene": (
            "A quiet still shot in clean plain light: one simple "
            "carved wooden chair standing alone on a stone "
            "floor, its seat worn smooth, a single band of "
            "window light across it — one place wide, one place "
            "deep, incapable by its own carpentry of holding "
            "two occupants — the whole argument standing on "
            "four legs. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r041-b14", "out": "s14-it-is-something-good-we.jpeg", "seg": "n4",
        "window": "75.59-77.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY"],
        "narration": "It is something good we love more.",
        "must_show": "the good rival — a father's face bent over his sleeping infant, love total and lawful; the kind of good thing that takes first place.",
        "must_not_show": "no halo, glare or rim-light; NOTHING sinister — the danger is precisely that this is beautiful.",
        "scene": (
            "Close in the warm lamplight: the young father's "
            "face bent low over the infant asleep on his "
            "forearm, his whole expression dissolved in a love "
            "with no flaw in it anywhere — the truest, cleanest "
            "rival first place will ever have, painted at full "
            "warmth, asleep on the arm of the man it owns. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b15", "out": "s15-and-whosoever-doth-not-bear.jpeg", "seg": "j2",
        "window": "78.43-83.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROAD", "CROWD"],
        "narration": (
            "And whosoever doth not bear his cross, and come after me, cannot "
            "be my disciple."
        ),
        "must_show": "SCRIPTURE-EXACT: the second saying landing — a close knot of three listeners going pale as the word arrives; this word they know by sight.",
        "must_not_show": "no halo, glare or rim-light; no cross in this frame — the WORD lands first; the picture follows in the next beats.",
        "scene": (
            "Close on a knot of three listeners in the bright "
            "road light as the second saying lands: a woman's "
            "hand rising to her mouth, an old man's eyes "
            "closing briefly, two young men exchanging one "
            "flat look over her head — faces going pale rather "
            "than puzzled, a crowd hearing a word they have "
            "all, every one of them, seen with their own eyes "
            "beside a road like this one. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b16", "out": "s16-nobody-in-that-road-heard.jpeg", "seg": "n5",
        "window": "85.27-94.05", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD", "CROWD"],
        "narration": (
            "Nobody in that road heard a figure of speech. Rome crucified "
            "people along the highways of Galilee, out in the open, where "
            "everybody walked past."
        ),
        "must_show": "RESTRAINED: the context — the highway passing beneath a rocky rise where two bare EMPTY upright posts stand against the sky, travellers below averting their eyes as they pass.",
        "must_not_show": "no halo, glare or rim-light; EMPTY posts only — no bodies, no crossbeams occupied, nothing graphic; the averted eyes carry the dread.",
        "scene": (
            "Where the highway passes beneath a barren rocky "
            "rise, two weathered upright wooden posts stand bare "
            "and empty against the hard afternoon sky — Rome's "
            "standing furniture — and the camera holds the road "
            "from its far side, the walking families passing in "
            "profile below, every face bent away from the rise, "
            "eyes fixed forward as "
            "they pass, a father angling his son to his far "
            "side, a woman drawing her shawl across her face, "
            "the whole crowd's gaze bent away from the hill by "
            "long habit. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r041-b17", "out": "s17-and-the-condemned-man-carried.jpeg", "seg": "n5",
        "window": "94.05-98.32", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "And the condemned man carried the beam himself, through his own "
            "town."
        ),
        "must_show": "RESTRAINED: the beam-carrier — a man bent under a heavy rough timber across his shoulders, two soldiers walking him through a town street, townsfolk still in doorways; no wounds, no gore.",
        "must_not_show": "no halo, glare or rim-light; the man unmarked and unbloodied — the WEIGHT and the walk are the whole image; faces in doorways grieved, not gawking.",
        "scene": (
            "Through a narrow town street, the camera holding "
            "the way from the side so the walk crosses the "
            "frame in profile, a man walks bent "
            "nearly double under a rough squared timber laid "
            "across both shoulders, his hands roped up over its "
            "ends, two bored soldiers pacing him — and the town "
            "stands still for it: a potter frozen at his wheel, "
            "a woman turned to the wall with her jar, an old "
            "man in a doorway with his hand over his beard — a "
            "man carrying the instrument through streets that "
            "know his name. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r041-b18", "out": "s18-for-which-of-you-intending.jpeg", "seg": "j3",
        "window": "98.93-107.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["BUILDER", "VINEYARD"],
        "narration": (
            "For which of you, intending to build a tower, sitteth not down "
            "first, and counteth the cost, whether he have sufficient to finish "
            "it?"
        ),
        "must_show": "SCRIPTURE-EXACT: the sitting down — the builder SEATED on his own stone stack before one stone is laid, counting on a tally slate against his knee, the cleared corner waiting.",
        "must_not_show": "no halo, glare or rim-light; sitting BEFORE building — the stack unbroached, the foundation not yet begun; counting as the first act of construction.",
        "scene": (
            "At the vineyard's cleared corner in working morning "
            "light the stocky builder sits on his own stack of "
            "quarried pale stones — not one of them yet laid — "
            "with a slate tilted against his knee and the "
            "cord-wound measuring reed across his lap, scoring "
            "tallies with a flint and looking from the slate to "
            "the stack to the empty corner and back — a tower "
            "being built first, entirely, in arithmetic. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b19", "out": "s19-that-nothing-is-off-limits.jpeg", "seg": "n10",
        "window": "222.99-225.55", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "That nothing is off limits to him.",
        "must_show": "no held-back corner — a house's every door standing open in one view down its rooms, keys left in the last lock; total access granted.",
        "must_not_show": "no halo, glare or rim-light; openness as architecture — a home with no locked room left.",
        "scene": (
            "Down the length of a modest stone house the view "
            "runs through doorway after doorway, every door "
            "standing open in line — the storeroom, the sleeping "
            "room, the inner chamber — morning light falling "
            "through them in successive panels to the small "
            "furthest room, where an iron key has been left "
            "sitting IN its own lock, surrendered — a house with "
            "no corner kept back from its owner's Lord. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b20", "out": "s20-a-watchtower-in-a-vineyard.jpeg", "seg": "n6",
        "window": "109.05-115.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": (
            "A watchtower in a vineyard guarded the harvest you had worked all "
            "year for. Everyone there had built something."
        ),
        "must_show": "the tower's purpose — a FINISHED watchtower in a neighbouring vineyard at dusk, a watchman on its top platform over the ripening rows; what the building is FOR.",
        "must_not_show": "no halo, glare or rim-light; a finished example first — so the half-built failure later has something to fail against.",
        "scene": (
            "On the neighbouring slope in warm early-dusk light "
            "a finished stone watchtower stands over its "
            "vineyard, squat and sound, a watchman leaning at "
            "the rail of its top platform with the ripening "
            "rows spread dark and laden below him and a fox-"
            "scaring sling loose in his hand — the whole "
            "year's harvest sleeping safe inside the circle of "
            "one paid-for building. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b21", "out": "s21-and-they-all-knew-you.jpeg", "seg": "n6",
        "window": "115.10-119.96", "wide": False, "jesus": False, "ref": False,
        "locks": ["BUILDER", "VINEYARD"],
        "narration": (
            "And they all knew you do not start with the stones. You start "
            "sitting on them."
        ),
        "must_show": "the craft's first rule — close on the builder seated on the stone stack, slate in hand; the posture of counting AS the posture of wisdom.",
        "must_not_show": "no halo, glare or rim-light; stillness before labour — hands on slate, not on stone.",
        "scene": (
            "Close in the morning light: the builder settled on "
            "the cold pale stones of his own stack, elbows on "
            "his knees, the slate of tallies held in both "
            "lime-dusted hands, his broad face bent over the "
            "figures with a craftsman's unhurried patience — the "
            "stones beneath him doing their first and most "
            "important job: being sat on. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b22", "out": "s22-not-a-dozen-men.jpeg", "seg": "n1",
        "window": "2.86-4.38", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD", "CROWD"],
        "narration": "Not a dozen men.",
        "must_show": "the contrast of scale — the crowd from road level: a wall of walking people filling the frame edge to edge, no end visible.",
        "must_not_show": "no halo, glare or rim-light; sheer human mass — the dozen this movement started with, swallowed whole.",
        "scene": (
            "From road level at the verge, the camera taking "
            "the passing column from the side: walking people "
            "fill the frame from stone wall to stone wall and "
            "back into their own dust, all crossing in profile, "
            "staffs and bundles and children on shoulders, rank "
            "behind rank behind rank until faces dissolve into "
            "the shimmer — a movement that was twelve men "
            "around a fire not two years ago. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b23", "out": "s23-lest-haply-after-he-hath.jpeg", "seg": "jv29",
        "window": "120.52-133.71", "wide": True, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": (
            "Lest haply, after he hath laid the foundation, and is not able to "
            "finish it, all that behold it begin to mock him, Saying, This man "
            "began to build, and was not able to finish."
        ),
        "must_show": "SCRIPTURE-EXACT: the mockery — the abandoned foundation, three courses high with weeds, and passers-by on the road laughing toward it, one pointing; the monument to not-counting.",
        "must_not_show": "no halo, glare or rim-light; the builder himself ABSENT — the mockery lands on the stones; weeds through the courses date the failure.",
        "scene": (
            "At the vineyard corner the failure stands three "
            "courses high and years old, the camera in the vine "
            "rows behind the courses looking past them down to "
            "the road: a squared foundation "
            "of good pale stone with tall dry weeds growing up "
            "through its middle, the stone stack beside it "
            "slumped and lichened — and on the road below, two "
            "passing farmers have stopped to enjoy it, one "
            "pointing with his staff, both laughing, a joke the "
            "whole district has told at harvest for years. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b24", "out": "s24-because-half-a-tower-is.jpeg", "seg": "n7",
        "window": "135.27-137.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": "Because half a tower is worse than none.",
        "must_show": "the comparison in one frame — the weedy abandoned courses in the foreground, and on the far slope the FINISHED tower standing complete; half against whole.",
        "must_not_show": "no halo, glare or rim-light; both towers in one look — the argument as landscape.",
        "scene": (
            "From low beside the abandoned foundation: the "
            "weed-split courses fill the near frame, lichen on "
            "the good wasted stone — and beyond them, small and "
            "sound on the far slope in the same light, the "
            "neighbouring vineyard's finished watchtower stands "
            "complete with its watchman at the rail — the whole "
            "and the half, weighed in a single glance of "
            "country. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r041-b25", "out": "s25-an-empty-field-is-just.jpeg", "seg": "n7",
        "window": "137.57-147.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": (
            "An empty field is just a field. A foundation with three courses of "
            "stone and weeds growing through it is a monument to a man who did "
            "not think it through."
        ),
        "must_show": "the monument close — the abandoned courses at golden hour, weeds seeding in the wind off the top course; failure made permanent and public.",
        "must_not_show": "no halo, glare or rim-light; the stone is GOOD stone — the tragedy is the plan, not the material.",
        "scene": (
            "Close on the abandoned foundation in low golden "
            "light: three true, well-laid courses of pale stone "
            "— honest work, square corners — and rising through "
            "the middle of them a stand of dry seeding weeds "
            "leaning in the evening wind, drifting their seed "
            "off the top course like smoke — good stone keeping "
            "a bad decision on public display through its "
            "fourth summer. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r041-b26", "out": "s26-this-is-the-moment-every.jpeg", "seg": "n1",
        "window": "8.37-11.56", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "CROWD"],
        "narration": "This is the moment every movement dreams about.",
        "must_show": "the summit of momentum — the vast crowd cresting a rise behind Jesus, banners of dust, the scale at its peak; everything a movement wants.",
        "must_not_show": "no halo, glare or rim-light on Jesus; triumph-shaped — deliberately, because he is about to spend it.",
        "scene": (
            "The multitude crests a long rise in the bright "
            "afternoon like a slow wave, the camera below the "
            "crest taking the column from the side — the road's whole "
            "width pouring over the hilltop behind the small "
            "cream figure at its head, dust standing off the "
            "column like banners, children riding shoulders, "
            "somebody's song carrying thin over the mass — the "
            "exact picture every movement in history has "
            "marched toward, owned for one afternoon by a man "
            "about to give it away. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b27", "out": "s27-or-what-king-going-to.jpeg", "seg": "j5",
        "window": "147.80-159.32", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING", "WARTENT"],
        "narration": (
            "Or what king, going to make war against another king, sitteth not "
            "down first, and consulteth whether he be able with ten thousand to "
            "meet him that cometh against him with twenty thousand?"
        ),
        "must_show": "SCRIPTURE-EXACT: the king SITTING DOWN — the king dropped onto a camp stool at the sand-map, moving stone counters with one finger: ten against twenty, counted honestly.",
        "must_not_show": "no halo, glare or rim-light; the sitting mirrors the builder's — the row's repeated posture; the counters' two clusters visibly unequal.",
        "scene": (
            "In the lamplit tent the king has sat down hard on "
            "a camp stool at the map table, chin on his fist, "
            "one finger pushing the stone counters across the "
            "sand ridges — his own cluster of ten stones drawn "
            "into a tight square, the enemy's twenty spread "
            "wide across the far slope of the map — while his "
            "two captains wait silent behind him, watching a "
            "king do a merchant's honest arithmetic by "
            "lamplight. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r041-b28", "out": "s28-and-he-did-the-last.jpeg", "seg": "n2",
        "window": "19.52-23.63", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD", "CROWD"],
        "narration": (
            "And he did the last thing you would expect from a man with a crowd "
            "that size."
        ),
        "must_show": "the anti-climax poised — close on Jesus facing the crowd in the hush before he speaks, the multitude's expectant faces banked behind; a leader about to spend his capital.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hush is the frame — thousands waiting for a rally and about to get a reckoning.",
        "scene": (
            "Close at the column's head: Jesus stands facing "
            "the halted thousands in a hush you can almost "
            "hear, the nearest faces banked behind him out of "
            "focus and expectant, a child hoisted higher to "
            "see — and on his face, plainly, is nothing a "
            "crowd-keeper would recognize: no pleasure in the "
            "number, only the settled look of a man about to "
            "spend all of it on the truth. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b29", "out": "s29-and-look-at-what-he.jpeg", "seg": "n8",
        "window": "162.88-167.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING", "WARTENT"],
        "narration": "And look at what he asks about the king. Not whether he is brave.",
        "must_show": "courage set aside — the king's sword and helmet hung UNTOUCHED on the tent post behind him while he counts; bravery present, unconsulted.",
        "must_not_show": "no halo, glare or rim-light; the hung arms are the beat — the question on the table is not the one on the post.",
        "scene": (
            "In the tent's lamplight the king's fine sword "
            "hangs sheathed on the tent post beside his "
            "crested iron helmet, both catching the flame "
            "dully, both untouched — while beyond them at the "
            "table their owner sits bent over stones and sand "
            "with a counter between finger and thumb — a brave "
            "man's bravery hung up on a post while he asks "
            "himself a different question entirely. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b30", "out": "s30-whether-he-can-count-an.jpeg", "seg": "n8",
        "window": "167.35-175.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": (
            "Whether he can count. An army of ten thousand against an army of "
            "twenty thousand is arithmetic, not courage."
        ),
        "must_show": "the arithmetic made landscape — from a ridgeline at dusk: the king's compact camp on the near slope, and across the valley the enemy's fires spread TWICE as wide; the count visible in firelight.",
        "must_not_show": "no halo, glare or rim-light; distant camps only — no battle, no clash, ever; the two fields of fires do the math.",
        "scene": (
            "From a dark ridgeline at full dusk the valley "
            "tells the whole sum: on the near slope the king's "
            "camp burns in a tight disciplined grid of perhaps "
            "a hundred fires — and across the black valley "
            "floor the enemy's fires spread along the far "
            "hillside twice as wide and twice as deep, a "
            "second sky of sparks laid over the land — "
            "arithmetic written in firelight, readable by "
            "anyone honest enough to look. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b31", "out": "s31-but-in-the-language-he.jpeg", "seg": "n3",
        "window": "42.03-46.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD", "ROAD"],
        "narration": "But in the language he spoke, there was no way to say love less.",
        "must_show": "the idiom's gap — two listeners mid-crowd turning to each other, hands sketching the missing word in the air between them; a language reaching for a comparative it doesn't have.",
        "must_not_show": "no halo, glare or rim-light; conversation, not distress — two men worrying a word like a knot.",
        "scene": (
            "Mid-crowd in the afternoon light two grey-bearded "
            "listeners have turned to each other, the road "
            "forgotten — one with his hand tilted side to side "
            "in the air between them, weighing an invisible "
            "word, the other frowning and offering a different "
            "shape with both palms — two old men bargaining "
            "with their own language for a gentler word it "
            "simply does not stock. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b32", "out": "s32-or-else-while-the-other.jpeg", "seg": "j6",
        "window": "175.91-183.85", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": (
            "Or else, while the other is yet a great way off, he sendeth an "
            "ambassage, and desireth conditions of peace."
        ),
        "must_show": "SCRIPTURE-EXACT: the embassy — three unarmed envoys with an olive branch riding out across the wide open ground between the two distant camps at first light.",
        "must_not_show": "no halo, glare or rim-light; the open ground between armies is the picture — peace sought while distance remains.",
        "scene": (
            "At first grey-gold light, the camera on the king's "
            "slope looking down the valley, three envoys ride out "
            "unarmed across the wide empty floor in profile, the "
            "leader holding up a green olive branch that "
            "catches the early sun — behind them the king's "
            "tight camp still smoking on the near slope, far "
            "ahead the great sprawl of the enemy's lines just "
            "waking on the other — and between the two armies, "
            "nothing but open ground and three men using it "
            "while it is still there. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b33", "out": "s33-and-the-wise-king-does.jpeg", "seg": "n9",
        "window": "185.41-189.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING", "WARTENT"],
        "narration": "And the wise king does not win the war. He does not fight it.",
        "must_show": "wisdom's anticlimax — the king watching his envoys go from the tent flap, hand resting on the post, the sword still hung; a victory that looks like nothing.",
        "must_not_show": "no halo, glare or rim-light; no triumph imagery — the unfought war is the whole point.",
        "scene": (
            "At the open tent flap in the early light the "
            "compact king stands watching his three envoys "
            "shrink across the valley floor, one hand resting "
            "up on the tent post beside the still-sheathed "
            "sword, his grave face unreadable — a king winning "
            "the only way arithmetic allowed, in a picture with "
            "no banners in it anywhere. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b34", "out": "s34-he-sends-men-to-ask.jpeg", "seg": "n9",
        "window": "189.24-196.07", "wide": True, "jesus": False, "ref": False,
        "locks": ["BUILDER", "KING"],
        "narration": (
            "He sends men to ask for terms while there is still open ground "
            "between the armies. Both stories turn on one act."
        ),
        "must_show": "the shared act named — one continuous frame holding both sitters: the builder seated on his stones in his corner of the frame's world, the king seated at his map in his; the same posture twice.",
        "must_not_show": "no halo, glare or rim-light; ONE unified scene (never split panels) — a dusk landscape where vineyard corner and camp tent both truly sit.",
        "scene": (
            "One deep dusk landscape holds them both, the "
            "camera high on the valley's shoulder behind the "
            "vineyard corner: in the "
            "near ground the builder sits on his pale stone "
            "stack at the vineyard corner, slate on knee, a "
            "small figure bent in thought — and far down the "
            "same darkening valley the king's lamplit tent "
            "stands open-flapped, the seated silhouette at its "
            "map table just readable inside — two men, miles "
            "apart in one country, folded into the identical "
            "shape of sitting down first. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b35", "out": "s35-a-man-sits-down-while.jpeg", "seg": "n9",
        "window": "196.07-200.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["BUILDER", "VINEYARD"],
        "narration": "A man sits down while he still can, and tells himself the truth.",
        "must_show": "the act at its purest — close on the builder seated, slate lowered, eyes lifted from the figures to the middle distance: the moment of honest verdict.",
        "must_not_show": "no halo, glare or rim-light; the look past the slate is the beat — arithmetic finished, truth being told inside.",
        "scene": (
            "Close in the last working light: the builder still "
            "seated on his stones, but the slate has sunk to "
            "rest against his knee and his eyes have lifted off "
            "the tallies to the middle distance, his broad face "
            "gone quiet around a verdict — the stillest moment "
            "a building site ever holds, a man alone with a "
            "true number and deciding to believe it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b36", "out": "s36-so-likewise-whosoever-he-be.jpeg", "seg": "j7",
        "window": "200.74-207.84", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD", "CROWD"],
        "narration": (
            "So likewise, whosoever he be of you that forsaketh not all that he "
            "hath, he cannot be my disciple."
        ),
        "must_show": "SCRIPTURE-EXACT: the sum stated — a medium shot of Jesus in the long amber light, his open hand turning palm-up and over in the 'all' gesture; two listener profiles at the frame's edges, each alone inside the word.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the afternoon visibly aged — the road's light keeping time with the sermon.",
        "scene": (
            "A medium shot in the long amber light: Jesus "
            "brings both parables home with one open hand "
            "turning slowly palm-up and over in the gesture of "
            "everything — and at the frame's near edges two "
            "listeners' profiles have stopped being an audience "
            "and become individuals, each visibly somewhere "
            "alone inside the word 'all', the festival gone "
            "entirely out of the afternoon. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b37", "out": "s37-he-was-not-telling-them.jpeg", "seg": "n10",
        "window": "209.34-212.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD", "ROAD"],
        "narration": (
            "He was not telling them to sell their houses in the road that "
            "afternoon."
        ),
        "must_show": "the misreading declined — a farmer in the crowd clutching his pack to his chest, and his neighbour's gentle hand on his arm easing it back down; not that, friend.",
        "must_not_show": "no halo, glare or rim-light; a small human comedy — panic met by sense.",
        "scene": (
            "Mid-crowd in the amber light a worried farmer has "
            "hugged his whole travelling pack up to his chest "
            "like a man ready to surrender it on the spot — and "
            "his older neighbour's weathered hand rests gently "
            "on his forearm, easing the pack back down, the old "
            "man's face saying not-that with the patience of "
            "someone who has misunderstood a rabbi or two in "
            "his time. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r041-b38", "out": "s38-the-word-means-letting-go.jpeg", "seg": "n10",
        "window": "212.83-220.16", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The word means letting go of your claim. No longer keeping one "
            "corner of your life back as the part he does not get to touch."
        ),
        "must_show": "release of claim — two hands unclenching from around a small locked coffer and laying flat on its lid, leaving it closed but claimed no longer.",
        "must_not_show": "no halo, glare or rim-light; the coffer STAYS — nothing is taken; only the grip changes.",
        "scene": (
            "A close shot in warm evening light: a small "
            "iron-cornered wooden coffer on a table, and around "
            "it two hands caught in the act of unclenching — "
            "the white-knuckled grip loosening finger by finger "
            "until both palms lie flat and quiet on the closed "
            "lid, the box unopened, unmoved, un-surrendered — "
            "and no longer gripped. The whole word in eight "
            "knuckles. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r041-b39", "out": "s39-not-that-everything-is-taken.jpeg", "seg": "n10",
        "window": "220.16-222.99", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Not that everything is taken from you.",
        "must_show": "the goods still there — the same table now wide: coffer, tools, bread, cloak all present and untouched in the warm light; nothing confiscated.",
        "must_not_show": "no halo, glare or rim-light; abundance intact — the release changed the owner, not the inventory.",
        "scene": (
            "The same table seen wider in the warm evening "
            "light: the small coffer sits exactly where it sat, "
            "and around it the household's goods stand whole "
            "and untouched — a workman's tools in their roll, a "
            "round loaf under its cloth, a folded winter cloak, "
            "a clay lamp burning — everything still here, "
            "everything still his, and all of it lighter by "
            "exactly one grip. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r041-b40", "out": "s40-and-it-worked-the-way.jpeg", "seg": "n11",
        "window": "226.16-229.83", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD", "CROWD"],
        "narration": "And it worked, the way he meant it to. The crowd got smaller.",
        "must_show": "the thinning — the road at dusk visibly emptier: gaps in the column, families peeling off at a junction toward home; sober, unshamed leaving.",
        "must_not_show": "no halo, glare or rim-light; NO shame in the leavers — thoughtful faces, honest departures; the thinning is the sermon working.",
        "scene": (
            "At a dusk junction the crowd is visibly fewer, "
            "the camera at the fork behind the leaving family "
            "so the parting reads both ways: "
            "real gaps have opened in the column, and down the "
            "homeward lane a family walks away together in the "
            "amber light — the father carrying his sleeping "
            "daughter, his face thoughtful rather than ashamed "
            "— while two young men stand at the fork still "
            "deciding, and the smaller road-column moves on "
            "south without them. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b41", "out": "s41-people-who-had-walked-with.jpeg", "seg": "n11",
        "window": "229.83-236.66", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD", "CROWD"],
        "narration": (
            "People who had walked with him all morning went home. He watched "
            "them go, and he did not lower the price."
        ),
        "must_show": "SCRIPTURE-EXACT in spirit: the watching — a medium single from the side: Jesus in profile watching the leavers grow small down the homeward lane, grief and respect together in his stillness; no calling after them.",
        "must_not_show": "no halo, glare or rim-light on Jesus; he does NOT call out, does not gesture — the unlowered price is his silence.",
        "scene": (
            "A medium single from the side on the darkening "
            "road: Jesus in profile, still, hands at his "
            "sides, watching the leaving family grow small "
            "between the field walls in the last amber light — "
            "grief and respect held together in his face, and "
            "his mouth closed on every easy word that would "
            "have brought them back — the small blur of the "
            "waiting column soft at the frame's edge, and the "
            "price staying what it is. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b42", "out": "s42-salt-is-good-but-if.jpeg", "seg": "j8",
        "window": "237.19-243.45", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Salt is good: but if the salt have lost his savour, wherewith "
            "shall it be seasoned?"
        ),
        "must_show": "SCRIPTURE-EXACT: good salt first — a close still of coarse grey-white salt crystals heaped in a wooden bowl beside cured fish and dough; salt at work, worth its name.",
        "must_not_show": "no halo, glare or rim-light; the good version before the ruined one — usefulness visible in its company.",
        "scene": (
            "A close still shot on a kitchen board in flat grey "
            "light: a wooden bowl heaped with coarse grey-white "
            "salt crystals, glinting faintly wet — and around "
            "it its work in progress: two split fish laid in "
            "their salt bed, a round of dough with its pinch "
            "already kneaded in, a housewife's scoop resting in "
            "the bowl — salt in the middle of everything it "
            "keeps and seasons. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r041-b43", "out": "s43-he-is-not-asking-you.jpeg", "seg": "n3",
        "window": "60.67-63.21", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY"],
        "narration": "He is not asking you to hate anyone.",
        "must_show": "the reassurance — the family embracing at their door in warm light; the loves are safe; only the order changes.",
        "must_not_show": "no halo, glare or rim-light; full warmth — the teaching never costs the family its embrace.",
        "scene": (
            "At the family's low doorway in warm evening light "
            "the embrace is general: the grey father's arms "
            "around the half-grown boy, the mother pressing "
            "the young wife's head to her shoulder, the baby "
            "passed laughing between hands — every love in the "
            "sentence alive and kept, held exactly as close as "
            "before, in a house that has only ever been asked "
            "about the order of its loves and not their "
            "existence. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r041-b44", "out": "s44-it-is-neither-fit-for.jpeg", "seg": "j8",
        "window": "243.45-250.55", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "It is neither fit for the land, nor yet for the dunghill; but men "
            "cast it out."
        ),
        "must_show": "SCRIPTURE-EXACT: the casting out — a woman tossing a bowlful of spent grey powder out a doorway onto the path where feet have already trodden earlier scatterings flat.",
        "must_not_show": "no halo, glare or rim-light; the powder visually salt-like and utterly inert — landing where only footsteps use it.",
        "scene": (
            "At a kitchen doorway a housewife tosses a bowl of "
            "spent grey powder out onto the packed path with "
            "the flat unceremony of emptying ash — the cloud of "
            "it drifting down onto earlier scatterings already "
            "trodden flat and pale into the dirt where every "
            "foot to the well walks over them — stuff that "
            "looks like salt, thrown where looking like things "
            "is all that is left to it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b45", "out": "s45-he-that-hath-ears-to.jpeg", "seg": "j8 + n12",
        "window": "250.55-259.40", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "He that hath ears to hear, let him hear. Salt from the Dead Sea "
            "marshes was never pure."
        ),
        "must_show": "the source shown — the white crusted salt marshes of the Dead Sea shore, harvesters cutting grey-white cakes from the crust under a hazy sky.",
        "must_not_show": "no halo, glare or rim-light; mineral geography — the impurity built in from the shore itself.",
        "scene": (
            "On the blinding-pale shore of the Dead Sea under a "
            "hazy white sky, two harvesters cut slabs of "
            "grey-white salt crust from the marsh flats with "
            "wooden spades, stacking the rough cakes on a "
            "waiting donkey — the water lying heavy and "
            "metallic beyond them, the crust marbled visibly "
            "with grit and earth even as it comes up — salt "
            "born mixed, from the lowest shore on earth. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b46", "out": "s46-leave-it-in-the-damp.jpeg", "seg": "n12",
        "window": "259.40-268.10", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Leave it in the damp and the salt leaches away, and what is left "
            "is a powder that still looks like salt and does nothing at all."
        ),
        "must_show": "the leaching — a close still: a salt cake gone dull in a damp storeroom corner, its base dissolved into a tide-ring on the stone, the remainder pale and dead.",
        "must_not_show": "no halo, glare or rim-light; the LOOK preserved and the power gone — that treacherous resemblance is the whole frame.",
        "scene": (
            "A close still in a dim storeroom: on the damp "
            "stone floor by a sweating wall, an old salt cake "
            "sits dull and crumbling, its base dissolved away "
            "into a dried tide-ring of mineral stain around it "
            "— and the cake itself still perfectly salt-shaped, "
            "salt-coloured, salt-looking, and by now, to the "
            "tongue and the dough and the fish, nothing "
            "whatsoever. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r041-b47", "out": "s47-that-is-the-warning.jpeg", "seg": "n12",
        "window": "268.10-269.83", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "That is the warning.",
        "must_show": "the warning compact — the two bowls side by side in one light: working salt with its cured fish, and the dead lookalike powder; tell them apart if you can.",
        "must_not_show": "no halo, glare or rim-light; visually NEAR-identical bowls — only the company they keep betrays them.",
        "scene": (
            "On one board in flat even light two wooden bowls "
            "sit side by side, filled with what looks like the "
            "same grey-white crystal — but beside the first lie "
            "firm cured fish and risen dough, and beside the "
            "second lies a split fish gone soft and a flat "
            "unrisen round — twin bowls, told apart not by "
            "their contents but by everything around them. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r041-b48", "out": "s48-not-a-bad-man-a.jpeg", "seg": "n12",
        "window": "269.83-275.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": "Not a bad man. A man who looks the part with nothing in him.",
        "must_show": "the human version — a respectable, pleasant, entirely hollow-eyed man in the thinned crowd walking the road by rote; the lookalike, walking.",
        "must_not_show": "no halo, glare or rim-light; nothing villainous — pleasant emptiness; the horror is only in the eyes not being home.",
        "scene": (
            "In the thinned dusk column one man walks perfectly "
            "in step: robe decent, beard trimmed, staff swinging "
            "at the regulation angle, a pleasant half-smile "
            "fixed and seamless — and his eyes, caught close, "
            "are simply not home: focused nowhere, lit by "
            "nothing, a well-kept house with no lamp in it, "
            "keeping pace with a road he stopped walking some "
            "years ago. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r041-b49", "out": "s49-so-here-is-the-question.jpeg", "seg": "n13a",
        "window": "275.70-282.94", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "CROWD"],
        "narration": (
            "So here is the question. Why would a man who came to save the "
            "world take the biggest crowd he ever had, and try to thin it out?"
        ),
        "must_show": "the question posed over the evidence — the dusk road with its visible gaps, Jesus walking on at the head of the smaller, quieter column.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the thinned column itself is the riddle on screen.",
        "scene": (
            "In the deep amber of the day's end, the camera "
            "looking along the road from behind the column's "
            "last walkers, the column "
            "moves on visibly smaller — gaps of bare road "
            "showing where hundreds walked at noon, the "
            "remaining walkers spread thin and quiet between "
            "the darkening field walls — and at their head the "
            "cream-clad figure walks steadily on south, "
            "unhurried, leading fewer people than he had this "
            "morning and plainly at peace with the trade. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r041-b50", "out": "s50-because-he-will-not-let.jpeg", "seg": "n13b",
        "window": "283.48-286.45", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Because he will not let you sign before you have read it.",
        "must_show": "the contract honest — a close still: a covenant scroll held OPEN under a lamp, every line exposed, the reed pen laid aside unused until the reading is done.",
        "must_not_show": "no halo, glare or rim-light; dense ancient script, no modern legibility; the pen WAITING is the ethic.",
        "scene": (
            "A close still under warm lamplight: a covenant "
            "scroll held fully open by two smooth stone "
            "weights, its dense columns exposed line to line "
            "from head to foot — and the reed pen lying "
            "deliberately aside on the table's edge, dry, "
            "untouched, waiting behind the reading like a "
            "door behind a long hallway — terms first, names "
            "after, always in that order at this table. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b51", "out": "s51-think-what-else-in-your.jpeg", "seg": "n13b",
        "window": "286.45-291.59", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Think what else in your life ever did that. The loan showed you "
            "the payment afterward. The habit showed you the cost years "
            "afterward."
        ),
        "must_show": "the afterward-price — a debtor's table: a man discovering the true figures at the BOTTOM of a bill he signed long ago, lamplight, head in hand.",
        "must_not_show": "no halo, glare or rim-light; recognizable regret — costs that introduced themselves late.",
        "scene": (
            "At a night table a man sits with his head propped "
            "in one hand over an old unrolled bill, his lamp "
            "burned low — his finger resting far down the "
            "parchment where the accumulated figures have "
            "finally shown themselves, years after the easy "
            "signing visible in the faded flourish at the top "
            "— the universal posture of a man meeting the "
            "price after the purchase. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b52", "out": "s52-the-habit-showed-you-the.jpeg", "seg": "n13b",
        "window": "291.59-298.34", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD", "CROWD"],
        "narration": (
            "He told a crowd the whole price first, and let them choose."
        ),
        "must_show": "the contrast crowned — past the shoulders of two remaining walkers: Jesus turned to them with both hands open at his sides, palms forward; the whole price told, the choice theirs.",
        "must_not_show": "no halo, glare or rim-light on Jesus; open hands, open road, open choice — no pressure in the frame.",
        "scene": (
            "Past the shoulders of two remaining walkers on "
            "the dusk road: Jesus has turned to the smaller "
            "column with both hands open at his sides, palms "
            "forward — nothing hidden in them and nothing held "
            "out as bait — the two listeners at the frame's "
            "near edges standing in the amber light as free "
            "people, each holding the whole known price, the "
            "road south lying open behind him and the roads "
            "home lying open behind them. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b53", "out": "s53-he-is-not-trying-to.jpeg", "seg": "n14",
        "window": "298.85-303.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": (
            "He is not trying to keep you out. He is trying to keep you from a "
            "half-built life."
        ),
        "must_show": "the two outcomes final — the finished watchtower warm-lit at dusk with its watchman, and far below in the corner of the frame the weedy abandoned courses in shadow; the choice as architecture.",
        "must_not_show": "no halo, glare or rim-light; the finished tower gets the light — the frame roots FOR the builder.",
        "scene": (
            "In the last warm light the finished watchtower "
            "stands on its slope with dusk gold on its stones "
            "and the watchman's small lamp just kindled at the "
            "platform rail — while far below at the frame's "
            "shadowed corner the abandoned three courses sit "
            "cold among their weeds — two endings of the same "
            "ambition sharing one hillside, and all the light "
            "in the picture standing with the one that was "
            "counted first. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r041-b54", "out": "s54-he-tells-you-what-it.jpeg", "seg": "n14 + n15",
        "window": "303.27-308.43", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": (
            "He tells you what it costs because he wants the tower standing. "
            "And one more thing."
        ),
        "must_show": "the hinge to the teller — close on Jesus's face on the dusk road, the day's hard honesty in it, and something further arriving behind his eyes.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the 'one more thing' gathering in the face — the row's deepest turn coming.",
        "scene": (
            "Close on Jesus's face in the deep dusk of the "
            "road: the long day's honesty still set in the "
            "lines of it, dust on the cheekbone, the light "
            "nearly gone — and behind the warm brown eyes "
            "something further is arriving, a weight the "
            "sermon has been walking toward all afternoon, "
            "turning his gaze briefly south along the darkening "
            "road before the words come. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b55", "out": "s55-the-man-asking-that-crowd.jpeg", "seg": "n15",
        "window": "308.43-316.58", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": (
            "The man asking that crowd to count what it would cost them had "
            "already counted what it would cost him. He was walking toward "
            "Jerusalem while he said it."
        ),
        "must_show": "SCRIPTURE-EXACT in trajectory: the destination revealed — Jesus walking on ahead of the column at dusk, and far on the southern horizon the faint high shape of Jerusalem's ridge against the last light.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the city faint and far — a direction, not a backdrop; his stride even and unhesitating.",
        "scene": (
            "In the deep blue dusk, the camera off the road's "
            "side taking his walk in profile, Jesus moves a few "
            "paces ahead of the quiet column, his stride even, "
            "his face set south — and far off on the horizon, "
            "faint against the last green-gold band of sky, "
            "the high ridge of Jerusalem stands with its walls "
            "just discernible, the road running thin and pale "
            "all the way to it — a man teaching arithmetic "
            "while walking, steadily, toward his own summed "
            "and accepted total. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b56", "out": "s56-he-knew-the-number-he.jpeg", "seg": "n15",
        "window": "316.58-319.54", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": "He knew the number. He did not turn back.",
        "must_show": "resolution embodied — from behind: Jesus's cream-clad figure walking on into the dusk toward the far city, alone at the column's head, no pause in the stride.",
        "must_not_show": "no halo, glare or rim-light; from behind is right here — the unbroken stride into the dark is the whole beat.",
        "scene": (
            "From behind at road level: the cream-clad figure "
            "walks away down the darkening road at an even, "
            "unbroken pace, sandals lifting small puffs of "
            "day's-end dust, the field walls funnelling the "
            "last light along his path toward the faint far "
            "ridge — a back that does not turn, on a road "
            "whose end he has already counted to the last "
            "coin. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r041-b57", "out": "s57-so-he-is-not-waiting.jpeg", "seg": "n16",
        "window": "320.12-328.40", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": (
            "So he is not waiting at the end of that road with a bill. He is "
            "standing at the start of it, telling you the truth, watching to "
            "see if you want to come."
        ),
        "must_show": "the invitation's geometry — Jesus turned back at the road's beginning in the last light, facing toward the road's start, the long honest road stretching behind him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; his gaze rests just PAST the camera's edge, never into the lens — the whole priced road visible over his shoulder.",
        "scene": (
            "At a milestone where the long south road begins, "
            "Jesus has turned fully around in the last of the "
            "light and stands facing back toward the road's "
            "start — behind his "
            "shoulder the whole honest length of the road runs "
            "visible into the dusk, walls and rises and the "
            "far faint city, nothing of it hidden — and his "
            "eyes rest level a breath past the camera's edge, "
            "on whoever stands at the start of the road, with "
            "the patient watching openness of a man who has "
            "told the whole truth and now simply waits. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r041-b58", "out": "s58-he-would-rather-you-came.jpeg", "seg": "n16",
        "window": "328.40-332.90", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": (
            "He would rather you came slowly than said yes in a hurry and quit."
        ),
        "must_show": "the closing image — close on Jesus's extended open hand in the dusk, unhurried, held out toward the road's start with all the time in the world in it.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hand is PATIENT — half-extended, no urgency, an offer built for slow answers; his eyes on the hand's destination, never into the lens.",
        "scene": (
            "A close final frame in the deep dusk: Jesus's "
            "work-worn hand extended past the camera's edge "
            "toward the start of the road, open "
            "and easy, not reaching, not insisting — held out "
            "at the unhurried half-distance of an offer that "
            "will still be there tomorrow, and next year, and "
            "the year after that — the last light of the day "
            "resting quiet along the open palm. Every figure "
            "has two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "ROAD": "PLACE-REF/road.jpeg",  # build-38-persistent-widow v2-r038-b39
    "VINEYARD": "PLACE-REF/vineyard.jpeg",  # build-23-vineyard v2-r023-b03
}
# === end PLACE-PLATES ===
