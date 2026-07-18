#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #194 — The Fruit of the
Spirit (Galatians 5:22-23). From DRAFTS/row-194.md, validated against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — Galatians 5:22-23 added
verbatim as the SCRIPTURE VOICE centerpiece (Christopher, cream italic
caption, sacred silence). The narrator never quotes KJV (n4's near-echo of
v23 softened to plain words).
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Holy Ghost" (THE-200 → GL).
Jesus does not appear (Paul's epistle); the Spirit hinted as soft light only.
HOMOGRAPH LAW: "lives" in n0 ("when God's Spirit LIVES in a person") — the #1
TTS offender, verb, must read /LIVZ/. SPOKEN respelling applied; the caption
keeps the true spelling. Ear-check n0 anyway. No other flagged words (card
checked).
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Paul wrote that when God's Spirit lives in a person, a "
     "harvest grows — not crops, but character."),
    # Exact KJV Gal 5:22-23 — THE CENTERPIECE, scripture voice.
    ("s1", NARRATOR, "-20%", "-4Hz",
     "But the fruit of the Spirit is love, joy, peace, "
     "longsuffering, gentleness, goodness, faith, Meekness, "
     "temperance: against such there is no law."),
    # n1 split so "joy" and "peace" land on their own fruit stills (s3 joy,
    # s4 peace) per the CAPTION LAW.
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "First, love. Then joy."),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "Then peace — the kind that doesn't depend on circumstances."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Longsuffering next — patience that doesn't quit. Then "
     "gentleness, and goodness, and faith that holds."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Meekness, and temperance — self-control that masters the "
     "storms inside."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "And no law anywhere forbids any of it. These are the things "
     "that can't be overdone."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "This fruit isn't grown by strain. Ask the Spirit — and let "
     "it ripen in you."),
]

# HOMOGRAPH LAW — n0's "lives" must read /LIVZ/. SPOKEN respelling steers the
# audio; the caption keeps the true spelling. Ear-check before assembly.
SPOKEN = {
    "n0": ("Paul wrote that when God's Spirit livs in a person, a "
           "harvest grows — not crops, but character."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
