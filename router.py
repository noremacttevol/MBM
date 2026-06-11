"""
Learning router.

Every signal feeds back into the user's personal resonance profile.
Content is ranked per-user on every request. Sequences build journeys.
Special cards (transparency, invitation) appear at the right moment —
not randomly, but earned through genuine engagement.

The four tiers mirror how Jesus actually ministered:
  MILK        — Meet people where they are. No assumptions.
  BRIDGE      — Honor their questions. Give them real answers.
  RESTORATION — Introduce the specific story honestly, before asking anyone to join it.
  MAINTENANCE — Walk with those who have chosen to follow.
"""

import uuid
import json
import random
from database import get_db

ANSWER_MAP = {
    "A": {"profile": "MEMBER",   "feed_tag": "MAINTENANCE"},
    "B": {"profile": "SKEPTIC",  "feed_tag": "BRIDGE"},
    "C": {"profile": "SEEKER",   "feed_tag": "MILK"},
    "D": {"profile": "SECULAR",  "feed_tag": "MILK"},
    "E": {"profile": "UNKNOWN",  "feed_tag": "MILK"},
}

KEYWORD_SIGNALS = {
    "BRIDGE": [
        "doubt", "prove", "evidence", "impossible", "science", "logic",
        "why", "skeptic", "atheist", "question", "rational", "reason",
        "proof", "history", "facts", "research",
    ],
    "RESTORATION": [
        "restoration", "apostasy", "joseph", "authority", "original church",
        "priesthood", "1830", "prophet", "reformed", "denomination",
    ],
    "MAINTENANCE": [
        "church", "lds", "latter", "temple", "covenant", "member",
        "sacrament", "ward", "mission", "bishop", "stake", "seminary",
    ],
    "MILK": [
        "peace", "hope", "love", "feel", "good", "beautiful", "spirit",
        "god", "faith", "believe", "prayer", "comfort", "lost", "searching",
        "meaning", "purpose", "lonely",
    ],
}

FEED_PROGRESSION     = ["MILK", "BRIDGE", "RESTORATION", "MAINTENANCE"]
QUESTION_TRACKS      = ["UNBELIEVER", "INVESTIGATOR", "CALVINIST",
                        "OTHER_TRADITION", "FALLING_AWAY_LDS", "LOYAL_LDS"]
STAGE_ORDER          = {"ENTRY": 0, "EARLY": 1, "MID": 2, "DEEP": 3}

ANSWER_TO_TRACK = {
    "A": "LOYAL_LDS",
    "B": "UNBELIEVER",
    "C": "INVESTIGATOR",
    "D": "UNBELIEVER",
    "E": "INVESTIGATOR",  # overridden by NLP in create_session
}

ALL_TRAITS = [
    "honest_inquiry", "openness", "humility", "hunger",
    "compassion", "courage", "sincerity",
]
TRAIT_MIN = 0.0
TRAIT_MAX = 10.0
GRADUATION_THRESHOLD = 4
INVITE_THRESHOLD     = 8   # interactions before the invitation card appears

WEIGHT_MIN = 0.1
WEIGHT_MAX = 5.0

WEIGHT_DELTA = {
    "thumbs_up":    0.30,
    "view":         0.05,
    "bookmark":     0.20,
    "share":        0.35,
    "prompt_yes":   0.15,
    "thumbs_down": -0.20,
    "prompt_no":   -0.05,
}

DWELL_THRESHOLDS = [
    (120, 0.20),
    (60,  0.10),
    (30,  0.05),
]

ALL_STYLES = [
    "emotional", "logical", "moral", "comfort", "historical",
    "doctrinal", "foundational", "personal", "philosophical",
    "devotional", "study",
]


def _default_weights() -> dict:
    return {style: 1.0 for style in ALL_STYLES}


def _default_traits() -> dict:
    return {trait: 5.0 for trait in ALL_TRAITS}


