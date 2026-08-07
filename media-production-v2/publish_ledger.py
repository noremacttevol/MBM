#!/usr/bin/env python3
"""publish_ledger.py — THE PUBLISH LOOP (Cameron, 2026-08-06).

One tool that manages what is APPROVED and what is PUBLISHED, with versions,
and shows what is posted where. The repo is the memory; every change commits
to GitHub so the whole history tracks.

THE VERSION RULE (Cameron's words, 2026-08-06):
  A published video is a NEW STAGE of the most recent cut. The first time a
  row's realistic-v2 cut goes live anywhere it becomes v2.1. If it must be
  fixed or changed later, the fixed re-publish becomes v2.2 — and v2.1 stays
  in the ledger forever as the first that got published. Nothing is ever
  overwritten in history; the ledger only appends.

  Major version:  2 = realistic-v2 rebuild era (the current wave)
                  1 = legacy cut (cartoon/old-voice era — REDO-ALL pending)
  Minor version:  counts publishes of that major. v2.1 first publish,
                  v2.2 first fix re-publish, and so on.

THE LOOP (every row walks this cycle; the board shows where each row stands):
  BUILT (on reviewer) -> APPROVED (Cameron says good) -> PUBLISHED vN.1
    -> [complaint / fix ordered] -> REBUILT -> RE-APPROVED -> PUBLISHED vN.2
  Each arrow is a git commit, so GitHub is the audit trail.

WHERE THE TRUTH COMES FROM (derived from real files, never from checkboxes):
  - site/review.html            card hash + wave = the current cut on review
  - media-production/approvals.json  row -> {hash, date} = Cameron's approvals
  - media-production-v2/build-*/     the actual mp4 cuts (content sha1)
  - site/story-videos/<N>.mp4        what is actually LIVE on the app gallery
  - mobile/src/data/videos.ts        PRODUCED_VIDEO_IDS = rows the app lists

COMMANDS:
  sync   [--commit] [--push]   recompute everything, auto-record any gallery
                               publish that happened, regenerate the board
  status [N]                   print the loop state (one row or summary)
  history N                    full version history of one row
  approve N                    stamp Cameron's approval of row N's current cut
  publish N --platform P [--url U] [--note T]
                               record a publish (external platforms too);
                               bumps the minor version if the cut changed
  fix N --reason "..."         open a fix on a published row (the live version
                               stays on record as the first published)
  fix N --close                close the fix without a re-publish

Stdlib only. State of record: PUBLISH-LEDGER.json (append-only versions).
Human board: PUBLISH-BOARD.md (generated — never hand-edit).
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import date, datetime

HERE = os.path.dirname(os.path.abspath(__file__))          # media-production-v2
REPO = os.path.dirname(HERE)                               # MBM repo root

LEDGER_PATH    = os.path.join(HERE, "PUBLISH-LEDGER.json")
BOARD_PATH     = os.path.join(HERE, "PUBLISH-BOARD.md")
CACHE_PATH     = os.path.join(HERE, ".hash-cache.json")
REVIEW_HTML    = os.path.join(REPO, "site", "review.html")
APPROVALS_JSON = os.path.join(REPO, "media-production", "approvals.json")
QUEUE_MD       = os.path.join(REPO, "media-production", "QUEUE.md")
GALLERY_DIR    = os.path.join(REPO, "site", "story-videos")
VIDEOS_TS      = os.path.join(REPO, "mobile", "src", "data", "videos.ts")
GALLERY_URL    = "https://milk-b4-meat.web.app/story-videos"

TODAY = date.today().isoformat()


# ---------------------------------------------------------------- hashing ----

def _load_cache():
    try:
        with open(CACHE_PATH) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _save_cache(cache):
    with open(CACHE_PATH, "w") as f:
        json.dump(cache, f)


_CACHE = _load_cache()
_CACHE_DIRTY = False


def sha1_of(path):
    """Content sha1 of a file, cached on (size, mtime) so the loop stays fast."""
    global _CACHE_DIRTY
    try:
        st = os.stat(path)
    except OSError:
        return None
    key = os.path.relpath(path, REPO)
    hit = _CACHE.get(key)
    if hit and hit["size"] == st.st_size and hit["mtime"] == st.st_mtime:
        return hit["sha1"]
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    digest = h.hexdigest()
    _CACHE[key] = {"size": st.st_size, "mtime": st.st_mtime, "sha1": digest}
    _CACHE_DIRTY = True
    return digest


# ---------------------------------------------------------------- sources ----

def parse_review():
    """review.html cards -> {row: {card_hash, wave, built, title, src_file}}."""
    cards = {}
    try:
        with open(REVIEW_HTML, encoding="utf-8") as f:
            html = f.read()
    except OSError:
        return cards
    chunks = re.split(r'(?=<div class="card")', html)
    for chunk in chunks[1:]:
        m = re.search(r'data-num="(\d+)"', chunk)
        if not m:
            continue
        num = int(m.group(1))
        hash_m  = re.search(r'data-hash="([0-9a-f]{6,40})"', chunk)
        wave_m  = re.search(r'data-review-wave="([^"]*)"', chunk)
        built_m = re.search(r'data-built="([^"]*)"', chunk)
        title_m = re.search(r'<p class="title">\d+\s*[—-]\s*([^<]+)', chunk)
        src_m   = re.search(r'src="[^"]*/([^/"?]+\.mp4)', chunk)
        path_m  = re.search(r'src="[^"]*raw/main/([^"?]+\.mp4)', chunk)
        cards[num] = {
            "card_hash": hash_m.group(1) if hash_m else None,
            "wave":      wave_m.group(1) if wave_m else None,
            "built":     built_m.group(1) if built_m else None,
            "title":     title_m.group(1).strip() if title_m else None,
            "src_file":  src_m.group(1) if src_m else None,
            "src_path":  path_m.group(1) if path_m else None,
        }
    return cards


def parse_queue():
    """QUEUE.md 'The 200' rows -> {row: {title, ref}} (titles only — ticks are
    not trusted; the ledger derives state from real files)."""
    rows = {}
    try:
        with open(QUEUE_MD, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return rows
    for m in re.finditer(
        r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", text, re.M
    ):
        num = int(m.group(1))
        if num not in rows:                       # first table wins (The 200)
            rows[num] = {"title": m.group(2).strip(), "ref": m.group(3).strip()}
    return rows


def parse_approvals():
    """LIVE reviewer approvals — the store Cameron's approve button writes,
    via admin/dump-approvals.mjs. THIS is the authority (2026-08-06 lesson:
    the local approvals.json is a stale partial copy — trusting it published
    6 rows when Cameron had approved 41). Falls back to the local file only
    if the dump fails, and says so loudly."""
    try:
        r = subprocess.run(
            ["node", os.path.join(REPO, "admin", "dump-approvals.mjs")],
            capture_output=True, timeout=120)
        if r.returncode == 0:
            raw = json.loads(r.stdout)
            return {
                k: {"hash": v.get("approvedHash"),
                    "date": (v.get("approvedAt") or "")[:10]}
                for k, v in raw.items() if v.get("approved")
            }
        sys.stderr.write("WARNING: dump-approvals.mjs failed (rc=%d) — "
                         "falling back to STALE approvals.json\n" % r.returncode)
    except (OSError, ValueError, subprocess.TimeoutExpired) as e:
        sys.stderr.write("WARNING: live approval dump unavailable (%s) — "
                         "falling back to STALE approvals.json\n" % e)
    try:
        with open(APPROVALS_JSON) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def approved_bytes_sha1(appr_hash, src_path):
    """sha1 of the actual APPROVED cut's bytes, resolved from git objects
    (never the working tree — autopilot rewrites working-tree mp4s).
    approvedHash is either the mp4's git blob hash or a shipping commit hash;
    in the commit case the card's repo path locates the blob."""
    global _CACHE_DIRTY
    if not appr_hash or len(appr_hash) < 40:
        return None
    key = "obj:%s:%s" % (appr_hash, src_path or "")
    hit = _CACHE.get(key)
    if hit:
        return hit["sha1"]
    t = subprocess.run(["git", "-C", REPO, "cat-file", "-t", appr_hash],
                       capture_output=True)
    otype = t.stdout.decode().strip() if t.returncode == 0 else None
    spec = None
    if otype == "blob":
        spec = appr_hash
    elif otype == "commit" and src_path:
        spec = "%s:%s" % (appr_hash, src_path)
    if not spec:
        return None
    r = subprocess.run(["git", "-C", REPO, "cat-file", "blob", spec],
                       capture_output=True)
    if r.returncode != 0:
        return None
    digest = hashlib.sha1(r.stdout).hexdigest()
    _CACHE[key] = {"size": len(r.stdout), "mtime": 0, "sha1": digest}
    _CACHE_DIRTY = True
    return digest


