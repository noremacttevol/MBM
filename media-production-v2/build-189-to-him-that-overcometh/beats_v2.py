#!/usr/bin/env python3
"""V2 beat map — row 189, build-189-to-him-that-overcometh (Revelation 3:20-21 — the
risen Christ's letter to Laodicea: "Behold, I stand at the door, and knock: if any man
hear my voice, and open the door, I will come in to him, and will sup with him, and he
with me. To him that overcometh will I grant to sit with me in my throne, even as I also
overcame, and am set down with my Father in his throne.").

COVERAGE: 12 pictures over 46.241 s (card_start) = ~3.85 s/picture (lesson 12
movie-coverage). Three registers, cut like a short film:
  DOOR-NIGHT     the knock at the drowsy house (n0, j1 open, n1) — exterior night.
  LAMPLIT-ROOM   the hearing, the latch, the offered supper (j1 mid, n2) — warm interior.
  THRONE-GLORY   the shared throne (j2, n3) — a radiant heavenly hall.
No group portraits — an establishing NON-Jesus wide of the door (b01), then singles,
two-shots and inserts (a hand at the latch, the offered table, the empty seat) through
the exchange. ONE recurring human, the OVERCOMER — the "any man" the letter addresses:
he hears (b04), his hand lifts the latch (b07), Christ offers him supper (b05), and he
is the one who overcomes and shares the throne (b11/b12). Same face throughout.

=====================================================================
OPEN CAMERON COMPLAINT (v2_outline.py 189): "Pronounce overcometh as OH-vur-kuh-muhth
0:38." This is an AUDIO defect and is NOT closed by this picture map. ROOT CAUSE +
PARK: the SPOKEN respell {"overcometh": "overcummeth"} is ALREADY in make_narration.py
(added 2026-07-29 09:44) BUT the delivered j2.mp3 was rendered 2026-07-28 16:11 — the
day BEFORE the fix — so the respell has never actually been rendered into audio. The
segment is ElevenLabs (44100/128k), and its median F0 ≈ 90.7 Hz matches the OLD/wrong
Jesus voice that row 185 diagnosed (chosen ≈ 105-118 Hz), so j1/j2 likely also carry the
stale Jesus voice. Both are audio-lane work with engine hazards (mbm_speakers still shows
stale edge-tts EricNeural for JESUS, so a naive make_narration re-run would SWAP Jesus to
the wrong engine — the rows-50/51/70 trap). Row PARKED NEEDS-AUDIO; do NOT set Ready
until audio is corrected. Full spec in QC.md COMPLAINT LEDGER.
=====================================================================

SPEAKER LAW (see make_narration.py — Revelation red-letters Christ's explicit sayings;
a red-letter KJV prints all of chapter 3 red):
  j1  Rev 3:20  "Behold, I stand at the door, and knock..."      JESUS → RED caption
  j2  Rev 3:21  "To him that overcometh will I grant to sit..."   JESUS → RED caption
Every other segment (n0, n1, n2, n3, card) is the NARRATOR → white. Both j1 and j2 are
the risen Christ dictating to Laodicea, so both are genuinely red and sit on Jesus's own
face. Only Jesus wears cream.

**HARD GATE — GOD / THE FATHER IS NEVER EMBODIED.** j2's "and am set down with my Father
in his throne" is carried by CHRIST himself (embodied, the Son) beside a throne of pure
radiant white light — NEVER by any figure, face, hand, throne-occupant, beam-as-person,
dove, triangle, all-seeing eye or Trinitarian symbol standing in for the Father. The only
embodied divine person is Jesus the Son. No halo, ring or rim-light around anyone
(drift-word gate — word every light as radiant / luminous / warm, never a ring around a
head).

CONTENT-CARE: the knock is gentle — "not a storm, just a knock." No force, no breaking
the door, no fear. Christ waits to be invited; the whole build turns on a latch the
overcomer lifts himself. The throne is glory and welcome, not an earthly empire's
gold-and-jewels excess; the shared seat is grace, not a reward earned by being flawless.

TIME-OF-DAY: DOOR-NIGHT and LAMPLIT-ROOM are a quiet night lit by a low oil lamp
(warm, close, drowsy). THRONE-GLORY is a radiant heavenly hall of brilliant warm-white
light — reverent and luminous like the Latter-day Saint Gospel Art Book, but with NO
divine figure but Christ.

PLACES / LOCKS (all three are NEW build-local places — no committed plate yet):
  DOOR-NIGHT     the exterior of the drowsy house at night; runner PROMOTES from b01
                 (NON-Jesus). b02/b03/b06 reuse it.
  LAMPLIT-ROOM   the warm interior; runner PROMOTES from b04 (NON-Jesus — the man inside
                 hearing, Jesus still outside the door). b05/b07/b08 reuse it.
  THRONE-GLORY   the radiant heavenly hall; runner PROMOTES from b11 (NON-Jesus — the
                 overcomer before the empty shared seat). b09/b10/b12 reuse it.
  OVERCOMER      build-local person lock — the ordinary believer the letter addresses
                 (b04/b05/b07/b11/b12); never cream/white.
  Jesus          injected by the assembler on every jesus=True beat (ref=True + LOCK);
                 only he wears cream.

AUDIO: PARKED NEEDS-AUDIO (see complaint block). Once the audio lane re-voices j2 (and,
if confirmed, restores the chosen Jesus voice on j1/j2) it must set
AUDIO_FROM_V1_SEGMENTS = True so v2_assemble rebuilds from the corrected segments.
card_start = 46.241 s.
"""

