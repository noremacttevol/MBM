#!/usr/bin/env python3
"""Audit or sync canonical TRANSCRIPTS text into build make_narration.py files.

The ElevenLabs recovery pass correctly voiced the trimmed JSON transcripts, but
many build scripts still contain the older text.  That produces stale captions and
false echo failures even when the audio itself is correct.

By default this is read-only.  Pass ``--apply`` to rewrite only the SEGMENTS
assignment, preserving each build's three-field or five-field tuple format.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys
from dataclasses import dataclass

from corpus import (
    canonical_builds,
    load_build_segments,
    load_transcript,
    transcript_paths,
)
from mbm_eleven import eleven_spoken_text


HERE = os.path.dirname(os.path.abspath(__file__))
SPEAKER_CONST = {
    "narrator": "NARRATOR",
    "jesus": "JESUS",
    "god": "GOD",
    "scripture": "SCRIPTURE",
    "woman": "WOMAN",
}


@dataclass
class Audit:
    row: int
    build: str
    transcript: str
    changed_text: list[str]
    missing_from_build: list[str]
    removed_from_transcript: list[str]
    speaker_mismatch: list[str]
    audio_mismatch: list[str]

    @property
    def differs(self) -> bool:
        return bool(
            self.changed_text
            or self.missing_from_build
            or self.removed_from_transcript
            or self.speaker_mismatch
            or self.audio_mismatch
        )


def _segments_assignment(tree: ast.AST) -> ast.Assign:
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if any(isinstance(target, ast.Name) and target.id == "SEGMENTS" for target in node.targets):
            if not isinstance(node.value, (ast.List, ast.Tuple)):
                raise RuntimeError("SEGMENTS is not a literal list/tuple")
            return node
    raise RuntimeError("SEGMENTS assignment not found")


def _literal_id(node: ast.AST) -> str:
    value = ast.literal_eval(node)
    return str(value)


def audit_row(
    row: int,
    build_dir: str,
    transcript_path: str,
) -> Audit:
    build_segments = load_build_segments(build_dir, executable=sys.executable, strict=True) or []
    transcript_segments = load_transcript(transcript_path)
    build_by_id = {sid: (speaker, text) for sid, speaker, text in build_segments}
    transcript_by_id = {sid: (speaker, text) for sid, speaker, text in transcript_segments}
    audio_mismatch = []
    for sid, _speaker, text in transcript_segments:
        timing_path = os.path.join(build_dir, "audio", f"{sid}.timing.json")
        try:
            timing = json.load(open(timing_path, encoding="utf-8"))
            voiced = " ".join(str(item["text"]) for item in timing)
        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError):
            audio_mismatch.append(sid)
            continue
        normalize = lambda value: re.sub(  # noqa: E731
            r"\s+", " ", re.sub(r"[^a-z ]", "", value.lower())
        ).strip()
        if normalize(voiced) != normalize(eleven_spoken_text(text)):
            audio_mismatch.append(sid)
    return Audit(
        row=row,
        build=build_dir,
        transcript=transcript_path,
        changed_text=[
            sid
            for sid in transcript_by_id.keys() & build_by_id.keys()
            if transcript_by_id[sid][1] != build_by_id[sid][1]
        ],
        missing_from_build=sorted(transcript_by_id.keys() - build_by_id.keys()),
        removed_from_transcript=sorted(build_by_id.keys() - transcript_by_id.keys()),
        speaker_mismatch=[
            sid
            for sid in transcript_by_id.keys() & build_by_id.keys()
            if transcript_by_id[sid][0] != build_by_id[sid][0]
        ],
        audio_mismatch=audio_mismatch,
    )


def rewrite_segments(audit: Audit) -> None:
    path = os.path.join(audit.build, "make_narration.py")
    source = open(path, encoding="utf-8").read()
    tree = ast.parse(source, filename=path)
    assignment = _segments_assignment(tree)
    assert isinstance(assignment.value, (ast.List, ast.Tuple))

    originals: dict[str, ast.Tuple] = {}
    tuple_lengths: set[int] = set()
    for element in assignment.value.elts:
        if not isinstance(element, ast.Tuple) or len(element.elts) < 3:
            raise RuntimeError(f"row {audit.row}: unsupported SEGMENTS element")
        sid = _literal_id(element.elts[0])
        originals[sid] = element
        tuple_lengths.add(len(element.elts))

    transcript = load_transcript(audit.transcript)
    missing = [sid for sid, _speaker, _text in transcript if sid not in originals]
    if missing:
        raise RuntimeError(
            f"row {audit.row}: transcript adds segment(s) absent from build: "
            + ", ".join(missing)
        )

    lines = ["SEGMENTS = ["]
    build_current = {
        sid: speaker
        for sid, speaker, _text in (
            load_build_segments(audit.build, executable=sys.executable, strict=True) or []
        )
    }
    for sid, speaker, text in transcript:
        original = originals[sid]
        parts = [ast.get_source_segment(source, part) for part in original.elts]
        if any(part is None for part in parts):
            raise RuntimeError(f"row {audit.row}: cannot preserve tuple for {sid}")
        current_speaker = build_current[sid]
        if current_speaker != speaker:
            parts[1] = SPEAKER_CONST[speaker]
        text_index = 4 if len(parts) >= 5 else 2
        parts[text_index] = repr(text)
        lines.append("    (" + ", ".join(parts) + "),")
    lines.append("]")
    replacement = "\n".join(lines)

    start = assignment.lineno - 1
    end = assignment.end_lineno
    source_lines = source.splitlines(keepends=True)
    new_source = "".join(source_lines[:start]) + replacement + "\n" + "".join(source_lines[end:])
    compile(new_source, path, "exec")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(new_source)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("rows", nargs="*", type=int)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument(
        "--allow-structural",
        action="store_true",
        help="allow transcript segments to be removed from SEGMENTS",
    )
    args = parser.parse_args()

    builds = canonical_builds(HERE)
    transcripts = transcript_paths(HERE)
    selected = sorted(set(args.rows) if args.rows else set(builds) & set(transcripts))
    changed = applied = skipped = failures = 0
    for row in selected:
        if row not in builds or row not in transcripts:
            print(f"#{row}: missing build or transcript")
            failures += 1
            continue
        try:
            result = audit_row(row, builds[row], transcripts[row])
            if not result.differs:
                continue
            changed += 1
            details = []
            if result.changed_text:
                details.append("text=" + ",".join(sorted(result.changed_text)))
            if result.missing_from_build:
                details.append("new=" + ",".join(result.missing_from_build))
            if result.removed_from_transcript:
                details.append("drop=" + ",".join(result.removed_from_transcript))
            if result.speaker_mismatch:
                details.append("speaker=" + ",".join(sorted(result.speaker_mismatch)))
            if result.audio_mismatch:
                details.append("audio=" + ",".join(sorted(result.audio_mismatch)))
            print(f"#{row:03d} {os.path.basename(result.build)}: {'; '.join(details)}")
            if args.apply:
                if result.audio_mismatch:
                    print(
                        f"  SKIP #{row:03d}: transcript/audio mismatch requires re-voice"
                    )
                    skipped += 1
                    continue
                if (result.missing_from_build or result.removed_from_transcript) and not args.allow_structural:
                    print(
                        f"  SKIP #{row:03d}: structural transcript change requires "
                        "--allow-structural"
                    )
                    skipped += 1
                    continue
                rewrite_segments(result)
                applied += 1
        except Exception as exc:
            failures += 1
            print(f"#{row:03d}: ERROR {exc}", file=sys.stderr)

    if args.apply:
        print(
            f"\n{changed} build script(s) differed; {applied} updated; "
            f"{skipped} skipped; {failures} error(s)"
        )
    else:
        print(f"\n{changed} build script(s) differ; {failures} error(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
