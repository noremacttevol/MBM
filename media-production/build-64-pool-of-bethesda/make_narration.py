#!/usr/bin/env python3
"""Generate narration audio for Story Video #64 — The Pool of Bethesda (John 5:1-16).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
John 5:6b and 5:8 (fetched, not hand-typed).
GREEN story. The 5:14 warning line is not used (no shame framing); the story
ends on wholeness, the sabbath stir, and grace-before-faith (5:13).
Homograph ear-check list scanned; no offenders used.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "By the sheep gate in Jerusalem there was a pool called Bethesda, "
     "ringed by five covered porches. And those porches were full of "
     "the city's most hopeless people — the blind, the lame, the "
     "paralyzed — all waiting on a legend: every so often the water "
     "stirred, and the first one in, people said, would be healed. "
     "Imagine the math of that place. Hundreds waiting. One winner. "
     "And the fastest one wins a race for the people who can't run."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "One man had been lying there thirty-eight years. Let that "
     "number land. That was longer than most people in that world "
     "even got to be alive. Whole generations had grown up and grown "
     "old while he lay on that mat, watching the water, losing the "
     "same race every time. By now, being the sick man by the pool "
     "was not just his condition. It was his whole identity."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Jesus walked those porches, past hundreds of the suffering, and "
     "stopped at this one man. John says he knew — knew he had been "
     "there a long time. And then he asked him a question that sounds "
     "almost unkind, until you sit with it:"),
    # Exact KJV John 5:6b — SILENCE around it.
    ("j1", JESUS, "-20%", "-2Hz",
     "Wilt thou be made whole?"),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Do you want to be well? After thirty-eight years, that is a real "
     "question. Healing would mean a new name, new work, a whole new "
     "life — and no more excuse. And notice: the man does not answer "
     "yes. He answers with the obstacle. Sir, I have no one to put me "
     "in the water — someone always gets there first. He explains the "
     "system. Jesus was not asking about the system."),
    # Exact KJV John 5:8 — SILENCE around it.
    ("j2", JESUS, "-18%", "-2Hz",
     "Rise, take up thy bed, and walk."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "No angel. No water. No race. The pool had nothing to do with "
     "it. And immediately the man was made whole — thirty-eight years "
     "of atrophy gone between one breath and the next. Legs that had "
     "forgotten what weight felt like took his weight. He stood up, "
     "rolled up the mat that had been his whole world, and walked."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "It was the sabbath, so the rule-keepers stopped him at once — "
     "not to celebrate him, but to tell him carrying a mat was not "
     "allowed. And here is the astonishing part: when they asked who "
     "had healed him, he did not know. He had never asked the name. "
     "Jesus had healed a man who could not identify him, had not "
     "followed him, had not even clearly said yes. Grace came first. "
     "Everything else came after."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "Later, Jesus found him in the temple — found him, again, the "
     "way he found the man born blind — and only then did the man "
     "learn the name of the one who had given him his life back. He "
     "went and told everyone: it was Jesus."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "Thirty-eight years, and one question. Not: why are you still "
     "here. Not: whose fault is this. Just — do you want to be "
     "whole? The pool never healed anybody. The person standing next "
     "to that man did."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "However long it has been for you — he is not put off by the "
     "years. He is still asking: do you want to be whole?"),
]

# HOMOGRAPH LAW — scanned: no bow/wound/wind/tears/lead/sow/live(s)/read/dove/
# bass/minute/use(d)/close in any segment. No overrides needed.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
