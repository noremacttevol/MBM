#!/usr/bin/env python3
"""Narration for build-130-what-manner-of-spirit — Luke 9.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: j1 is correct as it stands. 'Ye know not what manner of spirit ye are
of. For the Son of man is not come to destroy men's lives, but to save them' is
Luke 9:55-56, Jesus speaking in the flesh, and a red-letter KJV inks it. The KJV
frame around it - 'But he turned, and rebuked them, and said' - is NOT in the
segment, so there was no welded frame to split. n2 already carries that framing
in the storyteller's own modern words, which is where it belongs.

LIFTED - the line the whole video answers, which was never voiced.
  s54  Luke 9:54  'Lord, wilt thou that we command fire to come down from heaven,
       and consume them, even as Elias did?'  SCRIPTURE, light blue. James and
       John are apostles, not Deity, so blue is right. n1 was paraphrasing this
       in the narrator's voice; n1 keeps its original text and now works as the
       retelling immediately after it. The rebuke lands ten times harder once you
       have heard two of the Twelve ask for it out loud.

ADDED: n3b, covering Luke 9:56b - they simply went to another village. The
original build had no beat doing that work on ST6 ('walking on'), and it moves n4
onto ST7 ('warmth not fire'), which the original left unused entirely.

NOTE ON THE STILLS: the brief's still_vars has no ST2 - s2-sorrow-not-wrath.jpeg
is on disk but is not bound to a variable, so it cannot be used in beats. Left
alone; the artwork is untouched.

WOMEN: Luke 9:51-56 records no woman speaking. Nothing added, nothing invented.

WHY-LAW: he did not rebuke the village that shut its gate. He rebuked the two men
who wanted it burned. Milk framing - the wanting-to-destroy is the thing that is
not from him, and he says so gently, to people he loves.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "As Jesus traveled toward Jerusalem, a Samaritan village refused to welcome Him. The disciples James and John were hot with anger."),
    # Luke 9:54
    ("s54", SCRIPTURE, "Lord, wilt thou that we command fire to come down from heaven, and consume them, even as Elias did?"),
    ("n1", NARRATOR, "They asked if they should call down fire from heaven to burn the place. They wanted judgment."),
    ("n2", NARRATOR, "Jesus turned and rebuked them — not the village, but His own disciples' hearts."),
    # Luke 9:55-56
    ("j1", JESUS, "Ye know not what manner of spirit ye are of. For the Son of man is not come to destroy men's lives, but to save them."),
    ("n3", NARRATOR, "He didn't come to burn. He came to rescue. The fire in the disciples' hearts was the wrong kind."),
    ("n3b", NARRATOR, "And then they simply walked on to the next village. No fire. No answer to the insult at all — just the road, and somewhere else to be."),
    ("n4", NARRATOR, "Anger that wants to destroy isn't from Him. The spirit He brings saves."),
    ("card", NARRATOR, "He came to save, not to burn. Let His Spirit — the saving one — shape yours."),
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
