#!/usr/bin/env python3
"""Generate narration audio for Story Video #129 — Nazareth: Only a Few
(Mark 6:5-6). From DRAFTS/row-129.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
VOICE-LAW FIX: the draft labeled Mark 6:5-6 as a "JESUS" line, but that verse
is the evangelist narrating ABOUT Jesus — he never speaks it. It is read here
by the SCRIPTURE VOICE (Christopher) per the build-161 precedent: Christopher
carries exact KJV; the narrator never quotes KJV; the Jesus voice is used only
for words Jesus actually speaks (he has none in this passage).
KJV verified: Mark 6:5 + the first sentence of 6:6, word-exact.
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
     "Jesus went back to Nazareth, the town that watched Him grow "
     "up. He taught in the synagogue."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "But the people who'd known Him as a boy couldn't believe. "
     "They took offense at Him — and their unbelief became a "
     "wall."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "He could do only a few mighty works there. Not because His "
     "power ran out, but because they wouldn't receive it."),
    # Exact KJV Mark 6:5-6a — scripture voice (see docstring).
    ("s1", SCRIPTURE, "-22%", "-2Hz",
     "And he could there do no mighty work, save that he laid his "
     "hands upon a few sick folk, and healed them. And he "
     "marvelled because of their unbelief."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "He still healed the few who came. Even amazement at their "
     "doubt didn't stop His mercy."),
    # sacred-silence beat follows n3.
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Faith opens the door. Where people believed, even a little, "
     "He worked."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He healed the few who reached out. The door is the same "
     "today — believe, and let Him work."),
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
