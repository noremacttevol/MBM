#!/usr/bin/env python3
"""Generate narration audio for Story Video #17 — The Raising of Lazarus
(John 11:1-44).
Narrator: en-US-AndrewNeural — plain American, never Multilingual.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: John 11:4 (j1), 11:25-26 (j2), 11:40 (j3),
11:43 (j4), 11:44b (j5) — from qc/john11-kjv.txt, never hand-typed.
Translation Law: no narrator line echoes KJV Jesus wording; the narrator
MAY paraphrase the sisters and mourners modernly (their words, not his).
Two standards: STILLS-ONLY (Law E) + Jesus face-never (#18).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 — Bethany, the family he loved; the sisters send word (s1). vv1-3.
    ("n0", NARRATOR, "-20%", "-4Hz",
     "In a village called Bethany, close enough to Jerusalem to walk, "
     "there lived two sisters, Martha and Mary, and their brother "
     "Lazarus. Jesus loved this family. Their home was the one place on "
     "the whole road where he could stop being a public figure and "
     "simply be a friend. And now their brother was dying. So the "
     "sisters sent word to Jesus — not a demand, just a few aching "
     "words: Lord, the one you love is sick."),
    # n1 — the strange delay + j1 (s2). v6 + v4.
    ("n1", NARRATOR, "-22%", "-4Hz",
     "You would expect him to drop everything and run. He did the "
     "opposite. When the news reached him, he stayed where he was two "
     "more days. But listen to what he said about it:"),
    ("j1", JESUS, "-27%", "-6Hz",
     "This sickness is not unto death, but for the glory of God, that "
     "the Son of God might be glorified thereby."),
    ("n1b", NARRATOR, "-22%", "-4Hz",
     "He was not being careless with the people he loved. He was "
     "reaching for something deeper than a quick rescue — something "
     "that would show everyone who he really was. And it would cost "
     "those two sisters four days of grief to see it."),
    # n2 — four days dead (s3). v17 + the WHY-gem about the fourth day.
    ("n2", NARRATOR, "-22%", "-4Hz",
     "By the time Jesus started for Bethany, the message had changed. "
     "Lazarus was not sick anymore. Lazarus was dead, and had been "
     "sealed in the tomb four days. That number is in the story on "
     "purpose. People of that time held that a soul might linger near "
     "the body for three days. Four days meant the door was shut — no "
     "lingering, no hope, no loophole left. Everyone in Bethany knew "
     "exactly how final four days was."),
    # n3 — Martha runs to the road (s4). v21 + v22, her words modernly.
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Martha heard he was finally near and ran out to meet him on the "
     "road, before he even reached the town. What she said was grief "
     "and faith tangled together in one breath: Lord, if you had been "
     "here, my brother would not have died. And then, still holding "
     "on — but even now, I know God will give you whatever you ask."),
    # n4 — thy brother shall rise -> the pivot into j2 (s5). vv23-24.
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Jesus told her, your brother will rise again. Martha nodded the "
     "way we nod at things we believe but cannot feel — yes, at the "
     "end of the world, on the last day, I know. And Jesus took the "
     "whole promise out of the far-off future and set it down in the "
     "person standing right in front of her:"),
    # J2 — exact KJV John 11:25-26 (the theological peak). In near-silence.
    ("j2", JESUS, "-28%", "-6Hz",
     "I am the resurrection, and the life: he that believeth in me, "
     "though he were dead, yet shall he live: And whosoever liveth and "
     "believeth in me shall never die. Believest thou this?"),
    # n5 — Mary comes and weeps (s6 setup). vv28-33, modern.
    ("n5", NARRATOR, "-22%", "-4Hz",
     "He did not offer her a doctrine to file away until the last day. "
     "He offered her himself, right there in the dust of the road. "
     "Then Mary came — the quieter sister — and she fell at his feet "
     "and wept, and every mourner who had followed her out wept too. "
     "The whole road dissolved into grief."),
    # n6 — Jesus wept (s6). v35 — the gem. Narrator describes; not spoken.
    ("n6", NARRATOR, "-24%", "-4Hz",
     "And then comes the shortest verse in the whole Bible, and one of "
     "the most staggering. Jesus wept. Sit with that. The one man there "
     "who knew — knew — that in a few minutes Lazarus would be breathing "
     "again, stood at the grave of his friend and cried. Not because he "
     "had run out of options. He cried because the people he loved were "
     "broken, and death is a horror, and he would not stand there "
     "pretending it wasn't. He did not skip the grief. He walked all the "
     "way into it with them."),
    # n7 — the tomb, take away the stone, + j3 (s7). vv38-40.
    ("n7", NARRATOR, "-22%", "-4Hz",
     "The tomb was a cave with a heavy stone rolled across its mouth. "
     "Jesus said, take away the stone. Practical, careful Martha "
     "panicked — Lord, by now there will be a smell, it has been four "
     "days. And Jesus answered her:"),
    ("j3", JESUS, "-27%", "-6Hz",
     "Said I not unto thee, that, if thou wouldest believe, thou "
     "shouldest see the glory of God?"),
    ("n7b", NARRATOR, "-24%", "-4Hz",
     "So they leaned into the great stone and rolled it back, and the "
     "dark mouth of the grave stood open to the daylight."),
    # n8 — he prayed aloud, then called + j4 (s8 — THE MIRACLE).
    ("n8", NARRATOR, "-22%", "-4Hz",
     "He lifted his eyes and prayed out loud — not because heaven was "
     "hard of hearing, but because he wanted the crowd to know exactly "
     "where the power came from. And then he called into the dark, in a "
     "voice they said was loud enough to wake the dead:"),
    ("j4", JESUS, "-24%", "-6Hz",
     "Lazarus, come forth."),
    # n9 — the dead man comes out (s8 hold). v44a.
    ("n9", NARRATOR, "-24%", "-4Hz",
     "And the dead man came out. Bound hand and foot in strips of "
     "grave-linen, his face still wrapped, Lazarus stood in the mouth "
     "of his own tomb — alive. Four days gone, and standing in the "
     "light. Nobody moved. Nobody breathed."),
    # J5 — exact KJV John 11:44b (s9 — the release).
    ("j5", JESUS, "-26%", "-6Hz",
     "Loose him, and let him go."),
    # n10 — the seed / the gospel (s9 hold). the meaning.
    ("n10", NARRATOR, "-24%", "-4Hz",
     "Unwrap him. Take the grave-linen off a living man and let him "
     "walk home to dinner. This was the last great sign before Jesus "
     "turned toward his own cross — and he did it in the open, at a "
     "marked grave, in front of a crowd, so that no one could ever call "
     "it a trick of the light. The one who stands over every grave you "
     "have ever wept beside looked death full in the face and called a "
     "friend home. He does not merely explain the resurrection. He is "
     "the resurrection."),
    # n11 — the closing card, read aloud gently (Readable-Card Law).
    ("n11", NARRATOR, "-26%", "-4Hz",
     "He wept at the grave, even though he was about to open it. Is "
     "there a grief you are carrying that he would not rush you past, "
     "but would sit down inside it, and weep there with you first?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
