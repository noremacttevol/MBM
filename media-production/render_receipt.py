#!/usr/bin/env python3
"""Content-hash receipts proving which exact inputs produced an MBM MP4.

File timestamps and audio markers have repeatedly lied about render freshness.
A receipt binds the finished MP4 to the bytes of its build code, narration,
timing sidecars, and still assets.  Changing any one of those invalidates it.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone

from corpus import find_main_mp4


RECEIPT = ".render-receipt.json"
VERSION = 1


def _files(build_dir: str) -> list[str]:
    paths: list[str] = []
    uses_shared_still_builder = False
    for name in sorted(os.listdir(build_dir)):
        path = os.path.join(build_dir, name)
        if os.path.isfile(path) and name.endswith(".py"):
            paths.append(path)
            if name == "build.py":
                with open(path, encoding="utf-8") as handle:
                    uses_shared_still_builder = "mbm_still_video" in handle.read()
    if uses_shared_still_builder:
        shared = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "mbm_still_video.py")
        if os.path.isfile(shared):
            paths.append(shared)
    for folder in ("audio", "assets"):
        root = os.path.join(build_dir, folder)
        if not os.path.isdir(root):
            continue
        for current, dirs, names in os.walk(root):
            dirs.sort()
            for name in sorted(names):
                if name.startswith("."):
                    continue
                paths.append(os.path.join(current, name))
    return paths


def _sha256(paths: list[str], root: str) -> str:
    digest = hashlib.sha256()
    for path in paths:
        relative = os.path.relpath(path, root).encode("utf-8")
        digest.update(len(relative).to_bytes(4, "big"))
        digest.update(relative)
        with open(path, "rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    return digest.hexdigest()


def file_sha256(path: str) -> str:
    return _sha256([path], os.path.dirname(path))


def source_sha256(build_dir: str) -> str:
    return _sha256(_files(build_dir), build_dir)


def receipt_path(build_dir: str) -> str:
    return os.path.join(build_dir, RECEIPT)


def record(build_dir: str, mp4: str | None = None) -> dict:
    mp4 = mp4 or find_main_mp4(build_dir)
    if not mp4:
        raise RuntimeError("no finished MP4")
    data = {
        "version": VERSION,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "source_sha256": source_sha256(build_dir),
        "mp4": os.path.basename(mp4),
        "mp4_sha256": file_sha256(mp4),
        "mp4_size": os.path.getsize(mp4),
    }
    path = receipt_path(build_dir)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, sort_keys=True)
        handle.write("\n")
    os.replace(tmp, path)
    return data


def verify(build_dir: str, mp4: str | None = None) -> tuple[bool, str]:
    path = receipt_path(build_dir)
    try:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        return False, "no content-hash render receipt"
    except (OSError, ValueError, TypeError) as exc:
        return False, f"unreadable render receipt: {exc}"
    if data.get("version") != VERSION:
        return False, f"unsupported render receipt version {data.get('version')!r}"
    mp4 = mp4 or find_main_mp4(build_dir)
    if not mp4:
        return False, "receipt exists but finished MP4 is missing"
    if data.get("mp4") != os.path.basename(mp4):
        return False, "finished MP4 filename differs from render receipt"
    if data.get("mp4_size") != os.path.getsize(mp4):
        return False, "finished MP4 size differs from render receipt"
    if data.get("source_sha256") != source_sha256(build_dir):
        return False, "render inputs changed after the MP4 was built"
    if data.get("mp4_sha256") != file_sha256(mp4):
        return False, "finished MP4 bytes differ from render receipt"
    return True, "exact render inputs and MP4 bytes match"