# NEW build-local places are declared as text LOCKS here; PLACE_REFS stays empty and the
# runner promotes each place's plate from its first NON-Jesus frame (see QC.md). Setting
# locks never name a character. Only Jesus wears cream; Jesus is injected on jesus=True
# beats.
LOCKS = {
    "DOOR-NIGHT": (
        "DOOR-NIGHT LOCK: the same place in every frame — the outside of a modest "
        "first-century stone house at night. A plain heavy timber door set in a stone "
        "frame on a low worn threshold, warm lamplight leaking thin around its edges "
        "from within, a quiet dark street and shuttered wall to either side, a deep "
        "blue-black night sky above. The house reads settled and comfortable, its "
        "household drowsy and half-asleep behind the shut door. Ancient and real; no "
        "modern object anywhere, and nothing legible or rendered is written on any "
        "surface. The same door, threshold and quiet night throughout."
    ),
    "LAMPLIT-ROOM": (
        "LAMPLIT-ROOM LOCK: the same place in every frame — the warm interior of that "
        "same modest house at night: plain lime-plastered stone walls, a low wooden "
        "table, a single small clay oil lamp casting a soft close light, woven floor "
        "mats and simple cushions, and the inner face of the shut timber door with its "
        "wooden latch. Comfortable, lived-in and drowsy. Ancient and spare; no modern "
        "object anywhere, and nothing legible or rendered is written on any surface. "
        "The same warm lamplit room throughout."
    ),
    "THRONE-GLORY": (
        "THRONE-GLORY LOCK: the same place in every frame — a radiant heavenly hall of "
        "brilliant warm-white light, reverent and luminous like Latter-day Saint gospel "
        "art. A single shining throne of light stands on a broad low step, with an open "
        "place beside it; the air itself is softly luminous so no hard shadows fall. It reads "
        "as glory and welcome, NOT an earthly palace or an empire's gold-and-jewels "
        "excess — no crowns of state, no courtiers, no banners. No figure of God or the "
        "Father anywhere. No modern object, and nothing legible or rendered is written "
        "on any surface. The same radiant hall throughout. The brilliance fills the "
        "room and rests on the people; it is never a ring or rim of light around anyone's "
        "head."
    ),
    "OVERCOMER": (
        "OVERCOMER LOCK: the same man in every frame he appears — the ordinary believer "
        "the letter is written to, about thirty-five, warm olive-brown skin, short dark "
        "hair, a neat short dark beard, keen tired hopeful dark eyes, in a plain undyed "
        "brown-grey wool tunic and mantle (never cream, never white). A humble, "
        "unpolished working man — weary but awake, longing rather than proud, plainly "
        "not flawless. The same face, beard, build and clothing throughout."
    ),
}

# AUDIO-FIX lane 2026-08-07 (Machine A `Dev`): j1 + j2 re-voiced through the CHOSEN
# ElevenLabs Jesus "Chris" (iP95p4xoKVk53GoZ742B — Cameron-approved rows 50/51/70/185),
# j2 with the committed `overcummeth` respell (target OH-vur-kuh-muhth). Pitch-preserving
# atempo-matched to the original V1-twin durations (j1 11.598 s, j2 8.202 s; Δ ≤ 26 ms =
# one MP3 frame) so no window moves. Narrator segments byte-identical. Originals in
# media-production/build-189…/audio-oldvoice-backup/. Rebuild reads the corrected V1-twin
# segments:
AUDIO_FROM_V1_SEGMENTS = True

REF = False

