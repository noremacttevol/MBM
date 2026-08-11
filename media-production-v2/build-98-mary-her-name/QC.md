# QC / RUNNER HANDOFF — build-98-mary-her-name (John 20:11-18)

## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 98`). Parked
because the narration mp3s are newer than the V1 mp4 (2026-07-24) and |Δ|>1.0, so the
packet-copy AUDIO LOCK would ship stale voices. Fix ($0, no new TTS): set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler rebuilds from this build's
own 17 mp3 segments (present in the V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md
step 6, board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture runner assembles on
the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 21 beats, ~121 s.

## TOMB UNWIRED (fifth wrong-plate catch — the parable-tomb trap again)

The stash keeps offering build-37's parable tomb by token name. This is
JESUS'S garden tomb — the rows 71/96/97 family. Take row 97's approved
frame; re-remove the build-37 wire if --wire reruns.

## MARY MAGDALENE (the third Mary — her canon starts here or in 97)

Madder-red per her lock — distinct from Bethany-Mary (dusty-indigo,
CAST-V2 sheet exists now) and the mother (indigo-blue veil). Whichever
of rows 97/98 builds first sets Magdalene's canonical face; the other
anchors. Never cross the three Marys.

## The risen Jesus (rendering law)

NATURAL — cream robe, warm, real; NO wounds shown, no shining, no
glow: the whole story turns on him being mistakable for the gardener
(b04-b07), so he must look like a MAN in a garden. Recognition comes
from her, not from effects.

## The recognition (b12 — the row's heart, kept TIGHT)

One word — her name — and she turns: the frame is her face blazing
alive mid-turn. "RABBONI." If the render gives a generic joyful
reunion instead of the mid-turn instant, reroll.

## The touch-me-not (b16 — gentleness law)

His raised hand is SOFT between them — a gentle hold, never a rebuff;
her reaching arms and his tenderness share the frame. Any cold or
rejecting render fails.

## Coverage shape

Three true wides with stated geometry: b01 (the stayer — figure and
doorway from the side), b10 (the love measured — both figures in one
profile), b14 (the flip — camera behind her rushing shoulder). Seven
flips including b20's LONE full-stride run (phantom trap).

- Direction (row-83): she faces the tomb; turns BACK to him; runs
  TOWARD the city at the send — three pivots, each readable.
- Early gold → full clear morning, one direction.
- Only Jesus wears cream.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: timeline vs V1 mp4 |Δ|=1.02s (>1.0).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.

---

## ✅ RUNNER SHIP — realistic-V2 first cut (Opus runner, Machine A `Dev`, 2026-08-07, UNATTENDED/HEADLESS)

**COMPLAINT LEDGER: none open.** `v2_outline.py 98` shows no Cameron complaint on this row; QUEUE row 98 = "Mary at the tomb: her name" (John 20) — cross-checked, NOT swapped.

**Build:** 21 realistic stills @ native 2K, 126.7s / 20.7 MB. **AUDIO REBUILD PASS SHA256=3261c510639ce86616e428e04378f9e89100eba02c2b57340e25391a72c8072b** (rebuilt from the 17 V1-dir segment mp3s via AUDIO_FROM_V1_SEGMENTS=True — narration byte-identical, nothing re-voiced). Decode-clean (`ffmpeg -v error -f null` = 0 errors). Stale-window pre-check: max still-window 120.69 < live card_start 120.811 (drift −0.121s, no overrun) — all 21 stills placed, no dropped beat.

**TOMB plate (wrong-plate trap handled):** `v2_stash.py --wire` again offered build-37's PARABLE tomb (and silently edited PLACE-WIRING.json + beats_v2.py PLACE_REFS + wrote PLACE-REF/tomb.jpeg). Reverted all three (git checkout of both files + rm of the plate), regenerated b01 plate-free so it rendered JESUS's garden tomb from the text lock, QC'd it (rock-cut garden tomb, rolled-away stone disc, olive garden, dawn, no modern objects, Mary madder-red NOT cream), then `--promote`d THIS row's own b01 as the TOMB plate (rows-71/96/97 family). Cost the one wasted b01 gen (~$0.13) to catch the wire bug — logged honestly.

**Light QC (one pass, all 21 viewed):** Jesus ONE locked face across all 9 Jesus frames (s04/s05/s07/s10/s11/s12/s13/s14/s15/s16/s18/s19), cream-only held (Mary + disciples never cream), natural/no-glow/no-wounds so he reads as the "gardener" (b04–b07, the story's hinge), s07 even carries a period billhook. Three-Marys law: Magdalene locked madder-red throughout, one consistent olive-skinned face. b12 (Rabboni) landed the mid-turn recognition instant (not a generic reunion); b16 touch-me-not is a SOFT gentle hold, not a rebuff; b20 LONE run is ONE Mary (no phantom twin), running toward the city; b21 epilogue = three DISTINCT disciples, none cream, all period props. No lens-stare, no modern objects (after the s19 fix), anatomy/scale clean, Jesus ordinary-sized.

**Rerolls: 1 / 21 = 4.8%** (under the 15% budget). s19 ("go to my brothers") first take had white multi-storey MODERN-LOOKING buildings on the far skyline (row-83 modern-skyline class) — one `--redo` cleared it to olive trees + stone wall + hillside.

**FIX-WAVE (no filed complaint, not blocking — author's beat text drives these, not a runner reroll):**
- b05 / b13 are intimate Jesus↔Magdalene two-shots; the closeness is AUTHORED (b13 must_show literally "the two faces close … the intimacy of HABIT"). Render obeyed the text. Given the Jesus/Magdalene pairing's sensitivity, if Cameron ever reads it as romantic, the fix is an AUTHOR edit (add arm's-length + "no romantic/intimate framing" to b05/b13 must_not_show, per the row-49 lesson) then reroll only those two — NOT a runner reroll of author-driven framing.
- s19 reroll left a large madder cloth draped over the rolled stone (minor oddity, not a modern object / not a figure) — FIX-WAVE.
- A tiny recurring red speck on a background tree propagates from the TOMB plate (s01) into TOMB-locked frames — negligible background artifact, FIX-WAVE.

**Cost:** row spend ≈ $3.48 (490.17 − 486.69 on the meter): 20 beats $2.68 + s19 reroll $0.13 + the good b01 plate $0.13 + the one wasted build-37-plate b01 $0.13 + the promote is free. Under the $6.10/row average — COST-LAW trend DOWN holds. QC rerolls 4.8%.

---

## QC-VERIFY (FULL-CUT GATE 6b) — 2026-08-11, Machine A `Dev` — CLEAN, QC-OK, NOT re-cut

**COMPLAINT LEDGER: none open** (`v2_outline.py 98` = beat map only, no Cameron complaint on file). Pure verify pass before Cameron's eyes reached this BUILT row in his Unwatched queue (the row-11 "quality is going down" mandate).

Extracted ONE frame per beat (21) from the RENDERED mp4 at each clip's mid-window (durations from segs/c000–c020) + 2 caption frames + the closing card, and viewed every frame against the defect checklist + RUNNER-LESSONS.

- **Verdict: CLEAN — QC-OK, NOT re-cut** (instruction: do not re-cut a clean row).
- **Jesus ONE locked master face on every appearance** (b04/05/06/09/12/13/14/15/16/17/18/19): warm Middle-Eastern, dark wavy hair, full beard, warm brown/green eyes, **cream-only** (Mary is madder-red — no 2nd cream figure anywhere, incl. the b21 disciples in brown/tan), **no halo/glow/rim-light** (golden-hour hair backlight is natural). Ordinary human scale — NO giant/composite.
- **Mary Magdalene** madder-red-locked and consistent across all 21 beats; grief→recognition→joy arc reads (b11/12 RABBONI, b14/16 rush, b20 run, b21 first-sermon at the disciples' door).
- **Story gates read at a glance:** gardener billhook (mistakable-as-gardener) b09; soft touch-me-not stay (not recoil) b16/17/18; commission-pointing compass b19; b21 discloses no accidental second Jesus among the Twelve.
- **Captions two-voice correct + bottom-band only:** narrator WHITE, **WOMAN pink** (0xFF9EC7 — the defined color for any woman the Bible records speaking; verified in mbm_speakers.py, NOT a defect) on Mary's KJV lines (w13/w15), **Jesus RED** on his red-letter (b17 "…my Father, and your Father"). Card renders clean (serif, centred, cream): "He knows your name — and he speaks it even in your grief. Listen for it."
- **Live-verified (assurance = gate output, not my word):** github-raw served mp4 md5 `30f8a031119d9c30c0d181d5c4609664` == local == the bytes I gated; HTTP 200, 20,662,192 B. Live review card `v98` hash `e665631f…`, NO `data-machine-reason` (correctly in Unwatched). No deploy needed (clean, already live). Cameron watches the exact bytes I QC'd.
- **FIX-WAVE (pre-logged, NOT blocking, NOT re-cut):** soft LOCATION-continuity variance — most tomb-exterior beats are the lush olive-garden, but b10/b11/b21 read as a drier arid/wilderness rock-tomb palette; each frame is individually reverent and realistic, cross-frame soft-continuity harmonisation is the fix wave's job (touch-once/cost law forbids voiding a pending approval to chase subtle drift). Also carries forward the already-logged s19 draped-cloth oddity + the s01-plate background red speck.
