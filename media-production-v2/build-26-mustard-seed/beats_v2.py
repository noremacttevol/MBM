#!/usr/bin/env python3
"""V2 beat map — row 26, build-26-mustard-seed (Matthew 13:31-32 / Luke 13:19), realistic.

COVERAGE: 24 pictures against V1's SIX, over 79.14 s of story = 3.30 s/picture.
V1 reused `s1.jpeg` for n0, n1 AND n8 (three separate places in the video) and held
`s5.jpeg` across n4, n5 AND n9. Six pictures for a 1:27 video is one still every
fourteen seconds, and the two KJV segments — j1 at 10.9 s and j1b at 12.1 s, the
longest single stretches in the video and the only red-letter words in it — got ONE
picture each.

⚠️ THE INHERITED beats_v2.py WAS DISCARDED, and this is why (measured, not assumed).
Its fourteen windows were built from `audio_start`→`spoken_end` instead of from the
SEGMENT boundaries, so the map had a DEAD GAP at every single segment join — 3.44→4.01,
8.93→9.47, 12.91→13.45, 17.91→18.47, 27.85→29.39, 40.07→41.52, 46.53→47.11,
54.31→54.84, 59.44→60.00, 63.16→63.65, 71.96→72.51, 79.15→79.42 — twelve gaps totalling
about 5.9 s with no picture assigned at all. It also gave the whole of j1 (9.4 s) and
the whole of j1b (10.7 s) one picture each, and staged the frame at the seaside, which
is the third row running to use rows 24/25's beach and boat.

AUDIO IS CLEAN AND LOCKED (checked from the FILES, not from prose):
  * `matthew-13_mustard-seed.mp4` and every `audio/*.mp3` last changed bytes in the
    SAME commit (git CONTENT date 2026-07-28 16:30:55 — mtimes are worthless in this
    repo). No mp3 is newer than the MP4, so `assert_v1_final_is_current()` has nothing
    to refuse.
  * V1 MP4 runs 87.067 s against the summed timeline's 87.015 s — a 0.052 s tail, far
    inside the 0.75 s tripwire.
  * SOURCING TRAP CHECKED AND CLEARED. `n0 j1 j1b n5 n8 n9 card` were all transcribed
    with faster-whisper and every one matches the LIVE `make_narration.py` word for
    word. NO `TEXT_OVERRIDES` are needed on this row and `AUDIO_FROM_V1_SEGMENTS`
    stays off.

⚠️ WINDOWS COMPUTED FROM SCRATCH 2026-08-02 with the fixed `extract_beats.py` reading
the V1 build, then split inside each segment on WORD boundaries measured from that
segment's own mp3 with faster-whisper `word_timestamps=True`. The `.timing.json`
sidecars on this row carry only ONE phrase for nine of the twelve segments, so they
cannot supply an interior split at all — word timings are the only honest source here.
No split falls inside a word and every split sits on a comma, a clause head or a
sentence boundary. Contiguous 0.280 s → 79.419 s (the card start), zero gaps, zero
overlaps, shortest window 2.10 s.

SCRIPTURE FACTS (Matthew 13:31-32, Luke 13:19 KJV):
  Matt 13:31  "The kingdom of heaven is like to a grain of mustard seed, which a man
              took, and SOWED IN HIS FIELD" — Luke 13:19 has "cast INTO HIS GARDEN".
  Matt 13:32  "which indeed is the LEAST OF ALL SEEDS: but when it is grown, it is the
              GREATEST AMONG HERBS, and becometh a TREE, so that the BIRDS OF THE AIR
              come and LODGE IN THE BRANCHES thereof."
The whole parable is a size comparison, so every frame has to make size READABLE: the
seed is always shown against something a viewer already knows the size of (a fingertip,
the creases of a palm, a clod of earth), and the grown plant is always shown against
the garden beds, the wall and the people it towers over. A seed floating on a plain
background proves nothing.

BOTANICAL FACT THE STORY TURNS ON: black mustard seed is a hard round grain about one
millimetre across — smaller than a peppercorn, dark red-brown. The grown plant is a
woody-stemmed shrub three to four metres tall with a spreading OPEN crown of large
rough green leaves and sprays of small four-petalled YELLOW flowers, strong enough at
the forks to carry a nesting bird. It is NOT a broad shade tree, NOT an oak, NOT a fig
and NOT a palm, and getting that wrong turns the parable into a different one.

STAGING ACROSS THE LIBRARY — this row must not repeat a composition already used:
  rows 2, 8, 21 (Luke 15)      courtyard table / low wall under a fig tree / house meal
  row 11 (the storm)           an open boat at NIGHT in a gale
  row 16 (Mary & Martha)       a lamplit evening interior
  row 19 (breakfast on shore)  a Galilee beach at FIRST LIGHT with a charcoal fire
  row 22 (unmerciful servant)  a black basalt Capernaum doorstep and street
  row 23 (vineyard workers)    a terraced hillside above a vineyard
  row 24 (the sower)           a moored fishing boat off a daylit shingle beach
  row 25 (wheat and tares)     an open grain plain and a round threshing floor
So this row is staged inside a SMALL WALLED KITCHEN GARDEN on the edge of a village —
mud-brick walls barely above head height, narrow raised beds of dark hand-tilled soil,
hand-cut watering channels, a stone-lined cistern in one corner, a plank gate. It is
enclosed, intensively worked and human-scale: the visual opposite of row 25's open
grain plain and row 24's beach, and no other row uses it. Luke 13:19's "cast into his
garden" is the scriptural warrant, and V1's own narration already says "the largest
plant in the WHOLE GARDEN", so the garden is the setting the audio itself asks for.
The light is CLEAR BRIGHT DAYLIGHT throughout — high late-morning sun in the frame
beats, clear low early-morning sun in the story beats. There is no sunset palette
anywhere in this row, no night anywhere, and no lamp anywhere.

TERRAIN IS THE INVARIANT, GROWTH STAGE IS WHAT MOVES (the rule rows 24 and 25
established for a parable that spans a season). ONE garden, described identically in
every frame, and THE MUSTARD PLANT GROWS IN THE SAME CORNER BED IN EVERY FRAME, so the
teaching and the story happen in one continuous place and the closing wide shot can
put Jesus and the grown plant in the same picture without inventing anything:
  b01-b02, b06, b09, b19-b22, b24   the frame — Jesus teaching in the garden, the
                                    grown mustard standing in the far corner bed
  b03-b05, b07-b08, b13             the corner bed as BARE dark tilled soil
  b14                               the first shoot breaking the soil crust
  b15                               the young plant waist high above the herb beds
  b10-b12, b16-b18, b23             the full-grown mustard, three to four metres

CAST NOTE — ANCHOR-FIRST (the rows 20-25 lesson that has held the reroll rate at
3-15%). This row needs exactly ONE new face, so exactly ONE beat is an anchor and it
is generated in its OWN run before anything else, composed so the face is large, lit
and alone in the frame:
  b04  the GARDENER, kneeling alone in his own bed, pressing the seed into the soil
`v2_gen_api` builds its REFS cache ONCE per run, so an anchor generated in the same
run as its dependants does not exist yet when they are built — it MUST be a separate
invocation. Jesus is held by JESUS-V2-REF as always.

A FACE SHEET ALONE DOES NOT HOLD A CHARACTER WHO IS SMALL IN FRAME (rows 19, 22-25).
So the GARDENER lock states age, build, hair and beard as explicit invariants, and
every beat that names him RESTATES him positively in its own scene text.

CREAM: only Jesus. A gardener is exactly the figure a model dresses in pale undyed
linen, which reads as a second unlocked Jesus, so he is pinned to DEEP UMBER-BROWN and
the listeners to dark indigo, russet and umber. The phrase "undyed grey-brown wool" is
deliberately NOT used anywhere in this file — on row 21 it rendered near-white every
single time. Every near foreground is stated POSITIVELY and DARK, because the single
reroll on row 24 and one on row 25 were both an out-of-focus CREAM shoulder filling the
near foreground beside Jesus.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks NEVER name a
# character. Clothing colours are stated POSITIVELY and DARK.
LOCKS = {
    # ------------------------------------------------------------- people ----
    "GARDENER": (
        "GARDENER LOCK: the man who took the mustard seed and planted it — the owner "
        "of this garden — is the SAME man in every shot, and these are invariants "
        "that hold even when he is small, distant, in shadow or out of focus: a man "
        "of about forty, lean and wiry with long ropey forearms and big knuckled "
        "hands, deeply sun-browned olive skin, a narrow weathered face with a long "
        "straight nose and deep creases at the corners of steady dark brown eyes, a "
        "MEDIUM-LENGTH DARK BROWN BEARD reaching a hand's width below the chin with "
        "grey coming in at the chin only, and DARK BROWN HAIR to the jawline pushed "
        "back behind his ears. He wears a DEEP UMBER-BROWN coarse wool tunic to the "
        "knee with straight unshaped sleeves rolled to the elbow, a dark madder-red "
        "folded-cloth sash at the waist, and a dark brown head cloth wound close and "
        "tucked at the back of the neck, with plain dark leather sandals. He is NEVER "
        "dressed in cream, off-white or pale linen and never in any light-coloured "
        "garment; his beard is never trimmed short and never absent."
    ),
    "LISTENERS": (
        "LISTENERS LOCK: the people sitting and standing in the garden to hear him "
        "are ordinary Galilean villagers of mixed age — men, women and a few children "
        "— each with a distinct face and none repeated. The men wear DEEP INDIGO, "
        "DARK UMBER and DARK OLIVE-DRAB wool; the women wear RUSSET-RED and dark "
        "madder-brown with head cloths of the same dark cloth; children are in plain "
        "dark brown. NOT ONE of them wears cream, off-white, pale linen or any "
        "light-coloured garment anywhere in the frame, including blurred figures at "
        "the edges, because a pale garment on anyone but Jesus reads as a second, "
        "unlocked Jesus and fails the picture."
    ),
    # ------------------------------------------------------------ settings ----
    "GARDEN": (
        "GARDEN LOCK — this place is IDENTICAL in every frame it appears in and only "
        "the growth of the plants and the angle of the daylight ever change: ONE "
        "small walled kitchen garden on the edge of a village, roughly twelve paces "
        "by eighteen, enclosed by MUD-BRICK WALLS of tan sun-dried brick a little "
        "above head height, plastered rough and rounded at the top by weather. There "
        "is ONE opening in the near wall, a plain gateway closed by a gate of hewn "
        "planks lashed with twisted flax cord. Inside, the ground is worked into "
        "NARROW RAISED BEDS of dark hand-tilled soil separated by shallow hand-cut "
        "watering channels and beaten earth paths just wide enough to kneel in. A "
        "STONE-LINED CISTERN with a low fieldstone kerb sits in the near left corner "
        "with two fired-clay water jars standing beside it and a hand-woven basket "
        "tipped on its side. The far right corner holds ONE larger bed, the corner "
        "bed, and nothing else stands there. Beyond the walls the flat mud roofs of "
        "the village show on one side and low tawny bare hills close the horizon on "
        "the other. There is no other building inside the garden, no roof, no post, "
        "no fence, no animal and no second gate, and the walls, the gateway, the "
        "cistern, the bed layout, the village roofs and the hills never move, never "
        "change shape and never change season between frames."
    ),
    "MUSTARD-SEED": (
        "MUSTARD-SEED LOCK: the seed is a black mustard grain — a hard, perfectly "
        "round, DARK RED-BROWN grain about one millimetre across, smaller than a "
        "peppercorn and barely larger than a grain of coarse sand, with a faintly "
        "pitted matte surface. Its smallness is only readable against something whose "
        "size a viewer already knows, so wherever the seed is shown it is shown "
        "against a human fingertip, the lines and callouses of a palm, or a clod of "
        "broken earth in the same sharp focus. It is never a large bean, never a pale "
        "seed, never a nut, never a pod and never glowing."
    ),
    "MUSTARD-PLANT": (
        "MUSTARD-PLANT LOCK: the grown plant is a black mustard shrub gone to full "
        "size — a single WOODY MAIN STEM about as thick as a man's wrist rising from "
        "the soil and branching low into a SPREADING OPEN CROWN three to four metres "
        "tall and about as wide, carrying large rough mid-green leaves with irregular "
        "lobed edges and loose sprays of small four-petalled YELLOW flowers along the "
        "outer branch tips. Its branches are springy and open enough to see daylight "
        "through, and strong enough at the forks to carry a nesting bird. It is NOT a "
        "broad shade tree, NOT an oak, NOT a fig, NOT an olive, NOT a palm and NOT a "
        "cedar; it has no massive buttressed trunk, no dense unbroken canopy and no "
        "fruit of any kind. It always stands in the far right corner bed of this "
        "garden and nowhere else."
    ),
    "BIRDS": (
        "BIRDS LOCK: the birds are small wild birds of the Galilean countryside — "
        "sparrows, linnets and finches, each about a hand's length, in plain brown, "
        "grey-brown and dull streaked plumage with short conical beaks. They are "
        "correctly sized against the leaves and branches they sit on, with two legs, "
        "two wings and complete feet gripping the twigs. There is no large bird, no "
        "raptor, no dove, no crow, no stork and no exotic or brightly coloured bird "
        "anywhere in the frame, and no bird is larger than a man's hand."
    ),
}

OUTPUT_ASSET_DIR = "assets"

# The V1 MP4 and every V1 mp3 last changed bytes in the same commit and the MP4 runs
# 0.052 s past the summed timeline, so the finished V1 audio stream is current and the
# normal packet-copy AUDIO LOCK applies. Nothing is re-voiced; V1 is never written to.
AUDIO_FROM_V1_SEGMENTS = False

REF = True

REFS = {
    "GARDENER": "assets/s04-planted-it-in-his-field.jpeg",
}

BEATS = [
    # ================== FRAME — the walled garden, bright late morning ==========
    {
        "id": "v2-r026-b01", "out": "s01-a-story-about-the-smallest-seed.jpeg",
        "seg": "n0", "window": "0.280-3.727", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GARDEN", "MUSTARD-PLANT", "LISTENERS"],
        "narration": "Jesus told a story about the smallest seed a farmer knew.",
        "must_show": "Jesus seated on the kerb of the cistern in a small walled kitchen garden in bright late-morning light, beginning to speak, with village listeners settled on the paths and bed edges around him and the tall mustard shrub standing in the far corner bed behind him.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no sunset or sunrise colouring, no boat, no water beyond the cistern, no interior; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, fast prime, clear bright high late-morning "
            "sunlight from the upper left, short hard shadows on the beaten earth "
            "paths, fine film grain. THE CAMERA STANDS BEHIND THE NEAREST LISTENERS "
            "AND SHOOTS PAST THEM ACROSS THE GARDEN: two seated backs fill the near "
            "bottom corners, soft and out of focus, a DEEP INDIGO shoulder at the near "
            "left and a DARK UMBER back and dark brown head cloth at the near right, "
            "and NOT ONE FACE IS TURNED TOWARD THE LENS. Sharp in the middle distance "
            "Jesus sits on the low fieldstone kerb of the stone-lined cistern, leaning "
            "forward with his forearms on his knees and one hand open as he begins to "
            "speak, his head turned to his right and his gaze travelling along the "
            "seated row and out through the right-hand edge of the frame. Around him "
            "villagers sit on the bed edges and squat on the paths in dark indigo, "
            "russet and umber wool, all of them facing him. Two fired-clay water jars "
            "stand at the cistern kerb. In the far right corner bed the full-grown "
            "mustard shrub rises well above the mud-brick wall, its open crown of "
            "rough green leaves and small yellow flower sprays bright against the sky."
        ),
    },
    {
        "id": "v2-r026-b02", "out": "s02-one-grain-between-his-fingers.jpeg",
        "seg": "n1", "window": "3.727-6.927", "jesus": True, "ref": REF,
        "locks": ["GARDEN", "MUSTARD-SEED"],
        "narration": "It was a mustard seed — so tiny it could be lost in the palm of your hand.",
        "must_show": "a close photograph of Jesus alone, holding one single dark mustard grain up between the tip of his thumb and forefinger and looking at it, so the grain is the smallest thing in the frame.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no sunset colouring; no second figure and no pale or off-white cloth anywhere in the frame; his pupils never centred on the lens; the seed is never a large bean, a nut or a pod.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, clear bright "
            "late-morning sunlight from the left modelling one side of his face while "
            "the shaded side stays open and readable, fine film grain. THE CAMERA SITS "
            "LEVEL AND WELL TO HIS LEFT SIDE, SO HIS EYELINE RUNS ACROSS AND UPWARD TO "
            "A NAMED TARGET INSIDE THE PICTURE — the single grain pinched between his "
            "own raised thumb and forefinger at the upper right of the frame — and his "
            "pupils are never centred on the lens. Jesus is framed from the chest up, "
            "his right hand lifted to just above shoulder height with the tiny dark "
            "red-brown mustard grain held between the very tips of his thumb and "
            "forefinger, sharply in focus and dwarfed by his own fingertips, his lips "
            "parted mid-word and his expression warm and unhurried. The near "
            "foreground between the camera and him is nothing but the empty sunlit "
            "beaten earth of the garden path, with nobody standing, sitting or passing "
            "between the camera and him. Behind him the dark raised beds and the rough "
            "tan mud-brick wall fall away into soft blur."
        ),
    },
    {
        "id": "v2-r026-b03", "out": "s03-lost-in-the-palm-of-your-hand.jpeg",
        "seg": "n1", "window": "6.927-9.194",
        "locks": ["GARDEN", "MUSTARD-SEED"],
        "narration": "It was a mustard seed — so tiny it could be lost in the palm of your hand.",
        "must_show": "an extreme close photograph of one weathered working man's open palm held flat in sunlight with a single tiny dark mustard grain sitting alone in the creases of it, so small it is nearly lost among the lines and callouses.",
        "must_not_show": "no face and no second person anywhere in the frame; no cream, off-white or pale cloth at any edge; no night, no lamp; the grain is never large, never pale, never a bean, nut or pod, and never glowing; no text or measurement marks.",
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, clear "
            "bright late-morning sunlight raking from the right so every crease, "
            "callous and grain of dust on the skin throws its own tiny shadow, fine "
            "film grain. THE CAMERA LOOKS STRAIGHT DOWN FROM ABOVE ONTO THE OPEN PALM "
            "and no face is in the picture at all. A single broad sun-browned working "
            "hand fills the frame, palm up and flat, the fingers slightly curled, the "
            "skin cracked at the base of the fingers and darkened with soil. In the "
            "hollow of the palm, sharp and alone, lies ONE hard round dark red-brown "
            "mustard grain about one millimetre across, so small against the deep "
            "lines of the hand that a viewer has to look for it, with a few specks of "
            "dry soil beside it for scale. The near foreground is nothing but the "
            "sunlit skin of the hand itself. Behind and below the hand the dark tilled "
            "soil of a raised garden bed falls completely out of focus."
        ),
    },
    # ================== THE PLANTING — the corner bed, early morning ============
    {
        # ANCHOR — the GARDENER's face sheet. Generated in its OWN run.
        "id": "v2-r026-b04", "out": "s04-planted-it-in-his-field.jpeg",
        "seg": "n2", "window": "9.194-13.173",
        "locks": ["GARDENER", "GARDEN", "MUSTARD-SEED"],
        "narration": "A man took that one little seed and planted it in his field.",
        "must_show": "the gardener kneeling alone in the bare dark corner bed of his own walled garden in clear early-morning light, his face large and fully lit, pressing one tiny mustard grain down into the soil with the tip of one finger.",
        "must_not_show": "no other person anywhere in the frame; no growing mustard plant of any kind, this bed is bare freshly turned soil; no night, no lamp, no sunset colouring; no cream, off-white or pale garment on him or anywhere in the frame; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, clear low "
            "early-morning sun from the right laying warm light straight across his "
            "face and his working hand, fine film grain. THE CAMERA IS DOWN AT KNEE "
            "HEIGHT AND WELL TO HIS LEFT, SHOOTING HIS FACE IN THREE-QUARTER FROM THE "
            "SIDE. HIS GAZE HAS A NAMED TARGET INSIDE THE PICTURE: he is watching the "
            "point of his own finger pressing the grain into the soil at the lower "
            "right of the frame, so his head is bowed and turned down and to his right "
            "and his eyeline leaves the picture through the bottom right corner, far "
            "below and to the side of the lens. The gardener fills the frame from the "
            "waist up, a lean wiry sun-browned man of about forty with a long "
            "weathered face, a MEDIUM-LENGTH DARK BROWN beard greying at the chin, "
            "dark brown hair to the jawline, a dark brown head cloth wound close, and "
            "a DEEP UMBER-BROWN coarse wool tunic with sleeves rolled to the elbow and "
            "a dark madder-red sash. He kneels on one knee in the path beside the "
            "corner bed; his left hand is cupped at his chest holding a small pinch of "
            "dark grain; his right forefinger is pressing one single tiny dark "
            "red-brown mustard grain down into the crumbled dark soil. He is the only "
            "person in the picture. The near foreground is the dark broken soil of the "
            "bed itself. Behind him the raised beds, the watering channels and the "
            "rough tan mud-brick wall run soft and out of focus."
        ),
    },
    {
        "id": "v2-r026-b05", "out": "s05-the-smallest-of-them-all.jpeg",
        "seg": "n3", "window": "13.173-18.192",
        "locks": ["GARDEN", "MUSTARD-SEED"],
        "narration": "Of all the seeds he could have sown, it was just about the smallest of them all.",
        "must_show": "a close photograph looking down at four shallow fired-clay dishes set on the earth path, each holding a different seed a gardener could sow — plump broad beans, flat lentils, round chickpeas — and beside them a fourth dish holding only a thin scatter of the tiny dark mustard grains, visibly the smallest by far.",
        "must_not_show": "no person, no hand, no face anywhere in the frame; no night, no lamp; no cream or pale cloth at any edge; no writing, label, number or marking on any dish; the mustard grains are never as large as the other seeds.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, clear low "
            "early-morning sun from the left so each seed casts its own small shadow "
            "inside its dish, fine film grain. THE CAMERA LOOKS DOWN AT A STEEP ANGLE "
            "ONTO THE EARTH PATH from just above waist height and there is no person "
            "in the picture at all. FOUR shallow hand-thrown fired-clay dishes stand "
            "separated on the beaten earth in a loose row, each one individually "
            "visible and countable: the first holds a handful of large plump "
            "pale-brown broad beans, the second a heap of flat russet lentils, the "
            "third a scatter of round knobbled chickpeas — and the fourth, sharpest in "
            "the frame, holds only a thin scatter of hard round DARK RED-BROWN mustard "
            "grains, each about one millimetre across, so much smaller than everything "
            "beside them that the difference is unmistakable. The near foreground is "
            "the sunlit beaten earth of the path itself. Behind the dishes the dark "
            "raised beds and the rough tan mud-brick wall fall out of focus."
        ),
    },
    # ============================ KJV — verse 31, Jesus speaking ================
    {
        "id": "v2-r026-b06", "out": "s06-the-kingdom-of-heaven-is-like.jpeg",
        "seg": "j1", "window": "18.192-22.090", "jesus": True, "ref": REF,
        "locks": ["GARDEN", "LISTENERS"],
        "narration": "The kingdom of heaven is like to a grain of mustard seed,",
        "must_show": "a closer photograph of Jesus on the cistern kerb mid-sentence, one hand turned palm-up in front of him as he names the kingdom of heaven, with a listener seated close in front of him.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no sunset colouring; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, clear bright "
            "late-morning sunlight from the upper left, fine film grain. THE CAMERA "
            "SHOOTS PAST THE SHOULDER OF A SEATED LISTENER, whose DEEP INDIGO shoulder "
            "and dark head cloth fill the near left of the frame out of focus, SO THAT "
            "JESUS'S GAZE HAS A NAMED TARGET INSIDE THE PICTURE — he is looking "
            "directly at that seated man, his eyeline running horizontally across the "
            "frame to the left and never toward the lens. Sharp in the middle, Jesus "
            "is framed from the waist up, seated on the low fieldstone kerb of the "
            "cistern with his body turned three-quarters toward that listener, his "
            "right hand lifted and turned palm-up in the explaining gesture, his lips "
            "parted mid-word, his expression warm and steady. Behind him a fired-clay "
            "water jar stands at the kerb and the dark raised beds and rough tan "
            "mud-brick wall fall away into soft blur under a bright sky."
        ),
    },
    {
        "id": "v2-r026-b07", "out": "s07-which-a-man-took-and-sowed.jpeg",
        "seg": "j1", "window": "22.090-25.110", "wide": True,
        "locks": ["GARDENER", "GARDEN"],
        "narration": "which a man took, and sowed in his field:",
        "must_show": "a wider photograph of the gardener alone at work in the bare corner bed of his walled garden in early-morning light, stooping over the turned soil, seen from behind and to one side.",
        "must_not_show": "no other person anywhere in the frame; no growing mustard plant, this bed is bare turned soil; no night, no lamp, no sunset colouring; no cream, off-white or pale garment anywhere in the frame; not one face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, clear low early-morning sun from the right "
            "throwing his long shadow across the beds, fine film grain. THE CAMERA "
            "STANDS INSIDE THE GATEWAY BEHIND HIM AND SHOOTS PAST HIM DOWN THE LENGTH "
            "OF THE GARDEN: his BACK and one shoulder fill the middle left of the "
            "frame, seen from behind and three-quarters, HIS FACE TURNED AWAY FROM THE "
            "CAMERA down toward the soil at his feet, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. He is the lean wiry man of about forty in the DEEP "
            "UMBER-BROWN wool tunic with the sleeves rolled to the elbow, the dark "
            "madder-red sash and the dark brown head cloth wound close, his "
            "medium-length dark brown beard just visible in profile as he stoops over "
            "the bare dark corner bed with a woven seed pouch open at his hip and one "
            "hand lowered to the soil. The near foreground is the sunlit beaten earth "
            "of the path and the shadowed top of a raised bed, with nobody standing or "
            "passing between the camera and him. Around him the narrow raised beds, "
            "the hand-cut watering channels, the stone-lined cistern with its two clay "
            "jars, the rough tan mud-brick walls and the plank gate; the flat mud "
            "roofs of the village show above one wall and low tawny hills beyond. He "
            "is the only person anywhere in the frame."
        ),
    },
    {
        "id": "v2-r026-b08", "out": "s08-the-least-of-all-seeds.jpeg",
        "seg": "j1", "window": "25.110-29.114",
        "locks": ["GARDEN", "MUSTARD-SEED"],
        "narration": "which indeed is the least of all seeds:",
        "must_show": "an extreme close photograph down in the bed itself of one tiny dark mustard grain lying alone in the shadow of a broken clod of damp earth many times its size, dwarfed by the soil around it.",
        "must_not_show": "no person, no hand, no face anywhere in the frame; no night, no lamp; no cream or pale cloth at any edge; the grain never glows and is never larger than a clod; no plant, no shoot, nothing growing yet.",
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, clear low "
            "early-morning sun from the right so the clods throw long hard shadows "
            "across the soil, fine film grain. THE CAMERA IS DOWN AT SOIL LEVEL "
            "LOOKING ALONG THE SURFACE OF THE BED and there is no person in the "
            "picture at all. Filling the frame are broken clods of dark damp tilled "
            "earth, each the size of a fist and rough with crumbs and root fibre. In "
            "the trough between two of them, sharp and alone and almost lost, lies ONE "
            "hard round DARK RED-BROWN mustard grain about one millimetre across, "
            "smaller than the smallest crumb of soil beside it. The near foreground is "
            "a single dark out-of-focus clod at the bottom edge. Behind, the ridged "
            "surface of the bed and the base of the rough tan mud-brick wall fall "
            "completely out of focus."
        ),
    },
    # ============================ KJV — verse 32, the grown plant ===============
    {
        "id": "v2-r026-b09", "out": "s09-but-when-it-is-grown.jpeg",
        "seg": "j1b", "window": "29.114-31.214", "jesus": True, "ref": REF,
        "locks": ["GARDEN", "MUSTARD-PLANT", "LISTENERS"],
        "narration": "but when it is grown, it is the greatest among herbs,",
        "must_show": "Jesus turning on the cistern kerb and lifting one open hand toward the tall mustard shrub standing in the far corner bed, his eyes following his own hand.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no sunset colouring; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, clear bright "
            "late-morning sunlight from the upper left, fine film grain. THE CAMERA "
            "SITS LOW AND WELL TO HIS RIGHT SIDE, SO HIS EYELINE RUNS HORIZONTALLY "
            "ACROSS THE FRAME AND OUT THROUGH THE LEFT EDGE toward a NAMED TARGET "
            "INSIDE THE PICTURE — the tall mustard shrub in the far corner bed, its "
            "crown catching the light at the upper left — and never toward the lens. "
            "Jesus is framed from the waist up, seated on the low fieldstone kerb of "
            "the cistern, his body turned away from the camera as he twists toward the "
            "plant, his left arm lifted and his hand open toward it, his chin raised "
            "and his gaze travelling up along his own arm. The near foreground is the "
            "empty sunlit beaten earth of the path and the shadowed rim of the "
            "cistern, with nobody standing, sitting or passing between the camera and "
            "him. Behind him the dark raised beds and the rough tan mud-brick wall "
            "fall away into soft blur, and the open crown of rough green leaves and "
            "small yellow flower sprays rises out of focus above the wall."
        ),
    },
    {
        "id": "v2-r026-b10", "out": "s10-greatest-among-herbs.jpeg",
        "seg": "j1b", "window": "31.214-35.194", "wide": True,
        "locks": ["GARDEN", "MUSTARD-PLANT"],
        "narration": "but when it is grown, it is the greatest among herbs, and becometh a tree,",
        "must_show": "a wide photograph of the full-grown mustard shrub standing three to four metres tall in the far corner bed, towering over the low herb beds and rising well above the mud-brick garden wall, so its size against everything else in the garden is unmistakable.",
        "must_not_show": "no person anywhere in the frame; no oak, fig, olive, palm or cedar and no massive buttressed trunk; no fruit of any kind; no night, no lamp, no sunset colouring; no cream or pale cloth anywhere; no seed, no bare bed.",
        "scene": (
            "One photograph, 28mm lens, clear bright late-morning sun from the upper "
            "left, hard short shadows on the beaten earth, fine film grain. THE CAMERA "
            "STANDS LOW ON THE PATH AT THE FAR END OF THE GARDEN AND SHOOTS ACROSS AND "
            "SLIGHTLY UPWARD toward the corner bed; there is no person in the picture "
            "at all and no face anywhere, so nothing is squared up to the lens. The "
            "full-grown black mustard shrub fills the right two-thirds of the frame, "
            "one woody stem as thick as a man's wrist rising from the dark soil and "
            "branching low into a spreading open crown three to four metres tall, its "
            "large rough lobed green leaves and loose sprays of small yellow "
            "four-petalled flowers bright against a clear pale sky, the crown standing "
            "a full body height above the top of the rough tan mud-brick wall behind "
            "it. Beside and below it the narrow raised beds carry only low knee-high "
            "herbs and greens, so the difference in size is plain. The near foreground "
            "is a shadowed raised bed of dark tilled soil and low green leaves at the "
            "bottom edge, with nothing pale in it. The stone-lined cistern, the plank "
            "gate, the flat mud village roofs above one wall and the low tawny hills "
            "beyond close the view."
        ),
    },
    {
        "id": "v2-r026-b11", "out": "s11-the-birds-of-the-air-come.jpeg",
        "seg": "j1b", "window": "35.194-37.714",
        "locks": ["GARDEN", "MUSTARD-PLANT", "BIRDS"],
        "narration": "so that the birds of the air come",
        "must_show": "small brown wild birds flying in low over the mud-brick garden wall toward the crown of the mustard shrub, wings open in mid-air.",
        "must_not_show": "no person anywhere in the frame; no raptor, dove, crow, stork or brightly coloured bird and no bird larger than a man's hand; no night, no lamp, no sunset colouring; no cream or pale cloth anywhere.",
        "scene": (
            "One photograph, 135mm lens, fast shutter, shallow depth of field, clear "
            "bright late-morning sun from behind the camera's left shoulder lighting "
            "the birds and the leaves from the front, fine film grain. THE CAMERA "
            "STANDS INSIDE THE GARDEN LOOKING UP AND ACROSS AT THE TOP OF THE WALL and "
            "there is no person in the picture at all. FIVE small wild birds — plain "
            "brown and grey-brown sparrows and linnets, each about a hand's length, "
            "separated in the air and individually countable — are crossing the frame "
            "from the left in level flight just above the rounded top of the rough tan "
            "mud-brick wall, wings open, legs tucked, every one of them heading toward "
            "the open crown of the mustard shrub at the right of the frame. The near "
            "foreground is a single out-of-focus dark green mustard leaf at the bottom "
            "right corner. Behind them a clear pale sky and the low tawny hills."
        ),
    },
    {
        "id": "v2-r026-b12", "out": "s12-lodge-in-the-branches-thereof.jpeg",
        "seg": "j1b", "window": "37.714-41.237",
        "locks": ["MUSTARD-PLANT", "BIRDS"],
        "narration": "and lodge in the branches thereof.",
        "must_show": "a close photograph up inside the crown of the mustard shrub where three small brown birds are settled on the springy branch forks among the rough green leaves and yellow flower sprays, one of them tucked down into a small nest of woven twigs.",
        "must_not_show": "no person, no hand, no face anywhere in the frame; no raptor, dove, crow or brightly coloured bird and no bird larger than a man's hand; no night, no lamp, no sunset colouring; no cream or pale cloth anywhere; no fruit of any kind.",
        "scene": (
            "One photograph, 135mm lens, shallow depth of field, clear bright "
            "late-morning sunlight coming down through the leaves in broken patches, "
            "fine film grain. THE CAMERA IS UP CLOSE INSIDE THE CROWN LOOKING SLIGHTLY "
            "UPWARD THROUGH THE BRANCHES and there is no person in the picture at all. "
            "Three small plain brown and streaked grey-brown wild birds, each about a "
            "hand's length and clearly separated so all three can be counted, are "
            "settled among the springy branch forks: one gripping a bare twig with "
            "both feet and its head turned to the right, one part hidden behind a "
            "large rough lobed green leaf, and one tucked down into a small round nest "
            "of woven dry twigs and grass wedged in a fork, only its head and back "
            "showing. Loose sprays of small yellow four-petalled flowers hang beside "
            "them. The near foreground is a broad out-of-focus green mustard leaf "
            "across the bottom left corner. Behind, the rest of the crown and a bright "
            "sky fall out of focus."
        ),
    },
    # ================== THE GROWING — the corner bed through the season =========
    {
        "id": "v2-r026-b13", "out": "s13-it-did-not-stay-small.jpeg",
        "seg": "n4", "window": "41.237-44.317",
        "locks": ["GARDEN"],
        "narration": "But that tiny seed did not stay small.",
        "must_show": "a low quiet photograph of the bare corner bed early in the morning with nothing at all showing above the soil yet, only the flat raked surface and the shadow of the garden wall lying across it.",
        "must_not_show": "no person, no hand, no face anywhere in the frame; no plant, shoot or green thing in the bed; no night, no lamp, no sunset colouring; no cream or pale cloth anywhere.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, clear low "
            "early-morning sun from the right, the long soft-edged shadow of the "
            "mud-brick wall lying across the near half of the bed, fine film grain. "
            "THE CAMERA IS DOWN AT SOIL LEVEL LOOKING ALONG THE LENGTH OF THE BED and "
            "there is no person in the picture at all. The dark raked soil of the "
            "corner bed runs away from the camera, faintly ridged and completely bare "
            "— not one shoot, not one green leaf anywhere on it. The near foreground "
            "is a single out-of-focus dark clod at the bottom edge. At the far end the "
            "shallow hand-cut watering channel, the base of the rough tan mud-brick "
            "wall and a fired-clay water jar stand soft and out of focus, with the "
            "flat mud roofs of the village showing above the wall."
        ),
    },
    {
        "id": "v2-r026-b14", "out": "s14-quietly-slowly-it-began-to-grow.jpeg",
        "seg": "n4", "window": "44.317-46.830",
        "locks": ["GARDEN"],
        "narration": "Quietly, slowly, it began to grow.",
        "must_show": "an extreme close photograph of one pale green seedling shoot pushing up through the crust of the dark soil, its two first leaves still bent over and carrying crumbs of earth on them.",
        "must_not_show": "no person, no hand, no face anywhere in the frame; no full-grown plant, no branches, no flowers, no birds; no night, no lamp, no sunset colouring; no cream or pale cloth anywhere.",
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, clear low "
            "early-morning sun from the right catching the translucent edges of the "
            "leaves, fine film grain. THE CAMERA IS DOWN AT SOIL LEVEL A HAND'S WIDTH "
            "FROM THE SHOOT and there is no person in the picture at all. Filling the "
            "centre of the frame, sharp against the dark crumbled earth, ONE pale "
            "yellow-green seedling on a thin hooked stem has broken the crust of the "
            "soil, its two first seed leaves still folded over and each carrying a few "
            "crumbs of dark earth on its surface, with the cracked ring of lifted soil "
            "crust around its base. The near foreground is a single out-of-focus dark "
            "clod at the bottom edge. Everything behind the shoot — the ridged bed and "
            "the base of the rough tan mud-brick wall — falls completely out of focus."
        ),
    },
    {
        "id": "v2-r026-b15", "out": "s15-higher-and-higher.jpeg",
        "seg": "n5", "window": "46.830-50.500",
        "locks": ["GARDEN"],
        "narration": "Up out of the ground, higher and higher,",
        "must_show": "the young mustard plant now waist high in the corner bed, a single green stem with broad rough leaves standing clearly taller than the low herbs in the beds beside it, in clear morning light.",
        "must_not_show": "no person, no hand, no face anywhere in the frame; no woody trunk, no full crown, no flowers, no birds — it is not grown yet; no night, no lamp, no sunset colouring; no cream or pale cloth anywhere.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, clear early-morning "
            "sun from the right laying warm light through the leaves so the veins "
            "show, fine film grain. THE CAMERA IS DOWN AT BED HEIGHT LOOKING SLIGHTLY "
            "UPWARD ALONG THE STEM and there is no person in the picture at all. In "
            "the corner bed a single young black mustard plant about waist high stands "
            "sharp in the middle of the frame, one green stem no thicker than a finger "
            "carrying six or seven broad rough lobed leaves that step up the stem and "
            "spread outward, its lowest leaves already above the knee-high herbs and "
            "greens filling the neighbouring beds. The near foreground is the shadowed "
            "dark soil of the bed and a low out-of-focus green herb leaf at the bottom "
            "left. Behind it the shallow watering channel and the rough tan mud-brick "
            "wall fall out of focus under a clear bright sky."
        ),
    },
    {
        "id": "v2-r026-b16", "out": "s16-a-tall-spreading-tree.jpeg",
        "seg": "n5", "window": "50.500-54.560", "wide": True,
        "locks": ["GARDEN", "MUSTARD-PLANT"],
        "narration": "until it became the largest plant in the whole garden — a tall, spreading tree.",
        "must_show": "a wide photograph looking up the woody stem of the full-grown mustard shrub into its spreading open crown, filling the sky above the whole garden.",
        "must_not_show": "no person anywhere in the frame; no oak, fig, olive, palm or cedar and no massive buttressed trunk; no fruit of any kind; no night, no lamp, no sunset colouring; no cream or pale cloth anywhere.",
        "scene": (
            "One photograph, 24mm lens, clear bright mid-morning sun coming down "
            "through the crown in hard broken shafts, fine film grain. THE CAMERA IS "
            "SET ON THE PATH AT THE FOOT OF THE PLANT LOOKING STEEPLY UPWARD PAST THE "
            "STEM into the crown, seeing the plant from the side; there is no person "
            "in the picture at all and no face "
            "anywhere, so nothing is squared up to the lens. The single woody main "
            "stem, as thick as a man's wrist and rough with grey-brown bark, rises "
            "from the dark soil at the bottom of the frame and branches low into a "
            "spreading open crown of large rough lobed green leaves and loose sprays "
            "of small yellow four-petalled flowers that fills the top two-thirds of "
            "the picture, daylight showing through the gaps between the springy "
            "branches. The near foreground is the dark tilled soil of the corner bed "
            "and a low out-of-focus green herb leaf at the bottom right. At the edges "
            "of the frame, well below the crown, the rounded top of the rough tan "
            "mud-brick wall and the low knee-high herb beds show how far above "
            "everything else it stands."
        ),
    },
    {
        "id": "v2-r026-b17", "out": "s17-the-wild-birds-came.jpeg",
        "seg": "n6", "window": "54.560-56.780", "wide": True,
        "locks": ["GARDEN", "MUSTARD-PLANT", "BIRDS"],
        "narration": "And the wild birds came",
        "must_show": "a wide photograph of the whole mustard shrub standing over the garden with a scattered handful of small brown birds coming in toward it from over the village roofs.",
        "must_not_show": "no person anywhere in the frame; no raptor, dove, crow, stork or brightly coloured bird and no bird larger than a man's hand; no night, no lamp, no sunset colouring; no cream or pale cloth anywhere.",
        "scene": (
            "One photograph, 35mm lens, clear bright late-morning sun from the upper "
            "left, fine film grain. THE CAMERA STANDS LOW ON THE PATH BESIDE THE "
            "CISTERN AND SHOOTS ACROSS THE GARDEN toward the corner bed, seeing the "
            "plant from the side; there is no "
            "person in the picture at all and no face anywhere, so nothing is squared "
            "up to the lens. The full-grown mustard shrub stands in the right half of "
            "the frame, its woody stem and spreading open crown of rough green leaves "
            "and yellow flower sprays rising a body height above the rough tan "
            "mud-brick wall. SIX small plain brown and grey-brown wild birds, each "
            "about a hand's length and clearly separated so every one can be counted, "
            "are strung across the sky in flight, wings open, all of them converging "
            "on the crown from over the flat mud roofs of the village at the upper "
            "left. The near foreground is a shadowed raised bed of dark soil and low "
            "green herbs across the bottom edge, with nothing pale in it. The "
            "stone-lined cistern with its two fired-clay jars stands at the near left "
            "and the low tawny hills close the horizon."
        ),
    },
    {
        "id": "v2-r026-b18", "out": "s18-built-their-nests.jpeg",
        "seg": "n6", "window": "56.780-59.724",
        "locks": ["MUSTARD-PLANT", "BIRDS"],
        "narration": "and built their nests in its broad, sheltering branches.",
        "must_show": "a close photograph of a small round nest of woven dry twigs and grass wedged in a fork of the mustard branches, with a parent bird standing on its rim and the open beaks of nestlings showing inside.",
        "must_not_show": "no person, no hand, no face anywhere in the frame; no raptor, dove, crow or brightly coloured bird and no bird larger than a man's hand; no night, no lamp, no sunset colouring; no cream or pale cloth anywhere; no fruit of any kind.",
        "scene": (
            "One photograph, 135mm lens, very shallow depth of field, clear bright "
            "late-morning sunlight filtering down through the leaves onto the nest, "
            "fine film grain. THE CAMERA IS UP IN THE CROWN LEVEL WITH THE NEST AND "
            "SLIGHTLY TO ONE SIDE and there is no person in the picture at all. Sharp "
            "in the centre, a small round nest of woven dry twigs, grass stems and "
            "root fibre is wedged into a three-way fork of springy mustard branches. "
            "ONE plain brown parent bird about a hand's length stands on the rim of "
            "the nest with both feet gripping the woven edge, its head turned down and "
            "to the right toward the nest cup, where THREE small nestlings with wide "
            "open beaks reach up out of the nest, each one separately visible and "
            "countable. Large rough lobed green leaves and a spray of small yellow "
            "flowers frame the nest. The near foreground is a broad out-of-focus dark "
            "green mustard leaf across the bottom right corner. Behind, the rest of "
            "the crown and a bright sky fall completely out of focus."
        ),
    },
    # ================== FRAME — the close, back in the garden ===================
    {
        "id": "v2-r026-b19", "out": "s19-what-gods-kingdom-is-like.jpeg",
        "seg": "n7", "window": "59.724-63.369", "jesus": True, "ref": REF,
        "locks": ["GARDEN", "LISTENERS"],
        "narration": "That, Jesus said, is what God's kingdom is like.",
        "must_show": "Jesus lowering his hand and looking back at the listeners in front of him, quiet and certain, the point made.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no sunset colouring; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, clear bright "
            "late-morning sunlight from the upper left modelling one side of his face, "
            "fine film grain. THE CAMERA SHOOTS OVER THE SHOULDER OF A SEATED "
            "LISTENER, whose DARK UMBER back and dark brown head cloth fill the near "
            "right of the frame out of focus, SO THAT JESUS'S GAZE HAS A NAMED TARGET "
            "INSIDE THE PICTURE — he is looking directly at that seated man, his "
            "eyeline running horizontally across the frame to the right and never "
            "toward the lens. Sharp in the middle, Jesus is framed from the chest up, "
            "seated on the low fieldstone kerb of the cistern, his lifted hand now "
            "lowered and resting open on his knee, his head slightly inclined toward "
            "the man, his mouth closed and his expression quiet, warm and certain. "
            "Behind him a fired-clay water jar, the dark raised beds and the rough tan "
            "mud-brick wall fall away into soft warm blur under a bright sky."
        ),
    },
    {
        "id": "v2-r026-b20", "out": "s20-it-almost-never-begins-big.jpeg",
        "seg": "n8", "window": "63.369-65.709",
        "locks": ["GARDEN", "LISTENERS"],
        "narration": "It almost never begins big.",
        "must_show": "a close photograph of one listener's face in the garden, a middle-aged woman sitting on the edge of a raised bed, taking the words in, her eyes lowered in thought.",
        "must_not_show": "no Jesus in this frame; no halo, glow or rim-light anywhere; no night, no lamp, no sunset colouring; no cream, off-white or pale cloth on her or anywhere at the edges of the frame; her pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, very shallow depth of field, clear bright "
            "late-morning sunlight from the upper left, fine film grain. THE CAMERA IS "
            "LEVEL AND WELL TO HER LEFT SIDE, SO HER EYELINE RUNS DOWNWARD AND ACROSS "
            "TO A NAMED TARGET INSIDE THE PICTURE — her own hands folded in her lap at "
            "the bottom left of the frame — and her pupils are never centred on the "
            "lens. She is framed from the chest up, a Galilean village woman of about "
            "forty-five with warm sun-browned olive skin, a lined thoughtful face and "
            "dark hair covered by a DARK MADDER-BROWN head cloth, in a RUSSET-RED wool "
            "mantle, seated on the edge of a raised bed with her shoulders still and "
            "her lips closed. The near foreground is the shadowed dark soil and low "
            "green herbs of the bed in front of her, with nothing pale in it. Behind "
            "her the beaten earth path, the rough tan mud-brick wall and the blurred "
            "dark shapes of other seated villagers fall out of focus."
        ),
    },
    {
        "id": "v2-r026-b21", "out": "s21-a-whispered-prayer.jpeg",
        "seg": "n8", "window": "65.709-68.569",
        "locks": ["GARDEN", "LISTENERS"],
        "narration": "It begins small — a whispered prayer,",
        "must_show": "a quiet photograph of a young man kneeling alone at the foot of the mud-brick garden wall with his head bowed and his hands closed together at his forehead, praying under his breath.",
        "must_not_show": "no Jesus in this frame; no halo, glow or rim-light anywhere; no night, no lamp, no sunset colouring; no cream, off-white or pale cloth on him or anywhere at the edges of the frame; no face turned toward the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, clear bright "
            "late-morning sunlight from the upper left, the wall throwing a soft-edged "
            "band of shade across him, fine film grain. THE CAMERA STANDS BACK ON THE "
            "PATH AND SHOOTS HIM IN THREE-QUARTER FROM BEHIND AND TO ONE SIDE, HIS "
            "FACE TURNED AWAY FROM THE CAMERA AND BOWED TOWARD HIS OWN CLOSED HANDS, "
            "so no face is turned toward the lens. He is a young Galilean man of about "
            "twenty-five with sun-browned olive skin, short dark hair and a short dark "
            "beard, in a DEEP INDIGO wool tunic with a dark cord at the waist, "
            "kneeling on both knees on the beaten earth at the foot of the rough tan "
            "mud-brick wall, his back rounded, his elbows drawn in and both hands "
            "closed together and pressed to his forehead, his lips just parted. He is "
            "the only person in the picture. The near foreground is a shadowed raised "
            "bed of dark soil and low green herbs across the bottom edge, with nothing "
            "pale in it. Behind him the sunlit wall and a fired-clay jar at its base."
        ),
    },
    {
        "id": "v2-r026-b22", "out": "s22-a-single-kind-act.jpeg",
        "seg": "n8", "window": "68.569-72.230",
        "locks": ["GARDEN", "LISTENERS"],
        "narration": "a single kind act, one quiet change of heart.",
        "must_show": "a young woman crouching beside the cistern to steady a shallow clay cup of water into the shaking hands of a very old man seated on the kerb, both of their eyes on the cup between them.",
        "must_not_show": "no Jesus in this frame; no halo, glow or rim-light anywhere; no night, no lamp, no sunset colouring; no cream, off-white or pale cloth on either of them or anywhere at the edges of the frame; neither of their pupils centred on the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, clear bright "
            "late-morning sunlight from the upper left, fine film grain. THE CAMERA IS "
            "DOWN AT KERB HEIGHT AND WELL TO ONE SIDE, SHOOTING BOTH OF THEM IN "
            "PROFILE FROM THE SIDE SO THEIR EYELINES RUN HORIZONTALLY TOWARD EACH "
            "OTHER ACROSS THE FRAME. BOTH GAZES HAVE THE SAME NAMED TARGET INSIDE THE "
            "PICTURE: the shallow fired-clay cup of water held between them at the "
            "centre of the frame, so both faces are turned down and inward and neither "
            "pair of pupils is anywhere near the lens. On the left, a young Galilean "
            "woman of about twenty with sun-browned olive skin and dark hair under a "
            "DARK MADDER-BROWN head cloth, in a RUSSET-RED wool mantle, crouches on "
            "the path with both her hands closed around the old man's hands to steady "
            "them. On the right, a very old man with a deeply lined face, a thin white "
            "beard and a DEEP INDIGO wool mantle over a DARK UMBER tunic sits on the "
            "low fieldstone kerb of the cistern, his knotted hands shaking around the "
            "cup. The near foreground is the shadowed dark stone rim of the cistern "
            "across the bottom edge. Behind them the rough tan mud-brick wall and the "
            "dark raised beds fall out of focus."
        ),
    },
    {
        "id": "v2-r026-b23", "out": "s23-god-takes-that-smallest-beginning.jpeg",
        "seg": "n9", "window": "72.230-75.150",
        "locks": ["GARDEN", "MUSTARD-PLANT"],
        "narration": "But God takes that smallest beginning",
        "must_show": "a close photograph low at the foot of the mustard shrub where the thick woody stem comes out of the dark soil of the corner bed, the whole weight of the plant rising from that one small point.",
        "must_not_show": "no person, no hand, no face anywhere in the frame; no oak, fig, olive, palm or cedar and no massive buttressed trunk; no fruit of any kind; no night, no lamp, no sunset colouring; no cream or pale cloth anywhere.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, clear bright "
            "late-morning sunlight coming down through the crown and falling in broken "
            "patches on the soil, fine film grain. THE CAMERA IS DOWN AT SOIL LEVEL A "
            "PACE FROM THE STEM, LOOKING SLIGHTLY UPWARD ALONG IT, and there is no "
            "person in the picture at all. Sharp in the centre, the single woody main "
            "stem of the mustard shrub, as thick as a man's wrist and rough with "
            "grey-brown bark, comes straight out of the dark tilled soil of the corner "
            "bed, the earth around its base cracked and ringed where the stem has "
            "swelled. Above it the stem branches low and the spreading open crown of "
            "rough green leaves and small yellow flower sprays runs up out of focus "
            "toward the top of the frame. The near foreground is a broken dark clod of "
            "soil at the bottom edge, in the same sharp focus as the stem, so the "
            "smallness of the point it grew from is readable. Behind it the shallow "
            "watering channel and the rough tan mud-brick wall fall out of focus."
        ),
    },
    {
        "id": "v2-r026-b24", "out": "s24-far-greater-than-anyone-imagined.jpeg",
        "seg": "n9", "window": "75.150-79.419", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GARDEN", "MUSTARD-PLANT", "LISTENERS"],
        "narration": "and grows it into something far greater than anyone could have imagined.",
        "must_show": "a wide photograph of the whole garden with Jesus and the seated listeners small at the near end and the full-grown mustard shrub towering over all of them at the far corner, the size difference doing the work of the sentence.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no oak, fig, olive, palm or cedar and no massive buttressed trunk; no night, no lamp, no sunset colouring; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; not one face turned toward the lens.",
        "scene": (
            "One photograph, 24mm lens, clear bright late-morning sun from the upper "
            "left, short hard shadows across the beaten earth paths, fine film grain. "
            "THE CAMERA STANDS INSIDE THE GATEWAY BEHIND THE SEATED LISTENERS AND "
            "SHOOTS PAST THEM DOWN THE LENGTH OF THE GARDEN: their BACKS and dark head "
            "cloths fill the near bottom third of the frame, soft and out of focus, a "
            "DEEP INDIGO back at the near left and a DARK UMBER back at the near "
            "right, and NOT ONE FACE IS TURNED TOWARD THE LENS. Beyond them, small in "
            "the middle distance but sharp, Jesus sits on the low fieldstone kerb of "
            "the cistern with the villagers gathered on the bed edges and paths around "
            "him, his head turned to his right toward them and his gaze running along "
            "the seated row, well away from the camera. Rising over all of them at the "
            "far right corner of the garden, the full-grown black mustard shrub "
            "carries its woody stem and spreading open crown of rough green leaves and "
            "small yellow flower sprays a full body height above the rough tan "
            "mud-brick wall, dwarfing every person in the picture. The narrow raised "
            "beds, the hand-cut watering channels and the two fired-clay jars at the "
            "cistern fill the ground between, the flat mud roofs of the village show "
            "above one wall and low tawny hills close the horizon."
        ),
    },
]
