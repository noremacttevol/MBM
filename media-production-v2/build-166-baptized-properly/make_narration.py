#!/usr/bin/env python3
"""Narration for build-166-baptized-properly — Acts 19.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Both red segments were misattributions. Acts 19 is Luke narrating and Paul
speaking; the risen Christ does not speak here at all. kv5 and kv6 both move
JESUS-RED -> SCRIPTURE (light blue). Two lines out of red.

kv6 was checked specifically for the mixed-segment case and it is NOT mixed:
'And when Paul had laid his hands upon them, the Holy Ghost came on them; and
they spake with tongues, and prophesied' is Luke narrating from the first word
to the last. A red-letter KJV prints none of it red. It stays one segment,
SCRIPTURE throughout. Nothing in this build was split.

Two verses lifted out of narrator paraphrase so the exchange is heard rather
than described:
  s2  Acts 19:2  Paul's question and the disciples' answer
  s4  Acts 19:4  Paul explaining what John's baptism was for
Acts 19:2 contains two speakers (Paul, then the Ephesian disciples) plus Luke's
'He said unto them' / 'And they said unto him'. All three are SCRIPTURE, so the
single light-blue colour is correct for the whole verse and no split is needed.
Each lift is followed by the existing narrator beat that already retells it
(n2 retells s2, n3 retells s4).

All original ids kept. New ids are s2 and s4 only. New beats reuse S2 and S3;
no new artwork.

MILK: the point — baptism by proper authority, then the gift by the laying on of
hands — is carried by verses 5 and 6 standing side by side. The narration never
argues that their first baptism was invalid; it only says Paul set it right, and
lets Luke's own sentence do the rest.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, 'Paul came through the inland country and arrived at Ephesus, where he found a small group of disciples. They were sincere. They already believed. By every outward sign they looked like people who were fully in.'),
    ("s2", SCRIPTURE, 'He said unto them, Have ye received the Holy Ghost since ye believed? And they said unto him, We have not so much as heard whether there be any Holy Ghost.'),
    ("n2", NARRATOR, 'But Paul asked them a searching question: And their answer was startling.'),
    ("s4", SCRIPTURE, 'Then said Paul, John verily baptized with the baptism of repentance, saying unto the people, that they should believe on him which should come after him, that is, on Christ Jesus.'),
    ("n3", NARRATOR, 'So Paul asked what baptism they had been given. They had known only the baptism of John — a real and honest baptism of repentance, but a preparation, meant to point people forward to the one who was still to come.'),
    ("n4", NARRATOR, 'Here is the tender thing: these were good, believing people, and yet something was genuinely missing. Their baptism had prepared them, but it had not been the full ordinance done under the authority now given. So Paul set it right.'),
    ("kv5", SCRIPTURE, 'When they heard this, they were baptized in the name of the Lord Jesus.'),
    ("n5", NARRATOR, 'And baptism was not the final step. There was one thing more, the same step we have seen before: the laying on of hands by one who held the authority to give the gift.'),
    ("kv6", SCRIPTURE, 'And when Paul had laid his hands upon them, the Holy Ghost came on them; and they spake with tongues, and prophesied.'),
    ("n6", NARRATOR, 'Here is the quiet study gem. Their sincerity was never in doubt, and it was never enough on its own. The ordinance still had to be done right, by one who was sent. Sincerity did not replace authority — it was completed by it.'),
    ("n7", NARRATOR, 'And the same careful pattern is offered to you: not a vague good feeling, but a real baptism by proper authority, and then the gift of the Spirit by the laying on of hands. When that pattern is offered to you, will you follow it in?'),
    ("card", NARRATOR, 'Sincere disciples at Ephesus were baptized again, properly, and received the Holy Ghost when Paul laid his hands on them. Sincerity did not replace authority. When that pattern is offered to you, will you follow it in?'),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}
SPOKEN.update({'sincerity': 'sin serity', 'Sincerity': 'Sin serity'})  # 2026-07-21: recorded takes kept coming out "sensarity" (n6+card, and again with 'sinserrity'); 'sin serity' is STABLE 3/3 in Andrew and round-trips "sin-SERR-ity". Captions unchanged.


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
