#!/usr/bin/env python3
"""Generate narration audio for Story Video #79 — The Seventy Sent
(Luke 10:1-9, 17-20). Narrator: modern, warm, low, unhurried (American). Plain US.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Luke 10:2, 10:9, and the FULL 10:20 including "Notwithstanding in this" (fetched,
not hand-typed). CONTENT-CARE: v17's devils are narrator-paraphrased in one gentle
line and NEVER depicted (Adversary law); v18-19 imagery is not used.
HOMOGRAPH LAW: no known offenders — SPOKEN empty; ear-check every segment anyway.
No music bed: narration + intentional silence only.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus picked seventy of his followers and sent them out two by "
     "two, ahead of him, into every town he was about to visit."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He didn't send them with much — no extra bag, no spare sandals, "
     "no backup plan. Just each other, and a message."),
    # Exact KJV Luke 10:2 — sacred pause around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "The harvest truly is great, but the labourers are few: pray ye "
     "therefore the Lord of the harvest, that he would send forth "
     "labourers into his harvest."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Wherever they were welcomed, they were to heal the sick and say "
     "the same simple thing."),
    # Exact KJV Luke 10:9 (the message he gave them) — SILENCE around it.
    ("j2", JESUS, "-18%", "-2Hz",
     "The kingdom of God is come nigh unto you."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "They came back amazed — even the dark things had listened when "
     "they spoke in his name. And Jesus told them what to actually "
     "celebrate."),
    # Exact KJV Luke 10:20, the whole verse — SILENCE around it.
    ("j3", JESUS, "-20%", "-2Hz",
     "Notwithstanding in this rejoice not, that the spirits are subject "
     "unto you; but rather rejoice, because your names are written in "
     "heaven."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Your name, written in heaven — that's the joy he wanted them to "
     "keep. It's meant for you as well."),
]

# HOMOGRAPH LAW — no bow/wound/wind/tears/lead/sow/live/read in these segments;
# SPOKEN stays empty. Ear-check every segment before assembly regardless.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
