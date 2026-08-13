## 2026-08-13 — WEBSITE OLD-ERA PURGE + STORY-FIRST REBUILD: 2.8GB of old cuts off hosting, homepage leads with the films, stories page 44→116, gate extended to the site — Machine A `Dev`

Cameron: "the website... has a bunch of the old videos on it and just isnt giving the app
its justice." He was right, three ways:
- **site/fixed/ = 152 OLD-ERA mp4s (2.8 GB) publicly hosted** at guessable URLs — and
  fully ORPHANED (zero pages referenced it). Archived to
  media-production-v2/site-media-archive/, now 404 live.
- **Homepage fronted the old app era**: June explainer video + 37 old walkthrough
  screenshots + a loose old peter-walks-on-water cut in the site root. All archived; the
  homepage now leads with the REAL films — featured tap-to-play Cloak player (#watch),
  realistic scene sections replacing every old screenshot, hero copy leads with the films.
- **stories.html showed 44 while 116 are approved** (the FULL-THROTTLE publisher landed 72
  more between builds). Regenerated from PUBLISH-LEDGER.json → 116 cards, counts synced.
  NEW scripts/regen_stories_page.py — publisher sessions run it whenever an approval
  lands so the site never undersells again.
- Internal tool pages (review, post-kit, how-i-see-it, characters) noindexed; review.html
  backups off hosting.
- **Gate extended** (scripts/audit_public_videos.py): F1 = no mp4 anywhere on the site
  outside the approved gallery; F2 = public pages reference only approved ids/no retired
  paths. **10/10 checks PASS against the LIVE site** (116 byte-exact vs approval sha1s,
  20 old-era rows 404, fixed//explainer/walk all 404). DOM-verified: featured player
  present, 0 broken images, 116 cards, zero old-media references.

**Cost:** $0 media. Deploys: 2× firebase hosting.

---

## 2026-08-13 (cont. 94) — Row 118 C-FIX SHIPPED: fixed Cameron's 2:37 giant-Jonah + 3:08 dead-crowd complaint (billing restored) — Machine A `Dev`, Opus runner

Complaint-first + lowest-waiting → row 118 (open since 2026-08-12, billing-parked 13×).
Billing wall CLEARED overnight (row-95 paid gens 01:34/01:36 today). Landed the
touch-once fix:
- Confirmed BOTH complaints off the live mp4 (ffmpeg -ss 157 / -ss 188): 2:37 Jonah
  larger than same-depth townsfolk; 3:08 crowd grey/terracotta = "look dead".
- Regenerated only the 2 flagged beats (staged fix already --check PASS v4):
  b28 (2:37) → high/back camera, Jonah SMALL mid-distance, consistent scale;
  b33 (3:08) → LIVING warm-skinned praying crowd, ash on cloth/brow only.
- FULL-CUT GATE (6b): one mid-window frame per beat off the NEW mp4, 46/46 clean +
  3 caption frames; only b28/b33 changed, 44 others match the 08-11 clean gate.
- AUDIO REBUILD PASS byte-identical (SHA 172b62c7, AUDIO_FROM_V1_SEGMENTS=True).
- Rerolls 2/46 = 4.3% (≤15%); cost ~$0.27 (far below $6.10/row avg — COST LAW trend holds).
- Shipped: commit 924f1c51, review card v118 rewritten (both complaints answered in
  Cameron's words, billing-parked note removed), deployed + live-verified.

Commit: b0127ce3a880e5df8ba0adb93e71e52faaf973d6
## 2026-08-13 (cont. 93) — FULL THROTTLE for Cameron's "all 200 tonight": API confirmed OPEN (auto-reload landed), 12 stranded ready rows FREED, row 140 rerouted to author lane, cron 10min->5min + 4->6 lanes, escalation-crash hotfix — Machine A `Dev`, process-engineer session

Cameron: "there is money now do like we have discussed. also i want all 200 made into new versions tonight."

- **API OPEN:** live probe returned OK on the production key — his rule held (auto-reload landed; the loop's own probe picks it up on the next tick). Board truth at start: **130 BUILT / 2 RUNNING / 68 AUTHORED (62 Ready) = 70 rows to go.**
- **12 stranded rows FREED (115, 116, 133, 134, 142-145, 185, 188, 189, 200):** stale PARKED-BILLING / AUDIO-FIX-DONE notes sat in the Claim column, which the picker reads as "a lane owns this row" — they would NEVER have built. Notes archived into the Ready cell, claims cleared, ✅ ensured. This was the LOW-NUMBER law's "a park with no pickup" failure class, live.
- **Row 140 (Naaman) NOT built** — its park is Cameron's own story-level complaint (duplicate prodigal-son moral); State -> NEEDS-REBUILD so the $0 author lane re-authors the moral (obedience angle) instead of the row shipping the rejected story or rotting in limbo.
- **Throughput:** cron `*/5` (was every 10 min) with `MBM_LANES=6` (was 4) — lanes fill in ~30 min and stay full; runner sessions already continue to next ready rows within one session.
- **HOTFIX:** yesterday's model-escalation block crashed the whole tick under `set -e pipefail` whenever a row had no prior sessions (grep no-match exit killed the pipeline); billing-down had masked it — caught by dry-run minutes before the first paid tick, fixed with an in-pipeline `|| true`.
- Honest math told to Cameron: ~70 builds at observed session times ≈ 12-20 h of full-throttle running; also flagged that the Claude-side weekly limit is the one ceiling the loop cannot fix itself.

---

