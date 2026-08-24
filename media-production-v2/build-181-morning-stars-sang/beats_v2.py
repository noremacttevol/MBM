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
CURRENT CAMERON COMPLAINT (reported against 53514a78d): "0:12 god mispronounced
wast and pictures can't be duplicates with just missing pieces. Make better pictures."
PROMPT AUTOPSY: CAUSED. The first V2 generation promoted b02 and b03 as place plates,
then fed those exact compositions back into every sibling beat under the rough-draft
continuity instruction. The resulting contact sheet visibly repeats the same seated
Job/whirlwind frame across b01/b02/b07/b08 and the same shore/starfield across
b03/b05/b09/b10/b11, sometimes with only Job or a patch of light removed. This fix
generates all fourteen pictures without either place plate, keeps only Job's face
reference, and gives every beat a different named camera geometry. No copy, crop,
extended hold, removal-only edit, or plate-derived variant can satisfy this complaint.
God's g4 source receives persistent Flash-v2 CMU W AO1 S T (American stressed
/wɔst/, rhyming with "lost"), while the visible KJV spelling remains "wast."
=====================================================================

AUDIO: AUDIO_FROM_V1_SEGMENTS remains required. Re-voice ONLY g4 through the
persistent build-local revoice_wast.py; all other source segments remain untouched.

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

# AUDIO: the V1 final mp4 (67.433s) is 0.821s longer than the current segment
# timeline (66.612s) — a stale trailing take the STALE-V1 guard rejects for a
# stream-copy. Per the assembler's prescribed fix, rebuild the track from THIS
# build's own ElevenLabs mp3s (audio/*.mp3 = 44100/128000, byte-identical voices
# to the V1 final) at the extract_beats offsets. Nothing re-voiced, nothing
# re-timed; V1 stays read-only.
AUDIO_FROM_V1_SEGMENTS = True

