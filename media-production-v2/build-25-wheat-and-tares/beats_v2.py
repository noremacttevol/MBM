#!/usr/bin/env python3
"""V2 beat map — row 25, build-25-wheat-and-tares (Matthew 13:24-30, 43), realistic.

COVERAGE: 33 pictures against V1's EIGHT, over 160.58 s of story = 4.87 s/picture.
V1 held `s4-servants-ask.jpeg` from 48.4 s to 70.1 s (j27, n6, n7) and
`s7-harvest.jpeg` from 107.7 s to 132.7 s — TWENTY-FIVE SECONDS across j30, n11 and
n12, swallowing the whole harvest including Jesus's own "gather the wheat into my
barn". Eight pictures for a 2:47 video is one still every twenty-one seconds.

⚠️ THE V1 FINAL MP4 ON THIS ROW IS STALE AND IS **NOT** THE AUDIO AUTHORITY.
This is a new trap, not one the earlier rows documented, and it was proved from the
FILES, not from any prose:
  * `matthew-13_wheat-and-tares.mp4` was rendered 2026-07-22 02:03 and runs 229.033 s.
  * The ElevenLabs re-voice ran 2026-07-23 04:26 (`audio-eleven.log`) — AFTER it. So
    the MP4's audio is the pre-REDO-ALL voice set. Shipping it would violate REDO-ALL.
  * The mp3s were then cut again 2026-07-29 09:47 by the ECHO-DELETE sweep, which
    removed `n1` outright and trimmed one sentence out of `n9`. Both deletions are
    real echoes: n1 ("The kingdom of heaven, he said, is like a farmer who sowed good
    seed all across his field") merely repeats j24's own KJV line, and n9's deleted
    "So let them both grow." repeats j1's "Let both grow together until the harvest."
  * Transcribing the MP4 with faster-whisper puts n1 back on screen at 14-23 s, and
    transcribing `audio/n9.mp3` shows the shortened text. `n1.mp3` no longer exists;
    only an orphan `n1.mp3.words.json` does.
So the mp3 set on disk is the current narration and the MP4 is a stale render of an
older one — 229.033 s against the real 166.818 s. V1 stays read-only (hard protection
#1), so this build declares `AUDIO_FROM_V1_SEGMENTS = True` and `v2_assemble` renders
the finished track from the V1 build's OWN mp3s at exactly the offsets extract_beats
computes from that build's own constants. Nothing is re-voiced or re-timed.

⚠️ SOURCING TRAP CHECKED AND CLEARED. `make_narration.py.pre-echo` and
`make_narration.py.pre-speaker` both disagree with the live script (the pre-echo
sibling still carries n1 and the longer n9). `n9`, `s24`, `n2`, `n14` and `card` were
transcribed with faster-whisper and every one matches the LIVE script word for word;
`n9.timing.json` agrees with it too. The live script is authoritative and NO
`TEXT_OVERRIDES` are needed on this row.

⚠️ WINDOWS COMPUTED FROM SCRATCH 2026-08-02 with the fixed `extract_beats.py` reading
the V1 build, then split inside each segment on that segment's own
`audio/*.timing.json` phrase boundaries. No split falls mid-phrase. Contiguous
0.280 s → 160.858 s (the card start), zero gaps, zero overlaps.
NOTE this build computes `vdur = LEAD + audio_dur + gap` (RAW mp3 duration, not the
silence-trimmed one) and `PEAK = {"j1"}` is already a Jesus segment, so extract's
speaker test reproduces V1's `is_scripture(...) or name in PEAK` exactly.

SCRIPTURE FACTS (Matthew 13 KJV):
  v24   "The kingdom of heaven is likened unto a man which SOWED GOOD SEED in his
        field:" — good seed, deliberately sown, nothing wrong with it.
  v25   "But WHILE MEN SLEPT, his enemy came and sowed TARES among the wheat, and
        went his way." NIGHT. The enemy is not caught and does not linger.
  v26   "But when the blade was sprung up, and BROUGHT FORTH FRUIT, then appeared the
        tares also." The two are indistinguishable until the HEADS come.
  v27   "Sir, didst thou not sow good seed in thy field? from whence then hath it
        tares?" — the SERVANTS speak this. It is red-letter because Jesus is quoting
        them, but the picture must show the servants asking, not Jesus.
  v29-30 "Nay; lest while ye gather up the tares, ye ROOT UP ALSO THE WHEAT with
        them. LET BOTH GROW TOGETHER UNTIL THE HARVEST" — the householder answers.
  v30   "Gather ye together first the tares, and BIND THEM IN BUNDLES to burn them:
        but gather the wheat into MY BARN."
  v43   "Then shall the righteous SHINE FORTH AS THE SUN in the kingdom of their
        Father. Who hath ears to hear, let him hear."

BOTANICAL FACT THE STORY TURNS ON: the tare is darnel, a grass that looks like wheat
until it heads and then carries a THIN, DARK, RAGGED spike instead of the wheat's fat
pale ear. The pictures must make that difference visible at the heading stage and
invisible before it, or the parable does not read.

STAGING ACROSS THE LIBRARY — this row must not repeat a composition already used:
  rows 2, 8, 21 (Luke 15)      courtyard table / low wall under a fig tree / inside a
                               village house at a crowded meal
  row 16 (Mary & Martha)       a lamplit evening interior
  row 22 (unmerciful servant)  a black basalt Capernaum doorstep and street
  row 23 (vineyard workers)    a terraced hillside above a vineyard
  row 24 (the sower)           a moored fishing boat off a daylit shingle beach
  row 11 (the storm)           an open boat at NIGHT in a gale
  row 19 (breakfast on shore)  a Galilee beach at FIRST LIGHT with a charcoal fire
So the FRAME of this row is staged on a THRESHING FLOOR — a round, swept, packed
limestone floor on a low rise at the head of the grain plain, its winnowing forks and
grain baskets standing at the rim, listeners sitting on the stone kerb around it in
warm late-afternoon light. It is the one place in the story world that exists only
because of harvest, which is what this parable is about, and no other row uses it.

TERRAIN IS THE INVARIANT, GROWTH STAGE IS WHAT MOVES (the rule row 24 established for
a parable that spans a season; this one spans a season too). ONE field, described
identically in every frame: a long rectangular field on the flat, bounded on the near
side by a LOW DRY-LAID FIELDSTONE WALL with a single gap where the cart track enters;
ONE old carob tree alone at the far right corner; the ground lifting at the far end to
the pale limestone rise that carries the threshing floor; low tawny hills beyond. The
wall, the gap, the tree, the rise and the hills never move, never change season and
never change architecture. What changes from beat to beat is ONLY growth stage and
light:
  b03            bare, freshly broken red-brown earth, first light — the sowing
  b04-b06        that same bare sown ground at NIGHT under a low moon (v25)
  b07-b08        young green blades a hand high, clear morning — indistinguishable,
                 then headed and unmistakable
  b09-b10        knee-high and heading, morning
  b11-b21        the standing crop in tall green-gold ear, mid-morning
  b22-b23        the season turning, hard bright midday, green going to gold
  b24-b27, b32   HARVEST — ripe gold and cut stubble, late afternoon
  b28-b29, b31, b33  the threshing floor, warm low late-afternoon light
  b30            the clean field under a high bright sun
There is no sunset palette anywhere and no lamp anywhere; the only night is b04-b06.

CAST NOTE — ANCHOR-FIRST (the row-20/21/22/23/24 lesson that has held the reroll rate
at 3-15%). THREE story beats are also the identity ANCHORS and are generated in their
OWN run before anything else, each composed so its character's face is large, lit and
alone in the frame:
  b03  the FARMER, in his own field at first light with the seed in his hand
  b05  the ENEMY, close in the moonlight as he scatters the darnel
  b11  the HEAD SERVANT, at the wall, asking the question of verse 27
Each accepted anchor is wired into REFS below so every later frame naming that lock
gets the image attached. `v2_gen_api` builds its REFS cache ONCE per run, so an anchor
generated in the same run as its dependants does not exist yet when they are built —
it MUST be a separate invocation.

A FACE SHEET ALONE DOES NOT HOLD A CHARACTER WHO IS SMALL IN FRAME (rows 19, 22, 23,
24). So every lock below states age, build, hair and beard as explicit invariants, and
each beat that names a locked person also restates that person POSITIVELY in its own
scene text.

CREAM: only Jesus. A prosperous farmer is exactly the figure a model dresses in pale
undyed linen, which reads as a second unlocked Jesus, so the farmer is pinned to DEEP
UMBER-BROWN and the reapers to dark indigo. The phrase "undyed grey-brown wool" is
deliberately NOT used anywhere in this file — on row 21 it rendered near-white every
single time. Foregrounds are stated POSITIVELY (row 24's single reroll was an
out-of-focus CREAM shoulder filling the near foreground beside Jesus).
"""

