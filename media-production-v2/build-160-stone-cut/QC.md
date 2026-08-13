# QC / RUNNER HANDOFF — build-160-stone-cut (Daniel 2:31-45)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 21 beats, ~146 s. The unstoppable-kingdom row (BRIDGE).

## WITHOUT HANDS (absolute — the row's whole doctrine)

The stone is NEVER touched by any hand, chisel, tool, workman or army
in ANY frame — it breaks free alone (b08), strikes alone (b09), grows
alone (b11/b12). NO divine hand either — that is the point. b07 is
the doctrine insert: the fresh break-socket with NOT ONE tool mark
and the slope empty of anyone. Any hand/tool/figure at the stone, at
any scale, = automatic reject. The mountain stays tool-markless too
(b17/b18 — the b07 rhyme at mountain scale).

## Two worlds, never mixed

COURT frames (b01/b02/b13/b16): lamplit Babylonian throne hall, deep
night. DREAM frames (everything else): the vast amber plain. No court
figure ever stands in the dream; the dream is never a wall-painting
or vision-bubble inside the court. Time arc: lamplit night court →
amber twilight dream → morning mountain → full-dawn close.

## The statue (prop-board it)

Metals in scripture order, NEVER shuffled: GOLD head, SILVER chest/
arms, BRONZE belly/thighs, IRON legs, IRON+CLAY feet. It is a STATUE
— its fall harms nobody; NO people or armies anywhere on the plain.
b09: the stone strikes the FEET, never head or chest. b10: the dust
STREAMS AWAY on wind (the chaff clause). By b20 not one metal glint
remains anywhere.

## The people are dignified

The king's trouble is sleepless gravity, never weakness or
caricature; b16 he is SOBERED, not humiliated. The wise men's failure
is the EMPTY floor before the dais (b01) — no mocked men rendered.
Daniel explains calmly, never gloats — the plainest robe in Babylon
(slate-grey; never cream — no Jesus beats in this row).

## Sequence reads as motion (lesson 12)

b05 small far point → b06 stone standing FREE beside its fresh
break → b07 empty-socket insert → b08 mid-descent with kicked dust
(travel RIGHTWARD toward the statue) → b09 strike at the feet →
b10 collapse with wind → b11 grown, alone → b12 mountain touching
BOTH frame edges. Check the stone is the SAME rough grey rock at
every size.

## Coverage shape

