#!/usr/bin/env python3
"""Rebuild the verified postable list for social posting.

Run from the repo root:  python3 social/refresh-postable.py

What it does, start to finish:
1. Runs admin/dump-approvals.mjs for the live approvals.
2. Parses site/review.html for each row's served data-hash, title, meta, data-src.
3. A row is POSTABLE only if approved:true AND approvedHash == the served data-hash
   AND the file bytes are verified against the approved cut.
4. Byte verification handles the three hash schemes the review board has used:
     - blob:   approvedHash is the git blob hash of the mp4 itself
     - commit: approvedHash is the shipping commit; the blob at <commit>:<path>
               must equal the blob at origin/main:<path> (what GitHub raw serves)
     - sha1-prefix12: first 12 hex chars of approvedHash match the first 12 of the
               plain sha1 of the served file (some cards stored a 12-char-prefix id)
5. Extracts every verified approved cut from git objects (NEVER the working tree —
   the autopilot rewrites working-tree mp4s) into social/exports/, re-verifies.
6. Extracts a representative cover frame (30% in, ffmpeg thumbnail filter) into
   social/covers/ for any row that doesn't have one yet.
7. Writes social/postable.json (postable + excluded-with-reason).

Exit code 0 = list written. Any row that cannot be byte-verified is EXCLUDED and
listed with its reason — it is never silently included.
"""
import hashlib
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)


def run(*args, binary=False):
    r = subprocess.run(args, capture_output=True)
    out = r.stdout if binary else r.stdout.decode().strip()
    return r.returncode, out


