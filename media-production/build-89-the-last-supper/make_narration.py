#!/usr/bin/env python3
"""Narration for build-89-the-last-supper — Luke 22.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, both exact and both correctly his:
  j1  Luke 22:19  'This is my body which is given for you: this do in
      remembrance of me.'
  j2  Luke 22:20  'This cup is the new testament in my blood, which is shed for
      you.'
Neither carried Luke's framing welded on, so neither needed splitting. Ids kept.

RED ADDED -- two of his sayings in this room were only paraphrased:
  jv15 Luke 22:15  'With desire I have desired to eat this passover with you
       before I suffer.'  -- n1 said 'he told them plainly: he had wanted this
       meal with them.' That sentence is one of the most tender things he says
       all week and it was in white. n1 keeps its id and now retells it.
  jv18 Luke 22:18  'For I say unto you, I will not drink of the fruit of the
       vine, until the kingdom of God shall come.'  -- n4 reported it in modern
       English. n4 keeps its id and its first sentences are now the retelling.

RETELLINGS ADDED: n2b after the bread, n3b after the cup. Both were missing --
the video quoted the sacrament in Old English and then moved straight on.

NO GREEN: the Father does not speak in Luke 22:14-20.

WOMEN: Luke 22:14-20 records no woman speaking; the upper room is the twelve.
Nothing added, nothing invented.

CONSIDERED, LEFT OUT. Luke 22:21-22, 'the hand of him that betrayeth me is with
me on the table,' is red and it is in this chapter. Left out: it turns a video
about the gift into a video about the betrayal, and it needs meat-level context
about Judas to land. Reverence over completeness.

WHY-LAW: on the last night he had, he gave them something to hold. Milk: the
sacrament is not a ritual he left behind, it is the table he still hosts.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0a", NARRATOR, "The Passover had come."),
    ("n0b", NARRATOR, "Jesus gathered his closest friends around one table in an upper room, knowing the night would change everything."),
    # Luke 22:15
    ("jv15", JESUS, "With desire I have desired to eat this passover with you before I suffer."),
    ("n1", NARRATOR, "I have wanted this meal with you, he told them — wanted it badly — before the hard thing happens. He knew what was coming that night, and what he wanted first was to sit down and eat with his friends."),
    ("n2", NARRATOR, "Then he took the bread, gave thanks, broke it, and gave it to them."),
    # Luke 22:19
    ("j1", JESUS, "This is my body which is given for you: this do in remembrance of me."),
    ("n2b", NARRATOR, "This is my body, he said, and it is given for you. Do this to remember me. Not a symbol he was explaining — a gift he was handing over, piece by piece, into their hands."),
    ("n3", NARRATOR, "After the meal he lifted the cup, and gave it to them, too."),
    # Luke 22:20
    ("j2", JESUS, "This cup is the new testament in my blood, which is shed for you."),
    ("n3b", NARRATOR, "A brand new promise between God and people, and he was signing it with his own life."),
    # Luke 22:18
    ("jv18", JESUS, "For I say unto you, I will not drink of the fruit of the vine, until the kingdom of God shall come."),
    ("n4", NARRATOR, "He was telling them this was not goodbye — it was see you at the next meal. Then he and his friends sang together and walked out into the night."),
    ("n5", NARRATOR, "The bread and the cup, still on the table — a gift to remember him by."),
    ("card", NARRATOR, "He left a simple meal to remember him by. Come to his table — he is still the host."),
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
