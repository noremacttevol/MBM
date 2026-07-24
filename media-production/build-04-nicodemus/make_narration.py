#!/usr/bin/env python3
"""Narration for build-04-nicodemus — John 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

STAYED RED: all three existing red beats are Jesus speaking in the flesh, and a
red-letter KJV prints all three.
  j1  John 3:3      'Verily, verily, I say unto thee, Except a man be born again...'
  j2  John 3:8      'The wind bloweth where it listeth...'
  j3  John 3:16-17  'For God so loved the world...'
None of the three has John's narration welded onto it, so none needed splitting.

LIFTED FROM PARAPHRASE - Nicodemus's own four lines, all SCRIPTURE (blue). This
is the point of the build: it is a conversation, and only one man in it was ever
allowed to talk.
  s2   John 3:2  'Rabbi, we know that thou art a teacher come from God: for no
                  man can do these miracles that thou doest, except God be with him.'
  s4   John 3:4  'How can a man be born when he is old? can he enter the second
                  time into his mother's womb, and be born?'
  s9   John 3:9  'How can these things be?'
  s51  John 7:51 'Doth our law judge any man, before it hear him, and know what he
                  doeth?' - the council scene months later. Blue, and it is the
                  same man's voice in daylight, which is the whole arc of the video.

EDITS TO EXISTING NARRATOR TEXT: four narrator beats were trimmed at the point
where they used to speak his lines for him, and the remainder became a new
retelling beat on the SAME still - n2 -> s2 -> n2b, n4 -> s4 -> n4b,
n6 -> s9 -> n6b, n10 -> s51 -> n10b. Every retelling reuses the old wording, so
the storyteller's voice is unchanged and no still moved.

NOT LIFTED: n8 describes John 3:19-21 (light and darkness) in modern English
rather than quoting it. That is the storyteller doing his job and it stays
narrator. n11's hundred pounds of myrrh and aloes is John 19:39 narrated, not
quoted - also correctly narrator.

WOMEN: John 3 records no woman speaking. Nothing added; nothing invented.

WHY-LAW: Jesus never shamed the fear and never shamed the night. He answered the
real question underneath and let the courage grow on its own - from a man at the
door in the dark to a man carrying a king's burial in the open.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "In Jerusalem there was a man named Nicodemus. He was a Pharisee, and more than that — a ruler of the Jews, a member of the great council that governed the nation's faith. Educated. Respected. Listened to. A man like that had everything to lose by being seen with a controversial teacher from Galilee. His seat, his standing, his name."),
    ("n1", NARRATOR, "So he came at night."),
    ("n2", NARRATOR, "He knocked on the door in the dark, and the first thing he said was this."),
    # John 3:2
    ("s2", SCRIPTURE, "Rabbi, we know that thou art a teacher come from God: for no man can do these miracles that thou doest, except God be with him."),
    ("n2b", NARRATOR, "Teacher, we know you have come from God, because no one could do what you do unless God were with him. Bible students notice one small word there — we. Not I. We know. Nicodemus had been talking with other rulers, quietly, behind closed doors. Some of the very men who opposed Jesus in public already believed it in private. He just couldn't say it in daylight."),
    ("n3a", NARRATOR, "And Jesus didn't turn him away for coming at night. He didn't point out the fear. He skipped past the compliment entirely, and answered the real question underneath — the one Nicodemus hadn't dared to ask."),
    # John 3:3
    ("j1", JESUS, "Verily, verily, I say unto thee, Except a man be born again, he cannot see the kingdom of God."),
    ("n3b", NARRATOR, "That's where the phrase comes from — this conversation, this night. And notice who heard it first. Not a hardened sinner. The most religious man in the country. Jesus was telling him that all his learning and all his rule-keeping could not do it. Everyone has to start over. Everyone."),
    ("n4", NARRATOR, "Nicodemus took it literally."),
    # John 3:4
    ("s4", SCRIPTURE, "How can a man be born when he is old? can he enter the second time into his mother's womb, and be born?"),
    ("n4b", NARRATOR, "Here was a master of the scriptures, completely lost. And Jesus didn't laugh at him. He didn't shame him for not getting it. He reached for something Nicodemus could feel — the night wind moving outside the window."),
    # John 3:8
    ("j2", JESUS, "The wind bloweth where it listeth, and thou hearest the sound thereof, but canst not tell whence it cometh, and whither it goeth: so is every one that is born of the Spirit."),
    ("n5", NARRATOR, "You can't see the wind. You only see what it moves — the trees bending, the flame leaning. That, Jesus said, is how God changes a person. You may not be able to explain it. But you can watch a life bend."),
    ("n6", NARRATOR, "And something in Nicodemus gave way. Three words at a time, the formal questions of a scholar were falling away — until what was left was just a man in the lamplight, asking the only thing he had really come to ask."),
    # John 3:9
    ("s9", SCRIPTURE, "How can these things be?"),
    ("n6b", NARRATOR, "No title on it. No argument behind it. Just a tired, honest man finally asking what he actually wanted to know."),
    ("n7a", NARRATOR, "And then Jesus said the words. The ones the whole world would come to know."),
    # John 3:16-17
    ("j3", JESUS, "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life. For God sent not his Son into the world to condemn the world; but that the world through him might be saved."),
    ("n7b", NARRATOR, "Those words weren't preached to a stadium. They were said quietly, at night, to one scared man who came with questions."),
    ("n8", NARRATOR, "Then Jesus spoke about light and darkness — how people hide in the dark when they're afraid of what the light will show, but whoever lives by the truth steps into the light gladly. Think about who he was saying that to. A man who had crept to his door under cover of darkness. It wasn't a jab. It was an invitation: you won't always have to come at night."),
    ("n9", NARRATOR, "Here's a detail worth keeping. Every time John's gospel mentions Nicodemus again, it adds the same tag — the one who came to Jesus by night. John wants you to remember how he started. Because he wants you to watch what happened to him."),
    ("n10", NARRATOR, "Months later, the council met in broad daylight, furious, ready to condemn Jesus without a hearing. And one voice rose to stop them. Nicodemus."),
    # John 7:51
    ("s51", SCRIPTURE, "Doth our law judge any man, before it hear him, and know what he doeth?"),
    ("n10b", NARRATOR, "Does our law judge a man, he asked, before it hears him? It sounds mild. It wasn't. He was defending Jesus to the most powerful men in the nation — the very room he had everything to lose in. They turned on him for it. The man who once came at night was starting to speak in the light."),
    ("n11", NARRATOR, "And then came the darkest day. Jesus was dead. His own apostles were hiding behind locked doors. And Nicodemus came — openly, in the daylight, when believing could no longer gain anyone anything — carrying a hundred pounds of myrrh and aloes for the burial. A hundred pounds. That was a quantity fit for royalty. The man who had crept to Jesus in the dark gave him a king's burial in the open."),
    ("n12", NARRATOR, "Jesus never shamed the fear, and never shamed the night. He just answered the real question underneath — and let the courage grow on its own. Have you ever felt drawn toward something, and been afraid to let anyone else see it?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN, speaker), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
