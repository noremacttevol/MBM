#!/usr/bin/env python3
"""V2 beat map — row 36, build-36-shrewd-steward (Luke 16:1-13). REALISTIC V2.

THE INHERITED SCAFFOLD WAS DISCARDED and is kept beside this file as
`beats_v2.py.inherited-scaffold` for provenance only. Two measured reasons:
  1. It planned 31 pictures at 5.7 s each and called that "the library
     density" — against the wave's MEASURED 3.1-4.9 s per picture across rows
     24-35. A picture costs about thirteen cents and regenerates in seconds; a
     five-and-a-half second hold is the exact defect V2 exists to remove.
  2. Its windows were NOT CONTIGUOUS and were not in time order — it left
     dead intervals (2.70-3.82, 11.25-12.44, 21.17-21.76, 53.38-53.99,
     73.01-74.11, 166.46 onward) where no picture is declared at all.

WHAT V1 ACTUALLY DID (verified against the artefact, not the prose):
  EIGHT stills for 177.87 s of finished video, and the holds are among the
  worst in the wave:
    * `s8-two-masters.jpeg` covers j13 + n9 + n10 — 136.48 s to 171.49 s,
      THIRTY-FIVE SECONDS on ONE picture: the whole two-masters saying
      (Luke 16:13), the line that ties the story together, AND the ENTIRE
      closing application, the reason the video exists. The closing
      application therefore had no picture of its own at all.
    * `s1-accused.jpeg` covers s1 + j0 + n1 + n2 — 0.00 s to 32.29 s,
      THIRTY-TWO SECONDS: the opening scripture, the whole red-letter setup,
      the manager at work, the accusation, the summons and the dismissal —
      six distinct events on one image.
    * `s6-commended.jpeg` covers j1 + n7 — 88.26 s to 113.49 s, TWENTY-FIVE
      SECONDS, including the hinge of the parable ("he had done wisely") and
      the paragraph that explains what Jesus did and did not praise.
    * `s7-welcomed.jpeg` covers j2 + n8 — 113.49 s to 136.48 s, TWENTY-THREE
      SECONDS.
  V2 gives all seventeen spoken segments their own pictures: 47 pictures over
  171.494 s = 3.65 s/picture, shortest 1.78 s, longest 5.01 s.
  `s8b-the-fork.jpeg` sits in V1's assets and is never used by V1's BEATS.

AUDIO: LOCKED, never re-voiced, V1 never written to. The V1 MP4's audio stream
is 177.888 s and extract_beats' reconstruction of V1's own timeline arithmetic
(LEAD 0.28, GAP 0.72, KJV_GAP 1.15, TAIL 1.5, seven scripture/Jesus segments)
totals 177.872 s — 0.016 s apart, nowhere near the 0.75 s staleness tripwire.
GIT CONTENT DATES (mtimes are worthless here): every mp3 is 2026-07-24T04:03:29
and the MP4 is 2026-07-24T07:56:18, i.e. the shipped video POST-DATES all of its
own audio, and make_narration.py (2026-07-23T05:12:00) pre-dates both. Neither
tripwire fires, so the normal packet-copy AUDIO LOCK applies.

SOURCING TRAP CHECKED AND CLEARED: all 18 segments transcribed with
faster-whisper (small.en, word_timestamps=True) and compared against the LIVE
make_narration.py — not the V2-folder copy, not the `.pre-echo`/`.pre-speaker`
siblings. Every segment matches. Four apparent differences were chased down and
every one of them is whisper's, not the audio's:
  * j6/n5/n6  "write fifty" / "write down fifty" / "eighty" came back as the
    NUMERALS "50" and "80" — whisper normalises spoken numbers to digits.
  * j2  "when YE fail" came back as "when you fail" — whisper does not have
    the archaic pronoun and substitutes the modern one; the audio says "ye".
  * j1/j13  "the Lord" / "Mammon" capitalisation only.
  * n3  whisper's first word is "the", dropping the script's leading "And" —
    it habitually swallows an unstressed sentence-initial "And" (rows 33 and
    34 both saw it). Caption text comes from the V1 script regardless.
No TEXT_OVERRIDES and no SPEAKER_OVERRIDES: this build already uses the modern
mbm_speakers constants (SCRIPTURE / JESUS / NARRATOR), so caption colour is
correct without help.

WINDOWS: rebuilt from scratch from extract_beats plus the MEASURED word
timings, never from the `.timing.json` sidecars. Contiguous 0.000 -> 171.494
(the card's own start), ZERO gaps, and every one of the seventeen speech onsets
lands inside the window written for it. Each interior split is placed 0.15 s
BEFORE the onset of the word it belongs to, so a picture is never still
changing while its first word is already sounding.

CONTENT CARE — THIS IS THE HARDEST PARABLE IN THE GOSPELS TO STAGE HONESTLY.
The master commends the steward's SHREWDNESS, not his dishonesty, and the
narration says so outright ("He was not praising the cheating. He was pointing
at the urgency"). So:
  * NO FRAME CELEBRATES THE FRAUD. Nobody winks, smirks, gloats, sneers,
    laughs slyly, exchanges a conspiratorial glance, counts money with
    delight, toasts, or is lit or framed as a hero pulling off a heist. The
    dealings are painted matter-of-fact, hurried and tense — a frightened man
    working fast. The `_NO_HEIST` clause below carries this into every beat of
    the parable and it is not optional.
  * The commendation beat (b23) is the master's RUEFUL, COMPLICATED look — a
    head shaken while half-smiling at the sheer nerve of it — never a triumph
    shot, never a handshake, never an embrace, never a reward handed over.
  * The debtors are painted neither as victims being robbed nor as
    accomplices: ordinary men handed their own sheet, astonished.
  * Nothing of heaven, hell, throne, crown, gate, angel, wing, judgement,
    death, punishment or afterlife is painted anywhere in this build, because
    the narration states none of it. "Everlasting habitations" (j2) is staged
    as what the word actually says in that world — A HOUSE, at dusk, whose
    people take a traveller in — never a sky-city, never a gate of light.
    "Past the end of your life" (n8) is staged as Jesus speaking, never as a
    deathbed, a grave or a departing soul.
  * GOD IS NEVER DEPICTED AS ANY FIGURE, FACE, FORM, LIGHT OR PRESENCE. This
    matters most at b40, "Ye cannot serve God and mammon", which is staged on
    Jesus's own face and nowhere else. The two-masters illustration (b38, b39,
    b42) uses TWO ORDINARY HUMAN HOUSEHOLDERS in a courtyard, which is exactly
    what the saying's own image is; neither stands for God and neither is lit,
    framed or robed to suggest it, and money is never personified.
  * Nobody is seized, dragged or restrained anywhere in this cut.

WHO CARRIES WHICH RED-LETTER LINE. Jesus is on screen ONLY in the frames he
actually speaks in as himself. j3 ("What shall I do?... I cannot dig; to beg I
am ashamed") and j6 ("Take thy bill, and sit down quickly, and write fifty")
are red-letter but they are THE STEWARD talking INSIDE the parable — putting
Jesus's face under a caption of a panicking man planning a write-down would
invert the line, so both are staged inside the parable where the words are
said. j0 is Jesus narrating the setup, and its two frames illustrate the setup
rather than showing him, because b01 has just shown him beginning to speak.
j1 splits: its first clause is the master commending, staged inside the parable
(b23); its second clause is Jesus's own comment on the world and returns to him
(b24, b25). j2 and j13 are Jesus speaking as himself throughout.

STAGING — six places, none of them repeating a composition used elsewhere in
the realistic wave (rows 2/8/21 Luke 15; 11 night gale; 16 interior; 19 dawn
shore; 22 basalt doorstep; 23 terraced hillside; 24 moored boat; 25 wheat
field; 26 kitchen garden; 27 synagogue bench + baking yard; 28 ploughed field +
mud-brick hut; 29 limestone shelf / caravan road / quayside / stone courtyard;
30 breakwater / open water / strand; 31 night road + bridegroom's house; 32
trading yard + master's hall; 33 mount + six mercy scenes; 34 barns + threshing
floor; 35 banquet house + city lanes):
  * the FLAT MUD-BRICK ROOFTOP of a village house in clear morning light,
    where Jesus sits with his disciples above the waking town — a rooftop is
    used by no other row in the wave, and Luke 16:1 says he said it "unto his
    disciples", so the frame is a teaching among his own men, not a crowd;
  * the RICH MAN'S WALLED WORKING YARD, its storerooms and its gateway (row
    32's master's hall was an interior reception room and row 29's stone
    courtyard was a merchant's; this is an open agricultural work yard with
    sunken oil jars, and it states so positively);
  * the ACCOUNTS CORNER of that yard — a shaded recess with the loose bill
    sheets standing in a reed basket, worked sitting on a floor mat;
  * the OIL STORE, a cool half-dark room of great sunken fired-clay jars;
  * the ESTATE'S GRAIN BINS (row 34's barns were a farm's own granary seen
    from outside on a reaped field; these are small plastered bins inside a
    working yard wall, in shade, with sacks);
  * the VILLAGE LANE and its doorways in daylight and at dusk (row 35's lanes
    were stepped and lamplit at night; these are level, sunlit, and the dusk
    frames are lit by a single clay lamp INSIDE a doorway).

LOCK-WORDING AUDIT (the row-34/35 lesson: read every lock you write as if the
model will build the most modern thing your words permit). Five rewrites before
the first paid image:
  * "office" and "desk" never appear; the shared ESTATE-ACCOUNTS lock is named
    on every beat where a sheet, a pen or a basket of bills is visible, and
    the beat text ALSO restates the loose-sheet geometry, because a close
    macro is where a shared lock is weakest.
  * "bill" is everywhere stated as ONE LOOSE LEAF, because the bare word
    invites a bound page.
  * "storeroom door" was deleted outright: every opening in this build is
    stated as a plain rectangular gap closed by a hanging panel of dark cloth,
    because "door" invites hinges and "plank" invites battens (the row-35
    lesson, learned when "a plank of adzed timber" produced a battened door on
    iron hinges).
  * "grain bin" is pinned to the shared GRANARY-BARN lock so it cannot become
    a silo or a boarded American barn.
  * "counting money" is stated as LOOSE STRUCK COINS TIPPED FROM A CLOTH
    PURSE INTO A PALM, because "counting" invites an abacus, a ledger and
    stacked columns.

CAST: TWO anchors, both of them pictures that had to exist on the timeline
anyway, so the anchors cost nothing extra. Both are generated in ONE anchor run
before anything else, and NEITHER has the other anchor in its frame, so the
REFS cache cannot make an anchor reference itself.
  b05 MASTER   — face-showing, strict side-on profile, alone in his yard.
  b09 STEWARD  — face-showing, strict side-on profile, alone against a wall.
Jesus needs no anchor: he carries JESUS-V2-REF on every frame he is in.
The two debtors appear in four and three frames respectively and are held by
text locks plus the steward's own attached anchor in the same frames. The
disciples are never given a face: every rooftop group beat puts the camera
BEHIND them, which is simultaneously the lens-gaze cure and the reason no
recurring apostle can drift off his CAST-BIBLE sheet in this build.
"""

import os

OUTPUT_ASSET_DIR = "assets"

# See the AUDIO paragraph above: neither staleness tripwire fires, so the
# normal packet-copy AUDIO LOCK applies. Nothing is re-voiced, nothing is
# re-timed, and the V1 build is never written to.
AUDIO_FROM_V1_SEGMENTS = False

REF = True

# Wired in AFTER the two anchor beats are generated in their own run.
A_MASTER = "assets/s05-word-came-to-the-rich-man.jpeg"
A_STEW = "assets/s09-what-shall-i-do.jpeg"
REFS = {"MASTER": A_MASTER, "STEWARD": A_STEW}

_HERE = os.path.dirname(os.path.abspath(__file__))


def _have(rel):
    """ANCHOR-FIRST: a character reference attaches only once its anchor exists.

    On the first (anchor-only) run every list below is empty, so `--check`
    passes and no anchor can reference itself through the REFS cache. Every run
    after it wires the accepted anchors into all the later beats automatically.
    """
    return [rel] if os.path.isfile(os.path.join(_HERE, rel)) else []


_MASTER = _have(A_MASTER)
_STEW = _have(A_STEW)
_BOTH = _MASTER + _STEW

# ---------------------------------------------------------------- negatives ---
_NO_CREAM = ("no cream, off-white, ivory, buff, beige, taupe, sand, khaki, white "
             "or pale garment, tunic, robe, mantle, sash, wrap or head covering on "
             "anybody anywhere in the frame including the blurred edges; ")
_NO_HALO = ("no halo, no nimbus, no aura, no corona, no bright outline, edge or "
            "contour around any head, hair, shoulder or body, and no light source "
            "of any kind standing behind, above or beyond anyone's head; ")
_NO_HEAVEN = ("no heaven, sky kingdom, throne, seat of judgement, crown, gate, "
              "golden street, cloud of glory, opening sky, shaft of light from "
              "above, radiance, angel, wing or winged figure anywhere; no hell, "
              "fire, pit, chain or punishment; no death, corpse, grave, tomb, "
              "shroud, bier or departing spirit; no hand, arm or face reaching "
              "down from the sky; and no depiction of God as any figure, face, "
              "form, light or presence; ")
_NO_HEIST = ("nobody winks, smirks, sneers, gloats, grins slyly, laughs, raises a "
             "cup, shakes hands on a deal, embraces, exchanges a knowing or "
             "conspiratorial glance over anyone's shoulder, or looks pleased with "
             "a trick; no money is handled with delight, no coins are fanned, "
             "spilled in a glittering heap or held up to the light, and nothing "
             "in the lighting, framing or expression makes this look like a "
             "clever heist, a triumph or a celebration; ")
_NO_FORCE = ("nobody is seized, grabbed by the clothing, dragged, hauled, pushed, "
             "struck, bound, roped, chained or restrained, and no hand grips any "
             "person against their will; ")
_NO_OFFICE = ("no bound book, codex, ledger, account book, spine, cover board or "
              "stacked sewn leaves; no ruled lines, columns, grid or tabulated "
              "figures; no sloped writing desk, lectern, bureau, table with legs, "
              "chair, stool or bench with a back; no quill or feather pen, no "
              "glass inkwell, no metal nib, no pencil, chalk or slate; no wax "
              "seal, seal ring, ribbon, envelope or folded sealed letter; no "
              "abacus, counting frame, beads on rods or scales of machined brass; "
              "and no even white machine-made paper anywhere; ")
_NO_MODERN_TOWN = ("no dome, minaret, bell tower, spire, clock, crenellation, "
                   "pitched roof, roof tile, shingle, chimney, gable or "
                   "half-timbering against any sky; no pole, mast, pylon, wire, "
                   "cable, aerial, guardrail, signpost or painted sign; no "
                   "asphalt, tarmac, concrete, kerb, gutter, drain, grating or "
                   "painted road marking; no vehicle, wheel of pneumatic rubber, "
                   "engine or machine of any kind; ")
_NO_GREEN = ("no green meadow, lawn, turf, pasture, moor, fell, upland, heather, "
             "clipped green hedgerow, deciduous woodland or lush temperate "
             "countryside of any kind, and no soft grey overcast northern European "
             "sky; ")
_NO_NIGHT = ("no night, no darkness, no stars, no lamp and no flame anywhere in "
             "this frame; ")
_NO_MODERN_LAMP = ("no candle, wax or taper, no glass, chimney, globe or shade, no "
                   "hurricane lamp, storm lantern, kerosene lamp or oil lantern, no "
                   "metal lamp, no hanging fixture, no ring handle, and no electric "
                   "light of any kind; ")
_NO_MOCK = ("nobody poor or old is drawn grotesque, comic, monstrous, filthy, "
            "ragged to indecency, cowering or pitiable; each is a real person "
            "with dignity; and no modern wheelchair, walking frame, prosthesis, "
            "metal crutch, white gauze bandage or medical dressing appears "
            "anywhere; ")
_GAZE = "nobody's pupils centred on the lens."

# Common lock stacks.
_ROOF_J = ["ROOFTOP", "DISCIPLES", "JUDEAN-LAND"]
_YARD = ["ESTATE", "JUDEAN-LAND", "BACKGROUND-CAST"]
_ACCTS = ["ESTATE-ACCOUNTS", "ESTATE", "STEWARD"]

