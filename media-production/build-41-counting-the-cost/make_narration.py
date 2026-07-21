#!/usr/bin/env python3
"""Narration for build-41-counting-the-cost — Luke 14.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, all seven, and every one of them is Jesus speaking in the flesh in Luke
14:26-35. A red-letter KJV inks the lot:
  j1 v26 hate not his father and mother   j2 v27 bear his cross
  j3 v28 the tower                        j5 v31 the king going to war
  j6 v32 the ambassage                    j7 v33 forsaketh not all that he hath
  j8 v34-35 salt that lost his savour
The two small parables inside this passage -- the tower builder and the warring king
-- are Jesus's own illustrations told in his own voice, with no character dialogue in
them at all, so nothing here even raised the parable question. Nothing needed
splitting; none of the seven carried Luke's framing.

BLUE ADDED -- LUKE'S FRAMING, THE ONE NON-RED SENTENCE IN THE PASSAGE:
  s25  Luke 14:25  'And there went great multitudes with him: and he turned, and said
       unto them.' That is Luke writing, so `scripture`, light blue. It is also the
       hinge of the video -- the turn -- and it was white paraphrase inside n2. s25
       goes first on S2 and n2 keeps its id and now retells it, then j1 lands. Frame
       blue, speech red, both on the same still, no new artwork.

RED ADDED -- THE HOLE IN THE MIDDLE OF THE BUILD:
  jv29  Luke 14:29-30  'Lest haply, after he hath laid the foundation, and is not
        able to finish it, all that behold it begin to mock him, Saying, This man
        began to build, and was not able to finish.' The build jumped from j3 to j5
        and skipped the actual point of the tower story -- the half-built foundation
        and the mocking. n7 was carrying that idea alone in white. jv29 now sits on
        S7, the half-built-tower still, and n7 keeps its id and retells it. Given a
        fresh id rather than reusing the vacant 'j4' so nothing outside BEATS that
        might still reference an old j4 can be confused.

Deliberately NOT lifted: nothing else. n3's explanation of the Semitic 'hate', n5 on
Roman crucifixion, n12 on Dead Sea salt, and the whole closing run n13a to n16 are the
storyteller's work and they are what make this build land. This passage is already
about seventy percent verbatim; adding more would make it a recitation.

NO GREEN and NO WOMEN in Luke 14:25-35. Nothing invented.

WHY-LAW: he told the whole price before anybody said yes, and he had already counted
his own. Milk: he would rather you came slowly than quit.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "By now the crowd walking with him was enormous. Not a dozen men. Thousands, filling the road, more joining at every village. This is the moment every movement dreams about."),
    # Luke 14:25
    ("s25", SCRIPTURE, "And there went great multitudes with him: and he turned, and said unto them,"),
    ("n2", NARRATOR, "And then he turned around. And he did the last thing you would expect from a man with a crowd that size. He started talking them out of it."),
    # Luke 14:26
    ("j1", JESUS, "If any man come to me, and hate not his father, and mother, and wife, and children, and brethren, and sisters, yea, and his own life also, he cannot be my disciple."),
    ("n3", NARRATOR, "That word stops people cold. But in the language he spoke, there was no way to say love less. You said hate, and everybody heard a comparison. Jacob hated Leah, and it only ever meant he loved Rachel more. Matthew wrote the same teaching plainly: anyone who loves father or mother more than me. He is not asking you to hate anyone. He is asking for first place."),
    ("n4", NARRATOR, "And he was not softening it. First place is the one seat you cannot give to two people. For most of us, what keeps us from him is not some sin. It is something good we love more."),
    # Luke 14:27
    ("j2", JESUS, "And whosoever doth not bear his cross, and come after me, cannot be my disciple."),
    ("n5", NARRATOR, "Nobody in that road heard a figure of speech. Rome crucified people along the highways of Galilee, out in the open, where everybody walked past. And the condemned man carried the beam himself, through his own town."),
    # Luke 14:28
    ("j3", JESUS, "For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it?"),
    ("n6", NARRATOR, "A watchtower in a vineyard guarded the harvest you had worked all year for. Everyone there had built something. And they all knew you do not start with the stones. You start sitting on them."),
    # Luke 14:29-30
    ("jv29", JESUS, "Lest haply, after he hath laid the foundation, and is not able to finish it, all that behold it begin to mock him, Saying, This man began to build, and was not able to finish."),
    ("n7", NARRATOR, "Because half a tower is worse than none. An empty field is just a field. A foundation with three courses of stone and weeds growing through it is a monument to a man who did not think it through."),
    # Luke 14:31
    ("j5", JESUS, "Or what king, going to make war against another king, sitteth not down first, and consulteth whether he be able with ten thousand to meet him that cometh against him with twenty thousand?"),
    ("n8", NARRATOR, "Second picture, higher stakes. And look at what he asks about the king. Not whether he is brave. Whether he can count. An army of ten thousand against an army of twenty thousand is arithmetic, not courage."),
    # Luke 14:32
    ("j6", JESUS, "Or else, while the other is yet a great way off, he sendeth an ambassage, and desireth conditions of peace."),
    ("n9", NARRATOR, "And the wise king does not win the war. He does not fight it. He sends men to ask for terms while there is still open ground between the armies. Both stories turn on one act. A man sits down while he still can, and tells himself the truth."),
    # Luke 14:33
    ("j7", JESUS, "So likewise, whosoever he be of you that forsaketh not all that he hath, he cannot be my disciple."),
    ("n10", NARRATOR, "He was not telling them to sell their houses in the road that afternoon. The word means letting go of your claim. No longer keeping one corner of your life back as the part he does not get to touch. Not that everything is taken from you. That nothing is off limits to him."),
    ("n11", NARRATOR, "And it worked, the way he meant it to. The crowd got smaller. People who had walked with him all morning went home. He watched them go, and he did not lower the price."),
    # Luke 14:34-35
    ("j8", JESUS, "Salt is good: but if the salt have lost his savour, wherewith shall it be seasoned? It is neither fit for the land, nor yet for the dunghill; but men cast it out. He that hath ears to hear, let him hear."),
    ("n12", NARRATOR, "Salt from the Dead Sea marshes was never pure. Leave it in the damp and the salt leaches away, and what is left is a powder that still looks like salt and does nothing at all. That is the warning. Not a bad man. A man who looks the part with nothing in him."),
    ("n13a", NARRATOR, "So here is the question. Why would a man who came to save the world take the biggest crowd he ever had, and try to thin it out?"),
    ("n13b", NARRATOR, "Because he will not let you sign before you have read it. Think what else in your life ever did that. The loan showed you the payment afterward. The habit showed you the cost years afterward. He told a crowd the whole price first, and let them choose."),
    ("n14", NARRATOR, "He is not trying to keep you out. He is trying to keep you from a half- built life. He tells you what it costs because he wants the tower standing."),
    ("n15", NARRATOR, "And one more thing. The man asking that crowd to count what it would cost them had already counted what it would cost him. He was walking toward Jerusalem while he said it. He knew the number. He did not turn back."),
    ("n16", NARRATOR, "So he is not waiting at the end of that road with a bill. He is standing at the start of it, telling you the truth, watching to see if you want to come. He would rather you came slowly than said yes in a hurry and quit."),
    ("card", NARRATOR, "He told a crowd the whole price before a single one of them said yes. Nothing else in your life has done that for you. What would you ask a man who refuses to lie to you about the cost?"),
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
