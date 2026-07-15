#!/usr/bin/env python3
"""Generate narration audio for Story Video #165 — "Laying on of hands for the Holy
Ghost" (Acts 8:14-17). MEMBER shelf verse-video. → Gospel Library topic: Laying On of Hands.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY. (Luke's account
in Acts; the scripture voice carries the verses. God / the Holy Ghost is NOT depicted as
a figure; heaven is shown only as warm descending light — never a face, body or dove.)

KJV lines (exact):
  kv14 = Acts 8:14  the apostles sent Peter and John (SACRED SILENCE 1)
  kv17 = Acts 8:17  they laid hands on them, and they received the Holy Ghost (NAMED — SS 2)

WHY-LAW: holy order + the gift — Samaria believed and was baptized in water, yet the Holy
Ghost had not come, because the gift is conferred by those with authority. STUDY GEM: the
apostles SENT two of their own (n2); the believers were already baptized, yet still waited
(n3); the gift came only when apostolic hands were laid on (kv17); so the gift travels by
authority, not by sincerity alone (n5).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n3 paraphrases v15-16 (prayed,
already baptized, Spirit not yet fallen) without quoting; the exact KJV lands only in
kv14/kv17.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Laying On of Hands). No shame, no fear.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "A wave of faith had swept through Samaria. Whole crowds had heard the good news, "
     "believed it with glad hearts, and been baptized in water. Something real and joyful "
     "was happening among them."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Word of it reached the apostles back in Jerusalem. And notice their response: they "
     "did not simply send a letter of congratulations. They sent two of their own number, "
     "Peter and John, to go down in person."),
    # kv14 — SACRED SILENCE 1
    ("kv14", SCRIPTURE, "-24%", "-6Hz",
     "Now when the apostles which were at Jerusalem heard that Samaria had received the "
     "word of God, they sent unto them Peter and John:"),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "When the two arrived, they prayed over the new believers, asking that they might "
     "receive the Holy Ghost. And here is the surprising part: even though these people "
     "already believed, and had already been baptized, the gift had not yet come to a "
     "single one of them."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "So the water alone had not been enough. Their faith was sincere and their baptism was "
     "real, yet the promised gift of the Spirit still waited on something more — on the hands "
     "of those God had given authority."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Then Peter and John did the simple, deliberate thing Luke records so plainly. They "
     "laid their hands on each believer. And in that moment, under that authority, the "
     "gift finally came."),
    # kv17 — NAMED VERSE, SACRED SILENCE 2
    ("kv17", SCRIPTURE, "-26%", "-6Hz",
     "Then laid they their hands on them, and they received the Holy Ghost."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Here is the quiet study gem. The gift of the Holy Ghost did not arrive by sincerity "
     "alone, or by baptism alone. It travelled by authority — conferred through the laying "
     "on of hands by those God had sent. Order and gift belong together."),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "And that same gift is still offered to you, by that same pattern. Faith and baptism "
     "open the door, and then, by the hands of those with authority, the Comforter is "
     "given to be with you. When that gift is offered to you, will you receive it?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Samaria believed and was baptized, but the Holy Ghost came only when the apostles "
     "laid their hands on them. The gift travels by authority. When that gift is offered to "
     "you, will you receive it?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
