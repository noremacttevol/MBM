#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #178 — "Let Us Make Man in
Our Image" (Genesis 1:26-27). From DRAFTS/row-178.md, validated against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — the member verse-video format
(build-161 precedent) requires the exact KJV verses as the CENTERPIECE, read
by the SCRIPTURE VOICE (Christopher, cream italic caption, sacred silence).
Genesis 1:26 and 1:27 added verbatim as s1/s2 (the catalog row is 1:26-27 and
the draft's Eve beat rests on v27's "male and female").
TRANSLATION-LAW FIX: the draft's n3 echoed Genesis 2:7 nearly verbatim
("breathed into his nostrils the breath of life... a living soul") in the
narrator's mouth — reworded to plain modern words.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Godhead" (THE-200 → GL).
No divine figure is depicted (creation; light and Spirit-presence only).
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "At the start of all things, before any person drew breath, a "
     "counsel happened in the Godhead — let us make man in our "
     "image."),
    # Exact KJV Genesis 1:26 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "And God said, Let us make man in our image, after our "
     "likeness: and let them have dominion over the fish of the "
     "sea, and over the fowl of the air, and over the cattle, and "
     "over all the earth, and over every creeping thing that "
     "creepeth upon the earth."),
    # Exact KJV Genesis 1:27.
    ("s2", SCRIPTURE, "-24%", "-2Hz",
     "So God created man in his own image, in the image of God "
     "created he him; male and female created he them."),
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "Not in the shape of any creature, but bearing something of "
     "God himself:"),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "the capacity to know him, to choose him, to reflect him."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The plan included dominion — over fish, birds, cattle, and "
     "all the earth. Stewards, not owners."),
    # sacred-silence beat follows n2.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Then the act: God shaped a man from the dust of the ground "
     "and filled him with breath — and the man came alive."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Every person since carries that original dignity — made in "
     "the image, loved into being."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "You are made in his image. That is worth more than you "
     "know."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present. Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
