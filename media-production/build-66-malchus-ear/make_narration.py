#!/usr/bin/env python3
"""Generate narration audio for Story Video #66 — Malchus's Ear (Luke 22:47-51 / Matt 26).
Narrator: modern, warm, low, unhurried (American). Plain US model only.
Jesus voice: AMERICAN, never British. Jesus speaks ONLY exact KJV:
Matt 26:52 (put up thy sword) and Luke 22:51 (suffer ye thus far).
CONTENT-CARE (R): the sword-stroke and the severed ear are NEVER depicted — the cut
is implied only; the picture is the drawn sword lowered, the healing touch, and the
servant's wonder. No blood, no gore, no fear framing — the point is mercy to an enemy.
HOMOGRAPH LAW: ear-check list scanned; "wound" avoided; no offenders voiced.

Narration expanded 2026-07-17 by L1 (WHY-law + STUDY-GEM: Peter's math, twelve legions,
'put up thy sword', what Malchus carried home). Built on W1-STILLS's 7-shot PROMPTS.md.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — maps to W1-STILLS's 7 shots (s1-s7)
    ("n0", NARRATOR, "-20%", "-4Hz",
     "It was the middle of the night, in a garden called Gethsemane. "
     "Jesus had just finished praying — and now torchlight was coming "
     "up the hill. A mob, sent by the chief priests, armed with swords "
     "and clubs, led by one of his own friends, come to arrest him. "
     "This was the moment everything turned."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "And Peter could not stand it. Impulsive, loyal, terrified Peter "
     "grabbed a sword and swung — meaning, surely, to defend the man "
     "he loved. He caught the servant of the high priest, a man named "
     "Malchus, and cut off his ear. In one second, the whole night was "
     "about to become a massacre."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Understand Peter's math. Twelve tired men against an armed mob. "
     "He was not being smart — he was being brave and wrong, ready to "
     "die swinging for Jesus. And most leaders, in that moment, would "
     "have let him. But Jesus stopped everything. First, he stopped "
     "Peter:"),
    # Exact KJV Matt 26:52 — SILENCE around it. (Shot s3: Jesus steps in, hand raised.)
    ("j1", JESUS, "-20%", "-2Hz",
     "Put up again thy sword into his place: for all they that take "
     "the sword shall perish with the sword."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "Put it away, Peter. This is not that kind of kingdom. He said he "
     "could call down more than twelve legions of angels this instant "
     "if rescue were the plan — but rescue was not the plan. He was "
     "not being overpowered in a garden. He was laying his life down "
     "on purpose, and he would not spill one drop of someone else's "
     "blood to save his own."),
    ("n4", NARRATOR, "-20%", "-4Hz",
     "And then he did the most extraordinary thing in the whole "
     "arrest. With the mob closing in to seize him, with his own death "
     "now minutes away, Jesus turned to the injured man. Not his "
     "friend. His enemy — one of the very people who had come for him. "
     "And he said:"),
    # Exact KJV Luke 22:51 — SILENCE around it. (Shot s4: the healing touch.)
    ("j2", JESUS, "-20%", "-2Hz",
     "Suffer ye thus far."),
    ("n5", NARRATOR, "-20%", "-4Hz",
     "Let me do this one last thing. And he reached out, touched the "
     "side of the man's head, and made him whole. The last miracle "
     "Jesus performed as a free man was healing an injury done by his "
     "own defender, to one of the men arresting him."),
    ("n6", NARRATOR, "-20%", "-4Hz",
     "Think about what Malchus carried home that night. He had come "
     "with a mob to seize a man — and that man healed him. Whatever he "
     "had believed walking up that hill, he walked back down it whole, "
     "touched by the very person he came to hurt. You do not forget a "
     "thing like that."),
    ("n7", NARRATOR, "-20%", "-4Hz",
     "This is who he is, even at his own arrest, even on the worst "
     "night of his life: he will not let the moment be about violence. "
     "He heals the hand raised against him. There is no one on the "
     "wrong side of the sword he is unwilling to reach toward."),
    ("card", NARRATOR, "-22%", "-5Hz",
     "He healed the man sent to seize him. There is no enemy too far "
     "for his mercy — including the one you're afraid is in you."),
]

# HOMOGRAPH LAW — scanned: no bow/wound/wind/tears/lead/sow/live(s)/read/dove/
# bass/minute/use(d)/close voiced. ("wound" avoided — used "injury/cut".) No overrides.
SPOKEN = {}


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts_text = SPOKEN.get(name, text)
        tts = edge_tts.Communicate(tts_text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
