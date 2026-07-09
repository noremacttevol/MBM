#!/usr/bin/env python3
"""Generate narration audio for Story Video #4 — Nicodemus at Night
(John 3:1-21; full arc through John 7:50-51 and John 19:39).
Narrator: modern, warm, low, unhurried (American). Plain US model only —
Multilingual models are banned (Cameron, 2026-07-08).
Jesus voice: AMERICAN, never British (Cameron's permanent law, 2026-07-07).
Jesus speaks ONLY exact KJV: John 3:3, John 3:8, John 3:16-17 (fetched from
bible-api.com, not hand-typed).
Script pre-flighted on paper per PRODUCTION-BIBLE.md — see PREFLIGHT.md.
FULL-STORY law: the pack stopped at John 3 with an invented ending; the
real arc (7:50-51 council defense, 19:39 hundred-pound burial) is the point.
Translation Law: no narrator line echoes KJV wording after Jesus speaks it.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 — who he was, and WHY he had everything to lose (s1 chamber).
    ("n0", NARRATOR, "-20%", "-4Hz",
     "In Jerusalem there was a man named Nicodemus. He was a Pharisee, "
     "and more than that — a ruler of the Jews, a member of the great "
     "council that governed the nation's faith. Educated. Respected. "
     "Listened to. A man like that had everything to lose by being seen "
     "with a controversial teacher from Galilee. His seat, his standing, "
     "his name."),
    # n1 — over the Veo street clip. The held beat.
    ("n1", NARRATOR, "-25%", "-5Hz",
     "So he came at night."),
    # n2 — the knock; the "we know" study gem (s3 threshold).
    ("n2", NARRATOR, "-20%", "-4Hz",
     "He knocked on the door in the dark, and the first thing he said "
     "was this: Teacher, we know you have come from God, because no one "
     "could do what you do unless God were with him. Bible students "
     "notice one small word there — we. Not I. We know. Nicodemus had "
     "been talking with other rulers, quietly, behind closed doors. "
     "Some of the very men who opposed Jesus in public already believed "
     "it in private. He just couldn't say it in daylight."),
    # n3a — set up J1.
    ("n3a", NARRATOR, "-22%", "-4Hz",
     "And Jesus didn't turn him away for coming at night. He didn't "
     "point out the fear. He skipped past the compliment entirely, and "
     "answered the real question underneath — the one Nicodemus hadn't "
     "dared to ask."),
    # J1 — exact KJV John 3:3b.
    ("j1", JESUS, "-25%", "-6Hz",
     "Verily, verily, I say unto thee, Except a man be born again, he "
     "cannot see the kingdom of God."),
    # n3b — bridge: origin of "born again", said to the most religious man.
    ("n3b", NARRATOR, "-22%", "-4Hz",
     "That's where the phrase comes from — this conversation, this "
     "night. And notice who heard it first. Not a hardened sinner. The "
     "most religious man in the country. Jesus was telling him that all "
     "his learning and all his rule-keeping could not do it. Everyone "
     "has to start over. Everyone."),
    # n4 — the womb question; Jesus doesn't mock him (s5).
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Nicodemus took it literally. How can a man be born when he is "
     "old, he asked — can he enter a second time into his mother's "
     "womb? Here was a master of the scriptures, completely lost. And "
     "Jesus didn't laugh at him. He didn't shame him for not getting "
     "it. He reached for something Nicodemus could feel — the night "
     "wind moving outside the window."),
    # J2 — exact KJV John 3:8.
    ("j2", JESUS, "-25%", "-6Hz",
     "The wind bloweth where it listeth, and thou hearest the sound "
     "thereof, but canst not tell whence it cometh, and whither it "
     "goeth: so is every one that is born of the Spirit."),
    # n5 — bridge: you can't see wind, only what it moves.
    ("n5", NARRATOR, "-22%", "-4Hz",
     "You can't see the wind. You only see what it moves — the trees "
     "bending, the flame leaning. That, Jesus said, is how God changes "
     "a person. You may not be able to explain it. But you can watch a "
     "life bend."),
    # n6 — "How can these things be?" (s7 face).
    ("n6", NARRATOR, "-22%", "-4Hz",
     "And something in Nicodemus gave way. How can these things be, he "
     "asked. Three words at a time, the formal questions of a scholar "
     "were falling away — until what was left was just a man, in the "
     "lamplight, finally asking what he actually wanted to know."),
    # n7a — set up the peak. Music is cutting to silence under this line.
    ("n7a", NARRATOR, "-25%", "-5Hz",
     "And then Jesus said the words. The ones the whole world would "
     "come to know."),
    # J3 — exact KJV John 3:16-17. THE PEAK. Full silence under it.
    ("j3", JESUS, "-25%", "-6Hz",
     "For God so loved the world, that he gave his only begotten Son, "
     "that whosoever believeth in him should not perish, but have "
     "everlasting life. For God sent not his Son into the world to "
     "condemn the world; but that the world through him might be "
     "saved."),
    # n7b — the pack's bridge line: not preached to a stadium.
    ("n7b", NARRATOR, "-25%", "-5Hz",
     "Those words weren't preached to a stadium. They were said "
     "quietly, at night, to one scared man who came with questions."),
    # n8 — light/darkness paraphrase (3:19-21): invitation, not a jab (s9).
    ("n8", NARRATOR, "-22%", "-4Hz",
     "Then Jesus spoke about light and darkness — how people hide in "
     "the dark when they're afraid of what the light will show, but "
     "whoever lives by the truth steps into the light gladly. Think "
     "about who he was saying that to. A man who had crept to his door "
     "under cover of darkness. It wasn't a jab. It was an invitation: "
     "you won't always have to come at night."),
    # n9 — John's tag: watch what happens to him (s9 hold).
    ("n9", NARRATOR, "-22%", "-4Hz",
     "Here's a detail worth keeping. Every time John's gospel mentions "
     "Nicodemus again, it adds the same tag — the one who came to "
     "Jesus by night. John wants you to remember how he started. "
     "Because he wants you to watch what happened to him."),
    # n10 — John 7:50-51: first daylight courage, and WHY it cost (s10).
    ("n10", NARRATOR, "-22%", "-4Hz",
     "Months later, the council met in broad daylight, furious, ready "
     "to condemn Jesus without a hearing. And one voice rose to stop "
     "them. Nicodemus. Does our law judge a man, he asked, before it "
     "hears him? It sounds mild. It wasn't. He was defending Jesus to "
     "the most powerful men in the nation — the very room he had "
     "everything to lose in. They turned on him for it. The man who "
     "once came at night was starting to speak in the light."),
    # n11 — John 19:39: the hundred-pound burial in the open (s11).
    ("n11", NARRATOR, "-25%", "-5Hz",
     "And then came the darkest day. Jesus was dead. His own apostles "
     "were hiding behind locked doors. And Nicodemus came — openly, in "
     "the daylight, when believing could no longer gain anyone "
     "anything — carrying a hundred pounds of myrrh and aloes for the "
     "burial. A hundred pounds. That was a quantity fit for royalty. "
     "The man who had crept to Jesus in the dark gave him a king's "
     "burial in the open."),
    # n12 — closing + card read aloud (Readable-Card Law).
    ("n12", NARRATOR, "-25%", "-5Hz",
     "Jesus never shamed the fear, and never shamed the night. He just "
     "answered the real question underneath — and let the courage grow "
     "on its own. Have you ever felt drawn toward something, and been "
     "afraid to let anyone else see it?"),
]

async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
