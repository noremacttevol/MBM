# PRESCRIPTION — build-60-gerasene-demoniac

**Row:** 60   **Shelf:** Everyone   **Scripture:** Mark 5:1–20
**Tier:** T3 Full Arc   **Length:** 227s (keep — the audio carries a long, real drama)
**Pictures:** 16 beats (current 9 stills → the words go to places the pictures don't)

> He crossed a whole sea in a storm for one man. The narration moves through the
> Gentile shore at dawn, the man among the tombs, the broken chains, the run and the
> fall, "torment me not," "come out," "what is thy name / Legion," the herd of pigs,
> the stampede into the sea, the pig-tenders' flight, the town finding the man in his
> right mind, their fear, the boat and the man's plea, "go home and tell them," and
> the healed man's mission through the Decapolis. Sixteen moments, carried now on 9.

## The impact read
- **The one thing:** there is no distance he will not cross for the one person
  everyone else has written off.
- **The turn:** the town gave up on the man and didn't even know Jesus — but the
  darkness knew it was finished. The hinge is the man clothed, calm, in his right
  mind at Jesus's feet (the before/after the whole town comes to see).
- **Character shown:** fearless compassion; then he makes the outcast his first
  missionary.
- **Whose face carries it:** THE DEMONIAC — torment among the tombs, then the quiet
  restored face at Jesus's feet. Jesus's face is allowed via master ref (this build
  is face-locked); keep the emotional weight on the man.
- **The card question falls out of:** "There is no distance he will not cross for
  you." — the card is a statement here, and it lands on the one thing. No change.

## Beat list (= the picture plan) — 16 stills
1. [n0] the boat touching the far Gentile shore at first light, weary disciples, pigs on the hills — agrees: "The boat touched the far shore... first light... herds of pigs on the hills"
2. [n1] the man living among the tombs — driven out, the town's warning — "He made his home among the tombs... He was a warning"
3. [n1] the broken chains no one could bind him with — "They had tried chains. He tore them apart"
4. [n2] the man seeing Jesus far down the shore and running to fall at his feet — "He ran and fell down at his feet"
5. [s7] the tormented man at Jesus's feet, the thing inside crying out — "What have I to do with thee, Jesus, thou Son of the most high God?... torment me not"
6. [n3/j1] Jesus unafraid, commanding the spirit — "Come out of the man, thou unclean spirit"
7. [j2/s9] Jesus asking "What is thy name?" and the answer — "My name is Legion: for we are many"
8. [n6] the herd of about two thousand pigs feeding on the hillside above — "a herd of about two thousand pigs was feeding"
9. [s12/n6b] the spirits begging into the pigs; the herd stampeding down the steep bank into the sea — "the whole herd stampeded down the steep bank into the sea"
10. [n6b] the pig-tenders running for town with the story of their lives — "The men tending the pigs ran for town"
11. [n7] the town arriving to find the man clothed, calm, in his right mind, at Jesus's feet — "sitting quietly at the feet of Jesus. Clothed. Calm. In his right mind"
12. [n7] the townspeople afraid, asking Jesus to leave — "they were afraid... So they asked Jesus to leave"
13. [n8] Jesus stepping into the boat as the healed man begs to come with him — "as he climbed into the boat, the healed man begged to come with him"
14. [j3] Jesus giving him his commission instead — "Go home to thy friends, and tell them how great things the Lord hath done for thee"
15. [n9] the healed man going out through the Decapolis, telling his story, people amazed — "a one-man mission to the ten Gentile cities of the Decapolis. And everywhere he went, people were amazed"
16. [card] hold on the healed man, sent out, for the closing card

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n0, n1, n2, n2b, n3, n4, n5, n6, n6b, n7, n8, n9, card
- **SCRIPTURE** (light blue): s7, s9, s12
- **JESUS** (red): j1, j2, j3
- No women speak. Narrator sets scene + retells the KJV lines in modern English.

## The fix
Current 9 stills. Split the tombs vs the broken chains (2, 3), the stampede vs the
pig-tenders' flight (9, 10), the restored man vs the town's fear (11, 12), and the
boat-plea vs the commission vs the Decapolis mission (13, 14, 15). Rewire build.py
BEATS so each still switches when its words arrive. Let beat 11 (the man in his
right mind) breathe — it is the whole reversal.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] Jesus via master ref only; emotional weight stays on the man (beats 5, 11)
- [ ] `bash admin/verify-mp4.sh <mp4> 227` green; frame-verify beats 3, 9, 11

## Length read
Verdict: TRIM to ~205s — cut n2b's editorial aside ("Hear what just happened...")
A genuine multi-scene arc (storm crossing, tombs, Legion, swine, the town, the sending), so most of the 227s earns its place; but n2b stops the story to explain the irony to the viewer, which Part B forbids.

## Narration read
- Narrator fixes: n2b ("Hear what just happened. The man's own town... The darkness holding him knew...") → trim to the plain contrast or cut; it editorializes instead of advancing the scene.
- Scripture lifts: none available — j1/j2/j3 red; the Legion's three lines (s7, s9, s12) already blue.
- Cast/colour: correct — the spirit's "Son of the most high God" stays SCRIPTURE/blue (the spirit is speaking, not Deity), so no green.
