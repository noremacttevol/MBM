#!/usr/bin/env python3
"""Narration for build-60-gerasene-demoniac — Mark 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, all three, and all three are Jesus in the flesh with a red-letter KJV
inking them. All kept their ids.
  j1  Mark 5:8   "Come out of the man, thou unclean spirit."
  j2  Mark 5:9   "What is thy name?"
  j3  Mark 5:19  "Go home to thy friends, and tell them how great things the Lord
      hath done for thee, and hath had compassion on thee."

THE LEGION SPEAKS, AND IT WAS ALL IN WHITE. Three of the most quoted sentences in
Mark were sitting inside narrator paraphrase. They are beings in the story, not
Deity, so they are [scripture], light blue -- the colour says "somebody in this story
is talking," which is exactly right and does not dignify them:
  s7   Mark 5:7   "What have I to do with thee, Jesus, thou Son of the most high
       God? I adjure thee by God, that thou torment me not."   -- was "the thing
       inside him cried out in terror." n2 trimmed to the frame, n2b retells.
  s9   Mark 5:9   "My name is Legion: for we are many."   -- was n5's "the answer
       that came back was a Roman army word." The single most famous line in the
       chapter, and the video never said it. n5 keeps its id and now retells it.
  s12  Mark 5:12  "Send us into the swine, that we may enter into them."   -- was
       n6's "the spirits begged not to be sent out of the country, but into the
       herd." n6 trimmed to the frame, n6b retells.

DELIBERATE QUESTION-AND-ANSWER PAIR: j2 asks "What is thy name?" and s9 answers "My
name is Legion: for we are many." Red straight into blue with nothing between them
is the whole point of the beat -- a narrator retelling wedged into that exchange
would flatten it. n5 retells immediately after.

n4 REWRITTEN, ID KEPT. It was two words of connective tissue ("Then he asked it a
question."). It now carries the retelling of j1 and still frames j2.

NO GREEN: nothing here is the Father or a voice from heaven. The unclean spirit calls
Jesus "Son of the most high God," but the spirit is the one speaking, so it is blue.

WOMEN: Mark 5:1-20 records no woman speaking. Nothing invented.

WHY-LAW: he crossed a whole sea through a storm to reach one man his own town had
buried in its memory. And when the healed man asked to come along, Jesus told him no
and sent him home to the people who had chained him. Milk: the man everyone wrote
off was the first missionary he ever sent out.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "The boat touched the far shore of the Sea of Galilee at first light — the disciples still shaking from the storm that had nearly sunk them in the night. This was the other side. Gentile country. Foreign gods, foreign food, herds of pigs on the hills. No rabbi took his students here on purpose. Jesus had crossed the whole sea in a storm to reach it."),
    ("n1", NARRATOR, "Because one man lived there — if you could call it living. He made his home among the tombs, the caves where the dead were laid, because the town had driven him out. Something had hold of him that no one could fix. They had tried chains. He tore them apart. Night and day he cried out among the graves. To his town he was no longer a name. He was a warning."),
    ("n2", NARRATOR, "And when that man saw Jesus step out of the boat, far down the shore, he ran. Not to attack him. He ran and fell down at his feet. And the thing inside him cried out:"),
    # Mark 5:7
    ("s7", SCRIPTURE, "What have I to do with thee, Jesus, thou Son of the most high God? I adjure thee by God, that thou torment me not."),
    ("n2b", NARRATOR, "What do you want with me, Jesus, Son of the most high God? Swear to me you won't torture me. Hear what just happened. The man's own town had given up on him and did not know who Jesus was. The darkness holding him knew exactly who had just stepped onto that beach, and knew it was finished."),
    ("n3", NARRATOR, "Jesus did not step back. He was not afraid of him. He spoke straight past the man, to the thing that held him."),
    # Mark 5:8
    ("j1", JESUS, "Come out of the man, thou unclean spirit."),
    ("n4", NARRATOR, "Come out of him. Not a negotiation, not a ritual — one sentence, aimed past the man at the thing wearing him. And then he asked it a question."),
    # Mark 5:9
    ("j2", JESUS, "What is thy name?"),
    # Mark 5:9
    ("s9", SCRIPTURE, "My name is Legion: for we are many."),
    ("n5", NARRATOR, "My name is Legion, it said, for we are many. Legion was a Roman army word — thousands of soldiers. That is how outnumbered this one man was on the inside. And standing in front of Jesus, the thousands were the ones begging."),
    ("n6", NARRATOR, "On the hillside above them, a herd of about two thousand pigs was feeding — remember, this was Gentile land; no Jewish town keeps pigs. And the spirits begged him:"),
    # Mark 5:12
    ("s12", SCRIPTURE, "Send us into the swine, that we may enter into them."),
    ("n6b", NARRATOR, "Send us into the pigs, they said. Let us go into them. And Jesus gave them leave. In an instant the whole herd stampeded down the steep bank into the sea, and the water closed over them. The men tending the pigs ran for town with the story of their lives."),
    ("n7", NARRATOR, "The whole town came out to see. And what they found was the man they had chained and lost and buried in their memory — sitting quietly at the feet of Jesus. Clothed. Calm. In his right mind. And the scripture says a strange thing: they were afraid. Power like that, standing on their beach, had just cost them two thousand pigs. So they asked Jesus to leave."),
    ("n8", NARRATOR, "And he did. He never argues his way in where he is not wanted. But as he climbed into the boat, the healed man begged to come with him. It is the only time in the gospels someone asks to follow Jesus and is told no. Listen to what he was given instead."),
    # Mark 5:19
    ("j3", JESUS, "Go home to thy friends, and tell them how great things the Lord hath done for thee, and hath had compassion on thee."),
    ("n9", NARRATOR, "Go home. To the town that chained you. To the people who gave up on you. Tell them what God did for you, and how he had compassion on you. The man everyone had written off became the first person Jesus ever sent out with his story — a one-man mission to the ten Gentile cities of the Decapolis. And everywhere he went, people were amazed."),
    ("card", NARRATOR, "He crossed a sea in a storm for one man everyone else had given up on. There is no distance he will not cross for you."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
