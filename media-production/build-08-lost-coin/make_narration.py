#!/usr/bin/env python3
"""Generate narration audio for Story Video #8 — The Lost Coin (Luke 15:8-10).
Narrator: modern, warm, low, unhurried (American).
Jesus voice: AMERICAN, never British (Cameron's permanent law, 2026-07-07).
Jesus speaks ONLY exact KJV: Luke 15:9 and Luke 15:10.
Script follows media-production/08-lost_coin-production-pack.md exactly.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewMultilingualNeural"
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-22%", "-4Hz",
     "When Jesus wanted to show how God feels about one lost soul, "
     "he didn't talk about crowds. He told this story."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A woman has ten coins. She loses one."),
    ("n2a", NARRATOR, "-20%", "-4Hz",
     "She lights a lamp. She sweeps the whole house."),
    ("n2b", NARRATOR, "-22%", "-4Hz",
     "She searches carefully — not casually, carefully — until she finds it."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Then she calls her neighbors and friends to celebrate."),
    ("j1", JESUS, "-25%", "-6Hz",
     "Rejoice with me; for I have found the piece which I had lost."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "One coin. Out of ten. The joy is disproportionate to the value of the coin."),
    ("j2", JESUS, "-25%", "-6Hz",
     "Likewise, I say unto you, there is joy in the presence of the angels "
     "of God over one sinner that repenteth."),
    ("n5", NARRATOR, "-25%", "-5Hz",
     "Over one. Not a crowd. One."),
]

async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
