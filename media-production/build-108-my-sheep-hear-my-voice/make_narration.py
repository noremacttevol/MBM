#!/usr/bin/env python3
"""Narration audio for Video #108 — My Sheep Hear My Voice (John 10).

Narrator: en-US-AndrewNeural. Jesus: en-US-ChristopherNeural (exact KJV only).

Jesus's KJV lines (Christopher, cream italic):
  jv27  John 10:27  "My sheep hear my voice, and I know them, and they follow me:" — silence 1
  jv28  John 10:28  "And I give unto them eternal life; and they shall never perish,
                     neither shall any man pluck them out of my hand." — silence 2

WHY-LAW: a shepherd in that world did not drive his sheep from behind with a whip — he
walked ahead and they followed his voice, because they knew him and trusted him. Jesus
says that is what he is to his people: not a driver, but a voice they come to know; and
once they are in his hand, nothing and no one can tear them out. Milk framing: you are
known by name, led not driven, and held so securely that nothing can snatch you away. An
invitation, never a threat.

HOMOGRAPH EAR-CHECK: no high-risk homographs. NUMBER-STRESS LAW obeyed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "In that world, a shepherd did not drive his sheep from behind. He walked out in "
     "front of them, and they followed — not because they were forced, but because they "
     "knew his voice.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Several flocks might share one fold overnight. But in the morning, when a shepherd "
     "called, only his own sheep lifted their heads and came. They could tell his voice "
     "from a stranger's. That is the picture Jesus reaches for.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "He knows them one at a time. Not a nameless herd — each one, called by its own "
     "name, gently, personally. And knowing his voice, they come to him and follow.", None),
    # jv27 — silence 1
    ("jv27", JESUS, "-26%", "-6Hz",
     "My sheep hear my voice, and I know them, and they follow me:", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Hear, know, follow. He leads them to green places and still water, to rest and to "
     "plenty. And when one is small or tired or hurt, he does not scold it for falling "
     "behind — he lifts it up and carries it.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And here is the turn: the sheep are people. You. Tired, wandering, easily lost "
     "people, whom he knows by name and leads with his voice and gathers close and will "
     "not lose.", None),
    # jv28 — silence 2
    ("jv28", JESUS, "-26%", "-6Hz",
     "And I give unto them eternal life; and they shall never perish, neither shall any "
     "man pluck them out of my hand.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Once you are in his hand, it is over — for the fear, that is. Never perish. Never "
     "be snatched away. Not by your failures, not by your enemies, not by death itself. "
     "His grip on you does not depend on how tightly you can hold on to him.", None),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "He leads them home in the evening to the safe fold, and counts them in, and none "
     "are missing.", None),
    ("n7b", NARRATOR, "-24%", "-4Hz",
     "That is the shepherd he is. Led, not driven. Known, not counted. Held, and never "
     "let go. And even now he is calling, gently, past the flock, to whoever is still "
     "outside.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "The good shepherd knows his sheep by name, leads them by his voice, and holds them "
     "so no one can pluck them from his hand. He is still calling, gently, past the "
     "flock, to whoever is outside. Do you think that voice could be for you?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
