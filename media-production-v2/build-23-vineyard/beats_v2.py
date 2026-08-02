#!/usr/bin/env python3
"""V2 beat map — row 23, build-23-vineyard (Matthew 20:1-16), realistic.

COVERAGE: 40 pictures against V1's EIGHT, over 196.24 s of story = 4.91 s/picture.
V1 held `s3-eleventh-hour.jpeg` on screen from 32.83 s to 73.79 s — FORTY-ONE
SECONDS on one picture across SIX segments (n5, j6, j7a, n5b, j7b, n6) — and
`s7-friend-reply.jpeg` for another 34 s across n11, j1 and n12. Eight pictures for
a 3:23 video is one still every 25 seconds.

⚠️ WINDOWS COMPUTED FROM SCRATCH 2026-08-02 with the fixed `extract_beats.py`
reading the V1 build, then split inside each segment on its own
`audio/*.timing.json` phrase boundaries. Contiguous 0.28 s → 196.518 s (the card
start), zero gaps, zero overlaps. Extracted total 202.896 s against the V1 mp4's
202.967 s. The INHERITED 30-beat map dated 2026-07-29 that was in this file was
DISCARDED, not re-timed: it ran on a 171.6 s timeline against the real 202.9 s,
i.e. it was adrift by a growing margin that reached most of a whole segment by the
end of the story.

⚠️ SOURCING TRAP CHECKED AND CLEARED. This build carries a `make_narration.py`
`.pre-speaker` sibling, and the two DO disagree — but not ambiguously: the sibling
is the whole pre-SPEAKER-LAW script and has no j6/j7a/j7b/j12/n5b/n10b in it at
all, while those six mp3s exist in `audio/`. Eight segments were transcribed with
faster-whisper (n1, n5, n5b, n6, n10, n10b, n14, card) and every one matches the
LIVE script word for word, including the two the SPEAKER-LAW rebuild trimmed
(n5 loses its last sentence, n6 is rewritten). So the live script is authoritative
and NO `TEXT_OVERRIDES` are needed on this row.

SCRIPTURE FACTS (Matthew 20:1-16 KJV):
  v1    "an householder, which went out EARLY IN THE MORNING to hire labourers
        into his vineyard" — first light, before the sun clears the ridge.
  v2    "agreed with the labourers for a PENNY A DAY" — one silver denarius, the
        ordinary full day's wage. Countable: ONE coin, never a handful.
  v3    "about the THIRD HOUR" (~9 a.m.) "standing IDLE IN THE MARKETPLACE."
  v5    "about the SIXTH and NINTH HOUR" (noon and ~3 p.m.).
  v6    "about the ELEVENTH HOUR" (~5 p.m., one hour of daylight left) "Why stand
        ye here all the day idle?"
  v7    "BECAUSE NO MAN HATH HIRED US" — the turn of the whole parable. They were
        not lazy; they were never picked. Their faces carry this row.
  v8    "when EVEN was come ... Call the labourers, and give them their hire,
        BEGINNING FROM THE LAST UNTO THE FIRST" — the order is deliberate and the
        first crew is standing there watching it happen.
  v9-10 each man, first-hired and last-hired alike, receives ONE penny.
  v11   "they MURMURED against the goodman of the house."
  v12   "these last have wrought but ONE HOUR ... we have borne the burden and
        HEAT OF THE DAY."
  v13   "FRIEND, I do thee no wrong" — he does not shout and he does not throw the
        man out. He calls him friend. The warmest frames in the row sit here.
  v15   "Is thine eye evil, because I am GOOD?" — the sentence the whole video is
        built to land.
  v16   "So the last shall be first, and the first last."

WHY-LAW (from the V1 narration script, kept): the first men were not underpaid.
They got everything they agreed to. What stung was watching somebody else get
grace they had not earned.

STAGING ACROSS THE LIBRARY — this row must not repeat a composition already used:
  row 2  (prodigal, Luke 15)     outdoor COURTYARD TABLE, three standing Pharisees
  row 8  (lost coin, Luke 15)    Jesus on a LOW WALL UNDER A FIG TREE
  row 21 (lost sheep, Luke 15)   INSIDE a village house at a crowded meal
  row 16 (Mary & Martha)         a lamplit evening INTERIOR
  row 22 (unmerciful servant)    a BLACK BASALT Capernaum doorstep and street
So this frame story is staged HIGH ON A TERRACED HILLSIDE ABOVE THE VINEYARD
ITSELF, Jesus sitting on the dry-stone retaining wall of a vine terrace with the
rows falling away below him — the parable's own landscape is the backdrop of the
frame that tells it, which no other row uses.

TIME OF DAY IS THE STORY'S OWN CLOCK, and on this row the clock IS the plot:
  b01, b38-b40   the FRAME — clear bright MID-MORNING on the terrace, the sun
                 well up and to the east, crisp shadows. Deliberately NOT dusk, so
                 the frame can never be mistaken for the parable's evening.
  b02-b03        FIRST LIGHT — cold blue-grey air, the sun not yet over the ridge,
                 the first gold just touching the top terraces.
  b04-b05        THIRD HOUR — clean mid-morning sun, short shadows.
  b06            SIXTH HOUR — hard white overhead noon, shadows straight down.
  b07            NINTH HOUR — warm slanting mid-afternoon.
  b08-b16        ELEVENTH HOUR — low gold sun raking along the ground, shadows
                 stretched the length of the square.
  b17-b37        EVENING — the sun already gone behind the western ridge, a warm
                 afterglow in the sky, cool blue shadow filling the vineyard yard,
                 and a clay oil lamp lit at the pay table as it deepens to stars.
No sunrise colouring in the frame story; no midday anywhere after b06; no orange
sunset palette anywhere at all — evening arrives as blue, not as orange.

CHANGING CONDITION (deliberately kept OUT of the locks, which are invariants): the
first-hired man's STATE changes across the row — willing at dawn → sunburnt and
spent → indignant → argued with kindly → quietened. His clothing never changes.
Only posture, dirt, sweat and face carry it. The same is true of the last-hired
man: unwanted → chosen → astonished. Neither man's garment ever changes colour.

CAST NOTE — ANCHOR-FIRST (the row-20/21/22 lesson that took the reroll rate to
10-12%). FOUR story beats are also the identity ANCHORS and are generated in their
OWN run before anything else, each composed so that its character's face is large,
lit and alone in the frame:
  b06  the LANDOWNER, alone in the empty noon square
  b09  the LAST-HIRED man, nearest the camera against the market wall
  b18  the FOREMAN at the pay table with the wage bag
  b21  the FIRST-HIRED man watching the line from further back
Each accepted anchor is then wired into REFS below so every later frame naming
that lock gets the image attached. `v2_gen_api` builds its REFS cache ONCE per
run, so an anchor generated in the same run as its dependants does not exist yet
when they are built — it MUST be a separate invocation.

A FACE SHEET ALONE DOES NOT HOLD A CHARACTER WHO IS SMALL IN FRAME (row 19, Peter
drifting into a grey-haired old man in three wide shots). So every lock below
states age, build, hair and beard as explicit invariants, and those invariants
ride into every beat that names the lock, wide or tight.

CREAM: the landowner is a rich man and the obvious drift is to dress him in pale
linen, which would read as a second, unlocked Jesus. He is pinned to DEEP INDIGO
and DARK OXBLOOD instead, and no worker, foreman or bystander in this row wears
anything pale. The phrase "undyed grey-brown wool" is deliberately NOT used
anywhere in this file: on row 21 it rendered near-white every time.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks NEVER name a
# character. Clothing colours are stated POSITIVELY and DARK.
LOCKS = {
    # ------------------------------------------------------------- people ----
    "LANDOWNER": (
        "LANDOWNER LOCK: the vineyard owner is the SAME man in every shot and "
        "these are invariants that hold even when he is small, distant, in "
        "shadow or out of focus — a man of about fifty-five, broad through the "
        "shoulders and thickening at the waist, tall, with a wide sun-darkened "
        "olive-brown face, a heavy square jaw, calm deep-set dark brown eyes "
        "under level brows, and a FULL IRON-GREY BEARD trimmed square just below "
        "the jaw with thick dark grey hair reaching his collar — never cropped, "
        "never shaved at the sides, never a short modern haircut. He wears an "
        "ankle-length robe of DEEP INDIGO wool under a DARK OXBLOOD-RED mantle "
        "with a narrow band of dull gold thread at its edge, a wide dark leather "
        "belt, a heavy dark leather purse hung from it, and worn dark leather "
        "sandals. His garments are never cream, never off-white, never pale, "
        "never linen-white. His hands are a working farmer's hands, thick and "
        "scarred across the knuckles. His face is shown clearly and is capable of "
        "both great warmth and great firmness; he is never cruel and never smug."
    ),
    "FOREMAN": (
        "FOREMAN LOCK: the steward who pays the wages is the SAME man in every "
        "shot and these are invariants that hold even when he is small, distant "
        "or out of focus — about forty, of medium height and spare build, "
        "weathered brown skin, a long narrow face with a hooked nose, watchful "
        "dark eyes, a SHORT BLACK BEARD clipped close to the jaw and BLACK HAIR "
        "cut to the nape and bound back off his forehead with a twisted dark cord. "
        "He wears a knee-length tunic of DARK OLIVE-BROWN wool over dark brown "
        "leggings, a wide RUSSET sash, and carries a heavy dark leather wage bag "
        "on a strap across his chest. Nothing he wears is cream, off-white or "
        "pale. He is an employee doing an unpleasant job carefully, never a "
        "sneering overseer, and he never carries a whip, rod or weapon."
    ),
    "FIRSTMAN": (
        "FIRST-HIRED MAN LOCK: the labourer hired at first light — the one the "
        "owner later calls friend — is the SAME man in every shot and these are "
        "invariants that hold even when he is small, distant or out of focus — "
        "about thirty-five, lean and hard-muscled with heavy forearms and a "
        "corded neck, sun-blackened olive-brown skin, a square face with a "
        "straight nose and a deep vertical line between his brows, dark brown "
        "eyes, a DENSE BLACK BEARD grown out to two fingers' depth and thick "
        "BLACK HAIR to the tops of his ears bound off his forehead with a strip "
        "of dark cloth. He wears a knee-length work tunic of DEEP UMBER-BROWN "
        "wool, worn through and darkened with sweat at the chest and back, a "
        "twisted rope belt, and bare feet or thin dark sandals. Nothing he wears "
        "is cream, off-white or pale. He is a decent hard-working man who has "
        "been wronged in his own mind, never a villain and never a comic sneer."
    ),
    "LASTMAN": (
        "LAST-HIRED MAN LOCK: the labourer nobody hired until the eleventh hour "
        "is the SAME man in every shot and these are invariants that hold even "
        "when he is small, distant or out of focus — about twenty-six, thin and "
        "wiry with narrow shoulders and visible collarbones, olive-brown skin "
        "gone dusty grey with standing in the road all day, a narrow face with "
        "large dark eyes set wide, a SPARSE SHORT DARK BEARD that has never "
        "filled in properly, and dark brown hair to the jaw pushed back behind "
        "his ears. He wears a knee-length tunic of FADED DARK BROWN wool patched "
        "at one shoulder with a square of DARK RUSSET cloth, a plain cord at the "
        "waist, and bare dusty feet. Nothing he wears is cream, off-white or "
        "pale. He carries himself like a man braced to be turned away again; he "
        "is never idle-looking, never sly, never comic — his face is the face of "
        "somebody who wants to work and was not chosen."
    ),
    "CREW-DAWN": (
        "DAWN CREW LOCK: the labourers hired at first light are six hard-handed "
        "working men between twenty-five and fifty, all with weathered "
        "olive-brown skin, dark beards and dark hair either bound back or covered "
        "by a wound headcloth. Their knee-length work tunics are DEEP UMBER, DARK "
        "INDIGO, DEEP RUSSET, DARK OLIVE and CHARCOAL BROWN — all of them dark, "
        "and none of them cream, off-white, pale, bleached or grey-white; the two "
        "men nearest the camera are always in DEEP UMBER and DARK INDIGO. Each man "
        "has his own distinct face and none is a copy of another. They carry hand "
        "tools of wood and forged iron — a pruning hook, a short mattock, a "
        "woven-fibre carrying basket — and nothing else."
    ),
    "CREW-LATE": (
        "LATE CREW LOCK: the labourers hired through the middle of the day are "
        "five men between twenty and forty-five with weathered olive-brown skin, "
        "dark hair and dark beards, in knee-length tunics of DARK OCHRE, DEEP "
        "BROWN, DARK RUSSET, CHARCOAL and DARK OLIVE — all dark, none cream, "
        "off-white, pale or bleached. Each has his own distinct face. They carry "
        "nothing but their own hands and, between two of them, one hand-woven "
        "fibre basket."
    ),
    "CREW-LAST": (
        "ELEVENTH-HOUR CREW LOCK: the men still standing in the square at the end "
        "of the day are exactly THREE and they can be counted: the last-hired man "
        "nearest the camera plus two others — one grey-bearded and stooped of "
        "about sixty in a DARK CHARCOAL tunic, and one broad-shouldered man of "
        "about thirty in DEEP RUSSET. Their clothing is dark and none of it is "
        "cream, off-white, pale or bleached. They are lean, dusty and tired from "
        "standing, not lounging, not asleep and not drunk."
    ),
    "LISTENERS": (
        "LISTENERS LOCK: the people listening to Jesus on the terrace are exactly "
        "FIVE and they can be counted — three men and two women, ordinary "
        "Galilean villagers between twenty and sixty, weathered olive-brown skin, "
        "the men bearded with wound headcloths, the women in headcloths covering "
        "their hair. Their clothing is DEEP INDIGO, DARK UMBER, DEEP RUSSET, DARK "
        "OCHRE and CHARCOAL BROWN — every one of them dark, and NOT ONE of them "
        "in cream, off-white, pale or bleached cloth of any kind, including at "
        "the blurred edges of the frame. They sit and stand on the terrace stones "
        "listening, never posed in a row, never facing the camera."
    ),
    # ----------------------------------------------------------- settings ----
    "TERRACE": (
        "TERRACE SETTING LOCK: a hillside in the Judean hill country cut into "
        "long horizontal vine terraces, each held up by a dry-stone retaining "
        "wall of stacked honey-coloured limestone about waist high, with rows of "
        "low goblet-pruned grapevines on the flat earth behind each wall and the "
        "hillside falling away in step after step to a dry valley floor. There is "
        "bare pale rock, thistle, dust and a single wind-bent fig tree. "
        "Everything built here is dry-stacked stone, hewn timber, fired clay or "
        "hand-forged iron; there is no mortar, no plaster, no wire, no post and "
        "no fence of any modern kind, and no building of any sort on the skyline "
        "except the flat mud-and-timber roofs of a small stone village far off in "
        "the valley — no tower, no dome, no spire, no minaret, no tiled roof."
    ),
    "VINEYARD": (
        "VINEYARD SETTING LOCK: a working first-century vineyard on terraced "
        "ground — rows of low goblet-pruned vines trained on short forked wooden "
        "stakes, the earth between the rows dry, pale and cracked. THE SEASON IS "
        "THE SAME IN EVERY SINGLE FRAME OF THIS STORY: every vine stands in FULL "
        "GREEN LEAF and carries heavy clusters of dusty dark ripe grapes, so the "
        "rows read as continuous banks of green foliage. No vine anywhere in the "
        "picture is a bare pruned-back winter stump, leafless, dormant or stripped "
        "of fruit. At its head stand a square dry-stone watchtower two "
        "storeys high with an open timber-framed doorway, a shallow rock-cut "
        "winepress with a channel and a lower catching basin, and a beaten "
        "threshing-yard of packed earth inside a low stone wall with a gap for a "
        "gate. Baskets are hand-woven plant fibre, jars and lamps are fired clay, "
        "tools are hewn wood and hammer-marked iron. There is no wire, no trellis "
        "post of milled timber, no metal fitting, no painted surface and no "
        "lettering anywhere."
    ),
    "MARKET": (
        "MARKET SQUARE SETTING LOCK: the open hiring square just inside the gate "
        "of a small Judean farming village — packed earth underfoot, a long "
        "waist-high dry-stone wall down one side with a strip of shade beside it, "
        "single-storey houses of rough limestone blocks with flat roofs of packed "
        "mud over timber beams, low black doorways, and a stone well head with a "
        "worn rope groove. Roofs carry only earth, timber, drying herbs and clay "
        "storage jars — no pipe, no vent, no cable, no aerial, no chimney. The "
        "skyline holds only flat village roofs and the bare ridge behind them: no "
        "dome, no spire, no minaret, no bell tower, no tiled roof. Baskets are "
        "woven fibre, jars are fired clay, and no surface anywhere carries "
        "readable lettering."
    ),
}

REF = True

OUTPUT_ASSET_DIR = "assets"

# REFS — wired in AFTER the four anchor beats (b06, b09, b18, b21) are generated in
# their own run and pass QC. Until then these paths do not exist and v2_gen_api
# prints "character lock MISSING (skipped)" and carries on, which is exactly why
# the anchors must be generated first.
REFS = {
    "LANDOWNER": "assets/s06-again-at-noon.jpeg",
    "LASTMAN": "assets/s09-still-more-men-standing-idle.jpeg",
    "FOREMAN": "assets/s18-beginning-with-the-last.jpeg",
    "FIRSTMAN": "assets/s21-since-dawn-were-thinking.jpeg",
}

BEATS = [
    # ============================== FRAME — the terrace above the vineyard ====
    {
        "id": "v2-r023-b01", "out": "s01-the-kingdom-is-like.jpeg", "seg": "n1",
        "window": "0.28-6.98", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LISTENERS", "TERRACE"],
        "narration": "Jesus said the kingdom of heaven is like a landowner who went out at first light to hire workers for his vineyard.",
        "must_show": "Jesus telling this parable outdoors on a vine terrace in bright mid-morning light, with the terraced vineyard itself falling away below him and five villagers listening.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off Jesus; no dusk, no sunset, no lamp, no synagogue, no temple, no raised platform, no cream or off-white cloth on anybody but Jesus, and nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, clear bright mid-morning sunlight from high "
            "on the left, crisp short shadows, fine film grain. THE CAMERA STANDS ON "
            "THE TERRACE PATH BEHIND TWO SEATED LISTENERS AND SHOOTS PAST THEIR "
            "BACKS: a deep umber shoulder and a dark indigo headcloth fill the near "
            "left and near right of the frame, soft and out of focus, and NOT ONE "
            "FACE IS TURNED TOWARD THE LENS. Beyond them, sharp, Jesus sits on the "
            "waist-high dry-stone retaining wall of the vine terrace with one "
            "sandalled foot on the stones below him and his forearms loose on his "
            "knees. His head is turned down and to his right toward the nearest "
            "listener's face, his eyes fixed on that man inside the frame, and his "
            "right hand is open and lifted a little as he begins the story. Behind "
            "and below him the hillside steps away in terrace after terrace of low "
            "grapevines to a dry valley floor. The three standing listeners are seen "
            "from the side and in three-quarter from behind, all of them looking at "
            "Jesus, none of them squared up to the camera."
        ),
    },
    # ============================== PARABLE — first light, the dawn hiring ====
    {
        "id": "v2-r023-b02", "out": "s02-agreed-on-a-penny.jpeg", "seg": "n2",
        "window": "6.98-11.03", "wide": True, "jesus": False,
        "locks": ["LANDOWNER", "CREW-DAWN", "MARKET"],
        "narration": "He agreed with the first crew on a penny for the day — a full day's fair wage —",
        "must_show": "The landowner striking the day's bargain with six labourers in the village hiring square before sunrise, one small silver coin held up between his finger and thumb so the wage is a visible, single, countable thing.",
        "must_not_show": "no sunrise-orange sky, no sun disc in frame, no heap or handful of coins, no cream or off-white cloth on anyone, no lettering on the coin, nobody looking into the lens.",
        "scene": (
            "One photograph, 40mm lens, the cold blue-grey light of the half hour "
            "before sunrise with only the top of the ridge behind the village "
            "catching the first thin gold, fine film grain. THE CAMERA STANDS AMONG "
            "THE LABOURERS AND SHOOTS PAST THEM toward the landowner: the backs and "
            "shoulders of two of the dawn crew, one in deep umber and one in dark "
            "indigo, fill the near left and near bottom of the frame, out of focus, "
            "and NOT ONE FACE IS TURNED TOWARD THE LENS. Sharp beyond them the "
            "landowner stands square to the group, his right hand raised with ONE "
            "small plain silver coin held edge-on between finger and thumb, his eyes "
            "on the face of the labourer directly in front of him, and his left hand "
            "gripping that man's forearm in the grip that seals a day's agreement. "
            "The other labourers stand loosely around him, all of them looking at the "
            "coin or at the two men. Packed earth underfoot, the long dry-stone wall "
            "behind, flat village roofs and the bare ridge on the skyline."
        ),
    },
    {
        "id": "v2-r023-b03", "out": "s03-out-into-the-rows.jpeg", "seg": "n2",
        "window": "11.03-15.09", "wide": True, "jesus": False,
        "locks": ["CREW-DAWN", "VINEYARD"],
        "narration": "and sent them out into the rows.",
        "must_show": "The dawn crew walking away from the camera up between the vine rows as the first sunlight reaches the top terrace, tools on their shoulders, a full day's work ahead of them.",
        "must_not_show": "no sunset colouring, no sun disc in frame, no landowner, no cream or off-white cloth on anyone, no modern trellis wire or milled posts, nobody looking into the lens.",
        "scene": (
            "One photograph, 50mm lens, first low sunlight coming in from the right "
            "along the terraces so the top row is lit warm gold while the rows below "
            "are still in cool blue shadow, long shadows thrown to the left, fine "
            "film grain. THE CAMERA STANDS AT THE BOTTOM OF THE VINE ROW AND SHOOTS "
            "STRAIGHT UP IT AT THE BACKS OF THE SIX LABOURERS as they walk away from "
            "the lens between the low staked vines: every man is seen from directly "
            "behind or in three-quarter from behind, moving away up the slope, and "
            "NOT ONE FACE IS TURNED TOWARD THE LENS. The nearest man, in deep umber, "
            "carries a short iron mattock over his shoulder; the man beside him in "
            "dark indigo carries a woven fibre basket on his hip. Dust hangs low "
            "around their ankles in the raking light. The dry-stone watchtower stands "
            "at the head of the vineyard ahead of them."
        ),
    },
    # ============================== PARABLE — third hour ====
    {
        "id": "v2-r023-b04", "out": "s04-men-standing-with-no-work.jpeg", "seg": "n3",
        "window": "15.09-20.02", "wide": True, "jesus": False,
        "locks": ["LANDOWNER", "CREW-LATE", "MARKET"],
        "narration": "A few hours later he went back to the market and found more men just standing around with no work.",
        "must_show": "Mid-morning in the hiring square: five men still waiting along the wall with nothing to do, and the landowner arriving into the square and seeing them.",
        "must_not_show": "no dawn or dusk colouring, no market stalls of goods for sale, no cream or off-white cloth on anyone, no crowd of shoppers, nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, clean mid-morning sun from the upper left, "
            "short hard shadows, fine film grain. THE CAMERA STANDS SIDE-ON TO THE "
            "WHOLE SCENE, OUT IN THE MIDDLE OF THE SQUARE, AND LOOKS ALONG THE LINE "
            "OF THE WALL — the landowner enters from the LEFT EDGE of the frame in "
            "full profile, walking rightward across the picture, and the five waiting "
            "labourers are ranged along the wall on the RIGHT, all of them turned to "
            "their right IN PROFILE OR THREE-QUARTER PROFILE toward him. Every "
            "eyeline in the picture runs horizontally ACROSS the frame from right to "
            "left, from the labourers to the landowner inside the picture, and NOT "
            "ONE FACE IS SQUARED UP TO THE LENS OR TURNED TOWARD THE CAMERA. Exactly "
            "five labourers, countable, waiting with nothing in their hands — two "
            "sitting on their heels, three standing, one scraping a line in the dust "
            "with his toe. Packed earth, the strip of shade under the long dry-stone "
            "wall, flat village roofs and the bare ridge behind."
        ),
    },
    {
        "id": "v2-r023-b05", "out": "s05-whatever-is-right.jpeg", "seg": "n3",
        "window": "20.02-25.28", "wide": False, "jesus": False,
        "locks": ["LANDOWNER", "CREW-LATE", "MARKET"],
        "narration": "He sent them into the vineyard too, and promised to pay them what was right.",
        "must_show": "The landowner's open hand pointing the late crew toward the vineyard road, his face steady and matter-of-fact, one labourer already turning to go.",
        "must_not_show": "no coins in this frame, no dawn or dusk colouring, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, clean mid-morning "
            "sun from the upper left, fine film grain. A waist-up three-quarter view "
            "of the landowner from his left side: his right arm is extended and his "
            "open hand points out of the frame to the right toward the vineyard road, "
            "his head turned that way too so his eyes travel clearly past the camera "
            "and out through the right edge of the picture. His mouth is set in the "
            "plain expression of a man stating terms he intends to keep. Close in "
            "front of him and sharp, the shoulder and turning head of one labourer in "
            "dark ochre who has already begun to move in the direction the hand "
            "points, his face in profile. Behind them the dry-stone wall and two more "
            "of the late crew rising to their feet, soft and out of focus."
        ),
    },
    # ============================== PARABLE — sixth hour (LANDOWNER ANCHOR) ====
    {
        "id": "v2-r023-b06", "out": "s06-again-at-noon.jpeg", "seg": "n4",
        "window": "25.28-29.49", "wide": False, "jesus": False,
        "locks": ["LANDOWNER", "MARKET"],
        "narration": "He did the same thing again at noon,",
        "must_show": "IDENTITY ANCHOR — the landowner alone in the emptied square at hard midday, his face large, clearly lit and fully readable, looking along the shaded wall for anyone still unhired.",
        "must_not_show": "no other person in the frame, no dawn or dusk colouring, no long shadows, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, hard white "
            "overhead noon sun dropping shadow straight down under his brows and "
            "nose, a bounce of warm light coming back up off the pale packed earth to "
            "fill the underside of his face, fine film grain. A chest-up "
            "three-quarter view of the landowner standing alone in the middle of the "
            "empty hiring square. His head is turned to his right and slightly down "
            "as he searches the strip of shade under the long wall: his eyes are "
            "fixed on that shaded wall inside the frame and travel clearly out "
            "through the right edge of the picture, nowhere near the lens. His "
            "iron-grey beard, the deep lines beside his eyes and the weave of his "
            "deep indigo robe and dark oxblood mantle are all sharp and fully "
            "legible. Behind him the square is empty, the single-storey village "
            "houses and the dry-stone wall soft and blown out in the glare."
        ),
    },
    {
        "id": "v2-r023-b07", "out": "s07-and-again-mid-afternoon.jpeg", "seg": "n4",
        "window": "29.49-32.55", "wide": True, "jesus": False,
        "locks": ["CREW-LATE", "VINEYARD"],
        "narration": "and again in the middle of the afternoon. More workers, the same promise.",
        "must_show": "A fresh group of labourers arriving into the vineyard in warm mid-afternoon light and starting work among the vines, while men hired earlier are already deep in the rows.",
        "must_not_show": "no noon overhead light, no dusk, no landowner, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, warm slanting mid-afternoon sun from the "
            "right laying soft long shadows across the terrace, fine film grain. THE "
            "CAMERA IS SET LOW BEHIND THE ARRIVING MEN AND SHOOTS PAST THEM DOWN THE "
            "ROW: the backs of three labourers in dark ochre, deep brown and charcoal "
            "fill the near frame as they step in among the vines, seen from directly "
            "behind and in three-quarter from behind, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. Ahead of them and sharp, two men hired earlier are "
            "already bent in among the vines, both in profile with their eyes on the "
            "heavy dark grape clusters in their hands. THE VINES ARE IN FULL GREEN "
            "LEAF AND HANGING WITH RIPE FRUIT ON EVERY ROW, near and far, so the "
            "terrace reads as a bank of green foliage — not one bare, leafless or "
            "winter-pruned stump anywhere in the picture. Dust, dry cracked earth "
            "between the rows, the dry-stone watchtower standing beyond them."
        ),
    },
    # ============================== PARABLE — eleventh hour ====
    {
        "id": "v2-r023-b08", "out": "s08-one-hour-of-daylight-left.jpeg", "seg": "n5",
        "window": "32.55-36.40", "wide": True, "jesus": False,
        "locks": ["LANDOWNER", "MARKET"],
        "narration": "Then, with only one hour of daylight left, he went out a final time",
        "must_show": "The landowner walking back into the hiring square one last time with the sun almost down, his own shadow thrown the whole length of the square ahead of him.",
        "must_not_show": "no sun disc in frame, no orange sunset sky, no lamps or torches yet, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 28mm lens, very low gold sunlight raking in from the "
            "left just above the rooftops so every upright thing throws a shadow "
            "stretched right across the square, the sky above a clear pale blue "
            "rather than an orange sunset, fine film grain. THE CAMERA STANDS LOW IN "
            "THE SQUARE AHEAD OF THE LANDOWNER, SHOOTING BACK ALONG HIS OWN SHADOW so "
            "the long dark shape of him reaches toward the lens across the packed "
            "earth; he is seen from the side in full profile as he walks in from the "
            "gate, his head turned to his left toward the shaded wall he is coming to "
            "search, his eyes travelling out through the left edge of the frame and "
            "nowhere near the camera. The square is otherwise empty in the "
            "foreground. Flat village roofs, the dry-stone wall and the bare ridge on "
            "the skyline."
        ),
    },
    {
        "id": "v2-r023-b09", "out": "s09-still-more-men-standing-idle.jpeg", "seg": "n5",
        "window": "36.40-40.24", "wide": False, "jesus": False,
        "locks": ["LASTMAN", "CREW-LAST", "MARKET"],
        "narration": "and found still more men standing idle.",
        "must_show": "IDENTITY ANCHOR — the last-hired man's face large, clearly lit and fully readable as he stands against the market wall at the end of the day with two other unhired men, watching the empty road for anyone who might still come.",
        "must_not_show": "no landowner in this frame, no more than three waiting men, no lounging or sleeping, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, very low "
            "gold sunlight coming in from the left across his face so one cheek is "
            "warmly lit and the other falls into soft shadow, fine film grain. A "
            "chest-up three-quarter view of the last-hired man standing with his "
            "shoulder against the dry-stone wall. His head is turned to his left and "
            "lifted slightly as he watches the empty road running out through the "
            "left edge of the frame: his eyes are on that road, sharp and hoping, and "
            "his pupils are nowhere near the lens. Dust is grey in his sparse beard "
            "and along his cheekbone; his large dark eyes, the patch of dark russet "
            "cloth at his shoulder and the weave of his faded dark brown tunic are "
            "all fully legible. Exactly two other waiting men stand further along the "
            "wall behind him, both soft and out of focus, one stooped and "
            "grey-bearded and one broad-shouldered, both looking the same way he is."
        ),
    },
    {
        "id": "v2-r023-b10", "out": "s10-why-stand-ye-here-idle.jpeg", "seg": "j6",
        "window": "40.24-43.94", "wide": False, "jesus": False,
        "locks": ["LANDOWNER", "LASTMAN", "CREW-LAST", "MARKET"],
        "narration": "Why stand ye here all the day idle?",
        "must_show": "The landowner stopped in front of the three waiting men and asking them the question, his face open and genuinely enquiring rather than accusing.",
        "must_not_show": "no anger, no pointing finger, no raised hand, no scolding expression, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 50mm lens, very low gold sidelight from the left, fine "
            "film grain. THE CAMERA IS OVER THE LAST-HIRED MAN'S RIGHT SHOULDER: the "
            "back of his head and the patched shoulder of his faded dark brown tunic "
            "fill the near left of the frame, out of focus, and his face is not "
            "visible to the lens. Sharp beyond him the landowner has stopped a pace "
            "away and stands square to him, his weight settled, his head tipped a "
            "little as he asks — his deep-set eyes fixed on that man's face inside "
            "the frame, warm and puzzled rather than hard, and his hands open and "
            "loose at his sides. The other two waiting men stand behind him along the "
            "wall, both turned toward the landowner. The square behind is empty and "
            "raked with long shadow."
        ),
    },
    {
        "id": "v2-r023-b11", "out": "s11-no-man-hath-hired-us.jpeg", "seg": "j7a",
        "window": "43.94-47.46", "wide": False, "jesus": False,
        "locks": ["LASTMAN", "MARKET"],
        "narration": "Because no man hath hired us.",
        "must_show": "The last-hired man answering — the single most important face in this video: not lazy, not ashamed of being lazy, but the plain worn honesty of a man who waited all day and was never chosen.",
        "must_not_show": "no smirk, no shrug of indifference, no comic expression, no tears running, no landowner's face, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 105mm lens, very shallow depth of field, very low warm "
            "gold light from the left, fine film grain. A tight head-and-shoulders "
            "frame of the last-hired man mid-sentence. His chin is lifted just enough "
            "to answer and his head is turned a few degrees to his left, so his gaze "
            "goes to the landowner's face standing just off frame to the left and "
            "exits cleanly through the left edge of the picture, far off the camera "
            "axis. His mouth is open on the word; his brows are drawn slightly "
            "together; his eyes are steady and tired and completely without guile. "
            "Grey road dust lies in the creases of his neck and in his sparse beard. "
            "Behind him the dry-stone wall and the empty square dissolve into warm "
            "out-of-focus gold."
        ),
    },
    {
        "id": "v2-r023-b12", "out": "s12-not-lazy-not-hiding.jpeg", "seg": "n5b",
        "window": "47.46-51.97", "wide": False, "jesus": False,
        "locks": ["LASTMAN", "CREW-LAST", "MARKET"],
        "narration": "Why have you stood here all day doing nothing, he asked them. Not lazy. Not hiding.",
        "must_show": "Proof on their bodies that these are working men who were never given work — hard calloused hands hanging empty, and their own tools set ready against the wall all day and never used.",
        "must_not_show": "no faces filling the frame, no lounging or sleeping, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 60mm close-focus lens, shallow depth of field, very low "
            "gold sidelight from the left picking out every ridge and crack, fine "
            "film grain. A waist-down framing: three pairs of hands hanging empty at "
            "the men's sides against the dark wool of their tunics, thick with "
            "callus, split at the knuckles, grey with road dust. Propped against the "
            "dry-stone wall beside their bare dusty feet stand their own tools, "
            "hewn-wood and hammer-marked iron — a short mattock and a pruning hook — "
            "clean and unused, with a fine skin of dust settled along the top edge of "
            "each blade. No face is inside this frame at all. Behind them the wall "
            "stones and the long shadow lying across the packed earth."
        ),
    },
    {
        "id": "v2-r023-b13", "out": "s13-nobody-had-picked-them.jpeg", "seg": "n5b",
        "window": "51.97-55.46", "wide": True, "jesus": False,
        "locks": ["LASTMAN", "CREW-LAST", "MARKET"],
        "narration": "Nobody had ever picked them.",
        "must_show": "The loneliness of being the ones left: three small figures still at the wall in an otherwise wholly empty square, with the trampled ground showing where everybody else walked away hours ago.",
        "must_not_show": "no other people anywhere in the square, no landowner, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 24mm wide lens, very low gold light from the left, fine "
            "film grain. THE CAMERA STANDS FAR BACK ACROSS THE SQUARE AND SLIGHTLY "
            "BEHIND THE THREE MEN, SHOOTING PAST THEIR BACKS along the length of the "
            "dry-stone wall: all three are seen from behind and in three-quarter from "
            "behind, small in the frame and pressed to one side of it, and NOT ONE "
            "FACE IS TURNED TOWARD THE LENS. The whole rest of the square opens out "
            "empty in front of them, its packed earth churned all over with the "
            "footprints and cart ruts of everybody who was hired and left. Their "
            "three shadows are thrown enormously long across that empty ground. The "
            "village roofs and the bare ridge sit low on the skyline and the sky "
            "above is clear pale blue."
        ),
    },
    {
        "id": "v2-r023-b14", "out": "s14-go-ye-also-into-the-vineyard.jpeg", "seg": "j7b",
        "window": "55.46-62.40", "wide": False, "jesus": False,
        "locks": ["LANDOWNER", "LASTMAN", "MARKET"],
        "narration": "Go ye also into the vineyard; and whatsoever is right, that shall ye receive.",
        "must_show": "The moment of being chosen: the landowner's open hand held out toward the vineyard road, and the last-hired man's face changing as he understands it is meant for him.",
        "must_not_show": "no coins in this frame, no kneeling, no grovelling, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, very low gold light "
            "from the left, fine film grain. Two figures close together in "
            "three-quarter profile, both facing across the frame rather than out of "
            "it. On the right, sharp, the landowner with his right arm swung open and "
            "his broad scarred hand held out flat toward the vineyard road, his head "
            "turned back to his left so his eyes rest on the last-hired man's face "
            "inside the frame. On the left, also sharp, the last-hired man has "
            "half-turned to follow that hand: his eyes are on the landowner's open "
            "palm inside the frame, his lips just parted, the braced-for-refusal set "
            "of his shoulders coming loose. HE IS THE SAME MAN AS IN EVERY OTHER "
            "PICTURE OF HIM AND HIS IDENTITY IS RESTATED HERE SO IT CANNOT DRIFT: "
            "about twenty-six, thin and wiry with narrow shoulders, a narrow face "
            "with large dark eyes set wide, a sparse short dark beard that has never "
            "filled in, dark brown hair to the jaw pushed back behind his ears, and "
            "a knee-length tunic of DEEP DARK BROWN wool — dark, never pale, never "
            "light tan, never grey-white, never cream — patched at one shoulder with "
            "a square of DARK RUSSET cloth. Neither man's pupils go anywhere near "
            "the lens. Behind them the empty square and the wall fall away into warm "
            "gold blur."
        ),
    },
    {
        "id": "v2-r023-b15", "out": "s15-you-go-in-too.jpeg", "seg": "n6",
        "window": "62.40-68.20", "wide": True, "jesus": False,
        "locks": ["LASTMAN", "CREW-LAST", "VINEYARD"],
        "narration": "You go into the vineyard too, he told them, and whatever is right, that is what you will get.",
        "must_show": "The three eleventh-hour men going up the terrace path into the vines at last, hurrying, with barely any daylight left on the rows.",
        "must_not_show": "no landowner, no sun disc in frame, no orange sunset sky, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, the last low gold light lying only along the "
            "top terrace while the lower rows have already gone blue with shadow, "
            "fine film grain. THE CAMERA STANDS AT THE FOOT OF THE TERRACE PATH AND "
            "SHOOTS UP IT AT THE BACKS OF THE THREE MEN as they climb away from the "
            "lens between the low staked vines: all three are seen from directly "
            "behind and in three-quarter from behind, moving away up the slope, and "
            "NOT ONE FACE IS TURNED TOWARD THE LENS. The last-hired man is nearest "
            "the camera, the patched dark russet square at his shoulder catching the "
            "light, taking the path two steps at a time. Dust lifts around their "
            "feet. The dry-stone watchtower stands dark against the pale sky ahead."
        ),
    },
    {
        "id": "v2-r023-b16", "out": "s16-still-out-looking.jpeg", "seg": "n6",
        "window": "68.20-73.51", "wide": False, "jesus": False,
        "locks": ["LANDOWNER", "MARKET"],
        "narration": "One hour of daylight left, and he was still out looking for people.",
        "must_show": "The landowner left alone in the emptied square, not going home yet, still watching the road and the doorways for one more person to hire.",
        "must_not_show": "no other person in the frame, no lamps or torches, no sun disc, no orange sunset sky, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, the very last low "
            "gold light coming in from the left and already going thin, fine film "
            "grain. A three-quarter chest-up view of the landowner standing alone. "
            "His head is turned away to his right and slightly up as he searches the "
            "far end of the square, so his eyes travel clearly out through the right "
            "edge of the frame and nowhere near the camera; one hand rests on the "
            "heavy leather purse at his belt. His face is patient and unhurried, the "
            "face of a man in no rush to stop looking. Behind him the empty square "
            "and the low doorways of the houses are soft and dim, the light dying out "
            "of them."
        ),
    },
    # ============================== PARABLE — evening and the reckoning ====
    {
        "id": "v2-r023-b17", "out": "s17-when-evening-came.jpeg", "seg": "n7",
        "window": "73.51-77.91", "wide": False, "jesus": False,
        "locks": ["LANDOWNER", "FOREMAN", "VINEYARD"],
        "narration": "When evening came, the owner told his foreman to call the workers and pay them —",
        "must_show": "The landowner giving the foreman his instruction in the vineyard yard after sundown, the wage bag already on the foreman's shoulder.",
        "must_not_show": "no sun in the sky, no orange sunset glare, no daylight on the ground, no workers yet, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, the sun already gone "
            "behind the western ridge — a soft cool light left high in the sky, blue "
            "shadow filling the yard, and one clay oil lamp with a bare wick burning "
            "on the low stone wall throwing a small pool of warm light, fine film "
            "grain. Two men in three-quarter profile facing each other across the "
            "frame. On the left, sharp, the landowner leans in with one hand on the "
            "foreman's shoulder, his head turned so his eyes are on the foreman's "
            "face inside the frame, speaking low. On the right the foreman listens "
            "with his head bent toward him, eyes down on the packed earth between "
            "them, the heavy dark leather wage bag already slung across his chest and "
            "one hand resting on it. Neither man's gaze comes near the lens. Behind "
            "them the dry-stone watchtower and the vine rows go dark blue."
        ),
    },
    {
        "id": "v2-r023-b18", "out": "s18-beginning-with-the-last.jpeg", "seg": "n7",
        "window": "77.91-82.30", "wide": False, "jesus": False,
        "locks": ["FOREMAN", "VINEYARD"],
        "narration": "starting, strangely, with the ones hired last.",
        "must_show": "IDENTITY ANCHOR — the foreman's face large, clearly lit and fully readable in lamplight at the pay table, opening the wage bag and calling the first name down the line.",
        "must_not_show": "no other face in the frame, no daylight, no landowner, no coins spilled in a heap, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, night has "
            "not quite come — the dim blue of the sky after sundown behind him and one clay oil lamp "
            "with a bare wick standing on the table close to his left, so his face is "
            "modelled by warm low lamplight from below and to the side, fine film "
            "grain. A chest-up three-quarter view of the foreman standing behind a "
            "rough hewn-plank table set on the packed earth of the threshing yard. He "
            "has just loosened the mouth of the dark leather wage bag with both hands "
            "and his head is turned to his left and lifted as he calls down the "
            "waiting line: his eyes are fixed along that line inside the frame and "
            "travel out through the left edge of the picture, nowhere near the lens. "
            "His short black beard, the twisted dark cord binding his hair back, the "
            "russet sash and the grain of the plank table are all fully legible. "
            "Behind him the yard and the dark shape of the watchtower fall away out "
            "of focus."
        ),
    },
    {
        "id": "v2-r023-b19", "out": "s19-a-full-days-pay.jpeg", "seg": "n8",
        "window": "82.30-87.73", "wide": False, "jesus": False,
        "locks": ["FOREMAN", "LASTMAN", "VINEYARD"],
        "narration": "The men who had worked a single hour came up first, and each of them was handed a full day's pay.",
        "must_show": "ONE single silver coin passing from the foreman's fingers into the last-hired man's open palm — exactly one coin, plainly countable, nothing else in the hand.",
        "must_not_show": "no handful, heap or scatter of coins, no purse pouring out, no lettering or numerals on the coin, no daylight, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 100mm close-focus lens, very shallow depth of field, "
            "warm low lamplight from a clay oil lamp just out of frame to the left "
            "with deep blue evening dark beyond, fine film grain. A tight framing of "
            "two hands only, cropped at the wrists. From the upper right the "
            "foreman's hand lowers ONE plain hand-struck silver coin, held on edge "
            "between thumb and forefinger, into the open upturned palm of the "
            "last-hired man at lower left — a thin, dusty, work-hardened hand. That "
            "coin is the only coin anywhere in the picture, sharp and unmistakably "
            "single, catching a hard little highlight along its rim. No face is "
            "inside this frame at all. The plank table edge runs beneath, and the "
            "dark yard dissolves behind."
        ),
    },
    {
        "id": "v2-r023-b20", "out": "s20-a-whole-penny-for-one-hour.jpeg", "seg": "n8",
        "window": "87.73-91.66", "wide": False, "jesus": False,
        "locks": ["LASTMAN", "VINEYARD"],
        "narration": "A whole penny, for one hour of work.",
        "must_show": "The last-hired man's face as he looks down at the coin in his own hand and cannot make it add up — astonishment breaking through, not greed.",
        "must_not_show": "no grinning, no comic surprise, no biting the coin, no foreman's face, no daylight, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 85mm lens, very shallow depth of field, warm low "
            "lamplight from below and to the left with deep blue evening dark behind, "
            "fine film grain. A head-and-shoulders frame of the last-hired man. His "
            "head is bowed and his eyes are cast down to his own cupped hands held at "
            "the bottom edge of the frame, where the single silver coin sits in his "
            "palm — his gaze has that coin as its target inside the picture and comes "
            "nowhere near the lens. His lips are parted; his brows have gone up in "
            "the middle; the tendons stand out in his neck. Lamplight catches the wet "
            "in his large dark eyes without a tear falling. Road dust still grey on "
            "his cheek."
        ),
    },
    {
        "id": "v2-r023-b21", "out": "s21-since-dawn-were-thinking.jpeg", "seg": "n9",
        "window": "91.66-94.98", "wide": False, "jesus": False,
        "locks": ["FIRSTMAN", "VINEYARD"],
        "narration": "You can guess what the men who had worked since dawn were thinking.",
        "must_show": "IDENTITY ANCHOR — the first-hired man's face large, clearly lit and fully readable as he watches the pay table from further back in the line, doing arithmetic in his head.",
        "must_not_show": "no other face in the frame, no anger yet, no daylight, no coins, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, warm low "
            "lamplight reaching him from the pay table off to his left with deep blue "
            "evening dark filling everything behind him, fine film grain. A chest-up "
            "three-quarter view of the first-hired man standing back in the waiting "
            "line. His head is turned to his left and levelled as he watches the "
            "table: his eyes are fixed on that table inside the frame and travel out "
            "through the left edge of the picture, nowhere near the lens. His jaw is "
            "set and the deep vertical line between his brows has drawn in — "
            "calculating, not yet angry. A whole day is on him: sunburn across the "
            "bridge of his nose, dried salt in the dense black beard, his deep "
            "umber-brown tunic dark with sweat down the chest, dust to the knee. The "
            "yard behind him is out of focus and almost dark."
        ),
    },
    {
        "id": "v2-r023-b22", "out": "s22-surely-they-would-get-more.jpeg", "seg": "n9",
        "window": "94.98-100.31", "wide": True, "jesus": False,
        "locks": ["FIRSTMAN", "CREW-DAWN", "VINEYARD"],
        "narration": "If the one-hour crew got a full penny, surely they would get more.",
        "must_show": "The dawn crew murmuring to each other in the line, heads inclined together, all of their attention on the pay table ahead of them.",
        "must_not_show": "no shouting yet, no shoving, no coins in this frame, no daylight, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 40mm lens, warm low lamplight from far ahead of the line "
            "picking out the near edges of the men while the rest of them stays in "
            "cool blue evening dark, fine film grain. THE CAMERA STANDS IN THE LINE "
            "BEHIND THE DAWN CREW AND SHOOTS PAST THEM toward the lamplit pay table: "
            "their backs and shoulders fill the near frame, the two nearest in deep "
            "umber and dark indigo, seen from directly behind and in three-quarter "
            "from behind, and NOT ONE FACE IS TURNED TOWARD THE LENS. Two of them "
            "have leaned their heads together in profile, one talking low against the "
            "other's ear, and every face that can be seen at all is angled away "
            "toward the table ahead. The lamp on that table is a small warm point "
            "deep in the frame with the foreman's dark shape beside it."
        ),
    },
    {
        "id": "v2-r023-b23", "out": "s23-the-very-same-one-penny.jpeg", "seg": "n10",
        "window": "100.31-106.75", "wide": False, "jesus": False,
        "locks": ["FIRSTMAN", "VINEYARD"],
        "narration": "But when their turn came, they got the very same — one penny. And they were furious.",
        "must_show": "One single silver coin lying in the first-hired man's split, blistered, filthy hand, with his own face above it hardening as he takes in that it is all there is.",
        "must_not_show": "no second coin anywhere, no throwing the coin, no violence, no daylight, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 70mm lens, shallow depth of field, warm low lamplight "
            "from the left, deep blue dark behind, fine film grain. A vertical "
            "framing that holds his open right hand low and large in the near "
            "foreground, sharp — the palm split, blistered at the base of the "
            "fingers, black with vine dirt — with exactly ONE plain hand-struck "
            "silver coin lying flat in it and nothing else. Above and slightly "
            "behind, still readable but a touch softer, his own face is bent down "
            "over that hand: his eyes are locked on the coin inside the frame, his "
            "jaw clamped, his nostrils flared, the vertical line between his brows "
            "cut deep. His gaze never approaches the lens. XX"
        ),
    },
    {
        "id": "v2-r023-b24", "out": "s24-thou-hast-made-them-equal.jpeg", "seg": "j12",
        "window": "106.75-111.50", "wide": False, "jesus": False,
        "locks": ["FIRSTMAN", "LASTMAN", "VINEYARD"],
        "narration": "These last have wrought but one hour, and thou hast made them equal unto us,",
        "must_show": "The first-hired man's arm flung back to point at the eleventh-hour men behind him — the comparison itself, made visible in one gesture.",
        "must_not_show": "no striking, no grabbing, no fist, no coins spilling, no daylight, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, warm low lamplight from the right, deep blue "
            "evening dark elsewhere, fine film grain. The first-hired man stands in "
            "the near left of the frame in three-quarter profile, his body turned "
            "toward the pay table off to the right and his left arm flung back and "
            "out behind him with the hand open, pointing across the frame at the "
            "eleventh-hour men — his head is turned to the right, his eyes on the "
            "table inside the frame, travelling out through the right edge and "
            "nowhere near the lens, his mouth open on the accusation. HE IS THE SAME "
            "MAN AS IN EVERY OTHER PICTURE OF HIM AND HIS IDENTITY IS RESTATED HERE "
            "SO IT CANNOT DRIFT: about thirty-five, lean and hard-muscled with heavy "
            "forearms and a corded neck, sun-blackened olive-brown skin, a square "
            "face with a deep vertical line between his brows, a DENSE BLACK BEARD "
            "grown out two fingers deep, thick BLACK HAIR bound off his forehead "
            "with a STRIP OF DARK CLOTH TIED ROUND HIS HEAD, and a sweat-darkened "
            "DEEP UMBER-BROWN work tunic. Behind his "
            "pointing hand and sharp enough to read, the last-hired man stands "
            "quietly holding his own coin, his head down, not answering. The lamp on "
            "the table burns at the right edge of the picture."
        ),
    },
    {
        "id": "v2-r023-b25", "out": "s25-the-burden-and-the-heat.jpeg", "seg": "j12",
        "window": "111.50-116.25", "wide": False, "jesus": False,
        "locks": ["FIRSTMAN", "CREW-DAWN", "VINEYARD"],
        "narration": "which have borne the burden and heat of the day.",
        "must_show": "What a whole day in the sun actually costs a body — burnt necks, sweat-stiffened wool, and dirt worked into every crease of the dawn crew.",
        "must_not_show": "no faces filling the frame, no blood, no wounds, no daylight, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 90mm close-focus lens, very shallow depth of field, warm "
            "raking lamplight from the left with deep blue dark behind, fine film "
            "grain. A close framing of the dawn crew from behind and to the side at "
            "shoulder height, faces out of frame above the top edge: the back of one "
            "man's neck fills the near left, burnt brick-red across the top and "
            "banded darker where a headcloth sat, running with dried sweat tracks "
            "through the dust. Beside it the deep umber wool of another man's tunic "
            "is stiffened dark across the shoulder blades with dried salt, its weave "
            "clogged with vine dust, and one forearm hangs into the frame corded and "
            "grimed with dirt driven into every crease and under every nail. Nothing "
            "in this picture is clean."
        ),
    },
    {
        "id": "v2-r023-b26", "out": "s26-you-made-them-equal-to-us.jpeg", "seg": "n10b",
        "window": "116.25-120.48", "wide": True, "jesus": False,
        "locks": ["FIRSTMAN", "FOREMAN", "CREW-DAWN", "VINEYARD"],
        "narration": "These men worked one hour, they said, and you have made them equal to us",
        "must_show": "The argument itself at the pay table: the dawn crew pressed forward complaining, the foreman standing his ground behind the table with the wage bag.",
        "must_not_show": "no violence, no overturned table, no weapons, no landowner yet, no daylight, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 28mm lens, warm lamplight from the clay oil lamp on the "
            "table throwing the men's shadows huge and ragged onto the dry-stone wall "
            "behind, deep blue evening dark above, fine film grain. THE CAMERA STANDS "
            "BEHIND AND BETWEEN THE COMPLAINING MEN AND SHOOTS PAST THEIR BACKS "
            "ACROSS THE TABLE: three dark backs and shoulders, the nearest in deep "
            "umber and dark indigo, crowd the near frame from behind and in "
            "three-quarter from behind, and NOT ONE FACE IS TURNED TOWARD THE LENS. "
            "Sharp beyond them the foreman stands his ground behind the plank table "
            "with both hands flat on the boards, his head lifted and his eyes going "
            "from one complaining man to the next inside the frame. The first-hired "
            "man is nearest the table on the left, one arm raised, seen from behind. "
            "The wage bag sits between the foreman's hands."
        ),
    },
    {
        "id": "v2-r023-b27", "out": "s27-we-carried-the-whole-day.jpeg", "seg": "n10b",
        "window": "120.48-124.72", "wide": False, "jesus": False,
        "locks": ["FIRSTMAN", "VINEYARD"],
        "narration": "and we carried the whole day and the burning heat of it.",
        "must_show": "The first-hired man's two hands thrust palms-up across the table as his whole argument — split, blistered, black with dirt, with the single coin still lying in one of them.",
        "must_not_show": "no second coin, no blood, no open wounds, no daylight, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 65mm close-focus lens, shallow depth of field, warm "
            "lamplight raking across from the right so every crack and blister throws "
            "its own small shadow, deep blue dark behind, fine film grain. Both of "
            "the first-hired man's hands are thrust forward palms-up over the plank "
            "table, large and sharp in the near frame, cropped at the wrists — the "
            "callus at the base of the fingers split open and shining, the creases "
            "packed black with vine dirt, one silver coin lying flat and alone in the "
            "right palm. Above and behind them his own chin, beard and open mouth are "
            "just inside the top of the frame and out of focus, angled away to the "
            "right; his eyes are not visible to the camera at all. The foreman's dark "
            "olive-brown sleeve and the wage bag sit soft across the table."
        ),
    },
    # ============================== PARABLE — the owner answers ====
    {
        "id": "v2-r023-b28", "out": "s28-he-called-him-friend.jpeg", "seg": "n11",
        "window": "124.72-130.45", "wide": False, "jesus": False,
        "locks": ["LANDOWNER", "FIRSTMAN", "VINEYARD"],
        "narration": "The owner turned to one of them, and he was not harsh about it. He called him friend.",
        "must_show": "The warmest frame in the row — the landowner having come around the table to the angry man himself, his hand settling on the man's shoulder, his face entirely without contempt.",
        "must_not_show": "no anger on the landowner, no pointing, no shouting, no crowd pressing in, no daylight, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 60mm lens, shallow depth of field, warm lamplight from "
            "the left with soft blue evening dark behind, fine film grain. Two men "
            "close together in three-quarter profile facing each other across the "
            "frame. On the right, sharp, the landowner has come around from the table "
            "and stands half a pace from the first-hired man, his broad scarred right "
            "hand laid flat and unhurried on that man's shoulder, his head bent a "
            "little toward him and his deep-set eyes resting steadily on the man's "
            "face inside the frame. His expression is warm, level and completely "
            "without contempt. On the left the first-hired man is caught mid-turn "
            "toward him, still stiff with anger, his eyes coming up to meet the "
            "landowner's inside the picture. Neither man's gaze goes near the lens. "
            "The lamplit table edge burns warm at the right of the frame."
        ),
    },
    {
        "id": "v2-r023-b29", "out": "s29-didst-not-thou-agree.jpeg", "seg": "j1",
        "window": "130.45-135.47", "wide": False, "jesus": False,
        "locks": ["LANDOWNER", "FIRSTMAN", "VINEYARD"],
        "narration": "Friend, I do thee no wrong: didst not thou agree with me for a penny?",
        "must_show": "The landowner asking the question straight to the man's face, reasonable and unhurried, reminding him of a bargain they both made at dawn.",
        "must_not_show": "no scolding finger, no raised-voice posture, no crowd, no daylight, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 85mm lens, very shallow depth of field, warm lamplight "
            "from the lower left, blue dark behind, fine film grain. THE CAMERA IS "
            "OVER THE FIRST-HIRED MAN'S LEFT SHOULDER: the dark umber-brown wool of "
            "his shoulder and the edge of his black beard fill the near right of the "
            "frame, out of focus, and his face is not visible to the lens. Sharp "
            "beyond, the landowner's head and shoulders fill the left of the picture, "
            "turned three-quarters toward that shoulder — his eyes are fixed on the "
            "man's face inside the frame, patient and direct, his mouth open on the "
            "question, his iron-grey beard and the deep lines beside his eyes lit "
            "warmly from below. One of his hands is lifted just into frame, palm up "
            "and open, asking rather than accusing."
        ),
    },
    {
        "id": "v2-r023-b30", "out": "s30-i-will-give-unto-the-last.jpeg", "seg": "j1",
        "window": "135.47-142.38", "wide": False, "jesus": False,
        "locks": ["LANDOWNER", "FIRSTMAN", "LASTMAN", "VINEYARD"],
        "narration": "Take that thine is, and go thy way: I will give unto the last, even as unto thee.",
        "must_show": "The landowner's two hands making the whole argument at once — one turned toward the coin already in the first man's grasp, the other opened toward the last-hired man standing quietly behind.",
        "must_not_show": "no coins in the landowner's own hands, no crowd, no daylight, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 50mm lens, warm lamplight from the left, blue evening "
            "dark beyond, fine film grain. A waist-up two-shot in three-quarter "
            "profile. On the left, sharp, the landowner stands with his right hand "
            "turned palm-up toward the first-hired man's closed fist at the bottom "
            "left of the frame, and his left arm opened wide across the picture, palm "
            "up, toward the last-hired man who stands further back on the right. His "
            "head follows the left hand, so his eyes travel across the frame to the "
            "last-hired man's face inside the picture. The first-hired man is a dark "
            "shoulder and turned head at the near left edge, seen from behind. The "
            "last-hired man, softer but clearly readable, stands still with his own "
            "coin held against his chest, looking back at the landowner. Every gaze "
            "in the frame ends on another face inside it."
        ),
    },
    {
        "id": "v2-r023-b31", "out": "s31-what-i-will-with-mine-own.jpeg", "seg": "j1",
        "window": "142.38-147.56", "wide": True, "jesus": False,
        "locks": ["LANDOWNER", "FIRSTMAN", "CREW-DAWN", "VINEYARD"],
        "narration": "Is it not lawful for me to do what I will with mine own?",
        "must_show": "The scale of what belongs to him — the whole terraced vineyard standing dark behind the two men in the lamplit yard, so 'mine own' is a visible fact.",
        "must_not_show": "no daylight, no sun, no sunset colour on the horizon, no crowd of strangers, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 24mm wide lens, one small clay oil lamp on the pay table "
            "carrying the only warm light in the picture, the sky above deep blue and "
            "the first stars out, fine film grain. THE CAMERA STANDS BACK IN THE "
            "DARKNESS OF THE YARD BEHIND THE DAWN CREW AND SHOOTS PAST THEIR BACKS "
            "toward the lamp: two dark backs, one deep umber and one dark indigo, "
            "frame the near left and near right edges as silhouettes, and NOT ONE "
            "FACE IS TURNED TOWARD THE LENS. In the lamplight beyond them the "
            "landowner stands in profile with one arm swept out and up across the "
            "picture toward the hillside, the first-hired man facing him in profile "
            "and following that arm with his eyes inside the frame. Behind them both "
            "the terraced vineyard climbs away in step after step of vine rows into "
            "the blue dark, the watchtower a black shape against the sky."
        ),
    },
    {
        "id": "v2-r023-b32", "out": "s32-because-i-am-good.jpeg", "seg": "j1",
        "window": "147.56-151.94", "wide": False, "jesus": False,
        "locks": ["LANDOWNER", "FIRSTMAN", "VINEYARD"],
        "narration": "Is thine eye evil, because I am good?",
        "must_show": "The sentence landing — the first-hired man's face at the exact moment the question stops being about money, with the landowner soft behind him still waiting for an answer.",
        "must_not_show": "no anger on the landowner, no sneer, no comic double-take, no daylight, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 105mm lens, very shallow depth of field, warm lamplight "
            "from the lower right, blue dark behind, fine film grain. A tight "
            "head-and-shoulders frame of the first-hired man, HIS HEAD TURNED FULLY "
            "TO HIS OWN LEFT SO HE IS SEEN IN NEAR PROFILE and the camera sits well "
            "off the axis of his eyes. THE LANDOWNER'S FACE IS THE TARGET AND IT IS "
            "INSIDE THIS FRAME: he stands close on the LEFT, softly out of focus but "
            "plainly there, his iron-grey beard and dark oxblood shoulder filling the "
            "left edge. The first-hired man's eyes are lifted and locked on THAT face "
            "at the left edge, so his gaze crosses the picture horizontally and exits "
            "through the left side — his pupils are nowhere near the lens and he is "
            "not looking out of the picture toward the viewer. The clenched set has gone "
            "out of his jaw and not been replaced by anything yet; his brows have "
            "come up in the middle; his mouth is closed. Lamplight finds the sweat "
            "and dust still on his temple and the salt dried in his black beard."
        ),
    },
    {
        "id": "v2-r023-b33", "out": "s33-exactly-what-we-agreed.jpeg", "seg": "n12",
        "window": "151.94-156.68", "wide": False, "jesus": False,
        "locks": ["FIRSTMAN", "VINEYARD"],
        "narration": "In other words: I have not cheated you. You got exactly what we agreed on.",
        "must_show": "The one coin still in the first-hired man's hand — the full wage, unbroken and not one bit short — his fingers loosening around it rather than throwing it.",
        "must_not_show": "no second coin, no throwing, no coin falling, no lettering or numerals on the coin, no daylight, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 100mm close-focus lens, very shallow depth of field, "
            "warm lamplight from the right, blue dark behind, fine film grain. His "
            "one hand fills the frame, cropped at the wrist, half-opened from a fist "
            "so the fingers are uncurling — and in the middle of that dirty split "
            "palm lies exactly ONE plain hand-struck silver coin, the only coin in "
            "the picture, sharp, catching a clean highlight along its rim. The "
            "callus, blisters and black-packed creases of the hand are all in focus "
            "around it. No face is inside this frame. Beyond the hand the lamplit "
            "plank table and the dark yard fall away into soft blur."
        ),
    },
    {
        "id": "v2-r023-b34", "out": "s34-kindness-to-someone-else.jpeg", "seg": "n12",
        "window": "156.68-160.18", "wide": False, "jesus": False,
        "locks": ["LASTMAN", "VINEYARD"],
        "narration": "Why is my kindness to someone else a problem for you?",
        "must_show": "The man the kindness was actually shown to — the last-hired man standing apart at the edge of the lamplight, still holding his coin, quietly watching the argument he caused.",
        "must_not_show": "no smugness, no gloating, no argument in the near frame, no daylight, no cream or off-white cloth anywhere, nobody looking into the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, warm lamplight "
            "reaching him weakly from the left so only one side of his face and "
            "shoulder is lit and the rest goes into blue dark, fine film grain. A "
            "chest-up three-quarter view of the last-hired man standing back from the "
            "table at the edge of the light, both hands closed around the single coin "
            "and held low against his stomach. His head is turned to his left toward "
            "the lamplit argument, which sits out of focus as warm shapes at the left "
            "edge of the frame: his eyes are on those figures inside the picture and "
            "leave through the left edge, nowhere near the lens. His face is not "
            "pleased and not ashamed — it is careful, watching something happen "
            "because of him."
        ),
    },
    {
        "id": "v2-r023-b35", "out": "s35-angry-because-i-chose-good.jpeg", "seg": "n12",
        "window": "160.18-164.46", "wide": False, "jesus": False,
        "locks": ["FIRSTMAN", "LANDOWNER", "VINEYARD"],
        "narration": "Are you really angry only because I chose to be good?",
        "must_show": "The anger coming apart — the first-hired man's eyes going down and away from the landowner's face, unable to hold the question.",
        "must_not_show": "no tears running, no collapse, no embrace, no smiling, no daylight, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 90mm lens, very shallow depth of field, warm lamplight "
            "from the right, blue dark behind, fine film grain. A tight framing of "
            "the first-hired man's head and shoulders in three-quarter view, his head "
            "now dropped so that his eyes are cast down toward the packed earth at "
            "the bottom edge of the frame, away from the landowner — the gaze has the "
            "ground inside the picture as its target and could not be further from "
            "the lens. His mouth is shut hard, the muscle jumping at the hinge of his "
            "jaw. At the right edge, out of focus, the landowner's dark oxblood "
            "shoulder and the edge of his iron-grey beard stand waiting, turned "
            "toward him and not moving away."
        ),
    },
    {
        "id": "v2-r023-b36", "out": "s36-everything-they-were-promised.jpeg", "seg": "n13",
        "window": "164.46-170.75", "wide": True, "jesus": False,
        "locks": ["FIRSTMAN", "CREW-DAWN", "VINEYARD"],
        "narration": "That is the whole point. The first men were not underpaid. They got everything they were promised.",
        "must_show": "The dawn crew walking home through the vineyard gate in the dark with their wages in their hands — paid in full, nothing owed to them, nothing taken away.",
        "must_not_show": "no daylight, no sunset colouring, no fighting, no coins dropped in the dust, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, one clay oil lamp behind the men at the pay "
            "table and deep blue starlit dark ahead of them, so they read as near "
            "silhouettes with warm edges of lamplight on their backs and shoulders, "
            "fine film grain. THE CAMERA STANDS INSIDE THE YARD BEHIND THE MEN AND "
            "SHOOTS OUT THROUGH THE GATE GAP AT THEIR BACKS as they walk AWAY from "
            "the lens into the dark: every man is seen from directly behind or in "
            "three-quarter from behind, receding down the track, NOT ONE FACE IS "
            "VISIBLE TO THE CAMERA AT ALL and nobody is walking toward the lens. "
            "Each of them holds his closed fist against his chest where the coin is. "
            "The first-hired man is the last through the gap, the nearest and "
            "largest back in the frame. Beyond the gate the dark terraces climb away "
            "under the first stars."
        ),
    },
    {
        "id": "v2-r023-b37", "out": "s37-grace-they-had-not-earned.jpeg", "seg": "n13",
        "window": "170.75-176.46", "wide": False, "jesus": False,
        "locks": ["FIRSTMAN", "LASTMAN", "VINEYARD"],
        "narration": "What stung was watching someone else receive grace they had not earned.",
        "must_show": "The sting itself, in one look — the first-hired man stopped in the dark and glancing back at the last-hired man still standing in the lamplight with his coin.",
        "must_not_show": "no violence, no shouting, no cartoon sneer, no daylight, no cream or off-white cloth on anyone, nobody looking into the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, one warm lamp deep in "
            "the frame and cold blue starlight on everything nearer, fine film grain. "
            "THE CAMERA IS BEHIND AND TO THE LEFT OF THE FIRST-HIRED MAN, who fills "
            "the near right of the picture as a dark shoulder and the back of his "
            "head, stopped on the path and turned back over that shoulder — only the "
            "edge of his cheekbone and one eye are visible to the lens, and that eye "
            "is aimed deep into the frame, not at the camera. What he is looking at "
            "is sharp in the distance: the last-hired man still standing alone in the "
            "small pool of lamplight by the table, his head bent over the coin in his "
            "cupped hands. The whole rest of the picture is dark yard between them."
        ),
    },
    # ============================== FRAME — Jesus closes ====
    {
        "id": "v2-r023-b38", "out": "s38-the-last-shall-be-first.jpeg", "seg": "j2",
        "window": "176.46-183.81", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LISTENERS", "TERRACE"],
        "narration": "So the last shall be first, and the first last: for many be called, but few chosen.",
        "must_show": "Jesus back on the terrace in the same bright mid-morning light, delivering the parable's closing line to the five listeners.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off Jesus; no dusk, no lamp, no night, no vineyard workers, no cream or off-white cloth on anybody but Jesus, nobody looking into the lens.",
        "scene": (
            "One photograph, 40mm lens, clear bright mid-morning sunlight from high "
            "on the left, crisp short shadows, fine film grain. THE CAMERA STANDS ON "
            "THE UPPER TERRACE BEHIND AND ABOVE TWO OF THE LISTENERS AND SHOOTS PAST "
            "THEM AND DOWN: their dark indigo and deep russet backs and headcloths "
            "fill the near left and near top of the frame, out of focus, and NOT ONE "
            "FACE IS TURNED TOWARD THE LENS. Sharp below and beyond, Jesus has risen "
            "from the dry-stone wall and stands with his weight on one foot, his head "
            "turned up and to his right toward the two standing listeners on that "
            "side, his eyes on the nearer man's face inside the frame, one hand "
            "loosely open at his side. The terraced vine rows fall away behind him "
            "into the dry valley. The other listeners are seen from the side and in "
            "three-quarter from behind, all looking at him."
        ),
    },
    {
        "id": "v2-r023-b39", "out": "s39-his-goodness-is-never-used-up.jpeg", "seg": "n14",
        "window": "183.81-190.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TERRACE"],
        "narration": "God does not run low on generosity when he spends it on someone who came late. His goodness is never used up.",
        "must_show": "Jesus's face alone, warm and unhurried, with the whole terraced vineyard behind him — the goodness the parable has been arguing about, on one face.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off him; no other person in the frame, no dusk, no lamp, no night, nobody looking into the lens.",
        "scene": (
            "One photograph, 105mm portrait lens, very shallow depth of field, clear "
            "bright mid-morning sunlight from the upper left with warm bounce coming "
            "back off the honey-coloured limestone terrace wall to fill the shadow "
            "side of his face, fine film grain. A head-and-shoulders three-quarter "
            "view of Jesus standing on the terrace. His head is turned a few degrees "
            "to his left and levelled, his eyes resting on a listener who is entirely "
            "outside the frame beyond its left edge, so his gaze leaves the picture "
            "through that edge and comes nowhere near the lens. His expression is "
            "warm, settled and unhurried. Behind him the terraced hillside of low "
            "vine rows and dry-stone walls drops away completely out of focus into "
            "green and gold."
        ),
    },
    {
        "id": "v2-r023-b40", "out": "s40-a-full-days-welcome.jpeg", "seg": "n14",
        "window": "190.53-196.52", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LISTENERS", "TERRACE"],
        "narration": "There is a full day's welcome waiting for you, no matter what hour you finally come in.",
        "must_show": "The invitation made physical — Jesus's hand held open toward the listeners, and one of them stepping in toward him across the terrace.",
        "must_not_show": "no halo, no glow, no rim-light, no light coming off him; no kneeling, no worship posture, no dusk, no lamp, no cream or off-white cloth on anybody but Jesus, nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, clear bright mid-morning sunlight from high "
            "on the left, crisp short shadows, fine film grain. THE CAMERA STANDS "
            "BEHIND THE LISTENERS AND SHOOTS PAST THEM toward Jesus: the near "
            "listener's dark umber shoulder and the back of a charcoal-brown "
            "headcloth fill the near right and near bottom of the frame, out of "
            "focus, and NOT ONE FACE IS TURNED TOWARD THE LENS. Sharp beyond them "
            "Jesus stands at the edge of the terrace with his right arm out and his "
            "hand open, palm up, held toward the listeners, his head turned and his "
            "eyes on the face of the one who has just taken a step in toward him — "
            "that man is seen in profile between the camera and Jesus, mid-step, and "
            "the two eyelines meet inside the picture. Behind Jesus the terraces of "
            "vines step away down the hillside into the bright valley."
        ),
    },
]
