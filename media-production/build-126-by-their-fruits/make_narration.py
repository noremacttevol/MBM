#!/usr/bin/env python3
"""Generate narration audio for Story Video #126 — By Their Fruits
(Matthew 7:15-20). From DRAFTS/row-126.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Matthew 7:15, 7:16-17, 7:19-20 (all verified against the passage).
CONTENT-CARE (teaching): gentle warning, no fear framing — "cast into the
fire" is heard in the KJV line only, never painted.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus taught how to tell what is true — look at what grows "
     "from it."),
    # Exact KJV Matt 7:15 — delivered in two breaths so each phrase lands on
    # its own still (s2 beware, s3 sheeps-clothing) per the CAPTION LAW. The
    # words are unchanged KJV; only the pause between phrases is added.
    ("j1a", JESUS, "-20%", "-2Hz",
     "Beware of false prophets,"),
    ("j1b", JESUS, "-20%", "-2Hz",
     "which come to you in sheep's clothing, but inwardly they "
     "are ravening wolves."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A tree shows what it is by what it bears. You don't guess at "
     "a tree by its bark."),
    # sacred-silence beat follows n1. Exact KJV Matt 7:16-17.
    ("j2", JESUS, "-20%", "-2Hz",
     "Ye shall know them by their fruits. Do men gather grapes of "
     "thorns, or figs of thistles? Even so every good tree "
     "bringeth forth good fruit; but a corrupt tree bringeth forth "
     "evil fruit."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The good and the rotten cannot switch places — what is "
     "inside comes out in the open."),
    # Exact KJV Matt 7:19-20.
    ("j3", JESUS, "-20%", "-2Hz",
     "Every tree that bringeth not forth good fruit is hewn down, "
     "and cast into the fire. Wherefore by their fruits ye shall "
     "know them."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "What grows from a life with him is good fruit — love, "
     "kindness, truth. Abide in him, and let it show."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present. Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
