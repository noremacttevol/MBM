#!/usr/bin/env python3
"""Generate narration audio for Story Video #98 — Mary at the Tomb: Her Name
(John 20:11-18). From DRAFTS/row-098.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 20:16 — the single word "Mary." — delivered tenderly.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment ("weeping" is not ambiguous).
No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Mary Magdalene stayed behind at the tomb, weeping. She "
     "thought someone had taken his body, and grief was all she "
     "had left."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "She turned and saw a man standing there. Thinking he was the "
     "gardener, she begged — please, if you've moved him, tell me "
     "where."),
    # sacred-silence beat follows n1: the still holds on her grief.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "He said one word. Her name."),
    # Exact KJV John 20:16 — SILENCE around it. One word, tender.
    ("j1", JESUS, "-26%", "-2Hz",
     "Mary."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "And instantly she knew. Grief flipped to joy in a single "
     "heartbeat — he was alive, and he had come looking for HER, "
     "by name."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "He sent her to tell the others. The first person to see the "
     "risen Lord, and the first preacher of the resurrection, was "
     "a weeping woman he called by name."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He knows your name — and he speaks it even in your grief. "
     "Listen for it."),
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
