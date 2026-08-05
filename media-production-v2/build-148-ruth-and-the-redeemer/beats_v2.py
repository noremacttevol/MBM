#!/usr/bin/env python3
"""V2 beat map — row 148, build-148-ruth-and-the-redeemer (Ruth 1-4).

COVERAGE: 29 pictures over 164.4 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Ruth KJV):
  1:3-5 Naomi widowed in MOAB, both sons buried there.
  1:14  "Orpah kissed her mother in law; but Ruth CLAVE unto her."
  1:16-17 "INTREAT ME NOT TO LEAVE THEE... whither thou goest, I
        will go... thy people shall be my people, and thy God my
        God: Where thou diest, will I die."
  1:20-21 "Call me not Naomi, call me MARA... I went out FULL, and
        the LORD hath brought me home again EMPTY."
  2:3   Ruth GLEANED "after the reapers" — the field of BOAZ.
  2:12  Boaz: "a full reward be given thee... under whose WINGS
        thou art come to trust."
  3:9   the threshing floor: "spread therefore thy SKIRT over thine
        handmaid; for thou art a NEAR KINSMAN."
  3:11  "all the city... doth know that thou art a VIRTUOUS woman."
  4:1-13 the GATE: Boaz redeems before witnesses and marries Ruth.
  4:16-17 the son laid in Naomi's LAP — Obed, grandfather of DAVID.

RENDERING LAWS:
  - THE THRESHING FLOOR (b25) IS RENDERED WITH EXACT MODESTY: Ruth
    kneeling at the FEET of the waking Boaz beside the grain pile,
    his cloak being spread over her SHOULDERS — a legal-betrothal
    sign, dignified, lamplit, nothing suggestive in framing or
    pose, ever. Automatic reject otherwise.
  - The Moab deaths (b01) are aftermath only: three stone grave
    markers on a foreign hillside, Naomi small beside them — no
    burial scenes, no bodies.
  - RUTH's clinging (b03) is the story's engine — fierce, physical,
    dignified; Orpah's leaving (b05) is tender, not villainous.
  - NAOMI's bitterness (b12-b18) is honest grief with dignity —
    never shrewish; the empty→filled arc lands at b28 (the child
    in her LAP — the same lap the emptiness was spoken over).
  - Boaz is protective WARMTH without possession — an honourable
    older man; the wings-image (b19/b21) may echo in a cloak's
    shelter, never literal wings.
  - b29's Davidic line: the sleeping child + a shepherd's staff and
    a far Bethlehem hill — the greater Redeemer suggested by the
    town itself, nothing more.

TIME OF DAY ARC (intentional): Moab and the road in grey overcast
(grief weather); the Naomi-return scenes in flat dusty light; the
HARVEST fields in bright gold day; the threshing floor at LAMPLIT
NIGHT by design; the gate scene in clear morning; the child and
close in full warm gold.

CHANGING CONDITIONS (kept OUT of the locks): Naomi — bowed and
bitter, then holding the child; Ruth — road-worn widow, then
gleaner, then bride; the season — harvest ripening through the row.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row).
LOCKS = {
    "NAOMI": (
        "NAOMI LOCK: Naomi is the same woman in every shot — about "
        "sixty, small and worn, deep grief-lines, grey hair under a "
        "DARK CHARCOAL widow's shawl, a patched DARK GREY-BROWN "
        "dress (never cream, never white); bowed early, straightened "
        "late; dignity always, never shrewish."
    ),
    "RUTH": (
        "RUTH LOCK: Ruth is the same woman in every shot — about "
        "twenty-five, a strong young Moabite widow: dark expressive "
        "eyes, black hair braided under a DEEP TERRACOTTA head-"
        "scarf, a simple DARK OLIVE dress with a woven sash (never "
        "cream, never white); loyal, fierce, warm; work-capable "
        "hands."
    ),
    "BOAZ": (
        "BOAZ LOCK: Boaz is the same man in every shot — about "
        "fifty-five, a broad honourable landowner: silver-streaked "
        "dark beard, sun-lined kind eyes, in a DEEP WINE-BROWN "
        "mantle over a dark tunic (never cream, never white); "
        "protective warmth without possession."
    ),
    "FIELD": (
        "FIELD LOCK: the barley field — golden standing barley in "
        "harvest, reapers' swathes, sheaves standing bound, a low "
        "stone boundary and an olive at the corner, Bethlehem's "
        "hill beyond. The same field throughout."
    ),
    "GATE": (
        "GATE LOCK: the Bethlehem town gate — a stone gateway with "
        "worn benches where the elders sit, morning light through "
        "the arch. The same gate throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r148-b01", "out": "s01-a-widow-named-naomi-lost.jpeg", "seg": "n0",
        "window": "0.40-5.93", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI"],
        "narration": (
            "A widow named Naomi lost everything in a foreign land — her "
            "husband and both sons buried there."
        ),
        "must_show": "the losses as aftermath — THREE stone grave markers on a grey Moabite hillside, Naomi small and bowed beside them in her widow's shawl; everything, buried foreign.",
        "must_not_show": "ABSOLUTE: no burials, no bodies — three markers and one bowed widow; grey overcast.",
        "scene": (
            "Everything she had fits under three stones now: "
            "on the grey Moabite hillside the three rough "
            "grave markers stand in a short row — a husband's "
            "and two sons' — and beside them Naomi, small and "
            "bowed in her charcoal shawl, one hand resting on "
            "the middle stone the way you rest a hand on a "
            "shoulder — a foreign sky over a foreign field "
            "holding all three of her reasons for living, "
            "and the road home running empty behind her. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r148-b02", "out": "s02-she-told-her-two-to.jpeg", "seg": "n1",
        "window": "7.46-10.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI", "RUTH"],
        "narration": "She told her two daughters-in-law to go home to their own people.",
        "must_show": "the releasing — on the grey road, Naomi's hands gently pushing the two young widows back toward Moab; love doing the sensible unselfish thing.",
        "must_not_show": "no halo; the push GENTLE — a blessing, not a rejection; three women, grief-worn.",
        "scene": (
            "Her last act of mothering is to send them away: "
            "on the grey road out of Moab Naomi turns to her "
            "two young daughters-in-law and pushes them "
            "gently back the way they came — worn hands on "
            "young shoulders, aiming them home toward their "
            "own mothers, their own people, their own "
            "second chances — nothing left in her purse to "
            "offer them except the exit — love, doing the "
            "sensible unselfish arithmetic with its own "
            "loneliness. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r148-b03", "out": "s03-but-ruth-clung-to-her.jpeg", "seg": "n1",
        "window": "11.95-14.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI", "RUTH"],
        "narration": "But Ruth clung to her, and would not go.",
        "must_show": "SCRIPTURE-EXACT: the clinging — Ruth's arms wrapped fierce around Naomi, her face pressed to the old shoulder, feet planted; the refusal physical.",
        "must_not_show": "no halo; the cling FIERCE and dignified — a decision, not desperation.",
        "scene": (
            "One daughter-in-law does not do the sensible "
            "thing: Ruth's arms wrap around Naomi and lock — "
            "her young face pressed into the charcoal shawl "
            "at the old woman's shoulder, her feet planted "
            "in the road dust like fence posts — the whole "
            "strong body one refusal — clung, the scripture "
            "says, and this is what the word looks like: "
            "loyalty with its arms full, holding on to a "
            "future of nothing because the nothing has "
            "Naomi in it. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r148-b04", "out": "s04-intreat-me-not-to-leave.jpeg", "seg": "w1a",
        "window": "16.43-28.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI", "RUTH"],
        "narration": (
            "Intreat me not to leave thee, or to return from following "
            "after thee: for whither thou goest, I will go; and where thou "
            "lodgest, I will lodge: thy people shall be my people, and thy "
            "God my God."
        ),
        "must_show": "SCRIPTURE-EXACT: the vow — Ruth holding Naomi's two hands on the grey road, speaking the great pledge into her face; covenant-love at eye level.",
        "must_not_show": "no halo; the vow EYE TO EYE — Ruth steady, Naomi undone.",
        "scene": (
            "The greatest loyalty speech in scripture is "
            "delivered on a dirt road between two widows: "
            "Ruth takes Naomi's worn hands in both of hers "
            "and says it straight into the grief-lined "
            "face — where thou goest, I go; where thou "
            "lodgest, I lodge; thy people, MY people; thy "
            "God, MY God — each clause laid down like a "
            "course of stone, a Moabite girl building a "
            "covenant on the open road while the old woman "
            "she is choosing stands undone inside her "
            "hands. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r148-b05", "out": "s05-one-kissed-her-and-left.jpeg", "seg": "n1",
        "window": "10.28-11.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI"],
        "narration": "One kissed her and left.",
        "must_show": "Orpah's tender leaving — the other young widow's farewell kiss on Naomi's cheek, already turning back toward Moab; grief and sense, no villainy.",
        "must_not_show": "no halo; Orpah SYMPATHETIC — tears at the turning; the road dividing behind her.",
        "scene": (
            "The other goodbye is tender and it is still a "
            "goodbye: Orpah's kiss lands wet on Naomi's "
            "cheek, her hands lingering one last squeeze on "
            "the old arms — and then the turning, the road "
            "back toward Moab taking her a step at a time, "
            "her shawl pulled up against her own tears — "
            "nothing wrong in it, nothing cold: the "
            "reasonable choice, made with love, walking "
            "away down the reasonable road — which is what "
            "makes the one who stayed astonishing. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r148-b06", "out": "s06-ask-me-to-leave-you.jpeg", "seg": "n2",
        "window": "42.12-44.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI", "RUTH"],
        "narration": "Don't ask me to leave you, Ruth said.",
        "must_show": "the plea's heart — close on Ruth's face over Naomi's hands: don't ask; the young eyes unmovable and warm.",
        "must_not_show": "no halo; unmovable WARMTH — no anger in the refusal.",
        "scene": (
            "The refusal is made of warmth all the way "
            "through: close on Ruth's young face bent over "
            "the old hands she is holding — don't ask me; "
            "don't even ask — the dark expressive eyes "
            "steady on Naomi's with nothing hard in them "
            "anywhere: just a loyalty that has already "
            "finished deciding, asking gently to be spared "
            "the ceremony of being talked out of what no "
            "talking will reach. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r148-b07", "out": "s07-where-thou-diest-will-i.jpeg", "seg": "w1b",
        "window": "30.65-40.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI", "RUTH"],
        "narration": (
            "Where thou diest, will I die, and there will I be buried: the "
            "LORD do so to me, and more also, if ought but death part thee "
            "and me."
        ),
        "must_show": "SCRIPTURE-EXACT: the vow's far end — Ruth's hand rising in oath toward the grey sky, the other still holding Naomi's; loyalty sworn past death.",
        "must_not_show": "no halo; the oath-hand SOLEMN; both women's faces wet now.",
        "scene": (
            "The vow runs all the way to the grave and "
            "signs there: Ruth's free hand rises toward the "
            "grey Moabite sky in the old oath gesture — the "
            "LORD do so to me, and MORE — while her other "
            "hand keeps its grip on Naomi's — where you "
            "die, I die; where they lay you, they will lay "
            "me — a girl of Moab swearing herself into a "
            "family's dust by the name of a God she has "
            "just made hers, until both faces on the road "
            "are wet. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r148-b08", "out": "s08-wherever-you-go-going.jpeg", "seg": "n2",
        "window": "44.06-46.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI", "RUTH"],
        "narration": "Wherever you go, I'm going.",
        "must_show": "the going — the two women walking the road TOGETHER now, Ruth matching Naomi's slower steps, bundles shared; the vow already in motion.",
        "must_not_show": "no halo; DIRECTION — together toward Bethlehem, away from Moab; the pace matched to the older woman.",
        "scene": (
            "The vow starts keeping itself immediately: the "
            "two widows walk the long road together now — "
            "Ruth's young stride reined to Naomi's worn "
            "one, the heavier bundle riding the younger "
            "shoulder, the two shawled heads level in the "
            "grey light — wherever you go: currently, a "
            "dusty road west, at an old woman's pace, "
            "toward a town that owes neither of them "
            "anything — and the going, step for step, "
            "already keeping the promise. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r148-b09", "out": "s09-wherever-you-stay-staying.jpeg", "seg": "n2",
        "window": "46.14-48.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI", "RUTH"],
        "narration": "Wherever you stay, I'm staying.",
        "must_show": "the staying — a night camp on the road: one small fire, Ruth settling her cloak over sleeping Naomi before lying down beside her; lodging shared.",
        "must_not_show": "no halo; the care QUIET — the cloak-settling gesture the frame.",
        "scene": (
            "Where thou lodgest tonight is a road verge "
            "with one small fire: Naomi sleeps curled under "
            "the wall's lee, and Ruth — before she takes "
            "her own place on the cold side — settles her "
            "spare cloak over the old woman's shoulders, "
            "tucking the edge with a daughter's hands — "
            "then lies down between Naomi and the open "
            "dark — wherever you stay, I stay: tonight "
            "that means here, on stones, nearest the "
            "night. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r148-b10", "out": "s10-only-death-gets-to-separate.jpeg", "seg": "n2",
        "window": "52.84-58.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI", "RUTH"],
        "narration": (
            "Only death gets to separate us — and even that, may God deal "
            "with me if it does."
        ),
        "must_show": "the vow sealed — the two women's clasped hands close, old fingers and young interlocked; the bond as one image.",
        "must_not_show": "no halo; the clasp the WHOLE frame — two generations, one grip.",
        "scene": (
            "The whole covenant fits in one interlocked "
            "grip: close on the two hands — Naomi's old "
            "fingers, knuckled and thin, laced through "
            "Ruth's young strong ones, neither letting the "
            "other go — the clasp that walked out of Moab "
            "and will walk into Bethlehem, that gleans and "
            "is fed, that empties and is filled — only "
            "death licensed to open it, and even death put "
            "on notice — loyalty, printed in fingers. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r148-b11", "out": "s11-your-people-are-my-people.jpeg", "seg": "n2",
        "window": "48.44-52.84", "wide": False, "jesus": False, "ref": False,
        "locks": ["RUTH"],
        "narration": "Your people are my people now, and your God is my God.",
        "must_show": "the adoption — Ruth at the ridge's crest looking DOWN toward distant Bethlehem on its hill, her face taking in her new people's country; the belonging chosen.",
        "must_not_show": "no halo; Bethlehem FAR and small — a stranger's first sight of home.",
        "scene": (
            "Her new country shows itself from the last "
            "ridge: Ruth stands at the crest with the wind "
            "off the barley lands in her scarf, looking "
            "down the long slope to where Bethlehem sits "
            "small and pale on its hill — her people now, "
            "every stranger in it; her God now, in its "
            "little houses' prayers — a Moabite widow "
            "surveying the inheritance she swore herself "
            "into: a town that has never heard of her, "
            "about to become the address of her whole "
            "story. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r148-b12", "out": "s12-call-me-not-naomi-call.jpeg", "seg": "w2a",
        "window": "59.93-65.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI"],
        "narration": (
            "Call me not Naomi, call me Mara: for the Almighty hath dealt "
            "very bitterly with me."
        ),
        "must_show": "SCRIPTURE-EXACT: the renaming — Naomi in the Bethlehem lane amid welcoming neighbour women, refusing her own name; grief spoken with dignity into kind faces.",
        "must_not_show": "no halo; the neighbours KIND and shocked; Naomi's bitterness dignified, never shrewish.",
        "scene": (
            "The town welcomes a name she no longer answers "
            "to: in the Bethlehem lane the neighbour women "
            "crowd warm around the returned widow — Naomi! "
            "is it Naomi? — and she stops them with one "
            "worn hand: call me not Naomi — call me MARA — "
            "bitter — the renaming delivered level and "
            "quiet into their kind shocked faces, a woman "
            "correcting the town's records to match her "
            "ledger: pleasant went out; bitter came home. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r148-b13", "out": "s13-i-went-out-full-and.jpeg", "seg": "w2b",
        "window": "67.22-70.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI"],
        "narration": "I went out full, and the LORD hath brought me home again empty.",
        "must_show": "SCRIPTURE-EXACT: the emptiness stated — Naomi's two open EMPTY hands held out before the neighbour women; the whole loss in two palms.",
        "must_not_show": "no halo; the empty hands the frame's centre — nothing else needed.",
        "scene": (
            "Her testimony is two open hands with nothing "
            "in them: Naomi holds them out before the "
            "lane's gathered women — palms up, empty, "
            "steady — I went out FULL — a husband on this "
            "arm, sons at this side — and the LORD hath "
            "brought me home again EMPTY — the arithmetic "
            "of her decade held out in the oldest visual "
            "aid there is, and not one woman in the lane "
            "able to look away from the nothing she is "
            "showing them. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r148-b14", "out": "s14-naomi-means-pleasant.jpeg", "seg": "n2b",
        "window": "72.87-74.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI"],
        "narration": "Naomi means pleasant.",
        "must_show": "the name's meaning — close on Naomi's grief-lined face, the pleasantness the name promised still faintly legible under the years; the word and the face together.",
        "must_not_show": "no halo; the trace of the old warmth VISIBLE — the name was once true.",
        "scene": (
            "The name was a prophecy her life stopped "
            "keeping: close on the grief-lined face under "
            "the charcoal shawl — and faintly, under the "
            "cut of the years, the pleasantness the name "
            "promised is still legible: the laugh-lines "
            "older than the grief-lines, the warmth the "
            "neighbour women remembered at the gate — "
            "Naomi, pleasant, a word her parents chose in "
            "hope, worn now like an inscription weathering "
            "on stone. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r148-b15", "out": "s15-i-went-out-with-a.jpeg", "seg": "n2b",
        "window": "79.26-84.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI", "RUTH"],
        "narration": (
            "I went out with a husband and two sons, and I've come back "
            "with nothing."
        ),
        "must_show": "the accounting — Naomi bowed in the lane; and BEHIND her, quietly holding their bundles, Ruth — the 'nothing' visibly not quite true; the frame's gentle irony.",
        "must_not_show": "no halo; Ruth PRESENT and unnoticed — the audit missing its own asset.",
        "scene": (
            "Her accounting is honest and it is wrong by "
            "one: Naomi bows under the lane's kind eyes — "
            "a husband out, two sons out, NOTHING home — "
            "and two steps behind her, holding both their "
            "bundles and saying not a word, stands the "
            "nothing: Ruth, sworn to her past death, "
            "already scanning the town for work to feed "
            "her — the empty ledger's uncounted entry, "
            "waiting patient in a terracotta scarf for "
            "the story to audit itself. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r148-b16", "out": "s16-hold-on-to-that-word.jpeg", "seg": "n2b",
        "window": "84.06-86.28", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Hold on to that word, empty.",
        "must_show": "the word held — an empty grain basket alone by the door in flat light; emptiness as an object the story will fill.",
        "must_not_show": "no halo; ONE empty basket — the story's tracking-object introduced.",
        "scene": (
            "Keep your eye on the word, says the storyteller, "
            "and hands you a basket: it stands empty by the "
            "doorway in the flat dusty light — a woven grain "
            "basket with nothing in it at all, ribs showing, "
            "light pooling in its bare bottom — EMPTY, the "
            "word made wicker, set down where the "
            "storyteller can find it again — because this "
            "particular emptiness is about to be argued "
            "with by an entire harvest. No people are "
            "needed in this frame."
        ),
    },
    {
        "id": "v2-r148-b17", "out": "s17-ruth-gleaned-grain-in-the.jpeg", "seg": "n3",
        "window": "90.08-96.77", "wide": True, "jesus": False, "ref": False,
        "locks": ["RUTH", "FIELD"],
        "narration": (
            "Ruth gleaned grain in the fields behind the harvesters to keep "
            "Naomi fed — and the field belonged to a man named Boaz."
        ),
        "must_show": "the gleaning — the golden barley field at harvest: reapers ahead, Ruth stooped BEHIND them gathering dropped stalks into her arm; honest hard work in bright gold.",
        "must_not_show": "no halo; DIRECTION — she works behind the reapers per the law; her labour dignified.",
        "scene": (
            "Her love has become stoop-labour in a stranger's "
            "field, the camera low in the stubble taking the "
            "harvest line from the side: the reapers swing "
            "ahead through the standing gold, and behind "
            "them, bent double in the cut rows, Ruth gleans — "
            "hand, stalk, arm; hand, stalk, arm — gathering "
            "the law's leavings one dropped head at a time "
            "to keep an old woman fed — while up the field, "
            "not yet noticing her, rides the shadow of the "
            "man whose name is on the boundary stone. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r148-b18", "out": "s18-call-me-that-anymore-she.jpeg", "seg": "n2b",
        "window": "74.43-79.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI"],
        "narration": (
            "Don't call me that anymore, she said when she got home — call "
            "me bitter."
        ),
        "must_show": "the renaming repeated at the threshold — Naomi at her own worn door, hand on the frame, the words over her shoulder to the following women; home, and renamed.",
        "must_not_show": "no halo; the door WORN (the old family house); her dignity intact in the bitterness.",
        "scene": (
            "She reaches her own door carrying her new "
            "name: Naomi's hand comes to rest on the worn "
            "doorframe of the house she left full — the "
            "wood grey now, the courtyard weedy — and over "
            "her shoulder to the women who followed she "
            "says it once more, quieter: don't call me "
            "that anymore — call me bitter — then steps "
            "over her own threshold into the empty house, "
            "a renamed woman entering rooms that remember "
            "her old name in every corner. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r148-b19", "out": "s19-the-lord-recompense-thy-work.jpeg", "seg": "s1",
        "window": "98.28-106.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["RUTH", "BOAZ", "FIELD"],
        "narration": (
            "The LORD recompense thy work, and a full reward be given thee "
            "of the LORD God of Israel, under whose wings thou art come to "
            "trust."
        ),
        "must_show": "SCRIPTURE-EXACT: the blessing — Boaz standing before straightened Ruth in the gold field, his blessing given with open honour; her surprise at being SEEN.",
        "must_not_show": "no halo; NO literal wings — the shelter-image carried by his mantled gesture at most; honour, not possession.",
        "scene": (
            "The field's owner turns out to know her whole "
            "story: Boaz stands before the straightened "
            "gleaner in the bright gold, silver-streaked "
            "and broad, giving her a blessing with the "
            "formality of a man honouring a soldier — the "
            "LORD recompense thy work; a FULL reward — "
            "under whose wings thou art come to trust — "
            "and on Ruth's dusty astonished face the "
            "discovery that her loyalty, done in stoops "
            "and silence, has been seen the whole time by "
            "the whole town. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r148-b20", "out": "s20-the-story-is-not-finished.jpeg", "seg": "n2b",
        "window": "86.28-88.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": "The story is not finished with it.",
        "must_show": "the turn promised — the empty basket now standing at the FIELD'S edge before the standing gold; emptiness brought to where fullness grows.",
        "must_not_show": "no halo; the SAME basket as b16 — position moved to the harvest's edge.",
        "scene": (
            "The basket has been carried somewhere "
            "interesting: it stands at the field's edge now "
            "— the same bare wicker from the doorway — set "
            "down in the stubble with the standing gold "
            "towering behind it, harvest-heavy heads "
            "leaning over its emptiness like an argument "
            "about to be made — the word EMPTY, hauled out "
            "to the one address in Judah where words like "
            "it go to be contradicted. No people are "
            "needed in this frame."
        ),
    },
    {
        "id": "v2-r148-b21", "out": "s21-may-the-lord-pay-you.jpeg", "seg": "n4",
        "window": "108.13-117.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["RUTH", "BOAZ", "FIELD"],
        "narration": (
            "May the Lord pay you back for what you've done, Boaz told her, "
            "and may He give you a full reward — the God of Israel, the One "
            "you came here to take shelter under."
        ),
        "must_show": "the blessing warmed — Boaz seating Ruth at the harvesters' meal, bread and parched grain passed to her hands; the blessing turning into lunch.",
        "must_not_show": "no halo; the meal COMMUNAL — she seated among the workers, served plainly, honoured.",
        "scene": (
            "The blessing comes with bread attached: at the "
            "harvesters' midday cloth Boaz seats the "
            "Moabite gleaner among his own workers and "
            "passes her the food himself — bread, and "
            "parched grain until she is sufficed — the "
            "May-the-LORD-repay-you already repaying in "
            "advance out of his own field — shelter under "
            "the Almighty's wings served, this noon, as a "
            "place at the cloth and a full portion, with "
            "the reapers making room. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r148-b22", "out": "s22-he-protected-her-fed-her.jpeg", "seg": "n4",
        "window": "117.52-120.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["RUTH", "BOAZ", "FIELD"],
        "narration": "He protected her, fed her, and spoke kindly.",
        "must_show": "the threefold care — Boaz instructing his reapers to drop extra handfuls in Ruth's path, his order visible; provision arranged with dignity-preserving stealth.",
        "must_not_show": "no halo; the handfuls dropped ON PURPOSE readable — the kindness engineered to look like luck.",
        "scene": (
            "His kindness is engineered to spare her pride: "
            "Boaz bends close to two of his reapers with a "
            "quiet instruction, and down the row the "
            "purpose-built accident begins — good handfuls "
            "slipping from the sheaves into the gleaner's "
            "path, barley falling where only she will "
            "follow — protection posted at the field's "
            "corners, kindness in the water jars, and all "
            "of it disguised as ordinary luck so the "
            "proud young widow never has to feel like "
            "charity. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r148-b23", "out": "s23-for-all-the-city-of.jpeg", "seg": "s2",
        "window": "126.11-129.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["RUTH", "BOAZ"],
        "narration": (
            "For all the city of my people doth know that thou art a "
            "virtuous woman."
        ),
        "must_show": "SCRIPTURE-EXACT: the reputation — Boaz speaking the town's verdict to Ruth with grave respect; her worth publicly known and plainly said.",
        "must_not_show": "no halo; his respect GRAVE and formal — the sentence an honour, nothing else.",
        "scene": (
            "The town's verdict is read to her like a "
            "citation: Boaz says it with the gravity of a "
            "man at a gate — ALL the city of my people "
            "doth KNOW — that thou art a VIRTUOUS woman — "
            "the reputation she never sought, assembled "
            "stoop by stoop and kindness by kindness in "
            "the town's watching eyes, handed back to her "
            "now as the one wealth no famine ever "
            "touched — and the Moabite stranger standing "
            "in Bethlehem's full esteem, still holding a "
            "gleaner's bundle. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r148-b24", "out": "s24-the-whole-town-knows-what.jpeg", "seg": "n5",
        "window": "131.96-134.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["RUTH"],
        "narration": "The whole town knows what kind of woman you are, he said.",
        "must_show": "the worth received — close on Ruth's face taking in the town's esteem: the stranger discovering she is known and honoured; quiet moved dignity.",
        "must_not_show": "no halo; her surprise QUIET — esteem landing on humility.",
        "scene": (
            "Being known turns out to be the harvest she "
            "never planted: close on Ruth's face as the "
            "town's verdict lands — the dark eyes widening "
            "and then steadying, the chin coming up a "
            "quiet degree under the terracotta scarf — a "
            "foreigner who asked only to glean, informed "
            "that the whole city has been keeping her "
            "accounts in honour — worth, credited publicly "
            "to a woman who thought she was invisible in "
            "the stubble. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r148-b25", "out": "s25-at-the-threshing-floor-ruth.jpeg", "seg": "n5",
        "window": "134.70-142.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["RUTH", "BOAZ"],
        "narration": (
            "At the threshing floor Ruth had asked him to cover her with "
            "his cloak, the sign of a kinsman's duty — and he promised to "
            "redeem her."
        ),
        "must_show": "SCRIPTURE-EXACT WITH EXACT MODESTY: the lamplit threshing floor — Ruth KNEELING at the feet of the waking Boaz beside the grain pile, his cloak being spread over her SHOULDERS; a legal-betrothal sign, dignified entirely.",
        "must_not_show": "ABSOLUTE: nothing suggestive in pose or framing — she kneels at the FEET, the cloak covers SHOULDERS, both fully robed; lamplit, solemn, legal.",
        "scene": (
            "The boldest legal request in the book is made "
            "kneeling, and answered with a cloak: on the "
            "lamplit threshing floor beside the winnowed "
            "grain pile, Ruth kneels at the feet of the "
            "waking Boaz — robed, solemn, her petition "
            "already spoken: spread thy skirt over thine "
            "handmaid, for thou art a near kinsman — and "
            "his wine-brown cloak comes down over her "
            "SHOULDERS like a signature on a covenant: the "
            "kinsman's duty accepted, redemption promised, "
            "everything in the frame as legal and as "
            "tender as a betrothal at an altar. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r148-b26", "out": "s26-before-the-town-gate-in.jpeg", "seg": "n6a",
        "window": "144.41-148.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOAZ", "GATE"],
        "narration": (
            "Before the town gate, in front of witnesses, Boaz bought the "
            "right to marry Ruth."
        ),
        "must_show": "SCRIPTURE-EXACT: the gate transaction — Boaz before the seated elders at the stone gate in morning light, the sandal-token of redemption changing hands; law made public.",
        "must_not_show": "no halo; the SANDAL-token exact (the period sign); the elders dignified witnesses.",
        "scene": (
            "Redemption is transacted in public, at the "
            "gate, by sandal: Boaz stands before the ten "
            "seated elders in the gateway's morning light, "
            "and across the open space the nearer "
            "kinsman's drawn-off sandal passes into his "
            "hand — the period's signature on a "
            "transferred right, witnessed by every bench — "
            "the right to redeem Elimelech's line, to "
            "raise the fallen name, and to marry Ruth the "
            "Moabitess, purchased openly where the whole "
            "town does its truth. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r148-b27", "out": "s27-he-was-a-near-kinsman.jpeg", "seg": "n4",
        "window": "120.87-124.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOAZ"],
        "narration": "He was a near kinsman — a redeemer by the law.",
        "must_show": "the office named — Boaz's steady face, the weight of the goel's duty settling on it consciously; a man measuring his obligation and accepting it.",
        "must_not_show": "no halo; the acceptance DELIBERATE — duty embraced, not stumbled into.",
        "scene": (
            "The law has a word for what he is to her, and "
            "he knows it: close on Boaz's sun-lined face "
            "as the reckoning settles consciously in — near "
            "kinsman; GOEL; redeemer-by-blood — the old "
            "statute naming him into the widow's story "
            "whether he moves or not — and in the kind "
            "eyes the deliberate acceptance forming: not "
            "duty dodged, not duty endured, but the "
            "obligation picked up whole, the way an "
            "honourable man picks up what is his to "
            "carry. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r148-b28", "out": "s28-emptiness-was-filled-a-son.jpeg", "seg": "n6b",
        "window": "149.83-155.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAOMI", "RUTH"],
        "narration": (
            "Naomi's emptiness was filled; a son was born, and the "
            "neighbour women laid him in her lap."
        ),
        "must_show": "SCRIPTURE-EXACT: the filling — the newborn laid in NAOMI'S lap by the neighbour women, her empty hands full at last; Ruth radiant beside; the arc closed.",
        "must_not_show": "no halo; the LAP exact (the same hands that were empty in b13); joy on every face.",
        "scene": (
            "The hands from the empty testimony get their "
            "rebuttal laid right into them: in the warm "
            "gold of the little house the neighbour women "
            "lower the newborn into NAOMI'S lap — the same "
            "two palms she held out empty in the lane now "
            "curling full around a grandson — Ruth radiant "
            "at her shoulder, the women's blessing loud "
            "around them — went out full, came home empty, "
            "and filled again by a route no accounting "
            "could have drawn: a Moabite's loyalty, a "
            "kinsman's cloak, and God's long arithmetic. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r148-b29", "out": "s29-that-boy-became-the-grandfather.jpeg", "seg": "n7",
        "window": "156.99-163.35", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "That boy became the grandfather of King David — and part of "
            "the line that leads to the greater Redeemer still to come."
        ),
        "must_show": "the line forward — the sleeping child in the warm gold; beside the cradle a shepherd's staff; through the window, Bethlehem's hill in evening light; the future suggested, nothing depicted.",
        "must_not_show": "ABSOLUTE: no depiction of David or the Redeemer — staff, town and light carry the whole lineage.",
        "scene": (
            "The story tips its hand with three quiet "
            "objects: the child Obed asleep in the warm "
            "gold, a shepherd's staff leaned by the cradle "
            "where a visitor left it, and through the small "
            "window the hill of Bethlehem holding the last "
            "evening light — a grandson who will teach a "
            "grandson named David to keep sheep on that "
            "hill — and over the town, unspoken, the longer "
            "line running on toward another Bethlehem "
            "child, the greater Redeemer, whose family "
            "tree keeps, in its third-to-front row, a "
            "loyal widow out of Moab. Every figure has "
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
    # FIELD: build-28 auto-match REJECTED (the barren dug treasure-plot —
    # dry dirt and walls, no crops; this row needs golden standing barley in
    # harvest). Promote-first from b17.
}
# === end PLACE-PLATES ===
