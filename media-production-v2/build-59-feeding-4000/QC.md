# QC / RUNNER HANDOFF — build-59-feeding-4000 (Mark 8:1-9)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 27 beats, ~154 s.

---

## ✅ AUTHOR DONE 2026-08-07 (Machine A `Dev`, Fable-5 author lane) — SECOND-FEEDING SCHOLARSHIP added, $0, 0 image credits

**COMPLAINT LEDGER — the ONE open complaint on this row is now ANSWERED:**

> Cameron (2026-08-06, reportedAgainst 3005df5d1da3): *"if we tell this story as
> the second time he did this and dont give any biblical scholarship on the fact
> that it was true that he did it twice and it was different times becasue it was
> recorded that he did comment on that then we are doing a huge disservice... we
> need refrences in this one and comparisons that give the act a better light not
> just telling the story the same way twice."*

**What in THIS cut fixes it (narrator scholarship, riding existing stills):**

1. **Named plainly as the SECOND, distinct feeding.** `n2b` now adds: *"And here
   they were, working the very same sums a second time, as if that first miracle
   had never happened."* — on the counting-disciple callback (b13b reuses s12),
   right after the existing "the man who had already fed five thousand" line.
2. **The recorded proof that Jesus commented on both.** `n5` now cites it directly:
   *"Later Jesus made the disciples count both feedings — twelve baskets, then
   seven — so they could never blur the two into one. He wanted both of them
   remembered."* This IS Mark 8:19-21 / Matt 16:9-10, where Jesus makes them count
   the five-loaves/twelve-baskets AND the seven-loaves/seven-baskets. (b24, on the
   sack-vs-baskets "arithmetic in one image" still.)
3. **The comparison that gives the act a better light.** `n5` also adds: *"And the
   numbers were the proof this was no retelling: five loaves had left twelve
   baskets the first time; seven loaves left seven this time."* — the differing
   counts (5→12 in Jewish Galilee, Matt 14, vs 7→7 in the Gentile Decapolis, Mark
   8, after three days) are surfaced as the EVIDENCE the events are distinct, not
   trivia. (b23b reuses the seven-loaf inventory still s16 — the loaf image carries
   the loaf-count comparison.)

**Mechanics / cost:** narration edited in the AUTHORITATIVE V1 make_narration.py
(and mirrored in V2); only the two NARRATOR segments n2b + n5 re-voiced with the
same edge-tts AndrewNeural (FREE — Jesus/scripture segments untouched, no
ElevenLabs, $0). Two scholarship beats added (b13b, b23b) that REUSE already-built
stills s12 and s16 — **no new image generated, 0 credits, 0 rerolls.** Timeline
recomputed from the new segment durations (extract_beats: total 172.5 s → 207.3 s,
card_start 189.303); all 29 beats_v2 still-windows remapped and re-audited
contiguous with zero gaps; `--check` PASS. AUDIO_FROM_V1_SEGMENTS=True (already set)
rebuilds the track from the V1 mp3s.

**Complaint stays OPEN in REVIEW-LESSONS until the re-cut ships.** Board: State
BUILT/NEEDS-REBUILD → **Ready ✅**. Re-assembled locally by the author (stills were
all done); RUNNER: verify the new mp4, deploy, and ship with the review card telling
Cameron his second-feeding-scholarship complaint was addressed.

## Coverage shape

