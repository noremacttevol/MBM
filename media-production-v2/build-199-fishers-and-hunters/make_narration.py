#!/usr/bin/env python3
"""Narration for build-199-fishers-and-hunters — Jeremiah 16.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Jeremiah 16:16. The one red beat moves to GREEN.

  s1  Jeremiah 16:16  'Behold, I will send for many fishers, saith the LORD...'  RED -> GOD

The LORD speaking in the first person - 'I will send for many fishers', 'after
will I send for many hunters'. That is Jehovah, the premortal Christ, so it is
green. Jeremiah is Old Testament, so `jesus` is not available and would be wrong:
a red-letter KJV prints this black because Christ had not yet come in the flesh.

NOT SPLIT, deliberately. 'saith the LORD' sits three words into the verse and is
technically Jeremiah's attribution wrapper. Splitting it would make three beats
out of one sentence - green, blue, green - and put a colour flicker on the two
most important words in the build ('many fishers'). The clause is inside the
LORD's quoted speech rather than a narrator aside wrapped around it, and the
whole verse is one continuous first-person declaration. It stays one green beat.
Same call as build-191.

Verbatim: s1 is Jeremiah 16:16 word for word, including 'out of the holes of the
rocks'. Nothing was smoothed.

Retelling: already covered, and this build does it better than most. n1 retells
the verse directly ('the nets and the hunt find everyone'), and then n2, n3 and
n4 do the harder work of turning it over - the same God who sends the search
wants them found. No new narration was needed.

Nothing lifted from paraphrase. n0 is the storyteller setting up the chapter and
refers to the LORD in the third person, so it is not a quotation and stays white.
n4's 'the Fisher of men' is the narrator's own image drawing the Old Testament
picture forward, not a verse being cited.

Ids and beats unchanged. The card is 'card' and stays out of beats, as the
original had it.

WHY-LAW: milk, and this is the build in the set that most needed the care. The
verse is a judgement text and could easily be made frightening. The narration
already refuses to do that - it reads the search as God not letting his people
slip away unnamed. Green helps: the voice a listener hears is the peaceful one,
not a threatening one, which is exactly the reading the video argues for.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "The prophet Jeremiah spoke a hard word to a people who would not turn. The LORD said He would send searchers — and no hiding place would be far enough."),
    # Jeremiah 16:16
    ("s1", GOD, "Behold, I will send for many fishers, saith the LORD, and they shall fish them; and after will I send for many hunters, and they shall hunt them from every mountain, and from every hill, and out of the holes of the rocks."),
    ("n1", NARRATOR, "It is a picture of judgment — the nets and the hunt find everyone."),
    ("n2", NARRATOR, "But hear the mercy underneath: the same God who sends the search is the one who wants them found, not lost. Judgment is the last call, not the first."),
    ("n3", NARRATOR, "The point was never the catching — it was that a holy God would not let His people slip away unnamed. He seeks, even when seeking means discipline."),
    ("n4", NARRATOR, "For us the picture flips into hope: the Fisher of men searches still, not to condemn, but to bring home whoever will be found."),
    ("card", NARRATOR, "The hunt was a wake-up, not a goodbye. He's still searching for you — let yourself be found."),
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
