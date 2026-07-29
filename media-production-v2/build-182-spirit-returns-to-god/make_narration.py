#!/usr/bin/env python3
"""Narration for build-182-spirit-returns-to-god — Ecclesiastes 12.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

The one scripture beat was painted JESUS-RED and it is not Deity speaking at
all. Ecclesiastes is the Preacher - Solomon - writing, so this moves red ->
BLUE, not green:
  s1  Ecclesiastes 12:7  'Then shall the dust return to the earth as it was:
                          and the spirit shall return unto God who gave it.'
                                                          RED -> SCRIPTURE

This is the subtle case and it is easy to get wrong in the green direction. The
verse is entirely about God - the spirit goes back to him, he is the one who
gave it - but God is spoken OF, never speaking. Third person throughout: 'unto
God WHO GAVE it'. That is the man with the pen describing what happens, not
Deity announcing it. Green would have had God narrating a death he is receiving.

LIFTED ONE VERSE out of narrator paraphrase:
  s0  Ecclesiastes 12:1  'Remember now thy Creator in the days of thy youth,
                          while the evil days come not, nor the years draw
                          nigh, when thou shalt say, I have no pleasure in
                          them;'                             NEW, scripture
n0 was summarising the whole opening of Ecclesiastes 12 - the body growing old,
the days growing dim - without ever quoting the sentence that starts it. 12:1 is
the Preacher's actual instruction and it is what turns the chapter from a
lament into an invitation. Also the Preacher, so also blue. It sits on ST1 with
n0, so no new artwork.

ADDED n0b - a narrator retelling of Ecclesiastes 12:1, on ST2 ahead of n1.
Required by the retelling rule.

NO SPLIT anywhere. Both quoted lines are unbroken Preacher, one speaker each.

Nothing left as paraphrase from uncertainty; both are verbatim Ecclesiastes 12:1
and 12:7.

WHY-LAW: milk, and gently. The subject is death, so nothing here is dramatised.
The spirit goes home to the One who lent it - that is the whole message, and the
video lets it be rest rather than reckoning.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "The Teacher, Solomon, wrote honestly about the end of life. The body grows old, the days grow dim, and then — the breath leaves."),
    # Ecclesiastes 12:1
    ("s0", SCRIPTURE, "Remember now thy Creator in the days of thy youth, while the evil days come not, nor the years draw nigh, when thou shalt say, I have no pleasure in them;"),
    ("n0b", NARRATOR, "That is how he opens it. Remember your Maker while you are still young, he says — before the hard years arrive, before you get to the age where you say there is nothing in this for me anymore. He is not being grim. He is telling you not to wait."),
    ("n1", NARRATOR, "He did not leave it there in the dark. He pointed plainly to where the breath goes."),
    # Ecclesiastes 12:7
    ("s1", SCRIPTURE, "Then shall the dust return to the earth as it was: and the spirit shall return unto God who gave it."),
    ("n2", NARRATOR, "The body, made from dust, goes back to the ground. But the part of you that is from God goes home to Him."),
    ("n3", NARRATOR, "Death is not the end of the story. It is the spirit's quiet return to the One who lent it."),
    ("n4a", NARRATOR, "And the Giver who receives it back is the same Giver who first breathed it into you —"),
    ("n4b", NARRATOR, "— with mercy, not anger."),
    ("card", NARRATOR, "You were given breath by God. He is ready to receive it — and ready to give you more."),
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
