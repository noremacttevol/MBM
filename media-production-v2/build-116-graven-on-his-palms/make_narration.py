#!/usr/bin/env python3
"""Narration for build-116-graven-on-his-palms — Isaiah 49.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both red beats are Jehovah speaking through Isaiah. Isaiah is Old Testament, so
neither can be red — both are GOD (green):
  jv15  Isaiah 49:15  'Can a woman forget her sucking child...'
  jv16  Isaiah 49:16  'Behold, I have graven thee upon the palms of my hands...'

LIFTED FROM PARAPHRASE:
  s14  Isaiah 49:14  'But Zion said, The LORD hath forsaken me, and my Lord hath
                      forgotten me.'  SCRIPTURE
n2 was paraphrasing this verse in modern English. Verse 14 is the whole reason
verses 15 and 16 exist — the complaint has to be heard before the answer means
anything — so it is now spoken verbatim, and n2 was rewritten as its retelling.

WHY s14 IS BLUE AND NOT PINK — A JUDGMENT CALL, FLAGGING IT: this build renders
Zion as a woman throughout (the stills are 'the light finds her', 'she lifts her
head', and n6 says 'she'). It is tempting to give verse 14 the pink WOMAN voice.
I did not. Zion is a city spoken of as a woman, not a woman the Bible records
speaking, and SPEAKER-LAW reserves pink for the latter. Blue is the honest call.
If Cameron would rather hear a woman's voice say verse 14 — and it would be
beautiful — it is a one-word change and his to make.

NOTE ON jv15: the verse is about a woman but it is God speaking about her, so it
is green, not pink. The speaker is the test, never the subject.

WHY-LAW: God answers the fear of being forgotten with the most physical promise
in scripture — a name cut into his own hands. Milk framing — you are not
overlooked.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "There is a particular loneliness that comes from feeling forgotten. Not hated. Just overlooked. Slipped from someone's mind, as if you never really mattered enough to be remembered."),
    # Isaiah 49:14
    ("s14", SCRIPTURE, "But Zion said, The LORD hath forsaken me, and my Lord hath forgotten me."),
    ("n2", NARRATOR, "That is exactly how God's people felt, and they said it out loud — the Lord has walked away from me, and my God has forgotten I exist. And God's answer to that fear is one of the most tender things he ever said."),
    ("n3", NARRATOR, "He points to the strongest, most instinctive love a human being knows — a mother with her newborn, unable to look away, unable to forget the child at her breast even for a moment."),
    # Isaiah 49:15
    ("jv15", GOD, "Can a woman forget her sucking child, that she should not have compassion on the son of her womb? yea, they may forget, yet will I not forget thee."),
    ("n4", NARRATOR, "Even if a mother somehow could forget — I never will. And then he says something almost too intimate to imagine. He does not just keep you in mind. He has carved you into his own hands, where he cannot help but see you."),
    # Isaiah 49:16
    ("jv16", GOD, "Behold, I have graven thee upon the palms of my hands; thy walls are continually before me."),
    ("n5", NARRATOR, "Graven — engraved, cut in deep, permanent. Not a note he might lose. You are written into the very hands of God, and everything about you is always right there in front of him. He could not forget you if he tried."),
    ("n6", NARRATOR, "And that changes the person who thought she had been left behind. The same God she feared had forgotten her was carrying her the whole time — her name, her walls, her whole life, held in his hands."),
    ("n7", NARRATOR, "So if you have ever felt like the one who gets forgotten — the one nobody keeps in mind — hear this slowly."),
    ("n7b", NARRATOR, "You are not out of sight. You are not out of mind. You are graven on the hands of God, and he has never once looked away."),
    ("card", NARRATOR, "God told the ones who felt forgotten that he had carved them into his own hands, always before his eyes. You are not overlooked. Where do you most need to hear that you have not been forgotten?"),
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
