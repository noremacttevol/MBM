#!/usr/bin/env python3
"""Narration for build-186-joint-heirs — Romans 8.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

s1 and s2 both move JESUS-RED -> SCRIPTURE (light blue). Two lines out of red.
Romans 8:16-17 is Paul writing to the saints at Rome. This is the exact case
Cameron named — red being used for Paul — and a red-letter KJV prints none of
Romans in red.

No mixed segments; both verses are Paul throughout and neither was split.

One new narrator beat, n0b, added between s1 and s2. Under the retelling rule
every Old English line gets said again in plain modern English, and as the build
stood the two verses ran back to back with the retelling of both arriving only
after the second. Splitting the retelling means the viewer understands verse 16
before verse 17 asks them to take the next step. n1 still retells s2, unchanged.

All original ids kept (n0, s1, s2, n1, n2, n3a, n3b, card). New id is n0b only.
It reuses ST2 as a second beat on the same still, so the picture the viewer sees
is unchanged and no artwork is needed.

MILK: joint-heirs is a large doctrine and the build does not reach for it. It
lets Paul say heirs of God, and joint-heirs with Christ in his own words, then
says the plain thing — you are family, not a visitor. Nothing about exaltation
is explained or argued. The verse carries it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Paul wrote to the believers in Rome about who they really were — not strangers, not outsiders."),
    # Romans 8:16
    ("s1", SCRIPTURE, "The Spirit itself beareth witness with our spirit, that we are the children of God:"),
    ("n0b", NARRATOR, "God's own Spirit tells your spirit the truth about you. Not a rumour, not a hope — a witness, given straight to you: you are a child of God."),
    # Romans 8:17
    ("s2", SCRIPTURE, "And if children, then heirs; heirs of God, and joint-heirs with Christ; if so be that we suffer with him, that we may be also glorified together."),
    ("n1", NARRATOR, "Children first — and because children, inheritors. What the Father has belongs to the family, and the family includes you."),
    ("n2", NARRATOR, "The terms were honest: share in his suffering, and you will share in his glory too."),
    ("n3a", NARRATOR, "Not earned by effort. Received by belonging."),
    ("n3b", NARRATOR, "Heirs together with the Son."),
    ("card", NARRATOR, "You're not a visitor at the table — you're family. Heir with the Son. Come home."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN, speaker), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
