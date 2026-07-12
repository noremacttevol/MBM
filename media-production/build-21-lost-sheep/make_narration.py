#!/usr/bin/env python3
"""Generate narration audio for Story Video #21 — The Lost Sheep
(Luke 15:1-7).

Narrator: en-US-AndrewNeural — plain American, never a Multilingual model.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: Luke 15:4 (j1), Luke 15:6 (j2), Luke 15:7 (j3).

CAPTIONS ARE VERBATIM (Cameron, 2026-07-11): build.py imports these SEGMENTS
and word-wraps each text as the on-screen caption, so every spoken word is on
the screen. After each KJV Jesus line the narrator gives ONLY the plain modern
meaning and never re-quotes the KJV words (Translation Law).

A parable told BY Jesus: he is the narrating voice and appears only in the
bookend shots as a seated storyteller seen from behind (STILLS-ONLY, Law E;
Jesus face-never). The shepherd IS a character in the parable, shown fully.

WHY-LAW: the script opens on why the religious men were offended (Jesus welcomed
and ate with the very people they had written off) and makes the point sayable
in one sentence — not one person is expendable to him. STUDY-GEMS woven small:
"an hundred sheep" was a modest one-shepherd flock; leaving the ninety-nine
means leaving them safe (bedded in a fold / under a hired hand) to go after the
one; "until he find it" means the search does not stop while the sheep is lost.
NUMBER-STRESS: no sentence opens on a bare number (Andrew under-stresses a
sentence-initial "one"/"two" into "to"); numbers are spelled out and buried
mid-sentence.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text) — text is BOTH spoken and captioned.
    # --- Shot 1: the murmur (Luke 15:1-2) ---
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The tax collectors and the outcasts were crowding in close to hear Jesus. "
     "And the religious men could not stand it."),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "They muttered that this man welcomes sinners and even sits down to eat "
     "with them. To them, that was the whole problem. So Jesus told them a "
     "story."),
    # --- Shot 2: the hundred sheep, the parable's core (KJV j1 = Luke 15:4) ---
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Picture a shepherd, he said, out on the hills with a flock of a hundred "
     "sheep."),
    ("j1", JESUS, "-26%", "-6Hz",
     "What man of you, having an hundred sheep, if he lose one of them, doth not "
     "leave the ninety and nine in the wilderness, and go after that which is "
     "lost, until he find it?"),
    # --- Shot 3: one is missing (translation of j1 + the count) ---
    ("n4", NARRATOR, "-22%", "-4Hz",
     "In other words, not one of them is written off. Lose a single sheep, and "
     "you go after it. So the shepherd counts the flock at dusk, and comes up "
     "one short."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "He could tell himself the math is fine. Ninety-nine out of a hundred is a "
     "good day. But that is not how he sees it. One of his own is out there "
     "alone in the dark, and that is one too many."),
    # --- Shot 4: he leaves the ninety-nine and goes ---
    ("n6", NARRATOR, "-22%", "-4Hz",
     "So he leaves the ninety-nine bedded down safe together, and he walks out "
     "into the wilderness after the one. Not a search party. Not a hired hand. "
     "Him, himself, into the cold and the rocks."),
    # --- Shot 5: until he find it ---
    ("n7", NARRATOR, "-22%", "-4Hz",
     "And notice how long he looks. Not until he gets tired. Not until it gets "
     "too dark. He goes, the story says, until he finds it. The searching does "
     "not stop while the sheep is still lost."),
    # --- Shot 6: found (the peak, lands in silence) ---
    ("n8", NARRATOR, "-25%", "-5Hz",
     "And he finds it. Tangled in the thorns, worn out, unable to get itself "
     "home."),
    # --- Shot 7: layeth it on his shoulders, rejoicing ---
    ("n9", NARRATOR, "-22%", "-4Hz",
     "He does not scold it. He does not drive it ahead of him. He lifts the "
     "frightened animal onto his own shoulders and carries its whole weight the "
     "long way home. And the story says he does it rejoicing."),
    # --- Shot 8: rejoice with me (KJV j2 = Luke 15:6) ---
    ("n10", NARRATOR, "-22%", "-4Hz",
     "When he gets home he cannot keep it in. He calls his friends and his "
     "neighbors together and tells them,"),
    ("j2", JESUS, "-25%", "-6Hz",
     "Rejoice with me; for I have found my sheep which was lost."),
    ("n11", NARRATOR, "-22%", "-4Hz",
     "He throws a celebration over one recovered sheep. The lost one coming home "
     "is not an embarrassment to hide. It is the best news he has had all week."),
    # --- Shot 9: joy in heaven (KJV j3 = Luke 15:7), the turn on the murmurers ---
    ("n12", NARRATOR, "-22%", "-4Hz",
     "Then Jesus looked back at the men who could not stand who he ate with, and "
     "told them what the whole story was really about."),
    ("j3", JESUS, "-26%", "-6Hz",
     "I say unto you, that likewise joy shall be in heaven over one sinner that "
     "repenteth, more than over ninety and nine just persons, which need no "
     "repentance."),
    ("n13", NARRATOR, "-23%", "-4Hz",
     "Heaven throws that same party, he said, over one person turning back to "
     "God. The people they despised were never a nuisance to him. Each one was "
     "the sheep he would leave everything to go and carry home."),
    ("n14", NARRATOR, "-24%", "-4Hz",
     "That is how good he is. You are never the ninety-nine he can afford to "
     "lose. If you are the one, he is already out looking."),
    # --- closing card, read gently (Readable-Card Law) ---
    ("card", NARRATOR, "-26%", "-4Hz",
     "You are never a number he can afford to lose. If you are the one he's "
     "missing, will you let him carry you home?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