def _text_to_question_track(text: str) -> str:
    text_lower = text.lower()
    calvinist_kw   = {"reformed", "calvinist", "predestination", "sola", "election",
                      "presbyterian", "baptist", "evangelical", "grace alone", "total depravity"}
    falling_kw     = {"used to", "left the", "no longer", "stopped going", "doubts", "shelf",
                      "ex-member", "exmo", "faith crisis", "stopped believing"}
    maintenance_kw = {"temple", "covenant", "member", "sacrament", "ward", "mission",
                      "bishop", "stake", "latter day", "lds", "church of jesus"}
    for kw in falling_kw:
        if kw in text_lower:
            return "FALLING_AWAY_LDS"
    for kw in calvinist_kw:
        if kw in text_lower:
            return "CALVINIST"
    for kw in maintenance_kw:
        if kw in text_lower:
            return "LOYAL_LDS"
    return "INVESTIGATOR"


def route_from_text(text: str) -> dict:
    text_lower = text.lower()
    scores = {tag: 0 for tag in KEYWORD_SIGNALS}
    for tag, keywords in KEYWORD_SIGNALS.items():
        for kw in keywords:
            if kw in text_lower:
                scores[tag] += 1
    best_tag = max(scores, key=scores.get)
    if scores[best_tag] == 0:
        best_tag = "MILK"
    profile_map = {
        "BRIDGE": "SKEPTIC", "RESTORATION": "SEEKER",
        "MAINTENANCE": "MEMBER", "MILK": "SEEKER",
    }
    return {"profile": profile_map.get(best_tag, "SEEKER"), "feed_tag": best_tag}


def create_session(answer_key: str, free_text: str = "") -> str:
    session_id = str(uuid.uuid4())
    if answer_key == "E" and free_text.strip():
        routing = route_from_text(free_text)
        q_track = _text_to_question_track(free_text)
    else:
        routing = ANSWER_MAP.get(answer_key, ANSWER_MAP["E"])
        q_track = ANSWER_TO_TRACK.get(answer_key, "INVESTIGATOR")

    db = get_db()
    db.execute(
        """INSERT INTO user_session
           (session_id, profile, feed_tag, resonance_weights, seen_content,
            bookmarked_content, interaction_count, onboarding_text,
            transparency_shown, invitation_shown,
            trait_scores, question_track, answered_question_ids, dialogue_signals)
           VALUES (?, ?, ?, ?, ?, ?, 0, ?, 0, 0, ?, ?, ?, ?)""",
        (session_id, routing["profile"], routing["feed_tag"],
         json.dumps(_default_weights()), json.dumps([]),
         json.dumps([]), free_text,
         json.dumps(_default_traits()), q_track, json.dumps([]), json.dumps([])),
    )
    db.commit()
    db.close()
    return session_id


# ── Scoring ────────────────────────────────────────────────────────────────────

def _global_score(item: dict) -> float:
    ups   = item.get("upvote_count", 0) or 0
    downs = item.get("downvote_count", 0) or 0
    return (ups + 1) / (ups + downs + 2)


def _sequence_boost(item: dict, recently_seen_sequences: dict) -> float:
    grp = item.get("sequence_group")
    if not grp or grp not in recently_seen_sequences:
        return 0.0
    last_order = recently_seen_sequences[grp]
    item_order = item.get("sequence_order", 0) or 0
    if item_order == last_order + 1:
        return 0.4
    return 0.0


def _score_for_user(item: dict, weights: dict, recently_seen_sequences: dict) -> float:
    style         = item.get("resonance_style") or "foundational"
    user_affinity = weights.get(style, 1.0)
    global_q      = _global_score(item)
    seq_boost     = _sequence_boost(item, recently_seen_sequences)
    noise         = random.uniform(0, 0.03)
    return user_affinity * global_q + seq_boost + noise


def _get_recent_sequences(db, session_id: str) -> dict:
    rows = db.execute(
        """SELECT c.sequence_group, MAX(c.sequence_order) as max_order
           FROM interaction_log il
           JOIN content c ON il.content_id = c.id
           WHERE il.session_id = ? AND c.sequence_group IS NOT NULL
             AND il.action IN ('view', 'thumbs_up', 'bookmark', 'share', 'prompt_yes')
           GROUP BY c.sequence_group""",
        (session_id,),
    ).fetchall()
    return {row["sequence_group"]: row["max_order"] for row in rows}


