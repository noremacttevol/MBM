#!/usr/bin/env python3
"""Narration for build-118-jonah-god-who-relents — Jonah 1.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both red beats are the LORD speaking to Jonah - Old Testament, so GOD (green),
never `jesus`. A red-letter KJV prints none of Jonah in red.

LINES LIFTED OUT OF NARRATOR PARAPHRASE:
  gv1   Jonah 1:2   the first commission - n1 paraphrased it; now GOD, and it pairs
                    with jvA (Jonah 3:2), the second commission, so the viewer hears
                    God say the same thing twice to a man who ran the first time.
  s112  Jonah 1:12  Jonah telling the sailors to throw him overboard - SCRIPTURE.
  s29   Jonah 2:9   'Salvation is of the LORD.' The hinge of the book, said from
                    inside the fish - SCRIPTURE.
  s34   Jonah 3:4   'Yet forty days, and Nineveh shall be overthrown.' This was
                    already verbatim inside narrator beat n6 - pulled out to SCRIPTURE.
  s42   Jonah 4:2   Jonah's complaint: he ran because he knew God was gracious. This
                    is the reason the book exists and it was missing entirely.

NEW CLOSING RETELL: jvB (Jonah 4:11) was the last spoken beat before the card, so the
Old English landed unexplained. n9 now retells it over the same still S10.

LEFT AS PARAPHRASE ON PURPOSE: n7, the city repenting (Jonah 3:5-9). The king's decree
runs long and I was not certain enough of the exact clause order across 3:7-9 to quote
it, so the whole repentance beat stays narrator. Nothing was approximated.

MILK FRAMING: the book answers one question - is God eager to destroy or eager to
spare? Jonah's own complaint is the answer, and God gets the last word arguing for
mercy against his own prophet.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "God had a hard errand for a man named Jonah. He was to go to Nineveh — a huge, violent, foreign city, the capital of the empire everyone in Israel was afraid of. And this is how the word came to him."),
    # Jonah 1:2
    ("gv1", GOD, "Arise, go to Nineveh, that great city, and cry against it; for their wickedness is come up before me."),
    ("n1b", NARRATOR, "Go to that great city and preach against it, God said, because I have seen how bad it has gotten. Notice what that actually is. It is a warning. God would far rather warn a wicked city than lose it."),
    ("n2", NARRATOR, "But Jonah did not want mercy for people like that. So he ran. He found a ship going the exact opposite way and sailed off, trying to put an ocean between himself and a God he thought was far too forgiving."),
    ("n3", NARRATOR, "A great storm caught the ship, so fierce the sailors were sure they would all drown. They cast lots to find out whose fault it was, and the lot fell on Jonah. He knew it already. And what he told them is the first decent thing he does in the whole book."),
    # Jonah 1:12
    ("s112", SCRIPTURE, "Take me up, and cast me forth into the sea; so shall the sea be calm unto you: for I know that for my sake this great tempest is upon you."),
    ("n3b", NARRATOR, "Throw me in, he said. The sea will go quiet, because this storm is on me, not on you. He would rather drown than preach to Nineveh — but he would not let a boatful of strangers go down with him. So at last they did the only thing left, and cast him into the raging sea."),
    ("n4", NARRATOR, "And here is the first surprise of this story. The sea should have been the end of him. Instead, God sent a great fish — not to punish Jonah, but to catch him, and carry him, and keep him alive in the deep."),
    ("n5", NARRATOR, "For three days and three nights, in the dark, Jonah finally stopped running. From the belly of the fish he prayed, and his hard, resentful heart began at last to turn back toward the God who would not let him drown. His prayer ends in four words."),
    # Jonah 2:9
    ("s29", SCRIPTURE, "Salvation is of the LORD."),
    ("n5b", NARRATOR, "Rescue belongs to God. That is the whole lesson of the fish, and Jonah says it from the one place on earth where he could not save himself and had nothing left to bargain with."),
    # Jonah 3:2
    ("jvA", GOD, "Arise, go unto Nineveh, that great city, and preach unto it the preaching that I bid thee."),
    ("n6", NARRATOR, "The fish set him safe on dry land, and God gave him the exact same errand a second time — no mention of the running, no punishment attached. This time Jonah went. He walked into the great city and cried out his warning."),
    # Jonah 3:4
    ("s34", SCRIPTURE, "Yet forty days, and Nineveh shall be overthrown."),
    ("n6b", NARRATOR, "Forty more days and this city is finished. That was the entire sermon. No comfort in it anywhere, no invitation, no offer — just a countdown, preached by a man who was hoping it would come true."),
    ("n7", NARRATOR, "And the second surprise is bigger than the first. They listened. From the king on his throne down to the poorest beggar, the whole city turned — sackcloth, fasting, and honest sorrow — begging God for mercy they knew they did not deserve."),
    ("n8", NARRATOR, "And God, who had been looking for a reason to spare them all along, saw that they turned from their evil — and he relented. He did not destroy the city. He forgave it. The judgment never fell. And Jonah, watching from a hill outside the walls, was furious. Listen to why."),
    # Jonah 4:2
    ("s42", SCRIPTURE, "I knew that thou art a gracious God, and merciful, slow to anger, and of great kindness, and repentest thee of the evil."),
    ("n8b", NARRATOR, "I knew it, he says. I knew you were gracious and merciful and slow to anger. I knew you would forgive them. That is the confession at the bottom of the book. Jonah never ran because he thought God was harsh. He ran because he was afraid God was too good."),
    # Jonah 4:11
    ("jvB", GOD, "And should not I spare Nineveh, that great city, wherein are more than sixscore thousand persons that cannot discern between their right hand and their left hand; and also much cattle?"),
    ("n9", NARRATOR, "Should I not spare Nineveh? A hundred and twenty thousand people who cannot tell their right hand from their left — and the animals too. That is how the book ends. Not with Jonah answering, but with God still arguing for mercy, out loud, with his own prophet."),
    ("card", NARRATOR, "The whole book of Jonah exists to answer one question: is God eager to destroy, or eager to spare? He spared a city of a hundred thousand strangers the moment they turned. What would it change to believe God is that quick to forgive?"),
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
