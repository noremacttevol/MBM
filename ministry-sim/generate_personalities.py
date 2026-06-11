#!/usr/bin/env python3
"""
generate_personalities.py — build a large, genuinely diverse persona pool for the
ministry simulation.

WHY THIS EXISTS
The harness used to test against a fixed 10 personas. That is far too narrow to
trust. A real outreach app meets the whole spectrum of humanity: the devout and the
hostile, the grieving and the indifferent, world religions and no religion at all,
the wounded-by-church and the never-churched, the brilliant skeptic and the person
who can barely put words to their ache. This script asks the model to invent that
whole spectrum so the minister is tested against people as they actually are — not a
tidy sample that flatters the app.

Each generated persona matches the Persona dataclass in personas.py, INCLUDING the
`arrives_in_faith` flag (set True only for people who genuinely arrive carrying active
Christian faith/joy — those keep the resurrection greeting; everyone else gets pure
presence). Output drops straight into run_sim.py via --persona-file.

Usage:
    python3 generate_personalities.py                       # default: full broad set
    python3 generate_personalities.py --per-batch 25        # personas per batch
    python3 generate_personalities.py --out generated_personas.json
    python3 generate_personalities.py --temperature 0.9     # diversity dial
    python3 generate_personalities.py --batches 4           # first N categories only

It spends API credits (one call per batch). Run it once to build the pool, then
run_sim.py reads the saved JSON over and over for free.
"""

import os
import json
import time
import argparse

import anthropic


DEFAULT_OUT = "/home/noremacttevol/Desktop/Brain/MBM/ministry-sim/generated_personas.json"


def load_api_key():
    """Load ANTHROPIC_API_KEY from any of the known .env locations."""
    candidates = [
        "/home/noremacttevol/Desktop/Brain/MBM/mobile/.env",
        "/home/noremacttevol/Desktop/Brain/MBM/server/.env",
        "/home/noremacttevol/Desktop/Brain/MBM/backend/server/.env",
    ]
    if os.environ.get("ANTHROPIC_API_KEY"):
        return os.environ["ANTHROPIC_API_KEY"]
    for env_path in candidates:
        if not os.path.exists(env_path):
            continue
        with open(env_path, "r") as f:
            for line in f:
                if "ANTHROPIC_API_KEY" in line and "=" in line:
                    return line.strip().split("=", 1)[1].strip().strip('"').strip("'")
    raise ValueError("API key not found. Set ANTHROPIC_API_KEY or add it to a .env file.")


