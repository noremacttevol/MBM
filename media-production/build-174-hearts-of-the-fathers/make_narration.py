#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #174 — Elijah, and the
Hearts of the Fathers (Malachi 4:5-6; cf. Luke 1:17). From DRAFTS/row-174.md,
validated against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — the member verse-video format
(build-161 precedent) requires the exact KJV verses as the CENTERPIECE, read
by the SCRIPTURE VOICE (Christopher, cream italic caption, sacred silence).
Malachi 4:5-6 added verbatim as s1 (the "curse" is named in the verse per the
draft's own care note — never depicted; every image is mercy). Closing card
carries the Gospel Library pointer:
"Learn more — Gospel Library: Elijah; Family History" (THE-200 → GL).
Jesus does not appear as a character.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Before the great day, a messenger would come first — Elijah, "
     "the prophet, sent ahead."),
    # Exact KJV Malachi 4:5-6 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "Behold, I will send you Elijah the prophet before the coming "
     "of the great and dreadful day of the LORD: And he shall turn "
     "the heart of the fathers to the children, and the heart of "
     "the children to their fathers, lest I come and smite the "
     "earth with a curse."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "His work was not to thunder, but to mend. To turn the hearts "
     "of fathers back to their children, and children back to "
     "their fathers."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "So that when the Lord came, families would be ready — not "
     "divided, but whole."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The same spirit would later rest on John, preparing the "
     "way."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He cares about your family. Let the healing start with your "
     "own heart."),
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
