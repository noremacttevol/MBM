#!/usr/bin/env python3
"""V2 beat map — row 178, build-178-in-our-image (Genesis 1:26-27, 2:7 — "Let us
make man in our image, after our likeness").

COVERAGE: 21 pictures over 106.33 s (card_start) = ~5.0 s/picture (lesson 12
movie-coverage). g26 (the LORD's own words) is 20.8 s and legitimately needs 4
beats to cover the whole created order it names (sea, air, land, creeping
things). ONE establishing wide per place (b01 the formless deep, b10 the living
garden). FIRST-MAN and FIRST-WOMAN are the human spine.

NO OPEN CAMERON COMPLAINT — `v2_outline.py 178` shows none. Fresh V2 picture map
on the SPEAKER-LAW narration (all 13 segments ElevenLabs new-voice 44100/128k in
the v1 dir; V1 mp4 current 2026-07-29 → default AUDIO LOCK stream-copy, no flag).

SPEAKER LAW (see make_narration.py):
  s1  "And God said,"                          SCRIPTURE  → LIGHT-BLUE
  g26 Genesis 1:26  "Let us make man..."       GOD        → GREEN
  s2  Genesis 1:27  "So God created man..."     SCRIPTURE  → LIGHT-BLUE
  s3  Genesis 2:7   "formed man of the dust..." SCRIPTURE  → LIGHT-BLUE
Everything else is the NARRATOR (white). NO Jesus red-letter and NO Jesus anywhere
(this is the creation; no cream on anyone).

**HARD GATE — GOD / THE GODHEAD IS NEVER EMBODIED.** On the GOD-voice beats
(b04-b07) and the "counsel in the Godhead" beats (b02, b08), God creates and
speaks but is NEVER shown: no figure, face, hand, body, throne or
beam-shaped-being, and no halo/ring of light around anything. The plurality — the
"us," the counsel, "talking with someone" — is carried by the NARRATION ONLY and
is NEVER pictured: **do not depict two or three divine figures in council.** The
creative presence is light over the deep and the created world appearing by the
word; the source stays unseen. The image of God is shown through the CREATED
HUMANS, never by showing God.

**MODESTY GATE — the first man and woman.** FIRST-MAN and FIRST-WOMAN are shown
with full dignity but ALWAYS modestly: framed above the chest, from behind, in
soft shadow, or with natural light, earth, water or foliage covering — NEVER nude,
never explicit, no exposed genitals, breasts or buttocks. The dignity reads in
their faces and bearing, not their bodies. They are EQUAL image-bearers (Gen
1:27, "male and female"; the narration: "not one closer to God than the other").

CONTENT-CARE: the created world is a peaceable primordial Eden at first light —
no violence, no predation, harmony among the creatures ("stewards, not owners").
First-created natural world only; no modern object; no rendered writing (captions
live in the bottom band only). n4 speaks of "every person since" — keep it the
first couple in the garden; do NOT introduce modern people or dress.

PLACES:
  COSMOS-DEEP (NEW)   the formless deep and the creative light before the world
                      (b01-b04, b08)
  EDEN-GARDEN (NEW)   the finished living garden where the humans are made and
                      dwell (b09-b21)
  (b05 sea / b06 air / b07 land are distinct created-domain nature shots and carry
   no place lock — nothing recurring to plate.)
NEW places (runner promotes each from its first good frame, lesson 11):
  COSMOS-DEEP  promote b01 (establishing wide)
  EDEN-GARDEN  promote b10 (establishing wide)
Steps in QC.md.
"""

