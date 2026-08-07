# QC / RUNNER HANDOFF — build-80-come-unto-me (Matthew 11:28-30)

## ✅ AUDIO FIX DONE — AUDIO-FIX session, Machine A, 2026-08-06 ($0)

**STALE-V1 audio-lock CLEARED.** Added `AUDIO_FROM_V1_SEGMENTS = True` to
beats_v2.py. V1 mp4 `matthew-11_come-unto-me.mp4` (2026-07-29 09:47) is older
than all 11 re-voiced segment mp3s (2026-07-29 23:03), so the recency tripwire
in `assert_v1_final_is_current` refused to copy its stale AAC (row-69 class).
With the flag set, v2_assemble rebuilds narration from the V1 build's OWN
new-voice mp3s at the extract offsets — nothing re-voiced/re-timed, V1 read-only.
**Segment parity 11/11 exact.** Validated: `v2_assemble.py 80` now clears the
audio gate and stops only on missing stills (0 V2 stills); `v2_prompt.py 80
--check` PASSES (14 beats). Board NEEDS-AUDIO → AUTHORED / Audio OK / Ready ✅,
claim cleared → picture runner generates + assembles on corrected audio.

---

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 14 beats, ~83 s.

## Coverage shape

Three true wides with stated geometry: b01 (the homeward lane in
profile — every spine writing the same sentence), b03 (the offer —
camera behind the burdened listeners' shoulders as the arms open), b06
(the yoke cutaway — team and beam in profile beside the furrow). Five
flips.

## THE YOKE (the row's own doctrine-prop)

- A carved wooden DOUBLE yoke with two bow-loops — a SHARED beam for
  two oxen. Never a single-animal harness, never leather tack (the
  entire teaching lives in the two-sidedness).
- The arc: one ox laboring beside an EMPTY loop (the vacancy visible)
  → the second ox stepping IN under the open loop (b12) → the pair
  pulling as one (b13). Same two russet oxen, same beam, all frames.
- The plough keeps biting in b13 — rest is SHARED pulling, not
  stopping (the honest promise; do not render the field finished).

## The carrier's echo arc (mirrors the oxen on purpose)

Sack roped on his back alone (b01/b04) → coming WHILE loaded (b07 —
no precondition; the load stays ON through the offer) → the closing
(b14): Jesus walking BESIDE him, one hand steadying the sack's weight
— shared, not removed. If a render takes the sack away, it breaks the
doctrine; reject.

## Other checks

- Day's-end gold throughout, deepening to last light — a CORRECT
  story sunset (stated in the docstring; not the row-11 defect).
- The weary are dignified — tired workers, never wretched caricatures
  (row-15 dignity class). Crowd varied (90/107).
- Direction (row-83): homeward flow one way down the lane; the
  carrier turns TOWARD Jesus mid-step; the second ox steps IN under
  the loop.
- LANE wired from build-38's golden village-edge frame (light-
  compatible). OXFIELD promote-first from b06.
- Only Jesus wears cream.

---

## RUNNER PARK — NEEDS-AUDIO (A-auto Machine A `Dev`, 2026-08-06, $0 spent)

**Pre-flighted at step 2 BEFORE any generation (lesson-74 $0 park). NOTHING
generated — zero credits.**

`assert_v1_final_is_current(row 80)` FAILS: the V1 final
`media-production/build-80-come-unto-me/matthew-11_come-unto-me.mp4` was
rendered **2026-07-24 10:15:29**, but ALL 11 of its narration mp3s are NEWER
(**2026-07-28 14:28:20**). Timeline total = 90.6s, mp4 dur = 88.5s (excess
-2.1s), newer_mp3s = 11/11. The V1 mp4's audio stream predates the current
narration, so `v2_assemble` refuses AUDIO LOCK — copying it would ship stale
voices / a shortened timeline (rubric audio-immutability law).

