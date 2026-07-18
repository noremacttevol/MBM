#!/usr/bin/env python3
"""Generate narration audio for Story Video #132 — Forbid Him Not
(Mark 9:38-41). From DRAFTS/row-132.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Mark 9:39-40 (verified against the passage).
CONTENT-CARE: the expulsion is never depicted graphically — light overcoming
gloom only, no embodied spirit.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "John came to Jesus with a complaint. They'd seen someone "
     "driving out demons using Jesus's name — and the man wasn't "
     "one of their group. So they told him to stop."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "John thought he was protecting the cause. The man wasn't "
     "with them, so he shouldn't be using the name."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Jesus corrected the instinct. Don't stop him. Anyone doing "
     "good in My name isn't against you."),
    # sacred-silence beat follows n2. Exact KJV Mark 9:39-40.
    ("j1", JESUS, "-20%", "-2Hz",
     "Forbid him not: for there is no man which shall do a miracle "
     "in my name, that can lightly speak evil of me. For he that "
     "is not against us is on our part."),
    # n3 split so the cup-of-water still and the wide-circle still each
    # carry their half — draft words verbatim.
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "Whoever gives a cup of water in His name won't lose his "
     "reward."),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "The work isn't about belonging to a team — it's about Him."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "John learned a lesson that day: the kingdom is bigger than "
     "the inner circle."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Don't draw the circle too small. Whoever works in His name "
     "is on your side."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): n0 contains "using" and n1 "using" — the
# ordinary verb, unambiguous. Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
