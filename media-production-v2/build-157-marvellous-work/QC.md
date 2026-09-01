# QC / RUNNER HANDOFF — build-157-marvellous-work (Isaiah 29:11-14)

## ✅ COMPLAINT FIX BUILT — 2026-08-17 (Machine A `Dev`, offline lane)

**Cameron:** “42 weird giant picture.”

The old eight-picture cut was not reused. This is a complete 28-picture
realistic-V2 rebuild. The complained 0:42 scripture shot is now three
ordinary-scale adults in one continuous scholar's room: two deliverers, one
seated scholar, the sealed scroll and a small clay oil lamp. There is no giant,
forced-perspective giant, oversized body, or cream garment. The exact rendered
0:42 frame was inspected directly and passed local Qwen vision: all three people
are realistically scaled; the KJV caption is cyan-blue, legible, fully inside
the bottom black band, and does not cover the art.

Source QC rejected and rerolled visible failures before assembly: a two-seal
anchor, the original giant/briefcase complaint frame, a four-panel ceremony,
modern magnifiers/codices/cases, readable pseudo-text, a wax candle, cream
clothing, incomplete seal counts, and closed-versus-open scroll-state errors.
44 total image calls produced the 28 accepted stills (16 required rejection
rerolls, approximately **$5.90**, meter `$724.00` → `$729.90`, under the hard
`$730.00` ceiling). The high reroll count records mandatory first-pass gate
failures rather than optional aesthetic churn.

Final evidence:

- Prompt contract: v4 checklist PASS, 28/28 beats.
- Jesus face gate: PASS (this Old Testament row has no Jesus shots).
- Audio: `AUDIO_FROM_V1_SEGMENTS=True`; all 13 source clips are 44.1 kHz
  ElevenLabs; stale 209.8 s V1 MP4 audio was never reused; AUDIO REBUILD PASS
  SHA `925136487161f1fde750c18c21b3e7aa386a6fcd6bcfffe05af625da413473e2`.
- Finished MP4: full decode PASS; `verify-mp4` PASS; deep `qc_gate` PASS with
  Whisper actually run; no script/audio echo; duration `173.933333` s; size
  `20,219,608` bytes; raw SHA-256
  `d7e2d1b2df50163eaf85e2241d19103a6ac06c024f80604e3a7c0420c67a6592`.
- Full rendered frame-per-beat contact sheet inspected in chronological order:
  28 distinct realistic stills, captions confined to the bottom band, narrator
  white / scripture cyan-blue / God green, sealed-scroll state through the human
  impasse and open-scroll state only after God's promised intervention.
- Finished-audio Whisper transcript covers the complete authored story and
  closing card. Local sheet-level Qwen made false positives (called shallow clay
  oil lamps “wax candles,” called the intentionally opened final-act scroll a
  continuity error, and alleged hand defects disproved at full resolution).
  Those advisory claims were not allowed to override the actual pixels. Its
  dedicated full-size 0:42 inspection returned PASS.
