# MBM SESSION LOG — the never-ending chain link

**This is the running record of every work session on MBM. Newest entry is at the TOP.**

### How the chain works (read this if you're an AI assistant)
1. At the START of every new chat you MUST read the TOP entry below, then run
   `git log --oneline -5` and confirm the "Commit:" hash of that top entry appears
   in the history (proving that session was actually saved/pushed). Your FIRST
   message to Cameron must recap that last session and show that commit hash —
   proving you read the chain and that the previous session was saved. Do no other
   work until you've done this.
2. At the END of every session where anything happened, add a NEW entry at the top
   (copy the template), then commit and push to GitHub. That commit hash becomes the
   proof the session was saved, and the next chat verifies against it.
3. If the top entry's commit hash does NOT match `git log`, something wasn't saved —
   tell Cameron immediately instead of guessing.

### Entry template (copy this for each new session)
```
## YYYY-MM-DD — <one-line title>
- What we did:
- What changed in the app (files/commits):
- What is now true that wasn't before:
- What's next / handed off:
- Commit: aa40403
```

---

## 2026-07-09 (pt.26) — Cameron's fourth review: rescue still staging fixed; Peter #07 rebuilt as V5
- What we did: Cameron reviewed V4 and flagged the picture at 2:41 — the s8 rescue
  still had Peter reaching with two arms (one gripped by Jesus, the other raised
  open) instead of his staging law: one arm up being gripped, the other arm down in
  the water. Extended Correction #7 in PRODUCTION-BIBLE.md to cover stills as well
  as clips. Generated a new rescue still in Flow (Nano Banana 2, first try): Peter's
  right forearm gripped by the rescuing hand from above (only hem and arm visible,
  no face), left arm plunged into the sea, no tear beads. Zoom-QC'd at 2K, banked as
  s8-the-reach-v2.jpeg, updated build.py, rebuilt peter-water-07.mp4 as V5 (19.1 MB,
  256.0s), and ran Self-Revision with 10 frames covering the whole rescue window
  plus spot checks — V5 PASSED.
- What changed in the app (files/commits): media-production/PRODUCTION-BIBLE.md
  (Correction #7 stills update), build-07-peter-water/PREFLIGHT.md (V5 execution
  results), build-07-peter-water/build.py (S8 -> s8-the-reach-v2.jpeg), new asset
  s8-the-reach-v2.jpeg, qc/v5-s8 + qc/v5-final frame sets, peter-water-07.mp4 V5,
  tracker row 07 in 00-MASTER-PLAN.md.
- What is now true that wasn't before: the one-arm-in-water/one-arm-reaching staging
  law now covers stills and clips alike. peter-water-07 V5 exists and passed full
  QC; the old s8-the-reach.jpeg is dead. 0 Flow credits spent (still only).
