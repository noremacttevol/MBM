#!/usr/bin/env python3
"""Narration for build-93-barabbas-goes-free — Mark 15.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

THIS BUILD HAD NO SCRIPTURE IN IT AT ALL. Seven beats, all white, and
the trial that decides the whole thing was summarized rather than heard. Mark 15
is a shouting match, and none of the shouting was in the video.

LIFTED VERBATIM AS SCRIPTURE (light blue -- Pilate is a man in the story and the
crowd is a crowd; neither is Deity and a red-letter KJV inks neither):
  s9   Mark 15:9   'Will ye that I release unto you the King of the Jews?'
       -- Pilate. n1a is trimmed to the frame and n1a2 carries the retelling.
  s13  Mark 15:13  'Crucify him.'  -- the crowd. n2 is trimmed to the frame and
       n2b carries the retelling.
  s14  Mark 15:14  'Why, what evil hath he done?'  -- Pilate again. This is the
       line the whole video needs and it was missing entirely: the man with the
       power to stop it saying out loud that there was no case. n2c retells it.

NO RED, DELIBERATELY. Jesus does speak in this trial -- Mark 15:2, 'Thou sayest
it,' answering Pilate, and a red-letter KJV inks it. It was left out. Two words
of ambiguous Old English dropped into the middle of a shouting match would need
paragraphs of explanation to land, and this video's spine is the swap, not the
interrogation. Left out on judgment, not uncertainty; the verse is exact if a
later pass wants it.

NO GREEN: the Father does not speak in Mark 15.

WOMEN: Mark 15:6-15 records no woman speaking. (Pilate's wife speaks in Matthew
27:19 -- 'Have thou nothing to do with that just man' -- but that is Matthew, not
this chapter, and this video is not about Pilate's conscience. Left out on
judgment.)

WHY-LAW: a guilty man walked out of the courtyard free because the innocent one
took the exact sentence he had earned. Milk: that is the whole gospel in one
swap, and Barabbas did nothing to deserve it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "It was the custom at Passover for the governor to release one prisoner the crowd chose. Pilate had two men: Jesus, and a killer named Barabbas."),
    ("n1a", NARRATOR, "Pilate could see Jesus had done nothing worth death. So he put the choice to the crowd himself."),
    # Mark 15:9
    ("s9", SCRIPTURE, "Will ye that I release unto you the King of the Jews?"),
    ("n1a2", NARRATOR, "Do you want me to release the King of the Jews to you? He was almost offering it to them."),
    ("n1b", NARRATOR, "He thought the crowd would surely pick the innocent one."),
    ("n2", NARRATOR, "But the chief priests worked the crowd, and they shouted for Barabbas instead. Pilate asked them what he should do with Jesus, then — and they answered with one word."),
    # Mark 15:13
    ("s13", SCRIPTURE, "Crucify him."),
    ("n2b", NARRATOR, "Crucify him. That was it. That was the answer. And Pilate could not make sense of it."),
    # Mark 15:14
    ("s14", SCRIPTURE, "Why, what evil hath he done?"),
    ("n2c", NARRATOR, "Why? he asked them. What has he actually done? The man holding all the power in that courtyard said out loud that there was no case — and then handed him over anyway."),
    ("n3", NARRATOR, "So the guilty man walked free, and the innocent one was handed over in his place."),
    ("n4", NARRATOR, "Think about what Barabbas got: he was condemned, and then someone else took his exact sentence. He walked out free because Jesus took his cross."),
    ("n5", NARRATOR, "That's not just Barabbas's story. That's the whole gospel in one swap — the innocent for the guilty, so the guilty could go free."),
    ("card", NARRATOR, "Barabbas walked free because the Son of God took his place. So can you. That's the whole point."),
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
