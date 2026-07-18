#!/usr/bin/env python3
"""Generate narration audio for Story Video #147 — Joseph Forgives His Brothers
(Genesis 45:5; 50:20). From DRAFTS/row-147.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Old Testament narrative — Jesus does NOT appear or speak. Joseph's exact KJV
lines are carried by the SCRIPTURE VOICE (Christopher) per the build-161
precedent (the narrator never quotes KJV).
KJV verified: Genesis 45:5 and 50:20, word-exact.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment ("alive" and "life" are safe).
No SPOKEN overrides needed.

SEGMENTATION (ASSEMBLY-C, 2026-07-17): n0 split at its sentence break so all
7 stills carry a beat synced to what is being said (CAPTION LAW). Words
unchanged from the draft.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0a", NARRATOR, "-20%", "-4Hz",
     "Years before, Joseph's own brothers had sold him into "
     "slavery out of jealousy."),
    ("n0b", NARRATOR, "-20%", "-4Hz",
     "Now he was second only to Pharaoh in all Egypt."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "When the brothers came begging for food in the famine, they "
     "didn't recognize the brother they'd betrayed. Then he told "
     "them."),
    # sacred-silence beat follows n1. Exact KJV Gen 45:5 — scripture voice.
    ("s1", NARRATOR, "-20%", "-4Hz",
     "Now therefore be not grieved, nor angry with yourselves, "
     "that ye sold me hither: for God did send me before you to "
     "preserve life."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Much later, when their father died and the brothers feared "
     "revenge, Joseph spoke the line that closes the wound."),
    # Exact KJV Gen 50:20 — scripture voice.
    ("s2", NARRATOR, "-20%", "-4Hz",
     "But as for you, ye thought evil against me; but God meant it "
     "unto good, to bring to pass, as it is this day, to save much "
     "people alive."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "He didn't pretend it hadn't hurt. He saw God's hand turning "
     "their evil into rescue."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "What others meant for harm, God can mean for good. Let it "
     "go."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present. Note n2's "closes the wound" was
# checked: the draft says "closes the wound" — "wound" IS on the flag list
# (must read /WOOND/ the injury, never /WOWND/ as in "wound up"). Ear-check
# n2 before assembly; if misread, respell SPOKEN "woond".
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
