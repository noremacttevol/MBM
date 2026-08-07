#!/usr/bin/env python3
"""V2 beat map — row 193, build-193-the-comforter (John 14:18, 26 — "I will not leave you
comfortless: I will come to you... But the Comforter, which is the Holy Ghost, whom the
Father will send in my name, he shall teach you all things, and bring all things to your
remembrance, whatsoever I have said unto you.").

COVERAGE: 13 pictures over 57.038 s (card_start) = ~4.39 s/picture (lesson 12
movie-coverage). ONE place: the UPPER-ROOM — the lamplit upper room on the night before the
cross, where Jesus sits with the Eleven and promises the Comforter. Human spine: JESUS, the
one doing the comforting hours from the cross, and the DISCIPLES (Peter and John nearest)
receiving the promise. Red-letter j0 and j1 sit on JESUS's own face.

=====================================================================
No open Cameron complaint (v2_outline.py 193). Fresh V2 beat map; Board Audio = OK.
=====================================================================

SPEAKER LAW: this is Jesus's own Upper-Room discourse.
  j0  John 14:18  "I will not leave you comfortless: I will come to you."       JESUS → RED
  j1  John 14:26  "But the Comforter, which is the Holy Ghost ... unto you."    JESUS → RED
Every other segment (n0, n0b, n1, n2a, n2b, n3a, n3b, card) is the NARRATOR → white. Jesus
IS in this story: on every beat he appears set jesus=True + ref=True so the locked master
face and the JESUS LOCK attach and the red-letter lands on him. **Only Jesus wears cream** —
no one else is in cream or white.

**HARD GATE — GOD/THE FATHER IS NEVER EMBODIED, AND THE HOLY GHOST / COMFORTER IS NEVER
EMBODIED.** The Father who "will send" the Comforter is never shown — no figure, face, hand,
throne or beam. The Comforter / Holy Ghost promised here is likewise NEVER given a body:
NO third person standing in for the Spirit, NO dove-with-rays, NO glowing figure, NO
beam-shaped-like-a-person, NO halo. The Spirit's work — teaching and bringing to
remembrance — is carried by JESUS's promise and by the DISCIPLES' faces (attention,
understanding, recollection) in ordinary warm lamplight, never by any supernatural glow or
figure. Drift-word gate: no halo / glow / rim-light / beam anywhere.

CONTENT-CARE: this is comfort and reassurance, not fear. Jesus is calm and giving hope even
though he is hours from the cross; the disciples are troubled but steadied. NO cross, NO
wounds, NO blood, NO Gethsemane agony shown here — the scene stays in the quiet upper room.

TIME-OF-DAY: NIGHT — the upper room is warm lamplight (oil lamps), the night before the
cross. Windows dark. No daylight, but no divine glow either; the light is the lamps.

PLACES / LOCKS:
  UPPER-ROOM  the lamplit upper room (all 13 beats). NEW build-local place — no committed
              plate yet; the runner promotes it from b01 (a NON-Jesus-safe establishing
              wide is not possible here since Jesus is at the table, so the promote frame
              b01 DOES contain Jesus — that is fine, the plate carries the ROOM, and Jesus
              is separately injected by the assembler). If v2_stash.py --wire SUGGESTS the
              build-74 lamplit `room` plate and it is a true match, the runner may --take it.
People locks: DISCIPLES (the Eleven — first-century Galilean men, distinct faces), with
PETER and JOHN named on the beats where they are nearest Jesus (global cast auto-attaches by
token). None wear cream or white; only Jesus wears cream (injected).

AUDIO: default AUDIO LOCK stream-copy (no re-voice; no open complaint). Board Audio = OK.
card_start = 57.038 s. Picture-only — do NOT re-voice.
"""

