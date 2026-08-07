#!/usr/bin/env python3
"""V2 beat map — row 188, build-188-be-ye-therefore-perfect (Matthew 5:44-48 — "Love your
enemies… That ye may be the children of your Father which is in heaven: for he maketh his
sun to rise on the evil and on the good… Be ye therefore perfect, even as your Father
which is in heaven is perfect.").

COVERAGE: 16 pictures over 71.724 s (card_start) = ~4.5 s/picture (lesson 12
movie-coverage). The Sermon on the Mount. Two registers: the HILLSIDE where Jesus teaches
the crowd (the frame), and the VALLEY-FIELDS below where the sun/rain doctrine is shown as
landscape — ONE sun and ONE rain lying equally on the evil and the good. HILLSIDE and
CROWD locks are BYTE-IDENTICAL to build-124 (love-your-enemies) and the rest of the sermon
family (rows 121-124) for cross-video continuity.

=====================================================================
CAMERON COMPLAINT (v2_outline.py 188): "'Maketh' (the archaic version of the modern
word 'makes') is pronounced MAY-kith 0:29." — an AUDIO pronunciation defect in j2.

**RESOLVED — the delivered ElevenLabs audio ALREADY says "maketh" correctly (MAKE-eth).
Audio OK; row handed to the picture runner.** (AUDIO-FIX lane, Machine A `Dev`,
2026-08-07. $0 spent — no re-voice needed.)

WHAT THE PRIOR PARK GOT WRONG: the park diagnosis assumed the edge-tts respell
`"maketh": {"jesus": "mayketh"}` from the global mbm_pronounce SAY map was being applied
to the ElevenLabs render, producing MAY-kith. It is NOT. The real ElevenLabs renderer
`media-production/voice_from_transcripts.py` builds its spoken string with
`eleven_spoken_text()`, which applies ONLY PHRASES + build-local SPOKEN — it BYPASSES the
SAY / SAY_BY_VOICE map by design (that map was measured on Azure voices and would hurt
ElevenLabs). So j2 was rendered from the PLAIN word "maketh", and ElevenLabs reads the
plain word correctly. Cameron's "MAY-kith 0:29" was the PRE-MIGRATION edge-tts cut (edge
DID apply "mayketh"); the 2026-07-23 ElevenLabs re-voice already fixed it.

VERIFICATION (this lane, faster-whisper small.en, beam 5):
  * delivered j2.mp3 (both this v2 dir AND the V1 twin media-production/build-188…/audio)
    -> "...for he MAKETH his son to rise..." — CORRECT.
  * fresh control render of plain "maketh" on the ElevenLabs JESUS voice -> "maketh"
    (identical to delivered).
  * control render of the old "mayketh" respell -> "...for he MAY KETH..." — reproduces
    Cameron's MAY-kith defect. This is what the old edge cut sounded like.

DURABILITY GUARD: make_narration.py now carries a build-local `SPOKEN = {"maketh":
"maketh"}` — build overrides WIN over the global map in BOTH engines (mbm_pronounce
spoken_text priority; eleven_spoken_text overrides), so no future re-render (edge OR
ElevenLabs) can re-introduce "mayketh". The global SAY map is left untouched (other rows).

AUDIO_FROM_V1_SEGMENTS = True (below): assembly rebuilds the track from the build's own
correct segment mp3s at the extract_beats offsets — nothing re-voiced, nothing re-timed.
The 16-beat picture map below is COMPLETE and PASSES --check — the picture runner may
build every still now and assemble on this corrected-and-verified audio.
=====================================================================

SPEAKER LAW (see make_narration.py):
  j1  Matt 5:44  "But I say unto you, Love your enemies…"       JESUS → RED caption
  j2  Matt 5:45  "That ye may be the children of your Father…"  JESUS → RED caption
  j3  Matt 5:48  "Be ye therefore perfect…"                     JESUS → RED caption
Every other segment (n0, n0b, n1, n2, n3, card) is the NARRATOR → white. Only Jesus wears
cream. Red-letter sits on Jesus's face (j1/j2/j3, jesus=True + ref=True).

**HARD GATE — GOD / THE FATHER IS NEVER EMBODIED.** "children of your Father which is in
heaven" (j2), "Be ye… perfect, even as your Father… is perfect" (j3) and every "Father"
in n1/n3 are carried by the warm open SKY, the equal sun and rain, and Jesus's teaching —
NEVER by any figure, face, hand, throne, beam or rays. No dove/triangle/all-seeing-eye/
Trinitarian symbol. The only embodied divine person is Jesus the Son. No halo/ring/
rim-light (drift-word gate — word light as warm sun / morning gold, never a ring around a
head).

CONTENT-CARE: "love your enemies / bless them that curse you" is shown as the crowd
receiving a hard, generous teaching — no violence, no persecutors depicted attacking. The
sun/rain doctrine shows ordinary people (some warm-faced, some sullen) receiving the SAME
light and rain — the equality must be VISIBLE (no brighter field, no favoured side).

TIME-OF-DAY: the hillside in warm late-afternoon gold (matches the sermon family). The
sun/rain doctrine frames are a DELIBERATE separate register — b09 a bright morning SUN
rising over the valley, b10/b11 a silver even RAIN — not a lighting drift.

PLACES / LOCKS:
  HILLSIDE   byte-identical to build-124 / rows 121-124 (same sermon slope). Teaching
             beats.
  CROWD      byte-identical to build-124 (same congregation). Crowd beats.
  VALLEY-FIELDS  (NEW place) the valley of farmed fields below the mount where the sun/
             rain doctrine is shown as landscape — b09, b10, b11, b12.
  Jesus      injected on j-beats + the teaching frames (jesus=True + ref=True + LOCK).
NEW-place promote plan (runner): promote VALLEY-FIELDS from b09 (a NON-Jesus frame).
HILLSIDE may reuse build-124/112's mount plate via v2_stash --wire. Steps in QC.md.

AUDIO: **OK — complaint resolved** (see complaint block above; delivered ElevenLabs j2
already says "maketh" correctly, whisper-verified). AUDIO_FROM_V1_SEGMENTS = True.
card_start = 71.724 s; total with card = 79.773 s.
"""

