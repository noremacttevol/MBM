#!/usr/bin/env python3
"""V2 beat map — row 200, build-200-gospel-to-all-the-world (Matthew 24:14 — "And this gospel
of the kingdom shall be preached in all the world for a witness unto all nations; and then
shall the end come."), spoken by Jesus in the Olivet discourse on the Mount of Olives. THE
FINAL VIDEO of the 200 — the Great-Commission promise that the good news reaches the whole
world.

COVERAGE: 12 pictures over 40.190 s (card_start) = ~3.35 s/picture (lesson 12 movie-coverage).
Two places: OLIVET (the Mount of Olives, where Jesus sits with his disciples and gives the
discourse — Jesus IS embodied here) and NATIONS-WORLD (the good news going out to peoples of
every nation — the church carrying it, jesus=False). Human spine: JESUS foretelling the road
ahead and the one thing that outlasts it — the gospel to all the world; then the believers of
all nations who carry it.

=====================================================================
No open Cameron complaint (v2_outline.py 200). Fresh V2 beat map; Board Audio = OK.
=====================================================================

SPEAKER LAW:
  j1  Matthew 24:14  "And this gospel of the kingdom shall be preached in all the world for a
      witness unto all nations; and then shall the end come."   = JESUS → RED-letter caption.
n0a, n0b, n1a, n1b, n2a, n2b, n3 and card are the NARRATOR → white.
**JESUS IS IN THIS STORY** (the Olivet discourse): on every beat he appears set **jesus=True +
ref=True** so the locked JESUS-MASTER-REF face and the JESUS LOCK attach and the red-letter
lands on his own face (b09/b10). **Only Jesus wears cream** — no one else is in cream or white.
The Jesus beats are b01, b02, b03, b04, b09, b10.

**HARD GATE — GOD / THE FATHER IS NEVER EMBODIED, AND THE JESUS FACE GATE MUST PASS.** The
gospel going out (b05-b08, b11, b12) is carried by REAL PEOPLE — messengers and believers of
every nation preaching, receiving, carrying and living the good news — NEVER by a divine
figure, dove, beam, hand-from-sky, ring or symbol. Jesus himself is embodied only in the OLIVET
beats (b01-b04, b09/b10) under the master-face lock; the Father is never shown. Run
`jesus_face_gate.py` before any credit — every Jesus beat carries the REF line and the LOCK.
Drift-word gate: no halo / glow / rim-light / beam in any scene text.

CONTENT-CARE: "wars, rumors, hardship, patience under strain" (b03) is foretold with grave
tenderness on Jesus's face and sober disciples — NEVER graphic war, battle, blood or gore (at
most a distant, restrained smudge of smoke on the far horizon; the focus stays on the faces).
"and then shall the end come" (b10) is Jesus's sure, calm word — NOT a scene of destruction or
apocalypse; the certainty is on his face, no cataclysm shown. The nations receiving the good
news (b07/b12) are glad and dignified, peoples of every land, never caricatured.

TIME-OF-DAY: warm daylight throughout — the Mount of Olives in clear day with Jerusalem below,
the lands of the nations in warm day. Not night; no divine light.

PLACES / LOCKS:
  OLIVET        the Mount of Olives — an olive-clad slope above Jerusalem, the city and temple
                spread below, where Jesus teaches the disciples (b01-b04, b09/b10). NEW
                build-local place; runner promotes from b01 (a NON... — this is a JESUS frame,
                so the runner must NOT auto-wire it; promote b01 by hand per QC).
  NATIONS-WORLD the wide world and its many nations, where the good news is carried and
                received (b05-b08, b11, b12). NEW build-local place; runner promotes from b05
                (a NON-Jesus frame).
People locks: JESUS (locked master face + JESUS LOCK, injected on jesus/ref beats — only he
wears cream), DISCIPLES (the disciples on the mount), NATIONS-BELIEVERS (the messengers and
peoples of every nation who carry and receive the gospel). No one but Jesus wears cream/white.

AUDIO: ⚠ OPEN COMPLAINT "Still the wrong audio. Im pissed" (reportedAgainst the live
Jul-29 V1 cut). DO NOT default-stream-copy — that re-ships the exact rejected audio.
Row is PARKED NEEDS-AUDIO: the audio-fix lane must voice-ID/transcribe the delivered
audio, re-voice through the chosen ElevenLabs cast ONLY if genuinely wrong (or confirm a
stale-cache delivery like row 110), then set AUDIO_FROM_V1_SEGMENTS / ship corrected,
BEFORE any picture build. Board Audio = OK is the audit-spec gate only, not a voice check.
card_start = 40.190 s (TAIL 5.0 — a longer closing card for the final video). Picture-only.
"""

