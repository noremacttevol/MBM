#!/usr/bin/env python3
"""Generate narration audio for Story Video #87 — "The Boy in the Temple" (Luke 2:41-52).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV: Luke 2:49.
CONTENT-CARE: GREEN — tender family story; the parents' worry is love, never blame.
HOMOGRAPH LAW: draft flags clean — SPOKEN empty; ear-check every segment anyway.
No music bed: narration + intentional silence only.
Built from DRAFTS/row-087.md (validated 2026-07-17 by W1-STILLS; face per
Cameron's 2026-07-17 child addendum — boy version of the master face).
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 split: the caravan leaving (s1) then realizing he's missing (s2).
    ("n0a", NARRATOR, "-20%", "-4Hz",
     "Every year Jesus's family went to Jerusalem for the Passover. When "
     "he was twelve, they made the trip as usual."),
    ("n0b", NARRATOR, "-20%", "-4Hz",
     "On the way home, they realized he wasn't with them."),
    # n1 split: the three-day search (s3), finding him among the teachers
    # (s4), and the questions that amazed them (s5).
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "They turned back, searching for three days."),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "And they found him in the temple, sitting among the teachers, "
     "listening,"),
    ("n1c", NARRATOR, "-20%", "-4Hz",
     "and asking questions that amazed everyone."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "His mother, relieved and worried, asked why he'd done this to "
     "them. He answered with a question of his own."),
    # Exact KJV Luke 2:49 — SILENCE around it.
    ("j1", JESUS, "-18%", "-2Hz",
     "How is it that ye sought me? wist ye not that I must be about my "
     "Father's business?"),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "They didn't fully understand. But he went home with them and "
     "obeyed them — and he kept growing in wisdom, in stature, and in "
     "favor with God and people."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Even as a boy he knew where he belonged. You were made for the "
     "Father's house too — come find your place."),
]

# HOMOGRAPH LAW — draft flags clean; SPOKEN stays empty. Ear-check every
# segment before assembly regardless ("wist" is archaic but not a homograph).
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