LOCKS = {
    # ------------------------------------------------------------- people ----
    "STEWARD": (
        "STEWARD LOCK: the steward — the manager who ran everything the rich "
        "man owned — is the SAME MAN in every picture he appears in, and he is "
        "a JUDEAN of the first century, born and weathered in the dry country "
        "of that place. He is about forty, of middling height, lean and "
        "narrow-shouldered, quick on his feet, a man who has spent his life "
        "indoors keeping other men's goods rather than working the ground. HIS "
        "SKIN IS WARM OLIVE-BROWN, clearly Middle Eastern, less weathered than "
        "a field hand's, with a narrow straight nose, a long jaw, and dark "
        "brown eyes set deep under level dark brows. He has a SHORT NEAT DARK "
        "BROWN BEARD trimmed close along the jaw, with a very few grey hairs at "
        "the chin, and THICK DARK BROWN HAIR, straight and pushed back off a "
        "high forehead to just below the ears; it is never long to the "
        "shoulders, never curly, never bare, bald, shaven or thinning, and a "
        "clear band of that dark brown hair shows at the front edge, at the "
        "temples and at the nape in EVERY shot of him, INCLUDING EVERY SHOT "
        "TAKEN FROM BEHIND HIM. HIS HANDS ARE THE POINT OF HIM: long-fingered, "
        "smooth-palmed, soft and unmarked, an educated man's hands with clean "
        "nails and lamp-black ink faintly stained into two fingertips, never a "
        "labourer's cracked and callused hands. HE WEARS EXACTLY THREE SEPARATE "
        "PIECES OF CLOTH AND NOTHING ELSE: (1) ONE ankle-length hand-woven wool "
        "tunic in DARK OLIVE with straight unshaped sleeves to the wrist; "
        "(2) ONE rectangular hand-woven wool mantle in CHARCOAL thrown over the "
        "left shoulder — and THAT MANTLE IS THE LARGEST PIECE OF CLOTH IN "
        "MOST OF HIS FRAMES, SO ITS WEAVE IS STATED HERE: it is a FLAT, THIN, "
        "MATTE LOOM-WOVEN rectangle showing a clear slightly irregular "
        "over-and-under grid of warp and weft threads and a frayed selvedge "
        "edge, exactly like coarse hand-woven wool sacking, and it is NEVER "
        "thick, fluffy, furry, felted, fleeced, brushed, napped, looped, "
        "tufted, blanket-like or sheepskin-like, never knitted, and never has "
        "a raised pile or a soft mottled grey woolly surface; and (3) ONE "
        "folded cloth sash of DEEP RUST knotted at "
        "his waist. On his feet, good plain leather sandals. HE NEVER WEARS "
        "CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, WHITE OR ANY PALE "
        "CLOTH, and he wears no head covering, no turban, no cap, no jewellery, "
        "no ring, no brooch, no clasp, no chain and no belt of manufactured "
        "metal. He is a healthy living man in every frame: no wound, no scar, "
        "no blood, no bandage, no glow and no light of any kind coming off him."
    ),
    "MASTER": (
        "MASTER LOCK: the rich man, the steward's lord, is the SAME MAN in "
        "every picture he appears in, and he is a JUDEAN of the first century. "
        "He is about fifty-five, tall and heavy through the chest and "
        "shoulders, standing square and still, a landowner rather than a "
        "labourer, and NOBODY EVER MISTAKES HIM FOR THE STEWARD — he is a head "
        "taller, far broader, and twenty years older. HIS SKIN IS WARM "
        "SUN-DARKENED OLIVE-BROWN, clearly Middle Eastern, heavily lined across "
        "the forehead and at the outer corners of dark brown eyes, with a broad "
        "blunt nose and heavy dark brows. He has a FULL WIDE BEARD, iron grey "
        "shot through with dark brown, reaching the top of his chest, and THICK "
        "IRON-GREY HAIR waving back off a broad forehead to the nape of his "
        "neck; it is never bare, bald, shaven, cropped or thinning, and a clear "
        "band of that thick grey hair shows at the front edge, at the temples "
        "and at the nape in EVERY shot of him, INCLUDING EVERY SHOT TAKEN FROM "
        "BEHIND HIM. His hands are broad, thick-fingered and steady. HE WEARS "
        "EXACTLY THREE SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) ONE "
        "ankle-length hand-woven wool tunic in DEEP MAROON with straight "
        "unshaped sleeves; (2) ONE rectangular hand-woven wool mantle in DARK "
        "UMBER over both shoulders; and (3) ONE folded cloth sash of DEEP "
        "INDIGO knotted at his waist. Good leather sandals. HE NEVER WEARS "
        "CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, WHITE OR ANY PALE "
        "CLOTH, and he wears no head covering, no turban, no cap, no crown, no "
        "jewellery, no ring, no chain and no metal ornament of any kind. He is "
        "never a caricature of a rich man: not fat, not jewelled, not gloating "
        "and not cruel — a serious working owner. No wound, scar, blood, "
        "bandage or glow anywhere on him."
    ),
    "OIL-DEBTOR": (
        "OIL-DEBTOR LOCK: the first debtor, the man who owes a hundred measures "
        "of olive oil, is the SAME MAN in every picture he appears in, and he "
        "is a JUDEAN olive farmer of the first century. He is about forty-five, "
        "short, thickset and bandy-legged, with WARM DEEPLY SUN-DARKENED "
        "OLIVE-BROWN skin, clearly Middle Eastern, burnt dark across the "
        "cheekbones and the backs of the hands, a wide flat nose and quick "
        "worried dark brown eyes in a nest of squint lines. He has a SHORT "
        "BUSHY BEARD, black going grey in streaks, and SHORT THICK BLACK HAIR "
        "cut close to the skull with grey at the temples, clearly visible at "
        "the crown, the temples and the nape in EVERY shot of him, INCLUDING "
        "EVERY SHOT TAKEN FROM BEHIND HIM. His hands are broad, cracked, "
        "calloused and stained dark green-black from a lifetime of olives — the "
        "exact opposite of the steward's soft hands. HE WEARS EXACTLY TWO "
        "SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) ONE calf-length "
        "hand-woven wool work tunic in DEEP RUST, faded, patched at one "
        "shoulder and mended with plainly visible stitching, with short "
        "straight unshaped sleeves; and (2) ONE twisted cloth belt of DARK "
        "UMBER at his waist. He is barefoot or in worn plain leather sandals. "
        "HE NEVER WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, "
        "WHITE OR ANY PALE CLOTH, and no head covering, no cap, no jewellery "
        "and no metal ornament. He does not share a face with the wheat debtor, "
        "the steward or the master."
    ),
    "WHEAT-DEBTOR": (
        "WHEAT-DEBTOR LOCK: the second debtor, the man who owes a hundred "
        "measures of wheat, is the SAME MAN in every picture he appears in, and "
        "he is a JUDEAN grain farmer of the first century. He is about thirty, "
        "very tall and heavy through the shoulders and arms, stooping slightly "
        "as tall men do indoors, with WARM SUN-DARKENED OLIVE-BROWN skin, "
        "clearly Middle Eastern, a long straight nose, a heavy jaw and steady "
        "dark brown eyes. He has a FULL THICK BLACK BEARD with no grey in it at "
        "all, and THICK BLACK CURLING HAIR to the middle of the neck, clearly "
        "visible at the temples and the nape in EVERY shot of him, INCLUDING "
        "EVERY SHOT TAKEN FROM BEHIND HIM. His hands are enormous, hard and "
        "dusted pale with grain flour. HE WEARS EXACTLY TWO SEPARATE PIECES OF "
        "CLOTH AND NOTHING ELSE: (1) ONE calf-length hand-woven wool work tunic "
        "in DARK UMBER with short straight unshaped sleeves, hitched up and "
        "tucked into (2) ONE twisted cloth belt of DARK OLIVE at his waist. "
        "Worn plain leather sandals. HE NEVER WEARS CREAM, OFF-WHITE, IVORY, "
        "BUFF, BEIGE, SAND, KHAKI, WHITE OR ANY PALE CLOTH, and no head "
        "covering, no jewellery and no metal ornament. He does not share a face "
        "with the oil debtor, the steward or the master."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the men listening to Jesus on the rooftop are between "
        "THREE and FIVE Judean working men of the first century, aged from "
        "about twenty-five to about fifty, fishermen and tradesmen, each with "
        "warm sun-darkened olive-brown Middle Eastern skin, dark hair and a "
        "dark beard, and no two of them sharing a face. THE CAMERA IS ALWAYS "
        "BEHIND THEM AND NOT ONE OF THEIR FACES IS EVER TURNED TOWARD THE "
        "LENS: they are seen as heads, shoulders and backs, sitting or "
        "crouching on the roof, leaning in toward the man they are listening "
        "to. Every one of them is dressed head to foot in ONE SOLID DARK "
        "SATURATED EARTH COLOUR — DEEP INDIGO, DARK UMBER, DEEP RUST, DARK "
        "OLIVE, CHARCOAL or DEEP MAROON — so every listener in the frame, in "
        "focus or out of focus, near or far, sharp or blurred, is a DARK MASS "
        "from edge to edge. NOT ONE OF THEM WEARS CREAM, OFF-WHITE, IVORY, "
        "BUFF, BEIGE, TAUPE, SAND, KHAKI, WHITE OR PALE GREY CLOTH, DRAPE, "
        "MANTLE, SHAWL, TUNIC, SASH OR HEAD COVERING, at any distance and at "
        "any focus — a pale figure among these men reads as a second, unlocked "
        "Jesus and fails the picture. THE ONLY PALE WOOL IN ANY ROOFTOP PICTURE "
        "IS JESUS'S OWN ROBE, and the only other light-toned things anywhere in "
        "the frame are bare stone, mud plaster, dust, reed basketry, raw timber "
        "and bare skin."
    ),
    "TWO-MASTERS": (
        "TWO-MASTERS LOCK: the household in the two-masters saying is THREE "
        "ORDINARY JUDEAN MEN of the first century and NOTHING MORE — this is a "
        "plain domestic picture of a servant with two employers, and NEITHER "
        "HOUSEHOLDER STANDS FOR GOD, is lit, robed, raised, haloed or framed to "
        "suggest a deity, a king, a judge or a spirit, and neither of them "
        "personifies money. THE SERVANT is about nineteen, slight and "
        "narrow-framed, smooth-faced with only the first light dark down of a "
        "beard on his jaw, warm olive-brown Middle Eastern skin and SHORT BLACK "
        "CURLING HAIR cropped close to the skull, wearing ONE knee-length "
        "hand-woven wool work tunic in DARK OLIVE hitched into ONE twisted "
        "cloth belt of CHARCOAL and nothing else, barefoot; he is plainly a "
        "much younger and much slighter man than the steward and shares no face "
        "with him. THE FIRST HOUSEHOLDER is about forty-five, spare and "
        "upright, with a full dark brown beard and dark brown hair to the nape, "
        "in ONE ankle-length wool tunic of DEEP INDIGO with ONE sash of "
        "charcoal. THE SECOND HOUSEHOLDER is about sixty, shorter and thicker "
        "set, with a wide grey beard and grey hair, in ONE ankle-length wool "
        "tunic of DARK UMBER with ONE sash of deep rust. NOT ONE OF THE THREE "
        "WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, WHITE OR ANY "
        "PALE CLOTH, and none of them wears a crown, a robe of state, "
        "jewellery, a chain or any metal ornament. There is no idol, no statue, "
        "no altar, no shrine, no heap of coins raised up, no scales of "
        "judgement and no symbolic object of any kind in the picture."
    ),
    "NEIGHBOURS": (
        "NEIGHBOURS LOCK: the ordinary village people in the application frames "
        "are first-century Judeans of that town, men and women together, from "
        "about eight to about seventy, all with warm sun-darkened olive-brown "
        "Middle Eastern skin, dark hair and dark eyes, and no two of them "
        "sharing a face. They are real people with dignity: worn, thin in the "
        "face where the narration calls for it, but upright, clean-limbed and "
        "human. EACH WEARS EXACTLY ONE OR TWO SEPARATE PIECES OF CLOTH AND "
        "NOTHING ELSE: one calf-length or ankle-length hand-woven wool tunic, "
        "faded, patched and mended with plainly visible stitching, and for some "
        "ONE rectangular wool mantle over the shoulders — and every piece is "
        "ONE SOLID DARK MUTED EARTH COLOUR: DARK UMBER, CHARCOAL, DEEP RUST, "
        "DARK OLIVE, DEEP INDIGO or DEEP MAROON, faded but never pale. NOT ONE "
        "OF THEM WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, "
        "KHAKI, WHITE OR PALE GREY CLOTH. Most are barefoot; a few have worn "
        "leather sandals. HEAD COVERING IS STATED POSITIVELY: where a woman "
        "covers her hair she does it with ONE FOLD OF HER OWN MANTLE drawn up "
        "over the head, in exactly the same dark colour as the rest of her "
        "cloth, and NOBODY IN THIS PICTURE WEARS A SEPARATE SCARF, VEIL, WRAP, "
        "SHAWL, TURBAN OR HEAD CLOTH OF ITS OWN, and least of all a pale one."
    ),
}

LOCKS.update({
    # ------------------------------------------------------------- places ----
    "ROOFTOP": (
        "ROOFTOP LOCK: this is the FLAT ROOF of an ordinary first-century "
        "Judean village house and it is stated positively. The roof itself is a "
        "deck of rough round timber poles with the bark still on them, crossed "
        "with brushwood and matting and finished with a thick layer of packed "
        "earth and lime plaster, worn, cracked and swept, warm pale tan "
        "underfoot, with a heavy STONE ROLLER lying at one edge for pressing it "
        "after rain. It is bounded by ONE low parapet of unmortared field "
        "limestone about knee high, and reached by an OUTSIDE STONE STAIR "
        "climbing the outer wall with no rail of any kind. On the roof lie the "
        "plain things of that household and nothing else: hand-woven reed mats, "
        "a hand-woven reed basket, one fired-clay water jar in the shade, a few "
        "flat cakes of figs drying on a mat, and a low pile of firewood. Beyond "
        "and below the parapet spread the FLAT ROOFS of the rest of the "
        "village, mud brick and dressed limestone plastered pale tan, with "
        "outside stairs climbing them, and beyond those the bare dry limestone "
        "hills. AGAINST THE SKY THERE IS ONLY FLAT ROOFLINE AND BARE HILL: no "
        "dome, minaret, bell tower, spire, clock, crenellation, pitched roof, "
        "roof tile, shingle, chimney, gable or half-timbering; no pole, mast, "
        "pylon, aerial, wire, cable or washing line; no railing, guardrail, "
        "balustrade, handrail or fence of any kind; no awning of striped, "
        "printed or synthetic cloth; no potted ornamental plant; and no "
        "lettering, numeral or sign anywhere."
    ),
    "ESTATE": (
        "ESTATE-YARD LOCK: the rich man's house is a well-off first-century "
        "JUDEAN farming estate built round a walled WORKING YARD, and it is a "
        "place of work, not a reception room. The yard is a wide floor of "
        "packed pale tan earth and worn limestone, swept in tracks by feet, "
        "enclosed by walls of dressed limestone blocks below and mud brick "
        "plastered pale tan above, with FLAT roofs of poles and packed earth "
        "and an outside stone stair climbing one wall. ONE wide GATEWAY of "
        "plain squared stone jambs and a plain flat stone lintel opens to the "
        "lane. EVERY OTHER OPENING IN THIS ESTATE IS A PLAIN RECTANGULAR GAP IN "
        "THE WALL CLOSED ONLY BY ONE HEAVY HANGING PANEL OF COARSE UNDYED "
        "GOAT-HAIR CLOTH IN NEAR-BLACK CHARCOAL AND DEEP UMBER, pushed against "
        "one jamb and knotted back on itself in a thick dark bundle, hung from "
        "ONE hewn timber pole — there is no door of any kind anywhere in this "
        "building, no hinge, no frame, no jamb of sawn timber, no batten, no "
        "latch, hasp, bolt, ring, handle or padlock, and NO HANGING, CURTAIN, "
        "DRAPE OR PANEL ANYWHERE IN THIS ESTATE IS CREAM, OFF-WHITE, IVORY, "
        "BUFF, BEIGE, PALE GOLD, LINEN-COLOURED OR ANY LIGHT TONE, and none is "
        "sheer, gathered, softly pleated, floor-pooling or hung on a rail. In "
        "the yard stand the plain hand-made things of that work: great "
        "fired-clay storage jars sunk to the shoulder in the shaded earth along "
        "one wall, hand-woven reed baskets, coarse dark goat-hair sacks, coils "
        "of twisted flax rope, a fired-clay water trough, ONE fig tree throwing "
        "hard shade in a corner, and a tethered donkey. THERE IS NO ARCH OF "
        "DRESSED VOUSSOIRS, no column with a carved capital, no pediment, no "
        "carved stone ornament, no glass in any opening, no tiled or pitched "
        "roof, no chimney, no metal gate, no wire, no chain and no lettering, "
        "numeral or sign anywhere on the building."
    ),
    "OIL-STORE": (
        "OIL-STORE LOCK: the oil store is a cool half-dark room off the estate "
        "yard, cut back into the thickness of the wall, its floor bare worn "
        "limestone and its ceiling three rough hewn timber beams with the adze "
        "marks still on them. Sunk into that floor to the shoulder stand GREAT "
        "FIRED-CLAY OIL JARS, plain unglazed terracotta, taller than a man's "
        "waist, wide-bellied and narrow-necked, their rims stained dark and "
        "greasy, each stopped with ONE flat disc of stone or ONE plug of folded "
        "cloth. Beside them lie hand-woven reed baskets, a shallow fired-clay "
        "dipping bowl on a cord, a hewn timber ladle and coils of twisted flax "
        "rope. THE ONLY LIGHT IS DAYLIGHT falling in through ONE plain "
        "rectangular opening in the wall, striking the floor and the flanks of "
        "the near jars and leaving the back of the room in honest darkness. "
        "THERE IS NO GLASS, no bottle, no barrel, no cask, no stave, no iron "
        "hoop, no vat of metal, no tap, spigot, valve, pipe, funnel or hose, no "
        "press of cast iron, no crate, no shelf of sawn boards, no hinged door, "
        "no latch, no printed or stencilled mark on any jar, and no lamp, "
        "candle or flame anywhere in this room."
    ),
    "GRAIN-BINS": (
        "GRAIN-BIN LOCK: the estate's grain is kept in the shade along the "
        "inner wall of its own working yard, and it is NOT a separate barn "
        "standing in a field. There are TWO squat rectangular bins of sun-dried "
        "MUD BRICK and undressed field stone, plastered over with mud and "
        "chopped straw and weathered to a pale tan, standing about chest high, "
        "each with ONE low square drawing hole near the ground that is simply "
        "an open dark square gap in the mud brick with nothing in it. Loose "
        "wheat lies heaped on a plastered earth floor in front of them, pale "
        "gold and countable grain by grain where the light strikes it, and it "
        "is moved in HAND-WOVEN REED BASKETS and coarse dark goat-hair SACKS "
        "standing open, with ONE hewn wooden scoop and ONE hand-woven winnowing "
        "basket lying on top of the heap. A GRAIN BIN HAS NO DOOR THAT SWINGS "
        "and no lid that lifts: no planked or boarded door, no vertical boards, "
        "no cross-batten, no frame, no jamb of sawn timber, no hinge, strap "
        "hinge, iron band, nail head, handle, ring, latch, hasp, bolt or "
        "padlock anywhere. THIS IS NOT MODERN, NOT AMERICAN AND NOT INDUSTRIAL: "
        "no metal or concrete silo, hopper, chute, auger or conveyor; no "
        "corrugated iron, tin or sheet metal; no sawn plank, board, batten, "
        "weatherboard, plywood or pallet; no red-painted or boarded barn, no "
        "pitched or gabled roof, no shingle, no hayloft; and no printed sack, "
        "label, stencil, lettering or numeral anywhere on anything."
    ),
    "VILLAGE-LANE": (
        "VILLAGE-LANE LOCK: the lane outside the estate is the level, sunlit "
        "way of a small first-century Judean village, and it is stated "
        "positively. Its floor is bare packed earth and worn limestone, dusty, "
        "rutted only by feet and hooves. On both sides stand plain house walls "
        "of mud brick and dressed limestone plastered pale tan, with FLAT roofs "
        "of poles and packed earth above them and outside stone stairs climbing "
        "to those roofs. EVERY OPENING IN EVERY WALL OF THIS VILLAGE IS SPANNED "
        "BY ONE PLAIN FLAT LINTEL — a single squared limestone block or one "
        "hewn timber beam laid straight across the top of a plain rectangular "
        "gap — so every doorway and window in the frame is a RECTANGLE, and not "
        "one opening anywhere is curved, rounded, vaulted or arched; each is "
        "closed only by ONE hanging panel of dark woven goat-hair cloth. Along "
        "the walls lie the plain things of that place: a fired-clay water jar "
        "on a doorstep, a hand-woven reed basket, a coil of twisted flax rope, "
        "a heap of swept dust, a tethered goat. THERE IS NOTHING BUILT OR "
        "FITTED THAT IS NOT STONE, MUD BRICK, TIMBER, CLAY OR CLOTH: no arch of "
        "dressed voussoirs, no carved capital, no dome, minaret, bell tower, "
        "spire, clock, crenellation, pitched roof, roof tile, shingle, chimney "
        "or gable; no cobbled setts or laid regular paving, no kerb, gutter, "
        "drain or grating; no pole, wire, cable, aerial, rail, gate, hinge or "
        "fitting of manufactured metal; no painted sign, notice, lettering or "
        "numeral anywhere; and no modern person, garment, footwear or object."
    ),
    "JUDEAN-LAND": (
        "JUDEAN-LAND LOCK: this is the dry limestone farming country of "
        "first-century JUDEA in the hot part of the year, and the land is "
        "stated positively. The ground is pale chalky limestone breaking "
        "through thin stony soil in bald shelves and slabs, with dry straw-gold "
        "grass, thistle, thorn scrub and dusty grey-green olive, fig and "
        "terebinth trees. Everything is in the colours of drought: bleached "
        "gold, straw, tan, pale ochre and dust grey. Low dry-stone terraces of "
        "unmortared limestone step down every slope. THE SKY BY DAY IS THE HARD "
        "CLEAR PALE BLUE OF A HOT DRY COUNTRY, whitening toward the horizon. "
        "THERE IS NO GREEN COUNTRYSIDE ANYWHERE IN THIS FRAME: no green grass, "
        "lawn, turf, meadow, pasture, moor, fell, upland, heather, bracken, "
        "clipped hedge, deciduous wood, oak, birch, pine forest, fern, ivy, "
        "rolling green hill or lush temperate valley, and no soft grey overcast "
        "northern sky. Nothing in this picture is Britain, Ireland, "
        "Scandinavia, the Alps or the American Midwest."
    ),
    "BILL-SHEET": (
        "BILL-SHEET LOCK: a debtor's bill in this build is ONE SINGLE LOOSE "
        "LEAF and never anything else — a rectangle of PAPYRUS about the size "
        "of two spread hands, its surface visibly fibrous with the horizontal "
        "and vertical strips of pith showing through, uneven, cream-brown, "
        "slightly cockled and curling at the corners, its edges cut rough or "
        "torn. It carries a few short lines of dark brown-black reed-pen "
        "strokes in Hebrew or Aramaic letters, irregular in size and spacing, "
        "the ink faded and uneven, sitting crooked on the sheet, with ONE "
        "figure standing alone at the foot of the writing — never printed, "
        "never typeset, never in even mechanical rows, never in modern arabic "
        "numerals and never any recognisable modern word. The other bills stand "
        "ROLLED into loose tubes or FOLDED in three in ONE hand-woven reed "
        "basket on the floor. The writing kit is ONE cut REED PEN with a split "
        "nib and ONE small shallow fired-clay pot of lamp-black ink standing on "
        "the floor beside the mat, with a scrap of dark cloth to wipe it."
    ),
})