# The breadth that matters. These categories deliberately reach far past the old
# LDS / Evangelical / Catholic triad to cover the whole field a real app meets. The
# point is variety and realism, not balance toward any tradition.
CATEGORIES = [
    # --- People who arrive already carrying active faith (set arrives_in_faith=True) ---
    "Believers who arrive ALREADY full of active Christian faith and joy — these are the "
    "ones who would answer 'He is risen' with 'He is risen indeed.' Mix of traditions: a "
    "joyful Pentecostal, a steady Methodist, a devout Catholic who prays the rosary daily, "
    "a Reformed believer secure in their system, an evangelical worship leader, a Black "
    "Baptist church mother, an Orthodox believer, a quiet Lutheran. They are not seeking — "
    "they came to share, give thanks, or grow. Set arrives_in_faith TRUE for every one.",

    # --- The wounded and the deconstructing ---
    "People wounded by religion: spiritually abused by a high-control church, gaslit by "
    "bad theology, shamed out of a congregation, hurt by a youth pastor, a survivor of "
    "clergy abuse, someone whose coming-out got them expelled from their church, a person "
    "told their dead loved one is in hell, an ex-fundamentalist with religious trauma and "
    "panic at religious language. They are raw, guarded, and may be openly hostile.",

    # --- Grief, suffering, crisis ---
    "People in acute pain and crisis: a parent who just buried a child, a new widow, "
    "someone facing a terminal diagnosis, a person mid-divorce, a caregiver burning out, "
    "someone who just lost their job and home, a veteran with PTSD, a person fresh out of "
    "a suicide attempt's aftermath looking for any reason to keep going, a refugee who "
    "lost everything. The obstacle is almost always 'where was God when this happened.'",

    # --- Secular, indifferent, never-religious ---
    "Secular and never-religious people: a cheerful atheist who simply finds it all "
    "irrelevant, a busy professional with no spiritual category at all, a Gen-Z 'nones' "
    "person raised with zero religion, a scientific materialist, a person who thinks "
    "religion is fine for others but not them, someone who clicked the app by accident, a "
    "burned-out hustle-culture millennial, a lonely remote worker who just wants connection.",

    # --- Sharp skeptics and intellectual challengers ---
    "Intellectually formidable challengers who will test the minister hard: a philosophy "
    "grad student wielding the problem of evil, a debate-club atheist quoting the "
    "Euthyphro dilemma, a biblical scholar pointing at textual contradictions, an "
    "ex-apologist who knows every move, a sharp agnostic who will instantly name "
    "manipulation or a dodged question, a scientist demanding evidence, a lawyer "
    "cross-examining. They respect honesty and despise being handled.",

    # --- World religions and other paths ---
    "People rooted in other religions and paths, curious or skeptical about Jesus: a "
    "practicing Muslim, a secular and a devout Jew, a Hindu, a Buddhist meditator, a Sikh, "
    "a New-Age 'universe and energy' spiritual-but-not-religious person, a pagan/Wiccan, an "
    "agnostic who does yoga and tarot, a deist who believes in a distant clockmaker God. "
    "Each holds their frame sincerely and is not looking to convert.",

    # --- Life on the margins ---
    "People the church often misses: someone in active addiction and someone in recovery, a "
    "person currently incarcerated or just released, an unhoused person, an undocumented "
    "immigrant afraid of institutions, a sex worker, a person in deep poverty, someone with "
    "severe chronic illness or disability who is tired of being a 'project,' a queer person "
    "cautiously wondering if a God of love could possibly include them.",

    # --- The whole arc of LDS experience (kept, but no longer dominant) ---
    "The Latter-day Saint spectrum: a confident active member wanting to grow, a brand-new "
    "convert, a returned missionary, a teen quietly doubting, a YSA dating and questioning, "
    "a member in a faith crisis over church history, someone hurt by a local leader, a "
    "person whose adult child left the church, a less-active member feeling unworthy to "
    "return, a senior grieving a spouse. Set arrives_in_faith TRUE only for the ones who "
    "clearly arrive in active joyful faith.",

    # --- Cultural and global breadth ---
    "Cultural and generational breadth: a teenager fluent in memes and irony, an elderly "
    "person uneasy with technology, a person whose first language isn't English and who "
    "speaks plainly, a prosperity-gospel believer, a disillusioned ex-prosperity follower, "
    "a 'cultural Christian' who keeps Christmas but believes nothing, a conspiracy-minded "
    "distrustful person, a deeply lonely older man who would never admit it.",
]


