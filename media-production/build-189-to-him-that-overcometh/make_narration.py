#!/usr/bin/env python3
"""Narration for build-189-to-him-that-overcometh — Revelation 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both, and this is the build where that has to be said out loud,
because Revelation is not a Gospel.
  j1  Revelation 3:20  'Behold, I stand at the door, and knock: if any man hear my
      voice, and open the door, I will come in to him, and will sup with him, and
      he with me.'
  j2  Revelation 3:21  'To him that overcometh will I grant to sit with me in my
      throne, even as I also overcame, and am set down with my Father in his
      throne.'
Revelation red-letters Christ's explicit sayings, and the letters to the seven
churches are the clearest case of it — a red-letter King James Bible prints all
of chapter 3 red. Both of these are the risen Christ dictating to Laodicea, so
both are genuinely red and neither moves. John's visionary narration elsewhere in
the book would be `scripture`, but none of it is quoted here.

Both verses checked verbatim and left exactly as the build had them. NO SPLITS —
neither has John's framing welded on. Nothing lifted from paraphrase: n1 retells
verse 20 and n3 retells verse 21, so the retelling rule is already met.

ST5 is absent from the build's still vars; no beat uses it, and this plan does
not introduce one. The closing card is not a beat and has been left out of BEATS,
exactly as the original had it.

WHY-LAW: milk. He knocks, he does not break the door, and the throne is shared
rather than earned. The whole build turns on a latch you get to lift yourself.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "To a church that had grown comfortable and half-asleep, Jesus sent a knock at the door — not a storm, just a knock."),
    # Revelation 3:20
    ("j1", JESUS, "Behold, I stand at the door, and knock: if any man hear my voice, and open the door, I will come in to him, and will sup with him, and he with me."),
    ("n1", NARRATOR, "He does not break the door. He waits to be invited in."),
    ("n2", NARRATOR, "And to the one who opens, who keeps opening, he promises a seat no empire can give."),
    # Revelation 3:21
    ("j2", JESUS, "To him that overcometh will I grant to sit with me in my throne, even as I also overcame, and am set down with my Father in his throne."),
    ("n3", NARRATOR, "The one who overcomes doesn't earn a throne by being flawless. He shares the one Christ already won."),
    ("card", NARRATOR, "He is knocking right now. Open, and you will eat with him — and reign with him."),
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
