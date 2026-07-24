#!/usr/bin/env python3
"""Narration for build-90-washing-feet — John 13.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, both exact:
  j1  John 13:8   'If I wash thee not, thou hast no part with me.'
  j2  John 13:14  'If I then, your Lord and Master, have washed your feet; ye
      also ought to wash one another's feet.'
Neither had John's framing welded on, so neither needed splitting. Ids kept.

PETER WAS NEVER HEARD. The hinge of this story is a man refusing to be served,
and his refusal was sitting inside n2 in modern English, in white. Lifted
verbatim as SCRIPTURE (light blue -- Peter is a man in the story, not Deity), on
ST4, the still already named 's4-peter-protests':
  s8  John 13:8  'Thou shalt never wash my feet.'
  n2 is trimmed to the frame only -- 'When he came to Peter, Peter pulled back.'
  -- and a new n2b carries the retelling and hands off to Jesus's answer.

RETELLINGS ADDED: n2c after 'no part with me', n3b after 'ye also ought'. Neither
Old English line was being said again in plain words.

CONSIDERED, LEFT OUT. John 13:9, Peter's swing to the other extreme -- 'Lord, not
my feet only, but also my hands and my head' -- is exact and it is charming. Left
out on judgment: it lightens a moment that should stay heavy, and ST4 is already
carrying three beats. The verse is exact if a later pass wants it.

NO GREEN: the Father does not speak in John 13:1-17.

WOMEN: John 13:1-17 records no woman speaking. Nothing added, nothing invented.

WHY-LAW: he took the job nobody in the room would take, and then told Peter that
being served by him is not optional. Milk: you cannot be his until you let him do
something for you.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "At that last supper, knowing he was about to leave the world, Jesus did something no master would ever do for his servants."),
    ("n1a", NARRATOR, "He got up from the table, wrapped a towel around his waist, and poured water into a basin."),
    ("n1b", NARRATOR, "And he began to wash his disciples' feet — one by one."),
    ("n2", NARRATOR, "When he came to Peter, Peter pulled back."),
    # John 13:8
    ("s8", SCRIPTURE, "Thou shalt never wash my feet."),
    ("n2b", NARRATOR, "Not you. Not for me. And Jesus answered him gently, but he did not back down."),
    # John 13:8
    ("j1", JESUS, "If I wash thee not, thou hast no part with me."),
    ("n2c", NARRATOR, "That is how serious this is. Peter thought he was protecting Jesus's dignity. What he was really doing was refusing to be loved."),
    ("n3", NARRATOR, "When he had finished, he dried their feet with the towel at his waist, sat back down, and asked if they understood what he had just done."),
    # John 13:14
    ("j2", JESUS, "If I then, your Lord and Master, have washed your feet; ye also ought to wash one another's feet."),
    ("n3b", NARRATOR, "Whatever he just did for them, they were to go do for each other."),
    ("n4", NARRATOR, "The greatest one in the room knelt at the dirtiest job in the house. That is the kind of king he is."),
    ("card", NARRATOR, "He kneels to serve the ones he loves. Will you let him near enough to do it for you?"),
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
