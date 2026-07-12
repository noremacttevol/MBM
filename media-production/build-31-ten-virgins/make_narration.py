#!/usr/bin/env python3
"""Narration for Story Video #31 — The Ten Virgins (Matthew 25:1-13).
Two-Voice Law: Andrew narrates (plain American, NEVER Multilingual); Christopher
speaks ONLY the exact KJV Jesus seal (25:13). Translation Law: the narrator
paraphrases and quotes the characters' words in modern English; never echoes the
KJV wording of Jesus's spoken line."""
import asyncio, edge_tts, os

NARRATOR = "en-US-AndrewNeural"        # plain American, NEVER Multilingual
JESUS    = "en-US-ChristopherNeural"   # American, never British

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0",  NARRATOR, "-18%", "-4Hz",
     "Jesus told a story about ten young women waiting for a wedding."),
    ("n1",  NARRATOR, "-18%", "-4Hz",
     "In those days, a whole village would wait for the bridegroom to come, late in the "
     "evening, and lead everyone in to the feast."),
    ("n2",  NARRATOR, "-18%", "-4Hz",
     "So ten young women took their oil lamps and went out into the dusk to meet him."),
    ("n3",  NARRATOR, "-18%", "-4Hz",
     "Five of them were wise. Along with their lamps, they each carried a small jar of "
     "extra oil."),
    ("n4",  NARRATOR, "-18%", "-4Hz",
     "The other five were foolish. They brought their lamps — but no extra oil at all."),
    ("n5",  NARRATOR, "-18%", "-4Hz",
     "The bridegroom was delayed. Hour after hour slipped by, and one by one, all ten "
     "women grew drowsy and fell asleep."),
    ("n6",  NARRATOR, "-18%", "-4Hz",
     "Then, at midnight, a cry rang out: The bridegroom is coming! Come out to meet him!"),
    ("n7",  NARRATOR, "-18%", "-4Hz",
     "They all woke and reached for their lamps. The wise trimmed theirs, and they burned "
     "warm and bright."),
    ("n8",  NARRATOR, "-18%", "-4Hz",
     "But the foolish looked down in dismay. Their lamps were sputtering out — they had no "
     "oil left."),
    ("n9",  NARRATOR, "-18%", "-4Hz",
     "Please, they cried out to the others — give us some of your oil!"),
    ("n10", NARRATOR, "-18%", "-4Hz",
     "But the wise couldn't. There isn't enough for all of us, they said. Hurry — go and "
     "buy your own."),
    ("n11", NARRATOR, "-18%", "-4Hz",
     "And while the foolish rushed off into the dark to find oil, the bridegroom arrived."),
    ("n12", NARRATOR, "-18%", "-4Hz",
     "The ones who were ready went in with him to the wedding feast. And the door was shut."),
    ("n13", NARRATOR, "-18%", "-4Hz",
     "Later the others came back, knocking. Lord, they called, open the door for us! But "
     "the answer came from inside: I do not know you."),
    ("n14", NARRATOR, "-18%", "-4Hz",
     "Then Jesus told them why he had shared this story."),
    ("j1",  JESUS,    "-24%", "-6Hz",
     "Watch therefore, for ye know neither the day nor the hour wherein the Son of man "
     "cometh."),
    ("n15", NARRATOR, "-18%", "-4Hz",
     "The oil is the one thing you cannot borrow at the last minute — a heart that is truly "
     "ready, a faith that is really your own, a lamp you have kept burning."),
    ("n16", NARRATOR, "-18%", "-4Hz",
     "And here is the good news: the door is still open now. Tonight, your lamp can be "
     "filled. He is worth being ready for."),
    ("card", NARRATOR, "-18%", "-4Hz",
     "You cannot borrow someone else's oil. Is your own lamp burning — are you ready to "
     "meet him?"),
]

async def main():
    os.makedirs("audio", exist_ok=True)
    for name, voice, rate, pitch, text in SEGMENTS:
        await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(f"audio/{name}.mp3")
        print("saved", name)

# Guard so `from make_narration import SEGMENTS` (qc_narration.py) does NOT re-run TTS.
if __name__ == "__main__":
    asyncio.run(main())
