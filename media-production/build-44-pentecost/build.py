#!/usr/bin/env python3
"""build-44-pentecost (Acts 2) — timeline metadata for the V2 pipeline.

Row 44 was swapped 2026-07-23 from "two debtors" (a double-telling of #74) to
Pentecost, an all-new story with NO prior V1 render. The V2 build supplies the
pictures (build-44-pentecost/beats_v2.py) and rebuilds the audio track from this
build's OWN ElevenLabs mp3s (AUDIO_FROM_V1_SEGMENTS = True), placing each segment
at the offsets extract_beats.py computes from the constants below. This module
therefore carries the AUTHORITATIVE timeline (segment order, gaps, card) that the
V2 assembler reads; it is parsed, never executed.

SPEAKER LAW: narrator = Brian (modern English); Peter's quoted KJV, the crowd's
question and every scripture line = Roger (SCRIPTURE voice, light-blue captions).
Jesus does not speak here (post-Ascension). The closing card is a SILENT
invitation card (CARD_TEXT / CARD_DUR — no card mp3), like build-128.
"""
import make_narration  # noqa: F401  (SEGMENTS are read by extract_beats via AST)

# Caption text = verbatim spoken text, keyed by segment name.
TEXT = {s[0]: s[2] for s in make_narration.SEGMENTS}

# Scripture segments take the longer, reverent hold. Peter/crowd speak KJV here;
# they are apostolic words (light-blue), not Jesus red-letter, so the hold is
# reverent but not the full Jesus pause.
KJV = {"s1", "s2", "s3", "s4", "s5"}

# Timeline constants (read by extract_beats — never assumed).
LEAD = 0.28        # silent lead-in before each segment's voice
GAP = 0.72         # breath after a narrator segment
KJV_GAP = 1.15     # reverent hold after each scripture segment
TAIL = 1.5         # hold after the closing card

# Closing card: a SILENT invitation (no narration of its own — n6 already speaks
# the invitation). CARD_TEXT + CARD_DUR triggers extract_beats' silent-card path.
CARD_TEXT = "He kept his promise and poured out the Comforter.\nRepent, be baptized, and receive the gift of the Holy Ghost."
CARD_DUR = 6.5

# BEATS: (segment_name, still, zoom_dir). One entry per narration segment, in
# spoken order. The V2 build (beats_v2.py) hangs SEVERAL pictures on each of
# these audio windows; the still names here are nominal (V2 owns the pictures).
BEATS = [
    ("n1", "s1-they-waited-and-prayed.jpeg", "in"),
    ("s1", "s2-a-rushing-mighty-wind.jpeg", "in"),
    ("n2", "s3-every-nation-heard.jpeg", "out"),
    ("n3", "s4-peter-stood-up.jpeg", "in"),
    ("s2", "s5-crucified-and-slain.jpeg", "out"),
    ("n4", "s6-living-again.jpeg", "in"),
    ("s3", "s7-lord-and-christ.jpeg", "in"),
    ("n5", "s8-cut-to-the-heart.jpeg", "out"),
    ("s4", "s9-what-shall-we-do.jpeg", "in"),
    ("s5", "s10-repent-and-be-baptized.jpeg", "in"),
    ("n6", "s11-three-thousand-souls.jpeg", "out"),
]
