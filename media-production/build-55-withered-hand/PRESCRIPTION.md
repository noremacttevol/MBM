# PRESCRIPTION — build-55-withered-hand

**Row:** 55   **Shelf:** Everyone   **Scripture:** Mark 3:1–6
**Tier:** T2 Encounter   **Length:** 147s (keep — the audio is fine)
**Pictures:** 12 beats (current 9 stills → beats are being skipped)

> A healing done in church, in the open, against the rules and the watchers. The
> narration moves through the withered hand, the leaders lying in wait, "stand
> forth," the man moved to the center, the unanswerable question, the silence, the
> angry-grieved look, "stretch forth thine hand," the hand coming alive, and the
> leaders storming out to plot. Twelve moments, carried now on 9.

## The impact read
- **The one thing:** he will always move toward the suffering person, past every
  rule ever used to shut them out — mercy is the whole reason for the sabbath.
- **The turn:** "Stand forth" — he pulls the overlooked man into the middle of the
  room, refusing to hide the moment, then "Stretch forth thine hand." The hinge is
  the man in the center reaching out the hand he cannot use.
- **Character shown:** courage joined to mercy; anger at hard hearts, tenderness
  toward the man.
- **Whose face carries it:** THE MAN — years of shame, then being centered, then the
  hand coming alive. The angry-grieved look is Jesus's; shoot it over-the-shoulder
  onto the leaders' hard faces.
- **The card question falls out of:** "Will you stretch out the very thing you
  thought was beyond help?" — lands on the one thing. No change needed.

## Beat list (= the picture plan) — 12 stills
1. [n1] the man with the withered hand in the synagogue crowd, cradling the shrunken hand, ashamed — agrees: "a man whose hand was withered, shrunken and useless"
2. [n2] the religious leaders watching Jesus, waiting to catch him healing — "hoping to catch him breaking the law, so they could accuse him"
3. [n3/j3] Jesus calling the man out — "Stand forth" — the man beginning to rise from the crowd — "Stand forth"
4. [n3b] the man moved to the center of the floor, every eye on the one they'd looked past — "moved to the center of the floor"
5. [jv4] Jesus turning the question on the silent leaders — "Is it lawful to do good on the sabbath days... to save life, or to kill?"
6. [n4] the leaders silent, no answer, hard faces — "they said nothing at all"
7. [s5a] Jesus's look sweeping the room — anger, grief at their hard hearts (over-shoulder onto the leaders) — "looked round about on them with anger, being grieved for the hardness of their hearts"
8. [jv5/n4b] Jesus turning from them to the man — "Stretch forth thine hand"
9. [n5] the man stretching out the useless hand — and it made whole as he reaches, strong like the other — "as he reached, it was made whole, restored, strong and alive again"
10. [n6] the leaders storming out, furious, already plotting to destroy him — "They walked out and began... to plot together how they might destroy him"
11. [n7] Jesus with the healed man — he always moves toward the person; the man flexing his restored hand — "He will always move toward the person"
12. [card] hold on the restored hand / the man for the closing question

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n1, n2, n3, n3b, n4, n4b, n5, n6, n7, card
- **SCRIPTURE** (light blue): s5a
- **JESUS** (red): j3, jv4, jv5
- No women speak. Narrator sets scene + retells the KJV lines in modern English.

## The fix
Current 9 stills. Split the question → silence → angry-grieved look → command
(beats 5, 6, 7, 8) and give the man-moved-to-center its own frame (4). Rewire
build.py BEATS so each still switches when its words arrive. Let beat 9 (the hand
coming alive as he reaches) breathe.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] beat 7 shot over Jesus's shoulder onto the leaders' hard faces, not on his face
- [ ] `bash admin/verify-mp4.sh <mp4> 147` green; frame-verify beats 4, 7, 9

## Length read
Verdict: TRIM to ~140s — cut n7 (narrator explains the moral)
n7 ("Mercy, to him, was never a breaking of the sabbath; it was the whole reason for it") tells the viewer the meaning the story just showed, and the card lands the same point — dead weight against Part A.

## Narration read
- Narrator fixes: n7 explains the moral ("He will always move toward the person... mercy was the whole reason for it") → cut or shrink to a one-line bridge; the card carries it.
- Scripture lifts: none available — j3 "Stand forth", jv4 and jv5 are all red already; Mark's anger/grief frame is s5a/blue.
- Cast/colour: correct.