# UPPER-ROOM + DISCIPLES are declared as build-local text LOCKS; PLACE_REFS stays empty and
# the runner promotes the room from b01. Jesus is injected by the assembler on every
# jesus=True/ref=True beat (only he wears cream); no image REFS needed.
LOCKS = {
    "UPPER-ROOM": (
        "UPPER-ROOM LOCK: the same place in every frame — the upper room on the night "
        "before the crucifixion: a plain first-century stone-walled upper chamber with a "
        "low table set for a simple meal (bread, cups, a shallow dish), floor cushions and "
        "woven mats, a couple of clay oil lamps giving warm low light, and dark night "
        "windows beyond. Ancient and spare; no modern object anywhere, and nothing legible "
        "or rendered is written on any surface. The same lamplit room throughout, at night."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the same men in every frame they appear — the Eleven, "
        "first-century Galilean men of varied ages in plain earth-toned wool tunics and "
        "mantles in muted browns, blues, russets and greys (NEVER cream, NEVER white — "
        "cream is Jesus's alone). Weathered, ordinary faces, distinct individuals and not "
        "twins; troubled and attentive as they listen to Jesus this last night. The same "
        "men throughout."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r193-b01", "out": "s01-the-last-night.jpeg", "seg": "n0",
        "window": "0.000-3.400", "wide": True, "jesus": True, "ref": True,
        "locks": ["UPPER-ROOM", "DISCIPLES"],
        "narration": "On the night before He died, Jesus sat with His disciples",
        "must_show": "the ONE establishing wide (UPPER-ROOM promote) — Jesus seated at the low table in the warm lamplit upper room with the Eleven gathered close around him on the night before the cross; only Jesus wears cream.",
        "must_not_show": "no God or Father figure; no Holy-Ghost figure, dove or beam; no halo, glare or rim-light; only Jesus in cream, no one else in cream or white; no cross or wounds; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing wide of the lamplit upper room at night, camera set low and "
            "behind the shoulders of the disciples so their backs are three-quarters to the "
            "lens and their gazes travel inward across the table toward Jesus and exit the "
            "frame toward him, never to the camera. Jesus — in the plain cream robe (only "
            "he wears cream) — sits at the low table among the Eleven, who lean in close on "
            "the last night; two clay oil lamps give warm low light and the windows beyond "
            "are dark night. Ancient and spare; the lamplight rests on their faces, not "
            "around any head; nothing is written anywhere; no divine figure and no "
            "Spirit-figure."
        ),
    },
    {
        "id": "v2-r193-b02", "out": "s02-not-left-alone.jpeg", "seg": "n0",
        "window": "3.400-6.494", "wide": False, "jesus": True, "ref": True,
        "locks": ["UPPER-ROOM", "PETER", "JOHN"],
        "narration": "and told them they would not be left alone.",
        "must_show": "a close on Jesus speaking gently to Peter and John beside him, reassuring them they will not be left alone; only Jesus in cream.",
        "must_not_show": "no God or Father figure; no Holy-Ghost figure or beam; no halo, glare or rim-light; only Jesus in cream; no cross or wounds; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus in the warm lamplight leaning toward Peter and John beside "
            "him, his face gentle and steady as he reassures them they will not be left "
            "alone. Only Jesus wears cream; the disciples are in muted wool. Ordinary-"
            "sized, one head each, gazes meeting between them and not to the camera; warm "
            "lamplight on their faces, not around any head; nothing is written anywhere; no "
            "divine figure and no Spirit-figure."
        ),
    },
    {
        "id": "v2-r193-b03", "out": "s03-i-will-not-leave-you.jpeg", "seg": "j0",
        "window": "6.494-11.887", "wide": False, "jesus": True, "ref": True,
        "locks": ["UPPER-ROOM", "DISCIPLES"],
        "narration": "I will not leave you comfortless: I will come to you.",
        "must_show": "RED caption (Jesus's own words) — Jesus, warm and sure, an open hand toward the disciples as he promises 'I will not leave you comfortless: I will come to you'; only Jesus in cream.",
        "must_not_show": "no God or Father figure; no Holy-Ghost figure, dove or beam; no halo, glare or rim-light; only Jesus in cream; no cross or wounds; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of Jesus in the lamplit room, warm and sure, one open hand extended "
            "toward the gathered disciples as he speaks the promise not to leave them "
            "comfortless. Only he wears the plain cream robe; the disciples lean in, "
            "steadied. Ordinary-sized people, one head each, gazes on Jesus's face and "
            "hand, not to the camera; warm lamplight on them, not around any head; nothing "
            "is written anywhere; no divine figure and no Spirit-figure."
        ),
    },
    {
        "id": "v2-r193-b04", "out": "s04-hours-from-the-cross.jpeg", "seg": "n0b",
        "window": "11.887-16.800", "wide": False, "jesus": True, "ref": True,
        "locks": ["UPPER-ROOM"],
        "narration": "He was hours from the cross, and He was the one doing the comforting —",
        "must_show": "a close on Jesus's own calm, giving face — hours from the cross yet He is the one doing the comforting, steady and full of quiet hope; only Jesus in cream.",
        "must_not_show": "no God or Father figure; no Holy-Ghost figure or beam; no cross, wounds, blood or agony shown; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus's face in the warm lamplight — calm, giving and full of quiet "
            "hope though he is only hours from the cross; he is the one doing the "
            "comforting, not the one comforted. Only he wears cream. Ordinary-sized, one "
            "head, gaze warm toward his disciples and not to the camera; lamplight on his "
            "face, not around his head; nothing is written anywhere; no divine figure and "
            "no Spirit-figure. No cross, wound or agony anywhere."
        ),
    },
    {
        "id": "v2-r193-b05", "out": "s05-not-on-their-own.jpeg", "seg": "n0b",
        "window": "16.800-21.733", "wide": False, "jesus": True, "ref": True,
        "locks": ["UPPER-ROOM", "PETER", "JOHN"],
        "narration": "promising that whatever else they lost that week, they would not be left on their own.",
        "must_show": "the disciples' troubled faces steadied — Peter and John anxious about the week to come but reassured, Jesus's steadying hand on a shoulder; only Jesus in cream.",
        "must_not_show": "no God or Father figure; no Holy-Ghost figure or beam; no halo, glare or rim-light; only Jesus in cream; no cross or wounds; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of Peter and John in the lamplight, faces troubled about the week "
            "ahead yet steadied as Jesus lays a reassuring hand on a shoulder — they will "
            "not be left on their own. Only Jesus wears cream; the disciples are in muted "
            "wool. Ordinary-sized, one head each, gazes between them and to Jesus, not to "
            "the camera; warm lamplight on their faces, not around any head; nothing is "
            "written anywhere; no divine figure and no Spirit-figure."
        ),
    },
    {
        "id": "v2-r193-b06", "out": "s06-another-helper.jpeg", "seg": "n1",
        "window": "21.733-27.857", "wide": False, "jesus": True, "ref": True,
        "locks": ["UPPER-ROOM", "DISCIPLES"],
        "narration": "He promised another Helper would come — the Holy Ghost, sent by the Father in His name.",
        "must_show": "Jesus promising another Helper — the Holy Ghost the Father will send; carried entirely by Jesus's promise and the disciples' listening faces. THE HOLY GHOST IS NOT SHOWN as any figure, dove or beam; the Father is NOT shown. Only Jesus in cream.",
        "must_not_show": "THE HOLY GHOST / COMFORTER IS NOT EMBODIED — no third person for the Spirit, no dove-with-rays, no radiant figure, no beam-shaped-like-a-person; THE FATHER IS NOT SHOWN — no figure, hand-from-sky, throne or beam; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of Jesus in the lamplit room, an open hand as he promises that another "
            "Helper — the Holy Ghost — will be sent by the Father in his name; the "
            "disciples lean in, listening. The promise is carried by Jesus's words and "
            "their attentive faces alone — no figure stands in for the Spirit and none for "
            "the Father, and no dove or beam appears. Only Jesus wears cream. "
            "Ordinary-sized people, one head each, gazes on Jesus, not to the camera; warm "
            "lamplight on them, not around any head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r193-b07", "out": "s07-teach-them-everything.jpeg", "seg": "n2a",
        "window": "27.857-31.860", "wide": False, "jesus": True, "ref": True,
        "locks": ["UPPER-ROOM", "DISCIPLES"],
        "narration": "This Helper would do two things: teach them everything,",
        "must_show": "the teaching — the disciples receiving understanding as Jesus speaks, comprehension settling on their faces; the Helper's teaching carried by their dawning understanding, NOT by any Spirit figure. Only Jesus in cream.",
        "must_not_show": "THE HOLY GHOST IS NOT EMBODIED — no Spirit figure, dove or beam; no Father figure; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot across the disciples' faces in the warm lamplight as Jesus teaches — "
            "understanding settling on them, eyes lifting in comprehension; the Helper's "
            "promised teaching is shown by their dawning understanding, never by a figure "
            "or beam. Jesus at the edge of frame in cream (only he wears cream); the "
            "disciples in muted wool. Ordinary-sized, one head each, gazes on Jesus and "
            "inward in thought, not to the camera; lamplight on their faces, not around any "
            "head; nothing is written anywhere; no Spirit-figure."
        ),
    },
    {
        "id": "v2-r193-b08", "out": "s08-brought-to-remembrance.jpeg", "seg": "n2b",
        "window": "31.860-36.186", "wide": False, "jesus": False, "ref": False,
        "locks": ["UPPER-ROOM", "DISCIPLES"],
        "narration": "and bring every word Jesus had spoken back to their minds.",
        "must_show": "an insert on a disciple's face lit with recollection — remembering the words Jesus had spoken, quiet recognition dawning; remembrance carried by the man's face, NOT by any Spirit figure or beam.",
        "must_not_show": "THE HOLY GHOST IS NOT EMBODIED — no Spirit figure, dove or beam; no Father figure; no Jesus in this insert; no halo, glare or rim-light; no one in cream or white; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A tight insert on one disciple's face in the warm lamplight, quiet "
            "recollection dawning as words Jesus spoke come back to his mind — recognition "
            "and wonder settling in his eyes. The remembrance is shown in his face alone, "
            "never by a figure, dove or beam. Muted wool (not cream). Ordinary scale, "
            "one head, gaze inward and down in thought, not to the camera; lamplight on his "
            "face, not around his head; nothing is written anywhere; no divine figure and "
            "no Spirit-figure."
        ),
    },
    {
        "id": "v2-r193-b09", "out": "s09-the-comforter.jpeg", "seg": "j1",
        "window": "36.186-41.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["UPPER-ROOM", "DISCIPLES"],
        "narration": "But the Comforter, which is the Holy Ghost, whom the Father will send in my name,",
        "must_show": "RED caption (Jesus's own words) — Jesus naming the Comforter, the Holy Ghost whom the Father will send in His name; carried by Jesus alone. THE HOLY GHOST AND THE FATHER ARE NOT SHOWN. Only Jesus in cream.",
        "must_not_show": "THE HOLY GHOST / COMFORTER IS NOT EMBODIED — no Spirit figure, dove-with-rays or beam; THE FATHER IS NOT SHOWN — no figure, throne or hand-from-sky; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of Jesus in the lamplit room speaking the promise of the Comforter, the "
            "Holy Ghost whom the Father will send in his name; the disciples listen close. "
            "Only Jesus carries the words — no figure stands in for the Spirit or the "
            "Father, and no dove or beam appears. Only he wears cream. Ordinary-"
            "sized people, one head each, gazes on Jesus, not to the camera; warm lamplight "
            "on them, not around any head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r193-b10", "out": "s10-teach-you-all-things.jpeg", "seg": "j1",
        "window": "41.000-45.700", "wide": False, "jesus": True, "ref": True,
        "locks": ["UPPER-ROOM", "DISCIPLES"],
        "narration": "he shall teach you all things,",
        "must_show": "RED caption (Jesus's own words) — Jesus promising the Comforter 'shall teach you all things', the disciples attentive; the teaching carried by Jesus and their faces, no Spirit figure. Only Jesus in cream.",
        "must_not_show": "THE HOLY GHOST IS NOT EMBODIED — no Spirit figure, dove or beam; no Father figure; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of Jesus in the warm lamplight, hand gently open as he promises that "
            "the Comforter shall teach them all things; the disciples are drawn in, "
            "attentive. Only Jesus wears cream. No Spirit-figure, dove or beam. "
            "Ordinary-sized, one head each, gazes on Jesus, not to the camera; lamplight on "
            "their faces, not around any head; nothing is written anywhere; no divine "
            "figure."
        ),
    },
    {
        "id": "v2-r193-b11", "out": "s11-to-your-remembrance.jpeg", "seg": "j1",
        "window": "45.700-50.340", "wide": False, "jesus": True, "ref": True,
        "locks": ["UPPER-ROOM", "DISCIPLES"],
        "narration": "and bring all things to your remembrance, whatsoever I have said unto you.",
        "must_show": "RED caption (Jesus's own words) — Jesus promising the Comforter will bring all his words back to their remembrance; the disciples holding his words close. Only Jesus in cream; no Spirit figure.",
        "must_not_show": "THE HOLY GHOST IS NOT EMBODIED — no Spirit figure, dove or beam; no Father figure; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of Jesus in the lamplight finishing the promise — that the Comforter "
            "will bring all his words back to their remembrance — his disciples holding his "
            "words close, quiet and reassured. Only Jesus wears cream. No Spirit-figure, "
            "dove or beam. Ordinary-sized people, one head each, gazes on Jesus, not "
            "to the camera; warm lamplight on them, not around any head; nothing is written "
            "anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r193-b12", "out": "s12-the-promise-stands.jpeg", "seg": "n3a",
        "window": "50.340-52.600", "wide": False, "jesus": True, "ref": True,
        "locks": ["UPPER-ROOM"],
        "narration": "The promise still stands.",
        "must_show": "a close on Jesus's steady, timeless face — the promise still stands; calm assurance. Only Jesus in cream.",
        "must_not_show": "no God or Father figure; no Holy-Ghost figure or beam; no halo, glare or rim-light; only Jesus in cream; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus's face in the warm lamplight, steady and full of quiet "
            "assurance — the promise still stands. Only he wears cream. Ordinary-sized, one "
            "head, gaze warm and level, not to the camera; lamplight on his face, not "
            "around his head; nothing is written anywhere; no divine figure and no "
            "Spirit-figure."
        ),
    },
    {
        "id": "v2-r193-b13", "out": "s13-teaches-everyone-who-listens.jpeg", "seg": "n3b",
        "window": "52.600-57.038", "wide": False, "jesus": False, "ref": False,
        "locks": ["UPPER-ROOM", "DISCIPLES"],
        "narration": "The Spirit who taught them then teaches everyone who listens now.",
        "must_show": "the closing image — the disciples in the warm lamplit room, quiet and receptive, listening with open hearts; the same promise resting on anyone who listens. The Spirit is present as warmth and attention, NOT as any figure or beam.",
        "must_not_show": "THE HOLY GHOST IS NOT EMBODIED — no Spirit figure, dove or beam; no Father figure; no halo, glare or rim-light; no one in cream or white (Jesus is not in this closing frame); no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closing shot of the disciples in the warm lamplit upper room, quiet and "
            "receptive, faces open and listening — the same promise resting on everyone who "
            "listens. The Spirit's presence is only the warmth of the room and the "
            "attention on their faces; there is no figure, dove or beam. Muted wool "
            "(none cream). Ordinary-sized men, one head each, gazes inward and lifted in "
            "quiet reception, not to the camera; lamplight on their faces, not around any "
            "head; nothing is written anywhere; no divine figure and no Spirit-figure."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# UPPER-ROOM is a NEW place — no committed plate yet. The runner promotes it from b01 (the
# establishing wide; Jesus is in that frame but the plate carries the ROOM, and Jesus is
# separately injected by the assembler). Alternatively, if v2_stash.py --wire SUGGESTS the
# build-74 lamplit `room` plate and the runner judges it a true match, it may --take it.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: the UPPER-ROOM and DISCIPLES are carried by the build-local text locks
# above; PETER and JOHN attach by token from the global cast; Jesus is injected by the
# assembler on every jesus=True/ref=True beat. Only Jesus wears cream. The Father and the
# Holy Ghost are never embodied.
REFS = {
}
