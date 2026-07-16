#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #171 — "Else What Shall They
Do Which Are Baptized for the Dead?" (1 Corinthians 15:29).
From DRAFTS/row-171.md, validated against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV at all — the member verse-video
format (build-161 precedent) requires the exact KJV verse as the CENTERPIECE,
read by the SCRIPTURE VOICE (Christopher, cream italic caption, sacred
silence). 1 Cor 15:29 added verbatim as s1. The narrator gives modern meaning
and never quotes KJV. Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Baptisms for the Dead" (THE-200 → GL).
Jesus does not appear as a character.
HOMOGRAPH LAW: the card contains "Because He LIVES" — the #1 TTS offender:
must read /LIVZ/, never /LYVZ/. SPOKEN respelling applied; the caption keeps
the true spelling. Ear-check the card before assembly anyway. No other
flagged words.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Paul asked a striking question: if the dead don't rise at "
     "all, why would anyone be baptized on their behalf?"),
    # Exact KJV 1 Cor 15:29 — THE CENTERPIECE, scripture voice, sacred silence.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "Else what shall they do which are baptized for the dead, if "
     "the dead rise not at all? why are they then baptized for the "
     "dead?"),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The only reason to do such a thing is the quiet hope that "
     "the dead are not gone forever."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Baptism stands for new life — a beginning, not an end."),
    # sacred-silence beat follows n2.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "So the work done for those who've passed is built on one "
     "promise: that death is not the last word."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Christ rose. And because He rose, the grave loses its grip — "
     "for Him first, and then for all who belong to Him."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "The ordinance done in love reaches across the veil, offering "
     "every soul the chance to choose."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Death separates for a while, not forever. Because He lives, "
     "there is hope for every name on the other side of the veil."),
]

# HOMOGRAPH LAW — the card's "lives" must read /LIVZ/. SPOKEN respelling
# steers the audio; the caption keeps the true spelling. Ear-check it.
SPOKEN = {
    "card": ("Death separates for a while, not forever. Because He livs, "
             "there is hope for every name on the other side of the veil."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
