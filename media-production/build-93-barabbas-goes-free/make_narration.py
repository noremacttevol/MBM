#!/usr/bin/env python3
"""Generate narration audio for Story Video #93 — Barabbas Goes Free
(Mark 15:6-15). From DRAFTS/row-093.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus is SILENT in this passage — no KJV line, narrator only. The theology of
substitution is carried by the narration; mercy is spoken out loud.
CONTENT-CARE: no wounds, no scourging, no violence depicted or dwelt on.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "It was the custom at Passover for the governor to release one "
     "prisoner the crowd chose. Pilate had two men: Jesus, and a "
     "killer named Barabbas."),
    # n1 split so Pilate's judgment and his expectation land on their own
    # stills (s2 pilate-weighs-it, s3 the-innocent-one) per the CAPTION LAW.
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "Pilate could see Jesus had done nothing worth death."),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "He thought the crowd would surely pick the innocent one."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "But the leaders stirred the crowd, and they shouted for "
     "Barabbas. Pilate asked, then what about Jesus? And they "
     "cried, crucify him."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "So the guilty man walked free, and the innocent one was "
     "handed over in his place."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Think about what Barabbas got: he was condemned, and then "
     "someone else took his exact sentence. He walked out free "
     "because Jesus took his cross."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "That's not just Barabbas's story. That's the whole gospel in "
     "one swap — the innocent for the guilty, so the guilty could "
     "go free."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Barabbas walked free because the Son of God took his place. "
     "So can you. That's the whole point."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present. Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
