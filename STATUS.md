# 📊 MBM — LIVE STATUS BOARD

**This is the one file to look at. It shows what is DONE, what is IN PROGRESS,
and what is still TO DO — with a link to watch or download every finished
video.** Updated 2026-07-30.

Repo: `github.com/noremacttevol/MBM`

---

## 👷 ACTIVE WORKERS RIGHT NOW (2026-08-01 — every agent updates its own row; a row older than a day is stale, reclaim it)

| Worker | On | State |
|---|---|---|
| Codex (VS Code, Machine A) | Story 04 (Nicodemus at Night) realistic replacement | in progress — claimed 2026-08-01 after Story 3 shipped live. Audit the existing V2 story plan and pictures against the complete approved script/audio, night geography, recurring Nicodemus/Jesus identities, anatomy, action, and encoded gates before repairing anything. App feed remains untouched. |
| Claude worker 1 | Story 07 Peter — "immediately" re-voice | ✅ shipped V7 to reviewer (2c0c66159) |
| Claude worker 2 | Story 11 Storm — 3 pictures + "Peace, be still" pacing | ✅ shipped realistic V4 to reviewer (f8acb3acc) |
| Claude worker 3 | Story 02 Prodigal — full realistic rebuild | ✅ shipped realistic V2 cut to reviewer (2026-08-01) |
| Claude worker 4 | Story 06 Two Sons — full realistic rebuild + father's-ask complaint fix | ✅ shipped realistic V2 to reviewer (2026-08-01) — open complaint root-caused: the ask WAS voiced 2026-07-24 but the old assembly dropped j28/j29/j30/n1b/n2b/j29b/s31/n5b; V1 rebuilt 1:23→2:06 assembly-only (zero re-voicing), 23 realistic 2K pictures, AUDIO LOCK PASS. |
| Claude worker 4 (Machine A, Dev) | Story 05 (Bent-Over Woman) full realistic rebuild | ✅ shipped realistic V2 cut to reviewer (2026-08-01) |
| Claude worker 6 (Machine A, Dev) | Story 09 (Rich Young Ruler) full realistic rebuild | ✅ shipped realistic V2 to reviewer (2026-08-01) — 31 pictures rebuilt at native 2K (old set Session-6 rejected), all 31 windows re-timed from the fixed extract_beats (old card sat ~12 s early), the two weight-bearing frames (b12 "loved him", b29 watching him go) pass the love-not-pity standard, AUDIO LOCK PASS, ≈$6.16 spend. |
| Claude worker 7 (Machine A, Dev) | Story 10 (Woman at the Well) full realistic rebuild | in progress — claimed 2026-08-01. All 32 old V2 stills are 768x1376 (resolution audit: entire row 1K) and Session-6 rejected; regenerating all beats to the realistic standard on the Gemini API at native 2K, audio LOCKED to the authoritative narration (founding story), windows re-timed from the fixed extract_beats. Ships to Reviewer only. |
| Claude worker 5 (Machine A, Dev) | Story 08 (The Lost Coin) full realistic rebuild | ✅ shipped realistic V2 to reviewer (2026-08-01) — 12 pictures rebuilt at native 2K (old set was the pre-V5 rejected wave), windows re-timed from the fixed extract_beats (old drifted up to 4.2 s), AUDIO LOCK PASS, $2.95 spend. |

Coordination law for ALL workers (Codex included — it reads AGENTS.md): claim by push
BEFORE building, commit only your own files, update your row here in the same commit,
and push as you go. Work that isn't pushed is invisible and will be collided with.

## 🎬 CURRENT WORK — realistic V2 visual rebuild

The mobile app is intentionally untouched. The existing scripts, chosen voices,
narration, music, timing, and captions stay locked unless Cameron reports a
specific defect. The story pictures are being fully rebuilt to the realistic,
reverent standard Cameron approved on 2026-07-30.

