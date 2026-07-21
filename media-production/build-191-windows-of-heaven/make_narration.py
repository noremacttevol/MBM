#!/usr/bin/env python3
"""Narration for build-191-windows-of-heaven — Malachi 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Malachi 3:10. The one red beat moves to GREEN.

  s1  Malachi 3:10  'Bring ye all the tithes into the storehouse...'  RED -> GOD

This is the LORD speaking in the first person for the whole segment - 'prove me
now herewith', 'if I will not open you the windows of heaven', 'pour you out a
blessing'. That is Jehovah, the premortal Christ, so it is green. Malachi is Old
Testament, so `jesus` is not available and would be wrong anyway: a red-letter
KJV leaves this black because Christ had not yet come in the flesh.

NOT SPLIT, deliberately. 'saith the LORD of hosts' sits in the middle of the
verse and is technically Malachi's attribution wrapper. Splitting it out would
make three beats out of one breath - green, blue, green - for four words, and
the colour would flicker mid-sentence for no gain. The clause is inside the
LORD's own quoted speech, not a narrator aside around it, so the whole verse
stays one green beat. This is the judgement call the law asks for.

Verbatim: s1 is Malachi 3:10 word for word, KJV, including 'meat in mine house'.
Nothing was smoothed.

Retelling: already covered. n2 ('test me, and see if I don't open the windows'),
n3a and n3b carry the verse into plain modern English across three beats. No new
narrator beat was needed.

Nothing lifted from paraphrase. n0 and n1 are the storyteller setting the scene
in modern English about the LORD and the storehouse - narrator is correct for
both; neither is a buried quotation.

Beats unchanged. The card is 'card' and stays out of beats, as the original had it.

WHY-LAW: milk. The invitation is the whole point - God asks to be tested on his
generosity. Nothing on screen argues about tithing law. 2026-07-21: added n2b (same still ST4) — the cut ran 59.3s, 0.8s under the 60s floor.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Through the prophet Malachi, the LORD made a strange offer to a people holding back — bring everything in, and watch what I do."),
    ("n1", NARRATOR, "The storehouse was the place set apart for the Lord's house, and the tithe was the part meant for him."),
    # Malachi 3:10
    ("s1", GOD, "Bring ye all the tithes into the storehouse, that there may be meat in mine house, and prove me now herewith, saith the LORD of hosts, if I will not open you the windows of heaven, and pour you out a blessing, that there shall not be room enough to receive it."),
    ("n2", NARRATOR, "A dare no king could make — test me, and see if I don't open the windows."),
    ("n2b", NARRATOR, "He is the only one in scripture who ever says: prove me. Put me to the test, and watch what I do."),
    ("n3a", NARRATOR, "Not a trickle."),
    ("n3b", NARRATOR, "A pouring out, more than there is room to hold."),
    ("card", NARRATOR, "He invites you to test his goodness. Bring it all, and watch the windows open."),
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
