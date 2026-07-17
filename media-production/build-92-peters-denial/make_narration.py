#!/usr/bin/env python3
"""Generate narration audio for Story Video #92 — Peter's Denial and the Look
(Luke 22:54-62). From DRAFTS/row-092.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus has NO spoken line in this story — the LOOK (Luke 22:61) is the moment,
held in sacred silence. Narrator only.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment ("wept" and "crowed" are not on the
flag list but ear-check them anyway). No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "After they arrested Jesus, Peter followed at a distance and "
     "warmed himself by a fire in the courtyard, trying not to be "
     "noticed."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A servant girl looked at him and said, this man was with him "
     "too. Peter said, woman, I don't know him."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "A little later, someone else. Then a third. Each time Peter "
     "denied it harder — I don't know what you're talking about."),
    # sacred-silence beat follows n2.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "And right then, while the words were still in his mouth, a "
     "rooster crowed."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Across the courtyard, Jesus turned and looked straight at "
     "Peter. Just looked at him."),
    # sacred-silence beat: the LOOK holds — no spoken line from Jesus.
    # n5 split into three so each beat lands on its own still (s6 peter-
    # remembers, s7 out-through-the-gate, s8 the-dying-fire-at-dawn) per the
    # CAPTION LAW.
    ("n5a", NARRATOR, "-20%", "-4Hz",
     "And Peter remembered — Jesus had told him this would "
     "happen."),
    ("n5b", NARRATOR, "-20%", "-4Hz",
     "He went outside and wept bitterly."),
    ("n5c", NARRATOR, "-20%", "-4Hz",
     "But the look wasn't scorn. It was the face of someone who "
     "already knew, and already loved him anyway."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He looked at Peter in his worst moment — and still chose him. "
     "He looks at you the same way."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present. Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
