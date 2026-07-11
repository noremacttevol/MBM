#!/usr/bin/env python3
"""Generate narration audio for Story Video #12 — Blind Bartimaeus
(Mark 10:46-52).
Narrator: en-US-AndrewNeural — plain American, never Multilingual.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Mark 10:51 (j1), 10:52 (j2) — fetched from
bible-api.com (qc/mark10-kjv.txt), never hand-typed.
Pre-flighted on paper per PRODUCTION-BIBLE §4b — see PREFLIGHT.md.
Translation Law: no narrator line echoes KJV Jesus wording; the narrator
MAY quote Bartimaeus and the crowd modernly (their words, not his).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 — the road out of Jericho (s1). v46 setup + WHY-gem: Passover road.
    ("n0", NARRATOR, "-20%", "-4Hz",
     "The road out of Jericho, on a loud and dusty day. Jericho was the "
     "last stop before the climb up to Jerusalem, and with the Passover "
     "feast coming, that road carried half the country. For a beggar, "
     "crowds meant coins. And so a blind man named Bartimaeus sat where "
     "he always sat — at the edge of the highway, his ragged cloak "
     "spread across his lap to catch whatever fell, listening to a "
     "thousand feet walk past him. Listening was his whole life. He "
     "knew the road by its sounds."),
    # n1 — he hears the name (s2). v47a.
    ("n1", NARRATOR, "-20%", "-4Hz",
     "But this day the sound was different. A procession was coming out "
     "of the city — a moving wall of voices — and inside the noise he "
     "caught a name. Jesus of Nazareth was passing by. He had heard the "
     "stories everyone had heard: a teacher who opened deaf ears, who "
     "made lepers clean. Passing by, and never again. A blind man "
     "cannot chase a crowd. All he had was his voice."),
    # n2 — the shout (s3). v47b + the Son of David gem.
    ("n2", NARRATOR, "-22%", "-4Hz",
     "So he used it. He pulled in all the air his body would hold and "
     "shouted: Jesus, Son of David — have mercy on me! Catch that "
     "title. The crowd called him Jesus of Nazareth — the man from up "
     "north. Son of David was something else entirely: it was the name "
     "reserved for the promised King, the Messiah. Everyone with "
     "working eyes saw a traveling teacher. The blind man was the one "
     "who saw who was actually walking past."),
    # n3 — shouted down (s4). v48a + WHY the crowd hushed him.
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And the crowd turned on him. Many voices — Mark says many — told "
     "one desperate man to be quiet. Understand why: to them, a beggar "
     "screaming at a famous rabbi was an embarrassment, noise that "
     "needed hushing. Respectable people, telling a man in the dust "
     "that his need was bad manners."),
    # n4 — the held beat (s5). v48b. This line alone.
    ("n4", NARRATOR, "-26%", "-4Hz",
     "He shouted louder."),
    # n5 — the procession stops (s6). v49a. Music is thinning under this.
    ("n5", NARRATOR, "-24%", "-4Hz",
     "And Jesus stood still. The whole procession stopped around him — "
     "hundreds of feet going quiet in the dust. Remember where this "
     "road was taking him: up to Jerusalem, into the last week of his "
     "life. He was carrying all of that. And one blind beggar's voice — "
     "the voice everyone else was trying to shut off — stopped him in "
     "the road. He told them: call him over."),
    # n6 — the crowd's turnaround (s7). v49b — the crowd's line, modern.
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And listen to the crowd change its tune. The same voices that "
     "had been hushing him now crowded in with: take heart — get up! "
     "He is calling for you."),
    # n7 — the cloak (s8 still + Clip A). v50 + the cloak gem.
    ("n7", NARRATOR, "-22%", "-4Hz",
     "What happened next is one small verse, and it holds the whole "
     "man. He threw off his cloak, jumped up, and came. That cloak was "
     "a beggar's entire world — his coat, his bed at night, the very "
     "thing he spread out to catch the coins he lived on. A blind man "
     "who throws his cloak behind him may never find it again. He "
     "threw it anyway, coins and all. He spent everything he owned on "
     "the chance that the shout had been heard."),
    # n8 — standing before him (s9 setup). v51 lead-in.
    ("n8", NARRATOR, "-24%", "-4Hz",
     "So he came, hands out in front of him, through a corridor of "
     "staring people, and stood breathing hard in front of the man he "
     "could not see. And Jesus asked him one question:"),
    # J1 — exact KJV Mark 10:51.
    ("j1", JESUS, "-27%", "-6Hz",
     "What wilt thou that I should do unto thee?"),
    # n9 — bridge + his answer (s10a). Modern meaning only; no KJV echo.
    ("n9", NARRATOR, "-24%", "-4Hz",
     "As if it weren't obvious. A blind man, standing in a beggar's "
     "tunic. But he asked anyway — because he wanted the man's own "
     "voice, not the crowd's guess about him. Nobody had asked "
     "Bartimaeus what he wanted in a very long time. His answer came "
     "out in a breath: Rabbi — I want to see."),
    # J2 — exact KJV Mark 10:52. A breath of quiet before and after.
    ("j2", JESUS, "-27%", "-6Hz",
     "Go thy way; thy faith hath made thee whole."),
    # n10 — sight (s10b). v52a. Near-silence under this.
    ("n10", NARRATOR, "-26%", "-4Hz",
     "And immediately, Mark says, he saw. The clouds in his eyes "
     "cleared like silt settling out of water, and the first thing "
     "those new eyes ever held was daylight on the road ahead. Notice "
     "what Jesus told him: your trust did this — and you are free. "
     "Free to go anywhere."),
    # n11 — he followed (s11 still + Clip B). v52b + the ending gem.
    ("n11", NARRATOR, "-24%", "-4Hz",
     "And here is the ending Mark wants you to catch. Free to go "
     "anywhere, with brand new eyes and no cloak to go back for, he "
     "picked his road — the one Jesus was walking. He followed him, up "
     "the climb toward Jerusalem, staring at everything: the hills, "
     "the faces, his own two hands. The man who had been told to keep "
     "quiet walked in the middle of the procession that had hushed "
     "him."),
    # n12 — the closing card, read aloud gently (Readable-Card Law).
    ("n12", NARRATOR, "-26%", "-4Hz",
     "The crowd told him to keep quiet, and he shouted louder. What is "
     "the thing you would shout for, if no one could tell you to be "
     "quiet?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
