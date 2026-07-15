#!/usr/bin/env python3
"""flow_driver.py — drive Google Flow with NO Claude Chrome extension (2026-07-15).

Why: the Claude-in-Chrome extension connection kept flaking across machines and
stalling production. This driver uses Playwright against a dedicated persistent
Chrome profile (~/.mbm-flow-profile). Cameron logs into Google ONCE per machine in
that profile; after that every session generates Flow stills deterministically from
the command line — no extension, no screenshots, almost no model tokens.

Commands:
  python3 flow_driver.py open
      Opens the profile's Chrome at Flow. FIRST TIME: Cameron logs into his Google
      (Ultra) account in this window, then just closes it (or waits — the command
      detects login). Also auto-creates/saves a working project URL.
  python3 flow_driver.py check
      One-line status: logged in? project saved? ready?
  python3 flow_driver.py gen --prompt "FULL prompt text" --out assets/s1-slug.jpeg
                             [--ref path.jpeg ...]
      Generates ONE image in the saved project and saves the jpeg to --out.
      --ref attaches reference image(s) (character lock / master face).
      Settings note: the project remembers Image · Nano Banana 2 · 9:16 · 1x once
      set. `gen` verifies the chip says "Nano Banana 2" and "0 credits" appears;
      it sets 9:16/1x via the chip popup when needed.

Money law: this drives Cameron's FLOW (Ultra, 0 credits for Nano Banana 2 images).
It never touches the paid Gemini API.
"""
import argparse
import base64
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

PROFILE = Path.home() / ".mbm-flow-profile"
CONF = Path.home() / ".mbm-flow-project"
FLOW = "https://labs.google/fx/tools/flow"

NAMES_JS = """() => [...document.querySelectorAll('img')]
  .filter(i => i.src.includes('getMediaUrl'))
  .map(i => new URL(i.src).searchParams.get('name'))"""

FETCH_JS = """async (name) => {
  const img = [...document.querySelectorAll('img')]
    .find(i => i.src.includes(name));
  if (!img) return null;
  const b = await (await fetch(img.src)).blob();
  const fr = new FileReader();
  return await new Promise(r => { fr.onload = () => r(fr.result); fr.readAsDataURL(b); });
}"""


def launch(p, headless=False):
    return p.chromium.launch_persistent_context(
        str(PROFILE), channel="chrome", headless=headless, no_viewport=True,
        args=["--disable-blink-features=AutomationControlled",
              "--window-size=1440,900"])


def logged_in(page):
    page.goto(FLOW, wait_until="domcontentloaded")
    page.wait_for_timeout(3000)
    # landing page always shows the CTA; a logged-in click lands on the dashboard
    try:
        page.get_by_text("Create with Google Flow").first.click(timeout=8000)
    except PWTimeout:
        pass
    page.wait_for_timeout(5000)
    if "accounts.google.com" in page.url:
        return False
    try:
        page.get_by_text("New project").first.wait_for(timeout=10000)
        return True
    except PWTimeout:
        return "/project/" in page.url


def ensure_project(page):
    if CONF.exists():
        url = CONF.read_text().strip()
        if url:
            return url
    page.get_by_text("New project").first.click(timeout=15000)
    page.wait_for_url("**/project/**", timeout=30000)
    url = page.url
    CONF.write_text(url)
    return url


def cmd_open():
    with sync_playwright() as p:
        ctx = launch(p)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(FLOW, wait_until="domcontentloaded")
        print("Chrome window is open. If you see a sign-in, LOG INTO GOOGLE now.")
        print("Waiting up to 10 minutes for login...")
        for _ in range(60):
            time.sleep(10)
            try:
                if logged_in(page):
                    url = ensure_project(page)
                    print(f"LOGGED IN. Project saved: {url}")
                    ctx.close()
                    return
            except Exception:
                pass
        print("Timed out waiting for login. Run `open` again after logging in.")
        ctx.close()


def cmd_check():
    with sync_playwright() as p:
        ctx = launch(p, headless=True)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        ok = logged_in(page)
        proj = CONF.read_text().strip() if CONF.exists() else ""
        ctx.close()
    print(f"logged_in={bool(ok)} project={'saved' if proj else 'MISSING'}")
    sys.exit(0 if ok and proj else 1)


def ensure_settings(page):
    """Verify Nano Banana 2 / 0 credits; set Image·9:16·1x via the chip if needed."""
    chip = page.locator('button:has-text("Nano Banana 2")').first
    try:
        chip.wait_for(timeout=8000)
    except PWTimeout:
        raise SystemExit("Settings chip not found — open the project once with "
                         "`flow_driver.py open` and set Image · Nano Banana 2 · "
                         "9:16 · 1x in the prompt bar.")
    chip.click()
    page.wait_for_timeout(1200)
    for label in ("Image", "9:16", "1x"):
        try:
            page.get_by_text(label, exact=True).locator("visible=true").first.click(timeout=3000)
            page.wait_for_timeout(400)
        except PWTimeout:
            pass
    body = page.inner_text("body")
    # Flow credits are PREPAID and expire monthly (Cameron, 2026-07-15): spending
    # them is fine and often smart. Just say what this generation costs.
    import re as _re
    m = _re.search(r"use ([\d,]+) credits?|0 credits", body)
    print(f"  credit cost: {m.group(0) if m else 'unknown'}")
    page.keyboard.press("Escape")
    page.wait_for_timeout(500)


