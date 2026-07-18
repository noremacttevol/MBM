#!/usr/bin/env python3
"""Generate narration audio for Story Video #62 — Ephphatha: the Deaf Man (Mark 7:31-37).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV: the one
word he spoke, "Ephphatha." (Mark 7:34) — Mark's gloss "that is, Be opened"
is given by the narrator.
GREEN story (no care flags). The spit detail of 7:33 is passed over gently
(the touch is what is shown and said). Homograph law: "wind" avoided in n6;
"Ephphatha" gets a SPOKEN respelling so TTS lands the Aramaic cleanly.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus came back from the coast by a long road — down through the "
     "Decapolis, the ten Gentile cities. Remember that name. It is the "
     "same region where the man from the tombs had been telling his "
     "story to anyone who would listen. Last time Jesus was on this "
     "side of the sea, the people asked him to leave. Now they come "
     "running, bringing him their broken. One man's testimony had "
     "changed the whole neighborhood."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "And they brought him a man who was deaf, and whose speech was "
     "tangled because of it. Think about what deafness meant in that "
     "world. No writing tablets for the poor, no signing schools, no "
     "way in. Every conversation, every joke, every warning, every "
     "kind word — all of it happened on the other side of a wall he "
     "could not cross. He was surrounded by people, and utterly "
     "alone."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "His friends begged Jesus just to touch him. Jesus did something "
     "better. He took the man by the hand and led him away from the "
     "crowd — completely alone, just the two of them. No audience. "
     "No spectacle. This healing was going to be private, personal, "
     "his."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Then Jesus did something beautiful. He could not explain "
     "anything with words — the man could not hear them. So he spoke "
     "the only language the man could receive. He put his fingers "
     "gently to the man's ears: I see exactly what is wrong. He "
     "touched the man's mouth: and this too. Then he looked up to "
     "heaven: what happens next comes from God. Sign language, from "
     "the Son of God, to one deaf man."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "And then Mark records a small, stunning detail. Looking up to "
     "heaven — Jesus sighed. He felt the weight of it: a world so "
     "broken that a man could go his whole life without hearing his "
     "own name. The sigh came first. Then, one word — in his own "
     "Aramaic mother tongue:"),
    # Exact KJV Mark 7:34 — the one word he spoke. SILENCE around it.
    ("j1", JESUS, "-25%", "-2Hz",
     "Ephphatha."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "It means: be opened. And everything opened. Sound rushed in "
     "where there had been forty years of nothing — birdsong, "
     "footsteps, voices, his own name. The knot in his tongue came "
     "loose, and the first plain words of his life came out."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "Jesus asked them to keep it quiet. They could not. The more he "
     "asked, the more they told everyone — and honestly, how do you "
     "keep a man's first words a secret? The whole region came to one "
     "verdict about Jesus: everything he does, he does well."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "Notice what kind of healer he is. He did not shout over the "
     "crowd. He took one man aside, met him inside his silence, "
     "explained everything in the man's own language before asking "
     "anything of him — and gave him back the world."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He does not heal for an audience. He takes you aside, meets you "
     "in your silence, and opens what was shut."),
]

# HOMOGRAPH LAW — "wind" deliberately avoided in n5 (birdsong instead).
# "Ephphatha" respelled for TTS so the Aramaic lands cleanly; caption stays exact.
SPOKEN = {
    "j1": "Effatha.",
}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        await save_narration(tts_text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
