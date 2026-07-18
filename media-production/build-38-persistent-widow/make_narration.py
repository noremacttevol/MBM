#!/usr/bin/env python3
"""Generate narration audio for Story Video #38 — The Persistent Widow
(Luke 18:1-8).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: the unjust judge's quoted resolve (Luke 18:4-5, j1)
and the turn where Jesus points from the judge to God (Luke 18:6-7, j2).

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS
and word-wraps each text as the on-screen caption. After each KJV line the
narrator gives ONLY the plain modern meaning and never re-quotes the KJV words
(Translation Law).

A parable told BY Jesus with NO Jesus figure on screen — only his narrating
voice; the widow and the cold judge are ordinary parable characters shown fully
(STILLS-ONLY, Law E; face gate trivial — no Jesus figure at all).

MILK FRAMING (how GOOD he is): the whole point is CONTRAST. God is NOTHING like
that reluctant, annoyed judge. He is not worn down into caring — he already loves
you, he is not reluctant, he wants to hear you. So keep coming to him, not because
he is hard to move, but because he is the opposite of that judge. End on
invitation, never pressure.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: a widow, wronged and alone ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus told a story about a widow. She had lost her husband and had no one "
     "to protect her. Someone had wronged her, and she had no power, no money, "
     "no one important to make anyone listen."),
    # --- s2: she pleads before the cold judge ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "In her town there was a judge who feared neither God nor man. The widow "
     "came to him with one simple plea: give me justice against the man who "
     "wronged me."),
    # --- s3: for a while he would not ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "But the judge did not care. He waved her away. She had nothing to offer "
     "him, no bribe, no rank, no reason for him to lift a finger."),
    # --- s4: she comes again and again ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "So she came back. And again. And again. She would not stop. Every day the "
     "same worn face at his door, the same steady voice asking for what was "
     "right."),
    # --- s5: the judge finally relents (KJV j1) ---
    ("j1", JESUS, "-26%", "-6Hz",
     "Though I fear not God, nor regard man; yet because this widow troubleth "
     "me, I will avenge her, lest by her continual coming she weary me."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Fine, the judge finally said. I do not fear God, and I do not care about "
     "her. But she is wearing me out. I will give her justice just to be rid of "
     "her."),
    # --- s6: the turn — Jesus points from the judge to God (KJV j2), the peak ---
    ("j2", JESUS, "-26%", "-6Hz",
     "Hear what the unjust judge saith. And shall not God avenge his own elect, "
     "which cry day and night unto him, though he bear long with them?"),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Listen to what even that cold judge finally did, Jesus said. Now think "
     "about God. If a man who cares for no one will still give justice to the one "
     "who keeps coming, how much more will your Father, who loves you, hear you?"),
    # --- s7: God is nothing like that judge ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Here is the whole point. God is not that judge. He is not reluctant. He is "
     "not annoyed by you. He does not have to be worn down into caring, because "
     "he already loves you, and he already wants to hear you."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "So when Jesus says to keep praying and never give up, it is not because God "
     "is hard to move. It is because he is the very opposite of that judge, and "
     "he has been waiting to hear from you all along."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "God is not the reluctant judge. What have you stopped asking him for, "
     "because you assumed he wasn't listening?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
