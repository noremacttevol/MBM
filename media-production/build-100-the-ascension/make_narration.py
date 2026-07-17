#!/usr/bin/env python3
"""Generate narration audio for Story Video #100 — The Ascension (Acts 1:6-11).
From DRAFTS/row-100.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Acts 1:8, ELIDED BY DESIGN — the draft drops the leading "But" and the place
list ("both in Jerusalem, and in all Judaea, and in Samaria,"); the spoken
fragments are word-exact KJV in their original order. Caption shows the same.
The angels' line is spoken plainly by the NARRATOR (never the Jesus voice).
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "In his last moments with them, the disciples asked Jesus if "
     "he was going to restore the kingdom right then. He turned "
     "them toward something bigger."),
    # Exact KJV Acts 1:8 (elided by design — see docstring).
    ("j1", JESUS, "-20%", "-2Hz",
     "Ye shall receive power, after that the Holy Ghost is come "
     "upon you: and ye shall be witnesses unto me, unto the "
     "uttermost part of the earth."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He was handing them the mission — go tell everyone, "
     "everywhere. And then something happened they would never "
     "forget."),
    # sacred-silence beat follows n1: the still holds on the ascending figure.
    # n2 split so the lift and the cloud land on their own stills (s4
    # lifted-up, s5 the-cloud-received-him) per the CAPTION LAW.
    ("n2a", NARRATOR, "-20%", "-4Hz",
     "While they watched, he was lifted up,"),
    ("n2b", NARRATOR, "-20%", "-4Hz",
     "and a cloud received him out of their sight. They stood "
     "there staring into the sky, stunned."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Then two figures in white stood beside them with a promise:"),
    ("n4", NARRATOR, "-18%", "-3Hz",
     "This same Jesus, who was taken up from you into heaven, will "
     "come back the same way you've seen him go."),
    # "leave them orphans" slurred to "the orphans" on ear-check (same trap as
    # #185); reworded to "abandon them", which reads clean.
    ("n5", NARRATOR, "-20%", "-4Hz",
     "He did not abandon them. He left them a mission, a "
     "promise, and the sure word that he's coming again."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He's coming back the same way he left. Until then, you're "
     "not alone — and you're not without purpose."),
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
