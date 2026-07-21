#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #179 — Stephen's Witness
(Acts 7:55-56). From DRAFTS/row-179.md, validated against the laws.
(Distinct from build-137: that is the bridge-shelf comfort telling; this is
the member-shelf GODHEAD witness — the Son standing, distinct, embodied, seen.)
TRANSLATION-LAW + MEMBER-FORMAT FIX: the draft's n3 put Acts 7:56 nearly
verbatim in the narrator's mouth — the exact KJV verse moves to the SCRIPTURE
VOICE (Christopher) as the verse-video CENTERPIECE (build-161 precedent).
Jesus APPEARS in the vision but does not speak in this passage — no Jesus
line is fabricated.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Godhead" (THE-200 → GL).
CONTENT-CARE (deep): no stones or injuries in focus, reverent distance.
REGEN 2026-07-21: the Father IS depicted — embodied per GOD-THE-FATHER-LOCK.md,
two distinct personages in the vision (narration already says so: n2/s1).
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
     "Stephen, full of the Holy Spirit, was dragged before the "
     "council for speaking the truth. He told them the whole story "
     "of Israel — and they boiled with rage."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "But Stephen didn't look at his accusers. He looked up, and "
     "what he saw changed everything."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "He saw the glory of God — and Jesus, standing at the right "
     "hand of the Father. And he said so, out loud:"),
    # sacred-silence beat. Exact KJV Acts 7:56 — THE CENTERPIECE.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "Behold, I see the heavens opened, and the Son of man "
     "standing on the right hand of God."),
    # n3/n4 split so each beat lands on its own still (CAPTION LAW). The
    # stoning is told with reverent distance — no gore, no stone striking
    # flesh in view (CONTENT-CARE, martyrdom).
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "They would not hear it. They rushed him out."),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "But Stephen's face was the face of an angel — at peace, not "
     "afraid."),
    ("n4a", NARRATOR, "-20%", "-4Hz",
     "His last words asked mercy for the ones throwing the "
     "stones."),
    ("n4b", NARRATOR, "-20%", "-4Hz",
     "Then he fell asleep."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He saw the Son of man standing to receive him. You can face "
     "your end with that same peace."),
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
