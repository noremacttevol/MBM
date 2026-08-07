# QC — row 10, build-10-well — REALISTIC rebuild (2026-08-01, Machine A `Dev`, Claude worker 7)

Cut: `john-4_woman-at-the-well-realistic-v2.mp4` · 49 stills, `assets-realistic/`,
gemini-3-pro-image native 2K (1536x2752), JESUS LOCK v5 + SAMARITAN WOMAN image
anchor (`CAST-REF-V2/woman-ref.jpeg`, generated this session) + Peter/John in
b41 anchored to the shared `CAST-V2-REF/` library sheets + rough-draft
continuity refs from the rejected 1K set in `assets/` (Session 6 blanket
rejection AND all 32 files 768x1376 per the resolution audit; 32 of 49 beats
had roughs, only 6 were kept — the rest carried the exact defect their beat
must avoid and were dropped up-front per the rough-echo lesson, recorded in
the beats_v2 docstring).

## The row's own defect class, found before any spend

The old roughs put THE JAR back in her hands in s44/s45/s46/s47/s49 — after
John 4:28 ("The woman then left her waterpot"), the story detail the whole
build exists to land. Root cause was this build's own WOMAN lock text ("She
carries a large rounded clay water jar"), which rode byte-identically into
every prompt. Per the row-9 corollary (a dropped rough's defect reproduces
from scene TEXT alone), the jar clause was removed from the lock, the early
scenes carry the jar explicitly, and b44-b49 state her hands are EMPTY.

## Gates run before generation

| gate | result |
|---|---|
| `v2_prompt.py --check` | PASS, 49 beats, 0 fails (re-run after every beat edit) |
| windows | ALL 49 verified against the FIXED `extract_beats.py` — segment boundaries and phrase splits already matched the absolute times (audio_start + raw phrase time) to within 0.01 s. THREE intra-phrase sub-splits sat 1.2-2.6 s late and were re-placed on the real pauses measured with faster-whisper (base.en, CPU) + silencedetect on the actual V1 mp3s, which agree with the extractor's phrase ends: j1 a/b 116.0 → 114.2 ("thirst again:"), j1 b/c 121.0 → 118.4 ("shall never thirst;"), n6 b34/b35 187.0 → 185.8 ("to worship on —"). The stale `*.words.json` files disagree with the real audio (segments were re-voiced 2026-07-21+) and were NOT trusted; whisper + silencedetect on the mp3s themselves are the evidence. The b39/b40 split (221.0) sits correctly in the measured pause after "his twelve —" and was kept. |
| music bed | none — narration + intentional silence only (V1 audio copied packet-for-packet at assembly) |
| ceiling | every paid run carried `--ceiling` recomputed from the live shared meter and sliced with `--only` |
| claim | claimed by push (8b356064c) BEFORE any spend |

## Per-still QC (every image Read at full size; face crops zoomed where gaze/identity was in question)