# LOCKS: HILLSIDE + CROWD are byte-identical cross-video reuses (build-124 / rows
# 121-124). VALLEY-FIELDS is build-local. Setting locks never name a character. Only
# Jesus wears cream; Jesus is injected on jesus=True beats.
LOCKS = {
    "HILLSIDE": (
        "HILLSIDE LOCK: the teaching hillside — a green grassy slope "
        "above the Sea of Galilee, wildflowers in the grass, the "
        "blue lake and far hills below, warm late-afternoon light. "
        "The same slope and lake view throughout."
    ),
    "CROWD": (
        "CROWD LOCK: the listening crowd — ordinary Galileans seated "
        "on the grass: weathered fishermen, mothers with children, "
        "sun-browned farmers, a few elders; varied earth-toned robes "
        "of brown, rust, olive and slate (no cream — only Jesus "
        "wears cream), varied ages and faces, never uniform."
    ),
    "VALLEY-FIELDS": (
        "VALLEY-FIELDS LOCK: the same farmed valley below the mount in every frame — a "
        "broad shallow valley of worked first-century fields and terraces, low dry-stone "
        "walls between plots, a few modest stone farmhouses and olive trees, ordinary "
        "sun-browned country folk at work in the plots. One continuous open sky arches "
        "over the whole valley so that any light or rain lies EQUALLY on every field — no "
        "field brighter or greener than another, no favoured side. Ancient and real; no "
        "modern object; nothing written anywhere. The same valley throughout."
    ),
}

# AUDIO-FIX lane 2026-08-07: rebuild the narration from this build's own correct segment
# mp3s (the "maketh" complaint was already resolved by the ElevenLabs re-voice — see the
# complaint block above). Nothing re-voiced, nothing re-timed.
AUDIO_FROM_V1_SEGMENTS = True

