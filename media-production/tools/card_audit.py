#!/usr/bin/env python3
"""Audit every build's end-card for overflow risk on its CURRENT code+text."""
import os, re, sys, importlib.util, json

ROOT = os.path.expanduser("~/Desktop/MBM/media-production")
MAXCH = 32  # ~32 chars at serif 50-52px fits inside 1080px with margins

def get_card_text(bdir, card_id):
    mn = os.path.join(bdir, "make_narration.py")
    if not os.path.exists(mn):
        return None
    spec = importlib.util.spec_from_file_location("mn_" + os.path.basename(bdir).replace("-","_"), mn)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, bdir)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        return ("IMPORT_FAIL", str(e)[:80])
    finally:
        sys.path.pop(0)
    segs = getattr(mod, "SEGMENTS", None)
    if segs is None:
        return ("NO_SEGMENTS", "")
    for s in segs:
        try:
            if s[0] == card_id:
                # text is usually field 2; fall back to longest str field
                if len(s) > 2 and isinstance(s[2], str):
                    return s[2]
                return max((f for f in s if isinstance(f, str)), key=len)
        except Exception:
            pass
    return ("CARD_ID_NOT_FOUND", card_id)

results = []
for b in sorted(os.listdir(ROOT)):
    bdir = os.path.join(ROOT, b)
    bp = os.path.join(bdir, "build.py")
    if not b.startswith("build-") or not os.path.exists(bp):
        continue
    src = open(bp, encoding="utf-8", errors="replace").read()
    m = re.search(r"def build_card.*?(?=\ndef |\nif __|\Z)", src, re.S)
    fn = m.group(0) if m else ""
    if not fn:
        results.append((b, "NO_BUILD_CARD", "", ""))
        continue
    wraps = "textwrap.wrap" in fn
    variant = "wrap" if wraps else ("perline-split" if 'split("\\n")' in fn or "split('\\n')" in fn else "raw-textfile")
    cm = re.search(r'^CARD\s*=\s*["\'](\w+)["\']', src, re.M)
    card_id = cm.group(1) if cm else None
    text = get_card_text(bdir, card_id) if card_id else None
    status, detail = "?", ""
    if isinstance(text, tuple):
        status, detail = "ERR:" + text[0], text[1]
    elif text is None:
        status = "ERR:NO_CARD_ID"
    elif wraps:
        status = "OK-wraps"
    else:
        lines = text.split("\n")
        long = [ln for ln in lines if len(ln) > MAXCH]
        if long:
            status = "OVERFLOW"
            detail = f"{len(long)} line(s), longest {max(len(l) for l in long)}ch: " + max(long, key=len)[:60]
        else:
            status = "ok-manual-breaks"
    results.append((b, variant, status, detail))

counts = {}
for b, v, s, d in results:
    counts[(v, s.split(":")[0])] = counts.get((v, s.split(":")[0]), 0) + 1
print(json.dumps({"%s|%s" % k: v for k, v in sorted(counts.items())}, indent=1))
print("\n--- OVERFLOW / ERROR builds ---")
for b, v, s, d in results:
    if s.startswith(("OVERFLOW", "ERR", "NO_")):
        print(f"{b:45s} {v:14s} {s:12s} {d}")
