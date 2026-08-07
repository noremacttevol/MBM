#!/usr/bin/env python3
"""V2 beat map — row 181, build-181-morning-stars-sang (Job 38:4-7 — God answers Job
out of the whirlwind: "Where wast thou when I laid the foundations of the earth?...
when the morning stars sang together, and all the sons of God shouted for joy?").

COVERAGE: 14 pictures over 59.87 s (card_start) = ~4.3 s/picture (lesson 12
movie-coverage). The row alternates two threads that must be VISIBLY distinct so the
pictures clearly fit the story: JOB hearing the answer (the human spine) and the
CREATION vision God takes him back to. One establishing wide per place (b02 Job in
the whirlwind, b03 the forming earth).

=====================================================================
OPEN CAMERON COMPLAINT (v2_outline.py 181): "the pictures need to be better made i
dont think they fit the story well."
FIX: this is a fresh, tightly-fitted map where EVERY beat depicts the exact narrated
moment — Job weary and questioning on the ash-heap, the wind rising, the earth's
foundations being laid, Job's eyes lifted off his wreckage, the star-filled heavens
breaking into song, the heavenly host rejoicing, and the comfort brought home to
Job. No vague generic "Bible sky" stand-ins: Job is a clear suffering man, the
creation is a clear first-morning cosmos, and the two never blur together. Review
card should tell Cameron the pictures were rebuilt to fit each moment of the story.
=====================================================================

AUDIO: default AUDIO LOCK stream-copy (no flag). Board Audio = OK. Picture-only
rebuild — do NOT re-voice.

SPEAKER LAW (see make_narration.py):
  g4  Job 38:4  "Where wast thou when I laid the foundations of the earth? declare,
      if thou hast understanding."                                     GOD → GREEN
  s1  Job 38:7  "When the morning stars sang together, and all the sons of God
      shouted for joy?"                                                GOD → GREEN
Everything else is the NARRATOR (white). NO Jesus and NO cream (Old Testament).

**HARD GATE — GOD IS NEVER EMBODIED.** On the GOD-voice beats (b04, b05, b10, b11)
the LORD speaks out of the whirlwind but is NEVER shown: no figure, face, hand,
mouth, throne or beam-being, and no halo/glow/ring of light around anything (the
drift-word gate also bans those literal words — word the light as radiant / brilliant
/ blazing in the scene, never a ring around a head). God's voice is carried by the
whirlwind over Job and by the creation vision itself; the source stays unseen. (This
is the DEFAULT gate — row 179's embodiment was a one-off Cameron asked for and does
NOT apply here.)

THE "SONS OF GOD" (b11): the heavenly host that shouted for joy is shown as a DISTANT
multitude of radiant beings high in the starry heavens, rejoicing — points and forms
of brilliant light far off, NO detailed faces, NO wings-and-halo cherub kitsch, and
NEVER a depiction of God the Father among them. Keep them reverent, distant and
plainly a JOYFUL host, not frightening.

INHERITED CAPTION/AUDIO DESYNC (locked V1 render — do NOT fix; audio immutable):
  · n1r delivered audio OPENS with a recap line ("Where were you, God asked him,
    when I laid the foundations of the earth.") ahead of the caption's "Tell me, if
    you know."; b06 pictures Job humbled under exactly that question, so it reads true.

CONTENT-CARE: plain milk, no violence flags. Job's suffering is shown as weariness and
grief, never as wounds or sores in close-up (restraint on the sick body). The whole
turn is hopeful — from wreckage to wonder to comfort. Time of day: the whirlwind is a
grey storm-dawn; the creation vision is a blazing first-light cosmos; the close brings
warm dawn light onto Job. No ordinary sunset (avoids the row-11 confusion).

PLACES:
  JOB-WHIRLWIND (NEW)  the desolate ground where Job sits in ash and grief as the
                       whirlwind rises and God answers (b01, b02, b06, b07, b08, b14).
  CREATION-DAWN (NEW)  the vision of the first morning God takes Job back to — the
                       forming earth and the star-filled singing heavens (b03, b04,
                       b05, b09, b10, b11, b12, b13).
NEW places (runner promotes each from its first good frame, lesson 11):
  JOB-WHIRLWIND  promote b02 (establishing wide of Job small in the whirlwind)
  CREATION-DAWN  promote b03 (establishing wide of the forming earth — no figure)
Steps in QC.md. No stash plate exists for either yet.
"""

