#!/usr/bin/env python3
"""Generate narration audio for Story Video #14 — The Ten Lepers
(Luke 17:11-19).
Narrator: en-US-AndrewNeural — plain American, never Multilingual.
Jesus voice: en-US-ChristopherNeural — American, never British.
Jesus speaks ONLY exact KJV: 17:14 (j1), 17:17-18 (j2), 17:19 (j3) —
verified against qc/luke17-kjv.txt (fetched from bible-api.com), never
hand-typed.
Pre-flighted on paper per PRODUCTION-BIBLE §4b — see PREFLIGHT.md.
Translation Law: no narrator line echoes KJV Jesus wording; the narrator
MAY quote the lepers' cry modernly (v13 is their words, not his).
No-Dead-Air Law: every storyboard beat s1-s12 + card has a narration line.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"     # plain American — never a Multilingual model
JESUS = "en-US-ChristopherNeural"   # American. Never a British voice.

SEGMENTS = [
    # (filename, voice, rate, pitch, text)
    # n0 — the border road (s1). v11 setting: why a mixed group exists.
    ("n0", NARRATOR, "-20%", "-4Hz",
     "On the way to Jerusalem, Jesus walked the borderland between Samaria "
     "and Galilee — the seam between two peoples who despised each other. "
     "Keep that seam in mind. It matters at the end of this story."),
    # n1 — ten at a distance (s2). v12 + the WHY-gem: the distance was LAW.
    ("n1", NARRATOR, "-20%", "-4Hz",
     "As he reached a village, ten men met him — but they stopped far off, "
     "strung along a rise, and came no closer. They were lepers. The Law "
     "of Moses required them to live outside the town and to warn everyone "
     "away. That gap of empty ground between them and the road was not "
     "shyness. It was the law. These were ten men no one had touched in "
     "years."),
    # n2 — the cry (s3). v13 — narrator MAY quote the lepers modernly.
    ("n2", NARRATOR, "-20%", "-4Hz",
     "So they did the only thing the distance left them. They lifted up "
     "their voices together and called across the gap: Jesus, Master, have "
     "mercy on us."),
    # n3 — he saw them; the instruction (s4 setup for J1). v14a.
    ("n3", NARRATOR, "-22%", "-4Hz",
     "When he saw them, he did not close the distance. He did not touch "
     "them, and he did not announce that they were healed. He simply gave "
     "them an instruction:"),
    # J1 — exact KJV Luke 17:14.
    ("j1", JESUS, "-28%", "-6Hz",
     "Go shew yourselves unto the priests."),
    # n4 — WHY that instruction (Translation Law: meaning, no KJV echo).
    ("n4", NARRATOR, "-22%", "-4Hz",
     "Now, why send them to a priest? Because in Israel the priest was the "
     "only inspector who could certify a leper clean and let him back into "
     "his family, his work, his worship. Sending them was a promise in "
     "disguise. That errand only made sense one way: if they would be "
     "clean by the time they arrived."),
    # n5 — obedience before evidence (s5). the story's hinge.
    ("n5", NARRATOR, "-24%", "-4Hz",
     "But nothing had changed yet. They looked at each other, at their own "
     "still-bandaged hands, at the long road to a city they had no proof "
     "they would be welcome in. And then, one by one, they turned and "
     "started walking anyway."),
    # n6 — HEALED as they went (s6 still+clip). THE PEAK. Music dies to
    # silence on "as they went"; the healing lands in the quiet after.
    ("n6", NARRATOR, "-25%", "-4Hz",
     "And as they went — on the road, mid-step, in the middle of obeying, "
     "before there was one thing to see — they were made clean."),
    # n7 — nine on, one sees (s7). v15a.
    ("n7", NARRATOR, "-23%", "-4Hz",
     "The linen loosened and fell. New skin underneath. Nine of them ran "
     "on toward the city, toward the priests, toward their old lives handed "
     "back. But one of them, when he saw what had happened to him, stopped "
     "in the road."),
    # n8 — the return (s8 still+clip). v15b — loud, public, running.
    ("n8", NARRATOR, "-23%", "-4Hz",
     "And he turned around. He came back the way he came, running, "
     "praising God at the top of his voice — the whole road hearing it."),
    # n9 — at his feet; the Samaritan reveal (s9). v16.
    ("n9", NARRATOR, "-24%", "-4Hz",
     "He threw himself face-down in the dust at Jesus's feet and poured out "
     "his thanks. And Luke adds one detail that would have stunned everyone "
     "listening: he was a Samaritan. The outsider. The one the religion of "
     "the day said did not belong."),
    # n10 — Jesus over the empty road (s10 setup for J2). v17-18 lead-in.
    ("n10", NARRATOR, "-24%", "-4Hz",
     "Jesus looked at the empty road where the other nine had gone, and "
     "asked:"),
    # J2 — exact KJV Luke 17:17-18.
    ("j2", JESUS, "-27%", "-6Hz",
     "Were there not ten cleansed? but where are the nine? There are not "
     "found that returned to give glory to God, save this stranger."),
    # n11 — WHY he asks (Translation Law: modern meaning only, no echo).
    ("n11", NARRATOR, "-24%", "-4Hz",
     "Except this stranger. This outsider. This is not wounded pride — the "
     "nine did nothing wrong. They obeyed, and they were healed, every one "
     "of them. His question is grief, not a scolding: they got the gift and "
     "kept walking, and they missed the giver. Only the one everyone "
     "counted out came back to find him."),
    # n12 — rising (s11 setup for J3). v19.
    ("n12", NARRATOR, "-24%", "-4Hz",
     "Then Jesus reached down to the man still trembling at his feet, and "
     "lifted him with a word:"),
    # J3 — exact KJV Luke 17:19.
    ("j3", JESUS, "-28%", "-6Hz",
     "Arise, go thy way: thy faith hath made thee whole."),
    # n13 — the cleansed-vs-whole gem (s11 close). the Seed's hinge.
    ("n13", NARRATOR, "-25%", "-4Hz",
     "Hear the two different words. All ten were cleansed — out on the "
     "road, before any of them said thank you. But only this one, the one "
     "who came back, was made whole. Cleansed happened to his skin. Whole "
     "happened to all of him."),
    # n14 — going home whole (s12).
    ("n14", NARRATOR, "-25%", "-4Hz",
     "And he rose and walked home a whole man, the old wrappings left "
     "behind him in the road."),
    # n15 — the closing card, read aloud gently (Readable-Card Law).
    ("n15", NARRATOR, "-26%", "-4Hz",
     "The healing happened while they walked, before they could see it. "
     "Have you ever had to move forward on nothing but a word — before "
     "there was any proof?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
