#!/usr/bin/env python3
"""Generate narration audio for Story Video #61 — The Syrophoenician Woman (Mark 7:24-30).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Mark 7:27 and 7:29 (fetched, not hand-typed).
The woman's reply (7:28) is PARAPHRASED by the narrator (Translation Law —
only Jesus quotes KJV; no narrator line echoes KJV wording).
CONTENT-CARE: the daughter is NEVER shown or described afflicted (Children Law);
no embodied devils; she appears only healed and peaceful.
WHY-LAW: the "dogs" line is explained the way she heard it (children first =
Israel first; the word is the little household pups) — a test, not an insult.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus went north — out of Jewish land entirely, up to the coast "
     "around Tyre. Gentile country. He slipped into a house and wanted "
     "no one to know he was there. But Mark says it plainly: he could "
     "not be hidden. Word about him had crossed the border long before "
     "he did."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "And one woman heard it. A Greek, born in that country — a "
     "Syrophoenician, which is Mark's way of saying: not one of us. "
     "Wrong nation, wrong religion, no claim at all on a Jewish rabbi. "
     "But her little girl was sick with something dark that no one "
     "could fix. And a mother with a sick child does not care about "
     "borders."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "She found the house. She came in uninvited, fell down at his "
     "feet, and begged him — cast this thing out of my daughter. "
     "Every social rule in the room said she had no right to ask. "
     "She asked anyway."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "What Jesus said next sounds harsh — until you hear it the way "
     "she heard it."),
    # Exact KJV Mark 7:27 — silence around the Jesus line.
    ("j1", JESUS, "-18%", "-2Hz",
     "Let the children first be filled: for it is not meet to take the "
     "children's bread, and to cast it unto the dogs."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Here is the why. The children first — that was his mission order: "
     "Israel first, then the whole world. And the word he chose was not "
     "the word for street dogs. It was the word for the little pups a "
     "family keeps under its own table. He had not slammed a door. He "
     "had painted a picture of a household — and left her a place in "
     "it, if she could see it. She saw it instantly."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "She did not argue with him. She stepped right into the picture. "
     "True, she said — but even the pups under the table get what the "
     "children drop. Bible students love this moment: it is the only "
     "time in the gospels anyone wins an exchange with Jesus. And you "
     "can almost hear how glad he was to lose it."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "He answered her:"),
    # Exact KJV Mark 7:29 — silence around the Jesus line.
    ("j2", JESUS, "-20%", "-2Hz",
     "For this saying go thy way; the devil is gone out of thy "
     "daughter."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "Notice what he did not do. He did not walk to her house. He did "
     "not touch the girl. He simply said it was done — across the "
     "distance, on his word alone. And she believed him enough to "
     "just... go home. That walk home, holding nothing but his word, "
     "was the faith he praised."),
    ("n8", NARRATOR, "-20%", "-4Hz",
     "She came to her door and found her daughter lying on the bed, "
     "resting — quiet, and whole. The dark thing was gone. It had left "
     "at the exact moment he spoke."),
    ("n9", NARRATOR, "-20%", "-4Hz",
     "The first outsider in Mark's gospel to be told yes was a Gentile "
     "mother with no credentials, no standing, and no appointment — "
     "just a stubborn, clear-eyed faith that would not leave without "
     "the crumbs. He gave her the whole loaf."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "She refused to believe there was no room for her at his table. "
     "There is room for you."),
]

# HOMOGRAPH LAW — ear-check list scanned: no bow/wound/wind/tears/lead/sow/
# live(s)/read/dove/bass/minute/use(d)/close in any segment. No overrides needed.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
