#!/usr/bin/env python3
"""Generate narration audio for Story Video #3 — Zacchaeus (Luke 19:1-10).
Narrator: modern, warm, low, unhurried (American). Plain US model only —
Multilingual models are banned (Cameron, 2026-07-08).
Jesus voice: AMERICAN, never British (Cameron's permanent law, 2026-07-07).
Jesus speaks ONLY exact KJV: Luke 19:5, 19:9, 19:10 (fetched, not hand-typed).
Script pre-flighted on paper per PRODUCTION-BIBLE.md section 4b — see
PREFLIGHT.md. FULL-STORY law: all ten verses covered, vv7-10 included
(the pack had stopped early and marked v10 "optional" — caught on paper).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-22%", "-4Hz",
     "Zacchaeus was a tax collector — which in his time meant he worked "
     "for the occupying empire, and got rich doing it. In Jericho everyone "
     "knew his name, and no one wanted him at their table."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "When Jesus came through town, Zacchaeus wanted to see him. But he "
     "was short, and the crowd was a wall. Nobody makes room for the man "
     "they all despise."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "So he ran ahead. A grown man. A rich man. Robes flapping, rings and "
     "dignity forgotten."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And he climbed a tree — just to catch a glimpse from a distance. "
     "He would have settled for that. A glimpse."),
    # PEAK — music has already cut to full silence before this line
    ("n4", NARRATOR, "-25%", "-5Hz",
     "Jesus stopped, right under that tree. And looked up."),
    # Exact KJV Luke 19:5b (fetched, not hand-typed) — split at the KJV
    # semicolon so each half carries its own caption (clip, then still).
    ("j1a", JESUS, "-25%", "-6Hz",
     "Zacchaeus, make haste, and come down;"),
    ("j1b", JESUS, "-25%", "-6Hz",
     "for to day I must abide at thy house."),
    # Pack-approved bridge — quotes only the two words as commentary,
    # never the sentence (Translation Law).
    ("n5", NARRATOR, "-22%", "-4Hz",
     "'I must' — not 'I might.' Out of everyone in that crowd, staying "
     "with the man everyone hated wasn't a detour. It was the plan."),
    # v6-7: the joyful coming down AND the murmuring crowd (Full-Story law)
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Zacchaeus half-fell out of that tree with joy. And the crowd "
     "couldn't believe it. Of every house in Jericho, he chose the "
     "cheat's. They grumbled about it, out loud."),
    # v8: the standing gift — narrator paraphrase (Zacchaeus is not the
    # Jesus voice), plus the Seed line from the pack.
    # v8 split into three caption-sized beats; the Seed line stands alone.
    ("n7a", NARRATOR, "-22%", "-4Hz",
     "Nobody demanded anything. But grace had already gotten there "
     "first."),
    ("n7b", NARRATOR, "-22%", "-4Hz",
     "Zacchaeus stood up at his own table: half of everything I own goes "
     "to the poor — and anyone I cheated, I will pay back four times "
     "over."),
    ("n7c", NARRATOR, "-25%", "-5Hz",
     "He changed because Jesus came first."),
    ("n8", NARRATOR, "-25%", "-5Hz",
     "And Jesus gave the story its last words."),
    # Exact KJV Luke 19:9b and 19:10 — the TRUE last story words.
    ("j2a", JESUS, "-25%", "-6Hz",
     "This day is salvation come to this house, forsomuch as he also is "
     "a son of Abraham."),
    ("j2b", JESUS, "-25%", "-6Hz",
     "For the Son of man is come to seek and to save that which was "
     "lost."),
    # Closing card read aloud, gently (Readable-Card Law).
    ("n9", NARRATOR, "-25%", "-5Hz",
     "Have you ever done something — maybe something a little "
     "embarrassing — just to get a look at something you thought might "
     "be real?"),
]

async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
