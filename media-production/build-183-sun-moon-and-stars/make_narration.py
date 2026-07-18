#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #183 — Sun, Moon, and Stars
(1 Corinthians 15:40-42). Adapted from DRAFTS/row-183.md, validated against
the laws.
CATALOG-RECONCILIATION FIX (the largest validation change this draft needed):
the draft wrote a Genesis 1:14-19 creation script, but THE-200 v2 and QUEUE.md
define row 183 as "Sun, moon, and stars — 1 Cor 15:40-42 — glories, plural;
resurrection has degrees" (GL: Degrees of Glory). The catalog is the approved
law; the draft's sun/moon/stars VISUAL beats map directly onto Paul's analogy,
so the storyboard is kept and the narration is re-anchored to the catalog's
passage. Exact KJV 1 Cor 15:41 and 15:42a carried by the SCRIPTURE VOICE
(Christopher) as the centerpiece.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Degrees of Glory" (THE-200 → GL).
No divine or human figure is depicted — cosmic light only.
HOMOGRAPH LAW — BUILDER EAR-CHECK s2 ("It is SOWN in corruption"): "sow" is on
the flag list; "sown" must read /SOHN/ (seed), which is its only natural
reading — LISTEN anyway. No other flagged words in any segment.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "When Paul wrote about the resurrection, people asked him "
     "what kind of body the dead could possibly rise with. He "
     "answered by pointing at the sky."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Look up, he said. Not everything that shines shines the same "
     "way. There are different kinds of bodies, and different "
     "kinds of glory."),
    # Exact KJV 1 Cor 15:41 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "There is one glory of the sun, and another glory of the "
     "moon, and another glory of the stars: for one star differeth "
     "from another star in glory."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The sun has its own brightness. The moon has another. And no "
     "two stars burn quite alike. Then Paul said the astonishing "
     "part."),
    # Exact KJV 1 Cor 15:42a — SILENCE around it.
    ("s2", SCRIPTURE, "-24%", "-2Hz",
     "So also is the resurrection of the dead. It is sown in "
     "corruption; it is raised in incorruption:"),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The resurrection isn't one flat outcome. Like the lights "
     "above, there are glories — plural — and every one of them is "
     "a gift of light."),
    # sacred-silence beat follows n3.
    ("n4", NARRATOR, "-20%", "-4Hz",
     "The same God who hung the sun, the moon, and every different "
     "star is preparing a brightness for you."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The heavens hold more than one kind of glory. Reach for the "
     "brightest — you were made for light."),
]

# HOMOGRAPH LAW — ear-check s2 "sown" (see docstring). Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
