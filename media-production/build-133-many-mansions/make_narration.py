#!/usr/bin/env python3
"""Generate narration audio for Story Video #133 — "In My Father's House Are
Many Mansions" (John 14:1-3). From DRAFTS/row-133.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 14:1-2 (word-exact fragments in order; the v3 return promise is carried
by the narrator in modern words, per the draft).
TRANSLATION-LAW FIX: the draft's closing card ended with the verbatim KJV
phrase "Let not your heart be troubled" in the NARRATOR's mouth — modernized
to "Don't let your heart be troubled" (the narrator never quotes KJV).
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment. No SPOKEN overrides needed.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 split so the goodbye still and the speaking-peace still each
    # carry their half — draft words verbatim.
    ("n0a", NARRATOR, "-20%", "-4Hz",
     "Jesus was preparing His disciples for a hard goodbye."),
    ("n0b", NARRATOR, "-20%", "-4Hz",
     "His words could have brought fear — instead they brought "
     "comfort."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Don't let your heart be troubled, He said. Trust God. Trust "
     "Me."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "He described a home they couldn't see yet — a place He was "
     "going to make ready for them, room for each one."),
    # sacred-silence beat follows n2. Exact KJV John 14:1-2.
    ("j1", JESUS, "-22%", "-2Hz",
     "Let not your heart be troubled: ye believe in God, believe "
     "also in me. In my Father's house are many mansions: if it "
     "were not so, I would have told you. I go to prepare a place "
     "for you."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "And then the promise that undoes every fear: I'm coming "
     "back. I'll bring you to Myself, so you're where I am."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Not a vague hope. A prepared place. A return. A reunion."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He's preparing a place — and He's coming back for you. Don't "
     "let your heart be troubled."),
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
