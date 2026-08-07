# QC / RUNNER HANDOFF — build-175-mountain-of-the-lords-house

Row 175 · Isaiah 2:2-3 ("the mountain of the LORD's house shall be established in
the top of the mountains... and all nations shall flow unto it"). RESTORATION
shelf (the house of the Lord / gathering of the nations). Authored fresh
2026-08-07 (Machine A `Dev`, Fable-5 author lane, $0).

## COMPLAINT LEDGER
- **No open Cameron complaint.** `v2_outline.py 175` shows none. First-time V2
  picture map on the already-authored SPEAKER-LAW narration (audio OK).

## SPEAKER LAW + GATES (verified)
Isaiah — s1/s2a/s2b are the SCRIPTURE voice → **LIGHT-BLUE** captions; the
narration itself says "That is Isaiah writing, NOT God speaking," so there is **NO
red-letter and NO God-voice.** **GOD IS NEVER EMBODIED** — no figure/face/hand/beam
anywhere; his teaching "going out" (b11/b14) is carried by PEOPLE, shown as natural
light. **NO Jesus and NO cream anywhere.** `--check` v4 PASS, no warnings.

## CONTENT-CARE
The "house of the LORD" is a grand **ANCIENT** stone temple exalted on a mountain
(credible first-century-world biblical architecture, in the manner of the Jerusalem
temple) — **NEVER a modern building and NEVER a specific real present-day temple.**
"All nations" are diverse peoples of the ANCIENT world in varied period dress —
never modern clothing, flags or signage. "Not summoned by force" (b12): NO
soldiers/weapons/chains. No rendered writing anywhere.

## Cast (build-local locks)
- **ISAIAH** — dignified prophet, dark greying beard, deep-toned robes (b06 only;
  beholding the vision, hand lifted, NOT God).
- **NATIONS-PILGRIMS** — the diverse ancient-nations crowd. **This is a text
  CROWD/CAST lock, NOT a location** — even though `v2_stash.py --wire` lists it
  among "NEW PLACES," do NOT treat it as a place. (Optional: the runner may
  `--promote` b05 as a crowd anchor to steady the diverse crowd across frames, but
  it is not required and PLACE_REFS is intentionally empty for it.)

## Places (both NEW build-local — these are the only real locations)
- **MOUNTAIN-TEMPLE** — the summit house of the Lord (b01-b04, b09, b11, b14).
- **MOUNTAIN-PATH** — the ascending roads / nations streaming (b05-b08, b10, b12,
  b13, b15).

## 🅿️ RUNNER — build steps (paid image lane)
1. **Generate b01 first** (MOUNTAIN-TEMPLE establishing wide, the mountain at
   dawn). QC (ancient architecture, NOT modern/real temple, no writing). Promote:
   `python3 media-production-v2/v2_stash.py --promote build-175-mountain-of-the-lords-house MOUNTAIN-TEMPLE build-175-mountain-of-the-lords-house/assets/s01-the-mountain-at-dawn.jpeg`
2. **Generate b05 next** (MOUNTAIN-PATH establishing wide, nations streaming up).
   QC (diverse ancient peoples, no modern dress/flags). Promote:
   `python3 media-production-v2/v2_stash.py --promote build-175-mountain-of-the-lords-house MOUNTAIN-PATH build-175-mountain-of-the-lords-house/assets/s05-all-nations-flow.jpeg`
3. Re-run `v2_stash.py --wire build-175-mountain-of-the-lords-house` (take the two
   PLACE plates; ignore/decline the NATIONS-PILGRIMS suggestion as a place), then
   `--check` (PASS) and `--dump`.
4. Generate the remaining beats against the plated places.
5. **Gates:** SACRED-FIGURE gate by eye on every beat — NO God figure/beam
   anywhere (esp. b06/b11/b14). Architecture gate: temple stays ancient/biblical,
   never modern or a real present-day temple. Crowd gate: ancient period dress
   only, no modern/flags. ISAIAH consistent on b06. Scale: everyone
   ordinary-sized. (No `jesus_face_gate` beats — no Jesus in this row.)
6. Assemble (AUDIO LOCK — narration authored + OK, byte-identical; do NOT
   re-voice). Re-audit, ship. No open complaint, so the card just presents the cut.

## Coverage / windows (authored, verified)
15 beats, windows contiguous 0.400 → 73.306 (= card_start), monotonic, each
segment's speech onset inside its window. ~4.9 s/picture. `--check` v4 PASS.
