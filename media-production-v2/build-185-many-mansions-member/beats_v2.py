#!/usr/bin/env python3
"""V2 beat map — row 185, build-185-many-mansions-member (John 14:1-3 — the Last Supper
night: "Let not your heart be troubled... In my Father's house are many mansions... I
go to prepare a place for you... I will come again, and receive you unto myself.").

COVERAGE: 14 pictures over 53.175 s (card_start) = ~3.8 s/picture (lesson 12
movie-coverage). Two clearly-distinct places: the UPPER-ROOM at night (Jesus comforting
the disciples — SAME EVENT as rows 89/170, ROOM lock byte-identical) and the
FATHERS-HOUSE vision (the promised home of many dwellings, shown on the NARRATOR beats
so the red-letter stays on Jesus's face). One establishing wide per place (b01 the
room, b05 the Father's house).

=====================================================================
OPEN CAMERON COMPLAINT (v2_outline.py 185): "Old.  That's not the chosen Jesus voice."
DIAGNOSIS (author lane, $0): VALID and OPEN. The Jesus segments jv1/j1/j2 are rendered
through ElevenLabs (audio-eleven.log) but NOT the CHOSEN Jesus voice. Acoustic proof
(median F0, 16 kHz autocorrelation): this build's Jesus ≈ 87-94 Hz, but the APPROVED
row-70 (chosen Jesus voice) ≈ 108 Hz — a ~15-20 Hz gap; meanwhile the NARRATOR matches
almost exactly (185 ≈ 104.6 Hz vs 70 ≈ 103.9 Hz), so it is specifically the JESUS voice
that is wrong, not the narrator. mbm_speakers.py still shows the stale edge-tts
EricNeural trap (the row-70 lesson).
FIX = AUDIO LANE, NOT this lane: re-voice jv1/j1/j2 through the SAME chosen ElevenLabs
Jesus voice as row 70 ("Chris"), keep the captions identical, atempo-match each to its
original duration so NO window moves, place in the V1 dir audio/ and set
AUDIO_FROM_V1_SEGMENTS=True; then the picture runner builds on the corrected audio.
This session CANNOT do it (no ELEVENLABS_API_KEY in this env), so the row is parked
NEEDS-AUDIO and is NOT marked Ready. The beat map below is complete and ready for the
picture runner the moment the audio is corrected.
=====================================================================

AUDIO: currently the WRONG Jesus voice (see above). After the audio lane re-voices
jv1/j1/j2 and sets AUDIO_FROM_V1_SEGMENTS=True, this is a picture-only build. Do NOT
mark Ready until the audio is corrected. card_start = 53.175 s; total with card
= 60.336 s (windows below assume the durations are held by atempo-match — see QC.md).

SPEAKER LAW (see make_narration.py):
  jv1 John 14:1  "Let not your heart be troubled..."          JESUS → RED (on Jesus)
  j1  John 14:2  "In my Father's house are many mansions..."  JESUS → RED (on Jesus)
  j2  John 14:3  "And if I go and prepare a place for you..." JESUS → RED (on Jesus)
Everything else is the NARRATOR (white). Jesus appears (jesus=True + ref=True + LOCK)
on every beat he is in; only he wears cream. Red-letter sits on Jesus's face (row-39):
the "many mansions / Father's house" imagery lives on the NARRATOR beats (b05/b08),
never cutting away from Jesus during his own words.

CONTENT-CARE: warm, comforting milk. NIGHT interior, lamplit (the last night together).
The FATHERS-HOUSE vision shows NO God/Father figure and NO throne — only a radiant,
welcoming home of many dwellings in warm light. No halo/ring/rim-light (drift-word
gate; word the light radiant/luminous/warm, never a ring around a head).

PLACES / LOCKS:
  ROOM          (byte-identical to rows 89/170) the upper room at night (b01-b04, b06,
                b07, b09-b13). Runner promotes from the NON-Jesus b01... but b01 has
                Jesus — so promote ROOM from a clean non-Jesus frame if one exists, or
                keep ROOM text-locked (see QC.md; row 89 shipped ROOM text-only).
  DISCIPLES     (TEXT-LOCK) the eleven disciples reclining, distinct men (b01, b09, b13).
  FATHERS-HOUSE (NEW place, plate) the promised home of many dwellings (b05, b08, b14).
                Runner promotes from the NON-Jesus b05.
NEW-place promote plan (runner): FATHERS-HOUSE from b05 (NON-Jesus). ROOM: promote from
a non-Jesus frame or keep text-only as row 89 did (never promote a Jesus-bearing frame,
lesson 11). Steps in QC.md.
"""

