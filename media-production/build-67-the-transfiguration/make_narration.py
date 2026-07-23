#!/usr/bin/env python3
"""Narration for build-67-the-transfiguration — Mark 9.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THE FATHER IS GREEN, NOT RED. This is the headline fix in this build.
  j2  Mark 9:7  'This is my beloved Son: hear him.'  was painted JESUS-RED. That
      is the FATHER speaking out of the cloud. Leaving it red has Christ standing
      on the mountain announcing himself as his own beloved Son. It is now `god`
      (green). The id is kept so the music bed stays attached.
      The framing was already split off correctly -- n3, 'Then a bright cloud
      settled over the mountain, and out of it came a voice,' is the storyteller
      and stays white -- so no further split was needed here.
      Mark's wording is 'hear him'; Matthew 17:5 has 'hear ye him'. This build's
      reference is Mark 9, so Mark's exact wording is kept and the verse field
      says Mark 9:7. Nothing blended, nothing approximated.

PETER WAS MIS-SPEAKERED TOO. j1, 'Master, it is good for us to be here: and let
us make three tabernacles...', is Mark 9:5 -- PETER. It was not red, but it was
sitting in the narrator's white voice as though the storyteller were saying it.
It is verbatim KJV out of a man's mouth, so it is now `scripture` (light blue).
The id is kept.

NOTHING STAYED RED. Jesus does not speak a red-letter line anywhere in this
build's cut. The only red-letter words in Mark 9:2-8 are in verse 9, after they
came down the mountain, which this video does not cover. n4's 'Do not be afraid,
he told them' is Matthew 17:7 paraphrased in the storyteller's voice and is left
as paraphrase deliberately -- it is not in Mark, and putting Matthew's exact
words in would mean lifting from a chapter this build never cites.

RETELLINGS ADDED: n2c after Peter's line, n3b after the Father's line.

WOMEN: Mark 9:2-8 records no woman speaking -- the three who went up the mountain
were Peter, James and John. Nothing added; nothing invented.

WHY-LAW: heaven interrupted a good idea to say one thing, and the one thing was
not 'look at him'. It was 'hear him'. Milk: the Father's instruction about his
Son is still an instruction about listening.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Jesus took three of his closest friends — Peter, James, and John — up a high mountain, away from everyone."),
    ("n1", NARRATOR, "And there, in front of them, he changed. His clothes turned a blinding white, brighter than anything on earth, and for one moment they saw him shining with who he really is."),
    ("n2a", NARRATOR, "Two of the greatest prophets, Moses and Elias, appeared and stood talking with him."),
    ("n2b", NARRATOR, "Peter, overwhelmed, blurted out the first thing that came to him."),
    # Mark 9:5
    ("j1", SCRIPTURE, "Master, it is good for us to be here: and let us make three tabernacles; one for thee, and one for Moses, and one for Elias."),
    ("n2c", NARRATOR, "Master, it's good that we're here — let us put up three shelters, one for you, one for Moses, one for Elias. He wanted to keep the moment. Build something, stay a while. Mark adds, kindly, that Peter did not know what to say, because they were so afraid."),
    ("n3", NARRATOR, "Then a bright cloud settled over the mountain, and out of it came a voice."),
    # Mark 9:7
    ("j2", GOD, "This is my beloved Son: hear him."),
    ("n3b", NARRATOR, "This is my Son, whom I love. Listen to him. Not build for him. Not stay up here with him. Listen to him. Of everything the Father could have said on that mountain, he gave them one sentence and one instruction."),
    ("n4", NARRATOR, "And then it was over. The light faded, the cloud lifted, and Jesus stood there alone — the same gentle friend, reaching down to lift them up. Do not be afraid, he told them."),
    ("card", NARRATOR, "For one moment they saw who he really is — and heaven said, hear him. That invitation still stands."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {
    # "Elias" — Cameron wants ee-LY-us in EVERY voice (complaint #67), and the
    # narrator paraphrases changed from "Elijah" to "Elias" above so all three
    # speakers now say the KJV name. NOTE: whisper writes "Elias" back no matter
    # the stress, so this respelling's ee-LY-us stress is NOT transcription-
    # verifiable — confirm by ear.
    "Elias": "ee lye us",
}


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
