#!/usr/bin/env python3
"""Generate narration audio for Story Video #99 — Flesh and Bone; Thomas's Hands
(Luke 24:36-43 / John 20:24-29). From DRAFTS/row-099.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Luke 24:39 (full), and John 20:27 ELIDED BY DESIGN — the clause "and reach
hither thy hand, and thrust it into my side:" is omitted for content-care
(no wound-touching imagery); the two spoken fragments are word-exact KJV in
their original order. Caption shows the same elided text.
PRE-FLIGHT FIX: the draft's n4 opened with a bare number ("Eight days
later...") — reworded per the NUMBER-STRESS law so the count lands stressed.
HOMOGRAPH LAW: ear-checked — no bow/wound(word)/wind/tears/lead/sow/live/read/
dove/bass/minute/use(d)/close in any segment ("handle" is not ambiguous).
No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "The disciples were hiding behind locked doors, afraid, when "
     "Jesus suddenly stood among them. They thought they were "
     "seeing a ghost."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He calmed them and showed them it was really him — flesh and "
     "bone, not a spirit."),
    # Exact KJV Luke 24:39.
    ("j1", JESUS, "-20%", "-2Hz",
     "Behold my hands and my feet, that it is I myself: handle me, "
     "and see; for a spirit hath not flesh and bones, as ye see me "
     "have."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "But Thomas wasn't there. And when they told him, he refused "
     "to believe it — unless he could see and touch for himself."),
    # sacred-silence beat follows n2.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "It was eight days later when Jesus appeared again — and he "
     "turned straight to Thomas, offering exactly what he'd "
     "demanded."),
    # Exact KJV John 20:27, elided by design (see docstring) — SILENCE around it.
    ("j2", JESUS, "-20%", "-2Hz",
     "Reach hither thy finger, and behold my hands; and be not "
     "faithless, but believing."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "He didn't scold Thomas for doubting. He met the doubt with "
     "his own hands. That's what he does with honest doubt — he "
     "steps toward it."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He met a doubter with open hands, not anger. Bring him your "
     "doubt. He can handle it."),
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
