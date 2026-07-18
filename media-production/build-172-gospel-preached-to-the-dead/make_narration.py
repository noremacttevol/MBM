#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #172 — The Gospel Preached
to the Dead (1 Peter 4:6; ref also 3:18-20). From DRAFTS/row-172.md,
validated against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — the member verse-video format
(build-161 precedent) requires the exact KJV verse as the CENTERPIECE, read by
the SCRIPTURE VOICE (Christopher, cream italic caption, sacred silence).
1 Peter 4:6 added verbatim as s1. Closing card carries the Gospel Library
pointer: "Learn more — Gospel Library: Spirit World" (THE-200 → GL).
Jesus does not appear as a character (Peter's letter).
HOMOGRAPH LAW: the KJV verse contains "but LIVE according to God in the
spirit" — the #1 TTS offender, verb, must read /LIV/. SPOKEN respelling
applied; the caption keeps the exact KJV word. Ear-check s1 anyway. No other
flagged words.

SEGMENTATION (ASSEMBLY-C, 2026-07-17): n1 and n3 split at natural breaks so
all 7 stills carry a beat synced to what is being said (CAPTION LAW):
n1a→s5 the hand on the promise, n1b→s3 the quiet marker, n3a→s7 the open
door, n3b→s6 light ascending. Words unchanged from the pack.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Some who heard the good news had already died before they "
     "could finish their lives in the body."),
    # Exact KJV 1 Peter 4:6 — THE CENTERPIECE, scripture voice, sacred silence.
    ("s1", NARRATOR, "-20%", "-4Hz",
     "For for this cause was the gospel preached also to them that "
     "are dead, that they might be judged according to men in the "
     "flesh, but live according to God in the spirit."),
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "The gospel was preached to them too."),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "Not in vain, not too late."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "They might be judged by men's measure in the flesh — and yet "
     "be alive by God's measure in the spirit."),
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "Death did not close the door."),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "The message crossed over."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The gospel reaches beyond the grave. No one is outside the "
     "reach of his mercy."),
]

# HOMOGRAPH LAW — s1's "live" must read /LIV/ (verb). SPOKEN respelling
# steers the audio; the caption keeps the exact KJV word. Ear-check it.
# (n2 was reworded to "be alive", removing the draft's second "live".)
SPOKEN = {
    "s1": ("For for this cause was the gospel preached also to them that "
           "are dead, that they might be judged according to men in the "
           "flesh, but liv according to God in the spirit."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
