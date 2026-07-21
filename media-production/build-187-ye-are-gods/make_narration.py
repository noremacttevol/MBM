#!/usr/bin/env python3
"""Narration for build-187-ye-are-gods — Psalm 82 (quoted in John 10).

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

MOVED OUT OF RED — this is the correction the build needed.
  j1  RED -> GOD, GREEN.  Psalm 82:6  'I have said, Ye are gods; and all of you are
      children of the most High.'
The video frames this as Jesus reaching into the leaders' own scriptures, and the
quoted words were painted red as though they were his. They are not. That text is
Psalm 82:6 — the LORD speaking in Asaph's psalm, long before Christ came in the flesh.
A red-letter King James Bible leaves Psalm 82 black. Under speaker law Old Testament
Deity speech is GREEN, never red: it is still Deity, and green carries that without
arguing it.

NO SPLIT. j1 is one speaker start to finish.

LIFTED FROM PARAPHRASE (2026-07-18 enrichment). The first pass repainted j1 and lifted
nothing, so cutting the 9.8s closing card to 1.5s dropped the story to 52.7s, under
this build's 60.5s floor. The fix is not a longer card. The real problem is that a
video built on one line of a psalm was only ever quoting one line of a psalm. Psalm 82
is eight verses long, and the rest of it is the reason verse 6 was ever said. Three
more passages are now in, and the psalm's own structure decides each colour:

  s82a  Psalm 82:1    NEW (scripture, blue). Asaph narrating — God standing up in the
        congregation of the mighty, judging among the gods. Third-person narration
        ABOUT the LORD is the writer, not the LORD, so this is blue and not green. It
        sets the courtroom the whole psalm happens in. Retold by n82a.
  g82b  Psalm 82:2    NEW (god, green). 'How long will ye judge unjustly, and accept
        the persons of the wicked?' Deity speech, Old Testament, so green. This is the
        interpretive key in one short line: it tells the viewer the 'gods' of verse 6
        are judges, which is the whole reason Christ could quote it at judges. Retold
        by n82b.
  g82g  Psalm 82:7    NEW (god, green). 'But ye shall die like men.' This is the verse
        that keeps the video honest, and it is the most important addition here.
        Retold by n82g.

NOT ADDED: Psalm 82:3-4, the charge to defend the poor and fatherless and deliver the
needy. It is the warmest passage in the psalm and I wanted it. But verse 2 already
establishes that these are judges being judged, which is the only work this video needs
the psalm's opening to do, and 3-4 would add a second full charge on the same point.
Two verses of social charge inside a sixty-second video about a courtyard argument
starts to become a different video. Left out for shape, not for doctrine.

WHY VERSE 7 MATTERS: verse 6 on its own is the most misquoted line in this psalm. Read
alone it sounds like a promise of status. Read with verse 7 — the LORD's very next
breath — it is a rebuke: you were handed the office of gods and you will die like men
anyway. Including it is what stops this video drifting out of milk and into an argument
about what men may become. It is also, plainly, what the text says.

ONE CLAUSE TRIMMED: verse 2 is quoted through 'the persons of the wicked?' and stops at
the question mark. The verse ends with 'Selah', a musical direction rather than part of
the sentence, and speaking it aloud would read as a word of the rebuke. The quotation
is verbatim up to a clean clause boundary; nothing is altered or added.

STILL NOT ADDED, and still deliberately: the John 10:34-36 frame — 'Is it not written
in your law' — would be a red Jesus beat and would put red back on the same still as
the green. The build does not need it; n1 already tells the viewer he is quoting their
own scripture, and n2 lands the argument. Staying inside Psalm 82 also keeps ONE voice
on the psalm block, which is what lets the green read as an older voice instead of as
Christ quoting himself.

NOTE FOR A FUTURE SESSION: briefs.json records this build's `book` as 'John', not
'Psalms', so validate_plan.py would in fact ALLOW `jesus` here — the Old Testament
guard everyone has assumed was protecting this build is not actually armed on it.
Keeping this video free of red is a judgement call, not a constraint. If a later
session wants the John 10 frame, the validator will not stop it; the reason not to is
the one above.

Psalm 82:5 and 82:8 were also left out. Verse 5 ('they know not, neither will they
understand') is the LORD turning aside to comment on them, and would blunt the drive
from verse 4 into verse 6. Verse 8 is Asaph's closing plea, 'Arise, O God, judge the
earth' — a fine ending for the psalm, but this video ends on Christ in the courtyard,
not on the psalmist, and n3b is the right last word.

Nothing else lifted. n2, n3a and n3b already retell the psalm and the point of it in
plain English, so the retelling rule is met there.

All five quotations were checked word for word against the 1769 Authorized Version.

ST6 is absent from the build's still vars; no beat uses it, and this plan does not
introduce one. The closing card is not a beat and has been left out of BEATS, exactly
as the original had it.

WHY-LAW: milk, and carefully so. This is a verse people reach for to argue about what
men may become, and the build does not go there. It stays on what actually happened in
the courtyard: he answered them out of their own book, and they had nothing to say
back.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "The religious leaders were circling Jesus, demanding he say plainly who he claimed to be."),
    ("n1", NARRATOR, "Instead of backing down, he reached into their own scriptures — to a psalm where God calls mere men gods."),
    # Psalm 82:1
    ("s82a", SCRIPTURE, "God standeth in the congregation of the mighty; he judgeth among the gods."),
    ("n82a", NARRATOR, "The psalm opens in a courtroom. God stands up in the middle of Israel's judges — and starts judging the judges."),
    # Psalm 82:2
    ("g82b", GOD, "How long will ye judge unjustly, and accept the persons of the wicked?"),
    ("n82b", NARRATOR, "How long, he asks them, will you rule crooked and keep taking the side of the people doing the harm?"),
    # Psalm 82:6
    ("j1", GOD, "I have said, Ye are gods; and all of you are children of the most High."),
    ("n2", NARRATOR, "His point was sharp: if scripture called men gods because God's word came to them, how could they condemn the one the Father set apart?"),
    # Psalm 82:7
    ("g82g", GOD, "But ye shall die like men, and fall like one of the princes."),
    ("n82g", NARRATOR, "And read the next line. The same psalm that called them gods tells them they will die like anybody else. The title was never theirs to keep."),
    ("n3a", NARRATOR, "He was not making himself a second God."),
    ("n3b", NARRATOR, "He was showing them their own book exposed their logic."),
    ("card", NARRATOR, "He stood on the scriptures they claimed to love. Come know him as he truly is."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


SPOKEN.update({'psalm': 'sahm'})  # round2 in-context A/B winners 2026-07-20 (SWEEP/round2-state.json)

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