# LOCKS: one entry per recurring person and per setting. Setting locks NEVER name a
# character. Clothing colours are stated POSITIVELY and DARK.
LOCKS = {
    # ------------------------------------------------------------- people ----
    "FARMER": (
        "FARMER LOCK: the man who sowed the good seed — the householder of the "
        "field — is the SAME man in every shot, and these are invariants that hold "
        "even when he is small, distant, in shadow or out of focus: a man of about "
        "forty-five, broad-shouldered and thickset with heavy hands and a short "
        "neck, deeply sun-browned olive skin, a wide open face with a heavy jaw and "
        "steady dark brown eyes set under level brows, a FULL DARK BROWN BEARD grown "
        "square to a hand's depth and shot through with grey along the jawline, and "
        "DARK BROWN HAIR to the nape of his neck, thick and pushed back off a high "
        "sunburnt forehead. He wears a DEEP UMBER-BROWN coarse wool tunic to "
        "mid-calf with straight unshaped sleeves, a dark ochre folded-cloth sash at "
        "the waist, and a heavy slate-grey wool mantle over his left shoulder, with "
        "plain dark leather sandals. He is NEVER dressed in cream, off-white or pale "
        "linen and never in any light-coloured garment; his beard is never trimmed "
        "short and never absent."
    ),
    "ENEMY": (
        "ENEMY LOCK: the man who sows the tares by night is the SAME man wherever he "
        "appears, and these are invariants even in darkness and at a distance: a lean "
        "wiry man of about thirty-five, narrow-faced and hollow-cheeked with a sharp "
        "chin, sallow olive skin, close-set dark eyes, a THIN SHORT BLACK BEARD "
        "clipped close along the jaw, and BLACK HAIR cropped to the ears. He is "
        "dressed head to foot in NEAR-BLACK DEEP INDIGO coarse wool — a short tunic "
        "to the knee, a dark cloth wound over his head and across the lower face so "
        "only the eyes and the bridge of the nose show, and a plain cord at the "
        "waist. He carries a small dark goat-hide bag slung at his hip. Nothing on "
        "him is cream, off-white or pale."
    ),
    "SERVANT": (
        "SERVANT LOCK: the head field servant who brings the question is the SAME man "
        "in every shot, and these are invariants even when he is small or turned "
        "away: a man of about twenty-eight, tall and rangy with long forearms, warm "
        "brown olive skin, a narrow eager face with a straight nose and wide dark "
        "eyes, a SHORT DARK BROWN BEARD just covering the jaw, and DARK BROWN HAIR to "
        "the jawline held back by a RUSSET-RED cloth band tied round the brow with "
        "the ends hanging at his left ear. He wears a DARK OLIVE-DRAB wool tunic to "
        "the knee with the sleeves pushed up, a plain twisted flax cord at the waist "
        "and bare legs. Never in cream, off-white or any pale garment."
    ),
    "FIELD-HANDS": (
        "FIELD-HANDS LOCK: the other field workers are grown men between twenty and "
        "fifty with sun-blackened forearms, dark beards and short dark hair, each "
        "with his own distinct face — no two share one face and none of them is the "
        "head servant, the farmer or the enemy. Their tunics are DEEP INDIGO, DARK "
        "OLIVE-DRAB, RUSSET-RED and DARK UMBER only; head cloths are dark madder-red "
        "or dark brown. NOT ONE of them wears cream, off-white, pale linen, a fleece "
        "or any light-coloured garment anywhere in the frame, in focus or out of it."
    ),
    "LISTENERS": (
        "LISTENERS LOCK: the people sitting and standing around the threshing floor "
        "are ordinary Galilean villagers of mixed age — men, women and a few "
        "children — each with a distinct face and none repeated. The men wear DEEP "
        "INDIGO, DARK UMBER and DARK OLIVE-DRAB wool; the women wear RUSSET-RED and "
        "dark madder-brown with head cloths of the same dark cloth; children are in "
        "plain dark brown. NOT ONE of them wears cream, off-white, pale linen or any "
        "light-coloured garment anywhere in the frame, including blurred figures at "
        "the edges, because a pale garment on anyone but Jesus reads as a second, "
        "unlocked Jesus and fails the picture."
    ),
    # ------------------------------------------------------------ settings ----
    "FIELD": (
        "FIELD LOCK — this terrain is IDENTICAL in every frame it appears in and only "
        "the growth stage and the light ever change: ONE long rectangular grain field "
        "lying flat on an open plain, bounded along the near side by a LOW DRY-LAID "
        "FIELDSTONE WALL of rough pale limestone about knee-high, with a single gap "
        "in it where a worn cart track enters the field. ONE old carob tree with a "
        "short thick trunk and a dense dark crown stands alone at the far right "
        "corner of the field and nowhere else. At the far end the ground lifts to a "
        "low pale limestone rise, and low tawny bare hills close the horizon beyond "
        "it. The soil is red-brown and stony. There is no other building, no fence, "
        "no track, no tree and no wall anywhere in the view, and the wall, the gap, "
        "the tree, the rise and the hills never move, never change shape and never "
        "change season between frames."
    ),
    "DARNEL": (
        "DARNEL LOCK: the weed among the wheat is darnel, a grass of exactly the same "
        "height and blade as the wheat. BEFORE THE HEADS FORM the two plants are "
        "genuinely indistinguishable — identical green blades, identical height, no "
        "difference a viewer could point at. ONCE THE HEADS FORM the difference is "
        "obvious and must be visible: the wheat carries a FAT, UPRIGHT, PALE-GOLD EAR "
        "with plump grains, while the darnel carries a THIN, DARK GREY-GREEN, RAGGED "
        "SPIKE that leans and splays. Wherever both are shown headed they stand mixed "
        "through one another all across the field, never sorted into separate "
        "patches. There are no flowers, no thistles, no brambles and no broadleaf "
        "weeds anywhere — the only two plants in the field are wheat and darnel."
    ),
    "THRESHING-FLOOR": (
        "THRESHING-FLOOR LOCK: a round, swept threshing floor about eight paces "
        "across, its surface packed earth beaten hard over pale flat limestone slabs, "
        "laid on a low open rise at the head of the grain plain where the wind "
        "crosses it. A low kerb of set fieldstones rings it. Standing at the rim are "
        "hand-made harvest tools only: wooden winnowing forks with three or four "
        "hewn prongs, flat wooden winnowing shovels, and round baskets of coiled "
        "plant fibre, some upright and some tipped on their sides. The grain plain "
        "and the low tawny hills open out below and beyond. There is no building, no "
        "roof, no post, no rope rigging and no animal on the floor itself."
    ),
    "BARN": (
        "BARN LOCK: the granary is a plain rectangular first-century field store "
        "built of rough dry-laid limestone blocks with a flat mud-and-timber roof of "
        "hewn poles and packed earth, a single low doorway closed by a plank of hewn "
        "wood, and no window. Large coiled-fibre grain baskets and hand-thrown clay "
        "storage jars stand inside and beside the doorway. Its walls are pale stone, "
        "but nothing about it is cloth and no garment anywhere near it is pale."
    ),
}

OUTPUT_ASSET_DIR = "assets"

# The finished V1 MP4 predates this build's current narration (see the module
# docstring), so the authoritative audio is rebuilt from the V1 build's own mp3s at
# the extract_beats offsets. Zero re-voicing; V1 is never written to.
AUDIO_FROM_V1_SEGMENTS = True

REF = True

REFS = {
    "FARMER": "assets/s03-clean-good-seed.jpeg",
    "ENEMY": "assets/s05-while-everyone-slept.jpeg",
    "SERVANT": "assets/s11-didst-thou-not-sow-good-seed.jpeg",
}

