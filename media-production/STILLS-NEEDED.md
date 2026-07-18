# STILLS NEEDED — work order for the art session

**This file is for a different session than the one that writes it.** The speaker /
narration rebuild (`SPEAKER-LAW.md`) does not generate art. It records, per build,
exactly where the story now needs a picture it does not have — and why.

Machine-readable companion: `SPEAKER-LAW/stills-needed.json`.
Read that; this file explains what it means and how to judge a request.

---

## Why better narration creates a stills shortage

This is not a wish list. The shortage is mechanical, and it comes from three
changes the speaker rebuild makes:

**1. Splitting mixed segments multiplies beats on one still.**
A line like *"And Jesus answering said unto him, Suffer it to be so now... Then he
suffered him"* used to be one beat on one picture. Under the speaker law it becomes
three beats — narrator frame, Jesus in red, narrator close — because a red-letter
Bible only prints the middle clause red. All three still sit on **one** still. That
image now has to hold the screen three times as long as it was designed to. A Ken
Burns drift that was gentle over 6 seconds becomes a slow crawl over 18.

**2. The retelling rule roughly doubles the scripture passages.**
Every Old English line is now followed by the narrator saying it again in plain
modern English. That is the right call for a listener — but it doubles the time
spent on whatever picture is under it.

**3. Green pulls Old Testament moments into the foreground.**
Rows 151–200 are full of Jehovah speaking. Those lines used to slide past in the
narrator's voice or in a red that quietly misattributed them. Now they land as their
own moment, in their own voice and colour — and a moment that lands wants an image
that matches it.

So: the better the story is told, the more the pictures have to carry. Every entry
in the JSON names the beat that got longer and what it now needs.

---

## The lens for this round of art

The last pass generated stills against a shorter, flatter narration. This round is
tuned differently, and the brief for the art session is:

**Show the moment the words are describing, not a summary of the scene.** When
Jehovah says *"I will make all my goodness pass before thee,"* the picture is that
promise being kept — light moving past a man hidden in a cleft of rock — not a
generic portrait of Moses. Specific beats, specifically drawn.

**Old Testament scenes are Christ's scenes.** The premortal Jehovah of these
stories is the same Lord as the Gospels. The art should feel continuous with the
Gospel stories — same warmth, same painted light, same reverence — not a colder,
more distant "Old Testament" look. A viewer should not be able to tell from the
palette which testament they are in. This is the single most important note for
rows 151–200.

**The restored gospel becomes obvious by being shown plainly, never argued.**
Priesthood conferred by laying on of hands, baptism by immersion, a prophet
receiving revelation, a temple, families sealed — where scripture describes these,
draw exactly what scripture describes. No captions arguing the point, no symbols
smuggled in. A viewer who reads the verse and looks at the picture should find they
match, and draw their own conclusion. That is milk before meat in art form.

**Reverence over spectacle.** Nothing sensational. Nothing that makes the viewer
admire the artwork instead of feeling the story.

### Binding laws the art session must still obey
All of `PRODUCTION-BIBLE.md` §1 "The Standing Laws" applies unchanged — including
the Jesus Look Standard (long dark hair past the shoulders, one plain undyed
off-white wool robe, warm Middle Eastern skin), the anti-panel sentence in every
wide multi-figure prompt, the action-logic law, and the time-of-day law.
Run `python3 media-production/jesus_face_gate.py --dir <build-folder>` before
spending any credit.

---

## Entry format

Each entry in `stills-needed.json`:

```json
{
  "build": "build-105-face-to-face",
  "reference": "Exodus 33",
  "priority": "high",
  "beat": "g2",
  "speaker": "god",
  "verse": "Exodus 33:19",
  "caption_text": "I will make all my goodness pass before thee...",
  "seconds_on_screen": 19.4,
  "current_still": "s4-moses-on-the-mount.jpeg",
  "reason": "split + retelling put three beats on one still; 19.4s of drift on an image built for 6s",
  "wants": "the promise being kept — light passing a man sheltered in the cleft of the rock",
  "slug": "s4b-goodness-passes-by"
}
```

- **priority** — `high` when one still now carries more than 15s, or when a
  `god` / `woman` beat has no image of its own; `medium` 10–15s; `low` under 10s
  but still thin.
- **seconds_on_screen** — measured from the rebuilt narration, not estimated.
- **slug** — the filename the build already expects. Drop the finished `.jpeg`
  into `build-NNN-name/assets/<slug>.jpeg` and the build picks it up with no
  code change.

## How the art session should work through it

1. Sort by `priority`, then by `seconds_on_screen` descending — the longest
   lonely image is the worst viewer experience in the library.
2. Generate against `wants` plus the verse in full context, under the standing laws.
3. Save to the named slug. Do not edit `build.py`, `make_narration.py`, `QUEUE.md`,
   `approvals.json`, or `COMPLAINTS.md` — those belong to other sessions.
4. Tick the entry's `done` field to `true` in the JSON and commit only that file
   plus the new assets.

---

*Generated by the speaker/narration rebuild. Entries are appended per build as each
video is rebuilt, so this file grows while the rebuild runs — an art session can
start on the high-priority entries before the rebuild finishes.*
