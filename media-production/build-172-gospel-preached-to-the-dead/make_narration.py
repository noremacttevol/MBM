#!/usr/bin/env python3
"""Narration for build-172-gospel-preached-to-the-dead — 1 Peter 4.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

s1 moves JESUS-RED -> SCRIPTURE (light blue). One line out of red. 1 Peter 4:6
is Peter writing his letter; Jesus is not speaking and a red-letter KJV prints
none of it red.

No mixed segments — s1 is Peter start to finish, so nothing was split. The
doubled 'For for' at the start of s1 is genuine KJV and was left exactly as it
stands rather than tidied.

One passage lifted in, SCRIPTURE (Peter):
  s19  1 Peter 3:18-19  'For Christ also hath once suffered for sins... By which
       also he went and preached unto the spirits in prison'
This is the verse chapter 4 verse 6 depends on, and without it the build asserts
that the message crossed over without ever showing the viewer where that comes
from. With it, the two verses sit next to each other and the conclusion is the
viewer's to draw. It is followed by n3a ('Death did not close the door.') which
retells it.

All original ids kept (n0, s1, n1a, n1b, n2, n3a, n3b, card). New id is s19
only. Beats reuse ST6 and ST7 — n3a and n3b swap stills so the new beat sits
cleanly and every still is still used; no new artwork.

MILK: the video never says the words spirit world, never explains what happens
next, and never argues about who is saved. It quotes two verses of Peter and
stops. That is the whole point of putting this one on the restoration shelf — a
member or a ready investigator sees the doctrine in the Bible itself before
anyone explains it to them.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Some who heard the good news had already died before they could finish their lives in the body."),
    # 1 Peter 4:6
    ("s1", SCRIPTURE, "For for this cause was the gospel preached also to them that are dead, that they might be judged according to men in the flesh, but live according to God in the spirit."),
    ("n1a", NARRATOR, "The gospel was preached to them too."),
    ("n1b", NARRATOR, "Not in vain, not too late."),
    ("n2", NARRATOR, "They might be judged by men's measure in the flesh — and yet be alive by God's measure in the spirit."),
    # 1 Peter 3:18-19
    ("s19", SCRIPTURE, "For Christ also hath once suffered for sins, the just for the unjust, that he might bring us to God, being put to death in the flesh, but quickened by the Spirit: By which also he went and preached unto the spirits in prison;"),
    ("n3a", NARRATOR, "Death did not close the door."),
    ("n3b", NARRATOR, "The message crossed over."),
    ("card", NARRATOR, "The gospel reaches beyond the grave. No one is outside the reach of his mercy."),
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
