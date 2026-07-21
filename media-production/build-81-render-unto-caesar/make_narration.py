#!/usr/bin/env python3
"""Narration for build-81-render-unto-caesar — Mark 12.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, all three. j1 (Mark 12:15), j2 (12:16) and j3 (12:17) are Jesus in
the flesh and a red-letter KJV inks every one, 'Render to Caesar' included.

THE QUESTION IS LIGHT BLUE, NOT RED. The Pharisees and Herodians are people in
the story, so they are SCRIPTURE like anyone else quoted from the KJV. Their
whole approach was sitting in the video as modern paraphrase:
  s14  Mark 12:14-15  'Master, we know that thou art true, and carest for no man:
       for thou regardest not the person of men, but teachest the way of God in
       truth: Is it lawful to give tribute to Caesar, or not? Shall we give, or
       shall we not give?'  The flattery and the trap are one continuous speech
       and they belong together - you cannot hear how oily it is until you hear
       the compliment attached to the question. n1 keeps its id and text and now
       retells it.
  s16  Mark 12:16  'And they said unto him, Caesar's.'  n4 keeps its id and now
       retells it.

TWO FRAMING SPLITS, both halves on the SAME still each time - no new artwork:
  s15  Mark 12:15  'But he, knowing their hypocrisy, said unto them,'  then j1 on
       S4. Mark writing, so light blue; the red starts at 'Why tempt ye me?'
  s17  Mark 12:17  'And Jesus answering said unto them,'  then j3 on S7. Same
       rule. n2, 'Jesus saw straight through it', already retold s15 and did not
       have to move.

CONSIDERED AND LEFT OUT: Mark 12:17b, 'And they marvelled at him.' Exact, but n5
is the closing turn - coin bears Caesar's face, you bear God's - and a beat about
the crowd's reaction between the answer and that turn would blunt it. Left out on
judgment, not uncertainty.

WOMEN: Mark 12:13-17 records no woman speaking. The widow with the two mites is
later in the same chapter and is not part of this build - and Mark records no
words from her either. Nothing added, nothing invented.

NO GREEN: the Father does not speak here. j3 names God but does not quote him.

WHY-LAW: they wanted him boxed into yes or no. He answered a bigger question than
the one they asked, and handed it back with their own coin in it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Some officials came to Jesus with a question built to trap him — flattering him first, so he'd let his guard down."),
    # Mark 12:14-15
    ("s14", SCRIPTURE, "Master, we know that thou art true, and carest for no man: for thou regardest not the person of men, but teachest the way of God in truth: Is it lawful to give tribute to Caesar, or not? Shall we give, or shall we not give?"),
    ("n1", NARRATOR, "Is it lawful to pay taxes to Caesar, or not? Say yes, and the crowd turns on you. Say no, and Rome arrests you. There was no safe answer."),
    ("n2", NARRATOR, "Jesus saw straight through it."),
    # Mark 12:15
    ("s15", SCRIPTURE, "But he, knowing their hypocrisy, said unto them,"),
    # Mark 12:15
    ("j1", JESUS, "Why tempt ye me? bring me a penny, that I may see it."),
    ("n3", NARRATOR, "They brought one — a small silver Roman coin. He held it up where everyone could see."),
    # Mark 12:16
    ("j2", JESUS, "Whose is this image and superscription?"),
    # Mark 12:16
    ("s16", SCRIPTURE, "And they said unto him, Caesar's."),
    ("n4", NARRATOR, "Whose face is this, he asked them, and whose name. They said it was Caesar's. And with that, the trap they had built swung shut on them instead."),
    # Mark 12:17
    ("s17", SCRIPTURE, "And Jesus answering said unto them,"),
    # Mark 12:17
    ("j3", JESUS, "Render to Caesar the things that are Caesar's, and to God the things that are God's."),
    ("n5", NARRATOR, "The coin bore Caesar's image, so give it back to Caesar. But you bear God's image — so the real question is what you owe to the One whose face you carry."),
    ("card", NARRATOR, "The coin belonged to Caesar because it bore his face. You bear God's. What does that make you worth to him?"),
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
