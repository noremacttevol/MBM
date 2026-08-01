#!/usr/bin/env python3
"""Build and enforce per-person face boards for an MBM V2 story.

The image generator cannot prove that a recurring actor stayed the same merely
because every prompt used the same words.  This tool makes the finished face
crops reviewable beside one canonical anchor and records the exact file hashes
that passed.  Replacing either an anchor or a frame invalidates that approval.

Usage:
    python3 v2_identity_board.py BUILD_DIR
    python3 v2_identity_board.py BUILD_DIR --record-pass paralysed-man
    python3 v2_identity_board.py BUILD_DIR --check
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont, ImageOps


CONFIG_NAME = "IDENTITY-QC.json"
TILE_SIZE = (360, 430)
IMAGE_SIZE = (340, 340)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_config(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"missing identity config: {path}") from exc
    if not isinstance(data.get("identities"), dict) or not data["identities"]:
        raise SystemExit(f"{path}: identities must be a non-empty object")
    return data


def resolve(build_dir: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else build_dir / path


def crop_face(image: Image.Image, crop: list[float] | list[int] | None) -> Image.Image:
    if crop is None:
        return image.copy()
    if len(crop) != 4:
        raise ValueError("crop must contain [left, top, right, bottom]")
    if all(isinstance(value, (int, float)) and 0 <= value <= 1 for value in crop):
        left, top, right, bottom = (
            round(crop[0] * image.width),
            round(crop[1] * image.height),
            round(crop[2] * image.width),
            round(crop[3] * image.height),
        )
    else:
        left, top, right, bottom = map(round, crop)
    if not (0 <= left < right <= image.width and 0 <= top < bottom <= image.height):
        raise ValueError(
            f"crop {(left, top, right, bottom)} outside image {image.size}"
        )
    return image.crop((left, top, right, bottom))


def tile(image: Image.Image, label: str, status: str) -> Image.Image:
    canvas = Image.new("RGB", TILE_SIZE, "#151515")
    fitted = ImageOps.contain(image.convert("RGB"), IMAGE_SIZE)
    x = (TILE_SIZE[0] - fitted.width) // 2
    canvas.paste(fitted, (x, 10))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()
    colour = {"PASS": "#63d471", "FAIL": "#ff6767"}.get(status, "#ffd166")
    draw.text((10, 360), status, fill=colour, font=font)
    words = label.replace("-", " ").split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if len(candidate) > 46 and current:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    draw.multiline_text((10, 378), "\n".join(lines[:3]), fill="white", font=font)
    return canvas


def current_status(item: dict[str, Any], frame_hash: str, anchor_hash: str) -> str:
    if item.get("result") == "fail":
        return "FAIL"
    if (
        item.get("result") == "pass"
        and item.get("approved_frame_sha256") == frame_hash
        and item.get("approved_anchor_sha256") == anchor_hash
    ):
        return "PASS"
    return "PENDING"


def build_boards(build_dir: Path, config: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    board_dir = resolve(build_dir, config.get("board_dir", "identity-boards"))
    board_dir.mkdir(parents=True, exist_ok=True)
    asset_dir = resolve(build_dir, config.get("asset_dir", "assets-realistic"))

    for slug, identity in config["identities"].items():
        anchor_path = resolve(build_dir, identity["anchor"])
        if not anchor_path.is_file():
            errors.append(f"{slug}: missing anchor {anchor_path}")
            continue
        anchor_hash = sha256(anchor_path)
        with Image.open(anchor_path) as source:
            anchor = crop_face(source, identity.get("anchor_crop"))
        tiles = [tile(anchor, f"ANCHOR — {anchor_path.name}", "ANCHOR")]

        appearances = identity.get("appearances", [])
        if not appearances:
            errors.append(f"{slug}: no appearances configured")
            continue
        for item in appearances:
            frame_path = asset_dir / item["file"]
            if not frame_path.is_file():
                errors.append(f"{slug}: missing frame {frame_path}")
                continue
            frame_hash = sha256(frame_path)
            try:
                with Image.open(frame_path) as source:
                    face = crop_face(source, item.get("crop"))
            except ValueError as exc:
                errors.append(f"{slug}/{item['file']}: {exc}")
                continue
            status = current_status(item, frame_hash, anchor_hash)
            tiles.append(tile(face, item["file"], status))

        columns = min(5, len(tiles))
        rows = (len(tiles) + columns - 1) // columns
        board = Image.new(
            "RGB", (columns * TILE_SIZE[0], rows * TILE_SIZE[1]), "#080808"
        )
        for index, face_tile in enumerate(tiles):
            board.paste(
                face_tile,
                ((index % columns) * TILE_SIZE[0], (index // columns) * TILE_SIZE[1]),
            )
        board.save(board_dir / f"{slug}.jpg", quality=94, subsampling=0)
    return errors


def record_pass(build_dir: Path, config_path: Path, config: dict[str, Any], slug: str) -> None:
    try:
        identity = config["identities"][slug]
    except KeyError as exc:
        choices = ", ".join(config["identities"])
        raise SystemExit(f"unknown identity {slug!r}; choose: {choices}") from exc
    asset_dir = resolve(build_dir, config.get("asset_dir", "assets-realistic"))
    anchor_path = resolve(build_dir, identity["anchor"])
    anchor_hash = sha256(anchor_path)
    for item in identity.get("appearances", []):
        frame_path = asset_dir / item["file"]
        item["result"] = "pass"
        item["approved_frame_sha256"] = sha256(frame_path)
        item["approved_anchor_sha256"] = anchor_hash
    config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")


def check(config: dict[str, Any], build_dir: Path) -> list[str]:
    failures: list[str] = []
    asset_dir = resolve(build_dir, config.get("asset_dir", "assets-realistic"))
    for slug, identity in config["identities"].items():
        anchor_path = resolve(build_dir, identity["anchor"])
        if not anchor_path.is_file():
            failures.append(f"{slug}: missing anchor")
            continue
        anchor_hash = sha256(anchor_path)
        appearances = identity.get("appearances", [])
        if not appearances:
            failures.append(f"{slug}: no appearances")
        for item in appearances:
            frame_path = asset_dir / item["file"]
            if not frame_path.is_file():
                failures.append(f"{slug}/{item['file']}: missing frame")
                continue
            status = current_status(item, sha256(frame_path), anchor_hash)
            if status != "PASS":
                failures.append(f"{slug}/{item['file']}: {status.lower()}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build_dir", type=Path)
    parser.add_argument("--config", default=CONFIG_NAME)
    parser.add_argument("--record-pass", metavar="IDENTITY")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    build_dir = args.build_dir.resolve()
    config_path = resolve(build_dir, args.config)
    config = load_config(config_path)
    if args.record_pass:
        record_pass(build_dir, config_path, config, args.record_pass)
        config = load_config(config_path)
    board_errors = build_boards(build_dir, config)
    failures = check(config, build_dir) if args.check else []
    for problem in board_errors + failures:
        print(f"FAIL: {problem}")
    if board_errors or failures:
        return 1
    print(f"PASS: identity boards current for {len(config['identities'])} identities")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
