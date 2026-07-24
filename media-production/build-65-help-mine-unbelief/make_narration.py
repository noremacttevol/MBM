#!/usr/bin/env python3
"""Narration for build-65-help-mine-unbelief — Mark 9.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THE HEADLINE FIX -- THE FATHER WAS PAINTED AS JESUS. fv1, 'Lord, I believe;
help thou mine unbelief,' was red. That is not Jesus. Mark 9:24 is the boy's
father crying out with tears. It is now `scripture` (light blue). The line the
whole video is named after was being spoken in the wrong man's voice and the
wrong colour.

STAYED RED -- both are Jesus in the flesh and a red-letter KJV prints both:
  j1  Mark 9:23  'If thou canst believe, all things are possible to him that believeth.'
  j2  Mark 9:25  'Thou dumb and deaf spirit, I charge thee, come out of him, and
      enter no more into him.'

LIFTED OUT OF PARAPHRASE -- the father speaks twice more, and both were white:
  s22  Mark 9:22  'If thou canst do any thing, have compassion on us, and help
       us.'  n2 said this in modern English and then told the viewer to listen to
       the word IF -- but the viewer never actually heard him say it. n2 is
       trimmed to the frame, s22 carries the real verse, n2b carries the retelling
       and the IF. All three on S3.
  j3   Mark 9:29  'This kind can come forth by nothing, but by prayer and
       fasting.'  n7 paraphrased this and dropped 'and fasting'. Now Jesus says it
       himself in red; n7 is trimmed to the frame and n7b retells it. All on S8.

RETELLINGS ADDED: n2b after s22, n3b after fv1, n5b after j2, n7b after j3.

NO GREEN: nothing in Mark 9:14-29 is the Father or a voice from heaven.

WOMEN: Mark 9:14-29 records no woman speaking. The parent in this story is the
father, explicitly, in verse 24. Nothing added; nothing invented.

WHY-LAW: the man did not get healing by mustering more faith. He got it by
telling the truth about how little he had. Milk: bring him the belief AND the
doubt, and ask him to help with both.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus came down from the mountain and walked straight into a mess. A crowd was arguing. His own disciples were in the middle of it, cornered and embarrassed — because a desperate father had brought them his son, and for once, they could not help. They had tried. Nothing happened. And everyone was watching them fail."),
    ("n1", NARRATOR, "The father pushed through to Jesus and told him the whole story. His only son had been tormented since he was little — thrown down, unable to speak, hurt again and again by something the family could not fight. Years of it. A father who had watched his boy suffer his entire childhood and could do nothing."),
    ("n2", NARRATOR, "And then he said the most honest thing in the story. He looked at Jesus, and this is exactly how Mark writes down what he said:"),
    # Mark 9:22
    ("s22", SCRIPTURE, "If thou canst do any thing, have compassion on us, and help us."),
    ("n2b", NARRATOR, "If you can do anything — anything at all — have compassion on us, and help us. If. After all those years of disappointment, hope had gotten expensive. Listen to how Jesus answered that trembling little word IF:"),
    # Mark 9:23
    ("j1", JESUS, "If thou canst believe, all things are possible to him that believeth."),
    ("n3", NARRATOR, "And now comes the moment this whole story is remembered for. The father did not pretend. He did not put on a brave religious face and claim a faith he did not fully have. He did something braver. He cried out the truest prayer in the Bible for anyone who has ever wanted to believe and struggled to:"),
    # Mark 9:24
    ("fv1", SCRIPTURE, "Lord, I believe; help thou mine unbelief."),
    ("n3b", NARRATOR, "Lord, I believe, he said. Help me where I don't. He did not hand Jesus a finished faith. He handed him a cracked one, and asked him to hold it anyway."),
    ("n4", NARRATOR, "Think about what he just did. He brought Jesus the little bit of faith he had AND the unbelief he was ashamed of — and laid both of them down. He did not wait to believe perfectly before he asked. He asked for help WITH his believing. And that — that cracked-open, honest, half-full faith — was enough."),
    ("n5", NARRATOR, "Jesus saw the crowd rushing in to gawk, and he did not wait. He spoke directly to the thing that had stolen this boy's whole childhood, and commanded it, once and for all:"),
    # Mark 9:25
    ("j2", JESUS, "Thou dumb and deaf spirit, I charge thee, come out of him, and enter no more into him."),
    ("n5b", NARRATOR, "You spirit that has kept him silent and shut his ears — I command you: come out of him, and never come back into him again. Not for a while. Never again."),
    ("n6a", NARRATOR, "It left. The boy went so still that people whispered he was dead. But Jesus reached down, took him by the hand, and lifted him up — and the boy stood, quiet and whole."),
    ("n6b", NARRATOR, "And he gave him back to his father. The tormented childhood was over. It ended with a hand reaching down into the dust to pull a son to his feet."),
    ("n7", NARRATOR, "Later, alone in the house, the disciples asked him why they had failed. And Jesus gave them one sentence:"),
    # Mark 9:29
    ("j3", JESUS, "This kind can come forth by nothing, but by prayer and fasting."),
    ("n7b", NARRATOR, "Nothing gets this out except prayer and fasting, he told them — meaning this was never about their technique. It was about who they were leaning on. The father got it right without knowing the rules: he stopped trying to be strong, and just brought his weakness to the only one who could carry it."),
    ("card", NARRATOR, "You do not need perfect faith to come to him. Bring the little you have — and the doubt you're ashamed of — and ask him to help you believe. That prayer has never been turned away."),
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
