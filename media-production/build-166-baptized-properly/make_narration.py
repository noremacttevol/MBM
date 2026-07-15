#!/usr/bin/env python3
"""Generate narration audio for Story Video #166 — "Baptized again, properly"
(Acts 19:1-6). MEMBER shelf verse-video. → Gospel Library topic: Baptism.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY. (Luke's account
in Acts; the scripture voice carries the verses. God / the Holy Ghost is NOT depicted as
a figure; heaven is shown only as warm light — never a face, body or dove.)

KJV lines (exact):
  kv5 = Acts 19:5  they were baptized in the name of the Lord Jesus (NAMED — SACRED SILENCE 1)
  kv6 = Acts 19:6  Paul laid hands, they received the Holy Ghost, spake with tongues (SS 2)

WHY-LAW: holy order — sincere disciples at Ephesus had only John's preparatory baptism and
had never heard of the Holy Ghost; they were baptized again, properly, by authority, and
received the gift when Paul laid hands on them. STUDY GEM: sincerity did not replace
authority; the ordinance had to be done right, by one sent (n6).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n2 paraphrases v2, n3-n4 paraphrase
v3-4; the exact KJV lands only in kv5/kv6.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Baptism). No shame, no fear.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Paul came through the inland country and arrived at Ephesus, where he found a small "
     "group of disciples. They were sincere. They already believed. By every outward sign "
     "they looked like people who were fully in."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "But Paul asked them a searching question: had they received the Holy Ghost since they "
     "believed? And their answer was startling. They had not so much as heard that there "
     "was a Holy Ghost to receive."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "So Paul asked what baptism they had been given. They had known only the baptism of "
     "John — a real and honest baptism of repentance, but a preparation, meant to point "
     "people forward to the one who was still to come."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Here is the tender thing: these were good, believing people, and yet something was "
     "genuinely missing. Their baptism had prepared them, but it had not been the full "
     "ordinance done under the authority now given. So Paul set it right."),
    # kv5 — NAMED VERSE, SACRED SILENCE 1
    ("kv5", SCRIPTURE, "-26%", "-6Hz",
     "When they heard this, they were baptized in the name of the Lord Jesus."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And baptism was not the final step. There was one thing more, the same step we have "
     "seen before: the laying on of hands by one who held the authority to give the gift."),
    # kv6 — SACRED SILENCE 2
    ("kv6", SCRIPTURE, "-26%", "-6Hz",
     "And when Paul had laid his hands upon them, the Holy Ghost came on them; and they "
     "spake with tongues, and prophesied."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "Here is the quiet study gem. Their sincerity was never in doubt, and it was never "
     "enough on its own. The ordinance still had to be done right, by one who was sent. "
     "Sincerity did not replace authority — it was completed by it."),
    ("n7", NARRATOR, "-24%", "-4Hz",
     "And the same careful pattern is offered to you: not a vague good feeling, but a real "
     "baptism by proper authority, and then the gift of the Spirit by the laying on of "
     "hands. When that pattern is offered to you, will you follow it in?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Sincere disciples at Ephesus were baptized again, properly, and received the Holy "
     "Ghost when Paul laid his hands on them. Sincerity did not replace authority. When "
     "that pattern is offered to you, will you follow it in?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
