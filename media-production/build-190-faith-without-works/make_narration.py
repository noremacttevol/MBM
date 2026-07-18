#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #190 — Faith Without Works
Is Dead (James 2:14-26). From DRAFTS/row-190.md, validated against the laws.
MEMBER-FORMAT + TRANSLATION-LAW FIX: the draft had no scripture-voice
centerpiece and its narrator echoed James 2:17 nearly verbatim. Fixed:
James 2:17 added verbatim as the SCRIPTURE VOICE centerpiece (Christopher);
the narrator line is rewritten as plain paraphrase.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Faith" (THE-200 → GL).
Jesus does not appear (James's epistle).
CONTENT-CARE: the needy shown with dignity; Abraham at reverent distance —
obedience, never the act.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment (card included). No SPOKEN overrides
needed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "James wrote plainly to the early church: a faith that stays "
     "only in the head is already dead."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He asked the sharp question — if a brother or sister has no "
     "clothes and no food, and you wish them well but give "
     "nothing, what good is that?"),
    # Exact KJV James 2:17 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "Even so faith, if it hath not works, is dead, being alone."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Then he pointed to Abraham, who showed his faith by what he "
     "did — offering his son on the altar."),
    # sacred-silence beat follows n2.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "And to Rahab, who hid the spies and was counted righteous by "
     "her action, not just her words."),
    # n4 is split in two so each sentence lands on its own storyboard still
    # (s6 faith-made-visible, s7 live-the-words) per the CAPTION LAW.
    ("n4a", NARRATOR, "-20%", "-4Hz",
     "Belief that never moves a muscle isn't belief yet."),
    ("n4b", NARRATOR, "-20%", "-4Hz",
     "Faith and life belong together."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Real faith reaches out a hand. Let yours move — he sees "
     "every small, true thing you do."),
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
