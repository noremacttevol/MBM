#!/usr/bin/env python3
"""Generate narration audio for Story Video #23 — The Workers in the Vineyard
(Matthew 20:1-16).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: the householder's reply Matthew 20:13-15 (j1) and
the conclusion Matthew 20:16 (j2). (In the parable those are the landowner's
words; Jesus is the storyteller quoting them, so the Jesus voice carries them —
same as the shepherd's "Rejoice with me" in #21.)

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS and
word-wraps each text as the on-screen caption. After the KJV line the narrator
gives ONLY the plain modern meaning and never re-quotes the KJV words
(Translation Law).

Stills-only parable (Law E): NO Jesus figure on screen — his narrating voice +
KJV only; face gate trivial. Every character in the story (the landowner, the
steward, the laborers) is shown fully.

WHY-LAW: a "penny" is the KJV denarius — a full day's fair living wage; the
last crew worked one hour and got the same. The first crew were NOT underpaid
(they got exactly what they agreed); grace to the latecomers just offended their
math. Matthew 20:15 is the heart: "Is thine eye evil, because I am good?"
NUMBER-STRESS: no sentence opens on a bare "one"/"a penny" that Andrew would
under-stress; numbers sit mid-sentence.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: hired at dawn ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus said the kingdom of heaven is like a landowner who went out at first "
     "light to hire workers for his vineyard."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "He agreed with the first crew on a penny for the day — a full day's fair "
     "wage — and sent them out into the rows."),
    # --- s2: more hired through the day ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "A few hours later he went back to the market and found more men just "
     "standing around with no work. He sent them into the vineyard too, and "
     "promised to pay them what was right."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "He did the same thing again at noon, and again in the middle of the "
     "afternoon. More workers, the same promise."),
    # --- s3: the eleventh hour ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Then, with only one hour of daylight left, he went out a final time and "
     "found still more men standing idle. He asked them why they had stood there "
     "all day doing nothing."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "They told him no one had hired them. So he sent them in too, for that last "
     "single hour of work."),
    # --- s4: evening, pay the last first ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "When evening came, the owner told his foreman to call the workers and pay "
     "them — starting, strangely, with the ones hired last."),
    # --- s5: the last get a full day's wage ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "The men who had worked a single hour came up first, and each of them was "
     "handed a full day's pay. A whole penny, for one hour of work."),
    # --- s6: the first murmur ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "You can guess what the men who had worked since dawn were thinking. If the "
     "one-hour crew got a full penny, surely they would get more."),
    ("n10", NARRATOR, "-22%", "-4Hz",
     "But when their turn came, they got the very same — one penny. And they "
     "were furious. They had worked all day in the burning heat, and he had made "
     "them equal to the latecomers."),
    # --- s7: Friend, I do thee no wrong (KJV j1 = Matthew 20:13-15) ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "The owner turned to one of them, and he was not harsh about it. He called "
     "him friend."),
    ("j1", JESUS, "-26%", "-6Hz",
     "Friend, I do thee no wrong: didst not thou agree with me for a penny? Take "
     "that thine is, and go thy way: I will give unto the last, even as unto "
     "thee. Is it not lawful for me to do what I will with mine own? Is thine eye "
     "evil, because I am good?"),
    ("n12", NARRATOR, "-23%", "-4Hz",
     "In other words: I have not cheated you. You got exactly what we agreed on. "
     "Why is my kindness to someone else a problem for you? Are you really angry "
     "only because I chose to be good?"),
    # --- s8: the last first (KJV j2 = Matthew 20:16), the sending ---
    ("n13", NARRATOR, "-22%", "-4Hz",
     "That is the whole point. The first men were not underpaid. They got "
     "everything they were promised. What stung was watching someone else "
     "receive grace they had not earned."),
    ("j2", JESUS, "-25%", "-6Hz",
     "So the last shall be first, and the first last: for many be called, but "
     "few chosen."),
    ("n14", NARRATOR, "-24%", "-4Hz",
     "God does not run low on generosity when he spends it on someone who came "
     "late. His goodness is never used up. There is a full day's welcome waiting "
     "for you, no matter what hour you finally come in."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "You have not missed your chance by coming late. Will you come into the "
     "vineyard now?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
