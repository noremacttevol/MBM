#!/usr/bin/env python3
"""V2 beat map — row 34, build-34-rich-fool (Luke 12:16-21). REALISTIC V2.

THE INHERITED SCAFFOLD WAS DISCARDED for a measured reason: it planned 21 pictures
at 5.7 s each and called that "the library density", against the wave's measured
3.1-4.9 s per picture across rows 24-33. A picture costs about thirteen cents and
regenerates in seconds; a five-and-a-half second hold is the exact defect V2 exists
to remove.

WHAT V1 ACTUALLY DID (verified against the artefact, not the prose):
  SEVEN stills for 128.13 s, and two of them are REUSED, so the closing
  application has no picture of its own at all.
    * `s3.jpeg` covers j3 + n3 + n4 — 14.77 s to 35.09 s, TWENTY AND A THIRD
      SECONDS on ONE picture, carrying the whole of Luke 12:18 (the red-letter
      line the parable turns on, "I will pull down my barns, and build greater")
      plus both narrator restatements of it.
    * `s4.jpeg` covers j4 + n5 + n6 — 35.09 s to 60.05 s, TWENTY-FIVE SECONDS,
      i.e. the second red-letter verse (12:19, "take thine ease, eat, drink, and
      be merry") AND the entire portrait of the man's self-absorption.
    * `s6.jpeg` covers n8 + n9 + n10 — 74.53 s to 93.99 s, NINETEEN AND A HALF
      SECONDS — and is then REUSED for n11 at 100.49 s, so the same picture
      carries both the end of the man's life and the moral drawn from it.
    * `s7.jpeg` covers j2 and is then REUSED for n12, so the ELEVEN-AND-A-HALF
      SECOND closing question — the reason the video exists — is shown on a
      picture the viewer has already been looking at.
  V2 gives every one of the 17 spoken segments its own pictures: 35 pictures over
  119.22 s = 3.41 s/picture.

AUDIO: LOCKED, never re-voiced. The V1 MP4 (128.133 s) and all eighteen mp3s share
ONE git content date (2026-07-27T23:02:58), and the summed V1 timeline is 128.087 s,
so the V1 stream sits 0.046 s past it — far inside the 0.75 s staleness tripwire.
Neither tripwire fires; the normal packet-copy AUDIO LOCK applies. Nothing is
re-voiced and V1 is never written to.

SOURCING TRAP CHECKED AND CLEARED: all 18 segments transcribed with faster-whisper
(small.en, word_timestamps=True) against the LIVE make_narration.py. Every segment
matches. ONE apparent difference was chased down and it is whisper's, not the
script's: j1 "then whose shall those things be" came back as "then who shall" —
whisper dropping the final consonant of the archaic "whose", the same failure family
as row 33's "an hungred". The script, and therefore the CAPTION, carries the
verbatim KJV. No TEXT_OVERRIDES.

WINDOWS: rebuilt from scratch from extract_beats plus the measured word timings —
twelve of the eighteen `.timing.json` sidecars hold ONE phrase spanning the whole
segment and could not supply an interior split. Contiguous 0.000 -> 119.216 (the
card's own start), ZERO gaps, shortest 2.20 s, longest 4.82 s, 3.41 s/picture, and
every one of the 17 speech onsets lands inside the window written for it.

SCRIPTURE FACTS (Luke 12:16-21 KJV):
  v16  "The ground of a certain rich man brought forth plentifully" — a harvest, not
       a windfall. The man is a FARMER and the story is agricultural end to end.
  v18  "I will pull down my barns, and build greater" — the parable's hinge, and the
       reason this build needed a BARN lock before its first paid image.
  v19  "Soul, thou hast much goods laid up for many years; take thine ease, eat,
       drink, and be merry."
  v20  "Thou fool, this night thy soul shall be required of thee." God's line, voiced
       by Jesus INSIDE the parable, so the caption inks RED (see make_narration.py).
  v21  "So is he that layeth up treasure for himself, and is not rich toward God."

WHY JESUS IS NOT ON SCREEN FOR j3, j4 AND j1: those three red-letter segments are
not Jesus speaking as himself. j3 and j4 are the RICH MAN'S own greedy words quoted
inside the parable, and j1 is GOD's answer to him. Painting Jesus's face under a
caption of the rich man's boasting would be worse than painting nothing. Those three
are staged inside the parable where the words are actually said, and Jesus carries
the frame he really speaks in: n0 opening it, and n10/j2/n12 closing it.

CONTENT CARE — THE HARDEST CALL ON THIS ROW: v20 is the most direct death line in
the wave, and the temptation is to paint the moment of death. IT IS NOT PAINTED.
There is no corpse, no dying man, no deathbed, no last breath, no soul, spirit,
wisp, mist or figure of light leaving a body; no angel, no wing, no reaching hand
from the sky, no tunnel, no gate, no scales, no throne, no judgement seat and no
afterlife of any kind anywhere in this build. God is never depicted as any figure,
face, form, light or presence. What IS painted is only what the parable itself
states, and it is enough: the full barns, the barns torn down, the greater barns
built, the man alone with his goods, and the morning that comes without him — a
door left standing open, a lamp burnt out and cold on the threshold, other men's
hands carrying his grain away. n9's "he would stand before God" is staged as the
swept empty threshing floor under a vast open dawn sky with one line of footprints
crossing the chaff and going out, and no returning line beside it. The man is never
shown with a wound, a scar, blood, a glow or cream cloth, so no figure in this build
can read as the crucified Christ (the row-31 lesson).

STAGING — five places, none of them used elsewhere in the realistic wave:
  * a great lone TEREBINTH on open dry ground where Jesus teaches the multitude
    (row 31's Olivet was an open boulder shoulder, row 32's a shaded olive-canopy
    terrace, row 33's a rock-cut limestone stair — this is one wide tree standing
    by itself on flat harvest country, and it carries no city and no settlement);
  * a windswept ridge THRESHING FLOOR of worn bare bedrock (row 25's wheat field was
    STANDING wheat with tares among it; this land is REAPED — stubble, stooked
    sheaves and heaped winnowed grain — and that difference is stated positively in
    the JUDEAN-LAND lock so the model cannot drift back to a standing crop);
  * a GRANARY YARD of squat mud-brick bins, first full, then torn down, then rebuilt;
  * the INTERIOR of the new great granary, dim and dusty under rough hewn beams;
  * a walled COURTYARD with a low supper table — by daylight, by lamp, and empty.
No skyline of Jerusalem or of any city appears anywhere in this build; it was
deleted from every lock before the first paid image, per rows 31/32/33.

NEW SHARED LOCK ADDED BY THIS ROW: GRANARY-BARN in v2_prompt.py. "Barn" is one of
the most modern-loaded nouns in English and PERIOD-MATERIALS cannot reach it,
because a barn is ARCHITECTURE, not an object — the same way a road surface (row 29)
and a prison cell (row 33) slip through. See the comment above the lock.

CAST: ONE anchor, generated in its OWN run before anything else so the REFS cache
cannot make the anchor reference itself, then wired into every later LANDOWNER beat
by `char_refs`.
  b04 LANDOWNER — a real placed picture on the timeline and a face-showing shot, so
  the anchor costs nothing extra. Jesus needs no anchor: he carries JESUS-V2-REF.
"""

import os

OUTPUT_ASSET_DIR = "assets"

# The V1 MP4 (128.133 s) and all eighteen mp3s share ONE git content date
# (2026-07-27T23:02:58) and the summed timeline is 128.087 s. Neither staleness
# tripwire fires; the normal packet-copy AUDIO LOCK applies.
AUDIO_FROM_V1_SEGMENTS = False

REF = True

# Wired in AFTER the b04 anchor beat is generated in its own run.
ANCHOR = "assets/s04-ran-out-of-room.jpeg"
REFS = {"LANDOWNER": ANCHOR}

# ANCHOR-FIRST: the character reference attaches itself only once the b04 anchor
# actually exists on disk. On the first (anchor-only) run the list is empty, so the
# REFS cache cannot make the anchor reference itself and `--check` passes; every
# run after it wires the accepted anchor into all fifteen later LANDOWNER beats.
_MAN = [ANCHOR] if os.path.isfile(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), ANCHOR)) else []

# ---------------------------------------------------------------- negatives ---
_NO_CREAM = ("no cream, off-white, ivory, buff, beige, taupe, sand, khaki, white "
             "or pale garment, tunic, robe, mantle, sash, wrap or head covering on "
             "anybody anywhere in the frame including the blurred edges; ")
_NO_HALO = ("no halo, no nimbus, no aura, no corona, no bright outline, edge or "
            "contour around any head, hair, shoulder or body, and no light source "
            "of any kind standing behind, above or beyond anyone's head; ")
_NO_CITY = ("no city, town, village skyline, wall, gate tower, dome, minaret, bell "
            "tower, spire, tiled or pitched roof, crenellation or distant row of "
            "buildings anywhere in this frame; ")
_NO_DEATH = ("no corpse, dead body, dying man, deathbed, sickbed, last breath, "
             "closed eyes of a dead face, shroud, bier, grave, tomb or funeral; no "
             "soul, spirit, ghost, wisp, mist, vapour or figure of light leaving or "
             "standing over any body; no angel, wing, feather or winged figure; no "
             "hand, arm or face reaching down from the sky; no throne, seat of "
             "judgement, scales, balance, open book, gate, doorway of light, tunnel, "
             "cloud of glory, opening sky, shaft of light from above or radiance of "
             "any kind; and no depiction of God as any figure, face, form, light or "
             "presence; ")
_NO_MODERN_FARM = ("no metal or concrete silo, grain bin, hopper, chute, auger, "
                   "elevator or conveyor; no corrugated iron, tin or sheet metal; no "
                   "sawn plank, board, weatherboard, plywood or pallet; no red "
                   "boarded barn, pitched or gabled roof, shingle, hayloft or "
                   "weather vane; no tractor, trailer, machine, engine or pneumatic "
                   "tyre; ")
_NO_GREEN = ("no green meadow, lawn, turf, pasture, moor, fell, upland, heather, "
             "hedgerow, deciduous woodland or lush temperate countryside of any "
             "kind, and no soft grey overcast northern European sky; ")
_NO_NIGHT = ("no night, no darkness, no stars, no lamp and no flame anywhere in "
             "this frame; ")
_NO_MODERN_LAMP = ("no candle, wax or taper, no glass, chimney, globe or shade, no "
                   "hurricane lamp, storm lantern, kerosene lamp or oil lantern, no "
                   "metal lamp, no hanging fixture, no ring handle, and no electric "
                   "light of any kind; ")
_GAZE = "nobody's pupils centred on the lens."

_DAY = ["GRANARY-BARN", "JUDEAN-LAND", "LANDOWNER", "WORKERS", "HAND-TOOLS"]
_NIGHT = ["GRANARY-BARN", "JUDEAN-LAND", "LANDOWNER", "NIGHT-LAMPLIGHT"]

