#!/usr/bin/env python3
"""Narration for build-88-triumphal-entry — Matthew 21.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

BOTH RED BEATS WERE WRONG, AND NEITHER WAS JESUS. This build painted the
crowd red.
  j1  Matthew 21:9  'Hosanna to the son of David...' -- that is the MULTITUDE
      shouting, not Jesus. A red-letter KJV leaves it black. Moved to SCRIPTURE
      (light blue). Id kept.
  j2  Matthew 21:10-11 'And when he was come into Jerusalem, all the city was
      moved, saying, Who is this? And the multitude said, This is Jesus the
      prophet of Nazareth of Galilee.' -- that is Matthew writing, with the
      crowd quoted inside it. Both halves are blue, so no split is needed for
      colour; it stays one beat as SCRIPTURE. Id kept.

RED ADDED -- HE NEVER SPOKE IN HIS OWN ENTRY. Jesus has exactly one speech in
Matthew 21:1-11 and it was sitting inside n0a's paraphrase. Lifted verbatim onto
ST1, the still already named 's1-go-into-the-village':
  jv2  Matthew 21:2-3  'Go into the village over against you, and straightway ye
       shall find an ass tied, and a colt with her: loose them, and bring them
       unto me. And if any man say ought unto you, ye shall say, The Lord hath
       need of them; and straightway he will send them.'
  n0a2 carries the retelling.

PROPHECY LIFTED. n0b said only 'It was exactly as the old prophecy had said' and
never said it. Matthew 21:5 quotes Zechariah, so it is Matthew writing --
SCRIPTURE, not god:
  s5  Matthew 21:5  'Tell ye the daughter of Sion, Behold, thy King cometh unto
      thee, meek, and sitting upon an ass, and a colt the foal of an ass.'
  n1b already retells this exactly ('The King was coming -- but not the kind they
  expected'), so it was left alone and simply follows the verse.

NO GREEN: the Father does not speak in Matthew 21:1-11.

WOMEN: Matthew 21:1-11 records no woman speaking. Nothing added, nothing invented.

WHY-LAW: the crowd's own words name him King, and the King they were shouting for
rode in on a borrowed farm animal. Milk: his kingdom arrives quietly, and you are
welcome in it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, "As Jesus came near Jerusalem, he sent two disciples ahead into the village with a strange errand."),
    # Matthew 21:2-3
    ("jv2", JESUS, "Go into the village over against you, and straightway ye shall find an ass tied, and a colt with her: loose them, and bring them unto me. And if any man say ought unto you, ye shall say, The Lord hath need of them; and straightway he will send them."),
    ("n0a2", NARRATOR, "Go into the village, he told them. Untie them and bring them to me. And if anyone asks why, just say the Lord needs them — and he'll let them go."),
    ("n0b", NARRATOR, "They went, and it happened exactly as he said. And all of it was exactly as the old prophecy had said, too."),
    # Matthew 21:5
    ("s5", SCRIPTURE, "Tell ye the daughter of Sion, Behold, thy King cometh unto thee, meek, and sitting upon an ass, and a colt the foal of an ass."),
    ("n1b", NARRATOR, "The King was coming — but not the kind they expected."),
    ("n1a", NARRATOR, "The crowds spread their cloaks on the road, and cut branches from the trees, and lined his path."),
    ("n2", NARRATOR, "And the people shouted as he rode in:"),
    # Matthew 21:9
    ("j1", SCRIPTURE, "Hosanna to the son of David: Blessed is he that cometh in the name of the Lord; Hosanna in the highest."),
    ("n2b", NARRATOR, "Hosanna means save us now. They were calling him King out loud, in the street, where everyone could hear it."),
    ("n3", NARRATOR, "The whole city was stirred. When they asked who this was, the crowd answered plainly."),
    # Matthew 21:10-11
    ("j2", SCRIPTURE, "And when he was come into Jerusalem, all the city was moved, saying, Who is this? And the multitude said, This is Jesus the prophet of Nazareth of Galilee."),
    ("n3b", NARRATOR, "Who is this? the city asked. And the answer came back from the road — this is Jesus, the prophet, out of Nazareth in Galilee."),
    ("n4", NARRATOR, "He came not with swords but with peace — riding on a donkey, the humble King the scriptures had promised."),
    ("card", NARRATOR, "The King rode in on a donkey, not a warhorse. His kingdom is peace. You're welcome in it."),
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
