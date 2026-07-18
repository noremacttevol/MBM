#!/usr/bin/env python3
"""Generate narration audio for Story Video #163 — "Built on apostles and prophets"
(Ephesians 2:19-20). MEMBER shelf verse-video. → Gospel Library topic: Church Organization.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY. (Paul's epistle;
the scripture voice carries the verse. Christ is NOT depicted as a figure; he is shown
only as the glowing chief CORNERSTONE and as warm light — never a face or body.)

KJV lines (exact):
  kv19 = Eph 2:19  no more strangers... of the household of God (SACRED SILENCE 1)
  kv20 = Eph 2:20  built on the foundation of apostles and prophets (NAMED VERSE — SACRED SILENCE 2)

WHY-LAW: belonging + order — the church is not a shapeless crowd; it has a real design
(foundation of apostles and prophets, Christ the cornerstone), and you belong in it. STUDY
GEMS: those once far off are brought near, made family (n2); a household needs a house built
right (n4); the foundation is apostles and prophets (n5); the cornerstone that keeps it
square is Christ (n6); you have a fitted place in it (n8).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n3 says "part of a household,"
delivered as paraphrase; the exact KJV lands only in kv19/kv20.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Church Organization). No shame, no fear.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The people Paul was writing to had once been outsiders — foreigners, strangers, on "
     "the far edge of God's promises, with no place at the table and no share in the "
     "family."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "But something had changed everything. The door had been thrown open, and those who "
     "were far off had been brought near — no longer guests to be tolerated, but family "
     "to be embraced."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Paul reached for a beautiful picture: they were now part of a household — the very "
     "household of God. Not a crowd of strangers passing through, but sons and daughters "
     "at home, belonging."),
    # kv19 — SACRED SILENCE 1
    ("kv19", SCRIPTURE, "-26%", "-6Hz",
     "Now therefore ye are no more strangers and foreigners, but fellowcitizens with the "
     "saints, and of the household of God;"),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "But a household needs a house — and a house needs to be built, and built right. So "
     "Paul changed the picture from a family to a building, the dwelling place of God "
     "among his people."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Every real building rests on a foundation. And this one, Paul said, was laid on the "
     "apostles and the prophets — men God had called and taught, whose witness became the "
     "solid ground the whole structure would stand on."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And at the most important place of all — the cornerstone, the stone that sets the "
     "angle, holds two walls together, and keeps the whole building square and true — "
     "stood Christ himself. Everything is lined up to him."),
    # kv20 — NAMED VERSE, SACRED SILENCE 2
    ("kv20", SCRIPTURE, "-26%", "-6Hz",
     "And are built upon the foundation of the apostles and prophets, Jesus Christ "
     "himself being the chief corner stone;"),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "So the church was never meant to be a loose, shapeless crowd. It has a design — a "
     "foundation of apostles and prophets, a cornerstone that is Christ, and living "
     "people fitted together into a home for God. There is a blueprint."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "And the best part is where that leaves you. You are not a stranger at the door. In "
     "this house you have a place, fitted in and belonging, part of what God is building. "
     "So the only question is a hopeful one. When he offers you a place in it, will you "
     "come inside?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "You are no longer a stranger, but part of the household of God — a building laid on "
     "apostles and prophets, with Christ the cornerstone holding it all together. When he "
     "offers you a place in it, will you come inside?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
