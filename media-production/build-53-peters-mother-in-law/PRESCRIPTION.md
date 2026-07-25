# PRESCRIPTION — build-53-peters-mother-in-law

**Row:** 53   **Shelf:** Everyone   **Scripture:** Mark 1:29–31
**Tier:** T2 Encounter   **Length:** 100s (keep — the audio is fine)
**Pictures:** 10 beats (current 8 stills → a few beats are being skipped)

> A quiet, no-audience miracle. The narration walks a small, ordinary path — the
> friends coming home, the heavy house, the sickbed in the back room, the family
> telling Jesus, him going in, taking her hand, the fever gone, her rising to serve.
> Ten distinct moments, carried now on 8 stills. Read it and give each its frame.

## The impact read
- **The one thing:** he comes into ordinary houses for quiet needs no crowd ever
  hears about — you don't need the right words, only to tell him where it hurts.
- **The turn:** "they told Jesus about her" → "he came and took her by the hand,
  and lifted her up." The hinge is the hand — the plainest possible mercy.
- **Character shown:** tender attentiveness to the small, private, unglamorous need.
- **Whose face carries it:** THE MOTHER — fever-flushed, then whole, then up and
  serving. Jesus's face not shown in the raising; hand + over-the-shoulder only.
- **The card question falls out of:** "What would it mean to simply put your trouble
  into his hand?" — lands directly on the one thing. No change needed.

## Beat list (= the picture plan) — 10 stills
1. [n1] Jesus and the four (Simon, Andrew, James, John) leaving the synagogue, walking home together — agrees: "he went home with his friends, into the house of Simon and Andrew"
2. [n2] the ordinary house, the family inside weighed down and anxious — "the house was heavy, because someone they loved was ill"
3. [n3] the mother lying in the back room, sick with fever, someone sitting beside her worrying — "Simon's wife's mother lay in a back room, sick with a fever"
4. [n4] the disciples quietly telling Jesus about her, no speech, just their trouble — "they simply brought their trouble to him"
5. [n5] Jesus stepping into the room where she lies — "he went in to where she was lying"
6. [s31] Jesus taking her by the hand and lifting her up (his hand + her face, over-the-shoulder) — "took her by the hand, and lifted her up"
7. [n6] her face — fever gone, colour back, well and strong — "she was herself once more, well and strong"
8. [n7] the woman up on her feet, serving the family who had carried her trouble to Jesus — "the first thing she did was rise and serve them"
9. [n8] wide, warm: the tired family together in the ordinary house, the quiet miracle — "a tired family, a sickbed, and a Savior who came in"
10. [card] warm hold on the household for the closing question — the card line

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n1, n2, n3, n4, n5, n6, n7, n8, card
- **SCRIPTURE** (light blue): s31
- No JESUS-spoken lines in this cut; no women speak. Narrator only sets scene; the
  card carries the meaning (Part 4 rule).

## The fix
Current 8 stills. Add the leaving-the-synagogue frame (1) and the "telling Jesus"
frame (4), and split the single raising into the hand (6), her restored face (7),
and her rising to serve (8) — the words go to each of those and the picture should
too. Not re-timing audio; rewire build.py BEATS so each still switches when its
words arrive. Let the hand-and-lift (6) breathe.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] Jesus's face not shown at beat 6 (hand + over-the-shoulder)
- [ ] `bash admin/verify-mp4.sh <mp4> 100` green; frame-verify beats 6, 7, 8

## Length read
Verdict: KEEP ~100s
Ten short segments carry Mark 1:29-31 end to end with no repetition and no over-explaining. The one reflective line (n8, "a small, quiet miracle... no crowd and no spectacle") is brief and reverent, so it stays.

## Narration read
- Narrator fixes: n8 slightly does the card's summarizing job ("a small, quiet miracle, tucked into an ordinary house") — trim only if a second is needed; otherwise clean.
- Scripture lifts: none available — Mark 1:29-31 records no direct speech from anyone; the healing verse is already lifted as s31 (SCRIPTURE/blue).
- Cast/colour: correct — no red/green/pink because no one speaks; Mark's sentence is blue. The woman is silent in Mark, Matthew 8 and Luke 4, so no pink is right.
