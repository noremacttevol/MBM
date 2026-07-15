#!/usr/bin/env python3
"""Generate narration audio for Story Video #72 — Calling Matthew (Matthew 9:9-13).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Two lines:
  j1 = Matthew 9:9      "Follow me." — the call, sacred silence 1
  j2 = Matthew 9:12-13  "They that be whole need not a physician... I am not come to
       call the righteous, but sinners to repentance." — THE heart line, the verse
       card, sacred silence 2.

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS and
word-wraps each text as the on-screen caption.

TRANSLATION LAW: after each KJV line the narrator gives only the plain modern meaning
and never re-quotes or echoes the KJV wording — n9 says "a doctor goes where the
sickness is" instead of repeating "physician/whole/sick", and explains "mercy, not
sacrifice" (n10) without quoting the phrase back.

WHY-LAW — this is the gospel in one scene, and the whole job is that the KINDNESS lands
without a drop of shame:
  1. Jesus goes TO the most hated man in town (n1-n3) — a tax collector, a collaborator
     who got rich cheating his neighbors — and calls him with NO conditions (n4).
  2. He eats with a whole room of outcasts (n6-n7) on purpose, and when the religious
     object (n8) he says the doctor goes where the sickness is (j2, n9).
  3. The turn (n10): the outcasts were near him because they knew they needed him; the
     righteous stood outside because they were sure they didn't. Self-sufficiency, not
     sin, is what keeps a person from the table.

"Sinners" and "outcasts" are named plainly but the guests are always drawn and spoken of
as human beings the town wrote off, NEVER as villains or grotesques. The Pharisees are
sincere, not cruel. No shame framing anywhere.

NUMBER-STRESS LAW: no sentence opens with a bare number. "one of the four accounts of
his life" lands the count mid-sentence (n11).

CLOSING CARD IS AN INVITATION, never a fear-question. The card's question reassures — if
the door was open that wide for the man the whole town wrote off, it is not closed to you.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: who Matthew was ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "There was one job in every Galilee town that made you a traitor to your own "
     "people. Tax collector. You worked for Rome, the empire occupying your homeland, "
     "and you got rich taking money from your neighbors, most of it more than Rome "
     "even asked. Matthew had that job."),
    # --- s2: rich and alone ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "So Matthew had money, and Matthew had no one. The devout would not touch him. "
     "His old friends were long gone. He sat at his booth by the road every day, "
     "counting silver, while the whole town walked a little wider around him. Rich, "
     "and completely alone."),
    # --- s3: Jesus walks up to him ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And this is the man Jesus walked up to. Not around. Up to. Past everyone who "
     "would have been a safer, more respectable choice, straight to the booth nobody "
     "else wanted to stand near."),
    # --- s4: v9 — the call. Sacred silence 1. ---
    ("j1", JESUS, "-26%", "-6Hz",
     "Follow me."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Two words. And notice what is missing from them. No pay it all back first. No "
     "prove you have changed. No list of conditions to clear before he was allowed to "
     "come. Just, come."),
    # --- s5: he arose and left the money ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And Matthew got up and left it. The coins, the scales, the ledgers, the whole "
     "profitable, lonely life, sitting right there on the table. He walked away from "
     "all of it that afternoon, and followed him."),
    # --- s6: the feast ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And then something even stranger. Jesus went to Matthew's house for dinner. And "
     "the room filled up with Matthew's kind of people. Other tax collectors. "
     "Outcasts. The men and women the rest of the town had quietly given up on. And "
     "he sat down in the middle of them and ate."),
    # --- s7: who they were ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Look at who is at that table. Not the respectable. Not the qualified. The people "
     "who were used to being turned away at every door, finding themselves, for once, "
     "welcome. You can see it on their faces."),
    # --- s8: the objection ---
    ("n8", NARRATOR, "-22%", "-4Hz",
     "The religious men could not stand it. They stood at the door, too clean to come "
     "in, and asked his disciples the question that gave the whole thing away. Why "
     "does your teacher eat with people like that?"),
    # --- s9: vv12-13 — THE heart line. Sacred silence 2. ---
    ("j2", JESUS, "-28%", "-6Hz",
     "They that be whole need not a physician, but they that are sick. But go ye and "
     "learn what that meaneth, I will have mercy, and not sacrifice: for I am not come "
     "to call the righteous, but sinners to repentance."),
    ("n9", NARRATOR, "-22%", "-4Hz",
     "A doctor does not spend his day with the healthy. He goes where the sickness is. "
     "That was his whole answer. He did not come for the people who had it all "
     "together. He came for the ones who knew that they did not."),
    # --- s10: the turn ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "And that is the quiet turn in the story. The outcasts were close to him because "
     "they knew they needed him. The religious men stood outside, arms folded, because "
     "they were sure they did not. The only thing that kept anyone from that table was "
     "believing they were already fine."),
    # --- s11: Matthew the writer ---
    ("n11", NARRATOR, "-22%", "-4Hz",
     "As for Matthew, the man who had spent his life writing down what other people "
     "owed became a writer of a very different kind: one of the four accounts of "
     "Jesus's life we still read today came from his pen, the Gospel of the tax "
     "collector nobody wanted. That is what the call did to him."),
    # --- s12: the invitation ---
    ("n12", NARRATOR, "-24%", "-4Hz",
     "And the table he sat at is still set. The same door is still open, the same "
     "welcome still held out to exactly the people who assume they would never be let "
     "in. He is not waiting for you to qualify. He is asking you to come and eat."),
    # --- closing card, read gently (Readable-Card Law). An INVITATION. ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "He walked past every respectable man in town to sit down with the one nobody "
     "else would. If the door was open that wide for the man the whole town had "
     "written off, what makes you think it is closed to you?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