BEATS = [
    {
        "id": "v2-r189-b01", "out": "s01-the-drowsy-house.jpeg", "seg": "n0",
        "window": "0.000-3.900", "wide": True, "jesus": False, "ref": False,
        "locks": ["DOOR-NIGHT"],
        "narration": "To a church that had grown comfortable and half-asleep,",
        "must_show": "the ONE establishing wide, NON-Jesus (the DOOR-NIGHT plate) — the outside of a modest, settled house at night, its plain timber door shut, warm lamplight leaking thin around the edges, the household plainly comfortable and half-asleep within; a still, quiet street.",
        "must_not_show": "no Jesus and no person at the door yet; no God or Father figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing wide of a modest first-century stone house at night, camera "
            "set in the quiet dark street a little back from the shut timber door. Warm "
            "lamplight leaks thin around the door's edges; the household is settled, "
            "comfortable and half-asleep behind it. Deep blue-black night sky, shuttered "
            "walls to either side. No one stands at the door yet. Ancient and real; warm "
            "light rests low around the doorway, not around anyone's head; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r189-b02", "out": "s02-the-gentle-knock.jpeg", "seg": "n0",
        "window": "3.900-7.703", "wide": False, "jesus": True, "ref": True,
        "locks": ["DOOR-NIGHT"],
        "narration": "Jesus sent a knock at the door — not a storm, just a knock.",
        "must_show": "Jesus arrived at the shut door in the night, raising a hand to knock gently on the timber — quiet and patient, not a storm, just a knock; favour Jesus and his hand at the wood.",
        "must_not_show": "no forcing or breaking the door; no God or Father figure; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A medium on Jesus standing at the shut timber door in the night, one hand "
            "raised to knock gently on the wood — his knock quiet and patient, not a "
            "storm. Only he wears the plain cream robe. Warm lamplight from within edges "
            "the door beside him. Ordinary-sized, one head, gaze on the door and not to "
            "the camera; the warm light rests on his hand and face, not around his head; "
            "nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r189-b03", "out": "s03-i-stand-and-knock.jpeg", "seg": "j1",
        "window": "7.703-11.600", "wide": False, "jesus": True, "ref": True,
        "locks": ["DOOR-NIGHT"],
        "narration": "Behold, I stand at the door, and knock:",
        "must_show": "RED caption (Jesus's own words) — a closer shot of Jesus standing steady at the door in the night, knocking again, patient and unhurried; his whole bearing is 'I stand at the door, and knock.'",
        "must_not_show": "no God or Father figure; no forcing the door; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closer shot of Jesus standing at the shut door in the night, knocking "
            "again — steady, patient and unhurried, waiting on the threshold. Only he "
            "wears the plain cream robe. Warm lamplight edges the door. Ordinary-sized, "
            "one head, gaze on the door and not to the camera; warm light on his face, "
            "not around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r189-b04", "out": "s04-any-man-hear-his-voice.jpeg", "seg": "j1",
        "window": "11.600-15.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAMPLIT-ROOM", "OVERCOMER"],
        "narration": "if any man hear my voice, and open the door,",
        "must_show": "RED caption (Jesus's words) — the LAMPLIT-ROOM plate frame, NON-Jesus: inside the warm room the overcomer stirs from his drowse, head lifting toward the knock at the door, one hand starting to move toward the wooden latch — 'if any man hear my voice, and open the door.'",
        "must_not_show": "Jesus is NOT shown here — he is still outside the shut door; no God or Father figure; no halo, glare or rim-light; the overcomer never wears cream or white; no modern object; nothing written; not a cartoon.",
        "scene": (
            "Inside the warm lamplit room at night, a single small oil lamp burning low. "
            "The overcomer — an ordinary weary working man in plain brown-grey wool "
            "(never cream) — has been drowsing; now his head lifts toward the knock on the "
            "shut timber door across the room, and one hand begins to move toward the "
            "wooden latch. Jesus is not in the room; he is still outside the door. "
            "Ordinary-sized, one head, gaze toward the door and not to the camera; the "
            "lamp's warm light rests on him, not around his head; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r189-b05", "out": "s05-sup-with-him.jpeg", "seg": "j1",
        "window": "15.500-19.471", "wide": False, "jesus": True, "ref": True,
        "locks": ["LAMPLIT-ROOM", "OVERCOMER"],
        "narration": "I will come in to him, and will sup with him, and he with me.",
        "must_show": "RED caption (Jesus's words) — the promised supper: the door now open, Jesus stepping in and offering to share the small lamplit table with the overcomer, a simple meal of bread and a cup between them — 'I will come in to him, and will sup with him, and he with me.'",
        "must_not_show": "no God or Father figure; no feast or empire's excess (a plain shared meal); no halo, glare or rim-light; only Jesus in cream; the overcomer never in cream or white; no modern object; nothing written; not a cartoon.",
        "scene": (
            "Inside the warm lamplit room, the timber door now open to the night. Jesus "
            "steps in and gestures warmly to the low table where a simple meal waits — "
            "plain bread and a clay cup — offering to share it with the overcomer, who "
            "rises to meet him. Only Jesus wears the plain cream robe; the overcomer is "
            "in his brown-grey wool. A small oil lamp lights them both. Ordinary-sized "
            "men on one floor, one head each, gazes on each other and the table and not to "
            "the camera; warm lamplight on them, not around their heads; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r189-b06", "out": "s06-he-does-not-break-the-door.jpeg", "seg": "n1",
        "window": "19.471-23.306", "wide": False, "jesus": True, "ref": True,
        "locks": ["DOOR-NIGHT"],
        "narration": "He does not break the door. He waits to be invited in.",
        "must_show": "an insert of Jesus's open hand resting gently against the shut timber door in the night — not pushing, not forcing; he waits to be invited in. Quiet patience, the latch on the inside untouched by him.",
        "must_not_show": "no forcing, pushing or breaking the door; no God or Father figure; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A tight insert favouring Jesus's open hand resting gently, flat and "
            "unforcing, against the outside of the shut timber door in the night — he "
            "does not push or break it but waits to be invited in. Only the edge of his "
            "cream sleeve shows. Warm lamplight leaks thin around the door. The hand is "
            "patient and still; warm light on the wood and his hand, not around any head; "
            "nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r189-b07", "out": "s07-the-hand-on-the-latch.jpeg", "seg": "n2",
        "window": "23.306-26.300", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAMPLIT-ROOM", "OVERCOMER"],
        "narration": "And to the one who opens, who keeps opening,",
        "must_show": "an insert from inside — the overcomer's own hand lifting the wooden latch of the door, the door beginning to swing inward, a strip of night-cool dark widening at the edge; 'the one who opens, who keeps opening.'",
        "must_not_show": "Jesus's face not shown in this insert (his cream form may be a soft blur beyond the opening gap); no God or Father figure; no halo, glare or rim-light; the overcomer never in cream or white; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A tight insert from inside the lamplit room: the overcomer's weathered hand "
            "lifts the wooden latch and the timber door begins to swing inward, a strip "
            "of the night widening at its edge. Focus on the hand and the latch. Warm "
            "lamplight behind, cool dark ahead. Ordinary-sized hand, natural grip; the "
            "warm light rests on the wood and the hand, not around any head; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r189-b08", "out": "s08-a-seat-no-empire-can-give.jpeg", "seg": "n2",
        "window": "26.300-29.117", "wide": False, "jesus": True, "ref": True,
        "locks": ["LAMPLIT-ROOM"],
        "narration": "he promises a seat no empire can give.",
        "must_show": "a close on Jesus at the now-open threshold, turned warmly toward the one who opened, his face full of promise — he pledges a seat no empire could ever give; the warmth of a promise, not a transaction.",
        "must_not_show": "no God or Father figure; no crown, throne of state or empire's finery here; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus standing warm and glad at the now-open threshold of the "
            "lamplit room, turned toward the one who opened, his face full of quiet "
            "promise as he pledges a seat no earthly empire could give. Only he wears the "
            "plain cream robe. Warm lamplight and the night beyond. Ordinary-sized, one "
            "head, gaze warm toward the overcomer and not to the camera; warm light on "
            "his face, not around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r189-b09", "out": "s09-sit-with-me-in-my-throne.jpeg", "seg": "j2",
        "window": "29.117-34.500", "wide": False, "jesus": True, "ref": True,
        "locks": ["THRONE-GLORY"],
        "narration": "To him that overcometh will I grant to sit with me in my throne,",
        "must_show": "RED caption (Jesus's words) — the risen glorified Christ in the radiant heavenly hall, seated by the shining throne of light and extending an open hand toward the open place beside him, granting the overcomer to sit with him — 'sit with me in my throne.'",
        "must_not_show": "no God or Father figure; no earthly empire's crown/jewels/courtiers; no halo, ring or rim-light around his head; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "In the radiant heavenly hall of brilliant warm-white light, the risen Christ "
            "sits by a single shining throne of light on a broad low step, an open place "
            "beside him, and extends an open hand toward that place — granting the "
            "overcomer to sit with him. Only he wears the plain cream robe. The whole "
            "room is filled with light so there are no hard shadows; the light fills the hall and rests "
            "on him — it is never a ring around his head. Ordinary-sized, one head, gaze "
            "warm and outward and not to the camera; nothing is written anywhere; no "
            "figure of God appears."
        ),
    },
    {
        "id": "v2-r189-b10", "out": "s10-set-down-with-my-father.jpeg", "seg": "j2",
        "window": "34.500-39.952", "wide": False, "jesus": True, "ref": True,
        "locks": ["THRONE-GLORY"],
        "narration": "even as I also overcame, and am set down with my Father in his throne.",
        "must_show": "RED caption (Jesus's words) — Christ himself now seated in glory on the throne of light, at rest and victorious, as one who has himself overcome; beside him a second throne is pure radiant white light with NO one seated there — the Father's place, unshown.",
        "must_not_show": "THE FATHER IS NOT SHOWN — no God figure, face, hand, occupant, beam-as-person, dove, triangle or symbol on or above the second throne (it is pure light only); no halo, ring or rim-light around Christ's head; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "In the radiant hall, Christ himself is now seated in glory on the shining "
            "throne of light, at rest and victorious as one who has overcome. Beside him "
            "a second throne is pure brilliant white light with no one seated on it and "
            "no figure above it — the Father's place, left unshown, carried by radiance "
            "alone. Only Christ wears the plain cream robe. The light fills the hall and "
            "rests on him, never a ring around his head. Ordinary-sized, one head, gaze "
            "calm and forward and not to the camera; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r189-b11", "out": "s11-not-by-being-flawless.jpeg", "seg": "n3",
        "window": "39.952-43.300", "wide": False, "jesus": False, "ref": False,
        "locks": ["THRONE-GLORY", "OVERCOMER"],
        "narration": "The one who overcomes doesn't earn a throne by being flawless.",
        "must_show": "the THRONE-GLORY plate frame, NON-Jesus — the ordinary overcomer standing humbly before the shining throne and its open place, plainly weary and unpolished, not flawless, received by grace rather than by earning; the open seat waits for him.",
        "must_not_show": "Jesus not shown in this frame; no God or Father figure; no halo, ring or rim-light; the overcomer never in cream or white; no modern object; nothing written; not a cartoon.",
        "scene": (
            "In the radiant heavenly hall, the overcomer — the same ordinary, weary, "
            "unpolished man in plain brown-grey wool (never cream) — stands humbly before "
            "the shining throne of light and its open place, plainly not flawless, "
            "received by grace rather than by earning; the open seat waits for him. Jesus "
            "is not in this frame. The room's brilliance rests on the man, never a ring "
            "around his head. Ordinary-sized, one head, gaze up toward the throne and not "
            "to the camera; nothing is written anywhere; no figure of God appears."
        ),
    },
    {
        "id": "v2-r189-b12", "out": "s12-shares-what-christ-won.jpeg", "seg": "n3",
        "window": "43.300-46.241", "wide": False, "jesus": True, "ref": True,
        "locks": ["THRONE-GLORY", "OVERCOMER"],
        "narration": "He shares the one Christ already won.",
        "must_show": "the closing image — the overcomer now seated beside Christ on the shared throne of light, side by side in the radiant hall, sharing the victory Christ already won; welcome and belonging, not a rival glory.",
        "must_not_show": "no God or Father figure; no second rival throne of state; no halo, ring or rim-light; only Jesus in cream, the overcomer in his brown-grey wool; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closing two-shot in the radiant hall: the overcomer is now seated beside "
            "Christ on the shared shining throne of light, the two side by side, the man "
            "sharing the very victory Christ already won — welcome and belonging, quiet "
            "and glad. Only Christ wears the plain cream robe; the overcomer is in his "
            "brown-grey wool. The hall's brilliance rests on them both, never a ring "
            "around either head. Ordinary-sized men, one head each, gazes forward and "
            "toward each other and not to the camera; nothing is written anywhere; no "
            "figure of God appears."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# DOOR-NIGHT, LAMPLIT-ROOM and THRONE-GLORY are all NEW places — no committed plate yet.
# The runner promotes each from its first NON-Jesus frame before generating the rest of
# that place: DOOR-NIGHT from b01, LAMPLIT-ROOM from b04, THRONE-GLORY from b11. Steps in
# QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: DOOR-NIGHT / LAMPLIT-ROOM / THRONE-GLORY and OVERCOMER are carried by the
# build-local text locks above; Jesus is injected by the assembler on every jesus=True
# beat (ref=True). Only Jesus wears cream.
REFS = {
}
