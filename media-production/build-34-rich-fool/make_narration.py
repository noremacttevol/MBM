#!/usr/bin/env python3
"""Narration for Story Video #34 — The Rich Fool (Luke 12:16-21).
Two-Voice Law: Andrew narrates (plain American, NEVER Multilingual); Christopher
speaks ONLY the exact KJV divine lines (God's rebuke 12:20, Jesus's seal 12:21).
Translation Law: the narrator paraphrases and quotes the rich man's own musings in
modern English; never echoes the KJV wording of the spoken divine lines."""
import asyncio, edge_tts, os

NARRATOR = "en-US-AndrewNeural"        # plain American, NEVER Multilingual
JESUS    = "en-US-ChristopherNeural"   # American, never British

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0",  NARRATOR, "-18%", "-4Hz",
     "Jesus told a story about a rich man who had a very good year."),
    ("n1",  NARRATOR, "-18%", "-4Hz",
     "His fields produced an enormous harvest — more grain and fruit than he had ever "
     "gathered in his life."),
    ("n2",  NARRATOR, "-18%", "-4Hz",
     "In fact, he had so much that he ran out of room to store it all."),
    ("n3",  NARRATOR, "-18%", "-4Hz",
     "So he thought to himself: What should I do? I know — I will tear down my barns and "
     "build bigger ones."),
    ("n4",  NARRATOR, "-18%", "-4Hz",
     "There I will store up all my grain and all my goods."),
    ("n5",  NARRATOR, "-18%", "-4Hz",
     "And then I will say to myself: You have plenty saved up for years to come. Relax. "
     "Eat, drink, and enjoy your life."),
    ("n6",  NARRATOR, "-18%", "-4Hz",
     "He had it all figured out. Every single plan was about himself — his barns, his "
     "goods, his own comfort."),
    ("n7",  NARRATOR, "-18%", "-4Hz",
     "But there was one thing he had never planned for. And that very night, God spoke "
     "to him."),
    ("j1",  JESUS,    "-24%", "-6Hz",
     "Thou fool, this night thy soul shall be required of thee: then whose shall those "
     "things be, which thou hast provided?"),
    ("n8",  NARRATOR, "-18%", "-4Hz",
     "That night, his life was over. And everything he had piled up — the barns, the "
     "grain, all of it — would simply pass to someone else."),
    ("n9",  NARRATOR, "-18%", "-4Hz",
     "He had planned for everything except the one thing that was certain: that one day "
     "he would stand before God."),
    ("n10", NARRATOR, "-18%", "-4Hz",
     "And Jesus ended the story with these words."),
    ("j2",  JESUS,    "-24%", "-6Hz",
     "So is he that layeth up treasure for himself, and is not rich toward God."),
    ("n11", NARRATOR, "-18%", "-4Hz",
     "His barns were full, but his soul was empty. He was rich in things — and poor in "
     "the only wealth that lasts."),
    ("n12", NARRATOR, "-18%", "-4Hz",
     "There is nothing wrong with a good harvest. The real question is quieter than that: "
     "are you only storing up for yourself — or are you storing up a life that is rich "
     "with God?"),
    ("card", NARRATOR, "-18%", "-4Hz",
     "His barns were full. His soul was empty. "
     "What are you storing up for yourself — and what are you storing up with God?"),
]

async def main():
    os.makedirs("audio", exist_ok=True)
    for name, voice, rate, pitch, text in SEGMENTS:
        await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(f"audio/{name}.mp3")
        print("saved", name)

# Guard so `from make_narration import SEGMENTS` (qc_narration.py) does NOT re-run TTS.
if __name__ == "__main__":
    asyncio.run(main())
