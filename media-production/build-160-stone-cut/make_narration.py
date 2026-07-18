#!/usr/bin/env python3
"""Generate narration audio for Story Video #160 — "The stone cut without hands"
(Daniel 2:44-45). MEMBER shelf verse-video. → Gospel Library topic: Kingdom of God.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY.
(Daniel is Old-Testament prophecy; the scripture voice carries the verse. Christ is NOT
depicted; God's kingdom is shown only as light. The dream statue is a VISION, never an
idol worshipped.)

KJV lines (exact):
  kv45 = Dan 2:45  the stone cut out of the mountain without hands (SACRED SILENCE 1)
  kv44 = Dan 2:44  God shall set up a kingdom... it shall stand for ever (NAMED VERSE — SACRED SILENCE 2)

WHY-LAW: hope and permanence — the kingdoms of men rise and fall, but God's kingdom is
unstoppable and forever, not built or torn down by human hands. STUDY GEMS: the stone is
cut by no human hand (n3); it shatters every empire and blows away like chaff (n4); it
grows to fill the whole earth (n5); never destroyed, never handed off (n7).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n3 says "cut by no human hand,"
delivered as paraphrase; the exact KJV lands only in kv45/kv44.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Kingdom of God). No shame, no fear.
CHRIST IS NEVER DEPICTED; the kingdom is shown only as warm light.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The king of Babylon had a dream that troubled him deeply, and none of his wise "
     "men could tell him what it meant. So a young exile named Daniel, who served the "
     "God of heaven, was brought in to explain it."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "In the dream, the king had seen an enormous statue, dazzling and terrible — a head "
     "of gold, chest of silver, belly of bronze, legs of iron, and feet of iron mixed "
     "with crumbling clay. It stood for the great kingdoms of the world, one after "
     "another."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And then, in the dream, something small appeared. A single stone, cut out of a "
     "mountain — but cut by no human hand. No chisel, no workman, no army. It simply "
     "broke free, all on its own."),
    # kv45 — SACRED SILENCE 1
    ("kv45", SCRIPTURE, "-26%", "-6Hz",
     "Forasmuch as thou sawest that the stone was cut out of the mountain without hands, "
     "and that it brake in pieces the iron, the brass, the clay, the silver, and the "
     "gold; the great God hath made known to the king what shall come to pass hereafter: "
     "and the dream is certain, and the interpretation thereof sure."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "That little stone, made by God and not by men, struck the great statue at its feet "
     "— and the whole towering thing came crashing down, shattered to dust, and blew "
     "away on the wind like chaff, until not a trace was left."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "But the stone did not stop. It began to grow. It became a mountain, and then a "
     "greater mountain, until it filled the whole earth, from one end of it to the "
     "other."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Daniel told the king what it meant. Every human empire, however golden, would rise "
     "and then fall and be forgotten. But God himself would set up a kingdom of his own, "
     "and that one would be different."),
    # kv44 — NAMED VERSE, SACRED SILENCE 2
    ("kv44", SCRIPTURE, "-26%", "-6Hz",
     "And in the days of these kings shall the God of heaven set up a kingdom, which "
     "shall never be destroyed: and the kingdom shall not be left to other people, but "
     "it shall break in pieces and consume all these kingdoms, and it shall stand for "
     "ever."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Never destroyed. Never handed off to someone else. Not built by human hands, and "
     "so not able to be torn down by them either — a kingdom cut from the mountain of "
     "God, that would outlast every throne on earth and stand forever."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "So this ancient dream is really a promise you can build your life on. The kingdoms "
     "of men come and go, but God is setting up one that never ends — a stone that fills "
     "the whole earth. So the only question is a hopeful one. When that kingdom is "
     "offered to you, will you belong to it?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "God showed a king a stone cut without hands that shattered every empire and grew to "
     "fill the earth — his own kingdom, that shall never be destroyed and shall stand for "
     "ever. When it is offered to you, will you belong to it?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