BEATS = [
    # ========== s1 — Luke 16:1a, LUKE writing (light blue) ====================
    {
        "id": "v2-r036-b01", "out": "s01-he-said-unto-his-disciples.jpeg",
        "seg": "s1", "window": "0.000-3.598", "wide": True, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "And he said also unto his disciples,",
        "must_show": "Jesus sitting on a village rooftop in clear morning light, turning to the four men sitting with him as he begins to speak; the camera is behind the listeners and shoots past their backs.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, clear hard mid-morning sun coming in "
            "low and level from the LEFT across the roof deck, the sun itself "
            "well out of frame and NEVER behind any head, fine film grain, true "
            "depth of field. THE CAMERA STANDS BEHIND AND SLIGHTLY ABOVE THE "
            "SEATED LISTENERS AND SHOOTS PAST THEM: four dark-clad men fill the "
            "lower and left third of the frame as heads, shoulders and BACKS "
            "seen entirely FROM BEHIND, crouched and sitting on hand-woven reed "
            "mats and leaning in, and NOT ONE FACE IS TURNED TOWARD THE LENS. "
            "Jesus sits facing them on the far side, right of centre, on the "
            "low unmortared limestone parapet with one knee up, three-quarter "
            "length and three-quarter view; he has just turned his head to his "
            "own right toward the nearest man, and his gaze travels level and "
            "to the RIGHT and exits the picture through the RIGHT EDGE. His "
            "right hand rests open and low on his knee. THIS IS A WIDE "
            "FULL-LENGTH GROUP PHOTOGRAPH AND NOT A PORTRAIT: the camera is far "
            "enough back that all five men and the whole swept plaster roof "
            "deck are in frame together, with the flat rooftops of the village "
            "and the bare dry limestone hills falling away behind him. THE ONLY "
            "PALE WOOL IN THE WHOLE PICTURE IS HIS OWN ROBE; every other man is "
            "a solid dark saturated mass of indigo, umber, rust, olive, "
            "charcoal or maroon from edge to edge, in focus and out of focus "
            "alike."
        ),
    },
    # ========== j0 — Luke 16:1b, JESUS speaking (RED) =========================
    {
        "id": "v2-r036-b02", "out": "s02-a-certain-rich-man.jpeg",
        "seg": "j0", "window": "3.598-6.470", "wide": True, "jesus": False,
        "locks": _YARD + ["MASTER", "STEWARD"], "char_refs": _BOTH,
        "narration": "There was a certain rich man, which had a steward;",
        "must_show": "The rich man standing in the middle of his own walled working yard in late-morning sun, the steward a pace behind and to one side of him with a rolled papyrus sheet in his soft hand; the camera is behind and to the right of both men.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear late-morning sun coming in "
            "high and from the LEFT, throwing short black shadows across the "
            "packed earth, the sun well out of frame and never behind any head, "
            "fine film grain. THE CAMERA STANDS INSIDE THE YARD BEHIND AND TO "
            "THE RIGHT OF BOTH MEN AND SHOOTS PAST THEM toward the sunken oil "
            "jars along the far wall: the master is centre frame seen in "
            "three-quarter FROM BEHIND, full length, only the back and side of "
            "his head in view, his dark umber mantle across his shoulders over "
            "his deep maroon tunic, his face turned away from the camera. "
            "BECAUSE THE CAMERA IS BEHIND HIS HEAD, HIS HAIR IS THE THING THE "
            "VIEWER SEES OF HIM AND IT IS STATED HERE: thick iron-grey hair "
            "waving back off a broad crown and curling onto the nape of his "
            "neck and the top of his mantle — never a bare, bald, shaven, "
            "cropped or thinning head, and he wears nothing on it. One pace "
            "behind him and to the LEFT stands the steward, a head shorter and "
            "far slighter, in profile to the camera and turned toward the "
            "master, his dark brown hair pushed back off his forehead and his "
            "short neat beard clear against the pale plastered wall, ONE loose "
            "leaf of papyrus rolled into a tube held low in his soft "
            "long-fingered hand. NOT ONE FACE IS TURNED TOWARD THE LENS. THIS "
            "IS A WIDE FULL-LENGTH SCENE: the camera is far enough back that "
            "both men are visible head to sandals, with the fig tree's hard "
            "shade in the corner and the tethered donkey by the gateway."
        ),
    },
    {
        "id": "v2-r036-b03", "out": "s03-accused-of-wasting.jpeg",
        "seg": "j0", "window": "6.470-10.906", "wide": True, "jesus": False,
        "locks": _YARD + ["MASTER", "STEWARD", "NEIGHBOURS"], "char_refs": _BOTH,
        "narration": "and the same was accused unto him that he had wasted his goods.",
        "must_show": "A household worker leaning close to the master's ear in the shade of the estate gateway and telling him something, the master's face going still and hard; far off across the sunlit yard the steward is at work with his back to them and has not noticed.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT
        + "nobody points a finger at anyone, nobody shouts, nobody is struck, seized or dragged, and no crowd gathers to accuse; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, hard clear late-morning sun outside and "
            "deep dry shade under the flat stone lintel of the gateway, the "
            "light coming from the LEFT and never behind any head, fine film "
            "grain, true depth of field. THE CAMERA STANDS IN THE YARD TO THE "
            "SIDE OF THE TWO MEN AND SLIGHTLY BEHIND THE SPEAKER: in the near "
            "LEFT foreground, sharp, a lean dark-umber-clad household worker is "
            "seen from behind and in three-quarter, stooping in to the master's "
            "ear with one hand half-raised beside his mouth, his own face "
            "hidden from the lens by the back of his head. The master stands "
            "facing him in strict side-on profile at centre right, "
            "three-quarter length, his iron-grey beard and iron-grey hair clear "
            "against the sunlit wall beyond, his one visible eye looking down "
            "and away to the RIGHT at the ground and exiting the picture "
            "through the RIGHT EDGE, the far cheek and far eye completely "
            "hidden behind the bridge of his nose. His face is not anger and "
            "not shock: it is a man going very still while he takes something "
            "in, the jaw set, the brows level. Far off across the bright yard, "
            "small, sharp-edged and unaware, the steward stands with his BACK "
            "to them beside the sunken oil jars, his dark olive tunic and "
            "charcoal mantle unmistakable and a clear band of dark brown hair "
            "showing at the back of his head. NOT ONE FACE IS TURNED TOWARD THE "
            "LENS. THIS IS A WIDE FULL-LENGTH SCENE: the camera is far enough "
            "back that all three men are visible head to sandals within the "
            "yard."
        ),
    },
    # ========== n1 — the manager who ran everything ===========================
    {
        "id": "v2-r036-b04", "out": "s04-the-manager-who-ran-it-all.jpeg",
        "seg": "n1", "window": "10.906-15.820", "wide": True, "jesus": False,
        "locks": _YARD + ["STEWARD", "NEIGHBOURS"], "char_refs": _STEW,
        "narration": "Jesus told a story about a rich man and the manager who ran everything he owned.",
        "must_show": "The steward in the middle of running the estate: standing over the sunken oil jars with a loose papyrus sheet in one hand, the other hand out and level, directing two workers who are carrying a heavy sack between them.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear late-morning sun from the "
            "LEFT laying short black shadows across the packed earth, the sun "
            "well out of frame and never behind any head, fine film grain. THE "
            "CAMERA STANDS BEHIND AND ABOVE THE TWO WORKERS AND SHOOTS PAST "
            "THEM toward the steward: in the near lower LEFT, large and softly "
            "out of focus, the backs of two dark-clad men bent under a coarse "
            "dark goat-hair sack slung between them on a pole, their heads and "
            "shoulders seen entirely FROM BEHIND. The steward stands beyond "
            "them, sharp, three-quarter length and in three-quarter view turned "
            "to his own left, one foot up on the shoulder of a sunken oil jar; "
            "ONE loose leaf of papyrus, rolled half open, is held in his left "
            "hand at his chest and his right hand is out flat and level, "
            "pointing the sack along toward the store. His gaze runs down the "
            "line of his own arm to the LEFT and exits the picture through the "
            "LEFT EDGE. His face is brisk and unbothered, a man in charge of an "
            "ordinary morning, and his soft long-fingered hands are clearly "
            "readable against the coarse fabric and rough clay. THIS IS A WIDE "
            "FULL-LENGTH SCENE: the camera is far enough back that the steward "
            "is visible head to sandals with the row of sunken jars, the fig "
            "tree's shade and the pale plastered wall of the estate behind him. "
            "NOT ONE FACE IS TURNED TOWARD THE LENS."
        ),
    },
    {
        # ANCHOR BEAT — MASTER. Generated in the anchor run before every other
        # beat, so the REFS cache cannot make this picture reference itself. No
        # char_refs and nobody else in the frame.
        "id": "v2-r036-b05", "out": "s05-word-came-to-the-rich-man.jpeg",
        "seg": "n1", "window": "15.820-20.709", "wide": False, "jesus": False,
        "locks": ["ESTATE", "MASTER", "ESTATE-ACCOUNTS", "BILL-SHEET"],
        "narration": "Word came to the rich man that this manager had been wasting his goods.",
        "must_show": "The rich man standing alone in the shade of his own yard holding ONE loose papyrus bill sheet open in both hands and reading it, his face clearly visible in strict side-on profile, taking in what it says.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, hard clear late-morning daylight coming "
            "in almost level from the LEFT through the open gateway and "
            "modelling the face from the front, fine film grain, shallow but "
            "honest depth of field. THIS IS A STRICT SIDE-ON PROFILE AND THE "
            "CAMERA SITS EXACTLY ON HIS LEFT: the master stands three-quarter "
            "length at the RIGHT of the frame turned fully to the LEFT, so the "
            "viewer sees ONE cheek, ONE eye, ONE ear and the clean outline of "
            "brow, nose, lips and full iron-grey beard against the pale "
            "plastered wall beyond. THE FAR CHEEK AND THE FAR EYE ARE "
            "COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF "
            "HIS HEAD and cannot be seen at all; his one visible eye looks down "
            "and to the LEFT at the sheet in his hands and exits the picture "
            "through the LEFT EDGE, so his pupils are nowhere near the lens. "
            "His face is not rage and not grief: the brows are drawn a little "
            "down and level and the mouth has gone flat, the look of a man "
            "reading something he already half suspected. He holds ONE single "
            "loose leaf of fibrous cream-brown papyrus open flat between both "
            "broad hands at chest height, its rough torn edge catching the "
            "light and its few crooked reed-pen lines of Hebrew letters faintly "
            "readable across it. His deep maroon tunic, dark umber shoulder "
            "mantle and deep indigo waist sash are all clearly readable, and "
            "his thick iron-grey hair waves back off the crown and onto the "
            "nape. HE IS THE ONLY PERSON IN THE PICTURE. Across the lower "
            "third, close to the camera and softly out of focus, runs the dark "
            "shoulder of a sunken fired-clay oil jar."
        ),
    },
]

