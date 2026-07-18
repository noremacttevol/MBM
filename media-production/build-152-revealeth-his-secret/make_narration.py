#!/usr/bin/env python3
"""Generate narration audio for Story Video #152 — "Surely the Lord GOD will do
nothing, but he revealeth his secret unto his servants the prophets" (Amos 3:7-8).
MEMBER shelf verse-video. → Gospel Library topic: Prophets.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — speaks the KJV text EXACTLY.
(Amos is Old-Testament prophecy; the scripture voice carries the verse itself.
Christ is NOT depicted anywhere in this video; God is shown only as light.)

KJV lines (exact):
  kv7 = Amos 3:7  the Lord GOD revealeth his secret unto the prophets (NAMED VERSE — SACRED SILENCE 1)
  kv8 = Amos 3:8  the lion hath roared... the Lord GOD hath spoken (SACRED SILENCE 2)

WHY-LAW: reassurance, not fear — God is not silent or arbitrary; before he acts he
WARNS, opening his plans to prophets so his people are never caught in the dark.
STUDY GEMS: he calls ordinary working people to carry his word (n1); he tells someone
BEFORE he acts (n3); a warned people can still turn and get ready (n6); once God has
spoken, the prophet cannot stay silent (n7).

TRANSLATION LAW: the narrator never re-quotes a KJV line. n3 says "before he acts, he
tells someone," never "he revealeth his secret"; n7 says "he cannot stay silent,"
never "who can but prophesy."

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Prophets). No shame, no fear.
CHRIST IS NEVER DEPICTED; God is shown only as light, never a figure or face.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts
from mbm_caption_timing import save_narration

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The man God chose to speak through was not a king or a priest. He was a "
     "herdsman, out with his flock on the hills, a plain working man. God has always "
     "loved to call ordinary people to carry extraordinary words."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "And one day the word of the Lord came to him. Not his own idea, not a clever "
     "guess about what was coming, but a message given to him from God, as real and "
     "clear as a voice carried on the wind."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Here is something steadying about the way God works. Before he acts, he tells "
     "someone. He does not move against his people in the dark, with no warning. He "
     "opens his plans to a servant he can trust to pass them on."),
    # kv7 — NAMED VERSE, SACRED SILENCE 1
    ("kv7", SCRIPTURE, "-26%", "-6Hz",
     "Surely the Lord GOD will do nothing, but he revealeth his secret unto his "
     "servants the prophets."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Think about what that means. The God who holds everything together chooses to "
     "let people in on what he is about to do. He trusts his real plan to a prophet, "
     "the way a father warns his household before the storm arrives."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "So the prophet does not keep it to himself. He goes down to where the people "
     "are, to the gate and the market, and he says out loud the very thing God told "
     "him, whether the crowd wants to hear it or not."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And this is a mercy, not a threat. A people who are warned can still turn. They "
     "can get ready, mend what is broken, and come home in time. No one who listened "
     "was ever caught by surprise."),
    # kv8 — SACRED SILENCE 2
    ("kv8", SCRIPTURE, "-26%", "-6Hz",
     "The lion hath roared, who will not fear? the Lord GOD hath spoken, who can but "
     "prophesy?"),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "When God has truly spoken, the prophet cannot stay silent, any more than you "
     "could ignore a lion roaring close beside you. The message is not his to soften "
     "or hold back. He simply has to say it."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "And that is the quiet comfort in this verse. God still does not leave his people "
     "guessing. He still opens his plans to living prophets, so that anyone willing to "
     "listen can hear where he is going before he gets there. So the only question is "
     "a gentle one. Are you listening for it?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "God does nothing without first telling his servants the prophets. He warns "
     "before he acts, because he wants his people ready, not surprised. He still "
     "speaks this way. Are you listening?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        await save_narration(text, voice, rate, pitch, f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
