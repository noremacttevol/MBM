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

