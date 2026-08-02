#!/usr/bin/env python3
"""V2 beat map — row 21, build-21-lost-sheep (Luke 15:1-7), realistic rebuild.

COVERAGE: 33 pictures against V1's SEVEN, over 138.17 s = 4.19 s/picture. V1 held
`s7-rejoicing.jpeg` on screen from 96.6 s to 138.5 s — nearly 42 SECONDS on one
picture, across four separate segments.

⚠️ WINDOWS WERE COMPUTED FROM SCRATCH 2026-08-02 (Claude worker 15) with the fixed
`extract_beats.py` reading the V1 build, then split inside each segment on its own
`audio/*.timing.json` phrase boundaries. Contiguous 0.28 s → 138.451 s (the card
start), zero gaps, zero overlaps. Extracted total 147.232 s against the V1 mp4's
147.237 s.

⚠️ SOURCING CHECK DONE (the row-20 trap). This build carries BOTH a
`make_narration.py.pre-echo` and a `.pre-speaker` sibling. The live script and
`.pre-echo` DISAGREE on exactly one segment — n9b, where `.pre-echo` has a longer
line ("I have found my sheep, the one that was lost… My sheep."). The shipped mp3
was transcribed with faster-whisper to settle it:

    n9b audio actually says: "Be glad with me, he tells them. Not I got my property
    back. It was his the whole time it was missing."

which is the LIVE script, not `.pre-echo`. Its `timing.json` agrees (3 phrases,
5.759 s against a 5.799 s file). So the live script is authoritative on this row and
NO `TEXT_OVERRIDES` are needed.

⚠️ THE SAME FRAME-STORY OCCASION AS ROW 2 AND ROW 8. Luke 15 holds all three
parables — prodigal (row 2), lost coin (row 8) and this one — told at one sitting to
one audience, so the library must not print the same opening picture three times.
Row 2 staged an outdoor COURTYARD TABLE with three standing Pharisees; row 8 staged
Jesus seated on a LOW WALL UNDER A FIG TREE. This build is staged INSIDE a village
house at a crowded meal, with the religious men standing out in the open DOORWAY,
looking in and refusing to cross the threshold — which is also the truest reading of
Luke 15:2, because the offence is specifically that he EATS with them.

⚠️ TIME OF DAY IS THE STORY'S OWN CLOCK, and the parable runs a full night:
  b01-b07, b29-b33   the FRAME story — inside the house, mid-afternoon daylight
                     coming through the open doorway and the high window slot. One
                     continuous afternoon; never night, never a sunset sky, and NO
                     LAMP IS EVER LIT because it is broad daylight outside.
  b08-b13            DUSK at the sheepfold — the last cold blue-grey light after the
                     sun is down, no colour left in the sky.
  b14-b19            deep NIGHT in the wilderness — moonlight and starlight only,
                     plus one pitch-pine torch. Nothing else is lit.
  b20-b23            FIRST LIGHT — thin level grey-gold light from the east, long
                     shadows, mist lying in the low ground.
  b24-b28            full MORNING in the village.
No sunset palette anywhere: the parable's evening is a working dusk, not a sky.

SCRIPTURE FACTS (Luke 15:1-7 KJV):
  v1  "Then drew near unto him all the publicans and sinners for to hear him." The
      outcasts come CLOSE — the frame story is a crowded shared meal, not a lecture.
  v2  "This man receiveth sinners, and EATETH WITH THEM." Food is the offence, so
      food is on screen: bread, a common dish, hands reaching into it.
  v4  "leave the ninety and nine IN THE WILDERNESS." He does not pen them somewhere
      safe first — he leaves them out in open country, which is the risk of the
      story.
  v4  "and go after that which is lost, UNTIL HE FIND IT." The search is long. Three
      night frames carry it.
  v5  "he layeth it on his SHOULDERS, rejoicing." Both shoulders, across the back of
      the neck, legs gathered at the chest — the real carry — and he is already
      rejoicing as he takes the weight, not merely relieved.
  v6  "he calleth together his FRIENDS AND NEIGHBOURS." A whole village turns out.
  v7  "joy shall be in heaven over ONE sinner that repenteth." The last frames go
      back to the faces of the actual publicans at the actual meal.

COUNTING — DELIBERATE. The narration names a hundred and a ninety-nine, and the
shared COUNT-AS-GEOMETRY lock would otherwise push the model to lay out a countable
hundred sheep, which is impossible and renders as a tiled carpet of clones. Every
flock frame therefore states POSITIVELY what the flock IS: a crowded moving mass of
backs that runs out of the frame on both sides, no number implied. The only
countable thing in this video is ONE sheep, which is the whole point of the parable.

CONTENT-CARE: GREEN. No violence and no blood; the found sheep is exhausted, filthy
and snagged in thorns, never injured on camera.

CAST NOTE — ANCHOR-FIRST (the row-20 lesson that took the reroll rate to 12 %).
THREE beats are generated FIRST, in their own separate process invocation, as
face-showing identity anchors — b02 (the publican), b04 (the chief Pharisee) and
b08 (the shepherd) — and each accepted anchor is then wired into REFS so every later
frame naming that lock gets the image attached. `v2_gen_api` builds its REFS cache
ONCE per run, so an anchor generated in the same run as its own dependants is
invisible to them. Every beat naming a recurring person ALSO restates his age, hair,
build and garment colour in its own scene text, because a face sheet does not hold a
character who is small in frame (row 19, PETER-HOLD).
"""

