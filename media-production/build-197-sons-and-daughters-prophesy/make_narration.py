#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #197 — "Your Sons and Your
Daughters Shall Prophesy" (Joel 2:28-29; quoted Acts 2:17-18). From
DRAFTS/row-197.md, validated against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — Joel 2:28 and 2:29 added
verbatim as the SCRIPTURE VOICE centerpiece (Christopher, cream italic
caption, sacred silence). The narrator never quotes KJV.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Revelation in the Last Days" (THE-200 → GL).
Jesus does not appear bodily (OT prophecy + post-ascension fulfillment).
CONTENT-CARE: symbolic only — soft light, no fire on faces.
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
     "The prophet Joel looked down the long corridor of time and "
     "described a day the LORD promised — not for a few insiders, "
     "but for all."),
    # Exact KJV Joel 2:28 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "And it shall come to pass afterward, that I will pour out my "
     "spirit upon all flesh; and your sons and your daughters "
     "shall prophesy, your old men shall dream dreams, your young "
     "men shall see visions:"),
    # Exact KJV Joel 2:29 — SILENCE around it.
    ("s2", SCRIPTURE, "-24%", "-2Hz",
     "And also upon the servants and upon the handmaids in those "
     "days will I pour out my spirit."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Not stopped by age or status — every kind of person, filled "
     "with the same Spirit."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Decades later, on the day of Pentecost, the apostle Peter "
     "stood and said this promise had arrived. The Spirit fell, "
     "and ordinary people told of the mighty works of God."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The promise was never meant to be locked in one building or "
     "one office. It was poured out — freely, widely, for whoever "
     "calls on the name of the LORD."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The promise was all flesh. That includes you. The Spirit is "
     "offered — receive Him."),
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
