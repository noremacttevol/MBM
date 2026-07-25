# PRESCRIPTION — build-59-feeding-4000

**Row:** 59   **Shelf:** Everyone   **Scripture:** Mark 8:1–9
**Tier:** T2 Encounter   **Length:** 165s (keep — the audio is fine)
**Pictures:** 12 beats (current 9 stills → beats are being skipped)

> "I have compassion" — again. The narration moves through the three-day crowd with
> nothing left to eat, Jesus noticing before anyone asks, his worry they'll faint on
> the road, the disciples' bafflement, "how many loaves," "seven," the small pile,
> the blessing and breaking, the crowd fed full, the seven baskets, and the crowd
> sent home cared for. Twelve moments, carried now on 9.

## The impact read
- **The one thing:** he notices what everyone else overlooks — that you're tired,
  empty, and a long way from home — and no one had to ask him.
- **The turn:** unprompted, "I have compassion on the multitude." He is the one who
  notices. The hinge is his noticing, then the breaking of the seven loaves.
- **Character shown:** compassion that anticipates the ordinary need — he cares that
  they'd faint on the road, not only about their souls.
- **Whose face carries it:** the TIRED CROWD and the disciples' bafflement. Jesus's
  compassion is in his own quoted words (red); his hands at the breaking.
- **The card question falls out of:** "What ordinary need are you afraid is too small
  to bring to him?" — lands on the one thing. No change needed.

## Beat list (= the picture plan) — 12 stills
1. [n1] the huge crowd in a remote, rugged place, three days with Jesus, worn and hungry — agrees: "with him three whole days... their food was completely gone"
2. [jv2] Jesus calling his disciples over, telling them he has compassion on the crowd — "I have compassion on the multitude... three days, and have nothing to eat"
3. [j3/n1b] Jesus concerned they'll faint on the road home — some came from far — "they will faint by the way: for divers of them came from far"
4. [n2/s4] the disciples baffled, gesturing at the empty wilderness — "From whence can a man satisfy these men with bread here in the wilderness?"
5. [n2b] the disciples doing the arithmetic in the wilderness — with the man who already fed 5000 in front of them — "standing in a wilderness doing the arithmetic"
6. [j5/s5] Jesus asking "How many loaves have ye?"; the disciples answering "Seven" — the seven loaves and a few fish held up — "How many loaves have ye? ... Seven"
7. [n3b] close on the small pile — seven loaves and a few fish, almost nothing — "It was almost nothing against so great a need"
8. [nbless] the crowd sitting on the ground; Jesus taking the seven loaves, giving thanks, breaking them, handing to the disciples (hands + bread) — "took the seven loaves, and gave thanks, and broke them"
9. [n4] the disciples carrying bread and fish through the whole multitude, everyone eating their fill — "everyone ate until they were completely satisfied"
10. [n5] the seven large baskets of leftovers — far more than the start — "filled seven large baskets with the broken pieces"
11. [n6] the crowd — about four thousand — heading home full and cared for — "every single one of them went home full"
12. [card] warm hold on the seven small loaves / the fed crowd for the closing question

## Speaker map (matches SPEAKER-LAW — do not disturb)
- **NARRATOR** (white): n1, n1b, n2, n2b, n3, n3b, nbless, n4, n5, n6, n7, card
- **SCRIPTURE** (light blue): s4, s5
- **JESUS** (red): jv2, j3, j5
- No women speak. Narrator sets scene + retells the KJV lines in modern English.

## The fix
Current 9 stills. Split the compassion vs faint-on-the-road (2, 3), the bafflement
vs the arithmetic (4, 5), and give the close-up on the small pile (7) its own frame.
Rewire build.py BEATS so each still switches when its words arrive. Let beat 8 (the
blessing and breaking) breathe.

## Self-check before the board
- [ ] every beat the words paint has its own frame; nowhere do the words move on while the picture stays behind
- [ ] each still agrees with its line (direction/position/scale/emotion/likeness)
- [ ] Jesus's face not the subject at beat 8 (hands + bread, over-the-shoulder)
- [ ] `bash admin/verify-mp4.sh <mp4> 165` green; frame-verify beats 7, 8, 10

## Length read
Verdict: KEEP ~164s
Mark 8:1-9 runs tight; the j5 -> s5 "How many loaves have ye?" / "Seven." exchange is intentionally back-to-back and earns its place.

## Narration read
- Narrator fixes: n7 leans lightly on the moral ("That is simply who he is") — a one-line trim if needed; the card already carries it. Otherwise clean.
- Scripture lifts: none available — jv2/j3/j5 red; the disciples' s4 and the one-word s5 ("Seven") already blue.
- Cast/colour: correct.
