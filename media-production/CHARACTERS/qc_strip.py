#!/usr/bin/env python3
"""qc_strip.py — one QC image per character: the three views side by side,
plus a zoomed face crop of the three-quarter and full-body so identity drift
is visible at a glance. Writes <slug>/_qc.jpg (never committed as approval —
it is a working QC aid; the contact sheet for Cameron is separate).

Usage: python3 CHARACTERS/qc_strip.py <slug> [...]
"""
import sys
from pathlib import Path

from PIL import Image

CH = Path(__file__).resolve().parent
H = 640


def load(p, height=H):
    im = Image.open(p)
    w = int(im.width * height / im.height)
    return im.resize((w, height))


def face_crop(p, height=H):
    im = Image.open(p)
    w, h = im.size
    c = im.crop((int(w * .20), int(h * .02), int(w * .80), int(h * .42)))
    nw = int(c.width * height / c.height)
    return c.resize((nw, height))


def strip(slug):
    d = CH / slug
    views = [d / "face-front.jpeg", d / "three-quarter.jpeg", d / "full-body.jpeg"]
    if not all(v.exists() for v in views):
        print(f"{slug}: missing views — skip")
        return
    tiles = [load(views[0]), load(views[1]), load(views[2]),
             face_crop(views[1]), face_crop(views[2])]
    w = sum(t.width for t in tiles) + 8 * (len(tiles) + 1)
    out = Image.new("RGB", (w, H + 16), (24, 24, 28))
    x = 8
    for t in tiles:
        out.paste(t, (x, 8))
        x += t.width + 8
    out.save(d / "_qc.jpg", quality=82)
    print(f"{slug}: _qc.jpg written")


if __name__ == "__main__":
    for s in sys.argv[1:]:
        strip(s)