def main():
    rc, raw = run('node', 'admin/dump-approvals.mjs')
    if rc:
        # Firestore down/quota-walled: fall back to autopilot's validated
        # mirror, but ONLY if it is fresh (<6h) — approvals fail closed.
        mirror = 'media-production-v2/.approvals.json'
        import time
        if os.path.exists(mirror) and time.time() - os.path.getmtime(mirror) < 6*3600:
            age_min = int((time.time() - os.path.getmtime(mirror)) / 60)
            print(f'WARNING: live dump failed - using fresh mirror {mirror} '
                  f'({age_min} min old)', file=sys.stderr)
            raw = open(mirror).read()
        else:
            print('FATAL: dump failed and no fresh (<6h) mirror - refusing '
                  'to guess approvals', file=sys.stderr)
            return 1
    appr = json.loads(raw)

    html = open('site/review.html').read()
    cards = {}
    for b in re.split(r'(?=<div class="card" id="v\d+")', html):
        m = re.match(r'<div class="card" id="v(\d+)"', b)
        if not m:
            continue
        head = b.split('>', 1)[0]
        num = re.search(r'data-num="(\d+)"', head)
        h = re.search(r'data-hash="([0-9a-f]*)"', head)
        if not num or not h:
            continue
        t = re.search(r'<p class="title">(.*?)<span class="meta">(.*?)</span>', b)
        s = re.search(r'data-src="([^"]+)"', b)
        cards[num.group(1)] = dict(
            hash=h.group(1),
            title=re.sub(r'^\d+\s*—\s*', '', t.group(1).strip()) if t else '?',
            meta=t.group(2).replace('&middot;', '·').strip(' ·') if t else '?',
            src=s.group(1) if s else None)

    # TIER ROUTING (Cameron 2026-09-02: "move the export and thumbnails and per
    # video folders to a new folder that is completed... so posting the remaining
    # 100 doesnt get polluted with the already posted 100"). Rows in
    # social/POSTED.json are fully posted on every platform: their kit lives in
    # social/posted-1-100/ and is VERIFIED there, never re-exported to active.
    # GP rows (>300) stage in social/gp-queue/ until Cameron starts that wave.
    try:
        POSTED = set(json.load(open('social/POSTED.json'))['posted_all_socials'])
    except Exception:
        POSTED = set()
    def tier_dir(n):
        if n in POSTED: return 'social/posted-1-100'
        if n >= 301: return 'social/gp-queue'
        return 'social'
    os.makedirs('social/exports', exist_ok=True)
    os.makedirs('social/covers', exist_ok=True)
    postable, excluded = [], []

    for num, a in sorted(appr.items(), key=lambda x: int(x[0])):
        if not a.get('approved'):
            continue
        n = int(num)
        card = cards.get(num)
        if not card:
            excluded.append((n, 'no card on review.html'))
            continue
        ah = a.get('approvedHash')
        if ah != card['hash']:
            excluded.append((n, f"cut changed since approval (served {card['hash'][:10]}, "
                                f"approved {str(ah)[:10]}) — new cut awaits Cameron's review"))
            continue
        if not card['src']:
            excluded.append((n, 'no data-src on card'))
            continue
        src = card['src']
        pinned = None
        if 'raw/main/' in src:
            path = src.split('raw/main/')[1].split('?')[0]
        elif '/MBM/main/' in src:
            path = src.split('/MBM/main/')[1].split('?')[0]
        else:
            # commit-pinned raw URL (cards wired 2026-08-16+):
            # raw.githubusercontent.com/noremacttevol/MBM/<sha>/<path> serves the
            # blob at <sha>:<path> — verify against THAT, not origin/main
            # (2026-09-01: this shape excluded 12 cards, 10 of them approved;
            # Cameron: "i cant find 44 in exports... this shouldnt happen to
            # any of them").
            mm = re.search(r'/MBM/([0-9a-f]{7,40})/([^?"]+\.mp4)', src)
            if mm:
                pinned, path = mm.group(1), mm.group(2)
            else:
                excluded.append((n, f"unrecognized data-src shape: {src[:60]}"))
                continue
        ref = pinned or 'origin/main'
        rc, served_blob = run('git', 'rev-parse', f'{ref}:{path}')
        if rc:
            excluded.append((n, f'path not at {ref[:12]}: {path}'))
            continue

        rc, typ = run('git', 'cat-file', '-t', ah)
        scheme = None
        if rc == 0 and typ == 'blob':
            if served_blob == ah:
                scheme = 'blob'
            else:
                excluded.append((n, f'origin/main blob {served_blob[:10]} != approved blob {ah[:10]}'))
                continue
        elif rc == 0 and typ == 'commit':
            rc2, appr_blob = run('git', 'rev-parse', f'{ah}:{path}')
            if rc2:
                excluded.append((n, f'path missing in approved commit {ah[:10]}'))
                continue
            if served_blob == appr_blob:
                scheme = 'commit'
            else:
                excluded.append((n, f'origin/main blob {served_blob[:10]} != blob in approved '
                                    f'commit {appr_blob[:10]} — file changed after approval'))
                continue
        else:
            _, data = run('git', 'cat-file', 'blob', served_blob, binary=True)
            if hashlib.sha1(data).hexdigest()[:12] == ah[:12]:
                scheme = 'sha1-prefix12'
            else:
                excluded.append((n, f'approved hash {ah[:10]} matches no git object and no '
                                    f'sha1 prefix of the served file — cannot verify'))
                continue

        slug = re.sub(r'[^a-z0-9]+', '-', card['title'].lower()).strip('-')
        export = f'{tier_dir(n)}/exports/row-{n:03d}-{slug}.mp4'
        os.makedirs(os.path.dirname(export), exist_ok=True)
        with open(export, 'wb') as f:
            subprocess.run(['git', 'cat-file', 'blob', served_blob], stdout=f, check=True)
        rc, chk = run('git', 'hash-object', export)
        if chk != served_blob:
            excluded.append((n, 'export re-verification failed'))
            os.remove(export)
            continue

        parts = [p.strip() for p in card['meta'].split('·')]
        # duration is the LAST mm:ss part — GP cards carry TWO scripture refs
        # before it, so a fixed parts[1] missed every GP cover (2026-09-01)
        duration = next((p for p in reversed(parts) if re.match(r'^\d+:\d+$', p)), '')
        cover = f'{tier_dir(n)}/covers/row-{n:03d}.jpg'
        os.makedirs(os.path.dirname(cover), exist_ok=True)
        if not os.path.exists(cover) and re.match(r'^\d+:\d+$', duration):
            mm, ss = duration.split(':')
            seek = max(3, int((int(mm) * 60 + int(ss)) * 0.30))
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', str(seek),
                            '-i', export, '-vf', 'thumbnail=120,scale=1080:1920',
                            '-frames:v', '1', '-q:v', '2', cover])

        postable.append(dict(
            row=n, title=card['title'],
            scripture=parts[0] if parts else '', duration=duration,
            approvedHash=ah, hashScheme=scheme, servedBlob=served_blob,
            approvedAt=a.get('approvedAt'), repoPath=path,
            exportPath=export, cover=cover))

    # PRUNE (2026-09-01, Cameron: "i need all posting needs made for each one
    # when i approve" — and the inverse: a row that is no longer postable must
    # not linger on the posting surface). Remove export files for rows that are
    # not currently postable (a re-cut voided the approval) or whose slug
    # changed. -yt variants follow their base file.
    import glob as _glob
    keep = {e['exportPath'] for e in postable}
    for _f in sorted(_glob.glob('social/exports/row-*.mp4')):  # active tier only
        base = _f[:-7] + '.mp4' if _f.endswith('-yt.mp4') else _f
        if base not in keep:
            os.remove(_f)
            print(f'  pruned {_f} (row no longer postable at this cut)')

    json.dump(dict(
        generated=subprocess.run(['date', '+%Y-%m-%d'], capture_output=True,
                                 text=True).stdout.strip(),
        rule=('POSTABLE = approved:true AND approvedHash == data-hash on site/review.html '
              'AND file bytes verified against the approved cut. Exports come from git '
              'objects, never the working tree (the autopilot rewrites working-tree mp4s).'),
        postable=postable,
        excluded=[dict(row=r, reason=w) for r, w in excluded],
    ), open('social/postable.json', 'w'), indent=2)

    print(f'POSTABLE (byte-verified, exported): {len(postable)}')
    for p in postable:
        print(f"  {p['row']:>3}  {p['title']}  ({p['scripture']}, {p['duration']})  [{p['hashScheme']}]")
    print(f'EXCLUDED: {len(excluded)}')
    for r, w in excluded:
        print(f'  {r}: {w}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
