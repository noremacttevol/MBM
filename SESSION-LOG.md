## 2026-07-29 — V2 row 2 DELIVERED: build-02-prodigal, 24 stills (Machine A / `Dev`)

Commit: ccbcb9f1d. Resumed row 2 at step E per the ledger and took it to delivery.
**Video #2 is finished and sent to Cameron; awaiting his approval.**

- **API died on arrival.** `v2_gen_api.py` hit `RESOURCE_EXHAUSTED` — *"prepayment
  credits are depleted"* — on b20. That is Cameron's Google AI Studio billing, not
  something a session can fix, so the line moved to Flow at 2K (already the standing
  default in V2-NEXT-SESSION-PROMPT) rather than stalling. **18 of the 24 delivered
  frames are Flow 2K (an upscale of 768x1376); 6 are API-native 2K.** Cameron's call
  whether to refill and re-shoot for parity.
- **QC was brutal and correct: 13 of the 19 API stills REJECTED.** Every still was
  Read at full resolution. Four of the six defect families were traced to root causes
  in the prompt system, so the fixes went into the system, not the frames:
  1. **PHARISEES LOCK v2** — the lock said "never white, never cream, never pale" and
     the model dressed all three in white prayer shawls anyway, the biggest pale mass
     in frame, beside the one man allowed cream. Colours now stated positively and
     anchored to the wall behind them.
  2. **Camera position** — the beats said WHAT happened but never where the lens was,
     so the model defaulted to hero-shots facing the camera. **The father ran AWAY
     from his son in the icon shot of the whole parable**, and "Then he left" read as
     the son ARRIVING. Four beats now state camera and travel direction.
  3. **`char_refs` added to `v2_prompt.py`** — recurring cast is now locked by IMAGE,
     not just text. The elder son had come back as three visibly different men across
     s16/s17/s18. `flow_driver` already accepted repeated `--ref`; `v2_prompt` was
     never passing any. Fixed, and it held on every subsequent frame.
  4. **`ANTI_PANEL` now goes on EVERY prompt**, not just wide ones — it used to ride
     along with the wide-shot defense line, so tight shots had no panel protection,
     and s18 came back with a landscape pasted in above the wall.
  Plus per-frame: wardrobe drift on the younger son (his lock omits clothing on
  purpose, so the beats that forgot to state it drifted rust-red to brown — and he is
  now BAREFOOT until the shoes are given in v22, so the gift still means something),
  two CGI-style drifts, one frame rendered ROTATED 90 degrees, one with a solid BLACK
  BAND across the bottom third.
- **Five beats needed a second pass; all five came good.** Final: **24/24 accepted**
  after 43 generations.
- **Delivered:** 158.4 s, 19.9 MB, 1080x1920, verify-mp4 OK, no silence gap over
  2.5 s, no music bed, captions correct per frame-strip (white narrator, red for
  every exact-KJV line — Jesus is the one telling the parable — cream question card).
  MINISTRY-GATE PASS on all four. V1 verified untouched.
- **Coverage:** 24 pictures against V1's 10. Seeing him a great way off, the run, the
  scandal of the run and the embrace are four frames instead of one; the elder
  brother's arc gets eight.
- **PUSH SKIPPED** — rejected again, this box's known 12.7 GB backlog. Commits
  5b98f8597 and ccbcb9f1d are safe locally. **Other machines still cannot see
  `media-production-v2/` until that repair happens.**
- **Two laws worth promoting, both now paid for twice:** state the CAMERA and not just
  the action; and a negation is a suggestion while a stated positive is an instruction
  (third occurrence — row 1 setting lock, row 2 pharisees lock, row 2 CGI drift).
- **Next session:** `Read V2-NEXT-SESSION-PROMPT.md and execute it. Start now.` The
  ledger says row 2 is DONE, so the line resumes at row 3.

## 2026-07-28 — V2 PRODUCTION LINE OPEN: row 1 delivered at 2K (Machine A / `Dev`)

Commit: 5cd098dd9. Ran `V2-KICKOFF.md` from scratch. `media-production-v2/` did not
exist; it does now, and **video #1 is finished and sent to Cameron**.

