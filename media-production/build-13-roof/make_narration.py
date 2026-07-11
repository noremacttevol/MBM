#!/usr/bin/env python3
"""Generate narration audio for Story Video #13 — Through the Roof
(Mark 2:1-12).
Narrator: en-US-AndrewNeural — plain American, never Multilingual.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Mark 2:5 (j1), 2:9 (j2), 2:11 (j3) —
fetched from bible-api.com (qc/mark2-kjv.txt), never hand-typed.
Pre-flighted on paper per PRODUCTION-BIBLE §4b — see PREFLIGHT.md.
Translation Law: no narrator line echoes KJV Jesus wording; the narrator
may quote the SCRIBES' thought and the crowd's reaction modernly (v7,
v12 are their words, not his).
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 — carried through the streets (s1). v1-3 setup + the friends.
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Capernaum, on the north shore of the Sea of Galilee. Jesus was "
     "home — and the word got out. By the time four men came up the "
     "street carrying their friend on a sleeping mat, one at each "
     "corner, the house he was teaching in had already swallowed half "
     "the town. The man on the mat was paralyzed. He could not walk to "
     "Jesus. So the people who loved him decided he would get there "
     "anyway."),
    # n1 — no way through (s2). v2 + v4a.
    ("n1", NARRATOR, "-22%", "-4Hz",
     "But the doorway was a wall of backs. People packed the room, "
     "packed the doorway, spilled into the street — no one was giving "
     "up a spot, not even for a man on a mat. Four friends stood there "
     "breathing hard, holding their friend, staring at an impossible "
     "crowd. And then one of them looked up. At the roof."),
    # n2 — digging through (s3). v4 + the roof study-gem.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "Here is something worth knowing: houses there had flat roofs of "
     "packed clay over reeds and beams, with a stairway up the outside "
     "wall. You could dig through one with your hands in a few minutes "
     "— and patch it in a day. Which is exactly what they did. Four "
     "men on a stranger's roof, tearing through the clay, coughing in "
     "the dust, grinning at each other like men doing something "
     "magnificent and slightly insane."),
    # n3 — lowered into the light (s4 still + clip). v4b — the money shot.
    ("n3", NARRATOR, "-24%", "-4Hz",
     "Below them, in the middle of the sermon, the ceiling cracked "
     "open. Daylight poured into the dark room through falling dust "
     "and straw. And down through that column of light, swaying on "
     "four ropes, lowered with enormous care, came a man on a mat — "
     "landing right at the feet of Jesus."),
    # n4 — THEIR faith (s5). v5a — the Seed's hinge.
    ("n4", NARRATOR, "-24%", "-4Hz",
     "Now listen to what the story says next, because it is easy to "
     "miss. When Jesus saw their faith — theirs. The friends'. The "
     "four sweat-streaked faces ringing the hole in the roof. The man "
     "on the mat hadn't said a word. His friends' faith counted for "
     "him. He was carried there — and heaven honored the carrying."),
    # n5 — setup for j1 (s6). Music dies to silence at the end of this line.
    ("n5", NARRATOR, "-26%", "-4Hz",
     "And Jesus looked at the man lying in the dusty light — a man "
     "braced for words about his legs — and the first thing he said "
     "was not about his legs at all."),
    # J1 — exact KJV Mark 2:5. Spoken into TRUE SILENCE.
    ("j1", JESUS, "-30%", "-6Hz",
     "Son, thy sins be forgiven thee."),
    # n6 — the deepest wound first (s6). Pack bridge + WHY-gem.
    ("n6", NARRATOR, "-26%", "-4Hz",
     "The first word was son. Not a diagnosis. Not a lecture about his "
     "legs. Son — and then forgiveness. In that world, everyone "
     "assumed a body like his was the proof of some hidden guilt — he "
     "had carried the shame along with the paralysis his whole life. "
     "Jesus went to the deepest wound first. His legs had not moved "
     "yet. And it was already the miracle."),
    # n7 — the scribes (s7). v6-7 — narrator quotes THEIR thought modernly.
    ("n7", NARRATOR, "-22%", "-4Hz",
     "But in the corner sat the scribes — the religious experts — and "
     "nothing about this made them glad. They didn't say a word out "
     "loud. They reasoned it in their hearts: this is blasphemy. No "
     "one can forgive sins but God alone. And on the logic, they were "
     "exactly right. That was the point they refused to see."),
    # n8 — he answered their thoughts (s8 setup). v8 gem.
    ("n8", NARRATOR, "-24%", "-4Hz",
     "And then came the strangest moment in that room — stranger than "
     "the ceiling. Jesus knew what they were thinking. They had said "
     "nothing, and he answered them anyway:"),
    # J2 — exact KJV Mark 2:9.
    ("j2", JESUS, "-27%", "-6Hz",
     "Whether is it easier to say to the sick of the palsy, Thy sins "
     "be forgiven thee; or to say, Arise, and take up thy bed, and "
     "walk?"),
    # n9 — translation bridge (Translation Law) + v10 reason.
    ("n9", NARRATOR, "-24%", "-4Hz",
     "He was asking them: which is easier to say? Anyone can announce "
     "that sins are forgiven — no one can check. But tell a paralyzed "
     "man to stand, and everyone in the room finds out in a second "
     "what your words are worth. So — he said — so that you will know "
     "the forgiveness was real, watch this. He turned back to the man "
     "on the mat:"),
    # J3 — exact KJV Mark 2:11.
    ("j3", JESUS, "-28%", "-6Hz",
     "I say unto thee, Arise, and take up thy bed, and go thy way "
     "into thine house."),
    # n10 — he arose (s9 still + clip). v12a.
    ("n10", NARRATOR, "-22%", "-4Hz",
     "And immediately, he did. He stood — on legs trembling like a "
     "newborn colt's — while the crowd pulled back and the dust "
     "floated in the light. Then he bent down, rolled up his mat, and "
     "tucked it under his arm. The bed that had carried him, he "
     "carried home."),
    # n11 — out before them all (s10). v12b + roofline beat.
    ("n11", NARRATOR, "-22%", "-4Hz",
     "He walked out the door in front of everyone — through the same "
     "crowd that had no room for him an hour before. They made room "
     "now. Mark says they were all amazed, and gave the glory to God, "
     "and said to each other: we have never seen anything like this. "
     "And up on the roofline, four filthy, grinning friends pounded "
     "each other's shoulders and laughed toward heaven."),
    # n12 — the closing card, read aloud gently (Readable-Card Law).
    ("n12", NARRATOR, "-26%", "-4Hz",
     "Four people tore a roof open because their friend could not get "
     "there alone. His faith didn't carry him that day — theirs did, "
     "and heaven counted it. So here is the question this story "
     "leaves behind: where do you find yourself in that room? On the "
     "mat — or holding a rope?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