BEATS += [
    # ========== n2 — the summons and the dismissal ============================
    {
        "id": "v2-r036-b06", "out": "s06-so-he-called-him-in.jpeg",
        "seg": "n2", "window": "20.709-23.240", "wide": False, "jesus": False,
        "locks": _YARD + ["MASTER", "STEWARD"], "char_refs": _BOTH,
        "narration": "So he called the manager in and said,",
        "must_show": "The steward crossing the sunlit yard toward the shaded opening where the master waits for him, seen from behind the steward, the master's dark shape standing square in the gap in the wall.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 50mm lens, hard clear midday sun on the yard and "
            "deep dry shade in the opening beyond, the light from the LEFT and "
            "never behind any head, fine film grain, true depth of field. THE "
            "CAMERA STANDS DIRECTLY BEHIND THE STEWARD AND SHOOTS OVER HIS "
            "SHOULDER: he fills the near RIGHT of the frame from the waist up, "
            "seen ENTIRELY FROM BEHIND and slightly from above, walking away "
            "from the camera into the picture — the charcoal mantle across his "
            "back and shoulders, and the back of his head sharp and close so "
            "that his THICK DARK BROWN HAIR, straight and pushed back off the "
            "crown and cut to just below the ears, is the clearest thing in the "
            "frame, never bare, bald, shaven or thinning. Ahead of him, six "
            "paces off and smaller, the master stands square in the plain "
            "rectangular gap in the wall with the heavy near-black goat-hair "
            "hanging knotted back against the far jamb beside him, his face in "
            "shadow and turned down toward the approaching man, his weight even "
            "on both feet and his hands loose at his sides. NOT ONE FACE IS "
            "TURNED TOWARD THE LENS. The whole picture is quiet and ordinary "
            "and slightly too still, the tension carried by the distance "
            "between the two men and by the black shade in the opening, never "
            "by a raised hand or a shout."
        ),
    },
    {
        "id": "v2-r036-b07", "out": "s07-give-an-account.jpeg",
        "seg": "n2", "window": "23.240-27.600", "wide": True, "jesus": False,
        "locks": _YARD + ["MASTER", "STEWARD", "ESTATE-ACCOUNTS", "BILL-SHEET"],
        "char_refs": _BOTH,
        "narration": "give an account of your work, because you cannot be my manager any longer.",
        "must_show": "The master facing the steward across the hand-woven reed basket of rolled bills standing on the floor between them, one broad hand held out low and open toward it, telling him he is finished; the steward standing very straight and still.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_NIGHT
        + "nobody shouts, points a finger, raises a fist, seizes, pushes or strikes anyone; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear midday daylight falling in "
            "through ONE plain rectangular opening from the LEFT onto the "
            "flagstone floor between the two men, the sun out of frame and "
            "never behind any head, fine film grain, true depth of field. THE "
            "CAMERA STANDS BEHIND AND TO THE LEFT OF THE STEWARD AND SHOOTS "
            "PAST HIM: the steward is in the near LEFT foreground seen in "
            "three-quarter FROM BEHIND, full length, standing very straight "
            "with his arms down at his sides and his hands open and empty, only "
            "the back and side of his head in view, his thick dark brown hair "
            "clear at the crown, the temple and the nape and his charcoal "
            "mantle down his back over his dark olive tunic; his face is NOT "
            "visible to the camera. The master faces him across the room at "
            "centre right, full length and in three-quarter view, his weight "
            "square, his left hand held out low and open, palm down, toward the "
            "HAND-WOVEN REED BASKET on the floor between them in which a dozen "
            "loose papyrus leaves stand ROLLED into loose tubes and FOLDED in "
            "three; his gaze goes down to that basket and exits the picture "
            "through the LOWER LEFT. His face is level and finished, not "
            "shouting. THIS IS A WIDE FULL-LENGTH SCENE: the camera is far "
            "enough back that both men and the whole bare plastered room are in "
            "frame, its ceiling on three rough hewn beams, its floor worn "
            "flagstone with one dark woven wool mat, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS."
        ),
    },
    {
        "id": "v2-r036-b08", "out": "s08-about-to-lose-everything.jpeg",
        "seg": "n2", "window": "27.600-32.289", "wide": False, "jesus": False,
        "locks": ["ESTATE", "STEWARD", "JUDEAN-LAND"], "char_refs": _STEW,
        "narration": "Just like that, the man was about to lose his job and his home.",
        "must_show": "The steward standing alone in the estate gateway looking out at the lane, his empty hands hanging at his sides, the whole yard he used to run behind him.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face anywhere in this frame; nobody weeps, kneels, covers the face or tears their clothing; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, hard clear midday sun outside the "
            "gateway and dry shade under its flat stone lintel, the light "
            "raking in from the LEFT and never behind his head, fine film "
            "grain, true depth of field. THE CAMERA STANDS INSIDE THE YARD "
            "BEHIND AND BELOW HIM AND SHOOTS PAST HIM out through the gateway: "
            "the steward is centre frame, full length, seen ENTIRELY FROM "
            "BEHIND as a dark upright shape against the glare of the lane, his "
            "charcoal mantle hanging straight down his back over the dark olive "
            "tunic, his arms down and his soft long-fingered hands open and "
            "EMPTY at his sides, one sandal half-turned as if he stopped "
            "mid-stride. BECAUSE THE CAMERA IS BEHIND HIS HEAD, HIS HAIR IS THE "
            "THING THE VIEWER SEES OF HIM AND IT IS STATED HERE: thick dark "
            "brown hair, straight, pushed back off the crown and cut to just "
            "below the ears, showing clearly at the crown, the temples and the "
            "nape, never bare, bald, shaven, cropped or thinning, with nothing "
            "worn on it. HIS FACE IS NOT VISIBLE AT ALL. The plain squared "
            "stone jambs and flat lintel of the gateway frame him and the "
            "bright dusty lane and the bare dry limestone hills beyond. There "
            "is no bright rim, edge or outline anywhere around his head, hair "
            "or shoulders: he is simply a dark shape in shade against a bright "
            "opening, and the light in the lane stays out in the lane."
        ),
    },
    # ==== j3 — Luke 16:3, the STEWARD speaking INSIDE the parable (RED) =======
    {
        # ANCHOR BEAT — STEWARD. Generated in the anchor run before every other
        # beat. No char_refs and nobody else in the frame.
        "id": "v2-r036-b09", "out": "s09-what-shall-i-do.jpeg",
        "seg": "j3", "window": "32.289-36.320", "wide": False, "jesus": False,
        "locks": ["ESTATE", "STEWARD"],
        "narration": "What shall I do? for my lord taketh away from me the stewardship:",
        "must_show": "The steward alone with his back against the estate wall, working out what to do, his face clearly visible in strict side-on profile, one hand pressed against his own mouth.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_CREAM + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face anywhere in this frame; nobody weeps, kneels, prays, raises the eyes to the sky or lifts the hands; no thick fluffy furry felted fleeced brushed napped tufted looped or blanket-like cloth on his shoulder or anywhere in the frame, and no raised pile, sheepskin, shearling or knitted texture on any garment; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, hard clear midday daylight coming in "
            "almost level from the LEFT and modelling the face from the front, "
            "fine film grain, shallow but honest depth of field. THIS IS A "
            "STRICT SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS LEFT: "
            "the steward stands half-length at the RIGHT of the frame with his "
            "shoulder blades against the pale plastered wall, turned fully to "
            "the LEFT, so the viewer sees ONE cheek, ONE eye, ONE ear and the "
            "clean outline of brow, nose, lips and short neat dark brown beard "
            "against the wall beyond. THE FAR CHEEK AND THE FAR EYE ARE "
            "COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF "
            "HIS HEAD and cannot be seen at all; his one visible eye is wide "
            "and moving, fixed on nothing, aimed level and to the LEFT and "
            "exiting the picture through the LEFT EDGE, so his pupils are "
            "nowhere near the lens. His face is real fear working itself into "
            "calculation: the brows up and drawn together, the jaw tight, the "
            "breath held. The knuckles of his SOFT LONG-FINGERED, SMOOTH-PALMED "
            "hand are pressed hard against his own mouth, the fingers clean and "
            "unmarked with faint lamp-black ink stains on two fingertips, and "
            "the difference between that hand and a labourer's is plainly "
            "visible. His dark olive tunic, charcoal shoulder mantle and deep "
            "rust waist sash are clearly readable, and his thick dark brown "
            "hair is pushed back off the forehead and cut to just below the "
            "ear. HE IS THE ONLY PERSON IN THE PICTURE. Across the bottom "
            "third, close to the camera and softly out of focus, runs the "
            "charcoal mantle where it has slipped off the shoulder — FLAT, "
            "THIN and MATTE with a plainly visible over-and-under grid of warp "
            "and weft threads and a frayed selvedge, never fluffy, felted, "
            "fleeced, brushed, napped, tufted or blanket-like."
        ),
    },
    {
        "id": "v2-r036-b10", "out": "s10-i-cannot-dig.jpeg",
        "seg": "j3", "window": "36.320-40.249", "wide": False, "jesus": False,
        "locks": ["ESTATE", "STEWARD", "HAND-TOOLS"], "char_refs": _STEW,
        "narration": "I cannot dig; to beg I am ashamed.",
        "must_show": "A close view of the steward's own two soft unmarked hands turned palm up in front of him, with a heavy hand-forged mattock standing against the wall just behind them, and the lower half of his face above.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_CREAM + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face anywhere in this frame; no begging bowl, no alms, no coin given, no crowd; " + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, hard clear midday daylight "
            "coming in almost level from the LEFT, fine film grain, shallow but "
            "honest depth of field. THE CAMERA IS CLOSE IN AND SET LOW AND TO "
            "HIS LEFT, LOOKING SLIGHTLY UP: his TWO OPEN HANDS fill the middle "
            "of the frame, held out and turned palm up in front of his own "
            "chest — adult MALE hands at true human scale, correctly "
            "proportioned, five fingers on each, long-fingered, smooth-palmed, "
            "clean-nailed and completely unmarked by work, with faint "
            "lamp-black ink stains on two fingertips. Above them, cut by the "
            "top of the frame, only the lower half of his face is visible in "
            "strict side-on profile turned to the LEFT — the short neat dark "
            "brown beard, the flat mouth and the underside of the jaw — and NO "
            "EYE IS VISIBLE IN THIS PICTURE AT ALL. The straight sleeve of his "
            "dark olive tunic runs across the lower left corner close to the "
            "camera, and it reads unmistakably as COARSE HAND-WOVEN WOOL, a "
            "visible slightly irregular over-and-under grid of warp and weft "
            "threads with a flat matte surface and a frayed selvedge hem, never "
            "as knitwear, jersey, rib or fleece. Just behind his hands, leaning "
            "against the pale plastered wall and softly out of focus, stands "
            "ONE MATTOCK: a straight rough-hewn unpainted wooden haft about an "
            "arm and a half long with a single heavy hand-forged iron blade "
            "wedged onto its head at an angle, the iron dark grey, uneven, "
            "pitted and showing hammer marks, its working edge bright and worn "
            "thin. The whole picture is the comparison between those hands and "
            "that tool, and nothing else."
        ),
    },
]

BEATS += [
    # ========== n3 — the panic ================================================
    {
        "id": "v2-r036-b11", "out": "s11-the-manager-panicked.jpeg",
        "seg": "n3", "window": "40.249-43.480", "wide": False, "jesus": False,
        "locks": ["ESTATE", "STEWARD"], "char_refs": _STEW,
        "narration": "And the manager panicked.",
        "must_show": "The steward mid-stride pacing along the shaded wall of the yard, his head down and one hand dragging through his hair, caught in movement rather than posed.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_CREAM + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face anywhere in this frame; nobody weeps, kneels, prays or raises the eyes to the sky; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, hard clear midday sun striking the "
            "packed earth beyond and dry reflected shade on the wall he is "
            "pacing along, the light from the LEFT and never behind his head, "
            "fine film grain, a hint of honest motion blur at the trailing "
            "hand. THE CAMERA SITS ON HIS LEFT AND SLIGHTLY AHEAD OF HIM: the "
            "steward is three-quarter length at centre left, caught MID-STRIDE "
            "walking fast to the LEFT ACROSS THE FRAME, his weight forward on "
            "the leading foot and the trailing sandal still off the ground, his "
            "charcoal mantle swinging out behind him. He is seen in strict "
            "side-on profile with his head DOWN, so the viewer sees ONE cheek, "
            "ONE eye and the outline of brow, nose and short beard, THE FAR "
            "CHEEK AND FAR EYE COMPLETELY HIDDEN behind the bridge of his nose; "
            "his one visible eye is aimed DOWN at the ground a pace in front of "
            "him and exits the picture through the LOWER LEFT EDGE, so his "
            "pupils are nowhere near the lens. His right hand is dragging back "
            "through his own thick dark brown hair, pushing it up off the "
            "forehead — the hair is plainly there, thick, straight and cut to "
            "just below the ear, never bare, bald, shaven or thinning. His face "
            "is fright, not despair: mouth open a little on a short breath, "
            "brows up, eyes moving. He is the only person in the picture."
        ),
    },
    {
        "id": "v2-r036-b12", "out": "s12-not-strong-enough-to-dig.jpeg",
        "seg": "n3", "window": "43.480-46.920", "wide": True, "jesus": False,
        "locks": ["ESTATE", "STEWARD", "JUDEAN-LAND", "HAND-TOOLS", "NEIGHBOURS"],
        "char_refs": _STEW,
        "narration": "I am not strong enough to dig ditches, he thought, and I am too ashamed to beg.",
        "must_show": "Seen past the steward's shoulder as he stands at the estate wall looking out: below him a labourer swings a mattock in a stony terrace, and further along the way an old man sits on the ground at the roadside with his hands open in his lap.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_MOCK + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear early-afternoon sun from the "
            "LEFT with the shadows beginning to lengthen, the sun well out of "
            "frame and never behind any head, fine film grain, true depth of "
            "field. THE CAMERA STANDS BEHIND THE STEWARD'S RIGHT SHOULDER AND "
            "SHOOTS PAST HIM out over the low unmortared limestone wall: he "
            "fills the near RIGHT of the frame from the waist up, seen ENTIRELY "
            "FROM BEHIND and softly out of focus, his charcoal mantle across "
            "his back and the back of his head sharp enough to show THICK DARK "
            "BROWN HAIR, straight, pushed back off the crown and cut to just "
            "below the ears, never bare, bald, shaven or thinning, with nothing "
            "worn on it; his face is NOT visible. Beyond him and below, sharp "
            "in the middle distance, ONE labourer stands to his waist in a "
            "half-cut ditch on a stony terrace, seen from the side and caught "
            "mid-swing with ONE MATTOCK — a rough-hewn unpainted wooden haft "
            "and a single heavy hand-forged iron blade, dark grey, pitted and "
            "hammer-marked — his back and arms hard with work, his face turned "
            "away down the line of his own swing. Further along the same dusty "
            "way, smaller and to the LEFT, ONE old man sits on the bare ground "
            "with his back to a dry-stone wall, upright and composed, his two "
            "open hands resting in his lap and his head turned away toward the "
            "hills; he is worn and thin but not filthy, not ragged to indecency "
            "and not pitiable. THIS IS A WIDE FULL-LENGTH SCENE and NOT ONE "
            "FACE IS TURNED TOWARD THE LENS."
        ),
    },
    {
        "id": "v2-r036-b13", "out": "s13-he-had-to-act-right-now.jpeg",
        "seg": "n3", "window": "46.920-51.933", "wide": False, "jesus": False,
        "locks": _ACCTS + ["BILL-SHEET"], "char_refs": _STEW,
        "narration": "He had to think fast, and he had to act right now, before the news got out.",
        "must_show": "The steward dropping to one knee in the shaded accounts corner and snatching up the hand-woven reed basket of rolled bills off the floor mat, moving fast.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, hard clear early-afternoon daylight "
            "falling in from the LEFT through ONE plain rectangular opening and "
            "striking the floor mat and the basket, the back of the recess in "
            "honest darkness, the sun out of frame and never behind his head, "
            "fine film grain, a hint of honest motion blur at his moving hand. "
            "THE CAMERA IS LOW, DOWN AT FLOOR LEVEL AND TO HIS LEFT: the "
            "steward is three-quarter length at centre right, dropped onto his "
            "left knee on a dark hand-woven wool mat and already rising, caught "
            "MID-ACTION with both hands closing round the rim of ONE hand-woven "
            "reed basket standing on the floor, in which a dozen loose papyrus "
            "leaves stand ROLLED into loose tubes and FOLDED in three, their "
            "rough torn edges and fibrous cream-brown surfaces catching the "
            "light. Beside the mat on the bare floor stand ONE small shallow "
            "fired-clay pot of lamp-black ink and ONE cut reed pen with a split "
            "nib. He is seen in strict side-on profile turned to the LEFT — ONE "
            "cheek, ONE eye, ONE ear, THE FAR CHEEK AND FAR EYE COMPLETELY "
            "HIDDEN behind the bridge of his nose — and his one visible eye is "
            "already aimed out to the LEFT toward the gateway, exiting the "
            "picture through the LEFT EDGE, so his pupils are nowhere near the "
            "lens. His face is hurry and hard concentration, not glee. His "
            "thick dark brown hair, his short neat beard, his dark olive tunic, "
            "charcoal mantle and deep rust sash are all clearly readable. HE IS "
            "THE ONLY PERSON IN THE PICTURE."
        ),
    },
    # ========== n4 — the debtors called in ====================================
    {
        "id": "v2-r036-b14", "out": "s14-he-called-in-the-debtors.jpeg",
        "seg": "n4", "window": "51.933-56.640", "wide": True, "jesus": False,
        "locks": _YARD + ["STEWARD", "OIL-DEBTOR", "WHEAT-DEBTOR"], "char_refs": _STEW,
        "narration": "So while he still could, he quickly called in every person who owed his employer money,",
        "must_show": "Two farmers coming in through the estate gateway out of the bright lane, the short thickset olive farmer first and the very tall grain farmer behind him, while the steward waits inside the yard with one hand raised to bring them on.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_FORCE + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear early-afternoon sun blazing "
            "in the lane beyond the gateway and dry shade inside the yard, the "
            "light from the LEFT and never behind any head, fine film grain, "
            "true depth of field. THE CAMERA STANDS INSIDE THE YARD BEHIND AND "
            "TO THE RIGHT OF THE STEWARD AND SHOOTS PAST HIM toward the "
            "gateway: the steward is in the near RIGHT foreground seen in "
            "three-quarter FROM BEHIND, three-quarter length, his charcoal "
            "mantle down his back and his thick dark brown hair clear at the "
            "crown and nape, his right hand raised only to shoulder height and "
            "turned palm inward, beckoning them on; his face is NOT visible to "
            "the camera. Coming through the bright rectangle of the gateway, "
            "sharp in the middle distance and both seen from the SIDE as they "
            "walk LEFT ACROSS THE FRAME, are EXACTLY TWO MEN AND NO MORE: first "
            "a short thickset bandy-legged farmer of about forty-five in a "
            "faded patched DEEP RUST work tunic and dark umber belt, his short "
            "bushy black-and-grey beard and short cropped black hair plain, his "
            "cracked stained hands swinging; behind him a very tall "
            "heavy-shouldered man of about thirty in a DARK UMBER work tunic "
            "hitched into a dark olive belt, stooping his head under the flat "
            "stone lintel, his full black beard and thick black curling hair to "
            "the middle of the neck plain. NOT ONE FACE IS TURNED TOWARD THE "
            "LENS. THIS IS A WIDE FULL-LENGTH SCENE: the camera is far enough "
            "back that all three men are visible head to sandals."
        ),
    },
    {
        "id": "v2-r036-b15", "out": "s15-one-after-another.jpeg",
        "seg": "n4", "window": "56.640-61.554", "wide": True, "jesus": False,
        "locks": _YARD + ["STEWARD", "OIL-DEBTOR", "WHEAT-DEBTOR"], "char_refs": _STEW,
        "narration": "one after another, to make himself some friends before it was too late.",
        "must_show": "The two farmers waiting apart in the shade against the yard wall while the steward stoops in the shaded accounts corner and turns to beckon the first of them over.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_FORCE + _NO_OFFICE + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear early-afternoon sun laying a "
            "long bright slab of light across the yard from the LEFT with the "
            "two waiting men standing back in dry shade, the sun out of frame "
            "and never behind any head, fine film grain, true depth of field. "
            "THE CAMERA STANDS OUT IN THE YARD BEHIND THE TWO WAITING MEN AND "
            "SHOOTS PAST THEM toward the shaded recess: the tall grain farmer "
            "and the short olive farmer stand apart from one another in the "
            "near LEFT foreground, both seen in three-quarter FROM BEHIND, full "
            "length, dark masses of umber and rust against the sunlit floor, "
            "the tall man's black curls and the short man's cropped grey-shot "
            "black hair clear at the backs of their heads, neither face visible "
            "to the camera. Beyond them, sharp and smaller, the steward is "
            "crouched on one knee at the mat in the recess with the reed basket "
            "of rolled papyrus leaves beside him, twisted round at the waist to "
            "look back at them and lifting one open hand to call the nearer man "
            "over; he is in three-quarter view, his one visible eye aimed to "
            "the LEFT past the camera at the waiting men and exiting the "
            "picture through the LEFT EDGE. His face is businesslike and "
            "hurried, not smiling and not sly. NOT ONE FACE IS TURNED TOWARD "
            "THE LENS. THIS IS A WIDE FULL-LENGTH SCENE: the camera is far "
            "enough back that all three men are visible head to sandals within "
            "the yard, with the sunken oil jars and the mud-brick grain bins "
            "along the wall behind them."
        ),
    },
    # ==== j6 — Luke 16:6b, the STEWARD speaking INSIDE the parable (RED) ======
    {
        "id": "v2-r036-b16", "out": "s16-take-thy-bill-write-fifty.jpeg",
        "seg": "j6", "window": "61.554-65.570", "wide": False, "jesus": False,
        "locks": _ACCTS + ["BILL-SHEET", "OIL-DEBTOR"], "char_refs": _STEW,
        "narration": "Take thy bill, and sit down quickly, and write fifty.",
        "must_show": "The steward pushing ONE loose papyrus sheet and a cut reed pen across the floor mat into the olive farmer's cracked hands, both men sitting down on the floor, the clay ink pot between them.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 50mm lens, hard clear afternoon daylight falling "
            "in from the LEFT through ONE plain rectangular opening onto the "
            "mat, the pale sheet and the two pairs of hands, the back of the "
            "recess in honest darkness, the sun out of frame and never behind "
            "any head, fine film grain, true depth of field. THE CAMERA IS DOWN "
            "AT FLOOR LEVEL AND SET BETWEEN THE TWO MEN AND SLIGHTLY BEHIND THE "
            "FARMER: the short thickset olive farmer is in the near LEFT "
            "foreground, seen in three-quarter FROM BEHIND, sitting straight "
            "down on the bare floor with his knees up, his DEEP RUST patched "
            "tunic filling the lower left third, the back of his head sharp "
            "enough to show his SHORT CROPPED BLACK HAIR GREYING AT THE "
            "TEMPLES, his face NOT visible to the camera, both his broad "
            "cracked green-black-stained hands coming forward to take what is "
            "offered. Facing him across the dark hand-woven wool mat the "
            "steward sits back on his heels in strict side-on profile turned to "
            "the LEFT — ONE cheek, ONE eye, ONE ear, THE FAR CHEEK AND FAR EYE "
            "COMPLETELY HIDDEN behind the bridge of his nose — his one visible "
            "eye aimed down and LEFT at the farmer's hands and exiting through "
            "the LEFT EDGE. He is pushing ONE SINGLE LOOSE LEAF of fibrous "
            "cream-brown papyrus, unrolled flat and carrying a few crooked "
            "reed-pen lines of Hebrew letters, across the mat with one soft "
            "hand, and holding out ONE cut reed pen with a split nib in the "
            "other. ONE small shallow fired-clay pot of lamp-black ink stands "
            "open on the mat between them and ONE hand-woven reed basket of "
            "other rolled leaves stands behind his knee. His face is urgency "
            "and pressure, mouth open on the word 'quickly', NOT a smile, NOT a "
            "wink and NOT a shared joke."
        ),
    },
]