- **Bootstrap.** Flow confirmed `logged_in`. Jesus V2 face: 3 candidates from a
  byte-identical identity sentence (only light/background varied) → **candidate-1
  locked** as `JESUS-V2-REF/jesus-v2-face.jpeg` — neutral light + neutral background
  are what a face-lock ref needs so the model copies the FACE, not a scene. **Cameron
  confirmed "1"** when shown all three. Three angle refs generated off the winner.
- **Two tooling gaps closed in `flow_driver.py`:** it had NO model selector — every
  generation silently rode whatever the project remembered, unlogged. Added
  `gen --model` (verifies the chip, aborts rather than spend on a lesser model) and a
  `models` diagnostic. Chip confirmed **Nano Banana Pro**; Flow's image output is
  768x1376 regardless of model.
- **`extract_beats.py`** parses a V1 build with `ast` instead of importing it, so V1
  stays read-only (build.py's own `spoken_of()` would have written into the V1 folder).
  It reproduced build-01's timeline to **109.0s vs the shipped mp4's 108.971s**.
- **`v2_prompt.py`** assembles STYLE-V2 / LOCK v4 / defense line / anti-panel from
  single definitions, so byte-identity is a property of the code, not a QC chore.
- **MONEY LAW REVERSED BY CAMERON MID-BUILD.** *"ignore the money law that was
  supposed to be removed because I already paid for it… there shouldn't be any
  limitations on the money. Make it how its supposed to be."* Written into
  FACTORY-ORDERS MONEY RULE #1 and propagated to V2-KICKOFF, PIPELINE-STATE,
  HERMES-HANDOFF, NEXT-SESSION-C. **This matters technically, not just financially:**
  Flow's 768x1376 is BELOW the 1080x1920 delivery size, so every Ken Burns move was
  upscaling — the exact thing the anti-shimmer law exists to prevent. That has been
  wrong since V1. `gemini-3-pro-image` at 2K = **1536x2752**, 4x the pixels, real
  supersample headroom, no ~20 gens/hr ceiling, and it never touches Cameron's screen.
  New `v2_gen_api.py` (deliberately NOT gen_stills.py, whose ANCHOR_TEXT/CHAR_TEXT
  tell the model to match a reference PAINTING — the style V2 retired).
- **Row 1 DONE.** 20 pictures vs V1's 11 on identical audio. V1's two STORY-COVERAGE
  misses fixed: `w28` — her only spoken line in all of Mark 5 — now has its own frame,
  and the hem-touch is separated from the pressing-through. Mark 5:27 obeyed: she
  reaches from BEHIND him in every approach shot. 109.0s / 19.8 MB, verify-mp4 OK,
  worst gap 1.58s, no music bed, captions correct per frame-strip. MINISTRY-GATE PASS.
- **Two defects caught at the LOCK, not the frame** — the reusable lesson:
  1. `CREAM-CROWD` — the crowd came back dressed in cream, so the one man allowed to
     wear cream did not read as different from anybody.
  2. `STRAY-JESUS` — the fix for #1 NAMED Jesus inside the SETTING lock, and the model
     duly painted him into b03, seven seconds before the narration introduces him.
  **Rule now written into the lock file itself: a setting lock describes the street and
  the villagers and must NEVER name a character, because naming one puts him in the
  frame.** The cream contrast belongs to JESUS LOCK v4's own "(only he wears cream)",
  which appears in exactly the shots he belongs in.
- **PUSH SKIPPED** (both attempts): `git push` rejected, branch behind origin — this
  box's known 12.7 GB backlog. All work is committed locally: be02f951a, ba8b6e93a,
  5cd098dd9. **The backlog still needs a separate repair before this machine can share.**
- **Cost measured:** $0.134/image → **$2.68 for row 1**; ~$536 for 200 videos at 20
  stills each, before rerolls. Generation ran ~2-3 min per 2K still.
- **Next session:** `Read V2-KICKOFF.md and continue.` Ledger says row 1 DONE, so the
  line resumes at row 2. Open question for Cameron: he has not yet approved video #1,
  and the Jesus face is still marked CANDIDATE pending that approval.

## 2026-07-23 (cont. 3) — UNIFY ORDER + fresh-chat handoff (Machine C)

Cameron issued the UNIFY ORDER (multi-session coordination): story source-of-truth =
`AUDITS/2026-07-20-repeat-audit.md` (dedup DONE) + `STORY-INTEGRITY-LAW.md` (rules);
STORY-LEDGER subordinate (2 calls retracted — another session committed that). NO more
dedup/story-hunting — the 200 is full & clean. Real work now = **ElevenLabs re-voice +
full re-approval of all 200** (trim the old-then-modern echo first, Rule 4), in parallel
with **pictures/Flow from complaints**, then a **character auto-finder** vs the cast rules.
Pronunciation respellings are DEAD (ElevenLabs owns it). Split by CLAIM (claim the QUEUE
row + push FIRST before touching a video). Pentecost (Acts 2) approved as next new story;
needs a slot = Cameron's pick. Wrote `media-production/FRESH-CHAT-KICKOFF-2026-07-23.md`
as the paste-and-go for the new low-context chat. All this session's work is pushed (0/0).

## 2026-07-23 (cont.) — PICTURE-REDO PASS: every picture complaint addressed (Machine C)

Flow driver is live on this box (`flow_driver.py check` = logged_in). Went through EVERY
picture complaint. The pattern: most "redo them all" complaints were ALREADY redone by
prior sessions and look good now — only a few had live defects.

- **REGENERATED + SHIPPED (Flow gen → Read-QC → rebuild → verify → push):**
  - #112 beatitudes s10 — giant Jesus → now in-scale among the crowd.
  - #157 marvellous-work s3 — oversized seated scribe → natural proportion.
  - #153 restitution s3 — awkward gesture/off-white → cleaner faces, earth tones.
  - #13 roof s7 — the judging scribes were in WHITE/CREAM (only-Jesus-cream violation)
    → regenerated in dark scholarly robes. (build.py final-encode is veryslow on a 331s
    video; ran the mux at preset slow to fit — 20.6MB. A temp SKIP_BUILT_SEGS guard was
    added to build.py then reverted.)
- **VERIFIED already-good (current stills fine; awaiting Cameron's APPROVAL, no regen):**
  #90 washing-feet (all clothed, no bare chest), #56 widow-of-nain (Jesus in-scale,
  consistent, kids fine), #107 john-baptist-doubt (John consistent across prison shots),
  #19 shore (Peter/disciples consistent blue-grey, Jesus cream), #113 where-art-thou
  (God embodied + consistent), #135 rainbow-covenant (family now balanced 4m/4f).
- **#181 morning-stars-sang — DONE (Cameron chose "ground it in Job"):** regenerated s1-s6
  as earthly painted skyscapes over ancient hills, with Job a small figure looking up at the
  singing stars (s3/s5); removed the modern NASA Earth-in-space and the flaming-earth. Rebuilt
  + shipped (18.8MB/85s).
- Untouched by design: #140 & #179 (doctrine/STOP); #63 Siloam / #173 live (borderline pron).

## 2026-07-23 — GIT RECONCILE (orphan lineage → healthy peer) + AUTO-FIX LOOP: 3 shipped, audit of the rest (Machine C)

Commit: (this commit). Ran AUTO-LOOP-KICKOFF.md (the auto-fix loop). First had to
un-block shipping from this box.

- **GIT: this box was an ORPHAN LINEAGE.** `git merge-base HEAD origin/main` = NO
  COMMON ANCESTOR — local `main` (1443 commits) and origin were unrelated histories
  (origin was rewritten, likely to get under GitHub's 1GB cap; this box kept
  committing on the dead lineage, which is why its pull "hung" and it "couldn't
  push"). Fixed non-destructively: `git pull --rebase origin main` actually
  replayed only 23 unique commits (git dropped the rest as already-upstream);
  SKIPPED the 2 old-caption-renderer commits (superseded by origin's Jost engine),
  resolved every code/build.py conflict to origin (`--ours`), kept my additive cast
  stills + CAST-REF + slash-commands/hooks. Net vs origin: +567/-30 (deletions only
  in archive/retired-builds). PUSHED clean (594a0632). This box is now a normal peer;
  normal pull-rebase+push works. The loop tools (admin/*.mjs|sh) need node, which is
  NOT installed here — so live-complaint refresh + firebase deploy happen on other
  machines; this box fixes + pushes, board deploys elsewhere.
- **SHIPPED (rebuilt + whisper-verified):** #109 findeth (was "fendeth" → measured
  respell "fyndith" = FIND-eth); #50 Cana (was "Canoe" — the respell "kaynuh" was
  the CAUSE; removed it, plain word = KAY-nuh); #52 demoniac-synagogue ("Six words."
  → "just a few short words", drops the wrong count).
- **AUDITED already-fixed (current cut is correct; awaiting Cameron's APPROVAL to
  clear — do NOT rebuild):** #46 putteth, #57 lieth, #62 "Mark records"(verb),
  #67 Elias, #83/#86 tail-timing (~1.9s, not 13s), #108 calleth, #146 abideth,
  #150/#171/#184 caption colour (scripture renders BLUE, only Jesus red — frame-
  confirmed on #150 Psalm 23), #188 maketh. Machine A's prior entry also already
  fixed #119 bows→"boughs", #135 family, #113 God-embodied.
- **STILL OPEN — need a Flow session (pictures, credits, Cameron's screen; kept for
  a fresh low-context session so a browser burst can't wedge on a context limit):**
  #13 pharisees pic, #19 Peter/boat "redo them all", #56 low-grade/size drift,
  #90, #107 John face-lock, #112/#157 giant Jesus, #153 weird pic, #181 pics-dont-fit.
- **DOCTRINE / STOP (left for Cameron):** #140 duplicate prodigal, #179 Stephen
  Father+Son vision. Borderline pron left: #63 Siloam, #173 live.

## 2026-07-21 (night) — COMPLAINT BURN-DOWN: all 32 rows proven, 15 rebuilt, #140 Naaman BUILT (Machine A)

Commit: (this commit). Verify-first pass over every COMPLAINTS.md row in number
order. Every row now has proof-before AND proof-after (whisper word-isolation,
acoustic vowel tests against same-voice references, or extracted frames) in
FIXNOTES.json / the per-video ship notes. #17 stayed DEFERRED per Cameron.

- REBUILT+SHIPPED: #8 calleth(kawleth), #9 run-toward-Jesus still (prior "fix"
  was still wrong), #10 (finished a dead session's corrupt-mp4 windlass fix; a
  second session later closed the seg-cache hole), #18 emmaus short-hair s6,
  #19 shore story-coverage (9 beat stills wired: call/"it is the Lord"/leap/
  swim/fire/breakfast), #65 (captions verified + cleaner take), #108 calleth+
  leadeth(was "letteth"), #113 God EMBODIED from locked sheet (dead "formless
  light" law reversed in PROMPTS.md), #119 bows(boughs — acoustic proof),
  #135 family now 4m/4f + split-panel ark repainted, #149 liveth round 2
  (livith; Cameron rejected livveth same-day), #150 maketh round 2 (maykith,
  shared dict upgraded — scripture voice), #153 half-buried crowd repainted,
  #157 giant scholar rescaled, #181 Job himself added to the Job beats,
  #189 overcometh(overcummeth), #179 vision = TWO embodied personages.
- #140 NAAMAN WASHES BUILT: sheet unblocked -> 7 character stills generated
  (+1 upright re-roll), assembled, gated, shipped. QUEUE ticked.
- VERIFIED-ALREADY-FIXED (proof notes on the board, no rebuild): #7, #22, #67,
  #83, #86, #90, #107, #109, #112, #146, #171, #184, #188.
- Tooling this session: whisper word-isolation proofs (small.en), an acoustic
  homograph vowel test (scipy spectral envelope vs same-voice reference words
  — settled bow/liveth/maketh arguments whisper can't hear), flow_driver refs
  for character-locked regens.
- OPEN QUESTION for Cameron: #10's original 3 complaints were overwritten on
  the board before anyone saved them — the cut was swept against every defect
  class instead. If one of the 3 was something else, one more complaint with
  the word pins it.

## 2026-07-21 — CHARACTER SHEETS APPROVED + WIRED INTO THE PIPELINE (Machine A)

Commit: (this commit). Cameron approved the whole roster ("okay characters are all
good"). All 63 sheets are now LOCKED refs alongside JESUS-MASTER-REF.

- Approval stamped in all 63 CHARACTERS/*/SPEC.md (status 🔒 LOCKED, approved
  2026-07-21) and across the CHARACTER-LAW.md status board.
- **CHARACTERS/character_refs.py** — the one place a build asks what a person
  looks like: `refs(name)` returns the 3 locked jpegs to pass as --ref,
  `lock_text(name)` returns the exact paragraph to paste, `find_in_text()` says
  who a build shows. Alias-aware (Simon Peter, the Baptist, Heavenly Father);
  ignores scripture citations ("Matt 9:9", "daniel-3_slug") and common-word
  names ("the biggest job of his life" is not Job). REFS.json = the manifest.
- **character_ref_gate.py** — mechanical gate in the shape of jesus_face_gate:
  a rostered name in PROMPTS.md with no lock text FAILS before any Flow credit;
  mentioned-but-not-painted names clear with `CHARACTER-REF-EXEMPT: <name>`.
  Wired into FLOW-BUILD-PLAYBOOK step 3-4, PRODUCTION-BIBLE's gate banner, and
  CREW-GUIDE.
- **AUDITS/CHARACTER-REF-RETROFIT.md** — 87 shipped builds show rostered
  characters; 45 already carry lock text, 42 predate the law and are listed for
  retrofit (their shipped videos are fine — the rule binds the next re-roll).
  Peter (19 builds) and John (16) are the highest-leverage fixes.
- Board republished as LOCKED: https://milk-b4-meat.web.app/characters.html
  (Firebase 429 → prune_hosting_versions.py, then deploy at concurrency 4).
- **#137 / #140 / #179 are UNBLOCKED** (WANTED.md closed out).

## 2026-07-21 (later) — TIMING/HEALTH SWEEP ROUND 2: re-render batch checked, 2 fixes, source hardened

Commit: (this commit). Audit: media-production/AUDITS/TIMING-HEALTH-SWEEP-2026-07-21.md

- The narration re-render batch rebuilt **144 of the 200** videos after round 1,
  invalidating those measurements and UNDOING the #70 size fix. Re-measured all 144.
- Only 2 failed, both fixed + shipped + on origin (ship-fixes run by hand):
  **#70** back to 28.5MB (build.py budgets 29.0MB, not 25 — it obeyed its own rule)
  -> re-encoded to 23.5MB; **#149** at -19.2 LUFS (the gain clamp min(10.0,...)
  cannot reach -15 from a -29 LUFS raw mix) -> re-normalized to -14.5.
- **Fixed at SOURCE so re-renders cannot undo it again (466f9f5f):** 102 build.py
  size budgets 29.0/29.5MB -> 24.0 (for 101 it is only a peak cap = no quality
  change; #70 alone used it as a hard 2-pass target); 201 build.py gain clamps
  +10/+12dB -> +16dB. Earlier today: 13 CARD_HOLD constants -> 2.0s.
- **FINAL: 199 measured, 196 clean.** All pass verify-mp4, all under 25MB, all
  -14.0..-16.0 LUFS, all local bytes = origin. The only 3 failures are
  approved-locked and untouched: #142 (12.8s), #143 (9.0s), #145 (9.6s) dead air —
  their build.py is already fixed, so a re-render clears them.
- Open: cron stopped firing after 10:33 (entry intact, lock free) — round-2 ships
  were manual; verify-mp4.sh still has no size gate; build-137-stephen-sees-him-
  standing is a purged dupe dir that still holds an mp4 and should be archived.