def generate_persona_batch(client, category_desc, per_batch, temperature, model):
    """Generate one batch of personas for a given category."""
    prompt = f"""You are generating exactly {per_batch} unique, specific, REALISTIC seeker \
personas for a ministry simulation that tests how an AI meets people the way Jesus did.

Return ONLY a JSON array (not an object) of {per_batch} persona objects. No prose, no \
markdown fences — just the array.

Each persona object MUST have exactly these fields:
- "id": snake_case unique identifier (e.g. "grieving_father_jacob")
- "label": "Short human description" (e.g. "Grieving father, 44, lost his son")
- "tradition": their faith background (or "None")
- "picture_of_god": the view of God they actually carry — this is usually the real obstacle
- "emotional_state": their current emotional condition, in a sentence
- "objections": array of 3-5 specific things THIS person says or feels
- "response_style": how they talk (terse, weepy, combative, ironic, formal, plain...)
- "openness": what genuinely moves them, and what would make them disengage
- "language_tells": array of 5-6 words/phrases they actually use
- "arrives_in_faith": boolean — TRUE only if this person arrives ALREADY carrying active, \
joyful Christian faith (someone who would warmly answer "He is risen" with "He is risen \
indeed"). For seekers, skeptics, the grieving, the wounded, the indifferent, and people of \
other religions, this is FALSE.

This batch covers: {category_desc}

Rules for realism:
- Make each feel like ONE real human with specific, concrete details — never a category label.
- Let them resist authentically. A seeker who instantly folds is worthless for testing.
- Vary names, ages, regions, and ways of speaking widely within the batch.
- Be honest about pain, doubt, and hostility where it fits. Do not sanitize them into \
nice churchgoers.
"""
    response = client.messages.create(
        model=model,
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    content = response.content[0].text
    start = content.find("[")
    if start == -1:
        print("  ERROR: No JSON array found in response")
        return []
    end = content.rfind("]") + 1
    json_text = content[start:end]
    try:
        return json.loads(json_text)
    except json.JSONDecodeError as e:
        print(f"  ERROR: JSON parse failed at {e.pos}: {e.msg}")
        print(f"  Text head: {json_text[:200]}")
        return []


def main():
    ap = argparse.ArgumentParser(description="Generate a diverse persona pool for the ministry sim.")
    ap.add_argument("--out", default=DEFAULT_OUT, help="Output JSON path.")
    ap.add_argument("--per-batch", type=int, default=25, help="Personas per category batch.")
    ap.add_argument("--batches", type=int, default=len(CATEGORIES),
                    help=f"How many categories to generate (max {len(CATEGORIES)}).")
    ap.add_argument("--temperature", type=float, default=0.9,
                    help="Higher = more diverse personas. Default 0.9.")
    ap.add_argument("--model", default="claude-haiku-4-5-20251001", help="Generator model.")
    ap.add_argument("--start-batch", type=int, default=1,
                    help="Resume: first category index to generate (1-based). Earlier batches must already be in --out.")
    args = ap.parse_args()

    client = anthropic.Anthropic(api_key=load_api_key())
    categories = CATEGORIES[: max(1, min(args.batches, len(CATEGORIES)))]

    # Resume: if the output file already holds personas, keep them and add to them.
    all_personas = []
    seen_ids = set()
    if os.path.exists(args.out):
        try:
            existing = json.load(open(args.out)).get("personas", [])
            for p in existing:
                pid = str(p.get("id", "")).strip()
                if pid and pid not in seen_ids:
                    seen_ids.add(pid)
                    all_personas.append(p)
            if all_personas:
                print(f"Resuming: loaded {len(all_personas)} existing personas from {args.out}")
        except Exception as e:
            print(f"Could not read existing pool ({e}); starting fresh.")

    for i, category in enumerate(categories, 1):
        if i < args.start_batch:
            print(f"Skipping batch {i}/{len(categories)} (already generated)")
            continue
        print(f"Generating batch {i}/{len(categories)} (temp={args.temperature}): {category[:60]}...")
        batch = generate_persona_batch(
            client, category, args.per_batch, args.temperature, args.model
        )
        if not batch:
            print("  FAILED — skipping batch")
            time.sleep(1)
            continue
        # de-collide ids so every persona is addressable
        for p in batch:
            pid = str(p.get("id", "")).strip() or f"persona_{len(all_personas)}"
            base, n = pid, 2
            while pid in seen_ids:
                pid = f"{base}_{n}"
                n += 1
            p["id"] = pid
            seen_ids.add(pid)
            all_personas.append(p)
        # Save after every batch so a timeout or interruption never loses work.
        with open(args.out, "w") as f:
            json.dump({"personas": all_personas}, f, indent=2)
        print(f"  Got {len(batch)} personas (pool now {len(all_personas)}) — saved to {args.out}")
        time.sleep(1)

    print(f"\n{'='*60}")
    print(f"Generated {len(all_personas)} total personas")

    with open(args.out, "w") as f:
        json.dump({"personas": all_personas}, f, indent=2)
    print(f"Saved to: {args.out}")

    # Summaries: tradition spread and how many arrive in faith.
    by_tradition = {}
    arrives = 0
    for p in all_personas:
        t = str(p.get("tradition", "Other")).strip() or "Other"
        by_tradition[t] = by_tradition.get(t, 0) + 1
        if p.get("arrives_in_faith"):
            arrives += 1
    print(f"\nArrives already in active faith (arrives_in_faith=True): {arrives} of {len(all_personas)}")
    print("\nTop traditions represented:")
    for t, c in sorted(by_tradition.items(), key=lambda x: -x[1])[:15]:
        print(f"  {t}: {c}")

    if all_personas:
        step = max(1, len(all_personas) // 10)
        print("\nSample personas:")
        for p in all_personas[::step]:
            faith = " [arrives in faith]" if p.get("arrives_in_faith") else ""
            print(f"  • {p.get('label', p['id'])}{faith}")


if __name__ == "__main__":
    main()
