#!/usr/bin/env python3
"""Narration for build-184-third-heaven — 2 Corinthians 12.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

This build is the rare epistle where a red beat is CORRECT, and it is the only one in
my set besides the Ascension.

  j1  2 Corinthians 12:9  'My grace is sufficient for thee: for my strength is made
      perfect in weakness.'  RED -> STAYS RED (jesus)

A red-letter King James Bible inks that clause. Paul is quoting the Lord's direct
answer to him word for word — 'And he said unto me' — so it is Christ speaking, not
Paul writing about Christ. Nothing moves out of red in this build. n2 already sets it
up correctly ('because of what the Lord had told him'), so the red lands on the right
sentence.

Everything else Paul says about himself is the writer, and the two segments that were
already not red are confirmed as light blue rather than left ambiguous:

  s1  2 Corinthians 12:2  -> scripture
  s2  2 Corinthians 12:4  -> scripture

No splits. The 'And he said unto me' clause that introduces the red line is not on
screen, so there is no mixed segment to break apart — n2 carries that job in the
narrator's voice already.

RETELLING: n3 was a one-line close that did not actually retell the red verse, which
is the strongest sentence in the video. It now says it in plain modern English first
and keeps its original closing thought after. No new segment ids were needed.

All three quoted verses are from the King James text as printed. Nothing left as
paraphrase from uncertainty.

WHY-LAW: milk. The man who saw the most had the least to say about it, and what he
repeated was not the vision — it was the sentence about grace. That is the whole
point, and it stays red because the Lord really said it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Paul wrote of a man he knew — caught up, in a single moment, far beyond the everyday world."),
    # 2 Corinthians 12:2
    ("s1", SCRIPTURE, "I knew a man in Christ above fourteen years ago, (whether in the body, I cannot tell; or whether out of the body, I cannot tell: God knoweth;) such an one caught up to the third heaven."),
    ("n1", NARRATOR, "Whether in the body or out of it, Paul could not say; God alone knew. And from that height, he was carried further still."),
    # 2 Corinthians 12:4
    ("s2", SCRIPTURE, "How that he was caught up into paradise, and heard unspeakable words, which it is not lawful for a man to utter."),
    ("n2", NARRATOR, "He heard things he was not allowed to repeat — words a person is not permitted to say out loud. He could have boasted. He had the credentials. Instead he pointed to his weakness — because of what the Lord had told him."),
    # 2 Corinthians 12:9
    ("j1", JESUS, "My grace is sufficient for thee: for my strength is made perfect in weakness."),
    ("n3", NARRATOR, "What I give you is enough, the Lord told him. My strength does its best work in the places where you are weakest. Paul was shown more than words can carry — and still pointed back to grace."),
    ("card", NARRATOR, "Paul was shown more than words can hold — and still pointed back to grace. There is more ahead than you can imagine."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
