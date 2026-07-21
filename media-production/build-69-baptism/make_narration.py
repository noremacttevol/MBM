#!/usr/bin/env python3
"""Narration for build-69-baptism — Matthew 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THE FATHER IS GREEN, NOT RED -- AND THE SEGMENT WAS WELDED SHUT.
  jv1 was ONE red beat reading: 'And lo a voice from heaven, saying, This is my
  beloved Son, in whom I am well pleased.' Two speakers in one block, painted red
  end to end. That means the video had Jesus, standing in the Jordan, announcing
  himself as his own beloved Son -- and reading Matthew's stage direction in his
  own voice on the way in. It is SPLIT:
     s17  `scripture`  'And lo a voice from heaven, saying,'   -- Matthew writing.
     jv1  `god` GREEN  'This is my beloved Son, in whom I am well pleased.'
  jv1 KEEPS ITS ID, so start_of['jv1'] and the music bed stay attached; the new
  framing clause gets the fresh id s17. Both beats stay on S7 -- same still,
  consecutive beats, and the edit the viewer sees is identical.
  This is the most important call in the build. Matthew 3:17 is the Father's
  voice, at the one moment in the Gospels where all three members of the Godhead
  are distinctly present, and n6 is built entirely on that point. Painting the
  Father red destroyed the very thing n6 goes on to explain.

STAYED RED: j1, Matthew 3:15, 'Suffer it to be so now: for thus it becometh us to
fulfil all righteousness.' Jesus in the flesh, red-lettered, verbatim. Unchanged.

JOHN THE BAPTIST NOW SPEAKS. n1 paraphrased his protest in modern English -- 'It
should be the other way around, he said' -- and the viewer never heard the actual
words. Lifted verbatim as `scripture` (a man in the story, not Deity):
  s14  Matthew 3:14  'I have need to be baptized of thee, and comest thou to me?'
  n1 is trimmed to the frame, n1b carries the retelling. Both on S2.

RETELLING: n3 already retells j1 ('Let it happen, John'), and n6 already retells
the Father's line and does the doctrinal work. Only n1b is new.

WOMEN: Matthew 3 records no woman speaking. Nothing added; nothing invented.

VALIDATOR NOTE: s17 is followed directly by jv1 rather than by a narrator
retelling. That is intentional and correct -- s17 is a five-word stage direction
introducing the Father, not a scripture quotation that needs explaining. Wedging
a retelling between 'and lo a voice from heaven, saying' and what the voice said
would be absurd. n6 retells the Father's words immediately after.

WHY-LAW: the Father's first recorded words about his Son came before Jesus had
preached one sermon or healed one person. Milk: identity first, approval before
achievement -- and he walked through the door ahead of us so no one would be
asked to go somewhere he had not gone.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Down at the Jordan river, John was baptizing. He was rough as the desert he came from — a coat of camel's hair, a leather belt, a voice like a trumpet — and the whole countryside was walking out to him to confess and start over in that muddy water. Every day, sinners lined the bank. And then one day, somebody joined the line who had nothing to confess."),
    ("n1", NARRATOR, "Jesus walked from Galilee — days on foot — specifically to be baptized by John. And John, the wild man who was afraid of nobody, took one look and refused:"),
    # Matthew 3:14
    ("s14", SCRIPTURE, "I have need to be baptized of thee, and comest thou to me?"),
    ("n1b", NARRATOR, "I'm the one who needs what you have, he said — and you're coming to me? It should be the other way around. You coming to ME makes no sense."),
    ("n2", NARRATOR, "And John was right — it did not make sense. Baptism was for washing sins away, and Jesus had none. So listen carefully to the reason Jesus gives, because it tells you why he did almost everything:"),
    # Matthew 3:15
    ("j1", JESUS, "Suffer it to be so now: for thus it becometh us to fulfil all righteousness."),
    ("n3", NARRATOR, "Let it happen, John — this is how we do everything right, together. He was not washing anything away. He was stepping into line with us. If baptism is the doorway God asks people to walk through, then Jesus would walk through it first — not because he needed it, but so that no one who followed him would ever be asked to do something he had not done himself. He never leads from behind."),
    ("n4", NARRATOR, "So John baptized him — lowered him under the water of the Jordan, and raised him up again. And as Jesus came straight up out of the water, the sky itself broke open."),
    ("n5", NARRATOR, "The Spirit of God came down through the opened heavens like a dove, gentle as falling light, and rested on him. And then a voice came out of heaven — not John's voice, not any voice on the riverbank. A Father's voice."),
    # Matthew 3:17
    ("s17", SCRIPTURE, "And lo a voice from heaven, saying,"),
    # Matthew 3:17
    ("jv1", GOD, "This is my beloved Son, in whom I am well pleased."),
    ("n6", NARRATOR, "Stand on that riverbank for a second. The Son is standing in the water. The Spirit is descending upon him. The Father is speaking from heaven. Three — each one distinct, each one present, all in one moment — and what the Father chose to say, before Jesus had preached one sermon or healed one person, was: this is my Son, and I love him, and I am pleased with him. Identity first. Approval before achievement."),
    ("n7", NARRATOR, "Jesus began everything from that sentence. Not working TOWARD being loved — working FROM it. And the doorway he walked through that day, he left standing open behind him."),
    ("card", NARRATOR, "He walked through the door first, so you would never face one he hadn't. The way in is still open."),
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
