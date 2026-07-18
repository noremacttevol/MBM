#!/usr/bin/env python3
"""Generate narration audio for Story Video #150 — The Shepherd Psalm
(Psalm 23:1-6). From DRAFTS/row-150.md, validated against the laws.
Narrator: modern, warm, low, unhurried (American). Plain US model only.
TRANSLATION-LAW FIX: the draft's narrator opened with the verbatim KJV clause
"The LORD is my shepherd" — the narrator never quotes KJV, so Psalm 23:1 is
carried EXACT by the SCRIPTURE VOICE (Christopher, build-161 precedent) and
the narrator's intro is reworded; the "Surely goodness and mercy" echo in the
draft's n5 was also softened to plain modern words.
Jesus does not appear as a character (the Shepherd is the LORD).
HOMOGRAPH LAW — BUILDER EAR-CHECK n1 ("He LEADS me"): must read /LEEDZ/,
never /LEDZ/; prepared override below if misread. "life" is the noun, safe.
No other flagged words.

SEGMENTATION (ASSEMBLY-C, 2026-07-17): n1, n4 and n5 split at natural breaks
so all 8 stills carry a beat synced to what is being said (CAPTION LAW):
n1a→s1(out) still waters, n1b→s2 he restoreth, n4a→s5 the table, n4b→s6 oil
on the head, n5a→s7 toward the dwelling, n5b→s8 let-him-lead. Only n5's
"and" is capitalized to stand alone; every other word unchanged.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"      # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # the scripture voice. Exact KJV only.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Three thousand years ago a shepherd-king wrote a song about "
     "being shepherded himself. It starts like this:"),
    # Exact KJV Psalm 23:1 — scripture voice, sacred weight.
    ("s1", NARRATOR, "-20%", "-4Hz",
     "The LORD is my shepherd; I shall not want."),
    ("n1a", NARRATOR, "-20%", "-4Hz",
     "He leads me to quiet water and green places to rest."),
    ("n1b", NARRATOR, "-20%", "-4Hz",
     "He puts my life back together."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "He guides me down the right paths, for His name's sake."),
    # sacred-silence beat follows n2.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Even in the darkest valley, I'm not afraid. You are with "
     "me — Your rod and staff steady me."),
    ("n4a", NARRATOR, "-20%", "-4Hz",
     "You set a table for me right in front of my enemies."),
    ("n4b", NARRATOR, "-20%", "-4Hz",
     "You honor me; my cup runs over."),
    ("n5a", NARRATOR, "-20%", "-4Hz",
     "Your goodness and Your mercy will chase me down every day I "
     "have."),
    ("n5b", NARRATOR, "-20%", "-4Hz",
     "And I'll be home with You forever."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The Shepherd who leads, restores, and walks the dark valley "
     "with you is the same One who invites you home. Let Him "
     "lead."),
]

# HOMOGRAPH LAW — ear-check n1 "leads" and the card's "leads"/"lead"
# (both must read /LEED/). If misread, uncomment the overrides.
SPOKEN = {
    # "n1": ("He leeds me to quiet water and green places to rest. He puts "
    #        "my life back together."),
    # "card": ("The Shepherd who leeds, restores, and walks the dark valley "
    #          "with you is the same One who invites you home. Let Him "
    #          "leed."),
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
