#!/usr/bin/env python3
"""V2 beat map — row 39, build-39-pharisee-publican (Luke 18:9-14). REALISTIC V2.

WHAT V1 ACTUALLY DID (verified from the artefact, not the prose): FOURTEEN stills
for 247.267 s of finished video, an average of 17.7 s a picture, and SEVEN of the
fourteen are held across two whole segments each:
  * `s5-pharisee-prays.jpeg` covers n5 + j1 — 64.171 to 88.124, TWENTY-FOUR
    SECONDS, the whole of the red-letter prayer of Luke 18:11-12.
  * `s6-afar-off.jpeg` covers jv13a + n7 — 101.426 to 128.122, TWENTY-SEVEN
    SECONDS, the entire introduction of the publican at the back of the temple.
  * `s9-the-verdict.jpeg` covers j3 + n10 — 167.982 to 197.576, TWENTY-NINE AND A
    HALF SECONDS: the red-letter verdict of Luke 18:14 AND the narrator's whole
    unpacking of it, the sentence the video exists to deliver, on one frame.
  * `s2-two-men-go-up.jpeg` covers jv10 + n2 (15.9 s), `s8-two-prayers.jpeg`
    covers n8b + n9 (12.7 s), `s3` 16.2 s, `s4` 15.9 s.
V2 gives all twenty-one spoken segments their own pictures: 58 pictures over
236.952 s = 4.09 s/picture, shortest 3.16 s, longest 4.86 s.

AUDIO: LOCKED, never re-voiced, V1 never written to. extract_beats' reconstruction
of V1's own timeline arithmetic (LEAD 0.28, GAP 0.72, KJV_GAP 1.75, TAIL 1.5)
totals 247.244 s against the delivered MP4's 247.266 s — 0.022 s apart, so the
staleness tripwire is nowhere near firing and the normal packet-copy AUDIO LOCK
applies.

SOURCING TRAP: CHECKED AND CLEAR. By GIT CONTENT DATE (mtimes are worthless here)
`make_narration.py` is 2026-07-24T00:35:41 and all twenty-one mp3s AND the
delivered MP4 share one later commit, 2026-07-27T23:20:01 — the script PRE-dates
its own audio, which is the safe direction. All twenty-one segments were
transcribed anyway with faster-whisper and compared word for word. FOUR apparent
differences came back and every one was chased:
  * s9 "parable unto certain" heard as "into"      — small.en only; medium.en
    returns "unto". Whisper mis-hearing archaic KJV, the family this wave has
    hit repeatedly.
  * n4 "A traitor with a money box" heard as "trader" — small.en only; medium.en
    returns "traitor".
  * n13 "did not tell this story" heard as "the story" — small.en only; medium.en
    returns "this".
  * card "If you stopped performing" heard as "stop" by BOTH small.en and
    medium.en. Settled as whisper's, not the audio's: the /t/ of "stopped"
    before the /p/ of "performing" is an assimilated plosive that leaves no
    separate burst, and the measured energy trace across that word shows ONE
    stop closure and ONE release, not two. Same contraction/inflection family
    rows 29, 31 and 38 all chased and settled the same way.
NO TEXT_OVERRIDES and no SPEAKER_OVERRIDES.

WINDOWS: rebuilt from scratch from extract_beats plus MEASURED whisper word
timings, never from the `.timing.json` sidecars (which on this build hold one
phrase spanning a whole segment). Contiguous 0.000 -> 236.952 (the card's own
start), ZERO gaps, and every one of the twenty-one speech onsets lands inside the
window written for it. Each interior split sits 0.15 s BEFORE the onset of the
word it belongs to.

WHO CARRIES WHICH RED-LETTER LINE — this row's sharpest content question, and the
one place it could invert. There are five red-letter segments and only ONE of them
belongs on Jesus's face:
  * jv10 (Luke 18:10) is Jesus SETTING THE SCENE — "Two men went up into the
    temple to pray". Staged INSIDE the parable, on the two men climbing.
  * j1 (Luke 18:11-12) is THE PHARISEE PRAYING. A red-letter Bible inks it, but
    the speaker is a character inside the parable. Putting Jesus's face under
    "God, I thank thee, that I am not as other men are" would invert the line
    completely — all four of its pictures are the Pharisee, out in the open
    pavement, alone.
  * jv13a (Luke 18:13a) is Jesus narrating inside his own parable — staged on
    the publican at the back wall.
  * j2 (Luke 18:13) is THE PUBLICAN PRAYING. His picture, his face.
  * j3 (Luke 18:14) IS Jesus speaking as himself — "I tell you, this man went
    down to his house justified" — so those three frames are his.
Jesus is on screen only in the eight frames the narration or the verse puts him
in as himself: b01, b02, b03, b41, b42, b43, b44, b56. He never appears inside
the parable and never in the temple.

CONTENT CARE. Luke 18:9-14 narrates no heaven, no hell, no angel, no soul, no
death and no punishment, so none is painted. GOD IS NEVER DEPICTED as any figure,
face, form, light or presence — both men pray to open sky and the sky is only
sky. "Would not lift up so much as his eyes unto heaven" is staged as a man not
raising his eyes, and heaven is the ordinary daylight above the court, nothing
more. n8a's "while a lamb is being killed for the sins of the whole nation" is
the ONE line in this row that the narration itself puts at the altar, so the
altar is shown — as STONE, SMOKE and standing priests only. No blood, no knife,
no carcass, no killing is visible anywhere; the lamb appears once, alive, led on
a plain cord. The Pharisee is NEVER A GROTESQUE: n3 is emphatic that he "was not
a fake", and a sneering caricature would let the viewer off the hook, so he is
handsome, disciplined, genuinely devout and completely certain. The publican is
never abject spectacle: no grovelling, no theatrical weeping, no filth.

STAGING — FIVE places, none repeating a composition used anywhere in the
realistic wave (rows 2/8/21 Luke 15; 11 night gale; 16 interior; 19 dawn shore;
22 basalt doorstep; 23 terraced hillside; 24 moored boat; 25 wheat field; 26
kitchen garden; 27 synagogue bench + baking yard; 28 ploughed field + mud-brick
hut; 29 limestone shelf / caravan road / quayside / stone courtyard; 30
breakwater / open water / strand; 31 night road + bridegroom's house; 32 trading
yard + master's hall; 33 mount + six mercy scenes; 34 barns + threshing floor; 35
banquet house + city lanes; 36 estate rooftop + accounts; 37 rich man's gate +
spirit world; 38 village judgment seat + widow's door):
  * A BROAD FLIGHT OF WORN CITY STEPS in a sunlit street below a high blank
    dressed-stone wall, where Jesus tells it standing, to a knot of prosperous
    well-dressed men who are standing too. Row 38's teaching place was an
    olive-press yard, 37's a fig court, 36's a rooftop, 35's a dining room, 34's
    a terebinth, 33's a rock-cut stair. Standing men on open street steps is used
    by none.
  * THE TEMPLE'S GREAT OUTER STAIR and its VAST OPEN PAVED COURT — the new
    shared TEMPLE-COURT lock.
  * THE PHARISEE'S OWN HOUSE DOOR at first light, where he fasts and tithes.
  * THE PUBLICAN'S TOLL TABLE beside the town gate — the new shared TOLL-STATION
    lock.
  * ONE PLAIN OPEN SQUARE-TOPPED GATEWAY for the closing two frames.

THE ROW'S VISUAL ENGINE — "the same two places in one court". Two camera
positions are fixed and returned to: POSITION A stands behind and above the
Pharisee out on the open middle of the pavement, and POSITION B stands at the
back wall behind the publican. b17, b23, b52, b53 and b55 are POSITION A at the
SAME spot with only the light and the crowd changing — and the last three are
after everyone else has gone home, which is what "he is still standing there"
actually means. b25 is the one frame that holds BOTH men in a single wide shot,
the near man large and the far man tiny against the far wall, and that single
composition is the parable. V1's fourteen reused stills could not do any of it.

LOCK-WORDING AUDIT (read every lock as if the model will build the most modern
thing the words permit). Four rewrites before the first paid image:
  * "temple", "altar", "priest" and "worship" pull, all at once, a Gothic church
    with pews and stained glass, a Greek temple with fluted columns and a
    pediment, a golden-domed mosque, and a modern synagogue with a curtained ark,
    a silver-crowned scroll, a six-pointed star and men in skullcaps and
    black-striped prayer shawls — every one of them centuries later than this
    story, and the last is the one an LDS outreach video can least afford to get
    wrong. Cured before the first credit by writing the new shared TEMPLE-COURT
    lock, which states the open stone courts, the plain square piers, the
    unhewn-stone altar and the barefoot linen-clad priests POSITIVELY.
  * "tax collector" and "toll" pull a Victorian counting window or a highway
    kiosk — a boarded booth with a hatch, a barrier arm, a metal cash box, a
    bound ledger, a uniform. Cured by the new shared TOLL-STATION lock, which
    states the low timber slab on two stones in the open dust POSITIVELY.
  * "Pharisee" pulls a sneering hook-nosed villain in flowing black. His lock
    states him as a handsome, upright, genuinely disciplined man of fifty in
    good dark-blue wool, because n3 says outright that he was not a fake.
  * "God" never appears in any scene text as anything to be depicted, and every
    beat that could invite it carries the no-deity clause.

CAST: TWO anchors, both of them pictures that had to exist on the timeline
anyway, so the anchors cost nothing extra. Both are generated in ONE anchor run
before anything else, and NEITHER anchor has the other character or Jesus in its
frame, so the REFS cache cannot make an anchor reference itself.
  b07 PUBLICAN — face-showing, strict side-on profile, alone on the great stair.
  b09 PHARISEE — face-showing, strict side-on profile, alone in his own doorway.
Jesus needs no anchor: he carries JESUS-V2-REF on every frame he is in.
"""

import os

OUTPUT_ASSET_DIR = "assets"

# See the AUDIO paragraph above: neither staleness tripwire fires, so the normal
# packet-copy AUDIO LOCK applies. Nothing is re-voiced, nothing is re-timed, and
# the V1 build is never written to.
AUDIO_FROM_V1_SEGMENTS = False

REF = True

# Wired in AFTER the two anchor beats are generated in their own run.
A_PUB = "assets/s07-the-other-a-publican.jpeg"
A_PHA = "assets/s09-was-not-a-fake.jpeg"
REFS = {"PUBLICAN": A_PUB, "PHARISEE": A_PHA}

_HERE = os.path.dirname(os.path.abspath(__file__))


def _have(rel):
    """ANCHOR-FIRST: a character reference attaches only once its anchor exists.

    On the first (anchor-only) run both lists below are empty, so `--check`
    passes and no anchor can reference itself through the REFS cache. Every run
    after it wires the accepted anchors into all the later beats automatically.
    """
    return [rel] if os.path.isfile(os.path.join(_HERE, rel)) else []


_PUB = _have(A_PUB)
_PHA = _have(A_PHA)
_BOTH = _PHA + _PUB

# ---------------------------------------------------------------- negatives ---
_NO_CREAM = ("no cream, off-white, ivory, buff, beige, taupe, sand, khaki, white "
             "or pale garment, tunic, robe, mantle, sash, wrap or head covering on "
             "anybody anywhere in the frame including the blurred edges, EXCEPT the "
             "plain undyed linen of a serving priest where the scene itself places "
             "one on the higher pavement; ")
_NO_CREAM_STRICT = ("no cream, off-white, ivory, buff, beige, taupe, sand, khaki, "
                    "white or pale garment, tunic, robe, mantle, sash, wrap or head "
                    "covering on anybody anywhere in the frame including the blurred "
                    "edges; ")
_NO_HALO = ("no nimbus, no aura, no corona, no bright outline, edge or contour "
            "around any head, hair, shoulder or body, nobody emits or radiates "
            "light, and no light source of any kind standing behind, above or "
            "beyond anyone's head; ")
_NO_CHURCH = ("no cross, crucifix, steeple, spire, bell, bell tower, dome, apse, "
              "minaret, pointed or round arch, ring of dressed voussoirs, vault, "
              "rose window, stained or leaded glass, fluted column, carved capital, "
              "entablature, frieze, cornice or triangular pediment; no pew, bench, "
              "chair, stall, throne, seat, kneeler, pulpit, lectern or communion "
              "rail; no candle, candlestick, candelabra, chandelier, sconce or "
              "swinging censer on chains; no organ, icon, fresco, framed picture or "
              "woven scene; no six-pointed star, hexagram, menorah, seven-branched "
              "lampstand, curtained ark or scroll with silver crowns; and on nobody "
              "a skullcap, black hat, black coat, side-curls, a striped fringed "
              "prayer shawl of a later century, a mitre, chasuble, stole, cassock "
              "or clerical collar; ")
_NO_BLOOD = ("no blood, carcass, cut, wound, knife, cleaver, hook, flayed or "
             "dismembered animal, no dying or struggling beast and no killing of "
             "any kind visible anywhere; ")
_NO_DEITY = ("no depiction of God, deity or any divine person as any figure, face, "
             "form, light or presence; no shaft, beam, column or burst of light "
             "coming down from the sky; no cloud floor, cloudscape, gate of light, "
             "wing, winged figure, cherub, feather, harp, crown, throne or shining "
             "architecture; and no angel, spirit, ghost, vision or apparition "
             "anywhere; ")
_NO_MOCK = ("nobody devout is drawn as a sneering, leering, hook-nosed, gloating or "
            "moustache-twirling villain, and nobody poor or despised is drawn "
            "grotesque, comic, filthy, ragged to indecency, grovelling, wailing or "
            "pitiable; each is a real person with dignity; ")
_NO_OFFICE = ("no built booth, hut, kiosk, window, serving hatch, counter, grille, "
              "turnstile, barrier or chain across any road; no table with legs, "
              "desk, chair or stool with legs; no metal cash box, strongbox, lock, "
              "hasp or padlock; no bound book, ledger, spine or stacked leaves; no "
              "scales, balance, weights, abacus or tally board; no banknote, paper "
              "money, printed paper, receipt, label, price board, notice or sign; "
              "and no soldier, armour, helmet, shield, spear, sword, standard or "
              "uniform; ")
_NO_MODERN_TOWN = ("no dome, minaret, bell tower, spire, clock, crenellation, "
                   "pitched roof, roof tile, shingle, chimney, gable or "
                   "half-timbering against any sky; no pole, mast, pylon, wire, "
                   "cable, aerial, guardrail, signpost or painted sign; no asphalt, "
                   "tarmac, concrete, kerb, gutter, drain, grating or painted road "
                   "marking; no vehicle, wheel of pneumatic rubber, engine or "
                   "machine of any kind; ")
_NO_GREEN = ("no green meadow, lawn, turf, pasture, moor, upland, heather, clipped "
             "hedgerow, deciduous woodland or lush temperate countryside, and no "
             "soft grey overcast northern European sky; ")
_NO_IRONGATE = ("no wrought iron, cast iron, railing, bar, grille, lattice, picket, "
                "spearhead, finial or ornamental metalwork on any door, gate or "
                "wall; no hinge, strap hinge, ring, knocker, handle, latch, hasp, "
                "bolt, lock plate, keyhole or padlock; no arch or curved head over "
                "any opening; and no nameplate, sign, lettering or lamp bracket "
                "on it; ")
_GAZE = "nobody's pupils centred on the lens."

_GRAIN = ("shot on a full-frame camera at f/2.8 with true optical depth of field, "
          "fine natural film grain, dust hanging in the air, no digital sharpening "
          "and no illustration line anywhere. ")

# Common lock stacks.
_STEPS = ["STREET-STEPS", "LISTENERS", "JUDEAN-LAND", "BACKGROUND-CAST"]
_TEMPLE = ["TEMPLE-COURT", "JUDEAN-LAND", "BACKGROUND-CAST"]
_T_PHA = ["TEMPLE-COURT", "PHARISEE", "JUDEAN-LAND", "BACKGROUND-CAST"]
_T_PUB = ["TEMPLE-COURT", "PUBLICAN", "JUDEAN-LAND", "BACKGROUND-CAST"]
_T_BOTH = ["TEMPLE-COURT", "PHARISEE", "PUBLICAN", "JUDEAN-LAND", "BACKGROUND-CAST"]
_HOUSE = ["PHARISEE-HOUSE", "PHARISEE", "JUDEAN-LAND"]
_TOLL = ["TOLL-STATION", "PUBLICAN", "JUDEAN-LAND", "MARKET-TOWN", "BACKGROUND-CAST"]
_GATE = ["COURTYARD-GATE", "JUDEAN-LAND"]

