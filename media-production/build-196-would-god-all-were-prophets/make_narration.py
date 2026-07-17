#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #196 — "Would God That All
the LORD's People Were Prophets" (Numbers 11:24-29). From DRAFTS/row-196.md,
validated against the laws.
MEMBER-FORMAT FIX: the draft carried Moses's great answer only as narrator
paraphrase — Numbers 11:29 (Moses's own words) added verbatim as the
SCRIPTURE VOICE centerpiece (Christopher, cream italic caption, sacred
silence). The narrator never quotes KJV.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Personal Revelation" (THE-200 → GL).
Jesus does not appear (OT narrative); the presence is cloud and light only.
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
     "The weight of leading a whole nation was crushing Moses. He "
     "told the LORD he could not carry the people alone, not one "
     "more day."),
    # n1 split so "gather seventy" and "share the Spirit" land on their own
    # stills (s2 gather-me-seventy, s3 the-spirit-shared) per the CAPTION LAW.
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "So God told Moses to gather seventy trusted men."),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "He would take some of the Spirit that rested on Moses and "
     "share it with them, and together they would help bear the "
     "load."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "When the Spirit came down on those seventy, they began to "
     "speak God's words. But two men, Eldad and Medad, had stayed "
     "back in the camp — and the Spirit came on them too, right "
     "there among the tents."),
    # n3 split so the runner and Joshua's objection land on their own stills
    # (s5 the-runner, s6 forbid-them) per the CAPTION LAW.
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "A runner hurried to Moses with the news."),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "Joshua, Moses's right-hand man, was worried — stop them, he "
     "said. That is not how it is supposed to work."),
    # sacred-silence beat. Exact KJV Num 11:29 — Moses's words, CENTERPIECE.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "Enviest thou me for my sake? would God that all the LORD's "
     "people were prophets, and that the LORD would put his spirit "
     "upon them!"),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "One of the most generous answers in all of scripture. Moses "
     "did not guard the gift — he wished it wider."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "Moses did not guard the gift — he wished it for everyone. "
     "The same Spirit is offered to you. Ask, and receive."),
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
