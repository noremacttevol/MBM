## 🛠 C-FIX SHIPPED — Cameron's 3 picture complaints (0:40 white faces / 0:47 multiple arms / 1:19 Jesus missing a hand) — 2026-08-13, Machine A `Dev`, Opus runner (unattended/headless)

**Cameron's complaint (against the live cut, complaintHash a62787cfb):**
"0:47 man has multiple arms replace the picture, 0:40 picture some bystanders have
white faces, fix it replace it. 1:19 picture has Jesus missing a hand, fix it."

### TRACE (each timestamp → the frame that RENDERS at that second in the live mp4)
- **0:40** → beat **b04** `s04-you-are-the-branches` (window 39.26–40.65). Several
  bystanders in the moonlit crowd rendered with cold grey/ashen/white faces.
- **0:47** → beat **b09** `s09-branches-part-of-the-same` (window 43.17–46.63, held
  through the 46.63–48.11 gap). The foreground brown-tunic figure read as having a
  THIRD arm (hoe over shoulder + reaching arm + a billhook hand tangled into him).
  NOTE: the adjacent b08 (`s08`, ~0:41) is a *different* frame — its arms are hidden
  behind foliage and on-brief (hired hands leaving, golden dusk); left untouched.
- **1:19** → beat **b14** `s14-he-asking-for-effort-he` (window 73.68–78.39; 1:19
  rounds to this last picture before the card). Jesus's clasp merged/hid a hand
  ("missing a hand") AND the frame rendered near-black / unreadable.

### PROMPT AUTOPSY (rubric meta-law 3) — verdict per frame
- **b04 = ALLOWED.** The moonlit-night register + ZERO skin-tone constraint let the
  generator drain several disciple faces to grey/ashen. Fix = add the missing
  constraint: `must_show`/`scene`/`must_not_show` now require every disciple's face
  to keep warm living olive/tan Middle-Eastern skin, softly moonlit — never grey,
  ashen, pale, white, bluish or drained.
- **b09 = ALLOWED (+ off-brief + wrong time-of-day).** The count line "two arms, two
  hands and one head" was present but insufficient: a from-behind figure shouldering
  a tool while also reaching invited a spare-limb read, and the frame rendered
  golden-day walking-workers when the brief was moonlit hands-on-branches. Fix =
  recompose to the ACTUAL brief (TIGHT waist-up of 2–3 disciples' hands resting on
  ONE trained branch, night), and forbid tools/baskets/walking-away and any extra,
  third, duplicated, floating or disembodied arm/hand — which also de-duplicates
  from s08.
- **b14 = ALLOWED.** The complex "three of them joined in one quiet stack" hand
  composition merged a hand (reads as missing), and "moonlight" with no readability
  floor rendered near-black. Fix = simple readable clasp with BOTH of Jesus's hands
  fully visible (five fingers each), and an explicit brightness floor ("clearly
  VISIBLE in soft moonlight — not a near-black or unreadable frame," still night, not
  sunset/sunrise).

### FIX + FULL-CUT GATE (6b) — the whole rendered cut re-checked, one frame per beat
- **3 rerolls** (b04, b09, b14 = **3/14 = 21%**, ~**$0.40**). These are mandatory
  complaint-fixes, exempt from the discretionary ≤15% reroll budget; the rest of the
  cut was reused untouched (no re-pull). Meter $633.95 → $634.36.
- **Verified in the RENDERED mp4:** 0:40 crowd now all warm olive faces; 0:47 now a
  clean close-up of three distinct men each with one whole hand on one branch, at
  night; 1:14–1:18 Jesus clasps the disciple with BOTH hands (five fingers each),
  frame clearly lit. The other 11 beats were extracted at true mid-window and viewed
  — all clean (Jesus locked face + cream-only + no halo on b01/b02/b07/b10/b14;
  green-cut vs withered pair correct; grapes read as much fruit; captions bottom-band
  only; closing card clean). **14/14 PASS.**
- **AUDIO LOCK: byte-identical.** AUDIO REBUILD PASS SHA256 `ae063a39…` — same hash as
  the prior ship; nothing re-voiced. 84.8s / 20.5 MB.

