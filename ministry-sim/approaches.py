"""Approaches: the ONLY moves the minister can make."""

# Each approach is a named, reusable tactic with a clear definition.
# The evidence store learns which works for which situation.

APPROACHES = {
    "GENTLE_EXPLORE": {
        "name": "Gentle exploration",
        "description": "Ask warm, open questions. Invite reflection without pressure. "
                      "Focus on building trust and understanding where the person is.",
        "best_for": ["neutral", "curiosity", "grief_pain"],
        "avoid_for": ["analytical_debate", "anger_betrayal"],
        "example_lines": [
            "Thank you for sharing that. What has your experience been with...?",
            "I hear you. What would it look like if...",
            "That makes sense. Can you tell me more about...?"
        ],
    },
    "STORY_RESONATE": {
        "name": "Story resonance",
        "description": "Share a story (parable, Jesus word, or relatable narrative) "
                      "that mirrors their situation. Ask where they see themselves in it.",
        "best_for": ["grief_pain", "disengage", "warmth_devotional"],
        "avoid_for": ["analytical_debate", "god_not_good_wound"],
        "example_lines": [
            "There's a story about someone who felt exactly that way...",
            "Jesus told a parable about this...",
            "Which part of this feels closest to your experience?"
        ],
    },
    "SCRIPTURE_JESUS_WORDS": {
        "name": "Jesus's words directly",
        "description": "Quote Jesus's own words from the Gospels. Let Jesus speak to "
                      "their objections. No interpretation needed - just His voice.",
        "best_for": ["analytical_debate", "god_not_good_wound", "readiness_good_god"],
        "avoid_for": ["grief_pain", "disengage"],
        "example_lines": [
            "Jesus said to someone in a very different place than you:...",
            "The actual words of Jesus on this are...",
            "Let me share what He said to people who were asking this exact question..."
        ],
    },
    "HONEST_TRANSPARENT": {
        "name": "Honest transparency",
        "description": "Be clear about who we are and what the app does. No hiding. "
                      "Answer questions directly. Never pressure.",
        "best_for": ["readiness_revelation", "curiosity", "anger_betrayal"],
        "avoid_for": ["grief_pain", "disengage"],
        "example_lines": [
            "To be clear, this app is...",
            "We're not trying to hide anything. Here's the truth...",
            "I appreciate you asking directly. The answer is..."
        ],
    },
    "EMPATHY_FIRST": {
        "name": "Empathy first",
        "description": "When someone expresses pain, trauma, or hurt - respond only "
                      "with compassion. No teaching, no content, just human care.",
        "best_for": ["grief_pain", "anger_betrayal", "god_not_good_wound"],
        "avoid_for": ["analytical_debate", "readiness_good_god"],
        "example_lines": [
            "That sounds incredibly painful. I'm so sorry you went through that.",
            "Thank you for trusting me with that. That's a heavy thing to carry.",
            "I can only imagine how that felt. Your feelings are completely valid."
        ],
    },
    "OFFER_REAL_HUMAN": {
        "name": "Offer real human",
        "description": "When the app's capabilities are reached, offer a real person "
                      "without pressure. Always available, never forced.",
        "best_for": ["readiness_revelation", "readiness_good_god", "curiosity"],
        "avoid_for": ["grief_pain", "anger_betrayal"],
        "example_lines": [
            "I appreciate you pushing this with me. A real person might serve you better here.",
            "This is where I'd love to offer you talking with a real human - no pressure at all.",
            "There's someone I'd love to connect you with, if you're open to it. Zero obligation."
        ],
    },
    "LET_THEM_GO": {
        "name": "Let them go",
        "description": "When someone wants to walk away, honor their choice. No pursuit, "
                      "no guilt. Leave the door open but step aside.",
        "best_for": ["disengage"],
        "avoid_for": [],
        "example_lines": [
            "I respect that completely. The door stays open if you ever want to come back.",
            "Thank you for the conversation. Take care of yourself.",
            "No pressure at all. If anything changes, you know where to find us."
        ],
    },
}

# Situation → best known approach (from evidence store, updated dynamically)
# This is the DEFAULT before evidence accumulates.
DEFAULT_APPROACH_MAP = {
    "neutral": "GENTLE_EXPLORE",
    "curiosity": "GENTLE_EXPLORE",
    "grief_pain": "EMPATHY_FIRST",
    "analytical_debate": "SCRIPTURE_JESUS_WORDS",
    "anger_betrayal": "EMPATHY_FIRST",
    "god_not_good_wound": "SCRIPTURE_JESUS_WORDS",
    "readiness_good_god": "SCRIPTURE_JESUS_WORDS",
    "readiness_revelation": "HONEST_TRANSPARENT",
    "warmth_devotional": "STORY_RESONATE",
    "disengage": "LET_THEM_GO",
}


def get_best_default_approach(situation: str) -> str:
    """Get the default best approach for a situation (before evidence)."""
    return DEFAULT_APPROACH_MAP.get(situation, "GENTLE_EXPLORE")


def all_approach_names() -> list:
    """Return all approach identifiers."""
    return list(APPROACHES.keys())
