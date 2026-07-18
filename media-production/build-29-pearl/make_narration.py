#!/usr/bin/env python3
"""Generate narration audio for Story Video #29 — The Pearl of Great Price
(Matthew 13:45-46).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Matthew 13:45 (j1) and 13:46 (j2).

CAPTIONS ARE VERBATIM. After each KJV line the narrator gives ONLY the plain
modern meaning and never re-quotes the KJV words (Translation Law).

Stills-only parable (Law E): NO Jesus figure on screen — his narrating voice +
KJV only; face gate trivial. The merchant is a character in the story, shown
fully.

A two-line parable, so a short video. PRIMARY reading: the kingdom / the real
thing is the pearl worth selling everything for — and the seller does it with
JOY, not grief. CLOSING TURN (the "Jesus is good" wonder, taught by many and
just as true): read the other way, Jesus is the merchant who went looking, found
YOU, and gave everything he had — his own life — gladly, to buy you. You were
worth everything to him.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: a merchant seeking pearls (KJV j1 = Matthew 13:45) ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus told one more short story, only two lines long. The kingdom of "
     "heaven, he said, is like a merchant."),
    ("j1", JESUS, "-25%", "-6Hz",
     "Again, the kingdom of heaven is like unto a merchant man, seeking goodly "
     "pearls:"),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "This was a man who knew pearls. He spent his whole life traveling and "
     "searching, handling the finest pearls in the world, always hunting for "
     "something better."),
    # --- s2: still searching ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "He had seen a lot of beautiful pearls. Good ones. Costly ones. But he kept "
     "looking, because not one of them was the one."),
    # --- s3: he finds THE pearl ---
    ("n4", NARRATOR, "-24%", "-4Hz",
     "And then one day, he found it. A single pearl, more perfect and more "
     "precious than anything he had ever held. The pearl he had been looking for "
     "his whole life."),
    # --- s4: sold all that he had (KJV j2 = Matthew 13:46) ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And he knew, the moment he saw it, exactly what he was going to do."),
    ("j2", JESUS, "-25%", "-6Hz",
     "Who, when he had found one pearl of great price, went and sold all that he "
     "had, and bought it."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "He went home and sold everything. His house, his goods, every other pearl "
     "he owned. All of it, gone, to buy the one."),
    # --- s5: he does it with JOY ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "And here is the thing. He did not do it grieving. He did not feel robbed. "
     "He gave up everything he had, gladly, because what he was getting was "
     "worth more than all of it put together."),
    ("n8", NARRATOR, "-22%", "-4Hz",
     "That is what finding the real thing does. When you finally find what your "
     "whole life was looking for, letting go of the rest is not a loss. It is the "
     "easiest trade you will ever make."),
    # --- s6: the turn — to him, YOU are the pearl ---
    ("n9", NARRATOR, "-23%", "-4Hz",
     "And there is one more wonder hidden in this little story. Some have read it "
     "the other way around, and it is just as true. That to Jesus, you are the "
     "pearl."),
    ("n10", NARRATOR, "-24%", "-4Hz",
     "That he is the merchant who went looking, who found you, and who gave up "
     "everything he had, his own life, gladly, to buy you back. That is how good "
     "he is. You were worth all of it to him."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "To him, you were the pearl worth everything. Have you seen how much you are "
     "worth to him?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
