#!/usr/bin/env python3
"""Narration for build-29-pearl — Matthew 13.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED -- AND NOTHING ELSE CHANGED. Both existing red beats are Jesus in the
flesh telling a parable, both were checked word for word against the KJV, and both
are exactly verbatim. A red-letter KJV prints both:
  j1  Matthew 13:45  'Again, the kingdom of heaven is like unto a merchant man,
      seeking goodly pearls:'
  j2  Matthew 13:46  'Who, when he had found one pearl of great price, went and sold
      all that he had, and bought it.'

NO FRAMING SPLIT NEEDED -- and this is worth stating, because it is the one place
this set differs from its neighbours. 'Again' at the head of verse 45 is not
Matthew's framing. It is Jesus's own word, continuing the run of parables he is
already speaking (compare 13:44, 'Again, the kingdom of heaven is like unto treasure
hid in a field'). A red-letter KJV inks it red along with the rest of the verse.
There is no evangelist's 'and he said unto them' anywhere in 13:45-46 to lift out,
so nothing was split. Both beats stay whole and stay red.

NOTHING LIFTED. This parable is two verses long and the build already speaks BOTH of
them verbatim, each with the storyteller's retelling right behind it -- j1 then n2,
j2 then n6. That is exactly the shape SPEAKER-LAW asks for; it was already right.
Every remaining segment is the storyteller's own application (the merchant's gladness,
and the turn at n9-n10 where you are the pearl and Christ is the merchant). That is
narrator work in modern English and it correctly stays white.

NO GREEN: no voice from heaven in Matthew 13. No one else speaks in the passage, so
nothing moved to `scripture` either.

WOMEN: Matthew 13:45-46 records no woman speaking, and no woman appears in the
parable. Nothing added; nothing invented.

PRONUNCIATION: nothing on the homograph list appears in either KJV line. 'goodly'
and 'merchant man' read correctly as written. No respellings.

WHY-LAW: read forward, letting go of everything is the easiest trade you will ever
make. Read backward, HE is the merchant, you are the pearl, and he gave everything he
had -- gladly -- to buy you back.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Jesus told one more short story, only two lines long."),
    # Matthew 13:45
    ("j1", JESUS, "Again, the kingdom of heaven is like unto a merchant man, seeking goodly pearls:"),
    ("n2", NARRATOR, "This was a man who knew pearls. He spent his whole life traveling and searching, handling the finest pearls in the world, always hunting for something better."),
    ("n3", NARRATOR, "He had seen a lot of beautiful pearls. Good ones. Costly ones. But he kept looking, because not one of them was the one."),
    ("n4", NARRATOR, "And then one day, he found it. A single pearl, more perfect and more precious than anything he had ever held. The pearl he had been looking for his whole life."),
    ("n5", NARRATOR, "And he knew, the moment he saw it, exactly what he was going to do."),
    # Matthew 13:46
    ("j2", JESUS, "Who, when he had found one pearl of great price, went and sold all that he had, and bought it."),
    ("n6", NARRATOR, "He went home and sold everything. His house, his goods, every other pearl he owned. All of it, gone, to buy the one."),
    ("n7", NARRATOR, "And here is the thing. He did not do it grieving. He did not feel robbed. He gave up everything he had, gladly, because what he was getting was worth more than all of it put together."),
    ("n8", NARRATOR, "That is what finding the real thing does. When you finally find what your whole life was looking for, letting go of the rest is not a loss. It is the easiest trade you will ever make."),
    ("n9", NARRATOR, "And there is one more wonder hidden in this little story. Some have read it the other way around, and it is just as true. That to Jesus, you are the pearl."),
    ("n10", NARRATOR, "That he is the merchant who went looking, who found you, and who gave up everything he had, his own life, gladly, to buy you back. That is how good he is. You were worth all of it to him."),
    ("card", NARRATOR, "To him, you were the pearl worth everything. Have you seen how much you are worth to him?"),
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
