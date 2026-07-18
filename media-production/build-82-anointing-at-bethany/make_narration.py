#!/usr/bin/env python3
"""Generate narration audio for Story Video #82 — The Anointing at Bethany
(Mark 14:3-9). Narrator: modern, warm, low, unhurried (American). Plain US only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Mark 14:6, the FULL 14:8 (including the burial clause), and 14:9 (fetched, not
hand-typed). v7 is narrator-paraphrased. CONTENT-CARE: dignity throughout; the
burial hint is told gently; the indignation is tension, never violence.
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
    # n0 split: the table (s1) then the jar she carries (s2).
    ("n0a", NARRATOR, "-20%", "-4Hz",
     "In a house in Bethany, days before the end, a woman came to Jesus "
     "at the table."),
    ("n0b", NARRATOR, "-20%", "-4Hz",
     "She carried an alabaster jar of pure, costly perfume."),
    # n1 split: breaking the jar (s3) then pouring it over his head (s4).
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "She broke the jar open,"),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "and poured all of it over his head — a year's wages, gone in a "
     "moment."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Some at the table were angry. That could have been sold and given "
     "to the poor. They scolded her."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Jesus stopped them cold, and defended her."),
    # Exact KJV Mark 14:6 — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "Let her alone; why trouble ye her? she hath wrought a good work "
     "on me."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "There would always be chances to do good for the poor, he told "
     "them. But he would not be at their table much longer."),
    # Exact KJV Mark 14:8, the whole verse — sacred pause around it.
    ("j2", JESUS, "-20%", "-2Hz",
     "She hath done what she could: she is come aforehand to anoint my "
     "body to the burying."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "Whether she fully knew it or not, she was the only one in that "
     "room who had prepared him for what was coming."),
    # Exact KJV Mark 14:9 — SILENCE around it.
    ("j3", JESUS, "-18%", "-2Hz",
     "Verily I say unto you, Wheresoever this gospel shall be preached "
     "throughout the whole world, this also that she hath done shall be "
     "spoken of for a memorial of her."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "She gave the most extravagant thing she owned, and he received it "
     "as beautiful. Not wasteful — worship. And he was right about the "
     "memorial: all these centuries later, here we are, telling her "
     "story."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "She gave him her best and he called it beautiful. What would it "
     "mean to stop holding back from him?"),
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
