## 2026-07-21 (later) — TIMING/HEALTH SWEEP ROUND 2: re-render batch checked, 2 fixes, source hardened

Commit: (this commit). Audit: media-production/AUDITS/TIMING-HEALTH-SWEEP-2026-07-21.md

- The narration re-render batch rebuilt **144 of the 200** videos after round 1,
  invalidating those measurements and UNDOING the #70 size fix. Re-measured all 144.
- Only 2 failed, both fixed + shipped + on origin (ship-fixes run by hand):
  **#70** back to 28.5MB (build.py budgets 29.0MB, not 25 — it obeyed its own rule)
  -> re-encoded to 23.5MB; **#149** at -19.2 LUFS (the gain clamp min(10.0,...)
  cannot reach -15 from a -29 LUFS raw mix) -> re-normalized to -14.5.
- **Fixed at SOURCE so re-renders cannot undo it again (466f9f5f):** 102 build.py
  size budgets 29.0/29.5MB -> 24.0 (for 101 it is only a peak cap = no quality
  change; #70 alone used it as a hard 2-pass target); 201 build.py gain clamps
  +10/+12dB -> +16dB. Earlier today: 13 CARD_HOLD constants -> 2.0s.
- **FINAL: 199 measured, 196 clean.** All pass verify-mp4, all under 25MB, all
  -14.0..-16.0 LUFS, all local bytes = origin. The only 3 failures are
  approved-locked and untouched: #142 (12.8s), #143 (9.0s), #145 (9.6s) dead air —
  their build.py is already fixed, so a re-render clears them.
- Open: cron stopped firing after 10:33 (entry intact, lock free) — round-2 ships
  were manual; verify-mp4.sh still has no size gate; build-137-stephen-sees-him-
  standing is a purged dupe dir that still holds an mp4 and should be archived.