# LOCKS: all build-local. No Jesus / no cream (OT). State clothing colours
# POSITIVELY and dark; only Jesus wears cream and he is not in this row.
LOCKS = {
    "JOB-WHIRLWIND": (
        "JOB-WHIRLWIND LOCK: the same place in every frame — a desolate patch of "
        "bare, ash-strewn ground on the edge of an ancient ruined homestead in the "
        "dry near-eastern wilderness, broken pottery and grey ash around, a low "
        "heap of ashes where a grieving man sits. Above and around, a vast grey "
        "storm-dawn sky with a great whirlwind of dust and cloud turning on the "
        "horizon — the storm out of which the answer comes. Bleak, ancient, "
        "windswept; no modern object, no writing. The same ground, ash-heap and "
        "storm light throughout."
    ),
    "CREATION-DAWN": (
        "CREATION-DAWN LOCK: the same vision-world in every frame — the very first "
        "morning of the world: a young unpeopled earth of raw dark land and bright "
        "new water taking shape under a vast heaven, and above it an immense sky "
        "ablaze with countless brilliant stars and the first radiant break of dawn "
        "light across the deep. Majestic, primordial, celebratory; no building, no "
        "person, no modern object, no writing of any kind. The same forming earth "
        "and blazing star-filled heaven throughout."
    ),
    "JOB": (
        "JOB LOCK: the same man in every shot — an older near-eastern man of about "
        "sixty, weathered olive-brown skin, grey-streaked dark hair and a full "
        "grey-streaked beard, a lined and grief-worn but dignified face. He wears a "
        "plain torn sackcloth-grey and brown robe of a man in mourning (NEVER "
        "cream, never white, never fine cloth). His suffering reads as weariness and "
        "grief only — NO open sores, wounds or lesions shown in close-up. The SAME "
        "man throughout — never twinned, never a cloned face, ordinary-sized, two "
        "hands, one head. Across the row his face turns from weary questioning to "
        "wonder to quiet comfort."
    ),
    "HEAVENLY-HOST": (
        "HEAVENLY-HOST LOCK (the sons of God, b11 only): a distant, joyful multitude "
        "high in the starry heavens — many far-off forms and points of brilliant "
        "radiant light spread across the blazing sky, rejoicing together. They are "
        "DISTANT and small, with NO detailed faces, NO winged-cherub kitsch, NO "
        "haloed cartoon angels; reverent shining figures of light, plainly glad. "
        "God the Father is NEVER among them or shown. Natural to the vast sky, not "
        "crowded to the foreground."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r181-b01", "out": "s01-job-asked-hard-questions.jpeg", "seg": "n0",
        "window": "0.400-2.242", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB-WHIRLWIND", "JOB"],
        "narration": "Job had asked God hard questions.",
        "must_show": "a close on weary Job on the ash-heap — an older grieving man, worn down, having flung hard questions up at heaven; his face searching and spent.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being; no open sores or wounds in close-up; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Job, an older grief-worn man, sitting on the low heap of "
            "ashes in the bleak grey light, his lined face turned up and searching, "
            "spent from flinging hard questions at heaven. Broken pottery and ash "
            "around him, the wind stirring his grey-streaked hair. Ordinary-sized, "
            "one head, gaze up and not to the camera; his suffering reads as "
            "weariness only; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r181-b02", "out": "s02-god-answered-from-the-storm.jpeg", "seg": "n0",
        "window": "2.242-8.641", "wide": True, "jesus": False, "ref": False,
        "locks": ["JOB-WHIRLWIND", "JOB"],
        "narration": "And God answered — not with explanations, but by taking Job back to the very first morning.",
        "must_show": "the ONE establishing wide of the whirlwind — Job small on the ash-heap beneath a vast grey sky with a great whirlwind turning on the horizon, the answer coming out of the storm; he lifts his head toward it.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being in the storm; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art; not a posed line facing the lens.",
        "scene": (
            "A wide from behind and to the side of Job as he sits small on the "
            "ash-heap, his back half to the camera, beneath an immense grey "
            "storm-dawn sky where a great whirlwind of dust and cloud turns on the "
            "horizon. He lifts his head toward the storm as the answer begins to "
            "come — not in words of explanation but as a summons back to the "
            "beginning. The land is desolate and windswept around him. Camera "
            "behind and beside him, his back to the lens; ordinary-sized on one "
            "ground plane; no figure in the storm; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r181-b03", "out": "s03-before-there-were-people.jpeg", "seg": "n1a",
        "window": "8.641-12.082", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREATION-DAWN"],
        "narration": "Before there were people to suffer or to doubt,",
        "must_show": "the ONE establishing wide of the creation vision — the young unpeopled earth of raw land and bright new water taking shape under a vast heaven at the first light, wholly empty of people; before anyone was there to suffer or doubt.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; NO person anywhere; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art; not a posed line facing the lens.",
        "scene": (
            "A vast establishing wide of the first morning of the world: raw dark "
            "new-made land and bright unspoiled water taking shape under an immense "
            "heaven, the first radiant break of dawn light across the deep and the "
            "last great stars still burning above. The camera looks out low across "
            "the forming earth away from the deep toward the far horizon (the world "
            "is utterly empty of people, so no one's back or face is toward the "
            "lens), new and unpeopled. No figure of any kind; nothing is written "
            "anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r181-b04", "out": "s04-foundations-of-the-earth.jpeg", "seg": "g4",
        "window": "12.082-15.402", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREATION-DAWN"],
        "narration": "Where wast thou when I laid the foundations of the earth?",
        "must_show": "GOD-VOICE, GREEN caption — the foundations being laid: great new land, mountains and bedrock rising and settling out of the deep in the first light, the earth's foundations being set; the Maker unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, hand or beam-being laying the earth; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A grand view of the earth's foundations being laid: massive new land, "
            "ridgelines and dark bedrock rising and settling out of the bright "
            "primordial water in the first radiant dawn, mist and light pouring "
            "over the raw young world. No hand or figure appears; the forming is "
            "shown by the land and the light alone. Nothing is written anywhere and "
            "no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r181-b05", "out": "s05-if-thou-hast-understanding.jpeg", "seg": "g4",
        "window": "15.402-20.439", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREATION-DAWN"],
        "narration": "declare, if thou hast understanding.",
        "must_show": "GOD-VOICE, GREEN caption — the scale of it: the immense forming world stretching away beyond comprehension, so vast that no one could declare or understand it; the greatness of what was made before Job.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no person; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "The forming world stretches away in overwhelming scale — range beyond "
            "range of new land, vast bright waters and towering cloud under a "
            "boundless first-light heaven — a greatness far past any human "
            "understanding or telling. Empty of people, immense and still becoming. "
            "Nothing is written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r181-b06", "out": "s06-job-humbled.jpeg", "seg": "n1r",
        "window": "20.439-24.177", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB-WHIRLWIND", "JOB"],
        "narration": "Where were you, God asked him, when I laid the foundations of the earth?",
        "must_show": "Job humbled under the question — back on the ash-heap, Job lowers his eyes, struck small and silent by being asked where he was when the earth was founded.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no open wounds; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Job back on the ash-heap in the grey storm light, his eyes "
            "lowering and his shoulders bowing as the question lands on him — struck "
            "small and silent by being asked where he was when the earth was "
            "founded. The wind pulls at his hair and torn robe. Ordinary-sized, one "
            "head, gaze lowered and not to the camera; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r181-b07", "out": "s07-tell-me-if-you-know.jpeg", "seg": "n1r",
        "window": "24.177-25.547", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB-WHIRLWIND", "JOB"],
        "narration": "Tell me, if you know.",
        "must_show": "Job silent, no answer — a held insert on Job with no reply on his lips, humbled to silence before the question.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A held close on Job in the grey light, lips parted but no answer "
            "coming, his weathered face gone quiet and humble — he has nothing to "
            "say before such a question. Ash and wind around him. Ordinary-sized, "
            "one head, gaze down and inward, not to the camera; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r181-b08", "out": "s08-his-eyes-lifted.jpeg", "seg": "n1r",
        "window": "25.547-36.113", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB-WHIRLWIND", "JOB"],
        "narration": "It sounds severe until you notice what it really does — it lifts Job's eyes off his own wreckage and sets them on something older and steadier than his pain.",
        "must_show": "the turn — Job slowly lifting his eyes UP off the ash and ruin around him toward the vast sky, his gaze pulled from his own wreckage onto something older and steadier than his pain.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "Job slowly lifts his lined face up off the broken pottery and ash "
            "around him toward the vast opening sky, seen from a low side angle, his "
            "eyes drawn away from his own ruin onto something far older and steadier "
            "than his pain. The first faint break of light shows at the edge of the "
            "grey storm. Ordinary-sized, one head, gaze lifting upward and not to "
            "the camera; nothing is written anywhere and no ring of light rings his "
            "head."
        ),
    },
    {
        "id": "v2-r181-b09", "out": "s09-astonishing-in-the-sky.jpeg", "seg": "n2",
        "window": "36.113-40.428", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREATION-DAWN"],
        "narration": "And when that happened, something astonishing broke out in the sky.",
        "must_show": "the heavens beginning to blaze — the first-morning sky breaking into an astonishing brilliance of light and countless stars, something wonderful about to happen above the young world.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no person; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "The first-morning heaven breaks into astonishing brilliance over the "
            "young earth — the vast sky suddenly ablaze with countless brilliant "
            "stars and pouring radiant light, something wonderful breaking loose "
            "above the new-made world. Empty of people; the wonder is in the sky "
            "itself. Nothing is written anywhere and no ring of light rings "
            "anything."
        ),
    },
    {
        "id": "v2-r181-b10", "out": "s10-the-morning-stars-sang.jpeg", "seg": "s1",
        "window": "40.428-43.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREATION-DAWN"],
        "narration": "When the morning stars sang together,",
        "must_show": "GOD-VOICE, GREEN caption — the singing stars: the great morning stars blazing together across the heavens as if in song, a heaven full of brilliant living light.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no faces in the stars; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A soaring view up into the blazing morning heaven where the great "
            "stars burn together in radiant brilliance, their light seeming to ring "
            "and pulse as if in song across the whole sky over the young earth — a "
            "heaven full of living light. No figure or face anywhere in it. Nothing "
            "is written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r181-b11", "out": "s11-sons-of-god-shouted.jpeg", "seg": "s1",
        "window": "43.500-47.487", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREATION-DAWN", "HEAVENLY-HOST"],
        "narration": "and all the sons of God shouted for joy?",
        "must_show": "GOD-VOICE, GREEN caption — the heavenly host rejoicing: a distant joyful multitude of radiant beings high in the blazing starry heavens, shouting for joy over the new-made world.",
        "must_not_show": "GOD IS NEVER SHOWN and the Father is NEVER among them — no God figure or beam-being; no winged-cherub or haloed-cartoon-angel kitsch, no detailed faces; no Jesus, no cream; no ring of light around any head; no modern object; no scroll or writing as art.",
        "scene": (
            "High in the blazing star-filled heaven a distant multitude of radiant "
            "beings — far-off forms and points of brilliant light spread across the "
            "sky — rejoice together over the new-made world, their gladness plain "
            "even at a distance. They are small, distant and reverent, with no "
            "detailed faces and no cartoon wings or rings; simply a joyful shining "
            "host. No figure of God is among them. Nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r181-b12", "out": "s12-stars-broke-into-song.jpeg", "seg": "n3",
        "window": "47.487-49.542", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREATION-DAWN"],
        "narration": "The stars themselves broke into song.",
        "must_show": "the whole singing cosmos — the entire heaven of stars alight and jubilant over the young world, the very stars breaking into song.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no faces in the stars; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "The whole heaven of brilliant stars is alight and jubilant over the "
            "young earth, wave upon wave of radiant light rolling across the sky as "
            "though the very stars have broken into song. Immense, joyful, "
            "unpeopled. Nothing is written anywhere and no ring of light rings "
            "anything."
        ),
    },
    {
        "id": "v2-r181-b13", "out": "s13-creation-a-celebration.jpeg", "seg": "n3",
        "window": "49.542-54.638", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREATION-DAWN"],
        "narration": "Creation was not a cold accident — it was a celebration.",
        "must_show": "creation as celebration — the new world and its blazing joyful heaven together, warm and glad, plainly a celebration and not a cold accident.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no person; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A warm, glad view of the whole new world under its blazing jubilant "
            "heaven at the first dawn — bright water and young land beneath a sky "
            "full of singing radiant stars, the whole scene alive with joy, plainly "
            "a celebration and not a cold and empty accident. Unpeopled, warm, "
            "rejoicing. Nothing is written anywhere and no ring of light rings "
            "anything."
        ),
    },
    {
        "id": "v2-r181-b14", "out": "s14-listening-to-you-now.jpeg", "seg": "n4",
        "window": "54.638-59.869", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB-WHIRLWIND", "JOB"],
        "narration": "The God who sang the world into being is the same one listening to your questions today.",
        "must_show": "the comfort brought home to Job — a close on Job, the wonder now on his face, comforted and quieted, warm first-light on him; the God who sang the world is the one listening to him now.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no open wounds; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Job back on the ash-heap, but changed — the grief eased into "
            "wonder and quiet comfort, his lined face lifted and softened as the "
            "first warm dawn light finally reaches him and the storm calms. The "
            "same God who sang the world into being is listening to him now. "
            "Ordinary-sized, one head, gaze lifted and peaceful, not to the camera; "
            "nothing is written anywhere and the warm light rests on him, not "
            "around his head."
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

# No image REFS: JOB is carried by a byte-identical text lock (no face sheet exists).
# NO Jesus and NO cream in this row.
REFS = {
}