LOCKS = {
    # ------------------------------------------------------------- people ----
    "LANDOWNER": (
        "LANDOWNER LOCK: the rich farmer is the SAME MAN in every picture he appears "
        "in, and he is a JUDEAN of the first century, born and worked in the dry "
        "country of that place. He is about fifty-five, heavy through the chest and "
        "thickening at the waist, a prosperous working farmer rather than a soft "
        "townsman. HIS SKIN IS DEEPLY SUN-DARKENED WARM OLIVE-BROWN, weathered and "
        "creased across the forehead and fanning from the outer corners of dark brown "
        "eyes, with a broad blunt nose and heavy dark brows. He has a FULL HEAVY "
        "BEARD, black shot through with iron grey, cut broad and square at the jaw "
        "and reaching the top of his chest. HIS HAIR IS THICK, BLACK AND GREYING AT "
        "THE TEMPLES, waving back off a high creased forehead to the nape of his "
        "neck; it is never a bare, bald, shaven, cropped or thinning head, and a "
        "clear band of that thick greying hair shows at the front edge, at the "
        "temples and at the nape in EVERY shot, including every shot taken from "
        "behind him. His hands are big, blunt-fingered, split-nailed and grimed from "
        "work. HE WEARS EXACTLY THREE SEPARATE PIECES OF CLOTH AND NOTHING ELSE: "
        "(1) ONE ankle-length hand-woven wool tunic in DEEP RUST-BROWN with straight "
        "unshaped sleeves to the elbow; (2) ONE rectangular hand-woven wool mantle in "
        "DARK UMBER thrown over the left shoulder and hanging down his back; and "
        "(3) ONE folded cloth sash of DARK OLIVE knotted at his waist. On his feet, "
        "worn leather sandals. HE NEVER WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, "
        "SAND, KHAKI, WHITE OR ANY PALE CLOTH, and he wears no head covering, no "
        "turban, no cap, no jewellery, no ring, no brooch, no clasp, no chain and no "
        "belt of manufactured metal. He is a healthy living man in every frame: no "
        "wound, no scar, no blood, no bandage and no glow anywhere on him."
    ),
    "WORKERS": (
        "FARM-WORKERS LOCK: the labourers on this farm are between two and four ADULT "
        "MEN of the first century, aged from about twenty to about forty-five, all of "
        "them Judean field hands with weathered sun-darkened olive-brown skin, dark "
        "hair and short dark beards, and no two of them share a face. Every one of "
        "them is younger, leaner and plainer than the landowner and none of them is "
        "ever mistaken for him. EACH WEARS EXACTLY TWO SEPARATE PIECES OF CLOTH AND "
        "NOTHING ELSE: (1) one knee-length or calf-length hand-woven wool work tunic, "
        "hitched up and tucked into (2) one twisted cloth belt at the waist — and "
        "each man's cloth is ONE SOLID DARK SATURATED EARTH COLOUR head to foot: DEEP "
        "INDIGO, DARK UMBER, DARK OLIVE, CHARCOAL or DEEP MAROON, so every worker in "
        "the frame is a DARK MASS from edge to edge, in focus or out of focus, near "
        "or far. NOT ONE OF THEM WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, "
        "SAND, KHAKI, WHITE OR PALE GREY CLOTH OF ANY KIND. They are barefoot or in "
        "plain leather sandals, and they are working, never posing."
    ),
    "CROWD": (
        "CROWD LOCK: the multitude listening to Jesus is a large press of ordinary "
        "first-century Judean country people — men, women and a few children "
        "together — sitting and standing on the dry ground. Every single person in "
        "the crowd, near or far, sharp or blurred, is dressed head to foot in ONE "
        "SOLID DARK SATURATED EARTH COLOUR: DEEP INDIGO, DARK UMBER, DEEP RUST, DARK "
        "OLIVE, CHARCOAL or DEEP MAROON, so the whole crowd reads as a DARK MASS "
        "across the frame. NOT ONE PERSON IN THE CROWD WEARS CREAM, OFF-WHITE, "
        "IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI, WHITE, PALE GREY OR ANY LIGHT-TONED "
        "CLOTH, DRAPE, MANTLE, SHAWL, TUNIC, SASH OR HEAD COVERING, at any distance "
        "and at any focus — a pale figure in this crowd reads as a second, unlocked "
        "Jesus and fails the picture. THE ONLY LIGHT-TONED THINGS ANYWHERE IN THE "
        "FRAME ARE BARE STONE, DUST, DRY STUBBLE, REED BASKETRY, RAW TIMBER AND BARE "
        "SKIN — and Jesus's own wool robe. Everyone in the crowd faces inward toward "
        "Jesus; nobody in the crowd faces the camera."
    ),
    # ------------------------------------------------------------- places ----
    "JUDEAN-LAND": (
        "JUDEAN-HARVEST-LAND LOCK: this is the dry farming country of first-century "
        "JUDEA at the very end of harvest, and the land is stated positively. The "
        "ground is SCORCHED STRAW-GOLD STUBBLE, cut short and sharp, over pale "
        "chalky limestone that breaks through in bald shelves and slabs. Everything "
        "is in the colours of drought: bleached gold, straw, tan, pale ochre, dust "
        "grey and the dark grey-green of a few dusty olive and terebinth trees. The "
        "soil is fine pale tan dust that lifts around every foot. Low dry-stone field "
        "terraces of unmortared limestone step down the slopes, with thistle, thorn "
        "scrub and dead sun-bleached grass in their corners. THE SKY IS THE HARD "
        "CLEAR PALE BLUE OF A HOT DRY COUNTRY, whitening toward the horizon. THIS IS "
        "REAPED LAND, NOT STANDING CROP: there is no field of tall standing green or "
        "golden wheat waving in the wind anywhere in this build — only cut stubble, "
        "bound sheaves stacked in stooks, and heaped threshed grain. THERE IS NO "
        "GREEN COUNTRYSIDE ANYWHERE IN THIS FRAME: no green grass, lawn, turf, "
        "meadow, pasture, moor, fell, upland, heather, bracken, hedgerow, deciduous "
        "wood, oak, birch, pine forest, fern, ivy, rolling green hill or lush "
        "temperate valley, and no soft grey overcast northern sky. Nothing in this "
        "picture is Britain, Ireland, Scandinavia, the Alps or the American Midwest."
    ),
    "THRESHING": (
        "THRESHING-FLOOR LOCK: the threshing floor is a wide flat circle of worn bare "
        "BEDROCK on an exposed ridge where the wind runs, swept clean, its surface "
        "polished pale by generations of hooves and sledges, with a low kerb of loose "
        "unmortared field stones ringing it. On it lie a heaped mound of threshed "
        "grain and a drift of pale chaff and broken straw, with bound sheaves stacked "
        "in stooks at the edge and hand-woven reed baskets and coarse dark goat-hair "
        "sacks set about. The floor is open to the sky on every side with nothing "
        "built on it and nothing built beside it. THERE IS NO BUILDING, ROOF, FENCE, "
        "POST, POLE, WIRE, GATE, TRACK OR VEHICLE ANYWHERE ON OR AROUND THIS FLOOR, "
        "and no machine of any kind: the grain is separated by an ox-drawn sledge of "
        "hewn planks studded with flint, by flails of two pegged sticks, and by "
        "wooden winnowing forks throwing it into the wind."
    ),
    "GRANARY-YARD": (
        "GRANARY-YARD LOCK: the yard is a flat swept apron of packed pale tan earth "
        "on a limestone shelf, ringed by a low unmortared dry-stone wall about "
        "waist high, with the squat plastered mud-brick grain bins standing on it and "
        "a single dusty terebinth throwing shade at one side. Underfoot the earth is "
        "beaten smooth and strewn with spilled grain, chaff and straw, with hand-woven "
        "reed baskets, coarse dark goat-hair sacks and fired-clay jars standing about "
        "and a hand-hewn wooden scoop lying where it was dropped. Beyond the wall the "
        "reaped terraces fall away into empty bleached harvest country and bare "
        "limestone hills, and there is NOTHING ELSE ON THE HORIZON — no city, town, "
        "village, wall, tower, dome, spire or distant row of buildings anywhere."
    ),
    "COURTYARD": (
        "SUPPER-COURTYARD LOCK: the courtyard is a small private square of beaten "
        "earth and worn flagstones enclosed by plain mud-plastered walls the colour "
        "of pale tan clay, with ONE low doorway of rough stone jambs closed by a "
        "hanging panel of dark woven cloth, and an old vine trained on rough poles "
        "across one corner for shade. In the middle stands ONE low table — a slab of "
        "adzed timber on four hewn legs, knee high — with plain flat rounds of "
        "barley bread, a shallow fired-clay bowl of olives, a fired-clay wine jar and "
        "two plain fired-clay cups set on it, and folded woollen mats and a bolster "
        "of dark cloth laid on the ground beside it for reclining. THERE IS NO CHAIR, "
        "STOOL, BENCH, COUCH OR FURNITURE OF ANY OTHER KIND, no cushion of printed or "
        "patterned fabric, no tablecloth of woven pattern, no glass, no metal vessel, "
        "no cutlery, no plate of any kind, no window of glass, no hinged door and "
        "nothing hanging on the walls."
    ),
    "TEREBINTH": (
        "TEREBINTH LOCK: Jesus is teaching in the open under ONE great lone terebinth "
        "tree standing by itself on flat dry harvest country — a broad low dome of "
        "dusty grey-green foliage on a thick gnarled trunk, throwing a wide pool of "
        "shade onto bare pale tan dust and cut stubble. The land runs away flat and "
        "empty on every side into bleached reaped terraces and low bare limestone "
        "hills. There is NO OTHER TREE NEAR IT, no grove, no orchard and no wood. "
        "AGAINST THE SKY THERE IS ONLY BARE HILL AND OPEN AIR: no city, town, "
        "village, house, wall, gate, tower, dome, minaret, bell tower, spire, "
        "crenellation, tiled or pitched roof or distant row of buildings anywhere on "
        "any horizon of this frame."
    ),
    "GRANARY-IN": (
        "GRANARY-INTERIOR LOCK: inside the great new grain store the air is dim, "
        "still and thick with floating dust. The walls are mud brick plastered smooth "
        "with mud and chopped straw, unpainted, the colour of pale tan clay, and the "
        "low roof is carried on three ROUGH HEWN TIMBER BEAMS with bark still on "
        "parts of them, adzed flat only where they bear on the wall heads and lashed "
        "with twisted flax cord. The floor is hard plastered earth. Grain lies in a "
        "great loose heap running up toward the beams at the back, with hand-woven "
        "reed baskets and coarse dark goat-hair sacks standing at the foot of it. "
        "THERE IS NO WINDOW, NO GLASS, NO HINGED DOOR, no shelf, no rack, no ladder "
        "of milled rungs, no sawn board, no metal, no chute and no machine of any "
        "kind anywhere inside this building."
    ),
}