- Reviewer-only publish verified live: candidate `2a6d8240c`, Reviewer wiring
  `3523eb254`, Firebase `879c10b4e6853fba`. Live HTML names Cameron's complaint
  and points to this V2 cut; GitHub-raw bytes equal the local MP4 SHA exactly;
  public `story-videos/157.mp4` remains HTTP 404. Cameron approval remains open.

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 28 beats, ~159 s. The sealed-book row (BRIDGE, kept in
Isaiah's own frame).

## The BOOK is one sealed scroll (prop-board it hardest)

Heavy rolled parchment + dark crossed cords + THREE wax seals — the SAME
object every frame. In some early sealed-state shots it rests on the same worn
open leather carrying wrap; it is never a modern briefcase, buckle or box. State per-beat:
SEALED through b23, OPEN from b24 (cords loose beside UNBROKEN
seals — opened, not broken). Script indistinct always.

## The opening is God's act — light and result ONLY (absolute)

b21: first dawn shaft landing on the still-sealed scroll. b23:
broad dawn, still sealed. b24: simply OPEN in morning light — NO
hands, NO figure, NO mechanism, ever. Any depicted opening
mechanics = reject.

## Both askers are honourable

The SCHOLAR's "I cannot" is honest admission (never a fool); the
PLAIN man's refusal is kind (never mocked). b12 frames them as two
honest limits, equal. Face-board both across their beats.

## Registers and rhymes

- b14/b17 = the row-128 lips/heart register (correct mouths, absent
  eyes, fastidious hollow ceremony).
- b19 = the 151 spent-light rhyme; b26 = spent clay-lamp wick vs risen sun.
- b16: God never embodied — the listening posture only.
- b20: the key-ring fluent in the wrong language.
- b28: kneeling OPEN hands receive the open scroll lowered from
  above frame — receiving, not grasping.

## Coverage shape

One true wide with stated geometry: b01 (camera behind Isaiah's
robed back at the window). No Jesus beats. File order HEAVILY
scrambled (b08 at 20.40s, b16 at 66s, b22 at 152s) — build by
WINDOW.

- Plates: PLAIN auto-wire REJECTED (a PERSON token wrongly matched
  to the build-38 doorway place-frame — note for the stash: person
  tokens should never place-wire). BOOK promote-first from b03.
- One drift-word FAIL ('aglow') caught and fixed pre-ship.

---

## 🅿️ RUNNER PARK → NEEDS-AUDIO — 2026-08-13 (Machine A `Dev`, Opus runner, headless)

**$0 spent. NO stills generated. Parked at the two-part audio PRE-FLIGHT before touching the meter.**

STALE-V1: row-141 class: V1 mp4 stale 209.8s vs current timeline 173.9s (+35.8s) AND 13/13 V1-dir mp3s NEWER (both tripwires fire) — so `v2_assemble`'s AUDIO LOCK refuses (the picture runner copies the V1 mp4's audio; `AUDIO_FROM_V1_SEGMENTS` is unset).

