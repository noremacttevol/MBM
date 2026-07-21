#!/usr/bin/env python3
"""Narration for build-110-lords-prayer — Matthew 6.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

This one is almost entirely red and correctly so. The Lord's Prayer is Jesus
speaking in the flesh, continuously, in the Sermon on the Mount; a red-letter KJV
inks Matthew 6:9 through 6:13 solid red. All three existing red beats are exact
KJV and stay exactly as they are.

STAYED RED (jesus), checked word for word against the KJV:
  jv9   Matt 6:9b-10  'Our Father which art in heaven, Hallowed be thy name. Thy
                       kingdom come. Thy will be done in earth, as it is in heaven.'
  jv11  Matt 6:11-12  'Give us this day our daily bread. And forgive us our debts,
                       as we forgive our debtors.'
  jv13  Matt 6:13     'And lead us not into temptation, but deliver us from evil:
                       For thine is the kingdom, and the power, and the glory, for
                       ever. Amen.'

THE FRAMING LINE IS ALSO RED, and this is the one that is easy to get wrong:
  jv9a  Matt 6:9a  'After this manner therefore pray ye:'
This is NOT an evangelist framing clause like 'And Jesus said unto them.' It is
Jesus's own sentence, inside his own teaching, and a red-letter KJV prints it
red. So it is added as a `jesus` beat immediately before jv9, on the same still,
restoring the first half of the verse the video had been dropping.

LIFTED FROM PARAPHRASE - also Jesus, so also RED:
  jv7   Matt 6:7  'But when ye pray, use not vain repetitions, as the heathen do:
                   for they think that they shall be heard for their much
                   speaking.'
n5 was already saying this in modern English ('prayer is not a performance, not
many clever words'), so the real verse now speaks first.

LIFTED FROM PARAPHRASE - the disciple, so SCRIPTURE (light blue):
  s11  Luke 11:1  'Lord, teach us to pray, as John also taught his disciples.'
n1 asserts that the disciples asked him how to pray, which is Luke's account
rather than Matthew's, and the actual request was nowhere in the video. It is
added verbatim with an explicit Luke reference so a viewer looking it up finds it
where it really is. FLAGGING THIS PLAINLY: it is the one line in this plan that
comes from outside the build's stated Matthew 6 reference. If Cameron would
rather keep the build strictly inside Matthew 6, drop s11 and fold n1 and n1b
back into one segment - nothing else depends on it.

EDITS TO EXISTING NARRATOR TEXT: n1 is split at its own seam so it hands to s11;
its second half becomes n1b, essentially unchanged. n5's opening clause changes
from 'Because Jesus had just warned them:' to 'That was his warning, just before
this:' so it reads as a retelling of jv7 rather than a forward reference. Nothing
else in any narrator beat changed.

WOMEN: neither Matthew 6 nor Luke 11:1 records a woman speaking. Nothing was
added rather than reaching for a line from an unrelated passage.

WHY-LAW: he answered a question about technique with a family word. Milk framing
- you do not need the right words, you need to begin.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "One day his followers asked him a simple question."),
    # Luke 11:1
    ("s11", SCRIPTURE, "Lord, teach us to pray, as John also taught his disciples."),
    ("n1b", NARRATOR, "Teach us how to pray. They expected, maybe, a technique. A ritual. Instead, Jesus gave them a family word."),
    # Matthew 6:9
    ("jv9a", JESUS, "After this manner therefore pray ye:"),
    # Matthew 6:9-10
    ("jv9", JESUS, "Our Father which art in heaven, Hallowed be thy name. Thy kingdom come. Thy will be done in earth, as it is in heaven."),
    ("n2", NARRATOR, "Father. Not a distant judge. Not a force. A Father you belong to. And the very first thing you long for, once you know him, is not for yourself at all — that his name be honoured, and his good kingdom come, everywhere."),
    # Matthew 6:11-12
    ("jv11", JESUS, "Give us this day our daily bread. And forgive us our debts, as we forgive our debtors."),
    ("n3", NARRATOR, "Then the plain, honest things. Bread — it is fine to ask for the ordinary needs of the day. And forgiveness — asked for, and passed on. We receive mercy with the same hands we use to give it away."),
    # Matthew 6:13
    ("jv13", JESUS, "And lead us not into temptation, but deliver us from evil: For thine is the kingdom, and the power, and the glory, for ever. Amen."),
    ("n4", NARRATOR, "Keep me safe. Lead me away from what would harm me. And it ends where it began — with him: the kingdom, the power, the glory, all his, for ever. Short. Honest. Nothing showy."),
    # Matthew 6:7
    ("jv7", JESUS, "But when ye pray, use not vain repetitions, as the heathen do: for they think that they shall be heard for their much speaking."),
    ("n5", NARRATOR, "That was his warning, just before this: prayer is not a performance. Not many clever words, not standing on a corner to be admired. The prayer God loves most may be the simplest one a child ever whispered."),
    ("n6", NARRATOR, "That is really all it is. Not a speech to impress heaven. A child, climbing into the lap of a good Father, and simply talking to him."),
    ("n7", NARRATOR, "So you do not need the right words. You only need to begin. And the beginning is just two words, the ones he gave them first of all: Our Father."),
    ("card", NARRATOR, "Jesus said you can talk to God the way a child talks to a good Father — simply, honestly, no performance. It starts with two words: Our Father. What would you say to him, if you began today?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
# Cameron denial #110 (2026-07-18): "lead" was read as the metal /led/. Here it is
# the VERB and rhymes with "seed" — /li:d/. Caption keeps the exact word.
SPOKEN = {
    "lead": "leed",
    "Lead": "Leed",
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
