#!/usr/bin/env python3
"""Generate narration audio for Story Video #74 — The Woman Who Washed His Feet
(Luke 7:36-50). Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Luke 7:47, 7:48, 7:50 (fetched, not hand-typed; v48 and v50 are separate segments
with the v49 murmur between them, per the text).
CONTENT-CARE: her reputation is named once, in plain words, and NEVER depicted;
no shame framing; mercy is spoken out loud in the KJV lines. Dignity over spectacle.
HOMOGRAPH LAW: "tears" in n2 gets a SPOKEN respelling ("teers"); caption stays exact.
EAR-CHECK j1 for "loved"/"loveth" before assembly. No music bed: narration + silence.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "A Pharisee named Simon invited Jesus to dinner. It was a careful, "
     "respectable house — and it was about to be interrupted."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A woman from the town — a woman everyone in that room knew by her "
     "reputation — came in uninvited. She carried an alabaster jar of "
     "costly perfume."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "She stood behind him at his feet — guests reclined at meals like "
     "this, their feet stretched away from the table — and she was "
     "weeping. Her tears fell on his feet. She wiped them with her hair, "
     "kissed them, and poured out the perfume."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Simon thought to himself: if this man were really a prophet, he "
     "would know what kind of woman is touching him."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Jesus answered the thought Simon never said out loud — with a "
     "small story. There were two people in debt; one owed ten times "
     "more than the other; and the lender forgave them both. Which one, "
     "he asked, will love him more? Simon had to say it: the one who "
     "was forgiven more."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "Then he turned toward the woman — but kept talking to Simon. Look "
     "at her, he said. When I walked into your house, you offered me no "
     "water for my feet, no welcome, no oil. She has done nothing else "
     "since she came in."),
    # Exact KJV Luke 7:47 — sacred pause around it. EAR-CHECK loved/loveth.
    ("j1", JESUS, "-20%", "-2Hz",
     "Her sins, which are many, are forgiven; for she loved much: but "
     "to whom little is forgiven, the same loveth little."),
    # Exact KJV Luke 7:48 — SILENCE around it.
    ("j2", JESUS, "-18%", "-2Hz",
     "Thy sins are forgiven."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "The table stirred — who is this, who even forgives sins? He did "
     "not answer them. He was still looking at her."),
    # Exact KJV Luke 7:50 — SILENCE around it.
    ("j3", JESUS, "-18%", "-2Hz",
     "Thy faith hath saved thee; go in peace."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "She was known for the worst thing she'd done. He knew her for her "
     "love. Which name would you rather answer to?"),
]

# HOMOGRAPH LAW — n2 contains "tears" (must say /teerz/, never /tairz/):
# SPOKEN respelling for audio only; the caption keeps the true word "tears".
SPOKEN = {
    "n2": ("She stood behind him at his feet — guests reclined at meals like "
           "this, their feet stretched away from the table — and she was "
           "weeping. Her teers fell on his feet. She wiped them with her hair, "
           "kissed them, and poured out the perfume."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
