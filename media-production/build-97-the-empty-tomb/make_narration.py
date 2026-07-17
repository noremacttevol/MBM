#!/usr/bin/env python3
"""Generate narration audio for Story Video #97 — The Empty Tomb (Luke 24:1-8).
From DRAFTS/row-097.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus does NOT appear and does NOT speak — he is risen; the empty tomb is the
point. The angels' line is spoken plainly by the NARRATOR (never the Jesus
KJV voice — that voice is reserved for exact KJV from Jesus alone).
HOMOGRAPH LAW: ear-checked — no bow/wound/wind/tears/lead/sow/live/read/dove/
bass/minute/use(d)/close in any segment ("living" and "risen" are not
ambiguous words). No SPOKEN overrides needed.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Very early on the first day of the week, while it was still "
     "dark, the women who loved him came to the tomb carrying "
     "spices to anoint his body."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "But when they arrived, the huge stone that had sealed the "
     "tomb was rolled away."),
    # sacred-silence beat follows n1: the still holds on the open tomb mouth.
    # n2 split so the empty ledge and their fear land on their own stills (s3
    # the-empty-ledge, s4 fear-and-awe) per the CAPTION LAW.
    ("n2a", NARRATOR, "-20%", "-4Hz",
     "They stepped inside — and the body was gone."),
    ("n2b", NARRATOR, "-20%", "-4Hz",
     "They stood there, confused and afraid."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Then two figures in dazzling clothing stood beside them, and "
     "asked a question that has echoed for two thousand years:"),
    ("n4", NARRATOR, "-18%", "-3Hz",
     "Why do you look for the living among the dead? He is not "
     "here — he is risen."),
    # n5 split so the reminder and the remembering land on their own stills
    # (s6 she-remembers, s7 running-into-sunrise) per the CAPTION LAW.
    ("n5a", NARRATOR, "-20%", "-4Hz",
     "Remember, they said, what he told you back in Galilee — that "
     "he would be crucified, and on the third day rise again."),
    ("n5b", NARRATOR, "-20%", "-4Hz",
     "And they remembered."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The tomb couldn't hold him. Whatever feels dead and sealed "
     "shut in your life — he's the God of the rolled-away stone."),
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