| # | Story | V2 state | Reviewer candidate |
|---|-------|----------|--------------------|
| 01 | Woman Who Touched His Cloak (Mark 5) | **Realistic V3 live on reviewer — awaiting Cameron** 🟡 — 17 face-only repairs and 3 byte-identical preserved frames pass the V4 rubric and hash-backed boards. Cameron's background-sound complaint was isolated to the two already-confirmed Alexander sources; those same takes were selectively denoised at their exact timeline positions with no TTS, rewrite, shortening, or retiming. Full 1:48.833 story and captions verified. Live browser check confirms the new hash is in Unwatched and the complaint is retained for comparison. App feed remains untouched. | [▶ Cloak realistic V3](media-production-v2/build-01-cloak/mark-5_woman-touches-his-cloak-realistic-v3.mp4) |
| 03 | Zacchaeus (Luke 19) | **Realistic V3 live on Reviewer 2026-08-01 — awaiting Cameron** 🟡 — all 26 final 1536×2752 pictures pass sequence review and encoded QC; 24 identity/action repairs and `s15`/`s19` retained byte-identical. Jesus and Zacchaeus pass hash-backed face boards; run, climb, invitation-before-vow, money-free vow, and later three-person restitution preserve the complete script. The full 3:42 audio is packet-identical to the approved original and all four Jesus lines are Alexander. Live raw bytes match the tested hash; the replacement is Unwatched with the earlier complaint retained. App feed untouched. | [▶ Zacchaeus realistic V3](media-production-v2/build-03-zacchaeus/luke-19_zacchaeus-realistic-v3.mp4) |
| 04 | Nicodemus at Night (John 3) | **Realistic replacement claimed by Codex 2026-08-01** 🔵 — audit the existing V2 draft and preserve the complete approved script/audio and sound composition. Require one stable Nicodemus, the locked Jesus identity, believable private nighttime geography and lamps, scripture-faithful conversation order, V4 prompt checks, hash-backed face boards, and encoded-frame QC before Reviewer-only publication. App feed remains untouched. | — |
| 07 | Peter Walks on Water (Matthew 14) | **V7 cut shipped 2026-08-01 — awaiting Cameron** 🟡 — "immediately" (n6) re-voiced: the old take slurred the word into 0.54s; in-context A/B (round2 pattern, whisper round-trip) adopted SPOKEN respelling "imediately", which renders the full word 3/3 takes; new cut whisper-verified. Lamp complaint already fixed in the V6 stills — pictures untouched. Board card now points at V7 (new hash → returns to Unwatched with the prior complaint retained for re-check). | [▶ Peter V7](media-production-v2/codex-test-07-peter-water/video-build/peter-walks-on-water-codex-test-v7.mp4) |
| 02 | The Prodigal Son (Luke 15) | **Realistic V3 live on reviewer — awaiting Cameron** 🟡 (2026-08-01) — Cameron's “All Faces changes too much” complaint drove an identity-only repair: 18 drifting pictures fixed, 6 already-correct pictures kept byte-identical, and Jesus/father/younger son/elder son pass hash-backed boards across all 32 appearances. The original Story 2 audio is packet-for-packet unchanged. New hash returned it to Unwatched and retains the complaint for comparison. | [▶ Prodigal realistic V3](media-production-v2/build-02-prodigal/luke-15_prodigal-son-realistic-v3.mp4) |
| 11 | Calming the Storm (Mark 4) | **FIX SHIPPED — realistic V4 cut, awaiting Cameron** 🟡 (2026-08-01) — all four complaints addressed: first picture regenerated at 2K from the composition he liked (Jesus set apart, crowd facing him); mast-climber frame (s10) redone with every man low in the hull, feet on deck; bailing frame (s11) redone throwing water OUT over the gunwale into the sea; j1 "Peace, be still" re-rendered slow and weighty (2.3s with a real pause, was 1.4s rushed) and the whole cut re-timed so captions/pictures land exactly with the voice (the old cut drifted up to 8s — extract_beats now reads each build's own raw-vs-trimmed timeline formula). | [▶ Storm realistic V4](media-production-v2/build-11-storm/mark-4_calming-the-storm-realistic-v4.mp4) |
| 06 | The Two Sons (Matthew 21) | **Realistic V2 live on reviewer 2026-08-01 — awaiting Cameron** 🟡 — his open complaint ("you cut out the original thing the father asked the sons") root-caused: the complete script WAS voiced on 2026-07-24 (j28 the father's KJV ask, j29/j30 both sons' answers, s31 "The first", n5b the plain-terms publican/harlot line from his QUEUE note) but the V1 build.py BEATS list was never updated, so the assembled cut silently dropped them. Fixed assembly-only — zero re-voicing — V1 rebuilt 1:23→2:06, whisper ear-check confirms every line. 23 realistic 2K pictures (father + both sons + priests held by fresh image anchors, Jesus by LOCK v5): the ask, the flat refusal, the courteous yes, the repentance, the empty row and the outsiders each land on their own frame; 5 QC rerolls (triptych, edge intruder, camera gaze, priest count, stray distant Jesus) — two traced to defective roughs, dropped per the prodigal b20 lesson. AUDIO LOCK PASS; rendered-frame caption check on the delivered file. New hash returns the card to Unwatched with the complaint retained. | [▶ Two Sons realistic V2](media-production-v2/build-06-two-sons/matthew-21_two-sons-realistic-v2.mp4) |
| 05 | The Bent-Over Woman (Luke 13) | **Realistic V2 live on reviewer 2026-08-01 — awaiting Cameron** 🟡 — all 37 pictures rebuilt at native 2K to the realistic standard (old set was Session-6 rejected, 3 frames 1K): one locked woman whose posture arc (bent double → caught halfway up → fully straight) carries the story, V2 Jesus in all 20 appearances, one consistent ruler and farmer, ADVERSARY LAW held (the bond shown only as the abandoned stick, which stays on the floor from "loosed from this bond" onward). All 37 windows re-timed from the fixed extract_beats (old windows drifted ~13 s); AUDIO LOCK PASS (byte-identical approved audio); verify-mp4 OK 4:08/20.8 MB; captions checked on 15 extracted frames. New hash puts it in Unwatched. App feed untouched. | [▶ Bent Woman realistic V2](media-production-v2/build-05-bent-woman/luke-13_bent-woman-realistic-v2.mp4) |
| 08 | The Lost Coin (Luke 15) | **Realistic V2 live on reviewer 2026-08-01 — awaiting Cameron** 🟡 — all 12 pictures rebuilt at native 2K to the realistic standard (the old 2026-07-29 set carried the pre-V5 Jesus and the Session-6 look): one locked woman across the whole search (image anchor, 9 appearances), V2 Jesus in both frame-story beats, TEN countable coins (nine in the row + the tenth in her fingers), NINE-with-a-gap after the loss, clay oil lamp (KJV "candle"), diligence on hands and knees, public doorway joy, and the close on one tax collector's face instead of V1's starfield; CONTENT-CARE held (v10's angels not painted). All 12 windows re-timed from the fixed extract_beats (old windows drifted up to 4.2 s) and verified with silencedetect. AUDIO LOCK PASS (byte-identical approved audio, the "cut short" complaint stays resolved); verify-mp4 OK 1:09/19.9 MB; captions checked on 13 extracted frames. New hash puts it in Unwatched. App feed untouched. | [▶ Lost Coin realistic V2](media-production-v2/build-08-lost-coin/luke-15_lost-coin-realistic-v2.mp4) |
| 09 | Rich Young Ruler (Mark 10) | **Realistic V2 live on reviewer 2026-08-01 — awaiting Cameron** 🟡 — all 31 pictures rebuilt at native 2K to the realistic standard (old set Session-6 rejected, only 21 of 31 beats ever generated): one locked rich young man carried by a fresh image anchor through the run, the public kneeling, the ring-clutch and the grief; V2 Jesus in all 17 appearances; the two frames the founding story stands on — b12 "Jesus, looking at him, loved him" (eyes open, unmistakably love, not pity) and b29 watching him go with tears — pass the beat map's own standard; Peter/Andrew/James/John from the CAST-V2-REF sheets; the poor at the gate dignified, with the red KJV "give to the poor" landing on their frame; sunset only after "The sun went down". All 31 windows re-timed from the fixed extract_beats (old card ~12 s early) with silencedetect-placed sub-splits. AUDIO LOCK PASS (byte-identical approved audio); verify-mp4 OK 3:17/21.9 MB; captions checked on 14 extracted frames. New hash puts it in Unwatched. App feed untouched. | [▶ Rich Ruler realistic V2](media-production-v2/build-09-rich-ruler/mark-10_rich-ruler-realistic-v2.mp4) |
| 13 | The Man Through the Roof (Mark 2) | **Realistic V3 live on reviewer 2026-08-01 — awaiting Cameron** 🟡 — 45 rebuilt pictures; same paralysed man, same four distinct friends, and locked V2 Jesus across the full story; all six recurring identities passed hash-backed face boards; exactly four carriers and four functional ropes; full roof-to-healing sequence rendered and inspected. The complete 4:59 script is present. Jesus-voice provenance is proven Alexander by exact source hashes, and punctuation pauses were measured. New hash returned the cut to Unwatched while retaining the prior complaint. | [▶ Roof realistic V3](media-production-v2/build-13-roof/mark-2_man-through-the-roof-realistic-v3.mp4) |

New V2 cuts are published to the Firebase reviewer at
`https://milk-b4-meat.web.app/review.html`. That board shows only this new visual
wave and keeps each exact cut in **Unwatched**, **Approved**, or
**Complained About**. The exact cut Cameron reported stays in **Complained
About**. A replacement returns to **Unwatched**, while retaining the earlier
complaint for Cameron to check, until he approves or reports that replacement.

The July 11 tables below are the historical V1 production record. Their former
"never show Jesus's face" rule is superseded for this V2 rebuild by the approved,
locked V2 Jesus reference and the visual rules in `AGENT-RULES.md`.

---

## 🔄 HOW THIS STAYS LIVE (every machine, every session)

This file is kept current through git — that is the "live" sync between all of
Cameron's computers. The rule for every Claude on every machine:

1. **PULL FIRST** — `git pull --rebase origin main` at the start of a session and
   before touching this file.
2. **UPDATE IT** — the moment a video changes state (claimed → built → approved),
   edit its row here in the same commit as the work.
3. **PUSH IMMEDIATELY** — `git push origin main` so every other machine (and
   Cameron) sees it right away.

If you ever see this file disagree with reality, fix the file — it is the human
dashboard. The detailed per-machine claim mechanics live in
[`media-production/VIDEO-ASSIGNMENTS.md`](media-production/VIDEO-ASSIGNMENTS.md);
this file is the at-a-glance summary of it.

**Historical V1 standards (Cameron, 2026-07-11; superseded for V2):**
1. **Jesus's face is NEVER shown** — real Middle-Eastern man seen only from
   behind / over-the-shoulder / at a distance (no white, no hood, no glow).
2. **Phase 1 = STILLS ONLY** — pictures + narration, NO AI motion clips (they
   come back in Phase 2, later).

---

## ✅ DONE — meets the new standard, ready to watch / download

> Click **▶ watch** to play it on GitHub in the browser, or **⬇ download** to save the file.

| # | Story | Length | Status | Watch / Download |
|---|-------|--------|--------|------------------|
| 01 | Woman Who Touched His Cloak (Mark 5) | 2:15 | **APPROVED** ✅ | [▶ watch](media-production/build-01-cloak/mark-5_woman-touches-his-cloak.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-01-cloak/mark-5_woman-touches-his-cloak.mp4) |
| 02 | The Prodigal Son (Luke 15) | 2:43 | **APPROVED** ✅ | [▶ watch](media-production/build-02-prodigal/luke-15_prodigal-son.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-02-prodigal/luke-15_prodigal-son.mp4) |
| 03 | Zacchaeus (Luke 19) | 4:09 | **APPROVED** ✅ | [▶ watch](media-production/build-03-zacchaeus/luke-19_zacchaeus.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-03-zacchaeus/luke-19_zacchaeus.mp4) |
| 04 | Nicodemus at Night (John 3) | 6:07 | **APPROVED** ✅ | [▶ watch](media-production/build-04-nicodemus/john-3_nicodemus.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-04-nicodemus/john-3_nicodemus.mp4) |
| 05 | The Bent-Over Woman (Luke 13) | 4:38 | **APPROVED** ✅ | [▶ watch](media-production/build-05-bent-woman/luke-13_bent-woman.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-05-bent-woman/luke-13_bent-woman.mp4) |
| 11 | Calming the Storm (Mark 4) | 4:30 | **built — awaiting Cameron** 🟡 (full redo) | [▶ watch](media-production/build-11-storm/mark-4_calming-the-storm.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-11-storm/mark-4_calming-the-storm.mp4) |
| 12 | Blind Bartimaeus (Mark 10) | 5:18 | **APPROVED** ✅ | [▶ watch](media-production/build-12-bartimaeus/mark-10_bartimaeus.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-12-bartimaeus/mark-10_bartimaeus.mp4) |
| 09 | Rich Young Ruler (Mark 10) | 3:37 | **APPROVED** ✅ | [▶ watch](media-production/build-09-rich-ruler/mark-10_rich-young-ruler.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-09-rich-ruler/mark-10_rich-young-ruler.mp4) |
| 10 | Woman at the Well (John 4) | 4:54 | **Realistic V2 live on reviewer 2026-08-01 — awaiting Cameron** 🟡 | [▶ watch](media-production-v2/build-10-well/john-4_woman-at-the-well-realistic-v2.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production-v2/build-10-well/john-4_woman-at-the-well-realistic-v2.mp4) |
| 17 | Lazarus (John 11) | 6:12 | **APPROVED** ✅ | [▶ watch](media-production/build-17-lazarus/john-11_lazarus.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-17-lazarus/john-11_lazarus.mp4) |
| 06 | Two Sons (Matthew 21) | 1:44 | **APPROVED** ✅ | [▶ watch](media-production/build-06-two-sons/matthew-21_two-sons.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-06-two-sons/matthew-21_two-sons.mp4) |
| 07 | Peter Walks on Water (Matthew 14) | 3:45 | **built — awaiting Cameron** 🟡 (complete current ElevenLabs narration) | [▶ watch](media-production/build-07-peter-water/matthew-14_peter-walks-on-water.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-07-peter-water/matthew-14_peter-walks-on-water.mp4) |
| 13 | Man Through the Roof (Mark 2) | 5:34 | **APPROVED** ✅ | [▶ watch](media-production/build-13-roof/mark-2_man-through-the-roof.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-13-roof/mark-2_man-through-the-roof.mp4) |
| 14 | Ten Lepers (Luke 17) | 4:34 | **APPROVED** ✅ | [▶ watch](media-production/build-14-ten-lepers/luke-17_ten-lepers.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-14-ten-lepers/luke-17_ten-lepers.mp4) |
| 15 | Centurion's Servant (Matthew 8) | 5:08 | **APPROVED** ✅ | [▶ watch](media-production/build-15-centurion/matthew-8_centurion.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-15-centurion/matthew-8_centurion.mp4) |
| 08 | Lost Coin (Luke 15) | 1:06 | **APPROVED** ✅ | [▶ watch](media-production/build-08-lost-coin/luke-15_lost-coin.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-08-lost-coin/luke-15_lost-coin.mp4) |
| 18 | Road to Emmaus (Luke 24) | 4:18 | **built — awaiting Cameron** 🟡 | [▶ watch](media-production/build-18-emmaus/luke-24_emmaus.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-18-emmaus/luke-24_emmaus.mp4) |
| 16 | Mary and Martha (Luke 10) | 3:06 | **built — awaiting Cameron** 🟡 | [▶ watch](media-production/build-16-mary-martha/luke-10_mary-and-martha.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-16-mary-martha/luke-10_mary-and-martha.mp4) |
| 36 | The Shrewd Steward (Luke 16) | 3:10 | **built — awaiting Cameron** 🟡 | [▶ watch](media-production/build-36-shrewd-steward/luke-16_shrewd-steward.mp4) · [⬇ download](https://github.com/noremacttevol/MBM/raw/main/media-production/build-36-shrewd-steward/luke-16_shrewd-steward.mp4) |

*(ALL 16 built videos — 01–15 and 17 — are **APPROVED by Cameron** (2026-07-11, second pass: he watched every built cut and approved them all). **#17 Lazarus beard fix has now SHIPPED** (Machine C, 2026-07-11): s9 regenerated with Lazarus's dark beard and rebuilt, so the approved file at `build-17-lazarus/john-11_lazarus.mp4` already contains the fix — no longer pending/optional. ALL 16 approved finals are LIVE at `https://milk-b4-meat.web.app/story-videos/<catalog-id>.mp4` (deployed 2026-07-11, every URL verified 200/video-mp4 with range support). The #17 stream copy WAS re-synced from the bearded rebuild before deploy — the live #17 is byte-identical to the fixed final.)*

---

## 🔧 IN PROGRESS — being redone right now

The files below **still play**, but they were made under the OLD rules (they
contain AI motion clips and/or predate the face-never rule). They are being
rebuilt to the new standard — the finished file will replace the old one.

| # | Story | Old cut (playable now) | Redone by | State |
|---|-------|------------------------|-----------|-------|
| 38 | The Persistent Widow (Luke 18) | *no file yet* | Machine C | **CLAIMED — building** 🔨 — Cameron's direct order "do 38" 2026-07-12 (off-list). Stills-only parable (Luke 18:1-8), NO Jesus figure (voice + KJV only, face-gate PASS). Milk: CONTRAST — God is nothing like the reluctant, annoyed judge; he is not worn down into caring, he already loves you and already wants to hear you, so keep coming. |
| 44 | The Two Debtors (Luke 7) | luke-7_two-debtors | Computer B (Elli's laptop, Leighton) | **BUILT — awaiting Cameron** 🟡 — 2026-07-14, Cameron's batch order (B=44). Old-faithful path: 8 Flow stills (Nano Banana 2, 2K, $0). Stills-only (Luke 7:36-50), face-gate PASS — Jesus only from behind/over-shoulder/distant (verified on render); parable creditor+debtors have no Jesus figure. Verbatim captions, 5 KJV cream-italic, two sacred silences (7:42 verdict, 7:47 payoff). Milk: forgiven much, loves much. [▶ watch](media-production/build-44-two-debtors/luke-7_two-debtors.mp4) (20.1MB, 4:18) |

*(#16 Mary and Martha and #36 The Shrewd Steward finished 2026-07-12 by Machine A — both moved to the DONE table above, awaiting Cameron.)*

*(06 and 07 are now rework-built — see the DONE table. 06: the last motion clip
was replaced with a still (fully stills-only), and the working son wears
rust-brown/red while the son who didn't work wears cream/white — Cameron's
wardrobe rule. 07: Cameron's 3 picture fixes done (Elli's laptop). 08 PREP is
done and **UNCLAIMED**. 09, 10, 12, 17 are rework/fresh built — see the DONE
table above.)*

---

## ⬜ TO DO — Wave One not started yet

| # | Story | File name | Note |
|---|-------|-----------|------|
| 19 | Breakfast on the Shore (John 21) | john-21_shore | **BUILT — awaiting Cameron** 🟡 — Machine C. Stills-only, verbatim captions, Jesus only behind/hand-only/distance (s1 & s3 face-fixed). [▶ watch](media-production/build-19-shore/john-21_shore.mp4) (20.5MB, 3:04) |
| 20 | Good Samaritan (Luke 10) | luke-10_samaritan | **APPROVED by Cameron 2026-07-12** ✅ — Machine C. Stills-only, 8 stills, Jesus only bookend storyteller from behind (all 3 verified face-safe; s8 face-fixed). [▶ watch](media-production/build-20-samaritan/luke-10_samaritan.mp4) (21.5MB, 3:22) |
| 24 | The Sower (Matthew 13) | matthew-13_sower | **BUILT — awaiting Cameron** 🟡 — Machine C. Stills-only parable, 7 stills, verbatim captions, Jesus only bookend storyteller from behind (both verified face-safe; s1 & s7 face-fixed). [▶ watch](media-production/build-24-sower/matthew-13_sower.mp4) (21.3MB, 2:56) |
| 21 | The Lost Sheep (Luke 15) | luke-15_lost-sheep | **APPROVED by Cameron 2026-07-12** ✅ — Machine A (Dev). Stills-only parable, Jesus fully off-screen (voice + KJV only; face-gate PASS). 7 stills (Machine C art on shared prep), verbatim captions, KJV j1–j4 (Luke 15:4/5/6/7). Cameron fix: narrator says "ninety-nine" cleanly; Jesus keeps exact KJV "the ninety and nine". luke-15_lost-sheep.mp4 (20.2MB, 2:47). |
| 22 | The Unmerciful Servant (Matthew 18) | matthew-18_unmerciful-servant | **BUILT — awaiting Cameron** 🟡 — Elli's Windows laptop, Cameron's direct order 2026-07-12. Stills-only parable, face-gate PASS (the Lord only in s1 from behind; s2–s8 no Jesus figure). 8 painted stills, verbatim captions, KJV j1 (18:22) + j2 (18:35) italic-cream; bed silent under the king's compassion + j2. Ear-check all-pass. [▶ watch](media-production/build-22-unmerciful-servant/matthew-18_unmerciful-servant.mp4) (21.5MB, 4:05) |
| 23 | Workers in the Vineyard (Matthew 20) | matthew-20_vineyard-workers | **APPROVED by Cameron 2026-07-12** ✅ — Machine A (Dev). Stills-only parable, Jesus fully off-screen. 8 stills, verbatim captions, KJV j1 (Matt 20:13-15, "Is thine eye evil, because I am good?") + j2 (20:16). matthew-20_vineyard-workers.mp4 (21.1MB, 3:23). |
| 25 | Wheat and Tares (Matthew 13) | matthew-13_wheat-and-tares | **APPROVED by Cameron 2026-07-12** ✅ — Machine A (Dev). Stills-only parable, Jesus fully off-screen. 8 stills, verbatim captions, KJV j1 (13:29-30) + j2 (13:43). Patience-is-mercy framing. matthew-13_wheat-and-tares.mp4 (20.7MB, 3:16). |
| 29 | The Pearl of Great Price (Matthew 13) | matthew-13_pearl-of-great-price | **BUILT — awaiting Cameron** 🟡 — Machine A (Dev). Stills-only short parable, Jesus fully off-screen (voice + KJV only; face-gate PASS). 6 fresh painted stills, verbatim captions, KJV j1 (13:45) + j2 (13:46) cream-italic. Closing "Jesus is good" turn: to him, YOU are the pearl he sold all to buy. Ear-check 13/13; hush after j2, no other dead air. **FIX 2026-07-13 (Machine A): s2-searching regenerated — the earlier render left the merchant's left sleeve ending with no hand; both hands now shown, rebuilt.** matthew-13_pearl-of-great-price.mp4 (20.0MB, 2:32). |
| 30 | The Net / Dragnet (Matthew 13) | matthew-13_the-net | **BUILT — awaiting Cameron** 🟡 — Machine A (Dev). Stills-only parable, Jesus fully off-screen (voice + KJV only; face-gate PASS). 6 fresh painted stills, verbatim captions, KJV j1 (13:47-48) + j2 (13:49) cream-italic. Milk framing: the net gathers "of every kind" (grace cast wide, comes first); sorting is God's alone at the end, not ours (furnace kept off-screen). Ear-check 14/14; hush after j2, no other dead air. matthew-13_the-net.mp4 (20.6MB, 3:02). |
| 33 | The Sheep and the Goats (Matthew 25) | matthew-25_sheep-and-goats | **BUILT — awaiting Cameron** 🟡 — Machine A (Dev), Cameron's direct order 2026-07-12. Stills-only, the King (Jesus) kept fully off-screen (voice + KJV only — face-gate PASS). 7 painted stills (shepherd from behind dividing the flock → feed the hungry → welcome the stranger → clothe the cold & tend the sick → visit the prisoner → an ordinary woman helping a beggar child → a hand giving bread & a cup). s6 was regenerated as an ordinary woman after the first render read too much like a Christ-figure. Verbatim captions, KJV j1 (25:34-36) + j2 (25:40 "ye have done it unto me") cream-italic, hush on j2. Milk: he hides in the needy; simple mercy reaches him; the punishment side kept gentle. Ear-check 12/12. [▶ watch](media-production/build-33-sheep-goats/matthew-25_sheep-and-goats.mp4) (19.9MB, 3:02) |
| 28 | Hidden Treasure (Matthew 13) | matthew-13_hidden-treasure | **BUILT — awaiting Cameron** 🟡 — Elli's Windows laptop, Cameron's direct order 2026-07-12. Stills-only parable (Matthew 13:44), NO Jesus figure (face-gate PASS). 7 painted stills, verbatim captions, KJV j1 (13:44) italic-cream; bed silent under j1. Ear-check all-pass. [▶ watch](media-production/build-28-hidden-treasure/matthew-13_hidden-treasure.mp4) (20.9MB, 1:57) |
| 27 | The Leaven (Matthew 13) | matthew-13_leaven | **BUILT — awaiting Cameron** 🟡 — Machine C (Cameron's direct order "go to 27"). Stills-only one-verse parable (13:33), NO Jesus figure (voice + KJV only). 7 painted stills (woman hides leaven → three measures → kneads → covered/waiting → risen → baked → bread shared with many), verbatim captions, KJV j1 (13:33) cream-italic, silence on the risen-dough peak. [▶ watch](media-production/build-27-leaven/matthew-13_leaven.mp4) (20.5MB, 2:05) |
| 32 | The Talents (Matthew 25) | matthew-25_talents | **BUILT — awaiting Cameron** 🟡 — Machine C (Cameron's direct order "do 32"). Stills-only parable (25:14-30), NO Jesus figure (the master is a parable nobleman shown fully). 7 painted stills (entrusting → 5-bag trades → 2-bag works → 1-bag buries it at night → return/reckoning → "well done" embrace → the buried bag returned in sorrow), verbatim captions, KJV j1 (25:21 "Well done… enter into the joy") + j2 (25:24-25 the fearful excuse), silence on the "well done" peak. Milk framing: the third servant buried the gift because he believed a LIE about the master's heart; God is not that hard man. [▶ watch](media-production/build-32-talents/matthew-25_talents.mp4) (20.9MB, 2:45) |
| 35 | The Great Banquet (Luke 14) | luke-14_great-banquet | **BUILT — awaiting Cameron** 🟡 — Machine C (Cameron's direct order "35 is next"). Stills-only parable (14:15-24), NO Jesus figure (the host is a parable nobleman). 7 painted stills (feast ready → servant sent → the excuses → servant returns → sent to the streets → welcoming the poor → the table full & the host with arms wide), verbatim captions, KJV j1 (14:21) + j2 (14:23) cream-italic, silence on the "house filled" peak. Milk framing: when the invited make excuses, the host opens the doors WIDER to the poor/maimed/blind — God's answer to rejection is MORE invitation, and there is still room for you. [▶ watch](media-production/build-35-great-banquet/luke-14_great-banquet.mp4) (20.9MB, 2:35) |
| 26 | The Mustard Seed (Matthew 13) | matthew-13_mustard-seed | **BUILT — awaiting Cameron** 🟡 — Elli's Windows laptop, Cameron's direct order 2026-07-12. Stills-only parable (Matthew 13:31-32), NO Jesus figure (face-gate PASS). 6 painted stills (seed in palm → sown → sprout → shrub → great tree → birds nesting), verbatim captions, KJV j1 (13:31-32) italic-cream split over two beats; bed silent under j1; seed→tree callback at the close. Ear-check all-pass. [▶ watch](media-production/build-26-mustard-seed/matthew-13_mustard-seed.mp4) (20.8MB, 1:42) |
| 37 | The Rich Man and Lazarus (Luke 16) | luke-16_rich-man-lazarus | **BUILT — awaiting Cameron** 🟡 — Elli's Windows laptop, Cameron's direct order 2026-07-12. Stills-only parable (Luke 16:19-31), NO Jesus figure (face-gate PASS). 8 painted stills (feast in purple & fine linen → Lazarus at the gate w/ dogs → the rich man passing by → angels carry Lazarus to Abraham's side → the rich man in torment reaching across the gulf → the great gulf fixed w/ Abraham & Lazarus in light → the five brothers heedless → someone stopping to feed the beggar at the gate). Verbatim captions, KJV j1 (16:25 Abraham "Son, remember…") + j2 (16:31 "…neither will they be persuaded, though one rose from the dead") italic-cream; bed silent under both KJV lines. Torment handled tastefully (dry shadowed gulf, NO fire). Ear-check 17/17. Milk framing (the gate/the person you walk past; today is the day). [▶ watch](media-production/build-37-rich-man-lazarus/luke-16_rich-man-lazarus.mp4) (21.2MB, 2:46) |
| 31 | The Ten Virgins (Matthew 25) | matthew-25_ten-virgins | **BUILT — awaiting Cameron** 🟡 — Elli's Windows laptop, Cameron's direct order 2026-07-12. Stills-only parable (Matthew 25:1-13). 7 painted stills (set out → wise vs foolish → all asleep → midnight arrival → oil can't be shared → the ready go in → shut out). Ten bridesmaids' faces shown; the bridegroom (represents Christ) shown reverently at a distance (s4) / from directly behind (s6), face never shown — face-gate PASS, verified in render. Verbatim captions, KJV j1 (25:13) italic-cream; bed silent under j1. Ear-check all-pass. **FIX 2026-07-13 (Machine A): s3 (all asleep) regenerated — earlier render stuck 3 oil-lamps onto the vertical wall; now every lamp rests on the ground, wall bare. Also upgraded s3 1K→2K and made build.py cross-platform so it rebuilds on Linux.** [▶ watch](media-production/build-31-ten-virgins/matthew-25_ten-virgins.mp4) (20.9MB, 2:28) |
| 34 | The Rich Fool (Luke 12) | luke-12_rich-fool | **BUILT — awaiting Cameron** 🟡 — Elli's Windows laptop, Cameron's direct order 2026-07-12. Stills-only parable (Luke 12:16-21), NO Jesus figure (face-gate PASS). 7 painted stills (great harvest → no room → build bigger barns → feasting alone → the night summons → goods remain/owner gone → the generous farmer "rich toward God"). Verbatim captions, KJV j1 (12:20 God's "Thou fool") + j2 (12:21 seal) italic-cream; bed silent under both divine lines. Ear-check all-pass. Milk framing (hopeful generous close). [▶ watch](media-production/build-34-rich-fool/luke-12_rich-fool.mp4) (21.5MB, 2:11) |

After Wave One (1–20), the full 200-story plan and each machine's ranked queue
live in [`media-production/VIDEO-ASSIGNMENTS.md`](media-production/VIDEO-ASSIGNMENTS.md).

---

## 📈 Count

- **Built + APPROVED + LIVE:** 16 (01–15 and 17) — approved by Cameron and deployed to Firebase Hosting 2026-07-11; streaming in the app.
- **In progress (building fresh):** 1 (16 Mary and Martha — stills 5–6 + assembly).
- **Not started (Wave One):** 3 (18–20).
- **Total in the plan:** 200.
