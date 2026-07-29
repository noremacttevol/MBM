#!/usr/bin/env python3
"""Narration for build-45-wicked-tenants — Mark 12.

SPEAKER-LAW rebuild (see media-production/SPEAKER-LAW.md). Who is speaking is
declared once here and decides BOTH the voice and the caption colour.

PARABLE LAW APPLIED. Mark 12:1-11 is one parable, so the husbandmen plotting among
themselves and the owner hoping out loud are both Jesus's words, and a red-letter KJV
inks the whole thing red. Nothing became blue.

STAYED RED, all five, correct as they stood:
  jv1   Mark 12:1     'A certain man planted a vineyard...'
  jv2   Mark 12:2     'And at the season he sent to the husbandmen a servant...'
  jv6   Mark 12:6     'Having yet therefore one son, his wellbeloved... They will
        reverence my son.' -- the owner's own hope, spoken inside the parable. Red.
  jv9   Mark 12:9     'What shall therefore the lord of the vineyard do?...'
  jv10  Mark 12:10-11 the stone the builders rejected.

BLUE ADDED -- the one sentence in the passage Mark wrote rather than Jesus spoke:
  s1  Mark 12:1a  'And he began to speak unto them by parables.' `scripture`, light
      blue. It now opens the video and the existing n1 keeps its id and retells it,
      naming the temple and the men plotting against him. Frame blue on S1, parable
      red from S2 on. This is the split the law asks for, and it costs no artwork.

RED ADDED -- THE MIDDLE OF THIS PARABLE WAS ALL PARAPHRASE. Four of Jesus's blocks
come back in, each one alternating with the existing narrator beat that now retells it:
  jv3    Mark 12:3    'And they caught him, and beat him, and sent him away empty.'
         n5 retells it.
  jv4_5  Mark 12:4-5  'And again he sent unto them another servant; and at him they
         cast stones, and wounded him in the head, and sent him away shamefully
         handled. And again he sent another; and him they killed, and many others;
         beating some, and killing some.' This whole escalation -- which is the
         patience the video is about -- was one sentence of white paraphrase in n6.
         n6 keeps its id and now retells it.
  jv7    Mark 12:7    'But those husbandmen said among themselves, This is the heir;
         come, let us kill him, and the inheritance shall be ours.' THIS IS THE LINE
         MOST LIKELY TO BE MISPAINTED IN THE WHOLE BUILD. It is villains talking, and
         it is still RED, because they are characters inside Jesus's parable. n9
         already calls it 'the coldest arithmetic in any story he ever told' and now
         the viewer hears the arithmetic in Jesus's own words.
  jv8    Mark 12:8    'And they took him, and killed him, and cast him out of the
         vineyard.' n10 keeps its id and retells it in the restrained way it already
         did -- 'the story does not linger on it and neither will we.'

Deliberately NOT lifted: Mark 12:12, 'And they sought to lay hold on him... and left
him, and went their way.' That is Mark narrating and would be blue, but n13 handles the
reaction better and the video ends on the owner who never stopped sending, not on the
men walking off.

NO GREEN and NO WOMEN in Mark 12:1-12. Nothing invented.

WHY-LAW: the owner kept sending after every reason to stop. Milk: he is not looking
for a reason to be done with you.
"""
import asyncio
import os

from mbm_caption_timing import save_speaker_narration
from mbm_pronounce import audit, spoken_text
from mbm_speakers import JESUS, NARRATOR, SCRIPTURE

