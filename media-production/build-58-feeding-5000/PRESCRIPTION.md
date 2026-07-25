# PRESCRIPTION — build-58-feeding-5000

**Row:** 58   **Shelf:** Everyone   **Scripture:** John 6:1–14
**Tier:** T3 Full Arc   **Length:** 156s (keep — the audio is fine)
**Pictures:** 14 beats (current 9 stills → beats are being skipped)

> The narration moves through the hillside crowd, the fading light, Philip's test,
> Andrew and the boy, the tiny barley lunch, the crowd sitting on the grass, the
> blessing and breaking, the food multiplying, the crowd eating full, "gather the
> fragments," the twelve baskets, and the crowd's amazement. Fourteen moments,
> carried now on 9.

## The impact read
- **The one thing:** he takes the little you're embarrassed to offer, gives thanks
  for it, breaks it, and it somehow becomes more than enough — with baskets to spare.
- **The turn:** the boy's cheap barley lunch placed in Jesus's hands → the loaves
  lifted to heaven, blessed, broken. That is the hinge.
- **Character shown:** he multiplies the small and wastes nothing ("that nothing be lost").
- **Whose face carries it:** THE BOY offering the embarrassing little lunch, and the
  crowd's wonder. Jesus's hands at the breaking, over-the-shoulder — not his face.
- **The card question falls out of:** "What small thing is he asking you to place in
  his hands?" — lands on the one thing. No change needed.

## Beat list (= the picture plan) — 14 stills
1. [n1] the huge crowd on the green hillside by the lake, Jesus teaching and healing them through the day — agrees: "He taught them and cared for them all day"
2. [n1] the sun sinking, the crowd far from any town or food — "the sun began to sink and they were a long way from any town or food"
3. [n2] the disciples anxious in the fading light; Jesus turning to Philip — "His disciples grew anxious as the light went"
4. [j5] Jesus asking Philip, gesturing at the oncoming crowd — "Whence shall we buy bread, that these may eat?"
5. [n3/s9] Andrew bringing the boy forward, almost embarrassed; the five loaves and two fish — "There is a lad here, which hath five barley loaves, and two small fishes"
6. [n3b] close on the small barley lunch — the cheapest food on that whole hillside — "the smallest, cheapest lunch on that whole hillside"
7. [j10/n4b] Jesus: "Make the men sit down"; the crowd settling in groups on the green grass — "settled in groups on the green grass"
8. [nbless] Jesus taking the loaves and fish, looking up to heaven, giving thanks, breaking the bread (hands + bread) — "looking up to heaven, he gave thanks, and broke the bread"
9. [n5] the disciples carrying the food out, and it keeps coming — more and more — "it kept coming, bread and fish, more and more"
10. [n5] the whole crowd eating, every person full — "every single person there had eaten as much as they wanted, and was full"
11. [jv12] "Gather up the fragments" — disciples gathering the leftovers — "Gather up the fragments that remain, that nothing be lost"
12. [n6] the twelve baskets filled with broken pieces — more than they started with — "filled twelve baskets with the broken pieces"
13. [n7/s14] the crowd amazed, naming him the prophet — "This is of a truth that prophet that should come into the world"
14. [card] warm hold on the boy's lunch beside the twelve full baskets for the closing question

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n1, n2, n2b, n3, n3b, n4, n4b, nbless, n5, n6, n7, n7b, card
- **SCRIPTURE** (light blue): s9, s14
- **JESUS** (red): j5, j10, jv12
- No women speak. Narrator sets scene + retells the KJV lines in modern English.

## The fix
Current 9 stills. Split the anxious-light vs sun-sinking (2, 3), the boy vs the
close-up on the tiny lunch (5, 6), and the food-multiplying vs the crowd-eating-full
(9, 10). Rewire build.py BEATS so each still switches when its words arrive. Let
beat 8 (the blessing and breaking) breathe.

## Deviations from the band
Honest beat read lands at **14**, just under the T3 band (16–24). This miracle is
one sustained action with few visual turns — it reads at the top of T2 / low T3.
Trusting the beats over the range (Part 3): 14 stills, no padding.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] Jesus's face not the subject at beat 8 (hands + bread, over-the-shoulder)
- [ ] `bash admin/verify-mp4.sh <mp4> 156` green; frame-verify beats 6, 8, 12
