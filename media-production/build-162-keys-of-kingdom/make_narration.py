#!/usr/bin/env python3
"""Generate narration audio for Story Video #162 — "The keys of the kingdom"
(Matthew 16:18-19). MEMBER shelf verse-video. → Gospel Library topic: Priesthood Keys.

Narrator: en-US-AndrewNeural — plain American, modern paraphrase, never a
Multilingual model, never echoes the KJV wording.
Scripture voice: en-US-ChristopherNeural — these are the LORD'S OWN WORDS (red-letter,
Matthew 16), spoken in the reverent scripture voice, EXACT KJV only.

Jesus IS depicted (with Peter) — his face shown, locked to the JESUS-MASTER-REF master
face; only Jesus wears cream.

KJV lines (exact, red-letter):
  kv18 = Matt 16:18  upon this rock I will build my church (SACRED SILENCE 1)
  kv19 = Matt 16:19  the keys of the kingdom of heaven (NAMED VERSE — SACRED SILENCE 2)

WHY-LAW: reassurance — Jesus did not leave his church leaderless or without authority; he
built it on rock and gave real keys. STUDY GEMS: Peter's confession was revealed by the
Father (n2); the church is so founded the gates of hell cannot prevail (n5); keys mean real
authority to act in God's name, honoured in heaven (n7); given by the Lord, not seized by
men (n7).

TRANSLATION LAW: the narrator never re-quotes a KJV line. The exact KJV lands only in
kv18/kv19; the paraphrase around it uses other words.

MILK FRAMING: an invitation. The closing card ends on an open question and a one-line
pointer to the Gospel Library topic (Priesthood Keys). No shame, no fear.

NUMBER-STRESS LAW: no sentence opens with a bare number.
"""
import asyncio
import edge_tts

NARRATOR = "en-US-AndrewNeural"
SCRIPTURE = "en-US-ChristopherNeural"

SEGMENTS = [
    ("n1", NARRATOR, "-20%", "-4Hz",
     "Far to the north, at a rocky place called Caesarea Philippi, Jesus stopped with "
     "his disciples and put a piercing question to them. Who do you say that I am?"),
    ("n2", NARRATOR, "-22%", "-4Hz",
     "It was Simon Peter, the fisherman, who answered for them all. You are the Christ, "
     "he said, the Son of the living God. And Jesus told him that flesh and blood had "
     "not revealed that to him; his Father in heaven had."),
    ("n3", NARRATOR, "-22%", "-4Hz",
     "Then Jesus said something that would change Simon's life. He gave him a new name — "
     "Peter, which means a rock — and told him that on rock like that, solid and sure, "
     "he would build something meant to outlast the ages."),
    # kv18 — SACRED SILENCE 1
    ("kv18", SCRIPTURE, "-26%", "-6Hz",
     "And I say also unto thee, That thou art Peter, and upon this rock I will build my "
     "church; and the gates of hell shall not prevail against it."),
    ("n4", NARRATOR, "-22%", "-4Hz",
     "His church, he called it — his own gathered people, built on a firm foundation, "
     "and so strong that not even the gates of death and darkness could ever overpower "
     "it or shut it down."),
    ("n5", NARRATOR, "-22%", "-4Hz",
     "That is a staggering promise. Empires would fall, storms would come, the powers of "
     "the grave itself would batter against it — and still it would stand, because its "
     "foundation was laid by God and not by men."),
    ("n6", NARRATOR, "-22%", "-4Hz",
     "But Jesus was not finished. He would not leave his church without a way to be led. "
     "So he turned to Peter and promised him something specific — real authority, handed "
     "down from heaven itself. He called it keys."),
    # kv19 — NAMED VERSE, SACRED SILENCE 2
    ("kv19", SCRIPTURE, "-26%", "-6Hz",
     "And I will give unto thee the keys of the kingdom of heaven: and whatsoever thou "
     "shalt bind on earth shall be bound in heaven: and whatsoever thou shalt loose on "
     "earth shall be loosed in heaven."),
    ("n7", NARRATOR, "-22%", "-4Hz",
     "Keys open and close, lock and unlock, admit and secure. To hold the keys of the "
     "kingdom is to carry real authority to act in God's name, so that what is done "
     "rightly on earth is honoured in heaven — not invented by men, but given by the "
     "Lord."),
    ("n8", NARRATOR, "-24%", "-4Hz",
     "So Jesus did not leave his people leaderless, or his church without authority. He "
     "built it on rock and placed real keys in human hands. So the only question is a "
     "hopeful one. When you find that authority, given by him and not seized by men, will "
     "you trust it?"),
    ("card", NARRATOR, "-26%", "-4Hz",
     "Jesus built his church on rock and gave Peter the keys of the kingdom — real "
     "authority, binding on earth and in heaven, given by the Lord and not seized by men. "
     "When you find it, will you trust it?"),
]


async def main():
    for name, voice, rate, pitch, text in SEGMENTS:
        tts = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await tts.save(f"audio/{name}.mp3")
        print(f"saved audio/{name}.mp3")

if __name__ == "__main__":
    asyncio.run(main())