# LOCKS: ROOM byte-identical to rows 89/170 (cross-video same upper room). Jesus is
# injected by the assembler on jesus=True beats; only Jesus wears cream.
LOCKS = {
    "ROOM": (
        "ROOM LOCK: the upper room — a large furnished chamber up an outside stair: a "
        "LOW U-SHAPED TABLE with cushions where diners recline, clay oil lamps on the "
        "table and in wall niches, plastered walls, one shuttered window open on the "
        "night. The same table, lamps and walls throughout."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the eleven disciples of Jesus reclining at the low table — "
        "distinct first-century Galilean Jewish men of varied ages, builds, hair and "
        "beards, in plain earth-toned and muted-coloured robes (NEVER cream — only "
        "Jesus wears cream). Real, individual faces, no twins or cloned features; their "
        "faces move from troubled to comforted as Jesus speaks. Ordinary-sized, on the "
        "cushions around the same table."
    ),
    "FATHERS-HOUSE": (
        "FATHERS-HOUSE LOCK: the same vision-home in every frame — the promised house "
        "of the Father: a vast, warm, welcoming dwelling of many rooms and open "
        "doorways, chamber beyond chamber filled with soft radiant golden light, room "
        "prepared for everyone, peaceful and homelike. There is NO God or Father "
        "figure, NO throne and NO divine being of any kind; it is a HOME, not a "
        "temple-court of judgment. Reverent, spacious, glad. Nothing is written "
        "anywhere. The same welcoming house of many dwellings and warm light "
        "throughout."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r185-b01", "out": "s01-the-last-night-together.jpeg", "seg": "n0",
        "window": "0.400-6.752", "wide": True, "jesus": True, "ref": True,
        "locks": ["ROOM", "DISCIPLES"],
        "narration": "On the night before everything changed, Jesus sat with his disciples and told them not to let their hearts be troubled.",
        "must_show": "the ONE establishing wide of the lamplit upper room at night — Jesus reclining with his disciples around the low U-shaped table, turning to them with a calm, tender face to tell their troubled hearts to be still; only Jesus in cream.",
        "must_not_show": "no God figure; no one but Jesus in cream; no halo, ring, rim-light or glow around Jesus; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "A wide of the lamplit upper room at night seen from behind and to the side "
            "of the disciples, their backs three-quarters to the camera as they recline "
            "on the cushions around the low U-shaped table, facing Jesus. Jesus, in his "
            "plain cream robe, leans toward them with a calm, tender face, quieting "
            "their troubled hearts on the last night together. Clay lamps warm the "
            "plastered walls; the night is at the shuttered window. Camera behind and "
            "beside the disciples looking past them to Jesus; ordinary-sized men on the "
            "cushions; the warm lamplight rests on them, not around their heads."
        ),
    },
    {
        "id": "v2-r185-b02", "out": "s02-let-not-your-heart-be-troubled.jpeg", "seg": "jv1",
        "window": "6.752-10.200", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM"],
        "narration": "Let not your heart be troubled:",
        "must_show": "RED caption (Jesus's own words) — a close on Jesus in the lamplight speaking gently and steadily to the disciples: 'Let not your heart be troubled.' Warm, reassuring; only he in cream.",
        "must_not_show": "no God figure; no one but Jesus in cream; no halo, ring, rim-light or glow; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A warm close on Jesus in the lamplit room, his cream robe soft in the "
            "warm lamplight, his face gentle and steady as he tells the disciples not to "
            "let their hearts be troubled. Kind, unhurried, comforting. Ordinary-sized, "
            "one head, gaze to his disciples and not to the camera; the lamplight rests "
            "on his face, not around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r185-b03", "out": "s03-believe-also-in-me.jpeg", "seg": "jv1",
        "window": "10.200-13.559", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM"],
        "narration": "ye believe in God, believe also in me.",
        "must_show": "RED caption (Jesus's own words) — Jesus continuing, an open hand toward himself as he says 'ye believe in God, believe also in me' — inviting their trust; warm and certain, only he in cream.",
        "must_not_show": "no God figure; no one but Jesus in cream; no halo, ring, rim-light or glow; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus in the lamplit room, one open hand resting toward his own "
            "chest as he tells them that as they believe in God, so they may believe "
            "also in him. His face is warm and certain, inviting their trust. "
            "Ordinary-sized, one head, gaze to his disciples and not to the camera; the "
            "warm light rests on him, not around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r185-b04", "out": "s04-not-to-leave-them-behind.jpeg", "seg": "n1",
        "window": "13.559-17.260", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM", "DISCIPLES"],
        "narration": "He was going somewhere — but not to leave them behind.",
        "must_show": "Jesus reassuring the disciples that though he is going away, he is not abandoning them — a warm two-shot of Jesus with a steadying hand toward a disciple, his face promising he will not leave them behind.",
        "must_not_show": "no God figure; no one but Jesus in cream; no halo, ring, rim-light or glow; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A warm two-shot in the lamplit room: Jesus, in his cream robe, lays a "
            "steadying hand toward a disciple beside him, his face promising that "
            "though he must go away he will not leave them behind. The disciple's "
            "worry begins to ease. Ordinary-sized men, two heads, on the cushions; the "
            "lamplight rests on them, not around their heads; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r185-b05", "out": "s05-going-to-get-a-place-ready.jpeg", "seg": "n1",
        "window": "17.260-19.811", "wide": True, "jesus": False, "ref": False,
        "locks": ["FATHERS-HOUSE"],
        "narration": "He was going to get a place ready.",
        "must_show": "the ONE establishing wide of the Father's house — a vast, warm, welcoming home of many rooms and open doorways filled with soft radiant golden light, a place being made ready to receive them.",
        "must_not_show": "no God or Father figure; no throne; no divine being; no Jesus, no cream (vision of the place, no person); no halo, ring or rim-light; no modern object; nothing written; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "A vast establishing wide looking down the length of the Father's house, the "
            "camera moving inward away from the entrance through chamber beyond chamber "
            "of warm radiant golden light, many open doorways and prepared rooms "
            "opening off a long welcoming hall — a home being made ready to receive "
            "them. Spacious, warm, peaceful, empty of any figure so no one's back or "
            "face is toward the lens. Nothing is written anywhere and no ring of light "
            "rings anything."
        ),
    },
    {
        "id": "v2-r185-b06", "out": "s06-many-mansions.jpeg", "seg": "j1",
        "window": "19.811-24.790", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM"],
        "narration": "In my Father's house are many mansions: if it were not so, I would have told you.",
        "must_show": "RED caption (Jesus's own words) — Jesus in the lamplit room telling them of his Father's house of many mansions, an open hand lifted in gentle assurance ('if it were not so, I would have told you'); warm and truthful, only he in cream.",
        "must_not_show": "no God figure; no one but Jesus in cream; no halo, ring, rim-light or glow; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus in the lamplit room, one hand lifted open in gentle "
            "assurance as he tells the disciples that in his Father's house are many "
            "dwellings, and that if it were not so he would have told them. His face is "
            "warm, honest and certain. Ordinary-sized, one head, gaze to his disciples "
            "and not to the camera; the lamplight rests on him, not around his head; "
            "nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r185-b07", "out": "s07-prepare-a-place-for-you.jpeg", "seg": "j1",
        "window": "24.790-28.481", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM"],
        "narration": "I go to prepare a place for you.",
        "must_show": "RED caption (Jesus's own words) — a close on Jesus promising 'I go to prepare a place for you', his hand over his heart or open toward them, tender and sure; only he in cream.",
        "must_not_show": "no God figure; no one but Jesus in cream; no halo, ring, rim-light or glow; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A tender close on Jesus in the lamplit room, one hand at his heart, "
            "promising the disciples that he goes to prepare a place for them. His face "
            "is warm and sure, full of quiet love. Ordinary-sized, one head, gaze to "
            "his disciples and not to the camera; the lamplight rests on him, not "
            "around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r185-b08", "out": "s08-room-for-everyone.jpeg", "seg": "n2",
        "window": "28.481-30.430", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHERS-HOUSE"],
        "narration": "A house with room for everyone.",
        "must_show": "the Father's house of many dwellings, plainly with room for everyone — many warm-lit chambers and open doorways ready and waiting, generous and welcoming.",
        "must_not_show": "no God or Father figure; no throne; no divine being; no Jesus, no cream (no person); no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A warm view into the Father's house showing many prepared chambers and "
            "open doorways opening one beyond another in soft radiant golden light — "
            "plainly a home with room for everyone, generous and waiting. Peaceful, "
            "spacious, glad; empty of any figure. Nothing is written anywhere and no "
            "ring of light rings anything."
        ),
    },
    {
        "id": "v2-r185-b09", "out": "s09-he-said-it-plainly.jpeg", "seg": "n2",
        "window": "30.430-35.399", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM", "DISCIPLES"],
        "narration": "He said it plainly — if it were not true, he would have told them.",
        "must_show": "Jesus's plain, honest face to the disciples — a two-shot of Jesus telling them the truth simply and openly, the disciples looking to him and beginning to trust it; only Jesus in cream.",
        "must_not_show": "no God figure; no one but Jesus in cream; no halo, ring, rim-light or glow; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A warm two-shot in the lamplit room of Jesus speaking plainly and openly "
            "to a disciple across the table, his honest face saying the thing simply — "
            "that if it were not true he would have told them. The disciple looks to "
            "him and begins to trust it. Ordinary-sized men, two heads, on the "
            "cushions; the lamplight rests on them, not around their heads; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r185-b10", "out": "s10-if-i-go-and-prepare.jpeg", "seg": "j2",
        "window": "35.399-39.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM"],
        "narration": "And if I go and prepare a place for you,",
        "must_show": "RED caption (Jesus's own words) — Jesus continuing the promise, 'if I go and prepare a place for you', warm and steady in the lamplight; only he in cream.",
        "must_not_show": "no God figure; no one but Jesus in cream; no halo, ring, rim-light or glow; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus in the lamplit room continuing his promise — that if he "
            "goes and prepares a place for them — his face warm and steady, one hand "
            "open in tender assurance. Ordinary-sized, one head, gaze to his disciples "
            "and not to the camera; the lamplight rests on him, not around his head; "
            "nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r185-b11", "out": "s11-i-will-come-again.jpeg", "seg": "j2",
        "window": "39.000-43.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM"],
        "narration": "I will come again, and receive you unto myself;",
        "must_show": "RED caption (Jesus's own words) — Jesus promising 'I will come again, and receive you unto myself', both hands opening toward the disciples to gather them in; warm and sure, only he in cream.",
        "must_not_show": "no God figure; no one but Jesus in cream; no halo, ring, rim-light or glow; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus in the lamplit room, both hands opening warmly toward the "
            "disciples as if to gather them in, promising that he will come again and "
            "receive them unto himself. His face is sure and full of love. "
            "Ordinary-sized, one head, gaze to his disciples and not to the camera; the "
            "lamplight rests on him, not around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r185-b12", "out": "s12-where-i-am-ye-may-be.jpeg", "seg": "j2",
        "window": "43.000-46.596", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM", "DISCIPLES"],
        "narration": "that where I am, there ye may be also.",
        "must_show": "RED caption (Jesus's own words) — Jesus finishing the promise, 'that where I am, there ye may be also', looking around the whole table at his disciples with deep love; only he in cream.",
        "must_not_show": "no God figure; no one but Jesus in cream; no halo, ring, rim-light or glow; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus in the lamplit room, his gaze moving warmly around the "
            "table over all his disciples as he finishes the promise — that where he "
            "is, there they may be also. Deep love and certainty on his face; the "
            "disciples' faces are comforted around him. Ordinary-sized men on the "
            "cushions; the lamplight rests on them, not around their heads; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r185-b13", "out": "s13-not-a-far-off-maybe.jpeg", "seg": "n3a",
        "window": "46.596-49.701", "wide": False, "jesus": True, "ref": True,
        "locks": ["ROOM", "DISCIPLES"],
        "narration": "He was not describing a far-off maybe.",
        "must_show": "the disciples reassured and Jesus present and certain — a warm two-shot where the disciples' faces have settled into peace, Jesus near and sure; this is no far-off maybe but a present promise; only Jesus in cream.",
        "must_not_show": "no God figure; no one but Jesus in cream; no halo, ring, rim-light or glow; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A warm two-shot in the lamplit room: the disciples' faces have settled "
            "into peace as Jesus sits near and certain among them — this is no far-off "
            "maybe but a present, sure promise. Quiet and comforted. Ordinary-sized "
            "men, two heads, on the cushions; the lamplight rests on them, not around "
            "their heads; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r185-b14", "out": "s14-carry-them-home.jpeg", "seg": "n3b",
        "window": "49.701-53.175", "wide": False, "jesus": True, "ref": True,
        "locks": ["FATHERS-HOUSE"],
        "narration": "He was promising to come back and carry them home himself.",
        "must_show": "the promise brought home — Jesus at the threshold of the warm Father's house, an open welcoming hand reaching back, ready to come again and carry them home himself; the radiant home of many dwellings behind him, only he in cream.",
        "must_not_show": "no God or Father figure; no throne; no one but Jesus in cream; no halo, ring, rim-light or glow around Jesus; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A warm close on Jesus, in his cream robe, standing at the threshold of the "
            "Father's house with an open welcoming hand reaching back toward those he "
            "loves — ready to come again and carry them home himself — the radiant "
            "home of many warm-lit dwellings opening behind him. Tender, homeward, "
            "glad. Ordinary-sized, one head, hand reaching back and gaze warm, not to "
            "the camera; the warm light rests on him, not around his head; nothing is "
            "written anywhere."
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

# No image REFS: ROOM is byte-identical to rows 89/170; DISCIPLES and FATHERS-HOUSE are
# text locks. Jesus is injected by the assembler on jesus=True beats. Only Jesus wears
# cream.
REFS = {
}
