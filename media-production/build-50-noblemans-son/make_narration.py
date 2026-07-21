#!/usr/bin/env python3
"""Narration for build-50-noblemans-son — John 4.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, BOTH. jv48 (John 4:48, 'Except ye see signs and wonders, ye will not
believe') and jv50 (John 4:50, 'Go thy way; thy son liveth') are Jesus in the
flesh and a red-letter KJV inks both. Neither carried John's framing -- 4:50 opens
'Jesus saith unto him,' and the segment already begins at 'Go thy way' -- so
neither needed splitting.

ADDED IN BLUE -- THREE VOICES THAT WERE ALL PARAPHRASE. This story turns on
things people say out loud, and every one of them was in white:
  s49  John 4:49  'Sir, come down ere my child die.'
       The father's whole prayer, in seven words. It was the tail of n6. n6 keeps
       its id, trimmed to the frame -- 'He just says it again, plain and breaking.'
       -- and a new n6b retells it.
  s51  John 4:51  'Thy son liveth.'
       The servants' message on the road. It is deliberately the SAME two words
       Jesus said a day earlier in jv50, and the video should let a viewer hear
       that rhyme rather than describing it. Lifted out of n9; n9 trimmed to the
       frame, new n9b retells it.
  s52  John 4:52  'Yesterday at the seventh hour the fever left him.'
       The hour that settles the whole story. Lifted out of n10; n10 trimmed to
       the frame, new n10b retells it and keeps n10's punchline about it being the
       very hour Jesus spoke.
All three are SCRIPTURE, light blue -- the nobleman and his servants are men in
the story, not Deity.

NO GREEN. Nothing in John 4:46-54 is the Father speaking.

WOMEN: John 4:46-54 records no woman speaking. The boy's mother is not mentioned
and the household believes as a household. Nothing added; nothing invented. (The
woman at the well is earlier in the same chapter but is a different video.)

WARNINGS ACCEPTED, NOT ERRORS: s49 and s52 will trip the validator's archaic-marker
check because 'ere' and 'the seventh hour' contain no thou/thee/hath. Both are
verbatim KJV as printed; I checked the wording rather than assuming it.

RETELLING RULE: jv48 by n5, s49 by n6b, jv50 by n7, s51 by n9b, s52 by n10b.

WHY-LAW: he healed a boy he never touched, and the word was already true for the
whole day the father spent walking home with nothing in his hands. Milk -- his
word works while you are still waiting to see it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Jesus came back to Cana, the little town where he had turned the water into wine. And word of it was spreading fast."),
    ("n2", NARRATOR, "About twenty miles away, in Capernaum, a royal official sat by his son's bed. A man of rank, used to giving orders and being obeyed. And none of it was any use now. His boy was burning with fever, and the doctors had run out of answers."),
    ("n3", NARRATOR, "Then he heard the healer was in Cana, a full day's walk uphill. So this powerful man dropped everything and went, hurrying on foot to find a village carpenter's son, because he had nowhere else left to turn."),
    ("n4", NARRATOR, "He found Jesus and begged him to come down to Capernaum and heal his boy before it was too late. A father with no pride left, only fear."),
    # John 4:48
    ("jv48", JESUS, "Except ye see signs and wonders, ye will not believe."),
    ("n5", NARRATOR, "It can sound like a scolding, but it was not. Jesus was reaching past the man's panic for something deeper. He was inviting him to trust without needing a show first."),
    ("n6", NARRATOR, "The father does not argue about it. He does not defend himself. He just says it again, plain and breaking."),
    # John 4:49
    ("s49", SCRIPTURE, "Sir, come down ere my child die."),
    ("n6b", NARRATOR, "Sir, come down before my child dies. That is the whole prayer. No argument, no explaining himself, nothing clever. Just a father running out of hours."),
    # John 4:50
    ("jv50", JESUS, "Go thy way; thy son liveth."),
    ("n7", NARRATOR, "No trip to Capernaum. No hand laid on the boy. Just a word, spoken over a sick child a day's journey away. And the man believed him, turned, and started home."),
    ("n8", NARRATOR, "Think about that walk. A whole day on the road with no proof in his hands, nothing to hold but a stranger's word that his son was already well."),
    ("n9", NARRATOR, "The next day, still on the road, he saw his own servants running toward him."),
    # John 4:51
    ("s51", SCRIPTURE, "Thy son liveth."),
    ("n9b", NARRATOR, "Your boy is alive. The very same two words Jesus had said to him a day before, coming back to him now from his own servants' mouths, out of breath from running to say them."),
    ("n10", NARRATOR, "So he asked them exactly when the boy had started to mend."),
    # John 4:52
    ("s52", SCRIPTURE, "Yesterday at the seventh hour the fever left him."),
    ("n10b", NARRATOR, "Yesterday, at the seventh hour, they told him. And he knew that hour. It was the exact hour Jesus had stood in front of him and said, thy son liveth. It had already been done while he was still walking."),
    ("n11", NARRATOR, "And that settled it. The man believed, and his whole household believed with him. The word had been true the entire way home, working quietly while he walked and could not see it."),
    ("card", NARRATOR, "He healed a boy he never touched, with a word that was already true before anyone could prove it. If his word can carry a whole day's journey, how far do you think it can reach? What would you trust him with tonight?"),
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
