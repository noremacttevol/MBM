#!/usr/bin/env python3
"""V2 beat map — row 29, build-29-pearl (Matthew 13:45-46), realistic.

COVERAGE: 36 pictures against V1's SIX, over 108.99 s of story = 3.03 s/picture.
V1's `s1-merchant.jpeg` covered n1, j1 AND n2 (0.28 s -> 19.36 s, NINETEEN SECONDS);
`s4-sells-all.jpeg` covered n5, j2 AND n6 (38.08 -> 60.71, TWENTY-TWO AND A HALF);
`s5-buys-it.jpeg` covered n7 and n8 (60.71 -> 85.48, TWENTY-FOUR AND A HALF); and
`s6-pearl-radiant.jpeg` covered n9 and n10 (85.48 -> 109.27, TWENTY-THREE AND A
HALF) — which is the ENTIRE closing turn of the video, the "to Jesus, YOU are the
pearl" reading that the whole story exists to deliver, on one held picture.

⚠️ THE INHERITED beats_v2.py WAS DISCARDED (saved off first), and this is why —
measured, not assumed:
  * It planned 18 pictures at 5.8 s each and called that "the library density",
    which it no longer is: rows 24-28 shipped at 3.1-4.9 s/picture.
  * IT STAGED THE FRAME IN A HOUSE INTERIOR, arguing from Matthew 13:36. Row 16 is
    already this wave's lamplit interior and row 28 examined and rejected exactly
    this argument for exactly this reason; the frame beats here run ELEVEN times
    across the video, so a second interior is the repeat, not the cure.
  * Its own search beats specified "dim lamplit dealer's stalls" and "harbour dusk"
    with "each searching beat may pick its own hour", which throws away the clock
    that rows 23-28 proved is the strongest single storytelling tool in this wave.
  * Its MERCHANT lock allowed "two gold rings" and a changing set of ornaments as a
    deliberate variable — the exact drift that a lock exists to prevent — and its
    PEARL lock said "flawless, perfectly round", which is a machined CGI sphere.

AUDIO IS CLEAN AND LOCKED (checked from the FILES, not from prose):
  * `matthew-13_pearl-of-great-price.mp4` last changed bytes 2026-07-27T22:46:55 and
    EVERY `audio/*.mp3` last changed bytes at that SAME commit (git CONTENT dates —
    mtimes are worthless in this repo, four machines pull it). No placed mp3 is newer
    than the MP4, so `assert_v1_final_is_current()`'s recency tripwire has nothing to
    refuse, and the V1 stream runs 115.798 s against the summed timeline.
  * SOURCING TRAP CHECKED AND CLEARED. All THIRTEEN segments (n1-n10, j1, j2, card)
    were transcribed with faster-whisper `word_timestamps=True` and every one matches
    the LIVE `make_narration.py` word for word. Two apparent differences were chased
    down and are whisper's, not the audio's: it renders the KJV "like unto" as
    "likened to" in j1 (an archaic phrase both base.en and small.en mishear), and it
    contracts "here is" to "here's" in n7. The card was re-run on small.en because
    base.en gave "you ARE the pearl" against the script's "you WERE the pearl" —
    small.en returns the script's wording exactly. So NO `TEXT_OVERRIDES` are needed
    on this row and `AUDIO_FROM_V1_SEGMENTS` stays off.

⚠️ WINDOWS COMPUTED FROM SCRATCH 2026-08-02 with `extract_beats.py` reading the V1
build, then split inside each segment on WORD timings measured from that segment's
own mp3 with faster-whisper. THE `.timing.json` SIDECARS WERE NOT TRUSTED (rows 26
and 27 proved that family unusable) and this build carries no `.mp3.words.json` at
all. Windows are SEGMENT-BOUNDARY CONTIGUOUS (`seg_start` -> the NEXT segment's
`seg_start`, never `audio_start` -> `spoken_end`), so there is no dead gap at any of
the twelve segment joins: contiguous 0.280 s -> 109.270 s (the card start), zero
gaps, zero overlaps, shortest window 1.36 s, longest 4.72 s. Every split lands on a
clause head or a sentence boundary and none falls inside a word.

SCRIPTURE (Matthew 13:45-46 KJV — the parable is TWO verses and one sentence):
  "Again, the kingdom of heaven is like unto a merchant man, seeking goodly pearls:
   who, when he had found one pearl of great price, went and sold all that he had,
   and bought it."
Three things have to be readable in the pictures or the parable does not land:
  1. HE IS ALREADY AN EXPERT AND ALREADY RICH. This is not a poor man's windfall —
     it is a connoisseur who has handled the best there is and still knows he has
     not found it. So his hands are clean and skilled, his goods are good, and the
     pearls he rejects are genuinely beautiful.
  2. THE COST IS TOTAL AND IT IS VISIBLE. "Sold ALL that he had" has to be SEEN as
     an emptied house, not implied — V1 gave the whole selling one reused picture.
  3. THE JOY IS THE POINT, and n7 says it outright: "He did not do it grieving. He
     did not feel robbed." Every emptying frame carries a face that is STEADY AND
     GLAD, and the closing frames are open and at peace, never mourning.

THE TURN AT n9/n10 IS THE REASON THE VIDEO EXISTS and V1 gave it no picture of its
own. Read backward, HE is the merchant and YOU are the pearl. It is staged with
RESTRAINT: it stays inside the frame story on Jesus's face and open hands, and
"his own life" is carried by his upturned empty palms and his eyes, never by any
depiction of the cross. Nothing graphic, nothing literal, no glow.

STAGING ACROSS THE LIBRARY — this row must not repeat a composition already used:
  rows 2, 8, 21 (Luke 15)      courtyard table / low wall under a fig / house meal
  row 11 (the storm)           an open boat at NIGHT in a gale
  row 16 (Mary & Martha)       a lamplit evening interior
  row 19 (breakfast on shore)  a Galilee beach at FIRST LIGHT with a charcoal fire
  row 22 (unmerciful servant)  a black basalt Capernaum doorstep and street
  row 23 (vineyard workers)    a terraced hillside above a vineyard
  row 24 (the sower)           a moored fishing boat off a daylit shingle beach
  row 25 (wheat and tares)     an open grain plain and a round threshing floor
  row 26 (mustard seed)        a small walled kitchen garden
  row 27 (the leaven)          a synagogue-wall stone bench and a walled baking yard
  row 28 (hidden treasure)     an olive grove / a walled stony field / a poor
                               MUD-BRICK dooryard on a dirt slope
So this row is staged in FOUR places, none of them used above:
  * THE FRAME — a BARE LIMESTONE SHELF above a dry wadi at the edge of the hills:
    open rock, no tree, no canopy, no wall, no building, the ravine falling away
    below and the hills opening beyond. Deliberately the OPPOSITE of row 28's olive
    grove (which is defined by canopy and dapple) and of row 27's synagogue bench.
  * THE ROAD — a CARAVAN TRACK winding between tawny hills, camels and laden
    donkeys in a string, dust hanging. No row in this wave has a road at all.
  * THE MARKET — the stone-flagged QUAYSIDE MARKET of a small coastal trading town,
    goat-hair awnings, the sea beyond the sea wall. No row has a town or a market.
  * THE COURTYARD — the merchant's own house: a PAVED DRESSED-LIMESTONE courtyard
    with an outside stone stair to a flat roof. Checked deliberately against row 28,
    which also has a man selling everything: 28's is a POOR MUD-BRICK hut on a bare
    DIRT slope with a thorn pen, shot as a village crowd buying a labourer's few
    goods. This is a PROSPEROUS DRESSED-STONE town house being STRIPPED — different
    material, different class, different emotional direction (28 gains, 29 empties).

THE CLOCK IS THE PLOT AND IT IS ON THE SCREEN. The light only ever moves forward
within each thread and never contradicts the story:
  b03-b04           HARD WHITE MIDDAY on the caravan road, dust, heat shimmer
  b05-b08           CLEAR BRIGHT MORNING under the market awnings
  b09               COLD BLUE FIRST LIGHT on the road (the years of searching)
  b10-b15           CLEAR BRIGHT MORNING in the market (he finds it)
  b16-b20, b22-b23  HARD HIGH NOON (the selling and the stripping — the most
                    exposed hour of his life, with no shadow to hide in)
  b24-b25, b27-b29  THE FIRST WARM GOLD OF DAWN the next morning (everything gone,
                    and he is glad)
The FRAME beats (b01, b02, b21, b26, b30, b31, b32, b33, b34, b35, b36) are ALL warm
low late-afternoon sun on the open rock and NEVER change, because the frame is one
continuous conversation.

TERRAIN IS THE INVARIANT (the rule rows 24-28 established). Each of the four places
is described identically in every frame it appears in; only the light and what is
being carried or laid out ever change.

CAST NOTE — ANCHOR-FIRST (the rows 20-28 lesson that has held the reroll rate at
3-15%). This row needs exactly TWO new faces, so exactly TWO beats are anchors and
they are generated in their OWN run before anything else, each composed so the face
is large, lit and unobstructed, AND — the row 28 lesson — with the HEAD TURNED OFF
THE CAMERA AXIS and the nose pointed at a named frame corner, because on a
near-frontal portrait naming a gaze target inside the frame was NOT enough alone:
  b10  the MERCHANT, his face over the pearl in his own palm, lit from the open sky
  b15  the SELLER, the old pearl trader, across his stall in morning light
`v2_gen_api` builds its REFS cache ONCE per run, so an anchor generated in the same
run as its dependants does not exist yet when they are built — it MUST be a separate
invocation. Jesus is held by JESUS-V2-REF as always.

A FACE SHEET ALONE DOES NOT HOLD A CHARACTER WHO IS SMALL IN FRAME (rows 19, 22-28).
So the MERCHANT and SELLER locks state age, build, hair and dress as explicit
invariants, and every beat naming either of them RESTATES him positively in its own
scene text — including in the wides where he is a distant figure.

CREAM: only Jesus. THE TRAP ON THIS ROW IS THAT THE HERO IS A RICH TRADER, which is
precisely the figure a model dresses in fine bleached linen — a second, unlocked
Jesus in every frame of his own story. So he is pinned ENTIRELY to DARK MURREY-PURPLE
and DARK CHARCOAL-BROWN, the word "linen" is never used of him, and — the row 28
lesson, where the leak was the SCARF and not the tunic — EVERY SEPARATE PIECE OF
CLOTH on every non-Jesus figure is enumerated by name (tunic, sleeves, sash, head
cloth, and any scarf, stole, shawl, wrap or mantle) and pinned dark.

THE SECOND TRAP ON THIS ROW IS THE PEARL ITSELF, and it is two traps in one:
  * A pearl is WHITE, and a white object is not cloth, so the cream law does not and
    must not reach it — but a model asked for a luminous pearl paints a GLOWING ORB,
    which breaks the no-glow law and turns a parable into fantasy. So the PEARL lock
    states positively that it is a small natural object with a soft directional
    highlight and that it emits no light of its own.
  * The pearl beats are TIGHT AND MACRO, and the row 28 lesson is that AN OBJECT
    LOCK PROTECTS THE OBJECT, NOT THE ROOM: a macro shot returns a wholly modern
    surrounding with no catchable prop. So every tight pearl beat states WHERE THE
    CAMERA STANDS IN THE WORLD and tilts so a band of the period market or courtyard
    is forced into the frame behind the hands.

TWO NEW SHARED SETTING LOCKS came out of this row and live in `v2_prompt.py`:
ANCIENT-ROAD (a road's own anachronism is the SURFACE and the things that line it —
tarmac, kerbs, painted lines, tyre ruts, poles, wire, guardrails, signposts — none of
which PERIOD-MATERIALS reaches, because a road surface is not an object) and
MARKET-TOWN (a market's own anachronism is the STALL — trestles, metal poles, striped
or printed awnings, plastic crates, price boards — with row 22's city-skyline lesson
folded in so no future town has to re-learn it).
"""