LOCKS = {
    # ------------------------------------------------------------- people ----
    "PHARISEE": (
        "PHARISEE LOCK: the Pharisee of the parable is the SAME MAN in every "
        "picture he appears in — in his own doorway, in the street, out on the "
        "temple pavement and walking down the great stair — and he is a JUDEAN "
        "of the first century, born and weathered in the dry country of that "
        "place. He is about FIFTY, tall, spare, straight-backed and physically "
        "disciplined, a man who has fasted twice a week for thirty years and "
        "looks it. HE IS NOT A VILLAIN AND NOT A CARICATURE: he is "
        "good-looking, dignified, calm and entirely sincere, and nothing in his "
        "face sneers, leers, gloats or curls. HIS SKIN IS WARM OLIVE-BROWN, "
        "clearly Middle Eastern, never fair, never pink, never European-looking, "
        "lightly weathered across the brow and the backs of the hands. He has a "
        "long straight nose, a high clear forehead, level dark brows and DARK "
        "BROWN EYES that are steady, bright and completely untroubled. His "
        "beard is FULL, THICK AND IRON-GREY, carefully combed and squared off "
        "at the jaw, and his HAIR IS THICK IRON-GREY, combed straight back off "
        "the forehead and cut level at the middle of the neck — never long to "
        "the shoulders, never loose, never bald, never shaven — and a clear "
        "band of that iron-grey hair shows at the front edge, at the temples "
        "and at the nape IN EVERY SHOT OF HIM, INCLUDING EVERY SHOT TAKEN FROM "
        "BEHIND HIM. HIS HANDS ARE A MAN'S: long, brown, clean, well-kept, "
        "broad across the knuckles, the nails trimmed short. HE WEARS EXACTLY "
        "FOUR SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) ONE ankle-length "
        "tunic of finely hand-woven wool in DEEP INDIGO BLUE, its weave close "
        "and even, with straight unshaped sleeves to the wrist and a plain slit "
        "neck; (2) ONE large rectangular mantle of the same finely woven wool "
        "in DARK BLUE-BLACK. HOW THAT MANTLE IS WORN, STATED AS GEOMETRY "
        "BECAUSE THE MODEL OTHERWISE BUILDS A MODERN DRESSING GOWN: it is ONE "
        "flat rectangle of cloth laid ACROSS THE BACK OF BOTH SHOULDERS with "
        "its two ends carried BACKWARD AND DOWN BEHIND HIM, so that THE WHOLE "
        "FRONT OF HIS BODY FROM COLLARBONE TO KNEE SHOWS ONLY THE UNBROKEN "
        "DEEP INDIGO BLUE TUNIC — no edge, seam, fold or border of the mantle "
        "runs vertically down the front of his chest. HE IS NOT WEARING A "
        "COAT, CARDIGAN, DRESSING GOWN OR BATHROBE: there is no front "
        "opening, no shawl collar, no lapel, no revers, no rolled collar band, "
        "no placket, no button, hook, tie or fastening, no set-in tailored "
        "shoulder and no cuff anywhere on him. Its four corners are each "
        "finished with ONE short twisted "
        "TASSEL OF PLAIN UNDYED WOOL THREAD with a single strand of blue "
        "through it, hanging plainly, undecorated; (3) ONE flat woven sash of "
        "DARK MADDER RED knotted at the waist; and (4) ONE folded rectangle of "
        "the same dark blue wool wound low round his head and left hanging at "
        "the nape, or left off entirely so the combed iron-grey hair shows. On "
        "his LEFT UPPER ARM and in the CENTRE OF HIS FOREHEAD he wears the "
        "small plain first-century phylactery: ONE little cube of plain dark "
        "brown leather about the size of a thumb joint, bound in place by ONE "
        "narrow plain leather strap wound and knotted, with no buckle, no metal "
        "and no ornament of any kind. ON HIS FEET, STATED POSITIVELY: PLAIN FLAT OPEN LEATHER THONG SANDALS — a flat rawhide sole cut to the shape of the foot with no heel, plain undyed leather straps knotted and tucked back through themselves, and HIS BARE BROWN TOES, INSTEP, HEEL AND ANKLE PLAINLY VISIBLE. HE NEVER WEARS A BOOT, SHOE, SLIPPER, CLOG OR ANY FOOT COVERING WITH AN UPPER THAT ENCLOSES THE FOOT, no lace, no buckle, no metal fitting, no moulded or rubber sole and no tread. HE NEVER "
        "WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, WHITE OR ANY "
        "PALE CLOTH, and he wears no jewellery, ring, chain, brooch, medallion "
        "or metal ornament anywhere. What is on his face is CALM, SETTLED, "
        "UNSHAKEABLE CERTAINTY — the peace of a man who is quite sure he is "
        "right — deepening across the story into serene satisfaction, and never "
        "into rage, scorn or comedy. "  "HIS CLOTH AT CLOSE RANGE, BECAUSE A MACRO IS WHERE THE WEAVE LOCK IS "
        "WEAKEST: wherever a sleeve, cuff, wrist, neck or hem of his comes near "
        "the camera it reads as COARSE HAND-WOVEN CLOTH and shows it — a visible, slightly irregular over-and-under grid of warp and weft threads, flat and matte, ending in a raw cut selvedge or a frayed hem, never a finished band. THERE IS NO KNITTED CLOTH ON HIM ANYWHERE: no knit or purl stitch, no rib, no ribbing, no cable, no jersey, no seed stitch, no stretchy or ribbed cuff, collar band or welt, no felted, fleeced, brushed, napped or looped pile, and no sweater, jumper or sweatshirt texture at any wrist, elbow, neck or hem. A SLEEVE THAT WOULD OTHERWISE END NEAR THE CAMERA IS PUSHED UP THE FOREARM SO THE BARE BROWN ARM SHOWS AND NO CUFF IS IN THE FRAME AT ALL. " "LIGHT GEOMETRY THAT TRAVELS WITH HIM: every light in every "
        "picture of this man stands IN FRONT OF HIM AND ON THE CAMERA'S "
        "SIDE OF HIM, never beyond him and never above and behind him. THE "
        "OUTER EDGE OF HIS HAIR, THE TOP OF HIS HEAD, THE LINE OF HIS BEARD "
        "AND THE OUTER EDGE OF HIS SHOULDER ARE ALWAYS DARKER THAN WHATEVER "
        "LIES BEHIND THEM and carry no brighter line, fringe, rim, edge, "
        "contour, ring or separation of any kind; his hair is never lit from "
        "behind into a bright fringe and he is never outlined against a "
        "brighter background. " "IDENTITY FLOOR, WHICH HOLDS EVEN WHEN HE "
        "IS SMALL, DISTANT, PARTLY CROPPED, SOFTLY OUT OF FOCUS OR SEEN "
        "ENTIRELY FROM BEHIND: a MAN of about fifty, tall and spare; warm "
        "olive-brown Middle Eastern skin; THICK IRON-GREY HAIR combed back and "
        "cut level at the neck with a FULL SQUARED IRON-GREY BEARD; and always "
        "the DEEP INDIGO BLUE tunic under the DARK BLUE-BLACK tasselled mantle."
    ),
    "PUBLICAN": (
        "PUBLICAN LOCK: the tax collector of the parable is the SAME MAN in "
        "every picture he appears in — at his toll table, on the great stair, "
        "at the back wall of the temple court and walking home — and he is a "
        "JUDEAN of the first century, born and weathered in the dry country of "
        "that place. He is about THIRTY-EIGHT, of middling height, thickset "
        "through the shoulders and beginning to go heavy at the waist, a man "
        "who sits all day and eats well. HIS SKIN IS WARM SUN-DARKENED "
        "OLIVE-BROWN, clearly Middle Eastern, never fair, never pink, never "
        "pale-toned, never European-looking, with a broad face, heavy cheeks, a "
        "short blunt nose, thick dark brows and DARK BROWN EYES that are "
        "guarded and tired and that he keeps aimed DOWNWARD. His beard is "
        "SHORT, BLACK AND THICK, cropped close to the jaw and not shaped, and "
        "his HAIR IS BLACK, thick and coarse, cut roughly at the top of the "
        "neck and pushed back off his forehead — never long to the shoulders, "
        "never loose, never bald, never shaven — and a clear band of that black "
        "hair shows at the front edge, at the temples and at the nape IN EVERY "
        "SHOT OF HIM, INCLUDING EVERY SHOT TAKEN FROM BEHIND HIM. HIS HANDS ARE "
        "A MAN'S: broad, thick-fingered, brown and soft-palmed, ink-stained "
        "along the first two fingers of the right, the nails short. HE WEARS "
        "EXACTLY THREE SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) ONE "
        "knee-length tunic of good but plain hand-woven wool in DEEP RUST-BROWN "
        "with a narrow woven border of the same colour a shade darker, straight "
        "unshaped sleeves to the elbow, a plain slit neck; (2) ONE rectangular "
        "mantle of coarser wool in DARK OLIVE-GREEN, going grey with dust, "
        "pulled round his shoulders; and (3) ONE plain twisted cord of undyed "
        "brown flax knotted at the waist. Plain flat worn leather sandals. HIS "
        "HEAD IS BARE in every picture, showing the black hair. HE NEVER WEARS "
        "CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, WHITE OR ANY PALE "
        "CLOTH, and he wears no jewellery, ring, chain, brooch or metal "
        "ornament anywhere. HE IS NEVER A GROTESQUE AND NEVER ABJECT "
        "SPECTACLE: not filthy, not ragged, not comic, not crawling, not "
        "grovelling, not howling, not clutching at anyone; he is a "
        "well-fed working man who has stopped being able to look anyone in the "
        "face. What is on his face is PLAIN, QUIET, EXHAUSTED SHAME that never "
        "performs itself — the eyes lowered, the mouth set, the jaw working — "
        "and at the very end of the story a stunned, careful relief. "  "HIS CLOTH AT CLOSE RANGE, BECAUSE A MACRO IS WHERE THE WEAVE LOCK IS "
        "WEAKEST: wherever a sleeve, cuff, wrist, neck or hem of his comes near "
        "the camera it reads as COARSE HAND-WOVEN CLOTH and shows it — a visible, slightly irregular over-and-under grid of warp and weft threads, flat and matte, ending in a raw cut selvedge or a frayed hem, never a finished band. THERE IS NO KNITTED CLOTH ON HIM ANYWHERE: no knit or purl stitch, no rib, no ribbing, no cable, no jersey, no seed stitch, no stretchy or ribbed cuff, collar band or welt, no felted, fleeced, brushed, napped or looped pile, and no sweater, jumper or sweatshirt texture at any wrist, elbow, neck or hem. A SLEEVE THAT WOULD OTHERWISE END NEAR THE CAMERA IS PUSHED UP THE FOREARM SO THE BARE BROWN ARM SHOWS AND NO CUFF IS IN THE FRAME AT ALL. " "LIGHT GEOMETRY THAT TRAVELS WITH HIM: every light in every "
        "picture of this man stands IN FRONT OF HIM AND ON THE CAMERA'S "
        "SIDE OF HIM, never beyond him and never above and behind him. THE "
        "OUTER EDGE OF HIS HAIR, THE TOP OF HIS HEAD, THE LINE OF HIS BEARD "
        "AND THE OUTER EDGE OF HIS SHOULDER ARE ALWAYS DARKER THAN WHATEVER "
        "LIES BEHIND THEM and carry no brighter line, fringe, rim, edge, "
        "contour, ring or separation of any kind; his hair is never lit from "
        "behind into a bright fringe and he is never outlined against a "
        "brighter background. " "IDENTITY "
        "FLOOR, WHICH HOLDS EVEN WHEN HE IS SMALL, DISTANT, PARTLY CROPPED, "
        "SOFTLY OUT OF FOCUS OR SEEN ENTIRELY FROM BEHIND: a MAN of about "
        "thirty-eight, thickset; warm sun-darkened olive-brown Middle Eastern "
        "skin; SHORT COARSE BLACK HAIR cut at the neck with a SHORT CROPPED "
        "BLACK BEARD and a BARE HEAD; and always the DEEP RUST-BROWN tunic "
        "under the DARK OLIVE-GREEN mantle."
    ),
    "LISTENERS": (
        "LISTENERS LOCK: the men Jesus is telling this to are the ones Luke "
        "names — 'certain which trusted in themselves that they were righteous, "
        "and despised others' — and they are FOUR PROSPEROUS JUDEAN MEN of the "
        "first century standing on the street steps, between about thirty-five "
        "and sixty, all of them warm olive-brown Middle Eastern men with dark "
        "hair and full dark or greying beards, none of them fair, pink or "
        "European-looking. THEY ARE WELL-DRESSED AND WELL-KEPT: each in ONE "
        "ankle-length tunic of closely woven wool in a SOLID DARK SATURATED "
        "EARTH COLOUR — deep indigo, dark maroon, deep rust, dark olive or "
        "charcoal — under ONE rectangular mantle of the same weight and depth "
        "of colour, with a plain woven sash at the waist and good flat leather "
        "sandals. NOT ONE OF THEM WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, "
        "SAND, KHAKI, WHITE OR ANY PALE CLOTH, and none wears a skullcap, a "
        "striped fringed prayer shawl of a later century, a black hat, a black "
        "coat, side-curls or any jewellery. WHAT IS AT THEIR NECKS AND ON "
        "THEIR HEADS, STATED POSITIVELY BECAUSE THIS IS WHERE PALE CLOTH KEEPS "
        "ARRIVING AND A BAN DOES NOT HOLD IT: wherever a man's neck, shoulders "
        "or head is covered at all — by a wrap, a scarf, a folded head cloth, a "
        "mantle edge, a collar or an under-sleeve — THAT COVERING IS THE SAME "
        "SOLID DARK SATURATED COLOUR AS HIS OWN TUNIC AND IS INDISTINGUISHABLE "
        "FROM IT IN TONE: deep indigo on indigo, dark maroon on maroon, deep "
        "rust on rust, dark olive on olive, charcoal on charcoal. EVERY ONE OF "
        "THESE MEN IS THEREFORE ONE SINGLE UNBROKEN BLOCK OF ONE DARK COLOUR "
        "FROM THE CROWN OF HIS HEAD TO HIS SANDALS, with no lighter, paler, "
        "contrasting or two-tone piece anywhere on him — no cream, off-white, "
        "ivory, buff, beige, taupe, sand, khaki, tan, oatmeal, pale grey or "
        "bleached cloth at any neck, throat, collar, shoulder, cuff, sleeve, "
        "hem, head or edge, in focus or blurred. THE GROUP IS CAPPED AT EXACTLY "
        "FOUR MEN and there is no fifth man, no extra shoulder, arm, sleeve, "
        "head or back at any edge of the frame, and NOBODY AT ALL stands in the "
        "background, near or far, sharp or hazy. THEY STAND — nobody sits, nobody "
        "kneels — with arms folded or hands clasped in front, listening "
        "closely, and their faces are ATTENTIVE, COMPOSED AND SLIGHTLY "
        "PLEASED, the faces of men who expect to come out of the story well. "
        "None of them is drawn as a sneering or gloating villain and none of "
        "them looks toward the camera."
    ),
    "JUDEAN-LAND": (
        "JUDEAN-LAND LOCK: this is the real first-century JUDEAN HILL COUNTRY "
        "and it is stated positively at length so nothing has to be guessed. "
        "THE GROUND is pale limestone country: bare rock breaking through thin "
        "stony soil, dry packed tan earth and fine pale dust, loose flakes of "
        "cream-grey limestone, low dry-stone walls of undressed field stone, "
        "and terraces cut into the hillsides by hand. THE PLANTS are the plants "
        "of that place and no other: grey-green olive trees with thick twisted "
        "trunks, dark cypress, fig, almond, low thorny scrub, dry silver-grey "
        "wild herbs, pale bleached summer grass and stubble. THE SKY is the "
        "high dry pale blue of the eastern Mediterranean, cloudless or with "
        "thin high cloud, and the sunlight is strong, clean and directional, "
        "throwing hard-edged shadows. THE PEOPLE ARE THE PEOPLE OF THAT LAND: "
        "every single person in the frame, named or unnamed, near or far, in "
        "focus or blurred, is a MIDDLE EASTERN JEW of the first century with "
        "WARM OLIVE-BROWN OR SUN-DARKENED BROWN SKIN, dark brown or black hair, "
        "dark brown eyes and Semitic features; the men wear full beards; and "
        "everyone is dressed in hand-woven wool and linen in the dyes of that "
        "century — indigo, madder red, umber, rust, dark olive, charcoal and "
        "undyed brown. NOBODY IN THE PICTURE IS FAIR-SKINNED, PINK-SKINNED, "
        "NORTHERN EUROPEAN, RED-HAIRED OR LIGHT-EYED, and nobody wears a "
        "garment, footwear, hairstyle or ornament of any later century."
    ),
    # ------------------------------------------------------------- places ----
    "STREET-STEPS": (
        "STREET-STEPS LOCK: the place where Jesus is telling this is a BROAD "
        "PUBLIC FLIGHT OF STEPS in a first-century Judean city street, and it "
        "is stated positively. The steps are SIX OR SEVEN SHALLOW COURSES of "
        "large pale limestone slabs running the full width of the street, laid "
        "by hand, uneven, their front edges worn round and hollowed by feet, "
        "with pale dust and small loose stones drifted into the angles. Behind "
        "and above them stands ONE HIGH BLANK WALL of very large square-cut "
        "pale limestone blocks laid in level courses without mortar, unbroken "
        "except by ONE plain SQUARE-TOPPED rectangular doorway with a single "
        "flat lintel and nothing in it. To one side a low run of tan mud-brick "
        "house wall with FLAT roofs of poles and packed earth, plain "
        "rectangular openings and NO glass. The light is strong late-morning "
        "sun coming in from one side, laying hard-edged shadows of the step "
        "edges across the stone. THERE IS NOTHING BUILT OF ANY LATER CENTURY "
        "HERE: no handrail, balustrade, railing, guard, bollard, kerb, gutter, "
        "drain, grating, paving slab of poured concrete, tarmac, asphalt, "
        "painted line, tactile strip or step nosing; no pole, wire, cable, "
        "lamp, bracket, sign, plaque, notice or lettering anywhere; no dome, "
        "minaret, bell tower, spire, pitched roof, roof tile, shingle, chimney "
        "or arch against the sky; and no bench, seat, planter, bin or street "
        "furniture of any kind."
    ),
    "PHARISEE-HOUSE": (
        "PHARISEE-HOUSE LOCK: the Pharisee's own house is a well-kept but plain "
        "first-century Judean town house and this is what it IS. Its walls are "
        "dressed pale limestone blocks below and smooth tan mud plaster above, "
        "its roof FLAT, of poles, brushwood and packed earth, reached by stone "
        "steps on the outside. Its door is ONE PLAIN SQUARE-TOPPED RECTANGULAR "
        "OPENING with two dressed limestone jambs and ONE single flat limestone "
        "lintel laid straight across the top, a worn hollowed threshold slab at "
        "ground level, and NO leaf, door, frame or curtain in it — the opening "
        "is simply a clear dark rectangle. Inside and beside it: a beaten "
        "plaster floor spread with ONE hand-woven wool mat in deep madder and "
        "indigo, ONE low stone ledge along the wall, plain fired-clay bowls and "
        "jars, a hand-woven reed basket, and a shallow fired-clay oil lamp with "
        "a bare fibre wick standing unlit on the ledge. Outside, bare packed "
        "earth and pale dust worn hollow by feet, and ONE small hand-dug bed of "
        "dark soil against the wall growing low grey-green kitchen herbs — mint "
        "and rue — in short rows. THIS HOUSE IS NOT OF ANY LATER CENTURY: no "
        "hinged or planked door, no jamb of sawn timber, no hinge, ring, "
        "knocker, handle, latch, hasp, bolt, lock plate, keyhole or padlock; no "
        "arch, curved head or ring of voussoirs over any opening; no glass, "
        "shutter, sash, frame or grille in any window; no chair, stool, table "
        "with legs, cupboard, shelf of books or chest of drawers; no candle, "
        "lantern, glass lamp or hanging fixture; no fireplace, mantel, chimney, "
        "tile, cornice, moulding, panelling or painted mural; and no lettering, "
        "numeral, plaque or sign anywhere."
    ),
}

