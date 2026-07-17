#!/usr/bin/env python3
"""Generate narration audio for Story Video #94 — "Father, Forgive Them"
(Luke 23:33-34). From DRAFTS/row-094.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Luke 23:34 (verified against the passage, not hand-typed from memory).
CONTENT-CARE (deepest): the crucifixion is carried with reverent distance —
no gore, no wounds dwelt on, mercy spoken out loud.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "They brought him to a place called Calvary, and there they "
     "crucified him — between two criminals, at the hands of "
     "soldiers just following orders."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He had every reason to curse them. Every right to call down "
     "judgment."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Instead, the first words out of his mouth on the cross were "
     "a prayer — for the very people driving the nails."),
    # Exact KJV Luke 23:34 — SILENCE around it.
    ("j1", JESUS, "-22%", "-2Hz",
     "Father, forgive them; for they know not what they do."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Not, forgive them later, if they're sorry. Forgive them "
     "now — while it's still happening."),
    # n4 split so the reach and the reassurance land on their own stills (s6
    # light-toward-the-center-cross, s7 mercy-reaching-down) per CAPTION LAW.
    ("n4a", NARRATOR, "-20%", "-4Hz",
     "That is how far his mercy reaches. If it covered the ones "
     "killing him,"),
    ("n4b", NARRATOR, "-20%", "-4Hz",
     "there is no one, and nothing you've done, it can't cover."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "His first words on the cross were mercy for the ones who put "
     "him there. That mercy has your name in it too."),
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
