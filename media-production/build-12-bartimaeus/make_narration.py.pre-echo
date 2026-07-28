#!/usr/bin/env python3
"""Narration for build-12-bartimaeus — Mark 10.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Mark 10:46-52. j1 and j2 are Jesus in the flesh and stay RED. Bartimaeus is a
man in the story, not Jesus, so his two famous lines are SCRIPTURE (blue) - and they
were not in the video at all, only paraphrased:
  s47  Mark 10:47  'Jesus, thou Son of David, have mercy on me.'
  s51  Mark 10:51  'Lord, that I might receive my sight.'
The crowd also gets its verbatim line, blue:
  s49  Mark 10:49  'Be of good comfort, rise; he calleth thee.'
n12 is the closing card and keeps its id.
still_vars are introduced for this build (S1..S11, S10A, S10B) - the old template
referenced the jpegs by literal filename and the brief extractor found none.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "The road out of Jericho, on a loud and dusty day. Jericho was the last stop before the climb up to Jerusalem, and with the Passover feast coming, that road carried half the country. For a beggar, crowds meant coins. And so a blind man named Bartimaeus sat where he always sat — at the edge of the highway, his ragged cloak spread across his lap to catch whatever fell, listening to a thousand feet walk past him. Listening was his whole life. He knew the road by its sounds."),
    ("n1", NARRATOR, "But this day the sound was different. A procession was coming out of the city — a moving wall of voices — and inside the noise he caught a name. Jesus of Nazareth was passing by. He had heard the stories everyone had heard: a teacher who opened deaf ears, who made lepers clean. Passing by, and never again. A blind man cannot chase a crowd. All he had was his voice."),
    # Mark 10:47
    ("s47", SCRIPTURE, "Jesus, thou Son of David, have mercy on me."),
    ("n2", NARRATOR, "So he used it. He pulled in all the air his body would hold and shouted: Jesus, Son of David — have mercy on me! Catch that title. The crowd called him Jesus of Nazareth — the man from up north. Son of David was something else entirely: it was the name reserved for the promised King, the Messiah. Everyone with working eyes saw a traveling teacher. The blind man was the one who saw who was actually walking past."),
    ("n3", NARRATOR, "And the crowd turned on him. Many voices — Mark says many — told one desperate man to be quiet. Understand why: to them, a beggar screaming at a famous rabbi was an embarrassment, noise that needed hushing. Respectable people, telling a man in the dust that his need was bad manners."),
    ("n4", NARRATOR, "He shouted louder."),
    ("n5", NARRATOR, "And Jesus stood still. The whole procession stopped around him — hundreds of feet going quiet in the dust. Remember where this road was taking him: up to Jerusalem, into the last week of his life. He was carrying all of that. And one blind beggar's voice — the voice everyone else was trying to shut off — stopped him in the road. He told them: call him over."),
    # Mark 10:49
    ("s49", SCRIPTURE, "Be of good comfort, rise; he calleth thee."),
    ("n6", NARRATOR, "And listen to the crowd change its tune. The same voices that had been hushing him now crowded in with: take heart — get up! He is calling for you."),
    ("n7", NARRATOR, "What happened next is one small verse, and it holds the whole man. He threw off his cloak, jumped up, and came. That cloak was a beggar's entire world — his coat, his bed at night, the very thing he spread out to catch the coins he lived on. A blind man who throws his cloak behind him may never find it again. He threw it anyway, coins and all. He spent everything he owned on the chance that the shout had been heard."),
    ("n8", NARRATOR, "So he came, hands out in front of him, through a corridor of staring people, and stood breathing hard in front of the man he could not see. And Jesus asked him one question:"),
    # Mark 10:51
    ("j1", JESUS, "What wilt thou that I should do unto thee?"),
    ("n9", NARRATOR, "As if it weren't obvious. A blind man, standing in a beggar's tunic. But he asked anyway — because he wanted the man's own voice, not the crowd's guess about him. Nobody had asked Bartimaeus what he wanted in a very long time. His answer came out in a breath: Rabbi — I want to see."),
    # Mark 10:51
    ("s51", SCRIPTURE, "Lord, that I might receive my sight."),
    # Mark 10:52
    ("j2", JESUS, "Go thy way; thy faith hath made thee whole."),
    ("n10", NARRATOR, "And immediately, Mark says, he saw. The clouds in his eyes cleared like silt settling out of water, and the first thing those new eyes ever held was daylight on the road ahead. Notice what Jesus told him: your trust did this — and you are free. Free to go anywhere."),
    ("n11", NARRATOR, "And here is the ending Mark wants you to catch. Free to go anywhere, with brand new eyes and no cloak to go back for, he picked his road — the one Jesus was walking. He followed him, up the climb toward Jerusalem, staring at everything: the hills, the faces, his own two hands. The man who had been told to keep quiet walked in the middle of the procession that had hushed him."),
    ("n12", NARRATOR, "The crowd told him to keep quiet, and he shouted louder. What is the thing you would shout for, if no one could tell you to be quiet?"),
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
