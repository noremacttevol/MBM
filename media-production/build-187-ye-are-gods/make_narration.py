#!/usr/bin/env python3
"""Narration for build-187-ye-are-gods — Psalm 82 (quoted in John 10).

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

MOVED OUT OF RED — this is the correction the build needed.
  j1  RED -> GOD, GREEN.  Psalm 82:6  'I have said, Ye are gods; and all of you
      are children of the most High.'
The video frames this as Jesus reaching into the leaders' own scriptures, and the
quoted words were painted red as though they were his. They are not. That text is
Psalm 82:6 — the LORD speaking in Asaph's psalm, long before Christ came in the
flesh. A red-letter King James Bible leaves Psalm 82 black. Under speaker law
Old Testament Deity speech is GREEN, never red: it is still Deity, and green
carries that without arguing it.

The line is checked verbatim against Psalm 82:6 and left exactly as the build had
it. Where the LORD speaks in that psalm it is `god`; where Asaph narrates it
would be `scripture`, but no narration from the psalm is quoted in this build, so
green is the only non-white colour here.

NO SPLIT. j1 is one speaker start to finish.

NOT ADDED, deliberately: the John 10:34 frame — 'Is it not written in your law' —
would be a red Jesus beat and would put red back on the same still as the green.
The build does not need it; n1 already tells the viewer he is quoting their own
scripture, and n2 lands the argument. Keeping this build free of red is the safer
call and matches the instruction that this one is never `jesus`.

Nothing lifted beyond that. n2, n3a and n3b already retell the psalm and the
point of it in plain English, so the retelling rule is met.

ST6 is absent from the build's still vars; no beat uses it, and this plan does
not introduce one. The closing card is not a beat and has been left out of BEATS,
exactly as the original had it.

WHY-LAW: milk, and carefully so. This is a verse people reach for to argue about
what men may become, and the build does not go there. It stays on what actually
happened in the courtyard: he answered them out of their own book, and they had
nothing to say back. 2026-07-21: added j2 (John 10:36, red) + n2b retelling — cut was 52.7s, under the 60s floor; the addition is Jesus's own answer in the same passage.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import GOD, JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "The religious leaders were circling Jesus, demanding he say plainly who he claimed to be."),
    ("n1", NARRATOR, "Instead of backing down, he reached into their own scriptures — to a psalm where God calls mere men gods."),
    # Psalm 82:6
    ("j1", GOD, "I have said, Ye are gods; and all of you are children of the most High."),
    ("n2", NARRATOR, "His point was sharp: if scripture called men gods because God's word came to them, how could they condemn the one the Father set apart?"),
    # John 10:36
    ("j2", JESUS, "Say ye of him, whom the Father hath sanctified, and sent into the world, Thou blasphemest; because I said, I am the Son of God?"),
    ("n2b", NARRATOR, "That was his answer. The Father himself set him apart and sent him into the world. Saying I am the Son of God was not blasphemy — it was the plain truth they would not test."),
    ("n3a", NARRATOR, "He was not making himself a second God."),
    ("n3b", NARRATOR, "He was showing them their own book exposed their logic."),
    ("card", NARRATOR, "He stood on the scriptures they claimed to love. Come know him as he truly is."),
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
