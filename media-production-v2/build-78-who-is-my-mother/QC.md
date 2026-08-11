# QC / RUNNER HANDOFF — build-78-who-is-my-mother (Mark 3:31-35)

## ✅ QC-VERIFY — FULL-CUT GATE (§6b) BEFORE CAMERON'S EYES — Machine A `Dev`, 2026-08-11 — CLEAN, no re-cut

Row 78 was BUILT and sitting in Cameron's Unwatched queue. Per PROMPT-OPUS-RUNNER §6b
(born from row 11 reaching him with 7 bad frames), ran the full-cut gate BEFORE he
watched it — a VERIFY pass, no fresh build. Extracted ONE frame per beat from the
RENDERED mp4 at each c000–c011 segment MIDPOINT (real segment durations, not the raw
beat windows) + the closing card + a scripture-caption frame (16.5s). Viewed all 14
against the defect checklist + RUNNER-LESSONS + this row's laws.

**Frame-by-frame verdict (all CLEAN):**
- s01 (packed house): Jesus cream-only, olive skin/dark wavy hair/full beard, only-Jesus-cream holds; realistic; caption white narrator. ✓
- s02 (family without): bright-exterior street (light law), mother-Mary in blue mantle, dignified/loving (NOT resentful), brothers distinct men; no Jesus/no cream. ✓
- s32 scripture (16.5s): caption **blue** "Behold, thy mother and thy brethren without seek for thee." — SPEAKER-LAW color correct. ✓
- s04 (relay close-up): message-relay reads correctly (not romantic); Jesus reads slightly light-eyed — KNOWN baked-in JESUS-MASTER-REF trait, RUNNER-LESSONS do-not-reroll, whole-wave item not a per-row defect. ✓
- s05/s07 (interior): Jesus cream-only, identity consistent, white narrator captions. ✓
- s06/s09/s10 (Jesus KJV): captions **red** (SPEAKER-LAW), natural gestures. ✓
- s08 (the ring): mother-and-child present in the circle as the beat requires ("mothers, a child"). ✓
- s10 (whosoever): mother-Mary at the doorway, hand on chest, serene/patient — never resentful; geometry (doorway = meeting point) held. ✓
- s11 (exterior): bright-exterior street, mother warm/dignified, brothers distinct; narrator white paraphrase caption. ✓
- s12 (opening the circle): interior, Jesus cream, ring incl. mother+child; white narrator caption. ✓
- card: cream card, serif brown, centered "He drew the family line around whoever would come. That door is open to you too." — no tofu/square glyphs. ✓

Inside/outside geometry + light law held (dim warm interior vs hard-bright exterior, doorway the only meeting point). Cream-only-Jesus holds EVERY frame. No modern object, no lens-stare, anatomy/scale/beards consistent, fully realistic (Law 14 PASS, zero cartoon). **No open Cameron complaint on this row** (COMPLAINT LEDGER: none open — QC below) so nothing to regress.

**Served-bytes proof:** live card v78 data-hash `573fb16a…`; served mp4 md5
`98920bc6ff5ca5ddfa0f17815893b147` == local md5 (HTTP 200). Cameron watches exactly
what was QC'd. Board row 78 Claim: QC-VERIFY LIVE → **QC-OK 2026-08-11**.
**$0** (ffmpeg/ffprobe/curl only), 0 pictures touched, 0 rerolls. NO re-cut on a clean row.

---


## ✅ AUDIO FIX DONE — AUDIO-FIX session, Machine A, 2026-08-06 ($0)

**STALE-V1 audio-lock CLEARED.** Added `AUDIO_FROM_V1_SEGMENTS = True` to
beats_v2.py. The V1 mp4 `media-production/build-78.../mark-3_who-is-my-mother.mp4`
(09:47) is older than all 11 re-voiced segment mp3s (2026-07-29 23:03), so
`assert_v1_final_is_current` (recency tripwire) refused to copy its stale AAC —
the same class as the shipped row-69 fix. With the flag set, v2_assemble
rebuilds the narration from the V1 build's OWN 11 new-voice mp3s at the
extract_beats offsets — nothing re-voiced, nothing re-timed, V1 stays read-only.

**Segment parity 11/11 exact** (n0, n1a, n1b, n1c, s32, j1, n2, j2, j3, n3,
card) across make_narration.py ↔ media-production-v2 audio ↔ V1 build audio.

**Validated:** `python3 v2_assemble.py 78` now clears the audio gate and stops
only on "missing picture … row not fully generated" (0 V2 stills) — i.e. the
STALE-V1 AUDIO LOCK no longer fires. `v2_prompt.py 78 --check` PASSES (12 beats).

**No visual ship** (0 stills, no ElevenLabs, $0). Board: NEEDS-AUDIO →
AUTHORED / Audio OK / Ready ✅, claim cleared → the picture runner generates
stills and assembles on the corrected (new-voice) audio. RESUME below still
applies.

---

## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 spent, 0 credits) — RESOLVED ABOVE

Pre-flighted the stale-V1 AUDIO LOCK at step 2 BEFORE any generate (row-74
lesson). GENUINELY STALE: V1 `mark-3_who-is-my-mother.mp4` rendered
2026-07-24 10:15:29, but all 11 locked mp3s are NEWER (2026-07-28 14:27:49);
timeline total=72.61s vs V1 mp4 dur=77.79s (excess=+5.18s).
`assert_v1_final_is_current` REFUSES → shipping it would carry stale voices.

