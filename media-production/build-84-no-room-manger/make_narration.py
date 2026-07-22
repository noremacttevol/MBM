#!/usr/bin/env python3
"""Narration for build-84-no-room-manger — Luke 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THE FIX: LUKE WAS PAINTED AS JESUS. v7 was red -- 'And she brought forth her
firstborn son, and wrapped him in swaddling clothes, and laid him in a manger;
because there was no room for them in the inn.' That is LUKE NARRATING, Luke 2:7.
Nobody speaks it. It is now `scripture` (light blue). Leaving it red had the
newborn in the manger narrating his own birth in the third person. The id v7 is
kept so the music bed and start_of[] stay attached. n7 already retells it and was
left alone.

NOTHING IS RED IN THIS BUILD, AND THAT IS CORRECT. Luke 2:1-7 contains no
dialogue at all -- not from Jesus, not from Mary, not from Joseph, not from the
innkeeper. Every word of the passage is Luke writing. A red-letter KJV prints not
one word of it red. So this build has no `jesus` beats, by design and not by
oversight.

ADDED -- LUKE'S OPENING SENTENCE, now `scripture`:
  sv1  Luke 2:1  'And it came to pass in those days, that there went out a decree
       from Caesar Augustus, that all the world should be taxed.'  Placed on S1
       with the existing n1 immediately after as its retelling -- n1 already says
       the same thing in modern English, so no narrator text needed rewriting. It
       is the most recognisable opening line in the Bible and it was not in the
       video.

NO GREEN: nothing in Luke 2:1-7 is the Father or a voice from heaven. Heaven does
not speak until the shepherds' hillside, which is build-85.

WOMEN -- MARY IS PRESENT AND SILENT. Luke records not one word from her in verses
1 through 7. She travels ninety miles nine months pregnant, gives birth, and says
nothing on the page. NOTHING was put in her mouth and there is NO PINK in this
build. Her one great speech, the Magnificat, is Luke 1:46-55, months earlier and
a different story; borrowing it into the stable would be putting words in her
mouth on the wrong night. n6 and n8 carry her in the storyteller's voice instead.

WHY-LAW: the King everyone was too busy to make room for did not force his way
in. He came small and poor and low enough for anyone at all to walk up to. Milk:
there was no room for him once, so that there would always be room for you.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    # Luke 2:1
    ("sv1", SCRIPTURE, "And it came to pass in those days, that there went out a decree from Caesar Augustus, that all the world should be taxed."),
    ("n1", NARRATOR, "In those days a decree went out from Caesar Augustus, the emperor in far-off Rome, that the whole known world should be counted and taxed. And so every family in the land had to pack up and travel to the town their ancestors came from, to be registered."),
    ("n2", NARRATOR, "For a young woman named Mary and a carpenter named Joseph, that meant a long, hard road. Ninety miles of hill country, on foot and by donkey, from Nazareth down to Bethlehem, the town of King David. And Mary was not travelling light. She was days away from giving birth."),
    ("n3", NARRATOR, "When they finally reached Bethlehem, the little town was bursting. Everyone with roots there had come back for the same count, and every house, every spare room, every corner was already taken. There was simply nowhere left."),
    ("n4", NARRATOR, "Door after door, the answer was the same. Not out of cruelty. The town was just full. And somewhere in that search, a tired householder, sorry that he had no space, pointed them to the only shelter left, the place where he kept his animals."),
    ("n5", NARRATOR, "So the King of all creation was born in a stable. A cave of rough stone, straw on the floor, an ox and a donkey for company, and a wooden feed-trough standing in the corner. It was the lowest room in the whole town. And it was the only one with space."),
    ("n6", NARRATOR, "And there, in the quiet, with no midwife and no crowd, Mary gave birth to her first son. She wrapped him tightly in strips of cloth, the way every mother there wrapped a newborn, and she looked into the face of God. Luke tells it in one sentence, and he does not raise his voice for any of it:"),
    # Luke 2:7
    ("v7", SCRIPTURE, "And she brought forth her firstborn son, and wrapped him in swaddling clothes, and laid him in a manger; because there was no room for them in the inn."),
    ("n7", NARRATOR, "She had her first son, wrapped him up, and laid him in a feed trough, because there was no room for them anywhere else. Read that again slowly. The one who made the stars had nowhere to lay his head the very night he arrived. The hands that shaped the mountains were small enough to curl around a mother's finger. He did not come down halfway. He came all the way down, to the bottom, to the people the world had no space for."),
    ("n8", NARRATOR, "And his mother and the man who would raise him knelt in the straw and simply looked at him. No trumpets. No palace. Just two ordinary, exhausted, overjoyed people, and a baby, and more love in that cold little room than the whole full town could hold."),
    ("n9", NARRATOR, "That is the scandal and the sweetness of it. The King everyone was too busy to make room for did not force his way in. He came small, and quiet, and poor, and laid himself down among the animals, close enough for anyone at all to come near."),
    ("n10", NARRATOR, "And the town slept on, not knowing. Every crowded house with no room, every window dark, while a few streets over the most important thing in the history of the world had just happened by the light of one small lamp."),
    ("n11", NARRATOR, "There is something in that you were meant to see. The room the world would not give him, heaven filled with light. He was turned away at every door, so that no one who comes to him would ever have to be."),
    ("n12", NARRATOR, "Because that is the whole reason he came down so low. There was no room for him, once, so that there would always be room for you. The door of that stable is still open. He is still the easiest person in the world to reach."),
    ("card", NARRATOR, "There was no room for him in the whole town, on the night he came to save it. If he was willing to be born in a cattle-stall to be near you, what makes you think there is no room for you near him?"),
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
