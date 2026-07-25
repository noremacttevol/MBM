# PRESCRIPTION — build-57-jairus-daughter

**Row:** 57   **Shelf:** Everyone   **Scripture:** Mark 5:21–43 (Luke 8 parallel)
**Tier:** T3 Full Arc   **Length:** 164s (keep — the audio is fine)
**Pictures:** ~21 beats (current ~10 → **beats are being skipped, not held too long**)

> This is the audit's #1 offender and the worked example for STORY-BLUEPRINT-SYSTEM.md.
> It's not that the stills sit "too long" — it's that the narration keeps moving to
> new things the picture never shows. The words walk through the plea, the death news,
> "only believe," the mourners' scorn, "talitha cumi," the girl rising, the girl
> walking, the parents' wonder, "give her something to eat" — each a new moment a
> listener pictures — while ~10 stills carry it. Read the story and it's ~21 distinct
> moments. Below is every one, so each gets its frame. (If a single frame — the held
> quiet before "arise," say — wants to breathe long, let it; that's not the problem here.)

## The impact read
- **The one thing:** he is never too late — he walks into the room the world has
  already given up on, and speaks life.
- **The turn:** the messengers on the road — "thy daughter is dead" → "Be not afraid,
  only believe." The story pivots from *hurry* to *trust*. That exchange is the hinge.
- **Character shown:** authority over death, joined to tenderness — his first thought
  after raising her is that a growing girl is hungry ("give her something to eat").
- **Whose face carries it:** JAIRUS through the first half (plea → grief → choosing to
  keep believing), then the PARENTS at the raising. Never Jesus's face in the grief or
  raising beats — over-the-shoulder / hand only.
- **The card question falls out of:** "What have you decided is finally too far gone
  for him?" — lands directly on the one thing. No change needed.

## Beat list (= the picture plan) — 21 stills
1. [n1] Jairus pushing through the packed crowd — agrees: "pushed through the crowd"
2. [n1] Jairus fallen at Jesus' feet, face desperate — "fell down at Jesus' feet"
3. [s23] close on Jairus's face pleading (his face carries it) — "come and lay thy hands on her"
4. [n1b] cutaway: the girl at home on a mat, mother beside her, fading — "slipping away at home"
5. [n2] Jesus and Jairus moving through the pressing crowd, father leading — "hurried toward the house, the father leading"
6. [n3] messengers intercepting on the road, grave faces — "messengers came from the house"
7. [s35] the messenger speaking; Jairus's face beginning to break — "Thy daughter is dead"
8. [n3b] Jairus's face breaking, grief in the road (THE HINGE, his face) — "Jairus' heart broke in the middle of the road"
9. [jv36] Jesus's hand steadying Jairus, over-the-shoulder on Jairus receiving it — "Be not afraid, only believe"
10. [n3c] Jairus lifting his eyes, choosing to keep walking — "he should not stop trusting him now"
11. [n4] the house: mourners weeping and wailing loudly — "the mourning had already begun"
12. [j39] Jesus speaking to the loud room, mourners turning — "the damsel is not dead, but sleepeth"
13. [n4b] mourners laughing / scoffing, faces mocking — "they laughed at him"
14. [n5] Jesus putting the crowd out, mourners being sent from the door — "He put them all outside"
15. [n5] the small group entering the quiet inner room, the girl lying small and still — "went in quietly to where the child was lying"
16. [jtal/jv41] Jesus kneeling, taking the girl's hand, speaking (hand + her face, not his) — "Talitha cumi… Damsel, arise"
17. [n6] the girl's eyes opening, first breath — "immediately she got up"
18. [n6] the girl standing / beginning to walk — "and began to walk"
19. [n6] the parents' faces — overwhelmed wonder, reaching for her — "her parents were beside themselves with wonder"
20. [n7] the tender ordinary moment: food brought, parents watching her eat — "give her something to eat"
21. [card] warm hold on the reunited family for the closing question — the card line

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n1, n1b, n2, n3, n3b, n3c, n4, n4b, n5, n6, n7, card
- **SCRIPTURE** (light blue): s23, s35, s41i
- **JESUS** (red): jv36, j39, jtal, jv41
- No women speak in this cut. Narrator only sets scene + names the turn; the card
  carries the meaning (Part 4 rule).

## The fix
Add the missing frames at beats 4, 6, 8, 10, 13, 14, 17, 18, 19, 20 and split the
crowd/road stretch — the story goes to those places and the pictures currently don't.
Not re-timing audio. Rewire build.py BEATS so each still switches at the moment its
words arrive. Some frames (the entry into the quiet room, the held breath before
"arise") should hold longer than others on purpose — pace to the story, not a clock.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] Jesus's face never shown in beats 8, 9, 16 (over-the-shoulder / hand)
- [ ] `bash admin/verify-mp4.sh <mp4> 164` green; frame-verify beats 8, 16, 19

## Length read
Verdict: KEEP ~164s
The existing prescription fixes this build by adding frames, not by re-timing audio; the narration itself walks the plea, the death-news, "only believe," the mourners, "talitha cumi" and the raising with no dead stretch.

## Narration read
- Narrator fixes: clean; n7's "the small things mattered to him too" is a one-clause tender read, not a moral lecture — keep.
- Scripture lifts: none available — Jairus (s23), the messengers (s35) and Mark's "being interpreted" (s41i) are blue; jv36, j39, jtal, jv41 red. All lifted.
- Cast/colour: correct — no pink; the mother and the girl say nothing in Mark 5.
