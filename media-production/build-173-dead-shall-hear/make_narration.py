#!/usr/bin/env python3
"""Narration for build-173-dead-shall-hear — John 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: all three, and nothing moved.
  j1a  John 5:25  'Verily, verily, I say unto you, The hour is coming, and now is,'
  j1b  John 5:25  'when the dead shall hear the voice of the Son of God:'
  j1c  John 5:25  'and they that hear shall live.'
Gospel, Jesus in the flesh, red-letter. The build had already broken John 5:25
into three beats for pacing — that is one red sentence cut three ways for the
edit, not three speakers, so all three are red. Checked against the King James
text: the three join back into verse 25 word for word with nothing lost at the
seams.

NO SPLITS NEEDED. There is no evangelist frame anywhere in the quoted material —
'Verily, verily' is Christ's own opening word, not John introducing him — so the
red starts at the first syllable of j1a.

Nothing lifted from paraphrase. n0 and n1 set the verse up and n2a and n2b retell
it after, which is the retelling rule already met. j1a, j1b and j1c touch each
other with no narrator between them; the validator will warn twice about that.
The warnings are wrong to act on here — this is one sentence by one speaker, and
putting the storyteller inside it would break the line in half.

The closing card is not a beat in this build and has been left out of BEATS,
exactly as the original had it.

WHY-LAW: milk. The resurrection is offered as a voice you can already hear, not
as a doctrine to be defended. Short, quiet, and it ends on listening. 2026-07-21: added j2 (John 5:28-29, red) + n2c retelling on still S6 — the cut was 48.8s, under the 60s floor (RULE-CONFLICTS case); the addition is the passage's own next verse.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus said a time was coming — and had already begun — when something impossible would happen."),
    ("n1", NARRATOR, "The dead would hear a voice. Not a rumor of a voice. His voice."),
    # John 5:25
    ("j1a", JESUS, "Verily, verily, I say unto you, The hour is coming, and now is,"),
    # John 5:25
    ("j1b", JESUS, "when the dead shall hear the voice of the Son of God:"),
    # John 5:25
    ("j1c", JESUS, "and they that hear shall live."),
    ("n2a", NARRATOR, "The One who made life is the One who calls it back."),
    # John 5:28-29
    ("j2", JESUS, "Marvel not at this: for the hour is coming, in the which all that are in the graves shall hear his voice, and shall come forth."),
    ("n2c", NARRATOR, "Not some of the dead. All of them. He said every grave will hear that same voice — and open. Nobody is too far gone, and nobody gets left in the ground."),
    ("n2b", NARRATOR, "To hear him is to live."),
    ("card", NARRATOR, "He speaks, and death loses its grip. Lean in and listen — and live."),
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