# ── Feed ───────────────────────────────────────────────────────────────────────

def get_feed(session_id: str, limit: int = 5) -> list:
    db = get_db()

    row = db.execute(
        "SELECT feed_tag, resonance_weights, seen_content FROM user_session WHERE session_id = ?",
        (session_id,),
    ).fetchone()

    if not row:
        db.close()
        return []

    feed_tag = row["feed_tag"]
    weights  = {**_default_weights(), **json.loads(row["resonance_weights"] or "{}")}
    seen_ids = set(json.loads(row["seen_content"] or "[]"))

    recently_seen_seqs = _get_recent_sequences(db, session_id)

    all_items = [
        dict(i) for i in
        db.execute("SELECT * FROM content WHERE tag = ? AND active = 1", (feed_tag,)).fetchall()
    ]

    unseen = [i for i in all_items if i["id"] not in seen_ids]
    pool   = unseen if len(unseen) >= limit else all_items

    ranked = sorted(pool, key=lambda i: _score_for_user(i, weights, recently_seen_seqs), reverse=True)
    top    = ranked[:limit]

    db.execute(
        "UPDATE user_session SET last_seen = CURRENT_TIMESTAMP WHERE session_id = ?",
        (session_id,),
    )
    db.commit()
    db.close()
    return top


def get_special_cards(session_id: str) -> dict:
    """
    Return special cards (transparency, invitation) when conditions are met.
    These are one-time moments in the user's journey — they appear when earned,
    not on every feed load.
    """
    db = get_db()
    row = db.execute(
        """SELECT feed_tag, interaction_count, transparency_shown, invitation_shown
           FROM user_session WHERE session_id = ?""",
        (session_id,),
    ).fetchone()

    if not row:
        db.close()
        return {}

    special = {}

    if row["feed_tag"] == "RESTORATION" and not row["transparency_shown"]:
        special["transparency"] = {
            "card_type":  "transparency",
            "title":      "You should know who built this.",
            "body":       (
                "This app was made by members of The Church of Jesus Christ of Latter-day Saints. "
                "We believe the content you've been reading points somewhere specific: "
                "to a restoration of Christ's original church that happened in 1830, "
                "through a young man named Joseph Smith.\n\n"
                "We didn't lead with that. We wanted to meet you where you were first. "
                "But we won't hide it from you either. "
                "What you're about to read is that story."
            ),
            "cta": "I understand — show me",
        }

    if (row["feed_tag"] in ("BRIDGE", "RESTORATION", "MAINTENANCE")
            and row["interaction_count"] >= INVITE_THRESHOLD
            and not row["invitation_shown"]):
        special["invitation"] = {
            "card_type": "invitation",
            "title":     "Would you like to talk to someone?",
            "body":      (
                "The questions you've been sitting with don't have to stay on a screen. "
                "Real people — members of The Church of Jesus Christ of Latter-day Saints — "
                "would be honored to have a conversation with you. "
                "No agenda. No pressure. Just an honest exchange."
            ),
        }

    db.close()
    return special


# ── Interactions ───────────────────────────────────────────────────────────────

def _apply_weight_delta(weights: dict, style: str, action: str, dwell_seconds: int = 0) -> dict:
    delta = WEIGHT_DELTA.get(action, 0.0)
    if action in ("view", "thumbs_up") and dwell_seconds:
        for threshold, bonus in DWELL_THRESHOLDS:
            if dwell_seconds >= threshold:
                delta += bonus
                break
    if not delta or not style:
        return weights
    current = weights.get(style, 1.0)
    weights[style] = round(max(WEIGHT_MIN, min(WEIGHT_MAX, current + delta)), 3)
    return weights


