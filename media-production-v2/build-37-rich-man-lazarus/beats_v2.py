#!/usr/bin/env python3
"""V2 beat map — row 37, build-37-rich-man-lazarus (Luke 16:19-31). REALISTIC V2.

THE INHERITED SCAFFOLD WAS DISCARDED and is kept beside this file as
`beats_v2.py.inherited-scaffold` for provenance only. Three measured reasons:
  1. 27 pictures at 5.25 s each against the wave's MEASURED 3.1-4.9 s.
  2. Its windows were NOT CONTIGUOUS — 22 separate dead intervals where no
     picture is declared at all.
  3. It covered only 141.750 s of the 156.525 s that need pictures: nearly
     FIFTEEN SECONDS of narration with no picture declared for it.

WHAT V1 ACTUALLY DID (verified against the artefact, not the prose): EIGHT
stills for 165.35 s of finished video, and one of them is REUSED:
  * `s5.jpeg` covers n6 + j3 + n7 — 44.708 s to 77.693 s, THIRTY-THREE
    SECONDS on ONE picture: the rich man's death and burial, his waking in
    torment, the WHOLE red-letter plea of Luke 16:24 ("Father Abraham, have
    mercy on me... for I am tormented in this flame"), and the sight across
    the gulf. Four distinct events and the longest red-letter line in the
    video, all on one image.
  * `s6.jpeg` covers j1 + j4 + n8 — 77.693 s to 109.681 s, THIRTY-TWO
    SECONDS — and is then REUSED for n11 + j2 at 133.452-143.640 s. So
    Abraham's FINAL ANSWER, the line the whole parable exists to deliver
    ("neither will they be persuaded, though one rose from the dead"), was
    shown on a picture the viewer had already been staring at for half a
    minute. The climax had NO PICTURE OF ITS OWN.
  * `s7.jpeg` covers n9 + j5 + n10 — 109.681 s to 133.452 s, TWENTY-FOUR
    SECONDS, including the five brethren and "They have Moses and the
    prophets".
  * `s8.jpeg` covers n12 + n13 — 143.640 s to the card, TWENTY-ONE SECONDS:
    the ENTIRE closing application on one image.
  V2 gives all nineteen spoken segments their own pictures: 49 pictures over
  156.525 s = 3.19 s/picture, shortest 1.75 s, longest 4.82 s.

AUDIO: LOCKED, never re-voiced, V1 never written to. The V1 MP4's audio stream
is 165.372 s and extract_beats' reconstruction of V1's own timeline arithmetic
(LEAD 0.28, GAP 0.65, KJV_GAP 1.6, TAIL 1.5) totals 165.351 s — 0.021 s apart,
nowhere near the 0.75 s staleness tripwire. GIT CONTENT DATES (mtimes are
worthless here): the MP4 and every one of the twenty mp3s share ONE commit,
2026-07-27T23:12:27.

SOURCING TRAP — THIS ROW HAD A LIVE ONE AND IT WAS CHASED TO THE BOTTOM.
`make_narration.py` is NEWER than its own audio (2026-07-28T13:28:03, the day
AFTER the mp3s), and that commit's message says "narration re-recorded". It
REWROTE n13, from a long three-sentence ending to the short "Because the day is
still yours - for now." A script that post-dates its audio is exactly the case
where the script cannot be trusted, so all twenty segments were transcribed with
faster-whisper (small.en, word_timestamps=True) and compared against the LIVE
script. THE AUDIO CARRIES THE SHORT n13 (2.586 s), i.e. the live script is the
one that matches the shipped audio, and the mp3s were evidently recommitted with
it. Three apparent differences were chased down and every one is whisper's:
  * n7 "Across a vast divide" came back as "He crossed a vast divide" from BOTH
    small.en AND medium.en — settled from the word timings, not by opinion:
    whisper's "He" spans 0.000-0.140 and "crossed" 0.140-0.380, i.e. ONE 380 ms
    word "Across" split into two tokens at the unstressed leading schwa.
  * n0 "who lived side by side" heard as "who live" — the dropped final -d
    family that rows 33 and 34 both paid for.
  * n12 "Jesus told this to people" heard as "told us to people".
No TEXT_OVERRIDES and no SPEAKER_OVERRIDES: this build already uses the modern
mbm_speakers constants, so caption colour is correct without help.

WINDOWS: rebuilt from scratch from extract_beats plus the MEASURED word timings,
never from the `.timing.json` sidecars — twelve of the twenty hold ONE phrase
spanning the whole segment and could not supply an interior split. Contiguous
0.000 -> 156.525 (the card's own start), ZERO gaps, and every one of the
nineteen speech onsets lands inside the window written for it. Each interior
split is placed 0.15 s BEFORE the onset of the word it belongs to.

CONTENT CARE — THIS IS THE ONE STORY IN THE 200 WHOSE NARRATION GOES PAST DEATH.
Every other row in the realistic wave was told to paint no heaven, hell, angel,
soul, death or torment BECAUSE THE NARRATION DOES NOT STATE IT, and rows
30/32/33/34/35/36 all held that line. Luke 16 states it outright. So the rule
does not become "paint anything" — it becomes STAGE ONLY WHAT THE TEXT SAYS,
AND NOTHING IT DOES NOT. Cameron is a Latter-day Saint and this app is his
ministry, so it is staged in Latter-day Saint terms, NOT medieval Christendom's:

  * NO CLASSICAL OR DANTE HELL IMAGERY ANYWHERE. No devil, demon, horns,
    pitchfork, tail, chain, cauldron, lake or river of fire, burning body,
    screaming crowd of the damned, cave-mouth hellmouth, skull or skeleton.
    That imagery teaches a doctrine Cameron does not hold.
  * THE PLACE OF TORMENT IS SEPARATION AND THIRST, not special effects. It is
    the SPIRIT WORLD (Greek *hades*), NOT the final state: arid, lit, hot and
    comfortless, empty to the horizon, and THE MAN IS ALONE IN EVERY FRAME OF
    IT. His torment reads on his FACE and in his isolation. "I am tormented in
    THIS FLAME" is staged as HEAT AND GLARE AND PARCHED AIR — the burning white
    sky, the scorching cracked ground, the shimmer — never a fire he stands in.
  * ABRAHAM'S BOSOM IS NEARNESS AND REST: deep tree shade, still clear water,
    green growing ground, Lazarus whole and cared for beside a dignified elderly
    Abraham. NOT clouds, NOT gates, NOT harps, NOT wings, NOT gold, NOT a throne.
  * THE GREAT GULF IS LITERAL GEOLOGICAL DISTANCE — one enormous dry rock chasm
    with both sides visible and the far side small and hazy with distance. Never
    a wall, a fence, a bridge, a veil or a canyon of fire.
  * THE ANGELS: the text says angels carried him, so they may appear — as
    dignified grown MEN in ordinary dark robes, NO wings, NO haloes, NO light
    coming off them. The risk of a winged-cherub render is removed by GEOMETRY
    rather than by prohibition, per the row-10/row-14 lesson: b14 puts the
    camera BEHIND AND ABOVE the bearers so they are seen as backs and shoulders,
    which is simultaneously the lens-gaze cure and the reason no wing, halo or
    invented face can appear on them.
  * GOD IS NEVER DEPICTED AS ANY FIGURE, FACE, FORM, LIGHT OR PRESENCE, and
    JESUS IS NEVER SHOWN INSIDE THE PARABLE — he is the one telling it.
  * NOBODY IS A GHOST. Every person in the spirit world is solid, opaque,
    embodied and fully clothed; nothing floats, hovers, dissolves or gives off
    light, and no spirit is shown leaving or rising from a body.
  * THE RICH MAN IS NEVER GROTESQUE OR COMIC and LAZARUS IS NEVER PITIABLE AS
    SPECTACLE. Both keep human dignity in every frame, in life and after it.
  * LAZARUS IS A NAMED PERSON and is held by his own anchor across life AND
    afterlife, so the viewer recognises the man at the gate when he is seen at
    rest. His sores are dry and healed-over on his SHINS AND CALVES ONLY —
    never bleeding, and never on the hands, the wrists, the tops of the feet,
    the side or the brow, so he can never read as the crucified Christ (the
    row-31 lesson). He also wears only DARK cloth and has SHORT hair.

WHO CARRIES WHICH RED-LETTER LINE. All five red-letter segments are characters
speaking INSIDE the parable, not Jesus speaking as himself: j3 is THE RICH MAN
("Father Abraham, have mercy on me"), and j1, j4, j5 and j2 are all ABRAHAM.
Per the row 34/35/36 precedent, putting Jesus's face under a caption of a man
begging from torment, or under Abraham's refusal, would invert the line — so
every one of them is staged inside the parable where the words are said. Jesus
is on screen ONLY in the three frames where the narration says he is speaking as
himself: b01 (n0, beginning to tell it), b46 and b48 (n12, the application).

STAGING — six places, none of them repeating a composition used elsewhere in the
realistic wave (rows 2/8/21 Luke 15; 11 night gale; 16 interior; 19 dawn shore;
22 basalt doorstep; 23 terraced hillside; 24 moored boat; 25 wheat field; 26
kitchen garden; 27 synagogue bench + baking yard; 28 ploughed field + mud-brick
hut; 29 limestone shelf / caravan road / quayside / stone courtyard; 30
breakwater / open water / strand; 31 night road + bridegroom's house; 32 trading
yard + master's hall; 33 mount + six mercy scenes; 34 barns + threshing floor;
35 banquet house + city lanes; 36 rooftop + estate yard + accounts corner):
  * the FIG COURT — a small walled village courtyard under one great old fig
    tree, where Jesus sits and tells it to well-dressed listeners (row 36's
    teaching place was a flat rooftop, row 33's a rock-cut stair, row 34's a
    lone terebinth on open harvest country, row 35's a Pharisee's dining room);
  * the RICH MAN'S DINING ROOM, his daily feast by lamp and by daylight
    (BANQUET-HALL; row 35's banquet hall was a host's one-off great supper with
    an empty table — this room is never empty and never waiting);
  * his GATEWAY in the boundary wall, and the dust outside it where Lazarus
    lies — the one object the whole parable hangs on;
  * the DRY HILLSIDE TOMBS where he is buried;
  * the SPIRIT WORLD'S PLACE OF REST — deep shade, still water, green ground;
  * the SPIRIT WORLD'S PLACE OF TORMENT and the GREAT GULF between them.

LOCK-WORDING AUDIT (the row-34/35/36 lesson: read every lock you write as if the
model will build the most modern — or most medieval — thing your words permit).
Four rewrites before the first paid image:
  * "fine linen" was NEVER written as a colour. Luke 16:19 says purple and fine
    linen, and the obvious render of "fine linen" is CREAM — which only Jesus
    may wear. The rich man's luxury is carried instead by DEEP TYRIAN PURPLE
    and SATURATED SAFFRON-GOLD, both real and expensive first-century dyes, and
    his lock forbids every pale tone by name.
  * "hell" and "hellfire" never appear in any prompt; the place is always named
    positively as the spirit world's place of torment, because the bare noun is
    what pulls the Inferno.
  * "angel" never appears in a scene text. The bearers are described as what
    they are — two grown men carrying him — because the word itself is what
    grows wings.
  * "gate" is pinned to the shared COURTYARD-GATE lock on every frame it is
    visible in, because the bare word pulls a wrought-iron estate gate; row 36
    hit the same defect from the other side and cured it by deleting a gateway,
    which this story cannot do.

CAST: THREE anchors, all of them pictures that had to exist on the timeline
anyway, so the anchors cost nothing extra. All three are generated in ONE anchor
run before anything else, and NO anchor has another anchor in its frame, so the
REFS cache cannot make an anchor reference itself.
  b03 RICHMAN — face-showing, strict side-on profile, alone in his own room.
  b06 LAZARUS — face-showing, strict side-on profile, alone outside the gate.
  b43 ABRAHAM — face-showing, strict side-on profile, alone.
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
A_RICH = "assets/s03-purple-and-fine-linen.jpeg"
A_LAZ = "assets/s06-a-poor-beggar-named-lazarus.jpeg"
A_ABE = "assets/s43-his-final-answer.jpeg"
REFS = {"RICHMAN": A_RICH, "LAZARUS": A_LAZ, "ABRAHAM": A_ABE}

_HERE = os.path.dirname(os.path.abspath(__file__))


def _have(rel):
    """ANCHOR-FIRST: a character reference attaches only once its anchor exists.

    On the first (anchor-only) run every list below is empty, so `--check`
    passes and no anchor can reference itself through the REFS cache. Every run
    after it wires the accepted anchors into all the later beats automatically.
    """
    return [rel] if os.path.isfile(os.path.join(_HERE, rel)) else []


_RICH = _have(A_RICH)
_LAZ = _have(A_LAZ)
_ABE = _have(A_ABE)
_RICH_LAZ = _RICH + _LAZ
_ABE_LAZ = _ABE + _LAZ
_ABE_RICH = _ABE + _RICH

# ---------------------------------------------------------------- negatives ---
_NO_CREAM = ("no cream, off-white, ivory, buff, beige, taupe, sand, khaki, white "
             "or pale garment, tunic, robe, mantle, sash, wrap or head covering on "
             "anybody anywhere in the frame including the blurred edges; ")
_NO_HALO = ("no halo, no nimbus, no aura, no corona, no bright outline, edge or "
            "contour around any head, hair, shoulder or body, nobody emits or "
            "radiates light, and no light source of any kind standing behind, "
            "above or beyond anyone's head; ")
# The doctrine clause. This is the one that matters most on this row.
_NO_INFERNO = ("no devil, demon, imp, satyr, monster or beast; no horns, tail, "
               "claws, bat wings, red skin or pitchfork; no chain, shackle, cage, "
               "rack, hook or instrument of torture; no cauldron, furnace, brazier, "
               "lake of fire, river of fire, pit of fire, burning coals, bonfire, "
               "burning person or flames touching anybody; no crowd of naked, "
               "writhing, screaming, tortured or damned figures; no cave mouth, "
               "jaws, arch or doorway standing for an entrance to hell; no skull, "
               "skeleton, bone, decay or death figure; and no carved or written "
               "inscription, sign or motto anywhere; ")
_NO_KITSCH = ("no cloud floor, cloudscape or city in the sky; no gate, gateway, "
              "arch or door of pearl, gold or light; no golden street, jewelled "
              "wall or shining architecture; no harp, trumpet, crown, throne, seat "
              "of judgement, scales or book of judgement; no wing, winged figure, "
              "cherub or feather anywhere on anybody; no shaft, beam, column or "
              "burst of light coming down from the sky; no stairway, ladder or path "
              "rising into the air; and no depiction of God, deity or any divine "
              "person as any figure, face, form, light or presence; ")
_NO_GHOST = ("nobody is a ghost, wisp, vapour, mist, shade, translucent or "
             "transparent figure; nobody floats, hovers, drifts or dissolves; "
             "nobody is naked or half-dressed; and no spirit is shown leaving, "
             "rising from or hovering over a body; ")
_NO_STIGMATA = ("no wound, cut, gash, blood, bleeding, bandage or dressing on any "
                "hand, wrist, palm, top of any foot, any side, rib or brow, and "
                "nobody wears cream or has long loose hair to the shoulders except "
                "where the scene itself places Jesus; ")
_NO_MOCK = ("nobody poor, sick or old is drawn grotesque, comic, monstrous, "
            "filthy, ragged to indecency, cowering, leering or pitiable, and "
            "nobody rich is drawn as a fat, jewelled, sneering caricature; each is "
            "a real person with dignity; and no modern wheelchair, walking frame, "
            "prosthesis, metal crutch, white gauze bandage or medical dressing "
            "appears anywhere; ")
_NO_IRONGATE = ("no wrought iron, cast iron, railing, bar, grille, lattice, picket, "
                "paling, spearhead, finial or ornamental metalwork on any gate or "
                "wall; no five-bar farm gate; no hinge, strap hinge, ring, knocker, "
                "handle, latch, hasp, bolt, lock plate, keyhole or padlock; no arch "
                "or curved head over the opening; and no nameplate, sign, lettering "
                "or lamp bracket on it; ")
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
_NO_FUNERAL = ("no open coffin, casket, hearse, headstone, gravestone, cross, "
               "carved memorial, dug rectangular grave pit, mound of loose earth "
               "with a spade in it, or modern funeral of any kind; no visible face, "
               "hand or foot of the dead man; and nobody is shown dying, gasping or "
               "collapsing on camera; ")
_GAZE = "nobody's pupils centred on the lens."

# Common lock stacks.
_TEACH = ["FIG-COURT", "LISTENERS", "JUDEAN-LAND", "BACKGROUND-CAST"]
_HOUSE = ["BANQUET-HALL", "RICH-HOUSE", "RICHMAN", "JUDEAN-LAND"]
_GATE = ["COURTYARD-GATE", "RICH-HOUSE", "JUDEAN-LAND"]
_REST = ["SPIRIT-WORLD", "ABRAHAM", "LAZARUS"]
_TORMENT = ["SPIRIT-WORLD", "RICHMAN"]

LOCKS = {
    # ------------------------------------------------------------- people ----
    "RICHMAN": (
        "RICH-MAN LOCK: the rich man of the parable is the SAME MAN in every "
        "picture he appears in — in his house, at his own gateway, in the lane, "
        "and afterwards in the place of torment — and he is a JUDEAN of the "
        "first century, born and weathered in the dry country of that place. He "
        "is about fifty, tall and solidly built but NOT fat, carrying himself "
        "upright and unhurried like a man used to being obeyed. HIS SKIN IS "
        "WARM OLIVE-BROWN, clearly Middle Eastern, well-fed and far less "
        "weathered than a labourer's, with a straight strong nose, a full mouth, "
        "heavy dark brows and dark brown eyes. He has a FULL, THICK, CAREFULLY "
        "TRIMMED DARK BROWN BEARD squared off at the jaw with a little grey at "
        "the chin, and THICK DARK BROWN WAVY HAIR combed back off a broad "
        "forehead and cut to the middle of the neck — never long to the "
        "shoulders, never loose to the collarbone, never bare, bald, shaven or "
        "cropped, and a clear band of that dark brown hair shows at the front "
        "edge, at the temples and at the nape in EVERY shot of him, INCLUDING "
        "EVERY SHOT TAKEN FROM BEHIND HIM. His hands are broad, clean, smooth "
        "and unmarked, with trimmed nails — a man who has never worked ground. "
        "HE WEARS EXACTLY THREE SEPARATE PIECES OF CLOTH AND NOTHING ELSE, AND "
        "THEIR COLOURS ARE THE WHOLE OF HIS WEALTH: (1) ONE ankle-length "
        "finely woven tunic in DEEP SATURATED SAFFRON-GOLD, a rich warm "
        "egg-yolk gold, smooth and closely woven with straight unshaped sleeves "
        "to the wrist; (2) ONE large rectangular mantle in DEEP TYRIAN PURPLE, "
        "a dark rich red-violet, draped over the left shoulder and falling to "
        "mid-calf, its lower edge carrying ONE narrow woven band of the same "
        "purple a shade darker; and (3) ONE folded cloth sash of DARK INDIGO "
        "knotted at his waist. Good dark leather sandals. HIS GARMENTS ARE "
        "NEVER CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI, WHITE, "
        "PALE GREY OR ANY PALE OR WASHED-OUT TONE — his 'fine linen' reads as "
        "the SATURATED SAFFRON-GOLD named above and never as a pale or "
        "undyed cloth. He wears no head covering, no turban, no cap, no crown, "
        "no diadem, no wreath, no jewellery, no ring, no chain, no brooch and no "
        "metal ornament of any kind. HE IS NEVER A CARICATURE OF A RICH MAN: "
        "not obese, not jewelled, not leering, not sneering, not gloating and "
        "not comic — a serious, composed, self-assured householder, which is "
        "exactly what makes his indifference at the gateway land. IDENTITY "
        "FLOOR, WHICH HOLDS EVEN WHEN HE IS SMALL, DISTANT, PARTLY CROPPED, "
        "SOFTLY OUT OF FOCUS OR SEEN ENTIRELY FROM BEHIND: he is a MAN OF ABOUT "
        "FIFTY, adult and full-grown, never a youth or an old man; his SKIN IS "
        "WARM OLIVE-BROWN AND CLEARLY MIDDLE EASTERN, never fair, never pink, "
        "never European-looking; he ALWAYS HAS HIS FULL TRIMMED DARK BROWN "
        "BEARD and is never clean-shaven; and in the place of torment he is "
        "STILL IN THE SAME SAFFRON-GOLD TUNIC AND DEEP PURPLE MANTLE, now "
        "dishevelled, dust-caked, sweat-darkened and dragging — the same "
        "clothes, worn out of their glory, which is how the viewer knows him. "
        "He carries no wound, no scar, no blood, no bandage and no light of any "
        "kind coming off him in any frame."
    ),
    "LAZARUS": (
        "LAZARUS LOCK: Lazarus the beggar is a NAMED PERSON and the SAME MAN in "
        "every picture he appears in — lying outside the rich man's gateway "
        "AND afterwards at rest in the place of rest — and the viewer must "
        "recognise him instantly in both, because that recognition is the whole "
        "point of the story. He is a JUDEAN of the first century, about "
        "thirty-five, small and very thin, his collarbones and the tendons of "
        "his neck showing, but NOT skeletal and NOT a horror. HIS SKIN IS WARM "
        "DEEPLY SUN-DARKENED OLIVE-BROWN, clearly Middle Eastern, burnt darker "
        "still across the cheekbones, the forehead and the backs of the hands "
        "from living out of doors. He has a narrow face, hollow cheeks, a thin "
        "straight nose and large steady dark brown eyes that are calm and "
        "aware, never vacant and never rolling. He has a SHORT RAGGED DARK "
        "BROWN BEARD, uneven and untrimmed but not long, and SHORT DARK BROWN "
        "HAIR cut close to the skull and matted flat with dust — NEVER long, "
        "NEVER loose to the shoulders, NEVER falling past the ears, clearly "
        "visible at the crown, the temples and the nape in EVERY shot of him, "
        "INCLUDING EVERY SHOT TAKEN FROM BEHIND HIM. His hands are thin, "
        "sinewy, dust-grey and cracked across the knuckles. HE WEARS EXACTLY "
        "TWO SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) ONE knee-length "
        "coarse hand-woven wool tunic in DARK UMBER-BROWN, faded to a dull "
        "grey-brown, worn thin, frayed at the hem and mended at one shoulder "
        "with plainly visible darker stitching, with short straight unshaped "
        "sleeves; and (2) ONE twisted cord of undyed brown flax at his waist. "
        "He is BAREFOOT. HE NEVER WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, "
        "SAND, KHAKI, WHITE OR ANY PALE CLOTH, and no head covering, no cap, no "
        "jewellery and no metal ornament. HIS SORES, WHICH LUKE 16:20 NAMES, "
        "ARE STATED EXACTLY AND ARE CONFINED: they are a scatter of small dry "
        "healed-over and half-healed circular sores, dull brick-red and dark "
        "brown, ONLY on his SHINS, CALVES AND KNEES — the skin around them "
        "rough, scaly and dust-grey. THEY ARE NEVER WET, NEVER BLEEDING, NEVER "
        "weeping, NEVER open, NEVER lurid, and there is NO sore, wound, cut, "
        "gash, blood, scar, bandage or dressing anywhere on his HANDS, WRISTS, "
        "PALMS, the TOPS OF HIS FEET, his SIDE, his RIBS or his BROW — this "
        "matters, because a thin bearded man with wounds in those places and "
        "pale cloth reads as the crucified Christ, which he is not. HE IS "
        "NEVER PITIABLE AS SPECTACLE: never grotesque, never comic, never "
        "monstrous, never leering, never cowering, never filthy beyond a man "
        "who sleeps in dust, and never ragged to indecency — he keeps the quiet "
        "dignity of a real person, and his face carries patience rather than "
        "self-pity. IDENTITY FLOOR, WHICH HOLDS EVEN WHEN HE IS SMALL, DISTANT, "
        "PARTLY CROPPED, SOFTLY OUT OF FOCUS OR SEEN FROM BEHIND: warm "
        "sun-darkened olive-brown Middle Eastern skin, never fair, never pale, "
        "never European-looking; SHORT dark hair and a SHORT ragged beard, "
        "never long hair; and always the DARK UMBER-BROWN knee-length tunic. "
        "IN THE PLACE OF REST HE IS THE SAME RECOGNISABLE MAN — same face, same "
        "short hair, same short beard, same DARK UMBER-BROWN tunic, now clean, "
        "whole and mended, his skin no longer dust-grey and HIS SHINS AND "
        "CALVES SMOOTH AND UNMARKED with the sores simply gone; he is still "
        "thin but no longer starved, and he is calm, rested and at ease. He "
        "never glows, never floats and never gives off light."
    ),
    "ABRAHAM": (
        "ABRAHAM LOCK: Abraham is the SAME MAN in every picture he appears in, "
        "and he is a very old JUDEAN patriarch of great dignity — the founding "
        "father of the nation, a real embodied human being, NOT a deity, NOT an "
        "angel and NOT a symbol of God. He is about eighty, tall and still "
        "upright though thin with age, broad through the shoulders, moving and "
        "sitting with unhurried composure. HIS SKIN IS WARM OLIVE-BROWN, "
        "clearly Middle Eastern, deeply lined across the forehead and around "
        "the eyes, the backs of his hands spotted and veined with age. He has a "
        "LONG FULL BEARD OF SILVER-GREY reaching the middle of his chest, and "
        "THICK SILVER-GREY HAIR falling in waves to his shoulders from a high "
        "lined forehead; it is never bare, bald, shaven, cropped or thinning, "
        "and a clear band of that silver-grey hair shows at the front edge, at "
        "the temples and at the nape in EVERY shot of him, INCLUDING EVERY SHOT "
        "TAKEN FROM BEHIND HIM. His eyes are dark brown, deep-set, steady and "
        "kind, and his expression is grave, compassionate and sorrowful — NEVER "
        "angry, NEVER stern, NEVER triumphant, NEVER condemning, because the "
        "words he speaks in this story are spoken with grief and he calls the "
        "man in torment 'Son'. His hands are large, bony and steady. HE WEARS "
        "EXACTLY THREE SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) ONE "
        "ankle-length hand-woven wool tunic in DEEP INDIGO-BLUE with straight "
        "unshaped sleeves to the wrist; (2) ONE large rectangular hand-woven "
        "wool mantle in DARK OLIVE-GREEN over both shoulders; and (3) ONE "
        "folded cloth sash of DEEP MAROON knotted at his waist. Plain worn "
        "leather sandals. HE NEVER WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, "
        "SAND, KHAKI, WHITE, PALE GREY OR ANY PALE CLOTH — a white-robed "
        "white-bearded old man reads as a painted God the Father, which this "
        "figure must NEVER be. He wears no head covering, no turban, no crown, "
        "no diadem, no wreath, no jewellery, no ring, no chain and no metal "
        "ornament. HE HAS NO WING, NO HALO, NO NIMBUS, NO AURA AND NO LIGHT OF "
        "ANY KIND COMING OFF HIM, he never floats or hovers, he is solid and "
        "opaque, his feet are on real ground and he casts a real shadow. He "
        "never holds a book, a scroll, a staff of authority, a key, a sceptre "
        "or scales, and he never sits on a throne or a raised seat of any kind "
        "— where he sits at all he sits on the plain ground, on a hand-woven "
        "mat or on a low natural rock. IDENTITY FLOOR, WHICH HOLDS EVEN WHEN HE "
        "IS SMALL, DISTANT, PARTLY CROPPED, SOFTLY OUT OF FOCUS OR SEEN FROM "
        "BEHIND: a MAN OF ABOUT EIGHTY with warm olive-brown Middle Eastern "
        "skin, never fair, never pink, never European-looking; a LONG FULL "
        "SILVER-GREY BEARD and SILVER-GREY HAIR to the shoulders; and always "
        "the DEEP INDIGO tunic under the DARK OLIVE-GREEN mantle."
    ),
    "BEARERS": (
        "BEARERS LOCK: the two who carry Lazarus are messengers of God, and in "
        "this picture they are shown as WHAT THEY LOOK LIKE — TWO ORDINARY "
        "GROWN MEN. Each is a Judean man of the first century between about "
        "thirty and forty-five, of normal adult human height and build, with "
        "warm olive-brown Middle Eastern skin, dark hair and a dark beard, and "
        "the two do not share a face. Each is dressed head to foot in ONE SOLID "
        "DARK SATURATED EARTH COLOUR — one in DEEP INDIGO, one in DARK UMBER — "
        "in a plain ankle-length hand-woven wool tunic with straight unshaped "
        "sleeves and a folded cloth sash, and plain leather sandals. NEITHER "
        "WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, WHITE OR ANY "
        "PALE CLOTH. THEY ARE PHYSICALLY ORDINARY AND ENTIRELY UNADORNED: "
        "NEITHER HAS A WING, A FEATHER, A PINION, A HALO, A NIMBUS, AN AURA, A "
        "CORONA, A BRIGHT OUTLINE OR ANY LIGHT COMING OFF HIM; neither floats, "
        "hovers, flies or drifts; neither is a child, a cherub, a woman in "
        "flowing drapery, an armoured warrior, a translucent spirit or a figure "
        "in white; neither carries a trumpet, a sword, a staff, a lamp or a "
        "lily; and neither has hair, skin or clothing that is unnaturally fair "
        "or luminous. They are simply two strong men carrying another man "
        "carefully and gently between them, with real weight in their arms and "
        "real footing on real ground, and they cast real shadows."
    ),
    "LISTENERS": (
        "LISTENERS LOCK: the people listening to Jesus in the fig court are "
        "between THREE and FIVE well-to-do Judean men of the first century, "
        "aged from about thirty to about sixty, prosperous townsmen in good "
        "cloth — this parable was told in the hearing of men who had money — "
        "each with warm sun-darkened olive-brown Middle Eastern skin, dark or "
        "greying hair and a dark or greying beard, and no two of them sharing a "
        "face. Every one of them is dressed head to foot in ONE SOLID DARK "
        "SATURATED EARTH COLOUR — DARK UMBER, CHARCOAL, DEEP RUST, DARK OLIVE, "
        "DEEP INDIGO or DEEP MAROON — in a plain ankle-length hand-woven wool "
        "tunic with a rectangular mantle over the shoulders and a folded cloth "
        "sash, and NOT ONE OF THEM WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, "
        "SAND, KHAKI, WHITE OR ANY PALE CLOTH, because a pale figure beside "
        "Jesus reads as a second, unlocked Jesus. None of them wears a crown, "
        "jewellery, chain, ring or metal ornament, and none is drawn as a "
        "sneering or comic caricature. THE CAMERA IS ALWAYS BEHIND THEM AND NOT "
        "ONE OF THEIR FACES IS EVER TURNED TOWARD THE LENS: they are seen as "
        "heads, shoulders and BACKS, sitting on the low bench or the ground or "
        "standing, leaning in toward the man they are listening to."
    ),
    "FEAST-GUESTS": (
        "FEAST-GUESTS LOCK: the rich man never dines alone — the text says he "
        "fared sumptuously EVERY DAY — so between TWO and FOUR other diners "
        "recline at his low table, all of them Judean men and women of the "
        "first century between about twenty-five and sixty, prosperous, "
        "relaxed, mid-conversation and mid-meal, each with warm olive-brown "
        "Middle Eastern skin and no two sharing a face. Every one of them is "
        "dressed head to foot in ONE SOLID DARK SATURATED COLOUR — DARK UMBER, "
        "CHARCOAL, DEEP RUST, DARK OLIVE, DEEP INDIGO or DEEP MAROON — and NOT "
        "ONE OF THEM WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, "
        "WHITE OR ANY PALE CLOTH, AND NOT ONE OF THEM WEARS SAFFRON-GOLD OR "
        "TYRIAN PURPLE, which belong to the rich man alone and are how the "
        "viewer picks him out of his own table. They are ordinary well-off "
        "people enjoying a good supper: nobody is drunk, sprawling, leering, "
        "gorging, obese or drawn as a caricature of greed, and nobody looks "
        "toward the camera. Servants, where the scene names them, are Judean "
        "men and women in plain DARK UMBER or CHARCOAL tunics, moving quietly "
        "with fired-clay dishes and jars."
    ),
    # ------------------------------------------------------------ settings ---
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
    "FIG-COURT": (
        "FIG-COURT LOCK: the place where Jesus tells this story is a small "
        "walled courtyard behind a village house, and it is used in no other "
        "video. THE COURT is an irregular rectangle of hard-swept packed earth "
        "and worn flagstones, perhaps six paces across, enclosed by walls of "
        "sun-dried mud brick over a footing of undressed field stone, plastered "
        "with mud and straw and weathered pale tan, a little higher than a "
        "man's head. ONE GREAT OLD FIG TREE stands in the corner with a thick "
        "grey gnarled trunk and broad dark green lobed leaves, throwing a wide "
        "pool of deep shade across most of the court, and the light that gets "
        "through falls in hard bright dapples on the ground. Along one wall "
        "runs a LOW BENCH of dry-laid limestone blocks, and hand-woven reed "
        "mats and a couple of fired-clay water jars sit on the ground. The one "
        "opening in the wall is a plain rectangular gap spanned by a single "
        "flat stone lintel, with nothing standing in it. THIS IS NOT A GARDEN "
        "AND NOT A COURTYARD OF ANY LATER CENTURY: no dome, minaret, bell "
        "tower, spire, tiled or pitched roof, chimney or gable against the sky; "
        "no column, carved capital, arch of dressed voussoirs, moulding, "
        "cornice, mosaic floor, fountain, statue or ornamental pool; no "
        "flowerbed, planter, trellis, pergola, clipped hedge, topiary or lawn; "
        "no chair, stool, bench with a back, table with legs or wooden door on "
        "hinges; and no pole, wire, cable, pipe, tap, drain or grating."
    ),
    "RICH-HOUSE": (
        "RICH-HOUSE LOCK: the rich man's house is a substantial first-century "
        "JUDEAN town house and every part of it is hand-built from the stone, "
        "mud brick, timber and cloth of that place. FROM OUTSIDE it presents a "
        "long blank wall of well-dressed pale limestone blocks over a rough "
        "stone footing, standing about the height of a man and a half with a "
        "flat roofline of poles and packed earth above it and NOTHING BUT THAT "
        "FLAT ROOFLINE AND BARE DRY HILLS AGAINST THE SKY. Its openings are "
        "plain rectangular gaps spanned by single flat stone lintels, with NO "
        "GLASS, closed only by panels of dark woven goat-hair cloth hung from "
        "wooden pegs and knotted back. INSIDE, walls are mud plaster washed "
        "pale tan, floors are worn flagstones or beaten plaster spread with "
        "hand-woven wool mats in deep madder, indigo and umber, and flat "
        "ceilings are carried on rough hewn timber beams with the adze marks "
        "still on them. It is wealthy in the way that world is wealthy — good "
        "stone, thick walls, many jars, deep-dyed cloth — and NOT in any later "
        "way: there is no marble, no polished or veined stone, no mosaic, no "
        "tiled floor, no fresco, no painted mural, no framed picture, no "
        "mirror, no tapestry with a woven scene, no carved panelling, no "
        "fireplace or mantel, no staircase with a balustrade, no glazed window, "
        "no hinged panelled door, no metal fitting of any kind, and no gilding, "
        "gold leaf, silver, brass or polished metal anywhere in or on it."
    ),
    "TOMBS": (
        "HILLSIDE-TOMBS LOCK: the burial place is a first-century JUDEAN "
        "rock-cut tomb and it is stated positively. A low bare limestone scarp "
        "runs along a dry hillside of stony ground and thorn scrub; cut "
        "straight into the face of that rock are ONE or TWO plain SQUARE "
        "openings about waist high, dark inside, their edges rough and "
        "chisel-marked, with a large ROUND FLAT DISC OF UNDRESSED LIMESTONE "
        "standing on edge in a shallow channel cut along the rock beside one "
        "opening, ready to be rolled across it. The ground in front is bare "
        "trodden dust and loose chippings. A body is carried on a simple BIER "
        "of two hewn poles with woven palm-fibre webbing lashed between them, "
        "and it is entirely WRAPPED AND BOUND head to foot in plain dark "
        "hand-woven wool cloth with no part of the body showing. THIS IS NOT A "
        "GRAVEYARD OF ANY LATER CENTURY: there is no headstone, gravestone, "
        "cross, obelisk, urn, carved memorial, statue, railing, kerbed plot, "
        "mown grass, gravel path, yew tree, chapel or church; no coffin, "
        "casket, hearse or flowers; no dug rectangular pit in the earth and no "
        "heap of loose soil with a spade standing in it; and no lettering, "
        "inscription, name or date carved or painted on any stone."
    ),
}

BEATS = [
    # ===== n0 — the narrator opens; Jesus begins to tell it ==================
    {
        "id": "v2-r037-b01", "out": "s01-jesus-once-told-a-story.jpeg",
        "seg": "n0", "window": "0.000-2.150", "wide": True, "jesus": True, "ref": REF,
        "locks": _TEACH,
        "narration": "Jesus once told a story about two men",
        "must_show": "Jesus sitting on the low stone bench in a shaded village fig court, turning to the well-dressed men sitting with him as he begins to speak; the camera stands behind the listeners and shoots past their backs.",
        "must_not_show": _NO_HALO + _NO_KITSCH + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the man Jesus is speaking to is NOT behind the camera — he sits "
            "far out at the LEFT EDGE of the picture, so Jesus's head is turned "
            "a quarter-turn away from the lens and STAYS there. The camera sees "
            "the SIDE of his face, the near cheek broad and the far cheek "
            "foreshortened with the far eye narrowed behind the bridge of his "
            "nose, and his eyeline runs LATERALLY ACROSS the frame and out "
            "through the LEFT EDGE. HIS PUPILS NEVER COME ROUND ONTO THE LENS "
            "AXIS, HE NEVER FACES THE VIEWER SQUARE-ON, AND HE NEVER LOOKS INTO "
            "THE CAMERA. "
            "One photograph, 35mm lens, hard bright late-morning sun falling "
            "through the broad dark leaves of the fig tree in sharp dapples "
            "across the packed earth, the deep shade cool and blue by contrast, "
            "the sun itself well out of frame and NEVER behind any head, fine "
            "film grain, true depth of field. THE CAMERA STANDS BEHIND AND "
            "SLIGHTLY ABOVE THE SEATED LISTENERS AND SHOOTS PAST THEM: four "
            "dark-clad prosperous townsmen fill the lower and right third of "
            "the frame as heads, shoulders and BACKS seen entirely FROM BEHIND, "
            "sitting on hand-woven reed mats and on the low limestone bench and "
            "leaning in, and NOT ONE FACE IS TURNED TOWARD THE LENS. Jesus sits "
            "facing them on the far side, left of centre, on the low dry-laid "
            "limestone bench with one forearm resting across his knee, "
            "three-quarter length and three-quarter view; he has just turned "
            "his head to his own left toward the nearest man and his gaze "
            "travels level and to the LEFT and exits the picture through the "
            "LEFT EDGE. THIS IS A WIDE FULL-LENGTH GROUP PHOTOGRAPH AND NOT A "
            "PORTRAIT: the camera is far enough back that all five men, the "
            "thick grey gnarled trunk of the fig tree and the plastered mud-"
            "brick courtyard wall behind them are in frame together. THE ONLY "
            "PALE WOOL IN THE WHOLE PICTURE IS HIS OWN ROBE; every other man is "
            "a solid dark saturated mass of indigo, umber, rust, olive, "
            "charcoal or maroon from edge to edge, in focus and out of focus "
            "alike."
        ),
    },
    {
        "id": "v2-r037-b02", "out": "s02-worlds-apart.jpeg",
        "seg": "n0", "window": "2.150-4.952", "wide": True, "jesus": False,
        "locks": _GATE + ["MARKET-TOWN", "BACKGROUND-CAST"],
        "narration": "who lived side by side, yet worlds apart.",
        "must_show": "One wide frame that contains both worlds at once: the long blank dressed-limestone wall of a rich house running away down a dusty lane, with the plain square-topped gateway in it, and the bare dust of the lane outside — the whole distance of the story held in one picture with no person in it.",
        "must_not_show": _NO_IRONGATE + _NO_MODERN_TOWN + _NO_CREAM + _NO_GREEN + _NO_KITSCH + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear late-afternoon sun raking in "
            "low from the LEFT, throwing the long shadow of the wall across the "
            "dust, the sun well out of frame, fine film grain, true depth of "
            "field. AN EMPTY ARCHITECTURAL WIDE SHOT WITH NO PEOPLE IN IT AT "
            "ALL. THE CAMERA STANDS LOW IN THE LANE, BACK FROM THE WALL AND "
            "LOOKING ALONG IT AWAY FROM THE TOWN, so the wall runs from the "
            "near right edge diagonally away into the distance and the lane "
            "runs beside it: the near foreground is filled edge to edge by the "
            "bare packed dust of the lane, worn hollow, scattered with loose "
            "pale limestone chippings and one flat trodden stone. The long "
            "blank wall of well-dressed pale limestone blocks fills the right "
            "half of the frame, its flat roofline of poles and packed earth "
            "along the top, and set into it about a third of the way along is "
            "ONE plain upright rectangular gateway — two dressed limestone "
            "jambs and one single flat limestone lintel straight across the "
            "top, its heavy weathered timber leaf pushed back open flat against "
            "the inside of the wall, the opening beyond it dark and empty. "
            "Beyond the far end of the wall the flat rooflines of the town and "
            "the bare dry rounded limestone hills stand against a deep "
            "cloudless blue sky burning almost white at the horizon. THIS IS A "
            "WIDE FULL-LENGTH SCENE: the camera is far enough back that the "
            "whole height of the wall from its stone footing to its roofline "
            "and the whole width of the lane are in frame together."
        ),
    },
    # ===== n1 — the rich man. ANCHOR b03. ====================================
    {
        "id": "v2-r037-b03", "out": "s03-purple-and-fine-linen.jpeg",
        "seg": "n1", "window": "4.952-8.300", "wide": False, "jesus": False,
        "locks": ["RICHMAN", "RICH-HOUSE", "JUDEAN-LAND"],
        "narration": "One was rich. He wore the finest purple and linen,",
        "must_show": "ANCHOR FRAME. The rich man alone in his own room, standing in strict side-on profile, his face clearly readable, his deep purple mantle over his saffron-gold tunic — the single reference picture that fixes his face and his colours for every later frame in life and after it.",
        "must_not_show": _NO_CREAM + _NO_HALO + _NO_MOCK + _NO_KITSCH + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the man stands in EXACT LEFT-FACING PROFILE to the camera, "
            "his shoulders square to the LEFT EDGE of the picture and his nose, "
            "lips and chin drawn cleanly against the plastered wall behind him. "
            "THE CAMERA SEES ONE SIDE OF HIS FACE ONLY — the far cheek and the "
            "far eye are HIDDEN behind the bridge of his nose and are not in "
            "the picture at all — so a lens gaze is geometrically impossible. "
            "His near eye looks level and straight ahead along his own profile "
            "line and out through the LEFT EDGE of the frame. "
            "One photograph, 50mm lens, three-quarter length from mid-thigh up, "
            "hard clear morning daylight coming in sideways from the LEFT "
            "through a plain rectangular wall opening out of frame, modelling "
            "the front planes of his face and leaving the back of his head and "
            "the wall behind him in soft shadow, the light source LOW AND IN "
            "FRONT OF HIM and never behind his head, fine film grain, shallow "
            "depth of field with the wall softly out of focus. HE IS ALONE IN "
            "THE FRAME AND NO OTHER PERSON, SHOULDER, ARM, HEAD OR BLURRED BODY "
            "APPEARS ANYWHERE IN IT, at any edge, in focus or out of focus. He "
            "is about fifty, tall and solidly built, standing still and "
            "composed with his chin level. RESTATE HIS IDENTITY IN THIS FRAME: "
            "warm olive-brown clearly Middle Eastern skin, a full thick "
            "carefully trimmed dark brown beard squared at the jaw with a "
            "little grey at the chin, and thick dark brown wavy hair combed "
            "back off a broad forehead and cut to the middle of the neck, with "
            "a clear band of that dark hair showing at the front edge and at "
            "the nape; his head is bare and he wears nothing on it. HIS CLOTH "
            "IS THE SUBJECT OF THIS PICTURE AND EACH PIECE IS SEPARATE AND "
            "COUNTABLE: ONE ankle-length finely woven tunic of DEEP SATURATED "
            "SAFFRON-GOLD, smooth and closely woven, its straight unshaped "
            "sleeve running to the wrist; over it ONE large rectangular mantle "
            "of DEEP TYRIAN PURPLE, a dark rich red-violet, draped over his "
            "left shoulder and falling in heavy folds, with ONE narrow woven "
            "band of darker purple along its lower edge; and ONE folded sash of "
            "DARK INDIGO knotted at his waist. Every one of those three cloths "
            "is a FLAT MATTE LOOM-WOVEN surface showing a slightly irregular "
            "over-and-under grid of warp and weft threads and a frayed selvedge "
            "— never knitted, ribbed, felted, fleeced, brushed, napped or "
            "shiny, and never satin or velvet. His right hand hangs relaxed and "
            "open at his side, broad, clean and unmarked. He is composed and "
            "unhurried, not proud, not sneering, not gloating."
        ),
    },
    {
        "id": "v2-r037-b04", "out": "s04-every-day-a-feast.jpeg",
        "seg": "n1", "window": "8.300-11.151", "wide": True, "jesus": False,
        "locks": _HOUSE + ["FEAST-GUESTS"], "char_refs": _RICH,
        "narration": "and every day of his life was a feast.",
        "must_show": "The rich man's daily supper in full swing: him reclining on his left elbow at the low U-shaped table among three other diners, the clay dishes full, a servant reaching in — an ordinary good supper happening, not a staged banquet.",
        "must_not_show": _NO_CREAM + _NO_HALO + _NO_MOCK + _NO_MODERN_LAMP + _NO_KITSCH + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon daylight "
            "falling in a broad shaft through a plain rectangular wall opening "
            "on the LEFT across the food and the mats, the rest of the room "
            "falling away into warm shadow, the light source out of frame and "
            "never behind any head, fine film grain, true depth of field. THE "
            "CAMERA STANDS INSIDE THE ROOM BEHIND AND ABOVE THE OPEN FOURTH "
            "SIDE OF THE TABLE AND SHOOTS PAST THE NEAREST DINERS: two "
            "dark-clad diners fill the near lower corners of the frame as "
            "shoulders, elbows and BACKS seen from behind, and NOT ONE FACE IS "
            "TURNED TOWARD THE LENS. THE RICH MAN reclines beyond them at the "
            "far side of the low knee-high adzed-timber table, propped on his "
            "LEFT elbow on a folded wool bolster with his feet away behind him, "
            "seen in three-quarter view from the side, his DEEP TYRIAN PURPLE "
            "mantle unmistakable across his shoulder over his SATURATED "
            "SAFFRON-GOLD tunic — HE IS THE ONLY PERSON IN THE FRAME WEARING "
            "EITHER OF THOSE TWO COLOURS, which is how the viewer picks him "
            "out. His right hand is halfway to a piece of flat bread and his "
            "head is turned toward the diner on his own right, his gaze running "
            "laterally across the table and out through the RIGHT EDGE. Between "
            "them the low table carries flat rounds of barley bread laid "
            "straight on the bare wood, shallow fired-clay bowls of olives, "
            "lentils, figs and dates, a joint of roast kid on a clay platter, "
            "and plain fired-clay jars and unstemmed clay cups. A servant in a "
            "plain dark umber tunic leans in from the open side with a clay "
            "jug, seen from behind. THIS IS A WIDE FULL-LENGTH SCENE: the "
            "camera is far enough back that the whole low table, all the "
            "reclining diners on their mats and bolsters and the rough hewn "
            "ceiling beams above are in frame together. The room is plainly "
            "prosperous — thick walls, mud plaster washed pale tan, hand-woven "
            "wool mats in deep madder and indigo — and the plenty on the table "
            "is the only wealth on show."
        ),
    },
    # ===== n2 — the gate, and the man at it. ANCHOR b06. =====================
    {
        "id": "v2-r037-b05", "out": "s05-at-his-own-gate.jpeg",
        "seg": "n2", "window": "11.151-13.940", "wide": True, "jesus": False,
        "locks": _GATE + ["MARKET-TOWN"],
        "narration": "Just outside his house, at his own gate,",
        "must_show": "The gateway itself, close and central and empty of people — two dressed limestone jambs, one flat stone lintel, the heavy timber leaf standing pushed back open, the worn threshold slab, and the bare dust outside it. The object the whole parable hangs on, established before anyone is put beside it.",
        "must_not_show": _NO_IRONGATE + _NO_MODERN_TOWN + _NO_CREAM + _NO_GREEN + _NO_KITSCH + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear midday sun almost overhead "
            "and slightly to the RIGHT, throwing a short black shadow of the "
            "lintel down across the threshold, the sun well out of frame, fine "
            "film grain, true depth of field. AN ARCHITECTURAL WIDE SHOT WITH "
            "NO PERSON IN IT ANYWHERE. THE CAMERA STANDS OUTSIDE IN THE LANE, "
            "SQUARE ON TO THE WALL AND BACK FROM IT, at about waist height, and because the frame is empty of people there is no eyeline in it at all and nothing is seen from the side or from behind. "
            "THE GATEWAY FILLS THE MIDDLE OF THE FRAME AND IS STATED PIECE BY "
            "PIECE: two upright jambs of well-dressed pale limestone blocks; "
            "ONE SINGLE FLAT LIMESTONE LINTEL laid straight across the top so "
            "that THE OPENING IS A PLAIN SQUARE-TOPPED RECTANGLE with no curve, "
            "arch or ring of wedge-shaped stones anywhere in it; a worn "
            "hollowed limestone threshold slab lying flush with the dust at "
            "ground level; and ONE heavy leaf of adzed timber planks set edge "
            "to edge and pegged across the back with two wooden battens, "
            "unpainted, silvered and split by weather, STANDING PUSHED BACK "
            "OPEN FLAT AGAINST THE INSIDE OF THE WALL and turning on a carved "
            "round STONE PIVOT SOCKET sunk into the threshold. Through the open "
            "rectangle a strip of the sunlit inner courtyard's packed earth and "
            "a fired-clay water jar are visible in soft focus. To either side "
            "the boundary wall of sun-dried mud brick over undressed field "
            "stone, plastered pale tan and weathered, runs out to the frame "
            "edges. THE NEAR FOREGROUND IS FILLED EDGE TO EDGE by the bare "
            "packed dust of the lane, worn hollow by feet, with loose pale "
            "limestone chippings in it. THIS IS A WIDE FULL-LENGTH SCENE: the "
            "camera is far enough back that the whole gateway from its "
            "threshold slab to its lintel and a good stretch of wall on both "
            "sides are in frame together."
        ),
    },
    {
        "id": "v2-r037-b06", "out": "s06-a-poor-beggar-named-lazarus.jpeg",
        "seg": "n2", "window": "13.940-16.548", "wide": False, "jesus": False,
        "locks": ["LAZARUS", "COURTYARD-GATE", "JUDEAN-LAND"],
        "narration": "lay a poor beggar named Lazarus.",
        "must_show": "ANCHOR FRAME. Lazarus alone, lying propped against the wall beside the gateway, in strict side-on profile with his face clearly readable — the single reference picture that fixes his face, his short hair and his dark tunic for every later frame, in life and at rest.",
        "must_not_show": _NO_STIGMATA + _NO_MOCK + _NO_CREAM + _NO_HALO + _NO_KITSCH + _NO_IRONGATE + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: the man is propped sitting against the foot of the wall "
            "with his shoulders square to the RIGHT EDGE of the picture, so the "
            "camera sees his head in EXACT RIGHT-FACING PROFILE, his brow, "
            "nose, lips and chin drawn cleanly against the sunlit plaster "
            "behind him. THE FAR CHEEK AND THE FAR EYE ARE HIDDEN behind the "
            "bridge of his nose and are not in the picture at all, so a lens "
            "gaze is geometrically impossible. His near eye is open, level and "
            "steady and looks straight ahead along his own profile line and out "
            "through the RIGHT EDGE. "
            "One photograph, 50mm lens, a tight three-quarter figure from the "
            "knees up, hard clear midday sun coming from the RIGHT and slightly "
            "in front of him so it rakes across the front planes of his face "
            "and the wall, the back of his head left in shadow and the light "
            "source never behind it, fine film grain, shallow depth of field "
            "with the plastered mud-brick wall softly out of focus behind him. "
            "HE IS ALONE IN THE FRAME AND NO OTHER PERSON, SHOULDER, ARM, HEAD "
            "OR BLURRED BODY APPEARS ANYWHERE IN IT, at any edge, in focus or "
            "out of focus. RESTATE HIS IDENTITY IN THIS FRAME: a Judean man of "
            "about thirty-five, small and very thin but not skeletal, with warm "
            "deeply sun-darkened olive-brown clearly Middle Eastern skin, a "
            "narrow face and hollow cheeks, a SHORT RAGGED DARK BROWN BEARD, "
            "and SHORT DARK BROWN HAIR cut close to the skull and matted flat "
            "with dust, clearly visible at the crown, the temple and the nape — "
            "his hair NEVER reaches his shoulders and never falls loose past "
            "his ears. He wears ONE knee-length coarse hand-woven wool tunic in "
            "DARK UMBER-BROWN faded to a dull grey-brown, worn thin, frayed at "
            "the hem and mended at the shoulder with visible darker stitching, "
            "belted with ONE twisted cord of undyed brown flax, and he is "
            "BAREFOOT. His near arm rests across his drawn-up knee, the hand "
            "thin, sinewy and dust-grey, cracked across the knuckles and "
            "ENTIRELY UNMARKED — no cut, wound, blood or bandage on the hand, "
            "the wrist or the palm. His drawn-up shin and calf carry a scatter "
            "of small DRY HEALED-OVER circular sores, dull brick-red and dark "
            "brown, the skin around them rough and scaly — dry and closed, "
            "never wet, never bleeding, never open. His expression is patient "
            "and quietly aware, tired but present: he is a real person with "
            "dignity, never grotesque, never comic, never cowering, never "
            "pitiable as a spectacle. Behind him at the extreme left edge the "
            "dressed limestone jamb and the worn threshold slab of the gateway "
            "are just visible in soft focus."
        ),
    },
    # ===== n3 — the sores, the crumbs, the dogs ==============================
    {
        "id": "v2-r037-b07", "out": "s07-covered-in-sores.jpeg",
        "seg": "n3", "window": "16.548-19.240", "wide": False, "jesus": False,
        "locks": ["LAZARUS", "JUDEAN-LAND"], "char_refs": _LAZ,
        "narration": "He was covered in sores, and so hungry,",
        "must_show": "A close, unflinching but wholly dignified frame of Lazarus's own thin folded legs and bare feet in the dust, the dry healed-over sores on his shins plainly visible — his condition shown by the body the text names, without making a spectacle of his face.",
        "must_not_show": _NO_STIGMATA + _NO_MOCK + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 85mm lens, a CLOSE frame filled by the man's own "
            "folded lower legs and bare feet where he sits in the dust against "
            "the wall, hard clear midday sun raking across from the RIGHT, fine "
            "film grain, shallow depth of field. NO FACE IS IN THIS PICTURE AT "
            "ALL — the frame is cut at the thigh and the man's head and "
            "shoulders are above the top edge and out of shot — so a lens gaze "
            "is geometrically impossible and nobody is put on display. HE IS "
            "ALONE IN THE FRAME and no other person, foot, hand, shoulder or "
            "blurred body appears anywhere in it. His shins and calves are "
            "thin, sinewy and dust-grey, and across them lies a scatter of "
            "small DRY HEALED-OVER AND HALF-HEALED CIRCULAR SORES, dull "
            "brick-red and dark brown, flat and closed, the skin around each "
            "one rough, scaly and pale with dust: THEY ARE DRY, never wet, "
            "never weeping, never bleeding, never open, never lurid. His feet "
            "are BARE, hard-soled, cracked at the heel and grey with dust, and "
            "the tops of both feet are ENTIRELY UNMARKED — no cut, wound, hole, "
            "blood or bandage anywhere on them. His near hand rests on his "
            "shin, thin and dust-grey, ALSO ENTIRELY UNMARKED across the palm "
            "and the wrist. THE NEAR FOREGROUND AND BOTH LOWER CORNERS ARE "
            "FILLED EDGE TO EDGE by the frayed hem of his DARK UMBER-BROWN wool "
            "tunic falling across his knee, its coarse loom-woven grid of warp "
            "and weft threads plainly visible at this distance with a frayed "
            "cut edge, and by the bare packed dust of the lane. Behind and "
            "above, the sunlit plastered mud-brick wall is softly out of focus. "
            "The picture is plain and matter-of-fact and carries no cruelty in "
            "it."
        ),
    },
    {
        "id": "v2-r037-b08", "out": "s08-the-scraps-that-fell.jpeg",
        "seg": "n3", "window": "19.240-23.080", "wide": False, "jesus": False,
        "locks": _HOUSE + ["BANQUET-HALL"],
        "narration": "he only wished for the scraps that fell from the rich man's table.",
        "must_show": "A close frame of the crumbs and broken bread fallen on the floor mat under the edge of the rich man's low table — the scraps themselves, countable and ordinary, with the meal going on above and behind them out of focus.",
        "must_not_show": _NO_CREAM + _NO_HALO + _NO_MOCK + _NO_MODERN_LAMP + _NO_KITSCH + _GAZE,
        "scene": (
            "One photograph, 85mm lens, a CLOSE LOW frame taken at floor level "
            "under the edge of the low knee-high adzed-timber table, warm low "
            "late-afternoon daylight falling in from the LEFT across the mat, "
            "fine film grain, shallow depth of field. NO FACE IS IN THIS "
            "PICTURE AT ALL — the camera is below the tabletop and the diners "
            "are above the top edge of the frame — so a lens gaze is "
            "geometrically impossible. THE NEAR FOREGROUND FILLS THE WHOLE "
            "LOWER HALF OF THE FRAME: a hand-woven wool floor mat in deep "
            "madder and umber, its weave and its knotted fringe sharp and "
            "close, and lying scattered across it SEVEN OR EIGHT separated, "
            "individually visible pieces of broken flat barley bread — torn "
            "crusts, a corner of a round, and loose crumbs — each one clearly "
            "countable, together with two fallen olive stones and a smear of "
            "oil soaked dark into the wool. Above and behind them, softly out "
            "of focus, the edge of the low timber tabletop cuts across the "
            "frame with a shallow fired-clay bowl and a plain unstemmed clay "
            "cup standing on it, and beyond that the warm shadowed room with "
            "one dark-clad reclining figure's elbow and folded bolster just "
            "readable and no face visible. At the extreme right edge, also out "
            "of focus, one bare human foot rests on the mat, turned away. The "
            "picture is quiet and ordinary: this is simply what falls from a "
            "good table while people eat, and nothing in it is staged, "
            "glittering or theatrical."
        ),
    },
    {
        "id": "v2-r037-b09", "out": "s09-even-the-dogs.jpeg",
        "seg": "n3", "window": "23.080-26.196", "wide": False, "jesus": False,
        "locks": ["LAZARUS", "COURTYARD-GATE", "JUDEAN-LAND"], "char_refs": _LAZ,
        "narration": "Even the stray dogs came and licked his wounds.",
        "must_show": "Two lean Levantine street dogs at Lazarus's legs where he lies against the wall by the gateway, one with its muzzle lowered to his shin — the animals gentle and matter-of-fact, and the man enduring it without struggle.",
        "must_not_show": _NO_STIGMATA + _NO_MOCK + _NO_CREAM + _NO_HALO + _NO_IRONGATE + _GAZE,
        "scene": (
            "One photograph, 50mm lens, a low CLOSE frame taken from ground "
            "level in the lane, hard clear midday sun raking across from the "
            "RIGHT and throwing short black shadows, fine film grain, shallow "
            "depth of field. THE CAMERA IS LOW AND SET BEHIND AND TO THE SIDE "
            "OF THE DOGS AND SHOOTS PAST THEM toward the wall: the nearer dog "
            "fills the lower left of the frame seen FROM BEHIND as haunches, "
            "back and lowered head, so NO ANIMAL AND NO PERSON FACES THE LENS. "
            "EXACTLY TWO DOGS ARE IN THE PICTURE and both are separated and "
            "individually countable: lean, short-haired Levantine pariah street "
            "dogs of ordinary size, tan and dust-grey, with pricked ears, "
            "narrow muzzles, visible ribs and long thin tails — ordinary living "
            "animals, never snarling, never baring teeth, never menacing, never "
            "monstrous, never wolf-like and never comic. The nearer dog's "
            "muzzle is lowered to the man's shin. LAZARUS sits propped against "
            "the foot of the plastered wall beyond them, seen in three-quarter "
            "view from his right side, his legs stretched out into the dust, "
            "his head turned DOWN AND AWAY toward the dogs so his gaze runs "
            "down and out through the LOWER LEFT of the frame and never toward "
            "the camera. RESTATE HIS IDENTITY IN THIS FRAME: warm deeply "
            "sun-darkened olive-brown Middle Eastern skin, a SHORT ragged dark "
            "brown beard, SHORT dark brown hair cut close to the skull and "
            "matted with dust and never reaching his shoulders, and ONE "
            "knee-length DARK UMBER-BROWN coarse wool tunic with a twisted flax "
            "cord at the waist, and bare feet. His shins carry the same scatter "
            "of small DRY HEALED-OVER brick-red sores, closed and not bleeding, "
            "and his hands, wrists and the tops of his feet are entirely "
            "unmarked. His face is calm and enduring, neither disgusted nor "
            "pitiful; one thin hand rests open on the ground. Behind him the "
            "dressed limestone jamb of the gateway and the bare dust of the "
            "lane run out of frame."
        ),
    },
    # ===== n4 — the rich man passes, every day ===============================
    {
        "id": "v2-r037-b10", "out": "s10-walked-past-that-gate.jpeg",
        "seg": "n4", "window": "26.196-29.310", "wide": True, "jesus": False,
        "locks": _GATE + ["RICHMAN", "MARKET-TOWN", "BACKGROUND-CAST"],
        "char_refs": _RICH,
        "narration": "The rich man walked past that gate every single day.",
        "must_show": "The rich man walking out through his own gateway into the lane, seen from behind, unhurried and composed — the whole daily routine of the parable in one frame.",
        "must_not_show": _NO_IRONGATE + _NO_MODERN_TOWN + _NO_CREAM + _NO_MOCK + _NO_HALO + _NO_GREEN + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear morning sun coming in high "
            "from the LEFT, throwing a short black shadow ahead of the walking "
            "man across the dust, the sun well out of frame and never behind "
            "any head, fine film grain, true depth of field. THE CAMERA STANDS "
            "IN THE LANE BEHIND THE MAN AND SHOOTS PAST HIM AWAY FROM THE "
            "GATEWAY: he is centre frame, full length, seen ENTIRELY FROM "
            "BEHIND and walking AWAY from the camera down the lane, so no face "
            "is in the picture at all and a lens gaze is geometrically "
            "impossible. HIS DIRECTION OF TRAVEL IS AWAY FROM THE CAMERA AND "
            "TOWARD THE FAR END OF THE LANE. BECAUSE THE CAMERA IS BEHIND HIS "
            "HEAD, HIS HAIR IS THE THING THE VIEWER SEES OF HIM AND IT IS "
            "STATED HERE: thick dark brown wavy hair combed back off a broad "
            "crown and cut level at the middle of the neck, sitting clear "
            "against the DEEP TYRIAN PURPLE mantle across his shoulders — never "
            "a bare, bald, shaven, cropped or thinning head, and he wears "
            "nothing on it. Below the purple mantle his SATURATED SAFFRON-GOLD "
            "tunic falls to his ankles and his dark leather sandals are lifting "
            "out of the dust mid-stride; HE IS THE ONLY PERSON IN THE FRAME "
            "WEARING PURPLE OR SAFFRON-GOLD. He walks upright, unhurried and "
            "composed, his arms swinging easily, his head level and facing "
            "straight down the lane ahead of him. Behind him at the right of "
            "frame stands his own gateway in the long dressed-limestone wall — "
            "two stone jambs, one flat stone lintel, the square-topped opening, "
            "the heavy timber leaf pushed back open flat against the inside of "
            "the wall. THIS IS A WIDE FULL-LENGTH SCENE: the camera is far "
            "enough back that the man is visible head to sandals and the whole "
            "height of the wall and gateway are in frame with him. Far down the "
            "lane, small with distance, ONE other townsman in a solid dark "
            "umber garment walks away in the same direction."
        ),
    },
    {
        "id": "v2-r037-b11", "out": "s11-stepped-around-him.jpeg",
        "seg": "n4", "window": "29.310-32.810", "wide": True, "jesus": False,
        "locks": _GATE + ["RICHMAN", "LAZARUS"], "char_refs": _RICH_LAZ,
        "narration": "And every day he stepped around the suffering man lying there,",
        "must_show": "The single most important composition in the video: the rich man's stride visibly bending OUT AND AROUND the man lying in the dust at the foot of his own gateway — the two of them in one frame, close enough to touch, and the detour unmistakable.",
        "must_not_show": _NO_IRONGATE + _NO_MOCK + _NO_STIGMATA + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear morning sun from the LEFT "
            "throwing both men's short black shadows across the dust, the sun "
            "well out of frame and never behind any head, fine film grain, true "
            "depth of field. THE CAMERA STANDS LOW IN THE LANE, BEHIND AND TO "
            "THE LEFT OF THE WALKING MAN, AND SHOOTS PAST HIM toward the wall: "
            "he is seen in three-quarter FROM BEHIND, full length, and no face "
            "is turned toward the lens. THE ACTION MUST READ CORRECTLY AT A "
            "GLANCE AND IT IS STATED AS GEOMETRY: LAZARUS lies low along the "
            "foot of the wall on the RIGHT of frame, propped on one elbow with "
            "his legs drawn along the base of the stonework, taking up the "
            "ground directly across the walking man's straight path; THE RICH "
            "MAN'S LINE OF WALK VISIBLY BENDS OUT AROUND HIM, his leading "
            "sandal planted well out to the LEFT in the open dust and his body "
            "angled away from the wall, his hem swinging clear of the lying "
            "man's feet, with a clear gap of bare trodden dust between them. HE "
            "IS NOT STEPPING OVER HIM, NOT TREADING ON HIM, NOT KICKING HIM, "
            "NOT LOOKING DOWN AT HIM AND NOT REACTING TO HIM AT ALL: his head "
            "stays level and faces straight down the lane ahead, his gaze "
            "exiting through the FAR END of the lane, and his expression is "
            "simply preoccupied and untroubled — the indifference is the whole "
            "point and it is carried by his level head and his unbroken pace, "
            "never by a sneer, a smirk or a look of disgust. RESTATE BOTH "
            "IDENTITIES: the walking man has thick dark brown wavy hair cut to "
            "the middle of the neck above a DEEP TYRIAN PURPLE mantle and a "
            "SATURATED SAFFRON-GOLD ankle-length tunic, and he is the only "
            "person in the frame in either colour; the lying man has SHORT dark "
            "brown hair matted with dust, a SHORT ragged dark beard, warm "
            "deeply sun-darkened olive-brown Middle Eastern skin, ONE "
            "knee-length DARK UMBER-BROWN wool tunic and bare feet, with dry "
            "healed-over brick-red sores on his shins only and his hands, "
            "wrists and the tops of his feet unmarked. His face is turned up "
            "and toward the passing man in patient appeal, his gaze travelling "
            "up and to the LEFT past the camera and out through the LEFT EDGE, "
            "never onto the lens. Above and behind them stand the two dressed "
            "limestone jambs and the single flat lintel of the square-topped "
            "gateway. THIS IS A WIDE FULL-LENGTH SCENE: the camera is far "
            "enough back that both men are visible complete, head to feet."
        ),
    },
    {
        "id": "v2-r037-b12", "out": "s12-and-did-nothing.jpeg",
        "seg": "n4", "window": "32.810-34.603", "wide": False, "jesus": False,
        "locks": _GATE + ["LAZARUS"], "char_refs": _LAZ,
        "narration": "and did nothing.",
        "must_show": "The lane after he has gone: Lazarus still lying at the foot of the wall, alone, with the empty dust and the fading footprints where the other man walked around him.",
        "must_not_show": _NO_IRONGATE + _NO_MOCK + _NO_STIGMATA + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 50mm lens, hard clear morning sun from the LEFT, "
            "fine film grain, shallow depth of field. THE CAMERA STANDS IN THE "
            "LANE LOOKING DOWN AND ALONG THE WALL FROM BEHIND AND ABOVE THE "
            "LYING MAN, so he is seen from behind and above as the back of his "
            "head, one shoulder and the length of his body, and NO FACE IS IN "
            "THE PICTURE AT ALL — a lens gaze is geometrically impossible. "
            "BECAUSE THE CAMERA IS BEHIND HIS HEAD, HIS HAIR IS STATED HERE: "
            "SHORT dark brown hair cut close to the skull, matted flat and grey "
            "with dust, clearly visible at the crown and the nape and never "
            "reaching his shoulders. He lies along the foot of the plastered "
            "mud-brick wall on his side with his knees drawn up, ONE "
            "knee-length DARK UMBER-BROWN coarse wool tunic frayed at the hem, "
            "a twisted flax cord at his waist, bare hard-soled dust-grey feet, "
            "and one thin unmarked hand loose on the ground beside him. THE "
            "NEAR FOREGROUND AND THE WHOLE LOWER THIRD ARE FILLED EDGE TO EDGE "
            "by the bare packed dust of the lane, and running across it, sharp "
            "and unmistakable, ONE line of fresh sandal prints that CURVES OUT "
            "AND AROUND the lying man and continues away down the lane — the "
            "detour left in the dust and nothing else. THE MAN IS ALONE IN THE "
            "FRAME: no other person, shoulder, arm, head, hem or blurred body "
            "appears anywhere in it, at any edge, in focus or out of focus, and "
            "the lane beyond him is empty to the end. Above him the dressed "
            "limestone jamb and flat lintel of the gateway stand in soft focus "
            "and the opening beyond is dark and empty. The frame is still and "
            "quiet and carries no cruelty in it."
        ),
    },
    # ===== n5 — Lazarus dies and is carried ==================================
    {
        "id": "v2-r037-b13", "out": "s13-the-day-that-comes.jpeg",
        "seg": "n5", "window": "34.603-37.950", "wide": False, "jesus": False,
        "locks": _GATE + ["JUDEAN-LAND"],
        "narration": "Then the day came that comes for us all.",
        "must_show": "The place at the foot of the wall where Lazarus lay, now empty — the worn hollow in the dust, his twisted flax cord left behind, and the long shadow of evening across it. Nobody in the frame, and no death shown.",
        "must_not_show": _NO_FUNERAL + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _NO_IRONGATE + _GAZE,
        "scene": (
            "One photograph, 50mm lens, the low warm raking light of late "
            "evening coming in almost level from the LEFT, throwing the long "
            "shadow of the wall right across the dust, the sun itself well out "
            "of frame, fine film grain, shallow depth of field. THERE IS NO "
            "PERSON, BODY, FIGURE, SHOULDER, HAND OR BLURRED SHAPE OF ANYBODY "
            "ANYWHERE IN THIS FRAME — it is completely empty of people, and "
            "that emptiness is the whole picture. THE CAMERA IS LOW AND CLOSE "
            "TO THE GROUND, looking along the foot of the plastered mud-brick "
            "wall. THE NEAR FOREGROUND FILLS THE FRAME EDGE TO EDGE: bare "
            "packed dust, and pressed into it a shallow WORN HOLLOW the length "
            "and shape of a man who has lain in the same place for a long time, "
            "its edges smoothed, a scatter of loose pale limestone chippings "
            "around it. Lying in the hollow, ONE twisted cord of undyed brown "
            "flax, left where it fell, its frayed end curling. Nothing else is "
            "on the ground. Behind and above, the wall runs away out of focus "
            "into the evening shadow and the dressed limestone jamb of the "
            "gateway stands dark against the last of the light. The sky beyond "
            "the roofline is deepening blue. NOTHING IN THIS PICTURE DEPICTS "
            "DEATH ITSELF: there is no body, no bier, no shroud, no grave, no "
            "tomb, no mourner and no departing shape of any kind — only a place "
            "somebody is no longer lying in."
        ),
    },
    {
        "id": "v2-r037-b14", "out": "s14-the-angels-carried-him.jpeg",
        "seg": "n5", "window": "37.950-42.050", "wide": True, "jesus": False,
        "locks": ["SPIRIT-WORLD", "BEARERS", "LAZARUS"], "char_refs": _LAZ,
        "narration": "Lazarus died — and the angels carried him home, to Abraham's side,",
        "must_show": "Two ordinary grown men carrying Lazarus carefully between them, seen from behind and above so that only their backs and shoulders are in view — walking away from the camera toward the deep tree shade and still water of the place of rest.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_INFERNO + _NO_CREAM + _NO_HALO + _NO_STIGMATA + _GAZE,
        "scene": (
            "GEOMETRY FIRST, BECAUSE IT GOVERNS THIS FRAME AND IS THE WHOLE "
            "REASON IT IS SAFE: THE CAMERA STANDS BEHIND AND ABOVE THE THREE "
            "FIGURES AND SHOOTS PAST THEM AS THEY WALK AWAY FROM IT. The two "
            "carrying men are seen ENTIRELY FROM BEHIND — backs, shoulders, the "
            "backs of their heads, their arms — and NOT ONE FACE IS IN THE "
            "PICTURE AT ALL, so a lens gaze is geometrically impossible and "
            "nothing above their shoulders can be invented. THEY HAVE NOTHING "
            "ON OR ABOVE THEIR BACKS: no wing, no feather, no pinion, no bright "
            "outline, no ring or disc of light around any head, and nothing "
            "rising from their shoulders — their backs are plain dark woven "
            "wool from collar to hem and their shoulder line is unbroken. "
            "One photograph, 35mm lens, soft even warm daylight coming from "
            "ahead and to the LEFT, filtered through the leaves of the trees "
            "they are walking toward, the light source out of frame and never "
            "behind any head, fine film grain, true depth of field. THE TWO "
            "CARRYING MEN are ordinary Judean men of about thirty-five and "
            "forty-five, of normal adult human height and build, one in a solid "
            "DEEP INDIGO ankle-length wool tunic and one in solid DARK UMBER, "
            "with plain leather sandals on real ground; they walk steadily side "
            "by side with real weight in their arms, their heads bowed slightly "
            "toward the man they carry, and they cast real shadows on the "
            "grass. Between and slightly below them they carry LAZARUS lying "
            "along their forearms, cradled and level, one man supporting his "
            "shoulders and the other his knees, his head turned in against the "
            "nearer man's chest and AWAY FROM THE CAMERA so his face is not in "
            "the picture. RESTATE HIS IDENTITY: SHORT dark brown hair cut close "
            "to the skull, visible at the crown and the nape and never reaching "
            "his shoulders, and ONE knee-length DARK UMBER-BROWN wool tunic, "
            "his bare feet hanging relaxed; he is whole, calm and at rest, "
            "solid and opaque with real weight, not floating, not translucent "
            "and giving off no light. Ahead of them the ground rises gently "
            "into the deep cool shade of broad real trees, with low green "
            "plants and one channel of still clear water lying open on the "
            "ground catching the light. THIS IS A WIDE FULL-LENGTH SCENE: the "
            "camera is far enough back that all three men are visible complete "
            "from head to sandals with the shade of the trees ahead of them."
        ),
    },
    {
        "id": "v2-r037-b15", "out": "s15-into-light-and-comfort.jpeg",
        "seg": "n5", "window": "42.050-44.708", "wide": True, "jesus": False,
        "locks": _REST, "char_refs": _ABE_LAZ,
        "narration": "into light and comfort at last.",
        "must_show": "Lazarus at rest in the place of rest — sitting on the ground in deep tree shade beside Abraham, clean, whole and unhurried, a clay cup of water in his hand and the still water lying open beside them.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_INFERNO + _NO_CREAM + _NO_HALO + _NO_STIGMATA + _GAZE,
        "scene": (
            "One photograph, 35mm lens, soft even dappled daylight coming down "
            "through the broad leaves of real trees from the upper LEFT, cool "
            "deep shade beneath, warm sunlit ground beyond, the light source "
            "out of frame and never behind any head, fine film grain, true "
            "depth of field. THE CAMERA STANDS BACK AND TO THE SIDE OF BOTH "
            "MEN, seeing them from the side in strict three-quarter view, and "
            "NOT ONE FACE IS TURNED TOWARD THE LENS: both men look at each "
            "other, their eyelines running LATERALLY ACROSS the frame between "
            "them and never out toward the camera. They sit on the bare "
            "ground on a hand-woven reed mat under the trees, ABRAHAM on the "
            "LEFT and LAZARUS on the RIGHT, close together, at ease, neither "
            "raised above the other and NEITHER SITTING ON ANY SEAT, CHAIR, "
            "BENCH, DAIS OR THRONE. RESTATE BOTH IDENTITIES: Abraham is a man "
            "of about eighty with warm olive-brown Middle Eastern skin, a LONG "
            "FULL SILVER-GREY BEARD to the middle of his chest and SILVER-GREY "
            "hair waving to his shoulders, in ONE DEEP INDIGO-BLUE ankle-length "
            "tunic under ONE DARK OLIVE-GREEN rectangular mantle with ONE DEEP "
            "MAROON folded sash — never cream, off-white or any pale cloth — "
            "his expression grave, kind and unhurried, one bony hand resting "
            "open on his knee; Lazarus is the SAME MAN the viewer saw in the "
            "dust, unmistakably recognisable, with the same narrow face, the "
            "same SHORT dark brown hair cut close to the skull, the same SHORT "
            "ragged dark beard and the same ONE knee-length DARK UMBER-BROWN "
            "wool tunic — but now clean, mended, his skin no longer dust-grey, "
            "his shins and calves SMOOTH AND ENTIRELY UNMARKED with the sores "
            "simply gone, still thin but no longer starved, sitting upright and "
            "rested. He holds a plain unstemmed fired-clay cup of water in both "
            "hands, half raised. Beside them ONE channel of still clear water "
            "lies open along the ground, its surface unbroken and reflecting the "
            "leaves, with low green plants and soft grass along its edge. BOTH "
            "MEN ARE SOLID, OPAQUE AND FULLY CLOTHED, sitting with real weight "
            "on real ground and casting real shadows: neither floats, neither "
            "is translucent, and neither gives off light of any kind. THIS IS A "
            "WIDE FULL-LENGTH SCENE: the camera is far enough back that both "
            "men, the mat, the open water and the trunks of the trees are in "
            "frame together."
        ),
    },
    # ===== n6 — the rich man dies, is buried, and wakes ======================
    {
        "id": "v2-r037-b16", "out": "s16-died-too-and-was-buried.jpeg",
        "seg": "n6", "window": "44.708-47.480", "wide": True, "jesus": False,
        "locks": ["TOMBS", "JUDEAN-LAND", "BACKGROUND-CAST"],
        "narration": "The rich man died too, and was buried.",
        "must_show": "A first-century Judean burial on a dry hillside: a wrapped and bound form carried on a plain pole bier toward a square rock-cut tomb opening, the bearers seen from behind, the round sealing stone standing ready on edge beside it.",
        "must_not_show": _NO_FUNERAL + _NO_KITSCH + _NO_GHOST + _NO_INFERNO + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear flat midday sun from almost "
            "overhead and slightly RIGHT, bleaching the limestone and throwing "
            "short black shadows, the sun well out of frame and never behind "
            "any head, fine film grain, true depth of field. THE CAMERA STANDS "
            "ON THE HILLSIDE BEHIND THE BEARERS AND SHOOTS PAST THEM toward the "
            "rock face: FOUR dark-clad men fill the near lower half of the "
            "frame as heads, shoulders and BACKS seen entirely FROM BEHIND, "
            "walking AWAY from the camera, and NOT ONE FACE IS TURNED TOWARD "
            "THE LENS. Every one of them is dressed head to foot in ONE SOLID "
            "DARK SATURATED EARTH COLOUR — dark umber, charcoal, deep rust or "
            "deep indigo — and not one wears cream, off-white or any pale "
            "cloth. On their shoulders they carry a plain BIER of two hewn "
            "poles with woven palm-fibre webbing lashed between them, and lying "
            "on it a form ENTIRELY WRAPPED AND BOUND head to foot in plain DARK "
            "hand-woven wool cloth tied round with cord at intervals, with NO "
            "PART OF THE BODY, no face, no hand and no foot showing anywhere. "
            "Ahead of them a low bare limestone scarp runs across the frame "
            "with ONE plain SQUARE opening about waist high cut straight into "
            "the rock face, dark inside, its edges rough and chisel-marked, and "
            "standing on edge in a shallow channel cut along the rock beside it "
            "ONE large ROUND FLAT DISC OF UNDRESSED LIMESTONE ready to be "
            "rolled across. The ground is bare trodden dust, loose chippings, "
            "grey-green thorn scrub and dead sun-bleached grass, with bare dry "
            "rounded hills hazy behind. THIS IS A WIDE FULL-LENGTH SCENE: the "
            "camera is far enough back that all four bearers, the whole bier "
            "and the rock face with its opening are in frame together. NOTHING "
            "IN THIS PICTURE IS A LATER FUNERAL: no coffin, casket, headstone, "
            "cross, carved memorial, flowers, dug pit or heap of loose earth."
        ),
    },
    {
        "id": "v2-r037-b17", "out": "s17-he-opened-his-eyes.jpeg",
        "seg": "n6", "window": "47.480-50.340", "wide": False, "jesus": False,
        "locks": _TORMENT, "char_refs": _RICH,
        "narration": "But he opened his eyes in a place of torment:",
        "must_show": "The rich man's face at the instant of waking in the place of torment — a tight side-on profile, eyes screwed half open against a hard white glare, dust on his skin, the same purple mantle now dishevelled. All of it carried on his face.",
        "must_not_show": _NO_INFERNO + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _NO_MOCK + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: his head is in EXACT RIGHT-FACING PROFILE to the camera, "
            "his brow, nose, lips and chin drawn cleanly against the bright "
            "empty ground beyond. THE FAR CHEEK AND THE FAR EYE ARE HIDDEN "
            "behind the bridge of his nose and are not in the picture at all, "
            "so a lens gaze is geometrically impossible. His near eye is barely "
            "open, screwed up against the light, and looks straight ahead along "
            "his own profile line and out through the RIGHT EDGE. "
            "One photograph, 85mm lens, a TIGHT frame of head and shoulders "
            "only, hard flat scorching overhead daylight from the upper RIGHT "
            "AND IN FRONT of him, colourless and glaring, striking the front "
            "planes of his face and leaving the back of his head unlit and "
            "dark, the light source never behind his head, fine film grain, "
            "very shallow depth of field. HE IS ALONE IN THE FRAME and no other "
            "person, shoulder, arm, head or blurred body appears anywhere in "
            "it, at any edge. HE IS PROPPED ON ONE ELBOW ON BARE CRACKED "
            "SUN-BAKED CLAY, just risen onto it, the ground pressing into his "
            "forearm. RESTATE HIS IDENTITY: warm olive-brown clearly Middle "
            "Eastern skin, a full thick trimmed dark brown beard squared at the "
            "jaw with a little grey at the chin, and thick dark brown wavy hair "
            "cut to the middle of the neck, now disordered and grey with dust "
            "at the temple. He wears the SAME clothes the viewer has already "
            "seen him in — the DEEP TYRIAN PURPLE mantle, now dragged askew off "
            "the shoulder, dulled and caked with pale dust, over the SATURATED "
            "SAFFRON-GOLD tunic, its collar dark with sweat — the same "
            "garments worn out of their glory, which is how the viewer knows "
            "him. HIS FACE CARRIES THE WHOLE OF IT: dry cracked lips slightly "
            "parted, a bead of sweat at the temple cutting a track through the "
            "dust, the tendons of his neck standing, his brow drawn hard down "
            "against the glare — bewilderment and dawning fear, not rage and "
            "not caricature; he keeps his human dignity. Behind him the "
            "background is nothing but hot bare empty ground and a burning "
            "white sky shimmering with heat haze, thrown far out of focus. "
            "THERE IS NO FIRE, FLAME, EMBER, SMOKE, RED LIGHT OR BURNING "
            "OBJECT ANYWHERE IN THE FRAME — the heat is in the light, the "
            "shimmer, the dust and his own skin."
        ),
    },
    {
        "id": "v2-r037-b18", "out": "s18-a-dark-and-thirsty-place.jpeg",
        "seg": "n6", "window": "50.340-53.969", "wide": True, "jesus": False,
        "locks": _TORMENT, "char_refs": _RICH,
        "narration": "a dark and thirsty place, far from the light.",
        "must_show": "The full width of the place of torment: bare cracked ground running flat and empty to a far horizon under a burning white sky, and the rich man alone in the middle of it, small against the emptiness. The isolation IS the torment.",
        "must_not_show": _NO_INFERNO + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 24mm wide lens, hard flat scorching overhead "
            "daylight, colourless and glaring, shadows short and black beneath "
            "everything, the air shimmering with heat haze and hanging dust, "
            "the sun itself out of frame, fine film grain, deep focus "
            "throughout. THE CAMERA STANDS WELL BACK AND SLIGHTLY ABOVE AND "
            "BEHIND THE MAN AND SHOOTS PAST HIM out across the emptiness: he is "
            "seen from behind and to one side, three-quarter FROM BEHIND, "
            "standing small and alone at the lower left of a very wide frame, "
            "and NO FACE IS TURNED TOWARD THE LENS. BECAUSE THE CAMERA IS "
            "BEHIND HIS HEAD, HIS HAIR IS STATED HERE: thick dark brown wavy "
            "hair cut to the middle of the neck, disordered and dust-grey, "
            "clear against the DEEP TYRIAN PURPLE mantle dragging from his "
            "shoulder over the SATURATED SAFFRON-GOLD tunic. He stands with his "
            "head slightly bowed and one hand raised to shield his eyes, "
            "looking out and away from the camera across the ground. HE IS THE "
            "ONLY PERSON IN THE ENTIRE PICTURE: no other figure, shoulder, "
            "head, silhouette or blurred body appears anywhere in it, near or "
            "far, in focus or out of focus, and the emptiness around him is "
            "total and is the whole subject of the frame. THE GROUND runs flat "
            "and unbroken away from him to a far horizon — bare sun-baked clay "
            "cracked into a wide pattern of curling plates, drifted grit, and "
            "scattered bleached broken stone — WITH NO WATER, NO SHADE, NO "
            "SHELTER, NO TREE, NO PLANT, NO BUILDING AND NO ROAD ANYWHERE IN "
            "IT. Above it a burning white sky, colourless with heat, with no "
            "cloud and no sun disc. THIS IS A WIDE FULL-LENGTH SCENE: the "
            "camera is far enough back that the man is visible complete from "
            "head to sandals and reads as small against the size of the empty "
            "land. THERE IS NO FIRE, FLAME, EMBER, SMOKE, BURNING GROUND, "
            "MOLTEN FISSURE OR RED LIGHT ANYWHERE IN THE PICTURE, and no cave, "
            "pit, opening or descent of any kind: the torment is the heat, the "
            "thirst, the glare and the absolute emptiness around one man."
        ),
    },
]

BEATS += [
    # ===== j3 — Luke 16:24, THE RICH MAN speaking (RED) ======================
    {
        "id": "v2-r037-b19", "out": "s19-father-abraham-have-mercy.jpeg",
        "seg": "j3", "window": "53.969-56.480", "wide": False, "jesus": False,
        "locks": _TORMENT, "char_refs": _RICH,
        "narration": "Father Abraham, have mercy on me,",
        "must_show": "The rich man calling out across the emptiness — a tight side-on profile, mouth open on the shout, one hand raised, his whole body turned toward something impossibly far away.",
        "must_not_show": _NO_INFERNO + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _NO_MOCK + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: his head and shoulders are in EXACT LEFT-FACING PROFILE to "
            "the camera, his brow, nose, open mouth and chin drawn cleanly "
            "against the bright empty distance. THE FAR CHEEK AND THE FAR EYE "
            "ARE HIDDEN behind the bridge of his nose and are not in the "
            "picture at all, so a lens gaze is geometrically impossible. His "
            "near eye is narrowed against the glare and fixed on something far "
            "off, and his eyeline runs level and out through the LEFT EDGE. "
            "One photograph, 85mm lens, a TIGHT frame of head, shoulders and "
            "one raised forearm, hard flat scorching daylight from the upper "
            "LEFT AND IN FRONT of him, colourless and glaring, catching the "
            "front planes of his face and leaving the back of his head unlit, "
            "the light source never behind his head, fine film grain, very "
            "shallow depth of field. HE IS ALONE IN THE FRAME and no other "
            "person, shoulder, arm or blurred body appears anywhere in it. His "
            "mouth is OPEN ON A SHOUT, the jaw dropped and the neck tendons "
            "standing hard, his chin lifted; his near hand is raised open-"
            "palmed beside his face, reaching out toward the distance he is "
            "calling to. RESTATE HIS IDENTITY: warm olive-brown clearly Middle "
            "Eastern skin, a full thick trimmed dark brown beard squared at the "
            "jaw, thick dark brown wavy hair cut to the middle of the neck now "
            "disordered and grey with dust, the DEEP TYRIAN PURPLE mantle "
            "dragged askew and dust-caked over the SATURATED SAFFRON-GOLD "
            "tunic. His face is desperate but NOT grotesque, NOT contorted into "
            "a mask, NOT screaming in agony and NOT a caricature — it is a man "
            "calling out to someone he knows, and there is grief in it. "
            "Behind him the background is nothing but hot bare cracked ground "
            "and burning white sky shimmering with heat, thrown far out of "
            "focus. THERE IS NO FIRE, FLAME, EMBER, SMOKE OR BURNING THING "
            "ANYWHERE IN THE FRAME."
        ),
    },
    {
        "id": "v2-r037-b20", "out": "s20-send-lazarus-the-tip-of-his-finger.jpeg",
        "seg": "j3", "window": "56.480-61.160", "wide": False, "jesus": False,
        "locks": _REST, "char_refs": _ABE_LAZ,
        "narration": "and send Lazarus, that he may dip the tip of his finger in water,",
        "must_show": "The thing he is asking for, shown as the small ordinary thing it is: one man's hand at the edge of the still water in the place of rest, one fingertip breaking the surface, a single bead of water on it.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_INFERNO + _NO_CREAM + _NO_HALO + _NO_STIGMATA + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, a VERY CLOSE frame of one human "
            "hand at the edge of open water, soft cool dappled daylight coming "
            "down through leaves from the upper LEFT, fine film grain, very "
            "shallow depth of field with everything beyond the hand thrown soft. "
            "NO FACE IS IN THIS PICTURE AT ALL — the frame holds a hand, a "
            "wrist and a cuff and nothing above them — so a lens gaze is "
            "geometrically impossible. THE HAND IS A GROWN MAN'S HAND, thin, "
            "sinewy and clean, of ordinary adult male size and clearly "
            "male-scaled against the width of the water channel, its skin warm "
            "sun-darkened olive-brown; it reaches down from the upper right and "
            "ONE SINGLE INDEX FINGERTIP just breaks the surface of the water, "
            "dimpling it into two or three fine rings that spread out across "
            "the frame, ONE clear bead of water standing on the fingertip "
            "itself. THE HAND IS ENTIRELY UNMARKED: no cut, wound, hole, scar, "
            "blood, bandage or dressing anywhere on the palm, the back of the "
            "hand or the wrist. AT THE WRIST, FILLING THE UPPER RIGHT CORNER OF "
            "THE FRAME EDGE TO EDGE, is the straight unshaped cuff of a coarse "
            "hand-woven DARK UMBER-BROWN wool sleeve, and BECAUSE THIS IS A "
            "CLOSE MACRO THE WEAVE IS RESTATED HERE: a clear slightly irregular "
            "over-and-under grid of warp and weft threads on a flat matte "
            "surface with a plain frayed cut edge — never knitted, never "
            "ribbed, never a stretchy cuff, never felted, brushed or napped. "
            "THE NEAR FOREGROUND AND THE LOWER HALF OF THE FRAME ARE FILLED "
            "EDGE TO EDGE by the still clear water itself, dark and glassy, "
            "with the soft green of leaves reflected in it and pale rounded "
            "pebbles and fine sand visible under the surface at the near edge. "
            "The water is COOL, CLEAN AND ORDINARY: it does not shine, sparkle "
            "unnaturally, steam or give off light of any kind."
        ),
    },
    {
        "id": "v2-r037-b21", "out": "s21-and-cool-my-tongue.jpeg",
        "seg": "j3", "window": "61.160-63.140", "wide": False, "jesus": False,
        "locks": _TORMENT, "char_refs": _RICH,
        "narration": "and cool my tongue;",
        "must_show": "A very close frame of the rich man's own dry cracked mouth and jaw in profile — thirst shown on the body, nothing else in the picture.",
        "must_not_show": _NO_INFERNO + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, a VERY CLOSE frame holding only "
            "the lower half of a man's face in STRICT LEFT-FACING PROFILE — "
            "mouth, chin, jaw, the near cheek and the edge of the beard — cut "
            "off above the nose so that NO EYE IS IN THE PICTURE AT ALL and a "
            "lens gaze is geometrically impossible. Hard flat scorching "
            "daylight comes from the upper LEFT AND IN FRONT, raking across the "
            "skin, the light source never behind his head, fine film grain, "
            "very shallow depth of field. HE IS ALONE IN THE FRAME and no other "
            "person or blurred body appears anywhere in it. THE SKIN AND THE "
            "MOUTH CARRY THE WHOLE PICTURE: warm olive-brown clearly Middle "
            "Eastern skin filmed with pale dust and running with sweat at the "
            "jaw, the lips DRY AND CRACKED and slightly parted, the lower lip "
            "split in one fine line, the tongue just visible and dry against "
            "the teeth, the beard — full, thick, trimmed and dark brown, greyed "
            "at the chin — matted with dust. At the bottom edge of the frame "
            "the collar of the SATURATED SAFFRON-GOLD tunic and the edge of the "
            "DEEP TYRIAN PURPLE mantle fill the lower corners, dulled and "
            "dust-caked, and BECAUSE THIS IS A CLOSE MACRO THEIR WEAVE IS "
            "RESTATED HERE: a flat matte loom-woven surface showing a clear "
            "slightly irregular over-and-under grid of warp and weft threads — "
            "never knitted, ribbed, satin, velvet, shiny or napped. Behind, the "
            "burning white sky is thrown completely soft. THERE IS NO FIRE, "
            "FLAME, EMBER, SMOKE OR BURNING THING ANYWHERE IN THE FRAME, and "
            "there is no blood anywhere on the mouth."
        ),
    },
    {
        "id": "v2-r037-b22", "out": "s22-tormented-in-this-flame.jpeg",
        "seg": "j3", "window": "63.140-66.810", "wide": True, "jesus": False,
        "locks": _TORMENT, "char_refs": _RICH,
        "narration": "for I am tormented in this flame.",
        "must_show": "What 'this flame' actually is in this staging: the scorching air itself. The man small and alone on the cracked ground under a white sky, the whole frame distorted by heat shimmer — and no fire anywhere.",
        "must_not_show": _NO_INFERNO + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 200mm long lens compressing the distance, shot "
            "through a heavy layer of rising heat haze so the whole picture "
            "ripples and wavers, hard flat colourless overhead daylight, the "
            "sun out of frame, fine film grain. THE CAMERA STANDS FAR BACK AND "
            "LOW AND SHOOTS PAST THE MAN toward the horizon: he is seen from "
            "the side and slightly BEHIND, standing small in the middle "
            "distance at the right of frame, and NO FACE IS TURNED TOWARD THE "
            "LENS — his head is turned away toward the horizon and his eyeline "
            "exits through the RIGHT EDGE. He stands with his shoulders "
            "dropped, one arm hanging, the DEEP TYRIAN PURPLE mantle trailing "
            "from one shoulder over the SATURATED SAFFRON-GOLD tunic, both "
            "dulled to the colour of the dust; his dark brown hair, cut to the "
            "middle of the neck, is clear against the bright ground. HE IS THE "
            "ONLY PERSON IN THE ENTIRE PICTURE and no other figure, "
            "silhouette or blurred body appears anywhere in it, near or far. "
            "THE HEAT IS THE SUBJECT AND IT IS STATED AS OPTICS, NOT AS FIRE: "
            "the air between the camera and the man BOILS with shimmer, the "
            "horizon line breaks up and floats, a false mirage of water lies "
            "along the far distance and dissolves, and everything beyond the "
            "middle distance wavers and smears. THE GROUND is bare sun-baked "
            "clay cracked into curling plates, drifted grit and bleached broken "
            "stone, running flat and empty to the horizon with no water, no "
            "shade, no tree, no plant and no building. Above it a burning white "
            "sky with no cloud and no sun disc. THIS IS A WIDE FULL-LENGTH "
            "SCENE: the camera is far enough back that the man is visible "
            "complete from head to sandals and reads as very small against the "
            "emptiness. ABSOLUTELY NO FIRE APPEARS IN THIS PICTURE: no flame, "
            "no ember, no coal, no smoke, no burning ground, no molten fissure, "
            "no red or orange light, no torch and nothing alight of any kind — "
            "the burning is entirely in the air, the glare and the dust."
        ),
    },
    # ===== n7 — he sees across the gulf ======================================
    {
        "id": "v2-r037-b23", "out": "s23-across-a-vast-divide.jpeg",
        "seg": "n7", "window": "66.810-70.460", "wide": True, "jesus": False,
        "locks": _TORMENT, "char_refs": _RICH,
        "narration": "Across a vast divide he could see Abraham in the distance,",
        "must_show": "The great gulf itself for the first time: an enormous dry rock chasm splitting the ground, the man standing small at the near lip of it, and the far side visible across the emptiness as a distant line of green shade — small and hazy with sheer distance.",
        "must_not_show": _NO_INFERNO + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 24mm wide lens, hard flat colourless overhead "
            "daylight on the near side, the far side softer and hazier with "
            "distance, the sun out of frame, fine film grain, deep focus "
            "throughout. THE CAMERA STANDS WELL BACK AND ABOVE AND BEHIND THE "
            "MAN AND SHOOTS PAST HIM ACROSS THE CHASM: he is seen entirely FROM "
            "BEHIND, small at the lower left of a very wide frame, standing at "
            "the near lip, and NO FACE IS IN THE PICTURE AT ALL. BECAUSE THE "
            "CAMERA IS BEHIND HIS HEAD, HIS HAIR IS STATED HERE: thick dark "
            "brown wavy hair cut to the middle of the neck, disordered and "
            "dust-grey, clear against the DEEP TYRIAN PURPLE mantle over the "
            "SATURATED SAFFRON-GOLD tunic. His arms hang at his sides and he "
            "simply looks out across. THE GULF FILLS THE MIDDLE OF THE FRAME "
            "AND IS PLAIN GEOLOGY: an enormous DRY CHASM of bare stratified "
            "rock splitting the land from one side of the picture to the other, "
            "its near lip crumbling into scree, its walls dropping away in "
            "banded limestone ledges into deep blue shadow far below where the "
            "bottom is lost in darkness, its width so great that the far wall "
            "is small and softened by distance. IT IS NOT A WALL, A FENCE, A "
            "BARRIER, A BRIDGE, A CURTAIN OR A VEIL, THERE IS NOTHING BUILT "
            "ANYWHERE IN IT, AND THERE IS NO FIRE, SMOKE, MOLTEN FISSURE, LAVA "
            "OR RED LIGHT IN ITS DEPTHS — it is dry rock, dust and shadow. THE "
            "NEAR SIDE where the man stands is bare cracked sun-baked clay and "
            "bleached broken stone under a burning white sky. THE FAR SIDE, "
            "small and hazy with sheer distance across the top third of the "
            "frame, is a low green line of real trees in deep shade with the "
            "glint of open water in it — clearly the same place of rest, "
            "clearly the same real world, and clearly impossibly far away. TWO "
            "TINY SEATED FIGURES are just readable there among the trees, far "
            "too distant for any feature to be made out, one in deep indigo and "
            "one in dark umber. THIS IS A WIDE FULL-LENGTH SCENE: the camera is "
            "far enough back that the standing man is visible complete and "
            "reads as small against the size of the chasm."
        ),
    },
    {
        "id": "v2-r037-b24", "out": "s24-lazarus-resting-beside-him.jpeg",
        "seg": "n7", "window": "70.460-72.880", "wide": False, "jesus": False,
        "locks": _REST, "char_refs": _ABE_LAZ,
        "narration": "with Lazarus resting beside him.",
        "must_show": "The far side seen close: Lazarus resting easily on the ground beside Abraham in the deep shade, the two of them near and quiet together — the nearness itself is the point.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_INFERNO + _NO_CREAM + _NO_HALO + _NO_STIGMATA + _GAZE,
        "scene": (
            "One photograph, 85mm lens, soft cool dappled daylight falling "
            "through broad real leaves from the upper RIGHT, deep green shade "
            "beneath, warm sunlit ground beyond and out of focus, the light "
            "source out of frame and never behind any head, fine film grain, "
            "shallow depth of field. THE CAMERA STANDS TO THE SIDE OF BOTH MEN "
            "AND SLIGHTLY BEHIND THE NEARER ONE, so both are seen in strict "
            "side view and NOT ONE FACE IS TURNED TOWARD THE LENS: neither man "
            "is speaking, both are simply at rest, and their eyelines run "
            "LATERALLY ACROSS the frame or down at the ground, never out toward "
            "the camera. LAZARUS is nearer the camera on the RIGHT, seen in "
            "left-facing profile, sitting back on the ground on a hand-woven "
            "reed mat with one knee drawn up and his weight on one hand behind "
            "him, his head tipped back a little against the trunk of a tree, "
            "his eyes half closed and easy. RESTATE HIS IDENTITY: the SAME MAN "
            "the viewer saw lying in the dust — warm sun-darkened olive-brown "
            "Middle Eastern skin, a narrow face, the same SHORT ragged dark "
            "brown beard, the same SHORT dark brown hair cut close to the skull "
            "and never reaching his shoulders, the same ONE knee-length DARK "
            "UMBER-BROWN coarse wool tunic with a twisted flax cord — now "
            "clean, mended and unstained, his skin no longer dust-grey, and his "
            "drawn-up SHIN AND CALF SMOOTH AND ENTIRELY UNMARKED with the sores "
            "simply gone. His hands, wrists and the tops of his bare feet are "
            "unmarked. ABRAHAM sits a little beyond him on the LEFT, seen in "
            "three-quarter from behind, his LONG FULL SILVER-GREY BEARD and "
            "SILVER-GREY shoulder-length hair clear against his DARK "
            "OLIVE-GREEN mantle over his DEEP INDIGO-BLUE tunic, one bony hand "
            "resting on his own knee, his head turned down and away toward the "
            "ground. NEITHER MAN SITS ON ANY SEAT, CHAIR, BENCH, DAIS OR "
            "THRONE, both sit on the bare ground, both are solid, opaque and "
            "fully clothed with real weight and real shadows, and neither "
            "floats, is translucent or gives off light. Beside them the still "
            "clear water lies open along the ground and low green plants grow "
            "at its edge."
        ),
    },
    {
        "id": "v2-r037-b25", "out": "s25-begging-for-a-drop-of-water.jpeg",
        "seg": "n7", "window": "72.880-77.693", "wide": True, "jesus": False,
        "locks": _TORMENT, "char_refs": _RICH,
        "narration": "And he cried out, begging for just a drop of water to cool his tongue.",
        "must_show": "The rich man at the very lip of the chasm, leaning out and calling across with both hands raised — the enormous empty air in front of him carrying how hopeless the distance is.",
        "must_not_show": _NO_INFERNO + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard flat colourless overhead daylight, "
            "the sun out of frame and never behind his head, fine film grain, "
            "true depth of field. THE CAMERA STANDS BEHIND AND TO THE RIGHT OF "
            "THE MAN, ON THE SAME LIP OF ROCK, AND SHOOTS PAST HIM out over the "
            "chasm: he is seen in three-quarter FROM BEHIND, full length, and "
            "NO FACE IS TURNED TOWARD THE LENS — the camera sees the back and "
            "side of his head only, and his shout goes away from the lens into "
            "the empty air. BECAUSE THE CAMERA IS BEHIND HIS HEAD, HIS HAIR IS "
            "STATED HERE: thick dark brown wavy hair cut to the middle of the "
            "neck, disordered and dust-grey, clear against the DEEP TYRIAN "
            "PURPLE mantle dragging from his shoulder over the SATURATED "
            "SAFFRON-GOLD tunic. THE ACTION MUST READ CORRECTLY AT A GLANCE: he "
            "stands right at the crumbling edge, his weight forward on his "
            "front foot with the rock dropping away immediately beyond his "
            "sandals, BOTH ARMS RAISED AND OPEN toward the far side, his head "
            "thrown back and his jaw dropped on a shout, the tendons of his "
            "neck standing — a man calling with everything he has across a "
            "distance he already knows is too great. HE IS NOT FALLING, NOT "
            "JUMPING, NOT CLIMBING DOWN AND NOT BEING PUSHED. HE IS THE ONLY "
            "PERSON IN THE PICTURE and no other figure, hand or blurred body "
            "appears anywhere in it. THE NEAR FOREGROUND AND THE LOWER CORNERS "
            "ARE FILLED EDGE TO EDGE by the broken bleached limestone of the "
            "lip itself, cracked, dusty and scattered with loose scree. Beyond "
            "him the chasm opens as bare stratified dry rock falling away into "
            "deep blue shadow, and far across it, small and hazy with distance, "
            "the low green line of trees in shade. THIS IS A WIDE FULL-LENGTH "
            "SCENE: the camera is far enough back that the man is visible "
            "complete from head to sandals against the width of the gulf. THERE "
            "IS NO FIRE, FLAME, SMOKE, MOLTEN FISSURE OR RED LIGHT ANYWHERE IN "
            "THE FRAME."
        ),
    },
    # ===== j1 — Luke 16:25, ABRAHAM speaking (RED) ===========================
    {
        "id": "v2-r037-b26", "out": "s26-son-remember.jpeg",
        "seg": "j1", "window": "77.693-82.240", "wide": False, "jesus": False,
        "locks": _REST, "char_refs": _ABE,
        "narration": "Son, remember that thou in thy lifetime receivedst thy good things,",
        "must_show": "Abraham answering — a strict side-on profile of an old man's grave, sorrowful, compassionate face as he speaks across the distance. He calls the man 'Son' and his expression must carry that.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_INFERNO + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: his head is in EXACT RIGHT-FACING PROFILE to the camera, "
            "his brow, nose, lips and the long fall of his beard drawn cleanly "
            "against the soft green shade behind him. THE FAR CHEEK AND THE FAR "
            "EYE ARE HIDDEN behind the bridge of his nose and are not in the "
            "picture at all, so a lens gaze is geometrically impossible. His "
            "near eye looks level and far off along his own profile line and "
            "exits through the RIGHT EDGE. "
            "One photograph, 85mm lens, a frame of head and shoulders and the "
            "top of the chest, soft cool dappled daylight falling through "
            "leaves from the RIGHT AND IN FRONT of him, modelling the front "
            "planes of his face and leaving the back of his head in green "
            "shade, the light source never behind his head, fine film grain, "
            "very shallow depth of field with the trees thrown soft behind. HE "
            "IS ALONE IN THE FRAME and no other person, shoulder, arm, head or "
            "blurred body appears anywhere in it, at any edge. RESTATE HIS "
            "IDENTITY IN THIS FRAME: a man of about eighty with warm "
            "olive-brown clearly Middle Eastern skin deeply lined across the "
            "forehead and around the eye, a LONG FULL SILVER-GREY BEARD "
            "reaching the middle of his chest, and THICK SILVER-GREY HAIR "
            "falling in waves to his shoulders from a high lined forehead, with "
            "a clear band of that silver hair at the temple and the nape; his "
            "head is BARE and he wears nothing on it — no turban, no cap, no "
            "crown, no diadem and no wreath. He wears ONE DEEP INDIGO-BLUE "
            "tunic with a straight unshaped sleeve, under ONE DARK OLIVE-GREEN "
            "rectangular mantle over the shoulder, with the edge of ONE DEEP "
            "MAROON folded sash just visible — never cream, off-white, ivory or "
            "any pale cloth anywhere on him. HIS EXPRESSION IS THE SUBJECT: "
            "grave, compassionate and deeply sorrowful, his brow drawn, his "
            "mouth open mid-word, his chin a little lowered — he is grieving "
            "for the man he is answering and he is NEVER angry, NEVER stern, "
            "NEVER triumphant, NEVER condemning and NEVER scolding. He carries "
            "NO wing, NO feather, NO bright ring around his head and no light "
            "of any kind coming off him, and he is solid, opaque and casts a "
            "real shadow."
        ),
    },
    {
        "id": "v2-r037-b27", "out": "s27-and-likewise-lazarus-evil-things.jpeg",
        "seg": "j1", "window": "82.240-85.100", "wide": False, "jesus": False,
        "locks": _GATE + ["LAZARUS"], "char_refs": _LAZ,
        "narration": "and likewise Lazarus evil things.",
        "must_show": "A remembered image of the old life: Lazarus back at the foot of the wall in the dust and the cold blue shadow, thin and hungry — the 'evil things' of his lifetime, shown as the plain hard fact it was.",
        "must_not_show": _NO_STIGMATA + _NO_MOCK + _NO_CREAM + _NO_HALO + _NO_IRONGATE + _NO_KITSCH + _GAZE,
        "scene": (
            "One photograph, 50mm lens, the cold flat blue light of very early "
            "morning before the sun has reached the lane, no direct sunlight on "
            "anything, the light soft and shadowless and coming from the open "
            "sky above, fine film grain, shallow depth of field. THE CAMERA "
            "STANDS ABOVE AND SLIGHTLY BEHIND THE MAN, LOOKING DOWN AND ALONG "
            "THE WALL, so he is seen from behind and above in three-quarter and "
            "NO FACE IS TURNED TOWARD THE LENS — his head is turned down and "
            "away toward his own drawn-up knees and his eyeline exits through "
            "the LOWER LEFT of the frame. BECAUSE THE CAMERA IS BEHIND AND "
            "ABOVE HIS HEAD, HIS HAIR IS STATED HERE: SHORT dark brown hair cut "
            "close to the skull, matted flat and grey with dust, clearly "
            "visible at the crown and the nape and never reaching his "
            "shoulders. HE IS ALONE IN THE FRAME and no other person, shoulder, "
            "arm, head or blurred body appears anywhere in it; the lane beyond "
            "him is empty. He sits huddled at the foot of the plastered "
            "mud-brick wall with his knees drawn up against his chest and both "
            "thin arms wrapped around them for warmth, his shoulders hunched, "
            "ONE knee-length DARK UMBER-BROWN coarse wool tunic pulled tight, "
            "frayed at the hem, a twisted flax cord at his waist, bare "
            "hard-soled dust-grey feet drawn in. His visible shin carries the "
            "same scatter of small DRY HEALED-OVER brick-red sores, closed and "
            "not bleeding; his hands, wrists and the tops of his feet are "
            "entirely unmarked. THE NEAR FOREGROUND AND THE LOWER THIRD ARE "
            "FILLED EDGE TO EDGE by the bare packed dust of the lane and an "
            "empty shallow fired-clay bowl lying on its side beside him with "
            "nothing in it. Behind him the dressed limestone jamb of the "
            "gateway stands in soft focus and the opening beyond is dark. THE "
            "PICTURE IS PLAIN AND UNSENTIMENTAL: he is cold and hungry and he "
            "keeps his dignity — never grotesque, never comic, never cowering "
            "and never pitiable as a spectacle."
        ),
    },
    {
        "id": "v2-r037-b28", "out": "s28-now-comforted-thou-tormented.jpeg",
        "seg": "j1", "window": "85.100-89.915", "wide": True, "jesus": False,
        "locks": _REST, "char_refs": _ABE_LAZ,
        "narration": "But now he is comforted, and thou art tormented.",
        "must_show": "The comfort itself, plainly: Abraham's old hand resting on Lazarus's shoulder as the two sit together in the shade — an ordinary human kindness, which is the whole meaning of 'comforted'.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_INFERNO + _NO_CREAM + _NO_HALO + _NO_STIGMATA + _GAZE,
        "scene": (
            "One photograph, 50mm lens, soft cool dappled daylight falling "
            "through broad real leaves from the upper LEFT, deep green shade "
            "beneath, the light source out of frame and never behind any head, "
            "fine film grain, true depth of field. THE CAMERA STANDS BEHIND AND "
            "TO THE SIDE OF BOTH SEATED MEN AND SHOOTS PAST THEM out toward the "
            "open water and the sunlit ground beyond: both men are seen from "
            "behind and from the side as backs, shoulders and the sides of "
            "their heads, and NOT ONE FACE IS TURNED TOWARD THE LENS. They sit "
            "side by side on the bare ground on a hand-woven reed mat, ABRAHAM "
            "on the LEFT and LAZARUS on the RIGHT, close enough to touch, both "
            "looking out and away from the camera across the water. RESTATE "
            "BOTH IDENTITIES, AND BOTH ARE SEEN LARGELY FROM BEHIND SO THEIR "
            "HAIR IS STATED: Abraham has THICK SILVER-GREY HAIR falling in "
            "waves to his shoulders and a LONG FULL SILVER-GREY BEARD whose "
            "edge shows past his cheek, above ONE DARK OLIVE-GREEN mantle over "
            "ONE DEEP INDIGO-BLUE tunic; Lazarus has SHORT dark brown hair cut "
            "close to the skull, clearly visible at the crown and the nape and "
            "never reaching his shoulders, a SHORT ragged dark beard whose edge "
            "shows past his cheek, and ONE knee-length DARK UMBER-BROWN wool "
            "tunic, clean and mended. NEITHER WEARS CREAM, OFF-WHITE OR ANY "
            "PALE CLOTH. THE ACTION IS THE WHOLE PICTURE AND IT MUST READ AT A "
            "GLANCE: ABRAHAM'S NEAR HAND — old, large, bony, veined and spotted "
            "with age — RESTS OPEN AND FLAT ON LAZARUS'S NEARER SHOULDER, the "
            "fingers relaxed over the coarse dark wool, the weight of it "
            "visible in the slight give of the cloth. It is a plain steadying "
            "hand of ordinary human kindness: he is not gripping him, not "
            "pulling him, not blessing him with a raised palm, not ordaining "
            "him and not pointing. Lazarus's shoulders are dropped and easy "
            "under it. NEITHER MAN SITS ON ANY SEAT, BENCH, DAIS OR THRONE, "
            "both sit on the ground, both are solid, opaque, fully clothed and "
            "cast real shadows, and neither floats or gives off light. Beyond "
            "them the still clear water lies open and bright, low green plants "
            "grow along its edge and the broad shade of the trees closes over "
            "the frame. THIS IS A WIDE FULL-LENGTH SCENE: the camera is far "
            "enough back that both seated men, the mat and the open water are "
            "in frame together."
        ),
    },
    # ===== j4 — Luke 16:26, ABRAHAM speaking (RED) ===========================
    {
        "id": "v2-r037-b29", "out": "s29-a-great-gulf-fixed.jpeg",
        "seg": "j4", "window": "89.915-93.960", "wide": True, "jesus": False,
        "locks": ["SPIRIT-WORLD"],
        "narration": "Between us and you there is a great gulf fixed:",
        "must_show": "The gulf shown whole and empty of people, from high above and along its length — an enormous dry rock chasm dividing green shade on one side from bare scorched ground on the other, so that the fixedness of it is simply obvious.",
        "must_not_show": _NO_INFERNO + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 24mm wide lens from a high vantage, hard clear "
            "daylight from the LEFT with the near wall of the chasm in shadow "
            "and the far country hazy with distance, the sun out of frame, fine "
            "film grain, deep focus throughout. A LANDSCAPE FRAME WITH NO "
            "PERSON IN IT ANYWHERE — no figure, silhouette, shoulder or blurred "
            "body appears at any point in this picture, near or far, and the "
            "land itself is the entire subject. THE CAMERA LOOKS DOWN AND ALONG "
            "THE CHASM FROM ABOVE ONE SHOULDER OF ROCK, so it runs away from "
            "the near foreground into the distance and both of its sides are "
            "visible at once. THE GULF IS PLAIN GEOLOGY AND IS STATED PIECE BY "
            "PIECE: an enormous dry rift splitting the land, its walls bare "
            "stratified limestone in horizontal bands of tan, grey and ochre, "
            "stepping down in broken ledges and scree fans into deep blue "
            "shadow far below where the floor is lost in darkness; its width "
            "is so great that the far rim reads as a distant line and the "
            "country beyond it is softened by haze. ON THE FAR SIDE the ground "
            "carries a low band of deep green — real broad-leaved trees in "
            "shade and the glint of open water among them. ON THE NEAR SIDE, "
            "filling the whole near foreground edge to edge, the ground is bare "
            "sun-baked clay cracked into curling plates, drifted grit and "
            "bleached broken stone running back to a burning white horizon, "
            "with no water, no shade, no tree and no plant in it. THE TWO "
            "COUNTRIES ARE OBVIOUSLY THE SAME WORLD, obviously divided, and "
            "obviously beyond reach of each other. THERE IS NOTHING BUILT "
            "ANYWHERE IN THE PICTURE: no wall, fence, barrier, rail, rope, "
            "bridge, causeway, stair, path, ladder, curtain or veil crosses or "
            "spans the chasm at any point, and there is NO fire, flame, smoke, "
            "steam, lava, molten fissure or red light anywhere in its depths — "
            "it is dry rock, dust and shadow. THIS IS A WIDE FULL-LENGTH SCENE: "
            "the camera is far enough back that both rims and the whole depth "
            "of the rift are in frame together."
        ),
    },
    {
        "id": "v2-r037-b30", "out": "s30-they-which-would-pass-cannot.jpeg",
        "seg": "j4", "window": "93.960-98.280", "wide": False, "jesus": False,
        "locks": _TORMENT, "char_refs": _RICH,
        "narration": "so that they which would pass from hence to you cannot;",
        "must_show": "The near lip from the rich man's own side: his sandalled feet stopped hard at the crumbling edge with the rock falling away into shadow immediately beyond them — the physical fact that there is nowhere further to go.",
        "must_not_show": _NO_INFERNO + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 35mm lens, a LOW CLOSE frame taken at ground level "
            "at the very edge of the rock, hard flat colourless overhead "
            "daylight, the sun out of frame, fine film grain, shallow depth of "
            "field falling away into the chasm. NO FACE IS IN THIS PICTURE AT "
            "ALL — the frame is cut at the knee and the man's body is above the "
            "top edge and out of shot — so a lens gaze is geometrically "
            "impossible. THE NEAR FOREGROUND FILLS THE WHOLE LOWER HALF OF THE "
            "FRAME EDGE TO EDGE: broken bleached limestone at the lip, cracked "
            "and crumbling, with loose scree and pale dust, and a hairline "
            "fissure running along it. Standing on it, cut off at the knee, ONE "
            "PAIR OF FEET IN DARK LEATHER SANDALS — good sandals, once fine, "
            "now scuffed and grey with dust — the toes stopped hard at the very "
            "edge with the weight forward, one heel lifted, the hem of a "
            "SATURATED SAFFRON-GOLD tunic and the trailing corner of a DEEP "
            "TYRIAN PURPLE mantle falling across the stone beside them, both "
            "dulled and dust-caked. THE SANDALS ARE FIRST-CENTURY: a flat sole "
            "of layered thick leather cut to the shape of the foot with no "
            "heel, and plain undyed leather thongs passing up through slits cut "
            "straight through that sole and KNOTTED, the loose ends hanging — "
            "no buckle, no ring, no metal fitting, no moulded or treaded sole "
            "and no stitching of any machine kind. IMMEDIATELY BEYOND THE TOES "
            "the rock simply ENDS and the wall of the chasm drops away in bare "
            "banded ledges into deep blue shadow, falling out of focus into "
            "darkness with no bottom visible. Far across and above, small and "
            "hazy, the low green line of trees on the far rim catches the "
            "light. THERE IS NO PATH, STEP, LEDGE, FOOTHOLD, ROPE, BRIDGE, "
            "RAIL, STAIR OR HANDHOLD ANYWHERE IN THE PICTURE, and no fire, "
            "flame, smoke, molten fissure or red light in the depths."
        ),
    },
    {
        "id": "v2-r037-b31", "out": "s31-neither-can-they-pass-to-us.jpeg",
        "seg": "j4", "window": "98.280-102.696", "wide": True, "jesus": False,
        "locks": _REST + ["SPIRIT-WORLD"], "char_refs": _ABE,
        "narration": "neither can they pass to us, that would come from thence.",
        "must_show": "The same impossibility from the far side: Abraham standing at the green rim looking out across the chasm, seen from behind, with the scorched country tiny and far away on the other side.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_INFERNO + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 35mm lens, soft warm afternoon daylight on the "
            "green rim from the LEFT, the far country beyond bleached and hazy "
            "with distance, the sun out of frame and never behind any head, "
            "fine film grain, deep focus throughout. THE CAMERA STANDS BEHIND "
            "THE OLD MAN AND SHOOTS PAST HIM out across the chasm: he is seen "
            "ENTIRELY FROM BEHIND, standing at the near rim at the lower left "
            "of a wide frame, and NO FACE IS IN THE PICTURE AT ALL, so a lens "
            "gaze is geometrically impossible. BECAUSE THE CAMERA IS BEHIND HIS "
            "HEAD, HIS HAIR IS STATED HERE: THICK SILVER-GREY HAIR falling in "
            "waves to his shoulders from a bare crown, clear against ONE DARK "
            "OLIVE-GREEN rectangular mantle over ONE DEEP INDIGO-BLUE "
            "ankle-length tunic, with the edge of his LONG SILVER-GREY BEARD "
            "just showing past the line of his cheek as he stands in "
            "three-quarter from behind. He wears nothing on his head. HE IS "
            "ALONE IN THE FRAME and no other person, shoulder, arm or blurred "
            "body appears anywhere in it. He stands still and unhurried with "
            "his hands at his sides, his head level, simply looking out. THE "
            "GROUND HE STANDS ON is the green rim of the place of rest — soft "
            "grass and low green plants running to the edge, the deep shade of "
            "broad real trees behind him at the left, and NO wall, fence, rail, "
            "kerb or built edge of any kind between him and the drop. BEYOND "
            "HIM the enormous dry chasm opens in bare stratified rock falling "
            "into deep blue shadow, and beyond that again, small and pale and "
            "shimmering with heat haze across the top of the frame, the far "
            "country of bare cracked clay under a burning white sky, empty to "
            "its horizon. THIS IS A WIDE FULL-LENGTH SCENE: the camera is far "
            "enough back that the standing man is visible complete from head to "
            "sandals and reads as small against the width of the gulf. THERE IS "
            "NOTHING BUILT ANYWHERE IN THE PICTURE and no fire, smoke, molten "
            "fissure or red light in the depths."
        ),
    },
    # ===== n8 — the narrator on the gulf =====================================
    {
        "id": "v2-r037-b32", "out": "s32-a-great-gulf-had-been-fixed.jpeg",
        "seg": "n8", "window": "102.696-107.090", "wide": True, "jesus": False,
        "locks": _REST, "char_refs": _ABE,
        "narration": "And between them, Abraham said, a great gulf had been fixed —",
        "must_show": "Abraham in half profile at the rim with the chasm behind him, mid-sentence, one hand open toward the emptiness he is describing — the man saying the words, on his own side.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_INFERNO + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 50mm lens, soft warm afternoon daylight from the "
            "LEFT AND IN FRONT of him modelling the front planes of his face, "
            "the light source out of frame and never behind his head, fine film "
            "grain, shallow depth of field with the chasm behind thrown soft. "
            "THE CAMERA STANDS TO HIS LEFT AND SLIGHTLY BEHIND HIM, so he is "
            "seen in three-quarter FROM BEHIND turning into near profile: his "
            "head is turned away from the lens toward the chasm, the camera "
            "sees the side of his face with the far cheek foreshortened and the "
            "far eye narrowed behind the bridge of his nose, and his eyeline "
            "runs LATERALLY ACROSS the frame and out through the RIGHT EDGE. "
            "HIS PUPILS NEVER COME ROUND ONTO THE LENS AXIS. HE IS ALONE IN THE "
            "FRAME and no other person, shoulder, arm or blurred body appears "
            "anywhere in it. He stands three-quarter length at the green rim. "
            "RESTATE HIS IDENTITY: a man of about eighty with warm olive-brown "
            "clearly Middle Eastern skin deeply lined at the brow and the eye, "
            "a LONG FULL SILVER-GREY BEARD to the middle of his chest, THICK "
            "SILVER-GREY HAIR waving to his shoulders from a bare high "
            "forehead, wearing nothing on his head — no turban, cap, crown, "
            "diadem or wreath — in ONE DEEP INDIGO-BLUE ankle-length tunic "
            "under ONE DARK OLIVE-GREEN rectangular mantle with ONE DEEP MAROON "
            "folded sash, and never cream, off-white or any pale cloth. HIS "
            "ACTION MUST READ AT A GLANCE: his near hand is lifted waist high "
            "and held OPEN AND FLAT, palm down, extended out toward the "
            "emptiness beyond the rim — the plain gesture of a man saying 'this "
            "is how far it is'. He is not pointing at a person, not raising a "
            "hand in blessing, not commanding and not forbidding, and he holds "
            "nothing. His mouth is open mid-word and his expression is grave "
            "and sorrowful, never angry and never stern. Behind and below him "
            "the bare stratified rock of the chasm falls away out of focus into "
            "deep shadow, and the soft grass and low green plants of the rim "
            "run across the near foreground. THIS IS A WIDE FULL-LENGTH SCENE: "
            "the camera is far enough back that the man and the rim and the far "
            "drop are in frame together."
        ),
    },
    {
        "id": "v2-r037-b33", "out": "s33-one-no-one-could-cross.jpeg",
        "seg": "n8", "window": "107.090-109.681", "wide": True, "jesus": False,
        "locks": ["SPIRIT-WORLD"],
        "narration": "one that no one could ever cross.",
        "must_show": "The chasm alone, straight down into it, empty of every person and every built thing — sheer bare rock walls dropping into darkness with no floor visible.",
        "must_not_show": _NO_INFERNO + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 35mm lens angled steeply DOWN INTO the rift from "
            "the rim, hard daylight catching the upper ledges on the LEFT and "
            "the depths falling into cool blue shadow, the sun out of frame, "
            "fine film grain, deep focus. A LANDSCAPE FRAME WITH NO PERSON IN "
            "IT ANYWHERE — no figure, silhouette, shoulder, hand or blurred "
            "body appears at any point, near or far, in focus or out of focus. "
            "THE CAMERA LOOKS DOWN THE NEAR WALL AND ACROSS TO THE FAR ONE, angled from the side rather than square on and with no eyeline anywhere in it because nobody is present to be seen from behind, so "
            "the frame is almost entirely rock. THE NEAR FOREGROUND AND THE "
            "LOWER CORNERS ARE FILLED EDGE TO EDGE by the crumbling bleached "
            "limestone of the rim itself, cracked and dusty with loose scree "
            "spilling over. Below it the wall drops away in bare stratified "
            "bands of tan, grey and ochre limestone, stepping through broken "
            "ledges and long scree fans, each band smaller than the last, down "
            "into deep blue-black shadow where THE FLOOR IS NEVER VISIBLE and "
            "the darkness simply closes. Across the frame the far wall rises "
            "again in the same bands, softened by distance and haze. THE SCALE "
            "IS ENORMOUS AND IS MADE READABLE BY THE ROCK ITSELF — the "
            "diminishing bands, the haze in the air across the gap, the "
            "shrinking of the ledges — AND NOT BY ANY PERSON, ANIMAL, BUILDING "
            "OR OBJECT PLACED FOR SCALE. THERE IS NOTHING BUILT ANYWHERE IN THE "
            "PICTURE: no bridge, causeway, span, arch, rope, cable, plank, "
            "stair, ladder, path, foothold, rail, fence or wall crosses or "
            "descends it at any point. THERE IS NO FIRE, FLAME, EMBER, SMOKE, "
            "STEAM, LAVA, MOLTEN ROCK, MOLTEN FISSURE, RED LIGHT OR ORANGE LIGHT "
            "ANYWHERE IN THE DEPTHS — the darkness below is simply shadow and "
            "distance, and everything in the picture is dry stone and dust."
        ),
    },
    # ===== n9 — the five brethren ============================================
    {
        "id": "v2-r037-b34", "out": "s34-he-begged-again.jpeg",
        "seg": "n9", "window": "109.681-111.790", "wide": False, "jesus": False,
        "locks": _TORMENT, "char_refs": _RICH,
        "narration": "So the rich man begged again:",
        "must_show": "The rich man asking a second time — the fight gone out of him, down on one knee at the lip in side profile, one hand open in appeal rather than raised in a shout.",
        "must_not_show": _NO_INFERNO + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _NO_MOCK + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: his head and body are in EXACT LEFT-FACING PROFILE to the "
            "camera, his brow, nose, lips and beard drawn cleanly against the "
            "bright empty distance. THE FAR CHEEK AND THE FAR EYE ARE HIDDEN "
            "behind the bridge of his nose and are not in the picture at all, "
            "so a lens gaze is geometrically impossible. His near eye is "
            "lowered and looks out and slightly down along his own profile line "
            "and exits through the LEFT EDGE. "
            "One photograph, 50mm lens, three-quarter length, hard flat "
            "colourless daylight from the upper LEFT AND IN FRONT of him, the "
            "light source never behind his head, fine film grain, shallow depth "
            "of field. HE IS ALONE IN THE FRAME and no other person, shoulder, "
            "arm or blurred body appears anywhere in it. HE IS DOWN ON ONE "
            "KNEE on the broken bleached limestone near the lip, the other foot "
            "flat, his weight sagging back onto his heel, his shoulders dropped "
            "and his back curved — the posture of a man who has stopped "
            "shouting. His near hand is held out low and OPEN, palm upward, in "
            "plain appeal; the other hangs. RESTATE HIS IDENTITY: warm "
            "olive-brown clearly Middle Eastern skin, a full thick trimmed dark "
            "brown beard squared at the jaw with grey at the chin, thick dark "
            "brown wavy hair cut to the middle of the neck, disordered and "
            "dust-grey, the DEEP TYRIAN PURPLE mantle hanging off one shoulder "
            "and dragging on the stone over the SATURATED SAFFRON-GOLD tunic, "
            "both dulled and caked with dust, his dark leather sandals scuffed "
            "and grey. HIS EXPRESSION IS EXHAUSTED AND URGENT rather than "
            "furious: the brow drawn, the mouth open mid-word, real grief in it "
            "— he is asking for somebody else now. He is never grotesque, never "
            "a caricature and never comic, and he keeps his human dignity. "
            "Behind him the bare cracked ground and the burning white sky are "
            "thrown out of focus, with the shadowed line of the chasm crossing "
            "behind his knee. THERE IS NO FIRE, FLAME, SMOKE OR BURNING THING "
            "ANYWHERE IN THE FRAME."
        ),
    },
    {
        "id": "v2-r037-b35", "out": "s35-my-five-brothers.jpeg",
        "seg": "n9", "window": "111.790-114.610", "wide": True, "jesus": False,
        "locks": _HOUSE + ["FEAST-GUESTS", "BANQUET-HALL"],
        "narration": "then send someone to my five brothers,",
        "must_show": "The five brethren, countable: exactly five men at the low table in the rich man's house, living exactly as he did, each one separated and individually visible.",
        "must_not_show": _NO_CREAM + _NO_HALO + _NO_MOCK + _NO_MODERN_LAMP + _NO_KITSCH + _GAZE,
        "scene": (
            "One photograph, 28mm wide lens, warm low late-afternoon daylight "
            "falling through a plain rectangular wall opening on the LEFT "
            "across the low table, the rest of the room in warm shadow, the "
            "light source out of frame and never behind any head, fine film "
            "grain, deep focus throughout. COUNT AS GEOMETRY: THERE ARE EXACTLY "
            "FIVE MEN IN THIS PICTURE AND NO SIXTH PERSON OF ANY KIND — no "
            "servant, no woman, no child, no extra shoulder, arm, head or "
            "blurred body at any edge, in focus or out of focus. The five are "
            "spread out around three sides of the low knee-high adzed-timber "
            "table with CLEAR SEPARATION BETWEEN EVERY ONE OF THEM so that the "
            "viewer can count five distinct men without effort, each reclining "
            "propped on his LEFT elbow on his own folded wool bolster with his "
            "feet away behind him. THE CAMERA STANDS BACK AND ABOVE AT THE OPEN "
            "FOURTH SIDE OF THE TABLE AND SHOOTS PAST THE TWO NEAREST MEN: "
            "those two fill the near lower corners as shoulders, elbows and "
            "BACKS seen entirely from behind, the three beyond are seen in side "
            "and three-quarter view turned toward each other in conversation, "
            "and NOT ONE FACE IS TURNED TOWARD THE LENS — every eyeline runs "
            "laterally across the table between them. They are Judean men "
            "between about twenty-five and forty-five, prosperous and relaxed, "
            "each with warm olive-brown Middle Eastern skin, dark hair and a "
            "dark beard, and no two sharing a face. EVERY ONE OF THEM IS "
            "DRESSED HEAD TO FOOT IN ONE SOLID DARK SATURATED COLOUR — dark "
            "umber, charcoal, deep rust, dark olive and deep indigo, one each — "
            "and NOT ONE WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, "
            "WHITE OR ANY PALE CLOTH, AND NOT ONE WEARS SAFFRON-GOLD OR TYRIAN "
            "PURPLE. Nobody is drunk, sprawling, leering, gorging or drawn as a "
            "caricature of greed: they are simply five well-off brothers "
            "enjoying a good supper. The table carries flat rounds of bread "
            "laid on the bare wood, shallow fired-clay bowls of olives, figs "
            "and lentils, and plain clay jars and unstemmed cups. THIS IS A "
            "WIDE FULL-LENGTH SCENE: the camera is far enough back that all "
            "five men, the whole low table and the rough hewn ceiling beams are "
            "in frame together."
        ),
    },
    {
        "id": "v2-r037-b36", "out": "s36-to-warn-them.jpeg",
        "seg": "n9", "window": "114.610-117.232", "wide": True, "jesus": False,
        "locks": _GATE + ["MARKET-TOWN", "BACKGROUND-CAST"],
        "narration": "to warn them, so they never come to this place.",
        "must_show": "The same gateway and the same worn hollow in the dust, now with one of the brothers walking out past it exactly as the rich man used to — the warning that has not landed, staged as the habit simply continuing.",
        "must_not_show": _NO_IRONGATE + _NO_MODERN_TOWN + _NO_CREAM + _NO_MOCK + _NO_HALO + _NO_KITSCH + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard clear morning sun from the LEFT "
            "throwing a short black shadow ahead of the walking man, the sun "
            "well out of frame and never behind any head, fine film grain, true "
            "depth of field. THE CAMERA STANDS IN THE LANE BEHIND THE MAN AND "
            "SHOOTS PAST HIM AWAY FROM THE GATEWAY: he is centre frame, full "
            "length, seen ENTIRELY FROM BEHIND and walking AWAY from the camera "
            "down the lane, so no face is in the picture at all and a lens gaze "
            "is geometrically impossible. HIS DIRECTION OF TRAVEL IS AWAY FROM "
            "THE CAMERA. He is ONE prosperous Judean man of about thirty-five, "
            "and BECAUSE THE CAMERA IS BEHIND HIS HEAD HIS HAIR IS STATED HERE: "
            "thick dark brown hair cut level at the nape above a plain "
            "rectangular mantle, never a bare, bald, shaven or cropped head, "
            "and he wears nothing on it. HE IS DRESSED HEAD TO FOOT IN ONE "
            "SOLID DARK SATURATED CHARCOAL — a plain ankle-length wool tunic "
            "and mantle with a folded sash — and HE WEARS NO CREAM, OFF-WHITE "
            "OR PALE CLOTH AND NO SAFFRON-GOLD OR TYRIAN PURPLE, because he is "
            "one of the brothers and not the man himself. He walks upright, "
            "unhurried and preoccupied, his head level and facing straight down "
            "the lane. AT THE RIGHT OF FRAME stands the same gateway in the "
            "long dressed-limestone wall — two stone jambs, one flat stone "
            "lintel, the square-topped opening, the heavy timber leaf pushed "
            "back open flat against the inside of the wall — and at the foot of "
            "the wall beside it, EMPTY, lies the same shallow WORN HOLLOW in "
            "the dust the length and shape of a man, with nobody in it and "
            "nobody anywhere near it. His line of walk passes straight along "
            "the wall without deviating. THIS IS A WIDE FULL-LENGTH SCENE: the "
            "camera is far enough back that the man is visible head to sandals "
            "and the whole gateway and the empty hollow are in frame with him. "
            "Far down the lane, small with distance, ONE other townsman in a "
            "solid dark umber garment walks away."
        ),
    },
    # ===== j5 — Luke 16:29, ABRAHAM speaking (RED) ===========================
    {
        "id": "v2-r037-b37", "out": "s37-they-have-moses-and-the-prophets.jpeg",
        "seg": "j5", "window": "117.232-119.060", "wide": False, "jesus": False,
        "locks": _REST + ["ESTATE-ACCOUNTS"], "char_refs": _ABE,
        "narration": "They have Moses and the prophets;",
        "must_show": "What they already have, shown as the physical thing it is: a hand-inked Hebrew scroll of the law open across a man's knees, the brush-drawn letters plainly hand-made.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, a VERY CLOSE frame of an open "
            "scroll lying across a man's knees, soft cool dappled daylight "
            "falling through leaves from the upper LEFT, fine film grain, very "
            "shallow depth of field. NO FACE IS IN THIS PICTURE AT ALL — the "
            "frame holds knees, hands and the scroll and nothing above them — "
            "so a lens gaze is geometrically impossible. THE SCROLL IS THE "
            "SUBJECT AND IS STATED PIECE BY PIECE: ONE length of thin scraped "
            "PARCHMENT, its surface fibrous, uneven, cream-brown and slightly "
            "cockled, its edges cut rough, unrolled flat across the knees with "
            "the rolled remainder curling away to both frame edges over two "
            "plain hewn wooden rollers. THE WRITING ON IT IS HAND-DRAWN: "
            "several columns of dark brown-black HEBREW letters made with brush "
            "and reed-pen strokes, irregular in size and spacing, the ink faded "
            "and uneven and sitting a little crooked on the sheet, with visible "
            "ruling scored by hand rather than printed — never typeset, never "
            "mechanical, never in even machine rows, and never in modern arabic "
            "numerals or any recognisable modern word. TWO OLD HANDS hold the "
            "parchment flat at its edges: large, bony, veined, spotted with age "
            "and warm olive-brown, clearly a very old man's hands and clearly "
            "of adult male size against the width of the scroll, ENTIRELY "
            "UNMARKED with no cut, wound, blood or bandage anywhere on them. AT "
            "THE EDGES OF THE FRAME, filling the lower corners, are the knees "
            "and lap of ONE DEEP INDIGO-BLUE hand-woven wool tunic with the "
            "edge of ONE DARK OLIVE-GREEN mantle falling across it, and BECAUSE "
            "THIS IS A CLOSE MACRO THEIR WEAVE IS RESTATED HERE: a flat matte "
            "loom-woven surface showing a clear slightly irregular over-and-"
            "under grid of warp and weft threads with a frayed selvedge — never "
            "knitted, ribbed, felted, brushed or napped. THERE IS NO BOUND "
            "BOOK, CODEX, SPINE, COVER BOARD, PAGE NUMBER, PRINTED TYPE OR "
            "MODERN PAPER ANYWHERE IN THE FRAME."
        ),
    },
    {
        "id": "v2-r037-b38", "out": "s38-let-them-hear-them.jpeg",
        "seg": "j5", "window": "119.060-121.612", "wide": False, "jesus": False,
        "locks": _REST, "char_refs": _ABE,
        "narration": "let them hear them.",
        "must_show": "Abraham finishing the sentence — a strict side profile, quiet and final, without hardness. The answer is plain rather than severe.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_INFERNO + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: his head is in EXACT RIGHT-FACING PROFILE to the camera, "
            "his brow, nose, lips and the long fall of his beard drawn cleanly "
            "against the soft green shade behind him. THE FAR CHEEK AND THE FAR "
            "EYE ARE HIDDEN behind the bridge of his nose and are not in the "
            "picture at all, so a lens gaze is geometrically impossible. His "
            "near eye looks level and far off along his own profile line and "
            "exits through the RIGHT EDGE. "
            "One photograph, 85mm lens, a frame of head and shoulders, soft "
            "cool dappled daylight falling through leaves from the RIGHT AND IN "
            "FRONT of him, modelling the front planes of his face and leaving "
            "the back of his head in green shade, the light source never behind "
            "his head, fine film grain, very shallow depth of field with the "
            "trees thrown soft. HE IS ALONE IN THE FRAME and no other person, "
            "shoulder, arm or blurred body appears anywhere in it. RESTATE HIS "
            "IDENTITY: a man of about eighty, warm olive-brown clearly Middle "
            "Eastern skin deeply lined at the brow and the eye, a LONG FULL "
            "SILVER-GREY BEARD to the middle of his chest, THICK SILVER-GREY "
            "HAIR waving to his shoulders, his head BARE with nothing on it, in "
            "ONE DEEP INDIGO-BLUE tunic under ONE DARK OLIVE-GREEN mantle and "
            "never cream, off-white or any pale cloth. HIS EXPRESSION IS THE "
            "SUBJECT AND IT IS QUIET: the sentence has just ended, his mouth is "
            "closed, his jaw relaxed, his brow still drawn with sorrow, his "
            "chin level. HE IS NOT ANGRY, NOT STERN, NOT SEVERE, NOT REBUKING, "
            "NOT TRIUMPHANT AND NOT CONDEMNING — the answer is plain and it "
            "costs him something to give it. He holds nothing, raises no hand "
            "and makes no gesture. He carries no wing, no feather, no bright "
            "ring around his head and no light of any kind coming off him; he "
            "is solid and opaque and casts a real shadow."
        ),
    },
    # ===== n10 — the plea about the dead =====================================
    {
        "id": "v2-r037-b39", "out": "s39-the-writings-of-moses.jpeg",
        "seg": "n10", "window": "121.612-124.300", "wide": True, "jesus": False,
        "locks": ["RICH-HOUSE", "ESTATE-ACCOUNTS", "JUDEAN-LAND", "BACKGROUND-CAST"],
        "narration": "They already have the writings of Moses and the prophets,",
        "must_show": "The scrolls in the brothers' own house — a stack of rolled parchment scrolls standing in a reed basket in a plain niche, dusty and clearly unopened for a long time.",
        "must_not_show": _NO_CREAM + _NO_HALO + _NO_MODERN_LAMP + _NO_KITSCH + _GAZE,
        "scene": (
            "One photograph, 50mm lens, warm low late-afternoon daylight "
            "falling in sideways from the LEFT through a plain rectangular wall "
            "opening out of frame, raking across the wall and catching the dust "
            "in the air, the light source never behind anything, fine film "
            "grain, shallow depth of field. AN INTERIOR FRAME WITH NO PERSON IN "
            "IT ANYWHERE — no figure, shoulder, arm, hand, head or blurred body "
            "appears at any point in this picture, in focus or out of focus. "
            "THE CAMERA STANDS BACK FROM THE WALL AND SQUARE ON TO IT at chest "
            "height. Set into the mud-plaster wall, washed pale tan and "
            "hand-smoothed, is ONE plain square recessed niche spanned by a "
            "single flat hewn timber lintel with no door, frame, shelf-board or "
            "fitting of any kind. Standing upright inside it, in ONE "
            "hand-woven split-reed basket, are SIX or SEVEN rolled scrolls, "
            "each one separated and individually countable: tubes of thin "
            "scraped parchment and papyrus, cream-brown, fibrous and slightly "
            "cockled, each wound on a plain hewn wooden roller with the rough "
            "cut edge of the sheet showing, and each tied round with ONE turn "
            "of twisted flax cord. A VISIBLE FILM OF PALE DUST lies over the "
            "tops of the rolls and along the rim of the basket, unbroken and "
            "undisturbed, with a fine cobweb strung across one upper corner of "
            "the niche — nothing here has been lifted out for a very long time. "
            "One shallow fired-clay lamp stands unlit and cold on the sill of "
            "the niche with no flame in it. THIS IS A WIDE FULL-LENGTH SCENE: "
            "the camera is far enough back that the whole niche, the basket of "
            "scrolls and a good spread of the plastered wall around them are in "
            "frame together, with the rough hewn ceiling beams above. THERE IS "
            "NO BOUND BOOK, CODEX, SPINE, SHELF OF BOOKS, DESK, LECTERN OR "
            "MODERN PAPER ANYWHERE IN THE FRAME."
        ),
    },
    {
        "id": "v2-r037-b40", "out": "s40-let-them-listen.jpeg",
        "seg": "n10", "window": "124.300-127.100", "wide": False, "jesus": False,
        "locks": _REST, "char_refs": _ABE,
        "narration": "Abraham replied. Let them listen.",
        "must_show": "Abraham's old hand and forearm resting open on his knee as he finishes speaking — the stillness of a man who has said what he has to say.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, a VERY CLOSE frame of one old "
            "man's hand and forearm resting on his own knee, soft cool dappled "
            "daylight falling through leaves from the upper LEFT, fine film "
            "grain, very shallow depth of field. NO FACE IS IN THIS PICTURE AT "
            "ALL — the frame holds a hand, a forearm and a knee and nothing "
            "above them — so a lens gaze is geometrically impossible, AND ONLY "
            "ONE PERSON IS IN THE FRAME, with no second hand, arm, shoulder or "
            "blurred body anywhere in it. THE HAND IS VERY OLD AND CLEARLY A "
            "GROWN MAN'S: large, bony and long-fingered, of full adult male "
            "size against the knee it rests on, the skin warm olive-brown, "
            "loose over the tendons, spotted and mottled with age, the veins "
            "standing proud across the back, the knuckles enlarged and the "
            "nails short, blunt and ridged. It lies OPEN AND RELAXED, palm "
            "down, fingers slightly apart and settled, with no tension in it: "
            "it is not clenched, not pointing, not gripping and not raised in "
            "any gesture, and it holds nothing. THE HAND IS ENTIRELY UNMARKED — "
            "no cut, wound, hole, scar, blood, bandage or dressing anywhere on "
            "the back of it or the wrist. THE NEAR FOREGROUND AND THE WHOLE "
            "LOWER HALF OF THE FRAME ARE FILLED EDGE TO EDGE by the knee and "
            "lap beneath it in ONE DEEP INDIGO-BLUE hand-woven wool tunic, with "
            "the heavy folded edge of ONE DARK OLIVE-GREEN mantle crossing the "
            "upper right corner, and BECAUSE THIS IS A CLOSE MACRO THE WEAVE IS "
            "RESTATED HERE: both cloths are flat, thin and matte, showing a "
            "clear slightly irregular over-and-under grid of warp and weft "
            "threads and a frayed selvedge edge, exactly like coarse hand-woven "
            "wool — never knitted, never ribbed, never a stretchy cuff, never "
            "felted, fleeced, brushed, napped or blanket-like, and never satin, "
            "velvet or shiny. Beyond, the green shade and the still water are "
            "thrown completely soft."
        ),
    },
    {
        "id": "v2-r037-b41", "out": "s41-if-one-came-back-from-the-dead.jpeg",
        "seg": "n10", "window": "127.100-131.700", "wide": True, "jesus": False,
        "locks": _TORMENT, "char_refs": _RICH,
        "narration": "But the man pleaded — no, if only someone came back from the dead,",
        "must_show": "The rich man's last argument: back on his feet at the lip, leaning out across the chasm with one arm flung toward the far side, insisting — the final push of a man who will not accept the answer.",
        "must_not_show": _NO_INFERNO + _NO_KITSCH + _NO_GHOST + _NO_CREAM + _NO_HALO + _NO_MOCK + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hard flat colourless overhead daylight, "
            "the sun out of frame and never behind his head, fine film grain, "
            "true depth of field. THE CAMERA STANDS BEHIND AND TO THE LEFT OF "
            "THE MAN, ON THE SAME LIP OF ROCK, AND SHOOTS PAST HIM out over the "
            "chasm: he is seen in three-quarter FROM BEHIND, full length, and "
            "NO FACE IS TURNED TOWARD THE LENS — the camera sees the back and "
            "side of his head and his words go away from the lens across the "
            "empty air. BECAUSE THE CAMERA IS BEHIND HIS HEAD, HIS HAIR IS "
            "STATED HERE: thick dark brown wavy hair cut to the middle of the "
            "neck, disordered and dust-grey, clear against the DEEP TYRIAN "
            "PURPLE mantle hanging from one shoulder over the SATURATED "
            "SAFFRON-GOLD tunic, both dulled and caked with pale dust. THE "
            "ACTION MUST READ CORRECTLY AT A GLANCE: he has got back onto his "
            "feet and stands at the crumbling edge with his weight thrown "
            "forward onto the front foot, his upper body leaning out over the "
            "drop, ONE ARM FLUNG OUT AND EXTENDED toward the far side with the "
            "hand open and the fingers spread, the other arm braced back for "
            "balance, his head pushed forward and his jaw dropped mid-word. "
            "This is insistence, not collapse and not attack: HE IS NOT "
            "FALLING, NOT JUMPING, NOT CLIMBING DOWN, NOT THROWING ANYTHING AND "
            "NOT BEING PUSHED, and nobody else is touching him. HE IS THE ONLY "
            "PERSON IN THE PICTURE and no other figure, hand or blurred body "
            "appears anywhere in it. THE NEAR FOREGROUND AND THE LOWER CORNERS "
            "ARE FILLED EDGE TO EDGE by the broken bleached limestone of the "
            "lip, cracked and scattered with loose scree, with the rock ending "
            "abruptly just beyond his leading sandal. Beyond him the chasm "
            "opens as bare stratified dry rock falling into deep blue shadow, "
            "and far across it, small and hazy with distance, the low green "
            "line of trees in shade. THIS IS A WIDE FULL-LENGTH SCENE: the "
            "camera is far enough back that the man is visible complete from "
            "head to sandals against the width of the gulf. THERE IS NO FIRE, "
            "FLAME, SMOKE, MOLTEN FISSURE OR RED LIGHT ANYWHERE IN THE FRAME."
        ),
    },
    {
        "id": "v2-r037-b42", "out": "s42-then-they-would-turn.jpeg",
        "seg": "n10", "window": "131.700-133.452", "wide": True, "jesus": False,
        "locks": _HOUSE + ["FEAST-GUESTS", "BANQUET-HALL"],
        "narration": "then they would turn.",
        "must_show": "The brothers at the table again, unchanged and untroubled, mid-meal and mid-laugh — the answer to the plea, shown rather than argued.",
        "must_not_show": _NO_CREAM + _NO_HALO + _NO_MOCK + _NO_MODERN_LAMP + _NO_KITSCH + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon daylight "
            "falling through a plain rectangular wall opening on the LEFT, the "
            "room beyond in warm shadow, the light source out of frame and "
            "never behind any head, fine film grain, true depth of field. THE "
            "CAMERA STANDS INSIDE THE ROOM BEHIND AND ABOVE THE OPEN FOURTH "
            "SIDE OF THE LOW TABLE AND SHOOTS PAST THE NEAREST DINERS: two "
            "dark-clad men fill the near lower corners as shoulders, elbows and "
            "BACKS seen entirely from behind, and NOT ONE FACE IS TURNED TOWARD "
            "THE LENS. Beyond them THREE more men recline propped on their LEFT "
            "elbows on folded wool bolsters around the low knee-high "
            "adzed-timber table, seen in side and three-quarter view, turned "
            "toward one another in easy conversation, one with his head back "
            "mid-laugh and his hand lifted, another reaching for bread — every "
            "eyeline running laterally across the table between them. THERE ARE "
            "EXACTLY FIVE MEN IN THE PICTURE AND NO SIXTH PERSON OF ANY KIND, "
            "each separated and individually countable. They are prosperous "
            "Judean men between about twenty-five and forty-five with warm "
            "olive-brown Middle Eastern skin, dark hair and dark beards, no two "
            "sharing a face, EACH DRESSED HEAD TO FOOT IN ONE SOLID DARK "
            "SATURATED COLOUR — dark umber, charcoal, deep rust, dark olive and "
            "deep indigo, one each — and NOT ONE WEARS CREAM, OFF-WHITE, IVORY, "
            "BUFF, BEIGE, SAND, WHITE OR ANY PALE CLOTH, AND NOT ONE WEARS "
            "SAFFRON-GOLD OR TYRIAN PURPLE. NOTHING IN THE ROOM HAS CHANGED AND "
            "NOTHING TROUBLES THEM: nobody has stopped eating, nobody looks up, "
            "nobody has heard anything, there is no messenger, no visitor, no "
            "empty place laid and no figure standing in any opening. Nobody is "
            "drunk, leering, gorging or drawn as a caricature. The table "
            "carries flat rounds of bread on the bare wood, fired-clay bowls of "
            "olives and figs, and plain clay jars and unstemmed cups. THIS IS A "
            "WIDE FULL-LENGTH SCENE: the camera is far enough back that all "
            "five men and the whole low table are in frame together."
        ),
    },
    # ===== n11 — ANCHOR b43 ==================================================
    {
        "id": "v2-r037-b43", "out": "s43-his-final-answer.jpeg",
        "seg": "n11", "window": "133.452-136.000", "wide": False, "jesus": False,
        "locks": ["ABRAHAM", "SPIRIT-WORLD"],
        "narration": "And Abraham gave his final answer.",
        "must_show": "ANCHOR FRAME. Abraham alone, in strict side-on profile, his face clearly readable, about to speak the last word — the single reference picture that fixes his face, his silver beard and his indigo and olive cloth for every other frame he appears in.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_INFERNO + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: his head and shoulders are in EXACT RIGHT-FACING PROFILE to "
            "the camera, his brow, nose, lips and the long fall of his beard "
            "drawn cleanly against the soft shaded ground behind him. THE FAR "
            "CHEEK AND THE FAR EYE ARE HIDDEN behind the bridge of his nose and "
            "are not in the picture at all, so a lens gaze is geometrically "
            "impossible. His near eye is open, level and steady and looks far "
            "off along his own profile line and out through the RIGHT EDGE. "
            "One photograph, 85mm lens, a frame of head, shoulders and upper "
            "chest, soft cool daylight coming in sideways from the RIGHT AND IN "
            "FRONT of him under the shade of real trees, modelling the front "
            "planes of his face and leaving the back of his head and the "
            "background in soft green shadow, the light source LOW AND IN FRONT "
            "and never behind his head, fine film grain, very shallow depth of "
            "field with the trees thrown completely soft. HE IS ALONE IN THE "
            "FRAME AND NO OTHER PERSON, SHOULDER, ARM, HEAD OR BLURRED BODY "
            "APPEARS ANYWHERE IN IT, at any edge, in focus or out of focus. "
            "RESTATE HIS IDENTITY IN THIS FRAME, BECAUSE THIS PICTURE FIXES IT "
            "FOR EVERY OTHER: a Judean patriarch of about eighty, tall and "
            "still upright though thin with age, with WARM OLIVE-BROWN CLEARLY "
            "MIDDLE EASTERN skin — never fair, never pink, never European-"
            "looking — deeply lined across the forehead and around the eye, a "
            "strong straight nose and a heavy brow; a LONG FULL SILVER-GREY "
            "BEARD reaching the middle of his chest, thick and slightly waved "
            "and clearly separated into strands; and THICK SILVER-GREY HAIR "
            "falling in waves to his shoulders from a high lined forehead, with "
            "a clear band of that silver hair at the temple and at the nape. "
            "HIS HEAD IS BARE and he wears nothing on it — no turban, cap, "
            "crown, diadem, wreath or head cloth of any kind. HE WEARS ONE DEEP "
            "INDIGO-BLUE hand-woven wool tunic with a straight unshaped sleeve, "
            "under ONE DARK OLIVE-GREEN rectangular mantle drawn over the near "
            "shoulder, with the edge of ONE DEEP MAROON folded sash just "
            "showing; each cloth is a flat matte loom-woven surface with a "
            "visible warp-and-weft grid and a frayed selvedge, never knitted, "
            "felted, brushed or shiny. HE WEARS NO CREAM, OFF-WHITE, IVORY OR "
            "ANY PALE CLOTH ANYWHERE, and no jewellery, ring, chain or metal "
            "ornament. HIS EXPRESSION: grave, compassionate and sorrowful, the "
            "brow drawn, the mouth just opening on the first word — never "
            "angry, never stern, never triumphant and never condemning. He "
            "carries NO wing, NO feather, NO bright ring or disc around his "
            "head and no light of any kind coming off him; he is a solid, "
            "opaque, embodied old man casting a real shadow."
        ),
    },
    # ===== j2 — Luke 16:31, ABRAHAM speaking (RED) ===========================
    {
        "id": "v2-r037-b44", "out": "s44-if-they-hear-not-moses.jpeg",
        "seg": "j2", "window": "136.000-140.370", "wide": True, "jesus": False,
        "locks": _REST, "char_refs": _ABE,
        "narration": "If they hear not Moses and the prophets, neither will they be persuaded,",
        "must_show": "Abraham speaking the last word from his own side, seen from behind and to one side with the enormous gulf and the far scorched country in front of him — the answer given out across the distance.",
        "must_not_show": _NO_KITSCH + _NO_GHOST + _NO_INFERNO + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 35mm lens, soft warm afternoon daylight on the "
            "green rim from the LEFT, the far country beyond bleached and "
            "shimmering with distance, the sun out of frame and never behind "
            "any head, fine film grain, deep focus throughout. THE CAMERA "
            "STANDS BEHIND AND TO THE LEFT OF THE OLD MAN AND SHOOTS PAST HIM "
            "out across the chasm: he is seen in three-quarter FROM BEHIND, "
            "full length, standing at the near rim at the left of frame, and NO "
            "FACE IS TURNED TOWARD THE LENS — the camera sees the back and side "
            "of his head only and his words go away from the lens across the "
            "gulf. BECAUSE THE CAMERA IS BEHIND HIS HEAD, HIS HAIR IS STATED "
            "HERE: THICK SILVER-GREY HAIR falling in waves to his shoulders "
            "from a bare crown, with the edge of his LONG FULL SILVER-GREY "
            "BEARD showing past the line of his cheek, clear against ONE DARK "
            "OLIVE-GREEN rectangular mantle over ONE DEEP INDIGO-BLUE "
            "ankle-length tunic; he wears nothing on his head and no cream, "
            "off-white or pale cloth anywhere. HE IS ALONE IN THE FRAME and no "
            "other person, shoulder, arm or blurred body appears anywhere in "
            "it. HIS POSTURE IS STILL AND UNHURRIED: he stands square and "
            "level with his weight even on both feet, his near hand hanging "
            "open and relaxed at his side, his head level and facing out across "
            "the distance. He is not leaning out, not reaching, not pointing, "
            "not raising a hand and not gesturing at all — the finality is "
            "carried entirely by how still he is. THE GROUND HE STANDS ON is "
            "the green rim, soft grass and low green plants running to the "
            "edge, with the deep shade of broad real trees behind him and NO "
            "wall, fence, rail or built edge of any kind between him and the "
            "drop. Beyond him the enormous dry chasm falls away in bare "
            "stratified rock into deep blue shadow, and beyond that again, "
            "small and pale across the top of the frame, the far country of "
            "bare cracked clay under a burning white sky. THIS IS A WIDE "
            "FULL-LENGTH SCENE: the camera is far enough back that the man is "
            "visible complete from head to sandals against the width of the "
            "gulf. THERE IS NOTHING BUILT ANYWHERE IN THE PICTURE and no fire, "
            "smoke, molten fissure or red light in the depths."
        ),
    },
    {
        "id": "v2-r037-b45", "out": "s45-though-one-rose-from-the-dead.jpeg",
        "seg": "j2", "window": "140.370-143.640", "wide": True, "jesus": False,
        "locks": ["TOMBS", "JUDEAN-LAND"],
        "narration": "though one rose from the dead.",
        "must_show": "The tomb on the hillside with its round sealing stone rolled back and the square opening standing open and empty — the possibility Abraham has just named, shown as an empty doorway in the rock with nobody in the frame.",
        "must_not_show": _NO_FUNERAL + _NO_GHOST + _NO_KITSCH + _NO_INFERNO + _NO_CREAM + _NO_HALO + _GAZE,
        "scene": (
            "One photograph, 35mm lens, the low warm raking light of very early "
            "morning coming in almost level from the LEFT across the hillside, "
            "throwing the long shadow of the rock face across the ground, the "
            "sun itself well out of frame, fine film grain, deep focus. A "
            "LANDSCAPE FRAME WITH NO PERSON IN IT ANYWHERE — no figure, "
            "silhouette, shoulder, hand, footprint or blurred body appears at "
            "any point in this picture, near or far, in focus or out of focus, "
            "and nothing is entering or leaving the opening. THE CAMERA STANDS "
            "BACK FROM THE ROCK FACE AND A LITTLE TO THE SIDE OF IT, low on the "
            "hillside. A low bare limestone scarp runs across the frame, its "
            "surface weathered, chisel-marked and streaked with lichen. Cut "
            "straight into it is ONE plain SQUARE opening about waist high, its "
            "edges rough and hand-cut, and BEYOND THE OPENING THERE IS ONLY "
            "PLAIN DARKNESS — flat, even, unlit shadow with nothing visible in "
            "it, no interior detail, no shelf, no cloth, no shape and NO LIGHT "
            "OF ANY KIND coming out of it. Beside the opening, ONE large ROUND "
            "FLAT DISC OF UNDRESSED LIMESTONE stands ROLLED BACK along the "
            "shallow channel cut into the rock, leaning against the face, with "
            "a clear arc scraped in the dust of the channel showing where it "
            "has been moved. THE NEAR FOREGROUND AND THE LOWER THIRD ARE FILLED "
            "EDGE TO EDGE by the stony hillside ground — bare trodden dust, "
            "loose pale chippings, grey-green thorn scrub and dead sun-bleached "
            "grass in tufts. Behind and above, the bare dry rounded limestone "
            "hills stand hazy against a deep blue morning sky. THIS IS A WIDE "
            "FULL-LENGTH SCENE: the camera is far enough back that the whole "
            "rock face, the opening and the rolled-back stone are in frame "
            "together. NOTHING IN THIS PICTURE IS A LATER GRAVEYARD: no "
            "headstone, cross, carved memorial, railing, flowers, coffin, dug "
            "pit or lettering of any kind."
        ),
    },
    # ===== n12 — the application; Jesus speaking as himself ==================
    {
        "id": "v2-r037-b46", "out": "s46-jesus-told-this-to-people.jpeg",
        "seg": "n12", "window": "143.640-146.050", "wide": True, "jesus": True, "ref": REF,
        "locks": _TEACH,
        "narration": "Jesus told this to people who had everything,",
        "must_show": "Back in the fig court: Jesus finishing the story to the well-dressed men sitting with him, the camera behind their backs, his attention level and unhurried on the man he is addressing.",
        "must_not_show": _NO_HALO + _NO_KITSCH + _NO_CREAM + _NO_MODERN_TOWN + _NO_GREEN + _GAZE,
        "scene": (
            "LENS-AXIS GEOMETRY, STATED FIRST BECAUSE IT GOVERNS THIS FRAME: "
            "the man Jesus is addressing is NOT behind the camera — he sits far "
            "out at the RIGHT EDGE of the picture, so Jesus's head is turned a "
            "quarter-turn away from the lens and STAYS there. The camera sees "
            "the SIDE of his face, the near cheek broad and the far cheek "
            "foreshortened with the far eye narrowed behind the bridge of his "
            "nose, and his eyeline runs LATERALLY ACROSS the frame and out "
            "through the RIGHT EDGE. HIS PUPILS NEVER COME ROUND ONTO THE LENS "
            "AXIS, HE NEVER FACES THE VIEWER SQUARE-ON, AND HE NEVER LOOKS INTO "
            "THE CAMERA. "
            "One photograph, 35mm lens, the light now lower and warmer than "
            "before — late afternoon slanting in under the fig leaves from the "
            "LEFT in long soft dapples across the packed earth, the sun well "
            "out of frame and NEVER behind any head, fine film grain, true "
            "depth of field. THE CAMERA STANDS BEHIND AND SLIGHTLY ABOVE THE "
            "SEATED LISTENERS AND SHOOTS PAST THEM: four dark-clad prosperous "
            "townsmen fill the lower and left third of the frame as heads, "
            "shoulders and BACKS seen entirely FROM BEHIND, sitting on the low "
            "limestone bench and on reed mats, one of them very still with his "
            "head slightly lowered, and NOT ONE FACE IS TURNED TOWARD THE LENS. "
            "Jesus sits facing them on the far side, right of centre, on the "
            "low dry-laid limestone bench, three-quarter length and "
            "three-quarter view, both forearms resting easily across his knees, "
            "his head turned to his own right toward the man at the edge and "
            "his gaze travelling level and to the RIGHT and out through the "
            "RIGHT EDGE. His expression is quiet, warm and unhurried — he has "
            "just finished telling something hard and he is not accusing "
            "anybody. THIS IS A WIDE FULL-LENGTH GROUP PHOTOGRAPH AND NOT A "
            "PORTRAIT: the camera is far enough back that all five men, the "
            "thick grey gnarled trunk of the fig tree and the plastered "
            "mud-brick wall behind them are in frame together. THE ONLY PALE "
            "WOOL IN THE WHOLE PICTURE IS HIS OWN ROBE; every other man is a "
            "solid dark saturated mass of indigo, umber, rust, olive, charcoal "
            "or maroon from edge to edge, in focus and out of focus alike."
        ),
    },
    {
        "id": "v2-r037-b47", "out": "s47-walked-right-past.jpeg",
        "seg": "n12", "window": "146.050-149.510", "wide": True, "jesus": False,
        "locks": ["MARKET-TOWN", "JUDEAN-LAND", "BACKGROUND-CAST"],
        "narration": "and walked right past the ones who had nothing.",
        "must_show": "An ordinary town lane today: two well-dressed men walking on, seen from behind, and a thin man sitting against the wall behind them that neither has turned toward — the parable's point happening in real life, without accusation.",
        "must_not_show": _NO_MOCK + _NO_STIGMATA + _NO_MODERN_TOWN + _NO_CREAM + _NO_HALO + _NO_KITSCH + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun raking down "
            "the lane from the LEFT, throwing long shadows across the dust, the "
            "sun well out of frame and never behind any head, fine film grain, "
            "true depth of field. THE CAMERA STANDS IN THE LANE BEHIND THE TWO "
            "WALKING MEN AND SHOOTS PAST THEM DOWN THE LANE: both are seen "
            "ENTIRELY FROM BEHIND, full length, walking AWAY from the camera "
            "side by side, so no face is in the picture at all and a lens gaze "
            "is geometrically impossible. THEIR DIRECTION OF TRAVEL IS AWAY "
            "FROM THE CAMERA. BECAUSE THE CAMERA IS BEHIND THEIR HEADS, THEIR "
            "HAIR IS STATED HERE: both have thick dark hair cut level at the "
            "nape, one dark brown and one greying, above plain rectangular "
            "mantles, and neither head is bare, bald, shaven or cropped. Both "
            "are prosperous Judean townsmen, one in solid DEEP MAROON and one "
            "in solid CHARCOAL head to foot, and NEITHER WEARS CREAM, "
            "OFF-WHITE, IVORY, BUFF, BEIGE, SAND OR ANY PALE CLOTH. They walk "
            "at an easy pace with their heads level, talking to each other, one "
            "with a hand lifted mid-gesture toward the other — their attention "
            "entirely on their own conversation. BEHIND THEM AND TO THE RIGHT, "
            "already passed and slipping out of their world, a thin man sits on "
            "the ground against the foot of the plastered mud-brick wall with "
            "his knees drawn up, in ONE knee-length coarse DARK UMBER-BROWN "
            "wool tunic, barefoot, an empty shallow fired-clay bowl on the "
            "ground beside him. HE IS NOT LAZARUS AND MUST NOT BE HIM: his hair "
            "is dark and cut short, his beard is short, his face and legs are "
            "unmarked with NO sore, wound, cut, blood or bandage anywhere on "
            "him, and he simply looks down and away at the ground so his "
            "eyeline exits through the LOWER RIGHT of the frame. He is a real "
            "person with dignity, not grotesque, not comic, not cowering and "
            "not pitiable as a spectacle. THE ACTION MUST READ AT A GLANCE: the "
            "two walkers' line of travel runs straight down the middle of the "
            "lane without deviating and neither head is turned even slightly "
            "toward him; nobody is jeering, sneering, shoving or reacting to "
            "him at all — he is simply not seen, and that is the whole picture. "
            "THIS IS A WIDE FULL-LENGTH SCENE: the camera is far enough back "
            "that both walkers are visible head to sandals and the seated man "
            "and the wall are in frame with them."
        ),
    },
    {
        "id": "v2-r037-b48", "out": "s48-a-warning-and-a-mercy.jpeg",
        "seg": "n12", "window": "149.510-153.379", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FIG-COURT", "JUDEAN-LAND"],
        "narration": "It was a warning — but underneath it, a mercy.",
        "must_show": "Jesus's own face, close and in strict profile, at the moment the story turns from warning to mercy — the kindness in it plainly readable and no severity anywhere.",
        "must_not_show": _NO_HALO + _NO_KITSCH + _NO_CREAM + _NO_MODERN_TOWN + _GAZE,
        "scene": (
            "STRICT SIDE-ON PROFILE, STATED FIRST BECAUSE IT GOVERNS THIS "
            "FRAME: his head is in EXACT LEFT-FACING PROFILE to the camera, his "
            "brow, nose, lips and beard drawn cleanly against the soft shaded "
            "courtyard wall behind him. THE FAR CHEEK AND THE FAR EYE ARE "
            "HIDDEN behind the bridge of his nose and are not in the picture at "
            "all, so a lens gaze is geometrically impossible. His near eye "
            "looks level and steady along his own profile line and out through "
            "the LEFT EDGE toward the man he has been speaking to. "
            "One photograph, 85mm lens, a frame of head and shoulders only, "
            "warm low late-afternoon daylight coming in from the LEFT AND IN "
            "FRONT of him under the fig leaves, LOW AND FORWARD so it travels "
            "upward and forward onto the front planes of his face — catching "
            "the underside of the brow, the nose, the cheekbone and the chin — "
            "while the crown, the back of the head and the hair stay unlit and "
            "dark and merge into the shade behind; NO LIGHT SOURCE OF ANY KIND "
            "STANDS BEHIND, ABOVE OR BEYOND HIS HEAD, and there is no bright "
            "rim, edge, outline, contour line, ring or corona anywhere around "
            "his head, hair or shoulders. Fine film grain, very shallow depth "
            "of field with the plastered mud-brick wall and the fig leaves "
            "thrown completely soft. HE IS ALONE IN THE FRAME and no other "
            "person, shoulder, arm, head or blurred body appears anywhere in "
            "it, at any edge, in focus or out of focus. HIS EXPRESSION IS THE "
            "ENTIRE SUBJECT: the mouth closed and settled, the jaw relaxed, the "
            "brow open rather than drawn, the near eye warm, steady and "
            "unguarded, with real compassion and a trace of sorrow in it — the "
            "face of somebody who has told a hard story because he wants the "
            "hearer to be spared it. HE IS NOT STERN, NOT GRIM, NOT ANGRY, NOT "
            "ACCUSING, NOT WARNING AND NOT TRIUMPHANT. He wears his one plain "
            "undyed off-white wool robe with the mantle over the shoulder, and "
            "he is the only figure in the picture."
        ),
    },
    # ===== n13 — the closing line ============================================
    {
        "id": "v2-r037-b49", "out": "s49-the-day-is-still-yours.jpeg",
        "seg": "n13", "window": "153.379-156.525", "wide": True, "jesus": False,
        "locks": _GATE + ["MARKET-TOWN", "JUDEAN-LAND"],
        "narration": "Because the day is still yours — for now.",
        "must_show": "The gateway in the evening light with somebody sitting quietly at the foot of the wall beside it and the lane still open and empty — the choice still standing, unresolved, with no verdict placed on it.",
        "must_not_show": _NO_IRONGATE + _NO_MOCK + _NO_STIGMATA + _NO_MODERN_TOWN + _NO_CREAM + _NO_HALO + _NO_KITSCH + _GAZE,
        "scene": (
            "One photograph, 35mm lens, the warm low raking light of late "
            "evening coming in almost level from the LEFT down the length of "
            "the lane, throwing very long soft shadows across the dust and "
            "turning the plastered wall warm gold, the sun itself well out of "
            "frame and never behind any head, fine film grain, deep focus. THE "
            "CAMERA STANDS LOW IN THE MIDDLE OF THE LANE, BACK FROM THE "
            "GATEWAY AND LOOKING ALONG THE WALL, so the wall and the lane run "
            "away together into the warm distance. THE NEAR FOREGROUND FILLS "
            "THE LOWER THIRD EDGE TO EDGE: bare packed dust worn hollow by "
            "feet, scattered with loose pale limestone chippings, the long "
            "shadows lying across it and the lane ahead standing OPEN AND EMPTY "
            "with nobody walking in it. In the middle distance at the right "
            "stands the gateway in the long dressed-limestone wall — two stone "
            "jambs, ONE flat stone lintel, the square-topped opening, the heavy "
            "weathered timber leaf pushed back open flat against the inside of "
            "the wall, the worn threshold slab at ground level. Sitting on the "
            "ground at the foot of the wall just beside it is ONE thin man in "
            "ONE knee-length coarse DARK UMBER-BROWN wool tunic, barefoot, his "
            "knees drawn up and his arms loose across them, seen in "
            "three-quarter FROM BEHIND AND TO THE SIDE so that only the back "
            "and side of his lowered head are visible and NO FACE IS TURNED "
            "TOWARD THE LENS; his short dark hair is clear at the crown and the "
            "nape. He carries no sore, wound, cut, blood or bandage anywhere, "
            "he is not Lazarus, and he is drawn as a real person with dignity — "
            "not grotesque, not cowering, not pitiable as a spectacle. HE IS "
            "THE ONLY PERSON IN THE PICTURE: nobody else stands, walks or "
            "waits anywhere in it, at any edge, in focus or out of focus. "
            "NOTHING IN THIS FRAME RESOLVES THE STORY — nobody is helping him, "
            "nobody is refusing him, nobody is approaching and nobody is "
            "walking away — the lane is simply still open and the light is "
            "still on it. THIS IS A WIDE FULL-LENGTH SCENE: the camera is far "
            "enough back that the whole height of the wall and gateway, the "
            "seated man and the open lane are in frame together, with the flat "
            "rooflines of the town and the bare dry hills warm against a "
            "deepening blue evening sky."
        ),
    },
]
