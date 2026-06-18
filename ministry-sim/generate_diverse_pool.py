#!/usr/bin/env python3
"""
Fast persona generator: makes many SMALL parallel calls instead of one giant call.
Each call generates 3 personas. 10 parallel workers × 9 categories × 3 each = 270 personas.
Cheap, fast, never times out.

Usage:
    python3 generate_diverse_pool.py --out generated_personas_v2.json --workers 10
"""
import json
import os
import sys
import time
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import anthropic

HERE = Path("/home/noremacttevol/Desktop/Brain/MBM/ministry-sim")


def load_api_key():
    candidates = [
        "/home/noremacttevol/Desktop/Brain/MBM/mobile/.env",
        "/home/noremacttevol/Desktop/Brain/MBM/server/.env",
    ]
    if os.environ.get("ANTHROPIC_API_KEY"):
        return os.environ["ANTHROPIC_API_KEY"]
    for env_path in candidates:
        if not os.path.exists(env_path):
            continue
        with open(env_path) as f:
            for line in f:
                if "ANTHROPIC_API_KEY" in line and "=" in line:
                    return line.strip().split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError("ANTHROPIC_API_KEY not found")


# Categories + per-call descriptors — each generates 3 distinct personas
CATEGORY_PROMPTS = [
    ("faithful_christian", "A joyful Pentecostal worship leader, 34, woman; a steady Methodist small-group leader, 58, man; a devout Catholic grandmother, 71, woman who prays the rosary daily."),
    ("wounded_religion", "A woman, 41, expelled from her church for divorce and publicly shamed; a man, 45, whose pastor gaslit the congregation after embezzling funds; a woman, 26, who left a high-control cult with her children."),
    ("grief_crisis", "A new widow, 52, whose husband died three weeks ago; a father, 44, who just buried his teenage son; a woman, 38, diagnosed with terminal cancer, asking where God is."),
    ("secular_neverchurched", "A Gen-Z 'nones' person, 22, raised with zero religion; a busy software engineer, 35, who finds religion irrelevant; a cheerful atheist, 48, who simply isn't convinced."),
    ("intellectual_skeptic", "A philosophy grad student, 27, wielding the Euthyphro dilemma; a biblical scholar, 55, pointing at textual contradictions; a debate-club atheist, 31, who will name any manipulation instantly."),
    ("world_religions", "A practicing Muslim woman, 36, curious about Jesus; a secular Jew, 44, who keeps high holidays; a Buddhist meditator, 39, who finds Christian claims interesting but incomplete; a Hindu IT worker, 29, raised in Mumbai."),
    ("church_margins", "A person in addiction recovery, 45, looking for meaning; a queer college student, 21, wondering if a loving God could include them; a unhoused veteran, 57, who lost everything; a person with chronic illness, 33, tired of being a project."),
    ("lds_spectrum", "An active Latter-day Saint mother, 39, wanting to deepen her conversion; a returned missionary, 26, in a faith crisis over church history; a less-active member, 48, feeling unworthy to return; a teenager, 17, quietly doubting."),
    ("cultural_breadth", "A Black church mother, 68, whose faith is the center of her life; a conspiracy-minded person, 51, who distrusts all institutions; a prosperity-gospel believer, 44, whose faith collapsed when hardship hit; an elderly man, 74, who would never admit how lonely he is."),
    ("exchristian_deconstructing", "A former evangelical, 33, whose faith fell apart after reading church history; a burned-out ex-pastor, 46, now openly agnostic; someone told their daughter is in hell, 58, and can never forgive God; a person who had a traumatic experience with religious hypocrisy, 29."),
    ("seeking_curious", "A person, 40, who keeps feeling drawn to church but is afraid of the community; a dad, 36, who lost his job and wonders if anyone will help; a person, 54, who always wanted to believe but never felt they could; a spiritual-but-not-religious yoga instructor, 31, who finds the Jesus story compelling."),
]


PER_CALL = 3  # personas per API call
WORKERS = 10  # parallel API calls


