# FACTORY ORDERS — the single source of truth for the MBM video factory

> 🛑 **ANTI-SPIN ORDER (2026-07-15, amended): the JESUS-MASTER-REF bootstrap
> belongs to the FIRST machine whose browser preflight passes on the FIRST try —
> generate the portrait per the face law, save as JESUS-MASTER-REF/jesus-face.jpeg,
> push, then continue your range. If your preflight does NOT pass first try, the
> face is not your job — skip it.** If JESUS-MASTER-REF/
> is empty: do non-Jesus prep only (narration scripts, PROMPTS.md, non-Jesus
> stills), or say "SESSION DONE" and stop. NEVER retry browsers/extensions more
> than twice for ANY task — two failures = note it in one line and move to work
> that needs no browser. Wheel-spinning burns Cameron's Claude credits; a stopped
> session is cheaper than a spinning one.

> Written 2026-07-14. Every Claude Code session on every computer reads THIS file
> after pulling the latest repo, then does its job with no further questions.
> This supersedes any older ad-hoc kickoff prompt. If anything elsewhere conflicts
> with this file, this file wins.

---

## MONEY RULE #1 — corrected by Cameron, 2026-07-15

**BANNED (real extra dollars):** the paid Gemini image API — never run gen_stills.py,
never call the API. That bills Cameron's card on top of what he already pays.

**FREE TO USE (already paid for):** Cameron's Flow ULTRA plan credits — 25,000/month,
and they EXPIRE monthly. Spending them costs nothing extra; letting them rot wastes
money already spent. So in Flow:
- Nano Banana 2 (0 credits) is the default for ordinary stills.
- SPEND CREDITS FREELY whenever they buy quality or fewer rerolls — Nano Banana Pro /
  higher tiers for the master face, Jesus close-ups, complex crowd scenes, or any shot
  that keeps failing on the free model. A 5-credit still that lands first try beats
  five free rerolls.
- Sanity ceiling so one machine can't drain the month: keep a video's credit spend
  roughly under 150 credits; note total credits used in the row's Claim column.

(The local/free tools remain required: jesus_face_gate.py, make_narration.py,
build.py, gen_site_index.py, flow_driver.py.)

## ✅ THE-200 v2 IS LIVE (approved by Cameron 2026-07-15). ALL MACHINES GO.

The catalog is now three shelves: rows 1–100 EVERYONE · 101–150 BRIDGE · 151–200
MEMBER (see THE-200.md). QUEUE.md is regenerated to match. All holds are lifted.

**Migration notes (one-time):**
- Old row 84 (Calling the Fishermen, built) is now row 71 — folder renamed.
- Old row 85 (Calling Matthew) is now row 72 — Machine B: finish your in-flight
  build and tick ROW 72; name the folder build-72-calling-matthew.
- Old row 124 (Gethsemane, REJECTED — hair changes length in one scene) is now
  row 91 — folder renamed build-91-gethsemane. Fix the one scene, rebuild, tick 91.
- Old row 164 (Rainbow covenant) is now row 135 — Machine D: finish your in-flight
  build and tick ROW 135; name the folder build-135-rainbow-covenant.
- MEMBER rows (151–200) are verse-videos: same style block, same laws, same feed
  card; the closing card also carries a one-line pointer to the matching Gospel
  Library topic named in THE-200.md. No church logos, footage, or manual text ever.

## MACHINE ASSIGNMENTS (v4 — TWO LINUX MACHINES ONLY; see PROTOCOL-V4.md)

| Machine | Rows 1–200, yours completely |
|---|---|
| **L1** | 1–100 |
| **L2** | 101–200 |

Windows machines are RETIRED from building (audio/font defects) — drafts/audits only.

Within YOUR range, work in this order:
1. **BOOTSTRAP (whichever machine gets here first):** if
   media-production/JESUS-MASTER-REF/ is EMPTY — generate THREE candidate portraits
   of the standardized Jesus in Flow (the locked painted style; JESUS LOCK v3
   description; bust portrait + three-quarter + full-figure for each candidate is
   ideal, minimum one clear bust portrait each), save to
   media-production/JESUS-MASTER-REF/candidates/, push, then tell Cameron in ONE
   line to pick 1, 2 or 3. When he picks, move the winner's images to
   JESUS-MASTER-REF/ as jesus-face.jpeg (+ any extra angles), delete the losers,
   push. If another machine already pushed candidates, skip this.
