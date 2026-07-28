# PRESCRIPTION — build-63-man-born-blind

**Row:** 63   **Shelf:** Everyone   **Scripture:** John 9
**Tier:** T3 Full Arc   **Length:** 241s (keep — the audio carries a long, real drama)
**Pictures:** ~18 moments (current 10 → the words go to places the pictures don't)

> Read the narration and the story goes: the roadside beggar → the disciples' blame
> question → Jesus throwing out the equation → kneeling to knead clay → spreading it
> on the eyes → the blind walk across Jerusalem → the wash → the first sight of light
> → the neighbors' argument → the interrogation → his great answer → cast out → Jesus
> going to FIND him → the searching question → seeing his healer's face → "Lord, I
> believe." Ten stills can't hold that. Each moment below is its own frame. A couple
> — the first sight, the recognition — should hold and breathe; that's not the problem,
> the skipped moments are.

## The impact read
- **The one thing:** suffering isn't a punishment to be explained — and when the
  world shuts you out, he comes and finds you.
- **The turn:** "Thou hast both seen him, and it is he that talketh with thee" — the
  first face this man ever truly studied is the face of the one who gave him eyes.
- **Character shown / wound answered:** God refuses the blame-math ("who sinned?").
  Answers the "you're being punished / God is angry at me" wound even on the Everyone
  shelf.
- **Whose face carries it:** the BLIND MAN throughout — his face at first sight, his
  defiance before the leaders, his recognition. Jesus's face only at beat 15 (the
  man finally seeing him), and even there shoot over Jesus's shoulder onto the man's
  wonder.
- **The card question falls out of:** "when the world shuts you out, he comes and
  finds you." No change needed.

## Beat list (= the picture plan) — ~18 stills
1. [n0] the blind man begging at the roadside; Jesus and disciples approaching — "as Jesus and his disciples passed by"
2. [s2] the disciples gesturing at him, debating — "who did sin, this man, or his parents"
3. [n0b/n1] the man's face while he is talked ABOUT, eyes clouded — "the question everyone assumed had an answer"
4. [j1] Jesus answering, looking at the man (over-shoulder) — "that the works of God should be made manifest"
5. [n2] Jesus kneeling, kneading clay in the dust of the ground — "made soft clay with the dust of the ground"
6. [n2/n3] Jesus's hands spreading the clay over the blind eyes — "gently spread it over the blind man's eyes"
7. [j2] Jesus directing him, the man listening, mud on his eyes — "Go, wash in the pool of Siloam"
8. [n4] the man walking blind across Jerusalem, hands out along a wall — "feeling his way... one wall and one step at a time"
9. [n5] the man kneeling at the pool, washing the clay away — "he knelt at the pool of Siloam and washed"
10. [n5] FIRST SIGHT — light pouring in, staring at his own two hands (his face, let it breathe) — "the first things he ever saw"
11. [n6] the neighbors crowding, arguing whether it's even him — "the neighbors argued about whether he was even the same man"
12. [n6] the interrogation — religious leaders questioning him, pressing — "hauled him in for questioning"
13. [s25/n6b] the man standing firm before them, plain and unshaken — "one thing I know... now I see"
14. [n7] the man thrown out, the synagogue doors behind him, alone — "cast out of the synagogue"
15. [n7/j3] Jesus finding the outcast, coming to him (over Jesus's shoulder, man's face) — "he went and FOUND him"
16. [n8/s36] the man's face searching, asking for the name — "Who is he, Lord, that I might believe"
17. [j4/n9] RECOGNITION — the man truly seeing his healer's face for the first time — "it is he that talketh with thee"
18. [s38/n9b/card] the man believing, face to face; warm hold for the closing question — "Lord, I believe"

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n0, n0b, n1, n2, n3, n4, n5, n6, n6b, n7, n8, n8b, n9, n9b, card
- **SCRIPTURE** (light blue): s2, s25, s36, s38
- **JESUS** (red): j1, j2, j3, j4
- No women speak in this cut. Narrator sets scene + names turns; the card carries the point.

## The fix
Add frames at the split moments the current cut collapses: clay knead vs spread (5,6);
the blind walk as its own frame (8); wash vs first-sight (9,10); neighbors vs
interrogation (11,12); cast-out vs found (14,15); searching vs recognition (16,17).
Rewire build.py BEATS so each switches when its words arrive. Let 10 (first sight) and
17 (recognition) hold longer than the rest — pace to the story.

## Self-check before the board
- [ ] every moment the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] Jesus's face shown only at beat 15/17, over-the-shoulder onto the man's face
- [ ] `bash admin/verify-mp4.sh <mp4> 241` green; frame-verify beats 10, 15, 17

## Length read
Verdict: TRIM to ~225s — cut the modern aside in n1 ("People still run that math on themselves today")
John 9 is a real multi-scene chapter (healing, two interrogations, the casting-out, Jesus finding him), so the length is mostly earned; the trim is the handful of present-day asides that step outside the scene, not any story beat.

## Narration read
- Narrator fixes: n1 "People still run that math on themselves today" → cut (modern editorializing). Rest stays on scene and turn.
- Scripture lifts: none available — the blind man's three lines (s25, s36, s38) and the disciples' question (s2) already blue; j1-j4 red.
- Cast/colour: correct — the parents answer jointly in John 9:20-21, so no single line is the mother's; no pink is right.
