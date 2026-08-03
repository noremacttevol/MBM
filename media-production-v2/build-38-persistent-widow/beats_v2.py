#!/usr/bin/env python3
"""V2 beat map — row 38, build-38-persistent-widow (Luke 18:1-8). REALISTIC V2.

THE INHERITED SCAFFOLD WAS DISCARDED and is kept beside this file as
`beats_v2.py.inherited-scaffold` for provenance only. Three measured reasons:
  1. 29 pictures at 5.7 s each against the wave's MEASURED 3.1-4.9 s, and its
     own docstring called 5.7 s "the library density" — it is not; rows 31-37
     shipped at 3.1-3.7.
  2. Its windows were NOT CONTIGUOUS and were not even in time order: the
     sixth entry declared 58.13-59.46 between windows ending 27.80 and
     starting 28.41.
  3. It covered only up to 164.94 s against the 171.743 s that need pictures,
     leaving nearly SEVEN SECONDS of the closing application undeclared.

WHAT V1 ACTUALLY DID (verified against the artefact, not the prose): SEVEN
stills used for 180.07 s of finished video, and an eighth that was generated
and never placed at all (`s7b-heard-at-once.jpeg` is in `assets/` and appears
nowhere in build.py's BEATS list).
  * `s7-the-good-father.jpeg` covers jv8 + n7b + n7 + n8 — 121.781 s to the
    card at 171.743 s. FIFTY SECONDS on ONE picture: the whole of the KJV
    red-letter Luke 18:8 ("I tell you that he will avenge them speedily...
    shall he find faith on the earth?"), the quiet closing question, AND the
    entire two-segment application the video exists to deliver. Nearly a
    third of the running time on a single frame.
  * `s1-widow-alone.jpeg` covers s1 + n1b + n1 — 0.000 to 29.448, TWENTY-NINE
    SECONDS: Luke's stated purpose, the narrator's framing, and the whole
    introduction of the widow.
  * `s6-praying-heard.jpeg` covers j2 + n6 — 96.599 to 121.781, TWENTY-FIVE
    SECONDS, including the entire "how much more will your Father" contrast
    that the parable turns on.
  * `s5` held 24.1 s (j1 + n5), `s4` 13.0 s, `s2` 13.6 s, `s3` 10.6 s.
  V2 gives all fifteen spoken segments their own pictures: 46 pictures over
  171.743 s = 3.73 s/picture, shortest 2.72 s, longest 4.85 s.

AUDIO: LOCKED, never re-voiced, V1 never written to. The V1 MP4's audio stream
is 180.070 s and extract_beats' reconstruction of V1's own timeline arithmetic
(LEAD 0.28, GAP 0.72, KJV_GAP 1.15, TAIL 1.5) totals 180.07 s — the staleness
tripwire is nowhere near firing.

SOURCING TRAP: CHECKED AND CLEAR ON THIS ROW, which is NOT the same as absent
elsewhere in the wave (rows 20, 22 and 37 all had live ones). By GIT CONTENT
DATE — mtimes are worthless here — `make_narration.py` is 2026-07-23T04:35:31
and every one of the sixteen mp3s AND the delivered MP4 share ONE later commit,
2026-07-27T23:15:18 ("REDO #38: new voice + pacing"). The script PRE-dates its
own audio, which is the safe direction. All sixteen segments were transcribed
anyway with faster-whisper (small.en, word_timestamps=True) and every one
matches the live script. ONE apparent difference and it is whisper's: n7 "Here
is the whole point" came back as "Here's the whole point" — the contraction
family rows 29 and 31 both chased down and settled as the model's own. NO
TEXT_OVERRIDES and no SPEAKER_OVERRIDES.

WINDOWS: rebuilt from scratch from extract_beats plus the MEASURED whisper word
timings, never from the `.timing.json` sidecars. Contiguous 0.000 -> 171.743
(the card's own start), ZERO gaps, and every one of the fifteen speech onsets
lands inside the window written for it. Each interior split is placed 0.15 s
BEFORE the onset of the word it belongs to.

WHO CARRIES WHICH RED-LETTER LINE — this row's sharpest content question.
There are four red-letter segments and they do NOT all belong on Jesus's face:
  * jv2 (Luke 18:2-3) is Jesus SETTING THE SCENE of the parable — "There was
    in a city a judge... and there was a widow in that city; and she came unto
    him, saying, Avenge me of mine adversary." The last clause is THE WIDOW'S
    OWN SENTENCE. Staged INSIDE the parable, in the court, and b11 puts
    "Avenge me of mine adversary" on the widow saying it.
  * j1 (Luke 18:4-5) is THE UNJUST JUDGE TALKING TO HIMSELF — "Though I fear
    not God, nor regard man; yet because this widow troubleth me..." Putting
    Jesus's face under a caption of a godless man admitting he fears no God
    would invert the line completely. All three of its pictures are the judge,
    alone in his own chamber.
  * j2 (Luke 18:6-7) and jv8 (Luke 18:8) ARE Jesus speaking as himself —
    "Hear what the unjust judge saith" — so those are the frames he is in.
Jesus is on screen ONLY where the narration or the verse puts him speaking as
himself: b01, b03, b27, b29, b30, b34, b35, b37, b44 — nine frames. He never
appears inside the parable.

CONTENT CARE. Luke 18:1-8 narrates no heaven, no hell, no angel, no soul, no
death and no punishment, so none of that is painted (the standing wave law).
God is NEVER depicted as any figure, face, form, light or presence — the
contrast beats show a HUMAN father in a doorway, which is the comparison the
narration itself makes ("how much more will your Father"), and he is staged so
he can never be mistaken for a depiction of God: an ordinary Judean villager in
ordinary dark cloth, in his own doorway, in daylight, with no light coming off
him, and his lock forbids long loose hair so he can never read as Jesus either.
The widow's husband is DEAD before the story opens and stays off camera: no
corpse, no bier, no grave, no funeral, no dying man — he is present only as one
folded mantle she keeps. The judge is COLD, never a grotesque or a comic
villain, because a caricature lets the viewer off the hook. The widow is
DIGNITY ITSELF — worn, steady, never pitiable, never cowering, never weeping on
camera; her persistence is the point, not her misery.

STAGING — FOUR places, none of them repeating a composition used anywhere in
the realistic wave (rows 2/8/21 Luke 15; 11 night gale; 16 interior; 19 dawn
shore; 22 basalt doorstep; 23 terraced hillside; 24 moored boat; 25 wheat
field; 26 kitchen garden; 27 synagogue bench + baking yard; 28 ploughed field
+ mud-brick hut; 29 limestone shelf / caravan road / quayside / stone
courtyard; 30 breakwater / open water / strand; 31 night road + bridegroom's
house; 32 trading yard + master's hall; 33 mount + six mercy scenes; 34 barns +
threshing floor; 35 banquet house + city lanes; 36 estate rooftop + accounts;
37 rich man's gate + spirit world):
  * the OLIVE-PRESS YARD where Jesus tells it — a walled village WORK yard
    with a stone crushing basin, an edge-runner stone, a timber beam press and
    clay collecting jars, in the long light of late afternoon. Row 37's
    teaching place was a fig court, 36's a flat rooftop, 35's a Pharisee's
    dining room, 34's a lone terebinth, 33's a rock-cut stair. A WORKING yard,
    mid-pressing, with dust and oil on the listeners' hands, is used by none.
  * the CITY-GATE JUDGMENT CHAMBER and the sunlit square outside its opening —
    the new shared JUDGMENT-SEAT lock.
  * the WIDOW'S ONE BARE ROOM and the dust lane outside her door.
  * the GOOD FATHER'S DOORWAY in a village lane, warm early morning — the
    contrast the narration draws, and the closing image.

THE ROW'S VISUAL ENGINE — "the same worn face at his door". The four n4 beats
(b17-b20) are ONE composition repeated at FOUR HOURS of the same day-after-day:
first light, hard midday, a dust-wind afternoon, and the last of the light. The
camera does not move between them; only the light, the shadow direction and the
dust change, and the fourth goes all the way down to the threshold stone her
feet have hollowed. That repetition IS the picture, and it is the one thing
V1's single still could not do.

LOCK-WORDING AUDIT (the row-34/35/36/37 lesson: read every lock you write as if
the model will build the most modern thing your words permit). Four rewrites
before the first paid image:
  * "judge" and "court" are the most modern-loaded nouns in this story and pull
    an English or American courtroom — a panelled bench, a gavel, a wig and
    gown, a dock, a jury box, a blindfolded statue of Justice. NOTHING in the
    shared recipe reached it, because a courtroom is ARCHITECTURE AND
    FURNITURE, exactly the way a road surface, a prison cell and a barn slip
    through. Cured before the first credit by writing the new shared
    JUDGMENT-SEAT lock, which states the gate chamber, the plain stone seat and
    the standing petitioners POSITIVELY.
  * "widow" pulls VICTORIAN MOURNING — a black crepe gown, a lace veil over the
    face, a bonnet. Her lock states her three pieces of cloth positively in
    dark umber and deep indigo, head bare or under one draped wrap, and beats
    the veil by describing what is actually on her head.
  * "justice" and "the scales of justice" are never written in any prompt; the
    thing she is asking for is stated as what it physically IS — a ruling
    written on one loose sheet of papyrus — because the abstract noun is what
    grows a pair of brass balance scales.
  * "God" never appears in a scene text as anything to be depicted. The
    contrast beats name a HUMAN FATHER IN A DOORWAY and nothing else, and every
    beat that could invite it carries the no-deity clause.

CAST: THREE anchors, all of them pictures that had to exist on the timeline
anyway, so the anchors cost nothing extra. All three are generated in ONE
anchor run before anything else, and NO anchor has another anchor in its frame,
so the REFS cache cannot make an anchor reference itself.
  b05 WIDOW  — face-showing, strict side-on profile, alone in her own room.
  b08 JUDGE  — face-showing, strict side-on profile, alone on his seat.
  b31 FATHER — face-showing, strict side-on profile, alone in his doorway.
Jesus needs no anchor: he carries JESUS-V2-REF on every frame he is in.
"""

import os

OUTPUT_ASSET_DIR = "assets"

# See the AUDIO paragraph above: neither staleness tripwire fires, so the normal
# packet-copy AUDIO LOCK applies. Nothing is re-voiced, nothing is re-timed, and
# the V1 build is never written to.
AUDIO_FROM_V1_SEGMENTS = False

REF = True

# Wired in AFTER the three anchor beats are generated in their own run.
A_WID = "assets/s05-a-widow.jpeg"
A_JUD = "assets/s08-which-feared-not-god.jpeg"
A_FAT = "assets/s31-now-think-about-god.jpeg"
REFS = {"WIDOW": A_WID, "JUDGE": A_JUD, "FATHER": A_FAT}

_HERE = os.path.dirname(os.path.abspath(__file__))


def _have(rel):
    """ANCHOR-FIRST: a character reference attaches only once its anchor exists.

    On the first (anchor-only) run every list below is empty, so `--check`
    passes and no anchor can reference itself through the REFS cache. Every run
    after it wires the accepted anchors into all the later beats automatically.
    """
    return [rel] if os.path.isfile(os.path.join(_HERE, rel)) else []


_WID = _have(A_WID)
_JUD = _have(A_JUD)
_FAT = _have(A_FAT)
_WID_JUD = _WID + _JUD

# ---------------------------------------------------------------- negatives ---
_NO_CREAM = ("no cream, off-white, ivory, buff, beige, taupe, sand, khaki, white "
             "or pale garment, tunic, robe, mantle, sash, wrap or head covering on "
             "anybody anywhere in the frame including the blurred edges; ")
_NO_HALO = ("no halo, no nimbus, no aura, no corona, no bright outline, edge or "
            "contour around any head, hair, shoulder or body, nobody emits or "
            "radiates light, and no light source of any kind standing behind, "
            "above or beyond anyone's head; ")
_NO_COURTROOM = ("no panelled bench, desk, counter, rail, balustrade, screen or "
                 "barrier; no dock, witness box, jury bench, pew, gallery, chair, "
                 "stool, throne, canopy or high-backed seat; no gavel, mallet, "
                 "block, bell, mace, sceptre, staff of office, sword or balance "
                 "scales; no wig, black gown, academic robe, chain of office, "
                 "medallion, badge or uniform; no statue, bust, carved relief, coat "
                 "of arms, banner or flag; no bound book, ledger or framed "
                 "document; and no lettering, numeral, inscription, plaque or sign "
                 "anywhere; ")
_NO_MOURNING = ("no black crepe gown, lace veil, mourning bonnet, hood or cowl over "
                "anybody's face, no face covered or hidden by cloth, no rosary, "
                "cross, crucifix, pendant, brooch or metal ornament, and nobody "
                "kneels at any altar, shrine, statue or built religious structure; ")
_NO_DEITY = ("no depiction of God, deity or any divine person as any figure, face, "
             "form, light or presence; no shaft, beam, column or burst of light "
             "coming down from the sky; no cloud floor, cloudscape, gate of light, "
             "wing, winged figure, cherub, feather, harp, crown, throne, book of "
             "judgement or shining architecture; and no angel, spirit, ghost, "
             "vision or apparition anywhere; ")
_NO_DEATH = ("no corpse, body, bier, shroud, coffin, grave, tomb, headstone, funeral "
             "procession or mourning rite, nobody dead, dying, gasping or collapsing "
             "on camera, and no blood, wound, bandage or dressing on anybody; ")
_NO_MOCK = ("nobody poor, old or bereaved is drawn grotesque, comic, monstrous, "
            "filthy, ragged to indecency, cowering, wailing, grovelling or pitiable, "
            "and nobody powerful is drawn as a fat, jewelled, sneering, leering or "
            "moustache-twirling caricature; each is a real person with dignity; and "
            "no modern wheelchair, walking frame, crutch, gauze bandage or medical "
            "dressing appears anywhere; ")
_NO_MODERN_TOWN = ("no dome, minaret, bell tower, spire, clock, crenellation, "
                   "pitched roof, roof tile, shingle, chimney, gable or "
                   "half-timbering against any sky; no pole, mast, pylon, wire, "
                   "cable, aerial, guardrail, signpost or painted sign; no asphalt, "
                   "tarmac, concrete, kerb, gutter, drain, grating or painted road "
                   "marking; no vehicle, wheel of pneumatic rubber, engine or "
                   "machine of any kind; ")
_NO_GREEN = ("no green meadow, lawn, turf, pasture, moor, fell, upland, heather, "
             "clipped hedgerow, deciduous woodland or lush temperate countryside, "
             "and no soft grey overcast northern European sky; ")
_NO_MODERN_LAMP = ("no candle, wax or taper, no glass, chimney, globe or shade, no "
                   "hurricane lamp, storm lantern, kerosene lamp or oil lantern, no "
                   "metal lamp, no hanging fixture, no ring handle, and no electric "
                   "light of any kind; ")
_NO_IRONGATE = ("no wrought iron, cast iron, railing, bar, grille, lattice, picket, "
                "spearhead, finial or ornamental metalwork on any door, gate or "
                "wall; no hinge, strap hinge, ring, knocker, handle, latch, hasp, "
                "bolt, lock plate, keyhole or padlock; no arch or curved head over "
                "any opening; and no nameplate, sign, lettering or lamp bracket "
                "on it; ")
_NO_PAPER = ("no bound book, codex, ledger, spine, stacked leaves or cover board; no "
             "ruled lines, columns, page numbers or tabulated figures; no writing "
             "desk, lectern, table with legs or stool; no quill, feather pen, metal "
             "nib, glass inkwell, pencil, slate or wax seal; and no even white "
             "machine-made paper anywhere; ")
_GAZE = "nobody's pupils centred on the lens."

# Common lock stacks.
_YARD = ["OLIVE-YARD", "LISTENERS", "JUDEAN-LAND", "BACKGROUND-CAST"]
_COURT = ["JUDGMENT-SEAT", "JUDGE", "JUDEAN-LAND"]
_COURT_W = ["JUDGMENT-SEAT", "JUDGE", "WIDOW", "JUDEAN-LAND", "BACKGROUND-CAST"]
_DOOR = ["JUDGMENT-SEAT", "WIDOW", "COURTYARD-GATE", "JUDEAN-LAND"]
_HOME = ["WIDOW-HOUSE", "WIDOW", "JUDEAN-LAND"]
_FATHERS = ["FATHER", "VILLAGE-LANE", "COURTYARD-GATE", "JUDEAN-LAND"]

