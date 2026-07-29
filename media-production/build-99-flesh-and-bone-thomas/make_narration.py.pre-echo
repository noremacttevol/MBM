#!/usr/bin/env python3
"""Narration for build-99-flesh-and-bone-thomas — John 20.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED, and one of the two was quietly repaired:
  j1  Luke 24:39  'Behold my hands and my feet, that it is I myself: handle me,
      and see; for a spirit hath not flesh and bones, as ye see me have.'
      Correct and exact. Tagged to Luke, which is where this sentence actually
      comes from; the build's reference stays John 20.
  j2  John 20:27  REPAIRED. The build had 'Reach hither thy finger, and behold my
      hands; and be not faithless, but believing' -- which silently dropped the
      middle of the verse. That is an abridgement, not verbatim, and a viewer
      looking it up would not find it as printed. Restored to the full verse:
      'Reach hither thy finger, and behold my hands; and reach hither thy hand,
      and thrust it into my side: and be not faithless, but believing.' Id kept.

RED ADDED -- the line the viewer needs was missing:
  jv29 John 20:29  'Thomas, because thou hast seen me, thou hast believed:
       blessed are they that have not seen, and yet have believed.'
       That is the sentence that turns this from a story about Thomas into a
       promise to whoever is watching. n4b keeps its id and now retells it.

THOMAS IS BLUE, BOTH TIMES. He is a man in the story, not Deity, so a red-letter
KJV leaves him black. Both his lines were narrator paraphrase in white:
  s25  John 20:25  'Except I shall see in his hands the print of the nails, and
       put my finger into the print of the nails, and thrust my hand into his
       side, I will not believe.'
       n2 is trimmed to the frame and n2b carries the retelling. His demand and
       Jesus's answer are almost word for word the same sentence -- that only
       lands if you hear both in their own words.
  s28  John 20:28  'My Lord and my God.'
       THE confession, and it was not in the video at all. n4a keeps its id and
       now retells it.

RETELLINGS ADDED: n1b after 'flesh and bones', n3b after 'reach hither thy
finger'. Neither Old English line was being said again in plain words.

NO GREEN: the Father does not speak in John 20:19-29.

WOMEN: John 20:19-29 records no woman speaking; the locked room is the disciples.
Nothing added, nothing invented.

CONSIDERED, LEFT OUT. 'Peace be unto you' (John 20:19, 26) is red and it is
lovely, but it is said twice in this passage and adding it would put a fifth red
beat in an eight-still video whose spine is the hands. Left out on judgment; the
verse is exact if a later pass wants it.

WHY-LAW: Thomas named the exact proof he needed, and eight days later Jesus
walked in and offered him that exact proof, word for word, without a word of
rebuke. Milk: honest doubt is not the opposite of faith, and he moves toward it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "The disciples were hiding behind locked doors, afraid, when Jesus suddenly stood among them. They thought they were seeing a ghost."),
    ("n1", NARRATOR, "He calmed them and showed them it was really him — flesh and bone, not a spirit."),
    # Luke 24:39
    ("j1", JESUS, "Behold my hands and my feet, that it is I myself: handle me, and see; for a spirit hath not flesh and bones, as ye see me have."),
    ("n1b", NARRATOR, "Look at my hands and my feet, he said. It's me. Touch me and see — a spirit doesn't have flesh and bones like I have. He did not ask them to take it on faith. He told them to put their hands on him."),
    ("n2", NARRATOR, "But Thomas wasn't there. And when they told him what they had seen, he would not have it."),
    # John 20:25
    ("s25", SCRIPTURE, "Except I shall see in his hands the print of the nails, and put my finger into the print of the nails, and thrust my hand into his side, I will not believe."),
    ("n2b", NARRATOR, "Unless I see the nail marks in his hands, he said, and put my finger where the nails went, and my hand into his side — I will not believe it. He did not just doubt. He named the exact proof he would need."),
    ("n3", NARRATOR, "It was eight days later when Jesus appeared again — and he turned straight to Thomas, and offered him that exact proof, in almost the same words Thomas had used."),
    # John 20:27
    ("j2", JESUS, "Reach hither thy finger, and behold my hands; and reach hither thy hand, and thrust it into my side: and be not faithless, but believing."),
    ("n3b", NARRATOR, "Put your finger here, he said, and look at my hands. Put your hand into my side. Stop doubting, and believe. Every single thing Thomas had demanded, handed to him without one word of scolding."),
    # John 20:28
    ("s28", SCRIPTURE, "My Lord and my God."),
    ("n4a", NARRATOR, "My Lord and my God. That is all Thomas said. He never did reach out and touch anything. Jesus didn't scold him for doubting — he met the doubt with his own hands, and the doubt was over."),
    # John 20:29
    ("jv29", JESUS, "Thomas, because thou hast seen me, thou hast believed: blessed are they that have not seen, and yet have believed."),
    ("n4b", NARRATOR, "You believed because you saw me, he told him. Blessed are the ones who have not seen, and believe anyway. That last line was not about Thomas. That one was about you. And that's what he does with honest doubt — he steps toward it."),
    ("card", NARRATOR, "He met a doubter with open hands, not anger. Bring him your doubt. He can handle it."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


SPOKEN.update({'doubt': 'dowt'})  # round2 in-context A/B winners 2026-07-20 (SWEEP/round2-state.json)

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