BEATS = [
    # ===== s9 — Luke 18:9, Luke's own framing (light blue) ===================
    {
        "id": "v2-r039-b01", "out": "s01-he-spake-this-parable.jpeg",
        "seg": "s9", "window": "0.000-3.850", "wide": True, "jesus": True, "ref": REF,
        "locks": _STEPS,
        "narration": "And he spake this parable unto certain which trusted in themselves",
        "must_show": "Jesus standing three steps up on a broad public flight of worn limestone city steps in strong late-morning light, half turned toward four prosperous men standing below him as he begins to speak; the camera stands behind the listeners and shoots past their backs.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the man Jesus is answering is NOT behind the camera — he stands "
            "far out at the RIGHT EDGE of the picture, so Jesus's head is "
            "turned a quarter-turn away from the lens and STAYS there. The "
            "camera sees the SIDE of his face, the near cheek broad and the far "
            "cheek foreshortened with the far eye narrowed behind the bridge of "
            "his nose, and his eyeline runs LATERALLY ACROSS the frame and out "
            "through the RIGHT EDGE. HIS PUPILS NEVER COME ROUND ONTO THE LENS "
            "AXIS AND HE NEVER LOOKS INTO THE CAMERA. "
            "One photograph, 35mm lens, hard clean late-morning sun raking in "
            "from the LEFT across the worn step edges, laying long hard-edged "
            "shadows down the stone, the sun itself well out of frame and NEVER "
            "behind any head; the blank limestone wall behind Jesus is in "
            "shadow and reads DARKER than he does. " + _GRAIN +
            "THE CAMERA STANDS BEHIND AND SLIGHTLY BELOW THE STANDING "
            "LISTENERS AND SHOOTS PAST THEM AND UP: three dark-clad prosperous "
            "men fill the lower and left third of the frame as heads, shoulders "
            "and BACKS seen entirely FROM BEHIND, standing on the lower steps "
            "with arms folded, and NOT ONE FACE IS TURNED TOWARD THE LENS. "
            "Jesus stands three shallow courses above them, right of centre, "
            "full length from head to sandals, weight on one foot, one hand "
            "low and open at his side, in three-quarter view; he has just "
            "turned his head to his own left and his gaze travels level and to "
            "the RIGHT and exits the picture through the RIGHT EDGE. THIS IS A "
            "WIDE FULL-LENGTH GROUP PHOTOGRAPH AND NOT A PORTRAIT: the camera "
            "is far enough back that all four men, the full width of the "
            "worn steps and the great blank block wall above are in frame "
            "together. THE ONLY PALE WOOL IN THE WHOLE PICTURE IS HIS OWN ROBE; "
            "every other person is a solid dark saturated mass of indigo, "
            "maroon, rust, olive or charcoal from edge to edge, in focus and "
            "out of focus alike."
        ),
    },
    {
        "id": "v2-r039-b02", "out": "s02-that-they-were-righteous.jpeg",
        "seg": "s9", "window": "3.850-7.984", "wide": True, "jesus": True, "ref": REF,
        "locks": _STEPS,
        "narration": "that they were righteous, and despised others.",
        "must_show": "The four prosperous listeners' faces, composed and quietly pleased with themselves, seen past Jesus's shoulder from behind him; one of them has just glanced sideways and down at a poorer man passing at the foot of the steps.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MODERN_TOWN + _NO_GREEN + _NO_MOCK + _GAZE,
        "scene": (
            "REVERSE OF THE PREVIOUS FRAME. THE CAMERA NOW STANDS BEHIND AND "
            "ABOVE JESUS AND SHOOTS PAST HIM DOWN THE STEPS: the back of his "
            "head, his shoulder and the top of his cream wool mantle fill the "
            "lower LEFT corner of the picture, softly out of focus, seen "
            "ENTIRELY FROM BEHIND — his face is not visible at all and no part "
            "of it turns toward the lens. Beyond him, sharp and full length, "
            "the four prosperous men stand on the lower courses in a loose "
            "uneven group, not a line, three of them watching Jesus so their "
            "eyeline runs INTO the frame and away from the camera, and the "
            "fourth, nearest the right edge, has turned his head away to his "
            "own right and is looking DOWN and OUT through the RIGHT EDGE at a "
            "thin man in patched dark umber carrying a bundle who is walking "
            "past at the foot of the steps with his back to us. Their faces are "
            "calm, attentive and faintly satisfied — no sneer, no scowl, no "
            "grimace — and NOT ONE PAIR OF PUPILS IS CENTRED ON THE LENS. "
            "One photograph, 35mm lens, hard late-morning sun from the LEFT, "
            "the shadows of the step edges running in hard parallel bands "
            "across the stone between them. " + _GRAIN +
            "THE ONLY PALE WOOL IN THE PICTURE IS THE OUT-OF-FOCUS SHOULDER OF "
            "JESUS'S OWN ROBE in the near corner; every other person, in focus "
            "or blurred, is a solid dark saturated mass of indigo, maroon, "
            "rust, olive or charcoal from edge to edge."
        ),
    },
    # ===== n1 — the narrator's retelling of Luke 18:9 (white) ================
    {
        "id": "v2-r039-b03", "out": "s03-a-certain-kind-of-man.jpeg",
        "seg": "n1", "window": "7.984-12.014", "wide": False, "jesus": True, "ref": REF,
        "locks": ["STREET-STEPS", "JUDEAN-LAND"],
        "narration": "Jesus told this story to a certain kind of man. The kind who was sure",
        "must_show": "A tight, quiet, strictly side-on profile of Jesus mid-sentence on the city steps, his mouth open on a word and his eyes level and steady, aimed across the frame at the men below him.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the line between "
            "Jesus and the man he is speaking to, so we see the clean edge of "
            "his profile against the shadowed wall — the near cheek, the "
            "eyelash line, the bridge of the nose in silhouette against the "
            "background, and THE FAR CHEEK AND FAR EYE ARE HIDDEN BEHIND THE "
            "BRIDGE OF HIS NOSE AND NOT VISIBLE AT ALL. His single visible eye "
            "looks straight ACROSS the frame and out through the RIGHT EDGE. "
            "The pose itself makes a look into the lens physically impossible. "
            "One photograph, 85mm lens at f/2.8, head and shoulders only, the "
            "great blank limestone block wall four paces behind him thrown "
            "completely soft, hard late-morning sun coming from the LEFT and "
            "IN FRONT of him so it lands on the front planes of his face — the "
            "brow, the nose, the cheekbone, the beard — while the back of his "
            "head and the top of his hair stay in his own shadow and read "
            "DARKER than the wall behind them; the sun is well out of frame "
            "and there is no light source anywhere behind or above his head. "
            + _GRAIN +
            "His lips are parted mid-word, his jaw is dropped a little, the "
            "muscles at the corner of his eye are relaxed, and his expression "
            "is level, unhurried and kind. Nothing else is in the frame: no "
            "other person, no hand, no object, no shoulder at any edge."
        ),
    },
    {
        "id": "v2-r039-b04", "out": "s04-and-just-as-sure.jpeg",
        "seg": "n1", "window": "12.014-16.198", "wide": True, "jesus": False,
        "locks": _STEPS,
        "narration": "he was one of the good ones, and just as sure that other people were not.",
        "must_show": "Two of the prosperous listeners in the street below, one of them stepping back and lifting the hem of his good dark mantle clear of a poorer man crouched against the wall with a begging bowl, without once looking at him.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MODERN_TOWN + _NO_GREEN + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 50mm lens, hard late-morning sun from the LEFT, "
            "the foot of the great limestone steps and the dusty street "
            "running away to the right. " + _GRAIN +
            "THE CAMERA STANDS BEHIND AND TO THE SIDE OF THE TWO WELL-DRESSED "
            "MEN AND SHOOTS PAST THEM: they are seen in three-quarter from "
            "behind, full length from head to sandals, walking away from the "
            "lens toward the right, and NOT ONE FACE IS TURNED TOWARD THE "
            "CAMERA. The nearer of the two has swung his weight onto his "
            "outside foot and gathered the hem of his dark blue-black mantle up "
            "into his fist to keep it clear of the ground; his head is turned "
            "AWAY, forward along the street, and his eyeline exits through the "
            "RIGHT EDGE. Low against the base of the wall in the middle "
            "distance, sitting on the dust with his knees drawn up, is a thin "
            "man in a patched dark umber tunic with an empty shallow fired-clay "
            "bowl on the stone beside his foot; he is in strict side-on profile "
            "looking down at the bowl, his face calm and unremarkable, NOT "
            "grotesque, NOT comic, NOT grovelling and NOT reaching out. "
            "Neither well-dressed man is looking at him. THE COMPOSITION IS THE "
            "POINT: the two upright dark figures pass through the sunlight in "
            "the near half of the frame and the seated man sits in the shade "
            "behind them, unnoticed. Every person in the picture, in focus or "
            "blurred, is a solid dark saturated mass of indigo, maroon, rust, "
            "olive, umber or charcoal from edge to edge, and NO PALE OR "
            "OFF-WHITE CLOTH APPEARS ON ANYBODY ANYWHERE."
        ),
    },
    # ===== jv10 — Luke 18:10, Jesus setting the parable (red, in the parable) =
    {
        "id": "v2-r039-b05", "out": "s05-two-men-went-up.jpeg",
        "seg": "jv10", "window": "16.198-19.628", "wide": True, "jesus": False,
        "locks": _T_BOTH, "char_refs": _BOTH,
        "narration": "Two men went up into the temple to pray; the one",
        "must_show": "The two men climbing the temple's great outer stair, far apart, both seen from behind and below — the Pharisee upright and well ahead, the tax collector a long way below and to one side, climbing slowly.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_BLOOD + _NO_MODERN_TOWN + _NO_GREEN + "no round column, cylindrical shaft, colonnade, peristyle, portico, porch, stoa, temple front, entablature, architrave, frieze, cornice, pediment, gable or coffered ceiling anywhere in the frame or against the sky; no boot, shoe, clog or any foot covering with an upper enclosing the foot on anybody; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard bright mid-morning sun coming from "
            "the upper LEFT, the enormous pale limestone stair climbing away "
            "from the camera and filling most of the frame, its worn step edges "
            "running in hard parallel bands of light and shadow. " + _GRAIN +
            "THE CAMERA STANDS LOW AT THE FOOT OF THE STAIR, BEHIND BOTH MEN, "
            "AND SHOOTS UP PAST THEM: both are seen ENTIRELY FROM BEHIND, full "
            "length from head to sandals, climbing AWAY from the lens, and "
            "NEITHER FACE IS VISIBLE AT ALL. THE PHARISEE — a tall spare man of "
            "about fifty in a DEEP INDIGO BLUE tunic under a DARK BLUE-BLACK "
            "tasselled mantle, with THICK IRON-GREY HAIR combed back and cut "
            "level at the middle of the neck, a clear band of that iron-grey "
            "hair showing at the nape — is well up the stair, right of centre, "
            "back straight, taking the courses evenly. THE TAX COLLECTOR — a "
            "thickset man of about thirty-eight in a DEEP RUST-BROWN tunic "
            "under a DARK OLIVE-GREEN mantle, BAREHEADED, with SHORT COARSE "
            "BLACK HAIR cut at the neck — is far below him and off to the LEFT "
            "edge, much smaller in the frame, one hand on his own knee, "
            "climbing slowly. THE ENORMOUS DISTANCE BETWEEN THE TWO MEN ON THE "
            "STAIR IS THE WHOLE COMPOSITION. WHAT IS AT THE TOP OF THE STAIR, STATED AS A DELETION BECAUSE A "
            "COLONNADE HAS ARRIVED THERE TWICE: the stair simply ENDS at ONE "
            "HIGH BLANK WALL of very large square-cut pale limestone blocks laid "
            "in level courses, pierced by ONE plain SQUARE-TOPPED rectangular "
            "gateway with a single flat lintel, and ABOVE THE TOP OF THAT WALL "
            "THERE IS NOTHING WHATEVER BUT EMPTY SKY. NO BUILDING, ROOF, COLUMN, "
            "PILLAR, COLONNADE, PORTICO, PORCH, PEDIMENT, GABLE, ENTABLATURE OR "
            "STRUCTURE OF ANY KIND RISES ABOVE THAT WALL LINE OR APPEARS "
            "ANYWHERE AGAINST THE SKY. At "
            "most three other people are anywhere on the stair, all of them "
            "small, far off and dressed head to foot in solid dark umber, "
            "charcoal, deep rust or deep indigo."
        ),
    },
    {
        "id": "v2-r039-b06", "out": "s06-a-pharisee-and-a-publican.jpeg",
        "seg": "jv10", "window": "19.628-23.632", "wide": True, "jesus": False,
        "locks": _T_BOTH, "char_refs": _BOTH,
        "narration": "one a Pharisee, and the other a publican.",
        "must_show": "The two men arriving on the vast open paved court through the plain square-topped gate of the portico — the Pharisee striding on ahead into the sunlight, the tax collector stopping just inside the shadow of the piers.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            "One photograph, 28mm lens, the vast open limestone pavement of the "
            "temple court running away into hard bright sunlight, the shaded "
            "colonnade of plain square-section piers in the near ground. "
            + _GRAIN +
            "THE CAMERA STANDS BEHIND BOTH MEN INSIDE THE SHADOW OF THE PORTICO "
            "AND SHOOTS PAST THEM OUT INTO THE LIGHT: both are seen from behind "
            "and in three-quarter from behind, full length, and NEITHER FACE IS "
            "TURNED TOWARD THE LENS. THE PHARISEE, in his DEEP INDIGO BLUE "
            "tunic and DARK BLUE-BLACK tasselled mantle with THICK IRON-GREY "
            "HAIR combed back and cut level at the neck, has already walked out "
            "of the shade and is a dozen paces into the blazing pavement, right "
            "of centre, head up, mantle swinging, his shadow short and hard "
            "beneath him. THE TAX COLLECTOR, thickset, BAREHEADED with SHORT "
            "COARSE BLACK HAIR, in his DEEP RUST-BROWN tunic and DARK "
            "OLIVE-GREEN mantle, has STOPPED dead just inside the shadow at the "
            "LEFT of the frame, close to the camera and large, one shoulder "
            "almost against a pier, looking out and down at the pavement in "
            "front of his own feet so his eyeline goes DOWN and out through the "
            "BOTTOM EDGE. Far across the court the tall plain rectangular block "
            "of the sanctuary stands against the sky with one straight column "
            "of pale grey-white smoke going up beside it. At most three other "
            "worshippers stand out on the pavement, small and far off, every "
            "one of them a solid dark mass of indigo, umber, charcoal or deep "
            "rust from head to foot."
        ),
    },
    # ===== n2 — the narrator on the two men (white) ===========================
    # ANCHOR RUN 1: b07 is the PUBLICAN anchor — alone, face-showing, no other
    # locked character and no Jesus anywhere in the frame.
    {
        "id": "v2-r039-b07", "out": "s07-the-other-a-publican.jpeg",
        "seg": "n2", "window": "23.632-27.522", "wide": False, "jesus": False,
        "locks": ["TEMPLE-COURT", "PUBLICAN", "JUDEAN-LAND"],
        "narration": "The other was a tax collector. And to anyone watching them climb those",
        "must_show": "The tax collector alone, stopped in the shadow of the portico at the edge of the temple court, his face clearly visible in strict side-on profile, eyes lowered, jaw set.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the direction he is "
            "facing, so we see the clean edge of his profile against the "
            "sunlit pavement beyond — the near cheek, the eyelash line, the "
            "short blunt nose in silhouette — and THE FAR CHEEK AND FAR EYE ARE "
            "HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND NOT VISIBLE AT ALL. His "
            "single visible eye is aimed DOWNWARD and forward, out through the "
            "LEFT EDGE at the pavement. The pose itself makes a look into the "
            "lens physically impossible. "
            "One photograph, 85mm lens at f/2.8, head and shoulders and the top "
            "of his chest only, the enormous sunlit limestone court beyond him "
            "thrown completely soft and bright, the shaded square pier he "
            "stands beside dark at the right edge. He is lit by strong sunlight "
            "BOUNCING UP OFF THE PALE PAVEMENT IN FRONT OF HIM, so the light "
            "comes from LOW AND IN FRONT and lands on the underside of his brow, "
            "his cheek and his jaw, while the top and back of his head stay in "
            "shadow; there is no light source anywhere behind or above his head "
            "and nothing outlines his hair. " + _GRAIN +
            "HE IS A THICKSET JUDEAN MAN OF ABOUT THIRTY-EIGHT with warm "
            "sun-darkened olive-brown Middle Eastern skin, a broad face, heavy "
            "cheeks, a short blunt nose, a SHORT CROPPED BLACK BEARD and SHORT "
            "COARSE BLACK HAIR cut roughly at the top of the neck and pushed "
            "back off the forehead, his HEAD BARE, in a DEEP RUST-BROWN wool "
            "tunic with a DARK OLIVE-GREEN mantle pulled round his shoulders. "
            "His mouth is closed and set, the jaw muscle working, the eyes "
            "lowered — plain quiet exhausted shame that is not performing "
            "itself. Nothing else is in the frame: no other person, no shoulder "
            "at any edge, no object in any hand."
        ),
    },
    {
        "id": "v2-r039-b08", "out": "s08-which-god-was-pleased-with.jpeg",
        "seg": "n2", "window": "27.522-32.132", "wide": True, "jesus": False,
        "locks": _T_BOTH, "char_refs": _BOTH,
        "narration": "steps, it was obvious which of the two God was pleased with.",
        "must_show": "Three worshippers standing on the temple pavement whose heads have turned to follow the Pharisee approvingly as he passes, while the tax collector stands unregarded far behind them in the shade.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard bright mid-morning sun from the "
            "upper LEFT laying short black shadows on the huge pale limestone "
            "flags of the open court. " + _GRAIN +
            "THE CAMERA STANDS BEHIND AND ABOVE THE THREE STANDING WORSHIPPERS "
            "AND SHOOTS PAST THEM ACROSS THE COURT: they are seen from behind "
            "and in three-quarter from behind, heads, shoulders and BACKS "
            "filling the near right of the frame, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS — what the camera reads is that ALL THREE HEADS "
            "HAVE SWUNG THE SAME WAY, tracking a man crossing left to right in "
            "front of them. That man is THE PHARISEE, mid-ground and left of "
            "centre, full length, walking across the frame in strict side-on "
            "profile with his chin level and his eyeline running out through "
            "the RIGHT EDGE: a tall spare man of about fifty in a DEEP INDIGO "
            "BLUE tunic under a DARK BLUE-BLACK tasselled mantle, THICK "
            "IRON-GREY HAIR combed back and cut level at the neck, a full "
            "squared iron-grey beard. Far behind them all, small, at the very "
            "back of the frame in the shadow of the square piers, stands THE "
            "TAX COLLECTOR — a thickset BAREHEADED man with SHORT COARSE BLACK "
            "HAIR in a DEEP RUST-BROWN tunic and DARK OLIVE-GREEN mantle — "
            "alone, unnoticed, seen from behind, facing away toward the wall. "
            "Nobody is looking at him. The three worshippers are ordinary "
            "respectful men, NOT sneering and NOT gloating. Every person in the "
            "picture wears any pale cloth at all: all of them are solid dark "
            "saturated masses of indigo, umber, charcoal, deep rust or deep "
            "maroon from edge to edge, in focus and blurred alike."
        ),
    },
]

# ===== n3 — the Pharisee was not a fake (white) ==============================
# ANCHOR RUN 1: b09 is the PHARISEE anchor — alone, face-showing, no other
# locked character and no Jesus anywhere in the frame.
BEATS += [
    {
        "id": "v2-r039-b09", "out": "s09-was-not-a-fake.jpeg",
        "seg": "n3", "window": "32.132-35.742", "wide": False, "jesus": False,
        "locks": ["PHARISEE-HOUSE", "PHARISEE", "JUDEAN-LAND"],
        "narration": "The Pharisee was not a fake. God had asked for one fast a",
        "must_show": "The Pharisee alone against the plain shaded plaster wall of his own house at first light, face clearly visible in strict side-on profile, calm and disciplined, an untouched bowl of food on the stone ledge beside him.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MOCK + _NO_IRONGATE + "no doorway, door opening, door, leaf, plank, shutter, timber post, jamb or dark rectangle anywhere in the frame; no shawl collar, lapel, revers, collar band, placket, front opening, button, hook, tie or fastening on any garment; no coat, cardigan, dressing gown or bathrobe; and no brighter line, fringe, rim, edge or outline along the top of the head, the hair, the beard or the shoulder; " + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the direction he is "
            "facing, so we see the clean edge of his profile against a plain "
            "flat mud-plastered wall — the near cheek, the eyelash line, the "
            "long straight nose in silhouette — and THE FAR CHEEK AND FAR EYE "
            "ARE HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND NOT VISIBLE AT ALL. "
            "His single visible eye is level and aimed straight out through the "
            "LEFT EDGE. The pose itself makes a look into the lens physically "
            "impossible. "
            "LIGHT GEOMETRY, STATED SECOND BECAUSE IT ALSO GOVERNS THIS FRAME: "
            "THE SUN IS IN FRONT OF HIM AND ON THE CAMERA'S SIDE OF HIM, low, "
            "out of frame past the LEFT edge and turned slightly toward the "
            "lens, so its light travels FORWARD onto the front planes of his "
            "face — the brow, the nose, the cheekbone and the front of the "
            "combed beard. NOTHING BEHIND HIM IS A LIGHT SOURCE AND THE WALL "
            "BEHIND HIM IS IN FULL SHADOW AND READS DARKER THAN HE DOES. THE "
            "TOP OF HIS HEAD, THE OUTER EDGE OF HIS HAIR, THE BACK OF HIS NECK "
            "AND THE OUTER EDGE OF HIS SHOULDER ARE ALL DARKER THAN THE WALL "
            "BEHIND THEM AND CARRY NO BRIGHTER LINE, FRINGE, RIM, EDGE OR "
            "SEPARATION WHATEVER. "
            "One photograph, 85mm lens at f/2.8, head and shoulders and the top "
            "of his chest only. THE BACKGROUND IS ONE FLAT SHADED MUD-PLASTERED "
            "WALL A PACE BEHIND HIM, thrown soft, unbroken and featureless — "
            "there is NO doorway, NO opening, NO door, NO leaf, NO plank, NO "
            "timber post, NO stone jamb and NO dark rectangle of any kind "
            "anywhere in the picture. " + _GRAIN +
            "HE IS A TALL SPARE UPRIGHT JUDEAN MAN OF ABOUT FIFTY with WARM "
            "SUN-DARKENED OLIVE-BROWN MIDDLE EASTERN SKIN — never fair, never "
            "pink, never European-looking — a high clear forehead, a long "
            "straight nose, a FULL SQUARED IRON-GREY BEARD carefully combed, "
            "and THICK IRON-GREY HAIR combed straight back off the forehead and "
            "cut level at the middle of the neck, HIS HEAD BARE so that hair "
            "shows at the front edge, the temples and the nape. HIS CLOTHING, "
            "STATED AS GEOMETRY: ONE DEEP INDIGO BLUE finely woven wool tunic "
            "with a plain slit neck, ONE DARK MADDER RED woven sash, and ONE "
            "flat rectangle of DARK BLUE-BLACK wool laid across the BACK of "
            "both shoulders with both ends carried BACKWARD AND DOWN BEHIND "
            "HIM. THE WHOLE FRONT OF HIS CHEST SHOWS ONLY THE UNBROKEN INDIGO "
            "TUNIC: no vertical edge, seam, border, fold or opening of the "
            "mantle runs down the front of him, and there is no shawl collar, "
            "lapel, revers, collar band, placket, button, hook, tie or "
            "fastening anywhere on him. HE IS NOT A VILLAIN: his face is "
            "handsome, composed, serious and completely untroubled, the eyes "
            "bright and steady, nothing sneering or curling anywhere in it. At "
            "the very bottom edge of the frame, softly out of focus, one "
            "shallow fired-clay bowl of barley bread and olives sits UNTOUCHED "
            "on the low stone ledge, exactly as it was set down. Nothing else "
            "is in the frame: no other person, no shoulder at any edge."
        ),
    },
    {
        "id": "v2-r039-b10", "out": "s10-fasted-twice-a-week.jpeg",
        "seg": "n3", "window": "35.742-39.942", "wide": False, "jesus": False,
        "locks": ["PHARISEE-HOUSE", "PHARISEE", "JUDEAN-LAND"],
        "narration": "fast a year, and this man fasted twice a week. He gave away a tenth of",
        "must_show": "A close macro of the Pharisee's own hands winding the narrow plain leather strap of a small first-century phylactery round his left forearm, the untouched bowl of food soft in the background behind them.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _GAZE + "no buckle, roller buckle, frame, pin, prong, eyelet, grommet, rivet, stud, snap, clasp, hook, ring or fitting of metal anywhere on the strap or the cube; and no printing, lettering, numeral or stamp on anything; ",
        "scene": (
            "One photograph, 100mm macro lens at f/2.8, filling the frame with "
            "two hands and one forearm and nothing else. " + _GRAIN +
            "THE CAMERA LOOKS DOWN AND ACROSS AT THE HANDS FROM THE SIDE, "
            "slightly behind the working right hand, so no face and no head "
            "is anywhere in the picture. THE HANDS ARE A MAN'S: long, brown, "
            "clean, broad across the knuckles, the nails trimmed short, the "
            "skin warm olive-brown and lightly weathered on the backs — clearly "
            "an adult man's hands and clearly Middle Eastern. The right hand is "
            "drawing a NARROW PLAIN DARK BROWN LEATHER STRAP, hand-cut, its "
            "edges slightly uneven, in a neat spiral turn round the bare left "
            "forearm; the strap runs up to ONE LITTLE CUBE OF PLAIN DARK BROWN "
            "LEATHER about the size of a thumb joint seated against the inside "
            "of the upper arm, and the strap is held simply by being tucked "
            "back under its own turns. The sleeve of the DEEP INDIGO BLUE wool "
            "tunic is pushed up above the elbow and its coarse hand-woven "
            "over-and-under weave is clearly visible at the fold. Low "
            "horizontal first light from the LEFT rakes across the skin and the "
            "leather. Behind the hands, thrown completely soft, the shallow "
            "fired-clay bowl of barley bread and olives sits untouched on the "
            "stone ledge. Nothing else is in the frame."
        ),
    },
    {
        "id": "v2-r039-b11", "out": "s11-down-to-the-herbs.jpeg",
        "seg": "n3", "window": "39.942-44.202", "wide": False, "jesus": False,
        "locks": ["PHARISEE-HOUSE", "PHARISEE", "JUDEAN-LAND"],
        "narration": "everything he owned, down to the herbs in his garden. Ask that city who",
        "must_show": "EXACTLY TEN bundles of freshly cut grey-green kitchen herbs on ONE stone ledge — nine in one straight countable row and the tenth pushed a hand's width apart — with a BARE forearm reaching in and no sleeve or cloth anywhere in frame.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _GAZE + "no vague heap, pile, handful, bunch, basketful or uncountable mass of herbs, no eleventh bundle, no ninth-and-no-more, no bundle on any second surface, lower step or the ground; no sleeve, cuff, wrist band, hem or any cloth in the frame; no knitted, ribbed, jersey, fleece or sweater texture anywhere; and no pot, tray, punnet, label, tag or lettering on anything; ",
        "scene": (
            "One photograph, 100mm macro lens at f/4 so the whole ledge stays "
            "sharp, looking steeply DOWN onto a low stone ledge from just above "
            "and to the SIDE, so no face and no head is anywhere in the "
            "picture. " + _GRAIN +
            "COUNT AS GEOMETRY, AND THE ARITHMETIC IS EXACT: there are TEN "
            "BUNDLES IN THIS PICTURE AND TEN ONLY — NINE of them lie in ONE "
            "SINGLE STRAIGHT EVEN ROW along the flat top of ONE stone ledge, "
            "all nine on THAT SAME ONE SURFACE, evenly spaced with a clear "
            "finger's width of bare stone between each, and THE TENTH lies a "
            "clear hand's width apart from the end of that row ON THE SAME "
            "LEDGE. NINE PLUS ONE MAKES TEN AND THE VIEWER CAN COUNT THEM. "
            "There is no eleventh bundle, no eighth-and-no-more, no bundle on "
            "any lower step, any second ledge, any other surface or the ground, "
            "and no loose heap, pile, handful or scatter of stems anywhere. "
            "Each bundle is low grey-green mint and rue, stems together and "
            "tied once with plain undyed flax thread, leaves fanned, about the "
            "size of two fingers. A BARE MAN'S ARM reaches into the frame from "
            "the near edge — long, brown, clean, broad-knuckled, warm "
            "olive-brown, the forearm BARE SKIN ALL THE WAY OUT OF THE FRAME "
            "WITH NO SLEEVE, CUFF, WRIST BAND, HEM OR CLOTH OF ANY KIND "
            "ANYWHERE IN THE PICTURE — and two fingertips rest on the tenth, "
            "separated bundle. Low horizontal "
            "first light from the LEFT rakes across the stone and throws each "
            "of the ten small shadows in the same direction. Nothing else is in "
            "the frame."
        ),
    },
    {
        "id": "v2-r039-b12", "out": "s12-every-finger-pointed-at-him.jpeg",
        "seg": "n3", "window": "44.202-48.307", "wide": True, "jesus": False,
        "locks": ["PHARISEE", "JUDEAN-LAND", "MARKET-TOWN", "BACKGROUND-CAST"],
        "narration": "its best man was, and every finger would have pointed at him.",
        "must_show": "The Pharisee walking up a narrow dusty town lane while three townspeople step aside and incline their heads to him as he passes, seen past their backs.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MOCK + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            "One photograph, 35mm lens, early morning, the low sun coming down "
            "the lane from the far end and OUT of frame, the tan mud-brick "
            "house walls on either side, FLAT roofs of poles and packed earth "
            "against a high dry pale blue sky. " + _GRAIN +
            "THE CAMERA STANDS BEHIND THE THREE TOWNSPEOPLE AND SHOOTS PAST "
            "THEM UP THE LANE: they fill the lower and left of the frame as "
            "heads, shoulders and BACKS seen from behind and in three-quarter "
            "from behind, pressed back against the wall to let a man through, "
            "one of them with his head inclined; NOT ONE FACE IS TURNED TOWARD "
            "THE LENS. THE PHARISEE walks up the middle of the lane away from "
            "the camera, mid-ground, full length from head to sandals, seen "
            "from BEHIND and slightly to the side — a tall spare upright man of "
            "about fifty in a DEEP INDIGO BLUE tunic under a DARK BLUE-BLACK "
            "tasselled mantle, the four plain undyed wool corner tassels "
            "swinging, THICK IRON-GREY HAIR combed back and cut level at the "
            "middle of the neck with a clear band of that iron-grey hair "
            "showing at the nape. He does not look at anybody. THIS IS A WIDE "
            "FULL-LENGTH STREET PHOTOGRAPH AND NOT A PORTRAIT: the camera is "
            "far enough back that all four people, the full width of the lane "
            "and the roofline against the sky are in frame together. Every "
            "person in the picture is a solid dark saturated mass of indigo, "
            "umber, charcoal, deep rust or deep maroon from head to foot, in "
            "focus and blurred alike, and NO PALE OR OFF-WHITE CLOTH APPEARS "
            "ANYWHERE."
        ),
    },
]

