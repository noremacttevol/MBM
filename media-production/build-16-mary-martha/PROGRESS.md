# Build #16 — Mary and Martha (Luke 10:38–42) — PROGRESS / HANDOFF

**Machine A (Dev). Claimed on VIDEO-ASSIGNMENTS. Stills-only (Law E), face-never (Law B).**
Last updated 2026-07-11 by the Machine A session (paused by Cameron to review).

## DONE ✅

- **Rules re-read** (PRODUCTION-BIBLE §0 laws + §1 Standing Laws + CLAUDE.md chain). Fixed a
  stale contradiction: CLAUDE.md guardrail **#12** still said "motion clips required" — corrected
  it to Phase-1 stills-only to match Law E (commit `be31a59`).
- **Claim** pushed (VIDEO-ASSIGNMENTS + STATUS) — `be31a59`.
- **PROMPTS.md** — 6-shot sheet written; **face gate PASS** (`jesus_face_gate.py --dir` exits 0).
- **Narration** — `make_narration.py` (12 narrator segments + 1 KJV Jesus line j1 + closing card);
  generated with edge-tts (Andrew narrator, Christopher = Jesus, KJV only). **Ear-check PASS 14/14**
  (`qc_narration.py`). Commit `8f2acd7`.
- **build.py** — assembly engine ready (verbatim captions, KJV cream italic, music silent on
  "Martha, Martha," Ken Burns drift, loudness ~-15 LUFS, names output `luke-10_mary-and-martha.mp4`).
- **Stills 1–4 generated, QC'd (face law + anatomy), downloaded 2K (1536×2752), placed in assets/:**
  | Shot | File | Flow edit | Face-law |
  |------|------|-----------|----------|
  | 1 arrival | s1-arrival.jpeg | edit/78d714b8-99ef-4915-bbe3-cd80a8ea6d57 | Jesus from behind at door ✅ |
  | 2 Martha serving | s2-martha-serving.jpeg | edit/b8e258b6-072b-4fda-a105-eb1db65237e9 | no Jesus in frame ✅ |
  | 3 Mary at his feet | s3-mary-at-his-feet.jpeg | edit/197d64c0-b89f-4001-ac11-7d74ddc0f4ea | Jesus center, from behind ✅ |
  | 4 worn thin | s4-worn-thin.jpeg | edit/fc554248-89be-4976-af98-a78fc53e5063 | Jesus foreground, from behind ✅ |

## LEFT TO DO ⏳

1. **Generate stills 5 & 6** in Flow ("MBM Story Videos — Wave One" project), 9:16, Nano Banana 2,
   download 2K → `assets/s5-her-name.jpeg`, `assets/s6-two-sisters.jpeg`. Prompts are in PROMPTS.md;
   the sheet already passes the face gate. (Shot 5 is tight on Martha's face — no Jesus in frame;
   shot 6 has Jesus from behind at a distance.)
2. **Run `python3 build.py`** (needs all 6 stills present) → `luke-10_mary-and-martha.mp4`.
3. **Self-revision loop / QC** (§1, §5): watch through, frame-strip, confirm face never visible in any
   frame at any zoom, captions verbatim, no dead air, <25 MB, 1080×1920.
4. Update STATUS.md / VIDEO-ASSIGNMENTS row to "BUILT — awaiting Cameron", SESSION-LOG entry, push.
5. Then **#19 Breakfast on the Shore** (Machine A rank 3) — same pipeline.

## NOTE for whoever finishes on this machine (Dev = Machine A)

The Claude-in-Chrome extension lists 3 browsers. **Browser 2** (deviceId
16cace08-0272-4e98-b9f1-ae065c310164) is THIS machine — its Flow 2K downloads land in
`~/Downloads` (then move into `assets/`). **Browser 1** is a DIFFERENT computer; its downloads do
NOT reach this disk, so don't assemble from it. When sending a Flow prompt, click the **"Create"**
button by its element ref (find "send/submit arrow"), not by fixed coordinates — the coordinate
click silently missed twice.
