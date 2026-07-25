# PRESCRIPTION — build-64-pool-of-bethesda

**Row:** 64   **Shelf:** Everyone   **Scripture:** John 5:1–15
**Tier:** T2 Encounter   **Length:** 227s (keep — the audio carries a long, real drama)
**Pictures:** 11 beats (current 9 stills → beats are being skipped)

> "Wilt thou be made whole?" — consent. The narration moves through the crowded five
> porches, the man of thirty-eight years, the question, his answer-with-the-obstacle,
> "rise, take up thy bed, and walk," the man standing and rolling up his mat, the
> sabbath rule-keepers, his not even knowing the name, Jesus finding him again in the
> temple, and the man learning at last who healed him. Eleven moments, carried now on 9.

## The impact read
- **The one thing:** he doesn't ask whose fault it is or why you're still here — he
  asks whether you want to be whole, and the healing never depended on the pool.
- **The turn:** "Wilt thou be made whole?" → "Rise, take up thy bed, and walk." The
  hinge is the man standing after thirty-eight years, no angel, no water, no race.
- **Character shown:** he singles out the one among hundreds, and grace comes before
  the man can even name him.
- **Whose face carries it:** THE MAN — thirty-eight years of resignation, then the
  question, then standing, then recognition. Jesus's face allowed (face-locked) at
  the question and the temple; the weight stays on the man.
- **The card question falls out of:** "Do you want to be whole?" — the card asks it
  straight, off the one thing. No change needed.

## Beat list (= the picture plan) — 11 stills
1. [n0] the five porches of Bethesda crowded with the blind, lame, and paralyzed, all watching the water — agrees: "ringed by five covered porches... all waiting on a legend"
2. [n1] the one man on his mat, thirty-eight years, worn into the place, watching the water he can never reach first — "One man had been lying there thirty-eight years"
3. [n2/j1] Jesus stopping at this one man among the hundreds, asking — "Wilt thou be made whole?"
4. [n3/s7] the man not saying yes, answering with the obstacle — no one to put him in — "Sir, I have no man... another steppeth down before me"
5. [j2] Jesus: "Rise, take up thy bed, and walk"
6. [n4] the man standing — thirty-eight years of atrophy gone — rolling up the mat that was his whole world, and walking — "He stood up, rolled up the mat... and walked"
7. [n5/s10] the sabbath rule-keepers stopping him — about the mat — "It is the sabbath day: it is not lawful for thee to carry thy bed"
8. [n5b] the healed man unable to name who healed him — grace came first — "when they asked who had healed him, he did not know"
9. [n6/j14] Jesus finding him again in the temple — "Behold, thou art made whole: sin no more, lest a worse thing come unto thee"
10. [n6b] the man realizing the name at last, going to tell everyone it was Jesus — "He went and told everyone: it was Jesus"
11. [card] hold on the man standing, whole, for the closing question

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n0, n1, n2, n3, n3b, n4, n5, n5b, n6, n6b, n7, card
- **SCRIPTURE** (light blue): s7, s10
- **JESUS** (red): j1, j2, j14
- No women speak. Narrator sets scene + retells the KJV lines in modern English.

## The fix
Current 9 stills. Split the man standing/walking (6) from the sabbath-mat confrontation
(7), give the not-knowing-the-name beat (8) its own frame, and split the temple
finding (9) from the man telling everyone (10). Rewire build.py BEATS so each still
switches when its words arrive. Let beat 6 (standing after 38 years) breathe.

## Deviations from the band
Runtime **227s** sits well over the T2 length band (80–120s). I prescribe pictures
only and keep the audio unchanged (Part 5) — the narration is a full, real drama.
Flagging the length so no one "fixes" it by trimming narration.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] Jesus via master ref; the man's face carries beats 2, 6, 10
- [ ] `bash admin/verify-mp4.sh <mp4> 227` green; frame-verify beats 2, 6, 9
