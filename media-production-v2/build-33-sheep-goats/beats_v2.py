#!/usr/bin/env python3
"""V2 beat map — row 33, build-33-sheep-goats (Matthew 25:31-46). REALISTIC V2.

THE INHERITED SCAFFOLD WAS DISCARDED for measured reasons. It planned 29 pictures
at 5.8 s each and called that "the library density", against the wave's measured
3.1-4.9 s (rows 24-32). It also staged v31 as JESUS ENTHRONED ON A RAISED STONE
SEAT on an open dawn plain — a painted last-day throne scene, which the row-21,
row-30 and row-32 content-care precedent has each time refused, and which the
narration of this build never asks for.

WHAT V1 ACTUALLY DID (verified against the artefact, not the prose):
  SEVEN stills for 180.03 s, and the holds are among the worst in the wave.
    * `s1-separate.jpeg` covers n1 + j32 + n2 — 0.28 s to 32.73 s, THIRTY-TWO AND
      A HALF SECONDS on ONE picture, containing the opening red-letter verse
      (25:32) and the whole setup of the parable.
    * `s2-hungry-fed.jpeg` covers n3 + j1 — 34.09 s to 63.57 s, TWENTY-NINE AND A
      HALF SECONDS, i.e. the ENTIRE list of the six works of mercy (25:34-36),
      the longest red-letter passage in the video, held on ONE picture of ONE of
      the six mercies. That is the single biggest structural failure of V1.
    * `s4-clothed-sick.jpeg` covers j37 + n5 — 74.75 s to 107.12 s, THIRTY-TWO AND
      A HALF SECONDS, the whole bewildered question of the righteous, which the
      V1 make_narration docstring itself calls "the beat the video was missing".
    * `s7-hands-close.jpeg` covers n8 + n9 — 141.05 s to 172.07 s, THIRTY-ONE
      SECONDS, the ENTIRE closing application, the reason the video exists.
  V2 gives every one of the 13 spoken segments its own pictures, and every one of
  the six works of mercy its own frame: 45 pictures over 172.90 s = 3.85 s/picture.

AUDIO: LOCKED, never re-voiced. The V1 MP4 (180.033 s) and all fourteen mp3s share
ONE git content date (2026-07-27T22:59:51) and the summed V1 timeline is 180.03 s,
so neither staleness tripwire fires and the normal packet-copy AUDIO LOCK applies.

SOURCING TRAP CHECKED AND CLEARED: all 14 segments transcribed with faster-whisper
(small.en, word_timestamps=True) against the LIVE make_narration.py. Three apparent
differences were chased down and every one is whisper's, not the script's:
"an hungred" -> "an hungry" in j1 and "an hungred" -> "in hungry" in j37 (the
archaic word this build's own docstring already flagged as unusual — the CAPTION
prints the verbatim KJV either way), and "locked-away" -> "locked away" in n7
(hyphen tokenisation only). No TEXT_OVERRIDES.

WINDOWS: rebuilt from scratch from extract_beats plus the measured word timings.
Contiguous 0.280 -> 173.179 (the card's own start), ZERO gaps, shortest 2.30 s,
longest 5.03 s, 3.85 s/picture. j1 and j37 are split on their own clause
boundaries so that each of the six mercies — hungry, thirsty, stranger, naked,
sick, prisoner — lands on its own picture.

SCRIPTURE FACTS (Matthew 25:31-46 KJV):
  v32  "as a shepherd divideth his sheep from the goats" — the parable supplies
       its own image and this build stays inside it.
  v34-36 the six works of mercy, spoken to those on the right hand.
  v37-39 the righteous do not recognise their own kindness. This is the heart.
  v40  "Inasmuch as ye have done it unto one of the least of these my brethren,
       ye have done it unto me."
  v41-46 the word to those on the left hand is DELIBERATELY left in the narrator's
       compressed handling at n8 (the V1 make_narration docstring states this as a
       milk-before-meat decision and it is honoured here).

CONTENT CARE — THE HARDEST CALL ON THIS ROW: this is the wave's most direct
judgement passage and the temptation is to paint the last day. IT IS NOT PAINTED.
There is no throne, no crown, no sceptre, no angel, no wing, no cloud of glory, no
opening sky, no fire, no furnace and no person being punished anywhere in this
build. Jesus's red-letter lines are staged where he actually speaks them — sitting
on the Mount of Olives with his men in the last gold of one evening — and the
parable's imagery is staged as the parable's OWN imagery: a real shepherd dividing
a real flock at a real fold at dusk, and six real acts of ordinary kindness. n8's
people simply walk past a man they do not see. Care was also taken that no poor or
suffering figure reads as the crucified Christ (the row-31 lesson): Eli and the
prisoner carry no wound, scar, blood, glow or cream cloth, and each beat says so.

STAGING — nine places, none of them used elsewhere in the wave:
  * a rock-cut STAIRWAY of worn limestone steps descending the eastern flank of
    Olivet, shot along the stair looking AWAY from any settlement into the empty
    dry valley (row 31's Olivet was an open boulder shoulder in clear late
    afternoon; row 32's was a shaded olive-canopy terrace shot from behind seated
    men; this is a descending stair in the last gold of evening). NO CITY
    ANYWHERE — the Jerusalem skyline was deleted from every lock in this build
    before the first paid image, per the rows 31/32 lesson.
  * a dry-stone SHEEPFOLD with one narrow gap, at dusk (row 21's sheep were on
    open hillside pasture and in a village house; this is a built pen at last
    light and the story it tells is the DIVIDING, not the searching).
  * a NARROW ALLEY between two mud-brick houses.
  * a ROADSIDE under a lone thorn tree on the caravan track.
  * a LAMPLIT THRESHOLD at nightfall.
  * a CISTERN STEP in cold grey dawn.
  * a dim SICKROOM lit by one clay lamp.
  * a PRISON UNDERCROFT below a house (the new shared ANCIENT-PRISON lock).
  * a great stone GATEWAY where the well-dressed wait.

THE CLOCK IS THE PLOT: the frame runs through the last gold of one evening; the
fold darkens from gold to blue dusk; the six mercies run right around a whole
ordinary day — bright alley noon, hot roadside afternoon, lamplit nightfall, cold
grey dawn, lamplit sickroom, dim undercroft — and the closing beats come back to
warm ordinary daylight, because the point of the narration is that this is ANY
day, not the last one.

CAST: four anchors, each generated in its OWN run before anything else so the REFS
cache cannot make an anchor reference itself, then wired into REFS.
  b03 SHEPHERD, b27 MIRIAM, b28 TOBIAH, b40 ELI — every one of them a real placed
  picture on the timeline and a face-showing shot, so the anchors cost nothing
  extra.
"""

OUTPUT_ASSET_DIR = "assets"

# The V1 MP4 (180.033 s) and all fourteen mp3s share ONE git content date
# (2026-07-27T22:59:51). Neither staleness tripwire fires; the normal packet-copy
# AUDIO LOCK applies. Nothing is re-voiced and V1 is never written to.
AUDIO_FROM_V1_SEGMENTS = False

REF = True

# Filled in AFTER the four anchor beats are generated in their own run.
# ANCHOR ORDER: b03 (SHEPHERD), b27 (MIRIAM), b28 (TOBIAH), b40 (ELI).
REFS = {
    "SHEPHERD": "assets/ref-shepherd.jpeg",
    "MIRIAM": "assets/ref-miriam.jpeg",
    "TOBIAH": "assets/ref-tobiah.jpeg",
    "ELI": "assets/ref-eli.jpeg",
}

# ---------------------------------------------------------------- negatives ---
_NO_CREAM = ("no cream, off-white, ivory, buff, beige, taupe, sand, khaki, white "
             "or pale garment, tunic, robe, mantle, sash, wrap or head covering on "
             "anybody anywhere in the frame including the blurred edges; ")
_NO_HALO = ("no halo, no nimbus, no aura, no corona, no bright outline, edge or "
            "contour around any head, hair, shoulder or body, and no light source "
            "of any kind standing behind, above or beyond anyone's head; ")
_NO_CITY = ("no city, town, wall, gate tower, dome, minaret, bell tower, spire, "
            "tiled or pitched roof, crenellation or distant skyline of buildings "
            "anywhere in this frame; ")
_NO_JUDGEMENT = ("no throne, dais, crown, sceptre, robe of state or seat of "
                 "judgement; no angel, wing, feather or winged figure; no cloud of "
                 "glory, shaft of light from the sky, opening sky or radiance; no "
                 "fire, flame-pit, furnace, smoke of torment, chain-gang, beating, "
                 "binding or any person being punished, dragged or driven anywhere; ")
_NO_MODERN_LAMP = ("no candle, wax or taper, no glass, chimney, globe or shade, no "
                   "hurricane lamp, storm lantern, kerosene lamp or oil lantern, no "
                   "metal lamp, no hanging fixture, no ring handle, and no electric "
                   "light of any kind; ")
_NO_NIGHT = ("no night, no darkness, no stars, no lamp and no flame anywhere in "
             "this frame; ")
_GAZE = "nobody's pupils centred on the lens."

_NIGHT = ["NIGHT-LAMPLIGHT"]

