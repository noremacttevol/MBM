# BLITZ-40 (Cameron, 2026-07-16): 40 videos at one-per-10-minutes — by splitting the clock

Flow's measured ceiling (~20 gens/hr/session) makes live 10-minute cadence impossible.
So: BANK the art first, BLITZ the assembly after. Laws unchanged (orders/protocol).

## Phase 1 — FILL THE BANK (starts now, runs until 40 folders are art-complete)
- L1/L2 (and Hermes via DRAFTS/): write prompt sheets + narration for the next 40
  unbuilt rows — take rows 151–200 FIRST (verse videos: simplest art, fewest faces),
  then continue by number. Gate each sheet, drop STILLS-WANTED, push, keep going.
  Do NOT wait for art — sheet after sheet.
- W1/W2: farm every marker at CAPTCHA-safe pace (~1 gen/2min sustained; spend credits
  on Pro for first-try quality). Push jpegs, delete marker, next.
- Bank target: 40 folders with full assets/. Track: folders with assets complete and
  no mp4 = the bank.

## Phase 2 — THE 400-MINUTE BLITZ (when the bank holds 40)
- L1 takes banked folders lowest-number-first; L2 highest-number-first (no collisions).
- Per folder: QC stills (face-match, anatomy, no baked text) → make_narration.py if
  audio missing → build.py → tick Built → TITLES → gen_site_index.py → push. Target
  ≤20 min per video per machine; two machines = one published video every ~10 min.
- No new prompt-writing during the blitz. Fix-queue rows count toward the 40.
- Every 4 videos: audit + fresh session (hygiene law holds even in a blitz).
