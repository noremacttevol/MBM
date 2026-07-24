#!/usr/bin/env python3
"""Regenerate the GitHub Pages landing page (repo-root index.html) so every
finished story video is watchable at https://noremacttevol.github.io/MBM/ .

It scans media-production/build-NN-*/ for the one scripture-named .mp4 at the
build-folder root (not the per-segment files under segs/ or the raw clips under
assets/), reads its real duration with ffprobe, and reads the approval state
straight out of media-production/QUEUE.md so the page is split into sections:

  🟡 NEEDS YOUR REVIEW  — built, waiting on Cameron's yes  (shown FIRST, on top)
  ✅ APPROVED           — Cameron said yes, not yet posted
  🌐 LIVE IN THE APP    — already shipped (Post ✅)
  🔧 BEING REWORKED     — rejected / in the fix queue

The approval monitor chat runs this after every approve/reject and pushes, so
the live site always matches the board.  Run from the repo root:
  python3 media-production/gen_site_index.py
"""
import glob
import json
import os
import re
import subprocess

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Videos stream straight from GitHub instead of being re-published by Pages, so
# the published site stays tiny (just this HTML) and always deploys. This is the
# same direct-link pattern used by the watch links in STATUS.md.
RAW_BASE = "https://github.com/noremacttevol/MBM/raw/main/"

# The review gallery is hosted on Firebase (milk-b4-meat.web.app/review.html),
# not GitHub Pages — the repo is far over Pages' 1 GB limit, but Firebase only
# uploads the small site/ folder. Videos stream from GitHub (RAW_BASE), so this
# page stays tiny. Deploy with:  firebase deploy --only hosting
OUT_DIR = os.path.join(REPO, "site")
OUT_NAME = "review.html"

# GitHub repo behind the Report-a-problem button + complaint display. Public, so
# the page reads open/closed complaint issues with no token.
GH_OWNER, GH_REPO = "noremacttevol", "MBM"

# Version-lock: Cameron's approval is tied to the EXACT video he watched. We store
# the git blob hash of the mp4 he approved. When a machine rebuilds that video the
# hash changes, the approval auto-falls-off, and it returns to the review list
# flagged "NEW cut." This file is written ONLY by the approval monitor (monitor.py)
# so build machines never conflict on it.
APPROVALS_FILE = os.path.join(REPO, "media-production", "approvals.json")

# RE-CAPTION CAMPAIGN (2026-07-17): all 200 are being re-captioned with the new
# Jost caption engine. Cameron wants to review ONLY the freshly re-captioned cuts.
# A video's build folder gets this file when it's migrated, so we show a card only
# when this marker is present. Set to None to go back to showing every built video.
NEW_CAPTION_MARKER = "mbm_caption_timing.py"

# NEW-VOICE WAVE: Cameron locked the new speaker picks (Jesus=Eric, God=Christopher,
# scripture=Steffan, women=Michelle) in the SPEAKER LAW commit at 2026-07-18 13:29.
# Any video whose finished mp4 was rebuilt at/after that moment has the new voices,
# so it's genuinely ready for his review — those sort to the TOP of the review list
# with a badge. Bump this epoch when a new wave starts.
NEW_VOICE_SINCE = 1784395766  # 2026-07-18 13:29 — SPEAKER LAW

