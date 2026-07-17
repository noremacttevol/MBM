#!/usr/bin/env python3
"""Generate narration audio for Story Video #80 — "Come Unto Me" (Matt 11:28-30).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Matt 11:28, 11:29, 11:30 (fetched, not hand-typed).
CONTENT-CARE: GREEN — pure comfort, no conflict; the weariness of the crowd is
painted with dignity, never misery. STUDY-GEM: one plain line explains what a yoke
is (word-meaning tidbits are sanctioned by the pre-flight checklist).
HOMOGRAPH LAW: no known offenders — SPOKEN empty; ear-check every segment anyway.
No music bed: narration + intentional silence only.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0a", NARRATOR, "-20%", "-4Hz",
     "To a crowd of people worn down by work, by rules, by just getting "
     "through the day,"),
    ("n0b", NARRATOR, "-20%", "-4Hz",
     "Jesus made one of the gentlest offers ever spoken."),
    # Exact KJV Matt 11:28 — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "Come unto me, all ye that labour and are heavy laden, and I will "
     "give you rest."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A yoke was the wooden beam that let two oxen pull a load "
     "together, so no single animal carried it alone."),
    # Exact KJV Matt 11:29 — sacred pause around it.
    ("j2", JESUS, "-20%", "-2Hz",
     "Take my yoke upon you, and learn of me; for I am meek and lowly "
     "in heart: and ye shall find rest unto your souls."),
    # Exact KJV Matt 11:30 — SILENCE around it.
    ("j3", JESUS, "-18%", "-2Hz",
     "For my yoke is easy, and my burden is light."),
    ("n2a", NARRATOR, "-20%", "-4Hz",
     "He wasn't promising a life with nothing to carry."),
    ("n2b", NARRATOR, "-20%", "-4Hz",
     "He was promising to get under the load with you, so it never has "
     "to be carried alone again."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Whatever you've been carrying by yourself — he's offering to take "
     "the other side of it. Come."),
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
