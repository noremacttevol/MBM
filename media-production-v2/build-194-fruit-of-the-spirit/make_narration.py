#!/usr/bin/env python3
"""Narration for build-194-fruit-of-the-spirit — Galatians 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Galatians 5:22-23. The one red beat moves to BLUE.

  s1  Galatians 5:22-23  'But the fruit of the Spirit is love, joy...'  RED -> SCRIPTURE

Galatians is an epistle. This is Paul writing to the churches of Galatia, not
Jesus speaking, and a red-letter King James Bible prints no red anywhere in
Galatians 5. The beat was simply misattributed. Light blue is correct - Paul is
one of the men with the pen, the shared `scripture` voice.

No split. The segment is one continuous sentence from one writer; there is no
seam in it.

Verbatim: s1 is Galatians 5:22-23 word for word, and the capital M on 'Meekness'
is not a typo - it is where the KJV starts verse 23, and the caption keeps the
true spelling. Nothing was smoothed and no word was reordered.

Retelling: already covered and unusually well. n1a, n1b, n2 and n3 walk the nine
fruits back through in plain modern English in the same order Paul lists them,
and n4 lands 'against such there is no law'. Four beats of retelling for one
quoted verse - no new narration was needed or added.

Nothing lifted from paraphrase. n0 is the storyteller introducing Paul in modern
English and is correctly narrator; it is not a buried quotation. The rest of the
narration is retelling, not paraphrase of some other verse.

Ids and beats unchanged. The card is 'card' and stays out of beats, as the
original had it.

WHY-LAW: milk. Character is fruit, not effort. The video does not argue law
versus grace - it just names the nine things and says no law forbids them.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Paul wrote that when God's Spirit lives in a person, a harvest grows — not crops, but character."),
    # Galatians 5:22-23
    ("s1", SCRIPTURE, "But the fruit of the Spirit is love, joy, peace, longsuffering, gentleness, goodness, faith, Meekness, temperance: against such there is no law."),
    ("n1a", NARRATOR, "First, love. Then joy."),
    ("n1b", NARRATOR, "Then peace — the kind that doesn't depend on circumstances."),
    ("n2", NARRATOR, "Longsuffering next — patience that doesn't quit. Then gentleness, and goodness, and faith that holds."),
    ("n3", NARRATOR, "Meekness, and temperance — self-control that masters the storms inside."),
    ("n4", NARRATOR, "And no law anywhere forbids any of it. These are the things that can't be overdone."),
    ("card", NARRATOR, "This fruit isn't grown by strain. Ask the Spirit — and let it ripen in you."),
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
