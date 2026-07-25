# PRESCRIPTION — build-17-lazarus

**Row:** 17   **Shelf:** Everyone   **Scripture:** John 11
**Tier:** T3 Full Arc   **Target length:** 120–165s   **Pictures:** 16–24 (planned: 20)

## The impact read
- **The one thing:** he is the resurrection in person — and even knowing he is about to open the grave, he walks all the way into the grief and weeps there first.
- **The turn:** "I am the resurrection, and the life" spoken to Martha on the road (j2) — the whole far-off promise set down in the person standing in front of her. The second hinge is "Lazarus, come forth" (j4).
- **Character shown:** authority over death joined to real tears — he does not skip the grief, he honors it; he refuses to pretend death isn't a horror even when he holds the cure.
- **Whose face carries it:** MARTHA and MARY (the witnesses) — grief on the road, Martha's confession, Mary at his feet; and LAZARUS in the tomb-mouth. "Jesus wept" is shown restrained, via master ref / over-the-shoulder onto the weeping mourners — the power is that they see him weep.
- **The card question falls out of:** "Is there a grief you are carrying that he would not rush you past, but would sit down inside it, and weep there with you first?" — falls straight out of the one thing. No change needed.

## Beat list (= the picture plan) — 20 stills
1. [n0] the Bethany home — Martha, Mary and Lazarus, the one place Jesus could just be a friend; now Lazarus is dying — agrees: "Jesus loved this family... their brother was dying"
2. [w3/n0] the sisters at the sickbed sending word — "Lord, behold, he whom thou lovest is sick"
3. [n1/j1] Jesus receiving the news and, instead of running, staying two more days — "This sickness is not unto death, but for the glory of God"
4. [n2] Bethany later — Lazarus dead and sealed in the tomb four days, the mourners gathered — "sealed in the tomb four days... everyone knew exactly how final four days was"
5. [w21/n3] Martha running out to meet him on the road, grief and faith in one breath — "Lord, if thou hadst been here, my brother had not died. But I know... God will give it thee"
6. [n4] Jesus telling her "your brother will rise again"; Martha's tired, last-day nod — "Martha nodded the way we nod at things we believe but cannot feel"
7. [j2] over Jesus's shoulder onto Martha — "I am the resurrection, and the life... Believest thou this?"
8. [w27] Martha's confession, her face — "Yea, Lord: I believe that thou art the Christ, the Son of God, which should come into the world"
9. [n5/w32] Mary coming and falling at his feet weeping, the mourners weeping with her — "Lord, if thou hadst been here, my brother had not died"
10. [n6] Jesus weeping at the grave of his friend — shown restrained, the mourners watching him — "Jesus wept"
11. [n7/w39] the tomb — a cave with a heavy stone; practical Martha panicking at the stone — "Lord, by this time he stinketh: for he hath been dead four days"
12. [j3] Jesus answering her — "Said I not unto thee, that, if thou wouldest believe, thou shouldest see the glory of God?"
13. [n7b] the great stone leaned back, the dark mouth of the grave open to daylight — "the dark mouth of the grave stood open to the daylight"
14. [n8] Jesus lifting his eyes and praying aloud so the crowd knows where the power comes from — "he lifted his eyes and prayed out loud"
15. [j4] calling into the dark, loud enough to wake the dead — "Lazarus, come forth"
16. [n9] the dead man coming out — bound hand and foot in grave-linen, face wrapped, standing in the tomb-mouth, alive — "Lazarus stood in the mouth of his own tomb — alive"
17. [n9] the crowd frozen — nobody moving, nobody breathing — "Nobody moved. Nobody breathed."
18. [j5] Jesus's word to unwrap the living man — "Loose him, and let him go"
19. [n10] the grave-linen coming off, Lazarus freed to walk home — the sisters reaching for him — "Take the grave-linen off a living man and let him walk home"
20. [n11/card] hold at the open grave for the closing question — the card line

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n0, n1, n1b, n2, n3, n4, n5, n6, n7, n7b, n8, n9, n10, n11/card
- **WOMAN** (pink): w3, w21, w27, w32, w39 — Martha and Mary; the sisters carry this chapter and were all paraphrase before
- **JESUS** (red): j1, j2, j3, j4, j5 — Jesus in the flesh
- No voice from heaven in the passage.

## The fix
The sisters were never heard — five lines are now pink. The picture plan must keep pace with the words: give the road exchange (5–8), Mary at his feet (9), "Jesus wept" (10), the stone (11–13), and the raising sequence (15–19) each its own frame. A single block of paraphrase over a handful of stills skips beats the words plainly paint. Rewire build.py BEATS so each still switches when its words arrive; let beat 10 ("Jesus wept") and beat 16 (Lazarus at the tomb-mouth) hold and breathe.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] Jesus's face restrained at beat 10 (weeping) — the mourners' faces carry it; over-the-shoulder at j4 (beat 15)
- [ ] Lazarus is bound in grave-linen with his face wrapped in beat 16, not already unwrapped
- [ ] `bash admin/verify-mp4.sh <mp4>` green; frame-verify beats 10, 16, 19
