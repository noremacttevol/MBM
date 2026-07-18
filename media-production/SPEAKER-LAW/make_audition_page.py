#!/usr/bin/env python3
"""Build the self-contained audition page: voice candidates + caption colours.

Everything is inlined as data: URIs (the Artifact CSP blocks every external host).
The caption specimens use the REAL Jost-Bold from media-production/ over a REAL
still at the REAL band geometry, so what Cameron judges is what will render.
"""
import base64
import glob
import io
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
MP = os.path.dirname(HERE)
JOST = os.path.join(MP, "Jost-Bold.ttf")
AUD = os.path.join(HERE, "auditions")

VOICES = [
    ("Jesus", "red", "#EE3322", "John 14:27",
     "Younger than the voice we have now. Put together, slow, calm, collected.",
     [("Brian", "approachable, sincere — the youngest read of the four"),
      ("Guy", "warmer and rounder, a little more feeling in it"),
      ("Eric", "even, measured, very steady"),
      ("Steffan", "quiet and level, the most restrained")]),
    ("God / the Godhead", "green", "#5BE38B", "Isaiah 41:10",
     "Older, deeper, peaceful, stable. This is the premortal Jehovah of the Old "
     "Testament as much as the Father — the voice behind the green captions.",
     [("Christopher", "the voice Jesus uses today — reads older, which is why it "
       "fits God better than it fits Jesus"),
      ("GB-Thomas", "British, grave and still"),
      ("GB-Ryan", "British, warmer and rounder"),
      ("Roger", "American, bigger and more resonant")]),
    ("Everyone else in scripture", "light blue", "#8FDCFF", "Romans 8:38–39 (Paul)",
     "Paul, the prophets, the apostles, the people inside the stories. One shared "
     "man's voice for all of them.",
     [("IN-Prabhat", "the closest thing edge-tts has to a non-Western cadence"),
      ("ZA-Luke", "South African, dry and raspy"),
      ("KE-Chilemba", "Kenyan, deeper and rounder"),
      ("Steffan", "plain American, pitched down for rasp — the safe option")]),
    ("Women in scripture", "pink", "#FF9EC7", "Ruth 1:16",
     "Any woman the Bible records speaking, in Old English.",
     [("Jenny", "warm and considerate, the gentlest"),
      ("Aria", "clearer and more confident"),
      ("GB-Sonia", "British, more formal"),
      ("Michelle", "brighter and lighter")]),
]

COLORS = [
    ("Jesus", "locked", [("#EE3322", "the red we already have")],
     "Come unto me, all ye that labour and are heavy laden"),
    ("God", "pick one", [("#3FD97A", "A"), ("#5BE38B", "B"), ("#57DD6B", "C")],
     "Fear thou not; for I am with thee: be not dismayed"),
    ("Scripture", "pick one", [("#79D2F7", "A"), ("#8FDCFF", "B"), ("#6FC9EE", "C")],
     "For I am persuaded, that neither death, nor life"),
    ("Women", "pick one", [("#FF9EC7", "A"), ("#FFB0D2", "B"), ("#F98FBB", "C")],
     "Thy people shall be my people, and thy God my God"),
]


def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def still_uri():
    """Brightest bottom-band still in the library = the worst case for readability."""
    best = None
    for f in glob.glob(f"{MP}/build-*/assets/*.jpeg")[:400]:
        try:
            im = Image.open(f).convert("L")
            w, h = im.size
            v = sum(im.crop((0, int(h * .80), w, h)).resize((40, 10)).getdata()) / 400.0
            if best is None or v > best[0]:
                best = (v, f)
        except Exception:
            pass
    im = Image.open(best[1]).convert("RGB")
    w, h = im.size
    sc = max(760 / w, 1350 / h)
    im = im.resize((int(w * sc), int(h * sc)))
    l, t = (im.width - 760) // 2, (im.height - 1350) // 2
    im = im.crop((l, t, l + 760, t + 1350))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=82)
    return base64.b64encode(buf.getvalue()).decode(), os.path.basename(best[1])


