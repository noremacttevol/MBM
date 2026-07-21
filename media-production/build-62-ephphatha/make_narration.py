#!/usr/bin/env python3
"""Narration for build-62-ephphatha — Mark 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED. j1 "Ephphatha" (Mark 7:34) is Jesus speaking in the flesh, in his own
Aramaic, and a red-letter KJV inks it. Kept its id and its one word.

NARRATION FRAMING SPLIT OFF IT. Mark 7:34 reads "And looking up to heaven, he
sighed, and saith unto him, Ephphatha, that is, Be opened." Three different things
are welded together there and only the middle one is Jesus:
  s34a  [scripture]  "And looking up to heaven, he sighed, and saith unto him,"
  j1    [jesus]      "Ephphatha."
  "that is, Be opened" is Mark translating for his Greek readers -- narration, not
  speech. n5 already carries it in the storyteller's voice ("It means: be opened"),
  which is exactly right, so nothing new was added there.
s34a sits on the SAME still (S6) immediately before j1. n4 keeps its id and is
trimmed so it sets the sigh up instead of describing it twice.

THE WHOLE REGION SPEAKS, AND IT WAS IN WHITE. n6 ended on a paraphrase --
"everything he does, he does well." That is Mark 7:37, the crowd's verdict, and it
is one of the great sentences in the gospel. Lifted verbatim as s37 [scripture] on
S8: "He hath done all things well: he maketh both the deaf to hear, and the dumb to
speak." n6 keeps its id, trimmed to the frame; n6b retells it.

PRONUNCIATION FLAG, NOT GUESSED AT. "Ephphatha" is the single word this whole video
is built on, and if the voice mangles it the video fails. I have NOT put a
respelling in `spoken` -- the law says a bad respelling is worse than none, and this
one has to be verified by transcribing the rendered audio with faster_whisper, not
assumed. Flagging it here so the audio pass checks this build first. The target is
ep-FA-tha. The caption keeps the true spelling either way.

NO GREEN: Jesus looks up to heaven, but the Father does not speak in Mark 7:31-37.
WOMEN: no woman speaks in this passage. Nothing invented.

S3 (s3-they-brought-him.jpeg) is on disk but the original build left it out of the
running order. Left out, deliberately -- the law says do not touch the artwork.

WHY-LAW: he took one man out of the crowd, alone, and explained the whole thing in
the only language that man could receive before he asked anything of him. Milk: he
does not heal for an audience.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus came back from the coast by a long road — down through the Decapolis, the ten Gentile cities. Remember that name. It is the same region where the man from the tombs had been telling his story to anyone who would listen. Last time Jesus was on this side of the sea, the people asked him to leave. Now they come running, bringing him their broken. One man's testimony had changed the whole neighborhood."),
    ("n1", NARRATOR, "And they brought him a man who was deaf, and whose speech was tangled because of it. Think about what deafness meant in that world. No writing tablets for the poor, no signing schools, no way in. Every conversation, every joke, every warning, every kind word — all of it happened on the other side of a wall he could not cross. He was surrounded by people, and utterly alone."),
    ("n2", NARRATOR, "His friends begged Jesus just to touch him. Jesus did something better. He took the man by the hand and led him away from the crowd — completely alone, just the two of them. No audience. No spectacle. This healing was going to be private, personal, his."),
    ("n3", NARRATOR, "Then Jesus did something beautiful. He could not explain anything with words — the man could not hear them. So he spoke the only language the man could receive. He put his fingers gently to the man's ears: I see exactly what is wrong. He touched the man's mouth: and this too. Then he looked up to heaven: what happens next comes from God. Sign language, from the Son of God, to one deaf man."),
    ("n4", NARRATOR, "And then Mark records a small, stunning detail — one that has nothing to do with the healing at all. Listen to exactly how he writes it."),
    # Mark 7:34
    ("s34a", SCRIPTURE, "And looking up to heaven, he sighed, and saith unto him,"),
    # Mark 7:34
    ("j1", JESUS, "Ephphatha."),
    ("n5", NARRATOR, "He sighed. Before the word, he sighed. He felt the weight of it — a world so broken that a man could go a whole lifetime without hearing his own name. The sigh came first. Then one word, in his own Aramaic mother tongue. It means: be opened. And everything opened. Sound rushed in where there had been a lifetime of nothing — birdsong, footsteps, voices, his own name. The knot in his tongue came loose, and the first plain words of his life came out."),
    ("n6", NARRATOR, "Jesus asked them to keep it quiet. They could not. The more he asked, the more they told everyone — and honestly, how do you keep a man's first words a secret? The whole region came to one verdict about him:"),
    # Mark 7:37
    ("s37", SCRIPTURE, "He hath done all things well: he maketh both the deaf to hear, and the dumb to speak."),
    ("n6b", NARRATOR, "He has done everything well, they said. He makes the deaf hear, and he gives the speechless their voice. Not a bad verdict from a region that had asked him to leave the last time he came."),
    ("n7", NARRATOR, "Notice what kind of healer he is. He did not shout over the crowd. He took one man aside, met him inside his silence, explained everything in the man's own language before asking anything of him — and gave him back the world."),
    ("card", NARRATOR, "He does not heal for an audience. He takes you aside, meets you in your silence, and opens what was shut."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
