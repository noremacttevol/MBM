# QC / RUNNER HANDOFF — build-61-syrophoenician-woman (Mark 7:24-30)

## 🅿️ AUTHOR-FIXED → NEEDS-REBUILD (2026-08-07, Machine A `Dev`, $0 Fable-5 author lane)

**COMPLAINT LEDGER — OPEN Cameron complaint (row 61): "jesus's eyes in 0:52 are crazy looking."**

- **The 0:52 frame is `s11-she-asked-anyway.jpeg` (beat v2-r061-b11, window 47.38–53.49).**
  Jesus is in the frame ("the one face that has not hardened"), but the beat prose never
  specified his eyes, so the **JESUS-V2-REF master-face eye-cast** rendered them wide/wild
  ("crazy") — the exact failure now codified as **rubric lesson 18** (row 109 was the first
  instance; this is the second). Root cause is mostly SYSTEMIC (the master sheet's own
  eye-cast recurs on Jesus close-ups), not per-row prose.
- **AUTHOR FIX (this session, $0 — no image gen):** added an explicit CALM-EYES instruction
  to b11 (must_show: "Jesus's EYES are CALM, warm and softly open — the settled, kind gaze
  of the master face, steady on the kneeling woman"; must_not_show bans wide/wild/bulging/
  staring/manic/'crazy' eyes, whites-showing wide-eye, lens-stare; scene now names his calm
  warm steady gaze). Reinforced the SAME ban on the adjacent Jesus close-up b12 (the pause)
  so the whole close-up cluster is safe. `--check PASS` (31 beats), audio UNTOUCHED.
- **🅿️ RUNNER — do this (paid, ONE targeted re-cut, touch-once):** reroll ONLY
  `s11-she-asked-anyway.jpeg` against the fixed b11 prose (face-board it vs
  `JESUS-MASTER-REF/jesus-face.jpeg` for the locked calm-eyed Jesus). Keep every other still
  byte-identical. Re-assemble with **AUDIO LOCK byte-identical** (nothing re-voiced), re-run
  the face gate (must exit 0), and ship with a review card telling Cameron the crazy-eyes
  complaint was addressed. **SYSTEMIC FLAG (non-blocking):** if a calm-eyes reroll STILL
  lands a wild gaze after ≤2 tries, STOP rerolling — it is the master-ref sheet's eye-cast;
  FIX-WAVE it and escalate for a master-ref review (per lesson 18), do not churn credits.

## ✅ AUDIO FIX DONE — STALE-V1 lock cleared + realistic-V2 cut SHIPPED (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

**Class: STALE-V1 (duration/recency), NOT a pronunciation complaint.** `v2_outline.py 61`
shows ZERO open Cameron complaints — the row was parked only on the AUDIO LOCK
(`extracted timeline 185.202s vs stale V1 mp4 179.333s, +5.869s`), because the V1 mp4
(rendered 2026-07-29 09:47) predates the make_narration.py edit (2026-07-29 23:03) by ~13h.

**Fix (the sanctioned exception, $0 — NO new TTS):** set `AUDIO_FROM_V1_SEGMENTS = True`
in beats_v2.py (module level, after `REF = True`). `v2_assemble.py 61` then rebuilds the
track from the 15 current V1 mp3 segments (the new-voice segments) rather than copying the
stale mp4 audio:
- `AUDIO REBUILT from 15 V1 segment mp3s (-24.4 LUFS -> +9.4 dB), 185.202s`
- `AUDIO REBUILD PASS` — the lock passes via the rebuild path.

**Shipped as a full realistic-V2 cut** (all 31 stills were already generated + Light-QC
passed, 0 rerolls — nothing regenerated, $0 pictures):
- mp4: `media-production-v2/build-61-syrophoenician-woman/mark-7_syrophoenician-woman.mp4`
- 185.2s / 21.2 MB, video+audio streams verified via ffprobe.
- SHA256 (mp4) = `106884ad52f72da70f9448d0e8b3a9212d3b4fde1f4322a3369e7a57ea6ab278`
- Rebuilt-audio segment SHA256 = `274d1bbdd26fa164f519c7b54eac65826ebe9a7034f5757502b479eea3c97aed`

