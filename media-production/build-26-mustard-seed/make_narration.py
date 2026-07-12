#!/usr/bin/env python3
"""Narration for Story Video #26 — The Mustard Seed (Matthew 13:31-32).
Two-Voice Law: Andrew narrates (plain American, NEVER Multilingual); Christopher
speaks ONLY the exact KJV Jesus line. Translation Law: the narrator paraphrases
Jesus's spoken line and never echoes its KJV wording (says 'God's kingdom' not
'kingdom of heaven'; 'wild birds built their nests' not 'birds of the air lodge')."""
import asyncio, edge_tts, os

NARRATOR = "en-US-AndrewNeural"        # plain American, NEVER Multilingual
JESUS    = "en-US-ChristopherNeural"   # American, never British

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0",  NARRATOR, "-18%", "-4Hz",
     "Jesus told a story about the smallest seed a farmer knew."),
    ("n1",  NARRATOR, "-18%", "-4Hz",
     "It was a mustard seed — so tiny it could be lost in the palm of your hand."),
    ("n2",  NARRATOR, "-18%", "-4Hz",
     "A man took that one little seed and planted it in his field."),
    ("n3",  NARRATOR, "-18%", "-4Hz",
     "Of all the seeds he could have sown, it was just about the smallest of them all."),
    ("j1",  JESUS,    "-24%", "-6Hz",
     "The kingdom of heaven is like to a grain of mustard seed, which a man took, and "
     "sowed in his field: which indeed is the least of all seeds: but when it is grown, "
     "it is the greatest among herbs, and becometh a tree, so that the birds of the air "
     "come and lodge in the branches thereof."),
    ("n4",  NARRATOR, "-18%", "-4Hz",
     "But that tiny seed did not stay small. Quietly, slowly, it began to grow."),
    ("n5",  NARRATOR, "-18%", "-4Hz",
     "Up out of the ground, higher and higher, until it became the largest plant in the "
     "whole garden — a tall, spreading tree."),
    ("n6",  NARRATOR, "-18%", "-4Hz",
     "And the wild birds came and built their nests in its broad, sheltering branches."),
    ("n7",  NARRATOR, "-18%", "-4Hz",
     "That, Jesus said, is what God's kingdom is like."),
    ("n8",  NARRATOR, "-18%", "-4Hz",
     "It almost never begins big. It begins small — a whispered prayer, a single kind act, "
     "one quiet change of heart."),
    ("n9",  NARRATOR, "-18%", "-4Hz",
     "But God takes that smallest beginning and grows it into something far greater than "
     "anyone could have imagined."),
    ("card", NARRATOR, "-18%", "-4Hz",
     "God does enormous things from the smallest of starts. "
     "What small seed is he asking you to plant today?"),
]

async def main():
    os.makedirs("audio", exist_ok=True)
    for name, voice, rate, pitch, text in SEGMENTS:
        await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(f"audio/{name}.mp3")
        print("saved", name)

# Guard so `from make_narration import SEGMENTS` (qc_narration.py) does NOT re-run TTS.
if __name__ == "__main__":
    asyncio.run(main())
