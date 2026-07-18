#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #184 — Caught Up to the
Third Heaven (2 Corinthians 12:2-4, 9). From DRAFTS/row-184.md, validated
against the laws.
MEMBER-FORMAT + TRANSLATION-LAW + ATTRIBUTION FIXES: the draft had no
scripture-voice centerpiece and put the KJV fragment "my strength is made
perfect in weakness" in the NARRATOR's mouth. Fixed: 2 Cor 12:2 and 12:4
added verbatim as the scripture-voice centerpiece — and 2 Cor 12:9 is the
LORD's own answer to Paul ("And he said unto me..."), so it is carried by the
JESUS voice as an exact KJV line.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Degrees of Glory" (THE-200 → GL).
No divine figure is depicted — the heavens are layered light only.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment (card included). No SPOKEN overrides
needed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # scripture voice AND Jesus voice. Exact KJV only.
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Paul wrote of a man he knew — caught up, in a single moment, "
     "far beyond the everyday world."),
    # Exact KJV 2 Cor 12:2 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "I knew a man in Christ above fourteen years ago, (whether in "
     "the body, I cannot tell; or whether out of the body, I "
     "cannot tell: God knoweth;) such an one caught up to the "
     "third heaven."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Whether in the body or out of it, Paul could not say; God "
     "alone knew. And from that height, he was carried further "
     "still."),
    # Exact KJV 2 Cor 12:4 — SILENCE around it.
    ("s2", SCRIPTURE, "-24%", "-2Hz",
     "How that he was caught up into paradise, and heard "
     "unspeakable words, which it is not lawful for a man to "
     "utter."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "He could have boasted. He had the credentials. Instead he "
     "pointed to his weakness — because of what the Lord had told "
     "him."),
    # Exact KJV 2 Cor 12:9 — the Lord's own answer to Paul, Jesus voice.
    ("j1", JESUS, "-22%", "-2Hz",
     "My grace is sufficient for thee: for my strength is made "
     "perfect in weakness."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Paul was shown more than words can carry — and still pointed "
     "back to grace."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Paul was shown more than words can hold — and still pointed "
     "back to grace. There is more ahead than you can imagine."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present. Captions stay exact.
# SPOKEN-OVERRIDE (Cameron denial #184, 2026-07-18: "it read from Jesus' voice a
# winkey face at 22 secs"). KJV 2 Cor 12:2 closes its parenthetical with "knoweth;)"
# — semicolon immediately followed by a close-paren — and edge-tts read ";)" aloud as
# a WINKY FACE in the scripture voice. The spoken text drops the two parenthesis
# characters (they are editorial punctuation, never spoken anyway); the on-screen
# caption still carries the exact KJV text with its parentheses, because build.py
# takes caption text from SEGMENTS, never from SPOKEN.
SPOKEN = {
    "s1": ("I knew a man in Christ above fourteen years ago, whether in "
           "the body, I cannot tell; or whether out of the body, I "
           "cannot tell: God knoweth; such an one caught up to the "
           "third heaven."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
