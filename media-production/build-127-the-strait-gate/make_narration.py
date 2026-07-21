#!/usr/bin/env python3
"""Narration for build-127-the-strait-gate — Matthew 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both j1 and j2 are Jesus preaching in the flesh in the Sermon on the
Mount, and a red-letter KJV inks both. Neither carries evangelist framing, so
neither needed splitting.
  j1  Matthew 7:13
  j2  Matthew 7:14

THE FIX: the two red verses ran back to back with no storyteller between them,
and the two narrator beats that explain them (n1, n2) sat BEFORE the verses
instead of after. The viewer got the plain-English version first and the King
James second, which is backwards - the retelling rule wants the Old English to
land and then be made plain.

Nothing was rewritten. n1 and n2 were already near-perfect retellings of 7:13 and
7:14; they were simply moved to follow the verses they explain. It now reads
verse, retelling, verse, retelling.

ADDED: n4, a short closing narrator beat, so the video ends on S7 ('step through')
instead of leaving that still unused. All seven stills are now in the running
order; the original build used only six.

WOMEN: Matthew 7:13-14 records no woman speaking. Nothing added.

WHY-LAW: he did not describe two roads to frighten anybody. He described them
because one of them is worth finding, and finding it is a decision, not an
accident.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus stood before the crowd and described two roads — two ways that every person gets to choose."),
    # Matthew 7:13
    ("j1", JESUS, "Enter ye in at the strait gate: for wide is the gate, and broad is the way, that leadeth to destruction, and many there be which go in thereat:"),
    ("n1", NARRATOR, "One road looks easy. The gate is wide, the path is broad, and a lot of people walk that way."),
    # Matthew 7:14
    ("j2", JESUS, "Because strait is the gate, and narrow is the way, which leadeth unto life, and few there be that find it."),
    ("n2", NARRATOR, "The other road looks harder. The gate is narrow, the path is tight, and far fewer find it."),
    ("n3a", NARRATOR, "He wasn't describing geography. He was describing a decision."),
    ("n3b", NARRATOR, "A narrow gate that leads to life, found by the few who choose it."),
    ("n4", NARRATOR, "He never said the narrow way would be crowded. He said it leads to life. Both gates are standing open right now, and nobody walks through either one by accident."),
    ("card", NARRATOR, "There are two gates, and one choice. He said the narrow way is worth finding. Step through."),
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
