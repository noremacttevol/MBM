#!/usr/bin/env python3
"""V2 beat map — row 173, build-173-dead-shall-hear (John 5:25-29, "the dead
shall hear the voice of the Son of God... and they that hear shall live... all
that are in the graves shall hear his voice, and shall come forth").

COVERAGE: 13 pictures over 58.85 s (card_start) = ~4.5 s/picture (lesson 12
movie-coverage). ONE establishing wide per place (b01 the discourse, b10 the
resurrection ground); every other beat is a single, a close or a two-shot.

OPEN CAMERON COMPLAINT (audio) — ALREADY FIXED AT SOURCE, verified: `v2_outline.py
173` shows [OPEN — MUST BE FIXED]: "Mispronounced live at the end." The homograph
"live" (the VERB, /liv/, rhymes with give) was rendered as the adjective (/lyv/,
rhymes with hive) on the closing narrator line n2b "To hear him is to live." The
fix is authored in BOTH make_narration.py files: SPOKEN = {"live": "liv"} (Cameron
denial #173, 2026-07-22), covering every "live" in the build — j1c "they that hear
shall live", n2a-area, n2b "to hear him is to live", and the card "listen — and
live" — all the verb. The AUTHORITATIVE V1 mp4 was RE-RENDERED 2026-07-29 (after
the fix), so unlike rows 50/51 this is NOT an orphaned fix — the delivered audio
already carries "liv". RUNNER: assemble on the fixed V1 audio (do NOT re-voice),
and the review card MUST tell Cameron the ending "live" pronunciation is fixed.
See QC.md COMPLAINT LEDGER.

SPEAKER LAW: John's gospel, Jesus in the flesh → RED-LETTER. j1a/j1b/j1c (John
5:25, one sentence cut three ways for pacing) and j2 (John 5:28-29) are the JESUS
voice → RED captions, and every red beat pictures JESUS on his own words (row-39
law — a red caption sits on the speaker's face, never on a listener's). The
narrator beats (n0/n1/n2a/n2c/n2b) are WHITE; some of them also picture Jesus
(b01/b03/b07) because they describe him, which is not a red-letter misattribution.
Only Jesus wears cream.

CONTENT-CARE (the DEAD + the general resurrection → restraint governs):
  - "come forth" / "every grave will open" is the RESURRECTION shown as DIGNITY
    and LIFE: whole, healthy, FULLY-CLOTHED, living people rising and standing in
    the dawn light, faces full of life. NEVER corpses, skeletons, bones, rotting
    or bandaged flesh, zombies clawing out, gaping pits of bones, gore or ghosts
    (row-171 lesson: the grave loses its grip is DAWN LIGHT, not the walking
    dead). Graves are plain rock tombs opening to warm light.
  - No halo, glow or rim-light on anyone, least of all Jesus; light is real
    directional dawn/day light.

PLACES:
  TEMPLE-COURT (shared/global lock)  Jesus's discourse to the crowd in Jerusalem
                                     (b01-b09)
  RESURRECTION-GROUND (NEW build-local)  the burial hillside at first light where
                                     the dead come forth whole (b10-b13)
NEW place (runner promotes from its first good NON-Jesus frame, lesson 11):
  RESURRECTION-GROUND  promote b10 (the establishing wide — no Jesus in it)
  TEMPLE-COURT is a shared place; v2_stash.py --wire will suggest a plate to reuse.
Steps in QC.md.
"""

