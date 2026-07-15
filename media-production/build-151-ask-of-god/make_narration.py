#!/usr/bin/env python3
"""Generate narration audio for Story Video #151 — "If any of you lack wisdom,
let him ask of God" (James 1:5-6). MEMBER shelf verse-video.
→ Gospel Library topic: Restoration.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY.
(James is apostolic epistle, not red-letter words of Jesus; the scripture voice
carries the verse itself. Christ is NOT depicted anywhere in this video.)

KJV lines (exact):
  kv5 = James 1:5  if any of you lack wisdom, let him ask of God (NAMED VERSE — SACRED SILENCE 1)
  kv6 = James 1:6  but let him ask in faith, nothing wavering (SACRED SILENCE 2)

WHY-LAW: reassurance, not pressure — when you don't know, you are not stuck; God
gives wisdom to ANYONE who asks, generously and without scolding. STUDY GEMS:
he giveth to ALL men (n5); LIBERALLY, not a measured trickle (n5); and upbraideth
NOT — no shame for asking, for not knowing, or for coming late (n6); the promise on
the end is "it shall be given," not "maybe" (n8).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n3 says "you can go
straight to the One who made you and ask," never "let him ask of God"; n5 says
"he gives to everyone, openly," never "giveth to all men liberally."

MILK FRAMING: an invitation. The closing card ends on an open question and a
one-line pointer to the Gospel Library topic (Restoration). No shame, no pressure.
CHRIST IS NEVER DEPICTED; God is shown only as light, never a figure or face.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the question too big for us ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Sooner or later, every one of us reaches a question too big for us. A fork in "
     "the road, a choice we cannot reason our way through, a doubt we cannot settle "
     "on our own. We lack wisdom, and trying harder does not seem to give it."),
    # --- s2: asking everyone, coming away confused ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "When that happens, most of us ask everyone around us. Friends, teachers, the "
     "loudest voices in the crowd. And often we come away more tangled than before, "
     "because the answers all disagree with each other."),
    # --- s3: another door — ask God himself ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "But there is another door, and it has been standing open the whole time. You "
     "can go straight to the One who made you and simply ask. Not only a teacher, "
     "not only a book, but God himself, directly."),
    # --- s4: kv5 — NAMED VERSE, SACRED SILENCE 1 ---
    ("kv5", SCRIPTURE, "-26%", "-6Hz",
     "If any of you lack wisdom, let him ask of God, that giveth to all men "
     "liberally, and upbraideth not; and it shall be given him."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "So a young man does the plainest thing there is. He finds a quiet place away "
     "from the noise, he kneels down, and he asks. Honestly, out loud, the way a "
     "child asks a father who is glad to be asked."),
    # --- s5: giveth to all men liberally ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Now look at how God is described here. He gives to everyone who asks. Not "
     "grudgingly, not a thin trickle measured out drop by drop, but openly and "
     "generously, more than the person even came for."),
    # --- s6: and upbraideth not ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And he does not scold. He does not shame you for not knowing, or hold your "
     "past against you, or make you feel small for coming late to ask. He simply "
     "gives. That is the kind of God this verse is describing."),
    # --- s7: kv6 — SACRED SILENCE 2 ---
    ("kv6", SCRIPTURE, "-26%", "-6Hz",
     "But let him ask in faith, nothing wavering."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "There is one thing asked of us in return, and it is not cleverness. It is "
     "faith. To ask believing that he truly hears, and then to hold steady, without "
     "letting doubt quietly pull the question back apart before the answer comes."),
    # --- s8: it shall be given / invitation ---
    ("n8", NARRATOR, "-24%", "-4Hz",
     "And the promise on the end of that verse is not a maybe. It shall be given "
     "him. Wisdom you could never argue your way into can be given, to anyone, for "
     "the honest asking. So here is the only question left. What have you been "
     "trying to work out all alone, that you could ask him about instead?"),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "You do not have to stay stuck. If you lack wisdom, ask of God. He gives to "
     "all, openly, and does not scold. Ask in faith, and it shall be given. What "
     "would you ask him?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