# ===== n4 — the tax collector was exactly what they thought (white) ==========
BEATS += [
    {
        "id": "v2-r039-b13", "out": "s13-exactly-what-they-thought.jpeg",
        "seg": "n4", "window": "48.307-52.117", "wide": True, "jesus": False,
        "locks": _TOLL, "char_refs": _PUB,
        "narration": "The tax collector was exactly what everyone thought he was.",
        "must_show": "The tax collector sitting low behind his single low timber slab table in the dust beside the town gate, seen from the side, coins in small counted heaps in front of him.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_OFFICE + _NO_MOCK + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard high mid-morning sun, the plain "
            "square-topped town gateway of dressed pale limestone standing "
            "behind and to the right, its opening a clear dark rectangle, bare "
            "packed earth and pale dust underfoot. " + _GRAIN +
            "THE CAMERA STANDS OFF TO THE SIDE AT A RIGHT ANGLE TO THE TABLE "
            "AND SHOOTS ACROSS IT, so the seated man is in near-strict side-on "
            "profile with his far cheek foreshortened and his single visible "
            "eye aimed DOWN at the table top and out through the LEFT EDGE; HIS "
            "PUPILS NEVER COME ROUND ONTO THE LENS AXIS. He sits LOW, "
            "cross-legged on a folded dark wool mat in the dust in the shade of "
            "one rectangle of undyed dark goat-hair cloth slung from rough "
            "poles, behind a SINGLE LOW TABLE that is one weathered silver-grey "
            "adzed timber slab laid across two undressed stone blocks about "
            "knee high. He is a thickset BAREHEADED Judean man of about "
            "thirty-eight with SHORT COARSE BLACK HAIR cut at the top of the "
            "neck, a SHORT CROPPED BLACK BEARD and warm sun-darkened "
            "olive-brown skin, in a DEEP RUST-BROWN wool tunic and a DARK "
            "OLIVE-GREEN mantle. On the slab, and nothing else: loose struck "
            "coins of dull silver and dark bronze pushed into four small "
            "separate counted heaps, ONE WIDE SHALLOW HAND-THROWN FIRED-CLAY BOWL "
            "holding more of them — there is NO wooden box, chest, tray or "
            "container of planks anywhere on the table or near it — and one "
            "hand-woven reed basket of loose rolled papyrus sheets. THIS IS A WIDE FULL-LENGTH SCENE AND NOT A "
            "PORTRAIT: the camera is far enough back that the whole table, the "
            "man from head to sandals, the cloth awning and the gateway behind "
            "are in frame together. Two travellers with a laden donkey wait in "
            "the dust further off, both of them solid dark masses of umber and "
            "charcoal from head to foot, seen from behind."
        ),
    },
    {
        "id": "v2-r039-b14", "out": "s14-he-worked-for-rome.jpeg",
        "seg": "n4", "window": "52.117-56.017", "wide": False, "jesus": False,
        "locks": ["TOLL-STATION", "PUBLICAN", "JUDEAN-LAND"],
        "narration": "He worked for Rome, the empire occupying his own country,",
        "must_show": "A macro of one struck silver coin held up between the tax collector's thumb and forefinger, the ruler's head in profile and the worn rim legend clearly readable as a struck coin.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_OFFICE + _GAZE + "no modern coin, milled edge, machine-perfect rim, arabic numeral, date, banknote or paper money; no sleeve, cuff, wrist band, hem or any cloth in the frame; no knitted, ribbed, jersey, cabled, fleece or sweater texture anywhere; ",
        "scene": (
            "One photograph, 100mm macro lens at f/2.8, filling the frame with "
            "one hand and one coin and nothing else. " + _GRAIN +
            "THE CAMERA LOOKS ACROSS AT THE HAND FROM THE SIDE and slightly "
            "above, so no face and no head is anywhere in the picture. A MAN'S "
            "HAND — broad, thick-fingered, warm sun-darkened olive-brown, "
            "soft-palmed, ink-stained along the first two fingers, the nails "
            "short, THE FOREARM BARE SKIN ALL THE WAY OUT OF THE FRAME WITH NO "
            "SLEEVE, CUFF, WRIST BAND, HEM OR CLOTH OF ANY KIND ANYWHERE IN "
            "THE PICTURE — holds ONE "
            "single small STRUCK SILVER COIN edge-on between thumb and "
            "forefinger, turned up toward the light. The coin is hand-struck "
            "and imperfect: slightly oval, its edge irregular and unmilled, its "
            "surface worn smooth at the high points, bearing a RULER'S HEAD IN "
            "PROFILE facing right and a worn ring of Latin rim letters around "
            "it, the letters shallow, uneven and partly rubbed away. Hard high "
            "sunlight from the upper LEFT catches the raised profile and throws "
            "the low relief into sharp relief. Behind the hand, thrown "
            "completely soft, the weathered silver-grey timber slab of the "
            "table and the dull heaps of more coins on it. Nothing else is in "
            "the frame."
        ),
    },
    {
        "id": "v2-r039-b15", "out": "s15-from-his-own-neighbors.jpeg",
        "seg": "n4", "window": "56.017-59.997", "wide": True, "jesus": False,
        "locks": _TOLL, "char_refs": _PUB,
        "narration": "collecting from his own neighbors, and keeping whatever extra he could squeeze out",
        "must_show": "A poor neighbour standing at the low table with his hands empty and open, and the tax collector's hand sweeping the man's coins across the timber slab toward himself, neither man looking at the other's face.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_OFFICE + _NO_MOCK + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            "One photograph, 50mm lens, hard high midday sun straight down, "
            "short black shadows in the dust, the awning cloth casting a hard "
            "rectangle of shade across the table. " + _GRAIN +
            "THE CAMERA STANDS BEHIND AND BESIDE THE STANDING NEIGHBOUR AND "
            "SHOOTS PAST HIM DOWN ACROSS THE TABLE: the neighbour fills the "
            "near LEFT of the frame from the waist up, seen ENTIRELY FROM "
            "BEHIND, a thin man in a patched DARK UMBER tunic with dusty bare "
            "forearms, his two hands hanging open and empty at his sides; his "
            "face is not visible at all. Beyond and below him, sharp, THE TAX "
            "COLLECTOR sits low behind the weathered timber slab in near-strict "
            "side-on profile, his single visible eye aimed DOWN at the table "
            "top; his broad thick-fingered right hand is dragging four dull "
            "bronze coins across the wood toward his own side, the fingers "
            "curled. He is a thickset BAREHEADED man of about thirty-eight with "
            "SHORT COARSE BLACK HAIR cut at the neck and a SHORT CROPPED BLACK "
            "BEARD, in a DEEP RUST-BROWN tunic and DARK OLIVE-GREEN mantle. "
            "NEITHER MAN IS LOOKING AT THE OTHER'S FACE and NOT ONE PAIR OF "
            "PUPILS IS CENTRED ON THE LENS. THIS IS A WIDE FULL-LENGTH SCENE "
            "AND NOT A PORTRAIT: the whole table, both men, the awning poles "
            "and the dusty road beyond are in frame together. At most two other "
            "travellers wait further off, solid dark masses of charcoal and "
            "umber from head to foot."
        ),
    },
    {
        "id": "v2-r039-b16", "out": "s16-and-he-knew-it.jpeg",
        "seg": "n4", "window": "59.997-64.171", "wide": False, "jesus": False,
        "locks": ["TOLL-STATION", "PUBLICAN", "JUDEAN-LAND"],
        "narration": "of them. A traitor with a money box. And he knew it.",
        "must_show": "The tax collector alone after everyone has gone, sitting still behind the table looking down at the open plank box of coins, his face in profile carrying plain quiet self-knowledge.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_OFFICE + _NO_MOCK + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the direction he is "
            "facing, so we see the clean edge of his profile against the sunlit "
            "dust beyond, and THE FAR CHEEK AND FAR EYE ARE HIDDEN BEHIND THE "
            "BRIDGE OF HIS NOSE AND NOT VISIBLE AT ALL. His single visible eye "
            "is aimed steeply DOWN into the open box on the table and out "
            "through the BOTTOM LEFT of the frame. The pose itself makes a look "
            "into the lens physically impossible. "
            "One photograph, 85mm lens at f/2.8, head, shoulders and the near "
            "edge of the timber slab only; the dusty road behind him thrown "
            "completely soft and empty — everybody has gone. Hard afternoon "
            "sunlight BOUNCES UP off the pale dust in front of him and lands on "
            "the underside of his brow, his heavy cheek and his jaw, while the "
            "top and back of his head stay in shadow; there is no light source "
            "anywhere behind or above his head. " + _GRAIN +
            "He is a thickset Judean man of about thirty-eight with warm "
            "sun-darkened olive-brown skin, a broad face and heavy cheeks, a "
            "SHORT CROPPED BLACK BEARD, SHORT COARSE BLACK HAIR cut at the top "
            "of the neck, HIS HEAD BARE, in a DEEP RUST-BROWN tunic and DARK "
            "OLIVE-GREEN mantle. He is completely still. His mouth is closed, "
            "the jaw set, the eyes lowered into the WIDE SHALLOW HAND-THROWN "
            "FIRED-CLAY BOWL of dull coins at the bottom of the frame — A BOWL "
            "OF FIRED CLAY AND NOT A BOX: there is no wooden box, chest, tray, "
            "till or container of planks anywhere in the picture, and no lid, "
            "hinge, hasp, staple, clasp, band, bracket, nail head or metal "
            "fitting of any kind — a man who knows exactly "
            "what he is, with no self-pity in it and nothing theatrical about "
            "it. He is NOT sneering, NOT gloating and NOT weeping. Nothing "
            "else is in the frame: no other person, no shoulder at any edge."
        ),
    },
]

# ===== n5 + j1 — the Pharisee prays. POSITION A, the fixed camera. ===========
# THE RED LETTERS OF j1 BELONG TO THE PHARISEE, NOT TO JESUS. Jesus is in none
# of these four frames; putting his face under "God, I thank thee, that I am
# not as other men are" would invert the line completely.
BEATS += [
    {
        "id": "v2-r039-b17", "out": "s17-out-in-the-open.jpeg",
        "seg": "n5", "window": "64.171-68.661", "wide": True, "jesus": False,
        "locks": _T_PHA, "char_refs": _PHA,
        "narration": "The Pharisee took his place out in the open, where he could be seen, and lifted his",
        "must_show": "POSITION A, ESTABLISHED HERE AND RETURNED TO LATER: the Pharisee walking out alone to the open middle of the vast temple pavement, seen from behind and above, with the sanctuary and the smoke of the altar far ahead of him.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "THIS IS CAMERA POSITION A AND IT IS FIXED: a 35mm lens standing "
            "BEHIND THE PHARISEE AND ABOUT A MAN'S HEIGHT ABOVE HIM, looking "
            "out across the enormous open limestone pavement of the temple "
            "court toward the far sanctuary. This exact framing, this exact "
            "spot on the pavement and this exact distance are used again later "
            "in the story; only the light and the crowd will change. " + _GRAIN +
            "THE CAMERA SHOOTS PAST HIM: he is seen ENTIRELY FROM BEHIND, full "
            "length from head to sandals, alone, left of centre and walking "
            "AWAY from the lens into the light, and HIS FACE IS NOT VISIBLE AT "
            "ALL. A tall spare upright man of about fifty in a DEEP INDIGO BLUE "
            "tunic under a DARK BLUE-BLACK tasselled mantle, THICK IRON-GREY "
            "HAIR combed back and cut level at the middle of the neck with a "
            "clear band of that iron-grey hair showing at the nape. He has just "
            "stopped in the middle of a great empty rectangle of sunlit "
            "pavement with nobody within twenty paces of him, and his short "
            "hard shadow lies on the stone beside him. Hard bright "
            "late-morning sun comes from the upper LEFT and IN FRONT of him; "
            "the sun is well out of frame and there is no light source behind "
            "or above his head. Far across the court the tall plain "
            "rectangular block of the sanctuary stands against a high dry pale "
            "blue sky with one straight column of pale grey-white smoke rising "
            "beside it. At most three other worshippers stand far off along the "
            "edges, small, every one a solid dark mass of indigo, umber, "
            "charcoal or deep rust from head to foot."
        ),
    },
    {
        "id": "v2-r039-b18", "out": "s18-lifted-his-hands.jpeg",
        "seg": "n5", "window": "68.661-73.469", "wide": False, "jesus": False,
        "locks": _T_PHA, "char_refs": _PHA,
        "narration": "his hands to pray. Listen to who his prayer is really about.",
        "must_show": "The Pharisee's two hands lifted open and level in front of him against the bright empty pavement, seen from the side, with his chin lifted at the top of the frame.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _GAZE,
        "scene": (
            "One photograph, 85mm lens at f/2.8, THE CAMERA STANDING AT A RIGHT "
            "ANGLE TO HIM AND SHOOTING ACROSS, filling the frame with his two "
            "raised forearms and hands and the underside of his lifted jaw at "
            "the very top edge; his eyes are ABOVE THE TOP EDGE OF THE FRAME "
            "AND NOT VISIBLE AT ALL, so no gaze of any kind can meet the lens. "
            + _GRAIN +
            "BOTH HANDS ARE A MAN'S: long, brown, clean, broad across the "
            "knuckles, the nails trimmed short, the skin warm olive-brown and "
            "lightly weathered on the backs. They are raised to shoulder height "
            "and held OPEN AND STEADY, palms turned upward and slightly "
            "outward, fingers relaxed and separated — the ordinary standing "
            "prayer posture, unhurried and practised, not clasped, not folded, "
            "not clenched. The sleeves of the DEEP INDIGO BLUE hand-woven wool "
            "tunic fall back from the wrists showing their coarse "
            "over-and-under weave, and one corner of the DARK BLUE-BLACK "
            "mantle with its short plain undyed wool tassel hangs beside the "
            "left forearm. On the left upper arm, partly in frame, the small "
            "plain dark brown leather cube on its narrow tucked leather strap. "
            "Behind the hands the enormous sunlit limestone pavement is thrown "
            "completely soft and bright and is EMPTY. Hard high sun from the "
            "upper LEFT and IN FRONT lands on the backs of the hands and the "
            "underside of the jaw; there is no light source behind or above "
            "his head."
        ),
    },
    {
        "id": "v2-r039-b19", "out": "s19-i-thank-thee.jpeg",
        "seg": "j1", "window": "73.469-77.299", "wide": False, "jesus": False,
        "locks": _T_PHA, "char_refs": _PHA,
        "narration": "God, I thank thee, that I am not as other men are,",
        "must_show": "The Pharisee praying aloud, strictly side-on, his lips shaping a word, his face calm and completely certain — this red line is HIS, spoken by him, and Jesus is nowhere in this picture.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_MOCK + _GAZE + "no second man, no figure in cream or off-white, and nobody resembling Jesus anywhere in the frame; ",
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the direction he "
            "faces, so we see the clean edge of his profile against the bright "
            "soft pavement beyond — the near cheek, the eyelash line, the long "
            "straight nose in silhouette — and THE FAR CHEEK AND FAR EYE ARE "
            "HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND NOT VISIBLE AT ALL. His "
            "single visible eye is open, level and aimed slightly UPWARD and "
            "forward, out through the RIGHT EDGE at the open sky above the far "
            "wall. The pose itself makes a look into the lens physically "
            "impossible. "
            "One photograph, 85mm lens at f/2.8, head and shoulders only, the "
            "enormous sunlit court behind him thrown completely soft and "
            "EMPTY — there is no second person anywhere in this picture. Hard "
            "high late-morning sun from the LEFT and IN FRONT lands on the "
            "brow, the nose, the cheekbone and the combed beard while the back "
            "and top of his head stay in his own shadow; the sun is well out of "
            "frame and there is no light source behind or above his head. "
            + _GRAIN +
            "He is a tall spare Judean man of about fifty with warm olive-brown "
            "Middle Eastern skin, a high clear forehead, a long straight nose, "
            "a FULL SQUARED IRON-GREY BEARD carefully combed and THICK "
            "IRON-GREY HAIR combed straight back and cut level at the middle of "
            "the neck, HIS HEAD BARE, in a DEEP INDIGO BLUE tunic and DARK "
            "BLUE-BLACK tasselled mantle. His lips are parted mid-word and his "
            "chin is lifted a little. His expression is CALM, WARM, SINCERE AND "
            "COMPLETELY UNTROUBLED — a good man saying what he honestly "
            "believes — and there is nothing sneering, gloating, curling or "
            "comic anywhere in it. The sky above the far wall is ordinary high "
            "dry pale blue daylight and nothing else is in it."
        ),
    },
    {
        "id": "v2-r039-b20", "out": "s20-extortioners-unjust.jpeg",
        "seg": "j1", "window": "77.299-80.459", "wide": False, "jesus": False,
        "locks": _T_PHA, "char_refs": _PHA,
        "narration": "extortioners, unjust, adulterers, or even as this",
        "must_show": "A tighter three-quarter-from-behind view of the Pharisee's head and raised hand as he counts the list off, his eyes narrowing very slightly.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_MOCK + _GAZE + "no second man, no figure in cream or off-white, and nobody resembling Jesus anywhere in the frame; ",
        "scene": (
            "One photograph, 85mm lens at f/2.8. THE CAMERA STANDS BEHIND HIS "
            "RIGHT SHOULDER AND SLIGHTLY ABOVE, SHOOTING PAST HIM: we see the "
            "back and side of his head, the ear, the line of the jaw and only "
            "the far edge of the cheekbone — HIS EYES ARE ON THE FAR SIDE OF "
            "HIS HEAD AND BARELY VISIBLE, and his whole face is turned away "
            "from the lens toward the bright open pavement beyond, so no gaze "
            "can reach the camera. " + _GRAIN +
            "THICK IRON-GREY HAIR combed straight back off the forehead and cut "
            "level at the middle of the neck fills the near part of the frame, "
            "a clear band of it showing at the nape above the DARK BLUE-BLACK "
            "wool of the mantle across his shoulder, the coarse hand-woven "
            "over-and-under weave of that mantle sharp in the raking light. "
            "His right hand is raised into the frame beside his head, open, "
            "with the index finger of the left hand just touching one lifted "
            "finger of it — a man ticking items off. Hard high sun from the "
            "upper LEFT and IN FRONT of him lands on the pavement beyond and on "
            "the side of his face; the back of his head is in his own shadow "
            "and reads DARKER than the bright stone behind it, with no bright "
            "outline, edge or ring anywhere around his hair. The enormous "
            "sunlit court beyond is thrown completely soft and EMPTY."
        ),
    },
]

