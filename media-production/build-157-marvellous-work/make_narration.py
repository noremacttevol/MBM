#!/usr/bin/env python3
"""Generate narration audio for Story Video #157 — "A marvellous work and a wonder;
the sealed book" (Isaiah 29:11-14). MEMBER shelf verse-video.
→ Gospel Library topic: Book of Mormon.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY.
(Isaiah is Old-Testament prophecy; the scripture voice carries the verse. Christ is
NOT depicted; God's marvellous work is shown only as light. Keep entirely in Isaiah's
ANCIENT imagery — no modern objects, no modern books, no named modern events; the
Gospel Library pointer on the closing card carries the connection.)

KJV lines (exact):
  kv11 = Isa 29:11  a book that is sealed... I cannot; for it is sealed (SACRED SILENCE 1)
  kv14 = Isa 29:14  a marvellous work and a wonder (NAMED VERSE — SACRED SILENCE 2)

WHY-LAW: hope — when human wisdom runs out, God is only getting started; he opens what
men sealed and reaches hearts that wandered. STUDY GEMS: neither the learned nor the
unlearned can open it alone (n3-n4); the deeper problem is hearts drawn far off (n5); no
cleverness fixes that (n6); God does the marvel himself (n7).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n1 says "like a book that is
sealed shut," delivered as paraphrase; the exact KJV lands only in kv11/kv14.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Book of Mormon). No shame, no mocking any group.
CHRIST IS NEVER DEPICTED; the marvellous work is shown only as warm light.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The prophet Isaiah painted a strange, almost sad picture of his people. The truth "
     "of God, he said, had become to them like a book that is sealed shut — right there "
     "in their hands, and yet closed, its meaning locked away."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Imagine a precious book, clasped and sealed, that no one around can open. Everyone "
     "senses it matters. No one can get inside it. The words of heaven, sitting sealed "
     "in the middle of them."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "So they carry it to their most educated man, the scholar everyone respects, and "
     "they say, please, read this for us. He turns it over in his hands, and has to "
     "admit the plain truth: he cannot. It is sealed."),
    # kv11 — SACRED SILENCE 1
    ("kv11", SCRIPTURE, "-26%", "-6Hz",
     "And the vision of all is become unto you as the words of a book that is sealed, "
     "which men deliver to one that is learned, saying, Read this, I pray thee: and he "
     "saith, I cannot; for it is sealed:"),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Then they hand it to a plain, unschooled man, hoping simple honesty might succeed "
     "where learning failed. But he only shakes his head kindly. Neither the wise nor "
     "the simple can open it on their own."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Isaiah saw the deeper trouble underneath. The people still said the right words "
     "and kept the outward forms, honouring God with their lips — but their hearts had "
     "quietly drifted far away, and their worship had shrunk to habits taught by men."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And no amount of human cleverness was going to fix that. The wisdom of the wise "
     "had run to the very end of itself. The experts had no key for a sealed book, or "
     "for a heart that had wandered off."),
    # kv14 — NAMED VERSE, SACRED SILENCE 2
    ("kv14", SCRIPTURE, "-26%", "-6Hz",
     "Therefore, behold, I will proceed to do a marvellous work among this people, even "
     "a marvellous work and a wonder: for the wisdom of their wise men shall perish, and "
     "the understanding of their prudent men shall be hid."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "So God promised to step in himself and do something marvellous — a genuine wonder. "
     "Not one more lecture from the learned, but an act of God that would open what men "
     "had sealed and reach hearts that had wandered."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "That is the beautiful turn in this verse. When human wisdom hits its limit, God is "
     "only getting started. He is fond of marvellous works and wonders — the very things "
     "the experts said could not happen. So the only question is a hopeful one. When the "
     "wonder comes, will you be humble enough to receive it?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "When human wisdom runs dry and the book is sealed, God promises a marvellous work "
     "and a wonder — opening what men could not, and reaching hearts that had wandered. "
     "When the wonder comes, will you receive it?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
