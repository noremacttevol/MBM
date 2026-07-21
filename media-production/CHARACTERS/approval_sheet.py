#!/usr/bin/env python3
"""approval_sheet.py — labeled master contact sheets Cameron approves from.

Each character cell: face-front + three-quarter + full-body side by side with
the character's name underneath. Writes CHARACTERS/_approval-1.jpg (NT) and
_approval-2.jpg (OT) plus the same grid as one big _approval-all.jpg.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

CH = Path(__file__).resolve().parent
TH = 300           # thumb height
COLS = 3           # characters per row
PAD = 10
LABEL = 34
BG = (24, 24, 28)
FG = (240, 240, 240)

try:
    FONT = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
except OSError:
    FONT = ImageFont.load_default()

NT = ["god-the-father", "young-jesus", "peter", "john-beloved", "james",
      "andrew", "matthew", "thomas", "judas-iscariot", "john-the-baptist",
      "mary-mother-of-jesus", "joseph-of-nazareth", "mary-magdalene",
      "martha", "mary-of-bethany", "lazarus", "zacchaeus", "nicodemus",
      "pilate", "stephen", "paul", "bartimaeus", "jairus", "cleopas",
      "barabbas", "zebedee", "malchus", "simon-the-pharisee"]
OT = ["adam", "eve", "noah", "abraham", "sarah", "isaac", "jacob",
      "joseph-of-egypt", "moses", "aaron", "joshua", "elijah", "elisha",
      "eli", "samuel", "hannah", "david", "ruth", "naomi", "boaz", "job",
      "jonah", "daniel", "shadrach", "meshach", "abednego",
      "nebuchadnezzar", "naaman", "isaiah", "jeremiah", "ezekiel", "hosea",
      "gomer", "joel", "malachi"]


def cell(slug):
    ims = []
    for v in ["face-front", "three-quarter", "full-body"]:
        p = CH / slug / f"{v}.jpeg"
        im = Image.open(p)
        ims.append(im.resize((int(im.width * TH / im.height), TH)))
    w = sum(i.width for i in ims) + PAD * 2
    c = Image.new("RGB", (w, TH + LABEL), BG)
    x = 0
    for i in ims:
        c.paste(i, (x, 0))
        x += i.width + PAD
    d = ImageDraw.Draw(c)
    d.text((6, TH + 5), slug.replace("-", " ").upper(), font=FONT, fill=FG)
    return c


def sheet(slugs, out):
    cells = [cell(s) for s in slugs]
    cw = max(c.width for c in cells)
    chh = TH + LABEL
    rows = (len(cells) + COLS - 1) // COLS
    W = COLS * (cw + PAD) + PAD
    H = rows * (chh + PAD) + PAD
    im = Image.new("RGB", (W, H), BG)
    for i, c in enumerate(cells):
        r, col = divmod(i, COLS)
        im.paste(c, (PAD + col * (cw + PAD), PAD + r * (chh + PAD)))
    im.save(CH / out, quality=80)
    print(out, im.size)


if __name__ == "__main__":
    sheet(NT, "_approval-1-NT.jpg")
    sheet(OT, "_approval-2-OT.jpg")
