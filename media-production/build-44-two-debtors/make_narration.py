#!/usr/bin/env python3
"""Narration for build-44-two-debtors — Luke 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THIS BUILD HAS BOTH KINDS OF SPEECH IN IT, AND THAT IS THE WHOLE JOB HERE.
The parable of the two debtors is only two verses long and sits inside a conversation
between Jesus and Simon the Pharisee. Inside the parable, everything is red. Outside
it, Simon is a real man in a real house and he is BLUE.

STAYED RED:
  j1  Luke 7:40  'Simon, I have somewhat to say unto thee.'
  j2  Luke 7:41  'There was a certain creditor which had two debtors...' -- named in
      SPEAKER-LAW itself as a line that stays red.
  j3  Luke 7:42  'And when they had nothing to pay, he frankly forgave them both.
      Tell me therefore, which of them will love him most?'
  j4  Luke 7:47  'Her sins, which are many, are forgiven; for she loved much...'
  j5  Luke 7:50  'Thy faith hath saved thee; go in peace.'

BLUE ADDED -- SIMON, WHO IS OUTSIDE THE PARABLE AND WAS NEVER HEARD:
  s40  Luke 7:40  'Master, say on.' Simon answering Jesus at his own table. Not
       inside the parable, not Jesus's words, so `scripture`, light blue.
  s43  Luke 7:43  'I suppose that he, to whom he forgave most.' Simon's answer to the
       riddle. This was buried inside n7 as white paraphrase -- 'And Simon answered, a
       little carefully' -- and it is the line the entire trap closes on. Blue.
  Note the colour change across three consecutive beats on S6: j3 red (the question,
  inside the parable), s43 blue (Simon answering, outside it), j3b red (Jesus's
  verdict). That run is the clearest demonstration in this whole set of where the
  parable ends.

RED ADDED:
  j3b   Luke 7:43  'Thou hast rightly judged.' Jesus's four-word reply to Simon.
  jv44  Luke 7:44-46  'Seest thou this woman? I entered into thine house, thou gavest
        me no water for my feet: but she hath washed my feet with tears... Thou gavest
        me no kiss... My head with oil thou didst not anoint: but this woman hath
        anointed my feet with ointment.' The comparison that breaks Simon open, and it
        was entirely white paraphrase in n8. n8 keeps its id and now retells it.
  jv48  Luke 7:48  'Thy sins are forgiven.' The actual absolution, said out loud to
        her, and it was missing from the video completely. New n9b retells it before
        j5 lands.

THE WOMAN -- LOOKED FOR HER, AND SHE IS SILENT. Cameron's standing instruction is to
find the women and let them speak. Luke 7:36-50 does not record one word from her. She
weeps, wipes his feet with her hair, kisses them and pours out the ointment, and she
never says anything. Luke never even gives her a name. So there is NO `woman` beat in
this plan, and nothing was invented to make one. She is heard in this video the way
Luke wrote her -- Jesus does all her talking for her, in jv44 and j4 and jv48, and
that is the point of the passage. If a later pass wants her voice, it does not exist
in this chapter and must not be manufactured.

NEW NARRATOR BEATS: n4b retells j1 and s40; n9b retells jv48. Both are additions, no
existing id was renamed or dropped.

NO GREEN in Luke 7:36-50.

WHY-LAW: she was not forgiven because she loved much, she loved much because she had
been forgiven. Milk: the size of your love follows the size of the debt you know was
torn up.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "A Pharisee named Simon invited Jesus to dinner. It was a careful, respectable house, and having a well-known teacher at your table made you look good. So Jesus came, and took his place at the low table with the other guests."),
    ("n2", NARRATOR, "Then the door opened, and a woman came in who did not belong there. Everyone in that town knew what she was. She had lived a life the whole village whispered about, and she walked into a Pharisee's house carrying a small alabaster jar of costly perfume."),
    ("n3", NARRATOR, "She went straight to his feet. And there, in front of every important man in the room, she broke. She wept until her tears fell on his feet, and she wiped them away with her own hair, and kissed them, and poured the perfume out over them."),
    ("n4", NARRATOR, "Simon watched, and said nothing out loud. But inside, he had already made up his mind. If this man were really a prophet, he thought, he would know what kind of woman is touching him, and he would never let her near."),
    # Luke 7:40
    ("j1", JESUS, "Simon, I have somewhat to say unto thee."),
    # Luke 7:40
    ("s40", SCRIPTURE, "Master, say on."),
    ("n4b", NARRATOR, "Simon, there is something I want to say to you. Say it, teacher, Simon answered. He had been thinking it, not saying it, and Jesus answered the thought."),
    ("n5", NARRATOR, "And instead of scolding anyone, Jesus told him a small story. There was a man who lent money, and two people owed him."),
    # Luke 7:41
    ("j2", JESUS, "There was a certain creditor which had two debtors: the one owed five hundred pence, and the other fifty."),
    ("n6", NARRATOR, "One of them owed about two years of wages. The other owed a couple of months. Very different weights around their necks. But the same problem: neither of them had a single coin left to pay it back."),
    # Luke 7:42
    ("j3", JESUS, "And when they had nothing to pay, he frankly forgave them both. Tell me therefore, which of them will love him most?"),
    # Luke 7:43
    ("s43", SCRIPTURE, "I suppose that he, to whom he forgave most."),
    # Luke 7:43
    ("j3b", JESUS, "Thou hast rightly judged."),
    ("n7", NARRATOR, "To forgive them frankly meant he simply let it go. He did not lower the payments. He tore both debts up and asked for nothing back. And Simon answered, a little carefully: I suppose the one who was let off the most. You have judged rightly, Jesus told him. The one who was carrying the heavier weight is the one who walks away loving the most."),
    # Luke 7:44-46
    ("jv44", JESUS, "Seest thou this woman? I entered into thine house, thou gavest me no water for my feet: but she hath washed my feet with tears, and did wipe them with the hairs of her head. Thou gavest me no kiss: but this woman since the time I came in hath not ceased to kiss my feet. My head with oil thou didst not anoint: but this woman hath anointed my feet with ointment."),
    ("n8", NARRATOR, "Then Jesus turned and looked at the woman, but he kept speaking to Simon. He set the two of them side by side. Simon had given him no water for his feet; she had washed them with her tears. Simon had given him no greeting; she had not stopped kissing his feet since she came in."),
    # Luke 7:47
    ("j4", JESUS, "Her sins, which are many, are forgiven; for she loved much: but to whom little is forgiven, the same loveth little."),
    ("n9", NARRATOR, "Read that slowly, because it is easy to turn it backwards. She was not forgiven because she loved so much. She loved so much because she had already been forgiven. The tears were not the payment. They were what it looks like when a debt you could never repay is torn up right in front of you. Simon loved little, because he believed he owed little."),
    # Luke 7:48
    ("jv48", JESUS, "Thy sins are forgiven."),
    ("n9b", NARRATOR, "Your sins are forgiven. He said it out loud, at a full table, in front of every important man in that town, to the one person in the room everybody there had already written off."),
    # Luke 7:50
    ("j5", JESUS, "Thy faith hath saved thee; go in peace."),
    ("n10", NARRATOR, "She came in as the woman everybody had already judged. She walked out saved, and at peace, and loved. And here is the quiet danger in Simon's seat at the table. If you are sure you are only a small sinner, you will only ever be a small lover of God. But let yourself be the one forgiven much, and you get to be the one who loves much. That was never the punishment. That is the gift."),
    ("card", NARRATOR, "The woman knew exactly how much she had been forgiven, and it made her fearless with love. How much do you believe you have been forgiven?"),
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
