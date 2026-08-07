# QC / RUNNER HANDOFF — build-189-to-him-that-overcometh

**Row 189 · Revelation 3:20-21 · "Behold, I stand at the door, and knock" + "To him that
overcometh."** State: **NEEDS-AUDIO** (picture map authored & `--check` PASS, but an OPEN
pronunciation complaint must be fixed by the AUDIO lane before Ready). Fable-5 author
lane, Machine A `Dev`, 2026-08-07, $0.

---

## ✅ AUTHOR DONE — 12-beat V2 map, `--check` PASS, windows contiguous 0.000→46.241 (=card)

Fresh movie-coverage beat map written from scratch (NEEDS-BEATS → AUTHORED). 12 pictures
over 46.241 s ≈ 3.85 s/pic. Three registers cut like a short film:

- **DOOR-NIGHT** (exterior, night) — b01 drowsy house (establishing, NON-Jesus), b02
  Jesus knocks gently, b03 "I stand at the door and knock," b06 his open hand resting on
  the door (does not break it).
- **LAMPLIT-ROOM** (warm interior, night) — b04 the man hears (NON-Jesus, Jesus still
  outside), b05 the offered supper, b07 hand lifts the latch (insert), b08 "a seat no
  empire can give."
- **THRONE-GLORY** (radiant heavenly hall) — b09 "sit with me in my throne," b10 "set
  down with my Father in his throne" (Father's throne = pure light, unshown), b11 the
  overcomer before the open seat (NON-Jesus), b12 seated WITH Christ — closing image.

One recurring human = **OVERCOMER** (the "any man" the letter addresses): he hears (b04),
his hand opens the door (b07), Christ offers him supper (b05), and he is the overcomer who
shares the throne (b11/b12) — same face throughout, never cream/white.

