#!/usr/bin/env python3
"""Narration for build-198-ensign-for-the-nations — Isaiah 11.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Isaiah 11:11-12. Both red beats move to BLUE.

  s1  Isaiah 11:11  'And it shall come to pass in that day, that the Lord shall
                     set his hand again the second time...'                RED -> SCRIPTURE
  s2  Isaiah 11:12  'And he shall set up an ensign for the nations...'     RED -> SCRIPTURE

This is the one in the Old Testament set that is NOT green. Both segments are
Isaiah narrating ABOUT the Lord in the third person - 'the LORD SHALL set his
hand', 'HE shall set up an ensign', 'HIS people'. There is no first-person divine
speech anywhere in these two verses. That is the man with the pen describing what
God is going to do, so it is light blue, the shared scripture voice. Green would
have been the easy mistake here: the subject is God, but the speaker is Isaiah.

No splits. Neither segment mixes speakers - both are Isaiah start to finish, so
there is no seam and nothing to cut.

Verbatim: s1 is the opening of Isaiah 11:11 word for word and stops mid-verse at
'to recover the remnant of his people,' - the trailing comma is honest, the verse
carries on into the list of nations. That is a truncation, not an alteration, and
every word on screen is exact. s2 is Isaiah 11:12 complete and word for word,
including 'the dispersed of Judah from the four corners of the earth'. Neither
was smoothed.

TWO BLUE BEATS BACK TO BACK, on purpose. s1 runs into s2 with no narrator
between, which the validator flags. Same speaker, same sentence-run, consecutive
verses - Isaiah is building one thought across them, the recovery and then the
banner that causes it. n2 retells both immediately after: 'exiles in every
direction, lifted out of every nation, brought home. The ensign is the
invitation; the gathering is the answer.' The retelling rule is met once for the
pair rather than twice, which is right when the pair is one continuous prophecy
from one man.

Nothing lifted from paraphrase. n0 and n1 are the storyteller explaining the root
of Jesse and the raised banner in modern English. They gesture at Isaiah 11:1 and
11:10 but do not quote them, and adding a third Old English block to a six-beat
video would swamp it.

Ids and beats unchanged. The card is 'card' and stays out of beats, as the
original had it.

WHY-LAW: milk. A banner is raised so people can find their way to it. The
gathering is an invitation being answered, not a claim being staked.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "The prophet Isaiah pointed far ahead to a figure he called the root of Jesse — David's family tree, springing up fresh after it looked cut down."),
    ("n1", NARRATOR, "This one would stand as a banner, a signal, lifted up so the nations could find their way to Him. Not hidden. Raised for all to see."),
    # Isaiah 11:11
    ("s1", SCRIPTURE, "And it shall come to pass in that day, that the Lord shall set his hand again the second time to recover the remnant of his people,"),
    # Isaiah 11:12
    ("s2", SCRIPTURE, "And he shall set up an ensign for the nations, and shall assemble the outcasts of Israel, and gather together the dispersed of Judah from the four corners of the earth."),
    ("n2", NARRATOR, "Exiles in every direction, lifted out of every nation, brought home. The ensign is the invitation; the gathering is the answer."),
    ("n3", NARRATOR, "The banner is raised — and the seeking ones, from every people, come home."),
    ("card", NARRATOR, "A banner was raised so you could find your way. Seek Him, and you'll be gathered in."),
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