REF = False

BEATS = [
    {
        "id": "v2-r188-b01", "out": "s01-taught-on-the-hillside.jpeg", "seg": "n0",
        "window": "0.000-4.800", "wide": True, "jesus": True, "ref": True,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Jesus sat on the hillside and taught the crowds a kind of love they had never heard before —",
        "must_show": "the ONE establishing wide — Jesus seated on the grassy slope teaching, the crowd settled thick on the grass before him, the blue lake and hills below; warm late-afternoon gold.",
        "must_not_show": "no God or Father figure; no halo, glare or rim-light on Jesus; only Jesus in cream; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing wide of the teaching hillside, camera set behind and to the "
            "side of the seated crowd so their backs are three-quarters to the lens and "
            "they look up the slope toward Jesus, who sits teaching above them — only he "
            "wears the plain cream robe. The blue lake and far hills lie below in warm "
            "late-afternoon gold. Ordinary-sized people on one grassy slope, one head "
            "each; the warm light rests on them, not around their heads; nothing is "
            "written anywhere and no figure stands in for God."
        ),
    },
    {
        "id": "v2-r188-b02", "out": "s02-not-just-friends.jpeg", "seg": "n0",
        "window": "4.800-8.868", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "not just for friends, but for enemies too.",
        "must_show": "a close among the crowd — ordinary listeners' faces turning surprised and uneasy at the idea of a love owed not just to friends but to enemies too.",
        "must_not_show": "no God or Father figure; no Jesus, no cream; no halo, glare or rim-light; no modern object; nothing written; not a cartoon; distinct faces, not twins.",
        "scene": (
            "A close among the seated crowd on the slope: two or three ordinary distinct "
            "listeners — a fisherman, a mother, an elder — their faces turning surprised "
            "and uneasy at the hard idea being taught, a love owed not only to friends "
            "but to enemies too. Warm late-afternoon light. Ordinary-sized, one head "
            "each, gazes up the slope toward the teacher and not to the camera; no one "
            "wears cream; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r188-b03", "out": "s03-love-your-enemies.jpeg", "seg": "j1",
        "window": "8.868-13.500", "wide": False, "jesus": True, "ref": True,
        "locks": ["HILLSIDE"],
        "narration": "But I say unto you, Love your enemies,",
        "must_show": "RED caption (Jesus's own words) — a close on Jesus teaching warmly and firmly, 'Love your enemies', his hands open in earnest appeal.",
        "must_not_show": "no God or Father figure; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus seated on the slope in the warm late-afternoon light, his "
            "hands open in earnest appeal as he teaches — only he wears the plain cream "
            "robe. His face is warm and firm, giving a hard new command. Ordinary-sized, "
            "one head, gaze toward the crowd and not to the camera; warm light on his "
            "face, not around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r188-b04", "out": "s04-bless-and-do-good.jpeg", "seg": "j1",
        "window": "13.500-18.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["HILLSIDE"],
        "narration": "bless them that curse you, do good to them that hate you,",
        "must_show": "RED caption (Jesus's own words) — Jesus pressing the teaching on, an open hand extended outward as if to give good even to those who hate — the outbound direction of blessing clear.",
        "must_not_show": "no God or Father figure; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon; no violence.",
        "scene": (
            "A close on Jesus on the slope, one hand extended outward and open, palm "
            "turned to give — pressing the teaching that blessing and good must go OUT "
            "even to those who curse and hate; only he wears the plain cream robe. Warm "
            "late-afternoon light. Ordinary-sized, one head, gaze and open hand directed "
            "outward toward the crowd and not to the camera; the light rests on him, not "
            "around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r188-b05", "out": "s05-pray-for-them.jpeg", "seg": "j1",
        "window": "18.000-22.149", "wide": False, "jesus": True, "ref": True,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "and pray for them which despitefully use you, and persecute you;",
        "must_show": "RED caption (Jesus's own words) — the hardest turn: Jesus teaching to PRAY for those who mistreat and persecute you, the crowd's faces sobered and stretched by the demand.",
        "must_not_show": "no God or Father figure; no persecutors attacking, no violence; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A two-shot over Jesus's shoulder to the sobered faces of the nearest crowd "
            "as he teaches the hardest turn — to pray even for those who mistreat and "
            "persecute them; only he wears the plain cream robe. The listeners are "
            "stretched and quiet, weighing it. Warm late-afternoon light. Ordinary-sized "
            "people on one slope, one head each, the crowd's gazes on Jesus and not to "
            "the camera; no ring of light around any head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r188-b06", "out": "s06-do-good-and-pray.jpeg", "seg": "n0b",
        "window": "22.149-27.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Do good to the ones who hate you, and pray for the people who use you badly.",
        "must_show": "a crowd listener taking the hard teaching in — an ordinary man on the grass with his hands opening, letting the demand to do good and to pray for enemies settle on him.",
        "must_not_show": "no God or Father figure; no Jesus, no cream; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on an ordinary man seated in the crowd on the slope, his weathered "
            "hands opening on his knees as he lets the hard teaching settle — to do good "
            "to those who hate him and pray for those who use him badly. Warm "
            "late-afternoon light. Ordinary-sized, one head, gaze thoughtful up the slope "
            "and not to the camera; no one wears cream; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r188-b07", "out": "s07-love-them-and-mean-it.jpeg", "seg": "n0b",
        "window": "27.000-32.671", "wide": False, "jesus": True, "ref": True,
        "locks": ["HILLSIDE"],
        "narration": "Not put up with them. Not stay out of their way. Love them, and mean it.",
        "must_show": "Jesus pressing the point home, earnest and warm — not mere tolerance or avoidance, but real love, and meaning it; a strong, sincere gesture of the heart.",
        "must_not_show": "no God or Father figure; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus on the slope, leaning in with an earnest, warm face and a "
            "hand pressed sincerely toward his own heart — pressing home that this is not "
            "mere tolerating or avoiding but real love, and meaning it; only he wears the "
            "plain cream robe. Warm late-afternoon light. Ordinary-sized, one head, gaze "
            "to the crowd and not to the camera; the light on his face, not around his "
            "head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r188-b08", "out": "s08-children-of-your-father.jpeg", "seg": "j2",
        "window": "32.671-37.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["HILLSIDE"],
        "narration": "That ye may be the children of your Father which is in heaven:",
        "must_show": "RED caption (Jesus's own words) — Jesus lifting an open hand toward the warm open sky as he names the goal: that they may be the children of their Father in heaven; the Father unseen, the sky warm and boundless.",
        "must_not_show": "the Father is NOT shown — no God figure, throne, face, hand, beam or rays in the sky; no dove or symbol; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus on the slope lifting an open hand toward the warm, "
            "boundless late-afternoon sky as he names the goal — that they may be the "
            "children of their Father in heaven; only he wears the plain cream robe. The "
            "sky is warm and open and empty of any figure — no one stands in for the "
            "Father. Ordinary-sized, one head, gaze lifted to the open sky and not to the "
            "camera; the light rests on him, not around his head; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r188-b09", "out": "s09-sun-on-evil-and-good.jpeg", "seg": "j2",
        "window": "37.000-41.200", "wide": True, "jesus": False, "ref": False,
        "locks": ["VALLEY-FIELDS"],
        "narration": "for he maketh his sun to rise on the evil and on the good,",
        "must_show": "RED caption (Jesus's words) — the ONE establishing wide of the valley of fields below: a bright morning SUN rising over the whole valley, its light lying EQUALLY on every plot — the evil and the good alike, a warm-faced worker and a sullen one both under the same sun.",
        "must_not_show": "the Father is NOT shown — no God figure in the sun or sky; no field brighter or more favoured than another; no halo, glare or rim-light; no Jesus, no cream; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing wide of the farmed valley below the mount at sunrise, camera "
            "set on the higher slope looking down and across so the workers' backs are "
            "three-quarters to the lens as they face the rising sun — one bright morning "
            "sun climbing over the whole valley and laying its warm light EQUALLY on "
            "every field and terrace, a warm-faced worker in one plot and a sullen, hard "
            "worker in the next both lit the same, neither field favoured. No figure "
            "stands in the sun or sky. Ordinary-sized country folk on the valley floor, "
            "one head each; the sun is in the sky, not ringing any head; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r188-b10", "out": "s10-rain-on-just-and-unjust.jpeg", "seg": "j2",
        "window": "41.200-45.019", "wide": False, "jesus": False, "ref": False,
        "locks": ["VALLEY-FIELDS"],
        "narration": "and sendeth rain on the just and on the unjust.",
        "must_show": "RED caption (Jesus's words) — a silver even RAIN falling over the same valley, wetting the just and the unjust field alike; two neighbouring workers, an open honest one and a grasping one, both caught in the same equal rain.",
        "must_not_show": "the Father is NOT shown — no God figure in the sky; no side drier or wetter, no favoured field; no lightning of judgement; no halo, glare or rim-light; no Jesus, no cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of the same valley under a soft even silver rain that falls equally "
            "over every plot — two neighbouring workers, one open and honest and one "
            "grasping and hard, both caught in the same rain with no field drier or "
            "wetter than the other. Grey but gentle, not a storm of judgement. No figure "
            "stands in the sky. Ordinary-sized country folk on the valley floor, one head "
            "each, faces up into the equal rain and not to the camera; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r188-b11", "out": "s11-kindness-falls-on-everyone.jpeg", "seg": "n1",
        "window": "45.019-48.900", "wide": False, "jesus": False, "ref": False,
        "locks": ["VALLEY-FIELDS"],
        "narration": "The point was simple and hard at once — God's kindness falls on everyone,",
        "must_show": "the equal gift received — several ordinary valley folk of every sort standing in the same warming light and clearing rain, God's kindness plainly falling on everyone alike.",
        "must_not_show": "the Father is NOT shown — no God figure; no favoured person or field; no halo, glare or rim-light; no Jesus, no cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot across the valley as the rain clears and warm light returns, several "
            "ordinary folk of every sort standing among their plots receiving the same "
            "warmth and wet — the kindness falling plainly on everyone alike. No figure "
            "stands in the sky. Ordinary-sized country folk on the valley floor, one head "
            "each, faces to the returning light and not to the camera; no field or person "
            "favoured; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r188-b12", "out": "s12-grateful-and-cruel-alike.jpeg", "seg": "n1",
        "window": "48.900-52.372", "wide": False, "jesus": False, "ref": False,
        "locks": ["VALLEY-FIELDS"],
        "narration": "the grateful and the cruel alike.",
        "must_show": "a tight two-shot in the field — a grateful, open-faced worker and a hard, cruel-faced one standing near each other in the very same light, receiving the same gift though their hearts differ.",
        "must_not_show": "the Father is NOT shown; no God figure; no favoured side; no halo, glare or rim-light; no Jesus, no cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A tight two-shot in the valley field: a grateful, open-faced worker and a "
            "hard, cruel-faced worker stand near one another in the very same warm light, "
            "each receiving the same gift though their hearts plainly differ. Neither is "
            "favoured by the light. Ordinary-sized men on one ground, one head each, "
            "their faces turned to the light and not to the camera; nothing is written "
            "anywhere and no figure stands in the sky."
        ),
    },
    {
        "id": "v2-r188-b13", "out": "s13-set-the-bar.jpeg", "seg": "n2",
        "window": "52.372-57.096", "wide": False, "jesus": True, "ref": True,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Then he set the bar that no one could reach alone, and meant for us to run toward it.",
        "must_show": "back on the hillside, Jesus raising the standard high — a lifted open hand setting a bar no one could reach alone, the crowd leaning in, drawn to run toward it.",
        "must_not_show": "no God or Father figure; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot on the slope of Jesus raising an open hand high as he sets the "
            "standard — a bar no one could reach alone — the nearest crowd leaning in, "
            "drawn and stirred to run toward it; only he wears the plain cream robe. Warm "
            "late-afternoon light. Ordinary-sized people on one slope, one head each, the "
            "crowd's gazes up to Jesus and not to the camera; the light on him, not "
            "around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r188-b14", "out": "s14-be-ye-perfect.jpeg", "seg": "j3",
        "window": "57.096-62.919", "wide": False, "jesus": True, "ref": True,
        "locks": ["HILLSIDE"],
        "narration": "Be ye therefore perfect, even as your Father which is in heaven is perfect.",
        "must_show": "RED caption (Jesus's own words) — the title verse: a strong warm close on Jesus giving the whole aim, 'Be ye therefore perfect, even as your Father which is in heaven is perfect', an open hand toward the boundless sky; the Father unseen.",
        "must_not_show": "the Father is NOT shown — no God figure, throne, face, hand, beam or rays in the sky; no dove or symbol; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A strong warm close on Jesus on the slope, an open hand lifted toward the "
            "boundless late-afternoon sky as he gives the whole aim of the teaching — to "
            "be perfect, even as their Father in heaven is perfect; only he wears the "
            "plain cream robe. The sky is warm, open and empty of any figure — no one "
            "stands in for the Father. Ordinary-sized, one head, gaze steady and warm to "
            "the crowd and not to the camera; the light on his face, not around his head; "
            "nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r188-b15", "out": "s15-not-by-comparison.jpeg", "seg": "n3",
        "window": "62.919-65.266", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Not perfect by comparison with each other.",
        "must_show": "two ordinary crowd members side by side no longer measuring themselves against each other — the sideways comparing look set aside, both turned instead toward the teacher.",
        "must_not_show": "no God or Father figure; no Jesus, no cream; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on two ordinary crowd members seated side by side on the slope, no "
            "longer casting the sideways measuring glance at one another but both turned "
            "the same way up toward the teacher — perfection not by comparison between "
            "them. Warm late-afternoon light. Ordinary-sized, one head each, gazes up the "
            "slope and not to the camera; no one wears cream; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r188-b16", "out": "s16-a-love-with-no-limit.jpeg", "seg": "n3",
        "window": "65.266-71.724", "wide": False, "jesus": True, "ref": True,
        "locks": ["HILLSIDE"],
        "narration": "Perfect by the measure of a Father whose love has no edge, no favor, no limit.",
        "must_show": "the closing image — Jesus with both arms opening wide beneath the vast warm open sky, giving the measure of a Father's love that has no edge, no favour, no limit; the boundless love shown by the open sky, the Father unseen.",
        "must_not_show": "the Father is NOT shown — no God figure, throne, face, hand, beam or rays; no dove or symbol; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closing shot of Jesus on the slope with both arms opening wide beneath the "
            "vast warm open late-afternoon sky, giving the measure of a Father's love "
            "that has no edge, no favour and no limit — the boundlessness carried by the "
            "wide open sky and his open arms; only he wears the plain cream robe. The sky "
            "is empty of any figure — no one stands in for the Father. Ordinary-sized, "
            "one head, gaze warm and open outward and not to the camera; the light on "
            "him, not around his head; nothing is written anywhere."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# HILLSIDE has reusable mount plates in the stash (build-124 / build-112). VALLEY-FIELDS
# is a NEW place — the runner promotes it from b09 (a NON-Jesus frame). Runner runs
# `v2_stash.py --wire build-188-be-ye-therefore-perfect` (--scan first if stale) and
# --takes the suggested HILLSIDE plate. Steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: HILLSIDE/CROWD/VALLEY-FIELDS are text locks; Jesus is injected by the
# assembler on the jesus=True beats. Only Jesus wears cream.
REFS = {
}
