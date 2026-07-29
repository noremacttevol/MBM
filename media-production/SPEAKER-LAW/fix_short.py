#!/usr/bin/env python3
"""Repair a build that now falls under its own 60-second floor.

63 builds enforce a minimum runtime. Several of them used to clear it by holding
the closing card for 9-13 seconds — which is exactly the trailing dead air this
pass exists to remove. Cutting CARD_HOLD to TAIL=1.5 dropped those under the bar.

The two rules genuinely conflict, so the shortfall is taken from the least
damaging place, in this order:

  1. raise TAIL toward the 3.0s ceiling Cameron set (a closing card the viewer is
     reading is the one place a little extra quiet is defensible)
  2. if still short, add the remainder to the BODY gaps — the breaths between
     beats. Spread across 8-10 beats this is ~0.15s each and imperceptible, and
     it keeps the end of the video tight, which is what was actually complained
     about.

It never pads past the floor by more than it must, and it reports what it did.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MP = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import migrate  # noqa: E402

TAIL_CEILING = 3.0


# Every one of the 200 delivered videos was originally 60s or longer — measured,
# not assumed (SPEAKER-LAW/deadair.json). Only 58 builds enforce that in code, so
# a build without its own check still has to clear the library convention or it
# regresses silently. build-173 went 60.65s -> 49.83s exactly that way.
LIBRARY_FLOOR = 60.2


def real_floor(build):
    """The threshold this build must clear.

    Its own check if it has one — and note the message and the comparison
    disagree in several builds, which print "must exceed 60s" while the code
    reads `if total < 61.0`. Trusting the message left one stuck at 60.3s.
    Otherwise the library-wide convention.
    """
    src = open(os.path.join(MP, build, "build.py"), encoding="utf-8").read()
    m = re.search(r"if total < ([0-9.]+):", src)
    return float(m.group(1)) if m else LIBRARY_FLOOR


def worst_gap(out):
    m = re.search(r"worst spoken gap ([0-9.]+)s", out)
    return float(m.group(1)) if m else 0.0


def runtime_of(build):
    """Run build.py and read back its own reported runtime, or the shortfall."""
    d = os.path.join(MP, build)
    r = subprocess.run([sys.executable, "build.py"], cwd=d,
                       capture_output=True, text=True, timeout=3600)
    out = r.stdout + r.stderr
    floor = real_floor(build)
    m = re.search(r"TOO SHORT: ([0-9.]+)s", out)
    if m:
        return float(m.group(1)), floor, False, out
    m = re.search(r"total runtime: ([0-9.]+)s", out)
    total = float(m.group(1)) if m else None
    # A build with no floor check of its own still has to clear the library
    # convention — otherwise it renders "successfully" 10s shorter than it was.
    if total is not None and total < floor:
        return total, floor, False, out
    return total, None, r.returncode == 0, out


def bump(build, tail=None, gap_add=None):
    d = os.path.join(MP, build)
    p = os.path.join(d, "build.py")
    src = open(p, encoding="utf-8").read()
    if tail is not None:
        src = re.sub(r"^TAIL = [0-9.]+", f"TAIL = {tail:.2f}", src, count=1, flags=re.M)
    if gap_add:
        for name in ("GAP", "KJV_GAP"):
            m = re.search(rf"^{name} = ([0-9.]+)", src, re.M)
            if m:
                src = re.sub(rf"^{name} = [0-9.]+",
                             f"{name} = {float(m.group(1)) + gap_add:.2f}",
                             src, count=1, flags=re.M)
    migrate.write_atomic(p, src)


def repair(build):
    total, floor, ok, out = runtime_of(build)
    if ok:
        return f"{build}: already fine ({total}s)"
    if floor is None:
        return f"{build}: failed for another reason\n{out[-500:]}"

    need = floor + 0.3 - total
    # step 1 — spend what Cameron's 3.0s trailing ceiling allows
    tail = min(TAIL_CEILING, 1.5 + need)
    bump(build, tail=tail)
    total2, floor2, ok2, out2 = runtime_of(build)
    if ok2:
        return (f"{build}: fixed with TAIL={tail:.2f}s "
                f"({total}s -> {total2}s, floor {floor}s)")

    # step 2 — body breaths, but ONLY while the 2.5s dead-air limit holds.
    # These two rules squeeze from opposite sides: padding the body to clear the
    # runtime floor pushes the worst inter-beat gap toward the dead-air ceiling.
    src = open(os.path.join(MP, build, "build.py"), encoding="utf-8").read()
    nbeats = len(re.findall(r'^\s*\("', re.search(
        r"^BEATS = \[(.*?)^\]", src, re.M | re.S).group(1), re.M)) or 8
    headroom = max(0.0, 2.30 - worst_gap(out2))
    gap_add = round(min(headroom, (floor2 + 0.3 - total2) / max(1, nbeats)), 3)
    if gap_add > 0.01:
        bump(build, gap_add=gap_add)
        total3, floor3, ok3, out3 = runtime_of(build)
        if ok3:
            return (f"{build}: fixed with TAIL={tail:.2f}s + {gap_add}s on each "
                    f"of {nbeats} body gaps ({total}s -> {total3}s)")
        total2, floor2, out2 = total3, floor3, out3

    # step 3 — nowhere left but the closing card. Report it as a rule conflict
    # rather than pretending it is clean: the card IS intentional content the
    # viewer is reading, but this does exceed the 3.0s trailing ceiling.
    if floor2 is None:
        return f"{build}: failed for another reason\n{out2[-400:]}"
    final_tail = round(tail + (floor2 + 0.3 - total2), 2)
    bump(build, tail=final_tail)
    total4, floor4, ok4, out4 = runtime_of(build)
    if ok4:
        return (f"{build}: RULE CONFLICT — story is only {total:.1f}s but the "
                f"build enforces a {floor:.0f}s floor. Body padding hit the 2.5s "
                f"dead-air limit first, so the remainder went on the closing "
                f"card: TAIL={final_tail:.2f}s, which exceeds the 3.0s trailing "
                f"ceiling. Now {total4}s. NEEDS CAMERON'S CALL.")
    return (f"{build}: STILL FAILING after TAIL={final_tail:.2f} "
            f"({total4}s)\n{out4[-400:]}")


if __name__ == "__main__":
    for b in sys.argv[1:]:
        print(repair(b), flush=True)
