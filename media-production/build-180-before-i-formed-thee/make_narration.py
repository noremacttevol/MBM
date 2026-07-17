#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #180 — "Before I Formed
Thee in the Belly I Knew Thee" (Jeremiah 1:4-10). From DRAFTS/row-180.md,
validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
The LORD's words (Jeremiah 1:5 and 1:8, both verified exact) are carried by
the SCRIPTURE VOICE (Christopher) — the verse-video centerpiece is present in
the draft. The narrator never quotes KJV.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Premortal Existence" (THE-200 → GL).
No divine figure is depicted — the presence is light only.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment (card included). No SPOKEN overrides
needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "A young man named Jeremiah felt far too small for the job. "
     "God was calling him to speak to nations, and he was certain "
     "he could not do it."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "But the call did not begin the day he heard it. Long before "
     "he was born, before he ever drew a breath, the plan was "
     "already set."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The God who made him had already chosen him — and blessing, "
     "not pressure, was the shape of it."),
    # sacred-silence beat follows n2. Exact KJV Jer 1:5 — THE CENTERPIECE.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "Before I formed thee in the belly I knew thee; and before "
     "thou camest forth out of the womb I sanctified thee, and I "
     "ordained thee a prophet unto the nations."),
    # n3 split so Jeremiah's objection and the LORD's charge land on their own
    # stills (s2 only-a-child, s7 the-road-opens) per the CAPTION LAW.
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "Jeremiah answered that he was only a child."),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "The LORD replied — go where I send you, speak what I "
     "command, and do not be afraid, for I am with you to deliver "
     "you."),
    # Exact KJV Jer 1:8.
    ("s2", SCRIPTURE, "-24%", "-2Hz",
     "Be not afraid of their faces: for I am with thee to deliver "
     "thee, saith the LORD."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "The same God who knew you before you were born is the one "
     "who walks with you now. The calling is His; the courage is "
     "His gift."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "You were known before you were born. You are not too small "
     "for what He has for you."),
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
