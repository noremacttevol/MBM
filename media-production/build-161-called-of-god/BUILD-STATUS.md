# BUILD STATUS — #161 Called of God, as was Aaron (Hebrews 5:1-6)

**Machine D, 2026-07-15.** MEMBER shelf verse-video → Gospel Library: Priesthood.
Phase-1 STILLS-ONLY (Law E), GREEN / plain-milk (no CONTENT-CARE flags).
**Status: PREP COMPLETE + all 8 stills SUBMITTED to Flow. Awaiting download + assemble.**
Row 161 in QUEUE.md is CLAIMED (Built ⬜) — do not tick Built until the mp4 exists.

## Done and committed
- Row 161 claimed and pushed.
- `PROMPTS.md` — 8 painted stills; face gate **PASS** (Christ referenced but never depicted).
- `make_narration.py` + all 12 audio clips generated (Andrew narrator; Christopher scripture
  voice for the KJV verses kv1/kv4/kv5; two sacred silences on kv4 and kv5).
- `build.py` — copied from build-135 (Windows-ready: `_ensure_fonts()`, `_find()`, 30MB cap),
  adapted to 8 stills, this video's BEATS/KJV set, output `hebrews-5_called-of-god.mp4`, and a
  closing-card **Gospel Library: Priesthood** pointer (`GL_POINTER`).

## In flight — the 8 stills are generating in Flow
Flow project **`1d0eb579-4041-4860-a0a7-1ba369bcc93b`** (Ultra account), Nano Banana 2, 9:16, 1x.
Prompts submitted in order s1…s8. NEXT SESSION: download them per FLOW-BUILD-PLAYBOOK.md
(fetch by media-id → anchor download → land in Downloads), QC via contact sheet, map each to
its slug, save as `assets/<slug>.jpeg`:
  s1-the-high-priest · s2-compassed-with-infirmity · s3-no-man-taketh-it · s4-called-of-god ·
  s5-laying-on-of-hands · s6-the-anointing · s7-so-also-christ (no figure — veil + light) ·
  s8-called-still.
Then `python build.py` → QC frames → tick Built ✅ row 161 → add title "Called of God, as was
Aaron" (num 161) to gen_site_index.py TITLES → regen index → commit + push.

## QC watch-list for this build
- s7 must contain NO figure of any kind (the Christ beat is light + the veil only).
- Aaron consistent across s1/s2/s4/s5/s6: blue robe + gold-blue-purple-scarlet ephod +
  twelve-stone breastplate + white linen turban with gold plate; face shown.
- Anatomy on the two laying-on-of-hands beats (s5, s8): two hands on the head, folded hands
  below, no third arm.
- Nobody but the priestly vestments in blue-and-gold; no one in off-white/cream.
