#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #195 — "Prove All Things;
Hold Fast That Which Is Good" (1 Thessalonians 5:21-22). From
DRAFTS/row-195.md, validated against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — 1 Thessalonians 5:21 and
5:22 added verbatim as the SCRIPTURE VOICE centerpiece (Christopher, cream
italic caption, sacred silence). The narrator never quotes KJV.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Personal Revelation" (THE-200 → GL).
Jesus does not appear (Paul's epistle).
CONTENT-CARE: discernment without fear — no embodied evil anywhere.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment (card included). No SPOKEN overrides
needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Paul gave the early church a short, sharp command about what "
     "to believe and what to keep."),
    # Exact KJV 1 Thes 5:21 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "Prove all things; hold fast that which is good."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Test everything, he said. Don't swallow every voice — weigh "
     "it, hold it up to the light."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "And when you find what is genuinely good, cling to it. Don't "
     "let it slip."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "He paired it with a warning — and it's the shortest fence he "
     "ever built:"),
    # Exact KJV 1 Thes 5:22.
    ("s2", SCRIPTURE, "-24%", "-2Hz",
     "Abstain from all appearance of evil."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "The same word fits now: a faith that checks, then commits — "
     "that's steady, not gullible."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Weigh it, then hold it. The good He shows you is worth "
     "keeping — reach for it."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present. Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