LOCKS = {
    # ------------------------------------------------------------- people ----
    "WIDOW": (
        "WIDOW LOCK: the widow of the parable is the SAME WOMAN in every "
        "picture she appears in — in her own room, in the lane, at the "
        "judgment chamber door and standing before the seat — and she is a "
        "JUDEAN of the first century, born and weathered in the dry country of "
        "that place. She is about forty-five, small, spare and upright, with "
        "square set shoulders and the balanced stance of a woman who has "
        "carried water uphill her whole life. HER SKIN IS WARM SUN-DARKENED "
        "OLIVE-BROWN, clearly Middle Eastern, never fair, never pink, never "
        "pale, never European-looking, weathered across the cheekbones and the "
        "backs of the hands, with fine deep lines at the outer corners of the "
        "eyes and either side of the mouth. She has a narrow strong face, high "
        "flat cheekbones, a straight nose, a firm mouth and LARGE STEADY DARK "
        "BROWN EYES that are calm, level and aware — never vacant, never "
        "rolling, never streaming with tears. HER HAIR IS DARK BROWN GOING "
        "IRON-GREY AT THE TEMPLES, thick, parted in the centre and drawn back "
        "into a low coiled knot at the nape, and a clear band of that hair "
        "shows at the front edge, at the temples and at the nape IN EVERY SHOT "
        "OF HER, INCLUDING EVERY SHOT TAKEN FROM BEHIND HER. Her hands are "
        "small, brown, sinewy and work-hardened, the knuckles enlarged and the "
        "nails short and clean — a woman's hands, narrow-boned and clearly not "
        "a man's. SHE IS A WOMAN AND READS AS ONE IN EVERY FRAME. SHE WEARS "
        "EXACTLY THREE SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) ONE "
        "ankle-length coarse hand-woven wool tunic in DARK UMBER-BROWN, faded "
        "unevenly by sun and washing, worn thin at the elbows, its hem frayed "
        "and dust-grey, with straight unshaped sleeves to the wrist; (2) ONE "
        "large rectangular mantle of hand-woven wool in DEEP INDIGO, almost "
        "black in the fold, draped over both shoulders and crossed at the "
        "breast, its ends carrying two narrow woven stripes of the same indigo "
        "a shade darker; and (3) ONE twisted cord of undyed brown flax knotted "
        "at her waist. Plain flat worn leather sandals. HER HEAD IS EITHER "
        "BARE, showing the coiled hair, OR the loose end of that same indigo "
        "mantle is drawn up loosely over the back of her head — HER FACE IS "
        "NEVER COVERED, NEVER SHADOWED OUT, NEVER BEHIND A VEIL, NET, LACE, "
        "GAUZE, HOOD OR COWL, and there is no bonnet, no cap, no black crepe, "
        "no mourning dress of any later century, no jewellery, no ring, no "
        "chain, no brooch and no metal ornament anywhere on her. SHE NEVER "
        "WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, WHITE, PALE "
        "GREY OR ANY PALE OR WASHED-OUT CLOTH. SHE IS NEVER PITIABLE AS "
        "SPECTACLE: never grotesque, never comic, never cowering, never "
        "grovelling, never wailing, never on her knees begging, never clutching "
        "at anybody's clothes, and never weeping on camera. Her bearing is the "
        "whole point of the story — she stands straight, she looks the man she "
        "is speaking to in the face, and she says the same thing again. What is "
        "on her face is PATIENCE AND STEADY RESOLVE, deepening across the story "
        "into plain exhaustion, and never self-pity. IDENTITY FLOOR, WHICH "
        "HOLDS EVEN WHEN SHE IS SMALL, DISTANT, PARTLY CROPPED, SOFTLY OUT OF "
        "FOCUS OR SEEN ENTIRELY FROM BEHIND: a WOMAN of about forty-five, "
        "adult and full-grown, never a girl and never ancient; warm "
        "sun-darkened olive-brown Middle Eastern skin; DARK BROWN HAIR GOING "
        "GREY AT THE TEMPLES, coiled low at the nape; and always the DARK "
        "UMBER-BROWN tunic under the DEEP INDIGO mantle."
    ),
    "JUDGE": (
        "JUDGE LOCK: the judge of the parable is the SAME MAN in every picture "
        "he appears in, and he is a JUDEAN city magistrate of the first "
        "century. He is about fifty-five, of middling height and comfortably "
        "built but NOT fat, sitting and standing with the settled ease of a man "
        "nobody hurries. HIS SKIN IS WARM OLIVE-BROWN, clearly Middle Eastern, "
        "never fair, never pink, never pale, never European-looking, smooth and "
        "far less weathered than a labourer's, with a heavy jaw, a broad "
        "straight nose, thick dark brows and DARK BROWN EYES that are flat, "
        "unhurried and entirely uninterested. He has a FULL, THICK, CAREFULLY "
        "TRIMMED IRON-GREY BEARD squared off at the jaw, and THICK IRON-GREY "
        "HAIR combed back off a high forehead and cut to the middle of the neck "
        "— never long to the shoulders, never loose, never bald, never shaven, "
        "never cropped to the skull — and a clear band of that iron-grey hair "
        "shows at the front edge, at the temples and at the nape IN EVERY SHOT "
        "OF HIM, INCLUDING EVERY SHOT TAKEN FROM BEHIND HIM. HIS HANDS ARE A "
        "MAN'S: broad, heavy-boned, clean, smooth and unmarked, with trimmed "
        "nails — plainly larger and squarer than the widow's small sinewy "
        "brown ones, so the two can never be confused in a close shot. HE "
        "WEARS EXACTLY THREE SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) "
        "ONE ankle-length closely woven wool tunic in DEEP DARK RUST-RED with "
        "straight unshaped sleeves to the wrist; (2) ONE large rectangular "
        "mantle of fine dark wool in DEEP CHARCOAL-BLACK draped over the left "
        "shoulder and falling to mid-calf, its lower edge carrying ONE narrow "
        "woven band a shade darker; and (3) ONE folded cloth sash of DARK "
        "OLIVE knotted at his waist. Good dark leather sandals. HE WEARS NO "
        "HEAD COVERING, no turban, no cap, no wig, no crown, no diadem, no "
        "wreath, no chain of office, no medallion, no badge, no ring, no "
        "jewellery and no metal ornament of any kind, and NEVER a black gown, "
        "academic robe or uniform of any later century. HIS GARMENTS ARE NEVER "
        "CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, WHITE OR ANY PALE "
        "OR WASHED-OUT TONE. HE IS COLD, NOT A VILLAIN: he never sneers, "
        "leers, gloats, smirks, shouts or bares his teeth, he is never obese, "
        "never jewelled, never comic and never monstrous. What is on his face "
        "is BOREDOM AND INDIFFERENCE — a man looking slightly past whoever is "
        "in front of him, entirely untroubled — which across the story frays "
        "into irritation and finally into worn-down annoyance. THAT "
        "ORDINARINESS IS THE POINT: he is exactly the sort of official a real "
        "person meets. IDENTITY FLOOR, WHICH HOLDS EVEN WHEN HE IS SMALL, "
        "DISTANT, PARTLY CROPPED, SOFTLY OUT OF FOCUS OR SEEN ENTIRELY FROM "
        "BEHIND: a MAN of about fifty-five, adult and full-grown; warm "
        "olive-brown Middle Eastern skin; ALWAYS his full trimmed IRON-GREY "
        "beard and iron-grey hair, never clean-shaven; and always the DEEP DARK "
        "RUST-RED tunic under the DEEP CHARCOAL-BLACK mantle. He carries no "
        "wound, no scar, no blood and no light of any kind coming off him in "
        "any frame."
    ),
    "FATHER": (
        "FATHER LOCK: the father in the contrast beats is the SAME MAN in every "
        "picture he appears in, and he is AN ORDINARY JUDEAN VILLAGE FATHER of "
        "the first century standing in the doorway of his own small house — a "
        "human being and nothing more. HE IS NEVER A DEPICTION OF GOD, NEVER A "
        "DIVINE FIGURE, NEVER A PRIEST, NEVER A PATRIARCH ON A SEAT, and he "
        "gives off no light of any kind. He is about forty, lean and "
        "strong-shouldered from work, of middling height. HIS SKIN IS WARM "
        "SUN-DARKENED OLIVE-BROWN, clearly Middle Eastern, never fair, never "
        "pale, never European-looking, with an open weathered face, laugh lines "
        "at the outer corners of warm dark brown eyes, a broad nose and a wide "
        "mouth that rests just short of a smile. He has a SHORT FULL DARK BROWN "
        "BEARD, neatly kept but not barbered, and SHORT THICK DARK BROWN HAIR "
        "cut close above the ears and at the nape — NEVER long, NEVER loose to "
        "the shoulders — clearly visible at the crown, the temples and the nape "
        "IN EVERY SHOT OF HIM, INCLUDING EVERY SHOT TAKEN FROM BEHIND HIM, "
        "because a bearded man with long loose hair reads as Jesus and he is "
        "not. His hands are a working man's: broad, brown, calloused across the "
        "palm, the nails short. HE WEARS EXACTLY TWO SEPARATE PIECES OF CLOTH "
        "AND NOTHING ELSE: (1) ONE knee-length coarse hand-woven wool tunic in "
        "WARM DEEP RUST-BROWN with short straight unshaped sleeves, and (2) ONE "
        "folded cloth sash of DARK OLIVE knotted at his waist. He is barefoot "
        "or in plain flat worn leather sandals. HE NEVER WEARS CREAM, "
        "OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, WHITE OR ANY PALE CLOTH, "
        "no mantle over the head, no head covering, no jewellery and no metal "
        "ornament. WHAT IS ON HIS FACE IS GLADNESS AND ATTENTION — a man who "
        "was already listening for the sound at his door and is pleased it "
        "came. He never looks reluctant, put upon, weary of being interrupted, "
        "stern or grand."
    ),
    "LISTENERS": (
        "LISTENERS LOCK: the people listening to Jesus in the olive yard are "
        "between THREE and FIVE Judean men and women of the first century, aged "
        "from about twenty-five to about sixty — ordinary working villagers who "
        "have been pressing olives, with dust and oil on their hands — each "
        "with warm sun-darkened olive-brown Middle Eastern skin, dark or "
        "greying hair, the men with dark or greying beards, and no two of them "
        "sharing a face. Every one of them is dressed head to foot in ONE SOLID "
        "DARK SATURATED EARTH COLOUR — DARK UMBER, CHARCOAL, DEEP RUST, DARK "
        "OLIVE, DEEP INDIGO or DEEP MAROON — in a plain hand-woven wool tunic "
        "with a rectangular mantle over the shoulders and a folded cloth sash, "
        "and NOT ONE OF THEM WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, "
        "KHAKI, WHITE OR ANY PALE CLOTH, because a pale figure beside Jesus "
        "reads as a second, unlocked Jesus. None of them wears a crown, "
        "jewellery, chain, ring or metal ornament, and none is drawn as a "
        "sneering or comic caricature. THEIR EYELINES ARE STATED AS GEOMETRY "
        "AND NOT AS A PROHIBITION: every one of them is looking AT THE MAN WHO "
        "IS SPEAKING. When the camera stands behind them they are seen as "
        "heads, shoulders and BACKS and no face is in frame at all; when the "
        "camera stands at the speaker's own shoulder their faces ARE visible "
        "and every single eyeline runs past the lens on the side the speaker "
        "sits, converging on him well off the camera axis, so that NOT ONE "
        "PAIR OF PUPILS IS EVER CENTRED ON THE LENS. They lean in, they sit on "
        "the ground, on reed mats and on the low stone kerb of the press bed, "
        "and nobody poses, presents themselves to the viewer or acknowledges "
        "being photographed."
    ),
    # ------------------------------------------------------------- places ----
    "OLIVE-YARD": (
        "OLIVE-PRESS-YARD LOCK: the place where Jesus tells this story is the "
        "walled working yard of a village olive press, and it is used in no "
        "other video. THE YARD is an irregular rectangle of hard-swept packed "
        "earth and worn limestone flags, perhaps eight paces across, enclosed "
        "by walls of sun-dried mud brick over a footing of undressed field "
        "stone, plastered with mud and straw and weathered pale tan, a little "
        "higher than a man's head. THE PRESS ITSELF stands at one side and is "
        "the yard's whole machinery: a THICK CIRCULAR CRUSHING BASIN cut from "
        "one block of grey limestone, its rim worn smooth and dark, with a "
        "heavy ROUND EDGE-RUNNER STONE standing upright in it on a rough hewn "
        "timber axle, and beside it a long unpainted HEWN TIMBER BEAM lying "
        "level in its stone socket with a big rough stone weight lashed to the "
        "far end by twisted flax rope. Under the beam sit flat woven-reed "
        "pressing mats stacked in a short column, and set into the flags below "
        "them is a small round collecting hollow with two fired-clay jars "
        "standing beside it, the stone around them stained dark and glossy "
        "with oil. Two or three more clay jars, a reed basket of unpressed "
        "olives and a folded goat-hair sack sit against the wall. ONE OLD "
        "OLIVE TREE with a gnarled grey split trunk and small dusty grey-green "
        "leaves stands in the corner and throws broken shade across part of "
        "the yard. The one opening in the wall is a plain SQUARE-TOPPED "
        "rectangular gap spanned by a single flat stone lintel. THIS IS NOT A "
        "MILL, A FACTORY OR A YARD OF ANY LATER CENTURY: no metal press, "
        "screw, jack, gear, wheel of iron, chain, cable, pipe, tap, spout, "
        "drain, grating, vat, barrel, cask or bottle; no sawn plank, board, "
        "batten, pallet, nailed frame or dimensional lumber; no dome, minaret, "
        "bell tower, spire, tiled or pitched roof, chimney or gable against "
        "the sky; no column, carved capital, arch of dressed voussoirs, "
        "moulding, mosaic, fountain or statue; no chair, stool, bench with a "
        "back, table with legs or wooden door on hinges; and no lettering, "
        "numeral or painted mark anywhere."
    ),
    "WIDOW-HOUSE": (
        "WIDOW-HOUSE LOCK: the widow's home is ONE SMALL ROOM of a first-"
        "century Judean village house and it is nearly bare, which is the whole "
        "statement. THE ROOM is about four paces across, its walls sun-dried "
        "mud brick plastered with mud and straw and washed a dull pale tan, "
        "hand-smoothed and cracked, its floor beaten earth polished dark and "
        "hard by feet. The flat ceiling is carried on ROUGH HEWN TIMBER BEAMS "
        "with the bark still on parts of them, packed above with brushwood and "
        "earth. THE ONLY OPENINGS are the plain SQUARE-TOPPED rectangular "
        "doorway and ONE small high square hole in the wall, both completely "
        "EMPTY — no glass, no frame, no sash, no shutter, no bars, no curtain "
        "rail — so daylight comes in as one flat slab across the floor. "
        "EVERYTHING SHE OWNS IS IN SIGHT AND IT IS LITTLE: one folded "
        "hand-woven wool sleeping mat against the wall, one rolled reed mat, "
        "two fired-clay jars and a shallow clay bowl, one hand-woven reed "
        "basket, a small clay oil lamp unlit on a ledge cut into the wall, and "
        "a single folded man's mantle of dark wool laid away on a low stone "
        "shelf. THERE IS NOTHING ELSE: no chair, stool, bench, table, bed, "
        "chest, cupboard, shelf of boards, hook, peg rail, picture, mirror, "
        "hanging, rug of pattern, cushion pile, flower, plant pot or ornament; "
        "no hearth surround, mantel, stove, chimney breast, tiled floor or "
        "plaster moulding; no glass, metal fitting, hinge, latch, nail head or "
        "manufactured object of any kind; and no lettering or numeral anywhere."
    ),
    "VILLAGE-LANE": (
        "VILLAGE-LANE LOCK: this is a narrow lane between the houses of a "
        "first-century Judean hill village. THE HOUSES either side are cubes of "
        "sun-dried mud brick over undressed field-stone footings, plastered "
        "with mud and straw and weathered pale tan, with FLAT roofs of poles, "
        "brushwood and packed earth, outside stone stairs climbing to those "
        "roofs, and plain SQUARE-TOPPED rectangular door and window openings "
        "with NO GLASS in them. THE LANE UNDERFOOT is bare packed earth and "
        "pale dust worn hollow by feet, with bedrock breaking through and loose "
        "stones kicked to the sides. Along the walls stand fired-clay jars, "
        "hand-woven reed baskets and a low dry-laid stone bench. AGAINST THE "
        "SKY THERE IS ONLY FLAT ROOFLINE AND BARE TERRACED HILL: no dome, "
        "minaret, bell tower, spire, clock, crenellation, pitched roof, roof "
        "tile, shingle, chimney, gable or half-timbering; no pole, mast, pylon, "
        "wire, cable, aerial, guardrail, signpost or painted sign; no asphalt, "
        "tarmac, concrete, kerb, gutter, drain, grating or painted marking on "
        "the ground; no vehicle, pneumatic wheel, engine or machine; no "
        "flowerbed, planter, trellis, clipped hedge or lawn; and no lettering, "
        "numeral or painted mark anywhere."
    ),
    "JUDEAN-LAND": (
        "JUDEAN-LAND LOCK: this is the dry limestone hill country of first-"
        "century Judea and the land is stated POSITIVELY, because a Judean "
        "hillside has more than once come back as a green northern European "
        "one. THE GROUND is pale grey-tan limestone breaking through thin "
        "stony soil, bare packed dust worn hollow by feet, loose flints and "
        "weathered rock. WHAT GROWS is sparse, hard and drought-adapted: "
        "scorched straw-gold stubble and dead sun-bleached grass in tufts, "
        "grey-green thorn scrub, low aromatic shrubs, and old olive, fig and "
        "almond trees with gnarled trunks and small dusty grey-green leaves. "
        "THE LIGHT is hard, dry and brilliant, the sky a deep cloudless blue "
        "burning almost white at the horizon, and the far hills are bare, "
        "rounded, terraced and hazy with heat. THERE IS NO GREEN MEADOW, LAWN, "
        "TURF, PASTURE, MOOR, FELL, UPLAND, HEATHER, BRACKEN, CLIPPED "
        "HEDGEROW, DECIDUOUS WOODLAND, PINE FOREST, FERN, BLUEBELL, RIVER "
        "VALLEY OF LUSH TEMPERATE GRASS OR SOFT GREY OVERCAST NORTHERN SKY "
        "ANYWHERE, and no rain, mud, moss, ivy or standing puddle."
    ),
}

