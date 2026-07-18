#!/usr/bin/env python3
"""Generate narration audio for Story Video #67 — "The Transfiguration" (Mark 9:2-8).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Scripture voice: AMERICAN, never British. Exact-KJV lines only:
 - Peter, Mark 9:5b: "Master, it is good for us to be here: and let us make three
   tabernacles; one for thee, and one for Moses, and one for Elias."
 - The voice from the cloud, Mark 9:7b: "This is my beloved Son: hear him."
CONTENT-CARE: GREEN — awe and beloved-Sonship, never fear.
HOMOGRAPH LAW: no offenders. NOTE "Elias" is pronounced by edge-tts fine (ee-LY-as);
ear-check anyway. SPOKEN empty.
No music bed: narration + intentional silence only.
Authored 2026-07-17 by W1-STILLS (no Hermes draft existed for this row).
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus took three of his closest friends — Peter, James, and John — "
     "up a high mountain, away from everyone."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "And there, in front of them, he changed. His clothes turned a "
     "blinding white, brighter than anything on earth, and for one "
     "moment they saw him shining with who he really is."),
    ("n2a", NARRATOR, "-20%", "-4Hz",
     "Two of the greatest prophets, Moses and Elijah, appeared and stood "
     "talking with him."),
    ("n2b", NARRATOR, "-20%", "-4Hz",
     "Peter, overwhelmed, blurted out the first thing that came to him."),
    # Exact KJV Mark 9:5b — Peter, sacred pause.
    ("j1", SCRIPTURE, "-18%", "-2Hz",
     "Master, it is good for us to be here: and let us make three "
     "tabernacles; one for thee, and one for Moses, and one for Elias."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Then a bright cloud settled over the mountain, and out of it came "
     "a voice."),
    # Exact KJV Mark 9:7b — the voice from the cloud, SILENCE around it.
    ("j2", SCRIPTURE, "-16%", "-3Hz",
     "This is my beloved Son: hear him."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "And then it was over. The light faded, the cloud lifted, and Jesus "
     "stood there alone — the same gentle friend, reaching down to lift "
     "them up. Do not be afraid, he told them."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "For one moment they saw who he really is — and heaven said, hear "
     "him. That invitation still stands."),
]

# HOMOGRAPH LAW — no offenders; SPOKEN stays empty. Ear-check every segment anyway.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
