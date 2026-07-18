#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #181 — "When the Morning
Stars Sang Together" (Job 38:1-7). From DRAFTS/row-181.md, validated against
the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
The LORD's words (Job 38:7, verified exact — including the verse's closing
question mark, restored: it is part of God's question to Job) are carried by
the SCRIPTURE VOICE (Christopher) — the verse-video centerpiece.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Council in Heaven" (THE-200 → GL).
No divine or human figure is depicted — cosmic light only.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment (the draft's "whirlwind" flag refers
to a word not present in the final text). No SPOKEN overrides needed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Job had asked God hard questions. And God answered — not "
     "with explanations, but by taking Job back to the very first "
     "morning."),
    # n1 split so its two clauses land on their own stills (s2 earth-forming,
    # s4 foundations-laid-in-joy) per the CAPTION LAW.
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "Before there were people to suffer or to doubt,"),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "the foundations of the earth were being laid."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "And when that happened, something astonishing broke out in "
     "the sky."),
    # Exact KJV Job 38:7 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "When the morning stars sang together, and all the sons of "
     "God shouted for joy?"),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The stars themselves broke into song. Creation was not a "
     "cold accident — it was a celebration."),
    # sacred-silence beat follows n3.
    ("n4", NARRATOR, "-20%", "-4Hz",
     "The God who sang the world into being is the same one "
     "listening to your questions today."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The stars sang when the world began. Your story is still "
     "being written by the same hand."),
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
