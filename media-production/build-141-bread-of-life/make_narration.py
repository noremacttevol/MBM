#!/usr/bin/env python3
"""Generate narration audio for Story Video #141 — "I Am the Bread of Life"
(John 6:35, 48, 51). From DRAFTS/row-141.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 6:35, 6:48, 6:51 (all verified against the passage).
CONTENT-CARE: "my flesh" kept reverent, never graphic — the imagery on screen
is bread and light only.
HOMOGRAPH LAW: "live" (the #1 TTS offender) appears in j3, John 6:51 —
"he shall live for ever" must read /LIV/, never /LYVE/. SPOKEN respelling
"liv" applied; the caption keeps the exact KJV word. Ear-check j3 anyway.
No other flagged words.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "A crowd had followed Jesus after He fed thousands with a few "
     "loaves. They wanted more bread. He gave them something "
     "deeper."),
    # Exact KJV John 6:35.
    ("j1", JESUS, "-20%", "-2Hz",
     "I am the bread of life: he that cometh to me shall never "
     "hunger; and he that believeth on me shall never thirst."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Not the kind you chew. The kind that satisfies the part of "
     "you food can't reach."),
    # sacred-silence beat follows n1. Exact KJV John 6:48.
    ("j2", JESUS, "-22%", "-2Hz",
     "I am that bread of life."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The bread their ancestors ate in the wilderness didn't keep "
     "them alive forever. But the bread Jesus gives does."),
    # Exact KJV John 6:51 — SILENCE around it.
    ("j3", JESUS, "-20%", "-2Hz",
     "I am the living bread which came down from heaven: if any "
     "man eat of this bread, he shall live for ever: and the bread "
     "that I will give is my flesh, which I will give for the life "
     "of the world."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "He was speaking of Himself — given, like bread broken, so "
     "the world could have life."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Come hungry. He is the bread that actually fills you."),
]

# HOMOGRAPH LAW — "live" in j3 must read /LIV/. SPOKEN respelling steers the
# audio; the caption keeps the exact KJV word. Ear-check before assembly.
SPOKEN = {
    "j3": ("I am the living bread which came down from heaven: if any "
           "man eat of this bread, he shall liv for ever: and the bread "
           "that I will give is my flesh, which I will give for the life "
           "of the world."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
