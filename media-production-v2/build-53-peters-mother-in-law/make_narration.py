#!/usr/bin/env python3
"""Narration for build-53-peters-mother-in-law — Mark 1.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

NOBODY SPEAKS IN THIS STORY. Mark 1:29-31 is three verses long and contains no
direct speech at all -- not from Jesus, not from the disciples, not from the woman
it is about. Verse 30 says only 'anon they tell him of her'; it does not report
what they said. So there is no red in this build and there is nothing to lift into
red, and I did not invent a line to create some.

ADDED IN BLUE -- MARK'S OWN SENTENCE. Rather than leave the build with no
scripture in it anywhere, the healing verse itself is now spoken verbatim as
SCRIPTURE, light blue. Under the law, narration inside the Gospels is `scripture`
-- that is Mark writing:
  s31  Mark 1:31  'And he came and took her by the hand, and lifted her up; and
       immediately the fever left her, and she ministered unto them.'
It sits on S5, s5-took-her-by-the-hand, right after n5 which is already the frame
for it. n5 keeps its id and is trimmed by one clause so it hands off to the verse
instead of paraphrasing it first. The retelling was already written: n6 retells
the lifting and the fever, and n7 retells 'she ministered unto them.' Nothing new
was needed after it.

WOMEN -- AND THE HONEST ANSWER. This is a video about a woman, and I looked hard
for a line for her. Mark gives her none. Neither does Matthew 8:14-15. Luke 4:38-39
comes closest and still only says 'they besought him for her' -- the disciples,
not her, and not in direct speech. She is one of the women scripture records being
loved without recording anything she said. There is no pink in this build, and
putting words in her mouth to get some would break the one rule that matters most.
Flagging it plainly rather than quietly.

NO RED, NO GREEN. Neither is present in Mark 1:29-31.

RETELLING RULE: s31 is followed immediately by n6 and then n7, which between them
say the whole verse again in plain English.

WHY-LAW: they did not make a speech, they just told him what was wrong -- and the
first thing she did with her strength was spend it on other people. Milk: you do
not need the right words, only somewhere to put the trouble.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "When Jesus came out of the synagogue that sabbath, he did not go off alone. He went home with his friends, into the house of Simon and Andrew, and James and John went in with them."),
    ("n2", NARRATOR, "It was an ordinary house, the kind of place where real life happens. But that day the house was heavy, because someone they loved was ill."),
    ("n3", NARRATOR, "Simon's wife's mother lay in a back room, sick with a fever. In those days a fever like that could take a life, and there was little anyone could do but sit beside her and worry."),
    ("n4", NARRATOR, "So they told Jesus about her. They did not make a speech or a grand request; they simply brought their trouble to him, the way you tell a friend what is wrong."),
    ("n5", NARRATOR, "And he went in to where she was lying. What happened next, Mark tells in a single sentence."),
    # Mark 1:31
    ("s31", SCRIPTURE, "And he came and took her by the hand, and lifted her up; and immediately the fever left her, and she ministered unto them."),
    ("n6", NARRATOR, "No slow recovery, no days of weakness; the heat and the sickness were gone, and she was herself once more, well and strong."),
    ("n7", NARRATOR, "And the first thing she did was rise and serve them. With her strength fully back, she cared for the very ones who had carried her trouble to Jesus, glad to be on her feet again."),
    ("n8", NARRATOR, "It is a small, quiet miracle, tucked into an ordinary house. No crowd and no spectacle; only a tired family, a sickbed, and a Savior who came in, took her by the hand, and made her whole."),
    ("card", NARRATOR, "He still comes into ordinary houses and ordinary lives. You do not need the right words or a grand request; you only need to tell him where it hurts. What would it mean to simply put your trouble into his hand?"),
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
