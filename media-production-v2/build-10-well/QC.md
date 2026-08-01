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
