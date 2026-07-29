#!/usr/bin/env python3
"""Assemble canonical video #133, What Jesus Called Hell (Mark 9:43-48).

Historically grounded BRIDGE cut: Gehenna is tied to the Valley of Hinnom and
the prophetic history of Topheth.  It does not repeat the unsupported modern
claim that the valley was Jerusalem's continuously burning garbage dump.
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
    ("n0", "s1-inherited-fear.png", "in"),
    ("n1", "s2-city-valley.png", "in"),
    ("n2", "s2-city-valley.png", "out"),
    ("n3", "s4-jesus-teaches.png", "in"),
    ("j1", "s4-jesus-teaches.png", "out"),
    ("j2", "s5-release-rope.png", "in"),
    ("j3", "s5-release-rope.png", "out"),
    ("n4", "s8-warning-love.png", "in"),
    ("n5", "s1-inherited-fear.png", "out"),
    ("n6", "s10-shepherd.jpeg", "in"),
]


if __name__ == "__main__":
    render(
        output="mark-9_what-jesus-called-hell.mp4",
        beats=BEATS,
        text=TEXT,
        speaker=SPEAKER,
        hold={"j3": 1.80},
    )

