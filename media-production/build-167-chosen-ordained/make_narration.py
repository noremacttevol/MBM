#!/usr/bin/env python3
"""Narration for build-167-chosen-ordained — John 15.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both halves, unchanged.
  kv16a  John 15:16  'Ye have not chosen me, but I have chosen you, and ordained you,'
  kv16b  John 15:16  'that ye should go and bring forth fruit, and that your fruit
                      should remain: that whatsoever ye shall ask of the Father in
                      my name, he may give it you.'
Gospel, Jesus in the flesh in the upper room, red-letter. The build had already
split John 15:16 into two beats for pacing — that split is between two halves of
ONE red sentence, not between two speakers, so both halves are red and both stay
red. Nothing moved.

NO NEW SPLITS. There is no evangelist frame anywhere in this verse; 'Ye have not
chosen me' is Christ's own opening, not John's introduction, so kv16a is red from
its first word.

Checked both halves against the King James text and they join back into John
15:16 word for word with nothing dropped at the seam. Nothing lifted from
paraphrase — n2 retells kv16a and n5 retells kv16b, so the retelling rule is
already satisfied by the narrator the build has.

WHY-LAW: milk. Being called is presented as a gift you receive by name, never a
badge you pin on yourself. No office is named and no organisation is argued for
— just the direction of the choosing, from heaven down.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "The people God calls to his work rarely go looking for the honour. They are usually found doing something ordinary — mending a net, carrying water, quietly living an unremarkable life, never dreaming of appointing themselves to anything."),
    # John 15:16
    ("kv16a", JESUS, "Ye have not chosen me, but I have chosen you, and ordained you,"),
    ("n2", NARRATOR, "Notice the direction of it. The choosing runs from heaven down to us, not the other way. He picks a person out, calls them by their own name, and sets them apart with real authority for a work that is his to give."),
    ("n3", NARRATOR, "And a calling is never just a title to wear. It is a sending. Those he chose were meant to go — out to the roads and the villages, to actually do the thing they had been set apart to do."),
    ("n4", NARRATOR, "The measure of it would be simple and real: fruit. Not applause, not a position, but honest results — good work done, and people lifted and gathered in, like a harvest brought home."),
    # John 15:16
    ("kv16b", JESUS, "that ye should go and bring forth fruit, and that your fruit should remain: that whatsoever ye shall ask of the Father in my name, he may give it you."),
    ("n5", NARRATOR, "And what fruit it was to be: not a flash that fades, but a harvest that lasts. Better still, the calling came backed with power — so that what these called ones asked of heaven, in the proper way, heaven would answer and give."),
    ("n6", NARRATOR, "Here is the quiet study gem. You do not license yourself into God's service, and you do not have to. He calls of his own choosing, by name, and ordains for the work. To be called of God is a gift you receive, not a badge you take."),
    ("n7", NARRATOR, "And that call still goes out, still by name, still to ordinary people who never went looking for it. When heaven singles you out and calls you by your own name, will you look up, and answer?"),
    ("card", NARRATOR, "You do not choose yourself into God's work — he chooses and ordains, by name, for fruit that lasts. When heaven calls you by your own name, will you look up, and answer?"),
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
