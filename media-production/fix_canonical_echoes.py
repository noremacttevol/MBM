#!/usr/bin/env python3
"""Audit or trim adjacent dialogue echoes in canonical transcript JSON files.

The canonical transcript is the source of truth.  This tool never edits audio,
build scripts, rendered videos, or the app.  By default it only prints proposed
sentence removals.  ``--apply`` updates the JSON and its human-readable TXT twin.
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass

from corpus import normalize_speaker, transcript_paths
from echo_scan import echo_sentences, sentences


HERE = os.path.dirname(os.path.abspath(__file__))


@dataclass(frozen=True)
class Cut:
    segment_id: str
    character_text: str
    sentences: tuple[str, ...]


def cuts_for_segments(segments: list[dict]) -> list[Cut]:
    by_segment: dict[str, dict[str, object]] = {}
    for left, right in zip(segments, segments[1:]):
        left_speaker = normalize_speaker(left["speaker"])
        right_speaker = normalize_speaker(right["speaker"])
        speakers = {left_speaker, right_speaker}
        if "narrator" not in speakers or speakers == {"narrator"}:
            continue
        if left_speaker == "narrator":
            narrator, character = left, right
        else:
            narrator, character = right, left
        bad = echo_sentences(str(character["text"]), str(narrator["text"]))
        if not bad:
            continue
        segment_id = str(narrator["id"])
        entry = by_segment.setdefault(
            segment_id,
            {"character_text": str(character["text"]), "sentences": []},
        )
        for sentence in bad:
            if sentence not in entry["sentences"]:
                entry["sentences"].append(sentence)
    return [
        Cut(
            segment_id=segment_id,
            character_text=str(entry["character_text"]),
            sentences=tuple(str(value) for value in entry["sentences"]),
        )
        for segment_id, entry in by_segment.items()
    ]


def trim_text(text: str, cut_sentences: tuple[str, ...]) -> str:
    unwanted = set(cut_sentences)
    return " ".join(sentence for sentence in sentences(text) if sentence not in unwanted)


def write_transcript(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    text_path = os.path.splitext(path)[0] + ".txt"
    with open(text_path, "w", encoding="utf-8") as handle:
        for index, segment in enumerate(data["segments"]):
            if index:
                handle.write("\n")
            handle.write(
                f"[{normalize_speaker(segment['speaker'])}] {segment['text']}\n"
            )
        handle.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("rows", nargs="*", type=int)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    paths = transcript_paths(HERE)
    selected = sorted(set(args.rows) if args.rows else paths)
    affected = updated = cuts = blocked = errors = 0
    for row in selected:
        path = paths.get(row)
        if not path:
            print(f"#{row:03d}: ERROR no canonical transcript")
            errors += 1
            continue
        try:
            with open(path, encoding="utf-8") as handle:
                data = json.load(handle)
            proposed = cuts_for_segments(data["segments"])
            if not proposed:
                continue
            affected += 1
            print(f"#{row:03d} {os.path.basename(path)}")
            by_id = {str(segment["id"]): segment for segment in data["segments"]}
            row_blocked = False
            for cut in proposed:
                cuts += len(cut.sentences)
                print(f"  narrator[{cut.segment_id}] beside: {cut.character_text}")
                for sentence in cut.sentences:
                    print(f"    CUT: {sentence}")
                replacement = trim_text(str(by_id[cut.segment_id]["text"]), cut.sentences)
                if not replacement:
                    print("    BLOCKED: automatic cut would empty the segment")
                    row_blocked = True
                else:
                    by_id[cut.segment_id]["text"] = replacement
            if row_blocked:
                blocked += 1
                continue
            if args.apply:
                write_transcript(path, data)
                updated += 1
        except Exception as exc:
            print(f"#{row:03d}: ERROR {exc}")
            errors += 1

    if args.apply:
        print(
            f"\n{affected} transcript(s) differed; {updated} updated; "
            f"{cuts} sentence cut(s); {blocked} blocked; {errors} error(s)"
        )
    else:
        print(
            f"\n{affected} transcript(s) would change; {cuts} sentence cut(s); "
            f"{blocked} blocked; {errors} error(s)"
        )
    return 1 if blocked or errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
