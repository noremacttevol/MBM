# QC / RUNNER HANDOFF — build-198-ensign-for-the-nations

**Row 198 · Isaiah 11:10-12 · "he shall set up an ensign for the nations, and shall assemble
the outcasts of Israel, and gather together the dispersed of Judah from the four corners of
the earth."**
State: **AUTHORED / Ready ✅** (picture map authored, `--check` PASS 0 warnings). Audio complaint
now fixed at $0 (see ledger). Fable-5 author lane, Machine A `Dev`, 2026-08-07.

---

## COMPLAINT LEDGER — OPEN complaint AUDIO-FIXED at $0 (2026-08-07, Machine A `Dev`)

- **OPEN Cameron complaint (`v2_outline.py 198`): "Not new audio."** — VALID. Root cause:
  STALE-V1 stream-copy. The delivered V1 mp4 (`media-production/build-198-.../isaiah-11_ensign-for-the-nations.mp4`,
  dated **2026-07-23 06:56**) PREDATES the ElevenLabs re-voice and stream-copied the old-voice
  track. But the V1 build's `audio/` holds **7 new-voice ElevenLabs segments** (n0, n1, s1, s2,
  n2, n3, card), all dated **2026-07-29 09:47**, ffprobe-confirmed 44100 Hz / 128k mono —
  identical spec to the already-fixed row 191, and logged in `audio-eleven.log` via the
  ElevenLabs backend (`.audio-eleven-done` marker present).
- **FIX ($0, no image gen, no re-voice):** set `AUDIO_FROM_V1_SEGMENTS = True` (module level in
  beats_v2.py, after the docstring). `v2_assemble` now rebuilds the shipped track from those 7
  new-voice segments instead of copying the stale mp4 audio. Same sanctioned exception as rows
  191/177/78/80/82. `--check` PASS (12 beats), windows contiguous.
- **🅿️ RUNNER — do this:** this row has 0 stills, so you BUILD it fresh (12 stills, all
  `jesus=False`, NO cream/white — OT prophecy, God/Messiah never embodied; see the HARD GATE in
  beats_v2.py). On assemble, the AUDIO REBUILD path copies the **new voice** (verify AUDIO REBUILD
  PASS). Ship with a review card that tells Cameron **the voice is the real new voice** (closes
  his "Not new audio" complaint). No re-voice — the segments are already correct.

---

## ✅ AUTHOR DONE — 12-beat V2 map, `--check` PASS (0 warnings), windows contiguous 0.000→52.740 (=card)

Fresh movie-coverage beat map. 12 pictures over 52.740 s ≈ 4.40 s/pic. Every onset in-window,
monotonic. Isaiah's prophecy of the root of Jesse who stands as an ensign, and the SECOND-TIME
recovery — the Lord raising a banner so the outcasts of Israel and the dispersed of Judah are
gathered home from the four corners of the earth. RESTORATION cornerstone: the gathering of
Israel, a signal lifted up so the scattered can find their way.

Beat spine:
- b01 Isaiah points far ahead (**establishing, ISAIAH-HEIGHT promote**) · b02 the root of
  Jesse = **a green shoot from an old cut stump** (insert, NO figure — Isaiah 11:1 metaphor)
- b03 stand as a banner (the ensign run up the pole) · b04 raised high, not hidden, for all to
  see (low-angle hero shot of the banner against the sky)
- b05 **s1 SCRIPTURE (blue)** "the Lord shall set his hand again the second time" (exiles set
  out, GATHERING-ROADS promote) · b06 **s1 blue** "to recover the remnant" (a remnant journeys)
- b07 **s2 SCRIPTURE (blue)** "set up an ensign for the nations" (banner + nations turning to
  it) · b08 **s2 blue** "assemble the outcasts of Israel" (a lone outcast drawn in) · b09 **s2
  blue** "gather the dispersed of Judah from the four corners" (roads converge from every way)
