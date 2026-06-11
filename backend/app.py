from flask import Flask, request, jsonify, render_template, session
from database import init_db, get_db
from router import (
    create_session, get_feed, get_special_cards, log_interaction,
    log_transparency_ack, log_invite_response, log_question, log_connect,
    get_bookmarks, get_next_question, log_dialogue_response, get_trait_scores,
)
from ai_guide import get_ai_response
import json
import os

app = Flask(__name__)
app.secret_key          = os.environ.get("MBM_SECRET", "mbm-dev-secret-change-in-prod")
ADMIN_PASSWORD          = os.environ.get("MBM_ADMIN_PASSWORD", "mbm-admin-dev")
# Phase 1: links to official LDS missionary referral page.
# Phase 3: replace with internal missionary chat endpoint.
MISSIONARY_REFERRAL_URL = os.environ.get(
    "MISSIONARY_REFERRAL_URL",
    "https://www.churchofjesuschrist.org/comeuntochrist/requests/missionary-visit"
)

init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/config", methods=["GET"])
def config():
    return jsonify({"missionary_referral_url": MISSIONARY_REFERRAL_URL})


@app.route("/admin")
def admin():
    if request.args.get("pw") != ADMIN_PASSWORD:
        return "Unauthorized", 401
    return render_template("admin.html", pw=request.args.get("pw"))


# ── Session ────────────────────────────────────────────────────────────────────

@app.route("/api/session/check", methods=["GET"])
def session_check():
    session_id = session.get("mbm_session")
    if not session_id:
        return jsonify({"active": False})
    db = get_db()
    row = db.execute(
        "SELECT session_id FROM user_session WHERE session_id = ?", (session_id,)
    ).fetchone()
    db.close()
    return jsonify({"active": bool(row)})


# ── Onboarding ─────────────────────────────────────────────────────────────────

@app.route("/api/onboard", methods=["POST"])
def onboard():
    data       = request.get_json()
    answer_key = data.get("answer")
    free_text  = data.get("free_text", "")

    if answer_key not in ("A", "B", "C", "D", "E"):
        return jsonify({"error": "Invalid answer key"}), 400

    session_id = create_session(answer_key, free_text)
    session["mbm_session"] = session_id
    return jsonify({"session_id": session_id})


# ── Feed ───────────────────────────────────────────────────────────────────────

@app.route("/api/feed", methods=["GET"])
def feed():
    session_id = session.get("mbm_session")
    if not session_id:
        return jsonify({"error": "No active session"}), 401
    items    = get_feed(session_id)
    special  = get_special_cards(session_id)
    question = get_next_question(session_id)
    return jsonify({"items": items, "special": special, "dialogue_question": question})


# ── Interactions ───────────────────────────────────────────────────────────────

@app.route("/api/interact", methods=["POST"])
def interact():
    data          = request.get_json()
    session_id    = session.get("mbm_session")
    content_id    = data.get("content_id")
    action        = data.get("action")
    dwell_seconds = int(data.get("dwell_seconds", 0))
    reflect_text  = data.get("reflect_text", "")

    signal_actions = {"more_depth", "keep_simple", "referral_click", "dialogue_skip"}
    valid_actions  = {
        "view", "thumbs_up", "thumbs_down", "bookmark", "share",
        "prompt_yes", "prompt_no", "prompt_reflect",
    } | signal_actions

    if not session_id or action not in valid_actions:
        return jsonify({"error": "Bad request"}), 400

    if action not in signal_actions and not content_id:
        return jsonify({"error": "content_id required"}), 400

    log_interaction(session_id, content_id, action, dwell_seconds, reflect_text)
    items    = get_feed(session_id)
    special  = get_special_cards(session_id)
    question = get_next_question(session_id)
    return jsonify({"items": items, "special": special, "dialogue_question": question})


# ── Special card acknowledgments ───────────────────────────────────────────────

