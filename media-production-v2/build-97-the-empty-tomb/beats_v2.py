#!/usr/bin/env python3
"""V2 beat map — row 97, build-97-the-empty-tomb (Luke 24:1-8; Mark 16:1-4).

COVERAGE: 12 pictures over 65.6 s = 5.5 s/picture (matches the library density).

SCRIPTURE FACTS (KJV):
  Luke 24:1  "VERY EARLY in the morning, the FIRST DAY of the week"
        (John 20:1 "when it was yet DARK") — women with prepared
        SPICES coming to anoint the body.
  Mark 16:3  "Who shall ROLL US AWAY THE STONE from the door of the
        sepulchre?" — the worry of the road; v4 "it was VERY GREAT."
  Luke 24:2-3 "they found the stone ROLLED AWAY... and found NOT THE
        BODY."
  Luke 24:4  "TWO MEN stood by them in SHINING GARMENTS" — two
        dazzling figures; v5 the women "bowed down their faces to
        the earth."
  Luke 24:5-6 "WHY SEEK YE THE LIVING AMONG THE DEAD? He is not here,
        but IS RISEN: REMEMBER how he spake unto you..."
  Luke 24:8  "And they REMEMBERED his words."

ANGEL RENDERING (CONTENT-CARE law): the two are real, plain-robed
figures in PALE SILVER-GREY lit to brilliance — NO wings, no ring of
light, nothing outlining the bodies; the shining is the garments in
a light of their own, never the word glow.

TIME OF DAY ARC (intentional): pre-dawn DARK on the road, the first
grey-rose of dawn at the tomb, growing to clear early light by the
close — the first day's sunrise is the story itself, not the row-11
defect.

CONTENT-CARE: no flags. The tomb is EMPTY — grave clothes folded,
never a body; the women's fear rendered with dignity, turning to awe
and remembering.

CHANGING CONDITION (kept OUT of the locks): the light — dark, dawn,
risen morning; the stone — feared, then found rolled; the women —
grieving, afraid, remembering.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream (he does not appear in this row).
LOCKS = {
    "TOMB": (
        "TOMB LOCK: a rock-cut garden tomb — a low doorway cut into "
        "a limestone face, a GREAT DISC STONE in its channel beside "
        "the opening, a hewn stone bench within, olive trees and "
        "spring flowers in the garden around. The same face, stone "
        "and garden throughout."
    ),
    "WOMEN": (
        "WOMEN LOCK: the women are the same three in every shot — "
        "an older one in DEEP MADDER-RED, a tall one in DARK "
        "INDIGO-BLUE, a younger one in DEEP OLIVE-GREEN (never "
        "cream, never white), carrying clay SPICE JARS and folded "
        "linen; grieving, brave, dignified."
    ),
    "TWO": (
        "TWO LOCK: the two messengers are the same pair in every "
        "shot — tall, real human figures in plain PALE SILVER-GREY "
        "robes that shine with a brilliance of their own — NO wings, "
        "no ring of light above any head, nothing outlining the "
        "bodies; calm, strong, ageless faces; feet on the ground."
    ),
}

REF = True

# STALE-V1-FINAL fix (AUDIO-FIX 2026-08-06, Machine A): narration mp3s are newer
# than the V1 mp4 (recency gate fails) and |Δ|>1.0, so the packet-copy AUDIO LOCK
# would ship stale voices. Rebuild from this build's own mp3 segments — $0.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r097-b01", "out": "s01-very-early-on-the-first.jpeg", "seg": "n0",
        "window": "0.28-7.79", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMEN"],
        "narration": (
            "Very early on the first day of the week, while it was still "
            "dark, the women who loved him came to the tomb carrying spices "
            "to anoint his body."
        ),
        "must_show": "SCRIPTURE-EXACT: the dark walk — the three women on the pre-dawn path, spice jars held close, the last stars over the garden hill ahead; love doing the hardest errand.",
        "must_not_show": "no halo, glare or rim-light; the dark REAL pre-dawn — their way lit only by the greying east.",
        "scene": (
            "Before the first birds, the camera beside the path "
            "taking the climb in profile, three "
            "shapes climb the garden path "
            "in the dark: the women with "
            "their clay spice jars held "
            "close and their folded linen, "
            "shawls drawn against the "
            "cold, feet finding the stony "
            "way by the last starlight "
            "and the first grey thinning "
            "of the east — love walking "
            "out before dawn to do the "
            "one tender thing left that "
            "it can think of to do for "
            "the dead. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r097-b02", "out": "s02-and-the-whole-way-there.jpeg", "seg": "n0",
        "window": "7.79-11.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMEN"],
        "narration": "And the whole way there, one thing worried them.",
        "must_show": "the worry — close on the three faces in the greying dark: grief with one practical fear working in it; eyes trading the unspoken problem.",
        "must_not_show": "no halo, glare or rim-light; the worry PRACTICAL — a physics problem carried through grief.",
        "scene": (
            "Close on the three faces in "
            "the greying dark, and the "
            "one worry passing between "
            "them: the older woman's "
            "eyes lifting toward the "
            "hill, the tall one's mouth "
            "tightening, the youngest "
            "glancing from jar to path — "
            "grief's whole errand hanging "
            "on a single practical "
            "problem none of them can "
            "solve, and all of them "
            "walking toward anyway. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r097-b03", "out": "s03-who-shall-roll-us-away.jpeg", "seg": "w3",
        "window": "11.56-14.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB", "WOMEN"],
        "narration": "Who shall roll us away the stone from the door of the sepulchre?",
        "must_show": "SCRIPTURE-EXACT: the question on the road — the women pausing on the path, the tomb's rock face ahead in the half-dark, the great stone's mass the sentence's subject.",
        "must_not_show": "no halo, glare or rim-light; the stone NOT yet visible as moved — the question honest, the answer withheld one beat more.",
        "scene": (
            "The question stops them on "
            "the path: ahead in the "
            "half-dark the limestone face "
            "waits among the olive trees "
            "with its low cut door — and "
            "between the women and their "
            "errand stands the remembered "
            "mass of the great disc "
            "stone, heavier than all "
            "three of them together — "
            "WHO SHALL ROLL IT AWAY — "
            "the honest arithmetic of "
            "small strength against "
            "sealed rock, asked into the "
            "grey air with no answer "
            "anywhere in sight. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r097-b04", "out": "s04-it-took-several-men-to.jpeg", "seg": "n0b",
        "window": "16.41-21.15", "wide": True, "jesus": False, "ref": False,
        "locks": ["TOMB", "WOMEN"],
        "narration": (
            "It took several men to move it, and there were only a few women "
            "walking up that hill in the dark."
        ),
        "must_show": "the disproportion — the three small figures climbing toward the rock face; scale stated by composition: little women, great hill, greater stone.",
        "must_not_show": "no halo, glare or rim-light; the smallness the picture — courage measured against mass.",
        "scene": (
            "The wide grey frame states, the camera behind the "
            "three climbing backs toward the rock face, "
            "the odds: three small "
            "shawled figures on the "
            "climbing path, jars in "
            "arms, and above them the "
            "dark limestone shoulder of "
            "the hill with its tomb cut "
            "in — a stone in its channel "
            "that took a work crew and "
            "levers to seat — the whole "
            "morning's mathematics "
            "walking uphill anyway: not "
            "enough hands, not enough "
            "strength, exactly enough "
            "love. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r097-b05", "out": "s05-but-when-they-arrived-the.jpeg", "seg": "n1",
        "window": "21.66-25.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB", "WOMEN"],
        "narration": (
            "But when they arrived, the huge stone that had sealed the tomb "
            "was rolled away."
        ),
        "must_show": "SCRIPTURE-EXACT: the stone rolled — the women stopped at the garden's edge in first dawn-rose light: the great disc stands OFF its channel, the low doorway open and dark.",
        "must_not_show": "no halo, glare or rim-light; the stone VISIBLY displaced — full doorway open; the women frozen mid-step.",
        "scene": (
            "The path turns and the "
            "problem is gone: in the "
            "first rose-grey of dawn the "
            "great disc stone stands "
            "rolled full off its channel, "
            "leaned aside like a door "
            "someone left open — the low "
            "cut entrance gaping dark and "
            "unsealed — and the three "
            "women stop mid-step at the "
            "garden's edge, jars "
            "forgotten in their arms, "
            "staring at an answered "
            "question they never actually "
            "asked anyone but the air. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r097-b06", "out": "s06-they-stepped-inside-and-the.jpeg", "seg": "n2a",
        "window": "26.19-28.93", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB", "WOMEN"],
        "narration": "They stepped inside — and the body was gone.",
        "must_show": "SCRIPTURE-EXACT: found not the body — inside the tomb: the hewn bench EMPTY, the linen grave clothes lying folded; the women's stunned faces in the doorway light.",
        "must_not_show": "ABSOLUTE: no body anywhere; the linen ORDERLY — absence with the shape of a miracle, not a robbery.",
        "scene": (
            "They duck through the low "
            "door into the cool rock "
            "dark, and the lamp of dawn "
            "follows them in: the hewn "
            "stone bench lies EMPTY — the "
            "linen grave clothes resting "
            "folded and orderly where a "
            "body should be, the head "
            "cloth apart by itself — "
            "nothing torn, nothing "
            "dragged, no robbery's mess: "
            "an absence arranged as "
            "carefully as a made bed, "
            "and three women staring at "
            "it with their spices gone "
            "useless in their hands. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r097-b07", "out": "s07-then-two-figures-in-dazzling.jpeg", "seg": "n3",
        "window": "32.28-38.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB", "WOMEN", "TWO"],
        "narration": (
            "Then two figures in dazzling clothing stood beside them, and "
            "asked a question that has echoed for two thousand years:"
        ),
        "must_show": "SCRIPTURE-EXACT: the two in shining garments — the pair standing suddenly beside the women in the tomb's chamber, silver-grey robes brilliant in the dimness; the women bowing to the earth.",
        "must_not_show": "ABSOLUTE: no wings, no ring of light, nothing outlining the figures — the garments themselves bright; the women's fear reverent.",
        "scene": (
            "Between one heartbeat and "
            "the next the chamber has "
            "four more feet in it: two "
            "tall figures standing where "
            "no one stood, their plain "
            "silver-grey robes bright "
            "with a light that owes "
            "nothing to the door — calm "
            "ageless faces above, the "
            "rock walls washed pale "
            "around them — and the three "
            "women going down, faces to "
            "the earth among their "
            "dropped jars, while the "
            "question of the ages "
            "gathers overhead. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r097-b08", "out": "s08-why-seek-ye-the-living.jpeg", "seg": "s5",
        "window": "39.23-43.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["TWO", "WOMEN"],
        "narration": (
            "Why seek ye the living among the dead? He is not here, but is "
            "risen:"
        ),
        "must_show": "SCRIPTURE-EXACT: the question — close on the nearer messenger's calm face asking it, a hand gesturing at the empty bench; gentle logic overturning the world.",
        "must_not_show": "no wings, no ring of light, no outline; the tone KIND — the question a gift, not a rebuke.",
        "scene": (
            "Close on the kindest "
            "correction ever issued: the "
            "nearer messenger's calm face "
            "bent toward the bowed "
            "women, one hand opening "
            "toward the empty folded "
            "linen — WHY SEEK YE THE "
            "LIVING AMONG THE DEAD — the "
            "question turning the whole "
            "errand gently on its head: "
            "wrong building, wrong "
            "category, wrong tense — HE "
            "IS RISEN — the grammar of "
            "the universe corrected in a "
            "tomb. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r097-b09", "out": "s09-he-is-not-here-he.jpeg", "seg": "n4",
        "window": "45.36-47.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB"],
        "narration": "He is not here — he is risen.",
        "must_show": "the empty bench as gospel — close on the vacant hewn stone and folded linen in the growing dawn light from the door; absence as the best news ever.",
        "must_not_show": "ABSOLUTE: no body, no figure — the emptiness itself the subject, lit warm by the strengthening dawn.",
        "scene": (
            "The frame rests on the best "
            "empty space in history: the "
            "hewn bench bare in the "
            "strengthening light from the "
            "door, the linen lying "
            "folded with the head cloth "
            "set apart, dawn's first warm "
            "gold reaching in across the "
            "cool stone — a vacancy that "
            "no thief could have left so "
            "tidy and no death could "
            "have left at all — NOT "
            "HERE, said the stone; "
            "RISEN, said the light. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r097-b10", "out": "s10-remember-how-he-spake-unto.jpeg", "seg": "s6",
        "window": "48.26-58.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB", "WOMEN", "TWO"],
        "narration": (
            "remember how he spake unto you when he was yet in Galilee, "
            "Saying, The Son of man must be delivered into the hands of "
            "sinful men, and be crucified, and the third day rise again."
        ),
        "must_show": "SCRIPTURE-EXACT: the remember — the two messengers with the risen women, faces lifting as the Galilee words are recalled to them; memory being handed back.",
        "must_not_show": "no wings, no ring of light, no outline; the women RISING from their bow as the remembering begins.",
        "scene": (
            "The messengers hand them "
            "their own memory: REMEMBER "
            "HOW HE SPAKE — and the "
            "women rise slowly from the "
            "earth as it comes: Galilee "
            "evenings, the strange "
            "sentences nobody wanted to "
            "hear, DELIVERED — CRUCIFIED "
            "— AND THE THIRD DAY — the "
            "words rising in their faces "
            "line by line like water "
            "climbing a well, everything "
            "he said standing suddenly "
            "in the light of an empty "
            "bench. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r097-b11", "out": "s11-they-stood-there-confused-and.jpeg", "seg": "n2b",
        "window": "29.49-31.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB", "WOMEN"],
        "narration": "They stood there, confused and afraid.",
        "must_show": "the bewilderment — the three in the tomb's dimness before the empty bench: fear and confusion honest on each face; the moment before the answer.",
        "must_not_show": "no halo, glare or rim-light; the fear DIGNIFIED — trembling stillness, not panic.",
        "scene": (
            "For one long moment the "
            "chamber holds only their "
            "not-knowing: the three "
            "women stock-still in the "
            "cool dimness before the "
            "impossible bench — the "
            "older one's hand pressed to "
            "her mouth, the tall one "
            "gripping the youngest's "
            "arm, all three hearts "
            "hammering against a fact "
            "with no shelf to put it on "
            "— grief's whole map suddenly "
            "useless, and nothing yet "
            "arrived to replace it. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r097-b12", "out": "s12-he-had-said-all-of.jpeg", "seg": "n5a + n5b",
        "window": "60.37-65.24", "wide": True, "jesus": False, "ref": False,
        "locks": ["TOMB", "WOMEN"],
        "narration": (
            "He had said all of it, out loud, before any of it happened. And "
            "they remembered."
        ),
        "must_show": "the closing image — the women stepping out of the tomb into the risen morning: faces alight with remembering, the garden gold with the first day's sun; the running-to-tell about to begin.",
        "must_not_show": "no halo, glare or rim-light; the morning FULLY risen — first sunlight through the olive trees; joy overtaking fear.",
        "scene": (
            "They come out of the dark, the camera outside the "
            "mouth taking their emergence from the side, "
            "into the first day's "
            "morning: the garden gold "
            "and green with new sun "
            "through the olive leaves, "
            "the great stone standing "
            "harmless beside the open "
            "door — and on the three "
            "faces the remembering "
            "finishing its work, fear "
            "tipping over into a joy "
            "with legs in it: skirts "
            "already gathering, jars "
            "left where they fell, three "
            "women one breath from "
            "running with the news that "
            "outruns everything. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    # TOMB: build-37 wire REMOVED 2026-08-05 — build-95's authored law says
    # never the build-37 PARABLE tomb for Jesus's garden tomb (no garden, no
    # olives in that frame). Promote this build's own first approved garden
    # frame instead.
}
# === end PLACE-PLATES ===
