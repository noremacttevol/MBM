#!/usr/bin/env python3
"""Narration for build-162-keys-of-kingdom — Matthew 16.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: both original red beats, unchanged.
  kv18  Matthew 16:18  'And I say also unto thee, That thou art Peter...'
  kv19  Matthew 16:19  'And I will give unto thee the keys of the kingdom...'
Gospel, Jesus in the flesh at Caesarea Philippi, red-letter both. Already
verbatim, no evangelist frame welded on, so no split was needed on either.

LIFTED FROM PARAPHRASE — this is the change that matters here. The scene is an
exchange, and neither half of it was ever spoken in the video:
  jv15  Matthew 16:15  'But whom say ye that I am?'                     JESUS, RED
  s16   Matthew 16:16  'Thou art the Christ, the Son of the living God.' SCRIPTURE
n1 was asking Christ's question in the storyteller's modern voice and n2 was
reporting Peter's answer second-hand. Now the Lord asks it himself in red, and
Peter answers in his own words in light blue. Peter is an apostle, not Christ,
so his confession is blue — this is the same call build-103-peters-confession
makes. The KJV frame 'And Simon Peter answered and said,' is deliberately left
off so s16 is his words only.

jv15 -> s16 is a DELIBERATE question-and-answer pair, the one place in this
build where two non-narrator beats touch. It is the exception the retelling
rule allows, and n2 retells both halves immediately after. The validator will
warn about it; the warning is expected and correct to ignore.

Both new beats sit on stills the build already has — jv15 on S1 with n1, s16 on
S2 with n2 — so no new artwork.

WHY-LAW: milk. Keys are shown as something given, never seized. The build says
authority came from the Lord to a fisherman and stops there; it does not argue
where the keys are now, it only asks whether you would trust them if you found
them.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Far to the north, at a rocky place called Caesarea Philippi, Jesus stopped with his disciples and put a piercing question to them. Who do you say that I am?"),
    # Matthew 16:15
    ("jv15", JESUS, "But whom say ye that I am?"),
    # Matthew 16:16
    ("s16", SCRIPTURE, "Thou art the Christ, the Son of the living God."),
    ("n2", NARRATOR, "It was Simon Peter, the fisherman, who answered for them all. You are the Christ, he said, the Son of the living God. And Jesus told him that flesh and blood had not revealed that to him; his Father in heaven had."),
    ("n3", NARRATOR, "Then Jesus said something that would change Simon's life. He gave him a new name — Peter, which means a rock — and told him that on rock like that, solid and sure, he would build something meant to outlast the ages."),
    # Matthew 16:18
    ("kv18", JESUS, "And I say also unto thee, That thou art Peter, and upon this rock I will build my church; and the gates of hell shall not prevail against it."),
    ("n4", NARRATOR, "His church, he called it — his own gathered people, built on a firm foundation, and so strong that not even the gates of death and darkness could ever overpower it or shut it down."),
    ("n5", NARRATOR, "That is a staggering promise. Empires would fall, storms would come, the powers of the grave itself would batter against it — and still it would stand, because its foundation was laid by God and not by men."),
    ("n6", NARRATOR, "But Jesus was not finished. He would not leave his church without a way to be led. So he turned to Peter and promised him something specific — real authority, handed down from heaven itself. He called it keys."),
    # Matthew 16:19
    ("kv19", JESUS, "And I will give unto thee the keys of the kingdom of heaven: and whatsoever thou shalt bind on earth shall be bound in heaven: and whatsoever thou shalt loose on earth shall be loosed in heaven."),
    ("n7", NARRATOR, "Keys open and close, lock and unlock, admit and secure. To hold the keys of the kingdom is to carry real authority to act in God's name, so that what is done rightly on earth is honoured in heaven — not invented by men, but given by the Lord."),
    ("n8", NARRATOR, "So Jesus did not leave his people leaderless, or his church without authority. He built it on rock and placed real keys in human hands. So the only question is a hopeful one. When you find that authority, given by him and not seized by men, will you trust it?"),
    ("card", NARRATOR, "Jesus built his church on rock and gave Peter the keys of the kingdom — real authority, binding on earth and in heaven, given by the Lord and not seized by men. When you find it, will you trust it?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN, speaker), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
