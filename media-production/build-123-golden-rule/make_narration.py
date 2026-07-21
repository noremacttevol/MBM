#!/usr/bin/env python3
"""Narration for build-123-golden-rule — Matthew 7.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

BOTH RED BEATS STAY RED. Nothing moved out of red in this build.
  jvA  Matthew 7:12 — the golden rule, Jesus on the mount. Verified verbatim,
       whole verse, nothing trimmed.
  jvB  Luke 6:38 — this is NOT Matthew. It is the Sermon on the Plain, and it
       is still Jesus speaking in the flesh, so it is still red. The verse
       reference is now recorded on the beat so the cross-book jump is
       visible to anyone reading the plan rather than silently wrong. Text
       checked against the KJV: it ends at a real sentence boundary
       ('...into your bosom.'), so the partial quote is honest.

NOTE ON THE QUOTED LAW: 'for this is the law and the prophets' is Jesus
citing the whole Old Testament inside his own sentence. It stays red. He is
the one talking — citing the law does not hand the microphone to the law.

NO MIXED SEGMENTS. Neither red beat has a narration frame welded to it.

RETELLING: n2 now opens by retelling jvA directly in plain English before
continuing word for word as it was, and n3 through n6 spend four beats
working it out in everyday terms — bread, water, mercy, lifting someone off
the road. n7 gained an opening sentence that retells jvB literally (good
measure, pressed down, shaken together, running over) before the rest of n7
continues unchanged. Nothing else in the narrator text was touched.

NOTHING LEFT AS PARAPHRASE FROM UNCERTAINTY.

WHY-LAW: the golden rule is not one more weight. It is the short way to
everything the law was reaching for. Milk framing — you already know how you
want to be treated, so you already know what to do.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "Of everything Jesus taught on that hillside, he gave the whole law of how to treat each other in a single sentence — one so simple a child can live it, and so deep it holds up everything else."),
    # Matthew 7:12
    ("jvA", JESUS, "Therefore all things whatsoever ye would that men should do to you, do ye even so to them: for this is the law and the prophets."),
    ("n2", NARRATOR, "However you wish people would treat you, he said — go and treat them that way. That is the law and the prophets, the whole of it, in one line. And every one of us already knows how we long to be treated. To be seen when we are tired. To be fed when we are hungry. To be forgiven when we have failed. That longing is not selfish — it is the measuring line."),
    ("n3", NARRATOR, "So Jesus turns it outward. The bread you wish someone would hand you when you are empty — hand it to the next person you find standing at your door with nothing."),
    ("n4", NARRATOR, "The cool drink you would want on a long, dusty road — be the one who holds it out to the stranger before he even thinks to ask."),
    ("n5", NARRATOR, "And the mercy you would ache for if it were your own mistake laid bare — give that first, and give it fully, to the person who wronged you."),
    ("n6", NARRATOR, "When someone stumbles on the road ahead of you, do not step around him. Lift him the way you would want to be lifted if it were your own knees in the dust."),
    # Luke 6:38
    ("jvB", JESUS, "Give, and it shall be given unto you; good measure, pressed down, and shaken together, and running over, shall men give into your bosom."),
    ("n7", NARRATOR, "Give, he said, and it will be given back to you — a full measure, packed down, shaken together to make room for more, and spilling over the sides into your lap. That is the quiet secret of it. A life poured out in kindness does not run dry. It comes back around — table to table, neighbor to neighbor — until a whole village is carrying one another."),
    ("n8", NARRATOR, "The golden rule is not a weight Jesus laid on us. It is the shortest way to everything the law was ever trying to teach. Treat others the way you long to be treated, and you will have kept nearly all of it at once."),
    ("card", NARRATOR, "Jesus folded the whole law into one line you can start living today. Before you decide how to treat someone, picture how you would want to be treated in their place — then simply do that. Who is the one person, this week, you could treat the way you have always wished someone would treat you?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
