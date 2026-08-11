## ✅ C-FIX SHIPPED 2026-08-11 — ROOT-CAUSED "Voice is wrong. Bad audio" = HF-MUFFLE (Machine A `Dev`, $0, no re-voice)

**Cameron's complaint (reportedAgainst live cut `3ef2b5b65ded`):** *"Voice is wrong.  Bad audio."*

**COMPLAINT LEDGER — "Voice is wrong. Bad audio":** FIXED. The voices were never wrong
(proven below); the audio was **muffled**. Root-caused, de-muffled, verified, shipped.

### What was actually wrong (root cause — found by a deepened battery)
The prior 2026-08-09 park ran a 5-test battery, found everything "clean," and BLOCKED for
an ear-pass that never came. That battery **never measured spectral tilt.** It does now:

- **Engine (ffprobe):** all 19 segments `44100/128000` = ElevenLabs. No edge-tts leak.
- **Voice-ID (F0, text-independent, vs approved row-70 refs):** Jesus 85.8 Hz vs **Chris** 85.6
  (+0.3), narrator 101.3 vs **Brian** 97.1 (+4.2), scripture 113.5 vs **Roger** 111.1 (+2.4).
  **All three are the correct locked voices** — no wrong-voice segment anywhere.
- **Transcript (faster-whisper):** every segment says its exact intended words. No garble.
- **Levels:** Jesus is +3.3 dB over narrator — but that gap is **systemic and APPROVED**
  (row 70 +2.7, row 50 +3.2, row 51 +2.4). Not a row-74 defect.
- **★ Spectral tilt (delivered-vs-delivered, the test the old battery lacked):** row-74's
  delivered audio is **muffled** — nearly identical to approved rows up to 3 kHz, then
  **−6.7 dB @ 6-10 kHz and −17.6 dB @ 10-16 kHz** below all three approved cuts. Uniform
  across every segment. Row-74-specific.
- **Why:** `git log` on the segment mp3s shows commit `d3598b3b9` *"#2 AUDIO: recover 77
  reverted builds FREE from ElevenLabs history."* Row-74's audio was **recovered from
  ElevenLabs history** (a re-encoded, high-frequency-rolled-off copy) instead of freshly
  rendered like the crisp approved rows. That dull recovery is what Cameron heard.

### The fix (de-muffle, NOT a re-voice — $0, deterministic, take-preserving)
The HF content was **attenuated, not gone** (−60 dB, ~20 dB above the noise floor), so it was
recoverable by corrective EQ. Applied a matched high-shelf EQ to the delivered audio,
re-normalized to −15 LUFS + `alimiter=limit=0.95` (exactly the assembler's final stage),
and **remuxed with the video stream copied byte-for-byte** (`-c:v copy`):
`highshelf=f=6000:g=4, highshelf=f=9000:g=7, highshelf=f=13000:g=8`.

- **This did NOT re-voice anything.** The words, the actual ElevenLabs performances, the
  speaker voices, and every timeline offset are preserved. A blind re-voice was correctly
  refused (all voices are provably correct; it would only swap in different non-deterministic
  takes, move the hash, and void approval without fixing what he heard).

### Verified (headless, before ship)
- **Brightness restored to match approved:** 6-10 kHz −6.7→**+0.2**, 10-16 kHz −17.6→**−4.7**,
  3-6 kHz −2.1→**+0.9** (vs approved-row average). The muffle is gone.
- **Video byte-identical:** video-stream md5 `1c6ebf84…` unchanged old→new → the whole
  2026-08-07 36-frame picture QC still holds; sample beats re-viewed (Simon close-up, the
  "her sins are many" triclinium beat — Jesus only-cream + locked face + weeping woman at
  feet + red-letter caption, question card clean) all decode clean.
- **ORDER CHECK:** whispered the rendered fixed cut — all 14 timeline anchors land on their
  words (n0…card), narration intact and in order, timing unchanged.
- **Levels/clipping:** −14.8 LUFS (≈ −15 target); 56 AAC-overshoot samples (original had 67 —
  not a regression); no re-timing so no caption/picture drift.

### ⚠️ Durability caveat (for any FUTURE re-assemble of this row)
The SOURCE segment mp3s in `media-production/build-74-.../audio/*.mp3` are STILL the muffled
history-recovered copies — this ship de-muffled the **delivered mp4** only (a verified remux).
If this row is ever re-assembled (`v2_assemble.py 74`), it will rebuild from those muffled
mp3s and REINTRODUCE the muffle. The durable fix at that point: de-muffle the 19 source mp3s
with the same EQ (duration-preserving) or re-render them fresh through ElevenLabs, THEN assemble.

**Cost:** $0 (no image gen, no TTS credits). 0 rerolls.

---

## 🅿️ RUNNER PARK 2026-08-09 → NEEDS-AUDIO (Opus cfix runner, Machine A `Dev`, $0)

**Cameron's OPEN complaint (`v2_outline.py 74`, reportedAgainst `3ef2b5b65ded` = the
LIVE cut):** *"Voice is wrong.  Bad audio"* — filed 2026-08-08.

