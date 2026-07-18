#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #177 — "Make Me a
Sanctuary; That I May Dwell Among Them" (Exodus 25:8). From
DRAFTS/row-177.md, validated against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — the member verse-video format
(build-161 precedent) requires the exact KJV verse as the CENTERPIECE, read by
the SCRIPTURE VOICE (Christopher, cream italic caption, sacred silence).
Exodus 25:8 added verbatim as s1.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Temples" (THE-200 → GL).
No divine figure is depicted (the presence is cloud and light only).
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
     "While Israel camped in the wilderness, the LORD gave Moses a "
     "strange instruction — have the people build me a sanctuary."),
    # Exact KJV Exodus 25:8 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "And let them make me a sanctuary; that I may dwell among "
     "them."),
    # NOTE (ASSEMBLY-C): played AFTER n2 so the how/pattern stills (s3/s4)
    # precede the dwell/near payoff — reads well, all words unchanged.
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "Not for his sake. For theirs."),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "So that he could dwell among them in the middle of their "
     "ordinary days."),
    ("n2a", NARRATOR, "-20%", "-4Hz",
     "He told them exactly how — the ark, the table, the "
     "lampstand —"),
    ("n2b", NARRATOR, "-20%", "-4Hz",
     "every detail meant to say: I am near."),
    # sacred-silence beat follows n2b.
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "The pattern was carried by a people on the move,"),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "yet the promise was fixed — God with his people."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Centuries later that promise would take a face. But here it "
     "begins as a tent in the desert, God pitching his tent beside "
     "them."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He wanted to live among his people then. He wants to live "
     "among you now."),
]

# HOMOGRAPH LAW — 🛑 the CARD contains "live" TWICE ("to live among his
# people... to live among you") — the #1 TTS offender, verb, must read /LIV/.
# SPOKEN respelling applied; the caption keeps the true spelling. Ear-check.
SPOKEN = {
    "card": ("He wanted to liv among his people then. He wants to liv "
             "among you now."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
