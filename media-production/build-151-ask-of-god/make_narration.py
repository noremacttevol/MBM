#!/usr/bin/env python3
"""Narration for build-151-ask-of-god — James 1.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

James 1 is an epistle. The writer is James, the Lord's brother — not Jesus.
A red-letter King James Bible prints nothing in James in red. Both red beats
move to SCRIPTURE (light blue):
  kv5  James 1:5  'If any of you lack wisdom...'   RED -> SCRIPTURE
  kv6  James 1:6a 'But let him ask in faith...'    RED -> SCRIPTURE

No mixed segments — neither verse quotes anyone else, so nothing is split.

ADDED: s6b is the rest of James 1:6, verbatim, so the wavering image James
actually wrote is heard instead of only summarised. It sits on the same still
as kv6 (S7), so the picture the viewer sees is unchanged, and n7 already does
the modern-English retelling for both halves.

WHY-LAW: milk. God is glad to be asked, gives openly, and does not scold. The
one thing asked back is faith. Nothing on screen argues the Restoration — but
n4's quiet 'a young man... finds a quiet place... and asks' is left exactly as
written, so a viewer who later meets Joseph Smith's account recognises it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Sooner or later, every one of us reaches a question too big for us. A fork in the road, a choice we cannot reason our way through, a doubt we cannot settle on our own. We lack wisdom, and trying harder does not seem to give it."),
    ("n2", NARRATOR, "When that happens, most of us ask everyone around us. Friends, teachers, the loudest voices in the crowd. And often we come away more tangled than before, because the answers all disagree with each other."),
    ("n3", NARRATOR, "But there is another door, and it has been standing open the whole time. You can go straight to the One who made you and simply ask. Not only a teacher, not only a book, but God himself, directly."),
    # James 1:5
    ("kv5", SCRIPTURE, "If any of you lack wisdom, let him ask of God, that giveth to all men liberally, and upbraideth not; and it shall be given him."),
    ("n4", NARRATOR, "So a young man does the plainest thing there is. He finds a quiet place away from the noise, he kneels down, and he asks. Honestly, out loud, the way a child asks a father who is glad to be asked."),
    ("n5", NARRATOR, "Now look at how God is described here. He gives to everyone who asks. Not grudgingly, not a thin trickle measured out drop by drop, but openly and generously, more than the person even came for."),
    ("n6", NARRATOR, "And he does not scold. He does not shame you for not knowing, or hold your past against you, or make you feel small for coming late to ask. He simply gives. That is the kind of God this verse is describing."),
    # James 1:6
    ("kv6", SCRIPTURE, "But let him ask in faith, nothing wavering."),
    # James 1:6
    ("s6b", SCRIPTURE, "For he that wavereth is like a wave of the sea driven with the wind and tossed."),
    ("n7", NARRATOR, "There is one thing asked of us in return, and it is not cleverness. It is faith. To ask believing that he truly hears, and then to hold steady, without letting doubt quietly pull the question back apart before the answer comes."),
    ("n8", NARRATOR, "And the promise on the end of that verse is not a maybe. It shall be given him. Wisdom you could never argue your way into can be given, to anyone, for the honest asking. So here is the only question left. What have you been trying to work out all alone, that you could ask him about instead?"),
    ("card", NARRATOR, "You do not have to stay stuck. If you lack wisdom, ask of God. He gives to all, openly, and does not scold. Ask in faith, and it shall be given. What would you ask him?"),
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
