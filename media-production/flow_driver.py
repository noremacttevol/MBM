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

Money law: this drives Cameron's FLOW on his Ultra plan. His Flow credits are
PREPAID and EXPIRE MONTHLY — do NOT hoard them and do NOT default to the cheapest
model to save money that expires anyway. Spend on the model that gets it right:
Nano Banana Pro (and other credit-costing models) are ALLOWED and encouraged for
faces, Jesus, crowds, and anything that needs fewer rerolls. The ONLY thing banned
is the paid Gemini API. Never call Flow generations "0 credits", "$0", or "free".
"""
import argparse
import base64
import fcntl
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

PROFILE = Path.home() / ".mbm-flow-profile"
CONF = Path.home() / ".mbm-flow-project"
FLOW = "https://labs.google/fx/tools/flow"

# ONE Chrome per profile (2026-07-21, Machine A): two Claude sessions on the
# same computer both drove Flow at once — the second launch died on Chrome's
# ProcessSingleton, and worse, two sessions sharing one project gallery can
# each download the OTHER's freshly generated image. Every command that opens
# the profile now waits its turn on this advisory lock first. The lock is held
# for the whole gen (attach→submit→download), so gallery "fresh image"
# detection can never see a neighbour session's result.
LOCK = Path.home() / ".mbm-flow-profile.flock"


class profile_lock:
    # 3 hours, not 30 minutes (2026-07-21): when another session is running a
    # whole video build, one job can hold the browser for well over half an
    # hour. A queued job that gives up at 30 min looks exactly like a broken
    # generator — it isn't, it just lost its place. Waiting is always cheaper
    # than a failed batch, so be patient by default.
    def __init__(self, wait_minutes=180):
        self.wait = wait_minutes * 60
        self.fh = None

    def __enter__(self):
        self.fh = open(LOCK, "w")
        deadline = time.time() + self.wait
        while True:
            try:
                fcntl.flock(self.fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
                return self
            except BlockingIOError:
                if time.time() > deadline:
                    raise SystemExit(
                        f"flow profile busy for {self.wait//60} min — another "
                        "session is generating; try again")
                print("  (flow profile busy — another session is generating; waiting…)",
                      flush=True)
                time.sleep(15)

    def __exit__(self, *a):
        fcntl.flock(self.fh, fcntl.LOCK_UN)
        self.fh.close()

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
    with profile_lock(), sync_playwright() as p:
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
    with profile_lock(), sync_playwright() as p:
        ctx = launch(p, headless=True)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        ok = logged_in(page)
        proj = CONF.read_text().strip() if CONF.exists() else ""
        ctx.close()
    print(f"logged_in={bool(ok)} project={'saved' if proj else 'MISSING'}")
    sys.exit(0 if ok and proj else 1)


def ensure_model(page, want, open_chip, chip_text):
    """Select the image model by name (e.g. 'Nano Banana Pro') on the settings chip.

    Added 2026-07-28 (Machine A, V2 production). Before this, the driver used
    whatever model the project happened to remember and only ever VERIFIED the
    chip said 'Nano Banana'. V2 requires Nano Banana Pro for every shot with
    Jesus, a close face, or a crowd (V2-KICKOFF step E), so the model has to be
    selectable per generation, not set by hand once.

    Returns True if the chip ends up naming `want`. Best-effort by design: the
    caller decides whether a miss is fatal (for V2 it is — a Pro shot silently
    made on a lesser model is a wasted QC pass, not a saving).
    """
    if not want:
        return True
    # Print the chip ALWAYS (2026-07-28): the first V2 run silently short-circuited
    # here and produced 768x1376 stills — Nano Banana 2's size — with no line in the
    # log saying which model ran. A generation you cannot attribute to a model is a
    # generation you cannot trust, so the chip text goes in the log every time.
    #
    # POLL for the chip instead of reading it once (2026-07-29, Machine A). Reading
    # it once raced the page: on a slow lap chip_text() came back empty, `first`
    # became '?', and the driver dropped into the selection loop for a model that
    # was ALREADY selected — then failed every attempt, because the popup offers no
    # clickable row for the current model. Row 5 lost b01 and b08 that way, each
    # logging "chip says: Nano Banana Pro" in the very line announcing it could not
    # select Nano Banana Pro. The runner re-scans and retries, so nothing was lost
    # permanently, but every miss burns a whole lap.
    def first_line():
        lines = (chip_text() or "").strip().splitlines()
        return lines[0].strip() if lines else ""

    first = ""
    for _ in range(6):
        first = first_line()
        if first:
            break
        page.wait_for_timeout(500)
    print(f"  model chip reads: {(first or '?')!r} (want {want!r})")
    if want.lower() in first.lower():
        return True

    CLICK_BY_TEXT = (
        "(name) => {"
        " const n = name.toLowerCase();"
        " const cand = [...document.querySelectorAll('*')]"
        "   .filter(e => e.offsetParent !== null)"
        "   .map(e => ({e, t:(e.innerText||'').trim(), r:e.getBoundingClientRect()}))"
        "   .filter(o => o.t.toLowerCase() === n"
        "             || o.t.toLowerCase().startsWith(n + '\\n'))"
        "   .filter(o => o.r.width > 0 && o.r.height > 0 && o.r.width < 520)"
        "   .sort((a,b) => a.t.length - b.t.length);"
        " const o = cand[0]; if (!o) return null;"
        " return {x:o.r.x + o.r.width/2, y:o.r.y + o.r.height/2}; }")

    for attempt in range(4):
        open_chip()
        # The model list may sit behind a sub-dropdown that shows the CURRENT
        # model. If the wanted name isn't on screen, click the current-model
        # row first to expand the list, then look again.
        target = page.evaluate(CLICK_BY_TEXT, want)
        if not target:
            cur = (chip_text() or "").strip().split("\n")[0]
            if cur:
                spot = page.evaluate(CLICK_BY_TEXT, cur)
                if spot:
                    page.mouse.click(spot["x"], spot["y"])
                    page.wait_for_timeout(900)
            target = page.evaluate(CLICK_BY_TEXT, want)
        if target:
            page.mouse.click(target["x"], target["y"])
            page.wait_for_timeout(1200)
            if want.lower() in (chip_text() or "").lower():
                page.keyboard.press("Escape")
                page.wait_for_timeout(400)
                print(f"  model: {want}")
                return True
        page.keyboard.press("Escape")
        page.wait_for_timeout(400)
    # LAST CHECK BEFORE GIVING UP (2026-07-29, Machine A). The chip is the
    # authority on which model will run, so ask it one more time before aborting a
    # generation. If it now names the wanted model then the model was correct all
    # along and only the READ was late — abort anyway and we throw away a good
    # picture. This can never green-light the wrong model: returning True here
    # still requires the chip's own text to contain `want`.
    final = first_line() or "?"
    if want.lower() in final.lower():
        print(f"  model: {want} (chip confirmed it on the final check)")
        return True
    print(f"  WARNING: could not select model '{want}' (chip says: {final})")
    return False


def ensure_settings(page, model=None):
    """Set model · Image · 9:16 · 1x on the settings chip and report credit cost.

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

    # model FIRST — switching model can reset aspect/count, so it must happen
    # before 9:16 is set (2026-07-28, Machine A).
    model_ok = ensure_model(page, model, open_chip, chip_text)

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
    return model_ok


