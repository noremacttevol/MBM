# LENGTH & NARRATION LAW — the words earn the runtime

**Locked by Cameron, 2026-07-24.** Third leg of the STORY-BLUEPRINT system, beside
STORY-COVERAGE-LAW (pictures) and STORY-BLUEPRINT-SYSTEM.md. Governs how LONG a video
runs and what the NARRATOR and the Bible VOICES actually say. Companion to SPEAKER-LAW.

The picture audit answered "how many stills and what do they show." This answers the
other two things Cameron asked for: **"determine the length of the video"** and
**"who needs to talk and say what, and what the narrator needs to say in between to
tell the story the best way."**

---

## PART A — LENGTH (story-driven, never a target)

Same law as the pictures: **no clock, no target runtime.** A video is the right
length when **every second earns its place** — the words are either advancing the
story or giving a beat room to land. Cut nothing that carries the story; keep nothing
that doesn't.

### TOO LONG — trim it. Signs (all measured against the actual narration):
- **The narrator explains the moral.** Once the story has shown it, extra sentences
  telling the viewer what it means are dead weight — the closing card does that job.
- **Repetition.** The same point made twice in different words. Keep the stronger one.
- **Editorializing / commentary** the scene doesn't need ("and isn't that just like
  us today…"). If it isn't scene, turn, or the bridge to the next line, it's padding.
- **Dead stretches** where nothing new is said and nothing new is shown.
- Practical flag: most builds over ~200s are rambling unless they are a genuine
  multi-scene epic (nativity/passion/resurrection sequences). Read them first.

### TOO SHORT — give it room. Signs:
- A **turn gets rushed** — the hinge of the story flies by in half a sentence.
- A beat the picture plan needs has **no words under it** to carry it.
- The ending **lands before the feeling does.**

### The verdict to write (per video)
`KEEP ~Ns` · or `TRIM to ~Ns — cut <which segments/lines> (reason)` · or
`EXPAND — <the turn/beat that needs words>`. Give the honest read; the tier range in
STORY-BLUEPRINT-TABLE is a sanity mirror, not the answer.

---

## PART B — NARRATION (the narrator's three jobs, and nothing else)

Between the quoted Bible lines, the narrator does exactly three things:
1. **Sets the scene** the next picture will show.
2. **Names the turn** so the beat lands.
3. **Bridges** to the next quoted line.

That is all. The narrator **never explains the moral, never tells the viewer what to
feel, never editorializes, never preaches.** The pictures, the Bible voices, and the
one closing question carry the meaning.

### Flag and prescribe a fix where the narration:
- **Explains the moral / tells us what to feel** ("this shows us that God…", "and
  don't we all…"). → Cut or shrink to scene-and-turn.
- **Rambles or repeats.** → Tighten to the one strong line.
- **Breaks the reverent tone** with modern editorial voice or slang. → Rephrase plain
  and reverent (do not rewrite into KJV — narrator is plain modern English).
- **Runs long before a quoted line** so the scripture loses its punch. → Trim the
  wind-up.

### THE BIG ONE — scripture lifts (who should be talking)
The most powerful narration fix: wherever the narrator **paraphrases words a Bible
figure actually said**, prescribe **lifting that line out of narration into the real
voice, in KJV** — Jesus-red, God-green, scripture-blue (for other people quoted), or
women-pink — exactly as the prodigal build did (the father's and the elder brother's
lines were lifted from narrator paraphrase into Jesus-red because Jesus tells the
parable). Hearing Jesus / the character say it themselves always beats the narrator
reporting it. For each, name: the segment, the paraphrase, the KJV line it becomes,
and the speaker/colour.

### Confirm the cast
Is every voice the story needs present? Flag any figure whose own recorded words are
currently missing entirely (not just paraphrased). Confirm speaker colours match
SPEAKER-LAW (Deity-green vs. about-the-LORD-blue; a quoted man = blue not red; women
= pink).

---

## OUTPUT (append to each build's PRESCRIPTION.md)

Add two sections to every PRESCRIPTION.md, drawn ONLY from the actual make_narration.py
SEGMENTS (anti-fabrication — never invent lines):

```markdown
## Length read
Verdict: KEEP ~Ns  /  TRIM to ~Ns — cut <what> (<why>)  /  EXPAND — <what>
<one or two sentences of evidence from the actual narration>

## Narration read
- Narrator fixes: <segment id → what to cut/tighten/rephrase, or "clean">
- Scripture lifts: <seg → "paraphrase" → KJV line → SPEAKER/colour>, or "none available"
- Cast/colour: <missing voice or colour correction, or "correct">
```

Do not rewrite the audio or the SEGMENTS yourself — another session owns that. You are
writing the SPEC of what length and narration changes are needed. Report, don't edit
the scripts.
