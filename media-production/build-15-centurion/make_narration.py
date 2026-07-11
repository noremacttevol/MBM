#!/usr/bin/env python3
"""Generate narration audio for Story Video #15 — The Centurion's Servant
(Matthew 8:5-13).
Narrator: en-US-AndrewNeural — plain American, never Multilingual.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Matthew 8:7 (j1), 8:10 (j2), 8:11-12 (j2b),
8:13 (j3) — fetched from bible-api.com (qc/matthew8-kjv.txt), never hand-typed.
Pre-flighted on paper per PRODUCTION-BIBLE §4b — see PREFLIGHT.md.
Translation Law: no narrator line echoes Jesus's KJV wording; the narrator MAY
quote the CENTURION modernly (v6/v8/v9 — his words, not Jesus's).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 — Capernaum arrival (s1). v5 setting + the garrison-town WHY.
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Capernaum, a fishing town on the north shore of the Sea of Galilee. It "
     "was Jesus's home base — but it was also a garrison town, which meant "
     "Roman soldiers on the streets of a Jewish village. Rome was the "
     "occupying power. Its army was the boot on the neck of everyone who "
     "lived here. So when the man at the center of this story walks in, "
     "remember what uniform he is wearing."),
    # n1 — the sick servant (s2). v6 the need.
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Across town, in a Roman officer's house, a young servant lay dying. The "
     "word the text uses is palsy — his body had seized up, paralyzed, and he "
     "was in constant pain. In that world a servant was property; a sick one "
     "could simply be replaced. But this officer was not looking for a "
     "replacement. He had set his armor aside and was sitting with the boy, "
     "trying to help."),
    # n2 — the centurion comes (s3, Clip B). v5 + the study gems.
    ("n2", NARRATOR, "-21%", "-4Hz",
     "A centurion. The title means the commander of a hundred soldiers — a "
     "hard, career military man near the top of the local chain of command. "
     "And he came himself, in armor, to a Jewish teacher. Picture that street "
     "going silent as he walks it: the enemy's officer, moving through a "
     "village that had every reason to hate him. Another account tells us "
     "this particular Roman actually loved the Jewish people and had paid to "
     "build their synagogue — a rare soldier. And he came for a servant. Not "
     "a son, not an officer. A servant."),
    # n3 — the plea / humility posture (s4). v6, the bow.
    ("n3", NARRATOR, "-22%", "-4Hz",
     "He reached the teacher, and this commander of a hundred men bowed his "
     "head. His servant was at home, he said — paralyzed, in agony. Could "
     "something be done? He asked it plainly, the way a soldier makes a "
     "report: no performance, just the truth."),
    # J1 — exact KJV Matthew 8:7.
    ("j1", JESUS, "-27%", "-6Hz",
     "I will come and heal him."),
    # n4 — not worthy / say the word (s6). v8, the centurion's words modern.
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Jesus answered at once — he would come to the house himself. And that "
     "is where the Roman stopped him. He would not let him come. Lord, he "
     "said, I am not worthy to have you come under my roof. Only say the "
     "word, and my servant will be healed. By the custom of the day, a Jew "
     "who stepped inside a Gentile's house became unclean; the centurion "
     "knew it, and he would not put that on Jesus. But underneath the "
     "courtesy was something bigger."),
    # n5 — authority logic (s7). v9, the centurion's words modern.
    ("n5", NARRATOR, "-22%", "-4Hz",
     "He explained the faith behind it in the only language he knew — the "
     "chain of command. I am a man under authority myself, he said. I tell "
     "one soldier go, and he goes; another come, and he comes. I do not have "
     "to march them there. I speak, and it is done. He had watched his own "
     "words move men across a camp without lifting a hand. He believed this "
     "teacher's word could cross a whole town and move a disease just as "
     "surely. He did not need Jesus in the room. He only needed him to "
     "speak."),
    # n6 — Jesus marvels (s8). v10a. THE PEAK — music dies to silence here.
    ("n6", NARRATOR, "-24%", "-4Hz",
     "And Jesus marveled. Stop on that word. The Gospels almost never say "
     "Jesus was amazed by anyone — it happens twice: once at his own "
     "hometown, for how little they believed, and once here, for how much "
     "this outsider did. He turned to the crowd following him and said:"),
    # J2 — exact KJV Matthew 8:10. Lands in sacred quiet.
    ("j2", JESUS, "-27%", "-6Hz",
     "Verily I say unto you, I have not found so great faith, no, not in "
     "Israel."),
    # n7 — bridge to the opened door (s9). Modern force of "verily", no KJV echo.
    ("n7", NARRATOR, "-23%", "-4Hz",
     "Truly, he said — mark this. And he said it about a Roman officer, the "
     "enemy, a Gentile, in front of the very people who were certain that "
     "faith belonged to them and no one else. Then he opened the door wider "
     "than anyone standing there wanted it opened:"),
    # J2b — exact KJV Matthew 8:11-12.
    ("j2b", JESUS, "-27%", "-6Hz",
     "And I say unto you, That many shall come from the east and west, and "
     "shall sit down with Abraham, and Isaac, and Jacob, in the kingdom of "
     "heaven. But the children of the kingdom shall be cast out into outer "
     "darkness: there shall be weeping and gnashing of teeth."),
    # n8 — gentle plain meaning (s9). Handles v12 without threat; serves Seed.
    ("n8", NARRATOR, "-23%", "-4Hz",
     "He was saying that people would come from every direction — every "
     "nation, every kind of outsider — and take their place at God's table. "
     "And that being born into the right family, the right religion, the "
     "right group, was never the thing that saved anyone. Faith was. The "
     "centurion had it. That was the whole of it."),
    # n9 — j3 setup (s10).
    ("n9", NARRATOR, "-24%", "-4Hz",
     "Then Jesus turned back to the soldier and gave him the one thing he had "
     "asked for — a word."),
    # J3 — exact KJV Matthew 8:13a.
    ("j3", JESUS, "-27%", "-6Hz",
     "Go thy way; and as thou hast believed, so be it done unto thee."),
    # n10 — the walk home on a word + the healing (s11). v13b, selfsame hour.
    ("n10", NARRATOR, "-24%", "-4Hz",
     "Go home, he said — it is done, just as you believed. And notice: there "
     "was no proof yet. The officer had to turn around and walk the whole way "
     "back on nothing but that sentence. So he did. And in that same hour, "
     "across the town, in a room Jesus never entered, the young servant drew "
     "a sudden clean breath. The color came back into his face like dawn "
     "filling a room. His body loosened, and he sat up, whole — and no one "
     "was there to see it happen. It happened on a word spoken half a town "
     "away."),
    # n11 — the reunion (s12).
    ("n11", NARRATOR, "-23%", "-4Hz",
     "When the officer reached his door, his servant was on his feet to meet "
     "him — well, ordinary, alive. The hard-faced man who commanded a hundred "
     "soldiers put a hand over his mouth, and his composure quietly came "
     "apart. He had trusted a word, and the word had been enough."),
    # n12 — the closing card, read aloud gently (Readable-Card Law). Pack card
    # verbatim.
    ("n12", NARRATOR, "-26%", "-4Hz",
     "I am not worthy to have you under my roof — but say the word. Which "
     "half of that sentence is easier for you to say?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
