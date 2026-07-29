#!/usr/bin/env python3
"""probe_flow_download.py — download one existing Flow image at 2K and 4K.

Found 2026-07-28: the image viewer's Download menu offers 1K (Original size),
2K (Upscaled) and 4K. flow_driver has always fetched the gallery <img> src,
which is the 1K original — so every Flow still ever delivered was the smallest
variant. This grabs the newest gallery image at 2K and 4K so the quality can be
judged against the API's native 2K on the same content.
"""
import sys
sys.path.insert(0, "media-production")
import flow_driver as fd
from playwright.sync_api import sync_playwright

OUT2 = "media-production-v2/JESUS-V2-REF/flowtest-2k.jpeg"
OUT4 = "media-production-v2/JESUS-V2-REF/flowtest-4k.jpeg"

LEAF_SPOT = """(tok) => { const cand=[...document.querySelectorAll('*')]
  .filter(e=>e.offsetParent!==null && (e.innerText||'').trim()===tok)
  .map(e=>{const r=e.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2};});
  return cand[0]||null; }"""

CLICK_FIRST_IMG = """() => {
  const img = [...document.querySelectorAll('img')]
    .find(i => i.src.includes('getMediaUrl'));
  if (!img) return null;
  const r = img.getBoundingClientRect();
  return {x: r.x + r.width/2, y: r.y + r.height/2};
}"""


def click_leaf(page, tok, wait=1500):
    spot = page.evaluate(LEAF_SPOT, tok)
    if not spot:
        raise SystemExit(f"leaf {tok!r} not found")
    page.mouse.click(spot["x"], spot["y"])
    page.wait_for_timeout(wait)


def grab(page, size_label, out):
    click_leaf(page, "download")
    with page.expect_download(timeout=180000) as dl:
        click_leaf(page, size_label, wait=200)
    d = dl.value
    d.save_as(out)
    print(f"{size_label} -> {out}")


url = fd.CONF.read_text().strip()
with fd.profile_lock(), sync_playwright() as p:
    ctx = fd.launch(p, headless=True)
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_timeout(6000)
    spot = page.evaluate(CLICK_FIRST_IMG)
    if not spot:
        raise SystemExit("no gallery image")
    page.mouse.click(spot["x"], spot["y"])
    page.wait_for_timeout(2500)
    import sys as _s
    want = _s.argv[1] if len(_s.argv) > 1 else "2K"
    grab(page, want, OUT2 if want == "2K" else OUT4)
    ctx.close()
print("done")
