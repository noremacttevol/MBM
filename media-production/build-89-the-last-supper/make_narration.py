#!/usr/bin/env python3
"""Generate narration audio for Story Video #89 — "The Last Supper" (Luke 22:14-20).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Luke 22:19b and 22:20b, per the draft.
CONTENT-CARE: DEEP — intimate Passover meal; betrayal only implied, never shown;
mercy and love spoken plainly.
HOMOGRAPH LAW: draft flags clean. NOTE "shed" and "blood" are safe; ear-check
"given" and every segment anyway. SPOKEN empty.
No music bed: narration + intentional silence only.
Built from DRAFTS/row-089.md (validated 2026-07-17 by W1-STILLS).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0a", NARRATOR, "-20%", "-4Hz",
     "The Passover had come."),
    ("n0b", NARRATOR, "-20%", "-4Hz",
     "Jesus gathered his closest friends around one table in an upper "
     "room, knowing the night would change everything."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "He told them plainly: he had wanted this meal with them before "
     "the hard thing happened."),
    # n2 reworded (ASSEMBLY-C, Translation Law): the pack's "said it was
    # his body, given for them" echoed j1 verbatim — j1 delivers those words.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Then he took the bread, gave thanks, broke it, and gave it to "
     "them."),
    # Exact KJV Luke 22:19b — SILENCE around it.
    ("j1", JESUS, "-18%", "-2Hz",
     "This is my body which is given for you: this do in remembrance "
     "of me."),
    # n3 reworded (ASSEMBLY-C, Translation Law): the pack's "the new
    # promise written in his own blood, poured out" echoed j2 — j2 says it.
    ("n3", NARRATOR, "-20%", "-4Hz",
     "After the meal he lifted the cup, and gave it to them, too."),
    # Exact KJV Luke 22:20b — SILENCE around it.
    ("j2", JESUS, "-18%", "-2Hz",
     "This cup is the new testament in my blood, which is shed for "
     "you."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "He said he would not drink the fruit of the vine again until the "
     "kingdom of God arrives. Then he and his friends sang together "
     "and walked out into the night."),
    # n5 (ASSEMBLY-C): the emblems-remain still (s9) closing beat — carries
    # the pack's own "a gift to remember him by".
    ("n5", NARRATOR, "-20%", "-4Hz",
     "The bread and the cup, still on the table — a gift to remember "
     "him by."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He left a simple meal to remember him by. Come to his table — he "
     "is still the host."),
]

# HOMOGRAPH LAW — draft flags clean; SPOKEN stays empty. Ear-check every
# segment before assembly regardless.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
