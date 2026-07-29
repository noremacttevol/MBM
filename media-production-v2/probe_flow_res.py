#!/usr/bin/env python3
"""probe_flow_res.py — does Flow store images bigger than the gallery serves?

2026-07-28, Machine A. Cameron's order: "I need the same quality from Flow."
The driver saves whatever URL the gallery <img> carries (getMediaUrl?...). Many
Google image CDNs serve a SIZED-DOWN variant in the DOM and accept size params
for the original. If the stored original is >=1536 wide, Flow can deliver the
same 2K quality the API does, on the subscription. Read-only: fetches existing
gallery images at several URL variants and reports decoded dimensions.
"""
import sys
sys.path.insert(0, "media-production")
import flow_driver as fd
from playwright.sync_api import sync_playwright

MEASURE = """async (src) => {
  try {
    const r = await fetch(src);
    const b = await r.blob();
    const bmp = await createImageBitmap(b);
    return {ok: true, w: bmp.width, h: bmp.height, bytes: b.size,
            type: b.type, status: r.status};
  } catch (e) { return {ok: false, err: String(e)}; }
}"""

def variants(src):
    from urllib.parse import urlsplit, parse_qsl, urlencode, urlunsplit
    parts = urlsplit(src)
    q = dict(parse_qsl(parts.query))
    out = [("as-served", src)]
    for wh in ((2048, 3671), (4096, 7342)):
        q2 = dict(q); q2["width"] = str(wh[0]); q2["height"] = str(wh[1])
        out.append((f"width={wh[0]}", urlunsplit(parts._replace(query=urlencode(q2)))))
    q3 = {k: v for k, v in q.items() if k.lower() not in ("width", "height", "w", "h", "sz")}
    out.append(("no-size-params", urlunsplit(parts._replace(query=urlencode(q3)))))
    return out

url = fd.CONF.read_text().strip()
with fd.profile_lock(), sync_playwright() as p:
    ctx = fd.launch(p, headless=True)
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_timeout(6000)
    srcs = page.evaluate("""() => [...document.querySelectorAll('img')]
        .filter(i => i.src.includes('getMediaUrl')).map(i => i.src)""")
    print(f"gallery getMediaUrl images: {len(srcs)}")
    if not srcs:
        raise SystemExit("no gallery images found")
    src = srcs[0]
    print("sample query:", src.split("?", 1)[1][:220] if "?" in src else "(no query)")
    for label, u in variants(src):
        r = page.evaluate(MEASURE, u)
        print(f"  {label:<16} -> {r}")
    ctx.close()
