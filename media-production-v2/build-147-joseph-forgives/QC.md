## ✅ AUDIO-FIX UNBLOCKED — STALE-V1 resolved — 2026-08-11, Machine A `Dev`, audio lane

**`AUDIO_FROM_V1_SEGMENTS = True` set in `beats_v2.py`.** Root cause: the V1 final
mp4 (2026-07-24) predates the re-recorded narration — all 11 V1 segment mp3s are
NEWER (2026-07-28) and are the correct ElevenLabs new-voice takes (verified
44100 Hz / 128 kbps), but the runtimes matched within 0.015 s so the *newer-mp3*
tripwire (not the duration guard) refused to copy the stale mp4 AAC. Fix rebuilds
the track from the V1 build's OWN mp3s at the extract_beats offsets — **no re-voice
($0), no still regen** (16 realistic stills already FULL-CUT-clean).

- Verified in isolation: `rebuild_audio_from_segments` → **AUDIO REBUILT 96.591 s,
  guard |total−track| = 0.0 (PASS)**.
- **Not shipped this turn on purpose:** a live *local* autopilot assemble lane was
  churning this row (partial `segs/video_silent.mp4` @ 17:34) in the shared working
  tree; running a parallel `v2_assemble` + deploy would corrupt its `segs/`. With the
  flag now set, the next audio/runner tick assembles → **AUDIO REBUILD PASS** →
  FULL-CUT GATE → ships (deploy + live-verify) in ONE touch. Pure mechanical STALE-V1
  fix (row-118/200/143/144/145 template).

---

## 🅿️ RUNNER PARK → NEEDS-AUDIO (2026-08-11, Machine A `Dev`, Opus runner)  *(resolved above)*

**All 16 V2 realistic stills are DONE + FULL-CUT-clean on disk — do NOT regen
(row-118/141 template).** Blocked at the AUDIO LOCK: the V1 final mp4
(`genesis-45_joseph-forgives.mp4`, rendered 2026-07-24) predates the re-recorded
narration — **11 of 11 V1 mp3s are NEWER (2026-07-28)** than the mp4, so copying
its audio would ship stale voices. (Duration matched to 0.015s — this was caught by
the newer-mp3 tripwire, NOT the duration guard; see lesson.)

**AUDIO LANE — RESUME (row-118/200 template, expected $0/no re-voice):**
1. Voice-ID the segments (confirm the 2026-07-28 re-record is the chosen ElevenLabs
   cast; Joseph's two KJV lines Gen 45:5 / 50:20 are in the SCRIPTURE voice per the
   build-161 precedent).
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `build-147-joseph-forgives/beats_v2.py`.
3. `python3 media-production-v2/v2_assemble.py 147` → **AUDIO REBUILD PASS** (~96.6s).
4. Hand back to the picture runner: FULL-CUT GATE §6b (transcribe + caption↔timing.json
   diff per row-131) → ship + deploy + live-verify. The 16 stills are already gated.

**The 16 stills, FULL-CUT-QC'd 2026-08-11 (0 rerolls, ~$2.27):** all realistic
biblical Egypt, HALL plate consistent (b02-b07,b10), JOSEPH face consistent across
all his frames + correct aging (grey at temples b12/b14), no Jesus in this OT story
(cream rule N/A), correct hands/anatomy incl. the b16 group embrace, period props only
(granary sacks, clay jars, spears, scrolls, baskets, grain), leprosy/gore N/A, natural
scale throughout. Nothing to reroll.

---

# QC / RUNNER HANDOFF — build-147-joseph-forgives (Gen 45; Gen 50)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 16 beats, ~91 s.

## The selling (b01) — distance and aftermath only

Far caravan + tiny ridge-knot of brothers at harsh noon. NO pit, NO
struggle, NO violence, ever — automatic reject.

## Joseph's costume exception (note for the reviewer)

Joseph wears WHITE-LINEN Egyptian vizier dress + gold collar — a
deliberate, documented exception to the no-pale-cloth rule (Egyptian
office costume; this is not a Jesus-cream conflict — no Jesus in
this row). Warmth always visible under the authority. Three ages:
young-at-distance (b01), vizier ~40 (b02-b11), older ~55 (b12-b16)
— face-board the ageing for continuity.

## The brothers are TEN (counts law)

Ten in every group frame (b03, b05, b06, b07, b12, b16's embrace-
knot). Varied, weathered, guilt-worn — never villains. Their arc:
bowed-unknowing → frozen terror → unclenching (b08) → sob released
(b11) → older fear (b12) → embraced (b16).

## The row's spine: truth-telling forgiveness

