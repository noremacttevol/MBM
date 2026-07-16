#!/usr/bin/env python3
"""Generate narration audio for Story Video #78 — "Who Is My Mother?" (Mark 3:31-35).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Mark 3:33, 3:34 and 3:35 as three separate lines (fetched, not hand-typed) — the
look around the room (v34a) sits between them as narrator, per the text's own order.
CONTENT-CARE: GREEN — warmth and belonging; his family is treated with dignity and
the narrator says plainly he was not pushing them away.
HOMOGRAPH LAW: no known offenders — SPOKEN empty; ear-check every segment anyway.
No music bed: narration + intentional silence only.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus was inside a packed house, teaching, when word came in from "
     "the edge of the crowd."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "His mother and his brothers were standing outside, asking for "
     "him. The people near him passed it forward: your family is here — "
     "they want you."),
    # Exact KJV Mark 3:33 — sacred pause around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "Who is my mother, or my brethren?"),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Nobody expected that. Then he looked slowly around at the "
     "ordinary people sitting in a circle right in front of him — "
     "farmers, fishermen, mothers, a child — and answered his own "
     "question."),
    # Exact KJV Mark 3:34 — SILENCE around it.
    ("j2", JESUS, "-20%", "-2Hz",
     "Behold my mother and my brethren!"),
    # Exact KJV Mark 3:35 — SILENCE around it.
    ("j3", JESUS, "-18%", "-2Hz",
     "For whosoever shall do the will of God, the same is my brother, "
     "and my sister, and mother."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "He wasn't pushing his family away. He was opening the circle — "
     "telling a room full of nobodies they could belong to him like "
     "blood."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He drew the family line around whoever would come. That door is "
     "open to you too."),
]

# HOMOGRAPH LAW — no bow/wound/wind/tears/lead/sow/live/read in these segments;
# SPOKEN stays empty. Ear-check every segment before assembly regardless.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
