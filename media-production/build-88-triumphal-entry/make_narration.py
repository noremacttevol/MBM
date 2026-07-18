#!/usr/bin/env python3
"""Generate narration audio for Story Video #88 — "The Triumphal Entry" (Matthew 21:1-11).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Scripture voice: AMERICAN, never British. The crowd lines are EXACT KJV
(Matthew 21:9 and 21:10-11), spoken by the scripture voice per the draft's notes.
CONTENT-CARE: GREEN — joy and peace; celebration, never mob energy.
HOMOGRAPH LAW: draft flags clean — SPOKEN empty; ear-check every segment anyway
("moved" in 21:10 is safe).
No music bed: narration + intentional silence only.
Built from DRAFTS/row-088.md (validated 2026-07-17 by W1-STILLS).
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 split: sending the two ahead (s1) then the colt brought (s2).
    ("n0a", NARRATOR, "-20%", "-4Hz",
     "As Jesus came near Jerusalem, he sent two disciples ahead to bring "
     "him a donkey and her colt."),
    ("n0b", NARRATOR, "-20%", "-4Hz",
     "It was exactly as the old prophecy had said."),
    # n1 split: the King riding in (s3) then the road laid for him (s4).
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "The King was coming — but not the kind they expected."),
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "The crowds spread their cloaks on the road, and cut branches from "
     "the trees, and lined his path."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "And the people shouted as he rode in:"),
    # Exact KJV Matthew 21:9 — SILENCE around it.
    ("j1", SCRIPTURE, "-18%", "-2Hz",
     "Hosanna to the son of David: Blessed is he that cometh in the name "
     "of the Lord; Hosanna in the highest."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The whole city was stirred. When they asked who this was, the "
     "crowd answered plainly."),
    # Exact KJV Matthew 21:10-11 — SILENCE around it.
    ("j2", SCRIPTURE, "-18%", "-2Hz",
     "And when he was come into Jerusalem, all the city was moved, "
     "saying, Who is this? And the multitude said, This is Jesus the "
     "prophet of Nazareth of Galilee."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "He came not with swords but with peace — riding on a donkey, the "
     "humble King the scriptures had promised."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The King rode in on a donkey, not a warhorse. His kingdom is "
     "peace. You're welcome in it."),
]

# HOMOGRAPH LAW — draft flags clean; SPOKEN stays empty. Ear-check every
# segment before assembly regardless.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
