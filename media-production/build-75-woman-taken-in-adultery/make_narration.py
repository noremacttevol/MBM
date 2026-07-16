#!/usr/bin/env python3
"""Generate narration audio for Story Video #75 — The Woman Taken in Adultery
(John 8:1-11). Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 8:7, 8:10, 8:11 (fetched, not hand-typed; v10 and v11 are separate segments —
her reply "No man, Lord" is narrator-paraphrased, never voiced in KJV).
CONTENT-CARE (D,R): the accusation is named once, never dramatized; no violence, no
stone ever raised or in the air; no shame framing. Mercy spoken out loud in the KJV.
HOMOGRAPH LAW: no known offenders in these lines — SPOKEN empty; ear-check every
segment anyway before assembly. No music bed: narration + intentional silence only.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Early morning at the temple, Jesus was teaching a crowd, when a "
     "knot of religious leaders shoved their way through — dragging a "
     "woman with them."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "They stood her in the middle of everyone. They said she had been "
     "caught in adultery, and that the law of Moses said to stone her. "
     "Then they asked him: so, teacher — what do you say?"),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "It was a trap. Say let her go, and he breaks the law. Say stone "
     "her, and he's just another man with a rock."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Jesus said nothing at first. He bent down and wrote in the dust "
     "with his finger. Then he straightened up."),
    # Exact KJV John 8:7 — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "He that is without sin among you, let him first cast a stone at "
     "her."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "And he bent down and wrote again. They dropped their stones and "
     "walked away, one by one — the oldest first — until it was only "
     "the two of them."),
    # Exact KJV John 8:10 — sacred pause around it.
    ("j2", JESUS, "-20%", "-2Hz",
     "Woman, where are those thine accusers? hath no man condemned "
     "thee?"),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "She looked up at him. No one, sir, she said."),
    # Exact KJV John 8:11 — SILENCE around it.
    ("j3", JESUS, "-18%", "-2Hz",
     "Neither do I condemn thee: go, and sin no more."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "The only one with the right to condemn her, wouldn't. What would "
     "it change to hear him say that to you?"),
]

# HOMOGRAPH LAW — no bow/wound/wind/tears/lead/sow/live/read in these segments;
# SPOKEN stays empty. Ear-check every segment before assembly regardless.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
