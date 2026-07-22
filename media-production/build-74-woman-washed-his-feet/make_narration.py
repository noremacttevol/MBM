#!/usr/bin/env python3
"""Narration for build-74-woman-washed-his-feet — Luke 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THE WOMAN IS SILENT, AND THAT IS THE POINT. Checked carefully: Luke 7:36-50
records not one word from her. She weeps, she washes his feet with her tears,
she wipes them with her hair, she kisses them, she pours out the ointment - and
she never speaks. NOTHING WAS INVENTED FOR HER. There is no pink in this video
and there should not be. Every word about her in this chapter is spoken by
somebody else: Simon writes her off in his head, and Jesus defends her out loud.
That is the story. She never has to say anything.

STAYED RED: j1 (Luke 7:47), j2 (7:48) and j3 (7:50) are all Jesus in the flesh
and a red-letter KJV inks all three.

ADDED RED. Most of what he actually said was sitting in the video as narrator
paraphrase:
  j40  Luke 7:40  'Simon, I have somewhat to say unto thee.'
  j41  Luke 7:41-42  'There was a certain creditor which had two debtors: the
       one owed five hundred pence, and the other fifty. And when they had
       nothing to pay, he frankly forgave them both. Tell me therefore, which of
       them will love him most?'  - this is one of the three parables named in
       SPEAKER-LAW section 5 as still-red. Inside a parable the characters'
       words are Jesus's words.
  j44  Luke 7:44  'Seest thou this woman? I entered into thine house, thou
       gavest me no water for my feet: but she hath washed my feet with tears,
       and wiped them with the hairs of her head.'  n5 keeps its id and text and
       now retells it, on the same still S3.

ADDED AS SCRIPTURE, light blue - everyone in the room who is not Jesus:
  s39  Luke 7:39  'This man, if he were a prophet, would have known who and what
       manner of woman this is that toucheth him: for she is a sinner.'  Simon,
       thinking it, not saying it. n3 keeps its id and now retells it.
  s40  Luke 7:40  'Master, say on.'  Simon answering. Short on purpose - it is
       the permission that lets the parable start.
  s43  Luke 7:43  'I suppose that he, to whom he forgave most.'  Simon walking
       into it. n4 keeps its id and was rewritten to retell the parable and his
       answer together, since the verbatim now does the work n4 used to do.
  s49  Luke 7:49  'Who is this that forgiveth sins also?'  the table muttering.
       n6 keeps its id and text and now retells it.
  n5b  new narrator beat on S7 so 'Her sins, which are many, are forgiven' gets
       retold before 'Thy sins are forgiven' lands.

THE HUSH IS UNTOUCHED. j3 'Thy faith hath saved thee; go in peace' runs straight
into the silent still on S9 with no retelling, deliberately. That line needs no
translating and the silence after it is the best beat in the video. Left exactly
as the original build had it.

WHY-LAW: Simon knew what she was. Jesus knew what she had become. She was the
only person at that table who did not need the parable explained to her.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "A Pharisee named Simon invited Jesus to dinner. It was a careful, respectable house — and it was about to be interrupted."),
    ("n1", NARRATOR, "A woman from the town — a woman everyone in that room knew by her reputation — came in uninvited. She carried an alabaster jar of costly perfume."),
    ("n2", NARRATOR, "She stood behind him at his feet — guests reclined at meals like this, their feet stretched away from the table — and she was weeping. Her tears fell on his feet. She wiped them with her hair, kissed them, and poured out the perfume."),
    # Luke 7:39
    ("s39", SCRIPTURE, "This man, if he were a prophet, would have known who and what manner of woman this is that toucheth him: for she is a sinner."),
    ("n3", NARRATOR, "Simon thought to himself: if this man were really a prophet, he would know what kind of woman is touching him. He never said a word of it out loud."),
    # Luke 7:40
    ("j40", JESUS, "Simon, I have somewhat to say unto thee."),
    # Luke 7:40
    ("s40", SCRIPTURE, "Master, say on."),
    # Luke 7:41-42
    ("j41", JESUS, "There was a certain creditor which had two debtors: the one owed five hundred pence, and the other fifty. And when they had nothing to pay, he frankly forgave them both. Tell me therefore, which of them will love him most?"),
    # Luke 7:43
    ("s43", SCRIPTURE, "I suppose that he, to whom he forgave most."),
    ("n4", NARRATOR, "Jesus answered the thought Simon never said out loud — with a small story. Two men were in debt. One owed ten times what the other did, and neither of them could pay a penny of it, so the lender wiped out both debts. Which one will love him more? Simon gave the only answer there was: the one who was forgiven more. And he was right — he just had not noticed he was talking about the woman on the floor."),
    # Luke 7:44
    ("j44", JESUS, "Seest thou this woman? I entered into thine house, thou gavest me no water for my feet: but she hath washed my feet with tears, and wiped them with the hairs of her head."),
    ("n5", NARRATOR, "Then he turned toward the woman — but kept talking to Simon. Look at her, he said. When I walked into your house, you offered me no water for my feet, no welcome, no oil. She has done nothing else since she came in."),
    # Luke 7:47
    ("j1", JESUS, "Her sins, which are many, are forgiven; for she loved much: but to whom little is forgiven, the same loveth little."),
    ("n5b", NARRATOR, "Her sins are many, he said, and they are forgiven — and that is exactly why she loves like this. The one who thinks he has been forgiven little, loves little. Simon had been sitting there the whole meal, certain he was the clean one."),
    # Luke 7:48
    ("j2", JESUS, "Thy sins are forgiven."),
    # Luke 7:49
    ("s49", SCRIPTURE, "Who is this that forgiveth sins also?"),
    ("n6", NARRATOR, "The table stirred — who is this, who even forgives sins? He did not answer them. He was still looking at her."),
    # Luke 7:50
    ("j3", JESUS, "Thy faith hath saved thee; go in peace."),
    ("card", NARRATOR, "She was known for the worst thing she'd done. He knew her for her love. Which name would you rather answer to?"),
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