BEATS += [
    # ========== n5 — the oil bill =============================================
    {
        "id": "v2-r036-b17", "out": "s17-how-much-do-you-owe.jpeg",
        "seg": "n5", "window": "65.570-70.500", "wide": True, "jesus": False,
        "locks": ["OIL-STORE", "STEWARD", "OIL-DEBTOR", "ESTATE-ACCOUNTS", "BILL-SHEET"],
        "char_refs": _STEW,
        "narration": "How much do you owe? he asked the first man. A hundred jugs of olive oil.",
        "must_show": "The two men standing among the great sunken oil jars in the cool half-dark store, the olive farmer with one hand laid flat on a jar rim as he says how much, the steward listening with the loose sheet in his hand.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_NIGHT + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "One photograph, 35mm lens, ONE shaft of hard clear afternoon "
            "daylight coming in from the LEFT through a plain rectangular "
            "opening and striking the floor and the flanks of the two nearest "
            "jars, the back of the room falling away into honest darkness, the "
            "sun out of frame and never behind any head, fine film grain, true "
            "depth of field. THE CAMERA STANDS BACK IN THE DARK BEHIND AND "
            "BETWEEN THE TWO MEN AND SHOOTS PAST THEM toward the light: both "
            "are seen in three-quarter FROM BEHIND, full length, dark shapes "
            "with the daylight on their far sides, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. On the LEFT the short thickset olive farmer "
            "stands with one broad cracked hand laid flat on the wide rim of a "
            "great sunken fired-clay jar and the other hand lifted a little, "
            "his cropped grey-shot black hair clear at the back of his head, "
            "his head turned away toward the steward. On the RIGHT and half a "
            "pace nearer the camera the steward stands taller and far "
            "slighter, the back of his head showing thick straight dark brown "
            "hair pushed off the crown, ONE loose leaf of fibrous cream-brown "
            "papyrus held half-rolled low in his soft hand. THIS IS A WIDE "
            "FULL-LENGTH SCENE: the camera is far enough back that both men are "
            "visible head to sandals with the whole row of great jars sunk to "
            "the shoulder in the floor around them, their rims stained dark and "
            "greasy, each stopped with a flat stone disc or a plug of folded "
            "cloth."
        ),
    },
    {
        "id": "v2-r036-b18", "out": "s18-write-down-fifty.jpeg",
        "seg": "n5", "window": "70.500-73.920", "wide": False, "jesus": False,
        "locks": ["ESTATE-ACCOUNTS", "BILL-SHEET", "OIL-DEBTOR"],
        "narration": "Quick, said the manager, take your bill and write down fifty.",
        "must_show": "A very close view of the olive farmer's own cracked stained hand holding a cut reed pen and writing one short line of Hebrew letters at the foot of ONE loose papyrus sheet resting across his knee.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_NIGHT
        + "no face, head, eye or shoulder is visible anywhere in this frame; no printed or typeset lettering, no ruled line, no column, no modern arabic numeral and no recognisable modern word on the sheet; " + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, hard clear afternoon daylight "
            "raking in from the LEFT across the sheet, fine film grain, very "
            "shallow but honest depth of field. THE CAMERA IS RIGHT DOWN AT "
            "KNEE HEIGHT AND LOOKING STEEPLY DOWN AND ACROSS: the frame holds "
            "ONLY his knee, his forearm and his two hands, and NO FACE, HEAD, "
            "EYE OR SHOULDER APPEARS ANYWHERE IN THE PICTURE. ONE SINGLE LOOSE "
            "LEAF OF PAPYRUS lies flat across the knee, filling the middle of "
            "the frame — a rectangle about the size of two spread hands, its "
            "surface visibly fibrous with the horizontal and vertical strips of "
            "pith showing through, uneven, cream-brown, slightly cockled, its "
            "edge torn rough, its few existing lines of dark brown-black "
            "reed-pen strokes in Hebrew letters irregular in size and spacing "
            "and sitting crooked. His RIGHT hand — a broad, cracked, calloused "
            "adult MALE hand at true human scale, correctly proportioned with "
            "five fingers, its nails split and its skin stained dark "
            "green-black from olives — grips ONE cut reed pen with a split nib "
            "low down like a man unused to writing, and is drawing ONE short "
            "fresh wet line of hand-drawn Hebrew brush strokes at the foot of "
            "the sheet, the ink glossy black where it is new. His LEFT hand "
            "holds the far edge of the sheet flat. ONE small shallow fired-clay "
            "pot of lamp-black ink stands on the mat beside his knee. THE CLOTH "
            "OF HIS TUNIC ACROSS THE BOTTOM OF THE FRAME READS AS COARSE "
            "HAND-WOVEN WOOL AT THIS DISTANCE: a visible, slightly irregular "
            "over-and-under grid of warp and weft threads with a flat matte "
            "surface, a frayed selvedge and one plainly stitched patch — never "
            "knitted, never ribbed, never jersey, never fleece."
        ),
    },
    {
        "id": "v2-r036-b19", "out": "s19-he-could-hardly-believe-it.jpeg",
        "seg": "n5", "window": "73.920-76.627", "wide": False, "jesus": False,
        "locks": ["ESTATE-ACCOUNTS", "OIL-DEBTOR", "BILL-SHEET"],
        "narration": "And the farmer could hardly believe it.",
        "must_show": "The olive farmer sitting back on the mat holding the rewritten sheet in both hands, his face in strict side-on profile, plain open astonishment.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face anywhere in this frame; nobody laughs, cheers, weeps or raises the hands in triumph; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, hard clear afternoon daylight coming in "
            "almost level from the LEFT and modelling the face from the front, "
            "fine film grain, shallow but honest depth of field. THIS IS A "
            "STRICT SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS LEFT: "
            "the olive farmer is seen half-length at the RIGHT of the frame, "
            "sitting back on the mat and turned fully to the LEFT, so the "
            "viewer sees ONE cheek, ONE eye, ONE ear and the clean outline of "
            "brow, wide flat nose, mouth and short bushy black-and-grey beard "
            "against the dim plastered wall beyond. THE FAR CHEEK AND THE FAR "
            "EYE ARE COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE "
            "MASS OF HIS HEAD and cannot be seen at all; his one visible eye is "
            "wide open and aimed DOWN and to the LEFT at the sheet held in his "
            "own hands, exiting the picture through the LOWER LEFT EDGE, so his "
            "pupils are nowhere near the lens. His mouth is a little open and "
            "his brows are up: plain disbelief, not laughter, not triumph, not "
            "a smirk. Both his broad cracked green-black-stained hands hold ONE "
            "SINGLE LOOSE LEAF of fibrous cream-brown papyrus up in front of "
            "his chest, its torn edge and crooked hand-drawn Hebrew lines "
            "catching the light, the newest line still glossy. His short "
            "cropped black hair, grey at the temples, and his faded patched "
            "DEEP RUST tunic are clearly readable. HE IS THE ONLY PERSON IN THE "
            "PICTURE."
        ),
    },
    # ========== n6 — the wheat bill ===========================================
    {
        "id": "v2-r036-b20", "out": "s20-a-hundred-measures-of-wheat.jpeg",
        "seg": "n6", "window": "76.627-79.580", "wide": True, "jesus": False,
        "locks": ["GRAIN-BINS", "GRANARY-BARN", "ESTATE", "STEWARD", "WHEAT-DEBTOR"],
        "char_refs": _STEW,
        "narration": "And you? A hundred measures of wheat.",
        "must_show": "The very tall grain farmer standing at the estate's mud-brick grain bins beside open goat-hair sacks and a heap of loose wheat, one huge hand held out over the grain as he says the amount, the steward beside him.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear afternoon sun outside and "
            "dry reflected shade along the inner wall where the bins stand, the "
            "light from the LEFT and never behind any head, fine film grain, "
            "true depth of field. THE CAMERA STANDS BEHIND AND TO THE LEFT OF "
            "BOTH MEN AND SHOOTS PAST THEM at the bins: both are seen in "
            "three-quarter FROM BEHIND, full length, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. On the RIGHT the very tall heavy-shouldered grain "
            "farmer stoops slightly, his DARK UMBER work tunic hitched into its "
            "dark olive belt, his THICK BLACK CURLING HAIR to the middle of the "
            "neck plain at the back of his head, one enormous flour-dusted hand "
            "held out palm down and level over the heap of loose pale gold "
            "wheat on the plastered floor. Half a pace to his LEFT and much "
            "slighter stands the steward with his charcoal mantle down his back "
            "and his thick straight dark brown hair clear at the crown and "
            "nape, his head turned toward the farmer. Between and behind them "
            "stand TWO squat chest-high bins of mud brick and field stone "
            "plastered pale tan, each with ONE low open square drawing hole "
            "near the ground, and TWO coarse dark goat-hair sacks standing open "
            "with grain spilling from one mouth, ONE hewn wooden scoop lying on "
            "the heap. THIS IS A WIDE FULL-LENGTH SCENE: the camera is far "
            "enough back that both men are visible head to sandals."
        ),
    },
    {
        "id": "v2-r036-b21", "out": "s21-write-down-eighty.jpeg",
        "seg": "n6", "window": "79.580-83.230", "wide": False, "jesus": False,
        "locks": ["ESTATE-ACCOUNTS", "BILL-SHEET", "WHEAT-DEBTOR", "GRAIN-BINS"],
        "narration": "Take your bill, he said, and write down eighty.",
        "must_show": "The grain farmer sitting straight down on the floor beside the grain heap with ONE loose papyrus sheet across his knee, bent low over it, writing with a cut reed pen held awkwardly in his enormous hand.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face anywhere in this frame; no printed or typeset lettering, no ruled line, no column, no modern arabic numeral and no recognisable modern word on the sheet; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, hard clear afternoon daylight raking in "
            "from the LEFT across the sheet and the man's forearms, fine film "
            "grain, shallow but honest depth of field. THE CAMERA SITS LOW ON "
            "HIS LEFT AND SLIGHTLY BEHIND HIM: the grain farmer fills the RIGHT "
            "two-thirds of the frame, sitting straight down on the plastered "
            "floor with his knees up and his back rounded, bent so far over the "
            "sheet on his knee that his head is DOWN and his face is almost "
            "entirely hidden — only the underside of his jaw and the near edge "
            "of his full black beard are visible, NO EYE IS VISIBLE IN THIS "
            "PICTURE AT ALL, and his THICK BLACK CURLING HAIR falls forward "
            "from the crown to the middle of his neck and is the clearest part "
            "of his head. ONE SINGLE LOOSE LEAF OF PAPYRUS lies across his knee "
            "— fibrous, uneven, cream-brown, cockled, its edge torn rough, its "
            "existing lines of dark brown-black reed-pen Hebrew strokes "
            "irregular and crooked. His enormous flour-dusted right hand, an "
            "adult MALE hand at true human scale correctly proportioned with "
            "five fingers, grips ONE cut reed pen with a split nib awkwardly "
            "low down, the whole arm braced, drawing ONE short fresh wet line "
            "of hand-drawn Hebrew brush strokes at the foot of the sheet. ONE "
            "small shallow fired-clay pot of lamp-black ink stands on the floor "
            "by his foot. His DARK UMBER tunic across the bottom of the frame "
            "reads unmistakably as COARSE HAND-WOVEN WOOL: a visible slightly "
            "irregular over-and-under grid of warp and weft threads, flat and "
            "matte, with a frayed selvedge — never knitted, ribbed, jersey or "
            "fleece. Behind him, softly out of focus, the pale gold heap of "
            "loose wheat and one open goat-hair sack."
        ),
    },
    {
        "id": "v2-r036-b22", "out": "s22-friends-who-would-take-him-in.jpeg",
        "seg": "n6", "window": "83.230-88.259", "wide": True, "jesus": False,
        "locks": _YARD + ["STEWARD", "WHEAT-DEBTOR"], "char_refs": _STEW,
        "narration": "One after another he made friends who would remember him and take him in when he had nothing.",
        "must_show": "At the estate gateway the grain farmer stopping on his way out to take the steward's forearm in both hands in plain thanks, the steward standing still and letting him.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_FORCE + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT
        + "nobody embraces, kisses, bows, kneels, laughs, cheers or shakes hands on a bargain; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun slanting in "
            "through the gateway from the LEFT with long shadows stretched "
            "across the packed earth, the sun well out of frame and never "
            "behind any head, fine film grain, true depth of field. THE CAMERA "
            "STANDS INSIDE THE YARD BEHIND AND TO THE RIGHT OF THE STEWARD AND "
            "SHOOTS PAST HIM out toward the gateway: the steward is in the near "
            "RIGHT foreground seen in three-quarter FROM BEHIND, full length, "
            "standing quite still with his charcoal mantle down his back and "
            "his thick straight dark brown hair clear at the crown, the temple "
            "and the nape, his left forearm held out level in front of him and "
            "his face NOT visible to the camera. Facing him and stopped in the "
            "bright gateway, sharp, the very tall grain farmer has taken that "
            "forearm in BOTH his enormous flour-dusted hands and holds it, "
            "leaning his weight forward, his head bowed a little toward it so "
            "that his face is turned DOWN and AWAY and his thick black curling "
            "hair and full black beard are what the camera sees; a rolled "
            "papyrus leaf is tucked in his belt. NOT ONE FACE IS TURNED TOWARD "
            "THE LENS. Beyond them the bright dusty lane and the bare dry "
            "limestone hills. THIS IS A WIDE FULL-LENGTH SCENE: the camera is "
            "far enough back that both men are visible head to sandals. The "
            "moment is plain gratitude between two ordinary men, quiet and "
            "slightly awkward — not a celebration, not a bargain struck and not "
            "a shared joke."
        ),
    },
]

