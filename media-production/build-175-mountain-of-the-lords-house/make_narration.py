#!/usr/bin/env python3
"""Narration for build-175-mountain-of-the-lords-house — Isaiah 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

All three scripture beats were painted JESUS-RED and NONE of them is Deity
speaking. This whole build moves red -> BLUE, with no green anywhere:
  s1   Isaiah 2:2   'And it shall come to pass in the last days...'  RED -> SCRIPTURE
  s2a  Isaiah 2:3a  'And many people shall go and say, Come ye...'   RED -> SCRIPTURE
  s2b  Isaiah 2:3b  'for out of Zion shall go forth the law...'      RED -> SCRIPTURE

This is the case the law calls subtle, and it is worth being explicit about.
Every one of these lines is ABOUT the LORD - his house, his mountain, his ways,
his word - but not one of them is the LORD talking. Isaiah is the man with the
pen throughout: 'the mountain of the LORD's house SHALL BE established', 'HE
will teach us of HIS ways'. Third person, every time. Green would have put words
in God's mouth that Isaiah wrote about him.

s2a is a second layer of the same thing - Isaiah quoting what the nations will
one day say to each other. Quoted people in the stories are `scripture` under the
law, so it stays blue rather than picking up a colour of its own.

NO SPLIT anywhere. s2a/s2b are the two halves of Isaiah 2:3 and were already
separate segments in the original; both halves are Isaiah, so the seam does not
need a colour change. They stay consecutive with no narrator wedged between,
because n1 and n2a immediately after them already retell both halves.

ADDED n0b - a plain-English retelling of Isaiah 2:2. Without it, three verses of
Old English ran back to back before the storyteller said a word. n0b sits on S2,
the same still as s1, so the edit is unchanged.

Nothing left as paraphrase from uncertainty; all three are verbatim Isaiah 2:2-3.

WHY-LAW: milk. The mountain draws, it never drags. Nations 'flow' to it and
people invite each other up - the pull is the point, and the video never argues
whose mountain it is.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "In the last days, a mountain would rise above all mountains — not by height, but by drawing every people to it."),
    # Isaiah 2:2
    ("s1", SCRIPTURE, "And it shall come to pass in the last days, that the mountain of the LORD's house shall be established in the top of the mountains, and shall be exalted above the hills; and all nations shall flow unto it."),
    ("n0b", NARRATOR, "That is Isaiah writing, not God speaking — a prophet describing what he was shown. In the last days, he says, the house of the Lord will be set up higher than anything else on earth, and people from every nation will come streaming toward it."),
    # Isaiah 2:3
    ("s2a", SCRIPTURE, "And many people shall go and say, Come ye, and let us go up to the mountain of the LORD, to the house of the God of Jacob; and he will teach us of his ways, and we will walk in his paths:"),
    # Isaiah 2:3
    ("s2b", SCRIPTURE, "for out of Zion shall go forth the law, and the word of the LORD from Jerusalem."),
    ("n1", NARRATOR, "Nations streaming uphill — not summoned by force, but drawn by invitation. The mountain everyone chooses to climb."),
    ("n2a", NARRATOR, "And from that high place, God's teaching would go out"),
    ("n2b", NARRATOR, "to everyone, everywhere."),
    ("card", NARRATOR, "The mountain is open to you. Come, and walk in his paths."),
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