BEATS += [
    {
        "id": "v2-r039-b21", "out": "s21-as-this-publican.jpeg",
        "seg": "j1", "window": "80.459-84.299", "wide": True, "jesus": False,
        "locks": _T_BOTH, "char_refs": _BOTH,
        "narration": "publican. I fast twice in the week, I give",
        "must_show": "Past the Pharisee's shoulder, his eyeline running back across the whole width of the sunlit court to the tiny figure of the tax collector standing alone at the far wall.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 35mm lens at f/4, hard high late-morning sun from "
            "the upper LEFT, the enormous pale limestone pavement running away "
            "from the near ground to a far wall of very large square-cut "
            "blocks. " + _GRAIN +
            "THE CAMERA STANDS BEHIND THE PHARISEE'S LEFT SHOULDER AND SHOOTS "
            "PAST HIM DIAGONALLY ACROSS THE COURT: he fills the near LEFT third "
            "of the frame from the chest up, seen from BEHIND AND IN "
            "THREE-QUARTER FROM BEHIND, his head turned away to his own right "
            "so only the far edge of his cheekbone shows and HIS FACE IS NOT "
            "PRESENTED TO THE LENS AT ALL. THICK IRON-GREY HAIR combed back and "
            "cut level at the middle of the neck, a clear band of it at the "
            "nape, DARK BLUE-BLACK tasselled wool across the shoulder. EVEN "
            "FROM THIS ANGLE HIS FULL THICK CAREFULLY COMBED IRON-GREY BEARD "
            "IS VISIBLE AS IT PASSES THE LINE OF HIS JAW AND CHEEK — HE IS "
            "NEVER CLEAN-SHAVEN, NEVER STUBBLED AND NEVER BARE-CHINNED IN ANY "
            "PICTURE. HIS "
            "EYELINE IS THE COMPOSITION: it runs from him diagonally away "
            "across the whole sunlit width of the pavement to the far RIGHT of "
            "the frame, where THE TAX COLLECTOR stands ALONE and VERY SMALL "
            "against the base of the great far wall — a thickset BAREHEADED "
            "figure with SHORT COARSE BLACK HAIR in a DEEP RUST-BROWN tunic and "
            "DARK OLIVE-GREEN mantle, head down, seen from behind and to the "
            "side, no bigger in the frame than a thumb. THE ENORMOUS EMPTY "
            "DISTANCE OF BURNING PAVEMENT BETWEEN THE TWO MEN IS THE WHOLE "
            "PICTURE and nobody else stands in it. At most three other "
            "worshippers are visible right at the far edges, small and dark. "
            "Every person in the frame is a solid dark saturated mass of "
            "indigo, umber, charcoal, rust or olive from head to foot."
        ),
    },
    {
        "id": "v2-r039-b22", "out": "s22-tithes-of-all-i-possess.jpeg",
        "seg": "j1", "window": "84.299-88.124", "wide": False, "jesus": False,
        "locks": _T_PHA, "char_refs": _PHA,
        "narration": "I give tithes of all that I possess.",
        "must_show": "A macro of the Pharisee's open right hand held out palm up against the bright empty pavement, the fingers spread as though presenting something, with nothing in it.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _GAZE + "no coin, purse, scroll, sheet, bag or object of any kind lying in the palm; ",
        "scene": (
            "One photograph, 100mm macro lens at f/2.8, THE CAMERA LOOKING "
            "ACROSS AT THE HAND FROM THE SIDE and slightly above, filling the "
            "frame with one hand, one forearm and the soft bright pavement "
            "behind; no face and no head is anywhere in the picture. " + _GRAIN +
            "THE HAND IS A MAN'S: long, brown, clean, broad across the "
            "knuckles, the tendons standing on the back, the nails trimmed "
            "short, the skin warm olive-brown and lightly weathered. It is held "
            "out at chest height, PALM UP AND WIDE OPEN, the fingers spread and "
            "slightly cupped as though presenting something for inspection — "
            "and THE PALM IS COMPLETELY EMPTY, bare skin from wrist to "
            "fingertips with nothing resting in it. The sleeve of the DEEP "
            "INDIGO BLUE hand-woven wool tunic falls back from the wrist "
            "showing its coarse over-and-under weave, and the DARK BLUE-BLACK "
            "mantle with its short plain undyed wool corner tassel hangs across "
            "the forearm. Hard high sun from the upper LEFT rakes across the "
            "palm lines and throws a crisp shadow of the fingers onto the wrist. "
            "The enormous sunlit limestone court behind is thrown completely "
            "soft, bright and EMPTY. Nothing else is in the frame."
        ),
    },
    # ===== n6 — he is not asking God for anything (white) ====================
    {
        "id": "v2-r039-b23", "out": "s23-not-asking-for-anything.jpeg",
        "seg": "n6", "window": "88.124-92.254", "wide": True, "jesus": False,
        "locks": _T_PHA, "char_refs": _PHA,
        "narration": "He is not asking God for anything. He is handing God a list of his own",
        "must_show": "POSITION A AGAIN, the identical fixed framing of the same spot on the pavement, the Pharisee standing in it with both hands raised, the court around him unchanged.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "THIS IS CAMERA POSITION A AGAIN AND IT HAS NOT MOVED: the same "
            "35mm lens standing BEHIND THE PHARISEE AND ABOUT A MAN'S HEIGHT "
            "ABOVE HIM, the same spot on the enormous open limestone pavement, "
            "the same distance, the same far sanctuary and the same straight "
            "column of pale grey-white smoke beyond it. THE COMPOSITION IS "
            "DELIBERATELY IDENTICAL TO THE EARLIER FRAME OF THIS SPOT; only he "
            "has changed. " + _GRAIN +
            "THE CAMERA SHOOTS PAST HIM: he is seen ENTIRELY FROM BEHIND, full "
            "length from head to sandals, alone, left of centre, standing "
            "still now with BOTH ARMS RAISED to shoulder height and both hands "
            "open, and HIS FACE IS NOT VISIBLE AT ALL. A tall spare upright man "
            "of about fifty in a DEEP INDIGO BLUE tunic under a DARK "
            "BLUE-BLACK tasselled mantle, THICK IRON-GREY HAIR combed back and "
            "cut level at the middle of the neck with a clear band of that "
            "iron-grey hair showing at the nape. Nobody is within twenty paces "
            "of him and his short hard shadow lies on the stone beside him. "
            "Hard bright late-morning sun comes from the upper LEFT and IN "
            "FRONT of him; the sun is well out of frame and there is no light "
            "source behind or above his head. At most three other worshippers "
            "stand far off along the edges, small, every one a solid dark mass "
            "of indigo, umber, charcoal or deep rust from head to foot."
        ),
    },
    {
        "id": "v2-r039-b24", "out": "s24-says-the-word-i.jpeg",
        "seg": "n6", "window": "92.254-96.754", "wide": False, "jesus": False,
        "locks": _T_PHA, "char_refs": _PHA,
        "narration": "of his own achievements. In one short prayer, he says the word I five times",
        "must_show": "A very tight side-on macro of the Pharisee's mouth and beard mid-word, the lips shaping a vowel, the jaw and throat working.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_MOCK + _GAZE + "no eyes visible in the frame at all; ",
        "scene": (
            "One photograph, 100mm macro lens at f/2.8, THE CAMERA AT A RIGHT "
            "ANGLE TO HIM SHOOTING STRAIGHT ACROSS. The frame is cropped to the "
            "lower half of his face only — the mouth, the moustache, the "
            "combed beard, the line of the jaw and the front of the throat — "
            "and HIS EYES ARE ABOVE THE TOP EDGE OF THE FRAME AND NOT VISIBLE "
            "AT ALL, so no gaze of any kind can meet the lens. " + _GRAIN +
            "The lips are parted mid-vowel, the lower lip drawn slightly down, "
            "the tip of the tongue not visible; the tendon at the side of the "
            "throat stands out a little as the jaw drops. The skin is warm "
            "olive-brown, clearly Middle Eastern, lightly weathered, with fine "
            "lines running down from the corner of the mouth into the "
            "moustache. The beard is FULL, THICK AND IRON-GREY, carefully "
            "combed downward and squared off at the jaw, each hair separately "
            "readable in the raking light. Below it the neck of a DEEP INDIGO "
            "BLUE hand-woven wool tunic shows its coarse over-and-under weave "
            "at a plain slit opening. Hard high sun from the LEFT and IN FRONT "
            "rakes across the mouth and the beard; the enormous sunlit court "
            "behind is thrown completely soft and empty, and there is no light "
            "source behind or above his head. Nothing else is in the frame."
        ),
    },
    {
        "id": "v2-r039-b25", "out": "s25-the-man-behind-him.jpeg",
        "seg": "n6", "window": "96.754-101.426", "wide": True, "jesus": False,
        "locks": _T_BOTH, "char_refs": _BOTH,
        "narration": "and he cannot even finish it without stepping on the man behind him.",
        "must_show": "THE ONE FRAME THAT HOLDS BOTH MEN: a wide high view of the whole court with the Pharisee large in the near ground with his arms up, and the tax collector tiny and alone against the far wall, the enormous empty pavement between them.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "THIS IS THE COMPOSITION THE WHOLE PARABLE LIVES IN. One "
            "photograph, 28mm lens at f/5.6 so both men stay readable, THE "
            "CAMERA STANDING HIGH AND BEHIND THE PHARISEE and shooting past him "
            "straight down the long axis of the enormous open limestone "
            "pavement. " + _GRAIN +
            "IN THE NEAR GROUND, LEFT OF CENTRE AND LARGE, THE PHARISEE seen "
            "ENTIRELY FROM BEHIND, full length from head to sandals, both arms "
            "raised and open, HIS FACE NOT VISIBLE AT ALL — a tall spare "
            "upright man of about fifty in a DEEP INDIGO BLUE tunic under a "
            "DARK BLUE-BLACK tasselled mantle, THICK IRON-GREY HAIR combed back "
            "and cut level at the neck, a clear band of it at the nape. FAR "
            "AWAY AT THE BOTTOM OF THE FRAME'S DEPTH, at the base of the great "
            "far wall of very large square-cut blocks, THE TAX COLLECTOR stands "
            "ALONE AND VERY SMALL, no taller in the frame than a finger joint, "
            "seen from behind and to the side, head down, shoulders rounded — "
            "thickset, BAREHEADED, SHORT COARSE BLACK HAIR, DEEP RUST-BROWN "
            "tunic, DARK OLIVE-GREEN mantle. BETWEEN THEM LIES AN ENORMOUS "
            "UNBROKEN RECTANGLE OF EMPTY BURNING PAVEMENT with nobody standing "
            "in it at all. Hard high late-morning sun from the upper LEFT, "
            "short hard shadows, the tall plain rectangular sanctuary and its "
            "single straight column of pale grey-white smoke standing against a "
            "high dry pale blue sky at the top of the frame. At most three "
            "other worshippers stand far off at the very edges, tiny, every one "
            "a solid dark mass from head to foot, and NO PALE OR OFF-WHITE "
            "CLOTH APPEARS ON ANY OF THEM."
        ),
    },
]

# ===== jv13a + n7 + j2 — the publican. POSITION B, the back wall. ============
# jv13a is Jesus narrating INSIDE his own parable, so it is staged on the
# publican; j2 is the publican's own prayer and is his face.
BEATS += [
    {
        "id": "v2-r039-b26", "out": "s26-standing-afar-off.jpeg",
        "seg": "jv13a", "window": "101.426-106.036", "wide": True, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "And the publican, standing afar off, would not lift up so much as his eyes unto",
        "must_show": "POSITION B, ESTABLISHED HERE: the tax collector standing alone at the very back of the court close under the great blank wall, seen from behind and above, the whole vast pavement running away in front of him.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "THIS IS CAMERA POSITION B: a 35mm lens standing BEHIND THE TAX "
            "COLLECTOR AND ABOUT A MAN'S HEIGHT ABOVE HIM, close under the "
            "great blank rear wall, looking out across the enormous open "
            "limestone pavement toward the far sanctuary. " + _GRAIN +
            "THE CAMERA SHOOTS PAST HIM: he is seen ENTIRELY FROM BEHIND, full "
            "length from head to sandals, alone, right of centre, standing "
            "still, and HIS FACE IS NOT VISIBLE AT ALL. A thickset man of about "
            "thirty-eight, BAREHEADED, with SHORT COARSE BLACK HAIR cut roughly "
            "at the top of the neck and a clear band of that black hair showing "
            "at the nape, in a DEEP RUST-BROWN tunic under a DARK OLIVE-GREEN "
            "mantle pulled round his shoulders. HIS HEAD IS BOWED FORWARD so "
            "the crown of it is toward the camera, his shoulders are rounded "
            "and pulled in, and he stands so close to the great wall of very "
            "large square-cut limestone blocks that it fills the entire left "
            "side of the frame beside him. The whole enormous sunlit pavement "
            "runs away in front of him, EMPTY for a great distance, to the "
            "small far figure of another worshipper and the tall plain "
            "rectangular sanctuary against a high dry pale blue sky. Hard "
            "bright late-morning sun from the upper LEFT; the sun is well out "
            "of frame and there is no light source behind or above his head. "
            "THE DISTANCE HE HAS PUT BETWEEN HIMSELF AND EVERYONE ELSE IS THE "
            "COMPOSITION."
        ),
    },
    {
        "id": "v2-r039-b27", "out": "s27-smote-upon-his-breast.jpeg",
        "seg": "jv13a", "window": "106.036-110.892", "wide": False, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "heaven, but smote upon his breast, saying,",
        "must_show": "The tax collector's closed fist coming against his own chest, seen from the side, his lowered face at the top of the frame with the eyes cast down.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_MOCK + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the direction he "
            "faces, so we see the clean edge of his profile against the bright "
            "soft pavement beyond and THE FAR CHEEK AND FAR EYE ARE HIDDEN "
            "BEHIND THE BRIDGE OF HIS NOSE AND NOT VISIBLE AT ALL. His single "
            "visible eye is aimed steeply DOWN at the stone in front of his own "
            "feet and out through the BOTTOM EDGE. The pose itself makes a look "
            "into the lens physically impossible. "
            "One photograph, 85mm lens at f/2.8, framed from the top of the "
            "head down to the waist. " + _GRAIN +
            "HIS RIGHT HAND IS CLOSED INTO A LOOSE FIST and has just come in "
            "against the centre of his own chest — the knuckles pressed to the "
            "DEEP RUST-BROWN wool over the breastbone, the forearm bent up "
            "across the body, the wrist bent, the shoulder rolled forward — the "
            "old gesture of grief, made once, hard and unhurried, NOT a "
            "theatrical beating and NOT a flailing. His head is bowed, his "
            "chin near his collarbone, his mouth closed and set. He is a "
            "thickset BAREHEADED Judean man of about thirty-eight with warm "
            "sun-darkened olive-brown skin, a broad face, heavy cheeks, a SHORT "
            "CROPPED BLACK BEARD and SHORT COARSE BLACK HAIR cut at the top of "
            "the neck. Hard sunlight BOUNCING UP off the pale pavement in front "
            "of him lights the underside of his brow and jaw from LOW AND IN "
            "FRONT, while the top and back of his head stay in shadow and read "
            "darker than the stone behind them; there is no light source "
            "anywhere behind or above his head. Nothing else is in the frame."
        ),
    },
    {
        "id": "v2-r039-b28", "out": "s28-did-not-go-up-front.jpeg",
        "seg": "n7", "window": "110.892-115.362", "wide": True, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "The tax collector did not go up front. He stopped at the very back as",
        "must_show": "A wide side-on view along the base of the great rear wall showing how far back he has stopped — his small dark figure hard against the stone with the sunlit court opening away to one side.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 28mm lens at f/5.6, THE CAMERA STANDING WELL OFF "
            "TO ONE SIDE AND SHOOTING ALONG THE FACE OF THE GREAT REAR WALL, at "
            "a right angle to the direction the man faces, so he is seen in "
            "strict SIDE-ON PROFILE and NOT ONE PAIR OF PUPILS IS ANYWHERE NEAR "
            "THE LENS AXIS. " + _GRAIN +
            "The enormous wall of very large square-cut pale limestone blocks "
            "laid in level courses without mortar runs the full width of the "
            "picture in hard perspective, its shadow lying along the foot of it "
            "in a long dark band. THE TAX COLLECTOR stands in that shadow, "
            "small, right of centre, full length from head to sandals, in "
            "strict profile facing LEFT into the picture with his head bowed "
            "and his hands loose at his sides — thickset, BAREHEADED, SHORT "
            "COARSE BLACK HAIR cut at the neck, SHORT CROPPED BLACK BEARD, DEEP "
            "RUST-BROWN tunic, DARK OLIVE-GREEN mantle. To the LEFT of him the "
            "vast sunlit pavement opens away and runs on for an enormous "
            "distance to the far figures and the tall plain rectangular "
            "sanctuary, and THE WHOLE OF THAT DISTANCE IS EMPTY BETWEEN HIM AND "
            "THEM. Hard high sun from the upper LEFT. THIS IS A WIDE "
            "FULL-LENGTH SCENE AND NOT A PORTRAIT: the camera is far enough "
            "back that the man, the whole run of the wall and the open court "
            "beyond are in frame together. At most three other worshippers are "
            "visible far off, tiny and dark, and NO PALE OR OFF-WHITE CLOTH "
            "APPEARS ON ANY OF THEM."
        ),
    },
    {
        "id": "v2-r039-b29", "out": "s29-still-be-in-the-temple.jpeg",
        "seg": "n7", "window": "115.362-119.362", "wide": False, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "far as a man could get and still be in the temple. He could not bring himself",
        "must_show": "A low macro of the tax collector's worn sandals and dusty feet standing on the last flagstone at the very foot of the great wall, the mortarless stone courses rising behind his heels.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _GAZE + "NO BUCKLE, roller buckle, frame, pin, prong, tongue, eyelet, grommet, rivet, stud, snap, clasp, hook, ring or metal fitting anywhere on any strap; no moulded or rubber sole, heel, welt, stitched rand, tread pattern, lace, boot or enclosing upper; and no maker's stamp, lettering or logo; ",
        "scene": (
            "One photograph, 50mm lens at f/4, THE CAMERA SET DOWN ON THE "
            "PAVEMENT ITSELF AND LOOKING ACROSS AND SLIGHTLY UP at two feet "
            "from the SIDE; no face, no head and no other person is anywhere in "
            "the picture. " + _GRAIN +
            "TWO ADULT MAN'S FEET, broad and thick through the instep, the skin "
            "warm sun-darkened olive-brown, the ankles and the tops of the feet "
            "grey with road dust, stand still and square on the last worn "
            "limestone flagstone. EACH SANDAL IS BUILT THE FIRST-CENTURY WAY "
            "AND IS STATED POSITIVELY: a FLAT sole of layered rawhide cut to "
            "the shape of the foot, no heel and no shaping, its edge irregular "
            "and worn thin at the ball; plain undyed leather THONGS passing up "
            "through slits cut straight through that sole, crossing the instep "
            "and passing round the ankle, and FASTENED BY BEING KNOTTED AND "
            "TUCKED BACK THROUGH THEMSELVES with the loose end left hanging "
            "against the side of the foot. The hem of a DEEP RUST-BROWN "
            "hand-woven wool tunic hangs to mid-calf above them, its coarse "
            "over-and-under weave and frayed selvedge edge clearly readable. "
            "Directly behind his heels the great wall rises: enormous "
            "square-cut pale limestone blocks laid in level courses with fine "
            "dry joints and no mortar, filling the whole background. He is "
            "standing as close to it as a man can stand. Hard high sun from the "
            "upper LEFT lays a short hard shadow of both feet across the flag."
        ),
    },
    {
        "id": "v2-r039-b30", "out": "s30-could-not-lift-his-eyes.jpeg",
        "seg": "n7", "window": "119.362-123.642", "wide": False, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "himself to lift his eyes. He struck his own chest the way people do when",
        "must_show": "A close strict profile of the tax collector's face with the eyes held down and the lids lowered — a man physically unable to raise his look, with only ordinary daylight above him.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_MOCK + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the direction he "
            "faces, so we see the clean edge of his profile — the near cheek, "
            "the lowered eyelash line, the short blunt nose in silhouette — and "
            "THE FAR CHEEK AND FAR EYE ARE HIDDEN BEHIND THE BRIDGE OF HIS NOSE "
            "AND NOT VISIBLE AT ALL. His single visible eye is HALF-LIDDED AND "
            "AIMED STEEPLY DOWN, out through the BOTTOM EDGE of the frame. The "
            "pose itself makes a look into the lens physically impossible. "
            "One photograph, 85mm lens at f/2.8, head and shoulders only, the "
            "great mortarless limestone wall a pace behind him thrown "
            "completely soft. " + _GRAIN +
            "He is a thickset Judean man of about thirty-eight with warm "
            "sun-darkened olive-brown Middle Eastern skin, a broad face, heavy "
            "cheeks, a short blunt nose, a SHORT CROPPED BLACK BEARD and SHORT "
            "COARSE BLACK HAIR cut roughly at the top of the neck and pushed "
            "back off the forehead, HIS HEAD BARE, in a DEEP RUST-BROWN tunic "
            "and DARK OLIVE-GREEN mantle. There is sweat at his temple and a "
            "dust line at his collar. His mouth is closed, the lower lip caught "
            "very slightly, the muscle at the hinge of the jaw standing out. "
            "The expression is PLAIN, QUIET, EXHAUSTED SHAME — no tears running, "
            "no grimace, no sob, nothing performed. Sunlight BOUNCING UP off "
            "the pale pavement lights the underside of his brow and jaw from "
            "LOW AND IN FRONT while the top and back of his head stay dark; "
            "there is no light source anywhere behind or above his head. Above "
            "the wall behind him there is only ordinary high dry pale blue "
            "daylight sky and nothing whatever in it."
        ),
    },
]

