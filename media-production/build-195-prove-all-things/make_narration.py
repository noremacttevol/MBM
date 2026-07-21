#!/usr/bin/env python3
"""Narration for build-195-prove-all-things — 1 Thessalonians 5.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

1 Thessalonians 5:21-22. Both red beats move to BLUE.

  s1  1 Thessalonians 5:21  'Prove all things; hold fast that which is good.'  RED -> SCRIPTURE
  s2  1 Thessalonians 5:22  'Abstain from all appearance of evil.'             RED -> SCRIPTURE

First Thessalonians is an epistle. Paul is writing, in his own voice, to a young
congregation - these are two lines from the rapid-fire string of instructions
that closes the letter. A red-letter King James Bible prints no red in First
Thessalonians 5. Both beats were misattributed and both go light blue.

No splits. Each segment is a single short imperative from a single writer; there
is nothing mixed to cut.

Verbatim: both are word for word KJV, including the semicolon in verse 21 and
'appearance' in verse 22. Neither was smoothed or modernised. Note for the
validator's benefit - these two lines carry no thee/thou/hath markers at all,
because Paul happened to write them plainly and the KJV translators had nothing
archaic to render. They are still exact; a viewer can open to 1 Thessalonians 5
and find them.

Retelling: already covered. n1 retells 'prove all things' and n2 retells 'hold
fast that which is good', both immediately after s1. n4 follows s2 and carries
the whole pair into modern English. n3 is the setup between them. No new
narration was needed.

Nothing lifted from paraphrase. n3's 'the shortest fence he ever built' is the
storyteller's own line, not a buried quotation, and stays white.

Ids and beats unchanged. The card is 'card' and stays out of beats, as the
original had it. Note the original CARD_HOLD here was 8.0 seconds, the longest in
this set - worth a look in the dead-air pass, but out of scope for a speaker plan.

WHY-LAW: milk. Faith that checks is not weak faith. Test it, then keep what is
good - that is an invitation to think, not a warning to obey.

ENRICHED 2026-07-18: the video ran 55.0s against a 60.5s floor because it only had two verses. It reached 60s before by holding the closing card 8s — the dead air this pass removes. Added 5:19-20, which is the ACTUAL lead-in Paul writes immediately before 'Prove all things' and the video skipped entirely, and 5:24 as a warm close. Both verbatim, both with the narrator's retelling. Content now carries the runtime instead of padding.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "Paul gave the early church a short, sharp command about what to believe and what to keep."),
    # 1 Thessalonians 5:19-20
    ("s19", SCRIPTURE, "Quench not the Spirit. Despise not prophesyings."),
    ("n0b", NARRATOR, "Don't put out the Spirit's fire, he said. And don't wave away a word from God just because it came through a person. Then, in the very next breath, he told them how to handle it."),
    # 1 Thessalonians 5:21
    ("s1", SCRIPTURE, "Prove all things; hold fast that which is good."),
    ("n1", NARRATOR, "Test everything, he said. Don't swallow every voice — weigh it, hold it up to the light."),
    ("n2", NARRATOR, "And when you find what is genuinely good, cling to it. Don't let it slip."),
    ("n3", NARRATOR, "He paired it with a warning — and it's the shortest fence he ever built:"),
    # 1 Thessalonians 5:22
    ("s2", SCRIPTURE, "Abstain from all appearance of evil."),
    ("n4", NARRATOR, "The same word fits now: a faith that checks, then commits — that's steady, not gullible."),
    # 1 Thessalonians 5:24
    ("s24", SCRIPTURE, "Faithful is he that calleth you, who also will do it."),
    ("n5", NARRATOR, "The One who calls you is faithful — and He will finish what He started in you. You are not asked to weigh it all on your own strength."),
    ("card", NARRATOR, "Weigh it, then hold it. The good He shows you is worth keeping — reach for it."),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


SPOKEN.update({'calleth': 'kawleth'})  # Cameron complaints #10/#108 2026-07-21, in-context verified (kawleth/leedeth/messyeus)

SPOKEN.update({'quench': 'kwench'})  # round2 in-context A/B winners 2026-07-20 (SWEEP/round2-state.json)

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