- What's next / handed off: Cameron reviews V5. Still open: #09 rich-ruler rework
  (missing hand, fake tears, cloak drift, s7 full-back restage), re-audit of older
  videos (#1,#3,#4,#5) against all seven corrections, painted-vs-cartoon style call.
- Commit: <hash filled in after you commit>

---

## 2026-07-09 (pt.25) — Cameron caught a third arm in V3; Correction #7 added; Peter #07 sink clip restaged as V4
- What we did: Cameron reviewed V3 and rejected the sinking clip — "the guy has three
  arms he should i have one arm in the water ANd one reaching for jesus." Confirmed it
  by re-extracting every second of the V3 clip: a third sleeved forearm crosses Peter's
  chest at the 2-second mark, which the old f0/f4/f7 sampling missed. Recorded
  Correction #7 in PRODUCTION-BIBLE.md as permanent law: clip QC now extracts EVERY
  second and explicitly counts limbs; plus Cameron's staging law — a sinking person
  reaching for Jesus gets one arm down in the water and one arm reaching toward the
  Jesus presence, never both arms thrown up. Generated a new sink anchor still with
  that exact staging (one in-place edit to dissolve a face that appeared on the radiant
  figure), generated the V4 sinking clip from it, and ran per-second limb-count QC —
  all 8 frames passed with exactly two arms. Rebuilt peter-water-07.mp4 as V4 and ran
  Self-Revision (11 frames, dense over the sink window) — V4 PASSED.
- What changed in the app (files/commits): media-production/PRODUCTION-BIBLE.md
  (Correction #7), build-07-peter-water/PREFLIGHT.md (V4 execution results),
  build-07-peter-water/build.py (CLIP_SINK -> s7-sinking-v4.mp4), new assets
  (s7-sink-anchor-v4.jpeg, s7-sinking-v4.mp4), qc/v3-sink recheck frames + qc/v4-sink
  + qc/v4-final frame sets, peter-water-07.mp4 V4, tracker row 07 in 00-MASTER-PLAN.md.
- What is now true that wasn't before: seven Cameron Corrections are law. Every clip
  QC from now on counts arms/hands/legs in every extracted second. peter-water-07 V4
  exists with Cameron's exact sinking staging; V3's sink clip is dead. ~10 more Flow
  credits spent (anchor + edit were 0 credits).
- What's next / handed off: Cameron reviews V4. Still open: #09 rich-ruler rework
  (missing hand, fake tears, cloak drift, s7 full-back restage), re-audit of older
  videos (#1,#3,#4,#5) against all seven corrections, painted-vs-cartoon style call.
- Commit: 9e94911

---

## 2026-07-09 (pt.24) — Cameron rejected V2; Corrections #5/#6 added; Peter #07 fully rebuilt as V3
- What we did: Cameron reviewed V2 of peter-water-07 and rejected it — the walking
  clip didn't show Peter moving toward Jesus (and the Jesus figure read as looking
  away), and the sinking clip drifted into a different-looking character ("caveman").
  Recorded two new permanent laws in PRODUCTION-BIBLE.md: Correction #5 (motion clips
  must honor the story's geometry — person moving toward Jesus, Jesus presence facing
  them) and #6 (one character every clip — frame-check against the banked reference
  face; still-anchor pipeline mandatory for close human figures). Regenerated BOTH
  motion clips via still-anchor pipeline in Flow: two new anchor stills (Nano Banana 2,
  first-try each, zoom-QC'd against the s4 Peter reference) and two new Frames-to-video
  clips (Veo 3.1 Fast, 10 credits each). Full local frame QC on both clips (ffmpeg
  extraction + crop zooms) — both PASSED: correct geometry, stable identity, no tear
  beads, radiant Jesus figure faces Peter with no features. Rebuilt peter-water-07.mp4
  as V3 (256.0s, 19.5 MB) and ran full Self-Revision (32 frames across the runtime).
- What changed in the app (files/commits): media-production/PRODUCTION-BIBLE.md
  (Corrections #5 and #6), build-07-peter-water/PREFLIGHT.md (V3 REWORK section + V3
  execution results), build-07-peter-water/build.py (CLIP_WALK/CLIP_SINK -> v3 files),
  new assets (s5-walk-anchor-v3.jpeg, s7-sink-anchor-v3.jpeg, s5-walking-v3.mp4,
  s7-sinking-v3.mp4), qc/v3-walk + qc/v3-sink + qc/v3-final frame sets,
  peter-water-07.mp4 V3, tracker row 07 in 00-MASTER-PLAN.md.
- What is now true that wasn't before: six Cameron Corrections are law (was four).
  The still-anchor pipeline is mandatory for any clip with a close human figure.
  peter-water-07 V3 exists and passed full QC; V2 is dead. ~20 Flow credits spent.
- What's next / handed off: Cameron reviews V3. Still open: #09 rich-ruler rework
  (missing hand, fake tears, cloak drift, s7 full-back restage), re-audit of older
  videos (#1,#3,#4,#5) against all six corrections, painted-vs-cartoon style call.
- Commit: <hash filled in after you commit>

## 2026-07-09 (pt.23) — CAMERON'S CORRECTIONS become law; Peter #07 rescue rebuilt as V2; #09 sent back to rework
- What we did: Cameron reviewed the videos himself and approved NEITHER #07 nor #09. His corrections are now standing law, recorded in PRODUCTION-BIBLE.md as "The Cameron Corrections (2026-07-09)": (1) full-back shots of Jesus are a LAST resort, never the default, and never in beats where Jesus acts toward someone — prefer partial framing (a sleeve entering frame, a hem, feet at the frame edge, a shadow, off-frame light); (2) rescue/touch beats MAY show Jesus's reaching hand/forearm in a wool sleeve — Cameron's amendment to hands-never; the face stays absolutely never; (3) no fake painted tear beads — emotion lives in eyes/brows/mouth, wet shining eyes at most; (4) wardrobe locks go INSIDE the anatomy sentence of every clip prompt and clips are frame-checked against banked stills before banking. Cameron's priority: fix Peter first. The offending s8-the-catch still (full-back Jesus over drowning Peter — read as Jesus turning his back on him) was replaced: one Nano Banana 2 generation produced s8-the-reach — a single hand and forearm in a cream wool sleeve entering from the top edge, gripping Peter's wrist, warm light down the arm, no head/face/body. Zoom QC passed (grip anatomy, Peter's open 5-finger hand, no tear beads). Swapped S8 in build.py, rebuilt peter-water-07.mp4 as V2 (256.0s, 19.4MB), extracted 7 frames across the 146.6–197.5s rescue window — all pass, captions legible over the darker water (which also RESOLVES V1 watch item #1, caption contrast over the old light burst). #09's four rework items logged in its PREFLIGHT: missing hand in one scene, fake tears on the close-ups, cloak drift between the walk-away clip and the next still, and the s7 full-back restage.
- What changed in the app (files/commits): No app code. PRODUCTION-BIBLE.md: Cameron Corrections block added before "THE LOCKED LOOK". build-07-peter-water/: build.py S8 swap, assets/s8-the-reach.jpeg banked, peter-water-07.mp4 rebuilt (V2), qc/reach/ frames, PREFLIGHT.md V2 section. build-09-rich-ruler/PREFLIGHT.md: REWORK QUEUE section. Tracker: row 07 "V2 rebuilt per Cameron's correction — awaiting his look"; row 09 "❌ sent back by Cameron — rework queued".
- What is now true that wasn't before: The Cameron Corrections govern every video from now on, and every previously approved video (#1, #3, #4, #5) gets re-audited against them when its turn comes. #07 V2 is the release candidate awaiting Cameron's look. #09 V1 is rejected with a concrete 4-item rework queue.
- What's next / handed off: (1) Cameron's look at peter-water-07.mp4 V2; (2) #09 rich-ruler V2 rework pass (4 items in its PREFLIGHT); (3) re-audit of older videos against the Corrections; (4) still open: painted-vs-cartoon style call, Firebase delivery pipeline, Part C BRIDGE research, feed engine rework, comment study.
- Commit: 3c631f6

## 2026-07-09 (pt.22) — RICH YOUNG RULER #09 built end-to-end; local-frame clip-QC law born; Leighton's day shift
- What we did: Leighton said "start on next," so Story Video #9 — The Rich Young Ruler (Mark 10:17-22) — was built start to finish under the full law stack. Pre-flight on paper corrected the pack's misquote ("take up THY cross" → the real KJV "take up THE cross") and documented the pack's conscious, theological exclusion of vv23-27: the young man's story ends at v22 and the ending stays in sorrow — no softened close, no look back. 9 narration segments (Two-Voice law: Jesus speaks ONLY exact KJV Mark 10:21, slow and warm, in full silence), ear-check 9/9 PASS with the fixed qc_narration.py carried forward from build-07. Generated 8 stills + 2 motion clips: s3 (the look) banked FIRST as the reference face and every close-up verified against it. THE RUN CLIP took the full escalation path and produced this build's law: the original Veo clip passed browser-side scrubs but post-assembly frame extraction caught a bare HAND on the foreground Jesus figure; a direct regen with hardened wording failed the same way; still-anchor attempt 1 rendered a profile FACE on the Jesus figure; the restaged anchor (robed figure small and DISTANT down the road, fully from behind) passed zoom QC, and Frames-to-video from it passed full local frame QC including dedicated distant-figure crops. Rebuilt rich-ruler-09.mp4 (217.4s, 18.6MB, music dies at the start of n5 — "And Jesus let him go" — and never returns; s7, s8, and the card play in true silence). Self-Revision: 15 frames sampled across the full runtime — every law held; 2 non-blocking watch items logged (satchel-vs-belt-purse drift in the walk-away clip; faint head covering on the far distant figure in s7).
- What changed in the app (files/commits): No app code. New media-production/build-09-rich-ruler/: PREFLIGHT.md (beat map, locks, full production + V1 Self-Revision findings), make_narration.py, qc_narration.py, build.py, assets/ (7 stills + s1-run-anchor.jpeg + 2 clips), qc/ frames. Tracker row 09: Clips ✅ Cut ✅, pending Leighton review. Output: rich-ruler-09.mp4 — 1080x1920 H.264, 217.4s, 18.6MB, crf 21. AWAITING Leighton's READY-FOR-DAD mark.
- What is now true that wasn't before: #09 exists and passed every law. NEW QC LAW (recorded in PREFLIGHT findings, carry to PRODUCTION-BIBLE next session): browser scrubs are NEVER sufficient clip QC — every clip must be downloaded and frame-extracted locally (ffmpeg, every second, full frames PLUS crop zooms of any Jesus-figure region at closest approach) BEFORE banking. Hands-NEVER wording must cover EVERY figure representing Jesus; near-foreground Jesus figures are high-risk — prefer distant-from-behind staging.
- What's next / handed off: (1) Leighton's yes/no on rich-ruler-09.mp4; (2) Cameron's final yes on #07 (Leighton already marked it READY FOR DAD); (3) Cameron's painted-vs-cartoon style call; (4) next build: #06 two_sons or #08 lost_coin; (5) Firebase delivery pipeline, Part C BRIDGE research, feed engine rework, comment study all still open.
- Commit: 8436b53

## 2026-07-09 (pt.21) — PETER WALKS ON WATER #07 built end-to-end; still-anchor pipeline born; Leighton's day shift
- What we did: Leighton's shift (Cameron sleeping). Built Story Video #7 — Peter Walks on Water (Matthew 14:22-33, the FULL story) start to finish. Pre-flight on paper restored what the pack omitted: v22-23 (Jesus praying alone on the mountain — the WHY he wasn't in the boat), v26 ("It is a spirit"), and v32-33 (the wind ceasing + "Of a truth thou art the Son of God" — the summit). 13 narration segments (Two-Voice law: Jesus speaks ONLY exact KJV — Matthew 14:27, the single word "Come" of 14:29, and 14:31b as THE PEAK in dead silence). Fixed two bugs in qc_narration.py itself (SequenceMatcher autojunk collapsing long strings; whisper homophone/number spellings scored as failures) — fix recorded in PRODUCTION-BIBLE. Story earned TWO motion clips (walking, sinking). Both original Veo clips drifted to sleeveless tunics; the sinking redo passed with strengthened wrist-length-sleeve wording, but the WALKING shot failed text-to-video THREE times — beaten by a NEW pipeline: generate an anchor STILL first (stills obey wardrobe), Leighton picked "photo 7," then Frames-to-video from that still at 10 credits (after toggling OFF Flow's Agent chip, which intercepts at 100 credits). One in-place video edit rejected for turning Peter into a Jesus-lookalike (identity drift). All 12 assets banked with zoom QC; assembled build.py (256.0s, clips stretched 1.6x/1.35x, beds dead before every KJV line and through the peak, loudness -19.8→-15 LUFS). Self-Revision: 13 frames sampled — all laws held; 3 non-blocking watch items logged in PREFLIGHT (caption contrast over the s8 light burst; sinking clip runs golden vs. the storm palette; s6 still has 3/4 sleeves — future still locks get wrist-length wording).
- What changed in the app (files/commits): No app code. New media-production/build-07-peter-water/: PREFLIGHT.md (beat map, locks, production findings, Leighton's crew notes, full V1 Self-Revision findings), make_narration.py, qc_narration.py (the FIXED version — copy forward), build.py, assets/ (10 stills + 2 Veo clips), qc/ frames. PRODUCTION-BIBLE.md updated with the qc_narration fix note. Tracker row 07: Clips ✅ Cut ✅, awaiting review. Output: peter-water-07.mp4 — 1080x1920 H.264, 256.0s, 19.3MB, crf 21 first pass. AWAITING Leighton's READY-FOR-DAD mark.
- What is now true that wasn't before: #07 exists and passed every law. The still-anchor + Frames-to-video pipeline is the recorded fix for wardrobe-stubborn motion shots. Flow's Agent chip must be OFF for normal 10-credit generation. LEIGHTON'S STYLE VOTE is logged in PREFLIGHT crew notes: she prefers a cartoonish look — input to Cameron's OPEN painted-vs-cartoon decision (his call, corpus-wide).
- What's next / handed off: (1) Leighton's yes/no on peter-water-07.mp4, then Cameron's look; (2) Cameron's painted-vs-cartoon style call (Leighton's vote logged); (3) next video in THE-200 queue; (4) Firebase delivery pipeline, Part C BRIDGE research, feed engine rework, comment study on video #1 all still open.
- Commit: e2d1b36

## 2026-07-09 (pt.20) — BENT-OVER WOMAN #05 built end-to-end; #04 approved; Leighton takes over review
- What we did: Cameron approved Nicodemus #04 ("perfect approved by cameron") and handed review of the next video to Leighton (pronounced "Leeton"). Built Story Video #5 — The Bent-Over Woman (Luke 13:10-17, the FULL story) start to finish. Pre-flight on paper caught that the pack stopped at "daughter of Abraham" and omitted the ruler of the synagogue entirely — but j2 is Jesus ANSWERING that ruler — so 13:13 (glorified God), 13:14 (the ruler's objection) and 13:17 (ashamed / all rejoiced) were restored (FULL-STORY law). 16 narration segments (Two-Voice law: Jesus speaks ONLY exact KJV — Luke 13:12b and 13:15b-16), whisper ear-check 16/16 PASS (j2 needed the new medium.en tie-break — KJV phrasing, not a TTS defect; also NEW EAR-CHECK RULE born this session: any small-model FAIL is re-judged once by medium.en). Generated 10 stills + 1 Veo rising clip in Flow with zoom QC on every one. Two new Nano Banana 2 defect patterns caught and beaten: (1) stills rendering as 2-3 stacked comic panels — in-place edits can NOT remove the dividers (a retry reproduced it); fix is full regeneration with a "one single continuous scene painted edge to edge" clause (s1, s2); (2) insufficient bend — the woman rendered only mildly stooped, violating the WOMAN LOCK; fix is a targeted bend edit (s3, s4). All 11 assets banked at verified 2K (clip 720x1280 upscaled in assembly). Wrote build.py from measured durations + tails: 27 video segments, 16 audio cues, ~4s held beat after "he had already decided.", music beds fully out before BOTH KJV lines AND before the peak — the spine unbends in total silence. One assembly pass, first crf accepted. Self-Revision: 16 frames sampled — every law held; audio trace shows -91 dB in all three sacred-quiet windows. Zero rebuilds; V1 is the release candidate.
- What changed in the app (files/commits): No app code. New media-production/build-05-bent-woman/: PREFLIGHT.md (beat map, locks, prompts, full V1 Self-Revision findings), make_narration.py, qc_narration.py (with the new tie-break rule), build.py, assets/ (10 stills + Veo clip), qc/ frames. Output: bent-woman-05.mp4 — 1080x1920 H.264 30fps, 278.0s, 20.1MB, crf 21 first pass. AWAITING Leighton's one look.
- What is now true that wasn't before: #04 is APPROVED. #05 exists and passed every law on first assembly. Leighton is the reviewer going forward. The ear-check has a tie-break law, and the two Nano Banana 2 failure modes (panel-split, under-bend) have known, recorded fixes.
- What's next / handed off: (1) Leighton's yes/no on bent-woman-05.mp4; (2) next video in THE-200 queue; (3) Firebase delivery pipeline still unbuilt; (4) painted-vs-cartoon style call, Part C BRIDGE research, feed engine rework, comment study on video #1 all still open.
- Commit: a21b8d2

## 2026-07-09 (pt.19) — NICODEMUS #04 built end-to-end under the full law stack; V1 clean on first assembly
- What we did: Cameron approved Zacchaeus V3 ("beautiful and approved lets go to the next"), so Story Video #4 — Nicodemus at Night (John 3, full arc through John 7:50-51 and 19:39) — was built start to finish. Pre-flight on paper caught the pack's invented ending (FULL-STORY law): the real arc — the daylight council defense and the hundred-pound royal burial — is the point, so the video runs ~367s instead of the pack's 60s. Wrote 18 narration segments (Two-Voice law: Jesus speaks ONLY exact KJV — John 3:3, 3:8, and 3:16-17 as THE PEAK), whisper ear-check 18/18 PASS. Generated 10 stills + 1 Veo street clip in Flow with anatomy-count QC at zoom on every one; caught and fixed a pair of modern eyeglasses on the council table (free Nano Banana edit) and rode out one "Upscaling Failed" retry; all eleven assets banked at verified 2K (1536x2752). Wrote build.py from measured mp3 durations + measured trailing silences: 25 video segments, 18 audio cues, a deliberate 6.3s held beat after "So he came at night.", detuned-pair music beds all fully out before every KJV line, and 2.1s of dead silence before John 3:16-17 (RMS trace confirms -83 dB right before the peak enters at 198.5s). One assembly pass, first crf accepted. Self-Revision sampled 21 frames across 366.6s: every law held (silhouette, burial, captions, anatomy, no anachronisms) — zero rebuilds; V1 is the release candidate.
- What changed in the app (files/commits): No app code. New media-production/build-04-nicodemus/: PREFLIGHT.md (beat map, locks, prompts, full V1 Self-Revision findings), make_narration.py, qc_narration.py, build.py, assets/ (10 stills + Veo clip), qc/ frames, build.log. Output: nicodemus-04.mp4 — 1080x1920 H.264 30fps, 366.7s, 19.95MB, sacred-quiet peak verified. Also folds in the earlier 00-MASTER-PLAN.md tracker edit. AWAITING Cameron's one look.
- What is now true that wasn't before: Video #4 exists and passed every law on its first assembly — the first build in the series to need zero regenerations after banking (the pre-flight-on-paper + anatomy-count-at-bank-time discipline is paying for itself).
- What's next / handed off: (1) Cameron's yes/no on nicodemus-04.mp4; (2) next video in THE-200 queue; (3) Firebase delivery pipeline still unbuilt; (4) painted-vs-cartoon style call, Part C BRIDGE research, feed engine rework, comment study on video #1 all still open.
- Commit: 1ed15ed

## 2026-07-09 (pt.18) — ZACCHAEUS V3: Cameron's v2 rejection births the ANATOMY-COUNT and PHYSICALITY CALIBRATION laws
- What we did: Cameron rejected V2 in one message: three feet on the man in the tree ("these are simple things you should be able to watch for") and the shortness pushed into a demeaning dwarf-like caricature in every frame ("you took the short man too far... its to much"). Two permanent Bible laws written from it: ANATOMY-COUNT QC (on the QC zoom of every still and sampled frame, literally count 2 arms, 2 hands, 2 legs, 2 feet, 1 head per figure — wrong count = automatic regenerate) and PHYSICALITY CALIBRATION (a relative trait is calibrated, never caricature: short = short ADULT, normal proportions, head about level with other men's shoulders; the fix for "doesn't read" is scale references, never bigger distortion). Recalibrated the character lock to "a short grown man... of completely normal adult build and proportions — simply a head shorter than the men around him." Regenerated all 9 Zacchaeus stills in Flow under the new lock and QC'd each with literal limb counts: 3 needed free Nano Banana edits (shot5-lit: unrequested Jesus-faced crowd removed; shot2-blocked: shortness didn't read + he faced the camera calmly → made a head shorter, on tiptoes, craning; and in Self-Revision, shot7-table: the standing figure behind Zacchaeus read as Jesus with a fully visible face — passed in still QC as "a servant," caught on the timeline where the narration says Jesus is in the house — removed, since Jesus appears lawfully from behind in shot8). New QC lesson recorded: judge every still in STORY CONTEXT — ask who the viewer will think a figure is at that beat. The climb shot verified at tight zoom: exactly two sandaled feet. Rebuilt on the UNCHANGED V2 timeline/narration/audio; Self-Revision sampled 16 frames across 249.0s with anatomy counts + proportion checks on every one.
- What changed in the app (files/commits): No app code. PRODUCTION-BIBLE.md §4b + two new laws (PHYSICALITY CALIBRATION, ANATOMY-COUNT QC, dated 2026-07-09). build-03-zacchaeus/: PREFLIGHT.md V3 section (Cameron's words verbatim, the calibrated lock, V3 scene lines, full Self-Revision findings), assets/ — 9 stills replaced (all 1536x2752 2K). Output: zacchaeus-03.mp4 V3 — 1080x1920 H.264 30fps, 249.0s, 20.0MB. AWAITING Cameron's one look.
- What is now true that wasn't before: Every future QC pass literally counts limbs on every figure, physical traits are calibrated with dignity instead of exaggerated, and stills are judged in story context so a stray face can never silently become Jesus.
- What's next / handed off: (1) Cameron's yes/no on zacchaeus-03.mp4 V3; (2) next video in THE-200 queue; (3) Firebase delivery pipeline still unbuilt; (4) painted-vs-cartoon style call, Part C BRIDGE research, feed engine rework, comment study on video #1 all still open.
- Commit: 6788abf

## 2026-07-09 (pt.17) — ZACCHAEUS V2: full rebuild from Cameron's rejection — the CLARITY/WHY, STUDY-GEM, and RELATIVE-PHYSICALITY laws are born
- What we did: Cameron rejected zacchaeus v1 with five notes: (1) confusing, doesn't get the point — explain WHY Jesus does what he does; (2) add scripture-study insights; (3) address the common "wasn't his name Matthew?" mix-up; (4) stay true to the story, small connecting tidbits only; (5) Zacchaeus must read as SHORT in every single frame. Turned each note into permanent Bible law: CLARITY/WHY-LAW (every surprising action in a script must carry its WHY), STUDY-GEM TIDBITS (weave in what scripture students collect — the fourfold repayment, the traded dignity, what a shared meal meant), and the RELATIVE-PHYSICALITY LOCK (a physical trait is stated RELATIVE to visible people in every image prompt, with a taller adult in frame for scale, and QC zoom must confirm the trait reads instantly). Rewrote the entire script from scratch — 18 narration segments opening with the Matthew/Zacchaeus clarification, every beat carrying its WHY, exact KJV only in the Jesus voice (19:5, 19:9, 19:10), ear-checked ALL PASS (j1a re-cut at -22% after the -25% take slurred "Zacchaeus" and failed BOTH whisper models). Regenerated all ten stills in Flow under the relative-shortness lock, zoom-QC'd each (short reads instantly; Jesus face never visible), 2K downloads verified by resolution. Rebuilt to a 249.0s timeline (25 video segments, 18 audio cues, dual detuned beds with the sacred silence before the look up). Self-Revision PASS 1 caught a real lesson: the final-mux maxrate must be COMPUTED FROM RUNTIME (24.5MB×8/249s ≈ 787k total → 640k video cap), not copied from a shorter video — v1's 1200k cap gave 31.3MB at every crf. Re-muxed → 20.1MB, crf 21 veryslow, -14.8 LUFS. PASS 2: NOTHING FOUND (only the four planned silences; motion clip 2.38 vs still 1.37; 15 QC frames verified all laws).
- What changed in the app (files/commits): No app code. PRODUCTION-BIBLE.md §4b + three new laws (CLARITY/WHY, STUDY-GEM TIDBITS, RELATIVE-PHYSICALITY LOCK, dated 2026-07-09). build-03-zacchaeus/: make_narration.py (18 V2 segments), build.py (25-segment 249.0s timeline, runtime-computed rate cap with the lesson in a comment), PREFLIGHT.md (V2 script, prompts, self-revision findings). Output: zacchaeus-03.mp4 V2 — 1080x1920 H.264 30fps, 249.0s, 20.1MB, -14.8 LUFS. AWAITING Cameron's one look.
- What is now true that wasn't before: Zacchaeus exists as a V2 that answers all five rejection notes, and the three new laws mean every future video explains its WHYs, carries study gems, and locks physical traits relatively so they can never silently vanish. The size law is now computed from runtime, never inherited.
- What's next / handed off: (1) Cameron's yes/no on zacchaeus-03.mp4 V2; (2) next video in THE-200 queue; (3) Firebase delivery pipeline still unbuilt; (4) painted-vs-cartoon style call, Part C BRIDGE research, feed engine rework, comment study on video #1 all still open.
- Commit: b2ebe8e

## 2026-07-09 (pt.16) — VIDEO #3 ZACCHAEUS built end-to-end under the full law stack — first video born under the Assembly Craft Laws
- What we did: Cameron approved the craft-pass prodigal ("yeah i think it got better lets go to the next one"), making #2 the fourth approved video (#1, #8, #6, #2). Built Story Video #3 — Zacchaeus (Luke 19:1-10) — the first video built under the Assembly Craft Laws from the first frame. Full §4b pre-flight ON PAPER first: KJV fetched via bible-api.com and read END-TO-END; the FULL-STORY check caught (at zero cost) that the production pack stopped at "he changed because Jesus came first" and marked v10 "optional" — repeating the Prodigal omission. All ten verses are in the build: the murmuring crowd (v7), the standing gift (v8), and Jesus's true last words KJV 19:9-10 in the Jesus voice. 16 narration segments generated (Andrew narrator / Christopher Jesus, exact KJV only) and ear-checked ALL PASS — including a new tie-break law: whisper-small misheard "Zacchaeus" as "secchias" (0.90) while medium.en heard it perfectly (1.00), so any FAIL is now re-judged once by medium.en before it counts (a real TTS defect fails both). 8 stills + 1 Veo 3.1 Fast motion clip (the look up — the money moment) generated in Flow; shot3-run's first take broke the character lock (no gold trim, no cream tunic) and was regenerated rather than let a visible inconsistency through; every download verified by resolution (1536x2752), not filename. Jesus face zoom-verified never visible in every frame he appears in. Assembled under all five Craft Laws; Self-Revision pass 1 CLEAN (silences all planned and ≤2.4s + the intended sacred quiet before the look up, captions fade, card 5 lines within width, -14.8 LUFS, 16.0MB at crf 21, motion smooth).
- What changed in the app (files/commits): No app code. New media-production/build-03-zacchaeus/: PREFLIGHT.md (full-story finding, locks, beat map, 9 verbatim prompts, clean self-revision pass), make_narration.py (16 segments), qc_narration.py (with the medium.en tie-break law), build.py (17 video segments incl. the Veo clip split into two caption beats via clip_start trim, dual detuned beds — bed1 silent BEFORE the look up, bed2 out before the final KJV). Output: zacchaeus-03.mp4 — 1080x1920 H.264 30fps, 131.3s, 16.0MB, -14.8 LUFS. AWAITING Cameron's one look. Credits: 10 (one Veo clip; all stills free on Nano Banana 2).
- What is now true that wasn't before: Video #3 exists, complete (all ten verses), and is the first built under the Assembly Craft Laws from scratch — no craft retrofit needed. The ear-check now has a proper-noun tie-break so rare biblical names can't false-positive.
- What's next / handed off: (1) Cameron's yes on zacchaeus-03.mp4; (2) next video in THE-200 queue; (3) Firebase delivery pipeline still unbuilt; (4) painted-vs-cartoon style call, Part C BRIDGE research, feed engine rework, comment study on video #1 all still open.
- Commit: 40658b5

## 2026-07-09 (pt.15) — "it just seems like a video made by ai, it glitches" — the ASSEMBLY CRAFT LAWS are born
- What we did: Cameron pushed for true best-quality work on the full-story prodigal cut. Root-caused four real craft defects instead of tweaking blindly: (1) KEN BURNS SHIMMER — ffmpeg's zoompan rounds its crop position to whole pixels every frame; rendered straight at 1080 that stepping is the classic "AI slideshow" jitter. Fix: every move now rendered supersampled (4320x7680 in → 2160x3840 out → lanczos down to 1080x1920) so steps land on quarter-pixels — measured frame-to-frame motion variation HALVED (cv 0.22 → 0.11). (2) CAPTION POP — captions appeared/vanished in a single frame at every cut. Fix: each caption (text+box+shadow) rendered on its own transparent RGBA layer and alpha-faded 0.5s in/out as one piece, then overlaid. (3) STARVED ENCODE — the final pass had been squeezed to 1050k/crf24 to fit the 25MB law, causing blockiness. Fix: intermediates near-lossless crf 16, final preset veryslow starting crf 21 with an automatic step-up loop only if size demands — landed crf 21 at 20.1MB. (4) THIN AUDIO — the music bed was four bare sine waves and the entire second half played bone dry; the mix sat at -19.6 LUFS (quiet reads as amateur). Fix: every bed voice is now a detuned pair (natural slow beating) through a soft room echo; a quieter second bed sits under the feast/brother section (70.5–130.5) and fades to full silence before the father's final KJV answer; loudness measured and lifted +4.6dB to -14.8 LUFS with a true-peak limiter (measurement automated in build.py). Full Self-Revision pass on the rebuilt file: all four silences planned and ≤2.2s, caption fades verified frame-by-frame at a cut, frame strip clean, feast detail crop shows no blocking. All four fixes written into Bible §4b as the dated ASSEMBLY CRAFT LAWS so every future video is built this way from the start.
- What changed in the app (files/commits): No app code. PRODUCTION-BIBLE.md §4b + Assembly Craft Laws block (anti-shimmer, caption fades, encode, loudness, music bed — dated 2026-07-09). build-02-prodigal/build.py reworked (supersampled zoompan, RGBA caption overlays, dual detuned music beds, automated R128 loudness gain, crf step-up mux); PREFLIGHT.md findings +1. Output: prodigal-02.mp4 — 1080x1920 H.264 30fps, 162.8s, 20.1MB, crf 21, -14.8 LUFS. AWAITING Cameron's one look.
- What is now true that wasn't before: The pipeline no longer produces the "AI slideshow" tells — motion is subpixel-smooth, captions dissolve, the encode isn't starved, and loudness is delivered at platform level, automatically. These are laws now, not one-off fixes.
- What's next / handed off: (1) Cameron's yes on the craft-pass prodigal-02.mp4; (2) next video in THE-200 queue built under the new laws; (3) Firebase delivery pipeline still unbuilt; (4) painted-vs-cartoon style call, Part C BRIDGE research, feed engine rework, comment study on video #1 all still open.
- Commit: 79698fb

## 2026-07-09 (pt.14) — VIDEO #2 REJECTED for telling HALF the parable — rebuilt with the older brother; FULL-STORY LAW born
- What we did: Cameron rejected the pt.13 cut: "you didnt tell the entire story... the other son is the other side of the stroy and ommiting it leaves out half of it." He was right — the cut ended at the feast and omitted Luke 15:25-32 entirely, the half aimed at the very religious men the parable was told to answer. The pre-flight loop did NOT catch this; Cameron did. Response: (1) a permanent FULL-STORY check added to Bible §4b, placed FIRST in the audio checklist, dated 2026-07-09, with the honest note that Cameron caught it, not the loop — before generating any audio, read the parable's scripture END-TO-END against the beat map through the FINAL verse; (2) fetched exact KJV Luke 15:25-32, mapped 7 new beats on paper in PREFLIGHT.md (incl. OLDER BROTHER character lock; noted his crossed arms are the scene's point — the crossed-arms ban applies to the waiting father only); (3) rewrote n7 (old line "Jesus ended the story with the father's own words" was now FALSE), wrote n9/n10a/n10b/n11 narration, j2a/j2b exact KJV 15:31-32 as the TRUE last story words, and the card question rewritten to the canonical three-character version (son who left / father who ran / brother who stayed and felt unseen); all 17 segments ear-checked (1.00 except j2b 0.99, all pass); (4) two new stills on Nano Banana 2 (free): shot8-brother-outside (feast light vs cool night, rigid fists), shot9-father-entreats (open pleading hand), both QC'd and 2K'd; (5) rebuilt from measured spoken-ends. Self-Revision loop found three things and fixed all: 27.6MB over the 25MB cap (mux tightened to crf 24 / maxrate 1050k → 20.5MB), the breath before the card measured 2.50s at the No-Dead-Air limit (n8 pulled 149.9→149.5), and the closing card's long lines CLIPPED at both frame edges at 50pt (re-broken to ≤31-char lines; caption-crop QC caught it). Final pass found nothing.
- What changed in the app (files/commits): No app code. PRODUCTION-BIBLE.md §4b + FULL-STORY check. build-02-prodigal: PREFLIGHT.md second-half section, make_narration.py (17 segments), build.py (16 video segments, 162.8s timeline, tighter mux), assets +2 stills, all audio regenerated. Output: prodigal-02.mp4 — 1080x1920 H.264 30fps, 162.8s, 20.5MB, whole parable, KJV 15:24 at the feast + KJV 15:31-32 to the older brother as the last spoken story words, 14.5s read-aloud card. AWAITING Cameron's one look.
- What is now true that wasn't before: Video #2 tells the COMPLETE parable — both sons, both times the father goes out. No future video can ship a partial parable: the Full-Story check is the first thing the pre-flight asks. Credits this session: 0 (both new stills free on Nano Banana 2).
- What's next / handed off: (1) Cameron's final yes on the full-story prodigal-02.mp4; (2) next video in THE-200 queue; (3) Firebase delivery pipeline still unbuilt; (4) painted-vs-cartoon style call, Part C BRIDGE research, feed engine rework, comment study on video #1 all still open.
- Commit: 6328de8

## 2026-07-08 (pt.13) — VIDEO #2 THE PRODIGAL SON built RIGHT-FIRST-TIME — the pre-flight system's proving run
- What we did: Cameron challenged: "fine prove it to me with the next one" — build the next video with ZERO revision rounds, using the new Bible §4b RIGHT-FIRST-TIME PRE-FLIGHT (written this session, commit c4b7871). Executed it on #2 The Prodigal Son (Luke 15:11-32): full pre-flight ON PAPER first (PREFLIGHT.md — scripture card, storyboard s00–s08, complete narration script checked against every law, character/wardrobe locks, all 7 prompts written and scanned before submission). The pre-flight caught two would-be defects before they cost anything: the pack's "tears streaking into his beard" in the run clip (same instant-liquid AI tell as #6's sweat) was cut from the motion prompt, and the pack's 6s card was replanned to 13s + read aloud. Results: narration ear-check 1.00 on ALL 11 segments first try (zero rewrites); 6 stills + 1 Veo Fast run clip all passed QC on first generation (10 credits total spent); assembly from measured durations. The Self-Revision loop found exactly ONE thing: j1's mp3 carries a ~1.2s silent tail inside the file, stretching the planned 2s breath before the card to 3.46s (over the 2.5s law) — fixed (n8 93.0→92.0) and, per the §4b standing rule, a new dated check was added to the Bible: measure mp3 internal tails; compute breaths from the SPOKEN end, not the file end. Second pass found nothing.
- What changed in the app (files/commits): No app code. NEW media-production/build-02-prodigal/ (PREFLIGHT.md, make_narration.py, qc_narration.py, build.py). PRODUCTION-BIBLE.md §4b +1 check (mp3 internal tails, 2026-07-08). Output: prodigal-02.mp4 — 1080x1920 H.264, 104.2s, 17.2MB, ONE motion clip (THE FATHER RUNS, music cut to silence before "The father ran."), KJV Luke 15:24 as the last story words, 13s read-aloud card. AWAITING Cameron's one look.
- What is now true that wasn't before: The pre-flight system works — one build, zero Cameron-visible revision rounds, 10 credits, and the only loop finding became a permanent check the same hour. Video #2 is built and presented; approval pending.
- What's next / handed off: (1) Cameron's final yes on prodigal-02.mp4; (2) next video in THE-200 queue after #2; (3) Firebase delivery pipeline for approved videos still unbuilt; (4) painted-vs-cartoon style call, Part C BRIDGE research, feed engine rework, comment study on video #1 all still open.
- Commit: bf24b50

## 2026-07-08 (pt.12) — VIDEO #6 APPROVED ("actually perfect now") after 5 revisions — the AI grows ears and the Self-Revision Law is born
- What we did: Produced #6 The Two Sons (Matthew 21:28-32) end-to-end and got Cameron's yes — but it took 5 revision rounds, and every failure became permanent law. The road: (1) all six visual scenes approved on sight; (2) Shot 4 clip v1 rejected (sweat appeared instantly on the head-wipe — AI tell) → v2 retake with NO sweat/wipe beat, positive-only phrasing, passed frame QC; (3) first cut rejected — 16 seconds of dead air mid-video ("it just stops talking, it's broken") → new narration n2c/n2d so the narrator carries EVERY scene; (4) second cut rejected on three counts — TTS stumbled on "he just went to work" (reworded), the narrator re-quoted Jesus's KJV "twain" line (now gives only the plain modern meaning), and the closing card cut away before it could be read (now held 13s AND read aloud); (5) the fix introduced a NEW bug — the Multilingual narrator voice drifted into foreign accents on words Cameron never flagged. He escalated: stop wasting my time and credits, find a better way. Root cause: the AI couldn't hear its own audio. Answer: built qc_narration.py — an EAR-CHECK that transcribes every narration mp3 with faster-whisper and diffs it word-for-word against the script (≥0.93 or fail) — and banned Multilingual voices permanently (narrator is now plain en-US-AndrewNeural). Rebuilt, all 12 segments verified, silencedetect clean. Cameron: "thats good its actually perfect now" — and mandated the whole revision discipline become automatic. Written into the Bible as the SELF-REVISION LAW: re-read the bible, ear-check, silence-scan, frame-strip, watch as a stranger, fix and loop until a pass finds nothing. Cameron sees a video ONCE, for the final yes.
- What changed in the app (files/commits): No app code. NEW media-production/build-06-two-sons/ (build.py, make_narration.py, qc_narration.py — the reusable ear-check). PRODUCTION-BIBLE.md gained five laws (all Cameron, 2026-07-08): Multilingual-voice ban, Ear-Check Law, No-Dead-Air Law, Translation Law, Readable-Card Law, plus the Self-Revision Law. Output: two-sons-06.mp4 — 1080x1920, 104.0s, 17.2MB, APPROVED.
- What is now true that wasn't before: Video #6 has cleared the Approval Law (third approved video: #1, #8, #6). The AI has ears — narration is machine-verified against the script before assembly, forever. Cameron is the approver, not the QC department. Credits this video: ~20 (Shot 4 clip + its retake; all stills free).
- What's next / handed off: (1) next video in the corpus queue; (2) Firebase delivery pipeline for approved videos (#1, #8, #6) still unbuilt; (3) Cameron's painted-vs-cartoon style call still open; (4) still pending: Part C BRIDGE research, feed engine rework, comment study on video #1.
- Commit: 5eee413

## 2026-07-08 (pt.11) — VIDEO #8 APPROVED BY CAMERON: two-coins fix, God's-joy opening, and the Prompt Failure Log is born
- What we did: Cameron reviewed the READY FOR DAD cut and caught two problems: the found-coin clip looked too AI, and after she picked up her coin a SECOND coin was still lying on the floor (so it read like she found two). First fix attempt FAILED badly — I put a "NEGATIVE PROMPT:" list into the Veo prompt and strengthened the 2D-animation wording; it came back flat-cartoon (verdict: "horrible, way worse") and wasted 10 credits. That failure is now permanently documented in PRODUCTION-BIBLE.md as new section "5b. PROMPT FAILURE LOG" with two standing bans: (1) never put a negative-prompt list in a Veo prose prompt — naming what you don't want can pull it INTO the video; say what you WANT, positively; (2) never add/strengthen style words beyond the byte-identical Master Style Block. The v4 retake followed those rules ("EXACTLY ONE small silver coin — one single coin, and only that one coin, in every frame"; "the patch of floor where it lay is now bare swept earth, completely empty") and passed QC: one coin start-to-finish, floor bare after pickup, saucer-lamp lock held, camera stays on her after the pickup so no stray-coin floor shot is even possible. Also per Cameron: the video now OPENS with why Jesus told the story — new shot s00 on the starry sky, narration "When Jesus wanted to show how God feels about one lost soul, he didn't talk about crowds. He told this story." — bookending the closing starry-sky "Over one. Not a crowd. One." and the everyone-is-special closing question. Cameron watched the final cut: APPROVED ("thats good dad approves").
- What changed in the app (files/commits): No app code. PRODUCTION-BIBLE.md +section 5b Prompt Failure Log. build-08-lost-coin/build.py (s00 opening, all audio offsets +10.5s, MUSIC_END 57.5, CLIP_FOUND → Woman_finding_single_coin_202607082018.mp4), make_narration.py (+n0). Output: lost-coin-08.mp4 — 1080x1920, 80.0s, 13.5MB, APPROVED.
- What is now true that wasn't before: Video #8 The Lost Coin has cleared Cameron's Approval Law. The Prompt Failure Log exists — every credit-wasting prompt mistake gets a dated entry + ban before any retry. Reusable pattern proven: for object-reveal beats, state the object count and post-pickup emptiness positively. Credits this segment: ~20 (2 Veo Fast redos; ~50 total for video #8).
- What's next / handed off: (1) DELIVERY of approved lost-coin-08.mp4 (Firebase pipeline still unbuilt); (2) Cameron's painted-vs-cartoon style call STILL open — Veo renders people smoother-skinned than the painted stills, and it bothered Cameron enough to flag "too AI"; worth a dedicated style test before video #6; (3) next production: #6 The Two Sons; (4) still pending: Part C BRIDGE research, feed engine rework, comment study on video #1.
- Commit: 491fb8e

## 2026-07-08 (pt.10) — VIDEO #8 THE LOST COIN: built end-to-end on Leighton's first solo day shift — READY FOR DAD
- What we did: Leighton (day shift) ran production of video #8 The Lost Coin (Luke 15:8-10) with the AI driving Flow per the Bible + Crew Guide. All 6 scenes generated as painted stills (Nano Banana 2, free) + 1 Veo 3.1 Fast money-moment clip; Leighton gave keep/redo verdicts throughout and caught THREE real QC failures the AI's prompts then fixed: (1) wardrobe drift (her clothes kept changing → wardrobe-lock phrase "ONE plain rough undyed brown wool dress, no apron, no jacket" now in every prompt), (2) lamp continuity (the found-clip lamp morphed into a pot → lamp-lock phrase "SMALL SHALLOW CLAY OIL LAMP, flat saucer, NOT a pot NOT a jug", 10-credit redo), (3) coin pop-in (the coin appeared from nothing → redo with "coin present from the VERY FIRST FRAME, half-buried in dust, gradually UNCOVERED, NEVER pops into existence", 10-credit redo — this phrasing works and should be reused for any object-reveal beat). Also proved the "arrange for countability" trick: when the 9 coins couldn't be counted at screen resolution, a free Nano Banana edit arranged them "in three neat rows of three so they are clearly countable." Downloaded all approved assets (stills at 2K), generated two-voice narration (edge-tts; narrator Andrew, Jesus en-US-ChristopherNeural speaking ONLY exact KJV Luke 15:9 + 15:10), assembled locally with ffmpeg per the build-01 pattern. Full QC pass: 10-frame montage verified, audio windows measured (music bed fades out by 47s so the angels line lands in dead silence; card tail at -91dB). Leighton watched the final cut and marked it READY FOR DAD.
- What changed in the app (files/commits): No app code. NEW media-production/build-08-lost-coin/ (build.py, make_narration.py, .gitignore; media local-only). Output: lost-coin-08.mp4 — 1080x1920 H.264, 69.5s, 11.6MB.
- What is now true that wasn't before: Video #8 is assembled and awaiting Cameron's final yes (the Approval Law). The crew system works in practice — an 11-year-old operator + AI assembly line produced a finished video in one shift, and her catches produced two new permanent prompt locks (wardrobe-lock, lamp/prop-lock) plus the no-pop-in reveal phrasing. Credits used this session: ~30 (3 Veo Fast clips incl. redos; all stills/edits free).
- What's next / handed off: (1) Cameron watches lost-coin-08.mp4 → yes/no (it's at media-production/build-08-lost-coin/lost-coin-08.mp4); (2) Cameron's painted-vs-cartoon style call from the pt.9 cartoon test still open; (3) next production: #6 The Two Sons; (4) Firebase delivery pipeline for approved videos; (5) still pending: Part C BRIDGE research, feed engine rework, comment study on video #1.
- Commit: 7cc1169

## 2026-07-08 (pt.9) — THE CREW SYSTEM: Ultra $200 active, Leighton joins as day-shift operator, factory goes round-the-clock
- What we did: Cameron reviewed v2 of video #1 — verdict: factually right, but paces slow and reads AI-made; HOLD it as-is, gather real viewer comments, study them to improve future videos (now the Feedback-Study Law in the Bible, with pacing + human-feel as the first improvement targets). Cameron bought Google AI Ultra $200/mo (25,000 credits) to produce the corpus at full speed this month. He's adding his daughter Leighton (11) as day-shift crew so production runs around the clock while he sleeps — and so she learns AI by watching it work. Built the human side of the factory: NEW media-production/CREW-GUIDE.md — who does what (AI does prompting/Chrome-driving/QC/assembly; crew answers story questions and reacts), shift handoff phrases ("Leighton is working on it for the day" / "this is cameron again"), the session script, the learning goal (AI teaches while working; prompt-only mode when the crew wants to drive), crew safety rails, the queue, and the video-vs-spoken-only decision guide. Encoded the Approval Law in the Bible: Cameron's final yes ships every video; Leighton marks videos "READY FOR DAD" and continues the queue.
- What changed in the app (files/commits): No app code. NEW media-production/CREW-GUIDE.md. PRODUCTION-BIBLE.md: Approval Law, Feedback-Study Law, active plan updated to Ultra $200 (25,000/mo, Veo Fast 10 credits/clip).
- What is now true that wasn't before: The factory has an operating manual any crew member can follow. Ultra is live — constraint is throughput, not credits. Next two productions stay the locked low-animation validators: #8 The Lost Coin, then #6 The Two Sons. Video #1 is held-as-approved, awaiting viewer comments.
- What's next / handed off: (1) Start #8 The Lost Coin — full assembly line per the Bible + Crew Guide, applying the pacing/human-feel targets; (2) collect and study comments on video #1; (3) Firebase delivery pipeline for approved videos; (4) still pending: Part C BRIDGE research, feed engine rework.
- Commit: a979d87

## 2026-07-07 (pt.8) — v2 REBUILT per Cameron's feedback: American Jesus voice (permanent law), fuller story, sequencing fixes (awaiting yes/no)
- What we did: Cameron reviewed the v1 prototype and gave 4 fixes; all executed. (1) VOICE: the British Jesus voice is banned permanently — Jesus is now en-US-ChristopherNeural (American, warm, low). Encoded as **The Voice Law** in PRODUCTION-BIBLE.md §1. (2) FULLER STORY: encoded as **The Full-Story Law** in the Bible — never flatten a story to its headline moment. v2 narration now includes the Jairus backstory (Jesus was already on his way to a ruler's dying twelve-year-old daughter; the crowd made one sick woman nearly invisible), that he FELT power go out of him, a SECOND red-letter line — exact KJV Mark 5:30 "Who touched my clothes?" — the disciples questioning him, and that he ignored them and kept looking until he found her. (3) SEQUENCING: the ~58s bug (narration "he turned" over a walking-away still) fixed — the turn beat now sits on the animated turn clip itself with the Mark 5:30 line. (4) REDUNDANCY: the tassel-touch still removed; the animated hem clip carries that beat alone. Generated 2 new painted stills FREE in Flow (disciples exchanging puzzled glances; hooded man from behind walking down a stone street for the backstory beat — purpose-built after QC caught a continuity risk in the repurposed walking-away still), QC'd both, downloaded at 2K. Regenerated all 11 narration files (edge-tts), rebuilt, full QC pass: frame montage in correct order, face law holds, audio windows verified (sacred pause dead silent at -91dB before the Mark 5:34 line).
- What changed in the app (files/commits): No app code. media-production/build-01-cloak/build.py and make_narration.py rewritten to v2; PRODUCTION-BIBLE.md gained the Voice Law + Full-Story Law; 01-cloak-production-pack.md narration script replaced with v2. Output: cloak-01-prototype.mp4 now 134.5s (2:14), 22.5MB, 1080×1920.
- What is now true that wasn't before: Two permanent laws exist that govern all 200 videos: the Jesus voice is AMERICAN forever, and stories keep their surrounding humanity (backstory + resistance beats). Video #1 v2 is built and QC'd. Credits unchanged: ~160 of 1,000 Pro remaining (both new stills were free).
- What's next / handed off: (1) Cameron watches v2 and says yes/no; (2) on yes → Firebase delivery + the two locked LOW-ANIMATION validation stories; (3) Cameron's Ultra purchase call still open; (4) narrator voice still a placeholder he can veto (Jesus voice law now fixed: American); (5) still pending from pt.5: Part C BRIDGE verification research; feed engine rework.
- Commit: b674176

## 2026-07-07 (pt.7) — PROTOTYPE FINISHED: video #1 fully assembled in the new painted-storybook style (awaiting Cameron's yes/no)
- What we did: Continued from the style pivot (Cameron rejected all 8 photoreal clips; hand-painted 2D storybook animation is the permanent locked look — see PRODUCTION-BIBLE.md, commits 98dabff/e25d4db). Ran the full assembly line for video #1 "The Woman Who Touched His Cloak" solo, per the Bible: (1) generated all 12 painted stills in Flow Image mode (Nano Banana 2, 9:16, FREE — 0 credits), retaking still 4 (crowd) and still 8 (photoreal drift + wrong-age woman) until they passed QC; (2) generated the turn/"Daughter" money-moment clip in Veo 3.1 Fast (20 credits), QC'd frame-by-frame — face never visible, hands never visible; (3) downloaded all 14 assets (12 stills at 2K + the gold-standard hem-touch clip + the turn clip); (4) assembled locally with ffmpeg + edge-tts (all free): Ken Burns drift over the stills, the 2 animated clips at their money beats, two-voice narration (modern narrator; Jesus voice speaks ONLY exact KJV Mark 5:34 after the 2s sacred pause), serif captions, soft music bed faded to full silence BEFORE the KJV line, cream #F7F2E9 verse card (Mark 5:34, text from the pack/PAIRING-LIST — not hand-typed) and 6s closing question card. Output: media-production/build-01-cloak/cloak-01-prototype.mp4 — 1080×1920 H.264, 98.5s, 18.6MB (<25MB spec). Full §5 QC pass done: montage + full-frame checks (no face/hands of Jesus anywhere, painted style consistent, no AI gibberish text) and audio level checks (narration ~-21dB, silence in the sacred gap).
- What changed in the app (files/commits): No app code. NEW: media-production/build-01-cloak/ (build.py assembly script, make_narration.py TTS script, cloak-01-prototype.mp4 — media files kept local via .gitignore, scripts committed so any session can rebuild).
- What is now true that wasn't before: The complete hybrid pipeline is PROVEN end-to-end: stills are free, one video cost ~20 credits total this pass, assembly costs nothing. Credits: ~160 of 1,000 Pro remaining. QC lessons added to practice: (a) style drift fixed by reinforced wording "Flat painted artwork... absolutely not photorealistic, not a 3D render, not a photograph"; (b) never approve motion from a thumbnail — scrub the player/filmstrip; (c) Flow toasts at top-right block card clicks — dismiss first; (d) download stills at 2K (menu under the download icon).
- What's next / handed off: (1) Cameron watches cloak-01-prototype.mp4 and says yes/no; (2) on yes → delivery pipeline (Firebase Hosting /story-videos/cloak.mp4) + start the two locked LOW-ANIMATION validation stories; (3) Cameron's purchase call, his alone: Ultra $100/mo (10,000 credits, covers all 200 lean) vs $200/mo (25,000, >2x margin) — Pro's 1,000/mo is too slow for 200 videos; (4) voice audition: current edge-tts voices (Andrew narrator / Ryan KJV) are placeholders Cameron can veto; (5) still pending from pt.5: Part C BRIDGE verification research; feed engine rework.
- Commit: d833f3d

## 2026-07-07 (pt.6) — Video #1 GENERATED: all 8 shots of "The Woman Who Touched His Cloak" made in Veo 3 (Flow)
- What we did: Cameron signed into Veo 3 (Google Flow, Pro account noremacttevol@gmail.com) and said go. Created Flow project "MBM Story Videos — Wave One" (https://labs.google/fx/tools/flow/project/0e265a0d-b227-40e0-86d0-c8c1f2a182dc). Generated all 8 shots of pack 01 (cloak) in direct text-to-video mode, Veo 3.1 Quality, 9:16 vertical, 8s each, 1x per prompt. Every prompt = pack STYLE BLOCK + shot prompt verbatim + a no-audio line (narration/KJV voice get added in Descript). Reviewed every clip myself against the pack spec — Cameron never had to check anything. Shot 5 (the reach — fingers on the tasseled hem, golden bloom at contact) landed first take. Shot 7 verified frame-by-frame in the player: Jesus's face never visible through the whole turn — only light where his face would be. Face rule holds 8/8. Shot 8 (close-up, fear → weeping relief → fade to white) approved.
- What changed in the app (files/commits): No app code. All 8 clips live in the Flow project (not yet downloaded). SESSION-LOG entry only.
- What is now true that wasn't before: Wave-one production has begun and video #1's raw footage is complete. Learnings: Quality generations fail transiently sometimes ("not charged for failed generations") — the leftmost card button is Retry and re-queues free (Shot 1 needed several retries; shots 2–8 mostly first try). Submit clicks occasionally don't register — click the arrow again. Credits: ~800 of 1,000 monthly Pro credits used (8 × 100/clip Quality); ~200 left = 2 retakes this month. All 200 videos ≈ 1,600 clips, so scaling needs a decision AFTER video #1 is assembled and judged: monthly Pro refresh (slow), Veo Fast at 20 credits/clip (cheaper, lower quality), or Google AI Ultra — Cameron's purchase call.
- What's next / handed off: (1) download the 8 clips from Flow (download icon in each clip's player view); (2) assemble video #1 in Descript per pack 01 — narration voice audition (or Cameron records the 5 lines), KJV Mark 5:34 Jesus voice over shots 7–8 after the 2s pause, music cut to silence on "daughter," serif captions, 6s closing question card on cream, export 1080×1920 H.264 <25MB; (3) Cameron reviews assembled video #1, then the credit-scaling decision; (4) still pending from pt.5: Part C BRIDGE verification research; feed engine rework.
- Commit: 4940ca3

## 2026-07-07 (pt.5) — Master pairing list built: 200 video↔verse pairs, the ~105 verse-only pool, BRIDGE study drafts
- What we did: Executed FEED-2.0-SPEC.md build-order step 1. NEW media-production/PAIRING-LIST.md with three parts. Part A: the exact linked verse for every one of the 200 THE-200 entries (Sections I–VIII KJV; Section IX standard works, BOM-law gated), each chosen to carry that video's Seed, with a one-line why. Part B: the verse-only pool in three gated tiers — Tier 1 MILK (58 universal goodness-of-God verses), Tier 2 BRIDGE (24, questioning-signal gated, incl. Jas 1:5, Amos 3:7, Ezek 37:16–17, Acts 3:21, 1 Pet 3:18–19), Tier 3 member track (25 from all standard works). Part C: scholar-grade research DRAFTS of the three BRIDGE sprinkles Cameron named (1 Cor 15:29, John 10:30 hen/heis + John 17, Gal 1:8 in context — marked study-only) with explicit VERIFY-before-shipping requirements and binding placement rules. Engineering law encoded: verse TEXT is pulled at build time from verified public-domain sources and script-verified — never typed by hand; build fails on unresolvable references; Part C items blocked from the composer until verification passes are logged.
- What changed in the app (files/commits): No app code. NEW: media-production/PAIRING-LIST.md.
- What is now true that wasn't before: build-order step 1 is drafted end-to-end; the feed engine (step 2) has its complete content manifest to compose against.
- What's next / handed off: (1) verification pass on Part C research (web research) before any BRIDGE copy ships; (2) feed engine rework in RN per spec §6.2; (3) Cameron's unchanged blocker: Veo 3 sign-in (~$20) for wave-one clips.
- Commit: 82a2fd8

## 2026-07-07 (pt.4) — FEED 2.0 locked: the prescribed feed, wheel navigation, honoring rules, video playback law
- What we did: Cameron gave the full feed-revamp vision and answered two rounds of precision questions. Everything is captured in the new FEED-2.0-SPEC.md (repo root). Highlights: the 200 videos live in the FEED (two per prescribed page, each paired with its KJV verse beneath — honored separately); the 20-story opening bank stays text-only; page composition = 2 video+verse pairs + 0–1 rare standalone verse + 1 question + 1 invitation; ~100 verse-only pool; style stays cinematic live-action (Cameron confirmed over "cartoonistic"); runtime 90s–3min story-driven; wheel navigation with HOME anchor, instant previous-pages archive, ladder-delayed next pages (5s/15s/30s/60s+60s, resets each session), dots + home icon; honoring/replacement rules (replace on scroll-away after honoring; un-honored stays; auto-refresh only after full-scroll + no engagement + tab-leave); video playback law (no controls, 100% watch required, leave-app rewinds 5s, close-app = no credit) with a flagged App-Store-risk fallback (pause-only, one code flag); verse pools gated by self-proclaimed signals per the BOM law; BRIDGE sprinkles to research carefully (1 Cor 15:29, John 10:30 Greek, Gal 1:8 + LDS scholarship); member track gets more standard-works verse text (public domain — verified). Master plan corrected (placement + runtime).
- What changed in the app (files/commits): No app code yet. NEW: FEED-2.0-SPEC.md. Updated: media-production/00-MASTER-PLAN.md (placement correction, runtime 90s–3min).
- What is now true that wasn't before: the entire feed revamp is specified end-to-end and survives session loss; build order is defined (pairing list → feed engine → video layer → wave-one production).
- What's next / handed off: (1) Cameron signs into a generator (Veo 3, ~$20) — still the only blocker for video production; (2) assistant starts the master pairing list (exact KJV verse per THE-200 entry + the 100-verse pool + BRIDGE research); (3) then the RN feed engine rework per spec section 6.
- Commit: b4a0fad

## 2026-07-07 (pt.3) — The Two-Voice Law: KJV red-letter Jesus voice + modern LDS-lens narrator, wired into all 20 packs
- What we did: Cameron locked the voice design. Every video has exactly two voices, the same two across all 200: (1) a Narrator in modern, plain storytelling language telling the story through a Latter-day Saint lens and gently unpacking Jesus's harder sayings to show he is a kind, loving, merciful God; (2) a distinct Jesus voice that speaks ONLY the words of Jesus, ONLY in exact KJV red-letter text (the Church's approved translation) — never modernized. Since his face is never shown, his voice IS his face: same voice in every video so people learn to recognize him. Parable rule: narrator retells the parable modern; Jesus voice delivers only the KJV heart-lines. Added a "Red-letter lines (KJV)" section to every pack 01-20 with the exact KJV text, where it lands in the shot list, and a modern narrator bridge after each hard phrase ("be whole of thy plague," "careful and troubled," "whether of them twain," etc.). Emmaus note: the stranger's voice is the Jesus voice — recurring viewers recognize him before the disciples do. Also answered Cameron's automation question: everything automatable except his generator sign-in; quality held by hard gates (word-for-word script/KJV verification, spec checks, assistant reviews every clip, Cameron reviews finished videos in batches).
- What changed in the app (files/commits): No app code. media-production/00-MASTER-PLAN.md gained the Two-Voice Law; packs 01-20 each gained "## Red-letter lines (KJV)".
- What is now true that wasn't before: the voice architecture for all 200 videos is decided and encoded per-story; no per-video voice decisions remain except the one-time audition on video #1 (narrator + Jesus voice candidates).
- What's next / handed off: unchanged blocker — Cameron signs into a generator (Veo 3 recommended); then clips for #1 (cloak), Descript assembly with both voice auditions, Cameron picks the two voices, template locks.
- Commit: b6ae69e

## 2026-07-07 (pt.2) — THE 200: full video corpus cataloged; Seed sections added to all 20 packs
- What we did: Cameron confirmed alignment ("you nailed it") and raised the target from 20 to 200 videos, with a locked storytelling law: these are NOT generic Christian videos — every one must show the actual character of the good Godhead (worthy of worship because of how they love us) so a viewer's inherited theology starts to feel too small, without argument and without naming the Church early. Added a "Seed" section to every existing pack (01-20): the quiet restoration-pointing question each video must leave behind, and which shots carry it. Wrote THE-200.md — the complete numbered catalog (verified 1..200, no gaps/dupes) across nine sections: the 20-story bank, 33 parables, 28 miracles, 30 encounters, 8 nativity, 22 passion/resurrection, 20 teachings-as-scenes, 19 Old Testament good-God stories, and 20 post-signal Restoration-track entries (3 Nephi, Ether 3, Moses 1/7, D&C 121, First Vision as #200) — Section IX gated by the BOM law, member-track from day one. Master plan updated to the 200 vision (~1,400 clips, generated in waves).
- What changed in the app (files/commits): No app code. media-production/: THE-200.md new; 00-MASTER-PLAN.md updated; packs 01-20 each gained "## The Seed".
- What is now true that wasn't before: the media effort has a complete target corpus and a theological aim locked into every recipe, not left to generation-time chance.
- What's next / handed off: unchanged — Cameron picks a generator (Veo 3 recommended) and signs in; assistant generates wave one (the 20), assembles in Descript, Cameron reviews #1 (cloak). New in-app stories get written from THE-200 in Jesus-Method format before their videos.
- Commit: cdaf563

## 2026-07-07 — Media production: packs for all 20 story videos written and verified
- What we did: Cameron asked for videos of every Jesus story in the app. Direction chosen: AI-generated cinematic scenes, played in-app, Cameron reviews each video. Created `media-production/` with a master plan (pipeline, style block, tracker, backlog of 16 future gospel stories) and a full production pack for EVERY one of the 20 opening stories: narration script (the app's exact story text, programmatically verified word-for-word), closing question card, and 6-8 paste-ready shot prompts per story. Two locked rules: Jesus's face is never shown (light/silhouette/hands/hem only), and narration is never rewritten. HeyGen/HyperFrames tried for a quick sample — out of free credits (see 07-06 entry: marketing videos consumed them) and wrong style anyway. No AI-video-generation MCP exists in the registry.
- What changed in the app (files/commits): No app code. New folder `media-production/` — 00-MASTER-PLAN.md + packs 01-20 (commit 8f99b53).
- What is now true that wasn't before: every story in the bank has a complete, verified video production recipe; clip generation is the only blocked step. NOTE: 3 HeyGen motion-graphics story videos already exist on disk (Marketing-Launch-Kit/videos/, per 07-06 session) — social-marketing style, distinct from this cinematic in-app effort.
- What's next / handed off: Cameron picks a generator (recommended: Google Veo 3 via Google AI Pro ~$20 for one month, covers all ~140 clips) and signs in on his browser; assistant drives generation via Chrome, assembles in Descript, Cameron reviews video #1 (cloak) first. Delivery: Firebase Hosting /story-videos/, streamed via expo-video, text story stays as the offline fallback.
- Commit: 8f99b53

## 2026-07-06 — Marketing kit re-activated: 3 story videos downloaded, bio link updated to live app
- What we did: Re-surfaced the Marketing-Launch-Kit for the social launch. Checked HeyGen: 3 of 4 story videos were rendered COMPLETED but never downloaded. Downloaded all three MP4s (verified frame-by-frame which story is which) into `Marketing-Launch-Kit/videos/`: 01-Woman-at-the-Well.mp4, 02-Prodigal-Son.mp4, 03-Woman-and-the-Cloak.mp4. Fourth (Good Shepherd) still stuck "processing" on HeyGen free tier since 07-01 — script ready, recompose when monthly credits reset or on paid tier.
- What changed in the app (files/commits): No app code. SOCIAL-PAGE-KIT.md "Link in bio" updated — app is live, so bio link = https://milkb4meat.org (+ App Store direct link). Videos added to kit (gitignored or committed per repo policy).
- What is now true that wasn't before: Cameron has the actual posting-ready MP4s on disk; the social kit's bio-link advice matches reality (app live).
- What's next / handed off: Cameron creates the IG/FB/X accounts per SOCIAL-PAGE-KIT.md (2 min each, needs his phone/password), posts Woman at the Well first + pins it, follows CAPTIONS-AND-CALENDAR.md. Good Shepherd video pending HeyGen credits. Spend cap + Android testers still open.
- Commit: fdd181f

## 2026-07-05 (pt.4) — App Store public indexing CONFIRMED; watcher retired
- What we did: Scheduled "check-appstore-live" watcher ran; iTunes lookup API (`https://itunes.apple.com/lookup?id=6783621048`) now returns resultCount 1. The app is fully live and publicly indexed: https://apps.apple.com/us/app/milk-before-meat/id6783621048 (Milk Before Meat, free, 4+, Lifestyle/Books, v1.0, released 2026-07-02).
- What changed in the app (files/commits): No app code. START-HERE.md "Last verified true" block updated to state indexing is confirmed and the watcher is disabled; this SESSION-LOG entry added.
- What is now true that wasn't before: App Store search index has the app — the last outstanding launch dependency on Apple's side is closed. Direct link, QR, and search all work.
- What's next / handed off: Scheduled task "check-appstore-live" disabled (no longer needed). Cameron: spend cap at console.anthropic.com still open; keep gathering Android testers toward the closed test.
- Commit: 49a8d44

## 2026-07-05 (pt.3) — Opening story on EVERY cold open, story bank 9 → 20, feed never repeats the opening story
- What we did: Fixed Cameron's Android report that the opening screen stopped appearing. Root cause: once all 9 stories were seen, cold opens skipped Hook and went straight to Main. Now the sanctuary opening (Hook) shows on EVERY cold open; its "Come and see" button routes to Onboard when an unseen story remains (or first launch), otherwise straight into the app. Wrote 11 new entry stories (well, storm, bartimaeus, roof, ten_lepers, centurion, mary_martha, lazarus, emmaus, shore, samaritan) in the exact Jesus-Method format — 20 total, each with the believer's testimony "E" choice. Added feed dedupe: the story just told on cold open is never re-served as a feed card in the same session (new `openingStoryRefs.ts` maps every story id to its scripture-chapter prefixes; `buildFeed` filters them out, with a fallback so the feed can never go empty).
- What changed in the app: `mobile/src/navigation/AppNavigator.tsx` (initialRouteName always 'Hook'), `mobile/src/screens/HookScreen.tsx` (CTA branches), `mobile/src/screens/OnboardScreen.tsx` (+11 stories), `mobile/src/store/useAppStore.ts` (session story exclusion in markStorySeen + buildFeed), new `mobile/src/data/openingStoryRefs.ts`.
- What is now true that wasn't before: every cold open begins at the opening screen; a fresh, never-repeated story plays on each cold open until all 20 are seen and answered; the feed never shows the passage the opening screen just told. Shipped OTA to production (update group a2a43538-81fc-4c14-bb17-6fe025bb14d6, iOS + Android, runtime 1.0.0) — reaches installed apps after close/reopen ×2.
- What's next / handed off: print the Bishopric-Stack when ink arrives; Cameron: spend cap at console.anthropic.com, keep gathering Android testers toward 15.
- Commit: 76d90de

## 2026-07-05 (pt.2) — Bishopric-Stack refined: white covers on the big three, compliance doc added, ink-heavy fully separated
- Built on the parallel session's stack (2d24a76). Docs 14 (Overview & Launch Plan) and
  15 (Cameron's Field Guide) replaced with NEW white-cover printable versions (sources:
  pitch-book/book-printable.html, cameron-guide-printable.html — CSS overrides kill the
  solid-navy cover page and dark quote/table blocks that drain cartridges).
- Added doc 16: "Within the Lord's Boundaries" compliance review, white-cover printable
  (compliance-printable.html). Verified current (0 stale terms).
- Moved "Walkthrough for Testers" (4.6MB of screenshots) out of the stack into
  TO-PRINT/"Ink-Heavy (screen or print shop)/", alongside the dark-cover Come-and-See and
  The Complete Book (screen-read, slightly dated — no rebuildable source; do not print).
- READ-ME — Print Kit.md updated to explain the two folders.
- Context: Cameron's printer ran out of ink mid-proof-set; all queues canceled. The full
  16-doc Bishopric-Stack (~62 pages, all ink-light) is ready to print when ink arrives.
- Commit: (this chain-link, on top of 2d24a76)

---

## 2026-07-05 (pt.2) — Bishopric-Stack built & printed; every doc de-staled; ink-heavy separated from printable
- Cameron asked for a complete printable stack for presenting to the bishopric, with
  ink-heavy (dark-page) pieces separated out, after verifying EVERY file is accurate.
- **Full staleness audit + fixes (all TestFlight/"waiting on Apple" wording removed):**
  pitch-book/book.html (status table → "Live", links + Ch.10 iPhone steps → public App
  Store), church-launch-kit 00/02/03/07 md files. 04_Install-Guide, sheets 2–4, Field
  Guide, Walkthrough already clean. Overview & Launch Plan PDF regenerated from the fixed
  book.html (22 pp, 0 stale) and synced to FOR-CAMERON + pitch-book.
- **NEW ink-light Come-and-See brochure** (pitch-book/brochure-printable.html → 4 white
  pages, same words, cross mark instead of dark cover/screenshots). Dark original moved
  to TO-PRINT/"Ink-Heavy (screen or print shop)/". Ink-light copy is the new TO-PRINT #1.
- **NEW TO-PRINT/Bishopric-Stack/** — 16 numbered PDFs in presentation order (90 pp):
  01 Church-Day Sheet · 02 Bishop Brochure · 03 Honest Review (kit 01) · 04 Privacy
  One-Pager · 05 FAQ & Objections · 06 Staged Approach · 07 Plain-English Map ·
  08 Priesthood Email · 09 Come-and-See ink-light · 10 For-Members · 11 How-to-Get ·
  12 Install Guide · 13 Roadmap · 14 Overview & Launch Plan · 15 Field Guide ·
  16 Walkthrough. Docs 03–08 + 12 newly rendered from the kit .md files (pandoc + Chrome,
  house style). Kit READ-ME updated to explain the new layout.
- **Excluded from print: FOR-CAMERON/The Complete Book.pdf** — 20 pp, still has 3 stale
  TestFlight mentions and NO rebuildable source found; screen-read only until rebuilt.
- **Printed on the HP DeskJet 4300:** earlier a 6-piece proof set (jobs 11–16), then per
  Cameron's explicit choice the FULL 90-page stack (jobs 17–32).
- Commit: (this chain-link, on top of 4769b29)

---

## 2026-07-05 — 🎉 STORE PAGE VERIFIED LIVE; church-day prep: roadmap refreshed everywhere, Cameron sheet made
- **The App Store page is publicly LIVE.** Direct URL https://apps.apple.com/app/id6783621048
  returns 200 and renders "Milk Before Meat" (verified by curl + content grep). The iTunes
  lookup API still returns resultCount 0 — that's just Apple's SEARCH index lagging, which is
  why the "check-appstore-live" watcher hasn't fired. Practical meaning: the QR/direct link
  works NOW; App Store *search* may not find the app for a day or two. Watcher left running
  to confirm when search indexing completes.
- Confirmed for Cameron: the three pt.3 fixes shipped OTA to BOTH platforms (one JS bundle,
  iOS + Android, runtime 1.0.0) — his Android internal-track build gets them after close/open ×2.
- **Roadmap was stale in 3 places, all fixed:** site/roadmap.html still had "Apple's review —
  submitted and waiting" as a NOW item (removed; the "approved and live" done-item already
  existed) and the section header said "invite-only testing phase" (now "iPhone public,
  Android finishing its test"). Regenerated the print PDF from the fixed page and synced all
  three copies: TO-PRINT/"5 - Roadmap (where it's going).pdf", site/Milk-Before-Meat-Roadmap.pdf,
  FOR-CAMERON/Roadmap.pdf. Site redeployed to Firebase hosting (verified serving).
  Old printed #5 copies are obsolete — reprint.
- Text-verified sheets 1–4: no stale TestFlight/waiting wording (sheet #4's "invite-only"
  line is about Android, which is true). #4 from July 4 is current.
- **NEW: FOR-CAMERON/Church-Day-Sheet.pdf (+.html)** — one-page printable, Cameron-only:
  60-second pre-church verification of the 3 fixes, what's true now (iPhone live but tell
  people to use the QR not search; Android invite flow), print quantities, one-breath script +
  ask-for-counsel framing, in-the-moment fallbacks, open Cameron tasks. Visually verified 1 page.
- Advice given: green light to show/share at church and seek counsel — iPhone installs work
  via QR/link today.
- Commit: (this chain-link, on top of d17db46)

---

## 2026-07-04 (pt.3) — Cameron's 3 fixes: cold-open flash, clipped clock icon, consent reworked his way — SHIPPED OTA
- Cameron's feedback (voice): (1) bottom "not God / not affiliated" disclaimer still flashes
  for a split second BEFORE the cold-open animation on the App Store build — the old fix
  didn't cover it; (2) the clock/history icon on Talk About It is clipped at the top ~10%
  on iPhone; (3) the AI-consent gate felt like it broadcast AI as the app's main purpose —
  he ruled: REMOVE it from onboarding ASAP, default OFF, keep the Profile toggle, disclose
  just-in-time at first chat use, say "AI" not "Anthropic" in-app (privacy policy still
  names Anthropic in full — Apple requires that and it stays), and when a "Talk about it"
  link arrives with AI off, offer BOTH turning AI on AND taking the sourced question to a
  real person.
- Fixes (commit 841af0e, all JS-only):
  1. HookScreen: root cause was the footer's static-0 → native-animated opacity handoff
     painting one full-opacity frame on iOS. Footer fade now uses the JS driver (opacity is
     a plain prop, 0 from frame one) — flash is structurally impossible; layout unchanged.
  2. ChatScreen header: 🕐 emoji (clipped by Jost lineHeight) replaced with Ionicons
     "time-outline" vector icons on both history buttons.
  3. OnboardScreen aiConsent page DELETED (faith page enters app directly; aiConsent stays
     'unknown' = off by default, nothing leaves device). ChatScreen consent card reworked:
     one short card for unknown+declined, no vendor name, honest "not tied to your name"
     wording, shows the sourced draft it arrived with, two equal buttons — "Turn on the AI
     conversation" / "Talk to a real person instead" (blue, sends the carried draft into a
     fresh real-person thread via sendConnectMessage + copied banner). ProfileScreen toggle
     reworded the same way. Apple 5.1.1(i)/5.1.2(i) still satisfied: disclosure + explicit
     yes still precede ANY send — just at point of use instead of onboarding.
- Verified: tsc --noEmit clean; no user-facing "Anthropic"/"Claude" strings remain (only
  code comments); consent gating in store untouched (aiConsentGranted still guards every
  network call).
- SHIPPED: eas update → production branch, runtime 1.0.0, iOS + Android (update group
  4093b44f-7fe2-445d-b294-08fe7a7f5e6d). Reaches App Store build 8 and Play vc7 on next
  app relaunch ×2 (first launch downloads, second applies).
- Commit: (chain-link on top of 841af0e)

## 2026-07-04 (pt.2) — "Fix it all": site flipped to App Store + deployed, print kit refreshed, domain warning stale
- What we did (Cameron said "fix it all, you're my project manager"):
  1. WEBSITE: site/index.html iPhone card flipped from TestFlight to the public App Store
     (https://apps.apple.com/app/id6783621048); section header updated ("It's here / Get it
     on your phone"). roadmap.html updated: iPhone = public/approved, Android = still testing.
     Deployed to Firebase hosting via the service-account method; VERIFIED the new card and
     roadmap text serving on milk-b4-meat.web.app. (The previously-uncommitted index.html
     TestFlight edits were superseded by this, as intended.)
  2. PRINT KIT: generated church-launch-kit/qr-appstore.png (QR → App Store URL). Rewrote the
     iPhone section of How-to-Get-the-App.html (App Store steps, no TestFlight), regenerated
     the PDF via headless Chrome, copied over TO-PRINT sheet #4, and visually verified the
     PDF (one page, clean, both QRs render). Rewrote 04_Install-Guide.md iPhone path for the
     App Store. Old printed copies of sheet #4 are obsolete — reprint. Other brochures fine.
  3. DOMAIN: verified milkb4meat.org is ALREADY on Firebase (apex 199.36.158.100, www CNAME
     milk-b4-meat.web.app, HTTP 200, real site content). START-HERE's June-30 Squarespace
     placeholder warning was STALE — corrected in START-HERE.md.
  4. STORE PAGE: still not indexed at time of writing (availability fix was earlier today;
     up to ~24h is normal). Created scheduled task "check-appstore-live" (3x daily) that
     notifies Cameron when live, updates START-HERE, commits, and disables itself.
- What changed: site/index.html, site/roadmap.html (deployed), church-launch-kit
  How-to-Get-the-App.html/pdf + qr-appstore.png (+ committed the existing qr pngs),
  TO-PRINT sheet #4, 04_Install-Guide.md, START-HERE.md, this entry.
- Commit: (chain-link on top of c3fcf5b)

## 2026-07-04 — Store-page 404 root-caused: ZERO territories set — FIXED via ASC API
- What we did: Cameron asked if Apple approved and whether the website/printed material
  need changing. Verified the chain (193cba4 ✓). Re-checked: 1.0 still READY_FOR_SALE,
  releaseType AFTER_APPROVAL (no release tap pending) — but iTunes lookup STILL returned
  0 results 2 days after approval. Dug in: GET appAvailabilityV2 returned NOT_FOUND —
  the app had NO territory availability record, i.e. available in ZERO countries. That,
  not propagation, was the 404.
- The fix: POST /v2/appAvailabilities with all 175 territories, availableInNewTerritories
  =true. Verified: 175 territories available, releaseDate 2026-07-04. Lookup not yet
  indexed at time of writing (expected lag after the change).
- Printed-material audit (for when the page goes live): TO-PRINT #4 hand-out,
  church-launch-kit How-to-Get-the-App (html+pdf), 04_Install-Guide.md, and
  qr-testflight.png all point at TestFlight → refresh with the App Store link.
  Come-and-See brochure only shows milkb4meat.org — fine as is. Website: site/index.html
  iPhone card still TestFlight (has UNCOMMITTED local edits — preserve them when flipping).
- What's next: re-check the store URL; when live, flip the site card + deploy hosting,
  refresh the print pieces above, update START-HERE.md.
- What changed: START-HERE.md truth block; this entry. No code. (Local uncommitted edits
  to site/index.html and print files were left untouched, as found.)
- Commit: (chain-link on top of 193cba4)

## 2026-07-02 (pt.5) — 🎉 APPLE APPROVED — 1.0 is READY_FOR_SALE (store page still propagating)
- What we did: Cameron asked if Apple accepted. Confirmed via the ASC API (signed JWT with
  the .p8 key): version 1.0 = READY_FOR_SALE / READY_FOR_DISTRIBUTION. Build 8 passed.
- BUT: the public listing https://apps.apple.com/us/app/id6783621048 was still 404 and the
  iTunes lookup API returned 0 results (checked ~19:55Z) — normal propagation lag after
  approval. So the website iPhone card was deliberately NOT flipped yet (no 404 buttons).
- What's next (one clean step for any session): re-check the store URL; when it loads,
  swap the site/index.html iPhone card from TestFlight to the App Store link, deploy
  Firebase hosting, verify, update START-HERE.md. Note site/index.html has uncommitted
  local edits — preserve them when editing.
- What changed: START-HERE.md truth block; this entry. No code.
- Commit: (chain-link on top of 87f9986)

## 2026-07-02 (pt.4) — Roadmap: prompt-caching restructure added (Cameron's call)
- What we did: after an honest cost comparison of AI providers (switching is a ~20-line
  proxy change, cheap models are 5-10x less, but tone risk + near-zero current bill =
  stay on Haiku for now), Cameron locked the cost lever into the roadmap instead:
  restructure the system prompt into a fixed shared prefix + small per-person tail so
  Anthropic prompt caching cuts input costs up to ~90% with zero quality change.
- Framing (Cameron's words, now a rule): the CURRENT TESTER PHASE is purposefully the
  research phase for this — we're using testers to learn which prompt parts stay fixed
  for everyone vs. truly vary per person, so the restructure is designed from real usage.
- What changed: docs/roadmap/FORWARD-WORK-PLAN.md — new APP IMPROVEMENTS item 2
  (others renumbered).
- What's next: keep collecting tester transcripts with that question in mind; build the
  split (pairs with tiered model routing); revisit provider choice only if the monthly
  bill nears $100.
- Commit: (chain-link commit on top of d4bd068)

## 2026-07-02 (pt.3) — SECURITY AUDIT + LIVE HARDENING of proxy and Firestore
- What we did (Cameron asked for a full security check of the app):
  - Audited everything: no secret keys in the repo or in ANY git commit ever; Firestore
    rules solid; server deps clean; mobile npm "vulns" are Expo build-tooling only.
  - THE real hole: the Railway key proxy (/api/chat) answered ANYONE on the internet —
    a stranger could extract the URL from the app bundle and burn Cameron's Anthropic
    money at unlimited volume. Fixed and DEPLOYED the same day.
- What changed (code commit f4a6cc2, deployed live to Railway + Firebase):
  - server/index.js: per-IP rate limits (chat 10/min + 300/day; connect/factcheck
    5/min + 30/day), global 5000/day chat fuse (env-tunable), message/system size caps,
    model locked server-side, queue caps (500) so disk can't fill, client IP taken from
    x-forwarded-for (req.ip was unreliable behind Railway — first deploy proved it).
  - App token groundwork: mobile sends x-mbm-app (EXPO_PUBLIC_MBM_APP_TOKEN in
    eas.json); Railway has MBM_APP_TOKEN set. NOT enforced yet — flip
    REQUIRE_APP_TOKEN=1 on Railway ONLY after builds carrying the token are what
    people have installed (the build in Apple review does NOT send it).
  - firebase/firestore.rules: size caps on message create (body/excerpt ≤4000 etc.) —
    PUBLISHED LIVE via new admin/deploy-rules.mjs (service-account path; the firebase
    CLI lacked a permission, the Rules API works).
  - FOR-CAMERON/SECURITY-REPORT-2026-07-02.md — plain-language report.
- Verified live: 11th rapid chat request → 429; oversize message → 400 message_too_long;
  a normal chat still answers (build 8 in Apple review is unaffected); connect throttles.
  (4 test notes labeled "security-test — safe to ignore/delete" are in the connect queue.)
- Cameron-only action: set a monthly spend cap at console.anthropic.com (Billing).
- What's next: after the next builds ship + old builds age out, set REQUIRE_APP_TOKEN=1
  on Railway (railway variables --service mbm-proxy --set REQUIRE_APP_TOKEN=1).
- Commit: f4a6cc2 (code) + chain-link on top.

## 2026-07-02 (pt.2) — REBUILT + RESUBMITTED TO APPLE (Waiting for Review) + Android vc7 live
- What we did (all automated, nothing left for Cameron):
  - Verified the updated privacy policy (naming Anthropic + consent) is LIVE at
    milk-b4-meat.web.app/privacy.html.
  - Built BOTH platforms from commit 9438d84 (`eas build --platform all --profile
    production --auto-submit`): iOS build 8, Android version code 7.
  - iOS: build 8 uploaded + processed (VALID, export compliance clean). Via the ASC API:
    attached build 8 to version 1.0, CANCELED the dead rejected review submission
    (99f5b00a…), created a NEW review submission 3888660e-454c-4d81-bd4a-67dc30b6463c,
    added the version, and SUBMITTED. Confirmed state: **WAITING_FOR_REVIEW**,
    submittedDate 2026-07-02T10:55Z. No Resolution Center reply was needed — the file
    "FOR-CAMERON/APPLE-RESUBMIT — copy-paste reply.md" is marked no-longer-needed (kept in
    case Apple writes back).
  - Android: auto-submit completed; Play **internal track now serves vc 7 (status
    completed)** — Cameron's phone gets the consent gate, small-screen fix, and
    Discipleship warm-up via Play internal testing.
- What is now true: iOS 1.0 (build 8) is in Apple's review queue; Android internal has vc7.
- What's next: wait for Apple (~24h typical). If approved, the public-release tap is
  Cameron's. If rejected again, read the new message and iterate.
- Commit: (chain-link commit on top of b668015)

---

## 2026-07-02 — Apple-rejection audit + small-Android fix + Discipleship warm-up
- NOTE ON THE CHAIN: the July 1 session (commit 41ecf03, the Apple 5.1.1(i)/5.1.2(i)
  consent fix) never wrote a session-log entry. This entry records it retroactively so
  the chain is whole again.
- What we did:
  - AUDITED the July 1 consent fix end to end. Verified all four AI call sites in
    useAppStore.ts (chat send, blessings, note summaries, discipleship summary) hard-block
    until aiConsent === 'granted'; onboarding consent page, chat consent card, and Profile
    on/off control all present; no other network path sends user words to the AI. The
    human-inbox Firestore path is user-initiated and covered by the published privacy label.
    eas.json production has autoIncrement (new build number automatic) and ships no
    Anthropic key — only the proxy URL.
  - FIXED the small-Android opening screen (HookScreen): the non-affiliation/"not God"
    disclaimer was position-absolute and overlapped the "Come and see" button on short or
    oddly-shaped phones. It now lives in normal layout flow below a flex centered zone, so
    overlap is impossible on any screen shape; a COMPACT mode (height < 700) also scales
    type/margins down. Footer now reserves its space from frame one (no flash, no jump).
  - WARMED UP My Discipleship (members-only): added "today's word" — a daily-rotating
    scripture verse per Christlike quality (all four standard works; member track only,
    never visible to seekers) opening the examen card; a "kept" confirmation moment after
    saving a reflection; and a "N reflections kept · walking here since <date>" gathering
    line on My Walk with Christ. No new AI calls, no scores, no streaks.
- What changed in the app: mobile/src/screens/HookScreen.tsx,
  mobile/src/screens/DiscipleshipScreen.tsx, mobile/src/data/examenPrompts.ts.
- Verified: tsc --noEmit clean, tools/feed_test.js ALL PASS, tools/kjv_test.js ALL PASS,
  scripts/preflight.sh ALL CHECKS PASSED (no secrets tracked).
- What is now true: the code is ready for the Apple resubmission build. NOT YET DONE:
  a new iOS production build + eas submit + reply in the ASC Resolution Center, and the
  updated site/privacy.html must be verified deployed on Firebase hosting.
- What's next / handed off: build + resubmit iOS (build number auto-increments); confirm
  privacy.html is live; Cameron confirms the rejection message in the Resolution Center
  matches 5.1.1(i)/5.1.2(i) only (the API cannot read it, so if Apple listed anything
  more, it needs to be pasted in).
- Commit: 9438d84 (work) + the chain-link commit on top; retroactively also records 41ecf03.

---

## 2026-06-30 (pt.7) — deletion cleanup: cut the project from 1.9 GB to ~994 MB
- What we did: Cameron asked what could be DELETED (not just added) to improve organization.
  Surveyed the whole folder; deleted the dead weight after his go-ahead.
- What changed:
  - DELETED ~920 MB of old builds & old app copies: `archive/_old-folders/builds-archive/`
    (old .apk/.aab installers + old DB backup), `archive/legacy/MBM-mobile/` (full
    superseded app copy), `archive/legacy/mobile-expo/` (old Expo copy). The big binaries
    were gitignored (never on GitHub); all regenerable from EAS or git history.
  - DELETED 4 duplicate book formats in `pitch-book/` (book-drive.html, book-upload.html,
    book-text.txt, book-doc.txt) — kept the real PDF book + book.html source.
  - DELETED stale top-level chat-openers NEXT-CHAT-PROMPT.md and SESSION-OPENER.txt
    (fully covered by CLAUDE.md's session-chain steps).
  - Updated the map/index files so none point at deleted things: CAMERON — START HERE.md,
    START-HERE.md, README.md, OPEN-ME-FIRST.txt, docs/00-PROJECT-MAP.md.
- What is now true: the project is ~half its former size and the top level is cleaner.
  No live app, website, or source code touched — only old copies/outputs and duplicates.
- What's next / handed off: nothing required of Cameron.
- Commit: feb5a14 (cleanup) + this chain-link commit on top.

---

## 2026-06-30 (pt.6) — organized the folder for release + polish/print kit (NOT yet committed)
- What we did: gave MBM a human-friendly layer for Cameron (non-technical owner) WITHOUT moving any
  code/build paths. Added top-level master index `CAMERON — START HERE.md`; a `FOR-CAMERON/` folder
  (roadmap, launch plan, field guide, tester walkthrough, full book + "READ-ME — For You.md"); and a
  `TO-PRINT/` print kit (5 numbered ready-to-print finals + "READ-ME — Print Kit.md"). Updated
  `OPEN-ME-FIRST.txt` and `docs/00-PROJECT-MAP.md` to point at the new buckets.
- Polish pass: the Bishop brochure still had `[your phone]`/`[your email]` placeholders — filled in
  (843) 582-7278 · admin@milkb4meat.org · milkb4meat.org and regenerated
  `church-launch-kit/Bishop-Brochure.pdf` (weasyprint). Created two NEW pieces:
  `Members-Outreach-Brochure.pdf` (members: feed faith + share it) and `How-to-Get-the-App.pdf`
  (iPhone/Android sign-up sheet). Corrected `church-launch-kit/00_README-Start-Here.md` (its old
  "replace the placeholders by hand" note was now stale). Website: copied the Come-and-See brochure
  into `site/` and added footer download links (Roadmap PDF + Brochure PDF) on `site/index.html` and
  `site/roadmap.html`. Verified milkb4meat.org references are consistent everywhere — no wrong
  spellings, no remaining placeholders.
- What changed in the app (files): none in `mobile/`. Marketing/site/docs only.
- What is now true that wasn't before: clear FOR-CAMERON / TO-PRINT buckets + one master index; the
  Bishop brochure is contact-complete; a members brochure and a get-the-app sheet now exist; the site
  links to the public PDFs. Verified the live site serves fully at milk-b4-meat.web.app (Roadmap link
  present). milkb4meat.org STILL returns an SSL cert altname mismatch — Firebase hasn't finished
  issuing the custom-domain certificate (same as pt.3/4/5); resolves automatically, no redeploy needed.
- DONE (Cameron approved "commit + push + deploy live"): committed e649300, recorded it in chain
  commit ba6d48c, pushed to origin/main. Deployed Firebase hosting via the service-account method
  (45 files) — verified LIVE on milk-b4-meat.web.app: home 200, the new footer links "Roadmap (PDF)"
  + "Brochure (PDF)" present, and both PDFs serve as application/pdf (200).
- What's next / handed off: Cameron-only — confirm milkb4meat.org SSL once Firebase finishes issuing
  the cert (still an altname mismatch as of now; auto-resolves, no redeploy needed); the physical
  print run; optionally swap the Bishop-brochure phone for a personal one.
- Commit: e649300 (work) + ba6d48c (chain link); deploy verified live after.

---

## 2026-06-30 (pt.5) — built the public Roadmap (page + printable PDF) and deployed it live
- What we did: built a professional, forward-looking roadmap in the site's navy/gold serif style.
  Created site/roadmap.html (Foundation = done checks; Phase 1 incl. a "where it is right now —
  invite-only testing phase" block + tester-critique/test-as-non-member invites; Phase 2; Phase 3
  framed as a possibility for the Church to decide; a Vision section incl. a "real social presence"
  card). Added a "Roadmap" link to the top nav in site/index.html. Generated a print-friendly
  (light-paper) PDF with WeasyPrint -> site/Milk-Before-Meat-Roadmap.pdf, linked from the page.
  Wrote NEXT-CHAT-PROMPT.md (a copy-paste prompt for a fresh chat whose job is folder organization
  + a print kit + a release-readiness consistency pass). Deployed hosting via the service-account
  method (44 files).
- What changed: site/roadmap.html (new), site/index.html (nav link), site/Milk-Before-Meat-Roadmap.pdf
  (new), NEXT-CHAT-PROMPT.md (new).
- What is now true that wasn't before: the Roadmap page + PDF are LIVE and confirmed serving 200 on
  milk-b4-meat.web.app (roadmap.html, the PDF as application/pdf, the nav link, and the new content
  all verified). NOTE: the custom domain milkb4meat.org resolves to Firebase (199.36.158.100) and
  301-redirects to https, but as of this deploy Firebase has NOT yet issued the SSL cert for the
  custom domain ("no alternative certificate subject name matches milkb4meat.org") — so
  https://milkb4meat.org still throws a cert error. This completes automatically; no redeploy needed
  once the cert lands, and the new content will be there.
- What's next / handed off: next chat = organize the cluttered MBM folder (see NEXT-CHAT-PROMPT.md):
  sort into for-Cameron / to-print / computer-only, build an index + print kit, and run a
  consistency pass (website URL on brochures, members-only outreach brochure, ensure the site links
  to the public PDFs). Also keep watching Firebase Console > Hosting > Domains until milkb4meat.org
  flips to "Connected" (SSL issued).
- Commit: 5fe8f58

## 2026-06-30 (pt.4) — set up www.milkb4meat.org as well
- What we did: added www.milkb4meat.org as a second Firebase custom domain (under the OWNER
  account admin@milkb4meat.org) and saved the CNAME it asked for in Squarespace:
  CNAME www -> milk-b4-meat.web.app. Hit the Squarespace "Verify to continue as
  admin@milkb4meat.org" Google gate again; Cameron cleared it ("i think its good") and the record
  saved. Confirmed in the Squarespace records list (www CNAME present; admin->Railway CNAME and all
  email records still intact). Clicked Verify in Firebase — still "Records not yet detected" because
  the CNAME had just been added (propagation lag, same as the apex).
- What is now true that wasn't before: both milkb4meat.org (apex, A + TXT) and www.milkb4meat.org
  (CNAME) are fully configured in DNS and added in Firebase. Nothing left to configure on either.
- What's next / handed off: just propagation + Firebase's automatic recheck. Re-open Firebase
  Hosting > Domains later and both should read "Connected" with SSL issued. milk-b4-meat.web.app is
  live now in the meantime. Rule reaffirmed: do all MBM work under admin@milkb4meat.org.
- Commit: d588162

---

## 2026-06-30 (pt.3) — connected the custom domain milkb4meat.org to the live Firebase site
- What we did: pointed milkb4meat.org at the live Firebase Hosting site. In Firebase Console
  (signed in as the project OWNER, admin@milkb4meat.org — NOT Cameron's personal
  noremacttevol@gmail.com) added milkb4meat.org as a custom domain. In Squarespace DNS deleted the
  "Squarespace Defaults" group (4 parking A records 198.185.159.144/145 + 198.49.23.144/145, the
  www CNAME to ext-sq.squarespace.com, and the HTTPS @ record) and added the two Firebase records:
  A @ -> 199.36.158.100 and TXT @ -> hosting-site=milk-b4-meat. Left ALL email/admin records
  untouched (Google Workspace MX, Amazon SES, DKIM/SPF/DMARC, and the admin -> Railway CNAME).
- Account correction (important, now a rule): Cameron does NOT want MBM under his personal
  noremacttevol@gmail.com. Verified via Firebase IAM that admin@milkb4meat.org is the project
  OWNER and switched to it for all MBM work. Always use admin@milkb4meat.org for MBM going forward.
- What is now true that wasn't before: DNS has fully propagated — milkb4meat.org now resolves to
  199.36.158.100 (the Firebase IP) on Google (8.8.8.8), Cloudflare (1.1.1.1), and the authoritative
  Squarespace nameserver; the hosting-site=milk-b4-meat TXT record is live. curl confirms the
  domain connects to the Firebase IP. The old Squarespace parking IPs are gone.
- What's next / handed off: Firebase still showed "Needs setup" at the moment we finished, because
  its earlier ACME check hit the OLD (cached) Squarespace IPs and 403'd. That check runs again
  automatically and will succeed now that DNS is correct, then it issues the SSL cert. This is
  just propagation/recheck time (minutes to a couple hours) — nothing left to configure. Re-open
  the Firebase Hosting > Domains page later to confirm it flipped to "Connected." In the meantime
  the site is fully live at https://milk-b4-meat.web.app. Follow-up: www.milkb4meat.org currently
  has no record (its old CNAME was removed) — add www as a second custom domain or a redirect.
- Commit: af8287a (chain link: this entry recorded in 7d936d4)

---

## 2026-06-30 (pt.2) — rebuilt the public website into a real promotional landing page
- What we did: Cameron asked me to "do it all like always" and build the website first so it
  promotes the app to everyone — church members and non-members alike — with a gentle note that
  members of The Church of Jesus Christ of Latter-day Saints get "the extra stuff" when they
  declare it, but not heavy-handed. Rebuilt site/index.html from a single hero into a full
  landing page: navy/gold palette, sticky nav, hero, a 6-pillar "Why this is good for the world"
  section (Met where you are / Never pushed / Always honest / A real human always / Yours to
  keep / For everyone), an embedded explainer video, a "what it really is" section, a 4-shot
  glimpse strip of real app screenshots, the gentle "For everyone — and a little more for some /
  Milk first. Meat when you're ready." member section, get-it cards (TestFlight + Play), and a
  footer with the not-officially-affiliated disclaimer. Matched privacy.html and support.html to
  the navy palette and switched all contact emails to admin@milkb4meat.org.
- What changed (files): site/index.html (major rewrite), site/privacy.html, site/support.html,
  + copied site/img/walk/*.png (37) and site/Milk-Before-Meat-Explainer.mp4 into site/.
- What is now true that wasn't before: the site source is a genuine promotional page, verified
  via Playwright on desktop and mobile.
- DEPLOYED LIVE at https://milk-b4-meat.web.app (HTTP 200, new promo content confirmed serving).
  The stored Firebase user token was expired, so I deployed using the service account at
  admin/serviceAccount.json via GOOGLE_APPLICATION_CREDENTIALS (temporarily stripped the expired
  tokens/user from ~/.config/configstore/firebase-tools.json so the CLI fell back to ADC; original
  config restored afterward). REUSABLE for future deploys without Cameron's login.
  Domain milkb4meat.org still points at the Squarespace "Coming Soon" placeholder (separate DNS
  fix, see website-status memory).
- What's next / handed off: Connect milkb4meat.org to Firebase (custom domain + Squarespace DNS
  swap) — needs Cameron's logins.
- Commit: 8d40e07 (code) / live deploy done after

## 2026-06-30 — fixed the ministry-console scroll snap-back bug
- What we did: Cameron reported the "mc" (ministry console) website scrolling back down to
  the bottom whenever he scrolled up to read the top of a message thread. Traced it to the
  real console (admin/inbox.mjs — the inline PAGE served on port 4545, NOT the older
  server/public/admin.html, which was a red herring). Root cause: the 15-second auto-refresh
  (`setInterval(() => { loadThreads(); if(current) openThread(current); }, 15000)`) re-called
  openThread on the open thread, and openThread unconditionally ran `conv.scrollTop =
  conv.scrollHeight`, yanking him to the bottom every 15s. Fixed openThread to (a) detect a
  same-thread refresh vs a fresh open, and (b) only jump to the newest message on first open
  or when the reader was already near the bottom (<60px); otherwise it preserves the reader's
  scroll position. Applied the same guard to the older server/public/admin.html review pane.
- What changed in the app (files/commits): admin/inbox.mjs (openThread scroll logic) and
  server/public/admin.html (openConv scroll logic). Commit 8e5d44b.
- What is now true that wasn't before: scrolling up in a thread on the ministry console no
  longer gets dragged back to the bottom by the auto-refresh; live watching at the bottom
  still follows new messages.
- Verification: node --check on inbox.mjs passed; both inline browser <script> blocks parse
  clean (new Function). THEN deployed live and Cameron confirmed it: "yeap its good."
- DEPLOYED LIVE (this was the real hold-up). The code fix alone did nothing for Cameron
  because the live site at admin.milkb4meat.org is a Railway deployment and the new code had
  never been pushed to it — he kept seeing the old snapping behavior. I (the assistant)
  deployed it myself using the Railway CLI already installed + logged in on his machine:
  `export PATH="$HOME/.npm-global/bin:$PATH" && cd ~/Desktop/Brain/MBM/admin && railway up --ci`.
  The admin/ folder is linked to project `mbm-proxy`, service `MBM Ministry Console`
  (URL https://admin.milkb4meat.org). Build finished "Deploy complete", new deployment ID,
  service Online, site HTTP 200. Cameron hard-refreshed and confirmed the scroll holds.
  LESSON (saved to .auto-memory/deploy-ministry-console.md): I can redeploy this console
  myself — do NOT hand Cameron terminal commands or "log into Railway" steps. Just deploy.
- Commit: 8e5d44b (code); live deployment done via railway up on 2026-06-30.

## 2026-06-29 (pt.2) — made the folder actually SIMPLE for Cameron + put contact info on the brochure
- What we did: Cameron opened the folder and was still overwhelmed — last cleanup added a `docs/`
  tree but did NOT reduce the 22 top-level folders he sees, so it didn't feel organized. Fixed that:
  (1) Added his phone (843) 582-7278 + email admin@milkb4meat.org + milkb4meat.org to the BACK PAGE
  of the Come-and-See brochure and regenerated the PDF (verified on the rendered page). (2) Archived
  the 5 junk book drafts (book-drive/drive2/upload/upload2/noimg) into docs/archive/book-drafts/.
  (3) Deleted __pycache__ (auto-junk) and swept all dead leftover folders (app-screens,
  finish-the-screens, port-back, web-preview, work-logs, outputs, builds-archive) + 2 junk loose
  files into archive/_old-folders/. Top level went from 22 folders -> 14. (4) Wrote OPEN-ME-FIRST.txt
  at the root: a plain-English map grouping everything into "things you print," "the app + website,"
  "your notes," and "machinery — ignore." Verified all 11 live folders intact, site/ files present,
  mobile/package.json readable, connect.py/knowing_engine.py still at root, git moves = clean renames.
- What changed in the app (files/commits): NO app source changed. New: OPEN-ME-FIRST.txt. Edited:
  pitch-book/brochure.html (contact block) + regenerated Milk-Before-Meat-Come-and-See.pdf. Moves only.
- What is now true that wasn't before: the brochure is print-ready WITH Cameron's contact info, and
  opening the MBM folder shows 14 clearly-grouped folders instead of 22 with junk mixed in.
- What's next / handed off: optional — could further reduce by tucking machinery folders into one
  "behind-the-scenes" folder, but that needs renaming load-bearing paths (mobile/site/server/admin
  are referenced in the rule files), so left alone to avoid breaking the app/website. Big PDFs
  (Complete-Book, Overview-and-Launch-Plan) still in pitch-book — asked Cameron if he wants those too.
- Commit: 10dc408

---

## 2026-06-29 — v1 rough-draft cleanup: organized the whole repo + wrote the handoff docs
- What we did: Did a full "professional handoff" cleanup of the project. Verified the chain
  (top entry 51e2cbc present in git log). Archived all 7 superseded .apk/.aab builds (~460MB)
  and the old DB backup into a new `builds-archive/` (nothing deleted). Moved ~28 loose root
  markdown docs into an organized `docs/` tree (publishing / roadmap / vision / reviews /
  claude-setup / archive{handoffs,superseded,old-screenshots}). Left the authority files at the
  root (START-HERE, AGENT-RULES, SESSION-LOG, CLAUDE, .claudecode, AGENTS) so the chain still
  works, plus config/brand assets and the prototype engine files (connect.py/knowing_engine.py
  are still imported by ministry-sim, so they stay).
- What changed in the app (files/commits): docs/structure only — NO app source changed. New:
  `README.md` (front door), `docs/00-PROJECT-MAP.md` (full table of contents), `docs/archive/README.md`,
  `docs/publishing/PUBLISHING-VIABILITY-REVIEW.md` (fresh go/no-go review),
  `docs/roadmap/FORWARD-WORK-PLAN.md` (one prioritized to-do list),
  `docs/claude-setup/CLAUDE-RECOMMENDATIONS.md`. Updated PUBLISHING-ROADMAP (June 29 snapshot +
  fixed stale iOS/Android checkboxes) and START-HERE's file-hierarchy section to the new paths.
- What is now true that wasn't before: the repo looks like a clean v1 dev handoff — a small root,
  a single index (PROJECT-MAP), current vs historical docs clearly separated, and the publishing
  plan has an honest viability review + a forward work plan.
- What's next / handed off: app state is UNCHANGED (still waiting on Apple; Android 12-tester gate
  still the last Android gate — see WAITING-ON-APPLE.md / FORWARD-WORK-PLAN.md). Optional follow-ups
  I recommended but did NOT auto-apply: update CLAUDE.md's internal doc paths to the new docs/ locations,
  and set up the two scheduled checks (Apple-approval + 14-day clock) — see CLAUDE-RECOMMENDATIONS.md.
- Commit: d4ae3ef

---

## 2026-06-27 — milkb4meat.org landing page built; iPhone card parked in a "coming soon" state while we wait on Apple
- What we did: Built the public website for `milkb4meat.org` (Squarespace) as a self-contained
  responsive landing page — hero, embedded explainer video, the "not the Church / not God / just a
  helper" framing, four screenshots, and two install cards (iPhone + Android) plus the disclaimer.
  Cameron pastes the content into Squarespace himself (assistant can't log into Squarespace).
  Cameron then found the public TestFlight link shows "this beta isn't accepting any new testers
  right now." Diagnosed: that's expected until Apple's Beta App Review passes (the build, 1.0.0 (6),
  is still WAITING_FOR_REVIEW — confirmed via `eas build:list`). To keep the site publishable with no
  dead button, switched the iPhone card to a temporary "Coming any day — email admin@milkb4meat.org"
  state, matching Android, and preserved the LIVE direct-link card as an HTML comment right beside it
  for a one-step revert.
- What changed in the app (files/commits): docs/marketing only. NEW `pitch-book/site-milkb4meat.html`;
  NEW `WAITING-ON-APPLE.md` (single resume checklist for any future session). No app source changed.
- What is now true that wasn't before: there is a publish-ready website, and a clear tracked trail so
  any later chat can finish the iOS hookup the moment Apple approves.
- What's next / handed off: WAIT ON APPLE. When build 1.0.0 (6) shows "Ready to Test" (or the link
  `https://testflight.apple.com/join/cPNpeh3H` starts accepting testers), follow `WAITING-ON-APPLE.md`:
  un-comment the LIVE iPhone card, re-verify, tell Cameron, update START-HERE, commit+push. Optional:
  add Kyle/Rich as internal testers for iPhone now (skips review). Also confirm admin@milkb4meat.org
  is a watched inbox. Still pending separately: printed walkthrough, telling Kyle & Rich.
- Commit: 51e2cbc

---

## 2026-06-26 — Pitch/tester kit finalized (walkthrough, explainer video, gallery) per Cameron's punch list
- What we did: Revised the full tester-facing kit to Cameron's detailed feedback. Fixed the tester
  walkthrough opening to lead with the "not the Church / not God / just a helper" forewarnings
  (captured AFTER the sanctuary animation settles), corrected onboarding steps (answer+reply, then
  faith question+reply with the Enter button), reframed the Feed step to sell the scripture depth
  honestly (100+ for non-members pointing to the Restoration; 100+ meat for members/friends of the
  Church), added the journal kept-notes truth, the "Talk About It" upload links across the app, and
  the real-person toggle/crop/send/cancel detail. Rewrote the feedback question away from the
  machine/AI framing. Rebuilt the explainer video intro (it isn't God / just a helper → story about
  the Lord asking how you feel) and added a journal scene. Rebuilt the gallery with 15 real-
  interaction tiles (common questions + popups).
- What changed in the app (files/commits): docs/marketing only — pitch-book/walkthrough.html +
  book.html, the rendered PDFs (Walkthrough-for-Testers, Overview-and-Launch-Plan, Come-and-See),
  Milk-Before-Meat-Explainer.mp4, and app-screens/ (new g01–g09 interaction shots, 06b-faith-enter,
  settled 01-welcome-sanctuary, rebuilt _GALLERY.png). No app source code changed.
- What is now true that wasn't before: the tester kit is internally consistent with how the app
  actually behaves and frames itself; nothing implies the app plays God or answers for Him.
- What's next / handed off: waiting on Apple TestFlight approval; Cameron to get a printer for the
  printed walkthrough, then tell Kyle and Rich. Open questions raised: TestFlight/Play tester-invite
  mechanics, and turning the domain into a real website for all this.
- Commit: dd68dcf

---

## 2026-06-26 — iOS status documented; Apple side confirmed done + easy for the pitch stage
- What we did: Cameron asked, for his upcoming friends/family/church beta pitch, whether the
  Apple app is done and will be easy, and whether anything on the App Store page should be done
  better. Verified iOS state directly (EAS build:list: v1.0 build 6, commit dda114e, finished
  2026-06-26) and confirmed against START-HERE. Wrote a dedicated tracked record so the separate
  pitch chat can rely on it.
- What changed in the app (files/commits): NEW file IOS-STATUS-AND-APPLE-READINESS.md (honest
  iOS verdict + what's done + optional App Store polish + how iOS fits the testing plan). No app
  code changed — docs only.
- What is now true that wasn't before: there is now a single tracked source of truth for the iOS
  side. Verdict recorded: Apple is effectively FINISHED — submitted, AFTER_APPROVAL auto-release,
  TestFlight public link live NOW (https://testflight.apple.com/join/cPNpeh3H) so beta users can
  install today. Only optional polish: more screenshots (have 2 of Apple's allowed 10; the
  Android shots are the wrong aspect so iOS-sized frames would need generating) — additive, no
  re-review, not a blocker.
- What's next / handed off: nothing required on iOS. The real dependency is Android's 12-tester /
  14-day closed test. Pitch is being handled in a separate chat per Cameron.
- Commit: 1493311

---

## 2026-06-26 — ANDROID AUTO-PUBLISH VERIFIED + latest build live for Cameron's pre-check
- What we did: Stood up and PROVED the automated Google Play publishing pipeline, and got
  the latest fixed build onto internal testing so Cameron can check it before any 14-day
  clock. Ran `eas submit --platform android --profile production` with the new service
  account → pushed production **vc 6** (commit dda114e) to the **internal track**, status
  COMPLETED. Confirmed in Play Console: internal testing latest release is now 1.0.0,
  released Jun 26 ~5:26 AM, "Available to internal testers". Verified Cameron
  (noremacttevol@gmail.com) is in the active "MBM Testers" list; internal opt-in link is
  https://play.google.com/apps/internaltest/4700576250998456373 .
  Also built out the Play **store listing**: app name, short + full description (from
  store-assets/STORE-COPY.md), app icon (512×512) and feature graphic (1024×500) — the two
  graphics were cropped in-console from the existing brand art (icon.png) since the
  in-browser uploader can't drive the OS native file-picker. Saved successfully.
- What changed (files/commits): no app CODE change. Docs/config: START-HERE.md Android
  section rewritten to reflect verified auto-publish + internal link + store-listing state;
  this SESSION-LOG entry. eas.json was already wired last session.
- What is now true that wasn't before: Android publishing is automated and proven (a build
  reached a Play track via the service account, no manual upload). The latest member-fix
  build (vc 6) is installable by Cameron via internal testing right now. Store listing is
  ~90% done (text + icon + feature graphic in; screenshots pending).
- What's next / handed off: (1) Cameron uploads the 6 screenshots in store-assets/ under
  Phone / 7" tablet / 10" tablet (Add assets → Upload) — this is the last store-listing
  item and it needs the native picker only he can use. (2) After the listing turns green,
  set up the closed-test track (eas submit to a closed track) + line up 12 testers; the
  14-day clock then starts. The single substantive human dependency for public Android is
  those 12 testers.
- Commit: fbd9842

## 2026-06-26 — iOS SUBMITTED TO APPLE FOR PUBLIC REVIEW (App Privacy published)
- What we did: Finished the last iOS blocker and pushed the app to public App Store review.
  Completed and PUBLISHED the App Privacy data-usage label in App Store Connect (the one
  thing the API couldn't do): declared 4 data types — Name, Sensitive Info (the religious
  faithNote), Other User Content (inbox messages), User ID (anon Firebase UID) — each as
  "App Functionality", linked to the user's identity, used for NO tracking. Basis came from
  reading messaging.ts (Firebase persistently stores those tied to an anonymous UID; the
  Anthropic chat is real-time so it isn't "collected"). Then via the ASC REST API: added the
  version item to the review submission (201, READY_FOR_REVIEW — no blockers left) and
  PATCHed submitted:true.
- What changed (files/commits): no app CODE change. Docs/config only: START-HERE.md updated
  to reflect iOS submitted; new ANDROID-PUBLISH-PATH.md; auto-memory updated.
- What is now true that wasn't before: **iOS v1.0 (build 6) is WAITING_FOR_REVIEW at Apple**,
  releaseType AFTER_APPROVAL (auto-goes-live on approval). App Privacy is PUBLISHED. The
  entire iOS store side (metadata, screenshots, age rating, pricing, contact, privacy,
  submit) was driven without a Mac and without browser uploads.
- What's next / handed off: iOS — just wait for Apple (~24h typical). Android to go public
  needs two owner-only things from Cameron: (1) round up 12 testers for the 14-day closed
  test, (2) download one Google Play service-account key and hand it to me. See
  ANDROID-PUBLISH-PATH.md. Public Android is ≥2 weeks out by Google's rule regardless.
- Commit: 137726d

## 2026-06-26 — Double-check pass found & fixed a MEAT LEAK (non-members saw meat)
- What we did: Cameron said "double check everything." Re-verified the whole three-way
  routing against the actual files (not trusting prior claims). Found a real bug:
  free-text onboarding (`inferTagFromText`) keyword-guessed the feed tag and sent
  generic Christian words (faith/church/gospel/grow/scripture) to MAINTENANCE — which
  shows the MEAT track. A Baptist/Catholic typing their faith in the opening free-text
  box would have seen meat on their very first feed. That broke milk-before-meat AND
  Cameron's law that ONLY Latter-day Saint membership flips the flow.
- What changed in the app (files/commits):
  - `inferTagFromText` now routes free text through the SAME guarded path everything
    else uses — `harvestSignals -> routeFeedTag` — so the founding entry obeys the
    LDS-only member guard and the bridge-acceptance rule. (useAppStore.ts)
  - chatEar: split sentences on semicolons too, so a negated clause can't silence a
    real acceptance in the next clause and vice versa.
  - chatEar: detect the exact contradiction Cameron named — God does NOT damn people
    for His glory — guarded so a Calvinist AFFIRMING the harsh view stays on milk.
- What is now true that wasn't before: Every non-LDS tradition starts on milk, the way
  Jesus would treat them the same. Only explicit LDS self-ID reaches the member/meat
  track. Verified: tsc 0; 18/18 route cases pass (Baptist/Catholic->MILK, LDS->
  MAINTENANCE, ambiguous "mission/priesthood" don't mint membership, third-person &
  negation guarded, bridge acceptances->BRIDGE, Calvinist affirming harsh view->MILK).
- What's next / handed off: re-shipped corrected OTA + new build (the earlier 80b009d
  OTA/build were pre-fix and must be replaced on the phone).
- Commit: cb9ac2b

## 2026-06-26 — Three-way stage structure: member / bridge / milk, the Jesus way
- What we did: Implemented Cameron's full ministering structure and tightened member
  detection to exactly one religion, per his correction.
- What changed in the app (files):
  - `mobile/src/engine/chatEar.ts` — added two bridge-acceptance signals
    (`accepts_ongoing_revelation`, `rejects_creation_ex_nihilo`) to VALID_REPORT_TOKENS
    and harvestSignals (affirmation-only, negation-guarded); TIGHTENED member markers to
    be unambiguously Latter-day Saint (dropped bare "served a mission" / "hold the
    priesthood" which other faiths use).
  - `mobile/src/engine/connect.ts` + `connect.py` (kept in sync) — added `BRIDGE_SIGNALS`
    + `bridgeReady()`; added `accepts_ongoing_revelation` to the milk gate's openness set.
  - `mobile/src/store/useAppStore.ts` — rewrote `routeFeedTag` to the three-way structure
    (member→MAINTENANCE, gate+consent→RESTORATION, bridgeReady→BRIDGE, else MILK) and
    REMOVED the old wrong "analytical doubt → BRIDGE"; biased the BRIDGE content pool to
    the question-sparking `restoration` milk track; injected a bridge note into the chat's
    LIVE GUIDANCE; humanized the two new signals for the Profile.
- What is now true that wasn't before: ONLY membership in The Church of Jesus Christ of
  Latter-day Saints flips the app into member/meat mode — every other tradition is treated
  the same. A non-member moves into the BRIDGE only by accepting a distinctively-LDS truth
  in their own words (God isn't cruel for His glory, God still speaks, creation organized
  not made from nothing); on the bridge the feed and chat steer a little harder toward the
  Restoration while still never naming the Church before the milk gate.
- Verified: tsc 0, web export 0, feed_test ALL PASS, connect.py self-test passed, node
  regex tests (member-only + bridge acceptances, with negation/third-person) ALL PASS.
- What's next / handed off: this is IN CODE; kicking off a new build so it reaches the
  phone. Future: build the deeper member "meat" learning sections + more bridge ministering
  functions/content.
- Commit: 5152c22

## 2026-06-26 — Member recognition FIXED + reset/public-release rules rewritten
- What we did: Fixed the app's #1 broken behavior — editing the faith box on the
  PROFILE to say "I am a member of the Church of Jesus Christ of Latter-day Saints"
  was being IGNORED instead of snapping the app into member/meat mode. Also confirmed
  the chat-header and iPhone-animation complaints are already fixed in code (old build
  on the phone), and rewrote two of Cameron's rules (reset + public-release promise).
- What changed in the app (files):
  - `mobile/src/engine/chatEar.ts` — broadened member self-ID phrasings in
    `harvestSignals` + added negation/third-person guards (Law 8 honored).
  - `mobile/src/store/useAppStore.ts` — `editFaithWord`, `addFaithWord`, and
    `recordFaithBackground` now detect `becameMember`, enable discipleship, push a
    "Welcome, fellow Latter-day Saint" moment, and `appendMetaMessage` to chat — the
    same member handling the chat path already had.
  - `mobile/src/screens/FeedScreen.tsx` — visible gold "Walk with Christ" banner on
    the home feed whenever the person reads as a member; taps into Discipleship.
  - `START-HERE.md` — removed the "Start fresh" reset idea (decided against; users
    remove/edit individual items instead); rewrote the public-release rule into a sworn
    promise that the assistant does everything up to the single legally-required tap and
    points Cameron right at it; logged the member fix; bumped date to 2026-06-26.
  - `.auto-memory/MEMORY.md` — recorded the member fix, the two-stage non-member design
    (unbeliever/milk vs bridge) + member meat track, the reset decision, the promise.
- What is now true that wasn't before: editing the Profile faith box to declare LDS
  membership snaps the whole app into member/meat mode (feed → MAINTENANCE, discipleship
  companion on, visible banner, chat acknowledgment) and it fires from any faith-write
  path or from chat. Verified: regex unit test all-pass (7 yes / 6 no) + `tsc --noEmit` 0.
- What's next / handed off: these fixes are IN CODE but NOT on Cameron's phone yet — they
  need a new build (or `eas update` for the JS-only parts) to land. The header/animation
  complaints clear with that same build. Larger follow-up: build out the deeper member
  "meat" learning sections and the bridge-stage ministering functions.
- Commit: 6dc061c (+ this log update committed right after)

## 2026-06-26 — Built the memory chain so chats stop losing context
- What we did: Diagnosed why new chats kept losing the project's true state and
  repeating stale facts (the "create a Google Play account / pay $25" mistake).
- Root cause found: `.auto-memory/MEMORY.md` (June 19) still listed Google Play as
  "pending ($25+ID)", and there were 24+ competing status/handoff docs with no clear
  winner, so chats trusted whichever stale file they read first.
- What changed:
  - Fixed the stale "pending Google Play $25" line in `.auto-memory/MEMORY.md` and
    added a banner pointing to START-HERE.md as the truth.
  - Rebuilt `START-HERE.md` into the single dated current-state file (accounts all
    exist; iOS on TestFlight; Android internal testing v3/v4 shipped, v5 built; the
    "code committed != code on phone" build gotcha; file-authority hierarchy).
  - Pointed `CLAUDE.md` (auto-loaded) at START-HERE.md first.
  - Created `SESSION-OPENER.txt` (paste-at-start checklist) for Cameron.
  - Created this `SESSION-LOG.md` chain and the start-of-chat recap protocol.
- What is now true that wasn't before: there is one dated source of truth, the stale
  Google Play lie is gone, and every future chat is instructed to open by recalling
  the last session from this log and verifying it against git.
- What's next / handed off: (optional) move the old contradicting status docs into an
  /archive folder; the written-but-not-built items remain — tiered model routing,
  Profile "Start fresh" reset, belief/testimony dialogue option.
- Commit: 16f2d65 (system created) — see also the follow-up commit that recorded this hash
