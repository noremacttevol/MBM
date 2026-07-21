#!/usr/bin/env python3
"""Narration for build-76-suffer-the-little-children — Mark 10.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, both. j1 (Mark 10:14b) and j2 (Mark 10:15) are Jesus in the flesh
and a red-letter KJV inks both.

THE FRAMING SPLIT. Mark 10:14 reads in full: 'But when Jesus saw it, he was much
displeased, and said unto them, Suffer the little children to come unto me, and
forbid them not: for of such is the kingdom of God.' Everything before 'Suffer'
is Mark writing, and a red-letter KJV leaves it black. The build had that frame
only as modern paraphrase in n2, so the verse is split properly now, BOTH HALVES
ON THE SAME STILL S4 - no new artwork, and the edit the viewer sees is unchanged:
  s14  Mark 10:14  'But when Jesus saw it, he was much displeased, and said unto
       them,'  SCRIPTURE, light blue - narration inside the Gospels is never red.
  j1   Mark 10:14  'Suffer the little children to come unto me, and forbid them
       not: for of such is the kingdom of God.'  JESUS, red, unchanged.
n2 keeps its id and now sets it up; n3 was already the retelling and is untouched.

ADDED AS SCRIPTURE, both Mark narrating, both light blue:
  s13  Mark 10:13  'And they brought young children to him, that he should touch
       them: and his disciples rebuked those that brought them.'  n1 keeps its id
       and text and now retells it.
  s16  Mark 10:16  'And he took them up in his arms, put his hands upon them, and
       blessed them.'  This is the tenderest sentence in the chapter and the
       video only had it in paraphrase. n5 keeps its id and text and now retells
       it, on the same still S6.

WOMEN: Mark 10:13-16 records no woman speaking. The parents who brought the
children are not named and not quoted. Nothing added, nothing invented.

NO GREEN: the Father does not speak in this passage. 'The kingdom of God' is
Jesus's phrase about the Father, not the Father talking.

THE HUSH IS UNTOUCHED - the silent still on S8 stays exactly where the original
build put it, after n5.

BEAT ORDER NOTE: the original build runs n4 on S7 BEFORE n5 on S6, so the stills
go out of numeric order at the end. That is deliberate in the delivered video and
it is preserved exactly.

PRONUNCIATION: 'Suffer' is left alone - it is the whole point of n3, which stops
and explains that the old word just means let.

WHY-LAW: the disciples were sure the important work was happening somewhere else
in the room. He stopped all of it and sat down with the people who could do
nothing for him.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Parents were bringing their little kids to Jesus, just so he could put his hands on them and bless them."),
    # Mark 10:13
    ("s13", SCRIPTURE, "And they brought young children to him, that he should touch them: and his disciples rebuked those that brought them."),
    ("n1", NARRATOR, "The disciples tried to wave them off — the Teacher is busy, this is grown-up work, not the place for children."),
    ("n2", NARRATOR, "But he saw them do it. And Mark does not soften how he took it."),
    # Mark 10:14
    ("s14", SCRIPTURE, "But when Jesus saw it, he was much displeased, and said unto them,"),
    # Mark 10:14
    ("j1", JESUS, "Suffer the little children to come unto me, and forbid them not: for of such is the kingdom of God."),
    ("n3", NARRATOR, "That old word suffer just means let. Let them come. Don't stand in their way. Then he went further."),
    # Mark 10:15
    ("j2", JESUS, "Verily I say unto you, Whosoever shall not receive the kingdom of God as a little child, he shall not enter therein."),
    ("n4", NARRATOR, "He meant: nobody earns their way into the kingdom of God. You receive it the way a child receives a gift — with open hands."),
    # Mark 10:16
    ("s16", SCRIPTURE, "And he took them up in his arms, put his hands upon them, and blessed them."),
    ("n5", NARRATOR, "Then he gathered them up in his arms and blessed them, one at a time, unhurried — like there was nowhere else he needed to be."),
    ("card", NARRATOR, "He had time for the smallest and least important person in the room. That includes you."),
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
