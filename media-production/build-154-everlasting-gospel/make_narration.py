#!/usr/bin/env python3
"""Narration for build-154-everlasting-gospel — Revelation 14.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Revelation is the one book in this set where red is sometimes right — a
red-letter King James Bible does print Christ's explicit sayings red ('I am
Alpha and Omega', 'To him that overcometh', the letters to the seven churches).
Neither of this build's red beats is one of them.

  kv6  Revelation 14:6  RED -> SCRIPTURE. This is John narrating his own vision:
       'And I saw another angel fly in the midst of heaven...' Christ is not
       speaking and is not even the subject of the sentence.
  kv7  Revelation 14:7  RED -> SCRIPTURE. This is the ANGEL's cry, quoted by
       John. An angel is a messenger, not Deity — so it is neither red nor
       green. A red-letter KJV leaves 14:7 black.

kv7 is technically two voices in one verse — 'Saying with a loud voice,' is
John writing and the rest is the angel — but BOTH are `scripture`, so the
colour is correct either way and the segment is deliberately left unsplit
rather than cut the line for no visible gain.

No new verses lifted. n4, n5 and n7 already carry the modern-English retelling
for both quotations, so nothing is added.

WHY-LAW: milk at its plainest. An angel brings the gospel back to a world that
had lost hold of it, for every nation and kindred and tongue. The video never
says the angel's name or points at 1830 — it lets the verse do it.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "For long stretches of history, whole peoples lived without it — the good news about God, misplaced, buried, or never yet heard. Men reached for heaven in the dark and could not quite find the way."),
    ("n2", NARRATOR, "And then, in a vision, John of Patmos saw heaven open, and something come. Not an army, not a storm, but an angel, sent on an errand of mercy, carrying a message meant for the whole earth."),
    ("n3", NARRATOR, "The angel flew across the height of heaven for all to see, holding out an open book: the good news about God, ready to be given back to a world that had lost hold of it."),
    # Revelation 14:6
    ("kv6", SCRIPTURE, "And I saw another angel fly in the midst of heaven, having the everlasting gospel to preach unto them that dwell on the earth, and to every nation, and kindred, and tongue, and people,"),
    ("n4", NARRATOR, "Notice the word: everlasting. This good news was never really invented, or improved, by anyone. It is older than the nations, the same true message from the beginning, carried down from heaven and offered fresh again."),
    ("n5", NARRATOR, "And notice who it is for. Not one favoured people, not one language or land, but every nation, every family, every tongue. No one is too far away, too foreign, or too late to be handed this."),
    ("n6", NARRATOR, "The angel's call is simple and clean. Honour God, give him the glory, and worship the One who made it all — the heavens, the earth, the sea, and every spring of water. Turn your face back toward your Maker."),
    # Revelation 14:7
    ("kv7", SCRIPTURE, "Saying with a loud voice, Fear God, and give glory to him; for the hour of his judgment is come: worship him that made heaven and earth, and the sea, and the fountains of waters."),
    ("n7", NARRATOR, "It is a call to come home to the God of creation — the same God who set the stars in place and filled the seas. Not a distant idea, but the Maker of the very ground under your feet, quietly asking for your heart."),
    ("n8", NARRATOR, "So here is the quiet wonder of this verse. The good news was never abandoned for good. Heaven sent it out again, on purpose, for everyone — which means it was sent for you, too. So the only question is a gentle one. Will you receive it?"),
    ("card", NARRATOR, "The gospel was never lost for good. Heaven sent an angel to carry it back to every nation, kindred, and tongue — everlasting, and meant for you. Will you receive it?"),
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
