#!/usr/bin/env python3
"""V2 beat map — row 53, build-53-peters-mother-in-law (Mark 1:29-31).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 15 pictures over 87.2 s narration = 5.8 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Mark 1:29-31 KJV):
  v29  FORTHWITH, when they were come OUT OF THE SYNAGOGUE, they entered
       into the house of SIMON AND ANDREW, WITH JAMES AND JOHN — same
       sabbath day as the synagogue deliverance (row 52); Capernaum;
       midday-to-afternoon light.
  v30  Simon's WIFE'S MOTHER lay SICK OF A FEVER, and ANON THEY TELL HIM
       OF HER — the telling is its own beat; no speech, just friends
       bringing trouble to a friend.
  v31  he came and TOOK HER BY THE HAND, and LIFTED HER UP; and IMMEDIATELY
       the fever left her, and SHE MINISTERED UNTO THEM — the hand-clasp
       lift is THE picture of the build; her serving after is the proof
       and her joy, never servitude.

CONTENT-CARE: row 53 is not in the §3 flag table = GREEN. Restraint anyway:
the fever is real danger (the narration says it could take a life) but she is
never corpse-like; the worry is a family's, quiet. Her ministering is shown
as gladness and restored strength — she WANTS her kitchen back.

CHARACTER CONSISTENCY ACROSS ROWS: Simon, James and John here carry the SAME
descriptions as row 51 (build-51-first-catch-of-fish) so the same men read
across the library. If a simon-ref.jpeg exists in build-51/CAST-REF-V2 when
these frames QC, prefer cross-copying it here as CAST-REF-V2/simon-ref.jpeg.

TIME-OF-DAY ARC: one sabbath — bright midday leaving the synagogue, soft
interior light in the house, dim shuttered back room for the sickbed, then
warm late-afternoon light for the healing, the serving and the meal.

CAST-REF NOTE: when the first still with the mother-in-law's face is ACCEPTED
at QC, copy it to CAST-REF-V2/mother-ref.jpeg and add
"char_refs": ["CAST-REF-V2/mother-ref.jpeg"] to b10-b15. Same for Simon
(simon-ref.jpeg) and Simon's wife (wife-ref.jpeg). Text locks alone do not
hold a face.
"""

LOCKS = {
    "SIMON": (
        "SIMON LOCK: Simon is the same man in every shot — a fisherman of "
        "about thirty-five, thick-set and powerful through the shoulders, "
        "deeply weathered olive-brown skin, dark curly hair, a full dark "
        "beard, heavy brows over quick dark eyes, rope-scarred hands. He "
        "wears a coarse DARK CHARCOAL-BROWN wool tunic with a wide worn "
        "leather belt; never cream, never white. His face is shown clearly."
    ),
    "ANDREW": (
        "ANDREW LOCK: Andrew, Simon's brother, is the same man in every "
        "shot — about thirty, leaner and half a head shorter than Simon, "
        "the same olive-brown weathered skin, straighter dark hair, a "
        "shorter trimmed dark beard, a readier smile. He wears a DARK "
        "SEA-GREEN-GREY wool tunic with a plain leather belt; never cream, "
        "never white."
    ),
    "JAMESJOHN": (
        "JAMES AND JOHN LOCK: the two brothers are the same two men in "
        "every shot — James about thirty, square-built, a full dark beard "
        "and heavy forearms, in a DEEP RUSSET-BROWN wool work tunic; John "
        "about twenty, the youngest of them all, clean-jawed with only the "
        "first shadow of a beard, dark hair to the ears, in a DUSTY DARK "
        "INDIGO wool work tunic. Both wear plain leather belts; neither "
        "wears cream, off-white or any pale near-white cloth."
    ),
    "MOTHER": (
        "MOTHER LOCK: Simon's wife's mother is the same woman in every "
        "shot — about sixty-five, small and fine-boned, silver hair "
        "braided back under a DARK WALNUT-BROWN head covering, a deeply "
        "lined warm face, capable hands that have kept a house for fifty "
        "years. She wears a plain DEEP MADDER-BROWN wool dress; on the "
        "sickbed she lies under a DARK OLIVE-BROWN wool blanket. Nothing "
        "she wears or lies under is cream, off-white or any pale "
        "near-white cloth. Her face is shown clearly."
    ),
    "WIFE": (
        "WIFE LOCK: Simon's wife is the same woman in every shot — about "
        "thirty, strong and steady like her husband, dark hair bound back "
        "under a DUSTY DARK INDIGO head covering, warm worried dark eyes, "
        "her mother's fine-boned face a generation younger. She wears a "
        "DEEP RUSSET wool dress with a dark woven sash; never cream, "
        "never white."
    ),
    "HOUSE": (
        "HOUSE LOCK: the house of Simon and Andrew in Capernaum — a plain "
        "one-storey fisherman's house of dark basalt fieldstone around a "
        "small open courtyard, low doorways hung with dark woven cloth, "
        "rush mats and low wooden stools, clay water jars by the door, "
        "drying nets over the courtyard wall, an outdoor clay oven in the "
        "corner. Ordinary and well-kept — real life happens here. No "
        "cloth anywhere in the house is cream, off-white or any pale "
        "near-white."
    ),
}

