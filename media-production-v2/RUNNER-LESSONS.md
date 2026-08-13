# RUNNER-LESSONS — the shared defect memory (every build session reads AND feeds this)

Created 2026-08-06 after Cameron: "it will probably still suck and make mistakes
becasue your not doing anythign for making it do it better learning from
previous mistakes or using previously made pictures."

**The law:** before Light QC on any row, read every pattern below and check the
frames against them. When you find a defect class NOT listed here — even one
you rerolled successfully — ADD it as one line before your session ends and
commit it. This file is how one session's $0.13 mistake stops being every
session's $0.13 mistake. Keep entries deduped and one line each.

- **A TEXT-LOCK-ONLY human-spine character (`REFS={}`) DRIFTS across a location/scene change — different age, beard and wardrobe in the interior vs exterior half — and it BLOCKS the ship (2026-08-13, row 179 stephens-witness, Opus runner resume PARK).** With no image ref wired to any beat, the lock TEXT alone did not hold Stephen: the council-interior frames rendered a ~20yo light-patchy-beard man in a plain oatmeal tunic, while the outdoor-martyrdom frames rendered a ~30yo full-dark-beard man in a **cream tunic + brown mantle** (the cream also violating his "NEVER cream" wardrobe lock), and the closing frame flipped back to the young look. Two visibly different men = a FACE-BOARD failure Cameron would flag, and it is NOT runner-fixable: making them consistent needs 5-8 regens (>15% COST-LAW budget) and the real fix is pinning an on-lock ref, which is an author-lane `REFS`/lock edit the runner may not make (blind `--redo` of the same text just re-drifts — the continuity lesson). **On resume/QC of any build, check `grep -n "REFS = {}" beats_v2.py`: if the spine character is text-lock-only, FULL-CUT GATE it hardest for cross-location drift, and PARK NEEDS-REBUILD (author pins a single on-lock portrait ref to every beat of that person, deletes + regens only the off-model cluster) rather than shipping or blowing the reroll budget.** Author lesson under it: a `v2_story_cast` portrait sitting in `CAST-REF-V2/` is NOT wired unless it is in `REFS` (or a committed CAST sheet) — a spine character carried by prose alone will drift the moment the scene context changes.

- **A TEXT-LOCK-ONLY miracle-recipient (`REFS={}`) FLIPS AGE/HAIR-COLOUR ACROSS THE HEALING even inside ONE continuous location — and a committed `CAST-REF-V2/<char>.jpeg` portrait may be sitting UNWIRED on disk (2026-08-13, row 142 light-of-the-world, Opus runner resume PARK).** Not just cross-LOCATION drift (row 179): here the born-blind man rendered ~50yo grey-bearded in the PRE-healing beats (b07/b08) and ~33yo solid-black-haired in the POST-healing beats (b09/b10) — an age + grey flip at the state change, in the same daytime street. The `BLINDMAN` prose lock ("about thirty-five, unruly black hair, short dark beard") could not hold him because it was text-only, AND the build already contained the correct canonical `CAST-REF-V2/blindman.jpeg` that was never added to `REFS`. GATE any miracle/transformation row (blind→seeing, sick→healed, mourning→restored) HARDEST across the BEFORE/AFTER split, not just across locations. When such a recipient is text-lock-only, check `CAST-REF-V2/` for an accepted portrait: the author-lane fix is to wire it (`REFS={"TOKEN":"CAST-REF-V2/<char>.jpeg"}`) and regen only the off-model half — NOT a runner blind `--redo` (re-drifts) and NOT within the ≤15% reroll budget. PARK NEEDS-REBUILD. Also here: a text-only born-blind man rendered OPEN/SEEING dark eyes in a pre-healing beat where the author QC required MILK-PALE eyes — a wired ref + the per-beat eye-state cue must both be present.

- **CARD-AUDIO-LONGER-THAN-CARD-WINDOW silently DROPS the last picture beat — a REDONE story whose "windows line up with the V1 mp4" claim is FALSE (2026-08-13, row 173 dead-shall-hear, Opus runner PARK).** On a rebuilt row (V1 was a 7-still ASSEMBLY-C; V2 authored 13 beats), `v2_assemble` builds still chunks from beats_v2 window `start`s but caps the last chunk at `card_start = data['card']['seg_start']` from `extract_beats`. When the closing CARD narration is longer than the authored card window (row 173: card audio **6.863 s** vs authored card window 58.851→61.595 = **2.744 s**), `extract_beats` fits the card by setting `card_start = total − card_dur = 54.732 s` — which lands BEFORE the last beat's window (b13 = 55.65→58.851), so b13 gets a negative duration and is **silently skipped** (`if dur <= 0.05: continue`). Symptom: `segs/concat_base.txt` has FEWER clips than BEATS (12 vs 13); `base.mp4` is ~4 s short of the audio; the last-beat still never appears and its narration rides the prior still + card. **DETECT before shipping any rebuilt/new-story row: after assemble, `grep -c "^file" <build>/segs/concat_base.txt` must equal `len(BEATS)`; and compare `extract_beats` card_start (`data['card']['seg_start']`) to the beats_v2 last-beat window — if card_start < last beat window start, a beat is dropped.** Also verify the beats_v2 total matches the shipped V1 mp4 duration (`ffprobe`); row 173's V1 mp4 was a stale 59.396 s vs the beats_v2 61.595 s timeline, so BOTH the default path (AUDIO LOCK fail) and AUDIO_FROM_V1_SEGMENTS (correct audio, dropped video beat) exposed the same authored-timeline error. This is an AUTHOR-lane fix (reconcile card narration length ↔ card window, or re-window the tail beats, or make the card a short visual with a voiceover audio) — NOT a runner window edit. PARK NEEDS-REBUILD.

- **`v2_stash.py --wire` can OVERWRITE a build's committed PLACE-REF plate with the WRONG auto-picked source (2026-08-13, row 173).** Running `--wire` re-derived TEMPLE-COURT from the stash and copied a build-96 *crucifixion* frame over the author's committed build-39 `PLACE-REF/temple-court.jpeg` (308 952 → 363 924 bytes). Generation reads the FILE in `PLACE_REFS` (not PLACE-WIRING provenance), so this silently poisons every beat of that place. FIX: `git checkout HEAD -- <build>/PLACE-REF/<token>.jpeg` to restore the committed plate, and pin the wiring entry `"manual": true` so a future `--wire` won't re-derive it. Only `--wire` a build that has NEW unplated places; on a build with a committed reused plate, promote the new place directly (`--promote`) and leave the committed plates alone.

