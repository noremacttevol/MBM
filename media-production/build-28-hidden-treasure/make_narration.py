#!/usr/bin/env python3
"""Narration for Story Video #28 — Hidden Treasure (Matthew 13:44).
Two-Voice Law: Andrew narrates (plain American, NEVER Multilingual); Christopher
speaks ONLY the exact KJV Jesus line. Translation Law: the narrator paraphrases
Jesus's spoken line in modern English and never echoes its KJV wording
(e.g. narrator says 'God's kingdom', not 'kingdom of heaven')."""
import asyncio, edge_tts, os

NARRATOR = "en-US-AndrewNeural"        # plain American, NEVER Multilingual
JESUS    = "en-US-ChristopherNeural"   # American, never British

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0",  NARRATOR, "-18%", "-4Hz",
     "Jesus once told a very short story — about a man, and a field."),
    ("n1",  NARRATOR, "-18%", "-4Hz",
     "He was a hired worker, out digging in a field that wasn't even his own."),
    ("n2",  NARRATOR, "-18%", "-4Hz",
     "And on one ordinary day, his spade struck something hard, buried in the ground."),
    ("n3",  NARRATOR, "-18%", "-4Hz",
     "He cleared away the dirt — and there it was. A treasure. Hidden, forgotten, "
     "and worth more than he had ever seen in his life."),
    ("n4",  NARRATOR, "-18%", "-4Hz",
     "His heart pounded. Quickly, quietly, he covered it back over — and told no one."),
    ("j1",  JESUS,    "-24%", "-6Hz",
     "Again, the kingdom of heaven is like unto treasure hid in a field; the which "
     "when a man hath found, he hideth, and for joy thereof goeth and selleth all "
     "that he hath, and buyeth that field."),
    ("n5",  NARRATOR, "-18%", "-4Hz",
     "Did you catch what he did? He went home and sold everything he owned."),
    ("n6",  NARRATOR, "-18%", "-4Hz",
     "His house. His tools. All of it — gladly, without a second thought."),
    ("n7",  NARRATOR, "-18%", "-4Hz",
     "And with every coin he had, he bought that one field for himself."),
    ("n8",  NARRATOR, "-18%", "-4Hz",
     "Because he knew what was waiting under the soil. That field was worth more "
     "than everything else he owned, put together."),
    ("n9",  NARRATOR, "-18%", "-4Hz",
     "That, Jesus said, is what God's kingdom is like."),
    ("n10", NARRATOR, "-18%", "-4Hz",
     "At first it can look like an ordinary field. But once you catch sight of the "
     "treasure in it — once you truly see who Jesus is — nothing else even compares."),
    ("n11", NARRATOR, "-18%", "-4Hz",
     "And you don't give everything up sadly. You do it out of pure joy — because "
     "you've found the one thing worth having everything else."),
    ("card", NARRATOR, "-18%", "-4Hz",
     "The man sold all he had — and called it the best trade of his life. "
     "If you have found the treasure, what is he worth to you?"),
]

async def main():
    os.makedirs("audio", exist_ok=True)
    for name, voice, rate, pitch, text in SEGMENTS:
        await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(f"audio/{name}.mp3")
        print("saved", name)

# Guard so `from make_narration import SEGMENTS` (qc_narration.py) does NOT re-run
# TTS and churn the audio files. Run this module directly to generate.
if __name__ == "__main__":
    asyncio.run(main())