def parse_app_ids():
    """PRODUCED_VIDEO_IDS from videos.ts — the rows the app actually lists."""
    try:
        with open(VIDEOS_TS, encoding="utf-8") as f:
            ts = f.read()
    except OSError:
        return set()
    m = re.search(r"PRODUCED_VIDEO_IDS\s*=\s*new Set<number>\(\[(.*?)\]\)", ts, re.S)
    if not m:
        return set()
    return {int(n) for n in re.findall(r"\d+", m.group(1))}


def find_builds():
    """media-production-v2/build-NN-* -> {row: {slug, mp4s: {name: path}}}."""
    builds = {}
    for entry in sorted(os.listdir(HERE)):
        m = re.match(r"build-(\d+)-", entry)
        if not m:
            continue
        folder = os.path.join(HERE, entry)
        if not os.path.isdir(folder):
            continue
        mp4s = {
            name: os.path.join(folder, name)
            for name in os.listdir(folder)
            if name.endswith(".mp4")
        }
        builds[int(m.group(1))] = {"slug": entry, "mp4s": mp4s}
    return builds


# ----------------------------------------------------------------- ledger ----

def load_ledger():
    try:
        with open(LEDGER_PATH) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {"rows": {}, "updated": None}


def save_ledger(ledger):
    ledger["updated"] = datetime.now().isoformat(timespec="seconds")
    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, sort_keys=True)
        f.write("\n")
    if _CACHE_DIRTY:
        _save_cache(_CACHE)


