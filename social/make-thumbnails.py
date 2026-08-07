#!/usr/bin/env python3
"""Build branded thumbnails for every approved video — zero API cost.

Run from the repo root:  python3 social/make-thumbnails.py  [--force]

Why frames, not fresh AI images: the approved cuts already contain the approved
art with the locked faces. Generating new pictures would cost API money and risk
face drift that would have to pass the whole gate again. So every thumbnail is a
frame FROM the cut Cameron approved, plus clean title + app branding on top.

For each row in social/postable.json:
  social/thumbs/yt/row-NNN.jpg        1280x720 (YouTube regular uploads)
  social/thumbs/vertical/row-NNN.jpg  1080x1920 (TikTok / Instagram Reel covers)

Typography matches the videos themselves: DejaVu Serif Bold for the story title
(the scripture-caption serif) and Jost Bold (the production caption font) for the
small app line. Design is reverent: frame, title, quiet brand line. No clickbait.

New approvals: refresh-postable.py first (new covers), then rerun this script —
it only builds what's missing unless --force.
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

SERIF = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
JOST = 'media-production-v2/Jost-Bold.ttf'
BRAND = 'MILK BEFORE MEAT'
BRAND2 = 'free app · milkb4meat.org'
CREAM = (245, 234, 210)
WHITE = (255, 255, 255)

FORCE = '--force' in sys.argv


def fit_lines(draw, text, font_path, max_w, start_px, min_px=30, max_lines=2):
    """Largest font size whose wrapped text fits max_w in <= max_lines lines."""
    size = start_px
    while size >= min_px:
        font = ImageFont.truetype(font_path, size)
        words, lines, cur = text.split(), [], ''
        for w in words:
            t = (cur + ' ' + w).strip()
            if draw.textlength(t, font=font) <= max_w:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        if len(lines) <= max_lines and all(
                draw.textlength(l, font=font) <= max_w for l in lines):
            return font, lines
        size -= 4
    font = ImageFont.truetype(font_path, min_px)
    return font, [text]


def gradient(w, h, top_alpha, bottom_alpha):
    g = Image.new('L', (1, h))
    for y in range(h):
        a = top_alpha + (bottom_alpha - top_alpha) * y / max(1, h - 1)
        g.putpixel((0, y), int(a))
    return g.resize((w, h))


def draw_block(img, title, x, base_w, anchor_bottom, title_px):
    """Title + brand block, bottom-aligned at anchor_bottom. Returns top y used."""
    d = ImageDraw.Draw(img)
    tfont, tlines = fit_lines(d, title, SERIF, base_w, title_px)
    bfont = ImageFont.truetype(JOST, max(22, title_px * 4 // 13))
    b2font = ImageFont.truetype(JOST, max(18, title_px * 3 // 13))
    lh = int(tfont.size * 1.18)
    y = anchor_bottom
    y -= b2font.size + 6
    b2y = y
    y -= bfont.size + 10
    by = y
    y -= lh * len(tlines) + 14
    ty = y
    yy = ty
    for line in tlines:
        d.text((x + 2, yy + 2), line, font=tfont, fill=(0, 0, 0, 160))
        d.text((x, yy), line, font=tfont, fill=WHITE)
        yy += lh
    d.text((x, by), BRAND, font=bfont, fill=CREAM)
    d.text((x, b2y), BRAND2, font=b2font, fill=(200, 195, 180))
    return ty


def make_yt(cover, title, out):
    src = Image.open(cover).convert('RGB')
    W, H = src.size                      # 1080x1920
    ch = int(W * 9 / 16)                 # 607 — 16:9 crop window
    y0 = int(H * 0.20)                   # face zone; above the caption band
    img = src.crop((0, y0, W, y0 + ch)).resize((1280, 720), Image.LANCZOS)
    band_h = 300
    g = gradient(1280, band_h, 0, 215)
    black = Image.new('RGB', (1280, band_h), (0, 0, 0))
    img.paste(Image.composite(black, img.crop((0, 720 - band_h, 1280, 720)), g),
              (0, 720 - band_h))
    draw_block(img, title, 46, 1280 - 92, 720 - 34, 78)
    img.save(out, quality=91)


def make_vertical(cover, title, out):
    img = Image.open(cover).convert('RGB')   # keep full frame incl. its caption
    band_h = 560
    g = gradient(1080, band_h, 225, 0)
    black = Image.new('RGB', (1080, band_h), (0, 0, 0))
    img.paste(Image.composite(black, img.crop((0, 0, 1080, band_h)), g), (0, 0))
    d = ImageDraw.Draw(img)
    tfont, tlines = fit_lines(d, title, SERIF, 1080 - 120, 88)
    bfont = ImageFont.truetype(JOST, 34)
    b2font = ImageFont.truetype(JOST, 26)
    y = 64
    for line in tlines:
        w = d.textlength(line, font=tfont)
        x = (1080 - w) // 2
        d.text((x + 2, y + 2), line, font=tfont, fill=(0, 0, 0, 160))
        d.text((x, y), line, font=tfont, fill=WHITE)
        y += int(tfont.size * 1.18)
    y += 10
    w = d.textlength(BRAND, font=bfont)
    d.text(((1080 - w) // 2, y), BRAND, font=bfont, fill=CREAM)
    y += 44
    w = d.textlength(BRAND2, font=b2font)
    d.text(((1080 - w) // 2, y), BRAND2, font=b2font, fill=(210, 205, 190))
    img.save(out, quality=90)


def main():
    os.makedirs('social/thumbs/yt', exist_ok=True)
    os.makedirs('social/thumbs/vertical', exist_ok=True)
    rows = json.load(open('social/postable.json'))['postable']
    built = skipped = 0
    for p in rows:
        n = p['row']
        title = p['title']
        cover = p['cover']
        if not os.path.exists(cover):
            print(f'  !! row {n}: cover missing ({cover}) — run refresh-postable.py')
            continue
        yt = f'social/thumbs/yt/row-{n:03d}.jpg'
        vt = f'social/thumbs/vertical/row-{n:03d}.jpg'
        if FORCE or not os.path.exists(yt):
            make_yt(cover, title, yt)
            built += 1
        else:
            skipped += 1
        if FORCE or not os.path.exists(vt):
            make_vertical(cover, title, vt)
            built += 1
        else:
            skipped += 1
    print(f'thumbnails built: {built}, already existed: {skipped}')


if __name__ == '__main__':
    main()
