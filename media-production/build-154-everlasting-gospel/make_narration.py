#!/usr/bin/env python3
"""Generate narration audio for Story Video #154 — "Another angel, the everlasting
gospel" (Revelation 14:6-7). MEMBER shelf verse-video. → Gospel Library: Restoration.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY.
(Revelation is apostolic prophecy; the scripture voice carries the verse. Christ is
NOT depicted anywhere; God the Creator is shown only as light. An ANGEL — clearly
winged, not the Lord — carries the gospel.)

KJV lines (exact):
  kv6 = Rev 14:6  another angel... having the everlasting gospel (NAMED VERSE — SACRED SILENCE 1)
  kv7 = Rev 14:7  fear God... worship him that made heaven and earth (SACRED SILENCE 2)

WHY-LAW: hope, not fear — the gospel was never lost for good; heaven sent it back, on
purpose, for EVERYONE. STUDY GEMS: it is "everlasting," older than the nations, not
invented (n4); it is for every nation, kindred and tongue — no one too far or too late
(n5); the call is simply to honour and worship the Creator (n6); it was sent for you too
(n8).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n3 says "an open book, the
good news ready to be given back," never "having the everlasting gospel"; n6 says
"honour God, give him the glory," but that thought is delivered as paraphrase, and the
exact KJV lands only in kv7.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Restoration). No shame, no fear.
CHRIST IS NEVER DEPICTED; God the Creator is shown only as light. The angel is clearly
a winged heavenly messenger, never the Lord and never Jesus's face.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "For long stretches of history, whole peoples lived without it — the good news "
     "about God, misplaced, buried, or never yet heard. Men reached for heaven in the "
     "dark and could not quite find the way."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "And then, in a vision, John of Patmos saw heaven open, and something come. Not an "
     "army, not a storm, but an angel, sent on an errand of mercy, carrying a message "
     "meant for the whole earth."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "The angel flew across the height of heaven for all to see, holding out an open "
     "book: the good news about God, ready to be given back to a world that had lost "
     "hold of it."),
    # kv6 — NAMED VERSE, SACRED SILENCE 1
    ("kv6", SCRIPTURE, "-26%", "-6Hz",
     "And I saw another angel fly in the midst of heaven, having the everlasting gospel "
     "to preach unto them that dwell on the earth, and to every nation, and kindred, "
     "and tongue, and people,"),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Notice the word: everlasting. This good news was never really invented, or "
     "improved, by anyone. It is older than the nations, the same true message from the "
     "beginning, carried down from heaven and offered fresh again."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And notice who it is for. Not one favoured people, not one language or land, but "
     "every nation, every family, every tongue. No one is too far away, too foreign, or "
     "too late to be handed this."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "The angel's call is simple and clean. Honour God, give him the glory, and worship "
     "the One who made it all — the heavens, the earth, the sea, and every spring of "
     "water. Turn your face back toward your Maker."),
    # kv7 — SACRED SILENCE 2
    ("kv7", SCRIPTURE, "-26%", "-6Hz",
     "Saying with a loud voice, Fear God, and give glory to him; for the hour of his "
     "judgment is come: worship him that made heaven and earth, and the sea, and the "
     "fountains of waters."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "It is a call to come home to the God of creation — the same God who set the stars "
     "in place and filled the seas. Not a distant idea, but the Maker of the very "
     "ground under your feet, quietly asking for your heart."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "So here is the quiet wonder of this verse. The good news was never abandoned for "
     "good. Heaven sent it out again, on purpose, for everyone — which means it was "
     "sent for you, too. So the only question is a gentle one. Will you receive it?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "The gospel was never lost for good. Heaven sent an angel to carry it back to "
     "every nation, kindred, and tongue — everlasting, and meant for you. Will you "
     "receive it?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