# Nice display titles keyed by build number (the folder slug drives discovery;
# this map only supplies the human-facing name). Anything not listed falls back
# to a title derived from the filename slug.
TITLES = {
    1: "Woman Who Touched His Cloak", 2: "The Prodigal Son", 3: "Zacchaeus",
    4: "Nicodemus at Night", 5: "The Bent-Over Woman", 6: "The Two Sons",
    7: "Peter Walks on Water", 8: "The Lost Coin", 9: "The Rich Young Ruler",
    10: "The Woman at the Well", 11: "Calming the Storm", 12: "Blind Bartimaeus",
    13: "The Man Through the Roof", 14: "The Ten Lepers",
    15: "The Centurion's Servant", 16: "Mary and Martha", 17: "Lazarus",
    18: "The Road to Emmaus", 19: "Breakfast on the Shore",
    20: "The Good Samaritan", 21: "The Lost Sheep",
    22: "The Unmerciful Servant", 23: "The Workers in the Vineyard",
    24: "The Sower", 25: "The Wheat and the Tares", 26: "The Mustard Seed",
    27: "The Leaven", 28: "The Hidden Treasure", 29: "The Pearl of Great Price",
    30: "The Net", 31: "The Ten Virgins", 32: "The Talents",
    33: "The Sheep and the Goats", 34: "The Rich Fool", 35: "The Great Banquet",
    36: "The Shrewd Steward", 37: "The Rich Man and Lazarus", 38: "The Persistent Widow", 39: "The Pharisee and the Publican",
    40: "The Friend at Midnight", 43: "The Wedding Garment",
    41: "Counting the Cost", 42: "The Barren Fig Tree Spared",
    45: "The Wicked Tenants", 46: "The Seed Growing Secretly",
    47: "Houses on Rock and Sand", 48: "New Wine, Old Bottles",
    49: "Water to Wine at Cana", 50: "The Nobleman's Son",
    51: "The First Catch of Fish", 52: "The Demoniac in the Synagogue",
    53: "Peter's Mother-in-Law", 54: "The Leper Made Clean",
    55: "The Withered Hand", 56: "The Widow of Nain's Son",
    57: "Jairus's Daughter", 58: "Feeding the Five Thousand",
    59: "Feeding the Four Thousand", 60: "The Gerasene Demoniac", 61: "The Syrophoenician Woman", 62: "Ephphatha: the Deaf Man", 63: "The Man Born Blind", 64: "The Pool of Bethesda",
    70: "The Temptations",
    71: "Calling the Fishermen", 72: "Calling Matthew",
    81: "Render Unto Caesar",
    73: "This Day Fulfilled", 74: "The Woman Who Washed His Feet",
    75: "The Woman Taken in Adultery",
    76: "Suffer the Little Children",
    84: "No Room: the Manger", 91: "Gethsemane",
    101: "The Still Small Voice", 102: "Jacob's Ladder", 103: "Peter's Confession", 104: "The Boy Samuel", 105: "Face to Face, as a Friend", 106: "God Spake by the Prophets", 107: "John the Baptist's Doubt", 108: "My Sheep Hear My Voice", 109: "Ask, Seek, Knock", 110: "The Lord's Prayer", 111: "Lilies and Sparrows", 112: "The Beatitudes", 113: "Where Art Thou?", 114: "Abraham Pleads for Sodom", 115: "The Ram in the Thicket", 116: "Graven on His Palms", 117: "Hosea Buys Her Back",
    118: "Jonah and the God Who Relents",
    119: "The Fourth Man in the Fire",
    120: "Job Answered from the Whirlwind",
    121: "Salt and Light", 122: "The Mote and the Beam",
    123: "The Golden Rule",
    124: "Love Your Enemies",
    135: "The Rainbow Covenant",
    151: "If Any of You Lack Wisdom",
    152: "He Revealeth His Secret to the Prophets",
    153: "The Restitution of All Things",
    154: "The Angel with the Everlasting Gospel",
    155: "A Falling Away First",
    156: "A Famine of Hearing the Word",
    157: "A Marvellous Work and a Wonder",
    158: "The Stick of Judah and Joseph",
    159: "Other Sheep I Have",
    162: "The Keys of the Kingdom",
    160: "The Stone Cut Without Hands",
    161: "Called of God, as was Aaron",
    163: "Built on Apostles and Prophets",
    164: "Till We All Come in the Unity of the Faith",
    165: "Laying On of Hands for the Holy Ghost",
    166: "Baptized Again, Properly",
    167: "I Have Chosen You, and Ordained You",
    168: "Born of Water and of the Spirit",
    169: "To Fulfil All Righteousness",
    170: "The Sacrament, Worthily",
}

SMALL = {"of", "and", "the", "a", "an", "in", "on", "to", "his", "her"}


