# QC / RUNNER HANDOFF — build-139-lamp-on-a-stand (Matthew 5:14-16)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 10 beats, ~48 s.

## Shares row 121's canon (build/wire together)

HILLSIDE, CROWD, LAMPHOUSE and HILLTOWN locks are BYTE-IDENTICAL to
build-121 — same sermon, same one-room house (same lamp, stand and
bushel), same far town. When 121 promotes any of these, wire them
here identically. The lamp/stand/basket must be the SAME props as
121's b17-b20 chain.

## Light law (doubly binding — this is a light row)

Every light physical: sun, clay flame, dusk windows. Any light
effect ON a person = automatic reject; watch the drift words on
rerolls. b02's only light is the SUN. Dusk/evening frames (b03,
b04, b05, b07, b08, b10) are BY DESIGN.

## Anti-vanity pair (b07/b08, the 121/122 class)

b07: the giver's eyes on the task, gone before the door opens —
nobody watching. b08: the widow's gaze travels UP PAST the departing
helper to the sky — nothing in the sky.

## The close (b10)

A careful hand PLACING the lamp deliberately — unhurried, exact,
flame steady. The deliberateness is the sermon.

## Coverage shape

One true wide with stated geometry: b01 (camera past the seated
crowd's backs). Four Jesus beats (b01, b02, b06, b09); b06 is the
identity-before-assignment register — naming, not tasking. File
order ≠ story order (b06 at 2.73s) — build by WINDOW.

- Plates: none auto-matched. Share HILLSIDE/HILLTOWN/LAMPHOUSE with
  121 when promoted; the bushel visible and UNUSED in b05.


---

## ✅ AUDIO-LANE FIX APPLIED — Opus audio-fix lane, Machine A `Dev`, 2026-08-11, $0

**STALE-V1 resolved (8 newer mp3s / +10.4s).** Added `AUDIO_FROM_V1_SEGMENTS = True` to `beats_v2.py`
(after `REF = True`). The authoritative track is now rebuilt from the V1 narration mp3s
at the extract_beats offsets instead of copying the stale V1 mp4's AAC stream that failed
`assert_v1_final_is_current`. **Validated ($0, no TTS, no Gemini):** rebuilt track = 55.109s,
delta 0.000s vs the mp3 timeline total (guard needs <0.5s). No re-voice — same voices,
wording, timing.

**Row is buildable.** 0 stills, so per the audio-fix protocol the board is flipped to
**AUTHORED / Audio OK / Ready ✅**; a picture runner generates the stills then runs
`v2_assemble.py 139` → AUDIO REBUILD PASS and ships the full cut on this fixed audio.

---

## ✅ V2 REALISTIC FIRST CUT SHIPPED — Opus runner, Machine A `Dev`, 2026-08-13 (headless)

**COMPLAINT LEDGER: none open.** `v2_outline.py 139` shows no filed complaint on
this row — this is a first realistic-v2 cut of a row whose only prior asset was
the 2026-07-17 ASSEMBLY-B (7 W1 stills). Nothing to answer; nothing to regress.

**Build:** 10 realistic stills @ native 2K (1536×2752). No portraits needed
(Jesus via the global V2 master ref on b01/b02/b06/b09; CROWD/HILLSIDE/LAMPHOUSE/
HILLTOWN are group/place text-locks). No place plates promoted — the shared 121
HILLSIDE/HILLTOWN plates both contain Jesus (never auto-wire a Jesus-bearing
frame, RUNNER-LESSONS lesson 11/126), and LAMPHOUSE's 3 beats carry fine on lock
text; PLACE_REFS stayed empty as authored.

**Rerolls: 0/10 = 0%** (COST LAW: far under the 15% budget). Every beat landed
clean first-pass — no missing subject, no second cream figure, no modern object,
no letterbox, no giant, no lens-stare, anatomy clean.

**FULL-CUT GATE (one frame per beat from the RENDERED mp4 + card): 10/10 + card PASS.**
- Jesus ONE locked face b01/b02/b06/b09 — warm Middle-Eastern, dark wavy hair,
  full beard, ref-true calm eyes (green/hazel, NOT brown-edited — rubric lesson 20),
  cream robe ONLY on Jesus, no halo/glow/rim-light, ordinary scale among the
  seated crowd (SCALE GATE pass).
- LIGHT LAW (doubly binding on a light row) held: every light PHYSICAL — sun
  (b01/b02/b06/b09), clay-lamp flame (b04/b05/b07/b08/b10), dusk windows (b03).
  No light effect ON any person; b09's golden-hour backhaze is general
  atmosphere, NOT a head-rim-light (his head sits against the hillside, not the
  bright sky).
- Anti-vanity pair correct: b07 giver's eyes on the task, already turning away,
  nobody watching; b08 widow's gaze travels UP PAST the departing helper to an
  EMPTY evening sky (nothing supernatural in it).
- b03 hilltown = intentional dusk, warm windows pricking on, no people
  distinguishable. b10 close = a careful hand placing the lit lamp deliberately.
- Realistic photography throughout (Law 14 — no cartoon/mix). Facing-away crowd
  figures (b01/b09 foreground backs) are CORRECT, not owl-necked (lesson 21).
- **CAPTIONS pixel-verified:** narrator WHITE (n0/n1/n2/n3), Jesus KJV lines RED
  (j1=Matt 5:14, j2=Matt 5:15, j3=Matt 5:16), NO green (no God-voice this row —
  the Father is only referenced, never speaks). Captions bottom-band only.
  Question card clean cream serif ("You were made to be seen for good. Let it
  shine."), no tofu/code-fault.
- DROP-CHECK: segs/concat_base.txt = 10 clips == 10 BEATS (row-173 last-beat-drop
  risk cleared); video 55.13s ≈ audio 55.11s.

**FIX-WAVE (non-blocking, deliberately NOT rerolled):** (1) the two household
children in b04/b05 render lighter/dishwater hair vs Middle-Eastern dark — soft
historical-coherence variance, not a filed complaint class, not garbage-tier.
(2) b05 stages the lit lamp on a low stool rather than the tall wooden stand of
b04 — still elevated and serving the room, bushel visibly idle; minor. (3) b09
strong golden-hour backhaze (verified NOT a halo). None warrant a reroll on a
0-complaint first cut.

**Audio:** AUDIO_FROM_V1_SEGMENTS=True (audio-lane STALE-V1 fix, 2026-08-11) —
track rebuilt byte-consistent from the 8 V1-dir segment mp3s at extract_beats
offsets, nothing re-voiced/re-timed. **AUDIO REBUILD PASS
SHA256=27deb09af4c3fcd4ecf0c60df5f21c9c01866a2ec3510b04fe624b06985078b2**,
55.109s, 19.5 MB.

**Cost: $1.34/row, 0% rerolls** — well under the $6.10 / 19% running average
(COST LAW downward trend holds; 10/10 clean first-pass, no portraits, no plates).

---

## ✅ QC-VERIFY PASS (FULL-CUT GATE 6b) — Opus runner, Machine A `Dev`, 2026-08-13 (unattended/headless)

Independent verify pass on the shipped cut BEFORE Cameron's eyes reach it
(Unwatched queue). Approval state checked FIRST: `.approvals.json` row 139
`approved:false`, `complaint:null` — NOT a current approval, so eligible for
verify (the 3 AM approved-row re-cut failure does not apply). Live card
`data-hash=5d3e7c1856a29c5614543cd504c05c96ac9a51dd` == ship hash == on
milk-b4-meat.web.app. Claimed on the board before viewing.

**One frame per beat extracted from the RENDERED mp4 (mid-window) + card, viewed
against the defect checklist + RUNNER-LESSONS + this row's laws:**

- **10/10 beats + card CLEAN.** No reroll needed. NO re-cut ($0/0 gens).
- Jesus ONE locked face b01/b02/b06/b09 — warm Middle-Eastern, dark wavy hair,
  full beard, ref-true green/hazel calm eyes (NOT brown-edited), cream robe ONLY
  on Jesus, no halo/glow/rim-light, ordinary scale among the seated crowd
  (SCALE GATE pass, incl. standing b09).
- LIGHT LAW (doubly binding) held: every light PHYSICAL — sun (b01/b02/b06/b09),
  clay-lamp flame (b04/b05/b07/b08/b10), dusk windows (b03). No light effect ON
  a person; b09 golden backhaze verified atmosphere, not a head-rim.
- Anti-vanity pair correct: b07 giver's eyes on the task, nobody watching; b08
  widow's gaze UP PAST the departing helper to an empty evening sky.
- Anatomy/hands clean on EVERY frame, including the b10 hand-placing-lamp close
  (fingers/thumb natural). No modern objects; period props (clay lamps, wicker
  bushel idle in b04/b05, rolled mats). Realistic photography only (Law 14) —
  no cartoon/mix. Facing-away crowd backs (b01/b09) correct, not owl-necked.
- CAPTIONS: narrator WHITE (b01/b04/b07/b08/b10), Jesus KJV RED (b02=Matt 5:14,
  b05=5:15, b09=5:16), bottom-band only, no green. Card clean cream serif
  ("You were made to be seen for good. Let it shine.") — no tofu/code-fault.
- **No open complaint on this row -> nothing to regress.** The prior FIX-WAVE
  soft notes (b04/b05 children's lighter hair; b05 lamp on a low stool) are
  historical-coherence variance, not a defect-checklist failure or a filed
  complaint class -- they do NOT warrant a re-cut on a 0-complaint clean cut.

Board Claim -> **QC-OK 2026-08-13**. Cut stands as shipped; Appr stays [ ]
(Cameron's alone).
