#!/usr/bin/env python3
"""Narration for build-66-malchus-ear — Luke 22.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED -- both are Jesus in the flesh:
  j1  'Put up again thy sword into his place: for all they that take the sword
      shall perish with the sword.'  Note this line is MATTHEW 26:52, not Luke.
      The build blends the two accounts, which is fine, but the `verse` field now
      says so honestly rather than mislabelling it Luke 22.
  j2  Luke 22:51  'Suffer ye thus far.'  This is the one the build is named for
      and it is genuinely red.

PETER AND THE DISCIPLES ARE `scripture`, NOT RED. Nothing of theirs was painted
red, but the disciples' question was buried in narrator paraphrase and is now
lifted out verbatim:
  s49  Luke 22:49  'Lord, shall we smite with the sword?'
       n1 is trimmed to the frame and n1b carries the retelling plus the strike.
       Both on S2, no new artwork. This matters: they ASKED first, and did not
       wait for the answer. The old cut had Peter swinging out of nowhere.

RETELLINGS: n3 already retells j1 in the storyteller's voice ('Put it away,
Peter'), and n5 already retells j2 ('Let me do this one last thing'). Both were
left alone. Only n1b is new.

NO GREEN: no Father, no voice from heaven, in Luke 22:47-53.

WOMEN: Luke 22:47-53 records no woman speaking. The women in Luke's passion
narrative do not appear until the road to the cross. Nothing added; nothing
invented.

WHY-LAW: the last thing he did as a free man was heal a man who had come to
arrest him. Milk: there is nobody on the wrong side of the sword he is unwilling
to reach toward.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "It was the middle of the night, in a garden called Gethsemane. Jesus had just finished praying — and now torchlight was coming up the hill. A mob, sent by the chief priests, armed with swords and clubs, led by one of his own friends, come to arrest him. This was the moment everything turned."),
    ("n1", NARRATOR, "And his friends could not stand it. Luke says they saw what was about to happen, and they asked him first:"),
    # Luke 22:49
    ("s49", SCRIPTURE, "Lord, shall we smite with the sword?"),
    ("n1b", NARRATOR, "Lord — should we fight? they said. And then they did not wait for the answer. Impulsive, loyal, terrified Peter grabbed a sword and swung — meaning, surely, to defend the man he loved. He caught the servant of the high priest, a man named Malchus, and cut off his ear. In one second, the whole night was about to become a massacre."),
    ("n2", NARRATOR, "Understand Peter's math. Twelve tired men against an armed mob. He was not being smart — he was being brave and wrong, ready to die swinging for Jesus. And most leaders, in that moment, would have let him. But Jesus stopped everything. First, he stopped Peter:"),
    # Matthew 26:52
    ("j1", JESUS, "Put up again thy sword into his place: for all they that take the sword shall perish with the sword."),
    ("n3", NARRATOR, "Put it away, Peter. This is not that kind of kingdom. He said he could call down more than twelve legions of angels this instant if rescue were the plan — but rescue was not the plan. He was not being overpowered in a garden. He was laying his life down on purpose, and he would not spill one drop of someone else's blood to save his own."),
    ("n4", NARRATOR, "And then he did the most extraordinary thing in the whole arrest. With the mob closing in to seize him, with his own death now minutes away, Jesus turned to the injured man. Not his friend. His enemy — one of the very people who had come for him. And he said:"),
    # Luke 22:51
    ("j2", JESUS, "Suffer ye thus far."),
    ("n5", NARRATOR, "Let me do this one last thing. And he reached out, touched the side of the man's head, and made him whole. The last miracle Jesus performed as a free man was healing an injury done by his own defender, to one of the men arresting him."),
    ("n6", NARRATOR, "Think about what Malchus carried home that night. He had come with a mob to seize a man — and that man healed him. Whatever he had believed walking up that hill, he walked back down it whole, touched by the very person he came to hurt. You do not forget a thing like that."),
    ("n7", NARRATOR, "This is who he is, even at his own arrest, even on the worst night of his life: he will not let the moment be about violence. He heals the hand raised against him. There is no one on the wrong side of the sword he is unwilling to reach toward."),
    ("card", NARRATOR, "He healed the man sent to seize him. There is no enemy too far for his mercy — including the one you're afraid is in you."),
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
