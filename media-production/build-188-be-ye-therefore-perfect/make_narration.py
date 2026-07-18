#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #188 — "Be Ye Therefore
Perfect" (Matthew 5:44-48). From DRAFTS/row-188.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Matthew 5:44, 5:45 and 5:48 (all verified against the passage) — the
5:48 line is the centerpiece.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Perfection" (THE-200 → GL).
HOMOGRAPH LAW — 🛑 BUILDER MUST EAR-CHECK j1 ("despitefully USE you"): "use"
is on the flag list — the verb must read /YOOZ/, its natural reading, but
LISTEN before assembly. No other flagged words in any segment (card checked).
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus sat on the hillside and taught the crowds a kind of "
     "love they had never heard before — not just for friends, but "
     "for enemies too."),
    # Exact KJV Matt 5:44 — ear-check "use" (see docstring).
    ("j1", JESUS, "-20%", "-2Hz",
     "But I say unto you, Love your enemies, bless them that curse "
     "you, do good to them that hate you, and pray for them which "
     "despitefully use you, and persecute you;"),
    # Exact KJV Matt 5:45.
    ("j2", JESUS, "-20%", "-2Hz",
     "That ye may be the children of your Father which is in "
     "heaven: for he maketh his sun to rise on the evil and on the "
     "good, and sendeth rain on the just and on the unjust."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The point was simple and hard at once — God's kindness falls "
     "on everyone, the grateful and the cruel alike."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Then he set the bar that no one could reach alone, and meant "
     "for us to run toward it."),
    # Exact KJV Matt 5:48 — THE CENTERPIECE, SILENCE around it.
    ("j3", JESUS, "-22%", "-2Hz",
     "Be ye therefore perfect, even as your Father which is in "
     "heaven is perfect."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Not perfect by comparison with each other. Perfect by the "
     "measure of a Father whose love has no edge, no favor, no "
     "limit."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He asks for a love without limits — and he gives the grace "
     "to grow into it. Come and learn it from him."),
]

# HOMOGRAPH LAW — ear-check j1 "use" (see docstring). Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
