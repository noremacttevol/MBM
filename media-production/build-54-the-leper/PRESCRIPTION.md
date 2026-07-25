# PRESCRIPTION — build-54-the-leper

**Row:** 54   **Shelf:** Everyone   **Scripture:** Mark 1:40–45
**Tier:** T2 Encounter   **Length:** 145s (keep — the audio is fine)
**Pictures:** 12 beats (current 9 stills → beats are being skipped)

> The story of a touch. The narration moves through the leper's lonely life, his
> forbidden approach, the plea about the *will*, Jesus's reach, the touch itself,
> the skin made new, the instruction to the priest, and the news running ahead.
> Each is its own moment. Twelve frames, carried now on 9.

## The impact read
- **The one thing:** no one is too unclean or too far gone for him to reach and
  touch — "I will" answers the fear that he wouldn't even want to bother.
- **The turn:** the reach and "I will; be thou clean." He touches *before* the
  healing — the untouchable is touched first. That is the hinge.
- **Character shown:** compassion that closes distance — his hand goes toward the
  one thing everyone else steps back from.
- **Whose face carries it:** THE LEPER — shame and the wondering about the will,
  then wonder, then freedom. Jesus's hand at the touch; his face not the subject.
- **The card question falls out of:** "What would you ask him to make clean?" —
  lands on the one thing. No change needed.

## Beat list (= the picture plan) — 12 stills
1. [n1] the leper alone and apart, wasted skin, people drawing back as he cries out — agrees: "made to cry out 'unclean' if anyone drew near... had not felt a kind hand in years"
2. [n2] the leper breaking the rule — coming close, falling on his knees before Jesus, begging — "he came close. He fell on his knees and begged him"
3. [s40] close on the leper's face pleading, the wondering about the will — "If thou wilt, thou canst make me clean"
4. [n3] Jesus reaching out his hand toward the man everyone stepped back from — the reach, before contact — "He reached out his hand toward the very thing no one would touch"
5. [s41a/jv41] Jesus's hand touching the leper (hand + the leper's stunned face) — "put forth his hand, and touched him... I will; be thou clean"
6. [n4] the moment of change — the untouchable touched, the leprosy leaving — "the untouchable man was touched; and then, at once, the leprosy left him"
7. [n5] the leper's skin made new, warm and whole like a child's — his face realizing he can go home — "his skin was warm and whole again, like the skin of a young child"
8. [n6/j44] Jesus speaking the strict instruction, the man listening — "See thou say nothing to any man: but go thy way, shew thyself to the priest"
9. [n6b] the cleansed man before the priest, making the offering Moses commanded, given his life back — "go and show yourself to the priest, and make the offering Moses commanded"
10. [n7] the man unable to hold it in, telling everyone joyfully, everywhere — "He went out and told everyone, freely, everywhere"
11. [n8] the news running ahead of him, people coming to him from every direction — "people came to him from every direction, out of every corner of the land"
12. [card] warm hold on the reached-out hand / the healed man for the closing question

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n1, n2, n2b, n3, n4, n5, n6, n6b, n7, n8, card
- **SCRIPTURE** (light blue): s40, s41a
- **JESUS** (red): jv41, j44
- No women speak. Narrator sets scene + retells the KJV lines in modern English.

## The fix
Current 9 stills. Split the collapsed reach → touch → change (beats 4, 5, 6) and
add the priest/offering frame (9) and the news-running-ahead frame (11). Rewire
build.py BEATS so each still switches when its words arrive. Let the reach (4) and
the touch (5) breathe — that pause is the whole point.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] Jesus's face not the subject at beat 5 (hand + leper's face)
- [ ] `bash admin/verify-mp4.sh <mp4> 145` green; frame-verify beats 4, 5, 6
