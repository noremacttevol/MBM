#!/usr/bin/env python3
"""Generate narration audio for Story Video #63 — The Man Born Blind (John 9).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 9:3(-manifest), 9:7a, 9:35b, 9:37 (fetched, not hand-typed).
The healed man's famous line (9:25) is PARAPHRASED by the narrator.
GREEN story. Homograph ear-check list scanned; no offenders used.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "In Jerusalem there was a man who begged at his same spot every "
     "day, because he had been blind since the day he was born. He had "
     "never seen his mother's face. Never seen morning. And as Jesus "
     "and his disciples passed by, the disciples asked the question "
     "everyone in that world assumed had an answer: whose fault is "
     "this? Who sinned — this man, or his parents?"),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "It was the standard theology of the day: if you are suffering, "
     "somebody must have earned it. People still run that math on "
     "themselves today. Jesus threw the whole equation out."),
    # Exact KJV John 9:3 — SILENCE around it.
    ("j1", JESUS, "-18%", "-2Hz",
     "Neither hath this man sinned, nor his parents: but that the "
     "works of God should be made manifest in him."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Nobody's fault. Not a punishment. Jesus refused to explain the "
     "man's suffering — and instead announced what it was about to "
     "become: a place where God's work would be seen. Then he knelt "
     "down, made soft clay with the dust of the ground, and gently "
     "spread it over the blind man's eyes with his own hands."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Why clay? Bible students hear an echo: in the beginning, God "
     "formed man from the dust of the ground. Whatever had been left "
     "unfinished in those eyes from birth, the maker was finishing it "
     "now, with the same material he started with. Then he gave the "
     "man one simple instruction:"),
    # Exact KJV John 9:7a — SILENCE around it.
    ("j2", JESUS, "-20%", "-2Hz",
     "Go, wash in the pool of Siloam."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Understand what was asked of him. A blind man, eyes packed with "
     "mud, feeling his way across Jerusalem, one wall and one step at "
     "a time, holding nothing but the instruction of a stranger whose "
     "face he had never seen. He went. That walk was the faith."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "He knelt at the pool of Siloam and washed the clay away. And "
     "light came pouring in where there had never been light — color, "
     "water, sky, his own two hands. The first things he ever saw. He "
     "came back seeing."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "And then the trouble started. The neighbors argued about "
     "whether he was even the same man. The religious leaders hauled "
     "him in for questioning — twice — because the healing had "
     "happened on the sabbath, and that broke their rules. They "
     "pressed him to call Jesus a sinner. His answer is one of the "
     "greatest sentences anyone ever said: he only knew one thing for "
     "certain — he had been blind all his life, and now he could "
     "see."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "They could not shake him, so they threw him out — cast out of "
     "the synagogue, cut off from the whole religious life of his "
     "people. Healed, and homeless in the same week. And here is the "
     "part to remember: when Jesus heard they had thrown him out, he "
     "went and FOUND him. The man had never actually seen the one who "
     "healed him. Jesus asked him:"),
    # Exact KJV John 9:35b — SILENCE around it.
    ("j3", JESUS, "-20%", "-2Hz",
     "Dost thou believe on the Son of God?"),
    ("n8", NARRATOR, "-20%", "-4Hz",
     "The man asked who that was, so he could believe. And Jesus said:"),
    # Exact KJV John 9:37.
    ("j4", JESUS, "-20%", "-2Hz",
     "Thou hast both seen him, and it is he that talketh with thee."),
    ("n9", NARRATOR, "-20%", "-4Hz",
     "The first face he ever truly studied was the face of the one "
     "who gave him his eyes. He said, Lord, I believe — and he "
     "worshipped him, right there in the street the religious world "
     "had thrown him out of. The question of whose fault it was got "
     "no answer that day. The man got something better. He got found."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "You may never get the why for what you carry. But when the "
     "world shuts you out, he comes and finds you."),
]

# HOMOGRAPH LAW — scanned: no bow/wound/wind/tears/lead/sow/live(s)/read/dove/
# bass/minute/use(d)/close in any segment. No overrides needed.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