def cmd_gen(prompt, out, refs):
    url = CONF.read_text().strip() if CONF.exists() else ""
    if not url:
        raise SystemExit("No saved project. Run: flow_driver.py open")
    prompt = " ".join(prompt.split())  # ONE line — Enter submits
    with sync_playwright() as p:
        # HEADED on purpose: Cameron can watch it work, and Flow behaves like a
        # normal browser. Headless hid everything and stalled (2026-07-15 lesson).
        ctx = launch(p, headless=False)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(6000)
        if "accounts.google.com" in page.url:
            raise SystemExit("Not logged in — run: flow_driver.py open")
        try:  # settings are best-effort — defaults still generate; never block on UI
            ensure_settings(page)
        except Exception as e:
            print(f"  (settings skipped: {e})")

        before = page.evaluate(NAMES_JS) or []
        for ref in refs or []:
            # "add Add Media" button opens a file chooser for reference images
            try:
                with page.expect_file_chooser(timeout=6000) as fc:
                    page.evaluate(
                        "() => [...document.querySelectorAll('button')]"
                        ".find(b => (b.innerText||'').includes('Add Media'))"
                        "?.click()")
                fc.value.set_files(ref)
                page.wait_for_timeout(2500)
            except Exception:
                print(f"  (warning: could not attach ref {ref} — generating without)")
        # Focus via JS, then REAL keyboard input (CDP insertText) — value-setter
        # injection filled the box visually but React never registered it and
        # Create submitted nothing (2026-07-15). Real input events work.
        # the real prompt box is a VISIBLE textarea or contenteditable div — the
        # first textarea in the DOM is a hidden decoy (found 2026-07-15)
        ok = page.evaluate(
            "() => {"
            " const els = [...document.querySelectorAll("
            "   'textarea, [contenteditable=\\'true\\']')]"
            "   .filter(e => e.offsetParent !== null);"
            " if (!els.length) return 'no-visible-promptbox';"
            " const el = els[els.length - 1];"
            " el.focus(); window.__mbmBox = el; return el.tagName; }")
        if ok == "no-visible-promptbox":
            raise SystemExit("prompt focus failed: no visible prompt box")
        print(f"  prompt box: {ok}")
        page.keyboard.insert_text(prompt)
        page.wait_for_timeout(800)
        got = page.evaluate(
            "() => (window.__mbmBox.value ?? window.__mbmBox.innerText ?? '').length")
        print(f"  prompt in box: {got} chars")
        if not got:
            raise SystemExit("prompt box still empty after insert_text")
        clicked = page.evaluate(
            "() => {"
            " const b = [...document.querySelectorAll('button')]"
            "   .find(b => (b.innerText||'').includes('arrow_forward'));"
            " if (!b) return 'no-button';"
            " b.click(); return 'ok'; }")
        if clicked != "ok":
            raise SystemExit(f"create click failed: {clicked}")
        print("  submitted, waiting for the image...")

        newest = None
        for i in range(36):  # up to 3 min
            page.wait_for_timeout(5000)
            names = page.evaluate(NAMES_JS) or []
            fresh = [n for n in names if n not in before]
            if fresh:
                newest = fresh[0]
                break
            if i % 4 == 3:  # gallery is virtualized — nudge thumbnails to mount
                try:
                    page.evaluate("() => [...document.querySelectorAll('button')]"
                                  ".find(b => (b.innerText||'').includes('All Media'))"
                                  "?.click()")
                    page.mouse.wheel(0, 600)
                except Exception:
                    pass
        if not newest:
            raise SystemExit("No new image appeared within 3 minutes.")
        page.wait_for_timeout(2000)
        data = page.evaluate(FETCH_JS, newest)
        ctx.close()
    if not data or "," not in data:
        raise SystemExit("Download failed (empty data URL).")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_bytes(base64.b64decode(data.split(",", 1)[1]))
    print(f"saved {out} ({Path(out).stat().st_size // 1024} KB)")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("open")
    sub.add_parser("check")
    g = sub.add_parser("gen")
    g.add_argument("--prompt", required=True)
    g.add_argument("--out", required=True)
    g.add_argument("--ref", action="append", default=[])
    a = ap.parse_args()
    if a.cmd == "open":
        cmd_open()
    elif a.cmd == "check":
        cmd_check()
    else:
        cmd_gen(a.prompt, a.out, a.ref)


if __name__ == "__main__":
    main()
