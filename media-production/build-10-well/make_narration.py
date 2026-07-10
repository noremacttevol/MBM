#!/usr/bin/env python3
"""Generate narration audio for Story Video #10 — The Woman at the Well
(John 4:4-30, 39-42).
Narrator: en-US-AndrewNeural — plain American, never Multilingual.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: John 4:13-14 and John 4:26 (fetched from
bible-api.com — see qc/john4-kjv.txt — never hand-typed).
Pre-flighted on paper per PRODUCTION-BIBLE §4b — see PREFLIGHT.md.
vv20-24 (worship in spirit and truth) consciously summarized in one
narrator line per PREFLIGHT; vv39-42 carried by the closing narration.
Translation Law: no narrator line echoes KJV wording; modern meaning only.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 — noon, alone on purpose (s1). v6-v7a + the WHY-gem about the hour.
    ("n0", NARRATOR, "-20%", "-4Hz",
     "A woman walked out to a well at noon — the hottest, emptiest hour "
     "of the day. You need to understand what that hour means. Women "
     "drew their water in the cool of the morning, together. It was "
     "where the talk happened. She came at noon because of the talk. "
     "Five marriages behind her, living now with a man who wasn't her "
     "husband — and the whole town knew every chapter. Noon was the "
     "hour with nobody in it. She chose it on purpose."),
    # n1 — the traveler (s2). v6, v9 background: seven hundred years of contempt.
    ("n1", NARRATOR, "-20%", "-4Hz",
     "But this day, somebody was there. A traveler sat by the well, worn "
     "out from the road — a Jewish man, resting in Samaria. That detail "
     "matters more than it sounds. Jews and Samaritans had despised each "
     "other for seven hundred years. They didn't share roads if they "
     "could help it, didn't share tables, and certainly didn't share "
     "water. Everything in her body said: turn around."),
    # n2 — he asked HER (s3). v7. The double wall broken in one sentence.
    ("n2", NARRATOR, "-22%", "-4Hz",
     "Then he spoke to her. He asked her for a drink. Understand how "
     "impossible that sentence was. A rabbi did not speak to an unknown "
     "woman in public — and no Jew asked a Samaritan for anything. He "
     "broke both walls at once, and he did it by needing her help. She "
     "almost laughed. How is it that you, a Jew, would ask me for "
     "water? And he answered that if she knew who was asking, she "
     "would have asked him — and he would have given her living water."),
    # n3 — setup for the KJV line (s4). Music thins to silence under this.
    ("n3", NARRATOR, "-24%", "-4Hz",
     "She pointed out the obvious — the well is deep, sir, and you "
     "don't even have a rope. This well came from Jacob himself. Are "
     "you greater than Jacob? She meant it as a corner. He stepped "
     "right into it."),
    # J1 — exact KJV John 4:13-14. Slow, warm, in full silence.
    ("j1", JESUS, "-27%", "-6Hz",
     "Whosoever drinketh of this water shall thirst again: But "
     "whosoever drinketh of the water that I shall give him shall "
     "never thirst; but the water that I shall give him shall be in "
     "him a well of water springing up into everlasting life."),
    # n4 — translation bridge (s4 out). Translation Law: modern meaning only.
    ("n4", NARRATOR, "-24%", "-4Hz",
     "A well inside you — springing up, not running dry. He wasn't "
     "talking about the water in the jar. He was talking about the "
     "thirst underneath the thirst. The one you can't carry a jar big "
     "enough for."),
    # n5 — her whole life, and he stayed (s5 clip — THE PEAK).
    # Music cuts to silence at "he did not turn away."
    ("n5", NARRATOR, "-22%", "-4Hz",
     "Then he said: go get your husband. And the whole conversation "
     "changed. I have no husband, she said. And he agreed with her — "
     "gently, and completely. Five husbands, he said. And the man you "
     "have now is not one. He already knew. All of it. Every chapter "
     "the town whispered about — he said it out loud, to her face. And "
     "he did not turn away. He stayed in the conversation. She came "
     "for water, and found herself fully known — and still spoken to "
     "with respect."),
    # n6 — worship summary + Messiah setup (s5 tail). vv19-25 in one modern line.
    ("n6", NARRATOR, "-24%", "-4Hz",
     "She called him a prophet. She asked him her people's oldest "
     "question — which mountain is the right one to worship on — and "
     "he told her the day was coming when the question itself would be "
     "old news: God is spirit, and what he wants is the heart. Then "
     "she said, almost to herself: I know the Messiah is coming. When "
     "he comes, he'll explain everything. And the tired traveler at "
     "the well said:"),
    # J2 — exact KJV John 4:26. The first plain "I am he" in the gospel.
    ("j2", JESUS, "-27%", "-6Hz",
     "I that speak unto thee am he."),
    # n7 — the gem: who he told first (s6 — disciples return, marveling).
    ("n7", NARRATOR, "-24%", "-4Hz",
     "The first person Jesus ever told plainly that he was the "
     "Messiah — not a king, not a priest, not even one of his twelve — "
     "a Samaritan woman with five marriages behind her, at the bottom "
     "of every list her world kept. Right then his followers came back "
     "from town, and stopped short — stunned that he was talking with "
     "her at all. Nobody dared say a word."),
    # n8 — the jar left behind (s7 clip). v28-29.
    ("n8", NARRATOR, "-22%", "-4Hz",
     "And look what she did. She left the jar. The thing she walked "
     "all that way in the heat to fill — she left it standing at the "
     "well, and she ran. Ran toward the town she had spent years "
     "avoiding, to the very people she came out at noon to miss, "
     "shouting: come see a man who told me everything I ever did."),
    # n9 — the harvest (s8 → s9). vv30, 39-42 in modern words.
    ("n9", NARRATOR, "-24%", "-4Hz",
     "And they came. The town that whispered about her followed her "
     "up the road to see for themselves. Many believed because of her "
     "word — the woman who wouldn't meet their eyes at sunrise became "
     "the first missionary in that gospel by sundown. They asked him "
     "to stay, and he stayed two days — with Samaritans. And they told "
     "her: now we've heard him ourselves. We know."),
    # n10 — the closing card, read aloud gently (Readable-Card Law).
    ("n10", NARRATOR, "-26%", "-4Hz",
     "She came for one thing, and found out she was thirsty for "
     "something much deeper. Have you ever been searching for "
     "something — and realized later it was deeper than what you "
     "thought you wanted?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
