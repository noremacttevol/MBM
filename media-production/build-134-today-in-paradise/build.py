#!/usr/bin/env python3
"""Assemble canonical video #134, Today Shalt Thou Be with Me in Paradise.

BRIDGE cut using Luke 23:42-43 and John 20:17, with speaker identity controlling
both narration voice and caption color.  Crucifixion imagery remains non-graphic.
"""

import os
import sys

import make_narration

MEDIA_PRODUCTION = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if MEDIA_PRODUCTION not in sys.path:
    sys.path.insert(0, MEDIA_PRODUCTION)

from mbm_still_video import render


TEXT = {segment[0]: segment[2] for segment in make_narration.SEGMENTS}
SPEAKER = {segment[0]: segment[1] for segment in make_narration.SEGMENTS}

BEATS = [
    ("n0", "s1-two-doors.png", "in"),
    ("n1", "s2-three-crosses.jpeg", "in"),
    ("s1", "s3-thief-hope.jpeg", "in"),
    ("j1", "s4-promise.png", "in"),
    ("n2", "s4-promise.png", "out"),
    ("n3", "s6-mary-tomb.jpeg", "in"),
    ("j2", "s7-not-yet-ascended.png", "in"),
    ("n4", "s7-not-yet-ascended.png", "out"),
    ("n5", "s9-paradise.png", "in"),
]


if __name__ == "__main__":
    render(
        output="luke-23_today-in-paradise.mp4",
        beats=BEATS,
        text=TEXT,
        speaker=SPEAKER,
        hold={"j1": 1.80, "j2": 1.80},
    )