BEATS += [
    # ========== j1 — Luke 16:8, JESUS speaking (RED) ==========================
    {
        "id": "v2-r036-b23", "out": "s23-the-lord-commended-him.jpeg",
        "seg": "j1", "window": "88.259-91.990", "wide": False, "jesus": False,
        "locks": _YARD + ["MASTER", "STEWARD"], "char_refs": _BOTH,
        "narration": "And the lord commended the unjust steward, because he had done wisely:",
        "must_show": "The master standing in his own yard looking at the steward with a rueful, complicated half-smile and shaking his head slightly — grudging admiration for the sheer nerve of it, not approval and not a reward.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_CREAM + _NO_NIGHT
        + "nobody shakes hands, embraces, claps a shoulder, hands over money, offers a gift, bows, kneels or is given anything; nobody laughs out loud, cheers or raises a cup; nothing in the picture reads as a reward, a promotion or a celebration; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, warm low late-afternoon sun coming in "
            "almost level from the LEFT and modelling the face from the front, "
            "long shadows across the packed earth, the sun well out of frame "
            "and never behind any head, fine film grain, shallow but honest "
            "depth of field. THIS IS A STRICT SIDE-ON PROFILE AND THE CAMERA "
            "SITS EXACTLY ON THE MASTER'S LEFT: he is seen half-length at the "
            "RIGHT of the frame turned fully to the LEFT, so the viewer sees "
            "ONE cheek, ONE eye, ONE ear and the clean outline of brow, blunt "
            "nose, mouth and full iron-grey beard against the sunlit plastered "
            "wall beyond. THE FAR CHEEK AND THE FAR EYE ARE COMPLETELY HIDDEN "
            "BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF HIS HEAD and cannot "
            "be seen at all; his one visible eye is aimed level and to the LEFT "
            "and exits the picture through the LEFT EDGE. HIS FACE IS THE WHOLE "
            "POINT OF THIS PICTURE AND IT IS COMPLICATED: the head is tipped "
            "and turned very slightly as though shaking once from side to side, "
            "one eyebrow up, the mouth pulled sideways just short of a smile "
            "and not opening — the look of a man who has been beaten at his own "
            "game and cannot help acknowledging it, with the anger still "
            "underneath. His hands are down and empty and he holds out nothing. "
            "Far behind him at the LEFT edge, small, soft and out of focus, the "
            "steward stands in the shade with his back half turned, a dark "
            "olive and charcoal shape with dark brown hair at the crown, his "
            "face not visible. There is no bright rim, edge or outline anywhere "
            "around either head."
        ),
    },
    {
        "id": "v2-r036-b24", "out": "s24-the-children-of-this-world.jpeg",
        "seg": "j1", "window": "91.990-94.610", "wide": False, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "for the children of this world",
        "must_show": "A close side-on view of Jesus on the rooftop, half-turned toward the village below the parapet as he says it, one hand lifted low and open.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 85mm lens, clear late-morning sun coming in almost "
            "level from the LEFT and modelling the face from the front, fine "
            "film grain, shallow but honest depth of field. THIS IS A STRICT "
            "SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS LEFT: Jesus is "
            "seen half-length at the RIGHT of the frame, sitting on the low "
            "unmortared limestone parapet and turned fully to the LEFT, so the "
            "viewer sees ONE cheek, ONE eye, ONE ear and the clean outline of "
            "brow, nose, lips and beard against the soft pale distance beyond. "
            "THE FAR CHEEK AND THE FAR EYE ARE COMPLETELY HIDDEN BEHIND THE "
            "BRIDGE OF HIS NOSE AND THE MASS OF HIS HEAD and cannot be seen at "
            "all; his one visible eye looks out level and to the LEFT over the "
            "flat rooftops of the village and exits the picture through the "
            "LEFT EDGE, so his pupils are nowhere near the lens. His right hand "
            "is lifted low and open at his own chest height, palm up and "
            "slightly turned out, the small plain gesture of a man naming "
            "something ordinary. His expression is level and unguarded, neither "
            "stern nor smiling. Across the bottom third of the frame, close to "
            "the camera and softly out of focus, runs the top of the unmortared "
            "limestone parapet with one hand-woven reed mat folded on it. His "
            "hair, beard, eyes and robe are exactly as locked, and there is no "
            "bright rim, edge or outline anywhere around his head, hair or "
            "shoulders."
        ),
    },
    {
        "id": "v2-r036-b25", "out": "s25-wiser-than-the-children-of-light.jpeg",
        "seg": "j1", "window": "94.610-98.701", "wide": True, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "are in their generation wiser than the children of light.",
        "must_show": "The rooftop group from above and behind Jesus's shoulder, looking down at the four listeners sitting on their mats with their heads down, taking in what he has just said.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, clear late-morning sun from the LEFT "
            "laying long shapes of shadow across the swept plaster roof deck, "
            "the sun well out of frame and never behind any head, fine film "
            "grain, true depth of field. THE CAMERA STANDS HIGH AND BEHIND "
            "JESUS'S RIGHT SHOULDER AND SHOOTS DOWN AND PAST HIM: his shoulder, "
            "the side of his jaw and the fall of his hair occupy the near RIGHT "
            "edge, large and softly out of focus, seen from BEHIND so that his "
            "face is not presented to the lens at all, the cream wool of his "
            "robe unmistakable. Below and beyond him, sharp, the four listeners "
            "sit and crouch on hand-woven reed mats in a loose half-circle on "
            "the roof deck, seen from ABOVE: every one of them has his head "
            "DOWN or turned aside — one looking at the plaster between his own "
            "sandals, one at his own hands, one turned away toward the parapet "
            "— so that NOT ONE FACE IS TURNED TOWARD THE LENS and no eyes are "
            "visible. They are dark saturated masses of indigo, umber, rust, "
            "olive, charcoal and maroon from edge to edge. Beyond them the low "
            "limestone parapet, the flat rooftops of the village and the bare "
            "dry limestone hills. THIS IS A WIDE FULL-LENGTH GROUP SCENE: the "
            "camera is far enough back that all four seated men and the whole "
            "roof deck are in frame together. THE ONLY PALE WOOL IN THE WHOLE "
            "PICTURE IS JESUS'S OWN ROBE."
        ),
    },
    # ========== n7 — what Jesus was and was not praising ======================
    {
        "id": "v2-r036-b26", "out": "s26-even-his-employer-admired-it.jpeg",
        "seg": "n7", "window": "98.701-101.150", "wide": False, "jesus": False,
        "locks": _YARD + ["MASTER"], "char_refs": _MASTER,
        "narration": "Even his employer had to admire it.",
        "must_show": "The master alone at the end of the day, arms folded, looking off across his own empty yard with the same rueful complicated expression, working it over.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_CREAM + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face anywhere in this frame; nobody smiles broadly, laughs or looks delighted; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, warm low late-afternoon sun coming in "
            "almost level from the LEFT and modelling the face from the front, "
            "the sun well out of frame and never behind his head, fine film "
            "grain, shallow but honest depth of field. THIS IS A STRICT SIDE-ON "
            "PROFILE AND THE CAMERA SITS EXACTLY ON HIS LEFT: the master stands "
            "half-length at the LEFT of the frame turned fully to the RIGHT, so "
            "the viewer sees ONE cheek, ONE eye, ONE ear and the clean outline "
            "of brow, blunt nose, mouth and full iron-grey beard against the "
            "sunlit yard beyond. THE FAR CHEEK AND THE FAR EYE ARE COMPLETELY "
            "HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF HIS HEAD and "
            "cannot be seen at all; his one visible eye is aimed level and to "
            "the RIGHT across the empty yard and exits the picture through the "
            "RIGHT EDGE, so his pupils are nowhere near the lens. His thick "
            "arms are folded across his chest and his weight is on one hip. His "
            "expression is the same complicated one: brows drawn a little, "
            "mouth pulled sideways and closed, a short breath out through the "
            "nose — grudging respect with the anger still in it, never open "
            "pleasure. His deep maroon tunic, dark umber mantle, deep indigo "
            "sash and thick iron-grey hair are all clearly readable. HE IS THE "
            "ONLY PERSON IN THE PICTURE. Behind him, softly out of focus, the "
            "sunken oil jars and the long shadow of the fig tree across the "
            "packed earth."
        ),
    },
    {
        "id": "v2-r036-b27", "out": "s27-he-was-not-praising-the-cheating.jpeg",
        "seg": "n7", "window": "101.150-105.870", "wide": True, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "And here is the strange point Jesus was making. He was not praising the cheating.",
        "must_show": "Jesus on the rooftop leaning forward toward the listeners with both hands low and open in front of him, laying something plain and careful in front of them; the camera is behind the listeners' backs.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT
        + "nobody smiles slyly or approvingly, nobody winks, and no money, coin, purse or bill appears anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, clear late-morning sun coming in low "
            "and level from the LEFT across the roof deck, the sun well out of "
            "frame and NEVER behind any head, fine film grain, true depth of "
            "field. THE CAMERA STANDS BEHIND THE SEATED LISTENERS AND SHOOTS "
            "PAST THEM: two dark-clad men fill the near lower LEFT and lower "
            "RIGHT corners as heads, shoulders and BACKS seen entirely FROM "
            "BEHIND, large and softly out of focus, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. Jesus sits facing them between and beyond those "
            "two dark shapes, sharp, three-quarter length and in three-quarter "
            "view, leaning forward from the low limestone parapet with his "
            "forearms on his knees and BOTH HANDS held low and open in front of "
            "him, palms up and slightly apart, as though setting something down "
            "carefully where they can all see it. His gaze goes DOWN and to the "
            "LEFT toward the nearest listener's hands and exits the picture "
            "through the LOWER LEFT EDGE. His expression is careful and "
            "serious, correcting a misunderstanding gently — not stern, not "
            "amused, not sly. THIS IS A WIDE FULL-LENGTH SCENE: the camera is "
            "far enough back that Jesus is visible head to sandals with the "
            "swept plaster roof deck, the low parapet and the flat village "
            "rooftops behind him. THE ONLY PALE WOOL IN THE WHOLE PICTURE IS "
            "HIS OWN ROBE, and there is no bright rim, edge or outline anywhere "
            "around any head."
        ),
    },
    {
        "id": "v2-r036-b28", "out": "s28-worldly-people-are-so-clever.jpeg",
        "seg": "n7", "window": "105.870-110.050", "wide": True, "jesus": False,
        "locks": ["VILLAGE-LANE", "MARKET-TOWN", "BACKGROUND-CAST", "NEIGHBOURS", "JUDEAN-LAND"],
        "narration": "He was pointing at the urgency. Worldly people are so clever,",
        "must_show": "A working village market at speed in the afternoon: a trader stooped over his low stone bench of goods dealing fast with a customer, everyone moving, nobody idle.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear afternoon sun down the "
            "length of the lane from the LEFT with black shade under the "
            "goat-hair awning, the sun well out of frame and never behind any "
            "head, fine film grain, true depth of field, a hint of honest "
            "motion blur on one moving arm. THE CAMERA STANDS OUT IN THE LANE "
            "BEHIND THE CUSTOMER AND SHOOTS PAST HIM at the stall: the "
            "customer's dark umber back, shoulders and the back of his dark "
            "head fill the near RIGHT third of the frame, large and softly out "
            "of focus, seen ENTIRELY FROM BEHIND. Beyond him, sharp, ONE trader "
            "of about fifty in a deep indigo tunic is stooped low over a stall "
            "that is a LOW BENCH OF DRY-LAID STONE shaded by ONE rectangle of "
            "undyed dark goat-hair cloth slung from rough wooden poles lashed "
            "with twisted fibre cord, hand-woven reed baskets and fired-clay "
            "bowls of lentils, olives and almonds on it; he is seen in strict "
            "side-on profile turned AWAY to the LEFT, one hand sweeping goods "
            "into a fold of cloth and the other already reaching, his one "
            "visible eye down on his own hands and exiting the picture through "
            "the LOWER LEFT. AT MOST THREE other people are visible further "
            "down the lane, every one of them a solid dark saturated mass of "
            "umber, charcoal, rust, olive, indigo or maroon from head to foot, "
            "in focus or out of focus, all of them walking and none facing the "
            "camera. THIS IS A WIDE FULL-LENGTH SCENE and NOT ONE FACE IS "
            "TURNED TOWARD THE LENS. The whole picture is speed and ordinary "
            "business, never sinister and never comic."
        ),
    },
    {
        "id": "v2-r036-b29", "out": "s29-so-quick-about-money.jpeg",
        "seg": "n7", "window": "110.050-113.494", "wide": False, "jesus": False,
        "locks": ["VILLAGE-LANE", "ESTATE-ACCOUNTS", "NEIGHBOURS"],
        "narration": "so quick about money and their own future.",
        "must_show": "A very close view of two adult hands tipping a few loose struck coins out of a small dark cloth purse into a waiting palm, fast, over the stone bench.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_NIGHT
        + "no face, head, eye or shoulder is visible anywhere in this frame; no heap, pile, stack, tower or glittering spill of coins, no chest of treasure, no gold bar or ingot, and no coin held up to the light; " + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, hard clear afternoon daylight "
            "raking in low from the LEFT across the stone, fine film grain, "
            "very shallow but honest depth of field. THE CAMERA IS RIGHT DOWN "
            "AT BENCH HEIGHT AND CLOSE IN: the frame holds ONLY two pairs of "
            "forearms and hands over the dry-laid stone bench, and NO FACE, "
            "HEAD, EYE OR SHOULDER APPEARS ANYWHERE IN THE PICTURE. From the "
            "LEFT, one adult MALE hand at true human scale, correctly "
            "proportioned with five fingers, weathered and olive-brown, tips a "
            "SMALL DARK CLOTH PURSE of coarse hand-woven wool mouth-down; from "
            "it fall EXACTLY FIVE small struck coins and no more, individually "
            "separated in the air and on the stone so a viewer can count every "
            "one, dull worn silver and bronze discs of uneven thickness, each "
            "correctly bearing a ruler's head in profile and a worn Greek rim "
            "legend. From the RIGHT, a second adult hand waits open and cupped "
            "beneath, already closing. The movement is fast: one coin is caught "
            "mid-fall with a hint of honest motion blur. Behind the hands, "
            "softly out of focus, the coarse woven warp and weft of a dark "
            "umber sleeve and the pale dust of the lane. Nothing glitters, "
            "nothing is heaped and nothing is held up to admire; this is a "
            "hurried ordinary payment."
        ),
    },
]