LOCKS = {
    # ------------------------------------------------------------ people ----
    "SHEPHERD": (
        "SHEPHERD LOCK: one working Judean shepherd of about THIRTY-FIVE — never "
        "old, never grey, never white-bearded. He is lean, broad-shouldered and "
        "weather-hardened, sun-darkened to a deep brown at the face, neck and "
        "forearms, with thick black hair to the jaw pushed back off his forehead and "
        "a short full black beard with no grey in it at all. He has a straight nose, "
        "a heavy brow and dark brown eyes set deep from squinting into distance. He "
        "wears a short knee-length tunic of coarse undyed DARK EARTH-BROWN wool, "
        "worn thin at the shoulder, with a wide folded rust-brown cloth sash knotted "
        "at the waist, a rolled coarse DARK UMBER-BROWN wool mantle slung across one "
        "shoulder, and hard-worn dark leather sandals. HE WEARS NO SHEEPSKIN, NO "
        "FLEECE-LINED GARMENT AND NOTHING PALE, WHITE OR CREAM-COLOURED ANYWHERE ON "
        "HIS BODY — every piece of cloth on him is dark brown or rust-brown. He carries a long "
        "hand-cut olivewood staff with a natural crook, its wood polished dark by his "
        "hands. HE IS NEVER IN CREAM, OFF-WHITE, IVORY OR ANY NEAR-WHITE CLOTH. He is "
        "the same man, same age, same black hair and beard, same brown tunic in every "
        "frame he appears in, near or far, sharp or blurred, front or back, and he is "
        "never aged, greyed, thinned, or replaced by another man."
    ),
    "PHARISEE": (
        "PHARISEE LOCK: one religious teacher of about FIFTY-FIVE, and he is the "
        "same man every time. Tall and upright, well fed and well kept, with a full "
        "square iron-grey beard combed flat, grey hair under a neatly folded "
        "DARK BLUE-GREY head-cloth held by a twisted cord, a smooth unweathered face "
        "and cold appraising deep-set brown eyes. He wears a long fine DEEP "
        "INDIGO-BLUE wool robe, clean and closely woven, with a broad indigo mantle "
        "bearing two narrow woven bands of dark madder red near the hem and knotted "
        "tassels at its four corners, and good dark leather sandals. HE IS NEVER IN "
        "CREAM, OFF-WHITE, IVORY OR ANY NEAR-WHITE CLOTH. Same man, same iron-grey "
        "beard, same indigo robe in every frame."
    ),
    "SCRIBE": (
        "SECOND RELIGIOUS MAN LOCK: one scribe of about FORTY who stands beside the "
        "Pharisee and is clearly a DIFFERENT man — shorter, slighter, with a narrow "
        "clean-boned face, a close-trimmed black beard along the jaw with no grey, "
        "black hair cropped short under a plain DARK OLIVE-GREEN head-cloth, and a "
        "tight anxious mouth. He wears a long DARK OLIVE-GREEN wool robe with a "
        "rust-brown sash and a rust-brown mantle held closed in one fist. HE IS NEVER "
        "IN CREAM, OFF-WHITE OR ANY NEAR-WHITE CLOTH, his face is never given to the "
        "Pharisee, and the Pharisee's face is never given to him."
    ),
    "PUBLICAN": (
        "PUBLICAN LOCK: one tax collector of about THIRTY-EIGHT — a heavy-set man "
        "with a thick neck, a fleshy weathered face, a broad flattened nose and short "
        "curly black hair receding at the temples, with a full black beard trimmed "
        "close. His skin is warm olive-brown. He is prosperous and out of place: a "
        "good but plain robe of DEEP RUST-RED wool with a wide dull ochre sash, a "
        "small hand-forged bronze weight on a cord at his belt, and good leather "
        "sandals. HE IS NEVER IN CREAM, OFF-WHITE OR ANY NEAR-WHITE CLOTH. His face "
        "carries the specific expression of a man who expected to be told to leave "
        "and has not been. Same man, same face, same rust-red robe in every frame."
    ),
    "OUTCASTS": (
        "OUTCASTS LOCK: the people crowded in around the meal are ordinary working "
        "Galileans and people the town has written off — men and women of every age "
        "between twenty and sixty, a labourer with cracked hands, a woman with her "
        "head covered, a young man with a scarred cheek, a second tax collector. "
        "EVERY GARMENT, HEAD-CLOTH, SHAWL AND MANTLE IN THE FRAME, including the "
        "large out-of-focus ones and the ones cut off by the frame edges, is a named "
        "saturated earth colour — umber brown, madder red, dull ochre, olive green, "
        "indigo, soot grey or undyed grey-brown wool. NOT ONE OF THEM WEARS CREAM, "
        "OFF-WHITE, IVORY OR ANY NEAR-WHITE CLOTH; a pale shoulder at the edge of the "
        "frame reads as a second, unlocked Jesus and fails the picture. They lean IN "
        "toward the centre, close enough to touch, never arranged in a neat ring "
        "facing outward."
    ),
    "VILLAGERS": (
        "VILLAGERS LOCK: the shepherd's friends and neighbours are a working hill "
        "village — men, women, old people and children of every age, barefoot or in "
        "worn leather sandals. EVERY tunic, mantle, head-cloth and shawl in the "
        "frame, near or far, sharp or blurred, whole or cut off by the frame edge, is "
        "a named saturated earth colour: umber brown, madder red, dull ochre, olive "
        "green, indigo or undyed grey-brown wool. NOBODY IN THE FRAME WEARS CREAM, "
        "OFF-WHITE, IVORY OR ANY NEAR-WHITE CLOTH. Their joy is physical and unposed "
        "— hands raised, arms around shoulders, a child running, people talking over "
        "one another."
    ),
    # ------------------------------------------------------------ animals ----
    "FLOCK": (
        "FLOCK LOCK: Near Eastern fat-tailed Awassi sheep as they actually are, not "
        "white show sheep. Their fleece is dirty grey-brown, tawny and dark umber, "
        "matted and dusty, with brown or black faces and legs, long drooping ears and "
        "heavy fat tails. Rams carry curled horns; the ewes do not. NUMBERS ARE NOT "
        "THE SUBJECT OF THIS PICTURE AND NO NUMBER IS COUNTABLE IN IT: the flock is "
        "one crowded moving mass of backs and shoulders that runs straight out of the "
        "frame on both sides and into the dark or the haze at the back, so no viewer "
        "could or should count them, and they are never laid out in a countable grid, "
        "row or tidy arc. No two sheep are identical copies of each other."
    ),
    "ONE-SHEEP": (
        "LOST-SHEEP LOCK: ONE single ewe, alone, and never more than one — a young "
        "fat-tailed Awassi ewe with dirty tawny-grey matted fleece, a dark brown face "
        "and dark legs, long drooping ears, no horns, and a distinctive dark brown "
        "patch over her right shoulder that is present in every frame she appears in. "
        "She is exhausted and filthy: dust caked into the fleece, dry thorn twigs and "
        "burrs snagged along her flank, her eyes wide and her breathing hard. She is "
        "never bleeding, never wounded, never injured — only worn out and afraid. "
        "Exactly one sheep and no second sheep anywhere in the frames that name this "
        "lock."
    ),
    # ------------------------------------------------------------ places ----
    "HOUSE-MEAL": (
        "HOUSE-MEAL LOCK: the single room of a poor Galilean village house at a "
        "crowded midday meal — walls of undressed limestone rubble under mud plaster, "
        "a beaten earth floor, a low ceiling of rough wooden beams with brush and "
        "packed earth above, and a raised stone ledge along one wall. People sit on "
        "coarse woven mats on the floor around a low plank table barely a foot high. "
        "On the table: torn flat barley loaves, a shallow fired clay dish of stew, a "
        "clay jug, salt in a pottery shard, a bowl of olives. IT IS BROAD DAYLIGHT "
        "AND THE ONLY LIGHT IN THE ROOM IS DAYLIGHT: a hard bright wedge of "
        "afternoon sun coming through the one open doorway with its woven door-cloth "
        "pushed aside, plus a narrow shaft from a small high window slot, with the "
        "corners of the room falling to deep warm shadow and dust turning in the "
        "beams. NO LAMP IS LIT ANYWHERE IN THE FRAME and there is no candle, no "
        "glass, no lantern, no hanging fixture and no light without a visible source. "
        "Everything in the room is hand-made — fired clay, hewn and pegged wood, "
        "woven flax, hand-forged iron. EVERY TUNIC, MANTLE, SASH, HEAD-CLOTH AND "
        "SHAWL WORN BY ANYONE IN THIS ROOM, near or far, sharp or blurred, whole or "
        "cut off by the frame edge, is a named saturated earth colour — umber brown, "
        "madder red, dull ochre, olive green, indigo or soot grey — and NOT ONE of "
        "them is cream, off-white, ivory, oatmeal, pale beige or any near-white "
        "cloth."
    ),
    "DOORWAY": (
        "DOORWAY LOCK: the house's one doorway is a low crooked opening in a thick "
        "rubble-stone wall with a heavy hewn timber lintel and a worn stone "
        "threshold, its woven umber door-cloth pushed back to one side on a peg. "
        "Beyond it, out in the hard bright afternoon, is the village lane: beaten "
        "dust, a dry-stone terrace wall and a fig tree. Men standing OUTSIDE that "
        "doorway are backlit by the daylight behind them and their faces sit in soft "
        "shade, while the room they refuse to enter is dim and warm. NOTHING ON THE "
        "DOOR IS MANUFACTURED: no hinge, no bolt, no lock, no nail heads, no metal "
        "fitting, no sawn plank."
    ),
    "FOLD": (
        "SHEEPFOLD LOCK: a hillside sheepfold on the high pasture — a rough dry-stone "
        "wall of stacked unmortared limestone about chest high, laid in a rough oval, "
        "with a single gap for a gateway closed by piled thorn brush. Bare stony hill "
        "pasture outside it: thin dry grass, exposed pale limestone shelves, "
        "scattered boulders, low thorn scrub, a few wind-bent terebinth trees. The "
        "ground inside the wall is trodden to dust. Nothing in the frame is "
        "manufactured — no wire, no nails, no sawn timber, no gate hardware, no fence "
        "posts."
    ),
    "WILDERNESS": (
        "JUDEAN-WILDERNESS LOCK: bare, dry, broken hill country falling away ridge "
        "after ridge into deep steep-sided ravines — pale limestone shelves, loose "
        "scree, dry watercourses in the bottoms, thorn scrub and a few wind-shaped "
        "terebinths clinging to the slopes. There is no cultivated ground, no road, "
        "no building, no wall and no other person anywhere in these frames: the "
        "emptiness is the point. Great physical scale — a human figure is small "
        "against the ridges."
    ),
    "NIGHT-LAW": (
        "NIGHT-LIGHT LOCK: this frame is deep night in open country and the ONLY "
        "light sources in it are a bright moon high and behind, a sky thick with real "
        "stars, and — where the scene says so — one burning pitch-pine torch of split "
        "resinous wood with a real ragged flame and drifting sparks. Moonlight "
        "renders the limestone cold silver-grey and the shadows near black; skin lit "
        "only by the moon is cool and desaturated, while skin lit by the torch is "
        "warm orange on one side only. There is no other light in the picture: no "
        "lantern, no lamp with a glass chimney, no candle, no fire outside the frame "
        "lighting everything evenly, no light without a visible source, and no light "
        "coming off any person."
    ),
    "VILLAGE": (
        "HILL-VILLAGE LOCK: a small Galilean hill village of a dozen houses — "
        "single-storey boxes of undressed limestone rubble and mud plaster with flat "
        "roofs of packed earth over wooden beams and brush, low crooked doorways "
        "closed by hanging woven cloth, external stone stairs against a side wall, a "
        "stone-kerbed well, a threshing floor of beaten rock. Fig and olive trees "
        "between the houses, dry stone terrace walls up the slope behind. THE SKYLINE "
        "BEHIND THE VILLAGE IS BARE HILL AND OPEN SKY: no dome, no minaret, no tower, "
        "no bell tower, no arch, no tiled roof, no plastered white walls, no city "
        "wall, and no aerial, pole or wire of any kind."
    ),
}