# LOCKS: one entry per recurring person and per setting. Setting locks NEVER name a
# character. Clothing colours are stated POSITIVELY and DARK, piece by piece.
LOCKS = {
    # ------------------------------------------------------------- people ----
    "MERCHANT": (
        "MERCHANT LOCK: the pearl merchant is the SAME man in every shot, and these "
        "are invariants that hold even when he is small, distant, in shadow or out "
        "of focus: a travelled trader of about forty-five, of middling height, dry "
        "and spare rather than heavy, with wind-and-sun-weathered olive-brown skin, "
        "a lean intelligent face with a high straight nose and deep lines at the "
        "outer corners of the eyes from years of squinting into light, a full "
        "close-trimmed DARK BROWN beard shot with grey at the chin, dark brown hair "
        "cut to the jaw, and steady dark brown eyes. His hands are clean, dry and "
        "long-fingered, uncallused, the hands of a man who handles small precious "
        "things, and they are BARE — he wears no ring, no band, no bracelet, no armlet and no ornament of any kind on either hand or wrist in any frame. His clothing "
        "NEVER changes and EVERY SEPARATE PIECE OF CLOTH ON HIM IS A DARK SATURATED "
        "COLOUR: a DARK CHARCOAL-BROWN wool tunic to the ankle with straight "
        "unshaped sleeves to the wrist, a heavy DARK MURREY-PURPLE mantle of one "
        "rectangle of cloth over his left shoulder, a wide folded DARK OCHRE-BROWN "
        "cloth sash at the waist, a DARK CHARCOAL-BROWN head cloth bound with a dark "
        "brown cord, and good dark leather sandals. He wears NO other cloth of any "
        "kind — no scarf, stole, shawl, wrap or second mantle. EVERY PIECE OF CLOTH "
        "ON HIM IS COARSE WOOL WOVEN ON A LOOM and shows a visible over-and-under "
        "grid of warp and weft threads with a flat matte surface — never knitted, "
        "ribbed, cabled, jersey, fleeced, brushed or napped, and never a sweater or "
        "sweatshirt texture, including at a cuff, the neck opening, the mantle edge "
        "or any blurred edge. He is NEVER dressed in cream, off-white, white, ivory, "
        "ecru, oatmeal, buff, sand, khaki, beige, taupe, pale grey or pale linen and "
        "NEVER in any light-coloured garment of any kind anywhere in any frame, "
        "because any pale cloth on anyone but Jesus reads as a second, unlocked "
        "Jesus and fails the picture. He is never young, never a boy, never old, "
        "never fat, never fair-skinned, never long-haired and never bare-headed "
        "with loose flowing hair."
    ),
    "SELLER": (
        "SELLER LOCK: the old pearl trader who sells him the pearl is the SAME man "
        "in every shot, and these are invariants that hold even when he is small, "
        "distant or out of focus: a very old dealer of about seventy, small, stooped "
        "and thin, a full head shorter than the merchant, with dark leathery "
        "deeply-creased olive skin, a narrow bony face, a long thin WHITE beard to "
        "his chest, thin white hair, heavy white brows, and pale-clouded shrewd dark "
        "eyes. His hands are knotted and arthritic. EVERY SEPARATE PIECE OF CLOTH ON "
        "HIM IS A DARK SATURATED COLOUR: a DARK OLIVE-DRAB wool tunic to the ankle "
        "with straight unshaped sleeves, a DEEP RUST-BROWN mantle of one rectangle "
        "of cloth over both shoulders, a twisted DARK BROWN cord at the waist, and a "
        "DARK SLATE-GREY head cloth bound with a dark cord. He wears NO scarf, "
        "stole, shawl or wrap of any other kind. EVERY PIECE OF CLOTH ON HIM IS "
        "COARSE WOOL WOVEN ON A LOOM with a visible warp-and-weft grid and a flat "
        "matte surface — never knitted, ribbed, cabled, fleeced or napped. He is "
        "NEVER dressed in cream, off-white, white, ivory, buff, sand, beige, taupe, "
        "pale grey or pale linen and NEVER in any light-coloured garment anywhere in "
        "any frame; the ONLY white thing about him is the hair of his head and "
        "beard. He is never young, never tall, never heavy, never black-bearded and "
        "never clean-shaven."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the men gathered around Jesus on the limestone shelf are a "
        "small closed circle of eight to ten of his own disciples and NOBODY ELSE — "
        "no crowd, no women, no children, no passing stranger. They are Galilean "
        "working men between twenty-five and fifty, each with a distinct face, build "
        "and beard, none of them repeated or cloned, all seated low on the bare rock. "
        "EVERY SEPARATE PIECE OF CLOTH ON EVERY DISCIPLE IS A DARK SATURATED COLOUR "
        "— tunic, sleeves, sash, head cloth, and ANY scarf, stole, shawl, wrap or "
        "mantle draped round a neck or over a shoulder is DEEP INDIGO, DARK UMBER, "
        "DARK OLIVE-DRAB, RUSSET-RED or DARK MADDER-BROWN and nothing else. NOT ONE "
        "of them wears cream, off-white, white, ivory, ecru, oatmeal, buff, sand, "
        "khaki, beige, taupe, pale grey or pale linen, and NO DISCIPLE HAS A PALE OR "
        "LIGHT-COLOURED SCARF, STOLE OR SHAWL ROUND HIS NECK OR OVER HIS SHOULDER, "
        "anywhere in the frame, in focus or out of focus, sharp or blurred, in the "
        "foreground or the far background, because any pale cloth on anyone but "
        "Jesus reads as a second, unlocked Jesus and fails the picture. EVERY PIECE "
        "OF CLOTH ON THEM IS COARSE WOOL WOVEN ON A LOOM with a visible "
        "warp-and-weft grid — never knitted, ribbed, fleeced or napped. THE ONLY "
        "PALE THING IN ANY OF THESE FRAMES IS THE WOOL OF JESUS'S OWN ROBE."
    ),
    "BUYERS": (
        "BUYERS LOCK: the townspeople who come to buy the merchant's goods are "
        "people of this same coastal trading town — four or five working men, two "
        "women and one boy — each with a distinct face and none repeated or cloned, "
        "all of them at believable human scale beside the merchant. EVERY SEPARATE "
        "PIECE OF CLOTH ON EVERY ONE OF THEM IS A DARK SATURATED COLOUR — tunic, "
        "sleeves, sash, head cloth, and ANY scarf, stole, shawl, wrap or mantle over "
        "a neck or shoulder is DEEP INDIGO, DARK UMBER, DARK OLIVE-DRAB, RUSSET-RED "
        "or DARK MADDER-BROWN and nothing else. NOT ONE of them wears cream, "
        "off-white, white, ivory, ecru, oatmeal, buff, sand, khaki, beige, taupe, "
        "pale grey or pale linen, and NOT ONE has a pale or light-coloured scarf, "
        "stole or shawl round the neck or over the shoulder, anywhere in the frame, "
        "in focus or out of focus, including blurred figures at the edges. Every "
        "piece of cloth on them is coarse loom-woven wool with a visible "
        "warp-and-weft grid — never knitted, ribbed, fleeced or napped."
    ),
    # ------------------------------------------------------------ settings ----
    "SHELF": (
        "LIMESTONE-SHELF LOCK — this place is IDENTICAL in every frame it appears in "
        "and nothing about it ever changes: a broad BARE FLAT SHELF OF PALE GREY "
        "LIMESTONE, perhaps fifteen paces across, standing out from the shoulder of "
        "a hill at the head of a DRY WADI. The rock is weathered, cracked in long "
        "irregular seams, bleached almost white where the sun has had it and warm "
        "grey-tan in the hollows, with loose flat slabs and a scatter of small round "
        "stones lying on it and dry grey scrub tufting from the cracks at its edges. "
        "At the near side the shelf drops away into the dry stony bed of the wadi "
        "below, a pale winding channel of rounded boulders with no water in it. "
        "Beyond and below, low tawny bare hills fold away one behind another to a "
        "clean far horizon under an open sky. THIS PLACE IS COMPLETELY OPEN AND "
        "BARE: there is NO tree, no olive tree, no orchard, no canopy, no dappled "
        "light, no green foliage, no field wall, no terrace, no building, no roof, "
        "no fence, no post, no wire, no cable, no pipe and no straight manufactured "
        "line anywhere on the shelf, in the wadi, on the hills or against the sky. "
        "The light in every frame here is WARM LOW LATE-AFTERNOON SUN coming in "
        "almost level from one side across the open rock, throwing long soft-edged "
        "shadows out across the stone."
    ),
    "ROAD": (
        "CARAVAN-ROAD LOCK — this place is IDENTICAL in every frame it appears in "
        "and only the light ever changes: ONE narrow caravan track of bare packed "
        "pale earth and dust, about three paces wide, worn hollow below the level of "
        "the ground on either side by centuries of feet and hooves, winding along "
        "the flank of a bare tawny hill and away between two shoulders of rock into "
        "the distance. Grey limestone bedrock breaks through the surface in places "
        "and loose stones lie kicked to the sides. The hills on both sides are dry "
        "tawny grass and grey rock with low thorn scrub in the folds, and no crop, "
        "no terrace, no wall and no tree stands anywhere on them. Dust hangs in the "
        "air along the track. Every surface here is either bare ground, bare rock or "
        "dry scrub; there is nothing built, laid, planted or fenced anywhere in the "
        "picture."
    ),
    "MARKET": (
        "QUAYSIDE-MARKET LOCK — this place is IDENTICAL in every frame it appears in "
        "and only the light and what is laid out ever change: the small open market "
        "of a coastal trading town, set on a floor of worn irregular pale limestone "
        "flags. A single row of low stalls runs along one side — each a plank of "
        "hewn wood laid on stacked stone blocks, shaded by ONE rectangle of VERY "
        "DARK BROWN-BLACK GOAT-HAIR CLOTH slung from rough unpainted wooden poles "
        "lashed with twisted fibre cord. EVERY AWNING, SHADE CLOTH AND HANGING IN "
        "THIS MARKET, near or far, sharp or blurred, IS THAT SAME VERY DARK "
        "BROWN-BLACK GOAT HAIR and reads almost black against the sky — not one of "
        "them is pale, cream, off-white, ivory, sand, buff, ecru, oatmeal, beige, "
        "tan, bleached canvas, sailcloth, or striped. EVERY PERSON ANYWHERE IN THIS "
        "MARKET, including every small, distant and out-of-focus figure in the "
        "background, wears DEEP INDIGO, DARK UMBER, DARK OLIVE-DRAB, RUSSET-RED or "
        "DARK MADDER-BROWN coarse wool with a dark head cloth, and NOT ONE of them "
        "wears cream, off-white, ivory, buff, sand, khaki, beige, taupe, pale grey "
        "or pale linen, because pale cloth on anyone but Jesus reads as a second, "
        "unlocked Jesus and fails the picture. Behind the stalls stand flat-roofed houses of dressed "
        "honey-coloured limestone with plain rectangular door and window openings "
        "and outside stone stairs climbing to the roofs. On the open side a low "
        "dry-laid SEA WALL of rough limestone blocks closes the market, and beyond "
        "it the flat blue-green Mediterranean runs out COMPLETELY EMPTY to a clean "
        "bare horizon — there is NO boat, ship, hull, mast, sail, oar, buoy, mooring "
        "or vessel of any kind anywhere on that water, near or far, in focus or out "
        "of focus, and nothing at all floats on it. Baskets of "
        "split reed, fired-clay bowls and jars, and folded squares of dark "
        "hand-woven wool stand along the stalls. Everything here is stone, hewn "
        "wood, fired clay, plant fibre or wool, hand-made and irregular."
    ),
    "COURTYARD": (
        "MERCHANT'S-COURTYARD LOCK — this place is IDENTICAL in every frame it "
        "appears in and only the light and what stands in it ever change: the "
        "enclosed courtyard of a prosperous town house, floored with LARGE WORN "
        "DRESSED LIMESTONE FLAGS laid unevenly. It is closed on all four sides by "
        "walls of dressed honey-coloured limestone blocks about twice the height of "
        "a man, with ONE tall doorway of heavy hewn cedar planks in the near wall "
        "and a worn stone threshold under it. Along the right-hand wall an OUTSIDE "
        "STONE STAIR of solid blocks, with no rail of any kind, climbs to the FLAT "
        "roof of poles and packed earth. Two plain rectangular storeroom openings "
        "with no doors stand in the far wall. A large fired-clay water jar stands on "
        "a flat stone in one corner. Every surface here is dressed stone, hewn "
        "timber, fired clay or packed earth; there is no dome, no tower, no minaret, "
        "no bell tower, no arch of dressed voussoirs, no tiled or pitched roof, no "
        "column with a carved capital, no glass, no shutter, no hinge, no lock, no "
        "railing, no corrugated or sheet metal, no pipe, no wire and no cable "
        "anywhere on any surface or against the sky above the walls."
    ),
    "PEARL": (
        "PEARL LOCK: the great pearl is ONE natural pearl and it is always the same "
        "one — a single rounded pearl about the size of a large hazelnut, slightly "
        "irregular rather than a perfect machined sphere, warm milky white shading "
        "to the faintest silver-rose in its depths, with a deep soft satiny sheen "
        "and ONE small clean highlight where the sky is reflected in its shoulder. "
        "IT IS AN ORDINARY PHYSICAL OBJECT LIT BY THE SCENE'S OWN LIGHT: it takes "
        "the light of the frame and gives back a soft directional lustre and a quiet "
        "shadow beneath itself, and it NEVER emits, radiates, throws or casts light "
        "of any kind onto a hand, a cloth, a face or the air around it. There is NO "
        "glow, no halo, no aura, no inner light, no rays, no sparkle, no starburst, "
        "no lens flare, no bloom, no magical or supernatural effect and no glassy "
        "CGI sphere anywhere in the picture. The lesser pearls beside it are the "
        "same kind of object — small, irregular, softly lustrous, dull rather than "
        "brilliant. Pearls are always laid on DARK cloth and are never strung, "
        "boxed, mounted, drilled, set in metal, faceted or cut."
    ),
}

OUTPUT_ASSET_DIR = "assets"

# Every V1 mp3 and the V1 MP4 share ONE git content date (2026-07-27T22:46:55) and the
# MP4's runtime sits inside the guard's tripwire, so the finished V1 audio stream is
# current and the normal packet-copy AUDIO LOCK applies. Nothing is re-voiced and V1
# is never written to.
AUDIO_FROM_V1_SEGMENTS = False

REF = True

# Filled in AFTER the two anchor beats are generated in their own run. v2_gen_api
# builds this cache once per invocation, so an anchor cannot be referenced by a beat
# generated in the same run as itself.
REFS = {
    "MERCHANT": "assets/s10-and-then-one-day-he-found-it.jpeg",
    "SELLER": "assets/s15-one-pearl-of-great-price.jpeg",
}

_NO_JESUS = ("no Jesus in this frame; no limestone shelf, no dry wadi and no "
             "late-afternoon frame-story light; ")
_NO_CREAM = ("no cream, off-white, ivory, buff, beige, taupe or pale garment on "
             "anybody anywhere in the frame including the blurred edges; ")
_GAZE = "nobody's pupils centred on the lens."

