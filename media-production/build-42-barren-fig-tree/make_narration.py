#!/usr/bin/env python3
"""Narration for build-42-barren-fig-tree — Luke 13.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

PARABLE LAW APPLIED, AND THIS BUILD WAS ALREADY RIGHT. Luke 13:6-9 is four verses
long and the build already quotes all four verbatim. Every one of them stays RED,
including both characters' dialogue -- SPEAKER-LAW names this exact parable as the
worked example of where red is still correct:
  jv6  Luke 13:6  'A certain man had a fig tree planted in his vineyard...'
  jv7  Luke 13:7  the owner: 'cut it down; why cumbereth it the ground?'
  jv8  Luke 13:8  the vinedresser: 'Lord, let it alone this year also...'
  jv9  Luke 13:9  'And if it bear fruit, well: and if not...'
The owner and the vinedresser are the two most tempting characters in this whole set
to paint blue. They are not blue. They are Jesus, red, because a red-letter KJV inks
the whole parable and these are words Jesus put in their mouths.

BLUE ADDED -- one sentence, and it is the only non-red thing in the passage:
  s6a  Luke 13:6a  'He spake also this parable.' Luke's framing, so `scripture`,
       light blue. Short on purpose. It sits on S2 immediately before jv6, the frame
       blue and the parable red on the same still, which is the split pattern the law
       asks for. It goes straight into jv6 without a retelling between them -- that
       is deliberate, five words of framing do not need retelling, and n2 retells the
       verse right after.

NOTHING ELSE ADDED, AND THAT IS THE FINDING. There is no buried scripture left in
this build. n2, n3, n4, n5, n6, n7, n8, n9, n10, n10b, n11 and n12 are all the
storyteller working on material he has already quoted -- the vineyard soil, the
hardness of the ground, the dung, the axe going back against the wall, and who the
gardener is. Not one of them is a paraphrase of a verse that exists. Lifting anything
further would mean inventing scripture, and there is none to invent: the parable is
four verses and all four are already in the video.

Deliberately NOT pulled in: Luke 13:1-5, the tower of Siloam and 'except ye repent, ye
shall all likewise perish.' It is red and it is the lead-in that provokes this parable,
but this build is deliberately built as the kindness story, and opening with that verse
would turn a video about a second year into a video about perishing. That is a milk
decision, not an accuracy one.

NO GREEN and NO WOMEN in Luke 13:6-9. Nothing invented.

WHY-LAW: the tree did not change, and it got the year anyway, because somebody knelt
in the dirt and asked for it. Milk: mercy is asked for on your behalf before you have
anything to show.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "He told them a short story about a tree that was not doing its job. It sounds at first like a warning. Stay with it, because it turns into one of the kindest things he ever said about being given more time."),
    # Luke 13:6
    ("s6a", SCRIPTURE, "He spake also this parable;"),
    # Luke 13:6
    ("jv6", JESUS, "A certain man had a fig tree planted in his vineyard; and he came and sought fruit thereon, and found none."),
    ("n2", NARRATOR, "A fig tree in a vineyard had the best spot on the whole property. Deep worked soil, water meant for the grapes, a wall around it, full sun. Everything a tree could want was already handed to it. All it had to do was grow figs."),
    ("n3", NARRATOR, "So the owner came out to pick a few, the way you would. And there was nothing on it. Not a small crop. Not a late one. Bare leaves, and no fruit at all."),
    ("n4", NARRATOR, "And this was not the first time. Coming up on three seasons now he had walked out to that same tree expecting figs, and walked back with empty hands every time. A fig tree gets a fair trial, and this one had had a long one."),
    # Luke 13:7
    ("jv7", JESUS, "Then said he unto the dresser of his vineyard, Behold, these three years I come seeking fruit on this fig tree, and find none: cut it down; why cumbereth it the ground?"),
    ("n5", NARRATOR, "And you can hear that he is not being cruel. His last words are just plain sense. The tree is holding a place a fruitful one could be using, and any farmer in that crowd would have nodded. It was a fair call."),
    # Luke 13:8
    ("jv8", JESUS, "And he answering said unto him, Lord, let it alone this year also, till I shall dig about it, and dung it:"),
    ("n6", NARRATOR, "And then someone speaks up for the tree. The man who tends it. He does not argue that the owner is wrong. He just asks for one more year, and takes the tree's side when it cannot speak for itself."),
    ("n7", NARRATOR, "And look at what he offers to do with that year. Get down and break up the hard, packed earth around the roots, so the tree can finally breathe and drink. Not scold the tree. Work the soil."),
    ("n8", NARRATOR, "And then feed it. The lowest, messiest job on the whole farm, done by hand at the foot of a tree that has given him nothing back. He is not asking for time so he can wait and watch. He is asking for time so he can go to work."),
    # Luke 13:9
    ("jv9", JESUS, "And if it bear fruit, well: and if not, then after that thou shalt cut it down."),
    ("n9", NARRATOR, "And if it comes to life, wonderful. And if it does not, we will face that when it comes. But not today. The axe goes back against the wall, and the tree gets its year."),
    ("n10", NARRATOR, "Here is the part worth sitting with. The tree had not changed. It had not turned itself around or grown a single fig overnight. It got its extra year for one reason only. Someone who cared for it stood between it and the axe and asked."),
    ("n10b", NARRATOR, "That is the whole picture. Not a tree earning its keep. A gardener buying it time it could never have bought for itself."),
    ("n11", NARRATOR, "He never tells us who the gardener is. He does not have to. Everyone listening knew what it felt like to be the barren tree. And every one of them just heard that there is Someone in the vineyard whose first move is to ask for more time on your behalf."),
    ("n12", NARRATOR, "So the story he told to warn them turns out to be the story that saves them. The owner had every right to the axe. The gardener asked for the year. And the tree is still standing."),
    ("card", NARRATOR, "He told a story where the tree that had earned the axe got another year instead, because someone knelt down in the dirt and asked for it. What would you say to a Gardener like that?"),
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