def _auto_graduate(db, session_id: str, feed_tag: str) -> str:
    if feed_tag not in FEED_PROGRESSION:
        return feed_tag
    idx = FEED_PROGRESSION.index(feed_tag)
    if idx >= len(FEED_PROGRESSION) - 1:
        return feed_tag

    count = db.execute(
        """SELECT COUNT(*) FROM interaction_log il
           JOIN content c ON il.content_id = c.id
           WHERE il.session_id = ? AND c.tag = ?
             AND il.action IN ('thumbs_up', 'bookmark', 'share', 'prompt_yes')""",
        (session_id, feed_tag),
    ).fetchone()[0]

    if count >= GRADUATION_THRESHOLD:
        next_tag = FEED_PROGRESSION[idx + 1]
        db.execute(
            "UPDATE user_session SET feed_tag = ? WHERE session_id = ?",
            (next_tag, session_id),
        )
        return next_tag
    return feed_tag


def log_interaction(session_id: str, content_id: int, action: str,
                    dwell_seconds: int = 0, reflect_text: str = ""):
    db = get_db()

    db.execute(
        """INSERT INTO interaction_log (session_id, content_id, action, dwell_seconds, reflect_text)
           VALUES (?, ?, ?, ?, ?)""",
        (session_id, content_id, action, dwell_seconds, reflect_text),
    )

    row = db.execute(
        "SELECT feed_tag, resonance_weights, seen_content, bookmarked_content FROM user_session WHERE session_id = ?",
        (session_id,),
    ).fetchone()

    if not row:
        db.commit()
        db.close()
        return

    feed_tag       = row["feed_tag"]
    weights        = {**_default_weights(), **json.loads(row["resonance_weights"] or "{}")}
    seen_ids       = json.loads(row["seen_content"] or "[]")
    bookmarked_ids = json.loads(row["bookmarked_content"] or "[]")

    resonance_style = None
    if content_id:
        content_row = db.execute(
            "SELECT resonance_style FROM content WHERE id = ?", (content_id,)
        ).fetchone()
        if content_row:
            resonance_style = content_row["resonance_style"]

        if action == "thumbs_up":
            db.execute("UPDATE content SET upvote_count = upvote_count + 1 WHERE id = ?", (content_id,))
        elif action == "thumbs_down":
            db.execute("UPDATE content SET downvote_count = downvote_count + 1 WHERE id = ?", (content_id,))
        elif action in ("view", "share"):
            db.execute("UPDATE content SET view_count = view_count + 1 WHERE id = ?", (content_id,))
            if content_id not in seen_ids:
                seen_ids.append(content_id)
        elif action == "bookmark":
            db.execute("UPDATE content SET upvote_count = upvote_count + 1 WHERE id = ?", (content_id,))
            if content_id not in bookmarked_ids:
                bookmarked_ids.append(content_id)
            if content_id not in seen_ids:
                seen_ids.append(content_id)

    weights = _apply_weight_delta(weights, resonance_style, action, dwell_seconds)

    if action == "keep_simple":
        feed_tag = "MILK"
        weights  = _default_weights()
    elif action == "more_depth":
        idx = FEED_PROGRESSION.index(feed_tag) if feed_tag in FEED_PROGRESSION else 0
        if idx < len(FEED_PROGRESSION) - 1:
            feed_tag = FEED_PROGRESSION[idx + 1]
    elif action in ("thumbs_up", "bookmark", "share", "prompt_yes"):
        feed_tag = _auto_graduate(db, session_id, feed_tag)

    db.execute(
        """UPDATE user_session SET
               resonance_weights = ?, seen_content = ?, bookmarked_content = ?,
               feed_tag = ?, interaction_count = interaction_count + 1
           WHERE session_id = ?""",
        (json.dumps(weights), json.dumps(seen_ids), json.dumps(bookmarked_ids),
         feed_tag, session_id),
    )
    db.commit()
    db.close()


def log_transparency_ack(session_id: str):
    db = get_db()
    db.execute(
        "UPDATE user_session SET transparency_shown = 1 WHERE session_id = ?", (session_id,)
    )
    db.execute(
        "INSERT INTO interaction_log (session_id, content_id, action) VALUES (?, NULL, 'transparency_ack')",
        (session_id,),
    )
    db.commit()
    db.close()