@app.route("/api/transparency/ack", methods=["POST"])
def transparency_ack():
    session_id = session.get("mbm_session")
    if not session_id:
        return jsonify({"error": "No active session"}), 401
    log_transparency_ack(session_id)
    items   = get_feed(session_id)
    special = get_special_cards(session_id)
    return jsonify({"items": items, "special": special})


@app.route("/api/invite/respond", methods=["POST"])
def invite_respond():
    session_id = session.get("mbm_session")
    response   = request.get_json().get("response")
    if not session_id or response not in ("later", "decline"):
        return jsonify({"error": "Bad request"}), 400
    log_invite_response(session_id, response)
    return jsonify({"ok": True})


# ── Questions and connections ──────────────────────────────────────────────────

@app.route("/api/question", methods=["POST"])
def question():
    session_id    = session.get("mbm_session")
    question_text = (request.get_json() or {}).get("question", "").strip()
    if not session_id or not question_text:
        return jsonify({"error": "Bad request"}), 400

    question_id, feed_tag = log_question(session_id, question_text)

    ai = get_ai_response(question_text, feed_tag)

    db = get_db()
    db.execute(
        """INSERT INTO ai_response
           (question_id, session_id, question_text, feed_tag,
            response_text, is_certain, context_ids)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (question_id, session_id, question_text, feed_tag,
         ai["response_text"], 1 if ai["is_certain"] else 0,
         json.dumps(ai["context_ids"])),
    )
    db.commit()
    db.close()

    items   = get_feed(session_id)
    special = get_special_cards(session_id)
    return jsonify({
        "items":       items,
        "special":     special,
        "ai_response": {
            "response_text": ai["response_text"],
            "is_certain":    ai["is_certain"],
            "error":         ai["error"],
        },
    })


@app.route("/api/connect", methods=["POST"])
def connect():
    session_id = session.get("mbm_session")
    data       = request.get_json() or {}
    name       = data.get("name", "").strip()
    contact    = data.get("contact", "").strip()
    message    = data.get("message", "").strip()
    if not session_id or not contact:
        return jsonify({"error": "Contact required"}), 400
    log_connect(session_id, name, contact, message)
    return jsonify({"ok": True})


# ── Bookmarks ──────────────────────────────────────────────────────────────────

@app.route("/api/bookmarks", methods=["GET"])
def bookmarks():
    session_id = session.get("mbm_session")
    if not session_id:
        return jsonify({"error": "No active session"}), 401
    return jsonify({"items": get_bookmarks(session_id)})


# ── Dialogue ──────────────────────────────────────────────────────────────────

@app.route("/api/dialogue/respond", methods=["POST"])
def dialogue_respond():
    session_id   = session.get("mbm_session")
    data         = request.get_json() or {}
    question_id  = data.get("question_id")
    answer_value = data.get("answer_value", "")
    answer_text  = data.get("answer_text", "")

    if not session_id or not question_id:
        return jsonify({"error": "Bad request"}), 400

    traits   = log_dialogue_response(session_id, question_id, answer_value, answer_text)
    items    = get_feed(session_id)
    special  = get_special_cards(session_id)
    question = get_next_question(session_id)
    return jsonify({"items": items, "special": special,
                    "dialogue_question": question, "trait_scores": traits})


@app.route("/api/profile", methods=["GET"])
def user_profile():
    session_id = session.get("mbm_session")
    if not session_id:
        return jsonify({"error": "No active session"}), 401

    data = get_trait_scores(session_id)
    if not data:
        return jsonify({"error": "Session not found"}), 404

    db   = get_db()
    recent = db.execute(
        """SELECT dq.question_text, udr.answer_value, udr.answer_text
           FROM user_dialogue_response udr
           JOIN dialogue_question dq ON udr.question_id = dq.id
           WHERE udr.session_id = ?
           ORDER BY udr.responded_at DESC LIMIT 8""",
        (session_id,),
    ).fetchall()
    db.close()

    interpretation = _generate_profile_interpretation(
        data["scores"], [dict(r) for r in recent]
    )
    return jsonify({
        "trait_scores":    data["scores"],
        "track":           data["track"],
        "interpretation":  interpretation,
    })


def _generate_profile_interpretation(traits: dict, recent_answers: list) -> str:
    """Call Claude to generate an honest character interpretation."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return (
            "Your answers are being collected. "
            "An honest interpretation will appear here as the conversation continues."
        )
    try:
        import anthropic

        trait_summary = "\n".join(
            f"  {t.replace('_', ' ').title()}: {round(v, 1)}/10"
            for t, v in sorted(traits.items(), key=lambda x: -x[1])
        )
        answers_summary = "\n".join(
            f"  Q: {r['question_text']}\n  A: {r['answer_value'] or r['answer_text'] or '(no response)'}"
            for r in recent_answers[:5]
        ) or "  No answers yet."

        prompt = (
            f"Trait scores:\n{trait_summary}\n\n"
            f"Recent answers:\n{answers_summary}\n\n"
            "Write a 2–3 sentence honest interpretation of this person — "
            "in the voice of someone who sees them clearly and loves them anyway. "
            "Not flattering, not condemning. What is true about who they are right now? "
            "End with one sentence about what you sense they are actually looking for. "
            "Do not mention the trait scores directly. Do not use their name. "
            "Write as if speaking to them directly."
        )

        client  = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            system=(
                "You are writing an honest, warm character interpretation for someone "
                "engaging with a gospel-based app. You model your voice after how Jesus "
                "described people — honestly, with love, without flattery or condemnation. "
                "You are not Jesus. You are an AI doing your best to reflect someone back "
                "to themselves accurately."
            ),
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text.strip()
    except Exception:
        return (
            "Your answers are shaping a picture of who you are. "
            "Keep going — the interpretation deepens as the conversation does."
        )