def main():
    font = b64(JOST)
    still, still_name = still_uri()

    rows = []
    for role, colname, hexc, ref, note, cands in VOICES:
        items = []
        for i, (name, desc) in enumerate(cands, 1):
            f = glob.glob(os.path.join(AUD, f"{role.split()[0].upper()}*-{i}-*.mp3"))
            if not f:
                key = {"Jesus": "JESUS", "God": "GOD",
                       "Everyone": "SCRIPTURE", "Women": "FEMALE"}[role.split()[0]]
                f = glob.glob(os.path.join(AUD, f"{key}-{i}-*.mp3"))
            if not f:
                continue
            items.append(f'''
      <li class="cand">
        <span class="num">{i}</span>
        <div class="cand-body">
          <p class="cand-name">{name}</p>
          <p class="cand-desc">{desc}</p>
          <audio controls preload="none"
            src="data:audio/mpeg;base64,{b64(f[0])}"></audio>
        </div>
      </li>''')
        rows.append(f'''
  <section class="role">
    <header class="role-head">
      <span class="swatch" style="--c:{hexc}"></span>
      <div>
        <h3>{role}</h3>
        <p class="role-meta">{colname} captions &middot; {ref}</p>
      </div>
    </header>
    <p class="role-note">{note}</p>
    <ol class="cands">{''.join(items)}
    </ol>
  </section>''')

    swatches = []
    for role, state, opts, text in COLORS:
        tiles = []
        for hexc, label in opts:
            tiles.append(f'''
        <figure class="tile">
          <div class="phone" role="img" aria-label="story still with caption">
            <p class="cap" style="--c:{hexc}">{text}</p>
          </div>
          <figcaption><b>{label}</b><code>{hexc}</code></figcaption>
        </figure>''')
        swatches.append(f'''
  <section class="crole">
    <h3>{role} <span class="tag {'locked' if state == 'locked' else ''}">{state}</span></h3>
    <div class="tiles">{''.join(tiles)}</div>
  </section>''')

    html = f'''<title>MBM — Speaker Voices &amp; Caption Colours</title>
<style>
  @font-face {{
    font-family: "Jost";
    src: url(data:font/ttf;base64,{font}) format("truetype");
    font-weight: 700; font-display: block;
  }}
  :root {{
    --ground:#12100E; --surface:#1D1A16; --raised:#26221C;
    --rule:#342F27; --ink:#E8E0D2; --muted:#8C8275; --accent:#EE3322;
    --sans:"Jost", system-ui, sans-serif;
    --serif: Georgia, "Times New Roman", serif;
    --still:url(data:image/jpeg;base64,{still});
  }}
  * {{ box-sizing:border-box; }}
  body {{
    margin:0; background:var(--ground); color:var(--ink);
    font-family:var(--serif); font-size:17px; line-height:1.65;
    -webkit-font-smoothing:antialiased;
  }}
  .wrap {{ max-width:64rem; margin:0 auto; padding:3rem 1.25rem 6rem; }}
  .lede {{ max-width:34rem; }}
  h1 {{
    font-family:var(--sans); font-weight:700; font-size:clamp(2rem,5vw,3rem);
    line-height:1.05; letter-spacing:-.02em; margin:0 0 .75rem; text-wrap:balance;
  }}
  .kicker {{
    font-family:var(--sans); font-size:.78rem; letter-spacing:.16em;
    text-transform:uppercase; color:var(--accent); margin:0 0 1rem;
  }}
  .lede p {{ color:var(--muted); margin:0 0 .8rem; }}
  h2 {{
    font-family:var(--sans); font-weight:700; font-size:1.6rem; letter-spacing:-.01em;
    margin:0; padding-bottom:.6rem; border-bottom:1px solid var(--rule);
  }}
  .deck {{ display:flex; flex-direction:column; gap:2rem; margin-top:3.5rem; }}
  .deck > p.hint {{ color:var(--muted); font-size:.95rem; margin:0; }}
  .role {{
    background:var(--surface); border:1px solid var(--rule); border-radius:4px;
    padding:1.4rem 1.5rem 1.6rem; display:flex; flex-direction:column; gap:.9rem;
  }}
  .role-head {{ display:flex; align-items:flex-start; gap:.9rem; }}
  .role-head h3 {{ font-family:var(--sans); font-size:1.25rem; margin:0; }}
  .role-meta {{
    font-family:var(--sans); font-size:.74rem; letter-spacing:.12em;
    text-transform:uppercase; color:var(--muted); margin:.15rem 0 0;
  }}
  .swatch {{
    width:1.1rem; height:2.2rem; border-radius:2px; background:var(--c);
    flex:none; margin-top:.2rem;
  }}
  .role-note {{ margin:0; color:var(--muted); font-size:.95rem; max-width:44rem; }}
  .cands {{ list-style:none; margin:.2rem 0 0; padding:0;
    display:flex; flex-direction:column; gap:.55rem; }}
  .cand {{
    display:flex; gap:.9rem; align-items:flex-start;
    background:var(--raised); border-radius:3px; padding:.8rem .9rem;
  }}
  .num {{
    font-family:var(--sans); font-size:.95rem; color:var(--ground);
    background:var(--ink); width:1.6rem; height:1.6rem; border-radius:50%;
    display:grid; place-items:center; flex:none;
  }}
  .cand-body {{ flex:1; min-width:0; display:flex; flex-direction:column; gap:.3rem; }}
  .cand-name {{ font-family:var(--sans); font-size:1rem; margin:0; }}
  .cand-desc {{ margin:0; font-size:.9rem; color:var(--muted); }}
  audio {{ width:100%; max-width:30rem; height:2rem; margin-top:.25rem; }}
  .crole {{ display:flex; flex-direction:column; gap:.9rem; }}
  .crole h3 {{
    font-family:var(--sans); font-size:1.15rem; margin:0;
    display:flex; align-items:center; gap:.6rem;
  }}
  .tag {{
    font-size:.68rem; letter-spacing:.12em; text-transform:uppercase;
    color:var(--ground); background:var(--ink); padding:.15rem .5rem; border-radius:2px;
  }}
  .tag.locked {{ background:var(--accent); color:#fff; }}
  .tiles {{ display:flex; gap:1rem; overflow-x:auto; padding-bottom:.4rem; }}
  .tile {{ margin:0; flex:none; width:15rem; }}
  .phone {{
    position:relative; width:100%; aspect-ratio:9/16; overflow:hidden;
    border-radius:3px; border:1px solid var(--rule);
    background:#000 var(--still) center/cover no-repeat;
    display:flex; align-items:flex-end;
  }}
  .cap {{
    position:absolute; left:0; right:0; bottom:0; margin:0;
    background:rgba(0,0,0,.5); color:var(--c);
    font-family:var(--sans); font-size:.82rem; line-height:1.25;
    text-align:center; padding:.5rem 3.4%;
    text-shadow:1px 1px 0 rgba(0,0,0,.9);
  }}
  figcaption {{
    font-family:var(--sans); font-size:.8rem; color:var(--muted);
    display:flex; justify-content:space-between; gap:.5rem; padding-top:.4rem;
  }}
  figcaption b {{ color:var(--ink); }}
  code {{ font-size:.78rem; }}
  .note {{
    margin-top:3.5rem; border-left:2px solid var(--accent);
    padding:.2rem 0 .2rem 1rem; color:var(--muted); font-size:.95rem; max-width:44rem;
  }}
  :focus-visible {{ outline:2px solid var(--accent); outline-offset:2px; }}
  @media (max-width:34rem) {{ .tile {{ width:11rem; }} }}
</style>

<div class="wrap">
  <p class="kicker">Phase 1 &middot; sign-off needed</p>
  <div class="lede">
    <h1>Five voices, four colours</h1>
    <p>Every line that is not the storyteller becomes verbatim King James text
    spoken by whoever actually said it. Play each candidate and tell me the
    number you want. The storyteller keeps the voice he has — that one works.</p>
    <p>Colour specimens below use the real caption font over the brightest still
    in the library, which is the hardest case for readability.</p>
  </div>

  <div class="deck">
    <h2>The voices</h2>
    <p class="hint">Same verse inside each group, so you are comparing the voice
    and nothing else.</p>
    {''.join(rows)}
  </div>

  <div class="deck">
    <h2>The colours</h2>
    <p class="hint">Shown on <code>{still_name}</code> — the brightest bottom band
    of all 200 videos.</p>
    {''.join(swatches)}
  </div>

  <p class="note">Red stays exactly where a red-letter King James Bible prints red
  — nowhere else. Old Testament passages where Jehovah speaks go green, not red,
  because he had not yet come in the flesh. That single change moves hundreds of
  lines out of red across the library.</p>
</div>
'''
    dest = os.path.join(HERE, "audition.html")
    tmp = dest + ".tmp"
    with open(tmp, "w") as f:
        f.write(html)
    os.replace(tmp, dest)
    print(f"wrote {dest}  ({os.path.getsize(dest)/1e6:.2f} MB)  still={still_name}")


if __name__ == "__main__":
    main()