**FIX (audio lane, NOT runner — beats_v2.py is off the runner write-list):**
1. Voice-ID the V1-dir `audio/*.mp3` — confirm new-voice ElevenLabs cast.
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py` (rebuild audio from the newer mp3s, $0, no re-voice).
3. 0 stills exist → hand back to the picture runner: board State NEEDS-AUDIO → AUTHORED, keep Ready ✅, Claim BLANK.

**RESUME (audio lane):** `python3 media-production-v2/v2_assemble.py 157` (refuses until the flag is set).

---

## ✅ AUDIO-FIX DONE → AUTHORED — 2026-08-13 (Machine A `Dev`, audio lane, $0, 0 stills)

STALE-V1 cleared (row-141 class, both tripwires). **Voice-ID:** all 13 placed
V1-dir mp3s (`media-production/build-157-marvellous-work/audio/*.mp3`) ffprobe as
**44100 Hz / 128 k = ElevenLabs new-voice**, and `audio-eleven.log` records all
13 (n1-n8, kv11, kv13a, kv13b [god], kv14 [god], card) cast through the
ElevenLabs pipeline — no edge-tts, no old voice. (The log's "undecided homograph"
notes on n1/n3/kv11 are pre-existing render notes, not a Cameron complaint — no
PRON fix asked for.) The V1 mp4 was BOTH stale-longer (209.8 s vs the current
~159-174 s timeline, i.e. carrying deleted segments) AND older than every mp3, so
the AUDIO LOCK's STALE-V1-FINAL guard fired both tripwires and refused the
packet-copy.

**Fix:** set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py`. Track now rebuilt
from the new-voice mp3s at extract_beats offsets — the stale 209.8 s mp4 stream is
never touched, no re-voice, no re-time, V1 read-only, **$0 (no Gemini, no
ElevenLabs)**. Verified: extract_beats reads all 28 phrases cleanly (159.3 s);
`v2_assemble 157` no longer refuses on the audio lock, it stops only at the
missing stills — the picture runner's job.

**Handed to the picture runner:** board State NEEDS-AUDIO → AUTHORED, Ready ✅,
Claim cleared. When the runner generates the stills, `v2_assemble` rebuilds the
new-voice track via the flag and ships. Nothing else touched.

---

## ✅ C-FIX SHIPPED (2026-08-31, Machine A `Dev`, Claude session)

**COMPLAINT (Cameron):** "0:58 no beard, 1:00 beard, and 1:03 no beard again."

**ROOT CAUSE:** the PLAIN (unschooled) man had a TEXT-ONLY lock with no beard
stated and no face reference — three different actors rendered the one character
(stubble b11 / full beard b13 / clean-shaven b12; b27 drifted too). Rubric
lesson 2/28: a text lock alone is not identity.

**FIX:** canonized b13's fully-bearded man as the anchor (tight face crop that
clearly SHOWS the beard → `CAST-REF-V2/plain.jpeg`), wired `REFS["PLAIN"]`,
added "FULL SHORT DARK BEARD (never clean-shaven, never mere stubble) …
EXACTLY as the attached reference" to the lock, and regenerated b11, b12, b27
with the ref attached (3 gens, $0.40; b13 untouched as the anchor). Face-board
of anchor vs all three regens: one man everywhere. Scroll script in the new b27
checked at full crop — dense period squiggle, indistinct, no legible letters.

**Verified in the ENCODED replacement at 0:58 / 1:01 / 1:03** — the same
bearded man in every frame. AUDIO REBUILD PASS SHA256=9251364871…, 173.9s,
20.1 MB — narration untouched.


## RE-CUT 2026-09-01 — COMPLAINT LEDGER (the understandable ending)
Cameron (chat, then filed): "i dont understand the point... its super confusing
just to show people we may never understand something?" -> "fix it how we
discussed the recut to make it more undersatandable"
- ROOT CAUSE: the cut spent four beats on "nobody can open the book" and ended
  on an abstract promise — it never showed Isaiah's OWN resolution, so the
  takeaway read as "we may never understand" (the opposite of the point).
- FIX (the recut we discussed): Isaiah 29:18 and 29:24 added VERBATIM (Roger,
  scripture voice), a new narrator bridge and a new landing + card (Brian):
  the scroll is OPENED (three wax seals hanging broken), the deaf hear ITS
  words, the PLAIN man who once shook his head now READS it (same locked face),
  the erred come to understanding, and the closing question becomes "when God
  offers to open the book, will you let him?" 10 new beats (b29-b38) authored
  from the fresh extract_beats timeline with distinct camera geometry per
  lesson 26; old ending beats b22/b25-b28 retired. V1 build.py BEATS extended
  (kv18/n7b/kv24) because the V2 timeline iterates it. New segs voiced through
  mbm_eleven.render_segment (never save_speaker_narration — edge-tts trap),
  round-tripped clean through whisper-small.

### SHIP VERIFICATION 2026-09-01 (the recut, encoded-mp4 proof)
- 33 beats + card, 209.0s. AUDIO REBUILD PASS 26916be36976. Encoded tail
  round-trips every new line (kv18/n7b/kv24/n8/card; whisper's dropped
  final-/d/ on "murmured" verified present at render with whisper-small).
- FULL-CUT GATE: 34/34 frames viewed. New ending verified in the encoded cut:
  seals SNAPPED at "does not stay sealed", PLAIN man face-boarded ✓ (ref vs s11
  vs s33 — same locked face), reverse-angle kv24, no rays in s37, card text new.
- Rerolls: s32/s35 (still read sealed -> forced flat-open + snapped halves),
  logged 2/10 = 20% on the new beats (meaning-critical, complaint IS confusion).
- 3 same-motif sealed-scroll pairs (b03/b21/b23) are the prior shipped design,
  verified distinct at full size.
