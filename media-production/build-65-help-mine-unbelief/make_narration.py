#!/usr/bin/env python3
"""Generate narration audio for Story Video #65 — "Help thou mine unbelief" (Mark 9:14-29).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV: Mark 9:23, 9:25.
The FATHER'S cry (Mark 9:24) is the title line — read by the scripture voice as an
exact quotation, framed clearly by the narrator so it is unmistakably the father,
not Jesus (build-169 scripture-voice precedent).
CONTENT-CARE (A,R,G): NO embodied devil ever; the seizure is ONE restrained beat —
the father's face is the shot, not the boy's suffering; the boy is shown distressed
but never grotesque, and ends calm and whole.
HOMOGRAPH LAW: ear-check list scanned; no offenders voiced.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.
SCRIPTURE = JESUS                   # scripture-quote voice (the father's exact KJV line)

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus came down from the mountain and walked straight into a "
     "mess. A crowd was arguing. His own disciples were in the middle "
     "of it, cornered and embarrassed — because a desperate father had "
     "brought them his son, and for once, they could not help. They "
     "had tried. Nothing happened. And everyone was watching them "
     "fail."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The father pushed through to Jesus and told him the whole story. "
     "His only son had been tormented since he was little — thrown "
     "down, unable to speak, hurt again and again by something the "
     "family could not fight. Years of it. A father who had watched "
     "his boy suffer his entire childhood and could do nothing."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "And then he said the most honest thing in the story. He looked "
     "at Jesus and said: if you can do anything — anything at all — "
     "have compassion on us, and help us. If. After all those years "
     "of disappointment, hope had gotten expensive. Listen to how "
     "Jesus answered that trembling little word IF:"),
    # Exact KJV Mark 9:23 — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "If thou canst believe, all things are possible to him that "
     "believeth."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "And now comes the moment this whole story is remembered for. "
     "The father did not pretend. He did not put on a brave "
     "religious face and claim a faith he did not fully have. He did "
     "something braver. He cried out the truest prayer in the Bible "
     "for anyone who has ever wanted to believe and struggled to:"),
    # Exact KJV Mark 9:24 — the FATHER'S cry (scripture-voice, framed). SILENCE.
    ("fv1", SCRIPTURE, "-22%", "-4Hz",
     "Lord, I believe; help thou mine unbelief."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "Think about what he just did. He brought Jesus the little bit "
     "of faith he had AND the unbelief he was ashamed of — and laid "
     "both of them down. He did not wait to believe perfectly before "
     "he asked. He asked for help WITH his believing. And that — that "
     "cracked-open, honest, half-full faith — was enough."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "Jesus saw the crowd rushing in to gawk, and he did not wait. He "
     "spoke directly to the thing that had stolen this boy's whole "
     "childhood, and commanded it, once and for all:"),
    # Exact KJV Mark 9:25 — SILENCE around it.
    ("j2", JESUS, "-18%", "-2Hz",
     "Thou dumb and deaf spirit, I charge thee, come out of him, and "
     "enter no more into him."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "It left. The boy went so still that people whispered he was "
     "dead. But Jesus reached down, took him by the hand, and lifted "
     "him up — and the boy stood, quiet and whole, and gave him back "
     "to his father. The tormented childhood was over. It ended with "
     "a hand reaching down into the dust to pull a son to his feet."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "Later, alone, the disciples asked why they had failed. And "
     "Jesus told them this kind only comes out by prayer — meaning "
     "this was never about their technique. It was about who they "
     "were leaning on. The father got it right without knowing the "
     "rules: he stopped trying to be strong, and just brought his "
     "weakness to the only one who could carry it."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "You do not need perfect faith to come to him. Bring the little "
     "you have — and the doubt you're ashamed of — and ask him to "
     "help you believe. That prayer has never been turned away."),
]

# HOMOGRAPH LAW — scanned: no bow/wound/wind/tears/lead/sow/live(s)/read/dove/
# bass/minute/use(d)/close voiced. ("tears" avoided.) No overrides needed.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
