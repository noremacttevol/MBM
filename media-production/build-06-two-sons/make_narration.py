#!/usr/bin/env python3
"""Narration for build-06-two-sons — Matthew 21.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

PARABLE - SO IT ALL STAYS RED. This is the exception SPEAKER-LAW section 5 is
about: inside a parable the characters' words are Jesus's words, and a red-letter
KJV prints the father's line and both sons' lines red. Nothing inside the parable
became blue.

STAYED RED (existing):
  j1  Matthew 21:31  'Whether of them twain did the will of his father?'
  j2  Matthew 21:31  'Verily I say unto you, That the publicans and the harlots go
                      into the kingdom of God before you.'

ADDED, ALL RED - the parable itself was never actually spoken in this build. The
narrator told the story in modern English from end to end and Jesus only got the
two lines after it was over.
  j28  Matthew 21:28  'But what think ye? A certain man had two sons; and he came
                       to the first, and said, Son, go work to day in my vineyard.'
  j29  Matthew 21:29  'He answered and said, I will not.'      (first clause)
  j30  Matthew 21:30  'And he came to the second, and said likewise. And he
                       answered and said, I go, sir: and went not.'
  j29b Matthew 21:29  'but afterward he repented, and went.'   (second clause)
Verse 29 is deliberately split across the video the way the story is: the refusal
lands early, the turning lands where the build already puts it, at n2c/n2d. Both
halves are verbatim; neither is reworded, and nothing between them is invented.

MOVED OUT OF RED - one line, and it is the crowd, not Jesus:
  s31  Matthew 21:31  'They say unto him, The first.'  SCRIPTURE (blue). A
       red-letter KJV breaks red for exactly this clause and resumes at 'Verily I
       say unto you'. This is the mixed-verse split the law describes.

EDITS TO EXISTING NARRATOR TEXT: n1, n2 and n4 were trimmed where they used to
speak the parable's lines in modern English, since the red beats now speak them
and the narrator retells. n1b is a new retelling of the refusal. n5 gains one
opening sentence retelling s31, then continues word for word. n5b is a new
closing retelling after j2, which previously had nothing after it at all - the
video used to end on Old English with no landing.

WOMEN: Matthew 21:28-32 records no woman speaking. Nothing added; nothing
invented. ('Harlots' in j2 is Jesus naming them, not them speaking.)

NOT ADDED: Matthew 21:32, the John the Baptist explanation, is red and would be
legitimate, but it takes the video into meat and past its ending. Left out on
purpose, not by oversight.

WHY-LAW: the son who said no and went is the one who did his father's will. Milk
framing - God reads what you actually do, and a late yes still counts.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus told this story to religious leaders — people who were sure they had already said yes to God. He told it so they would hear themselves in it."),
    # Matthew 21:28
    ("j28", JESUS, "But what think ye? A certain man had two sons; and he came to the first, and said, Son, go work to day in my vineyard."),
    ("n1", NARRATOR, "A father told his first son: go work in the vineyard today. And the son answered him flat."),
    # Matthew 21:29
    ("j29", JESUS, "He answered and said, I will not."),
    ("n1b", NARRATOR, "I will not. No excuse offered, nothing softened. Just no."),
    ("n2", NARRATOR, "Then the father went to his second son and asked him the same thing."),
    # Matthew 21:30
    ("j30", JESUS, "And he came to the second, and said likewise. And he answered and said, I go, sir: and went not."),
    ("n2b", NARRATOR, "Yes sir, that one said. I'm going. And didn't."),
    ("n2c", NARRATOR, "The first son meant his no. But it wouldn't leave him alone. All morning, the vineyard kept pulling at him."),
    # Matthew 21:29
    ("j29b", JESUS, "but afterward he repented, and went."),
    ("n2d", NARRATOR, "So he got up. And he went. No announcement, no apology. He went back to the vineyard, and he worked."),
    ("n3", NARRATOR, "The row the second son promised to work stayed empty all day. Then Jesus asked the crowd a question."),
    # Matthew 21:31
    ("j1", JESUS, "Whether of them twain did the will of his father?"),
    ("n4", NARRATOR, "He was asking: which of the two actually did what his father wanted? And the crowd answered him."),
    # Matthew 21:31
    ("s31", SCRIPTURE, "They say unto him, The first."),
    ("n5", NARRATOR, "The first one, they said. The one who started with no. Then he turned to the religious leaders — the ones who were sure they were the second son."),
    # Matthew 21:31
    ("j2", JESUS, "Verily I say unto you, That the publicans and the harlots go into the kingdom of God before you."),
    ("n5b", NARRATOR, "The tax collectors and the worst-thought-of people in town are going in ahead of you. Not because their lives were tidier. Because when they finally heard, they turned around and went."),
    ("n6", NARRATOR, "Have you ever said no to something — maybe loudly — and found yourself moving toward it anyway, because part of you couldn't let it go?"),
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
