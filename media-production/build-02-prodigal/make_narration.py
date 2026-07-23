#!/usr/bin/env python3
"""Narration for build-02-prodigal — Luke 15.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Luke 15:11-32, the prodigal son. A red-letter KJV inks the WHOLE parable,
including every word Jesus puts in the mouths of the father, the younger son and
the elder brother. So j1, j2a and j2b all stay JESUS-RED, and two more of the
parable's own lines are lifted out of narrator paraphrase and join them in red:
  j3  Luke 15:18-19  the son's rehearsed speech, which n3 was paraphrasing
  j4  Luke 15:29     the elder brother's complaint, which n10b was paraphrasing
No speaker moved OUT of red in this build. n8 is the closing card and keeps its id.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "When religious men complained that Jesus spent his time with sinners, he didn't argue with them. He answered with a story, about a father and his two sons."),
    ("n1", NARRATOR, "The younger son asked for his inheritance early — as if to say he wished his father were already dead. Then he left, and poured it all out on a life that emptied him."),
    ("n2", NARRATOR, "When the money was gone, a famine came. He ended up feeding pigs, so hungry he would have eaten what they ate. And there, in the mud, he came to his senses."),
    ("n3", NARRATOR, "So he started walking home, rehearsing a speech the whole way."),
    # Luke 15:18-19
    ("j3", JESUS, "I will arise and go to my father, and will say unto him, Father, I have sinned against heaven, and before thee, And am no more worthy to be called thy son: make me as one of thy hired servants."),
    ("n4", NARRATOR, "He was still a long way off... when his father saw him."),
    ("n5a", NARRATOR, "The father ran."),
    ("n5b", NARRATOR, "Old men in that world did not run. It was beneath their dignity. He ran anyway."),
    ("n6", NARRATOR, "He didn't wait for the speech. He wrapped his arms around his son before a single word was said."),
    ("n7", NARRATOR, "That night the father dressed him in the finest robe, put a ring on his hand, and called for a feast — and he told everyone why."),
    # Luke 15:24
    ("j1", JESUS, "For this my son was dead, and is alive again; he was lost, and is found."),
    ("n9", NARRATOR, "But Jesus wasn't finished. The older son was still out in the field, like always. When he came near the house and heard the music, a servant told him: your brother is home. And he was so angry, he refused to go in."),
    ("n10a", NARRATOR, "So the father left his own feast, and went out again — this time to the son who had never left."),
    ("n10b", NARRATOR, "The older son's hurt poured out. All these years I have served you. I never disobeyed you. And you never gave me even a young goat, to celebrate with my friends."),
    # Luke 15:29
    ("j4", JESUS, "Lo, these many years do I serve thee, neither transgressed I at any time thy commandment: and yet thou never gavest me a kid, that I might make merry with my friends:"),
    ("n11", NARRATOR, "The father didn't argue with him, either. Jesus gave him the last words of the story."),
    # Luke 15:31
    ("j2a", JESUS, "Son, thou art ever with me, and all that I have is thine."),
    # Luke 15:32
    ("j2b", JESUS, "It was meet that we should make merry, and be glad: for this thy brother was dead, and is alive again; and was lost, and is found."),
    ("n8", NARRATOR, "Which one feels closest to where you are right now — the son who left, the father who ran to meet him, or the brother who stayed, and felt unseen?"),
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