2. **v3 REDO of built rows in your range — TRIAGE FIRST (Cameron, 2026-07-15):**
   not every old video needs the face rework. Sort each built row into one of three
   buckets before touching it:
   - **NO-JESUS videos** (no divine figure in any frame — parable interiors, OT
     stories, verse videos): NO face redo. Eligible for Cameron's approval AS-IS.
     Apply only the cheap sweep (caption-v2 re-assembly + homograph ear-check) and
     note "sweep only" in the row.
   - **FRAME-ONLY videos** (Jesus appears just in a brief framing shot telling the
     story — e.g. one or two from-behind shots): NO face redo required, IF the frame
     does its real job — it must clearly show WHERE he was, WHO he was telling it
     to, and make the WHY land (why this story mattered to those hearers, there,
     then). If the existing frame shots already do that: sweep only. If the frame
     is vague about place/audience: regenerate just those 1–2 frame shots (face
     optional, master-ref if shown).
   - **JESUS-ACTIVE videos** (he acts in the story — healings, encounters, callings,
     passion week): full v3 face redo per the section below.
   THE FRAME LAW (applies to all storytelling videos, new and old): a parable's
   framing shots exist to teach context — place, audience, stakes — not to showcase
   Jesus. His face does NOT need to appear in every video; moderate and natural.
   Work order within the redo: (see the v3 REDO section): oldest row
   first. Skip any row already noted "v3 REDONE".
3. **New builds** of unbuilt rows in your range, lowest number first.
If JESUS-MASTER-REF/ is empty and candidates are already pushed awaiting Cameron's
pick, do NOT idle and do NOT build Jesus stills — build the narration + prompts +
non-Jesus stills of your next row, or say in one line you are blocked on the pick.

## FLOW ACCESS — EXTENSION FIRST (corrected 2026-07-15 late: the driver's fresh
profile forced needless logins and blocked the fleet — Cameron's daily Chrome is
ALREADY logged into Flow)

PREFLIGHT, in order:
1. **Claude Chrome extension** (the proven path — it built every existing video):
   try to connect, twice max. If it connects → use the playbook's Flow procedure in
   Cameron's normal Chrome. NO login needed — he's already signed in.
2. If the extension won't connect: `python3 media-production/flow_driver.py check`.
   If it prints logged_in=True → use the driver
   (`gen --prompt ... --ref ... --out ...`; it prints each generation's credit cost).
3. Only if BOTH fail: say in ONE line
   "BLOCKED: need either the Claude extension enabled or one Google login in the
   driver window (flow_driver.py open)" — then do browserless work (narration,
   prompts, QC, queue) or say SESSION DONE. Never idle, never retry beyond two.
## SESSION HYGIENE (context is the scarcest resource)

- One chat session builds/redoes AT MOST 4 videos, then hands off. The REPO is the
  memory, not the chat: QUEUE.md holds all state, so a fresh session loses nothing.
- HANDOFF = (1) push everything (partial work pushed is fine — note it in the Claim
  column), (2) append any NEW gotcha as ONE dated bullet to FLOW-BUILD-PLAYBOOK.md,
  (3) say exactly: "SESSION DONE — built rows X, Y, Z. Start a fresh chat."
- No narrative session logs. No re-reading files the playbook summarizes. No
  narrating between steps. Tokens spent talking are tokens not spent building.

## RUN UNATTENDED

Do NOT ask Cameron questions. Make sensible defaults, keep going until every row in
your range is built and pushed. Only stop for a real technical blocker you cannot
solve — and then say it in one line. Standing decisions already made (do not re-ask):
- Over-length videos: **30MB size cap**, keep every word (don't trim, don't starve).
- Style/look: locked. Use the Master Style Block byte-identical.

---

## READ ONCE, THEN NEVER AGAIN (save Claude tokens)

Read whole big files at most once; use `grep`/`sed` for single lines; copy templates
instead of re-inventing. Do NOT read SESSION-LOG.md, other builds' logs, or history
prose.
1. `media-production/CREW-GUIDE.md`
2. `media-production/PRODUCTION-BIBLE.md` — LAW sections only (§0 Three Laws, Standing
   Laws, §4b Pre-Flight, §5 QC, §5b Failure Log). Skip history/money/mission prose.
