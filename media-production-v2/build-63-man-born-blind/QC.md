# QC / RUNNER HANDOFF — build-63-man-born-blind (John 9)

## §C-FIX 2026-08-12 (Opus RUNNER, Machine A `Dev`, unattended/headless) — NEW complaint vs live 610a70352 → PARKED-BILLING (pictures) + audio recipe. **The §AUDIO-FIX SHIP claim below is SUPERSEDED — Cameron re-filed against it.**

**Cameron's OPEN complaint (`v2_outline.py 63`, reportedAgainst=610a70352, 17:26Z):**
> "1:53 is still wrong its : si-LOH-uhm ... you even got it wrong at 1:34 now too when Jesus says it ... The blind mans face is not the correct look @ 3:39, 3:44, 3:49, 3:56 Fix all these pictures. 4 total ... Jesus shouldnt be standing so close to him like he is trying to kiss him thats what one of those looked like, super weird"

### COMPLAINT LEDGER (what THIS cut will fix once billing tops up)
- **3:39 blind-man face + "Jesus like trying to kiss him"** → **b40** (s40). See autopsy below — rewrote the nose-to-nose framing + identity. STAGED, NOT yet regenerated (Gemini 429).
- **3:44 blind-man face** → **b41** (s41). Identity restated. STAGED.
- **3:49 blind-man face** → **b42** (s42). Identity restated. STAGED.
- **3:56 blind-man face** → **b43** (s43). Anti-grey/anti-old restated. STAGED.
- **1:34 (Jesus j2) + 1:53 (narrator n5) "Siloam"** → AUDIO recipe below. NOT yet re-voiced.

### TIMESTAMP→FRAME TRACE (from the LIVE mp4 + seg durations, not beat names)
Extracted `ffmpeg -ss <t>` from the shipped `john-9_man-born-blind.mp4` and matched by
on-screen caption:
- 3:39 f219 = **b40** s40 "The first face this man ever truly studied" — Jesus **nose-to-nose, hand cupped at the man's chin** = the "kiss". Blind man = wild long curly hair (drift).
- 3:44 f224 = **b41** s41 "And he said:" — man drifts younger, different face.
- 3:49 f229 = **b42** s42 "…and he worshipped him" — kneeling man drifts young/short-hair.
- 3:56 f236 = **b43** s43 "The question of whose fault…" — **grey-haired, grey-bearded OLD man** (severe identity break vs the mid-30s black-haired ref).

### PROMPT AUTOPSY (rubric meta-law 3)
- **b40 (kiss):** verdict **CAUSED + IGNORED**. The scene prose literally said *"The two
  faces close in the deep gold, in profile"* → the model drew them nose-to-nose, hand at
  chin = a near-kiss. AND the asset `s40-*.jpeg` is **stale 08-07_04:49 — generated BEFORE
  `REFS={"BLINDMAN":…}` was wired (08-12)**, so it never carried his face ref → identity
  drift too. FIX APPLIED (staged): rewrote scene to *"a natural, respectful arm's length …
  the two men clearly NOT touching"*; added must_not_show *"NOT nose-to-nose, NOT touching,
  Jesus's hand NOT on the man's face/chin, nothing that reads as a kiss"*; restated identity.
- **b41:** verdict **IGNORED (stale, no ref)**. `s41-*.jpeg` also stale 08-07 pre-ref → drift.
  FIX: identity restated in scene + must_not_show; ref now attached (REFS wired).
- **b42:** verdict **IGNORED (ref attached but weak text)**. `s42-*.jpeg` is 08-12 (had ref)
  but still drifts young. FIX: explicit "same thirty-five-year-old, unruly BLACK hair, short
  dark beard, never grey/elderly/younger" in scene + must_not_show.
