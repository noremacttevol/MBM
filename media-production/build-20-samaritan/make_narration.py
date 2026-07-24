#!/usr/bin/env python3
"""Narration for build-20-samaritan — Luke 10.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both existing red beats are Jesus in the flesh and a red-letter KJV
prints both.
  j1  Luke 10:36  'Which now of these three, thinkest thou, was neighbour unto
      him that fell among the thieves?'
  j2  Luke 10:37  'Go, and do thou likewise.'

ADDED RED, INSIDE THE PARABLE. A red-letter KJV prints the whole parable red,
including the words Jesus puts in a character's mouth, so the Samaritan's own
line is JESUS, not `scripture`:
  j35  Luke 10:35  'Take care of him; and whatsoever thou spendest more, when I
       come again, I will repay thee.'
n11 already ends on the frame ('and said, take care of him'), and n12 already
opens with the retelling, so this slotted in between them on the SAME still S6
with no rewriting at all. This is the rule the brief calls out: the priest, the
Levite and the Samaritan do not go blue.

ADDED BLUE, OUTSIDE THE PARABLE. The lawyer is a real man asking a real question
in Luke's narrative frame -- he is not a character in the parable -- so he is
SCRIPTURE, light blue. Both his questions were narrator paraphrase:
  s25  Luke 10:25  'Master, what shall I do to inherit eternal life?'
  s29  Luke 10:29  'And who is my neighbour?'
  s37  Luke 10:37  'He that shewed mercy on him.'
n1 is trimmed to the frame only. n1b is a new retelling that also carries the two
sentences trimmed out of n1 ('It sounds humble. It was not.') so nothing the
storyteller used to say is lost. n2 keeps its original text and now retells s29.
s37 is a deliberate question-and-answer pair with j1 -- the blue answer directly
under the red question is the entire point of the scene, and n14 retells it.

LEFT AS PARAPHRASE ON PURPOSE: the lawyer's own recital of the law in Luke 10:27
('Thou shalt love the Lord thy God with all thy heart...') is summarised inside
n1b rather than lifted. Lifting it would put a third blue block in the opening
before the story has started, and the video's subject is the second question, not
the first.

WOMEN: Luke 10:25-37 records no woman speaking. Nothing added; nothing invented.

WHY-LAW: he asked for a line so he would know who he was allowed to walk past,
and Jesus flipped the question -- not who counts as my neighbour, but which of
them acted like one.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "A scholar of the law stood up to test Jesus, and asked him a question."),
    # Luke 10:25
    ("s25", SCRIPTURE, "Master, what shall I do to inherit eternal life?"),
    ("n1b", NARRATOR, "Jesus turned it straight back on him — what does the law say? And the man answered it well: love God with everything you are, and love your neighbor as yourself. Then he asked one more question. It sounds humble. It was not."),
    # Luke 10:29
    ("s29", SCRIPTURE, "And who is my neighbour?"),
    ("n2", NARRATOR, "It was the kind of question you ask when you are hoping the answer has limits. He wanted a line drawn, so he could know exactly who he was allowed to ignore."),
    ("n3", NARRATOR, "Jesus answered with a story. A man was traveling the steep, lonely road down to Jericho, a road so full of robbers that people called it the Way of Blood."),
    ("n4", NARRATOR, "Robbers were exactly what he found. They stripped him, beat him, and left him half dead in the dust beside the road."),
    ("n5", NARRATOR, "A priest came down that same road, saw the man, and crossed to the far side. Then a temple assistant came, looked, and also crossed over."),
    ("n6", NARRATOR, "These were the religious professionals, the men who knew the law best. Maybe they feared a bloody body would make them unclean for the temple. Either way, they kept their distance."),
    ("n7", NARRATOR, "Then a Samaritan came down the road. And the crowd listening to Jesus was raised to despise Samaritans. Different blood, wrong worship, an old hatred hundreds of years deep."),
    ("n8", NARRATOR, "A Samaritan was the last man in the world they expected to be the hero of the story."),
    ("n9", NARRATOR, "He saw the beaten stranger. And the text says he was moved with compassion."),
    ("n10", NARRATOR, "He knelt down in the dirt beside a man his people were supposed to hate. He cleaned and bound the wounds, lifted him onto his own animal, and walked beside him on foot."),
    ("n11", NARRATOR, "He brought him to an inn and cared for him through the night. In the morning he pressed two silver coins into the innkeeper's hand, about two days wages, and said, take care of him."),
    # Luke 10:35
    ("j35", JESUS, "Take care of him; and whatsoever thou spendest more, when I come again, I will repay thee."),
    ("n12", NARRATOR, "And whatever more it costs, when I come back, I will repay you myself. He did not just help and move on. He tied his own name to a stranger's recovery."),
    ("n13", NARRATOR, "Then Jesus turned the scholar's own question back on him, and asked which of the three men had been the neighbor."),
    # Luke 10:36
    ("j1", JESUS, "Which now of these three, thinkest thou, was neighbour unto him that fell among the thieves?"),
    # Luke 10:37
    ("s37", SCRIPTURE, "He that shewed mercy on him."),
    ("n14", NARRATOR, "The scholar could not even say the word Samaritan. He answered, the one who showed mercy. Jesus had flipped the whole question. Not who counts as my neighbor, but which of them acted like one."),
    # Luke 10:37
    ("j2", JESUS, "Go, and do thou likewise."),
    ("n15", NARRATOR, "Stop asking who you are allowed to walk past. Go, and be the neighbor. That is how good he is. He will not even let you keep score."),
    ("card", NARRATOR, "Everyone finds themselves somewhere on that road. Where are you on it right now?"),
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
