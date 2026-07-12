#!/usr/bin/env python3
"""Generate narration audio for Story Video #35 — The Great Banquet
(Luke 14:15-24).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV, delivering the host's quoted lines:
Luke 14:21 (j1, bring in the poor/maimed/halt/blind) and 14:23 (j2, the
highways and hedges, that my house may be filled).

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS
and word-wraps each text as the on-screen caption. After each KJV line the
narrator gives ONLY the plain modern meaning and never re-quotes the KJV words
(Translation Law).

A parable told BY Jesus with NO Jesus figure on screen — only his narrating
voice; the host is an ordinary parable nobleman shown fully (STILLS-ONLY, Law E;
face gate trivial — no Jesus figure at all).

MILK FRAMING (how GOOD he is): when the invited guests make excuses, the host
does NOT cancel the feast or shrink his generosity — he opens the doors WIDER,
to the poor and the overlooked. God's answer to rejection is MORE invitation.
The "compel them to come in" is warm insistence born of love (make sure they
know they are truly wanted), never coercion — MBM never pressures.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the feast is prepared ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus told a story about a man who threw a great feast. He prepared "
     "everything, the finest food, the tables set, every place ready, and he "
     "sent out his invitations."),
    # --- s2: the servant is sent ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "When the feast was ready, he sent his servant to tell the invited guests, "
     "come, for everything is ready now."),
    # --- s3: the excuses ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "But one by one, they all made excuses. One had just bought a field and "
     "had to go see it. One had bought oxen and had to try them out. One had "
     "just married, and simply would not come."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "They were not evil people. They were just busy. Their own plans felt more "
     "urgent than the joy waiting for them at his table."),
    # --- s4: the servant returns; the host does not cancel ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "The servant came back alone. And here is where you would expect the host "
     "to cancel the feast, hurt and offended. He did not."),
    # --- s5: go to the streets (KJV j1) ---
    ("j1", JESUS, "-26%", "-6Hz",
     "Go out quickly into the streets and lanes of the city, and bring in "
     "hither the poor, and the maimed, and the halt, and the blind."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Go out into the streets, he said, and bring in the poor, the crippled, "
     "the blind, everyone the respectable guests would never have invited."),
    # --- s6: bringing them in; still room ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "So the servant went and found them, the overlooked and the left out, and "
     "told them there was a seat with their name on it. You can imagine their "
     "faces. Nobody had ever invited them to anything."),
    ("n8", NARRATOR, "-24%", "-5Hz",
     "And there was still room."),
    # --- s7: the highways and hedges (KJV j2), the peak ---
    ("j2", JESUS, "-26%", "-6Hz",
     "Go out into the highways and hedges, and compel them to come in, that my "
     "house may be filled."),
    ("n9", NARRATOR, "-22%", "-4Hz",
     "Go further out, he said, to the roads and the edges of town, and do not "
     "take no for an answer. Make sure they know they are truly wanted, until "
     "my house is full."),
    ("n10", NARRATOR, "-24%", "-4Hz",
     "That is how good he is. When the ones who should have come turned him "
     "down, he did not shrink his table. He opened the doors wider. The feast "
     "was always going to be full, and there has always been a place at it for "
     "you."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "The table is set, and there is a seat with your name on it. What excuse "
     "have you been giving for not sitting down?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
