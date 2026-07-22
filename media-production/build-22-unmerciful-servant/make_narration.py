#!/usr/bin/env python3
"""Narration for build-22-unmerciful-servant — Matthew 18.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Matthew 18:21-35. Two different things are happening in this chapter and they
get two different colours.
PETER is a real man asking a real question in the frame of the story, not a character
inside the parable, so his line is SCRIPTURE (blue):
  s21  Matthew 18:21  'Lord, how oft shall my brother sin against me...'
EVERYTHING INSIDE THE PARABLE IS RED. A red-letter KJV inks the king, the servant and
the fellowservant, because those are Jesus's own words. j1 and j2 stay red and three
more parable lines are lifted out of paraphrase and join them:
  j3  Matthew 18:26     the servant begging the king
  j4  Matthew 18:28     'Pay me that thou owest.'
  j5  Matthew 18:32-33  'O thou wicked servant...'
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "One day Peter came to Jesus with a question that had been sitting heavy on his heart. It was about forgiveness — and about someone who kept hurting him."),
    # Matthew 18:21
    ("s21", SCRIPTURE, "Lord, how oft shall my brother sin against me, and I forgive him? till seven times?"),
    ("n1", NARRATOR, "Lord, he asked, how many times do I have to forgive my brother when he keeps sinning against me? Would seven times be enough? Peter must have thought he was being generous."),
    # Matthew 18:22
    ("j1", JESUS, "I say not unto thee, Until seven times: but, Until seventy times seven."),
    ("n2", NARRATOR, "In other words, stop counting. Real forgiveness doesn't keep a ledger. And then, to show them what he meant, Jesus told a story."),
    ("n3", NARRATOR, "There was once a king who decided to settle his accounts. One by one, his servants were brought in to answer for what they owed him."),
    ("n4", NARRATOR, "One man was dragged forward who owed the king ten thousand talents. It was a staggering fortune — more money than a working man could earn in ten thousand lifetimes. A debt like that could never, ever be repaid."),
    ("n5", NARRATOR, "The man had nothing to pay with. So the king ordered that he be sold — his wife, his children, everything he owned — to recover even a fraction of it."),
    ("n6", NARRATOR, "The servant threw himself down on the ground and begged. Please, he cried, be patient with me, and I will pay back everything!"),
    # Matthew 18:26
    ("j3", JESUS, "Lord, have patience with me, and I will pay thee all."),
    ("n7", NARRATOR, "And the king looked at this desperate man crumpled before him — and his heart broke with compassion. He did something no one expected."),
    ("n8", NARRATOR, "He didn't just give him more time. He cancelled the whole debt. Every last coin of that impossible fortune — forgiven, wiped away, gone. The man was free."),
    ("n9", NARRATOR, "But then that same servant walked outside. And there he found one of his fellow servants — a man who owed him a hundred silver coins. A few months' wages. Real money, yes — but nothing next to the ocean he'd just been forgiven."),
    ("n10", NARRATOR, "He grabbed the man by the throat and started to choke him. Pay me what you owe me! he snarled. Pay me now!"),
    # Matthew 18:28
    ("j4", JESUS, "Pay me that thou owest."),
    ("n11", NARRATOR, "His fellow servant fell down at his feet and begged him with the very same words he himself had used only moments before: Please, be patient with me, and I will pay you back!"),
    ("n12", NARRATOR, "But he refused. He would not listen. He had the man thrown into prison until he could pay back every penny."),
    ("n13", NARRATOR, "The other servants saw the whole thing, and it grieved them deeply. They went and told the king everything that had happened."),
    ("n14", NARRATOR, "The king summoned him back. You wicked servant! he said. I forgave you that enormous debt because you begged me to. Shouldn't you have shown the same mercy to your fellow servant that I showed to you?"),
    # Matthew 18:32-33
    ("j5", JESUS, "O thou wicked servant, I forgave thee all that debt, because thou desiredst me: Shouldest not thou also have had compassion on thy fellowservant, even as I had pity on thee?"),
    ("n15", NARRATOR, "And in his anger the king handed him over to be punished until he should pay back all that he owed. Then Jesus turned the story toward every one of us."),
    # Matthew 18:35
    ("j2", JESUS, "So likewise shall my heavenly Father do also unto you, if ye from your hearts forgive not every one his brother their trespasses."),
    ("n16", NARRATOR, "Here is the whole point of the story. Look at the two debts side by side. The mountain that was forgiven us, and the small handful we're asked to forgive each other. They aren't even close."),
    ("n17", NARRATOR, "We forgive the small things because of the mountain we've been forgiven. To be handed an ocean of mercy, and then choke someone over a cup of it — that is the one thing this King cannot bear."),
    ("card", NARRATOR, "You were forgiven a debt you could never repay. Who is holding a small one against you — that you could let go of today?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
# owest (KJV Matt 18:28, Cameron complaint #22 twice): the Eric voice reads
# "owest" as "our'st". A/B/C/D tested 2026-07-21: "owe est" renders OH-est —
# the correct sound (whisper spells it o'est). Caption keeps KJV "owest".
SPOKEN = {"owest": "owe est"}

# Cameron complaint #22: Eric reads plain "owest" as "Alice" and the earlier
# 'ohest' respell vanished in the mix. 'owesst' round-trips "owe-est" clean
# (A/B 2026-07-21, in-context, Eric voice). Do NOT drop this on rewrites —
# it was lost once already in a SPEAKER-LAW batch rewrite.
SPOKEN.update({"owest": "owesst"})


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
