#!/usr/bin/env python3
"""Narration for build-108-my-sheep-hear-my-voice — John 10.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both existing red beats are correctly red and were left alone. John 10:1-18 and
10:27-28 are Jesus speaking in the flesh, straight through, with no evangelist
framing welded into either segment, so there was nothing to split and nothing to
move out of red.

STAYED RED (jesus):
  jv27  John 10:27  'My sheep hear my voice, and I know them, and they follow me:'
  jv28  John 10:28  'And I give unto them eternal life; and they shall never
                     perish, neither shall any man pluck them out of my hand.'

LIFTED FROM PARAPHRASE - both are also Jesus, so both are RED:
  jv3   John 10:3   'The sheep hear his voice: and he calleth his own sheep by
                     name, and leadeth them out.'
  jv11  John 10:11  'I am the good shepherd: the good shepherd giveth his life
                     for the sheep.'
n3 was already saying John 10:3 in modern English ('each one, called by its own
name'), so the real verse now speaks first and n3 stands as its lead-in. jv11 is
the sentence the whole video is built on and it was not in the video at all.
These are inside the shepherd discourse, so a red-letter KJV prints them red -
this is not a character inside a parable, it is Jesus in his own voice.

NEW NARRATOR BEAT: n4b retells jv11 in plain English, per the retelling rule.

STILL REASSIGNED, NO NEW ART: n6 moves from S6 to S8. n6 is the retelling of
jv28 ('Once you are in his hand'), and S8 is literally 'in his hand', while S6
now carries jv11 and its retelling. Nothing was added to or removed from the
artwork; one beat points at a different existing still, and it removes an
out-of-order jump back to S6 that was in the original running order.

WOMEN: John 10 records no woman speaking. Nothing was added rather than importing
a line from elsewhere.

WHY-LAW: he leads rather than drives, knows rather than counts, and holds rather
than hoping you hold on. Milk framing - the grip is his, not yours.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "In that world, a shepherd did not drive his sheep from behind. He walked out in front of them, and they followed — not because they were forced, but because they knew his voice."),
    ("n2", NARRATOR, "Several flocks might share one fold overnight. But in the morning, when a shepherd called, only his own sheep lifted their heads and came. They could tell his voice from a stranger's. That is the picture Jesus reaches for."),
    ("n3", NARRATOR, "He knows them one at a time. Not a nameless herd — each one, called by its own name, gently, personally. And knowing his voice, they come to him and follow."),
    # John 10:3
    ("jv3", JESUS, "The sheep hear his voice: and he calleth his own sheep by name, and leadeth them out."),
    # John 10:27
    ("jv27", JESUS, "My sheep hear my voice, and I know them, and they follow me:"),
    ("n4", NARRATOR, "Hear, know, follow. He leads them to green places and still water, to rest and to plenty. And when one is small or tired or hurt, he does not scold it for falling behind — he lifts it up and carries it."),
    # John 10:11
    ("jv11", JESUS, "I am the good shepherd: the good shepherd giveth his life for the sheep."),
    ("n4b", NARRATOR, "I am the good shepherd, he said. Not a hired man who runs off when it turns dangerous — a shepherd who lays his own life down for the sheep. That is what he was willing to spend to keep them. That is what he was willing to spend to keep you."),
    ("n5", NARRATOR, "And here is the turn: the sheep are people. You. Tired, wandering, easily lost people, whom he knows by name and leads with his voice and gathers close and will not lose."),
    # John 10:28
    ("jv28", JESUS, "And I give unto them eternal life; and they shall never perish, neither shall any man pluck them out of my hand."),
    ("n6", NARRATOR, "Once you are in his hand, it is over — for the fear, that is. Never perish. Never be snatched away. Not by your failures, not by your enemies, not by death itself. His grip on you does not depend on how tightly you can hold on to him."),
    ("n7", NARRATOR, "He leads them home in the evening to the safe fold, and counts them in, and none are missing."),
    ("n7b", NARRATOR, "That is the shepherd he is. Led, not driven. Known, not counted. Held, and never let go. And even now he is calling, gently, past the flock, to whoever is still outside."),
    ("card", NARRATOR, "The good shepherd knows his sheep by name, leads them by his voice, and holds them so no one can pluck them from his hand. He is still calling, gently, past the flock, to whoever is outside. Do you think that voice could be for you?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
# calleth/leadeth (Cameron complaint #108, twice): measured A/B 2026-07-21 in the
# jesus voice (EricNeural -22%): plain "calleth" renders isolated as "Kalloth";
# "kawleth" round-trips "calleth" in-sentence (same fix as #8). Plain "leadeth"
# renders "Lettuce"/"letteth" BOTH isolated and in-sentence; "leedeth"
# round-trips "leadeth" clean both ways. Captions keep the true KJV spellings.
SPOKEN = {"calleth": "kawleth", "leadeth": "leedeth"}


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
