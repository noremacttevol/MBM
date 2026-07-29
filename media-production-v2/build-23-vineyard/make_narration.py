#!/usr/bin/env python3
"""Narration for build-23-vineyard — Matthew 20.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both existing red beats are Jesus in the flesh telling a parable, and
a red-letter KJV prints the whole parable red -- the householder's speech in j1
is Jesus's words in a character's mouth, so it stays RED, not blue.
  j1  Matthew 20:13-15  'Friend, I do thee no wrong: didst not thou agree with me
      for a penny?...'
  j2  Matthew 20:16     'So the last shall be first, and the first last: for many
      be called, but few chosen.'
Neither carried Matthew's framing, so neither needed splitting.

ADDED RED, ALL OF IT INSIDE THE PARABLE. Four exchanges were told only in
narrator paraphrase, and every one of them is red-letter -- including the
labourers' own lines, which are still Jesus speaking:
  j6   Matthew 20:6   'Why stand ye here all the day idle?'          (householder)
  j7a  Matthew 20:7   'Because no man hath hired us.'                (the labourers -- RED)
  j7b  Matthew 20:7   'Go ye also into the vineyard; and whatsoever is right, that
                       shall ye receive.'                            (householder)
  j12  Matthew 20:12  'These last have wrought but one hour, and thou hast made
                       them equal unto us, which have borne the burden and heat of
                       the day.'                                     (the murmurers -- RED)
j6 and j7a are a deliberate question-and-answer pair on the SAME still S3, with
n5b retelling both together straight after. j12 goes on the SAME still S6 that
already carried the grumbling.

TRIMS, so nothing is said twice: n5 loses its last sentence (now j6), n6 loses
its first sentence (now j7a) and is rewritten as the retelling of j7b, and n10
loses its last sentence (now j12) with n10b carrying that retelling. No original
id was dropped or renamed.

Hearing the labourers say 'no man hath hired us' in their own voice is the
turnaround of the whole video -- they were not lazy, they were never picked.

WOMEN: Matthew 20:1-16 records no woman speaking. Nothing added; nothing invented.

NO GREEN: no voice from heaven in Matthew 20:1-16.

WHY-LAW: the first men were not underpaid, they got everything they agreed to.
What stung was watching somebody else get grace they had not earned.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, 'Jesus said the kingdom of heaven is like a landowner who went out at first light to hire workers for his vineyard.'),
    ("n2", NARRATOR, "He agreed with the first crew on a penny for the day — a full day's fair wage — and sent them out into the rows."),
    ("n3", NARRATOR, 'A few hours later he went back to the market and found more men just standing around with no work. He sent them into the vineyard too, and promised to pay them what was right.'),
    ("n4", NARRATOR, 'He did the same thing again at noon, and again in the middle of the afternoon. More workers, the same promise.'),
    ("n5", NARRATOR, 'Then, with only one hour of daylight left, he went out a final time and found still more men standing idle.'),
    ("j6", JESUS, 'Why stand ye here all the day idle?'),
    ("j7a", JESUS, 'Because no man hath hired us.'),
    ("n5b", NARRATOR, 'The question revealed the wound: they had not refused work. Nobody had chosen them.'),
    ("j7b", JESUS, 'Go ye also into the vineyard; and whatsoever is right, that shall ye receive.'),
    ("n6", NARRATOR, 'Even with one hour of daylight left, the owner was still looking for people others had passed over.'),
    ("n7", NARRATOR, 'When evening came, the owner told his foreman to call the workers and pay them — starting, strangely, with the ones hired last.'),
    ("n8", NARRATOR, "The men who had worked a single hour came up first, and each of them was handed a full day's pay. A whole penny, for one hour of work."),
    ("n9", NARRATOR, 'You can guess what the men who had worked since dawn were thinking. If the one-hour crew got a full penny, surely they would get more.'),
    ("n10", NARRATOR, 'But when their turn came, they got the very same — one penny. And they were furious.'),
    ("j12", JESUS, 'These last have wrought but one hour, and thou hast made them equal unto us, which have borne the burden and heat of the day.'),
    ("n10b", NARRATOR, 'Their anger was not about a broken agreement. It was about being treated no better than men they considered less deserving.'),
    ("n11", NARRATOR, 'The owner turned to one of them, and he was not harsh about it. He called him friend.'),
    ("j1", JESUS, 'Friend, I do thee no wrong: didst not thou agree with me for a penny? Take that thine is, and go thy way: I will give unto the last, even as unto thee. Is it not lawful for me to do what I will with mine own? Is thine eye evil, because I am good?'),
    ("n12", NARRATOR, "The owner's answer exposed the real grievance: generosity to the latecomers felt like theft to those who had arrived early."),
    ("n13", NARRATOR, 'That is the whole point. The first men were not underpaid. They got everything they were promised. What stung was watching someone else receive grace they had not earned.'),
    ("j2", JESUS, 'So the last shall be first, and the first last: for many be called, but few chosen.'),
    ("n14", NARRATOR, "God does not run low on generosity when he spends it on someone who came late. His goodness is never used up. There is a full day's welcome waiting for you, no matter what hour you finally come in."),
    ("card", NARRATOR, 'You have not missed your chance by coming late. Will you come into the vineyard now?'),
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
