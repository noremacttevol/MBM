#!/usr/bin/env python3
"""Narration for build-96-it-is-finished — John 19.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, and it is exact:
  j1  John 19:30  'It is finished.'
  Id kept. Three words, and they are the video.

RED ADDED -- his last sentence was missing. John records 'It is finished' and
then moves straight to the bowed head. Luke 23:46 records what he said in that
same breath, and a red-letter KJV inks it:
  jv46 Luke 23:46  'Father, into thy hands I commend my spirit.'
  n1c carries the retelling. It is from Luke rather than John, which is noted
  plainly here; the moment is the same moment and it is the last thing he says.

FRAMING LIFTED TO BLUE. n2 paraphrased the second half of John 19:30. That is
John writing, not Jesus speaking, so it is SCRIPTURE (light blue), never red:
  s30b John 19:30  'And he bowed his head, and gave up the ghost.'
  n2 keeps its id and now retells it.
And the veil, which n3a reported in modern English, is Matthew writing:
  s51  Matthew 27:51  'And, behold, the veil of the temple was rent in twain
       from the top to the bottom.'
  n3a keeps its id and now retells it. Tagged to Matthew because that is where
  the sentence comes from; this build's reference stays John 19.

RETELLING ADDED: n1b after 'It is finished'. The three words were being left to
carry themselves.

NO GREEN: the Father is spoken TO here and does not answer out loud.

WOMEN: John 19:25-27 puts Mary and the other women at the foot of the cross, but
the KJV records none of them speaking there. Nothing added, nothing invented.

CONSIDERED, LEFT OUT. Two red sayings from this hour were deliberately not used.
'I thirst' (John 19:28) is exact and it is two verses before this one, but this
video is built on a single declaration and a second short saying in front of it
would split the focus. 'Eloi, Eloi, lama sabachthani' (Mark 15:34) is exact and
it is red, and it was left out on purpose: it is the hardest sentence in the
Bible, it needs real teaching about what the Atonement cost, and this is a milk
video about a finished work. Reverence over completeness. Both verses are exact
if a later, more careful video wants them. (Note for whoever writes that one: the
KJV translation clause that follows, 'which is, being interpreted, My God, my
God, why hast thou forsaken me?', is Mark writing, not Jesus speaking, and would
need to be split off into blue.)

WHY-LAW: he did not lose. He finished. Milk: the work of getting you back to God
is not still in progress and not waiting on you -- it is done, and the way in is
standing open.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "At the very end, Jesus knew everything had now been accomplished. He wasn't a victim losing a fight — he was finishing a work."),
    ("n1", NARRATOR, "With his last breath he spoke three words that weren't a cry of defeat, but a declaration of completion."),
    # John 19:30
    ("j1", JESUS, "It is finished."),
    ("n1b", NARRATOR, "It is finished. Not I am finished. The thing he came to do was done — completed, paid in full, nothing left owing."),
    # Luke 23:46
    ("jv46", JESUS, "Father, into thy hands I commend my spirit."),
    ("n1c", NARRATOR, "The last words he said were words of trust, spoken to the Father he had been talking to all night."),
    # John 19:30
    ("s30b", SCRIPTURE, "And he bowed his head, and gave up the ghost."),
    ("n2", NARRATOR, "And he bowed his head and gave up the spirit — on his own terms, not theirs. Nobody took his life from him. He laid it down."),
    # Matthew 27:51
    ("s51", SCRIPTURE, "And, behold, the veil of the temple was rent in twain from the top to the bottom."),
    ("n3a", NARRATOR, "At that moment, in the temple across the city, the great veil that walled off the holiest place was torn in two, from the top down —"),
    ("n3b", NARRATOR, "as if torn by a hand from above."),
    ("n4a", NARRATOR, "That curtain had kept people out of God's presence for centuries. The instant he died, it was ripped open."),
    ("n4b", NARRATOR, "The way in was thrown wide — for everyone."),
    ("card", NARRATOR, "The curtain that kept you out was torn open the moment he died. The way to God is open. Walk in."),
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
