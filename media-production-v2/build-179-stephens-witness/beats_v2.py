#!/usr/bin/env python3
"""V2 beat map — row 179, build-179-stephens-witness (Acts 7 — Stephen full of the
Holy Ghost, his testimony, the vision of the Father and the Son, his stoning, and
his forgiving prayers).

COVERAGE: 14 pictures over 56.83 s (card_start) = ~4.0 s/picture (lesson 12
movie-coverage). ONE establishing wide per place (b01 the council chamber, b09 the
gate/ground outside the walls); everything else is singles, the vision, and inserts
that follow STEPHEN as the human spine.

=====================================================================
OPEN CAMERON COMPLAINT — THIS IS THE WHOLE SPEC (v2_outline.py 179):
  "Regenerate this video about Stephen in Acts 7 from a Latter-day Saint
   perspective. The vision scene (Acts 7:55-56) must clearly show two distinct
   glorified personages in radiant heavenly light: God the Father and His Son
   Jesus Christ standing at the Father's right hand. Portray them as separate
   embodied beings, just as Stephen saw them — not as one figure, not as Jesus
   only, and do not add a dove or Trinitarian symbol. Use a reverent, luminous
   style like official Latter-day Saint gospel art... Keep the story simple,
   scripturally accurate, and 'milk' level — Christ-centered and uplifting for
   everyone. Focus on Stephen being full of the Holy Ghost, his bold testimony of
   Jesus, the vision of the Father and Son, his martyrdom, and his forgiving
   prayers to the Lord Jesus."

**DELIBERATE EMBODIMENT — READ BEFORE ANY QC.** For THIS row ONLY, and by
Cameron's explicit filed instruction, the general "GOD / the Father is never
embodied" hard gate is OVERRIDDEN in the vision beats (b05, b07). The Father and
the Son are shown as TWO distinct, separate, embodied, glorified personages in
radiant heavenly light — the Son standing at the Father's right hand — in the
reverent luminous manner of the Latter-day Saint Gospel Art Book depiction of
Stephen's vision. This is scripturally what Stephen saw (Acts 7:55-56) and is the
exact fix Cameron asked for. Do NOT "correct" this back to an unseen presence, a
single figure, or a Jesus-only frame; and NEVER add a dove or any Trinitarian
symbol. Everywhere ELSE in this row (council, mob, martyrdom) there is no divine
figure at all. A future author/runner who un-embodies this vision RE-OPENS the
complaint — the worst failure. (Logged as V2-REBUILD-RUBRIC.md lesson 15 this
session. NOTE: CONTENT-CARE.md's numeric table is keyed to the THE-200 catalog,
where #179 is the fiery furnace — a DIFFERENT story — so it is intentionally left
untouched; the durable record is rubric lesson 15, which every session must read.)
=====================================================================

AUDIO: default AUDIO LOCK stream-copy (no flag). All 9 segments + card are
ElevenLabs new-voice 44100/128k in the v1 dir; V1 mp4 current 2026-07-29, built
from the SPEAKER-LAW segments below → the shipped track already carries the
speaker-law voices. Board Audio = OK. Do NOT re-voice (picture-only rebuild).

SPEAKER LAW (see make_narration.py — Acts 7 has NO red-letter and NO God-voice):
  s1   Acts 7:56  "Behold, I see the heavens opened, and the Son of man standing
       on the right hand of God."       SCRIPTURE (Stephen speaking) → LIGHT-BLUE
  s60  Acts 7:60  "Lord, lay not this sin to their charge."
       SCRIPTURE (Stephen's dying prayer) → LIGHT-BLUE
Jesus STANDS in the vision but never SPEAKS a word in this story — every quoted
line is Stephen's. So there is NO Jesus red-letter caption anywhere, and the two
scripture segments are Stephen's, light-blue (the row-39 lesson: a quoted line
sits on the man who says it). Everything else is the NARRATOR (white).

INHERITED CAPTION/AUDIO DESYNCS (from the locked V1 render — do NOT try to fix;
audio is immutable and Cameron did not complain about them; noted so a runner is
not surprised at QC):
  · n3a: the delivered audio OPENS with an extra recap line ("Look, he told them —
    heaven is open, and the Son of man is standing at God's right hand.") that is
    not in the v2 caption text; b08 pictures the council refusing that testimony,
    which reads true against both the audio and the caption.
  · n3b: the delivered audio speaks ONLY the first sentence ("...the face of an
    angel — at peace, not afraid."); the caption's second sentence has no audio.
    b10 pictures the first sentence, which is what is heard.

CONTENT-CARE — R (RESTRAINT, martyrdom/violence): the stoning is NEVER the
picture. No stone shown striking Stephen, no wound, no blood, no gore, no stone in
close flight at his body. The weight lands on Stephen's peaceful, forgiving face
and on the witnesses. Parent test on every martyrdom frame (b09-b14): "would a
parent let a 10-year-old see this?" The mob is at a distance; hands may hold or
lower stones but no blow lands on camera.

PLACES:
  COUNCIL-CHAMBER (NEW)  the Sanhedrin council hall where Stephen is tried
                         (b01-b04, b06, b08). The vision (b05, b07) happens here
                         too but the frame is the opened heaven, not the room.
  OUTSIDE-WALLS   (NEW)  the ground just outside the city gate where he is taken
                         and stoned (b09-b14).
NEW places (runner promotes each from its first good frame, lesson 11):
  COUNCIL-CHAMBER  promote b01 (establishing wide)
  OUTSIDE-WALLS    promote b09 (establishing wide of the gate/ground)
Steps in QC.md. No stash plate exists for either yet.
"""

