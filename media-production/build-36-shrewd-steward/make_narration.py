#!/usr/bin/env python3
"""Generate narration audio for Story Video #36 — The Shrewd Steward
(Luke 16:1-13).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV — his own commendation/application of the parable:
Luke 16:8 (j1, "the lord commended the unjust steward... wiser than the children
of light") and Luke 16:9 (j2, "Make to yourselves friends of the mammon of
unrighteousness... everlasting habitations").

CAPTIONS ARE VERBATIM. After each KJV line the narrator gives ONLY the plain
modern meaning and never re-quotes the KJV words (Translation Law).

Stills-only parable (Law E): NO figure of the Lord on screen — his narrating
voice + KJV only; face gate trivial. The rich owner, the steward, and the
debtors are ordinary parable characters, shown fully.

MILK FRAMING (how GOOD he is): this is a hard parable — the Lord praises a
dishonest manager — so we keep the LIGHT exactly where the heart line THE-200
names it: URGENCY ABOUT ETERNAL THINGS. The point is NOT the man's dishonesty;
it is his URGENCY and cleverness about his future. Worldly people are shrewd and
quick about money; are we half that wise about the things that actually last —
people, kindness, God? The good news underneath: God is not after your money. He
is after YOU. "Ye cannot serve God and mammon" is not a jealous rule but a
rescue — money makes a cruel owner, and a good Father wants your heart free and
your hands open. Use whatever you have to love people NOW; those friendships are
the only thing you carry into forever, and there is a place kept for you there.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the steward is accused ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus told a story about a rich man and the manager who ran everything he "
     "owned. Word came to the rich man that this manager had been wasting his "
     "goods."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "So he called the manager in and said, give an account of your work, "
     "because you cannot be my manager any longer. Just like that, the man was "
     "about to lose his job and his home."),
    # --- s2: the worried plan ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And the manager panicked. I am not strong enough to dig ditches, he "
     "thought, and I am too ashamed to beg. He had to think fast, and he had to "
     "act right now, before the news got out."),
    # --- s3: he calls in the debtors ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "So while he still could, he quickly called in every person who owed his "
     "employer money, one after another, to make himself some friends before it "
     "was too late."),
    # --- s4: the oil bill ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "How much do you owe? he asked the first man. A hundred jugs of olive oil. "
     "Quick, said the manager, take your bill and write down fifty. And the "
     "farmer could hardly believe it."),
    # --- s5: the wheat bill ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And you? A hundred measures of wheat. Take your bill, he said, and write "
     "down eighty. One after another he made friends who would remember him and "
     "take him in when he had nothing."),
    # --- s6: the commendation (KJV j1 = Luke 16:8) ---
    ("j1", JESUS, "-25%", "-6Hz",
     "And the lord commended the unjust steward, because he had done wisely: for "
     "the children of this world are in their generation wiser than the children "
     "of light."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Even his employer had to admire it. And here is the strange point Jesus "
     "was making. He was not praising the cheating. He was pointing at the "
     "urgency. Worldly people are so clever, so quick, about money and their own "
     "future."),
    # --- s7: make friends with mammon (KJV j2 = Luke 16:9), the peak ---
    ("j2", JESUS, "-26%", "-6Hz",
     "And I say unto you, Make to yourselves friends of the mammon of "
     "unrighteousness; that, when ye fail, they may receive you into everlasting "
     "habitations."),
    ("n8", NARRATOR, "-22%", "-4Hz",
     "Use your money, he said, use your things, use whatever you have, to love "
     "people now. Those friendships are the one thing you carry with you past "
     "the end of your life. Be that urgent about what actually lasts."),
    # --- s8: you cannot serve two, and the good news ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "Then he said the line that ties it all together. You cannot serve God and "
     "money. You will end up loving one and despising the other. And money is a "
     "hard, hungry thing to serve."),
    ("n10", NARRATOR, "-24%", "-4Hz",
     "That is how good he is. He is not after your money. He is after you. He "
     "wants your heart free of that cruel little master and your hands open, so "
     "that you spend your one short life being urgent about the things that last "
     "forever."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He is not after your money. He is after you. What are you being urgent "
     "about?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