BEATS = [
    # ============================ FRAME — the threshing floor, late afternoon ====
    {
        "id": "v2-r025-b01", "out": "s01-another-parable.jpeg", "seg": "s24",
        "window": "0.28-4.068", "wide": True, "jesus": True, "ref": REF,
        "locks": ["THRESHING-FLOOR", "LISTENERS"],
        "narration": "Another parable put he forth unto them, saying,",
        "must_show": "Jesus seated on the stone kerb of a round threshing floor in warm late-afternoon light, beginning to speak, with village listeners settled on the kerb and the ground around him.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no sunset colouring, no boat, no water, no building; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, fast prime, warm low late-afternoon sunlight "
            "raking in from the left across the swept floor, long soft shadows, fine "
            "film grain. THE CAMERA STANDS BEHIND THE NEAREST LISTENERS AND SHOOTS "
            "PAST THEM ACROSS THE FLOOR: two seated backs fill the near bottom "
            "corners, soft and out of focus, a DEEP INDIGO shoulder at the near left "
            "and a DARK UMBER back at the near right, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. Sharp in the middle distance Jesus sits on the low "
            "stone kerb on the far side of the floor, leaning slightly forward with "
            "his forearms on his knees and one hand open as he begins to speak, his "
            "head turned to his right and his gaze travelling along the seated row to "
            "the right-hand edge of the frame. Around him the villagers sit on the "
            "kerb and on the packed floor in dark indigo, russet and umber wool, all "
            "of them facing him. A wooden winnowing fork leans against the kerb at "
            "the left. The grain plain and low tawny hills open out behind him."
        ),
    },
    {
        "id": "v2-r025-b02", "out": "s02-a-man-sowed-good-seed.jpeg", "seg": "j24",
        "window": "4.068-9.495", "jesus": True, "ref": REF,
        "locks": ["THRESHING-FLOOR"],
        "narration": "The kingdom of heaven is likened unto a man which sowed good seed in his field:",
        "must_show": "a closer photograph of Jesus alone on the kerb of the threshing floor, mid-sentence, one hand turned palm-up as he describes the sowing.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no sunset colouring; no second figure in cream or off-white anywhere in the frame; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, warm low "
            "late-afternoon sunlight from the left modelling one side of his face "
            "while the shaded side stays open and readable, fine film grain. THE "
            "CAMERA SITS LOW AND WELL TO HIS RIGHT SIDE, SO HIS EYELINE RUNS "
            "HORIZONTALLY ACROSS THE FRAME AND OUT THROUGH THE RIGHT EDGE and never "
            "toward the lens. Jesus is framed from the waist up, seated on the low "
            "stone kerb, his body turned three-quarters away from the camera toward "
            "the listeners, his right hand lifted and turned palm-up in the "
            "explaining gesture, his lips parted mid-word and his expression warm and "
            "unhurried. The near foreground between the camera and him is nothing but "
            "the empty swept surface of the threshing floor, with nobody standing, "
            "sitting or passing between the camera and him. Behind him the floor falls "
            "out of focus into the pale grain plain and the low tawny hills, with the "
            "blurred hewn prongs of a wooden winnowing fork at the far right edge."
        ),
    },
    # ================================================ THE SOWING — first light ====
    {
        # ANCHOR — the FARMER's face sheet. Generated in its own run.
        "id": "v2-r025-b03", "out": "s03-clean-good-seed.jpeg", "seg": "n2",
        "window": "9.495-15.171",
        "locks": ["FARMER", "FIELD"],
        "narration": "It was clean, good wheat seed. He wanted a good harvest, and he did everything right.",
        "must_show": "the farmer standing alone in his own bare freshly broken field at first light, a handful of clean plump wheat seed lifted in his open palm, looking down at it with quiet satisfaction.",
        "must_not_show": "no other person anywhere in the frame; no growing crop of any kind, the ground is bare; no night, no lamp; no cream, off-white or pale garment on him; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, clear low first-light "
            "sun from the right laying warm light straight across his face and the "
            "seed in his hand, fine film grain. THE CAMERA IS AT CHEST HEIGHT SLIGHTLY "
            "TO HIS LEFT AND HIS EYELINE RUNS STEEPLY DOWNWARD TO THE SEED IN HIS OWN "
            "PALM, well below the lens. The farmer is framed from the waist up and "
            "fills the frame, a thickset sun-browned man of about forty-five with a "
            "full square DARK BROWN beard greying along the jaw and dark brown hair "
            "pushed back off a high forehead, in a DEEP UMBER-BROWN coarse wool tunic "
            "with a dark ochre sash and a slate-grey mantle over his left shoulder. "
            "His left hand holds the mouth of a heavy woven seed bag slung across his "
            "body; his right hand is lifted open at chest height with a small heap of "
            "plump pale-gold wheat grains in the palm, every grain separate and "
            "sharply in focus. He is the only person in the picture. Behind him the "
            "bare red-brown broken earth of the field runs soft and out of focus to "
            "the low dry-laid limestone wall, the gap where the cart track enters, and "
            "the lone carob tree at the far right corner."
        ),
    },
    # ========================================== THE ENEMY — night, verse 25 ====
    {
        "id": "v2-r025-b04", "out": "s04-while-men-slept.jpeg", "seg": "j25",
        "window": "15.171-20.911", "wide": True,
        "locks": ["FIELD"],
        "narration": "But while men slept, his enemy came and sowed tares among the wheat, and went his way.",
        "must_show": "the whole sown field lying empty and silent at night under a low moon, with one small dark figure just entering through the gap in the field wall, far off and unnoticed.",
        "must_not_show": "no sunset or sunrise colouring of any kind, this is deep night; no lamp, torch, fire or lantern anywhere; no growing crop, the ground is bare and freshly sown; no cream or pale garment anywhere; nobody looking into the lens.",
        "scene": (
            "One photograph, 28mm lens, DEEP NIGHT lit only by a low moon behind the "
            "camera's left shoulder — cool silver-blue light, deep blue-black shadow, "
            "the sky full of stars, no warm colour anywhere in the picture, fine film "
            "grain and true low-light noise. THE CAMERA STANDS INSIDE THE FIELD BEHIND "
            "THE NEAR WALL AND SHOOTS BACK TOWARD THE GAP: the top of the low dry-laid "
            "limestone wall runs across the near bottom of the frame, dark and out of "
            "focus, with nothing between the camera and it but bare open ground and "
            "nobody standing there. The bare red-brown sown soil stretches away, "
            "faintly ridged where the seed was worked in. At the gap in the wall, "
            "small and sharp in the middle distance, ONE lone hooded figure in "
            "near-black cloth has stepped through and stands turned away in profile, "
            "looking down the length of the field away from the camera. The lone carob "
            "tree stands black against the stars at the far right corner and the low "
            "rise closes the far end. He is the only person anywhere in the frame."
        ),
    },
    {
        # ANCHOR — the ENEMY's face sheet. Generated in its own run.
        "id": "v2-r025-b05", "out": "s05-while-everyone-slept.jpeg", "seg": "n3",
        "window": "20.911-28.091",
        "locks": ["ENEMY", "FIELD"],
        "narration": "But that night, while everyone was asleep, an enemy of his crept into the field and scattered weed seeds all through the wheat.",
        "must_show": "the enemy close in the moonlight, crouched low in the middle of the bare sown field, flinging a fistful of dark darnel seed out over the ground with his face lit and readable.",
        "must_not_show": "no sunset or sunrise colouring, this is deep night; no lamp, torch or fire anywhere; no other person in the frame; no cream or pale cloth anywhere; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, DEEP NIGHT lit only by "
            "a low moon from the right laying clear cool silver light across his face "
            "and forearm, deep blue-black shadow behind, fine film grain and true "
            "low-light noise. THE CAMERA IS DOWN AT GROUND LEVEL SLIGHTLY TO HIS RIGHT "
            "AND HIS EYELINE RUNS DOWNWARD AND AWAY ALONG THE GROUND toward the bottom "
            "left corner, following his own throw, never toward the lens. He is framed "
            "from the thighs up and fills the frame: a lean wiry narrow-faced man of "
            "about thirty-five in NEAR-BLACK DEEP INDIGO wool, the dark cloth wound "
            "over his head and across the lower face so only his close-set dark eyes "
            "and the bridge of his nose show, crouched forward on one knee in the bare "
            "red-brown earth with a small dark goat-hide bag open at his hip. His "
            "right arm is caught mid-sweep, low and across his body, and a scatter of "
            "small dark seeds hangs in the air in front of it, each seed separate "
            "against the moonlight. He is the only person in the picture. Behind him "
            "the field runs out of focus to the low wall and the black shape of the "
            "lone carob tree."
        ),
    },
    {
        "id": "v2-r025-b06", "out": "s06-he-slipped-away.jpeg", "seg": "n3",
        "window": "28.091-31.942", "wide": True,
        "locks": ["ENEMY", "FIELD"],
        "narration": "Then he slipped away, and no one saw.",
        "must_show": "the enemy already leaving, seen from behind at a distance as he steps back out through the gap in the field wall into the dark, with the sown field empty behind him.",
        "must_not_show": "no sunset or sunrise colouring, this is deep night; no lamp, torch or fire; no other person anywhere; no cream or pale cloth; no face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, DEEP NIGHT under a low moon from the left, "
            "cool silver-blue light and deep blue-black shadow, no warm colour "
            "anywhere, fine film grain and true low-light noise. THE CAMERA STANDS IN "
            "THE FIELD BEHIND HIM AND SHOOTS AT HIS BACK: he is walking directly away "
            "from the camera, seen entirely from behind, so no face is visible at all. "
            "He is small in the frame at the gap in the low dry-laid limestone wall, a "
            "lean figure in NEAR-BLACK DEEP INDIGO with the dark head cloth still "
            "wound over his head, the empty goat-hide bag hanging slack at his hip, "
            "one foot already through the gap onto the cart track outside. The bare "
            "sown red-brown ground fills the whole foreground with nobody standing on "
            "it. The lone carob tree is black against the stars at the far right "
            "corner and the low rise closes the far end. He is the only person in the "
            "picture."
        ),
    },
    # ============================= BOTH COME UP — indistinguishable, then not ====
    {
        "id": "v2-r025-b07", "out": "s07-looks-like-young-wheat.jpeg", "seg": "n4",
        "window": "31.942-35.272",
        "locks": ["FIELD", "DARNEL"],
        "narration": "The weed he chose looks almost exactly like young wheat.",
        "must_show": "a very close photograph low among young green blades a hand high, where every blade looks exactly the same as every other and no difference can be seen.",
        "must_not_show": "no heads, ears or seed spikes of any kind, the plants are too young; no flowers, thistles or broadleaf weeds; no person anywhere in the frame; no night, this is clear morning.",
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, clear soft "
            "morning sunlight from the left, fine film grain. THE CAMERA LIES ALMOST "
            "ON THE SOIL LOOKING HORIZONTALLY THROUGH THE YOUNG CROP, with no person "
            "anywhere in the picture. Young green grass blades a hand high stand thick "
            "and even out of the red-brown stony earth, a few sharp in the near middle "
            "and the rest falling away into soft green blur. Every blade has the same "
            "width, the same colour and the same upright habit as every other blade, "
            "so that nothing in the picture marks one plant as different from another. "
            "A few crumbs of dry soil and one small pale limestone chip sit sharp in "
            "the very near foreground."
        ),
    },
    {
        "id": "v2-r025-b08", "out": "s08-until-the-heads-appear.jpeg", "seg": "n4",
        "window": "35.272-39.577",
        "locks": ["FIELD", "DARNEL"],
        "narration": "You cannot tell them apart until they grow up and the heads appear.",
        "must_show": "a close photograph of the crop now headed, with fat pale-gold wheat ears and thin dark ragged darnel spikes standing side by side so the difference is unmistakable.",
        "must_not_show": "no person anywhere in the frame; no flowers, thistles or broadleaf weeds; no night; no separate patches, the two plants are mixed through one another.",
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, clear soft "
            "morning sunlight from the left, fine film grain. THE CAMERA IS AT THE "
            "HEIGHT OF THE EARS LOOKING HORIZONTALLY ALONG THE ROW, with no person "
            "anywhere in the picture. Sharp across the middle of the frame stand three "
            "or four FAT UPRIGHT PALE-GOLD WHEAT EARS with plump grains and stiff "
            "whiskers, and standing directly among them, at the same height and on the "
            "same green stems, two THIN DARK GREY-GREEN RAGGED SPIKES that lean and "
            "splay open. The difference between the two kinds of head is obvious and "
            "fully in focus. Behind them the rest of the field falls into a soft "
            "green-gold blur under a pale morning sky."
        ),
    },
    {
        "id": "v2-r025-b09", "out": "s09-came-up-green-and-strong.jpeg", "seg": "n5",
        "window": "39.577-44.607", "wide": True,
        "locks": ["FIELD", "DARNEL"],
        "narration": "So the wheat came up green and strong, and right in the middle of it, so did the weeds.",
        "must_show": "the whole field seen from the near wall, standing knee-high and green and strong across its full length in clear morning light.",
        "must_not_show": "no person anywhere in the frame; no night, no lamp, no sunset colouring; no bare ground, the field is fully grown up; no building.",
        "scene": (
            "One photograph, 28mm lens, clear bright morning sunlight from the right, "
            "crisp short shadows, a pale blue sky, fine film grain. THE CAMERA STANDS "
            "JUST OUTSIDE THE LOW WALL, BEHIND THE WALL LINE AND SHOOTING PAST IT "
            "FROM THE SIDE DOWN THE LENGTH OF THE "
            "FIELD, with no person anywhere in the picture and nobody between the "
            "camera and the wall. The top of the low dry-laid pale limestone wall runs "
            "across the near bottom of the frame, sharp and lit, with the gap where "
            "the cart track enters at the near left. Beyond it the crop stands "
            "knee-high and dense green across the whole field, the heads just "
            "beginning to form, the surface of it leaning one way under the wind. The "
            "lone carob tree with its short thick trunk and dark crown stands at the "
            "far right corner, the ground lifts to the pale limestone rise at the far "
            "end, and low tawny bare hills close the horizon."
        ),
    },
    {
        "id": "v2-r025-b10", "out": "s10-the-field-was-full-of-both.jpeg", "seg": "n5",
        "window": "44.607-48.362",
        "locks": ["FIELD", "DARNEL"],
        "narration": "Now anyone could see the field was full of both.",
        "must_show": "a waist-height photograph into the standing crop where fat pale-gold wheat ears and thin dark ragged darnel spikes are mixed through one another everywhere, right across the field.",
        "must_not_show": "no person anywhere in the frame; no separate patches or clean edges between the two plants; no flowers, thistles or broadleaf weeds; no night.",
        "scene": (
            "One photograph, 50mm lens, moderate depth of field so the mixing stays "
            "readable well back into the field, clear bright morning sunlight from the "
            "right, fine film grain. THE CAMERA IS AT WAIST HEIGHT LOOKING OUT ACROSS "
            "THE TOP OF THE CROP, with no person anywhere in the picture. The standing "
            "crop fills the whole lower two thirds of the frame: FAT UPRIGHT PALE-GOLD "
            "WHEAT EARS and THIN DARK GREY-GREEN RAGGED SPIKES stand shoulder to "
            "shoulder throughout, scattered evenly through one another with no patch "
            "anywhere that is only one kind, the dark heads clearly visible against "
            "the pale ones all the way back. Above them the field runs to the low "
            "dry-laid wall, the lone carob tree at the far right corner, the pale "
            "limestone rise and the low tawny hills under a pale blue sky."
        ),
    },
    # ========================================== THE SERVANTS ASK — verse 27 ====
    {
        # ANCHOR — the SERVANT's face sheet. Generated in its own run.
        "id": "v2-r025-b11", "out": "s11-didst-thou-not-sow-good-seed.jpeg", "seg": "j27",
        "window": "48.362-54.285",
        "locks": ["SERVANT", "FIELD", "DARNEL"],
        "narration": "Sir, didst thou not sow good seed in thy field? from whence then hath it tares?",
        "must_show": "the head servant at the field wall holding up a torn-off dark ragged darnel spike, asking his question, his face large and lit and full of baffled dismay.",
        "must_not_show": "no other person in the frame; no night, no lamp; no cream, off-white or pale garment on him; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, clear mid-morning "
            "sunlight from the left modelling his face, fine film grain. THE CAMERA "
            "SITS SLIGHTLY BELOW HIS EYE LEVEL AND WELL TO HIS LEFT, SO HIS EYELINE "
            "RUNS HORIZONTALLY ACROSS THE FRAME AND OUT THROUGH THE LEFT EDGE toward "
            "the man he is speaking to, and never toward the lens. He is framed from "
            "the chest up and fills the frame: a tall rangy man of about twenty-eight "
            "with a narrow eager face, a SHORT DARK BROWN beard just covering the jaw "
            "and dark brown hair to the jawline held back by a RUSSET-RED cloth band "
            "tied at the brow with the ends hanging at his left ear, in a DARK "
            "OLIVE-DRAB wool tunic with the sleeves pushed up his forearms. His right "
            "hand is lifted to chest height holding up a single torn-off THIN DARK "
            "GREY-GREEN RAGGED DARNEL SPIKE, sharp and fully in focus, its root end "
            "still trailing soil. His brows are drawn together and his mouth is open "
            "mid-question. He is the only person in the picture. Behind him the "
            "standing green-gold crop and the low dry-laid wall fall out of focus."
        ),
    },
    {
        "id": "v2-r025-b12", "out": "s12-the-workers-were-upset.jpeg", "seg": "n6",
        "window": "54.285-59.315", "wide": True,
        "locks": ["SERVANT", "FIELD-HANDS", "FIELD", "DARNEL"],
        "narration": "The workers were upset. They came to the farmer and said, did you not plant good seed?",
        "must_show": "four field workers striding up the cart track from the standing crop toward the field wall, agitated, two of them carrying torn-out dark darnel spikes.",
        "must_not_show": "no cream, off-white or pale garment on anyone in the frame; no night, no lamp; nobody advancing into the camera and no face turned toward the lens; no more than four people.",
        "scene": (
            "One photograph, 35mm lens, clear mid-morning sunlight from the right, "
            "crisp short shadows, fine film grain. THE CAMERA STANDS INSIDE THE FIELD "
            "TO ONE SIDE OF THE CART TRACK AND SHOOTS ACROSS IT, so the four men are "
            "seen in full side profile moving from the right of the frame toward the "
            "left, NOT ONE FACE IS TURNED TOWARD THE LENS and nobody advances into the "
            "camera. Exactly FOUR men are in the picture and no fifth. Nearest the "
            "camera and sharpest is the head servant, a tall rangy man of about "
            "twenty-eight with a short dark brown beard and a RUSSET-RED brow band "
            "with the ends hanging at his left ear, in a DARK OLIVE-DRAB tunic, "
            "striding hard with a torn-out THIN DARK GREY-GREEN RAGGED DARNEL SPIKE "
            "swinging in his right fist. Behind him three other field hands in DEEP "
            "INDIGO, RUSSET-RED and DARK UMBER wool, each with his own distinct "
            "dark-bearded face, one of them also carrying a pulled darnel plant with "
            "soil on the roots. The standing green-gold crop fills the background to "
            "the low dry-laid wall and the lone carob tree at the far right corner."
        ),
    },
    {
        "id": "v2-r025-b13", "out": "s13-where-did-these-come-from.jpeg", "seg": "n6",
        "window": "59.315-62.338",
        "locks": ["SERVANT", "FARMER", "FIELD"],
        "narration": "Where did all these weeds come from?",
        "must_show": "the head servant and the farmer face to face at the field wall, the servant's hand thrown out toward the field behind him, the farmer listening.",
        "must_not_show": "no cream, off-white or pale garment on either man; no night, no lamp; no third person in the frame; neither man's pupils centred on the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, clear mid-morning "
            "sunlight from the right, fine film grain. THE CAMERA IS SIDE-ON TO THE "
            "TWO MEN AT CHEST HEIGHT SO THEIR EYELINES RUN HORIZONTALLY ACROSS THE "
            "FRAME INTO EACH OTHER and neither looks anywhere near the lens. On the "
            "left, sharp, the head servant stands in three-quarter profile facing "
            "right — a tall rangy man of about twenty-eight with a short dark brown "
            "beard and a RUSSET-RED brow band, in a DARK OLIVE-DRAB tunic — his left "
            "arm flung back and out toward the standing crop behind him, his face "
            "turned up to the older man. On the right, facing him, the farmer stands "
            "in three-quarter profile — a thickset sun-browned man of about "
            "forty-five with a full square dark brown beard greying along the jaw, in "
            "a DEEP UMBER-BROWN tunic with a dark ochre sash and a slate-grey mantle "
            "over his left shoulder — listening with his head lowered a little and his "
            "hands still at his sides. Only these two people are in the frame and the "
            "ground between the camera and them is bare open earth. The low dry-laid "
            "limestone wall runs behind them with the green-gold crop beyond it out of "
            "focus."
        ),
    },
    {
        "id": "v2-r025-b14", "out": "s14-an-enemy-has-done-this.jpeg", "seg": "n7",
        "window": "62.338-65.308",
        "locks": ["FARMER", "FIELD"],
        "narration": "He told them, an enemy has done this.",
        "must_show": "a close photograph of the farmer alone, quiet and certain, looking out over his ruined field as he says it.",
        "must_not_show": "no other person in the frame; no anger, no shouting, no raised fist; no cream, off-white or pale garment on him; no night; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, clear mid-morning "
            "sunlight from the right laying warm light along his cheek, fine film "
            "grain. THE CAMERA IS AT HIS SHOULDER HEIGHT AND WELL TO HIS RIGHT, SO HIS "
            "EYELINE RUNS HORIZONTALLY ACROSS THE FRAME AND OUT THROUGH THE LEFT EDGE "
            "over the crop, and never toward the lens. The farmer is framed from the "
            "chest up and fills the frame, alone: a thickset sun-browned man of about "
            "forty-five with a full square DARK BROWN beard greying along the jaw and "
            "dark brown hair pushed back off a high forehead, in a DEEP UMBER-BROWN "
            "coarse wool tunic with a dark ochre sash and a slate-grey mantle over his "
            "left shoulder. His jaw is set and his expression is level and unangry, "
            "the look of a man who already knows the answer. One heavy hand rests flat "
            "on the top stone of the low wall. He is the only person in the picture. "
            "Behind him the standing green-gold crop falls away into soft blur."
        ),
    },
    {
        "id": "v2-r025-b15", "out": "s15-shall-we-pull-them-out.jpeg", "seg": "n7",
        "window": "65.308-70.051", "wide": True,
        "locks": ["SERVANT", "FIELD-HANDS", "FARMER", "FIELD", "DARNEL"],
        "narration": "And they asked, do you want us to go and pull all the weeds out right now?",
        "must_show": "the four workers already half-turned toward the standing crop, poised to wade in and start pulling, waiting on the farmer's word.",
        "must_not_show": "no cream, off-white or pale garment on anyone in the frame; no night; nobody advancing into the camera and no face turned toward the lens; no more than five people in total.",
        "scene": (
            "One photograph, 35mm lens, clear mid-morning sunlight from the right, "
            "crisp short shadows, fine film grain. THE CAMERA STANDS BEHIND THE GROUP "
            "AT THE WALL AND SHOOTS PAST THEM INTO THE FIELD: the backs and shoulders "
            "of the four field workers fill the near half of the frame, seen from "
            "behind and from the side, and NOT ONE FACE IS TURNED TOWARD THE LENS. "
            "Exactly FIVE people are in the picture and no sixth. Nearest the camera "
            "at the left, the head servant is seen from behind and slightly in "
            "profile, a tall rangy man in a DARK OLIVE-DRAB tunic with the RUSSET-RED "
            "brow band's ends hanging at his left ear, one leg already lifted over the "
            "low wall and his body twisted back over his shoulder. Beside him three "
            "other field hands in DEEP INDIGO, RUSSET-RED and DARK UMBER wool lean "
            "forward toward the crop with their hands open and ready. Facing all of "
            "them, small and sharp beyond the wall on the right, the farmer stands in "
            "profile in his DEEP UMBER-BROWN tunic with the slate-grey mantle, one "
            "hand beginning to lift. The green-gold crop with its pale wheat ears and "
            "dark ragged darnel spikes fills the background to the lone carob tree."
        ),
    },
    # ========================================== THE ANSWER — verses 29-30 ====
    {
        "id": "v2-r025-b16", "out": "s16-what-kind-of-man-he-is.jpeg", "seg": "n8",
        "window": "70.051-72.941",
        "locks": ["FARMER", "FIELD"],
        "narration": "And here is where you see what kind of man he is.",
        "must_show": "a very close photograph of the farmer's face as he weighs the answer, patient and unhurried, the ruined field soft behind him.",
        "must_not_show": "no other person in the frame; no anger; no cream, off-white or pale garment; no night; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 135mm lens, very shallow depth of field, clear "
            "mid-morning sunlight from the right, fine film grain. THE CAMERA IS "
            "SIDE-ON TO HIM AT EYE LEVEL SO HIS EYELINE RUNS HORIZONTALLY ACROSS THE "
            "FRAME AND OUT THROUGH THE LEFT EDGE toward the field, never toward the "
            "lens. His head and shoulders fill the frame, alone: a thickset "
            "sun-browned man of about forty-five with a full square DARK BROWN beard "
            "greying along the jaw, dark brown hair pushed back off a high sunburnt "
            "forehead, and steady dark brown eyes under level brows, in a DEEP "
            "UMBER-BROWN coarse wool tunic with a slate-grey mantle at his left "
            "shoulder. Every line of his weathered face is sharp — the sun creases at "
            "the eye, the grey in the beard, the dust on his skin. His expression is "
            "quiet and considering, not angry. He is the only person in the picture "
            "and the green-gold crop behind him is a soft wash of blur."
        ),
    },
    {
        "id": "v2-r025-b17", "out": "s17-he-said-no.jpeg", "seg": "n8",
        "window": "72.941-77.634",
        "locks": ["FARMER", "SERVANT", "FIELD"],
        "narration": "He did not send them tearing through the field. He said, no.",
        "must_show": "the farmer's open hand raised low and flat to stop the servant, holding him back from the crop, both men in profile.",
        "must_not_show": "no cream, off-white or pale garment on either man; no night; no third person in the frame; no pulling or trampling of the crop; neither man's pupils centred on the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, clear mid-morning "
            "sunlight from the right, fine film grain. THE CAMERA IS SIDE-ON AT CHEST "
            "HEIGHT SO BOTH EYELINES RUN HORIZONTALLY ACROSS THE FRAME INTO EACH "
            "OTHER and neither man looks anywhere near the lens. Sharp in the near "
            "middle, the farmer's right hand is raised low and flat, palm down and "
            "open, at the height of the servant's chest — the sharpest thing in the "
            "picture, its calluses and dust fully resolved. Behind that hand the "
            "farmer stands in three-quarter profile facing left, a thickset "
            "sun-browned man of about forty-five with a full square DARK BROWN beard "
            "greying along the jaw, in a DEEP UMBER-BROWN tunic with a dark ochre "
            "sash and a slate-grey mantle over his left shoulder, his head shaking "
            "slightly and his expression firm and kind. Facing him at the left edge, "
            "the head servant has stopped mid-stride in his DARK OLIVE-DRAB tunic "
            "with the RUSSET-RED brow band, his weight still forward, his own hands "
            "dropping. Only these two people are in the frame. The green-gold crop "
            "and the low dry-laid wall are soft behind them."
        ),
    },
    {
        "id": "v2-r025-b18", "out": "s18-ye-root-up-also-the-wheat.jpeg", "seg": "j1",
        "window": "77.634-82.034",
        "locks": ["FIELD", "DARNEL"],
        "narration": "Nay; lest while ye gather up the tares, ye root up also the wheat with them.",
        "must_show": "a very close photograph at the soil line of one darnel plant being lifted, its roots twisted tightly around the roots of the wheat plants beside it so they come up together.",
        "must_not_show": "no person's face in the frame; no night; no clean separated roots — the two root systems are visibly tangled into one another; no flowers or broadleaf weeds.",
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, clear "
            "mid-morning sunlight from the left, fine film grain. THE CAMERA IS DOWN "
            "AT THE SOIL LINE LOOKING HORIZONTALLY INTO THE BASE OF THE CROP; no face "
            "appears in the picture at all. Sharp in the centre a single darnel plant "
            "has been drawn part-way out of the red-brown earth, and its pale fibrous "
            "roots are visibly braided and knotted through the roots of THREE wheat "
            "plants standing beside it, so that the wheat stems are already tilting "
            "and lifting with it and a wedge of soil is breaking away under them. A "
            "weathered brown hand grips the darnel stem low at the top edge of the "
            "frame, cropped at the wrist. Loose crumbs of soil hang in the air. Above "
            "and behind, the standing stems blur into green-gold."
        ),
    },
    {
        "id": "v2-r025-b19", "out": "s19-let-both-grow-together.jpeg", "seg": "j1",
        "window": "82.034-85.987", "wide": True,
        "locks": ["FARMER", "SERVANT", "FIELD-HANDS", "FIELD"],
        "narration": "Let both grow together until the harvest.",
        "must_show": "the farmer turning back to the field with the workers standing down behind him, the whole standing crop left untouched in front of them.",
        "must_not_show": "no cream, off-white or pale garment on anyone; no night; no trampled or pulled crop; nobody advancing into the camera and no face turned toward the lens; no more than five people.",
        "scene": (
            "One photograph, 35mm lens, clear mid-morning sunlight from the right, "
            "crisp short shadows, fine film grain. THE CAMERA STANDS BEHIND ALL FIVE "
            "MEN AT THE WALL AND SHOOTS PAST THEM DOWN THE FIELD: every one of them is "
            "seen from behind or in three-quarter from behind, NOT ONE FACE IS TURNED "
            "TOWARD THE LENS, and nobody moves toward the camera. Exactly FIVE people "
            "are in the picture and no sixth. Nearest and largest, seen from behind, "
            "the farmer stands square-shouldered in his DEEP UMBER-BROWN tunic with "
            "the slate-grey mantle across his left shoulder, both hands loose at his "
            "sides, facing away down the length of the crop. A pace behind him and to "
            "the left the head servant stands down, seen from behind in his DARK "
            "OLIVE-DRAB tunic with the RUSSET-RED brow band's ends showing at the side "
            "of his head, his arms lowered. Three other field hands in DEEP INDIGO, "
            "RUSSET-RED and DARK UMBER wool stand back along the wall, also facing "
            "away. In front of all of them the untouched green-gold crop runs unbroken "
            "to the lone carob tree at the far right corner, the pale limestone rise "
            "at the far end and the low tawny hills."
        ),
    },
    {
        "id": "v2-r025-b20", "out": "s20-their-roots-are-tangled.jpeg", "seg": "n9",
        "window": "85.987-93.637",
        "locks": ["FIELD", "DARNEL"],
        "narration": "In other words: if you rip the weeds out now, their roots are tangled around the wheat, and you will tear up the good plants along with them.",
        "must_show": "a close photograph of a torn hole in the standing crop where a darnel plant has just been pulled, with four good wheat plants dragged out of the ground on their sides beside it.",
        "must_not_show": "no person's face in the frame; no night; no tidy or repaired ground — the damage is obvious; no flowers or broadleaf weeds.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, clear mid-morning "
            "sunlight from the left throwing the torn hollow into relief, fine film "
            "grain. THE CAMERA LOOKS STEEPLY DOWN INTO THE BASE OF THE CROP FROM JUST "
            "ABOVE IT; no face appears in the picture at all. Sharp in the centre is a "
            "ragged hole torn in the standing crop: bare broken red-brown soil, a "
            "loose wedge of earth turned over, and lying on their sides beside it "
            "exactly FOUR uprooted wheat plants, each one whole and separately "
            "countable with its FAT PALE-GOLD EAR still attached and its pale roots "
            "trailing soil. One THIN DARK GREY-GREEN RAGGED DARNEL SPIKE lies across "
            "them. The standing crop leans in over the hole from every side and falls "
            "out of focus into green-gold."
        ),
    },
    {
        "id": "v2-r025-b21", "out": "s21-not-lose-a-single-stalk.jpeg", "seg": "n9",
        "window": "93.637-97.697",
        "locks": ["FARMER", "FIELD", "DARNEL"],
        "narration": "He would rather wait than lose a single stalk of wheat.",
        "must_show": "the farmer's weathered hand closed gently around one standing wheat stem, steadying it without pulling it, his face soft behind it.",
        "must_not_show": "no other person in the frame; no pulling, tearing or cutting; no night; no cream, off-white or pale garment; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 100mm lens, very shallow depth of field, clear "
            "mid-morning sunlight from the right, fine film grain. THE CAMERA IS AT "
            "THE HEIGHT OF THE EARS AND WELL TO HIS LEFT, SO HIS EYELINE RUNS "
            "DOWNWARD AND ACROSS TO THE STEM IN HIS OWN HAND, well below and to the "
            "side of the lens. Sharp in the near centre, a broad weathered sun-browned "
            "hand is closed loosely around one standing green stem just under its FAT "
            "PALE-GOLD EAR, holding it upright without bending or pulling it, every "
            "callus and dust line in focus. Softer behind the hand, the farmer's face "
            "is turned down toward it — a thickset man of about forty-five with a full "
            "square DARK BROWN beard greying along the jaw, in a DEEP UMBER-BROWN "
            "tunic with a slate-grey mantle at his shoulder — his expression quiet and "
            "protective. He is the only person in the picture and the rest of the crop "
            "is a green-gold blur."
        ),
    },
    # ================================================== THE SEASON PASSES ====
    {
        "id": "v2-r025-b22", "out": "s22-so-the-farmer-waited.jpeg", "seg": "n10",
        "window": "97.697-99.217",
        "locks": ["FARMER", "FIELD"],
        "narration": "So the farmer waited.",
        "must_show": "the farmer alone and small, sitting on the low field wall, simply watching his field.",
        "must_not_show": "no other person anywhere in the frame; no night, no lamp, no sunset colouring; no work being done; no cream, off-white or pale garment; no face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, hard bright midday sunlight from high above, "
            "short shadows straight below, a pale washed sky, fine film grain. THE "
            "CAMERA STANDS BEHIND HIM AND OFF TO HIS LEFT AND SHOOTS PAST HIM INTO THE "
            "FIELD, so he is seen from behind and slightly in profile and no face is "
            "turned toward the lens. He sits small in the frame on the top stones of "
            "the low dry-laid limestone wall, elbows on his knees, a thickset "
            "square-shouldered man in a DEEP UMBER-BROWN tunic with a slate-grey "
            "mantle across his left shoulder, perfectly still. He is the only person "
            "in the picture and the ground between the camera and him is bare open "
            "earth. In front of him the crop stands tall and half-turned from green to "
            "gold, running away to the lone carob tree at the far right corner, the "
            "pale limestone rise at the far end and the low tawny hills."
        ),
    },
    {
        "id": "v2-r025-b23", "out": "s23-grew-up-side-by-side.jpeg", "seg": "n10",
        "window": "99.217-107.657", "wide": True,
        "locks": ["FIELD", "DARNEL"],
        "narration": "All season long the wheat and the weeds grew up side by side, and he let them, because his patience was protecting the crop he loved.",
        "must_show": "the whole field at the height of the season, tall and heavy, wheat ears and dark darnel spikes standing mixed together right across it under a hard bright sky.",
        "must_not_show": "no person anywhere in the frame; no night, no lamp, no sunset colouring; no cut, trampled or cleared ground; no building.",
        "scene": (
            "One photograph, 28mm lens, hard bright midday sunlight from high above, "
            "short shadows, a pale washed-out blue sky, fine film grain. THE CAMERA "
            "STANDS LOW AT THE GAP IN THE WALL, BEHIND THE WALL LINE AND SHOOTING "
            "PAST IT FROM THE SIDE DOWN THE LENGTH OF THE FIELD, "
            "with no person anywhere in the picture. The crop stands chest-high and "
            "heavy and fills the whole lower two thirds of the frame, half green and "
            "half turned to gold, and FAT UPRIGHT PALE-GOLD WHEAT EARS and THIN DARK "
            "GREY-GREEN RAGGED DARNEL SPIKES are mixed evenly through one another all "
            "the way to the far end, with no patch that is only one kind. The low "
            "dry-laid limestone wall runs off to the left, the lone carob tree stands "
            "at the far right corner, the ground lifts to the pale limestone rise and "
            "the low tawny bare hills close the horizon."
        ),
    },
    # ==================================================== HARVEST — verse 30 ====
    {
        "id": "v2-r025-b24", "out": "s24-bind-them-in-bundles.jpeg", "seg": "j30",
        "window": "107.657-115.435", "wide": True,
        "locks": ["FIELD-HANDS", "SERVANT", "FIELD", "DARNEL", "BARN"],
        "narration": "Gather ye together first the tares, and bind them in bundles to burn them: but gather the wheat into my barn.",
        "must_show": "the reapers at work in the ripe field, dark darnel already tied into bundles and stacked apart on the cut stubble, cut wheat sheaves going the other way toward the stone granary.",
        "must_not_show": "no cream, off-white or pale garment on anyone in the frame; no night, no lamp, no sunset colouring; no fire yet; nobody advancing into the camera and no face turned toward the lens.",
        "scene": (
            "One photograph, 28mm lens, warm late-afternoon sunlight from the left, "
            "long raking shadows across the stubble, fine film grain. THE CAMERA "
            "STANDS BEHIND THE NEAREST REAPER AND SHOOTS PAST HIM ACROSS THE CUT "
            "GROUND: his back and one shoulder fill the near left of the frame, out of "
            "focus, bent over his work in DEEP INDIGO wool, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. Sharp in the middle distance the ripe gold field is half "
            "cut. On the near right, exactly FOUR tied bundles of THIN DARK GREY-GREEN "
            "RAGGED DARNEL stand stacked together on the stubble, each one separate "
            "and countable, bound with twisted flax cord. Away to the left three other "
            "reapers in DARK OLIVE-DRAB, RUSSET-RED and DARK UMBER wool work in "
            "profile with hand-forged iron sickles among the standing gold wheat, and "
            "one of them carries a cut sheaf on his shoulder toward a plain dry-laid "
            "limestone granary with a flat mud-and-timber roof standing beyond the "
            "wall. The lone carob tree is at the far right corner and the low tawny "
            "hills close the horizon."
        ),
    },
    {
        "id": "v2-r025-b25", "out": "s25-easy-to-tell-apart.jpeg", "seg": "n11",
        "window": "115.435-119.795",
        "locks": ["FIELD", "DARNEL"],
        "narration": "Then harvest came. And at harvest, the two are finally easy to tell apart.",
        "must_show": "a close photograph of two cut handfuls laid side by side on the stubble — one of fat ripe pale-gold wheat ears, one of thin dark ragged darnel spikes — obviously different.",
        "must_not_show": "no person's face in the frame; no night, no lamp; no mixing of the two handfuls, they are laid clearly apart; no flowers or broadleaf weeds.",
        "scene": (
            "One photograph, 100mm lens, shallow depth of field, warm late-afternoon "
            "sunlight raking in from the left, fine film grain. THE CAMERA LOOKS DOWN "
            "ONTO THE CUT STUBBLE FROM JUST ABOVE IT; no face appears in the picture. "
            "Laid on the pale cut stubble, sharp and fully in focus, are TWO separate "
            "cut handfuls a hand's width apart and not touching: on the left a bound "
            "handful of FAT UPRIGHT PALE-GOLD WHEAT EARS, plump and heavy with stiff "
            "whiskers catching the low light; on the right a bound handful of THIN "
            "DARK GREY-GREEN RAGGED DARNEL SPIKES, lean and splayed and dull. The "
            "difference in colour, thickness and weight between the two is obvious. "
            "The cut field falls away out of focus behind them into warm gold."
        ),
    },
    {
        "id": "v2-r025-b26", "out": "s26-gathered-into-the-barn.jpeg", "seg": "n11",
        "window": "119.795-126.596", "wide": True,
        "locks": ["FIELD-HANDS", "FARMER", "BARN", "FIELD"],
        "narration": "The reapers gathered the weeds and bundled them away, and then gathered all the good wheat safely into the barn.",
        "must_show": "reapers carrying cut wheat sheaves in through the low doorway of the stone granary while a small fire of tied darnel bundles burns down well away from them at the field's edge.",
        "must_not_show": "no cream, off-white or pale garment on anyone in the frame; no night, no lamp, no sunset colouring; no fire near the granary or near the standing crop; nobody advancing into the camera and no face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, warm late-afternoon sunlight from the left, "
            "long raking shadows, fine film grain. THE CAMERA STANDS BEHIND THE MEN "
            "AND SHOOTS PAST THEM TOWARD THE GRANARY DOORWAY: the nearest reaper is "
            "seen entirely from behind, a cut sheaf of gold wheat balanced on his "
            "right shoulder in DEEP INDIGO wool, and NOT ONE FACE IS TURNED TOWARD THE "
            "LENS. Ahead of him a second reaper in RUSSET-RED is already stooping "
            "through the low plank-closed doorway of a plain dry-laid limestone "
            "granary with a flat mud-and-timber roof of hewn poles and packed earth, "
            "coiled fibre baskets and clay storage jars standing beside the door. To "
            "the right, standing beside the doorway watching the grain go in, the "
            "farmer is seen in profile — a thickset man of about forty-five with a "
            "full square DARK BROWN beard greying along the jaw, in a DEEP UMBER-BROWN "
            "tunic with a slate-grey mantle — his face turned toward the sheaf and not "
            "toward the camera. Far away at the left edge of the frame, small and well "
            "clear of everyone, a low open fire of wood and tied darnel bundles burns "
            "down on bare cut stubble with a thin column of pale smoke rising straight "
            "up. The cut gold field and the low tawny hills lie beyond."
        ),
    },
    {
        "id": "v2-r025-b27", "out": "s27-nothing-good-was-lost.jpeg", "seg": "n12",
        "window": "126.596-132.742",
        "locks": ["BARN"],
        "narration": "Nothing good was lost. Everything the farmer had waited and hoped for came safely home.",
        "must_show": "the inside of the granary doorway with the harvested grain heaped deep and gold in the coiled fibre baskets and clay jars, warm light falling in through the low door.",
        "must_not_show": "no person in the frame; no lamp, candle, glass or lantern of any kind; no night; no spillage or damage; no cream or off-white cloth anywhere.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, the only light a warm "
            "late-afternoon shaft falling in through the low open doorway from the "
            "left and pooling on the grain, the corners of the store dropping to soft "
            "brown shadow, fine film grain. THE CAMERA STANDS JUST INSIDE THE DOORWAY "
            "LOOKING IN AT THE STORED GRAIN; there is no person anywhere in the "
            "picture. Sharp in the light stand THREE large round coiled plant-fibre "
            "baskets heaped to the brim with clean pale-gold threshed wheat grain, "
            "each grain separate where the light hits, and beside them two "
            "hand-thrown clay storage jars with their shoulders catching the same "
            "light. The rough dry-laid limestone wall and the hewn poles of the flat "
            "roof are behind them in shadow. A few loose grains lie on the packed "
            "earth floor in the shaft of light."
        ),
    },
    # ============================ BACK TO THE FRAME — the threshing floor ====
    {
        "id": "v2-r025-b28", "out": "s28-that-is-how-god-works.jpeg", "seg": "n13",
        "window": "132.742-137.892", "wide": True, "jesus": True, "ref": REF,
        "locks": ["THRESHING-FLOOR", "LISTENERS"],
        "narration": "Jesus said that is how God works with the world. He is not quick to rip things up.",
        "must_show": "Jesus on the threshing floor bringing the parable home to the listeners around him in warm late-afternoon light.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no sunset colouring; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sunlight raking in "
            "from the left across the swept floor, long soft shadows, fine film grain. "
            "THE CAMERA STANDS BESIDE THE SEATED LISTENERS AND SHOOTS ACROSS THE FLOOR "
            "FROM THE SIDE, so every eyeline in the picture runs horizontally across "
            "the frame and NOT ONE FACE IS TURNED TOWARD THE LENS. On the right, "
            "sharp, Jesus sits on the low stone kerb turned three-quarters away from "
            "the camera toward the people, one hand open and low as he speaks, his "
            "gaze travelling left across the frame to an older man seated on the "
            "packed floor. On the left, filling the near frame in soft focus, are the "
            "backs and shoulders of the seated villagers in DEEP INDIGO, RUSSET-RED "
            "and DARK UMBER wool, a woman's DARK MADDER-RED head cloth nearest the "
            "camera, all of them facing him. A round coiled-fibre basket tipped on its "
            "side sits on the kerb between them. Behind him the grain plain and the "
            "low tawny hills open out."
        ),
    },
    {
        "id": "v2-r025-b29", "out": "s29-his-patience-is-mercy.jpeg", "seg": "n13",
        "window": "137.892-143.068", "jesus": True, "ref": REF,
        "locks": ["THRESHING-FLOOR"],
        "narration": "He gives time, because his patience is mercy. And in the end,",
        "must_show": "a close photograph of Jesus on the kerb of the threshing floor, unhurried and warm, letting the thought land.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no sunset colouring; no second figure in cream or off-white anywhere; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, very shallow depth of field, warm low "
            "late-afternoon sunlight from the left modelling one side of his face "
            "while the shaded side stays open and readable, fine film grain. THE "
            "CAMERA SITS AT EYE LEVEL WELL TO HIS LEFT SO HIS EYELINE RUNS "
            "HORIZONTALLY ACROSS THE FRAME AND OUT THROUGH THE LEFT EDGE toward the "
            "people he is teaching, and never toward the lens. He is framed from the "
            "chest up, seated on the low stone kerb and turned three-quarters away "
            "from the camera, his hands loose and open in his lap, his head tilted a "
            "little and his expression quiet and unhurried, holding the pause. The "
            "near foreground between the camera and him is nothing but the empty swept "
            "surface of the floor, with nobody standing or passing between them. The "
            "threshing floor, a tipped fibre basket and the pale grain plain fall away "
            "behind him into soft warm blur."
        ),
    },
    {
        "id": "v2-r025-b30", "out": "s30-shine-forth-as-the-sun.jpeg", "seg": "j2",
        "window": "143.068-146.738", "wide": True,
        "locks": ["FIELD"],
        "narration": "Then shall the righteous shine forth as the sun in the kingdom of their Father.",
        "must_show": "the harvested field blazing pale gold under a high clear sun, clean and bright and entirely free of the dark weed.",
        "must_not_show": "no person anywhere in the frame; no dark ragged darnel spikes anywhere, the field is clean wheat only; no night, no lamp, no sunset or sunrise colouring; no fire, no smoke.",
        "scene": (
            "One photograph, 35mm lens, brilliant high clear sunlight almost behind "
            "the crop so the ears are lit through and burn pale gold, a clean pale "
            "blue sky, fine film grain. THE CAMERA IS DOWN AMONG THE EARS LOOKING "
            "UPWARD AND ACROSS THE FIELD, with no person anywhere in the picture. FAT "
            "UPRIGHT PALE-GOLD WHEAT EARS fill the frame from bottom to top, sharp in "
            "the near middle and blurring into a broad field of light behind, every "
            "one of them a clean wheat ear and not one thin dark ragged spike anywhere "
            "among them. Beyond and above, the lone carob tree stands at the far right "
            "corner, the pale limestone rise lifts at the far end and the low tawny "
            "hills close the horizon under the bright sky."
        ),
    },
    {
        "id": "v2-r025-b31", "out": "s31-who-hath-ears-to-hear.jpeg", "seg": "j2",
        "window": "146.738-150.350",
        "locks": ["THRESHING-FLOOR", "LISTENERS"],
        "narration": "Who hath ears to hear, let him hear.",
        "must_show": "a close photograph of three listeners on the threshing floor caught in the moment of understanding, their eyes on the speaker.",
        "must_not_show": "no cream, off-white or pale garment on anyone in the frame; no night, no lamp, no sunset colouring; nobody's pupils centred on the lens; no more than three people.",
        "scene": (
            "One photograph, 85mm lens, very shallow depth of field, warm low "
            "late-afternoon sunlight from the right, fine film grain. THE CAMERA IS "
            "SIDE-ON TO THEM AT SEATED EYE LEVEL SO EVERY EYELINE RUNS HORIZONTALLY "
            "ACROSS THE FRAME AND OUT THROUGH THE RIGHT EDGE toward the man speaking, "
            "and nobody's pupils are anywhere near the lens. Exactly THREE people are "
            "in the picture and no fourth: sharp in the middle a woman of about thirty "
            "in RUSSET-RED wool with a DARK MADDER-RED head cloth, her lips just "
            "parted and her eyes bright with recognition; beside her at the left an "
            "older man in DEEP INDIGO with a grey beard, his chin lifted; behind them "
            "at the right a boy of about ten in plain DARK BROWN, leaning forward past "
            "the woman's shoulder. All three are seated on the packed floor at the "
            "stone kerb and all three look the same way across the frame. The swept "
            "threshing floor and the pale grain plain blur away behind them."
        ),
    },
    {
        "id": "v2-r025-b32", "out": "s32-will-shine-like-the-sun.jpeg", "seg": "n14",
        "window": "150.350-154.940",
        "locks": ["FARMER", "BARN"],
        "narration": "The people who belong to him will shine like the sun. That is how good he is.",
        "must_show": "the farmer standing in his granary doorway at the end of harvest with both hands buried in the heaped gold grain, quietly glad.",
        "must_not_show": "no other person in the frame; no night, no lamp, no candle, no glass, no lantern; no cream, off-white or pale garment on him; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, a warm late-afternoon "
            "shaft of sunlight coming in through the doorway from the right and "
            "falling across the grain and the lower half of his face, the store behind "
            "him dropping to soft brown shadow, fine film grain. THE CAMERA IS INSIDE "
            "THE STORE AT CHEST HEIGHT AND WELL TO HIS RIGHT, SO HIS EYELINE RUNS "
            "STEEPLY DOWNWARD INTO THE GRAIN IN HIS OWN HANDS, well below the lens. He "
            "is framed from the waist up, alone: a thickset sun-browned man of about "
            "forty-five with a full square DARK BROWN beard greying along the jaw and "
            "dark brown hair pushed back off a high forehead, in a DEEP UMBER-BROWN "
            "coarse wool tunic with a dark ochre sash and a slate-grey mantle over his "
            "left shoulder. Both hands are sunk to the wrist in a coiled fibre basket "
            "heaped with clean pale-gold threshed grain, lifting a double handful so "
            "the grains spill between his fingers, each falling grain separate in the "
            "light. His eyes are lowered to the grain and his mouth is soft with "
            "relief. He is the only person in the picture and the rough limestone wall "
            "of the store is behind him."
        ),
    },
    {
        "id": "v2-r025-b33", "out": "s33-patient-enough-to-wait-for-you.jpeg", "seg": "n14",
        "window": "154.940-160.858", "jesus": True, "ref": REF,
        "locks": ["THRESHING-FLOOR", "LISTENERS"],
        "narration": "He is patient enough to wait for you, and he will not let one good stalk be lost.",
        "must_show": "Jesus on the threshing floor at the close, looking steadily at one man seated in front of him, warm and unhurried.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no sunset colouring; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, warm low "
            "late-afternoon sunlight from the left, long soft shadows across the swept "
            "floor, fine film grain. THE CAMERA SHOOTS OVER THE SHOULDER OF A SEATED "
            "LISTENER, whose DARK UMBER back and head fill the near right of the frame "
            "out of focus, SO THAT JESUS'S GAZE HAS A NAMED TARGET INSIDE THE PICTURE "
            "— he is looking directly at that seated man, not at the lens, and his "
            "eyeline runs across the frame to the right. Sharp in the middle, Jesus "
            "sits forward on the low stone kerb with his forearms on his knees and his "
            "hands loosely clasped, his head slightly inclined toward the man, his "
            "expression warm, steady and unhurried. Behind him the kerb, a wooden "
            "winnowing fork leaning against it, the swept floor and the pale grain "
            "plain fall away into soft warm blur under the low tawny hills."
        ),
    },
]
