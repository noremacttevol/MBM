#!/usr/bin/env python3
"""Generate narration audio for Story Video #144 — "I Am the Resurrection and
the Life" (John 11:25-26). From DRAFTS/row-144.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 11:25 and 11:26 (both verified against the passage).
CONTENT-CARE: death handled with hope — no decay, no gore; faces and light.
HOMOGRAPH LAW: "live" (the #1 TTS offender) in j1 ("yet shall he live") —
must read /LIV/; SPOKEN respelling applied. 🛑 BUILDER MUST ALSO EAR-CHECK
j2 ("whosoever LIVETH") — must read /LIV-eth/, never /LYVE-eth/; the natural
reading is usually right, but LISTEN before assembly; a prepared override is
commented below. Captions keep the exact KJV words.

SEGMENTATION (ASSEMBLY-C, 2026-07-17): the draft's n1 and n3 are each split at
their sentence break so all 8 stills get a beat whose caption matches what is
being said at that moment (CAPTION LAW): n1a→s2 Martha speaks, n1b→s3 his face,
j1→s4 the promise two-shot, n2→s5 light from the seam, j2→s6 believest-thou,
n3a→s7 the weight lifting, n3b→s8 out of the tomb. Words unchanged from the
draft — only where the file boundaries fall.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Lazarus had been in the tomb four days. His sister Martha "
     "came to Jesus, heavy with grief but still full of faith."),
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "She said she believed her brother would rise again at the "
     "last day."),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "Jesus answered with a promise bigger than the last day."),
    # sacred-silence beat follows n1b. Exact KJV John 11:25.
    ("j1", JESUS, "-22%", "-2Hz",
     "I am the resurrection, and the life: he that believeth in "
     "me, though he were dead, yet shall he live:"),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Not a theory about life after death. He said He Himself is "
     "the life — and that trusting Him beats the grave."),
    # Exact KJV John 11:26.
    ("j2", JESUS, "-22%", "-2Hz",
     "And whosoever liveth and believeth in me shall never die. "
     "Believest thou this?"),
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "Martha said yes."),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "And moments later, her brother walked out of the tomb."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Death is not the end of the story. He is the life."),
]

# HOMOGRAPH LAW — j1 "live" respelled /LIV/. Ear-check j2 "liveth" too;
# if misread, uncomment its override. Captions keep the exact KJV words.
SPOKEN = {
    "j1": ("I am the resurrection, and the life: he that believeth in "
           "me, though he were dead, yet shall he liv:"),
    # j2 override APPLIED (ASSEMBLY-C 2026-07-17, build-50 precedent): forces
    # /LIV-eth/ — the caption still shows the exact KJV "liveth".
    "j2": ("And whosoever livveth and believeth in me shall never die. "
           "Believest thou this?"),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
