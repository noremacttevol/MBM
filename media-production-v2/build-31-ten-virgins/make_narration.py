#!/usr/bin/env python3
"""Narration for build-31-ten-virgins — Matthew 25.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Matthew 25:1-13. A parable, so a red-letter KJV inks the whole of it - the
midnight cry, the foolish, the wise and the bridegroom are all Jesus's own words.
j1 stays RED and five more lines that the video only paraphrased are lifted out and
join it in red:
  j2  Matthew 25:6   'Behold, the bridegroom cometh; go ye out to meet him.'
  j3  Matthew 25:8   'Give us of your oil; for our lamps are gone out.'
  j4  Matthew 25:9   'Not so; lest there be not enough for us and you...'
  j5  Matthew 25:11  'Lord, Lord, open to us.'
  j6  Matthew 25:12  'Verily I say unto you, I know you not.'
The ten women are NOT `woman` beats - they are characters in a story Jesus is
telling, so the words are his and the Bible prints them red. Pink is reserved for
women the Bible records actually speaking. still_vars S1..S7 introduced.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus told a story about ten young women waiting for a wedding."),
    ("n1", NARRATOR, "In those days, a whole village would wait for the bridegroom to come, late in the evening, and lead everyone in to the feast."),
    ("n2", NARRATOR, "So ten young women took their oil lamps and went out into the dusk to meet him."),
    ("n3", NARRATOR, "Five of them were wise. Along with their lamps, they each carried a small jar of extra oil."),
    ("n4", NARRATOR, "The other five were foolish. They brought their lamps — but no extra oil at all."),
    ("n5", NARRATOR, "The bridegroom was delayed. Hour after hour slipped by, and one by one, all ten women grew drowsy and fell asleep."),
    # Matthew 25:6
    ("j2", JESUS, "Behold, the bridegroom cometh; go ye out to meet him."),
    ("n6", NARRATOR, "Then, at midnight, a cry rang out: The bridegroom is coming! Come out to meet him!"),
    ("n7", NARRATOR, "They all woke and reached for their lamps. The wise trimmed theirs, and they burned warm and bright."),
    ("n8", NARRATOR, "But the foolish looked down in dismay. Their lamps were sputtering out — they had no oil left."),
    # Matthew 25:8
    ("j3", JESUS, "Give us of your oil; for our lamps are gone out."),
    ("n9", NARRATOR, "Please, they cried out to the others — give us some of your oil!"),
    # Matthew 25:9
    ("j4", JESUS, "Not so; lest there be not enough for us and you: but go ye rather to them that sell, and buy for yourselves."),
    ("n10", NARRATOR, "But the wise couldn't. There isn't enough for all of us, they said. Hurry — go and buy your own."),
    ("n11", NARRATOR, "And while the foolish rushed off into the dark to find oil, the bridegroom arrived."),
    ("n12", NARRATOR, "The ones who were ready went in with him to the wedding feast. And the door was shut."),
    # Matthew 25:11
    ("j5", JESUS, "Lord, Lord, open to us."),
    # Matthew 25:12
    ("j6", JESUS, "Verily I say unto you, I know you not."),
    ("n13", NARRATOR, "Later the others came back, knocking. Lord, they called, open the door for us! But the answer came from inside: I do not know you."),
    ("n14", NARRATOR, "Then Jesus told them why he had shared this story."),
    # Matthew 25:13
    ("j1", JESUS, "Watch therefore, for ye know neither the day nor the hour wherein the Son of man cometh."),
    ("n15", NARRATOR, "The oil is the one thing you cannot borrow at the last minute — a heart that is truly ready, a faith that is really your own, a lamp you have kept burning."),
    ("n16", NARRATOR, "And here is the good news: the door is still open now. Tonight, your lamp can be filled. He is worth being ready for."),
    ("card", NARRATOR, "You cannot borrow someone else's oil. Is your own lamp burning — are you ready to meet him?"),
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
