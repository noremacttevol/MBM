## 2026-08-13 (Opus runner, unattended/headless) — Row 177 MAKE ME A SANCTUARY V2 FIRST CUT SHIPPED: 19 realistic beats, 0 rerolls, "Not real new voice" fixed at source — Machine A `Dev`, ~$2.81 Gemini

Ran AUTHOR-BOARD row 177 (lowest Ready ✅, THE LOW-NUMBER LAW). Cross-checked QUEUE.md first: row 177 = "Make me a sanctuary" (Ex 25:8), NOT a swapped/replaced story — legit build. Session-chain verified: prior top entry row 147 joseph-forgives C-FIX, commit `64f67520a449` present in git log.

- **Audio-fix verified real before spending:** the one OPEN complaint (`v2_outline.py 177`) was "Not real new voice." Author fixed at source — all 13 segment mp3s ffprobe as ElevenLabs 44100/128k and `AUDIO_FROM_V1_SEGMENTS=True`. Confirmed, then built. AUDIO REBUILD PASS SHA256 `23fba3a1`, 96.0s, decode-clean.
- **MOSES face-lock wired by runner:** `v2_story_cast.py` generated MOSES + TABERNACLE-HOLY portraits but skipped writing REFS (its `"\nREFS = {" not in src` guard tripped on the author's empty `REFS = {}`). MOSES spans b02/b04/b07 (≥3 legible-face beats) + QC requires a MOSES face-board → text-only WOULD flip (rows 52/55). Wired `REFS={"MOSES":"CAST-REF-V2/moses.jpeg"}`; gen log confirmed `[+1 char ref: MOSES]`; face held b02/b04. TABERNACLE-HOLY left a PLACE (promoted from b07), never wired as a character.
- **Places:** promoted WILDERNESS-CAMP←s01 (12 beats), TABERNACLE-HOLY←s07 (6 beats); SINAI-MOUNT single-beat, no promote. Anchors QC'd first + hardest.
- **0 rerolls (0%)** — all 19 first-attempt frames passed Light QC. ~$2.81 total (2 portraits + 19 beats), meter $651.24→$654.19. Far under the $6.10/row average and the 15% reroll budget — COST LAW trend holds down.
- **FULL-CUT GATE (§6b) in the RENDERED mp4:** 19/19 beats + 3 caption frames + question card PASS. HARD GATE GOD-NEVER-EMBODIED — b03 formless cloud over the tent, b08/b09/b11 ark + two carved-gold cherubim statues + soft light in the EMPTY space above the mercy seat (no figure), b18 "would take a face" = tent-only NO Jesus. Cherubim = gold statues throughout. MOSES consistent. No cream, no modern objects, realistic, anatomy/scale/hands clean, all upright (no rotation). Captions bottom-band GREEN (God s1/g22) / WHITE (narrator); card clean verse-only.
- **Ship:** commit `97f2afbd7721` (mp4 force-added + 19 assets + MOSES/place plates + QC.md ledger + beats_v2 MOSES REFS + boards + QUEUE). Reviewer card v177 repointed (data-hash `97f2afbd7721`, data-review-wave realistic-v2, ?v=97f2afbd7721, flag tells Cameron the voice is the real new voice + God-never-shown). Deployed to Firebase + live-verified. AUTHOR-BOARD BUILT, QUEUE V2 SHIPPED. Appr stays ⬜ (Cameron's alone).

Commit: 97f2afbd7721da27d7f24884d6987c2653d06a45 (ship)

---

## 2026-08-13 (Fable-5 AUTHOR lane, low-number, unattended/headless) — Row 153 restitution: Peter off-model root-caused & AUTHOR-FIXED; handed to RUNNER (AUTHORED+Ready), complaint stays OPEN until the regenerated cut ships — Machine A `Dev`, $0

**Commit:** author fix `ca2daf876` (beats 9 PETER locks + b02 prose + QC + plates), handoff `5933b1988` (board AUTHORED+Ready, 9 off-model stills deleted, QC correction). HEAD==origin==5933b1988.

Ran AUTHOR-BOARD lowest-open row = 153 (the NEEDS-REBUILD park from the prior session). Board now has ZERO NEEDS-BEATS/NEEDS-REBUILD rows — 153 was the last author-actionable one.

- **Root cause corrected (the park note was partly wrong).** Peter — the protagonist — rendered as an older grey man because **PETER was in no beat\'s `locks`**. The park note said "add PETER lock + set `ref:True`". Verified in code that **`ref` is the JESUS face lock ONLY** (`face_b64 = b64_file(JESUS_REF)`, attached iff `beat.get("ref")`; `check()` ties ref to `jesus:True`) — setting `ref:True` on a Peter-only Acts beat would inject **Jesus\'s face** into a scene with no Jesus. The real, single fix: add `"PETER"` to `locks` → `GLOBAL_CAST["PETER"]="peter"` auto-attaches `peter-front/quarter.jpeg` (3.2 MB each, on disk) AND `CAST_LOCKS["PETER"]` injects the canonical lock text (mid-30s, dark curly hair, dark beard, BLUE-GREY tunic). `ref` stays False. Proven by peer build-103 b04 (PETER in locks, `ref:False, jesus:False`, renders correctly).
- **Fix applied to the 9 REAL Peter beats** (b02,b03,b04,b05,b06,b07,b12,b13,b15). **b18 EXCLUDED** — the park note wrongly listed it; b18 is scrolls-only ("No people needed in this frame"), no Peter figure. Softened b02\'s "weathered face…remade" aging prose (deferred to the sheet). `v2_prompt --check` PASS; assembled b02 now carries `PETER LOCK`/`mid-thirties`/`BLUE-GREY`, no `remade`.
- **Handoff corrected mid-session (caught a stranding trap).** First flipped State→BUILT for the cfix lane — but `autopilot.sh` cfix fires only when `cur.get(row) is not None` (a LIVE published hash) and row 153 was never published, so BUILT strands it forever (the "cfix hash-gate strands rebuilds" class; cf. row-140). Correct route = **AUTHORED + Audio OK + Claim empty + Ready ✅** → RUNNER PASS 2 picks it, complaint-first (153 is in openc). Because the runner skips existing stills >50 KB, **deleted the 9 off-model Peter stills** so only those regenerate; 16 good frames + b18 kept (touch-once; parked $3.48 carries, ~$1.2 to regen 9). Cleared the stale `cool-runner-153` cooldown so the runner takes it next tick.
- **$0 this session** (author lane; no image generation). Complaint **"1:12 is weird picture — needs Peter" stays OPEN** — closes only when the runner regenerates the 9 (FULL-CUT-gating Peter vs peter-front + verifying b13 shows Peter @~1:12), ships, and Cameron approves.

**LESSON (for the rubric/next author):** a cast member\'s identity drift is fixed by adding their TOKEN to `locks` (auto-attaches sheet + lock text), NEVER by `ref:True` (that is Jesus-face-only and would inject Jesus). And an UNPUBLISHED NEEDS-REBUILD row is finished by the RUNNER via AUTHORED+Ready, not by cfix via BUILT (cfix needs a live hash).

---

