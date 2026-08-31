#!/usr/bin/env python3
"""GREAT PLAN speaker system — who is talking decides voice AND caption colour.

Forked from the 200-queue's mbm_speakers.py (SPEAKER-LAW.md) with ONE deliberate
doctrinal deviation, decided 2026-08-31 for The Great Plan film:

  The 200-queue folds the premortal Christ (Jehovah) into the GOD speaker.
  The Great Plan's entire thesis is that the Father and the Son are TWO distinct
  persons — so here the Son (pre-mortal AND mortal) is always JESUS (red, Chris),
  and FATHER (green, Bill) is only ever Elohim. The film also adds DEVIL: a voice
  with no body (Cameron, 2026-08-31 — he is never rendered, only heard).

THE HARD RULE carries over: everything except NARRATOR is VERBATIM scripture a
viewer could look up (KJV or LDS standard works). Only the storyteller speaks in
modern English.
"""

NARRATOR = "narrator"
JESUS = "jesus"        # the Son — premortal Jehovah and the mortal Christ alike
FATHER = "father"      # Elohim only
DEVIL = "devil"        # a spirit and a voice; NEVER rendered in any picture
SCRIPTURE = "scripture"
WOMAN = "woman"

ALL = (NARRATOR, JESUS, FATHER, DEVIL, SCRIPTURE, WOMAN)

# Caption colours. Narrator/Jesus/scripture/woman match the 200-queue exactly so
# the two products read as one family. FATHER keeps the green Cameron already
# knows as the Father's colour. DEVIL gets a cold ash-violet no one else uses.
COLOR = {
    NARRATOR:  "white",
    JESUS:     "0xEE3322",   # locked red-letter red
    FATHER:    "0x5BE38B",   # the GOD green from the 200-queue
    DEVIL:     "0xB39DDB",   # cold ash-violet — only the enemy speaks in it
    SCRIPTURE: "0x8FDCFF",
    WOMAN:     "0xFF9EC7",
}

# mbm_caption_timing imports color_of/is_scripture from this module when it sits
# on sys.path ahead of the 200-queue copy.
def is_scripture(speaker):
    return speaker != NARRATOR


def color_of(speaker):
    return COLOR[speaker]


def check(speaker):
    if speaker not in COLOR:
        raise ValueError(f"unknown speaker {speaker!r}; expected one of {ALL}")
    return speaker