def _row(ledger, num):
    return ledger["rows"].setdefault(
        str(num), {"slug": None, "title": None, "open_fix": None, "versions": []}
    )


def _major_of(version):
    return int(version.split(".")[0])


def _next_version(row, major):
    minors = [
        int(v["version"].split(".")[1])
        for v in row["versions"]
        if _major_of(v["version"]) == major
    ]
    return "%d.%d" % (major, (max(minors) + 1) if minors else 1)


def _live_event(row):
    """Most recent version event that is on the app gallery."""
    for ev in reversed(row["versions"]):
        if any(w["platform"] == "app-gallery" for w in ev["where"]):
            return ev
    return None


def _last_event(row):
    return row["versions"][-1] if row["versions"] else None


# ------------------------------------------------------------- world scan ----

def scan():
    """Assemble the real state of every row from files on disk."""
    cards     = parse_review()
    queue     = parse_queue()
    approvals = parse_approvals()
    app_ids   = parse_app_ids()
    builds    = find_builds()

    nums = sorted(set(queue) | set(cards) | set(builds))
    world = {}
    for num in nums:
        card  = cards.get(num, {})
        build = builds.get(num)

        # The current cut = the file the reviewer card streams; fall back to
        # the newest root mp4 in the build folder.
        cut_path = cut_sha = None
        build_sha1s = set()
        if build:
            for path in build["mp4s"].values():
                s = sha1_of(path)
                if s:
                    build_sha1s.add(s)
            src = card.get("src_file")
            if src and src in build["mp4s"]:
                cut_path = build["mp4s"][src]
            elif build["mp4s"]:
                cut_path = max(build["mp4s"].values(), key=os.path.getmtime)
            if cut_path:
                cut_sha = sha1_of(cut_path)

        gallery_path = os.path.join(GALLERY_DIR, "%d.mp4" % num)
        gallery_sha = sha1_of(gallery_path) if os.path.exists(gallery_path) else None

        appr = approvals.get(str(num))
        # Publish-ready = Cameron's live approval stamps the CURRENT reviewer
        # cut. His approval is the authority, whatever era the cut is — an
        # approval on an older card hash means the cut changed since he said
        # yes, so the new cut awaits him.
        approved_current = bool(
            appr and card.get("card_hash") and appr.get("hash") == card["card_hash"]
        )
        appr_sha = (approved_bytes_sha1(appr.get("hash"), card.get("src_path"))
                    if approved_current else None)

        world[num] = {
            "title": (card.get("title") or (queue.get(num) or {}).get("title")
                      or "row %d" % num),
            "ref": (queue.get(num) or {}).get("ref", ""),
            "slug": build["slug"] if build else None,
            "wave": card.get("wave"),
            "card_hash": card.get("card_hash"),
            "built_date": card.get("built"),
            "cut_path": cut_path,
            "cut_sha": cut_sha,
            "build_sha1s": build_sha1s,
            "gallery_sha": gallery_sha,
            "gallery_mtime": (os.path.getmtime(gallery_path)
                              if gallery_sha else None),
            "approved": bool(appr),
            "approved_current": approved_current,
            "approved_date": appr.get("date") if appr else None,
            "approved_sha1": appr_sha,
            "in_app": num in app_ids,
        }
    return world