- **REPEAT-COMPLAINT ALERT — the row-146 night-crowd fixes above were tried ONCE and were INSUFFICIENT; here are the DURABLE fixes (2026-08-13, row 146 vine-and-branches C-FIX#2, Cameron: "all three problems are still there you fixed nothing and wasted my time and credits").** C-FIX#1 added the skin-tone words / "no disembodied arm" / "both hands, five fingers / not near-black" exactly as the lesson above says — and shipped claiming "14/14 PASS" WITHOUT extracting the frames from the rendered mp4. All three defects survived. The words alone are not enough: (a) **white faces** — a moonlit crowd needs a PRACTICAL WARM FILL LIGHT rendered IN the frame (a low oil lamp among the group throwing warm firelight up on every face) + keep the ring SHALLOW so no face sits in cold background; skin-tone adjectives with no warm light source will still drain the back row. (b) **multiple arms on hands-on-one-branch** — forbidding "disembodied" limbs does NOT stop hands STACKING/overlapping on one branch; demand EXACTLY N hands (one per person), laid SEPARATELY with a clear GAP of bare wood between each, no touching/stacking, each short forearm plainly attached — countable at a glance. (c) **Jesus missing a hand** — NEVER stage a Jesus handclasp "against/behind" a trunk; the trunk occludes his body into an embrace-tangle and hides a hand. Keep Jesus CLEAR of the trunk, whole upper body open, both hands RAISED and engaged in the clasp (not one dropped at his side). (d) a warm cozy-lamp night scene will drift PAINTERLY/illustrated unless you add an explicit "PHOTOREAL ONLY — real photograph, not a painting/illustration/CGI render" clause (a stylized frame among photoreal ones is a Law-14 mix-fail = a new complaint). (e) **META, the reason this became a repeat complaint: NEVER write "FULL-CUT GATE PASS" without `ffmpeg`-extracting the frame from the RENDERED mp4 and LOOKING at it — the source asset and the Ken-Burns-cropped render differ, and a claimed pass you didn't verify is the row-11 failure that costs a re-cut, a voided approval, and Cameron's trust.**

- **ENGINE PARITY (Cameron 2026-08-11, row 10 j2 — "you changed to the old Jesus
  voice and kept messing it up... you keep making the same mistake"): a segment
  re-voice MUST use the ENGINE + VOICE that rendered its siblings.** Rows migrated
  to ElevenLabs must be re-voiced via the BUILD-LOCAL `mbm_eleven.render_segment`
  (Jesus = Chris `iP95p4xoKVk53GoZ742B`); `make_narration.py` is the OLD edge-tts
  engine — regenerating any segment with it swaps in the WRONG voice even when the
  pacing is right. FOUR pacing fixes in a row repeated this. Check provenance
  BEFORE re-voicing (memory: eleven-bypasses-say-map). Gate every re-voiced
  segment with word-exact whisper transcription (small.en, beam 5) — all words
  heard separately, no fusions ("Amhi") — before assembly.

- **DETERMINE THE SHIPPED AUDIO ENGINE BY DURATION, NOT ROLLOFF — and remember a
  row with `AUDIO_FROM_V1_SEGMENTS=False` SHIPS THE V1 mp4's AUDIO, which may be
  ElevenLabs even when the V2 dir is edge-tts (row 27, 2026-08-11).** Row 27 sat
  "ear-blocked" through EIGHT $0 audio passes that all reasoned about it as edge-tts
  and found it clean. They analysed the wrong engine. The v2-dir `audio/*.mp3` are a
  red herring; with `AUDIO_FROM_V1_SEGMENTS=False` the assembler COPIES the V1 build's
  finished mp4 audio, and the V1 build here carried `mbm_eleven.py` + `.audio-eleven-done`
  = the shipped voices are ElevenLabs (Brian/Chris/Roger), NOT the edge-tts Andrew/Eric/
  Steffan in mbm_speakers. DECIDE the engine acoustically the RIGHT way: render the
  segment's exact text via edge-tts (`make_narration` path) and compare DURATION —
  edge-tts -20% is deterministic and much SLOWER (row 27 n1: shipped 6.30s vs fresh
  edge-tts 9.38s → ElevenLabs). The spectral-rolloff test is USELESS here: ElevenLabs
  mp3_44100_128 ALSO rolls off ~12kHz, so "no energy >16kHz" does NOT prove edge-tts.
  To re-voice a segment on such a row you MUST use ElevenLabs `render_segment` (parity)
  — edge-tts would swap in the wrong voice. KEY GOTCHA: the `elevenlabs*KEY*.txt` file
  now holds MULTIPLE labelled keys, so `mbm_eleven._key()` returns garbage; extract
  `re.search(r'sk_[A-Za-z0-9]+', raw)` and pass `key=` explicitly. Also: VIEW a
  spectrogram (ffmpeg showspectrumpic) don't just compute numbers — a rendered
  spectrogram is a real "listen" a headless agent CAN do and it catches glitches/
  dropouts/wrong-voice segments the numeric passes miss.

- **SERVED-BYTES VERIFICATION (Cameron 2026-08-11, row 17: "17 wasent fixed" —
  he was right): a ship is NOT live until the bytes the reviewer serves MATCH
  your fixed mp4.** What happened: a `git add` earlier in the chain died on
  gitignored files, `&&` skipped the mp4 commit, the card's data-hash got set
  from `git log -1` (= an older commit), the page-level "live verify" grep
  passed on the LABEL, and Cameron watched the OLD cut wearing a FIXED badge.
  MANDATORY before calling any row shipped: (1) `git ls-tree HEAD -- <mp4>`
  must equal `git hash-object <mp4>` and origin/main must contain HEAD;
  (2) DOWNLOAD the mp4 via the card's exact URL (with its ?v=) and
  md5-compare against the local file — grep-ing the card hash proves nothing
  about the video; (3) `git add -f` media FIRST in its own command — never
  behind a fallible add in an && chain. GitHub raw edge-cache can lag a few
  minutes after push; poll until the served md5 matches, THEN report shipped.

- **A CONTINUITY complaint that survives 2+ blind re-rolls is a BEAT-TEXT defect,
  not a generation fluke — fix the TEXT, don't regenerate again (Cameron 2026-08-11,
  row 66, 3rd RE-OPEN: "people keep disappearing quickly and coming back and the
  army is going the wrong way").** A multi-figure sequence (an arrest party, a crowd,
  a procession) whose beats don't PIN a count and a direction lets every regeneration
  reset the figures' distance/position, and the tight close-ups drop the surrounding
  cast entirely — so across the intercut people flicker in/out and the group's motion
  reverses. Two prior fixes each just `--redo`'d the same beat text and reproduced it
  exactly (that is the trap). ROOT-CAUSE FIX (Cameron's order authorizes editing
  scene/must_show for a continuity C-FIX): add ONE shared continuity clause to EVERY
  beat in the block pinning (a) a single approach DIRECTION ("one column climbing from
  the lower-left toward X, never receding/reversed"), (b) a fixed COUNT/identity of
  the figures ("the same three men, no more no fewer"), and (c) that even tight
  close-ups keep the group/column in the background so the scene never empties; also
  de-conflict any beat whose camera note fights the locked direction (row 66 b03 said
  "from the side"). THEN regenerate. Verify with the FULL-CUT GATE viewed in
  PLAY-ORDER (window order, not b-number order) so a distance reset / direction flip
  is visible as a sequence. Cost: locking the text + regenerating the block (~$1.21,
  9 frames) is cheaper than another blind full "restart" ($4.29) that repeats the
  complaint. A continuity complaint re-opened 3× is the LEARNING LAW's exact warning.

- **HF-MUFFLE from ElevenLabs-HISTORY recovery — a "Voice is wrong / bad audio"
  complaint whose voices are ALL CORRECT (Cameron 2026-08-11, row 74, 2nd complaint;
  the 1st park BLOCKED it as "no localizable defect").** The old 5-test $0 battery
  (engine / transcript / MFCC / uniform-voice / clip%) does NOT measure SPECTRAL TILT,
  so it missed the real defect and re-blocked. ADD a 6th test and run it on any
  "bad audio" row: decode the SERVED mp4 and 2-3 APPROVED rows' mp4s, average the
  voiced-frame power spectrum of each, and compare by band. Row 74 was nearly identical
  to approved up to 3 kHz then **−6.7 dB @ 6-10 kHz, −17.6 dB @ 10-16 kHz** — uniformly
  muffled across EVERY segment, row-specific (approved 50/51/70 all crisp). Root cause:
  `git log` on the segment mp3s showed commit `d3598b3b9` *"recover 77 reverted builds
  FREE from ElevenLabs history"* — those 77 builds' audio is a re-encoded, HF-rolled-off
  history copy, not a fresh render. **This is a whole CLASS (77 builds); on ANY "bad
  audio" complaint, `git log <build>/audio/*.mp3 | grep d3598b3b9` — a hit means suspect
  HF-muffle, run the spectrum test.**
  - **Prove the voices are the CORRECT locked models with F0, not MFCC.** Median F0 over
    voiced frames IS text-independent and speaker-discriminative where the homemade
    MFCC-cosine (~0.97 for everything) failed: measure the row's per-speaker median F0 and
    compare to an approved row's — **Chris(Jesus)≈85 Hz, Brian(narr)≈97-101 Hz,
    Roger(scrip)≈111-115 Hz**. Row 74 matched all three within a few Hz ⇒ voices correct,
    so the complaint is NOT a wrong voice and a blind re-voice is still forbidden.
  - **FIX = corrective de-muffle EQ, NOT a re-voice ($0, deterministic, take-preserving).**
    The HF was attenuated (−60 dB) not gone (noise floor −81 dB), so EQ recovers it. Extract
    the served audio, apply `highshelf=f=6000:g=4,highshelf=f=9000:g=7,highshelf=f=13000:g=8`
    (converge by re-measuring bands vs the approved average — target the deficit, cap boosts
    to avoid noise), re-normalize to −15 LUFS + `alimiter=limit=0.95` (the assembler's exact
    final stage), then **remux with `-c:v copy`** so the video stream is byte-identical
    (its md5 must be unchanged old→new — the whole picture QC/gate carries over). VERIFY:
    re-measure spectrum (6-10 k and 10-16 k now within a couple dB of approved) + whisper
    ORDER CHECK (words unchanged, EQ preserves duration so no window/caption drift).
  - **Caveat:** this de-muffles the DELIVERED mp4 only; the SOURCE segment mp3s stay the
    muffled history copies, so a FUTURE `v2_assemble` reintroduces the muffle — a re-assemble
    session must de-muffle the 19 source mp3s (same EQ, duration-preserving) or re-render them.
  - **The lesson under the lesson:** an "all-clean → BLOCK for ear-pass" verdict can be a
    battery that isn't deep enough, not a truly-clean row. Before re-blocking a REPEAT
    complaint, add a test the prior battery lacked (here: spectral tilt vs approved rows).

- **PROMPT AUTOPSY IS THE STANDARD REWORK (Cameron 2026-08-11): before ANY
  reroll, read the exact prompt that made the bad frame and rule CAUSED (bad
  wording — rewrite it) / ALLOWED (missing constraint — add it) / IGNORED
  (generator drift — attach a reference image; words cannot pin appearance).
  Verdict goes in QC.md; new bad-wording patterns become lessons here. Blind
  rerolls re-run the same evidence and hope — forbidden.**

- **A "resolved" complaint can silently REGRESS or never-land on the LIVE cut — the
  FULL-CUT GATE must re-verify each resolved complaint in the RENDERED mp4, never trust
  the card's "fixed" flag (2026-08-12, row 1 QC-VERIFY).** Row 1's 2026-08-06 card said
  the 0:52 touch complaint ("she touches the edge/tassels only, not his back/thigh") was
  fixed, but the live realistic-v3 mp4 STILL showed her full open palm flat on Jesus's
  lower back, fringe far below at his ankles — the earlier fix regressed or never rendered.
  A QC-VERIFY pass that only reads the card/QC header would have shipped the repeat
  complaint straight to Cameron. On any row with resolved complaints: extract that beat's
  frame from the DELIVERED mp4 and confirm the resolved defect is actually absent. Fix
  here was PROMPT-AUTOPSY ALLOWED: the "reach" beat named the correct target (tasselled
  fringe at his ankles) but never BANNED touching his back/hip/thigh, so the generator
  drifted a full-palm press onto his body — add the explicit body-contact ban to
  must_not_show (a positive target is not enough when the wrong pose is anatomically
  adjacent), and reinforce the reaching figure's locked wardrobe in must_show (take 1
  fixed the hand but dropped her dust-rose head cloth to near-cream beige; take 2 nailed
  both).

- **A "the people came ASKING the prophet" beat with no PROP/SIGN pinned in must_show drifts to a generic OCCUPATION genre scene (2026-08-13, row 158 two-sticks b13).** The beat's narration was "and of course the people came asking, what do you mean by this?" and its scene described exiles converging on Ezekiel — but must_show named only the convergence, not the SIGN he holds, so the model rendered the prophet at a POTTER'S WHEEL working clay (a stock "biblical craftsman" scene) with the crowd merely milling in the background: the reason they're coming (the two-rods sign) was absent and Ezekiel's action read as pottery, not prophecy (ACTION-LOGIC fail). It is per-frame generator drift, not subtle: one plain `--redo` re-rolled a correct converging-exiles frame (elder waving his stick, families+children moving toward the prophet). On any "crowd comes to the prophet/teacher to ask about X" beat, QC that the FRAME actually shows X (the sign/prop that prompts the question) and that the central figure is doing the story action, not an unrelated trade — reroll on sight if it drifted to an occupation.

## FLEET / COLLISION — read this at CLAIM time (step 1), before you pick a row

- **A `while pgrep -f "v2_assemble.py <row>"` wait-loop MATCHES ITS OWN COMMAND LINE — a false "STILL RUNNING" that can mask a dead assemble (2026-08-12, row 63, headless).** The monitoring loop's own bash process contains the literal string `v2_assemble.py 63`, so `pgrep -f "v2_assemble.py 63"` returns that loop's PID even after the real assemble has died — I read "STILL RUNNING" for ~20 min while the actual assemble was gone and the final mp4 was never rewritten (it stayed the PRIOR run's bytes, i.e. the un-fixed cut). MONITOR BY THE REAL PID (`nohup … & echo $!`, then `kill -0 <pid>`) or by an OUTPUT ARTIFACT (final mp4 mtime advancing past your reroll + `grep "AUDIO REBUILD PASS" <log>`), NEVER by `pgrep -f` on a string that also matches your own watcher. And at this concurrency a re-assemble CAN be starved/OOM-killed by a sibling autopilot lane's assemble (row 147 here) after the caption pass but before the final mux — always confirm the final mp4 mtime is NEWER than your last reroll AND re-extract the fixed beat from the delivered mp4 before shipping; a "DONE" earlier in the log is not proof THIS mp4 carries your fix.


- **A SHIP must NEVER tick the QUEUE `Appr` column — that is Cameron's alone (2026-08-11, row 94 QC-VERIFY).** The realistic-v2 ship commit `29ed2667b` flipped row 94's QUEUE cells from `Prep✅ Built✅ Appr⬜ Post✅` to `…Appr✅…`, falsely marking it Cameron-approved when he had never seen it (its same-day siblings 92/93/95 correctly stayed `Appr⬜`). The harm is silent: `Appr=✅` DROPS the row from Cameron's review list ("review list = Built✅ AND Appr⬜"), so a cut that should be sitting in his queue disappears from it. When you ship a row, set `Built✅` only — leave `Appr`/`Post` exactly as they were. When QC-verifying, if you find an `Appr=✅` with no matching "NN good"/approval commit in `git log`, it is this bug: correct it back to `⬜` and note it (Cameron re-ticks if he really approved). A build session touching `Appr` is a hard-rail miss.

- **WRONG-JESUS-VOICE / "speaker changes mid-video" is an AUDIO park, and its
  usual cause is a PRIOR fix that re-voiced one segment through edge-tts on an
  ElevenLabs build (2026-08-07, row 22 CAMERON complaint "2:46 Jesus speaker is
  wrong one and it changes to the right one later").** Builds migrated to
  ElevenLabs "Chris" for Jesus on 2026-07-23, but every build still carries the
  OLD edge-tts `make_narration.py`. When an earlier audio-fix "re-voiced ONLY jN
  via make_narration.py", it renders that ONE Jesus line in the DEAD edge-tts
  Eric voice while the siblings stay ElevenLabs — so Jesus's voice audibly
  changes mid-video. DETECT with ffprobe:
  `ffprobe -v error -show_entries stream=sample_rate,bit_rate -of csv=p=0 audio/jN.mp3`
  → **`44100,128000` = ElevenLabs (correct)**, **`24000,48000` = edge-tts (the
  dead old speaker)**; any Jesus segment whose signature differs from its siblings
  is the wrong voice. This is OUT of runner scope (re-voice through ElevenLabs is
  audio-lane work): PARK **NEEDS-AUDIO**, put the ffprobe proof + the offending
  segment id in the QC.md RUNNER PARK note, and — CRITICAL — the row's Claim cell
  must NOT contain the literal token `AUDIO-FIX` or the autopilot audio picker
  (`'AUDIO-FIX' not in cl`) will SKIP it; replace any stale "AUDIO-FIX SHIPPED"
  claim with a fresh park claim. Full rule: SPEAKER-LAW.md "OLD-JESUS-SPEAKER BAN".
- **AUDIO-PRONUNCIATION complaints are OUT of runner scope — park the row, do
  NOT ship over them (2026-08-06, rows 50/51; row 46 shipped WRONG).** Run
  `v2_outline.py <row>` at claim time: if the OPEN complaint is a mispronunciation
  ("Cana → Kane-a", "tear → tare", "put-uth", "Lieth → lie-eth"), the fix is a
  re-voice (respell/spoken-override + regenerate narration), which the runner is
  forbidden to do (audio-immutability). Mark the row **NEEDS-AUDIO** on the board,
  write a RUNNER PARK note in QC.md with the resume, and take the next row. Do
  NOT ship a picture-rebuild over an open audio complaint — the audio is unchanged,
  so the complaint repeats (the worst failure). Row 46 was shipped this way with
  its "put-uth" complaint still open because its QC.md wrongly claimed "no open
  complaint"; always trust `v2_outline.py`, not the QC header, for open complaints.
  - **EXCEPTION — a pronunciation complaint whose re-voice is ALREADY DONE and
    baked into the V1 mp4 is NOT a park; SHIP it (2026-08-06, row 57 "lieth →
    lie-eth").** Before parking a pronunciation row, check whether the author
    already fixed it: (1) board Audio column says **OK** (not CHECK); (2)
    `make_narration.py` has the `SPOKEN`/respell override for that word;
    (3) `git log` shows a "verified in final audio" fix commit AND the V1 mp4
    was re-rendered AFTER it. If all three hold, the runner is NOT re-voicing —
    it ships the already-corrected byte-identical audio, and **AUDIO LOCK PASS
    is the cryptographic proof** the fix is in the shipped audio. Rows 50/51
    park because their audio is CHECK and the fix is not yet rendered; row 57
    ships because its audio is OK and the fix is already in the mp4. Put the
    proof in the QC COMPLAINT LEDGER and answer it on the review card.
  Rendering complaints (question-card "squares") are DIFFERENT — the V2 card
  renderer already fixed that class, so just verify the rendered end card is clean
  and ship.
  - **A board that says "AUDIO FIX DONE / Audio OK" is NOT proof the fix ships —
    verify the fix reached the AUTHORITATIVE audio before trusting it (2026-08-07,
    row 50).** `v2_assemble` sources narration from the V1 mp4
    (`media-production/<build>/*.mp4`), or from the V1-dir mp3s only when
    `AUDIO_FROM_V1_SEGMENTS=True`; it EXPLICITLY ignores the V2 build-local
    `audio/` dir. Row 50's Cana→cayna fix ran `make_narration.py` from inside the
    V2 build dir, so the corrected n1/n3 landed in
    `media-production-v2/<build>/audio/` (orphaned) while the V1 mp4 (2026-07-29,
    plain "Cana"=KAH-nuh) was never re-rendered. AUDIO LOCK would deceptively PASS
    (durations match, newer_mp3s=0) yet ship the OLD rejected pronunciation =
    repeat the complaint. DETECT before building any "audio-fixed" pronunciation
    row: (a) `grep AUDIO_FROM_V1_SEGMENTS beats_v2.py`; if absent/False the ship
    audio is the V1 mp4 — check the V1 mp4 mtime is AFTER the fix commit; (b) if
    the flag is True, hash-compare the V1-dir mp3 vs the V2-dir fixed mp3 (`md5sum`)
    — they must MATCH. If the fix is only in the V2 dir, PARK NEEDS-AUDIO (the
    audio authority must copy the fixed mp3s into the V1 dir + re-render the V1
    mp4, or set the flag). A passing AUDIO LOCK proves byte-consistency with the
    V1 mp4, NOT that a pronunciation complaint is fixed.
  - **A MULTI-part pronunciation complaint can be HALF-fixed — one word landed in
    the shipping mp4, the other orphaned (2026-08-07, row 70).** Row 70's "I-S/IF"
    was fixed by the earlier REDO render (shipping mp4 says "if/is" —
    whisper-confirmed), but the SAME-session respell for the 2nd word
    ("proceedeth→proceeduth") was committed AFTER the V1 mp4 (respell 2026-08-06,
    mp4 2026-07-28), so it never reached the shipping audio. ANY unfixed part =
    park. When whisper CAN'T adjudicate the sound (-eth vs -uth both transcribe
    "proceedeth"), decide acoustically: extract the segment window from the
    shipping mp4 and cross-correlate the 16k-mono waveform against BOTH the V1-dir
    mp3 (old) and the V2-dir mp3 (fixed) — the mp4 matches whichever it was
    rendered from (row 70: 0.757 vs OLD, 0.026 vs FIXED, fixed take +1.1s longer).
    High-corr-with-OLD → the fix is orphaned → park.
- **A CRUCIFIXION beat that puts Jesus on his cross in the FOREGROUND can render a
  redundant distant Golgotha behind him — a readable 4-cross (or more) contradiction
  (2026-08-07, row 96 it-is-finished b03).** The first take had Jesus crucified in the
  foreground AND three more crosses on the distant ridge = four crosses total / a
  duplicate Golgotha (who is on the back three?). It reads as a count/geometry error,
  not subtle drift — one `--redo` landed a clean 3-cross frame (Jesus centre, two
  flanking). On any single-cross foreground crucifixion beat, zoom the far skyline for
  extra crosses; on a 3-cross beat, count to exactly three. Distinct from the thief-row
  geometry (sides never swap) — here it's a stray extra cross in the background.
- **Crown-of-thorns continuity across a passion/crucifixion ROW (2026-08-07, row 96):**
  a multi-beat crucifixion row will render the crown of thorns on SOME Jesus frames and
  not others (row 96: crown on s04/s05, bare-headed on s01/s02/s06/s08/s11). Each frame
  is individually fine and scripturally defensible (John 19:2-5), so it is NOT a
  per-frame garbage reroll — it is a cross-frame continuity drift (lesson-13/beard-board
  family). Do NOT blind-reroll the crown frames (the choice of crown-throughout vs
  no-crown is a creative/restraint call, and the crown frames are often otherwise the
  best takes). Log FIX-WAVE: harmonize in one deliberate pass (add or remove the crown
  across the row via targeted edit), don't burn the row's reroll budget guessing.
  - **PACING/"too fast"/"meaningless"/"rushed" complaints are ALSO audio-domain —
    park them the same as a mispronunciation (2026-08-06, row 10).** Cameron's
    row-10 complaint was not a wrong word but the DELIVERY of Jesus's Messiah
    reveal j2 "I that speak unto thee am he" being too fast to land. The fix is a
    re-voice (extend the SPOKEN/PHRASE_SPOKEN pauses + regenerate + re-assemble),
    which the runner may not do. A row can even already carry a partial
    PHRASE_SPOKEN ellipsis (row 10 had one for a slur) and STILL be too fast
    overall — a pre-existing override is not proof the pacing complaint is fixed.
    Park NEEDS-AUDIO, do NOT re-cut pictures.
  - **OVER-CORRECTION swings back to a complaint — a pacing re-voice can go too
    FAR the other way (2026-08-07, row 10 recurrence).** The row-10 audio-fix
    answered "too fast" by stacking `-30%` rate + a leading ellipsis + a mid-line
    ellipsis on one 5-word edge-tts line → 4.92 s, and Cameron came back with "now
    its too slow and sounds horrible like a robot... undo it and make it right." A
    synthetic voice (edge-tts) dragged well below its default with two dead-air
    gaps reads as a robot. Fix ONE slow-down at a time and ear-check toward the
    MIDDLE (deliberate, not stretched); don't pile rate-cut + multiple pauses on a
    short line. Still an audio-domain park for the runner — NEEDS-AUDIO, no re-cut.
- **A SIZE complaint over-corrects into its opposite — and a place PLATE does
  not stop close-up scale drift (2026-08-12, row 51 RE-OPEN #3).** Row 51's
  RE-OPEN #2 answered "boats too small / paddle-only" by locking a LARGE ~8m
  masted-boat plate; the plate is correct and holds fine in wide/medium shots —
  but the tight fish-hauling CLOSE-UPS (s14/s15/s16) had no scale wording, so
  the low-angle framing ballooned the same boat into a towering galleon that
  dwarfed the men → Cameron's next complaint was "boats too BIG." The plate
  anchors identity/type, NOT apparent scale in a tight crop. For any boat/figure
  close-up put explicit scale in must_show ("men are the largest thing in frame,
  gunwale ~waist height, NEVER a towering high-sided hull"). Target the
  historically-correct size (Galilee boat ~8m), not "bigger" or "smaller" — a
  size fix aimed at the last complaint direction just triggers the opposite one.
- **A required prop the LOCK omits vanishes in the one wide beat that needs it
  (2026-08-12, row 51 s21 "no sail mast").** b16/b17 spelled out the mast in
  must_show; b21 (same BOATS lock, same plate) did not — and that single wide
  frame rendered mastless. A shared lock/plate is not enough; every beat that
  must SHOW a locked feature has to name it in its own must_show, or a wide/loose
  crop will drop it.
- **"White tears" is a recurring painted-streak defect — ban it, don't invite it
  (2026-08-12, row 51; see rows 71/74).** Any scene word like eyes "wet",
  "tear-tracks", "tear-streaked" on a weeping/repentant close-up makes the model
  paint bright white streaks down the cheeks that read as artificial. On grief
  beats say "stricken/broken", put the emotion in the eyes+brow+mouth, and
  must_not_show "NO tears/tear-tracks/wet or white streaks". FULL-CUT GATE every
  sibling beat of the same scene — the defect clusters across all the kneeling
  frames, not just the one Cameron timed.
- **FIRST check ALREADY-SHIPPED, before you check LIVE (2026-08-06, row-45
  second pile-on, ~$5 wasted).** A row can be fully DONE — mp4 committed, review
  card live — with NO live `v2_gen_api` process, because the lane that built it
  already exited. The "no live sibling → safe to resume" check below will then
  WRONGLY greenlight a full rebuild. So before generating ANY `RUNNING`/`A-auto`
  row, run `git log --oneline -1 -- media-production-v2/<build>/*.mp4` AND
  `grep 'id="v<NN>".*realistic-v2' site/review.html`: if either is non-empty the
  row is SHIPPED — do NOT regenerate, tick it BUILT on the AUTHOR-BOARD if it is
  not already, and take the next AUTHORED row. (The `assets/` count alone does
  not tell you shipped-vs-mid-build; the committed mp4 does.)
- **QC the frames in the build's `OUTPUT_ASSET_DIR`, NOT `assets/` (2026-08-07, row 11 storm).** A realistic rebuild sets `OUTPUT_ASSET_DIR = "assets-realistic"` in beats_v2.py — `v2_gen_api` generates INTO it and `v2_assemble` renders FROM it, while the old rejected roughs stay in `assets/`. If you Light-QC `assets/`, you review the STALE rough frames, not what shipped — on row 11 this made me wrongly conclude two rerolls "reproduced identical / no Jesus" (I was comparing old-to-old) when the real `assets-realistic/` frames were correct and my rerolls had actually WORKED. Before QC, run `grep OUTPUT_ASSET_DIR beats_v2.py` (default "assets") and view THAT dir; or extract frames from the rendered mp4 (ground truth). `ls --time-style=full-iso` both dirs — the shipped one is today's date. Confusing the two burns rerolls chasing phantom defects and can ship un-QC'd frames.
- **Art lives in `<build>/assets/*.jpeg`, NOT `<build>/frames/*.png`.** The
  `frames/` dir is essentially always empty. Judging "this claimed row crashed"
  by an empty `frames/` is WRONG and is what made 3+ lanes all pile onto row 45
  and burn redundant Gemini money (2026-08-06). Count `assets/*.jpeg` instead.
- **A `RUNNING` + `A-auto` row is NOT automatically stranded.** The autopilot
  runs up to 6 parallel lanes and every lane signs claims `A-auto`, so that
  signature CANNOT tell a live sibling from a crashed self. Before resuming any
  `RUNNING`/`A-auto` row, run `ps aux | grep v2_gen_api | grep -v grep`: if a
  `v2_gen_api.py <that-build>` process is alive, or its `assets/` is still
  growing, a LIVE sibling owns it — do NOT touch it, take the next clean row.
  Only resume a `RUNNING` row when NO sibling gen is live (mirror
  `autopilot.sh` next_stranded, which resumes only when LIVE==0).
- **Claim uniquely so the next lane can tell:** put asset count + "LIVE" in the
  AUTHOR-BOARD claim cell of a row you are actively building, and mark it BUILT
  the instant it ships so `next_ready` (state must be AUTHORED) skips it.
- **Never `git add -A` while siblings generate** — you will sweep another
  lane's in-flight `assets/` and `api-spend.jsonl` into your commit. Add only
  your row's paths + the boards/SESSION-LOG explicitly. Pull with
  `--rebase --autostash`.
- **Your `git commit` can "fail" with `no changes added` even though you just
  staged — a sibling lane's concurrent commit absorbed your staged index
  (2026-08-06, row 76).** Concurrent `git` processes share `.git/index`, so if a
  sibling runs `git commit` while your files are staged, ITS commit ships YOUR
  staged mp4/QUEUE/AUTHOR-BOARD and your own commit then finds nothing. This is
  NOT data loss: run `git log -1 --format=%H -- <build>/<mp4>` to find the commit
  that actually contains your mp4 and `git branch -r --contains <hash>` to confirm
  it's on origin/main — then point the review card's `data-hash` at THAT commit,
  not a hash you expected to create. Verify with `git ls-files <mp4>` (tracked)
  before assuming you must re-commit.

## Known defect patterns (check every frame)

- **A SWIMMER'S DIRECTION reads from the FACE/GAZE, not the leading arm** (2026-08-07,
  row 19 b17 Peter-swims-for-shore, CAMERON complaint "1:05 he is swimming the wrong way").
  The rejected take had Peter's leading arm reaching toward the shore but his HEAD turned
  BACK toward the boat — the viewer reads travel direction from where the swimmer looks, so
  it read as swimming the wrong way even though the stroke aimed correctly. On any swim/wade
  beat: the face, leading arm AND wake must all point the SAME way (toward the destination),
  and the thing being left behind (boat) must sit clearly BEHIND the swimmer. One reroll fixed
  it. Verify the direction in the RENDERED mp4, not just the still (a strong profile can still
  read ambiguously in motion-drift Ken Burns).

- **Modern objects sneak in**: hurricane/kerosene lamps (b41 war tent), modern
  chairs (b41), school slates chalked with ARABIC NUMERALS (b41 — period
  writing only, or blank), wristwatches, buttons, stitched tailoring.
- **Modern-style CLOTHESPINS on a laundry line in a village domestic frame** (2026-08-07,
  row 88 b05 village-lane): a "cloths drying on a line" background detail can render clip/peg
  clothespins that read modern (the spring/dolly clothespin is a 19th-c invention); first-century
  laundry was draped over walls/lines, not pegged. Background, non-subject, borderline — usually
  FIX-WAVE not a mandatory reroll, but glance at any laundry-line/domestic frame for pegs.
- **Modern LUG-SOLE boot/sneaker TREAD PRINTS pressed into desert sand/dirt**
  (2026-08-07, row 70 b03 stones-in-the-desert): a ground-level desert frame with
  bare sand in the foreground can render crisp herringbone/waffle hiking-boot or
  sneaker sole prints — a modern-footwear anachronism hiding in the dirt while the
  figures/props all look period. First-century sandals leave a flat print, never a
  lugged tread. Scan the SAND/DIRT of every ground-level or overhead desert/path
  frame for tread patterns; reroll on sight (one `--redo` cleared it, $0.13).
- **Wrong aspect inside the canvas**: a 16:9 image letterboxed inside the 9:16
  frame (b41) — reroll on sight, never crop-rescue.
- **Second cream-robed figure**: ONLY Jesus wears cream; any other cream robe
  fails the frame.
- **Unlocked secondary figure defaults to a Jesus DOUBLE (row 65 C-FIX, b02
  "his own disciples were in the middle of it").** On a `jesus:False` beat whose
  named figures (here two cornered disciples) carry NO locked garment colour and
  NO face lock, the model paints them with Jesus's exact bearded/long-haired
  look AND puts one in cream — the frame reads as "2 jesus" even though no Jesus
  REF is attached. QC EVERY `jesus:False` multi-figure frame for a Jesus double,
  not just for cream. Fix: reroll `--only <beat> --redo` (no lock edit needed —
  the CAST-CLOSURE + no-cream clauses usually resolve it in one take; the two
  disciples came back in brown + dark-red with ordinary faces). Root cause is
  UNSPECIFIED garment/face on the secondary cast, per v2_prompt.py's own note.
  - **The Jesus-double ALSO spawns on `jesus:True` FULL-TABLE beats — and the
    seat it takes is a foreground/mid GUEST, not a background edge (2026-08-11,
    row 74 "2 Jesus figures in one picture").** Any wide dinner/banquet beat that
    says "Jesus among his guests/the others" but locks NO wardrobe on those guests
    will paint one of them (often the one reclining at the head of the U-table) in
    cream with Jesus's hair+beard = a clean second Jesus. BACKGROUND_CAST_LOCK does
    NOT catch it (that caps only ~3 *background* people; these are foreground
    diners). Fix is the same reroll (`--only <beat> --redo`, no lock edit — s26 came
    back single-cream first take, 0 re-rerolls). **SWEEP EVERY table frame in the
    cut, not just the seconds Cameron timestamped:** row 74 he flagged 7 seconds but
    the FULL-CUT GATE found the double in 11 of 36 frames — shipping only the 7 he
    named would have repeated his complaint on the other 4.
- **Lens-staring**: any figure looking into the camera fails.
- **Fair-haired INCIDENTAL children/extras** (row 47 b15 family-in-the-house):
  even non-locked background people default to blond/light hair — a first-century
  Judean scene wants dark hair on everyone. Check kids in domestic/crowd frames,
  not just the locked cast. One reroll usually darkens them; a slightly-light
  child is FIX-WAVE, not garbage.
  - **A PROMINENT foreground ADULT can default blond too — not just background
    children (2026-08-11, row 52 s24 closing going-out).** An unpinned incidental
    figure (`jesus:False ref:False locks:[]`) who is the MAIN subject of a frame —
    here the traveller telling a family the news in the final picture — rendered
    fully blond with a ginger beard, the only light-haired person in the video. On
    the closing/epilogue frame this is a real complaint risk (it's the last thing
    Cameron sees), so it BLOCKS under the FULL-CUT GATE, not FIX-WAVE. GOTCHA: a
    reroll of a going-out landscape can trade the blond hair for a MODERN VEHICLE
    (car/SUV) on the road at the distant village (row-71 going-out class) — zoom
    the far village/road at full-res on every reroll. Row 52 took 2 rerolls (take 1
    fixed hair but added a car; take 2 clean: dark-haired traveller+family+donkey,
    dirt road, vehicle-free village). Runner may NOT add a dark-hair clause to the
    beat text (author-lane); reroll within budget, else park.
- **Headless/extra-limbed figures** (b16 headless at b07): count heads, arms,
  legs at full resolution, especially in crowds.
- **Beards appear/disappear/recolor between frames** (rubric lesson 13 — rows
  9/62/91/102): run the beard-only pass per person.
- **A wired IMAGE-ref character can STILL drift beard LENGTH + head-covering on
  scattered beats — separate the two: the beard-length change is the Cameron-flag
  class (reroll it), the cap↔hood alternation is usually uniform stylistic variance
  (leave it) (2026-08-13, row 115 ram-in-the-thicket, b25/b32).** ABRAHAM carried a
  real `REFS` portrait (tight grey knit cap + LONG white beard), yet ~2 of 32 beats
  rendered a SHORTER/fuller beard + a draped mantle-hood instead of the cap
  (PROMPT-AUTOPSY verdict 3 — generator ignored the attached ref; a fresh `--redo`
  re-anchored the beard on both, no lock/text edit). The KEY nuance for the reroll
  decision: the cap↔draped-hood head covering alternated across the WHOLE cut
  (incl. the already-banked half) — because it is uniform and the FACE holds, it is
  NOT an identity break and chasing it burns budget; the BEARD LENGTH flipping
  short↔long is the rubric-13 defect Cameron flags, so reroll only for that (and for
  a clearly-wrong FACE), not for a hood. Verify the reroll landed in the RENDERED
  mp4, not just the source asset.
- **Giant/shrunken figures** (rubric lesson 14 — rows 56/69/107/112): height-
  check every multi-figure frame against a shared reference; Jesus is
  ordinary-sized, children stay child-sized.
- **Oversized birds/animals in nature frames** (2026-08-07, row 111 b11/s11,
  Cameron C-FIX "0:09 everything is out of scale and weird"). A beat whose scene
  names small wildlife working the FOREGROUND ("sparrows working the seed") can
  render the birds GIANT — the sparrows beside Jesus's hand and next to a seated
  baby came out bigger than the infant's head, throwing the whole frame out of
  scale. It is the same failure as lesson 14 but for animals, and it hides
  because the PEOPLE are fine. FIX: one `--only <beat> --redo` re-anchors small
  birds at true size ($0.13, one frame). CHECK: in every nature/wildlife frame,
  height-check the animals against the nearest person the same way you check
  figures — a sparrow must read tiny next to a hand, never cat-sized.
- **Empty sandals with toes / lamps burning off the wick** (b17): objects obey
  physics; flames sit ON wicks only.
- **Fair-haired / blue-eyed drift on locked cast** (BUILDER in a FIX-WAVE
  note): locks say dark hair/eyes — check every named person against their
  lock even when the face "looks fine".
- **Warm/golden side-light washes a locked dark-haired figure GINGERY-ORANGE**
  (row 69 b12/s12 — Cameron C-FIX "John's hair changed to orange").** A
  black-haired locked character (John, whose lock even says "sun-shot black
  hair") in a low warm-sun frame can render a light sandy grey-gingery top
  that reads ORANGE next to the same character's black hair in cooler frames.
  It is NOT subtle drift to ignore — Cameron reads it as a character/reference
  break. Check every locked-cast frame's HAIR TONE against the reference,
  weighting warm-lit / backlit / low-sun frames hardest; a lone warm frame
  among cooler ones is the tell. One `--only <beat> --redo` re-anchors to the
  ref and lands the correct dark hair. When only 1 of N frames drifts, reroll
  JUST that frame — the others are already correct (13/14 were fine on row 69).
- **PLATE frames propagate their defects** (b41 lamp was IN the plate): QC the
  plate/anchor frame FIRST and hardest — every later beat of that place
  inherits its mistakes.
- **DO NOT reroll — AND DO NOT IRIS-EDIT — Jesus's green/hazel eyes** (row 54
  b13; loophole closed 2026-08-12 after rows 71/89/98/120): the locked V2
  reference `JESUS-V2-REF/jesus-v2-face.jpeg` is itself green/hazel-eyed, so
  every Jesus frame echoes it and it is CONSISTENT across shipped V2 rows. A
  reroll cannot change it and only burns meter; editing the ref is a hard-rail
  violation — **and a targeted iris-recolour edit to brown is the SAME
  violation through the back door.** In the week of 2026-08-11 three C-FIX
  sessions brown-edited close-ups citing the V1-era CLAUDE.md 8(g) "warm brown
  eyes"; that text governs the V1 pipeline (LOCK v3), not V2 — rubric lesson 20
  reverses those edits. The ref image outranks every prose law line. Cameron
  has never filed an eye-COLOUR complaint; "weird/crazy eyes" = gaze geometry
  (rubric lesson 18), reroll for that only. Restore ref-true eyes on rows
  71/89/98/120 in each row's next touch-once re-cut. (Memory:
  `v2_rebuild_plan` "green-eyed Jesus".)
- **"Weird eyes" ≠ eye COLOUR — DO reroll a misaligned/dead-stare gaze** (row 1
  C-FIX, b15, Cameron complaint "1:10 Jesus's eyes looking weird"). The
  no-reroll rule above is about the ref's green/hazel *colour*, which a reroll
  cannot change. A *wall-eye, cross-eye, mismatched pupils, dead stare, or a
  gaze not converging on one point* is a per-frame generation defect and a
  reroll DOES fix it (one reroll gave both eyes open, symmetric, aligned). When
  a beat carries an author "CAMERON GATE ... NO weird eyes" line, that beat is
  cleared to reroll for gaze geometry — inspect the eyes at full resolution
  before accepting the take.
- **Reach/touch lands on the wrong body part** (row 1 C-FIX, b11, Cameron
  complaint "she touches ... the tassels only not his back thigh"). A "touch the
  hem/edge" beat can render the hand up on the back/thigh even when the scene
  text says fingertips at the fringe near the ankles. QC every reaching frame by
  asking WHERE on the body the hand actually lands; if it is not on the named
  target (hem/tassel/foot), reroll — the beat text already specifies the correct
  spot, the model just missed it, and a fresh gen usually obeys.
- **Place wired as a person** (WARTENT queued as a portrait, b41 session): a
  place must never carry a character lock.
- **Wrong story on the board** (row 44 two-debtors vs the QUEUE's Pentecost
  swap): cross-check the row against media-production/QUEUE.md BEFORE spending.
- **Footwear drift on a lone recurring figure** (row 46 farmer: sandals in
  b02/b06/b15 but tall boots in b12/b25): a one-person, many-frame story lets
  footwear (and other small worn items) swap between shots — glance at feet on
  the beard/identity pass. Minor: FIX-WAVE it, do not burn a reroll unless the
  frame is otherwise flawed.
- **Thin wire / power-line across open sky** (row 53 b13 courtyard exterior):
  a taut wire-straight line crossing the sky between rooftops/walls reads as a
  modern utility cable — a modern-object fail. It PROPAGATES from a courtyard
  PLATE (row 53's s03 plate carried it faintly), so QC the plate's sky first;
  one reroll of the affected beat usually clears it. Glance at the sky on every
  exterior/courtyard frame, not just the ground. NOT courtyard-only: it also hits
  open-landscape frames (row 71 b12 garden-tomb in an olive orchard had a taut
  line crossing the misty sky between the trees) — check the sky on EVERY exterior,
  orchard and hillside frame; one reroll cleared it. A doorway/window looking OUT
  onto a village street is the worst offender (row 73 b21 "the open synagogue door
  onto the sunlit Nazareth road"): it stacks a full modern streetscape — a utility
  POLE + strung power lines + cut-ashlar concrete houses with red-tile roofs and a
  rooftop vent — not just one wire, and it is STUBBORN (recurred as a faint sky
  hairline across BOTH rerolls). Budget only 2 rerolls/frame: take 1 kill the pole +
  modern houses, take 2 chase the wire; if a hairline survives, keep the best take and
  FIX-WAVE it (it is subtle background drift, not a foreground defect). Prefer a
  tighter framing / lower horizon so the sky (where wires live) is minimal.
- **Modern paved roads / shoreline highway in a FAR-AERIAL landscape** (row 71
  b21 "the going-out" descent, and faintly b19): a high wide aerial of the Galilee
  hills can render modern-looking paved switchback roads and a straight shoreline
  highway among the terraces. At extreme distance it is borderline (ancient paths
  and terraces look similar), so it is usually FIX-WAVE, not a mandatory reroll —
  but if a straight, graded, modern-width road reads clearly, reroll the aerial;
  the model can land the same vista with only footpaths. Watch the going-out /
  epilogue landscape beats specifically. **CONFIRMED a hard complaint (row 71
  C-FIX 2026-08-07): Cameron flagged the shipped b21 as "the last picture makes
  no sense and leaves people confused" — the paved roads + straight shoreline
  highway + tiny black silhouettes read as a modern drone photo. One reroll to a
  grounded eye-level going-out (robed figures on an old dirt footpath toward the
  sea, warm light) fixed it. If a going-out aerial has ANY graded/paved road,
  reroll it — Cameron's eye catches it even when the runner calls it borderline.**
- **Rerolling a no-Jesus crowd/going-out wide can spawn a stray CREAM-robed
  figure** (row 71 C-FIX b21, 1st reroll): a beat marked `jesus:False` with no
  REF still landed a pale/cream-robed lead figure — off-spec because ONLY Jesus
  wears cream, and on a no-REF beat a Jesus-looking figure is also unlocked.
  Always scan a rerolled multi-figure frame for a second cream robe (RUNNER-
  LESSONS §"cream" family), not just for the named defect; one more reroll landed
  the group in earth-tone robes only.
- **A stiff, board-flat OPEN SCROLL reads wrong — real scrolls/scriptures are
  soft** (row 71 C-FIX b20, 1:51): Cameron flagged "the scroll the guy is passing
  is stiff and open scrolls of paper are not stiff." The model had rendered a
  rigid flat panel of parchment. Fix: reroll toward a CLOSED, soft, worn
  leather-wrapped scripture/codex that folds in the hand (or a naturally curling
  rolled scroll) — never a flat rigid open sheet held out like a board. Glance at
  any hand-off / reading beat for a plank-stiff scroll.
- **A broken figure lying SIDEWAYS/HORIZONTAL across a frame edge** (row 71 C-FIX
  b16, 1:26): a close group shot rendered one figure as a horizontal body draped
  across the top-left edge (Cameron: "a person sideways"). This is per-frame
  garbage, not drift — reroll on sight; one redo landed all figures upright. QC
  every close/crowd frame for any figure that is not vertically posed.
- **A single CARTOON / CGI-render frame in an otherwise-realistic row** (row 56
  b22 the-news-went-out came back as a smooth 3D-illustration/plasticky render
  while all 21 other frames were photographic). It reads as a totally different
  medium and, under Law 14 (realistic-only), a MIX fails the whole cut — worse
  than all-cartoon. It tends to hit the LAST/wide "epilogue" beat (news-goes-out,
  aftermath) where the prompt is a generic landscape with small figures. Check
  the STYLE of every frame, not just its content; one reroll usually lands a
  photographic take. Not subtle drift — this is a mandatory reroll on sight.
- **Green/hazel-eyed Jesus in extreme close-ups** (row 56 b09): the JESUS-MASTER-REF
  face carries a hazel/green cast that only reads clearly in a tight close-up
  (wides read brown). It is SYSTEMIC (all 200, baked into the reference) and a
  plan-level item awaiting Cameron — NOT a per-row regression. One reroll will
  NOT clear a baked-in reference trait, so do not burn rerolls chasing it; log
  FIX-WAVE and keep the best take. Fix belongs at the master-ref level.
- **Multi-panel COLLAGE inside one 9:16 frame** (row 42 barren-fig; row 45 b10
  twice — a 4-up then a 3-up grid of separate shots stacked in one frame):
  triggered by beats that ask for MANY workers doing MANY tasks at once
  ("tenants working the lease"). Reroll on sight — the model eventually lands a
  single coherent wide. Never crop-rescue a panel out of it.
- **A COLLAGE on an ANOINTING beat can import the WRONG anointing event (row 82 b03,
  2026-08-07).** The Mark-14 HEAD-anointing pour beat first rendered a 4-panel collage
  whose second panel showed oil poured on a FOOT — the Luke-7 feet/tears anointing
  bleeding into a Mark-14 beat (the THREE-WOMEN-LAW crossing, now as a collage panel).
  Both defects clear in one `--redo` (single coherent frame, pour on the HEAD). On any
  anointing row, QC a collage reroll for BOTH "is it one panel now" AND "is it the right
  body part (head vs feet) for THIS story."
- **Collage also fires on a SINGLE-figure ACTION beat, as a repeated-same-pose
  triptych** (row 66 b07 Peter's sword-swing came back as 3 vertically-stacked
  near-identical shots of the same man swinging). Not just many-workers beats —
  any "dramatic motion" beat (a swing, a fall, a run) can stack the motion into
  sequential panels. Mandatory reroll on sight; one redo lands a single coherent
  frame. Never crop-rescue one panel.
- **A beat whose TEXT repeats a COUNTING sequence is a STRUCTURAL collage
  trigger that survives the reroll budget** (row 114 b13 "what about forty,
  thirty each"): the enumerated numbers make the model tile one panel per number
  — TWO rerolls both returned 4-up stacks (unlike the row-66/45 collages that a
  single redo fixes). This is NOT a coin-flip a runner can win: keep the best
  take, FIX-WAVE it, and hand to the AUTHOR to de-repeat the counting in the beat
  text (or add an anti-collage cue). Do not burn more than the row's 2 rerolls
  proving it stays a collage — the fix is beat-text, not another render.
- **False "tiled/collage" frame from ffmpeg INPUT-seek (`-ss` BEFORE `-i`)**
  (row 55 caption QC): extracting a caption frame with `ffmpeg -ss <t> -i mp4`
  can land on a non-keyframe and decode a garbled/striped image that looks like
  2-3 stacked panels — it is a DECODE ARTIFACT, not a real collage in the video.
  Before rerolling/re-cutting, re-extract with OUTPUT seek (`ffmpeg -i mp4 -ss <t>
  -frames:v 1`): if the accurate-seek frame is a single clean image, the mp4 is
  fine. Always confirm a suspected assembly defect with an accurate-seek frame.
- **A person-free "calm establishing WIDE" beat renders figures as a floating
  CUT-OUT composited over a bird's-eye AERIAL mini-view of the same place** (row
  45 C-FIX, b46 `s46-that-is-the-setup`, Cameron "0:50 ... trash and just look
  stupid"): the establishing beat locked a VINEYARD plate and its own text is
  person-free, but the model pasted the story's tenants at eye-level ON TOP of an
  aerial view of the vineyard — two clashing perspectives, a ghosting/haze seam
  around the people, a melting head. It is the collage/double-perspective family
  and a MANDATORY reroll on sight; one `--redo` landed a single coherent
  establishing wide. Check every "whole place laid out / the setup / establishing"
  wide for a pasted-in perspective mismatch, not just multi-worker beats.
- **A CRUCIFIXION establishing wide that names all three crucified men AND asks for
  a "far-off, from down the slope, behind the watchers" distant wide is a STRUCTURAL
  double-perspective composite magnet (row 95 thief-on-cross b01, 2026-08-07).** Both
  the first gen (floating cut-out heads + haze seam over the hill) and the 1 redo
  returned a giant foreground trio composited over tiny distant watchers — the beat
  wants the three men legible AND far away at once, so the model splits it into two
  perspectives (same family as row-45-b46 / row-114). It is NOT a coin-flip a runner
  wins: keep the coherent take, FIX-WAVE it (author makes b01 a person-free HILL-plate
  establish or places the three at true distance on the crosses), and do NOT burn a
  3rd reroll on the passion-block opener. Watch the b01 opener on rows 94/95/96 (the
  Golgotha block) specifically. Distinct sub-variant seen same row: b11 came back a
  STACKED DIPTYCH (a clean portrait two-shot on top, an unrelated landscape band on
  the bottom, hard horizontal seam) — that one IS a coin-flip a single `--redo` fixes
  (landed a clean rope-bound Jesus↔thief two-shot).

- **A MODERN CITY SKYLINE renders behind an ancient-city OVERLOOK wide** (row 83
  b02 "he stopped," the Mount-of-Olives view of Jerusalem): a wide that paints a
  whole ancient city panorama behind the hero figures can seed the FAR skyline
  with modern high-rise tower blocks, thin antenna/radio masts and a construction
  crane — the temple + walls read period but the distant skyline is 20th/21st
  century. Same family as the modern-paved-road (row 71) and modern-pilgrimage-
  crowd (row 68) creep, but in ARCHITECTURE behind an intact-city establishing
  shot. On a HERO frame (a complaint frame, the "he stopped/beheld the city"
  beat) it's a mandatory reroll on sight — one `--redo` landed an all-period
  limestone skyline ($0.13). Zoom the far skyline of every ancient-city overlook/
  panorama wide; a faint hazy far element in a NON-hero landscape wide is
  FIX-WAVE (a reroll re-seeds the whole vista for one distant speck).
  - **Sub-variant: the GOLDEN DOME OF THE ROCK renders where the Herodian temple
    should be, on any Jerusalem/Temple-Mount overlook frame (row 100 ascension b11,
    the HERO ascent).** A Jerusalem-panorama beat pulls the model's present-day
    Temple-Mount prior — the gold-domed 7th-century Islamic shrine — into the exact
    spot the Second-Temple sanctuary belongs, often alongside the row-83 modern
    high-rises + crane. It is a period anachronism, not subtle drift, and on a hero
    frame (the ascent, "he beheld the city") it's a mandatory reroll on sight; the
    period MOUNT/Jerusalem plate anchors the correct Herodian temple, so one `--redo`
    against the plate landed an all-period limestone skyline ($0.13). Its sibling
    MOUNT-plate frames on the same row all rendered period, so this was an unlucky
    single draw. Zoom the Temple-Mount area of every Jerusalem-overlook frame for a
    gold dome; there must be the flat-roofed Herodian temple, never a dome.

- **A night-interior beat that OMITS the ROOM/setting lock inherits NEITHER the "night" cue NOR the period-lamp spec — it renders DAYLIGHT windows AND modern kerosene/glass-chimney lamps at once (2026-08-07, row 90 washing-feet b02/b06).** In a night story (last supper), beats whose `locks` include ROOM (whose text said "window open on the night, clay oil lamps") rendered night with clay saucer lamps; beats that locked only BASIN/PETER (no ROOM) drifted to bright daylight windows AND invented glass-chimney hurricane lamps — BOTH defects trace to the one missing setting lock (row-103 class). A reroll without the lock is a coin-flip: b09 (locks ROOM) rerolled straight to night; b06 (no ROOM) stayed daylight on the reroll. Diagnose by comparing the defect beats' `locks` to the clean beats' — if the wrong-setting beats omit the place token, it is an AUTHOR fix (add ROOM to those beats' `locks`), not a runner reroll; do ONE probe reroll then FIX-WAVE. Distinct from a pure generation fluke where a ROOM-locked beat still drifts (that one a reroll fixes). Also note: a beat whose must_show enumerates a SEQUENCE ("close on the sequence: robe aside… towel knotted… water arcing") is a collage magnet even after the daylight/lamp is fixed (row-66/114) — b02 took two rerolls to land a single frame; the durable fix is de-sequencing the must_show (author).

- **A "count" complaint can really be a GENDER-BALANCE complaint — pin 4m/4f, not just "8 total" (2026-08-13, row 135 rainbow-covenant, OPEN reviewer complaint "1st picture has 3 girls and 5 boys that needs to change").** On a fixed-family row (Noah's eight = Noah + 3 sons + his wife + 3 sons' wives), the eight must be exactly **4 men + 4 women, all adults**. A frame with 8 TOTAL figures still REPEATS the complaint if it splits 5 male/3 female — so counting heads to 8 is not enough; count the SEXES. Root cause is systemic: a shared FAMILY lock that names "eight" but not the gender split lets ~⅓ of family frames drift to 5m/3f, and intimate/huddle beats that center "one wife" (row-135 b09) or an embrace cluster (b25/b27) reliably render a nuclear **7** or a 5m/3f — because their `must_show` has NO count pin, unlike the clean count beats (b08 "exactly eight backs", b27 "count eight", b43 "the eight"). Blind rerolls can't fix a missing must_show/lock pin (b09/b27 both hit the 2-reroll cap still wrong) → it is an AUTHOR fix: add "exactly four men + four women, all adults, no children (except the born-since-child beat)" to the FAMILY lock and give the intimate beats a real count pin, then regen only the violators (reuse the rest — COST LAW). Audit EVERY family frame for the 4m/4f split, not just total 8, before shipping any fixed-family row.

## Reuse before regenerate (Cameron's core order — rubric lesson 11 + COST LAW)

- Plates: `v2_stash.py --wire` before generating; promote-first for new places.
- **After every ship: run `python3 media-production-v2/v2_stash.py --scan` and
  commit STASH-INDEX.json** so the row's passing stills instantly become
  reusable plates for every later row. A place generated twice because the
  index was stale is a COST LAW violation.
- Portraits/cast sheets are reused across rows automatically — never re-pay
  for a face that has a sheet.
- **Basket of "fragments/leftovers" renders as pale STONES in dusk/low light**
  (row 58 b21 twelve-baskets): a count beat that should show baskets of BROKEN
  BREAD can come back with grey rounded lumps that read as rocks, especially at
  dusk. Check that basket contents plainly read as bread (golden crust, not grey
  stone); one reroll usually lands clear bread. Distinct from the count itself —
  fix the food-legibility first. Exact object counts (e.g. "twelve baskets")
  rarely land to the exact number in a receding line; that is FIX-WAVE, not a
  reroll, once the contents read correctly.
- **`v2_stash.py --wire` auto-suggests a WRONG-REGION place plate the row's QC
  forbids** (row 59: WILDS auto-wired from build-54 the-leper, but row-59 QC.md
  explicitly bans it — leper's Judean broken country ≠ this Decapolis slope).
  `--wire` matches on TOKEN name only, blind to region/period intent. ALWAYS read
  the row's QC.md place notes before trusting a wired plate: if QC says "do NOT
  take build-XX's <TOKEN>" or "promote-first," clear PLACE-WIRING.json (echo '{}'
  > it), generate the anchor beat, eyeball it, and `--promote` from THIS row's own
  frame. A copied wrong-region plate would propagate the wrong place to every beat.
- **`v2_stash.py --wire` OVERWRITES an already-committed PLACE-WIRING.json entry
  with a different (newer) source build (2026-08-07, row 50 ROAD).** The author had
  committed `ROAD ← build-38-persistent-widow b39`; running `--wire` at build time
  silently rewrote it to `build-79-the-seventy-sent` (a newer ROAD that didn't exist
  at authoring time). Both are valid ROAD plates, but the runner must not override
  the AUTHOR's committed wiring. DETECT: `git diff PLACE-WIRING.json` right after any
  `--wire`; if an EXISTING token's src_build changed, `git checkout PLACE-WIRING.json`
  to restore the committed choice. `--wire` is only for tokens with NO committed entry.
- **`v2_stash.py --wire` writes THREE things, not one — reverting only PLACE-WIRING.json
  is NOT enough (2026-08-07, row 98 TOMB).** When `--wire` attaches a wrong/forbidden
  plate it (a) rewrites PLACE-WIRING.json, (b) edits the build's `beats_v2.py` PLACE_REFS
  dict (replacing an author "deliberately UNWIRED" comment with `"TOKEN": "PLACE-REF/x.jpeg"`),
  AND (c) writes the actual plate art into `PLACE-REF/x.jpeg`. `v2_gen_api` attaches the
  plate by the beats_v2 PLACE_REFS pointer + the file on disk, NOT the JSON — so a
  `git checkout PLACE-WIRING.json` alone still generates against the wrong plate (row 98:
  b01 rendered against build-37's parable tomb even though the JSON read `{}`). When a
  build's QC.md says a token is deliberately unwired ("take row X's frame / never build-37"),
  revert ALL THREE: `git checkout PLACE-WIRING.json beats_v2.py` AND `rm PLACE-REF/<token>.jpeg`,
  then regenerate the anchor plate-free and `--promote` this row's own frame.
- **DECLINE a place plate when its token spans two different rooms/times-of-day
  (2026-08-07, row 50 HOUSE).** Row 50's HOUSE token covers BOTH a night lamplit
  sickroom (b03-b06) AND a bright daytime colonnaded court (b27). Promoting either
  as the single plate bleeds the wrong time-of-day onto the other (the row-101/103
  plate-composition class), and a reroll can't fix it because the plate re-attaches.
  When the receiving beats are genuinely different scenes, DON'T promote — leave the
  token plate-free so each beat renders its own place/time; the CHARACTER refs
  (NOBLEMAN/BOY) already hold identity, and each beat came out correct (verified b27
  as the day court with sea view). Minor within-room architecture drift is FIX-WAVE.
- **A big "crowd streaming up a real Galilee slope" wide comes back as a MODERN
  PILGRIMAGE PHOTO — the background fills with tourists in ballcaps, sunglasses,
  backpacks, windbreakers and a lanyard** (row 68 b30 `no-names`): asking for a
  large crowd on the actual Sea-of-Galilee hills pulls the model toward
  present-day Holy-Land-tour stock photography, so a period foreground figure
  ends up surrounded by 21st-century hikers. Modern-object fail — mandatory
  reroll on sight; one redo usually lands an all-period crowd. Scan the WHOLE
  crowd of any real-location wide for modern dress/gear, not just the named
  subject. Distinct from a single stray modern prop — here the entire background
  population is modern.
- **A "he does X with the traveling prop" single spawns a near-identical TWIN of
  the lone recurring subject** (row 64 b25 "he stood up, rolled up the mat"): the
  beat's only subject is the healed man rolling/carrying his mat, but the model
  added a SECOND grey-bearded old man ALSO carrying a rolled mat right behind him —
  a confusing duplicate (lesson 3 twins + lesson 12 single-subject). One reroll of
  such a prop-handling single usually drops the extra figure; but beware the reroll
  landing a MULTI-PANEL COLLAGE instead (row 64 b25 reroll #1 came back a 4-up grid),
  so verify the reroll is a single coherent frame, not a montage. Two rerolls cleared
  it. Distinct from crowd variety — this is the STORY'S subject duplicated in a shot
  that should hold only him.
- **Model bakes a hallucinated SUBTITLE into the still** (row 67 b06: a first-take
  frame printed "…one for Moses and one for Elijah" as a caption burned into the
  art). It hits beats whose narration is a spoken quote; the model "helpfully"
  renders the line as an on-image subtitle. Two-fold failure: (a) a text-in-image
  defect that will collide with the assembler's real caption, and (b) it can print
  the EXACT word of an open complaint (here "Elijah"). Scan every frame for any
  burned-in lettering; reroll on sight — the real caption is added at assembly.
- **"Sketching/drawing X in the air" prompts render literal cartoon doodles**
  (row 67 b07: "hands sketching three shelters in the air" came back as black
  line-drawn tent ICONS floating in the frame — a Law-14 realistic/cartoon MIX).
  Any beat whose must_show describes drawing/sketching/imagining a shape is at
  risk of a graphic-overlay doodle. Reroll → the model lands a realistic gesture
  (open hands toward the subject) with no floating graphic.

## ASSEMBLY / AUDIO-LOCK

- **A NEW-STORY / old-ASSEMBLY-C row needs BOTH `AUDIO_FROM_V1_SEGMENTS=True` AND a full window remap — the author's `v2_outline` timeline can diverge from `extract_beats`, dropping the LAST still (2026-08-13, row 171).** Row 171's V1 was a 2026-07-17 "ASSEMBLY-C" cut (82.6s, old wider gaps); the current pipeline's `extract_beats.extract(171)` gives 74.45s (card_start 66.672) — so the normal AUDIO LOCK fails (can't stream-copy the 82.6s V1 mp4) and needs `AUDIO_FROM_V1_SEGMENTS=True` (rebuild from the V1-dir segment mp3s at current-pipeline LEAD/GAP offsets; segment mp3s are byte-identical content, so audio is unchanged). BUT the author had scaffolded the beats_v2 windows to `v2_outline`'s OLD gapped timeline (ran to 73.427, ~7s past the live card_start 66.672), so `v2_assemble`'s last-beat slot went negative (`dur<=0.05 continue`) and **s15 was silently dropped (14 c-files for 15 beats)** AND every still drifted vs its caption. FIX (runner timing-metadata, row-42/89 class, allowed): remap all 15 windows piecewise onto the LIVE `extract_beats` segment slices — for each seg, split `[seg_start, seg_end]` by the authored window-width ratios; single-beat segs take the whole slice; the last beat ends at card_start. Verify AFTER: `grep -c "file 'c" segs/concat_base.txt` == beat count, and `ffprobe` video ≈ audio ≈ total. DETECT this class at assemble time: AUDIO LOCK says "extracted Ns but V1 final Ms" with M≫N AND the V1 was an old ASSEMBLY-C (`git log` on the V1 mp4). Both fixes are timing-only — no re-voice, no reroll; audio SHA stays constant across the remap.

- **A STALE-V1 row cleared with AUDIO_FROM_V1_SEGMENTS=True can STILL ship a
  broken cut — the audio rebuilds to the live length but the beats_v2 STILL-
  WINDOWS were scaffolded on a LONGER timeline, so the picture track overruns
  the audio and the final mux truncates the tail + the whole question card
  (2026-08-07, row 74).** AUDIO REBUILD PASS only proves the AUDIO is right; it
  does NOT check the VIDEO length. Row 74: audio 184.57s but captioned.mp4 =
  201.5s (windows ran to 206.32s vs live card_start 176.738s, ~30s drift) → last
  ~25s of stills + the beige card chopped, and stills drift vs captions (row-42
  class). ALWAYS after assembling any AUDIO_FROM_V1_SEGMENTS row, check
  `ffprobe segs/captioned.mp4 duration` ≈ `extract_beats card_start` (±0.2s); if
  captioned ≫ that, the windows are stale. FIX (runner, timing-metadata only, no
  re-voice/reroll — §row-42): remap every beats_v2 `window` onto the live
  extract timeline (piecewise-linear on segment onsets, last still→card_start),
  re-assemble; AUDIO REBUILD SHA256 stays identical (audio untouched). This is a
  SYSTEMIC risk for the whole 74/78/80/82/86-100/105/106/108 STALE-V1 batch —
  verify captioned≈card_start on each before shipping.
  - **Even a SMALL stale drift (~1.7s) silently DROPS the final beat entirely, not just chops the tail (2026-08-07, row 89 last-supper).** v2_assemble places each still from its beats_v2 window START to the NEXT beat's start (or card_start for the last) — so if the LAST beat's window start sits just past the live card_start, its slot is NEGATIVE and that still is skipped, and its caption lands over the previous still. Row 89: b16 window 88.66 > live card_start 86.979 → s16 (the person-free closer) dropped, its n5 caption shown over s15 (the hymn); video_silent 95.9 vs audio 94.13. Watch for a rendered still COUNT less than the beat count (assemble log lists s01..s15 for 16 beats), not just a big duration gap. Same fix: remap all windows onto the live per-segment slices (preserve split ratios for multi-beat segments), last beat → card_start; audio SHA stays identical.
- **AUDIO LOCK fails with "extracted timeline Ns but authoritative V1 final Ms"
  when the V1 mp4 is STALE (2026-08-06, row 69).** If a build's
  `make_narration.py` (or narration segments) was edited AFTER the V1 mp4 was
  rendered, the V1 mp4's audio is out of date and its duration won't match the
  current beats timeline. The runner CANNOT fix this — the assembler's hint
  ("set AUDIO_FROM_V1_SEGMENTS = True in beats_v2.py") requires editing
  beats_v2.py (outside runner writes) and is an author audio decision under the
  audio-immutability law. Diagnose (compare V1 mp4 mtime vs make_narration.py
  mtime; sum audio/*.mp3), write the root cause + resume into QC.md, mark the
  board row NEEDS-AUDIO with the stills-generated note, clear Ready, push, take
  the next row. The generated stills are valid and reusable — do NOT regenerate
  when the author later fixes the audio.
- **PRE-FLIGHT the AUDIO LOCK for $0 BEFORE generating stills (2026-08-06, rows 74 & 77). TWO independent gates — check BOTH.** Load `v2_assemble` + `extract_beats`, compute `total = data['total']`, `d = duration_of(V1mp4)`, and count placed mp3s whose `content_time` > the mp4's `content_time`+1.0 (`newer_mp3s`). Park NEEDS-AUDIO and generate NOTHING if EITHER fails:
  1. **RECENCY** (`assert_v1_final_is_current`): `newer_mp3s > 0` (mp3s changed after the V1 mp4 render). Row 74 = 19/19 newer, d 12.9s short.
  2. **DURATION** (v2_assemble.py line 531, the one I missed first time): `abs(total - d) > 1.0` — a mismatch in EITHER direction, not just `excess>0.75`. Row 77 tripped at d−total = **−1.74s** (V1 *shorter*) even though newer_mp3s=0, and it cost ~$2.40 to learn because the first version of this lesson only tested the positive-excess direction. BUILDABLE requires `newer_mp3s==0 AND abs(total-d) ≤ 1.0`. Shipped rows read `newer=0, |excess|≈0` (75: −0.47 ✓). From the row 75-100 batch, rows with `abs(excess)>1.0` (77 −1.74, 83 −2.20, 86 −1.06, plus the newer>0 rows 78/80/82/88/92/96/99/100) all fail — do NOT claim/generate them; they need an author `AUDIO_FROM_V1_SEGMENTS=True` edit first. Doing both checks at step 2 turns a ~$3-6 wasted-generate-then-park into a $0 park.
  - **The pre-flight MUST read the mp3s from `extract_beats.extract(row)["v1_dir"]`
    under `media-production/`, NOT the v2 build dir (2026-08-06, row 76 false
    alarm).** `assert_v1_final_is_current` locks to the V1 build's `audio/*.mp3`.
    Those are tracked, so `content_time` returns their git COMMIT time. The
    `media-production-v2/<build>/audio/*.mp3` copies are UNTRACKED, so
    `content_time` falls back to their checkout MTIME — always "newer" than the
    committed mp4 — and a pre-flight pointed there fires a false STALE-V1 on
    EVERY row (I saw 76–90 all "STALE", but with the correct V1 dir rows
    76/77/79/81/83/84/85/86/87 PASS and only 78/80/82/88/89/90 are genuinely
    stale). Resolve `v1dir = os.path.join(ROOT, data["v1_dir"])`, pick the single
    non-backup `*.mp4` in it, and call `assert_v1_final_is_current(row, v1dir,
    locked_final, data, total, duration_of(locked_final))` verbatim — never
    hand it the v2 dir. Batch-pre-flighting a whole authored block this way ($0)
    tells you which rows to build vs park before you touch the meter.

## COVERAGE / SCRIPTURE-DETAIL DRIFT
- **Provision-absence ("no purse, no scrip, no shoes") drifts back into the WIDE
  frames even when the close-ups obey it (2026-08-06, row 79 the-seventy-sent).**
  When a beat's must_show is the explicit ABSENCE (Luke 10:4 — the tracked pair
  set out empty-handed), the tight close-ups (b02/b03) land clean: empty hands,
  no bag on either shoulder. But the SENDING/HARVEST/RETURN wides (b01/b04/b09/
  b13/b16) quietly re-add a small shoulder scrip/satchel to the disciples — the
  model's default "traveller" silhouette. This is SUBTLE drift, not obvious
  garbage: it doesn't repeat a filed complaint and the beats where "no bag" is
  the spoken subject are correct, so under the COST LAW it is a FIX-WAVE note,
  NOT a reroll (rerolling a wide for one small satchel burns budget and the
  ROADS/plate re-seeds the same silhouette anyway). Log it in QC.md FIX-WAVE and
  keep the take; the fix wave can prop-edit the scrips out of the wides later.
- **Single-figure close-up beat renders in DAYTIME/SUNSET, ignoring a night row** (row 85 b04 "and the angel said" came back a rugged man in a dirty tunic against a bright golden daylight/sunset sky while all 22 other frames were deep night). Isolated 1-character beats (a portrait-style "X said/spoke" shot) lose the scene's time-of-day because the surrounding geometry is gone. Check the SKY/lighting on every lone-figure beat against the row's stated time of day, not just the wides; one reroll restored night. Mandatory reroll on a clear time-of-day mismatch.
- **Angel-announcement / tight-composition beats drop below the row's stated crowd COUNT** (row 85 s03/s05: three shepherds instead of the canonical four — the fourth falls outside the tighter angel framing). Subtle count drift in a non-count-named beat is FIX-WAVE, not a reroll; the wides still carry the full count. Glance at head-count on tightly-framed hero beats.
- **Heavenly-host / glory-light color drifts GOLDEN vs a row-canon WHITE** (row 85 s09 "Glory to God" came back amber while s08/s11/s12 read white-from-above). On angel-canon rows whose QC specifies WHITE glory light (never sunset tones), a golden take is borderline — FIX-WAVE it unless it reads as a literal horizon sunset. The host itself should be rank-upon-rank of INDIVIDUAL robed people, never a swirl of light (this held on 85).
- **A beat authored with an INTERIOR must_show renders a DAYLIT INTERIOR ROOM
  that breaks a night/outdoor story's continuity** (row 91 b10 "he did not hide
  it": a bright-windowed mud-brick room among 39 night-olive-garden frames). A
  reroll (`--only bNN --redo`) REPRODUCES the interior because the beat's own
  must_show drives it — it is NOT a generation fluke, so do not burn a 2nd
  reroll chasing it. It also does not hit any runner reroll-garbage criterion
  (subject present, only-Jesus-cream, no modern object, no lens-stare, anatomy
  fine), so the runner keeps the best take and logs it as a FIX-WAVE **author
  beat-text** item (rewrite must_show to the correct place/time, then --redo).
  Distinct from subtle drift: the whole SCENE (place + time-of-day) is wrong,
  but the fix is the author's beat text, not the runner's meter.
- **A promote-first PLACE plate propagates its static anchor composition onto a
  MOVEMENT/journey beat of that place** (row 101 b06 "went forty days ... unto
  Horeb": the HOREB plate was promoted from b12's cave-mouth frame, so b06 —
  which wants the tiny figure crossing vast country toward the far mountain —
  inherited the arrived-at-the-cave composition instead). Expected side-effect of
  place-locking by image; the destination beats look right, only the travel beat
  loses its "journey" wide. NOT garbage and NOT a reroll under the COST LAW
  (rerolling re-attaches the same plate) — FIX-WAVE note it. If a place has a
  distinct travel/approach beat, promote its plate from a WIDE anchor, or leave
  that one movement beat plate-free so it can render the journey.
- **Single-location OUTDOOR story drifts INDOOR on beats that don't lock the place token** (row 103 peters-confession b04/06/12/13/15/17 — the whole story is "the same glade under the pale cliff throughout," yet the 6 beats whose `locks` omit CLIFF rendered a generic house/village interior). The place PLATE attaches ONLY to beats whose `locks` name the place token, and when those beats' scene text carries no outdoor cue the model defaults to an interior. Rerolling does NOT fix it (verified: 2 rerolls of b13 both stayed indoor, and the first even broke Peter's locked face) — it is a coin-flip that burns meter (COST LAW) and can damage a locked face. NOT runner-fixable: log FIX-WAVE + author handoff (author adds the place token to EVERY beat's `locks` in a single-setting story, or adds an outdoor cue to the scene text, then regenerates only those beats). Do not burn more than one probe reroll confirming it stays indoor. **RESOLUTION CONFIRMED (2026-08-07 C-FIX):** once the author added `CLIFF` to the 6 beats' locks, a plain `--only b04 b06 b12 b13 b15 b17 --redo` landed ALL 6 outdoors first-try (0 extra rerolls) with Peter's face held — the author-lock-then-regen handoff is the correct, cheap fix for this class; do NOT reroll before the lock is added (it's a coin-flip that also breaks the face).
- **A COLLAGE reroll can return a CARTOON/CGI frame — budget for a 2nd attempt**
  (row 104 b06): rerolling a stacked-panel collage beat ("he ran to him" action)
  first landed a smooth stylized 3D/animated-film render (Law-14 mix fail), and
  only the 2nd allowed reroll landed a clean photographic single. Both collage
  AND cartoon are mandatory-reroll on sight, so an action/motion beat can legitimately
  need TWO rerolls; count on it when budgeting, and always re-view a collage reroll
  for STYLE, not just for "is it one panel now."
- **A beat that omits a character's REF drifts that character's costume/identity —
  a reroll will NOT fix it** (row 104 b14): n4 was authored with only the ELI ref,
  no SAMUEL ref, so Samuel's locked navy tunic rendered TAN and re-drifted tan on
  reroll (nothing to lock it). The runner cannot edit the beat (hard rail). Do NOT
  burn rerolls chasing a costume/identity drift on a beat whose `[+N char ref: …]`
  banner is missing that person — log it FIX-WAVE for the author to add the ref.
- **A single still renders ROTATED 90° (whole scene sideways)** (row 110 b07 "his
  name be honoured … kingdom come": a rooftop-figure-hands-lifted-over-the-town
  beat came back with the horizon running vertically down one edge and the figure
  lying sideways — the correct COMPOSITION, just rotated a quarter turn). It is
  outright garbage (nobody can read a sideways frame), distinct from the 16:9-
  letterbox-inside-9:16 defect. Mandatory reroll on sight; one `--redo` landed it
  upright. Tends to hit lone-figure "lifted hands / reaching outward" beats.
  **CONFIRMED AGAIN row 51 C-FIX (Cameron: "the first 2 pictures are sideways and
  bad, replace them") — TWO ADJACENT frames rotated at once (b01 crowd, b02 empty
  boats), NOT just lone-figure beats.** It also slips past an in-session QC that
  views frames one at a time, because a rotated frame still contains the right
  people/props; the tell is only the ORIENTATION (horizon vertical, everyone
  lying on their side). LESSON: at claim time, view the OPENING 2-3 frames of any
  built row specifically for orientation before trusting the ship — the first
  frames are what Cameron sees first and rotation there sinks the whole cut. One
  `--redo` each landed both upright; audio byte-identical (same SHA), ~$0.27.
  **CONFIRMED AGAIN row 82 QC-VERIFY full-cut gate (2026-08-11): a MULTI-FIGURE WIDE
  hit this, not a lone-figure beat — s12 "for ye have the poor" (a "speaks it soberly
  down the length of the table" supper wide) came back rotated a quarter-turn, the
  whole 7-figure table lying on its side. It sailed through the original 2026-08-07
  ship because that build's light-QC viewed contact sheets, where a rotated tile still
  shows the right people. Only the §6b full-cut gate (one frame per beat, straight
  from the rendered mp4, judged for ORIENTATION) caught it before Cameron. One `--redo`
  landed it upright; audio SHA de0b21ab unchanged; $0.13. Rotation is NOT limited to
  lifted-hands/lone-figure beats — screen EVERY beat for orientation, wides included.**
- **QC a promote-first plate for UNWANTED PEOPLE before promoting — a crowded
  anchor bleeds a crowd onto later beats of that place (row 114 abraham-sodom
  HEIGHT plate s05).** The HEIGHT anchor b05 ("for those cities had grown dark")
  is authored person-free (locks HEIGHT only, landscape must_show), but the model
  added a ~6-person foreground group. It was promoted anyway on the reasoning
  "the receiving beats' own text dominates" — WRONG: the crowd bled into 3 of the
  solo-plea beats (s10/s15/s20) where Abraham should be ALONE (Gen 18:22), while
  s08/s18/s21/s23 stayed correctly solo/person-free. Lesson: when the place's
  beats are meant to be solo or person-free, the plate anchor MUST be QC'd
  person-free BEFORE `--promote`; if the anchor rendered a crowd, reroll the
  anchor for a clean person-free plate first (one reroll on the plate is far
  cheaper than 3 FIX-WAVE regens downstream). Once promoted, the crowd is a
  FIX-WAVE (re-promote a person-free frame like s21/s23 and regen only the
  crowded beats), NOT a per-beat reroll.
- **`429 RESOURCE_EXHAUSTED "prepayment credits are depleted" is a REAL balance-
  zero, not the auto-reloading rate limit (row 114, 2026-08-06).** Distinguish
  the two: a rate-limit 429 clears on the one-retry-after-60s; a "prepayment
  credits are depleted" 429 persists after the retry and halts EVERY lane until
  Cameron tops up Google AI Studio billing. On the depleted variant, do the one
  retry per law, then park with the resume command in QC.md, push, and stop clean
  — no other row is buildable either (all need generation), so there is no next
  ready row to move to.
- **"Coats of skins" / any leather-garment beat renders as a MODERN tailored
  leather JACKET or trench coat** (row 113 b20 the-coats-found, and faintly
  b21/b24): a Genesis-3 beat asking for "garments of soft dark leather" comes
  back as a present-day leather jacket with a COLLAR, LAPELS and BUTTONS laid on
  a stone — a modern-object fail. One `--redo` landed raw draped animal HIDES
  (correct, untailored). Watch any beat whose prompt names leather/hide/skin
  clothing; the model defaults to modern outerwear. Reroll on sight when buttons/
  lapels/zippers appear; a slightly-modern seamed hide is FIX-WAVE. (For Adam/Eve
  a fur/hide look is CORRECT — the "never fur/fleece" rule is Jesus-only.)
- **A CLOTHED identity portrait (CAST-REF-V2/*.jpeg) REPRINTS its wardrobe onto
  every tight single/pair shot, defeating the beat's own covering wording (2026-08-07,
  row 113 Eden C-FIX, b15/b16/b19/b06).** Genesis-3 needs Adam & Eve nude→fig-leaf,
  but their committed portraits showed them in first-century WOOL (Eve = burlap hood +
  linen tunic, Adam = wool tunic). On WIDE beats the scene context won and they rendered
  fig-leaf/nude correctly; on TIGHT close-ups (b15/b16) and the standing pair (b19) the
  identity anchor dominated the composition and faithfully reprinted the portrait's wool
  = the exact "rags" the row was being C-FIXED for. **Three reroll passes could not beat
  it** — a clothed anchor + the base STYLE_V2 block ("clothing of rough-woven wool and
  linen", "head covering locked", "a mantle or shawl is one loose rectangle of cloth")
  overpower a per-beat "never rags" line at a face crop. This is NOT a runner reroll fix:
  the portrait and the beat text are both author-owned (hard rail). CORRECT RESPONSE:
  root-cause it by OPENING the CAST-REF-V2 portraits (not just viewing the frames), and
  if the anchor's wardrobe contradicts the story's required covering, PARK to author
  (NEEDS-REBUILD) with: regenerate the portrait in the story-correct covering (keep the
  face) + strengthen the tight beats with an explicit "own hair ONLY, NO shawl/
  head-covering/mantle-of-cloth" override. **Lesson-general: when a covering/wardrobe
  defect survives 2 rerolls on the TIGHT shots but the WIDES are clean, suspect the
  identity portrait, not the beat — open the CAST-REF before spending a third reroll.**
- **Pre-fall nakedness beats trip the Gemini safety filter (`'parts'` no-image, row 113
  b05).** The "they felt shame / saw they were naked" beat returned no image parts after
  retries. Keep the crop chest-up and lean on hair/foliage covering wording; do NOT add
  cloth to force it through (cloth re-triggers the very "rags" complaint). If it still
  blocks it is a beat-authoring reframe for the author, not a runner reroll.

## INFRA / BILLING
- **`429 RESOURCE_EXHAUSTED` with body "Your prepayment credits are depleted" is a HARD billing wall, NOT the transient rate-limit 429 (2026-08-06, rows 115 & 116).** The brief's "retry once after 60 s, billing auto-reloads" applies to the rate-limit 429 only; the *prepayment-depleted* message does NOT clear on a 60 s retry (verified twice). It is GLOBAL to the Gemini key — every concurrent lane hits it, so there is NO other Ready row to fall to (the same dead key blocks all of them). Correct response: retry once to confirm, then PARK the row (QC.md RUNNER PARK + exact resume command; keep any already-generated stills — they are valid, do NOT regen), leave the board/QUEUE noting "Gemini credits depleted — Cameron top up AI Studio billing," add a SESSION-LOG entry flagging the ACTION FOR CAMERON, commit, push, and STOP the session clean. Do not burn turns re-trying or hopping rows on a depleted key.

## C-FIX / COMPLAINT HANDLING
- **⛔ A TIMESTAMPED complaint MUST be resolved on the frame that RENDERS at that
  second — found from the SHIPPED mp4 + the window map — NEVER by guessing the beat
  from its NAME. Guessing the beat is how a "fixed" complaint SILENTLY REGRESSES and
  comes back three times (2026-08-07, row 13 roof — Cameron re-filed "1:40 the man is
  missing AGAIN, that was fixed previously but brought back").** Root cause of that
  regression: the frame Cameron sees at 1:37/1:40 is `s17-easy-to-miss` (window
  96.1–103.4s), which rendered ropes lowering an EMPTY mat (man missing + ropes-to-
  nothing = his "ghost ropes / weird room"). But the beat literally NAMED
  "…missing-the-man…" work went to `s18-the-four-sweat-streaked-faces` (window
  103.4–108.5s) THREE times — the man was "restored" in a frame that plays 3–5s LATER
  than the one he sees, so from his seat it was never fixed and looked like a
  regression. Each fix even PASSED its own QC by checking s18 at 105.5s — the wrong
  timestamp. THE GATE (do this every C-FIX, no exceptions):
  1. **Map complaint-second → asset via the window table**, not the name. The table is
     the dict at the bottom of `beats_v2.py` (`"sNN-...jpeg": ("segN", start, end)`),
     or `python3 -c "import beats_v2,bisect; ..."`. Cameron's clock is loose (±5s) —
     read the asset whose window CONTAINS the second AND its immediate neighbours.
  2. **Extract that exact second from the CURRENTLY-SHIPPED mp4** (`ffmpeg -ss <sec>
     -i <shipped.mp4> -frames:v 1`) and confirm with your eyes THAT is the frame he
     means before touching anything. The rendered mp4 is ground truth; the beat name
     lies (b18 is "four-sweat-streaked-faces" but the defect lived in b17).
  3. Fix THAT asset. **Verify by re-extracting the SAME second from the RE-BUILT mp4**
     — not the beat's mid-window, the complaint's second. If the defect frame isn't
     visibly different at that second, you fixed the wrong beat.
  4. A single defect frame can trigger MULTIPLE of his timestamps (row 13: the one
     empty-mat frame is both his "1:40 missing man" and his "1:49 ghost ropes/weird
     room they are dropping him into"). Don't split one frame's fix across two
     unrelated beats — find the ONE frame that explains all the words.
- **A shipped C-FIX mp4 must be committed WITH its changed assets in the SAME commit
  (row 13, contributing cause).** The prior ghost-rope ship committed only the mp4;
  `git log -- assets-realistic/s18…` showed its last commit was the EARLIER fix, so
  s14/s15/s18 sat UNCOMMITTED — the shipped render depended on working-tree files that
  any `git checkout`/clean would silently revert to the old frame. Always
  `git add -f` every touched `assets-realistic/*.jpeg` alongside the mp4 so the tree
  that built the cut is the tree in git. `git status assets-realistic/` must be clean
  after you ship.
- **"lost his beard at N seconds" is usually a WIDE-SHOT small-face drop, and the
  beat text hard-gating the beard does NOT guarantee it renders (2026-08-06, row 9
  b10).** s10-he-meant-it rendered the rich young man clean-shaven even though its
  own must_show/must_not_show demanded "SHORT DARK BEARD present and identical" with
  a CAMERON GATE — the model just dropped it on a small distant face. Beard-board the
  ACTUAL rendered frame against the character ref, never trust the prompt. Fix =
  `--only <beat> --redo` WITH the character REF wired (row 9's RULER lock pulls the
  bearded ruler-ref) — one reroll restored it. Map "N seconds" to the beat by
  cumulative segment/window duration before touching anything.
- **"the picture at M:SS is dumb / not needed" is a COVERAGE complaint, not a picture
  defect — REMOVE the beat, do NOT reroll it (2026-08-06, row 9 b13).** Rerolling a
  "better" version keeps a picture Cameron said shouldn't exist = complaint stands.
  Delete the beat dict and EXTEND the previous beat's `window` to cover the removed
  span (row 9: b12 67.84-73.49 → 67.84-78.49, b13 deleted). Audio stays byte-identical
  because v2_assemble builds the video track from beat `window` fields while the audio
  track is rebuilt independently from the V1 timeline — AUDIO LOCK still PASSes. This
  also directly answers Cameron's recurring "excessive luxuries / wasting api money"
  theme: fewer pictures = fewer chances for drift, and the removal is $0.
- **"the pictures aren't uniform — different boats / changing crew count / the
  subject wanders" is an AUTHOR boat-lock REBUILD, NOT a runner reroll — PARK it
  $0 (2026-08-06, row 11 storm).** A uniformity complaint (Cameron: "10 pictures of
  4 people in one boat and 10 of 6 in a different boat … some don't have Jesus in the
  boat at all") is NOT fixable by rerolling frames. Root cause is structural: the
  boat and the crew are locked in PROSE only ("the same EIGHT men, same boat") with
  NO reference IMAGE — so every Gemini generation invents a fresh hull and headcount,
  exactly like a face with no REF drifts. Uniformity requires an author to (a)
  generate ONE canonical boat plate, commit it as `PLACE-REF/BOAT.jpeg`, and wire a
  `REF:` line into EVERY hull beat (editing beat content + the lock = HARD-RAIL
  forbidden to the runner), and (b) regenerate ~25 frames (≫ the ≤15% reroll
  budget). Rerolling WITHOUT a wired boat plate just mints 25 MORE different boats
  and ships a cut that repeats the complaint = the worst failure. Correct runner
  move: build a labelled contact sheet, confirm the defect, write a RUNNER PARK +
  AUTHOR REBUILD SPEC in QC.md (boat-lock, EIGHT-man crew = crops never smaller
  crews, subject position-lock, plus any single named-frame identity fix), flip
  AUTHOR-BOARD State→NEEDS-REBUILD with Ready empty, $0. Same shape as the row-10
  audio park: complaint real, but the fix lives one stage upstream.

- **Lock rewritten but per-beat scene text still commands the old defect (row 15
  centurion, 2026-08-07).** Cameron's complaint (sick servant "age keeps changing
  … too grey … partially alive") had already triggered a SERVANT *lock* rewrite
  (eighteen, PALE-BUT-ALIVE, never grey), yet the shipped cut STILL showed a grey
  curly corpse in one frame and a 13-yr-old boy in three others. Root cause: four
  beats' own `scene`/`must_show` text literally said "He is very young … dark curls
  … soft grey" and "the boy … the boy's grey face." **The per-beat scene text
  OVERRIDES the shared lock** — the generator concatenates them, and the concrete
  beat wording wins. A lock fix is not applied until the contradicting beat wording
  is scrubbed too. Runner move on a repeat-complaint of a supposedly-fixed lock:
  grep the offending beats for the exact defect words ("boy", "grey", "curls",
  "child", age words), scrub them to agree with the lock, THEN reroll only those
  frames (char-ref anchored to a good kept frame). 4/41 rerolls, ~$0.54, audio
  byte-identical.

- **"Video stops playing / won't play through the N:NN mark" = a CORRUPT AAC
  PACKET in the mux, and it IS runner-fixable — not a NEEDS-AUDIO park (row 31,
  2026-08-07).** Cameron's complaint "stops playing and will not play through the
  1:59 mark ... i can skip past it and it will play but its not playing correctly"
  is a PLAYBACK/encode defect, NOT a re-voice. Diagnose it, don't guess: run
  `ffmpeg -v error -i <mp4> -f null -`; a corrupt audio packet prints
  `channel element X.Y is not allocated` / `Invalid data found` and stalls the
  browser player exactly where the bad packet sits. Confirm scope: `ffmpeg -v error
  -i <mp4> -map 0:v -f null -` (video clean?) and decode-check every source
  `audio/*.mp3` — if the sources are clean, the corruption is only in the final
  mux. FIX: set `AUDIO_FROM_V1_SEGMENTS = True` and re-assemble — the track is
  rebuilt from the build's own clean mp3s at the extract_beats offsets (byte-
  identical narration content, NOTHING re-voiced), producing a clean AAC encode.
  Proof of fix = the NEW mp4 decodes with ZERO `-v error` output. $0 / 0 rerolls,
  pictures untouched. This is DISTINCT from the audio-park class (pronunciation/
  pacing → re-voice → park); a container/encode corruption is the runner's own
  assembly step, so the runner fixes it.
- **A beat whose `must_not_show` GATE contradicts its own `scene` body is an AUTHOR park, NOT a runner reroll (2026-08-07, row 33 b20 "the nails black").** Row 33's prison-hand beat carried a CAMERON GATE in `must_not_show` forbidding black nails, yet its `scene` body still literally said "the nails black" — so every reroll re-paints them. The runner may not edit locked scene text, so rerolling only burns credits on a self-contradicting prompt. When a reroll target's own scene text PRESCRIBES the very thing an open complaint forbids, PARK NEEDS-REBUILD (author deletes the offending scene phrase, then regenerates that one still), $0. Also: a "Jesus is speaking words not spoken by Jesus" complaint on a righteous/crowd KJV quote is a SPEAKER reassignment (make_narration.py entry JESUS→SCRIPTURE), which fixes the wrong voice AND the wrong red caption in one edit — author/NEEDS-REBUILD, never a runner picture reroll.
- **"Random black spots on hands/fingers/lips" = a localized ink/blemish ARTIFACT, fixed by a targeted image-EDIT pass, not a full reroll (2026-08-07, row 39).** Gemini paints small blue-black ink-like smudges on laborer/tax-collector fingers, nails and occasionally a lip — Cameron reads them as "random black spots." They are cosmetic and localized, so a full `--redo` is the wrong tool (it changes the whole composition and can re-roll the smudge back). FIX: attach the finished frame alone to gemini-3-pro-image with an EDIT-ONLY instruction ("return the SAME photograph, remove ONLY the dark ink smudges on the fingers, keep every other pixel"), write to a `.cand.jpeg`, QC it at zoom AND full-frame (FACE-BOARD: no new figure, no crop/light drift), then promote over the original. ~$0.13/frame, composition and identity preserved, audio untouched → AUDIO LOCK stays byte-identical. Same technique fixes an anatomy read like "2 hands of the same side" — instruct it to correct ONLY the handedness to a natural left/right pair while keeping the pose. Sweep every hand/lip frame of that character in the same pass (touch-once), but only edit the ones that actually carry the defect.
- **"1 guy with 3 hands" / extra-hand anatomy comes from a figure doing TWO hand-actions PLUS holding a prop (2026-08-07, row 40 b26).** When a beat has a person leaning/knocking at a door AND carrying a lamp, Gemini can render a forearm to the forehead + a knocking fist + BOTH hands cupping the lamp = four hands. Cameron reads it as "1 guy with 3 hands." A plain reroll (`--only <beat> --redo`, new seed, same locked char-ref) usually resolves it in one take because the prompt already carries "Every figure has two arms, two hands and one head" — the extra hands were a seed artifact, not a prompt defect. QC the reroll by literally counting arms/hands. ~$0.13, audio untouched. If a reroll keeps re-adding the hand, escalate to a targeted image-EDIT ("keep the SAME photo, give him exactly two arms/two hands: one fist on the door, one holding the lamp").
- **"Floating lamp" = a hand-prop rendered with no support surface when its owner is out of frame (2026-08-07, row 40 b36).** On a person-free door/insert beat that still mentions "the lamp's small light," Gemini often paints the clay lamp hovering in mid-air against the wall/door because nothing in-frame holds it. Cameron reads it as "a floating lamp." A reroll grounds it when the scene has an available surface (a stone doorsill/step at the base of the frame) — the new take rests the lamp on that ledge. QC person-free light-source inserts specifically for "what is holding this object?"; if the answer is "nothing," it's a floating-object defect. ~$0.13, audio untouched.
- **"Captions are messed up / don't match the words" can be a whole-video TIMING drift, NOT a wording defect — and it is runner-fixable in assembly (2026-08-07, row 42).** Cameron: "the captions are messed up multiple times match them up to the words, the correct wordage." The caption TEXT was already correct (each segment's caption == its `timing.json` spoken text). The real bug: `beats_v2.py` still-`window`s had been scaffolded from a STALE `beats.json` written on an OLDER, SHORTER narration timeline (before this row's "REDO: new voice + pacing" re-voice lengthened the audio). The assembler draws CAPTIONS on the LIVE `extract_beats` timeline but places STILLS on `beats_v2.py` windows — so the whole picture-and-caption track ran progressively AHEAD of the voice (0s early → ~12s by the end) and the last still froze ~19s. DETECT: `python3 -c "import extract_beats; d=extract_beats.extract(R); print(d['card']['seg_start'])"` vs the max `beats_v2.py` window-end — good rows agree within ~0.1s; row 42 was off by +12.56s. FIX (assembly-only, no reroll, no re-voice): build a monotonic piecewise-linear A→B time map anchored on the stable per-segment `audio_start`+`spoken_end` pairs (stale beats.json = A, live extract = B), remap every `"window": "a-z"` in `beats_v2.py`, re-assemble → AUDIO LOCK PASS (narration byte-identical). Verify still+caption+word agree at ~7 rendered timestamps + the card. Only the `window` timing metadata changes — never scene text/locks. $0, 0 rerolls.
- **A character's DISEASE/skin texture bleeds onto whoever TOUCHES them at the point of contact (2026-08-07, row 54 b12+b14, the leper).** Cameron: "1:01 looks like Jesus had lepracy on his hand. That is wrong." When a beat's scene text describes the sick person's "ashen scaled skin" AND a healthy figure's hand landing on that skin, Gemini paints the ashen/scaly texture onto BOTH — the healer's hand/forearm picks up the leprosy patches. It ONLY happens in the frames where the healthy hand physically contacts the marked skin (the reach-in-air frame one beat earlier was clean). FIX: targeted image-EDIT pass (row-39 method), repaint ONLY the healer's hand/wrist/forearm as clean healthy skin, keep the patient's marks and every other pixel; a plain reroll risks re-rolling the bleed back and loses the composition. Sweep EVERY contact frame of that healing (touch-once) — count them: reach/hover frames are usually clean, only skin-on-skin contact frames carry it. The disease must live on the patient alone, never on Jesus. ~$0.13/frame, audio byte-identical.
- **A one-off recurring character with `locks` but NO `REFS`/GLOBAL_CAST entry renders TEXT-ONLY, and his face FLIPS shot to shot (2026-08-07, row 52, the synagogue demoniac).** Cameron: "The demoniac face kept changing. Beard to no beard to old man and his looks kept flipping." The beats file even carried a CAST-REF NOTE telling the runner to promote the first accepted face to `CAST-REF-V2/<char>-ref.jpeg` and wire `REFS` — but the A-auto ship skipped it, so every FREEDMAN beat invented a new face (clean-shaven / old-grey / young-stranger). A per-build lock token only auto-attaches an IMAGE if it's in `REFS` (build-local) or `GLOBAL_CAST` (library sheet on disk); a token that is neither is text-only no matter how detailed the LOCK prose — text never holds a face. DETECT before shipping any multi-frame single-character arc: `grep -q 'REFS *=' beats_v2.py` OR the token is in GLOBAL_CAST with a >50KB sheet; if neither, the face is unheld. FIX (C-FIX, no re-voice): pick the 1-2 keeper stills that best match the LOCK, copy them to `CAST-REF-V2/<char>-ref-*.jpeg`, add `REFS={"<TOKEN>":[...]}` (paths relative to the build dir), then reroll ONLY the frames whose face grossly deviates (`--only <beats> --redo`) — the gen log must print `[+N char ref: <TOKEN>]` on each. Keep every non-flipping frame byte-identical; don't chase subtle hair-length drift. The reroll count will exceed the 15% light-QC budget on a heavy single-character story — that's expected for this complaint class (the fix re-anchors a face across many beats); batch them all into ONE re-cut. ~$0.13/frame, audio byte-identical.
- **A complaint asking for ADDED scholarship / references / comparisons / "tell it differently" is an AUTHOR content rebuild, NOT a runner reroll or an audio re-voice (2026-08-07, row 59 feeding-4000 "second feeding").** Cameron's row-59 complaint wanted the narration to establish this as the distinct SECOND feeding, cite that Jesus himself commented on both (Matt 16:9-10 / Mark 8:19-21), and draw the 5-loaves/12-baskets vs 7-loaves/7-baskets comparisons. That is new spoken CONTENT that changes the beat map — the runner may not edit scene text or beat content, and no picture reroll touches it. PARK NEEDS-REBUILD (author rewrites narration, may add 1-2 KJV/comparison beats), Ready empty, $0, pictures + audio byte-identical. Distinct from NEEDS-AUDIO (pronunciation/pacing re-voice of EXISTING words) — this ADDS words, so it is author-domain. Also: a stale "COMPLAINT LEDGER: none open" from an earlier build does NOT mean none open — always re-run `v2_outline.py <row>` at claim time; row 59's complaint was filed AFTER the cut shipped.
- **RECURRENCE of the row-52 face-flip class (2026-08-07, row 55, the withered-hand man) + a profile-arm sub-lesson.** Same root cause as row 52: the beats file carried a CAST-REF NOTE telling the runner to build `CAST-REF-V2/hand-man-ref.jpeg` and wire `REFS`, the A-auto ship skipped it, so the MAN token was text-only and his face flipped across the arc (s03 heavy full-grey beard, s09 elderly long-white beard, s10 a YOUNG dark-haired man — three different people). This is now a CONFIRMED repeat, so make it MECHANICAL: at claim time for ANY row whose story follows one named non-Jesus character across ≥3 legible-face beats, run `grep -q 'REFS *=' beats_v2.py` — if it's absent, the face is unheld and the row WILL flip; build the anchor and wire REFS BEFORE the light-QC pass, not after a complaint. Fix method is identical to row 52 (crop the best keeper to the anchor, wire `REFS={"MAN":...}`, reroll only the wrong-person frames, gen log must show `[+1 char ref: MAN]`, keep matching frames byte-identical, audio byte-identical). SUB-LESSON (the "1:34 mutilated double right arm"): a figure drawn in STRICT side-profile reaching forward can render the near-side arm TWICE — once extended and once fisted at the belt — because both read as the same near shoulder; Cameron reads it as a doubled/mutilated arm. The anchored reroll fixed it in one take (the char-ref stabilizes the body plan); QC any profile reach-frame by counting arms on the near side.

- **Mother/family two-shots read ROMANTIC when the scene text pulls faces together (row 49 C-FIX).** "a hand's breadth from her son's", "the two faces stay close", "one hand risen toward her shoulder" produced a lover-like forehead-to-forehead / near-embrace between Jesus and his mother Mary — Cameron flagged it "weird". For any mother/son (or non-couple) beat, state a NATURAL, RESPECTFUL arm's-length and add must_not_show "faces not close, no touch, no romantic/intimate framing."
- **"Lamp/flame reflected ON a liquid surface" paints a flame INSIDE the cup (row 49 C-FIX).** b29's "the strung lamps' small flames riding its moving surface" rendered a lit candle-flame floating in the wine. For close-ups of liquid in a vessel, describe a soft even ambient light (NOT "glow" — drift-word) and must_not_show "NO flame, candle, wick, ember or bright point of light on or inside the liquid."
- **The V2 green-eyed Jesus lock can render as a flat pale-green STARE on a frontal, well-lit face (row 60 C-FIX).** b28's after-picture had Jesus frontal and lit; the lock's intended "green-amber-gold luminous" iris drifted to a washed-out pale-green that reads like colored contacts / a hunted stare — Cameron: "Jesus eyes do not look good." Do NOT edit the shared lock (v2_prompt.py). Reroll ONLY the offending frame; a downcast or three-quarter Jesus gaze in aftermath/after beats reads as warm depth instead of a stare. Spot-check the other Jesus close-ups first to confirm the drift is isolated to one frame (it was — every other close-up was already warm).
- **The JESUS LOCK v5 "eyes lit from within like a flame of fire" over-renders as GLOWING LIGHT-EMITTING EYES in high-radiance beats — reads as demonic (row 67 C-FIX, the Transfiguration).** Cameron: *"0:37 that picture is bad because jesus's eyes turned into light… looks like a demon."* In ordinary beats the lock's eyes render fine, but on a transfigured / blazing-white / glory beat the model amplifies "flame of fire" into literal glowing white-blue orbs. Do NOT edit the shared lock (v2_prompt.py). At claim time on ANY row with a transfiguration/glory/radiance beat, QC every Jesus face for glowing eyes and reroll the offending frame(s) — the brightness must stay on the RAIMENT and a face bloom, never the eyeballs. Sweep ALL radiance frames, not just the complained timestamp (row 67 had it in TWO frames, 0:14 and 0:37 — only the second was reported). WATCH the reroll: on this row the b07 reroll re-introduced the old cartoon tent-doodle Law-14 fail (its scene text says "hands sketching three tent-shapes in the air"), needing a second reroll — always re-QC a reroll for a NEW defect, don't assume the fix is clean. **UPDATE 2026-08-09 — DO NOT REROLL THESE; USE THE IDENTITY-EDIT (lesson 825).** Row 67 RE-OPENED: the 08-07 reroll of s03 REGRESSED — a blind reroll of a radiance beat re-amplifies "flame of fire" into glowing orbs again, so Cameron re-filed the identical demon-eyes complaint. A reroll cannot reliably kill Jesus light-eyes on a glory beat. The fix that HELD: gemini-3-pro-image edit "repaint ONLY the eyes as natural warm-brown human eyes, no glow" (input frame only, NO face REF, NO stylize words) → PIL feathered-ellipse composite (GaussianBlur 18) over just the eye box back onto the byte-identical original (s03 eye box `(675,790,855,865)`). 1 edit $0.134, 0 rerolls, audio byte-identical, every pixel outside the eye box unchanged. Treat Jesus light-eyes on a radiance/glory frame exactly like the storm white-eyes (825): IDENTITY-EDIT, never reroll.

- **A COMBINED complaint (picture drift + "the message isn't giving the fullness / teach it differently") is a WHOLE AUTHOR REBUILD, not a picture-only C-FIX — do NOT get lured into rerolling just the faces (2026-08-07, row 73 "this day fulfilled").** Cameron flagged BOTH that the first two Jesus pictures "look one way and then another" AND that the narration only reports the event ("he still reads it the same") instead of teaching the fullness — that Jesus meant every word, has risen, and continues the same plan today, framed the way the prophets/restored Church would teach it (without naming the church). The message half is RUNNER-LESSONS §511 author-content-rebuild; it changes the beat map, so the runner cannot touch it. Rerolling only the two drifting faces would ship a cut that STILL repeats the message complaint — the worst failure. When the dominant thrust is message/teaching, PARK the WHOLE row NEEDS-REBUILD and hand the author BOTH parts (the rebuild regenerates the opening stills, curing the face drift for free), $0, pictures+audio byte-identical. Rule of thumb: if ANY part of a complaint requires new/changed spoken content, the whole row is author-domain even when it also names a picture defect.

- **"This is the OLD pictures version, I don't know why I'm seeing it as fixed" is a REVIEWER DELIVERY / CACHE bug, NOT a picture defect — verify the mp4 before spending a single credit (2026-08-07, row 110 lords-prayer C-FIX).** Cameron filed this AGAINST the realistic-v2 ship's own hash. Extracting frames from the committed mp4 proved it was already fully realistic (olive-grove prayer, locked Jesus, realistic forgiveness scene) — the pictures were never the problem. ROOT CAUSE: every reviewer card streamed video from `https://github.com/noremacttevol/MBM/raw/main/<path>?v=<hash>`. That github.com/raw URL 302-redirects to `raw.githubusercontent.com` and **STRIPS the `?v=` query on the redirect** (`curl -sI` shows the `location:` header with no query). So the cache-buster the generator relied on did nothing — the browser cached the bare-path mp4 from BEFORE the ship and re-served the stale OLD cut every time Cameron reopened the reviewer. DETECT: `curl -sI "<github.com/raw URL>?v=x" | grep -i location` — if the location drops the `?v=`, the buster is dead. FIX ($0, no reroll, no re-voice, sweep ALL rows — it's systemic): point every `data-src` at the DIRECT host `https://raw.githubusercontent.com/noremacttevol/MBM/main/<path>?v=<hash>` (no redirect → `?v=` survives as a real browser+CDN cache key → a new hash always misses cache and fetches the current bytes). Also fix the generator (`media-production/gen_site_index.py` RAW_BASE line 30) so a regen can't reintroduce it. Verified: the direct URL returns HTTP 200, no redirect, exact content-length. This is the one complaint class where the correct action is to VERIFY-then-fix-delivery, never reroll — a reroll would burn credits re-making pictures that were already correct and would NOT fix what Cameron saw.
- **Head/face pressed THROUGH a barred cell grate (row 107 C-FIX, s05 "the two messengers at the cell door's grate").** A beat that puts a prisoner "close to the bars" speaking through the grate can render with the face + both hands jammed INTO the small barred window so the head reads as poking THROUGH the metal bars ("weird" — Cameron). Reroll for a composition where the prisoner is clearly BEHIND/inside the bars, face BESIDE the barred panel, hand on the bars — not through them. Watch the swing-back: a reroll can over-correct and stand the prisoner FREE in the corridor with the visitors (row 107 take 1) — the prisoner must stay visibly imprisoned. Do NOT edit the beat text (the scene already says "close to the bars"); it is a render-composition defect a reroll fixes.
- **A QC-named "person-free" promote-first plate can be authored to CONTAIN a distant figure — verify the beat's SCENE TEXT before promoting, and NEVER promote a Jesus-bearing frame (2026-08-07, row 51 BOATS/LAKE).** Row 51's author QC said "BOATS from b02 (person-free)," but b02's own scene text authors in "the crowd around the distant teacher" — a distant cream Jesus — so the render is NOT person-free, and b01 (the LAKE candidate) is Jesus+crowd. `v2_stash.py --promote` copies the WHOLE frame (distant figure and all) and wires it to every beat of that place, and the auto-`--wire` path explicitly refuses Jesus frames (`if not e["jesus"]`) for exactly this reason — a promoted distant cream figure becomes a spurious second-cream-robed figure across the place's frames. You may not edit scene text to strip the figure (hard rail). So: before promoting, `grep`/read the candidate beat's scene text; if it authors ANY figure (esp. Jesus/cream) into the plate frame, do NOT promote it — leave that place on its text lock and QC uniformity by eye. Log the decision in QC.md; it is not a defect, it is a forced no-promote.
- **A CRUCIFIXION-HILL WIDE renders as a fog-seam DOUBLE of the same scene, with the three crosses DUPLICATED top and bottom** (2026-08-07, row 94 father-forgive-them, b03 AND b10). A wide "brought him to the place / establishing the hill" beat came back as two stacked scenes split by a horizontal mist band — a distant three-cross hill in the TOP half and a second, larger three-cross scene in the BOTTOM half (row-45 double-perspective/collage family, but the tell here is the crosses appearing TWICE). It hit TWO beats on the same row, so it is a structural tendency of crucifixion-hill wides, not a one-off. Mandatory reroll on sight; one `--redo` each landed a single coherent wide (crosses at distance, one scene). QC every crucifixion/hill establishing or coverage wide for a horizontal haze seam and any duplicated cross/skyline before accepting.
- **A "tired / worn / spent Jesus" beat can push the exhaustion INTO his face and override the identity lock — producing a gaunt, hollow-eyed, blotchy-skinned, wild-haired stranger even with the REF attached (2026-08-07, row 11 calming-the-storm, b02 "He was worn through" @ 0:11).** Cameron: *"The picture of jesus tied [tired] is bad it doesn't look like him at all."* ROOT CAUSE was the beat's OWN prose — "his face drawn and hollowed with tiredness, dark shadows under his eyes, his lips dry and cracked… grey with tiredness" — which the model applied literally to his features, so the face left the locked Jesus entirely. A blind reroll of the same over-heavy prompt reproduces the same off-model face and wastes credits. FIX (root-cause, C-FIX-authorized): retune the beat so weariness reads through POSTURE and heavy eyelids ONLY (shoulders low, slow unhurried turn), and add a must_not_show that forbids gaunting/hollowing/blotching/greying/wild-hair and REQUIRES the reference man's warm olive-tan skin, smooth dark shoulder-length waves, full dark beard and warm brown eyes ("healthy and himself, just spent"). Then reroll ONLY that frame against jesus-face.jpeg. Rule: for ANY beat that asks Jesus to look tired/weak/spent/grieved, keep the emotion in body language and eyes — never in facial structure, skin health, or hair — or the face drifts to a stranger and repeats this complaint.
- **A RESURRECTION/empty-tomb story renders the tomb ALREADY OPEN on the PRE-reveal beats, and a reroll will NOT seal it (2026-08-07, row 97 the-empty-tomb, b03/b04).** The beats where the women are still ASKING "who shall roll us away the stone?" (b03, `must_not_show`: "the stone NOT yet visible as moved") and climbing "in the dark" (b04) both rendered the disc stone rolled aside with a dark OPEN doorway — the model's iconic "empty-tomb-open" postcard prior overrides the beat text and spoils the b05 reveal ("the huge stone that had sealed the tomb was rolled away"). ONE probe reroll each did NOT seal it (structural prior, not a seed fluke) — do not burn a 2nd. NOT runner-fixable: keep the best take, FIX-WAVE → AUTHOR adds explicit "the great disc stone SEALS the low doorway, tomb CLOSED, NO dark opening visible" to the pre-reveal beats' `must_show`, then regen only those. Same family: a pre-dawn tomb-APPROACH wide (row 97 b04) renders bright DAYLIGHT even when narration says "in the dark," because the beat text doesn't lock the pre-dawn SKY (§477 lone-wide-loses-night subclass, for tomb wides) — a reroll won't fix a time-of-day the text doesn't lock; author adds "pre-dawn darkness/night sky before sunrise/no daylight."
- **A TOUCH-NEGATION beat can render the actual touch it denies (2026-08-07, row 99 flesh-and-bone-thomas b10).** The beat narration was "He never did reach out and touch anything" (Thomas, John 20:29 — the offer is enough, he never touches), but the first take showed Thomas clasping/gripping Jesus's offered forearm — the frame contradicted its own text. The model gravitates to the more dramatic contact even when the scene prose says "hand stops short / does not touch." On any beat whose narration NEGATES a touch/grasp/reach ("never touched", "stopped short", "did not reach"), zoom the hands: if they make contact, reroll (one `--redo` landed a clean hand-raised-but-stopped take, $0.13). Same family as the action-logic law — QC "what does this person appear to be doing?" against the narration, not just against the still in isolation.
- **A HEALED/RESTORED subject keeps rendering with the ILLNESS he was just cured of — the post-healing/reunion frames read SICK even after the shot that made him well (2026-08-07, row 15 centurion, b41 "the word had been enough" @ 3:58).** Cameron: *"the servant shouldnt look sick in the last picture at 3:58 redo that one."* The closing embrace showed the healed servant with hollow, dark-ringed sunken eyes and a gaunt, drawn face — the model carries the sickbed prior (grey/pallid/hollow) forward into the AFTER frames because the same character was painted ill for most of the row and the char-ref/anchor may itself be a sick-state frame. ROOT is prose + anchor: the healed frame's scene text must not merely omit the illness, it must AFFIRMATIVELY state FULLY WELL (warm healthy skin, clear bright eyes, upright and strong) AND ban every leftover sick cue (grey/ashen/pale/sallow pallor, fever-sweat, sunken cheeks, hollow/dark-ringed eyes, cracked lips, sickbed frailty) — an author `must_not_show` HEALED-NOT-SICK ban. Then reroll ONLY the post-healing frame(s) against that prose and face-board vs the HEALTHY reference frames (not the sick ones). At claim time on ANY healing/resurrection/restoration story, QC every AFTER frame (reunion, "rose and was well", "sat up completely well") for residual illness, not just the sick-state frames. WATCH the reroll for a NEW anachronism: row 15's first reroll fixed the health but put MODERN SUEDE LACE-UP SHOES on the servant (period sandals elsewhere) — a second reroll fixed both. 2 rerolls / 42 beats = 4.8%, audio byte-identical.
- **Consecutive `wide:False` close beats set in the SAME place can all render as near-COPIES of that place's establishing WIDE — the crowd then flickers in/out across the intercut and any receding background line reads as "the army going the wrong way" (2026-08-07, row 66 malchus-ear, b04+b05 vs b01).** Three opening arrest beats — b01 (`wide:True`, Jesus on the prayer rock, torch column below) and b04/b05 (`wide:False`, meant to be TIGHT: disciples bunching / faces turned to Jesus) — all came back as the same Jesus-on-rock wide with the same background torch line. Watching the cut, the identical crowd appears, cuts to a close-up, then reappears identically = Cameron's *"people keep disappearing quickly and coming back"*; and because the establishing torch column trails AWAY uphill, the repeated wides read as the mob leaving = *"the army is going the wrong way."* The model anchors hard on the first strong composition of a place and reprints it for later same-place beats even when they're authored `wide:False`. FIX (runner-legal, C-FIX): reroll the offending beats so each lands its authored intent — one establishing wide, then genuinely DIFFERENT shots (mob ADVANCING toward the subject; interposition; faces-to-subject) — and make at least one frame show the crowd's direction UNAMBIGUOUSLY (leader walking toward camera) so no wide can read as "wrong way." One `--redo` each landed distinct shots (5/29 first-attempt, $0.67). At claim time on any multi-beat single-place opening, QC the sequence AS A SEQUENCE, not frame-by-frame: if two+ close beats duplicate the establishing wide, or a background procession's travel direction flips between frames, reroll for distinctness + one clear direction anchor.
- **"OUTCAST / SINNER / TAX-MEN" guest briefs make the model paint gratuitous facial SCARS, wounds and bandages on ordinary dinner guests; and small clay OIL LAMPS render with the flame coming out of the central FILL HOLE instead of the pinch SPOUT (2026-08-07, row 72 calling-matthew, feast frames s16-s21, Cameron @ 1:41).** Cameron: *"1:41 floating cups and lamps lit from the fill hole. and scars on people, for no reason."* ROOT CAUSE (scars): a "varied/human — tax men, the limping, the loud" or "outcasts/sinners" guest description gets read as physically INJURED people, so guests come back with red facial gashes, welts and arm bandages that no beat asked for. ROOT CAUSE (lamps): the base model's terracotta-oil-lamp prior lights the round top fill hole, not the rim spout — very common in any lamplit-table/feast interior. Also floating cups/vessels that don't sit on the surface. FIX that worked cheaply and touch-once WITHOUT a full reroll: gemini-3-pro-image IMAGE-EDIT each offending frame — "remove every facial scar/wound/bandage → clean healthy skin; move each lamp flame to the pinch SPOUT, fill hole closed; ground any floating cup with a contact shadow" under a hard "do not change any face/pose/composition/lighting" constraint. This preserves the composition Cameron already had and is ~$0.13/frame. **TRAP:** on the edit, do NOT attach the Jesus face REF and do NOT use the word "painting" — either one stylizes the frame into a CARTOON/illustrated Jesus and can paint a golden HALO around his head (Law-14 realism + no-glow violations). Run the edit with the input frame ONLY plus explicit "photorealistic, no halo/glow/rim-light, do not stylize" guardrails; if a frame comes back cartoon or haloed, restore the backup and re-edit with those guardrails. At claim time on ANY feast/meal/crowd interior, QC every guest face for scars/wounds/bandages that the narration never mentions, and every oil lamp for a fill-hole flame.
- **GLOWING WHITE / blank / pupil-less eyes on a JESUS frame = "white evil eyes"; fix by IDENTITY-EDIT with a byte-identical eye-box COMPOSITE, never a reroll (2026-08-07, row 11 storm, s04 @0:23, Cameron "the picture of jesus is bad it has white evil looking eyes").** A single Jesus frame can render his eyes as luminous white with no iris/pupil (demonic). Rerolling can't fix eye colour — the frame echoes the reference. The cheap touch-once fix: send ONLY the offending still to gemini-3-pro-image (input frame ONLY, NO face REF, NO "painting"/stylize words — see the row-72 halo/cartoon TRAP) with "repaint ONLY the eyes as natural warm-brown human eyes, dark pupils, normal sclera, no glow; change nothing else"; then in PIL composite ONLY a feathered ellipse over the eye box (row 11: `(930,1178,1070,1252)`, GaussianBlur 14) from the edit back onto the ORIGINAL still — so every pixel outside the eye box is byte-identical (honours Cameron's "keep everything else byte-identical"). FACE-BOARD recheck + confirm in the RENDERED mp4 at the complaint second. ~$0.13, 0 rerolls. Same method fixes any single-frame local defect (scars, fill-hole lamp) without disturbing a composition Cameron already accepted.
- **On a `--redo` of a BOAT/PLACE beat that also gains a face lock + multiple character refs, the payload cap silently DROPS the place plate (2026-08-07, row 11 b07/b08: "payload cap: dropping place plate BOAT").** v2_gen_api caps attached refs (~6) and drops the place plate FIRST when face + char refs fill the budget, so a hull can drift from the locked boat. In row 11 the attached rough_draft (the prior frame) still carried the hull, so the boats stayed consistent — but do NOT rely on it: after any boat/place regen that logged a dropped plate, eyeball the hull/place against the locked plate (planks, mast, sail, bow, anchor) and reroll if it drifted. Fewer char refs (drop redundant :quarter variants) keeps the plate attached.
- **Prose that asks for a GESTURE SEQUENCE in one still — "a small span, THEN thrown wide" / "the TWO measures distinct" — is a DIPTYCH trigger: the model renders two stacked panels (frame 1 = span, frame 2 = wide) with a hard horizontal seam instead of one moment (2026-08-07, row 109 b17 "if ye then being evil," the crazy-eyes C-FIX).** Distinct from the generic single-frame diptych coin-flip: here the beat's own "then / two measures" wording invites a comic-strip layout. It IS a coin-flip a single `--redo` fixes — the 2nd take landed one seated frame with one arm thrown wide (horizon) AND the small-span pinch both readable at once. When a beat's must_show describes a before→after gesture, expect the diptych and reroll for the combined single-moment pose; don't burn a 3rd credit — keep the best single-panel take and FIX-WAVE. (Runner may NOT edit the sequence prose out — that's a lock; the fix is the reroll.)
- **A cache/delivery complaint (e.g. row 110 "old pictures version") does NOT close when you hand-edit `REVIEW-LESSONS.json`/`COMPLAINTS.md` `open:false` — those files are Firestore-DERIVED and the next `admin/sync-reviews.mjs` (autopilot triggers it) overwrites your edit back to `open:true` (2026-08-07, row 110 C-FIX #3).** sync-reviews line 72: a complaint is open while `d.complaint && !d.approved`; line 61: approved needs `d.approvedHash === current hash`. So the ONLY thing that closes a complaint is Cameron pressing Approve on a fresh view (writes `approved` to Firestore), or an admin Firestore action setting `complaintOpen:false` for a confirmed non-defect. TWO prior row-110 sessions set `open:false` locally, "SHIPPED", and the sync reverted it every time — so the complaint-first picker re-dispatched row 110 as the lowest waiting complaint on the NEXT session, forever. DETECT: `git diff media-production-v2/REVIEW-LESSONS.json` showing committed HEAD `open:false` vs running-autopilot working copy `open:true` = the revert in the act. CORRECT ACTION for a verified cache/delivery non-defect: (1) confirm the live mp4 is byte-identical realistic (frames + content-length), (2) bump the card cache-buster to a token Cameron has never loaded so his next play is uncached, (3) make the card flag tell him to watch once + Approve, (4) deploy+live-verify, (5) DOCUMENT that it now awaits his Approve — do NOT touch the `open` state and do NOT fake his approval. Parking "awaits Cameron" is the honest, correct end state; a re-cut would burn credit re-making pictures that were already right.

- **A cache-buster query change is NOT a cfix — change the HASH (2026-08-07, row 110).**
  Row 110's "old pictures" complaint reopened 4 times. The first 3 sessions only
  appended a new `?v=` token to the video URL and left the mp4 byte-identical, so
  its content hash never moved off `824b4260`. Two things stayed broken: (1) the
  autopilot dispatcher fires a cfix whenever `open && reportedAgainst == live card
  hash`, so an unchanged hash makes it re-select the same row EVERY tick — an
  infinite auto-dispatch, not a fix; (2) a query token is only a browser hint, so a
  device that byte-caches the file by path still serves the old copy. The protocol
  cfix step — "Re-assemble (AUDIO LOCK PASS), redeploy" — actually changes the mp4
  bytes → new content hash → new commit hash. THAT is what breaks the reopen loop
  (`reportedAgainst != live hash`) AND gives a genuinely new file no cache can
  shadow. Re-assembly is $0 (no image re-gen). If a "delivery/cache" complaint keeps
  reopening on a row whose pictures are already correct, RE-ASSEMBLE to move the
  hash — never just bump the query string.

- **Face-lock a recurring one-off character with an UNAMBIGUOUS descriptor + 2-3
  agreeing image refs — not "streaked grey" and one loose ref (row 52 RE-OPEN,
  2026-08-09).** Row 52's demoniac face-flip complaint re-opened after the first
  C-FIX because that fix's own anchor note said the man had "dark hair streaked
  grey" and used two mildly-disagreeing refs. The word "grey" kept birthing an
  OLD grey-maned face (s08), hair length wandered to near-bald (s14), and beards
  flipped to shaved (s05/s07/s10). Lesson: any age/color ambiguity in a lock
  ("streaked grey", "greying", "middle-aged") WILL be rendered literally, and a
  fix that leaves the ambiguity re-opens on the next viewing. Lock it hard —
  "gaunt ~42, DARK brown-black hair (never grey, never bald, never cropped), FULL
  DARK beard (never shaven, never grey)" — AND attach 2-3 strongly-agreeing image
  refs (frontal + 3/4 + close), then reroll only the true outliers. $0.67/5.

- **A repeat of the EXACT same complaint means the prior fix never actually landed — re-verify the REROLL against the complaint, and never re-ship a complained frame byte-identical (2026-08-09, row 45, "0:50, 1:04 pictures trash... same problem you didnt fix either").** The 08-07 C-FIX rerolled b46 ONCE and shipped a frame that STILL had the defect (two men cut off at a terrace wall reading as floating disembodied heads + a duplicate mini-watchtower + a toy-diorama aerial), then wrote in QC "two small mid-ground workers... not the defect Cameron named" — rationalizing the very defect away. It also declared the OTHER named timestamp (1:04) "already clean" and left it byte-identical, so Cameron saw NO visible change at either spot → he re-filed word-for-word with "same problem you didnt fix EITHER." RULES: (1) after a complaint reroll, VIEW the new frame against Cameron's words and refuse to ship if the flagged look survives — do not narrate why it's "not really the defect"; if it looks stupid, it is. (2) If a named timestamp's frame is genuinely already clean, do NOT leave it byte-identical a second time — a viewer reads "unchanged" as "unfixed"; give it a fresh take that visibly moves (here b12: center-framed servant with a random torn tunic-hole → off-center servant in a whole tunic, distinct from the establishing shot), keeping the better draw. (3) Map every complaint timestamp to the frame in the RENDERED live mp4 (ffmpeg -ss), never the beat name. (4) A person-free authored beat that keeps hallucinating figures (b46 wants an empty vineyard) may need 2 takes — take the empty one, not the coherent-but-populated one. 3 rerolls/54=5.6%, ~$0.39, AUDIO byte-identical.

- **A "character reference" that is a WIDE SHOT is NOT a face lock — open every ref before you trust it (row 52 RE-OPEN #3, 2026-08-11).** Row 52's demoniac face-flip re-opened a THIRD time even after the 08-09 "unambiguous descriptor + 3 agreeing refs" fix. Root cause found only on the 3rd pass: two of those three "agreeing refs" (freedman-ref-a=s18, ref-c=s11) were WIDE ROOM SHOTS in which the man's face is ~30 px — they carry almost no identity signal, so the tool re-invented his beard/hair on every gen and both prior C-FIXes (which rerolled a few frames against those same weak refs) never actually matched anything. RULES: (1) Before trusting any `char_ref`/REFS image, OPEN it — if the person's face isn't a large, clear, well-lit region (roughly >15% of the frame), it is not a lock. Crop a tight head shot from the cleanest close-up and use THAT as the anchor. A recurring one-off face needs ≥1 tight face crop, not three wide establishing shots. (2) To fix identity drift on an otherwise-good frame, do NOT free-regenerate (it changes the composition and spawns new defects — this run's free regens produced a grey-old-man in a pale tunic AND a 3-panel triptych). Instead set `rough_ref` = the current frame + attach the tight face crop: the pipeline keeps the approved blocking and re-renders only identity (lesson-10 identity-edit, at scale). (3) When a complaint has re-opened twice, assume the LOCK ITSELF is broken, not the individual frames — inspect the reference images, don't just reroll again. 9 regens + 2 rerolls / 24 = 46% (a filed 3rd-re-open, touch-once), $1.48, AUDIO byte-identical.

- **A rendered prop/state can silently contradict the NEXT beat's required action — check continuity forward, not just the single frame (row 66 COMPLETE-RESTART, 2026-08-11).** On this restart b21's first take gave Jesus rope-bound wrists, and it passed a single-frame look (nice night arrest). But the very next beat b22 is "he reached out, touched the man's head, and made him whole" — bound hands can't heal, and the scene text for b21 itself says "held by both arms," not bound. RULE: when you gate a frame, glance at the beat before and after it — if this frame renders a STATE (bound/blindfold/kneeling/holding X) that the adjacent beat's action requires to be different, it's a defect even if the frame is pretty. Fix: reroll to the scene's actual staging (here held-by-arms, hands free). Also: a "complete restart" complaint on a whole video ("all the pictures are bad, very low grade") is NOT satisfied by a 5-frame patch — the 08-07 targeted fix is exactly why Cameron re-opened; regenerate ALL beats fresh (Cameron-mandated, not counted against the reroll budget) and gate the whole rendered cut. 2 gate rerolls/29=6.9%, ~$4.29, AUDIO byte-identical.

- **`AUDIO_FROM_V1_SEGMENTS=True` sources the V1 dir, so an audio-lane fix saved ONLY to the V2 build dir is ORPHANED and the OLD take ships even with the flag set (2026-08-11, row 119 "mispronounced bow").** The audio lane re-voiced n1 to the guaranteed /baʊz/ "boughs" take but wrote it to `media-production-v2/build-119/audio/n1.mp3`; `v2_assemble` with the flag reads `media-production/build-119/audio/*.mp3` (V1 dir), whose n1 was byte-identical to the OLD `.eleven-20260728` (md5 match). First assemble shipped the OLD "beau" audio. AUDIO REBUILD PASS does NOT prove the *right words/pronunciation* — only byte-consistency of whatever it read. VERIFY which take shipped: extract the segment window from the rendered mp4 and best-lag ENERGY-ENVELOPE cross-correlate (robust to AAC re-encode/normalization, unlike raw waveform corr which reads ~0) against BOTH the corrected and old mp3 — the mp4 matches whichever it rendered from (row 119: 0.973 vs corrected, 0.382 vs old). FIX (applying the audio lane's completed take, NOT a re-voice): if the corrected take is duration-identical (no timeline shift), copy it over the V1-dir mp3 and re-assemble; the AUDIO REBUILD SHA moves as proof. Whisper can't adjudicate beau/bough (both -> "bows"); the envelope corr + the "boughs" spelling in the corrected take are the proof.
- **A blind reroll of the FOURTH-MAN / any divine-radiance beat can RESOLVE the forbidden face — worse than the halo you were removing (2026-08-11, row 119 s22).** The beat forbids a resolved fourth face AND a ring of light, but the model's structural prior for "the form of the fourth is like the Son of God" is a glowing cream-robed Jesus. Reroll #1 to kill the halo instead painted a detailed bearded Jesus face (the #1 forbidden thing); reroll #2 restored a face "veiled in brightness" (the law's ALLOWED treatment). The radiance itself is structural and won't fully clear on rerolls. Rule: aim only for face-NEVER-resolved (turned/veiled/at-distance); accept the residual soft brightness as "veiled in brightness"; do NOT chase the halo with more rerolls (you'll resolve the face or re-amplify the glow). v2_gen_api overwrites in place with NO backup — if the pre-reroll take had the better (veiled) face, you've lost it, so weigh the first take before rerolling a radiance frame. Durable halo-dimming is an author beat-text tweak, not a runner reroll.
- **A BUILT/clean-pictures row can still hide a CAPTION↔AUDIO WORDING mismatch on SEVERAL segments — the full-cut gate must TRANSCRIBE the audio, not just read the burned captions (2026-08-11, row 84 no-room-manger).** The V1 make_narration script was tightened AFTER the ElevenLabs voices were cut, so extract_beats fed the caption filter the newer/shorter text while the mp3s speak the older/fuller take. n1 captioned "A command issued in a distant palace…" but the audio speaks "In those days a decree went out from Caesar Augustus, the emperor in far-off Rome…"; n6 and n7 the same. The captions LOOK internally fine (correct band, split, colour) — the only way to catch it is to transcribe the mp4 audio (faster-whisper small.en; global `whisper` was numba/numpy-broken) and diff each live segment's spoken words vs `extract_beats` `s["text"]`. FIX is assembly-only, $0, audio byte-identical: `TEXT_OVERRIDES={"n1":…,"n6":…,"n7":…}` in beats_v2.py with the timing.json spoken text (V1 never edited). Provenance check FIRST: audio-eleven.log + identical mtimes proved all segments are ONE ElevenLabs batch (same voice) → NOT a re-voice job, just stale caption text. This row ALSO carried the row-74 still-window drift (beats_v2 max window 190.68 vs live card_start 217.408, ~27s → s34 froze ~33s); both fixed in one re-assemble by remapping all 34 windows onto the live per-segment slices (row-42/89 method). AUDIO LOCK PASS does NOT catch either — always transcribe-diff + check captioned≈card_start on a stale-window batch row before it reaches Cameron.

- **A PERIOD-AMBIGUOUS UTENSIL (a fork) BAKED INTO A PROMOTED MEAL/ROOM PLATE propagates to EVERY wide of that place and CANNOT be rerolled away — plate-level fix only, not a runner reroll (row 89 last-supper, QC-VERIFY 2026-08-11).** The ROOM plate (s01) carries small forks among the table utensils; they re-appear in every ROOM wide (s05/s06/s09/s10/s12) because a `--redo` re-attaches the same plate that contains them (identical family to the systemic green-eye ref). Forks are an anachronism at a first-century meal, but they are BACKGROUND/non-subject, small, and the eye goes to Jesus + the bread/cup — below the Cameron-complaint glance-read bar (unlike blood/giant-Jesus/rotation), so on QC-VERIFY it is FIX-WAVE, NOT a re-cut (a re-cut voids approval + can't even fix a plate-baked detail). CRITICAL for reuse: this ROOM plate is wired BYTE-IDENTICAL into rows 170/185 (and any Last-Supper-night row), so the forks propagate there too — the durable fix is ONE plate-level regen (author removes the forks from room.jpeg, re-promote), which cleans every dependent row at once. Do NOT burn per-row rerolls on it.
- **JOY-BEAT BLOOD/WOUND OVER-RENDER (Cameron-grade, row 88 s14, QC-VERIFY 2026-08-11).** A crowd
  close-up on a CELEBRATION beat (Hosanna / triumphal entry) came back with a bleeding forehead
  gash, an under-eye cut, and raw chest abrasions on the shouting old man (+ a bloody-tear streak on
  a woman) — pure generation fluke: the beat text said "taxed / tired / occupied / the word's real
  cargo" and the model rendered SUFFERING as literal WOUNDS. Reads as injury/violence in a joy scene
  = a Cameron complaint. Light-QC missed it at full-frame (marks are small); the FULL-CUT GATE caught
  it only on ZOOM of the faces. LESSON: on any intense-emotion crowd close-up, ZOOM the nearest faces
  and check for stray red = blood/wounds before shipping; one `--only <beat> --redo` clears it
  (prompt text is fine, don't edit it). Applies to every "shouting/weeping/fervent crowd" beat.

- **A metaphor/illustration beat can render WITHOUT the absurd prop the narration
  explicitly names (row 122 b15 — "with an entire wooden beam sticking straight
  out of his own head" rendered with NO beam, just the fixer pointing at the
  brother's speck).** QC every illustration beat against the narration's named
  object, not just the locks — if the narration names the beam/lamp/coin and the
  frame omits it, the picture contradicts the words. Reroll (it usually returns
  with the prop on the first retry). Separate failure mode from the collage one:
  b04's single-figure ACTION beat ("he cannot even see straight") collaged TWICE
  before landing a coherent single frame — budget for a 2nd/3rd attempt on a
  single-figure action beat, per the known collage lesson.

- **AUDIO_FROM_V1_SEGMENTS silently DESYNCS the cut when the V1 beat structure
  differs from the v2 picture map — and the AUDIO LOCK will NOT catch it (row 95,
  QC-VERIFY 2026-08-11).** The AUDIO LOCK only compares the audio track's TOTAL
  duration to the video's (row 95: 70.67s ≈ 70.70s → PASS), so a per-segment
  structural mismatch sails through. Row 95's audio is built from
  `extract_beats.extract(95)` = the V1 **10-beat** timeline whose beat-3 is a modern
  paraphrase ("If you're really the Christ, save yourself and us"); the v2
  `beats_v2.py` **11-beat** PICTURE map has `n0b` ("That was one of them, sneering")
  there and no paraphrase. That stray ~3.4s segment pushed all back-half audio ~4s
  behind the pictures — Jesus SPEAKS "today shalt thou be with me in paradise"
  (52.8–54.4s) while the picture is the thief ALONE. **VERIFY RULE for the FULL-CUT
  GATE: when a row sets `AUDIO_FROM_V1_SEGMENTS = True`, do NOT trust the duration
  match — TRANSCRIBE the delivered mp4 (faster-whisper word timestamps) and confirm a
  known line (esp. the Jesus red-letter line) is spoken while ITS picture is on
  screen. A ≥1-frame drift that grows across the video = structural desync = BLOCK
  → NEEDS-REBUILD (author lane; the audio lane's AUDIO_FROM_V1 rebuild only
  reproduces it). Compare `extract_beats.extract(row)`'s beat list against
  `beats_v2.py` BEATS one-to-one; any count/content mismatch is the smoking gun.**
  **AUTHOR-LANE FIX (row 95, 2026-08-11, $0, no re-voice, V1 read-only):** the audio
  (from `extract_beats`) is the SOLE timing authority; the beats_v2 `window` fields
  ONLY control when pictures SWITCH. So do NOT try to strip paraphrases out of the
  read-only V1 mp3s — instead RE-TIME the picture windows to the audio that actually
  plays: transcribe the delivered mp4 (faster-whisper), then set every beat's window
  START ~0.2s before its own spoken line's first word (contiguous, `end` is cosmetic
  — only `start` is used, each beat holds until the next beat's start). Re-assemble
  (`v2_assemble.py <row>`; audio stays byte-identical, same AUDIO REBUILD hash), then
  RE-TRANSCRIBE + frame-check the new mp4 to prove the Jesus line lands on the Jesus
  frame. Ship: board NEEDS-REBUILD→BUILT, reviewer card repointed (new mp4 sha256 as
  data-hash + ?v=, remove data-machine-reason, flag→QC-VERIFIED, card text tells
  Cameron the timing was fixed), deploy + live-verify served-bytes == local. The V1
  narration's redundant paraphrases (a KJV line + its modern echo) are pre-existing
  content, NOT the defect — leave them; the fix is purely picture timing.

- **The STALE-V1 pre-flight has a STRICTER gate than the documented `abs(total-d)≤1.0`
  heuristic — `assert_v1_final_is_current` refuses on RUNTIME EXCESS > 0.75s, so trust the
  actual assembler guard, not the loose rule (2026-08-11, rows 125/126/127 batch pre-flight).**
  The pre-flight lesson above says "BUILDABLE requires newer_mp3s==0 AND abs(total-d) ≤ 1.0."
  But `v2_assemble`'s own `assert_v1_final_is_current` (default path) throws when
  `locked_duration - total > 0.75` (an EXCESS means the V1 mp4 carries audio the current
  mp3s no longer have). Rows 125 (+0.893), 126 (+0.969), 127 (+0.889) PASS the ≤1.0 rule
  but FAIL the real 0.75 guard — a generate-then-can't-assemble trap (~$2/row wasted) if you
  trust the loose heuristic. Run the actual guard in the $0 pre-flight
  (`assert_v1_final_is_current(row, v1dir, locked, d, total, dur)` in a try/except). A ~0.9s
  excess with newer=0 across CONSECUTIVE rows is REAL extra content, not tail-silence noise:
  validated against shipped rows 121-124 which all land ~0.04s excess (121 +0.038, 122 +0.047,
  123 +0.015, 124 +0.073). Such rows are picture-runner-unbuildable — PARK NEEDS-AUDIO for the
  audio lane to set `AUDIO_FROM_V1_SEGMENTS=True` (rebuild from V1 mp3s, nothing re-voiced),
  which then makes them buildable. Batch pre-flighting the whole authored block this way ($0)
  tells you which rows to build vs park before touching the meter.

- **AUDIO_FROM_V1_SEGMENTS crashed on a SILENT question card (2026-08-11, row 128, audio
  lane).** `rebuild_audio_from_segments` unconditionally appended the card's mp3, so a row
  whose closing question card is silent (`beats.json "silent": true` → `card seg=None,
  audio_start=None`) died with `missing V1 segment audio audio/None.mp3` — blocking the
  sanctioned STALE-V1 fix. FIX (shipped in v2_assemble.py): only place the card when
  `data["card"].get("seg") is not None`; a silent card contributes no audio and the existing
  `apad=whole_dur=total` already pads the track through its on-screen duration. Spoken cards
  (seg='card') are unchanged. Any future silent-card row now rebuilds cleanly.

- **A CARVED EMBLEM on a stone prop (throne/judgment-seat/shield/lintel) can hallucinate
  a MODERN OBJECT — row 93 baked a literal BICYCLE (two wheels + frame + handlebars) into
  the judgment-seat backrest** (2026-08-11, QC-VERIFY of the BUILT cut before Cameron saw
  it). It was in the b01 anchor, so the promoted PAVEMENT plate carried it and it appeared
  in ALL 7 seat-wides. Two lessons: (1) at CLAIM/plate-QC time, zoom any decorative
  carving on a prop and read it literally — "what does this emblem actually look like?" —
  a plain seat back is safer than an invented symbol. (2) When a plate-level defect has
  already propagated to N frames, DO NOT reroll N times (blows the budget and re-drifts
  faces): run a **localized `gemini-3-pro-image` edit pass** (attach the finished frame,
  instruct "preserve everything EXACTLY, change ONLY <the defect>") — it kept every face,
  pose and the only-Jesus-cream lock intact across 7 frames for $1.07, and the audio stayed
  byte-identical so no re-voice/approval churn. Re-promote the plate from the FIXED anchor
  afterward or the warehouse re-propagates the defect. One edit occasionally leaves a faint
  remnant (s07 here) — re-verify the actual rendered mp4, not just the asset, and retry that
  one frame.

- **Establishing WIDE that names FOREGROUND REF characters can go giant-composite,
  and a reroll makes it WORSE, not better (row 95 b01, QC-VERIFY 2026-08-11).** An
  opening "the three of them against the sky, behind the watchers" wide that also names
  the crucified trio prominently kept compositing a GIANT chest-up foreground trio over a
  correctly-scaled miniature crowd (haze seam at the crest). Three attempts across sessions
  failed; the QC-VERIFY reroll came back worst of all — the model pasted the REF portraits
  as literal FRAMED RECTANGLES onto the tops of the crosses. This is a STRUCTURAL collage
  class a runner reroll CANNOT win (like rows 45/66/82 collages). STOP after one reroll
  (COST LAW). The fix is a BEAT-TEXT change (author lane, runner barred): make it a TRUE
  distant establishing wide — a person-free PLATE establish, or place the named figures at
  genuine distance on their crosses — and do NOT keep them as foreground giants. Park
  NEEDS-REBUILD, pull the card from Cameron's queue (data-machine-reason), name the defect.

- **The row-84 caption↔audio mismatch ALSO hits FRESH first-attempt authored rows, not just STALE-V1 rows — the FULL-CUT GATE must transcribe the mp4 on EVERY build (2026-08-11, row 131 scribe-near-the-kingdom).** A brand-new V2 build with `AUDIO_FROM_V1_SEGMENTS` unset (audio copied from the V1 mp4) still shipped 4 narrator captions that didn't match the voice: the V1 `SEGMENTS` narration SCRIPT (which extract_beats reads for caption text via `s[4]`/`s[2]`) was tightened AFTER the ElevenLabs voices + `audio/<seg>.timing.json` were cut, so the captions printed a shorter/different NARRATOR draft the mp3s never speak (KJV/scripture segments + n0a/n3/card all matched — it's narrator-only). DETECT the same way regardless of engine flag: transcribe the delivered mp4 (faster-whisper small.en) and diff each live segment's spoken words vs its `audio/<seg>.timing.json` text (the word-timed ground truth), NOT vs the outline/SEGMENTS. FIX = `TEXT_OVERRIDES={"n0b":…,"n1":…,"n2":…,"n4":…}` in beats_v2.py set to the timing.json spoken text; re-assemble → AUDIO LOCK PASS with the SAME SHA256 (byte-identical, $0, zero re-voice). Do NOT assume a fresh row's captions are correct because it isn't a STALE-V1 rebuild — a light contact-sheet QC never reads the burned caption against the voice; only the transcribe step catches it.

- **A background CREAM figure in a jesus=False beat is often the AUTHOR-INTENDED disciples' band, not a stray Jesus-double — READ THE SCENE TEXT before rerolling it (2026-08-11, row 132 b10).** b10 ("whoever isn't against us is on our side") came back with a cream-robed Jesus walking the lane behind the stranger's mercy; I read it as a stray second-cream defect and rerolled — but the beat's SCENE TEXT explicitly authors BOTH groups ("down the bright lane the little band of disciples walks the road… two crews of the same kingdom… no fence between them"), so the cream figure IS Jesus's band, intended. Both takes were valid; the reroll was a wasted $0.13. Before spending a reroll on a background cream figure, grep the beat's `scene`/`must_show` for "disciples"/"the two groups"/"band" — if the composition authors Jesus's group, keep it (a locked-face reroll or FIX-WAVE for the unlocked background face is the only real concern, not its presence). Cost-law: read-before-reroll.
- **A recurring cast token wired TEXT-ONLY (no image REF in the build's REFS dict) WILL drift, and a reroll is a coin-flip, not a fix (2026-08-11, row 132 JOHN).** build-132 locked JOHN by prose only (REFS held STRANGER but not JOHN); b05's JOHN came back younger/fairer/straighter-haired vs the dark tight curls of his other 6 beats. One probe `--redo` happened to land a matching JOHN, but per the continuity law a text-only token that drifts is an author gap (wire the REF), not a runner churn — do ONE probe then FIX-WAVE, never chase it with multiple rerolls.
- **A frame can carry a ROLLABLE defect AND an UNROLLABLE one at once — reroll the rollable half, flag the rest; don't discard the row (row 97 b03/b04, 2026-08-11).** The empty-tomb approach beats shipped with BOTH bright-daylight-under-"in-the-dark" (TIME-OF-DAY, a named law) AND the disc stone rolled aside before the b05 reveal. The scene text was actually CORRECT ("half-dark" / "wide grey frame" / "stone in its channel") — so the LIGHTING was pure generation drift and a reroll fixed it (midday→dusk, flat-day→blue-hour). But the OPEN-TOMB is the model's iconic empty-tomb prior and survived 3 rerolls (RUNNER-LESSONS "continuity surviving 2+ rerolls = beat-text" — needs the AUTHOR to add "disc stone SEALS the doorway, tomb CLOSED"). Lesson: on a mixed-defect frame, don't blind-reroll forever and don't park the whole row — reroll to clear the rollable/named-law half (what would make Cameron type a complaint), keep the best take, and hand the iconic-object prior to the author lane as a text-seal FIX-WAVE.
- A ROTATED-90 (sideways) still (row-110 class) can SURVIVE reroll-1 (row 100 b04, 2026-08-11: reroll-1 came back rotated the OTHER way — a strong scene prior). reroll-2 fixed the rotation but DRIFTED the location INDOOR because that beat's `locks` carry no place token (row-103 indoor-drift class stacks on top). So on a rotation reroll of a place-tokenless beat, budget for the upright take to also lose the outdoor setting: keep the upright frame (upright >> sideways), FIX-WAVE the location (author adds the place token, then `--only <beat> --redo` lands it outdoors first-try). Do NOT burn a 3rd over-budget reroll chasing both at once.

- **A FROM-SCRATCH / REPLACED row can read "Ready ✅ / Audio OK" on AUTHOR-BOARD yet have NO assemblable audio — PRE-FLIGHT it for $0 before spending (2026-08-11, rows 133 + 134 parked).** Some authored-from-scratch rows never had their V1 audio landed: the V1 dir (`media-production/<build>/`) has NO final `*.mp4`, its `audio/` holds only `.timing.json` (**zero `.mp3`**), and `beats_v2.py` has no `AUDIO_FROM_V1_SEGMENTS` flag — so NEITHER `v2_assemble` audio path can run (locked-mp4 path finds no mp4; segments path `SystemExit`s on missing mp3), and `extract_beats.extract(row)` itself CRASHES (`dur_of('')` ValueError) because the beats carry SEGMENTS text so it doesn't skip the missing mp3. The narration usually exists only as V2-dir mp3s + V1 `segs/audio_mix.m4a`. CHECK at claim time (all $0): `ls media-production/<build>/*.mp4` (must exist) OR (`ls media-production/<build>/audio/*.mp3` present AND `grep -c 'AUDIO_FROM_V1_SEGMENTS = True' <v2build>/beats_v2.py`). Every buildable sibling (rows 100/105/108) has a V1 mp4 + V1 audio mp3s + the flag. If all are absent, do NOT generate — restoring V1 audio / setting the flag is AUTHOR/audio-lane work (hard-protection #1 + audio-immutability). $0 park (board State NOT-READY, Ready cleared) beats a ~$6 strand of stills that can never assemble.

- **The AUTHOR-BOARD "Audio OK" column does NOT catch a STALE-LONGER V1 mp4 — pre-flight the AUDIO LOCK for $0 BEFORE generating (2026-08-11, row 141 parked after $1.34 of stills).** Row 141 read "Ready ✅ / Audio OK", but at assembly `v2_assemble` refused: current V2 segments timeline = 61.022s vs the authoritative V1 mp4 = 68.700s (a 7.68s gap — the V1 mp4 was the old 7-still 1:09 cut, its audio no longer matches the re-cut segments). The stills were fine and are banked (row-118 template: audio lane sets `AUDIO_FROM_V1_SEGMENTS=True`, verifies the segs are new-voice, re-assembles, ships), so the spend isn't lost — but a $0 pre-flight would have parked it NEEDS-AUDIO before touching the meter. CHEAP PRE-FLIGHT at claim time, regardless of the board's Audio column: compare `extract_beats` timeline total vs the V1 mp4 duration (`ffprobe`); if `|timeline - mp4| > 0.75s` AND the beats_v2.py has no `AUDIO_FROM_V1_SEGMENTS=True`, it's a STALE-V1 park (audio lane), not a build. This complements the earlier +0.9s consecutive-rows lesson — the same guard catches both the small-excess and the large-stale-mp4 cases.

- **The $0 audio pre-flight MUST check BOTH halves — a duration match does NOT mean buildable (2026-08-11, row 147: gap 0.015s but 11 newer mp3s → still STALE-V1).** My row-141 lesson said to compare `extract_beats` timeline vs the V1 mp4 duration, but row 147 passed that (0.015s) and STILL failed the AUDIO LOCK because `v2_assemble`'s SECOND tripwire fires when any V1 `audio/*.mp3` has an mtime NEWER than the V1 mp4 (re-recorded narration over an older render). The correct claim-time pre-flight (matches RUNNER-LESSONS "BUILDABLE requires newer_mp3s==0 AND abs(total-d) ≤ 1.0"): `mp4=newest non-backup .mp4 in media-production/<build>/`; BUILDABLE only if `abs(extract_beats total - ffprobe(mp4)) ≤ 1.0` **AND** `count(mp3 in <build>/audio with mtime > mtime(mp4)) == 0` AND the beats_v2.py has no AUDIO_FROM_V1_SEGMENTS flag. If EITHER fails → STALE-V1 → NEEDS-AUDIO park (audio lane sets the flag). The whole 141-149 I-AM/OT block was authored with 2026-07-28 re-recorded narration over ~2026-07-24 mp4s, so all but 148 are stale — this two-part pre-flight parks them at $0 instead of after generating.
- **In a TWO-AGE-ONE-FACE story (one character rendered at two ages from a single multi-panel ref sheet), the age a beat renders is driven by an explicit age CUE in that beat's OWN scene text — NOT by the ref, and a reroll does NOT move it (2026-08-11, row 150 shepherd-psalm b11/b16).** build-150's DAVID sheet holds BOTH a ~50 royal-blue KING and a ~17 ruddy rust-tunic SHEPHERD. Beats that say "young David"/"the young shepherd" (b02/b06-09/b13/b15) rendered young; beats that say only "the shepherd"/"the guest" (b11 valley, b16 anointing) rendered the MATURE KING, leaving an age flip against the adjacent young frames. Rerolling b11 AND b16 did NOT change the age (it is text-cue-locked, same as costume/identity drift on a ref-less beat, lessons 1108/1112) and wasted meter — one probe even dropped b11's required rod. RULE: when a two-age story renders a beat at the wrong age, DON'T probe-reroll it — grep the beat's scene text; if it lacks the age word its siblings carry, it is an AUTHOR beat-text fix (add "young …"/"the old king …"), PARK NEEDS-REBUILD, keep the banked frames, regen only those beats after the text edit. Recognize this at plate/anchor QC time (my b11 GORGE anchor rendered old before the batch — that was the early signal) and park immediately instead of spending rerolls. (Companion: a "both halves / two-location" CLOSING beat — b21 "the fold AND the palace table" — is the structural-diptych magnet of lesson 481/954: 3 takes all hard-seam collages; also author-domain, de-scope to one scene, never ship a split-panel closing frame.)

- **AUDIO/AUTHOR HANDOFF MUST LEAVE THE `Claim` CELL EMPTY OR THE ROW STRANDS FOREVER (2026-08-11, swept 14 rows).** The autopilot runner picker (`autopilot.sh` ~line 218) fires only on `State==AUTHORED and Audio==OK and Claim.strip()=='' and Ready==✅ and not active`. An audio-fix/author lane that writes its completed "…DONE → handed to picture runner" note INTO the `Claim` column (col 6) leaves `Claim` non-empty, so the runner skips the row — AND no other branch picks it up (resume only rescues `State==RUNNING/A-auto`; the audio lane only takes `NEEDS-AUDIO`). The AUTHORED+claim-filled row falls through every branch = a permanent dead zone = "a park with no pickup is a complaint left waiting" (the exact LOW-NUMBER-LAW failure). This had silently stranded Cameron's LOWEST videos incl. complaint rows 63 (Siloam) & 149. **FIX: on any audio/author handoff, put the detail in the row's QC.md + the committed code flag (`AUDIO_FROM_V1_SEGMENTS`), set `Ready ✅`, and leave `Claim` BLANK.** Swept clear on 2026-08-11: rows 63,105,106,108,125,126,127,128,135,136,138,139,146,149 (146 also needed `Ready` set). A claim-clear is $0 board hygiene — it does NOT build a claimed row (rule-1 is about RUNNING strands), it re-enables autopilot's own picker.

- **A TEXT-ONLY place/prop lock (no reference image in `REFS`) drifts on WIDE establishing shots even when the prose lock is strong — the fix is one targeted `--redo`, or wire a rough_ref crop if it recurs (2026-08-11, row 51 boat-scale complaint).** Cameron: "the boats need to stay the same size, find all the pictures where the size changes and fix them." The `BOATS` lock reads "broad-beamed dark oiled-cedar boats … high curved prow, single stubby mast" — detailed, but TEXT-ONLY (REFS held only SIMON/JAMESJOHN face sheets). Every boat frame rendered the canonical dark boat EXCEPT the one wide teaching shot (s05/b05), which drifted to a small pale open dinghy — half the size, wrong wood, no prow/mast — a jarring size flip between s04 and s06's big dark boat. This is the SAME failure mode as text-only FACE locks (memory: drift that survives a text lock needs an image anchor): the wider the shot, the less prose alone constrains a large prop. HOW TO CATCH IT: on any multi-boat/multi-vehicle/multi-building story, at QC extract one frame per beat from the RENDERED mp4 and eyeball the recurring large prop side-by-side — a single wide-shot outlier is the tell. FIX: `--only <beat> --redo` with the explicit prose lock usually lands it in ONE gen (it did here, $0.13, 3.8%); if it drifts again, set the beat's `rough_ref` to a crop of the canonical prop from an adjacent correct frame (same technique as the tight-face-crop identity edit) rather than blindly rerolling.

- **A FACE-LOCK LOOP THAT SURVIVES 3 FIXES MEANS THE ANCHOR IS WRONG, NOT THE METHOD — OPEN THE REF CROPS AND CONFIRM THE TRAIT YOU KEEP LOSING IS ACTUALLY PRESENT IN THEM (2026-08-11, row 52 demoniac, 4th RE-OPEN).** Cameron re-filed the same "beard to no beard to old man, none match each other" complaint a FOURTH time. Every prior fix used the right technique (tight face crop + `rough_ref` identity-edit) but the beard kept flipping full→thin→shaven. ROOT: BOTH C-FIX#3 "face" refs (`freedman-face.jpeg` + `freedman-ref-b.jpeg`) had been cut from **s17 — the ONE frame in the whole cut where the man's beard is thinnest/near-shaven.** So every identity-edit was faithfully conforming his face to a near-beardless anchor; the full beard could only appear when the TEXT lock happened to win, which is exactly a flip. TWO compounding lessons: (1) **When a trait keeps drifting despite an image lock, open the ref crops full-size and verify the trait is IN them — a ref cut from the frame where the trait is weakest teaches the model to drop it.** Cut the anchor from the frame where the canonical trait is STRONGEST (here: full-dark-beard s10 3/4 + s08 frontal), throw the weak refs away. (2) **`rough_ref` (identity-edit) PRESERVES the draft's version of the drifting trait — it cannot ADD a beard the draft doesn't have.** To force a trait the drafts lack, set `ROUGH={}` and FRESH-generate against the corrected anchor so the beard is built in, not borrowed. Fixed in ONE touch-once redo: 9 fresh regens, 0 rerolls, $1.21, full dark beard consistent across all 24 beats. (Companion, same row: a beat with NO place lock wanders out of the story's room — b16 `locks=["FREEDMAN"]` only had drifted to an outdoor courtyard with different helpers; adding `SYNAGOGUE` + interior scene text pinned it back inside. On a single-location story, every legible beat should carry the location lock.)

- **A CHARACTER token with a strong TEXT lock but NO `REFS` entry renders TEXT-ONLY and drifts on any reroll — and the fix is often FREE because an accepted portrait already sits unused in `CAST-REF-V2/` (2026-08-11, row 60 gerasene 2:39 healed-man hair).** Cameron: "2:39 doesn't look like the man Jesus just healed; the whole rest of the video shows him with black hair." The `MAN` lock text was correct ("long matted black hair and a wild tangled black beard") but the build had NO `REFS` dict, so every MAN beat rendered text-only; an earlier Jesus-eyes reroll of the after-picture (b28) therefore had nothing anchoring the man's identity and drifted him to light sandy/greying hair (every other frame stayed black). The build already contained an accepted black-haired `CAST-REF-V2/man.jpeg` — it was just never wired (the author's own CAST-REF note said to wire a face ref once accepted; that step was skipped). FIX ($0.27, 2 rerolls): add `REFS = {"MAN": "CAST-REF-V2/man.jpeg"}` and reroll ONLY the drifted beat — image lock now drives identity. HOW TO CATCH: at claim/QC, `grep -c 'REFS' <build>/beats_v2.py`; if a recurring named character has a strong text lock but no REFS entry, check `CAST-REF-V2/` for an accepted portrait and wire it BEFORE any reroll. COMPANION (confirms row-52 lesson 2): reroll 1 here kept a `rough_ref` of the old light-haired frame and the hair bled grey/brown toward the draft; dropping the draft so identity came only from the FACE + character locks landed solid black in one gen — a rough_ref cannot change the very trait you're fixing.

- **A PLACE-PLATE THAT IS A FULLY-PEOPLED ESTABLISHING WIDE FORCES ITS WHOLE COMPOSITION INTO EVERY BEAT THAT SHARES THE LOCK — this is a top cause of "the pictures keep looking the same / people disappear and come back / the crowd faces the wrong way," and no amount of re-rolling the beat TEXT fixes it (2026-08-11, row 66 malchus, 4th RE-OPEN, complete-restart complaint).** Cameron rejected this row FOUR times over the 0-35s arrest ("people keep disappearing and coming back, the army is going the wrong way, disciples look asleep, all looks dumb"); the prior 3 C-FIXes only re-rolled the same beat text and reproduced the mess. ROOT: `PLACE_REFS["GARDEN"]` was promoted from `s01` — the establishing WIDE showing Jesus standing over RECLINING disciples with a torch-line snaking DOWNHILL. That plate is fed to every beat carrying the `GARDEN` lock, so the model reproduced that exact arrangement in the close beats too: b05 (should be a tight alarmed reaction) rendered the reclining disciples again = "asleep"; the downhill torch-line reappeared in every frame = "army going the wrong way"; b01/b05/b15 came out near-identical = "disappear and come back." A tight-reaction instruction in the beat text CANNOT win against a peopled wide plate. HOW TO CATCH IT: when a story reuses one place lock across many beats AND a complaint says shots "look the same / repeat / people vanish," open the promoted plate — if it contains the PRINCIPAL FIGURES in a fixed arrangement (not just the location), that is the culprit. FIX (what worked, one touch-once, 9 gens ~$1.21): re-compose the harmed close beats away from the plate's arrangement with explicit "TIGHT reaction, NOT the wide establishing view, nobody seated/reclining, mob CLOSE" text and fresh-gen them; for a durable fix promote a PEOPLE-LIGHT location plate (the empty-aftermath frame, e.g. this row's b29) so the plate anchors SETTING not BLOCKING. PRINCIPLE: a place-plate should be a LOCATION (trees, terrain, light), never a fully-staged peopled composition — a peopled plate is a composition lock in disguise.
- **A drawn weapon in-frame with Jesus gets aimed AT Jesus unless the beat text explicitly forbids it (2026-08-11, row 66).** Cameron: "1:04 Peter about to swing on Jesus / 0:50 someone about to swing on Jesus." Wherever a beat put a disciple's drawn blade in the same frame as Jesus, the model pointed the tip at Jesus (the visual centre) — reading as an attack on him. FIX: hard `must_not` "the blade points at the MOB or DOWN at the wielder's own side, its tip NEVER toward Jesus or across his body; no weapon points at the cream-robed man," + compose Jesus BEHIND his own men or with Peter's sword dropping tip-down. Applies to any arrest/betrayal/rescue beat where a friend holds a weapon near Jesus.
- **The final AUDIO + CAPTION authority for a V2 cut is the V1 build folder, not the V2 one (2026-08-11, row 66 audio complaint).** `v2_assemble` maps the audio track (`-map 1:a`) from `media-production/<build>/luke-...mp4` and imports the caption text from the V1 folder's `make_narration` SEGMENTS + `audio/*.timing.json`. Editing the V2-folder `audio/*.mp3`, `make_narration.py` or `timing.json` does NOTHING to the render. To fix a narration word/caption without a re-voice: (1) mute/trim the region IN the V1-folder source mp4's audio (keep duration byte-identical so no still-window moves), (2) fix the caption text in the V1-folder `make_narration` SEGMENTS AND `audio/<seg>.timing.json`, AND the beat's own `narration` field if it carries the phrase, (3) delete the stale `segs/<seg>_*.txt` caption cache so it regenerates, (4) reassemble — the audio hash MOVES (breaks autopilot's reopen loop) and the caption matches. Verify BOTH in the rendered mp4 (audio RMS at the timestamp + the extracted caption frame).

- **Head-state / any single-attribute drift the AUTHOR already specified → targeted image EDIT, not reroll (row 120 Job, 2026-08-11).** `beats_v2.py` designed Job "SHAVED from b05 on" (mourning, Job 1:20) but the generator gave him hair on ~half the mourning beats — a flip-flop Cameron complained about. Rerolling reproduces it (the beat text already says shaved). FIX: feed each finished still back to gemini-3-pro-image with a pure edit — "change ONLY <attribute> (shave the scalp), keep beard/face/robe/pose/EVERY other person/background/lighting identical." Preserves group-shot friends + counts + composition; only the one attribute changes. ~$0.134/frame, no recomposition risk. Use this for consistency defects (head shaved/haired, a wrong prop, one figure's clothing) where full regen would gamble the rest of the frame. Keep `*.prehair.bak` backups.

- **A wide "authority-at-the-rail/podium/judgment-seat" beat can render the standing figure as a TRUNCATED BUST behind a narrow parapet — no lower body, arms spread and disconnected, reading as a "talking statue on a pedestal" (2026-08-12, row 93 Barabbas, s07 @36s: Cameron *"36 second picture is weird, replace it"*).** The beat authored "Pilate at the rail, palms out asking what-then"; the model set him behind a too-narrow stone lectern and cropped his body so only the muscled-cuirass torso + floating spread arms showed = uncanny. Every OTHER seat-wide of the same place (s04/s10/s11) drew him as a full standing figure, so it was a lone bad roll, not a place/plate problem — a plain `--redo` of that one beat ($0.13) landed a whole coherent figure at the dais step. DETECT at the full-cut gate: on any "someone speaks from a podium/rail/throne over a crowd" frame, check the SPEAKER reads as a full body (or a clearly-seated full figure), not a head-and-arms bust sprouting from the furniture; if the parapet truncates him into a floating torso, reroll for a full figure. Cheap single-beat reroll, no plate/lock touch.

- **"Doesn't look like Jesus" on a close-up whose eyes read pale/glassy/green → targeted iris EDIT to warm brown, NOT a reroll, and do EVERY Jesus close-up in the cut together (2026-08-11, row 89 Last Supper, s03 @0:14: Cameron *"0:14 doesnt look like Jesus"*).** This refines the row-54 "DON'T reroll Jesus's green/hazel eyes" lesson: a reroll can't fix it because the drift rides the systemic V2 ref, but LEAVING it fails Cameron — the JESUS LOOK STANDARD is WARM BROWN, never pale/blue, and pale glassy-green irises with a bright catch-light read as "not Jesus." FIX = the row-120 edit technique aimed at the eyes: feed each finished close-up back to gemini-3-pro-image, "recolour ONLY the irises to warm medium brown, remove the pale/greenish cast + catch-light, keep every other pixel identical" (~$0.134/frame, `*.preeye.bak` backups). CRUCIAL: edit ALL the tight Jesus close-ups in the cut in the same touch (here s03/s07/s11/s13) — a single brown-eyed frame among green ones is the Law-14 MIX defect. Wider group shots (eyes small/dark) usually don't need it; judge by whether the iris colour actually reads on screen.

- **"They are touching / standing with no distance like they are lovers. She did not touch him. Stop making it weird" — a two-figure INTIMACY/PROXIMITY defect that traces to the BEAT PROSE, not a bad seed (2026-08-11, row 98 "Mary, Her Name", Cameron flagged SEVEN timestamps: 0:25/1:09/1:12/1:26/1:32/1:41/1:48).** On the John 20 garden-recognition beats every Jesus↔Mary two-shot rendered them shoulder-to-shoulder, hands on each other, foreheads near-touching, and at 1:48 his arm literally around her back — reading as lovers, and directly contradicting the "TOUCH ME NOT" verse it illustrates. PROMPT AUTOPSY (rubric meta-law 3): the scene text itself CAUSED it — "closing the distance," "two faces close," "the intimacy of HABIT," "something better than an embrace," "can afford to wait for the embrace," "his arm extended" (→ arm-around). The lock/gen faithfully drew the prose. A blind reroll would reproduce it. FIX = rewrite the blocking of every affected beat AND add an explicit ban to must_not_show: **"ABSOLUTELY NO CONTACT: a full clear pace of open air between them; she keeps her own hands at her own breast; his stay-hand stays in HIS own space and never lands on her; his commission arm sweeps OUTWARD toward the city, never around her; no clasped hands, no embrace, no leaning together, no shoulder-to-shoulder, no near-touching faces, nothing romantic."** Then reroll — the gap lands in one take. DETECT at the full-cut gate on ANY man↔woman (esp. Jesus↔woman) two-shot: ask "is there open ground between them, and are her hands to herself?" — if they touch, overlap, or their faces nearly meet, it's this defect. Sweep every two-shot of the pair in the same touch-once re-cut (here b05/b12/b13/b14/b16/b18/b19); the tender-but-separate reverent distance is the target, and it is also the doctrinally correct read of "touch me not."

- **A caption-word complaint can be a CAPTION-ONLY (picture-domain) fix, not an audio park — transcribe the delivered mp3 FIRST (2026-08-11, row 71 Great Commission, Cameron: *'Jesus said "…I am with you always, even unto the end of the world" not "alway"'*).** The RED jv20 caption read the archaic KJV "alway" (drawn from the V1 `make_narration.py` SEGMENTS), but faster-whisper on `audio/jv20.mp3` showed the shipped ElevenLabs **Chris** voice already SAYS "always" — it had modernized the archaic spelling. So the caption was out of sync with the spoken word; Cameron was reading a caption that didn't match what he hears. FIX = declare `TEXT_OVERRIDES = {"jv20": "…always…"}` in the build's beats_v2.py (the blessed `v2_assemble._text_overrides` path) so the caption matches the DELIVERED audio — NOT a re-voice, and V1 make_narration is NEVER edited (hard rail). Audio stays byte-identical (AUDIO LOCK PASS same SHA). RULE: on any caption-spelling/word complaint, whisper-transcribe the delivered mp3 before deciding domain; if the voice already says Cameron's word, it is a TEXT_OVERRIDES caption fix (picture-domain, ship it), NOT a NEEDS-AUDIO park. Archaic KJV spellings (alway, holpen, sheweth, wist) are prime candidates — ElevenLabs often modernizes them in audio while the caption keeps the old spelling.

- **A white PAINTED TEAR / bright opaque cheek-streak on an emotional-reaction face (2026-08-11, row 71, Cameron: *'1:37 a man has a white tear'*).** b18 asked for Peter's "weathered face taking the word with the particular gratitude…" (an emotional face) but its must_not_show banned no tear → the model rendered a bright, opaque WHITE streak down his cheek (real tears aren't opaque white; it reads as a paint artifact). AUTOPSY = **ALLOWED** (emotional framing invited it, nothing banned it). FIX = add explicit ban to must_not_show ("ABSOLUTELY NO painted or white tear, no bright white streak, drip or opaque droplet on any cheek; emotion carried by the eyes and the set of the mouth alone") + one reroll. DETECT at the full-cut gate on ANY grief/gratitude/weeping-adjacent face: scan the cheeks for a bright white vertical streak.

- **THE GREEN-EYE LOCK BUG (systemic, every v2 row — 2026-08-11, rows 89/98/71 all fixed it the same day).** `v2_prompt.py` JESUS_LOCK_V5 literally specifies "luminous GREEN eyes" (lines ~953/971/992), so EVERY v2 Jesus generates with pale glassy green/amber irises + a bright catch-light on tight close-ups — the "wrong-Jesus" look. This VIOLATES CLAUDE.md law 8(g) ("warm brown eyes… NEVER pale/blue") and Law 5/6 (one locked face across EVERY video); Cameron has rejected it ("doesn't look like Jesus", row 89). Until the lock is corrected at source, the FULL-CUT GATE must brown-edit every tight Jesus close-up whose iris colour READS on screen, using the row-89 `_eye_edit.py` technique (feed the finished still back to gemini-3-pro-image: "recolour ONLY the irises to warm medium brown, remove the pale/greenish cast + catch-light, keep every other pixel identical"; backups `*.preeye.bak`), and do ALL of a cut's close-ups together (a lone brown among green = Law-14 mix). Group/wide shots (eyes small/dark) don't need it. This is a per-row tax on all ~200 v2 rows — **it should be FLAGGED to Cameron to fix JESUS_LOCK_V5 to warm brown at source** so future generations stop producing green.

- **THE "boughs" RESPELL REGRESSES A HOMOGRAPH THAT WAS ALREADY RIGHT (2026-08-11, row 119, Cameron: *'Mispronounced bow at 7 seconds its still mispronounced'* — filed AFTER the 08-11 "fix" claimed it CLOSED).** n1 "everyone bows" (bend-down, /baʊz/=BOUGH) already rendered CORRECT in the original ElevenLabs **Brian** take (formant F1≈700 Hz, open vowel; md5 6da0ad05). An audio lane then "fixed" it by re-voicing the text spelled **"boughs"** + atempo-stretching 1.02× → ElevenLabs Brian read "boughs" as **/oʊ~uː/ (BEAU/"booze")**, F1≈250 Hz rounded onset, mangled into two blobs — WORSE. The 08-11 gate validated by whisper ("bows") and correlation-to-the-intended-take (0.973) — **both are DEAF to the vowel** — so it shipped the wrong sound as "CLOSED". FIX = $0 revert to the original plain-"bows" take (name `.OLD-beau-bak` was a misnomer — it was the BOUGH take), re-assemble; audio SHA returned to the pre-fix dc3ae03e; live mp4 @6.9 s corr flipped 0.919-bad/0.091-good → 0.121-bad/0.877-good. RULES: (1) "bows"=bend-down already renders correct /aʊ/ in Brian — NEVER respell it "boughs" (he reads that /oʊ/). (2) NEVER validate a homograph-VOWEL fix by whisper or correlation-to-intended-take; use FORMANT/spectrogram (open F1≈700=/aʊ/ vs closed F1≈250=/oʊ/). (3) An atempo-stretched re-voice onto a static window distorts the vowel — prefer reverting to a clean natural take over stretching a re-voice.

- **Crucifixion frames — titulus + solemn face + consistent wardrobe (row 94 C-FIX, 2026-08-11).**
  Cameron rejected a cut where (a) Jesus was smiling on the cross at 0:54 and (b) the 0:48 frame
  had a bare cross-top while an earlier frame (0:29) carried the titulus board — a presence-
  inconsistency. On ANY Jesus-on-cross beat where the top of the upright beam is in frame, the
  scene MUST name the titulus placard fixed above his head (describe it weathered/worn, don't
  demand legible text — the model renders gibberish), his expression MUST be solemn/in-pain
  (must_not_show: no smile, no grin, no bared teeth), his eyes lifted-natural (not rolled back /
  whites-only), and his wardrobe (stripped loincloth vs full robe) locked the SAME across every
  cross frame of the row. A close-up that crops the cross-top above frame needs no plaque (it is
  cropped, not inconsistent) — but two cross frames that disagree on plaque-presence WILL draw a
  complaint.

- **Crucifixion Jesus is a PER-BUILD override, not the shared robe lock (row 96, 2026-08-11).**
  The shared `JESUS_LOCK_V5` (cream wool robe, "flame-of-fire" eyes) is the identity lock for
  normal scenes — on the cross it drove a robed, no-crown, no-titulus, pale-eyed Jesus that
  flipped frame-to-frame (Cameron: "redo the whole thing, all the Jesus pictures... clothes on
  again"). NEVER edit the shared lock for one crucifixion row. Instead add per-build
  `CRUCIFIX_LOOK` + `CRUCIFIX_REJECT` strings and inject them via each Jesus beat's `scene` /
  `must_not_show` — they render AFTER the shared lock in `assemble()` and override it for that
  row only. Spec ONE depiction and apply it to EVERY readable Jesus beat: stripped rough
  loincloth (garments gambled — dice), crown of woven thorns, weathered titulus above the head,
  warm living dark eyes (never white/never lens), cross timber behind the head. Verify the
  override lands after the lock with a quick `assemble()` string-index check before spending.
- **Two Nano-Banana crucifixion traps to pre-empt with the reject clause (row 96):** (1) the
  HILL/place "THREE crosses" lock, in a Jesus-foreground shot, spawns a SECOND trio of crosses
  on the background hill = 4+ crosses ("floating/duplicate"). Forbid "a second separate group of
  crosses on a background hill or horizon — only THREE total." (2) a titulus/title-board renders
  garbled legible Latin ("KICEIDE", "TVREI-TOM"). Spec "an aged placard, worn indistinct ancient
  marks, no readable modern word" and expect one reroll; do not chase faint pseudo-lettering past
  the 2-reroll cap — FIX-WAVE it (background object, not a Cameron complaint about text).

- **A "SHIPPED" label in QUEUE/QC/AUTHOR-BOARD is NOT proof the reviewer serves
  that cut — a VERIFY-PASS must curl the LIVE card (2026-08-12, row 121).** The
  2026-08-09 session committed row 121's realistic-v2 mp4 to the warehouse
  (`media-production-v2/…`, blob `551bfcc0`) and wrote "REALISTIC V2 SHIPPED TO
  REVIEWER" in QUEUE + QC, but never executed step 7b/7c — the `v121` card still
  pointed at the OLD 2026-07-28 V1 cut (`data-hash=cb1b23f6…`, `media-production/`
  path, no `data-review-wave="realistic-v2"`), and the site was never redeployed.
  So Cameron's Unwatched queue served the OLD cartoon/mixed cut under a "shipped"
  label — exactly the row-17 served-bytes trap, but caused by a SKIPPED card
  repoint rather than a broken `git add`. On ANY QC-VERIFY: `curl` the live card
  and confirm data-hash + `realistic-v2` wave + vslot PATH all point at the
  `media-production-v2` mp4, then md5-compare the served bytes to local. If the
  card serves the OLD cut, the pictures can be perfectly clean and the row is
  still NOT delivered — complete the ship ($0, byte-identical, no re-cut): repoint
  the card, deploy, live-verify.

- **A "shave the scalp, keep the beard" head-edit can silently strip the BEARD too
  (2026-08-12, row 120 s18).** Cameron: "1:39 his beard is shaved." The word
  "shaved-headed" in a beat's scene — OR a targeted bald-scalp edit — biases the
  generator to shave the FACE as well, leaving only stubble even though the person
  lock says "full beard." So: (1) after ANY scalp/bald edit, run the lesson-13
  BEARD BOARD on that exact frame; (2) restore a lost beard with a targeted
  identity-edit that adds the beard and attaches a good neighbour frame as the
  beard anchor (s19 anchored s18 here), never a blind reroll (the scene already
  says shaved, so a reroll reproduces the stubble). Cheap: one edit, $0.134.
- **A shave/beard/identity SWEEP must include EVERY frame the person appears in —
  even a "cosmic/wide/vision" beat where they sit small at the frame foot
  (2026-08-12, row 120 s27).** Cameron: "2:36 he is not head hair shaved." The
  2026-08-11 shaved-head C-FIX misfiled s27 (a Pleiades/Orion night-vision with
  Job tiny at the bottom) as "person-free cosmic — untouched" and skipped it, so
  Job kept his hair there while every other mourning frame was bald. Before a
  sweep, list beats by WHO-APPEARS from the rendered frames, not by beat name/role;
  a person in the lower third of a landscape beat still counts. Belt-and-braces:
  state the changing-condition (shaved-headed) in that beat's `scene` too, so a
  future regen can't reallow it (the b27 scene relied on the lock and got hair).
- **Vowel-pronunciation audio complaints: respell the SPOKEN token only, render
  N takes, FORMANT-validate, atempo-lock (2026-08-12, row 120 jvA "wast"→"waste").**
  ElevenLabs read KJV "wast" as /weɪst/ ("waste"; F1=412 F2=2395, a front vowel).
  Whisper is deaf to this (it prints "was" either way) — validate the vowel by LPC
  formants: the target back vowel /wʌst/ needs F2 well below ~1600, not ~2400. Fix
  without touching the caption: feed ElevenLabs the literal respelling `wust`
  (caption stays KJV "wast" — the two are decoupled), render several takes, keep
  only the ones whose target-word formant is a back vowel, pick the take whose
  duration is CLOSEST to the original segment length, then `atempo`-lock to the
  exact original duration (drift <1 frame) so no caption window moves and the
  AUDIO_FROM_V1_SEGMENTS rebuild timeline is unchanged. Confirm the re-voiced
  segment's median F0 still matches the other same-speaker segments (voice
  identity) and that the DELIVERED mp4's audio carries the fix at that timestamp.
  Back up the old segment mp3 + timing.json + words.json to `audio-oldvoice-backup/`.

- **A "stubby/short mast" word in a vessel lock invites a DROPPED mast in wide shots — and a promoted plate whose token doesn't match the beats' lock token attaches to NOTHING (row 51, 2026-08-12, boat complaint's 3rd re-open).** Two independent traps caused the same "boats are small paddle-only dinghies with no upright sail mast" complaint to survive two prior fixes: (1) the BOATS lock read "a single **stubby** mast" — the model reads "stubby" as "optional/short" and drops it entirely in any wide/establishing frame → mastless open boats. Fix: write the trait as it must READ — "a single TALL UPRIGHT mast … rising well above the men's heads, sail furled to the yard," and put the negative ("NEVER a mastless open hull, NEVER a small paddle-only rowboat/dinghy") INSIDE the lock so it binds every beat, not just the ones whose must_show happens to mention it. (2) A prior fix "promoted s02 as the BOAT plate" but `PLACE_REFS` stayed `{}` and the wiring token was `BOAT` while every beat locks on `BOATS` — so `place_plates_for` attached the plate to zero beats and consistency rode entirely on prose. ALWAYS verify after `v2_stash.py --promote`: `grep PLACE_REFS beats_v2.py` shows the token, and that token must appear in the offending beats' `locks`. If a background element (e.g. boats behind net-washers in b03) needs the plate/lock, ADD the lock token to that beat's `locks` — a beat that omits the token gets neither the lock text nor the plate. The check gate FAILs a stale `PLACE_REFS` token whose plate file is missing — remove dead wiring entries.

- **A `jesus:False` beat that still contains Jesus's OWN body (his anointed feet, his back, his robe hem) invites a SECOND Jesus among the unlocked guests — and a prior reroll that only forbade a second CREAM robe does NOT stop a second Jesus-FACE (row 74, 2026-08-12, "1:38 jesus is in 2 places", the SECOND time this frame was rerolled).** s21 was `jesus:False`: Jesus's feet were being anointed at the couch's foot, but with no Jesus REF/lock and no wardrobe/face lock on the table guests, the model painted an unlocked guest with Jesus's dark-wavy-hair-plus-full-beard face → the true Jesus (feet/back) + a front-facing Jesus-double = "two Jesus." The 08-11 fix added only a no-cream clause, so the double came back as a tan-robed but Jesus-FACED guest. Durable fix: when Jesus's body is in a frame at all, attach the Jesus REF + set `jesus:True` so exactly ONE canonical Jesus exists (and the frame comes under `jesus_face_gate`), AND write the negative against the FACE not just the robe — "EXACTLY ONE man is Jesus … every other guest is a DIFFERENT man (older/greying, trimmed or no beard, earth-tone), NONE with Jesus's long dark wavy hair and full beard, NONE in cream." No-cream ≠ no-Jesus.
- **A parable/vignette beat that OMITS a figure the scene needs (the moneylender, a servant, a bystander) lets the model invent that figure and default him to the JESUS ARCHETYPE — long dark wavy hair, full beard, cream/tan robe (row 74, 2026-08-12, "1:36 old picture / make realistic": the two-debtors s19/s20 lender rendered as a Jesus-lookalike, and painterly/flat).** If the scene needs a person, NAME him explicitly with a non-Jesus description ("an ORDINARY older greying Judean merchant in a plain BROWN wool tunic, close-trimmed beard") — an unnamed figure is a Jesus-double waiting to happen. Pair it with a realism anchor in `must_not_show` ("a REALISTIC PHOTOGRAPH with natural skin texture and true lamplight — never a smooth digital painting/illustration/cartoon/CGI"), because the same beats that drift to the Jesus archetype also drift to a flat illustration look.
- **A `jesus:False` FACELESS close-up of a woman's/other's hands that plays UNDER Jesus's spoken line reads as a BAD JESUS unless the hands are explicitly feminine AND guarded against being Jesus (row 82, 2026-08-12, "1:35 picture does not look like Jesus").** b17 was a close-up of the WOMAN'S hands on the broken flask while the narrator paraphrases Jesus ("she has come… to prepare my body for burial"). The prompt locked her *garment* olive-green and forbade cream-on-anyone-but-Jesus, but described the hands only as gender-neutral "composed, unhurried hands" — so the model rendered large weathered masculine-reading hands in a muted sleeve, and with no face + Jesus's voice over it, viewers read it as a stand-in Jesus that "doesn't look like Jesus." Durable fix for any faceless close-up of a NON-Jesus person's hands: describe the hands so they READ as that person (for a woman: "clearly a woman's hands, slender, ~30, softer/smaller, her DEEP OLIVE-GREEN sleeves visible at the wrists"), and add an explicit guard in must_not_show ("THESE ARE THE WOMAN'S HANDS, NOT JESUS'S — no cream/off-white sleeve in the crop, no man's hands, nothing may read as Jesus"). Attaching that person's char-ref (locks: WOMAN) reinforces it. Locking only the robe COLOUR does not stop a masculine faceless read.
- **⛔ SUPERSEDES the brown-iris lessons above (the "recolour Jesus's irises to warm brown" lines ~1164/1172): DO NOT brown-edit Jesus's eyes — it is a WRONG edit AWAY from the ref (CLAUDE.md rubric lesson 20, 2026-08-12, which reversed the brown-edits on rows 71/89/98/120).** The V2 Jesus reference image (`JESUS-V2-REF/jesus-v2-face.jpeg`, LOCK v5) HAS green/amber/gold eyes on purpose — the ref image IS his face and outranks any sentence. Row 89's 0:14 complaint "doesn't look like Jesus" RE-OPENED precisely because the 2026-08-11 session read it as "eyes too pale/green" and iris-recoloured them to brown; Cameron then rejected the brown cut too. If a Jesus close-up's eyes look wrong, the fix is to make them match the REF (green-gold, luminous, not a flat pale STARE — a downcast/three-quarter gaze reads warmer), NOT to paint them brown.
- **A "doesn't look like Jesus" complaint that SURVIVED a prior iris/eye edit is FACE-IDENTITY drift, not eye colour — regen the frame FRESH against JESUS-V2-REF, do not edit the eyes again (row 89 RE-OPEN #2, 2026-08-12, 0:14/s03).** When Cameron has rejected TWO different eye-states of the same frame (check REVIEW-LESSONS history hashes), the eyes were never the problem — the whole face had drifted to a rounder/heavier/generic man off the ref. b03 carried no `rough_ref`, so a plain `--only <beat> --redo` re-draws purely from the ref + place plate; the new draw matched the ref (long wavy bronze-highlighted hair, lean Semitic face, green-gold eyes). Watch the ROOM/place plate: on a close-up beat the first redo came back a WIDE establishing shot (plate dominated, failed the close-up must_show) — 1 reroll fixed it. To make a drifted close-up consistent with the rest of the cut, REVERT any other close-ups that were wrongly brown-edited back to their `*.preeye.bak` green originals (free) rather than re-editing them.
- **PROMPT AUTOPSY catches eye-colour drift at the source: scan the beat's SCENE TEXT for colour words on Jesus's eyes (row 89 b03 literally said "the warm brown eyes").** Any positive eye-colour phrase in `scene`/`must_show` that isn't the lock-v5 "luminous green-and-gold" is a sentence outranking the ref (lesson 20 forbids it) and will drag the gen off-ref no matter that the REF is attached. For a C-FIX this is a CAUSED verdict — rewrite the words to match lock v5, then regen. (Author lane: never write a Jesus eye-colour into scene text; let the ref carry it.)
- **A crucifixion-block row (the passion rows 94/95/96) MUST show a CROWN OF THORNS on every readable Jesus-on-cross frame — a bare-headed crucified Jesus reads as "wrong / you didn't fix anything," even when smile/eyes/plaque were fixed (row 94 RE-OPEN, 2026-08-12).** Cameron: *"he needs a crown of thorns when he is on the cross so all of these pictures need to be redone … You didnt fix anything."* The 08-11 row-94 fix touched only b09/b10 smile/eyes/plaque and left every cross frame bare-headed, so to him nothing was fixed. Matt 27:29 / John 19:2-5 — he wore the crown ON the cross. FIX = port row 96's proven `CRUCIFIX_LOOK`/`CRUCIFIX_REJECT` (crown of woven thorns + loincloth + weathered titulus + open reverent eyes + no smile + cross-behind-head + ONLY-3-crosses) and apply it via a `_CRUCIFY_IDS` loop to every READABLE Jesus frame; leave distant wides (Jesus a speck, crown imperceptible) untouched (cost law). When you touch ANY passion row, verify the crown is present on the close/mid Jesus frames BEFORE shipping — its absence is a guaranteed re-open.
- **"a random cross falling towards them" on a dice-game insert = the model rendered the cross timber as tilted/X-crossed overhead beams; the scene named "in the shadow of the beam" with no orientation constraint (CAUSED/ALLOWED, row 94 b07).** FIX = must_not_show forbids any cross/beam leaning/tilting/falling toward the men and any X-crossing overhead beams; scene names ONE plain vertical upright at the back edge. Also anchor the insert to the row's light+ground (cold grey overcast, bare rock, no village) or it drifts to a sunny courtyard and breaks continuity.
- **A recurring NON-Jesus character with a face-sheet on disk but NO `REFS` dict in beats_v2.py renders TEXT-ONLY and drifts to a different person every frame — check `cast_refs_for` actually attaches it (row 63 RE-OPEN, 2026-08-12, the born-blind man @ 0:12/1:29/3:16/3:29/3:35/3:49/3:55).** Cameron: *"the blind mans face is not the correct look … wrong lookijg blind person."* The build had `CAST-REF-V2/blindman.jpeg` (a good dignified anchor) but the beats only listed the `BLINDMAN` lock TOKEN and there was no `REFS = {"BLINDMAN": "CAST-REF-V2/blindman.jpeg"}`, so `cast_refs_for()` (which reads `getattr(mod,"REFS",{})` first, then GLOBAL_CAST) attached NOTHING — the man rendered from text only and his hair swung black→brown→grey, his age/beard changed shot to shot. A token in `locks=[...]` is NOT proof the face is attached; it only matters if the token is in GLOBAL_CAST (with a `<stem>-front/quarter.jpeg` sheet on disk) OR in the build's own `REFS`. FIX = add the `REFS` entry, then regen the drifted frames. Author law: whenever you drop a `CAST-REF-V2/<name>.jpeg` for a one-off story character, WIRE it in `REFS` in the same commit, or it is dead weight.
- **A per-beat CHANGING CONDITION (clay over the eyes, a bound wrist, a wound) stated once in prose gets silently dropped by the generator — force it in BOTH must_show AND must_not_show, describing the visible mask, not the abstract state (row 63 b19, 2026-08-12, "1:41 the blind mans eyes were supposed to be pack with clay … and they are not").** The scene said "the clay-eyed man" twice and the man still walked with clean open eyes. FIX = must_show "BOTH EYES COMPLETELY PACKED AND SEALED SHUT UNDER A THICK MASK OF WET GREY-BROWN CLAY (no eyeball, no iris, no open eye visible)" + must_not_show "his eyes are NOT open, NOT clear, NOT visible." Describe the covering as a physical mask; the generator honours a concrete object it must paint far more than an adjective ("clay-eyed").
- **A negative/covering constraint that names a subject the beat does NOT lock will bind to whatever locked figure IS present (row 113 b20, 2026-08-12, Cameron: "1:51 God does not also need to be wearing the leaves").** b20's `must_not_show` said *"the couple still wear their GREEN FIG-LEAF girdles here"* but the beat's `locks` were only `GARDEN`+`GOD` (no `ADAM`/`EVE`) — so the fig-leaf-girdle language had no couple to attach to and the generator dressed the ONLY embodied figure, the Father, in a leaf girdle over his white robe. FIX = lock the covering's OWNER (add `ADAM`+`EVE` to the beat), bind the covering to them explicitly ("ONLY the man and the woman, never the Father, wear the girdles"), and ban the covering on the other locked figure ("the Father wears ONLY brilliant white — NO leaves/foliage/girdle ever"). Rule: never leave a "the couple/he/she wears X" clothing line in a beat that does not lock that person — the words land on the nearest locked body. ALSO (same touch): when re-cutting a "God makes them coats" beat, ban modern tailoring (jacket/blazer/trench/collar/lapel/zipper/buttons) or Gemini renders a modern leather jacket — specify "primitive hand-stitched hide tunic matching the approved worn coats."
- **A CORRECTLY-WIRED recurring-character ref can STILL drift in a single beat — the FULL-CUT GATE must crop-compare that character's face across ALL its beats, not spot-check (row 122 b17, 2026-08-12, independent QC-VERIFY caught it before Cameron).** Unlike the row-63 wiring bug, build-122's FIXER ref was attached (gen banner "[+2 char ref: FIXER, BROTHER]") and rendered as the correct lean salt-and-pepper man in 10 of its 11 workshop beats — yet b17 alone drifted to a different actor (younger, darker-skinned, full black beard). A per-beat generation miss is invisible to any single-frame or portrait check; you only see it by lining the recurring face up across every beat it appears in. FIX = crop the face from the outlier + a canonical beat + the portrait, confirm the mismatch, `--redo` the one beat (cheap: 1-2 rerolls @ ~$0.13). Take the reroll that ALSO satisfies the beat's scene text (b17 take-2 restored identity AND put the beam front-and-centre per "the brother regards the beam's full length") over one that only fixes the face.

- **Deleting the `segs/*_N.txt` caption cache does NOT fix a caption↔audio mismatch when the orphaned sentence lives in the V1-dir make_narration SEGMENTS — it regenerates the SAME stale text; use TEXT_OVERRIDES (2026-08-12, row 108 n4b).** V1 make_narration n4b had a 3rd sentence ("Not a hired man who runs off…") the re-voiced audio (timing.json) no longer speaks, so the burned caption @69s printed it while the voice said "That is what he was willing to spend to keep them." `rm segs/n4b_*.txt` + re-assemble reproduced it byte-for-byte (extract_beats re-reads the stale V1 SEGMENTS, not the cache). FIX = `TEXT_OVERRIDES={"n4b": "<timing.json spoken text>"}` in beats_v2.py (blessed `_text_overrides` path); audio SHA unchanged. This is the row-84/131 class; the extra lesson is that the cache-delete step (row-66 lesson 1201) alone is a no-op when the source itself carries the orphaned words — go straight to TEXT_OVERRIDES. VALIDATE any homograph/vowel audio complaint (calleth) by LPC FORMANT of the delivered mp4, never whisper: back /ɔ/ "KAWL" reads F2≈1272, the wrong /æ/ "KAL" reads F2>1600.

- **A PEOPLED wide (crowd/establishing) promoted as a PLACE PLATE forces its crowd composition onto a same-place beat that needs a SINGLE figure — a plain `--redo` re-attaches the plate and reproduces the crowd; reroll that ONE beat with `--no-plates` so its own text drives the composition (row 127 strait-gate b10, 2026-08-12).** The GATES plate was promoted from b03 (a wide-gate frame thronged with cheerful travellers — the author's named promote-first). It carried the valuable both-gates fork geometry and helped the narrow-gate/stooping/three-walkers beats fine, BUT the CLOSING beat b10 ("both gates open, one traveller caught MID-STEP toward the NARROW gate; choice as motion") cloned the plate's wide-gate crowd twice — a near-duplicate of b03 AND the wrong emphasis on the last frame Cameron sees. This is lesson-1199 (malchus peopled-plate) but with an ANONYMOUS crowd, so it slipped promotion QC. FIX that worked in ONE take: `python3 v2_gen_api.py <build> --only b10 --redo --no-plates` — without the plate, b10's strong single-figure beat text landed the intended lone traveller stepping toward the narrow gate. Slight architecture variance from the plate is acceptable and far better than a crowd-dup that misses the closing message. RULE: when promoting a place plate, prefer a PEOPLE-LIGHT/location frame; if the author's promote-first frame is peopled, use it for the establishing/crowd beats but `--no-plates`-reroll any same-place beat whose text calls for a SINGLE figure or a specific different composition. (Companion: the PLACE_LOCK_TEXT already says "people in a place photograph are NOT part of this scene" — but a peopled plate still bleeds the crowd in practice, so don't rely on that clause for a single-figure beat.)

- **A Jesus beat that attaches the ref + says "the locked face" but gives NO EXPRESSION or FOOT-PLACEMENT direction can render a SMUG SMIRK and FEET-UP-ON-THE-TABLE — a smirking Jesus stops reading as Jesus even with the correct ref, and reclining-meal beats need his feet placed (row 74 b21, 2026-08-12; Cameron: "1:40 … doesnt look like jesus and he is propping his feet up and smirkijg lookijg more evil than Jesus would").** The 08-12 fix had rerolled b21 to `jesus:True` to kill a Jesus-double; that reroll was single-cream and identity-locked, but the scene only said "his face the locked face" with zero emotional or postural constraint, so the model painted a lopsided up-glance grin and stretched his bare feet onto the table edge — over a weeping woman it reads as amused/smug (Cameron heard "evil"), and the smirk itself broke the "looks like Jesus" read. AUTOPSY VERDICT = ALLOWED (the ref was correct; the ref did NOT need swapping — the words did). FIX in ONE take: must_show += "Jesus's face tender, grave and compassionate, his gaze lowered toward the [subject]"; must_not_show += "Jesus NEVER smirks, grins, smiles smugly, or looks amused/mocking/sly/smug/self-satisfied … his feet are NEVER propped, raised, or resting up on the table; feet stay LOW on the floor toward [the subject]". RULE: for ANY Jesus beat where the emotional read matters (someone suffering/weeping/repenting at his feet), DIRECT his expression explicitly (tender/grave/compassionate, gaze toward the person) — "the locked face" governs identity, not mood, and a wrong mood fails the "looks like Jesus" test the same as a wrong face. For any reclining/foot-washing beat, also state where his feet are (down toward the person, away from the table), or they drift up onto the furniture.

- **A "doesn't look like Jesus" that survives BOTH eye-edits AND a "fresh regen from scratch" can be a PALE/EUROPEAN "white-Jesus" drift — the regen went the WRONG way off the ref (row 89 RE-OPEN #3, 2026-08-12, 0:14/s03; reportedAgainst the SAME hash the #2 fix shipped).** The 08-11 fix browned the irises; the 08-12 #2 fix threw the frame out and regenerated it — but the new draw came back fair-skinned, medium-brown-haired and softer-featured, a classic Western "white Jesus," even though the REF (`JESUS-V2-REF`, olive-brown Middle-Eastern) was attached and LOCK v5 says "never fair, never pale, never European." Autopsy = IGNORED + reroll-away-from-ref (lesson 20): the beat's scene text reinforced only the EYES, so the model had no in-scene skin/hair anchor to hold the ref against the stereotype pull, and a stochastic redraw drifted pale. TWO fixes, together: (1) HARDEN the beat — state the identity positively in `must_show`/`scene` ("HIS FACE THE ATTACHED REFERENCE FACE EXACTLY: warm olive-brown sun-darkened Middle-Eastern skin, lean weathered face, aquiline nose, long dark wavy hair, full dark beard") and ban the drift in `must_not_show` ("NEVER pale/fair/Caucasian/European; NEVER a rounder, softer, lighter-skinned man than the reference") — the ref image alone is NOT enough on a close-up that keeps drifting; the words must back it. (2) Before spending a credit, check the build for a `*.preeye.bak`/prior-gen of that frame — the ORIGINAL generation (before the eye-editing chain) is often a good olive-brown ME match that was progressively broken by iris edits; restoring it is $0 and, if it matches the cut's OTHER already-passing dark-ME closeups (here b04/b07/b11), it makes the frame both ref-accurate AND internally consistent. This let row 89 SHIP with the complaint closed even though Gemini billing was DEPLETED (429) and no live regen was possible — do NOT park a complaint when a proven-good asset restore is available. Verdict rule: when Cameron has rejected THREE states of one frame, the FACE (skin/hair/structure), not the eyes, is the defect — never touch the eyes again.

- **"doesn't look like Jesus" on a WIDE multi-figure beat whose NARRATION is actually about the OTHER figures can be fixed at $0 by an OFF-CENTER CROP of the existing frame that excludes Jesus's face — do NOT billing-park it (row 82 s18/b18, 2026-08-12; Cameron "1:36 does not look like Jesus", 6th consecutive Gemini-prepay-depleted session).** The live s18 was the whole supper table with a forward-facing OFF-MODEL cream man at the head under the line "Nobody else in that house would even let him say the word" — a line that is about the FRIENDS refusing the truth, not about Jesus. Prior sessions rewrote b18 to friends-only + a no-frontal-Jesus guard (correct autopsy = ALLOWED) but then parked FIVE times waiting on billing to regenerate the still, AND explicitly dismissed "crop" — because they only pictured a CENTER crop, which keeps Jesus dead-center. The fix: an **off-center crop toward the side where the reacting figures already are** (here a RIGHT crop, box on the 1536×2752 source → 9:16, LANCZOS back to 1536×2752) cleanly excludes Jesus's face and lands exactly the authored "friends flinching, a turned faceless cream shoulder at most" composition, at $0, with the audio byte-identical. RULE: when the complaint is an off-model Jesus in a WIDE and the beat's own narration/authored-fix wants the emphasis OFF him, VIEW an off-center crop that drops his face before you conclude "no $0 path exists." A crop of an existing realistic frame is same-style, no repaint, no billing — it is a legitimate asset the runner may write. Only park for billing if the beat genuinely REQUIRES Jesus's face on-model in that frame (then a paid regen is unavoidable). Companion to the row-89 lesson: never park a complaint when a proven-good $0 asset (restore OR crop) satisfies the authored fix.
- ADJACENT-BEAT REUSE = a $0 identity/composition C-FIX (row 63, 2026-08-12, 17th pass): when a complained frame's defect is an off-model FACE or a bad two-figure composition (e.g. a "kiss"-close reveal) and Gemini is billing-walled, DON'T declare "no $0 path." Check the NEIGHBOR beats: if an adjacent beat already holds a correct still of the same subject, `cp neighbor.jpeg → bad.jpeg` — because the beats are adjacent it renders as ONE CONTINUOUS HOLD, not a visible duplicate. Only the truly off-model stills need swapping; verify side-by-side which flagged frames were ALREADY correct (row 63: s41/s42 were fine; only s40 kiss+grey & s43 grey-elder were defects). Cameron's complaint is about the FACE/kiss, not preserving the exact composition. 16 passes missed this and parked on billing.
- **RE-CROP A CORRECT IN-CUT STILL to fix a NON-ADJACENT defect frame at $0 — the row-63 reuse extended past adjacency (row 94, 2026-08-12; Cameron "0:46 his eyes are Lake white and looks evil … 0:22 he has brown eyes and short hair and looks way different").** Two Jesus close-ups were off-model (0:22/s02 amber eyes + hair hidden = "different man"; 0:46/s09 eyes rolled fully to the WHITES), Gemini billing-walled (429 prepay-depleted). The correct green-eyed locked face existed in the SAME cut at s08 (0:42). Fix, both $0: (1) the ADJACENT defect (s09, next beat after s08, 0.6s gap) → `cp s08 → s09` = a continuous hold across the red-letter "Father, forgive them" (row-63 method, clean). (2) the NON-ADJACENT defect (s02, 17s / 3 shots before s08) → do NOT cp s08 whole (that IS the row-63 "visible dup after a gap" trap). Instead make s02 a **tighter punch-in CROP of s08** (PIL crop box on the 1536×2752 source, resize back with LANCZOS) — the correct face, but a DISTINCT framing (tight face vs s08's chest-up) so it reads as a cut-in, not a duplicate. A ~1.25× crop stays sharp; keep the crown near the top edge to remove s08's cross-beam headroom so the two framings clearly differ. RULE: when the complaint is an off-model FACE and a correct face exists elsewhere in the cut, reuse it — adjacent → straight cp (continuous hold); non-adjacent → a differently-CROPPED punch-in of the same still. Row-63's law holds: "don't park on billing when the complaint is FACE not the exact composition." Also autopsy-first: s02 was CAUSED by the beat literally writing "warm brown eyes" (overrode the green/hazel V2 ref — lesson 20); s09 was CAUSED by "eyes turned upward to heaven" over-rotating into the sclera despite the anti-white constraint — both prompts fixed in beats_v2 (staged for any future paid bespoke regen) even though the shipped fix was the $0 reuse.
- **CROP THE ADJACENT-BEAT still to fix a whole-FACE identity drift when the frame's OWN prompt keeps drifting and billing is walled — check the neighbor beat that shares the SAME room/scene before parking (row 89 RE-OPEN #5, 2026-08-12; Cameron "0:14 doesnt look like Jesus … sane problem 4 times in a row").** 0:14/b03/s03 was a DIFFERENT, heavier, near-black-haired man than JESUS-V2-REF (whole-face drift, not eyes — cont.91's #4 diagnosis). Prose was already word-fixed to defer to the ref, but Gemini was 429 prepay-depleted so no paid regen. cont.91 (#4) PARKED because the ONLY reuse it considered — s07 — is a stone-wall / broken-bread close-up (wrong room + wrong action for the "before I suffer" line). It MISSED that the IMMEDIATELY ADJACENT beat b04 ("I have wanted this meal…") holds the ref-CORRECT Jesus IN THE SAME WINDOW ROOM with the bread NOT yet broken. Fix at $0: a tight punch-in CROP of s04 (PIL crop → 9:16 → LANCZOS to 1536×2752, ~1.5× upscale, sharp) installed as s03 — the correct face, a DISTINCT close framing (so it's not a visible dup of the wider b04), no continuity break (same room/night/meal-state). FULL-CUT GATE 16/16 clean, audio byte-identical. RULE: when a close-up's face keeps drifting and billing is walled, don't only check the obvious hero close-up (b07 here) for reuse — check the ADJACENT beats that share the room/scene/action; a wider adjacent frame with the correct face can be CROPPED into the needed close-up. Extends the row-63/94 reuse law: adjacent→cp (continuous hold), non-adjacent→crop-of-in-cut-still, and now adjacent-but-wrong-framing→CROP-of-the-adjacent-still.

- **A repentance / mourning crowd whose scene prose leans on "ash," "sackcloth," "haircloth" renders the WHOLE crowd corpse-grey and reads as DEAD, not grieving (2026-08-13, row 118 b33, Cameron: "The people in 3:08 look dead").** Gemini applies the monochrome ash/haircloth tone to the SKIN of every figure, so hundreds of bowed people come out uniform grey-terracotta — the terracotta-army look. The whole frame is that tone, so there is NO $0 crop path (the corpse tone fills it edge to edge) and a global warm grade cannot revive statue-toned figures — it genuinely needs a paid regen. FIX in the beat prose: require LIVING warm skin explicitly (must_show "LIVING people with warm natural skin, faces flushed and tear-streaked, chests breathing, hands raised"), forbid the failure (must_not_show "grey, ashen, or corpse-like skin; statue-like; a field of motionless identical bowed figures"), and confine the ash to CLOTH AND BROW ONLY ("a little grey ash smudged on foreheads and dusted on the cloth only; it never greys or deadens the skin"). Verify off the RENDERED mp4, not just the asset. Same root family as the leprosy skin-bleed (row 54): a texture/colour word in the scene migrates onto skin the author never meant it to touch.
- **Figure-scale fail in a wide crowd shot is WITHIN-FRAME relative scale — a crop cannot fix it (2026-08-13, row 118 b28, Cameron: "2:37 jonah was 3 times bigger than the people he was walking around").** When the named subject is drawn hero-scale against same-depth townsfolk, a paid regen is required; the crop can't shrink one figure against its neighbours. FIX in the prose: pull the CAMERA high and back so the subject is a SMALL mid-distance figure, state he is "no larger than any townsperson near him... same body scale, same head size," and add "the townsfolk nearest the camera are drawn LARGER than he is" + "no single figure looms out of proportion to those beside him." Verify off the rendered mp4 at the exact complaint timestamp.

- **A titulus / plaque / sign close enough to read renders as LEGIBLE AI-gibberish that can spell a real, out-of-place word (2026-08-13, row 95 b10/s10: the thief's titulus close-up read "…Nut allah dij is pone" — the word "allah" on a crucifixion title-board).** On crucifixion rows (INRI titulus above each head) or any beat with a foreground sign, Gemini fills the board with pseudo-Latin/Hebrew letters; on a tight close-up those letters are legible and occasionally land on a jarring real word that throws the viewer out of the scene. It is a genuine complaint-class defect, not subtle drift — FULL-CUT-GATE every readable sign for stray real words. Cheapest fix: ONE reroll of just that beat usually returns different (neutral) gibberish; keep the take whose board is illegible/neutral. Prefer authoring distant/blurred plaques or an explicit "INRI" so the text is controlled rather than random. Belongs to the same family as legible-caption/legible-text checks: anything a viewer can actually READ in-frame must be QC'd for meaning, not just presence.

- **A seated crowd figure told to "glance sideways at a neighbour" renders with a BACK-TO-CAMERA torso and the FACE wrenched a full ~180° back to the lens — the "head on backwards" owl-neck (2026-08-13, row 122 b06/s06/0:33, Cameron: "The man's head is turned around backwards 0:33. same problem for the 5th time" — his 5th filing of this class).** The scene wanted a sideways glance and the anti-glitch line only bounded COUNT ("two arms, two hands and one head") — nothing forbade an impossible neck rotation, so the generator, needing to show a FACE glancing on a figure seated with his back to us, screwed the head around backwards. This is why it recurs: "one head" is not "the head faces the way the shoulders do." FIX the prose in any beat that stages a glance/over-shoulder look: must_show puts the glancer in three-quarter view with head AND shoulders turned the SAME way (a natural glance under ~45°); must_not_show forbids "any head rotated impossibly on the neck; owl-neck; a seated figure with back or shoulders to the camera while the face is wrenched a full half-turn back to the lens"; and extend the anti-glitch tail to "every head sits forward on the neck facing the same way as its own shoulders — no one twisted so their face looks back over a body that faces away." GATE: on every crowd/two-shot with a back-to-camera figure, confirm you see the BACK of that head, not a face impossibly turned around. A figure legitimately facing away (b01/b02 of this same row) shows the back of the head — that is correct and must NOT be "corrected."

- **A locked recurring character NAMED only in a beat's `must_show` prose but MISSING from that beat's `locks` list renders a FREE-INVENTED, non-canonical version — the char ref attaches by `locks` TOKEN, never by prose (2026-08-13, row 140 build-140-bronze-serpent, b17 the hero "lifted on a pole"/promoted SERPENT-POLE plate).** b17's must_show said "Moses steadying its base" but its `locks` were only `["SERPENT-POLE","WILDERNESS-CAMP"]` — no `MOSES` token — so `moses.jpeg` never attached (the gen banner showed `[+1 place: WILDERNESS-CAMP]` with NO `[+1 char ref: MOSES]`) and the generator painted a younger brown-bearded Moses while every ref-locked Moses beat (b03/b11/b13/b15) rendered the canonical old white-bearded man. This is a lesson-2/lesson-13 identity break on the single most important frame — a hard FULL-CUT-GATE block, not subtle drift. DETECT AT QC: for every beat, cross-check the NAMED people in must_show against the `locks` list — any locked-cast name in prose that is absent from `locks` will drift. The runner CANNOT fix it (editing `locks` is a hard rail and a blind `--redo` won't attach the ref, so it can't restore the SAME face — lesson 10): PARK **NEEDS-REBUILD** for the author to add the missing token, then a $0.13 `--only <beat> --redo` lands the correct face (and, if the beat also locks the place plate, the pole/place stays byte-consistent so downstream beats need no regen). AUTHORS: every character a beat's prose names MUST be in that beat's `locks`, not just in the text.

- **A WIDE place-plate attached to a TIGHT close/ground-level beat is itself a DIPTYCH trigger — the plate becomes a pasted top band (2026-08-13, row 121 salt-and-light b05 C-FIX, Cameron "0:31 has a double picture").** b05 was a tight feet-and-scattered-salt ground shot that carried the `LANE` place-lock — a WIDE dusk-street image. Gemini reconciled the wide-street reference against the described low close-up by STACKING them: the whole street plate as a top band, the feet/salt scene below, hard horizontal seam. This is the place-lock cousin of the prose-driven diptych (lesson 1028): the trigger is the reference/scene SCALE mismatch, not "then/two-measures" wording. FIX that worked in one `--redo` ($0.13): keep the lock but add to must_not_show an explicit ban on split-screen/stacked/two-panel/diptych/horizontal-seam AND rewrite the scene to "one unbroken ground-level frame with the [place] receding softly out-of-focus in the background of that SAME frame." When a beat's shot is tight/close but its `locks` name a WIDE establishing plate, expect the stack and pre-empt it with the anti-diptych line.
- **"A big Jesus floating in the sky" on an over-the-shoulder DISPERSAL wide = the from-behind direction IGNORED + no scale/grounding bound (2026-08-13, row 121 b29 C-FIX, Cameron "2:45 is corny").** The scene said "camera behind Jesus's shoulder at the crest / backs to the height," intending Jesus naturally large in the foreground with a tiny distant crowd. Gemini rendered his 3/4 FRONT face as a huge bust with no feet/ground contact — a floating giant (scale-gate / lesson-14 family, but the tell is the missing ground contact, not just size). FIX in one `--redo`: rewrite the scene to a TRUE from-behind grounded shot (back/side of head + cream robe, sandaled feet on the grass, "ordinary-sized man ... no larger than the people near him") and add to must_not_show "NOT a giant, NOT floating, NOT a disembodied head/bust, NOT a cutout, does not fill half the frame, feet on the ground." A from-behind Jesus still passes the face lock (ref line + lock text present; face need not be frontal on a watching/dispersal beat).

- **A NIGHT/moonlit beat fails THREE ways at once unless the prose sets three floors — grey "white faces," a spare arm, and a near-black frame (2026-08-13, row 146 vine-and-branches, Cameron: "0:40 some bystanders have white faces… 0:47 man has multiple arms… 1:19 picture has Jesus missing a hand"; all three on one moonlit cut, all PROMPT-AUTOPSY=ALLOWED).** (a) A moonlit crowd with NO skin-tone floor drains several disciple faces to grey/ashen/white ("white faces") — add to must_show/scene "every face warm living olive/tan Middle-Eastern skin, softly moonlit" and to must_not_show "no grey, ashen, pale, white, bluish, desaturated or drained faces" (row 146 b04). (b) The generic "two arms, two hands and one head" tail does NOT stop a spare/third arm on a from-behind figure shouldering a tool while also reaching (row 146 b09 read as 3 arms) — when a hands/arms beat drifts, recompose to the ACTUAL brief (a TIGHT close of the hands doing the one thing) and add "NO extra, third, duplicated, floating or disembodied arm/hand; every visible person has exactly two arms both joined at the shoulders." (c) "Moonlight" with no readability floor renders NEAR-BLACK/unviewable (row 146 b14 was pure dark at 1:19, and the clasp also merged a hand → "Jesus missing a hand") — every night beat needs "clearly VISIBLE in soft moonlight — not a near-black or unreadable frame; every face and hand plainly lit," and complex stacked-hand clasps must state "BOTH of Jesus's hands fully visible, five fingers each." BONUS: b09's prose said "moonlit" but rendered golden-day walking-workers (wrong scene + wrong time); recomposing to the briefed close hands-on-branch fixed the arms, the time-of-day, AND de-duplicated it from adjacent s08 in ONE reroll. Trace each timestamped complaint to the frame that RENDERS at that second (0:47 fell in a beat's hold-through-gap, so it was s09 not the adjacent s08) before rerolling.

- **A closing/reflective TWO-SHOT beat renders "facing each other" when the SCENE prose says both faces turn toward each other — the positive instruction beats a correct must_not_show (2026-08-13, row 95 thief-on-the-cross s11 C-FIX, Cameron: "1:03 they are facing each other again and that is wrong replace it"; PROMPT-AUTOPSY=CAUSED).** b11's must_not_show already forbade "NO crosses angled toward each other," yet the scene commanded "the two faces turned each other's way along the row." The model obeyed the positive line — put BOTH men in a mutual profile gaze and angled both crosses inward to make the eye-line work; the negative bound lost. FIX in one `--redo`: rewrite the scene to "both crosses standing as straight PARALLEL UPRIGHTS seen from the FRONT, both pinned bodies squared to the viewer, each face lifted and at rest looking OUTWARD, never the two faces turned toward each other," and mirror it in must_show + must_not_show (add "NO two faces turned toward each other in a mutual profile gaze, NO figures body-to-body across a gap"). RULE: a "facing each other" complaint is almost always a positive SCENE sentence, not a missing must_not_show — fix the prose that COMMANDS the gaze, don't just re-add the ban. Turn beats (a man turning toward another) must say "only the HEAD turns, the pinned/standing body stays facing FORWARD" (pattern already proven in b05/b07).
- **The Calvary HILL / archaeological-overlook plate can spawn a MODERN metal guardrail-railing + bolts in a closing frame (2026-08-13, row 95 s11 reroll).** Regenerating a low two-cross closer on the HILL look produced a modern metal handrail with vertical bars across the mid-ground (a tourist-overlook guardrail) plus a metal bolt on the cross upright — a modern-object gate fail. FIX: add to the beat's must_not_show "NO modern fence / railing / guardrail / handrail / metal bars, NO modern metal bolts or hardware — ancient bare-rock ground with only the distant stone city wall behind." Watch any Calvary/hilltop closer for this; it does not appear on the wide 3-cross beats (crowd + wall fill the mid-ground) but shows up when the mid-ground opens up behind two figures.
- **v2_gen_api HTTP calls can HANG indefinitely (no read-timeout) — wrap paid gens in `timeout` (2026-08-13, row 95).** A b11 `--redo` sat 9 min in state S (sleeping), 0% CPU, one open socket, no new api-spend row, while billing was healthy (a concurrent lane was spending). It was a hung HTTP read with no client timeout, not a 429. Killing it left nothing partial (the script writes the image only after the full response). Re-running under `timeout 240 python3 v2_gen_api.py …` succeeded immediately. When a single-beat gen exceeds ~3–4 min with no output and no spend row, it is hung, not slow — kill and retry under a timeout guard; do not keep waiting.
- **A NEW-STORY REPLACEMENT row has no rendered V1 mp4 — `v2_assemble` needs TWO module-level flags set or it crashes, and the archived old build must be de-globbed (2026-08-13, row 140 bronze-serpent, first V2 cut of a Cameron-approved story swap).** When a row was REPLACED (old story archived in a sibling `build-NN-oldslug/`, new story authored fresh), the new build's V1 dir (`media-production/build-NN-newslug/`) has only `audio/*.mp3` segments, no rendered `.mp4`. Two failures, in order: (1) `v2_assemble.py NN` → "expected exactly one v2 build dir … found ['build-NN-new','build-NN-old']" because the archived build still carries a `beats_v2.py` the row-resolver globs; fix by `git mv build-NN-old/beats_v2.py build-NN-old/beats_v2.RETIRED.py` (established pattern, cf. row 44 two-debtors). (2) Then "needs exactly one authoritative V1 MP4, found []" and a `None` output-name crash; the assembler's OWN FIX message says add `AUDIO_FROM_V1_SEGMENTS = True` — ALSO add `OUTPUT_VIDEO_NAME = "book-ch_slug.mp4"` (no V1 mp4 means the output name can't be inferred, so it stays None). Both are module-level assembly config (like pentecost row 44), NOT beat/scene/lock content, so they're a legitimate runner edit. Audio then rebuilds from the V1 segment mp3s (AUDIO REBUILD PASS, not AUDIO LOCK — there's no prior mp4 to hash against; the hash WILL be new, that's expected). Also sweep the reviewer: a replaced row often has STALE duplicate `id="vNN"` cards for the old story/stories — convert one to the new cut and DELETE the rest so exactly one correct card is served.

- **An "aging" character lock that GREYS THE HAIR reads to Cameron as a BROKEN IDENTITY, not as the passage of time (2026-08-13, row 147 joseph-forgives, OPEN complaint "Joseph's hair is grey even though it has been black before… change it").** On a story that spans years (Joseph: Genesis 45 vizier → Genesis 50 after Jacob's death), the authored JOSEPH lock said "older (~55) in Genesis 50" and the late beats' scene text said "greyer now"/"grey heads" — so the model greyed Joseph in exactly those beats while he stayed jet-black in the reveal beats. Cameron does not read that as ageing; he reads it as "this is a different man / you broke the character," ESPECIALLY when the surrounding brothers are also greyed (Joseph blends into a row of matching white beards). AUTOPSY = CAUSED (the lock/scene words did it, the image ref alone couldn't override the text). Durable fix: keep the character's HAIR COLOUR CONSTANT across the whole story (match the face-ref), and age only through deeper face lines and a graver expression — never grey the hair. Regen only the greyed beats (touch-once). Same family as any identity-drift complaint: continuity is carried by keeping the locked traits fixed, and "age" is a trait Cameron wants LOCKED, not varied.
- **A GROUP LOCK that only says "varied faces" collapses to a row of near-identical men — pin the VARIATION explicitly (2026-08-13, row 147, "all the brothers are made to look the exact same, all like santa white hair and beard").** "Weathered, varied faces, guilt-worn" was too weak; the ten brothers rendered as a uniform crowd of grey/white-bearded old men in every group beat. Fix = state the spread positively in the lock: different hair AND beard COLOUR and cut, a real range of ages (most dark-haired 30s–40s, a few salt-and-pepper, only the eldest 1–2 truly grey), "no two share the same face/hair/beard," and an explicit "NOT a uniform crowd of white 'Santa' beards." Add a per-beat must_not_show ("not a row of identical white-bearded old men") on the intimate group beats. Same class as the row-135 count-vs-distinctness lesson: counting heads isn't enough, the individuals must be visibly different. Blind rerolls won't fix a missing distinctness pin — it's an author/lock fix.
- **A single-frame establish that names TWO subjects at TWO distances is a stacked-diptych magnet even WITH the global anti-grid lock present (2026-08-13, row 147 b01, "0:01 is a double picture").** b01's must_show asked for the caravan low in the desert AND the brothers on a ridge *behind* — the model separated them into an upper zone and a lower zone divided by a horizontal dust/haze band, reading as two stacked photos (same family as row-95 thief-on-cross b01/b11). The global "SINGLE UNIFIED PHOTOGRAPHIC FRAME… not stacked panels" lock did NOT prevent it, because the beat's own composition invited the split. Fix = rewrite the composition to ONE continuous depth plane (foreground subject reading unbroken back to the distant subject, no mid-frame band) and add a beat-level must_not_show forbidding "any horizontal band of dust/haze/colour splitting the frame into an upper and lower scene; not two stacked pictures." One reroll on the rewritten prompt landed a clean single desert.

- **A FLEET-CANONICAL character (one of the Twelve, or anyone `character_refs` knows) authored with NO lock + `ref:False` renders OFF-MODEL — promote-first only makes them internally consistent, not fleet-correct; this is an authoring gap → NEEDS-REBUILD, do NOT ship (2026-08-13, row 153 restitution, Peter).** Row 153's 10 Peter beats attached only the temple plate and carried Peter as prose ("PETER per the cast sheets"); PETER was in no beat's `locks` and every beat was `ref:False`, so neither the canonical PETER lock text nor his reference image reached the model → Peter (the protagonist) rendered as an older grey-haired man, a different actor from his mid-30s dark-haired sheet (verified vs shipped build-103, and peers build-19/build-103 lock Peter with `ref:True`). CHECK AT QC TIME: if a recurring named person looks wrong, run `character_refs.resolve('<name>')` — if it's a KNOWN fleet character but the beats don't put them in `locks` with a ref, it's an authoring gap the runner can't fix (editing locks/ref is author-lane) → park NEEDS-REBUILD with the beat list, don't reroll (reroll can't attach a ref) and don't ship (off-model protagonist = repeat-complaint class). DISTINGUISH from STORY-LOCAL characters (LAMEMAN; Moses-per-row-140/105) where local-lock text + `ref:False` + promote-first IS the accepted, shipped pattern — those are fine to build.
- **A "pillar/column descending" beat can render as STACKED TRIPLE PANELS (triptych) despite the ANTI_PANEL clause, and the "pillar of cloud" can read as a thin steam plume (2026-08-13, row 105 b06).** One `--redo` landed a single unified frame with a proper vertical cloud column. Check any pillar/column/beam beat for panel-splitting AND for a weak smoke-plume look; reroll on either.
- **A "shining face" beat (Moses, Ex 34 "the skin of his face shone") most dangerously renders the shine as a hot WHITE LIGHT-BURST concentrated ON THE EYES/forehead — which reads as glowing white demon-eyes, the EXACT defect Cameron has filed 3× (rows 67 "eyes turned into light... looks like a demon", 94 "eyes are Lake white and looks evil", 96) (2026-08-13, row 105 b24 QC-VERIFY-FIX; the first build's single `--redo` only moved the blob from eyes→forehead — still a hot-spot).** The row's own law wants BRIGHT SKIN, no halo/rays. It took TWO rerolls to land it: the passing draw has the radiance as a SOFT backlight bloom behind/around the head with NATURAL DOWNCAST EYES (never a hot-spot on the eye region), people shielding their eyes (Ex 34:30-apt), subject unaware. On ANY glorified/shining face (this + row 67 transfiguration), inspect the EYES at full res first — a shine that touches the eyes is a certain complaint; don't over-reroll into no-shine-at-all either.
- **Long background image-gen runs get SIGTERM'd (exit 143) at an interval under lane concurrency — resume is idempotent and completes on the next call; block on the task with a blocking TaskOutput to keep a headless/unattended turn alive (2026-08-13, rows 153/105).** The kill leaves partial progress on disk (assets already saved persist); just re-invoke the same `v2_gen_api` command (it skips existing frames) until it exits 0. Never conclude "no assets" from an `ls` run in the wrong cwd.

- **`v2_story_cast.py` SILENTLY skips writing REFS when the author left an empty `REFS = {}` block — the runner must wire the face-lock by hand or a ≥3-beat face flips (2026-08-13, row 177 make-me-a-sanctuary, headless).** The tool generates the portrait sheets into `CAST-REF-V2/` but only appends a `REFS = {...}` block when `"\nREFS = {" not in src` (v2_story_cast line ~208). An author who wrote a placeholder empty `REFS = {}` (common on a text-lock-only build) trips that guard, so the portraits land on disk ORPHANED and every beat renders TEXT-ONLY — the exact row-52/55 face-flip setup. DETECT at claim time on any story that follows a named non-Jesus character across ≥3 legible-face beats: after `v2_story_cast`, `grep -A3 'REFS = {' beats_v2.py` — if the portrait exists in `CAST-REF-V2/<tok>.jpeg` but the token is absent from REFS, the face is UNHELD. FIX (runner-legal face-lock, not a beat-content edit): open the portrait to confirm it's a clean legible face, then wire `REFS = {"<TOKEN>": "CAST-REF-V2/<tok>.jpeg"}`; the gen log must print `[+1 char ref: <TOKEN>]`. NOTE the tool also mis-classifies a PLACE token (e.g. TABERNACLE-HOLY) as a person and makes it a portrait — never wire that into REFS (place-as-person is forbidden); leave the place on its promoted plate and ignore the orphaned portrait. Row 177: MOSES wired (held across b02/b04/b07), TABERNACLE-HOLY left a place — 0 rerolls, first-attempt clean.

- **RESUMING a SIGTERM-killed NEEDS-REBUILD regen: AUDIT the on-disk frames before spending — some of the park's target beats may ALREADY be correctly regenerated, and a blind `--only <full-list> --redo` re-pays for them (2026-08-13, row 153 restitution resume).** The park/handoff listed 9 Peter beats to regenerate and gave a `--only … --redo` RESUME command. But a prior (killed) session had already regenerated 4 of them (s02–s05) correctly with the wired PETER lock — they were on disk, >50 KB, dated after the author fix. VIEW the target-beat stills first (crop-compare vs the char ref): the ones that already match the ref are DONE. Then run the PLAIN runner (`v2_gen_api <build> --ceiling …`, NO `--redo`) — it auto-skips existing >50 KB frames and generates ONLY the still-missing ones. Here that meant paying for 5, not 9 ($0.67 vs ~$1.2), and never touching the 4 good frames (touch-once/COST LAW). Rule on any resume: the handoff's beat list is the MAXIMUM set that MIGHT need regen; the ACTUAL set is (that list) minus (whatever a dead prior run already landed correctly) — confirm by eye, and prefer the plain skip-existing runner over `--redo` unless a specific on-disk frame is verified still-bad. Companion to line-61 (resume is idempotent): idempotent means it won't double-generate missing frames, but `--redo` DEFEATS that by forcing regen of everything named.

- **A CLOSING "reaching back / welcoming" beat with the mover at a threshold still draws a full lens-stare + hand-out-at-the-viewer even when must_not_show says "not to the camera" (2026-08-13, row 185 many-mansions b14).** The first take of the final Father's-house threshold beat put Jesus square to the lens with his hand extended at the camera (an unwanted direct address). ONE `--redo` fixed it: the reroll turned his body INTO the scene (into the house) with the hand reaching back into the frame and a warm GLANCE back over the shoulder — reads as "come home, follow me," not a stare. When authoring/QC a "reaching back toward those he loves" closer, expect the lens-stare failure and check the render; the fix is body-into-scene + hand-into-frame + glance (not a frontal address). 7.1% reroll, $0.13.

- **CROWD-LOOKING-UP-IN-WONDER beats drift to GOSPEL-ART ILLUSTRATION even in a photoreal row — QC them hardest, a plain reroll usually fixes it (2026-08-13, row 191 b10 "a dare no king could make", Opus runner).** A beat where a GROUP turns their faces/open hands up toward a radiant opened sky (awe/praise) is the one most likely to render as a smooth idealized digital-painting (Latter-day Saint Gospel-Art look) while every other frame in the row is a real photograph — a Law-14 mix-fail (a single stylised frame among photoreal ones throws the viewer out = a new complaint). Extends RUNNER-LESSONS 146d (warm cozy scenes drift painterly). Author-lane fix is the explicit "PHOTOREAL ONLY — real photograph, not a painting/illustration/CGI render" clause; the runner (forbidden to edit beat text) just `--redo`s — the drift is stochastic and one reroll landed photoreal here (b10, within the 15% budget). Always extract these beats from the RENDERED mp4 and confirm they read as a photo, not an illustration.

- **RESUMING A DIED BUILD whose STALE-V1 guard trips on the EXCESS branch → set `AUDIO_FROM_V1_SEGMENTS = True`, but FIRST engine-parity-check the segment mp3s or you swap the voice (2026-08-13, row 181 morning-stars-sang, Opus runner resume).** A generate-only session died before assembly; on resume the default stream-copy raised `STALE V1 FINAL … runs 67.433s but the timeline … is 66.612s — 0.821s of audio … not in this build any more` (the excess branch, not the row-25 predates branch). The prescribed fix is `AUDIO_FROM_V1_SEGMENTS = True` (rebuild from `<v1dir>/audio/*.mp3` at extract_beats offsets — nothing re-voiced). **BUT before flipping it, prove the segment mp3s are the SAME engine/voice as the V1 final** — `ffprobe -show_entries stream=sample_rate,bit_rate`: ElevenLabs = `44100,128000` (segments) / `44100,~92k` (the final's AAC), edge-tts = `24000,48000`. Row 181's audio/ segs were all 44100/128000 = the same ElevenLabs voices as the final, so the flag rebuilds identical voices; if they had been 24000 edge-tts on an ElevenLabs final, flipping the flag would ship the WRONG (old edge-tts) voice — that is the engine-parity failure. Also: this flag makes the shipped audio a fresh segment-assembly, NOT byte-identical to the stale V1 mp4 — so word the review card "the voices/narration are the same recording," not "byte-identical to the cut you have" (the stale 0.8s tail is intentionally dropped). Drop-check still applies (concat_base clips == len(BEATS); last-beat window start < card_start).

- **A must_show that literally contains "BLUE caption (SCRIPTURE)" can make the generator BAKE the word "SCRIPTURE" into the frame as on-screen text (2026-08-13, row 198 b09, 1 reroll).** On a scripture beat whose must_show opens with the parenthetical "BLUE caption (SCRIPTURE)" (an author cue meant for the caption layer, NOT the picture), one take out of the row rendered the literal blue word SCRIPTURE across the bottom of the image — a generated-text artifact (Law-7 / no rendered text = mandatory reroll). Its sibling scripture beats (b05-b08, same cue) rendered clean, so it is a one-off fluke a single `--redo` clears — NOT a systemic park. GATE: on any scripture/GOD-voice beat, scan the frame for the baked words SCRIPTURE/GOD/BLUE/CAPTION and reroll on sight. (Author-side follow-up if it recurs on a build: keep the "(SCRIPTURE)"/"(BLUE)" caption cue OUT of the picture must_show text — put the colour law in the beat's SPEAKER note, not in the sentence the generator reads as scene content.)

- **A "Messiah/God NEVER embodied" OT row can still drift an EMBODIED-JESUS read onto a gathering/homecoming CLOSING frame — a central lone long-haired bearded figure the crowd faces reads as Christ even in a NON-cream robe (2026-08-13, row 198 b12, 2 rerolls).** The closing "the seeking ones come home" beat twice rendered a central bearded, shoulder-length-haired man that the whole gathered crowd walked toward / faced — a "coming to Christ" composition — first in a light/cream tunic (double fail), then in a blue-grey tunic (still Jesus-adjacent). For a row whose entire doctrinal spine is that the Messiah is never pictured, this is the exact closing image Cameron would flag, so it is mandatory-garbage (not subtle drift) even though "no cream" alone technically passed on take 2. FIX that lands: compose the homecoming around a PEER action (a homecoming embrace between two ordinary travellers, families with children greeting) with NO single central bearded focal figure the crowd is oriented toward. GATE any Messiah-never-embodied gathering/teaching/welcome wide for a lone central long-haired bearded man being faced/approached by the group — reroll toward a distributed, peer-to-peer composition.

- **A build's authored QC.md "no open complaint" line is a SNAPSHOT and can be STALE — a complaint filed AFTER authoring is caught ONLY by `v2_outline.py <row>` at build time (2026-08-13, row 199 fishers-and-hunters).** QC.md (authored 2026-08-07) said "no open Cameron complaint," but the LEARNING-LAW re-check at build time (`v2_outline 199`) surfaced **"Not real new voice"** — filed after the author lane ran. Had the runner trusted the authored QC line and default-stream-copied, it would have re-shipped the exact stale-audio cut Cameron rejected (the worst failure). **ALWAYS run `v2_outline` yourself before the first credit and treat ITS complaint list as authoritative over any authored QC/board text; correct the COMPLAINT LEDGER to match.** For "Not real new voice / Not new audio," the fix is the rows-191/181/189/198 class: verify the V1-dir `audio/*.mp3` are 44100/128k (the ElevenLabs cast; edge-tts is 24000/48000), set `AUDIO_FROM_V1_SEGMENTS=True`, and ship the AUDIO REBUILD (the stale V1 mp4's embedded track is the thing he's complaining about).

- **THE GENERATOR ADDS ANACHRONISTIC EYEGLASSES/SPECTACLES TO ELDERLY CRAFTSMEN & READERS — a modern-object ship-blocker that a blind `--redo` may REPRODUCE (2026-08-13, row 116 graven-on-his-palms b21, Opus runner).** The closing beat staged an old engraver "examining the finished tablet"; the model twice rendered him in modern wire-rim reading spectacles (with nose-pads) — a clear first-century anachronism Cameron would flag, plus a lens-stare. AUTOPSY = ALLOWED (verdict 2): nothing in the beat banned eyewear, and the generator strongly associates "old man examining fine/close work" (engraving, reading a scroll, threading, jewellery) with reading glasses. Reroll #1 reproduced them; reroll #2 (the 2-reroll cap) cleared them. GATE any beat with an ELDERLY person doing close/fine work or reading for spectacles/pince-nez/monocle and REROLL them off (they are a random artifact, usually gone within 2 tries). The durable author-lane fix is a `must_not_show` ban ("no eyeglasses/spectacles/reading glasses/pince-nez/monocle — no eyewear of any kind; first-century Judea had none") on every close-work/reading beat — a runner may not add it, so if 2 rerolls don't clear it, FIX-WAVE + flag the author, never ship the glasses.

- **AN ETHEREAL / "no visible sun / strange warm light" DAY beat can drift to a PAINTERLY ILLUSTRATION even when its photoreal sibling beats (same crowd, same place) render fine — and a blind reroll can repeat it AND bake readable text into scrolls (2026-08-13, row 125 i-never-knew-you b06).** b06's scene ("morning light that comes from no visible sun") pushed the model to a smooth digital-illustration render (Law-14 MIX = hard fail) TWICE; the 2nd take also printed legible Hebrew on the scrolls (a text-in-image defect). b07/b08/b09 (the same pleaders-at-the-door composition one moment later) all rendered photoreal, so it is seed/wording luck on the one ethereal-lit beat, NOT systemic — a 3rd `--redo` landed photoreal. Autopsy = generator style-drift (runner can't edit the beat's "no visible sun" wording; the durable author fix is an explicit "PHOTOREAL ONLY, real photograph not a painting/illustration" clause on any ethereal-light beat). When a warm/strange-light beat drifts painterly, reroll (budget for up to the cap) and re-QC the reroll for BOTH style AND freshly-baked scroll/tablet text.
- **A GREAT-DOOR / THRESHOLD beat renders MODERN door hardware — a lever handle, knob, mortise lock, keyhole and rectangular metal escutcheon — on the finale/hero frame (2026-08-13, row 125 b15).** The "invitation / open door / Jesus's hand" closing beat put a 19th-20th-c. lever-and-escutcheon lockset on the wooden door; a reroll still carried a metal lockset (and redraws the locked Jesus face = risk). Autopsy = ALLOWED (nothing banned hardware; runner can't edit beat text). BEST FIX = a targeted `gemini-3-pro-image` EDIT (row-39/93 method): "remove the modern handle/lock/keyhole/plate, leave a plain door or at most a simple forged-iron RING pull, keep every other pixel" — preserves the perfect composition + locked face, `.predooredit.bak`, ~$0.13, NOT a reroll. GATE any door/gate/threshold frame for a lever/knob/keyhole/escutcheon; period doors have a wooden bar, ring pull or iron bolt only.
