#!/usr/bin/env python3
"""Generate narration audio for Story Video #84 — No Room, the Manger (Luke 2:1-7).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.

NO JESUS-SPEECH LINE: the child is a newborn, so there is no Christopher (Jesus) voice
in this video. The sacred KJV moment is the birth verse itself, Luke 2:7, read reverently
by the NARRATOR and rendered cream-italic as a scripture verse card (build.py flags "v7"
as KJV for cream-italic styling + a sacred silence). Christopher's voice is reserved for
Jesus's own words and is deliberately not used here.

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS and
word-wraps each text as the on-screen caption.

TRANSLATION LAW: n7 gives the meaning of v7 without re-quoting "swaddling / manger / inn".

FACE LAW: the infant's face is never shown or constructed anywhere in the video (swaddled,
turned away, seen past the parents) — see PROMPTS.md. Narration never asks the art to show
his face; "she looked into the face of God" (n6) is spoken over a shot where the baby's
face is turned in toward Mary and unseen.

WHY-LAW — milk of the gentlest kind: the God who made everything arrived with nowhere to
stay and was laid in a feed-trough, all the way down at the bottom, close enough for anyone
to reach. "No room for him then, so there would always be room for us now" (n11-n12). The
birth is spoken of with complete modesty — never graphic.

NUMBER-STRESS LAW: "Ninety miles of hill country" (n2) is a rare sentence-opening number,
but it lands as distance/hardship, not a bare count; kept for the weight of the journey.

CLOSING CARD IS AN INVITATION, never a fear-question. The card's question reassures — if he
would be born in a cattle-stall to be near you, there is room for you near him.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the decree ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "In those days a decree went out from Caesar Augustus, the emperor in far-off "
     "Rome, that the whole known world should be counted and taxed. And so every "
     "family in the land had to pack up and travel to the town their ancestors came "
     "from, to be registered."),
    # --- s2: the long road ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "For a young woman named Mary and a carpenter named Joseph, that meant a long, "
     "hard road. Ninety miles of hill country, on foot and by donkey, from Nazareth "
     "down to Bethlehem, the town of King David. And Mary was not travelling light. "
     "She was days away from giving birth."),
    # --- s3: crowded Bethlehem ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "When they finally reached Bethlehem, the little town was bursting. Everyone "
     "with roots there had come back for the same count, and every house, every spare "
     "room, every corner was already taken. There was simply nowhere left."),
    # --- s4: no room ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Door after door, the answer was the same. Not out of cruelty. The town was just "
     "full. And somewhere in that search, a tired householder, sorry that he had no "
     "space, pointed them to the only shelter left, the place where he kept his "
     "animals."),
    # --- s5: the stable ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "So the King of all creation was born in a stable. A cave of rough stone, straw "
     "on the floor, an ox and a donkey for company, and a wooden feed-trough standing "
     "in the corner. It was the lowest room in the whole town. And it was the only one "
     "with space."),
    # --- s6: the birth (modest) ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And there, in the quiet, with no midwife and no crowd, Mary gave birth to her "
     "first son. She wrapped him tightly in strips of cloth, the way every mother "
     "there wrapped a newborn, and she looked into the face of God."),
    # --- s7: Luke 2:7 — the verse card. Cream-italic, sacred silence. ---
    ("v7", NARRATOR, "-26%", "-6Hz",
     "And she brought forth her firstborn son, and wrapped him in swaddling clothes, "
     "and laid him in a manger; because there was no room for them in the inn."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Read that again slowly. The one who made the stars had nowhere to lay his head "
     "the very night he arrived. The hands that shaped the mountains were small enough "
     "to curl around a mother's finger. He did not come down halfway. He came all the "
     "way down, to the bottom, to the people the world had no space for."),
    # --- s8: the wonder ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "And his mother and the man who would raise him knelt in the straw and simply "
     "looked at him. No trumpets. No palace. Just two ordinary, exhausted, overjoyed "
     "people, and a baby, and more love in that cold little room than the whole full "
     "town could hold."),
    # --- s9: the humble king ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "That is the scandal and the sweetness of it. The King everyone was too busy to "
     "make room for did not force his way in. He came small, and quiet, and poor, and "
     "laid himself down among the animals, close enough for anyone at all to come "
     "near."),
    # --- s10: the sleeping town ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "And the town slept on, not knowing. Every crowded house with no room, every "
     "window dark, while a few streets over the most important thing in the history of "
     "the world had just happened by the light of one small lamp."),
    # --- s11: heaven's answer ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "There is something in that you were meant to see. The room the world would not "
     "give him, heaven filled with light. He was turned away at every door, so that no "
     "one who comes to him would ever have to be."),
    # --- s12: there is room now ---
    ("n12", NARRATOR, "-24%", "-4Hz",
     "Because that is the whole reason he came down so low. There was no room for him, "
     "once, so that there would always be room for you. The door of that stable is "
     "still open. He is still the easiest person in the world to reach."),
    # --- closing card, read gently (Readable-Card Law). An INVITATION. ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "There was no room for him in the whole town, on the night he came to save it. "
     "If he was willing to be born in a cattle-stall to be near you, what makes you "
     "think there is no room for you near him?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
