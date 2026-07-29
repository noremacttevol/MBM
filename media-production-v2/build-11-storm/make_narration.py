#!/usr/bin/env python3
"""Narration for build-11-storm — Mark 4.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

All three existing red beats are correctly red and were left alone - Mark 4 is
Jesus in the flesh and none of the three segments had narration welded onto them.
The real problem was that the disciples had no voice: the two lines Mark actually
records them saying were both sitting inside narrator paraphrase, so the video
was Jesus speaking into silence.

STAYED RED (jesus):
  j0  Mark 4:35  'Let us pass over unto the other side.'
  j1  Mark 4:39  'Peace, be still.'
  j2  Mark 4:40  'Why are ye so fearful? how is it that ye have no faith?'

LIFTED FROM PARAPHRASE - the disciples, so SCRIPTURE (light blue):
  s38  Mark 4:38  'Master, carest thou not that we perish?'
  s41  Mark 4:41  'What manner of man is this, that even the wind and the sea
                   obey him?'
These are the two hinges of the story. s38 is the accusation the whole video is
answering - they never doubted his power, they doubted his heart - and it was
being spoken in the storyteller's white voice as 'Teacher, don't you care that we
are going down?' s41 is the question the video ends on. Both are now verbatim and
blue, set against the red, which is exactly the contrast this story is made of.

EDITS TO EXISTING NARRATOR TEXT - both splits at natural seams, both halves on
the SAME still, no new artwork:
  n4 (S5) keeps its first sentence and now ends on the colon, handing to s38.
     Its remaining sentences become n4b, unchanged apart from the dropped
     paraphrase, and now serve as the retelling.
  n9 (S9) keeps everything up to 'and they asked each other:', hands to s41, and
     its closing lines about the old psalm become n9b.

BEATS FIX: n10 existed as a segment but appeared in NO beat in the original
running order, so it was never on screen. It is now placed on S7, the great-calm
still, as the closing word. This is a bug fix, not a rewrite - its text is
untouched.

NOTE ON THE CLOSER: this build has no segment literally named `card`; n10 is the
closing card and is left last and unedited.

WOMEN: Mark 4:35-41 records no woman speaking. Nothing was added rather than
importing a line from another passage.

WHY-LAW: he did not calm the storm from the shore. He was in the boat, and he
asked about their fear only after he had already saved them. Milk framing - he is
in it with you.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, 'Evening, on the Sea of Galilee. Jesus had been teaching crowds on the shore all day — story after story, until the light was going and his voice was nearly gone with it. He was worn through. And when the last story was told, he said to his friends:'),
    ("j0", JESUS, 'Let us pass over unto the other side.'),
    ("n1", NARRATOR, 'So they took him, Mark says, even as he was — no rest, no supper, straight from the last word into the boat. Other little boats followed them out.'),
    ("n1b", NARRATOR, 'And here is something worth knowing about the men at the oars: at least four of them were professional fishermen. Peter and his brother Andrew, and James and John, the sons of Zebedee. This lake was their workplace. They had crossed it at night their whole lives. Nothing about dark water scared them.'),
    ("n2", NARRATOR, "Then the lake turned on them. The Sea of Galilee lies seven hundred feet below sea level, in a bowl of hills — when cold wind spills down those slopes, calm water can turn violent in minutes. This storm was savage even by that lake's standard."),
    ("n2b", NARRATOR, 'Waves broke over the side faster than the men could bail. The boat was filling. And the fishermen who had survived a hundred storms looked at this one — and believed it was going to be their last.'),
    ("n3", NARRATOR, "And Jesus was asleep. In the stern, on the steersman's cushion, soaked with spray, rising and falling with the pitching deck — asleep. Not because he didn't know what was happening. Because he wasn't afraid of it."),
    ("n4", NARRATOR, 'So they woke him. Rough hands on his shoulder, screaming over the wind the question people have been asking in storms ever since:'),
    ("s38", SCRIPTURE, 'Master, carest thou not that we perish?'),
    ("n4b", NARRATOR, "Don't you care that we are going down? Listen to what they were really saying. They never doubted his power. They doubted his heart."),
    ("n5", NARRATOR, 'He got up. He stood in the stern of a sinking boat, in the middle of the worst storm those fishermen had ever seen. And he did not speak to the men. He spoke to the storm.'),
    ("j1", JESUS, 'Peace, be still.'),
    ("n6", NARRATOR, "And the wind quit. The sea fell flat — glass flat — with stars where the storm had been, and the only sound left was water dripping off the ropes. Sailors will tell you the waves keep rolling for hours after a wind dies. These didn't. The lake did not calm down. It obeyed."),
    ("n7", NARRATOR, 'Then he turned to his friends — soaked, shaking, still gripping the ropes — and he asked them, gently:'),
    ("j2", JESUS, 'Why are ye so fearful? how is it that ye have no faith?'),
    ("n8", NARRATOR, "Hear where he asked that from. Standing in their boat, on the sea he had just flattened to save them. He didn't ask it from the shore. He came through the storm with them — and then he asked why the fear had gotten so much bigger than their trust. He never said the storm wasn't real. He never scolded them for waking him. He was simply bigger than it."),
    ("n9", NARRATOR, "And then a strange thing happened: the fear didn't leave the boat — it changed direction. Mark says they feared exceedingly — more awe after the calm than in the storm — and they asked each other:"),
    ("s41", SCRIPTURE, 'What manner of man is this, that even the wind and the sea obey him?'),
    ("n9b", NARRATOR, 'These men knew their scriptures. They knew the old psalm that says it is God who stills the storm to a whisper. And now they were staring at a man in dripping clothes who had just done it.'),
    ("n10", NARRATOR, 'Whatever storm you are in tonight, hear this: the same Jesus is still in the boat with you. He has not left you alone in it. Bring him your fear, and let him speak his peace over your storm.'),
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
