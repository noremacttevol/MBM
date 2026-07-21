#!/usr/bin/env python3
"""Narration for build-119-fourth-man-in-fire — Daniel 3.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

Nothing in this build was painted red, and nothing becomes red. Daniel is Old
Testament - a red-letter KJV prints none of it in red, so no segment is `jesus`.

The fourth figure is described by Nebuchadnezzar as 'like the Son of God', and
Latter-day Saints understand that as the premortal Christ. But that figure never
SPEAKS in Daniel 3 - there is no line to colour. Nebuchadnezzar's report about him is
Nebuchadnezzar talking, so it is SCRIPTURE (light blue), not god and not jesus. The
video says nothing on screen about who the fourth man is. Milk, not meat.

FIVE LINES LIFTED OUT OF NARRATOR PARAPHRASE - this build had zero non-narrator beats
and Daniel 3 is almost entirely dialogue, so it gained the most:
  s315  Daniel 3:15  the king's ultimatum, ending 'who is that God that shall deliver
                     you out of my hands?' - SCRIPTURE
  s317  Daniel 3:17-18  'our God whom we serve is able to deliver us... But if not,
                     be it known unto thee, O king, that we will not serve thy gods.'
                     The line the whole video is built around, and it was only being
                     paraphrased. Now verbatim, SCRIPTURE.
  s325  Daniel 3:25  'Lo, I see four men loose...' - was already sitting verbatim
                     inside narrator beat n6, spoken in the narrator's voice.
  s326  Daniel 3:26  'ye servants of the most high God, come forth, and come hither'
  s328  Daniel 3:28  'Blessed be the God of Shadrach, Meshach, and Abednego' - was
                     also sitting verbatim inside narrator beat n10.

Notice the shape this gives the video: the king asks 'who is that God that shall
deliver you' at the start and answers his own question at the end. That was invisible
while both lines were narrator paraphrase.

SPOKEN: left empty. Nebuchadnezzar and Abednego are already in the global pronunciation
map. 'bow' appears here meaning to bend down, NOT the archery bow, so it must NOT be
respelled - flagging that because build-135 respells it the other way.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("n1", NARRATOR, "A king built a golden statue ninety feet high and made one rule: when the music plays, everyone bows. And everyone did — a whole plain of people face-down in the dust. Everyone except three."),
    ("n2", NARRATOR, "Shadrach, Meshach, and Abednego would not bow to anything but God. So they were dragged before the furious king, who gave them one last chance, and finished it with a dare."),
    # Daniel 3:15
    ("s315", SCRIPTURE, "But if ye worship not, ye shall be cast the same hour into the midst of a burning fiery furnace; and who is that God that shall deliver you out of my hands?"),
    ("n2b", NARRATOR, "Bow, or burn. And who is this God of yours who could possibly get you out of my hands? Hold on to that question. The king is going to answer it himself before this is over."),
    # Daniel 3:17-18
    ("s317", SCRIPTURE, "Our God whom we serve is able to deliver us from the burning fiery furnace, and he will deliver us out of thine hand, O king. But if not, be it known unto thee, O king, that we will not serve thy gods, nor worship the golden image which thou hast set up."),
    ("n3", NARRATOR, "Our God can save us, they said, and we believe he will. But if not — if he does not — we still will not bow. That is one of the bravest things anyone ever said. They did not obey because they were promised a rescue. They obeyed because he is God either way."),
    ("n4", NARRATOR, "So the king had the furnace stoked seven times hotter than ever and had the three cast in, still bound hand and foot — a fire so fierce no one should have survived a single moment in it."),
    ("n5", NARRATOR, "And that is exactly when the impossible began. The ropes burned away, but the men did not. They stood up inside the fire, unharmed, not a single thread of their clothing even scorched."),
    ("n6", NARRATOR, "Then the king leapt up off his seat in astonishment. He had thrown in three men, bound. Now he was counting four, walking loose. And this is what he said out loud, in front of his whole court."),
    # Daniel 3:25
    ("s325", SCRIPTURE, "Lo, I see four men loose, walking in the midst of the fire, and they have no hurt; and the form of the fourth is like the Son of God."),
    ("n6b", NARRATOR, "Four men, loose, walking in the middle of the fire, and none of them hurt. And the fourth one, the king says, looks like the Son of God. The man who gave the order to light that furnace is now the eyewitness describing what came of it."),
    ("n7", NARRATOR, "They were not alone in the fire. Whatever else that fourth figure was, it walked with them, and where it walked the flames could not touch them. God had not kept them out of the furnace — he met them inside it."),
    # Daniel 3:26
    ("s326", SCRIPTURE, "Shadrach, Meshach, and Abednego, ye servants of the most high God, come forth, and come hither."),
    ("n8", NARRATOR, "Come out, he called them — servants of the most high God. The man who demanded they call his statue god is now calling their God the highest one there is. And they walked from the heart of the fire onto solid ground, alive and whole, in front of everyone who had watched them go in."),
    ("n9", NARRATOR, "The officials crowded around and could not believe it. Not a hair of their heads was singed, their coats were not burned, and there was not even the smell of smoke on them. The fire had done nothing at all."),
    # Daniel 3:28
    ("s328", SCRIPTURE, "Blessed be the God of Shadrach, Meshach, and Abednego, who hath sent his angel, and delivered his servants that trusted in him."),
    ("n10", NARRATOR, "Blessed be their God, the proud king says, who sent his angel and rescued the servants that trusted him. That is the same man who asked, an hour earlier, who is that God that shall deliver you out of my hands. He got his answer, and he said it himself."),
    ("card", NARRATOR, "God never promised these three that they would not face the fire. He promised something better — that he would be in it with them. What would change if you believed God meets you inside the hard thing, not only on the far side of it?"),
]

# Homographs this build decides for itself (never auto-replaced globally).
SPOKEN = {}


SPOKEN.update({'Meshach': 'meeshak'})  # 2026-07-21: shipped narrator audio said "Emi Shek"/"Amishach"; plain "Meshach" is UNSTABLE in Andrew's voice (fresh render clean, recorded mp3 bad). 'meeshak' round-trips "Meshach" 3/3 in Andrew (already the measured winner for the scripture voice). Cameron complaint #119 area.
SPOKEN.update({'Shadrach': 'shadrack'})  # 2026-07-21: the GLOBAL 'SHAD-rak' entry is a hyphen split (Trap 2) — Steffan's recorded s326 take said "Red Rack". 'shadrack' round-trips "Shadrach" clean in Steffan; single word, no hyphen. Build override beats the global map.

async def main():
    os.makedirs("audio", exist_ok=True)
    for name, speaker, text in SEGMENTS:
        flagged = [w for w in audit(text) if w not in SPOKEN]
        if flagged:
            print(f"  ! {name}: undecided homograph(s) {flagged}")
        await save_speaker_narration(spoken_text(text, SPOKEN), speaker,
                                     f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3  [{speaker}]")


if __name__ == "__main__":
    asyncio.run(main())
