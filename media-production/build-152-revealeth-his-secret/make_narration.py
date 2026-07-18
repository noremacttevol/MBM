#!/usr/bin/env python3
"""Narration for build-152-revealeth-his-secret — Amos 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both red beats come OUT of red, and neither becomes green. This is the subtle case in the prophets set.

Amos 3:7 and 3:8 are not the LORD speaking in first person. They are AMOS writing ABOUT the LORD — 'he revealeth his secret', 'the Lord GOD hath spoken'. Third person, every clause. That is the man with the pen, so both are SCRIPTURE (light blue), not GOD (green). A red-letter KJV prints nothing here, and neither would a green one.

  kv7  Amos 3:7  scripture (was red)
  kv8  Amos 3:8  scripture (was red)

Nothing is split. Neither verse mixes speakers — both are wholly Amos.

Deliberately NOT added: Amos 3:2 ('You only have I known of all the families of the earth: therefore I will punish you for all your iniquities') is genuine first-person Jehovah and would have given this build a green beat. It is left out on purpose — it turns a warm video about a God who warns before he acts into a video about punishment. Milk, not meat. This build having no green beat at all is the correct outcome, not an oversight.

Both Old English lines already have narrator retellings after them (n4 after kv7, n7 after kv8), so nothing was added there.

WHY-LAW: God does not move against his people in the dark. He tells somebody first. That is mercy, and it is why living prophets matter.

SPOKEN: left empty. 'revealeth' is the one word at risk here, but the law requires respellings be verified by transcribing rendered audio with faster_whisper, and that could not be done in this session. Flagged for the audio pass rather than guessed at — a bad respelling is worse than none.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "The man God chose to speak through was not a king or a priest. He was a herdsman, out with his flock on the hills, a plain working man. God has always loved to call ordinary people to carry extraordinary words."),
    ("n2", NARRATOR, "And one day the word of the Lord came to him. Not his own idea, not a clever guess about what was coming, but a message given to him from God, as real and clear as a voice carried on the wind."),
    ("n3", NARRATOR, "Here is something steadying about the way God works. Before he acts, he tells someone. He does not move against his people in the dark, with no warning. He opens his plans to a servant he can trust to pass them on."),
    # Amos 3:7
    ("kv7", SCRIPTURE, "Surely the Lord GOD will do nothing, but he revealeth his secret unto his servants the prophets."),
    ("n4", NARRATOR, "Think about what that means. The God who holds everything together chooses to let people in on what he is about to do. He trusts his real plan to a prophet, the way a father warns his household before the storm arrives."),
    ("n5", NARRATOR, "So the prophet does not keep it to himself. He goes down to where the people are, to the gate and the market, and he says out loud the very thing God told him, whether the crowd wants to hear it or not."),
    ("n6", NARRATOR, "And this is a mercy, not a threat. A people who are warned can still turn. They can get ready, mend what is broken, and come home in time. No one who listened was ever caught by surprise."),
    # Amos 3:8
    ("kv8", SCRIPTURE, "The lion hath roared, who will not fear? the Lord GOD hath spoken, who can but prophesy?"),
    ("n7", NARRATOR, "When God has truly spoken, the prophet cannot stay silent, any more than you could ignore a lion roaring close beside you. The message is not his to soften or hold back. He simply has to say it."),
    ("n8", NARRATOR, "And that is the quiet comfort in this verse. God still does not leave his people guessing. He still opens his plans to living prophets, so that anyone willing to listen can hear where he is going before he gets there. So the only question is a gentle one. Are you listening for it?"),
    ("card", NARRATOR, "God does nothing without first telling his servants the prophets. He warns before he acts, because he wants his people ready, not surprised. He still speaks this way. Are you listening?"),
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