def log_invite_response(session_id: str, response: str):
    db = get_db()
    db.execute(
        "UPDATE user_session SET invitation_shown = 1 WHERE session_id = ?", (session_id,)
    )
    db.execute(
        "INSERT INTO interaction_log (session_id, content_id, action) VALUES (?, NULL, ?)",
        (session_id, f"invite_{response}"),
    )
    db.commit()
    db.close()


def log_question(session_id: str, question_text: str) -> tuple:
    """Store the user's question. Returns (question_id, feed_tag)."""
    db = get_db()
    row = db.execute(
        "SELECT feed_tag FROM user_session WHERE session_id = ?", (session_id,)
    ).fetchone()

    current_tag = row["feed_tag"] if row else "MILK"

    cursor = db.execute(
        "INSERT INTO user_question (session_id, question_text, feed_tag) VALUES (?, ?, ?)",
        (session_id, question_text, current_tag),
    )
    question_id = cursor.lastrowid

    routing = route_from_text(question_text)
    new_tag = routing["feed_tag"]
    if new_tag in FEED_PROGRESSION and current_tag in FEED_PROGRESSION:
        if FEED_PROGRESSION.index(new_tag) > FEED_PROGRESSION.index(current_tag):
            db.execute(
                "UPDATE user_session SET feed_tag = ? WHERE session_id = ?",
                (new_tag, session_id),
            )
            current_tag = new_tag

    db.execute(
        "INSERT INTO interaction_log (session_id, content_id, action, reflect_text) VALUES (?, NULL, 'question', ?)",
        (session_id, question_text),
    )
    db.commit()
    db.close()
    return (question_id, current_tag)


def log_connect(session_id: str, name: str, contact: str, message: str = ""):
    db = get_db()
    row = db.execute(
        "SELECT feed_tag FROM user_session WHERE session_id = ?", (session_id,)
    ).fetchone()
    feed_tag = row["feed_tag"] if row else None

    db.execute(
        "INSERT INTO connection_request (session_id, name, contact, message, feed_tag) VALUES (?, ?, ?, ?, ?)",
        (session_id, name, contact, message, feed_tag),
    )
    db.execute(
        "UPDATE user_session SET invitation_shown = 1 WHERE session_id = ?", (session_id,)
    )
    db.execute(
        "INSERT INTO interaction_log (session_id, content_id, action) VALUES (?, NULL, 'connect_request')",
        (session_id,),
    )
    db.commit()
    db.close()


# ── Dialogue engine ────────────────────────────────────────────────────────────

def get_next_question(session_id: str) -> dict | None:
    """Return the next question whose prerequisites the user has met, or None."""
    db = get_db()
    row = db.execute(
        "SELECT answered_question_ids, dialogue_signals, interaction_count FROM user_session WHERE session_id = ?",
        (session_id,),
    ).fetchone()

    if not row:
        db.close()
        return None

    answered_ids     = set(json.loads(row["answered_question_ids"] or "[]"))
    active_signals   = set(json.loads(row["dialogue_signals"] or "[]"))
    interaction_count = row["interaction_count"] or 0

    # Add automatic signal when they've viewed content
    if interaction_count >= 1:
        active_signals.add("viewed_content")

    all_questions = [
        dict(q) for q in db.execute(
            "SELECT * FROM dialogue_question WHERE active = 1 ORDER BY id"
        ).fetchall()
    ]
    db.close()

    def meets_prerequisites(q: dict) -> bool:
        prereqs = json.loads(q.get("prerequisite_signals") or "[]")
        if not prereqs:
            return True
        return all(p in active_signals for p in prereqs)

    eligible = [
        q for q in all_questions
        if q["id"] not in answered_ids and meets_prerequisites(q)
    ]

    if not eligible:
        return None

    eligible.sort(key=lambda q: (STAGE_ORDER.get(q["stage"], 1), q["id"]))
    return eligible[0]