# The V1 script is authoritative on this row — the transcript check is in the
# docstring above — so nothing is overridden.
TEXT_OVERRIDES = {}

# Anchor-first casting. These paths are the OUTPUTS of b02 / b04 / b08, which are
# generated in their own separate run; until they exist the generator prints
# "character lock MISSING (skipped)" and carries on, which is exactly why the anchor
# run must come first and must be its own process invocation.
REFS = {
    "PUBLICAN": "assets/s02-drew-near-to-hear-him.jpeg",
    "PHARISEE": "assets/s04-receiveth-sinners.jpeg",
    "SHEPHERD": "assets/s08-one-of-them-missing.jpeg",
}

BEATS = [
    # ======================================= FRAME STORY — inside the house ====
    {
        "id": "v2-r021-b01", "out": "s01-they-drew-near.jpeg", "seg": "n1",
        "window": "0.28-4.30", "wide": True, "jesus": True, "ref": True,
        "locks": ["OUTCASTS", "HOUSE-MEAL"],
        "narration": "The people everyone else had written off kept crowding in close to hear Jesus.",
        "must_show": "a crowded low table inside a village house with Jesus seated on the floor among ordinary working people and tax collectors who are leaning IN toward him, close enough to touch, listening while they eat.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off Jesus; no synagogue, no temple, no raised platform, no lamp burning, no cream or off-white cloth on anybody but Jesus, and nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, mid-afternoon daylight, fine film grain. THE "
            "CAMERA SITS LOW INSIDE THE ROOM BEHIND THE NEAR SIDE OF THE TABLE AND "
            "SHOOTS PAST THE BACKS of two seated listeners: their shoulders and the "
            "backs of their heads fill the near left and near right of the frame, out "
            "of focus, and NOT ONE FACE IS TURNED TOWARD THE LENS. Between them, "
            "across the low plank table with its torn barley loaves and shallow clay "
            "dish, Jesus sits on a woven mat on the beaten earth floor, sharp, "
            "mid-sentence, one hand open and low over the bread. Eight or nine "
            "working people and two prosperous tax collectors are pressed in around "
            "him on the floor, all leaning inward; one man is reaching into the "
            "common dish without looking at it because he is watching Jesus. A hard "
            "bright wedge of afternoon sun comes through the open doorway behind "
            "Jesus and lies across the floor and the table, and the dust turns in it; "
            "the corners of the room fall away to deep warm shadow."
        ),
    },
    {
        "id": "v2-r021-b02", "out": "s02-drew-near-to-hear-him.jpeg", "seg": "n1",
        "window": "4.30-8.837", "wide": False, "jesus": False, "ref": False,
        "locks": ["PUBLICAN", "HOUSE-MEAL"],
        "narration": "The cheats, the outcasts, the ones with a past — crowding in close.",
        "must_show": "a sharply readable close study of the tax collector's FACE listening — this frame is the identity anchor for him and every feature must be plainly legible.",
        "must_not_show": "Jesus is not in this frame. No cream or off-white cloth anywhere, no other face in focus, no lamp burning, and his pupils are nowhere near the lens.",
        "scene": (
            "One photograph, 85mm prime lens at f/2, shallow depth of field, "
            "mid-afternoon daylight, fine grain. Tight on the tax collector from the "
            "chest up, seated on the floor and turned three quarters to his own left "
            "so his face is fully lit and fully readable — a heavy-set man of "
            "thirty-eight, thick neck, fleshy weathered olive-brown face, broad "
            "flattened nose, short receding curly black hair, close-trimmed black "
            "beard, deep rust-red robe with a dull ochre sash. He has stopped eating. "
            "His mouth is slightly open, his chin is down, and his eyes are lifted "
            "and fixed on someone seated lower and further away to his left, so his "
            "gaze travels up and out through the LEFT edge of the frame, well off the "
            "camera axis. The hard shaft of daylight from the doorway crosses his "
            "cheek from behind his right shoulder and picks out the curls at his "
            "temple; the dim room and the other diners behind him are a soft "
            "unreadable wash of brown and ochre. He has one head and two complete "
            "hands."
        ),
    },
    {
        "id": "v2-r021-b03", "out": "s03-the-religious-men-muttered.jpeg", "seg": "n2",
        "window": "8.837-12.005", "wide": True, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "SCRIBE", "OUTCASTS", "HOUSE-MEAL", "DOORWAY"],
        "narration": "And the religious men muttered about it.",
        "must_show": "the Pharisee and the scribe standing OUTSIDE in the bright doorway, framed by it, refusing to cross the threshold into the meal they are watching.",
        "must_not_show": "Jesus is not in this frame. Nobody is shouting or pointing; no cream or off-white cloth anywhere; no lamp burning; no face turned toward the lens.",
        "scene": (
            "One photograph, 50mm lens, mid-afternoon, fine grain. THE CAMERA STANDS "
            "INSIDE THE DIM ROOM BEHIND THE SEATED MEAL AND SHOOTS PAST THE BACKS of "
            "the seated people toward the bright doorway: the near third of the frame "
            "is out-of-focus seated backs and shoulders in umber and madder red, and "
            "NOT ONE FACE IS TURNED TOWARD THE LENS. Out in the doorway beyond them, "
            "standing on the worn stone threshold in the hard daylight and both seen "
            "in profile from the side, are two religious men who have not come in — a "
            "tall well-fed man of fifty-five with an iron-grey square beard, a "
            "blue-grey head-cloth and a deep indigo robe, and beside him a shorter "
            "slighter man of forty with a close black beard and a dark olive-green "
            "robe. Their heads are inclined toward each other and the older man's "
            "lips are moving close to the other's ear, one hand half raised toward "
            "the table without pointing. Neither of them looks at the camera. The "
            "daylight is behind them so their faces sit in soft shade against the "
            "glare of the lane outside."
        ),
    },
    {
        "id": "v2-r021-b04", "out": "s04-receiveth-sinners.jpeg", "seg": "s2",
        "window": "12.005-16.491", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "DOORWAY"],
        "narration": "This man receiveth sinners, and eateth with them.",
        "must_show": "a sharply readable close study of the Pharisee's FACE mid-mutter — this frame is the identity anchor for him and every feature must be plainly legible.",
        "must_not_show": "Jesus is not in this frame. No cream or off-white cloth anywhere, no second face in focus, no lamp, no pupils on the lens.",
        "scene": (
            "One photograph, 85mm prime lens at f/2, shallow depth of field, hard "
            "mid-afternoon daylight in the lane, fine grain. Tight on the Pharisee "
            "from the chest up as he stands outside the doorway, turned three "
            "quarters to his own right so his face is fully lit and fully readable — "
            "a tall well-fed man of fifty-five, full square iron-grey beard combed "
            "flat, grey hair under a neatly folded blue-grey head-cloth, smooth "
            "unweathered skin, deep indigo-blue robe and mantle with two narrow "
            "madder-red bands. He is speaking low and sideways to someone just off "
            "frame to his right: the lips barely parted, the jaw set, the nostrils "
            "drawn in, one eyebrow slightly raised — distaste held under good "
            "manners. His eyes are aimed downward and to the right at something lower "
            "and further away than the camera, so his gaze leaves the picture through "
            "the RIGHT edge and his pupils are nowhere near the lens. Bright daylight "
            "from the right models his cheekbone and the weave of the indigo wool; "
            "the mud-plastered wall and the dark doorway behind him are a soft "
            "unreadable wash."
        ),
    },
    {
        "id": "v2-r021-b05", "out": "s05-and-eateth-with-them.jpeg", "seg": "n2b",
        "window": "16.491-20.783", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "SCRIBE", "DOORWAY"],
        "narration": "This man welcomes sinners, they said, and even eats with them.",
        "must_show": "the two religious men exchanging a look with each other, and past them, out of focus in the dim room, the shared dish and the hands reaching into it that they are objecting to.",
        "must_not_show": "Jesus is not in this frame. No cream or off-white cloth anywhere, no lamp, and neither man's gaze goes anywhere near the lens.",
        "scene": (
            "One photograph, 85mm lens at f/2.8, shallow depth of field, hard "
            "mid-afternoon daylight, fine grain. A tight two-shot of the two "
            "religious men on the threshold, seen from the side and both sharp in the "
            "near frame — the man of fifty-five with the iron-grey square beard and "
            "indigo robe on the left, facing right, and the slighter man of forty "
            "with the close black beard and dark olive-green robe on the right, "
            "facing left. They are looking straight at EACH OTHER, so both gazes are "
            "locked inside the frame and neither travels toward the camera, and the "
            "older man's eyebrows are lifted in the small ugly satisfaction of being "
            "agreed with. Between and beyond their shoulders, thrown far out of focus "
            "in the dim room behind them, the low table: a shallow clay dish and "
            "three or four brown and madder-red arms reaching into it at once. "
            "Daylight from the left edges the older man's beard and leaves the "
            "younger man's face in soft shade."
        ),
    },
    {
        "id": "v2-r021-b06", "out": "s06-so-he-told-them-a-story.jpeg", "seg": "n3",
        "window": "20.783-26.563", "wide": False, "jesus": True, "ref": True,
        "locks": ["HOUSE-MEAL"],
        "narration": "So Jesus told them a story about how heaven really feels about one lost person.",
        "must_show": "Jesus turning toward the men in the doorway and beginning to speak — unhurried, warm, entirely unembarrassed to be caught eating with the people he is eating with.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off him; he is not rebuking, not pointing, not standing; no lamp; his pupils are not on the lens.",
        "scene": (
            "One photograph, 105mm lens wide open, very shallow depth of field, "
            "mid-afternoon daylight, fine grain. Shot OVER THE SHOULDER of an "
            "out-of-focus indigo-robed figure who fills the near right of the frame "
            "from behind, so the picture has a target inside itself: past that "
            "shoulder, sharp and centred, Jesus is seated on the floor mat and has "
            "turned his head and upper body toward that shoulder to answer. He is "
            "mid-breath at the start of a sentence, mouth just opening, one hand "
            "lifting a few inches off his knee in the small gesture that begins a "
            "story. His eyes are fixed on the indigo shoulder in the near frame, so "
            "his gaze is aimed clearly into the picture and past the camera on the "
            "right. The wedge of daylight from the doorway crosses his cheek and "
            "beard from the left and leaves the other side of his face in soft "
            "shadow; every bit of light in the frame comes from that doorway and "
            "nothing comes off him. The dim plastered wall behind him dissolves to a "
            "warm blur."
        ),
    },
    {
        "id": "v2-r021-b07", "out": "s07-what-man-of-you.jpeg", "seg": "j1",
        "window": "26.563-31.00", "wide": False, "jesus": True, "ref": True,
        "locks": ["HOUSE-MEAL", "OUTCASTS"],
        "narration": "What man of you, having an hundred sheep, if he lose one of them...",
        "must_show": "Jesus telling the parable to the whole room — speaking, alive, his hands doing part of the telling.",
        "must_not_show": "no halo, no glow, no rim-light; he is not standing, not preaching over a crowd; no lamp; his pupils are not on the lens.",
        "scene": (
            "One photograph, 85mm lens at f/2, shallow depth of field, mid-afternoon "
            "daylight, fine grain. Jesus seated on the floor at the low table, framed "
            "from the waist up and turned three quarters to his own left, sharp "
            "against a soft warm wash of out-of-focus listeners in umber and madder "
            "red. He is well into the sentence: lips shaped around a word, eyebrows "
            "raised in the middle of asking a question, both hands open in front of "
            "his chest — the left held out flat and wide to mean a whole flock, the "
            "right holding up a single finger to mean one. His eyes are on a listener "
            "seated to his left and slightly below him, so his gaze travels down and "
            "out through the LEFT edge of the frame, past the camera. The daylight "
            "shaft from the doorway rakes across the table and the side of his face "
            "from the right; nothing about him emits light."
        ),
    },
    # ==================================== THE PARABLE — dusk at the sheepfold ====
    {
        "id": "v2-r021-b08", "out": "s08-one-of-them-missing.jpeg", "seg": "j1",
        "window": "31.00-34.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "FOLD"],
        "narration": "...doth not leave the ninety and nine in the wilderness...",
        "must_show": "a sharply readable close study of the shepherd's FACE at the fold as he realises one is gone — this frame is the identity anchor for him and every feature must be plainly legible. He is a man of thirty-five with black hair and a black beard.",
        "must_not_show": "he is NOT an old man, NOT grey-haired, NOT white-bearded, NOT frail; no sheep are countable in this frame; no cream or off-white cloth anywhere; his pupils are not on the lens.",
        "scene": (
            "One photograph, 85mm prime lens at f/2, shallow depth of field, the cold "
            "blue-grey light of dusk after the sun is down, fine grain. Tight on the "
            "shepherd from the chest up at the gap in the dry-stone fold wall, turned "
            "three quarters to his own right so his face is fully lit by the last "
            "flat sky light and fully readable — a lean, broad-shouldered, "
            "sun-darkened working man of THIRTY-FIVE with thick BLACK hair to the jaw "
            "pushed back off his forehead, a short full BLACK beard with no grey in "
            "it, a heavy brow and deep-set dark brown eyes. Coarse dark earth-brown "
            "knee-length tunic, rust-brown sash, a rolled dark umber wool mantle over "
            "one shoulder, a polished olivewood crook standing in his right fist. His "
            "head has just come up and his eyes have gone hard and far away: he is "
            "counting again and the count is wrong. His gaze is aimed out over the "
            "darkening hills to his right, leaving the picture through the RIGHT "
            "edge, well off the camera axis. Behind and below him the flock is a "
            "dark, crowded, unreadable mass of dusty backs running out of both sides "
            "of the frame, thrown well out of focus, with no individual sheep "
            "countable."
        ),
    },
    {
        "id": "v2-r021-b09", "out": "s09-the-empty-place.jpeg", "seg": "j1",
        "window": "34.90-38.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["FLOCK", "FOLD"],
        "narration": "...and go after that which is lost, until he find it?",
        "must_show": "the packed flock crowding through the thorn-brush gateway into the fold at dusk, filling the frame, and the bare stony hills beyond that swallow everything.",
        "must_not_show": "no person's face in this frame; no countable rows or grids of sheep; no cloned identical sheep; no wire, fence posts, sawn timber or gate hardware.",
        "scene": (
            "One photograph, 35mm lens low to the ground, the cold blue-grey light of "
            "dusk after the sun is down, fine grain. THE CAMERA IS SET DOWN AT SHEEP "
            "HEIGHT BEHIND THE FLOCK AND SHOOTS PAST THEIR BACKS toward the gap in "
            "the dry-stone wall: the near half of the frame is a crowded moving mass "
            "of dusty tawny and umber fleeced backs, fat tails and dark brown faces "
            "pressing forward and away from the camera, running out of the frame on "
            "both sides so that no number is countable. Dust hangs in the flat blue "
            "light. Beyond the low unmortared limestone wall the bare stony hills "
            "fall away ridge behind ridge into a ravine already full of darkness, and "
            "the last of the light is a cold pale band low on the horizon with no "
            "colour in it. At the very edge of the fold, small and sharp, one man's "
            "back in a dark brown tunic and umber mantle is turned away from the flock "
            "and toward those hills."
        ),
    },
    {
        "id": "v2-r021-b10", "out": "s10-he-does-not-count.jpeg", "seg": "n4",
        "window": "38.86-44.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "FOLD"],
        "narration": "Which of you, with a hundred sheep, would not leave the ninety-nine behind to go after the one that wandered off?",
        "must_show": "the shepherd's hands and face as he makes the decision — hauling the thorn brush across the fold gap to shut the rest in, already looking out at the dark hills.",
        "must_not_show": "he is NOT old, NOT grey, NOT white-bearded; no sheep countable; no cream or off-white cloth; his pupils are not on the lens.",
        "scene": (
            "One photograph, 50mm lens at f/2.8, the cold blue-grey light of dusk, "
            "fine grain. The shepherd in three-quarter view from the side, crouched "
            "at the gap in the dry-stone wall, both hands gripping a heavy bundle of "
            "cut thorn brush and hauling it across the gap — the thorns sharp and "
            "individually visible, his knuckles pale on the wood, a fresh scratch "
            "along the back of one wrist. He is a lean, sun-darkened man of "
            "thirty-five with thick black hair to the jaw and a short full black "
            "beard with no grey in it, in a coarse dark earth-brown tunic with a "
            "rust-brown sash and a rolled dark umber wool mantle across one shoulder. His body is "
            "doing the work but his head is already turned away, up and out to his "
            "left toward the black ridges, so his gaze leaves the frame through the "
            "LEFT edge, far off the camera axis. Behind him, well out of focus, the "
            "flock is a dark shapeless crowd of backs with no number readable in it."
        ),
    },
    {
        "id": "v2-r021-b11", "out": "s11-he-goes-after-it.jpeg", "seg": "n4",
        "window": "44.00-49.003", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "WILDERNESS"],
        "narration": "...and keep searching until you found it.",
        "must_show": "the shepherd setting off DOWNHILL away from the fold into the empty wilderness, the ridges falling away in front of him, the scale of what he is walking into.",
        "must_not_show": "he is NOT old or grey; no road, no building, no wall, no second person anywhere; no cream or off-white cloth; nobody facing the lens.",
        "scene": (
            "One photograph, 35mm lens, the last cold blue-grey light of dusk, fine "
            "grain. THE CAMERA STANDS UPHILL BEHIND THE SHEPHERD AND SHOOTS PAST HIS "
            "BACK: he is in the near third of the frame, seen from directly behind "
            "and slightly above, walking away from the camera and DOWNHILL, so no "
            "part of his face is turned toward the lens. Coarse dark earth-brown "
            "tunic, rust-brown sash, a rolled dark umber wool mantle across one shoulder, the "
            "olivewood crook out in his right hand feeling the ground, his black hair "
            "to the jaw lifting slightly in the wind. In front of him the Judean "
            "wilderness falls away ridge behind ridge into steep ravines already "
            "black with shadow, pale limestone shelves catching the last flat light, "
            "thorn scrub and one wind-bent terebinth on the slope. He is small "
            "against it. There is no road, no building and no other living person in "
            "the picture."
        ),
    },
    {
        "id": "v2-r021-b12", "out": "s12-the-ninety-nine-behind.jpeg", "seg": "n5",
        "window": "49.003-53.00", "wide": True, "jesus": False, "ref": False,
        "locks": ["FLOCK", "SHEPHERD", "FOLD"],
        "narration": "He does not stand there counting what he still has.",
        "must_show": "the flock left behind in the fold in the last of the light, and the shepherd already gone small over the lip of the hill.",
        "must_not_show": "no countable number of sheep, no rows or grids; no other person; no cream or off-white cloth; no face toward the lens.",
        "scene": (
            "One photograph, 35mm lens, deep depth of field, the last cold blue-grey "
            "light of dusk, fine grain. THE CAMERA IS LOW INSIDE THE FOLD BEHIND THE "
            "FLOCK AND SHOOTS OUT PAST THEIR BACKS AND HEADS toward the hill: the "
            "near half of the frame is a crowded mass of dusty tawny and umber "
            "fleeced backs and dark faces settling for the night, packed too tight "
            "and running too far out of both sides of the frame for any number to be "
            "countable. Beyond the low dry-stone wall, out on the bare hillside and "
            "already very small, the shepherd's back in dark brown and umber is "
            "going down over the lip of the slope with his crook in his hand, seen "
            "from directly behind, already half below the skyline. The sky above the "
            "ridge is a flat cold grey-blue with no colour in it."
        ),
    },
    {
        "id": "v2-r021-b13", "out": "s13-out-after-the-one.jpeg", "seg": "n5",
        "window": "53.00-56.951", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "WILDERNESS"],
        "narration": "He leaves the ninety-nine behind to go out after the one that is gone.",
        "must_show": "the shepherd well out in the empty country now, working — reading the ground for tracks, moving fast, the light almost gone.",
        "must_not_show": "he is NOT old or grey; no flock in this frame; no building, road or second person; no cream or off-white cloth; no pupils on the lens.",
        "scene": (
            "One photograph, 50mm lens at f/4, the last blue-grey minutes of dusk, "
            "fine grain. The shepherd in three-quarter view from the side and "
            "slightly behind, half crouched on a scree slope with one hand flat on "
            "the dust and the crook braced across the ground, reading a scuff of "
            "tracks. He is a lean, sun-darkened man of thirty-five with thick black "
            "hair to the jaw and a short full black beard with no grey, in a coarse "
            "dark earth-brown tunic, rust-brown sash and a rolled dark umber wool mantle "
            "across one shoulder. His head is up and turned away to his right, following the "
            "line of the tracks along the slope, so his gaze leaves the frame through "
            "the RIGHT edge, nowhere near the camera. Around him nothing but pale "
            "broken limestone, loose scree, dry thorn scrub and a ravine dropping "
            "away behind him into full darkness."
        ),
    },
    # ============================================== THE SEARCH — deep night ====
    {
        "id": "v2-r021-b14", "out": "s14-through-the-night.jpeg", "seg": "n6",
        "window": "56.951-60.90", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "WILDERNESS", "NIGHT-LAW"],
        "narration": "He searches through the night, over the rocks and the ravines...",
        "must_show": "deep night in the open wilderness: the shepherd climbing across broken rock with a burning pine torch, tiny under a sky full of real stars.",
        "must_not_show": "no lantern, no glass, no candle, no unexplained light; no sunset or sunrise colour anywhere; no other person; no face toward the lens.",
        "scene": (
            "One photograph, 24mm lens, long exposure, deep night, heavy fine grain. "
            "THE CAMERA IS SET HIGH ON THE OPPOSITE SLOPE AND LOOKS ACROSS AND DOWN "
            "AT THE SHEPHERD'S BACK as he climbs away from it: he is small in the "
            "lower third of the frame, seen from behind and above, one arm out on a "
            "limestone shelf for balance, the other holding up a burning split pine "
            "torch with a ragged flame and a few sparks lifting off it. Its orange "
            "light reaches only a few feet and picks out the hard edges of the rocks "
            "around him and the dark brown of his tunic and umber mantle; everything "
            "past that is cold silver-grey moonlight on bare limestone and black "
            "shadow in the ravine below him. Above, the sky is thick with real stars "
            "and a hard bright moon sits high and behind the camera. There is no "
            "other light anywhere in the picture."
        ),
    },
    {
        "id": "v2-r021-b15", "out": "s15-calling-into-the-dark.jpeg", "seg": "n6",
        "window": "60.90-64.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "WILDERNESS", "NIGHT-LAW"],
        "narration": "...calling into the dark, because to him that one is not a loss he can shrug off.",
        "must_show": "the shepherd stopped at the edge of a black ravine, shouting down into it, his whole body committed to the call.",
        "must_not_show": "he is NOT old or grey; no lantern, no glass, no candle, no light without a source; no cream or off-white cloth; his gaze is not on the lens.",
        "scene": (
            "One photograph, 50mm lens wide open, deep night, heavy fine grain. The "
            "shepherd from the knees up in three-quarter view from the side, standing "
            "on the lip of a ravine with his weight forward on his front foot, one "
            "hand cupped hard at the side of his mouth and the other gripping the "
            "olivewood crook planted in the rock, his head thrown back and his mouth "
            "wide open in the middle of a shout downward into the black. He is a "
            "lean, sun-darkened man of thirty-five with thick black hair to the jaw, "
            "a short full black beard with no grey, a coarse dark earth-brown tunic, "
            "rust-brown sash and a rolled dark umber wool mantle. The torch in the crook of his other "
            "arm throws hard orange light up one side of his face and neck and leaves "
            "the other side to cold moonlight; his eyes are aimed steeply DOWN into "
            "the ravine, so his gaze leaves the frame through the BOTTOM edge and is "
            "nowhere near the camera. Behind him the ravine is a wall of black, and "
            "cold silver stars fill the top of the frame."
        ),
    },
    {
        "id": "v2-r021-b16", "out": "s16-that-one-is-his.jpeg", "seg": "n6",
        "window": "64.80-68.714", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "NIGHT-LAW"],
        "narration": "That one is his.",
        "must_show": "the shepherd's face alone in the dark, worn out and utterly unwilling to stop — this is the frame that says the sheep belongs to him.",
        "must_not_show": "he is NOT old or grey; no lantern, no glass, no candle; no other person; his pupils are not on the lens.",
        "scene": (
            "One photograph, 105mm lens wide open, very shallow depth of field, deep "
            "night, heavy fine grain. Very tight on the shepherd's face and "
            "shoulders, turned three quarters to his own left. He is a sun-darkened "
            "man of thirty-five with thick black hair to the jaw and a short full "
            "black beard with no grey in it; his face is filthy with dust, sweat has "
            "cut clean lines through it at the temple, his lips are cracked, and he "
            "is breathing hard through his mouth after the climb. He is completely "
            "still, LISTENING — head tipped, eyes narrowed and aimed far off into the "
            "dark to his left, out through the LEFT edge of the frame and well past "
            "the camera. The torch is low and out of shot below the frame, throwing "
            "hard orange light up under his jaw and cheekbone from beneath while cold "
            "moonlight touches the top of his hair; behind him is nothing but black "
            "night and a scatter of stars far out of focus."
        ),
    },
    # ============================================ THE FINDING — first light ====
    {
        "id": "v2-r021-b17", "out": "s17-and-when-he-finds-it.jpeg", "seg": "n7",
        "window": "68.714-72.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "ONE-SHEEP", "WILDERNESS", "NIGHT-LAW"],
        "narration": "And when he finds it —",
        "must_show": "the moment of finding: looking down past the shepherd's shoulder into a rock cleft where ONE sheep is wedged in a thorn thicket, lit by his torch.",
        "must_not_show": "exactly one sheep and no second sheep; no blood, no wound, no injury; no lantern, no glass, no candle; no face toward the lens.",
        "scene": (
            "One photograph, 35mm lens, deep night, heavy fine grain. Shot OVER THE "
            "SHEPHERD'S SHOULDER from behind and above, so his dark brown shoulder "
            "and umber mantle and the black hair at the back of his head fill the near "
            "left of the frame out of focus and no part of his face is toward the "
            "lens. Past him, down in a narrow cleft between two limestone shelves and "
            "sharply lit by the torch he is holding out over the drop, ONE ewe is "
            "wedged among the branches of a low thorn thicket — dirty tawny-grey "
            "matted fleece, a dark brown face, long drooping ears, a dark brown patch "
            "over her right shoulder, thorn twigs and burrs caught the whole length "
            "of her flank. Her head is twisted up toward the light and her eyes are "
            "wide. Everything outside the torchlight is black rock and night. There "
            "is exactly one sheep in this picture."
        ),
    },
    {
        "id": "v2-r021-b18", "out": "s18-too-worn-out-to-walk.jpeg", "seg": "n7",
        "window": "72.40-76.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["ONE-SHEEP", "NIGHT-LAW"],
        "narration": "— frightened, tangled in the thorns, too worn out to walk —",
        "must_show": "a close study of the one sheep herself: exhausted, filthy, snagged, ribs heaving, no strength left to stand.",
        "must_not_show": "no second sheep; no blood, no wound, no gore; no person's face; no lantern, glass or candle; nothing looking into the lens.",
        "scene": (
            "One photograph, 85mm lens at f/2, very shallow depth of field, deep night "
            "lit by a torch just out of frame, heavy fine grain. Very close on ONE ewe "
            "lying on her side in the dust and thorn litter at the bottom of the rock "
            "cleft, framed from the shoulder forward — dirty tawny-grey matted fleece "
            "packed with dust, a dark brown face, long drooping ears flattened back, a "
            "dark brown patch over her right shoulder, dry thorn twigs and burrs "
            "snagged through the wool along her neck and flank, grey dust caked around "
            "her nostrils. Her ribs are visibly heaving. Her eye is wide and rolled up "
            "and away toward something above and behind her to the right, so her look "
            "leaves the frame through the TOP RIGHT corner and not toward the camera. "
            "The torchlight comes in low and warm from the upper right and falls off "
            "to black within a hand's width; the thorn branches nearest the camera are "
            "dark unreadable silhouettes. There is exactly one animal in this picture."
        ),
    },
    {
        "id": "v2-r021-b19", "out": "s19-he-does-not-scold-it.jpeg", "seg": "n7",
        "window": "76.00-79.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "ONE-SHEEP", "NIGHT-LAW"],
        "narration": "he does not scold it, and he does not leave it there.",
        "must_show": "the shepherd's hands working the thorn branches back off the sheep one at a time — slow, careful, entirely gentle.",
        "must_not_show": "no second sheep; no blood or wound; he is NOT old or grey; no lantern, glass or candle; no gaze into the lens.",
        "scene": (
            "One photograph, 50mm lens at f/2.8, shallow depth of field, deep night "
            "lit by a torch wedged in the rocks just out of frame, heavy fine grain. "
            "Close on the shepherd's two hands and forearms filling the lower half of "
            "the frame — brown, scratched, dust-blackened in the creases, the fingers "
            "of one hand bending a thorn branch carefully back and away while the "
            "other hand lies flat and steady on the ewe's neck to keep her still. "
            "Above the hands, in the upper third of the frame, the shepherd's face is "
            "bent low over the work in three-quarter profile, black hair falling "
            "forward, short black beard, eyes down and fixed entirely on the thorn he "
            "is moving, so his gaze exits through the BOTTOM edge of the frame. His "
            "mouth is soft and slightly open, saying something quiet to her. The one "
            "ewe's dark brown face and tawny-grey fleece with its dark shoulder patch "
            "are pressed against the rock beside his hands. Warm torchlight from the "
            "left, black night behind."
        ),
    },
    {
        "id": "v2-r021-b20", "out": "s20-on-his-shoulders.jpeg", "seg": "j2",
        "window": "79.64-84.858", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "ONE-SHEEP", "WILDERNESS"],
        "narration": "And when he hath found it, he layeth it on his shoulders, rejoicing.",
        "must_show": "the lift: the sheep coming up across BOTH his shoulders behind his neck, her legs gathered in his fists, his face already breaking into joy as he takes the weight.",
        "must_not_show": "he is NOT old or grey; no second sheep; no blood or wound; no cream or off-white cloth; his pupils are not on the lens.",
        "scene": (
            "One photograph, 50mm lens at f/2.8, the thin level grey-gold light of "
            "first dawn from the east, mist low in the ravine behind, fine grain. The "
            "shepherd from the thighs up in three-quarter view from his left side, "
            "straightening up out of a crouch with the whole weight of ONE ewe coming "
            "up across BOTH shoulders behind his neck — her body lying along his upper "
            "back, her dark brown face and long ears hanging beside his left cheek, "
            "her four legs gathered together and gripped in his two fists in front of "
            "his chest, exactly the way a shepherd actually carries. Her fleece is "
            "dirty tawny-grey and matted with a dark brown patch over her right "
            "shoulder. His knees are bent under the load and the tendons stand out in "
            "his forearms, but his head is tipped back and his eyes are half shut and "
            "his mouth is open in a broad unguarded laugh of relief — a man of "
            "thirty-five with black hair to the jaw and a short full black beard. His "
            "look goes up and out through the TOP LEFT of the frame toward the "
            "brightening sky, not toward the camera. Cold pale limestone and drifting "
            "mist behind him."
        ),
    },
    {
        "id": "v2-r021-b21", "out": "s21-carries-it-home.jpeg", "seg": "n8",
        "window": "84.858-88.80", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "ONE-SHEEP", "WILDERNESS"],
        "narration": "He lifts it up, lays it across his own shoulders, and carries it the whole way home.",
        "must_show": "the long walk home at first light, the man and the sheep as one shape climbing away up the track, the distance he is willing to carry her.",
        "must_not_show": "he is NOT old or grey; no second sheep; no road, building or other person; no face toward the lens; no sunset colour.",
        "scene": (
            "One photograph, 35mm lens, deep depth of field, the thin level grey-gold "
            "light of early morning coming in flat from the left, fine grain. THE "
            "CAMERA STANDS DOWNHILL BEHIND THE SHEPHERD AND SHOOTS PAST HIS BACK as "
            "he climbs away from it: he fills the near left third of the frame seen "
            "from directly behind, no part of his face toward the lens, the ewe lying "
            "across both his shoulders with her dark brown face turned back over his "
            "left shoulder and her legs held in his fists at his chest. Dark "
            "earth-brown tunic, rust-brown sash, a rolled dark umber wool mantle, the olivewood crook "
            "hooked over one forearm. In front of him a faint animal track winds up "
            "between pale limestone shelves and thorn scrub toward a ridge line, and "
            "beyond it ridge after ridge of empty wilderness stands in the flat "
            "morning light with mist still lying in the ravine bottoms. His long "
            "shadow runs back toward the camera."
        ),
    },
    {
        "id": "v2-r021-b22", "out": "s22-not-relieved-rejoicing.jpeg", "seg": "n8",
        "window": "88.80-92.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "ONE-SHEEP"],
        "narration": "Not relieved. Not annoyed at the trouble. Rejoicing.",
        "must_show": "the shepherd's face carrying her, with her head right beside his — pure delight, not endurance; the two heads together are the picture.",
        "must_not_show": "he is NOT old or grey; no second sheep; no strain, grimace or resentment on his face; his pupils are not on the lens.",
        "scene": (
            "One photograph, 105mm lens wide open, very shallow depth of field, the "
            "thin level gold light of early morning from the left, fine grain. Very "
            "tight two-shot: the shepherd's head and left shoulder fill the right of "
            "the frame in three-quarter profile, and the ewe's dark brown face and "
            "long drooping ear hang down against his cheek on the left, close enough "
            "that her jaw rests on his collarbone. He is a sun-darkened man of "
            "thirty-five, thick black hair to the jaw damp at the temple, short full "
            "black beard with no grey, dust still on his skin. He is grinning — "
            "cheeks up, eyes creased almost shut, teeth showing — and he has turned "
            "his head slightly toward the animal so his eyes are aimed at HER, a "
            "target inside the frame, and nowhere near the lens. One of his hands "
            "comes up into the bottom of the frame gripping her forelegs. Warm level "
            "morning light rakes across both faces from the left; the wilderness "
            "behind is a soft grey-gold blur."
        ),
    },
    {
        "id": "v2-r021-b23", "out": "s23-the-whole-way-home.jpeg", "seg": "n8",
        "window": "92.70-96.568", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "ONE-SHEEP", "WILDERNESS", "VILLAGE"],
        "narration": "...and carries it the whole way home, rejoicing.",
        "must_show": "the shepherd cresting the last ridge with the sheep on his shoulders and the village coming into sight below him in the morning.",
        "must_not_show": "he is NOT old or grey; no dome, minaret, tower or tiled roof on the skyline; no face toward the lens; no sunset colour.",
        "scene": (
            "One photograph, 35mm lens, deep depth of field, full clear morning light "
            "from the left, fine grain. THE CAMERA STANDS BEHIND AND BELOW THE "
            "SHEPHERD ON THE TRACK AND SHOOTS PAST HIS BACK AND UP: he is in the near "
            "right of the frame, seen from behind in three-quarter, cresting a stony "
            "ridge with the ewe across both shoulders, so no part of his face is "
            "toward the lens. Beyond and below him the ground drops into a small hill "
            "village of a dozen flat-roofed limestone and mud-plaster houses with dry "
            "stone terraces and fig trees between them, smoke rising thin and "
            "straight from two roofs. The skyline behind the village is nothing but "
            "bare brown hill and open morning sky. Two or three villagers are already "
            "tiny figures in the lane below, one of them turning to look uphill."
        ),
    },
    # =========================================== THE CELEBRATION — morning ====
    {
        "id": "v2-r021-b24", "out": "s24-he-calls-them-together.jpeg", "seg": "n9",
        "window": "96.568-100.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "ONE-SHEEP", "VILLAGE", "VILLAGERS"],
        "narration": "Then he calls everyone together — friends, neighbors, the whole village —",
        "must_show": "the shepherd shouting the news up the village lane with the sheep still on his shoulders, and doors and roofs beginning to fill with people.",
        "must_not_show": "he is NOT old or grey; no cream or off-white cloth on anybody; no dome, minaret or tower; his gaze is not on the lens.",
        "scene": (
            "One photograph, 35mm lens at f/4, full morning light, fine grain. The "
            "shepherd from the waist up in the narrow village lane, three quarters "
            "toward his own right, the ewe still across both shoulders and her legs "
            "in his fists. His head is thrown back and his mouth is wide open in a "
            "shout up the lane to his right — face split with it, eyes crinkled — so "
            "his look goes up and out through the RIGHT edge of the frame, past the "
            "camera. He is a lean, dust-covered man of thirty-five with black hair to "
            "the jaw and a short full black beard with no grey, in a dark earth-brown "
            "tunic and rust-brown sash. Behind him along the lane, slightly out of "
            "focus, a woman in madder red is coming out through a hanging door-cloth, "
            "a boy in umber brown is already running toward him, and an old man in "
            "olive green is standing up on a flat earth roof. Undressed limestone "
            "walls and bare hill sky behind."
        ),
    },
    {
        "id": "v2-r021-b25", "out": "s25-and-throws-a-celebration.jpeg", "seg": "n9",
        "window": "100.20-103.681", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "ONE-SHEEP", "VILLAGERS", "VILLAGE"],
        "narration": "...and throws a celebration.",
        "must_show": "the village crowding around him in the open by the well — food and a jug being carried out, people arriving from every direction, real physical delight.",
        "must_not_show": "no cream or off-white cloth on anybody anywhere in the frame; no dome, minaret, tower or tiled roof; nobody posed for or facing the lens.",
        "scene": (
            "One photograph, 28mm lens, deep depth of field, full morning light, fine "
            "grain. THE CAMERA STANDS BEHIND THE ARRIVING VILLAGERS AND SHOOTS PAST "
            "THEIR BACKS toward the centre: the near third of the frame is the backs "
            "and shoulders of four or five people in umber, madder red and olive "
            "green pressing forward and away from the camera, out of focus, and NOT "
            "ONE FACE IS TURNED TOWARD THE LENS. In the middle of the open ground by "
            "the stone-kerbed well the shepherd stands sharp and surrounded, the ewe "
            "still across his shoulders, laughing, with a hand on his arm from one "
            "side and a hand on the sheep's flank from the other. Around him "
            "twenty-odd villagers of every age converge — a woman carrying out a wide "
            "clay platter of flat bread, an old man with a clay jug under his arm, "
            "two children running in from the left, a man stepping over the low "
            "terrace wall. Flat-roofed limestone houses, fig trees and bare brown "
            "hillside behind; nothing but hill and sky on the skyline."
        ),
    },
    {
        "id": "v2-r021-b26", "out": "s26-rejoice-with-me.jpeg", "seg": "j3",
        "window": "103.681-109.421", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "ONE-SHEEP", "VILLAGERS"],
        "narration": "Rejoice with me; for I have found my sheep which was lost.",
        "must_show": "the shepherd swinging the sheep down and holding her out toward his neighbours — the whole invitation of the line in one gesture.",
        "must_not_show": "he is NOT old or grey; exactly one sheep; no cream or off-white cloth on anybody; no face aimed at the lens.",
        "scene": (
            "One photograph, 50mm lens at f/2.8, full morning light, fine grain. The "
            "shepherd from the knees up, turned three quarters to his own left, "
            "swinging the ewe down off his shoulders and holding her up and out in "
            "both arms toward the people in front of him — her tawny-grey matted "
            "fleece, dark brown face and the dark patch over her right shoulder sharp "
            "against the sky, her legs still folded. His arms are locked straight "
            "under her, his chest is out, his head is up and his mouth is open "
            "mid-shout. He is a lean, dust-covered man of thirty-five with black hair "
            "to the jaw and a short full black beard with no grey, in a dark "
            "earth-brown tunic and rust-brown sash. His eyes are on the villagers "
            "standing to his left, so his gaze crosses the frame and leaves it "
            "through the LEFT edge, far off the camera axis. In the near left of the "
            "frame, out of focus, two villagers' shoulders in madder red and olive "
            "green and a pair of hands already coming up toward the sheep."
        ),
    },
    {
        "id": "v2-r021-b27", "out": "s27-my-sheep.jpeg", "seg": "n9b",
        "window": "109.421-112.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD", "ONE-SHEEP"],
        "narration": "Be glad with me, he tells them. Not, I got my property back.",
        "must_show": "his hand flat and tender on the sheep's flank, the burrs still in her wool — the frame that says she was his the whole time.",
        "must_not_show": "no second sheep; no blood or wound; no cream or off-white cloth; no face in this frame at all.",
        "scene": (
            "One photograph, 100mm macro lens at f/2.8, very shallow depth of field, "
            "full morning light from the right, fine grain. Extremely close: one "
            "brown, scratched, dust-creased human hand and wrist laid flat and open "
            "across the ewe's shoulder, the fingers sunk into the dirty tawny-grey "
            "matted fleece with the dark brown patch showing between them. Dry thorn "
            "twigs and burrs are still tangled in the wool under his palm and a single "
            "scratch runs across the back of his hand. Her ear and the top of her dark "
            "brown head are just in frame at the lower left, out of focus. Nothing "
            "else is sharp — the crowd behind is a warm unreadable blur of umber and "
            "madder red. No face appears in this picture."
        ),
    },
    {
        "id": "v2-r021-b28", "out": "s28-it-was-his-the-whole-time.jpeg", "seg": "n9b",
        "window": "112.90-116.22", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGERS", "VILLAGE"],
        "narration": "It was his the whole time it was missing.",
        "must_show": "the neighbours' faces catching the joy — two or three real, unposed, delighted faces turned toward the shepherd, who is out of frame.",
        "must_not_show": "no cream or off-white cloth on anybody; nobody looking into the lens; no dome, minaret or tower behind them.",
        "scene": (
            "One photograph, 85mm lens at f/2, shallow depth of field, full morning "
            "light, fine grain. Three villagers close together filling the frame from "
            "the chest up, all of them turned to their own right toward something "
            "happening just outside the RIGHT edge of the frame, so every gaze leaves "
            "the picture through that edge and none of them comes near the camera — "
            "an old woman in a madder-red head-cloth with her hand at her mouth and "
            "her eyes wet with laughing, a broad young man in umber brown behind her "
            "with his head back mid-laugh, and a small girl in dull ochre on his hip "
            "pointing to the right with her whole arm. Morning sun from the right "
            "lights the edges of their faces and the dust in the air between them. "
            "Behind them a mud-plastered limestone wall and a fig branch, thrown soft."
        ),
    },
    # ===================================== BACK INSIDE THE HOUSE — the point ====
    {
        "id": "v2-r021-b29", "out": "s29-joy-shall-be-in-heaven.jpeg", "seg": "j4",
        "window": "116.22-120.50", "wide": True, "jesus": True, "ref": True,
        "locks": ["OUTCASTS", "HOUSE-MEAL"],
        "narration": "I say unto you, that likewise joy shall be in heaven over one sinner that repenteth...",
        "must_show": "back in the same room in the same afternoon light: Jesus finishing the parable, the whole crowd still leaning in, absolutely quiet.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off him; no night, no lamp, no sunset sky; no cream or off-white cloth on anybody but Jesus; nobody facing the lens.",
        "scene": (
            "One photograph, 35mm lens, mid-afternoon daylight, fine film grain. THE "
            "CAMERA SITS LOW BEHIND THE SEATED CROWD AND SHOOTS PAST THEIR BACKS AND "
            "SHOULDERS toward Jesus: the near third of the frame is out-of-focus "
            "seated backs, heads and shoulders in umber, madder red and olive green, "
            "and NOT ONE FACE IS TURNED TOWARD THE LENS. Beyond them Jesus sits on "
            "the mat at the low table, sharp, leaning forward with both forearms on "
            "his knees, saying the last line of the story straight at the people in "
            "front of him — his face open and certain, not raised in triumph. Nobody "
            "is eating. Every visible body in the picture is angled inward toward "
            "him. The hard wedge of daylight from the open doorway lies across the "
            "floor between the camera and Jesus and the dust turns in it; the light is "
            "all daylight and none of it comes off him."
        ),
    },
    {
        "id": "v2-r021-b30", "out": "s30-one-sinner-that-repenteth.jpeg", "seg": "j4",
        "window": "120.50-124.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["PUBLICAN", "HOUSE-MEAL"],
        "narration": "...over one sinner that repenteth...",
        "must_show": "the tax collector's face taking it personally — the man who has just understood that he is the one who was carried home.",
        "must_not_show": "Jesus is not in this frame. No cream or off-white cloth; no second face in focus; no lamp; his pupils are not on the lens.",
        "scene": (
            "One photograph, 105mm lens wide open, very shallow depth of field, "
            "mid-afternoon daylight, fine grain. Very tight on the tax collector's "
            "face, turned three quarters to his own left — the heavy-set man of "
            "thirty-eight with the thick neck, fleshy olive-brown face, broad "
            "flattened nose, short receding curly black hair, close-trimmed black "
            "beard and deep rust-red robe. He has gone completely still. His mouth is "
            "closed and pulled tight at one corner, his chin has dropped a fraction, "
            "his brows have come together, and his eyes are shining wet without a "
            "tear falling. He is looking at someone lower and further away to his "
            "left, so his gaze travels down and out through the LEFT edge of the "
            "frame, well off the camera axis. The shaft of daylight from the doorway "
            "crosses the side of his face from the right and catches the wet along "
            "his lower lid; the dim room behind him is a soft unreadable wash of "
            "warm shadow."
        ),
    },
    {
        "id": "v2-r021-b31", "out": "s31-more-than-over-ninety-nine.jpeg", "seg": "j4",
        "window": "124.70-129.014", "wide": False, "jesus": False, "ref": False,
        "locks": ["PHARISEE", "SCRIBE", "DOORWAY"],
        "narration": "...more than over ninety and nine just persons, which need no repentance.",
        "must_show": "the two religious men on the threshold hearing the last line land on them — recognition and offence arriving at the same moment.",
        "must_not_show": "Jesus is not in this frame. Nobody is shouting or storming off; no cream or off-white cloth; neither gaze is on the lens.",
        "scene": (
            "One photograph, 85mm lens at f/2.8, shallow depth of field, hard "
            "mid-afternoon daylight, fine grain. The two religious men on the stone "
            "threshold of the doorway, framed from the chest up and seen from the "
            "side, both sharp — the well-fed man of fifty-five with the iron-grey "
            "square beard, the blue-grey head-cloth and the deep indigo robe standing "
            "nearest the camera in three-quarter from behind, and the slighter man of "
            "forty with the close black beard and dark olive-green robe half a step "
            "beyond him. The older man has stopped mid-mutter: his mouth is shut "
            "hard, his jaw muscle is set, and his eyes are fixed away to his left "
            "into the dim room, so his gaze crosses the frame and leaves it through "
            "the LEFT edge, nowhere near the camera. The younger man's eyes have "
            "dropped to the ground in front of his own feet. The daylight of the lane "
            "is behind them and throws their long shadows in through the doorway "
            "toward the camera."
        ),
    },
    {
        "id": "v2-r021-b32", "out": "s32-that-is-how-good-he-is.jpeg", "seg": "n10",
        "window": "129.014-133.70", "wide": False, "jesus": True, "ref": True,
        "locks": ["HOUSE-MEAL"],
        "narration": "That is how good he is. Heaven throws a party over one person turning back.",
        "must_show": "Jesus's face at the end of the story — warm, glad, entirely at home at this table with these people.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off him; he is not solemn, not stern, not looking into the lens; no lamp.",
        "scene": (
            "One photograph, 105mm lens wide open, very shallow depth of field, "
            "mid-afternoon daylight, fine grain. Shot OVER THE SHOULDER of the tax "
            "collector, whose rust-red shoulder and the back of his curly black head "
            "fill the near left of the frame out of focus, giving the picture a "
            "target inside itself. Past that shoulder Jesus sits sharp and close, "
            "framed from the chest up, looking directly at that man — so his eyes are "
            "aimed into the near frame and clearly past the camera on the left. His "
            "face has settled into an unhurried gladness: the corners of the eyes "
            "creased, the mouth just short of a smile, his head tipped very slightly. "
            "One hand rests open on his knee. The wedge of daylight from the doorway "
            "crosses his cheek and beard from the right and leaves the far side of "
            "his face in soft shadow; every bit of light in the frame comes from that "
            "doorway and none of it comes off him. The dim plastered wall behind him "
            "is a warm blur."
        ),
    },
    {
        "id": "v2-r021-b33", "out": "s33-not-a-lecture-joy.jpeg", "seg": "n10",
        "window": "133.70-138.451", "wide": True, "jesus": True, "ref": True,
        "locks": ["OUTCASTS", "HOUSE-MEAL"],
        "narration": "Not a lecture. Not a grudge. Joy.",
        "must_show": "the meal simply going on — hands back in the bread, people talking and laughing around Jesus, the outcasts closer to him than anyone.",
        "must_not_show": "no halo, no glow, no rim-light; no sunset-orange sky, no night, no lamp; no cream or off-white cloth on anybody but Jesus; nobody facing the lens.",
        "scene": (
            "One photograph, 35mm lens, mid-afternoon daylight, fine grain. THE CAMERA "
            "IS LOW AT THE END OF THE TABLE AND SHOOTS ALONG IT PAST THE BACKS AND "
            "SHOULDERS of the nearest seated people, whose out-of-focus arms and heads "
            "frame the bottom and both sides, and NOT ONE FACE IS TURNED TOWARD THE "
            "LENS. Along the table, torn barley loaves, a shallow clay dish, a clay "
            "jug, and four or five brown hands reaching in at once. Jesus sits halfway "
            "down on the far side, sharp, mid-conversation with the man beside him, "
            "one hand resting on the plank; the tax collector in rust red is leaning "
            "in from his other side saying something back, and a woman further down "
            "has her head back laughing. The bright wedge of daylight from the open "
            "doorway comes in flat from the right, lighting the dust in the air and "
            "the rim of every bowl and throwing long shadows down the table toward the "
            "camera. The corners of the room stay in deep warm shadow."
        ),
    },
]