3. `media-production/FLOW-BUILD-PLAYBOOK.md` — **read this** — the distilled fast/low-token
   procedure: exact Flow $0 settings, the reliable JS download (skip screenshots), panel/face
   reroll rules, Windows ffmpeg/font gotchas, the 9:16 reset, browser selection, caption-box
   tuning, and the routine gen_site_index / index.html rebase fix.
4. `media-production/build-47-houses-on-rock-and-sand/BUILD-STATUS.md` — the $0 FLOW procedure.
5. Templates — copy one, change only story content (Master Style Block byte-identical):
   - Story video: `build-135-rainbow-covenant/` (Windows-ready build.py, 30MB cap), or
     `build-48-new-wine-old-bottles/`, `build-41-counting-the-cost/`.
   - MEMBER verse-video (rows 151–200): `build-161-called-of-god/` (KJV in the scripture
     voice, Gospel Library pointer on the closing card).

## BINDING LAWS (don't re-derive)

🛑 FACE LAW REVERSED (Cameron, 2026-07-15): Jesus's face IS SHOWN — the SAME face in
every picture of every video. He is Middle Eastern: warm tan olive-brown skin,
shoulder-length dark brown-black hair, full dark beard, warm BROWN eyes — the familiar
modern-Christian depiction made unmistakably Middle Eastern. NEVER caucasian, pale,
blue-eyed or blond. No halo, no glow. Consistency is enforced by IMAGE, not prose:
every shot where he appears carries (a) the byte-identical JESUS LOCK v3 paragraph
(the exact text lives in jesus_face_gate.py — copy it from there) and (b) a
"REF: jesus-master-ref" line, and the generation ATTACHES the approved portraits from
media-production/JESUS-MASTER-REF/ as character references. Show him a MODERATE
amount — compose scenes naturally; he does not need a close-up in every frame, but
when his face is in frame it must match the master ref exactly. QC every Jesus frame
against the master portrait; ANY face drift = regenerate. jesus_face_gate.py (v3)
now enforces this — it must still exit 0 before any generation.
**Only Jesus wears cream/off-white** — dress everyone else in darker earth colors, in
every prompt; two-voice (narrator `en-US-AndrewNeural`, modern paraphrase; Jesus
`en-US-ChristopherNeural`, EXACT KJV only, no Multilingual voice); Phase-1
**STILLS-ONLY**, no motion clips; Master Style Block byte-identical in every prompt;
character/wardrobe locks written into every prompt the character appears in; no spoken
gap over 2.5s; tell the whole story to the final verse; closing card is an invitation,
never a fear-question. File name = `book-chapter_story-name.mp4`.

**HOMOGRAPH LAW (added 2026-07-15 — the #135 "bow" defect; "live" is the #1 offender
across MANY built videos: the verb live/lived must be /liv/, never /lyve/ — respell as
"liv" for TTS when misread):** edge-tts misreads
scripture homographs. EAR-CHECK every segment containing: bow, wound, wind, tears,
lead, sow/sows, live/lives, read, dove, bass, minute, use(d), close. If misread, fix
the AUDIO ONLY via a spoken respelling — in make_narration.py keep the caption text
exact, and add a SPOKEN override used only for TTS (e.g. TTS gets "beau" so "bow"
says /boh/; captions still show the true KJV word). Pattern documented in the playbook.
Re-listen to the fixed segment before assembly. A misread KJV word is a rejected video.

**CAPTION LAW v2 (Cameron, 2026-07-15 — replaces every earlier caption rule):** captions
sit WIDE along the BOTTOM of the frame and never climb toward the middle. Narrator
captions: max 2 lines. KJV: max 3 lines. A long segment is SPLIT into chunks that swap
in sync with the narration (proportional timing across the spoken audio) — the words
on screen are still the exact spoken words, just shown a piece at a time. The
implementation lives in the TEMPLATE build.py (build-48): chunk_caption() +
caption_layers() + the new build_still() signature. COPY IT — do not re-derive.
Every NEW video must use it. Videos built with the old tall captions will be
re-assembled in the remediation sweep (below).

