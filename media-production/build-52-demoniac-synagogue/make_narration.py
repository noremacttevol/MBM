#!/usr/bin/env python3
"""Generate narration audio for Video #52 — The Demoniac in the Synagogue (Mark 1:21-28).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.

Jesus speaks ONLY exact KJV. He has ONE line in this passage — his whole speech here:
  jv25 = Mark 1:25  "Hold thy peace, and come out of him."  (SACRED SILENCE — the command)

TRANSLATION LAW: after the KJV line the narrator gives plain meaning and never re-quotes
it. The unclean spirit's cry (Mark 1:24) is NOT red-letter KJV — the narrator reports it
plainly; it is captioned in the narrator's plain white style, never the cream scripture
style reserved for Jesus.

HOMOGRAPH LAW: avoided "read" (past tense /red/ vs /reed/) by writing "taught and
explained". Avoided the archaic "tare" (Mark 1:26) by reporting it as "convulsed" /
"shook". No other TTS homographs in the text; SPOKEN is empty.

CARE — R (RESTRAINT): a real deliverance shown gently. No visible demon or monster, no
gore, no horror; the torment is the man's own anguish, and the miracle is that at Christ's
word he is simply set free. The hope-beat is the freed man, whole and in his right mind.

MILK FRAMING: authority and mercy. The one whose word even the darkness must obey turns
that authority to set a suffering man free. Ends on an open invitation, never fear.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
JESUS = "en-US-ChristopherNeural"

# TTS-only respellings (captions still show the true text in build.py). None needed here.
SPOKEN = {}

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- s1: the sabbath synagogue ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "On the sabbath day, Jesus went into the synagogue at Capernaum and stood up to "
     "teach. The people had gathered as they always did, to hear the scriptures taught "
     "and explained by the teachers they knew."),
    # --- s2: taught as one with authority ---
    ("n2", NARRATOR, "-22%", "-4Hz",
     "But this was different. He taught them as one who had authority of his own, not "
     "leaning on teacher after teacher the way the scribes did. His words carried a "
     "quiet weight, and the whole room felt it, and was astonished."),
    # --- s3: the tormented man ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "There in the congregation was a man held by an unclean spirit. Something dark had "
     "bound him for a long time, and the nearness of Jesus stirred it. Unable to stay "
     "silent any longer, he suddenly cried out."),
    # --- s4: the cry (Mark 1:24, narrator-reported, NOT cream KJV) ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "The voice that broke from him was not his own. Let us alone, it said; what have we "
     "to do with thee, Jesus of Nazareth? Art thou come to destroy us? And then, almost "
     "trembling: I know who thou art, the Holy One of God."),
    # --- s5: jv25 — Hold thy peace, and come out of him. SACRED SILENCE. ---
    ("jv25", JESUS, "-26%", "-6Hz",
     "Hold thy peace, and come out of him."),
    # --- s6: the spirit comes out ---
    ("n5", NARRATOR, "-22%", "-4Hz",
     "There was no long battle, no struggle of equals. At his word the spirit shook the "
     "man one last time, cried out with a loud voice, and came out of him. The thing "
     "that had held him for so long simply had to go."),
    # --- s7: the man in his right mind ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And the man was free. The torment had drained from his face, and he stood there "
     "quiet and whole, himself again, like someone waking gently from a long and "
     "terrible dream."),
    # --- s8: the people amazed ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "The people were amazed, and they asked one another, what is this? A new teaching, "
     "and with such authority that he commands even the unclean spirits, and they obey "
     "him."),
    # --- s9: his fame spreads through Galilee ---
    ("n8", NARRATOR, "-24%", "-4Hz",
     "And right away the news of him went out everywhere, through all the country round "
     "about Galilee. Wherever the story was carried, people heard that one had come "
     "whose word even the darkness could not resist."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "The same voice that spoke into that man's torment still speaks today. There is no "
     "darkness in you so deep that his word cannot reach it, and nothing holding you "
     "that has to stay when he says come out. What is he asking you to let him set free?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        spoken = SPOKEN.get(name, text)
        await save_narration(spoken, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
