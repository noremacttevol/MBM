#!/usr/bin/env python3
"""Generate narration audio for Story Video #137 — Stephen Sees Him Standing
(Acts 7:55-56). From DRAFTS/row-137.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus does NOT speak in this passage. The exact KJV of Acts 7:56 is STEPHEN's
declaration — carried by the SCRIPTURE VOICE (Christopher) per the build-161
precedent (the narrator never quotes KJV; Christopher carries all exact KJV).
CONTENT-CARE (deep): the stoning is never in focus — reverent distance only;
faces carry the story. The Father is never depicted — glory-light only.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 split so the drag-out still and the looking-elsewhere still each
    # carry their half — draft words verbatim. Stoning stays off-focus.
    ("n0a", NARRATOR, "-20%", "-4Hz",
     "The council was furious. They dragged Stephen out and hurled "
     "stones."),
    ("n0b", NARRATOR, "-20%", "-4Hz",
     "But Stephen was looking somewhere else entirely."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Full of the Holy Ghost, he gazed up into heaven — and saw "
     "the glory of God."),
    # Exact KJV Acts 7:56 — Stephen's declaration, scripture voice.
    ("s1", SCRIPTURE, "-22%", "-2Hz",
     "Behold, I see the heavens opened, and the Son of man "
     "standing on the right hand of God."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Not sitting. Standing. As if ready to receive the one they "
     "were killing."),
    # sacred-silence beat follows n2.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The vision held him steady while the stones fell. He saw his "
     "Savior standing for him."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He stands for you too. Whatever falls on you today, you are "
     "not alone."),
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