def log_dialogue_response(session_id: str, question_id: int,
                          answer_value: str, answer_text: str = "") -> dict:
    """Record an answer, update trait scores, return updated scores."""
    db = get_db()

    q_row = db.execute(
        "SELECT * FROM dialogue_question WHERE id = ?", (question_id,)
    ).fetchone()
    u_row = db.execute(
        "SELECT trait_scores, answered_question_ids, dialogue_signals FROM user_session WHERE session_id = ?",
        (session_id,),
    ).fetchone()

    if not q_row or not u_row:
        db.close()
        return {}

    q               = dict(q_row)
    traits          = {**_default_traits(), **json.loads(u_row["trait_scores"] or "{}")}
    answered        = json.loads(u_row["answered_question_ids"] or "[]")
    active_signals  = set(json.loads(u_row["dialogue_signals"] or "[]"))
    answer_type     = q["answer_type"]
    deltas          = {}

    if answer_type == "SCALE":
        base = json.loads(q["trait_signals"] or "{}")
        try:
            scale_val = float(answer_value) / 10.0
        except (ValueError, TypeError):
            scale_val = 0.5
        deltas = {t: round(v * scale_val, 3) for t, v in base.items()}

    elif answer_type in ("CHOICE", "YES_NO"):
        options = json.loads(q["answer_options"] or "[]")
        for opt in options:
            if opt.get("value") == answer_value:
                deltas = opt.get("trait_signals", {})
                # Collect any signals this answer carries
                for sig in opt.get("signals", []):
                    active_signals.add(sig)
                break

    elif answer_type == "FREE_TEXT":
        base = json.loads(q["trait_signals"] or "{}")
        deltas = {t: round(v * 0.7, 3) for t, v in base.items()}
        if len(answer_text) > 120:
            deltas["sincerity"] = round(deltas.get("sincerity", 0) + 0.15, 3)

    for trait, delta in deltas.items():
        current = traits.get(trait, 5.0)
        traits[trait] = round(max(TRAIT_MIN, min(TRAIT_MAX, current + delta)), 3)

    if question_id not in answered:
        answered.append(question_id)

    db.execute(
        """INSERT INTO user_dialogue_response
           (session_id, question_id, answer_value, answer_text, trait_deltas)
           VALUES (?, ?, ?, ?, ?)""",
        (session_id, question_id, answer_value, answer_text, json.dumps(deltas)),
    )
    db.execute(
        """UPDATE user_session SET
           trait_scores = ?, answered_question_ids = ?, dialogue_signals = ?
           WHERE session_id = ?""",
        (json.dumps(traits), json.dumps(answered),
         json.dumps(list(active_signals)), session_id),
    )
    db.execute(
        "INSERT INTO interaction_log (session_id, content_id, action) VALUES (?, NULL, 'dialogue_answer')",
        (session_id,),
    )
    db.commit()
    db.close()
    return traits


def get_trait_scores(session_id: str) -> dict:
    db = get_db()
    row = db.execute(
        "SELECT trait_scores, question_track, dialogue_signals FROM user_session WHERE session_id = ?",
        (session_id,),
    ).fetchone()
    db.close()
    if not row:
        return {}
    return {
        "scores":  {**_default_traits(), **json.loads(row["trait_scores"] or "{}")},
        "track":   row["question_track"],
        "signals": json.loads(row["dialogue_signals"] or "[]"),
    }


def get_bookmarks(session_id: str) -> list:
    db = get_db()
    row = db.execute(
        "SELECT bookmarked_content FROM user_session WHERE session_id = ?", (session_id,)
    ).fetchone()
    if not row:
        db.close()
        return []
    ids = json.loads(row["bookmarked_content"] or "[]")
    if not ids:
        db.close()
        return []
    placeholders = ",".join("?" * len(ids))
    items = db.execute(
        f"SELECT * FROM content WHERE id IN ({placeholders})", ids
    ).fetchall()
    db.close()
    return [dict(i) for i in items]
