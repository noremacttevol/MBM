#!/usr/bin/env python3
"""Find where a NARRATOR segment restates an adjacent quoted (scripture/Jesus/God/
woman) segment. Heuristic: high distinctive-word overlap between a narrator line
and the quote right before/after it. These are the 'said it twice' spots."""
import ast, glob, os, re

STOP = set("the a an and or but of to in on at for with as is are was were be been being "
"that this these those he she it they them his her their you your thou thee thy ye i we us our "
"not no so then when where who whom which what how why him me my mine into unto from by up out "
"had has have will would shall should can could may might do does did done said say says saying "
"there here all any one out over under than more most very just now day come came go went made make "
"upon shall let man men god lord jesus for ever". split())

def words(t):
    return [w for w in re.findall(r"[a-z]+", t.lower()) if w not in STOP and len(w) > 2]

def load(build):
    p = os.path.join(build, "make_narration.py")
    if not os.path.exists(p): return []
    try: tree = ast.parse(open(p).read())
    except SyntaxError: return []
    segs = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(getattr(t,'id',None)=="SEGMENTS" for t in node.targets):
            if isinstance(node.value,(ast.List,ast.Tuple)):
                for elt in node.value.elts:
                    if isinstance(elt,(ast.Tuple,ast.List)) and len(elt.elts)>=3:
                        sid = elt.elts[0].value if isinstance(elt.elts[0],ast.Constant) else "?"
                        spk = elt.elts[1].id if isinstance(elt.elts[1],ast.Name) else "?"
                        txt = elt.elts[-1].value if isinstance(elt.elts[-1],ast.Constant) else ""
                        segs.append((sid,spk,txt))
    return segs

QUOTE = {"SCRIPTURE","JESUS","GOD","WOMAN"}
flagged_builds = 0; total_flags = 0; examples = []
for build in sorted(glob.glob("build-*")):
    segs = load(build)
    if not segs: continue
    hits = []
    for i,(sid,spk,txt) in enumerate(segs):
        if spk != "NARRATOR": continue
        nset = set(words(txt))
        if len(nset) < 3: continue
        for j in (i-1,i+1):
            if 0<=j<len(segs) and segs[j][1] in QUOTE:
                qset = set(words(segs[j][2]))
                if len(qset) < 3: continue
                shared = nset & qset
                ratio = len(shared)/min(len(nset),len(qset))
                if len(shared)>=3 and ratio>=0.45:
                    hits.append((sid,segs[j][0],sorted(shared),txt,segs[j][2]))
                    break
    if hits:
        flagged_builds += 1; total_flags += len(hits)
        if len(examples) < 6:
            examples.append((build,hits[0]))

print(f"builds with a likely narrator-restates-quote redundancy: {flagged_builds} / 204")
print(f"total flagged spots: {total_flags}")
print(f"avg per flagged build: {total_flags/max(flagged_builds,1):.1f}\n")
for build,(nid,qid,shared,ntxt,qtxt) in examples:
    print(f"### {build}   narrator[{nid}] echoes quote[{qid}]  shared: {', '.join(shared[:8])}")
    print(f"   QUOTE : {qtxt[:150]}")
    print(f"   NARR  : {ntxt[:150]}\n")