**Audio baseline change (V2 audio-immutability sanctioned exception):** OLD = stale V1 mp4
encoded audio (179.333s). NEW = rebuilt from the 15 current V1 mp3 segments (185.202s).
Same voices, same wording, same timing as the current mp3 segments — only the out-of-date
mp4 encode was replaced. No scene text, no locks, no beat structure touched.

**Review card:** `data-review-wave="realistic-v2"`, points at the v2 mp4; the 🛠 flag notes
the audio was rebuilt clean from the new-voice segments and the audio is otherwise
untouched. No Cameron complaint to answer (none was ever filed on this row).


Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 31 beats, ~178 s.

## Coverage shape

Three true wides with stated geometry: b01 (the coast-road arrival in
profile), b06 (the invisible wall — camera behind her shoulder with the
whole distance falling away), b25 (the word crossing the distance —
from behind Jesus's shoulder at the door as she climbs into the night).
Fourteen flips — this is an intimate two-room story; b26's moonlit
faith-walk is a LONE woman (phantom-people trap).

## The exchange (b13-b18) — the row's razor edge

The bread-and-dogs saying and her answer are the whole story. Laws:
- The saying beat (b13) has real BREAD on the low table — the
  metaphor's furniture is literal and in frame.
- Her face through the exchange: never humiliated-crushed, never
  sassy — a mother's unbudging wit. The posture arc IS the story:
  face-down (b10) → kneeling upright meeting his eyes (b18).
- Jesus's face during the hard saying carries the TEST, not contempt —
  the warmth is banked, then breaks open at her answer.

## The healing is REMOTE (like row 50)

Nothing visible crosses the distance — no beam, no light. The proof is
the sleeping child at rest (b28: face loose and peaceful, ALIVE —
row-15 law: restful, never corpse-still; her chest visibly mid-breath).

## Other checks

- The woman is PHOENICIAN — her dress differs from Galilean women
  (sea-dyed colors per her lock) but stays modest and dark; her
  identity constant across town/house/home frames (face-board).
- Direction (row-83): b06 she looks DOWN the lane toward the house;
  b26 she climbs UP toward home; b25 holds both poles in one frame.
- HOUSE plate: Bethany-lane suggested a SIXTH time — DECLINED (this
  is a borrowed Phoenician coast-town house). TYRE promote-first from
  b01; HERHOME from b07.
- GIRL: one age, one face, worn-but-alive sick, peaceful-asleep
  healed (row-15 + row-56 class).
- Only Jesus wears cream.

---

## RUNNER RESUME + LIGHT QC (2026-08-06, Machine A `Dev`, headless)

Resumed a lane that died mid-build (board RUNNING / A-auto). No live sibling
`v2_gen_api` owned the row (`ps` clean); mp4 NOT committed and no `realistic-v2`
card live → genuinely mid-build, safe to resume. `--check` PASS (31 beats).
Portraits 0-to-make (WOMAN, GIRL sheets set). Only 1 frame pending on resume:
**b31 s31-the-whole-loaf** (place HERHOME) — generated at 2K (2631 KB), ceiling
$441. All other 30 stills were already valid and re-pulled nothing (COST LAW).

### COMPLAINT LEDGER
`v2_outline.py 61` shows **none open.** COMPLAINT LEDGER: none open.

### Light QC — one pass, 3 contact sheets, all 31 frames viewed
Checked against must_show/must_not_show, this build's laws, and every
RUNNER-LESSONS pattern. **Result: PASS, 0 rerolls (0% — under the 15% budget).**
- Only Jesus wears cream across every frame he's in (s01,02,10,11,12,13,16,20,21,23,25). No second cream figure.
- The exchange furniture is literal: real BREAD in the basket on the low table (s13); house-PUPS under the family table eating a crumb, not street dogs (s15).
- Posture arc reads: face-down/kneeling (s10) → kneeling upright meeting his eyes (s18). Jesus's warmth banked during the test (s14), breaking open glad at her answer (s20/s22).
- REMOTE healing — nothing crosses the distance, no beam/light (s24/s25). Proof is the living, resting child: peaceful-asleep + mother's relief (s28), gathered in arms (s29), then fully awake eating the whole loaf (s31).
- b26 moonlit faith-walk is a LONE woman (phantom-people trap avoided); direction correct (b06 looks down the lane, b26 climbs up toward home, b25 over Jesus's shoulder at the door holds both poles).
- Night beats (s25/s26) render as night; no modern objects, no lens-stares; anatomy/scale fine; Phoenician woman + Jesus + girl identities consistent across town/house/home.
- Jesus's slightly hazel/green eye cast (s14 close-up) is the KNOWN baked-in JESUS-V2-REF trait shared by all shipped V2 rows — NOT rerolled (per RUNNER-LESSONS; a reroll only re-echoes the ref and burns meter).
- FIX-WAVE watch (no reroll, COST LAW): s30 tight embrace reads slightly limp in isolation, but s28/s29/s31 unambiguously establish a living, resting, then awake child — sequence disambiguates. Left as best take.

---

## ⛔ RUNNER PARK — STALE-V1 AUDIO LOCK (2026-08-06, Machine A `Dev`, headless)

**Assembly BLOCKED at the audio hash — do NOT ship.** `v2_assemble.py 61` prints:
`AUDIO LOCK: extracted timeline is 185.202s but the authoritative V1 final is 179.333s.`
Excess = **+5.869s** (V1 mp4 is SHORTER than the current narration timeline).

**Root cause — classic STALE-V1 (same class as rows 69/106):**
- V1 mp4 `media-production/build-61-syrophoenician-woman/mark-7_syrophoenician-woman.mp4`
  rendered **2026-07-29 09:47**.
- `media-production/build-61-syrophoenician-woman/make_narration.py` edited
  **2026-07-29 23:03** — ~13 h AFTER the V1 render. The narration source changed
  (the V1 dir has 15 mp3 segments reflecting the newer timeline), but the V1 mp4
  was never re-rendered, so its encoded audio is out of date.
- `beats_v2.py` has NO `AUDIO_FROM_V1_SEGMENTS` line set.

**Why the runner cannot fix it (audio-immutability law + hard rail):** the fix is
`AUDIO_FROM_V1_SEGMENTS = True` in this row's `beats_v2.py`, which rebuilds the
track from the current V1 mp3 segments. Editing `beats_v2.py` is outside the
runner's allowed writes and choosing the authoritative audio source is an AUTHOR
audio decision. The runner must not ship over a failed audio lock (row 46 shipped
this way = "the worst failure").

**State of the stills — ALL DONE, DO NOT REGENERATE (COST LAW):** all 31 stills
generated at 2K and PASSED Light QC (0 rerolls — see the QC section above). Only
b31 was pulled this session ($0.13); the other 30 were valid from the prior lane
and re-pulled nothing. Plates (TYRE, HERHOME) and cast (WOMAN, GIRL) committed.

**RESUME for the AUDIO-FIX / author lane (then it ships in ONE assemble, $0 pictures):**
1. In `media-production-v2/build-61-syrophoenician-woman/beats_v2.py` set
   `AUDIO_FROM_V1_SEGMENTS = True`.
2. `python3 media-production-v2/v2_assemble.py 61` → must print `AUDIO LOCK PASS`.
3. Ship per PROMPT-OPUS-RUNNER.md step 7 (commit mp4 + boards, review card
   `data-review-wave="realistic-v2"`, `firebase deploy --only hosting`, live-verify),
   then STASH `--scan`, publish_ledger sync, tick Built.