# ── Admin ──────────────────────────────────────────────────────────────────────

def _require_admin():
    return request.args.get("pw") == ADMIN_PASSWORD


@app.route("/api/admin/stats", methods=["GET"])
def admin_stats():
    if not _require_admin():
        return jsonify({"error": "Unauthorized"}), 401
    db = get_db()

    total_sessions     = db.execute("SELECT COUNT(*) FROM user_session").fetchone()[0]
    total_interactions = db.execute("SELECT COUNT(*) FROM interaction_log").fetchone()[0]
    total_questions    = db.execute("SELECT COUNT(*) FROM user_question").fetchone()[0]
    total_connections  = db.execute("SELECT COUNT(*) FROM connection_request").fetchone()[0]
    avg_interactions   = db.execute("SELECT ROUND(AVG(interaction_count), 1) FROM user_session").fetchone()[0]

    tag_dist    = db.execute("SELECT feed_tag, COUNT(*) as count FROM user_session GROUP BY feed_tag").fetchall()
    action_dist = db.execute("SELECT action, COUNT(*) as count FROM interaction_log GROUP BY action ORDER BY count DESC").fetchall()
    top_content = db.execute(
        """SELECT id, tag, content_type, title, upvote_count, downvote_count, view_count,
                  ROUND(CAST(upvote_count + 1 AS FLOAT) / (upvote_count + downvote_count + 2), 3) as score
           FROM content WHERE active = 1
           ORDER BY score DESC, view_count DESC LIMIT 20"""
    ).fetchall()

    db.close()
    return jsonify({
        "total_sessions":      total_sessions,
        "total_interactions":  total_interactions,
        "total_questions":     total_questions,
        "total_connections":   total_connections,
        "avg_interactions":    avg_interactions,
        "tag_distribution":    [dict(r) for r in tag_dist],
        "action_distribution": [dict(r) for r in action_dist],
        "top_content":         [dict(r) for r in top_content],
    })


