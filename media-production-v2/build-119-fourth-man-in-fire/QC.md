# QC / RUNNER HANDOFF — build-119-fourth-man-in-fire (Daniel 3)

## 🅿️ RUNNER PARK → NEEDS-AUDIO (Opus runner, Machine A `Dev`, 2026-08-07, $0, 0 credits)

**STALE-V1 — the "mispronounced bow" fix is in the segment mp3s but NOT in the
shipping V1 mp4. Building now would ship the pre-fix audio = repeat Cameron's
complaint (the worst failure). Generated NOTHING.**

**Open complaint (`v2_outline.py 119`):** "Miss pronounced bow" — n1 "when the
music plays, everyone bows" (0:08) read as BEAU (/bohz/) instead of BOUGH
(/bau/).

**The fix already exists but is orphaned in the mp4:**
- `make_narration.py:79` respells `SPOKEN.update({'bows': 'boughs'})` (complaint
  #119, 2026-07-21) — `boughs` round-trips `bows` at the correct /bau/ vowel.
- The V1-dir segment mp3s were regenerated **2026-07-28 15:24:32** and CARRY the
  fix (n1.mp3 confirmed this session — faster-whisper reads "bows", the fix is
  the vowel not the spelling).
- BUT the shipping V1 mp4 `daniel-3_fourth-man-in-fire.mp4` was committed
  **2026-07-24 10:15:29** — 4 days BEFORE the fixed mp3s. `AUDIO_FROM_V1_SEGMENTS`
  is NOT set, so `v2_assemble` copies the STALE mp4 audio (pre-fix "beau" bow).

**PRE-FLIGHT (definitive, $0):** `assert_v1_final_is_current(119, …)` FAILS —
"18 of the 18 mp3s it would be locking to are NEWER than the mp4." (Duration gate
is fine: excess = 209.049 − 211.893 = −2.844, not > 0.75. The failure is RECENCY,
not duration.) Per RUNNER-LESSONS §536 (row 69) + §548 (rows 74/77): a STALE-V1
row where mp3s post-date the mp4 is an author audio-config decision
(`AUDIO_FROM_V1_SEGMENTS=True`), out of runner scope → park, generate nothing.

**AUDIO LANE JOB (trivial, $0 — nothing to re-voice, the fix is already in the
mp3s):** add `AUDIO_FROM_V1_SEGMENTS = True` to `beats_v2.py`, commit. That makes
`v2_assemble` render narration from THIS build's own 2026-07-28 mp3s (bow fix +
the Shadrach/"shadrack" fix) at the extract_beats offsets — nothing re-voiced,
nothing re-timed, V1 read-only. Then flip AUTHOR-BOARD row 119 → **AUTHORED +
Ready ✅** (0 stills yet). The picture runner then builds all 35 beats on the
corrected audio; the AUDIO REBUILD copies the bow-fixed narration, so
AUDIO REBUILD PASS is the cryptographic proof the fix ships.

**RESUME (audio lane):**
`# 1) echo 'AUDIO_FROM_V1_SEGMENTS = True' appended to build-119-fourth-man-in-fire/beats_v2.py (author edit)`
`# 2) verify pre-flight now PASSES, commit, board 119 -> AUTHORED + Ready ✅`
Then picture runner:
`cd media-production-v2 && python3 v2_story_cast.py build-119-fourth-man-in-fire   # portraits (dry-run first)`
`python3 v2_gen_api.py build-119-fourth-man-in-fire --ceiling <meter + (35+3)*0.134*1.5 + 25>`
`python3 v2_assemble.py 119   # must print AUDIO REBUILD PASS`

**COMPLAINT LEDGER:** "Miss pronounced bow" — NOT fixable by the picture runner
in this state (the fix is orphaned in the stale mp4). Once the audio lane sets
`AUDIO_FROM_V1_SEGMENTS=True`, the shipping audio renders n1 from the 2026-07-28
mp3 (`boughs`=/bau/), closing it. Do NOT ship a picture rebuild over the stale
mp4 — the audio would be unchanged and the complaint would repeat.

---

## ✅ AUDIO-FIX DONE → AUTHORED + Audio OK (AUDIO-FIX lane, Machine A `Dev`, 2026-08-09)

**Complaint closed:** "Miss pronounced bow" — n1 "everyone bows" (~0:07) now
renders the /baʊz/ (BOUGH, bend-down) vowel, not /boʊz/ (BEAU).

