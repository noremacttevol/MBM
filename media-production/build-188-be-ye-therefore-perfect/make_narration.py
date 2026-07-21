#!/usr/bin/env python3
"""Narration for build-188-be-ye-therefore-perfect — Matthew 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: all three, and nothing moved.
  j1  Matthew 5:44  'But I say unto you, Love your enemies, bless them that curse
      you, do good to them that hate you, and pray for them which despitefully use
      you, and persecute you;'
  j2  Matthew 5:45  'That ye may be the children of your Father which is in
      heaven: for he maketh his sun to rise on the evil and on the good, and
      sendeth rain on the just and on the unjust.'
  j3  Matthew 5:48  'Be ye therefore perfect, even as your Father which is in
      heaven is perfect.'
Gospel, Jesus in the flesh on the mount, red-letter all three, and all three
already verbatim. NO SPLITS — none of them has Matthew's narration welded on.

ADDED, one narrator beat:
  n0b  a plain-English retelling of Matthew 5:44.
j1 and j2 ran back to back with nothing between them, so the viewer got two full
blocks of King James before anyone explained the first one. The retelling rule
says every Old English line gets said again in modern English, and verse 44 was
the one going unretold — n1 only carries verse 45. n0b sits on ST2 with j1, a
still the build already has, so no new artwork and no lost beat.

Companion to build-124-love-your-enemies, which covers verses 43 through 46. The
calls agree: 44 and 45 are red in both. Verse 43, which 124 lifts out, is NOT
imported here — this build runs to verse 48 instead and adding it would crowd the
front of a short piece.

WHY-LAW: milk. 'Be ye therefore perfect' is handed over as an invitation to grow
into, with the Father's indiscriminate sun as the picture of what it means. No
guilt, no ladder, no scoring.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus sat on the hillside and taught the crowds a kind of love they had never heard before — not just for friends, but for enemies too."),
    # Matthew 5:44
    ("j1", JESUS, "But I say unto you, Love your enemies, bless them that curse you, do good to them that hate you, and pray for them which despitefully use you, and persecute you;"),
    ("n0b", NARRATOR, "Love your enemies, he said. Bless the ones who curse you. Do good to the ones who hate you, and pray for the people who use you badly. Not put up with them. Not stay out of their way. Love them, and mean it."),
    # Matthew 5:45
    ("j2", JESUS, "That ye may be the children of your Father which is in heaven: for he maketh his sun to rise on the evil and on the good, and sendeth rain on the just and on the unjust."),
    ("n1", NARRATOR, "The point was simple and hard at once — God's kindness falls on everyone, the grateful and the cruel alike."),
    ("n2", NARRATOR, "Then he set the bar that no one could reach alone, and meant for us to run toward it."),
    # Matthew 5:48
    ("j3", JESUS, "Be ye therefore perfect, even as your Father which is in heaven is perfect."),
    ("n3", NARRATOR, "Not perfect by comparison with each other. Perfect by the measure of a Father whose love has no edge, no favor, no limit."),
    ("card", NARRATOR, "He asks for a love without limits — and he gives the grace to grow into it. Come and learn it from him."),
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
