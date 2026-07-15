#!/usr/bin/env python3
"""Generate narration audio for Story Video #7 — Peter Walks on Water
(Matthew 14:22-33, the FULL story through verse 33).
Narrator: en-US-AndrewNeural — plain American, never Multilingual.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Matthew 14:27, 14:29a, 14:31b (fetched from
bible-api.com, not hand-typed).
Pre-flighted on paper per PRODUCTION-BIBLE §4b — see PREFLIGHT.md.
FULL-STORY law: the pack omitted v22-23 (Jesus praying alone — WHY he was
not in the boat), v26 ("It is a spirit"), and v32-33 (the wind ceasing +
the worship "Of a truth thou art the Son of God"). All restored.
Translation Law: no narrator line echoes KJV wording; modern meaning only.
Leighton's crew call (2026-07-09): the walking clip is the money moment;
"Come" lands alone in the dark with a long quiet breath after.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 — the sending + the mountain (s1). v22-23, the restored WHY.
    ("n0", NARRATOR, "-20%", "-4Hz",
     "Jesus had just fed more than five thousand people with a few "
     "loaves of bread and two small fish. And when it was done, he told "
     "his disciples to take the boat and cross the lake ahead of him. "
     "He sent the crowds home. And then he climbed a mountain, alone, "
     "to pray. That is where the night found him. Not in the boat. On "
     "the mountain, talking with his Father."),
    # n1 — the storm (s2). v24 + fourth-watch study gem.
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Out on the water, the wind turned against the boat. The waves "
     "rose. The disciples — several of them fishermen who had worked "
     "this lake their whole lives — rowed against it for hours. "
     "Matthew tells us it was the fourth watch of the night when help "
     "came. That means between three and six in the morning. They had "
     "been fighting that sea nearly all night."),
    # n2 — the figure on the water (s3). v25-26.
    ("n2", NARRATOR, "-22%", "-4Hz",
     "And then, through the spray and the dark, they saw something "
     "that made grown fishermen scream. A figure. Walking toward them. "
     "On top of the water. They cried out that it was a ghost — "
     "because nobody walks on the sea. But the voice that came back "
     "across the water was one they knew."),
    # J1 — exact KJV Matthew 14:27.
    ("j1", JESUS, "-25%", "-6Hz",
     "Be of good cheer; it is I; be not afraid."),
    # n3 — translation bridge + Peter's ask (s4). v28, Peter paraphrased modern.
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Take heart. It's me. Don't be afraid. And Peter — impulsive, "
     "big-hearted Peter — called back across the storm: Lord, if it's "
     "really you, tell me to come to you on the water. Think about "
     "what he was asking for. Not for the storm to stop. To come out "
     "into it — to where Jesus stood."),
    # J2 — exact KJV Matthew 14:29a. One word, alone in silence.
    ("j2", JESUS, "-28%", "-6Hz",
     "Come."),
    # n4 — he was doing it (s5 clip). v29b.
    ("n4", NARRATOR, "-22%", "-4Hz",
     "One word. And Peter put his leg over the side of that pitching "
     "boat, and stood up on the sea. And he was doing it. Step after "
     "step on the moving water, his eyes fixed on Jesus. For a moment, "
     "an ordinary fisherman walked where only God can walk."),
    # n5 — the turn + the sinking (s6, s7 clip). v30.
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Then he noticed the wind tearing at him. He looked down at the "
     "waves instead of ahead at Jesus. And the moment his eyes moved, "
     "the water stopped holding him. He dropped to his waist, "
     "mid-stride, and cried out the shortest prayer in the Bible: "
     "Lord, save me."),
    # n6 — the catch, PEAK setup (s8). v31a. Music dies on "immediately."
    ("n6", NARRATOR, "-24%", "-4Hz",
     "And Jesus caught him. Immediately."),
    # n7 — the gap that wasn't (s8, in the silence).
    ("n7", NARRATOR, "-24%", "-4Hz",
     "Matthew uses that exact word. There was no pause. No lesson "
     "first. No letting him go under to teach him something. The hand "
     "was there before the prayer was finished. And from that grip — "
     "holding him above the water — Jesus asked him one question."),
    # J3 — exact KJV Matthew 14:31b. THE PEAK, in dead silence.
    ("j3", JESUS, "-25%", "-6Hz",
     "O thou of little faith, wherefore didst thou doubt?"),
    # n8 — translation bridge (Translation Law: modern meaning, no KJV echo).
    ("n8", NARRATOR, "-24%", "-4Hz",
     "Why did you doubt? Hear how he asked it. Not from the shore. Not "
     "after pulling him into the boat. From the hand already holding "
     "him. It isn't a scolding. It's a real question, from someone who "
     "had already caught him — as if to say: you were doing it. What "
     "made you stop trusting me?"),
    # n9 — back to the boat, the wind ceases (s9, s10). v32.
    ("n9", NARRATOR, "-22%", "-4Hz",
     "The two of them came back to the boat across the water together. "
     "And the moment they climbed in, the wind stopped. Not slowly. "
     "Not eventually. The sea that had fought them all night simply "
     "lay down flat under the stars."),
    # n10 — the worship (s11, s12). v33, paraphrased modern.
    ("n10", NARRATOR, "-22%", "-4Hz",
     "And the men in that boat — the same men who minutes earlier had "
     "screamed that he was a ghost — knelt down where they sat, soaked "
     "and shaking, and worshipped him. You really are the Son of God, "
     "they said. The storm had taught them who he was. And notice what "
     "the story remembers about Peter. Not that he sank. That he "
     "walked. And that when he fell, he was caught."),
    # n11 — the closing card, read aloud gently (INVITATION, closing-card law).
    ("n11", NARRATOR, "-26%", "-4Hz",
     "When your storm gets loud and your faith slips, look back up — "
     "the same hand is already reaching for you. Keep your eyes on "
     "him."),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
