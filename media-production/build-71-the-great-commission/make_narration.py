#!/usr/bin/env python3
"""Narration for build-71-the-great-commission — Matthew 28:16-20.

NEW STORY (Cameron, 2026-07-22): replaces the retired #71 calling-the-fishermen
duplicate (same calling event as #51). Cameron picked the Great Commission as the
milk story the restored-gospel Jesus would most want in the mix and that the
catalog obviously lacked: the risen Christ's final command to take the gospel to
all nations — the charter of missionary work, the true Godhead named plainly
(Father, Son, AND Holy Ghost, three), baptism by authority, and the promise that
carries it, "lo, I am with you alway."

SPEAKER-LAW: JESUS (red, verbatim red-letter KJV) speaks 28:18-20; NARRATOR
(white, modern) carries the setting and the retelling. Nobody else speaks here.

FACE-LAW: this is the RISEN Christ and the risen-jesus sheet is not yet rendered
or approved (CHARACTER-LAW age-variant, rule 7), so every still stages Jesus from
BEHIND / over-the-shoulder / at DISTANCE — the eleven's faces carry the scene.
jesus_face_gate.py must pass. If Cameron later wants his face shown here, render
the risen-jesus sheet first, then regenerate the Jesus stills.

RETELLING RULE: every red beat (jv18/jv19/jv20) is followed by the storyteller
saying it again in plain English (n3/n4/n5).

MILK: you were worth going to the ends of the earth for.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled. JESUS lines are verbatim KJV (Matt 28).
SEGMENTS = [
    ("n1", NARRATOR, 'He had been crucified. He had been buried. And now he was alive, and it was almost over. Before he returned to his Father, he gathered the eleven one last time, on a mountain in Galilee he had told them to go to.'),
    ("n2", NARRATOR, 'They climbed it not really knowing what to expect. And when they saw him standing there, alive, they fell down and worshipped him. Some of them still could hardly believe it was real. He did not scold the doubt. He gave them the whole world anyway.'),
    ("jv18", JESUS, 'All power is given unto me in heaven and in earth.'),
    ("n3", NARRATOR, 'Every authority there is, in heaven and on the earth, belongs to him. Whatever he was about to ask of them, he had the right to ask it, and the power to back it.'),
    ("jv19", JESUS, 'Go ye therefore, and teach all nations, baptizing them in the name of the Father, and of the Son, and of the Holy Ghost:'),
    ("n4", NARRATOR, 'Go to everyone. Not one nation, not one kind of person, but all of them, to the far edges of the map, and bring them in through baptism. And hear the three he names together, plainly, one breath apart: Three.'),
    ("jv20", JESUS, 'Teaching them to observe all things whatsoever I have commanded you: and, lo, I am with you alway, even unto the end of the world. Amen.'),
    ("n5", NARRATOR, 'Teach them not just to hear it but to live it, everything he had shown them. And then the promise that holds the whole thing up. I am with you always. Not until it gets hard. Not until you fail. Always, to the very end.'),
    ("n6", NARRATOR, 'That command has never stopped moving. Every person who ever told you about Jesus was standing in the long tail of that one sentence on that mountain. It reached across two thousand years and the whole round earth to get to you. That is how far he was willing to send someone, so that you would know.'),
    ("card", NARRATOR, 'He looked at eleven ordinary men, some of them still unsure, and trusted them with everyone. If it really is true that he is with you always, to the very end, what would that change about today?'),
]

# Homographs / archaic words this build decides for itself (A/B tested only).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN, speaker), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
