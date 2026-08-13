## 2026-08-13 (author lane, unattended/headless) — ROW 140 bronze-serpent AUTHOR-FIX: b17 Moses identity BLOCK cleared, handed back to the runner (complaint-first), $0 — Machine A `Dev`, Fable-5 author lane

**Commit:** `ae6560b98` (row 140: beats_v2.py + QC.md + ASSEMBLED-PROMPTS.txt + AUTHOR-BOARD + bad-s17 delete).

Dispatched to AUTHOR-BOARD row 140 (The Bronze Serpent — Cameron's approved
replacement that CUTS the Naaman prodigal-dupe he rejected; open complaint keyed
to 140). State was NEEDS-REBUILD with a RUNNER PARK note: all 24 stills built
(0 rerolls ~$3.48) but ONE authoring BLOCK — b17/s17-lifted-on-a-pole rendered a
young non-canonical Moses because b17's `locks` OMITTED the `MOSES` token, so the
char ref (`moses.jpeg`) never attached (it attaches by lock token, not prose).

**Author fix (the park note's spec):**
- Added `"MOSES"` to b17's `locks` in `beats_v2.py` (now
  `["MOSES","SERPENT-POLE","WILDERNESS-CAMP"]`) — symmetric with the working Moses
  beats b03/b11/b13/b15. Verified: `--check` PASS (24 beats); the "MOSES LOCK:"
  text now appears in b17's ASSEMBLED prompt (`--dump`). moses.jpeg present.
- **Deleted the one bad `assets/s17-lifted-on-a-pole.jpeg` (git rm)** so the runner's
  `v2_gen_api` resume regenerates ONLY b17 (missing-frame → COST LAW skips the 23
  banked-good frames; touch-once holds). Had to re-delete once — a concurrent lane's
  git op restored it before I committed; committed atomically the second time.

**Routing decision (why AUTHORED+Ready ✅, NOT BUILT):** row 140 was NEVER shipped,
so there is no live card hash. The documented "flip NEEDS-REBUILD→BUILT for the
cfix lane" path (PROMPT lines 93-108) only works for SHIPPED rows with a live
complaint hash — here cfix's `cur.get('140') is not None` guard is False and verify
skips rows in openc, so BUILT would STRAND it. Correct lane for a never-shipped
row with 23/24 stills is the RUNNER: set State NEEDS-REBUILD→AUTHORED, Ready ✅,
Claim cleared. Verified against the live picker: row 140 parses runner-eligible AND
(being in openc) is picked COMPLAINT-FIRST (picker line 272). QC.md handoff written
with exact runner steps + the caveat that the SERPENT-POLE plate was promoted from
the OLD bad s17 (if its young-Moses bleeds through the regen, reroll s17 + re-promote
the plate). Runner will regen b17 → assemble (AUDIO LOCK from V1 segment mp3s) → ship
→ resolve the Naaman-dupe complaint.

**Cost:** $0 (no Gemini, no ElevenLabs — one token edit + one frame delete). Author
queue is otherwise drained (0 NEEDS-BEATS, 0 NEEDS-REBUILD, 0 unfinished AUTHORED;
62 AUTHORED-Ready wait on the paid runner; 3 NEEDS-AUDIO 155/156/157 route to the
audio lane, not author — left for it).

## 2026-08-13 (cont. 102) — ROW 146 vine-and-branches C-FIX SHIPPED: Cameron's "0:40 white faces / 0:47 multiple arms / 1:19 Jesus missing a hand" ALL THREE FIXED, FULL-CUT GATE 14/14, $0.40/3 rerolls, audio byte-identical — Machine A `Dev`, Opus runner (unattended/headless)

**Commit:** ship `d4b437a004b0` (mp4 + QC autopsy + 3 rerolled stills + boards + api-spend); card repoint + complaint-resolve + lessons this session's commit B. Complaint-first + low-number dispatch to AUTHOR-BOARD row 146 (lowest waiting row with an OPEN picture complaint, reportedAgainst the live cut a62787cfb). Read PROMPT-OPUS-RUNNER laws + all rubric lessons + `v2_outline.py 146` first (LEARNING LAW).

**Cameron's complaint (complaintHash a62787cfb, against the live cut):** "0:47 man has multiple arms replace the picture, 0:40 picture some bystanders have white faces, fix it replace it. 1:19 picture has Jesus missing a hand, fix it."