LOCKS = {
    # ------------------------------------------------------------- people ----
    "JESUS-SEATED": (
        "JESUS-POSTURE NOTE: in every frame of this build Jesus is SITTING on the "
        "worn limestone steps of the stair, teaching quietly to the men around him. "
        "He never stands over anybody, never raises a hand above his own shoulder, "
        "never holds or wears any object of rank, and nothing at all is on his head."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the listeners are between five and nine ADULT MEN of the "
        "first century, aged from about twenty to about sixty, all of them Jewish "
        "labourers and fishermen with weathered sun-darkened olive-brown skin, dark "
        "hair and dark beards of differing lengths, and no two of them share a face. "
        "EVERY ONE OF THEM WEARS EXACTLY TWO SEPARATE PIECES OF CLOTH AND NOTHING "
        "ELSE: (1) one ankle-length woven wool tunic and (2) one rectangular woven "
        "head cloth or shoulder mantle — and each man's two pieces are ONE SOLID "
        "DARK SATURATED EARTH COLOUR head to foot: DEEP INDIGO, DARK UMBER, DEEP "
        "RUST, DARK OLIVE, CHARCOAL or DEEP MAROON, so every disciple in the frame "
        "is a DARK MASS from edge to edge, in focus or out of focus, near or far. "
        "NOT ONE OF THEM WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, "
        "KHAKI, WHITE OR PALE GREY CLOTH OF ANY KIND. They sit low on the steps and "
        "on the dust, listening. No woman and no child is among them."
    ),
    "SHEPHERD": (
        "SHEPHERD LOCK: the shepherd is the SAME MAN in every picture he appears "
        "in — a MALE herdsman of about forty, lean, wiry and hard-worked, with "
        "deeply sun-darkened olive-brown skin, weathered creases fanning from the "
        "outer corners of dark brown eyes, a broad flat nose, and a FULL BLACK BEARD "
        "cut square at the jaw. HIS HAIR IS THICK, BLACK AND STRAIGHT, cut to the "
        "nape and pushed back off his forehead; it is never a bare, bald, shaven or "
        "cropped head, and a band of it shows at the front edge and at the nape "
        "whenever a head cloth is on him and whenever the camera is behind him. HIS "
        "CLOTHING IS EXACTLY THREE SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) a "
        "knee-length DARK OLIVE-BROWN woven wool tunic with straight unshaped "
        "sleeves to the elbow, belted with a twisted flax cord; (2) a heavy DEEP "
        "UMBER woven wool cloak hanging from both shoulders to mid-calf; and (3) a "
        "CHARCOAL woven head cloth held by a plain twisted dark cord. He wears worn "
        "leather sandals and carries ONE rough-hewn wooden staff taller than his "
        "shoulder, cut from a single branch with the bark still on it. HE WEARS NO "
        "ANIMAL SKIN, NO FLEECE AND NO PALE CLOTH OF ANY KIND: nothing on him is "
        "cream, off-white, ivory, buff, beige, sand, khaki, white or pale grey, and "
        "he carries no bag, horn, sling or vessel. HIS CLOAK HANGS FROM HIS SHOULDERS "
        "BY ITS OWN WEIGHT ALONE and is closed by nothing: there is no brooch, pin, "
        "clasp, buckle, button, toggle, ring, hook or fastening of any kind at his "
        "throat, chest or shoulder, and no hood."
    ),
    "MIRIAM": (
        "MIRIAM LOCK: the woman is the SAME WOMAN in every picture she appears in — "
        "a FEMALE villager of about thirty-five, of ordinary height and solid "
        "working build, with warm olive-brown skin, an oval face with a firm rounded "
        "jaw, wide-set dark brown eyes under straight dark brows, one small vertical "
        "crease standing between those brows, a straight nose and a wide mouth held "
        "in quiet patience. HER HAIR IS BLACK, THICK AND STRAIGHT, parted in the "
        "centre and drawn back, and a band of it always shows along the front edge "
        "of her head cloth and at the nape of her neck; it is never a bare, bald or "
        "shaven head and it is never cut short, whichever way the camera faces her. "
        "HER CLOTHING IS EXACTLY THREE SEPARATE PIECES OF CLOTH AND NOTHING ELSE: "
        "(1) a long DEEP INDIGO woven wool tunic falling straight to the ankle with "
        "straight unshaped sleeves to the wrist; (2) a DARK RUST-BROWN woven wool "
        "mantle draped over both shoulders; and (3) a DARK OLIVE woven head cloth "
        "covering the crown of her head and falling behind her shoulders. She is "
        "barefoot or in worn leather sandals and wears no jewellery of any kind. "
        "NOTHING ON HER IS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI, "
        "WHITE OR PALE GREY."
    ),
    "ELI": (
        "ELI LOCK: the poor man is the SAME MAN in every picture he appears in — a "
        "MALE beggar of about fifty-five, gaunt and hollow-cheeked, thin through the "
        "shoulders and wrists, with dry sun-darkened olive-brown skin, deep-set dark "
        "brown eyes under heavy brows, and a THIN RAGGED BEARD OF GREY AND BLACK "
        "reaching a hand's breadth below his chin. HIS HAIR IS A BARE SUN-DARKENED "
        "CROWN WITH A THICK RING OF COARSE GREY-AND-BLACK HAIR ROUND THE SIDES AND "
        "BACK OF HIS HEAD, curling untidily over his ears and onto his neck — that "
        "grey ring is always visible, including when the camera is behind him. HIS "
        "CLOTHING IS EXACTLY TWO SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) a "
        "knee-length CHARCOAL-BROWN woven wool tunic, worn threadbare, patched at "
        "one shoulder and frayed along the hem; and (2) a torn DARK UMBER woven "
        "cloth wrapped round his hips and thrown over his left shoulder. He is "
        "BAREFOOT, his feet cracked and grey with road dust. NOTHING ON HIM IS "
        "CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI, WHITE OR PALE "
        "GREY, and he carries NO wound, scar, blood, mark or piercing of any kind on "
        "his hands, feet, side or brow. He is never comic and never grotesque — he "
        "is an ordinary tired man."
    ),
    "TOBIAH": (
        "TOBIAH LOCK: the boy is the SAME BOY in every picture he appears in — a "
        "MALE village child of about thirteen, slight and long-limbed, with smooth "
        "warm olive-brown skin, a rounded chin, large dark brown eyes with long "
        "lashes, and NO BEARD AND NO MOUSTACHE AT ALL. HIS HAIR IS THICK, BLACK AND "
        "TIGHTLY CURLED, standing out from his head and falling over his forehead "
        "and the tops of his ears; he wears NO head covering, and that mass of black "
        "curls is fully visible from every angle including from directly behind him "
        "— it is never a bare, bald, shaven or cropped head. HIS CLOTHING IS EXACTLY "
        "TWO SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) a DEEP RUST woven wool "
        "tunic reaching just below the knee, with straight unshaped sleeves to the "
        "elbow, gathered at the waist by a twisted flax cord; and (2) a DARK OLIVE "
        "woven cloth thrown over his left shoulder and knotted at his right hip. He "
        "is barefoot. NOTHING ON HIM IS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, "
        "SAND, KHAKI, WHITE OR PALE GREY."
    ),
    "CLEAR-EDGES": (
        "CLEAR-EDGES LOCK: the corners and edges of this picture are FILLED, and "
        "what fills them is stated POSITIVELY. Every one of the four corners of the "
        "frame, and the whole border all the way round it, is COMPLETELY OCCUPIED by "
        "the setting itself and by the named figures' own bodies and cloth — wall, "
        "stone, earth, dust, sky, or a continuous unbroken mass of one named figure's "
        "own garment running right off the edge of the picture. Nothing is left "
        "empty for a stranger to stand in. THERE IS NO SHOULDER, ARM, ELBOW, HAND, "
        "BACK, HEAD, "
        "HAIR, HEAD COVERING OR BODY OF ANY OTHER PERSON at any edge or in any "
        "corner of this picture, in focus or out of focus, sharp or blurred, and no "
        "pale, cream, off-white, ivory, buff, beige, grey or light-toned shape of "
        "any kind intrudes from outside the frame. Only the people the scene names "
        "are in the photograph, and nothing else crowds in past them."
    ),
    # ------------------------------------------------------------ settings ---
    "OLIVET-STAIR": (
        "OLIVET-STAIR LOCK: the place is a STAIRWAY OF WORN LIMESTONE STEPS cut and "
        "laid down the bare eastern flank of the Mount of Olives — a dozen or more "
        "shallow uneven treads of honey-grey stone, dished and rounded by "
        "generations of feet, running down the slope with dry tufted grass and loose "
        "pale stones pushing up between them and a low dry-stone retaining wall "
        "along one side. Two or three old olive trees with split silver-grey trunks "
        "stand off the stair, and beyond and below the steps the land falls away "
        "into an EMPTY DRY VALLEY of pale rock, thorn scrub and tawny grass, with "
        "bare rounded wilderness hills beyond it under an open sky. THE VIEW LOOKS "
        "AWAY FROM ANY SETTLEMENT AND THERE IS NO CITY IN IT: no wall, gate, tower, "
        "dome, minaret, bell tower, spire, tiled or pitched roof, crenellated "
        "parapet, building or distant skyline of any kind is visible anywhere in the "
        "frame, near or far, sharp or blurred. Nothing on the stair or the hillside "
        "is manufactured: no step edging, handrail, railing, post, wire, cable, sign "
        "or laid regular paving."
    ),
    "FOLD": (
        "FOLD LOCK: the place is a first-century SHEEPFOLD standing alone on open "
        "pasture — a roughly circular pen about twenty paces across, its wall built "
        "of dry-laid unmortared field stones piled to chest height with a rough "
        "uneven crest of thorn branches along the top, and ONE NARROW GAP in the "
        "wall just wide enough for one animal at a time, its two jambs worn smooth. "
        "THIS IS THE JUDEAN HILL COUNTRY OF THE NEAR EAST AT THE END OF A LONG DRY "
        "SUMMER AND THE LAND SHOWS IT: the ground inside the fold is bare trodden "
        "dust, and outside it every slope is SCORCHED STRAW-GOLD AND BARE — dead "
        "sun-bleached grass standing thin and sparse with pale limestone bedrock, "
        "chalky white stones and bare tan dust showing through it everywhere, a few "
        "grey thorn bushes, and beyond them bare rounded tan-and-grey hills with no "
        "trees on them. THERE IS NO GREEN ANYWHERE IN THIS LANDSCAPE: no green grass, "
        "no turf, no sward, no meadow, no pasture field, no bracken, no heather, no "
        "moor, no fell, no upland, no lush or damp ground, and nothing resembling "
        "northern Europe, Britain, Ireland or an alpine valley. THE ANIMALS ARE REAL "
        "NEAR-EASTERN STOCK: the sheep are fat-tailed Awassi ewes with heavy "
        "creamy-brown and dun fleeces, broad drooping ears and no horns; the goats "
        "are lean black-and-brown Levantine goats with long straight hair, "
        "swept-back horns and long hanging ears — the two kinds are instantly and "
        "obviously different animals in shape, colour and coat. Nothing here is "
        "manufactured: no wire, mesh, netting, staple, hinge, gate frame, post, "
        "plastic, painted wood, ear tag, paint mark, brand, collar, bell or tether "
        "of manufactured material anywhere on any animal or any part of the wall."
    ),
    "ALLEY": (
        "ALLEY LOCK: the place is a NARROW ALLEY about three paces wide running "
        "between two village houses of tan sun-dried mud brick, their walls "
        "hand-plastered with mud and straw, cracked, patched and streaked, with FLAT "
        "roofs of poles and packed earth and plain rectangular door openings closed "
        "by hanging dark goat-hair cloth. The ground is bare packed earth and pale "
        "dust with a shallow scraped channel down one side, a few loose stones, and "
        "a hand-woven reed basket and a fired-clay jar standing against a wall. "
        "Against the sky there is only flat roofline and bare hill. NOTHING HERE IS "
        "MANUFACTURED: no glass, no shutter, no hinge, no pipe, no gutter, no wire, "
        "no cable, no sign, no lettering, no tiled or pitched roof, no chimney, no "
        "sheet metal, no plastic and no painted surface anywhere."
    ),
    "ROADSIDE": (
        "ROADSIDE LOCK: the place is a bend of the caravan track where ONE lone "
        "flat-topped thorn tree throws a thin patch of shade over a low outcrop of "
        "pale bedrock worn smooth by travellers sitting on it. Dry tawny grass, "
        "thorn scrub and loose pale stones run away on both sides toward bare "
        "rounded hills under a hard bright sky, and the heat stands visibly in the "
        "air. A hand-woven reed basket and a fired-clay water jar with a rope-fibre "
        "carrying loop stand on the rock. There is no settlement in view and nothing "
        "manufactured anywhere in the frame."
    ),
    "THRESHOLD": (
        "THRESHOLD LOCK: the place is the doorway of a small village house of tan "
        "sun-dried mud brick — one plain rectangular opening a little taller than a "
        "man, its jambs and lintel rough hewn timber beams, its threshold a single "
        "worn limestone slab, with a heavy dark goat-hair door cloth pushed aside "
        "and hooked back on a wooden peg. Just inside, one shallow fired-clay oil "
        "lamp stands on a low stone ledge at about waist height. The packed-earth "
        "street outside is bare and empty. THERE IS NO GLASS, no window, no shutter, "
        "no hinge, no lock, no door of planks, no step edging, no lettering and "
        "nothing manufactured anywhere in the frame."
    ),
    "CISTERN": (
        "CISTERN LOCK: the place is a flight of four worn limestone steps going down "
        "to the mouth of a village cistern — a round hand-cut hole in the bedrock "
        "about two paces across, its rim rubbed smooth and dark with wet, a coil of "
        "twisted flax rope and a fired-clay jar set down on the top step. Around it "
        "the ground is bare wet rock and packed earth with pale puddles standing in "
        "the hollows, a low dry-stone wall behind, and beyond that dry scrub. "
        "Nothing here is manufactured: no windlass of machined metal, no chain, no "
        "bucket of metal or plastic, no pipe, tap, valve, grating or handrail, no "
        "laid regular paving and no lettering anywhere."
    ),
    "SICKROOM": (
        "SICKROOM LOCK: the place is the single room of a poor village house — walls "
        "of tan mud brick hand-plastered and cracked, a floor of packed earth strewn "
        "with a little dry straw, a low roof of rough poles and brushwood close "
        "overhead, and one small square unglazed opening high in the far wall. The "
        "furniture is a straw-stuffed sleeping mat laid directly on the floor with "
        "one folded DARK UMBER woven wool blanket over it, a shallow fired-clay oil "
        "lamp standing on a low stone block, and a fired-clay bowl and cup on the "
        "earth beside the mat. THERE IS NO BED FRAME, no cot, no chair, no table, no "
        "shelf, no cupboard, no glass, no shutter, no metal fixture, no hanging "
        "fixture, no textile with a printed or repeating pattern, and nothing "
        "manufactured anywhere in the frame."
    ),
    "GATEWAY": (
        "GATEWAY LOCK: the place is a great hand-built stone GATEWAY into a rich "
        "man's forecourt — two massive dressed limestone jambs and one enormous "
        "squared limestone lintel above them, the blocks chisel-dressed with visible "
        "tool marks, a broad worn threshold slab underfoot, and beyond the opening a "
        "swept packed-earth forecourt with a plain flat-roofed stone building at the "
        "far side. Against the sky there is only flat roofline and bare hill: no "
        "dome, no minaret, no bell tower, no spire, no arch of cut voussoirs, no "
        "Gothic tracery, no carved capital, no column with a moulded base, no "
        "crenellation, no tiled or pitched roof, no chimney, no half-timbering, no "
        "sheet metal, no wire and no cable. There is no gate of manufactured metal, "
        "no hinge, no lock, no railing, no lettering and no sign anywhere."
    ),
}

