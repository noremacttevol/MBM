#!/usr/bin/env python3
"""Narration for build-163-apostles-prophets — Ephesians 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Ephesians is an epistle — Paul writing to the saints at Ephesus. A red-letter
King James Bible prints no red in Ephesians 2. Both red beats move to
SCRIPTURE (light blue):
  kv19  Ephesians 2:19  'Now therefore ye are no more strangers...'  RED -> SCRIPTURE
  kv20  Ephesians 2:20  'And are built upon the foundation...'       RED -> SCRIPTURE

kv20 names Jesus Christ but does not quote him — 'Jesus Christ himself being
the chief corner stone' is Paul describing him in the third person. Being about
Christ is not the same as being spoken by Christ, and that distinction is
exactly what the red was getting wrong here.

No mixed segments, nothing split. No verses lifted — n4 through n7 already
retell both quotations in plain English.

WHY-LAW: milk. Apostles and prophets are the foundation and Christ is the
cornerstone — stated as Paul stated it, with no argument attached about who
holds those offices now. The viewer is simply told there is a blueprint, and
that there is a place in the house for them.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "The people Paul was writing to had once been outsiders — foreigners, strangers, on the far edge of God's promises, with no place at the table and no share in the family."),
    ("n2", NARRATOR, "But something had changed everything. The door had been thrown open, and those who were far off had been brought near — no longer guests to be tolerated, but family to be embraced."),
    ("n3", NARRATOR, "Paul reached for a beautiful picture: they were now part of a household — the very household of God. Not a crowd of strangers passing through, but sons and daughters at home, belonging."),
    # Ephesians 2:19
    ("kv19", SCRIPTURE, "Now therefore ye are no more strangers and foreigners, but fellowcitizens with the saints, and of the household of God;"),
    ("n4", NARRATOR, "But a household needs a house — and a house needs to be built, and built right. So Paul changed the picture from a family to a building, the dwelling place of God among his people."),
    ("n5", NARRATOR, "Every real building rests on a foundation. And this one, Paul said, was laid on the apostles and the prophets — men God had called and taught, whose witness became the solid ground the whole structure would stand on."),
    ("n6", NARRATOR, "And at the most important place of all — the cornerstone, the stone that sets the angle, holds two walls together, and keeps the whole building square and true — stood Christ himself. Everything is lined up to him."),
    # Ephesians 2:20
    ("kv20", SCRIPTURE, "And are built upon the foundation of the apostles and prophets, Jesus Christ himself being the chief corner stone;"),
    ("n7", NARRATOR, "So the church was never meant to be a loose, shapeless crowd. It has a design — a foundation of apostles and prophets, a cornerstone that is Christ, and living people fitted together into a home for God. There is a blueprint."),
    ("n8", NARRATOR, "And the best part is where that leaves you. You are not a stranger at the door. In this house you have a place, fitted in and belonging, part of what God is building. So the only question is a hopeful one. When he offers you a place in it, will you come inside?"),
    ("card", NARRATOR, "You are no longer a stranger, but part of the household of God — a building laid on apostles and prophets, with Christ the cornerstone holding it all together. When he offers you a place in it, will you come inside?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
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
