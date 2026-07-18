#!/usr/bin/env python3
"""MBM "how I see it" view.

For every ACTIVE complaint on Cameron's board, this pulls the exact frame at the
timestamp he named (e.g. "0:29", "@0:38") — or the closing frame when he talks
about the ending — and writes a single self-contained HTML page that puts his
words right next to the picture I'm looking at. Cameron opens ONE page and sees
that the machine is looking at the right spot; he never has to relay anything.

  python3 admin/complaint-view.py            # -> site/how-i-see-it.html

Run from the repo root (or anywhere; paths resolve to repo root).
"""
import base64
import glob
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MP = os.path.join(ROOT, "media-production")
OUT = os.path.join(ROOT, "site", "how-i-see-it.html")


def active_complaints():
    rows = []
    path = os.path.join(MP, "COMPLAINTS.md")
    if not os.path.exists(path):
        return rows
    with open(path) as f:
        for line in f:
            m = re.match(r"\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*$", line.strip())
            if m:
                rows.append((int(m.group(1)), m.group(2)))
    return rows


def build_dir(n):
    for d in sorted(glob.glob(os.path.join(MP, "build-*"))):
        base = os.path.basename(d)
        m = re.match(r"build-0*(\d+)-", base)
        if m and int(m.group(1)) == n and os.path.isdir(d):
            return d
    return None


def mp4_in(d):
    cands = [p for p in glob.glob(os.path.join(d, "*.mp4"))
             if not p.endswith(".orig")]
    return cands[0] if cands else None


def dur_of(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True)
    try:
        return float(out.stdout.strip())
    except ValueError:
        return 0.0


def pick_time(text, dur):
    """Timestamp Cameron named (m:ss), else the ending if he mentions it, else mid."""
    m = re.search(r"(\d+):(\d{2})", text)
    if m:
        return int(m.group(1)) * 60 + int(m.group(2)), "the moment you flagged"
    if re.search(r"end|cuts? off|too (early|soon)|last (question|line)|stopped",
                 text, re.I):
        return max(0.0, dur - 1.2), "the ending"
    return dur / 2, "mid-video"


def frame_b64(mp4, t):
    tmp = "/tmp/_mbm_complaint_frame.jpg"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.2f}",
                    "-i", mp4, "-frames:v", "1", "-vf", "scale=360:-1", tmp],
                   capture_output=True)
    if not os.path.exists(tmp):
        return None
    with open(tmp, "rb") as f:
        return base64.b64encode(f.read()).decode()


def main():
    rows = active_complaints()
    cards = []
    for n, text in rows:
        d = build_dir(n)
        mp4 = mp4_in(d) if d else None
        if not mp4:
            cards.append(f"<div class=card><h2>#{n}</h2><p class=says>{text}</p>"
                         f"<p class=miss>no built mp4 found for this video</p></div>")
            continue
        dur = dur_of(mp4)
        t, why = pick_time(text, dur)
        b = frame_b64(mp4, t)
        mm, ss = int(t) // 60, int(t) % 60
        img = (f"<img src='data:image/jpeg;base64,{b}'>" if b
               else "<p class=miss>could not grab frame</p>")
        cards.append(
            f"<div class=card><h2>#{n} &middot; {os.path.basename(mp4)}</h2>"
            f"<p class=says>&ldquo;{text}&rdquo;</p>"
            f"<div class=row>{img}<div class=meta>"
            f"<div>Looking at <b>{mm}:{ss:02d}</b> ({why})</div>"
            f"<div>Video length: {int(dur)//60}:{int(dur)%60:02d}</div>"
            f"</div></div></div>")
    body = "\n".join(cards) if cards else "<p class=clear>Board clear — 0 active complaints.</p>"
    html = f"""<!doctype html><meta charset=utf-8>
<title>MBM — How I see your complaints</title>
<style>
 body{{font:16px/1.5 -apple-system,system-ui,Segoe UI,Roboto,sans-serif;
   max-width:760px;margin:24px auto;padding:0 16px;color:#1a1a1a;background:#faf8f5}}
 h1{{font-size:22px}} .card{{background:#fff;border:1px solid #e6e0d8;border-radius:12px;
   padding:16px 18px;margin:16px 0;box-shadow:0 1px 3px rgba(0,0,0,.05)}}
 .card h2{{font-size:16px;margin:0 0 8px}} .says{{font-style:italic;color:#8a3b12;
   background:#fdf2ea;border-left:3px solid #d9743f;padding:8px 12px;border-radius:6px}}
 .row{{display:flex;gap:16px;align-items:flex-start;margin-top:12px}}
 .row img{{border-radius:8px;border:1px solid #ddd;width:220px}}
 .meta{{font-size:14px;color:#444}} .meta b{{color:#111}}
 .clear{{color:#2e7d32;font-weight:600}} .miss{{color:#b00}}
</style>
<h1>How I see your complaints</h1>
<p>Auto-pulled from your review board. This is the exact spot I'm looking at for each one.</p>
{body}
"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        f.write(html)
    print(f"wrote {OUT} ({len(rows)} active complaints)")


if __name__ == "__main__":
    main()