# LOCKS: RESURRECTION-GROUND is build-local. TEMPLE-COURT and BACKGROUND-CAST are
# shared/global tokens injected from the recipe (same as rows 171/162). Jesus is
# carried by jesus=True + ref=True; only Jesus wears cream.
LOCKS = {
    "RESURRECTION-GROUND": (
        "RESURRECTION-GROUND LOCK: the same place in every frame — a first-"
        "century burial hillside at the first warm light of morning, plain "
        "rock-cut tombs and simple stone markers set into a low grassy slope, "
        "dew on the grass, low hills and an open dawn sky beyond. This is the "
        "general resurrection shown with DIGNITY AND LIFE: the dead who come "
        "forth are WHOLE, HEALTHY, FULLY-CLOTHED, LIVING-LOOKING people of every "
        "age in ordinary earth-toned wool, standing, rising and stepping into the "
        "warm dawn light, their faces calm and full of life; the tombs stand open "
        "to the light. THIS IS NEVER A HORROR SCENE: nowhere is there a corpse, "
        "cadaver, skeleton, skull, bone, rotting or decayed flesh, grave-wrapping "
        "or mummy-bandage, a figure clawing or crawling out of the earth, a pit "
        "full of bones, gore, blood, or any ghost, mist or translucent shade. "
        "The same hillside, tombs and dawn throughout — never modern masonry, "
        "metal, railing, sign or fixture, and no rendered writing of any kind."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r173-b01", "out": "s01-the-hour-is-coming.jpeg", "seg": "n0",
        "window": "0.400-8.134", "wide": True, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT", "BACKGROUND-CAST"],
        "narration": "Jesus said a time was coming — and had already begun — when something impossible would happen.",
        "must_show": "the ONE establishing wide of the discourse — the camera stands back past the shoulders of a seated, standing crowd in a Jerusalem temple court, looking toward Jesus mid-teaching among them; the moment he begins to say the impossible.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; no scroll, writing, lettering or panel of any kind; no modern object; no face posed to the lens.",
        "scene": (
            "In a bright stone temple court the camera stands back past the "
            "shoulders and backs of a gathered crowd — men and women of Jerusalem "
            "seated and standing on the worn paving — and looks toward Jesus, a "
            "warm Middle Eastern man in a plain cream robe, teaching among them "
            "with a quiet, steady authority, one hand open as he begins to speak. "
            "Pale columns and the bright day stand beyond. Every figure is an "
            "ordinary-sized, distinct person with two hands and one head, none but "
            "Jesus in cream and none turned to the camera; nothing is written "
            "anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r173-b02", "out": "s02-the-crowd-listens.jpeg", "seg": "n1",
        "window": "8.134-11.620", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE-COURT", "BACKGROUND-CAST"],
        "narration": "The dead would hear a voice. Not a rumor of a voice.",
        "must_show": "close on the listeners — two or three distinct faces in the crowd turning toward Jesus, caught by a claim they can hardly believe; not a rumor but a promise being spoken to them.",
        "must_not_show": "no Jesus and no cream in this close; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Close among the crowd in the temple-court light: two or three "
            "ordinary Jerusalem faces of different ages turn toward the speaker, "
            "arrested and half-disbelieving, leaning in to be sure of what they "
            "have heard. Worn paving and pale stone sit soft behind. "
            "Ordinary-sized, distinct people with two hands and one head each, "
            "none in cream, their eyes toward the speaker off-frame and not the "
            "camera; nothing is written anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r173-b03", "out": "s03-his-voice.jpeg", "seg": "n1",
        "window": "11.620-14.138", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "His voice.",
        "must_show": "close on Jesus — a quiet, steady close on his face as he speaks; the voice the dead would hear is HIS.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "A quiet close on Jesus in the temple-court light — a warm Middle "
            "Eastern man in a plain cream robe, dark wavy shoulder-length hair and "
            "a full dark beard, warm brown eyes steady as he speaks, calm "
            "authority in his face. Pale stone stands soft behind him. An "
            "ordinary-sized man with two hands and one head, his gaze level toward "
            "the crowd and not the camera; nothing is written anywhere and no "
            "light rings his head."
        ),
    },
    {
        "id": "v2-r173-b04", "out": "s04-verily-verily.jpeg", "seg": "j1a",
        "window": "14.138-20.354", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "Verily, verily, I say unto you, The hour is coming, and now is,",
        "must_show": "RED-LETTER (Jesus) — Jesus speaking with solemn weight, an open hand lifting slightly as he says the hour is coming and now is; his own words on his own face.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Close on Jesus in the temple court, one hand lifting a little from "
            "his side with solemn weight as he speaks — the warm cream robe, the "
            "dark beard, the steady brown eyes — declaring a thing already "
            "beginning. Worn paving and pale columns sit soft behind. An "
            "ordinary-sized man with two hands and one head, his gaze on the crowd "
            "and not the camera; nothing is written anywhere and no light rings "
            "his head."
        ),
    },
    {
        "id": "v2-r173-b05", "out": "s05-voice-of-the-son-of-god.jpeg", "seg": "j1b",
        "window": "20.354-24.906", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "when the dead shall hear the voice of the Son of God:",
        "must_show": "RED-LETTER (Jesus) — Jesus naming himself the Son of God whose voice the dead will hear; quiet certainty, not spectacle.",
        "must_not_show": "no halo, glare, rim-light or shining aura on Jesus; only Jesus in cream; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Close on Jesus, his face lifted a little in quiet certainty as he "
            "names the voice the dead will hear as his own — the plain cream robe, "
            "the dark wavy hair and full beard, warm brown eyes calm and sure. "
            "The bright temple court stands soft beyond. An ordinary-sized man "
            "with two hands and one head, his gaze steady toward the crowd and not "
            "the camera; nothing is written anywhere and no light rings his head."
        ),
    },
    {
        "id": "v2-r173-b06", "out": "s06-they-shall-live.jpeg", "seg": "j1c",
        "window": "24.906-28.608", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "and they that hear shall live.",
        "must_show": "RED-LETTER (Jesus) — Jesus with an open, calling hand extended toward the crowd as he promises that those who hear shall live; a hand that gives life, not commands.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Jesus in the temple-court light extends an open hand toward the "
            "gathered people, his face warm and sure as he promises life to those "
            "who hear — the cream robe, the dark beard, a gesture that gives "
            "rather than commands. Pale stone and the bright day sit soft behind. "
            "An ordinary-sized man with two hands and one head, his gaze on the "
            "crowd and not the camera; nothing is written anywhere and no light "
            "rings his head."
        ),
    },
    {
        "id": "v2-r173-b07", "out": "s07-made-life-calls-it-back.jpeg", "seg": "n2a",
        "window": "28.608-33.222", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "The One who made life is the One who calls it back.",
        "must_show": "close on Jesus, calm and full of quiet power — the maker of life who calls it back; the same steady face, the promise settling.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "A close on Jesus in the temple court, calm and full of quiet power, "
            "his warm brown eyes steady and his hand resting open at his side — "
            "the one who made life speaking of calling it back, the promise "
            "settling over the crowd. Pale stone stands soft behind him. An "
            "ordinary-sized man in cream with two hands and one head, his gaze "
            "level toward the people and not the camera; nothing is written "
            "anywhere and no light rings his head."
        ),
    },
    {
        "id": "v2-r173-b08", "out": "s08-marvel-not.jpeg", "seg": "j2",
        "window": "33.222-38.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "Marvel not at this: for the hour is coming,",
        "must_show": "RED-LETTER (Jesus) — Jesus quieting the crowd's wonder, a steadying open hand, telling them not to marvel; the hour is coming.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Close on Jesus, an open steadying hand raised gently as if to calm "
            "the crowd's astonishment, his face patient and sure — the cream robe, "
            "the dark beard, the warm brown eyes — telling them not to marvel, for "
            "the hour is coming. The bright temple court sits soft beyond. An "
            "ordinary-sized man with two hands and one head, his gaze on the crowd "
            "and not the camera; nothing is written anywhere and no light rings "
            "his head."
        ),
    },
    {
        "id": "v2-r173-b09", "out": "s09-shall-come-forth.jpeg", "seg": "j2",
        "window": "38.000-43.335", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEMPLE-COURT"],
        "narration": "in the which all that are in the graves shall hear his voice, and shall come forth.",
        "must_show": "RED-LETTER (Jesus) — Jesus with an arm opening outward toward the far distance as he tells that all in the graves will hear and come forth; the full sweep of the promise in his gesture.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; no graves or corpses in this frame; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Jesus in the temple-court light opens an arm outward toward the far "
            "distance as he speaks of every grave hearing his voice and coming "
            "forth — the cream robe, the dark wavy hair, warm brown eyes wide with "
            "the sweep of the promise. Pale columns and the bright day stand "
            "beyond. An ordinary-sized man with two hands and one head, his gaze "
            "out past the crowd and not the camera; nothing is written anywhere "
            "and no light rings his head."
        ),
    },
    {
        "id": "v2-r173-b10", "out": "s10-all-of-them.jpeg", "seg": "n2c",
        "window": "43.335-46.500", "wide": True, "jesus": False, "ref": False,
        "locks": ["RESURRECTION-GROUND", "BACKGROUND-CAST"],
        "narration": "Not some of the dead. All of them.",
        "must_show": "the ONE establishing wide of the resurrection ground — the camera looks across a burial hillside at first light where whole, living people of every age are rising and standing in the dawn among the open tombs; not some, but all.",
        "must_not_show": "NO corpse, skeleton, skull, bone, rotting or bandaged flesh, figure clawing out of the earth, pit of bones, gore or ghost — the risen are whole, clothed, living people; no halo, glare or rim-light; no cream on anyone; no scroll, writing or panel; no modern object; no posed line to the lens.",
        "scene": (
            "The camera looks across a low grassy burial hillside in the first "
            "warm light of morning, past the backs of a few nearest figures: all "
            "across the slope, whole and healthy people of every age in ordinary "
            "earth-toned wool are rising to their feet and standing in the dawn "
            "among plain rock tombs that stand open to the light — calm, alive, "
            "restored, not some but all. Dew glints on the grass, low hills sit "
            "beyond. Ordinary-sized, distinct, living-looking people with two "
            "hands and one head each, none in cream and none turned to the camera; "
            "nothing is written anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r173-b11", "out": "s11-every-grave-shall-open.jpeg", "seg": "n2c",
        "window": "46.500-50.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["RESURRECTION-GROUND"],
        "narration": "He said every grave will hear that same voice — and open.",
        "must_show": "closer — one plain rock tomb standing open to the warm dawn light and a whole, living person stepping out of it upright and clothed, restored to life; the grave heard and opened.",
        "must_not_show": "NO corpse, skeleton, bone, decay, grave-wrapping, mummy-bandage, gore or figure crawling from the earth — the person steps out whole, clothed and alive; no ghost or mist; no halo, glare or rim-light; no cream; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Closer on the hillside: one plain rock tomb stands open to the warm "
            "dawn, and from its low doorway a whole, living person in ordinary "
            "earth-toned wool steps out upright and steady, restored and alive, "
            "the morning light on a calm and healthy face. Dew-bright grass and "
            "low hills sit soft beyond. An ordinary-sized, solid, living person "
            "with two hands and one head, not in cream, the eyes lifting toward "
            "the light and not the camera; nothing is written anywhere and no "
            "light rings the head."
        ),
    },
    {
        "id": "v2-r173-b12", "out": "s12-none-left-in-the-ground.jpeg", "seg": "n2c",
        "window": "50.500-55.650", "wide": False, "jesus": False, "ref": False,
        "locks": ["RESURRECTION-GROUND"],
        "narration": "Nobody is too far gone, and nobody gets left in the ground.",
        "must_show": "one risen person reaching down an open hand to help another up onto their feet in the dawn light; nobody too far gone, nobody left in the ground.",
        "must_not_show": "NO corpse, skeleton, bone, decay, gore or figure clawing out of a grave — both are whole living people; no ghost or mist; no halo, glare or rim-light; no cream; no scroll, writing or panel; no modern object; no posed line to the lens.",
        "scene": (
            "On the dawn hillside a risen person already on their feet reaches an "
            "open hand down to another and helps them up from the grassy ground, "
            "both whole and clothed in earth-toned wool, both alive — the strong "
            "and simple picture that nobody is too far gone and nobody is left in "
            "the ground. Open tombs and low hills sit soft in the morning light "
            "beyond. Ordinary-sized, distinct, living people with two hands and "
            "one head each, none in cream, their eyes on each other and not the "
            "camera; nothing is written anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r173-b13", "out": "s13-to-hear-him-is-to-live.jpeg", "seg": "n2b",
        "window": "55.650-58.851", "wide": False, "jesus": False, "ref": False,
        "locks": ["RESURRECTION-GROUND"],
        "narration": "To hear him is to live.",
        "must_show": "a close on one risen, living face lifted into the warm dawn light, breath drawn and eyes open and alive; to hear him is to live.",
        "must_not_show": "NO corpse, decay, bone or gore; no ghost or mist; no halo, glare or rim-light; no cream; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "A close on one risen person's face lifted into the warm dawn light, a "
            "breath drawn and the eyes open, calm and fully alive — an ordinary "
            "weathered face restored, the whole promise resting on this one living "
            "look. The dew-bright hillside sits soft behind. An ordinary-sized, "
            "living person with two hands and one head, not in cream, the eyes "
            "lifted into the light and not to the camera; nothing is written "
            "anywhere and no light rings the head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "TEMPLE-COURT": "PLACE-REF/temple-court.jpeg",  # build-39-pharisee-publican v2-r039-b05
}
# === end PLACE-PLATES ===

# No image REFS: Jesus is carried by the shared JESUS-MASTER-REF auto-attached on
# the jesus=True beats; every other person is an ordinary background/crowd figure.
REFS = {
}

# The delivered audio already carries the "live"->"liv" fix (V1 mp4 re-rendered
# 2026-07-29 after the SPOKEN fix). Assemble on the V1 audio track; do NOT
# re-voice. Leaving AUDIO_FROM_V1_SEGMENTS unset (default) uses the fixed V1 mp4.