# LOCKS: all build-local. No Jesus flag / no cream anywhere in this row — the only
# depiction of the Son is the GLORIFIED vision figure (b05/b07), locked below with
# his canonical features for face-continuity but in radiant glory, NOT the mortal
# cream robe. State clothing colours POSITIVELY.
LOCKS = {
    "COUNCIL-CHAMBER": (
        "COUNCIL-CHAMBER LOCK: the same place in every frame — the hall of the "
        "Sanhedrin council in first-century Jerusalem: a large stone chamber with "
        "dressed ashlar walls, a semicircle of tiered stone benches where robed "
        "elders and scribes sit, plain oil lamps in iron stands, a worn stone "
        "floor, daylight falling from high clerestory openings. Ancient, austere, "
        "no ornament of any later century; no glass, no modern object, no writing "
        "rendered as art anywhere. The same chamber, benches and light throughout."
    ),
    "OUTSIDE-WALLS": (
        "OUTSIDE-WALLS LOCK: the same place in every frame — bare open ground just "
        "outside the great stone gate and wall of first-century Jerusalem: dusty "
        "trodden earth, scattered rocks and low scrub, the tan city wall and gateway "
        "rising behind, dry hills beyond under an open sky. Ancient and plain; no "
        "modern object, no writing. The same gate, wall, ground and daylight "
        "throughout."
    ),
    "STEPHEN": (
        "STEPHEN LOCK: the same young man in every shot — a Hellenist Jewish "
        "believer of about thirty, warm olive-tan Middle-Eastern skin, short dark "
        "brown hair and a short dark beard, calm steady dark eyes, an open honest "
        "face full of peace. He wears a simple undyed oatmeal-and-brown rough wool "
        "tunic and mantle (NEVER cream, never white, never fine cloth). The SAME "
        "man throughout — never twinned, never a cloned face, ordinary-sized, two "
        "hands, one head. His mark is serenity: even accused and dying his face is "
        "unafraid, luminous with peace, 'the face of an angel.'"
    ),
    "SANHEDRIN": (
        "SANHEDRIN LOCK: the council are older Jewish men of the ruling court — "
        "grey-and-dark-bearded elders and scribes in layered robes and mantles of "
        "deep blue, brown, wine and grey, some in prayer shawls, a few in the taller "
        "headwear of the priesthood. They are DISTINCT individuals, not repeated "
        "faces or twins; a range of ages and builds. Across the row their mood "
        "hardens from listening, to rage, to stopping their ears — but they are the "
        "SAME men throughout. Ordinary-sized; period cloth only, no modern object."
    ),
    "THE-MOB": (
        "THE-MOB LOCK: the men who carry out the stoning are a handful of ordinary "
        "first-century Jerusalem men in rough working tunics and mantles of brown, "
        "grey and dull red, kept at a DISTANCE from the camera. Distinct faces, not "
        "twins. They may hold or set down stones and their outer coats, but NO blow "
        "is ever shown landing, no stone strikes flesh on camera, no blood or wound "
        "appears. Ordinary-sized; period cloth only, no modern object."
    ),
    "GLORIFIED-FATHER": (
        "GLORIFIED-FATHER LOCK (the vision only, b05/b07): God the Father shown as "
        "a majestic, benevolent, embodied glorified MAN standing within brilliant "
        "heavenly radiance — an older Middle-Eastern man of noble, kindly bearing, "
        "warm tan skin, long white hair and a full flowing white beard, clothed in "
        "a radiant pure-white robe of light. He is calm, fatherly and full of love, "
        "reverent and luminous in the manner of Latter-day Saint gospel art. He is "
        "a SEPARATE, distinct being from the Son beside him. Two arms, one head, "
        "human proportions. No dove, no triangle, no eye, no cross, no crown, no "
        "throne machinery — only the radiant Father and the light around him."
    ),
    "GLORIFIED-SON": (
        "GLORIFIED-SON LOCK (the vision only, b05/b07): Jesus Christ, the Son of "
        "man, shown as an embodied glorified MAN standing at the Father's right "
        "hand within the same brilliant heavenly radiance — the SAME canonical face "
        "as the Lord elsewhere: a Middle-Eastern man of about thirty-three, warm "
        "tan-olive skin (NEVER white, NEVER fair), shoulder-length dark brown wavy "
        "hair and a full dark beard, warm brown eyes, kind and strong. In the "
        "vision he is clothed in a radiant white robe of light (glorified, NOT the "
        "mortal earth-toned robe). He STANDS — upright, on his feet, at the "
        "Father's right side — distinct and separate from the Father, plainly a "
        "second person and not a merging of the two. Two arms, one head, human "
        "proportions, ordinary-sized beside the Father. No dove, no cross, no "
        "Trinitarian symbol."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r179-b01", "out": "s01-before-the-council.jpeg", "seg": "n0",
        "window": "0.400-5.261", "wide": True, "jesus": False, "ref": False,
        "locks": ["COUNCIL-CHAMBER", "STEPHEN", "SANHEDRIN"],
        "narration": "Stephen, full of the Holy Spirit, was dragged before the council for speaking the truth.",
        "must_show": "the ONE establishing wide of the council hall — Stephen stands alone at the centre of the semicircle of seated elders, brought before the Sanhedrin to answer for the truth he preached; he is calm, they are stern.",
        "must_not_show": "no divine figure of any kind here (the vision comes later); no violence, no blood; no cream robe on anyone; no modern object; no halo or ring of light; no scroll, writing or panel rendered as art.",
        "scene": (
            "The camera looks across the austere stone council chamber from the "
            "back of the floor, past the shoulders and backs of the nearest seated "
            "elders, toward Stephen standing alone at the centre of the semicircle "
            "of tiered benches. The robed elders and scribes are turned in on him "
            "from every side, stern and watchful; Stephen stands steady and calm, "
            "hands at his sides, plainly the accused. High daylight falls from the "
            "clerestory across the worn floor. Ordinary-sized figures on one ground "
            "plane; nothing is written anywhere as art."
        ),
    },
    {
        "id": "v2-r179-b02", "out": "s02-they-boiled-with-rage.jpeg", "seg": "n0",
        "window": "5.261-10.304", "wide": False, "jesus": False, "ref": False,
        "locks": ["COUNCIL-CHAMBER", "STEPHEN", "SANHEDRIN"],
        "narration": "He told them the whole story of Israel — and they boiled with rage.",
        "must_show": "Stephen mid-testimony and the council's fury — a two-shot favouring Stephen speaking earnestly while the nearest elders' faces darken with rage at his words.",
        "must_not_show": "no divine figure; no violence yet; no cream robe; no modern object; no halo or ring of light; no scroll or writing rendered as art.",
        "scene": (
            "A tighter two-shot in the chamber: Stephen in the foreground turned "
            "three-quarter, mouth open in earnest testimony, one hand lifted a "
            "little as he speaks; just beyond him two or three of the seated elders "
            "lean forward, brows knotted, jaws set, faces hot with anger at what he "
            "is saying. Warm lamp and daylight on their faces. Distinct individual "
            "faces, ordinary-sized, one ground plane; nothing written as art."
        ),
    },
    {
        "id": "v2-r179-b03", "out": "s03-not-his-accusers.jpeg", "seg": "n1",
        "window": "10.304-12.266", "wide": False, "jesus": False, "ref": False,
        "locks": ["COUNCIL-CHAMBER", "STEPHEN"],
        "narration": "But Stephen didn't look at his accusers.",
        "must_show": "a close on Stephen's calm face — he does NOT meet the angry men around him; his eyes are already turning away from them, unshaken.",
        "must_not_show": "no divine figure; no cream robe; no modern object; no halo or ring of light; no scroll or writing rendered as art.",
        "scene": (
            "A close on Stephen's face and shoulders in the chamber, the blurred "
            "shapes of the angry elders soft around the edges of the frame. He does "
            "not look at them; his gaze is steady and unafraid, beginning to turn "
            "away and upward, wholly at peace amid their fury. Soft daylight on his "
            "features; ordinary-sized, one head, gaze not to the camera."
        ),
    },
    {
        "id": "v2-r179-b04", "out": "s04-he-looked-up.jpeg", "seg": "n1",
        "window": "12.266-15.734", "wide": False, "jesus": False, "ref": False,
        "locks": ["COUNCIL-CHAMBER", "STEPHEN"],
        "narration": "He looked up, and what he saw changed everything.",
        "must_show": "Stephen looking up — his face lifted toward heaven, the first brightening of a radiant light beginning to fall on his upturned face; the reveal is about to come.",
        "must_not_show": "the two personages are NOT yet resolved here (that is the next beat); no divine figure fully shown; no cream robe; no modern object; no halo ringing his head; no scroll or writing as art.",
        "scene": (
            "A low close on Stephen from below and the side, his face lifted toward "
            "heaven, eyes opening wide with wonder as a brilliant radiance begins "
            "to break across his upturned features and the stone above him. The "
            "council falls away into shadow beneath. The light comes from high and "
            "beyond the frame, not yet resolved into any shape. Ordinary-sized, one "
            "head; the brightness is in the scene, not ringing his head."
        ),
    },
    {
        "id": "v2-r179-b05", "out": "s05-the-glory-of-god.jpeg", "seg": "n2",
        "window": "15.734-20.262", "wide": False, "jesus": False, "ref": False,
        "locks": ["GLORIFIED-FATHER", "GLORIFIED-SON", "STEPHEN"],
        "narration": "He saw the glory of God — and Jesus, standing at the right hand of the Father.",
        "must_show": "THE VISION (the complaint fix) — the heavens opened, and TWO distinct glorified personages standing in brilliant radiant light: God the Father, and His Son Jesus Christ standing at the Father's RIGHT hand; two separate embodied beings, reverent and luminous like Latter-day Saint gospel art. Stephen, small and awed, gazes up at them from below.",
        "must_not_show": "NEVER one merged figure, NEVER Jesus only, NEVER the Father only; NEVER a dove, triangle, eye, cross or any Trinitarian symbol; no cream robe; no modern object; no scroll or writing as art; the two must be plainly SEPARATE persons.",
        "scene": (
            "The heavens open above the chamber into brilliant, warm heavenly "
            "radiance, and within it stand TWO distinct glorified men, upright and "
            "separate, clothed in radiant white robes of light. On the left, God "
            "the Father — an older majestic man with long white hair and a full "
            "white beard, kindly and full of love. At his RIGHT hand, a half-step "
            "apart, stands his Son Jesus Christ — a Middle-Eastern man of about "
            "thirty-three with warm tan-olive skin, shoulder-length dark brown wavy "
            "hair and a full dark beard, calm and strong, plainly a second and "
            "separate person. Far below and small at the bottom of the frame, "
            "Stephen kneels and gazes up in awe, the radiance on his face. The two "
            "personages are unmistakably two beings; the light fills the sky, not a "
            "ring around any head. Ordinary human proportions, one head each."
        ),
    },
    {
        "id": "v2-r179-b06", "out": "s06-he-said-so-out-loud.jpeg", "seg": "n2",
        "window": "20.262-22.854", "wide": False, "jesus": False, "ref": False,
        "locks": ["COUNCIL-CHAMBER", "STEPHEN"],
        "narration": "And he said so, out loud:",
        "must_show": "Stephen declaring — a close on Stephen, face lit by the vision's radiance, lips parting as he speaks his testimony aloud to the court; the heavenly light still on him.",
        "must_not_show": "no full divine figure in this frame (only the light on him); no cream robe; no modern object; no halo ringing his head; no scroll or writing as art.",
        "scene": (
            "A close on Stephen in the chamber, his upturned face washed in warm "
            "heavenly radiance from above, eyes bright with what he sees, his lips "
            "parting as he begins to declare it aloud. The stone chamber and the "
            "dim shapes of the elders sit low and dark behind him. Ordinary-sized, "
            "one head, his gaze upward and outward, not to the camera; the light "
            "falls on him and is not a ring around his head."
        ),
    },
    {
        "id": "v2-r179-b07", "out": "s07-the-son-of-man-standing.jpeg", "seg": "s1",
        "window": "22.854-28.918", "wide": False, "jesus": False, "ref": False,
        "locks": ["GLORIFIED-FATHER", "GLORIFIED-SON"],
        "narration": "Behold, I see the heavens opened, and the Son of man standing on the right hand of God.",
        "must_show": "SCRIPTURE-EXACT (light-blue caption, Stephen's words) — a closer view of the vision: the Son of man, Jesus Christ, STANDING on the right hand of God the Father in the opened heavens, both glorified and radiant, two separate embodied beings — exactly the verse.",
        "must_not_show": "NEVER one figure, NEVER Jesus only, NEVER the Father only, NEVER the Son SITTING; NEVER a dove or Trinitarian symbol; no cream robe; no modern object; no scroll or writing as art; the two must be plainly SEPARATE persons.",
        "scene": (
            "A closer view up into the opened heavens filled with brilliant warm "
            "radiance: God the Father stands on the left, majestic and kindly with "
            "long white hair and beard in a radiant white robe; at his RIGHT hand, "
            "clearly on his own feet and clearly a separate man, stands the Son of "
            "man, Jesus Christ — warm tan-olive Middle-Eastern features, "
            "shoulder-length dark brown wavy hair, full dark beard, in a radiant "
            "white robe of light, risen and STANDING to receive his witness. The "
            "two are unmistakably two persons side by side, the Son at the Father's "
            "right. Human proportions, one head each; the radiance fills the sky, "
            "not a ring around either head."
        ),
    },
    {
        "id": "v2-r179-b08", "out": "s08-they-would-not-hear.jpeg", "seg": "n3a",
        "window": "28.918-34.096", "wide": False, "jesus": False, "ref": False,
        "locks": ["COUNCIL-CHAMBER", "SANHEDRIN", "STEPHEN"],
        "narration": "They would not hear it. (audio also recaps: heaven is open, the Son of man standing at God's right hand.)",
        "must_show": "the council refusing his testimony — several elders on their feet, hands clapped over their ears, faces contorted, shouting him down; they will not hear what he has seen.",
        "must_not_show": "no divine figure in this frame; no blow landing, no violence yet; no cream robe; no modern object; no halo or ring of light; no scroll or writing as art.",
        "scene": (
            "Inside the chamber the council erupts: three or four elders are up off "
            "their benches, hands pressed hard over their ears, mouths open in a "
            "furious shout, robes swinging as they surge toward Stephen to silence "
            "him. Stephen stands calm at the centre, still lit faintly by the light "
            "from above, unmoved by their rage. Distinct angry faces, ordinary-"
            "sized, one ground plane; nothing written as art."
        ),
    },
    {
        "id": "v2-r179-b09", "out": "s09-rushed-him-out.jpeg", "seg": "n3a",
        "window": "34.096-37.334", "wide": True, "jesus": False, "ref": False,
        "locks": ["OUTSIDE-WALLS", "STEPHEN", "THE-MOB"],
        "narration": "They rushed him out.",
        "must_show": "the establishing wide outside the walls — the crowd drives Stephen out through the city gate onto the bare open ground beyond the wall, the whole travel moving OUTWARD from the gate; the stoning ground.",
        "must_not_show": "no blow landing, no stone striking, no blood; no divine figure; no cream robe; no modern object; no halo; no scroll or writing as art; not a posed line facing the lens.",
        "scene": (
            "The camera looks from outside the city, past the backs of the hurrying "
            "crowd, as they drive Stephen out through the great stone gate onto the "
            "bare dusty ground beyond the wall — the whole press of people moving "
            "away from the gate and out toward open ground, Stephen carried along "
            "in their midst, upright and unresisting. The tan wall and gateway rise "
            "behind, dry hills beyond under an open sky. Backs to the camera, "
            "movement outward; ordinary-sized figures on one ground plane; nothing "
            "written as art; no stone in flight."
        ),
    },
    {
        "id": "v2-r179-b10", "out": "s10-face-of-an-angel.jpeg", "seg": "n3b",
        "window": "37.334-42.059", "wide": False, "jesus": False, "ref": False,
        "locks": ["OUTSIDE-WALLS", "STEPHEN"],
        "narration": "But Stephen's face was the face of an angel — at peace, not afraid.",
        "must_show": "a close on Stephen's serene, luminous face amid the hostile crowd — utterly at peace, unafraid, radiant with calm; the face of an angel.",
        "must_not_show": "no wound, no blood, no fear; no stone striking; no divine figure; no cream robe; no modern object; no halo ringing his head; no scroll or writing as art.",
        "scene": (
            "A close on Stephen's face outside the walls, the blurred angry crowd "
            "soft behind him, warm daylight on his features. His face is calm, open "
            "and luminous with peace, eyes clear and unafraid, the very picture of "
            "someone held by something the crowd cannot see — the face of an angel. "
            "No fear, no hurt shown; ordinary-sized, one head, gaze lifted and not "
            "to the camera; the calm light is on his face, not a ring around it."
        ),
    },
    {
        "id": "v2-r179-b11", "out": "s11-he-knelt-down.jpeg", "seg": "n4a",
        "window": "42.059-48.912", "wide": False, "jesus": False, "ref": False,
        "locks": ["OUTSIDE-WALLS", "STEPHEN", "THE-MOB"],
        "narration": "Then he knelt down, with the stones still coming, and his last words asked mercy for the ones throwing them.",
        "must_show": "Stephen kneeling in prayer for his killers — he has knelt on the open ground, hands open or lifted, face raised in prayer, asking mercy; the mob is a distant threat, never a blow on camera.",
        "must_not_show": "RESTRAINT LAW — NO stone shown striking him, NO stone in close flight at his body, NO wound, NO blood, NO gore; no divine figure; no cream robe; no modern object; no halo; no scroll or writing as art. Parent test.",
        "scene": (
            "Stephen has knelt on the bare dusty ground outside the wall, seen from "
            "the side and a little below, his hands open and lifted, his face raised "
            "to heaven in earnest prayer for the very men against him. The mob "
            "stands well back in the soft-focus distance, a few figures with stones "
            "in their hands held low — but no stone is in flight near him, no blow "
            "lands, and no hurt is shown on his body. The whole weight of the frame "
            "is his praying, forgiving face. Ordinary-sized, one head; nothing "
            "written as art."
        ),
    },
    {
        "id": "v2-r179-b12", "out": "s12-lay-not-this-sin.jpeg", "seg": "s60",
        "window": "48.912-52.842", "wide": False, "jesus": False, "ref": False,
        "locks": ["OUTSIDE-WALLS", "STEPHEN"],
        "narration": "Lord, lay not this sin to their charge.",
        "must_show": "SCRIPTURE-EXACT (light-blue) — the forgiving prayer: a close on Stephen kneeling, face lifted, lips moving in his dying prayer that his killers not be charged with this sin.",
        "must_not_show": "RESTRAINT LAW — no stone striking, no wound, no blood, no gore; no divine figure; no cream robe; no modern object; no halo; no scroll or writing as art.",
        "scene": (
            "A close on the kneeling Stephen outside the walls, face lifted to "
            "heaven, eyes closing, lips parted in the words of his dying prayer — a "
            "look of complete peace and mercy, no bitterness in it. The crowd is "
            "only a soft blur far behind. Warm daylight on his face; no hurt or "
            "blood shown; ordinary-sized, one head, gaze upward; nothing written as "
            "art."
        ),
    },
    {
        "id": "v2-r179-b13", "out": "s13-dont-hold-this.jpeg", "seg": "n4b",
        "window": "52.842-54.711", "wide": False, "jesus": False, "ref": False,
        "locks": ["OUTSIDE-WALLS", "STEPHEN"],
        "narration": "Don't hold this against them, he prayed.",
        "must_show": "Stephen still in prayer — his open, forgiving face and open hands, praying that this not be held against them; mercy to the end.",
        "must_not_show": "RESTRAINT LAW — no stone striking, no wound, no blood; no divine figure; no cream robe; no modern object; no halo; no scroll or writing as art.",
        "scene": (
            "A close on Stephen's face and open hands as he finishes his prayer, "
            "kneeling on the ground, features soft and forgiving, wholly given over "
            "to mercy for his killers. Gentle daylight, the crowd lost to blur "
            "behind. No hurt shown; ordinary-sized, one head, eyes lifted; nothing "
            "written as art."
        ),
    },
    {
        "id": "v2-r179-b14", "out": "s14-he-fell-asleep.jpeg", "seg": "n4b",
        "window": "54.711-56.831", "wide": False, "jesus": False, "ref": False,
        "locks": ["OUTSIDE-WALLS", "STEPHEN"],
        "narration": "And then he fell asleep.",
        "must_show": "the peaceful passing — Stephen sinking gently down at rest, eyes closed, his face perfectly at peace as if fallen asleep, a soft warmth of heaven's light on him; received into glory.",
        "must_not_show": "RESTRAINT LAW — no wound, no blood, no gore, no violent death shown; no divine figure fully shown; no cream robe; no modern object; no halo ringing his head; no scroll or writing as art.",
        "scene": (
            "Stephen sinks gently down onto the ground and comes to rest, seen from "
            "above and the side, his eyes closed and his face perfectly at peace, "
            "as though he has only fallen asleep. A soft warm light from above rests "
            "on his calm features. No wound or blood is shown, no violence — only "
            "rest and peace. Ordinary-sized, one head; the light lies softly on him "
            "and is not a ring around his head; nothing written as art."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: every person is carried by a byte-identical text lock (no face
# sheets exist for these figures). NO mortal Jesus and NO cream in this row; the
# glorified vision figures (b05/b07) are carried by the GLORIFIED-FATHER /
# GLORIFIED-SON text locks above.
REFS = {
}
