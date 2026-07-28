## 2026-07-28 — STILL-QC: found the ROOT CAUSE of the "same face / grey Peter / vanishing beard" complaints (Machine C)

Cameron ("you know what i want right?") — picture complaints, plain-language session.
Read the 67 open complaints live off review.html via the paired browser; 25 are picture
ones, and they say three things over and over: clone disciples (#90/#91/#103/#107),
beards + hair changing between shots (#102/#62/#32/#92), and somebody drawn as a giant
(#69/#112/#157/#56).

**The root cause, and it was not the image model.** Every build's PROMPTS.md carries its
OWN inline `[X LOCK] = ...` copy of a character's description, and those copies drifted
away from the approved sheet in `CHARACTERS/REFS.json`. build-90 contained BOTH at once —
its DISCIPLES LOCK said "PETER ~35 ... blue-grey" while its PETER LOCK said "of about
fifty ... streaked with grey ... rust-brown" — and the picture obeyed the wrong one. The
art was correctly following bad instructions.

- **NEW `media-production/character_drift_qc.py`** — the beard QC Cameron asked for in
  #102, generalised: compares every inline lock against the approved sheet and fails on a
  contradiction in AGE / GREY-HAIR / BEARD / GARMENT colour. Swept 203 builds → 4 real
  contradictions (Peter, in build-90 + build-197). Now exits 0.
  Killed three false-positive classes while building it, because a QC that cries wolf is
  worse than none: fuzzy name matching checked the Two Sons parable's vineyard FATHER
  against the GOD THE FATHER sheet, Joseph of EGYPT (#147) against Joseph of NAZARETH, and
  John the BAPTIST (#69) against John the Beloved → exact-slug only, bare first names never
  resolve; "never bearded" in Pilate's sheet read as an assertion → negation-stripping;
  young Jeremiah at his call (Jer 1:6) → explicit waiver with a scripture reason.
- **#90/#92/#103** build-90 + build-197 PETER LOCK rewritten to the sheet; repainted
  s4-peter-protests and s4-peter-stands with the peter refs attached. QC'd by eye against
  face-front.jpeg — both are now the same dark-bearded man in his thirties in the blue-grey
  tunic. Commit c912cf89.
- **#112** "last picture Jesus was a giant" = `s10-the-upside-down-kingdom`. Its prompt
  already had a long anti-giant paragraph and still lost, because the shot attached NO ref
  ("prompt-driven"). Attached the master face + put him IN the group, people on both sides,
  heads on one line. The first repaint then landed the sunset directly behind his head and
  gave him a glowing outline — caught by eye, no gate can see it — so the sun was pinned
  low and off to one side. Second repaint clean. Also enforced only-Jesus-wears-cream (a
  woman had a cream shawl). Commit after c912cf89.
- **#135** VERIFIED already correct (counted 4 men + 4 women, no children) — but its prompt
  said BOTH "No people are in the frame" AND "EIGHT GROWN ADULTS", and the abandoned
  `s1-the-ark-at-rest-v2.jpeg` is what that contradiction produces (empty hillside). Removed
  the contradiction and enumerated the eight positionally so it cannot regress.

**Deliberately did NOT rebuild any video.** A REDO-ALL sweep was running live on another
machine all through this session (at #72, 01:07). It re-renders every build, so these
stills reach the movies without two machines fighting over the same 250MB mp4. Checked the
whole backlog first: 32 fixed stills across 18 builds are painted-but-not-yet-rendered, and
every one of those builds is still pending REDO, so the sweep picks them all up. A separate
33 stills across 23 builds are new coverage art not yet wired into build.py — assembly's job.

Known/left open: build-90's character gate FAILS pre-existingly (verified against HEAD) —
its twelve disciples have no individual lock text or refs, which is the remaining half of
complaint #90. Old complaint timestamps ("2:11", "42") no longer map to the videos because
the voice/pacing rework moved every timing — identify shots by looking, not by seeking.
Commits: c912cf89 + the two that follow it.

## 2026-07-24 (cont.) — #3 STILL-MAKER: started the COVERAGE-STILLS marathon (15 painted) (Machine C)

Cameron pointed me at the narration session's per-story audit — `SPEAKER-LAW/stills-needed.json`,
728 beats where the improved narration leaves one picture frozen too long (293 "high", >25s).
Per `STORY-COVERAGE-LAW.md` I paint the missing moments, add each as a shot in the build's
PROMPTS.md, generate to a named slug, gate, and record slug+`done` in the JSON (assembly wires
build.py). Painting a new file never collides with other sessions.

- **15 new coverage stills painted, gated, pushed** across 7 builds: 120-Job (4: blessed-be-the-name,
  my-redeemer-liveth, pleiades-and-orion, hand-upon-my-mouth), 118-Jonah (3), 148-Ruth (3),
  65-help-mine-unbelief (2, Jesus-present, no halo), 117-Hosea (1), 70-temptations (1), 05-bent-woman (1).
- **Anti-duplication discipline** (the key lesson): checked existing art by eye on every build and
  marked ~11 flagged beats `covered_by` an existing still instead of repainting (build-03 both,
  118 s1/s5/s10, 117 s6/s8, 70 s7/s9). Never repaint what's already there.
- Wrote `media-production/KICKOFF-COVERAGE-STILLS.md` (workflow, gotchas, deferred theophany builds)
  so the marathon resumes seamlessly in a fresh chat from the JSON's `done` flags. ~710 entries remain.
- Gotchas logged: jesus gate bans `halo`/`rim-light` + JESUS_WORD in slugs; `--chars` only for
  characters with a CHARACTERS sheet; deferred build-119-fourth-man / build-105-face-to-face
  (Christ-figure depiction = Cameron's call). Commits fb545fd8…6976b7b6.

## 2026-07-24 — #3 STILL-MAKER: cleared 9 picture complaints (Machine C)

Read live complaints from the review board via the paired browser (git board is stale on
this box). Fixed and pushed every open picture complaint, QC'ing each jpeg BY EYE (the gates
can't see scale/duplicate/wrong-people/beard/grey drift):

- **#83** weeping-over-jerusalem — VERIFIED already correct (walk toward Jerusalem; Jesus normal scale).
- **#13** roof — s10's four celebrating friends now match the distinct carriers (black-beard / young-clean-shaven / grey-older / ginger-round); s3 mat-man young again (was grey). Sharpened the prose so it won't re-drift.
- **#56** widow-of-nain — s6 giant Jesus → normal human scale; s8 halo/glow behind his head removed; son consistent.
- **#99** flesh-and-bone-thomas — Thomas realigned to the canonical cast (wavy dark hair, not a black bowl-cut; full beard; brown eyes); regen s5/s6/s7 + fixed the LOCK prose.
- **#153** restitution — the weird 1:12 shot (s3-cool-refreshing, hand-on-chest) replaced by the clean v3.
- **#181** morning-stars-sang (Job 38) — cosmic beats had drifted terrestrial + a lone man; regen s1/s2/s3/s5/s6 as true outer-space creation, incl. the "sons of God" as ABSTRACT aurora light (not humanoid figures).
- **#71** great-commission — cast verified consistent; s2 sunset-glow behind Jesus's head removed.
- **#107** — VERIFIED (messengers distinct, John/Jesus normal scale). No regen.
- **#161** called-of-god — Aaron still salt-and-pepper grey at the anointing → regen s6 dark-haired, oil on bare head.

Visual-QC swept the highest-risk prior fixes (#90 washing-feet, #103 peters-confession): disciples
distinct, Peter dark, Jesus on-model — both hold. Every build committed + pushed separately; gates
green. Tool note: `regen_shot.py --out` defaults to `assets/<slug>.jpeg`, so a slug with an em-dash
(build-71 s2) saves to a mismatched filename — move it into place after. Commit: 0d8aefa8 (#161) + the
per-build commits above; final tracker/log commit follows.

## 2026-07-23 (cont. 7) — PLANNER echo sweep to ZERO (232→0 narrator repeats) (Machine C)

Cameron's order (ORDER-FOR-AGENT-1-ECHO-TRIM.md + ECHO-SWEEP-FOR-AGENT-1.md + echo_scan.py):
drive narrator-echo repeats to `TOTAL echo pairs: 0`. Those three files did NOT exist in the
repo or on origin (never pushed by whatever session was to make them) — so I built
`echo_scan.py` to the exact stated contract and did the work. echo_scan reads each build's
make_narration.py SEGMENTS and flags a NARRATOR sentence that restates an adjacent verbatim
character/scripture line (with a proper-noun guard so new info is never cut). `echo_trim.py`
shares that exact detection, so driving the scanner to 0 is real, not gamed.

- Baseline after cont.5's 105 trims: 60 echo sentences across 52 builds (the order's 232/125
  was the pre-cont.5 count).
- Applied: 49 sentence-trims + 8 whole-segment deletes (pure restatements the KJV line still
  carries) + #139 (old-format) hand-REWRITTEN to keep its "not to show off" teaching without
  re-quoting Matt 5:16. Two passes (deleting a beat re-exposes a neighbor's echo).
- Verified riskiest edits read BETTER: #25 wheat-and-tares now opens on the scripture intro →
  Jesus's parable → narrator (the deleted n1 was pre-echoing Jesus); #176 keeps Psalm 24's
  call-and-response in the scripture voice. All 52 changed files parse.
- `.eleven-done`/`.audio-eleven-done` dropped on every edited build so #2 re-voices them (none
  existed yet, so they were already in the re-voice state). Transcripts re-exported.
- **`python3 media-production/echo_scan.py` → TOTAL echo pairs: 0.** Commit 880c0481.

Touched only SEGMENTS narration text — no pictures/audio/captions. Rebased over #3's stills
commit aadf2eab; synced 0/0.

## 2026-07-23 (cont. 6) — PLANNER story-dup audit: 2 real double-tellings found + fixed (Machine C)

Cameron asked point-blank: "no double storytelling from differing disciples?" Honest answer:
the earlier pass was FOLDER-dedup, not a story audit — so I ran a real content-level one
(`story_dup_audit.py`, TF-cosine over all 200 transcripts + shared-chapter grouping →
`TRANSCRIPTS/STORY-DUP-AUDIT.md`). Found and CONFIRMED two genuine double-tellings the
2026-07-20 audit missed:
- **#44 two-debtors == #74 woman-washed-his-feet** — one Luke 7 scene (Simon's dinner);
  both narrations open identically and #74 already tells the two-debtors parable in full.
  #44 was POSTED. Cameron: "do what Jesus would want." → keep the fuller #74 as the Luke 7
  keeper; retire #44; reuse slot #44 for **Pentecost (Acts 2)** (his approved new story).
- **#128 == #156 Amos "famine of hearing"** — same story; #128's build folder still had
  the Amos narration though its row was swapped to Mark 7 on paper (never re-narrated,
  Built ⬜). → #156 keeps Amos; #128 rewritten to its true Mark 7 "their heart is far
  from me."

Delivered as Planner: full narration + storyboard DRAFTS (`DRAFTS/row-044-pentecost.md`,
`DRAFTS/row-128-heart-far-from-me.md`), QUEUE rows 44/74/128 updated (incl. ⚠️ for #4 to
pull the still-posted two-debtors and submit #74). New **STORY-INTEGRITY-LAW Rule 5**
(Cameron): be honest about differing gospel witnesses ONLY where it enriches, NEVER where
it invites doubt or degrades the sacred story. Candidate cluster (John 14 #133/#145/#185,
Sermon-light #121/#139, John 10 #134/#159/#108) still needs the distinct-vs-merge judgment
pass. Commit 97dab2a0. (Build/audio/stills for the two swaps belong to #2/#3/#4.)

## 2026-07-23 (cont. 5) — ROLE CORRECTED to #1 PLANNER: transcripts + dedup + Rule-4 trims (Machine C)

Cameron clarified the 4-session split: **#1 = Video Planner (THIS session)** — check what
Jesus would want, write the transcripts + plans, keep the library non-duplicated, QC vs
the others; **#2 = audio maker** (transcripts → ElevenLabs → new audio); **#3 = still
maker** (fix picture complaints to the rules); **#4 = captions + organize + submit +
reviewer health**. The ElevenLabs adapter I built in cont.4 is NOT my lane — it's handed
to #2 (annotated atop `ELEVENLABS-SETUP.md`; scaffold is fine and ready for them). This
session's real work, all pushed:

- **`export_transcripts.py` → `TRANSCRIPTS/`** — 200 clean, speaker-tagged transcripts,
  one per row (`{id,speaker,text}` JSON for #2 + human `.txt` + INDEX). AST-parsed from
  each build's make_narration.py (no side effects), handles new & old SEGMENTS formats.
- **Folder dedup** — found 5 rows with duplicate build folders (65, 67, 71, 137, 140:
  stale/archived old builds beside the current). Canonical chosen by QUEUE story title
  (so an archived build's leftover mp4 can't win); `TRANSCRIPTS/DUPLICATES.md` lists them.
- **Rule-4 trim** — `rule4_scan.py` flagged 221 narrator beats echoing an adjacent KJV
  verse. `rule4_trim.py` (sentence-level: drop the restatement, KEEP teaching, never empty
  a beat, keep new-proper-noun sentences) applied **105 trims across 79 videos**; re-scan
  221→131. Verified via git diff on sensitive builds (Job 19:25/38:4/38:7, Luke 22:18/
  23:46 echoes cleanly removed, narration still flows). All 79 files parse OK.
- **`TRANSCRIPT-LANE.md`** — claim + the 4-role division on the record; source of truth =
  make_narration.py, TRANSCRIPTS/ is the exported handoff.

NEXT for #1: the remaining **131 wholly-overlapping beats** (`TRIM-CANDIDATES.md`) need
manual rewrite (rephrase, not delete); then the story/Jesus-alignment QC pass and slotting
Pentecost (Acts 2). #2 reads `TRANSCRIPTS/*.json` when ready. Commits: d227962a (export +
tools + dedup), afaeab1f (105 trims applied).

## 2026-07-23 (cont. 4) — ELEVENLABS VOICE PATH built — SUPERSEDED, handed to #2 (Machine C)

Fresh chat off `FRESH-CHAT-KICKOFF-2026-07-23.md`. Chain verified (top entry af0cf734
present). Claimed the **ElevenLabs re-voice-setup lane** (priority #1) and pushed the
claim first (`01617b50`). Both headline lanes have a real gate: the picture/Flow lane is
character-sheet-blocked for every open picture complaint (#19/#56/#90/#113/#135/#153/#157
all on the block list), and the re-voice lane's ONLY blocker is Cameron's ElevenLabs key +
voice pick. So I built the entire drop-in ElevenLabs path up to that line:

- **`mbm_eleven.py`** — dependency-free (stdlib `urllib`) client for
  `/v1/text-to-speech/{voice}/with-timestamps`. Reproduces the exact per-sentence
  `timing.json` contract (`{text,start,end}` segment-local secs) from ElevenLabs char
  alignment — unit-tested on synthetic alignment (split + monotonic timing PASS).
  English-only model enforced (Voice Law bans Multilingual). Optional pronunciation
  dictionary built from a config lexicon (IPA), created once + locator cached.
- **`eleven_config.json`** — the single file Cameron edits: `api_key`, 5 speaker voice
  ids, model, seeded IPA lexicon for the archaic KJV words he's flagged (liveth, Esaias,
  Siloam, Elias, findeth, calleth, leadeth, abideth, maketh, putteth, lieth, overcometh,
  Cana, livest). Placeholders → treated as unset. Single-source (found via parent-dir
  lookup) so the key is never copied 204×.
- **`mbm_caption_timing.save_narration`** patched — routes to ElevenLabs when configured,
  else edge-tts fallback (nothing breaks today). A real ElevenLabs error aborts LOUD —
  never silently ships edge audio pretending it re-voiced.
- **`revoice_sweep.py`** — claim-aware: regen audio → `qc_narration.py` whisper ear-check
  → optional `build.py` mp4 rebuild. No-ops with a clear readiness report when no key.
  Syncs engine modules into each build just-in-time (no 200-file pre-commit).
- **`redistribute_modules.py`** (scoped to the 2 changed modules only — does NOT resync
  pronounce/speakers) + **`ELEVENLABS-SETUP.md`** handoff.

All pushed (`01617b50` claim, `e0282207` code). **BLOCKER for Cameron:** drop his
ElevenLabs API key (env `ELEVENLABS_API_KEY` preferred, or config) + pick a voice per
speaker (jesus must sound American), then `python3 revoice_sweep.py --rows 5 --build` to
test one. The 200-video re-voice sweep runs the moment those are in. Pictures/Flow lane +
character-sheet session are still open for another machine; #171 (scripture captions →
blue) is the one open picture complaint needing NO character sheet and NO key.

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

