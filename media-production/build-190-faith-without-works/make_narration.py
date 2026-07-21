#!/usr/bin/env python3
"""Narration for build-190-faith-without-works — James 2.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

MOVED OUT OF RED.
  s1  RED -> SCRIPTURE, light blue.  James 2:17  'Even so faith, if it hath not
      works, is dead, being alone.'
James is an epistle. That is James writing to the twelve tribes scattered abroad,
not Christ speaking, and a red-letter King James Bible prints no red anywhere in
the letter. Red made an apostle's argument read as the Lord's own words. Blue is
the writer. The line was already verbatim and is unchanged.

NO SPLITS. James 2:17 is one speaker start to finish.

LIFTED FROM PARAPHRASE:
  s26  James 2:26  'For as the body without the spirit is dead, so faith without
       works is dead also.'   SCRIPTURE, blue
n4a and n4b were closing the build on the chapter's own conclusion — 'belief that
never moves a muscle isn't belief yet' — while the verse that says it never got
spoken. It is the sentence the whole letter is remembered for and it belongs in
James's own words. s26 sits on ST6 with n4a, a still the build already has, so no
new artwork, and n4a and n4b become its retelling right where they already were.

The segment keeps its original id `s1` even though the id looks like a still var
— renaming it would orphan anything referencing it by name.

The closing card is not a beat in this build and has been left out of BEATS,
exactly as the original had it.

WHY-LAW: milk. Works are shown as faith becoming visible — a coat handed over, a
window rope let down — never as a price paid or a score kept. The close is
gentle: let your faith move, and he sees the small true things.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "James wrote plainly to the early church: a faith that stays only in the head is already dead."),
    ("n1", NARRATOR, "He asked the sharp question — if a brother or sister has no clothes and no food, and you wish them well but give nothing, what good is that?"),
    # James 2:17
    ("s1", SCRIPTURE, "Even so faith, if it hath not works, is dead, being alone."),
    ("n2", NARRATOR, "Then he pointed to Abraham, who showed his faith by what he did — offering his son on the altar."),
    ("n3", NARRATOR, "And to Rahab, who hid the spies and was counted righteous by her action, not just her words."),
    # James 2:26
    ("s26", SCRIPTURE, "For as the body without the spirit is dead, so faith without works is dead also."),
    ("n4a", NARRATOR, "Belief that never moves a muscle isn't belief yet."),
    ("n4b", NARRATOR, "Faith and life belong together."),
    ("card", NARRATOR, "Real faith reaches out a hand. Let yours move — he sees every small, true thing you do."),
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
