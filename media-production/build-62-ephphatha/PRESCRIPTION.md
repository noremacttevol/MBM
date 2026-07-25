# PRESCRIPTION — build-62-ephphatha

**Row:** 62   **Shelf:** Everyone   **Scripture:** Mark 7:31–37
**Tier:** T2 Encounter   **Length:** 192s (keep — the audio is fine)
**Pictures:** 10 beats (current 8 stills → beats are being skipped)

> Healed privately, with dignity. The narration moves through the Decapolis now
> welcoming him, the deaf man walled off in silence, Jesus leading him away alone,
> the three gentle sign-language gestures (ears, mouth, heaven), the sigh, the word
> "Ephphatha," everything opening, and the region's verdict. Ten moments, carried
> now on 8.

## The impact read
- **The one thing:** he does not heal for an audience — he takes you aside, meets you
  inside your silence, and speaks in the only language you can receive.
- **The turn:** the sigh before the word, then "Ephphatha" — and everything opens.
  The hinge is that one word landing in a lifetime of silence.
- **Character shown:** dignity and intimacy — he enters the man's silence rather than
  performing over a crowd.
- **Whose face carries it:** THE DEAF MAN — isolation, then the tender private
  gestures read on his face, then sound rushing in. Jesus's hands at the ears and
  mouth; his face at the sigh (allowed, face-locked), but the wonder is the man's.
- **The card question falls out of:** "He takes you aside, meets you in your silence,
  and opens what was shut." — the card is a statement, and it lands. No change.

## Beat list (= the picture plan) — 10 stills
1. [n0] the Decapolis welcoming Jesus now — people running to bring him their broken, where once they asked him to leave — agrees: "Now they come running, bringing him their broken"
2. [n1] the deaf man brought forward — surrounded by people yet walled off, alone in silence — "He was surrounded by people, and utterly alone"
3. [n2] Jesus taking the man by the hand and leading him away from the crowd, just the two of them — "led him away from the crowd — completely alone"
4. [n3] Jesus putting his fingers gently to the man's ears — "I see exactly what is wrong" — "He put his fingers gently to the man's ears"
5. [n3] Jesus touching the man's mouth — and this too — "He touched the man's mouth: and this too"
6. [n3] Jesus looking up to heaven — what comes next is from God — "Then he looked up to heaven"
7. [s34a] Jesus sighing before the word — feeling the weight of a broken world — "he sighed, and saith unto him"
8. [j1/n5] "Ephphatha" — be opened — the man's face as sound rushes in and his tongue loosens — "everything opened. Sound rushed in where there had been a lifetime of nothing"
9. [n6/s37] the region's verdict — "He hath done all things well: he maketh both the deaf to hear, and the dumb to speak"
10. [card] hold on the man hearing and speaking his first words for the closing card

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n0, n1, n2, n3, n4, n5, n6, n6b, n7, card
- **SCRIPTURE** (light blue): s34a, s37
- **JESUS** (red): j1  ("Ephphatha")
- No women speak. Narrator sets scene + retells the KJV lines in modern English.

## The fix
Current 8 stills. Split the sign-language into its three named gestures — ears (4),
mouth (5), heaven (6) — and give the sigh (7) its own frame before the word.
Rewire build.py BEATS so each still switches when its words arrive. Let beat 8
(everything opening) breathe.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] Jesus's hands are the subject in beats 4–5; the man's wonder carries beat 8
- [ ] `bash admin/verify-mp4.sh <mp4> 192` green; frame-verify beats 4, 7, 8

## Length read
Verdict: TRIM to ~180s — cut n7 (explains the moral, duplicates the card)
n7 ("Notice what kind of healer he is... met him inside his silence") says exactly what the card says next ("He does not heal for an audience. He takes you aside..."), so it repeats the meaning the card owns.

## Narration read
- Narrator fixes: n7 explains the moral and pre-says the card → cut or shrink to a one-line bridge.
- Scripture lifts: none available — "Ephphatha" (j1) red; Mark's frame (s34a) and the region's verdict (s37) blue. "that is, Be opened" correctly left as narrator retell in n5.
- Cast/colour: correct. (Separately, the docstring's "Ephphatha" pronunciation flag still needs an audio-pass check — target ep-FA-tha — but that is not a colour issue.)
