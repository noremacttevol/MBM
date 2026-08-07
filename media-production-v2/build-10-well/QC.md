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
