#!/usr/bin/env python3
"""Narration for build-192-the-fast-god-has-chosen — Isaiah 58.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Isaiah 58. Both red beats move to GREEN, and one buried verse is lifted out.

  s1  Isaiah 58:6  'Is not this the fast that I have chosen?...'      RED -> GOD
  s2  Isaiah 58:8  'Then shall thy light break forth as the morning'  RED -> GOD
  g7  Isaiah 58:7  NEW - lifted out of narrator paraphrase            -> GOD

Isaiah 58 is the LORD in the first person from verse 3 onward. 'the fast that I
HAVE CHOSEN' is God naming his own choice, so s1 is green. s2 is the same
unbroken oracle continuing into the promise, still God speaking to 'thou' - the
verse only sounds like narration because the given text stops before 'the glory
of the LORD shall be thy rereward'. Green for both. Isaiah is Old Testament, so
`jesus` is not available; a red-letter KJV prints this black.

n0 stays NARRATOR and is the split the brief warned about. 'Isaiah told God's
people what kind of fast the LORD actually wants' is the storyteller framing the
chapter in modern English - Isaiah's own third-person setup, not God's voice. It
is the boundary between the prophet's frame and God's speech, and it is already
its own segment, so no cut was needed.

LIFT - the real upgrade here. n1a, n1b and n2 were paraphrasing Isaiah 58:7 in
modern English without the verse ever being heard: bread to the hungry, the poor
brought home, the naked covered, not hiding from your own family. That is one of
the plainest verses in the Old Testament and the video was talking around it.
Isaiah 58:7 is now `g7`, verbatim and green, sitting on ST3 immediately before
the three narrator beats that already retell it. The retelling rule is satisfied
without writing a word of new narration - n1a, n1b and n2 were always the
retelling, they just had nothing to retell.

TWO GREEN BEATS BACK TO BACK, on purpose. s1 runs straight into g7 with no
narrator between, which the validator flags. Isaiah 58:6 and 58:7 are one
continuous divine question - 'Is not this the fast that I have chosen... Is it
not to deal thy bread to the hungry' - and God is still mid-sentence at the verse
break. Cutting a retelling into the middle would break the rhythm of the one
question the chapter is asking. n1a, n1b and n2 retell BOTH verses immediately
after, across three beats. The rule is met once for the pair rather than twice.

Verbatim: g7 is Isaiah 58:7 word for word including the closing 'and that thou
hide not thyself from thine own flesh?'. s1 and s2 were already exact and were
not touched.

n3 stays narrator paraphrase on purpose. It compresses Isaiah 58:9 and 58:10
('Then shalt thou call, and the LORD shall answer... thy darkness be as the
noonday') into one modern sentence, and it refers to the LORD in the third
person, so it is not a quotation and must not be painted green. Lifting a third
verse would have put three Old English blocks in a fifty-second video.

Ids: every original id kept. g7 is the only new one. The card is 'card' and stays
out of beats, as the original had it.

WHY-LAW: milk. The fast God wants is a hand opened to someone hurting. No
argument about fasting rules - just what he actually asked for.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Isaiah told God's people what kind of fast the LORD actually wants — not just going hungry to look holy."),
    # Isaiah 58:6
    ("s1", GOD, "Is not this the fast that I have chosen? to loose the bands of wickedness, to undo the heavy burdens, and to let the oppressed go free, and that ye break every yoke?"),
    # Isaiah 58:7
    ("g7", GOD, "Is it not to deal thy bread to the hungry, and that thou bring the poor that are cast out to thy house? when thou seest the naked, that thou cover him; and that thou hide not thyself from thine own flesh?"),
    ("n1a", NARRATOR, "Share your bread with the hungry."),
    ("n1b", NARRATOR, "Bring the poor, the ones with nowhere to go, into your home."),
    ("n2", NARRATOR, "When you see someone with no clothes, cover them. Don't turn away from your own family."),
    # Isaiah 58:8
    ("s2", GOD, "Then shall thy light break forth as the morning, and thine health shall spring forth speedily:"),
    ("n3", NARRATOR, "The LORD promises — call, and He answers. Help others, and your own darkness becomes noonday."),
    ("card", NARRATOR, "The fast God chooses is a hand opened to the hurting. Open yours — He meets you there."),
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
