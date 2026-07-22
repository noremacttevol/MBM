#!/usr/bin/env python3
"""Narration for build-63-man-born-blind — John 9.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, all four, all Jesus in the flesh with a red-letter KJV inking them, all
keeping their ids:
  j1  John 9:3   "Neither hath this man sinned, nor his parents: but that the works
      of God should be made manifest in him."
  j2  John 9:7   "Go, wash in the pool of Siloam."   -- the KJV continues "(which is
      by interpretation, Sent.)", which is John explaining, not Jesus speaking. It
      was already correctly left off, and stays off.
  j3  John 9:35  "Dost thou believe on the Son of God?"
  j4  John 9:37  "Thou hast both seen him, and it is he that talketh with thee."
None of the four had John's framing welded on, so none needed splitting.

THE BLIND MAN WAS NEVER HEARD -- AND HE HAS THE BEST LINE IN THE CHAPTER. Every word
he says was sitting in white paraphrase. Three of them are now [scripture], light
blue -- he is a man in the story, not Deity -- each on the SAME still the paraphrase
was already using:
  s25  John 9:25  "Whether he be a sinner or no, I know not: one thing I know, that,
       whereas I was blind, now I see."   -- n6 called it "one of the greatest
       sentences anyone ever said" and then did not say it. n6 keeps its id, trimmed
       to the frame; n6b retells.
  s36  John 9:36  "Who is he, Lord, that I might believe on him?"   -- was n8's "the
       man asked who that was, so he could believe." n8 keeps its id, trimmed;
       n8b retells and hands off to j4.
  s38  John 9:38  "Lord, I believe."   -- was three words of white narration inside
       n9. It is the confession the whole chapter is built toward. n9 keeps its id,
       trimmed to the frame; n9b retells and carries the closing thought.

THE DISCIPLES WERE NEVER HEARD EITHER. n0 paraphrased their question, and it is the
sentence j1 is answering. Lifted as s2 [scripture] on S1: "Master, who did sin, this
man, or his parents, that he was born blind?" n0 keeps its id, trimmed to the frame;
n0b retells.

NO GREEN: John 9 has no voice from heaven and no Father speaking. j1 is Jesus in the
flesh, so it is red, not green.

WOMEN: John 9 records no woman speaking. The man's parents answer the Pharisees in
9:20-21 but John gives the words to "his parents" jointly, not to his mother, so
there is no line that is hers to speak. Nothing invented.

WHY-LAW: he refused to answer whose fault it was, and answered what it was for
instead. And when the religious world threw the man out for telling the truth, Jesus
went and found him. Milk: you may never get the why. He comes and finds you.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "In Jerusalem there was a man who begged at his same spot every day, because he had been blind since the day he was born. He had never seen his mother's face. Never seen morning. And as Jesus and his disciples passed by, the disciples asked him:"),
    # John 9:2
    ("s2", SCRIPTURE, "Master, who did sin, this man, or his parents, that he was born blind?"),
    ("n0b", NARRATOR, "Who sinned, Teacher — this man, or his parents — for him to be born blind? Notice they did not ask whether somebody was at fault. They asked which one. It was the question everyone in that world assumed had an answer."),
    ("n1", NARRATOR, "It was the standard theology of the day: if you are suffering, somebody must have earned it. People still run that math on themselves today. Jesus threw the whole equation out."),
    # John 9:3
    ("j1", JESUS, "Neither hath this man sinned, nor his parents: but that the works of God should be made manifest in him."),
    ("n2", NARRATOR, "Nobody's fault. Not a punishment. Jesus refused to explain the man's suffering — and instead announced what it was about to become: a place where God's work would be seen. Then he knelt down, made soft clay with the dust of the ground, and gently spread it over the blind man's eyes with his own hands."),
    ("n3", NARRATOR, "Why clay? Bible students hear an echo: in the beginning, God formed man from the dust of the ground. Whatever had been left unfinished in those eyes from birth, the maker was finishing it now, with the same material he started with. Then he gave the man one simple instruction:"),
    # John 9:7
    ("j2", JESUS, "Go, wash in the pool of Siloam."),
    ("n4", NARRATOR, "Go and wash in the pool of Siloam. Understand what was asked of him. A blind man, eyes packed with mud, feeling his way across Jerusalem, one wall and one step at a time, holding nothing but the instruction of a stranger whose face he had never seen. He went. That walk was the faith."),
    ("n5", NARRATOR, "He knelt at the pool of Siloam and washed the clay away. And light came pouring in where there had never been light — color, water, sky, his own two hands. The first things he ever saw. He came back seeing."),
    ("n6", NARRATOR, "And then the trouble started. The neighbors argued about whether he was even the same man. The religious leaders hauled him in for questioning — twice — because the healing had happened on the sabbath, and that broke their rules. They pressed him to call Jesus a sinner. And he gave them one of the greatest answers anybody ever gave:"),
    # John 9:25
    ("s25", SCRIPTURE, "Whether he be a sinner or no, I know not: one thing I know, that, whereas I was blind, now I see."),
    ("n6b", NARRATOR, "Whether he's a sinner, I don't know. One thing I know: I was blind, and now I see. He would not argue theology with trained men. He just told them the one thing that had happened to him, and there was nothing they could do with it."),
    ("n7", NARRATOR, "They could not shake him, so they threw him out — cast out of the synagogue, cut off from the whole religious life of his people. Healed, and homeless in the same week. And here is the part to remember: when Jesus heard they had thrown him out, he went and FOUND him. The man had never actually seen the one who healed him. Jesus asked him:"),
    # John 9:35
    ("j3", JESUS, "Dost thou believe on the Son of God?"),
    ("n8", NARRATOR, "Do you believe on the Son of God? And the man — who wants to, and does not know who that is — answers:"),
    # John 9:36
    ("s36", SCRIPTURE, "Who is he, Lord, that I might believe on him?"),
    ("n8b", NARRATOR, "Who is he, sir? Tell me, so I can believe in him. He is not stalling. He is asking for a name so he can give himself to it. And Jesus said:"),
    # John 9:37
    ("j4", JESUS, "Thou hast both seen him, and it is he that talketh with thee."),
    ("n9", NARRATOR, "You have seen him — and he is the one talking with you right now. The first face this man ever truly studied was the face of the one who gave him his eyes. And he said:"),
    # John 9:38
    ("s38", SCRIPTURE, "Lord, I believe."),
    ("n9b", NARRATOR, "Lord, I believe — and he worshipped him, right there in the street the religious world had just thrown him out of. The question of whose fault it was never got an answer that day. The man got something better. He got found."),
    ("card", NARRATOR, "You may never get the why for what you carry. But when the world shuts you out, he comes and finds you."),
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