BEATS += [
    # ========== j2 — Luke 16:9, JESUS speaking (RED) ==========================
    {
        "id": "v2-r036-b30", "out": "s30-and-i-say-unto-you.jpeg",
        "seg": "j2", "window": "113.494-116.320", "wide": True, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "And I say unto you, make to yourselves friends",
        "must_show": "Jesus standing up from the parapet on the rooftop and turning back to the listeners, one hand out level toward them, beginning the thing he actually wants them to do.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, clear late-morning sun coming in low "
            "and level from the LEFT across the roof deck, the sun well out of "
            "frame and NEVER behind any head, fine film grain, true depth of "
            "field. THE CAMERA STANDS BEHIND AND BELOW THE SEATED LISTENERS AND "
            "SHOOTS UP AND PAST THEM: three dark-clad men fill the lower third "
            "of the frame as heads, shoulders and BACKS seen entirely FROM "
            "BEHIND, large and softly out of focus, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. Jesus has just stood up from the low limestone "
            "parapet and is caught MID-TURN back toward them, sharp, full "
            "length at centre right and seen in three-quarter view, his weight "
            "shifting onto the near foot and the hem of his robe still "
            "swinging; his right hand is out level at waist height, palm up and "
            "open toward the men. His gaze goes DOWN and to the LEFT to the "
            "nearest listener and exits the picture through the LOWER LEFT "
            "EDGE, so his pupils are nowhere near the lens. His expression is "
            "direct and warm, a man arriving at the point. THIS IS A WIDE "
            "FULL-LENGTH SCENE: the camera is far enough back that Jesus is "
            "visible head to sandals, with the swept plaster roof deck, the "
            "stone roller at its edge and the flat village rooftops behind him. "
            "THE ONLY PALE WOOL IN THE WHOLE PICTURE IS HIS OWN ROBE."
        ),
    },
    {
        "id": "v2-r036-b31", "out": "s31-mammon-of-unrighteousness.jpeg",
        "seg": "j2", "window": "116.320-119.720", "wide": False, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "of the mammon of unrighteousness, that when ye fail,",
        "must_show": "A close side-on view of Jesus on the rooftop, one open hand turned over and lowered a little as he names the money for what it is, his face level and unafraid.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_NIGHT
        + "no money, coin, purse, scales or treasure appears anywhere in this frame; nobody falls, stumbles, dies, lies down, is carried, is mourned or is buried; no deathbed, grave, tomb, shroud or bier; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, clear late-morning sun coming in almost "
            "level from the LEFT and modelling the face from the front, fine "
            "film grain, shallow but honest depth of field. THIS IS A STRICT "
            "SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS LEFT: Jesus is "
            "seen half-length at the RIGHT of the frame, standing and turned "
            "fully to the LEFT, so the viewer sees ONE cheek, ONE eye, ONE ear "
            "and the clean outline of brow, nose, lips and beard against the "
            "soft pale distance beyond. THE FAR CHEEK AND THE FAR EYE ARE "
            "COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF "
            "HIS HEAD and cannot be seen at all; his one visible eye looks "
            "steadily and level to the LEFT at the man he is speaking to and "
            "exits the picture through the LEFT EDGE, so his pupils are nowhere "
            "near the lens. His near hand is held out at waist height and has "
            "just been TURNED OVER, palm down and fingers loose and open, the "
            "small plain gesture of setting a thing aside without contempt. His "
            "expression is level, clear and entirely unafraid, neither stern "
            "nor sad. Across the bottom third of the frame, close to the camera "
            "and softly out of focus, runs the top of the unmortared limestone "
            "parapet and the dark shoulder of one listener. His hair, beard, "
            "eyes and robe are exactly as locked, and there is no bright rim, "
            "edge or outline anywhere around his head, hair or shoulders."
        ),
    },
    {
        "id": "v2-r036-b32", "out": "s32-they-may-receive-you.jpeg",
        "seg": "j2", "window": "119.720-123.936", "wide": True, "jesus": False,
        "locks": ["VILLAGE-LANE", "NEIGHBOURS", "NIGHT-LAMPLIGHT"],
        "narration": "they may receive you into everlasting habitations.",
        "must_show": "At dusk in the village lane, a household taking a road-worn traveller in at their own doorway — a woman's hand resting on his forearm as she steps back to make room, one small clay lamp burning low inside the room beyond.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_FORCE + _NO_MOCK + _NO_CREAM + _NO_MODERN_TOWN + _NO_MODERN_LAMP
        + "no gate of pearl or gold, no city in the sky, no stair or road climbing into the clouds, no opening in the sky, no beam or shaft of light from above, and nothing in this picture is a symbol of the afterlife — it is one ordinary village house at dusk; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, TRUE DUSK: the sky is deep blue "
            "darkening overhead with the first stars in it, the lane and the "
            "walls read as shape and silhouette, and the only colour in the "
            "picture comes from ONE small soft yellow-orange flame standing on "
            "a bare fibre wick at the pinched spout of ONE shallow closed oval "
            "fired-clay oil lamp, which sits LOW on a stone ledge just INSIDE "
            "the doorway at waist height and NEARER THE CAMERA THAN ANY HEAD, "
            "so its light travels UPWARD AND FORWARD onto the front planes of "
            "the faces and every crown, back of head, hair and shoulder stays "
            "UNLIT AND DARK. There is no sun, no sunset, no orange horizon and "
            "no warm band of colour along any skyline. THE CAMERA STANDS OUT IN THE LANE "
            "BEHIND AND TO THE LEFT OF THE TRAVELLER AND SHOOTS PAST HIM into "
            "the doorway: the traveller fills the near LEFT of the frame, full "
            "length, seen ENTIRELY FROM BEHIND, a dark umber road-worn shape "
            "with a rolled mantle on his shoulder, dust to the knees, the back "
            "of his dark head unlit and his face NOT visible. In the plain "
            "rectangular doorway, its dark goat-hair hanging knotted back "
            "against the far jamb, a woman of about forty in a deep indigo "
            "tunic has laid ONE open hand lightly on his forearm and stepped "
            "back to make room, her body already turning inward; she is in "
            "three-quarter view lit from below by the lamp, her one visible eye "
            "aimed at his hand and exiting the picture through the LOWER LEFT. "
            "Behind her a man crouches at the low hearth and a child looks at "
            "the fire. NOBODY IS PULLED, GRIPPED OR DRAGGED: her hand rests, it "
            "does not close. THIS IS A WIDE FULL-LENGTH SCENE and NOT ONE FACE "
            "IS TURNED TOWARD THE LENS."
        ),
    },
    # ========== n8 — use what you have, now ===================================
    {
        "id": "v2-r036-b33", "out": "s33-use-your-money-use-your-things.jpeg",
        "seg": "n8", "window": "123.936-126.830", "wide": False, "jesus": False,
        "locks": ["VILLAGE-LANE", "NEIGHBOURS", "JUDEAN-LAND"],
        "narration": "Use your money, he said. Use your things.",
        "must_show": "A close view of one woman's hands lowering a flat round of bread and a small fired-clay jar of oil into another woman's hand-woven reed basket in the lane, in ordinary daylight.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_MOCK + _NO_CREAM + _NO_MODERN_TOWN + _NO_NIGHT
        + "no face, head, eye or shoulder is visible anywhere in this frame; nobody kneels, bows, weeps or gives thanks theatrically; " + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, warm low late-afternoon daylight "
            "raking in from the LEFT across the basket, the sun well out of "
            "frame and never behind anything, fine film grain, very shallow but "
            "honest depth of field. THE CAMERA IS DOWN AT BASKET HEIGHT AND "
            "CLOSE IN: the frame holds ONLY forearms, hands and the basket "
            "between them, and NO FACE, HEAD, EYE OR SHOULDER APPEARS ANYWHERE "
            "IN THE PICTURE. From above LEFT, two adult FEMALE hands at true "
            "human scale, correctly proportioned with five fingers each, "
            "olive-brown, worn and clean, are lowering ONE flat round of barley "
            "bread and ONE small plain fired-clay jar stopped with a plug of "
            "folded cloth down into ONE hand-woven reed basket of split willow, "
            "its weave irregular and clearly hand-made. From below RIGHT, two "
            "older adult FEMALE hands, thinner and more lined, hold the "
            "basket's rim steady and are not grabbing. The two dark sleeves "
            "that enter the frame — one deep indigo, one dark umber — read "
            "unmistakably as COARSE HAND-WOVEN WOOL at this distance: a "
            "visible, slightly irregular over-and-under grid of warp and weft "
            "threads, flat and matte, one with a plainly stitched patch and a "
            "frayed selvedge — never knitted, ribbed, jersey or fleece. Behind "
            "and below, softly out of focus, the bare packed earth of the lane "
            "and the foot of a plastered wall. The gesture is unhurried, "
            "matter-of-fact and completely undramatic."
        ),
    },
    {
        "id": "v2-r036-b34", "out": "s34-to-love-people-now.jpeg",
        "seg": "n8", "window": "126.830-129.490", "wide": True, "jesus": False,
        "locks": ["VILLAGE-LANE", "NEIGHBOURS", "BACKGROUND-CAST", "JUDEAN-LAND"],
        "narration": "Use whatever you have to love people now.",
        "must_show": "A man crouched right down on his heels in the lane in front of an old woman sitting against a wall, settling his own dark mantle round her shoulders and speaking to her at her own level.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_FORCE + _NO_MOCK + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun down the "
            "lane from the LEFT with long shadows across the packed earth, the "
            "sun well out of frame and never behind any head, fine film grain, "
            "true depth of field. THE CAMERA STANDS OUT IN THE LANE BEHIND AND "
            "ABOVE THE CROUCHING MAN AND SHOOTS DOWN AND PAST HIM: he fills the "
            "near RIGHT of the frame, full length, crouched right down on his "
            "heels with his knees wide and his weight forward, seen ENTIRELY "
            "FROM BEHIND — his dark olive tunic across his back, the back of "
            "his dark head unlit and his face NOT visible to the camera at all "
            "— his two hands up at the old woman's shoulders settling a folded "
            "DARK UMBER wool mantle round them. The old woman sits on the bare "
            "ground with her back against the plastered wall, three-quarter to "
            "the camera and lit from the front, upright and composed, thin in "
            "the face but clean-limbed and dignified, her own deep rust tunic "
            "faded and patched with plainly visible stitching, ONE fold of her "
            "own mantle drawn up over her grey hair; her one clearly visible "
            "eye is aimed at HIS hands, not at the camera, and exits the "
            "picture through the LOWER RIGHT. Further down the lane AT MOST "
            "THREE other people are walking away from the camera, every one of "
            "them a solid dark mass head to foot. THIS IS A WIDE FULL-LENGTH "
            "SCENE and NOT ONE FACE IS TURNED TOWARD THE LENS."
        ),
    },
    {
        "id": "v2-r036-b35", "out": "s35-the-one-thing-you-carry.jpeg",
        "seg": "n8", "window": "129.490-133.210", "wide": True, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "Those friendships are the one thing you carry with you past the end of your life.",
        "must_show": "Jesus on the rooftop with one hand laid flat and steady over his own heart and the other still out toward the listeners, saying it quietly; the camera is behind the listeners.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT
        + "nobody dies, falls, lies down, is carried, is mourned or is buried, and there is no deathbed, grave, tomb, shroud, bier, mourner or departing spirit anywhere; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, clear late-morning sun coming in low "
            "and level from the LEFT across the roof deck, the sun well out of "
            "frame and NEVER behind any head, fine film grain, true depth of "
            "field. THE CAMERA STANDS BEHIND THE SEATED LISTENERS AND SHOOTS "
            "PAST THEM: two dark-clad men fill the near lower corners as heads, "
            "shoulders and BACKS seen entirely FROM BEHIND, large and softly "
            "out of focus, and NOT ONE FACE IS TURNED TOWARD THE LENS. Jesus "
            "stands facing them beyond those dark shapes, sharp, three-quarter "
            "length and in three-quarter view; his LEFT hand is laid flat and "
            "still against his own chest over the heart and his RIGHT hand is "
            "still held low and open toward the men. His gaze goes level and to "
            "the LEFT to the farther listener and exits the picture through the "
            "LEFT EDGE, so his pupils are nowhere near the lens. His expression "
            "is quiet certainty, warm and unhurried, neither solemn nor sad. "
            "THIS IS A WIDE FULL-LENGTH SCENE: the camera is far enough back "
            "that Jesus is visible head to sandals with the swept plaster roof "
            "deck, the low limestone parapet and the flat village rooftops "
            "behind him. THE ONLY PALE WOOL IN THE WHOLE PICTURE IS HIS OWN "
            "ROBE, and there is no bright rim, edge or outline anywhere around "
            "any head, hair or shoulder."
        ),
    },
    {
        "id": "v2-r036-b36", "out": "s36-be-that-urgent.jpeg",
        "seg": "n8", "window": "133.210-136.482", "wide": False, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "Be that urgent about what actually lasts.",
        "must_show": "A closer side-on view of Jesus on the rooftop, leaning in with real urgency, one hand closed lightly into a loose fist at his own chest.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_NIGHT
        + "nobody shouts, points a finger at anyone, raises a fist in anger or looks stern or threatening; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, clear late-morning sun coming in almost "
            "level from the LEFT and modelling the face from the front, fine "
            "film grain, shallow but honest depth of field. THIS IS A STRICT "
            "SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS LEFT: Jesus is "
            "seen from the chest up at the RIGHT of the frame, leaning forward "
            "and turned fully to the LEFT, so the viewer sees ONE cheek, ONE "
            "eye, ONE ear and the clean outline of brow, nose, lips and beard "
            "against the soft pale distance beyond. THE FAR CHEEK AND THE FAR "
            "EYE ARE COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE "
            "MASS OF HIS HEAD and cannot be seen at all; his one visible eye is "
            "aimed level and to the LEFT, close and intent on the man in front "
            "of him, and exits the picture through the LEFT EDGE, so his pupils "
            "are nowhere near the lens. His near hand is up at his own chest "
            "and lightly closed into a loose, unclenched fist — pressing "
            "something home, never threatening. His expression is urgency "
            "without anger: the brows drawn in a little, the eyes steady and "
            "alive, the mouth open on the word. Across the bottom third of the "
            "frame, close to the camera and softly out of focus, runs the dark "
            "shoulder and the back of the head of one listener, seen from "
            "behind. His hair, beard, eyes and robe are exactly as locked, and "
            "there is no bright rim, edge or outline anywhere around his head."
        ),
    },
]

