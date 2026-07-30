#!/usr/bin/env python3
"""Narration for build-13-roof — Mark 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Mark 2:1-12. j1, j2 and j3 are Jesus in the flesh and all three stay RED.
Two verbatim lines by other people were only paraphrased and are now SCRIPTURE (blue):
  s7   Mark 2:7   the scribes reasoning in their hearts: 'Why doth this man thus
       speak blasphemies? who can forgive sins but God only?'
  s12  Mark 2:12  the crowd: 'We never saw it on this fashion.'
n10 was one audio across two different stills and is split at the old caption
boundary into n10 and n10b. n12 is the closing card and keeps its id.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    # coverage 2026-07-29: n0 split after "the word got out" so the new Capernaum
    # establishing still can carry the opening (split_segment.py, approved mp3 cut).
    ("n0", NARRATOR, "Capernaum, on the north shore of the Sea of Galilee. Jesus was home — and the word got out."),
    ("n0b", NARRATOR, "By the time four men came up the street carrying their friend on a sleeping mat, one at each corner, the house he was teaching in had already swallowed half the town. The man on the mat was paralyzed. He could not walk to Jesus. So the people who loved him decided he would get there anyway."),
    ("n1", NARRATOR, "But the doorway was a wall of backs. People packed the room, packed the doorway, spilled into the street — no one was giving up a spot, not even for a man on a mat. Four friends stood there breathing hard, holding their friend, staring at an impossible crowd. And then one of them looked up. At the roof."),
    # coverage 2026-07-29: n2 split after the stairway sentence so the new
    # outside-stair still carries it; the digging stays on the digging still.
    ("n2", NARRATOR, "Here is something worth knowing: houses there had flat roofs of packed clay over reeds and beams, with a stairway up the outside wall."),
    ("n2b", NARRATOR, "You could dig through one with your hands in a few minutes — and patch it in a day. Which is exactly what they did. Four men on a stranger's roof, tearing through the clay, coughing in the dust, grinning at each other like men doing something magnificent and slightly insane."),
    ("n3", NARRATOR, "Below them, in the middle of the sermon, the ceiling cracked open. Daylight poured into the dark room through falling dust and straw. And down through that column of light, swaying on four ropes, lowered with enormous care, came a man on a mat — landing right at the feet of Jesus."),
    ("n4", NARRATOR, "Now listen to what the story says next, because it is easy to miss. When Jesus saw their faith — theirs. The friends'. The four sweat-streaked faces ringing the hole in the roof. The man on the mat hadn't said a word. His friends' faith counted for him. He was carried there — and heaven honored the carrying."),
    ("n5", NARRATOR, "And Jesus looked at the man lying in the dusty light — a man braced for words about his legs — and the first thing he said was not about his legs at all."),
    # Mark 2:5
    ("j1", JESUS, "Son, thy sins be forgiven thee."),
    # coverage 2026-07-29: n6 split three ways (split_segment.py x2, approved mp3
    # cuts) — "the first word was son" on the new close-up, the shame memory on
    # the new sepia flashback, "the deepest wound" back on the deepest-wound still.
    ("n6", NARRATOR, "The first word was son. Not a diagnosis. Not a lecture about his legs. Son — and then forgiveness."),
    ("n6b", NARRATOR, "In that world, everyone assumed a body like his was the proof of some hidden guilt — he had carried the shame along with the paralysis his whole life."),
    ("n6c", NARRATOR, "Jesus went to the deepest wound first. His legs had not moved yet. And it was already the miracle."),
    ("n7", NARRATOR, "But in the corner sat the scribes — the religious experts — and nothing about this made them glad. They didn't say a word out loud. They reasoned it in their hearts: this is blasphemy. And on the logic, they were exactly right. That was the point they refused to see."),
    # Mark 2:7
    ("s7", SCRIPTURE, "Why doth this man thus speak blasphemies? who can forgive sins but God only?"),
    ("n8", NARRATOR, "And then came the strangest moment in that room — stranger than the ceiling. Jesus knew what they were thinking. They had said nothing, and he answered them anyway:"),
    # Mark 2:9
    ("j2", JESUS, "Whether is it easier to say to the sick of the palsy, Thy sins be forgiven thee; or to say, Arise, and take up thy bed, and walk?"),
    ("n9", NARRATOR, "He was asking them: which is easier to say? Anyone can announce that sins are forgiven — no one can check. But tell a paralyzed man to stand, and everyone in the room finds out in a second what your words are worth. So — he said — so that you will know the forgiveness was real, watch this. He turned back to the man on the mat:"),
    # Mark 2:11
    ("j3", JESUS, "I say unto thee, Arise, and take up thy bed, and go thy way into thine house."),
    ("n10", NARRATOR, "And immediately, he did. He stood — on legs trembling like a newborn colt's — while the crowd pulled back and the dust floated in the light."),
    ("n10b", NARRATOR, "Then he bent down, rolled up his mat, and tucked it under his arm. The bed that had carried him, he carried home."),
    ("n11", NARRATOR, "He walked out the door in front of everyone — through the same crowd that had no room for him an hour before. They made room now. Mark says they were all amazed, and gave the glory to God, and said to each other: we have never seen anything like this. And up on the roofline, four filthy, grinning friends pounded each other's shoulders and laughed toward heaven."),
    # Mark 2:12
    ("s12", SCRIPTURE, "We never saw it on this fashion."),
    ("n12", NARRATOR, "Four people tore a roof open because their friend could not get there alone. His faith didn't carry him that day — theirs did, and heaven counted it. So here is the question this story leaves behind: where do you find yourself in that room? On the mat — or holding a rope?"),
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
