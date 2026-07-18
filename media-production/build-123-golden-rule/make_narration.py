#!/usr/bin/env python3
"""Narration audio for Video #123 — The Golden Rule (Matthew 7:12).

Narrator: en-US-AndrewNeural. Jesus's voice: en-US-ChristopherNeural (exact KJV only).
Jesus is never shown, but these are HIS words, so they are in the scripture voice and render
cream-italic; the narrator frames the illustration.

Jesus's KJV lines (Christopher, cream italic):
  jvA  Matt 7:12  "Therefore all things whatsoever ye would that men should do to you, do ye
                   even so to them: for this is the law and the prophets." — sacred silence 1
  jvB  Luke 6:38  "Give, and it shall be given unto you; good measure, pressed down, and
                   shaken together, and running over, shall men give into your bosom."
                   — sacred silence 2 (the companion promise: kindness returns)

CARE FLAGS: none (GREEN). Plain milk — a teaching, not a scene of violence or grief.

WHY-LAW: The golden rule is not a burden but a shortcut — the whole law folded into one line a
child can live. Before deciding how to treat someone, picture how you would want to be treated
in their place, then do that. Milk framing: warm, invitational, never a scolding; the reciprocity
of Luke 6:38 is a promise of abundance, not a transaction you earn.

HOMOGRAPH EAR-CHECK: 'bosom' (KJV, scripture voice) reads fine; 'measure' clear; no 'read'/'bow'/
'lead' traps. NUMBER-STRESS LAW: no numbers in the script.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Of everything Jesus taught on that hillside, he gave the whole law of how to treat each "
     "other in a single sentence — one so simple a child can live it, and so deep it holds up "
     "everything else.", None),
    # jvA — Matt 7:12 — sacred silence 1
    ("jvA", JESUS, "-26%", "-6Hz",
     "Therefore all things whatsoever ye would that men should do to you, do ye even so to "
     "them: for this is the law and the prophets.", None),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Every one of us already knows how we long to be treated. To be seen when we are tired. To "
     "be fed when we are hungry. To be forgiven when we have failed. That longing is not selfish "
     "— it is the measuring line.", None),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "So Jesus turns it outward. The bread you wish someone would hand you when you are empty — "
     "hand it to the next person you find standing at your door with nothing.", None),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "The cool drink you would want on a long, dusty road — be the one who holds it out to the "
     "stranger before he even thinks to ask.", None),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And the mercy you would ache for if it were your own mistake laid bare — give that first, "
     "and give it fully, to the person who wronged you.", None),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "When someone stumbles on the road ahead of you, do not step around him. Lift him the way "
     "you would want to be lifted if it were your own knees in the dust.", None),
    # jvB — Luke 6:38 — sacred silence 2
    ("jvB", JESUS, "-26%", "-6Hz",
     "Give, and it shall be given unto you; good measure, pressed down, and shaken together, "
     "and running over, shall men give into your bosom.", None),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "That is the quiet secret of it. A life poured out in kindness does not run dry. It comes "
     "back around — table to table, neighbor to neighbor — until a whole village is carrying one "
     "another.", None),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "The golden rule is not a weight Jesus laid on us. It is the shortest way to everything the "
     "law was ever trying to teach. Treat others the way you long to be treated, and you will "
     "have kept nearly all of it at once.", None),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Jesus folded the whole law into one line you can start living today. Before you decide how "
     "to treat someone, picture how you would want to be treated in their place — then simply do "
     "that. Who is the one person, this week, you could treat the way you have always wished "
     "someone would treat you?", None),
]


async def main():
    for name, voice, rate, pitch, text, cap in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    import os
    os.makedirs("audio", exist_ok=True)
    asyncio.run(main())