def derive_title(slug):
    words = slug.replace("-", " ").split()
    out = []
    for i, w in enumerate(words):
        out.append(w if (w in SMALL and i) else w.capitalize())
    return " ".join(out)


def scripture(book_chap):
    # "mark-5" -> "Mark 5"; "matthew-13" -> "Matthew 13";
    # numbered books: "1kings-19" -> "1 Kings 19", "2samuel-7" -> "2 Samuel 7"
    book, chap = book_chap.rsplit("-", 1)
    m = re.match(r"^(\d+)([a-z]+)$", book)
    if m:
        book = f"{m.group(1)} {m.group(2).capitalize()}"
    else:
        book = book.capitalize()
    return f"{book} {chap}"


def dur(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True)
    try:
        s = int(round(float(out.stdout.strip())))
        return f"{s // 60}:{s % 60:02d}"
    except ValueError:
        return ""


# Backup/working copies that must NEVER be picked as the delivered cut. A build
# folder often keeps a pre-fix copy next to the real video, and those backups are
# usually NOT committed — so linking one gives Cameron a dead URL and a blank
# player. (Video #16: the card pointed at luke-10_mary-and-martha.orig.mp4, which
# was never pushed — he reported "what the heck no video", 2026-07-18.)
_BACKUP_MP4 = re.compile(r"(\.orig\.|\.bak\.|[._-]old[._-]|_OLD|pre-[a-z0-9]+-fix)", re.I)


def find_main_mp4(build_dir):
    # the finished cut is the single scripture-named mp4 sitting directly in the
    # build folder (book-chap_slug.mp4), never inside segs/ or assets/
    # book part may itself contain hyphens for numbered books — "1-corinthians-15_",
    # "1-peter-4_" — so allow hyphens before the trailing "-<chapter>_". The old
    # pattern (^[0-9a-z]+-\d+_) rejected those, so videos #171 and #172 got NO card
    # on the review page at all and Cameron simply could not see them (2026-07-18).
    hits = [p for p in glob.glob(os.path.join(build_dir, "*.mp4"))
            if re.match(r"^[0-9a-z-]+-\d+_", os.path.basename(p))
            and not _BACKUP_MP4.search(os.path.basename(p))]
    if not hits:
        return None
    # Deterministic: glob order is filesystem order, so a stray second mp4 could
    # win at random. Prefer the most recently modified real cut, then sort by name.
    hits.sort(key=lambda p: (-os.path.getmtime(p), os.path.basename(p)))
    if len(hits) > 1:
        print(f"  WARNING: {os.path.basename(build_dir)} has {len(hits)} candidate "
              f"mp4s {[os.path.basename(h) for h in hits]} — using "
              f"{os.path.basename(hits[0])}")
    return hits[0]


