# BUILD STATUS — #44 The Two Debtors (luke-7_two-debtors)

**BUILT — awaiting Cameron — 2026-07-14 — Computer B (Elli's Windows laptop, operator Leighton).**

Luke 7:36-50 — the parable of the two debtors (vv. 41-43), told at Simon the
Pharisee's table while the forgiven woman anoints Jesus's feet. Milk framing:
*forgiven much → loves much.* The size of her love is the size of the debt she
knows was torn up; the danger in Simon's seat is thinking you owed too little to
bother. Ends on invitation.

## Result
- `luke-7_two-debtors.mp4` — 1080x1920 H.264 + AAC, **20.1 MB, 4:18 (258.2s)**, ~-15 LUFS.
- STILLS-ONLY (Law E): 8 painted stills, slow Ken Burns drift, no motion clips.

## The old-faithful path (Google Flow, $0)
All 8 stills generated in Google Flow (Nano Banana 2, 9:16) via Chrome, downloaded
at **2K (1536x2752)**, renamed into `assets/`. No paid API. Two stills came back as
comic-strip triptychs (s3) — the single-scene variation was used instead.

## Face Law (the #1 law) — PASS
Jesus is physically at the dinner, so he is the hard case. `jesus_face_gate.py
--dir build-44-two-debtors` exits 0. He is staged ONLY from behind (s1, s3, s4),
over-the-shoulder (s7) or small-and-distant through a doorway (s8) — his face is
never shown, **verified on the rendered frames** (t=6 s1, t=40 s3, t=172 s7). The
parable (s5 the two debtors, s6 the debts torn up) has NO Jesus figure at all —
the creditor is an ordinary moneylender, faces shown.

## Stills (assets/)
1. s1-the-invitation — Jesus reclines at Simon's evening table, seen from behind.
2. s2-the-woman-comes — the woman with the alabaster jar in the lamplit doorway.
3. s3-at-his-feet — she weeps at his feet, wiping them with her hair (Jesus behind).
4. s4-simon-judges — Simon's cold, silent judgment (Jesus's back in foreground).
5. s5-the-two-debtors — parable: the moneylender + two debtors who cannot pay.
6. s6-frankly-forgave — parable: he tears up both debts (THE VERDICT beat).
7. s7-she-loved-much — Jesus presents her to Simon (over-the-shoulder; THE PAYOFF).
8. s8-go-in-peace — she walks out saved into first-light morning.

## Narration & music
- Narrator en-US-AndrewNeural; Jesus en-US-ChristopherNeural (exact KJV only).
- 5 KJV lines cream-italic: j1 (7:40), j2 (7:41), j3 (7:42 verdict), j4 (7:47
  payoff), j5 (7:50 "go in peace").
- Verbatim captions (every spoken word), white serif / cream-italic for KJV.
- **Two sacred silences** — music dies to true silence under j3 (the verdict) and
  j4 (the payoff), then returns.
- **No-Dead-Air:** worst spoken gap 1.88s (law: ≤ 2.5s), enforced by build.py raise.

## Reproduce
`python make_narration.py` → `python build.py` (Windows: ffmpeg on PATH, Georgia
fonts). Stills already in `assets/`.