**TRACE → RENDERED frames (from the live mp4 + beat windows, not beat names):** 0:40 = b04 `s04` (window 39.26–40.65, moonlit crowd faces drained grey/white); 0:47 = b09 `s09` (43.17–46.63 held through gap; foreground man read as a 3rd arm — traced past the *adjacent* s08 which is a different, on-brief golden-dusk frame, left untouched); 1:19 = b14 `s14` (73.68–78.39; Jesus's clasp merged a hand AND rendered near-black).

**PROMPT AUTOPSY = ALLOWED ×3 (rubric meta-law 3):** all three were missing constraints, not bad refs. Hardened the three beats' prose: b04 → warm-olive-skin floor + ban grey/ashen/white faces; b09 → recompose to the ACTUAL brief (TIGHT moonlit hands-on-one-branch) + ban tools/walking-away + ban any third/floating/disembodied arm (which also de-duplicated it from s08 and fixed its wrong golden-day time-of-day); b14 → BOTH Jesus hands visible five-fingers each + explicit night-readability floor (not near-black). Rerolling without the autopsy is forbidden — verdicts recorded in QC.md.

**FIX + FULL-CUT GATE (6b):** 3 rerolls (b04/b09/b14 = 3/14 = 21%, ~$0.40; mandatory complaint-fixes, exempt from the discretionary ≤15% budget; rest of cut reused untouched). Verified in the RENDERED mp4: 0:40 all warm faces; 0:47 clean three-distinct-men one-hand-each at night; 1:14–1:18 Jesus clasps with both hands, five fingers, clearly lit (the dark 79s frame is only the fade to card). Other 11 beats extracted at mid-window and viewed — all clean. **14/14 PASS.** AUDIO LOCK byte-identical: AUDIO REBUILD PASS SHA256 `ae063a39…` (same as prior ship, nothing re-voiced), 84.8s / 20.5 MB.

**COST/LEARNING LAW:** ~$0.40 this touch, $0 audio — far under $6.10/row avg → trend DOWN. New RUNNER-LESSONS line + rubric **lesson 22** (night beats need three floors: warm-skin, no-spare-arm, readability) with Cameron's exact words. REVIEW-LESSONS 146 → open:false, resolvedBy d4b437a0. Card flag answers all three complaints in his words. Deploy + live-verify below.

---

## 2026-08-13 (cont. 102) — ROW 149 hannah-is-heard SHIPPED realistic-V2: Cameron's "Wrong caption at 2:06" FIXED & verified, FULL-CUT GATE 22/22 PASS, $3.62/2 rerolls (9.1%), live served==local — Machine A `Dev`, Opus runner (unattended/headless)

**Commit:** ship `52901ef7ce29` (card repoint `b20c13abd`; stash `7b027b83e`; publish-loop `a7ccd3d7d`; this SESSION-LOG commit closes the link). LOW-NUMBER dispatch to AUTHOR-BOARD row 149 (lowest ready AUTHORED). Cross-checked QUEUE.md (149 = Hannah/Eli/Samuel · 1 Sam 1 — consistent, not swapped) before spending. Read the two META-LAWS + all 20 rubric lessons + RUNNER-LESSONS defect memory + `v2_outline.py 149` first (LEARNING LAW).

- **OPEN complaint "Wrong caption at 2:06" — FIXED, proven in the rendered mp4.** Root cause = the frozen/dead-tail class (rows 83/86 family). This fresh V2 build fixes it: rendered frames at 125.5s/127.5s (= 2:05–2:07) show the CORRECT synced narrator caption over the correct picture (s22, Hannah walking away), NOT a frozen/wrong one; then a clean, narrated closing card (131.6→139.2s) ending ~1.6s after the last word. Transcription proof: audio fully narrated to ~138s (no 13s dead tail); video 139.17s vs audio 139.62s (ends on/before audio). AUDIO LOCK PASS eb5cb45e (byte-identical to V1 mp4, nothing re-voiced).
- **Built 22 realistic-V2 stills first-attempt, 2 rerolls/22 = 9.1% (COST-LAW budget was 15%), ~$3.62, meter $630.7→$634.4** — under the $6.10/row average (cost trend DOWN). 3 reused-forever portraits (HANNAH/ELI/SAMUEL; SAMUEL is a deliberate newborn→toddler→boy age panel). Rerolls: b03 (3-panel collage→single coherent tabernacle-door frame), b20 (modern glass hurricane lamp→period clay lamp).
- **FULL-CUT GATE (6b) on the rendered mp4 — 22/22 beats + 3 caption-type frames + card = PASS.** Identity ONE actor each (Hannah / Eli / Samuel-aging); scale gate PASS; realistic-only (no cartoon/mix/collage after rerolls); period clay saucer lamps every scene, no modern object after b20; the vow gesture-set + order-gate (b17 no child/sign) + leaving direction-law (b22) all read; captions 3-voice colour correct — NARRATOR white, HANNAH/woman-KJV pink, SCRIPTURE (Eli's blessing) light-blue — bottom-band only, synced, card clean. FIX-WAVE only (one light-haired background toddler s01/s19; Eli soft-cap drift, beard consistent) — non-blocking.
- Shipped two commits (mp4+QC+boards `52901ef7`; card repoint `b20c13abd`). Firebase deployed (pruned 5 old versions past the storage-quota 429, then deploy OK) + LIVE-VERIFIED: card v149 realistic-v2 + data-hash 52901ef7, mp4 HTTP 200 20.18MB, served md5 == local `7795bebc`. STASH-INDEX rescanned (3716 stills/130 builds). Publish-loop sync (0 new publishes — awaits Cameron's approval). Board State→BUILT (Appr/Post untouched). No new RUNNER-LESSONS class (clean row).

## 2026-08-13 (cont. 101) — ROW 121 salt-and-light C-FIX SHIPPED: Cameron's "0:31 double picture" + "2:45 corny big Jesus floating in the sky" BOTH FIXED, FULL-CUT GATE 29/29, $0.27/2 rerolls, live-verified served==local — Machine A `Dev`, Opus runner (unattended/headless)

**Commit:** ship `f19b00152` (card repoint in `acbd1e367`; memory/complaint-resolve this commit). Complaint-first + low-number dispatch to AUTHOR-BOARD row 121 (lowest waiting row with an OPEN complaint). Read PROMPT-OPUS-RUNNER laws + `v2_outline.py 121` first (LEARNING LAW).

- **Cameron's complaint (his words):** *"0:31 has a double picture and needs to be replaced. 2:45 is corny looking with a big Jesus floating in the sky it needs to be replaced."* Both PICTURE-domain — traced each timestamp to the frame that renders there: 0:31 = **b05/s05**, 2:45 = **b29/s29** (extracted from the live mp4, not guessed from beat names).
- **Confirmed both defects were baked into the source stills:** s05 was a genuine Gemini DIPTYCH (dusk lane stacked over a trodden-salt feet close-up, hard horizontal seam); s29 was a giant front-facing Jesus bust floating against the sky with no ground contact.
- **PROMPT AUTOPSY (meta-law 3):** b05 = **ALLOWED** — the LANE place-lock (a WIDE dusk-street image) attached to a TIGHT feet-level scene let Gemini stack the two references; remedy = added anti-diptych/single-frame constraint + "lane recedes softly in the background of the SAME frame" (lock kept). b29 = **ALLOWED + IGNORED** — the authored over-the-shoulder/"backs to the height" direction was ignored (rendered his front face) and nothing bounded scale/grounding; remedy = rewrote to a true from-behind, grounded, natural-scale Jesus watching the crowd descend.
- **Rerolled b05 + b29 only (2/29 = 6.9%, under the 15% budget), $0.27, meter $630.47→$631.27** — far under the $6.10/row average, cost trend DOWN. Touch-once: both fixes batched into one re-cut.
- **FULL-CUT GATE (6b) on the WHOLE rendered cut — all 29 beats + 3 caption frames + question card viewed:** the two complained beats FIXED (verified in the new mp4 at 0:31 and 2:45); **all 27 others CLEAN** (Jesus one locked face & natural scale in all 9 face beats, cream-only, no halo on a LIGHT row, lamp continuity chain reads, anatomy clean, realistic-only, captions bottom-band WHITE/RED, card clean). The prior 2026-08-12 QC-VERIFY that called this row "29/29 CLEAN" MISSED both — the row-11 failure this gate exists to prevent; caught and fixed this touch.
- **AUDIO LOCK PASS 642b6930 byte-identical** (nothing re-voiced/re-timed); mp4 content hash MOVED 20125547→02ff91fc so the complaint closes. Shipped (mp4+QC+beats+board), repointed card v121 (data-hash f19b0015, ?v=f19b00152e7c, flag answers Cameron's two complaints in his words), **Firebase deployed + LIVE-VERIFIED: served card v121 data-hash f19b0015, mp4 HTTP 200, served bytes 20096559 == local**. Complaint marked resolved (REVIEW-LESSONS open=false + resolvedBy; COMPLAINTS FIXED). 2 new RUNNER-LESSONS (wide-plate-on-tight-beat diptych trigger; from-behind grounding kills the floating-giant Jesus). STASH rescanned (3716 stills). Publish-loop sync (0 new publishes — awaits Cameron's re-approval).

## 2026-08-13 (audio lane, unattended/headless) — Rows 152/153/154: STALE-V1 AUDIO-FIX DONE, handed to picture runner — Machine A `Dev`

**Commit:** `d5fad6891` (154; 153 `aff2f515a`; 152 `758dd44e8`)

**Continuation of the same audio-lane session that shipped row 117** (below). After 117
I worked the next-lowest NEEDS-AUDIO rows per the LOW-NUMBER LAW. 152/153/154 are all the
same **STALE-V1 (row-147 class)** park: the V1-dir narration mp3s were re-recorded in the
new-voice ElevenLabs cast AFTER the old V1 mp4 render, so `v2_assemble`'s AUDIO LOCK
newer-mp3 tripwire refuses. All three have **0 stills** — so the fix is a $0 flag-set +
handoff, never a re-voice or a picture build.

**Per row (identical procedure):**
- Voice-ID'd every V1-dir mp3 = **44100 Hz / 128 k = chosen ElevenLabs new-voice** (152: 11
  mp3s; 153: 13; 154: 11 — zero old edge-tts segments).
- Set `AUDIO_FROM_V1_SEGMENTS = True` in that build's `beats_v2.py` (off the runner
  write-list; rebuilds audio from the newer mp3s at extract_beats offsets — nothing
  re-voiced, nothing re-timed, V1 read-only).
- Pre-flight PASS on all three: `extract_beats` (152=131.3s/10, 153=161.6s/12,
  154=141.4s/10), `v2_prompt <build> --check` v4 PASS (152=21, 153=26, 154=23 beats),
  `audio_audit --rows N` = **0 old-voice segments**.
- Board State NEEDS-AUDIO → AUTHORED, Ready ✅, Claim cleared (archived note in Ready col)
  so the PICTURE RUNNER builds the stills on the now-valid audio and ships. QC.md ✅ note
  written per row. **Row 153 carries an OPEN complaint for the runner:** "1:12 needs
  Peter" — b13 already re-authored to show Peter's arm at ~1:12; the runner MUST verify it
  in the FULL-CUT GATE before shipping (carried in 153's QC COMPLAINT LEDGER + board note).

**Cost:** $0 Gemini, $0 ElevenLabs, 0 rerolls across all three (no TTS, no image gen).

## 2026-08-13 (Opus runner, unattended/headless) — Row 140 The Bronze Serpent: 24 realistic stills BUILT + FULL-CUT-QC'd (0 rerolls ~$3.48), PARKED → NEEDS-REBUILD on ONE authoring block (b17 locks omit MOSES token) — Machine A `Dev`

**Commit:** `cb082d581` (park: 24 assets + 2 plates + 2 portraits + PLACE-WIRING + QC.md + AUTHOR-BOARD + QUEUE + RUNNER-LESSONS).

Claimed AUTHOR-BOARD row 140 (lowest Ready, complaint-first: the Bronze Serpent
is Cameron's approved replacement for the Naaman/prodigal-dupe he rejected).
Cross-checked QUEUE — story matches, legitimate build. Read the two META-LAWS +
all 20 rubric lessons + all of RUNNER-LESSONS before spending (Learning Law).
`--check` PASS (24 beats). Portraits (MOSES, BITTEN-MAN) $0.27. Promote-first per
QC: b01 → WILDERNESS-CAMP plate (great camp wide, camera-behind-backs), b17 →
SERPENT-POLE plate. Generated all 24 at 2K under ceiling (meter 624.71→632.88,
**$3.48/row, 0 rerolls = 0%** — well under the $6.10/19% baseline; not a full
shipped-row cost since parked).

**FULL-CUT GATE: 23/24 PASS.** Canonical Moses (old, long white hair, full white
beard, brown robe+dark mantle, staff) is consistent across s03/s11/s12/s13/s14
(all MOSES-ref-locked); BITTEN-MAN consistent s09/s18/s19; snakes natural/no-gore;
dead shrouded with dignity/no-gore; no divine figure anywhere; cross-form
serpent-pole payoff clean; no modern objects; no lens-stares; row-14 behind-backs
geometry held on the wides. **ONE BLOCK: b17/s17 (hero + promoted SERPENT-POLE
plate)** rendered Moses as a younger brown-bearded man — a lesson-2/13 identity
break on the payoff frame. PROMPT-AUTOPSY = ALLOWED/IGNORED: b17's must_show NAMES
"Moses steadying its base" but its `locks` omit the `MOSES` cast token, so the
char ref attaches by token not prose → moses.jpeg never attached → free-invented
face. Runner CANNOT fix (editing `locks` is a hard rail; a blind --redo won't
attach the ref, so it can't restore the SAME face — lesson 10). Parked
**NEEDS-REBUILD** for the author lane with a one-token resume: add `"MOSES"` to
b17 locks → runner `--only b17 --redo` (SERPENT-POLE plate keeps the pole
byte-consistent, so b18-b24 need NO regen) → assemble (AUDIO LOCK from V1 segment
mp3s) → ship → publish. All 24 frames banked ($0 to reuse). New RUNNER-LESSONS
entry added (locked-cast named in prose MUST be in `locks`). FIX-WAVE minor:
s21 pale-eyed incidental, s24 faint sky "vision" overlay, s06 tiny bluish speck
by far tents — none blocking. Board: 140 State→NEEDS-REBUILD, Ready cleared,
QUEUE claim carries the park. 142 was RUNNING (sibling lane) — untouched.

---

## 2026-08-13 (Opus runner, unattended/headless) — Row 122 mote-and-beam: C-FIX SHIPPED — Cameron's 0:33 "head turned around backwards" (his 5th filing of this class) — Machine A `Dev`

**Commit:** `ac4eeba64` (ship: mp4 + QC + beats_v2 + RUNNER-LESSONS + rubric lesson 21); card/board/log follow.

**Cameron's complaint (against the current shipped cut, complaintHash 10f6bd9a):**
"The man's head is turned around backwards 0:33. same problem for the 5th time."

**Trace:** 0:33 renders beat **v2-r122-b06** (`s06-and-we-are-experts-at.jpeg`,
window 30.05–34.53). The foreground bottom-centre listener sat with his BACK to
camera (the back-patch of his tunic toward the lens) while his face was wrenched
a full ~180° back to the lens — the owl-neck / head-on-backwards.

**PROMPT AUTOPSY = ALLOWED.** b06's scene asked for a legitimate "listener's eyes
slide sideways to a neighbour"; its anti-glitch line bounded COUNT only ("two
arms, two hands and one head") — nothing forbade an impossible neck rotation, so
the generator, needing a FACE glancing on a back-facing figure, screwed the head
around. Fix (verdict 2 — add the missing constraint): b06 `must_show` now puts the
glancer in three-quarter view with head AND shoulders turned the same way;
`must_not_show` + `scene` forbid the owl-neck / back-to-camera-face-wrenched-back,
and require every head to sit forward facing the same way as its own shoulders.

**Fix + FULL-CUT GATE:** 1 reroll of b06 (**1/27 = 3.7%**, ~$0.13) — foreground man
now faces away with the back of his head visible (natural), verified in the
RENDERED mp4 at 33 s. All 27 beats extracted at true mid-window and viewed: b06
was the ONLY owl-neck; b01/b02 use the same man but correctly show the BACK of his
head (facing away — verified by zoom, correct, NOT touched). Jesus locked +
green/hazel V2 eyes + cream-only + no halo on all 9 hillside beats; beam
absurd-never-gruesome throughout; b17 canonical fixer (prior QC-FIX) intact;
captions bottom-band only; closing card clean.

**AUDIO LOCK PASS SHA256=0df23a0e…** — byte-identical, nothing re-voiced. 175.0s /
20.1 MB. **Cost this touch ~$0.13, 0 audio $** — trend DOWN vs the $6.10/row avg.

**Learning law:** new RUNNER-LESSONS line (owl-neck class) + numbered rubric
**lesson 21** with Cameron's exact words + rows of record (122 b06), so the same
prose is never written again. Card flag answers his complaint in his words.
Deployed to Firebase + live-verified.

## 2026-08-13 (Opus runner) — Row 135 rainbow-covenant: resumed stranded build, FULL-CUT GATE caught the OPEN gender-balance complaint → PARKED NEEDS-REBUILD (author fix) — Machine A `Dev`

**Commit:** `fd27de444` (QC + board + RUNNER-LESSONS + plates + api-spend)

**Task:** resume the AUTHOR-BOARD row-135 build that a prior autopilot lane died on
mid-way (State RUNNING, Claim A-auto, 42/44 stills). Verified I was the target-row-135
lane (no other live gen owned it); already-shipped check = NOT shipped (no committed mp4,
no live card).

**What I did:** generated the last 2 frames (b43,b44 MOUNTAIN landscape/family), then ran
the FULL-CUT GATE on all 44 (this row was never gated — the dead lane never reached its
own gate). Read `v2_outline.py 135` (the LEARNING-LAW step the resume skipped) and found
the real OPEN complaint: **"1st picture has 3 girls and 5 boys that needs to change"** — a
GENDER-BALANCE rule: the eight = 4 men (Noah+3 sons) + 4 women (wife+3 wives), all adults.

**Why NOT shipped:** "8 total" is not enough — a 5m/3f frame REPEATS the complaint. Audited
every family frame for the sex split: **s06, s09, s25, s27 still render 5m/3f** (s09 also a
7-count). Rerolled the clear garbage that a runner CAN fix — b43 (7→correct 8 under a full
bow, 2 takes), b08 (child among the eight → 8 adults) — but s09 and s27 hit the 2-reroll cap
and stayed 5m/3f: the shared FAMILY lock + the intimate/huddle beats (b09 centers "one wife",
b25/b27) don't pin the 4m/4f split, so ~1/3 of family frames drift. That is a beat-text/lock
fix (author lane) — runner hard-rail forbids editing locks/beat content. Shipping would
re-file the exact complaint = the LEARNING LAW's worst failure. So PARKED, with the 40 good
frames on disk for reuse and a one-edit author fix documented (pin "4 men + 4 women, all
adults" in the FAMILY lock + give b09 a count pin → regen ONLY s06/s09/s25/s27 → assemble on
the already-fixed byte-stable audio → ship).

**Cost:** 7 rerolls (b43×2, b08×1, b09×2, b27×2) = 15.9% of 44 beats — a small logged overage
vs the 15% budget, spent chasing the count on the counts row before the systemic gender cause
was isolated. ~$0.94 Gemini (meter ~$632.4). No audio touched. Filed the "count complaint is
really a gender-balance complaint — audit 4m/4f not just 8 total" pattern into RUNNER-LESSONS.

---

## 2026-08-13 (audio lane) — Row 117 hosea-buys-her-back: closing-card "dramatized" re-voiced & SHIPPED — DEPLOYED — Machine A `Dev`

**Commit:** `bd4b029c3` (review.html + SESSION-LOG); mp4/QC/board commit `33b7d3ba1`

**Cameron's complaint (`v2_outline.py 117`):** *"it was all good until the very end
where you miss pronounced 'Dramatized' — fix that audio at the very end and its good."*

**Domain:** AUDIO, not picture. "dramatized" occurs in exactly one place — the closing
question card (`make_narration.py:56`). No still was wrong; 38 stills untouched
(complaint-first / touch-once). Row was parked NEEDS-AUDIO; picked lowest waiting
complaint per the LOW-NUMBER LAW.

**Diagnosis + fix:** ElevenLabs narrator Brian naturally read the word with the pitch
rising into the 2nd syllable (112→121 Hz) = the "druh-MAT-ized" sound Cameron heard.
Re-voiced the CARD ONLY through `mbm_eleven.render_segment` (Brian, 44100/128k — the
same engine the row already ships) with the spoken respell "DRAMatized" (caption stays
"dramatized"). Rendered a 6-take batch, scored each by front-stress energy + pitch;
chose the take with a falling contour (124→108 Hz) and front-loaded energy, then
pitch-preserving atempo-locked it to the original card duration (13.375s) so no
downstream still-window moved. Verified on the SHIPPED mp4 at ~3:35: now "God
DRAM-uh-tized …", front-stressed (e_front 0.192 > e_back 0.157).

**Ship:** card md5 03f3d9e4→9e9cc0d6; mp4 SHA256 358dd0f3 (AUDIO REBUILD PASS, 229.746s,
20.8 MB). Board 117 NEEDS-AUDIO → BUILT. review.html card v117 data-hash + ?v= + 🛠 flag
rewritten to answer Cameron in his words (old flag falsely claimed byte-identical audio).
Deployed `firebase deploy --only hosting` + live-verified.

**Cost:** $0 Gemini, 0 image rerolls. ~10 short ElevenLabs card takes (candidates +
robustness + 6-take pick). Only the card segment changed; all other voices/wording/timing
untouched.

## 2026-08-06 (interactive) — Posting tracker: all 200 rows, ✓ approved check, live WEB chip — DEPLOYED — Machine A `Dev`

**Commit:** `4a84e097e`

**Cameron's order:** the Posting tracker must show ALL 200 stories (number + name always
there), a ✓ check that lights when he approves one, and a WEB chip that lights when the
website has the video and links straight to it, so he can verify everything is on there.

**What changed (site/review.html, tracker section + renderTracker only; Firestore doc
shapes and toggleSocial untouched):**
- Tracker now lists every story (200 rows, numeric order) instead of only approved ones.
- New ✓ chip per row — lit green only when the CURRENT cut carries Cameron's approval
  (`approved && approvedHash === data-hash`), display-only.
- New WEB chip — truth-driven, not hand-set: on load the page fetches the live
  `/stories.html` (same origin, no-store) and lights WEB only for story numbers actually
  linked there (`data-video="/story-videos/N.mp4"`); a lit WEB is an <a> straight to
  that video on the website. Fetch failure = dim chips titled "could not check".
- Bars now read Approved / Website / In the app / YT / IG / TT / FB, all out of 200.
- Tapping a story name jumps to (and opens) its review card, opening any collapsed
  section it sits in.
- Verified LIVE on https://milk-b4-meat.web.app/review.html after
  `firebase deploy --only hosting`: 200 rows, ✓ lit on 122, WEB lit on 116, name-jump
  works, no console errors, still zero preloaded <video> elements.

**Found by the new chip — 6 APPROVED videos the website does NOT serve:** rows 89
(Last Supper), 94 (Father Forgive Them), 129 (Nazareth Only a Few), 137 (One As We Are
One), 141 (Bread of Life), 151 (If Any Lack Wisdom). App has them; website is behind.
Spawned a follow-up task chip to publish them through the audit_public_videos gate.

## 2026-08-13 (cont. 100) — ROW 117 hosea-buys-her-back: AUDIO-domain complaint ROUTED to the audio lane (NEEDS-AUDIO), pictures untouched — Machine A `Dev`, Opus runner (unattended/headless)

**Complaint-first + low-number dispatch to AUTHOR-BOARD row 117** (lowest waiting row with an OPEN complaint). Read PROMPT-OPUS-RUNNER laws + `v2_outline.py 117` first (LEARNING LAW).

- **Cameron's complaint (his words):** *"it was all good until the very end where you miss pronounced 'Dramatized' — fix that audio at the very end and its good."*
- **Domain verdict: AUDIO, not picture.** Grep-confirmed "dramatized" appears in EXACTLY ONE place in the whole cut — the closing question **card** narrator line (`make_narration.py:56`: *"God dramatized his own love with a marriage…"*). No still renders wrong. Per runner law 6b (audio-domain complaint) + touch-once/complaint-first: the picture runner does NOT re-cut pictures for a pronunciation defect — that would burn credits and change nothing Cameron flagged. All 38 stills stay as shipped.
- **Routed to the audio lane, not stranded.** Set State column BUILT → **NEEDS-AUDIO** (Audio col stays OK; Claim carries `RUNNER PARK`, no `AUDIO-FIX` string) so `autopilot.sh` line 219 (`st == 'NEEDS-AUDIO' and 'AUDIO-FIX' not in cl`) routes it to PROMPT-AUDIO-FIX. Wrote the full per-row authority into QC.md "RUNNER PARK 2026-08-13": re-voice ONLY the card so "dramatized" = DRAM-uh-tized (first-syllable stress); shipped card comes from the V1 dir (AUDIO_FROM_V1_SEGMENTS=True) so re-render `media-production/build-117.../audio/card.mp3`; transcribe first (44100/128k = likely ElevenLabs → SAY-map bypassed, re-render directly + A/B round-trip; if edge, add a measured SAY winner). Caption spelling stays "dramatized". Then re-assemble (AUDIO LOCK PASS), deploy, live-verify, review card answers his complaint in his words.
- **$0, 0 credits, 0 rerolls** — no image generation touched; picture-runner correctly hands the pronunciation fix to the audio toolchain.

## 2026-08-13 (cont. 99) — ROW 147 C-FIX #2 SHIPPED: "Joseph Forgives · Genesis 45" — Cameron's "same character / same face definition, match the story of Joseph" complaint FIXED with a REAL re-cut (content hash MOVED), FULL-CUT GATE 16/16 PASS, $0/0 rerolls — Machine A `Dev`, Opus runner (unattended/headless)

**Complaint-first + low-number dispatch to AUTHOR-BOARD row 147** (lowest waiting row with an OPEN complaint). Read PROMPT-OPUS-RUNNER laws, the two META-LAWS + all rubric lessons, RUNNER-LESSONS, and `v2_outline.py 147` first (LEARNING LAW).

- **Root-caused why the complaint kept reopening:** the prior same-day C-FIX was VERIFY-ONLY — it judged Joseph consistent and shipped the SAME mp4 (bytes unchanged, f7912b56). A complaint does not close until the mp4 CONTENT HASH moves (memory: cfix query-bump vs hash), so autopilot re-dispatched row 147 repeatedly. This session shipped a real re-cut.
- **AUTOPSY = ALLOWED (already-locked, unshipped):** JOSEPH was ALREADY an IMAGE lock — `REFS = {"JOSEPH": "CAST-REF-V2/joseph.jpeg"}` in the authored beats_v2.py; joseph.jpeg (17:24) predates every still (17:25+), so all 16 stills were generated WITH the canonical portrait attached. A prior lane had staged a DUPLICATE REFS block (redundant no-op) plus regenerated s02 but never re-assembled. Reverted the duplicate (`git checkout HEAD -- beats_v2.py`, single REFS, `--check` PASS).
- **Re-assembled the 16 realistic stills (incl. the on-model regenerated s02)** → AUDIO REBUILD PASS SHA256 f3cfb249 (audio byte-identical — nothing re-voiced/re-timed). mp4 md5 f7912b56 → **3dbc5095** — content hash MOVED, complaint closes. **$0 Gemini / 0 rerolls** (the old stills are already image-locked and on-model; regenerating would violate the COST LAW and risk new drift). Cost trend: $0 this row keeps the running average falling.
- **FULL-CUT GATE (6b) — SOURCE stills (16-tile contact sheet) + RENDERED mp4 (s02 / reveal-caption / close-up / end card): PASS.** One canonical clean-shaven Hebrew-Egyptian Joseph matched to joseph.jpeg in every frame (the 1:20 close-up IS the reference), aged correctly (grey temples in the Genesis-50 beats), realistic-only (zero cartoon/mixed), anatomy/hands clean, ten weathered brothers, granary alive not famished, no modern objects, no Jesus (OT row), no halo; captions bottom-band, Joseph KJV scripture-blue / narrator white, in sync; end card clean.
- **"The story of Joseph and this story looking the same":** confirmed NO separate young-Joseph (coat/dreams/sold) build or queue row exists (84–87 = Joseph father of Jesus; 158 = tribe stick of Joseph). Nothing to match against yet; FACE-BOARD note wires any future Joseph-origin arc to this exact joseph.jpeg so the two will share one face. Card tells Cameron this in his own words.
- Shipped two commits (mp4+QC+board **baaeac4f**; review card repoint). Firebase deployed (pruned 4 old hosting versions past a 429) + **LIVE-VERIFIED**: card v147 data-hash baaeac4f, mp4 HTTP 200 20.3 MB, **served md5 == local 3dbc5095**. STASH rescanned (3694 stills). Publish-loop sync (0 new publishes — awaits Cameron's re-approval). Board Claim → C-FIX SHIPPED #2 (Built already ✅; Appr/Post untouched). No new RUNNER-LESSONS class.

## 2026-08-13 (cont. 98) — ROW 146 SHIPPED: "The Vine and the Branches · John 15" realistic-V2, complaint "Abideth is pronounced wrong" FIXED & byte-verified, FULL-CUT GATE 14/14 PASS, 0 rerolls $1.88 — Machine A `Dev`, Opus runner (unattended/headless)

LOW-NUMBER dispatch to AUTHOR-BOARD row 146 (lowest ready AUTHORED). Cross-checked QUEUE.md (146 = John 15, story consistent — not swapped) before spending. Read the two META-LAWS + all 20 numbered rubric lessons + the full RUNNER-LESSONS defect memory + `v2_outline.py 146` first (LEARNING LAW).

- **Open complaint "Abideth is pronounced wrong" — FIXED and proven in the ship.** The audio lane (2026-08-11) had re-voiced Jesus's John 15:5 line so "abideth" reads /uh-BY-deth/ (long-i, KJV). This runner built the pictures over that corrected track. PROOF it shipped: `AUDIO_FROM_V1_SEGMENTS=True` rebuilds from V1-dir mp3s, and `audio/j1b.mp3` md5 = `a4bb0de3…` (the corrected take, not the old `910b8468…`) → AUDIO REBUILD PASS `ae063a39`. Reviewer card answers Cameron in his own words.
- **Built 14 realistic-V2 stills first-attempt, 0 rerolls (COST LAW budget was 2/15%; used 0), ~$1.88, meter $622.16→$624.17** — well under the $6.10/row average (cost trend DOWN). 0 portraits (Jesus=global V2 ref; DISCIPLES=earth-tone band). VINEYARD plate = build-23 b03 (wired/present).
- **FULL-CUT GATE (6b) on the rendered mp4 — all 14 beats + 3 caption frames + card = PASS.** Jesus one locked face across s01/s02/s04/s07/s10/s14 (olive skin, dark wavy hair, full beard, calm ref-true eyes — NOT edited, rubric lesson 20), cream-only, no halo; scale gate PASS; night-moonlit Jesus beats vs golden-day vignettes as authored; period props only (clay lamps s01, billhooks+basket s08); no cartoon/mixed, no collage, no rotation, no 2nd cream, no modern object; grapes read as "much fruit"; green-cut vs withered branch pair correct; captions bottom-band, RED Jesus KJV (incl. abideth s10) / WHITE narrator, none over the art; card clean.
- Shipped two commits (mp4+QC+boards `a62787cf`; card repoint). Firebase deployed + LIVE-VERIFIED: card v146 realistic-v2 + data-hash a62787cf, mp4 HTTP 200 20.6MB, served md5 == local `f229b44a`. STASH-INDEX rescanned (3694 stills). Publish-loop sync (0 new publishes — awaits Cameron's approval). Board Built✅ (Appr/Post untouched). No new RUNNER-LESSONS defect class (clean row).

## 2026-08-13 (Fable 5, main session, pt.3) — 6 MORE APPROVED PUBLISHED (89, 94, 129, 137, 141, 151): 122 live, gate PASS all eight, stale v137 duplicate card removed — Machine A `Dev`

**Commit:** (this commit)

The quota wall broke via autopilot's refreshed mirror (01:35). refresh-postable
→ **122 postable** (+6: 89, 94, 129, 137, 141, 151); only row 170 still
excluded (cut genuinely changed since approval — awaits Cameron). **Root-caused
Cameron's "117th":** row 137 was approved at 00:16 but review.html carried TWO
v137 cards — the approved realistic one AND a stale old-Stephen-era duplicate
(built 07-22) that shadowed it in every parser (last-card-wins) and
false-excluded the row. Stale card removed (commit `e7bf15b21`), tag balance
verified, deployed. Slot 137's captions confirmed authored for the SWAPPED
story (One As We Are One · John 17), not Stephen.

Published the 6 exactly like the 116: exports copied (backups kept),
PRODUCED_VIDEO_IDS = exactly the 122, gallery + branded thumbs, deploy,
**live sha1-verified all 6**, ledger v2.1 events, **audit gate PASS all eight
checks** (now includes F1/F2 website-hygiene), OTA EAS group
`aa46cf51-06b7-4a82-8696-531565f2a0f5`. QUEUE ticked 122; tracker App chips
seeded 122. POST-QUEUE +6 entries; sheet/post-kit/per-video regenerated —
**122 APPROVED / 78 DRAFT, all 200 per-video files current.**

## 2026-08-13 (cont. 98) — ROW 140 AUTHORED FRESH: The Bronze Serpent replaces prodigal-dupe Naaman — full from-scratch story authored, gated, Ready for the runner — Machine A `Dev`, Fable-5 author lane (unattended, $0 image spend)

Author-lane session on AUTHOR-BOARD row 140 (LOW-NUMBER law). Row 140's story was replaced mid-flight by a concurrent lane (commit `644a89180`, Cameron's decision) while I was working — I caught it via `git log`/board, reverted my dead work, and pivoted.

- **What happened first (the Naaman detour, reverted):** the board still read row 140 = Naaman when I began. Its park was Cameron's story-rejection ("using somebody else's gospel to redo the same prodigal-son story"). I author-reframed Naaman's n5 moral off the prodigal "way back / come back again" onto humble obedience (re-voiced n5 in ElevenLabs, reframed b15/b16 images, rebuilt beats.json + windows, `--check` PASS). THEN discovered the board/QUEUE had been changed + committed to **cut Naaman entirely and replace row 140 with THE BRONZE SERPENT**. Cleanly `git checkout`-reverted all Naaman edits (archive restored byte-identical). One wasted ElevenLabs n5 segment (~$0.01); lesson logged to memory.
- **The real work — Bronze Serpent authored from scratch (Num 21:4-9 + John 3:14-15):** the OT event Jesus himself chose to explain his cross ("as Moses lifted up the serpent... even so must the Son of man be lifted up"). Distinct moral (look in faith to God's lifted-up provision and live) — not a prodigal repeat, not a Nicodemus dupe.
  - Wrote the full narration (14 segments + card): NARRATOR modern; people's KJV p1/p2 = SCRIPTURE; the LORD 21:8 = GOD/green (OT Jehovah, not red); Jesus John 3:14 = JESUS/red. Rendered all via **ElevenLabs** (real audio, engine-parity cast).
  - Built the V1 scaffold: cloned the Naaman V1 helper stack, wrote new `make_narration.py` + `build.py` BEATS; remapped `CANONICAL_BUILD_SLUGS` 140 naaman→bronze-serpent in **corpus.py + extract_beats.py**; `v2_prep_row 140` → beats.json (139.4 s timeline).
  - Authored `beats_v2.py` — **24-beat movie-coverage** map (look-and-live 3-frame sequence, camera-behind-backs wides, MOSES/BITTEN-MAN/WILDERNESS-CAMP/SERPENT-POLE locks). CARE: no God/Jesus figure (OT era, both HEARD only — LORD = formless sky-light, Jesus beats hold on the lifted serpent); serpents natural/no-gore; the bronze-serpent-pole is the cross-form anchor.
  - **Gates:** `v2_prompt.py --check` PASS (24 beats, zero WARN, after fixing 3 `glow` drift-word FAILs + 3 wide-geometry WARNs); `audio_audit --rows 140` clean (0 old-voice). Board → **AUTHORED + Ready ✅**, claim cleared. QC.md carries the COMPLAINT LEDGER + promote-first place instructions.
- **Runner handoff:** 2 NEW places promote-first (WILDERNESS-CAMP from b01, SERPENT-POLE from b17), then generate 24 stills, face/beard board, assemble from the V1 segment mp3s, ship. Reroll budget ≤3 (15% of 24).
- **Cost:** $0 image generation (author lane); ~$0.03 ElevenLabs (15 bronze-serpent segments + 1 reverted Naaman). Commit `92d1bc587`.
- **Next author:** no clean unclaimed NEEDS-BEATS row surfaced on the board (95/102/113 are mid-flight cfix/billing-parked). Next author session: re-scan AUTHOR-BOARD for the lowest NEEDS-BEATS/NEEDS-REBUILD with empty Claim+Ready.

## 2026-08-13 (cont. 97) — ROW 137 VERIFY-PASS ABORTED (correctly): row is APPROVED with a CURRENT hash → UNTOUCHABLE — nothing claimed, nothing re-cut, $0 — Machine A `Dev`, Opus VERIFY-PASS (unattended/headless)

A VERIFY-PASS was dispatched to full-cut-gate row 137 ("One As We Are One · John 17") before Cameron's eyes reached it. FIRST ACTION per the guardrail: read `.approvals.json` myself and compare row 137's `approvedHash` to the live card `data-hash` in `site/review.html` — BEFORE claiming anything.

- **Result: hashes MATCH → approval is CURRENT → UNTOUCHABLE.** `.approvals.json` row 137: `approved: true`, `approvedHash 0434cfa666244948c256f5dfb119c104550f4915`, approvedAt 2026-08-13T00:16:01Z, no open complaint. Live card `id="v137"` (realistic-v2): `data-hash="0434cfa666244948c256f5dfb119c104550f4915"`. Identical.
- **Exited immediately: claimed nothing, extracted no frames, changed no art, re-cut nothing.** An approved row is Cameron's release decision and no defect outranks it — this check exists to prevent the 3 AM 2026-08-12 re-cut of approved rows 1/122/129. The only write was a log-only note appended to `build-137-one-as-we-are-one/QC.md` documenting the abort. Existing FIX-WAVE notes (b05 cool-light hair sheen, b12 distant ambiguous dome) stay non-blocking and are NOT to be acted on while this approval stands.
- Commit `ea387d572`. $0, meter unmoved.

## 2026-08-13 (cont. 96) — ROW 147 C-FIX SHIPPED: "Joseph Forgives" character-consistency complaint VERIFIED fixed in realistic-V2 — FULL-CUT GATE 16/16 PASS, $0/0 rerolls, reviewer card answers Cameron — Machine A `Dev`, Opus runner (unattended/headless)

Complaint-first + low-number dispatched me to AUTHOR-BOARD row 147 (lowest waiting complained row). Cameron's complaint (COMPLAINTS.md, status "newer cut shipped — VERIFY fixed"): *"Joseph should be the same character and same look as before, different hair maybe but same face definition. We should have the story of Joseph and this story looking the same. Match the characters and redo this one if you must."* No timestamp → a global identity complaint tracing to every Joseph appearance.

- **PROMPT AUTOPSY = ALLOWED-then-FIXED.** The complaint was filed against the OLD cartoon `ASSEMBLY-C` cut (7 reused W1 stills, 2026-07-17) where Joseph's face drifted frame-to-frame with no single locked face. The realistic-V2 rebuild (16 native-2K stills + JOSEPH lock, shipped 2026-08-12) already replaced that with ONE canonical Joseph — which is why COMPLAINTS.md auto-marked it "newer cut shipped — VERIFY." Per that rule I VERIFIED the current live cut rather than re-cutting a fixed one.
- **FULL-CUT GATE (6b) — all 16 beats, from BOTH source stills (4×4 contact sheet + full-size s02/s03/s05/s08/s09/s13/s14/s15/s16) AND the RENDERED mp4 (ffmpeg extracts @ 7.7/22.3/48.6/71.8/80.4/87.7s + 3 caption frames) = PASS.** Joseph is one man in every frame: clean-shaven Hebrew-Egyptian vizier, dark curly hair, warm dark eyes, white-linen+gold-collar — matches `CAST-REF-V2/joseph.jpeg` (the 1:20 portrait IS the ref). Only age/expression change, never the face — satisfies "different hair maybe but same face definition." Ten brothers consistent; realistic-only (Law 14) PASS, zero cartoon/mixed; anatomy/hands clean; granary (s15) alive not "dead crowd"; no modern objects; captions bottom-band, Joseph's KJV (Gen 45:4 / 50:20) styled cream/blue in sync. No Jesus (OT row).
- **VERIFY-ONLY, $0, 0 Gemini rerolls.** The pictures are already on-model against the cast-ref; regenerating them would violate the COST LAW / "don't chase subtle drift" and risk NEW drift. mp4 unchanged (live bytes == local, 20,294,602 B). Meter unmoved.
- **Shipped:** reviewer card v147 now answers his complaint in his own words ("Joseph should be the same character… same face definition… match the characters" → one canonical Joseph, the 1:20 close-up is the reference, same man throughout; and the future "story of Joseph" video will be built to this same face). data-built→2026-08-13. Commit `ac375403d`. Firebase deployed + live-verified (card flag live, mp4 HTTP 200). **FACE-BOARD note in QC:** any future regen / the "story of Joseph" arc must attach `joseph.jpeg` as the image anchor (identity is currently text-locked; it held, but image-lock is the durable standard). Row still awaiting Cameron's approval (a complaint clears only on approval).

## 2026-08-13 (cont. 95) — ROW 95 C-FIX SHIPPED: "Thief on the Cross" crucifixion re-staging — Cameron's five staging demands ALL fixed, FULL-CUT GATE 11/11 PASS, reshipped touch-once — Machine A `Dev`, Opus runner (unattended/headless)

Complaint-first + low-number dispatched me to AUTHOR-BOARD row 95 (lowest waiting complained row). Cameron's complaint on the live cut `9059485916c1…`: "0:08 he should be staked to the cross… 0:18 they are not facing each other and Jesus should be on the cross also… all shirts off… all pinned to the cross… all in line parallel not across… Jesus has a crown of thorns… they all have plaques above their heads." Prior sessions did the PROMPT AUTOPSY (verdict CAUSED — the beats_v2 "merciful distance / clothed / chest-up / facing-across" law authored the wrong staging) and fully staged the fix (all 11 beats + HILL/MOCKER/THIEF locks rewritten to three parallel forward-facing crosses, all men stripped & affixed, crown of thorns on centre Jesus, titulus plaque above every head; `v2_prompt.py --check` PASS), but were billing-walled for ~16 passes.

- **Billing cleared today.** A prior session regen'd s01-s07 on the new staging (01:36-01:39) then died mid-build; s08-s11 were still the old clothed frames. This session **regen'd ONLY the 4 stale frames b08-b11** (reused the 7 fresh — COST LAW, no re-pull), then **1 reroll** (b10 titulus legibly read "…allah…" → neutral gibberish). Cost ≈ **$0.67**, **9% rerolls** (≤15% budget), meter $621.49→$622.16 — well under the $6.10/row average (this was a partial-resume, not a full build).
- **FULL-CUT GATE 6b on the rendered mp4 (every beat + 3 caption frames + card) = PASS:** all 11 frames shirtless + affixed to a parallel-row cross + titulus plaque above every head + Jesus centre with crown of thorns (face-locked, olive skin / dark wavy hair / full beard / green-hazel V2 eyes); geometry never swaps; captions 3-colour + RED paradise line lands on Jesus @52.5s (desync fix held); AUDIO REBUILD PASS `e5ba558a` byte-identical; closing card clean. FIX-WAVE (non-blocking, rows-94/96 precedent): warm light on b08/b10.
- **Shipped:** commit `e743c7f79454…`; card v95 data-machine-reason removed (back in Cameron's Unwatched queue), hash + ?v = ship commit, "what this cut changed" answers each of his five demands in his own words. Deployed to Firebase + live-verified.

## 2026-08-13 (cont. 94) — ROW 140 STORY REPLACED: "The Bronze Serpent" (Num 21:4-9 + John 3:14-15) per Cameron's external-AI gap review — wired into QUEUE + board + QC spec, author lane picks it up — Machine A `Dev`, process-engineer session

Cameron ran the 200-story gap prompt (cont. 93 handoff file) through another AI and pasted back its answer; top pick **The Bronze Serpent** — the OT event Jesus himself used to explain his cross (John 3:14). Verified against the full lineup: no serpent/Numbers-21/Passover-institution/David-spares-Saul story exists; #4 Nicodemus is the John 3 conversation, not the type it points to. His paste = the standing instruction to fill slot 140 with it.

- **QUEUE.md row 140:** REPLACED per the rows-133/134 purge pattern — Naaman ARCHIVED in build-140-naaman-washes, new story + moral + CARE line (real snakes, dread not gore; bronze serpent on the pole as the cross-foreshadow anchor; OT era, no Jesus in frame, nobody in cream). Alternates (Passover Lamb Ex 12, David Spares Saul 1 Sam 24) logged for future gap-fills only.
- **AUTHOR-BOARD row 140:** Build -> build-140-bronze-serpent, Stills 0, State NEEDS-REBUILD, AUTHOR SPEC note in Claim; full spec appended to build-140-naaman-washes/QC.md (the park-note path the author prompt reads).
- The $0 author lane picks it up on its own; after authoring it joins the build queue in low-number order. $0 spend this session.

---