# OLIVET, NATIONS-WORLD, DISCIPLES and NATIONS-BELIEVERS are build-local text locks. JESUS is
# injected on every jesus=True/ref=True beat (master face + LOCK + cream); no other image REFS.
# The Father / God is never embodied; only Jesus wears cream.
LOCKS = {
    "OLIVET": (
        "OLIVET LOCK: the same place in every frame — the Mount of Olives above Jerusalem: "
        "a gentle olive-clad slope of old gnarled olive trees and grey terrace stones, and "
        "below and beyond it the ancient city of Jerusalem with its great stone temple "
        "spread across the valley under a broad daytime sky. Ancient Near-Eastern only; no "
        "modern building, vehicle, pole, wire or sign, no rendered writing. The same slope, "
        "olive trees and the city-and-temple below throughout, in warm daylight."
    ),
    "NATIONS-WORLD": (
        "NATIONS-WORLD LOCK: the same visual world in every frame — the wide ancient world "
        "of many nations: sunlit roads, harbours and market squares of varied ancient "
        "lands, peoples of many regions, dress and skin-tones going about their lives, hills "
        "and sea and distant cities. Ancient first-century world only; no modern building, "
        "vehicle, road, pole, wire, sign, flag or rendered writing anywhere. The same broad, "
        "many-nationed world throughout, in warm daylight."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the same men in every frame they appear — the disciples on the "
        "mount, first-century Galilean men of varied ages in plain earth-toned wool tunics "
        "and mantles in muted browns, blues, russets and greys (NEVER cream, NEVER white — "
        "cream is Jesus's alone). Weathered, ordinary faces, distinct individuals and not "
        "twins; attentive as they listen to Jesus. The same men throughout."
    ),
    "NATIONS-BELIEVERS": (
        "NATIONS-BELIEVERS LOCK: the messengers and peoples of every nation who carry and "
        "receive the good news — a wide, diverse mix of ordinary ancient-world men, women "
        "and children of many regions, dress and skin-tones, in varied earth-toned wool and "
        "linen (NEVER cream, NEVER white — cream is Jesus's alone, and Jesus is not among "
        "them). Distinct individual faces, never twins or cloned faces; ordinary-sized "
        "people with two hands and one head each; no modern clothing, tools, flags or "
        "signage. Together they are 'all nations.'"
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r200-b01", "out": "s01-on-the-mount-of-olives.jpeg", "seg": "n0a",
        "window": "0.000-3.300", "wide": True, "jesus": True, "ref": True,
        "locks": ["OLIVET", "DISCIPLES"],
        "narration": "Jesus sat with his disciples on the Mount of Olives,",
        "must_show": "the establishing frame — Jesus seated with his disciples on the olive slope of the Mount of Olives, Jerusalem and its temple spread below; the disciples' gazes converge on Jesus. Jesus in cream (locked master face); no one else in cream.",
        "must_not_show": "no one but Jesus in cream or white; no God or Father figure, dove, beam or hand-from-sky; no halo, glare or rim-light around Jesus or anyone; no modern object; no rendered writing; not a cartoon; not a detached tiny Jesus at the frame edge; not a posed line facing the lens.",
        "scene": (
            "An establishing wide on the olive slope of the Mount of Olives in warm daylight, "
            "camera set among the disciples looking slightly up toward Jesus so the disciples' "
            "backs and three-quarter faces turn toward him and every gaze converges on him, "
            "never to the camera: Jesus (the locked master face, cream robe) sits on the grey "
            "terrace stones under the old olive trees with his disciples (muted earth-toned "
            "wool, not cream) gathered close and attentive around him; below and beyond, the "
            "ancient city of Jerusalem and its great temple spread across the valley. This is "
            "a real hillside gathering, no one lined up facing the lens. Ordinary-sized people "
            "on one ground plane, Jesus an ordinary-sized man among them; warm daylight on "
            "them, no ring of light around any head; nothing is written anywhere; no divine "
            "figure but the embodied Jesus."
        ),
    },
    {
        "id": "v2-r200-b02", "out": "s02-the-road-ahead.jpeg", "seg": "n0a",
        "window": "3.300-6.300", "wide": False, "jesus": True, "ref": True,
        "locks": ["OLIVET", "DISCIPLES"],
        "narration": "telling them what the long road ahead would hold —",
        "must_show": "Jesus teaching — an over-shoulder two-shot of Jesus speaking earnestly to the attentive disciples, telling them what the long road ahead would hold; Jesus in cream, the disciples listening.",
        "must_not_show": "no one but Jesus in cream or white; no God or Father figure, dove or beam; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "An over-shoulder two-shot on the mount in warm daylight, camera behind a "
            "disciple's shoulder looking to Jesus so the disciple's back is to the lens and "
            "his gaze goes to Jesus, never to the camera: Jesus (locked master face, cream) "
            "speaks earnestly, one hand open, telling the attentive disciples what the long "
            "road ahead would hold. Ordinary-sized, one head each; warm daylight on their "
            "faces, no ring of light around any head; nothing is written anywhere; no divine "
            "figure but the embodied Jesus."
        ),
    },
    {
        "id": "v2-r200-b03", "out": "s03-wars-and-hardship.jpeg", "seg": "n0b",
        "window": "6.300-9.980", "wide": False, "jesus": True, "ref": True,
        "locks": ["OLIVET", "DISCIPLES"],
        "narration": "wars, rumors, hardship, and patience under strain.",
        "must_show": "Jesus foretelling hard times with grave tenderness, the disciples sober as they take it in; the hardship carried by their faces, NOT by any graphic war or violence.",
        "must_not_show": "no one but Jesus in cream or white; no God or Father figure, dove or beam; NO graphic war, battle, blood, gore or the dead; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus (locked master face, cream) on the mount in warm daylight, his "
            "face grave and tender as he foretells wars, rumours and hardship and the need "
            "for patience under strain; beside him a disciple's sober, weighed face takes it "
            "in. The hard times are carried only by their faces — at most a faint, distant "
            "smudge of smoke on the far horizon beyond the city, no battle, no blood, no dead. "
            "Their gazes are out over the land and between them, not to the camera; warm "
            "daylight on their faces, no ring of light around any head; nothing is written "
            "anywhere; no divine figure but the embodied Jesus."
        ),
    },
    {
        "id": "v2-r200-b04", "out": "s04-the-one-thing.jpeg", "seg": "n1a",
        "window": "9.980-13.520", "wide": False, "jesus": True, "ref": True,
        "locks": ["OLIVET", "DISCIPLES"],
        "narration": "Then he turned to the one thing that would outlast all of it:",
        "must_show": "the turn to hope — a close on Jesus, his grave face lifting with steady hope as he turns to the one thing that would outlast all the hardship; the disciples leaning in.",
        "must_not_show": "no one but Jesus in cream or white; no God or Father figure, dove or beam; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus (locked master face, cream) on the mount in warm daylight, his "
            "grave face lifting into steady, sure hope as he turns from the hard road to the "
            "one thing that would outlast all of it; a disciple leans in, drawn by the change. "
            "Jesus's gaze lifts out and ahead, not to the camera; warm daylight on his face, "
            "no ring of light around his head; nothing is written anywhere; no divine figure "
            "but the embodied Jesus."
        ),
    },
    {
        "id": "v2-r200-b05", "out": "s05-to-every-corner.jpeg", "seg": "n1b",
        "window": "13.520-16.540", "wide": True, "jesus": False, "ref": False,
        "locks": ["NATIONS-WORLD", "NATIONS-BELIEVERS"],
        "narration": "a message carried to every corner of the earth.",
        "must_show": "the establishing NATIONS-WORLD frame (NON-Jesus, the plate the runner promotes) — a wide of the broad ancient world with messengers setting out along roads toward its far corners, the good news beginning to travel.",
        "must_not_show": "no Jesus and no one else in cream or white; no God or Father figure, dove or beam; no halo or ring of light; no modern object, road, vehicle or sign; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing wide of the broad ancient world in warm daylight, camera raised "
            "and set behind travellers whose backs are to the lens so their travel goes out "
            "into the far land, never to the camera: messengers (earth-toned travelling wool, "
            "not cream) set out along sunlit roads toward the far corners of the world — "
            "hills, a harbour and distant cities of many lands beyond them — the message "
            "beginning to travel to every corner of the earth. Ordinary-sized people on the "
            "roads; warm daylight over the land, not around any head; nothing is written "
            "anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r200-b06", "out": "s06-not-a-secret.jpeg", "seg": "n2a",
        "window": "16.540-18.970", "wide": False, "jesus": False, "ref": False,
        "locks": ["NATIONS-WORLD", "NATIONS-BELIEVERS"],
        "narration": "Not a secret kept for a few.",
        "must_show": "not a secret — a believer speaking the good news openly to a gathered handful in a sunlit square, out in the open for all to hear, nothing hidden or whispered.",
        "must_not_show": "no Jesus and no one else in cream or white; no God or Father figure, dove or beam; no halo or ring of light; no secrecy, hiding or shadows; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot in a sunlit market square of an ancient town in warm daylight: a believer "
            "(earth-toned wool, not cream) speaks the good news openly, hands wide, to a "
            "gathered handful of ordinary townsfolk who lean in to hear — out in the open, "
            "nothing hidden or whispered, no secret kept for a few. Ordinary-sized people, "
            "one head each, gazes between the speaker and hearers, not to the camera; warm "
            "daylight on them, not around any head; nothing is written anywhere; no divine "
            "figure."
        ),
    },
    {
        "id": "v2-r200-b07", "out": "s07-witness-to-all-nations.jpeg", "seg": "n2b",
        "window": "18.970-22.000", "wide": True, "jesus": False, "ref": False,
        "locks": ["NATIONS-WORLD", "NATIONS-BELIEVERS"],
        "narration": "A witness given to all nations —",
        "must_show": "a witness to all nations — a wide of peoples of many different lands and skin-tones together receiving the good news, gladness dawning across their varied faces; the witness reaching every nation.",
        "must_not_show": "no Jesus and no one else in cream or white; no God or Father figure, dove or beam; no halo or ring of light; no modern object, flag or sign; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "A wide in warm daylight, camera behind a foreground hearer whose back is to the "
            "lens: peoples of many different lands and skin-tones (varied earth-toned dress, "
            "none cream) are gathered together receiving the good news, gladness dawning "
            "across their varied faces — a witness given to all nations. A real diverse crowd, "
            "no one lined up facing the lens. Ordinary-sized people on one ground plane; warm "
            "daylight over them, not around any head; nothing is written anywhere; no divine "
            "figure."
        ),
    },
    {
        "id": "v2-r200-b08", "out": "s08-until-the-end.jpeg", "seg": "n2b",
        "window": "22.000-25.020", "wide": False, "jesus": False, "ref": False,
        "locks": ["NATIONS-WORLD", "NATIONS-BELIEVERS"],
        "narration": "the good news of the kingdom going out until the very end.",
        "must_show": "the good news still going out — a messenger handing on the word to another who will carry it further, the message passing on and on toward the very end; carried person to person.",
        "must_not_show": "no Jesus and no one else in cream or white; no God or Father figure, dove or beam; no halo or ring of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot on a road at the edge of a town in warm daylight: one messenger "
            "(earth-toned travelling wool, not cream) clasps the shoulder of another and "
            "sends him on to carry the good news further down the road — the word passing on "
            "and on, going out until the very end. Ordinary-sized, one head each, gazes "
            "between them and down the onward road, not to the camera; warm daylight on them, "
            "not around any head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r200-b09", "out": "s09-preached-in-all-the-world.jpeg", "seg": "j1",
        "window": "25.020-28.500", "wide": False, "jesus": True, "ref": True,
        "locks": ["OLIVET", "DISCIPLES"],
        "narration": "And this gospel of the kingdom shall be preached in all the world for a witness unto all nations;",
        "must_show": "RED caption (JESUS) — back on the mount, a close on Jesus speaking the promise directly, the disciples intent on him; Jesus in cream (locked master face), the red-letter on his own face.",
        "must_not_show": "no one but Jesus in cream or white; no God or Father figure, dove or beam; no halo, glare or rim-light; no modern object; nothing written; not a cartoon; not a detached tiny Jesus at the frame edge.",
        "scene": (
            "A close two-shot on the mount in warm daylight: Jesus (locked master face, cream) "
            "speaks the promise directly and surely — that this gospel of the kingdom shall be "
            "preached in all the world for a witness unto all nations — a disciple beside him "
            "intent on his words. Jerusalem lies below beyond them. Jesus's gaze is out and "
            "sure, not to the camera; warm daylight on his face, no ring of light around his "
            "head; nothing is written anywhere; no divine figure but the embodied Jesus."
        ),
    },
    {
        "id": "v2-r200-b10", "out": "s10-then-the-end-come.jpeg", "seg": "j1",
        "window": "28.500-32.910", "wide": False, "jesus": True, "ref": True,
        "locks": ["OLIVET", "DISCIPLES"],
        "narration": "and then shall the end come.",
        "must_show": "RED caption (JESUS) — a close on Jesus's calm, certain face as he says 'and then shall the end come'; the certainty is on his face, NOT a scene of destruction; the disciples steadied by his sureness.",
        "must_not_show": "no one but Jesus in cream or white; no God or Father figure, dove or beam; NO destruction, apocalypse, fire, ruin or cataclysm; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Jesus (locked master face, cream) on the mount in warm daylight, his "
            "face calm and certain as he says that then shall the end come — the sureness "
            "carried entirely by his steady face, with NO scene of destruction or cataclysm "
            "anywhere; a disciple beside him steadied by his calm. Jesus's gaze is level and "
            "sure, not to the camera; warm daylight on his face, no ring of light around his "
            "head; nothing is written anywhere; no divine figure but the embodied Jesus."
        ),
    },
    {
        "id": "v2-r200-b11", "out": "s11-the-task-we-carry.jpeg", "seg": "n3",
        "window": "32.910-36.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["NATIONS-WORLD", "NATIONS-BELIEVERS"],
        "narration": "The task he gave is still the task we carry: tell it, show it, live it —",
        "must_show": "the task carried on — believers of different nations telling, showing and living the good news: one speaking it, one serving a neighbour, one living it out kindly; the same task carried on.",
        "must_not_show": "no Jesus and no one else in cream or white; no God or Father figure, dove or beam; no halo or ring of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot in a sunlit town in warm daylight: believers of different nations "
            "(varied earth-toned dress, none cream) carry the task on — one telling the good "
            "news to a listener, another lifting and serving a poor neighbour, another simply "
            "living it in a kind, honest act — tell it, show it, live it. Ordinary-sized "
            "people on one ground plane, one head each, gazes among one another and their "
            "work, not to the camera; warm daylight on them, not around any head; nothing is "
            "written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r200-b12", "out": "s12-for-all-nations.jpeg", "seg": "n3",
        "window": "36.500-40.190", "wide": True, "jesus": False, "ref": False,
        "locks": ["NATIONS-WORLD", "NATIONS-BELIEVERS"],
        "narration": "until the promise is fulfilled. Every nation, every people.",
        "must_show": "the closing image — a wide of peoples of every nation together in the good news, the promise reaching all of them; a picture of the whole world gathered into the message. THE FINAL FRAME of the 200.",
        "must_not_show": "no Jesus and no one else in cream or white; no God or Father figure, dove or beam; no halo or ring of light; no modern object, flag or sign; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "A closing wide in warm daylight, camera raised a little behind the near edge of a "
            "great mixed gathering so their backs and three-quarter faces fill the foreground "
            "and their gazes spread out across the scene, never to the camera: peoples of "
            "every nation and land (varied earth-toned dress, none cream) are gathered "
            "together in the good news, glad and at peace — the promise reaching every nation "
            "and every people, the whole world drawn into the message. Ordinary-sized people "
            "on one ground plane; warm daylight over the whole gathering, not around any head; "
            "nothing is written anywhere; no divine figure."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# OLIVET and NATIONS-WORLD are NEW places with no committed plate yet. OLIVET's first frame
# (b01) is a JESUS frame — the runner must NOT hand it to auto-wiring; promote OLIVET from b01
# BY HAND after it passes the Jesus face gate. NATIONS-WORLD is promoted from b05 (a NON-Jesus
# frame). Steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# JESUS is injected on every jesus=True/ref=True beat (master face + JESUS LOCK + cream — only
# he wears cream). OLIVET, NATIONS-WORLD, DISCIPLES and NATIONS-BELIEVERS are build-local text
# locks; no other image REFS. The Father / God is never embodied. THE FINAL VIDEO of the 200.
REFS = {
}
