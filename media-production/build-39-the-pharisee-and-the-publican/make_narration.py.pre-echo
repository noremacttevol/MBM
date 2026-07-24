#!/usr/bin/env python3
"""Narration for build-39-the-pharisee-and-the-publican — Luke 18.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THE MOST LIKELY MISTAKE IN THIS WHOLE SET WOULD HAVE BEEN HERE, AND IT WAS NOT MADE.
Both prayers stay RED. 'God, I thank thee, that I am not as other men are' is the
Pharisee praying, and 'God be merciful to me a sinner' is the publican praying --
but both men are characters inside Jesus's parable, and a red-letter KJV prints the
whole of Luke 18:9-14 red. Neither one becomes `scripture`. The test is never who
the character is; it is whether a red-letter Bible inks the line.

STAYED RED:
  j1  Luke 18:11-12  the Pharisee's prayer
  j2  Luke 18:13     'God be merciful to me a sinner.'
  j3  Luke 18:14     'I tell you, this man went down to his house justified...'

BLUE ADDED -- LUKE'S FRAMING, WHICH IS THE ONE THING IN THIS PASSAGE THAT IS NOT RED:
  s9  Luke 18:9  'And he spake this parable unto certain which trusted in themselves
      that they were righteous, and despised others.' That is Luke writing, so
      `scripture`, light blue. It is also the sentence that names the audience, and
      n1 was paraphrasing it in white. s9 now opens the video and n1 retells it.

RED ADDED -- the parable's own opening and its own stage direction:
  jv10  Luke 18:10  'Two men went up into the temple to pray; the one a Pharisee,
        and the other a publican.' n2 was paraphrasing it. n2 keeps its id and now
        retells it.
  jv13a Luke 18:13a 'And the publican, standing afar off, would not lift up so much
        as his eyes unto heaven, but smote upon his breast, saying.' NOTE CAREFULLY:
        this looks like evangelist framing, and in any other passage it would be
        blue -- but here it is Jesus narrating inside his own parable, so it is RED.
        It sits on S6 and the existing n7 retells it, then j2 lands the prayer on S7.
        Frame and speech are the same colour here on purpose.

Deliberately NOT lifted: nothing else. n3, n4, n6, n8a, n8b, n9 and the whole closing
run are the storyteller's commentary and the best writing in the build; turning any
of it into verbatim would flatten the video into a reading of five verses.

NO GREEN, and NO WOMEN: Luke 18:9-14 has neither. Nothing invented.

WHY-LAW: one man brought a list, the other brought nothing, and only one of them was
actually asking for something. Milk: you do not have to be presentable to pray.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    # Luke 18:9
    ("s9", SCRIPTURE, "And he spake this parable unto certain which trusted in themselves that they were righteous, and despised others."),
    ("n1", NARRATOR, "Jesus told this story to a certain kind of man. The kind who was sure he was one of the good ones, and just as sure that other people were not."),
    # Luke 18:10
    ("jv10", JESUS, "Two men went up into the temple to pray; the one a Pharisee, and the other a publican."),
    ("n2", NARRATOR, "Two men went up to the temple to pray. One was a Pharisee. The other was a tax collector. And to anyone watching them climb those steps, it was obvious which of the two God was pleased with."),
    ("n3", NARRATOR, "The Pharisee was not a fake. God had asked for one fast a year, and this man fasted twice a week. He gave away a tenth of everything he owned, down to the herbs in his garden. Ask that city who its best man was, and every finger would have pointed at him."),
    ("n4", NARRATOR, "The tax collector was exactly what everyone thought he was. He worked for Rome, the empire occupying his own country, collecting from his own neighbors and keeping whatever extra he could squeeze out of them. A traitor with a money box. And he knew it."),
    ("n5", NARRATOR, "The Pharisee took his place out in the open, where he could be seen, and lifted his hands to pray. Listen to who his prayer is really about."),
    # Luke 18:11-12
    ("j1", JESUS, "God, I thank thee, that I am not as other men are, extortioners, unjust, adulterers, or even as this publican. I fast twice in the week, I give tithes of all that I possess."),
    ("n6", NARRATOR, "He is not asking God for anything. He is handing God a list of his own achievements. In one short prayer, he says the word I five times. And he cannot even finish it without stepping on the man behind him."),
    # Luke 18:13
    ("jv13a", JESUS, "And the publican, standing afar off, would not lift up so much as his eyes unto heaven, but smote upon his breast, saying,"),
    ("n7", NARRATOR, "The tax collector did not go up front. He stopped at the very back, as far as a man could get and still be in the temple. He could not bring himself to lift his eyes. He struck his own chest, the way people do when someone has died. And he prayed a prayer of only seven words."),
    # Luke 18:13
    ("j2", JESUS, "God be merciful to me a sinner."),
    ("n8a", NARRATOR, "There is more in that prayer than it sounds like. He is standing in the temple at the hour of sacrifice, while a lamb is being killed for the sins of the whole nation, and he is asking God to let that mercy fall on him. Him, personally."),
    ("n8b", NARRATOR, "And in Luke's Greek, he does not count himself as one guilty man among many. He speaks as if he were the only one in the building."),
    ("n9", NARRATOR, "Two men. The same temple. The same God. One of them doing all the talking, the other barely able to speak. And then Jesus said the sentence that would have stopped every man listening to him cold."),
    # Luke 18:14
    ("j3", JESUS, "I tell you, this man went down to his house justified rather than the other: for every one that exalteth himself shall be abased; and he that humbleth himself shall be exalted."),
    ("n10", NARRATOR, "The traitor walked home right with God. The good man walked home exactly as he came. Not because God is impressed by failure, but because one of them came holding a list, and the other came holding nothing. Only one of them was actually asking for anything."),
    ("n11", NARRATOR, "He went down those steps a different man, and he had not done one thing to earn it. He had nothing to offer, and he knew it. That turned out to be the only thing he needed to get right."),
    ("n12", NARRATOR, "And the Pharisee? He is still standing there. Still praying. Still certain. Still fine. That is the saddest part of it. The only thing keeping that man out was how sure he was that he was already in."),
    ("n13", NARRATOR, "Jesus did not tell this story to shame the good men listening. He told it to let them in too. The door is not closed to people who have done wrong. It only closes from the inside, by people convinced they do not need it."),
    ("card", NARRATOR, "One man brought God his record. The other brought God the truth. If you stopped performing for a moment, what would you actually say to him?"),
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
