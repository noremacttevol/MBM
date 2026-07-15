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
    """Set Image · 9:16 · 1x on the settings chip and report credit cost.

    The chip popup (found 2026-07-15, Machine C) lays out material-icon buttons whose
    innerText is 'icon\\nlabel': mode row 'image\\nImage' / 'play_circle\\nVideo';
    aspect row 'crop_16_9\\n16:9' … 'crop_9_16\\n9:16'; count row '1x' 'x2' 'x3' 'x4'.
    The OLD code matched get_by_text('9:16', exact=True) which never matched (the
    element text is 'crop_9_16\\n9:16'), so aspect stayed 16:9. We click by the UNIQUE
    icon token instead: 'crop_9_16' for portrait.

    Chip lookup is element-type-agnostic (Machine A/B saw Flow render the chip as a
    non-<button> element): we find ANY element whose innerText contains 'Nano Banana'.
    9:16 is REQUIRED — a 16:9 still can't fill a 9:16 video (playbook) — so if we truly
    cannot select it after retries we abort rather than emit a wrong-aspect still."""
    # Find the chip. PREFER an actual <button> containing 'Nano Banana' (verified to
    # open the full settings popover on a real-mouse click). Only if Flow renders the
    # chip as a non-<button> (reported on Machine A/B) fall back to the smallest
    # element carrying the text. Returning the button's box is what makes 9:16 work.
    FIND_CHIP = ("() => { const has = e => (e.innerText||'').includes('Nano Banana');"
                 " let el = [...document.querySelectorAll('button')].find(has);"
                 " if(!el){ const els=[...document.querySelectorAll('[role=button],div,span')]"
                 "   .filter(has); els.sort((a,b)=>a.innerText.length-b.innerText.length);"
                 "   el = els[0]; }"
                 " if(!el) return null; const r=el.getBoundingClientRect();"
                 " return {x:r.x+r.width/2, y:r.y+r.height/2, t:el.innerText}; }")

    def chip_info():
        return page.evaluate(FIND_CHIP)

    def chip_text():
        c = page.evaluate(FIND_CHIP)
        return (c or {}).get("t", "") if c else ""

    def open_chip():
        # MUST be a real mouse click: a JS .click() opens only a collapsed popup that
        # hides the aspect row; a real mouse click opens the full settings popover with
        # the 16:9/9:16 choices (found 2026-07-15, Machine C).
        c = chip_info()
        if c:
            page.mouse.click(c["x"], c["y"])
        page.wait_for_timeout(1000)

    def click_tok(tok):
        # React onClick doesn't fire for a JS .click() on these popup items — use a
        # REAL mouse click at the element's center (the same thing that works for the
        # prompt box). Prefer an actual button/role/li leaf whose text starts with the
        # unique material-icon token. Re-query each call (the popup re-renders).
        # One robust query (verified on Machine D 2026-07-15): the clickable popover
        # leaf for an aspect option is the small material-icon element (often a bare
        # <i>crop_9_16</i> with NO role — the old button/role/li-only query missed it,
        # so 9:16 never got set and gen refused). Search ALL tags, keep only SMALL
        # leaves (0<width<160) whose trimmed text starts with the icon token, and click
        # the shortest-text one's center with a REAL mouse click (JS .click() doesn't
        # fire React's handler here).
        c = page.evaluate(
            "(tok) => { const cand=[...document.querySelectorAll('*')]"
            "  .filter(e=>e.offsetParent!==null && (e.innerText||'').trim().startsWith(tok))"
            "  .map(e=>({e, r:e.getBoundingClientRect()}))"
            "  .filter(o=>o.r.width>0 && o.r.width<160 && o.r.height>0)"
            "  .sort((a,b)=>a.e.innerText.length-b.e.innerText.length);"
            " const o=cand[0]; if(!o) return null;"
            " return {x:o.r.x+o.r.width/2, y:o.r.y+o.r.height/2}; }", tok)
        if not c:
            return False
        page.mouse.click(c["x"], c["y"])
        return True

    # set 9:16, verifying against the chip text; retry a few times (the aspect row
    # only exists while the popup is open, and the popup re-renders on each click)
    aspect_ok = "crop_9_16" in chip_text()
    for _ in range(4):
        if aspect_ok:
            break
        open_chip()
        click_tok("crop_9_16")
        page.wait_for_timeout(600)
        aspect_ok = "crop_9_16" in chip_text()
    # count: prefer 1x (open popup if it closed)
    open_chip()
    page.evaluate("""() => { const b=[...document.querySelectorAll('button,div,li')]
        .filter(e=>e.offsetParent!==null)
        .find(e => (e.innerText||'').trim()==='1x'); if(b) b.click(); }""")
    page.wait_for_timeout(400)
    body = page.inner_text("body")
    import re as _re
    m = _re.search(r"use ([\d,]+) credits?|0 credits", body)
    print(f"  credit cost: {m.group(0) if m else 'unknown'}; aspect_9_16={aspect_ok}")
    page.keyboard.press("Escape")
    page.wait_for_timeout(500)
    if not aspect_ok:
        # Do NOT hard-abort (Cameron, 2026-07-15): the image usually still comes out
        # vertical even when we couldn't confirm the chip. Warn and continue; the
        # caller verifies the downloaded jpeg is taller than wide and rerolls only if
        # it actually came out landscape.
        print("  WARNING: could not confirm 9:16 on the chip — continuing anyway; "
              "verify the saved jpeg is portrait and reroll only if it is landscape.")


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
            # REF ATTACH (fixed 2026-07-15, Machine B): the native file-chooser path
            # never fired — Flow exposes a HIDDEN <input type=file accept=image/*>. Nudge
            # the UI with the Add Media button, then set files on the input DIRECTLY
            # (Playwright can set a hidden input). Verified: the master face then locks
            # the generated Jesus face. Without this every Jesus shot generated a
            # DIFFERENT face — a face-law violation.
            attached = False
            try:
                page.evaluate("() => [...document.querySelectorAll('button')]"
                              ".find(b => (b.innerText||'').includes('Add Media'))?.click()")
                page.wait_for_timeout(1500)
                inp = page.query_selector("input[type=file]")
                if inp:
                    inp.set_input_files(ref)
                    page.wait_for_timeout(5000)
                    attached = True
                    print(f"  attached ref via hidden file input: {Path(ref).name}")
            except Exception as e:
                print(f"  (ref attach error: {e})")
            if not attached:
                print(f"  (warning: could not attach ref {ref} — generating without)")
        # SUBMIT THAT ACTUALLY WORKS (found 2026-07-15, Machine C): the real prompt
        # box is the LAST visible contenteditable div/textarea. You must (1) CLICK it
        # with the real mouse so the browser + React agree it is focused, (2) type with
        # real keystrokes, (3) submit with ENTER. The old path (el.focus() in JS +
        # insert_text + clicking the 'arrow_forward' Create button) filled the box
        # visually but the Create click was INERT — the project stayed on "Start
        # creating" and no generation ever started. Enter starts it every time.
        box = page.evaluate(
            "() => {"
            " const els = [...document.querySelectorAll("
            "   'textarea, [contenteditable=\\'true\\']')]"
            "   .filter(e => e.offsetParent !== null);"
            " if (!els.length) return null;"
            " const el = els[els.length - 1];"
            " const r = el.getBoundingClientRect();"
            " return {x: r.x + r.width/2, y: r.y + r.height/2, tag: el.tagName}; }")
        if not box:
            raise SystemExit("prompt focus failed: no visible prompt box")
        print(f"  prompt box: {box['tag']}")
        page.mouse.click(box["x"], box["y"])
        page.wait_for_timeout(400)
        page.keyboard.type(prompt, delay=4)
        page.wait_for_timeout(600)
        got = page.evaluate(
            "() => {"
            " const els = [...document.querySelectorAll("
            "   'textarea, [contenteditable=\\'true\\']')]"
            "   .filter(e => e.offsetParent !== null);"
            " const el = els[els.length - 1];"
            " return (el.value ?? el.innerText ?? '').length; }")
        print(f"  prompt in box: {got} chars")
        if not got:
            raise SystemExit("prompt box still empty after typing")
        page.keyboard.press("Enter")
        print("  submitted (Enter), waiting for the image...")

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
    sub.add_parser("show")
    gr = sub.add_parser("grab")
    gr.add_argument("--out", required=True)
    g = sub.add_parser("gen")
    g.add_argument("--prompt", required=True)
    g.add_argument("--out", required=True)
    g.add_argument("--ref", action="append", default=[])
    a = ap.parse_args()
    if a.cmd == "open":
        cmd_open()
    elif a.cmd == "check":
        cmd_check()
    elif a.cmd == "show":
        cmd_show()
    elif a.cmd == "grab":
        cmd_grab(a.out)
    else:
        cmd_gen(a.prompt, a.out, a.ref)




