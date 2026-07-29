#!/usr/bin/env python3
"""Narration for build-38-persistent-widow — Luke 18.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

PARABLE LAW APPLIED. Luke 18:1-8 is one of Jesus's parables, so every character
inside it speaks Jesus's words and a red-letter KJV inks the whole thing red.

STAYED RED, and correctly so:
  j1  Luke 18:4-5  'Though I fear not God, nor regard man; yet because this widow
      troubleth me, I will avenge her, lest by her continual coming she weary me.'
      This is the unjust judge talking to himself. It is NOT a man in a story
      getting a blue voice -- it is Jesus putting words in a character's mouth
      inside his own parable, and a red-letter Bible prints it red. Left alone.
  j2  Luke 18:6-7  'Hear what the unjust judge saith. And shall not God avenge his
      own elect...' Jesus in his own voice. No framing welded on, so no split.

THE WIDOW -- LOOKED FOR HER, AND SHE IS RED, NOT PINK. Luke 18:3 records her
speaking: 'Avenge me of mine adversary.' She is a woman with a recorded line, but
she is a character inside a parable, and the test is never who the character is --
it is whether a red-letter KJV prints the line red. It does. So her words come in
as part of the new jv2 block, in Jesus's voice, red. This is a deliberate call and
it is the difference between build-144 (Martha, a real woman in a real conversation,
pink) and this one. Nothing about her is lost; she is finally heard saying her own
seven words instead of being paraphrased.

BLUE ADDED -- LUKE'S FRAMING, WHICH WAS MISSING ENTIRELY:
  s1  Luke 18:1  'And he spake a parable unto them to this end, that men ought
      always to pray, and not to faint.' That is Luke writing, not Jesus speaking,
      so it is `scripture`, light blue. It is also the thesis sentence of the whole
      video and it was nowhere in the build. New n1b retells it, then the existing
      n1 opens the story as before.

RED ADDED -- THE PARABLE NOW ACTUALLY GETS TOLD:
  jv2 Luke 18:2-3  'There was in a city a judge, which feared not God, neither
      regarded man: And there was a widow in that city; and she came unto him,
      saying, Avenge me of mine adversary.' The setup and the widow's plea were
      both narrator paraphrase in n2. n2 keeps its id and now retells it.
  jv8 Luke 18:8  'I tell you that he will avenge them speedily. Nevertheless when
      the Son of man cometh, shall he find faith on the earth?' The video stopped
      at verse 7 and skipped the payoff. New n7b retells it before n7 and n8 land
      the point.

Deliberately NOT lifted: verse 4a, 'And he would not for a while.' n3 and n4 carry
that stretch better in the storyteller's voice, and lifting it would turn the
middle of the video into recitation. Verbatim and retelling alternate throughout.

NO GREEN: nothing in Luke 18:1-8 is the Father speaking.

WHY-LAW: the judge is not a picture of God, he is the opposite of God. The whole
argument is 'how much more.' Milk: you are not wearing him down, you are talking to
someone who has been waiting to hear from you.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    ("s1", SCRIPTURE, 'And he spake a parable unto them to this end, that men ought always to pray, and not to faint.'),
    ("n1b", NARRATOR, 'Luke tells us up front why Jesus told this one. He wanted people to keep praying and not lose heart. That is the whole reason the story exists.'),
    ("n1", NARRATOR, 'Jesus told a story about a widow. She had lost her husband and had no one to protect her. Someone had wronged her, and she had no power, no money, no one important to make anyone listen.'),
    ("jv2", JESUS, 'There was in a city a judge, which feared not God, neither regarded man: And there was a widow in that city; and she came unto him, saying, Avenge me of mine adversary.'),
    ("n2", NARRATOR, 'The widow came to him with one simple plea: give me justice against the man who wronged me.'),
    ("n3", NARRATOR, 'But the judge did not care. He waved her away. She had nothing to offer him, no bribe, no rank, no reason for him to lift a finger.'),
    ("n4", NARRATOR, 'So she came back. And again. And again. She would not stop. Every day the same worn face at his door, the same steady voice asking for what was right.'),
    ("j1", JESUS, 'Though I fear not God, nor regard man; yet because this widow troubleth me, I will avenge her, lest by her continual coming she weary me.'),
    ("n5", NARRATOR, 'Fine, the judge finally said. I do not fear God, and I do not care about her. But she is wearing me out. I will give her justice just to be rid of her.'),
    ("j2", JESUS, 'Hear what the unjust judge saith. And shall not God avenge his own elect, which cry day and night unto him, though he bear long with them?'),
    ("n6", NARRATOR, 'Listen to what even that cold judge finally did, Jesus said. Now think about God. If a man who cares for no one will still give justice to the one who keeps coming, how much more will your Father, who loves you, hear you?'),
    ("jv8", JESUS, 'I tell you that he will avenge them speedily. Nevertheless when the Son of man cometh, shall he find faith on the earth?'),
    ("n7b", NARRATOR, 'He will not drag his feet, Jesus said. He will act, and quickly. And then he asked one more question, almost quietly. When the Son of Man comes back, will he find anybody still believing that?'),
    ("n7", NARRATOR, 'Here is the whole point. God is not that judge. He is not reluctant. He is not annoyed by you. He does not have to be worn down into caring, because he already loves you, and he already wants to hear you.'),
    ("n8", NARRATOR, 'So when Jesus says to keep praying and never give up, it is not because God is hard to move. It is because he is the very opposite of that judge, and he has been waiting to hear from you all along.'),
    ("card", NARRATOR, "God is not the reluctant judge. What have you stopped asking him for, because you assumed he wasn't listening?"),
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
