## ✅ AUDIO FIX DONE — "Abideth is pronounced wrong" RESOLVED — 2026-08-11, Machine A `Dev`, audio lane

**Cameron's complaint: "Abideth is pronounced wrong." — FIXED.** The word "abideth"
in segment **`j1b`** (John 15:5b, JESUS red-letter, beat b10, "He that abideth in
me…") was rendered with the wrong pronunciation. Re-voiced ONLY `j1b` through the
LOCKED ElevenLabs Jesus voice **Chris `iP95p4xoKVk53GoZ742B`** (the same engine +
voice as siblings j0/j1a — ENGINE PARITY law), respelling **"abideth" → "uh-bide-eth"**
so it reads **/uh-BY-deth/** — long-i, three syllables (the KJV pronunciation, NOT
the "a-BID-eth"/short-i it was saying). Every other word/voice/timing is byte-for-byte
the same take pattern; nothing else was re-voiced.

- **Engine check first (hard rail):** `j1b.mp3` = 44100 Hz / 128 kbps / mono =
  ElevenLabs new-voice spec (NOT edge-tts 24000/48k), so this is a real re-voice
  through the SAME engine, not an accidental edge-tts swap.
- **Pacing match:** the fresh Chris take rendered 7.37 s (natural variance); the
  original window is 8.202449 s. Pitch-preserving `atempo=0.898089` stretched the
  new take to **exactly 8.202449 s**, so NO still-window in `beats_v2.py` moves and
  the 84.779 s timeline is unchanged.
- **Word-integrity gate (faster-whisper small.en, beam 5):** the re-voiced segment
  transcribes *"He that abideth in me, and I in him, the same bringeth forth much
  fruit, for without me ye can do nothing."* — all words present, correct order, no
  fusion/dropout.
- **AUDIO BASELINE (the sanctioned re-voice exception to audio-immutability):**
  V1 `audio/j1b.mp3` md5 **`910b8468…` → `a4bb0de3…`**. The V1 final mp4 still
  carries the OLD (mispronounced) take baked into its AAC, so the AUDIO LOCK must
  NOT copy it. Set **`AUDIO_FROM_V1_SEGMENTS = True`** in `beats_v2.py` → the
  assembler rebuilds the track from the V1 build's OWN mp3s (now incl. corrected
  j1b) at the extract_beats offsets. Verified: `rebuild_audio_from_segments` →
  **AUDIO REBUILT 84.779 s, guard |total−track| = 0.0 (PASS)**.
- **Cost:** Gemini $0 (no images). ElevenLabs: 1 segment re-voiced (2 short renders
  — one pacing test + the kept take). Meter untouched (Gemini).
- **0 V2 stills yet →** handed to the PICTURE RUNNER: build the 14 realistic V2
  stills over this corrected audio and ship in ONE touch. **The review card MUST
  tell Cameron his complaint is fixed** — e.g. *"Your complaint 'Abideth is
  pronounced wrong' — 'abideth' now says uh-BY-deth (long-i) at ~0:48 in Jesus's
  line; nothing else in the audio changed."*

---

## 🅿️ RUNNER PARK → NEEDS-AUDIO (pronunciation complaint) — 2026-08-11, Machine A `Dev`, Opus runner  *(resolved above)*

**OPEN COMPLAINT (Cameron, `v2_outline.py 146`): "Abideth is pronounced wrong."**
This is an AUDIO / pronunciation defect, not a picture defect — a picture rebuild
would ship the SAME mispronounced audio and REPEAT the complaint (worst failure).
Per COMPLAINT-FIRST + touch-once, the pronunciation must be fixed BEFORE any picture
ship, and pronunciation/re-voice is audio-lane work (off the runner's write-list).

COMPLAINT LEDGER (what must fix it): the word "abideth" is in segment **`j1b`**
(John 15:5, JESUS red-letter, 8.173s: *"He that abideth in me, and I in him, the same
bringeth forth much fruit: for without me ye can do nothing."*), rendered on beat
**b10** (`s10-he-that-abideth-in-me`). Note: this row's AUDIO LOCK is otherwise
CLEAN (timeline 84.900s vs V1 mp4 84.915s, gap 0.015s) — so `j1b` is likely the
CURRENT shipped audio Cameron heard, i.e. the mispronunciation is live, not stale.

**AUDIO LANE — RESUME (row-22/18 respell pattern):**
1. Listen/verify `audio/j1b.mp3`: confirm "abideth" is mispronounced (expected KJV
   /uh-BY-deth/, three syllables, long-i — NOT "abbi-deth" / "a-BID-eth").
2. Re-voice ONLY `j1b` through the LOCKED ElevenLabs Jesus voice ("Chris",
   iP95p4xoKVk53GoZ742B — edge-tts BANNED for Jesus per SPEAKER-LAW) with "abideth"
   respelled so it says /uh-BY-deth/; keep every other word identical. Pitch-preserving
   atempo-match back to **8.173s** so beat b10's window does not move.
3. Re-assemble → AUDIO LOCK/REBUILD PASS, then hand to the picture runner to build the
   14 realistic V2 stills over the corrected audio and ship in ONE touch (deploy +
   live-verify). The review card must tell Cameron his "abideth" pronunciation is fixed.

Runner did NOT build stills ($0, meter untouched) — building before the audio fix
would waste the touch (windows/audio must be final first).

---

# QC / RUNNER HANDOFF — build-146-vine-and-branches (John 15:1-5)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 14 beats, ~80 s. Sixth and last I AM row of the batch.

## VINEYARD plate accepted (family anchor)

build-23 b03 — the established vineyard family (rows 41/45 wire from
it). The GREAT OLD VINE at the head row is this row's protagonist-
plant: same gnarled trunk in every vineyard frame (prop-board it).

## The no-strain doctrine (b05/b06)

No effort imagery on any branch, ever — laden branches REST; b06's
extreme-close seamless joint is "the whole job description." A
straining/reaching branch render misses the row's point — reject.

## The cut-branch pair (b11/b12/b13)

SAME branch, same stones, position rhyme: fresh-green-strong →
withered grey-brown; the cutting itself NEVER shown. b13 stacks
both outcomes in one frame (laden above, withered below).

## Light discipline

Jesus beats at moonlit night (the upper-room walk — 137's grove
register, all light physical); vignettes in golden day BY DESIGN;
b12 flat dry noon; b14 back at night.

## Coverage shape

One true wide with stated geometry: b01 (camera behind the
disciples' cloaked backs at the wall). Seven Jesus beats (b01, b02,
b04, b07, b10, b14 + b07's composition joins him-to-trunk and
them-to-branches). b08's hired hands are ordinary workers, not
villains. File order ≠ story order (b04 at 39s, b05 at 22s) —
build by WINDOW.

- b14's close: the three-layer clasp (skin on bark on skin) —
  gentle, an offer.
