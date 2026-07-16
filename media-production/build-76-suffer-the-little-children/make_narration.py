#!/usr/bin/env python3
"""Generate narration audio for Story Video #76 — Suffer the Little Children
(Mark 10:13-16). Narrator: modern, warm, low, unhurried (American). Plain US only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Mark 10:14 and the FULL 10:15 including "Verily I say unto you" (fetched, not
hand-typed). STUDY-GEM: the archaic "suffer" = "let" is explained by the narrator in
one plain line (word-meaning tidbits are sanctioned by the pre-flight checklist).
CONTENT-CARE: GREEN — pure warmth; the disciples' blocking is gentle, never harsh.
HOMOGRAPH LAW: no known offenders — SPOKEN empty; ear-check every segment anyway.
No music bed: narration + intentional silence only.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Parents were bringing their little kids to Jesus, just so he could "
     "put his hands on them and bless them."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The disciples tried to wave them off — the Teacher is busy, this "
     "is grown-up work, not the place for children."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "When Jesus saw it, he wasn't pleased. He told them to stop."),
    # Exact KJV Mark 10:14 — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "Suffer the little children to come unto me, and forbid them not: "
     "for of such is the kingdom of God."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "That old word suffer just means let. Let them come. Don't stand "
     "in their way. Then he went further."),
    # Exact KJV Mark 10:15, the whole verse — sacred pause around it.
    ("j2", JESUS, "-20%", "-2Hz",
     "Verily I say unto you, Whosoever shall not receive the kingdom of "
     "God as a little child, he shall not enter therein."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "He meant: nobody earns their way into the kingdom of God. You "
     "receive it the way a child receives a gift — with open hands."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "Then he gathered them up in his arms and blessed them, one at a "
     "time, unhurried — like there was nowhere else he needed to be."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He had time for the smallest and least important person in the "
     "room. That includes you."),
]

# HOMOGRAPH LAW — no bow/wound/wind/tears/lead/sow/live/read in these segments;
# SPOKEN stays empty. Ear-check every segment before assembly regardless.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
