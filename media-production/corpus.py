#!/usr/bin/env python3
"""Shared, read-only helpers for resolving the authoritative MBM video corpus.

Several rows still have an archived build folder beside their current replacement.
Tools that select the first or last ``build-NNN-*`` directory silently operate on
the wrong story.  This module is the single resolver for media tooling.

It also normalizes both narration formats used in the repository:

* ``(id, speaker, text)``
* ``(id, voice, rate, pitch, text)``

Callers receive ``(id, canonical_speaker, text)`` in both cases.
"""

from __future__ import annotations

import glob
import json
import os
import re
import subprocess
import sys
from collections.abc import Iterable


BUILD_RE = re.compile(r"^build-0*(\d+)-(.+)$")
FINAL_MP4_RE = re.compile(r"^[0-9a-z]+(?:-[0-9a-z]+)*-\d+_.+\.mp4$")


# Rows with two root-level folders.  The other folder is historical and must never
# be selected by QC, re-voice, rebuild, or publish tooling.
CANONICAL_BUILD_SLUGS: dict[int, str] = {
    65: "help-mine-unbelief",
    67: "the-transfiguration",
    86: "the-wise-men",
    89: "the-last-supper",
    128: "heart-far-from-me",
    133: "what-jesus-called-hell",
    134: "today-in-paradise",
    137: "one-as-we-are-one",
    140: "naaman-washes",
}


SPEAKER_ALIASES = {
    "n": "narrator",
    "nar": "narrator",
    "narr": "narrator",
    "narrator": "narrator",
    "j": "jesus",
    "jes": "jesus",
    "jesus": "jesus",
    "g": "god",
    "god": "god",
    "s": "scripture",
    "scr": "scripture",
    "scripture": "scripture",
    "w": "woman",
    "wom": "woman",
    "woman": "woman",
}


def build_number(path: str) -> int | None:
    match = BUILD_RE.match(os.path.basename(path.rstrip("/")))
    return int(match.group(1)) if match else None


def build_slug(path: str) -> str | None:
    match = BUILD_RE.match(os.path.basename(path.rstrip("/")))
    return match.group(2) if match else None


def find_main_mp4(build_dir: str) -> str | None:
    """Return the scripture-named final MP4, excluding backups and render parts."""
    hits = [
        path
        for path in glob.glob(os.path.join(build_dir, "*.mp4"))
        if FINAL_MP4_RE.match(os.path.basename(path))
    ]
    return sorted(hits)[0] if hits else None


def canonical_builds(media_root: str) -> dict[int, str]:
    """Return row -> authoritative build directory for the current 200."""
    grouped: dict[int, list[str]] = {}
    for path in sorted(glob.glob(os.path.join(media_root, "build-[0-9]*"))):
        if not os.path.isdir(path):
            continue
        number = build_number(path)
        if number is not None:
            grouped.setdefault(number, []).append(path)

    resolved: dict[int, str] = {}
    for number, candidates in grouped.items():
        wanted = CANONICAL_BUILD_SLUGS.get(number)
        if wanted:
            exact = [path for path in candidates if build_slug(path) == wanted]
            if len(exact) != 1:
                names = ", ".join(os.path.basename(path) for path in candidates)
                raise RuntimeError(
                    f"row {number}: canonical slug {wanted!r} not found uniquely in {names}"
                )
            resolved[number] = exact[0]
            continue

        buildable = [
            path
            for path in candidates
            if os.path.isfile(os.path.join(path, "build.py"))
            and os.path.isfile(os.path.join(path, "make_narration.py"))
        ]
        if len(buildable) == 1:
            resolved[number] = buildable[0]
            continue
        if not buildable and len(candidates) == 1:
            resolved[number] = candidates[0]
            continue
        if len(candidates) == 1:
            resolved[number] = candidates[0]
            continue

        names = ", ".join(os.path.basename(path) for path in candidates)
        raise RuntimeError(
            f"row {number}: ambiguous build directories ({names}); add an explicit "
            "CANONICAL_BUILD_SLUGS entry"
        )
    return resolved


def transcript_paths(media_root: str) -> dict[int, str]:
    """Return row -> canonical transcript JSON path."""
    paths: dict[int, str] = {}
    pattern = os.path.join(media_root, "TRANSCRIPTS", "[0-9][0-9][0-9]-*.json")
    for path in sorted(glob.glob(pattern)):
        try:
            data = json.load(open(path, encoding="utf-8"))
            row = int(data["row"])
        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"cannot read transcript {path}: {exc}") from exc
        if row in paths:
            raise RuntimeError(
                f"row {row}: duplicate transcript JSON files "
                f"{os.path.basename(paths[row])}, {os.path.basename(path)}"
            )
        paths[row] = path
    return paths


def load_transcript(path: str) -> list[tuple[str, str, str]]:
    data = json.load(open(path, encoding="utf-8"))
    out: list[tuple[str, str, str]] = []
    for segment in data.get("segments", []):
        out.append(
            (
                str(segment["id"]),
                normalize_speaker(segment["speaker"]),
                str(segment["text"]),
            )
        )
    return out


def normalize_speaker(raw: object) -> str:
    value = str(raw).strip()
    return SPEAKER_ALIASES.get(value.lower(), value.lower())


def _segment_dump_code() -> str:
    """Python executed inside a build so its local narration module can load."""
    return r'''
import json
import make_narration as m

labels = {}
for canonical, names in {
    "narrator": ("NARRATOR", "NAR", "NARR"),
    "jesus": ("JESUS", "JES"),
    "god": ("GOD",),
    "scripture": ("SCRIPTURE", "SCR"),
    "woman": ("WOMAN", "WOM"),
}.items():
    for const in names:
        value = getattr(m, const, None)
        if value is not None:
            labels[str(value)] = canonical

aliases = {
    "n": "narrator", "nar": "narrator", "narr": "narrator",
    "narrator": "narrator",
    "j": "jesus", "jes": "jesus", "jesus": "jesus",
    "g": "god", "god": "god",
    "s": "scripture", "scr": "scripture", "scripture": "scripture",
    "w": "woman", "wom": "woman", "woman": "woman",
}

out = []
for segment in m.SEGMENTS:
    if len(segment) >= 5:
        sid, raw_speaker, text = segment[0], segment[1], segment[4]
    elif len(segment) >= 3:
        sid, raw_speaker, text = segment[0], segment[1], segment[2]
    else:
        raise ValueError("unsupported SEGMENTS tuple: %r" % (segment,))
    speaker = labels.get(str(raw_speaker), aliases.get(str(raw_speaker).lower(),
                                                        str(raw_speaker).lower()))
    out.append([str(sid), speaker, str(text)])
print(json.dumps(out))
'''


def load_build_segments(
    build_dir: str,
    *,
    executable: str | None = None,
    strict: bool = False,
) -> list[tuple[str, str, str]] | None:
    """Load and normalize a build's SEGMENTS without polluting this process."""
    executable = executable or sys.executable
    result = subprocess.run(
        [executable, "-c", _segment_dump_code()],
        cwd=build_dir,
        capture_output=True,
        text=True,
    )
    try:
        raw = json.loads(result.stdout.strip().splitlines()[-1])
        return [(str(sid), normalize_speaker(speaker), str(text)) for sid, speaker, text in raw]
    except (IndexError, TypeError, ValueError, json.JSONDecodeError) as exc:
        if strict:
            detail = result.stderr.strip() or result.stdout.strip() or str(exc)
            raise RuntimeError(
                f"cannot load narration segments from {build_dir}: {detail}"
            ) from exc
        return None


def rows(values: Iterable[str]) -> set[int]:
    return {int(value) for value in values}
