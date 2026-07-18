#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #175 — The Mountain of the
LORD's House (Isaiah 2:2-3). From DRAFTS/row-175.md, validated against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — the member verse-video format
(build-161 precedent) requires the exact KJV verses as the CENTERPIECE, read
by the SCRIPTURE VOICE (Christopher, cream italic caption, sacred silence).
Isaiah 2:2 and 2:3 added verbatim as s1/s2.
TRANSLATION-LAW FIX: the draft's n3 echoed "out of Zion shall go forth the
law, and the word of the LORD from Jerusalem" nearly verbatim in the
narrator's mouth — reworded to plain modern words.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Temples" (THE-200 → GL).
Jesus does not appear as a character.
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
    ("n0", NARRATOR, "-20%", "-4Hz",
     "In the last days, a mountain would rise above all "
     "mountains — not by height, but by drawing every people to "
     "it."),
    # Exact KJV Isaiah 2:2 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "And it shall come to pass in the last days, that the "
     "mountain of the LORD's house shall be established in the top "
     "of the mountains, and shall be exalted above the hills; and "
     "all nations shall flow unto it."),
    # Exact KJV Isaiah 2:3, split at the colon into two flowing pieces so it
    # spans two stills (s2a on s3 faces-upward, s2b on s4 the-path-upward).
    ("s2a", SCRIPTURE, "-24%", "-2Hz",
     "And many people shall go and say, Come ye, and let us go up "
     "to the mountain of the LORD, to the house of the God of "
     "Jacob; and he will teach us of his ways, and we will walk in "
     "his paths:"),
    ("s2b", SCRIPTURE, "-24%", "-2Hz",
     "for out of Zion shall go forth the law, and the word of the "
     "LORD from Jerusalem."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Nations streaming uphill — not summoned by force, but drawn "
     "by invitation. The mountain everyone chooses to climb."),
    # sacred-silence beat follows n1.
    ("n2a", NARRATOR, "-20%", "-4Hz",
     "And from that high place, God's teaching would go out"),
    ("n2b", NARRATOR, "-20%", "-4Hz",
     "to everyone, everywhere."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The mountain is open to you. Come, and walk in his paths."),
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
