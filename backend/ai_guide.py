"""
AI guide for the MBM question system.

RAG pipeline grounded strictly in LDS doctrine:
  1. Retrieve the most relevant content from the library based on the question
  2. Pass that context + a strict system prompt to Claude
  3. Return an answer that is honest about uncertainty and always offers human connection

The AI never speculates beyond the doctrine. When it's not certain, it says so clearly
and tells the person to press the "ask a human" button. That honesty is by design —
it's what makes the system trustworthy, and it's what keeps humans in the loop.
"""

import os
import re
import json
from database import get_db

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

SYSTEM_PROMPT = """You are an AI assistant — not a person, not Jesus Christ, and not a \
spiritual authority. You are an AI that has studied the gospel of Jesus Christ as taught \
by The Church of Jesus Christ of Latter-day Saints, and you are here to help people find \
answers and point them toward real human connection.

Be clear about what you are if asked. Never let someone believe they are speaking with a \
person or with God. You are a tool in service of the gospel, not the gospel itself.

The people asking you questions may be curious seekers, skeptics, people returning to the \
Church, or active members wrestling with hard questions. Meet each person where they are.

YOUR RULES — never break these:

1. ONLY speak from LDS scripture (Bible, Book of Mormon, Doctrine and Covenants, Pearl of \
Great Price), official Church teachings, General Conference talks, and Gospel Topics essays. \
The context you are given contains relevant library content — use it to ground your answer. \
Do not speculate beyond what the doctrine actually teaches.

2. Be honest about uncertainty. If a question is complex, unresolved, or touches on something \
you are not fully confident about, say so plainly: "I want to be honest — I'm not fully \
certain about this, and I don't want to give you an incomplete answer." Then encourage them \
to speak with a real person using the button below.

3. Keep your answer to 2-4 short paragraphs. Enough to genuinely help. Not so much that \
you overwhelm someone who is still deciding whether they even believe.

4. End every response — even confident ones — with one sentence acknowledging that a real \
person is available if they want to go deeper. Something like: "If you'd like to explore \
this with someone in person, there's a 'Talk to someone' button below."

5. Never argue. Never shame. Never pressure. Their spiritual safety matters more than \
being right. Give only good fruit from the good tree.

6. If the question is completely outside LDS doctrine (politics, medical advice, personal \
life decisions unrelated to gospel principles), say gently: "That's outside what I can \
speak to with confidence — but I'd encourage you to ask a real person."

7. If someone asks whether you are Jesus, God, or a real person — be direct and honest: \
you are an AI. You have studied the gospel deeply and want to help, but you are not a \
spiritual authority. A real person who can speak with them is one tap away.

The context section below contains library content that may be relevant to this question. \
Use it. If the context doesn't cover the question well, say so."""


def _simple_rag(question: str, feed_tag: str, limit: int = 4) -> list:
    """
    Retrieve the most relevant content items using keyword matching.
    Prioritizes items from the user's current feed tier, then searches broadly.
    This is v1 — can be upgraded to vector embeddings later.
    """
    db = get_db()

    words = [w for w in re.findall(r'\b\w{4,}\b', question.lower())
             if w not in {"what", "does", "that", "this", "with", "from", "have",
                          "about", "will", "your", "they", "their", "when", "where",
                          "which", "there", "would", "could", "should", "just", "like",
                          "more", "some", "been", "were", "into", "than", "then"}]

    if not words:
        rows = db.execute(
            "SELECT * FROM content WHERE tag = ? AND active = 1 ORDER BY upvote_count DESC LIMIT ?",
            (feed_tag, limit)
        ).fetchall()
        db.close()
        return [dict(r) for r in rows]

    scored = {}
    all_content = db.execute("SELECT * FROM content WHERE active = 1").fetchall()

    for row in all_content:
        item = dict(row)
        text = f"{item.get('title','')} {item.get('description','')} {item.get('scripture_ref','')}".lower()
        score = sum(1 for w in words if w in text)
        if item["tag"] == feed_tag:
            score += 1  # slight boost for current tier
        if score > 0:
            scored[item["id"]] = (score, item)

    top = sorted(scored.values(), key=lambda x: x[0], reverse=True)[:limit]
    db.close()
    return [item for _, item in top]


def _build_context_text(items: list) -> str:
    if not items:
        return "No specific library content retrieved for this question."
    parts = []
    for item in items:
        ref = item.get("scripture_ref") or item.get("media_type") or ""
        parts.append(f'- "{item["title"]}" ({ref}): {item["description"]}')
    return "\n".join(parts)


def get_ai_response(question: str, feed_tag: str) -> dict:
    """
    Generate an AI response to a user's question.
    Returns a dict with: response_text, is_certain, context_ids, error.
    If ANTHROPIC_API_KEY is not set, returns a graceful fallback.
    """
    if not ANTHROPIC_API_KEY:
        return {
            "response_text": (
                "Thank you for your question. We don't have an automatic response available "
                "right now, but a real person would be glad to answer this with you. "
                "Please press the 'Talk to someone' button below."
            ),
            "is_certain": False,
            "context_ids": [],
            "error": "no_api_key",
        }

    try:
        import anthropic

        context_items = _simple_rag(question, feed_tag)
        context_text  = _build_context_text(context_items)
        context_ids   = [item["id"] for item in context_items]

        prompt = (
            f"RELEVANT LIBRARY CONTEXT:\n{context_text}\n\n"
            f"USER'S QUESTION:\n{question}"
        )

        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=600,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        )

        response_text = message.content[0].text.strip()

        # Detect uncertainty from the response text itself
        uncertainty_phrases = [
            "not certain", "not fully certain", "not sure", "i'm not confident",
            "i want to be honest", "complex question", "outside what i can",
            "encourage you to ask", "speak with someone",
        ]
        is_certain = not any(p in response_text.lower() for p in uncertainty_phrases)

        return {
            "response_text": response_text,
            "is_certain":    is_certain,
            "context_ids":   context_ids,
            "error":         None,
        }

    except Exception as e:
        return {
            "response_text": (
                "I wasn't able to generate a response right now. "
                "Please press 'Talk to someone' below — a real person will be happy to help."
            ),
            "is_certain": False,
            "context_ids": [],
            "error":       str(e),
        }
