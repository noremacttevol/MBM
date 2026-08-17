#!/usr/bin/env python3
"""Inspect one or more QC images with the local Ollama vision model.

This is the headless equivalent of opening an extracted video frame. It keeps
the evidence local and prints the model's literal inspection so an unattended
worker cannot claim that it viewed a frame without sending the actual pixels
to a vision-capable model.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


DEFAULT_URL = "http://127.0.0.1:11434/api/chat"
DEFAULT_MODEL = "qwen3.5:27b"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ask the local Ollama vision model to inspect QC images."
    )
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument(
        "--prompt",
        required=True,
        help="Concrete visual question; quote the complaint when applicable.",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("MBM_LOCAL_VISION_MODEL", DEFAULT_MODEL),
    )
    parser.add_argument(
        "--url", default=os.environ.get("MBM_OLLAMA_CHAT_URL", DEFAULT_URL)
    )
    parser.add_argument("--timeout", type=int, default=600)
    return parser.parse_args()


def encode_image(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(path)
    mime, _ = mimetypes.guess_type(path.name)
    if mime not in {"image/jpeg", "image/png", "image/webp"}:
        raise ValueError(f"unsupported image type for {path}: {mime or 'unknown'}")
    return base64.b64encode(path.read_bytes()).decode("ascii")


def main() -> int:
    args = parse_args()
    try:
        images = [encode_image(path) for path in args.images]
    except (FileNotFoundError, OSError, ValueError) as exc:
        print(f"offline vision input error: {exc}", file=sys.stderr)
        return 2

    names = ", ".join(path.name for path in args.images)
    prompt = (
        "You are performing strict visual quality control on MBM narrated-still "
        "video evidence. Inspect the actual attached pixels; do not infer from a "
        "filename or prompt. State PASS or FAIL first, then list only what is "
        "visibly present. Read visible caption text exactly when relevant. If an "
        "important detail is too small or unclear, say UNCLEAR rather than "
        f"guessing. Files: {names}. QC question: {args.prompt}"
    )
    payload = {
        "model": args.model,
        "stream": False,
        "think": False,
        "messages": [{"role": "user", "content": prompt, "images": images}],
        "options": {"temperature": 0},
    }
    request = urllib.request.Request(
        args.url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            result = json.load(response)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"offline vision request failed: {exc}", file=sys.stderr)
        return 1

    answer = result.get("message", {}).get("content", "").strip()
    if not answer:
        print("offline vision request failed: Ollama returned no answer", file=sys.stderr)
        return 1
    print(f"OFFLINE VISION — {args.model} — {names}")
    print(answer)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
