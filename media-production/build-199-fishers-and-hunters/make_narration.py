#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #199 — Fishers and Hunters
(Jeremiah 16:14-16). From DRAFTS/row-199.md, validated against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — Jeremiah 16:16 added
verbatim as the SCRIPTURE VOICE centerpiece (Christopher, cream italic
caption, sacred silence). The narrator never quotes KJV.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Missionary Work" (THE-200 → GL).
Jesus does not appear (Jeremiah's prophecy).
CONTENT-CARE (judgment story): mercy spoken aloud throughout; the hunt kept
symbolic and reverent — open hands, never weapons.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment (card included). No SPOKEN overrides
needed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "The prophet Jeremiah spoke a hard word to a people who would "
     "not turn. The LORD said He would send searchers — and no "
     "hiding place would be far enough."),
    # Exact KJV Jeremiah 16:16 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "Behold, I will send for many fishers, saith the LORD, and "
     "they shall fish them; and after will I send for many "
     "hunters, and they shall hunt them from every mountain, and "
     "from every hill, and out of the holes of the rocks."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "It is a picture of judgment — the nets and the hunt find "
     "everyone."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "But hear the mercy underneath: the same God who sends the "
     "search is the one who wants them found, not lost. Judgment "
     "is the last call, not the first."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The point was never the catching — it was that a holy God "
     "would not let His people slip away unnamed. He seeks, even "
     "when seeking means discipline."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "For us the picture flips into hope: the Fisher of men "
     "searches still, not to condemn, but to bring home whoever "
     "will be found."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The hunt was a wake-up, not a goodbye. He's still searching "
     "for you — let yourself be found."),
]

# HOMOGRAPH LAW — every segment ear-checked against the flag list
# (bow, wound, wind, tears, lead, sow, live/lives, read, dove, bass,
# minute, use/used, close): none present. Captions stay exact.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