**SPEAKER LAW (Revelation red-letters Christ's sayings):** j1 (Rev 3:20) and j2 (Rev 3:21)
are BOTH the risen Christ → RED captions on Jesus's own face (b02/b03/b05 and b09/b10).
n0/n1/n2/n3/card = NARRATOR → white. Only Jesus wears cream.

**HARD GATE — GOD / THE FATHER NEVER EMBODIED.** b10's "set down with my Father in his
throne" is carried by Christ (the embodied Son) beside a second throne of pure radiant
white light with NO one on it and no figure above it. No dove/triangle/all-seeing-eye/
symbol anywhere. Drift-word gate clean (no halo/glow/rim-light — every light worded
radiant/luminous/warm).

**CONTENT-CARE:** the knock is gentle ("not a storm"); Christ never forces or breaks the
door; the throne is glory + welcome, never an empire's crowns/jewels/courtiers; the shared
seat is grace, not a reward earned by being flawless.

---

## 🅿️ COMPLAINT LEDGER — OPEN, must be closed by the AUDIO lane before Ready ✅

**Cameron (v2_outline.py 189):** *"Pronounce overcometh as OH-vur-kuh-muhth 0:38."*

**DIAGNOSED VALID + root-caused (this author lane, $0):**
- The SPOKEN respell `{"overcometh": "overcummeth"}` is **already in `make_narration.py`**
  (added 2026-07-29 09:44) with the A/B note that plain "overcometh" renders a seam
  (isolated whisper "Over Kometh"), and "overcummeth" reads as one word.
- **BUT the delivered `audio/j2.mp3` was rendered 2026-07-28 16:11 — the day BEFORE the
  respell was added.** So the fix exists in source but was **never rendered into audio.**
  That is exactly why the complaint is still open.
- Engine facts: `j2.mp3` is **ElevenLabs 44100/128k**, and its median **F0 ≈ 90.7 Hz**
  matches the OLD/wrong Jesus voice row 185 diagnosed (chosen ≈ 105-118 Hz). So j1/j2 very
  likely also carry the stale Jesus voice, not just the stale pronunciation.
- **HAZARD — do NOT `python3 make_narration.py` naively.** `mbm_speakers.py` still maps
  JESUS to edge-tts `en-US-EricNeural`, but the shipped audio is ElevenLabs — a plain
  re-run would SWAP Jesus to the wrong engine (the rows-50/51/70 trap).

**AUDIO LANE — the precise fix (why this is not a $0 author-lane job: it costs ElevenLabs
credits + is contested-voice territory):**
1. Re-voice **j2 only** through the SAME ElevenLabs JESUS voice the delivered audio uses.
   **Resolve the voice against Cameron's approved rows first** — row 185 restored **"Chris"**
   (`iP95p4xoKVk53GoZ742B`) as the chosen Jesus and proved it acoustically (F0 105-118 Hz),
   while `mbm_eleven.py`/the rubric still name **"Alexander"**. Use whichever the audio
   lane confirms is the approved chosen Jesus (row 185's evidence governs); render j2 with
   the `overcummeth` respell via `mbm_eleven.render_segment(..., JESUS)`, NOT make_narration.
2. **Verify** the render: whisper the isolated j2 round-trips to "overcometh" (one word, no
   "Over Kometh" seam) AND, by ear/F0, that "overcometh" lands as OH-vur-kuh-muhth and the
   voice is the chosen Jesus (F0 in the 105-118 Hz family, not ~90 Hz).
3. **atempo-match** the re-voiced j2 back to the original j2 seg duration (10.835 s
   seg / spoken 8.955 s) so NO beats_v2 window moves; the caption text is unchanged.
4. **While here (same touch):** if the F0 confirms j1 is also the stale/old Jesus voice,
   re-voice j1 to the chosen Jesus the same way (atempo-matched) so the whole video carries
   the approved voice — this is the row-185 restoration and closes a second latent defect
   in one pass. Narrator segments (n0/n1/n2/n3/card) stay byte-identical.
5. Set `AUDIO_FROM_V1_SEGMENTS = True` in `beats_v2.py` so `v2_assemble` rebuilds the track
   from the corrected segments. `v2_prompt --check` must still PASS; audio-audit → 0.
6. Then flip AUTHOR-BOARD row 189 **NEEDS-AUDIO → AUTHORED / Ready ✅** so the picture
   runner builds the 12 stills on the corrected audio (0 stills exist today).
7. The review card MUST tell Cameron, in plain words, that **"overcometh" is now
   pronounced OH-vur-kuh-muhth** (and, if step 4 ran, that the chosen Jesus voice is
   restored) — so he can verify at 0:38 in one look.

This is the same complaint-family as rows 50/51/70/185/188 (edge-tts respell orphaned to
an ElevenLabs migration / stale Jesus voice). The audio lane owns the mechanical fix.

---

## 🅿️ RUNNER — after the audio is fixed and Ready ✅ is set

0 V2 stills exist. Build all 12 on the corrected audio.

**NEW places — promote each from its first NON-Jesus frame BEFORE generating the rest of
that place (lesson 11 — never promote a Jesus frame):**
| Place | Promote from | Then reuse on |
|---|---|---|
| DOOR-NIGHT | **b01** (drowsy house, NON-Jesus) | b02, b03, b06 |
| LAMPLIT-ROOM | **b04** (man hears, NON-Jesus) | b05, b07, b08 |
| THRONE-GLORY | **b11** (overcomer before the open seat, NON-Jesus) | b09, b10, b12 |

Gates before assembly: face/beard board on OVERCOMER + Jesus; SCALE gate (Jesus and the
overcomer ordinary-sized, side by side in b12); sacred-figure gate on b10 (the Father's
throne must stay pure light, no figure/symbol); realistic-only (Law 14, no cartoon/mixed);
drift-word/one-cream checks. Then `v2_assemble` (AUDIO REBUILD from the corrected
segments), re-audit, ship with the COMPLAINT LEDGER card above.
