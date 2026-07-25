# PRESCRIPTION — build-56-widow-of-nain

**Row:** 56   **Shelf:** Everyone   **Scripture:** Luke 7:11–17
**Tier:** T2 Encounter   **Length:** 149s (keep — the audio is fine)
**Pictures:** 11 beats (current 9 stills → beats are being skipped)

> No one asked him. The narration moves through the two crowds meeting at the gate,
> the funeral of the only son, the silent grieving mother, Jesus seeing HER, "weep
> not," the touch on the bier, "arise," the son sitting up, the son handed back to
> his mother, and the crowd's holy fear. Eleven moments, carried now on 9.

## The impact read
- **The one thing:** no one asked and no one could fix it — he saw HER, and her
  grief alone moved him to speak life.
- **The turn:** "when the Lord saw her, he had compassion on her... Weep not." The
  story pivots on his seeing an uninvited stranger's sorrow. The hinge is the seeing
  and the touch on the bier.
- **Character shown:** unbidden compassion; he is not put off by death or grief.
- **Whose face carries it:** THE WIDOWED MOTHER — grief, then being seen, then the
  reunion — and the son's face returning to life. Jesus's compassion turned toward
  her, over-the-shoulder; not his face in the raising.
- **The card question falls out of:** "What have you already buried that he is
  asking to raise?" — lands on the one thing. No change needed.

## Beat list (= the picture plan) — 11 stills
1. [n1] Jesus and his crowd approaching the town gate of Nain — agrees: "they reached the town gate and met something coming the other way"
2. [n2] the funeral coming out the gate — the young man on the open bier, the widowed mother walking behind, a crowd with her — "behind him walked his mother, a widow, grieving"
3. [n3] close on the mother's grief — silent, asking nothing, not knowing who he is — "She never asks him for anything... simply walking behind her son's body"
4. [s13a] Jesus seeing her, compassion on his face turned toward her (over-the-shoulder onto her) — "when the Lord saw her, he had compassion on her"
5. [jv13] Jesus speaking to her — "Weep not" — her tear-streaked face lifting — "Weep not"
6. [n4/s14a] Jesus stepping to the bier and touching it — the bearers stopping dead — "he came and touched the bier: and they that bare him stood still"
7. [jv14] Jesus speaking to the dead young man, the procession holding its breath — "Young man, I say unto thee, Arise"
8. [n5] the young man sitting up and beginning to speak — life poured back — "the young man who had been dead sat up, and began to speak"
9. [n6] Jesus taking him by the hand and giving him back to his mother — mother and son reunited — "took him by the hand and gave him back to his mother"
10. [n7/s16] the crowd struck with holy fear, praising God — "a great prophet is risen up among us; and, That God hath visited his people"
11. [card] warm hold on the reunited mother and son for the closing question

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n1, n2, n3, n3b, n4, n4b, n5, n6, n7, n7b, card
- **SCRIPTURE** (light blue): s13a, s14a, s16
- **JESUS** (red): jv13, jv14
- The widow is **silent** in the text — do not invent her a line (SPEAKER-LAW).

## The fix
Current 9 stills. Split seeing-her → "weep not" → touch-the-bier → "arise" (beats
4, 5, 6, 7), and give the son sitting up (8) and the handing-back (9) their own
frames. Rewire build.py BEATS so each still switches when its words arrive. Let
beat 4 (the compassion as he sees her) and beat 9 (the reunion) breathe.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] Jesus's face not the subject in beats 4, 6, 7 (over-the-shoulder onto the mother / bier)
- [ ] `bash admin/verify-mp4.sh <mp4> 149` green; frame-verify beats 4, 8, 9

## Length read
Verdict: KEEP ~149s
Luke 7:11-17 moves beat to beat with no repetition; the widow's silence is named once (n3) as story, not padding.

## Narration read
- Narrator fixes: clean — narrator stays on scene and turn; the meaning is left to the card.
- Scripture lifts: none available — Jesus' "Weep not" (jv13) and "Arise" (jv14) red; Luke's two frames (s13a, s14a) and the town's verdict (s16) already blue.
- Cast/colour: correct — no pink, and rightly so: the widow of Nain speaks no recorded word (SPEAKER-LAW lists her among the silent).
