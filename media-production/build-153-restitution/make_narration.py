#!/usr/bin/env python3
"""Generate narration audio for Story Video #153 — "The times of restitution of all
things" (Acts 3:19-21). MEMBER shelf verse-video. → Gospel Library topic: Restoration.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY.
(Acts is apostolic history; the scripture voice carries Peter's words / the verse.
Christ is NOT depicted anywhere in this video; heaven is shown only as light.)

KJV lines (exact):
  kv19 = Acts 3:19  repent... when the times of refreshing shall come (SACRED SILENCE 1)
  kv21 = Acts 3:21  the times of restitution of all things (NAMED VERSE — SACRED SILENCE 2)

WHY-LAW: hope, not fear — the world is not just winding down into ruin; God has
promised to set ALL things right, a restoration foretold by every prophet. STUDY GEMS:
turning back brings "times of refreshing" now (n2-n3); heaven holds the promise until
the appointed day (n5); every prophet foretold the same great restoring (n6);
restitution means made whole, made new, not merely patched (n7).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n2 says "let your wrongs be
wiped away," never "your sins may be blotted out"; n7 says "made whole, made new,"
never "restitution of all things" as a quote.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Restoration). No shame, no fear.
CHRIST IS NEVER DEPICTED; heaven/God is shown only as light, never a figure or face.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "After a lame man was healed at the temple gate, a crowd came running, amazed. "
     "And Peter, a fisherman turned preacher, stood up among them to explain what they "
     "had really just seen."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "His message was not complicated. Turn back to God, he said. Change your "
     "direction, let your wrongs be wiped away, and something good will follow — not "
     "someday far off, but seasons of relief, sent from God himself."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Picture that word: refreshing. Like cool rain on cracked ground, like a deep "
     "breath after a long, hard road. That is what God longs to pour out on people who "
     "simply turn back toward him."),
    # kv19 — SACRED SILENCE 1
    ("kv19", SCRIPTURE, "-26%", "-6Hz",
     "Repent ye therefore, and be converted, that your sins may be blotted out, when "
     "the times of refreshing shall come from the presence of the Lord;"),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "But Peter pointed to something even larger than one person's fresh start. He "
     "spoke of a day when everything that has gone wrong with the world would finally "
     "be set right — a healing not only of people, but of all things."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Until that day, he said, heaven itself is keeping the promise safe, the way you "
     "hold back the best gift for exactly the right moment. It is coming, but at the "
     "appointed time, and not a moment before."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And this was not some new idea Peter dreamed up. Every true prophet, all the way "
     "back to the beginning, had promised the very same thing: a great restoring, a "
     "putting-right of everything, spoken of since the world began."),
    # kv21 — NAMED VERSE, SACRED SILENCE 2
    ("kv21", SCRIPTURE, "-26%", "-6Hz",
     "Whom the heaven must receive until the times of restitution of all things, which "
     "God hath spoken by the mouth of all his holy prophets since the world began."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Restitution means giving back what was lost, restoring what was broken to the "
     "way it was always meant to be. Not patched up, not almost — made whole, made new, "
     "every part of it."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "So this verse is a promise you can lean your full weight on. The world is not "
     "just sliding into ruin; it is heading toward a restoration God has planned from "
     "the very start. So the only question is a hopeful one. Will you turn, and be part "
     "of the refreshing when it comes?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "The world is not ending in ruin. It is heading toward a restoration of all "
     "things, promised by every prophet since the beginning. Turn back to God, and be "
     "refreshed. Will you be ready for the restoring?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