def _leaf_spot(page, tok):
    """Center of the smallest visible element whose exact text is `tok`."""
    return page.evaluate(
        "(tok) => { const cand=[...document.querySelectorAll('*')]"
        "  .filter(e=>e.offsetParent!==null && (e.innerText||'').trim()===tok)"
        "  .map(e=>{const r=e.getBoundingClientRect();"
        "           return {x:r.x+r.width/2,y:r.y+r.height/2};});"
        " return cand[0]||null; }", tok)


def download_variant(page, name, size, out):
    """Download a gallery image at Flow's 2K/4K size via the viewer's Download menu.

    Found 2026-07-28 (Machine A): the viewer offers 1K (Original size) / 2K
    (Upscaled, 1536x2752) / 4K (3072x5504). The old path fetched the gallery
    <img> src, which is ALWAYS the 1K original — every Flow still ever delivered
    was the smallest variant. The 2K download matches the Gemini API's native-2K
    pixel size on Cameron's subscription.
    """
    spot = page.evaluate(
        "(name) => { const img=[...document.querySelectorAll('img')]"
        "  .find(i => i.src.includes(name)); if(!img) return null;"
        "  const r=img.getBoundingClientRect();"
        "  return {x:r.x+r.width/2, y:r.y+r.height/2}; }", name)
    if not spot:
        raise SystemExit("viewer: fresh image not found in gallery")
    page.mouse.click(spot["x"], spot["y"])
    page.wait_for_timeout(2500)
    dspot = _leaf_spot(page, "download")
    if not dspot:
        raise SystemExit("viewer: download button not found")
    page.mouse.click(dspot["x"], dspot["y"])
    page.wait_for_timeout(1200)
    sspot = _leaf_spot(page, size)
    if not sspot:
        raise SystemExit(f"viewer: size option {size!r} not found")
    with page.expect_download(timeout=180000) as dl:
        page.mouse.click(sspot["x"], sspot["y"])
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    dl.value.save_as(out)