BEATS += [
    {
        "id": "v2-r039-b31", "out": "s31-a-prayer-of-seven-words.jpeg",
        "seg": "n7", "window": "123.642-128.122", "wide": False, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "someone has died. And he prayed a prayer of only seven words.",
        "must_show": "A macro of the closed fist held against the rust-brown wool of his own chest, the knuckles and the weave both sharp, no face in frame.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _GAZE + "no corpse, bier, shroud, coffin, grave, tomb or funeral anywhere; ",
        "scene": (
            "One photograph, 100mm macro lens at f/2.8, THE CAMERA LOOKING "
            "ACROSS FROM THE SIDE at a closed hand pressed to a chest, filling "
            "the frame with the fist, the forearm and the cloth; no face and no "
            "head is anywhere in the picture. " + _GRAIN +
            "THE HAND IS A MAN'S: broad, thick-fingered, warm sun-darkened "
            "olive-brown, soft-palmed, ink-stained along the first two fingers, "
            "the nails short, the knuckles pushed white where they press. It is "
            "closed into a loose fist and held STILL against the centre of the "
            "chest, not swinging. Under it the DEEP RUST-BROWN hand-woven wool "
            "of the tunic is pushed into a shallow crease, its coarse "
            "over-and-under grid of warp and weft threads slightly irregular "
            "and completely readable, flat and matte, with the DARK "
            "OLIVE-GREEN mantle falling away beside it and a plain twisted "
            "undyed brown flax cord crossing the bottom corner of the frame. "
            "Hard sunlight bouncing up off the pale pavement rakes across the "
            "knuckles from LOW AND IN FRONT. Behind the shoulder the great "
            "mortarless limestone wall is thrown completely soft. Nothing else "
            "is in the frame."
        ),
    },
    # j2 — Luke 18:13, THE PUBLICAN'S OWN PRAYER. His face, never Jesus's.
    {
        "id": "v2-r039-b32", "out": "s32-god-be-merciful-to-me.jpeg",
        "seg": "j2", "window": "128.122-131.869", "wide": False, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "God be merciful to me a sinner.",
        "must_show": "The tax collector saying the seven words: a strict profile of his face, lips parted mid-word, eyes still down, absolutely still — this red line is HIS, and Jesus is nowhere in this picture.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_MOCK + _GAZE + "no second man, no figure in cream or off-white, and nobody resembling Jesus anywhere in the frame; ",
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the direction he "
            "faces, so we see the clean edge of his profile against the great "
            "soft wall — the near cheek, the lowered eyelash line, the short "
            "blunt nose in silhouette — and THE FAR CHEEK AND FAR EYE ARE "
            "HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND NOT VISIBLE AT ALL. His "
            "single visible eye stays HALF-LIDDED AND AIMED DOWN, out through "
            "the BOTTOM EDGE. The pose itself makes a look into the lens "
            "physically impossible. "
            "One photograph, 85mm lens at f/2.8, head and shoulders only, the "
            "great mortarless limestone wall a pace behind him thrown "
            "completely soft; there is NO SECOND PERSON anywhere in this "
            "picture. " + _GRAIN +
            "He is a thickset Judean man of about thirty-eight with warm "
            "sun-darkened olive-brown Middle Eastern skin, a broad face and "
            "heavy cheeks, a SHORT CROPPED BLACK BEARD, SHORT COARSE BLACK HAIR "
            "cut at the top of the neck, HIS HEAD BARE, in a DEEP RUST-BROWN "
            "tunic and DARK OLIVE-GREEN mantle. HIS LIPS ARE PARTED MID-WORD "
            "and the breath is barely in it — the mouth hardly open, the jaw "
            "slack, the throat still. Everything else about him has stopped "
            "moving. His face carries plain quiet exhausted honesty and nothing "
            "performed: no tears running down it, no grimace, no sob, no "
            "clutching hand. Sunlight bouncing up off the pale pavement lights "
            "the underside of his brow and jaw from LOW AND IN FRONT while the "
            "top and back of his head stay dark; there is no light source "
            "anywhere behind or above his head, and nothing outlines his hair."
        ),
    },
    # ===== n8a — the hour of sacrifice (white) ===============================
    {
        "id": "v2-r039-b33", "out": "s33-more-in-that-prayer.jpeg",
        "seg": "n8a", "window": "131.869-135.559", "wide": False, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "There is more in that prayer than it sounds like. He is standing in",
        "must_show": "A slightly wider hold on the same man in the same place, from the same side, his head still bowed, the enormous scale of the wall beginning to show above him.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 50mm lens at f/2.8, THE CAMERA IN THE SAME PLACE "
            "AS THE PREVIOUS FRAME BUT PULLED BACK, still at a RIGHT ANGLE to "
            "the direction he faces so he stays in strict SIDE-ON PROFILE with "
            "the far cheek and far eye hidden behind the bridge of his nose and "
            "his single visible eye aimed DOWN and out through the BOTTOM EDGE. "
            + _GRAIN +
            "He is framed now from mid-thigh up, standing still in the long "
            "shadow at the foot of the wall — a thickset BAREHEADED man of "
            "about thirty-eight, SHORT COARSE BLACK HAIR cut at the neck, SHORT "
            "CROPPED BLACK BEARD, warm sun-darkened olive-brown skin, DEEP "
            "RUST-BROWN tunic, DARK OLIVE-GREEN mantle, both hands loose at his "
            "sides, head bowed. Behind and above him the enormous square-cut "
            "limestone blocks of the wall rise out of the top of the frame with "
            "their level mortarless courses running away in perspective, and "
            "the scale of them against him is the point. At the far RIGHT edge "
            "a narrow strip of the sunlit open pavement shows, empty. Hard high "
            "sun from the upper LEFT falls on the wall face beyond him; he "
            "stands in shadow lit only by the bright stone bouncing light back "
            "at him from LOW AND IN FRONT, and there is no light source behind "
            "or above his head."
        ),
    },
    {
        "id": "v2-r039-b34", "out": "s34-at-the-hour-of-sacrifice.jpeg",
        "seg": "n8a", "window": "135.559-139.379", "wide": True, "jesus": False,
        "locks": _TEMPLE,
        "narration": "in the temple at the hour of sacrifice, while a lamb is being killed",
        "must_show": "The great square altar of uncut field stone standing in the open court with pale smoke going straight up from it, two barefoot priests in plain undyed linen on the higher pavement, and one live lamb led on a plain cord toward the ramp.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _GAZE,
        "scene": (
            "One photograph, 35mm lens at f/5.6, hard high midday sun from the "
            "upper LEFT, a high dry pale blue sky. " + _GRAIN +
            "THE CAMERA STANDS BEHIND AND BELOW THE WORSHIPPERS ON THE LOWER "
            "PAVEMENT AND SHOOTS PAST THEM AND UP toward the altar: two "
            "dark-clad standing men occupy the lower corners as heads and "
            "shoulders seen ENTIRELY FROM BEHIND, softly out of focus, and NOT "
            "ONE FACE IS TURNED TOWARD THE LENS. Beyond them, sharp and filling "
            "the centre of the frame, THE ALTAR: one enormous SQUARE MASS OF "
            "UNCUT UNDRESSED FIELD STONES packed with mortar, wider than a room "
            "and about the height of two men, with one long unbroken RAMP of "
            "the same rough stone rising to its top on the near side. ONE "
            "COLUMN OF PALE GREY-WHITE SMOKE goes STRAIGHT UP from its top into "
            "the sky, thick at the base and feathering as it rises. TWO PRIESTS "
            "stand on the higher pavement beside the ramp, seen in side-on "
            "profile and from behind, BAREFOOT, in PLAIN UNDYED WHITE LINEN — a "
            "plain straight ankle-length tunic, a plain woven sash, a plain "
            "wound linen head wrapping — and nothing else on them. At the foot "
            "of the ramp a man leads ONE SINGLE LIVE LAMB on a plain twisted "
            "flax cord: the animal is standing calmly on all four feet with its "
            "head up, unhurt and unbound, and NOTHING IS BEING DONE TO IT. "
            "There is no blood, no knife, no carcass and no killing anywhere in "
            "the picture. THIS IS A WIDE FULL-LENGTH SCENE AND NOT A PORTRAIT: "
            "the whole altar, the ramp, the priests, the lamb and the pavement "
            "are in frame together. Everyone except the two linen-clad priests "
            "is a solid dark saturated mass of indigo, umber, charcoal or rust "
            "from head to foot."
        ),
    },
]

BEATS += [
    {
        "id": "v2-r039-b35", "out": "s35-for-the-whole-nation.jpeg",
        "seg": "n8a", "window": "139.379-143.339", "wide": True, "jesus": False,
        "locks": _TEMPLE,
        "narration": "for the sins of the whole nation. And he is asking God to let",
        "must_show": "A wide low view of the standing crowd of worshippers on the pavement seen from behind, all of them facing the far altar, with the single column of smoke going straight up beyond them into an empty sky.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _GAZE,
        "scene": (
            "One photograph, 28mm lens at f/5.6, hard high midday sun from the "
            "upper LEFT. " + _GRAIN +
            "THE CAMERA STANDS LOW AND BEHIND THE WHOLE CROWD AND SHOOTS PAST "
            "THEM ACROSS THE COURT: every person in the picture is seen "
            "ENTIRELY FROM BEHIND as heads, shoulders and BACKS, standing still "
            "on the huge pale limestone flags and facing away from the lens "
            "toward the far altar, and NOT ONE FACE IS VISIBLE ANYWHERE. Some "
            "have their hands raised open at shoulder height, some have their "
            "heads bowed. They stand loosely spaced with clear bare pavement "
            "between them — nobody sits, nobody kneels, and there is nothing "
            "anywhere to sit on. Beyond them the enormous square mass of the "
            "altar of uncut field stone stands small in the distance with ONE "
            "COLUMN OF PALE GREY-WHITE SMOKE going STRAIGHT UP from it, and "
            "beyond that the tall plain rectangular block of the sanctuary. "
            "ABOVE IT ALL THERE IS NOTHING BUT ORDINARY HIGH DRY PALE BLUE "
            "DAYLIGHT SKY — no cloud floor, no shaft or beam of light, no "
            "figure, no face, no form and no presence of any kind in it. Every "
            "person in the crowd is a solid dark saturated mass of indigo, "
            "umber, charcoal, deep rust, dark olive or deep maroon from head to "
            "foot, in focus and blurred alike, and NO PALE OR OFF-WHITE CLOTH "
            "APPEARS ON ANY OF THEM."
        ),
    },
    {
        "id": "v2-r039-b36", "out": "s36-fall-on-him-personally.jpeg",
        "seg": "n8a", "window": "143.339-147.265", "wide": False, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "let that mercy fall on him, him personally.",
        "must_show": "A tight profile of the tax collector's lowered face with the far-off column of altar smoke soft and small behind him, his expression unchanged and entirely private.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the direction he "
            "faces, so the far cheek and far eye are hidden behind the bridge "
            "of his nose and his single visible eye stays half-lidded and aimed "
            "DOWN, out through the BOTTOM EDGE. " + _GRAIN +
            "One photograph, 135mm lens at f/2.8 so the background compresses "
            "and goes completely soft, head and shoulders only. He is a "
            "thickset Judean man of about thirty-eight with warm sun-darkened "
            "olive-brown Middle Eastern skin, a broad face, heavy cheeks, a "
            "SHORT CROPPED BLACK BEARD and SHORT COARSE BLACK HAIR cut at the "
            "top of the neck, HIS HEAD BARE, in a DEEP RUST-BROWN tunic and "
            "DARK OLIVE-GREEN mantle. His face has not changed and is not "
            "performing anything: mouth closed, jaw set, eyes down. FAR BEHIND "
            "HIM AND THROWN COMPLETELY SOFT, small in the top corner of the "
            "frame, the pale grey-white column of altar smoke rises straight up "
            "against an empty pale blue sky — unfocused, unreachable, and "
            "clearly a long way off. There is nothing else in that sky at all. "
            "Sunlight bouncing up off the pale pavement lights the underside of "
            "his brow and jaw from LOW AND IN FRONT while the top and back of "
            "his head stay dark; there is no light source anywhere behind or "
            "above his head."
        ),
    },
    # ===== n8b — as if he were the only one in the building (white) ==========
    {
        "id": "v2-r039-b37", "out": "s37-not-one-among-many.jpeg",
        "seg": "n8b", "window": "147.265-151.015", "wide": True, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "And in Luke's Greek, he does not count himself as one guilty man",
        "must_show": "The tax collector very small against a vast unbroken field of mortarless limestone blocks that fills almost the whole frame, so the scale states the loneliness.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _GAZE,
        "scene": (
            "One photograph, 50mm lens at f/8, THE CAMERA STANDING WELL BACK "
            "AND TO THE SIDE, at a right angle to the wall, shooting flat "
            "across it. " + _GRAIN +
            "NINE TENTHS OF THIS PICTURE IS STONE: an enormous unbroken field "
            "of very large square-cut pale limestone blocks laid in level "
            "courses with fine dry mortarless joints, running edge to edge and "
            "top to bottom, its surface tooled, weathered and dust-streaked. "
            "THE MAN IS TINY AND ALONE at the bottom of it, right of centre, "
            "full length from head to sandals but no taller in the frame than a "
            "finger — a thickset BAREHEADED figure with SHORT COARSE BLACK HAIR "
            "cut at the neck, in a DEEP RUST-BROWN tunic and DARK OLIVE-GREEN "
            "mantle, standing in strict side-on profile facing LEFT with his "
            "head bowed and his arms at his sides, so no face is presented to "
            "the lens at all. THERE IS NOBODY ELSE ANYWHERE IN THE FRAME — no "
            "figure, no shoulder, no blurred stranger at any edge. The long "
            "hard shadow of the wall lies across the pavement at his feet and "
            "hard high sun from the upper LEFT rakes the stone above him. THIS "
            "IS A WIDE FULL-LENGTH SCENE AND NOT A PORTRAIT."
        ),
    },
    {
        "id": "v2-r039-b38", "out": "s38-the-only-one-in-the-building.jpeg",
        "seg": "n8b", "window": "151.015-155.249", "wide": True, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "man among many. He speaks as if he were the only one in the building.",
        "must_show": "A very high wide view straight down and across the enormous empty pavement with the tax collector as one small dark mark on it and no other person anywhere.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _GAZE + "no other person, figure, shoulder or blurred stranger anywhere in the frame; ",
        "scene": (
            "One photograph, 24mm lens at f/8, THE CAMERA VERY HIGH ABOVE AND "
            "BEHIND HIM looking steeply DOWN and across the enormous open "
            "limestone pavement of the temple court. " + _GRAIN +
            "THE FRAME IS ALMOST ENTIRELY EMPTY GROUND: huge rectangular slabs "
            "of pale dressed limestone, worn smooth and hollowed by feet, their "
            "joints running away in hard perspective, dust drifted along the "
            "seams, a long band of wall shadow crossing one corner. THE MAN IS "
            "ONE SMALL DARK MARK ON IT, low and right of centre, seen from "
            "ABOVE AND ENTIRELY FROM BEHIND so that only the crown of his SHORT "
            "COARSE BLACK HAIR, his rounded shoulders in the DARK OLIVE-GREEN "
            "mantle and the DEEP RUST-BROWN hem of his tunic are readable, and "
            "HIS FACE IS NOT VISIBLE AT ALL. His own short shadow lies beside "
            "him. THERE IS NOT ONE OTHER PERSON ANYWHERE IN THE PICTURE, in "
            "focus or out of focus, near or far, at any edge. Hard high midday "
            "sun from the upper LEFT. THIS IS A WIDE FULL-LENGTH SCENE AND NOT "
            "A PORTRAIT: the camera is far enough back that the man is small "
            "and the emptiness around him is the subject."
        ),
    },
]