# Reusable geometry sentences. Every one is PORTED from an accepted frame in
# rows 31-37, not newly invented.
_PROFILE = (
    "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: this is a "
    "STRICT SIDE-ON PROFILE. The camera stands square to the side of the head "
    "at eye height, so the picture shows the NEAR cheek broad and complete and "
    "the FAR cheek and the FAR EYE HIDDEN BEHIND THE BRIDGE OF THE NOSE. The "
    "eyeline runs LATERALLY ACROSS the frame and exits through the edge the "
    "face is turned toward. THE HEAD NEVER TURNS TOWARD THE LENS, THE FACE IS "
    "NEVER SEEN SQUARE-ON OR IN THREE-QUARTER, AND THE PUPILS NEVER COME ROUND "
    "ONTO THE CAMERA AXIS. "
)
_BEHIND = (
    "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: THE "
    "CAMERA STANDS BEHIND AND SLIGHTLY ABOVE THE NEAR PEOPLE AND SHOOTS PAST "
    "THEM, so the near figures are heads, shoulders and BACKS seen entirely "
    "FROM BEHIND and NOT ONE FACE IS TURNED TOWARD THE LENS. "
)
_GRAIN = "fine film grain, true depth of field, real physical scale. "

BEATS = [
    # ===== s1 — Luke 18:1, the stated purpose ================================
    {
        "id": "v2-r038-b01", "out": "s01-he-spake-a-parable.jpeg",
        "seg": "s1", "window": "0.000-3.590", "wide": True, "jesus": True, "ref": REF,
        "locks": _YARD,
        "narration": "And he spake a parable unto them to this end, that men ought",
        "must_show": "Jesus sitting on the low stone kerb of the olive press bed in a walled village press yard in late-afternoon light, turning to the villagers sitting with him as he begins to speak; the camera stands behind the listeners and shoots past their backs.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the villager Jesus is speaking to is NOT behind the camera — she "
            "sits far out at the LEFT EDGE of the picture, so Jesus's head is "
            "turned a quarter-turn away from the lens and STAYS there. The "
            "camera sees the SIDE of his face, the near cheek broad and the far "
            "cheek foreshortened with the far eye narrowed behind the bridge of "
            "his nose, and his eyeline runs LATERALLY ACROSS the frame and out "
            "through the LEFT EDGE. HIS PUPILS NEVER COME ROUND ONTO THE LENS "
            "AXIS AND HE NEVER LOOKS INTO THE CAMERA. "
            "One photograph, 35mm lens, long low late-afternoon sun raking in "
            "from the RIGHT across the packed earth of the yard, the shadow of "
            "the wall lying long across the flags, the sun itself well out of "
            "frame and NEVER behind any head, " + _GRAIN +
            "THE CAMERA STANDS BEHIND AND SLIGHTLY ABOVE THE SEATED LISTENERS "
            "AND SHOOTS PAST THEM: four dark-clad village men and women fill "
            "the lower and right third of the frame as heads, shoulders and "
            "BACKS seen entirely FROM BEHIND, sitting on hand-woven reed mats "
            "and on the low stone kerb of the crushing basin and leaning in, "
            "and NOT ONE FACE IS TURNED TOWARD THE LENS. Jesus sits facing them "
            "on the far side, left of centre, on the low limestone kerb with "
            "one forearm resting across his knee and the other hand open and "
            "low, three-quarter length and three-quarter view; he has just "
            "turned his head to his own left toward the nearest listener and "
            "his gaze travels level and to the LEFT and exits the picture "
            "through the LEFT EDGE. THIS IS A WIDE FULL-LENGTH GROUP PHOTOGRAPH "
            "AND NOT A PORTRAIT: the camera is far enough back that all five "
            "people, the round grey crushing stone of the press, the timber "
            "press beam and the plastered mud-brick wall behind them are in "
            "frame together. THE ONLY PALE WOOL IN THE WHOLE PICTURE IS HIS OWN "
            "ROBE; every other person is a solid dark saturated mass of indigo, "
            "umber, rust, olive, charcoal or maroon from edge to edge, in focus "
            "and out of focus alike."
        ),
    },
    {
        "id": "v2-r038-b02", "out": "s02-always-to-pray.jpeg",
        "seg": "s1", "window": "3.590-7.595", "wide": False, "jesus": False,
        "locks": ["OLIVE-YARD", "LISTENERS", "JUDEAN-LAND"],
        "narration": "always to pray and not to faint.",
        "must_show": "A tight, quiet close shot of one listening villager's worn brown hands resting open and loose on his own knees, oil and dust still on them from the pressing — the physical picture of praying and not fainting, with no face in the frame at all.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOCK + _NO_GREEN + _GAZE,
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, long low "
            "late-afternoon sun raking in from the RIGHT, the sun well out of "
            "frame, " + _GRAIN +
            "A TIGHT CLOSE SHOT WITH NO FACE IN IT ANYWHERE. The camera sits "
            "low and close, level with a seated man's knees and slightly to his "
            "side, and the frame is filled from edge to edge by his lap: the "
            "dark umber wool of his tunic falling across his crossed legs in "
            "coarse visible warp-and-weft, and both of his HANDS resting open, "
            "palms upward and fingers loosely curled, one on each knee. They "
            "are a working man's hands — broad, deeply sun-browned, the "
            "knuckles enlarged, the nails short and rimmed with dark olive "
            "dust, a green-black smear of crushed olive across one thumb. The "
            "picture is cropped at the waist so his chest, shoulders and head "
            "are entirely OUT OF FRAME and no face, eye or gaze appears at all. "
            "Behind the hands, thrown far out of focus, the packed earth of the "
            "yard and the pale plastered wall carry the long shadow of the "
            "press beam. Nothing else is in the frame."
        ),
    },
    # ===== n1b — the narrator states why the story exists ====================
    {
        "id": "v2-r038-b03", "out": "s03-he-wanted-people-to-keep-praying.jpeg",
        "seg": "n1b", "window": "7.595-11.985", "wide": True, "jesus": True, "ref": REF,
        "locks": _YARD,
        "narration": "Luke tells us up front why Jesus told this one. He wanted people to keep praying and",
        "must_show": "Jesus mid-sentence in the press yard, both hands open low in front of him, leaning slightly toward the villagers he is teaching; camera off to his side at his own shoulder height.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the camera stands well out to Jesus's RIGHT and slightly forward "
            "of him, so he is seen in near-profile with the near cheek broad "
            "and the far eye narrowed behind the bridge of his nose, and his "
            "eyeline runs LATERALLY ACROSS the frame to the listeners at the "
            "LEFT and exits through the LEFT EDGE. HIS PUPILS NEVER COME ROUND "
            "ONTO THE LENS AXIS. "
            "One photograph, 50mm lens, long low late-afternoon sun raking in "
            "from behind the camera's right shoulder so it falls on the FRONT "
            "planes of every face, never behind any head, " + _GRAIN +
            "Jesus sits forward on the low limestone kerb of the crushing basin "
            "at the RIGHT of the frame, three-quarter length, elbows on his "
            "knees and BOTH HANDS OPEN AND LOW in front of him, palms up, "
            "caught mid-sentence. At the LEFT of the frame, closer to the "
            "camera and a little below him, two villagers sit on reed mats seen "
            "in three-quarter FROM BEHIND, one leaning in with a forearm across "
            "his knee. Between them the packed earth, the oil-darkened "
            "collecting hollow and two fired-clay jars carry the eye. Behind "
            "them the plastered mud-brick wall and the gnarled grey olive trunk "
            "in the corner. THE ONLY PALE WOOL IN THE WHOLE PICTURE IS HIS OWN "
            "ROBE; every other person is a solid dark saturated mass of indigo, "
            "umber, rust, olive, charcoal or maroon from edge to edge."
        ),
    },
    {
        "id": "v2-r038-b04", "out": "s04-not-lose-heart.jpeg",
        "seg": "n1b", "window": "11.985-16.432", "wide": False, "jesus": False,
        "locks": ["OLIVE-YARD", "LISTENERS", "JUDEAN-LAND"],
        "narration": "not lose heart. That is the whole reason the story exists.",
        "must_show": "One tight portrait of a listening villager — a tired man of about sixty who has clearly been close to losing heart himself — his eyes fixed on the speaker well off to the side of the camera.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOCK + _NO_GREEN + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the man is looking at the speaker, who sits FAR OUT PAST THE RIGHT "
            "EDGE of the picture and well below the camera. His head is turned "
            "a clear quarter-turn to his own left and his eyeline runs "
            "diagonally across and DOWN, exiting through the RIGHT EDGE of the "
            "frame. HIS PUPILS ARE NEVER CENTRED ON THE LENS AND HE NEVER LOOKS "
            "INTO THE CAMERA. "
            "One photograph, 85mm lens, shallow depth of field, long low "
            "late-afternoon sun falling in from the RIGHT across the front "
            "planes of his face, the sun well out of frame and NEVER behind his "
            "head, " + _GRAIN +
            "A TIGHT THREE-QUARTER PORTRAIT of ONE man of about sixty filling "
            "the frame from the chest up, seated. Warm deeply sun-darkened "
            "olive-brown Middle Eastern skin, deep lines across the forehead "
            "and either side of the mouth, a full grey-white beard, thick grey "
            "hair, heavy tired eyelids over dark brown eyes. He wears a solid "
            "DARK CHARCOAL hand-woven wool tunic with a DEEP MAROON mantle over "
            "the shoulders, the weave plainly visible. His expression is quiet "
            "and absolutely still — a man who has been carrying something a "
            "long time and has just heard it named. Behind him the pale "
            "plastered mud-brick wall of the yard and the out-of-focus grey "
            "shape of the press beam. NOBODY ELSE IS IN THE PICTURE."
        ),
    },
    # ===== n1 — the widow introduced. b05 IS THE WIDOW ANCHOR ================
    {
        "id": "v2-r038-b05", "out": "s05-a-widow.jpeg",
        "seg": "n1", "window": "16.432-20.722", "wide": False, "jesus": False,
        "locks": _HOME,
        "narration": "Jesus told a story about a widow. She had lost her husband and had no one",
        "must_show": "THE WIDOW ANCHOR. One woman alone in her own bare room in flat morning light, seen in strict side-on profile, her whole face clearly readable — this frame defines her face for every later picture in the video.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOURNING + _NO_DEATH + _NO_MOCK + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            _PROFILE +
            "One photograph, 85mm lens, shallow depth of field, flat early "
            "morning daylight coming in through the empty square doorway at "
            "screen LEFT and lying across her face and the beaten earth floor "
            "in one soft slab, no other light source in the room, " + _GRAIN +
            "SHE IS THE ONLY PERSON IN THE PICTURE and she fills the frame from "
            "the waist up, standing still in the middle of her one bare room, "
            "turned to face the doorway light at the LEFT. The camera is square "
            "to her right side. Her chin is level, her shoulders square and her "
            "back straight; her hands are down and clasped loosely in front of "
            "her. Her face is fully lit from the LEFT by the doorway and reads "
            "completely: the strong narrow line of her profile, the high flat "
            "cheekbone, the fine deep lines at the outer corner of her eye, her "
            "dark brown hair going iron-grey at the temple and drawn back into "
            "its low coiled knot at the nape, plainly visible and uncovered. "
            "Her expression is steady, calm and tired — grief that has already "
            "been lived with, not grief being performed. Behind her, thrown "
            "gently out of focus, the mud-plastered wall, the rolled reed mat "
            "and one fired-clay jar. The room is otherwise empty and that "
            "emptiness is the point."
        ),
    },
    {
        "id": "v2-r038-b06", "out": "s06-someone-had-wronged-her.jpeg",
        "seg": "n1", "window": "20.722-25.042", "wide": False, "jesus": False,
        "locks": _HOME, "char_refs": _WID,
        "narration": "to protect her. Someone had wronged her and she had no power,",
        "must_show": "A tight low shot of the widow's own small brown hands resting flat on a dead man's folded dark mantle across her lap — the husband present only as a folded piece of cloth she keeps, with no face in the frame.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOURNING + _NO_DEATH + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, "
            "flat early morning daylight from the empty doorway at screen LEFT, "
            "no other light source, " + _GRAIN +
            "A TIGHT CLOSE SHOT WITH NO FACE IN IT ANYWHERE. The camera looks "
            "down and slightly across a seated woman's lap and the frame is "
            "filled edge to edge by it: the dark umber-brown coarse hand-woven "
            "wool of her own tunic, and lying folded square across her knees "
            "ONE large mantle of a man's dark brown wool, its coarse "
            "over-and-under warp-and-weft grid sharp in the light, its edge "
            "frayed and one corner mended with plainly visible darker "
            "stitching. BOTH OF HER HANDS rest flat on top of it, one over the "
            "other, perfectly still. THEY ARE A WOMAN'S HANDS AND READ AS ONE: "
            "small, narrow-boned, deeply sun-browned, sinewy, the knuckles "
            "enlarged by work, the nails short and clean, a plain twisted brown "
            "flax cord at her waist behind them. The picture is cropped at her "
            "waist so her chest, shoulders and head are entirely OUT OF FRAME "
            "and no face, eye or gaze appears at all. The beaten earth floor "
            "and the mud-plastered wall fall away far out of focus behind. "
            "NOBODY ELSE IS IN THE PICTURE and nothing else is on the cloth."
        ),
    },
    {
        "id": "v2-r038-b07", "out": "s07-no-one-to-make-anyone-listen.jpeg",
        "seg": "n1", "window": "25.042-29.448", "wide": True, "jesus": False,
        "locks": ["WIDOW", "VILLAGE-LANE", "COURTYARD-GATE", "JUDEAN-LAND",
                  "BACKGROUND-CAST"],
        "char_refs": _WID,
        "narration": "no money, no one important to make anyone listen.",
        "must_show": "The widow standing small and alone in her own empty doorway looking away down the village lane toward the town, the whole width of the lane lying empty in front of her — powerlessness stated as distance and empty space, not as misery.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOURNING + _NO_MOCK + _NO_MODERN_TOWN + _NO_IRONGATE + _NO_GREEN + _GAZE,
        "scene": (
            _BEHIND +
            "One photograph, 35mm lens, hard clear mid-morning sun raking in "
            "from the LEFT and throwing the long shadow of the house wall "
            "across the dust, the sun well out of frame, " + _GRAIN +
            "A WIDE FULL-LENGTH SCENE, NOT A PORTRAIT: the camera stands back "
            "inside the shadowed room behind her, low and near the floor, and "
            "shoots out past her through the plain SQUARE-TOPPED doorway. The "
            "near foreground is filled edge to edge by the dark interior — the "
            "beaten earth floor, the worn hollowed limestone threshold slab, "
            "and the two plain mud-plastered jambs framing the picture at left "
            "and right. SHE STANDS IN THAT OPENING SEEN ENTIRELY FROM BEHIND, "
            "small and full-length in the middle distance, one hand resting "
            "against the right-hand jamb, her weight even on both feet, her "
            "back straight. HER DARK BROWN HAIR GOING IRON-GREY AT THE TEMPLES "
            "IS PLAINLY VISIBLE, coiled low at the nape, uncovered, with the "
            "deep indigo mantle across her shoulders and the dark umber-brown "
            "tunic to her ankles. She is looking away from the camera down the "
            "lane and NO PART OF HER FACE IS TURNED TOWARD THE LENS. Beyond her "
            "the dust lane runs away between pale mud-brick houses with flat "
            "roofs and empty square openings, rising toward the town on the "
            "bare terraced hill, and THE WHOLE WIDTH OF THAT LANE LIES EMPTY — "
            "at most two distant figures, each a solid dark saturated mass head "
            "to foot, going about their own business far up the lane with their "
            "backs to her, nobody looking her way. Everything light-toned in "
            "the picture is stone, plaster, dust or bare skin."
        ),
    },
    # ===== jv2 — Luke 18:2-3, staged INSIDE the parable ======================
    # b08 IS THE JUDGE ANCHOR.
    {
        "id": "v2-r038-b08", "out": "s08-which-feared-not-god.jpeg",
        "seg": "jv2", "window": "29.448-32.998", "wide": False, "jesus": False,
        "locks": _COURT,
        "narration": "There was in a city a judge which feared not God,",
        "must_show": "THE JUDGE ANCHOR. The judge alone, seated on the plain stone seat in the gate chamber in flat daylight, seen in strict side-on profile with his whole face clearly readable — this frame defines his face for every later picture in the video.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_MOCK + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            _PROFILE +
            "One photograph, 85mm lens, shallow depth of field, hard flat "
            "daylight coming in from screen LEFT through a plain square-topped "
            "opening and lying across his face and the worn limestone flags in "
            "one clean slab, the sun itself well out of frame and NEVER behind "
            "his head, " + _GRAIN +
            "HE IS THE ONLY PERSON IN THE PICTURE and he fills the frame from "
            "the waist up, seated square and settled on the plain rectangular "
            "limestone block with its folded dark wool cushion, his back "
            "against the dressed stone of the chamber wall. The camera is "
            "square to his left side. One forearm rests along his thigh and his "
            "other hand hangs loose from the wrist. His face is fully lit from "
            "the LEFT and reads completely: the heavy jaw, the broad straight "
            "nose, the thick dark brow, the full carefully trimmed IRON-GREY "
            "beard squared at the jaw and the thick iron-grey hair combed back "
            "off a high forehead and cut to the middle of his neck. His "
            "expression is FLAT AND UNINTERESTED — the settled boredom of a man "
            "for whom this is simply the day's work — never a sneer, never a "
            "smirk, never a scowl. Behind him, thrown gently out of focus, the "
            "big dry-laid pale limestone blocks of the chamber wall and one "
            "hand-woven reed basket of rolled loose sheets on the floor. NOBODY "
            "ELSE IS IN THE PICTURE."
        ),
    },
    {
        "id": "v2-r038-b09", "out": "s09-neither-regarded-man.jpeg",
        "seg": "jv2", "window": "32.998-36.158", "wide": True, "jesus": False,
        "locks": ["JUDGMENT-SEAT", "JUDGE", "JUDEAN-LAND", "BACKGROUND-CAST"],
        "char_refs": _JUD,
        "narration": "neither regarded man, and there was a widow in that",
        "must_show": "A wide of the whole gate chamber: the judge small on his stone seat at the far end, three petitioners standing waiting along the walls, and the plain fact of the room — he sits, everyone else stands, and he is not looking at any of them.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_MOCK + _NO_MODERN_LAMP + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            _BEHIND +
            "One photograph, 28mm lens, hard flat late-morning daylight falling "
            "in through the big square-topped opening at screen RIGHT in one "
            "bright slab across the worn limestone flags, the rest of the "
            "chamber in deep cool shadow, the sun well out of frame, " + _GRAIN +
            "A WIDE FULL-LENGTH SCENE WITH SEVERAL PEOPLE, NEVER A PORTRAIT: "
            "the camera stands back at the mouth of the chamber, chest high, "
            "and shoots the length of it. The near foreground at the lower left "
            "is filled by the shoulder and BACK of ONE waiting petitioner seen "
            "entirely from behind, a solid dark umber mass, out of focus. "
            "Beyond him the empty stone floor runs away, and at the far end THE "
            "JUDGE sits small and full-length on his plain limestone seat "
            "against the back wall, in three-quarter view turned to his own "
            "left, his iron-grey hair and full iron-grey beard clearly readable "
            "even at that size, in his deep dark rust-red tunic and deep "
            "charcoal-black mantle. HE IS LOOKING AT NONE OF THEM: his eyeline "
            "runs down and away to the floor at his own left, exiting the "
            "picture through the LEFT EDGE. Two more petitioners stand waiting "
            "along the left-hand wall, both seen from behind or in lost "
            "profile, each a solid dark saturated mass of charcoal, deep rust "
            "or dark olive head to foot. HE IS THE ONLY PERSON SITTING; "
            "EVERYONE ELSE IN THE PICTURE IS STANDING, and NOT ONE FACE IS "
            "TURNED TOWARD THE LENS. Everything light-toned in the frame is "
            "dressed limestone, dust and bare skin."
        ),
    },
    {
        "id": "v2-r038-b10", "out": "s10-she-came-unto-him.jpeg",
        "seg": "jv2", "window": "36.158-39.818", "wide": True, "jesus": False,
        "locks": _COURT_W, "char_refs": _WID_JUD,
        "narration": "city, and she came unto him, saying, avenge",
        "must_show": "The widow walking in — small, upright, alone, framed in the bright square opening of the chamber — seen past the judge's shoulder from inside, so the whole distance between them is in one picture.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_MOURNING + _NO_MOCK + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            _BEHIND +
            "One photograph, 50mm lens, hard flat late-morning sun blazing in "
            "the square-topped opening beyond her so the sunlit square outside "
            "is bright and the chamber is cool shadow — but SHE IS LIT ON THE "
            "FRONT OF HER BODY AND FACE by that same light bouncing off the "
            "pale stone floor, never rimmed or outlined from behind, and no "
            "light source stands behind anybody's head, " + _GRAIN +
            "A WIDE FULL-LENGTH SCENE, NOT A PORTRAIT. The camera stands inside "
            "the chamber just behind and to the left of the seated judge and "
            "shoots past him: the near left third of the frame is filled by his "
            "SHOULDER, the deep charcoal-black wool of his mantle and the back "
            "and side of his head — his thick iron-grey hair plainly visible at "
            "the nape and temple — all of it close, dark and softly out of "
            "focus, and NO PART OF HIS FACE IS TURNED TOWARD THE LENS. Beyond "
            "him, sharp and small and full-length in the middle distance, THE "
            "WIDOW has walked in and stopped on the worn limestone flags, "
            "standing straight and square with her weight even on both feet, "
            "her chin level and her face turned toward the judge in clean "
            "three-quarter profile — her dark brown hair going iron-grey at the "
            "temples coiled low and uncovered, the deep indigo mantle crossed "
            "at her breast over the dark umber-brown tunic. Her eyeline runs "
            "across the frame to the man in the foreground and NEVER to the "
            "camera. Between them lies four paces of empty sunlit stone floor "
            "and NOTHING ELSE — no rail, no barrier, no furniture. Behind her "
            "the bright rectangle of the opening and the pale dust of the "
            "square outside, with ONE distant figure in solid dark cloth "
            "walking away out there."
        ),
    },
    {
        "id": "v2-r038-b11", "out": "s11-avenge-me-of-mine-adversary.jpeg",
        "seg": "jv2", "window": "39.818-43.077", "wide": False, "jesus": False,
        "locks": ["JUDGMENT-SEAT", "WIDOW", "JUDEAN-LAND"], "char_refs": _WID,
        "narration": "me of mine adversary.",
        "must_show": "The widow's own face as she says her one sentence — close, in profile, chin level, absolutely steady. This is HER line inside the parable, not Jesus speaking as himself, and it belongs on her.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOURNING + _NO_COURTROOM + _NO_MOCK + _GAZE,
        "scene": (
            _PROFILE +
            "One photograph, 85mm lens, shallow depth of field, hard flat "
            "daylight bouncing up off the pale limestone floor onto the FRONT "
            "planes of her face from below and in front, the sun well out of "
            "frame and NEVER behind her head, " + _GRAIN +
            "SHE IS THE ONLY PERSON IN THE PICTURE. A TIGHT SHOT filling the "
            "frame from the shoulders up, the camera square to her left side at "
            "her own eye height. Her head is turned to the LEFT, her chin "
            "level, her mouth open on a word — she is speaking, mid-sentence. "
            "Her whole profile reads: the strong narrow line of nose and brow, "
            "the high flat cheekbone, the fine deep lines at the outer corner "
            "of her eye, the firm set of her jaw, her dark brown hair going "
            "iron-grey at the temple drawn back into its low coiled knot at the "
            "nape and plainly visible, the deep indigo mantle across her "
            "shoulder over the dark umber-brown tunic. WHAT IS ON HER FACE IS "
            "PLAIN LEVEL RESOLVE — she is not begging, not weeping, not "
            "pleading, not cowering; she is stating a fact to a man's face for "
            "what is clearly not the first time. Behind her, far out of focus, "
            "the big pale dressed limestone blocks of the chamber wall and one "
            "bright out-of-focus slab of the sunlit opening. NOBODY ELSE IS IN "
            "THE PICTURE."
        ),
    },
    # ===== n2 — the plea =====================================================
    {
        "id": "v2-r038-b12", "out": "s12-one-simple-plea.jpeg",
        "seg": "n2", "window": "43.077-46.407", "wide": False, "jesus": False,
        "locks": ["JUDGMENT-SEAT", "WIDOW", "JUDEAN-LAND"], "char_refs": _WID,
        "narration": "The widow came to him with one simple plea,",
        "must_show": "The widow's two empty open hands held out low and steady in front of her — a close shot of the ask itself, with nothing in them and no face in the frame.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, "
            "hard flat daylight from screen LEFT, the sun well out of frame, "
            + _GRAIN +
            "A TIGHT CLOSE SHOT WITH NO FACE IN IT ANYWHERE. The camera is at "
            "waist height and slightly to the side, and the frame is filled "
            "from edge to edge by BOTH OF THE WIDOW'S HANDS held out low in "
            "front of her, side by side, palms turned upward and open, fingers "
            "relaxed and slightly apart, held perfectly steady and NOT "
            "trembling. THEY ARE A WOMAN'S HANDS AND READ AS ONE: small, "
            "narrow-boned, deeply sun-browned, sinewy, the knuckles enlarged by "
            "work, deep lines across the palms, the nails short and clean. THEY "
            "ARE COMPLETELY EMPTY — no coin, no cloth, no jar, no gift, no "
            "written sheet, nothing at all. The dark umber-brown coarse wool of "
            "her sleeves runs to her wrists and the deep indigo of her mantle "
            "hangs behind them. The picture is cropped at the breastbone so her "
            "shoulders and head are entirely OUT OF FRAME and no face, eye or "
            "gaze appears. Far behind and thrown right out of focus, the pale "
            "dressed limestone of the chamber wall and one dark shape that is "
            "the seated man she is speaking to."
        ),
    },
    {
        "id": "v2-r038-b13", "out": "s13-against-the-man-who-wronged-me.jpeg",
        "seg": "n2", "window": "46.407-49.824", "wide": False, "jesus": False,
        "locks": ["JUDGMENT-SEAT", "JUDGE", "ESTATE-ACCOUNTS", "JUDEAN-LAND"],
        "char_refs": _JUD,
        "narration": "give me justice against the man who wronged me.",
        "must_show": "The judge's face while she speaks — looking down at a loose written sheet in his hand instead of at her, entirely unmoved. His inattention is the picture.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_PAPER + _NO_MOCK + _GAZE,
        "scene": (
            _PROFILE +
            "One photograph, 85mm lens, shallow depth of field, hard flat "
            "daylight from screen RIGHT falling across the front of his face "
            "and down onto the sheet in his hand, the sun well out of frame and "
            "NEVER behind his head, " + _GRAIN +
            "HE IS THE ONLY PERSON SHARP IN THE PICTURE, filling the frame from "
            "the chest up, seated on his stone seat. The camera is square to "
            "his right side. His head is turned to the RIGHT and tipped DOWN, "
            "his eyes lowered onto ONE loose single leaf of fibrous cream-brown "
            "papyrus held slack in his broad heavy-boned right hand — its edges "
            "torn rough, its few short lines of dark brown hand-drawn reed-pen "
            "strokes crooked and irregular. HIS EYELINE RUNS DOWN AND OUT "
            "THROUGH THE LOWER RIGHT CORNER OF THE FRAME AND NEVER TOWARD THE "
            "CAMERA AND NEVER TOWARD THE PERSON SPEAKING TO HIM. His face reads "
            "completely: the heavy jaw, the full trimmed iron-grey beard, the "
            "iron-grey hair combed back and cut to the middle of his neck, the "
            "flat incurious set of the mouth. WHAT IS ON HIS FACE IS NOTHING AT "
            "ALL — not anger, not cruelty, not a sneer: simple boredom, a man "
            "reading something else while somebody talks. At the extreme left "
            "edge of the frame, thrown far out of focus and unreadable, one "
            "narrow dark shape stands for the woman speaking. Behind him the "
            "pale dressed limestone wall."
        ),
    },
    # ===== n3 — he waved her away ============================================
    {
        "id": "v2-r038-b14", "out": "s14-he-waved-her-away.jpeg",
        "seg": "n3", "window": "49.824-53.334", "wide": False, "jesus": False,
        "locks": _COURT, "char_refs": _JUD,
        "narration": "But the judge did not care. He waved her away.",
        "must_show": "The dismissal itself, mid-action: the judge's broad hand flicking outward and away toward the doorway while his head is already turning the other way.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_MOCK + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "his head is turned a full quarter-turn AWAY to his own right, so "
            "the camera sees mostly the line of his cheek and beard; his "
            "eyeline runs away across the frame and exits through the RIGHT "
            "EDGE. HIS PUPILS NEVER COME ROUND ONTO THE LENS AXIS. "
            "One photograph, 50mm lens, hard flat daylight from screen LEFT "
            "raking across the stone, the sun well out of frame and NEVER "
            "behind his head, " + _GRAIN +
            "A MID-ACTION SHOT CAUGHT AT ITS PEAK, not a pose. He fills the "
            "left two-thirds of the frame from the knees up, seated on the "
            "stone seat and already leaning back and turning away to his own "
            "right. HIS NEAR HAND IS THE SUBJECT: the broad heavy-boned left "
            "hand thrown out low and OUTWARD to screen right at hip height, "
            "wrist loose, fingers half open and flicking away from the body in "
            "the middle of the motion, unmistakably shooing something out of "
            "the room — the arm is extended and travelling, not resting. It is "
            "plainly A MAN'S HAND, large, square and smooth. His head is "
            "already turned the other way and he is not looking at whoever he "
            "is dismissing. His deep dark rust-red tunic and deep "
            "charcoal-black mantle fall around him; his iron-grey hair and full "
            "iron-grey beard read clearly. In the near right foreground, dark "
            "and thrown right out of focus, the edge of a standing figure's "
            "indigo mantle occupies the corner, unrecognisable. Behind him the "
            "pale dressed limestone wall and one basket of rolled sheets."
        ),
    },
    {
        "id": "v2-r038-b15", "out": "s15-no-bribe-no-rank.jpeg",
        "seg": "n3", "window": "53.334-56.474", "wide": True, "jesus": False,
        "locks": ["JUDGMENT-SEAT", "JUDGE", "JUDEAN-LAND", "BACKGROUND-CAST"],
        "char_refs": _JUD,
        "narration": "She had nothing to offer him. No bribe, no",
        "must_show": "What she does not have, shown by what somebody else does: a prosperous man leaning in close over the seated judge and pressing three struck silver coins into his hand, the judge's head turned attentively to him at last.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_MOCK + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the two men are turned toward EACH OTHER and their eyelines meet "
            "in the space between them, running LATERALLY ACROSS the frame; the "
            "camera stands well off to one side of that axis and NEITHER MAN'S "
            "PUPILS EVER COME ROUND ONTO IT. "
            "One photograph, 50mm lens, hard flat daylight from screen RIGHT, "
            "the sun well out of frame and NEVER behind any head, " + _GRAIN +
            "A WIDE FULL-LENGTH SCENE WITH TWO PEOPLE, NOT A PORTRAIT: the "
            "camera stands back and to the side at chest height so both men are "
            "in frame from head to sandals. THE JUDGE sits on his stone seat at "
            "the RIGHT, leaning in, his head turned attentively toward the "
            "other man for the first time. A PROSPEROUS TOWNSMAN of about "
            "forty, dressed head to foot in solid DEEP MAROON wool with a DARK "
            "OLIVE sash, stands close over him at the LEFT, bent from the waist "
            "with his own head lowered to the judge's ear. Between them, sharp "
            "and central and unmistakable, the townsman's hand is pressing "
            "THREE separate hand-struck silver coins into the judge's open "
            "palm — three, laid apart and individually countable, each a small "
            "irregular disc bearing a worn ruler's head in profile. Their two "
            "hands and the three coins sit at the exact centre of the frame. "
            "Far behind them at the LEFT, small and entirely out of focus in "
            "the bright rectangle of the opening, ONE lone figure in dark cloth "
            "waits with her back half turned, ignored. NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. Everything light-toned in the picture is dressed "
            "limestone, dust, silver and bare skin."
        ),
    },
    {
        "id": "v2-r038-b16", "out": "s16-lift-a-finger.jpeg",
        "seg": "n3", "window": "56.474-60.385", "wide": True, "jesus": False,
        "locks": ["WIDOW", "JUDGMENT-SEAT", "JUDEAN-LAND", "COURTYARD-GATE",
                  "BACKGROUND-CAST"],
        "char_refs": _WID,
        "narration": "rank, no reason for him to lift a finger.",
        "must_show": "The widow walking out alone across the sunlit square, seen from behind through the chamber opening — sent away, still upright, not defeated.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOURNING + _NO_MOCK + _NO_MODERN_TOWN + _NO_IRONGATE + _NO_GREEN + _GAZE,
        "scene": (
            _BEHIND +
            "One photograph, 35mm lens, hard high midday sun almost overhead "
            "and slightly to the LEFT, throwing a short hard black shadow "
            "directly beneath her, the sun well out of frame, " + _GRAIN +
            "A WIDE FULL-LENGTH SCENE, NOT A PORTRAIT. The camera stands back "
            "inside the shadowed mouth of the gate chamber, chest high, and "
            "shoots out past the plain square-topped opening into the glare. "
            "The near foreground and both upper corners are filled by the dark "
            "dressed-limestone jambs and lintel of that opening, framing the "
            "picture. THE WIDOW IS SEEN ENTIRELY FROM BEHIND, small and "
            "full-length in the middle distance, already three paces out into "
            "the sunlit square and walking away from the camera across the pale "
            "dust, her weight caught mid-stride on one foot. HER BACK IS "
            "STRAIGHT AND HER HEAD IS UP — she is not slumped, not stumbling, "
            "not hunched. HER DARK BROWN HAIR GOING IRON-GREY AT THE TEMPLES IS "
            "PLAINLY VISIBLE, coiled low at the nape and uncovered, the deep "
            "indigo mantle square across her shoulders, the dark umber-brown "
            "tunic to her ankles, her worn flat sandals lifting dust. NO PART "
            "OF HER FACE IS IN FRAME. Beyond her the square runs away to pale "
            "mud-brick house fronts with flat rooflines and empty square "
            "openings, and at most TWO distant people, each a solid dark "
            "saturated mass head to foot, cross it far away with their backs to "
            "her. Everything light-toned is stone, plaster, dust and bare skin."
        ),
    },
    # ===== n4 — THE MONTAGE: one composition, four hours =====================
    {
        "id": "v2-r038-b17", "out": "s17-so-she-came-back.jpeg",
        "seg": "n4", "window": "60.385-63.535", "wide": False, "jesus": False,
        "locks": _DOOR, "char_refs": _WID,
        "narration": "So she came back, and again,",
        "must_show": "FIRST LIGHT. The widow standing waiting at the same gate-chamber opening, framed by the same two jambs from the same camera position that beats 18, 19 and 20 repeat — only the light changes.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOURNING + _NO_MOCK + _NO_MODERN_TOWN + _NO_IRONGATE + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "she is looking INTO the chamber, away to her own right and past "
            "the camera's right shoulder; her head is turned a clear "
            "quarter-turn and her eyeline exits through the RIGHT EDGE of the "
            "frame. HER PUPILS ARE NEVER CENTRED ON THE LENS. "
            "THIS IS THE FIRST OF FOUR PICTURES THAT SHARE ONE FIXED CAMERA "
            "POSITION AND ONE COMPOSITION AND DIFFER ONLY IN THE LIGHT: the "
            "camera stands three paces outside the plain square-topped "
            "gate-chamber opening, at chest height, square on to the wall, so "
            "the two dressed-limestone jambs stand vertical at left and right, "
            "the single flat lintel runs across the top, and the worn hollowed "
            "limestone threshold slab crosses the bottom. "
            "IT IS FIRST LIGHT: thin level early sun coming in low from the far "
            "LEFT, the light cold and clean, long soft blue shadows lying right "
            "across the dust, the sky above the flat roofline pale and clear, "
            "the sun itself well out of frame and NEVER behind her head. "
            "One photograph, 50mm lens, " + _GRAIN +
            "THE WIDOW STANDS ALONE ON THE THRESHOLD SLAB, three-quarter "
            "length, weight even on both feet, hands down and clasped in front "
            "of her, her back straight and her chin level, waiting. She is lit "
            "on the FRONT of her body and face by the low light from the left. "
            "Her dark brown hair going iron-grey at the temples is coiled low "
            "and uncovered, the deep indigo mantle crossed at her breast over "
            "the dark umber-brown tunic. What is on her face is calm patience, "
            "not appeal. The chamber beyond her is cool dark shadow with "
            "nothing readable in it. NOBODY ELSE IS IN THE PICTURE."
        ),
    },
    {
        "id": "v2-r038-b18", "out": "s18-and-again.jpeg",
        "seg": "n4", "window": "63.535-66.855", "wide": False, "jesus": False,
        "locks": _DOOR, "char_refs": _WID,
        "narration": "and again. She would not stop. Every day",
        "must_show": "HARD MIDDAY. The identical framing of the same opening from the same camera position — she is standing in the thin strip of shade under the lintel, the dust white with glare.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOURNING + _NO_MOCK + _NO_MODERN_TOWN + _NO_IRONGATE + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "she is looking INTO the chamber, away to her own right and past "
            "the camera's right shoulder; her head is turned a clear "
            "quarter-turn and her eyeline exits through the RIGHT EDGE of the "
            "frame. HER PUPILS ARE NEVER CENTRED ON THE LENS. "
            "THIS IS THE SECOND OF FOUR PICTURES THAT SHARE ONE FIXED CAMERA "
            "POSITION AND ONE COMPOSITION AND DIFFER ONLY IN THE LIGHT — the "
            "framing is IDENTICAL to the first: the camera three paces outside "
            "the plain square-topped gate-chamber opening at chest height, "
            "square on to the wall, the two dressed-limestone jambs vertical at "
            "left and right, the single flat lintel across the top, the worn "
            "hollowed threshold slab across the bottom. "
            "IT IS HARD MIDDAY: the sun almost directly overhead and blazing, "
            "the dust of the square burnt white with glare, shadows short and "
            "black and pooled straight down beneath everything, heat shimmer "
            "along the ground, the sky above the flat roofline a deep blue "
            "burning almost white at the horizon, the sun well out of frame. "
            "One photograph, 50mm lens, " + _GRAIN +
            "THE WIDOW STANDS ALONE ON THE THRESHOLD SLAB in the one narrow "
            "band of shade the lintel throws, three-quarter length, weight even "
            "on both feet, hands down and clasped in front of her, back "
            "straight, waiting. Sweat shines at her temple and along her throat "
            "and dust has dulled the hem of her tunic. Her dark brown hair "
            "going iron-grey at the temples is coiled low and uncovered, the "
            "deep indigo mantle crossed at her breast over the dark umber-brown "
            "tunic. Her expression is unchanged from the morning — the same "
            "level patience. The chamber beyond her is black shadow. NOBODY "
            "ELSE IS IN THE PICTURE."
        ),
    },
    {
        "id": "v2-r038-b19", "out": "s19-the-same-worn-face.jpeg",
        "seg": "n4", "window": "66.855-70.215", "wide": False, "jesus": False,
        "locks": _DOOR, "char_refs": _WID,
        "narration": "the same worn face at his door, the same steady",
        "must_show": "DUST-WIND AFTERNOON. The same opening and the same camera position, but a hot dry wind is streaming dust across the square and pulling at her mantle — and her face, larger now, is plainly worn out and still absolutely steady.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOURNING + _NO_MOCK + _NO_MODERN_TOWN + _NO_IRONGATE + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "she is looking INTO the chamber, away to her own right and past "
            "the camera's right shoulder; her head is turned a clear "
            "quarter-turn and her eyeline exits through the RIGHT EDGE of the "
            "frame. HER PUPILS ARE NEVER CENTRED ON THE LENS. "
            "THIS IS THE THIRD OF FOUR PICTURES THAT SHARE ONE FIXED CAMERA "
            "POSITION AND ONE COMPOSITION AND DIFFER ONLY IN THE LIGHT AND "
            "WEATHER — the same plain square-topped gate-chamber opening, the "
            "same two dressed-limestone jambs vertical at left and right, the "
            "same flat lintel across the top, the same worn hollowed threshold "
            "slab across the bottom, but the lens is longer so she is larger in "
            "the frame. "
            "IT IS MID-AFTERNOON IN A HOT DRY WIND: the sun high and to the "
            "RIGHT, the air full of streaming pale dust that softens the far "
            "side of the square to a haze, grit moving in visible ribbons "
            "across the ground, the sky bleached almost white, the sun itself "
            "well out of frame and NEVER behind her head. "
            "One photograph, 85mm lens, " + _GRAIN +
            "THE WIDOW STANDS ALONE ON THE THRESHOLD SLAB, from the waist up, "
            "her weight set square against the wind, one hand holding the "
            "streaming edge of her deep indigo mantle down at her shoulder, the "
            "cloth and the loose strands of her hair pulling sideways. HER FACE "
            "IS THE SUBJECT and it is fully lit on its front planes: deeply "
            "sun-darkened olive-brown skin greyed with dust, the fine deep "
            "lines at the outer corner of her eye and either side of her mouth "
            "cut sharp, the flesh under her eyes bruised with tiredness, her "
            "lips dry and cracked — plainly WORN OUT — and her dark eyes "
            "absolutely level and unwavering, her jaw set. Her dark brown hair "
            "going iron-grey at the temples is still coiled low at the nape. "
            "She is not crying and not appealing. The chamber beyond her is "
            "dark. NOBODY ELSE IS IN THE PICTURE."
        ),
    },
    {
        "id": "v2-r038-b20", "out": "s20-asking-for-what-was-right.jpeg",
        "seg": "n4", "window": "70.215-73.349", "wide": False, "jesus": False,
        "locks": _DOOR, "char_refs": _WID,
        "narration": "voice asking for what was right.",
        "must_show": "LAST LIGHT. A tight low shot of her own worn feet in sandals standing on the same hollowed threshold stone, the hollow itself worn deep by feet — the repetition made physical, with no face in the frame.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOURNING + _NO_MOCK + _NO_IRONGATE + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "THIS IS THE FOURTH OF FOUR PICTURES OF THE SAME THRESHOLD, and it "
            "goes right down to the stone itself. "
            "IT IS THE LAST OF THE LIGHT: low level warm sun coming in from the "
            "far RIGHT almost along the ground, throwing one long soft shadow "
            "across the dust and the stone, the light amber and nearly spent, "
            "the sun itself well out of frame. THERE IS NO LAMP, FLAME, FIRE OR "
            "ARTIFICIAL LIGHT ANYWHERE IN THE PICTURE. "
            "One photograph, 50mm lens, the camera set right down at ground "
            "level a pace outside the opening, " + _GRAIN +
            "A TIGHT LOW SHOT WITH NO FACE IN IT ANYWHERE — the picture is "
            "cropped at mid-calf and everything above is entirely OUT OF FRAME. "
            "The frame is filled by the WORN HOLLOWED LIMESTONE THRESHOLD SLAB "
            "running across it, the pale stone dished and polished into a "
            "smooth shallow hollow in the middle by generations of feet, its "
            "grain and old chisel marks raking sharp in the low light, dust "
            "drifted along its edges. STANDING ON IT ARE ONE WOMAN'S TWO FEET, "
            "small, narrow, deeply sun-browned and coated grey with dust, in "
            "plain flat worn leather sandals whose thongs pass up through slits "
            "cut straight through the layered rawhide soles and are knotted and "
            "tucked back through themselves with the loose ends hanging. The "
            "frayed dust-grey hem of a dark umber-brown coarse hand-woven wool "
            "tunic hangs to her ankles. HER FEET ARE PLACED SQUARE AND STILL, "
            "both flat, planted — not shuffling, not turned to leave. Behind "
            "them the dark cool floor of the chamber falls away out of focus."
        ),
    },
    # ===== j1 — Luke 18:4-5, THE JUDGE talking to himself ====================
    {
        "id": "v2-r038-b21", "out": "s21-though-i-fear-not-god.jpeg",
        "seg": "j1", "window": "73.349-77.399", "wide": False, "jesus": False,
        "locks": _COURT, "char_refs": _JUD,
        "narration": "Though I fear not God, nor regard man, Yet",
        "must_show": "The judge alone on his seat with the heel of one hand pressed against his brow — a godless man admitting to himself what he is. This red-letter line belongs to HIM, inside the parable, and Jesus is nowhere in the frame.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_MOCK + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "his head is bowed and turned down and away to his own left; the "
            "camera stands square to his right side, so his eyeline runs DOWN "
            "and out through the LOWER LEFT of the frame. HIS PUPILS NEVER COME "
            "ROUND ONTO THE LENS AXIS. "
            "One photograph, 85mm lens, shallow depth of field, hard flat late "
            "daylight from screen RIGHT, the chamber behind him falling into "
            "cool shadow, the sun well out of frame and NEVER behind his head, "
            + _GRAIN +
            "HE IS THE ONLY PERSON IN THE PICTURE, filling the frame from the "
            "waist up, seated forward on the plain limestone seat with his "
            "elbows on his knees. THE HEEL OF HIS RIGHT HAND IS PRESSED HARD "
            "AGAINST HIS BROW, the fingers spread up into his iron-grey hair "
            "and dragging it out of its comb, his head bowed under the weight "
            "of the hand — plainly A MAN'S HAND, broad, heavy-boned and square. "
            "His full trimmed iron-grey beard and the deep dark rust-red of his "
            "tunic and the deep charcoal-black of his mantle read clearly. What "
            "is on his face is not remorse and not fear: it is BLANK, HONEST "
            "SELF-KNOWLEDGE — the flat expression of a man stating a plain fact "
            "about himself that does not trouble him. He is not praying, not "
            "weeping and not looking upward. Behind him the pale dressed "
            "limestone wall and one reed basket of rolled sheets, out of focus."
        ),
    },
    {
        "id": "v2-r038-b22", "out": "s22-this-widow-troubleth-me.jpeg",
        "seg": "j1", "window": "77.399-81.619", "wide": True, "jesus": False,
        "locks": ["JUDGMENT-SEAT", "JUDGE", "JUDEAN-LAND", "BACKGROUND-CAST"],
        "char_refs": _JUD,
        "narration": "because this widow troubleth me, I will avenge her,",
        "must_show": "The judge giving way: half turned on his seat, jabbing two fingers toward the doorway as he says it to his own clerk, who stands beside him.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_MOCK + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the judge is speaking UP AND ACROSS to the man standing at his "
            "left, whose back is to the camera; the judge's eyeline runs "
            "laterally across the frame to the LEFT and exits through the LEFT "
            "EDGE. HIS PUPILS NEVER COME ROUND ONTO THE LENS AXIS. "
            "One photograph, 35mm lens, hard flat late daylight from screen "
            "RIGHT falling across the front planes of his face, the sun well "
            "out of frame and NEVER behind any head, " + _GRAIN +
            "A WIDE FULL-LENGTH SCENE WITH TWO PEOPLE, NOT A PORTRAIT: the "
            "camera stands back and to the right at chest height so both men "
            "are in frame head to sandals. THE JUDGE sits at the RIGHT of the "
            "frame, half turned on his stone seat toward the LEFT, his body "
            "twisted and one shoulder dropped — caught mid-sentence with his "
            "near hand thrown out and JABBING TWO FINGERS toward the bright "
            "square-topped opening at the far left of the picture, the arm "
            "extended and travelling. His face is exasperated and worn down — "
            "irritated, giving in, NOT shouting, NOT sneering, NOT snarling. At "
            "the LEFT, nearer the camera, HIS CLERK stands seen entirely FROM "
            "BEHIND as a head, shoulders and back, a solid dark charcoal mass "
            "head to foot with a loose papyrus sheet slack in one hand, NO PART "
            "OF HIS FACE IN FRAME. Between and beyond them the empty stone "
            "floor of the chamber runs to the bright opening. Everything "
            "light-toned in the picture is dressed limestone, dust, papyrus and "
            "bare skin."
        ),
    },
    {
        "id": "v2-r038-b23", "out": "s23-lest-she-weary-me.jpeg",
        "seg": "j1", "window": "81.619-85.724", "wide": False, "jesus": False,
        "locks": ["JUDGMENT-SEAT", "JUDGE", "ESTATE-ACCOUNTS", "JUDEAN-LAND"],
        "char_refs": _JUD,
        "narration": "Lest by her continual coming she weary me.",
        "must_show": "The ruling being written: a close macro of a cut reed pen laying short crooked strokes of dark ink on one loose sheet of papyrus resting on a low board, a man's hand steadying it.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_PAPER + _NO_MOCK + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, "
            "hard flat late daylight from screen LEFT raking low across the "
            "sheet so every fibre stands up, the sun well out of frame, "
            + _GRAIN +
            "A TIGHT CLOSE SHOT WITH NO FACE IN IT ANYWHERE. The camera looks "
            "steeply down over a low flat board of adzed timber laid on the "
            "stone floor, and the frame is filled edge to edge by it. On the "
            "board lies ONE single loose leaf of PAPYRUS about the size of two "
            "hands: fibrous, uneven, cream-brown, slightly cockled, its edges "
            "torn rough, its surface showing the crossed fibre grid. A cut REED "
            "PEN with a split nib, held in a broad heavy-boned MAN'S right hand "
            "with trimmed nails, is laying down a short line of DARK "
            "BROWN-BLACK hand-drawn strokes — Hebrew and Aramaic letters, "
            "irregular in size and spacing, sitting crooked on the sheet, the "
            "ink wet and glossy at the nib and faded and uneven where it has "
            "dried. His other hand steadies the corner of the sheet flat. "
            "Beside the board sits a small shallow fired-clay pot of lamp-black "
            "ink and a scrap of dark cloth. The deep dark rust-red wool of his "
            "sleeve runs out of the top of the frame; his shoulders and head "
            "are entirely OUT OF FRAME and no face, eye or gaze appears. The "
            "worn limestone flags fall away out of focus at the edges."
        ),
    },
    # ===== n5 — the grudging concession ======================================
    {
        "id": "v2-r038-b24", "out": "s24-fine-the-judge-said.jpeg",
        "seg": "n5", "window": "85.724-89.414", "wide": False, "jesus": False,
        "locks": _COURT, "char_refs": _JUD,
        "narration": "Fine, the judge finally said. I do not fear God and",
        "must_show": "The judge's face at the moment of giving in: mouth set flat, eyes turned away to the side, sour and entirely ungracious about it.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_MOCK + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            _PROFILE +
            "One photograph, 85mm lens, shallow depth of field, hard flat late "
            "daylight from screen LEFT falling across the front planes of his "
            "face, the sun well out of frame and NEVER behind his head, "
            + _GRAIN +
            "HE IS THE ONLY PERSON IN THE PICTURE, filling the frame from the "
            "shoulders up, seated. The camera is square to his left side. His "
            "head is turned to the LEFT and tipped slightly back, his eyeline "
            "running level and away and exiting through the LEFT EDGE. His "
            "profile reads completely: the heavy jaw under the full carefully "
            "trimmed iron-grey beard squared at the jaw, the broad straight "
            "nose, the thick dark brow, the iron-grey hair combed back off the "
            "high forehead and cut to the middle of his neck, now slightly "
            "disordered where his hand went through it. His mouth is pressed "
            "into a flat line and one nostril is drawn — SOUR, GRUDGING, "
            "UNGRACIOUS, a man conceding something he resents conceding — but "
            "NOT snarling, NOT baring his teeth, NOT sneering, NOT comic. The "
            "deep charcoal-black wool of his mantle fills the lower corner over "
            "the deep dark rust-red tunic. Behind him the pale dressed "
            "limestone wall, far out of focus. NOBODY ELSE IS IN THE PICTURE."
        ),
    },
    {
        "id": "v2-r038-b25", "out": "s25-she-is-wearing-me-out.jpeg",
        "seg": "n5", "window": "89.414-93.214", "wide": False, "jesus": False,
        "locks": _COURT, "char_refs": _JUD,
        "narration": "I do not care about her, but she is wearing me out.",
        "must_show": "The judge slumped back against the chamber wall with his head tipped against the stone and his eyes shut, worn down — a picture of exhaustion, not of repentance.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_MOCK + _NO_MODERN_LAMP + _NO_DEATH + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "HIS EYES ARE CLOSED, so no gaze exists at all; his head is tipped "
            "back and turned slightly away to his own right and the camera "
            "stands well off to his left side. "
            "One photograph, 50mm lens, hard flat late daylight from screen "
            "RIGHT, the chamber falling to deep cool shadow, the sun well out "
            "of frame and NEVER behind his head, " + _GRAIN +
            "HE IS THE ONLY PERSON IN THE PICTURE, seen from the knees up, "
            "seated on the plain limestone seat and SLUMPED BACK against the "
            "big dry-laid limestone blocks of the chamber wall, his shoulders "
            "down, his spine curved, both broad hands dropped loose and open "
            "palm-up on his thighs, the crown of his head resting back against "
            "the stone. His face is tipped up a little and HIS EYES ARE SHUT, "
            "his mouth slightly open, his full trimmed iron-grey beard and "
            "combed-back iron-grey hair plainly readable, the hair now "
            "disordered. WHAT THIS PICTURE SHOWS IS EXHAUSTION AND DEFEAT BY "
            "SHEER PERSISTENCE — not remorse, not prayer, not sleep, not "
            "illness, and he is plainly alive and breathing. The deep dark "
            "rust-red tunic and deep charcoal-black mantle fall slack around "
            "him. On the floor beside the seat lies one loose papyrus sheet, "
            "face up. NOBODY ELSE IS IN THE PICTURE."
        ),
    },
    {
        "id": "v2-r038-b26", "out": "s26-just-to-be-rid-of-her.jpeg",
        "seg": "n5", "window": "93.214-96.599", "wide": False, "jesus": False,
        "locks": ["JUDGMENT-SEAT", "WIDOW", "ESTATE-ACCOUNTS", "JUDEAN-LAND"],
        "char_refs": _WID,
        "narration": "I will give her justice just to be rid of her.",
        "must_show": "The widow's own small brown hands closing around the loose written sheet as it is put into them — the ruling arriving, shown as a handover between two pairs of hands with no face in frame.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_PAPER + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, "
            "hard flat late daylight from screen LEFT, the sun well out of "
            "frame, " + _GRAIN +
            "A TIGHT CLOSE SHOT WITH NO FACE IN IT ANYWHERE — the picture is "
            "cropped at the breastbone on both people and every head is "
            "entirely OUT OF FRAME. At the centre of the frame, sharp, ONE "
            "single loose leaf of PAPYRUS about the size of two hands is "
            "passing between two pairs of hands: fibrous, uneven, cream-brown, "
            "slightly cockled, its edges torn rough, carrying a few short "
            "crooked lines of dark brown hand-drawn reed-pen strokes in Hebrew "
            "and Aramaic letters. FROM THE LEFT, one broad heavy-boned MAN'S "
            "hand in a DARK CHARCOAL wool sleeve is releasing it, the fingers "
            "already opening. FROM THE RIGHT, BOTH OF THE WIDOW'S HANDS are "
            "closing around it — small, narrow-boned, deeply sun-browned, "
            "sinewy, the knuckles enlarged, the nails short and clean, "
            "unmistakably A WOMAN'S HANDS and unmistakably smaller than his — "
            "the fingertips of one just curling over the top edge, the other "
            "coming up flat beneath it. The dark umber-brown coarse wool of her "
            "sleeve and the deep indigo of her mantle fill the right of the "
            "frame. Her grip is careful, not snatching. The worn pale limestone "
            "flags fall away far out of focus behind."
        ),
    },
    # ===== j2 — Luke 18:6-7, JESUS speaking as himself =======================
    {
        "id": "v2-r038-b27", "out": "s27-hear-what-the-unjust-judge-saith.jpeg",
        "seg": "j2", "window": "96.599-100.229", "wide": False, "jesus": True,
        "ref": REF, "locks": ["OLIVE-YARD", "JUDEAN-LAND"],
        "narration": "Hear what the unjust judge saith, And shall not God",
        "must_show": "Jesus back in the press yard, close, in profile, mid-sentence — the moment he turns the parable around on his listeners. This line is his own.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            _PROFILE +
            "One photograph, 85mm lens, shallow depth of field, long low "
            "late-afternoon sun coming in from screen LEFT and falling warm "
            "across the front planes of his face, the sun itself well out of "
            "frame and NEVER behind his head, and no bright rim, edge or "
            "outline anywhere around his hair or shoulders, " + _GRAIN +
            "HE IS THE ONLY PERSON IN THE PICTURE, filling the frame from the "
            "chest up, seated on the low limestone kerb of the press bed. The "
            "camera is square to his left side. His head is turned to the LEFT "
            "toward the listeners who sit out past the frame edge, his chin a "
            "little lifted, his mouth open on a word — mid-sentence, caught "
            "speaking. His face reads completely in profile: the aquiline nose, "
            "the strong dark brow, the high cheekbone, the full dark brown "
            "beard, the long thick tousled dark brown wavy hair with warm "
            "sun-bleached bronze lights falling below the shoulder. His "
            "expression is warm and direct and entirely unhurried. His near "
            "hand is lifted just into the bottom of the frame, open. Behind "
            "him, far out of focus, the round grey crushing stone of the olive "
            "press and the pale plastered mud-brick wall of the yard, with the "
            "long shadow of the press beam lying across it. NOBODY ELSE IS IN "
            "THE PICTURE."
        ),
    },
    {
        "id": "v2-r038-b28", "out": "s28-which-cry-day-and-night.jpeg",
        "seg": "j2", "window": "100.229-103.509", "wide": False, "jesus": False,
        "locks": ["VILLAGE-LANE", "JUDEAN-LAND"],
        "narration": "avenge his own elect, Which cry day and night unto",
        "must_show": "An ordinary Judean villager on his own flat rooftop at the very end of the day, kneeling with his hands open and his face lifted — one person praying, and nothing else. Nothing divine is depicted.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOCK + _NO_MODERN_TOWN + _NO_MOURNING + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the camera stands BEHIND AND TO THE SIDE of the kneeling man at "
            "his own shoulder height, so he is seen as a back and a lost "
            "profile; his face is turned up and AWAY from the lens toward the "
            "far horizon and his eyeline exits through the upper LEFT of the "
            "frame. NO PART OF HIS PUPILS IS EVER ON THE LENS AXIS. "
            "One photograph, 50mm lens, the very last level warm light of the "
            "day coming in low from the far LEFT along the rooftops, the sky "
            "above deepening from warm amber at the horizon to clear blue "
            "overhead, the sun itself already down and well out of frame. THERE "
            "IS NO LAMP, CANDLE, TORCH, FIRE OR ARTIFICIAL LIGHT ANYWHERE IN "
            "THE PICTURE and no light source of any kind behind his head. "
            + _GRAIN +
            "HE IS THE ONLY PERSON IN THE PICTURE: one ordinary Judean man of "
            "about fifty with warm sun-darkened olive-brown Middle Eastern "
            "skin, SHORT grey-black hair and a SHORT grey beard, dressed head "
            "to foot in solid DARK UMBER hand-woven wool with a DEEP INDIGO "
            "mantle, kneeling on a plain reed mat on the packed-earth flat roof "
            "of a mud-brick house, three-quarter length, seen from behind and "
            "to the side. His back is straight, his face is lifted toward the "
            "amber horizon and BOTH HANDS ARE OPEN AND RAISED to about the "
            "height of his own chest, palms upward. Around and below him the "
            "flat rooflines of the village step away into blue shadow with the "
            "bare terraced hills beyond. NOTHING ELSE IS IN THE SKY — no "
            "figure, no face, no light, no shaft, no beam, no cloud formation "
            "and no bird."
        ),
    },
    {
        "id": "v2-r038-b29", "out": "s29-though-he-bear-long.jpeg",
        "seg": "j2", "window": "103.509-107.459", "wide": True, "jesus": True,
        "ref": REF, "locks": _YARD,
        "narration": "him, Though he bear long with them?",
        "must_show": "Jesus in the press yard putting the question to the villagers, hands open — a wide of the whole group with the camera behind the listeners.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            _BEHIND +
            "One photograph, 35mm lens, long low late-afternoon sun raking in "
            "from the RIGHT across the packed earth of the yard, the sun well "
            "out of frame and NEVER behind any head, " + _GRAIN +
            "A WIDE FULL-LENGTH SCENE WITH MULTIPLE PEOPLE, NEVER A PORTRAIT: "
            "the camera is far enough back that all of them are visible head to "
            "sandals. THREE dark-clad village listeners fill the near lower "
            "third of the frame as heads, shoulders and BACKS seen entirely "
            "FROM BEHIND, sitting on reed mats and on the stone kerb of the "
            "crushing basin, one with a hand lifted to his own beard, and NOT "
            "ONE OF THEIR FACES IS TURNED TOWARD THE LENS. Jesus sits facing "
            "them on the far side of the yard, right of centre, full length on "
            "the low limestone kerb, leaning forward with BOTH HANDS TURNED "
            "PALM-UP AND OPEN in front of him — the gesture of a question just "
            "asked and left hanging. His head is turned to his own right toward "
            "the nearest listener and his gaze travels laterally and exits the "
            "picture through the RIGHT EDGE, never onto the lens. Behind them "
            "the timber press beam in its stone socket, the stacked reed "
            "pressing mats, two fired-clay jars by the oil-darkened collecting "
            "hollow, and the gnarled grey olive trunk in the corner. THE ONLY "
            "PALE WOOL IN THE WHOLE PICTURE IS HIS OWN ROBE; every other person "
            "is a solid dark saturated mass of indigo, umber, rust, olive, "
            "charcoal or maroon from edge to edge, in focus and out of focus "
            "alike."
        ),
    },
    # ===== n6 — the contrast: God is not that judge ==========================
    {
        "id": "v2-r038-b30", "out": "s30-listen-to-what-that-cold-judge-did.jpeg",
        "seg": "n6", "window": "107.459-110.749", "wide": False, "jesus": True,
        "ref": REF, "locks": ["OLIVE-YARD", "LISTENERS", "JUDEAN-LAND"],
        "narration": "Listen to what even that cold judge finally did,",
        "must_show": "Jesus close and quiet at the near edge of frame, with two listeners' faces visible beyond him — their eyes converging on him well off the camera axis.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the camera stands at JESUS'S OWN RIGHT SHOULDER, close in and just "
            "behind him. He is seen from behind and to the side as a "
            "three-quarter back and a lost profile with NO PART OF HIS PUPILS "
            "ON THE LENS AXIS. The two listeners facing him ARE seen face-on to "
            "the camera, but THEIR EYES ARE ON HIM, not on the lens: because he "
            "stands at the near RIGHT of the frame, both of their eyelines run "
            "clearly to the RIGHT and PAST the camera, well off its axis, and "
            "NEITHER PAIR OF PUPILS IS CENTRED ON IT. "
            "One photograph, 85mm lens, shallow depth of field, long low "
            "late-afternoon sun from screen RIGHT falling on the front planes "
            "of both listeners' faces, the sun well out of frame and NEVER "
            "behind any head, " + _GRAIN +
            "The near right quarter of the frame is filled, close and softly "
            "out of focus, by Jesus's shoulder and the back of his head — the "
            "long thick tousled dark brown wavy hair with warm sun-bleached "
            "bronze lights, and the cream wool of his robe — with his near hand "
            "lifted low and open at the edge of the frame. Sharp in the middle "
            "distance, TWO village listeners sit on the ground and on the stone "
            "kerb looking up at him: a woman of about thirty-five in solid DARK "
            "OLIVE wool with her hair covered by a DEEP INDIGO wrap, and a man "
            "of about forty-five in solid DEEP RUST with a dark beard, both "
            "leaning slightly forward, absolutely still, listening. Behind them "
            "the pale plastered mud-brick wall and the round grey crushing "
            "stone. HIS ROBE IS THE ONLY PALE WOOL IN THE PICTURE."
        ),
    },
    {
        "id": "v2-r038-b31", "out": "s31-now-think-about-god.jpeg",
        "seg": "n6", "window": "110.749-114.629", "wide": False, "jesus": False,
        "locks": ["FATHER", "VILLAGE-LANE", "COURTYARD-GATE", "JUDEAN-LAND"],
        "narration": "Jesus said. Now think about God, if a man who cares for no",
        "must_show": "THE FATHER ANCHOR. One ordinary Judean village father alone in his own doorway in early morning light, seen in strict side-on profile, his head just turning toward a sound outside — his whole face clearly readable. This frame defines his face for every later picture. He is a man, never a depiction of God.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_IRONGATE + _NO_MOCK + _NO_MODERN_TOWN + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            _PROFILE +
            "One photograph, 85mm lens, shallow depth of field, warm level "
            "early-morning sun coming in from screen LEFT and falling full on "
            "the front planes of his face, the sun itself well out of frame and "
            "NEVER behind his head, and no bright rim, edge or outline anywhere "
            "around his hair, head or shoulders, " + _GRAIN +
            "HE IS THE ONLY PERSON IN THE PICTURE and he fills the frame from "
            "the waist up, standing just inside the plain square-topped doorway "
            "of his own small mud-brick house with one hand flat against the "
            "mud-plastered jamb. The camera is square to his right side. HIS "
            "HEAD HAS JUST TURNED to the LEFT toward a sound out in the lane — "
            "the movement caught, not completed, the neck tendon showing. His "
            "face is fully lit and reads completely: warm sun-darkened "
            "olive-brown skin, an open weathered face, laugh lines at the outer "
            "corner of a warm dark brown eye, a broad nose, a wide mouth "
            "resting just short of a smile, a SHORT full dark brown beard, and "
            "SHORT thick dark brown hair cut close above the ear and at the "
            "nape, plainly visible. He wears one knee-length WARM DEEP "
            "RUST-BROWN coarse hand-woven wool tunic with a DARK OLIVE folded "
            "sash. WHAT IS ON HIS FACE IS IMMEDIATE GLADNESS AND ATTENTION — a "
            "man who was already listening for that sound. He is not solemn, "
            "not stern, not grand, not reluctant. Behind him the dark interior "
            "of the house falls out of focus. NOBODY ELSE IS IN THE PICTURE."
        ),
    },
    {
        "id": "v2-r038-b32", "out": "s32-the-one-who-keeps-coming.jpeg",
        "seg": "n6", "window": "114.629-118.069", "wide": True, "jesus": False,
        "locks": _FATHERS, "char_refs": _FAT,
        "narration": "one will still give justice to the one who keeps coming, how much",
        "must_show": "The father crossing his own room in two strides toward the doorway at the first sound — full length, mid-stride, already moving, in warm morning light.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_IRONGATE + _NO_MOCK + _NO_MODERN_TOWN + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            _BEHIND +
            "One photograph, 35mm lens, warm level early-morning sun blazing in "
            "through the plain square-topped doorway at the far side of the "
            "room and lying across the beaten earth floor in one long slab, the "
            "sun itself well out of frame, " + _GRAIN +
            "A WIDE FULL-LENGTH SCENE, NOT A PORTRAIT: the camera stands back "
            "in the dark corner of the small room behind him, chest high, and "
            "shoots past him toward the bright doorway. The near foreground is "
            "filled by the dark mud-plastered wall and a stacked reed basket, "
            "out of focus. THE FATHER IS SEEN FROM BEHIND AND SLIGHTLY TO THE "
            "SIDE, full length and CAUGHT MID-STRIDE two paces from the "
            "doorway, his weight forward on the leading foot with the trailing "
            "heel lifted clear of the floor, one arm swinging back — he is "
            "plainly MOVING FAST toward the door, not standing in it. His SHORT "
            "thick dark brown hair is plainly visible at the crown and the "
            "nape, his warm deep rust-brown knee-length tunic and dark olive "
            "sash clear against the light, and NO PART OF HIS FACE IS TURNED "
            "TOWARD THE LENS. Beyond him the empty bright doorway opens onto "
            "the sunlit dust of the village lane and one pale mud-brick house "
            "front with a flat roofline. THE DOORWAY IS COMPLETELY EMPTY — "
            "there is no door leaf, no gate, no barrier and nobody standing in "
            "it. Everything light-toned in the picture is plaster, stone, dust "
            "and bare skin."
        ),
    },
    {
        "id": "v2-r038-b33", "out": "s33-your-father-who-loves-you.jpeg",
        "seg": "n6", "window": "118.069-121.781", "wide": False, "jesus": False,
        "locks": _FATHERS, "char_refs": _FAT,
        "narration": "more will your father who loves you hear you?",
        "must_show": "The father down on one knee in his own doorway, his head bent right down level with a small child's, listening to her with his whole attention — the plain human picture the narration draws.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_IRONGATE + _NO_MOCK + _NO_MODERN_TOWN + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the man and the child are turned toward EACH OTHER and their "
            "eyelines meet in the narrow space between their two faces, running "
            "laterally across the frame; the camera stands well off to the side "
            "of that axis at their own height, and NEITHER PAIR OF PUPILS EVER "
            "COMES ROUND ONTO IT. "
            "One photograph, 85mm lens, shallow depth of field, warm level "
            "early-morning sun from screen LEFT falling on the front planes of "
            "both faces, the sun well out of frame and NEVER behind either "
            "head, " + _GRAIN +
            "TWO PEOPLE AND NOBODY ELSE. THE FATHER is down on one knee on the "
            "worn stone threshold of his own doorway at the RIGHT of the frame, "
            "seen in three-quarter profile, his back rounded and his head bent "
            "right down so his face is LEVEL WITH THE CHILD'S — his SHORT dark "
            "brown hair and SHORT full dark brown beard clear, his warm deep "
            "rust-brown tunic pulled tight across the shoulder, one broad "
            "calloused brown hand resting lightly on the child's upper arm. THE "
            "CHILD, a girl of about six with warm sun-darkened olive-brown "
            "Middle Eastern skin and dark hair braided back, in a plain "
            "knee-length DARK OLIVE wool tunic and barefoot, stands facing him "
            "at the LEFT in profile, close, both her small hands lifted and "
            "moving as she tells him something. HIS WHOLE ATTENTION IS ON HER "
            "and his face is warm and completely unhurried. Behind them the "
            "sunlit dust of the lane and a pale mud-brick wall, far out of "
            "focus. NEITHER OF THEM WEARS CREAM OR ANY PALE CLOTH."
        ),
    },
    # ===== jv8 — Luke 18:8, JESUS speaking as himself ========================
    {
        "id": "v2-r038-b34", "out": "s34-avenge-them-speedily.jpeg",
        "seg": "jv8", "window": "121.781-125.611", "wide": False, "jesus": True,
        "ref": REF, "locks": ["OLIVE-YARD", "JUDEAN-LAND"],
        "narration": "I tell you that He will avenge them speedily.",
        "must_show": "Jesus saying the decisive half of the verse — leaning in, one hand come down flat and open, certainty on his face.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the camera stands well out to his LEFT and slightly forward, so he "
            "is seen in near-profile with the near cheek broad and the far eye "
            "narrowed behind the bridge of his nose; his eyeline runs laterally "
            "across the frame to the RIGHT and exits through the RIGHT EDGE. "
            "HIS PUPILS NEVER COME ROUND ONTO THE LENS AXIS. "
            "One photograph, 85mm lens, shallow depth of field, long low "
            "late-afternoon sun from screen RIGHT falling warm across the front "
            "planes of his face, the sun well out of frame and NEVER behind his "
            "head, and no bright rim, edge or outline around his hair or "
            "shoulders anywhere, " + _GRAIN +
            "HE IS THE ONLY PERSON IN THE PICTURE, filling the frame from the "
            "waist up, seated forward on the low limestone kerb of the press "
            "bed and LEANING IN toward the listeners out past the right frame "
            "edge, his weight on one forearm across his knee. HIS OTHER HAND "
            "HAS JUST COME DOWN FLAT AND OPEN, palm down, onto his own thigh — "
            "the small decisive gesture of a plain statement, caught at the "
            "moment of contact. His face reads clearly: the aquiline nose, the "
            "strong dark brow, the full dark brown beard, the long tousled dark "
            "brown wavy hair with warm bronze lights. His expression is calm, "
            "warm and completely certain — never stern, never severe. Behind "
            "him, far out of focus, the timber press beam and the pale "
            "plastered wall of the yard. NOBODY ELSE IS IN THE PICTURE."
        ),
    },
    {
        "id": "v2-r038-b35", "out": "s35-when-the-son-of-man-cometh.jpeg",
        "seg": "jv8", "window": "125.611-128.331", "wide": False, "jesus": True,
        "ref": REF, "locks": ["OLIVE-YARD", "JUDEAN-LAND"],
        "narration": "Nevertheless, when the Son of Man cometh,",
        "must_show": "Jesus going quiet — his head turned away from the listeners toward the open gap in the yard wall and the far hills, the question already forming.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            _PROFILE +
            "One photograph, 85mm lens, shallow depth of field, long low "
            "late-afternoon sun from screen LEFT falling warm across the front "
            "planes of his face, the sun well out of frame and NEVER behind his "
            "head, and no bright rim, edge or outline around his hair, head or "
            "shoulders anywhere, " + _GRAIN +
            "HE IS THE ONLY PERSON IN THE PICTURE, filling the frame from the "
            "chest up, seated. The camera is square to his right side. His head "
            "is turned right away to the LEFT, away from the listeners and "
            "toward the open square-topped gap in the yard wall, his chin level "
            "and his mouth closed — he has stopped speaking. His eyeline runs "
            "level and far and exits through the LEFT EDGE, resting on "
            "something a long way off. His face reads completely in profile: "
            "the aquiline nose, the strong dark brow, the high cheekbone, the "
            "full dark brown beard, the long tousled dark brown wavy hair with "
            "warm bronze lights falling past his shoulder. His expression is "
            "quiet and sober and unguarded — thoughtful, never grim, never "
            "sad-eyed theatre. Behind him, thrown right out of focus, the "
            "warm-lit plastered wall of the yard and the bright gap in it with "
            "the pale bare terraced hills beyond. NOBODY ELSE IS IN THE "
            "PICTURE."
        ),
    },
    {
        "id": "v2-r038-b36", "out": "s36-shall-he-find-faith.jpeg",
        "seg": "jv8", "window": "128.331-131.570", "wide": False, "jesus": False,
        "locks": ["OLIVE-YARD", "LISTENERS", "JUDEAN-LAND"],
        "narration": "shall He find faith on the earth?",
        "must_show": "The question landing on the listeners: two of their faces, sober and silent, eyes fixed on the speaker off to the side of the camera.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOCK + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the man they are listening to sits FAR OUT PAST THE LEFT EDGE of "
            "the picture and below the camera. Both heads are turned a clear "
            "quarter-turn to their own right and both eyelines run diagonally "
            "across and DOWN, exiting through the LEFT EDGE of the frame. "
            "NEITHER PAIR OF PUPILS IS EVER CENTRED ON THE LENS AND NEITHER "
            "PERSON LOOKS INTO THE CAMERA. "
            "One photograph, 85mm lens, shallow depth of field, long low "
            "late-afternoon sun from screen LEFT falling on the front planes of "
            "both faces, the sun well out of frame and NEVER behind either "
            "head, " + _GRAIN +
            "TWO PEOPLE AND NOBODY ELSE, both from the chest up, seated close "
            "together on a reed mat. NEARER THE CAMERA, a woman of about "
            "thirty-five with warm sun-darkened olive-brown Middle Eastern "
            "skin, her dark hair covered by a DEEP INDIGO wrap and her body in "
            "solid DARK OLIVE wool, her lips slightly parted, absolutely still. "
            "BEHIND AND BESIDE HER, a little out of focus, a man of about sixty "
            "in solid DARK CHARCOAL with a full grey-white beard, his brows "
            "drawn together. WHAT IS ON BOTH FACES IS A SOBER, SILENT QUESTION "
            "TURNED INWARD — not fear, not alarm, not dread. Behind them the "
            "pale plastered mud-brick wall of the yard, far out of focus. "
            "NEITHER OF THEM WEARS CREAM OR ANY PALE CLOTH."
        ),
    },
    # ===== n7b — he will not drag his feet; the quiet question ===============
    {
        "id": "v2-r038-b37", "out": "s37-he-will-act-and-quickly.jpeg",
        "seg": "n7b", "window": "131.570-136.420", "wide": True, "jesus": True,
        "ref": REF, "locks": _YARD,
        "narration": "He will not drag his feet, Jesus said. He will act, and quickly.",
        "must_show": "A wide of the whole yard in the long last light with Jesus mid-gesture among the listeners — the place itself, unhurried and warm, the pressing done for the day.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            _BEHIND +
            "One photograph, 28mm lens, long low late-afternoon sun raking "
            "right across the yard from the RIGHT, the shadow of the wall lying "
            "long over the packed earth, the light deep amber, the sun itself "
            "well out of frame and NEVER behind any head, " + _GRAIN +
            "A WIDE FULL-LENGTH SCENE WITH MULTIPLE PEOPLE, NEVER A PORTRAIT: "
            "the camera stands back at the far corner of the yard, chest high, "
            "and the whole working yard is in frame — the circular grey "
            "limestone crushing basin with its upright edge-runner stone on its "
            "timber axle, the long hewn press beam lying level in its stone "
            "socket with the rough stone weight lashed to the far end, the "
            "stacked reed pressing mats, the oil-darkened collecting hollow "
            "with two fired-clay jars beside it, a reed basket of olives "
            "against the wall, and the gnarled grey olive trunk in the corner. "
            "FOUR village listeners fill the near lower left as heads, "
            "shoulders and BACKS seen entirely from behind, sitting on mats and "
            "on the stone kerb, and NOT ONE FACE IS TURNED TOWARD THE LENS. "
            "Jesus sits full length on the far side of the press bed at the "
            "RIGHT of centre, small in the wide frame, caught mid-gesture with "
            "one hand turned outward from the wrist toward them, his head "
            "turned to his own left so his gaze crosses the frame and exits "
            "through the LEFT EDGE. THE ONLY PALE WOOL IN THE WHOLE PICTURE IS "
            "HIS OWN ROBE; every other person is a solid dark saturated mass "
            "head to foot."
        ),
    },
    {
        "id": "v2-r038-b38", "out": "s38-one-more-question.jpeg",
        "seg": "n7b", "window": "136.420-140.500", "wide": False, "jesus": False,
        "locks": ["OLIVE-YARD", "LISTENERS", "JUDEAN-LAND"],
        "narration": "And then he asked one more question, almost quietly. When the Son of Man",
        "must_show": "One young listener's face, arrested — a man of about twenty-five who has just been handed a question he cannot put down.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOCK + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the speaker sits FAR OUT PAST THE RIGHT EDGE of the picture and "
            "below the camera. His head is turned a clear quarter-turn to his "
            "own left and his eyeline runs diagonally across and DOWN, exiting "
            "through the RIGHT EDGE. HIS PUPILS ARE NEVER CENTRED ON THE LENS "
            "AND HE NEVER LOOKS INTO THE CAMERA. "
            "One photograph, 105mm lens, very shallow depth of field, long low "
            "late-afternoon sun from screen RIGHT falling warm along the front "
            "planes of his face, the sun well out of frame and NEVER behind his "
            "head, " + _GRAIN +
            "A TIGHT PORTRAIT of ONE man of about twenty-five filling the frame "
            "from the shoulders up, seated. Warm sun-darkened olive-brown "
            "Middle Eastern skin, a short dark beard just filled in, thick "
            "black hair, dark brown eyes. He wears a solid DEEP RUST hand-woven "
            "wool tunic with the coarse warp-and-weft plainly visible at the "
            "shoulder. HE IS COMPLETELY STILL AND HIS LIPS ARE PARTED — caught "
            "in the half-second after a question lands, before any answer. His "
            "brows are drawn very slightly together and there is dust and a "
            "smear of crushed olive on his cheekbone from the day's work. "
            "Behind him, thrown right out of focus, the amber-lit plastered "
            "mud-brick wall of the yard. NOBODY ELSE IS IN THE PICTURE."
        ),
    },
    {
        "id": "v2-r038-b39", "out": "s39-will-he-find-anybody.jpeg",
        "seg": "n7b", "window": "140.500-145.005", "wide": True, "jesus": False,
        "locks": ["OLIVE-YARD", "COURTYARD-GATE", "ANCIENT-ROAD", "JUDEAN-LAND"],
        "narration": "comes back, will he find anybody still believing that?",
        "must_show": "The question left standing open: the plain square-topped gap in the yard wall looking out on an empty dust road and the bare Judean hills in the last light, with no person in the picture at all.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_IRONGATE + _NO_MODERN_TOWN + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "One photograph, 50mm lens, the last low level sun coming in almost "
            "along the ground from the far LEFT, the shadows enormously long, "
            "the light deep amber, the sky above deepening to clear blue, the "
            "sun itself well out of frame, " + _GRAIN +
            "AN EMPTY ARCHITECTURAL WIDE SHOT WITH NO PEOPLE IN IT AT ALL. The "
            "camera stands inside the olive-press yard, chest high and back "
            "from the wall, looking straight out through the one opening AWAY "
            "FROM the yard, with the press and the whole yard behind the "
            "camera. The "
            "near frame is filled by that opening: two jambs of dressed "
            "limestone blocks standing vertical at left and right, ONE SINGLE "
            "FLAT LIMESTONE LINTEL laid straight across the top so the opening "
            "is SQUARE-TOPPED, and a worn hollowed limestone threshold slab "
            "across the bottom, the mud-plastered wall around them warm and "
            "raking in the low light. THE OPENING IS COMPLETELY EMPTY — no "
            "door, no leaf, no gate, no barrier and nobody standing in it. "
            "Through it: bare packed earth and pale dust worn hollow by feet "
            "running away as a track, loose stones kicked to the sides, "
            "grey-green thorn scrub, and beyond it the bare rounded terraced "
            "limestone hills of Judea going hazy and blue with distance under "
            "the last of the light. NOTHING MOVES OUT THERE AND NOBODY IS ON "
            "THE ROAD. Everything light-toned in the picture is stone, plaster "
            "and dust."
        ),
    },
    # ===== n7 — the whole point =============================================
    {
        "id": "v2-r038-b40", "out": "s40-god-is-not-that-judge.jpeg",
        "seg": "n7", "window": "145.005-148.275", "wide": False, "jesus": False,
        "locks": ["JUDGMENT-SEAT", "JUDEAN-LAND"],
        "narration": "Here is the whole point, God is not that judge.",
        "must_show": "The judge's stone seat standing completely EMPTY in the cold shadowed gate chamber — the man himself gone from the picture entirely, which is exactly what the line says.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_COURTROOM + _NO_MODERN_LAMP + _NO_DEATH + _GAZE,
        "scene": (
            "One photograph, 50mm lens, flat cold indirect daylight from one "
            "plain square-topped opening off to screen LEFT, the rest of the "
            "chamber in deep cool shadow, the sun itself well out of frame and "
            "no other light source anywhere, " + _GRAIN +
            "THERE IS NO PERSON IN THIS PICTURE AT ALL — not in the foreground, "
            "not in the background, not in focus, not blurred, not in a "
            "doorway, not as a shadow. The camera stands square on and back, "
            "chest high. At the centre of the frame, against the big dry-laid "
            "pale limestone blocks of the back wall, stands THE PLAIN "
            "RECTANGULAR BLOCK OF DRESSED LIMESTONE that is the judge's seat, "
            "knee-high, with its folded dark wool cushion still dented in the "
            "middle where somebody sat. IT IS EMPTY. In front of it the worn "
            "limestone flags run bare to the bottom of the frame with a drift "
            "of pale dust along the joints. To one side sits a hand-woven reed "
            "basket with three rolled papyrus sheets standing in it, and beyond "
            "it a plain fired-clay jar. THE ROOM IS COLD, STILL AND ORDINARY — "
            "not sinister, not ruined, not haunted, not lit by anything but "
            "flat daylight. Nothing hangs on the walls."
        ),
    },
    {
        "id": "v2-r038-b41", "out": "s41-he-is-not-reluctant.jpeg",
        "seg": "n7", "window": "148.275-151.695", "wide": True, "jesus": False,
        "locks": _FATHERS, "char_refs": _FAT,
        "narration": "He is not reluctant. He is not annoyed by you.",
        "must_show": "The father's doorway standing wide open in warm early morning, with the father himself out on the threshold, arms loose at his sides, plainly waiting — the exact opposite picture of the empty cold seat before it.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_IRONGATE + _NO_MOCK + _NO_MODERN_TOWN + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "he is looking away down the lane to his own left, so his head is "
            "turned a clear quarter-turn from the camera and his eyeline runs "
            "laterally across and exits through the LEFT EDGE. HIS PUPILS NEVER "
            "COME ROUND ONTO THE LENS AXIS. "
            "One photograph, 35mm lens, warm level early-morning sun coming in "
            "low from the LEFT along the lane and falling full on the front of "
            "him and on the house wall, the sun itself well out of frame and "
            "NEVER behind his head, and no bright rim, edge or outline around "
            "his hair or shoulders, " + _GRAIN +
            "A WIDE FULL-LENGTH SCENE, NOT A PORTRAIT: the camera stands out in "
            "the lane, back and low, so the whole front of the small mud-brick "
            "house is in frame — pale mud plaster over a footing of undressed "
            "field stone, a flat roofline of poles and packed earth, one small "
            "empty square opening high in the wall, and the plain SQUARE-TOPPED "
            "doorway with its two dressed jambs, single flat lintel and worn "
            "hollowed threshold slab. THE DOORWAY IS WIDE OPEN AND ITS TIMBER "
            "LEAF IS PUSHED RIGHT BACK FLAT AGAINST THE INSIDE OF THE WALL, so "
            "the opening is entirely clear and the dark cool interior shows "
            "through. THE FATHER STANDS OUT ON THE THRESHOLD SLAB IN THE "
            "SUNLIGHT, full length, seen in three-quarter profile, his weight "
            "even on both bare feet, BOTH ARMS HANGING LOOSE AND OPEN AT HIS "
            "SIDES with the palms turned slightly forward — not folded, not on "
            "his hips, not barring the way. His SHORT dark brown hair and SHORT "
            "full dark brown beard read clearly and he wears the warm deep "
            "rust-brown knee-length tunic and dark olive sash. He is looking "
            "away up the lane, plainly waiting for somebody, and his face is "
            "easy and glad. THE LANE IN FRONT OF HIM IS EMPTY. Everything "
            "light-toned in the picture is plaster, stone, dust and bare skin."
        ),
    },
    {
        "id": "v2-r038-b42", "out": "s42-he-already-loves-you.jpeg",
        "seg": "n7", "window": "151.695-154.915", "wide": False, "jesus": False,
        "locks": _HOME, "char_refs": _WID,
        "narration": "He does not have to be worn down into caring because he already",
        "must_show": "The widow home again in her own bare room at first light, sitting on the floor with her hands open on her knees — the same woman, no longer at anybody's door, simply asking.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOURNING + _NO_MOCK + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "her head is turned toward the doorway light at her own right and "
            "tipped slightly up; the camera stands square to her left side, so "
            "her eyeline runs laterally across the frame and exits through the "
            "RIGHT EDGE. HER PUPILS NEVER COME ROUND ONTO THE LENS AXIS. "
            "One photograph, 50mm lens, thin level first light coming in "
            "through the empty square doorway at screen RIGHT and lying across "
            "her and the beaten earth floor in one clean slab, no other light "
            "source in the room and NO LAMP LIT, the sun itself well out of "
            "frame and NEVER behind her head, " + _GRAIN +
            "SHE IS THE ONLY PERSON IN THE PICTURE, seen full length, sitting "
            "on a plain reed mat on the beaten earth floor of her one bare room "
            "with her legs folded under her and her back straight. BOTH HANDS "
            "REST OPEN AND PALM-UP ON HER KNEES, loose and unhurried. Her face "
            "is lit full on its front planes, her chin slightly lifted toward "
            "the light. Her dark brown hair going iron-grey at the temples is "
            "coiled low at the nape and uncovered; the deep indigo mantle lies "
            "across her shoulders over the dark umber-brown tunic. SHE IS NOT "
            "KNEELING TO BEG, NOT PROSTRATE, NOT WEEPING and there is no altar, "
            "shrine, image or built religious thing of any kind in the room. "
            "Around her the mud-plastered walls, the folded sleeping mat, two "
            "fired-clay jars and the small unlit clay oil lamp on its wall "
            "ledge. NOTHING IS IN THE AIR OR THE LIGHT — no figure, no face, no "
            "shaft, no beam and no radiance of any kind."
        ),
    },
    {
        "id": "v2-r038-b43", "out": "s43-wants-to-hear-you.jpeg",
        "seg": "n7", "window": "154.915-158.308", "wide": False, "jesus": False,
        "locks": _HOME, "char_refs": _WID,
        "narration": "loves you and he already wants to hear you.",
        "must_show": "The widow's face, close, in the first light — her eyes open and level, her exhaustion still on her but the set of her mouth eased. She is being heard, and it shows only on her.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOURNING + _NO_MOCK + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            _PROFILE +
            "One photograph, 105mm lens, very shallow depth of field, thin "
            "level first light from screen LEFT falling full and soft on the "
            "front planes of her face, the sun well out of frame and NEVER "
            "behind her head, and no bright rim, edge or outline anywhere "
            "around her hair or shoulders, " + _GRAIN +
            "SHE IS THE ONLY PERSON IN THE PICTURE. A TIGHT SHOT filling the "
            "frame from the shoulders up, the camera square to her right side "
            "at her own eye height, her head turned to the LEFT toward the "
            "light. Her whole profile reads: the strong narrow line of nose and "
            "brow, the high flat cheekbone, the fine deep lines at the outer "
            "corner of her open dark eye and either side of her mouth, the "
            "bruised tiredness still under her eye and the dust still grey in "
            "her skin — SHE IS NOT MADE YOUNG OR PRETTY OR NEW. What has "
            "changed is small and entirely on her face: the set of her jaw has "
            "let go, her lips are closed and soft instead of pressed, and her "
            "eye is level and unhurried. Her dark brown hair going iron-grey at "
            "the temple is coiled low at the nape. The deep indigo mantle lies "
            "across her shoulder over the dark umber-brown tunic. Behind her, "
            "thrown right out of focus, the pale mud-plastered wall of her room "
            "and the soft bright rectangle of the empty doorway. NOTHING ELSE "
            "IS IN THE PICTURE."
        ),
    },
    # ===== n8 — the closing application ======================================
    {
        "id": "v2-r038-b44", "out": "s44-keep-praying-never-give-up.jpeg",
        "seg": "n8", "window": "158.308-162.738", "wide": False, "jesus": True,
        "ref": REF, "locks": ["OLIVE-YARD", "JUDEAN-LAND"],
        "narration": "So when Jesus says to keep praying and never give up, it is not",
        "must_show": "Jesus in the very last of the light in the press yard, quiet and settled, finishing the telling.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_MODERN_TOWN + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the camera stands out to his RIGHT and slightly behind, so he is "
            "seen in three-quarter view from behind the shoulder with the far "
            "cheek foreshortened; his eyeline runs away across the frame to the "
            "LEFT and exits through the LEFT EDGE. HIS PUPILS NEVER COME ROUND "
            "ONTO THE LENS AXIS. "
            "One photograph, 50mm lens, the very last low level warm sun coming "
            "in from screen LEFT almost along the ground, deep amber, the "
            "shadows long and blue, the sun itself well out of frame and NEVER "
            "behind his head, and no bright rim, edge or outline around his "
            "hair, head or shoulders anywhere, " + _GRAIN +
            "HE IS THE ONLY PERSON IN THE PICTURE, seen from the waist up, "
            "seated easy on the low limestone kerb of the press bed with one "
            "knee drawn up and both hands resting loose over it, his shoulders "
            "down and settled — a man who has finished saying what he came to "
            "say. His head is turned to his own left toward the listeners out "
            "past the frame edge. His face reads clearly in three-quarter: the "
            "aquiline nose, the full dark brown beard, the long tousled dark "
            "brown wavy hair with warm bronze lights, and an expression that is "
            "warm, quiet and completely unhurried. Behind him, out of focus, "
            "the round grey crushing stone, the timber press beam and the "
            "amber-raked plastered wall of the yard. NOBODY ELSE IS IN THE "
            "PICTURE."
        ),
    },
    {
        "id": "v2-r038-b45", "out": "s45-the-very-opposite-of-that-judge.jpeg",
        "seg": "n8", "window": "162.738-167.298", "wide": True, "jesus": False,
        "locks": ["OLIVE-YARD", "LISTENERS", "JUDEAN-LAND", "BACKGROUND-CAST"],
        "narration": "because God is hard to move, it is because he is the very opposite of that",
        "must_show": "The listeners in the emptying yard at the end of the day — two rising to go, one still sitting exactly where he was, not ready to leave.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_MOCK + _NO_MODERN_TOWN + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            _BEHIND +
            "One photograph, 35mm lens, the last low level warm sun raking in "
            "from the RIGHT almost along the ground, shadows enormously long "
            "across the packed earth, the light deep amber, the sun itself well "
            "out of frame and NEVER behind any head, " + _GRAIN +
            "A WIDE FULL-LENGTH SCENE WITH MULTIPLE PEOPLE, NEVER A PORTRAIT: "
            "the camera stands back at the corner of the olive-press yard, "
            "chest high, so all three are in frame head to sandals. TWO village "
            "listeners have got to their feet and are walking away from the "
            "camera toward the square-topped gap in the wall, seen entirely "
            "FROM BEHIND as backs and shoulders, one with a reed mat rolled "
            "under his arm, both mid-stride. THE THIRD — the man of about sixty "
            "with thick grey hair and a full grey-white beard — IS STILL "
            "SITTING EXACTLY WHERE HE WAS on the low stone kerb of the crushing "
            "basin, seen in lost profile from behind and to the side, his "
            "forearms on his knees and his head down, plainly not ready to get "
            "up. NOT ONE FACE IS TURNED TOWARD THE LENS. Around them the press "
            "stands quiet: the circular grey crushing basin, the long timber "
            "beam in its socket, the stacked reed mats, the oil-darkened "
            "collecting hollow, the fired-clay jars. NOBODY IN THIS PICTURE "
            "WEARS CREAM, OFF-WHITE OR ANY PALE CLOTH — every person is a solid "
            "dark saturated mass of indigo, umber, rust, olive, charcoal or "
            "maroon head to foot, in focus and out of focus alike, and Jesus is "
            "NOT in this frame."
        ),
    },
    {
        "id": "v2-r038-b46", "out": "s46-waiting-to-hear-from-you.jpeg",
        "seg": "n8", "window": "167.298-171.743", "wide": True, "jesus": False,
        "locks": ["VILLAGE-LANE", "COURTYARD-GATE", "JUDEAN-LAND"],
        "narration": "judge and he has been waiting to hear from you all along.",
        "must_show": "The closing image: the father's doorway standing wide open on a first-light lane, its threshold stone worn hollow by feet — the same worn threshold as the judge's, but this door is open and nobody is in the way.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_IRONGATE + _NO_MODERN_TOWN + _NO_GREEN + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "One photograph, 50mm lens, thin level first light coming in low "
            "from the far LEFT straight along the lane and reaching right "
            "through the doorway onto the floor inside, the light clean and "
            "warm, long soft shadows, the sky above the flat roofline pale and "
            "clear, the sun itself well out of frame, " + _GRAIN +
            "AN EMPTY ARCHITECTURAL WIDE SHOT WITH NO PEOPLE IN IT AT ALL — "
            "nobody in the doorway, nobody in the lane, nobody in the "
            "background, in focus or blurred. The camera stands out in the lane "
            "a few paces back, low and square on to the house front, with the "
            "rest of the lane running away behind the camera. The frame "
            "is filled by the small mud-brick house: pale mud plaster over a "
            "footing of undressed field stone, a flat roofline of poles and "
            "packed earth, one small empty square opening high in the wall, and "
            "at the centre the plain SQUARE-TOPPED doorway — two jambs of "
            "dressed limestone blocks, ONE SINGLE FLAT LIMESTONE LINTEL laid "
            "straight across the top, and a WORN HOLLOWED LIMESTONE THRESHOLD "
            "SLAB at ground level, dished and polished smooth in the middle by "
            "generations of feet, catching the low light along its hollow. THE "
            "DOOR STANDS WIDE OPEN: its single slab of adzed timber planks, "
            "pegged across the back with two wooden battens, unpainted and "
            "silvered by weather, turning on a carved round stone pivot socket "
            "sunk into the threshold, is PUSHED RIGHT BACK FLAT AGAINST THE "
            "INSIDE OF THE WALL, so the opening is entirely clear and the first "
            "light reaches through it onto the beaten earth floor inside. "
            "Beside the door stand two fired-clay jars. The dust of the lane "
            "runs away past the house between pale flat-roofed mud-brick houses "
            "toward the bare terraced Judean hills. Everything light-toned in "
            "the picture is plaster, stone, timber and dust."
        ),
    },
]
