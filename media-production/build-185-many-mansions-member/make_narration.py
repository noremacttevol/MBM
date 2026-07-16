#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #185 — "In My Father's
House Are Many Mansions" (John 14:2-3). From DRAFTS/row-185.md, validated
against the laws.
(Distinct from build-133: that bridge-shelf video covers John 14:1-3 with the
v3 return promise as narrator paraphrase; this member verse-video speaks BOTH
verses exact — prepared rooms, degrees of nearness.)
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 14:2 and 14:3 (both verified against the passage) — the centerpiece.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Heaven" (THE-200 → GL).
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment (card included). No SPOKEN overrides
needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "On the night before everything changed, Jesus sat with his "
     "disciples and told them not to let their hearts be "
     "troubled."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He was going somewhere — but not to leave them orphaned. He "
     "was going to get a place ready."),
    # Exact KJV John 14:2 — THE CENTERPIECE.
    ("j1", JESUS, "-22%", "-2Hz",
     "In my Father's house are many mansions: if it were not so, I "
     "would have told you. I go to prepare a place for you."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "A house with room for everyone. He said it plainly — if it "
     "were not true, he would have told them."),
    # sacred-silence beat follows n2. Exact KJV John 14:3.
    ("j2", JESUS, "-22%", "-2Hz",
     "And if I go and prepare a place for you, I will come again, "
     "and receive you unto myself; that where I am, there ye may "
     "be also."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "He was not describing a far-off maybe. He was promising to "
     "come back and carry them home himself."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He went to prepare a place — and he's coming back for you. "
     "You are not forgotten."),
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