# ===== n9 + j3 — back to Jesus on the steps. j3 IS his own line. ============
BEATS += [
    {
        "id": "v2-r039-b39", "out": "s39-two-men-same-temple.jpeg",
        "seg": "n9", "window": "155.249-159.399", "wide": True, "jesus": False,
        "locks": _T_BOTH, "char_refs": _BOTH,
        "narration": "Two men. The same temple. The same God. One of them doing",
        "must_show": "One last wide frame holding both men in the same court at once, the Pharisee's raised arms near and the tax collector's bowed head far, the empty pavement between them.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 35mm lens at f/5.6, THE CAMERA STANDING TO ONE "
            "SIDE OF BOTH MEN AND SHOOTING ACROSS THE COURT AT A RIGHT ANGLE TO "
            "THE LINE BETWEEN THEM, so both are in strict side-on profile and "
            "NEITHER PAIR OF PUPILS CAN COME ANYWHERE NEAR THE LENS AXIS. "
            + _GRAIN +
            "ON THE LEFT, mid-ground and larger, THE PHARISEE stands out on the "
            "open pavement in profile facing RIGHT, full length, both arms "
            "raised open at shoulder height, chin lifted — a tall spare upright "
            "man of about fifty in a DEEP INDIGO BLUE tunic under a DARK "
            "BLUE-BLACK tasselled mantle, THICK IRON-GREY HAIR combed back and "
            "cut level at the middle of the neck, a FULL SQUARED IRON-GREY "
            "BEARD. ON THE RIGHT, far back against the base of the great "
            "mortarless limestone wall and much smaller, THE TAX COLLECTOR "
            "stands in profile facing LEFT, full length, head bowed, arms at "
            "his sides — thickset, BAREHEADED, SHORT COARSE BLACK HAIR cut at "
            "the neck, SHORT CROPPED BLACK BEARD, DEEP RUST-BROWN tunic, DARK "
            "OLIVE-GREEN mantle. BETWEEN THEM RUNS AN ENORMOUS UNBROKEN "
            "RECTANGLE OF EMPTY SUNLIT PAVEMENT with nobody standing in it. "
            "Hard high sun from the upper LEFT, one straight column of pale "
            "grey-white smoke rising far off beyond the Pharisee, a high dry "
            "pale blue sky with nothing in it. At most three other worshippers "
            "are visible right at the far edges, tiny and dark, and NO PALE OR "
            "OFF-WHITE CLOTH APPEARS ON ANYBODY."
        ),
    },
    {
        "id": "v2-r039-b40", "out": "s40-barely-able-to-speak.jpeg",
        "seg": "n9", "window": "159.399-163.619", "wide": False, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "them doing all the talking, the other barely able to speak, and then Jesus said",
        "must_show": "A very tight macro of the tax collector's closed mouth and the small movement in his throat, no eyes in frame, the words barely getting out.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_MOCK + _GAZE + "no eyes visible in the frame at all; ",
        "scene": (
            "One photograph, 100mm macro lens at f/2.8, THE CAMERA AT A RIGHT "
            "ANGLE TO HIM SHOOTING STRAIGHT ACROSS. The frame is cropped to the "
            "lower half of his face only — the mouth, the short black "
            "moustache, the cropped black beard, the line of the jaw and the "
            "front of the throat — and HIS EYES ARE ABOVE THE TOP EDGE OF THE "
            "FRAME AND NOT VISIBLE AT ALL, so no gaze of any kind can meet the "
            "lens. " + _GRAIN +
            "The lips are barely apart, the lower lip dry and slightly cracked, "
            "the mouth hardly moving; the tendon at the side of the throat has "
            "just tightened on a swallow. The skin is warm sun-darkened "
            "olive-brown, clearly Middle Eastern, with sweat along the jaw and "
            "a fine grey line of road dust at the collar. The beard is SHORT, "
            "BLACK AND THICK, cropped close and unshaped, each hair separately "
            "readable. Below it the neck of a DEEP RUST-BROWN hand-woven wool "
            "tunic shows its coarse over-and-under weave at a plain slit "
            "opening, with the DARK OLIVE-GREEN mantle at the shoulder. Light "
            "bounced up from the pale pavement comes from LOW AND IN FRONT and "
            "rakes the mouth and jaw; there is no light source behind or above "
            "his head. The wall behind is thrown completely soft. Nothing else "
            "is in the frame."
        ),
    },
    {
        "id": "v2-r039-b41", "out": "s41-and-then-jesus-said.jpeg",
        "seg": "n9", "window": "163.619-167.982", "wide": True, "jesus": True, "ref": REF,
        "locks": _STEPS,
        "narration": "said the sentence that would have stopped every man listening to him cold.",
        "must_show": "Back on the city steps: Jesus about to speak, the four prosperous men still standing below him, the whole group seen past the listeners' backs.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            "One photograph, 35mm lens, the same broad flight of worn limestone "
            "city steps below the same high blank block wall, the sun now "
            "further round so the hard shadows of the step edges fall the other "
            "way. " + _GRAIN +
            "THE CAMERA STANDS BEHIND AND BELOW THE FOUR STANDING LISTENERS AND "
            "SHOOTS PAST THEM AND UP: they fill the lower half of the frame as "
            "heads, shoulders and BACKS seen entirely FROM BEHIND, and NOT ONE "
            "FACE IS TURNED TOWARD THE LENS. Jesus stands three shallow courses "
            "above them, centre frame, full length from head to sandals, "
            "completely still, weight settled, both hands low and open at his "
            "sides, in three-quarter view with his head turned a quarter-turn "
            "AWAY from the lens toward the man at the far LEFT; the camera sees "
            "the SIDE of his face, the far cheek foreshortened and the far eye "
            "narrowed behind the bridge of his nose, and his eyeline runs "
            "laterally across the frame and exits through the LEFT EDGE. HIS "
            "PUPILS NEVER COME ROUND ONTO THE LENS AXIS. The sun is out of "
            "frame to the RIGHT and IN FRONT of him and the blank limestone "
            "wall behind him is in shadow and reads DARKER than he does; there "
            "is no light source anywhere behind or above his head. THIS IS A "
            "WIDE FULL-LENGTH GROUP PHOTOGRAPH AND NOT A PORTRAIT. THE ONLY "
            "PALE WOOL IN THE PICTURE IS HIS OWN ROBE; every other person is a "
            "solid dark saturated mass of indigo, maroon, rust, olive or "
            "charcoal from edge to edge."
        ),
    },
    {
        "id": "v2-r039-b42", "out": "s42-went-down-justified.jpeg",
        "seg": "j3", "window": "167.982-171.872", "wide": False, "jesus": True, "ref": REF,
        "locks": ["STREET-STEPS", "JUDEAN-LAND"],
        "narration": "I tell you, this man went down to his house justified rather than",
        "must_show": "A tight strict side-on profile of Jesus delivering the verdict of Luke 18:14 — this red line is HIS OWN, spoken as himself, and it is the one that belongs on his face.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the line between "
            "Jesus and the men he is speaking to, so we see the clean edge of "
            "his profile against the shadowed limestone wall — the near cheek, "
            "the eyelash line, the bridge of the nose in silhouette — and THE "
            "FAR CHEEK AND FAR EYE ARE HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND "
            "NOT VISIBLE AT ALL. His single visible eye is wide, steady and "
            "aimed straight ACROSS the frame and out through the LEFT EDGE. The "
            "pose itself makes a look into the lens physically impossible. "
            "One photograph, 85mm lens at f/2.8, head and shoulders only, the "
            "great blank limestone block wall four paces behind him thrown "
            "completely soft and reading DARKER than he does. Strong afternoon "
            "sun comes from the LEFT and IN FRONT and lands on the front planes "
            "of his face — the brow, the nose, the cheekbone, the beard — while "
            "the back and top of his head stay in his own shadow; the sun is "
            "well out of frame and there is no light source anywhere behind or "
            "above his head, and nothing outlines his hair. " + _GRAIN +
            "His lips are parted mid-sentence, his chin level, the jaw firm. "
            "The expression is QUIET AND ABSOLUTELY CERTAIN — not raised, not "
            "angry, not triumphant — the face of a man stating a fact he "
            "expects to be argued with. Nothing else is in the frame: no other "
            "person, no hand, no object, no shoulder at any edge."
        ),
    },
]

BEATS += [
    {
        "id": "v2-r039-b43", "out": "s43-exalteth-himself-abased.jpeg",
        "seg": "j3", "window": "171.872-176.652", "wide": False, "jesus": True, "ref": REF,
        "locks": ["STREET-STEPS", "JUDEAN-LAND"],
        "narration": "the other: for every one that exalteth himself shall be abased,",
        "must_show": "Jesus in three-quarter from behind on the steps, one hand low and open turning slowly outward as he says the second half of the verdict.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            "One photograph, 85mm lens at f/2.8. THE CAMERA STANDS BEHIND "
            "JESUS'S RIGHT SHOULDER AND SLIGHTLY ABOVE, SHOOTING PAST HIM DOWN "
            "THE STEPS: we see the back and side of his head, the ear, the line "
            "of the jaw and only the far edge of the cheekbone — his face is "
            "turned away from the lens toward the men below, so NO GAZE CAN "
            "REACH THE CAMERA. " + _GRAIN +
            "His long thick tousled dark brown wavy hair falls to below the "
            "shoulders in the near part of the frame, the plain undyed "
            "off-white cream wool of his robe across the shoulder showing its "
            "coarse hand-woven over-and-under weave in the raking light. HIS "
            "RIGHT HAND IS RAISED INTO THE FRAME at chest height, low and OPEN, "
            "the palm turning slowly outward and downward, the fingers relaxed "
            "and separated — an offering gesture, not a pointing finger and not "
            "a fist. Below and beyond him, thrown soft, the dark shapes of the "
            "four listeners standing on the lower courses of the worn "
            "limestone steps, all seen from behind or in three-quarter from "
            "behind. Strong afternoon sun from the LEFT and IN FRONT of him "
            "falls on the step stone beyond; the back of his head is in his own "
            "shadow and reads DARKER than the sunlit stone behind it, with no "
            "bright ring, rim, edge or outline anywhere around his hair. THE "
            "ONLY PALE WOOL IN THE PICTURE IS HIS OWN ROBE."
        ),
    },
    {
        "id": "v2-r039-b44", "out": "s44-shall-be-exalted.jpeg",
        "seg": "j3", "window": "176.652-181.106", "wide": True, "jesus": True, "ref": REF,
        "locks": _STEPS,
        "narration": "and he that humbleth himself shall be exalted.",
        "must_show": "The four prosperous listeners' faces as the sentence lands — the certainty gone out of them, one man's mouth open, another looking away at the ground — seen past Jesus's shoulder.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MOCK + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            "THE CAMERA STANDS BEHIND AND ABOVE JESUS AND SHOOTS PAST HIM DOWN "
            "THE STEPS: the back of his head, his shoulder and the top of his "
            "cream wool robe fill the lower LEFT corner of the picture, softly "
            "out of focus, seen ENTIRELY FROM BEHIND — his face is not visible "
            "at all. " + _GRAIN +
            "One photograph, 50mm lens at f/2.8, strong late-afternoon sun from "
            "the LEFT laying long hard shadows down the worn step edges. "
            "Beyond him, sharp, the four prosperous men stand on the lower "
            "courses in a loose uneven group, full length, and THE SENTENCE HAS "
            "LANDED ON THEM: the nearest has gone completely still with his "
            "arms unfolded and hanging; the second has his mouth slightly open "
            "and his brows drawn together; the third has turned his head away "
            "to his own right and dropped his eyes to the stone at his feet, "
            "his eyeline exiting through the RIGHT EDGE; the fourth, furthest "
            "back and half turned away, has put one hand up to his own beard. "
            "NOT ONE PAIR OF PUPILS IS CENTRED ON THE LENS and nobody is "
            "presenting himself to the viewer. None of them is drawn as a "
            "sneering or gloating villain; what is on these faces is the "
            "ordinary shock of decent men who did not expect to be the ones in "
            "the story. THIS IS A WIDE FULL-LENGTH GROUP PHOTOGRAPH AND NOT A "
            "PORTRAIT. THE ONLY PALE WOOL IN THE PICTURE IS THE OUT-OF-FOCUS "
            "SHOULDER OF JESUS'S OWN ROBE in the near corner; every other "
            "person is a solid dark saturated mass of indigo, maroon, rust, "
            "olive or charcoal from edge to edge."
        ),
    },
    # ===== n10 — the two men walk home (white) ==============================
    {
        "id": "v2-r039-b45", "out": "s45-the-traitor-walked-home.jpeg",
        "seg": "n10", "window": "181.106-184.876", "wide": True, "jesus": False,
        "locks": _T_PUB, "char_refs": _PUB,
        "narration": "The traitor walked home right with God. The good man walked home",
        "must_show": "The tax collector going back down the temple's great outer stair, small, seen from behind and above, his shoulders no longer rounded.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _GAZE,
        "scene": (
            "One photograph, 35mm lens at f/5.6, THE CAMERA STANDING HIGH AT "
            "THE TOP OF THE GREAT STAIR, BEHIND HIM, LOOKING DOWN AND PAST HIM "
            "as he descends AWAY from the lens; he is seen ENTIRELY FROM "
            "BEHIND and HIS FACE IS NOT VISIBLE AT ALL. " + _GRAIN +
            "The enormous pale limestone stair drops away from the near ground "
            "in hard parallel bands of light and shadow across its worn step "
            "edges, out to the tan flat roofs of the city below and the dry "
            "hills beyond under a high pale blue sky. THE TAX COLLECTOR is "
            "small, left of centre, four or five courses down, full length from "
            "head to sandals — a thickset BAREHEADED figure with SHORT COARSE "
            "BLACK HAIR cut at the top of the neck and a clear band of that "
            "black hair showing at the nape, in a DEEP RUST-BROWN tunic and "
            "DARK OLIVE-GREEN mantle. HIS SHOULDERS ARE NO LONGER ROUNDED AND "
            "HIS HEAD IS NO LONGER BOWED: he is walking down evenly with his "
            "back straight and both arms swinging loose. Late-afternoon sun "
            "comes from the RIGHT and ahead of him; the sun is well out of "
            "frame and there is no light source behind or above his head. At "
            "most three other people are on the stair, far off, small, every "
            "one a solid dark mass of umber, charcoal or deep indigo from head "
            "to foot."
        ),
    },
    {
        "id": "v2-r039-b46", "out": "s46-exactly-as-he-came.jpeg",
        "seg": "n10", "window": "184.876-189.576", "wide": True, "jesus": False,
        "locks": _T_PHA, "char_refs": _PHA,
        "narration": "home exactly as he came. Not because God is impressed by failure,",
        "must_show": "The Pharisee coming down the same great stair, upright and unchanged, walking exactly as he walked up it, seen from behind and above.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 35mm lens at f/5.6, THE SAME CAMERA POSITION AS "
            "THE PREVIOUS FRAME — high at the top of the great stair, behind "
            "the walking man, looking down and past him as he descends AWAY "
            "from the lens; he is seen ENTIRELY FROM BEHIND and HIS FACE IS NOT "
            "VISIBLE AT ALL. " + _GRAIN +
            "The same enormous pale limestone stair drops away in the same hard "
            "parallel bands of light and shadow to the same tan flat roofs and "
            "dry hills under the same high pale blue sky. THE PHARISEE is "
            "right of centre, four or five courses down, full length from head "
            "to sandals — a tall spare upright man of about fifty in a DEEP "
            "INDIGO BLUE tunic under a DARK BLUE-BLACK tasselled mantle, THICK "
            "IRON-GREY HAIR combed back and cut level at the middle of the neck "
            "with a clear band of that iron-grey hair showing at the nape. HE "
            "IS WALKING EXACTLY AS HE WALKED UP: back straight, chin level, "
            "mantle gathered over the left forearm, the pace even and "
            "unhurried, nothing in his bearing altered by anything. "
            "Late-afternoon sun from the RIGHT and ahead of him, well out of "
            "frame, with no light source behind or above his head. At most "
            "three other people are on the stair, far off and small, every one "
            "a solid dark mass from head to foot."
        ),
    },
]

BEATS += [
    {
        "id": "v2-r039-b47", "out": "s47-came-holding-a-list.jpeg",
        "seg": "n10", "window": "189.576-193.316", "wide": False, "jesus": False,
        "locks": ["PHARISEE", "JUDEAN-LAND", "TEMPLE-COURT"], "char_refs": _PHA,
        "narration": "but because one of them came holding a list and the other came holding",
        "must_show": "A macro of the Pharisee's hand walking down the stair with the single small bundle of tithed herbs still held closed in his fingers.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _GAZE + "no bound book, ledger, spine, printed page, ruled line, column or modern paper anywhere; ",
        "scene": (
            "One photograph, 100mm macro lens at f/2.8, THE CAMERA LOOKING "
            "ACROSS AND DOWN AT ONE HAND FROM THE SIDE as it swings beside a "
            "walking body; no face and no head is anywhere in the picture. "
            + _GRAIN +
            "THE HAND IS A MAN'S: long, brown, clean, broad across the "
            "knuckles, the tendons standing on the back, the nails trimmed "
            "short, the skin warm olive-brown and lightly weathered. The "
            "fingers are CLOSED round ONE single small bundle of cut grey-green "
            "kitchen herb — mint and rue, stems together, leaves crushed a "
            "little where he grips it — held tight and low against the thigh. "
            "Beside the wrist the sleeve of a DEEP INDIGO BLUE hand-woven wool "
            "tunic shows its coarse over-and-under weave, and the corner of the "
            "DARK BLUE-BLACK mantle with its short plain undyed wool tassel "
            "swings past the bottom of the frame. Behind and below the hand, "
            "thrown completely soft, the worn pale limestone edges of the great "
            "stair and a hard band of late-afternoon shadow. Nothing else is in "
            "the frame."
        ),
    },
    {
        "id": "v2-r039-b48", "out": "s48-came-holding-nothing.jpeg",
        "seg": "n10", "window": "193.316-197.576", "wide": False, "jesus": False,
        "locks": ["PUBLICAN", "JUDEAN-LAND", "TEMPLE-COURT"], "char_refs": _PUB,
        "narration": "holding nothing. Only one of them was actually asking for anything.",
        "must_show": "A macro of the tax collector's two empty open hands hanging at his sides as he walks, nothing at all in either of them.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _GAZE + "no coin, purse, bag, box, sheet, scroll, bundle or object of any kind in either hand or anywhere in the frame; ",
        "scene": (
            "One photograph, 100mm macro lens at f/2.8, THE CAMERA LOOKING "
            "ACROSS AND DOWN AT TWO HANDS FROM THE SIDE as they swing beside a "
            "walking body; no face and no head is anywhere in the picture. "
            + _GRAIN +
            "BOTH HANDS ARE A MAN'S: broad, thick-fingered, warm sun-darkened "
            "olive-brown, soft-palmed, ink-stained along the first two fingers "
            "of the nearer one, the nails short. They hang LOOSE AND WIDE OPEN "
            "at his sides, the fingers uncurled and slightly apart, the palms "
            "turned a little forward — and BOTH ARE COMPLETELY EMPTY, bare skin "
            "from wrist to fingertip with nothing held, carried, gripped or "
            "resting in either of them and nothing at all in the frame beside "
            "them. The hem of a DEEP RUST-BROWN hand-woven wool tunic and the "
            "edge of a DARK OLIVE-GREEN mantle move past behind the wrists, "
            "their coarse over-and-under weave readable. Behind, thrown "
            "completely soft, the worn pale limestone edges of the great stair "
            "and warm late-afternoon light. Nothing else is in the frame."
        ),
    },
    # ===== n11 — he went down those steps a different man (white) ===========
    {
        "id": "v2-r039-b49", "out": "s49-a-different-man.jpeg",
        "seg": "n11", "window": "197.576-201.026", "wide": True, "jesus": False,
        "locks": ["PUBLICAN", "JUDEAN-LAND", "MARKET-TOWN", "BACKGROUND-CAST"],
        "char_refs": _PUB,
        "narration": "He went down those steps a different man, and he had not done",
        "must_show": "The tax collector at the foot of the great stair standing in the street in the late light, seen in profile, his head level for the first time.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MOCK + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            "One photograph, 50mm lens at f/4, THE CAMERA STANDING OFF TO THE "
            "SIDE AT A RIGHT ANGLE TO THE DIRECTION HE FACES, so he is in "
            "strict SIDE-ON PROFILE, the far cheek and far eye hidden behind "
            "the bridge of his nose, his single visible eye level and aimed "
            "straight out through the LEFT EDGE — NOT AT THE CAMERA. " + _GRAIN +
            "He has just come off the last course of the enormous pale "
            "limestone stair, which climbs away behind him and fills the right "
            "of the frame, and he stands still in the dusty street at the foot "
            "of it, full length from head to sandals, right of centre. A "
            "thickset BAREHEADED Judean man of about thirty-eight with SHORT "
            "COARSE BLACK HAIR cut at the top of the neck, a SHORT CROPPED "
            "BLACK BEARD and warm sun-darkened olive-brown skin, in a DEEP "
            "RUST-BROWN tunic and DARK OLIVE-GREEN mantle. HIS HEAD IS LEVEL "
            "FOR THE FIRST TIME IN THE STORY and his shoulders have come down "
            "and back; his hands hang open at his sides. Low warm "
            "late-afternoon sun comes from the LEFT and IN FRONT of him, laying "
            "a long shadow behind him and lighting the front planes of his "
            "face; the sun is well out of frame and there is no light source "
            "behind or above his head. Tan mud-brick house walls with FLAT "
            "roofs of poles and packed earth stand along the street. At most "
            "three other townspeople pass further off, small, seen from behind, "
            "every one a solid dark mass of umber, charcoal or deep rust from "
            "head to foot."
        ),
    },
    {
        "id": "v2-r039-b50", "out": "s50-he-had-nothing-to-offer.jpeg",
        "seg": "n11", "window": "201.026-204.506", "wide": False, "jesus": False,
        "locks": ["PUBLICAN", "JUDEAN-LAND"], "char_refs": _PUB,
        "narration": "done one thing to earn it. He had nothing to offer, and he",
        "must_show": "A close strict profile of the tax collector's face in the warm late light, changed — the shame gone out of it and something careful and stunned left behind.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MOCK + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the direction he "
            "faces, so we see the clean edge of his profile against the soft "
            "warm street beyond — the near cheek, the eyelash line, the short "
            "blunt nose in silhouette — and THE FAR CHEEK AND FAR EYE ARE "
            "HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND NOT VISIBLE AT ALL. His "
            "single visible eye is OPEN AND LEVEL now, aimed straight out "
            "through the LEFT EDGE at something ordinary further down the "
            "street. The pose itself makes a look into the lens physically "
            "impossible. "
            "One photograph, 85mm lens at f/2, head and shoulders only, the "
            "dusty street and tan mud-brick walls behind him thrown completely "
            "soft. " + _GRAIN +
            "He is a thickset Judean man of about thirty-eight with warm "
            "sun-darkened olive-brown Middle Eastern skin, a broad face, heavy "
            "cheeks, a SHORT CROPPED BLACK BEARD and SHORT COARSE BLACK HAIR "
            "cut at the top of the neck, HIS HEAD BARE, in a DEEP RUST-BROWN "
            "tunic and DARK OLIVE-GREEN mantle. THE FACE HAS CHANGED: the jaw "
            "is unclenched, the brow smooth, the mouth slightly open on an "
            "ordinary breath — CAREFUL, STUNNED RELIEF, the look of a man who "
            "has been let off something and does not quite trust it yet. It is "
            "not a smile, not a laugh and not tears. Low warm late-afternoon "
            "sun from the LEFT and IN FRONT lands on the brow, the nose and the "
            "cheek; the back and top of his head stay in his own shadow, the "
            "sun is well out of frame, and there is no light source anywhere "
            "behind or above his head."
        ),
    },
]

