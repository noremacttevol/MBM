#!/usr/bin/env python3
"""Narration for build-34-rich-fool — Luke 12.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Luke 12:16-21. A parable, so a red-letter KJV inks all of it. That includes
God's own line in verse 20 - 'Thou fool, this night thy soul shall be required of
thee' - because it is God as Jesus voices him INSIDE a story Jesus is telling, and
the Bible prints it red. It is deliberately NOT a `god` beat. j1 and j2 stay RED,
and two more parable lines the video only paraphrased join them:
  j3  Luke 12:18  'This will I do: I will pull down my barns, and build greater...'
  j4  Luke 12:19  'Soul, thou hast much goods laid up for many years...'
still_vars S1..S7 introduced.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus told a story about a rich man who had a very good year."),
    ("n1", NARRATOR, "His fields produced an enormous harvest — more grain and fruit than he had ever gathered in his life."),
    ("n2", NARRATOR, "In fact, he had so much that he ran out of room to store it all."),
    # Luke 12:18
    ("j3", JESUS, "This will I do: I will pull down my barns, and build greater; and there will I bestow all my fruits and my goods."),
    ("n3", NARRATOR, "So he thought to himself: What should I do? I know — I will tear down my barns and build bigger ones."),
    ("n4", NARRATOR, "There I will store up all my grain and all my goods."),
    # Luke 12:19
    ("j4", JESUS, "And I will say to my soul, Soul, thou hast much goods laid up for many years; take thine ease, eat, drink, and be merry."),
    ("n5", NARRATOR, "And then I will say to myself: You have plenty saved up for years to come. Relax. Eat, drink, and enjoy your life."),
    ("n6", NARRATOR, "He had it all figured out. Every single plan was about himself — his barns, his goods, his own comfort."),
    ("n7", NARRATOR, "But there was one thing he had never planned for. And that very night, God spoke to him."),
    # Luke 12:20
    ("j1", JESUS, "Thou fool, this night thy soul shall be required of thee: then whose shall those things be, which thou hast provided?"),
    ("n8", NARRATOR, "That night, his life was over. And everything he had piled up — the barns, the grain, all of it — would simply pass to someone else."),
    ("n9", NARRATOR, "He had planned for everything except the one thing that was certain: that one day he would stand before God."),
    ("n10", NARRATOR, "And Jesus ended the story with these words."),
    # Luke 12:21
    ("j2", JESUS, "So is he that layeth up treasure for himself, and is not rich toward God."),
    ("n11", NARRATOR, "His barns were full, but his soul was empty. He was rich in things — and poor in the only wealth that lasts."),
    ("n12", NARRATOR, "There is nothing wrong with a good harvest. The real question is quieter than that: are you only storing up for yourself — or are you storing up a life that is rich with God?"),
    ("card", NARRATOR, "His barns were full. His soul was empty. What are you storing up for yourself — and what are you storing up with God?"),
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
