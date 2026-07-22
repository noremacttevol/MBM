#!/usr/bin/env python3
"""Narration for build-14-ten-lepers — Luke 17.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Luke 17:11-19. j1, j2 and j3 are Jesus in the flesh and stay RED. The ten
lepers are men in the story, not Jesus, so their cry is SCRIPTURE (blue) - the video
only had it as a white caption with no verse behind it:
  s13  Luke 17:13  'Jesus, Master, have mercy on us.'
n15 is the closing card and keeps its id.
still_vars are introduced for this build (S1..S12); the old template referenced the
jpegs by literal filename.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "On the way to Jerusalem, Jesus walked the borderland between Samaria and Galilee — the seam between two peoples who despised each other. Keep that seam in mind. It matters at the end of this story."),
    ("n1", NARRATOR, "As he reached a village, ten men met him — but they stopped far off, strung along a rise, and came no closer. They were lepers. The Law of Moses required them to live outside the town and to warn everyone away. That gap of empty ground between them and the road was not shyness. It was the law. These were ten men no one had touched in years."),
    # Luke 17:13
    ("s13", SCRIPTURE, "Jesus, Master, have mercy on us."),
    ("n2", NARRATOR, "So they did the only thing the distance left them. They lifted up their voices together and called across the gap: Jesus, Master, have mercy on us."),
    ("n3", NARRATOR, "When he saw them, he did not close the distance. He did not touch them, and he did not announce that they were healed. He simply gave them an instruction:"),
    # Luke 17:14
    ("j1", JESUS, "Go shew yourselves unto the priests."),
    ("n4", NARRATOR, "Now, why send them to a priest? Because in Israel the priest was the only inspector who could certify a leper clean and let him back into his family, his work, his worship. Sending them was a promise in disguise. That errand only made sense one way: if they would be clean by the time they arrived."),
    ("n5", NARRATOR, "But nothing had changed yet. They looked at each other, at their own still-bandaged hands, at the long road to a city they had no proof they would be welcome in. And then, one by one, they turned and started walking anyway."),
    ("n6", NARRATOR, "And as they went — on the road, mid-step, in the middle of obeying, before there was one thing to see — they were made clean."),
    ("n7", NARRATOR, "The linen loosened and fell. New skin underneath. Nine of them ran on toward the city, toward the priests, toward their old lives handed back. But one of them, when he saw what had happened to him, stopped in the road."),
    ("n8", NARRATOR, "And he turned around. He came back the way he came, running, praising God at the top of his voice — the whole road hearing it."),
    ("n9", NARRATOR, "He threw himself face-down in the dust at Jesus's feet and poured out his thanks. And Luke adds one detail that would have stunned everyone listening: he was a Samaritan. The outsider. The one the religion of the day said did not belong."),
    ("n10", NARRATOR, "Jesus looked at the empty road where the other nine had gone, and asked:"),
    # Luke 17:17-18
    ("j2", JESUS, "Were there not ten cleansed? but where are the nine? There are not found that returned to give glory to God, save this stranger."),
    ("n11", NARRATOR, "Except this stranger. This outsider. This is not wounded pride — the nine did nothing wrong. They obeyed, and they were healed, every one of them. His question is grief, not a scolding: they got the gift and kept walking, and they missed the giver. Only the one everyone counted out came back to find him."),
    ("n12", NARRATOR, "Then Jesus reached down to the man still trembling at his feet, and lifted him with a word:"),
    # Luke 17:19
    ("j3", JESUS, "Arise, go thy way: thy faith hath made thee whole."),
    ("n13", NARRATOR, "Hear the two different words. All ten were cleansed — out on the road, before any of them said thank you. But only this one, the one who came back, was made whole. Cleansed happened to his skin. Whole happened to all of him."),
    ("n14", NARRATOR, "And he rose and walked home a whole man, the old wrappings left behind him in the road."),
    ("n15", NARRATOR, "The healing happened while they walked, before they could see it. Have you ever had to move forward on nothing but a word — before there was any proof?"),
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