def load_approvals():
    """{num(str): {"hash": blob, "date": "YYYY-MM-DD"}} — what Cameron approved
    and which exact cut. Missing/broken file = nothing approved (fresh slate)."""
    try:
        with open(APPROVALS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        return {}


def mp4_hashes():
    """build number -> git blob hash of its finished mp4 as it exists ON THE BOARD.
    The board streams from origin/main (RAW_BASE), so the cache-buster MUST come
    from origin/main — not local HEAD, which can diverge from what's published.
    Reads the git tree, not the file bytes, so it's instant even for 15 GB of video."""
    ref = "origin/main"
    if subprocess.run(["git", "rev-parse", "--verify", "-q", ref],
                      cwd=REPO, capture_output=True).returncode != 0:
        ref = "HEAD"
    out = subprocess.run(
        ["git", "ls-tree", "-r", ref, "--", "media-production"],
        cwd=REPO, capture_output=True, text=True).stdout
    hashes = {}
    for line in out.splitlines():
        try:
            meta, path = line.split("\t", 1)
            _, _typ, h = meta.split()
        except ValueError:
            continue
        m = re.match(r"media-production/build-(\d+)-.*/[0-9a-z]+-\d+_.*\.mp4$", path)
        if m:
            hashes[int(m.group(1))] = h
    return hashes


def new_voice_set():
    """Videos whose finished mp4 was rebuilt at/after the SPEAKER LAW — i.e. re-made
    with Cameron's new voices, so they're the ones actually ready for his review."""
    out = subprocess.run(
        ["git", "log", f"--since=@{NEW_VOICE_SINCE}", "--name-only", "--format=",
         "--", "media-production"],
        cwd=REPO, capture_output=True, text=True).stdout
    found = set()
    for line in out.splitlines():
        m = re.match(r"media-production/build-(\d+)-.*/[0-9a-z]+-\d+_.*\.mp4$", line.strip())
        if m:
            found.add(int(m.group(1)))
    return found


def parse_queue():
    """Read state from QUEUE.md.

    Returns (appr, post, rejected, reasons):
      appr[num]     -> True if that row's Appr column is ✅ (legacy; page now uses
                       approvals.json for approval + version)
      post[num]     -> True if that row's Post column is ✅
      rejected      -> set of numbers sitting in the Fix queue
      reasons[num]  -> the "What's wrong" text for a rejected video
    """
    path = os.path.join(REPO, "media-production", "QUEUE.md")
    appr, post, rejected, reasons = {}, {}, set(), {}
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return appr, post, rejected, reasons

    section = None
    for line in lines:
        s = line.strip()
        if s.startswith("## "):
            low = s.lower()
            if "fix queue" in low:
                section = "fix"
            elif low.startswith("## the 200"):
                section = "200"
            else:
                section = "other"
            continue
        if not s.startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|")]
        # parts[0] is '' (before first pipe); real columns start at parts[1]
        if len(parts) < 3 or not re.match(r"^\d+$", parts[1]):
            continue  # skips header + separator rows
        num = int(parts[1])
        if section == "fix":
            rejected.add(num)
            # fix-queue row: '' | # | Story | What's wrong | Claimed by | ''
            if len(parts) > 3 and num not in reasons:
                reasons[num] = parts[3]
        elif section == "200" and len(parts) >= 9:
            # '' | # | Story | Ref | Prep | Built | Appr | Post | notes | ''
            appr[num] = (parts[6] == "✅")
            post[num] = (parts[7] == "✅")
    return appr, post, rejected, reasons


FIREBASE_CONFIG = {
    "apiKey": "AIzaSyC9xaj2MNJMf1pmTWC8Q5Rh3bDkYJZ8-eo",
    "authDomain": "milk-b4-meat.firebaseapp.com",
    "projectId": "milk-b4-meat",
    "storageBucket": "milk-b4-meat.firebasestorage.app",
    "messagingSenderId": "626094743218",
    "appId": "1:626094743218:web:acaa328d38c6aaf04f33ab",
}

STYLE = """
  :root { color-scheme: dark; }
  * { box-sizing: border-box; }
  body { margin: 0; padding: 0 16px 64px; background: #0f0f12; color: #eee;
    font-family: -apple-system, system-ui, "Segoe UI", Roboto, sans-serif;
    line-height: 1.4; }
  header { padding: 24px 0 8px; max-width: 780px; margin: 0 auto; }
  h1 { font-size: 22px; margin: 0 0 4px; }
  .sub { color: #9aa; font-size: 14px; margin: 0 0 4px; }
  .wrap { max-width: 780px; margin: 0 auto; }
  h2 { font-size: 15px; text-transform: uppercase; letter-spacing: .06em;
       color: #8ab; margin: 32px 0 6px; border-bottom: 1px solid #2a2a30;
       padding-bottom: 6px; }
  .card { background: #16161b; border: 1px solid #26262e; border-radius: 14px;
          padding: 12px; margin: 0 0 18px; }
  .card.approved { border-color: #2e5a24; }
  .title { font-weight: 600; font-size: 16px; margin: 0 0 8px; }
  .meta { color: #889; font-size: 13px; font-weight: 400; }
  video { width: 100%; border-radius: 10px; background: #000; display: block; }
  .note { color: #778; font-size: 13px; margin: 0 0 12px; }
  .done-head { color: #667; border-bottom-color: #202028; }
  details { margin: 0 0 10px; }
  summary { cursor: pointer; list-style: none; user-select: none;
             font-size: 15px; font-weight: 600; color: #7c9;
             background: #14140f; border: 1px solid #26262e; border-radius: 12px;
             padding: 12px 14px; }
  summary::-webkit-details-marker { display: none; }
  summary::before { content: "\\25b8 "; color: #567; }
  details[open] > summary::before { content: "\\25be "; }
  details[open] > summary { margin-bottom: 14px; }
  .actions { display: flex; gap: 8px; margin-top: 10px; }
  .approve { flex: 1; cursor: pointer; font-size: 15px; font-weight: 700;
             background: #16351a; color: #b6e6a4; border: 1px solid #2e5a24;
             border-radius: 10px; padding: 12px; }
  .approve.on { background: #1f5a26; color: #eafce2; }
  .cbtn { cursor: pointer; font-size: 14px; font-weight: 600; background: #201014;
          color: #f0a9b8; border: 1px solid #52242e; border-radius: 10px; padding: 12px 14px; }
  .cbox { margin-top: 10px; }
  .cbox textarea { width: 100%; background: #0e0e12; color: #eee; border: 1px solid #3a2a2e;
                   border-radius: 8px; padding: 8px; font-size: 14px; font-family: inherit; }
  .csave { margin-top: 6px; cursor: pointer; background: #52242e; color: #ffd7df;
           border: 0; border-radius: 8px; padding: 8px 12px; font-weight: 600; }
  .cshow .cmsg { border-radius: 8px; padding: 8px 10px; margin: 8px 0 0; font-size: 13px;
                 background: #2a1414; border: 1px solid #6a2a2a; color: #f0b4b4; }
  .cshow .cmsg .clear { margin-left: 6px; font-size: 12px; background: transparent;
                        color: #f0b4b4; border: 1px solid #6a2a2a; border-radius: 6px;
                        padding: 2px 6px; cursor: pointer; }
  .flag { border-radius: 8px; padding: 8px 10px; margin: 0 0 8px; font-size: 13px; font-weight: 600; }
  .flag.new { background: #2a2410; border: 1px solid #6a5a1e; color: #e8cf7a; }
  .flag.fixed { background: #14210f; border: 1px solid #2e5a24; color: #b6e6a4; }
  .flag.voice { background: #101f2e; border: 1px solid #2b5c7a; color: #9fd4f5; }
  #status { color: #c9a; }
"""

SCRIPT = """
var CFG = __CONFIG__;
var REJECTED = __REJECTED__;
var db = null, ready = false, STATE = {};

function esc(s){ var d=document.createElement('div'); d.textContent=s||""; return d.innerHTML; }

function place(){
  var review=document.getElementById('review');
  var approved=document.getElementById('approved');
  var rework=document.getElementById('rework');
  var nR=0,nA=0,nW=0, reviewNew=[], reviewOld=[];
  document.querySelectorAll('.card').forEach(function(card){
    var num=card.dataset.num, hash=card.dataset.hash, d=STATE[num]||{};
    var approvedNow = d.approved && d.approvedHash===hash;
    var complaintActive = d.complaint && d.complaintHash===hash;
    var rebuiltAfterAppr = d.approved && d.approvedHash && d.approvedHash!==hash;
    var fixedByNewCut = d.complaint && d.complaintHash && d.complaintHash!==hash;
    var machineReason = REJECTED[num];

    var btn=document.getElementById('appbtn'+num);
    btn.textContent = approvedNow ? "\\u2713 Approved \\u2014 tap to undo" : "Approve";
    btn.className = "approve" + (approvedNow?" on":"");
    card.className = "card" + (approvedNow?" approved":"");

    var flags=document.getElementById('flags'+num); flags.innerHTML='';
    if(fixedByNewCut && !complaintActive)
      flags.innerHTML += '<div class="flag fixed">\\u2705 Your complaint was addressed by a newer cut \\u2014 re-watch to confirm.</div>';
    if(rebuiltAfterAppr)
      flags.innerHTML += '<div class="flag new">\\ud83d\\udd01 NEW cut \\u2014 changed since you approved it. Re-watch.</div>';

    var cshow=document.getElementById('cshow'+num); cshow.innerHTML='';
    if(complaintActive)
      cshow.innerHTML += '<div class="cmsg">\\ud83d\\udea9 Your complaint: '+esc(d.complaint)
        +' <button class="clear" onclick="clearComplaint('+num+')">mark resolved</button></div>';
    if(machineReason)
      cshow.innerHTML += '<div class="cmsg">\\ud83d\\udd27 '+esc(machineReason)+'</div>';

    var dest = (machineReason || complaintActive) ? rework : (approvedNow ? approved : review);
    if(dest===review){ (card.dataset.newvoice==='1' ? reviewNew : reviewOld).push(card); nR++; }
    else { dest.appendChild(card); if(dest===approved) nA++; else nW++; }
  });
  // New-voice re-makes go FIRST so Cameron sees what's actually ready.
  reviewNew.forEach(function(c){ review.appendChild(c); });
  reviewOld.forEach(function(c){ review.appendChild(c); });
  var vTxt = reviewNew.length ? (" \\u2014 "+reviewNew.length+" with the NEW VOICES on top") : "";
  document.getElementById('rh').textContent = "\\ud83d\\udfe1 Needs your review ("+nR+")"+vTxt;
  document.getElementById('ah').textContent = "\\u2705 Approved ("+nA+")";
  document.getElementById('wh').textContent = "\\ud83d\\udd27 Being reworked ("+nW+")";
}

function toggleApprove(num){
  if(!ready){ alert("Still connecting \\u2014 give it a second, then tap again."); return; }
  var card=document.getElementById('v'+num), hash=card.dataset.hash, d=STATE[num]||{};
  var approvedNow = d.approved && d.approvedHash===hash;
  db.collection('reviews').doc(String(num)).set({
    approved: !approvedNow, approvedHash: hash,
    approvedAt: firebase.firestore.FieldValue.serverTimestamp()
  }, {merge:true}).catch(function(e){ alert("Save failed: "+e.message); });
}
function toggleBox(num){ var b=document.getElementById('cbox'+num); b.hidden=!b.hidden; }
function saveComplaint(num){
  if(!ready){ alert("Still connecting \\u2014 give it a second, then save again."); return; }
  var t=document.getElementById('ctext'+num).value.trim(); if(!t) return;
  var hash=document.getElementById('v'+num).dataset.hash;
  db.collection('reviews').doc(String(num)).set({
    complaint: t, complaintHash: hash,
    complaintAt: firebase.firestore.FieldValue.serverTimestamp()
  }, {merge:true}).then(function(){ document.getElementById('cbox'+num).hidden=true; })
   .catch(function(e){ alert("Save failed: "+e.message); });
}
function clearComplaint(num){
  if(!ready) return;
  db.collection('reviews').doc(String(num)).set({ complaint:"", complaintHash:"" }, {merge:true});
}

place();  // show everything (in review) immediately, before the cloud loads

try {
  firebase.initializeApp(CFG);
  db = firebase.firestore();
  firebase.auth().signInAnonymously().catch(function(e){
    document.getElementById('status').textContent = "Cloud sign-in issue: "+e.message; });
  firebase.auth().onAuthStateChanged(function(user){
    if(!user) return;
    ready = true;
    document.getElementById('status').textContent = "";
    db.collection('reviews').onSnapshot(function(snap){
      STATE = {}; snap.forEach(function(doc){ STATE[doc.id]=doc.data(); });
      place();
    }, function(err){ document.getElementById('status').textContent = "Cloud read issue: "+err.message; });
  });
} catch(e) {
  document.getElementById('status').textContent = "Cloud offline \\u2014 showing all videos to review.";
}
"""


FIXNOTES_FILE = os.path.join(REPO, "media-production", "FIXNOTES.json")

# QC GATE (2026-07-24): the board's real source of truth for "is this actually
# ready for Cameron." Written by admin/qc_sweep.py, which reads each video's ACTUAL
# content (voice sample-rate, transcript echo, playable, complete). A video is
# shown for review ONLY if it passes here — no more trusting a git timestamp.
QC_STATUS_FILE = os.path.join(REPO, "media-production", "QC-STATUS.json")


def load_qc():
    """{num(int): {"pass": bool, "reasons": [...]}} — content-verified status.
    Empty (missing file) = fail open to the old behaviour so the board never goes
    blank if the sweep hasn't run; but the sweep is wired into the ship loop."""
    try:
        with open(QC_STATUS_FILE, encoding="utf-8") as f:
            return {int(k): v for k, v in json.load(f).items()}
    except (FileNotFoundError, ValueError):
        return {}


def load_fixnotes():
    """{num(str): [{"date": "YYYY-MM-DD", "note": "..."}]} — plain-English record of
    what each shipped cut changed, written by admin/ship-fixes.sh. The board shows
    the latest note under the video so Cameron knows exactly what to check."""
    try:
        with open(FIXNOTES_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        return {}


def card_html(num, title, scrip, length, rel, hashval, newvoice=False, fixnote=None):
    meta = f" · {scrip}" + (f" · {length}" if length else "")
    voice_badge = ('<div class="flag voice">✅ QC-VERIFIED — real new voice, no '
                   'scripture echo, plays start to finish</div>\n') if newvoice else ""
    fix_line = ""
    if fixnote:
        import html as _html
        fix_line = (f'<div class="flag fixed">🛠 What this cut changed '
                    f'({_html.escape(fixnote["date"])}): {_html.escape(fixnote["note"])}</div>\n')
    return (
        f'<div class="card" id="v{num}" data-num="{num}" data-hash="{hashval}"'
        f'{" data-newvoice=\"1\"" if newvoice else ""}>'
        f'<p class="title">{num:02d} — {title}<span class="meta">{meta}</span></p>\n'
        f'{voice_badge}'
        f'{fix_line}'
        f'<div class="flags" id="flags{num}"></div>\n'
        # ?v=<content hash> busts GitHub-raw + browser caching: same filename, new
        # bytes -> new URL, so Cameron always sees the CURRENT cut, never a stale one.
        f'<video controls preload="metadata" playsinline '
        f'src="{RAW_BASE}{rel}?v={(hashval or "0")[:12]}"></video>\n'
        f'<div class="actions">'
        f'<button class="approve" id="appbtn{num}" onclick="toggleApprove({num})">Approve</button>'
        f'<button class="cbtn" onclick="toggleBox({num})">🚩 Report a problem</button>'
        f'</div>\n'
        f'<div class="cbox" id="cbox{num}" hidden>'
        f'<textarea id="ctext{num}" rows="2" placeholder="What is wrong with this video?"></textarea><br>'
        f'<button class="csave" onclick="saveComplaint({num})">Save complaint</button>'
        f'</div>\n'
        f'<div class="cshow" id="cshow{num}"></div>'
        f'</div>')


def main():
    approved_nums = set(load_approvals().keys())  # never hide an approved video
    qc = load_qc()
    qc_pass = {n for n, v in qc.items() if v.get("pass")}  # content-verified good
    newvoice = qc_pass  # the badge now means "QC-verified", not "committed recently"
    builds = sorted(glob.glob(os.path.join(REPO, "media-production", "build-*")))
    cards = []
    total_built = 0
    qc_blocked = 0
    for bd in builds:
        m = re.match(r"build-(\d+)-", os.path.basename(bd))
        if not m:
            continue
        num = int(m.group(1))
        mp4 = find_main_mp4(bd)
        if not mp4:
            continue
        total_built += 1
        # Re-caption campaign: surface videos that have the new captions — PLUS any
        # Cameron already approved, so an approval can never vanish from the page.
        has_marker = os.path.exists(os.path.join(bd, NEW_CAPTION_MARKER)) if NEW_CAPTION_MARKER else True
        if not has_marker and str(num) not in approved_nums:
            continue
        # THE GATE: a video reaches the board ONLY if it passed content QC (real new
        # voice, no echo, plays fully). If the sweep has a verdict and it's a FAIL,
        # the video is held back — Cameron never sees a bad one dressed up as ready.
        # (Approved cuts are never hidden. If the sweep hasn't run at all, qc is
        # empty and we fall open so the board can't accidentally go blank.)
        if qc and num not in qc_pass and str(num) not in approved_nums:
            qc_blocked += 1
            continue
        rel = os.path.relpath(mp4, REPO).replace(os.sep, "/")
        fname = os.path.basename(mp4)
        book_chap = fname.split("_", 1)[0]
        slug = fname.rsplit("_", 1)[1].rsplit(".", 1)[0]
        title = TITLES.get(num, derive_title(slug))
        cards.append((num, title, scripture(book_chap), dur(mp4), rel))

    cards.sort(key=lambda c: c[0])
    _appr, _post, rejected, reasons = parse_queue()
    hashes = mp4_hashes()
    count = len(cards)
    approved_shown = sum(1 for (n, *_ ) in cards if str(n) in load_approvals())

    # Every video is rendered once into a hidden pool. The page's JavaScript reads
    # Cameron's approvals/complaints live from Firestore and moves each card into
    # the right section — approve + complaint save with ONE TAP, no leaving the page.
    fixnotes = load_fixnotes()
    pool = "\n".join(card_html(n, t, s, l, r, hashes.get(n, ""), n in newvoice,
                               (fixnotes.get(str(n)) or [None])[-1])
                      for (n, t, s, l, r) in cards)

    rejected_json = json.dumps({str(n): reasons.get(n, "") for n in rejected})
    config_json = json.dumps(FIREBASE_CONFIG)
    fb = "https://www.gstatic.com/firebasejs/10.12.2"

    script = (SCRIPT
              .replace("__CONFIG__", config_json)
              .replace("__REJECTED__", rejected_json))

    html = (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<title>MBM — Story Videos</title>\n"
        f"<style>{STYLE}</style>\n"
        f'<script src="{fb}/firebase-app-compat.js"></script>\n'
        f'<script src="{fb}/firebase-auth-compat.js"></script>\n'
        f'<script src="{fb}/firebase-firestore-compat.js"></script>\n'
        "</head>\n<body>\n<header>\n"
        "  <h1>Milk Before Meat — New-Caption Review</h1>\n"
        "  <p class=\"sub\">These are the videos re-done with the <b>new captions</b> — the only "
        "ones here. Watch each, tap <b>Approve</b> if the captions are good, or <b>Report a "
        "problem</b> to flag it. Both save the second you tap. More appear as they're re-captioned.</p>\n"
        f"  <p class=\"sub\">{count} passed QC and are ready to review · "
        f"{qc_blocked} held back (still old voice / not fully re-made) so you never "
        f"watch a bad one.</p>\n"
        "  <p id=\"status\" class=\"sub\">Connecting…</p>\n"
        "</header>\n<div class=\"wrap\">\n"
        "  <h2 id=\"rh\">🟡 Needs your review</h2>\n  <div id=\"review\"></div>\n"
        "  <h2 class=\"done-head\">Done — tap to open</h2>\n"
        "  <details><summary id=\"ah\">✅ Approved</summary><div id=\"approved\"></div></details>\n"
        "  <details><summary id=\"wh\">🔧 Being reworked</summary><div id=\"rework\"></div></details>\n"
        f"  <div id=\"pool\" hidden>\n{pool}\n  </div>\n"
        "</div>\n"
        f"<script>\n{script}\n</script>\n"
        "</body>\n</html>\n"
    )

    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, OUT_NAME)
    with open(out, "w") as f:
        f.write(html)
    print(f"wrote {out} with {count} videos ({len(rejected)} in fix queue)")


if __name__ == "__main__":
    main()