BEATS = [
    # ==================== n0 — Jesus begins the parable =======================
    {
        "id": "v2-r034-b01", "out": "s01-jesus-told-a-story.jpeg",
        "seg": "n0", "window": "0.000-3.917", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TEREBINTH", "CROWD", "JUDEAN-LAND"],
        "narration": "Jesus told a story about a rich man who had a very good year.",
        "must_show": "Jesus sitting in the shade of the great lone terebinth, teaching, with a large crowd of ordinary country people sitting and standing on the dry ground around and in front of him in the middle of a hot bright day.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard bright midday sun coming steeply from "
            "the upper LEFT and broken into moving dapple by the terebinth canopy, "
            "fine film grain, true depth of field. THE CAMERA STANDS BEHIND AND "
            "ABOVE THE BACK OF THE CROWD AND SHOOTS DOWN AND PAST THEM toward "
            "Jesus: the nearest six or seven listeners fill the lower third of the "
            "frame as dark heads, shoulders and backs seen entirely FROM BEHIND, and "
            "NOT ONE FACE IS TURNED TOWARD THE LENS. Jesus sits on a low limestone "
            "slab at the foot of the trunk, a little left of centre in the middle "
            "distance, seen in three-quarter view with one hand open and low at his "
            "own chest height; his gaze travels down and to the RIGHT across the "
            "seated people and exits the picture through the RIGHT EDGE. THIS IS A "
            "WIDE FULL-LENGTH GROUP PHOTOGRAPH AND NOT A PORTRAIT: the camera is far "
            "enough back that Jesus and thirty or more listeners appear together "
            "head to sandals, with the terebinth above them and the bleached reaped "
            "country running away flat and empty behind. Jesus occupies only a small "
            "part of the frame. THE ONLY PALE WOOL IN THE WHOLE PICTURE IS HIS OWN "
            "ROBE; every other person in the frame is a solid dark saturated mass of "
            "indigo, umber, rust, olive, charcoal or maroon from edge to edge, in "
            "focus and out of focus alike."
        ),
    },
    # ==================== n1 — the harvest was enormous ========================
    {
        "id": "v2-r034-b02", "out": "s02-his-fields-produced.jpeg",
        "seg": "n1", "window": "3.917-6.437", "wide": True, "jesus": False,
        "locks": _DAY + ["THRESHING"], "char_refs": _MAN,
        "narration": "His fields produced an enormous harvest —",
        "must_show": "The landowner standing at the edge of the ridge threshing floor with his back to the camera, looking out and down over his own reaped terraces where bound sheaves stand stacked in stooks across the stubble.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_MODERN_FARM + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 40mm lens, late-morning sun high and slightly behind "
            "the camera so the land in front is fully lit and no head is backlit, "
            "fine film grain. THE CAMERA STANDS CLOSE BEHIND THE LANDOWNER AND "
            "SHOOTS PAST HIM over his right shoulder: he is seen ENTIRELY FROM "
            "BEHIND, standing three-quarter length at the LEFT of the frame with his "
            "dark umber mantle hanging down his back and his deep rust-brown tunic "
            "below it, one big blunt hand hooked in his dark olive waist sash. "
            "BECAUSE THE CAMERA IS BEHIND HIS HEAD, HIS HAIR IS THE THING THE VIEWER "
            "SEES OF HIM AND IT IS STATED HERE: a thick mop of black hair going iron "
            "grey at the temples, waving back off the crown and curling onto the nape "
            "of his neck and the top of his mantle — it is NOT a bare, bald, shaven, "
            "cropped or thinning head, and he wears nothing on it. His face is not "
            "visible at all and NOT ONE FACE IS TURNED TOWARD THE LENS. Beyond and "
            "below him the reaped terraces fall away in steps of straw-gold stubble "
            "with BOUND SHEAVES STACKED IN STOOKS across them, pale limestone "
            "breaking through, and the hard clear pale blue sky whitening at a bare "
            "empty horizon. Dust hangs in the air between the camera and the "
            "furthest terrace."
        ),
    },
    {
        "id": "v2-r034-b03", "out": "s03-more-grain-than-ever.jpeg",
        "seg": "n1", "window": "6.437-10.545", "wide": False, "jesus": False,
        "locks": _DAY + ["THRESHING"], "char_refs": _MAN,
        "narration": "more grain and fruit than he had ever gathered in his life.",
        "must_show": "A wooden winnowing fork throwing threshed grain up into the wind above the great heaped mound on the threshing floor, the heavy grain falling back and the pale chaff blowing away sideways.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_MODERN_FARM + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens, strong side sun raking from the RIGHT and "
            "blazing through the flying chaff, fast shutter so every grain and husk "
            "is frozen sharp in the air, fine film grain. THE CAMERA IS LOW AND "
            "SLIGHTLY BEHIND THE WORKER, at the height of the grain heap, and shoots "
            "past his shoulder into the throw: he is seen from behind and to the side "
            "as a dark charcoal-clad back and two braced arms in the lower LEFT of "
            "the frame, his head turned away up after the grain, HIS FACE NOT VISIBLE "
            "and no face anywhere turned toward the lens. THE SUBJECT OF THE PICTURE "
            "IS THE THROW ITSELF: a broad fan of golden threshed barley arcing up "
            "through the middle of the frame off the tines of a HAND-HEWN WOODEN "
            "WINNOWING FORK of one rough branch split into five worn wooden tines, "
            "the heavy grain already curving back down onto the mound and the light "
            "pale chaff streaming off to the RIGHT on the wind and out of the frame. "
            "Below, the great mound of clean threshed grain fills the bottom of the "
            "picture, its surface pocked and shifting. Behind, the bare polished "
            "bedrock floor, the ring of loose field stones and open pale sky."
        ),
    },
    # ============ n2 — ANCHOR: he ran out of room (face-showing) ==============
    {
        "id": "v2-r034-b04", "out": "s04-ran-out-of-room.jpeg",
        "seg": "n2", "window": "10.545-14.770", "wide": False, "jesus": False,
        # ANCHOR BEAT — generated in its OWN run before every other beat, so the
        # REFS cache cannot make this picture reference itself. No char_refs here.
        "locks": _DAY + ["GRANARY-YARD"],
        "narration": "In fact, he had so much that he ran out of room to store it all.",
        "must_show": "The landowner standing in his granary yard in front of three squat plastered mud-brick grain bins, looking at grain that has been heaped on the ground outside them because there is no more room inside, his face clearly visible in strict side-on profile.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_MODERN_FARM + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens, warm low mid-afternoon sun coming in almost "
            "level from the LEFT and modelling the face from the front, fine film "
            "grain, shallow but honest depth of field. THIS IS A STRICT SIDE-ON "
            "PROFILE AND THE CAMERA SITS EXACTLY ON HIS LEFT: the landowner stands "
            "three-quarter length at the RIGHT of the frame turned fully to the "
            "LEFT, so the viewer sees ONE cheek, ONE eye, ONE ear and the clean "
            "outline of brow, nose, lips and beard against the yard beyond. THE FAR "
            "CHEEK AND THE FAR EYE ARE COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS "
            "NOSE AND THE MASS OF HIS HEAD and cannot be seen at all; his one "
            "visible eye looks steadily down and away to the LEFT at the spilled "
            "grain and exits the picture through the LEFT EDGE, so his pupils are "
            "nowhere near the lens. His face is doing arithmetic, not devotion: the "
            "brows drawn, the mouth pressed, one big blunt hand half-raised toward "
            "the bins as if counting them. His deep rust-brown tunic, dark umber "
            "shoulder mantle and dark olive waist sash are all clearly readable, and "
            "his thick black hair, iron grey at the temple, is lit along the top. "
            "BEHIND HIM, sharp enough to read: THREE squat plastered mud-brick grain "
            "bins standing separated and individually countable across the yard, "
            "three and no more, each with its low square drawing door near the "
            "ground. EVERY ONE OF THOSE THREE DOORWAYS IS SIMPLY AN OPEN DARK SQUARE "
            "HOLE IN THE MUD BRICK WITH NOTHING IN IT — there is no wooden door, no "
            "planked or boarded door, no cross-batten, no frame, no hinge, no iron "
            "band and no handle anywhere in this picture. From the nearest opening a slope of barley has spilled out onto the "
            "packed earth and lies heaped against the wall with reed baskets sunk in "
            "it, plainly more grain than the bins can hold."
        ),
    },
    # ============ j3 — Luke 12:18, the parable's hinge (RED) ==================
    {
        "id": "v2-r034-b05", "out": "s05-pull-down-my-barns.jpeg",
        "seg": "j3", "window": "14.770-19.480", "wide": True, "jesus": False,
        "locks": _DAY + ["GRANARY-YARD"], "char_refs": _MAN,
        "narration": "This will I do: I will pull down my barns, and build greater;",
        "must_show": "Farm workers breaking down the wall of one of the old mud-brick grain bins with mattocks while the landowner stands back watching, a slab of the plastered wall falling outward in a burst of pale dust.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_MODERN_FARM + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard early-afternoon sun from the upper "
            "RIGHT throwing crisp shadows across the yard and blazing in the hanging "
            "dust, fast shutter, fine film grain. THE CAMERA STANDS BEHIND AND TO "
            "THE LEFT OF THE LANDOWNER AND SHOOTS PAST HIM into the work: he is in "
            "the near LEFT foreground seen in three-quarter FROM BEHIND, only the "
            "back and side of his head, his thick greying black hair, his dark umber "
            "mantle and his rust-brown sleeve in frame, his face turned away toward "
            "the bin and NOT visible to the camera. NOT ONE FACE IS TURNED TOWARD "
            "THE LENS. In the middle distance TWO farm workers in dark hitched "
            "tunics are seen from the side, one with a mattock swung back above his "
            "own shoulder and one crouched levering at the footing, both of them "
            "clearly working ON the mud-brick bin and striking INTO it, never toward "
            "each other and never toward the camera. A slab of plastered mud brick "
            "is breaking away from the bin wall and falling OUTWARD toward the "
            "middle of the yard in a burst of pale tan dust, with broken brick and "
            "crumbled plaster already piled at the foot. THIS IS A WIDE FULL-LENGTH "
            "SCENE: the camera is far enough back that both workers and the "
            "landowner stand head to sandals with the whole bin, the yard wall and "
            "the empty bleached hills beyond them."
        ),
    },
    {
        "id": "v2-r034-b06", "out": "s06-there-will-i-bestow.jpeg",
        "seg": "j3", "window": "19.480-24.304", "wide": True, "jesus": False,
        "locks": _DAY + ["GRANARY-YARD"], "char_refs": _MAN,
        "narration": "and there will I bestow all my fruits and my goods.",
        "must_show": "The new, far larger grain store going up in the same yard: its mud-brick walls already at head height and rough hewn timber roof beams being lifted and set across them by workers, with the landowner standing below directing.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_MODERN_FARM + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, bright clear afternoon light from the upper "
            "LEFT, fine film grain, deep focus. THE CAMERA STANDS WELL BACK AND "
            "BEHIND THE LANDOWNER, LOW, AND SHOOTS UP PAST HIM at the rising "
            "building: he stands in the near RIGHT foreground seen ENTIRELY FROM "
            "BEHIND, a dark umber mantle and rust-brown tunic with his thick greying "
            "black hair curling at the nape, one arm raised no higher than his own "
            "shoulder pointing up at the beams, his face invisible to the camera. "
            "NOT ONE FACE IS TURNED TOWARD THE LENS. THE SUBJECT IS THE NEW STORE: a "
            "single large rectangular building of sun-dried mud brick and undressed "
            "field stone, plastered pale tan, its walls already above the height of a "
            "man, plainly two or three times the size of the small round bins that "
            "still stand beyond it. THREE rough hewn timber beams, bark still on "
            "parts of them, lie across the wall heads and a fourth is being walked up "
            "a ramp of packed earth on the shoulders of TWO workers in dark hitched "
            "tunics, both seen from the side, straining under the weight with the "
            "beam clearly resting ON their shoulders. Coils of twisted flax cord, "
            "reed baskets of wet mud plaster and a heap of fresh mud bricks drying in "
            "rows stand on the swept earth in the foreground."
        ),
    },
    # ============ n3 / n4 — the narrator restates the plan ====================
    {
        "id": "v2-r034-b07", "out": "s07-what-should-i-do.jpeg",
        "seg": "n3", "window": "24.304-27.114", "wide": False, "jesus": False,
        "locks": _DAY + ["GRANARY-YARD"], "char_refs": _MAN,
        "narration": "So he thought to himself: What should I do?",
        "must_show": "The landowner standing alone among the spilled grain in the yard, one hand at his beard, thinking, with nobody else in the picture.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_MODERN_FARM + _NO_CREAM
        + "no other person, shoulder, arm, head or back anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 105mm lens, warm low side light from the RIGHT, shallow "
            "depth of field so the yard behind falls soft, fine film grain. THIS IS A "
            "STRICT SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS RIGHT: the "
            "landowner is alone in the frame from the chest up, turned fully to the "
            "RIGHT, so the viewer sees ONE cheek, ONE eye and ONE ear, and THE FAR "
            "CHEEK AND THE FAR EYE ARE COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS "
            "NOSE AND THE MASS OF HIS HEAD. His one visible eye is lowered and looks "
            "down and away to the RIGHT at nothing in particular, exiting the frame "
            "through the RIGHT EDGE. His big blunt fingers are drawn slowly through "
            "the iron-grey and black beard at his jaw; the brows are pulled together "
            "and the mouth is slightly open in thought. THE CLOTH ACROSS HIS "
            "SHOULDER FILLS THE BOTTOM THIRD OF THE FRAME FROM THE LEFT EDGE TO THE "
            "RIGHT EDGE: his own dark umber wool mantle and the deep rust-brown "
            "tunic beneath it run as ONE CONTINUOUS MASS OF CLOTH across the whole "
            "bottom of the picture and off both sides, leaving no empty corner "
            "anywhere. That cloth is plainly HAND-WOVEN: a visible slightly "
            "irregular over-and-under grid of warp and weft threads on a flat matte "
            "surface, never knitted, ribbed, cabled, fleeced or napped. Behind his "
            "head, thrown far out of focus, the pale tan of a plastered bin wall and "
            "the gold of spilled grain."
        ),
    },
    {
        "id": "v2-r034-b08", "out": "s08-tear-down-build-bigger.jpeg",
        "seg": "n3", "window": "27.114-31.345", "wide": True, "jesus": False,
        "locks": _DAY + ["GRANARY-YARD"], "char_refs": _MAN,
        "narration": "I know — I will tear down my barns and build bigger ones.",
        "must_show": "One of the old mud-brick grain bins now half demolished, its dome gone and its wall broken down to waist height, with the rubble of broken brick and plaster spread across the yard and workers carrying it away in baskets.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_MODERN_FARM + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, flat bright high sun, pale dust hanging over "
            "everything and softening the far side of the yard, fine film grain. THE "
            "CAMERA STANDS BACK ACROSS THE YARD AND SLIGHTLY ABOVE, SHOOTING DOWN "
            "AND PAST THE BACKS of the two workers nearest it: they are in the lower "
            "LEFT of the frame seen ENTIRELY FROM BEHIND, dark hitched tunics and "
            "bent backs, one straightening with a loaded reed basket held against his "
            "hip, walking AWAY from the camera into the picture. NOT ONE FACE IS "
            "TURNED TOWARD THE LENS. THE SUBJECT IS THE RUIN: the old round bin "
            "stands open to the sky with its packed-earth dome gone entirely and its "
            "plastered mud-brick wall broken down to about waist height on the near "
            "side, the broken edge ragged and crumbling, its dark empty inside "
            "visible over the top. Rubble of broken mud brick, snapped brushwood "
            "roofing poles and crumbled pale plaster lies spread in a fan across the "
            "packed earth. Beyond it the walls of the new, far larger store rise "
            "plainly higher and longer. THIS IS A WIDE FULL-LENGTH SCENE with the "
            "workers, both bins and the bare bleached hills beyond all in one frame."
        ),
    },
    {
        "id": "v2-r034-b09", "out": "s09-store-up-all-my-grain.jpeg",
        "seg": "n4", "window": "31.345-35.093", "wide": False, "jesus": False,
        "locks": ["GRANARY-BARN", "GRANARY-IN", "LANDOWNER", "WORKERS"], "char_refs": _MAN,
        "narration": "There I will store up all my grain and all my goods.",
        "must_show": "The inside of the finished new grain store, heaped high with barley running back up to the hewn roof beams, one hard shaft of daylight falling through the roof hatch onto the grain with dust turning in it.",
        "must_not_show": _NO_HALO + _NO_DEATH + _NO_MODERN_FARM + _NO_CREAM
        + "no person, figure, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 28mm lens, taken from just inside the low drawing door "
            "looking into the dim interior, fine film grain, deep focus, no person in "
            "the picture at all. THE ONLY LIGHT IS ONE HARD SHAFT OF WHITE DAYLIGHT "
            "falling steeply from the open square filling hatch in the roof at the "
            "upper RIGHT down onto the grain, cutting a bright slanted lozenge across "
            "the heap while the corners of the store fall away into soft warm brown "
            "darkness. Fine dust and chaff turn slowly through the beam. THE HEAP "
            "FILLS THE PICTURE: clean golden barley running back and UP toward the "
            "rear wall until it almost touches the three rough hewn timber beams "
            "overhead, its surface poured into soft ridges and cones, single grains "
            "catching the light along the top edge. At the foot of the heap stand "
            "four hand-woven reed baskets and two coarse dark goat-hair sacks, "
            "filled and slumped, with a hand-hewn wooden scoop pushed into the grain "
            "beside them. The mud-plastered walls are pale tan and bare."
        ),
    },
    # ============ j4 — Luke 12:19 (RED) ======================================
    {
        "id": "v2-r034-b10", "out": "s10-i-will-say-to-my-soul.jpeg",
        "seg": "j4", "window": "35.093-37.743", "wide": False, "jesus": False,
        "locks": ["GRANARY-BARN", "GRANARY-IN", "LANDOWNER"], "char_refs": _MAN,
        "narration": "And I will say to my soul, Soul,",
        "must_show": "The landowner standing inside his full new grain store looking up at the heaped grain, alone, with the daylight from the roof hatch falling in front of him onto his face and chest.",
        "must_not_show": _NO_HALO + _NO_DEATH + _NO_MODERN_FARM + _NO_CREAM
        + "no other person, shoulder, arm, head or back anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, fine film grain. THE LIGHT IS PLACED SO NO "
            "HEAD CAN BE RINGED WITH LIGHT: the one shaft of daylight from the roof hatch comes "
            "down IN FRONT OF the man, between him and the camera, striking the "
            "grain heap and bouncing warm light UPWARD AND FORWARD onto the front "
            "planes of his face, the underside of his brow, his nose and his beard, "
            "while the top and back of his head, his hair and his shoulders stay "
            "UNLIT AND DARK and merge into the brown darkness of the store behind "
            "him. NO LIGHT SOURCE OF ANY KIND STANDS BEHIND, ABOVE OR BEYOND HIS "
            "HEAD and there is no bright rim, edge or outline anywhere around him. "
            "THIS IS A STRICT SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS "
            "LEFT: he stands three-quarter length at the LEFT of the frame turned "
            "fully to the RIGHT, showing ONE cheek, ONE eye and ONE ear, THE FAR "
            "CHEEK AND FAR EYE COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND "
            "THE MASS OF HIS HEAD. His one visible eye is raised, looking up and "
            "away to the RIGHT along the slope of the grain and out through the "
            "RIGHT EDGE of the picture. His chin is lifted and his mouth is parted "
            "in quiet satisfaction. His rust-brown tunic and dark umber mantle are "
            "clearly readable; the great golden heap fills the right two thirds of "
            "the frame behind and above him."
        ),
    },
    {
        "id": "v2-r034-b11", "out": "s11-much-goods-laid-up.jpeg",
        "seg": "j4", "window": "37.743-40.643", "wide": False, "jesus": False,
        "locks": ["GRANARY-BARN", "GRANARY-IN", "LANDOWNER"], "char_refs": _MAN,
        "narration": "thou hast much goods laid up for many years;",
        "must_show": "A close view of the landowner's big weathered hand lifted out of the heaped barley with the grain pouring back down between his fingers in a stream.",
        "must_not_show": _NO_HALO + _NO_DEATH + _NO_MODERN_FARM + _NO_CREAM
        + "no face and no second person anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, the warm bounced light from the "
            "grain heap coming up from BELOW AND IN FRONT so nothing is backlit, "
            "fast shutter freezing every falling grain, fine film grain, shallow "
            "depth of field. THE FRAME IS FILLED BY ONE ADULT MALE HAND AND THE "
            "GRAIN: a single big blunt-fingered, split-nailed, deeply sun-darkened "
            "olive-brown hand, plainly a heavy working man's hand and not a woman's "
            "or a child's, comes in from the LEFT and is lifted palm-down just above "
            "the heap, with clean golden barley pouring back out of it in a bright "
            "stream between the fingers and rattling onto the mound below. The wrist "
            "and the straight unshaped elbow-length sleeve of the deep rust-brown "
            "tunic show at the left edge, AND THAT SLEEVE IS PLAINLY HAND-WOVEN: a "
            "visible slightly irregular over-and-under grid of warp and weft threads "
            "on a flat matte surface with a plain frayed cut edge at the hem, never "
            "knitted, ribbed, cabled, purled, fleeced, brushed or napped. NO FACE IS "
            "IN THE PICTURE. Behind the hand the heap runs away out of focus into "
            "warm gold and brown, with the dim hewn beams just readable at the top."
        ),
    },
    {
        "id": "v2-r034-b12", "out": "s12-take-thine-ease.jpeg",
        "seg": "j4", "window": "40.643-45.283", "wide": False, "jesus": False,
        "locks": ["COURTYARD", "LANDOWNER"], "char_refs": _MAN,
        "narration": "take thine ease, eat, drink, and be merry.",
        "must_show": "The low supper table in the walled courtyard being laid: hands setting down a fired-clay wine jar beside rounds of barley bread and a bowl of olives, in warm late-afternoon light.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_CREAM
        + "no face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, warm low late-afternoon sun coming in over "
            "the courtyard wall from the LEFT and lying in a long gold band across "
            "the table, fine film grain, shallow depth of field. THE CAMERA IS LOW, "
            "AT THE HEIGHT OF THE TABLE TOP, AND SHOOTS ACROSS IT: the adzed timber "
            "slab runs from the near LEFT corner away to the RIGHT, filling the "
            "lower half of the frame, its grain and adze marks raking in the light. "
            "TWO adult hands and forearms only, in the straight unshaped sleeves of "
            "a dark tunic, come down into the frame from the upper RIGHT and are "
            "setting a round-bellied fired-clay wine jar onto the boards; NO HEAD "
            "AND NO FACE IS IN THE PICTURE AT ALL. Already on the table, laid out "
            "separated and individually countable: THREE flat rounds of dark barley "
            "bread, ONE shallow fired-clay bowl of black olives, and TWO plain "
            "fired-clay cups standing upright — three loaves, one bowl and two cups "
            "is the total number of vessels and loaves visible anywhere in this "
            "picture. Behind, thrown soft, the pale mud-plastered courtyard wall, "
            "the dark cloth panel over the low doorway and the dusty vine on its "
            "poles."
        ),
    },
    # ============ n5 / n6 — the man at his ease ==============================
    {
        "id": "v2-r034-b13", "out": "s13-plenty-saved-up.jpeg",
        "seg": "n5", "window": "45.283-50.003", "wide": True, "jesus": False,
        "locks": ["COURTYARD", "LANDOWNER", "JUDEAN-LAND"], "char_refs": _MAN,
        "narration": "And then I will say to myself: You have plenty saved up for years to come.",
        "must_show": "The landowner reclining alone on the woollen mats beside his laid supper table in the walled courtyard in the last warm light of the evening, entirely at his ease, with nobody else there.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_CREAM
        + "no other person, shoulder, arm, head or back anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, the last warm gold light of evening coming "
            "in almost level over the wall from the LEFT and throwing a long soft "
            "shadow of the table across the flagstones, fine film grain. THE CAMERA "
            "STANDS BEHIND AND ABOVE HIM AND SHOOTS DOWN PAST HIS BACK: he is seen "
            "from BEHIND AND SLIGHTLY TO THE SIDE, reclining on his left elbow on "
            "the folded woollen mats in the near lower LEFT of the frame with his "
            "legs stretched out toward the table, his dark umber mantle spread loose "
            "across his back and his thick black hair, iron grey at the temples, "
            "curling at the nape of his neck. HIS FACE IS TURNED AWAY toward the "
            "table and is NOT visible; NOT ONE FACE IS TURNED TOWARD THE LENS. One "
            "big blunt hand rests slack on his own thigh. THIS IS A WIDE "
            "FULL-LENGTH SCENE: the camera is far enough back that the whole man, "
            "the whole low table with its bread, olives, wine jar and two cups, the "
            "vine on its poles and two full walls of the courtyard are in one frame "
            "together. He is entirely alone in it. Beyond the wall, the empty "
            "bleached harvest country and a hard clear sky going warm at the edge."
        ),
    },
    {
        "id": "v2-r034-b14", "out": "s14-eat-drink-enjoy.jpeg",
        "seg": "n5", "window": "50.003-52.991", "wide": False, "jesus": False,
        "locks": ["COURTYARD", "LANDOWNER"], "char_refs": _MAN,
        "narration": "Relax. Eat, drink, and enjoy your life.",
        "must_show": "A close view of dark wine being poured from the tilted fired-clay jar into a plain fired-clay cup on the low table, the stream caught in the last gold light.",
        "must_not_show": _NO_HALO + _NO_DEATH + _NO_NIGHT + _NO_CREAM
        + "no face anywhere in this frame, and no blood; " + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, warm low gold light raking from the "
            "LEFT and lighting the pour from the front, fast shutter, fine film "
            "grain, very shallow depth of field. THE FRAME IS FILLED BY THE POUR: a "
            "round-bellied fired-clay wine jar, held and tilted by ONE big "
            "blunt-fingered sun-darkened adult male hand entering from the upper "
            "LEFT, sends a single dark red stream down into a plain fired-clay cup "
            "standing on the adzed timber table top in the lower RIGHT, the wine "
            "already halfway up the cup and turning with the light. NO HEAD AND NO "
            "FACE IS IN THE PICTURE. The straight unshaped sleeve of the deep "
            "rust-brown tunic shows at the upper left edge, PLAINLY HAND-WOVEN with "
            "a visible slightly irregular over-and-under grid of warp and weft "
            "threads on a flat matte surface, never knitted, ribbed or fleeced. "
            "Behind, thrown far out of focus into warm gold and shadow, the bread "
            "and the olive bowl on the table and the pale courtyard wall."
        ),
    },
    {
        "id": "v2-r034-b15", "out": "s15-he-had-it-figured-out.jpeg",
        "seg": "n6", "window": "52.991-56.961", "wide": False, "jesus": False,
        "locks": ["COURTYARD", "LANDOWNER"], "char_refs": _MAN,
        "narration": "He had it all figured out. Every single plan was about himself —",
        "must_show": "The landowner sitting back on the mats beside the table with the cup resting in his hand, wholly content, alone in the courtyard as the light goes.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_CREAM
        + "no other person, shoulder, arm, head or back anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, the last low gold light of evening coming "
            "level from the RIGHT and modelling the face from the front, fine film "
            "grain, shallow depth of field. THIS IS A STRICT SIDE-ON PROFILE AND THE "
            "CAMERA SITS EXACTLY ON HIS RIGHT: the landowner is alone in the frame "
            "from the waist up, turned fully to the RIGHT, showing ONE cheek, ONE "
            "eye and ONE ear, and THE FAR CHEEK AND THE FAR EYE ARE COMPLETELY "
            "HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF HIS HEAD. His one "
            "visible eye is half-lidded and looks out and down to the RIGHT across "
            "his own courtyard, exiting the picture through the RIGHT EDGE. His head "
            "is tipped comfortably back, his mouth relaxed into a small private "
            "smile, the fired-clay cup held loose and low against his chest in one "
            "big blunt hand. His deep rust-brown tunic, dark umber mantle and dark "
            "olive sash are clearly readable and his thick black hair, iron grey at "
            "the temple, is lit along the front edge only. Behind him, thrown far "
            "out of focus, the pale mud-plastered wall and the dark cloth doorway of "
            "the courtyard, both going warm and dim."
        ),
    },
    {
        "id": "v2-r034-b16", "out": "s16-his-barns-his-goods.jpeg",
        "seg": "n6", "window": "56.961-60.045", "wide": True, "jesus": False,
        "locks": _DAY + ["GRANARY-YARD", "COURTYARD"], "char_refs": _MAN,
        "narration": "his barns, his goods, his own comfort.",
        "must_show": "The whole farm compound seen from a distance at dusk — the great new grain store, the remaining bins, the walled courtyard — with the landowner a single small solitary figure in it and no other living soul anywhere.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_GREEN + _NO_MODERN_FARM + _NO_CREAM
        + "no other person anywhere in this frame, at any distance or focus; " + _GAZE,
        "scene": (
            "One photograph, 24mm lens, high wide vantage, the last cold-gold light "
            "of a dry evening lying flat across the country from the LEFT with long "
            "blue shadows reaching out from every wall, fine film grain, deep focus. "
            "THE CAMERA STANDS FAR BACK AND WELL ABOVE THE COMPOUND ON THE NEXT "
            "TERRACE AND LOOKS DOWN AND ACROSS IT, so every human figure is small, "
            "seen from above and behind, and NO FACE IS READABLE OR TURNED TOWARD "
            "THE LENS ANYWHERE. Laid out below: the long new mud-brick grain store "
            "with its flat packed-earth roof, TWO surviving round bins beside it, the "
            "rubble fan of the demolished third, the swept yard with its dry-stone "
            "wall, and the small walled courtyard with the vine and the low table "
            "still standing in it. ONE SINGLE HUMAN FIGURE IS IN THE PICTURE AND NO "
            "OTHER: the landowner, tiny, dark umber and rust against the pale earth, "
            "crossing his own yard alone toward the door of the new store with his "
            "back to the camera. The reaped terraces run away empty in every "
            "direction to bare limestone hills and a clear dimming sky. Nothing "
            "moves anywhere else."
        ),
    },
    # ============ n7 — the night comes ======================================
    {
        "id": "v2-r034-b17", "out": "s17-one-thing-he-never-planned.jpeg",
        "seg": "n7", "window": "60.045-62.545", "wide": True, "jesus": False,
        "locks": ["GRANARY-BARN", "JUDEAN-LAND", "NIGHT-LAMPLIGHT", "GRANARY-YARD"],
        "narration": "But there was one thing he had never planned for.",
        "must_show": "The farm compound at full night — the great new grain store and the round bins standing as black shapes against a deep blue-black sky full of stars, everything still, with no person in the picture.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_MODERN_FARM + _NO_MODERN_LAMP + _NO_CREAM
        + "no sun, sunrise, sunset, dawn, dusk band, orange or pink horizon or warm glow along any skyline; "
        + "no person, figure, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 24mm lens, long exposure on a tripod, fine film grain, "
            "deep focus, NO PERSON IN THE PICTURE AT ALL. IT IS GENUINELY NIGHT AND "
            "THE DARKNESS IS REAL: the sky is deep blue-black and thick with hard "
            "cold stars from edge to edge, the land reads as pure shape and "
            "silhouette, and away from the one small light the picture falls to near "
            "black and loses all detail, exactly as it does at night. THE CAMERA "
            "STANDS OUT IN THE DARK YARD LOOKING ACROSS IT at the buildings: the "
            "long flat-roofed mass of the new mud-brick grain store fills the middle "
            "of the frame as a black block against the stars, with TWO squat round "
            "bins beside it as two smaller black domes, and the low dry-stone wall "
            "running across the foreground as a broken black line. ONE SINGLE SMALL "
            "SOFT YELLOW-ORANGE FLAME is just visible far off and LOW DOWN at ground "
            "level in the black doorway of the courtyard — a bare fibre wick standing "
            "in a shallow fired-clay oil lamp set on the ground, nothing more, "
            "throwing a small warm patch onto the earth immediately around itself and "
            "reaching nothing else. It is far below and away from anything that could "
            "be a head. The bleached hills are a slightly darker black along the "
            "bottom of the sky."
        ),
    },
    {
        "id": "v2-r034-b18", "out": "s18-that-very-night.jpeg",
        "seg": "n7", "window": "62.545-65.382", "wide": False, "jesus": False,
        "locks": _NIGHT + ["GRANARY-YARD"], "char_refs": _MAN,
        "narration": "And that very night, God spoke to him.",
        "must_show": "The landowner standing alone in the dark doorway of his new grain store at night with one small clay oil lamp set low on the ground in front of him, having stopped and turned his head as if he has heard something.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_MODERN_FARM + _NO_MODERN_LAMP + _NO_CREAM
        + "no sunrise, sunset, dawn or warm glow along any skyline; "
        + "no other person, shoulder, arm, head or back anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, fine film grain. IT IS GENUINELY NIGHT: the "
            "sky behind is deep blue-black with stars, and away from the one flame "
            "the picture falls to near black. THE FLAME IS PLACED SO NO HEAD CAN BE "
            "RINGED WITH LIGHT: a single shallow fired-clay oil lamp with ONE small soft "
            "yellow-orange flame on a bare fibre wick stands ON THE GROUND at the "
            "man's feet, LOW AND IN FRONT OF HIM AND NEARER THE CAMERA THAN HIS "
            "HEAD, so its light travels only UPWARD AND FORWARD onto the front of "
            "his robe, his hands, the underside of his jaw, his cheekbones and his "
            "brow, while the crown and the back of his head, his hair and his "
            "shoulders stay UNLIT AND DARK and merge into the black doorway behind "
            "him. NO LIGHT SOURCE OF ANY KIND STANDS BEHIND, ABOVE OR BEYOND HIS "
            "HEAD, and there is no bright rim, edge, outline, ring or corona around "
            "any part of him. THE CAMERA SITS ON HIS LEFT AND SLIGHTLY BELOW: he "
            "stands three-quarter length in the middle of the frame turned mostly "
            "AWAY toward the black interior, his head checked and half-turned back "
            "over his own shoulder so the viewer sees the near cheek in profile "
            "only, THE FAR CHEEK AND FAR EYE HIDDEN BEHIND THE MASS OF HIS HEAD, and "
            "his one visible eye looking off past the camera into the dark to the "
            "LEFT and out through the LEFT EDGE. His rust-brown tunic and dark umber "
            "mantle read warm in the lamplight. Nobody else is there."
        ),
    },
    # ============ j1 — Luke 12:20 (RED). NO DEATH IS PAINTED. ================
    {
        "id": "v2-r034-b19", "out": "s19-thou-fool.jpeg",
        "seg": "j1", "window": "65.382-69.022", "wide": False, "jesus": False,
        "locks": _NIGHT, "char_refs": _MAN,
        "narration": "Thou fool, this night thy soul shall be required of thee:",
        "must_show": "The landowner's face by the low lamplight, stopped and stricken, listening — a living man hearing something, and nothing else.",
        "must_not_show": _NO_HALO + _NO_DEATH + _NO_MODERN_LAMP + _NO_CREAM
        + "no other person, shoulder, arm, head or back anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, fine film grain, shallow depth of field. IT "
            "IS GENUINELY NIGHT and everything beyond the man falls away to near "
            "black. THE FLAME IS PLACED SO NO HEAD CAN BE RINGED WITH LIGHT: the "
            "single small "
            "soft yellow-orange flame of a shallow fired-clay oil lamp stands LOW ON "
            "THE GROUND WELL BELOW HIS CHIN AND NEARER THE CAMERA THAN HIS HEAD, its "
            "light travelling only UPWARD AND FORWARD to catch the underside of his "
            "brow, the ridge of his nose, one cheekbone, his lower lip and the front "
            "of his beard, while the crown and back of his head, his hair and his "
            "shoulders stay UNLIT AND DARK and merge completely into the night. NO "
            "LIGHT SOURCE STANDS BEHIND, ABOVE OR BEYOND HIS HEAD and there is no "
            "rim, outline, ring or corona anywhere around him. THIS IS A "
            "STRICT SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS RIGHT: head "
            "and shoulders only, turned fully to the RIGHT, showing ONE cheek, ONE "
            "eye and ONE ear, THE FAR CHEEK AND FAR EYE COMPLETELY HIDDEN BEHIND THE "
            "BRIDGE OF HIS NOSE AND THE MASS OF HIS HEAD. His one visible eye is "
            "wide and fixed on nothing, looking level and away to the RIGHT and out "
            "through the RIGHT EDGE; his lips are parted, the breath stopped. HE IS "
            "A LIVING, HEALTHY, UPRIGHT MAN — awake, alert and unhurt, with no "
            "wound, blood, pallor, sweat, collapse or sign of illness. THE DARK "
            "CLOTH OF HIS OWN MANTLE FILLS THE BOTTOM THIRD OF THE FRAME FROM THE "
            "LEFT EDGE TO THE RIGHT EDGE as one continuous mass, leaving no empty "
            "corner. Everything behind him is plain black night."
        ),
    },
    {
        "id": "v2-r034-b20", "out": "s20-required-of-thee.jpeg",
        "seg": "j1", "window": "69.022-71.222", "wide": False, "jesus": False,
        "locks": _NIGHT[:2] + ["NIGHT-LAMPLIGHT", "GRANARY-YARD"],
        "narration": "then whose shall those things be,",
        "must_show": "The small clay oil lamp burning alone on the packed earth of the yard at night with the black mass of the great grain store rising behind it, and nobody in the picture.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_MODERN_FARM + _NO_MODERN_LAMP + _NO_CREAM
        + "no person, figure, hand, arm, shoulder, face or shadow of a person anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, low camera set on the ground itself, fine "
            "film grain, shallow depth of field, NO PERSON IN THE PICTURE AT ALL. IT "
            "IS GENUINELY NIGHT: the sky is deep blue-black with stars and everything "
            "outside the small pool of flame falls to near black. THE SUBJECT IS THE "
            "LAMP: ONE shallow closed oval of plain fired terracotta, small enough to "
            "sit in a cupped palm, with a round filling hole in its top and a pinched "
            "spout at one end, standing alone on the packed pale earth in the lower "
            "LEFT of the frame, ONE single small soft yellow-orange flame on a bare "
            "fibre wick standing at the spout and smoking faintly. Its light reaches "
            "only a hand's breadth of ground around it, picking out single spilled "
            "grains of barley and the edge of a hand-woven reed basket. BEHIND AND "
            "ABOVE, unlit, the long mud-brick wall of the new grain store rises as a "
            "flat black mass filling the right two thirds of the picture and cutting "
            "a hard straight edge against the star field. Nothing else is visible."
        ),
    },
    {
        "id": "v2-r034-b21", "out": "s21-which-thou-hast-provided.jpeg",
        "seg": "j1", "window": "71.222-74.527", "wide": False, "jesus": False,
        "locks": ["GRANARY-BARN", "GRANARY-IN", "NIGHT-LAMPLIGHT"],
        "narration": "which thou hast provided?",
        "must_show": "The great heap of stored grain inside the new barn at night, lit only by one small clay lamp set down on the grain itself, the rest of the store lost in blackness.",
        "must_not_show": _NO_HALO + _NO_DEATH + _NO_MODERN_FARM + _NO_MODERN_LAMP + _NO_CREAM
        + "no person, figure, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, fine film grain, NO PERSON IN THE PICTURE AT "
            "ALL. IT IS NIGHT INSIDE A WINDOWLESS STORE AND THE DARKNESS IS TOTAL "
            "EXCEPT FOR ONE FLAME: a shallow fired-clay oil lamp with ONE small soft "
            "yellow-orange flame on a bare fibre wick has been set down directly ON "
            "the grain in the lower middle of the frame, and it is the only light in "
            "the world of this picture. THE CAMERA IS LOW AND CLOSE, at the level of "
            "the lamp, looking up the slope of the heap: the light rakes ACROSS the "
            "barley immediately around the lamp, throwing every single grain into "
            "hard little shadows and turning that patch a deep warm gold, then falls "
            "away fast up the slope until the top of the heap and the hewn beams "
            "above it are lost entirely in flat black. No wall, no corner and no roof "
            "is visible. The picture is mostly darkness with one small warm island of "
            "grain in it, and there is nobody there to own it."
        ),
    },
    # ============ n8 — the morning after. Still no death painted. ============
    {
        "id": "v2-r034-b22", "out": "s22-that-night-his-life-was-over.jpeg",
        "seg": "n8", "window": "74.527-78.597", "wide": True, "jesus": False,
        "locks": ["GRANARY-BARN", "JUDEAN-LAND", "GRANARY-YARD"],
        "narration": "That night, his life was over. And everything he had piled up,",
        "must_show": "The same yard at grey first light, completely empty of people: the door of the new grain store standing open, the little clay lamp burnt out and cold on the threshold, chaff blowing across the packed earth.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_GREEN + _NO_MODERN_FARM + _NO_CREAM
        + "no person, figure, hand, arm, shoulder, face or body anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 28mm lens, the flat colourless grey-blue light of first "
            "dawn before the sun has risen, no sun disc in the frame, everything even "
            "and shadowless and cold, fine film grain, deep focus. THERE IS NO PERSON "
            "IN THIS PICTURE AT ALL AND THAT IS THE POINT OF IT. THE CAMERA STANDS "
            "BACK IN THE MIDDLE OF THE EMPTY YARD looking at the front of the new "
            "mud-brick grain store: its low square drawing door STANDS OPEN as a bare dark "
            "square hole in the mud brick, the single flat limestone slab that normally "
            "closes it heaved aside and leaning against the wall beside it. There is "
            "no wooden door, no planked or boarded door, no cross-batten, no frame, "
            "no hinge, no iron band and no handle anywhere in this picture, and "
            "beyond the opening there is only flat unreadable darkness. ON THE "
            "THRESHOLD STONE, small and exactly centred in the doorway, sits the "
            "shallow fired-clay oil lamp — BURNT OUT AND COLD, no flame, no light, no "
            "smoke, just a black charred stub of wick in the spout. Loose chaff and "
            "straw blow in a low drift across the packed pale earth of the yard from "
            "the LEFT. THIS IS A WIDE FULL-LENGTH SCENE with the whole face of the "
            "store, the swept yard, the dry-stone wall and the bleached hills beyond "
            "all in one frame. There are no backs, no shoulders and no faces anywhere in this frame because nobody is in it; nothing living is anywhere in the picture."
        ),
    },
    {
        "id": "v2-r034-b23", "out": "s23-the-barns-the-grain.jpeg",
        "seg": "n8", "window": "78.597-81.157", "wide": False, "jesus": False,
        "locks": ["GRANARY-BARN", "GRANARY-IN"],
        "narration": "the barns, the grain, all of it,",
        "must_show": "The inside of the full grain store at first light, the great heap of barley exactly as it was left, cold and grey and untouched, with nobody there.",
        "must_not_show": _NO_HALO + _NO_DEATH + _NO_MODERN_FARM + _NO_CREAM
        + "no person, figure, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, fine film grain, deep focus, NO PERSON IN "
            "THE PICTURE AT ALL. The light is completely different from the hot "
            "shaft of the day before: cold flat colourless GREY-BLUE first light "
            "leaking in through the open square roof hatch and the open low door, "
            "with no sun in it, no warmth in it and almost no shadow, so the whole "
            "interior reads dim, even and lifeless. THE CAMERA STANDS INSIDE AT "
            "CHEST HEIGHT looking along the length of the store: the great heap of "
            "barley runs back and up toward the rough hewn timber beams exactly as "
            "it was left, its poured ridges undisturbed and unmarked, the single "
            "hand-hewn wooden scoop still standing pushed into it where it was "
            "dropped. Four hand-woven reed baskets and two coarse dark goat-hair "
            "sacks stand filled at the foot of the heap. Fine dust hangs almost "
            "motionless. The mud-plastered walls are pale grey tan and bare. Nothing "
            "in the picture has moved and nobody is in it."
        ),
    },
    {
        "id": "v2-r034-b24", "out": "s24-pass-to-someone-else.jpeg",
        "seg": "n8", "window": "81.157-83.946", "wide": False, "jesus": False,
        "locks": ["GRANARY-BARN", "GRANARY-IN", "WORKERS"],
        "narration": "would simply pass to someone else.",
        "must_show": "Other men's hands filling reed baskets from the heap and carrying them out through the low door of the store, taking the grain away — and the landowner is not in the picture at all.",
        "must_not_show": _NO_HALO + _NO_DEATH + _NO_MODERN_FARM + _NO_CREAM
        + "no man of about fifty-five, no heavy grey-streaked black beard, no deep rust-brown ankle-length tunic and no dark umber mantle anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, cold flat grey morning light from the open "
            "door, fine film grain. THE CAMERA STANDS DEEP INSIDE THE STORE BEHIND "
            "THE MEN AND SHOOTS PAST THEM TOWARD THE DOOR, so every figure is seen "
            "ENTIRELY FROM BEHIND, walking AWAY from the camera into the pale "
            "rectangle of the doorway, and NOT ONE FACE IS TURNED TOWARD THE LENS "
            "and no face is visible anywhere. THREE farm workers in dark hitched "
            "knee-length tunics — charcoal, dark indigo and dark olive — are lifting "
            "and carrying the grain out: the nearest is crouched with both hands "
            "sunk in the heap filling a hand-woven reed basket, the second is "
            "straightening with a full basket braced on his shoulder, and the third "
            "is already stooping out through the low door with his load, half in "
            "silhouette against the grey light. Three men is the total number of "
            "people visible anywhere in this picture. The heap behind them is "
            "visibly cut into and dragged down on one side where they have been "
            "working. Nothing about the men is grand; they are simply taking it."
        ),
    },
    # ============ n9 — the reckoning, NOT painted as an afterlife =============
    {
        "id": "v2-r034-b25", "out": "s25-planned-for-everything.jpeg",
        "seg": "n9", "window": "83.946-87.586", "wide": True, "jesus": False,
        "locks": ["COURTYARD", "JUDEAN-LAND"],
        "narration": "He had planned for everything except the one thing that was certain:",
        "must_show": "The walled courtyard in the cold morning, the supper table still laid exactly as it was left the evening before, the mats still spread, and nobody there.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_GREEN + _NO_CREAM
        + "no person, figure, hand, arm, shoulder, face or body anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 28mm lens, cold flat colourless grey-blue morning light "
            "with no sun disc and almost no shadow, fine film grain, deep focus. "
            "THERE IS NO PERSON IN THIS PICTURE AT ALL. THE CAMERA STANDS IN THE "
            "LOW DOORWAY OF THE COURTYARD LOOKING IN AND SLIGHTLY DOWN across the "
            "whole small enclosure. The low adzed timber table stands exactly where "
            "it was, still laid from the evening before: the three flat rounds of "
            "barley bread now dry and curling at the edges, the shallow clay bowl of "
            "olives, the wine jar, and the TWO fired-clay cups — one still standing "
            "upright and one lying on its side where it was set down, with a dark "
            "dried stain of spilled wine across the boards beneath it. The folded "
            "woollen mats and the dark bolster are still spread on the flagstones "
            "beside the table with the shape of a body still pressed into them, and "
            "no body in them. THIS IS A WIDE FULL-LENGTH SCENE: the whole table, "
            "both mats, the vine on its poles, three walls of the courtyard and the "
            "open cold sky above are all in one frame. Chaff and dust have blown in "
            "across the flagstones in the night. There are no backs, no shoulders and "
            "no faces anywhere in this frame because nobody is in it."
        ),
    },
    {
        "id": "v2-r034-b26", "out": "s26-stand-before-god.jpeg",
        "seg": "n9", "window": "87.586-90.904", "wide": True, "jesus": False,
        "locks": ["JUDEAN-LAND", "THRESHING"],
        "narration": "that one day he would stand before God.",
        "must_show": "The bare ridge threshing floor at dawn, swept and empty under a vast open sky, with one line of a man's footprints crossing the drift of chaff and going away out of the frame.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_GREEN + _NO_MODERN_FARM + _NO_CREAM
        + "no person, figure, silhouette, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 24mm lens, camera low and close to the rock, the pale "
            "clear light of early morning coming from the RIGHT with the sun itself "
            "well out of frame, fine film grain, deep focus. THERE IS NO PERSON IN "
            "THIS PICTURE AT ALL and no figure of any kind. THE CAMERA LOOKS ALONG "
            "AND ACROSS the wide flat circle of worn bare bedrock: its surface is "
            "swept and polished pale, ringed by its low kerb of loose unmortared "
            "field stones, and the grain, the sheaves, the baskets and the sacks are "
            "ALL GONE — the floor is completely bare except for a thin drift of pale "
            "chaff and broken straw lying along one side. ACROSS THAT DRIFT RUNS ONE "
            "SINGLE LINE OF BARE-TRODDEN SANDAL PRINTS, pressed into the chaff and "
            "dust, coming from the near foreground and going away from the camera "
            "across the floor and out over the far edge of the ridge, with no "
            "returning line beside it. Beyond the ridge the land drops away into "
            "empty bleached reaped country and bare limestone hills, and above it "
            "the enormous hard clear pale sky fills the whole upper two thirds of "
            "the frame, open and unbroken, with no cloud formation, no shaft of "
            "light and nothing written in it."
        ),
    },
    # ============ n10 / j2 — back to Jesus, Luke 12:21 (RED) =================
    {
        "id": "v2-r034-b27", "out": "s27-jesus-ended-the-story.jpeg",
        "seg": "n10", "window": "90.904-93.993", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TEREBINTH", "CROWD", "JUDEAN-LAND"],
        "narration": "And Jesus ended the story with these words.",
        "must_show": "Jesus under the terebinth again, closer than before, finishing the parable to the listening crowd in the hot afternoon.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, hard afternoon sun from the upper LEFT "
            "broken into dapple by the canopy, fine film grain. THE CAMERA STANDS "
            "BEHIND AND ABOVE THE NEAREST SEATED LISTENERS AND SHOOTS DOWN AND PAST "
            "THEM: two dark heads and a dark shoulder cross the lower LEFT corner of "
            "the frame, seen ENTIRELY FROM BEHIND and thrown out of focus, and NOT "
            "ONE FACE IS TURNED TOWARD THE LENS. Jesus is in the middle distance a "
            "little RIGHT of centre, seen three-quarter FROM BEHIND AND TO THE SIDE, "
            "sitting on the low limestone slab at the foot of the terebinth with his "
            "head turned away from the camera toward the far side of the crowd; his "
            "own hair and shoulder are between the camera and his face, so his face "
            "is barely and only partly visible and his eyes cannot reach the lens. "
            "One hand rests open on his knee. THIS IS A WIDE FULL-LENGTH SCENE: the "
            "camera is far enough back that Jesus and at least a dozen seated "
            "listeners appear head to sandals together under the tree with the "
            "bleached reaped country beyond. THE ONLY PALE WOOL IN THE WHOLE PICTURE "
            "IS HIS OWN ROBE; every other person is a solid dark saturated mass of "
            "indigo, umber, rust, olive, charcoal or maroon, in focus and out of "
            "focus alike."
        ),
    },
    {
        "id": "v2-r034-b28", "out": "s28-layeth-up-treasure.jpeg",
        "seg": "j2", "window": "93.993-96.823", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEREBINTH", "JUDEAN-LAND"],
        "narration": "So is he that layeth up treasure for himself,",
        "must_show": "Jesus speaking the closing line, seen close in strict side-on profile in the dappled shade of the terebinth.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _GAZE,
        "scene": (
            "One photograph, 105mm lens, soft dappled shade under the canopy with "
            "warm light bouncing up off the pale dust from BELOW AND IN FRONT, so "
            "nothing behind his head is brighter than his head and there is no rim, "
            "edge, outline, ring or corona around his hair or shoulders anywhere. "
            "Fine film grain, shallow depth of field. THIS IS A STRICT SIDE-ON "
            "PROFILE AND THE CAMERA SITS EXACTLY ON HIS LEFT: Jesus is alone in the "
            "frame from the chest up, turned fully to the LEFT, so the viewer sees "
            "ONE cheek, ONE eye and ONE ear and the clean outline of brow, nose, "
            "lips and beard. THE FAR CHEEK AND THE FAR EYE ARE COMPLETELY HIDDEN "
            "BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF HIS HEAD and cannot be "
            "seen at all; his one visible eye looks steadily out and slightly down "
            "to the LEFT into the crowd and exits the picture through the LEFT EDGE, "
            "so his pupils are nowhere near the lens. His lips are parted mid-word "
            "and his expression is gentle, plain and serious. Behind him, thrown far "
            "out of focus, the grey-green dapple of the terebinth canopy and the "
            "pale dust and stubble beyond. His own robe and mantle fill the bottom "
            "third of the frame from edge to edge, plainly hand-woven with a visible "
            "over-and-under grid of warp and weft on a flat matte surface. He is the "
            "only person in the picture."
        ),
    },
    {
        "id": "v2-r034-b29", "out": "s29-not-rich-toward-god.jpeg",
        "seg": "j2", "window": "96.823-100.486", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TEREBINTH", "CROWD", "JUDEAN-LAND"],
        "narration": "and is not rich toward God.",
        "must_show": "The whole crowd under the terebinth in the moment after the line lands — heads still, nobody moving, seen from above and behind so that the listening is what the picture is about.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 24mm lens, hard bright afternoon sun from the upper "
            "LEFT, fine film grain, deep focus. THE CAMERA IS HIGH ABOVE AND WELL "
            "BEHIND THE CROWD, LOOKING DOWN AND FORWARD OVER THE TOPS OF THEIR "
            "HEADS: because the camera is behind and above every single person in "
            "the frame, EVERY HUMAN BEING IN THIS PICTURE INCLUDING JESUS IS SEEN "
            "FROM BEHIND OR FROM ABOVE AND BEHIND, no eyes face the camera at all, "
            "and a gaze into the lens is geometrically impossible. The near two "
            "thirds of the frame is a close-packed field of dark heads, dark head "
            "cloths, dark shoulders and dark backs, all of them turned inward and "
            "away from the camera, filling the picture corner to corner with no "
            "empty edge anywhere. Beyond them, small in the middle distance under "
            "the terebinth, Jesus sits on the low limestone slab with his back and "
            "one shoulder toward the camera, his face turned away and out of sight. "
            "THIS IS A WIDE FULL-LENGTH SCENE: forty or more people, the whole tree "
            "and the bleached reaped country beyond are all in one frame together. "
            "THE ONLY PALE WOOL IN THE WHOLE PICTURE IS HIS OWN ROBE; every other "
            "person is a solid dark saturated mass of indigo, umber, rust, olive, "
            "charcoal or maroon from edge to edge, sharp and blurred alike."
        ),
    },
    # ============ n11 / n12 — the closing application, its own pictures =======
    {
        "id": "v2-r034-b30", "out": "s30-his-barns-were-full.jpeg",
        "seg": "n11", "window": "100.486-103.476", "wide": False, "jesus": False,
        "locks": ["GRANARY-BARN", "GRANARY-IN"],
        "narration": "His barns were full, but his soul was empty.",
        "must_show": "The heaped grain filling the great store right up to the beams — full to the roof, and nobody in it.",
        "must_not_show": _NO_HALO + _NO_DEATH + _NO_MODERN_FARM + _NO_CREAM
        + "no person, figure, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 24mm lens, camera set low at the very foot of the heap "
            "looking steeply UP the slope of it, fine film grain, deep focus, NO "
            "PERSON IN THE PICTURE AT ALL. The one hard shaft of daylight from the "
            "roof hatch comes down from the upper RIGHT and rakes ACROSS the barley, "
            "throwing the poured ridges into relief and lighting a bright band up "
            "the middle of the slope while the flanks fall into warm brown shadow. "
            "THE GRAIN FILLS ALMOST THE ENTIRE FRAME: a vast mass of clean golden "
            "barley running from the bottom edge up and back until it meets the "
            "three rough hewn timber beams across the top of the picture, so full "
            "that the crest of the heap is pressed close under the beams with only a "
            "hand's breadth of dim air between. Single grains catch light along the "
            "crest. At the very bottom edge, a corner of one hand-woven reed basket "
            "and a coarse dark goat-hair sack. Nothing living is in the picture; the "
            "store is stuffed and silent."
        ),
    },
    {
        "id": "v2-r034-b31", "out": "s31-poor-in-the-only-wealth.jpeg",
        "seg": "n11", "window": "103.476-107.768", "wide": False, "jesus": False,
        "locks": ["COURTYARD"],
        "narration": "He was rich in things — and poor in the only wealth that lasts.",
        "must_show": "A close view of the fallen fired-clay cup lying on its side on the abandoned supper table, the spilled wine long dried to a dark stain in the timber.",
        "must_not_show": _NO_HALO + _NO_DEATH + _NO_CREAM
        + "no person, hand, arm, shoulder or face anywhere in this frame, and no blood; " + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, cold flat colourless grey morning "
            "light with no sun and almost no shadow, fine film grain, very shallow "
            "depth of field, NO PERSON IN THE PICTURE AT ALL. THE FRAME IS FILLED BY "
            "THE TABLE TOP AT ITS OWN LEVEL: the adzed timber slab runs across the "
            "picture with its grain, adze marks and old knife scars raking away out "
            "of focus. Sharp in the middle of the frame lies ONE plain fired-clay "
            "cup on its side, its mouth toward the camera and empty, a dark "
            "purple-brown stain of long-dried wine soaked into the boards in a "
            "narrow tongue running away from its rim. Beside it, going soft, the "
            "edge of a flat round of barley bread now dry and curled hard at the "
            "rim, and a few blown husks of chaff caught against it. Behind, thrown "
            "entirely out of focus into cold pale grey, the mud-plastered courtyard "
            "wall. Nothing is warm, nothing is lit and nobody has come back to it."
        ),
    },
    {
        "id": "v2-r034-b32", "out": "s32-nothing-wrong-with-harvest.jpeg",
        "seg": "n12", "window": "107.768-110.178", "wide": False, "jesus": False,
        "locks": ["JUDEAN-LAND", "WORKERS"],
        "narration": "There is nothing wrong with a good harvest.",
        "must_show": "Two weathered adult hands holding a small bound sheaf of ripe barley ears up in the warm light, clear of the ground, the ears heavy and full.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_CREAM
        + "no ground, soil, dirt, floor, dust or stone anywhere in this frame, and nothing lying down; "
        + "no face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 100mm lens, warm low golden late-afternoon sun coming "
            "from the LEFT and shining THROUGH the barley ears from the side, fine "
            "film grain, very shallow depth of field. THE SUBJECT IS HELD UP IN THE "
            "AIR AND THE GROUND IS NOT IN THE PICTURE AT ALL: TWO big weathered "
            "sun-darkened olive-brown adult hands come in from the lower LEFT and "
            "lower RIGHT and hold a small bound sheaf of ripe barley ears UP AND "
            "CLEAR, well above waist height, so that it is surrounded on every side "
            "by open air and out-of-focus light and nothing beneath it is visible. "
            "The ears are heavy, full, bearded with long awns, and shine warm gold "
            "where the sun passes through them. The hands are plainly adult male "
            "working hands, blunt-fingered and split-nailed, and the straight "
            "unshaped sleeves of dark hand-woven tunics show at both bottom corners, "
            "each with a visible over-and-under grid of warp and weft on a flat "
            "matte surface. NO FACE IS IN THE PICTURE. The whole background is "
            "thrown completely out of focus into warm gold, straw and pale blue — no "
            "horizon line, no building and no ground plane is readable anywhere."
        ),
    },
    {
        "id": "v2-r034-b33", "out": "s33-the-real-question.jpeg",
        "seg": "n12", "window": "110.178-112.998", "wide": True, "jesus": False,
        "locks": ["JUDEAN-LAND", "THRESHING", "WORKERS", "HAND-TOOLS"],
        "narration": "The real question is quieter than that:",
        "must_show": "A village threshing floor in the evening where several ordinary families are working the harvest together, passing filled baskets from hand to hand and sharing the labour.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_MODERN_FARM + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low evening sun from the RIGHT lying "
            "flat across the floor and throwing long soft shadows, dust and chaff "
            "hanging gold in the air, fine film grain, deep focus. THE CAMERA "
            "STANDS BEHIND THE NEAREST WORKERS AND SHOOTS PAST THEM ACROSS THE "
            "FLOOR: the two nearest people are in the lower LEFT foreground seen "
            "ENTIRELY FROM BEHIND as dark backs and shoulders, one of them bent and "
            "handing a loaded hand-woven reed basket up and away to the RIGHT, and "
            "NOT ONE FACE IS TURNED TOWARD THE LENS. FIVE people in total are "
            "visible anywhere in this picture, separated and individually countable "
            "across the bedrock floor: two in the near foreground from behind, two "
            "in the middle distance seen from the side working a wooden winnowing "
            "fork and a flail of two pegged sticks, and one further off in "
            "three-quarter from behind steadying a coarse dark goat-hair sack. The "
            "work is plainly shared and passed along: a chain of hands and baskets "
            "moving grain from the heap to the sacks. Every one of them wears solid "
            "dark saturated earth-coloured cloth head to foot. THIS IS A WIDE "
            "FULL-LENGTH SCENE: all five people head to foot, the whole swept "
            "bedrock floor, the heaped grain and the bleached hills beyond are in "
            "one frame together."
        ),
    },
    {
        "id": "v2-r034-b34", "out": "s34-storing-up-for-yourself.jpeg",
        "seg": "n12", "window": "112.998-115.378", "wide": False, "jesus": False,
        "locks": ["GRANARY-BARN", "GRANARY-YARD", "JUDEAN-LAND"],
        "narration": "are you only storing up for yourself —",
        "must_show": "One grain store shut fast and alone: the low door sealed with a heavy flat stone slab pushed tight against it, nobody near it, in cold flat light.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_MODERN_FARM + _NO_CREAM
        + "no person, figure, hand, arm, shoulder or face anywhere in this frame; "
        + "no padlock, hasp, latch, bolt, hinge, chain or metal fastening of any kind; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, camera low and square-on to the wall, flat "
            "cool daylight with the sun high and out of frame so shadows are short "
            "and hard, fine film grain, NO PERSON IN THE PICTURE AT ALL. THE FRAME "
            "IS FILLED BY ONE WALL AND ONE SHUT DOOR: the mud-plastered pale tan "
            "face of a single squat grain bin runs from edge to edge and top to "
            "bottom, its surface cracked, hand-smoothed and streaked by weather, "
            "with the straw in the plaster catching the light. At the bottom centre, "
            "its ONE low square drawing door is CLOSED FAST by a heavy rough flat "
            "slab of undressed limestone shoved hard up against the opening and "
            "wedged there with two smaller stones, packed round the edges with mud "
            "so that not one grain can escape and nothing inside can be seen. There "
            "is no handle, no hinge and no fastening of any kind — just weight. A "
            "little spilled barley lies in the dust at the foot of the slab, already "
            "blown into a thin drift. The yard around it is bare and empty."
        ),
    },
    {
        "id": "v2-r034-b35", "out": "s35-rich-with-god.jpeg",
        "seg": "n12", "window": "115.378-119.216", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TEREBINTH", "CROWD", "JUDEAN-LAND"],
        "narration": "or are you storing up a life that is rich with God?",
        "must_show": "Jesus and the whole crowd under the terebinth in the last warm light of the day, all of them looking out together across the wide reaped harvest country.",
        "must_not_show": _NO_HALO + _NO_CITY + _NO_DEATH + _NO_NIGHT + _NO_GREEN + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 24mm lens, the last low warm gold light of the day "
            "coming from the far side of the valley but with the sun itself well out "
            "of frame above, so the land ahead is lit and the people are seen as "
            "warm dark shapes from behind with NO bright rim, edge, outline or "
            "corona on any head, hair or shoulder. Fine film grain, deep focus. THE "
            "CAMERA STANDS HIGH ABOVE AND BEHIND THE WHOLE GATHERING AND LOOKS OUT "
            "OVER IT: because the camera is behind and above every person in the "
            "frame, EVERY HUMAN BEING INCLUDING JESUS IS SEEN FROM BEHIND, no eyes "
            "face the camera at all, and a gaze into the lens is geometrically "
            "impossible. The lower third is the dark mass of the seated and standing "
            "crowd and the near boughs of the terebinth. Jesus is in the middle "
            "distance, small, standing now at the edge of the shade with his back to "
            "the camera and one hand low at his side, looking out with them. THE "
            "UPPER TWO THIRDS IS THE LAND AND THE SKY: the whole bleached reaped "
            "country running away in terrace after terrace of straw-gold stubble and "
            "pale limestone to bare hills, with the threshing floors and the small "
            "mud-brick farms scattered small across it, all of it going warm and gold "
            "and quiet. THIS IS A WIDE FULL-LENGTH SCENE and THE ONLY PALE WOOL IN "
            "THE WHOLE PICTURE IS HIS OWN ROBE; every other person is a solid dark "
            "saturated mass of indigo, umber, rust, olive, charcoal or maroon."
        ),
    },
]