# LOCKS: all build-local. No cream on anyone (Jesus not in this row).
LOCKS = {
    "COSMOS-DEEP": (
        "COSMOS-DEEP LOCK: the same place in every frame — the formless deep "
        "before the world was finished: a vast dark expanse of primordial water "
        "under a heavy unlit sky, mist and cloud over the face of the waters, a "
        "soft diffuse creative light beginning to break far off across the deep. "
        "No land, building, object, figure or writing of any kind; only water, "
        "cloud, dark and the first light. The same deep and quality of light "
        "throughout."
    ),
    "EDEN-GARDEN": (
        "EDEN-GARDEN LOCK: the same place in every frame — a lush primordial "
        "garden of the new-made earth at first light: deep green foliage, "
        "fruit-bearing trees, soft grass, still pools and a quiet stream, low "
        "morning mist, gentle warm dawn light through the leaves, distant hills "
        "beyond. A pristine untouched natural world — NO building, wall, tool, "
        "path, fence, modern object, sign or writing of any kind. The same garden, "
        "trees, water and dawn light throughout."
    ),
    "FIRST-MAN": (
        "FIRST-MAN LOCK (Adam): the first man is the same man in every shot — a "
        "healthy young adult Hebrew-featured man of warm tan-brown skin, with "
        "short dark hair and a light dark beard, calm noble features, newly made. "
        "ALWAYS SHOWN MODESTLY: framed above the chest, from behind, in soft "
        "shadow, or with earth, grass, water, leaf or dawn light softly covering "
        "the body — NEVER nude, never explicit, no exposed genitals, buttocks or "
        "full torso. His dignity reads in his face and bearing. The SAME man "
        "throughout, never twinned, never a cloned face; ordinary-sized, with two "
        "hands and one head. Never in cream or any robe (he is newly made)."
    ),
    "FIRST-WOMAN": (
        "FIRST-WOMAN LOCK (Eve): the first woman is the same woman in every shot — "
        "a healthy young adult Hebrew-featured woman of warm tan-brown skin, with "
        "long dark hair, calm noble features, newly made. ALWAYS SHOWN MODESTLY: "
        "framed above the shoulders or upper chest, from behind, in soft shadow, "
        "or with her long hair, grass, foliage, water or dawn light softly "
        "covering the body — NEVER nude, never explicit, no exposed breasts, "
        "genitals or buttocks. Her dignity reads in her face and bearing. The "
        "SAME woman throughout, never twinned, never a cloned face; "
        "ordinary-sized, with two hands and one head. Never in cream."
    ),
    "CREATION-CREATURES": (
        "CREATION-CREATURES LOCK: the animals of the new-made world are ordinary, "
        "natural, peaceable creatures — fish in clear water, birds of the air, "
        "gentle grazing beasts and small creeping things — all calm and unharmed, "
        "no predation, blood, kill or fear among them, none monstrous, giant or "
        "invented. Natural anatomy and scale; no modern breed marks, tags or "
        "objects."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r178-b01", "out": "s01-the-formless-deep.jpeg", "seg": "n0",
        "window": "0.400-5.100", "wide": True, "jesus": False, "ref": False,
        "locks": ["COSMOS-DEEP"],
        "narration": "At the start of all things, before any person drew breath, a counsel happened in the Godhead — let us make man in our image.",
        "must_show": "the ONE establishing wide of the formless deep — the camera looks out low across a vast dark primordial ocean under a heavy unlit sky, mist over the waters and the first soft creative light breaking far off; before all things.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam-being; no two or three divine figures; no land, building or object; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "The camera looks out low across a vast dark expanse of primordial "
            "water in a wide, level three-quarter view over the surface, under a "
            "heavy, unlit sky, cloud and mist lying over "
            "the face of the deep, and far off across the water a soft diffuse "
            "light beginning to break — the world not yet made, before anything "
            "drew breath. Only water, cloud, dark and the first light; no shape "
            "or figure anywhere in the light, nothing is written and no ring of "
            "light rings anything."
        ),
    },
    {
        "id": "v2-r178-b02", "out": "s02-a-counsel-in-the-godhead.jpeg", "seg": "n0",
        "window": "5.100-9.826", "wide": False, "jesus": False, "ref": False,
        "locks": ["COSMOS-DEEP"],
        "narration": "a counsel happened in the Godhead — let us make man in our image.",
        "must_show": "the purposeful creative moment — the soft creative light over the deep gathering and strengthening, deliberate and about to act; a counsel in the Godhead, its members UNSEEN, carried only by the light and the narration.",
        "must_not_show": "GOD IS NEVER SHOWN and the Godhead is NEVER pictured — no God figure, no two or three divine persons in council, no faces, hands, thrones or beam-beings in the light; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "Over the dark deep the soft creative light gathers and strengthens "
            "across the mist, steady and purposeful, as if a decision is being "
            "made — but the light holds no shape, face or figure of any kind, and "
            "no persons appear in it. Only water, cloud and the deepening light. "
            "Nothing is written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r178-b03", "out": "s03-and-god-said.jpeg", "seg": "s1",
        "window": "9.826-12.816", "wide": False, "jesus": False, "ref": False,
        "locks": ["COSMOS-DEEP"],
        "narration": "And God said,",
        "must_show": "SCRIPTURE-EXACT (light-blue) — the word about to go out: the creative light moving over the face of the waters, poised on the edge of speech; And God said — the speaker unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam-being; no divine mouth; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "The creative light moves low over the face of the primordial waters, "
            "mist stirring beneath it, the whole deep hushed and poised on the "
            "edge of the first word — the moment just before God speaks, the "
            "speaker Himself unseen. Only water, cloud and moving light; nothing "
            "is written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r178-b04", "out": "s04-make-man-in-our-image.jpeg", "seg": "g26",
        "window": "12.816-18.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["COSMOS-DEEP"],
        "narration": "Let us make man in our image, after our likeness:",
        "must_show": "GOD-VOICE, GREEN caption — the world beginning to form at the word: across the deep, land and light taking shape, the earth being readied for the man who will bear the likeness; the Maker unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam-being; NO divine person and NO human figure yet; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "At the word the deep answers: light spreads across the waters and the "
            "first land and green begin to take shape out of the mist, the raw "
            "earth being made ready — the place prepared for the creature who will "
            "bear the likeness. No figure, divine or human, appears; only the "
            "world coming into being under the creative light. Nothing is written "
            "anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r178-b05", "out": "s05-the-fish-of-the-sea.jpeg", "seg": "g26",
        "window": "18.000-23.200", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREATION-CREATURES"],
        "narration": "and let them have dominion over the fish of the sea,",
        "must_show": "GOD-VOICE, GREEN caption — the sea filled with life: clear new waters teeming with ordinary peaceable fish; the domain of the sea readied for man's care.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no monstrous, giant or invented sea creature; no predation or blood; no modern object or vessel; no Jesus and no cream; no halo; no scroll, writing or panel.",
        "scene": (
            "Bright new sea water in the first light, alive with shoals of "
            "ordinary peaceable fish moving through it, weed and stone below, the "
            "sunlit surface above — the living fullness of the sea, calm and "
            "unharmed. Natural creatures at natural scale; nothing is written "
            "anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r178-b06", "out": "s06-the-fowl-of-the-air.jpeg", "seg": "g26",
        "window": "23.200-28.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREATION-CREATURES"],
        "narration": "and over the fowl of the air, and over the cattle,",
        "must_show": "GOD-VOICE, GREEN caption — the sky filled with birds: ordinary birds of many kinds crossing the bright dawn sky over the new land; the domain of the air readied.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no monstrous or invented bird; no modern aircraft or object; no Jesus and no cream; no halo; no scroll, writing or panel.",
        "scene": (
            "A wide bright dawn sky over the new-made hills, crossed by ordinary "
            "birds of many kinds on the wing — a flight of small birds, a few "
            "larger fowl gliding — the living fullness of the air in the morning "
            "light. Natural birds at natural scale; nothing is written anywhere "
            "and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r178-b07", "out": "s07-cattle-and-creeping-things.jpeg", "seg": "g26",
        "window": "28.000-33.626", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREATION-CREATURES"],
        "narration": "and over all the earth, and over every creeping thing that creepeth upon the earth.",
        "must_show": "GOD-VOICE, GREEN caption — the land filled with life: gentle grazing beasts on the green earth and small creeping creatures near the ground; the whole earth readied for man's dominion.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no predation, kill or blood; no monstrous or invented beast; no modern object; no Jesus and no cream; no halo; no scroll, writing or panel.",
        "scene": (
            "Across the green new-made land, gentle grazing beasts stand and feed "
            "in the morning light while small creeping creatures — a lizard, "
            "beetles, an ant-line — move over the earth and stones near the "
            "ground, all calm and unharmed together. The living fullness of the "
            "land; natural creatures at natural scale, no hunting or fear. Nothing "
            "is written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r178-b08", "out": "s08-hear-the-word-us.jpeg", "seg": "n0b",
        "window": "33.626-38.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["COSMOS-DEEP"],
        "narration": "Hear the word us. God is not talking to himself there — he is talking with someone,",
        "must_show": "the shared counsel, unseen — the strong creative light over the readied world, plainly purposeful and shared, yet EMPTY of any figure; the 'us' is heard, never pictured.",
        "must_not_show": "GOD IS NEVER SHOWN and the Godhead is NEVER pictured — no God figure, no two or three divine persons, no faces, hands or beam-beings in the light; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "The strong creative light lies over the newly formed world and its "
            "waters, steady and deliberate — the sense of a shared purpose at work "
            "— but the light holds no shape, face or figure, and no persons appear "
            "in it. The 'us' is carried by the words, not by the picture. Nothing "
            "is written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r178-b09", "out": "s09-a-creature-that-looks-like-them.jpeg", "seg": "n0b",
        "window": "38.500-43.270", "wide": False, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "FIRST-MAN"],
        "narration": "and what they decide together is to make a creature that looks like them.",
        "must_show": "the human form appearing — the first man's form emerging, still and new, of the earth of the garden, framed modestly; a creature made to bear the likeness (the Maker unseen).",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam-being; NUDITY GATE — no exposed genitals, buttocks or full nude torso; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "In the new garden the first man lies newly formed of the warm earth, "
            "still and unwaking, seen from above the chest with soft grass, dawn "
            "mist and the shadow of a low branch modestly across the body — a "
            "creature just shaped to bear the likeness, the Maker who shaped him "
            "unseen. His face is calm and noble. Framed modestly, ordinary-sized, "
            "one head; nothing is written anywhere and no ring of light rings his "
            "head."
        ),
    },
    {
        "id": "v2-r178-b10", "out": "s10-the-whole-living-world.jpeg", "seg": "n0b",
        "window": "43.270-48.113", "wide": True, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "CREATION-CREATURES"],
        "narration": "Then he hands that creature the whole living world to take care of.",
        "must_show": "the establishing wide of the garden — the camera looks across the whole lush living garden at first light, trees, water and gentle animals spread through it; the whole living world given into the creature's care.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no building, wall, tool or modern object; no predation among the animals; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no posed line facing the lens.",
        "scene": (
            "The camera looks across the whole lush primordial garden at first "
            "light in a high three-quarter view: fruit-bearing trees, soft grass, "
            "a still pool and a quiet stream, low morning mist, gentle grazing "
            "beasts and birds spread peacefully through it, distant hills beyond — "
            "a whole living world made ready and given into the man's care. No "
            "building or object; natural creatures at natural scale, seen at ease "
            "and not posed to the camera; nothing is written anywhere and no ring "
            "of light rings anything."
        ),
    },
    {
        "id": "v2-r178-b11", "out": "s11-in-his-own-image.jpeg", "seg": "s2",
        "window": "48.113-52.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "FIRST-MAN"],
        "narration": "So God created man in his own image, in the image of God created he him;",
        "must_show": "SCRIPTURE-EXACT (light-blue) — the first man, dignified: a close on the first man newly alive in the garden, noble and calm, bearing the likeness; created in the image of God (God unseen).",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being; NUDITY GATE — no exposed genitals, buttocks or nude torso; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no face posed to the lens.",
        "scene": (
            "A close on the first man newly alive in the garden, seen from the "
            "shoulders up in the soft dawn light among the green leaves, his face "
            "calm, noble and awake — a man made to bear the image of God. Framed "
            "modestly above the chest with foliage soft behind him, ordinary-sized, "
            "one head, not in cream, his gaze quietly outward and not to the "
            "camera; nothing is written anywhere and no ring of light rings his "
            "head."
        ),
    },
    {
        "id": "v2-r178-b12", "out": "s12-male-and-female.jpeg", "seg": "s2",
        "window": "52.800-57.133", "wide": False, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "FIRST-MAN", "FIRST-WOMAN"],
        "narration": "male and female created he them.",
        "must_show": "SCRIPTURE-EXACT — the man AND the woman together, both dignified and equal, standing side by side in the garden; male and female, both bearing the image.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; NUDITY GATE — no exposed genitals, breasts or buttocks on either; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no posed line facing the lens.",
        "scene": (
            "The first man and the first woman stand together side by side in the "
            "garden at dawn, seen from behind and the side from the shoulders up, "
            "her long hair and the surrounding foliage and soft light keeping both "
            "framed modestly — two equal image-bearers, neither above the other, "
            "looking out together over the new world. Ordinary-sized, distinct, "
            "one head each, not in cream; nothing is written anywhere and no ring "
            "of light rings either head."
        ),
    },
    {
        "id": "v2-r178-b13", "out": "s13-both-bearing-the-likeness.jpeg", "seg": "n0c",
        "window": "57.133-65.097", "wide": False, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "FIRST-MAN", "FIRST-WOMAN"],
        "narration": "And then he did it. Not one of them closer to God than the other. Both of them bearing the likeness.",
        "must_show": "the two as equals — a warm two-shot of the man and woman turned a little toward each other in the garden, equal in dignity, both bearing the likeness; neither closer to God than the other.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; NUDITY GATE — no exposed genitals, breasts or buttocks; no one figure raised, larger or favoured over the other; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "A warm two-shot of the first man and first woman in the garden, "
            "turned a little toward each other from the shoulders up, level with "
            "one another on the same ground in the same dawn light — plainly equal "
            "in dignity, both bearing the same likeness, neither set above or "
            "nearer than the other. Modestly framed with hair and foliage, "
            "ordinary-sized, one head each, not in cream, their eyes on each other "
            "and the garden and not the camera; nothing is written anywhere and no "
            "ring of light rings either head."
        ),
    },
    {
        "id": "v2-r178-b14", "out": "s14-formed-of-the-dust.jpeg", "seg": "s3",
        "window": "65.097-68.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "FIRST-MAN"],
        "narration": "And the LORD God formed man of the dust of the ground,",
        "must_show": "SCRIPTURE-EXACT (light-blue) — the forming from earth: a close on the first man's form of the warm dust and clay of the ground, being shaped, still lifeless (framed modestly); formed of the dust of the ground.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, sculpting hands of God or beam-being; NUDITY GATE — no exposed genitals, buttocks or nude torso; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "A close on the first man taking form of the warm earth of the "
            "garden — shoulder, jaw and brow of dust-toned clay just resolving "
            "into a human shape on the ground, still lifeless, grass and soil "
            "around and a fall of shadow keeping the body modestly framed. The "
            "hands that shape him are not shown. Ordinary-sized, one head; nothing "
            "is written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r178-b15", "out": "s15-the-breath-of-life.jpeg", "seg": "s3",
        "window": "68.800-72.400", "wide": False, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "FIRST-MAN"],
        "narration": "and breathed into his nostrils the breath of life;",
        "must_show": "SCRIPTURE-EXACT — the first breath: a close on the first man's face at the instant of coming alive, a first breath drawn, the air and light around him — the breath given by God UNSEEN, no divine mouth or hand.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, no divine face, mouth or hand near him, no beam-being; NUDITY GATE — no exposed torso; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "A close on the first man's face at the very instant life enters him — "
            "lips just parting on a first indrawn breath, the muscles of the face "
            "quickening, soft moving air and dawn light around his head among the "
            "leaves. The breath is given by a presence that is not shown: no face, "
            "mouth or hand appears near him. Framed at the head and shoulders, "
            "modestly, one head; nothing is written anywhere and no ring of light "
            "rings his head."
        ),
    },
    {
        "id": "v2-r178-b16", "out": "s16-a-living-soul.jpeg", "seg": "s3",
        "window": "72.400-75.196", "wide": False, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "FIRST-MAN"],
        "narration": "and man became a living soul.",
        "must_show": "SCRIPTURE-EXACT — alive: a close on the first man's eyes opening for the first time, awake and aware in the garden; man became a living soul.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; NUDITY GATE — no exposed torso; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no face posed to the lens.",
        "scene": (
            "A close on the first man's face as his eyes open for the first time, "
            "clear and aware, the first light of the garden reflected in them, "
            "wonder and calm waking together — a living soul. Framed at the head "
            "and shoulders, modestly, one head, not in cream, his gaze finding the "
            "world and not the camera; nothing is written anywhere and no ring of "
            "light rings his head."
        ),
    },
    {
        "id": "v2-r178-b17", "out": "s17-then-the-act.jpeg", "seg": "n3",
        "window": "75.196-77.858", "wide": False, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "FIRST-MAN"],
        "narration": "Then the act:",
        "must_show": "the living man taking his place — the first man rising to sit or stand in the garden, upright and alive, taking his place in the world (framed modestly).",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; NUDITY GATE — no exposed genitals, buttocks or full nude torso; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "The first man rises, coming up onto one arm to sit upright in the "
            "garden grass, alive and steady, taking his place in the new world — "
            "seen from behind and the side with grass, foliage and morning light "
            "keeping the body modestly framed. Ordinary-sized, one head, not in "
            "cream, his face toward the garden and not the camera; nothing is "
            "written anywhere and no ring of light rings his head."
        ),
    },
    {
        "id": "v2-r178-b18", "out": "s18-stewards-not-owners.jpeg", "seg": "n2",
        "window": "77.858-86.205", "wide": False, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "FIRST-MAN", "CREATION-CREATURES"],
        "narration": "The plan included dominion — over fish, birds, cattle, and all the earth. Stewards, not owners.",
        "must_show": "dominion as stewardship — the first man among the peaceable animals of the garden, a gentle hand resting on or tending a calm beast; caring for the living world, a steward and not an owner (framed modestly).",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no whip, yoke, cage, weapon or mastery by force; no predation or fear among the animals; NUDITY GATE — no exposed genitals, buttocks or nude torso; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "The first man stands among the gentle animals of the garden in the "
            "morning light, a calm grazing beast beside him and birds nearby, one "
            "hand resting softly on the animal's neck as he looks over the living "
            "world in his care — tending it, a steward and not an owner, nothing "
            "held over the creatures by force. Seen from behind and the side with "
            "foliage and light keeping the body modestly framed. Ordinary-sized, "
            "one head, not in cream; natural animals at ease; nothing is written "
            "anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r178-b19", "out": "s19-bearing-something-of-god.jpeg", "seg": "n1a",
        "window": "86.205-92.875", "wide": False, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "FIRST-MAN"],
        "narration": "Not in the shape of any creature, but bearing something of God himself:",
        "must_show": "the difference in him — a close on the first man's thoughtful, self-aware face, an inward depth beyond any animal; bearing something of God himself.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; NUDITY GATE — no exposed torso; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no face posed to the lens.",
        "scene": (
            "A close on the first man's face in the soft garden light, quiet and "
            "thoughtful, an inward awareness and depth in his eyes that no animal "
            "has — the mark of one who bears something of God himself. Framed at "
            "the head and shoulders, modestly, one head, not in cream, his gaze "
            "inward and not to the camera; nothing is written anywhere and no ring "
            "of light rings his head."
        ),
    },
    {
        "id": "v2-r178-b20", "out": "s20-to-know-to-choose-to-reflect.jpeg", "seg": "n1b",
        "window": "92.875-98.741", "wide": False, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "FIRST-MAN"],
        "narration": "the capacity to know him, to choose him, to reflect him.",
        "must_show": "the reach toward God — the first man's face lifted, eyes turned up toward the bright open dawn sky, open and reaching in relationship; the capacity to know, choose and reflect God (God unseen).",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being in the sky; NUDITY GATE — no exposed torso; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "The first man lifts his face toward the bright open dawn sky above the "
            "garden, eyes turned up, his look open and reaching — a creature able "
            "to know, to choose and to reflect the God who made him, that God "
            "Himself unseen above. Framed at the head and shoulders, modestly, one "
            "head, not in cream, seen from behind and the side; nothing is written "
            "anywhere and no ring of light rings his head or fills the sky."
        ),
    },
    {
        "id": "v2-r178-b21", "out": "s21-loved-into-being.jpeg", "seg": "n4",
        "window": "98.741-106.330", "wide": True, "jesus": False, "ref": False,
        "locks": ["EDEN-GARDEN", "FIRST-MAN", "FIRST-WOMAN"],
        "narration": "Every person since carries that original dignity — made in the image, loved into being.",
        "must_show": "the closing — the first man and woman together in the garden at full first light, dignified and at peace, the source of every person since; made in the image, loved into being.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; NUDITY GATE — no exposed genitals, breasts or buttocks; no modern people or dress; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no posed line facing the lens.",
        "scene": (
            "A closing wide of the first man and first woman standing together in "
            "the lush garden at full first light, seen from behind and the side "
            "from the shoulders up with hair, foliage and light keeping both "
            "framed modestly, the living world opening bright beyond them — the "
            "two from whom every person since would come, made in the image and "
            "loved into being. Ordinary-sized, distinct, one head each, not in "
            "cream, gazing out over the garden and not the camera; nothing is "
            "written anywhere and no ring of light rings either head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Both places are NEW (no stash plate yet); the runner promotes each from its own
# first good frame (b01 COSMOS-DEEP / b10 EDEN-GARDEN), so PLACE_REFS stays empty.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: every person is carried by a byte-identical text lock (no face
# sheets exist for these figures). NO Jesus in this row.
REFS = {
}
