#!/usr/bin/env python3
"""Generate narration audio for Story Video #164 — "Till we all come in the unity of
the faith" (Ephesians 4:11-14). MEMBER shelf verse-video. → Gospel Library topic: Apostles.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY. (Paul's epistle;
the scripture voice carries the verses. Christ is NOT depicted as a figure; he is shown
only as warm light from heaven — never a face or body.)

KJV lines (exact):
  kv11 = Eph 4:11  apostles, prophets, evangelists, pastors and teachers (SACRED SILENCE 1)
  kv13 = Eph 4:13  till we all come in the unity of the faith (NAMED VERSE — SACRED SILENCE 2)

WHY-LAW: holy order + growth — the risen Lord gave his church living leaders as gifts, to
build his people up until they all reach one faith and full maturity. STUDY GEM: those
offices were never meant to be temporary — they are given "till we all come" to that unity,
and the church has not yet arrived; the alternative is to stay children, tossed about by
every wind of teaching (n5).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n2 paraphrases v12, n3/n4 lead to
v13, n5 paraphrases v14; the exact KJV lands only in kv11/kv13.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Apostles). No shame, no fear.

HOMOGRAPH NOTE: "wind of teaching" — noun /wind/ (moving air), read correctly by Andrew in
this context; no override needed. No other flagged homographs present.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "When the risen Lord returned to heaven, he did not leave his church leaderless and "
     "on its own. From above, he poured out gifts on his people — and the greatest of "
     "those gifts were living leaders, given to shepherd and to teach."),
    # kv11 — SACRED SILENCE 1
    ("kv11", SCRIPTURE, "-24%", "-6Hz",
     "And he gave some, apostles; and some, prophets; and some, evangelists; and some, "
     "pastors and teachers;"),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "He gave them for a reason. Their whole calling was to mend and mature the ordinary "
     "believers — to do the work of the ministry, and to build up the body until it stood "
     "strong and whole."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "So the people were never meant to be a scattered crowd. Taught and strengthened, "
     "they were knit together, growing closer, becoming one body that could bear one "
     "another up."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "And there was a destination in view. All of them were being drawn toward the same "
     "place — one shared faith, one true knowledge of the Son of God, a people grown at "
     "last into full and finished maturity."),
    # kv13 — NAMED VERSE, SACRED SILENCE 2
    ("kv13", SCRIPTURE, "-26%", "-6Hz",
     "Till we all come in the unity of the faith, and of the knowledge of the Son of God, "
     "unto a perfect man, unto the measure of the stature of the fulness of Christ:"),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Paul set the opposite right beside it. Without that steady leading, believers stay "
     "children — pushed back and forth, carried off by every new wind of teaching, easy "
     "prey for clever men who lie in wait to fool them."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Here is the quiet study gem. If those leaders were given until we ALL arrive at that "
     "unity, and the church has plainly not arrived yet, then the gifts were never meant "
     "to be temporary. His people still need apostles and prophets to keep them from "
     "drifting."),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "And that is where it leaves you. You were never meant to grow up alone, or to be "
     "blown about by whatever is newest. You are meant to grow up in this, together, into "
     "one settled faith. When he offers you a place in it, will you come and grow?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "The risen Lord gave his church apostles and prophets, pastors and teachers — to "
     "build his people up until they all come to one faith and full maturity. When he "
     "offers you a place in it, will you come and grow?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