# ------------------------------------------------------------------ sync -----

def do_sync(commit=False, push=False):
    ledger = load_ledger()
    world = scan()
    events = []

    for num, w in world.items():
        row = _row(ledger, num)
        row["slug"] = w["slug"] or row["slug"]
        row["title"] = w["title"] or row["title"]

        if not w["gallery_sha"]:
            continue

        live = _live_event(row)
        if live and live["sha1"] == w["gallery_sha"]:
            continue  # gallery unchanged since last recorded publish

        # The gallery file changed (or was never recorded) — append a version.
        # Major 2 = the live bytes ARE an approved cut (byte-verified against
        # git objects) or a current v2 build; major 1 = legacy/unapproved.
        major = 2 if (w["gallery_sha"] == w["approved_sha1"]
                      or w["gallery_sha"] in w["build_sha1s"]) else 1
        version = _next_version(row, major)
        seeded = live is None and not row["versions"]
        ev_date = TODAY
        note = "auto-detected: gallery file changed"
        if seeded and w["gallery_mtime"]:
            ev_date = date.fromtimestamp(w["gallery_mtime"]).isoformat()
            note = ("seeded from live gallery file (date = file mtime); "
                    + ("realistic-v2 cut" if major == 2
                       else "legacy cut — REDO-ALL pending"))
        ev = {
            "version": version,
            "sha1": w["gallery_sha"],
            "date": ev_date,
            "where": [{"platform": "app-gallery",
                       "url": "%s/%d.mp4" % (GALLERY_URL, num)}],
            "note": note,
        }
        if major == 2 and w["card_hash"] and w["gallery_sha"] == w["cut_sha"]:
            ev["card_hash"] = w["card_hash"]
        row["versions"].append(ev)
        # A re-publish of a new cut closes any open fix.
        if row.get("open_fix") and live and live["sha1"] != w["gallery_sha"]:
            row["open_fix"] = None
        events.append("row %d -> v%s on app-gallery (%s)" % (num, version, note))

    save_ledger(ledger)
    write_board(ledger, world)

    for line in events:
        print("PUBLISH  " + line)
    print("sync: %d publish event(s) recorded; board regenerated." % len(events))

    if commit:
        msg = ("PUBLISH-LOOP sync: %d event(s) — %s" % (len(events),
               "; ".join(events)[:400]) if events
               else "PUBLISH-LOOP sync: board refresh, no new publishes")
        git_commit(msg, push=push)
    return events


