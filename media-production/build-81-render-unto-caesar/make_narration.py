#!/usr/bin/env python3
"""Generate narration audio for Story Video #81 — Render Unto Caesar (Mark 12:13-17).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Mark 12:15b, 12:16 and 12:17 (fetched, not hand-typed). The officials' one-word
reply "Caesar's" is narrator-paraphrased, never voiced as KJV.
CONTENT-CARE: GREEN — the trap is tension only; no conflict or violence shown.
HOMOGRAPH LAW: no known offenders — SPOKEN empty; ear-check every segment anyway.
No music bed: narration + intentional silence only.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Some officials came to Jesus with a question built to trap him — "
     "flattering him first, so he'd let his guard down."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Is it lawful to pay taxes to Caesar, or not? Say yes, and the "
     "crowd turns on you. Say no, and Rome arrests you. There was no "
     "safe answer."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Jesus saw straight through it."),
    # Exact KJV Mark 12:15 (his words) — sacred pause around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "Why tempt ye me? bring me a penny, that I may see it."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "They brought one — a small silver Roman coin. He held it up where "
     "everyone could see."),
    # Exact KJV Mark 12:16 (his question) — SILENCE around it.
    ("j2", JESUS, "-20%", "-2Hz",
     "Whose is this image and superscription?"),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "They said it was Caesar's. And with that, the trap they had built "
     "swung shut on them instead."),
    # Exact KJV Mark 12:17 — SILENCE around it.
    ("j3", JESUS, "-18%", "-2Hz",
     "Render to Caesar the things that are Caesar's, and to God the "
     "things that are God's."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "The coin bore Caesar's image, so give it back to Caesar. But you "
     "bear God's image — so the real question is what you owe to the "
     "One whose face you carry."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The coin belonged to Caesar because it bore his face. You bear "
     "God's. What does that make you worth to him?"),
]

# HOMOGRAPH LAW — no bow/wound/wind/tears/lead/sow/live/read in these segments.
# ARTICULATION FIX (2026-07-17, ear-check): the neural voice reduced the unstressed
# "and" in "image and superscription" to a schwa that both whisper models heard as
# "in" — a real mis-say of Jesus's exact KJV. A comma before "and" (TTS only) forces
# it to land as a clear word; the caption keeps the exact KJV (no comma).
SPOKEN = {
    "j2": "Whose is this image, and superscription?",
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
