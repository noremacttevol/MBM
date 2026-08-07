# QC / RUNNER HANDOFF — build-89-last-supper (Luke 22:14-20)

## ✅ AUDIO FIX DONE — STALE-V1-FINAL lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (duration shortfall), no open Cameron complaint (`v2_outline.py 89`).
Parked only on the AUDIO LOCK: timeline 101.900s vs V1 mp4 100.833s (|Δ|=1.067s > 1.0).
Fix ($0, no new TTS): set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler
rebuilds from this build's own 14 mp3 segments (present in the V1 audio/ dir) instead of
copying the stale V1 mp4 AAC. 0 V2 stills → per PROMPT-AUDIO-FIX.md step 6, ship nothing
visual: board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture runner assembles on
the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 16 beats, ~95 s.

## THE TABLE (count + staging laws)

- TWELVE apostles + Jesus — thirteen at the ring (count law; Judas IS
  present but the betrayal is NOT this row's subject: no empty-seat
  drama, no singled-out shadowed figure — the authored law says the
  ring is complete and warm).
- RECLINING at a low U-shaped table (the 44/74 staging law) — never
  chairs, never the painting-style long straight table with everyone
  on one side (that is a Renaissance composition, not a first-century
  meal; if a render gives the da-Vinci lineup, reject).
- PETER and JOHN auto-attach from global sheets — face-board them
  near Jesus per the beats.

## The bread and the cup (the sacrament frames)

- took/thanked/brake/gave (b06) is TIGHT — hands and bread; the
  breaking readable as one motion.
- ONE great two-handled clay cup — the same cup lifted (b10) and
  passed hand to hand (b12: the travel readable around the ring —
  direction law). Earthenware, nothing gilded (row-7 class).
- No halo/glow on the elements, ever.

## Coverage shape

Four true wides with stated geometry: b02 (the ring complete, camera
behind the near couches), b09 (the giving down the table's length),
b12 (the cup's round in profile), b15 (the hymn — camera behind the
rising company toward the door and the night). Four flips including
b01, the PERSON-FREE laid table.

## Other checks

- Lamplit night throughout (correct story darkness, stated).
- The hymn beat (b15) ends the row on its feet, singing, going OUT —
  toward Gethsemane's night (seeds row 91's opening mood).
- ROOM promote-first from b01 (person-free — ideal plate); its
  approved frame could serve row 90 (washing feet — the same upper
  room, same night: note it there).
- Only Jesus wears cream.


## RUNNER PARK (A-auto Machine A `Dev`, 2026-08-06) — NEEDS-AUDIO / STALE-V1-FINAL — $0 SPENT
Pre-flighted at step 2 BEFORE any credit (no stills generated, nothing to reuse-waste).

**BLOCKER — v2_assemble AUDIO LOCK will fail:** timeline total = 101.900s vs authoritative V1 mp4 `luke-22_the-last-supper.mp4` = 100.833s.
Tripwire(s): RUNTIME |Δ|=1.067s > 1.0 (line 531). V1 mp4 SHORTER than timeline (trailing-silence shortfall).
The AUDIO LOCK copies the finished V1 mp4's AAC stream packet-for-packet; it refuses when the mp4 does not match the recomputed timeline.

**Why the runner cannot fix it:** the fix is `AUDIO_FROM_V1_SEGMENTS = True` in this build's beats_v2.py (rebuilds the track from this build's OWN mp3s at the timeline offsets — nothing re-voiced, V1 stays read-only). Editing beats_v2.py is outside the runner's allowed writes (art / QC.md / boards / SESSION-LOG / review card / mp4 only — PROMPT-OPUS-RUNNER.md hard rails). Same class as parked rows 69/74/77/78/80/82/83.

**FIX (author):** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py  then this row builds normally.

**RESUME after fix:**
```
python3 media-production-v2/v2_story_cast.py build-89-last-supper --ceiling <c>
python3 media-production-v2/v2_gen_api.py build-89-last-supper --ceiling <c>
python3 media-production-v2/v2_assemble.py 89
```

---

## ✅ REALISTIC V2 SHIPPED — A-auto runner (Machine A `Dev`, 2026-08-07, unattended)

**COMPLAINT LEDGER:** none open (`v2_outline.py 89` shows no Cameron complaint). New realistic-V2 first-attempt cut.

**What was built:** 16 realistic stills on the promote-first ROOM plate (s01 promoted → 12 ROOM beats). 0 portraits (PETER/JOHN carry global sheets). AUDIO REBUILD PASS SHA256 29a5b1d0…, 94.1s, 20.1 MB, AUDIO_FROM_V1_SEGMENTS (14 V1 mp3s, byte-identical narration — no re-voice).

**Rerolls (2/16 = 12.5%, within ≤15% COST-LAW budget):**
- b02 (establishing wide) — first take rendered PAINTERLY/illustration (Law-14 realistic/cartoon MIX) with a hooded lighter-haired Jesus + a room the plate had been payload-dropped from; reroll landed a photographic take matching the set, complete warm ring, only-Jesus-cream.
- b06 (took the bread) — first take was a 4-panel COLLAGE (RUNNER-LESSONS collage class); reroll landed a single coherent bread-breaking frame on the ROOM plate.

**Row spend ≈ $2.15 (b01 anchor $0.13 + 15 beats $2.01 + 2 rerolls $0.27), meter → $472.89. WELL under the $6.10/row running average — COST LAW trend DOWN.**

**STALE-WINDOW REMAP (runner timing-only, row-42/row-74 class, no re-voice/reroll):** beats_v2 windows were scaffolded on the old ~101.9s timeline; live audio is 94.129s (card_start 86.979). First assemble placed stills on the stale windows → b16's window (88.66-93.30) started AFTER live card_start, so **s16 (the person-free "bread and cup remain" closer) was dropped** and its n5 caption landed over s15 (the hymn); video_silent 95.9s vs audio 94.13s. FIX: remapped all 16 windows onto the live extract per-segment slices (piecewise-linear, split ratios preserved for the 3 multi-beat segments n1/n2b/n4; b16 → 81.132-86.979). Re-assembled: video_silent 94.133 == audio 94.129, **AUDIO SHA256 UNCHANGED (29a5b1d0…)** proving audio byte-identical. Verified in rendered mp4: s16 shows at 0:83 with its matching caption, card clean at 0:88.

**FIX-WAVE:** the promoted ROOM plate (s01) carries a small period-ambiguous fork among the table utensils; it propagates to the wide ROOM frames (s05/s09/s10/s12/s16). Background, non-subject; rerolling re-attaches the plate, so left for the fix wave.

**Face/beard/scale/anatomy:** PETER/JOHN held by global sheets; only Jesus cream throughout; lamplit night throughout (correct story darkness); Jesus green/hazel eyes are the baked V2 ref (NOT rerolled — systemic). Sacrament frames (s06 break, s07 body, s10/s11 cup, s08 hands insert) read correctly.