Five true wides with stated geometry: b01 (the camped multitude in
broken country), b06 (the sweeping arm toward the empty distances — the
three-days/far-roads subject), b18 (the settling onto BARE ROCK), b23
(the SEVEN-basket line in profile), b25 (the homeward dispersal). Nine
flips including b27 — Jesus ALONE in the emptied dusk camp (phantom-
people trap; an injected crowd would erase the verse's solitude).

## THIS IS NOT ROW 58 — the differences are doctrine, keep them

- SEVEN baskets, not twelve (count law — the two miracles differ on
  purpose; Jesus quizzes the disciples on both numbers in Mark 8:19-20).
- BARE ROCKY ground, no grass (v6 "on the ground" vs John 6's "much
  grass") — if a render shows a green meadow, it is the WRONG miracle.
- The crowd has CAMPED THREE DAYS — settled camp texture (cold fire
  rings, laundry on thorns), not a fresh-arrived crowd.
- SEVEN loaves "and a few small fishes" — the starting basket differs
  from the lad's five-and-two.

## Other checks

- WILDS promote-first from b01. Do NOT take row-54's WILDS plate if
  the stash ever suggests it — the leper's Judean broken country is a
  different region from this Decapolis slope.
- BREAD is a prop lock (the tool misreads it as a place) — no plate.
- No multiplying effect, ever — abundance arrives through hands.
- Direction (row-83): b06's arm sweeps toward the far roads (empty
  distances in frame); b25's streams disperse OUTWARD homeward.
- DISCIPLES distinct (90/107); the compassion close-ups (b07: dozing
  old man, listless child) are ALIVE-looking, weary not corpse-toned
  (row-15).
- Hard bright day → late-afternoon gold → dusk, one direction.
- Only Jesus wears cream.

---

## RUNNER LIGHT-QC + COMPLAINT LEDGER (A-auto Machine A, 2026-08-06)

**COMPLAINT LEDGER: none open.** `v2_outline.py 59` shows no open Cameron
complaint on this row (the V1 draft was only "awaiting your yes"). Nothing to
answer; the cut is judged against the rubric + RUNNER-LESSONS only.

**Light QC — 27/27 frames viewed once, ZERO rerolls (0% vs 15% budget):**
- Realistic-only Law 14: PASS on all 27 — every frame photographic, no
  cartoon/CGI frame. The epilogue beats (s25 home-full, s26 sent-away,
  s27 who-he-is), which are the known cartoon-frame trap, are all photographic.
- WILDS plate: promoted from our own b01 (row-54's leper WILDS was auto-wired
  and REJECTED per this QC — different region; PLACE-WIRING cleared, promote-first
  used). Plate is bare rocky Decapolis slope, settled-camp texture (cold fire
  rings, bundles, laundry-less), NO green meadow → correct miracle vs John 6.
- Seven-count doctrine: s16 = exactly SEVEN loaves + a few small fish. Leftover
  baskets (s23/s24/s27) read ~seven and NEVER twelve — the Mark-8/John-6 count
  distinction holds.
- Scale gate (Law 14): Jesus ordinary-sized in every multi-figure frame;
  children child-sized and stable.
- b27: Jesus ALONE in the emptied dusk camp; departing crowd distant/blurred,
  solitude of the verse preserved.
- Only-Jesus-cream, dark-haired crowd + kids, consistent beards, no modern
  objects, no lens-staring: all PASS.
- Green/hazel Jesus eyes on close-ups s05/s09/s14 = baked-in JESUS-MASTER-REF
  trait, systemic across all V2 rows — NOT rerolled (RUNNER-LESSONS: reroll
  cannot change a baked-in ref trait; master-ref-level fix, not per-row).

**FIX-WAVE (no reroll, cost-law):** exact seven-basket COUNT in s23 (the
designated seven-basket line) and s27 reads ~6-7 in receding perspective, not a
crisp countable seven. Not obvious garbage and never twelve, so kept per COST
LAW; verify/tighten to exactly seven in the fix wave if Cameron flags the count.

---

## RUNNER PARK → NEEDS-REBUILD (Machine A `Dev`, 2026-08-07) — AUTHOR-DOMAIN complaint, $0, pictures untouched

**Cameron's OPEN complaint** (`reportedAgainst 3005df5d1da3`, filed 2026-08-06,
AFTER this cut shipped — the "COMPLAINT LEDGER: none open" note above was written
before the complaint existed and is now stale):

> "if we tell this story as the second time he did this and dont give any biblical
> scholarship on the fact that it was true that he did it twice and it was different
> times becasue it was recorded that he did comment on that then we are doing a huge
> disservice to telling the story. this is not how he wanted his gospel to be told.
> we need refrences in this one and comparisons that give the act a better light not
> just telling the story the same way twice."

**Why this is a runner PARK, not a runner fix (RUNNER-LESSONS "fix lives one stage
upstream", lines 424/439/474):** the complaint is NOT a picture defect and NOT an
audio pronunciation/pacing re-voice. It demands NEW narration CONTENT — added
biblical scholarship, cross-references, and comparisons — which changes the beat
map/scene text. The runner is forbidden to edit scene text or any beat's content
(hard rail). No reroll or identity-edit can add scholarship. $0 spent; all 27
stills and the audio are byte-identical, untouched.

**What the FABLE 5 AUTHOR must do (NEEDS-REBUILD):** rewrite/expand the narration
so this reads as the SECOND, distinct feeding — not a carbon copy of the 5,000 —
and give it the scholarship Cameron is asking for:

1. **Name it as the second miracle, and defend that it truly happened twice.**
   The current script only glances at it once ("the man who had already fed five
   thousand standing right in front of them"). Cameron wants the narration to
   establish plainly that this is a SEPARATE event at a different time and place,
   not the same story retold.
2. **Cite that Jesus himself commented on both feedings** — the recorded proof
   Cameron means: Matt 16:9-10 / Mark 8:19-21, where Jesus points the disciples
   back to BOTH — "the five loaves of the five thousand, and how many baskets ye
   took up? … the seven loaves of the four thousand, and how many baskets ye took
   up?" His own words treat the two as distinct historical acts. That reference
   must appear (as narrator scholarship and/or a KJV card).
3. **Draw the comparisons that "give the act a better light":** the deliberate
   contrasts already doctrinally locked in this build — 5 loaves→TWELVE baskets in
   Jewish Galilee vs SEVEN loaves→SEVEN baskets here in the Gentile Decapolis,
   after THREE days. The differing numbers are the evidence the events are distinct;
   surface them as the point, not trivia.
4. Author decides whether the scholarship rides on existing stills or needs 1-2
   new beats (e.g. a comparison/КJV card for the Matt 16 commentary). Keep audio
   immutability in mind — new narration content = new segment mp3s (author edit),
   which is exactly why this is an author rebuild and not a runner re-cut.

Complaint stays **OPEN** (REVIEW-LESSONS row 59 open:true) until the author's
rebuild ships and answers it. Board: State BUILT→NEEDS-REBUILD, Ready cleared.
