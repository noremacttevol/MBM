#!/usr/bin/env python3
"""MBM SPEAKER SYSTEM — who is talking decides both the voice and the caption colour.

See SPEAKER-LAW.md. This module is the single source of truth. A build declares a
speaker once, per segment, and BOTH the narration voice and the caption colour are
derived from it. That is the whole point: under the old system a build carried the
voice in make_narration.py and the colour in build.py's `KJV = {...}` set, and the
two drifted apart — 15 segments ended up painted Jesus-red while being spoken in the
narrator's voice. One declaration makes that class of bug impossible.

THE FIVE SPEAKERS
  NARRATOR   white       the storyteller. Modern English. Most of the runtime.
  JESUS      red         ONLY where a red-letter KJV actually prints red.
  GOD        green       the Father, the Holy Ghost, or the premortal Christ
                         (Jehovah) — including Old Testament passages, which are
                         NOT red-lettered because he had not yet come in the flesh.
  SCRIPTURE  light blue  everyone else quoted from the KJV — Paul, the prophets,
                         the apostles, the people inside the stories.
  WOMAN      pink        any woman the Bible records speaking.

THE HARD RULE: everything except NARRATOR is VERBATIM King James text a viewer
could look up. Only the storyteller speaks in modern English.
"""

NARRATOR = "narrator"
JESUS = "jesus"
GOD = "god"
SCRIPTURE = "scripture"
WOMAN = "woman"

ALL = (NARRATOR, JESUS, GOD, SCRIPTURE, WOMAN)

# ---------------------------------------------------------------- voices ----
# (voice, rate, pitch). The narrator is unchanged — Cameron is happy with it.
# Jesus MUST be an American voice (permanent law, 2026-07-07). No *Multilingual*
# models anywhere (existing narration law).
VOICE = {
    NARRATOR:  ("en-US-AndrewNeural",      "-20%", "-4Hz"),
    JESUS:     ("en-US-BrianNeural",       "-22%", "-3Hz"),
    GOD:       ("en-US-ChristopherNeural", "-25%", "-12Hz"),
    SCRIPTURE: ("en-US-SteffanNeural",     "-18%", "-8Hz"),
    WOMAN:     ("en-US-JennyNeural",       "-20%", "-2Hz"),
}

# ---------------------------------------------------------------- colours ---
# Chosen to stay readable on the black@0.5 band over the brightest still in the
# library, and to stay clearly distinct from each other and from the locked red.
COLOR = {
    NARRATOR:  "white",
    JESUS:     "0xEE3322",   # locked — the red-letter red, unchanged
    GOD:       "0x5BE38B",   # a regular green, deliberately NOT dark green
    SCRIPTURE: "0x8FDCFF",
    WOMAN:     "0xFF9EC7",
}

# Everything that is not the narrator is verbatim KJV and gets the scripture
# type treatment (slightly larger max size, up to 3 lines).
def is_scripture(speaker):
    return speaker != NARRATOR


def voice_of(speaker, rate=None, pitch=None):
    """(voice, rate, pitch) for a speaker; per-segment overrides win."""
    v, r, p = VOICE[speaker]
    return v, (rate or r), (pitch or p)


def color_of(speaker):
    return COLOR[speaker]


def check(speaker):
    if speaker not in VOICE:
        raise ValueError(f"unknown speaker {speaker!r}; expected one of {ALL}")
    return speaker