# (id, speaker, caption_text). The caption always shows this exact text; only the
# string handed to the TTS is respelled.
SEGMENTS = [
    # Mark 12:1
    ("s1", SCRIPTURE, "And he began to speak unto them by parables."),
    ("n1", NARRATOR, "He told this one in the temple, standing in front of the very men who were plotting against him. And underneath it, it is a story about patience. About an owner who kept giving people one more chance, long past the point anyone else would have."),
    # Mark 12:1
    ("jv1", JESUS, "A certain man planted a vineyard, and set an hedge about it, and digged a place for the winefat, and built a tower, and let it out to husbandmen, and went into a far country."),
    ("n2", NARRATOR, "Picture how much he put into it. He broke the ground and set in the young vines, ringed it with a wall to guard them, hollowed out a press for the grapes, and raised a lookout over the whole field. Everything was ready. Then he handed the whole place to the workers and trusted them with it."),
    ("n3", NARRATOR, "And he left. That is the setup. The owner is far away, the workers have the run of the place, and all he asked for was a share of the harvest when it came in, the way any honest agreement works."),
    # Mark 12:2
    ("jv2", JESUS, "And at the season he sent to the husbandmen a servant, that he might receive from the husbandmen of the fruit of the vineyard."),
    ("n4", NARRATOR, "So when the season came, he sent a man to collect his share. Not soldiers. One messenger, walking up the road with an empty basket, expecting nothing but an honest exchange."),
    # Mark 12:3
    ("jv3", JESUS, "And they caught him, and beat him, and sent him away empty."),
    ("n5", NARRATOR, "And the man came back with the basket still empty, and shaken. They had handled him roughly and sent him off with nothing. Now here is where the story stops making ordinary sense. Anyone else sends the law next. This owner sent another messenger."),
    # Mark 12:4-5
    ("jv4_5", JESUS, "And again he sent unto them another servant; and at him they cast stones, and wounded him in the head, and sent him away shamefully handled. And again he sent another; and him they killed, and many others; beating some, and killing some."),
    ("n6", NARRATOR, "And they treated that one worse. And another after that. Message after message, season after season, and every time it came back the same, or did not come back at all."),
    ("n7", NARRATOR, "Stop and feel how strange that is. Every reasonable line was crossed a long time ago. He had every right to come with force and end it. Instead he kept doing the one thing that left him exposed. He kept reaching out to people who had already shown him exactly who they were."),
    # Mark 12:6
    ("jv6", JESUS, "Having yet therefore one son, his wellbeloved, he sent him also last unto them, saying, They will reverence my son."),
    ("n8", NARRATOR, "He had one person left. His son. The one he loved most in the world. And he sent him too, holding on to a hope you can hear him say out loud. Surely they will respect my son."),
    # Mark 12:7
    ("jv7", JESUS, "But those husbandmen said among themselves, This is the heir; come, let us kill him, and the inheritance shall be ours."),
    ("n9", NARRATOR, "But when the workers saw the son coming up the road, they did not see a person. They saw an opening. If the heir is gone, they said to each other, the whole place falls to us. It is the coldest arithmetic in any story he ever told."),
    # Mark 12:8
    ("jv8", JESUS, "And they took him, and killed him, and cast him out of the vineyard."),
    ("n10", NARRATOR, "You can guess what they chose. The story does not linger on it and neither will we. They shut him out, and they took his life. And the father who had waited all those years, still hoping, lost the one he loved most of all. That is how far the patience went, and what it finally cost him."),
    # Mark 12:9
    ("jv9", JESUS, "What shall therefore the lord of the vineyard do? he will come and destroy the husbandmen, and will give the vineyard unto others."),
    ("n11", NARRATOR, "Then he turned it into a question. What is the owner going to do now? And the weight of the answer is not really the punishment. It is that the vineyard finally passes to people who will actually tend it and give its fruit back. The trust does not vanish. It goes to hands that will keep it. And then he reached back into their own scriptures for the last word."),
    # Mark 12:10-11
    ("jv10", JESUS, "And have ye not read this scripture; The stone which the builders rejected is become the head of the corner: This was the Lord's doing, and it is marvellous in our eyes?"),
    ("n12", NARRATOR, "The block the builders threw on the reject pile turned out to be the one the whole building leans its weight on. He is talking about himself. The son they were ready to throw out is the foundation everything else gets built on. They meant it for an ending. It was the beginning."),
    ("n13", NARRATOR, "The men he told it to heard themselves in it, and it made them furious. But sitting right underneath their anger is the kindest fact in the whole story. The owner never stopped sending. Not after the first, not after the tenth, not even after the worst. That is the God this whole thing is about."),
    ("card", NARRATOR, "He told this to the very people about to reject him, and he was still calling them in. An owner who keeps sending, after all of that, is not looking for a reason to be done with you. What would you do with a patience like that?"),
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
