#!/usr/bin/env python3
"""probe_flow_viewer.py — hunt for an upscale/quality action in Flow's image viewer.

Read-only UI dump: opens the saved project, clicks the first gallery image to
open the media viewer, prints every visible leaf text (buttons/menus), opens any
kebab (more_vert) menu and prints its items too. Looking for anything named
Upscale / Enhance / 2K / 4K / quality / download-size.
"""
import sys
sys.path.insert(0, "media-production")
import flow_driver as fd
from playwright.sync_api import sync_playwright

LEAVES = """() => [...document.querySelectorAll('*')]
  .filter(e => e.offsetParent !== null && !e.children.length)
  .map(e => (e.innerText||'').trim())
  .filter(t => t && t.length < 70)
  .filter((t,i,a) => a.indexOf(t) === i)"""

CLICK_FIRST_IMG = """() => {
  const img = [...document.querySelectorAll('img')]
    .find(i => i.src.includes('getMediaUrl'));
  if (!img) return false;
  const r = img.getBoundingClientRect();
  return {x: r.x + r.width/2, y: r.y + r.height/2};
}"""

url = fd.CONF.read_text().strip()
with fd.profile_lock(), sync_playwright() as p:
    ctx = fd.launch(p, headless=True)
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_timeout(6000)
    before = set(page.evaluate(LEAVES))
    spot = page.evaluate(CLICK_FIRST_IMG)
    if not spot:
        raise SystemExit("no gallery image")
    page.mouse.click(spot["x"], spot["y"])
    page.wait_for_timeout(2500)
    after = page.evaluate(LEAVES)
    new = [t for t in after if t not in before]
    print("VIEWER-NEW LEAF TEXTS:")
    for t in new:
        print("  -", repr(t))
    # open every kebab/more menu visible and dump what appears
    for icon in ("more_vert", "more_horiz", "download", "high_quality", "4k"):
        added = page.evaluate(
            """(tok) => { const cand=[...document.querySelectorAll('*')]
                 .filter(e=>e.offsetParent!==null && (e.innerText||'').trim()===tok)
                 .map(e=>{const r=e.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2};});
               return cand[0]||null; }""", icon)
        if added:
            base = set(page.evaluate(LEAVES))
            page.mouse.click(added["x"], added["y"])
            page.wait_for_timeout(1500)
            menu = [t for t in page.evaluate(LEAVES) if t not in base]
            print(f"MENU after clicking {icon!r}:")
            for t in menu:
                print("  -", repr(t))
            page.keyboard.press("Escape")
            page.wait_for_timeout(600)
    ctx.close()
