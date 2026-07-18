#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #191 — The Windows of
Heaven (Malachi 3:8-10). From DRAFTS/row-191.md, validated against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — Malachi 3:10 added verbatim
as the SCRIPTURE VOICE centerpiece (Christopher, cream italic caption, sacred
silence). The narrator never quotes KJV.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Tithing" (THE-200 → GL).
Jesus does not appear (the prophet speaks for the LORD); no divine figure —
the promise is light through parted clouds.
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
     "Through the prophet Malachi, the LORD made a strange offer "
     "to a people holding back — bring everything in, and watch "
     "what I do."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The storehouse was the place set apart for the Lord's house, "
     "and the tithe was the part meant for him."),
    # Exact KJV Malachi 3:10 — THE CENTERPIECE, scripture voice.
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "Bring ye all the tithes into the storehouse, that there may "
     "be meat in mine house, and prove me now herewith, saith the "
     "LORD of hosts, if I will not open you the windows of heaven, "
     "and pour you out a blessing, that there shall not be room "
     "enough to receive it."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "A dare no king could make — test me, and see if I don't open "
     "the windows."),
    # sacred-silence beat follows n2.
    # n3 is split in two so each phrase lands on its own storyboard still
    # (s5 no-room-enough, s6 wonder-not-worry) per the CAPTION LAW.
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "Not a trickle."),
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "A pouring out, more than there is room to hold."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He invites you to test his goodness. Bring it all, and watch "
     "the windows open."),
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
