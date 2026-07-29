#!/usr/bin/env python3
"""Narration for build-01-cloak — Mark 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both existing red beats are Jesus speaking in the flesh and a
red-letter KJV prints both.
  j0  Mark 5:30  'Who touched my clothes?'
  j1  Mark 5:34  'Daughter, thy faith hath made thee whole...'

THE WOMAN - the headline change. Mark 5:28 records what she said to herself, and
this build had it only as narrator paraphrase ('She did not ask permission. She
did not make a speech.'). It is now w28, PINK, verbatim:
  w28  Mark 5:28  'If I may touch but his clothes, I shall be whole.'
Quoted without Mark's frame 'For she said,' so the caption is her own voice.
This is the only line the woman gets in the whole chapter and the video was
telling her story without ever letting her speak.

LIFTED FROM PARAPHRASE - the disciples' pushback, which makes the moment an
exchange instead of a monologue:
  s31  Mark 5:31  'Thou seest the multitude thronging thee, and sayest thou,
                   Who touched me?'  SCRIPTURE (blue - this is the twelve, not Jesus)

EDITS TO EXISTING NARRATOR TEXT: n3a gains a closing hand-off sentence and n3b
gains a one-line retelling of w28 in front of its original sentence. n4c is
unchanged - it already retells the disciples' line perfectly ('His disciples
thought the question made no sense'), so s31 hands straight into it. Nothing
else changed.

NOT LIFTED: Mark 5:33 has her fall down and tell him 'all the truth', but the
KJV does not record the words, so n4b stays narrator. Nothing invented.

WHY-LAW: she reached in secret and he refused to let the healing stay secret -
he stopped a crowd, on his way to a dying child, to give one untouchable woman
a name. Milk framing: he stops for the one, and calls her daughter.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "There was a woman who had been suffering for twelve years."),
    ("n2", NARRATOR, "She had spent everything on doctors. Nothing helped. She was exhausted, desperate — and by the rules of her time, considered untouchable."),
    ("n2b", NARRATOR, "That day, Jesus was already on his way to save someone else — a ruler's daughter, twelve years old, and dying. The crowd pressed around him on every side. Almost no one would have noticed one more sick woman at its edge."),
    ("n3a", NARRATOR, "She heard Jesus was nearby. She did not ask permission. She did not make a speech. She said only one thing, and she said it to herself."),
    # Mark 5:28
    ("w28", WOMAN, "If I may touch but his clothes, I shall be whole."),
    ("n3b", NARRATOR, "If I can just touch his clothes, she told herself, I will be well. That was the whole of her plan. She pressed through the crowd and reached out to touch the edge of his cloak."),
    ("n4a", NARRATOR, "He stopped. He had felt it — power had gone out of him. The healing was already hers, given the moment she touched him."),
    # Mark 5:30
    ("j0", JESUS, "Who touched my clothes?"),
    # Mark 5:31
    ("s31", SCRIPTURE, "Thou seest the multitude thronging thee, and sayest thou, Who touched me?"),
    ("n4c", NARRATOR, "His disciples thought the question made no sense. The whole crowd was pressing against him — who hadn't touched him? He ignored them. He was already needed somewhere else, and he stopped anyway."),
    ("n4b", NARRATOR, "He looked for her until he found her."),
    # Mark 5:34
    ("j1", JESUS, "Daughter, thy faith hath made thee whole; go in peace, and be whole of thy plague."),
    ("n5", NARRATOR, "Be whole of thy plague — be free of what has been hurting you. Twelve years of it. Over, in a sentence. And the first word he chose was daughter."),
    ("card", NARRATOR, "Whatever you have carried for years — reach for him. He stops for the one. He calls you his own."),
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
