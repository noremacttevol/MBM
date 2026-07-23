#!/usr/bin/env python3
"""Narration for build-98-mary-her-name — John 20.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THIS IS THE ONE THIS WHOLE PASS EXISTED FOR. The video is built on one
word he says and one word she answers -- and in the original, only his word was
in his own voice. Every single thing Mary Magdalene says in John 20 was narrator
paraphrase, in white, including her answer to her own name.

MARY NOW SPEAKS, THREE TIMES, IN PINK. All verbatim:
  w13  John 20:13  'They have taken away my Lord, and I know not where they have
       laid him.'  -- her answer to the angels. n0 is trimmed to the frame and
       n0b carries the retelling.
  w15  John 20:15  'Sir, if thou have borne him hence, tell me where thou hast
       laid him, and I will take him away.'  -- said to the man she thinks is the
       gardener. n1b is trimmed to the frame and n1b2 carries the retelling. She
       is offering to carry a grown man's body home by herself. That is what the
       old paraphrase, 'she begged,' was hiding.
  w16  John 20:16  'Rabboni.'  -- ONE WORD, and it is the hinge of the video.
       The KJV adds 'which is to say, Master' as John's own gloss, so that clause
       is left out of her line rather than put in her mouth; n3 carries the
       translation in the storyteller's voice instead.

STAYED RED, and TWO MORE ADDED:
  j1   John 20:16  'Mary.'  -- unchanged, id kept.
  jv15 John 20:15  'Woman, why weepest thou? whom seekest thou?'  -- he speaks to
       her before she knows him, and it was missing entirely. n1a2 retells it.
  jv17 John 20:17  'Touch me not; for I am not yet ascended to my Father: but go
       to my brethren, and say unto them, I ascend unto my Father, and your
       Father; and to my God, and your God.'  -- n4a said only 'he sent her to
       tell the others.' The actual sending is one of the great sentences in the
       Gospels and it was not in the video. n4a keeps its id and now retells it.

DELIBERATE QUESTION-AND-ANSWER PAIR -- NO RETELLING BETWEEN THEM. j1 is 'Mary.'
and w16 is 'Rabboni.' Red straight into pink, one word each, nothing in between.
Wedging a narrator line between a man saying a woman's name and the woman
answering would destroy the only thing this video is about. n3 retells both
together immediately after. This is the same call made in build-144 with
'Believest thou this?' and Martha's answer.

NO GREEN: the Father is spoken ABOUT here, not by him.

WHY-LAW: she was standing three feet from the risen Lord and could not see him
through her own crying, and what opened her eyes was not an argument or a proof.
It was her name. Milk: he knows you by name, and he says it while you are still
crying.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Mary Magdalene stayed behind at the tomb, weeping. When she was asked why she was crying, all she had was one answer."),
    # John 20:13
    ("w13", WOMAN, "They have taken away my Lord, and I know not where they have laid him."),
    ("n0b", NARRATOR, "They have taken away my Lord, she said, and I don't know where they've put him. She had lost him once already. Now it felt like she had lost even the place where he lay."),
    ("n1a", NARRATOR, "She turned and saw a man standing there."),
    # John 20:15
    ("jv15", JESUS, "Woman, why weepest thou? whom seekest thou?"),
    ("n1a2", NARRATOR, "Why are you crying? he asked her. Who is it you're looking for? She did not know the voice yet. Through the tears, she could not even see his face."),
    ("n1b", NARRATOR, "Thinking he was the gardener, she pleaded with him."),
    # John 20:15
    ("w15", WOMAN, "Sir, if thou have borne him hence, tell me where thou hast laid him, and I will take him away."),
    ("n1b2", NARRATOR, "Sir, if you carried him off, just tell me where you put him, and I will go and get him. She was a woman offering to carry a grown man's body home by herself. That is how much she loved him."),
    ("n2", NARRATOR, "He said one word. Her name."),
    # John 20:16
    ("j1", JESUS, "Mary."),
    # John 20:16
    ("w16", WOMAN, "Rabboni."),
    ("n3", NARRATOR, "Mary. And she answered him — Rabboni. It means Master, in her own language, the word she had always called him. And instantly she knew. Grief flipped to joy in a single heartbeat — he was alive, and he had come looking for HER, by name."),
    # John 20:17
    ("jv17", JESUS, "Touch me not; for I am not yet ascended to my Father: but go to my brethren, and say unto them, I ascend unto my Father, and your Father; and to my God, and your God."),
    ("n4a", NARRATOR, "Don't hold on to me yet, he told her — I haven't gone up to my Father. Go to my brothers and tell them I'm going to my Father and your Father, to my God and your God. He gave her the message, and he sent her to carry it."),
    ("n4b", NARRATOR, "The first person to see the risen Lord, and the first preacher of the resurrection, was a weeping woman he called by name."),
    ("card", NARRATOR, "He knows your name — and he speaks it even in your grief. Listen for it."),
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
