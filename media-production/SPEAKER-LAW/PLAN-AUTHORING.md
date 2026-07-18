# How to author a speaker plan

You are deciding **who is speaking every line** of one MBM story video, so the
narration voice and the caption colour are both correct. Read
`media-production/SPEAKER-LAW.md` first — it is the law. This file is the
procedure.

You are working as a Latter-day Saint making "milk before meat" content: lead
with the simple, true, warm parts of the restored gospel. Never sensational,
never doctrinally sloppy.

---

## Input

`SPEAKER-LAW/briefs.json` — one entry per build, already extracted for you:

- `reference` / `book` / `testament` — e.g. `Exodus 33`, `OT`
- `segments` — every current segment: `id`, `text`, `currently_red`
- `beats` — the current `[seg_id, still_var, zoom_dir]` running order
- `still_vars` — `{"S1": "s1-the-tent.jpeg", ...}`
- `assets` — the image files actually on disk

## Output

`SPEAKER-LAW/plans/<build>.json`, exactly this shape:

```json
{
  "build": "build-114-abraham-sodom",
  "reference": "Genesis 18",
  "notes": "plain-English summary of what moved and why",
  "segments": [
    {"id": "n1", "speaker": "narrator", "text": "..."},
    {"id": "s23", "speaker": "scripture", "verse": "Genesis 18:23", "text": "..."},
    {"id": "jv26", "speaker": "god", "verse": "Genesis 18:26", "text": "..."}
  ],
  "beats": [["n1", "S1", "in"], ["s23", "S4", "out"]],
  "spoken": {},
  "stills_wanted": {"S5": "what this still now needs to show, and why"}
}
```

`speaker` is one of `narrator`, `jesus`, `god`, `scripture`, `woman`.

---

## The five decisions

### 1. Is this line verbatim KJV, or the storyteller?
Only the storyteller speaks modern English. Everything else is **verbatim King
James text a viewer could look up**. If a segment paraphrases scripture in
modern English, it stays `narrator` — unless you lift the real verse out (see 3).

### 2. If it is scripture, who said it?

| | |
|---|---|
| `jesus` | **Only** where a red-letter KJV actually prints red. |
| `god` | The Father, the Holy Ghost, or the premortal Christ (Jehovah). |
| `scripture` | Everyone else — Paul, prophets, apostles, people in the stories, the men who wrote it. |
| `woman` | Any woman the Bible records speaking. |

**The test is never "who is the character?" It is "does a red-letter King James
Bible print this line in red?"**

- **Old Testament Deity speech is `god`, never `jesus`.** A red-letter Bible
  leaves it black because Christ had not yet come in the flesh — but it is still
  Deity speaking, and green carries that. This is most of rows 151–200.
- **Epistles are `scripture`.** Romans, Corinthians, Ephesians, Hebrews, James,
  Peter, John's letters — that is Paul or another writer, never Jesus.
- **Acts is `scripture`** except where the risen Christ speaks directly.
- **Narration inside the Gospels is `scripture`**, not `jesus`: "And Jesus
  answering said unto him" is Matthew writing, not Jesus speaking.
- **Revelation** red-letters Christ's explicit sayings ("I am Alpha and Omega",
  the letters to the seven churches). John's visionary narration is `scripture`.

### 3. Parables — where red is still right
Inside a parable the characters' words are **Jesus's** words, and a red-letter
KJV prints the whole parable red. These stay `jesus`:
*"Well done, thou good and faithful servant"*, *"There was a certain creditor
which had two debtors"*, *"Then said he unto the dresser of his vineyard"*.

### 4. Split any segment that mixes speakers
A segment is the atomic unit of both audio and colour, so a mixed one cannot be
coloured correctly.

> `"And Jesus answering said unto him, Suffer it to be so now: for thus it
> becometh us to fulfil all righteousness. Then he suffered him."`

becomes three: `scripture` → `jesus` → `scripture`.

**Both halves stay on the SAME still** — consecutive beats over one image. No
new artwork, and the edit the viewer sees is unchanged.

### 5. Lift buried scripture, and look for the women
When the narrator paraphrases something a person actually said, lift the real
KJV line out as its own beat and let the narrator retell it after. This is the
biggest storytelling upgrade available, and it is where the women are:

- `#149 Hannah is Heard` narrates *"Lord of hosts, give me a son"* — that is
  1 Samuel 1:11, Hannah, and it should be `woman` speaking the real verse.
- `#148 Ruth` narrates *"Where you go, I'll go"* — Ruth 1:16, `woman`.

Cameron's instruction: **any time a woman in the Bible is recorded saying
something and you judge it would make the video better, include it. Look for
them.**

---

## The retelling rule (mandatory)

After every Old English line, the narrator says it again in plain modern
English. Not a summary — a retelling that makes it land for someone today.

> `god`: "I will make all my goodness pass before thee, and I will proclaim the
> name of the LORD before thee."
> `narrator`: "Show me your glory, Moses asked. And God answered — I will make
> all my goodness pass in front of you. Not his power. Not his greatness. His
> goodness."

Keep the narrator's existing voice and warmth. Where a narrator segment already
does this work, leave it; only add a retelling where the Old English would
otherwise land unexplained.

---

## Hard rules

1. **KEEP the original segment ids. Only ADD new ones.** Builds reference beats
   by name outside `BEATS` — music beds, `start_of['jv26']`, `PEAK`. Renaming an
   id orphans those and the render dies. If `jv26` becomes God's line, it stays
   `jv26`; Abraham's new line gets a fresh id like `s23`.
2. **Every segment in `segments` must appear in `beats`** (except `card`), and
   every beat's still var must exist in the brief's `still_vars`.
3. **Keep `card` last** and leave its text alone unless it quotes scripture.
4. **Never invent scripture.** Every non-narrator line must be verbatim KJV. If
   you are not certain of the exact wording, leave it as narrator paraphrase and
   say so in `notes`.
5. **Do not touch the artwork.** New beats reuse existing stills.
6. Put homograph decisions in `spoken` (e.g. `{"bow": "boh"}`) — caption keeps
   the true spelling, only the spoken string changes. Do not respell a word
   unless you are confident; a bad respelling is worse than none.

## `stills_wanted`

Where splitting and retelling now leave one still carrying a long stretch, note
what it should show. Keyed by still var. This feeds a separate art session — you
are not generating images, only describing the need. Frame it for the moment the
words describe, not a summary of the scene.
