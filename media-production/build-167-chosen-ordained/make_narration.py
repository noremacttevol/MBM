#!/usr/bin/env python3
"""Generate narration audio for Story Video #167 — "I have chosen you, and ordained you"
(John 15:16). MEMBER shelf verse-video. → Gospel Library topic: Callings.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY. (The Lord's own
words at the Last Supper; the scripture voice carries them. He is NOT depicted as a figure;
the one who calls is shown only as warm light from heaven — never a face or body.)

KJV lines (exact — the one verse split into two sacred silences):
  kv16a = John 15:16a  "...I have chosen you, and ordained you," (NAMED — SACRED SILENCE 1)
  kv16b = John 15:16b  "...bring forth fruit... ask of the Father in my name" (SACRED SILENCE 2)

WHY-LAW: calling — no one appoints himself to God's work; God chooses and ordains, by name,
for a purpose (fruit that lasts), and backs the calling with power. STUDY GEM: called of God,
by name — not self-chosen (n6); ties to the priesthood/authority thread.

TRANSLATION LAW: the narrator never re-quotes a KJV line. n2 paraphrases "chosen and
ordained" as "picked out and set apart"; the exact KJV lands only in kv16a/kv16b.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Callings). No shame, no fear.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The people God calls to his work rarely go looking for the honour. They are usually "
     "found doing something ordinary — mending a net, carrying water, quietly living an "
     "unremarkable life, never dreaming of appointing themselves to anything."),
    # kv16a — NAMED VERSE, SACRED SILENCE 1
    ("kv16a", SCRIPTURE, "-26%", "-6Hz",
     "Ye have not chosen me, but I have chosen you, and ordained you,"),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Notice the direction of it. The choosing runs from heaven down to us, not the other "
     "way. He picks a person out, calls them by their own name, and sets them apart with "
     "real authority for a work that is his to give."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "And a calling is never just a title to wear. It is a sending. Those he chose were "
     "meant to go — out to the roads and the villages, to actually do the thing they had "
     "been set apart to do."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "The measure of it would be simple and real: fruit. Not applause, not a position, but "
     "honest results — good work done, and people lifted and gathered in, like a harvest "
     "brought home."),
    # kv16b — SACRED SILENCE 2
    ("kv16b", SCRIPTURE, "-26%", "-6Hz",
     "that ye should go and bring forth fruit, and that your fruit should remain: that "
     "whatsoever ye shall ask of the Father in my name, he may give it you."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And what fruit it was to be: not a flash that fades, but a harvest that lasts. Better "
     "still, the calling came backed with power — so that what these called ones asked of "
     "heaven, in the proper way, heaven would answer and give."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Here is the quiet study gem. You do not license yourself into God's service, and you "
     "do not have to. He calls of his own choosing, by name, and ordains for the work. To "
     "be called of God is a gift you receive, not a badge you take."),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "And that call still goes out, still by name, still to ordinary people who never went "
     "looking for it. When heaven singles you out and calls you by your own name, will you "
     "look up, and answer?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "You do not choose yourself into God's work — he chooses and ordains, by name, for "
     "fruit that lasts. When heaven calls you by your own name, will you look up, and "
     "answer?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
