# QC / RUNNER HANDOFF — build-91-gethsemane

Complaint-gate addendum, 2026-08-05 (Machine A).

## OPEN CAMERON COMPLAINT — gates before build

"The pictures of the disciples did not stay the same. One grew a
beard with in seconds."
BEARD BOARD (rubric lesson 13) + face continuity: each of the three
(Peter, James, John) keeps his exact face AND beard in every frame —
step through frame by frame checking only beards, then only faces.
One beard appearing/disappearing between consecutive frames =
reject.

---

## RUNNER RESULT — A-auto Machine A (`Dev`), 2026-08-06 — SHIPPED V2 REALISTIC

40 painted stills @ native 2K, Luke 22:39-46 Gethsemane, night olive garden throughout.
AUDIO LOCK PASS SHA256=8b6bdf7a615201a736f321f7bf8f9f1e49650d0f4d2a01e5d02da226b35fa0dc
(V1 audio byte-identical; nothing re-voiced). 240.8s, 20.7 MB. luke-22_gethsemane.mp4.
Pre-flight buildable: |total−V1mp4|=0.47s ≤1.0, newer_mp3s=0.

### COMPLAINT LEDGER
- OPEN: "The pictures of the disciples did not stay the same. One grew a beard
  within seconds." → **FIXED.** Ran the dedicated BEARD BOARD (rubric lesson 13)
  across every multi-disciple frame (s07, s10, s11, s13, s26, s28, s30, s32,
  s39): Peter and James carry a FULL DARK beard in every frame they appear in;
  John stays the YOUNG light-stubble disciple in every frame; no beard
  appears / disappears / changes length on the same person between consecutive
  frames. All disciple beats generated with the CAST-REF face locks attached
  (gen log: [+char ref PETER:front/quarter, JAMES-Z:front/quarter, JOHN] on the
  group beats). Jesus one locked face + full dark beard + shoulder-length wavy
  hair identical in all 40 incl. the s35 close-up; only-Jesus-in-cream holds
  (disciples in grey/brown/blue; the Luke 22:43 angel is luminous pale, visually
  distinct, not a second cream human). Scale gate (lesson 14) passes — Jesus is
  ordinary-sized beside the disciples in s07/s11/s13/s39, no giant.

### FIX-WAVE (author beat-text, NOT a runner reroll)
- **s10 "he did not hide it"** renders a DAYLIT INTERIOR ROOM (bright window,
  indoor mud-brick) — mismatches the night olive-garden of the other 39 frames
  (TIME-OF-DAY + place). Confirmed BEAT-AUTHORED, not a fluke: a reroll
  (`--only b10 --redo`) reproduced the interior, so the beat's own must_show
  drives it. Runner may not edit beat text (hard rail). Kept the better of the
  two takes (Jesus with a visible tear = openly showing his sorrow, fits the
  narration; only-Jesus-in-cream; period objects; clean anatomy).
  AUTHOR FIX: rewrite beat b10 must_show to the night olive grove (Jesus showing
  his sorrow to the three under the trees, moonlight), then `--only b10 --redo`.

### COST
Row spend: portraits $0.13 (ANGEL) + 40 stills $5.36 + 1 reroll $0.13 = **$5.62**
(under the $6.10 running average — trend DOWN). Rerolls: 1/40 = **2.5%** (budget 15%).
