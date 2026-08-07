#!/usr/bin/env python3
"""Narration for build-10-well — John 4.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

John 4 - the woman at the well. THIS VIDEO WAS ABOUT A WOMAN AND NEVER LET HER
SAY A WORD. She is one of the most talkative people in the gospels and every line of
hers was narrator paraphrase in white. Six are now lifted out verbatim as WOMAN, pink:
  w9   John 4:9   'How is it that thou, being a Jew, askest drink of me, which am a
       woman of Samaria?'  (the clause 'for the Jews have no dealings with the
       Samaritans' is John's own aside, not her speech, so it is left out)
  w11  John 4:11  'Sir, thou hast nothing to draw with, and the well is deep...'
  w15  John 4:15  'Sir, give me this water, that I thirst not, neither come hither to draw.'
  w19  John 4:19  'Sir, I perceive that thou art a prophet.'
  w25  John 4:25  'I know that Messias cometh, which is called Christ...'
  w29  John 4:29  'Come, see a man, which told me all things that ever I did...'
j1 and j2 are Jesus in the flesh and stay RED. w25 now sets up j2 - she says the
Messiah is coming, and the next voice answers 'I that speak unto thee am he.'
n8 was one audio across two different stills; it is split at the old caption
boundary into n8 and n8b. n10 is the closing card and keeps its id.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "A woman walked out to a well at noon — the hottest, emptiest hour of the day. You need to understand what that hour means. Women drew their water in the cool of the morning, together. It was where the talk happened. She came at noon because of the talk. Five marriages behind her, living now with a man who wasn't her husband — and the whole town knew every chapter. Noon was the hour with nobody in it. She chose it on purpose."),
    ("n1", NARRATOR, "But this day, somebody was there. A traveler sat by the well, worn out from the road — a Jewish man, resting in Samaria. That detail matters more than it sounds. Jews and Samaritans had despised each other for seven hundred years. They didn't share roads if they could help it, didn't share tables, and certainly didn't share water. Everything in her body said: turn around."),
    ("n2", NARRATOR, "Then he spoke to her. He asked her for a drink. Understand how impossible that sentence was. A rabbi did not speak to an unknown woman in public — and no Jew asked a Samaritan for anything. He broke both walls at once, and he did it by needing her help. She almost laughed. How is it that you, a Jew, would ask me for water? And he answered that if she knew who was asking, she would have asked him — and he would have given her living water."),
    # John 4:9
    ("w9", WOMAN, "How is it that thou, being a Jew, askest drink of me, which am a woman of Samaria?"),
    # John 4:11
    ("w11", WOMAN, "Sir, thou hast nothing to draw with, and the well is deep: from whence then hast thou that living water?"),
    ("n3", NARRATOR, "She pointed out the obvious — the well is deep, sir, and you don't even have a rope. This well came from Jacob himself. Are you greater than Jacob? She meant it as a corner. He stepped right into it."),
    # John 4:13-14
    ("j1", JESUS, "Whosoever drinketh of this water shall thirst again: But whosoever drinketh of the water that I shall give him shall never thirst; but the water that I shall give him shall be in him a well of water springing up into everlasting life."),
    ("n4", NARRATOR, "A well inside you — springing up, not running dry. He wasn't talking about the water in the jar. He was talking about the thirst underneath the thirst. The one you can't carry a jar big enough for."),
    # John 4:15
    ("w15", WOMAN, "Sir, give me this water, that I thirst not, neither come hither to draw."),
    ("n5", NARRATOR, "Then he said: go get your husband. And the whole conversation changed. I have no husband, she said. And he agreed with her — gently, and completely. Five husbands, he said. And the man you have now is not one. He already knew. All of it. Every chapter the town whispered about — he said it out loud, to her face. And he did not turn away. He stayed in the conversation. She came for water, and found herself fully known — and still spoken to with respect."),
    # John 4:19
    ("w19", WOMAN, "Sir, I perceive that thou art a prophet."),
    ("n6", NARRATOR, "She called him a prophet. She asked him her people's oldest question — which mountain is the right one to worship on — and he told her the day was coming when the question itself would be old news: God is spirit, and what he wants is the heart. Then she said, almost to herself: When he comes, he'll explain everything. And the tired traveler at the well said:"),
    # John 4:25
    ("w25", WOMAN, "I know that Messiah cometh, which is called Christ: when he is come, he will tell us all things."),
    # John 4:26
    ("j2", JESUS, "I that speak unto thee am he."),
    ("n7", NARRATOR, "The first person Jesus ever told plainly that he was the Messiah — not a king, not a priest, not even one of his twelve — a Samaritan woman with five marriages behind her, at the bottom of every list her world kept. Right then his followers came back from town, and stopped short — stunned that he was talking with her at all. Nobody dared say a word."),
    ("n8", NARRATOR, "And look what she did. She left the jar. The thing she walked all that way in the heat to fill — she left it standing at the well, and she ran."),
    ("n8b", NARRATOR, "Ran toward the town she had spent years avoiding, to the very people she came out at noon to miss, shouting:"),
    # John 4:29
    ("w29", WOMAN, "Come, see a man, which told me all things that ever I did: is not this the Christ?"),
    ("n9", NARRATOR, "And they came. The town that whispered about her followed her up the road to see for themselves. Many believed because of her word — the woman who wouldn't meet their eyes at sunrise became the first missionary in that gospel by sundown. They asked him to stay, and he stayed two days — with Samaritans. And they told her: now we've heard him ourselves. We know."),
    ("n10", NARRATOR, "She came for one thing, and found out she was thirsty for something much deeper. Have you ever been searching for something — and realized later it was deeper than what you thought you wanted?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
# CAPTION OVERRIDE (Cameron, 2026-07-21 night): he rejected "Messias" on screen as
# well as in the voice — "the caption is still wrong". John 4:25's KJV spelling is
# replaced with "Messiah" in the SEGMENT TEXT itself, so the caption and the audio
# both read Messiah. This is a deliberate, Cameron-ordered exception to the
# verbatim-KJV caption rule for this one word. No SPOKEN respelling is needed now.
SPOKEN = {}

# j2 "I that speak unto thee am he" (John 4:26) — the Messiah reveal, the single
# most important sentence in the story.
#
# 2026-07-21 (slur fix): the Eric voice slurred the three-word run "unto thee am
# he" into "the Amhi" (Cameron complaint #10). A/B/C/D tested on the actual
# voice — plain, comma, and "hee" all still transcribed "the Amhi"; only an
# ellipsis pause broke the liaison.
#
# 2026-08-07 (PACING re-voice, AUDIO-FIX): Cameron's OPEN complaint — "how fast
# and meaningless Jesus pronounced the words while telling her he was the
# messiah. It is a very important text and the speaker says it too fast." The one
# mid-line ellipsis fixed the slur but left the WHOLE line racing by (the shipped
# take was 1.67 s). Fix, ear-checked 2026-08-07 by faster-whisper on 4 candidates:
# rebuild the SPOKEN string with a leading pause and a pause before "am he" AND
# slow this one segment to -30% rate. Result: 4.92 s, deliberate, and whisper
# hears the exact words ("I, that speak unto thee, am he"). Caption stays verbatim
# KJV "I that speak unto thee am he"; only the SPOKEN/TTS string + this segment's
# rate carry the weight.
PHRASE_SPOKEN = {"j2": ("I that speak unto thee am he",
                        "I... that speak unto thee... am he")}
# Per-segment TTS rate overrides (slower than the speaker default for weight).
PHRASE_RATE = {"j2": "-30%"}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        st = spoken_text(text, SPOKEN, speaker)
        if name in PHRASE_SPOKEN:
            st = st.replace(*PHRASE_SPOKEN[name])
        await save_speaker_narration(st, speaker, f"audio/{name}.mp3",
                                     rate=PHRASE_RATE.get(name))
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
