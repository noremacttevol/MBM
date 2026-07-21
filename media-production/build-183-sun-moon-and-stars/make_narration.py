#!/usr/bin/env python3
"""Narration for build-183-sun-moon-and-stars — 1 Corinthians 15.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

First Corinthians is a letter. Paul is writing to a congregation that asked him what
kind of body the dead rise with, and he answers them himself — Jesus is not quoted
anywhere in the passage. Both red beats are misattributions and both move:

  s1  1 Corinthians 15:41  'There is one glory of the sun, and another glory of the
      moon, and another glory of the stars: for one star differeth from another star
      in glory.'  RED -> SCRIPTURE
  s2  1 Corinthians 15:42  'So also is the resurrection of the dead. It is sown in
      corruption; it is raised in incorruption:'  RED -> SCRIPTURE

Two lines out of red into light blue. Nothing else changes.

No splits — both segments are Paul from end to end, no embedded speaker. Nothing
lifted from paraphrase: n0 through n4 are the storyteller's own framing and already
retell each quoted verse in modern English immediately after it. Both verses are
quoted from the King James text as printed; nothing left uncertain.

WHY-LAW: milk, and carefully so. The verse itself says there is more than one kind of
glory, and the video lets Paul say it without any Restoration vocabulary layered on
top. A Latter-day Saint hears the degrees of glory; everyone else hears a beautiful
true sentence about the sky. Neither one is misled. That is exactly the line this
library is supposed to walk.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "When Paul wrote about the resurrection, people asked him what kind of body the dead could possibly rise with. He answered by pointing at the sky."),
    ("n1", NARRATOR, "Look up, he said. Not everything that shines shines the same way. There are different kinds of bodies, and different kinds of glory."),
    # 1 Corinthians 15:41
    ("s1", SCRIPTURE, "There is one glory of the sun, and another glory of the moon, and another glory of the stars: for one star differeth from another star in glory."),
    ("n2", NARRATOR, "The sun has its own brightness. The moon has another. And no two stars burn quite alike. Then Paul said the astonishing part."),
    # 1 Corinthians 15:42
    ("s2", SCRIPTURE, "So also is the resurrection of the dead. It is sown in corruption; it is raised in incorruption:"),
    ("n3", NARRATOR, "That is what rising is like, he said. What goes into the ground breaks down; what comes back out never will again. The resurrection isn't one flat outcome. Like the lights above, there are glories — plural — and every one of them is a gift of light."),
    ("n4", NARRATOR, "The same God who hung the sun, the moon, and every different star is preparing a brightness for you."),
    ("card", NARRATOR, "The heavens hold more than one kind of glory. Reach for the brightest — you were made for light."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