def generate_one_batch(client, category_label, persona_descriptions, model):
    """Generate PER_CALL personas from a short text description."""
    prompt = f"""Generate {PER_CALL} unique, realistic seeker personas for a ministry simulation.

Return ONLY a JSON array of {PER_CALL} objects. No prose, no markdown fences.

Personas to generate (vary age, gender, region, specific details freely):
{persona_descriptions}

Each object MUST have exactly these fields:
- "id": snake_case unique id (e.g. "grieving_mother_julia")
- "label": short human description with age (e.g. "Grieving mother, 42, lost her son")
- "tradition": their faith background or "None"
- "picture_of_god": the view of God they actually carry — usually the real obstacle
- "emotional_state": their current emotional condition in one sentence
- "objections": array of 3-4 specific things THIS person says or feels
- "response_style": how they talk (terse, weepy, combative, ironic, plain, formal...)
- "openness": what genuinely moves them, and what makes them disengage
- "language_tells": array of 5-6 words/phrases they actually use
- "arrives_in_faith": boolean — TRUE only for people who arrive ALREADY carrying active, joyful Christian faith (they answer "He is risen" with warmth). For seekers, skeptics, grieving, wounded, indifferent: FALSE."""
    try:
        resp = client.messages.create(
            model=model,
            max_tokens=4000,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.95,
        )
        content = resp.content[0].text
        start = content.find("[")
        if start == -1:
            return []
        end = content.rfind("]") + 1
        return json.loads(content[start:end])
    except Exception as e:
        print(f"    ERROR {category_label}: {e}")
        return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "generated_personas_v2.json"))
    ap.add_argument("--workers", type=int, default=WORKERS)
    ap.add_argument("--model", default="claude-haiku-4-5-20251001")
    args = ap.parse_args()

    client = anthropic.Anthropic(api_key=load_api_key())

    # Load existing personas to avoid duplicates
    existing_ids = set()
    existing = []
    if os.path.exists(args.out):
        try:
            existing = json.load(open(args.out)).get("personas", [])
            for p in existing:
                if p.get("id"):
                    existing_ids.add(p["id"])
            print(f"Loaded {len(existing)} existing personas from {args.out}")
        except Exception:
            pass

    calls = []
    for cat_label, cat_desc in CATEGORY_PROMPTS:
        calls.append((cat_label, cat_desc))

    all_personas = list(existing)
    seen_ids = set(existing_ids)

    print(f"Generating ~{len(calls) * PER_CALL} personas across {len(calls)} categories, "
          f"{PER_CALL} per call, {args.workers} workers...")

    done = 0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = {
            ex.submit(generate_one_batch, client, cat_label, cat_desc, args.model): cat_label
            for cat_label, cat_desc in calls
        }
        for fut in as_completed(futures):
            cat_label = futures[fut]
            try:
                batch = fut.result()
            except Exception as e:
                print(f"  FAIL {cat_label}: {e}")
                continue

            for p in batch:
                pid = str(p.get("id", "")).strip() or f"persona_{len(all_personas)}"
                base = pid
                n = 2
                while pid in seen_ids:
                    pid = f"{base}_{n}"
                    n += 1
                p["id"] = pid
                seen_ids.add(pid)
                all_personas.append(p)

            done += 1
            print(f"  [{done}/{len(calls)}] {cat_label}: +{len(batch)} personas "
                  f"(pool now {len(all_personas)})")

    # Save
    with open(args.out, "w") as f:
        json.dump({"personas": all_personas}, f, indent=2)

    print(f"\nTotal: {len(all_personas)} personas saved to {args.out}")

    # Summary
    by_trad = {}
    arrives = 0
    for p in all_personas:
        t = p.get("tradition", "Other") or "Other"
        by_trad[t] = by_trad.get(t, 0) + 1
        if p.get("arrives_in_faith"):
            arrives += 1
    print(f"Arrives_in_faith: {arrives}")
    print("Top traditions:")
    for t, c in sorted(by_trad.items(), key=lambda x: -x[1])[:15]:
        print(f"  {t}: {c}")


if __name__ == "__main__":
    main()