# ------------------------------------------------------------------ BEATS ----
BEATS = [
    # ============ n1 — the frame opens on Olivet, the flock is named ==========
    {
        "id": "v2-r033-b01", "out": "s01-near-the-end.jpeg",
        "seg": "n1", "window": "0.280-3.620", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET-STAIR", "DISCIPLES", "JESUS-SEATED", "BACKGROUND-CAST"],
        "narration": "Near the end, Jesus told his friends what the last day would really be like.",
        "must_show": "Jesus sitting on a worn limestone step of the Olivet stair with a small group of adult male disciples sitting on the steps below and around him, the empty dry valley and bare wilderness hills falling away beyond, in the last low gold light of evening.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no woman and no child; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, the last low gold light of a clear evening "
            "raking in almost level from the LEFT and throwing long soft shadows down "
            "the steps, the sun itself well out of frame, fine film grain, true depth "
            "of field. THE CAMERA STANDS LOW ON THE STAIR BEHIND AND BELOW THE SEATED "
            "DISCIPLES AND SHOOTS UP PAST THEM toward Jesus: the four nearest men are "
            "seen entirely FROM BEHIND as dark backs, shoulders and dark head cloths "
            "filling the lower third of the frame, and NOT ONE FACE IS TURNED TOWARD "
            "THE LENS. Jesus sits on a step three treads above them, a little right of "
            "centre in the middle distance, seen in three-quarter view with one "
            "forearm resting across a raised knee; his gaze travels down and to the "
            "RIGHT into the seated men and exits the picture through the RIGHT EDGE. "
            "THIS IS A WIDE FULL-LENGTH GROUP PHOTOGRAPH AND NOT A PORTRAIT: the "
            "camera is far enough back that Jesus and at least five seated men appear "
            "together head to sandals, with the worn stair, the low dry-stone wall and "
            "the empty tawny valley and bare hills beyond them. Jesus occupies only a "
            "modest part of the frame. THE ONLY PALE WOOL IN THE WHOLE PICTURE IS HIS "
            "OWN ROBE; every disciple's back, shoulder and head cloth is a solid dark "
            "saturated mass of indigo, umber, rust, olive or charcoal from edge to "
            "edge, in focus and out of focus alike."
        ),
    },
    {
        "id": "v2-r033-b02", "out": "s02-gather-all-the-nations.jpeg",
        "seg": "n1", "window": "3.620-7.080", "wide": True, "jesus": False,
        "locks": ["FOLD", "BACKGROUND-CAST"],
        "narration": "He said the King would gather all the nations in front of him",
        "must_show": "A mixed flock of fat-tailed Awassi sheep and long-haired Levantine goats streaming together across the dry pasture toward the dry-stone fold, seen from behind the flock, in deep gold light just before dusk.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no person, figure, hand, shoulder or human silhouette anywhere in the frame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, deep gold evening light coming in almost level "
            "from the LEFT so every animal casts a long shadow to the right, the sun "
            "out of frame, dust hanging in the light, fine film grain, true depth of "
            "field. THE CAMERA IS SET LOW AT KNEE HEIGHT BEHIND THE MOVING FLOCK AND "
            "SHOOTS PAST IT: the nearest animals are seen from directly behind, their "
            "backs and rumps filling the lower frame, and the whole mass of them moves "
            "AWAY FROM THE CAMERA toward the dry-stone fold in the middle distance. "
            "Sheep and goats are mixed all through the flock, obviously two different "
            "kinds of animal side by side — the sheep heavy, broad-backed, "
            "creamy-brown and dun with drooping ears, the goats lean, long-haired and "
            "black-and-brown with swept-back horns. Beyond the fold the bare rounded "
            "hills run away into gold haze. THERE IS NO PERSON IN THIS PICTURE AT ALL: "
            "the frame contains only animals, the fold wall, the pasture and the hills."
        ),
    },
    {
        "id": "v2-r033-b03", "out": "s03-two-groups.jpeg",
        "seg": "n1", "window": "7.080-10.691", "wide": False, "jesus": False,
        "locks": ["SHEPHERD", "FOLD"],
        "narration": "and separate them into two groups.",
        "must_show": "The shepherd standing square in the narrow gap of the fold wall, one hand out low to turn a goat aside while a ewe passes at his other knee, his face lit three-quarter by the last gold light.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no second person anywhere in the frame; no sheepskin, fleece or pale garment on the shepherd; no staff or rod raised above his shoulder and no animal being struck; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a wide aperture, the last gold evening light "
            "coming in level from the LEFT and lighting the front planes of his face "
            "and chest while the fold wall behind him falls into shadow, the sun out "
            "of frame, fine film grain, shallow true depth of field with the animals "
            "nearest the lens softening. THE CAMERA IS OUTSIDE THE FOLD AT CHEST "
            "HEIGHT, three paces from the gap and set to the LEFT of it, so the "
            "shepherd is seen in THREE-QUARTER VIEW from his front-left, his body "
            "turned across the frame; his head is turned down and to his own right and "
            "HIS GAZE IS FIXED ON THE HEAD OF THE GOAT AT HIS KNEE, well below and "
            "left of the camera, exiting the picture through the LOWER LEFT EDGE. He "
            "IS A MIDDLE EASTERN JEWISH HERDSMAN OF THE FIRST CENTURY, about forty, "
            "lean and wiry, his skin DEEPLY SUN-DARKENED OLIVE-BROWN — never fair, "
            "never pinkish, never European-looking. His hair is THICK, BLACK AND "
            "STRAIGHT, cut to the nape and showing at his temples and at the back of "
            "his neck, never short-cropped and never grey; his beard is FULL AND "
            "BLACK, cut square at the jaw, never grizzled and never grey. A CHARCOAL "
            "WOVEN HEAD CLOTH IS ON HIS HEAD, draped over the crown and down behind "
            "both ears and held by a plain twisted dark cord. He wears his "
            "knee-length dark olive-brown tunic and his deep umber wool cloak, which "
            "hangs from his shoulders by its own weight and is closed by NOTHING — no "
            "brooch, pin, clasp, buckle or fastening at the throat, chest or "
            "shoulder — and his hewn staff stands upright in his left hand. HE STANDS "
            "SQUARELY IN THE NARROW GAP OF THE DRY-STONE WALL, its two worn stone "
            "jambs rising close on either side of him so the wall runs out of frame "
            "left and right behind his shoulders. His right hand is out low and open, "
            "palm down, turning a long-haired black-and-brown goat aside to his "
            "right, while a heavy creamy-brown fat-tailed ewe presses past his left "
            "knee into the gap. EVERY SCRAP OF GROUND AND HILLSIDE VISIBLE PAST HIM "
            "IS SCORCHED STRAW-GOLD AND BARE — dead sun-bleached grass, chalky pale "
            "stones and tan dust over bare treeless hills — with NO green grass, "
            "turf, meadow, moor or damp upland anywhere in the picture. Mid-action, "
            "caught between two animals, unposed."
        ),
    },
    # ================ j32 — the red-letter verse on the stair ================
    {
        "id": "v2-r033-b04", "out": "s04-before-him-gathered.jpeg",
        "seg": "j32", "window": "10.691-14.171", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLEAR-EDGES", "OLIVET-STAIR", "JESUS-SEATED"],
        "narration": "And before him shall be gathered all nations:",
        "must_show": "Jesus alone in the frame, sitting on the worn limestone step in strict side-on profile, speaking, the gold evening light full on the front of his face.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no other person, shoulder, arm, head or body anywhere in the frame; no object at all in his hands; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a wide aperture, the last gold evening light "
            "coming in level from the LEFT and lighting the whole front of his face, "
            "the stair and valley behind him dropping into soft shadow and shallow "
            "blur, fine film grain. THE CAMERA IS SET FULLY SIDE-ON AT HIS OWN SEATED "
            "EYE HEIGHT, so Jesus is seen in a STRICT LEFT PROFILE: his far cheek and "
            "his far eye are completely hidden behind the near side of his own head, "
            "only the near eye is visible, and his eyeline runs perfectly HORIZONTAL "
            "across the frame and exits through the LEFT EDGE. A lens gaze is "
            "geometrically impossible in this composition. He sits on the worn step "
            "with his forearms across his knees, his lips parted mid-word, his "
            "expression open and unhurried. His hair, beard and cream wool robe are "
            "exactly as locked. The background is only worn honey-grey steps, dry "
            "grass and the tawny empty valley falling away, all of it out of focus."
        ),
    },
    {
        "id": "v2-r033-b05", "out": "s05-one-from-another.jpeg",
        "seg": "j32", "window": "14.171-18.011", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "SHEPHERD", "FOLD"],
        "narration": "and he shall separate them one from another, as a",
        "must_show": "The shepherd's two weathered male hands and forearms working low in the gap of the fold wall, one palm on a goat's shoulder pushing it left, the other guiding a ewe right, the two animals visibly parting.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no face and no head of any person in the frame; no female hand, no smooth young hand and no child's hand; no rope, tether, collar, bell, ear tag or paint mark on any animal; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm lens at a wide aperture, close in and low, the last "
            "gold evening light raking in level from the LEFT across the animals' "
            "backs, fine film grain, very shallow true depth of field. THE CAMERA IS "
            "AT KNEE HEIGHT AND SET SIDE-ON to the gap in the dry-stone wall, framing "
            "only from the shepherd's chest down: the frame holds his TWO ADULT MALE "
            "HANDS AND FOREARMS — broad, thick-knuckled, deeply sun-darkened, "
            "hard-skinned, the nails short and split, dark hair on the wrists — coming "
            "down into the picture from the top edge out of the dark olive-brown "
            "sleeves of his tunic, with the lower part of his umber cloak and one "
            "sandalled foot behind them. His LEFT hand is flat on the shoulder of a "
            "lean long-haired black-and-brown goat, pressing it away to the left; his "
            "RIGHT hand is open under the jaw of a heavy creamy-brown fat-tailed ewe, "
            "turning her to the right; the two animals are visibly moving apart and a "
            "wedge of bare dust opens between them. NO PERSON'S HEAD OR FACE IS IN "
            "THIS FRAME AT ALL. Mid-action, unposed, dust lifting off the ground."
        ),
    },
    {
        "id": "v2-r033-b06", "out": "s06-sheep-from-the-goats.jpeg",
        "seg": "j32", "window": "18.011-21.917", "wide": True, "jesus": False,
        "locks": ["SHEPHERD", "FOLD", "BACKGROUND-CAST"],
        "narration": "shepherd divideth his sheep from the goats.",
        "must_show": "A wide view of the fold at last light with the two kinds of animal now standing plainly apart — the ewes gathered inside the wall on one side, the goats bunched outside it on the other — and the shepherd small in the gap between them, seen from behind.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no second person anywhere in the frame; no bare, bald or shaven head on the shepherd; no fence, wire, mesh, gate or post of manufactured material; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, the very last gold light of the evening coming "
            "in level from the LEFT with the shadows already running long and blue "
            "across the dust, the sun out of frame, fine film grain, true depth of "
            "field. THE CAMERA STANDS BACK ON RISING GROUND BEHIND THE SHEPHERD AND "
            "SHOOTS PAST HIM: he is seen from DIRECTLY BEHIND and small in the middle "
            "distance, standing in the narrow gap of the dry-stone wall, his back and "
            "the fall of his deep umber cloak toward the lens, his charcoal head cloth "
            "on his head WITH THE THICK BLACK HAIR OF HIS NAPE SHOWING BELOW IT — it "
            "is not a bare or shaven head — and his hewn staff angled out from his "
            "right hand. NOT ONE FACE IS TURNED TOWARD THE LENS. To the LEFT of him, "
            "inside the fold wall, a score of heavy creamy-brown and dun fat-tailed "
            "ewes stand packed together; to the RIGHT of him, outside the wall on the "
            "open pasture, a separate bunch of lean black-and-brown long-haired goats "
            "stands apart with clear empty ground between the two groups. THIS IS A "
            "WIDE FULL-LENGTH LANDSCAPE PHOTOGRAPH: the whole fold, both groups of "
            "animals and the bare rounded hills beyond are all in the frame together, "
            "and the shepherd is a small figure in it."
        ),
    },
    # =========== n2 — the shepherd's evening, and the surprise ==============
    {
        "id": "v2-r033-b07", "out": "s07-shepherd-at-evening.jpeg",
        "seg": "n2", "window": "21.917-25.857", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "SHEPHERD", "FOLD"],
        "narration": "Like a shepherd at evening quietly dividing his flock, the",
        "must_show": "The shepherd moving quietly among the animals inside the fold at deep dusk, seen from the side, his hand resting on a ewe's back as she passes, his face calm and lit only by the last colour left in the sky.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + "no lamp, torch, fire or flame anywhere in the frame; no second person; no sheepskin, fleece or pale garment on the shepherd; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, deep blue dusk with the very last cold "
            "orange-pink colour lying low along the horizon to the LEFT and the sky "
            "above already dark blue, the whole scene dim and desaturated so the "
            "animals read mostly as shape and mass, fine film grain, true depth of "
            "field. THE CAMERA IS SET AT CHEST HEIGHT FULLY SIDE-ON, five paces away "
            "inside the fold, so the shepherd is seen in pure PROFILE walking slowly "
            "across the frame from RIGHT to LEFT; his head is turned down toward the "
            "backs of the animals and HIS GAZE RESTS ON THE EWE PASSING AT HIS OWN "
            "KNEE, exiting the picture through the LOWER LEFT EDGE. He is the same "
            "lean forty-year-old herdsman with the full black beard and black hair to "
            "the nape, in his dark olive-brown tunic, deep umber cloak and charcoal "
            "head cloth, staff in his left hand, his right hand laid flat and easy on "
            "a passing ewe's back. Fat-tailed ewes press round his legs to waist "
            "height and fill the lower half of the frame, and the low dark crest of "
            "the dry-stone wall runs behind him. Nothing is lit by any flame; the only "
            "light in the picture is the dying daylight in the sky."
        ),
    },
    {
        "id": "v2-r033-b08", "out": "s08-one-side-and-the-other.jpeg",
        "seg": "n2", "window": "25.857-29.937", "wide": True, "jesus": False,
        "locks": ["FOLD", "BACKGROUND-CAST"],
        "narration": "sheep to one side and the goats to the other. And what decided which",
        "must_show": "A wide view along the line of the dry-stone wall at blue dusk, the ewes settled on the near side and the goats settled on the far side, a clear band of empty trodden dust between them, and no person in the frame.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + "no person, figure, hand, shoulder or human silhouette anywhere in the frame; no lamp, torch, fire or flame; no ear tag, paint mark, collar, bell or tether on any animal; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, deep blue dusk with the last cold light lying "
            "low along the horizon behind the hills, the whole picture dim and "
            "blue-grey with colour surviving only in the animals' coats, fine film "
            "grain, true depth of field. THE CAMERA IS SET LOW, at the height of a "
            "sheep's back, LOOKING ALONG THE LINE OF THE DRY-STONE WALL so the wall "
            "runs diagonally away from the lens into the middle distance and divides "
            "the frame. On the NEAR side of the wall the heavy creamy-brown and dun "
            "fat-tailed ewes are settled together, some standing, some already folded "
            "down onto the dust; on the FAR side the lean black-and-brown long-haired "
            "goats stand apart in their own bunch with their heads up. A clear band of "
            "empty trodden dust lies between the wall and each group. THERE IS NO "
            "PERSON IN THIS PICTURE AT ALL. Beyond them the bare rounded hills are a "
            "flat dark blue shape against a slightly lighter sky."
        ),
    },
    {
        "id": "v2-r033-b09", "out": "s09-not-what-people-expect.jpeg",
        "seg": "n2", "window": "29.937-33.810", "wide": True, "jesus": False,
        "locks": ["OLIVET-STAIR", "DISCIPLES", "BACKGROUND-CAST"],
        "narration": "side you were on was not at all what people expect.",
        "must_show": "Three or four of the disciples sitting on the Olivet steps in the last gold light, listening, one leaning forward with his brow drawn in honest puzzlement, all their eyes travelling up the stair out of frame.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and no man in cream, off-white or pale cloth of any kind; no woman and no child; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, the last low gold light of evening raking in "
            "level from the LEFT and catching the sides of their faces and hands, the "
            "sun out of frame, fine film grain, true depth of field. THE CAMERA IS SET "
            "LOW ON THE STEP BESIDE THEM AND SLIGHTLY BEHIND THE NEAREST MAN AND "
            "SHOOTS ALONG THE STAIR, so the nearest disciple is seen from BEHIND HIS "
            "SHOULDER as a dark mass in the near left foreground and the others are "
            "seen in three-quarter and side view; NOT ONE FACE IS TURNED TOWARD THE "
            "LENS. Every man's eyes travel UP THE STAIR to the RIGHT toward someone "
            "out of frame, exiting the picture through the RIGHT EDGE. The second man "
            "leans forward with his forearms on his knees and his brow drawn in, "
            "genuinely puzzled and working it out; a third has stopped mid-movement "
            "with one hand half-lifted. They are adult Jewish labourers with weathered "
            "olive-brown skin and dark beards, and each of them is a solid dark mass "
            "of indigo, umber, rust, olive, charcoal or maroon wool head to foot. THIS "
            "IS A WIDE PHOTOGRAPH OF SEVERAL MEN TOGETHER, not a portrait: the worn "
            "steps, the low dry-stone wall and the tawny valley beyond are all in "
            "frame."
        ),
    },
    # ============== n3 — he turns to the ones he welcomed in ================
    {
        "id": "v2-r033-b10", "out": "s10-to-the-first-group.jpeg",
        "seg": "n3", "window": "33.810-38.755", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OLIVET-STAIR", "JESUS-SEATED"],
        "narration": "To the first group, the ones he welcomed in, the King said this.",
        "must_show": "Jesus seated on the step, turning slightly and opening one hand low and outward in welcome toward the men below him on the stair, in warm gold evening light.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no crown, throne, sceptre or robe of state on him; no hand raised above his own shoulder; no other person's face in the frame; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a wide aperture, warm gold evening light "
            "coming in level from the LEFT full onto the front of his face and his "
            "opening hand, the stair behind him falling into soft shadow, fine film "
            "grain, shallow true depth of field. THE CAMERA IS SET AT HIS OWN SEATED "
            "EYE HEIGHT AND WELL ROUND TO HIS LEFT, so he is seen in a deep "
            "THREE-QUARTER view turned away from the lens: his head is turned down and "
            "to his own left, and HIS GAZE IS FIXED ON THE DARK SHOULDER OF A SEATED "
            "MAN AT THE LOWER LEFT CORNER OF THE FRAME, exiting the picture through "
            "the LOWER LEFT EDGE. Framed from the knees up. His right hand comes "
            "forward and low, palm turning upward and open toward that man in an "
            "unhurried gesture of welcome, no higher than his own chest. His face is "
            "warm and unguarded. His hair, beard and cream wool robe are exactly as "
            "locked. Behind him only worn honey-grey steps, dry grass and the empty "
            "tawny valley, all softly out of focus. Nothing else is in his hands and "
            "nothing is on his head."
        ),
    },
    # ==== j1 — the six works of mercy, 25:34-36, ONE PICTURE FOR EACH ======
    {
        "id": "v2-r033-b11", "out": "s11-come-ye-blessed.jpeg",
        "seg": "j1", "window": "38.755-42.695", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLEAR-EDGES", "OLIVET-STAIR", "JESUS-SEATED"],
        "narration": "Come, ye blessed of my Father, inherit the kingdom prepared",
        "must_show": "Jesus alone, close, in strict side-on profile on the step, mid-word, the gold evening light full on the front of his face.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no other person, shoulder, arm or head anywhere in the frame; no crown, throne or object of rank; " + _GAZE,
        "scene": (
            "One photograph, 105mm lens at a wide aperture, the last gold evening "
            "light coming in level from the RIGHT and lighting the whole front of his "
            "face, the background dropping into soft shadow and heavy blur, fine film "
            "grain. THE CAMERA IS SET FULLY SIDE-ON AT HIS OWN SEATED EYE HEIGHT, so "
            "Jesus is seen in a STRICT RIGHT PROFILE: his far cheek and his far eye "
            "are completely hidden behind the near side of his own head, only the near "
            "eye is visible, and his eyeline runs perfectly HORIZONTAL across the "
            "frame and exits through the RIGHT EDGE. A lens gaze is geometrically "
            "impossible in this composition. Framed from the chest up. His lips are "
            "parted mid-word and his chin is lifted very slightly; the expression is "
            "quiet gladness, not proclamation. His hair, beard and cream wool robe are "
            "exactly as locked. Behind him only the blurred honey-grey stone of the "
            "stair and dry grass."
        ),
    },
    {
        "id": "v2-r033-b12", "out": "s12-foundation-of-the-world.jpeg",
        "seg": "j1", "window": "42.695-46.315", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET-STAIR", "DISCIPLES", "JESUS-SEATED", "BACKGROUND-CAST"],
        "narration": "for you from the foundation of the world. For",
        "must_show": "A wide view of the whole stair from below with Jesus seated small among the men and the enormous evening sky and empty wilderness valley open above and beyond them.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no sun disc in the frame, no shaft of light from the sky, no opening cloud and no radiance; no woman and no child; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 24mm wide lens, the last gold evening light coming in "
            "level from the LEFT, the sky above filling most of the frame in clean "
            "graded blue and pale gold with the sun itself well outside the picture, "
            "fine film grain, true depth of field. THE CAMERA IS SET DOWN THE STAIR "
            "WELL BELOW THE WHOLE GROUP AND SHOOTS UP PAST THE MEN'S BACKS: the two "
            "nearest disciples are seen from DIRECTLY BEHIND as dark silhouetted "
            "backs, shoulders and head cloths in the lower corners, and NOT ONE FACE "
            "IS TURNED TOWARD THE LENS. Jesus is small in the middle distance, sitting "
            "on his step in three-quarter view with the other men around him, and HIS "
            "GAZE TRAVELS DOWN INTO THE GROUP and exits through the LOWER RIGHT EDGE. "
            "THIS IS A WIDE FULL-LENGTH LANDSCAPE PHOTOGRAPH AND NOT A PORTRAIT: the "
            "worn stair, all the seated men head to sandals, the old olive trees, the "
            "empty tawny valley and the bare rounded hills are all in the frame "
            "together, and Jesus occupies only a small part of it. THE ONLY PALE WOOL "
            "IN THE PICTURE IS HIS OWN ROBE; every other man is a solid dark mass of "
            "indigo, umber, rust, olive or charcoal."
        ),
    },
    {
        "id": "v2-r033-b13", "out": "s13-hungred-gave-me-meat.jpeg",
        "seg": "j1", "window": "46.315-49.395", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "MIRIAM", "ELI", "ALLEY", "MARKET-TOWN", "BACKGROUND-CAST"],
        "narration": "I was an hungred, and ye gave me meat.",
        "must_show": "Miriam crouched down on her heels in the alley putting a round flat barley loaf into the two open hands of Eli, who sits back against the mud-brick wall, in bright midday light.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no coin, purse or money changing hands; no bare, bald or shaven head on the woman; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens at a wide aperture, hard bright midday sun "
            "coming almost straight down and slicing the alley into one brilliant band "
            "of light and deep blue shade, both figures inside the shade with bounced "
            "warm light off the sunlit mud-brick wall opposite, fine film grain, "
            "shallow true depth of field. THE CAMERA IS SET LOW AT THEIR OWN SEATED "
            "HEIGHT AND SIDE-ON TO BOTH OF THEM, five paces down the alley, so the two "
            "are seen from the SIDE facing each other across the frame and NEITHER "
            "FACE IS TURNED TOWARD THE LENS. On the LEFT, MIRIAM — the same "
            "thirty-five-year-old woman with the oval face, the crease between her "
            "brows and her black hair showing along the front edge of her dark olive "
            "head cloth, in her deep indigo tunic and dark rust-brown mantle — is "
            "crouched right down on her heels with her knees together, both hands "
            "forward. On the RIGHT, ELI — the same gaunt fifty-five-year-old man with "
            "the thin ragged grey-and-black beard and the ring of coarse grey hair "
            "round his bare crown, in his threadbare charcoal-brown tunic and torn "
            "dark umber hip cloth, barefoot — sits back against the mud-brick wall "
            "with both hands cupped open in his lap. A round flat barley loaf is in "
            "the air between her fingers and his palms, at the exact instant of "
            "passing. HER GAZE IS ON HIS HANDS and HIS GAZE IS ON THE LOAF, both "
            "exiting the picture through the LOWER EDGE. Mid-action, candid, unposed. "
            "No other person is in the alley."
        ),
    },
    {
        "id": "v2-r033-b14", "out": "s14-thirsty-gave-me-drink.jpeg",
        "seg": "j1", "window": "49.395-52.735", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "TOBIAH", "ROADSIDE", "ANCIENT-ROAD", "BACKGROUND-CAST"],
        "narration": "I was thirsty, and ye gave me drink.",
        "must_show": "Tobiah standing over a spent old traveller sitting on the roadside rock, tipping a fired-clay water jar so a bright thread of water falls into the old man's cupped hands, in hard afternoon light under the thorn tree.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no bare, bald or shaven head on the boy and no beard or moustache on him; no metal, glass or plastic vessel of any kind; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens at a wide aperture, hard bright afternoon sun "
            "coming in high from the RIGHT, the thin thorn shade breaking it into "
            "sharp patches across both figures, heat haze standing off the pale ground "
            "beyond, fine film grain, shallow true depth of field. THE CAMERA IS SET "
            "LOW AT THE SEATED MAN'S OWN HEIGHT AND SIDE-ON TO BOTH, so the pair is "
            "seen from the SIDE and NEITHER FACE IS TURNED TOWARD THE LENS. On the "
            "LEFT, TOBIAH — the same thirteen-year-old boy with the smooth beardless "
            "face and the thick black curls standing out from his bare head, in his "
            "deep rust knee-length tunic and dark olive shoulder cloth, barefoot — "
            "stands leaning forward from the waist, both hands round a round-bellied "
            "fired-clay water jar tipped well over. On the RIGHT sits a spent MALE "
            "traveller of about seventy, deeply sun-burnt, with a white beard, a DEEP "
            "MAROON tunic and a DARK CHARCOAL head cloth, his sandals off beside him "
            "and his two hands cupped together at his chest. A single bright unbroken "
            "thread of water falls from the jar's lip into his cupped palms and "
            "splashes. THE BOY'S GAZE IS ON THE JAR'S LIP and THE OLD MAN'S GAZE IS ON "
            "HIS OWN CUPPED HANDS, both exiting the picture through the LOWER EDGE. "
            "Mid-action, water actually in flight, unposed."
        ),
    },
    {
        "id": "v2-r033-b15", "out": "s15-stranger-took-me-in.jpeg",
        "seg": "j1", "window": "52.735-56.475", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "THRESHOLD", "MARKET-TOWN"] + _NIGHT,
        "narration": "I was a stranger, and ye took me in,",
        "must_show": "A householder standing well aside in his own lit doorway with one arm holding the goat-hair door cloth back, while a dusty foreign traveller with a bundle on his shoulder steps up over the worn threshold slab out of the night.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; " + _NO_MODERN_LAMP + "no light source standing behind or above either man's head; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, full night outside, the ONLY light in the "
            "picture the single small soft yellow flame of one shallow fired-clay oil "
            "lamp standing on a low stone ledge JUST INSIDE the doorway at waist "
            "height — LOW, IN FRONT of both men and NEARER THE CAMERA THAN EITHER HEAD "
            "— so its light climbs only up the front planes of their faces and chests "
            "while the crowns and backs of both heads stay unlit and merge into the "
            "black of the doorway and the street. Away from the flame the picture "
            "falls to near black. Fine film grain, true depth of field. THE CAMERA "
            "STANDS OUTSIDE IN THE DARK STREET, SIDE-ON TO THE THRESHOLD, so both men "
            "are seen in PROFILE facing each other across the doorway and NEITHER FACE "
            "IS TURNED TOWARD THE LENS. Inside on the RIGHT the householder — a MALE "
            "villager of about forty-five, weathered olive-brown skin, a short greying "
            "black beard, thick black hair to the nape, in a DEEP INDIGO ankle-length "
            "tunic and a DARK UMBER shoulder mantle — has stepped right back against "
            "the jamb, his left arm up holding the heavy dark goat-hair door cloth "
            "wide open. Coming in from the LEFT the traveller — a MALE stranger of "
            "about thirty, dust grey to the knees, a dark cloth bundle roped over his "
            "right shoulder, in a DEEP RUST tunic and DARK OLIVE head cloth — is "
            "caught with one bare foot already on the worn limestone threshold slab "
            "and his weight coming forward. THE HOUSEHOLDER'S GAZE IS ON THE "
            "TRAVELLER'S FACE and THE TRAVELLER'S GAZE IS ON THE LIT FLOOR INSIDE, "
            "exiting the picture through the LOWER RIGHT EDGE. Mid-step, unposed."
        ),
    },
    {
        "id": "v2-r033-b16", "out": "s16-naked-ye-clothed-me.jpeg",
        "seg": "j1", "window": "56.475-58.775", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "MIRIAM", "CISTERN", "BACKGROUND-CAST"],
        "narration": "naked, and ye clothed me.",
        "must_show": "Miriam leaning in to draw her own dark rust-brown wool mantle round the shoulders of a shivering man hunched on the cistern step in the cold grey dawn.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no nudity and no bare torso — the man keeps a torn tunic on throughout; no bare, bald or shaven head on the woman; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a wide aperture, cold flat colourless "
            "overcast dawn light coming evenly from the whole sky with no sun and no "
            "warm colour anywhere, everything blue-grey and damp, their breath just "
            "visible, fine film grain, shallow true depth of field. THE CAMERA IS SET "
            "LOW AT THE SEATED MAN'S HEIGHT AND FULLY SIDE-ON, three paces away, so "
            "both are seen in PROFILE across the frame and NEITHER FACE IS TURNED "
            "TOWARD THE LENS. On the RIGHT, hunched on the worn limestone cistern step "
            "with his knees drawn up and his arms locked across his chest, is a MALE "
            "labourer of about forty, soaked and shuddering with cold, his hair and "
            "short black beard wet and flat to his head, wearing one torn sleeveless "
            "DARK CHARCOAL tunic that covers him from shoulder to knee and nothing "
            "else — he is fully covered and there is no nudity in this picture. On the "
            "LEFT, MIRIAM — the same thirty-five-year-old woman with the oval face, "
            "the crease between her brows and her black hair showing along the front "
            "edge of her dark olive head cloth, in her deep indigo tunic — has leaned "
            "in from a half-crouch and is drawing her own DARK RUST-BROWN woven wool "
            "mantle off her shoulders and round his, her two hands closing the cloth "
            "at his back. HER GAZE IS ON HER OWN HANDS AT HIS SHOULDER and HIS GAZE IS "
            "DOWN ON THE WET STONE BETWEEN HIS FEET, both exiting the picture through "
            "the LOWER EDGE. Mid-action, the cloth still moving, unposed."
        ),
    },
    {
        "id": "v2-r033-b17", "out": "s17-sick-ye-visited-me.jpeg",
        "seg": "j1", "window": "58.775-61.415", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "SICKROOM"] + _NIGHT,
        "narration": "I was sick, and ye visited me.",
        "must_show": "A young woman kneeling on the earth floor beside a straw sleeping mat holding a fired-clay cup to the lips of an old woman lying under a dark blanket, lit only by one small clay lamp standing low on a stone block in front of them.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; " + _NO_MODERN_LAMP + "no bed frame, cot, chair, table or shelf; no light source standing behind or above either head; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens at a wide aperture, deep night, the ONLY light "
            "in the picture the single small soft yellow flame of one shallow "
            "fired-clay oil lamp standing on a low stone block on the earth floor in "
            "the NEAR FOREGROUND — LOW, IN FRONT of both women and NEARER THE CAMERA "
            "THAN EITHER HEAD — so the light climbs only up the fronts of their faces "
            "and hands and the crowns and backs of both heads stay unlit and merge "
            "into the black of the room. The far walls and the roof poles fall to near "
            "black. Fine film grain, shallow true depth of field. THE CAMERA IS SET "
            "DOWN ON THE FLOOR AT MAT HEIGHT AND SIDE-ON, so both women are seen in "
            "PROFILE across the frame and NEITHER FACE IS TURNED TOWARD THE LENS. On "
            "the LEFT, kneeling on the packed earth with her weight forward, is a "
            "FEMALE villager of about twenty-five with warm olive-brown skin and black "
            "hair drawn back under a DARK UMBER head cloth, in a DEEP MAROON "
            "ankle-length tunic; her left hand is under the old woman's head and her "
            "right holds a small fired-clay cup to her lips. On the RIGHT, lying on "
            "the straw mat under one folded DARK UMBER wool blanket drawn to her "
            "chest, is a FEMALE woman of about seventy, hollow-faced and fevered, grey "
            "hair damp at the temples, a folded damp cloth across her brow. THE "
            "YOUNGER WOMAN'S GAZE IS ON THE RIM OF THE CUP and THE OLD WOMAN'S EYES "
            "ARE HALF CLOSED AND TURNED DOWN toward it, both exiting the picture "
            "through the LOWER EDGE. Mid-action, unposed."
        ),
    },
    {
        "id": "v2-r033-b18", "out": "s18-prison-came-unto-me.jpeg",
        "seg": "j1", "window": "61.415-65.210", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "MIRIAM", "TOBIAH", "ANCIENT-PRISON"] + _NIGHT,
        "narration": "I was in prison, and ye came unto me.",
        "must_show": "Miriam crouched at the timber-barred opening of the prison undercroft passing a round barley loaf between two thick timber bars into the hands of a shackled man inside, with Tobiah kneeling beside her holding the reed basket, lit by one small clay lamp set on the stone at their feet.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no round machined steel bars, welded grid, hinged barred door, lock plate, padlock, keyhole, bunk or cell corridor; no guard, weapon, whip or person being struck; " + _NO_MODERN_LAMP + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens at a wide aperture, deep night in a stone "
            "passage, the ONLY light in the picture the single small soft yellow flame "
            "of one shallow fired-clay oil lamp standing on the stone floor in the "
            "NEAR FOREGROUND — LOW, IN FRONT of everyone and NEARER THE CAMERA THAN "
            "ANY HEAD — so the light climbs only up the fronts of their faces and "
            "hands and up the lower half of the timber bars, and every crown and every "
            "shoulder stays unlit and black. Fine film grain, shallow true depth of "
            "field. THE CAMERA IS SET LOW ON THE PASSAGE FLOOR AND WELL ROUND TO THE "
            "LEFT, SIDE-ON to the barred opening, so the two visitors are seen in "
            "THREE-QUARTER VIEW FROM BEHIND AND TO THE SIDE and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. MIRIAM — the same thirty-five-year-old woman, her black "
            "hair showing at the nape below her dark olive head cloth as well as along "
            "its front edge, in her deep indigo tunic and dark rust-brown mantle — is "
            "crouched down on her heels at the opening with her right hand pushed "
            "through the gap between two thick square-cut timber bars, a round flat "
            "barley loaf in her fingers. Beside her on the right, TOBIAH — the same "
            "thirteen-year-old boy, beardless, his thick black curls fully visible from "
            "behind, in his deep rust tunic and dark olive shoulder cloth — kneels "
            "holding a hand-woven reed basket up in both hands. Inside the dark "
            "undercroft beyond the bars, a MALE prisoner of about forty with a matted "
            "black beard and a filthy DARK CHARCOAL tunic, a hand-forged iron shackle "
            "round his left ankle, has come forward on his knees with both hands "
            "reaching out to take the loaf. HER GAZE IS ON HIS REACHING HANDS and HIS "
            "GAZE IS ON THE LOAF, both exiting the picture through the LOWER RIGHT "
            "EDGE. Mid-action, unposed."
        ),
    },
    # ================= n4 — the narrator retells the list ===================
    {
        "id": "v2-r033-b19", "out": "s19-you-fed-me.jpeg",
        "seg": "n4", "window": "65.210-69.890", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "ALLEY"],
        "narration": "You fed me when I was hungry, he said. You clothed me, you sat",
        "must_show": "An extreme close view of one weathered older male hand closing round a broken half of a barley loaf while a woman's hand withdraws from it, nothing else in frame but dust and the alley floor.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no face, head or full figure of any person in the frame; no coin, purse or money; no ring, bracelet or jewellery on either hand; no wound, scar, nail mark or blood on either hand; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens at a wide aperture, bright bounced "
            "midday light coming from the LEFT off a sunlit mud-brick wall out of "
            "frame, fine film grain, very shallow true depth of field with the "
            "background dissolving completely. THE CAMERA IS DOWN ON THE ALLEY FLOOR "
            "AT CHEST HEIGHT AND SIDE-ON, framing ONLY the hands: no head, face or "
            "full figure is in the picture at all. THE BREAD IS HELD UP IN THE AIR "
            "BETWEEN THE TWO HANDS, well clear of the ground, at the centre of the "
            "frame — a broken half of a round flat barley loaf, the crumb open and "
            "coarse — and IT NEVER TOUCHES, RESTS ON OR LIES IN THE EARTH; the ground "
            "is not in this picture at all and no hand reaches down to the floor. "
            "Coming in from the RIGHT is ONE ADULT MALE HAND of an older man — gaunt, "
            "sun-darkened olive-brown, thin-skinned over the tendons, the knuckles "
            "enlarged, the nails short and split, road dust in the creases — its "
            "fingers curling UP AND UNDER the loaf and closing round it to take its "
            "weight. Coming in from the LEFT is ONE ADULT FEMALE HAND — smaller, "
            "olive-brown, work-roughened but smooth-knuckled, no ring and no "
            "jewellery of any kind — drawing back and away with its fingers already "
            "open and clear of the bread. HER SLEEVE AT THE WRIST IS DEEP INDIGO "
            "COARSE HAND-WOVEN WOOL and shows it: a visible over-and-under grid of "
            "warp and weft threads and a plain frayed cut edge, never a knitted, "
            "ribbed, cabled or cuffed sleeve, and never pale or light-toned. Behind "
            "them only a warm blurred mud-brick wall. Mid-action, at the instant of "
            "release."
        ),
    },
    {
        "id": "v2-r033-b20", "out": "s20-when-i-was-locked-away.jpeg",
        "seg": "n4", "window": "69.890-74.465", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "ANCIENT-PRISON"] + _NIGHT,
        "narration": "with me when I was sick. You came to me when I was locked away.",
        "must_show": "An extreme close view of one male prisoner's hand gripped through the gap between two thick timber bars by a woman's hand, the hand-forged iron shackle and a little straw just visible, lit low from the front by a clay lamp.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + "no face, head or full figure of any person in the frame; no round machined steel bars, welded grid, lock plate, padlock or keyhole; " + _NO_MODERN_LAMP + "no light source behind or above the hands; no wound, scar, nail mark or blood on either hand; CAMERON GATE (open complaint at 1:10 — 'why is the prisoner's nails painted black'): BOTH hands have natural, unpainted fingernails — never black, dark, painted or polished nails; ordinary clean-enough working nails only; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens at a wide aperture, deep night, the ONLY "
            "light the single small soft yellow flame of a shallow fired-clay oil lamp "
            "standing on the stone floor in the NEAR FOREGROUND below and in front of "
            "the hands, so the light climbs up onto their fronts and everything above "
            "and behind them falls to black. Fine film grain, very shallow true depth "
            "of field. THE CAMERA IS DOWN AT FLOOR LEVEL AND SIDE-ON to the barred "
            "opening, framing ONLY the hands and the bars: no head, face or full "
            "figure is in the picture at all. Two THICK SQUARE-CUT TIMBER BARS, adzed "
            "flat and unpainted, run vertically through the frame with a hand's width "
            "of black gap between them. Through that gap ONE ADULT MALE HAND — broad, "
            "filthy, the nails black, a heavy hand-forged iron shackle showing at the "
            "wrist above it, dark grey, uneven and pitted — reaches out and is being "
            "GRIPPED at the wrist and fingers by ONE ADULT FEMALE HAND, smaller, "
            "olive-brown, work-roughened, no ring and no jewellery, and A DEEP INDIGO "
            "SLEEVE OF COARSE HAND-WOVEN WOOL at its wrist, showing a visible "
            "over-and-under grid of warp and weft threads on a flat matte surface "
            "with a plain frayed cut edge — it is NOT knitted: no knit stitch, no "
            "purl, no rib, no cable, no jersey, no stretchy cuff or collar band and "
            "no sweater, jumper or sweatshirt texture anywhere on it. A little dry "
            "straw lies on the stone "
            "below. Both hands are still and held tight. Nothing else is in the "
            "picture."
        ),
    },
    # ===== j37 — the righteous never saw it, 25:37-39: one per question =====
    {
        "id": "v2-r033-b21", "out": "s21-when-saw-we-thee-hungred.jpeg",
        "seg": "j37", "window": "74.465-79.165", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "MIRIAM", "ALLEY", "BACKGROUND-CAST"],
        "narration": "Lord, when saw we thee an hungred, and fed thee,",
        "must_show": "Miriam standing back up in the empty alley with her hands hanging open and empty at her sides, looking down at the patch of bare dust where the man had been sitting, her brow drawn in honest puzzlement.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no second person in the alley; no bare, bald or shaven head on her; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a wide aperture, bright midday light "
            "bouncing warm off the sunlit mud-brick wall on the LEFT into the shaded "
            "alley, fine film grain, shallow true depth of field. THE CAMERA IS SET AT "
            "HER OWN STANDING EYE HEIGHT AND WELL ROUND TO HER LEFT SIDE, four paces "
            "away, so she is seen in a deep THREE-QUARTER view turned away from the "
            "lens; her head is bowed and turned down to her own right and HER GAZE IS "
            "FIXED ON THE EMPTY PATCH OF BARE DUST AT THE FOOT OF THE WALL, exiting "
            "the picture through the LOWER RIGHT EDGE. Framed from the knees up. She "
            "is MIRIAM, the same thirty-five-year-old woman with the oval face, the "
            "small vertical crease standing between her brows and her black hair "
            "showing along the front edge of her dark olive head cloth, in her deep "
            "indigo tunic and dark rust-brown mantle. Both her hands hang open and "
            "empty at her sides, one still half-curled from where the loaf was. Her "
            "expression is honest unremarkable puzzlement — she is trying to remember "
            "something and cannot. The alley behind her is empty; NO OTHER PERSON IS "
            "IN THE FRAME."
        ),
    },
    {
        "id": "v2-r033-b22", "out": "s22-or-thirsty.jpeg",
        "seg": "j37", "window": "79.165-81.825", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "TOBIAH", "ROADSIDE", "ANCIENT-ROAD", "BACKGROUND-CAST"],
        "narration": "or thirsty and gave thee drink?",
        "must_show": "Tobiah standing alone under the thorn tree with the empty clay jar hanging from one hand at his hip, looking off down the empty caravan track, in hot late afternoon light.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no second person on the road; no bare, bald or shaven head and no beard or moustache on the boy; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a wide aperture, hot low late-afternoon sun "
            "coming in from the RIGHT and lighting the front of his face and chest, "
            "the sun out of frame, heat haze standing over the pale track behind him, "
            "fine film grain, shallow true depth of field. THE CAMERA IS SET AT HIS "
            "OWN EYE HEIGHT AND WELL ROUND TO HIS RIGHT SIDE, so he is seen in a deep "
            "THREE-QUARTER view turned away from the lens; his head is turned away to "
            "his own left and HIS GAZE FOLLOWS THE EMPTY TRACK OFF INTO THE DISTANCE, "
            "exiting the picture through the LEFT EDGE. Framed from the thighs up. He "
            "is TOBIAH, the same thirteen-year-old boy with the smooth beardless face "
            "and the thick black curls standing out from his bare head and falling "
            "over his forehead, in his deep rust knee-length tunic and dark olive "
            "shoulder cloth. The empty round-bellied fired-clay water jar hangs from "
            "his right hand by its rope-fibre loop at his hip, tilted and clearly "
            "weightless. His mouth is slightly open and his brow lifted — he is "
            "puzzling over something small. The lone flat-topped thorn tree is above "
            "and behind him and the caravan track runs away empty; NO OTHER PERSON IS "
            "IN THE FRAME."
        ),
    },
    {
        "id": "v2-r033-b23", "out": "s23-when-saw-we-thee-a-stranger.jpeg",
        "seg": "j37", "window": "81.825-85.405", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "THRESHOLD", "MARKET-TOWN", "BACKGROUND-CAST"],
        "narration": "When saw we thee a stranger and took thee in,",
        "must_show": "The householder standing alone in his own doorway in the first flat grey light of morning, one shoulder against the timber jamb, looking out along the empty packed-earth street.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no lamp, flame, candle or lantern alight anywhere; no second person in the street; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens at a wide aperture, flat colourless overcast "
            "first light of morning with no sun and no warm colour anywhere, "
            "everything blue-grey and even, the clay lamp on the inside ledge now COLD "
            "AND UNLIT with a black wick, fine film grain, shallow true depth of "
            "field. THE CAMERA IS OUT IN THE STREET AT HIS OWN EYE HEIGHT AND WELL "
            "ROUND TO HIS LEFT, so he is seen in a deep THREE-QUARTER view turned away "
            "from the lens; his head is turned away to his own right and HIS GAZE "
            "TRAVELS OFF DOWN THE EMPTY PACKED-EARTH STREET, exiting the picture "
            "through the RIGHT EDGE. Framed from the waist up. He is the same MALE "
            "villager of about forty-five with weathered olive-brown skin, a short "
            "greying black beard and thick black hair to the nape, in his DEEP INDIGO "
            "ankle-length tunic and DARK UMBER shoulder mantle, one shoulder leaned "
            "against the rough hewn timber jamb and one hand flat on the other jamb. "
            "The heavy dark goat-hair door cloth hangs slack behind him. His "
            "expression is mildly bemused, working at a memory. The street is empty; "
            "NO OTHER PERSON IS IN THE FRAME."
        ),
    },
    {
        "id": "v2-r033-b24", "out": "s24-or-naked-and-clothed-thee.jpeg",
        "seg": "j37", "window": "85.405-87.765", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "MIRIAM", "CISTERN"],
        "narration": "or naked and clothed thee?",
        "must_show": "A close view of Miriam's two hands at the cistern step folding her dark rust-brown wool mantle back over her forearm, her face above them tilted down and slightly frowning.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no second person; no bare, bald or shaven head on her; no ring, bracelet or jewellery; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 105mm lens at a wide aperture, cold flat colourless "
            "overcast dawn light from the whole sky with no sun and no warm colour, "
            "fine film grain, very shallow true depth of field with the wet stone "
            "behind dissolving. THE CAMERA IS SET SLIGHTLY BELOW HER HANDS AND FULLY "
            "SIDE-ON, so MIRIAM is seen in a near-PROFILE from her left: her far cheek "
            "and far eye are largely hidden behind the near side of her own head, her "
            "chin is dropped, and HER GAZE IS FIXED ON HER OWN HANDS at the bottom of "
            "the frame, exiting the picture through the LOWER EDGE. Framed from the "
            "chest up, so her two ADULT FEMALE HANDS and her face are both in the "
            "picture. She is the same thirty-five-year-old woman with the oval face, "
            "the crease between her brows and her black hair showing along the front "
            "edge of her dark olive head cloth, in her deep indigo tunic. Her two "
            "hands — olive-brown, work-roughened, no ring and no jewellery — are "
            "folding the DARK RUST-BROWN woven wool mantle back over her own left "
            "forearm, the woven warp and weft of it clearly visible. Her brow is "
            "faintly drawn. NO OTHER PERSON IS IN THE FRAME."
        ),
    },
    {
        "id": "v2-r033-b25", "out": "s25-sick-or-in-prison.jpeg",
        "seg": "j37", "window": "87.765-92.796", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "MIRIAM", "ANCIENT-PRISON"],
        "narration": "Or when saw we thee sick or in prison and came unto thee?",
        "must_show": "Miriam climbing the worn stone stair up out of the prison undercroft toward the daylight opening above, seen from below and behind, the empty reed basket on her hip.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no round machined steel bars, welded grid, lock plate, padlock, keyhole or cell corridor; no guard, weapon or person being struck; no bare, bald, shaven or short-cropped head on her; no bright rim, outline or halo around her head or shoulders; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, cool flat daylight falling straight down the "
            "stair shaft from an open rectangle at the top out of frame, so the light "
            "lies on the treads and on the front of her body while the undercroft "
            "below stays dim; that opening is well ahead of her and above the frame, "
            "never behind her head, and there is no bright outline anywhere on her. "
            "Fine film grain, true depth of field. THE CAMERA IS SET DOWN AT THE "
            "BOTTOM OF THE STAIR BEHIND AND BELOW HER AND SHOOTS UP PAST HER: MIRIAM "
            "is seen from THREE-QUARTER BEHIND, her back, her right shoulder and the "
            "fall of her mantle toward the lens, and NO FACE IS TURNED TOWARD THE "
            "LENS. HER DARK OLIVE HEAD CLOTH IS ON HER HEAD WITH A BAND OF HER THICK "
            "BLACK HAIR SHOWING AT THE NAPE BELOW IT — it is not a bare, bald, shaven "
            "or cropped head — and her deep indigo tunic and dark rust-brown mantle "
            "are exactly as locked. She is halfway up the worn hand-cut limestone "
            "treads with one bare foot raised to the next, an empty hand-woven reed "
            "basket on her right hip, her left hand flat on the damp chiselled stone "
            "wall. Mid-step, unposed. NO OTHER PERSON IS IN THE FRAME."
        ),
    },
    # =============== n5 — the good people are confused ======================
    {
        "id": "v2-r033-b26", "out": "s26-the-good-people-confused.jpeg",
        "seg": "n5", "window": "92.796-96.996", "wide": True, "jesus": False,
        "locks": ["MIRIAM", "TOBIAH", "ALLEY", "MARKET-TOWN", "BACKGROUND-CAST"],
        "narration": "And here is the beautiful part. The good people are confused.",
        "must_show": "Miriam, Tobiah and three other ordinary villagers standing together at the mouth of the alley in warm late light, glancing at one another with open puzzled faces, none of them certain what is being asked.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no crowd of more than five people; no bare, bald or shaven head on the woman or the boy; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon light coming in from "
            "the RIGHT and raking across their faces and the mud-brick wall behind, "
            "the sun out of frame, fine film grain, true depth of field. THE CAMERA IS "
            "SET AT CHEST HEIGHT BEHIND AND TO THE LEFT OF THE NEAREST VILLAGER AND "
            "SHOOTS PAST HIM: that man is seen entirely FROM BEHIND as a solid DARK "
            "CHARCOAL back and shoulder filling the near left foreground, and NOT ONE "
            "FACE IS TURNED TOWARD THE LENS. Facing him across a small ragged "
            "half-circle are FOUR people, each turned toward one another and not "
            "toward the camera: MIRIAM in the centre, the same thirty-five-year-old "
            "woman with the oval face and her black hair showing along the front edge "
            "of her dark olive head cloth, in her deep indigo tunic and dark "
            "rust-brown mantle, her palms turned faintly upward at her waist; TOBIAH "
            "beside her, the same beardless thirteen-year-old with thick black curls "
            "on his bare head, in his deep rust tunic and dark olive shoulder cloth, "
            "looking up at her face; and two other adult villagers, one man in DEEP "
            "MAROON and one woman in DARK UMBER, each a solid dark mass head to foot. "
            "Every gaze in the frame lands on another person INSIDE the picture. THIS "
            "IS A WIDE FULL-LENGTH GROUP PHOTOGRAPH: all five are visible from head to "
            "feet, with the alley mouth, the mud-brick walls and the flat roofline "
            "behind them. Their expressions are mild, open, ordinary bewilderment — "
            "nobody is alarmed and nobody is celebrating."
        ),
    },
    {
        "id": "v2-r033-b27", "out": "s27-when-did-we-ever-see-you.jpeg",
        "seg": "n5", "window": "96.996-100.616", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "MIRIAM", "ALLEY"],
        "narration": "They say, Lord, when did we ever see you hungry or thirsty or sick",
        "must_show": "A close three-quarter view of Miriam's face mid-question, brows drawn together, mouth open on a word, warm late light on the front of her face.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no second person, shoulder, arm or head in the frame; no bare, bald or shaven head; no jewellery; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 105mm lens at a wide aperture, warm low late-afternoon "
            "light coming in from the LEFT and lighting the whole front of her face, "
            "the sun out of frame, the mud-brick wall behind dissolving into soft warm "
            "blur, fine film grain, very shallow true depth of field. THE CAMERA IS "
            "CLOSE IN AND SET AT HER OWN EYE HEIGHT AND WELL ROUND TO HER LEFT, WITH "
            "HER BACK ALMOST AGAINST THE MUD-BRICK WALL so there is no space behind "
            "or beside her for anybody to stand: she is seen in a deep THREE-QUARTER "
            "view turned away from the lens, her head is turned up "
            "and away to her own right and HER GAZE TRAVELS PAST THE CAMERA AND OUT "
            "THROUGH THE UPPER RIGHT EDGE of the picture, clearly aimed above and "
            "beyond the lens and never centred on it. THIS IS A TIGHT "
            "HEAD-AND-SHOULDERS CROP AND HER OWN BODY AND CLOTH FILL THE WHOLE LOWER "
            "FRAME: her head fills the upper middle of the picture, the blurred "
            "mud-brick wall fills both upper corners completely, and her own DARK "
            "RUST-BROWN woven wool mantle and DEEP INDIGO tunic run as ONE CONTINUOUS "
            "UNBROKEN MASS OF CLOTH across the entire bottom third of the frame, "
            "corner to corner, passing straight off both the LEFT and the RIGHT edge "
            "so that no gap of any kind is left at either bottom corner. "
            "She is MIRIAM, the same thirty-five-year-old woman: warm olive-brown "
            "skin, an oval face with a firm rounded jaw, wide-set dark brown eyes "
            "under straight dark brows, one small vertical crease standing between "
            "them, a straight nose and a wide mouth, her black hair parted centre with "
            "a band of it showing along the front edge of her DARK OLIVE woven head "
            "cloth, her DEEP INDIGO tunic and DARK RUST-BROWN mantle at her shoulders. "
            "Her brows are drawn together and her lips parted mid-word; the expression "
            "is sincere, searching, entirely without complaint. NO OTHER PERSON IS IN "
            "THE FRAME."
        ),
    },
    {
        "id": "v2-r033-b28", "out": "s28-do-not-even-remember.jpeg",
        "seg": "n5", "window": "100.616-104.036", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "TOBIAH", "ALLEY"],
        "narration": "or in prison? They do not even remember doing anything",
        "must_show": "Tobiah standing in the alley with both hands turned open and empty at his waist and his shoulders lifted in a small honest shrug, his face tilted up and off to the side.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no second person; no bare, bald or shaven head and no beard or moustache on the boy; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a wide aperture, warm low late-afternoon "
            "light coming in from the LEFT and lighting the front of his face and his "
            "open palms, the sun out of frame, the mud-brick alley wall behind him "
            "dissolving into warm blur, fine film grain, shallow true depth of field. "
            "THE CAMERA IS SET SLIGHTLY ABOVE HIS OWN EYE HEIGHT AND ROUND TO HIS "
            "LEFT, so he is seen in a THREE-QUARTER view turned away from the lens: "
            "his head is tilted up and away to his own right and HIS GAZE TRAVELS OUT "
            "THROUGH THE UPPER RIGHT EDGE of the picture, clearly past the camera and "
            "never centred on it. Framed from the hips up. He is TOBIAH, the same "
            "thirteen-year-old boy: slight and long-limbed, smooth warm olive-brown "
            "skin, a rounded chin, large dark brown eyes with long lashes, NO BEARD "
            "AND NO MOUSTACHE, and thick black tightly curled hair standing out from "
            "his bare uncovered head and falling over his forehead and the tops of his "
            "ears. He wears his DEEP RUST knee-length tunic corded at the waist and "
            "his DARK OLIVE shoulder cloth. Both his hands are turned palm-up and "
            "empty out at his waist and his shoulders are lifted in a small honest "
            "shrug; his eyebrows are up and his mouth is slightly open. NO OTHER "
            "PERSON IS IN THE FRAME."
        ),
    },
    {
        "id": "v2-r033-b29", "out": "s29-whoever-was-in-front-of-them.jpeg",
        "seg": "n5", "window": "104.036-108.190", "wide": True, "jesus": False,
        "locks": ["MIRIAM", "ALLEY", "MARKET-TOWN", "BACKGROUND-CAST"],
        "narration": "special. They just helped whoever was in front of them.",
        "must_show": "An ordinary unremarkable moment in the alley: Miriam handing a fired-clay bowl across to a neighbour woman in a doorway while a laden donkey passes, nobody making anything of it, in warm late light.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no more than three people besides Miriam; no bare, bald or shaven head on her; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon light slanting in from "
            "the RIGHT down the length of the alley and throwing long shadows on the "
            "packed earth, the sun out of frame, fine film grain, true depth of field. "
            "THE CAMERA STANDS BACK DOWN THE ALLEY AT CHEST HEIGHT BEHIND A LADEN "
            "DONKEY AND SHOOTS PAST IT: the donkey's dark rump and the hand-woven reed "
            "panniers roped on it fill the near right foreground and the animal is "
            "moving AWAY FROM THE CAMERA, and NOT ONE FACE IN THE PICTURE IS TURNED "
            "TOWARD THE LENS. In the middle distance on the LEFT, MIRIAM — the same "
            "thirty-five-year-old woman with her black hair showing along the front "
            "edge of her dark olive head cloth, in her deep indigo tunic and dark "
            "rust-brown mantle — is seen from three-quarter behind, half-turned, "
            "holding a fired-clay bowl out at arm's length toward a neighbour. The "
            "neighbour, a FEMALE villager of about fifty in a solid DEEP MAROON tunic "
            "and DARK UMBER head cloth, stands in her own doorway in profile with one "
            "hand already under the bowl. BOTH WOMEN'S GAZES ARE ON THE BOWL BETWEEN "
            "THEM, exiting the picture through the LOWER LEFT EDGE. Beyond them ONE "
            "further villager walks away up the alley, a solid dark charcoal mass seen "
            "from behind. THIS IS A WIDE FULL-LENGTH STREET PHOTOGRAPH: the alley "
            "floor, both mud-brick walls, the flat roofline and all the figures head "
            "to feet are in the frame. Nothing in this picture looks like an event."
        ),
    },
    # ================ n6 — kindness was simply their reflex =================
    {
        "id": "v2-r033-b30", "out": "s30-not-keeping-score.jpeg",
        "seg": "n6", "window": "108.190-111.770", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "ALLEY"],
        "narration": "They were not keeping score. They were not trying to earn",
        "must_show": "A close view of two adult female hands rinsing a fired-clay bowl in a shallow basin of water on the alley doorstep, entirely absorbed in ordinary work, with no face in the frame.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no face or head of any person in the frame; no coin, purse, money, tally, scratch mark, written list, scroll or record of any kind; no ring, bracelet or jewellery; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm lens at a wide aperture, warm low late-afternoon "
            "light coming in from the RIGHT across the doorstep, fine film grain, very "
            "shallow true depth of field with everything beyond the basin dissolving. "
            "THE CAMERA IS DOWN AT DOORSTEP HEIGHT AND SLIGHTLY TO THE SIDE, framing "
            "ONLY from the forearms down: no face and no head is in the picture at "
            "all. TWO ADULT FEMALE HANDS — olive-brown, work-roughened but "
            "smooth-knuckled, short clean nails, no ring and no jewellery of any kind, "
            "the cuffs of a DEEP INDIGO woven wool sleeve pushed up at both wrists — "
            "are turning a round fired-clay bowl under the surface of a shallow "
            "fired-clay basin of grey water, water running off the rim and dripping "
            "back. A worn limestone doorstep, wet in patches, and a little spill of "
            "water darkening the packed earth are the only other things in frame."
            "HER SLEEVE IS COARSE HAND-WOVEN WOOL AND SHOWS IT: a visible over-and-under grid of warp and weft threads on a flat matte surface with a plain frayed cut edge, never a knitted, ribbed, cabled or cuffed sleeve. "
            "Mid-action, water actually moving, unposed. There is nothing written, "
            "counted or recorded anywhere in this picture."
        ),
    },
    {
        "id": "v2-r033-b31", "out": "s31-kindness-was-their-reflex.jpeg",
        "seg": "n6", "window": "111.770-115.870", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "TOBIAH", "ALLEY", "BACKGROUND-CAST"],
        "narration": "anything. Kindness was simply their reflex. And then the",
        "must_show": "Tobiah putting out one hand to steady an old man's elbow on the uneven alley step without breaking stride or even looking round, the reed basket still on his other hip.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no bare, bald or shaven head and no beard on the boy; no third person; no fall, injury or distress; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens at a wide aperture, warm low late-afternoon "
            "light slanting in from the RIGHT, the sun out of frame, fine film grain, "
            "shallow true depth of field. THE CAMERA IS SET AT CHEST HEIGHT AND FULLY "
            "SIDE-ON, four paces off, so both figures are seen in PROFILE crossing the "
            "frame and NEITHER FACE IS TURNED TOWARD THE LENS. TOBIAH — the same "
            "beardless thirteen-year-old with thick black curls on his bare head, in "
            "his deep rust knee-length tunic and dark olive shoulder cloth, barefoot — "
            "is walking briskly LEFT TO RIGHT with a hand-woven reed basket on his "
            "left hip, already half past the old man, his right arm swung back and his "
            "open right hand cupped under the old man's elbow to steady him. The old "
            "man, MALE, about seventy-five, stooped, white-bearded, in a solid DARK "
            "UMBER ankle-length tunic and CHARCOAL head cloth, is stepping down off an "
            "uneven worn stone step with a hewn stick in his other hand. THE BOY'S "
            "GAZE IS STILL AHEAD DOWN THE ALLEY and exits through the RIGHT EDGE; THE "
            "OLD MAN'S GAZE IS DOWN AT THE STEP UNDER HIS OWN FOOT and exits through "
            "the LOWER EDGE. Neither looks at the other. Mid-stride, unposed, "
            "completely unremarked."
        ),
    },
    {
        "id": "v2-r033-b32", "out": "s32-the-secret-behind-it.jpeg",
        "seg": "n6", "window": "115.870-119.586", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET-STAIR", "DISCIPLES", "JESUS-SEATED", "BACKGROUND-CAST"],
        "narration": "King tells them the secret behind all of it.",
        "must_show": "Jesus on the step leaning forward toward the men with his forearms on his knees, the whole group gone very still around him, in the last deep gold of evening.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no crown, throne, sceptre or robe of state; no woman and no child; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, the last deep gold light of evening raking in "
            "almost level from the LEFT with the shadows already long and blue, the "
            "sun out of frame, fine film grain, true depth of field. THE CAMERA IS SET "
            "LOW ON THE STAIR BEHIND THE SEATED DISCIPLES AND SHOOTS UP PAST THEM: the "
            "three nearest men are seen entirely FROM BEHIND as solid dark backs, "
            "shoulders and dark head cloths across the lower third of the frame, and "
            "NOT ONE FACE IS TURNED TOWARD THE LENS. Jesus sits on his step in the "
            "middle distance, left of centre, seen in three-quarter view, LEANING "
            "FORWARD with both forearms across his knees and his hands loose between "
            "them; HIS GAZE GOES DOWN INTO THE NEAREST MAN'S FACE and exits the "
            "picture through the LOWER RIGHT EDGE. Every man has gone still. THIS IS A "
            "WIDE FULL-LENGTH GROUP PHOTOGRAPH AND NOT A PORTRAIT: Jesus and at least "
            "five seated men are visible together head to sandals with the worn stair, "
            "the dry-stone wall and the empty tawny valley beyond. THE ONLY PALE WOOL "
            "IN THE PICTURE IS HIS OWN ROBE; every disciple is a solid dark mass of "
            "indigo, umber, rust, olive or charcoal, in focus and out of focus alike."
        ),
    },
    # ============ j2 — 25:40, the sentence the video is built on ===========
    {
        "id": "v2-r033-b33", "out": "s33-inasmuch-as-ye-have-done-it.jpeg",
        "seg": "j2", "window": "119.586-124.366", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLEAR-EDGES", "OLIVET-STAIR", "JESUS-SEATED"],
        "narration": "Verily I say unto you, Inasmuch as ye have done it unto one of the",
        "must_show": "Jesus close and alone in strict side-on profile on the step, speaking quietly and deliberately, the last gold light on the front of his face.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no other person, shoulder, arm or head anywhere in the frame; no crown, throne, sceptre or object of rank; " + _GAZE,
        "scene": (
            "One photograph, 105mm lens at a wide aperture, the last deep gold light "
            "of evening coming in level from the LEFT and lighting the whole front of "
            "his face, the stair behind him almost gone into shadow and heavy blur, "
            "fine film grain. THE CAMERA IS SET FULLY SIDE-ON AT HIS OWN SEATED EYE "
            "HEIGHT, so Jesus is seen in a STRICT LEFT PROFILE: his far cheek and his "
            "far eye are completely hidden behind the near side of his own head, only "
            "the near eye is visible, and his eyeline runs perfectly HORIZONTAL across "
            "the frame and exits through the LEFT EDGE. A lens gaze is geometrically "
            "impossible in this composition. Framed from the chest up. His head is "
            "slightly lowered and his lips are parted mid-word; the delivery is quiet "
            "and deliberate, not loud. His hair, beard and cream wool robe are exactly "
            "as locked. Behind him only blurred honey-grey stone and dry grass going "
            "dark."
        ),
    },
    {
        "id": "v2-r033-b34", "out": "s34-ye-have-done-it-unto-me.jpeg",
        "seg": "j2", "window": "124.366-129.323", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLEAR-EDGES", "OLIVET-STAIR", "JESUS-SEATED"],
        "narration": "least of these, my brethren, ye have done it unto me.",
        "must_show": "Jesus seated on the step laying his own open right hand flat against his own chest as he finishes the sentence, his head turned down toward the men below him.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no crown, throne, sceptre or robe of state; no wound, scar, nail mark or blood on his hands or body; no other person's face in the frame; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a wide aperture, the last deep gold light of "
            "evening coming in level from the LEFT full onto the front of his face and "
            "his hand, the stair behind him dropping into shadow and soft blur, fine "
            "film grain, shallow true depth of field. THE CAMERA IS SET AT HIS OWN "
            "SEATED EYE HEIGHT AND WELL ROUND TO HIS RIGHT, so he is seen in a deep "
            "THREE-QUARTER view turned away from the lens: his head is turned down and "
            "to his own left and HIS GAZE GOES DOWN ONTO THE DARK SHOULDER AND HEAD "
            "CLOTH OF A SEATED MAN AT THE LOWER LEFT CORNER OF THE FRAME, exiting the "
            "picture through the LOWER LEFT EDGE. Framed from the waist up. His right "
            "hand is laid flat and open against the centre of his own chest, the "
            "fingers spread and relaxed, unhurried; his left forearm rests across his "
            "knee. There is no wound, scar or mark of any kind on the hand. His "
            "expression is grave and tender at once. His hair, beard and cream wool "
            "robe are exactly as locked. Only the blurred dark shoulder of the seated "
            "man intrudes at the very corner of the frame; no other face is visible."
        ),
    },
    # ============ n7 — he was in them the whole time ========================
    {
        "id": "v2-r033-b35", "out": "s35-every-hungry-person.jpeg",
        "seg": "n7", "window": "129.323-133.143", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "ELI", "ALLEY"],
        "narration": "He was in them the whole time. Every hungry person,",
        "must_show": "A close three-quarter view of Eli's face in the shaded alley, quiet and tired, his gaze travelling off along the foot of the wall, the bread already gone.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no second person; nothing to suggest this man is Christ — no halo, no glow, no bright outline, no wound, no scar, no blood and no crown of thorns; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 105mm lens at a wide aperture, soft warm light bounced "
            "into the shaded alley off a sunlit mud-brick wall on the RIGHT, no direct "
            "sun on him at all, the wall behind him dissolving into warm blur, fine "
            "film grain, very shallow true depth of field. THE CAMERA IS SET AT HIS "
            "OWN SEATED EYE HEIGHT AND WELL ROUND TO HIS RIGHT, so he is seen in a "
            "deep THREE-QUARTER view turned away from the lens: his head is turned "
            "away to his own left and HIS GAZE TRAVELS ALONG THE FOOT OF THE ALLEY "
            "WALL and exits the picture through the LEFT EDGE, never centred on the "
            "lens. Framed from the shoulders up. He is ELI, the same gaunt "
            "fifty-five-year-old man: hollow cheeks, dry sun-darkened olive-brown "
            "skin, deep-set dark brown eyes under heavy brows, a thin ragged beard of "
            "grey and black a hand's breadth below his chin, and a bare sun-darkened "
            "crown with a thick ring of coarse grey-and-black hair round the sides and "
            "back of his head curling over his ears. His threadbare CHARCOAL-BROWN "
            "tunic, patched at the shoulder, and the torn DARK UMBER cloth over his "
            "left shoulder are at the bottom of the frame. His expression is quiet and "
            "tired and entirely ordinary. NOTHING IN THIS PICTURE MARKS HIM OUT AS "
            "ANYTHING BUT A POOR MAN. No other person is in the frame."
        ),
    },
    {
        "id": "v2-r033-b36", "out": "s36-every-stranger.jpeg",
        "seg": "n7", "window": "133.143-137.203", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "THRESHOLD", "MARKET-TOWN"] + _NIGHT,
        "narration": "every stranger, every sick and forgotten and locked away person",
        "must_show": "The dusty traveller stopped just inside the lit doorway and half turning back over his shoulder toward the dark street, his bundle still roped on, lit low from the front by the clay lamp.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; " + _NO_MODERN_LAMP + "no light source behind or above his head and no bright rim or outline on his hair or shoulders; no second person's face; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a wide aperture, deep night outside, the "
            "ONLY light the single small soft yellow flame of one shallow fired-clay "
            "oil lamp standing on the low stone ledge at waist height in the NEAR "
            "FOREGROUND, LOW, IN FRONT of him and NEARER THE CAMERA THAN HIS HEAD, so "
            "the light climbs only up the front planes of his face, throat and chest "
            "while the crown and back of his head, his shoulders and the whole doorway "
            "behind fall to unlit black. Fine film grain, very shallow true depth of "
            "field. THE CAMERA IS INSIDE THE HOUSE AT HIS OWN EYE HEIGHT AND WELL "
            "ROUND TO HIS LEFT, so he is seen in a deep THREE-QUARTER view turned away "
            "from the lens: his head is turned back over his right shoulder toward the "
            "black street and HIS GAZE EXITS THE PICTURE THROUGH THE UPPER RIGHT EDGE, "
            "never centred on the lens. Framed from the chest up. He is the same MALE "
            "traveller of about thirty, dust dried grey in the creases of his face and "
            "in his short black beard, in his DEEP RUST tunic and DARK OLIVE head "
            "cloth, the dark cloth bundle still roped over his right shoulder with the "
            "twisted flax cord biting into it. His expression is guarded and not yet "
            "certain of his welcome. No other face is in the frame."
        ),
    },
    {
        "id": "v2-r033-b37", "out": "s37-wearing-a-disguise.jpeg",
        "seg": "n7", "window": "137.203-140.772", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "ANCIENT-PRISON"] + _NIGHT,
        "narration": "was him wearing a disguise.",
        "must_show": "The prisoner's face close behind two thick timber bars, half of it lit from below by the clay lamp and half lost in black, his eyes down on the bread in his own hands.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no round machined steel bars, welded grid, lock plate, padlock or keyhole; nothing to suggest this man is Christ — no halo, no glow, no bright outline, no wound, no scar, no blood, no crown of thorns and no cream cloth; " + _NO_MODERN_LAMP + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 105mm lens at a wide aperture, deep night, the ONLY light "
            "the single small soft yellow flame of the shallow fired-clay oil lamp "
            "standing on the stone floor OUTSIDE the bars in the NEAR FOREGROUND, well "
            "BELOW his chin and NEARER THE CAMERA THAN HIS HEAD, so the light climbs "
            "steeply up the underside of his brow, nose and cheek and the whole crown "
            "and back of his head disappear into unlit black. Fine film grain, very "
            "shallow true depth of field. THE CAMERA IS OUTSIDE THE CELL AT HIS OWN "
            "HEIGHT AND ROUND TO HIS LEFT, so he is seen in a deep THREE-QUARTER view "
            "turned away from the lens: his head is bowed and turned down to his own "
            "right and HIS GAZE IS FIXED ON THE PIECE OF BARLEY BREAD IN HIS OWN TWO "
            "HANDS at the bottom of the frame, exiting the picture through the LOWER "
            "EDGE. Two THICK SQUARE-CUT TIMBER BARS, adzed flat and unpainted, cross "
            "the frame vertically in front of him, one dark and out of focus at the "
            "very edge. He is a MALE prisoner of about forty, gaunt, with a matted "
            "black beard, dirt in the lines of his face, unwashed black hair to his "
            "shoulders and a filthy DARK CHARCOAL tunic. His two dirty hands are "
            "cupped round the bread at his chest. He is an ordinary wretched man and "
            "nothing in the picture marks him out as anyone else."
        ),
    },
    # ================= n8 — the others walked straight past =================
    {
        "id": "v2-r033-b38", "out": "s38-waiting-for-a-king.jpeg",
        "seg": "n8", "window": "140.772-145.292", "wide": True, "jesus": False,
        "locks": ["GATEWAY", "MARKET-TOWN", "BACKGROUND-CAST"],
        "narration": "The others missed him for the very same reason. They were waiting to serve a king on a",
        "must_show": "Three well-dressed men standing together just inside the great stone gateway, all looking expectantly out and up along the empty approach road, waiting for someone important who is not coming.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no throne, crown, sceptre, banner, guard, soldier, spear or weapon; no arrival, procession, horse or chariot in view; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, bright hard late-morning sun coming in from "
            "the RIGHT and throwing the deep shadow of the gateway across the "
            "threshold slab, fine film grain, true depth of field. THE CAMERA STANDS "
            "INSIDE THE FORECOURT BEHIND THE THREE MEN AND SHOOTS PAST THEM out "
            "through the gateway: all three are seen from DIRECTLY BEHIND and in "
            "three-quarter from behind, their backs, shoulders and head cloths filling "
            "the near frame, and NOT ONE FACE IS TURNED TOWARD THE LENS. Every one of "
            "them is looking OUT AND UP along the empty approach road beyond the "
            "gateway, their gazes exiting the picture through the UPPER CENTRE of the "
            "opening. They are three ADULT MEN of about forty to sixty with well-fed "
            "builds and neatly trimmed dark beards, each in EXACTLY TWO PIECES OF "
            "CLOTH — one ankle-length tunic and one shoulder mantle — in solid rich "
            "saturated colours: DEEP MAROON, DEEP INDIGO and DARK OLIVE, each with a "
            "woven border band of a darker shade of the same colour. One has his hands "
            "clasped behind his back, one shades his eyes with a flat hand, one stands "
            "with his weight on one hip. THIS IS A WIDE FULL-LENGTH PHOTOGRAPH: all "
            "three men are visible head to sandals with the massive dressed limestone "
            "jambs and lintel around them and the empty road running away outside. The "
            "road beyond is completely empty — nobody is coming."
        ),
    },
    {
        "id": "v2-r033-b39", "out": "s39-walked-right-past-him.jpeg",
        "seg": "n8", "window": "145.292-149.792", "wide": True, "jesus": False,
        "locks": ["ELI", "ALLEY", "MARKET-TOWN", "BACKGROUND-CAST"],
        "narration": "throne, and they walked right past him a hundred times because he did not",
        "must_show": "A well-dressed man striding briskly through the alley with his face turned away, passing within a pace of Eli sitting against the wall, neither of them registering the other.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; nobody being struck, kicked, mocked or driven; no more than two people in the frame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, bright hard midday sun cutting the alley into "
            "one brilliant band of light and deep blue shade, the walking man in the "
            "light and the seated man in the shade, fine film grain, true depth of "
            "field. THE CAMERA IS SET LOW AT SEATED HEIGHT AND SIDE-ON TO THE ALLEY, "
            "so the walking man crosses the frame in PROFILE from RIGHT to LEFT and "
            "NEITHER FACE IS TURNED TOWARD THE LENS. The walking man is an ADULT MALE "
            "of about fifty, well-fed, with a neatly trimmed dark beard and thick dark "
            "hair under a DARK OLIVE head cloth, in EXACTLY TWO PIECES OF CLOTH — a "
            "solid DEEP MAROON ankle-length tunic with a darker woven border and a "
            "DARK UMBER shoulder mantle — mid-stride with his hem swinging and one "
            "sandal off the ground; HIS HEAD IS TURNED AWAY TO HIS OWN LEFT AND HIS "
            "GAZE GOES STRAIGHT UP THE ALLEY AHEAD OF HIM, exiting the picture through "
            "the LEFT EDGE. He passes within a single pace of ELI — the same gaunt "
            "fifty-five-year-old man with the thin ragged grey-and-black beard and the "
            "bare sun-darkened crown ringed with coarse grey hair, in his threadbare "
            "charcoal-brown tunic and torn dark umber hip cloth, barefoot — who sits "
            "back against the mud-brick wall in the shade at the LEFT of the frame "
            "with his knees up; ELI'S GAZE IS DOWN ON THE DUST BETWEEN HIS OWN FEET, "
            "exiting through the LOWER EDGE. Neither man looks at the other and "
            "neither reacts. THIS IS A WIDE FULL-LENGTH PHOTOGRAPH: both men are "
            "visible head to feet with the alley floor, both mud-brick walls and the "
            "flat roofline above."
        ),
    },
    {
        "id": "v2-r033-b40", "out": "s40-someone-who-needed-help.jpeg",
        "seg": "n8", "window": "149.792-154.389", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "ELI", "ALLEY"],
        "narration": "look like a king. He looked like someone who needed help.",
        "must_show": "Eli alone against the mud-brick wall of the empty alley, seen close and a little from the side, weary and entirely unremarkable, in the last low light of the day.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no second person; no crown, throne or sign of rank; nothing to suggest this man is Christ — no glow, no bright outline, no wound, no scar, no blood and no crown of thorns; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a wide aperture, warm low light at the end of "
            "the day coming in from the LEFT along the alley and lighting the front of "
            "his face and one shoulder, the sun out of frame, the mud-brick wall "
            "behind him dissolving into soft warm blur, fine film grain, shallow true "
            "depth of field. THE CAMERA IS SET AT HIS OWN SEATED EYE HEIGHT AND ROUND "
            "TO HIS LEFT, so he is seen in a THREE-QUARTER view turned away from the "
            "lens: his head rests back against the wall and is turned down and to his "
            "own right, and HIS GAZE IS ON HIS OWN OPEN HANDS LYING IN HIS LAP, "
            "exiting the picture through the LOWER RIGHT EDGE. Framed from the hips "
            "up. He is ELI, the same gaunt fifty-five-year-old man: hollow cheeks, dry "
            "sun-darkened olive-brown skin, deep-set dark brown eyes under heavy brows, "
            "a thin ragged beard of grey and black a hand's breadth below his chin, "
            "and a bare sun-darkened crown with a thick ring of coarse grey-and-black "
            "hair round the sides and back of his head curling untidily over his ears. "
            "He wears his threadbare CHARCOAL-BROWN wool tunic, patched at one "
            "shoulder and frayed at the hem, and the torn DARK UMBER cloth over his "
            "hips and left shoulder; his bare cracked feet are dusty. He is simply "
            "tired. NO OTHER PERSON IS IN THE FRAME."
        ),
    },
    # ================= n9 — the closing application =========================
    {
        "id": "v2-r033-b41", "out": "s41-that-is-how-good-he-is.jpeg",
        "seg": "n9", "window": "154.389-158.329", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET-STAIR", "DISCIPLES", "JESUS-SEATED", "BACKGROUND-CAST"],
        "narration": "That is how good he is. He did not hide himself behind",
        "must_show": "A wide view of the stair in the very last warm light with Jesus sitting among the men, ordinary and unremarkable among them, nothing setting him apart but his robe.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_JUDGEMENT + _NO_NIGHT + "no crown, throne, sceptre or robe of state; no shaft of light from the sky, no opening cloud, no radiance and no sun disc in frame; no woman and no child; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, the very last warm light of the day lying "
            "level across the stair from the LEFT, most of the picture already in cool "
            "blue shadow with only the tops of the steps and shoulders still catching "
            "gold, the sun out of frame, fine film grain, true depth of field. THE "
            "CAMERA STANDS BEHIND THE WHOLE GROUP, HIGH ON THE STAIR, AND LOOKS DOWN "
            "AND OUT OVER THEIR HEADS TOWARD THE VALLEY: EVERY SINGLE PERSON IN THIS "
            "PICTURE, JESUS INCLUDED, IS SEEN FROM BEHIND OR FROM THREE-QUARTER "
            "BEHIND, so what the lens sees is backs, shoulders, the backs of heads "
            "and the backs of head cloths, and NOT ONE FACE, NOT EVEN A PROFILE, IS "
            "PRESENTED TO THE CAMERA. A lens gaze is geometrically impossible in this "
            "composition because no eyes face the camera at all. Jesus sits among the "
            "men in the middle distance, seen from THREE-QUARTER BEHIND — the back of "
            "his own long dark wavy hair toward the lens, the cream wool of his "
            "shoulder and one forearm resting on his knee, only the far edge of his "
            "cheekbone catching the light — his head turned away from the camera and "
            "DOWN INTO THE MAN SITTING BELOW HIM. He is at the same level as the men, "
            "no higher, and nothing in the composition centres or elevates him. NO "
            "SECOND LONG-HAIRED PALE-ROBED FIGURE SITS ANYWHERE IN THIS PICTURE. "
            "THIS IS A WIDE "
            "FULL-LENGTH GROUP PHOTOGRAPH AND NOT A PORTRAIT: the stair, the low "
            "dry-stone wall, the old olive trees and the empty tawny valley beyond are "
            "all in the frame with all the men head to sandals. THE ONLY PALE WOOL IN "
            "THE PICTURE IS HIS OWN ROBE; every disciple is a solid dark mass of "
            "indigo, umber, rust, olive or charcoal."
        ),
    },
    {
        "id": "v2-r033-b42", "out": "s42-something-impressive.jpeg",
        "seg": "n9", "window": "158.329-161.649", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "ELI", "ALLEY"],
        "narration": "something impressive. He hid in the people easiest to",
        "must_show": "An extreme close view of Eli's two worn empty male hands lying open in his lap, cracked and dust-grey, with the frayed hem of his charcoal-brown tunic across his knees.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no face or head of any person in the frame; no wound, scar, nail mark, blood or piercing on either hand; no ring, bracelet or jewellery; no coin or money; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens at a wide aperture, warm low light at "
            "the end of the day coming in from the LEFT and raking across the skin, "
            "the alley behind dissolving completely, fine film grain, very shallow "
            "true depth of field. THE CAMERA IS DOWN AT LAP HEIGHT AND SLIGHTLY TO THE "
            "SIDE, framing ONLY the hands and knees: no face and no head is in the "
            "picture at all. TWO ADULT MALE HANDS of an older man lie open and empty, "
            "palms up, in his own lap — thin, sun-darkened olive-brown, the knuckles "
            "enlarged, the tendons standing, the palms hard and cracked with grey dust "
            "deep in every line, the nails short, ridged and split. There is NO wound, "
            "scar, nail mark, blood or piercing on either hand and no ring or "
            "jewellery of any kind. Across his knees behind them lie the frayed hem of "
            "a threadbare CHARCOAL-BROWN woven wool tunic, its warp and weft plainly "
            "visible, and a fold of torn DARK UMBER cloth. Nothing else is in the "
            "frame."
        ),
    },
    {
        "id": "v2-r033-b43", "out": "s43-ordinary-kindness.jpeg",
        "seg": "n9", "window": "161.649-165.509", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "MIRIAM", "ELI", "ALLEY", "BACKGROUND-CAST"],
        "narration": "overlook, so that plain, ordinary kindness would always reach",
        "must_show": "Miriam crouching down again to Eli at the foot of the alley wall, seen from behind her shoulder, offering a fired-clay cup, the whole thing small and unremarkable in the warm last light.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no third person; no bare, bald or shaven head on the woman; no bright outline or rim around her head or shoulders; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens at a wide aperture, warm low light at the end "
            "of the day coming in from the LEFT down the alley, the sun out of frame "
            "and never behind her head, fine film grain, shallow true depth of field. "
            "THE CAMERA IS SET LOW BEHIND MIRIAM'S RIGHT SHOULDER AND SHOOTS PAST HER "
            "toward Eli: she is seen from THREE-QUARTER BEHIND, the back of her head, "
            "her right shoulder and the fall of her dark rust-brown mantle occupying "
            "the near left of the frame slightly out of focus, and HER FACE IS NOT "
            "VISIBLE TO THE LENS. HER DARK OLIVE HEAD CLOTH IS ON HER HEAD WITH A BAND "
            "OF HER THICK BLACK HAIR SHOWING AT THE NAPE BELOW IT — it is not a bare, "
            "bald, shaven or cropped head. She is crouched right down on her heels, "
            "holding out a small fired-clay cup in her right hand. Beyond her, sharp "
            "in focus, ELI sits back against the mud-brick wall — the same gaunt "
            "fifty-five-year-old man with the thin ragged grey-and-black beard and the "
            "bare crown ringed with coarse grey hair, in his threadbare charcoal-brown "
            "tunic and torn dark umber hip cloth — reaching up with his right hand "
            "toward the cup. HIS GAZE IS ON THE CUP, exiting the picture through the "
            "LEFT EDGE. Mid-action, the cup not yet taken, unposed. No other person is "
            "in the alley."
        ),
    },
    {
        "id": "v2-r033-b44", "out": "s44-stands-in-front-of-you.jpeg",
        "seg": "n9", "window": "165.509-169.109", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "ALLEY", "MARKET-TOWN"],
        "narration": "him. So when someone small and needy stands in front of",
        "must_show": "A small barefoot child standing still in a village doorway in flat overcast daylight, seen from outside and slightly below, waiting, with nobody else in the frame.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no Jesus in this frame and nobody in cream, off-white or pale cloth of any kind; no second person; no bright rim, outline or halo around the child's head, hair or shoulders and no light source behind or above the head; no glass, shutter, hinge or door of planks; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens at a wide aperture, FLAT COLOURLESS OVERCAST "
            "DAYLIGHT falling evenly from the whole sky with no sun anywhere and no "
            "bright source behind the child at all — the light INSIDE the doorway is "
            "dimmer than the light outside, so the child stands against a DARK interior "
            "and there is no rim, edge or outline of light anywhere on the head, hair "
            "or shoulders. Fine film grain, shallow true depth of field. THE CAMERA IS "
            "OUT IN THE STREET, SET LOW AT THE CHILD'S OWN CHEST HEIGHT AND OFF TO THE "
            "LEFT so the doorway is seen at a slight angle: the child is turned in a "
            "THREE-QUARTER view away from the lens, the head tipped down and to its "
            "own right, AND ITS GAZE IS ON THE WORN LIMESTONE THRESHOLD SLAB AT ITS "
            "OWN FEET, exiting the picture through the LOWER EDGE. The child is about "
            "seven, barefoot, thin, with warm olive-brown skin and dark hair cut "
            "roughly at the ears, wearing ONE piece of cloth only — a plain DARK OLIVE "
            "woven wool tunic to the shin, worn and patched at one knee — and standing "
            "quite still with both arms hanging at its sides. The doorway is one plain "
            "rectangular opening in tan mud brick with rough hewn timber jambs and "
            "lintel and a heavy dark goat-hair cloth pushed half aside. NO OTHER "
            "PERSON IS IN THE FRAME."
        ),
    },
    {
        "id": "v2-r033-b45", "out": "s45-it-might-be-him.jpeg",
        "seg": "n9", "window": "169.109-173.179", "wide": False, "jesus": False,
        "locks": ["CLEAR-EDGES", "ALLEY"],
        "narration": "you, that is not an interruption. It might be him.",
        "must_show": "An extreme close view of a small child's two hands closing around a fired-clay cup as an adult woman's two hands let go of it, warm last light on the clay, nothing else in frame.",
        "must_not_show": _NO_HALO + _NO_JUDGEMENT + _NO_NIGHT + "no face or head of any person in the frame; no wound, scar, nail mark or blood on any hand; no ring, bracelet or jewellery; no coin or money; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens at a wide aperture, warm low light at "
            "the very end of the day coming in from the LEFT and glancing off the damp "
            "rim of the clay, everything behind dissolving into warm blur, fine film "
            "grain, very shallow true depth of field. THE CAMERA IS DOWN AT HAND "
            "HEIGHT AND SIDE-ON, framing ONLY the hands and the cup: no face and no "
            "head is in the picture at all. Filling the centre of the frame is a small "
            "round fired-clay cup, its surface matte and unglazed, a little water "
            "standing in it. TWO SMALL CHILD'S HANDS come up from the lower edge and "
            "close round its body. THEY ARE UNMISTAKABLY A YOUNG CHILD'S HANDS: LESS "
            "THAN HALF THE SIZE of the adult hands beside them, with short stubby "
            "fingers, plump soft unlined skin, dimpled knuckles and small grubby "
            "nails — not an adult's hands and not a teenager's. A DARK OLIVE sleeve "
            "of coarse hand-woven wool sits at one small wrist. TWO ADULT FEMALE "
            "HANDS come down from the upper edge and are just releasing the cup — "
            "clearly larger, olive-brown, work-roughened but smooth-knuckled, no ring "
            "and no jewellery of any kind, the cuffs of a DEEP INDIGO sleeve at both "
            "wrists — the fingers already lifting clear. There is no wound, scar or "
            "mark on any hand."
            "HER SLEEVE IS COARSE HAND-WOVEN WOOL AND SHOWS IT: a visible over-and-under grid of warp and weft threads on a flat matte surface with a plain frayed cut edge, never a knitted, ribbed, cabled or cuffed sleeve. "
            "Behind them only the blurred warm dust of the alley floor. Mid-action, at "
            "the exact instant of handing over."
        ),
    },
]