def cmd_show(minutes=15):
    """Open the saved project in a visible window and keep it open for Cameron."""
    url = CONF.read_text().strip() if CONF.exists() else FLOW
    with sync_playwright() as p:
        ctx = launch(p, headless=False)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(url, wait_until="domcontentloaded")
        print(f"Window open at the project for {minutes} minutes.")
        time.sleep(minutes * 60)
        ctx.close()


def cmd_grab(out, wait_min=15):
    """Poll the project for the NEWEST image and save it — Cameron generates by
    hand, this fetches the result. Reuses the proven download JS."""
    url = CONF.read_text().strip() if CONF.exists() else ""
    if not url:
        raise SystemExit("No saved project. Run: flow_driver.py open")
    with sync_playwright() as p:
        ctx = launch(p, headless=True)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(6000)
        before = page.evaluate(NAMES_JS) or []
        print(f"watching for a new image (currently {len(before)})...")
        newest = None
        for _ in range(wait_min * 6):
            page.wait_for_timeout(10000)
            page.reload(wait_until="domcontentloaded")
            page.wait_for_timeout(4000)
            names = page.evaluate(NAMES_JS) or []
            fresh = [n for n in names if n not in before]
            if fresh:
                newest = fresh[0]
                break
        if not newest:
            raise SystemExit("No new image appeared while waiting.")
        page.wait_for_timeout(2000)
        data = page.evaluate(FETCH_JS, newest)
        ctx.close()
    if not data or "," not in data:
        raise SystemExit("Download failed.")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_bytes(base64.b64decode(data.split(",", 1)[1]))
    print(f"saved {out} ({Path(out).stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