The evil is NAMED plainly (b05/b06/b14 — "sold", "you meant it for
evil") and forgiven with the name intact. No soft-focus mercy;
honesty and warmth share one face. b13's two-hands composition:
one toward the brothers (evil named), one toward the fed land
(good meant).

## The rescue (b10/b15)

Full granaries, moving bread lines, children eating — the FED,
never the famished; no starvation imagery.

## Coverage shape

One true wide with stated geometry: b02 (camera up the painted
hall past the petitioners' backs). No Jesus beats (OT row). File
order = story order. b04's clearing: orderly exits, tension
climbing.

- Plates: HALL --take from build-22 REJECTED (parable king's hall ≠
  Egyptian painted-column hall; the 86/63 decline precedent). HALL
  promote-first from b02.

## C-FIX 2026-08-13 (Machine A `Dev`, Opus runner) — Joseph character-consistency complaint

**Cameron's complaint (COMPLAINTS.md row 147, status "newer cut shipped — VERIFY fixed"):**
> "Joseph should be the same character and same look as before, different hair
> maybe but same face definition. We should have the story of Joseph and this
> story looking the same. Match the characters and redo this one if you must."

**Domain:** PICTURE (character identity/consistency). No timestamp given — a
global identity complaint, so it traces to every Joseph appearance, not one
frame.

**PROMPT AUTOPSY (rubric meta-law 3): verdict = ALLOWED-then-FIXED.**
The complaint was filed against the OLD cartoon `ASSEMBLY-C` cut (7 reused
W1 stills, 2026-07-17), where Joseph's face drifted frame-to-frame (cartoon
era, mismatched stills). Root cause: cartoon assembly reused non-matching
stills with no single locked face → Joseph read as different men. The
realistic-V2 rebuild (16 native-2K stills, JOSEPH text-lock, 2026-08-11/12)
already replaced that with ONE canonical Joseph. This C-FIX VERIFIES the
current live cut per the COMPLAINTS.md rule ("newer cut shipped — VERIFY the
complaint is truly fixed in the CURRENT cut").

**FULL-CUT GATE (6b) — all 16 beats, viewed from BOTH the source stills AND
the RENDERED mp4 (ffmpeg mid-window extracts 7.7 / 22.3 / 48.6 / 71.8 / 80.4
/ 87.7 s + the 4x4 contact sheet):** PASS.
- Joseph is one consistent man in every frame: clean-shaven Hebrew-Egyptian
  vizier, dark curly hair, warm dark eyes, olive skin, white-linen + gold
  collar. The 1:20 portrait (s14 / b14) is essentially the CAST-REF-V2
  joseph.jpeg itself. Seated dais (s02/s03), standing reveal (s05), reaching
  (s09/s10), doorway (s13), embrace (s16) all match the reference — only age
  and expression change, never the face. Cameron's "different hair maybe but
  same face definition" is satisfied.
- The ten brothers: consistent weathered first-century faces across group
  frames; guilt-worn, never villains.
- Realistic-only (Law 14) PASS — zero cartoon/mixed frames. Anatomy/hands
  clean (s08 hand-on-chest 5 fingers; s09 reach OK). No modern objects
  (granary s15 = period sacks/bread/baskets, alive not "dead crowd"). No
  Jesus in this OT row. Captions bottom-band, scripture (Joseph's KJV
  Gen 45:4 / 50:20) styled cream/blue, narrator white — in sync.

**Action taken:** VERIFY-ONLY, $0, 0 Gemini rerolls. The pictures are already
on-model against the cast-ref; regenerating on-model frames would violate the
COST LAW / "don't chase subtle drift" rule and risk NEW drift. The realistic
V2 already answers the complaint. Reviewer card updated to tell Cameron his
complaint was addressed (in his words) so he can re-review and approve. mp4 is
unchanged (already the fixed cut, live-served bytes == local, 20,294,602 B).

**FACE-BOARD note for any future touch:** Joseph's beats currently anchor
identity by TEXT lock (ref:False). The results are consistent, but if this row
is ever regenerated — or when the future "story of Joseph" (the coat/dreams/
sold-into-Egypt arc) is built — attach `CAST-REF-V2/joseph.jpeg` to every
Joseph beat as the image anchor (FACE-BOARD LAW) so both videos share the exact
same face. joseph.jpeg IS the canonical Joseph.

**COMPLAINT LEDGER:**
- row 147 "Joseph should be the same character / same face definition, match
  the story of Joseph" → FIXED in realistic-V2 (verified this session): one
  canonical clean-shaven Joseph in all 16 frames, matching CAST-REF-V2/
  joseph.jpeg; the 1:20 close-up is the reference face. Full-cut gate PASS.
