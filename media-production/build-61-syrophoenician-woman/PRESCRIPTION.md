# PRESCRIPTION — build-61-syrophoenician-woman

**Row:** 61   **Shelf:** Everyone   **Scripture:** Mark 7:24–30
**Tier:** T2 Encounter   **Length:** 179s (keep — the audio is fine)
**Pictures:** 11 beats (current 9 stills → beats are being skipped)

> She argued with God and won. The narration moves through Jesus hidden in Gentile
> country, the outsider mother hearing of him, her uninvited plea at his feet, the
> household picture ("the children's bread"), the opening she catches, her answer
> about the crumbs, his gladness to lose, "it is done," her walk home on his word
> alone, and finding her daughter whole. Eleven moments, carried now on 9.

## The impact read
- **The one thing:** she refused to believe there was no room for her at his table —
  and there is room for you.
- **The turn:** she steps *into* the picture he painted and answers him — the only
  person in the Gospels to win an exchange with Jesus — and he heals her daughter on
  his word alone, across the distance. The hinge is her answer about the crumbs.
- **Character shown:** he honors stubborn, clear-eyed faith and heals without a
  touch, on his word.
- **Whose face carries it:** THE MOTHER — desperation, then the quick believing
  answer, then the walk home, then finding her daughter well. Jesus's face is allowed
  (face-locked) at the exchange — his gladness to lose it.
- **The card question falls out of:** "There is room for you." — the card is a
  statement here, and it lands on the one thing. No change.

## Beat list (= the picture plan) — 11 stills
1. [n0] Jesus arriving in Gentile country near Tyre, slipping into a house, unable to stay hidden — agrees: "up to the coast around Tyre... He slipped into a house... he could not be hidden"
2. [n1] the Gentile mother hearing he is there — her little girl sick with something dark at home — "her little girl was sick with something dark that no one could fix"
3. [n2] the woman coming in uninvited, falling at his feet, begging for her daughter — "came in uninvited, fell down at his feet, and begged him"
4. [j1] Jesus answering with the household picture — the children's bread, the dogs — "it is not meet to take the children's bread, and to cast it unto the dogs"
5. [n4] close on the woman's face as she catches the opening — the little pups under the family's table — "He had painted a picture of a household — and left her a place in it... She saw it instantly"
6. [w28] the woman stepping into the picture, answering him — "Yes, Lord: yet the dogs under the table eat of the children's crumbs"
7. [n5b] the exchange — the only person to win one with Jesus — his face glad to lose it — "you can almost hear how glad he was to lose it"
8. [j2] Jesus telling her it is already done — "the devil is gone out of thy daughter"
9. [n7] the woman walking home holding nothing but his word — no touch, no visit, just his word across the distance — "That walk home, holding nothing but his word, was the faith he praised"
10. [n8] the mother reaching her door, finding her daughter resting on the bed, quiet and whole — "found her daughter lying on the bed, resting — quiet, and whole"
11. [card] warm hold on mother and healed daughter for the closing card

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n0, n1, n2, n3, n4, n5, n5b, n6, n7, n8, n9, card
- **WOMAN** (pink): w28  — the Syrophoenician mother; pink per SPEAKER-LAW
- **JESUS** (red): j1, j2
- Narrator sets scene + retells the KJV lines in modern English.

## The fix
Current 9 stills. Give her catching-the-opening (5) and the walk-home-on-his-word
(9) their own frames, and split the exchange (6, 7) from the verdict "it is done"
(8). Rewire build.py BEATS so each still switches when its words arrive. Let beat 9
(the walk home) breathe — it is the faith he praised.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] w28 caption is **pink** (WOMAN), not blue
- [ ] `bash admin/verify-mp4.sh <mp4> 179` green; frame-verify beats 5, 9, 10

## Length read
Verdict: KEEP ~179s
Mark 7:24-30 is one tight exchange; n4's long "children's bread / pups under the table" setup is needed to make j1 land, so it stays.

## Narration read
- Narrator fixes: n5b breaks tone with a modern aside ("Bible students love this moment: it is the only time in the gospels anyone wins an exchange with Jesus") → rephrase plain and reverent, or trim to "and you can almost hear how glad he was to lose it."
- Scripture lifts: none available — her reply (w28) already lifted to WOMAN/pink; Jesus' j1/j2 red. Her Matthew 15:22 cry is not in Mark, correctly left out.
- Cast/colour: correct — WOMAN/pink present on the line the whole build turns on.
