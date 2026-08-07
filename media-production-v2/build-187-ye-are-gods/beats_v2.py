#!/usr/bin/env python3
"""V2 beat map — row 187, build-187-ye-are-gods (John 10:31-36 — the leaders take up
stones; Jesus answers by quoting Psalm 82:6, "I have said, Ye are gods; and all of you
are children of the most High," then: "Say ye of him, whom the Father hath sanctified,
and sent into the world, Thou blasphemest; because I said, I am the Son of God?").

COVERAGE: 15 pictures over 64.415 s (card_start) = ~4.3 s/picture (lesson 12
movie-coverage). One place — the TEMPLE-COURT in Jerusalem (Solomon's porch, John 10:23).
A single confrontation covered as a film would cut it: an establishing wide of the
leaders circling Jesus (b01), then singles, two-shots and inserts (the scroll, hands,
faces) through the exchange. Jesus is the steady centre of every beat; the hostile
LEADERS press him.

=====================================================================
OPEN CAMERON COMPLAINT (v2_outline.py 187): NONE. COMPLAINT LEDGER in QC.md is empty.
=====================================================================

SPEAKER LAW (see make_narration.py):
  j1  Ps 82:6 (quoted)  "I have said, Ye are gods..."           GOD → GREEN caption
  j2  John 10:36        "Say ye of him, whom the Father hath..." JESUS → RED caption
Every other segment (n0, n1, n2, n2b, n3a, n3b, card) is the NARRATOR → white.

  - **j1 is the GOD-voice** (the written Psalm's own "I have said"), so its caption is
    GREEN. But **GOD IS NEVER EMBODIED** — the words are the SCRIPTURE Jesus reads aloud
    from their own scroll. So b04/b05 PICTURE Jesus reading/declaring the Psalm to the
    leaders (jesus=True), and the GREEN caption sits over that; no God figure, throne,
    hand, beam or rays appears (the row-169 pattern: God-voice green, God unshown).
  - **j2 is Jesus's own words**, RED, on Jesus's face (b08/b09/b10).
Only Jesus wears cream.

**HARD GATE — GOD / THE FATHER IS NEVER EMBODIED.** j1 (the Psalm) and every mention of
"the Father" (n2 "the one the Father set apart"; j2 "whom the Father hath sanctified, and
sent"; n2b "The Father himself set him apart and sent him") are carried by JESUS himself
— the one the Father set apart and sent, standing embodied before them — and by the
written scroll, NEVER by any figure, face, hand, throne, beam or rays standing in for God
or the Father. No dove, triangle, all-seeing eye or Trinitarian symbol anywhere. The only
embodied divine person is Jesus the Son. No halo, ring or rim-light around anyone
(drift-word gate — word light as warm/plain daylight, never a ring around a head).

CONTENT-CARE: the leaders are hostile and pressing but this stays a DISPUTE OVER
SCRIPTURE, not a lynching — a few may hold loose stones low at the far edge of the wide
(John 10:31), but there is NO stone raised to strike, NO violence, NO blood, NO Jesus
cornered or cowering. Jesus is calm, steady and unafraid throughout; his authority is
quiet, not angry.

TIME-OF-DAY: the temple court in warm plain daylight throughout (winter Feast of
Dedication, John 10:22 — cool clear day, not sunset).

PLACES / LOCKS:
  TEMPLE-COURT   shared/global lock — the first-century Jewish temple court in Jerusalem;
                 v2_stash.py --wire suggests the reusable plate (build-39/173). All beats.
  BACKGROUND-CAST shared/global lock — the temple-court population on the wide beats.
  LEADERS        build-local — the hostile religious rulers/temple authorities circling
                 Jesus; distinct fine-robed men, the same faces across the row.
  Jesus          injected by the assembler on every beat (jesus=True + ref=True + LOCK);
                 only he wears cream.

AUDIO: default AUDIO LOCK stream-copy (no flag). Board Audio = OK. Picture-only build —
do NOT re-voice. card_start = 64.415 s; total with card = 70.793 s.
"""