# ------------------------------------------------------------------ board ----

def state_of(num, w, row):
    """(summary key, one-line loop state, next step) for a row."""
    live = _live_event(row)
    fix = row.get("open_fix")
    if fix:
        v = live["version"] if live else "?"
        return ("FIX OPEN",
                "FIX OPEN on v%s — %s" % (v, fix["reason"]),
                "rebuild, re-approve, re-publish (becomes v%s)"
                % _next_version(row, 2))
    if live:
        lv = live["version"]
        if w["gallery_sha"] and live["sha1"] == w["gallery_sha"]:
            if _major_of(lv) == 1:
                if w["approved_current"]:
                    nxt = ("publish the approved v2 cut — replaces the old"
                           " style, becomes v%s" % _next_version(row, 2))
                elif w["wave"] == "realistic-v2":
                    nxt = "REDO-ALL: v2 cut on reviewer — Cameron reviews"
                else:
                    nxt = "REDO-ALL: v2 rebuild pending"
                return ("LIVE — OLD STYLE (v1)", "LIVE v%s — OLD STYLE" % lv, nxt)
            # Judge staleness against the APPROVED bytes (git objects), never
            # the working tree — autopilot rewrites working-tree mp4s.
            if w["approved_current"] and w["approved_sha1"]:
                if w["approved_sha1"] == live["sha1"]:
                    return ("LIVE — current (approved cut)",
                            "LIVE v%s ✓ approved cut" % lv, "—")
                return ("LIVE — STALE",
                        "LIVE v%s — STALE (a newer APPROVED cut exists)" % lv,
                        "publish the approved cut (becomes v%s)"
                        % _next_version(row, 2))
            if w["approved"] and not w["approved_current"]:
                return ("LIVE — new cut awaits Cameron",
                        "LIVE v%s — cut changed since approval" % lv,
                        "Cameron re-reviews the new cut on the board")
            return ("LIVE — current", "LIVE v%s ✓" % lv, "—")
    if w["approved_current"]:
        return ("APPROVED — not published",
                "APPROVED %s — not published" % (w["approved_date"] or ""),
                "publish to app-gallery (becomes v%s)" % _next_version(row, 2))
    if w["wave"] == "realistic-v2":
        return ("ON REVIEWER — awaiting Cameron",
                "ON REVIEWER — awaiting Cameron", "Cameron reviews on the board")
    if w["cut_sha"] or w["slug"]:
        return ("BUILDING", "BUILDING / not on reviewer",
                "runner ships to reviewer")
    return ("NOT BUILT", "NOT BUILT", "author + build")


