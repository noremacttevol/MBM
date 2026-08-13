## 2026-08-12 (Fable 5, main session) — PER-VIDEO PUBLISH FILES for ALL 200: social/per-video/001-200.md, one numbered file per video, every platform's paste text — Machine A `Dev`

**Commit:** (this commit)

Cameron: working toward all 200 posted; "make it a file for the 200 and the
number as the file title only... info for each video... for each of the 4
social medias." Built `social/make-per-video.py` → `social/per-video/001.md`
through `200.md`. Each file: status line (APPROVED = exact published text +
byte-verified export name / DRAFT = ready text, regenerate on approval since a
story swap voids it), then fenced paste blocks: YouTube title / description /
tags, Facebook whole post, TikTok whole caption, Instagram whole caption —
hashtags assembled per platform, milkb4meat.org the only link, platform rules
restated in every header (Short vs regular, IG any-length note, FB=Reel).

**The 44 approved rows reuse the exact first-9-era text** (POST-QUEUE +
YOUTUBE-UPLOAD-SHEET parsers). **The 156 not-yet-approved rows were authored
fresh this session** (4 parallel writer agents, same voice: 2-3 truthful KJV
sentences + one mirror question + ref line; judgment calls documented in the
agents' notes — e.g. rows 69/169 same-scripture distinct angles, row 66 name
only in title since Luke doesn't name Malchus, row 158 stick-of-Joseph kept
strictly to Ezekiel's text). Validation: 156/156 rows, ZERO "word for word",
zero exclamations/emoji, every question ends in ?, every file carries the
link; merged to `social/captions-authored.json` (committed source of truth).
Cameron tracks posting via the reviewer chips; approved-state refresh =
refresh-postable.py → make-per-video.py.

## 2026-08-12 (cont. 97) — Row 118 C-FIX VERIFY (Jonah): wall STILL up, fixed a STALE-GREEN reviewer card that was bragging the exact frames Cameron flagged — Machine A `Dev`, Opus runner

**Commit:** this push.

- **Complaint-first + lowest-row:** row 118 is the lowest waiting row with an open complaint — "2:37 Jonah was 3× bigger than the people, fix it. The people in 3:08 look dead, fix it." Traced to the rendered frames: 2:37 = beat b28 (`s28`, giant Jonah at the Nineveh gate), 3:08 = beat b33 (`s33`, grey/statue repentant crowd).
- **Autopsy was already DONE + committed (eff25e6df):** b28 verdict ALLOWED → same-scale constraint added; b33 verdict CAUSED by "ashes"+haircloth monochrome → living-warm-skin rewrite. `--check` PASS (46 beats, v4) re-verified intact this session.
- **Real paid probe** `--only b28 b33 --redo --ceiling 645` → `429 prepay depleted`, meter frozen $617.34 (unmoved since 04:11). Wall STILL up — same block freezing rows 82/95/116/118. mp4 NOT reshipped (would repeat the complaint).
- **NEW THIS PASS (the genuine $0 fix):** reviewer card v118 had the row-95-class STALE-GREEN bug — its "🛠 What this cut changed" flag bragged *"consistent Jonah, realistic Nineveh, repentant city,"* the exact frames Cameron flagged, contradicting his own complaint. Rewrote it + added `data-machine-reason` so it honestly says the video on the page is still the OLD flagged cut and the giant-Jonah/dead-crowd fix is written+checked, blocked only on the billing top-up. Deployed + live-verified.
- **Billing tension surfaced:** cont.91 logged Cameron's rule that the prepay auto-reloads and to just retry — but it has now shown depleted for ~18h across many real probes, so it genuinely appears to need a manual top-up (https://ai.studio/projects). Inbox ask already current.
- NO identical re-park churn beyond the card fix (row-95 cont.123 STOP discipline).

---

## 2026-08-12 (cont. 91) — CAMERON'S AUTO-RELOAD RULE wired in: depleted 429 = transient, RETRY (gen backoff + live probe every tick); never "out of money", never ask him to top up — Machine A `Dev`, process-engineer session

**Commit:** this push. Cameron: "its never empty you just have to try it again it loads more cash automatically remember this."

- Probed the live API 3× (~30 s apart) at the time of his message: still `429 prepayment depleted` — reported as observation only, per the new rule.
- **v2_gen_api.py:** depleted 429 no longer `SystemExit("OUT OF MONEY")` — patient in-run retries (30/60/120/240/300 s), then a soft error saying the next tick retries; rows resume where they stopped.
- **autopilot.sh:** billing state now decided by a LIVE $0 probe each tick (3 tries, 10 s apart), never stale log-greps; a failed probe defers paid work ONE tick and re-probes — the cron loop is the retry engine and resumes the instant Google's auto-reload lands. Free (audio/author) work continues regardless. Idle message rewritten (no more top-up nagging).
- Memory: `gemini-prepay-auto-reload` (feedback). Monitor armed in-session to announce the moment the API opens.

---

