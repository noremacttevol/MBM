#!/usr/bin/env python3
"""Narration for build-36-shrewd-steward — Luke 16.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both existing red beats are Jesus in the flesh closing out his own
parable, and a red-letter KJV prints both.
  j1  Luke 16:8  'And the lord commended the unjust steward, because he had done
      wisely: for the children of this world are in their generation wiser than the
      children of light.'
  j2  Luke 16:9  'And I say unto you, Make to yourselves friends of the mammon of
      unrighteousness; that, when ye fail, they may receive you into everlasting
      habitations.'
Both verified verbatim. j1 is worth stating plainly because it is the trap in this
build: 'the lord' in 16:8 is the master INSIDE the parable, not the Lord Jesus -- but
that changes nothing, because the whole parable is Jesus speaking and a red-letter KJV
inks the entire block red. It is not `scripture`. It stays red.

THE FRAMING SPLIT. Luke 16:1 reads in full: 'And he said also unto his disciples, There
was a certain rich man, which had a steward; and the same was accused unto him that he
had wasted his goods.' The opening clause is LUKE writing and a red-letter KJV leaves it
black; the rest is Jesus. Split properly, BOTH HALVES ON THE SAME STILL S1 -- no new
artwork:
  s1  Luke 16:1  'And he said also unto his disciples,'   SCRIPTURE, light blue.
  j0  Luke 16:1  'There was a certain rich man, which had a steward; and the same was
      accused unto him that he had wasted his goods.'   JESUS, red.
n1 keeps its id and its text word for word and now lands directly behind them as the
retelling -- it already read as one.

ADDED RED, ALL INSIDE THE PARABLE. Three of Jesus's own lines were told only in
paraphrase. All three are dialogue he puts in a character's mouth, which is still red:
  j3   Luke 16:3   'What shall I do? for my lord taketh away from me the stewardship: I
       cannot dig; to beg I am ashamed.'   -- the steward's panic. n3 retells it.
  j6   Luke 16:6   'Take thy bill, and sit down quickly, and write fifty.'   -- the line
       SPEAKER-LAW names for this build. n5 keeps its text and retells it.
  j13  Luke 16:13  'No servant can serve two masters: for either he will hate the one,
       and love the other; or else he will hold to the one, and despise the other. Ye
       cannot serve God and mammon.'   -- this is the payoff of the whole video and it
       was living entirely inside n9's modern paraphrase. Lifted onto S8 ahead of n9,
       which now retells it. Biggest single upgrade in this build.
Red now lands on S1, S2, S4, S6, S7 and S8, with a narrator retelling behind every one.

LEFT AS PARAPHRASE ON PURPOSE. Luke 16:7, 'Take thy bill, and write fourscore', is red
and verbatim and is deliberately NOT lifted. It sits one still after j6 and is nearly
the same sentence; running both would read as a stutter rather than a rhythm. n6 carries
it, and the pattern is already established by j6 the beat before.

NOT ADDED. Luke 16:14 -- 'And the Pharisees also, who were covetous, heard all these
things: and they derided him' -- is Luke narrating from OUTSIDE the parable and would be
`scripture`, light blue, not red. It is not in this build and it is not added: the video
ends on an invitation, and importing the deriding Pharisees would sour that close for no
gain. Recorded here so the judgement is on the record rather than an oversight.

NO GREEN: no voice from heaven in Luke 16:1-13. 'Ye cannot serve God and mammon' is
Christ in the flesh speaking ABOUT God, which is red, not green.

WOMEN: Luke 16:1-13 records no woman speaking. Nothing added; nothing invented.

PRONUNCIATION: `spoken` is left empty. Nothing in the KJV lines is on the homograph
list. 'mammon', 'fourscore' and 'habitations' all read correctly as written, and a bad
respelling is worse than none.

WHY-LAW: he is not praising the cheating, he is pointing at the urgency. He is not after
your money -- he is after you, and he wants your hands open while you still have time.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("s1", SCRIPTURE, 'And he said also unto his disciples,'),
    ("j0", JESUS, 'There was a certain rich man, which had a steward; and the same was accused unto him that he had wasted his goods.'),
    ("n1", NARRATOR, 'Jesus told a story about a rich man and the manager who ran everything he owned. Word came to the rich man that this manager had been wasting his goods.'),
    ("n2", NARRATOR, 'So he called the manager in and said, give an account of your work, because you cannot be my manager any longer. Just like that, the man was about to lose his job and his home.'),
    ("j3", JESUS, 'What shall I do? for my lord taketh away from me the stewardship: I cannot dig; to beg I am ashamed.'),
    ("n3", NARRATOR, 'And the manager panicked. I am not strong enough to dig ditches, he thought, and I am too ashamed to beg. He had to think fast, and he had to act right now, before the news got out.'),
    ("n4", NARRATOR, 'So while he still could, he quickly called in every person who owed his employer money, one after another, to make himself some friends before it was too late. How much do you owe? he asked the first man. A hundred jugs of olive oil.'),
    ("j6", JESUS, 'Take thy bill, and sit down quickly, and write fifty.'),
    ("n5", NARRATOR, 'And the farmer could hardly believe it.'),
    ("n6", NARRATOR, 'And you? A hundred measures of wheat. Take your bill, he said, and write down eighty. One after another he made friends who would remember him and take him in when he had nothing.'),
    ("j1", JESUS, 'And the lord commended the unjust steward, because he had done wisely: for the children of this world are in their generation wiser than the children of light.'),
    ("n7", NARRATOR, 'Even his employer had to admire it. And here is the strange point Jesus was making. He was not praising the cheating. He was pointing at the urgency. Worldly people are so clever, so quick, about money and their own future.'),
    ("j2", JESUS, 'And I say unto you, Make to yourselves friends of the mammon of unrighteousness; that, when ye fail, they may receive you into everlasting habitations.'),
    ("n8", NARRATOR, 'Use your money, he said, use your things, use whatever you have, to love people now. Those friendships are the one thing you carry with you past the end of your life. Be that urgent about what actually lasts.'),
    ("j13", JESUS, 'No servant can serve two masters: for either he will hate the one, and love the other; or else he will hold to the one, and despise the other. Ye cannot serve God and mammon.'),
    ("n9", NARRATOR, 'Then he said the line that ties it all together. You will end up loving one and despising the other. And money is a hard, hungry thing to serve.'),
    ("n10", NARRATOR, 'That is how good he is. He is not after your money. He is after you. He wants your heart free of that cruel little master and your hands open, so that you spend your one short life being urgent about the things that last forever.'),
    ("card", NARRATOR, 'He is not after your money. He is after you. What are you being urgent about?'),
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
