#!/usr/bin/env python3
"""Generate narration audio for Story Video #86 — "The Wise Men" (Matthew 2:1-12).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Scripture voice: AMERICAN, never British. The wise-men lines are EXACT KJV
(Matthew 2:2 and 2:11), spoken by the scripture voice per the draft's notes.
CONTENT-CARE: GREEN — wonder and worship; Herod's court "troubled", never menacing.
HOMOGRAPH LAW: draft flags clean — SPOKEN empty; ear-check every segment anyway.
No music bed: narration + intentional silence only.
Built from DRAFTS/row-086.md (validated 2026-07-17 by W1-STILLS).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Some time after Jesus was born, travelers came from the east — "
     "scholars who had read the skies. They had seen his star, and they "
     "followed it."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "They arrived in Jerusalem asking a dangerous question."),
    # Exact KJV Matthew 2:2 — sacred pause around it.
    ("j1", SCRIPTURE, "-20%", "-2Hz",
     "Where is he that is born King of the Jews? for we have seen his "
     "star in the east, and are come to worship him."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "They were led at last to a house in Bethlehem. And there he was — "
     "not in a palace, but with his mother."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "They fell down and worshipped the child, and opened their "
     "treasures — gold, frankincense, and myrrh."),
    # Exact KJV Matthew 2:11 — SILENCE around it.
    ("j2", SCRIPTURE, "-18%", "-2Hz",
     "And when they were come into the house, they saw the young child "
     "with Mary his mother, and fell down, and worshipped him: and when "
     "they had opened their treasures, they presented unto him gifts; "
     "gold, and frankincense, and myrrh."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Warned in a dream, they went home another way. The nations had "
     "come to bow to the King."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Strangers from far away recognized him first. The door is open — "
     "you're invited to worship too."),
]

# HOMOGRAPH LAW — draft flags clean; SPOKEN stays empty. Ear-check every
# segment before assembly regardless.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