BEATS += [
    {
        "id": "v2-r039-b51", "out": "s51-the-only-thing-he-got-right.jpeg",
        "seg": "n11", "window": "204.506-208.548", "wide": True, "jesus": False,
        "locks": ["PUBLICAN", "JUDEAN-LAND", "MARKET-TOWN", "BACKGROUND-CAST"],
        "char_refs": _PUB,
        "narration": "he knew it. That turned out to be the only thing he needed to get right.",
        "must_show": "The tax collector walking away up the sunlit street with his back to the camera, ordinary town life going on around him.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            "One photograph, 50mm lens at f/4, THE CAMERA STANDING IN THE "
            "STREET BEHIND HIM AND SHOOTING PAST HIM up the lane; he is seen "
            "ENTIRELY FROM BEHIND, walking AWAY from the lens, and HIS FACE IS "
            "NOT VISIBLE AT ALL. " + _GRAIN +
            "He is centre frame, full length from head to sandals, mid-stride "
            "with one arm swinging — a thickset BAREHEADED man of about "
            "thirty-eight with SHORT COARSE BLACK HAIR cut at the top of the "
            "neck and a clear band of that black hair showing at the nape, in a "
            "DEEP RUST-BROWN tunic and DARK OLIVE-GREEN mantle. HIS BACK IS "
            "STRAIGHT AND HIS SHOULDERS ARE DOWN. Low warm late-afternoon sun "
            "comes down the lane from ahead of him and OUT of frame, so his "
            "long shadow runs back toward the camera along the packed earth and "
            "pale dust. Tan mud-brick house walls with FLAT roofs of poles and "
            "packed earth run away on either side, plain rectangular openings "
            "with no glass in them, one plain square-topped doorway with a flat "
            "stone lintel. At most three other townspeople are in the lane "
            "going about ordinary business, all of them small, seen from behind "
            "or in profile, every one a solid dark saturated mass of umber, "
            "charcoal, deep rust or deep indigo from head to foot, and NO PALE "
            "OR OFF-WHITE CLOTH APPEARS ON ANYBODY. THIS IS A WIDE FULL-LENGTH "
            "STREET PHOTOGRAPH AND NOT A PORTRAIT."
        ),
    },
    # ===== n12 — and the Pharisee? POSITION A, after everyone has gone. ======
    {
        "id": "v2-r039-b52", "out": "s52-still-standing-there.jpeg",
        "seg": "n12", "window": "208.548-212.098", "wide": True, "jesus": False,
        "locks": _T_PHA, "char_refs": _PHA,
        "narration": "And the Pharisee? He is still standing there,",
        "must_show": "POSITION A AGAIN, the identical fixed framing of the same spot on the temple pavement — the Pharisee still standing in exactly the same place with his arms still raised, but the light has moved on and the court has emptied.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE,
        "scene": (
            "THIS IS CAMERA POSITION A AGAIN AND IT HAS NOT MOVED: the same "
            "35mm lens standing BEHIND THE PHARISEE AND ABOUT A MAN'S HEIGHT "
            "ABOVE HIM, the same spot on the enormous open limestone pavement, "
            "the same distance, the same far sanctuary. THE COMPOSITION IS "
            "DELIBERATELY IDENTICAL TO THE EARLIER FRAMES OF THIS SPOT — ONLY "
            "THE LIGHT AND THE CROWD HAVE CHANGED. " + _GRAIN +
            "THE CAMERA SHOOTS PAST HIM: he is seen ENTIRELY FROM BEHIND, full "
            "length from head to sandals, standing in exactly the same place "
            "with BOTH ARMS STILL RAISED and both hands still open, and HIS "
            "FACE IS NOT VISIBLE AT ALL. A tall spare upright man of about "
            "fifty in a DEEP INDIGO BLUE tunic under a DARK BLUE-BLACK "
            "tasselled mantle, THICK IRON-GREY HAIR combed back and cut level "
            "at the middle of the neck with a clear band of that iron-grey hair "
            "showing at the nape. THE LIGHT HAS MOVED: the sun is now low and "
            "coming from the RIGHT, so his shadow lies long across the flags to "
            "the left instead of short beneath him, and the pavement has gone "
            "warm gold. THE COURT HAS EMPTIED: where several worshippers stood "
            "before, only ONE distant figure remains far off at the edge, small "
            "and dark. The column of pale grey-white smoke beyond the sanctuary "
            "is thinner now. The sun is well out of frame and there is no light "
            "source behind or above his head."
        ),
    },
    {
        "id": "v2-r039-b53", "out": "s53-still-praying-still-certain.jpeg",
        "seg": "n12", "window": "212.098-215.938", "wide": True, "jesus": False,
        "locks": _T_PHA, "char_refs": _PHA,
        "narration": "still praying, still certain, still fine.",
        "must_show": "POSITION A once more, the same fixed framing, the shadows longer again and the court now completely empty except for him.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE + "no other person, figure or blurred stranger anywhere in the frame; ",
        "scene": (
            "THIS IS CAMERA POSITION A AGAIN AND IT STILL HAS NOT MOVED: the "
            "same 35mm lens BEHIND HIM AND ABOUT A MAN'S HEIGHT ABOVE, the same "
            "spot, the same distance, the same far sanctuary — THE COMPOSITION "
            "IS DELIBERATELY IDENTICAL and only the light and the emptiness "
            "have changed again. " + _GRAIN +
            "He is seen ENTIRELY FROM BEHIND, full length from head to sandals, "
            "in exactly the same place with both arms still raised, and HIS "
            "FACE IS NOT VISIBLE AT ALL — a tall spare upright man of about "
            "fifty in a DEEP INDIGO BLUE tunic under a DARK BLUE-BLACK "
            "tasselled mantle, THICK IRON-GREY HAIR combed back and cut level "
            "at the middle of the neck, a clear band of it at the nape. THE SUN "
            "IS LOWER STILL and further to the RIGHT: his shadow now stretches "
            "an enormous distance across the flags to the left edge of the "
            "frame, the low light rakes hard across the worn surface of the "
            "stone and picks out every hollow and joint, and the pavement has "
            "gone deep warm amber. THERE IS NOT ONE OTHER PERSON ANYWHERE IN "
            "THE PICTURE — the whole enormous court is empty except for him. "
            "The sun is well out of frame and there is no light source behind "
            "or above his head."
        ),
    },
    {
        "id": "v2-r039-b54", "out": "s54-the-saddest-part.jpeg",
        "seg": "n12", "window": "215.938-219.678", "wide": False, "jesus": False,
        "locks": _T_PHA, "char_refs": _PHA,
        "narration": "That is the saddest part of it. The only thing keeping that man",
        "must_show": "A close strict profile of the Pharisee's face in the low warm light, entirely serene and satisfied — a man who has no idea anything is wrong.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_MOCK + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the direction he "
            "faces, so we see the clean edge of his profile against the soft "
            "warm pavement beyond — the near cheek, the eyelash line, the long "
            "straight nose in silhouette — and THE FAR CHEEK AND FAR EYE ARE "
            "HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND NOT VISIBLE AT ALL. His "
            "single visible eye is open, level and aimed slightly UPWARD and "
            "forward, out through the RIGHT EDGE at the ordinary evening sky "
            "above the far wall. The pose itself makes a look into the lens "
            "physically impossible. "
            "One photograph, 85mm lens at f/2, head and shoulders only, the "
            "empty amber court behind him thrown completely soft. " + _GRAIN +
            "He is a tall spare Judean man of about fifty with warm olive-brown "
            "Middle Eastern skin, a high clear forehead, a long straight nose, "
            "a FULL SQUARED IRON-GREY BEARD carefully combed and THICK "
            "IRON-GREY HAIR combed straight back and cut level at the middle of "
            "the neck, HIS HEAD BARE, in a DEEP INDIGO BLUE tunic and DARK "
            "BLUE-BLACK tasselled mantle. HIS EXPRESSION IS COMPLETELY SERENE: "
            "the brow smooth, the eyes bright and untroubled, the mouth "
            "relaxed and faintly content — a good man entirely at peace with "
            "himself, with NOTHING sneering, gloating, cruel, comic or ugly "
            "anywhere in the face. The sadness is only in the situation, never "
            "in the drawing of him. Low warm evening sun from the LEFT and IN "
            "FRONT lands on the front planes of the face while the back and top "
            "of his head stay in his own shadow; the sun is well out of frame "
            "and there is no light source behind or above his head. The sky "
            "above the far wall is ordinary deepening blue and there is nothing "
            "whatever in it."
        ),
    },
]

BEATS += [
    {
        "id": "v2-r039-b55", "out": "s55-sure-he-was-already-in.jpeg",
        "seg": "n12", "window": "219.678-223.591", "wide": True, "jesus": False,
        "locks": _T_PHA, "char_refs": _PHA,
        "narration": "man out was how sure he was that he was already in.",
        "must_show": "POSITION A a final time at the last of the light — the same fixed framing, the same man in the same place, alone in an enormous empty court.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM + _NO_CHURCH + _NO_BLOOD + _NO_MOCK + _GAZE + "no other person, figure or blurred stranger anywhere in the frame; ",
        "scene": (
            "THIS IS CAMERA POSITION A FOR THE LAST TIME AND IT HAS NOT MOVED: "
            "the same 35mm lens BEHIND HIM AND ABOUT A MAN'S HEIGHT ABOVE, the "
            "same spot on the enormous open limestone pavement, the same "
            "distance, the same far sanctuary — THE COMPOSITION IS DELIBERATELY "
            "IDENTICAL TO EVERY EARLIER FRAME OF THIS SPOT. " + _GRAIN +
            "He is seen ENTIRELY FROM BEHIND, full length from head to sandals, "
            "still in exactly the same place with both arms still raised, and "
            "HIS FACE IS NOT VISIBLE AT ALL — a tall spare upright man of about "
            "fifty in a DEEP INDIGO BLUE tunic under a DARK BLUE-BLACK "
            "tasselled mantle, THICK IRON-GREY HAIR combed back and cut level "
            "at the middle of the neck, a clear band of it at the nape. IT IS "
            "THE LAST OF THE LIGHT: the sun has dropped almost to the top of "
            "the far wall on the RIGHT and is out of frame; only the upper "
            "courses of the distant stonework and the top of the sanctuary "
            "still carry warm light, the pavement around him has gone into cool "
            "blue shadow, and his own long shadow has been swallowed by it. The "
            "column of smoke beyond the sanctuary has died to a thin thread. "
            "THERE IS NOT ONE OTHER PERSON ANYWHERE IN THE PICTURE: the whole "
            "enormous court is completely empty except for this one small "
            "standing figure with his arms up. There is no light source behind "
            "or above his head and nothing outlines his hair."
        ),
    },
    # ===== n13 — the closing application (white) ============================
    {
        "id": "v2-r039-b56", "out": "s56-to-let-them-in-too.jpeg",
        "seg": "n13", "window": "223.591-227.841", "wide": False, "jesus": True, "ref": REF,
        "locks": ["STREET-STEPS", "JUDEAN-LAND"],
        "narration": "Jesus did not tell this story to shame the good men listening. He told it to let",
        "must_show": "A close strict profile of Jesus on the city steps in the late light, his face gentle and open — not accusing anybody.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the camera stands at a RIGHT ANGLE to the line between "
            "Jesus and the men he is speaking to, so we see the clean edge of "
            "his profile against the shadowed limestone wall, and THE FAR CHEEK "
            "AND FAR EYE ARE HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND NOT "
            "VISIBLE AT ALL. His single visible eye is level, wide and gentle, "
            "aimed straight ACROSS the frame and out through the LEFT EDGE. The "
            "pose itself makes a look into the lens physically impossible. "
            "One photograph, 85mm lens at f/2, head and shoulders only, the "
            "blank limestone block wall four paces behind him thrown completely "
            "soft and reading DARKER than he does. Low warm late-afternoon sun "
            "comes from the LEFT and IN FRONT and lands on the front planes of "
            "his face — the brow, the nose, the cheekbone, the beard — while "
            "the back and top of his head stay in his own shadow; the sun is "
            "well out of frame and there is no light source anywhere behind or "
            "above his head, and nothing outlines his hair. " + _GRAIN +
            "His mouth is closed and soft at the corners, the brow unfurrowed, "
            "the whole face UNGUARDED, WARM AND WITHOUT ACCUSATION — he is not "
            "rebuking anyone and there is no anger, no severity and no "
            "hardness in it. Nothing else is in the frame: no other person, no "
            "hand, no object, no shoulder at any edge."
        ),
    },
    {
        "id": "v2-r039-b57", "out": "s57-the-door-is-not-closed.jpeg",
        "seg": "n13", "window": "227.841-232.421", "wide": True, "jesus": False,
        "locks": _GATE,
        "narration": "it to let them in too. The door is not closed to people who have done wrong. It only",
        "must_show": "ONE plain square-topped gateway standing WIDE OPEN AND EMPTY in a mud-brick wall, with warm light lying through it across the ground inside — there is no leaf, no door and nothing blocking it at all.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_IRONGATE + _NO_MODERN_TOWN + _GAZE + "NO DOOR LEAF, PANEL, SLAB, PLANK, SHUTTER, CURTAIN, HANGING, GRILLE, BAR OR OBSTRUCTION OF ANY KIND ANYWHERE IN OR ACROSS THE OPENING — the opening is completely clear from threshold to lintel and from jamb to jamb; and nothing is closing, swinging or standing part way across it; ",
        "scene": (
            "One photograph, 35mm lens at f/5.6, THE CAMERA STANDING SQUARE ON "
            "TO THE WALL FROM OUTSIDE, a little back and a little to the side, "
            "looking straight through the opening; there is NO PERSON ANYWHERE "
            "IN THIS PICTURE so no gaze exists to meet the lens. " + _GRAIN +
            "THE WALL is sun-dried tan mud brick over a footing of undressed "
            "field stone, plastered with mud and straw and weathered pale, "
            "about the height of a man and a half, its top finished flat with a "
            "course of rough stones. THE GATEWAY cut through it is a PLAIN "
            "UPRIGHT RECTANGLE — two jambs of dressed limestone blocks and ONE "
            "SINGLE FLAT LIMESTONE LINTEL laid straight across the top, "
            "SQUARE-TOPPED, with a worn hollowed limestone threshold slab at "
            "ground level rubbed smooth and dished by generations of feet. THE "
            "OPENING IS COMPLETELY EMPTY AND CLEAR: there is no door, no leaf, "
            "no panel, no plank, no shutter, no curtain and nothing at all "
            "standing in it or across it, and one can see straight through it. "
            "Through that clear rectangle, low warm late-afternoon sun lies "
            "across the beaten earth of the courtyard beyond in one long bright "
            "shape, running toward the camera over the threshold stone and out "
            "onto the dust outside. Bare packed earth and pale dust worn hollow "
            "by feet outside; one grey-green olive tree beyond the wall against "
            "a deepening blue sky. THIS IS A WIDE SCENE AND NOT A PORTRAIT: the "
            "whole run of wall, the whole opening and the ground on both sides "
            "of it are in frame together."
        ),
    },
    {
        "id": "v2-r039-b58", "out": "s58-closes-from-the-inside.jpeg",
        "seg": "n13", "window": "232.421-236.952", "wide": True, "jesus": False,
        "locks": _GATE,
        "narration": "It only closes from the inside. By people convinced they do not need it.",
        "must_show": "The SAME open gateway seen from INSIDE the courtyard looking out, still wide open and clear, with one ordinary man stepping in over the threshold from the sunlit street, seen from behind.",
        "must_not_show": _NO_HALO + _NO_DEITY + _NO_CREAM_STRICT + _NO_CHURCH + _NO_IRONGATE + _NO_MODERN_TOWN + _NO_MOCK + _GAZE + "NO DOOR LEAF, PANEL, SLAB, PLANK, SHUTTER, CURTAIN, HANGING, GRILLE, BAR OR OBSTRUCTION OF ANY KIND ANYWHERE IN OR ACROSS THE OPENING, nothing swinging shut, nothing standing part way across it, and nobody's hand on any door; ",
        "scene": (
            "REVERSE OF THE PREVIOUS FRAME AND THE SAME GATEWAY. One "
            "photograph, 35mm lens at f/4, THE CAMERA STANDING INSIDE THE "
            "COURTYARD IN THE SHADE, BEHIND THE MAN, looking out through the "
            "opening into the sunlit street. " + _GRAIN +
            "THE OPENING IS THE SAME PLAIN UPRIGHT SQUARE-TOPPED RECTANGLE — "
            "two dressed limestone jambs and ONE SINGLE FLAT LIMESTONE LINTEL "
            "straight across the top, the worn hollowed threshold slab below — "
            "and IT IS COMPLETELY EMPTY AND CLEAR from threshold to lintel and "
            "from jamb to jamb, with no door, leaf, panel, shutter or curtain "
            "anywhere in it or beside it. ONE ORDINARY JUDEAN MAN in a plain "
            "DARK UMBER hand-woven wool tunic with a DEEP RUST mantle, "
            "sun-darkened olive-brown skin and short dark hair, is stepping IN "
            "over the threshold stone and INTO the courtyard, walking TOWARD the "
            "camera position but seen ENTIRELY FROM BEHIND because the camera "
            "sits deeper in the courtyard than he does and is turned back "
            "toward the opening: what the lens reads is his BACK, his "
            "shoulders and the back of his head, large and low in the near "
            "frame, and HIS FACE IS NOT VISIBLE AT ALL. His weight is on the "
            "forward foot and one hand is loose at his side, touching nothing. "
            "Low warm late-afternoon sun in the street beyond throws his long "
            "shadow ahead of him across the courtyard floor toward the camera "
            "and fills the whole clear rectangle of the opening with warm "
            "light. THIS IS A WIDE FULL-LENGTH SCENE AND NOT A PORTRAIT: the "
            "whole opening, the man from head to sandals and the ground on both "
            "sides are in frame together. NOBODY ELSE IS IN THE PICTURE."
        ),
    },
]


# ---------------------------------------------------------------------------
# COURT-BOUNDARY INJECTION (2026-08-02). A classical colonnade of ROUND COLUMNS
# arrived in the temple court FOUR separate times: through the shared
# TEMPLE-COURT lock's own "PLAIN SQUARE-SECTION STONE PIERS" (b05, b06); again
# after that lock was hardened with an explicit prohibition list (b17); again
# after the covered walk was DELETED from the lock outright (b17 second pass);
# and again at extreme distance along the horizon (b26, b52, b53, b55). Rows 10
# and 14 already proved a prohibition loses to a strong noun, and "temple court"
# is one of the strongest -- while the shared lock sits ~1500 words before the
# scene text where the model's attention actually lands.
#
# So the cure is moved to the FRONT OF THE BEAT'S OWN SCENE -- the nearest text
# -- and stated as GEOMETRY (what the eye meets at each edge) plus an INVENTORY
# of everything allowed to stand up off the pavement, rather than as another
# list of forbidden orders. Injected mechanically into every WIDE beat staged in
# the temple so no beat can be missed and the wording cannot drift between them.
_COURT_BOUND = (
    "WHAT BOUNDS THIS COURT, STATED FIRST BECAUSE IT GOVERNS THE WHOLE FRAME: "
    "to the left, to the right and across the far side this court is bounded by "
    "ONE PLAIN UNBROKEN CLIFF OF STONE -- a high blank wall of very large "
    "square-cut pale limestone blocks in level mortarless courses, rising "
    "straight up from the pavement to a flat top edge against open sky. THAT "
    "WALL HAS NOTHING STANDING IN FRONT OF IT AND NOTHING SET INTO IT: no row "
    "of columns, pillars, piers, posts, uprights or shafts of any kind; no "
    "arcade, colonnade, cloister, covered walk, roofed aisle, portico, porch or "
    "stoa; no repeating openings, arches, recesses, niches, bays or shadowed "
    "gaps running along it; and no roof, canopy or overhang projecting from it. "
    "FROM ONE END OF THE PICTURE TO THE OTHER IT IS BLANK STONE AND NOTHING "
    "ELSE. "
    "THE FAR DISTANCE, STATED AS AN INVENTORY BECAUSE THAT IS WHERE A COLONNADE "
    "KEEPS REAPPEARING: counting everything that stands up off the pavement "
    "anywhere in this picture, there are EXACTLY TWO BUILT OBJECTS AND NO THIRD "
    "-- the ONE tall plain rectangular sanctuary block, and the ONE square mass "
    "of the altar with its ramp. Everything else in the frame is flat pavement "
    "below and blank bounding wall behind. BETWEEN THE TOP EDGE OF THAT WALL "
    "AND THE OPEN SKY THERE IS NOTHING AT ALL: no roofline, no parapet, no "
    "crenellation, no battlement, no cornice, no colonnade, no row of columns "
    "or piers, no second building, no tower, no gate house and no structure of "
    "any kind, near or far, sharp or blurred, at any point along the horizon. "
)

for _b in BEATS:
    if _b.get("wide") and "TEMPLE-COURT" in _b.get("locks", []):
        _b["scene"] = _COURT_BOUND + _b["scene"]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "TEMPLE-COURT": "PLACE-REF/temple-court.jpeg",  # build-39-pharisee-publican s23-not-asking-for-anything (manual)
}
# === end PLACE-PLATES ===