This is the **row-69 / row-74 / row-78 STALE-V1 class.** The runner is
forbidden from fixing it (the fix edits `beats_v2.py`, an author audio
decision outside runner writes).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this build's
`beats_v2.py` (renders narration from the V1 build's OWN mp3s at the
extract_beats offsets — nothing re-voiced, nothing re-timed, V1 stays
read-only), OR re-render the V1 mp4 from the current narration.

**RESUME (runner, after author fixes audio):** `Read
media-production-v2/PROMPT-OPUS-RUNNER.md and run the next ready rows.` — the
14 authored beats are ready to generate (`v2_prompt.py build-80-come-unto-me
--check` = PASS). No stills exist yet; a full build from step 2.

---

## ✅ BUILT realistic-v2 — Opus runner, Machine A `Dev` (UNATTENDED/HEADLESS), 2026-08-07

**COMPLAINT LEDGER: none open.** `v2_outline.py 80` shows no open complaint on
this row — the prior park was NEEDS-AUDIO (STALE-V1), now cleared by the author's
`AUDIO_FROM_V1_SEGMENTS=True`. Nothing re-voiced; narration content byte-identical
to the V1-dir segment mp3s.

**Build:** 14 realistic stills at native 2K (V1 ASSEMBLY-C had 8), 90.6s, 19.6 MB.
1 portrait (CARRIER). Places: LANE plate (author-wired from build-38), OXFIELD
promoted-first this row from b06 (person-free two-ox double-yoke anchor, QC'd clean
before promote) → wired to b06/b11/b12/b13. Only Jesus wears cream.

**Doctrine arc held (QC.md gates):** the double-yoke two-sidedness reads across the
oxen frames — b06 defines the shared beam (two oxen pulling together), b11 shows ONE
ox laboring beside the EMPTY loop (vacancy visible), b12 the second ox stepped IN under
the open loop, b13 the pair pulling as one with the plough still biting (rest = SHARED
pulling, field NOT finished). The carrier's echo arc held: sack roped on his back alone
(b01/b04/b05), coming WHILE loaded through the offer (b07), and the closing b14 = Jesus
walking BESIDE him with one hand steadying the sack's weight — the load stays ON (shared,
not removed). No render took the sack away.

**Light QC (1 sweep, all 14 frames viewed + 3 rendered caption frames): 0 rerolls / 14
= 0% (COST LAW: far under 15%).** Beard-board: CARRIER grizzled grey-brown beard present
every frame; Jesus full dark beard, dark wavy shoulder-length hair, warm skin, warm
brown eyes (no glow, no stare) every frame. Scale gate: Jesus ordinary-sized beside the
carrier/crowd in every multi-figure frame — no giant. No modern objects (checked sand/
ground for lug-tread prints — clean), no second cream figure, no lens-break, no collage,
no cartoon/CGI frame (all photographic), no burned-in text.
FIX-WAVE (kept, non-blocking): oxen cutaway frames (b06/b11/b12/b13) sit under a flatter
overcast daylight vs the day's-end gold of the human frames — they are metaphor cutaways
so it does not jar; a later wave could warm them to match.

**Audio (STALE-V1 batch — row-74 tail check done):** AUDIO REBUILD PASS
SHA256=97eaf33477e95642c9fbe5c3eafa5eb52206a4106000bce5b53abdbaf217ddd3, rebuilt from
11 V1-dir segment mp3s, 90.604s. Tail check: captioned.mp4 = 83.000s vs card seg_start
= 82.957s (diff 0.043s <= 0.2s) -> full question card present, no tail chop; final mp4
90.633s ~= audio 90.604s. Captions bottom-band only; Jesus sayings red, narrator white;
question card clean (no squares).

**Cost:** 1 portrait $0.13 + b06 anchor $0.13 + 13-beat run $1.74 = **~$2.00 this row**,
0 rerolls. Well under the $6.10/row average — COST LAW trend holds DOWN.
