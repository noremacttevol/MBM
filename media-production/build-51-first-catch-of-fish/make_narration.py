#!/usr/bin/env python3
"""Narration for build-51-first-catch-of-fish — Luke 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

PETER WAS THE HEART OF THIS VIDEO AND HE NEVER GOT TO SPEAK. Both of his lines
-- the two sentences everybody remembers from Luke 5 -- were narrator paraphrase
in white. Both are now lifted out verbatim as SCRIPTURE (light blue -- he is a man
in the story, not Deity), each on the SAME still the paraphrase already used:
  s5  Luke 5:5  'Master, we have toiled all the night, and have taken nothing:
      nevertheless at thy word I will let down the net.'
      This was the tail of n3, on S4, the still literally named s4-toiled-all-
      night. n3 keeps its id, trimmed to the frame, and a new n3b retells it.
      'Nevertheless at thy word' is the hinge of the whole story and it was being
      delivered in modern English by the storyteller.
  s8  Luke 5:8  'Depart from me; for I am a sinful man, O Lord.'
      This was buried in the middle of n6, on S7, s7-at-his-knees. n6 keeps its id,
      trimmed to the frame, and n6b carries the retelling and n6's closing line
      about what the wonder had shown him.

STAYED RED, BOTH. jv4 (Luke 5:4, 'Launch out into the deep, and let down your nets
for a draught') and jv10 (Luke 5:10, 'Fear not; from henceforth thou shalt catch
men') are Jesus in the flesh and a red-letter KJV inks both. Neither carried
Luke's framing, so neither needed splitting.

NO GREEN. Nothing in Luke 5:1-11 is the Father speaking.

WOMEN: Luke 5:1-11 records no woman speaking. Nothing added; nothing invented.

RETELLING RULE: jv4 by n3, s5 by n3b, s8 by n6b, jv10 by n7. Note jv4 is now
followed directly by n3, which is the frame for Peter's answer -- storyteller
between the two Old English blocks, as the law requires.

PRONUNCIATION: 'Gennesaret' in n1 and 'draught' in jv4 are both real risks with
this voice, but I do not know what respelling the existing build already uses and
the law says a bad respelling is worse than none. Left `spoken` empty and flagging
it here rather than guessing.

WHY-LAW: he met them at their emptiest -- a whole night of work and nothing to
show -- filled their hands past overflowing, and then asked for all of it. Milk:
the man who begged him to leave is the exact man he wanted.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "By the lake of Gennesaret, a crowd pressed in around him, hungry to hear the word of God. Two empty boats sat at the water's edge, and beside them tired fishermen were washing out their nets after a long night that had given them nothing."),
    ("n2", NARRATOR, "He stepped into one of the boats. It belonged to a fisherman named Simon. He asked him to push out a little way from the shore, and then he sat down and taught the people from the water."),
    # Luke 5:4
    ("jv4", JESUS, "Launch out into the deep, and let down your nets for a draught."),
    ("n3", NARRATOR, "Simon was bone-tired. They had worked that water all night and come back with nothing, and every instinct a fisherman has told him this was pointless. But something about this man made him answer the way he did."),
    # Luke 5:5
    ("s5", SCRIPTURE, "Master, we have toiled all the night, and have taken nothing: nevertheless at thy word I will let down the net."),
    ("n3b", NARRATOR, "Master, we worked that lake all night and caught nothing. But because you say so, I will put the net down again. Hear the word in the middle of that sentence. Nevertheless. He had every reason to say no, and he did it anyway."),
    ("n4", NARRATOR, "The moment the nets went down, they filled. A great shining mass of fish, far more than the ropes were made to hold, and the net began to tear under the sheer weight of it."),
    ("n5", NARRATOR, "There were too many for one boat. They waved to their partners, James and John, in the other boat to come and help, and both boats were loaded until they sat low in the water and began to sink."),
    ("n6", NARRATOR, "When Simon saw it, he fell down at Jesus' knees. He did not feel worthy of any of it, and what came out of him was not thank you."),
    # Luke 5:8
    ("s8", SCRIPTURE, "Depart from me; for I am a sinful man, O Lord."),
    ("n6b", NARRATOR, "Go away from me, Lord. I am a sinful man. On the best morning of his working life, kneeling in fish, the first thing he wanted was distance. The wonder of it had shown him exactly who he was, and exactly who this was."),
    # Luke 5:10
    ("jv10", JESUS, "Fear not; from henceforth thou shalt catch men."),
    ("n7", NARRATOR, "He does not send Simon away. He calls him. The trembling fisherman who begged him to leave is the very man he wants, and from this day on he will be gathering people, not fish."),
    ("n8", NARRATOR, "And that was enough. They brought the boats to land, left the greatest catch of their lives lying there on the shore, and followed him. They forsook all, the nets, the boats, the best day they had ever had, and went with him."),
    ("card", NARRATOR, "He met them at their emptiest, a whole night of work and nothing to show, and filled their hands past overflowing. Then he asked for all of it, so he could give them something far greater. What is he calling you to leave behind, to follow him?"),
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