def write_board(ledger, world):
    lines = []
    counts = {}
    rows_out = []
    for num in sorted(world):
        w = world[num]
        row = ledger["rows"].get(str(num),
                                 {"open_fix": None, "versions": []})
        key, state, nxt = state_of(num, w, row)
        counts[key] = counts.get(key, 0) + 1
        live = _live_event(row)
        where = []
        if live:
            for wh in live["where"]:
                where.append(wh["platform"])
        if w["in_app"]:
            where.append("in-app-list")
        appr = ("✅ " + (w["approved_date"] or "")) if w["approved_current"] \
            else ("(old appr)" if w["approved"] else "⬜")
        rows_out.append("| %d | %s | %s | %s | %s | %s | %s |" % (
            num, w["title"], appr,
            (("v" + live["version"]) if live else "—"),
            (", ".join(where) or "—"), state, nxt))

    lines.append("# PUBLISH BOARD — what is approved and posted where")
    lines.append("")
    lines.append("> **GENERATED by `publish_ledger.py sync` — never hand-edit.**")
    lines.append("> State of record: [`PUBLISH-LEDGER.json`](PUBLISH-LEDGER.json)"
                 " (append-only version history).")
    lines.append(">")
    lines.append("> **THE LOOP:** BUILT → on reviewer → **APPROVED** (Cameron)"
                 " → **PUBLISHED v2.1** → fix ordered → rebuilt → re-approved →"
                 " **PUBLISHED v2.2** → … The first published version stays in"
                 " the ledger forever; a fix never erases it. v1.x = legacy"
                 " cuts still live under REDO-ALL. Every step commits to"
                 " GitHub.")
    lines.append(">")
    lines.append("> Run the loop: `python3 media-production-v2/publish_ledger.py"
                 " sync --commit --push` (autopilot-safe; detects gallery"
                 " publishes automatically). Cameron's approval: `approve N`."
                 " External post: `publish N --platform youtube --url …`."
                 " Complaint on a live video: `fix N --reason \"…\"`.")
    lines.append("")
    lines.append("_Last sync: %s_" % datetime.now().isoformat(timespec="seconds"))
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key in sorted(counts):
        lines.append("- **%s** — %d row(s)" % (key, counts[key]))
    lines.append("")
    lines.append("## The rows")
    lines.append("")
    lines.append("| # | Story | Approved | Live | Posted where | State | Next step |")
    lines.append("|---|---|---|---|---|---|---|")
    lines.extend(rows_out)
    lines.append("")
    with open(BOARD_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# --------------------------------------------------------------- commands ----

def do_approve(num):
    world = scan()
    w = world.get(num)
    if not w or not w["card_hash"]:
        sys.exit("row %d has no reviewer card — nothing to approve" % num)
    approvals = parse_approvals()
    approvals[str(num)] = {"hash": w["card_hash"], "date": TODAY}
    with open(APPROVALS_JSON, "w") as f:
        json.dump(approvals, f, indent=2)
        f.write("\n")
    print("APPROVED row %d — card hash %s stamped %s (approvals.json)"
          % (num, w["card_hash"][:12], TODAY))
    do_sync()


def do_publish(num, platform, url, note, force):
    ledger = load_ledger()
    world = scan()
    w = world.get(num)
    if not w:
        sys.exit("row %d: unknown row" % num)
    row = _row(ledger, num)

    if platform == "app-gallery":
        sys.exit("app-gallery publishes are auto-detected — copy the mp4 to "
                 "site/story-videos/%d.mp4, deploy, then run `sync`." % num)

    sha = w["cut_sha"]
    if not sha:
        sys.exit("row %d has no built cut to publish" % num)
    if not w["approved_current"] and not force:
        sys.exit("row %d's current cut is NOT approved by Cameron — approve "
                 "first, or pass --force if he already said so in chat." % num)

    last = _last_event(row)
    entry = {"platform": platform, "url": url or ""}
    if last and last["sha1"] == sha:
        # Same cut, additional platform — same version, new location.
        if any(x["platform"] == platform for x in last["where"]):
            sys.exit("row %d v%s is already recorded on %s"
                     % (num, last["version"], platform))
        last["where"].append(entry)
        version = last["version"]
    else:
        version = _next_version(row, 2)
        row["versions"].append({
            "version": version, "sha1": sha, "date": TODAY,
            "where": [entry], "note": note or "manual publish",
            **({"card_hash": w["card_hash"]} if w["card_hash"] else {}),
        })
        if row.get("open_fix"):
            row["open_fix"] = None
    save_ledger(ledger)
    write_board(ledger, world)
    print("PUBLISHED row %d v%s -> %s %s" % (num, version, platform, url or ""))
    git_commit("PUBLISH row %d v%s -> %s" % (num, version, platform))


def do_fix(num, reason, close):
    ledger = load_ledger()
    row = _row(ledger, num)
    if close:
        row["open_fix"] = None
        print("fix on row %d closed" % num)
    else:
        if not reason:
            sys.exit("fix needs --reason \"what Cameron wants changed\"")
        row["open_fix"] = {"reason": reason, "opened": TODAY}
        live = _live_event(row)
        print("FIX OPEN on row %d (live %s stays on record as first published;"
              " the re-publish becomes v%s)"
              % (num, "v" + live["version"] if live else "— not live",
                 _next_version(row, 2)))
    save_ledger(ledger)
    write_board(ledger, scan())
    git_commit("PUBLISH-LOOP fix %s row %d%s"
               % ("close" if close else "open", num,
                  "" if close else ": " + reason[:80]))


def do_status(num):
    ledger = load_ledger()
    world = scan()
    targets = [num] if num else sorted(world)
    for n in targets:
        w = world.get(n)
        if not w:
            print("row %d: unknown" % n)
            continue
        row = ledger["rows"].get(str(n), {"open_fix": None, "versions": []})
        _, state, nxt = state_of(n, w, row)
        print("%3d  %-38s %-44s next: %s" % (n, w["title"][:38], state, nxt))


def do_history(num):
    ledger = load_ledger()
    row = ledger["rows"].get(str(num))
    if not row or not row["versions"]:
        print("row %d: no publish history yet" % num)
        return
    print("row %d — %s" % (num, row.get("title") or ""))
    for ev in row["versions"]:
        wheres = ", ".join(
            w["platform"] + ((" " + w["url"]) if w.get("url") else "")
            for w in ev["where"])
        print("  v%-5s %s  sha1 %s  %s  [%s]"
              % (ev["version"], ev["date"], ev["sha1"][:12], wheres,
                 ev.get("note", "")))
    if row.get("open_fix"):
        print("  FIX OPEN since %s: %s"
              % (row["open_fix"]["opened"], row["open_fix"]["reason"]))


# -------------------------------------------------------------------- git ----

def git_commit(msg, push=False):
    files = [LEDGER_PATH, BOARD_PATH, APPROVALS_JSON]
    subprocess.run(["git", "-C", REPO, "add"] + files, check=False)
    r = subprocess.run(["git", "-C", REPO, "diff", "--cached", "--quiet"])
    if r.returncode == 0:
        print("git: nothing to commit")
        return
    subprocess.run(["git", "-C", REPO, "commit", "-m", msg], check=False)
    print("git: committed — %s" % msg)
    if push:
        subprocess.run(["git", "-C", REPO, "pull", "--rebase", "origin", "main"],
                       check=False)
        p = subprocess.run(["git", "-C", REPO, "push", "origin", "main"])
        print("git: push %s" % ("OK" if p.returncode == 0 else "FAILED"))


# -------------------------------------------------------------------- cli ----

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("sync", help="recompute state, record publishes, regen board")
    s.add_argument("--commit", action="store_true")
    s.add_argument("--push", action="store_true")

    s = sub.add_parser("status")
    s.add_argument("row", nargs="?", type=int)

    s = sub.add_parser("history")
    s.add_argument("row", type=int)

    s = sub.add_parser("approve")
    s.add_argument("row", type=int)

    s = sub.add_parser("publish")
    s.add_argument("row", type=int)
    s.add_argument("--platform", required=True,
                   help="youtube / tiktok / facebook / … (app-gallery is auto)")
    s.add_argument("--url", default="")
    s.add_argument("--note", default="")
    s.add_argument("--force", action="store_true")

    s = sub.add_parser("fix")
    s.add_argument("row", type=int)
    s.add_argument("--reason", default="")
    s.add_argument("--close", action="store_true")

    a = ap.parse_args()
    if a.cmd == "sync":
        do_sync(commit=a.commit or a.push, push=a.push)
    elif a.cmd == "status":
        do_status(a.row)
    elif a.cmd == "history":
        do_history(a.row)
    elif a.cmd == "approve":
        do_approve(a.row)
    elif a.cmd == "publish":
        do_publish(a.row, a.platform, a.url, a.note, a.force)
    elif a.cmd == "fix":
        do_fix(a.row, a.reason, a.close)


if __name__ == "__main__":
    main()
