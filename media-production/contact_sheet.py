#!/usr/bin/env python3
"""
contact_sheet.py — tile one build folder's stills into a single labeled review image.
Lets a reviewer judge a whole story at a glance: quality + whether there are enough
pictures for the beats. Writes <folder>/_review.jpg.

Usage: python3 contact_sheet.py <build-folder> [more folders...]
"""
import os
import sys
import glob
from PIL import Image, ImageDraw, ImageFont

COLS = 4
THUMB_W = 360          # each thumb 360x640 (9:16)
THUMB_H = 640
LABEL_H = 26
PAD = 8
BG = (24, 24, 28)
FG = (235, 235, 235)

try:
    FONT = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    TITLEF = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
except OSError:
    FONT = TITLEF = ImageFont.load_default()


def sheet(folder):
    folder = folder.rstrip("/")
    assets = os.path.join(folder, "assets")
    imgs = sorted(glob.glob(f"{assets}/*.jpeg") + glob.glob(f"{assets}/*.jpg")
                  + glob.glob(f"{assets}/*.png"))
    if not imgs:
        print(f"SKIP {folder}: no stills")
        return None
    n = len(imgs)
    rows = (n + COLS - 1) // COLS
    title_h = 44
    W = COLS * THUMB_W + (COLS + 1) * PAD
    H = title_h + rows * (THUMB_H + LABEL_H + PAD) + PAD
    sheet = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(sheet)
    d.text((PAD, 10), f"{os.path.basename(folder)}   ({n} stills)",
           fill=FG, font=TITLEF)
    for i, p in enumerate(imgs):
        r, c = divmod(i, COLS)
        x = PAD + c * (THUMB_W + PAD)
        y = title_h + r * (THUMB_H + LABEL_H + PAD)
        try:
            im = Image.open(p).convert("RGB")
            im.thumbnail((THUMB_W, THUMB_H))
            ox = x + (THUMB_W - im.width) // 2
            sheet.paste(im, (ox, y))
        except Exception as e:
            d.text((x + 4, y + 4), f"ERR {e}", fill=(255, 80, 80), font=FONT)
        name = os.path.basename(p).rsplit(".", 1)[0]
        d.text((x, y + THUMB_H + 4), name[:34], fill=FG, font=FONT)
    out = os.path.join(folder, "_review.jpg")
    sheet.save(out, quality=82)
    print(f"OK {out}  ({n} stills, {rows}x{COLS})")
    return out


if __name__ == "__main__":
    for f in sys.argv[1:]:
        sheet(f)