One true wide with stated geometry: b01 (camera low at the hall's
far end, columns' backs nearest the lens, lines exiting far centre).
File order = story order; windows contiguous 0.28–145.63. One
drift-word FAIL ('glow') caught and fixed pre-ship.

- Plates: NO stash match — four NEW places, promote each from its
  first good frame:
  `python3 media-production-v2/v2_stash.py --promote build-160-stone-cut COURT <frame>` (from b01)
  `python3 media-production-v2/v2_stash.py --promote build-160-stone-cut DREAM-PLAIN <frame>` (from b03)
  `python3 media-production-v2/v2_stash.py --promote build-160-stone-cut STATUE <frame>` (from b03)
  `python3 media-production-v2/v2_stash.py --promote build-160-stone-cut STONE <frame>` (from b06)
  STATUE and STONE are effectively PROP tokens — if the stash ever
  auto-suggests a place-frame for them from another build, REJECT
  (the row-157 person/prop wiring lesson).

---

## 🅿️ RUNNER PARK → NEEDS-AUDIO (Opus runner, Machine A `Dev`, 2026-08-13, $0/0 gen)

**STALE-V1 — parked before ANY credit (the $0 audio pre-flight caught it).**
`v2_assemble.assert_v1_final_is_current(160,…)` FAILS: the authoritative V1 mp4
`media-production/build-160-stone-cut/daniel-2_stone-cut-without-hands.mp4` was
rendered **2026-07-24 10:15:29**, but **11 of the 11** narration mp3s it would
lock to are NEWER (n1/n2/n3/kv45/n4/n5 … all **2026-07-28 15:56:26**) — the
whole OT-block re-voice-over-old-mp4 pattern (row 141/147 class). Duration diff
is only −0.086 s, so the loose ≤1.0 s heuristic passes; the real guard trips on
the newer-mp3 tripwire. Copying the V1 mp4 audio would ship stale voices.

- `v2_prompt.py build-160-stone-cut --check` = PASS (21 beats, v4).
- `.approvals.json` "160" NOT PRESENT → not approved, not complained.
  **COMPLAINT LEDGER: none open.**
- 0 stills generated (parked at pre-flight — no meter touched).

**RESUME (audio lane, PROMPT-AUDIO-FIX, $0, no Gemini):**
1. Voice-ID the 11 V1-dir mp3s (`media-production/build-160-stone-cut/audio/*.mp3`)
   — confirm ElevenLabs new-voice (44100/128k) as on rows 155/156/157.
2. Add `AUDIO_FROM_V1_SEGMENTS = True` to
   `media-production-v2/build-160-stone-cut/beats_v2.py`.
3. Board State NEEDS-AUDIO → AUTHORED, Ready ✅, Claim BLANK (no stills yet →
   hand to picture runner). Then the picture runner generates the 21 stills +
   promotes the 4 NEW plates (COURT/DREAM-PLAIN/STATUE/STONE — STATUE & STONE
   are PROP tokens, reject any auto-place suggestion) and ships.

---

## ✅ AUDIO FIXED → AUTHORED (AUDIO-FIX lane, Machine A `Dev`, 2026-08-13, $0/0 gen)

**Resolved the STALE-V1 park. No Gemini, no ElevenLabs — pure config + verify.**

1. **Voice-ID:** all 11 V1-dir mp3s
   (`media-production/build-160-stone-cut/audio/{n1-n8,kv44,kv45,card}.mp3`)
   ffprobe **44100 Hz / 128 k** = ElevenLabs new-voice (matches rows 155/156/157).
   No old edge-tts (24000/48k) segment anywhere → no mid-video voice swap risk.
2. **Set `AUDIO_FROM_V1_SEGMENTS = True`** in `beats_v2.py` (after the docstring)
   so the final track is rebuilt from these current mp3s instead of packet-copied
   from the stale 2026-07-24 V1 mp4. $0.
3. **$0 audio pre-flight PASS** (before any credit, no assembly):
   - `v2_prompt.py build-160-stone-cut --check` = PASS (21 beats, v4).
   - All 11 referenced segs (n1,n2,n3,kv45,n4,n5,n6,kv44,n7,n8,card) map to
     existing mp3s — 0 missing.
   - Timeline contiguous, **no overlaps**; card audio_start 146.135 + 15.282
     dur = 161.417 end ≤ total 162.519 → **last beat/card will NOT drop** at
     assembly (guarded against the dropped-last-beat trap).
4. **Board:** NEEDS-AUDIO → **AUTHORED**, Ready ✅, Claim BLANK. 0 stills exist,
   so nothing visual ships from the audio lane — the picture runner now generates
   the 21 stills on this corrected audio + promotes the 4 NEW plates and ships.
   **COMPLAINT LEDGER: none open** (`.approvals.json` "160" absent). This park was
   a self-caught pre-flight guard, not a Cameron complaint — so there is no review
   card to answer; the fix simply unblocks the row for the picture runner.

---

## 🅿️ RUNNER PARK — TRANSIENT gemini-3-pro-image OUTAGE (Opus picture runner, Machine A `Dev`, 2026-08-13, $0/0 gen)

**Parked before any frame — board-wide endpoint outage, NOT a billing wall.**
Claimed row 160 (lowest empty-claim Ready row; 155/156/157 have filled audio-fix
claims → left to their pickup lane per PARALLEL-LANES rule #1). Pre-flight all
green: `AUDIO_FROM_V1_SEGMENTS=True` present, `v2_prompt.py --check` PASS (21
beats v4), COMPLAINT LEDGER none open (`.approvals.json` "160" absent).

**Blocker:** the `gemini-3-pro-image` endpoint is hanging every gen call
indefinitely (no read-timeout, RUNNER-LESSONS 1378). Evidence, measured:
- `api-spend.jsonl` last board-wide frame = **2026-08-13 12:22:14** (row 159 b01);
  now 13:29 → **67+ minutes, ZERO frames from ANY lane** = board-wide, not local.
- Two full `v2_story_cast build-160` runs + one 90 s `timeout` probe (DANIEL) all
  hung producing 0 frames, 0 spend (exit 124). Key HEALTHY / billing FINE — no
  429, no "prepayment credits depleted"; this is the SAME transient outage that
  parked row 159 at 12:22 (its QC: "board-wide 16min+ zero frames, NOT prepay").
- Nothing banked for 160 (0 stills, 0 portraits) → clean hand-back, no strand.

**Board:** State RUNNING → **AUTHORED**, Claim **BLANK**, Ready **✅** (unchanged)
so the next picture-runner session (or autopilot) re-picks it fresh the moment the
endpoint recovers. No inbox escalation (transient endpoint, self-recovers — row
159 precedent; no top-up needed).

**RESUME (picture runner, once gemini-3-pro-image is answering):**
1. `python3 media-production-v2/v2_story_cast.py build-160-stone-cut --ceiling <meter + 4.7 + 25>` (2 portraits DANIEL/KING → writes REFS).
2. Promote-first the 4 NEW plates: COURT (b01), DREAM-PLAIN (b03), STATUE (b03), STONE (b06). STATUE & STONE are PROP tokens — reject any auto-place suggestion.
3. `python3 media-production-v2/v2_gen_api.py build-160-stone-cut --ceiling <…>` (21 beats).
4. Light QC + FULL-CUT GATE (watch: WITHOUT-HANDS = no hand/tool/figure at the stone EVER; statue metal order gold→silver→bronze→iron→iron+clay; b02 metals-list = collage/panel/diptych magnet; person-free b07 socket = floating-figure risk; no embodied-Jesus/God drift on closing kingdom frame; OT = no cream). Assemble (AUDIO REBUILD PASS), ship, deploy, live-verify.

---

## 🅿️ RUNNER PARK — gemini-3-pro-image OUTAGE STILL ONGOING (Opus picture runner, Machine A `Dev`, 2026-08-13 ~13:50, $0/0 gen)

**Third confirmation of the board-wide endpoint outage. Parked before any frame.**
Pre-flight all green: `AUDIO_FROM_V1_SEGMENTS=True` present, `v2_prompt.py
build-160-stone-cut --check` PASS (21 beats, v4), `.approvals.json` "160" absent.
**COMPLAINT LEDGER: none open.**

**Blocker (measured this session):** `gemini-3-pro-image` still hangs every gen
call indefinitely (RUNNER-LESSONS 1378 — no read-timeout).
- `api-spend.jsonl` last board-wide frame = **2026-08-13 12:22:14** (row 159 b01);
  now ~13:50 → **~95 minutes, ZERO frames from ANY lane** = board-wide, not local.
- Two `v2_story_cast build-160 --ceiling 741` probes (120 s and 300 s foreground)
  both hung → **0 portraits, 0 frames, 0 spend** (exit 124/143). Meter unchanged
  **$711.00**. Key HEALTHY — no 429, no "prepayment credits depleted"; pure hang.
- 0 stills / 0 portraits banked → clean hand-back, no strand. Board left
  **AUTHORED / Ready ✅ / Claim BLANK** (never flipped RUNNING — nothing banked).

Taking "the next Ready row" is futile while the outage is board-wide (every row
draws the same endpoint). Re-pickable by any picture lane the instant the endpoint
recovers (first fresh `api-spend.jsonl` frame from any lane = recovered).

**RESUME (picture runner, once endpoint recovers):**
`python3 media-production-v2/v2_story_cast.py build-160-stone-cut --ceiling <meter+ (21+2)*0.134*1.5+25>`
then `v2_gen_api.py build-160-stone-cut --ceiling …`, promote COURT (b01) /
DREAM-PLAIN (b03) / STATUE (b03, PROP) / STONE (b06, PROP), FULL-CUT GATE, ship.
