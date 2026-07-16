#!/usr/bin/env python3
"""Generate narration audio for Story Video #149 — Hannah Is Heard
(1 Samuel 1:9-20). From DRAFTS/row-149.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Old Testament narrative — Jesus does not appear; no KJV is quoted (Hannah's
vow is the narrator's modern paraphrase, which the Translation Law permits).
CONTENT-CARE: barrenness carried with compassion, never shame; Hannah's
sorrow held with dignity.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment ("life" in n2 is the noun, safe; the
draft's tears/live flags refer to words not present in the final text).
No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Year after year, Hannah went to the house of the LORD and "
     "came away with an empty lap. The other wife mocked her for "
     "it."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "One year at Shiloh, Hannah slipped to the door of the "
     "tabernacle and prayed with a voice no one could hear — only "
     "her lips moved."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Lord of hosts, she whispered, give me a son, and I'll give "
     "him back to You for all his life."),
    # sacred-silence beat follows n2.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Eli the priest thought she was drunk. She told him no — she "
     "was pouring out her soul in deep sorrow."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Eli blessed her. She went away, and her face was no longer "
     "sad. The LORD remembered her."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "A boy was born. She named him Samuel — because I have asked "
     "him of the LORD."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "She kept her word. When he was weaned, she brought him to "
     "the house of the LORD and left him there to serve."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Hannah prayed the prayer no one else could hear, and God "
     "answered. Your quiet prayers are heard too."),
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