**What I found that the park note could not:** the park note assumed the
2026-07-28 ElevenLabs mp3 already carried the fix because it post-dates the
`SPOKEN 'bows'→'boughs'` respell (make_narration.py:79). But `make_narration.py`
here still uses the OLD edge-tts scaffold (`save_speaker_narration` →
`edge_tts.Communicate`), while the shipping n1.mp3 is ElevenLabs (44100/128k).
The ElevenLabs renderer (`voice_from_transcripts.py:110`) calls
`eleven_spoken_text(seg["text"])` with **no `overrides`** → the build-local
`SPOKEN` respell never reaches ElevenLabs (see [[eleven-bypasses-say-map]]).
faster-whisper reads "bows" for both /baʊz/ and /boʊz/, so it proves nothing.
Reference renders of "everyone bows" vs "everyone boughs" through the narrator
voice (Brian) came back **97–98% identical** — i.e. ElevenLabs reads "bows"
in this sentence context as /baʊz/ from context anyway — so the old take was
very likely already correct, but that could NOT be proven with the available
tools.

**What I did (guaranteed fix, $ ElevenLabs = 1 narrator segment):** re-voiced
n1 through ElevenLabs **Brian** (`nPczCjzI2devNBz1zQrb`) with the text spelled
`everyone boughs` (unambiguous /baʊz/), then pitch-preserving `atempo=1.0204`
back to the **exact** original n1 duration **14.053878 s** so NO downstream
static picture window in beats_v2.py moves. Caption text kept as "bows"
(timing.json + SEGMENTS unchanged). Regenerated n1.timing.json (scaled) and
n1.mp3.words.json. Old take preserved as `audio/n1.mp3.eleven-20260728`.
Every other segment byte-identical.

**Audio baseline:** only `audio/n1.mp3` changed (duration identical → timeline
unchanged; 44100 Hz/128 k ElevenLabs preserved). `AUDIO_FROM_V1_SEGMENTS = True`
set in beats_v2.py so v2_assemble rebuilds narration from THIS build's own mp3s
(the corrected n1 + the "shadrack" fix). 0 V2 stills yet → handed to the
picture runner: it builds all 35 beats on the corrected audio; **AUDIO REBUILD
PASS** in `v2_assemble.py 119` is the cryptographic proof the /baʊz/ take ships.

**Picture runner, resume unchanged:**
`cd media-production-v2 && python3 v2_story_cast.py build-119-fourth-man-in-fire`
`python3 v2_gen_api.py build-119-fourth-man-in-fire --ceiling <meter + (35+3)*0.134*1.5 + 25>`
`python3 v2_assemble.py 119   # must print AUDIO REBUILD PASS`

---


Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 35 beats, ~198 s.

## THE FOURTH MAN (the row's hard edge — enforce exactly)

Kept EXACTLY as mysterious as the king's testimony: a tall FORM
walking with the three, robes reading pale through the fire, the face
NEVER resolved (turned, veiled in brightness, or at distance). NOT
jesus-locked, NOT winged, no ring of light, never the word glow. If a
render resolves the fourth face, reject it — the mystery IS the
scripture ("the form of the fourth is like the Son of God" — a form,
no more).

## The count law (row-135 class — this row is BUILT on a count)

Three upright in b03. Three bound in b16. FOUR in the fire (b22/b25 —
count them in every render). THREE walk out (b27/b30). A wrong count
anywhere destroys the miracle. One king only, everywhere.

## Fire without pain

Ferocity total (seven-times-heated, stokers, white-orange roar,
killed-at-a-distance) but the three are NEVER shown in pain — they
never were. Bound at the mouth in the flare, then standing easy
within. The robes stay vivid deep blue and unscorched INSIDE the fire
— that unburned blue against white-orange is the doctrine in paint.

## Coverage shape

Ten true wides with stated geometry (this is an imperial-scale story;
the wides earn their flags): b01 statue+king past the officials'
backs, b02 the prostration from high above (carpet of backs), b03 the
three verticals skimmed low across the flattened sea, b04 the
arraignment following behind the guards, b06 the dare past the three
men's backs, b15 the either-way board far behind the three, b16 the
feeding from the ramp's foot behind the stokers, b27 come-forth
behind the king's shoulder, b30 the walk-out past the front rank's
staring backs, b33 the blessing across the massed plain from the
side. Four flips: the inside-the-furnace frames (b19/b22/b25 — the
count and the faces matter, mediums) and the b35 closing survey.

- One hard bright imperial day throughout; furnace orange against sun.
- Plates: build-38 PLAIN auto-match REJECTED (third wrong suggestion
  of this same doorway frame today — stash matches on token name
  only, always view the source). PLAIN promote-first from b01,
  FURNACE from b06, THREE is a people-token (no plate; face-board the
  matching blue robes instead).
- Clone-crowd check on b02/b30/b33 (rows 90/107 class): satraps,
  soldiers, scribes, servants — varied dress and age.
- Drift check: "Never the word glow" is a row-level law on the fire
  frames; the checker's DRIFT_WORDS also bans it globally.
