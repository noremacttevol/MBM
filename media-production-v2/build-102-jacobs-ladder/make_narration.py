#!/usr/bin/env python3
"""Narration for build-102-jacobs-ladder — Genesis 28.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both red beats are Jehovah speaking to Jacob in a dream. Genesis is Old
Testament, so neither can be red — both are GOD (green):
  jv13  Genesis 28:13  'I am the LORD God of Abraham thy father...'
  jv15  Genesis 28:15  'And, behold, I am with thee, and will keep thee...'

ON THE BRIEFING NOTE ABOUT n6: the note asked me to lift 'I am with thee. I will
keep thee. I will not leave thee' out of n6 as a verbatim GOD beat. That lift has
already been done in this build — jv15 is the full verbatim Genesis 28:15 and it
runs immediately BEFORE n6. n6 is not burying the verse; it is the mandated
narrator retelling of the verse the viewer just heard. Adding a second God beat
would say the same words twice in a row. So n6 stays narrator, unchanged. The
example in SPEAKER-LAW.md section 4 appears to describe an older cut of 102.

LIFTED FROM PARAPHRASE: Jacob's own words were the real gap. n7 paraphrased
Genesis 28:16-17 in modern English. Jacob now speaks it himself as the new s16
(SCRIPTURE, light blue), with n7 unchanged after it as the retelling. The text is
the two direct-speech halves of 16 and 17, with the writer's frame ('And he was
afraid, and said') left out — every word a viewer can look up.

NO WOMEN: Genesis 28 records no woman speaking. Rebekah's speech is chapter 27
and is outside this video.

WHY-LAW: God comes to a liar on the run, before he repents, and promises to stay.
Milk framing — heaven is open over the person who thinks he has disqualified
himself.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, 'Jacob was running. He had lied to his blind father and cheated his own brother, and now he was fleeing for his life, alone, with everything he knew behind him.'),
    ("n2", NARRATOR, 'When the sun went down he was in the middle of nowhere. No home, no bed, no welcome. He took a stone, put it under his head for a pillow, and lay down in the dark to sleep.'),
    ("n3", NARRATOR, 'And there, in the last place he would have expected it, God came to him in a dream. He saw a great stairway rising from the very ground where he lay, all the way up into an opening in heaven.'),
    ("n4", NARRATOR, 'And on it the angels of God were going up and coming down, moving between heaven and this lonely patch of dirt where a runaway lay sleeping. Heaven was not far off. It was open, right above him.'),
    ("jv13", GOD, 'I am the LORD God of Abraham thy father, and the God of Isaac: the land whereon thou liest, to thee will I give it, and to thy seed.'),
    ("n5", NARRATOR, 'God did not scold him for what he had done. He stood above the stairway and made him a promise — the same promise he had made to his grandfather Abraham. This wanderer with nothing would become a family as many as the dust of the earth.'),
    ("jv15", GOD, 'And, behold, I am with thee, and will keep thee in all places whither thou goest, and will bring thee again into this land; for I will not leave thee, until I have done that which I have spoken to thee of.'),
    ("n6", NARRATOR, 'I am with thee. I will keep thee. I will not leave thee. To a man who had just thrown his whole life away and run, God promised to go with him, everywhere, and never let go. He had done nothing to earn it.'),
    ("s16", SCRIPTURE, 'Surely the LORD is in this place; and I knew it not. How dreadful is this place! this is none other but the house of God, and this is the gate of heaven.'),
    ("n7", NARRATOR, 'Jacob woke with a start, shaken to his core. This is nothing less than the house of God. This is the gate of heaven — and I nearly slept through it.'),
    ("n8", NARRATOR, 'So he took the stone that had been his pillow and stood it up on end as a pillar, a marker of the place where heaven had opened over him.'),
    ("n8b", NARRATOR, 'And he poured oil over the top of it to set it apart as holy, and he called that place Bethel — the house of God.'),
    ("n9", NARRATOR, 'Then he went on his way — the same road, the same troubles waiting ahead, but a different man. Not because he had fixed himself, but because he finally knew he was not walking alone. That is how God still meets people: not at their best, but wherever they happen to lie down in the dark.'),
    ("card", NARRATOR, 'God met a runaway with a rock for a pillow, and promised to go with him and never leave. If heaven is that near even to the one who ran, what might God be wanting to say to you, right where you are?'),
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
