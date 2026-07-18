#!/usr/bin/env python3
"""Generate narration audio for Story Video #6 — The Two Sons (Matthew 21:28-32).
Narrator: modern, warm, low, unhurried (American).
Jesus voice: AMERICAN, never British (Cameron's permanent law, 2026-07-07).
Jesus speaks ONLY exact KJV: Matthew 21:31a and Matthew 21:31b.
Script follows media-production/06-two_sons-production-pack.md exactly,
plus the "why Jesus told it" opening bookend Cameron approved on video #8.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

# NARRATOR CHANGED 2026-07-08 (Cameron): the Multilingual voice model drifted
# into foreign-sounding accents on some words. Plain US model only, permanent.
NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # Opening bookend — why Jesus told this story (pattern approved on #8)
    ("n0", NARRATOR, "-22%", "-4Hz",
     "Jesus told this story to religious leaders — people who were sure "
     "they had already said yes to God. He told it so they would hear "
     "themselves in it."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A father told his first son: Go work in the vineyard today. "
     "The son said, \"I will not.\" "
     "Later he changed his mind, and went."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The father told his second son the same thing. That son said, "
     "\"Yes, I will go.\""),
    ("n2b", NARRATOR, "-25%", "-5Hz",
     "And didn't."),
    # n2c/n2d added 2026-07-08: Cameron caught a 16-second dead stretch with
    # no narration mid-video ("it just stops talking, it's broken"). The
    # narrator must carry the story all the way through — no silent scenes.
    ("n2c", NARRATOR, "-22%", "-4Hz",
     "The first son meant his no. But it wouldn't leave him alone. "
     "All morning, the vineyard kept pulling at him."),
    # n2d reworded 2026-07-08: the TTS voice stumbled on "he just went to
    # work" (Cameron's catch). Simpler ending phrase reads clean.
    ("n2d", NARRATOR, "-22%", "-4Hz",
     "So he got up. And he went. No announcement, no apology. "
     "He went back to the vineyard, and he worked."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "The row the second son promised to work stayed empty all day. "
     "Then Jesus asked the crowd a question."),
    ("j1", JESUS, "-25%", "-6Hz",
     "Whether of them twain did the will of his father?"),
    # n4 fixed 2026-07-08 (Cameron): the narrator must NOT re-quote Jesus's
    # KJV words back. Jesus speaks the scripture; the narrator gives only the
    # plain modern meaning, then the answer.
    ("n4", NARRATOR, "-22%", "-4Hz",
     "He was asking: which of the two did what his father wanted? "
     "The crowd answered: the one who first said no."),
    # peak — music cuts to silence under n4's answer
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Then he turned to the religious leaders — the ones who were sure "
     "they were the second son."),
    ("j2", JESUS, "-25%", "-6Hz",
     "Verily I say unto you, That the publicans and the harlots go into "
     "the kingdom of God before you."),
    # n6 added 2026-07-08 (Cameron): the closing card cut away too fast to
    # read. Now held longer AND spoken aloud, gently.
    ("n6", NARRATOR, "-25%", "-5Hz",
     "Have you ever said no to something — maybe loudly — and found "
     "yourself moving toward it anyway, because part of you couldn't "
     "let it go?"),
]

async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        # save_narration writes the mp3 AND a <name>.timing.json sidecar with
        # REAL per-sentence spoken timestamps, so captions line up with the voice.
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3 (+timing)")

if __name__ == "__main__":
    asyncio.run(main())