# LOCKS: TEMPLE-COURT and BACKGROUND-CAST resolve from the shared recipe in
# v2_prompt.py. LEADERS is build-local. Setting locks never name a character. Only
# Jesus wears cream; Jesus is injected on jesus=True beats.
LOCKS = {
    "LEADERS": (
        "LEADERS LOCK: the same group of hostile first-century religious rulers in "
        "every frame — temple authorities and elders of Jerusalem, distinct ordinary "
        "middle-aged and older men with full dark or greying beards, in fine but "
        "sober robes of deep indigo, russet and dark brown with fringed prayer shawls "
        "(never cream, never white) — plainly the men of standing and learning. Their "
        "faces are proud, wary and pressing, not a mob of twins; the same recognizable "
        "men throughout."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r187-b01", "out": "s01-leaders-circling.jpeg", "seg": "n0",
        "window": "0.000-6.867", "wide": True, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT", "LEADERS", "BACKGROUND-CAST"],
        "narration": "The religious leaders were circling Jesus, demanding he say plainly who he claimed to be.",
        "must_show": "the ONE establishing wide — Jesus standing calm and centred in the temple court while the hostile religious leaders close in a pressing ring around him, demanding he say plainly who he claims to be; a few of them hold loose stones low at the far edge, none raised.",
        "must_not_show": "no God or Father figure; no stone raised to strike, no violence, no blood; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing wide of the sunlit temple court, camera set low and behind "
            "the shoulders of the ring of leaders so their backs are three-quarters to "
            "the lens and they look inward past the camera toward Jesus, who stands calm "
            "and centred in the middle of the pressing ring — only he wears the plain "
            "cream robe. The fine-robed leaders close around him demanding an answer; a "
            "few hold loose stones low at the far edge, none raised. Temple porches and "
            "scattered onlookers beyond. Ordinary-sized people on one stone floor, one "
            "head each; warm daylight rests on them, not around their heads; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r187-b02", "out": "s02-not-backing-down.jpeg", "seg": "n1",
        "window": "6.867-11.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "Instead of backing down, he reached into their own scriptures —",
        "must_show": "a close on Jesus standing his ground, steady and unafraid, meeting the leaders' hostility without flinching — instead of backing down he holds firm and calm.",
        "must_not_show": "no God or Father figure; no fear or cowering; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus in the temple-court daylight, his face steady, calm and "
            "unafraid as he meets the leaders' pressing hostility without flinching or "
            "backing away — quiet authority, not anger. Only he wears the plain cream "
            "robe. Ordinary-sized, one head, gaze level toward the leaders and not to "
            "the camera; warm light on his face, not around his head; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r187-b03", "out": "s03-reaching-for-the-scroll.jpeg", "seg": "n1",
        "window": "11.000-15.012", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "to a psalm where God calls mere men gods.",
        "must_show": "Jesus taking up an open scroll of the Psalms from a nearby temple reader — his hands on their own scripture, turning it to the psalm where God calls mere men gods; an insert favouring the hands and the plain scroll.",
        "must_not_show": "no God or Father figure; no legible or rendered writing on the scroll; no halo, glare or rim-light; only Jesus in cream; no modern object; not a cartoon.",
        "scene": (
            "A tighter shot favouring Jesus's hands as he takes up an open scroll of the "
            "Psalms in the temple court and turns it toward the leaders — reaching into "
            "their own scripture to the psalm he means to read. Only he wears the plain "
            "cream robe. The parchment carries no legible or rendered writing. "
            "Ordinary-sized, one head, gaze on the scroll and not to the camera; warm "
            "daylight on his hands, not around his head."
        ),
    },
    {
        "id": "v2-r187-b04", "out": "s04-ye-are-gods.jpeg", "seg": "j1",
        "window": "15.012-19.800", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT", "LEADERS"],
        "narration": "I have said, Ye are gods;",
        "must_show": "GREEN caption (God-voice — the Psalm's own words that Jesus reads aloud) — Jesus reading the open scroll aloud to the leaders, declaring the written line 'I have said, Ye are gods'; the leaders listening, caught by their own book.",
        "must_not_show": "GOD IS NOT SHOWN — no God or Father figure, throne, hand, beam or rays; the words are the scroll Jesus reads; no legible or rendered writing on the scroll; no halo, glare or rim-light; only Jesus in cream; no modern object; not a cartoon.",
        "scene": (
            "A two-shot of Jesus reading the open scroll aloud toward the leaders in the "
            "temple-court daylight, declaring the written line from their own psalm — "
            "only he wears the plain cream robe. The nearest leaders listen, caught by "
            "their own scripture. The scroll carries no legible or rendered writing, and "
            "no figure stands in for God. Ordinary-sized men on one floor, gaze on the "
            "scroll and the leaders and not to the camera; warm daylight, no ring of "
            "light around any head."
        ),
    },
    {
        "id": "v2-r187-b05", "out": "s05-children-of-the-most-high.jpeg", "seg": "j1",
        "window": "19.800-24.295", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT", "LEADERS"],
        "narration": "and all of you are children of the most High.",
        "must_show": "GREEN caption (God-voice from the Psalm) — Jesus finishing the read line, an open hand extended toward the leaders as the scroll names even them 'children of the most High'; the leaders uneasy at hearing their own book turned on them.",
        "must_not_show": "GOD IS NOT SHOWN — no God or Father figure, throne, hand, beam or rays; no legible or rendered writing; no halo, glare or rim-light; only Jesus in cream; no modern object; not a cartoon.",
        "scene": (
            "A closer two-shot: Jesus finishes the line from the scroll and opens a hand "
            "toward the leaders as their own psalm names even them children of the most "
            "High — only he wears the plain cream robe. The leaders' faces turn uneasy at "
            "their own book turned back on them. No figure stands in for God; the scroll "
            "carries nothing legible. Ordinary-sized men on one floor, one head each, "
            "gaze between Jesus and the leaders, not to the camera; warm daylight, no "
            "ring of light around any head."
        ),
    },
    {
        "id": "v2-r187-b06", "out": "s06-if-scripture-called-men-gods.jpeg", "seg": "n2",
        "window": "24.295-28.800", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "His point was sharp: if scripture called men gods because God's word came to them,",
        "must_show": "Jesus reasoning, gesturing from the open scroll outward — making the sharp point that scripture itself called men gods because God's word came to them.",
        "must_not_show": "no God or Father figure; no legible or rendered writing; no halo, glare or rim-light; only Jesus in cream; no modern object; not a cartoon.",
        "scene": (
            "A close on Jesus in the temple-court daylight, one hand on the open scroll "
            "and the other opening outward as he makes his sharp point — that scripture "
            "itself named men gods because God's word had come to them. Only he wears the "
            "plain cream robe. The scroll carries nothing legible. Ordinary-sized, one "
            "head, gaze toward the leaders and not to the camera; warm light on his face, "
            "not around his head."
        ),
    },
    {
        "id": "v2-r187-b07", "out": "s07-condemn-the-one-set-apart.jpeg", "seg": "n2",
        "window": "28.800-32.914", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT", "LEADERS"],
        "narration": "how could they condemn the one the Father set apart?",
        "must_show": "the leaders faltering under the question — how could they condemn the very one the Father set apart, who stands before them; Jesus steady, the leaders' certainty cracking.",
        "must_not_show": "the Father is NOT shown — no God figure, throne, hand or beam (the one set apart is JESUS, embodied before them); no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A two-shot favouring the leaders' faces as they falter under Jesus's "
            "question — their proud certainty cracking at the thought of condemning the "
            "very one the Father set apart, who stands calm before them; only Jesus, at "
            "the edge of frame, wears the plain cream robe. No figure stands in for the "
            "Father. Ordinary-sized men on one floor, one head each, gazes wavering and "
            "not to the camera; warm daylight, no ring of light around any head."
        ),
    },
    {
        "id": "v2-r187-b08", "out": "s08-sanctified-and-sent.jpeg", "seg": "j2",
        "window": "32.914-37.500", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "Say ye of him, whom the Father hath sanctified, and sent into the world,",
        "must_show": "RED caption (Jesus's own words) — Jesus speaking of himself as the one the Father sanctified and sent into the world: a hand to his own breast, quietly claiming the sending.",
        "must_not_show": "the Father is NOT shown — no God figure, throne, hand, beam or rays; the sanctified-and-sent one is Jesus himself; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus in the temple-court daylight, one hand laid to his own "
            "breast as he speaks of himself — the one the Father set apart and sent into "
            "the world — his face grave and sure. Only he wears the plain cream robe. No "
            "figure stands in for the Father. Ordinary-sized, one head, gaze steady "
            "toward the leaders and not to the camera; warm light on his face, not around "
            "his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r187-b09", "out": "s09-thou-blasphemest.jpeg", "seg": "j2",
        "window": "37.500-41.200", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT", "LEADERS"],
        "narration": "Thou blasphemest;",
        "must_show": "RED caption (Jesus's own words) — Jesus repeating the leaders' own charge back to them, 'Thou blasphemest' — an accusing leader's hand thrust toward Jesus while Jesus stands unmoved, holding their word up to the light.",
        "must_not_show": "no God or Father figure; no stone raised, no violence; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A two-shot: a leader's hand thrusts toward Jesus in accusation as Jesus, "
            "unmoved, repeats their own charge back at them — only he wears the plain "
            "cream robe. The leader's face is hard, Jesus's is calm. No stone is raised. "
            "Ordinary-sized men on one floor, one head each, the leader's gaze on Jesus "
            "and Jesus's level, not to the camera; warm daylight, no ring of light around "
            "any head."
        ),
    },
    {
        "id": "v2-r187-b10", "out": "s10-i-am-the-son-of-god.jpeg", "seg": "j2",
        "window": "41.200-45.323", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "because I said, I am the Son of God?",
        "must_show": "RED caption (Jesus's own words) — a strong close on Jesus declaring plainly and without fear, 'because I said, I am the Son of God?' — quiet, certain, unashamed.",
        "must_not_show": "the Father is NOT shown; no God figure or symbol; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A strong close on Jesus in the temple-court daylight as he declares plainly "
            "and without fear that he said he is the Son of God — quiet, certain, "
            "unashamed. Only he wears the plain cream robe. Ordinary-sized, one head, "
            "gaze steady and open toward the leaders and not to the camera; warm light "
            "on his face, not around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r187-b11", "out": "s11-that-was-his-answer.jpeg", "seg": "n2b",
        "window": "45.323-46.880", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "That was his answer.",
        "must_show": "Jesus resolved and at rest after the answer — standing steady in the temple court, the matter plainly said, his face settled.",
        "must_not_show": "no God or Father figure; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus standing steady and resolved in the temple-court daylight, "
            "the answer plainly given and his face settled at rest. Only he wears the "
            "plain cream robe. Ordinary-sized, one head, gaze calm and not to the camera; "
            "warm light on his face, not around his head."
        ),
    },
    {
        "id": "v2-r187-b12", "out": "s12-father-set-him-apart.jpeg", "seg": "n2b",
        "window": "46.880-50.108", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "The Father himself set him apart and sent him into the world.",
        "must_show": "Jesus shown as the one the Father set apart and sent — standing sent and purposed in the temple court, warm daylight resting on him alone from above as the marked and sent one; the Father unseen.",
        "must_not_show": "the Father is NOT shown — no God figure, throne, hand, beam or rays; the setting-apart is warm plain daylight only; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus in the temple court, warm plain daylight resting on him as "
            "the one the Father set apart and sent into the world — purposed and sent, "
            "standing among them yet marked out. Only he wears the plain cream robe. No "
            "figure stands in for the Father, and the light is ordinary daylight, not a "
            "beam. Ordinary-sized, one head, gaze forward and not to the camera; the "
            "light rests on him, not around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r187-b13", "out": "s13-the-plain-truth.jpeg", "seg": "n2b",
        "window": "50.108-56.818", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT", "LEADERS"],
        "narration": "Saying I am the Son of God was not blasphemy — it was the plain truth they would not test.",
        "must_show": "the leaders silent and unwilling — refusing to weigh the plain truth Jesus has spoken; a couple of them looking away or down, unable to answer, while Jesus stands calm and open.",
        "must_not_show": "no God or Father figure; no violence; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A two-shot of the leaders fallen silent and unwilling in the temple-court "
            "daylight — a couple of them looking away or down, unable to answer or to "
            "test the plain truth Jesus has spoken, while Jesus stands calm and open "
            "before them; only he wears the plain cream robe. Ordinary-sized men on one "
            "floor, one head each, the leaders' gazes turned aside and Jesus's level, "
            "not to the camera; warm daylight, no ring of light around any head."
        ),
    },
    {
        "id": "v2-r187-b14", "out": "s14-not-a-second-god.jpeg", "seg": "n3a",
        "window": "56.818-60.247", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "He was not making himself a second God.",
        "must_show": "Jesus humble and single before them — not claiming to be a rival or second God, but the sent Son; an open, unassuming posture, hands low and open.",
        "must_not_show": "no God or Father figure; no second divine figure; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus in the temple-court daylight, his posture open and "
            "unassuming, hands low and open — not setting himself up as a rival or second "
            "God, but standing as the sent Son. Only he wears the plain cream robe. "
            "Ordinary-sized, one head, gaze humble and not to the camera; warm light on "
            "his face, not around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r187-b15", "out": "s15-their-own-book.jpeg", "seg": "n3b",
        "window": "60.247-64.415", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT", "LEADERS"],
        "narration": "He was showing them their own book exposed their logic.",
        "must_show": "the closing image — Jesus holding the open scroll of the Psalms between himself and the leaders, showing them that their own book has exposed the flaw in their logic; the leaders confronted by their own scripture, Jesus at peace.",
        "must_not_show": "no God or Father figure; no legible or rendered writing; no halo, glare or rim-light; only Jesus in cream; no modern object; not a cartoon.",
        "scene": (
            "A closing two-shot with the open scroll of the Psalms held between Jesus and "
            "the leaders in the temple-court daylight — Jesus, at peace, shows them that "
            "their own book has exposed the flaw in their own logic; the leaders stand "
            "confronted by their own scripture. Only he wears the plain cream robe. The "
            "scroll carries no legible or rendered writing. Ordinary-sized men on one "
            "floor, one head each, gazes on the scroll and not to the camera; warm "
            "daylight, no ring of light around any head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# TEMPLE-COURT is a SHARED place with a reusable plate in the stash (build-39/173).
# The runner runs `v2_stash.py --wire build-187-ye-are-gods`, which SUGGESTS the
# temple-court plate to --take; it copies into PLACE-REF/ and records it here. No NEW
# place in this row. Steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: LEADERS is carried by a build-local text lock; the temple-court
# BACKGROUND-CAST by the shared lock. Jesus is injected by the assembler on every beat
# (jesus=True, ref=True). Only Jesus wears cream.
REFS = {
}
