#!/usr/bin/env python3
"""Claim one MBM row on both coordination boards before local work starts."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
AUTHOR_BOARD = ROOT / "media-production-v2" / "AUTHOR-BOARD.md"
QUEUE = ROOT / "media-production" / "QUEUE.md"

JOB_LABELS = {
    "cfix": "C-FIX",
    "resume": "RESUME",
    "audio": "AUDIO-FIX",
    "verify": "QC-VERIFY",
    "runner": "A-auto",
    "author": "AUTHOR-LIVE",
}


def claim_line(line: str, row: int, cell_index: int, marker: str) -> tuple[str, bool]:
    if not re.match(rf"\|\s*{row}\s*\|", line):
        return line, False
    cells = line.rstrip("\n").split("|")
    if len(cells) <= cell_index:
        raise RuntimeError(f"row {row}: malformed coordination row")
    claim = cells[cell_index].strip()
    if marker in claim:
        return line, True

    # An unresolved LIVE marker means another worker owns the row. Historical
    # SHIPPED/PARK/DONE notes do not contain LIVE in the normal board grammar.
    live = re.search(
        r"(?:C-FIX|RESUME|AUDIO-FIX|QC-VERIFY|A-auto|AUTHOR-LIVE)"
        r"[^|]{0,180}\bLIVE\b",
        claim,
    )
    if live:
        raise RuntimeError(f"row {row} is already claimed: {live.group(0).strip()}")

    cells[cell_index] = f" {claim} · {marker} " if claim else f" {marker} "
    return "|".join(cells) + "\n", True


def update(path: Path, row: int, cell_index: int, marker: str) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    found = False
    changed = False
    output: list[str] = []
    for line in lines:
        new_line, matched = claim_line(line, row, cell_index, marker)
        if matched:
            if found:
                raise RuntimeError(f"row {row} appears more than once in {path}")
            found = True
            changed = changed or new_line != line
        output.append(new_line)
    if not found:
        raise RuntimeError(f"row {row} not found in {path}")
    if changed:
        path.write_text("".join(output), encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("job", choices=sorted(JOB_LABELS))
    parser.add_argument("row", type=int)
    args = parser.parse_args()

    marker = (
        f"{JOB_LABELS[args.job]} {date.today().isoformat()} OFFLINE LIVE "
        "(Machine A `Dev`)"
    )
    # split('|') retains an empty item before the first pipe: AUTHOR Claim is
    # index 6; QUEUE Claim/notes is index 8.
    author_changed = update(AUTHOR_BOARD, args.row, 6, marker)
    queue_changed = update(QUEUE, args.row, 8, marker)
    state = "written" if author_changed or queue_changed else "already present"
    print(f"row {args.row} offline claim {state}: {marker}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