# LOCKS: all build-local. No Jesus / no cream (OT). State clothing colours
# POSITIVELY and dark; only Jesus wears cream and he is not in this row.
LOCKS = {
    "SHOT-DIVERSITY": (
        "SHOT-DIVERSITY COMPLAINT LOCK: this must be a genuinely new cinematic "
        "composition made for this one narrated beat. Continuity means the same "
        "Job identity, materials, weather and story world — NEVER the same camera "
        "coordinates. Do not copy, crop, zoom, mirror, relight, mask, add to, or "
        "remove pieces from another frame. Never repeat another beat's horizon, "
        "shoreline, ground layout, seated pose, whirlwind placement or star pattern. "
        "The named camera height, direction, foreground and focal subject below are "
        "mandatory and visibly different from every adjacent picture."
    ),
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
        "locks": ["SHOT-DIVERSITY", "JOB-WHIRLWIND", "JOB"],
        "narration": "Job had asked God hard questions.",
        "must_show": "a TIGHT chest-and-face shot from Job's FRONT-LEFT — his searching face fills the upper half, one raised empty hand at lower right, only a thin blurred strip of ash behind him; a unique question-shot, not the seated whirlwind wide.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being; no open sores or wounds in close-up; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "TIGHT chest-and-face photograph from Job's FRONT-LEFT at eye height. "
            "His lined searching face fills the upper half as he looks far above "
            "the camera, and one empty weathered hand is lifted palm-up at lower "
            "right as the last hard question leaves him. The ash heap is only a "
            "thin soft-focus strip behind his shoulder; no visible horizon and no "
            "full seated body. Wind moves his grey-streaked hair. This exact "
            "face-and-hand geometry belongs only to b01; nothing is written."
        ),
    },
    {
        "id": "v2-r181-b02", "out": "s02-god-answered-from-the-storm.jpeg", "seg": "n0",
        "window": "2.242-8.641", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "JOB-WHIRLWIND", "JOB"],
        "narration": "And God answered — not with explanations, but by taking Job back to the very first morning.",
        "must_show": "an EXTREME WIDE from far behind — Job is a tiny full-body figure in the LOWER-LEFT fifth while a tall whirlwind occupies the RIGHT half and the storm sky fills most of the frame; unmistakably unlike b01.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being in the storm; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art; not a posed line facing the lens.",
        "scene": (
            "EXTREME WIDE from far behind Job across a long sweep of ash-strewn "
            "ground. Job is a tiny complete figure in the LOWER-LEFT fifth, back "
            "to the lens and head lifted. A single tall column of dust and cloud "
            "turns on the far RIGHT and the layered storm sky fills the upper two "
            "thirds. His stones and body do not resemble the b01 close. No figure "
            "in the storm, no copied seated portrait, nothing written."
        ),
    },
    {
        "id": "v2-r181-b03", "out": "s03-before-there-were-people.jpeg", "seg": "n1a",
        "window": "8.641-12.082", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "CREATION-DAWN"],
        "narration": "Before there were people to suffer or to doubt,",
        "must_show": "a LOW SHORELINE establishing shot — three jagged black foreground rocks form a diagonal from LOWER-LEFT toward a new silver-blue inlet on the RIGHT, with the first pale light on the horizon; completely unpeopled.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; NO person anywhere; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art; not a posed line facing the lens.",
        "scene": (
            "LOW SHORELINE establishing photograph only inches above raw stone. "
            "Three jagged black foreground rocks make a strong diagonal from the "
            "LOWER-LEFT toward a newly formed silver-blue inlet occupying the "
            "RIGHT half. A pale first-light horizon lies low in the frame and "
            "countless stars remain above. The world is empty of people. This "
            "specific low diagonal shoreline appears nowhere else; no figure or "
            "writing and no ring of light."
        ),
    },
    {
        "id": "v2-r181-b04", "out": "s04-foundations-of-the-earth.jpeg", "seg": "g4",
        "window": "12.082-15.402", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "CREATION-DAWN"],
        "narration": "Where wast thou when I laid the foundations of the earth?",
        "must_show": "GOD-VOICE, GREEN caption — a WATER-LEVEL UPWARD view at the base of one immense wet basalt cliff rising on the LEFT while surf explodes against newly exposed bedrock below; the earth's foundation visibly solid, Maker unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, hand or beam-being laying the earth; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "WATER-LEVEL camera looking steeply UP from churning primordial surf "
            "at the base of one immense wet basalt cliff that rises along the LEFT "
            "edge and disappears into first-dawn mist. Fresh black bedrock fills "
            "the lower half; white spray bursts against it from the RIGHT. No "
            "shoreline panorama, starfield template, hand or figure. The solid "
            "foundation itself is the subject; nothing is written."
        ),
    },
    {
        "id": "v2-r181-b05", "out": "s05-if-thou-hast-understanding.jpeg", "seg": "g4",
        "window": "15.402-20.439", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "CREATION-DAWN"],
        "narration": "declare, if thou hast understanding.",
        "must_show": "GOD-VOICE, GREEN caption — a HIGH BIRD'S-EYE view down over braided new rivers, multiple mountain chains and distant seas, no repeated shoreline or horizon; the world extends beyond comprehension, Maker unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no person; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "HIGH BIRD'S-EYE photograph looking diagonally DOWN across a continent-"
            "sized sweep of braided silver rivers, several parallel young mountain "
            "chains and distant dark seas. Clouds cast huge moving shadows across "
            "the land, with almost no sky visible. The scale is beyond one person's "
            "understanding. No copied inlet, no foreground shore, no person, no "
            "figure of God, and nothing written."
        ),
    },
    {
        "id": "v2-r181-b06", "out": "s06-job-humbled.jpeg", "seg": "n1r",
        "window": "20.439-24.177", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "JOB-WHIRLWIND", "JOB"],
        "narration": "Where were you, God asked him, when I laid the foundations of the earth?",
        "must_show": "a STEEP OVERHEAD view from behind Job's right shoulder — his bowed head and both open hands on his knees form a triangle inside a visible ring of ash and broken potsherds; no horizon and no duplicated seated landscape.",
        "must_not_show": "ONE SINGLE UNBROKEN PHOTOGRAPH ONLY — no stacked frames, repeated strips, split-screen, triptych, diptych, collage, panel, border or duplicated copy of Job; GOD IS NEVER SHOWN — no God figure or beam-being; no open wounds; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "ONE SINGLE UNBROKEN STEEP OVERHEAD photograph from behind Job's "
            "RIGHT shoulder, looking "
            "down onto his bowed grey-streaked head and BOTH open empty hands "
            "resting separately on his knees. A ring of ash and several broken "
            "potsherds surrounds him as the question humbles him. No face toward "
            "the lens, no horizon, no whirlwind column, no duplicated side-on "
            "seated landscape. The one camera view fills the entire canvas with no "
            "repeated strips, panels or borders; nothing is written."
        ),
    },
    {
        "id": "v2-r181-b07", "out": "s07-tell-me-if-you-know.jpeg", "seg": "n1r",
        "window": "24.177-25.547", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "JOB-WHIRLWIND", "JOB"],
        "narration": "Tell me, if you know.",
        "must_show": "an EXTREME RIGHT-SIDE PROFILE insert from temple to collarbone — Job's lips closed, jaw slack and gaze lowered out the LEFT edge; background is featureless windblown grey, not another full ash-heap pose.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "EXTREME RIGHT-SIDE PROFILE insert cropped from Job's temple to his "
            "collarbone. His mouth is now closed, jaw slack, and eyes lower out "
            "through the LEFT edge: no answer. Wind moves individual beard hairs "
            "against a featureless soft grey background. No hands, seated body, "
            "horizon, rocks or whirlwind are visible, so this cannot be a piece-"
            "removed version of b01/b02/b06. Nothing is written."
        ),
    },
    {
        "id": "v2-r181-b08", "out": "s08-his-eyes-lifted.jpeg", "seg": "n1r",
        "window": "25.547-36.113", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "JOB-WHIRLWIND", "JOB"],
        "narration": "It sounds severe until you notice what it really does — it lifts Job's eyes off his own wreckage and sets them on something older and steadier than his pain.",
        "must_show": "a LOW GROUND-LEVEL medium shot from Job's FRONT-RIGHT — sharp potsherds dominate the LOWER-LEFT foreground while Job, from waist up on the RIGHT, turns his eyes diagonally to an opening in the upper-left sky.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "LOW GROUND-LEVEL medium photograph from Job's FRONT-RIGHT. Large "
            "sharp potsherds and grey ash dominate the LOWER-LEFT foreground; Job "
            "appears waist-up on the RIGHT, turning his lined face and eyes "
            "diagonally toward a natural break in the UPPER-LEFT clouds. The "
            "wreckage and the destination of his gaze share one depth. No full "
            "seated silhouette, no repeated whirlwind placement, no lens gaze, "
            "nothing written and no light ring around his head."
        ),
    },
    {
        "id": "v2-r181-b09", "out": "s09-astonishing-in-the-sky.jpeg", "seg": "n2",
        "window": "36.113-40.428", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "CREATION-DAWN"],
        "narration": "And when that happened, something astonishing broke out in the sky.",
        "must_show": "a STRAIGHT-UP sky view through dark torn clouds — one brilliant diagonal river of stars opens from LOWER-RIGHT to UPPER-LEFT, with only a tiny black ridge at the bottom; no copied shoreline, inlet or familiar horizon.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no person; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "STRAIGHT-UP camera aimed through dark torn first-morning clouds. A "
            "single brilliant diagonal river of countless stars opens from the "
            "LOWER-RIGHT to the UPPER-LEFT, as if the heavens have just broken "
            "wide. Only a tiny black ridge touches the bottom edge; no water, "
            "shoreline, inlet, person or figure. The sky event is one continuous "
            "photograph, not a portal or ring; nothing is written."
        ),
    },
    {
        "id": "v2-r181-b10", "out": "s10-the-morning-stars-sang.jpeg", "seg": "s1",
        "window": "40.428-43.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "CREATION-DAWN"],
        "narration": "When the morning stars sang together,",
        "must_show": "GOD-VOICE, GREEN caption — an EARTH-ABSENT overhead sky composition: seven dominant morning stars sweep in a broad S-curve through a dense deep-blue starfield, visibly distinct from b09's cloud opening and every shoreline view.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no faces in the stars; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "EARTH-ABSENT overhead photograph containing sky edge to edge: seven "
            "dominant morning stars sweep in a broad S-curve from lower left to "
            "upper right through a dense deep-blue field of smaller stars. Their "
            "ordinary starlight varies like voices in one song, but there are no "
            "drawn sound waves, rings, faces, clouds, land, water, figures or "
            "writing. This is not b09's diagonal opening."
        ),
    },
    {
        "id": "v2-r181-b11", "out": "s11-sons-of-god-shouted.jpeg", "seg": "s1",
        "window": "43.500-47.487", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "CREATION-DAWN", "HEAVENLY-HOST"],
        "narration": "and all the sons of God shouted for joy?",
        "must_show": "GOD-VOICE, GREEN caption — from a LOW NEW-MOUNTAIN vantage, a wide crescent of many small distant radiant beings crosses only the UPPER third above a newborn valley; visibly humanlike host silhouettes, Father absent.",
        "must_not_show": "GOD IS NEVER SHOWN and the Father is NEVER among them — no God figure or beam-being; no glowing stick figures, cutouts, repeated identical silhouettes, evenly copied figures, circular ring or decorative arch; no winged-cherub or haloed-cartoon-angel kitsch, no detailed faces; no Jesus, no cream; no ring of light around any head; no modern object; no scroll or writing as art.",
        "scene": (
            "LOW camera from the floor of a newborn dark valley looking upward "
            "between two steep mountain walls. Across only the UPPER third, a "
            "loose gathering of many SMALL DISTANT, naturally proportioned "
            "humanlike host silhouettes raise DIFFERENT natural arm poses in "
            "visible joy. Starlight illuminates ordinary pale robes and bodies; "
            "the people do not emit light and are irregularly spaced at several "
            "depths, never copied into a ring or arch. They remain far away with "
            "no faces, wings or rings; the Father is not among them. The lower valley makes "
            "this unlike every star-only or shoreline frame. Nothing is written."
        ),
    },
    {
        "id": "v2-r181-b12", "out": "s12-stars-broke-into-song.jpeg", "seg": "n3",
        "window": "47.487-49.542", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "CREATION-DAWN"],
        "narration": "The stars themselves broke into song.",
        "must_show": "a WATER-REFLECTION insert — rippled black new sea fills most of the frame, reflecting many bright stars as broken dancing lines, while only a narrow band of real sky remains at the top; no copied sky panorama.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no faces in the stars; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "WATER-REFLECTION insert at the surface of a rippled black newborn sea. "
            "The water fills the lower four-fifths and reflects hundreds of bright "
            "stars as separate broken dancing lines; only a narrow band of the real "
            "starry sky remains at the very top. No shoreline panorama, host, face, "
            "figure, symbolic music marks or writing. The reflection itself makes "
            "the stars read as song."
        ),
    },
    {
        "id": "v2-r181-b13", "out": "s13-creation-a-celebration.jpeg", "seg": "n3",
        "window": "49.542-54.638", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "CREATION-DAWN"],
        "narration": "Creation was not a cold accident — it was a celebration.",
        "must_show": "a GROUND-LEVEL celebration shot — warm first sunlight strikes a newborn waterfall spilling through black rock into a bright pool, spray filling the air under a star-fading sky; no repeated inlet or empty starfield.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no person; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "GROUND-LEVEL photograph beside a newborn waterfall pouring through "
            "fresh black rock into a clear bright pool. Warm first sunlight catches "
            "every airborne drop while the last stars fade in a narrow upper strip "
            "of sky. Water, spray and warm stone make creation feel physically "
            "celebratory. No copied inlet, starfield panorama, person, divine figure "
            "or writing; one coherent natural frame."
        ),
    },
    {
        "id": "v2-r181-b14", "out": "s14-listening-to-you-now.jpeg", "seg": "n4",
        "window": "54.638-59.869", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHOT-DIVERSITY", "JOB-WHIRLWIND", "JOB"],
        "narration": "The God who sang the world into being is the same one listening to your questions today.",
        "must_show": "a MEDIUM THREE-QUARTER profile from several paces to Job's LEFT — both relaxed hands are visible open on his knees, his softened face turns toward calm dawn at frame RIGHT, and the spent whirlwind dissolves far behind at LEFT.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no open wounds; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "MEDIUM THREE-QUARTER profile photographed from several paces to Job's "
            "LEFT. Both relaxed hands are fully visible and open on his knees; his "
            "softened face turns toward calm warm dawn at frame RIGHT. Far behind "
            "him at LEFT, the spent whirlwind dissolves into ordinary cloud. The "
            "camera shows his full seated triangle but no foreground boulders and "
            "does not copy b01/b02/b06/b08. No lens gaze, figure of God, writing or "
            "light around his head."
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

# Job's accepted face board is the ONLY attached image. The old place plates are
# deliberately disabled because their composition cloning caused Cameron's current
# complaint. NO Jesus and NO cream in this row.
REFS = {
    "JOB": "CAST-REF-V2/job.jpeg",
}