- b10 exiles brought home (fuller road, home in view) · b11 the ensign is the invitation, the
  gathering His work (climbing the last road to the banner) · b12 closing — the seeking ones
  come home (arriving in the home valley, HOMELAND promote)

**SPEAKER LAW (OT prophecy, Isaiah):** s1 (11:11) and s2 (11:12) = SCRIPTURE → **light-blue**;
n0/n1/n2/n3/card narrator → white. **NO God-voice segment, NO red-letter. NO Jesus / NO cream /
NO white** anywhere.

**HARD GATE — GOD & THE MESSIAH NEVER EMBODIED.** "the root of Jesse", "nations could find
their way to Him", "the Lord shall set his hand again" are NEVER a figure/face/hand-from-sky/
beam/symbol. The **root of Jesse is Isaiah's own metaphor — a green shoot from an old cut
tree-stump (b02), NO person in that frame.** "Him"/the invitation is carried by the **ENSIGN —
a real plain cloth banner on a pole** (an object, not a divine figure); the banner carries NO
rendered writing/emblem. The "second time" recovery and the gathering are carried by **real
exiles coming home**. Drift-word gate clean in all scene text.

**CONTENT-CARE:** the outcasts/dispersed (b06/b08/b09/b10) are weary-but-hopeful travellers
with dignity — never misery, squalor, chains or gore; the gathering is an invitation answered,
glad, never a forced march. b09 shows no map/compass (the "four corners" is roads converging).

**TIME-OF-DAY:** bright warm daylight throughout, so the raised banner reads against the sky
and the roads home are plainly seen. Not night; no divine light.

---

## 🅿️ RUNNER — build the 12 stills (0 exist today)

**Places:**
| Place | Source | Promote |
|---|---|---|
| ISAIAH-HEIGHT | NEW | **promote b01** → reuse b02 (stump insert), b03, b04, b07. Keep the SAME banner + pole + stump across all these frames. |
| GATHERING-ROADS | NEW | **promote b05** → reuse b06, b08, b09, b10, b11. Keep the distant banner-on-the-skyline consistent. |
| HOMELAND | NEW | **promote b12** |

`git add -f build-198-ensign-for-the-nations/PLACE-REF/*.jpeg` after promoting.

**Gates before assembly:**
- Face/beard board on **ISAIAH** (SAME grey-bearded prophet b01/b03 — matches build-192's
  ISAIAH lock; NOTE two Isaiah locks exist in the tree, 175 vs 192, and this row uses **192's**
  — flag if a built 175/192 disagrees so Cameron's Isaiah stays one man). Keep GATHERED-EXILES
  **distinct** faces, not clones.
- SCALE gate (ordinary-sized people, one head each).
- **Sacred-figure gate — GOD/MESSIAH NEVER EMBODIED**: b02 is a stump + shoot with **NO
  person**; the ensign is a plain banner with **nothing written on it**; no figure/hand/beam
  anywhere; b05 no hand-from-sky for "the Lord shall set his hand."
- Consistency gate: the SAME banner (colour, shape, blank) and the SAME green home valley
  across the reused frames; the distant skyline banner in the road frames matches the height's
  banner.
- Content-care gate: exiles dignified/hopeful, not wretched; no chains/gore; b09 no map.
- Realistic-only Law 14 (no cartoon/mixed frame); NO ONE in cream/white; no modern object,
  road, vehicle, pole-line or rendered writing anywhere.

**Audio:** default AUDIO LOCK stream-copy (byte-identical narration; no re-voice). Assemble,
light-QC per the gates above, then ship.

---

## 🛠 REVIEW CARD (for Cameron)
Isaiah 11 — realistic V2. The root of Jesse (a green shoot from an old stump), a banner raised
high on the height so the nations can find their way, and the SECOND-TIME gathering: the
outcasts of Israel and the dispersed of Judah brought home from the four corners of the earth.
God and the Messiah are never pictured — the ensign is a real banner, the gathering is real
people coming home. No open complaint on this row.
