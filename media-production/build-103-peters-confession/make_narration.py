#!/usr/bin/env python3
"""Narration for build-103-peters-confession — Matthew 16.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: all four existing red beats are Jesus speaking in the flesh and a
red-letter KJV prints all four. None of them has Matthew's framing welded on, so
none needed splitting.
  jv13  Matthew 16:13  'Whom do men say that I the Son of man am?'
  jv15  Matthew 16:15  'But whom say ye that I am?'
  jv17  Matthew 16:17  'Blessed art thou, Simon Barjona...'
  jv18  Matthew 16:18  'And I say also unto thee, That thou art Peter...'

THE FIX THIS BUILD EXISTED FOR - Peter's confession was in the NARRATOR'S voice.
Segment `np` read 'And Simon Peter answered him: Thou art the Christ, the Son of
the living God.' That is one segment welding Matthew's frame onto Peter's words,
spoken by the storyteller in white. The whole video is an exchange, and one side
of it was never heard. Split, both halves on the SAME still:
  np    stays, trimmed to the frame only: 'And Simon Peter answered him.'
        NARRATOR - modern English, the storyteller, so it stays white.
  sp16  Matthew 16:16  'Thou art the Christ, the Son of the living God.'
        SCRIPTURE, light blue. Peter's own voice, verbatim.
Peter is an apostle, not Deity, so blue is right - this is exactly the case
PLAN-AUTHORING calls out: everyone else in the story is `scripture`.

ALSO LIFTED: the disciples' answer, which was narrator paraphrase.
  s14   Matthew 16:14  'Some say that thou art John the Baptist: some, Elias; and
        others, Jeremias, or one of the prophets.'  SCRIPTURE. n3 keeps its
        original text and now works as the retelling right after it, including
        the 'all second-hand' point, which lands harder once you have heard how
        borrowed the answers sound.

NO GREEN HERE, AND WORTH SAYING: 'my Father which is in heaven' inside jv17 is
Jesus speaking ABOUT the Father, not the Father speaking. There is no voice from
heaven anywhere in Matthew 16, so nothing was made `god`.

WOMEN: Matthew 16:13-18 records no woman speaking. Nothing added; nothing
invented.

WHY-LAW: the crowd's answers were respectful, safe, and someone else's. The
question that matters is the one nobody can answer for you, and the answer comes
quietly from the Father rather than from being clever.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Jesus had brought his disciples a long way north, to a quiet place far from the crowds, up under a great cliff of pale rock. And there he asked them a question he had never asked so plainly before."),
    # Matthew 16:13
    ("jv13", JESUS, "Whom do men say that I the Son of man am?"),
    ("n2", NARRATOR, "It was an easy question at first. What are people saying? And they had plenty of answers ready."),
    # Matthew 16:14
    ("s14", SCRIPTURE, "Some say that thou art John the Baptist: some, Elias; and others, Jeremias, or one of the prophets."),
    ("n3", NARRATOR, "Some say Elijah come back. Others, Jeremiah, or one of the old prophets. All respectful. All safe. All second-hand — what other people thought."),
    # Matthew 16:15
    ("jv15", JESUS, "But whom say ye that I am?"),
    ("n4", NARRATOR, "And there it was. Not what have you heard. Not what is the crowd saying. But you — who do you say that I am? The question stopped them cold. This one you cannot borrow from anybody else."),
    ("np", NARRATOR, "And Simon Peter answered him."),
    # Matthew 16:16
    ("sp16", SCRIPTURE, "Thou art the Christ, the Son of the living God."),
    ("n5", NARRATOR, "Not a prophet. Not a teacher. Peter said out loud the thing the others had only half-dared to hope."),
    # Matthew 16:17
    ("jv17", JESUS, "Blessed art thou, Simon Barjona: for flesh and blood hath not revealed it unto thee, but my Father which is in heaven."),
    ("n6", NARRATOR, "You did not work this out on your own, Jesus told him. My Father in heaven showed it to you. This kind of knowing does not come from clever thinking. It is given, quietly, from God, to a heart ready to receive it."),
    # Matthew 16:18
    ("jv18", JESUS, "And I say also unto thee, That thou art Peter, and upon this rock I will build my church; and the gates of hell shall not prevail against it."),
    ("n7", NARRATOR, "On this — on knowing who he really is — he would build something that hell itself could never tear down. Everything else in the gospel is built on top of this one answer."),
    ("card", NARRATOR, "The crowds had their opinions; Peter had an answer he would stake his life on. Jesus is still asking the one question that no one can answer for you. Who do YOU say that he is?"),
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
