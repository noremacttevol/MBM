#!/usr/bin/env python3
"""Narration for build-150-shepherd-psalm — Psalm 23.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

One line was red — s1, 'The LORD is my shepherd; I shall not want.' That is David
writing, not Jehovah speaking, so it is SCRIPTURE (light blue), not red and not green.
The LORD is the subject of the psalm; He is never the speaker in it.

The bigger fix: the entire rest of the psalm was in modern paraphrase. Psalm 23 is the
one passage in the Bible that people actually know BY ITS KING JAMES WORDING. A video
about it that never says 'he maketh me to lie down in green pastures' is not the psalm.
So all six verses are now spoken verbatim as SCRIPTURE, each followed by the existing
narrator line as its retelling. Every original id is kept and every narrator line is
left in its original place doing exactly the job the retelling rule asks for — they
were already plain-English retellings, they just had nothing to retell.

Verses 3, 5 and 6 are split at their colons so each half sits with the narrator line
that already retold it. Splits stay on the same still.

Psalm is Old Testament, nothing is `jesus`. Every quoted line is verbatim KJV; I am
certain of all six verses. Nothing left as paraphrase.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Three thousand years ago a shepherd-king wrote a song about being shepherded himself. It starts like this:"),
    # Psalm 23:1
    ("s1", SCRIPTURE, "The LORD is my shepherd; I shall not want."),
    ("n0b", NARRATOR, "The Lord takes care of me. There is nothing I need that I won't have. That is the whole psalm in one line — everything after it is David showing his work."),
    # Psalm 23:2
    ("s2", SCRIPTURE, "He maketh me to lie down in green pastures: he leadeth me beside the still waters."),
    ("n1a", NARRATOR, "He leads me to quiet water and green places to rest."),
    # Psalm 23:3
    ("s3a", SCRIPTURE, "He restoreth my soul:"),
    ("n1b", NARRATOR, "He puts my life back together."),
    # Psalm 23:3
    ("s3b", SCRIPTURE, "he leadeth me in the paths of righteousness for his name's sake."),
    ("n2", NARRATOR, "He guides me down the right paths, for His name's sake — not because I earned the guiding, but because of who He is."),
    # Psalm 23:4
    ("s4", SCRIPTURE, "Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me; thy rod and thy staff they comfort me."),
    ("n3", NARRATOR, "Even in the darkest valley, I'm not afraid. You are with me — Your rod and staff steady me. And notice what changes right there: up to now David has been saying He. In the valley he starts saying You. He gets closer to the Shepherd in the dark, not further away."),
    # Psalm 23:5
    ("s5a", SCRIPTURE, "Thou preparest a table before me in the presence of mine enemies:"),
    ("n4a", NARRATOR, "You set a table for me right in front of my enemies."),
    # Psalm 23:5
    ("s5b", SCRIPTURE, "thou anointest my head with oil; my cup runneth over."),
    ("n4b", NARRATOR, "You honor me; my cup runs over."),
    # Psalm 23:6
    ("s6a", SCRIPTURE, "Surely goodness and mercy shall follow me all the days of my life:"),
    ("n5a", NARRATOR, "Your goodness and Your mercy will chase me down every day I have."),
    # Psalm 23:6
    ("s6b", SCRIPTURE, "and I will dwell in the house of the LORD for ever."),
    ("n5b", NARRATOR, "And I'll be home with You forever."),
    ("card", NARRATOR, "The Shepherd who leads, restores, and walks the dark valley with you is the same One who invites you home. Let Him lead."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


SPOKEN.update({'leadeth': 'leedeth'})  # round2 in-context A/B winners 2026-07-20 (SWEEP/round2-state.json)
SPOKEN.update({'maketh': 'maykith'})  # 2026-07-21: Steffan reads plain "maketh" as "MOCKED (with)" — shipped Psalm 23 said "He mocked me to lie down". Round 2 2026-07-21: 'makith' proved unstable in Steffan (fresh renders 'may keep'); 'maykith' round-trips "maketh" exactly = MAY-kith. Caption keeps KJV "maketh".

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
