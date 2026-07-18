#!/usr/bin/env python3
"""Generate narration audio for Video #55 — The Withered Hand (Mark 3:1-6).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. Two lines — his whole speech in this passage:
  jv4 = Mark 3:4  "Is it lawful to do good on the sabbath days, or to do evil?
                   to save life, or to kill?"   (SACRED SILENCE 1 — the question)
  jv5 = Mark 3:5  "Stretch forth thine hand."   (SACRED SILENCE 2 — the healing)

TRANSLATION LAW: after each KJV line the narrator gives plain meaning and never re-quotes
it. The leaders' hostility is reported plainly; captioned in the narrator's plain white.

HOMOGRAPH LAW: no TTS homographs in this text (no live-adjective/bow/wound/read/tear/wind/
lead/sow). SPOKEN is empty.

CARE — ARC: the shadow of the cross begins here. Jesus's anger and grief at hard hearts is
real but righteous; the leaders' plot to destroy him is reported, shown only as men leaving
to conspire — no violence, no menace on screen. The heart is mercy over rule; the hope-beat
is the restored hand.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

SPOKEN = {}

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the man with the withered hand ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "On another sabbath Jesus went into the synagogue to teach, and there in the crowd "
     "was a man whose hand was withered, shrunken and useless, a hand that could not "
     "work or grip or hold. He had carried it, and the shame of it, for years."),
    # --- s2: they watched him ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "But others in the room were watching — not the man, but Jesus. Some of the "
     "religious leaders felt sure he would try to heal on the sabbath, and they waited, "
     "hoping to catch him breaking the law, so they could accuse him."),
    # --- s3: stand forth ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Jesus knew exactly what was in their hearts. He did not hide the moment away in a "
     "corner. He said to the man with the withered hand, stand up, and come out here "
     "into the midst, where everyone can see."),
    # --- s4: jv4 — is it lawful. SACRED SILENCE 1. ---
    ("jv4", JESUS, "-26%", "-6Hz",
     "Is it lawful to do good on the sabbath days, or to do evil? to save life, or to "
     "kill?"),
    # --- s5: hardness of heart ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "It was a simple question, and it left them no answer. They had no real love for "
     "the law, or for the man; they only wanted a reason to condemn him. So they said "
     "nothing at all. And Jesus looked around at them, angry and deeply grieved at how "
     "hard their hearts had grown."),
    # --- s6: jv5 — stretch forth thine hand. SACRED SILENCE 2. ---
    ("jv5", JESUS, "-26%", "-6Hz",
     "Stretch forth thine hand."),
    # --- s7: restored whole ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "And the man stretched out the hand he could not use — and as he reached, it was "
     "made whole, restored, strong and alive again, exactly like his other hand. The "
     "thing that had been dead came back to life at a single word."),
    # --- s8: they plotted ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "But the leaders were not amazed; they were furious. They walked out and began, that "
     "very day, to plot together how they might destroy him. He had done nothing but "
     "good, and it only hardened them."),
    # --- s9: mercy over the rule ---
    ("n7", NARRATOR, "-24%", "-4Hz",
     "Faced with a rule on one side and a suffering man on the other, Jesus never wavered. "
     "He will always move toward the person. Mercy, to him, was never a breaking of the "
     "sabbath; it was the whole reason for it."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "There will always be people upset that he loves you without conditions. Let them "
     "be. He looks past every rule that was ever used to shut you out, and he calls you "
     "to stand up, out in the open, and be made whole. Will you stretch out the very "
     "thing you thought was beyond help?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        await save_narration(spoken, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
