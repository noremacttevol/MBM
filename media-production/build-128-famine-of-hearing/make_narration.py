#!/usr/bin/env python3
"""Generate narration audio for Story Video #128 — The Famine of Hearing
(Amos 8:11-12). From DRAFTS/row-128.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Old Testament prophecy — Jesus does NOT appear. The KJV verses (the word of
the Lord through Amos) are read by the SCRIPTURE VOICE (Christopher), per the
build-161 verse-video precedent: Christopher carries exact KJV, narrator
never does.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "The prophet Amos carried a warning from the Lord — not about "
     "food, but about something people would miss even more."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A day would come when God's voice would seem far away — not "
     "because He stopped speaking, but because people stopped "
     "being able to hear."),
    # Exact KJV Amos 8:11 — scripture voice, sacred weight.
    ("s1", SCRIPTURE, "-22%", "-2Hz",
     "Behold, the days come, saith the Lord GOD, that I will send "
     "a famine in the land, not a famine of bread, nor a thirst "
     "for water, but of hearing the words of the LORD:"),
    # Exact KJV Amos 8:12.
    ("s2", SCRIPTURE, "-22%", "-2Hz",
     "And they shall wander from sea to sea, and from the north "
     "even to the east, they shall run to and fro to seek the word "
     "of the LORD, and shall not find it."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The deepest hunger isn't in the stomach. It's the ache of a "
     "soul that can't find a word from God."),
    # sacred-silence beat follows n2.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The cure was never far. It was to listen while His voice "
     "could still be heard."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "When His word is near, don't let it pass. Listen now — the "
     "famine is the silence we choose."),
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