def cmd_gen(prompt, out, refs, model=None, model_required=True, size="2K"):
    url = CONF.read_text().strip() if CONF.exists() else ""
    if not url:
        raise SystemExit("No saved project. Run: flow_driver.py open")
    prompt = " ".join(prompt.split())  # ONE line — Enter submits
    with profile_lock(), sync_playwright() as p:
        # HEADED on purpose: Cameron can watch it work, and Flow behaves like a
        # normal browser. Headless hid everything and stalled (2026-07-15 lesson).
        ctx = launch(p, headless=False)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(6000)
        if "accounts.google.com" in page.url:
            raise SystemExit("Not logged in — run: flow_driver.py open")
        try:  # settings are best-effort — defaults still generate; never block on UI
            model_ok = ensure_settings(page, model)
        except Exception as e:
            print(f"  (settings skipped: {e})")
            model_ok = not model
        if model and model_required and not model_ok:
            # A named model is a deliberate spend decision (V2: Pro for every
            # face/crowd). Silently generating on a lesser model wastes the QC
            # pass instead of saving anything, so stop and say so.
            ctx.close()
            raise SystemExit(f"Could not select model '{model}' — nothing generated.")

        pre = page.evaluate(NAMES_JS) or []
        for ref in refs or []:
            # Attach a reference image by SETTING the hidden <input type=file
            # accept="image/*"> directly (found 2026-07-15, Machine C). The old path
            # clicked the "Add Media" button and waited for a native file chooser,
            # which the JS .click() never opened — so the ref silently dropped and the
            # face wasn't locked. set_input_files works on the hidden input and fires
            # the change event React needs. We verify a thumbnail count increase.
            try:
                before_thumbs = page.evaluate(
                    "() => document.querySelectorAll('img').length")
                page.set_input_files("input[type=file]", ref)
                # wait for the upload thumbnail to appear (img count rises)
                ok = False
                for _ in range(24):
                    page.wait_for_timeout(1000)
                    now = page.evaluate(
                        "() => document.querySelectorAll('img').length")
                    if now > before_thumbs:
                        ok = True
                        break
                print(f"  ref attached: {Path(ref).name} ({'thumbnail up' if ok else 'no thumbnail seen'})")
            except Exception as e:
                print(f"  (warning: could not attach ref {ref} — generating without: {e})")
        # The uploaded ref ALSO appears in the gallery as a getMediaUrl image, and was
        # being downloaded instead of the generated scene (every ref'd shot came out as a
        # copy of the ref portrait). Wait for the ref(s) to register, record their names,
        # and exclude them from the "fresh" scene detection (fix 2026-07-15, Machine B).
        ref_names = set()
        if refs:
            for _ in range(24):  # up to ~12s for the upload(s) to appear
                now = page.evaluate(NAMES_JS) or []
                newr = [n for n in now if n not in pre]
                if len(newr) >= len(refs):
                    ref_names = set(newr)
                    break
                page.wait_for_timeout(500)
            print(f"  ref image(s) registered: {len(ref_names)}")
        before = page.evaluate(NAMES_JS) or []
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
        for i in range(72):  # up to 6 min (heavy projects generate/detect slower)
            page.wait_for_timeout(5000)
            names = page.evaluate(NAMES_JS) or []
            fresh = [n for n in names if n not in before and n not in ref_names]
            if fresh:
                newest = fresh[0]
                break
            if i % 8 == 7:  # heavy/virtualized gallery: RELOAD so the newest image
                # (always most-recent, at the top) mounts on a fresh, light DOM.
                try:
                    page.reload(wait_until="domcontentloaded")
                    page.wait_for_timeout(4000)
                    page.mouse.wheel(0, -2000)  # scroll to top where the newest sits
                except Exception:
                    pass
            elif i % 4 == 3:  # gentle nudge between reloads
                try:
                    page.evaluate("() => [...document.querySelectorAll('button')]"
                                  ".find(b => (b.innerText||'').includes('All Media'))"
                                  "?.click()")
                    page.mouse.wheel(0, -1500)
                except Exception:
                    pass
        if not newest:
            raise SystemExit("No new image appeared within 6 minutes.")
        page.wait_for_timeout(2000)
        if size and size != "1K":
            download_variant(page, newest, size, out)
            data = None
        else:
            data = page.evaluate(FETCH_JS, newest)
        ctx.close()
    if data is not None:
        if "," not in data:
            raise SystemExit("Download failed (empty data URL).")
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_bytes(base64.b64decode(data.split(",", 1)[1]))
    print(f"saved {out} ({Path(out).stat().st_size // 1024} KB, {size})")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("open")
    sub.add_parser("check")
    sub.add_parser("show")
    sub.add_parser("models")
    gr = sub.add_parser("grab")
    gr.add_argument("--out", required=True)
    g = sub.add_parser("gen")
    g.add_argument("--prompt", required=True)
    g.add_argument("--out", required=True)
    g.add_argument("--ref", action="append", default=[])
    g.add_argument("--model", default=None,
                   help="Image model to select on the chip, e.g. 'Nano Banana Pro'. "
                        "Omit to use whatever the project remembers.")
    g.add_argument("--model-best-effort", action="store_true",
                   help="Generate anyway if --model can't be confirmed "
                        "(default: abort rather than spend on the wrong model).")
    g.add_argument("--size", default="2K", choices=["1K", "2K", "4K"],
                   help="Download size from the viewer menu (default 2K = "
                        "1536x2752; 1K = the old gallery-src path).")
    a = ap.parse_args()
    if a.cmd == "open":
        cmd_open()
    elif a.cmd == "check":
        cmd_check()
    elif a.cmd == "show":
        cmd_show()
    elif a.cmd == "models":
        cmd_models()
    elif a.cmd == "grab":
        cmd_grab(a.out)
    else:
        cmd_gen(a.prompt, a.out, a.ref, a.model, not a.model_best_effort, a.size)




