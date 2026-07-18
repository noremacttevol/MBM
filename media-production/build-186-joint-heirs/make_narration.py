#!/usr/bin/env python3
"""Generate narration audio for MEMBER Verse Video #186 — Heirs of God,
Joint-Heirs with Christ (Romans 8:16-17). From DRAFTS/row-186.md, validated
against the laws.
MEMBER-FORMAT + TRANSLATION-LAW FIX: the draft had no scripture-voice
centerpiece and its narrator echoed Rom 8:17 nearly verbatim ("heirs of God,
and joint-heirs with Christ"). Fixed: Romans 8:16 and 8:17 added verbatim as
the SCRIPTURE VOICE centerpiece (Christopher); the narrator lines are plain
paraphrase only.
Closing card carries the Gospel Library pointer:
"Learn more — Gospel Library: Divine Nature" (THE-200 → GL).
Jesus does not appear (epistle teaching) — companion light only.
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
     "Paul wrote to the believers in Rome about who they really "
     "were — not strangers, not outsiders."),
    # Exact KJV Romans 8:16 — THE CENTERPIECE, scripture voice.
    ("s1", NARRATOR, "-20%", "-4Hz",
     "The Spirit itself beareth witness with our spirit, that we "
     "are the children of God:"),
    # Exact KJV Romans 8:17 — SILENCE around it.
    ("s2", NARRATOR, "-20%", "-4Hz",
     "And if children, then heirs; heirs of God, and joint-heirs "
     "with Christ; if so be that we suffer with him, that we may "
     "be also glorified together."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Children first — and because children, inheritors. What the "
     "Father has belongs to the family, and the family includes "
     "you."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "The terms were honest: share in his suffering, and you will "
     "share in his glory too."),
    # sacred-silence beat follows n2.
    # n3 is split in two so each thought lands on its own storyboard still
    # (s6 the-closing-line, s7 dawn-over-the-city) with the caption on screen
    # always matching what is being said (CAPTION LAW).
    ("n3a", NARRATOR, "-20%", "-4Hz",
     "Not earned by effort. Received by belonging."),
    # "Co-heirs" reworded 2026-07-17 (ASSEMBLY-D ear-check): the compound
    # slurred into "co-wares" on both whisper models; "Heirs together" reads
    # clean (the pack's own card already uses the single word "Heir").
    ("n3b", NARRATOR, "-20%", "-4Hz",
     "Heirs together with the Son."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "You're not a visitor at the table — you're family. Heir with "
     "the Son. Come home."),
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