Runner cannot fix: the assembler's own hint is to set
`AUDIO_FROM_V1_SEGMENTS = True` in this row's beats_v2.py, which is an AUTHOR
audio decision (editing beats_v2.py is outside runner writes; audio-immutability
law). No stills generated — this parks at $0.

**AUTHOR FIX:** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py (renders
narration from the V1 build's OWN mp3s at extract_beats offsets — nothing
re-voiced/re-timed) OR re-render the V1 mp4. Then set Ready ✅ / Audio OK.
**RESUME (after author fix):** `python3 media-production-v2/v2_story_cast.py build-78-who-is-my-mother`
then `v2_gen_api.py build-78-who-is-my-mother --ceiling …` then `v2_assemble.py 78`.


Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 12 beats, ~66 s — a short row.

## THREE-MARYS LAW (from row 49's QC — applies here)

The MOTHER outside is Mary the mother of Jesus. If row 49
(water-to-wine) has an approved mother-Mary frame by build time,
REFS-anchor this row's MOTHER to it; if this row builds first, ITS
approved frame becomes the canon and row 49 + the nativity/passion
rows anchor to it. Never a Bethany-Mary or Magdalene face.

## The inside/outside geometry (the story IS this)

The whole doctrine is spatial: family STANDING WITHOUT in the bright
street; the seated ring WITHIN the lamp-dim packed house; the message
relayed inward; the gaze circuit; the declaration landing on the ring
itself. Four wides with stated geometry hold the two worlds: b01 (the
packed ring from behind its backs), b02 (the family and doorway from
the side — bright street palette), b08 (the gaze circuit from behind
two shoulders), b12 (the whole room from the high corner). Three flips.

- The mother and brothers are NEVER rendered resentful — patient,
  loving concern (the scene texts have it; reject any sour render).
  The declaration honors the ring WITHOUT dishonoring them: Jesus's
  face carries warmth in both directions.
- Light law: hard bright exterior vs warm dim interior — the two
  palettes never bleed; the doorway is the only place they meet (b02).
- Direction (row-83): the message relays INWARD hand to hand (b03) —
  a readable chain; the sweep (b09) covers the RING, not the door.
- BROTHERS: distinct men sharing family resemblance with the mother
  (90/107 + family-likeness).
- HOUSE: Bethany-lane suggested a NINTH time — DECLINED (Capernaum
  packed one-room house). Promote-first from b01.
- Only Jesus wears cream.

---

## ✅ REALISTIC V2 SHIPPED — A-auto Machine A `Dev` (Opus picture runner, UNATTENDED) 2026-08-07

**COMPLAINT LEDGER (LEARNING LAW): none open.** `v2_outline.py 78` shows no
open Cameron complaint on this row; `grep` of media-production/COMPLAINTS.md for
mother/Mark-3/row-78 returns nothing (the only "mother" hit is row 49's
water-to-wine, a different row). First V2 visual build on the already-cleared
new-voice audio, not a complaint fix. Nothing to answer.

**Build.** 12 painted stills at native 2K (V1 had 8), 72.6s, 19.9 MB, 2 portraits
(MOTHER, BROTHERS — REFS wired into beats_v2.py, satisfying the row-52/55
face-lock lesson for the two single characters). Plate: **HOUSE promoted-first
from b01** (the packed one-room Capernaum house) → attached to 11 beats; b11 is
the exterior street beat (no HOUSE lock). Inside/outside geometry held: dim warm
interior (b01/b03/b05-b10/b12) vs bright exterior street (b02/b11), doorway the
only meeting point.

**Audio.** AUDIO_FROM_V1_SEGMENTS=True (author's stale-V1 clear); track rebuilt
from the 11 V1 segment mp3s = 72.606s. AUDIO REBUILD PASS SHA256
7d734e91aae0285af4b14467658a3b26da44293ccb7f5abb79e7791b67d5575b. Decode-clean
(ffmpeg -v error = 0 output). **Row-74 STALE-V1 duration tripwire CLEAR:**
captioned.mp4 = 66.467s ≈ extract card_start 66.448s (Δ0.02s ≪ 0.2s) — the
picture windows did NOT overrun the audio; no tail/card truncation.

**QC / rerolls.** 0 rerolls / 12 = **0%** (≤15% budget). All 12 frames passed the
light-QC bar: only Jesus in cream, no Jesus double on the two jesus:False family
frames (s02/s11 carry no cream and no Jesus), no modern objects, no lens-stare,
anatomy/scale/beards consistent, fully realistic (Law 14 PASS, zero cartoon).
Mother (Mary) dignified/loving in blue mantle every frame (never resentful), no
romantic framing on the s04 two-man relay. THREE-MARYS LAW: this row's MOTHER
frame becomes the mother-Mary canon (row 49 unapproved at build time).
Caption QC PASS: bottom-band white narrator, closing card clean (no tofu/square
glyphs — row-50 defect absent).

**FIX-WAVE (no reroll, per COST LAW):** (1) the HOUSE wide plate propagated its
wide composition onto b05/b06 (authored closer) — several wides (s01/s05/s06/s07/
s09/s12) share a similar frame; a later coverage wave can add tighter singles
(rubric lesson 12 / row-101 plate-propagation class). (2) Jesus reads
green/hazel-eyed in the s04 close-up — baked-in JESUS-MASTER-REF trait, DO NOT
reroll (RUNNER-LESSONS); whole-wave ref item, not a per-row defect.

**Cost.** Gemini this row ≈ **$1.87** (2 portraits $0.27 + 12 stills $1.60),
meter 452.38 → 454.53. FAR under the $6.10 average — COST LAW held hard (0%
rerolls vs 19% baseline; the promote-first plate + reuse kept spend minimal).
