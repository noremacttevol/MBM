#!/usr/bin/env python3
"""Narration for build-160-stone-cut — Daniel 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both red beats become BLUE, and this build ends up with no green at all — which is the correct reading, and worth stating plainly because it looks surprising next to the other prophet builds.

  kv45  Daniel 2:45  scripture (was red)
  kv44  Daniel 2:44  scripture (was red)

Daniel 2:44-45 is Daniel standing in front of Nebuchadnezzar explaining the dream. God is the SUBJECT of both verses — 'the God of heaven shall set up a kingdom', 'the great God hath made known to the king' — but he is spoken ABOUT, in the third person, the entire way through. Nowhere does Deity speak in first person in this passage. So it is the man talking: SCRIPTURE, light blue. Painting it green would be as wrong as leaving it red, just less obviously so.

Nothing is split — neither verse changes speaker at any point.

Beat order keeps kv45 before kv44 exactly as the build has it. That is out of verse order on purpose: the stone striking comes before the kingdom standing forever, which is the order the story wants. Left alone.

Both lines already have narrator retellings after them (n4, n7).

WHY-LAW: a kingdom not built by human hands cannot be torn down by them either. Every empire in the dream is gold and iron and gone. The stone was the small thing in the picture and it ends up filling the earth.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "The king of Babylon had a dream that troubled him deeply, and none of his wise men could tell him what it meant. So a young exile named Daniel, who served the God of heaven, was brought in to explain it."),
    ("n2", NARRATOR, "In the dream, the king had seen an enormous statue, dazzling and terrible — a head of gold, chest of silver, belly of bronze, legs of iron, and feet of iron mixed with crumbling clay. It stood for the great kingdoms of the world, one after another."),
    ("n3", NARRATOR, "And then, in the dream, something small appeared. A single stone, cut out of a mountain — but cut by no human hand. No chisel, no workman, no army. It simply broke free, all on its own."),
    # Daniel 2:45
    ("kv45", SCRIPTURE, "Forasmuch as thou sawest that the stone was cut out of the mountain without hands, and that it brake in pieces the iron, the brass, the clay, the silver, and the gold; the great God hath made known to the king what shall come to pass hereafter: and the dream is certain, and the interpretation thereof sure."),
    ("n4", NARRATOR, "That little stone, made by God and not by men, struck the great statue at its feet — and the whole towering thing came crashing down, shattered to dust, and blew away on the wind like chaff, until not a trace was left."),
    ("n5", NARRATOR, "But the stone did not stop. It began to grow. It became a mountain, and then a greater mountain, until it filled the whole earth, from one end of it to the other."),
    ("n6", NARRATOR, "Daniel told the king what it meant. Every human empire, however golden, would rise and then fall and be forgotten. But God himself would set up a kingdom of his own, and that one would be different."),
    # Daniel 2:44
    ("kv44", SCRIPTURE, "And in the days of these kings shall the God of heaven set up a kingdom, which shall never be destroyed: and the kingdom shall not be left to other people, but it shall break in pieces and consume all these kingdoms, and it shall stand for ever."),
    ("n7", NARRATOR, "Never handed off to someone else. Not built by human hands, and so not able to be torn down by them either — a kingdom cut from the mountain of God, that would outlast every throne on earth and stand forever."),
    ("n8", NARRATOR, "So this ancient dream is really a promise you can build your life on. The kingdoms of men come and go, but God is setting up one that never ends — a stone that fills the whole earth. So the only question is a hopeful one. When that kingdom is offered to you, will you belong to it?"),
    ("card", NARRATOR, "God showed a king a stone cut without hands that shattered every empire and grew to fill the earth — his own kingdom, that shall never be destroyed and shall stand for ever. When it is offered to you, will you belong to it?"),
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
