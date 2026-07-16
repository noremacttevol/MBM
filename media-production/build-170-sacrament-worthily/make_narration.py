#!/usr/bin/env python3
"""Generate narration audio for Story Video #170 — "The sacrament, worthily"
(1 Corinthians 11:23-29). MEMBER shelf verse-video. → Gospel Library topic: Sacrament.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY. (Paul recounting the
Lord's own words at the supper; the scripture voice carries them. Christ is NOT depicted as a
figure; his presence at the table is shown only as warm light — never a face or body.)

KJV lines (exact):
  kv24 = 1 Cor 11:24  the bread: this is my body... in remembrance of me (NAMED — SACRED SILENCE 1)
  kv25 = 1 Cor 11:25  the cup: this cup is the new testament in my blood (SACRED SILENCE 2)

WHY-LAW: remembrance + covenant renewal — bread and cup taken in remembrance; a covenant renewed
again and again, week by week. STUDY GEM: it repeats because it is a covenant RENEWED, a regular
chance to be made clean and begin fresh (n6).

CARE — WORTHINESS IS MILK: the passage's "unworthily... damnation" (v27,29) is framed ONLY as a
tender invitation to examine your own heart and come sincerely (n5). No threat, no shame.

TRANSLATION LAW: the narrator never re-quotes a KJV line. The exact KJV lands only in kv24/kv25.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Sacrament). No shame, no fear.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Paul was handing on something sacred that he had received himself: on the very night "
     "he was betrayed, at supper with his friends, the Master took a simple loaf of bread "
     "into his hands and gave thanks over it."),
    # kv24 — NAMED VERSE, SACRED SILENCE 1
    ("kv24", SCRIPTURE, "-26%", "-6Hz",
     "And when he had given thanks, he brake it, and said, Take, eat: this is my body, which "
     "is broken for you: this do in remembrance of me."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Then he lifted the cup. This one, he said, was the sign of a new covenant — a solemn "
     "promise sealed between God and his people, and offered freely to them."),
    # kv25 — SACRED SILENCE 2
    ("kv25", SCRIPTURE, "-26%", "-6Hz",
     "After the same manner also he took the cup, when he had supped, saying, This cup is the "
     "new testament in my blood: this do ye, as oft as ye drink it, in remembrance of me."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Ever since, his people have taken that same bread and that same cup together, quietly, "
     "reverently — a small, holy act of remembering the One who gave everything for them."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And it looks in two directions at once. Every time we take it, we are remembering a "
     "sacrifice already made, and we are looking forward, in hope, to the day he returns."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Paul asked for just one thing beforehand, and he asked it gently: that each person "
     "pause and look honestly into his own heart, and come sincerely. Not to keep anyone "
     "away, but so the moment stays real and tender."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Here is the quiet study gem. This is why it is done again and again, and never just "
     "once. It is a covenant renewed — week after week, a fresh chance to be made clean, to "
     "set down the past and begin again."),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "And a place at that table is kept for you. Not for the perfect, but for the sincere — "
     "for anyone willing to come and remember. When the bread and the cup are offered to "
     "you, will you come to the table?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "The bread and the cup are taken in remembrance — a covenant renewed again and again, a "
     "fresh chance to be made clean. Not for the perfect, but for the sincere. When they are "
     "offered to you, will you come to the table?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