**🛑 THE v3 REDO (Cameron, 2026-07-15 — this supersedes and absorbs the remediation
sweep; it is now THE priority job):** every already-built video gets REDONE under the
new face law. Per video: (1) KEEP the narration scripts (copy make_narration.py; only
fix homograph misreads with SPOKEN overrides); (2) KEEP every still where Jesus does
not appear; (3) REGENERATE every still where Jesus appears, staged naturally with his
face visible where the scene calls for it, locked to JESUS-MASTER-REF; (4) captions =
CAPTION v2 (copy from the build-48 template); (5) full QC incl. face-match against the
master portrait; (6) re-run build.py, gen_site_index.py, push. Row note: "v3 REDONE
<date>". Do NOT start a redo until media-production/JESUS-MASTER-REF/ contains the
approved portraits (Cameron picks the face first — if the folder is empty, build NEW
rows under the new law instead? NO: if JESUS-MASTER-REF is empty, STOP and tell
Cameron in one line that the master face awaits his pick.)

**OLD REMEDIATION SWEEP (absorbed into the v3 redo above):** for
each already-built video in your range: (1) ear-check all segments for homographs —
regenerate ONLY offending audio segments with a TTS respelling; (2) port the caption-v2
functions into that build's build.py; (3) re-run build.py (stills unchanged, $0),
QC one frame for caption placement, re-run gen_site_index.py, push. Note
"caption-v2 + ear-check remediated <date>" in the row's Claim column.

---

## PER-VIDEO LOOP (repeat until your range is empty)

1. `git pull --rebase`. In QUEUE.md find the lowest row in YOUR range with Built ⬜ and
   Claim empty. Stamp Claim `CLAIMED Machine <letter> <date>`, commit + push NOW.
2. Read the KJV passage in full context. Storyboard 8–16 beats, one still each.
3. Write `build-NN-<slug>/PROMPTS.md` from the template (Master Style Block
   byte-identical; character/wardrobe locks in every prompt a character appears in).
4. `python3 media-production/jesus_face_gate.py --dir <dir>` MUST exit 0. Fix prompts
   and re-run until it passes. NO art before it passes.
5. In Flow: New project → **Image → Nano Banana 2 → 9:16 → 1x** → paste the FULL prompt
   (style block + body) → generate → download the **2K** image → save as
   `<dir>/assets/<slug>.jpeg`. One still per beat. (Downloads: Chrome "ask where to
   save" OFF so files land on disk; see build-47 BUILD-STATUS for the download detail.)
6. QC every still: face never visible, count anatomy, action reads, time-of-day matches
   scripture, style matches template, no baked-in text, only-Jesus-in-cream. Regenerate
   misses in Flow.
7. `python3 make_narration.py` (edge-tts). Then `python3 build.py` to assemble (Ken
   Burns drift, serif captions, cream-italic KJV, closing card). Export 9:16
   1080x1920 H.264 **under 30MB**, named `book-chapter_story-name.mp4`.
8. Full QC pass: face-audit sampled frames, verify KJV captions are exact, no dead air.
9. Tick **Prep + Built** ✅ for the row in QUEUE.md (leave **Appr** blank — see below).
   Add the title to the TITLES map in `media-production/gen_site_index.py`, then
   `python3 media-production/gen_site_index.py`.
10. **PUBLISH = your notification to Cameron:** `git add -A`, commit, `git pull
    --rebase`, `git push origin main`. That publishes the finished video to the gallery
    at **https://noremacttevol.github.io/MBM/** — Cameron watches new videos appear
    there one by one. Cameron never touches git.
11. Next row. Repeat.

---

## APPROVAL — who sets the final checkmark

The **building machines set `Built` ✅ only. They NEVER set `Appr`.**

The **`Appr` ✅ checkmark is set only by the approval-monitor session**, after Cameron
watches a video and says yes. That is a separate Claude chat Cameron runs. Its job:
- When Cameron says a video number is **approved**: `git pull --rebase`, tick that
  row's **Appr** column ✅ in QUEUE.md, commit, push.
- When Cameron says a video is **rejected**: leave Appr blank, write his reason in that
  row's Claim/notes column, and set Built back to ⬜ so a building machine remakes it.
- The monitor NEVER builds videos and NEVER touches the paid API. It only moves the
  approval checkmark.

So the lifecycle of one row is:
`⬜ → Machine X builds + pushes (Built ✅) → appears on the gallery → Cameron watches →
Cameron tells the monitor yes/no → monitor sets Appr ✅ (or bounces it back).`