| still | verdict | note |
|---|---|---|
| anchor | ACCEPT (take 1) | woman-ref.jpeg — lock rendered exactly; candid off-lens gaze |
| s01 | **take 2** | take 1 CAMERA-GAZE (face crop confirmed eyes into the lens on the opening frame); scene text re-geometried to a three-quarter pass |
| s02 | ACCEPT (t1) | the morning contrast frame — a dozen women, rope in use, children, long golden shadows (deliberate morning, not a time-of-day defect) |
| s03 | ACCEPT (t1) | three heads together, hand half over mouth, brows up, eyes cut down the road |
| s04 | **take 2** | take 1 CAMERA-GAZE straight into the lens; re-geometried three-quarter |
| s05 | ACCEPT (t1) | the lane walk — watchers in doorways and windows tracking her, one stopped grinding, her eyes locked ahead |
| s06 | **take 2** | take 1 rendered the rope-wear grooves as a decorative carved rope MOLDING around the curb (reads ornamental); must_not hardened |
| s07 | ACCEPT (t1) | she checks mid-step on the rise, seated figure small and unreadable at the well |
| s08 | **take 2** | take 1 exhaustion was RIGHT but a ROPE was tied to the rim — "thou hast nothing to draw with" dies if the well provides one; rope banned in beat AND in the WELL lock (see below) |
| s09 | **take 2** | take 1 DUPLICATE-IDENTITY — the anchor echoed as a second copy of her face in the background |
| s10 | **take 2** | take 1 had her simply standing, not caught turning back toward town — the frame is "everything in her body said turn around" and the turn wasn't in her body |
| s11 | ACCEPT (t1) | the ask — he's seated, slumped, hand open; she's arrested mid-turn staring (seat is a low wall section rather than the round curb — recorded honestly; the at-a-glance read is correct) |
| s12 | ACCEPT (t1) | brows up, lips parted, pure disbelief |
| s13 | ACCEPT (t1) | close on Jesus asking — open empty hands, cracked-lip tiredness, V5 face, no strategy in it |
| s14 | ACCEPT (t1) | the startled half-laugh, head tipped back, jar down on hip — first crack in the guard |
| s15 | ACCEPT (t1) | she's closed the distance; he offers with the turned-open hand; both head-to-sandals |
| s16 | ACCEPT (t1) | w9 frame — palm-up "look at what I am", challenge not apology |
| s17 | ACCEPT (t1) | leaning over the mouth, gesturing INTO the dropping shaft, practical face, no rope anywhere (the dropped rough's near-gaze not echoed) |
| s18 | ACCEPT (t1) | rough held — the glassy worn grooves, black shadow, rope fibres in the cracks |
| s19 | ACCEPT (t1) | the corner — one brow up, mouth just curling, testing |
| s20 | **take 2** | take 1 lean/warmth/wake-up all right but a heavy ROPE lay coiled on the curb beside him (same defect class as s08). WELL lock now states no rope/bucket at the well, with a separate WELL-MORNING lock for b02 where the morning women legitimately haul one |
| s21 | ACCEPT (t1) | j1a — his hand indicates the jar she holds; noon; nobody at the lens |
| s22 | **take 2** | take 1 had a stray over-shoulder figure IN CREAM at the frame edge (only Jesus wears cream — a second unlocked Jesus, the row-9 s14 defect); must_not hardened to "only person visible" |
| s23 | ACCEPT (t1) | j1c lands on her working face — brows drawn, following something just out of reach |
| s24 | ACCEPT (t1) | the abandoned-errand frame — empty jar against the curb, her feet turned away toward the well |
| s25 | ACCEPT (t1) | guard fully down — unfocused wide eyes, softened mouth, no tears (correctly quieter than that) |
| s26 | **take 2** | take 1 expression and open hands exactly right, but a blurred cream shoulder rode the right edge — the stray-Jesus defect again; must_not hardened |
| s27–s29 | ACCEPT (t1) | the gentle "go, call thy husband", her flat "I have no husband", the five-husbands frame said without a leer |
| s30 | **take 2** ACCEPT | the fully exposed, braced face — gaze off-lens, no tears yet |
| s31 | **take 4** ACCEPT | ⚠️ the frame the whole exchange exists for. Takes 1–3 lost it three ways: t2 was a straight CAMERA-GAZE portrait, t3 put a second figure in a WHITE headscarf at the right edge (cream law). Take 4: alone in frame, head off the camera axis, eyes level and off-frame right at her, warm and unchanged, no recoil and no pity, no rim-light |
| s32 | ACCEPT (t1) | the two of them still in it, the empty jar forgotten on the stones |
| s33 | **take 2** ACCEPT | "thou art a prophet" — wariness gone, working it out, gaze off-lens |
| s34/s35 | ACCEPT (t1) | the mountain question with Gerizim behind them; "God is Spirit" |
| s36 | **take 2** ACCEPT | said to herself, looking away out over the fields — not at him, exactly as the beat requires |
| s37 | ACCEPT (t1) | "I know that Messiah cometh" |
| s38 | **take 2** ACCEPT | ⚠️ THE DECLARATION. Take 1 was a symmetrical portrait staring down the lens. Take 2: camera below his eyeline, eyes lifted clearly above and past it at the woman standing over him, sweat and road dust still on him, sitting on the well stone, no grandeur and no glow — the plainest possible delivery of the largest sentence |
| s39 | **take 2** ACCEPT | utter stillness receiving it, eyes brimming, gaze off-axis |
| s40 | ACCEPT (t1) | "bottom of every list" |
| s41 | **take 2** ACCEPT | the Twelve arrive up the road with bread and basket and stop dead in a clump, every gaze angled at the well, nobody speaking or pointing (v27); Jesus and the woman still turned toward each other at the well; her jar still present here, correctly — she has not left it yet |
| s42 | **take 2** ACCEPT | the hands releasing the jar onto the stone, fingers still curved to its shape — John 4:28 landed |
| s43–s49 | ACCEPT (t1) | the run, the town she avoided, "come see a man", the town coming out, meeting their eyes, the two days, "we have heard him ourselves" — her hands EMPTY in every one of these, the row's own defect class held |

## Second-pass session (2026-08-01, Claude worker 8)

Worker 7 died mid-run after 32 first-pass accepts and 6 completed rerolls,
leaving 11 beats with no image on disk (s20, s22, s26, s30, s31, s33, s36,
s38, s39, s41, s42 — their take-1 files already moved to `_rejected/`). The
true state was read from disk, not from the commit message. The beat text
hardening for those 11 was already in place from worker 7's pass; worker 8
committed the outstanding b20 no-rope clause, re-ran `v2_prompt.py --check`
(PASS, 49 beats), and generated the 11 under a recomputed ceiling.

Of those 11, 8 passed first look. Three were rerolled for law violations:
s22 (a second bearded man IN CREAM blurred at the frame edge — the only-Jesus-
wears-cream law, plus lens gaze; fixed by re-geometring the shot to a side
three-quarter with the camera off his left and an explicit "nobody else in
the frame, no cream cloth but his own"), s31 and s38 (both camera-gaze). s22
and s31 each needed one further pass; the wording that finally stuck in all
three cases was geometric rather than prohibitive — state where the camera
sits relative to the eyeline and which frame edge the gaze exits through,
instead of only forbidding "looking at the camera".

**Reroll rate this row: 21 defect passes across 50 keeps (49 beats + 1
anchor) = 30%.** Spend across both sessions: `build-10-well` rows in
`api-spend.jsonl`, ~$9.64 total, of which worker 8's share was $1.87
(11 finishing shots + 5 reroll passes, three runs, ceilings 41.0 / 41.3 / 41.6).

## AUDIO — the row's second real finding

Row 10's V1 "final" MP4 (`media-production/build-10-well/john-4_woman-at-the-
well.mp4`) is a TRUNCATED 67.70 s render — V1 never actually finished this
row, even though the reviewer card had been pointing at it. The extracted
timeline is 294.294 s. The byte-identical-audio lock in `v2_assemble.py`
therefore cannot apply here and correctly refused to mux.

Resolution, without re-voicing anything: the master audio was rebuilt from
the authoritative per-segment mp3s in `media-production/build-10-well/audio/`
(n0, n1, n2, w9, w11, n3, j1, n4, w15, n5, w19, n6, w25, j2, n7, n8, n8b,
w29, n9, n10), each placed at its own `seg_start` from the FIXED
`extract_beats.py` with silence between — the exact timeline the windows were
cut to. Result: 294.294 s, matching the picture timeline to 6 ms. The voices
are the approved ones, unchanged; nothing was re-recorded.

## Delivery gates

| gate | result |
|---|---|
| pictures | 49/49 present in `assets-realistic/`, all native 2K (1536x2752) |
| audio | rebuilt from the authoritative segment mp3s (see above), 294.294 s, no music bed, ~1.43 s tail after the last narration |
| verify-mp4 | OK — video 294.30 s / audio 294.294 s / 21.7 MB |
| rendered frames | 12 frames extracted and eyeballed: captions bottom-band only, narrator white, the woman's KJV lines in her own colour, Jesus's KJV in red ("whosoever drinketh… shall never thirst"), question card clean |

---

## RUNNER PARK — C-FIX 2026-08-06 (Machine A `Dev`) — NEEDS-AUDIO, generated nothing

**Cameron's OPEN complaint (verbatim, from `v2_outline.py 10`):** "The only.thing
wrong with this one is how fast and meaningles Jesus pronounced the words while
telling her he was the messiah. It is a very important text and the speaker says
it too fast."

**Domain: AUDIO (pacing), not picture.** The line is `j2` "I that speak unto thee
am he." (John 4:26), the Messiah reveal, at ~3:29-3:31 in the cut. Cameron is not
naming a picture defect — he wants Jesus's spoken delivery of the most important
sentence in the story SLOWED DOWN and given weight so it lands. That is a
re-voice: regenerate narration + re-assemble. Per audio-immutability + the
RUNNER-LESSONS AUDIO-PRONUNCIATION rule, the runner is FORBIDDEN to touch audio,
so **no pictures were re-cut and no credits were spent ($0).** Shipping a
picture-rebuild over an open audio complaint would leave the fast delivery
unchanged and repeat the complaint — the worst failure. Row parked NEEDS-AUDIO.

**Why the existing fix is not enough:** `make_narration.py` already carries
`PHRASE_SPOKEN = {"j2": ("unto thee am he", "unto thee... am he")}` — but that
single ellipsis was added on 2026-07-21 to break a word-SLUR ("the Amhi"), NOT to
slow the whole line. Cameron's current complaint is about the OVERALL pace/weight
of the sentence, so one mid-line pause is insufficient.

**AUTHOR resume (audio session, not runner):**
1. In `build-10-well/make_narration.py`, give `j2` real weight — extend the
   `PHRASE_SPOKEN` override so the delivery is slow and deliberate, e.g. a
   leading pause and a pause before "am he":
   `PHRASE_SPOKEN = {"j2": ("I that speak unto thee am he", "I... that speak unto thee... am he.")}`
   (caption stays byte-identical verbatim KJV "I that speak unto thee am he" —
   only the SPOKEN/TTS string carries the pauses, exactly as the current file
   already does for the slur fix). Ear-check with `qc_narration.py` until the
   line lands slow and clear.
2. Regenerate narration (`python3 make_narration.py`) and re-assemble
   (`python3 media-production-v2/v2_assemble.py 10`). The picture timeline may
   need re-extraction if j2's duration changes (extract_beats re-times the
   j2 window); the runner's 49 stills are all present and unchanged.
3. When the corrected audio is baked into the mp4, set the board row 10 back to
   BUILT / Audio OK and hand to the picture runner to re-ship (or ship directly
   since 49/49 stills are already accepted).

**Board:** row 10 → NEEDS-AUDIO, Audio CHECK, Claim "C-FIX 2026-08-06 PARKED
NEEDS-AUDIO". No mp4 re-render this session; existing byte-identical audio still
carries the too-fast j2.

---

## AUDIO FIX DONE — j2 Messiah-reveal pacing (2026-08-07, Machine A `Dev`, AUDIO-FIX session)

**Cameron's OPEN complaint (verbatim, `v2_outline.py 10`, `reportedAgainst`
e82197c50004):** "The only.thing wrong with this one is how fast and meaningles
Jesus pronounced the words while telling her he was the messiah. It is a very
important text and the speaker says it too fast."

**Root cause:** j2 "I that speak unto thee am he" (John 4:26) — the single most
important sentence in the story — shipped at **1.67 s**, racing by. The one
mid-line ellipsis added 2026-07-21 fixed a word-slur ("the Amhi") but did nothing
for the OVERALL pace/weight Cameron is complaining about.

**Fix (audio only, $0 — edge-tts EricNeural, no Gemini, no ElevenLabs):**
- `make_narration.py` (both V1 `media-production/build-10-well/` and the V2 copy):
  `PHRASE_SPOKEN["j2"]` now rewrites the whole line with a leading pause and a
  pause before "am he" — `"I... that speak unto thee... am he"` — and a new
  `PHRASE_RATE = {"j2": "-30%"}` slows this one segment below the Jesus default
  (-22%). Caption stays byte-identical verbatim KJV "I that speak unto thee am he".
- **Only j2.mp3 was regenerated.** Every other segment mp3 is byte-identical.
  - `audio/j2.mp3`: old SHA256 `45e86b9c08f2…9e9e3` (1.67 s) → new
    `c25eb945f58e…c218e` (**4.92 s**). Old file preserved as
    `audio/j2.mp3.orig-pre-pacing-2026-08-07`.
- Chosen from 4 A/B candidates ear-checked with faster-whisper (base.en): rate
  -30% + this pause layout lands slow and clear and transcribes the exact words.

**Assembly:** row's V1 final mp4 is a truncated 67.70 s render, so
`AUDIO_FROM_V1_SEGMENTS = True` added to `beats_v2.py` — the master audio is
rebuilt from the 20 V1 segment mp3s at the extract_beats offsets (the same
timeline the 49 stills hang on). New timeline **296.6 s** (was 294.3 s; +2.3 s is
the widened j2 window). All 49 stills unchanged; picture windows auto-recomputed.
`v2_assemble.py 10` → **AUDIO REBUILD PASS**, mp4 audio-stream SHA256
`f84a7136aa4d…4fce5`, 21.9 MB, 296.6 s.

**Verified in the RENDERED mp4** (not just the segment): extracted 209.0–214.5 s
and transcribed with faster-whisper → "I, that speak unto thee, am he." spoken
across ~4.4 s with the pauses audible — the Messiah reveal now lands with weight.

**Scope discipline:** no picture regenerated, no other segment re-voiced, no
wording/timing changed outside j2. $0.00 spent, 0 rerolls.

---

## ✅ RESOLVED — j2 re-voiced to the natural middle-ground (2026-08-07, audio-fix lane, Machine A `Dev`)

Cameron's recurrence ("now its too slow and sounds horrible like a robot… undo it
and make it right") is FIXED and SHIPPED. Backed the over-slow off exactly per the
park below: **deleted `PHRASE_RATE["j2"]`** (j2 now uses the Jesus speaker default
-22%, not -30%) and **removed the LEADING ellipsis**, keeping ONE gentle mid-line
pause — `PHRASE_SPOKEN["j2"] = ("I that speak unto thee am he", "I that speak unto
thee... am he")`.

**Measured / ear-checked (faster-whisper base.en):**
- new `audio/j2.mp3` = **3.960 s** (was 4.920 s robotic; the pre-pacing "too-fast"
  take was 3.504 s — this sits deliberately between them).
- delivered mp4 at j2 (209.9 s) transcribes **"I that speak unto thee, am he."** —
  exact words, the reveal-pause is audible, no "the Amhi" slur.
- Why this exact recipe: a comma or any rate faster than -22% re-slurs "thee am he"
  into "the Amhi" (tested); only the single ellipsis AT the default -22% both breaks
  the slur AND reads like a person, not a machine dragging one word at a time. The
  robotic quality of the 4.92 s take came from the -30% drag + TWO dead-air gaps,
  both now gone.
- Only j2 changed; all other segment mp3s byte-identical. Row uses
  `AUDIO_FROM_V1_SEGMENTS=True`, so re-assembly rebuilt the track from the V1 mp3s:
  **AUDIO REBUILD PASS SHA256=cc736013…6cac0**, 295.8 s. Old 4.92 s take preserved as
  `audio/j2.mp3.robot-2026-08-07`.

Board flipped NEEDS-AUDIO→BUILT, Audio CHECK→OK; review card rewritten to answer the
recurrence in Cameron's words; deployed + live-verified.

---

## RUNNER PARK — j2 robotic recurrence (2026-08-07, Machine A `Dev`, C-FIX session)

**Cameron's OPEN complaint (verbatim, `v2_outline.py 10`):** "The only.thing wrong
with this one is how fast and meaningles Jesus pronounced the words while telling
her he was the messiah. It is a very important text and the speaker says it too
fast.. **this is what i asked before and now you messed it up now its too slow and
sounds horrible like a robot. whatever you did undo it and make it right**"

**This is a RECURRENCE, and it is AUDIO-DOMAIN — parked, NOT re-cut.** RUNNER-LESSONS:
pacing / "too fast" / "robot" complaints are out of picture-runner scope. No picture
was touched this session; all 49/49 stills remain byte-identical and accepted. The
row is flipped to NEEDS-AUDIO / Audio CHECK for the audio lane (low rows go first, so
it is picked up next tick).

**Diagnosis — why the last fix made it worse.** The 2026-08-07 AUDIO-FIX over-corrected
the too-fast complaint. It stacked THREE slow-downs on one 5-word line:
1. `PHRASE_RATE = {"j2": "-30%"}` — well below the Jesus default (~-22%),
2. a **leading** ellipsis pause ("I... that speak..."),
3. a **second** ellipsis before "am he" ("...unto thee... am he").
Result: j2.mp3 = **4.92 s** on edge-tts EricNeural — a synthetic voice dragged to
-30% with two dead-air gaps reads as the "robot" Cameron is now rejecting. The
too-fast take (`audio/j2.mp3.orig-2026-07-21`, ~1.67 s) was the opposite failure.
The target is the MIDDLE: deliberate weight without the robotic stretch.

**Available takes on disk (do NOT delete either):**
- `audio/j2.mp3` — current SHIPPED 4.92 s take (-30% + double ellipsis) = TOO SLOW / robotic.
- `audio/j2.mp3.orig-2026-07-21` — pre-pacing ~1.67 s take (single mid-line ellipsis for
  the old slur fix) = TOO FAST.

**Audio lane — do this (edit `make_narration.py`, both this V2 copy AND the V1
`media-production/build-10-well/` copy so they stay in lock-step):**
1. Back OFF the over-slow. Recommended starting point: drop `PHRASE_RATE["j2"]` to the
   Jesus default (delete the j2 entry, or set `"-22%"`), and keep AT MOST ONE gentle
   pause — the single mid-line ellipsis before "am he" that broke the old "the Amhi"
   slur — i.e. `PHRASE_SPOKEN["j2"] = ("I that speak unto thee am he",
   "I that speak unto thee... am he")`. Remove the LEADING ellipsis entirely.
2. Ear-check 3-4 candidates with `qc_narration.py` / faster-whisper. Aim ~2.6-3.2 s:
   slower than the 1.67 s racing take, clearly NOT the 4.92 s robotic drag. It must
   transcribe the exact words and land with weight but sound like a person, not a
   machine reading one word at a time. Caption stays byte-identical verbatim KJV
   "I that speak unto thee am he" — only the SPOKEN/TTS string + rate change.
3. **Only j2.mp3 regenerates.** Every other segment mp3 stays byte-identical. Preserve
   the current 4.92 s file as `audio/j2.mp3.robot-2026-08-07` before overwriting.
4. Re-assemble: `python3 media-production-v2/v2_assemble.py 10` (row uses
   `AUDIO_FROM_V1_SEGMENTS=True`; j2's new duration re-times its picture window
   automatically — 49 stills unchanged). Must print AUDIO REBUILD PASS.
5. Re-ship per PROMPT-OPUS-RUNNER step 7 (commit mp4 + boards, update review.html card
   to answer THIS recurrence in Cameron's words — "you said it went too slow/robotic;
   the reveal is now deliberate but natural, not stretched" — set new hash, deploy
   `firebase deploy --only hosting`, verify live). Flip board row 10 back to BUILT /
   Audio OK. $0 (edge-tts, no Gemini/ElevenLabs).

**Board:** row 10 → NEEDS-AUDIO, Audio CHECK, Claim "C-FIX 2026-08-07 PARKED
NEEDS-AUDIO". No mp4 re-render this session; the shipped 296.6 s mp4 still carries the
too-slow j2 until the audio lane re-voices. $0.00 spent, 0 rerolls, 0 pictures touched.

---

## ✅ SHIPPED — j2 re-voiced GENUINELY slow (2026-08-07, AUDIO-FIX lane, Machine A `Dev`)

**Cameron RE-FILED the pacing complaint against the CURRENT 3.96 s cut** (verbatim,
`v2_outline.py 10`): "how fast and meaningles Jesus pronounced the words while telling
her he was the messiah. It is a very important text and the speaker says it too fast."
The previous "middle-ground" 3.96 s single-ellipsis take was **still not enough** — the
Messiah reveal still raced by. His direct order this session: make it genuinely SLOW and
weighty — long REAL pauses, roughly **double** the line's previous duration.

**Root understanding of the past whipsaw.** The 4.92 s take was rejected as *robotic* —
but the robot came from the **-30 % RATE DRAG** stretching every word on edge-tts
EricNeural, not from the pauses. So this fix builds the weight from **real silence
between naturally-spoken phrases only** — the words stay at the Jesus default (-22 %),
never dragged — so it lands heavy without sounding mechanical.

**Fix (audio only, $0 — edge-tts EricNeural, no Gemini/ElevenLabs):**
- `make_narration.py` (both the V1 `media-production/build-10-well/` copy that the
  assembler actually reads AND the V2 copy, kept in lock-step): new `build_j2()` renders
  j2 as **three chunks at the default rate** — `"I..."`, `"that speak unto thee..."`,
  `"am he."` — joined by `J2_GAP = 0.50 s` of real silence. `PHRASE_SPOKEN`/`PHRASE_RATE`
  for j2 are gone. Splitting the chunks also **permanently kills the "the Amhi" slur**
  (thee / am-he are now separate files, not one liaison).
- **Only j2.mp3 regenerated.** Every other segment mp3 byte-identical.
  - `audio/j2.mp3`: 3.960 s (sha `8eab005c…`) → **7.728 s** (sha `775c613e…`),
    ~1.95× — essentially the requested double. Delivered as three deliberate beats
    with ~1.4 s and ~1.2 s human pauses between them.
  - Prior takes preserved, none deleted: `.midfast-2026-08-07` (3.96 s, the racing take
    he re-complained about), `.robot-2026-08-07` (4.92 s), `.orig-pre-pacing-2026-08-07`,
    `.orig-2026-07-21` (~1.67 s).

**Assembly / new baseline.** Row uses `AUDIO_FROM_V1_SEGMENTS=True`; re-assembly rebuilt
the track from the 20 V1 mp3s at the extract_beats offsets. Timeline **295.8 s → 299.537 s**
(+3.77 s = exactly the j2 growth). **AUDIO REBUILD PASS SHA256=5bb6a5f8c2ce…5390**,
21.9 MB. All 49 stills byte-identical; j2's picture window auto-re-timed.

**Verified in the RENDERED mp4** (not just the segment): extracted 207–221 s and
transcribed with faster-whisper → "I, that speak unto thee." (211.3–213.8 s) … ~1.8 s
pause … "am he." (215.6–216.2 s) … n7 resumes 217.9 s. Three deliberate beats, exact
KJV words, no slur — the reveal now lands with weight.

**Scope discipline:** no picture regenerated, no other segment re-voiced, no wording or
timing changed outside j2. $0.00 spent, 0 rerolls.
