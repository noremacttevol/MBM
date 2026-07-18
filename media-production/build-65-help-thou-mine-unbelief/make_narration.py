#!/usr/bin/env python3
"""Generate narration audio for Story Video #65 — "Help Thou Mine Unbelief" (Mark 9:14-29).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Scripture voice: AMERICAN, never British. Exact-KJV lines only:
 - Jesus, Mark 9:23b: "If thou canst believe, all things are possible to him that believeth."
 - The father, Mark 9:24b: "Lord, I believe; help thou mine unbelief."
CONTENT-CARE: TENDER — a father's honest half-faith is treated with dignity; the boy's
suffering is never sensationalized.
HOMOGRAPH LAW: no offenders (believe/unbelief/faith are safe). SPOKEN empty; ear-check
every segment anyway.
No music bed: narration + intentional silence only.
Authored 2026-07-17 by W1-STILLS (no Hermes draft existed for this row).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
SCRIPTURE = "en-US-ChristopherNeural"  # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus came down from the mountain to find a crowd in an uproar — "
     "scribes arguing, his disciples cornered, and at the center a "
     "father at the end of his rope."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "His only son had suffered for years, and the disciples hadn't been "
     "able to help. The father turned to Jesus with the last of his "
     "hope: if you can do anything, have pity on us."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Jesus answered him gently."),
    # Exact KJV Mark 9:23b — Jesus, sacred pause.
    ("j1", SCRIPTURE, "-18%", "-2Hz",
     "If thou canst believe, all things are possible to him that "
     "believeth."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "And the father cried out the most honest prayer in the whole "
     "Bible — faith and doubt in the same breath."),
    # Exact KJV Mark 9:24b — the father, SILENCE around it.
    ("j2", SCRIPTURE, "-18%", "-2Hz",
     "Lord, I believe; help thou mine unbelief."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "It was enough. Jesus took the boy by the hand, lifted him up, and "
     "gave him back to his father — well, and whole."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He didn't wait for perfect faith. Bring him the little you have — "
     "and ask him to help the rest."),
]

# HOMOGRAPH LAW — no offenders; SPOKEN stays empty. Ear-check every segment anyway.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