@app.route("/api/admin/questions", methods=["GET"])
def admin_questions():
    if not _require_admin():
        return jsonify({"error": "Unauthorized"}), 401
    db = get_db()
    rows = db.execute(
        "SELECT id, session_id, question_text, feed_tag, asked_at FROM user_question ORDER BY asked_at DESC LIMIT 100"
    ).fetchall()
    db.close()
    return jsonify({"questions": [dict(r) for r in rows]})


@app.route("/api/admin/connections", methods=["GET"])
def admin_connections():
    if not _require_admin():
        return jsonify({"error": "Unauthorized"}), 401
    db = get_db()
    rows = db.execute(
        "SELECT id, name, contact, message, feed_tag, created_at FROM connection_request ORDER BY created_at DESC"
    ).fetchall()
    db.close()
    return jsonify({"connections": [dict(r) for r in rows]})


@app.route("/api/admin/content", methods=["GET"])
def admin_content():
    if not _require_admin():
        return jsonify({"error": "Unauthorized"}), 401
    db = get_db()
    rows = db.execute(
        """SELECT id, tag, content_type, title, resonance_style, sequence_group, sequence_order,
                  upvote_count, downvote_count, view_count, active
           FROM content ORDER BY tag, sequence_group, sequence_order"""
    ).fetchall()
    db.close()
    return jsonify({"content": [dict(r) for r in rows]})


@app.route("/api/admin/content", methods=["POST"])
def admin_add_content():
    if not _require_admin():
        return jsonify({"error": "Unauthorized"}), 401
    data     = request.get_json()
    required = ("tag", "title", "description", "resonance_style")
    if not all(data.get(f) for f in required):
        return jsonify({"error": "Missing required fields"}), 400
    if data["tag"] not in ("MILK", "BRIDGE", "RESTORATION", "MAINTENANCE"):
        return jsonify({"error": "Invalid tag"}), 400

    db = get_db()
    db.execute(
        """INSERT INTO content
           (tag, content_type, title, description, scripture_ref, media_type, resonance_style, url,
            sequence_group, sequence_order, estimated_read_minutes)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (data["tag"], data.get("content_type", "link"), data["title"], data["description"],
         data.get("scripture_ref"), data.get("media_type", "article"),
         data["resonance_style"], data.get("url"),
         data.get("sequence_group"), data.get("sequence_order", 0),
         data.get("estimated_read_minutes", 5)),
    )
    db.commit()
    db.close()
    return jsonify({"ok": True}), 201


@app.route("/api/admin/ai_responses", methods=["GET"])
def admin_ai_responses():
    if not _require_admin():
        return jsonify({"error": "Unauthorized"}), 401
    db = get_db()
    rows = db.execute(
        """SELECT id, question_text, feed_tag, response_text, is_certain,
                  human_status, human_note, created_at
           FROM ai_response ORDER BY created_at DESC LIMIT 100"""
    ).fetchall()
    db.close()
    return jsonify({"responses": [dict(r) for r in rows]})


@app.route("/api/admin/ai/confirm", methods=["POST"])
def admin_ai_confirm():
    if not _require_admin():
        return jsonify({"error": "Unauthorized"}), 401
    data = request.get_json() or {}
    ai_id = data.get("id")
    if not ai_id:
        return jsonify({"error": "id required"}), 400
    db = get_db()
    db.execute(
        "UPDATE ai_response SET human_status = 'confirmed' WHERE id = ?", (ai_id,)
    )
    db.commit()
    db.close()
    return jsonify({"ok": True})


@app.route("/api/admin/ai/correct", methods=["POST"])
def admin_ai_correct():
    if not _require_admin():
        return jsonify({"error": "Unauthorized"}), 401
    data = request.get_json() or {}
    ai_id = data.get("id")
    note  = (data.get("note") or "").strip()
    if not ai_id or not note:
        return jsonify({"error": "id and note required"}), 400
    db = get_db()
    db.execute(
        "UPDATE ai_response SET human_status = 'corrected', human_note = ? WHERE id = ?",
        (note, ai_id),
    )
    db.commit()
    db.close()
    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(debug=True, port=5050)
