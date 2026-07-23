#!/usr/bin/env python3
"""Narration for build-17-lazarus — John 11.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

John 11. j1..j5 are Jesus in the flesh and every one stays RED.
THE SISTERS NEVER SPOKE. Martha and Mary carry this chapter and all of it was
narrator paraphrase in white. Five lines are now WOMAN, pink. w21 and w27 use the
same ids, verses and verbatim wording already fixed in
plans/build-144-resurrection-and-the-life.json, which covers this same chapter:
  w3   John 11:3   the sisters: 'Lord, behold, he whom thou lovest is sick.'
  w21  John 11:21-22  Martha on the road
  w27  John 11:27  Martha's confession - one of the great confessions in scripture,
       and the old video reduced it to 'Martha said yes.'
  w32  John 11:32  Mary at his feet
  w39  John 11:39  Martha at the stone: 'Lord, by this time he stinketh...'
w39 now sits directly before j3, which is Jesus answering her - the exchange the old
video had as one block of white paraphrase.
n11 is the closing card and keeps its id. still_vars S1..S9 introduced.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, WOMAN

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n0", NARRATOR, "In a village called Bethany, close enough to Jerusalem to walk, there lived two sisters, Martha and Mary, and their brother Lazarus. Jesus loved this family. Their home was the one place on the whole road where he could stop being a public figure and simply be a friend. And now their brother was dying. So the sisters sent word to Jesus — not a demand, just a few aching words:"),
    # John 11:3
    ("w3", WOMAN, "Lord, behold, he whom thou lovest is sick."),
    ("n1", NARRATOR, "You would expect him to drop everything and run. He did the opposite. When the news reached him, he stayed where he was two more days. But listen to what he said about it:"),
    # John 11:4
    ("j1", JESUS, "This sickness is not unto death, but for the glory of God, that the Son of God might be glorified thereby."),
    ("n1b", NARRATOR, "He was not being careless with the people he loved. He was reaching for something deeper than a quick rescue — something that would show everyone who he really was. And it would cost those two sisters four days of grief to see it."),
    ("n2", NARRATOR, "By the time Jesus started for Bethany, the message had changed. Lazarus was not sick anymore. Lazarus was dead, and had been sealed in the tomb four days. That number is in the story on purpose. People of that time held that a soul might linger near the body for three days. Four days meant the door was shut — no lingering, no hope, no loophole left. Everyone in Bethany knew exactly how final four days was."),
    # John 11:21-22
    ("w21", WOMAN, "Lord, if thou hadst been here, my brother had not died. But I know, that even now, whatsoever thou wilt ask of God, God will give it thee."),
    ("n3", NARRATOR, "Martha heard he was finally near and ran out to meet him on the road, before he even reached the town. What she said was grief and faith tangled together in one breath:"),
    ("n4", NARRATOR, "Jesus told her, your brother will rise again. Martha nodded the way we nod at things we believe but cannot feel — yes, at the end of the world, on the last day, I know. And Jesus took the whole promise out of the far-off future and set it down in the person standing right in front of her:"),
    # John 11:25-26
    ("j2", JESUS, "I am the resurrection, and the life: he that believeth in me, though he were dead, yet shall he live: And whosoever liveth and believeth in me shall never die. Believest thou this?"),
    # John 11:27
    ("w27", WOMAN, "Yea, Lord: I believe that thou art the Christ, the Son of God, which should come into the world."),
    ("n5", NARRATOR, "He did not offer her a doctrine to file away until the last day. He offered her himself, right there in the dust of the road. Then Mary came — the quieter sister — and she fell at his feet and wept, and every mourner who had followed her out wept too. The whole road dissolved into grief."),
    # John 11:32
    ("w32", WOMAN, "Lord, if thou hadst been here, my brother had not died."),
    ("n6", NARRATOR, "And then comes the shortest verse in the whole Bible, and one of the most staggering. Jesus wept. Sit with that. The one man there who knew — knew — that in a few minutes Lazarus would be breathing again, stood at the grave of his friend and cried. Not because he had run out of options. He cried because the people he loved were broken, and death is a horror, and he would not stand there pretending it wasn't. He did not skip the grief. He walked all the way into it with them."),
    ("n7", NARRATOR, "The tomb was a cave with a heavy stone rolled across its mouth. Jesus said, take away the stone. Practical, careful Martha panicked — Lord, by now there will be a smell, it has been four days. And Jesus answered her:"),
    # John 11:39
    ("w39", WOMAN, "Lord, by this time he stinketh: for he hath been dead four days."),
    # John 11:40
    ("j3", JESUS, "Said I not unto thee, that, if thou wouldest believe, thou shouldest see the glory of God?"),
    ("n7b", NARRATOR, "So they leaned into the great stone and rolled it back, and the dark mouth of the grave stood open to the daylight."),
    ("n8", NARRATOR, "He lifted his eyes and prayed out loud — not because heaven was hard of hearing, but because he wanted the crowd to know exactly where the power came from. And then he called into the dark, in a voice they said was loud enough to wake the dead:"),
    # John 11:43
    ("j4", JESUS, "Lazarus, come forth."),
    ("n9", NARRATOR, "And the dead man came out. Bound hand and foot in strips of grave-linen, his face still wrapped, Lazarus stood in the mouth of his own tomb — alive. Four days gone, and standing in the light. Nobody moved. Nobody breathed."),
    # John 11:44
    ("j5", JESUS, "Loose him, and let him go."),
    ("n10", NARRATOR, "Unwrap him. Take the grave-linen off a living man and let him walk home to dinner. This was the last great sign before Jesus turned toward his own cross — and he did it in the open, at a marked grave, in front of a crowd, so that no one could ever call it a trick of the light. The one who stands over every grave you have ever wept beside looked death full in the face and called a friend home. He does not merely explain the resurrection. He is the resurrection."),
    ("n11", NARRATOR, "He wept at the grave, even though he was about to open it. Is there a grief you are carrying that he would not rush you past, but would sit down inside it, and weep there with you first?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}

# Cameron complaint #17 (2026-07-21, cut e090851b): shipped audio garbled the
# archaic verbs — "Believest thou this" came out "GIVE US thou this", "liveth"
# came out "lifeeth", and Michelle dropped "lovest"/"stinketh" entirely.
# All four respellings A/B-tested 2026-07-21 in the segments' real voices
# (Eric j2, Michelle w3/w39):
#   livveth   -> round-trips clean (locks short-i LIV-eth; plain flagged)
#   beleevest -> "believeth"-class round-trip (plain gave "believous"/"Give us")
#   luvvest   -> identical round-trip to plain, locks the unstable recording
#   stinkuhth -> round-trips "stinketh" exactly (plain gave "He's stinks")
# Captions keep the exact KJV words. VIDEO REBUILD DEFERRED per Cameron —
# next re-record + rebuild picks these up.
SPOKEN.update({
    "liveth": "livveth",
    "believest": "beleevest",
    "lovest": "luvvest",
    "stinketh": "stinkuhth",
})


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
