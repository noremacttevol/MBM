---
description: Run the Jesus/cast face-consistency gate on a build folder (arg = build slug or number)
argument-hint: "[build-07-peter-water | 7 | (blank = all build-* with a PROMPTS.md)]"
allowed-tools: Bash(python3:*), Bash(ls:*), Bash(git status:*)
---

Run the face/cast gate on the build folder(s) for: **$ARGUMENTS**

- If `$ARGUMENTS` names a folder (e.g. `build-07-peter-water`), run:
  `python3 media-production/jesus_face_gate.py --dir media-production/$ARGUMENTS`
- If it's a bare number (e.g. `7`), find the matching `media-production/build-7*`/`build-07*`
  folder and run the gate on it.
- If blank, run the gate on every `media-production/build-*` folder that has a `PROMPTS.md`
  and report only the ones that FAIL.

The gate must exit 0 ("RESULT: PASS"). A FAIL means a Jesus shot is missing the byte-identical
JESUS LOCK v3 paragraph or its `REF: jesus-master-ref` line, or a wrong-Jesus drift word
(caucasian/pale/blue-eyed/blond/halo/glow) appears. Report the exact failures and what to fix —
do not spend any Flow credit until it passes. Remember: the pre-commit hook also blocks any
commit whose staged PROMPTS.md fails this gate.