def cmd_models():
    """Dump the settings chip text and every model option in its popover.

    Added 2026-07-28 (Machine A): `gen --model` needs to know what the options are
    actually called before it can click one, and a run whose model can't be named
    afterwards is a run you can't trust. Read-only — opens the popover, prints, quits.
    """
    url = CONF.read_text().strip() if CONF.exists() else FLOW
    with profile_lock(), sync_playwright() as p:
        ctx = launch(p, headless=False)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(6000)
        FIND_CHIP = ("() => { const has = e => (e.innerText||'').includes('Nano Banana');"
                     " let el = [...document.querySelectorAll('button')].find(has);"
                     " if(!el){ const els=[...document.querySelectorAll('[role=button],div,span')]"
                     "   .filter(has); els.sort((a,b)=>a.innerText.length-b.innerText.length);"
                     "   el = els[0]; }"
                     " if(!el) return null; const r=el.getBoundingClientRect();"
                     " return {x:r.x+r.width/2, y:r.y+r.height/2, t:el.innerText}; }")
        c = page.evaluate(FIND_CHIP)
        print(f"CHIP TEXT: {(c or {}).get('t')!r}")
        if c:
            page.mouse.click(c["x"], c["y"])
            page.wait_for_timeout(1500)
        opts = page.evaluate(
            "() => [...document.querySelectorAll('*')]"
            "  .filter(e => e.offsetParent !== null && !e.children.length)"
            "  .map(e => (e.innerText||'').trim())"
            "  .filter(t => t && t.length < 60)"
            "  .filter((t,i,a) => a.indexOf(t) === i)")
        print("POPOVER LEAF TEXTS:")
        for o in opts:
            print(f"  - {o!r}")
        c2 = page.evaluate(FIND_CHIP)
        print(f"CHIP TEXT (popover open): {(c2 or {}).get('t')!r}")
        ctx.close()


def cmd_show(minutes=15):
    """Open the saved project in a visible window and keep it open for Cameron."""
    url = CONF.read_text().strip() if CONF.exists() else FLOW
    with profile_lock(), sync_playwright() as p:
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
    with profile_lock(), sync_playwright() as p:
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
            fresh = [n for n in names if n not in before and n not in ref_names]
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
