#!/usr/bin/env python3
"""Narration for build-179-stephens-witness — Acts 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

One red beat, misattributed. Jesus is standing in this story, but he never speaks —
every word quoted belongs to Stephen. So:

  s1  Acts 7:56  'Behold, I see the heavens opened, and the Son of man standing on
      the right hand of God.'  RED -> SCRIPTURE

One line out of red into light blue.

LIFTED FROM PARAPHRASE — the dying prayer:
  s60  Acts 7:60  NEW (scripture). n4a said only that 'his last words asked mercy for
       the ones throwing the stones', which is a summary of one of the most famous
       sentences in Acts. It is now spoken verbatim, on ST9 with n4a, and n4b
       ('Then he fell asleep') follows on ST8 exactly as it did before — which is
       itself Luke's own phrase, so the ending is unchanged.

This is Stephen's, not Christ's, and that matters: he prayed his Master's prayer from
the cross back at his own killers. Light blue is what lets a viewer feel the echo
instead of confusing the two men.

No splits — both quoted segments are single-speaker. Acts 7:56 and 7:60 are quoted
from the King James text as printed. Nothing left as paraphrase from uncertainty.

WHY-LAW: milk. You can face the worst thing that will ever happen to you with your
eyes on someone who is standing up for you, and with forgiveness still in your mouth.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, 'Stephen, full of the Holy Spirit, was dragged before the council for speaking the truth. He told them the whole story of Israel — and they boiled with rage.'),
    ("n1", NARRATOR, "But Stephen didn't look at his accusers. He looked up, and what he saw changed everything."),
    ("n2", NARRATOR, 'He saw the glory of God — and Jesus, standing at the right hand of the Father. And he said so, out loud:'),
    ("s1", SCRIPTURE, 'Behold, I see the heavens opened, and the Son of man standing on the right hand of God.'),
    ("n3a", NARRATOR, 'They would not hear it. They rushed him out.'),
    ("n3b", NARRATOR, "But Stephen's face was the face of an angel — at peace, not afraid. The court could condemn him, but it could not make him face death alone."),
    ("n4a", NARRATOR, 'Then he knelt down, with the stones still coming, and his last words asked mercy for the ones throwing them.'),
    ("s60", SCRIPTURE, 'Lord, lay not this sin to their charge.'),
    ("n4b", NARRATOR, "Don't hold this against them, he prayed. And then he fell asleep."),
    ("card", NARRATOR, 'He saw the Son of man standing to receive him. You can face your end with that same peace.'),
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