REF = True

# Identity law: SIMON is Peter; the token names do not auto-attach the
# global cast sheets (the Lazarus trap) — pin them here.
REFS = {
    "SIMON": ["../CAST-V2-REF/peter-front.jpeg", "../CAST-V2-REF/peter-quarter.jpeg"],
    "ANDREW": ["../CAST-V2-REF/andrew-front.jpeg", "../CAST-V2-REF/andrew-quarter.jpeg"],
    "JAMESJOHN": ["../CAST-V2-REF/james-z-front.jpeg", "../CAST-V2-REF/john-front.jpeg"],
}

BEATS = [
    {
        "id": "v2-r053-b01", "out": "s01-out-of-the-synagogue.jpeg", "seg": "n1 p1",
        "window": "0.28-4.53", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SIMON", "ANDREW", "JAMESJOHN"],
        "narration": ("When Jesus came out of the synagogue that sabbath, he "
                      "did not go off alone."),
        "must_show": "v29 — Jesus coming down the synagogue steps INTO the group of four friends waiting for him; togetherness is the point.",
        "must_not_show": "no crowd mobbing him here — the sabbath crowd has dispersed; this is the small circle.",
        "scene": (
            "The camera off at the street's side takes the meeting "
            "in profile: Jesus comes down the worn basalt steps of the Capernaum "
            "synagogue into the bright sabbath midday, and the four "
            "fishermen close around him easily as he reaches the street — "
            "Simon already talking, a hand half-raised, Andrew grinning at "
            "his brother, James and John falling in on the other side — "
            "five men leaving together the way friends leave a place, "
            "shoulder near shoulder. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r053-b02", "out": "s02-home-with-his-friends.jpeg", "seg": "n1 p2",
        "window": "4.53-11.36", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "ANDREW", "JAMESJOHN", "HOUSE"],
        "narration": ("He went home with his friends, into the house of "
                      "Simon and Andrew, and James and John went in with "
                      "them."),
        "must_show": "the arrival — Simon pushing back the door-cloth of his own house, bringing Jesus home.",
        "must_not_show": "an ordinary lane, an ordinary door — nothing announces what lives inside today.",
        "scene": (
            "In the narrow basalt lane the five men arrive at the house — "
            "Simon a step ahead, holding the dark door-cloth aside with "
            "one arm and turning back to bring Jesus in with a tilt of "
            "his head, Jesus stooping toward the low doorway, Andrew, "
            "James and John bunched behind them in the bright lane — a "
            "fisherman bringing the Teacher home to dinner, drying nets "
            "over the courtyard wall. Midday sabbath light. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r053-b03", "out": "s03-an-ordinary-house.jpeg", "seg": "n2 p1",
        "window": "11.36-14.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": ("It was an ordinary house, the kind of place where "
                      "real life happens."),
        "must_show": "the house itself — the small courtyard, the tools of a working family's daily life; no people needed.",
        "must_not_show": "nothing grand, nothing staged — worn, loved, ordinary.",
        "scene": (
            "The small basalt courtyard in soft midday light, empty of "
            "people for one quiet frame: rush mats and low stools around "
            "the cold clay oven, a water jar sweating by the doorway, a "
            "child's wooden toy boat forgotten by the wall, mended nets "
            "folded over the parapet, a sprig of herbs drying under the "
            "eave — fifty small proofs of a family's real, ongoing, "
            "ordinary life."
        ),
    },
    {
        "id": "v2-r053-b04", "out": "s04-the-house-was-heavy.jpeg", "seg": "n2 p2",
        "window": "14.44-19.72", "wide": False, "jesus": False, "ref": False,
        "locks": ["WIFE", "HOUSE"],
        "narration": ("But that day the house was heavy, because someone "
                      "they loved was ill."),
        "must_show": "the weight — Simon's wife at the back-room doorway, the worry a family carries in its shoulders.",
        "must_not_show": "no weeping; the heaviness is quiet, held-in, ongoing.",
        "scene": (
            "Simon's wife stands at the curtained doorway of the back "
            "room with a clay bowl of water held against her hip, paused "
            "mid-task — her head leaned against the doorpost for one "
            "stolen second, eyes closed, the worry of days plain in the "
            "set of her shoulders — before going back in. The bright "
            "courtyard behind her only makes the dark doorway darker. "
            "Exactly one person is in the frame, with two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r053-b05", "out": "s05-sick-with-a-fever.jpeg", "seg": "n3 p1",
        "window": "19.72-22.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOTHER", "HOUSE"],
        "narration": ("Simon's wife's mother lay in a back room, sick with "
                      "a fever."),
        "must_show": "v30 — the small silver-haired woman on her sleeping mat in the dim shuttered room, flushed and weak.",
        "must_not_show": "fevered and diminished, never corpse-like; she breathes, she suffers, she is loved.",
        "scene": (
            "In the dim back room, shutters drawn against the midday "
            "heat, the old woman lies small on a sleeping mat under the "
            "dark olive-brown blanket, her lined face flushed and damp, "
            "silver hair loose against the folded cloth beneath her "
            "head, one thin hand curled weakly on the blanket's edge — a "
            "strong capable woman shrunk by fever to the size of the "
            "worry she causes. A single line of light falls through the "
            "shutter. Exactly one person is in the frame, with two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r053-b06", "out": "s06-little-anyone-could-do.jpeg", "seg": "n3 p2",
        "window": "22.91-30.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOTHER", "WIFE", "HOUSE"],
        "narration": ("In those days a fever like that could take a life, "
                      "and there was little anyone could do but sit beside "
                      "her and worry."),
        "must_show": "the helpless vigil — the daughter wringing a cloth at the bedside, doing the only thing there is to do.",
        "must_not_show": "no physician, no remedies — that is the point; only love and a wet cloth.",
        "scene": (
            "Simon's wife kneels beside the sleeping mat in the "
            "shuttered dimness, wringing a cloth over the clay bowl "
            "with both hands before laying it gently across her "
            "mother's burning forehead — her own face tight with the "
            "specific helplessness of tending someone medicine cannot "
            "reach. The old woman's eyes are closed; her breathing "
            "shows shallow in the blanket's rise. Exactly two people "
            "are in the frame; each has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r053-b07", "out": "s07-they-told-him.jpeg", "seg": "n4 p1",
        "window": "30.28-31.96", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "HOUSE"],
        "narration": "So they told Jesus about her.",
        "must_show": "v30 — the telling: Simon speaking low to Jesus just inside the courtyard, a thumb toward the back room.",
        "must_not_show": "no kneeling, no formal petition — a man telling his friend.",
        "scene": (
            "Just inside the courtyard, Simon stands close to Jesus and "
            "tells him — voice plainly low, his head bent near, one "
            "rough thumb hooked back over his shoulder toward the "
            "curtained back-room doorway, his bearded face worried and "
            "direct — and Jesus listens with his eyes already moving "
            "past Simon's shoulder to the dark doorway. Exactly two "
            "people are in the frame; each has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r053-b08", "out": "s08-the-way-you-tell-a-friend.jpeg", "seg": "n4 p2",
        "window": "31.96-40.01", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON"],
        "narration": ("They did not make a speech or a grand request; they "
                      "simply brought their trouble to him, the way you "
                      "tell a friend what is wrong."),
        "must_show": "the closeness of it — two faces, one worried and one attending; friendship doing the asking.",
        "must_not_show": "no clasped begging hands; the trust is casual, and that is its beauty.",
        "scene": (
            "A close two-shot in the courtyard's soft light: Simon's "
            "weathered face carries the trouble plainly — brows drawn, "
            "the words simple and already half-relieved for having said "
            "them — and Jesus's face, close and turned fully to him, "
            "attends to his friend with the whole of his attention, "
            "nothing between the two men but trust. Exactly two people "
            "are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r053-b09", "out": "s09-he-went-in.jpeg", "seg": "n5 p1",
        "window": "40.01-41.55", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": "And he went in to where she was lying.",
        "must_show": "v31 — Jesus stooping under the low lintel through the curtain into the dim room; the light following him in.",
        "must_not_show": "he goes in without hesitation — no pause at the threshold.",
        "scene": (
            "Jesus stoops under the low stone lintel of the back room, "
            "one hand drawing the dark curtain aside, mid-step from the "
            "bright courtyard into the shuttered dimness — daylight "
            "spilling past his shoulders across the floor toward the "
            "sleeping mat — entering the sickroom as simply as a man "
            "enters his own house. Exactly one person is in the frame, "
            "with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r053-b10", "out": "s10-beside-her.jpeg", "seg": "n5 p2",
        "window": "41.55-45.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOTHER", "HOUSE"],
        "narration": "What happened next, Mark tells in a single sentence.",
        "must_show": "the stillness before — Jesus kneeling down beside the mat, looking at her face; nothing has happened yet.",
        "must_not_show": "his hand has not taken hers yet; this frame is the approach.",
        "scene": (
            "Jesus kneels down beside the sleeping mat in the dim room, "
            "settled on one knee close beside the small fevered woman, "
            "looking into her flushed sleeping face with unhurried "
            "attention — the line of shutter-light lying across the "
            "blanket between them, his hands still resting on his own "
            "knee. The room is utterly quiet. Exactly two people are in "
            "the frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r053-b11", "out": "s11-took-her-by-the-hand.jpeg", "seg": "s31",
        "window": "45.33-53.24", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOTHER", "HOUSE"],
        "narration": ("And he came and took her by the hand, and lifted her "
                      "up; and immediately the fever left her, and she "
                      "ministered unto them. (Mark 1:31)"),
        "must_show": "THE picture of the build — his hand clasping hers, lifting; her rising from the mat, eyes open, the fever visibly gone from her face.",
        "must_not_show": "no light effect, no glow; the miracle is a hand-clasp and a face coming clear.",
        "scene": (
            "The lift: Jesus's hand is closed firmly around the old "
            "woman's thin hand and forearm, drawing her up from the mat "
            "with the strength of it, and she is rising — coming up off "
            "the bedding toward sitting with her eyes open and her lined "
            "face already clear, the flush gone, her free hand catching "
            "the blanket at her lap — pulled back into her life by one "
            "human handhold. The shutter-light lands across their joined "
            "hands. Exactly two people are in the frame; each has two "
            "arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r053-b12", "out": "s12-the-fever-left-her.jpeg", "seg": "n6",
        "window": "53.24-62.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOTHER", "WIFE", "SIMON", "HOUSE"],
        "narration": ("No slow recovery, no days of weakness; the heat and "
                      "the sickness were gone, and she was herself once "
                      "more, well and strong."),
        "must_show": "the proof — her ON HER FEET in the room, steady, herself; the family crowding the doorway in disbelief.",
        "must_not_show": "she needs no supporting arm — standing unaided is the whole sentence.",
        "scene": (
            "The old woman stands beside her own sickbed on steady feet, "
            "unaided, smoothing down her madder-brown dress with both "
            "capable hands, her lined face clear and vivid with returned "
            "strength — Jesus stands back by the wall giving her room, "
            "quietly pleased — while at the curtained doorway Simon and "
            "his wife crowd in against each other, the daughter's hand "
            "flying to her mouth. The shutters have been thrown open; "
            "afternoon light fills the little room. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r053-b13", "out": "s13-she-rose-to-serve.jpeg", "seg": "n7 p1",
        "window": "62.53-65.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOTHER", "HOUSE"],
        "narration": "And the first thing she did was rise and serve them.",
        "must_show": "her choice — striding into HER courtyard, taking her kitchen back, already reaching for the work.",
        "must_not_show": "not obligation — appetite; a woman reclaiming the thing the fever stole.",
        "scene": (
            "The old woman strides out of the back room into the "
            "afternoon-lit courtyard with the purpose of a general "
            "retaking a city — sleeves already being pushed up her thin "
            "strong arms, her eye sweeping the cold oven and the water "
            "jars, one hand reaching down a flat basket from the wall "
            "peg without breaking stride — a woman restored to exactly "
            "where she rules. Exactly one person is in the frame, with "
            "two arms, two hands, two legs and one head."
        ),
    },
    {
        "id": "v2-r053-b14", "out": "s14-she-ministered-unto-them.jpeg", "seg": "n7 p2",
        "window": "65.16-73.03", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOTHER", "SIMON", "ANDREW", "JAMESJOHN", "HOUSE"],
        "narration": ("With her strength fully back, she cared for the very "
                      "ones who had carried her trouble to Jesus, glad to "
                      "be on her feet again."),
        "must_show": "v31 — the serving: her setting bread down before Jesus and the four, glad, quick, entirely herself.",
        "must_not_show": "nobody stops her or fusses over her — they let her serve, and that is the honour.",
        "scene": (
            "In the warm late-afternoon courtyard the old woman sets a "
            "board of flat bread and a dish of olives down in the middle "
            "of the seated circle — Jesus, Simon, Andrew, James and John "
            "on the mats and low stools — her lined face bright with the "
            "particular gladness of being useful again, mid-word in some "
            "scolding hospitality, while Simon leans back laughing and "
            "Jesus looks up at her with open warmth. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r053-b15", "out": "s15-the-quiet-house.jpeg", "seg": "n8",
        "window": "73.03-86.87", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOTHER", "WIFE", "SIMON", "ANDREW", "JAMESJOHN", "HOUSE"],
        "narration": ("It is a small, quiet miracle, tucked into an "
                      "ordinary house. No crowd and no spectacle; only a "
                      "tired family, a sickbed, and a Savior who came in, "
                      "took her by the hand, and made her whole."),
        "must_show": "the closing frame — the whole household at the meal in the golden hour, whole and at peace; the healed woman seated among them now.",
        "must_not_show": "no crowd at the gate yet (that is the next story); the frame stays private, warm, complete.",
        "scene": (
            "The whole household gathered in the small courtyard, "
            "the camera at the courtyard wall behind the near "
            "shoulders, as the "
            "light goes golden: Jesus and the four fishermen around the "
            "shared food, Simon's wife pouring water, and the old woman "
            "seated now in the midst of them — her work done, her hands "
            "finally at rest in her lap, watching Jesus talk with the "
            "unhurried face of a woman entirely well in a house entirely "
            "at peace. Drying nets over the wall, the day ending, an "
            "ordinary house holding a quiet miracle. Every figure has "
            "two arms, two hands and one head."
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
