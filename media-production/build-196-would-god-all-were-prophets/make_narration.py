#!/usr/bin/env python3
"""Narration for build-196-would-god-all-were-prophets — Numbers 11.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Numbers 11:28-29. The red beat moves to BLUE, and Joshua's line is lifted out.

  s1  Numbers 11:29  'Enviest thou me for my sake? would God that all...'  RED -> SCRIPTURE
  s0  Numbers 11:28  NEW - lifted out of narrator paraphrase               -> SCRIPTURE

This is the one in the set that looks like God speaking and is not. Checked the
surrounding verses: verse 28 is 'And Joshua the son of Nun, the servant of Moses,
one of his young men, answered and said, My lord Moses, forbid them.' Verse 29
opens 'And Moses said unto him' - so every word of s1 is MOSES. He is talking
ABOUT the LORD in the third person ('would God that all the LORD's people were
prophets, and that the LORD would put his spirit upon them'), which is the tell.
A man wishing God would do something is not God speaking. Light blue, not green.
Numbers is Old Testament so `jesus` was never available, but the trap here was
green, not red.

LIFT. n3b was paraphrasing Joshua - 'stop them, he said' - and the actual line is
four words long and better than the paraphrase. Numbers 11:28 is now `s0`,
verbatim and blue, on ST6, which is the still already named 'forbid them'. The
artwork was waiting for it.

QUESTION AND ANSWER - no retelling between s0 and s1, on purpose. Joshua asks
Moses to shut it down; Moses answers him. Putting a narrator retelling between
those two lines would break the only exchange in the story and kill the beat the
whole video is built on. The law's exception for a deliberate question-and-answer
pair covers exactly this. The meaning is not left hanging either way: n3b sits
immediately BEFORE s0 and already gives Joshua's sense in modern English, and n4
retells Moses right after. So both Old English lines are surrounded by plain
English, just not sandwiched individually.

Verbatim: s0 is 'My lord Moses, forbid them.' word for word. s1 is Numbers 11:29
from 'Enviest thou me' to the closing exclamation, exact, including the
possessive in 'the LORD's people'. Neither was smoothed.

n0, n1a and n1b stay narrator paraphrase and I am leaving them that way on
purpose. They compress the LORD's instructions from Numbers 11:16-17 into three
sentences. The real verses run long and are full of tabernacle logistics, and
lifting them would put a third Old English block into a short video and bury the
punchline. Said plainly: those beats are paraphrase, not quotation, and are
correctly white.

Ids: every original id kept. s0 is the only new one. The card is 'card' and stays
out of beats, as the original had it.

WHY-LAW: milk. Moses did not guard the gift. The most generous answer in the Old
Testament is a leader wishing everyone had what he had - no argument about
authority, just the wish itself.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "The weight of leading a whole nation was crushing Moses. He told the LORD he could not carry the people alone, not one more day."),
    ("n1a", NARRATOR, "So God told Moses to gather seventy trusted men."),
    ("n1b", NARRATOR, "He would take some of the Spirit that rested on Moses and share it with them, and together they would help bear the load."),
    ("n2", NARRATOR, "When the Spirit came down on those seventy, they began to speak God's words. But two men, Eldad and Medad, had stayed back in the camp — and the Spirit came on them too, right there among the tents."),
    ("n3a", NARRATOR, "A runner hurried to Moses with the news."),
    ("n3b", NARRATOR, "Joshua, Moses's right-hand man, was worried — stop them, he said. That is not how it is supposed to work."),
    # Numbers 11:28
    ("s0", SCRIPTURE, "My lord Moses, forbid them."),
    # Numbers 11:29
    ("s1", SCRIPTURE, "Enviest thou me for my sake? would God that all the LORD's people were prophets, and that the LORD would put his spirit upon them!"),
    ("n4", NARRATOR, "One of the most generous answers in all of scripture. Moses did not guard the gift — he wished it wider."),
    ("card", NARRATOR, "Moses did not guard the gift — he wished it for everyone. The same Spirit is offered to you. Ask, and receive."),
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