BEATS = [
    # ================= FRAME — the bare limestone shelf, warm late afternoon ====
    {
        "id": "v2-r029-b01", "out": "s01-one-more-short-story.jpeg",
        "seg": "n1", "window": "0.280-4.150", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SHELF", "DISCIPLES"],
        "narration": "Jesus told one more short story, only two lines long.",
        "must_show": "Jesus seated on the bare flat limestone shelf above the dry wadi, beginning to speak, with his small closed circle of disciples seated low on the open rock around him in warm low late-afternoon sun.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no overcast and no midday overhead glare; no tree, no olive grove, no canopy, no dappled light, no field wall, no building and no roof anywhere in this frame; no road, no camel, no market, no stall, no sea, no courtyard and no pearl; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun coming in almost "
            "level from the left across the open pale grey rock, throwing long "
            "soft-edged shadows out across the stone, fine film grain. THE CAMERA IS "
            "PLACED COMPLETELY SIDE-ON TO THE WHOLE CIRCLE, STANDING OUT ON THE ROCK "
            "WELL TO ONE SIDE AND SHOOTING ACROSS THE GROUP AT RIGHT ANGLES TO EVERY "
            "EYELINE IN THE PICTURE. Jesus sits at the LEFT of the frame on a low "
            "slab of the shelf and the disciples are ranged on the bare rock to the "
            "RIGHT of him, so the whole conversation runs HORIZONTALLY ACROSS THE "
            "FRAME: his gaze travels rightward into the seated men and exits through "
            "the RIGHT EDGE, and every disciple is seen in profile or three-quarter "
            "from behind with a gaze travelling leftward and out through the LEFT "
            "EDGE. NOT ONE MAN'S FACE IS SQUARED UP TO THE CAMERA AND NOT ONE PAIR OF "
            "PUPILS IS CENTRED ON THE LENS. THIS IS A WIDE FULL-LENGTH GROUP "
            "PHOTOGRAPH AND NOT A PORTRAIT: the camera is far enough back that Jesus "
            "AND at least six seated disciples are all in the frame together, head to "
            "sandals, with the dry wadi and the folded tawny hills open behind them; "
            "Jesus occupies only a modest part of the picture and is never framed "
            "from the chest up. EXACTLY TWO out-of-focus seated BACKS fill the near "
            "bottom corners and they are the only foreground objects: a DEEP INDIGO "
            "shouldered back with a dark indigo head cloth at the near LEFT and a "
            "DARK UMBER back with a dark brown head cloth at the near RIGHT, BOTH OF "
            "THEM A SOLID DARK SATURATED MASS FROM EDGE TO EDGE. THERE IS NO PALE, "
            "CREAM, IVORY, BEIGE, TAUPE, BUFF, SAND, KHAKI OR LIGHT-TAN SHAPE, "
            "SHOULDER, BACK, SLEEVE, DRAPE OR BLURRED MASS ANYWHERE IN THE FOREGROUND "
            "OR AT ANY EDGE OF THIS PICTURE — the ONLY pale thing in the whole frame "
            "is the wool of Jesus's own robe. Sharp in the middle distance Jesus sits "
            "on the slab seen from his left side, leaning forward with his forearms on "
            "his knees and one hand opening as he begins to speak."
        ),
    },
    {
        "id": "v2-r029-b02", "out": "s02-like-unto-a-merchant-man.jpeg",
        "seg": "j1", "window": "4.150-6.930", "jesus": True, "ref": REF,
        "locks": ["SHELF", "DISCIPLES"],
        "narration": "Again, the kingdom of heaven is like unto a merchant man,",
        "must_show": "Jesus mid-sentence on the limestone shelf, seen close in clean three-quarter profile, one hand lifted open as he sets the picture before them, his face warm and alive with the telling.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no overcast; no tree, no canopy, no dappled light, no building and no roof; no road, no camel, no market, no sea, no courtyard and no pearl; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, warm low "
            "late-afternoon sun coming in level from the left across his cheek with "
            "soft bounce off the pale rock filling under his jaw, fine film grain. "
            "THE CAMERA IS SET ON THE ROCK WELL TO HIS RIGHT AND SLIGHTLY BELOW HIM, "
            "SHOOTING HIM IN CLEAN THREE-QUARTER PROFILE SO HIS HEAD IS TURNED WELL "
            "OFF THE CAMERA AXIS AND HIS NOSE POINTS AT THE LEFT EDGE OF THE FRAME. "
            "HIS GAZE HAS A NAMED TARGET INSIDE THE PICTURE: the seated disciples "
            "out at the left of the frame, whose dark out-of-focus shoulders are "
            "visible there, so his eyeline runs level and leftward and leaves the "
            "picture through the LEFT EDGE, well away from the lens. Sharp and "
            "filling the frame from the chest up, Jesus is seated on the low "
            "limestone slab, leaning slightly forward, his right hand lifted and "
            "open at the level of his chest with the fingers relaxed as a man does "
            "when he is setting a picture in front of somebody, his face warm and "
            "alive and completely absorbed in the telling. The near foreground at the "
            "bottom left corner is ONE out-of-focus DEEP INDIGO shouldered back, a "
            "solid dark saturated mass edge to edge, and there is nothing else "
            "between the camera and him. Behind him the bare pale grey cracked rock "
            "of the shelf, the dry stony wadi and the folded tawny hills fall "
            "completely out of focus."
        ),
    },
    {
        "id": "v2-r029-b03", "out": "s03-seeking-goodly-pearls.jpeg",
        "seg": "j1", "window": "6.930-10.830", "wide": True,
        "locks": ["MERCHANT", "ROAD", "ANCIENT-ROAD"],
        "narration": "seeking goodly pearls:",
        "must_show": "the merchant far down the caravan track between the bare tawny hills, seen from behind and small, walking on with a string of laden camels and donkeys behind him under hard white midday sun — a man whose whole life is the search.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no courtyard and no pearl in this frame; no tree, no crop, no terrace and no field wall on the hills; no road surface of asphalt, gravel or laid paving, no kerb, no painted line, no tyre track, no pole, no wire, no fence, no signpost and no vehicle; " + _NO_CREAM + "no face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, deep depth of field, HARD WHITE MIDDAY SUN "
            "almost straight overhead so every stone throws a short black shadow "
            "directly beneath itself, pale dust hanging in the air along the track "
            "and a thin heat shimmer over the far shoulder of the hill, fine film "
            "grain. THE CAMERA STANDS DOWN ON THE TRACK WELL BEHIND THE WHOLE STRING "
            "AND LOW, SHOOTING PAST THEM UP THE ROAD, so every person and animal is "
            "seen SQUARELY FROM BEHIND, moving AWAY from the camera into the "
            "distance, and NOT ONE FACE IS TURNED TOWARD THE LENS. The near "
            "foreground across the bottom of the frame is the bare packed pale earth "
            "of the track itself with loose stones and one dry grey thorn tuft, sharp "
            "and close, and there is nobody between the camera and them. Ahead of the "
            "camera and small in the middle distance walks the merchant with his back "
            "to us — a spare, dry-built travelled trader of about forty-five in a DARK "
            "CHARCOAL-BROWN wool tunic to the ankle with a heavy DARK MURREY-PURPLE "
            "mantle over his left shoulder, a DARK OCHRE-BROWN sash and a DARK "
            "CHARCOAL-BROWN head cloth bound with a dark cord — his head up and his "
            "stride steady, going on. Behind him three camels and two laden donkeys "
            "walk in a string, roped nose to tail, with bulging dark goat-hair packs "
            "and reed baskets lashed on with twisted fibre cord, and two "
            "dark-clothed drovers walking at their flanks, also seen from behind. The "
            "hollow track winds on ahead between two shoulders of bare tawny hill and "
            "out of sight under a bleached pale-blue sky."
        ),
    },
    {
        "id": "v2-r029-b04", "out": "s04-his-whole-life-travelling.jpeg",
        "seg": "n2", "window": "10.830-13.470", "wide": True,
        "locks": ["MERCHANT", "ROAD", "ANCIENT-ROAD"],
        "narration": "He spent his whole life traveling and searching,",
        "must_show": "a wide photograph of the same caravan track from high on the hillside, the merchant and his string reduced to small dark figures strung out along a road that runs away into empty tawny country — distance and years, not a journey with an end.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no courtyard and no pearl; no tree, no crop, no terrace, no wall and no building anywhere in the country; no asphalt, gravel or laid paving, no kerb, no painted line, no tyre track, no pole, no wire, no fence, no signpost and no vehicle; " + _NO_CREAM + "no readable face anywhere in the picture.",
        "scene": (
            "One photograph, 24mm lens, deep depth of field, HARD WHITE MIDDAY SUN "
            "straight overhead, the whole country bleached and shadowless except for "
            "short black shadows directly under the animals, dust hanging low along "
            "the track, fine film grain. THE CAMERA STANDS HIGH UP ON THE HILLSIDE "
            "WELL ABOVE AND BEHIND THE STRING, LOOKING STEEPLY DOWN AND AWAY ALONG "
            "THE ROAD, so the figures are seen from behind and above, all of them "
            "moving away from the camera, and no face is turned toward the lens or "
            "even large enough to read. The near foreground across the bottom of the "
            "frame is the dry grey rock and thorn scrub of the hillside the camera "
            "stands on, sharp and close, with nobody between the camera and the drop. "
            "Below and far off, the narrow hollow track of bare packed earth winds "
            "along the flank of the hill and away between the shoulders of the "
            "country until it is a thread. Strung out along it are small dark "
            "figures: the merchant leading in a DARK CHARCOAL-BROWN tunic and DARK "
            "MURREY-PURPLE mantle, three camels and two laden donkeys roped nose to "
            "tail with dark goat-hair packs, and two dark-clothed drovers. Fold "
            "behind fold, bare tawny hills run back to a clean far horizon under a "
            "vast bleached sky, and there is nothing else in the whole picture — no "
            "village, no wall, no tree, nothing but road and distance."
        ),
    },
    {
        "id": "v2-r029-b05", "out": "s05-handling-the-finest-pearls.jpeg",
        "seg": "n2", "window": "13.470-16.010",
        "locks": ["MERCHANT", "MARKET", "MARKET-TOWN", "PEARL"],
        "narration": "handling the finest pearls in the world,",
        "must_show": "the merchant's clean skilled hands close in, turning a single small pearl between finger and thumb over a folded square of dark cloth on the stall plank, with the stone-flagged market and the goat-hair awning clearly behind — an expert at work, not a wondering amateur.",
        "must_not_show": _NO_JESUS + "no road, no camel, no courtyard; no glow, halo, aura, inner light, sparkle, starburst, lens flare or bloom on any pearl; no pale or white cloth under the pearls; no modern table, trestle, metal pole, umbrella, striped or printed awning, plastic crate, tray or bag anywhere; no minaret, bell tower, dome, tiled or pitched roof against the sky; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, CLEAR "
            "BRIGHT MORNING LIGHT coming from the left under the edge of the dark "
            "goat-hair awning so it rakes across the skin of the hands, fine film "
            "grain. THE CAMERA STANDS IN THE MARKET ITSELF, CLOSE OVER THE STALL "
            "PLANK AND WELL TO THE MAN'S LEFT, AND IS TILTED SO THAT THE UPPER THIRD "
            "OF THE FRAME CARRIES A CLEAR BAND OF THE MARKET BEHIND HIM — the "
            "out-of-focus dark goat-hair awning slung on its rough lashed wooden "
            "poles, the worn pale limestone flags of the market floor, and the "
            "flat-roofed honey limestone houses beyond — so the picture can never "
            "read as a modern interior. HIS GAZE HAS A NAMED TARGET INSIDE THE "
            "PICTURE: the pearl in his own fingers at the centre of the frame, so his "
            "head is bent steeply down and turned off the camera axis and his eyeline "
            "runs down and away through the BOTTOM of the picture, nowhere near the "
            "lens. Sharp and filling the lower two-thirds of the frame are his two "
            "hands over a folded square of DARK INDIGO wool laid on the hewn plank — "
            "clean, dry, long-fingered, uncallused BARE hands with NO ring, band, "
            "bracelet or ornament of any kind on either hand or wrist, the DARK "
            "CHARCOAL-BROWN sleeves of his "
            "tunic pushed back at the wrist. The right thumb and forefinger turn ONE "
            "small softly lustrous pearl slowly against the light while the left hand "
            "steadies the cloth; five or six more small irregular pearls lie separate "
            "on the dark wool below. Above the hands his bearded chin and the lower "
            "half of his face are visible in three-quarter, bent to the work, the "
            "lines at the corner of his eye deep with concentration. HIS HEAD IS "
            "COVERED: he wears his DARK CHARCOAL-BROWN head cloth bound with a dark "
            "brown cord, its loose end hanging down over his near shoulder, and the "
            "heavy DARK MURREY-PURPLE mantle lies over his left shoulder — no part of "
            "his bare hair or scalp shows anywhere in the frame. THE WALL BEHIND HIM "
            "IS BARE DRESSED LIMESTONE with nothing whatever hanging on it: no "
            "washing, no laundry, no drying cloth, no pale or white cloth, sheet, "
            "rag, towel, banner or hanging of any kind on the wall, on a line, on a "
            "pole or anywhere in the background."
        ),
    },
    {
        "id": "v2-r029-b06", "out": "s06-always-hunting-for-better.jpeg",
        "seg": "n2", "window": "16.010-19.360",
        "locks": ["MERCHANT", "MARKET", "MARKET-TOWN", "PEARL"],
        "narration": "always hunting for something better.",
        "must_show": "the merchant setting a good pearl back down on the dark cloth unsatisfied and already looking away past the stall — the small dismissive movement of an expert who knows this is not it.",
        "must_not_show": _NO_JESUS + "no road, no camel, no courtyard; no glow, halo, aura, sparkle or lens flare on any pearl; no pale or white cloth under the pearls; no modern table, trestle, metal pole, umbrella, striped or printed awning, plastic crate or bag; no minaret, bell tower, dome or tiled roof against the sky; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, CLEAR BRIGHT MORNING "
            "LIGHT from the left under the awning edge, fine film grain. THE CAMERA "
            "STANDS IN THE MARKET AT THE FAR END OF THE STALL PLANK, WELL TO HIS "
            "LEFT AND AT CHEST HEIGHT, SHOOTING ALONG THE PLANK SO HE IS SEEN IN "
            "CLEAN THREE-QUARTER PROFILE WITH HIS HEAD TURNED WELL OFF THE CAMERA "
            "AXIS AND HIS NOSE POINTING AT THE RIGHT EDGE OF THE FRAME. HIS GAZE HAS "
            "A NAMED TARGET INSIDE THE PICTURE: the far end of the row of stalls out "
            "at the right of the frame, already looking past this one, so his eyeline "
            "runs level and rightward and leaves the picture through the RIGHT EDGE. "
            "Framed from the waist up is the merchant — a spare dry-built travelled "
            "trader of about forty-five with weathered olive-brown skin, a lean "
            "intelligent face, deep lines at the outer corners of the eyes, a full "
            "close-trimmed DARK BROWN beard shot with grey at the chin and dark brown "
            "hair to the jaw under a DARK CHARCOAL-BROWN head cloth bound with a dark "
            "cord, in a DARK CHARCOAL-BROWN wool tunic with a heavy DARK "
            "MURREY-PURPLE mantle over his left shoulder and a DARK OCHRE-BROWN sash. "
            "His right hand is just laying a small lustrous pearl back down on the "
            "folded DARK INDIGO cloth on the plank, the fingers already opening away "
            "from it, and his mouth is closed in a flat unimpressed line. The near "
            "foreground along the bottom edge is the dark end of the hewn plank and "
            "the stacked stone blocks under it, sharp and close, with nobody between "
            "the camera and him. Behind him the dark goat-hair awning on its lashed "
            "wooden poles, the pale limestone flags and the flat-roofed honey "
            "limestone houses fall out of focus."
        ),
    },
    {
        "id": "v2-r029-b07", "out": "s07-a-lot-of-beautiful-pearls.jpeg",
        "seg": "n3", "window": "19.360-21.280",
        "locks": ["MARKET", "MARKET-TOWN", "PEARL"],
        "narration": "He had seen a lot of beautiful pearls.",
        "must_show": "a close overhead photograph of many small pearls laid out separate on a folded square of dark indigo cloth on the stall plank, each one individually visible, genuinely lovely — with a clear band of the stone-flagged market behind them.",
        "must_not_show": _NO_JESUS + "no road, no camel, no courtyard; no person's face in this frame; no glow, halo, aura, sparkle, starburst or lens flare on any pearl; no pale or white cloth; no strung, drilled, boxed, mounted or faceted pearls; no modern table, trestle, metal pole, plastic crate or tray; no lettering or price board anywhere.",
        "scene": (
            "One photograph, 100mm macro lens, shallow depth of field, CLEAR BRIGHT "
            "MORNING LIGHT raking in from the left under the awning edge so each "
            "pearl carries one small clean highlight on its shoulder and lays a soft "
            "shadow beside itself on the cloth, fine film grain. THE CAMERA STANDS IN "
            "THE MARKET DIRECTLY OVER THE STALL PLANK, LEANING IN AND TILTED "
            "DOWNWARD, BUT ANGLED SO THAT THE TOP QUARTER OF THE FRAME STILL CARRIES "
            "A CLEAR BAND OF THE MARKET BEYOND THE PLANK — the worn pale limestone "
            "flags of the market floor, the stacked stone blocks holding the plank "
            "up, and the out-of-focus dark goat-hair awning above — so the picture "
            "can never read as a modern tabletop. Filling the lower three-quarters of "
            "the frame is a folded square of DARK INDIGO hand-woven wool laid on the "
            "hewn wooden plank, its warp and weft threads clearly visible. Laid out "
            "on it, each one separated from the next and individually countable, are "
            "small natural pearls — slightly irregular rather than machined spheres, "
            "warm milky white with a deep soft satiny sheen, dull rather than "
            "brilliant, some rounder and some faintly pear-shaped, no two exactly "
            "alike. They are beautiful, ordinary, physical objects lit only by the "
            "morning; not one of them throws light onto the cloth. There is nobody in "
            "the picture and no hand in the frame."
        ),
    },
    {
        "id": "v2-r029-b08", "out": "s08-good-ones-costly-ones.jpeg",
        "seg": "n3", "window": "21.280-23.320",
        "locks": ["MERCHANT", "MARKET", "MARKET-TOWN", "PEARL"],
        "narration": "Good ones. Costly ones.",
        "must_show": "the merchant holding ONE fine pearl up between finger and thumb against the bright morning sky at the edge of the awning, examining it coolly — the connoisseur's test, and the answer is still no.",
        "must_not_show": _NO_JESUS + "no road, no camel, no courtyard; no glow, halo, aura, inner light, sparkle, starburst, lens flare or bloom on the pearl; no second person in the frame; no modern table, trestle, metal pole, umbrella, striped or printed awning; no minaret, bell tower, dome or tiled roof against the sky; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, CLEAR BRIGHT MORNING "
            "SKY beyond the edge of the dark awning giving a clean bright ground "
            "behind the lifted hand, fine film grain. THE CAMERA STANDS IN THE MARKET "
            "WELL TO HIS RIGHT AND SLIGHTLY LOW, SHOOTING HIM IN NEAR-PROFILE WITH "
            "HIS HEAD TURNED WELL OFF THE CAMERA AXIS AND HIS NOSE POINTING AT THE "
            "LEFT EDGE OF THE FRAME. HIS GAZE HAS A NAMED TARGET INSIDE THE PICTURE: "
            "the single pearl held up in his own left hand at the upper left of the "
            "frame, so his chin is lifted and his eyeline runs up and leftward and "
            "leaves the picture through the TOP LEFT CORNER, far from the lens. "
            "Framed from the chest up is the merchant — a spare travelled trader of "
            "about forty-five, weathered olive-brown skin, lean intelligent face, a "
            "full close-trimmed DARK BROWN beard shot with grey, dark brown hair to "
            "the jaw under a DARK CHARCOAL-BROWN head cloth, in a DARK CHARCOAL-BROWN "
            "wool tunic and a heavy DARK MURREY-PURPLE mantle over his left shoulder. "
            "His left hand is raised beside his head, thumb and forefinger holding ONE "
            "small softly lustrous pearl up against the open bright sky at the awning's "
            "edge; his eyes are narrowed in cool professional assessment and his mouth "
            "is unmoved. He wears his DARK CHARCOAL-BROWN head cloth bound with a "
            "dark brown cord and the heavy DARK MURREY-PURPLE mantle over his left "
            "shoulder. The near foreground at the bottom right corner is the dark "
            "out-of-focus edge of the goat-hair awning cloth, a solid dark mass, and "
            "there is nobody between the camera and him. THE CAMERA IS TURNED AWAY "
            "FROM THE WATER AND FACES INLAND, so behind him there is NO sea, NO "
            "harbour and NO shoreline at all: the whole background is the "
            "out-of-focus stone-flagged market floor, the stacked stone blocks of the "
            "stalls and the flat-roofed honey limestone houses of the town. THERE IS "
            "NO BOAT, SHIP, HULL, MAST, SAIL, OAR, PROW OR VESSEL OF ANY KIND "
            "ANYWHERE IN THIS PICTURE, in focus or out of focus, and nothing in the "
            "frame is painted, varnished or coloured blue or white."
        ),
    },
    {
        "id": "v2-r029-b09", "out": "s09-but-he-kept-looking.jpeg",
        "seg": "n3", "window": "23.320-28.060", "wide": True,
        "locks": ["MERCHANT", "ROAD", "ANCIENT-ROAD"],
        "narration": "But he kept looking, because not one of them was the one.",
        "must_show": "the merchant setting out on the caravan track again in cold blue first light, seen from behind and small, his string of animals behind him — the same road, another year, still going.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no courtyard and no pearl; no midday sun, no golden or warm light, no sunset colouring; no tree, no crop, no terrace and no building anywhere; no asphalt, gravel or laid paving, no kerb, no painted line, no tyre track, no pole, no wire, no fence, no signpost and no vehicle; " + _NO_CREAM + "no face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, deep depth of field, COLD BLUE FIRST LIGHT "
            "before sunrise — the whole country in flat shadowless blue-grey with no "
            "sun risen and no warm colour anywhere, the eastern sky pale and "
            "colourless above the hill shoulder, breath and dust faintly visible in "
            "the cold air, fine film grain. THE CAMERA STANDS ON THE TRACK WELL "
            "BEHIND THE STRING AND AT WAIST HEIGHT, SHOOTING PAST THEM UP THE ROAD, "
            "so every person and animal is seen SQUARELY FROM BEHIND and moving AWAY "
            "from the camera, and NOT ONE FACE IS TURNED TOWARD THE LENS. The near "
            "foreground across the bottom of the frame is the bare packed earth of "
            "the hollow track with loose stones and one dry grey thorn tuft, sharp "
            "and close, with nobody between the camera and them. Small in the middle "
            "distance the merchant walks away up the track with his back to us — a "
            "spare dry-built trader of about forty-five in a DARK CHARCOAL-BROWN wool "
            "tunic to the ankle, a heavy DARK MURREY-PURPLE mantle pulled close "
            "around his shoulders against the cold, a DARK OCHRE-BROWN sash and a "
            "DARK CHARCOAL-BROWN head cloth — his head up, his stride unhurried and "
            "settled, a man who has done this many times. Behind him three camels and "
            "two laden donkeys walk roped nose to tail with dark goat-hair packs and "
            "split-reed baskets lashed on with twisted fibre cord, and two "
            "dark-clothed drovers walk at their flanks, all seen from behind. The "
            "hollow track winds on between bare tawny-grey hills and out of sight."
        ),
    },
    # ============================ THE FINDING — bright morning market ==========
    {
        # ANCHOR A — the MERCHANT's face. Generated in its OWN run before every other
        # beat, so REFS["MERCHANT"] exists when the rest are built.
        "id": "v2-r029-b10", "out": "s10-and-then-one-day-he-found-it.jpeg",
        "seg": "n4", "window": "28.060-29.840",
        "locks": ["MERCHANT", "MARKET", "MARKET-TOWN", "PEARL"],
        "narration": "And then one day, he found it.",
        "must_show": "THE MERCHANT'S FACE, large and clearly lit, the instant of recognition — every professional guard gone out of it, lips parted, eyes wide and still, looking down at one pearl resting in his own open palm.",
        "must_not_show": _NO_JESUS + "no road, no camel, no courtyard; no glow, halo, aura, inner light, sparkle, starburst, lens flare or bloom on the pearl or anywhere in the frame; no second person in the frame; no modern table, trestle, metal pole, umbrella, striped or printed awning; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, CLEAR BRIGHT "
            "MORNING LIGHT falling from the open sky at the left onto his face and "
            "onto the pearl in his palm, with soft bounce from the pale limestone "
            "flags filling under his jaw, fine film grain. THE CAMERA STANDS IN THE "
            "MARKET CLOSE IN FRONT OF HIM AND SLIGHTLY TO HIS RIGHT AND BELOW HIM, "
            "AND HIS HEAD IS TURNED WELL OFF THE CAMERA AXIS INTO THREE-QUARTER VIEW "
            "WITH HIS NOSE POINTING DOWN TOWARD THE BOTTOM LEFT CORNER OF THE FRAME. "
            "HIS GAZE HAS A NAMED TARGET INSIDE THE PICTURE: the single pearl lying "
            "in his own cupped left palm, held at the bottom left of the frame, so "
            "his eyeline runs steeply down and leftward and leaves the picture "
            "through the BOTTOM LEFT CORNER, nowhere near the lens. Sharp and filling "
            "the frame from the shoulders up is the merchant — a spare travelled "
            "trader of about forty-five, of middling height, with weathered "
            "olive-brown skin, a lean intelligent face, a high straight "
            "nose, deep lines at the outer corners of the eyes, a full close-trimmed "
            "DARK BROWN beard shot with grey at the chin and dark brown hair cut to "
            "the jaw under a DARK CHARCOAL-BROWN head cloth bound with a dark brown "
            "cord, in a DARK CHARCOAL-BROWN wool tunic with a heavy DARK "
            "MURREY-PURPLE mantle over his left shoulder. HIS FACE IS THE PICTURE: "
            "every trace of professional coolness has gone out of it, his lips are "
            "parted, his brows lifted, his eyes wide and completely still — a man "
            "looking at the thing he has spent his life looking for. His clean "
            "long-fingered left hand is open flat at the bottom left of the frame "
            "with ONE softly lustrous pearl resting on the palm. The near foreground "
            "along the bottom edge is the dark hewn plank of the stall, sharp and "
            "close, with nobody between the camera and him. Behind him the dark "
            "goat-hair awning, the pale limestone flags and the flat-roofed honey "
            "limestone houses fall completely out of focus."
        ),
    },
    {
        "id": "v2-r029-b11", "out": "s11-a-single-pearl-more-perfect.jpeg",
        "seg": "n4", "window": "29.840-34.560",
        "locks": ["MERCHANT", "MARKET", "MARKET-TOWN", "PEARL"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "A single pearl, more perfect and more precious than anything he had ever held.",
        "must_show": "the great pearl itself in extreme close-up, resting alone in the merchant's cupped palm over the dark indigo cloth — visibly larger and finer than the lesser pearls lying beyond it, but still a real object in real morning light, with a band of the stone market behind.",
        "must_not_show": _NO_JESUS + "no road, no camel, no courtyard; no glow, halo, aura, inner light, radiance, rays, sparkle, starburst, lens flare or bloom on the pearl; no light thrown from the pearl onto the palm or the cloth; no glassy CGI sphere; no pale or white cloth; no modern table, trestle, metal pole or plastic tray; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, CLEAR "
            "BRIGHT MORNING LIGHT falling from the open sky at the left so ONE small "
            "clean highlight sits on the pearl's upper shoulder and it lays a quiet "
            "soft shadow into the creases of the palm, fine film grain. THE CAMERA "
            "STANDS IN THE MARKET LEANING CLOSE OVER HIS OPEN HAND FROM SLIGHTLY "
            "ABOVE AND TO HIS LEFT, AND IS TILTED SO THAT THE TOP QUARTER OF THE "
            "FRAME CARRIES A CLEAR BAND OF THE MARKET BEHIND — the hewn wooden stall "
            "plank on its stacked stone blocks, the worn pale limestone flags of the "
            "market floor and the out-of-focus dark goat-hair awning above — so the "
            "picture can never read as a modern studio shot. Filling the frame is the "
            "merchant's clean, dry, long-fingered open left palm, uncallused, with the "
            "DARK CHARCOAL-BROWN sleeve of his tunic pushed back at the wrist. The "
            "hand is BARE — there is no ring, band, bracelet or ornament of any kind "
            "on it or on his other hand, which steadies the "
            "cloth at the edge of the frame. Resting alone in the hollow of the palm "
            "is the great pearl — a single rounded natural pearl about the size of a "
            "large hazelnut, slightly irregular rather than a machined sphere, warm "
            "milky white shading to the faintest silver-rose in its depths, with a "
            "deep soft satiny sheen. It is plainly larger and finer than the four or "
            "five small dull lesser pearls lying separated on the folded DARK INDIGO "
            "wool cloth just beyond the hand and out of focus. It is an ordinary "
            "physical object taking the morning light and giving back a quiet lustre, "
            "and it throws no light of its own onto anything."
        ),
    },
    {
        "id": "v2-r029-b12", "out": "s12-looking-for-his-whole-life.jpeg",
        "seg": "n4", "window": "34.560-38.080", "wide": True,
        "locks": ["MERCHANT", "SELLER", "MARKET", "MARKET-TOWN", "PEARL"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg",
                      "assets/s15-one-pearl-of-great-price.jpeg"],
        "narration": "The pearl he had been looking for his whole life.",
        "must_show": "a wide photograph across the stall in bright morning: the merchant standing quite still with the pearl closed in his hand, the old white-bearded seller opposite him watching him closely, and the whole quayside market and the sea going on around them, oblivious.",
        "must_not_show": _NO_JESUS + "no road, no camel, no courtyard; no glow, halo, aura, sparkle or lens flare on the pearl; no modern table, trestle, metal pole, umbrella, striped or printed awning, plastic crate or bag; no minaret, bell tower, dome, spire, tiled or pitched roof against the sky; " + _NO_CREAM + "not one face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, CLEAR BRIGHT MORNING LIGHT falling into the "
            "open market from the left with clean hard-edged shadows on the pale "
            "flags, fine film grain. THE CAMERA STANDS OUT IN THE OPEN MARKET "
            "COMPLETELY SIDE-ON TO THE TWO MEN AND SHOOTS ACROSS THE STALL AT RIGHT "
            "ANGLES TO BOTH THEIR EYELINES, so the whole exchange runs HORIZONTALLY "
            "ACROSS THE FRAME and NOT ONE FACE IS SQUARED UP TO THE LENS. THIS IS A "
            "WIDE FULL-LENGTH SCENE AND NOT A PORTRAIT: the camera is far enough back "
            "that both men are visible head to sandals with the stalls, the sea wall "
            "and the sea behind them. At the LEFT of the frame stands the merchant, "
            "seen in profile facing right — a spare travelled trader of about "
            "forty-five with weathered olive-brown skin, a lean face, a full "
            "close-trimmed DARK BROWN beard shot with grey, dark brown hair to the "
            "jaw under a DARK CHARCOAL-BROWN head cloth, in a DARK CHARCOAL-BROWN "
            "wool tunic to the ankle with a heavy DARK MURREY-PURPLE mantle over his "
            "left shoulder and a DARK OCHRE-BROWN sash — standing quite still with "
            "his right hand closed round something at the level of his chest and his "
            "gaze fixed rightward on the old man, leaving the frame through the RIGHT "
            "EDGE. At the RIGHT, behind the hewn plank, stands the old seller in "
            "profile facing left — a small stooped dealer of about seventy, a full "
            "head shorter, dark leathery deeply-creased skin, a long thin WHITE beard "
            "to his chest and thin white hair under a DARK SLATE-GREY head cloth, in "
            "a DARK OLIVE-DRAB wool tunic with a DEEP RUST-BROWN mantle over both "
            "shoulders — his knotted hands flat on the plank, watching the merchant "
            "narrowly, his gaze leaving the frame through the LEFT EDGE. Around and "
            "behind them the market goes on unconcerned: dark-clothed townspeople "
            "moving along the row of stalls under their dark goat-hair awnings, "
            "baskets of split reed and fired-clay jars on the stones, the low "
            "dry-laid limestone sea wall and the flat blue-green sea beyond under a "
            "clear morning sky. The near foreground at the bottom of the frame is the "
            "worn pale limestone flags of the market floor, with nobody between the "
            "camera and the two men."
        ),
    },
    {
        "id": "v2-r029-b13", "out": "s13-and-he-knew-the-moment.jpeg",
        "seg": "n5", "window": "38.080-40.340",
        "locks": ["MERCHANT", "MARKET", "MARKET-TOWN"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "And he knew, the moment he saw it,",
        "must_show": "the merchant's face in close profile, the wonder already hardening into decision — jaw set, eyes steady and calculating nothing, a man who has stopped weighing and started acting.",
        "must_not_show": _NO_JESUS + "no road, no camel, no courtyard; no pearl visible in this frame; no glow, halo, aura, sparkle or lens flare anywhere; no second person sharp in the frame; no modern table, trestle, metal pole, umbrella or printed awning; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, CLEAR BRIGHT "
            "MORNING LIGHT from the left cutting a clean edge along his cheekbone and "
            "brow, fine film grain. THE CAMERA STANDS IN THE MARKET WELL TO HIS LEFT "
            "AND AT EYE HEIGHT, SHOOTING HIM IN CLEAN NEAR-PROFILE WITH HIS HEAD "
            "TURNED FULLY OFF THE CAMERA AXIS AND HIS NOSE POINTING AT THE RIGHT EDGE "
            "OF THE FRAME. HIS GAZE HAS A NAMED TARGET INSIDE THE PICTURE: his own "
            "loaded pack animals and bales standing out at the right of the frame, "
            "visible there as dark out-of-focus shapes, so his eyeline runs level and "
            "rightward and leaves the picture through the RIGHT EDGE, well away from "
            "the lens. Sharp and filling the frame from the shoulders up is the "
            "merchant — weathered olive-brown skin, a lean intelligent face with a "
            "high straight nose and deep lines at the outer corner of the eye, a full "
            "close-trimmed DARK BROWN beard shot with grey at the chin, dark brown "
            "hair to the jaw under a DARK CHARCOAL-BROWN head cloth bound with a dark "
            "cord, in a DARK CHARCOAL-BROWN wool tunic and a heavy DARK MURREY-PURPLE "
            "mantle. The wonder is still in his face but it has already gone hard "
            "into decision: his jaw is set, his mouth closed and firm, his eyes "
            "steady and unblinking, weighing nothing any more. The near foreground at "
            "the bottom left corner is the dark out-of-focus edge of the goat-hair "
            "awning, a solid dark mass, with nobody between the camera and him. "
            "Behind him the stone-flagged market and the flat blue-green sea beyond "
            "the low sea wall fall completely out of focus."
        ),
    },
    {
        "id": "v2-r029-b14", "out": "s14-exactly-what-he-would-do.jpeg",
        "seg": "n5", "window": "40.340-43.330",
        "locks": ["MERCHANT", "MARKET", "MARKET-TOWN", "PEARL"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "exactly what he was going to do.",
        "must_show": "the merchant's fist closing deliberately round the pearl at the level of his chest, seen close from the side, the whole gesture reading as a decision already taken.",
        "must_not_show": _NO_JESUS + "no road, no camel, no courtyard; no glow, halo, aura, inner light, sparkle or lens flare on the pearl or between his fingers; no light escaping from his closed hand; no second person sharp in the frame; no modern table, metal pole or printed awning; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 100mm lens, very shallow depth of field, CLEAR BRIGHT "
            "MORNING LIGHT from the left raking across the back of the hand and the "
            "dark wool of the sleeve, fine film grain. THE CAMERA STANDS IN THE "
            "MARKET CLOSE IN AND WELL TO HIS LEFT, AT CHEST HEIGHT, TILTED SLIGHTLY "
            "UP SO THAT THE UPPER PART OF THE FRAME CARRIES A BAND OF THE MARKET "
            "BEHIND HIM — the dark goat-hair awning on its rough lashed wooden poles "
            "and the flat-roofed honey limestone houses beyond, both out of focus — "
            "so the picture can never read as a modern studio shot. Sharp and filling "
            "the centre of the frame is his right hand at the level of his own chest, "
            "caught in the act of CLOSING: the clean long-fingered uncallused fingers "
            "folding down deliberately over the great pearl in the palm so that only "
            "a curve of its warm milky white is still visible between the second and "
            "third finger, the thumb coming across, the tendons standing on the back "
            "of the hand and no ring, band or ornament of any kind on it, the DARK "
            "CHARCOAL-BROWN sleeve at the wrist and the heavy DARK MURREY-PURPLE "
            "mantle falling behind the arm. No light of any kind escapes from between "
            "the fingers. Above the hand and softer in the frame, his bearded chin "
            "and the lower half of his face are visible in near-profile with the head "
            "turned well off the camera axis, the nose pointing at the RIGHT EDGE and "
            "his gaze directed at his own loaded pack animals out at the right of the "
            "picture, leaving the frame through the RIGHT EDGE."
        ),
    },
    # ================================== THE PRICE ==============================
    {
        # ANCHOR B — the SELLER's face. Generated in its OWN run before every other
        # beat, so REFS["SELLER"] exists when the rest are built.
        "id": "v2-r029-b15", "out": "s15-one-pearl-of-great-price.jpeg",
        "seg": "j2", "window": "43.330-46.950",
        "locks": ["SELLER", "MARKET", "MARKET-TOWN", "PEARL"],
        "narration": "Who, when he had found one pearl of great price,",
        "must_show": "THE OLD SELLER'S FACE, large and clearly lit in bright morning, one knotted hand resting flat on the dark cloth beside the great pearl — an old dealer who knows exactly what he is holding and exactly what it will cost.",
        "must_not_show": _NO_JESUS + "no road, no camel, no courtyard; no glow, halo, aura, inner light, sparkle, starburst or lens flare on the pearl; no second person sharp in the frame; no modern table, trestle, metal pole, umbrella, striped or printed awning, plastic crate or tray; no minaret, bell tower, dome or tiled roof; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, CLEAR BRIGHT "
            "MORNING LIGHT falling from the open sky at the right across the deep "
            "creases of his face and lighting his white beard, fine film grain. THE "
            "CAMERA STANDS IN THE MARKET CLOSE IN FRONT OF THE STALL AND SLIGHTLY TO "
            "HIS LEFT AND ABOVE HIM, AND HIS HEAD IS TURNED WELL OFF THE CAMERA AXIS "
            "INTO THREE-QUARTER VIEW WITH HIS NOSE POINTING DOWN TOWARD THE BOTTOM "
            "RIGHT CORNER OF THE FRAME. HIS GAZE HAS A NAMED TARGET INSIDE THE "
            "PICTURE: the great pearl lying on the folded DARK INDIGO cloth on the "
            "plank at the bottom right of the frame, so his eyeline runs steeply down "
            "and rightward and leaves the picture through the BOTTOM RIGHT CORNER, "
            "nowhere near the lens. Sharp and filling the frame from the chest up is "
            "the old seller — a small stooped thin dealer of about seventy with dark "
            "leathery deeply-creased olive skin, a narrow bony face, heavy white "
            "brows, shrewd dark eyes, thin white hair and a long thin "
            "WHITE beard falling to his chest, under a DARK SLATE-GREY head cloth "
            "bound with a dark cord, in a DARK OLIVE-DRAB wool tunic with a DEEP "
            "RUST-BROWN mantle over both shoulders and a twisted dark brown cord at "
            "the waist. His expression is unreadable and entirely awake — the face of "
            "a man who has handled pearls for fifty years and knows precisely what is "
            "lying on his cloth. One knotted arthritic hand rests flat on the plank "
            "beside the folded dark cloth, on which the great pearl sits alone, warm "
            "milky white, softly lustrous and throwing no light. The near foreground "
            "along the bottom edge is the dark hewn plank and the stacked stone "
            "blocks under it, sharp and close, with nobody between the camera and "
            "him. Behind him the dark goat-hair awning and the flat-roofed honey "
            "limestone houses fall completely out of focus."
        ),
    },
    {
        "id": "v2-r029-b16", "out": "s16-sold-all-that-he-had.jpeg",
        "seg": "j2", "window": "46.950-48.770", "wide": True,
        "locks": ["MERCHANT", "BUYERS", "MARKET", "MARKET-TOWN", "PEARL"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "went and sold all that he had,",
        "must_show": "the merchant's entire stock laid out on the market flags at hard noon and being carried away by buyers — his lesser pearls on their dark cloths, his bales, his baskets, his camels being led off — the man himself standing among it letting all of it go.",
        "must_not_show": _NO_JESUS + "no road country, no bare hills, no courtyard; no glow, halo, aura, sparkle or lens flare on any pearl; no modern table, trestle, metal pole, umbrella, striped or printed awning, plastic crate, tray or bag; no painted board, price sign or lettering anywhere; no minaret, bell tower, dome, spire or tiled roof against the sky; " + _NO_CREAM + "not one face turned toward the lens.",
        "scene": (
            "One photograph, 24mm lens, deep depth of field, HARD HIGH NOON SUN "
            "almost straight overhead so every person and bale throws a short black "
            "shadow directly beneath itself and the pale limestone flags glare, fine "
            "film grain. THE CAMERA STANDS OUT IN THE OPEN MARKET WELL BEHIND AND TO "
            "ONE SIDE OF THE WHOLE GROUP AND SHOOTS PAST THEM ACROSS THE FLAGS, so "
            "the nearest townspeople are seen from behind and from the side and NOT "
            "ONE FACE IS TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE AND "
            "NOT A PORTRAIT: the camera is far enough back that eight or nine people "
            "are visible head to sandals across the market floor. Spread out on the "
            "worn pale flags in the middle of the frame is a whole trading stock: four "
            "folded squares of DARK INDIGO wool with small dull lesser pearls laid "
            "separate on them, stacked dark goat-hair bales, split-reed baskets, "
            "fired-clay jars, coils of twisted fibre cord and folded dark woollen "
            "cloth. Dark-clothed townspeople — working men, two women and a boy, each "
            "with a distinct face, all seen from behind or in profile — are stooping "
            "over the goods, lifting bales onto their shoulders and carrying baskets "
            "away toward the left of the frame. At the far side two of his camels are "
            "being led off by their halters. Standing still among all of it in "
            "three-quarter from behind is the merchant, in his DARK CHARCOAL-BROWN "
            "wool tunic, heavy DARK MURREY-PURPLE mantle, DARK OCHRE-BROWN sash and "
            "DARK CHARCOAL-BROWN head cloth, one hand hanging open at his side and "
            "his head turned away toward the departing camels at the RIGHT EDGE, "
            "letting all of it go. The near foreground across the bottom of the frame "
            "is the bare sunlit limestone flags with the short black shadow of a "
            "stall plank across them, with nobody between the camera and the group. "
            "Behind them the low dry-laid sea wall and the flat blue-green sea run "
            "out to a clean horizon under a bleached noon sky."
        ),
    },
    {
        "id": "v2-r029-b17", "out": "s17-and-bought-it.jpeg",
        "seg": "j2", "window": "48.770-51.820",
        "locks": ["MERCHANT", "SELLER", "MARKET", "MARKET-TOWN"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg",
                      "assets/s15-one-pearl-of-great-price.jpeg"],
        "narration": "and bought it.",
        "must_show": "the price being paid — the merchant's hands tipping a heavy quantity of irregular hand-struck silver coins out onto the dark cloth on the stall plank into the old seller's waiting knotted hands, close in, with the stone market behind.",
        "must_not_show": _NO_JESUS + "no road, no camel country, no courtyard; no glow, halo, aura, sparkle or lens flare anywhere; no milled, ridged, reeded or knurled coin edge, no perfectly round machined disc, no stacked or rolled coins, no modern date or numeral; no purse with a metal clasp, buckle or zip; no modern table, trestle, metal pole or printed awning; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm lens, shallow depth of field, HARD HIGH NOON SUN "
            "coming almost straight down onto the plank so the coins throw tiny sharp "
            "shadows, fine film grain. THE CAMERA STANDS IN THE MARKET LEANING IN "
            "CLOSE OVER THE END OF THE STALL PLANK FROM ONE SIDE, TILTED SO THAT THE "
            "TOP QUARTER OF THE FRAME CARRIES A CLEAR BAND OF THE MARKET BEHIND — the "
            "worn pale limestone flags, the stacked stone blocks under the plank and "
            "the out-of-focus dark goat-hair awning above — so the picture can never "
            "read as a modern tabletop. Filling the frame are four hands over a "
            "folded square of DARK INDIGO wool on the hewn plank. From the LEFT come "
            "the merchant's clean long-fingered uncallused BARE hands, with no ring, "
            "band, bracelet or ornament of any kind on either of them, the DARK "
            "CHARCOAL-BROWN sleeves at the wrists, tipping a coarse dark goat-hair cloth pouch so that a "
            "heavy stream of IRREGULAR HAND-STRUCK SILVER COINS pours out and spreads "
            "across the dark wool — each coin a small uneven lump of dull tarnished "
            "grey-white metal with a worn off-centre ruler's head beaten into one "
            "face and a worn rim legend, no two exactly alike and none of them shiny. "
            "From the RIGHT come the old seller's knotted arthritic hands, dark and "
            "deeply creased, the DARK OLIVE-DRAB sleeve and the DEEP RUST-BROWN "
            "mantle edge at the wrist, opening flat to receive them. The pile of "
            "silver is plainly a great deal of money. No face is in the frame at all."
        ),
    },
    # ============================== THE EMPTYING — hard noon ===================
    {
        "id": "v2-r029-b18", "out": "s18-he-went-home-and-sold-everything.jpeg",
        "seg": "n6", "window": "51.820-53.980", "wide": True,
        "locks": ["MERCHANT", "BUYERS", "COURTYARD"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "He went home and sold everything.",
        "must_show": "the merchant's own dressed-limestone courtyard at hard noon with his household goods being carried out of the storerooms and set down on the flags — the emptying beginning, and him standing in the middle of it directing it himself.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no road and no camel; no mud brick, no dirt slope, no thorn pen and no poor hut anywhere; no dome, tower, minaret, bell tower, arch of voussoirs, tiled or pitched roof, column, glass, shutter, hinge, railing, sheet metal, pipe, wire or cable; " + _NO_CREAM + "not one face turned toward the lens.",
        "scene": (
            "One photograph, 24mm lens, deep depth of field, HARD HIGH NOON SUN "
            "almost straight overhead so the courtyard walls throw almost no shadow "
            "and the dressed limestone flags glare, fine film grain. THE CAMERA "
            "STANDS INSIDE THE COURTYARD IN THE NEAR CORNER BESIDE THE CEDAR DOORWAY, "
            "SHOOTING ACROSS AND PAST THE PEOPLE toward the far wall, so the nearest "
            "figures are seen from behind and in profile and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE AND NOT A PORTRAIT: "
            "the camera is far enough back that six or seven people are visible head "
            "to sandals with the courtyard walls and the outside stone stair behind "
            "them. Dark-clothed townspeople are carrying goods out of the two plain "
            "rectangular storeroom openings in the far wall and setting them down on "
            "the flags — fired-clay jars, split-reed baskets, folded stacks of dark "
            "woollen cloth and rolled bedding — each with a distinct face, all seen "
            "from behind or in profile. "
            "Standing in the middle of the courtyard in clean three-quarter from "
            "behind is the merchant — a spare travelled trader of about forty-five in "
            "a DARK CHARCOAL-BROWN wool tunic to the ankle, a heavy DARK "
            "MURREY-PURPLE mantle over his left shoulder, a DARK OCHRE-BROWN sash and "
            "a DARK CHARCOAL-BROWN head cloth — one arm raised and pointing toward "
            "the storeroom openings, directing the emptying of his own house himself, "
            "his head turned away toward the far wall at the TOP RIGHT of the frame. "
            "The near foreground across the bottom of the frame is the worn dressed "
            "limestone flags with the great fired-clay water jar on its flat stone at "
            "the near left, sharp and close, with nobody between the camera and the "
            "group. Above the honey limestone walls there is only open bleached noon "
            "sky and the flat line of the packed-earth roof."
        ),
    },
    {
        "id": "v2-r029-b19", "out": "s19-his-house-his-goods.jpeg",
        "seg": "n6", "window": "53.980-56.860",
        "locks": ["MERCHANT", "BUYERS", "COURTYARD"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "His house, his goods, every other pearl he owned,",
        "must_show": "the merchant handing over his own folded dark cloths of lesser pearls into a buyer's hands in his stripped courtyard at noon — the last of the stock, given up without hesitation.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no road and no camel; no mud brick, no dirt slope and no poor hut; no glow, halo, aura, sparkle or lens flare on any pearl; no dome, tower, minaret, tiled roof, column, glass, shutter, railing, sheet metal, pipe or wire; " + _NO_CREAM + "no face turned toward the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, HARD HIGH NOON SUN "
            "straight overhead throwing short black shadows directly under both men, "
            "fine film grain. THE CAMERA STANDS INSIDE THE COURTYARD COMPLETELY "
            "SIDE-ON TO THE TWO MEN AND SHOOTS ACROSS THE EXCHANGE AT RIGHT ANGLES TO "
            "BOTH EYELINES, so the whole handover runs HORIZONTALLY ACROSS THE FRAME "
            "and NOT ONE FACE IS SQUARED UP TO THE LENS. Framed from the knees up at "
            "the LEFT, seen in clean profile facing right, is the merchant — a spare "
            "travelled trader of about forty-five with weathered olive-brown skin, a "
            "lean face and a full close-trimmed DARK BROWN beard shot with grey. HIS "
            "HEAD IS COVERED AND THE HEAD CLOTH IS A VISIBLE PART OF THE "
            "COMPOSITION: a DARK CHARCOAL-BROWN woven head cloth is wound over his "
            "hair and bound with a dark brown cord, and its LONG LOOSE END HANGS DOWN "
            "THE BACK OF HIS NECK AND OVER HIS FAR SHOULDER, swinging clear of the "
            "mantle, so the cloth is unmistakably there and no part of his bare hair, "
            "scalp or crown is visible anywhere in the picture. He is in a DARK "
            "CHARCOAL-BROWN wool tunic and a heavy DARK MURREY-PURPLE mantle — "
            "holding out with both hands a small stack of folded DARK INDIGO woollen "
            "squares with small dull lesser pearls visible on the topmost one, his "
            "arms already fully extended and his fingers loosening, his gaze level and "
            "rightward on the other man's hands and leaving the frame through the "
            "RIGHT EDGE. At the RIGHT, in profile facing left, a dark-clothed "
            "townsman in a DEEP INDIGO tunic and DARK UMBER head cloth reaches to take "
            "them, his gaze leaving the frame through the LEFT EDGE. There is no "
            "hesitation and no grief in the merchant's face; his mouth is calm. The "
            "near foreground across the bottom of the frame is the sunlit worn "
            "dressed limestone flags of the courtyard, sharp and close, with nobody "
            "between the camera and the two men. Behind them the honey limestone "
            "courtyard wall, the outside stone stair climbing to the flat roof and "
            "the empty rectangular storeroom openings fall softly out of focus."
        ),
    },
    {
        "id": "v2-r029-b20", "out": "s20-all-of-it-gone.jpeg",
        "seg": "n6", "window": "56.860-60.710", "wide": True,
        "locks": ["MERCHANT", "COURTYARD"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "All of it, gone, to buy the one.",
        "must_show": "the completely stripped courtyard at hard noon — bare flags, empty storeroom openings, nothing left standing but the water jar — with the merchant alone and small in the middle of it, seen from behind.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no road and no camel; no second person anywhere in the frame; no goods, no bales, no baskets and no jars except the one water jar; no mud brick, no dirt slope and no poor hut; no dome, tower, minaret, tiled roof, column, glass, railing, sheet metal, pipe or wire; " + _NO_CREAM + "no face turned toward the lens.",
        "scene": (
            "One photograph, 24mm lens, deep depth of field, HARD HIGH NOON SUN "
            "almost straight overhead so the whole courtyard is flat, glaring and "
            "shadowless with only a short black shadow directly under the man's own "
            "feet, fine film grain. THE CAMERA STANDS INSIDE THE COURTYARD IN THE "
            "NEAR CORNER WELL BEHIND HIM AND LOW, SHOOTING PAST HIM TOWARD THE FAR "
            "WALL, so he is seen SQUARELY FROM BEHIND and not one part of his face is "
            "turned toward the lens; his own gaze is out across the empty courtyard "
            "away from the camera. The near foreground across the bottom of the frame "
            "is the bare worn dressed limestone flags of the courtyard floor, sharp "
            "and close, with nobody and nothing between the camera and him. Standing "
            "alone in the middle of the enclosure with his back to us, small enough "
            "in the frame that the whole courtyard fits around him, is the merchant — "
            "a spare travelled trader in a DARK CHARCOAL-BROWN wool tunic to the "
            "ankle, a heavy DARK MURREY-PURPLE mantle over his left shoulder, a DARK "
            "OCHRE-BROWN sash and a DARK CHARCOAL-BROWN head cloth, his arms hanging "
            "loose and open away from his sides and his head up. THE COURTYARD IS "
            "COMPLETELY EMPTY: the honey limestone walls close it on all four sides, "
            "the two plain rectangular storeroom openings in the far wall are dark and "
            "bare inside, the outside stone stair climbs the right-hand wall to the "
            "flat packed-earth roof, and the ONLY object left standing anywhere on "
            "the flags is the great fired-clay water jar on its flat stone in one "
            "corner. Above the walls there is nothing but open bleached noon sky."
        ),
    },
    # ================= FRAME + the gladness ====================================
    {
        "id": "v2-r029-b21", "out": "s21-and-here-is-the-thing.jpeg",
        "seg": "n7", "window": "60.710-62.070", "jesus": True, "ref": REF,
        "locks": ["SHELF", "DISCIPLES"],
        "narration": "And here is the thing.",
        "must_show": "Jesus leaning in close on the limestone shelf in warm late-afternoon light, dropping his voice for the point of the whole story, his face intent and warm.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no overcast, no midday glare; no tree, no canopy, no dappled light, no building and no roof; no market, no stall, no sea, no road, no camel, no courtyard and no pearl; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, warm low "
            "late-afternoon sun coming in level from the right across his face with "
            "soft bounce off the pale rock under his jaw, fine film grain. THE CAMERA "
            "IS SET LOW ON THE ROCK WELL TO HIS LEFT AND LOOKING SLIGHTLY UP AT HIM, "
            "AND HIS HEAD IS TURNED WELL OFF THE CAMERA AXIS INTO THREE-QUARTER VIEW "
            "WITH HIS NOSE POINTING AT THE RIGHT EDGE OF THE FRAME. HIS GAZE HAS A "
            "NAMED TARGET INSIDE THE PICTURE: the nearest seated disciple out at the "
            "right of the frame, whose dark out-of-focus shoulder and head cloth are "
            "visible there, so his eyeline runs level and rightward and leaves the "
            "picture through the RIGHT EDGE. Sharp and filling the frame from the "
            "chest up, Jesus is leaning well forward off the limestone slab with his "
            "forearms on his knees and his hands loosely clasped between them, come in "
            "close the way a man does when he is about to say the thing that matters, "
            "his face intent, warm and completely unguarded. The near foreground at "
            "the bottom left corner is ONE out-of-focus DARK UMBER shouldered back, a "
            "solid dark saturated mass edge to edge, and there is nothing else "
            "between the camera and him. Behind him the bare pale grey cracked rock, "
            "the dry stony wadi and the folded tawny hills fall completely out of "
            "focus."
        ),
    },
    {
        "id": "v2-r029-b22", "out": "s22-he-did-not-do-it-grieving.jpeg",
        "seg": "n7", "window": "62.070-63.810",
        "locks": ["MERCHANT", "COURTYARD"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "He did not do it grieving.",
        "must_show": "the merchant's face close in his emptied courtyard at noon — steady, clear-eyed and quietly glad, the exact opposite of a man in mourning.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no road and no camel; no sorrow, no tears, no downturned mouth, no bowed head and no mourning of any kind; no second person in the frame; no mud brick, no dirt slope and no poor hut; no dome, tower, minaret, tiled roof, glass, railing, sheet metal, pipe or wire; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, HARD HIGH "
            "NOON SUN from almost overhead and slightly to the left, with strong "
            "bounce off the pale limestone flags filling the light back under his jaw "
            "so nothing is lost in shadow, fine film grain. THE CAMERA STANDS INSIDE "
            "THE COURTYARD WELL TO HIS RIGHT AND AT EYE HEIGHT, AND HIS HEAD IS "
            "TURNED WELL OFF THE CAMERA AXIS INTO THREE-QUARTER VIEW WITH HIS NOSE "
            "POINTING AT THE LEFT EDGE OF THE FRAME. HIS GAZE HAS A NAMED TARGET "
            "INSIDE THE PICTURE: the empty storeroom openings in the far courtyard "
            "wall out at the left of the frame, visible there out of focus, so his "
            "eyeline runs level and leftward and leaves the picture through the LEFT "
            "EDGE, well away from the lens. Sharp and filling the frame from the "
            "shoulders up is the merchant — a spare travelled trader of about "
            "forty-five with weathered olive-brown skin, a lean "
            "intelligent face, a high straight nose, deep lines at the outer corners "
            "of the eyes, a full close-trimmed DARK BROWN beard shot with grey and "
            "dark brown hair to the jaw under a DARK CHARCOAL-BROWN head cloth, in a "
            "DARK CHARCOAL-BROWN wool tunic with a heavy DARK MURREY-PURPLE mantle "
            "over his left shoulder. HIS FACE IS THE PICTURE AND IT IS NOT GRIEF: his "
            "head is up, his eyes are clear and steady and dry, the deep lines at "
            "their corners are pulled slightly up, and one corner of his mouth has "
            "gone soft with a quiet private gladness — the settled look of a man who "
            "has done exactly what he wanted to do. The near foreground at the bottom "
            "right corner is the out-of-focus dark shoulder of a stacked dark "
            "goat-hair bale being carried past, a solid dark mass, with nobody "
            "between the camera and him. Behind him the honey limestone courtyard "
            "wall and the outside stone stair fall completely out of focus."
        ),
    },
    {
        "id": "v2-r029-b23", "out": "s23-he-did-not-feel-robbed.jpeg",
        "seg": "n7", "window": "63.810-65.850",
        "locks": ["MERCHANT", "BUYERS", "COURTYARD"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "He did not feel robbed.",
        "must_show": "the merchant's own hands letting go of the last bale into a buyer's arms, close in — fingers open, palms lifting away, the physical gesture of release rather than loss.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no road and no camel; no clutching, gripping, snatching or holding back of any kind; no tears; no mud brick, no dirt slope and no poor hut; no dome, tower, minaret, tiled roof, glass, railing, sheet metal, pipe or wire; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm lens, shallow depth of field, HARD HIGH NOON SUN "
            "from almost overhead raking across the backs of the hands and the coarse "
            "weave of the bale, strong bounce off the pale flags below, fine film "
            "grain. THE CAMERA STANDS INSIDE THE COURTYARD CLOSE IN AND WELL TO ONE "
            "SIDE OF THE HANDOVER AT CHEST HEIGHT, TILTED SLIGHTLY UP SO THAT THE "
            "UPPER PART OF THE FRAME CARRIES A CLEAR BAND OF THE COURTYARD BEHIND — "
            "the honey limestone wall of dressed blocks, the outside stone stair and "
            "the flat packed-earth roofline, all out of focus — so the picture can "
            "never read as a modern interior. Sharp and filling the centre of the "
            "frame are the merchant's two hands coming AWAY from a stacked dark "
            "goat-hair bale: the fingers fully open and lifting clear, the palms "
            "turned outward and upward, the DARK CHARCOAL-BROWN sleeves at the "
            "wrists, no ring, band or ornament of any kind on either hand, and no grip "
            "left anywhere in them. Below and beyond, a dark-clothed townsman's arms "
            "in a DEEP INDIGO sleeve have closed round the bale and taken its whole "
            "weight. The gesture is unmistakably RELEASE and not loss. Softer at the "
            "top of the frame the merchant's bearded chin and the lower half of his "
            "face are visible in three-quarter with the head turned well off the "
            "camera axis, the nose pointing at the LEFT EDGE and the gaze directed at "
            "the townsman's face out at the left of the picture."
        ),
    },
    {
        "id": "v2-r029-b24", "out": "s24-he-gave-up-everything-gladly.jpeg",
        "seg": "n7", "window": "65.850-68.770", "wide": True,
        "locks": ["MERCHANT", "COURTYARD"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "He gave up everything he had, gladly, because",
        "must_show": "the merchant walking out through his own tall cedar doorway at the first warm gold of dawn, carrying nothing but one small dark pouch, the emptied courtyard behind him — everything gone and his step easy.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no road and no camel; no noon glare, no overcast and no night; no goods, bales, baskets or animals; no second person in the frame; no mud brick, no dirt slope and no poor hut; no dome, tower, minaret, tiled roof, glass, hinge, railing, sheet metal, pipe or wire; " + _NO_CREAM + "no face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, THE FIRST WARM GOLD OF DAWN coming in low "
            "from the left over the courtyard wall, laying one long bar of warm light "
            "across the flags and leaving the rest of the courtyard in cool blue "
            "shade, fine film grain. THE CAMERA STANDS INSIDE THE COURTYARD WELL "
            "BEHIND HIM AND LOW, SHOOTING PAST HIM THROUGH THE OPEN CEDAR DOORWAY, so "
            "he is seen SQUARELY FROM BEHIND, walking AWAY from the camera, and not "
            "one part of his face is turned toward the lens. THIS IS A WIDE "
            "FULL-LENGTH SCENE AND NOT A PORTRAIT: the camera is far enough back that "
            "he is visible head to sandals with the whole emptied courtyard, the "
            "outside stone stair and the tall doorway around him. The near foreground "
            "across the bottom of the frame is the bare worn dressed limestone flags "
            "of the empty courtyard, sharp and close, with nothing and nobody between "
            "the camera and him. Walking away toward the doorway in the middle "
            "distance is the merchant — a spare travelled trader in a DARK "
            "CHARCOAL-BROWN wool tunic to the ankle, a heavy DARK MURREY-PURPLE "
            "mantle over his left shoulder, a DARK OCHRE-BROWN sash and a DARK "
            "CHARCOAL-BROWN head cloth — carrying NOTHING but one small dark "
            "goat-hair pouch in his left hand, his shoulders loose, his stride easy "
            "and unhurried, his head up toward the light in the doorway. Behind and "
            "around him the courtyard is completely bare: honey limestone walls on "
            "all four sides, two dark empty storeroom openings in the far wall, the "
            "stone stair climbing the right-hand wall, and one great fired-clay water "
            "jar on its flat stone. Through the open doorway ahead of him the pale "
            "gold morning sky and the flat roofline of the town are visible."
        ),
    },
    {
        "id": "v2-r029-b25", "out": "s25-worth-more-than-all-of-it.jpeg",
        "seg": "n7", "window": "68.770-73.490",
        "locks": ["MERCHANT", "COURTYARD", "PEARL"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "what he was getting was worth more than all of it put together.",
        "must_show": "the great pearl alone in the merchant's open palm in the low warm gold of dawn, held out level, with the completely emptied courtyard visible and out of focus behind it — the whole trade in one frame.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no road and no camel; no glow, halo, aura, inner light, radiance, rays, sparkle, starburst, lens flare or bloom on the pearl; no light thrown from the pearl onto the palm or the air; no glassy CGI sphere; no goods, bales or baskets in the courtyard; no dome, tower, minaret, tiled roof, glass, railing, sheet metal, pipe or wire; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, THE FIRST "
            "WARM GOLD OF DAWN coming in low from the left so it rakes right across "
            "the palm and lays ONE small clean highlight on the pearl's upper "
            "shoulder and a long quiet shadow beside it in the creases of the hand, "
            "fine film grain. THE CAMERA STANDS INSIDE THE EMPTIED COURTYARD CLOSE IN "
            "FRONT OF HIS OUTHELD HAND AND SLIGHTLY BELOW IT, TILTED UP SO THAT THE "
            "UPPER HALF OF THE FRAME CARRIES A CLEAR BAND OF THE COURTYARD BEHIND — "
            "the bare dressed limestone flags, the honey limestone wall of dressed "
            "blocks, the dark empty rectangular storeroom openings and the outside "
            "stone stair, all far out of focus — so the picture can never read as a "
            "modern studio shot, and so the emptiness behind the hand is legible. "
            "Sharp and filling the lower half of the frame is the merchant's clean, "
            "dry, long-fingered open right palm held out level, uncallused, with no ring, band or ornament of any kind on it and the DARK CHARCOAL-BROWN "
            "sleeve of his tunic at the wrist. Resting alone in the hollow of the "
            "palm is the great pearl — a single rounded natural pearl about the size "
            "of a large hazelnut, slightly irregular rather than a machined sphere, "
            "warm milky white shading to the faintest silver-rose in its depths, with "
            "a deep soft satiny sheen. It takes the dawn light and gives back a quiet "
            "lustre and throws no light of its own onto the hand, the sleeve or the "
            "air. Nothing else is in the hand and nothing else is in the courtyard."
        ),
    },
    # ================= n8 — the easiest trade =================================
    {
        "id": "v2-r029-b26", "out": "s26-what-finding-the-real-thing-does.jpeg",
        "seg": "n8", "window": "73.490-76.270", "wide": True,
        "locks": ["SHELF", "DISCIPLES"],
        "narration": "That is what finding the real thing does.",
        "must_show": "the disciples' faces on the limestone shelf in warm late-afternoon light, several of them together, caught in the middle of understanding it — leaning in, one man's brows lifting.",
        "must_not_show": "no Jesus in this frame; no halo, glow or rim-light anywhere; no night, no lamp, no overcast, no midday glare; no tree, no canopy, no dappled light, no building and no roof; no market, no stall, no sea, no road, no camel, no courtyard and no pearl; " + _NO_CREAM + "not one face turned toward the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, warm low "
            "late-afternoon sun coming in almost level from the left across the open "
            "pale grey rock and across their faces, fine film grain. THE CAMERA IS "
            "PLACED COMPLETELY SIDE-ON TO THE SEATED MEN AND SHOOTS ACROSS THEM AT "
            "RIGHT ANGLES TO EVERY EYELINE, so every face is in profile or "
            "three-quarter and NOT ONE IS SQUARED UP TO THE LENS. THIS IS A WIDE "
            "MULTI-FIGURE SCENE AND NOT A PORTRAIT: five of the disciples are in the "
            "frame together, seated low on the bare limestone shelf and visible from "
            "the knees up, ranged from the near left to the middle distance at the "
            "right. EVERY MAN'S GAZE HAS THE SAME NAMED TARGET INSIDE THE PICTURE: a "
            "point out beyond the LEFT EDGE of the frame where Jesus is sitting "
            "unseen, so every eyeline runs level and leftward and leaves the picture "
            "through the LEFT EDGE. They are Galilean working men between twenty-five "
            "and fifty, each with a distinct face, build and beard and none of them "
            "repeated — one older man with a grey beard leaning well forward with his "
            "elbows on his knees, one younger man with his brows lifting and his lips "
            "just parting as it lands, one broad-shouldered man very still. EVERY "
            "SEPARATE PIECE OF CLOTH ON EVERY ONE OF THEM IS A DARK SATURATED COLOUR "
            "— DEEP INDIGO, DARK UMBER, DARK OLIVE-DRAB and RUSSET-RED tunics with "
            "head cloths of the same dark cloth and no pale scarf, stole or shawl "
            "anywhere. The near foreground at the bottom left corner is ONE "
            "out-of-focus DEEP INDIGO shouldered back, a solid dark mass edge to "
            "edge, with nobody else between the camera and them. Behind them the bare "
            "cracked pale grey rock of the shelf, the dry stony wadi and the folded "
            "tawny hills fall away out of focus."
        ),
    },
    {
        "id": "v2-r029-b27", "out": "s27-what-your-whole-life-looked-for.jpeg",
        "seg": "n8", "window": "76.270-79.330",
        "locks": ["MERCHANT", "COURTYARD", "PEARL"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "When you finally find what your whole life was looking for,",
        "must_show": "the merchant sitting alone on the worn stone threshold of his emptied house in the low warm gold of dawn, the pearl held closed in both hands against his chest, his face at rest.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no road and no camel; no noon glare, no overcast and no night; no glow, halo, aura, sparkle or lens flare on the pearl or between his hands; no goods, bales or baskets; no second person in the frame; no mud brick, no dirt slope and no poor hut; no dome, tower, minaret, tiled roof, glass, hinge, railing, sheet metal, pipe or wire; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, THE FIRST WARM GOLD "
            "OF DAWN coming in low from the left across his chest and the side of his "
            "face, the rest of the courtyard still in cool blue shade, fine film "
            "grain. THE CAMERA STANDS INSIDE THE COURTYARD WELL TO HIS LEFT AND LOW, "
            "ALMOST DOWN ON THE FLAGS, SHOOTING HIM IN CLEAN THREE-QUARTER PROFILE "
            "WITH HIS HEAD TURNED WELL OFF THE CAMERA AXIS AND HIS NOSE POINTING AT "
            "THE RIGHT EDGE OF THE FRAME. HIS GAZE HAS A NAMED TARGET INSIDE THE "
            "PICTURE: the low dawn light on the top of the courtyard wall at the "
            "upper right of the frame, so his chin is slightly lifted and his eyeline "
            "runs up and rightward and leaves the picture through the TOP RIGHT "
            "CORNER. Framed from the knees up, seated on the worn stone threshold "
            "under the tall hewn cedar doorway with his back against the jamb, is the "
            "merchant — a spare travelled trader of about forty-five with weathered "
            "olive-brown skin, a lean face, a full close-trimmed DARK BROWN beard "
            "shot with grey, dark brown hair to the jaw under a DARK CHARCOAL-BROWN "
            "head cloth, in a DARK CHARCOAL-BROWN wool tunic and a heavy DARK "
            "MURREY-PURPLE mantle over his left shoulder. Both his hands are closed "
            "loosely together and held against his own chest with the great pearl "
            "inside them; no light escapes between his fingers. His shoulders have "
            "come down, his mouth is relaxed, and his whole face is at rest. The near "
            "foreground across the bottom of the frame is the bare worn dressed "
            "limestone flags of the empty courtyard, sharp and close, with nobody "
            "between the camera and him. Behind him the honey limestone wall and the "
            "dark empty storeroom openings fall out of focus."
        ),
    },
    {
        "id": "v2-r029-b28", "out": "s28-letting-go-is-not-a-loss.jpeg",
        "seg": "n8", "window": "79.330-81.790", "wide": True,
        "locks": ["MERCHANT", "COURTYARD"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "letting go of the rest is not a loss.",
        "must_show": "a wide photograph of the completely empty courtyard filled with the low warm gold of dawn, the merchant small on the threshold at one side — the emptiness reading as peace and space rather than as ruin.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no road and no camel; no noon glare, no overcast and no night; no second person in the frame; no goods, bales, baskets or animals; no rubble, no wreckage, no broken thing and nothing that reads as ruin; no mud brick, no dirt slope and no poor hut; no dome, tower, minaret, tiled roof, glass, railing, sheet metal, pipe or wire; " + _NO_CREAM + "no face turned toward the lens.",
        "scene": (
            "One photograph, 24mm lens, deep depth of field, THE FIRST WARM GOLD OF "
            "DAWN coming in low over the left-hand courtyard wall and laying long "
            "warm bars of light and long soft blue shadows right across the bare "
            "flags, the air clean and still, fine film grain. THE CAMERA STANDS "
            "INSIDE THE COURTYARD IN THE FAR CORNER, HIGH AT THE HEAD OF THE OUTSIDE "
            "STONE STAIR, AND IT IS TILTED STEEPLY DOWNWARD so that it looks down "
            "into the enclosure and NO SKYLINE, NO HORIZON, NO SKY AND NO ROOFTOP OF "
            "ANY OTHER BUILDING IS IN THE FRAME AT ALL — the courtyard's own walls "
            "close the top edge of the picture and everything above them is cropped "
            "away, so no roof of any kind can appear. The "
            "man below is seen from above and from behind at an angle and no part of "
            "his face is turned toward the lens. THIS IS A WIDE FULL-LENGTH SCENE AND "
            "NOT A PORTRAIT: the whole courtyard floor is in the frame, wall to wall, "
            "and the man is small within it. The near foreground across the bottom of the "
            "frame is the worn dressed stone of the stair treads and the flat "
            "packed-earth roof edge, sharp and close, with nobody between the camera "
            "and the courtyard. Below, THE COURTYARD IS COMPLETELY EMPTY AND CLEAN — "
            "bare worn limestone flags edge to edge, honey limestone walls closing all "
            "four sides, two dark bare rectangular storeroom openings in the far wall, "
            "and one great fired-clay water jar standing on its flat stone in a "
            "corner; nothing is broken, spilled, tipped over or left lying anywhere. "
            "Small at one side, seated on the worn stone threshold under the tall "
            "hewn cedar doorway with his back against the jamb, is the merchant — a "
            "spare travelled trader in a DARK CHARCOAL-BROWN wool tunic, a heavy DARK "
            "MURREY-PURPLE mantle over his left shoulder, a DARK OCHRE-BROWN sash and "
            "a DARK CHARCOAL-BROWN head cloth — his hands closed together at his "
            "chest and his head turned away toward the lit wall. The top edge of the "
            "picture is the plain flat coping of the courtyard's own honey limestone "
            "wall and nothing whatever is visible beyond or above it."
        ),
    },
    {
        "id": "v2-r029-b29", "out": "s29-the-easiest-trade-youll-ever-make.jpeg",
        "seg": "n8", "window": "81.790-85.480",
        "locks": ["MERCHANT", "COURTYARD"],
        "char_refs": ["assets/s10-and-then-one-day-he-found-it.jpeg"],
        "narration": "It is the easiest trade you will ever make.",
        "must_show": "THE MERCHANT'S FACE OPEN IN UNMISTAKABLE QUIET JOY in the low warm gold of dawn — eyes creased, a real smile broken across his face, entirely released.",
        "must_not_show": _NO_JESUS + "no market, no stall, no sea, no road and no camel; no noon glare, no overcast and no night; no sorrow, no restraint and no solemnity; no second person in the frame; no pearl visible; no mud brick, no dirt slope and no poor hut; no dome, tower, minaret, tiled roof, glass, railing, sheet metal, pipe or wire; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, THE FIRST "
            "WARM GOLD OF DAWN coming in low from the left straight across his face, "
            "clean and warm, with soft bounce off the pale limestone flags filling "
            "under his jaw, fine film grain. THE CAMERA IS SET LOW ON THE COURTYARD "
            "FLAGS WELL TO HIS RIGHT AND LOOKING UP AT HIM, AND HIS HEAD IS TURNED "
            "WELL OFF THE CAMERA AXIS INTO THREE-QUARTER VIEW WITH HIS NOSE POINTING "
            "TOWARD THE TOP LEFT CORNER OF THE FRAME. HIS GAZE HAS A NAMED TARGET "
            "INSIDE THE PICTURE: the open gold dawn sky above the courtyard wall at "
            "the upper left of the frame, so his head is tipped back and turned up "
            "and to his own left and his eyeline leaves the picture through the TOP "
            "LEFT CORNER, far above and to the side of the lens. Sharp and filling "
            "the frame from the chest up is the merchant — a spare travelled trader "
            "of about forty-five with weathered olive-brown skin, a lean "
            "intelligent face, a high straight nose, a full close-trimmed DARK BROWN "
            "beard shot with grey at the chin and dark brown hair to the jaw under a "
            "DARK CHARCOAL-BROWN head cloth, in a DARK CHARCOAL-BROWN wool tunic with "
            "a heavy DARK MURREY-PURPLE mantle over his left shoulder. HIS FACE IS "
            "OPEN IN A REAL, UNGUARDED, QUIET JOY — the deep lines at the corners of "
            "his eyes creased right up, his eyes bright and almost closed with it, a "
            "broad genuine smile broken across his mouth, his shoulders down and "
            "loose, everything held back in him let go. The near foreground at the "
            "bottom right corner is the out-of-focus dark edge of the hewn cedar "
            "doorpost, a solid dark mass, with nobody between the camera and him. "
            "Behind him the honey limestone courtyard wall and the pale gold dawn sky "
            "fall completely out of focus."
        ),
    },
    # ================= THE TURN — back in the frame, Jesus =====================
    {
        "id": "v2-r029-b30", "out": "s30-one-more-wonder-hidden.jpeg",
        "seg": "n9", "window": "85.480-88.520", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SHELF", "DISCIPLES"],
        "narration": "And there is one more wonder hidden in this little story.",
        "must_show": "a wide photograph of Jesus and his circle on the bare limestone shelf in warm late-afternoon light, Jesus sitting back a little with the beginning of something else in his face, the men waiting on him.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no overcast, no midday glare; no tree, no canopy, no dappled light, no building and no roof; no market, no stall, no sea, no road, no camel, no courtyard and no pearl; " + _NO_CREAM + "not one face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun coming in almost "
            "level from the left across the open pale grey rock, long soft-edged "
            "shadows reaching out across the stone, fine film grain. THE CAMERA IS "
            "PLACED COMPLETELY SIDE-ON TO THE WHOLE CIRCLE, STANDING OUT ON THE ROCK "
            "WELL TO ONE SIDE AND SHOOTING ACROSS THE GROUP AT RIGHT ANGLES TO EVERY "
            "EYELINE, so the conversation runs HORIZONTALLY ACROSS THE FRAME and NOT "
            "ONE MAN'S FACE IS SQUARED UP TO THE LENS. THIS IS A WIDE FULL-LENGTH "
            "GROUP PHOTOGRAPH AND NOT A PORTRAIT: the camera is far enough back that "
            "Jesus AND at least six seated disciples are in the frame together, head "
            "to sandals, with the dry wadi and the folded tawny hills behind them, and "
            "Jesus is never framed from the chest up. Jesus sits at the RIGHT of the "
            "frame on the low limestone slab, seen from his right side, sitting back a "
            "little now with his hands quiet in his lap and his chin slightly lifted, "
            "the beginning of something else in his face; his gaze travels leftward "
            "into the seated men and exits through the LEFT EDGE. The disciples are "
            "ranged on the bare rock to the LEFT of him, every one of them in profile "
            "or three-quarter with his gaze travelling rightward and out through the "
            "RIGHT EDGE, all of them waiting on him. EXACTLY TWO out-of-focus seated "
            "BACKS fill the near bottom corners and they are the only foreground "
            "objects: a DARK OLIVE-DRAB shouldered back with a dark head cloth at the "
            "near LEFT and a RUSSET-RED back with a dark brown head cloth at the near "
            "RIGHT, BOTH A SOLID DARK SATURATED MASS FROM EDGE TO EDGE. THERE IS NO "
            "PALE, CREAM, IVORY, BEIGE, TAUPE, BUFF, SAND OR LIGHT-TAN SHAPE, "
            "SHOULDER, BACK, SLEEVE, DRAPE OR BLURRED MASS ANYWHERE IN THE FOREGROUND "
            "OR AT ANY EDGE — the ONLY pale thing in the whole frame is the wool of "
            "Jesus's own robe."
        ),
    },
    {
        "id": "v2-r029-b31", "out": "s31-read-it-the-other-way-around.jpeg",
        "seg": "n9", "window": "88.520-92.340", "jesus": True, "ref": REF,
        "locks": ["SHELF", "DISCIPLES"],
        "narration": "Some have read it the other way around, and it is just as true,",
        "must_show": "Jesus's face close in warm late-afternoon light, turning the story over — the faintest knowing warmth at his mouth, his eyes steady, as a man does when he is about to say the thing underneath the thing.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no overcast, no midday glare; no tree, no canopy, no dappled light, no building and no roof; no market, no stall, no sea, no road, no camel, no courtyard and no pearl; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, warm low "
            "late-afternoon sun coming in level from the left across his cheekbone "
            "and brow with soft bounce off the pale rock filling under his jaw, fine "
            "film grain. THE CAMERA IS SET ON THE ROCK WELL TO HIS RIGHT AND AT EYE "
            "HEIGHT, AND HIS HEAD IS TURNED WELL OFF THE CAMERA AXIS INTO CLEAN "
            "THREE-QUARTER VIEW WITH HIS NOSE POINTING AT THE LEFT EDGE OF THE FRAME. "
            "HIS GAZE HAS A NAMED TARGET INSIDE THE PICTURE: the seated disciples out "
            "at the left of the frame, whose dark out-of-focus shoulders and head "
            "cloths are visible there, so his eyeline runs level and leftward and "
            "leaves the picture through the LEFT EDGE, well away from the lens. Sharp "
            "and filling the frame from the chest up, Jesus is seated on the low "
            "limestone slab, quite still, his head slightly tilted, the faintest "
            "knowing warmth at the corner of his mouth and his eyes steady and "
            "attentive — the look of a man about to turn a thing over and show the "
            "other side of it. His hands rest quiet in his lap at the bottom of the "
            "frame. The near foreground at the bottom left corner is ONE out-of-focus "
            "DARK OLIVE-DRAB shouldered back, a solid dark saturated mass edge to "
            "edge, and there is nothing else between the camera and him. Behind him "
            "the bare cracked pale grey rock, the dry stony wadi and the folded tawny "
            "hills fall completely out of focus."
        ),
    },
    {
        "id": "v2-r029-b32", "out": "s32-to-jesus-you-are-the-pearl.jpeg",
        "seg": "n9", "window": "92.340-95.920", "jesus": True, "ref": REF,
        "locks": ["SHELF", "DISCIPLES"],
        "narration": "that to Jesus, you are the pearl.",
        "must_show": "Jesus's own two open hands, palms up and empty, resting loosely on his knees in warm late-afternoon light, with his face soft and lowered above them — the whole weight of the turn carried by empty open hands.",
        "must_not_show": "no halo, no glow, no rim-light, no aura and no light coming off Jesus or his hands; no pearl, no object and nothing at all held in his hands; no cross, no wound, no nail mark, no blood and nothing graphic anywhere; no night, no lamp, no overcast, no midday glare; no tree, no canopy, no dappled light, no building and no roof; no market, no stall, no sea, no road, no camel and no courtyard; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 100mm lens, very shallow depth of field, warm low "
            "late-afternoon sun coming in level from the left so it rakes across the "
            "backs of his fingers and lays long soft shadows into the palms, fine "
            "film grain. THE CAMERA IS SET LOW ON THE ROCK CLOSE IN FRONT OF HIM AND "
            "WELL TO HIS RIGHT, LOOKING SLIGHTLY UP AND ACROSS SO THAT A BAND OF THE "
            "OPEN SHELF, THE DRY WADI AND THE TAWNY HILLS RUNS OUT OF FOCUS ACROSS "
            "THE TOP OF THE FRAME. Sharp and filling the middle of the picture are "
            "JESUS'S OWN TWO HANDS, resting loosely on his knees with the palms "
            "TURNED UP AND COMPLETELY EMPTY, the fingers open and slightly curled, "
            "unhurried and at rest — working hands, warm olive-brown, with the "
            "undyed off-white cream wool of his own sleeves falling back at the "
            "wrists. Nothing whatever lies in them and no light comes off them. "
            "Softer above the hands in the upper part of the frame his bearded face "
            "is visible in three-quarter, the head turned well off the camera axis "
            "with the nose pointing at the LEFT EDGE and lowered so that HIS GAZE HAS "
            "A NAMED TARGET INSIDE THE PICTURE: his own open palms at the centre of "
            "the frame, his eyeline running steeply down and leftward and leaving the "
            "picture through the BOTTOM LEFT, nowhere near the lens. His expression is "
            "soft, quiet and entirely without performance."
        ),
    },
    {
        "id": "v2-r029-b33", "out": "s33-the-merchant-who-went-looking.jpeg",
        "seg": "n10", "window": "95.920-98.160", "jesus": True, "ref": REF,
        "locks": ["SHELF"],
        "narration": "That he is the merchant who went looking,",
        "must_show": "Jesus risen to his feet at the edge of the limestone shelf in warm late-afternoon light, seen from behind and the side, looking out over the dry wadi toward the hills and the far country — the one who goes out looking.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no overcast, no midday glare; no tree, no canopy, no dappled light, no building and no roof; no market, no stall, no sea, no road, no camel, no courtyard and no pearl; no other person anywhere in the frame; " + _NO_CREAM + "his face is turned away and his pupils are never centred on the lens.",
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun coming in almost "
            "level from the left across the open rock and throwing his long soft-edged "
            "shadow back across the shelf toward the camera, fine film grain. THE "
            "CAMERA STANDS OUT ON THE SHELF WELL BEHIND HIM AND SLIGHTLY TO HIS "
            "RIGHT, SHOOTING PAST HIM OUT OVER THE WADI, so he is seen from BEHIND "
            "AND IN THREE-QUARTER FROM BEHIND with his face turned away from the lens "
            "and his own gaze out across the country, leaving the picture through the "
            "far distance. THIS IS A FULL-LENGTH FIGURE IN A LANDSCAPE AND NOT A "
            "PORTRAIT: the camera is far enough back that he is visible head to "
            "sandals and the open shelf, the dry wadi and the folded hills fill most "
            "of the frame. The near foreground across the bottom is the bare cracked "
            "pale grey limestone of the shelf with a scatter of small round stones "
            "and one tuft of dry grey scrub, sharp and close, with nobody between the "
            "camera and him. Standing at the very edge of the shelf where the rock "
            "drops away into the dry stony wadi, Jesus has risen to his feet, his "
            "weight settled, one hand loose at his side and the other holding the fall "
            "of his mantle, his head up and his shoulders open, looking out at the "
            "low tawny hills folding away one behind another to the far horizon. He "
            "is the only person in the picture."
        ),
    },
    {
        "id": "v2-r029-b34", "out": "s34-who-found-you.jpeg",
        "seg": "n10", "window": "98.160-101.220", "jesus": True, "ref": REF,
        "locks": ["SHELF", "DISCIPLES"],
        "narration": "who found you, and who gave up everything he had,",
        "must_show": "Jesus turned to ONE disciple beside him on the limestone shelf, his hand come to rest on that man's shoulder, both of them in profile — the whole picture saying: this one, found.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no overcast, no midday glare; no tree, no canopy, no dappled light, no building and no roof; no market, no stall, no sea, no road, no camel, no courtyard and no pearl; no crowd and no third person sharp in the frame; " + _NO_CREAM + "not one face turned toward the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, warm low "
            "late-afternoon sun coming in level from the left across both their "
            "faces, fine film grain. THE CAMERA IS PLACED COMPLETELY SIDE-ON TO THE "
            "TWO MEN AND SHOOTS ACROSS THEM AT RIGHT ANGLES TO BOTH EYELINES, so the "
            "whole exchange runs HORIZONTALLY ACROSS THE FRAME and NEITHER FACE IS "
            "SQUARED UP TO THE LENS. Framed from the waist up at the LEFT, seen in "
            "clean profile facing right, is Jesus, seated on the low limestone slab "
            "and turned bodily toward the man beside him, his right hand come to rest "
            "open on that man's near shoulder, his face warm and wholly attentive, "
            "his gaze fixed level and rightward on the other man's face and leaving "
            "the frame through the RIGHT EDGE. At the RIGHT, in profile facing left, "
            "seated lower on the bare rock, is ONE disciple — a Galilean working man "
            "of about forty with a short dark beard, in a DEEP INDIGO wool tunic with "
            "a DARK UMBER head cloth and no pale scarf, stole or shawl of any kind — "
            "his head half turned up to Jesus and his gaze leaving the frame through "
            "the LEFT EDGE, his mouth open slightly as if he has been caught out. The "
            "near foreground at the bottom right corner is ONE out-of-focus "
            "RUSSET-RED shouldered back, a solid dark saturated mass edge to edge, "
            "and there is nothing else between the camera and them; the ONLY pale "
            "thing in the whole frame is the wool of Jesus's own robe. Behind them "
            "the bare cracked pale grey rock, the dry stony wadi and the folded tawny "
            "hills fall completely out of focus."
        ),
    },
    {
        "id": "v2-r029-b35", "out": "s35-gladly-to-buy-you-back.jpeg",
        "seg": "n10", "window": "101.220-104.660", "jesus": True, "ref": REF,
        "locks": ["SHELF", "DISCIPLES"],
        "narration": "his own life, gladly, to buy you back.",
        "must_show": "Jesus's face very close in warm late-afternoon light, quiet and steady and glad — no sorrow, no dread; the gladness of a man who has already decided and does not regret it.",
        "must_not_show": "no halo, no glow, no rim-light, no aura and no light coming off Jesus; no cross, no crucifix, no wound, no nail mark, no thorns, no blood and nothing graphic of any kind anywhere in the frame; no grief, no dread, no tears and no anguish; no night, no lamp, no overcast, no midday glare; no tree, no canopy, no dappled light, no building and no roof; no market, no stall, no sea, no road, no camel, no courtyard and no pearl; " + _NO_CREAM + "his pupils never centred on the lens.",
        "scene": (
            "One photograph, 105mm portrait lens, very shallow depth of field, warm "
            "low late-afternoon sun coming in level from the left across his face "
            "with soft bounce off the pale rock filling under his jaw so nothing is "
            "lost, fine film grain. THE CAMERA IS SET ON THE ROCK CLOSE IN AND WELL "
            "TO HIS LEFT AND SLIGHTLY BELOW HIM, AND HIS HEAD IS TURNED WELL OFF THE "
            "CAMERA AXIS INTO THREE-QUARTER VIEW WITH HIS NOSE POINTING AT THE RIGHT "
            "EDGE OF THE FRAME. HIS GAZE HAS A NAMED TARGET INSIDE THE PICTURE: the "
            "face of the seated disciple out at the right of the frame, whose dark "
            "out-of-focus shoulder and head cloth are visible there, so his eyeline "
            "runs level and rightward and leaves the picture through the RIGHT EDGE, "
            "well clear of the lens. Sharp and filling the frame from the shoulders "
            "up is Jesus, seated, quite still. HIS FACE IS THE WHOLE PICTURE AND IT "
            "IS GLAD, NOT GRIEVING: his eyes are steady, warm and completely "
            "untroubled, the skin at their outer corners softly creased, his mouth "
            "closed and settled with the faintest warmth in it — the face of a man "
            "who decided long ago and has never once been sorry. The near foreground "
            "at the bottom left corner is ONE out-of-focus DEEP INDIGO shouldered "
            "back, a solid dark saturated mass edge to edge, with nothing else "
            "between the camera and him. Behind him the bare pale grey rock, the dry "
            "wadi and the tawny hills fall completely out of focus under warm open "
            "sky."
        ),
    },
    {
        "id": "v2-r029-b36", "out": "s36-you-were-worth-all-of-it.jpeg",
        "seg": "n10", "window": "104.660-109.270", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SHELF", "DISCIPLES"],
        "narration": "That is how good he is. You were worth all of it to him.",
        "must_show": "the wide closing photograph — Jesus and his circle small together on the bare limestone shelf with the dry wadi and the whole country of folded tawny hills opening away beyond them in deep warm late-afternoon light.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no overcast, no midday glare; no tree, no canopy, no dappled light, no building and no roof; no market, no stall, no sea, no road, no camel, no courtyard and no pearl; " + _NO_CREAM + "not one face turned toward the lens.",
        "scene": (
            "One photograph, 24mm lens, deep depth of field, DEEP WARM LATE-AFTERNOON "
            "SUN coming in almost level from the left, the whole open rock and the "
            "country beyond gone rich and gold, long soft-edged shadows reaching right "
            "across the shelf, fine film grain. THE CAMERA STANDS FAR BACK ON THE "
            "SHELF AND WELL TO ONE SIDE OF THE WHOLE GROUP AND SHOOTS ACROSS THEM AT "
            "RIGHT ANGLES TO EVERY EYELINE, so the near men are seen from behind and "
            "in profile and NOT ONE FACE IS TURNED TOWARD THE LENS. THIS IS A WIDE "
            "LANDSCAPE SCENE AND NOT A PORTRAIT: the camera is far enough back that "
            "the whole seated circle is small in the lower third of the frame, "
            "everyone visible head to sandals, and the dry wadi and the folded hills "
            "fill the rest of the picture. The near foreground across the bottom is "
            "the bare cracked pale grey limestone of the shelf with loose flat slabs "
            "and dry grey scrub in the seams, sharp and close, with nobody between "
            "the camera and the group. Seated together on and around the low slab in "
            "the middle distance are Jesus and eight or nine of his disciples, the "
            "men low on the bare rock in DEEP INDIGO, DARK UMBER, DARK OLIVE-DRAB and "
            "RUSSET-RED wool with dark head cloths and no pale scarf, stole or shawl "
            "anywhere among them, all of them turned in toward Jesus in profile or "
            "three-quarter from behind. Jesus sits among them on the slab in his one "
            "plain undyed off-white cream wool robe, seen from the side, leaning "
            "slightly forward with one hand open — the ONLY pale thing in the whole "
            "picture. Beyond and below the shelf the dry stony wadi winds away and low "
            "tawny hills fold one behind another to a clean far horizon under a wide "
            "warm evening sky."
        ),
    },
]
