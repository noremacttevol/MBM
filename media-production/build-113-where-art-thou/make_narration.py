#!/usr/bin/env python3
"""Narration for build-113-where-art-thou — Genesis 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

One red beat, and Genesis is Old Testament, so it cannot be red:
  jv9  Genesis 3:9  'Where art thou?'  — Jehovah in the garden. GOD, green.

LIFTED FROM PARAPHRASE:
  s10  Genesis 3:10  Adam   'I heard thy voice in the garden, and I was afraid,
                             because I was naked; and I hid myself.'  SCRIPTURE
  jv13 Genesis 3:13  Jehovah 'What is this that thou hast done?'  GOD
  w13  Genesis 3:13  Eve    'The serpent beguiled me, and I did eat.'  WOMAN

THE WOMAN: Eve is the first woman the Bible records speaking to God, and her
answer was sitting unspoken in this build. Genesis 3:13 is short, verbatim, and
pink, and it makes the exchange a real conversation instead of a monologue. Her
line follows God's question on the same still, so the picture is unchanged.

EDITS TO EXISTING NARRATOR TEXT: n5 lost its trailing paraphrase of Adam's answer
('I heard you, and I was afraid, and I hid myself') because s10 now speaks it
verbatim; n5 ends on 'And, trembling, the man answered' and hands straight to
Adam. n5b is a new retelling of s10. n6 gains one opening sentence retelling
Eve, then continues word for word as before. Nothing else changed.

NOT MARKED AS SCRIPTURE: n1 through n4 and n7 through n9 stay narrator. They
describe the garden and the clothing of Genesis 3:21 in modern English rather
than quoting it, which is correct — they are the storyteller, not the text.

WHY-LAW: God's first recorded words to a person who has failed him are not an
accusation but a search, and the chapter ends with him making them clothes.
Milk framing — God comes looking, and covers what we cannot cover.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "In the beginning there was a garden, and in the garden, peace. People and God walking together in the cool of the day, with nothing to hide and nothing to fear."),
    ("n2", NARRATOR, "There was only one thing they were asked not to do. And, as people do, they did it anyway — reaching for the one thing that was not theirs, hoping it would make them more than they were."),
    ("n3", NARRATOR, "And everything changed. For the first time they felt shame. They saw themselves, and did not like what they saw, and scrambled to cover up, hiding from each other."),
    ("n4", NARRATOR, "And then they heard him coming — the warm presence of God moving through the garden in the cool of the evening, the way he always had. And this time, they ran and hid themselves among the trees."),
    # Genesis 3:9
    ("jv9", GOD, "Where art thou?"),
    ("n5", NARRATOR, "Where are you. Not, what have you done. Not, how dare you. Where are you — the cry of a Father looking for a child who is hiding. He knew exactly where they were. He asked so they would come out. And, trembling, the man answered."),
    # Genesis 3:10
    ("s10", SCRIPTURE, "I heard thy voice in the garden, and I was afraid, because I was naked; and I hid myself."),
    ("n5b", NARRATOR, "I heard you, and I was afraid, and I hid. That is the whole of it. Not defiance — fear. Shame has never once made a person run toward God. It makes them run behind a tree."),
    # Genesis 3:13
    ("jv13", GOD, "What is this that thou hast done?"),
    # Genesis 3:13
    ("w13", WOMAN, "The serpent beguiled me, and I did eat."),
    ("n6", NARRATOR, "I was deceived, she said, and I ate. No excuses left — just the truth, spoken out loud at last. There were consequences; there always are. The easy garden was behind them now, and a hard world lay ahead. They stood there, ashamed, waiting for the end of everything."),
    ("n7", NARRATOR, "And instead, God did something they never expected. He made them clothes. With his own care he covered their shame — better coverings than the leaves they had grabbed for themselves — because they could not fix what they had broken, and he would not leave them exposed."),
    ("n8", NARRATOR, "Then he sent them out into the wide world — but not naked, and not alone, and not without a promise. Clothed by the very One they had run from."),
    ("n9", NARRATOR, "That is the God of the very first story. Not one who waits for you to clean yourself up and come find him. One who comes walking through the garden in the cool of the evening, calling, still calling — where are you? — because he wants you back."),
    ("card", NARRATOR, "The first thing God said to hiding people was not a scolding — it was, where are you? He still comes seeking, and still covers the shame we cannot cover ourselves. Where are you hiding, that he is gently calling you out of?"),
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