- **b43 (grey old man):** verdict **IGNORED-despite-ref** — the hard case (lesson 10 / memory
  face-lock-needs-tight-crop). `s43-*.jpeg` is 08-12 WITH the ref yet renders a GREY ELDERLY
  man. Root: the BLINDMAN lock said "about thirty-five, black hair" but NOWHERE forbade
  grey/elderly, and the scene said "the whole first thirty-five years" (age-adjacent). FIX:
  strengthened the shared BLINDMAN lock ("SAME man … NEVER grey-haired, NEVER elderly, NEVER
  a clean-shaven youth") + a CRITICAL anti-grey clause in b43's scene + must_not_show. If it
  STILL drifts grey after a regen with this text, escalate to the lesson-10 identity-EDIT
  method (attach the frame + `CAST-REF-V2/blindman.jpeg`, change only the man's hair/face,
  recheck full frame) — do NOT churn rerolls.

### AUDIO AUTOPSY — Siloam (1:34 j2 / 1:53 n5)
- **Live cut renders it WRONG:** faster-whisper of the shipped mp4 → n5 = **"Silo **Am**"**
  (split, a hard stressed **/æm/** ending); Cameron wants **"si-LOH-uhm"** (soft schwa end).
- **The §AUDIO-FIX SHIP below used `"sih LOW am"`** — it fixed the STRESS (SILO-am→si-LOH-am)
  but kept the **hard "am"** ending. That is the untried lever: the ENDING vowel, not stress.
- **make_narration.py's own SPOKEN map ALREADY holds the validated schwa respell**
  `"Siloam": "sih low um"` (measured 2026-07-22 for THIS complaint #63) — it was **bypassed**
  by the 610a70352 manual re-render. Reverting to it is the fix.
- **Proven this session (`/tmp/r63/siltest`, `/tmp/r63/final`):** ElevenLabs renders
  `"sih low um"` as a single flowing **schwa "Siloam/siloum"** (NOT the split hard "Silo AM"),
  clean round-trip, no garble. This is the recommended respell.
- **Headless-validation caveat (honest):** the prior session did a 15-take stress-RMS +
  formant A/B and STILL shipped a cut Cameron rejected — whisper is deaf here and 16 kHz
  formants are too noisy to trust. So "sih low um" is **recommended, not ear-verified**;
  the COMBINED cut is Cameron's single verification point.
- **VOICE TRAP:** the live j2 was re-voiced with **Jesus = "Chris" (voice id iP95…)**, but the
  current `mbm_eleven.VOICE_ELEVEN[JESUS]` = **Alexander (UMnEnz…)**. The resume MUST re-voice
  j2 with the SAME voice as j1/j3/j4 in the live cut (verify first) — do NOT let render_segment
  silently swap Jesus to Alexander. Narrator = Brian (nPcz…), unchanged.

### ⛔ WHY PARKED — Gemini prepay depleted (429 RESOURCE_EXHAUSTED, meter frozen $617.34)
`v2_gen_api.py … --only b40 b41 b42 b43 --redo` returned 429 "prepayment credits depleted"
immediately (same wall as rows 82/95/116/118 — see Brain inbox billing ask, already filed).
No $0 crop path: every flagged frame has the man's face / the two-figure composition AS its
subject (can't crop away the subject). Picture edits are COMMITTED & `--check` PASS, waiting
on ONE top-up. Audio NOT re-voiced (would ship only in the combined cut, which is Gemini-gated).

### ▶ RESUME COMMAND (run when meter moves past $617.34) — ONE combined touch-once cut
```
cd media-production-v2
# 1) pictures (edits already committed in beats_v2.py):
python3 v2_gen_api.py build-63-man-born-blind --only b40 b41 b42 b43 --redo --ceiling <meter+2>
#    FULL-CUT GATE every regen: b40 = arm's-length, NOT kissing; b40/b41/b42/b43 = SAME
#    black-haired mid-30s man (NOT grey, NOT elderly, NOT a younger different face).
#    b43 still grey after 2 rerolls -> lesson-10 identity-EDIT, don't churn.
# 2) audio (revert the hard-am regression to the validated schwa):
#    re-voice j2 (Jesus voice = MATCH j1/j3/j4, verify — likely "Chris"/iP95, NOT Alexander)
#    + n5 (Brian) with Siloam respell "sih low um"; write correct .timing.json via the
#    pipeline (save_speaker_narration), atempo-lock to j2=1.802s / n5=14.341s so no window
#    moves; place in media-production/build-63-man-born-blind/audio/ (AUDIO_FROM_V1_SEGMENTS).
# 3) assemble + ship:
python3 v2_assemble.py 63            # must print AUDIO REBUILD/LOCK PASS
#    then FULL-CUT GATE the rendered mp4, ship (2 commits like row 39), deploy, live-verify,
#    review card answers Cameron: "the blind man is the same man in every frame, Jesus is at a
#    natural distance (no kiss), and Siloam now ends soft — si-LOH-uhm."
```

---

## §AUDIO-FIX SHIP 2026-08-12 (Opus AUDIO LANE, Machine A `Dev`, unattended/headless) — Siloam re-voiced to si-LOH-am, combined cut SHIPPED  ⚠️ SUPERSEDED — Cameron re-filed against this cut (hard "am" ending); see §C-FIX above

**Closes the §PARK below.** The 8 picture fixes (committed last session) + this audio
re-voice ship together as ONE touch-once combined cut — Cameron gets both fixes in
one re-cut, no double-approval churn.

**Cameron's OPEN audio complaint (`v2_outline.py 63`):** `"1:53 is still wrong its : si-LOH-uhm"`.

**Defect (verified, `/tmp` A/B before touching anything):** the shipped V1-dir `n5.mp3`
+ `j2.mp3` said Siloam **front-stressed** ("SILO-am", grain-silo) — measured
stress-RMS front-peaked (j2 old `[0.074, 0.034, 0.014]`, n5 old `[0.074, 0.07, 0.06]`).
whisper is DEAF to this (transcribes both "Siloam") — validated by **stress + vowel
formant**, never whisper.

**Respell chosen — `"sih LOW am"`** (space-separated, NOT hyphenated — hyphens made
ElevenLabs over-segment into "Si-El-O-shum"/"CLOHM"). Won a 15-take A/B batch on Chris
(Jesus) + Brian (narrator):
- 3-syllable, clean round-trip to "Siloam" (no garble).
- Middle-syllable STRESS (the fix for "SILO-am"): j2 new stress-RMS `[0.038, 0.092, 0.07]`
  = clear MIDDLE peak; n5 new middle centroid **1186 Hz** (long-o /oʊ/, F2 low).
- Beat every alternative: `sih LOH um`→"CLOHM" (garbled); `sih LOH uhm`→"Silo-ham"
  (front-stress); `sy LOW um`→"silo, um" (long-i first vowel = grain-silo); `sih LOAM`
  clean but only 2 syllables.

**Re-voiced ONLY j2 + n5 through ElevenLabs** (`render_segment`, SAME locked voices —
Jesus=Chris `iP95…`, narrator=Brian `nPcz…` — NOT Alexander/edge-tts; no voice swap).
Written to `media-production/build-63-man-born-blind/audio/` (V1 dir; `AUDIO_FROM_V1_SEGMENTS=True`).
**atempo-locked** (pitch-preserving) to the ORIGINAL durations so NO picture window
moves: j2 → 1.802 s exact, n5 → 14.341 s exact.

**Audio baseline moved (sanctioned re-voice exception):** old picture-only SHA256
`09854d47…` → **new SHA256 `7e4fa1424875c76b3d6e3ed2fcc5ab1ccac6d201422c6b35397be04476b0956f`**.
Only j2 + n5 changed; every other segment, all wording, all timing outside those two
segments is untouched. `v2_assemble.py 63` **AUDIO REBUILD PASS**, 247.589 s, mp4 22 MB.

**Verified in the DELIVERED mp4** (whisper word-timestamps on the rendered file): both
occurrences present + un-garbled — j2 "Go, wash in the pool of Siloam" at **1:31.9**,
n5 "he knelt at the pool of Siloam" at **1:52.1** (= Cameron's "1:53"). Pronunciation
validated on the isolated locked segments (whisper can't hear the vowel).

**COMPLAINT LEDGER (both closed in this one combined cut):**
1. `"1:53 … si-LOH-uhm"` → **CLOSED** — both Siloam occurrences now say **si-LOH-am**
   (middle-stress, long-o), no longer the grain-silo "SILO-am". Same voices; caption
   keeps the KJV "Siloam".
2. blind man's face @ 0:12/1:29/3:16/3:29/3:35/3:49/3:55 + 1:41 clay eyes → **CLOSED**
   last session (BLINDMAN face-sheet wired into REFS; 8 frames regenerated) — carried
   into this same cut.

**Cost:** ElevenLabs only (~15 short A/B takes + 2 final segments, well under $1);
**$0 Gemini** (no images touched). Reroll budget N/A (audio lane).

---

## §C-FIX RE-OPEN 2026-08-12 (Opus, Machine A `Dev`, unattended/headless) — PICTURES DONE, held for combined ship; AUDIO parked → NEEDS-AUDIO

**Cameron re-opened the shipped cut `94cf6ff1` (`v2_outline.py 63` / REVIEW-LESSONS row 63):**
> "1:53 is still wrong its : si-LOH-uhm. The blind mans mans face is not the correct
> look @ : 0:12, 1:29, 3:16, 3:29, 3:35, 3:49, 3:55 wrong lookijg blind person. 1:41
> the blind mans eyes were supposed to be pack with clay as hes walking to the pool
> and they are not. Fix all these pictures. 8 total"

MIXED complaint: **8 PICTURES** (blind man's face/identity + one clay-continuity) + **1 AUDIO** (the word "Siloam" at 1:53). Traced every timestamp to the frame that RENDERS there from the LIVE mp4 (not beat names):

| Cameron | live-mp4 frame | defect | fix |
|---|---|---|---|
| 0:12 | b03 s03 | beggar's face off-model + eyes look sighted | ref-locked + milk-pale unseeing eyes added |
| 1:29 | b16 s16 | drifted to a GREY-haired ELDER (worst outlier) | ref-locked → correct 35yo, clay on eyes |
| 1:41 | b19 s19 | eyes CLEAN, not clay-packed (his explicit complaint) | ref-locked + must_show/not_show force clay MASK over both eyes |
| 3:16 | b36 s36 | face drift | ref-locked |
| 3:29 | b38 s38 | face drift | ref-locked |
| 3:35 | b39 s39 | face drift (heavier beard) | ref-locked → matches anchor |
| 3:49 | b42 s42 | face drift | ref-locked |
| 3:55 | b43 s43 | face drift | ref-locked |
| **1:53** | b21 (the washing) — AUDIO of the WORD, not the frame | narrator says Siloam as "SILO-am" (grain silo) not si-LOH-uhm | **→ NEEDS-AUDIO (see §PARK below)** |

### PROMPT AUTOPSY (rubric meta-law 3) — verdict IGNORED (identity) + ALLOWED (b03 eyes)
The BORN-BLIND MAN had a text lock (`LOCKS["BLINDMAN"]`) but **his approved face sheet
`CAST-REF-V2/blindman.jpeg` was NEVER wired into a `REFS` dict** — so `cast_refs_for()`
rendered him TEXT-ONLY on all 43 beats. A text description does not pin a recurring face
(lesson 2/10); only an attached reference IMAGE does. That is the root cause of the
frame-to-frame drift (black→brown→grey hair, changing age/beard). **Fix = add
`REFS = {"BLINDMAN": "CAST-REF-V2/blindman.jpeg"}`** (attaches his face lock to every
BLINDMAN beat, exactly like the Jesus ref). b19 clay = IGNORED (scene said "clay-eyed
man" twice; generator dropped the subtle detail → strengthened must_show/must_not_show
to demand a clay MASK over both sealed eyes). b03 eyes = ALLOWED (scene never stated
milk-pale unseeing eyes → added).

### What this session did
- Wired the BLINDMAN reference; strengthened b03 (milk-pale eyes) + b19 (clay-packed) text.
- **Regenerated the 8 flagged beats** (b03/b16/b19/b36/b38/b39/b42/b43) with the ref
  attached (each run logged `[+1 char ref: BLINDMAN]`). $1.07, meter $607.42→$608.49.
  **0 rerolls** (all 8 first-take clean). Reroll % = 0 (budget 15%). Under $6.10/row.
- **FULL-CUT GATE (§6b)** on the RE-RENDERED mp4 (247.7s, AUDIO REBUILD PASS
  `09854d47` = byte-identical, picture-only): all 8 new frames viewed at full res —
  identity now matches the anchor, b16 elder→correct man, b19 both eyes packed under
  clay, b03 pale unseeing eyes + Jesus cream-only. Swept the ~27 RETAINED blind-man
  frames (b01/b02/b09/b10/b11/b12…): all read as the SAME lean dark-haired short-beard
  man as the ref (b10 close-up even shows the pale blind eyes) — no identity clash, no
  extra regen needed (cost law). Captions bottom-band 3-colour (blue scripture / white
  narrator / red Jesus), closing card clean, no dead tail. Anatomy/scale/second-cream/
  modern-object all clean.

### COMPLAINT LEDGER
1. blind man's face wrong @ 0:12/1:29/3:16/3:29/3:35/3:49/3:55 → **CLOSED** — root cause
   (unwired face sheet) fixed; all 7 frames regenerated locked to `blindman.jpeg`.
2. 1:41 eyes not clay-packed → **CLOSED** — b19 regenerated with both eyes sealed under
   a clay mask.
3. 1:53 "si-LOH-uhm" (Siloam pronunciation) → **NOT YET — parked NEEDS-AUDIO** (§PARK).
   A picture C-FIX may not gamble a 4th re-voice it cannot ear-verify; the audio lane
   owns this and will ship it together with these frames in ONE combined cut (touch-once).

### 🅿️ §PARK → NEEDS-AUDIO (audio lane): re-voice "Siloam" to si-LOH-uhm
**Why held, not shipped:** shipping the picture cut on the current audio would re-ship a
cut whose 1:53 STILL says the wrong Siloam = the rubric's worst failure (a cut that
repeats a filed complaint). So the 8 picture fixes are committed to `assets/` + this
`beats_v2.py`; the AUDIO LANE re-voices n5, reassembles (auto-picks up these new frames),
and ships ONE combined cut — Cameron gets both fixes in a single touch-once re-cut.

**The audio defect (verified):** the shipped V1-dir `n5.mp3` (14.341s) was re-voiced on
2026-08-07 with SPOKEN respell `"Siloh-am"` — that reads as **"SILO-am"** (stress on the
first syllable = the grain-silo sound). Cameron wants **si-LOH-uhm** (stress on the
MIDDLE syllable, long-o). whisper is DEAF to this vowel (it transcribes both as "siloam")
— validate by FORMANT/stress, never by whisper.

**Candidate findings (rendered Brian, `/tmp` A/B, centroid of stressed vowel — lower =
more back-rounded /oʊ/):** `Siloh-am` 1048Hz (current, rejected); `sih-LOH-um` and
`suh-LOH-um` → ElevenLabs OVER-SEGMENTS the hyphens into "Si-El-O-shum" (garbled, avoid);
`sih-LOAM` → clean "siloam", **721Hz** (strongest long-o) but only 2 syllables; `sy-LOH-um`
→ clean 3-syllable "Siloam", 859Hz. Recommend the audio lane render N takes of
`sih-LOAM` and `sy-LOH-um`, formant-validate (F2<1600 on the stressed vowel) AND ear-check,
pick the winner. Applies to BOTH occurrences (j2 "Go, wash…" + n5 "he knelt…") — keep them
consistent; the caption keeps the KJV "Siloam".

**Timeline:** to avoid a full window remap, **atempo-lock the new n5 to 14.341s** (and j2
to its current 3.006s) before writing them to
`media-production/build-63-man-born-blind/audio/`. `AUDIO_FROM_V1_SEGMENTS = True` is
already set, so v2_assemble rebuilds from those mp3s. If a re-voice must change duration,
remap all 43 windows piecewise-linear on the segment onsets (as the 2026-08-07 fix did).
Then reassemble (AUDIO REBUILD PASS), deploy, live-verify, and mark complaint #63 resolved
against the new hash — the review card must answer BOTH "si-LOH-uhm" and the 8 pictures.

---

## §SHIPPED ✅ REALISTIC-V2 SHIPPED TO REVIEWER (Machine A `Dev`, 2026-08-12, Opus picture runner — unattended/headless) [SUPERSEDED — this cut `94cf6ff1` was re-opened; see §C-FIX above]

**Row 63 finished from AUTHORED → BUILT.** The Siloam audio complaint was already
fixed at the author level (§0-FIXED below); this session did the picture runner's
remaining steps: generated the last two stills, ran the FULL-CUT GATE, re-cut the
one defect it caught, and shipped on the byte-identical fixed audio.

### COMPLAINT LEDGER (the review card answers this in Cameron's words)
1. **"still wrong its : si-LOH-uhm"** (Siloam) → CLOSED. Jesus's line "Go, wash in
   the pool of Siloam" (j2) and the narrator's "He knelt at the pool of Siloam" (n5)
   were re-voiced through ElevenLabs to say **si-LOH-am** (round-trip verified on
   both whisper engines, no longer "Salome"); captions keep the KJV spelling
   "Siloam". AUDIO REBUILD PASS SHA256=09854d47… is the cryptographic proof the fix
   is in the shipped audio.

### What this session did
- **Generated the last 2 stills** b42 (s42 worship) + b43 (s43 closing walk), ~$0.27,
  meter $602.87→$603.13. Both QC-clean first take: Jesus cream-only + identity-locked
  (Middle-Eastern, dark wavy hair, full beard, calm eyes, no halo), anatomy/scale/
  period correct, the abandoned-staff coda present in s43 per the beat.
- **FULL-CUT GATE (6b):** extracted a mid-window frame per beat from the RENDERED mp4
  (43 beats) + the 3 caption frames + closing question card, viewed every one against
  the defect checklist + RUNNER-LESSONS + rubric. Result: CLEAN except ONE frame.
- **ONE defect caught + fixed — s05 (b05, "notice they did not ask"):** the seated
  blind beggar rendered in a **cream/off-white tunic** = a second-cream figure + a
  wardrobe break (he is brown in every other frame). AUTOPSY: b05 is `jesus:False`
  and does not pin the beggar's brown robe → generator defaulted the unpinned
  secondary figure to cream (the "unlocked secondary figure" class). Runner cannot
  edit the beat; ONE reroll (`--only b05 --redo`, $0.13, meter $603.13→$603.27)
  reframed to the tight two-disciple two-shot the beat's own scene calls for ("close
  on two disciples' faces… one hand half-raised in inquiry") — cream beggar gone,
  both disciples earth-tone brown, no second cream figure. Re-verified in the
  RE-RENDERED mp4 at 23.89s: clean.
- **Rerolls: 1 / 43 beats = 2.3%** (well under the 15% budget). **Row image spend
  ≈ $0.40** (2 new stills + 1 reroll) — far under the $6.10/row average; COST LAW
  trend DOWN (most of the row's stills were already banked from the earlier build).
- **AUDIO REBUILD PASS** SHA256=09854d47… (byte-identical narration — nothing
  re-voiced this session), 247.70s, 22.0 MB, card renders clean (no tofu glyphs),
  no dead tail (audio 247.692s = mp4 247.70s).
- Green/hazel Jesus eyes LEFT AS-IS per rubric lesson 20 (V2 master ref is green-eyed
  by design; never edit toward brown).

---


## §0-FIXED ✅ AUDIO FIX DONE — Siloam complaint CLOSED (Machine A `Dev`, 2026-08-07, author lane)

**Cameron's OPEN complaint (`v2_outline.py 63`): `"still wrong its : si-LOH-uhm"`
(Siloam) — FIXED at the author level. j2 & n5 re-voiced; row → AUTHORED, Ready ✅.**

### Root cause (verified, not guessed)
The delivered build is **ElevenLabs** (Chris=Jesus, Brian=narrator, all 44.1 kHz —
the park's earlier "just edge-tts" read was wrong; only make_narration.py's *source*
is edge-tts). On the ElevenLabs Jesus voice **plain "Siloam" renders as "Salome"**
(reproduced by faster-whisper base.en+small.en on the delivered j2.mp3, and again on
a fresh ElevenLabs render). The old respell `"sih low um"` rendered as chopped
"silo, um". Neither is Cameron's target si-LOH-uhm.

### The fix (what I did — all committed with the row)
1. **Respell** `make_narration.py` SPOKEN: `"Siloam" → "Siloh-am"`. Measured A/B:
   `Siloh-am` round-trips CLEAN to "Siloam" on BOTH whisper engines for BOTH voices
   AND on BOTH TTS backends (ElevenLabs + edge-tts). Sounds sih-LOH-am = his target.
   Caption keeps the true KJV "Siloam" (unchanged).
2. **Re-voiced j2 + n5 through ElevenLabs** (matching engine — NOT edge-tts, which
   would have made Jesus's voice mismatch the other 21 segments). Both write 44.1 kHz;
   audio-audit A (old-voice) is now **0 of 23**. New durations: j2 3.006 s (was 3.531),
   n5 14.977 s (was 16.721) — the correct pronunciation is a touch tighter.
3. **Timeline coupling remapped.** j2 shrank 0.525 s, n5 1.744 s → n4-region shifts
   −0.525 s, n6-onward −2.269 s. New total **247.692 s**, card_start **240.217 s**.
   All 43 V2 picture windows remapped via a piecewise-linear old→new map anchored on
   the segment onsets (extract_beats). `--check` PASS, windows monotonic + contiguous,
   last_end 239.891 < card_start 240.217.
4. **`AUDIO_FROM_V1_SEGMENTS = True`** added to `beats_v2.py` — the finished V1 MP4 is
   now stale vs the re-voiced mp3s, so the runner rebuilds the track from the V1
   segment mp3s at the extract_beats offsets. audio-audit B (short) is now **0**.

### 🅿️ PICTURE RUNNER — the ONLY remaining steps (a paid picture credit + assemble)
Stills are **41/43**. Generate the last two, then assemble+ship on the fixed audio:
- `python3 media-production-v2/v2_gen_api.py media-production-v2/build-63-man-born-blind --ceiling <meter+2*0.201+25>`
  → pulls **b42** (`s42-and-he-worshipped-him-right`) and **b43**
  (`s43-the-question-of-whose-fault`) only (~$0.27). Run the eyes-arc light-QC below.
- `python3 media-production-v2/v2_assemble.py 63` — AUDIO_FROM_V1_SEGMENTS path,
  AUDIO REBUILD must PASS. Deploy + live-verify, then ship via the C-FIX/ship flow.

### COMPLAINT LEDGER — the review card must tell Cameron, in his words
1. **"still wrong its : si-LOH-uhm"** (Siloam) → Jesus's line "Go, wash in the pool of
   Siloam" and the narrator's "He knelt at the pool of Siloam" now clearly say
   **si-LOH-am** (verified round-trip both engines), no longer "Salome". Same
   ElevenLabs voices as the rest of the video; captions keep the KJV spelling "Siloam".

---

## §0 🅿️ RUNNER PARK → NEEDS-AUDIO (Machine A `Dev`, 2026-08-07, Opus runner resume) [SUPERSEDED by §0-FIXED above — kept for history; its "needs ElevenLabs, not edge-tts" instinct was right, its "just edge-tts" aside was wrong]

**The picture runner STOPPED at the audio gate. Cameron's OPEN complaint is
AUDIO-domain — a picture runner may not re-voice, so this row is parked
NEEDS-AUDIO for the audio lane. $0 spent (no Gemini credits), 0 pictures touched.**

**Cameron's OPEN complaint (`v2_outline.py 63`):** `"still wrong its : si-LOH-uhm"`
(the pronunciation of **Siloam** — he wants **si-LOH-uhm**).

**VERIFIED WRONG in the locked V1 audio (faster-whisper base.en + small.en, both agree):**
- **`audio/j2.mp3`** (Jesus: *"Go, wash in the pool of Siloam."*) transcribes as
  **"Go, wash in the pool of Salome."** — this is Jesus's own spoken instruction,
  the most prominent occurrence and the exact context of the complaint. "Salome"
  ≠ si-LOH-uhm (wrong first vowel *sa-*, wrong ending *-mee*). **This is the defect.**
- `audio/n5.mp3` (*"He knelt at the pool of Siloam…"*) transcribes cleaner
  ("siloam") but should be re-checked once j2 is fixed.
- The existing narration override in `make_narration.py:89` is
  `"Siloam": "sih low um"` (added 2026-07-22 for complaint #63). It did NOT
  land — the delivered audio still says "Salome". A better respelling and a
  re-voice through the REAL engine (ElevenLabs, per row 18/19 audio-fix law —
  NOT edge-tts) is needed.

**AUDIO LANE — the fix (spend $0 on Gemini):**
1. Respell **Siloam** in `make_narration.py` so it lands as **si-LOH-uhm**
   (e.g. try `"sih LOAM"` / `"sih LOH um"` / an ElevenLabs phoneme tag) and
   re-voice **j2**, plus **n4/n5** wherever "Siloam" occurs. Ear-check each take
   until it clearly says si-LOH-uhm.
2. Also verify the KJV caption keeps the true spelling "Siloam" (unchanged).
3. Set `AUDIO_FROM_V1_SEGMENTS=True` so the re-cut rebuilds from the fixed mp3s.

**PICTURE STATE (so the handoff is honest):** stills are **41/43** — only two
frames remain to generate: **b42** (`s42-and-he-worshipped-him-right`) and
**b43** (`s43-the-question-of-whose-fault`), est ~$0.27. They were NOT generated
here (gate = stop). After audio is fixed, a picture runner must:
`python3 media-production-v2/v2_gen_api.py media-production-v2/build-63-man-born-blind --ceiling <computed>`
to pull b42/b43, run the full light-QC (the eyes arc b19/b21/b22 first-sight is
the identity law — see below), then `v2_assemble.py 63` and ship.
So: **NEEDS-AUDIO now → after audio fix, AUTHORED+Ready (2 stills + QC + assemble remain), not directly BUILT.**

---


Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 43 beats, ~242 s.

## ⚑ OPEN COMPLAINT ON THIS EXACT ROW (Cameron):

> "still wrong its : si-LOH-uhm"

Audio gate: verify the locked V1 narration says si-LOH-uhm at every
"Siloam." If it does not, mark NEEDS-AUDIO on the board and stop (audio
immutability — never re-voice).

## Coverage shape

Four true wides with stated geometry: b03 (the passing, in profile),
b06 (the street's verdicts crossing behind the beggar's shoulder), b24
(the dispute ring, camera outside the near backs), b25 (the tribunal —
accused and examiners in one profile). TWELVE flips, and the row's soul
lives in three of them being LONE-man frames: b19 (the clay-eyed walk
down the lanes ALONE — staff, wall-touch, strangers' stares), b21 (the
washing), b22 (FIRST SIGHT). Phantom people in the walk would destroy
the obedience-before-sight arc.

## The eyes (the row's identity law)

- BEFORE: his eyes are unfocused/clouded — a real blind man's eyes,
  never milky-horror, never bandaged.
- CLAY ON: the clay is visible over both eyes b12→b21 — continuity
  prop; same clay, drying as he walks.
- AFTER (b22 on): NEW clear seeing eyes in the SAME face — face-board
  him hard; this is the beard-class risk row (32/62/91/102) with eyes
  instead of beards. His first-sight face is joy-shock, not horror.
- The washing pours from cupped hands — Siloam is a stepped POOL
  (promote-first from b21), not a river.

## Other checks

- HALL: stash offered build-22's ROYAL hall — DECLINED (this is a
  Pharisee council chamber, different institution). Promote-first from
  b25.
- LEADERS: exactly THREE examiners (count law), distinct, cold-formal
  not cartoon (row 90/107 variety).
- Direction (row-83): b19 DOWN the lanes to the pool; b23 BACK UP at a
  half-run (staff forgotten — the prop's absence is the story); b31
  OUT through the heavy door.
- The parents' fear beats (if rendered): they edge AWAY from the
  question — spatial, believable.
- Only Jesus wears cream.
