#!/usr/bin/env python3
"""Narration for Story Video #22 — The Unmerciful Servant (Matthew 18:21-35).
Two-Voice Law: Andrew narrates (plain American, NEVER Multilingual); Christopher
speaks ONLY the exact KJV Jesus lines. Translation Law: the narrator paraphrases
Jesus's spoken lines in modern English and never echoes their KJV wording; the
characters' words (servants, king) may be quoted modernly."""
import asyncio, edge_tts, os

NARRATOR = "en-US-AndrewNeural"        # plain American, NEVER Multilingual
JESUS    = "en-US-ChristopherNeural"   # American, never British

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0",  NARRATOR, "-18%", "-4Hz",
     "One day Peter came to Jesus with a question that had been sitting heavy on his heart. "
     "It was about forgiveness — and about someone who kept hurting him."),
    ("n1",  NARRATOR, "-18%", "-4Hz",
     "Lord, he asked, how many times do I have to forgive my brother when he keeps sinning against me? "
     "Would seven times be enough? Peter must have thought he was being generous."),
    ("j1",  JESUS,    "-24%", "-6Hz",
     "I say not unto thee, Until seven times: but, Until seventy times seven."),
    ("n2",  NARRATOR, "-18%", "-4Hz",
     "In other words, stop counting. Real forgiveness doesn't keep a ledger. "
     "And then, to show them what he meant, Jesus told a story."),
    ("n3",  NARRATOR, "-18%", "-4Hz",
     "There was once a king who decided to settle his accounts. "
     "One by one, his servants were brought in to answer for what they owed him."),
    ("n4",  NARRATOR, "-18%", "-4Hz",
     "One man was dragged forward who owed the king ten thousand talents. "
     "It was a staggering fortune — more money than a working man could earn in ten thousand lifetimes. "
     "A debt like that could never, ever be repaid."),
    ("n5",  NARRATOR, "-18%", "-4Hz",
     "The man had nothing to pay with. So the king ordered that he be sold — "
     "his wife, his children, everything he owned — to recover even a fraction of it."),
    ("n6",  NARRATOR, "-18%", "-4Hz",
     "The servant threw himself down on the ground and begged. "
     "Please, he cried, be patient with me, and I will pay back everything!"),
    ("n7",  NARRATOR, "-18%", "-4Hz",
     "And the king looked at this desperate man crumpled before him — and his heart broke with compassion. "
     "He did something no one expected."),
    ("n8",  NARRATOR, "-18%", "-4Hz",
     "He didn't just give him more time. He cancelled the whole debt. "
     "Every last coin of that impossible fortune — forgiven, wiped away, gone. The man was free."),
    ("n9",  NARRATOR, "-18%", "-4Hz",
     "But then that same servant walked outside. "
     "And there he found one of his fellow servants — a man who owed him a hundred silver coins. "
     "A few months' wages. Real money, yes — but nothing next to the ocean he'd just been forgiven."),
    ("n10", NARRATOR, "-18%", "-4Hz",
     "He grabbed the man by the throat and started to choke him. "
     "Pay me what you owe me! he snarled. Pay me now!"),
    ("n11", NARRATOR, "-18%", "-4Hz",
     "His fellow servant fell down at his feet and begged him with the very same words he himself had used only moments before: "
     "Please, be patient with me, and I will pay you back!"),
    ("n12", NARRATOR, "-18%", "-4Hz",
     "But he refused. He would not listen. "
     "He had the man thrown into prison until he could pay back every penny."),
    ("n13", NARRATOR, "-18%", "-4Hz",
     "The other servants saw the whole thing, and it grieved them deeply. "
     "They went and told the king everything that had happened."),
    ("n14", NARRATOR, "-18%", "-4Hz",
     "The king summoned him back. You wicked servant! he said. "
     "I forgave you that enormous debt because you begged me to. "
     "Shouldn't you have shown the same mercy to your fellow servant that I showed to you?"),
    ("n15", NARRATOR, "-18%", "-4Hz",
     "And in his anger the king handed him over to be punished until he should pay back all that he owed. "
     "Then Jesus turned the story toward every one of us."),
    ("j2",  JESUS,    "-24%", "-6Hz",
     "So likewise shall my heavenly Father do also unto you, if ye from your hearts forgive "
     "not every one his brother their trespasses."),
    ("n16", NARRATOR, "-18%", "-4Hz",
     "Here is the whole point of the story. Look at the two debts side by side. "
     "The mountain that was forgiven us, and the small handful we're asked to forgive each other. "
     "They aren't even close."),
    ("n17", NARRATOR, "-18%", "-4Hz",
     "We forgive the small things because of the mountain we've been forgiven. "
     "To be handed an ocean of mercy, and then choke someone over a cup of it — that is the one thing this King cannot bear."),
    ("card", NARRATOR, "-18%", "-4Hz",
     "You were forgiven a debt you could never repay. "
     "Who is holding a small one against you — that you could let go of today?"),
]

async def main():
    os.makedirs("audio", exist_ok=True)
    for name, voice, rate, pitch, text in SEGMENTS:
        await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(f"audio/{name}.mp3")
        print("saved", name)

asyncio.run(main())
