#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #198 — An Ensign for the
Nations; the Second Time (Isaiah 11:10-12). From DRAFTS/row-198.md, validated
against the laws.
MEMBER-FORMAT FIX: the draft had no spoken KJV — Isaiah 11:11 (word-exact
opening fragment, the nation-list elided by design) and 11:12 added verbatim
as the SCRIPTURE VOICE centerpiece (Christopher, cream italic caption, sacred
silence). The narrator never quotes KJV.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Gathering of Israel" (THE-200 → GL).
Jesus does not appear in frame (messianic prophecy; the ensign is symbolic).
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
     "The prophet Isaiah pointed far ahead to a figure he called "
     "the root of Jesse — David's family tree, springing up fresh "
     "after it looked cut down."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "This one would stand as a banner, a signal, lifted up so the "
     "nations could find their way to Him. Not hidden. Raised for "
     "all to see."),
    # Exact KJV Isaiah 11:11 opening fragment (nation-list elided by design).
    ("s1", SCRIPTURE, "-24%", "-2Hz",
     "And it shall come to pass in that day, that the Lord shall "
     "set his hand again the second time to recover the remnant of "
     "his people,"),
    # sacred-silence beat. Exact KJV Isaiah 11:12 — THE CENTERPIECE.
    ("s2", SCRIPTURE, "-24%", "-2Hz",
     "And he shall set up an ensign for the nations, and shall "
     "assemble the outcasts of Israel, and gather together the "
     "dispersed of Judah from the four corners of the earth."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Exiles in every direction, lifted out of every nation, "
     "brought home. The ensign is the invitation; the gathering is "
     "the answer."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The banner is raised — and the seeking ones, from every "
     "people, come home."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "A banner was raised so you could find your way. Seek Him, "
     "and you'll be gathered in."),
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