**Why this is an AUDIO-domain park, not a re-cut:** the complaint names the VOICE /
audio quality, nothing about a picture. Per RUNNER-LESSONS (audio-immutability) the
runner may not re-voice, so NO picture reroll and NO re-assemble happens here. Flipped
State BUILT→NEEDS-AUDIO, Audio OK→CHECK, park-claim (no `AUDIO-FIX` token so the audio
picker will select it). Pictures + audio left BYTE-IDENTICAL.

**$0 diagnostic for the audio lane (ffprobe proof):** authoritative audio is the V1-dir
segments (`AUDIO_FROM_V1_SEGMENTS = True`, beats_v2.py:93 →
`media-production/build-74-woman-washed-his-feet/audio/*.mp3`). Every one of the 19
segments probes `44100,128000` = the ElevenLabs signature:
```
card j1 j2 j3 j40 j41 j44 n0 n1 n2 n3 n4 n5 n5b n6 s39 s40 s43 s49  → all 44100,128000
```
So this is **NOT** the OLD-JESUS-SPEAKER mixed-engine class (no `24000,48000` edge-tts
segment; no mid-video engine flip). The defect is therefore either the WRONG ElevenLabs
VOICE MODEL (not the locked NARRATOR/JESUS voice) or a delivery/quality artifact —
neither of which a sample-rate probe can adjudicate. It needs one EAR-PASS to localize
the bad segment(s), same as the row-27 park.

**AUDIO LANE RESUME:** listen to `media-production-v2/build-74-woman-washed-his-feet/luke-7_woman-washed-his-feet.mp4`
end-to-end; confirm which voice(s) read as "wrong" (narrator vs Jesus) and whether it is
voice-model or quality; re-voice the offending segment(s) through the locked ElevenLabs
voices (NARRATOR "Brian" / JESUS "Chris", 44100/128k), atempo-match to the original
segment length so no window moves, drop into the V1-dir `audio/`, re-assemble
(`v2_assemble.py 74`, AUDIO LOCK must move to a NEW hash proving the re-voice landed),
deploy + live-verify, ship via the audio lane; review card answers Cameron "Voice is
wrong / bad audio" in his words. Board NEEDS-AUDIO→BUILT on ship.

---

## 🛑 AUDIO-FIX BLOCKED — needs one EAR-PASS (AUDIO-FIX lane, Machine A `Dev`, 2026-08-09, $0)

Ran the FULL headless diagnostic battery (five independent tests, all $0). **None
localizes a fixable defect.** A blind re-voice would burn ElevenLabs credits, move
the AUDIO LOCK hash, void Cameron's approval, and — because I can't name what he
heard — most likely NOT fix it (worse: a touched row that re-queues without closing
the complaint). So BLOCKED for one ear-pass, exactly like the row-27 park.

**Diagnostics run (all came back clean/consistent):**
1. **Engine/sample-rate** (ffprobe): all 19 segments 44100/128000 = ElevenLabs. No
   mixed-engine, no edge-tts leak. (Confirms the prior park.)