BEATS += [
    # ========== j13 — Luke 16:13, JESUS speaking (RED) ========================
    {
        "id": "v2-r036-b37", "out": "s37-no-servant-can-serve-two-masters.jpeg",
        "seg": "j13", "window": "136.482-138.990", "wide": True, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "No servant can serve two masters:",
        "must_show": "Jesus on the rooftop holding both hands up and apart at shoulder width, palms facing one another, setting out the two sides of the saying.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT
        + "no money, coin, purse, scales, idol, statue, altar or symbolic object appears anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, clear late-morning sun coming in low "
            "and level from the LEFT across the roof deck, the sun well out of "
            "frame and NEVER behind any head, fine film grain, true depth of "
            "field. THE CAMERA STANDS BEHIND AND BELOW THE SEATED LISTENERS AND "
            "SHOOTS UP AND PAST THEM: three dark-clad men fill the lower third "
            "of the frame as heads, shoulders and BACKS seen entirely FROM "
            "BEHIND, large and softly out of focus, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. Jesus stands facing them beyond those dark "
            "shapes, sharp, full length at centre and seen in three-quarter "
            "view, with BOTH HANDS lifted to shoulder height and held wide "
            "apart, the palms turned in to face one another, marking out two "
            "separate things in the air. His gaze goes level and to the LEFT "
            "and exits the picture through the LEFT EDGE, so his pupils are "
            "nowhere near the lens. His expression is plain and matter-of-fact, "
            "a man stating something obvious. THIS IS A WIDE FULL-LENGTH SCENE: "
            "the camera is far enough back that Jesus is visible head to "
            "sandals with the swept plaster roof deck, the low limestone "
            "parapet, the flat village rooftops and the bare dry hills behind "
            "him. THE ONLY PALE WOOL IN THE WHOLE PICTURE IS HIS OWN ROBE."
        ),
    },
    {
        "id": "v2-r036-b38", "out": "s38-he-will-hate-the-one.jpeg",
        "seg": "j13", "window": "138.990-141.750", "wide": True, "jesus": False,
        "locks": ["TWO-MASTERS", "ESTATE", "JUDEAN-LAND"],
        "narration": "for either he will hate the one, and love the other;",
        "must_show": "A young household servant stopped in the middle of a courtyard between two ordinary householders standing well apart, each of them calling him at the same moment from opposite sides; his body is caught between them.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_FORCE + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT
        + "neither householder is raised up, enthroned, crowned, robed in state, lit differently from the other or framed as a god, a king, a judge or a spirit; no idol, statue, altar, shrine, heap of raised coins, scales of judgement or symbolic object anywhere; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, flat hard midday sun straight down into "
            "the courtyard with short shadows, the light even on both sides of "
            "the frame so that NEITHER MAN IS LIT MORE BRIGHTLY OR MORE WARMLY "
            "THAN THE OTHER, the sun well out of frame and never behind any "
            "head, fine film grain, true depth of field. THE CAMERA STANDS "
            "BEHIND THE YOUNG SERVANT AND SHOOTS PAST HIM ACROSS THE YARD: he "
            "is centre frame, full length, seen ENTIRELY FROM BEHIND, stopped "
            "mid-stride with his weight still on the back foot, his knee-length "
            "DARK OLIVE work tunic and charcoal belt plain, his SHORT BLACK "
            "CURLING HAIR cropped close to the skull clearly visible at the "
            "crown and nape, his head turned to his own LEFT and his shoulders "
            "still square to the RIGHT so his whole body reads as caught "
            "between two pulls; his face is NOT visible. Level with him and "
            "well apart, one at the LEFT edge and one at the RIGHT edge, stand "
            "the two householders, both full length, both in three-quarter view "
            "turned inward toward the boy, both with one hand lifted and open "
            "at chest height calling him — the LEFT one a spare upright man of "
            "about forty-five in DEEP INDIGO with a full dark brown beard, the "
            "RIGHT one a shorter thickset man of about sixty in DARK UMBER with "
            "a wide grey beard. Their gazes are both aimed at the boy in the "
            "middle and neither exits toward the camera. THIS IS A WIDE "
            "FULL-LENGTH SCENE and NOT ONE FACE IS TURNED TOWARD THE LENS. "
            "Nobody touches anybody and nobody is grabbed."
        ),
    },
    {
        "id": "v2-r036-b39", "out": "s39-hold-to-the-one.jpeg",
        "seg": "j13", "window": "141.750-145.170", "wide": True, "jesus": False,
        "locks": ["TWO-MASTERS", "ESTATE", "JUDEAN-LAND"],
        "narration": "or else he will hold to the one, and despise the other.",
        "must_show": "The same young servant having chosen: he has walked to the older householder on the right and stands close beside him facing his way, while his shoulder is turned squarely against the other man, who has let his calling hand fall.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_FORCE + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT
        + "neither householder is raised up, enthroned, crowned, robed in state, lit differently from the other or framed as a god, a king, a judge or a spirit; no idol, statue, altar, shrine, heap of raised coins or symbolic object anywhere; nobody sneers, spits, gestures rudely or strikes anyone; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, the same flat hard midday sun straight "
            "down into the same courtyard with short shadows, the light still "
            "even on both sides so that NEITHER MAN IS LIT MORE BRIGHTLY OR "
            "MORE WARMLY THAN THE OTHER, the sun out of frame and never behind "
            "any head, fine film grain, true depth of field. THE CAMERA STANDS "
            "WELL BACK AND TO THE LEFT, BEHIND THE ABANDONED HOUSEHOLDER, AND "
            "SHOOTS PAST HIM ACROSS THE YARD: the spare upright DEEP INDIGO man "
            "of about forty-five fills the near LEFT of the frame, full length, "
            "seen ENTIRELY FROM BEHIND, his calling hand now dropped and "
            "hanging at his side, his dark brown hair clear at the crown and "
            "nape and his face NOT visible. Away across the swept courtyard at "
            "the RIGHT, smaller and sharp, the young servant now stands close "
            "in beside the thickset DARK UMBER householder of about sixty; the "
            "boy is seen in three-quarter FROM BEHIND with his shoulder turned "
            "squarely away toward the camera's side of the yard, his head up "
            "and angled toward the older man, his short black curls plain — his "
            "face is not visible either. The older man's hand rests lightly and "
            "briefly on the boy's near shoulder and does not grip. Nobody is "
            "dragged, pulled or held. THIS IS A WIDE FULL-LENGTH SCENE: the "
            "camera is far enough back that all three men are visible head to "
            "sandals in one courtyard, and NOT ONE FACE IS TURNED TOWARD THE "
            "LENS. The whole picture is told by BODIES AND DISTANCE, never by a "
            "sneer."
        ),
    },
    {
        "id": "v2-r036-b40", "out": "s40-ye-cannot-serve-god-and-mammon.jpeg",
        "seg": "j13", "window": "145.170-148.622", "wide": False, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "Ye cannot serve God and mammon.",
        "must_show": "A close side-on view of Jesus on the rooftop saying the last clause simply and finally, both hands come down and still.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_NIGHT
        + "GOD IS NOT DEPICTED IN ANY WAY: no figure, face, form, hand, throne, cloud, opening sky, light, glow, radiance or presence stands for God anywhere in this frame; and money is not personified — no idol, statue, altar, shrine, demon, heap of raised coins, scales of judgement or symbolic object of any kind appears; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, clear late-morning sun coming in almost "
            "level from the LEFT and modelling the face from the front, fine "
            "film grain, shallow but honest depth of field. THIS IS A STRICT "
            "SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS LEFT: Jesus is "
            "seen half-length at the RIGHT of the frame, standing and turned "
            "fully to the LEFT, so the viewer sees ONE cheek, ONE eye, ONE ear "
            "and the clean outline of brow, nose, lips and beard against the "
            "soft pale distance of the village rooftops beyond. THE FAR CHEEK "
            "AND THE FAR EYE ARE COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS "
            "NOSE AND THE MASS OF HIS HEAD and cannot be seen at all; his one "
            "visible eye looks steadily and level to the LEFT at the man in "
            "front of him and exits the picture through the LEFT EDGE, so his "
            "pupils are nowhere near the lens. BOTH HIS HANDS HAVE COME DOWN "
            "AND ARE STILL, hanging open and empty at his sides, so the frame "
            "holds no gesture at all — the words land on their own. His "
            "expression is settled and kind and completely final, without a "
            "trace of threat. Across the bottom third of the frame, close to "
            "the camera and softly out of focus, runs the top of the unmortared "
            "limestone parapet with the coarse woven warp and weft of one dark "
            "reed mat folded on it. His hair, beard, eyes and robe are exactly "
            "as locked, and there is no bright rim, edge or outline anywhere "
            "around his head, hair or shoulders."
        ),
    },
    # ========== n9 — the line that ties it together ===========================
    {
        "id": "v2-r036-b41", "out": "s41-the-line-that-ties-it-together.jpeg",
        "seg": "n9", "window": "148.622-151.550", "wide": True, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "Then he said the line that ties it all together.",
        "must_show": "The rooftop from further back and lower, Jesus standing still among the seated listeners after the saying, the whole group quiet, the village spread out beyond the parapet.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 28mm lens, clear late-morning sun from the LEFT "
            "laying long shapes of shadow across the swept plaster roof deck, "
            "the sun well out of frame and NEVER behind any head, fine film "
            "grain, true depth of field. THE CAMERA IS SET LOW AND WELL BACK "
            "BEHIND THE SEATED LISTENERS, DOWN NEAR THE ROOF DECK, AND SHOOTS "
            "UP AND PAST THEM: four dark-clad men are strung across the near "
            "and middle ground, every one of them seen FROM BEHIND or from the "
            "side with the head down or turned away, dark saturated masses of "
            "indigo, umber, rust, olive, charcoal and maroon, and NOT ONE FACE "
            "IS TURNED TOWARD THE LENS. Jesus stands beyond them at centre "
            "right, full length and small in the frame, quite still with his "
            "hands down at his sides and his head turned to his own left in "
            "three-quarter view, looking out over the parapet; his gaze exits "
            "the picture through the LEFT EDGE. THIS IS A WIDE FULL-LENGTH "
            "SCENE and the widest in the video: the camera is far enough back "
            "that the whole roof deck, the stone roller at its edge, the low "
            "unmortared limestone parapet, the flat rooftops of the village "
            "below and the bare dry limestone hills beyond are all in frame "
            "together with the five men. THE ONLY PALE WOOL IN THE WHOLE "
            "PICTURE IS HIS OWN ROBE, and there is no bright rim, edge or "
            "outline anywhere around any head."
        ),
    },
    {
        "id": "v2-r036-b42", "out": "s42-loving-one-despising-the-other.jpeg",
        "seg": "n9", "window": "151.550-154.270", "wide": False, "jesus": False,
        "locks": ["TWO-MASTERS", "ESTATE"],
        "narration": "You will end up loving one and despising the other,",
        "must_show": "A close side-on view of the young servant's face in the courtyard, torn — looking one way while his body is still turned the other, no malice in him, just a boy who cannot do both.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_FORCE + _NO_CREAM + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face is sharply visible anywhere in this frame; nobody sneers, snarls, weeps or looks wicked; no idol, statue, altar, coin, purse or symbolic object anywhere; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, flat hard midday daylight coming in "
            "almost level from the LEFT and modelling the face from the front, "
            "fine film grain, shallow but honest depth of field. THIS IS A "
            "STRICT SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS LEFT: "
            "the young servant is seen from the chest up at the RIGHT of the "
            "frame, his shoulders squared to the RIGHT but his head turned "
            "fully to the LEFT, so the viewer sees ONE cheek, ONE eye, ONE ear "
            "and the clean outline of brow, straight nose, mouth and the first "
            "light dark down of a young beard on his jaw against the pale "
            "plastered courtyard wall beyond. THE FAR CHEEK AND THE FAR EYE ARE "
            "COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF "
            "HIS HEAD and cannot be seen at all; his one visible eye is aimed "
            "level and to the LEFT, away from the direction his body faces, and "
            "exits the picture through the LEFT EDGE, so his pupils are nowhere "
            "near the lens. He is about nineteen, slight and narrow-framed, "
            "with SHORT BLACK CURLING HAIR cropped close to the skull and warm "
            "olive-brown skin. His expression is genuine difficulty and no "
            "malice at all: the brows pulled together, the mouth closed and "
            "unhappy, the throat working. His DARK OLIVE knee-length work tunic "
            "and charcoal belt are clearly readable. Far behind him at the LEFT "
            "edge, very small and thoroughly out of focus, one dark human shape "
            "stands in the courtyard, unreadable and faceless."
        ),
    },
    {
        "id": "v2-r036-b43", "out": "s43-money-is-a-hungry-master.jpeg",
        "seg": "n9", "window": "154.270-157.825", "wide": False, "jesus": False,
        "locks": ["ESTATE", "NIGHT-LAMPLIGHT", "NEIGHBOURS", "ESTATE-ACCOUNTS"],
        "narration": "and money is a hard, hungry thing to serve.",
        "must_show": "A man alone late at night, sitting on the floor by one small clay lamp and dropping struck coins one at a time into a fired-clay jar, joyless and tired, long after everyone else has gone to bed.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_MODERN_LAMP
        + "no heap, pile, stack, tower or glittering spill of coins, no chest of treasure, no gold bar or ingot, no jewels; nobody grins, gloats, caresses money, laughs or is drawn as a monster, a miser caricature or a demon; no idol, statue, altar or symbolic figure anywhere; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, TRUE NIGHT: the room falls to near "
            "black away from the flame, the deep blue-black of an unlit doorway "
            "behind him, and the ONLY light in the frame is ONE small soft "
            "yellow-orange flame standing on a bare fibre wick at the pinched "
            "spout of ONE shallow closed oval fired-clay oil lamp, which stands "
            "on the floor LOW AND IN FRONT OF HIM, at knee height and NEARER "
            "THE CAMERA THAN HIS HEAD, so its light travels UPWARD AND FORWARD "
            "onto the underside of his brow, his nose, his cheekbone and his "
            "chin while the crown and the back of his head, his hair and his "
            "shoulders stay UNLIT AND DARK and merge into the night behind him. "
            "NO LIGHT SOURCE STANDS BEHIND, ABOVE OR BEYOND HIS HEAD and there "
            "is no rim, edge or bright outline anywhere around him. THE CAMERA "
            "SITS LOW AND EXACTLY ON HIS LEFT IN STRICT SIDE-ON PROFILE: a man "
            "of about forty-five in a dark umber tunic sits on the bare floor "
            "with one knee up, half-length at the RIGHT of the frame and turned "
            "fully to the LEFT — ONE cheek, ONE eye, ONE ear, THE FAR CHEEK AND "
            "FAR EYE COMPLETELY HIDDEN behind the bridge of his nose — his one "
            "visible eye aimed DOWN at his own hands and exiting the picture "
            "through the LOWER LEFT EDGE. He is dropping ONE small worn struck "
            "coin at a time from his right hand into the narrow mouth of ONE "
            "plain fired-clay jar held between his knees; THREE more coins lie "
            "separated and individually countable on the floor beside the lamp, "
            "dull and unglittering. His face is flat exhaustion — the eyes "
            "hollow, the mouth slack, no pleasure in it whatever. He is the "
            "only person in the picture."
        ),
    },
]

BEATS += [
    # ========== n10 — the closing application =================================
    {
        "id": "v2-r036-b44", "out": "s44-that-is-how-good-he-is.jpeg",
        "seg": "n10", "window": "157.825-159.600", "wide": False, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "That is how good he is.",
        "must_show": "A close side-on view of Jesus on the rooftop, the pressure gone out of his face, simply warm and at rest after saying it.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 85mm lens, clear late-morning sun coming in almost "
            "level from the LEFT and modelling the face from the front, fine "
            "film grain, shallow but honest depth of field. THIS IS A STRICT "
            "SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS RIGHT: Jesus is "
            "seen from the chest up at the LEFT of the frame, turned fully to "
            "the RIGHT, so the viewer sees ONE cheek, ONE eye, ONE ear and the "
            "clean outline of brow, nose, lips and beard against the soft pale "
            "distance beyond. THE FAR CHEEK AND THE FAR EYE ARE COMPLETELY "
            "HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF HIS HEAD and "
            "cannot be seen at all; his one visible eye looks level and to the "
            "RIGHT at the man he is speaking to and exits the picture through "
            "the RIGHT EDGE, so his pupils are nowhere near the lens. All the "
            "pressure has gone out of his face: the brows easy, the eyes warm "
            "and steady, the mouth relaxed just short of a smile — the settled "
            "look of a man who has finished saying a hard thing kindly. His "
            "hands are down and out of frame. Across the bottom third of the "
            "frame, close to the camera and softly out of focus, runs the dark "
            "shoulder and the back of the head of one listener seen from "
            "behind. His hair, beard, eyes and robe are exactly as locked, and "
            "there is no bright rim, edge or outline anywhere around his head, "
            "hair or shoulders."
        ),
    },
    {
        "id": "v2-r036-b45", "out": "s45-he-is-after-you.jpeg",
        "seg": "n10", "window": "159.600-163.160", "wide": True, "jesus": True, "ref": REF,
        "locks": _ROOF_J,
        "narration": "He is not after your money. He is after you.",
        "must_show": "Jesus on the rooftop with both hands open, empty and turned palm up toward the listeners, asking for nothing and offering everything; the camera is behind the listeners.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _NO_NIGHT
        + "no money, coin, purse, bill, scales or treasure appears anywhere in this frame, and nobody holds out a hand to receive anything; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, clear late-morning sun coming in low "
            "and level from the LEFT across the roof deck, the sun well out of "
            "frame and NEVER behind any head, fine film grain, true depth of "
            "field. THE CAMERA STANDS BEHIND THE SEATED LISTENERS AND SHOOTS "
            "PAST THEM: two dark-clad men fill the near lower LEFT and lower "
            "RIGHT corners as heads, shoulders and BACKS seen entirely FROM "
            "BEHIND, large and softly out of focus, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. Jesus stands facing them between and beyond those "
            "dark shapes, sharp, three-quarter length and in three-quarter "
            "view, with BOTH ARMS come a little forward and BOTH HANDS OPEN, "
            "EMPTY and turned fully palm up at waist height — the plain gesture "
            "of a man holding nothing back and asking for nothing. His gaze "
            "goes level and to the LEFT to the nearer listener and exits the "
            "picture through the LEFT EDGE, so his pupils are nowhere near the "
            "lens. His expression is open, warm and entirely without pressure. "
            "THIS IS A WIDE FULL-LENGTH SCENE: the camera is far enough back "
            "that Jesus is visible head to sandals with the swept plaster roof "
            "deck, the low limestone parapet and the flat village rooftops "
            "behind him. THE ONLY PALE WOOL IN THE WHOLE PICTURE IS HIS OWN "
            "ROBE, and there is no bright rim, edge or outline anywhere around "
            "any head, hair or shoulder."
        ),
    },
    {
        "id": "v2-r036-b46", "out": "s46-your-hands-open.jpeg",
        "seg": "n10", "window": "163.160-167.180", "wide": False, "jesus": False,
        "locks": ["VILLAGE-LANE", "NEIGHBOURS", "ESTATE-ACCOUNTS"],
        "narration": "He wants your heart free of that cruel little master and your hands open,",
        "must_show": "A close view of one adult hand tilting fully open above another person's cupped hands so that a few struck coins run out of it into theirs, the giving hand completely emptied and staying open.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_OFFICE + _NO_CREAM + _NO_NIGHT
        + "no face, head, eye or shoulder is visible anywhere in this frame; no heap, pile, stack or glittering spill of coins, no chest of treasure, no gold bar and no coin held up to the light; nobody snatches, grabs or pulls; " + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, warm low late-afternoon daylight "
            "raking in from the LEFT across the hands, the sun well out of "
            "frame and never behind anything, fine film grain, very shallow but "
            "honest depth of field. THE CAMERA IS CLOSE IN AT CHEST HEIGHT AND "
            "SLIGHTLY ABOVE: the frame holds ONLY two forearms and three hands, "
            "and NO FACE, HEAD, EYE OR SHOULDER APPEARS ANYWHERE IN THE "
            "PICTURE. From above, one adult MALE hand at true human scale, "
            "correctly proportioned with five fingers, olive-brown and "
            "weathered, has been TILTED FULLY OVER, palm down and fingers "
            "spread wide open, and is completely EMPTY — the last of what it "
            "held is falling. Below it two smaller adult FEMALE hands are "
            "cupped together to receive, and EXACTLY FOUR small worn struck "
            "coins and no more are caught between the two — one still in the "
            "air with a hint of honest motion blur, three already settled in "
            "the cupped palms, each one separated and individually countable, "
            "dull silver and bronze discs of uneven thickness bearing a ruler's "
            "head in profile and a worn Greek rim legend. Nothing glitters and "
            "nothing is heaped. The two sleeves entering the frame — one dark "
            "olive, one deep rust — read unmistakably as COARSE HAND-WOVEN WOOL "
            "at this distance: a visible, slightly irregular over-and-under "
            "grid of warp and weft threads, flat and matte, with a frayed "
            "selvedge — never knitted, ribbed, jersey or fleece. Behind them, "
            "softly out of focus, the pale dust of the lane and a plastered "
            "wall."
        ),
    },
    {
        "id": "v2-r036-b47", "out": "s47-the-things-that-last.jpeg",
        "seg": "n10", "window": "167.180-171.494", "wide": True, "jesus": False,
        "locks": ["VILLAGE-LANE", "NEIGHBOURS", "BACKGROUND-CAST", "JUDEAN-LAND"],
        "narration": "so that you spend your one short life being urgent about the things that last forever.",
        "must_show": "Golden evening in the village lane: a man in his own doorway handing a flat round of bread across to a neighbour while two children run past, an ordinary household in the middle of an ordinary kindness.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_HEIST + _NO_MOCK + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN
        + "no gate, city, stair or road in the sky, no opening in the clouds, no beam or shaft of light from above, and nothing in this picture is a symbol of eternity — it is one ordinary village lane at the end of a day; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low golden evening sun coming "
            "straight down the length of the lane from the LEFT, very long "
            "shadows stretched across the packed earth and the last light warm "
            "on the plastered walls, the sun itself well out of frame and NEVER "
            "behind any head, fine film grain, true depth of field. THE CAMERA "
            "STANDS OUT IN THE LANE BEHIND AND TO THE RIGHT OF THE NEIGHBOUR "
            "AND SHOOTS PAST HER toward the doorway: the neighbour fills the "
            "near RIGHT of the frame, full length, seen ENTIRELY FROM BEHIND, a "
            "dark umber shape with a hand-woven reed basket on her hip and one "
            "fold of her own mantle over her grey hair, her face NOT visible. "
            "In the plain rectangular doorway beyond, its dark goat-hair "
            "hanging knotted back against the far jamb, a man of about forty in "
            "a deep indigo tunic stands on his own threshold in three-quarter "
            "view, leaning out and holding a flat round of barley bread across "
            "to her in both hands, his head turned down toward the bread and "
            "his one visible eye exiting the picture through the LOWER RIGHT "
            "EDGE. Between them and closer to the camera, two children run LEFT "
            "ACROSS THE FRAME with a hint of honest motion blur, seen from the "
            "side and from behind, dark small shapes, neither face turned to "
            "the lens. Further down the lane AT MOST THREE other people walk "
            "away from the camera, each a solid dark mass head to foot. THIS IS "
            "A WIDE FULL-LENGTH SCENE and NOT ONE FACE IS TURNED TOWARD THE "
            "LENS."
        ),
    },
]
