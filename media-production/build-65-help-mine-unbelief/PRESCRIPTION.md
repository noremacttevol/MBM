# PRESCRIPTION — build-65-help-mine-unbelief

**Row:** 65   **Shelf:** Everyone   **Scripture:** Mark 9:14–29
**Tier:** T3 Full Arc   **Length:** 210s (keep — the audio carries a long, real drama)
**Pictures:** 13 beats (current 8 stills → the words go to places the pictures don't)

> Half-faith honestly offered is enough. The narration moves through the chaotic
> crowd and the failed disciples, the desperate father's story, the boy's lifelong
> torment, the trembling "if," Jesus's answer, the father's honest prayer, both faith
> and unbelief laid down together, the command out of the boy, the boy gone still,
> the hand lifting him up, the son given back, and the private lesson about prayer.
> Thirteen moments, carried now on 8.

## The impact read
- **The one thing:** you don't need perfect faith to come to him — the little you
  have, plus the doubt you're ashamed of, honestly offered, is enough.
- **The turn:** the father refuses to fake faith and instead hands Jesus his cracked
  one — "Lord, I believe; help thou mine unbelief." That prayer is the hinge.
- **Character shown:** he receives honest, unfinished faith and does not despise the
  doubt underneath it.
- **Whose face carries it:** THE FATHER — years of watching his son suffer, then the
  cracked honest prayer, then the reunion — and the boy's face. Jesus's face allowed
  (face-locked) at the command; the emotional weight is the father's and the boy's.
- **The card question falls out of:** "Bring the little you have — and the doubt —
  and ask him to help you believe." — lands on the one thing. No change needed.

## Beat list (= the picture plan) — 13 stills
1. [n0] Jesus coming down the mountain into a chaotic, arguing crowd — his disciples cornered and embarrassed, having failed — agrees: "walked straight into a mess... his own disciples were... cornered and embarrassed"
2. [n1] the desperate father pushing through, telling Jesus the whole story, his tormented son beside him — "The father pushed through to Jesus and told him the whole story"
3. [n1] the son's lifelong affliction — thrown down, unable to speak, hurt again and again — "thrown down, unable to speak, hurt again and again"
4. [s22] the father's trembling plea — "If thou canst do any thing, have compassion on us, and help us"
5. [j1] Jesus answering the word "if" — "If thou canst believe, all things are possible to him that believeth"
6. [fv1] the father crying out the honest prayer — "Lord, I believe; help thou mine unbelief"
7. [n4] the father laying down both his little faith and his shameful unbelief together — "brought Jesus the little bit of faith he had AND the unbelief he was ashamed of — and laid both of them down"
8. [n5/j2] Jesus, seeing the crowd rush in, commanding the spirit out for good — "come out of him, and enter no more into him"
9. [n6a] the boy going still — so still they whisper he is dead — "the boy went so still that people whispered he was dead"
10. [n6a] Jesus reaching down, taking the boy by the hand, lifting him up, whole — "took him by the hand, and lifted him up — and the boy stood, quiet and whole"
11. [n6b] Jesus giving the son back to his father — the tormented childhood over — "he gave him back to his father"
12. [j3/n7] alone in the house, Jesus telling the disciples why they failed — "This kind can come forth by nothing, but by prayer and fasting"
13. [card] warm hold on father and restored son for the closing card

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n0, n1, n2, n2b, n3, n3b, n4, n5, n5b, n6a, n6b, n7, n7b, card
- **SCRIPTURE** (light blue): s22, fv1  — the father is neither Jesus, God, nor a woman; his verbatim KJV lines are light-blue SCRIPTURE
- **JESUS** (red): j1, j2, j3
- No women speak. Narrator sets scene + retells the KJV lines in modern English.

## The fix
Current 8 stills. Split the father's story (2) from the boy's affliction (3), give
the "if"-plea, Jesus's answer, and the honest prayer their own frames (4, 5, 6),
and split the boy-gone-still (9) from the hand-lifting-him-up (10). Rewire build.py
BEATS so each still switches when its words arrive. Let beat 6 (the honest prayer)
breathe — it is what the whole story is remembered for.

## Deviations from the band
Honest beat read lands at **13**, just under the T3 band (16–24). This is a tight,
single-scene encounter that reads as high-T2 / low-T3. Trusting the beats over the
range (Part 3): 13 stills, no padding.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] fv1 caption is **light-blue** SCRIPTURE (the father), not red
- [ ] Jesus via master ref; the father and boy carry beats 6, 10, 11
- [ ] `bash admin/verify-mp4.sh <mp4> 210` green; frame-verify beats 6, 10, 11

## Length read
Verdict: TRIM to ~195s — cut n4 (narrator explains the moral at length)
n4 ("Think about what he just did... that cracked-open, honest, half-full faith — was enough") re-explains the point n3b just made and the card lands again — the story already showed it in the father's own lifted line.

## Narration read
- Narrator fixes: n4 explains the moral (redundant with n3b and the card) → cut or shrink hard. n7b tail is a mild explanation but it ties the disciples' failure to the father's honesty — keep.
- Scripture lifts: none available — the father's lines (s22, fv1) already lifted to SCRIPTURE/blue and Jesus' j1/j2/j3 red.
- Cast/colour: correct — and the headline fix is right: fv1 "Lord, I believe; help thou mine unbelief" is the father, so SCRIPTURE/blue, not Jesus-red. A quoted man is blue, never red or pink.
