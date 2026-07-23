#!/usr/bin/env python3
"""Narration for build-64-pool-of-bethesda — John 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, both, and one more added:
  j1   John 5:6   "Wilt thou be made whole?"   -- kept its id.
  j2   John 5:8   "Rise, take up thy bed, and walk."   -- kept its id.
  j14  John 5:14  "Behold, thou art made whole: sin no more, lest a worse thing come
       unto thee."   -- MISSING ENTIRELY. n6 reported that Jesus found him in the
       temple and then skipped what he actually said there. Lifted verbatim onto S8.
       n6 keeps its id, trimmed to the frame; n6b retells it warmly -- the sentence
       is an invitation out of what was breaking him, not a threat, and the
       retelling says so without arguing the point.

THE MAN WAS NEVER HEARD, AND HIS ANSWER IS THE POINT OF THE STORY. Jesus asks him a
straight yes-or-no question and he does not answer it -- he explains the system. That
whole beat was sitting in white paraphrase inside n3. Lifted verbatim as s7
[scripture] on the SAME still (S4):
  s7  John 5:7  "Sir, I have no man, when the water is troubled, to put me into the
      pool: but while I am coming, another steppeth down before me."
n3 keeps its id and now carries the setup and the frame; n3b retells.

THE RULE-KEEPERS WERE NEVER HEARD. n5 paraphrased John 5:10. Lifted as s10
[scripture] on S7: "It is the sabbath day: it is not lawful for thee to carry thy
bed." n5 keeps its id, trimmed to the frame; n5b retells and carries the rest of
what n5 used to say.

n4 REWRITTEN, ID KEPT -- it now opens by retelling j2 in plain English ("Get up, pick
up your mat, and walk") before going on to the healing, so the red line does not land
unexplained.

NO GREEN: John 5:1-15 has no voice from heaven. The angel of the pool is a legend
reported in the passage, and nobody speaks for it.

WOMEN: John 5:1-15 records no woman speaking. Nothing invented.

WHY-LAW: thirty-eight years, and the first thing Jesus does is ask his permission.
He healed a man who could not name him, had not followed him, and never clearly said
yes. Milk: grace came first. Everything else came after.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "By the sheep gate in Jerusalem there was a pool called Bethesda, ringed by five covered porches. And those porches were full of the city's most hopeless people — the blind, the lame, the paralyzed — all waiting on a legend: every so often the water stirred, and the first one in, people said, would be healed. Imagine the math of that place. Hundreds waiting. One winner. And the fastest one wins a race for the people who can't run."),
    ("n1", NARRATOR, "One man had been lying there thirty-eight years. Let that number land. That was longer than most people in that world even got to be alive. Whole generations had grown up and grown old while he lay on that mat, watching the water, losing the same race every time. By now, being the sick man by the pool was not just his condition. It was his whole identity."),
    ("n2", NARRATOR, "Jesus walked those porches, past hundreds of the suffering, and stopped at this one man. John says he knew — knew he had been there a long time. And then he asked him a question that sounds almost unkind, until you sit with it:"),
    # John 5:6
    ("j1", JESUS, "Wilt thou be made whole?"),
    ("n3", NARRATOR, "Do you want to be made well? After thirty-eight years, that is a real question. Healing would mean a new name, new work, a whole new life — and no more excuse. And notice: the man does not answer yes. He does not answer at all. He answers with the obstacle:"),
    # John 5:7
    ("s7", SCRIPTURE, "Sir, I have no man, when the water is troubled, to put me into the pool: but while I am coming, another steppeth down before me."),
    ("n3b", NARRATOR, "While I'm dragging myself toward it, somebody else always gets down there first. He was explaining the system. Jesus had not asked him about the system."),
    # John 5:8
    ("j2", JESUS, "Rise, take up thy bed, and walk."),
    ("n4", NARRATOR, "Get up. Pick up your mat. Walk. No angel. No water. No race. The pool had nothing to do with it. And immediately the man was made whole — thirty-eight years of atrophy gone between one breath and the next. Legs that had forgotten what weight felt like took his weight. He stood up, rolled up the mat that had been his whole world, and walked."),
    ("n5", NARRATOR, "It was the sabbath, so the rule-keepers stopped him at once — not to celebrate him, but to tell him:"),
    # John 5:10
    ("s10", SCRIPTURE, "It is the sabbath day: it is not lawful for thee to carry thy bed."),
    ("n5b", NARRATOR, "It's the sabbath. You're not allowed to carry that mat. A man walks for the first time in thirty-eight years and the first thing anybody says to him is about the mat. And here is the astonishing part: when they asked who had healed him, he did not know. He had never asked the name. Jesus had healed a man who could not identify him, had not followed him, and had not even clearly said yes. Grace came first. Everything else came after."),
    ("n6", NARRATOR, "Later, Jesus found him in the temple — found him, again, the way he found the man born blind — and said to him:"),
    # John 5:14
    ("j14", JESUS, "Behold, thou art made whole: sin no more, lest a worse thing come unto thee."),
    ("n6b", NARRATOR, "Look at you — you are whole. Now don't go back to the things that were destroying you. It is not a threat. It is a man who has just given you your legs back asking you not to walk them into a ditch. And only then did the man learn the name of the one who had given him his life. He went and told everyone: it was Jesus."),
    ("n7", NARRATOR, "Thirty-eight years, and one question. Not: why are you still here. Not: whose fault is this. Just — do you want to be whole? The pool never healed anybody. The person standing next to that man did."),
    ("card", NARRATOR, "However long it has been for you — he is not put off by the years. He is still asking: do you want to be whole?"),
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