### COST LAW / LEARNING LAW
- Cost this touch ~**$0.40, 0 audio $** — far under the $6.10/row average → trend DOWN.
- New RUNNER-LESSONS + rubric lesson: (a) any moonlit/night crowd needs an explicit
  warm-skin constraint or faces drain grey ("white faces"); (b) the count line alone
  won't stop a spare limb on a from-behind tool-carrying figure — a close hands frame
  with a "no disembodied/third arm" clause is the durable fix; (c) a "moonlight" beat
  needs a readability floor or it renders near-black.

---

## 🚢 PICTURE RUNNER SHIP — realistic-V2, 14 stills over the audio-fixed track — 2026-08-13, Machine A `Dev`, Opus runner (unattended/headless)

Built the 14 realistic-V2 stills over the already-audio-fixed track (the audio lane's
"abideth" re-voice, below) and shipped in ONE touch. `--check` PASS; 14/14 generated
first-attempt, **0 rerolls (COST LAW budget was 2 = 15% of 14; used 0)**; ~**$1.88**,
meter $622.16 → $624.17. AUDIO REBUILD PASS SHA256 `ae063a39…`, 84.8s, rebuilt from
12 V1 segment mp3s (incl. the corrected j1b). 0 portraits (Jesus = global V2 ref;
DISCIPLES is an earth-tone band, no face lock). VINEYARD plate = build-23 b03 (wired,
present). Well under the $6.10/row average → COST LAW trend DOWN.

### COMPLAINT LEDGER (LEARNING LAW)
- **OPEN (`v2_outline.py 146`): "Abideth is pronounced wrong." → FIXED, and verified byte-present in THIS ship.**
  The audio lane (2026-08-11) re-voiced segment `j1b` (John 15:5b, Jesus red-letter,
  beat b10 / s10) through the LOCKED ElevenLabs Jesus voice (Chris), respelling
  "abideth" so it now reads **/uh-BY-deth/** (long-i, three syllables — the KJV
  pronunciation, not the old "a-BID-eth"). `AUDIO_FROM_V1_SEGMENTS=True` makes the
  assembler rebuild the track from the V1-dir mp3s, so the corrected take ships.
  **Proof it shipped:** V1-dir `audio/j1b.mp3` md5 = `a4bb0de3…` (the corrected take,
  not the old `910b8468…`), and this mp4's audio was rebuilt from it (AUDIO REBUILD
  PASS). The s10 caption keeps the KJV spelling "abideth" and is in sync with the
  corrected audio. The reviewer card tells Cameron his complaint is fixed in his terms.

### FULL-CUT GATE (6b) — all 14 beats from the RENDERED mp4 + 3 caption frames + card = PASS
- Realistic biblical photography throughout (Law 14) — **zero cartoon/mixed** frames.
- Jesus ONE locked face across s01/s02/s04/s07/s10/s14: olive skin, dark wavy
  shoulder-length hair, full dark beard, calm warm eyes (ref-true — NOT edited;
  rubric lesson 20), **cream robe only on Jesus** in every frame; no halo/glow/rim-light.
- Scale gate PASS (Jesus ordinary-sized, never a giant); night moonlit register on the
  Jesus teaching beats (moon/stars, physical light), golden-day light on the vineyard
  vignettes — matches the authored time-of-day arc. b14 close in deep blue twilight.
- Anatomy/hands natural (incl. s10 both hands cupping the grape cluster, s14 the
  skin-on-bark-on-skin clasp); period props only — clay oil lamps (s01), viticulture
  billhooks + grape basket (s08); **no modern objects, no collage, no rotation, no
  lens-stare, no second cream figure, no ghost ropes**.
- Grapes read as "much fruit" (s10/s13); green-cut vs withered branch pair correct
  (s11 fresh-green cut / s12 withered brown).
- Captions bottom-band only, split/synced, **RED** for Jesus KJV lines (j0/j1a/j1b —
  incl. the "abideth" line on s10), **WHITE** for narrator; none cover the art.
  Closing question card clean, well-margined ("Stay connected to the Vine…").

Row Built ✅; Appr/Post untouched (Cameron's alone). Ship = two commits (mp4+boards, then
card repoint), Firebase deploy + live-verify.

---

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
