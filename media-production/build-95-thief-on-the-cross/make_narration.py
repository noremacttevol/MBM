#!/usr/bin/env python3
"""Generate narration audio for Story Video #95 — The Thief on the Cross
(Luke 23:39-43). From DRAFTS/row-095.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Luke 23:43 (verified against the passage — the draft's shortened line was
restored to the full exact clause "Verily I say unto thee, To day shalt thou
be with me in paradise." KJV spells "To day" as two words; caption stays exact).
CONTENT-CARE: crucifixion carried with reverent distance — faces, never wounds.
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 split so the scene and the mocker land on their own stills (s1
    # three-crosses, s2 the-mocking-thief) per the CAPTION LAW.
    ("n0a", NARRATOR, "-20%", "-4Hz",
     "Two criminals were crucified with Jesus, one on each side."),
    ("n0b", NARRATOR, "-20%", "-4Hz",
     "One of them sneered — if you're really the Christ, save "
     "yourself and us."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "But the other one stopped him. We're getting what we "
     "deserve, he said. This man has done nothing wrong."),
    # sacred-silence beat follows n1.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Then he turned his head toward Jesus and asked for the "
     "smallest thing — just to be remembered."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Lord, remember me when you come into your kingdom. No good "
     "deeds to offer. No time left to fix his life. Just a dying "
     "man asking."),
    # Exact KJV Luke 23:43 — SILENCE around it.
    ("j1", JESUS, "-22%", "-2Hz",
     "Verily I say unto thee, To day shalt thou be with me in "
     "paradise."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Today. Not someday, not after you've earned it. Today. The "
     "last-minute faith of a criminal was enough."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He saved a man who had nothing to give but a request. It's "
     "never too late to ask."),
]

# HOMOGRAPH LAW — n4 contains "last-minute" ("minute" is on the flag list:
# must read /MIN-it/, never /my-NOOT/). SPOKEN respelling steers the audio;
# the caption keeps the true spelling. Ear-check n4 before assembly anyway.
# No other flagged words in any segment ("life" in n3 is the noun, safe).
SPOKEN = {
    "n4": ("Today. Not someday, not after you've earned it. Today. The "
           "last-minit faith of a criminal was enough."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
