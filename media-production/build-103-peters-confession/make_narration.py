#!/usr/bin/env python3
"""Narration audio for Video #103 — Peter's Confession (Matthew 16:13-20).

Narrator: en-US-AndrewNeural. Jesus: en-US-ChristopherNeural (exact KJV only).
Peter's confession is voiced by the NARRATOR (Jesus's voice is reserved for Jesus's
own exact words); the caption shows Peter's words in plain white, while Jesus's KJV
lines render cream-italic — so the two voices stay visually distinct.

Jesus's KJV lines (Christopher, cream italic):
  jv13  Matt 16:13  "Whom do men say that I the Son of man am?"
  jv15  Matt 16:15  "But whom say ye that I am?"
  jv17  Matt 16:17  "Blessed art thou, Simon Barjona..." — sacred silence 1
  jv18  Matt 16:18  "...upon this rock I will build my church..." — sacred silence 2

WHY-LAW: this is the hinge of the gospel — who IS he? Everyone had a polite,
second-hand answer (a prophet, a teacher). Jesus pushes past all of it to the only
question that matters: but who do YOU say I am. And when Peter answers from his heart,
Jesus calls it the rock the whole thing is built on. Milk framing: a warm invitation to
answer the question yourself. Never a threat.

HOMOGRAPH EAR-CHECK: no high-risk homographs in the KJV lines. "Barjona" read plainly.
NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Jesus had brought his disciples a long way north, to a quiet place far from the "
     "crowds, up under a great cliff of pale rock. And there he asked them a question he "
     "had never asked so plainly before.", None),
    # jv13
    ("jv13", JESUS, "-24%", "-6Hz",
     "Whom do men say that I the Son of man am?", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "It was an easy question at first. What are people saying? And they had plenty of "
     "answers ready.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Some say you are John the Baptist, they told him. Some say Elijah come back. "
     "Others, Jeremiah, or one of the old prophets. All respectful. All safe. All "
     "second-hand — what other people thought.", None),
    # jv15
    ("jv15", JESUS, "-26%", "-6Hz",
     "But whom say ye that I am?", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And there it was. Not what have you heard. Not what is the crowd saying. But you — "
     "who do you say that I am? The question stopped them cold. This one you cannot "
     "borrow from anybody else.", None),
    # Peter's confession — NARRATOR voice, white caption (not Jesus's cream)
    ("np", NARRATOR, "-20%", "-2Hz",
     "And Simon Peter answered him: Thou art the Christ, the Son of the living God.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Not a prophet. Not a teacher. The Christ — the promised one — the Son of the living "
     "God himself. Peter said out loud the thing the others had only half-dared to hope.", None),
    # jv17 — blessing, sacred silence 1
    ("jv17", JESUS, "-26%", "-6Hz",
     "Blessed art thou, Simon Barjona: for flesh and blood hath not revealed it unto "
     "thee, but my Father which is in heaven.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "You did not work this out on your own, Jesus told him. My Father in heaven showed "
     "it to you. This kind of knowing does not come from clever thinking. It is given, "
     "quietly, from God, to a heart ready to receive it.", None),
    # jv18 — upon this rock, sacred silence 2
    ("jv18", JESUS, "-26%", "-6Hz",
     "And I say also unto thee, That thou art Peter, and upon this rock I will build my "
     "church; and the gates of hell shall not prevail against it.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "On this — on knowing who he really is — he would build something that hell itself "
     "could never tear down. Everything else in the gospel is built on top of this one "
     "answer.", None),
    # closing card
    ("card", NARRATOR, "-26%", "-4Hz",
     "The crowds had their opinions; Peter had an answer he would stake his life on. "
     "Jesus is still asking the one question that no one can answer for you. Who do YOU "
     "say that he is?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
