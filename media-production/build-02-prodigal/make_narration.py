#!/usr/bin/env python3
"""Generate narration audio for Story Video #2 — The Prodigal Son (Luke 15:11-32).
Narrator: modern, warm, low, unhurried (American). Plain US model only —
Multilingual models are banned (Cameron, 2026-07-08).
Jesus voice: AMERICAN, never British (Cameron's permanent law, 2026-07-07).
Jesus speaks ONLY exact KJV: Luke 15:24 (first sentence, per the pack).
Script pre-flighted on paper per PRODUCTION-BIBLE.md section 4b — see PREFLIGHT.md.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # Opening bookend — why Jesus told this story (pattern approved on #8/#6)
    ("n0", NARRATOR, "-22%", "-4Hz",
     "When religious men complained that Jesus spent his time with sinners, "
     "he didn't argue with them. He answered with a story, about a father "
     "and his two sons."),
    ("n1", NARRATOR, "-20%", "-4Hz",
     "The younger son asked for his inheritance early — as if to say he "
     "wished his father were already dead. Then he left, and poured it all "
     "out on a life that emptied him."),
    ("n2", NARRATOR, "-20%", "-4Hz",
     "When the money was gone, a famine came. He ended up feeding pigs, "
     "so hungry he would have eaten what they ate. And there, in the mud, "
     "he came to his senses."),
    ("n3", NARRATOR, "-20%", "-4Hz",
     "So he started walking home, rehearsing a speech the whole way. "
     "Father, I am not worthy to be called your son. "
     "Make me one of your servants."),
    ("n4", NARRATOR, "-25%", "-5Hz",
     "He was still a long way off... when his father saw him."),
    # PEAK — music has already cut to full silence before this line
    ("n5a", NARRATOR, "-25%", "-5Hz",
     "The father ran."),
    ("n5b", NARRATOR, "-22%", "-4Hz",
     "Old men in that world did not run. It was beneath their dignity. "
     "He ran anyway."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "He didn't wait for the speech. He wrapped his arms around his son "
     "before a single word was said."),
    # REWRITTEN 2026-07-09: the story does NOT end at the feast (Cameron's
    # catch — the older brother is the other half). Old line said "Jesus
    # ended the story with the father's own words" — false, removed.
    ("n7", NARRATOR, "-22%", "-4Hz",
     "That night the father dressed him in the finest robe, put a ring on "
     "his hand, and called for a feast — and he told everyone why."),
    # Exact KJV Luke 15:24 (fetched, not hand-typed).
    # Translation Law: the narrator never re-quotes or echoes this line.
    ("j1", JESUS, "-25%", "-6Hz",
     "For this my son was dead, and is alive again; "
     "he was lost, and is found."),
    # ---- SECOND HALF: the older brother (Luke 15:25-32), added 2026-07-09 ----
    ("n9", NARRATOR, "-22%", "-4Hz",
     "But Jesus wasn't finished. The older son was still out in the field, "
     "like always. When he came near the house and heard the music, a "
     "servant told him: your brother is home. And he was so angry, he "
     "refused to go in."),
    ("n10a", NARRATOR, "-25%", "-5Hz",
     "So the father left his own feast, and went out again — this time to "
     "the son who had never left."),
    ("n10b", NARRATOR, "-22%", "-4Hz",
     "The older son's hurt poured out. All these years I have served you. "
     "I never disobeyed you. And you never gave me even a young goat, to "
     "celebrate with my friends."),
    ("n11", NARRATOR, "-25%", "-5Hz",
     "The father didn't argue with him, either. Jesus gave him the last "
     "words of the story."),
    # Exact KJV Luke 15:31-32 (fetched, not hand-typed) — the TRUE last
    # story words. Translation Law: nothing after these re-quotes them.
    ("j2a", JESUS, "-25%", "-6Hz",
     "Son, thou art ever with me, and all that I have is thine."),
    ("j2b", JESUS, "-25%", "-6Hz",
     "It was meet that we should make merry, and be glad: for this thy "
     "brother was dead, and is alive again; and was lost, and is found."),
    # Closing card read aloud, gently (Readable-Card Law) — REWRITTEN to the
    # three-character question now that the whole story is told.
    ("n8", NARRATOR, "-25%", "-5Hz",
     "Which one feels closest to where you are right now — the son who "
     "left, the father who ran to meet him, or the brother who stayed, "
     "and felt unseen?"),
]

async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
