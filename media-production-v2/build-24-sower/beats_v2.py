#!/usr/bin/env python3
"""V2 beat map — row 24, build-24-sower (Matthew 13:1-9, 18-23), realistic.

COVERAGE: 35 pictures against V1's EIGHT, over 160.94 s of story = 4.60 s/picture.
V1 held `s6-good-harvest.jpeg` on screen from 87.37 s to 132.21 s — FORTY-FOUR
SECONDS on one picture across FOUR segments (j8, n9, j3, n10), swallowing the whole
good-ground half of the parable including Jesus's own fifteen-second explanation.
`s3-wayside-birds.jpeg` held another 25 s across j4, n4 and n5. Eight pictures for a
2:48 video is one still every twenty-one seconds.

⚠️ WINDOWS COMPUTED FROM SCRATCH 2026-08-02 with the fixed `extract_beats.py`
reading the V1 build, then split inside each segment on that segment's own
`audio/*.timing.json` phrase boundaries (mid-phrase splits only where a phrase runs
longer than ~9 s). Contiguous 0.28 s → 161.223 s (the card start), zero gaps, zero
overlaps. Extracted total 167.549 s against the V1 mp4's 167.600 s. The INHERITED
25-beat map dated 2026-07-29 that was in this file was DISCARDED, not re-timed: it
ran on a 140.8 s timeline against the real 167.5 s, adrift by nearly twenty-seven
seconds by the end of the story.

⚠️ SOURCING TRAP CHECKED AND CLEARED. This build carries `make_narration.py.pre-speaker`
and `build.py.pre-speaker`, and the live script and the sibling DO disagree: the
SPEAKER-LAW rebuild ADDED three segments the sibling has never heard of (s3 = the
black-letter frame of Matthew 13:3, j4 = Matthew 13:4, j8 = Matthew 13:8) and all
three mp3s exist in `audio/`. Six segments (n1, n3, n8, n11, n12, card) were
transcribed with faster-whisper and every one matches the LIVE script word for word.
The live script is authoritative and NO `TEXT_OVERRIDES` are needed on this row.

SCRIPTURE FACTS (Matthew 13 KJV):
  v1-2  "the same day went Jesus out of the house, and sat by the SEA SIDE ... great
        multitudes were gathered together unto him, so that HE WENT INTO A SHIP, and
        sat; and the whole multitude STOOD ON THE SHORE." Daylight, not night.
  v3    "And he spake many things unto them in parables, saying, Behold, a sower went
        forth to sow;" — the words before "Behold" are Matthew writing, not Jesus, so
        they are the light-blue SCRIPTURE segment s3 and j1 is red.
  v4    "some seeds fell BY THE WAY SIDE, and the FOWLS came and devoured them up."
  v5-6  "STONY PLACES, where they had NOT MUCH EARTH ... they had NO DEEPNESS OF
        EARTH ... when the sun was up, they were SCORCHED; and because they had no
        root, they WITHERED AWAY." Thin soil over a shelf of rock, not a boulder field.
  v7    "among THORNS; and the thorns SPRUNG UP, AND CHOKED THEM."
  v8    "GOOD GROUND, and brought forth fruit, some an hundredfold, some sixtyfold,
        some thirtyfold."
  v9    "Who hath ears to hear, let him hear."
  v23   the good ground is "he that heareth the word, and UNDERSTANDETH IT."

WHY-LAW (from the V1 narration script, kept): the farmer did not skip the hard path
or the rocky places. He threw seed everywhere, on every heart, hoping. And ground
can change — a hard path can be broken up, rocky soil can be cleared.

STAGING ACROSS THE LIBRARY — this row must not repeat a composition already used:
  rows 2, 8, 21 (Luke 15)     outdoor courtyard table / low wall under a fig tree /
                              inside a village house at a crowded meal
  row 16 (Mary & Martha)      a lamplit evening interior
  row 22 (unmerciful servant) a black basalt Capernaum doorstep and street
  row 23 (vineyard workers)   a terraced hillside above a vineyard
  row 11 (the storm)          an open boat at NIGHT in a gale
  row 19 (breakfast on shore) a Galilee beach at FIRST LIGHT with a charcoal fire
So this frame story is staged exactly where Matthew 13:1-2 puts it and nowhere else
in the library: a MOORED FISHING BOAT LYING JUST OFF A SHINGLE BEACH IN BRIGHT LATE
MORNING, Jesus seated on its stern thwart with the water between him and the crowd,
and the crowd banked up the natural slope of the shore. The daylight and the still
water are what separate it from row 11's night gale and row 19's dawn.

TIME OF DAY AND GROWING SEASON — this row needed a rule row 23's did not.
Row 23 pinned the SEASON globally because one location was revisited across one day.
Here the parable spans a whole growing season on ONE field, so a global season lock
would be a lie. THE RULE THIS ROW ESTABLISHES: pin the TERRAIN as the invariant and
let each beat state its own GROWTH STAGE. The field's path, rock shelf, thorn brake
and dark tilled corner are identical in every frame; what changes is only whether the
ground is bare, sprouting, or in ripe barley.
  b01-b04, b12, b24-b25, b27, b32   THE FRAME — bright late morning on the lake, high
                               sun, hard sparkle on flat water, crisp short shadows.
  b05-b11, b29-b31             SOWING — the same clear morning light on bare, freshly
                               broken earth; no crop anywhere yet.
  b14-b19                      SPRINGING UP then FAILING — b14/b18 morning, b15 hard
                               white overhead noon because verse 6 says the sun was
                               up and scorched them.
  b20-b23, b26, b28            GOOD GROUND — b20/b22 the same sowing morning on dark
                               earth, b21/b23/b26/b28 later in the season in ripe gold
                               barley and cut stubble.
  b33-b35                      THE GROUND CHANGING — warm low late-afternoon light,
                               the only late light in the row, so the hope at the end
                               reads as a different day from the sowing.
No sunset palette anywhere, no night anywhere, no lamp anywhere in this row.

CAST NOTE — ANCHOR-FIRST (the row-20/21/22/23 lesson that holds the reroll rate at
10-15%). THREE story beats are also the identity ANCHORS and are generated in their
OWN run before anything else, each composed so its character's face is large, lit and
alone in the frame:
  b05  the SOWER, stepping out of the field gate with the seed bag
  b16  the YOUNG MAN on the shore, lit up with joy
  b25  the WOMAN on the shore, understanding what she is hearing
Each accepted anchor is wired into REFS below so every later frame naming that lock
gets the image attached. `v2_gen_api` builds its REFS cache ONCE per run, so an anchor
generated in the same run as its dependants does not exist yet when they are built —
it MUST be a separate invocation.

A FACE SHEET ALONE DOES NOT HOLD A CHARACTER WHO IS SMALL IN FRAME (rows 19, 22, 23).
So every lock below states age, build, hair and beard as explicit invariants, and each
beat that names a locked person also restates that person POSITIVELY in its own scene
text.

CREAM: only Jesus. The sower is a prosperous-enough farmer and the obvious drift is to
put him in pale undyed linen, which reads as a second unlocked Jesus, so he is pinned
to DEEP UMBER-BROWN. The phrase "undyed grey-brown wool" is deliberately NOT used
anywhere in this file — on row 21 it rendered near-white every time.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks NEVER name a
# character. Clothing colours are stated POSITIVELY and DARK.
LOCKS = {
    # ------------------------------------------------------------- people ----
    "SOWER": (
        "SOWER LOCK: the farmer who goes out to sow is the SAME man in every shot "
        "and these are invariants that hold even when he is small, distant, in "
        "shadow or out of focus — a man of about forty, of medium height and lean "
        "hard build with heavy forearms and a corded neck, sun-blackened "
        "olive-brown skin, a broad square face with a blunt nose, a deep weathered "
        "line across his brow and calm dark brown eyes, a DENSE BLACK BEARD grown "
        "out to two fingers' depth and streaked with grey at the chin, and thick "
        "BLACK HAIR to the tops of his ears bound off his forehead with a strip of "
        "dark russet cloth — never cropped short, never shaved at the sides, never "
        "a modern haircut. He wears a knee-length work tunic of DEEP UMBER-BROWN "
        "wool, faded and sweat-darkened between the shoulders, a twisted rope belt, "
        "a wide strip of dark charcoal cloth wound over one shoulder and across his "
        "chest to carry a heavy hand-woven fibre seed bag at his hip, and thin dark "
        "leather sandals. Nothing he wears is cream, off-white, pale, bleached or "
        "linen-white. His hands are a working farmer's hands, thick and cracked "
        "across the knuckles. He is a decent, unhurried, generous man at his work; "
        "he is never grim, never comic, never a beggar and never a hired servant."
    ),
    "YOUNGMAN": (
        "YOUNG MAN LOCK: the young listener on the shore is the SAME person in "
        "every shot and these are invariants that hold even when he is small, "
        "distant or out of focus — about nineteen, slight and narrow-shouldered, "
        "warm olive-brown skin, a smooth open face with round cheeks, a straight "
        "nose and large dark brown eyes, only the FIRST THIN DARK BEARD along his "
        "jaw and upper lip, and dark brown wavy hair to the jaw pushed back behind "
        "his ears with no head covering at all. He wears a knee-length tunic of "
        "DARK INDIGO wool with a plain cord at the waist and bare dusty feet. "
        "Nothing he wears is cream, off-white, pale or bleached. He is an ordinary "
        "eager Galilean village boy, never a beggar, never sly and never comic."
    ),
    "WOMAN": (
        "WOMAN LOCK: the woman listening from the shore is the SAME person in every "
        "shot and these are invariants that hold even when she is small, distant or "
        "out of focus — about thirty-five, of ordinary build, weathered warm "
        "olive-brown skin, a long oval face with high cheekbones, a strong straight "
        "nose and steady dark brown eyes with fine lines at their corners, and dark "
        "brown hair entirely covered by a wound headcloth of DEEP RUSSET wool that "
        "falls over her shoulders. She wears an ankle-length robe of DARK OCHRE "
        "wool with a woven CHARCOAL sash. Nothing she wears is cream, off-white, "
        "pale or bleached. She is a working village woman with a quiet, intelligent, "
        "unguarded face; she is never glamorous, never sorrowful for its own sake "
        "and never posed."
    ),
    "HARDMAN": (
        "HARD-FACED MAN LOCK: the older listener standing apart at the back of the "
        "crowd is a man of about sixty, heavy-set and thick through the chest, "
        "sun-darkened olive-brown skin, a wide jowled face with deep brackets "
        "around a downturned mouth, hooded dark eyes under heavy brows, a broad "
        "IRON-GREY BEARD spread over his chest and grey hair covered by a wound "
        "headcloth of CHARCOAL wool. He wears an ankle-length robe of very DARK "
        "OLIVE-BROWN wool with a dark leather belt. Nothing he wears is cream, "
        "off-white, pale or bleached. His face is closed and unmoved rather than "
        "angry or cruel — a man who has already decided he has heard this before."
    ),
    "CROWD": (
        "SHORE CROWD LOCK: the multitude on the beach are ordinary first-century "
        "Galilean villagers and fishermen between about twelve and seventy — men "
        "with dark beards and wound headcloths, women with their hair covered by "
        "headcloths, and a few barefoot children. Their skin is weathered "
        "olive-brown and every face is distinct; no two are the same face. Their "
        "clothing is DEEP INDIGO, DARK UMBER, DEEP RUSSET, DARK OCHRE, CHARCOAL "
        "BROWN and DARK OLIVE — every single one of them dark, and NOT ONE of them "
        "in cream, off-white, pale, bleached or linen-white cloth of any kind, "
        "including at the blurred edges of the frame, because a pale garment on the "
        "shore reads as a second unlocked Jesus. They sit and stand and lean on the "
        "natural slope of the beach in loose uneven clusters, some on their heels, "
        "some with a child on a hip — never arranged in rows, never uniform, never "
        "presenting themselves to the camera."
    ),
    # ----------------------------------------------------------- settings ----
    "LAKESHORE": (
        "LAKESHORE SETTING LOCK: the north-west shore of the Sea of Galilee in the "
        "first century — a wide grey-brown shingle and coarse-sand beach strewn with "
        "smooth dark basalt cobbles, rising behind into a natural grassy slope of "
        "dry summer grass and scattered black basalt outcrops that forms a shallow "
        "bowl above the water. The lake itself is flat, wide and pale blue-green, "
        "with bare tawny hills low on the far shore. Along the beach lie hand-hewn "
        "timber drying racks, coils of twisted flax rope, hand-knotted fibre nets "
        "spread on the stones and fired-clay jars. Any building visible is a "
        "single-storey house of rough dark basalt blocks with a flat roof of packed "
        "mud over timber beams. The skyline holds only bare hills and flat village "
        "roofs: no dome, no spire, no minaret, no bell tower, no tiled roof, no "
        "pipe, no vent, no cable and no aerial. No surface anywhere carries readable "
        "lettering."
    ),
    "BOAT": (
        "BOAT LOCK: one small first-century Galilean fishing boat, about eight "
        "paces long, built of hand-adzed cedar and oak planks pegged with wooden "
        "treenails over sawn frames, the wood bare, silvered and weathered with the "
        "grain showing and the seams packed with dark pitch. It has a single low "
        "mast stepped forward with its sail furled and lashed down along the boom, "
        "a raised stern platform with a plank thwart across it, a steering oar "
        "hung over the quarter, twisted flax mooring rope, hand-knotted fibre nets "
        "heaped in the bottom, and a fired-clay water jar wedged against a frame. "
        "The hull is never painted, never varnished, never white and never "
        "fibreglass; there is no metal fitting, cleat, screw, hinge or chain "
        "anywhere on it, and no engine, motor or propeller. It floats upright in "
        "shallow clear water a few paces off the beach, its shadow visible on the "
        "pale stony bottom beneath it."
    ),
    "FIELD": (
        "FIELD SETTING LOCK: ONE single first-century Judean grain field on gently "
        "sloping ground, and it is THE SAME FIELD WITH THE SAME TERRAIN IN EVERY "
        "FRAME OF THIS STORY. Four kinds of ground are present in it and their "
        "positions never change: a hard-beaten FOOTPATH of pale packed earth, worn "
        "smooth and grey and printed with sandal marks, running across the near side "
        "of the field; a low SHELF OF EXPOSED PALE LIMESTONE breaking through the "
        "slope with only a finger's depth of thin stony soil skinned over it; a "
        "dense BRAKE OF THORNS along the field margin — grey-green woody thistle and "
        "spiny scrub with old dead canes standing among the new; and a broad corner "
        "of DEEP DARK RED-BROWN TILLED LOAM, freshly broken into clods, crumbly and "
        "open. Behind the field are dry-stone field walls of stacked pale limestone, "
        "bare tawny hills, and far off the flat mud-and-timber roofs of a small stone "
        "village — no tower, no dome, no spire, no minaret, no tiled roof, no fence "
        "of milled timber, no wire and no post of any modern kind. THE GROWTH STAGE "
        "OF THE CROP IS STATED SEPARATELY BY EACH SCENE AND IS THE ONLY THING THAT "
        "CHANGES; the path, the rock shelf, the thorn brake and the dark tilled "
        "corner are identical every time."
    ),
    "SEED": (
        "SEED LOCK: the grain is hand-threshed BARLEY — small, plump, pale "
        "gold-brown kernels with a visible crease, loose and dusty, never round "
        "peas, never beans, never modern uniform pellets. It is carried in a heavy "
        "hand-woven plant-fibre bag slung at the hip and thrown by the handful. "
        "When it is in the air it is a spreading arc of individually visible "
        "separated grains catching the light, never a solid stream, cloud, spray or "
        "smoke."
    ),
}

REF = True

OUTPUT_ASSET_DIR = "assets"

# REFS — wired in AFTER the three anchor beats (b05, b16, b25) are generated in their
# own run and pass QC. Until then these paths do not exist and v2_gen_api prints
# "character lock MISSING (skipped)" and carries on, which is exactly why the anchors
# must be generated first.
REFS = {
    "SOWER": "assets/s05-a-sower-went-forth.jpeg",
    "YOUNGMAN": "assets/s16-says-yes-with-joy.jpeg",
    "WOMAN": "assets/s25-and-understandeth-it.jpeg",
}

BEATS = [
    # ======================================= FRAME — the boat and the shore ====
    {
        "id": "v2-r024-b01", "out": "s01-so-many-people-crowded.jpeg", "seg": "n1",
        "window": "0.28-5.00", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CROWD", "LAKESHORE", "BOAT"],
        "narration": "So many people crowded the shore to hear Jesus that he pushed a small boat out onto the water",
        "must_show": "a large crowd packed right down to the water's edge on a stony Galilee beach in bright late morning, and beyond them the small wooden boat lying a few paces out in the shallows with Jesus aboard.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off Jesus; no night, no storm, no rough water, no sunset, no cooking fire, no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges, and nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, bright late-morning sunlight from high on the "
            "right, hard sparkle on flat water, crisp short shadows, fine film grain. "
            "THE CAMERA STANDS UP THE BEACH BEHIND THE CROWD AND SHOOTS PAST THEM "
            "TOWARD THE LAKE: the backs, shoulders and covered heads of the nearest "
            "villagers fill the whole bottom half of the frame, soft and out of focus, "
            "a deep indigo mantle at the near left and a dark umber back at the near "
            "right, and NOT ONE FACE IS TURNED TOWARD THE LENS. Every one of them "
            "faces away from the camera out over the water. Beyond them the ground "
            "falls to the waterline where the crowd stands ankle-deep in the shallows, "
            "pressed shoulder to shoulder along the edge. Sharp in the middle distance "
            "the weathered fishing boat lies broadside a few paces out, and Jesus sits "
            "on its stern thwart, small in the frame but plainly himself, his head "
            "turned to his left toward the far end of the crowd and his gaze travelling "
            "along the waterline inside the frame. Flat pale blue-green water fills the "
            "top of the picture with the low tawny far shore across it."
        ),
    },
    {
        "id": "v2-r024-b02", "out": "s02-taught-them-from-there.jpeg", "seg": "n1",
        "window": "5.00-9.542", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BOAT", "LAKESHORE"],
        "narration": "and taught them from there, the whole hillside listening.",
        "must_show": "Jesus seated on the stern thwart of the moored boat in bright daylight, mid-sentence, teaching across the water to the slope of people behind the camera's shoulder.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off Jesus; no night, no storm, no sunset, no standing on the water, no raised platform, no scroll or book, and Jesus never looks into the lens.",
        "scene": (
            "One photograph, 85mm prime lens at a wide aperture, shallow depth of "
            "field, bright late-morning sun from high on the right, fine film grain. "
            "The camera floats low and close to the water off the boat's shoreward "
            "quarter, near enough that the wet planking of the hull runs blurred across "
            "the bottom of the frame. Jesus sits on the plank thwart of the raised "
            "stern, leaning slightly forward with his forearms on his knees and his "
            "right hand lifted open at chest height mid-sentence, fingers loose. He is "
            "sharp; the furled sail and the heaped fibre nets behind him are soft. His "
            "head is turned three-quarters away from the camera to his left and his "
            "eyes are aimed up the beach past the camera's right shoulder and out of "
            "the frame, plainly fixed on people the viewer cannot see. Behind him the "
            "flat pale water and the low far hills are a soft bright band. No light "
            "of any kind comes off him."
        ),
    },
    {
        "id": "v2-r024-b03", "out": "s03-a-farmer-and-four-grounds.jpeg", "seg": "n2",
        "window": "9.542-14.669", "wide": True, "jesus": False,
        "locks": ["FIELD"],
        "narration": "And he told them a story about a farmer, and four kinds of ground.",
        "must_show": "one wide establishing photograph of the whole field with all four kinds of ground visible in it at once — the beaten footpath, the shelf of bare rock, the thorn brake and the dark tilled corner — with no crop growing anywhere yet.",
        "must_not_show": "no people at all, no animals, no crop, no green shoots, no ripe grain, no buildings close to the camera, no tower, no dome, no minaret, no tiled roof, no fence, no wire, and no lettering on anything.",
        "scene": (
            "One photograph, 28mm lens, clear late-morning sunlight from the right "
            "raking low enough to model the clods, deep focus front to back, fine film "
            "grain. The camera stands at ground level at the near edge of the field and "
            "looks across it up the gentle slope from behind the beaten path, with no "
            "person anywhere in the shot. The hard-beaten footpath of pale packed grey "
            "earth runs across the foreground from left to right, printed with sandal "
            "marks and swept smooth. Beyond it, left of centre, the low shelf of pale "
            "limestone breaks through the slope with a skin of thin stony soil over it. "
            "Along the right margin stands the dense grey-green brake of woody thorn "
            "and thistle with dead canes among the new. Filling the upper left is the "
            "broad corner of deep dark red-brown tilled loam, freshly broken into "
            "crumbling clods. The whole field is bare earth: nothing has been sown yet "
            "and nothing is growing. Dry-stone walls, tawny hills and a distant "
            "flat-roofed village close the top of the frame."
        ),
    },
    {
        "id": "v2-r024-b04", "out": "s04-he-spake-in-parables.jpeg", "seg": "s3",
        "window": "14.669-19.391", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BOAT", "LAKESHORE"],
        "narration": "And he spake many things unto them in parables, saying,",
        "must_show": "a close, warm photograph of Jesus in the boat at the moment he begins the parable, both hands opening outward, his attention entirely on the people ashore.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off Jesus; no night, no sunset, no scroll or book, no raised platform, no crowd faces in focus, and Jesus never looks into the lens.",
        "scene": (
            "One photograph, 105mm prime lens at a wide aperture, very shallow depth of "
            "field, bright late-morning sun from high on the right, fine film grain. A "
            "tight three-quarter shot of Jesus from his left side as he sits on the "
            "stern thwart. He has just begun to speak: both hands are opening outward "
            "and away from his chest, palms turning up, elbows still close to his "
            "sides. His face is calm and warm and completely unhurried, his chin "
            "slightly lifted, and his eyes are aimed past the left edge of the frame, "
            "steady on somebody standing on the beach outside the picture. His head is "
            "turned well off the camera axis and his pupils never come near the lens. "
            "Behind him the weathered hull rail, a coil of twisted flax rope and the "
            "bright flat water dissolve into soft blur. No light of any kind "
            "comes off him."
        ),
    },
    # ============================================== THE SOWER GOES OUT ========
    {
        "id": "v2-r024-b05", "out": "s05-a-sower-went-forth.jpeg", "seg": "j1",
        "window": "19.391-23.407", "wide": False, "jesus": False,
        "locks": ["SOWER", "FIELD", "SEED"],
        "narration": "Behold, a sower went forth to sow;",
        "must_show": "ANCHOR FRAME — the sower's face large, sharp and clearly lit as he steps through the gap in the field wall onto the bare field with the seed bag already at his hip and his hand going into it.",
        "must_not_show": "no other person anywhere in the frame, no crop, no green shoots, no ripe grain, no animal, no plough, no cream or off-white cloth on anyone, no tower, no dome, no minaret, no lettering, and he never looks into the lens.",
        "scene": (
            "One photograph, 50mm prime lens at a wide aperture, clear late-morning sun "
            "coming from the left and falling full and even across his face, shallow "
            "depth of field, fine film grain. The camera stands inside the field, low "
            "and close, level with his chest. The sower has just stepped through the "
            "gap in the dry-stone wall and stopped on the bare broken earth: a man of "
            "about forty, lean and hard, sun-blackened olive-brown skin, a dense black "
            "beard streaked with grey at the chin, thick black hair to the tops of his "
            "ears bound back with a strip of dark russet cloth, in a knee-length deep "
            "umber-brown work tunic with a twisted rope belt and a wide charcoal "
            "shoulder strap carrying the heavy woven fibre seed bag at his hip. His "
            "face fills the upper third of the frame, sharp and fully lit, weathered "
            "and calm and entirely absorbed in his work. His right hand is already "
            "buried in the mouth of the bag and pale gold-brown barley grain spills "
            "between his knuckles. His head is turned a little to his right and his "
            "eyes are down, fixed on the broken ground ahead of his own feet inside the "
            "frame. Behind him the wall, the bare slope and the distant hills fall into "
            "soft blur. He is alone."
        ),
    },
    {
        "id": "v2-r024-b06", "out": "s06-went-out-to-scatter.jpeg", "seg": "n3",
        "window": "23.407-28.168", "wide": True, "jesus": False,
        "locks": ["SOWER", "FIELD", "SEED"],
        "narration": "A farmer went out to scatter his seed. He did not measure it out grain by grain.",
        "must_show": "the sower walking out across the bare field at a steady working pace with his hand deep in the seed bag, seen from behind and to the side so the whole unsown field lies open in front of him.",
        "must_not_show": "no other person, no crop, no green shoots, no ripe grain, no animal, no plough, no measuring cup, bowl or scale of any kind, no cream or off-white cloth on anyone, and not one face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, clear late-morning sun from the right, crisp "
            "short shadows, deep focus, fine film grain. THE CAMERA STANDS BEHIND AND "
            "SLIGHTLY LEFT OF THE SOWER AND SHOOTS PAST HIM UP THE SLOPE: his back and "
            "the strap across his shoulders fill the near left of the frame in "
            "three-quarter from behind, and his face is not visible to the camera at "
            "all. The same locked man — about forty, lean and hard, deep umber-brown "
            "knee-length tunic, twisted rope belt, wide charcoal shoulder strap, black "
            "hair bound back with a strip of dark russet cloth — walks away from the "
            "camera to the right with his weight forward and his right arm buried to "
            "the wrist in the woven fibre bag at his hip, taking a full careless "
            "handful. His sandal has just come down on the beaten footpath and the dust "
            "is lifting off it. In front of him the whole bare field opens out: the "
            "grey packed path crossing away, the pale limestone shelf beyond it, the "
            "thorn brake along the right margin and the dark tilled corner at the top "
            "left. Nothing is growing anywhere."
        ),
    },
    {
        "id": "v2-r024-b07", "out": "s07-he-flung-it-wide.jpeg", "seg": "n3",
        "window": "28.168-33.680", "wide": False, "jesus": False,
        "locks": ["SOWER", "FIELD", "SEED"],
        "narration": "He flung it wide, across every kind of ground, hoping all of it would grow.",
        "must_show": "the throw itself caught mid-action — the sower's arm swung out across his body and a wide spreading arc of separate barley grains hanging in the air over the bare ground.",
        "must_not_show": "no other person, no crop, no green shoots, no ripe grain, no animal, no cream or off-white cloth on anyone, and the grain in the air is never a solid stream, cloud, spray or puff of smoke, and he never looks into the lens.",
        "scene": (
            "One photograph, 50mm lens, fast shutter freezing the grain in flight, "
            "clear late-morning sun low from the right and backlighting the throw, "
            "shallow depth of field, fine film grain. The camera stands side-on to the "
            "sower at waist height, three or four paces away, so his whole action runs "
            "flat across the frame from left to right and he is seen in profile. The "
            "same locked man — lean, about forty, dense black beard streaked with grey, "
            "black hair bound back with dark russet cloth, deep umber-brown tunic, "
            "charcoal shoulder strap, woven fibre bag at his hip — is caught at the end "
            "of the throw: his right arm swung all the way out and across his body, "
            "fingers open and empty, his shoulders turned, his left foot forward and "
            "his weight already moving into the next step. His head is turned to follow "
            "the throw and his eyes are fixed on the ground away to the right inside "
            "the frame. A wide spreading fan of individually visible pale gold-brown "
            "barley grains hangs in the air in front of him, each one separate and lit "
            "against the shadowed slope, falling across the bare packed path in the "
            "foreground and the broken earth beyond it."
        ),
    },
    # =============================================== THE WAY SIDE =============
    {
        "id": "v2-r024-b08", "out": "s08-fell-by-the-way-side.jpeg", "seg": "j4",
        "window": "33.680-37.700", "wide": False, "jesus": False,
        "locks": ["FIELD", "SEED"],
        "narration": "And when he sowed, some seeds fell by the way side,",
        "must_show": "a very close, low photograph of scattered barley grains lying loose ON TOP of the hard-beaten footpath, resting on the surface with nothing covering them.",
        "must_not_show": "no person, no bird yet, no crop, no green shoots, no soft or broken earth under the grain, no seed buried or half-buried, no cream or off-white cloth, and no lettering.",
        "scene": (
            "One photograph, 100mm macro lens close to the ground, clear late-morning "
            "sun from the right throwing a tiny hard shadow beside every grain, very "
            "shallow depth of field, fine film grain. The camera lies almost on the "
            "path itself, a hand's breadth above it, looking along the surface so the "
            "packed earth runs away into blur at the top of the frame. The path is pale "
            "grey-brown, beaten iron-hard and polished smooth by feet, printed with the "
            "overlapping marks of sandals and bare toes, cracked in a fine web and "
            "dusted with powder. Perhaps fifteen pale gold-brown barley grains lie "
            "scattered across it, each one separate and countable, sitting entirely on "
            "top of the surface with not one of them sunk in or covered. Two grains "
            "have rolled into a sandal print and stopped there. In the soft distance "
            "the thin dark line of the thorn brake and the pale limestone shelf are "
            "just readable."
        ),
    },
    {
        "id": "v2-r024-b09", "out": "s09-the-fowls-devoured-them.jpeg", "seg": "j4",
        "window": "37.700-41.746", "wide": False, "jesus": False,
        "locks": ["FIELD", "SEED"],
        "narration": "and the fowls came and devoured them up:",
        "must_show": "wild birds down on the footpath actually taking the grain — one bird's beak striking the ground mid-peck, another braking in to land with its wings spread.",
        "must_not_show": "no person, no crop, no green shoots, no scarecrow, no cage, no tame or ornamental bird, no bird of prey, no cream or off-white cloth, and no bird looking into the lens.",
        "scene": (
            "One photograph, 200mm telephoto lens from low and far off, fast shutter "
            "freezing the wings, clear late-morning sun from the right, shallow depth "
            "of field, fine film grain. The camera lies flat on the ground well along "
            "the path so the birds are seen level and side-on, running away from the "
            "lens down the beaten track. Six small wild brown-grey birds — plain "
            "sparrows and larks of the Judean fields, dust-coloured and streaked, all "
            "of them countable — are working the path where the barley fell. The "
            "nearest is sharp and side-on with its beak already down against the packed "
            "earth and a single grain caught in it, its tail cocked; behind it another "
            "is braking in to land with both wings spread wide and its feet reaching "
            "forward; two more are already pecking further up the path and two are "
            "blurred in the air above. The path behind them is swept bare and there is "
            "not one grain left where the nearest bird has already passed."
        ),
    },
    {
        "id": "v2-r024-b10", "out": "s10-packed-down-by-every-foot.jpeg", "seg": "n4",
        "window": "41.746-46.345", "wide": False, "jesus": False,
        "locks": ["FIELD"],
        "narration": "Some fell on the hard path, packed down by every foot that had ever walked it.",
        "must_show": "the hardness of the path itself as the subject — a long low view of the beaten track running away across the field, its surface polished, cracked and printed with countless overlapping footprints.",
        "must_not_show": "no person in the frame, no bird, no crop, no green shoots, no seed visible, no cart, no wheel rut of any modern kind, no cream or off-white cloth, and no lettering.",
        "scene": (
            "One photograph, 35mm lens held a hand's height above the ground, clear "
            "late-morning sun raking low from the right so every ridge and print throws "
            "a long hard shadow, deep focus, fine film grain. The camera sits on the "
            "path looking straight along it as it runs away up the slope and out of the "
            "frame at the top. There is no person anywhere in the shot. The track is "
            "pale grey and beaten to the hardness of stone, its surface glazed and "
            "faintly shining where feet have polished it, webbed all over with fine dry "
            "cracks, and crowded with the overlapping prints of bare feet and sandal "
            "soles laid one across another until none of them is separate any more. At "
            "the edges of the track the earth lifts into a low crumbling lip where the "
            "soft field begins, and the difference between the iron-hard path and the "
            "broken soil beside it is the whole subject of the picture. Beyond, the "
            "bare field, the dry-stone wall and the tawny hills."
        ),
    },
    {
        "id": "v2-r024-b11", "out": "s11-it-never-sank-in.jpeg", "seg": "n4",
        "window": "46.345-51.366", "wide": False, "jesus": False,
        "locks": ["FIELD", "SEED"],
        "narration": "It never sank in, and the birds came and ate it.",
        "must_show": "the aftermath on the path — the birds lifting away and the beaten track left completely clean, with only two or three last grains at the very edge of the frame.",
        "must_not_show": "no person, no crop, no green shoots, no nest, no dead bird, no scarecrow, no cream or off-white cloth, and no bird facing the lens.",
        "scene": (
            "One photograph, 85mm lens from low and to the side, clear late-morning sun "
            "from the right, shallow depth of field, fine film grain. The camera lies "
            "low beside the path looking across it. Four small dust-coloured wild birds "
            "are lifting away together, all of them going left and away from the "
            "camera, wings mid-beat and feet still trailing, their heads turned toward "
            "the far side of the field and not one of them toward the lens. Below them "
            "the beaten path runs across the frame swept absolutely clean — polished, "
            "cracked, printed with old footmarks and holding nothing at all. Right at "
            "the bottom edge of the picture, in the crumbling lip where the path meets "
            "the soft field, three last pale gold-brown barley grains lie separate and "
            "countable in the shadow. The bare unsown field and the thorn brake are "
            "soft behind."
        ),
    },
    {
        "id": "v2-r024-b12", "out": "s12-a-heart-so-hardened.jpeg", "seg": "n5",
        "window": "51.366-55.200", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BOAT", "LAKESHORE"],
        "narration": "That, he said, is a heart so hardened that the word never gets below the surface",
        "must_show": "Jesus in the boat saying the hard saying gently — his hand turned palm down and flat as he names the packed ground, his face grave but entirely without anger.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off Jesus; no night, no sunset, no pointing finger of accusation, no raised or shaking fist, no anger, no scroll or book, and Jesus never looks into the lens.",
        "scene": (
            "One photograph, 85mm prime lens at a wide aperture, very shallow depth of "
            "field, bright late-morning sun from high on the right, fine film grain. A "
            "close three-quarter shot of Jesus from his right side as he sits forward "
            "on the stern thwart with one elbow on his knee. His left hand is held out "
            "low and turned palm down, the fingers flat and level, the whole gesture "
            "describing a surface nothing can get through. His face is serious and sad "
            "and quiet — no anger anywhere in it, no severity, no accusation. His head "
            "is turned down and away from the camera to his left and his eyes rest on "
            "the flat of his own hand inside the frame. The weathered hull, the furled "
            "sail and the bright water behind him are entirely soft. No light of any "
            "kind comes off him."
        ),
    },
    {
        "id": "v2-r024-b13", "out": "s13-before-it-is-snatched-away.jpeg", "seg": "n5",
        "window": "55.200-59.079", "wide": False, "jesus": False,
        "locks": ["HARDMAN", "CROWD", "LAKESHORE"],
        "narration": "before it is snatched away.",
        "must_show": "one older listener standing at the back of the crowd on the beach with his arms folded and his face closed, already turning his shoulder away from the water while everyone near him leans in.",
        "must_not_show": "no Jesus in the frame, no boat, no cream or off-white cloth on anybody, no snarl, no sneer, no raised fist, no comic villain, and nobody looking into the lens.",
        "scene": (
            "One photograph, 135mm prime lens at a wide aperture, very shallow depth of "
            "field, bright late-morning sun from high on the right, fine film grain. "
            "The camera stands up the slope behind the crowd and to one side, shooting "
            "along the back row so the eyelines run flat across the frame. Sharp in the "
            "centre stands the heavy-set man of about sixty — thick through the chest, "
            "sun-darkened olive-brown skin, a wide jowled face, hooded dark eyes under "
            "heavy brows, a broad iron-grey beard spread over his chest, grey hair "
            "covered by a charcoal headcloth, in a very dark olive-brown ankle-length "
            "robe with a dark leather belt. His arms are folded high across his chest, "
            "his weight is back on one heel and his near shoulder has already begun to "
            "turn away toward the left edge of the frame. His mouth is a flat closed "
            "line and his eyes are aimed low and to the left at the stones by his own "
            "feet, entirely away from the lens. In front of him and behind him, "
            "blurred, the backs and covered heads of other villagers all lean the other "
            "way, out toward the water."
        ),
    },
    # =============================================== STONY PLACES =============
    {
        "id": "v2-r024-b14", "out": "s14-it-sprang-up-fast.jpeg", "seg": "n6",
        "window": "59.079-64.000", "wide": False, "jesus": False,
        "locks": ["FIELD"],
        "narration": "Some fell on thin soil over rock. It sprang up fast, green and hopeful,",
        "must_show": "a thick stand of bright new green barley shoots standing up out of the shallow skin of soil directly over the pale limestone shelf, healthy and vigorous at this moment.",
        "must_not_show": "no person, no bird, no ripe grain, no withering, no brown or scorched leaf anywhere, no thorns crowding these shoots, no cream or off-white cloth, and no lettering.",
        "scene": (
            "One photograph, 50mm lens close and low to the ground, soft clear morning "
            "sunlight from the left, shallow depth of field, fine film grain. The "
            "camera lies on the slope a hand's breadth above the shelf of pale "
            "limestone, looking along it. Out of the thin stony skin of soil lying over "
            "the rock stands a dense stand of brand-new barley — slender bright "
            "yellow-green blades a hand high, straight and crowded and vivid, some "
            "still carrying the split husk at the tip, every one of them fresh and "
            "unmarked. The morning light comes through the blades from behind so they "
            "read as vivid translucent green. Where the soil is thinnest the bare pale rock breaks "
            "through between the shoots and can be plainly seen carrying them, only a "
            "finger's depth of grit over solid stone. Beyond, out of focus, the bare "
            "field and the dry-stone wall."
        ),
    },
    {
        "id": "v2-r024-b15", "out": "s15-when-the-sun-grew-hot.jpeg", "seg": "n6",
        "window": "64.000-68.883", "wide": False, "jesus": False,
        "locks": ["FIELD"],
        "narration": "but it had no root, and when the sun grew hot it withered.",
        "must_show": "the same stand over the same rock shelf now scorched and collapsed under a hard white overhead sun, the shrivelled blades lying over and one clump lifted clear of the rock showing roots that stopped at the stone.",
        "must_not_show": "no person, no bird, no fire, no smoke, no green healthy shoots left in the frame, no ripe grain, no thorns, no cream or off-white cloth, and no lettering.",
        "scene": (
            "One photograph, 50mm lens close and low, HARD WHITE OVERHEAD NOON SUN "
            "straight down with almost no shadow and the light bleaching the stone, "
            "shallow depth of field, fine film grain. The camera lies on the shelf of "
            "pale limestone in the same place as before, looking along the same stand. "
            "The barley that stood up bright green is now dead: the blades are pale "
            "straw and rust-brown, twisted, curled at the edges and folded over flat "
            "against the hot rock, brittle enough to see the crimp in them. The thin "
            "grit between them has dried to dust and cracked. At the near edge of the "
            "frame one clump has pulled free of the stone and lies on its side, and the "
            "whole of its root system is visible in one glance — a pale flat mat of "
            "fine threads spread sideways with nothing going down, stopped dead against "
            "the solid limestone a finger's depth below the surface. The bleached rock "
            "and the shimmering heat close the picture."
        ),
    },
    {
        "id": "v2-r024-b16", "out": "s16-says-yes-with-joy.jpeg", "seg": "n7",
        "window": "68.883-72.600", "wide": False, "jesus": False,
        "locks": ["YOUNGMAN", "CROWD", "LAKESHORE"],
        "narration": "That is the heart that says yes with joy,",
        "must_show": "ANCHOR FRAME — the young man's face large, sharp and fully lit in the crowd on the beach, lit up with open delighted belief as he listens.",
        "must_not_show": "no Jesus in the frame, no boat, no cream or off-white cloth on anybody including the blurred crowd behind him, no tears, no anguish, no comic grin, and he never looks into the lens.",
        "scene": (
            "One photograph, 105mm prime lens at a wide aperture, very shallow depth of "
            "field, bright late-morning sun from high on the right falling full and "
            "even across his face, fine film grain. The camera stands among the crowd "
            "on the beach, side-on to him and close, so his face fills the upper "
            "left of the frame and his eyeline runs flat across the picture to the "
            "right. A young man of about nineteen, slight and narrow-shouldered, warm "
            "olive-brown skin, a smooth open face with round cheeks and large dark "
            "brown eyes, only the first thin dark beard along his jaw and upper lip, "
            "dark brown wavy hair to the jaw pushed back behind his ears with no head "
            "covering, in a dark indigo knee-length tunic with a plain cord belt. He is "
            "half risen from his heels with his weight up on the balls of his feet, his "
            "chin lifted and his mouth open in a broad involuntary smile of pure "
            "delight, both hands come up and open in front of his chest. His eyes are "
            "wide and shining and fixed out to the right across the frame on the water "
            "beyond the picture edge. Behind him the crowd in dark umber, indigo and "
            "russet is a soft blur."
        ),
    },
    {
        "id": "v2-r024-b17", "out": "s17-nothing-underneath-to-hold-it.jpeg", "seg": "n7",
        "window": "72.600-76.335", "wide": False, "jesus": False,
        "locks": ["YOUNGMAN", "CROWD", "LAKESHORE"],
        "narration": "but has nothing underneath to hold it when things get hard.",
        "must_show": "the same young man moments later with the joy gone out of him — sat back down on his heels, shoulders dropped, hands fallen empty into his lap, looking at the stones instead of the water.",
        "must_not_show": "no Jesus in the frame, no boat, no cream or off-white cloth on anybody, no tears running, no sobbing, no anger, no other person sharp in the frame, and he never looks into the lens.",
        "scene": (
            "One photograph, 105mm prime lens at a wide aperture, very shallow depth of "
            "field, bright late-morning sun from high on the right, fine film grain. "
            "The camera stands in the same place among the crowd, side-on and close, "
            "and his eyeline runs down and out through the bottom of the frame. The "
            "same locked young man — about nineteen, slight, warm olive-brown skin, the "
            "first thin dark beard along his jaw, dark brown wavy hair to the jaw and "
            "no head covering, dark indigo knee-length tunic with a cord belt — has "
            "settled back down onto his heels. His shoulders have dropped, his chest "
            "has gone hollow, his hands have fallen open and empty into his lap and one "
            "of them is turning a small dark basalt pebble over and over. His mouth is "
            "closed and his brows are drawn faintly together; the smile has left no "
            "trace. His eyes are down on the stones between his own feet inside the "
            "frame. The crowd behind him, dark and blurred, still leans out toward the "
            "water he is no longer watching."
        ),
    },
    # =============================================== AMONG THORNS ============
    {
        "id": "v2-r024-b18", "out": "s18-some-fell-among-thorns.jpeg", "seg": "n8",
        "window": "76.335-81.800", "wide": False, "jesus": False,
        "locks": ["FIELD"],
        "narration": "Some fell among thorns. The seed grew, but so did the weeds,",
        "must_show": "young green barley and young thorn and thistle coming up together in the same ground along the field margin, the crop still standing clear at this stage but the weeds already among it.",
        "must_not_show": "no person, no bird, no ripe grain, no scorched or withered blade, no bare rock shelf under these plants, no cream or off-white cloth, and no lettering.",
        "scene": (
            "One photograph, 50mm lens low among the plants, soft clear morning "
            "sunlight from the left, shallow depth of field, fine film grain. The "
            "camera sits down inside the growth at the field margin looking along the "
            "ground. Slender bright green barley blades a hand and a half high stand "
            "through the frame, healthy and upright. Rising among them, unmistakably "
            "different, are young thorn and thistle — thick grey-green stems already "
            "stouter than the barley, lobed spiny leaves with pale sharp points, and "
            "the first hooked prickles showing along the ribs. At this stage the barley "
            "is still clear of them and still has the light. Behind, out of focus, the "
            "dark mass of the old thorn brake with its dead grey canes standing among "
            "the new growth."
        ),
    },
    {
        "id": "v2-r024-b19", "out": "s19-crowded-in-and-choked-it.jpeg", "seg": "n8",
        "window": "81.800-87.366", "wide": False, "jesus": False,
        "locks": ["FIELD"],
        "narration": "and the worries and wants of this life crowded in and choked it before it could bear anything.",
        "must_show": "the thorns now grown far over the barley and shutting the light off it — the crop underneath thin, yellow, bent and carrying no ear of grain at all.",
        "must_not_show": "no person, no bird, no ripe grain, no full or heavy ear of barley anywhere in this frame, no fire, no rock shelf, no cream or off-white cloth, and no lettering.",
        "scene": (
            "One photograph, 50mm lens low and close, the light coming down through the "
            "thorn canopy in broken patches so most of the frame sits in green shade, "
            "shallow depth of field, fine film grain. The camera lies at the base of "
            "the growth looking up and along. Woody grey-green thorn and thistle have "
            "taken the whole space: thick fibrous stems as tall as a man's chest, wide "
            "spiny lobed leaves overlapping into a low roof, hard hooked prickles "
            "catching the light along every rib, some heads already gone to dry purple "
            "flower. Underneath them, in the shade, the barley is still alive and is "
            "plainly losing: pale sickly yellow-green, drawn thin and leggy from "
            "reaching for light, bent over sideways under a leaning thorn stem, and not "
            "one of its stalks carries an ear of grain — the heads never formed. A "
            "single thorn stem crosses hard through the foreground in sharp focus."
        ),
    },
    # =============================================== GOOD GROUND ==============
    {
        "id": "v2-r024-b20", "out": "s20-fell-into-good-ground.jpeg", "seg": "j8",
        "window": "87.366-92.400", "wide": False, "jesus": False,
        "locks": ["FIELD", "SEED"],
        "narration": "But other fell into good ground,",
        "must_show": "barley grain falling into the deep dark broken loam of the good corner and settling down between the clods, some grains already half covered by crumbling soil.",
        "must_not_show": "no person's face, no bird, no crop yet, no green shoots, no ripe grain, no path, no rock shelf, no thorns, no cream or off-white cloth, and no lettering.",
        "scene": (
            "One photograph, 100mm macro lens close to the ground, fast shutter, warm "
            "clear morning sunlight from the left raking across the clods and modelling "
            "every crumb, very shallow depth of field, fine film grain. The camera lies "
            "on the dark tilled corner of the field looking down into the broken earth. "
            "The loam is deep red-brown and freshly worked, crumbled into loose "
            "irregular clods with dark open pockets between them and a faint damp sheen "
            "on the fresh-turned faces. Pale gold-brown barley grains are coming down "
            "into it: three still in the air, sharp and separate and caught mid-fall, "
            "and eight already landed and lying down in the hollows between the clods, "
            "two of them half buried where a crumb of soil has rolled over them. A "
            "little dust hangs in the raking light. No plant is growing anywhere yet."
        ),
    },
    {
        "id": "v2-r024-b21", "out": "s21-brought-forth-fruit.jpeg", "seg": "j8",
        "window": "92.400-97.416", "wide": False, "jesus": False,
        "locks": ["FIELD"],
        "narration": "and brought forth fruit, some an hundredfold, some sixtyfold, some thirtyfold.",
        "must_show": "the same good corner later in the season standing in heavy ripe gold barley, the ears full and bearded and bowed over with their own weight.",
        "must_not_show": "no person, no bird, no bare earth, no green immature crop, no thorns, no withering, no machine, no sickle in a hand yet, no cream or off-white cloth, and no lettering.",
        "scene": (
            "One photograph, 85mm prime lens at a wide aperture, warm low sunlight "
            "coming from behind the crop and lighting it through, very shallow depth of "
            "field, fine film grain. The camera stands down inside the standing crop at "
            "chest height among the stalks, so the near ears run soft across the bottom "
            "of the frame and one ear stands sharp in the middle of the picture. The "
            "barley is fully ripe: stalks the colour of old straw, and heavy bearded "
            "ears packed tight with plump grain, every long awn lit like a wire by the "
            "sun behind them. The ears are so full that the stems have bowed over under "
            "the weight and the whole field leans one way. It runs back in a deep gold "
            "bank all the way to the dry-stone wall, which is soft in the far "
            "distance, with the tawny hills beyond it. Nobody is in the field."
        ),
    },
    {
        "id": "v2-r024-b22", "out": "s22-open-and-soft-and-ready.jpeg", "seg": "n9",
        "window": "97.416-101.028", "wide": False, "jesus": False,
        "locks": ["SOWER", "FIELD", "SEED"],
        "narration": "But some fell on good ground, open and soft and ready.",
        "must_show": "the sower's own hand down in the dark loam, pressing a few grains into ground that visibly gives way under his fingers.",
        "must_not_show": "no other person, no face in the frame at all, no bird, no crop, no green shoots, no ripe grain, no path, no rock shelf, no thorns, no cream or off-white cloth, and no lettering.",
        "scene": (
            "One photograph, 100mm macro lens, warm clear morning sunlight from the "
            "left, very shallow depth of field, fine film grain. The camera is down on "
            "the ground beside the dark tilled corner, level with the soil, and only "
            "one hand and the cuff of a deep umber-brown sleeve are in the picture — no "
            "face is visible at all. The hand is the locked sower's: a working farmer's "
            "hand of about forty, thick-fingered, sun-blackened olive-brown, cracked "
            "and dark across the knuckles, dirt worked into the creases and under the "
            "nails. It is pressed down into the deep red-brown loam, the fingers "
            "half-buried and the soil crumbling and closing over them, three pale "
            "gold-brown barley grains still resting in the hollow of the palm. The "
            "earth around the hand is loose, open and dark, holding the shape of his "
            "fingers where it has given way. Everything beyond a hand's breadth is soft "
            "blur."
        ),
    },
    {
        "id": "v2-r024-b23", "out": "s23-a-harvest-many-times-over.jpeg", "seg": "n9",
        "window": "101.028-106.018", "wide": True, "jesus": False,
        "locks": ["SOWER", "FIELD"],
        "narration": "It took root, and grew, and gave back a harvest many times over.",
        "must_show": "the sower standing chest-deep in his own ripe barley at harvest, seen from behind, with the loaded gold field running away in front of him.",
        "must_not_show": "no other person, no bird, no bare earth, no green immature crop, no thorns, no rock shelf, no machine, no cart, no cream or off-white cloth, and not one face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, warm low sunlight from the right, deep focus, "
            "fine film grain. THE CAMERA STANDS IN THE CROP BEHIND THE SOWER AND SHOOTS "
            "PAST HIM: his back fills the near left of the frame in three-quarter from "
            "behind and his face is not visible to the camera at all. The same locked "
            "man — about forty, lean and hard, deep umber-brown knee-length tunic, "
            "twisted rope belt, wide charcoal shoulder strap, black hair bound back "
            "with a strip of dark russet cloth — stands chest-deep in his own barley "
            "with his right hand out flat and open, resting on top of the ears the way "
            "a man rests his hand on water. His head is tipped a little back and his "
            "gaze goes away from the camera out across his field to the far wall inside "
            "the frame. In front of him the ripe crop runs away in a heavy gold bank, "
            "the ears bowed over with weight and the awns lit up by the low sun, all "
            "the way to the dry-stone wall, the tawny hills and the distant flat-roofed "
            "village."
        ),
    },
    # ===================================== JESUS EXPLAINS THE GOOD GROUND =====
    {
        "id": "v2-r024-b24", "out": "s24-he-that-heareth-the-word.jpeg", "seg": "j3",
        "window": "106.018-111.700", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BOAT", "LAKESHORE"],
        "narration": "But he that received seed into the good ground is he that heareth the word,",
        "must_show": "Jesus in the boat naming the good ground — leaning forward on the thwart with one hand open toward the people on the beach, his whole face given to them.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off Jesus; no night, no sunset, no scroll or book, no raised platform, no standing on the water, NO SECOND PERSON ANYWHERE IN THE FRAME — no shoulder, back, arm, head or garment of anybody else in the foreground, near edge or background, sharp or blurred — no cream, off-white, pale or bleached cloth anywhere in the picture except on Jesus himself, and Jesus never looks into the lens.",
        "scene": (
            "One photograph, 85mm prime lens at a wide aperture, very shallow depth of "
            "field, bright late-morning sun from high on the right, fine film grain. "
            "JESUS IS THE ONLY PERSON IN THIS PICTURE AND THE NEAR FOREGROUND IS OPEN "
            "WATER: the camera floats low on the lake itself off the boat's shoreward "
            "quarter with nothing between it and the hull but a hand's depth of clear "
            "shallow water and the pale stony bottom, so the bottom of the frame is "
            "water and wet planking and nothing else. Nobody stands, wades, kneels or "
            "passes between the camera and the boat, and no part of any other body is "
            "in the shot. Jesus is seen in three-quarter from his left. He has come "
            "forward off the "
            "thwart until his elbows are on his knees, and his right hand is out and "
            "open toward the shore, palm up and fingers spread, held low over the "
            "water. His face is warm and lit and entirely given away: brows lifted a "
            "little, mouth open on the word. His head is turned well off the camera "
            "axis to his left and his eyes travel out past the left edge of the frame "
            "to the people on the beach the viewer cannot see. The furled sail, the "
            "steering oar and the bright flat water behind him are soft. No light of any "
            "kind comes off him."
        ),
    },
    {
        "id": "v2-r024-b25", "out": "s25-and-understandeth-it.jpeg", "seg": "j3",
        "window": "111.700-117.400", "wide": False, "jesus": False,
        "locks": ["WOMAN", "CROWD", "LAKESHORE"],
        "narration": "and understandeth it;",
        "must_show": "ANCHOR FRAME — the woman's face large, sharp and fully lit in the crowd at the exact moment she understands: still, absorbed, her hand come up to the base of her throat.",
        "must_not_show": "no Jesus in the frame, no boat in focus, no cream or off-white cloth on anybody including the blurred crowd, no weeping, no ecstatic expression, no praying pose, and she never looks into the lens.",
        "scene": (
            "One photograph, 105mm prime lens at a wide aperture, very shallow depth of "
            "field, bright late-morning sun from high on the right falling full and "
            "even across her face, fine film grain. The camera stands among the crowd "
            "on the beach, side-on and close, so her face fills the right of the frame "
            "and her eyeline runs flat across the picture to the left. A woman of about "
            "thirty-five, ordinary build, weathered warm olive-brown skin, a long oval "
            "face with high cheekbones, a strong straight nose and steady dark brown "
            "eyes with fine lines at their corners, her hair entirely covered by a "
            "wound deep russet headcloth falling over her shoulders, in a dark ochre "
            "ankle-length robe with a charcoal sash. She has gone completely still. Her "
            "lips are parted, her brows have drawn up in the middle, and her right hand "
            "has come up without her noticing to rest at the base of her throat. Her "
            "eyes are fixed away to the left across the frame, out over the water, "
            "clear and wide and absolutely steady. Around her the crowd in dark indigo, "
            "umber and russet dissolves into blur."
        ),
    },
    {
        "id": "v2-r024-b26", "out": "s26-bringeth-forth-fruit.jpeg", "seg": "j3",
        "window": "117.400-123.043", "wide": True, "jesus": False,
        "locks": ["FIELD"],
        "narration": "which also beareth fruit, and bringeth forth, some an hundredfold, some sixty, some thirty.",
        "must_show": "the harvest actually being taken — reapers at work low in the ripe barley with hand sickles, and cut sheaves standing bound in the stubble behind them.",
        "must_not_show": "no Jesus in the frame, no boat, no machine of any kind, no cart with spoked or shod wheels, no animal in harness, no cream or off-white cloth on anybody, no bare earth, no thorns, and not one face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, warm low late-season sunlight from the right, "
            "deep focus, fine film grain. THE CAMERA STANDS IN THE STANDING CROP BEHIND "
            "THE REAPERS AND SHOOTS PAST THEM ACROSS THE FIELD: the near ears run "
            "blurred across the bottom of the frame and every worker is seen from "
            "behind or in profile, with not one face turned toward the lens. Four "
            "harvesters are bent low in the ripe barley, each in a dark knee-length "
            "tunic of deep umber, charcoal, dark ochre or deep russet, each with a "
            "wound dark headcloth against the sun. The nearest is caught mid-stroke: "
            "his left fist closed around a handful of standing stalks and his right arm "
            "drawing a short curved hand-forged iron sickle through them close to the "
            "ground. Behind the cut line the stubble is pale and bristled, and eight "
            "bound sheaves stand propped together in pairs, tied at the waist with "
            "twisted straw rope, the heavy ears all pointing up. Beyond them the "
            "uncut gold field, the dry-stone wall and the tawny hills."
        ),
    },
    {
        "id": "v2-r024-b27", "out": "s27-hears-him-takes-it-in.jpeg", "seg": "n10",
        "window": "123.043-127.584", "wide": False, "jesus": False,
        "locks": ["WOMAN", "CROWD", "LAKESHORE"],
        "narration": "The good ground is simply the heart that hears him, takes it in, and holds on.",
        "must_show": "the same woman a moment later holding on to what she has heard — her hand closed shut over her breastbone, her eyes still out on the water, everything else in the crowd blurred around her.",
        "must_not_show": "no Jesus in the frame, no boat in focus, no cream or off-white cloth on anybody, no weeping, no praying hands pressed together, no kneeling, and she never looks into the lens.",
        "scene": (
            "One photograph, 135mm prime lens at a wide aperture, extremely shallow "
            "depth of field, bright late-morning sun from high on the right, fine film "
            "grain. The camera stands among the crowd, side-on and a little further "
            "back, and her eyeline runs flat across the frame to the left. The same "
            "locked woman — about thirty-five, weathered warm olive-brown skin, a long "
            "oval face with high cheekbones and steady dark brown eyes, hair entirely "
            "covered by a wound deep russet headcloth, dark ochre ankle-length robe "
            "with a charcoal sash — has closed her right hand into a loose fist and "
            "pressed it flat against her breastbone, holding it there. Her chin has "
            "come down a little, her mouth is closed, and her eyes stay out on the "
            "water past the left edge of the frame, unblinking. Her shoulders have "
            "settled. Every other person around her is reduced to soft dark shapes of "
            "indigo, umber and russet."
        ),
    },
    {
        "id": "v2-r024-b28", "out": "s28-far-more-than-was-put-in.jpeg", "seg": "n10",
        "window": "127.584-131.932", "wide": False, "jesus": False,
        "locks": ["SOWER", "FIELD", "SEED"],
        "narration": "And it gives back far more than was ever put in.",
        "must_show": "the sower's two cupped hands overflowing with threshed barley at harvest, far more grain than a hand can hold, with the pale stubble field behind him.",
        "must_not_show": "no other person, no bird, no green crop, no bare unsown earth, no thorns, no rock shelf, no scale, balance or measure of any kind, no coins, no cream or off-white cloth, and his face never turns toward the lens.",
        "scene": (
            "One photograph, 100mm lens at a wide aperture, warm low late-afternoon "
            "sunlight from the right coming across the grain, very shallow depth of "
            "field, fine film grain. The camera is low and close and looks slightly "
            "down onto two cupped hands held out into the light. They are the locked "
            "sower's hands — thick-fingered, sun-blackened olive-brown, cracked across "
            "the knuckles, chaff dust caught in the creases — and the deep umber-brown "
            "cuffs of his tunic show at the wrists. They are heaped past overflowing "
            "with clean threshed barley: hundreds of plump pale gold-brown kernels "
            "mounded above the fingers, a stream of them already spilling over the edge "
            "of his little finger and falling out of the bottom of the frame, and a "
            "haze of chaff hanging lit in the air around them. Above and behind the "
            "hands his chest, beard and the underside of his jaw are visible but his "
            "face is tipped down toward the grain and away from the lens, out of focus. "
            "The pale cut stubble field runs away soft behind him."
        ),
    },
    # ============================== HE DID NOT SKIP THE HARD GROUND ==========
    {
        "id": "v2-r024-b29", "out": "s29-did-not-skip-the-hard-path.jpeg", "seg": "n11",
        "window": "131.932-135.927", "wide": False, "jesus": False,
        "locks": ["SOWER", "FIELD", "SEED"],
        "narration": "Notice the farmer did not skip the hard path or the rocky places.",
        "must_show": "the sower deliberately throwing seed straight ACROSS the beaten footpath and over the bare rock shelf — the two grounds he knows will fail — with the grain plainly in the air above them.",
        "must_not_show": "no other person, no bird, no crop, no green shoots, no ripe grain, no hesitation or reluctance in his face, no cream or off-white cloth, and he never looks into the lens.",
        "scene": (
            "One photograph, 35mm lens, fast shutter freezing the grain, clear "
            "late-morning sun from the right, deep focus, fine film grain. The camera "
            "stands side-on to the sower and low, at the far side of the footpath, so "
            "his whole throw runs flat across the frame from right to left and he is "
            "seen in profile. The same locked man — about forty, lean and hard, dense "
            "black beard streaked with grey, black hair bound back with a strip of dark "
            "russet cloth, deep umber-brown knee-length tunic, twisted rope belt, "
            "charcoal shoulder strap, woven fibre bag at his hip — is mid-stride with "
            "his right arm swung out and open at the end of the throw. His head is "
            "turned to follow the grain and his eyes are down on the path inside the "
            "frame. A wide fan of individually visible pale gold-brown barley grains "
            "hangs in the air directly over the hard grey beaten track in the "
            "foreground, and the far edge of the same throw is coming down on the pale "
            "limestone shelf beyond it. He is throwing onto the two worst grounds in "
            "the field on purpose and his face shows no reluctance at all."
        ),
    },
    {
        "id": "v2-r024-b30", "out": "s30-he-threw-seed-everywhere.jpeg", "seg": "n11",
        "window": "135.927-139.805", "wide": True, "jesus": False,
        "locks": ["SOWER", "FIELD", "SEED"],
        "narration": "He threw seed everywhere, on every heart, hoping.",
        "must_show": "one wide photograph in which the sower's thrown grain is visibly falling across all four grounds at once — the path, the rock shelf, the thorn margin and the dark tilled corner.",
        "must_not_show": "no other person, no bird, no crop, no green shoots, no ripe grain, no fence, no wire, no tower, no dome, no minaret, no cream or off-white cloth, and not one face turned toward the lens.",
        "scene": (
            "One photograph, 28mm lens, clear late-morning sun from the right, deep "
            "focus front to back, fine film grain. THE CAMERA STANDS BEHIND THE SOWER "
            "AND SHOOTS PAST HIM UP THE SLOPE: his back and his outflung right arm fill "
            "the near left of the frame in three-quarter from behind, dark and partly "
            "soft, and his face is not visible to the camera at all. The same locked "
            "man in the deep umber-brown knee-length tunic, charcoal shoulder strap and "
            "woven fibre bag has just released a full handful and it is spread out in "
            "front of him across the whole picture: separate pale gold-brown grains lit "
            "against the shadowed ground, falling at the same moment onto the hard grey "
            "footpath crossing the bottom of the frame, onto the pale limestone shelf "
            "at the left, into the grey-green thorn brake along the right margin, and "
            "onto the deep dark tilled corner at the top. Every kind of ground in the "
            "field is getting the same seed in the same throw. The dry-stone walls, the "
            "tawny hills and the far flat-roofed village close the top of the frame."
        ),
    },
    {
        "id": "v2-r024-b31", "out": "s31-how-generous-god-is.jpeg", "seg": "n11",
        "window": "139.805-143.930", "wide": False, "jesus": False,
        "locks": ["SOWER", "SEED", "FIELD"],
        "narration": "That is how generous God is with his word.",
        "must_show": "the emptied seed bag — the sower's hand holding its mouth wide open with only a few last grains and dust in the bottom, the sown field soft behind it.",
        "must_not_show": "no other person, no face in the frame at all, no bird, no crop, no green shoots, no ripe grain, no coins, no scale or measure, no cream or off-white cloth, and no lettering.",
        "scene": (
            "One photograph, 85mm lens at a wide aperture, warm clear late-morning "
            "sunlight from the left falling down into the bag, very shallow depth of "
            "field, fine film grain. The camera is close and slightly above, looking "
            "down into the mouth of the hand-woven plant-fibre seed bag where it hangs "
            "at the sower's hip. One weathered hand — thick-fingered, sun-blackened "
            "olive-brown, cracked across the knuckles, the deep umber-brown cuff at the "
            "wrist and the wide charcoal shoulder strap crossing behind it — holds the "
            "mouth of the bag pulled wide open. Inside, the coarse fibre weave is "
            "empty: nothing left but chaff dust, a few husks and five or six last pale "
            "gold-brown barley grains lying separate in the seam at the bottom, lit by "
            "the sun coming in over the rim. No face is in the picture. Beyond the bag "
            "the freshly sown bare field, the beaten path and the distant wall fall "
            "away into soft blur."
        ),
    },
    {
        "id": "v2-r024-b32", "out": "s32-who-hath-ears-to-hear.jpeg", "seg": "j2",
        "window": "143.930-147.867", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BOAT", "LAKESHORE"],
        "narration": "Who hath ears to hear, let him hear.",
        "must_show": "Jesus in the boat on the last line of the parable — quiet, direct and warm, his hands come to rest, everything in his face given to the people on the beach.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off Jesus; no night, no sunset, no pointing finger, no raised hand of warning, no scroll or book, and Jesus never looks into the lens.",
        "scene": (
            "One photograph, 105mm prime lens at a wide aperture, very shallow depth of "
            "field, bright late-morning sun from high on the right, fine film grain. A "
            "close three-quarter shot of Jesus from his left as he sits back on the "
            "stern thwart. He has finished: his hands have come down and settled loose "
            "and open on his knees, one thumb resting across the other, and his "
            "shoulders have dropped. His face is quiet and warm and completely without "
            "strain, his mouth just closing on the last word, his brows level. His head "
            "is turned off the camera axis to his left and his eyes are steady on one "
            "person standing on the beach beyond the left edge of the frame — plainly "
            "fixed on somebody inside the story and never near the lens. Behind him the "
            "weathered rail, the coiled flax rope and the wide bright water are soft. "
            "No light of any kind comes off him."
        ),
    },
    # =============================== AND GROUND CAN CHANGE ====================
    {
        "id": "v2-r024-b33", "out": "s33-a-hard-path-can-be-broken.jpeg", "seg": "n12",
        "window": "147.867-151.676", "wide": False, "jesus": False,
        "locks": ["SOWER", "FIELD"],
        "narration": "And ground can change. A hard path can be broken up.",
        "must_show": "the beaten footpath being broken open — an iron mattock driven into the hard grey track and the packed crust bursting apart into dark clods.",
        "must_not_show": "no other person, no bird, no crop, no green shoots, no ripe grain, no plough drawn by animals, no machine, no cream or off-white cloth, and his face never turns toward the lens.",
        "scene": (
            "One photograph, 50mm lens low and close to the ground, fast shutter "
            "freezing the flying earth, warm low late-afternoon sunlight from the right "
            "raking across the track, shallow depth of field, fine film grain. The "
            "camera lies on the path itself, side-on to the work, so the blow runs "
            "across the frame. A short-handled mattock of hewn olive wood with a heavy "
            "hammer-marked iron head is buried in the hard grey path at the moment of "
            "impact, and the packed crust is bursting open around it — a wedge of "
            "polished surface lifting and cracking away, dark damp earth showing "
            "underneath for the first time, clods and dust flying up into the low "
            "light. Above the tool the locked sower's forearms and chest are in the "
            "frame — sun-blackened olive-brown skin, corded muscle, the deep umber-brown "
            "tunic sleeve — with his weight driven down through the handle. His head is "
            "bent down over the work and away from the camera and his face is not "
            "visible."
        ),
    },
    {
        "id": "v2-r024-b34", "out": "s34-rocky-soil-can-be-cleared.jpeg", "seg": "n12",
        "window": "151.676-155.775", "wide": False, "jesus": False,
        "locks": ["SOWER", "FIELD"],
        "narration": "Rocky soil can be cleared. That is how good he is.",
        "must_show": "the stones being carried off the shelf by hand — the sower straightening up with a heavy stone in both arms and a low cleared heap of gathered stones already built at the field edge.",
        "must_not_show": "no other person, no bird, no crop, no green shoots, no ripe grain, no cart, no machine, no cream or off-white cloth, and he never looks into the lens.",
        "scene": (
            "One photograph, 50mm lens from low and side-on, warm low late-afternoon "
            "sunlight from the right, shallow depth of field, fine film grain. The "
            "camera stands beside the limestone shelf level with his knees, so his "
            "whole body runs across the frame in profile. The same locked man — about "
            "forty, lean and hard, dense black beard streaked with grey, black hair "
            "bound back with a strip of dark russet cloth, deep umber-brown knee-length "
            "tunic, twisted rope belt — is straightening up out of a crouch with a "
            "heavy angular pale limestone rock held against his chest in both arms, his "
            "back braced and the tendons standing out in his forearms. His head is "
            "turned down and to his right toward the low stone heap he is walking "
            "toward inside the frame, and his eyes are on it. At the field edge that "
            "heap is already knee-high, forty or fifty gathered pale stones stacked "
            "loose. Where he has been working, the shelf behind him is showing a "
            "widening patch of cleared dark soil among the rock."
        ),
    },
    {
        "id": "v2-r024-b35", "out": "s35-he-keeps-sowing.jpeg", "seg": "n12",
        "window": "155.775-161.223", "wide": True, "jesus": False,
        "locks": ["SOWER", "FIELD", "SEED"],
        "narration": "He keeps sowing, and he never stops hoping your heart will be the good ground.",
        "must_show": "the sower going back out across the newly broken ground in warm late-afternoon light and throwing again, the fresh grain in the air over earth that used to be the hard path.",
        "must_not_show": "no other person, no bird, no ripe grain, no thorns crowding him, no sunset colours, no orange or red sky, no night, no lamp, no cream or off-white cloth, and not one face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sunlight from the right "
            "with long soft shadows and clean unsaturated golden light, deep focus, "
            "fine film grain. THE CAMERA STANDS BEHIND THE SOWER AND SHOOTS PAST HIM "
            "ACROSS THE FIELD: he is walking away from the camera up the slope and is "
            "seen entirely from behind, his face not visible at all. The same locked "
            "man in the deep umber-brown knee-length tunic, twisted rope belt and wide "
            "charcoal shoulder strap has his right arm swung out again and a fresh wide "
            "fan of separate pale gold-brown barley grains hangs lit in the air in "
            "front of him. He is throwing it over the strip that used to be the hard "
            "beaten path and is now broken open into dark crumbling clods, his own "
            "footprints and the mattock marks still in it, and the cleared limestone "
            "shelf beyond it showing fresh dark soil among the stones. The stone heap "
            "he built stands at the field edge. Above the slope the sky is clear pale "
            "blue with no colour in it at all."
        ),
    },
]