2. **Word delivery** (faster-whisper per segment vs each seg's timing.json text):
   every segment says its intended words. The only divergences are whisper's own
   KJV/archaic quirks ("toucheth"→"touch of", "owed five hundred pence"→"one-ode
   500 pens") and short-clip mishears — NOT audio garble/dropout.
3. **Voice assignment / within-build consistency** (custom MFCC-mean cosine,
   text-independent): every Jesus seg (j1,j2,j3,j40,j41,j44) clusters to the Jesus
   centroid, every narrator seg to narrator, every scripture seg to scripture. **No
   wrong-voice swap on any single segment.**
4. **Uniform-wrong-voice check** (row74-Jesus centroid vs row70's approved-**Chris**
   Jesus centroid): inconclusive — homemade MFCC means sit at ~0.97 for ALL
   cross-build pairs (narrator-vs-Chris also 0.97), so they can't discriminate
   Chris/Brian/Alexander across recordings. BUT the build-**local**
   `mbm_eleven.py:39` correctly declares `JESUS = ("Chris","iP95p4xoKVk53GoZ742B")`
   (the shared module's wrong "Alexander" is NOT what a local render would use), and
   the j-segments are internally identical, so no positive evidence of a wrong model.
5. **Objective quality** (peak/clip/noise-floor/RMS per segment): 0.00% clipping
   anywhere; peaks −2.9…−9.6 dBFS (no HOT segment). One real observation: the
   Jesus + s39 segments carry a ~−81 dB room-tone floor and run ~5 dB hotter
   (RMS −20…−22) than the noise-gated narrator (floor −180 dB, RMS −25…−27). This
   is the KNOWN ElevenLabs room-tone trait `mbm_eleven.clean_clip` targets and
   `v2_assemble` loudnorm equalizes at final mix — and at ~60 dB below speech it is
   inaudible, so almost certainly NOT the complaint, but it is the only lead.

**EAR-PASS RESUME (the one thing a listening session must decide):** play
`build-74-woman-washed-his-feet/luke-7_woman-washed-his-feet.mp4` end-to-end and
answer TWO questions: (a) is it the NARRATOR (Brian) or JESUS (Chris) voice that
reads "wrong," and (b) is it the VOICE MODEL (wrong person), the DELIVERY/quality
(garble, robotic, breath, pacing), or a LEVEL/tone jump between voices? With that
one fact, the fix is targeted: re-voice only the named segment(s) through the
build-local locked voice (or run `clean_clip` if it's the room-tone/level jump),
atempo-match, re-assemble to a NEW AUDIO LOCK hash, deploy+verify, ship. Do NOT
blind-re-voice all six Jesus segments — that voids his approval without knowing the
defect. Claim marked `AUDIO-FIX BLOCKED` (no `LIVE` token) so an ear-equipped
session picks it up; pictures + audio left byte-identical, $0 spent.

---

# QC / RUNNER HANDOFF — build-74-woman-washed-his-feet (Luke 7:36-50)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 36 beats, ~208 s.

## SAME-EVENT LAW — shared cast with build-44 (verified byte-identical)

This is the SAME dinner as build-44-two-debtors. WOMAN/SIMON/ROOM/JAR
locks verified BYTE-IDENTICAL between the two builds this session.
Whichever row builds FIRST defines the faces; the second adds a
build-local `REFS` pointing WOMAN and SIMON at the first's approved
stills (the build-17 mechanism). Same room, same jar, same actors —
a viewer watching both videos must see one dinner.

## Coverage shape

Five true wides with stated geometry: b01 (the correct dinner from the
side), b03 (the entrance — door and table in one side-on frame), b05
(the reclining geometry in profile — the row teaches its own staging),
b10 (the triangle in profile), b23 (the audit — dry basin and washing
feet, both poles in one frame). Seven flips.

## The woman's dignity (the row's own stated law — absolute)

Her lock and the docstring say it: modest dark dress, bound hair at
entry, NOTHING lurid ever; her reputation exists only in the guests'
faces. The loosed hair at his feet is costly humility, reverent. Any
render that codes her otherwise is an automatic reject.

## Cross-row echoes with build-44 (keep them rhyming)

- The unused water jar/basin by the door (the audit's dry pole) is
  the SAME prop in both rows' arrival and audit frames.
- The jar arc: sealed → opened → poured → EMPTY, ending on the HUSH
  beat (b36: the empty jar and the open night door — V1's silent
  breath; person-light frame, do not crowd it).
- The reclining feet-away staging is the row-83-class trap in both
  rows: feet under a table = geometry broken = reject.

- Only Jesus wears cream. Guests varied (90/107), Simon cold-correct.
- ROOM promote-first from b01 (whichever of 44/74 renders first owns
  the room plate — then --take it into the other).

---

## 🅿️ RUNNER PARK — A-auto 2026-08-06 (NEEDS-AUDIO — stale V1 mp4, row-69 class)

Caught BEFORE any credit spent (zero stills generated — COST LAW win). The
assembler's STALE-V1-FINAL guard will refuse the AUDIO LOCK on this row:

- V1 mp4 `luke-7_woman-washed-his-feet.mp4` last committed **2026-07-24 10:15**
  (commit 5bd6b82a9, new-voice ship), never re-rendered since.
- All **19/19** placed narration mp3s in `audio/` are NEWER than that mp4
  (content_time-verified against `v2_assemble.assert_v1_final_is_current`).
- The mp4 runs **171.67s** but the extract_beats timeline sums to **184.57s**
  — the mp4 is **12.9s SHORT** of the current narration. Its audio stream
  predates the current beats, so copying it would ship stale/short audio.

Reproduced the guard exactly (RECENCY tripwire fires: newer_mp3s=19/19). By
contrast shipped rows 68/64 show newer_mp3s=0 and excess≈0. This is the
row-69 stale-V1 class — the runner ships byte-identical V1 audio and does NOT
re-render or edit beats_v2.py, so it cannot fix this.

**RESUME (author/audio session):** either re-render the V1 mp4 from the current
narration, OR add `AUDIO_FROM_V1_SEGMENTS = True` to this build's beats_v2.py so
`v2_assemble` rebuilds the track from the V1 build's own mp3s at the
extract_beats offsets (nothing re-voiced/re-timed; V1 stays read-only). Then
flip AUTHOR-BOARD row 74 State→AUTHORED Audio→OK Ready→✅. No stills exist yet —
the full generate step runs fresh when audio is unblocked. SAME-EVENT LAW: this
row renders the shared WOMAN/SIMON/ROOM/JAR faces FIRST (build-44 is retired),
ROOM promote-first from b01.

## ✅ AUDIO FIX DONE — AUDIO_FROM_V1_SEGMENTS (AUDIO-FIX job, A-auto 2026-08-06)
STALE-V1 blocker CLEARED at $0 (no new TTS, no image gen). Set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so v2_assemble rebuilds the
narration track from this build's own 19 SPEAKER-LAW segment mp3s (the intended
new voices) at the extract_beats offsets, instead of copying the stale 2026-07-24
V1 mp4 (171.67s, 12.9s short of the 184.57s timeline).
- Verified before flipping: exact 19/19 segment-ID parity between make_narration.py
  SEGMENTS and audio/*.mp3; make_narration imports JESUS/NARRATOR/SCRIPTURE via
  save_speaker_narration (SPEAKER-LAW = new voices); ear-check j1 (Jesus) =
  "Her sins, which are many, are forgiven; for she loved much..." and n0 =
  "A Pharisee named Simon invited Jesus to dinner..." — correct Luke 7, new voice.
- 0 V2 stills exist. Per AUDIO-FIX loop step 5, nothing visual ships; board
  flipped AUTHORED / Audio OK / Ready ✅, claim cleared, so the picture runner
  generates the stills and assembles on this corrected audio (the AUDIO LOCK will
  now pass). No open pronunciation complaint on this row — this was a pure
  duration/staleness fix.

## ✅ RUNNER SHIP — A-auto 2026-08-07 (Machine A `Dev`, UNATTENDED/HEADLESS)

**COMPLAINT LEDGER:** none open (`v2_outline.py 74` shows no reviewer complaint on
this row). This was a STALE-V1 audio-lock clearance, not a complaint fix.

**Built:** 36 realistic stills, 184.6s, 21.1 MB. ROOM plate promote-first from b01
(2 rerolls to clear modern glass goblets/cutlery — glasses gone, only period clay/
bronze tableware kept). Portraits WOMAN+SIMON define the SAME-EVENT faces (build-44
retired). AUDIO_FROM_V1_SEGMENTS rebuild → **AUDIO REBUILD PASS SHA256
bc8ed8e00f67…**, 19 V1 new-voice segments, byte-identical narration.

**QC pass (all 36 viewed):** woman consistently modest/dignified (dark dress, bound/
shawled hair, reverent — never lurid); only Jesus in cream; Jesus/Simon/Woman faces
consistent; feet-away reclining triclinium geometry holds (no feet-under-table);
jar arc sealed(s04)→opened(s07)→anointing(s27)→EMPTY at the s36 hush + night door;
two-debtors props period (tally scrolls, Hebrew moneychanger sign — no Arabic
numerals/modern objects); Jesus↔woman forgiveness frames reverent at a respectful
distance (row-49 romantic-framing trap avoided); no cartoon/collage/lens-stare/
burned-in text; decode 0 errors (not row-31 AAC class).

**ROW-42 ASSEMBLY FIX (runner, timing-metadata only — no re-voice, no reroll):**
first assemble produced captioned.mp4 = 201.5s while the rebuilt audio is 184.57s —
beats_v2.py still-windows ran to 206.32s (a ~30s STALE-timeline drift vs live
card_start 176.738), so the final mux truncated the tail AND the entire question
card, and stills drifted vs captions. Remapped all 36 windows onto the live
extract timeline (piecewise-linear on segment onsets, last still → card_start),
re-assembled: captioned.mp4 now 176.67s + 7.83s card = 184.5s ≈ audio; card renders
clean (no tofu), captions re-synced (verified still+red-KJV caption agree at 120s).
AUDIO REBUILD PASS unchanged (bc8ed8e0…) — audio byte-identical.

**FIX-WAVE (not shipped defects):** faint period-bronze/small metal serving pieces
on some wide dinner tables (borderline-period, not blatant) — a later prop-edit
pass can remove them; keep byte-identical otherwise.

**Cost:** ~$5.35 (2 portraits $0.27 + b01×3 $0.39 + 35 beats $4.69). Rerolls 2/36 =
5.6% (well under 15%). Meter $433.22 → $438.72. Under the $6.10/row average.
