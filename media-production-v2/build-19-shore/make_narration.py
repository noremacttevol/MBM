#!/usr/bin/env python3
"""Narration for build-19-shore — John 21.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both existing red beats are the risen Christ speaking on the shore
and a red-letter KJV prints both.
  j1  John 21:16  'Simon, son of Jonas, lovest thou me?'
  j2  John 21:16  'Feed my sheep.'
Neither had John's framing welded on, so neither needed splitting.

ADDED RED -- the dawn on the water was all paraphrase. n5 told the viewer that a
figure called out and told them where to cast, without ever letting him say it.
Both of his lines are red-letter, and both are now in his own voice, on the SAME
still S3:
  j0a  John 21:5  'Children, have ye any meat?'
  j0b  John 21:6  'Cast the net on the right side of the ship, and ye shall find.'
n5 is trimmed to the frame only; n5b and n5c are the retellings, one for each.

ADDED BLUE -- PETER'S ANSWER. The whole video is one exchange and Peter's half of
it was narrator paraphrase in white (n12, 'yes, Lord, you know that I love you').
Lifted verbatim as SCRIPTURE -- Peter is an apostle, not Deity, so light blue:
  s16  John 21:16  'Yea, Lord; thou knowest that I love thee.'
This is a deliberate question-and-answer pair with j1 across two beats, with n11
retelling the question in between so nothing lands unexplained. n12 keeps its
original text and now works as the retelling of Peter's real words.

LEFT AS PARAPHRASE ON PURPOSE: n6's 'it is the Lord.' John 21:7 reads 'Therefore
that disciple whom Jesus loved saith unto Peter, It is the Lord.' The quoted
words are only three, and lifting them would need its own frame and its own
retelling for almost no gain. Left in the storyteller's voice.

WOMEN: John 21 records no woman speaking. Nothing added; nothing invented.

NO GREEN: no voice from heaven in John 21.

WHY-LAW: three denials by a charcoal fire, three questions by another one. He did
not bring up the failure, he asked about the love -- and then trusted him again.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, 'Peter had sworn he would die before he would ever deny Jesus.'),
    ("n2", NARRATOR, 'Then, in one terrible night, he denied him three times. The rooster crowed, Jesus turned and looked at him, and Peter went out and wept bitterly.'),
    ("n3", NARRATOR, 'After the resurrection, Peter went back to fishing. Back to the old life.'),
    ("n4", NARRATOR, 'It is what people do with a failure they cannot carry. They go back to what they knew before it happened. And that night they caught nothing.'),
    ("n5", NARRATOR, 'At dawn, a figure on the shore called out across the water to the boat.'),
    ("j0a", JESUS, 'Children, have ye any meat?'),
    ("n5b", NARRATOR, 'Their answer was only one word: no. All night, nothing.'),
    ("j0b", JESUS, 'Cast the net on the right side of the ship, and ye shall find.'),
    ("n5c", NARRATOR, 'They did — and it came up so full they could not haul it in.'),
    ("n6", NARRATOR, 'Then one of them went very still and said, it is the Lord. And Peter did not wait for the boat. He threw himself into the sea and swam for shore, leaving everything behind.'),
    ("n7", NARRATOR, 'When he waded out of the water, he stopped cold. On the sand was a charcoal fire, with fish already laid over it, and bread.'),
    ("n8", NARRATOR, 'A charcoal fire. The same kind of fire Peter had stood beside in the courtyard the night he denied him. The smell alone would have brought the whole night back.'),
    ("n9", NARRATOR, 'Jesus did not bring up the denial. He simply had breakfast waiting, and they ate together on the shore in the first gold light.'),
    ("n10", NARRATOR, "When breakfast was over, Jesus turned to Peter. Three times, once it seems for each denial, he asked him the same question, using Peter's old name, the name he had before any of it:"),
    ("j1", JESUS, 'Simon, son of Jonas, lovest thou me?'),
    ("n11", NARRATOR, 'Not, how could you. Not, prove it. Not one word thrown back at him about the denial.'),
    ("s16", SCRIPTURE, 'Yea, Lord; thou knowest that I love thee.'),
    ("n12", NARRATOR, 'Peter answered each time. Every answer cost him more, and every answer carried more of the truth.'),
    ("j2", JESUS, 'Feed my sheep.'),
    ("n13", NARRATOR, 'To the man who had failed him worst, Jesus handed the biggest job of all. He did not only forgive Peter. He trusted him again.'),
    ("n14", NARRATOR, 'That is how good he is. He takes your worst night and hands you back your life, with a purpose bigger than the one you thought you had thrown away.'),
    ("card", NARRATOR, 'Peter went back to fishing because he thought his failure was final. Is there a failure you have quietly decided is final?'),
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
