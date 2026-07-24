#!/usr/bin/env python3
"""Narration for build-128-famine-of-hearing — Amos 8.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Second video on Amos 8, judged independently of build-156. Same two verses, same doctrinal call, different cut — this one is shorter, tighter, and runs the two verses back to back on ST3.

  s1  Amos 8:11  god (was red)
  s2  Amos 8:12  god (was red)

Amos 8:11-12 is one continuous oracle in the LORD's own first-person voice: 'I will send a famine in the land'. Jehovah, the premortal Christ, so GREEN. A red-letter KJV prints none of it red — Christ had not yet come in the flesh.

s1 carries 'saith the Lord GOD', Amos's attribution clause, wrapped around God's own words. NOT split, for the same reason as build-156: pulling three words of attribution into their own blue beat would chop the line in half and read worse than it sounds now. The segment as a whole is God speaking.

s1 and s2 run consecutively with no narrator between them. Left that way on purpose — they are one unbroken oracle and the pause would kill it. n2 does the retelling for both, which is what the retelling rule is for.

Nothing lifted or added. This cut is deliberately spare and the narrator beats are short; adding verses would fight the pacing.

WHY-LAW: the famine is the silence we choose. The cure was never far off — it was to listen while the voice could still be heard.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, "The prophet Amos carried a warning from the Lord —"),
    ("n0b", NARRATOR, "not about food, but about something people would miss even more."),
    ("n1", NARRATOR, "A day would come when God's voice would seem far away — not because He stopped speaking, but because people stopped being able to hear."),
    # Amos 8:11
    ("s1", GOD, "Behold, the days come, saith the Lord GOD, that I will send a famine in the land, not a famine of bread, nor a thirst for water, but of hearing the words of the LORD:"),
    # Amos 8:12
    ("s2", GOD, "And they shall wander from sea to sea, and from the north even to the east, they shall run to and fro to seek the word of the LORD, and shall not find it."),
    ("n2", NARRATOR, "The deepest hunger isn't in the stomach. It's the ache of a soul that can't find a word from God."),
    ("n3a", NARRATOR, "The cure was never far."),
    ("n3b", NARRATOR, "It was to listen while His voice could still be heard."),
    ("card", NARRATOR, "When His word is near, don't let it pass. Listen now — the famine is the silence we choose."),
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
