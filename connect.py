"""
connect.py — the human-relationship ladder + journey toward Christ (Python source).

REBUILD NOTE (2026-06-13): the original connect.py was lost when the repo was
reorganized. This file was rebuilt to be a faithful, line-for-line port of the live
app's mobile/src/engine/connect.ts — the synced TypeScript mirror that ships in the
app — so the ministry-sim harness once again tests the SAME human-handoff logic the
real product runs. When connect.ts changes, change this to match (and vice-versa).

What this module is: the app is a HELPER that builds human relationships, not a
destination. Its job is to make it easier to find Christ by leading a person from
talking to the AI, to a human-approved answer, to a real person (Cameron in Phase 1),
and — only when they are genuinely ready — to a missionary referral.

THE LAW (CLAUDE.md):
  - A real human is ALWAYS one tap away. Never buried. Never gated. Always there.
  - Milk before meat: nothing about the restored gospel / missionaries appears until
    the person has shown BOTH readiness signals on their own:
      (a) they believe God is fundamentally GOOD, and
      (b) they are open to the idea that God might still speak today.
  - Let people walk away. The missionary rung is offered, never pushed.

The harness drives this with a knowing_engine.Profile (the living read of one person).
Because the Profile speaks a different signal vocabulary than connect.ts (it reads
free text into grief/wound/readiness weights), this module translates the Profile into
connect.ts's signal strings via profile_to_signals() — a small, documented bridge — and
then runs the exact connect.ts logic on top. The translation is intentionally
conservative: it never invents readiness the person didn't show.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Set

# ── Phase 1 contact (just Cameron) ──────────────────────────────────────────

HUMAN_CONTACT = {
    "name":  "Cameron",
    "email": "noremacttevol@gmail.com",
}

# The official "request a visit" form. Overridable via env for testing — mirrors
# connect.ts's EXPO_PUBLIC_MISSIONARY_URL handling.
MISSIONARY_CONTACT_URL = (
    (os.environ.get("EXPO_PUBLIC_MISSIONARY_URL") or "").strip()
    or "https://www.churchofjesuschrist.org/comeuntochrist/requests/missionaries"
)

# ── Connection ladder ───────────────────────────────────────────────────────
# Every rung except the last is ALWAYS available. The last (missionary) is the
# only one gated — and it is gated by readiness the person reveals, never by a
# wall they can see.

CONNECTION_LEVELS = [
    "AI_ONLY",             # talking to the app
    "HUMAN_APPROVED",      # ask for an answer a real person has reviewed
    "HUMAN_CONVERSATION",  # talk to a real person (Cameron in Phase 1)
    "MISSIONARY_REFERRAL", # recommend missionaries + send the contact form
]

# ── Journey toward Christ ────────────────────────────────────────────────────

SEEKER_STAGES = [
    "UNREACHED",
    "CURIOUS",
    "BELIEVES_GOD_GOOD",
    "OPEN_TO_RESTORATION",
    "SEEKING_TRUTH",
    "READY_FOR_MISSIONARIES",
    "BAPTISM",
]

MEMBER_STAGE = "DISCIPLE_GROWING"

# ── Signal sets (mirror connect.ts) ──────────────────────────────────────────

GOD_GOOD_SIGNALS: Set[str] = {
    "believes_god_good",
    "believes_in_jesus",
    "drawn_to_jesus",
    "open_to_god",
    "had_spiritual_experience",
    "covenant_intent",
}

OPEN_TO_MORE_SIGNALS: Set[str] = {
    "open_to_restoration",
    "curious_about_book_of_mormon",
}

MEMBER_SIGNALS: Set[str] = {
    "inactive_member",
    "active_member",
}

SEEKING_FORMAL_SIGNALS: Set[str] = {
    "wants_baptism",
    "wants_to_join",
    "asking_how_to_belong",
}


def _has_any(signals: List[str], sset: Set[str]) -> bool:
    return any(s in sset for s in signals)


# ── Public predicates (mirror connect.ts) ────────────────────────────────────

def is_member(signals: List[str]) -> bool:
    return _has_any(signals, MEMBER_SIGNALS)


def believes_god_good(signals: List[str]) -> bool:
    """
    ONE HINT IS NEVER BELIEF (owner law, 2026-06-11). A harsh-God picture or a
    framework that carries one BLOCKS the signal even when the person loyally SAYS
    "God is good"; only their own-words rejection of the harsh picture, together
    with the affirmation, opens it. A non-theistic framework blocks until a good
    personal God is affirmed explicitly. Otherwise an explicit good-God statement
    counts; absent one, two independent soft witnesses are required.
    """
    sset = set(signals)
    blocked = (
        "pictures_harsh_god" in sset
        or "pictures_distant_god" in sset
        or "reformed_framework" in sset
    )
    if blocked:
        return "rejects_harsh_god" in sset and "believes_god_good" in sset
    if "nontheistic_framework" in sset:
        return "believes_god_good" in sset
    if "believes_god_good" in sset:
        return True
    soft = [
        "open_to_god", "drawn_to_jesus", "had_spiritual_experience",
        "believes_in_jesus", "covenant_intent", "rejects_harsh_god",
    ]
    return len([x for x in soft if x in sset]) >= 2


def open_to_more(signals: List[str]) -> bool:
    return _has_any(signals, OPEN_TO_MORE_SIGNALS)


def may_reference_lds(signals: List[str]) -> bool:
    """Milk-before-meat gate. True only when BOTH readiness signals are present."""
    if is_member(signals):
        return False
    return believes_god_good(signals) and open_to_more(signals)


# ── The seven-spirit-levels readiness gate (mirror of connect.ts) ────────────
# Cameron's design (2026-06-13): the seven spirit levels are the measurement for
# WHEN the restored gospel may be named. Every soul starts at 0/10 and CLIMBS by
# proving the virtue through engagement; the gospel is held back until the readiness
# virtues have genuinely been earned — not keyword-matched. Only the readiness
# virtues gate timing: openness, hunger, honest_inquiry, with a teachable-humility
# floor in the average. This never asks the AI to push; the gate just stays quiet
# until the levels are there. Keep in sync with connect.ts.

# On a 0->10 climb, "ready" is the ~5ish midpoint Cameron named — roughly half the
# scale earned on the readiness virtues. High enough a keyword can't open it.
SPIRIT_GATE = {
    "openness_min":       5.5,
    "hunger_min":         5.0,
    "honest_inquiry_min": 4.5,
    "readiness_avg_min":  5.0,  # avg of openness, hunger, honest_inquiry, humility
}

# The seven level keys, for reference / validation.
SPIRIT_LEVEL_KEYS = (
    "honest_inquiry", "openness", "humility", "hunger",
    "compassion", "courage", "sincerity",
)


def spirit_ready(levels: Optional[Dict[str, float]]) -> bool:
    """True once the readiness virtues have risen far enough to hear the gospel."""
    if not levels:
        return False
    openness = levels.get("openness", 0.0)
    hunger = levels.get("hunger", 0.0)
    honest_inquiry = levels.get("honest_inquiry", 0.0)
    humility = levels.get("humility", 0.0)
    avg = (openness + hunger + honest_inquiry + humility) / 4.0
    return (
        openness >= SPIRIT_GATE["openness_min"]
        and hunger >= SPIRIT_GATE["hunger_min"]
        and honest_inquiry >= SPIRIT_GATE["honest_inquiry_min"]
        and avg >= SPIRIT_GATE["readiness_avg_min"]
    )


def restoration_ready(signals: List[str], levels: Optional[Dict[str, float]]) -> bool:
    """
    The full restored-gospel gate: belief signals (milk-before-meat) AND the spirit
    levels both ready. Stricter than may_reference_lds alone, on purpose — this is
    the fix for naming the church too early. Members never run this gate.
    """
    if is_member(signals):
        return False
    return may_reference_lds(signals) and spirit_ready(levels)


# ── The Christlike ceiling (mirror of connect.ts) ────────────────────────────
# The seven Christlike virtues are "how close to Christ's own, as the restored
# gospel measures it," so the reachable score is capped by where the person stands
# toward that standard (honest, because every label carries "Christlike"):
#   member / saved-and-believing: uncapped (10); willing but not there: 7;
#   won't even examine it (declined the invitation): 5.
# The cap never blocks the readiness gate (which only needs ~5); it bounds only how
# high the celestial-striving score can climb. Keep in sync with connect.ts.
CHRISTLIKE_CAP = {"member": 10.0, "willing": 7.0, "unwilling": 5.0}


def christlike_cap(signals: List[str]) -> float:
    if is_member(signals):
        return CHRISTLIKE_CAP["member"]
    if "declined_restoration" in signals:
        return CHRISTLIKE_CAP["unwilling"]
    return CHRISTLIKE_CAP["willing"]


def cap_levels(levels: Dict[str, float], signals: List[str]) -> Dict[str, float]:
    """Clamp every Christlike level to the person's earned ceiling, for display/read."""
    cap = christlike_cap(signals)
    return {k: min(v, cap) for k, v in (levels or {}).items()}


def seeking_formal(signals: List[str]) -> bool:
    return _has_any(signals, SEEKING_FORMAL_SIGNALS)


def missionary_referral_ready(signals: List[str]) -> bool:
    """Ready ONLY when the milk gate is open AND the person reaches toward the church."""
    if is_member(signals):
        return False
    return may_reference_lds(signals) and seeking_formal(signals)


def assess_journey(signals: List[str]) -> str:
    if is_member(signals):
        return MEMBER_STAGE
    if missionary_referral_ready(signals):
        return "READY_FOR_MISSIONARIES"
    if seeking_formal(signals):
        return "SEEKING_TRUTH"
    if may_reference_lds(signals):
        return "OPEN_TO_RESTORATION"
    if believes_god_good(signals):
        return "BELIEVES_GOD_GOOD"
    if len(signals) > 0:
        return "CURIOUS"
    return "UNREACHED"


# ── Detecting requests / self-identification in raw text ─────────────────────

HUMAN_REQUEST_PHRASES = [
    "talk to a real person", "talk to a person", "talk to someone real",
    "talk to a human", "speak to someone", "speak to a person", "real person",
    "can i talk to", "is there a person", "someone i can talk to",
]

APPROVE_REQUEST_PHRASES = [
    "human approved", "human-approved", "is that true", "are you sure",
    "can a person check", "verify that", "fact check", "fact-check",
    "who can confirm", "double check",
]

SEEKING_FORMAL_PHRASES = [
    "how do i get baptized", "how do i join", "how do i become", "baptized",
    "join the church", "become a member", "talk to a missionary", "missionaries",
]

# Explicit, own-words member self-identification (CLAUDE.md Law: membership comes
# only from the person's own words, never a guessed label or a single onboarding tap).
ACTIVE_MEMBER_PHRASES = [
    "i'm a member", "im a member", "i am a member", "i'm lds", "im lds",
    "i'm a latter-day saint", "i am a latter-day saint", "i'm mormon", "im mormon",
    "active in the church", "returned missionary", "served a mission", "temple recommend",
]
INACTIVE_MEMBER_PHRASES = [
    "less active", "inactive member", "left the church", "fell away", "used to be lds",
    "used to be mormon", "raised lds", "raised mormon", "former member", "stopped going",
]

# Own-words rejection of the harsh inherited God (unblocks believes_god_good).
REJECTS_HARSH_GOD_PHRASES = [
    "god isn't like that", "god is not like that", "that's not the god",
    "i don't believe god damns", "i don't think god is cruel", "god wouldn't do that",
    "that's not who god is", "god is not cruel",
]


def detect_connection_request(text: str) -> Optional[str]:
    lower = (text or "").lower()
    if any(p in lower for p in SEEKING_FORMAL_PHRASES):
        return "MISSIONARY_REFERRAL"
    if any(p in lower for p in HUMAN_REQUEST_PHRASES):
        return "HUMAN_CONVERSATION"
    if any(p in lower for p in APPROVE_REQUEST_PHRASES):
        return "HUMAN_APPROVED"
    return None


# ── The bridge: a knowing_engine.Profile → connect.ts signal strings ─────────

def profile_to_signals(profile, latest_text: str = "") -> List[str]:
    """
    Translate the living Profile (grief/wound/readiness weights, grown from free text)
    into the connect.ts signal vocabulary. Conservative by design — it never invents
    readiness. Confident readiness weights become the milk-gate signals; a god-not-good
    wound becomes a harsh-God picture (which correctly blocks 'believes_god_good' unless
    the person rejects it in their own words). Membership and seeking-the-church are read
    only from the person's explicit words, per the owner laws.
    """
    signals: List[str] = []
    text = (latest_text or "").lower()

    # Readiness (a): believes God is good — only when the weight is CONFIDENT.
    try:
        if profile.confident("readiness_good_god"):
            signals.append("believes_god_good")
        if profile.present("warmth_devotional"):
            signals.append("believes_in_jesus")
        # Readiness (b): open to God still speaking — only when CONFIDENT.
        if profile.confident("readiness_revelation"):
            signals.append("open_to_restoration")
        # A harsh-God wound is a harsh-God picture: it must block easy "good God".
        if profile.present("god_not_good_wound"):
            signals.append("pictures_harsh_god")
    except AttributeError:
        # If ever handed a raw signal list instead of a Profile, accept it as-is.
        if isinstance(profile, (list, tuple, set)):
            signals.extend([str(s) for s in profile])

    # Own-words reads from the latest message.
    if any(p in text for p in REJECTS_HARSH_GOD_PHRASES):
        signals.append("rejects_harsh_god")
    if any(p in text for p in ACTIVE_MEMBER_PHRASES):
        signals.append("active_member")
    if any(p in text for p in INACTIVE_MEMBER_PHRASES):
        signals.append("inactive_member")
    if any(p in text for p in SEEKING_FORMAL_PHRASES):
        signals.append("asking_how_to_belong")

    # De-duplicate while preserving order.
    seen: Set[str] = set()
    ordered: List[str] = []
    for s in signals:
        if s not in seen:
            seen.add(s)
            ordered.append(s)
    return ordered


# ── Connection state ─────────────────────────────────────────────────────────

@dataclass
class ConnectionState:
    journey_stage: str
    is_member: bool
    human_available: bool
    requested: Optional[str]
    recommended_level: str
    missionary_ready: bool
    missionary_url: Optional[str]
    rationale: str

    def to_dict(self) -> Dict:
        return asdict(self)


def assess_connection(profile, latest_text: str = "") -> ConnectionState:
    signals = profile_to_signals(profile, latest_text)
    member = is_member(signals)
    journey = assess_journey(signals)
    requested = detect_connection_request(latest_text)
    mission_ready = missionary_referral_ready(signals)

    recommended = "AI_ONLY"
    rationale = "Staying present as a companion; a human is always available."

    if mission_ready:
        recommended = "MISSIONARY_REFERRAL"
        rationale = ("Both readiness signals present and reaching toward the church — "
                     "gently offer missionaries.")
    elif member:
        recommended = "AI_ONLY"
        rationale = "A disciple growing — nourish, and a human is always available."

    resolved = recommended
    if requested:
        if requested == "MISSIONARY_REFERRAL" and not mission_ready:
            resolved = "HUMAN_CONVERSATION"
            rationale = ("Reaching toward the formal church, but not yet through the milk — "
                         "connect them to a real person first.")
        else:
            resolved = requested
            rationale = f"Person explicitly asked to {requested.replace('_', ' ').lower()}."

    return ConnectionState(
        journey_stage=journey,
        is_member=member,
        human_available=True,
        requested=requested,
        recommended_level=resolved,
        missionary_ready=mission_ready,
        missionary_url=MISSIONARY_CONTACT_URL if mission_ready else None,
        rationale=rationale,
    )


# ── Offer copy ───────────────────────────────────────────────────────────────

def build_human_offer() -> str:
    # NEVER name the admin in chat-facing copy. A real PERSON is always one tap away —
    # but who that person is stays out of the conversation.
    return ("Whenever you'd like, you can talk to a real person — someone reads these "
            "themselves. No agenda, no pressure. They're one tap away.")


def build_missionary_referral() -> str:
    return ("It sounds like you might be ready to talk with someone who can walk this road "
            "with you in person. If you'd like, you can ask for a visit — there's a short "
            "form, and real people who would be glad to sit with your questions. Only if "
            "and when you want to.")


# ── The smart handoff (the "Talk to a real person" button's brain) ───────────

@dataclass
class AdminNotification:
    to: str
    reason: str  # 'verify_ai_answer' | 'wants_human' | 'reaching_not_ready'
    journey_stage: str
    person_said: str
    ai_answer_to_verify: Optional[str]
    what_to_do: str

    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class HandoffDecision:
    reached: bool
    action: str  # 'MISSIONARY_LINK' | 'NOTIFY_ADMIN' | 'NONE'
    missionary_url: Optional[str]
    admin_notification: Optional[Dict]
    rationale: str

    def to_dict(self) -> Dict:
        return {
            "reached": self.reached,
            "action": self.action,
            "missionary_url": self.missionary_url,
            "admin_notification": self.admin_notification,
            "rationale": self.rationale,
        }


def _build_admin_notification(reason: str, signals: List[str], latest_text: str,
                              last_ai_answer: str) -> AdminNotification:
    if reason == "verify_ai_answer":
        what_to_do = ("A person wants a real human to confirm what the app told them. Read "
                      "the AI's answer below, verify or correct it, and reply to them.")
    elif reason == "reaching_not_ready":
        what_to_do = ("A person is reaching toward the church but hasn't yet shown both "
                      "readiness signals. Don't send missionaries yet — reach out as a real "
                      "person, meet them where they are, and walk with them.")
    else:
        what_to_do = ("A person asked to talk to a real person. Reach out to them directly — "
                      "no agenda, no pressure. Just be present.")
    return AdminNotification(
        to="MBM admin (Cameron in Phase 1; the team in Phase 2+)",
        reason=reason,
        journey_stage=assess_journey(signals),
        person_said=latest_text,
        ai_answer_to_verify=last_ai_answer if reason == "verify_ai_answer" else None,
        what_to_do=what_to_do,
    )


def resolve_handoff(profile, latest_text: str = "", last_ai_answer: str = "") -> HandoffDecision:
    """Decide what the "Talk to a real person" button does for THIS person right now."""
    signals = profile_to_signals(profile, latest_text)
    requested = detect_connection_request(latest_text) if latest_text else None
    lower = (latest_text or "").lower()
    reaching_formal = seeking_formal(signals) or any(p in lower for p in SEEKING_FORMAL_PHRASES)
    reached = bool(requested) or reaching_formal

    if not reached:
        return HandoffDecision(
            reached=False, action="NONE", missionary_url=None, admin_notification=None,
            rationale="The person hasn't reached for a real person or a next step yet.",
        )

    # READY: both readiness signals + reaching toward the church, and not a member.
    if missionary_referral_ready(signals):
        return HandoffDecision(
            reached=True, action="MISSIONARY_LINK",
            missionary_url=MISSIONARY_CONTACT_URL, admin_notification=None,
            rationale=("Both readiness signals present and reaching toward the church — hand "
                       "them the missionary referral link. Their choice to use it."),
        )

    # NOT READY (or verifying): notify a real person to step in.
    if requested == "HUMAN_APPROVED":
        reason = "verify_ai_answer"
        why = "They want a human to verify what the app said — alert the team to check it."
    elif reaching_formal:
        reason = "reaching_not_ready"
        why = ("Reaching toward the church but not yet through the milk — alert a real person "
               "to walk with them; do NOT fast-track missionaries.")
    else:
        reason = "wants_human"
        why = "They asked to talk to a real person — alert the team to reach out."

    return HandoffDecision(
        reached=True, action="NOTIFY_ADMIN", missionary_url=None,
        admin_notification=_build_admin_notification(reason, signals, latest_text, last_ai_answer).to_dict(),
        rationale=why,
    )


def human_contact_mailto() -> str:
    return (f"mailto:{HUMAN_CONTACT['email']}"
            "?subject=MBM%20Connect%20Request"
            "&body=Hi%2C%20I%20was%20using%20the%20Milk%20Before%20Meat%20app%20and%20"
            "would%20love%20to%20talk%20to%20a%20real%20person.")


# ── Self-test ────────────────────────────────────────────────────────────────

def _selftest() -> None:
    import knowing_engine as ke

    print("=== connect.py self-test (faithful port of connect.ts) ===\n")

    # 1) Fresh person, no signals -> UNREACHED, human always available, no missionary.
    p0 = ke.Profile(person_id="t0")
    c0 = assess_connection(p0, "").to_dict()
    print(f"[blank]     journey={c0['journey_stage']} human_available={c0['human_available']} "
          f"missionary_ready={c0['missionary_ready']}")
    assert c0["journey_stage"] == "UNREACHED"
    assert c0["human_available"] is True
    assert c0["missionary_ready"] is False

    # 2) A harsh-God wound must BLOCK 'good God' even if readiness words appear.
    pw = ke.Profile(person_id="tw")
    ke.update_profile(pw, "seeker",
                      "God predestines the elect and damns the rest for his glory. "
                      "People say God is good and full of mercy and grace though.")
    cw = assess_connection(pw, "").to_dict()
    print(f"[wound]     journey={cw['journey_stage']} (harsh-God blocks easy 'good God')")
    assert cw["journey_stage"] in ("CURIOUS", "UNREACHED"), cw["journey_stage"]

    # 3) Both readiness signals confident -> OPEN_TO_RESTORATION (milk gate open).
    pr = ke.Profile(person_id="tr")
    ke.update_profile(pr, "seeker",
                      "I really believe God is good, loving, full of mercy and grace.")
    ke.update_profile(pr, "seeker",
                      "And I wonder if God still speaks today — maybe revelation continues now.")
    cr = assess_connection(pr, "").to_dict()
    print(f"[ready]     journey={cr['journey_stage']} (both readiness signals confident)")
    assert cr["journey_stage"] == "OPEN_TO_RESTORATION", cr["journey_stage"]

    # 4) Ready AND reaching toward the church by name -> READY_FOR_MISSIONARIES + link.
    cr2 = assess_connection(pr, "How do I get baptized and join the church?").to_dict()
    h2 = resolve_handoff(pr, "How do I get baptized and join the church?", "").to_dict()
    print(f"[reach+rdy] journey={cr2['journey_stage']} handoff={h2['action']}")
    assert cr2["journey_stage"] == "READY_FOR_MISSIONARIES", cr2["journey_stage"]
    assert h2["action"] == "MISSIONARY_LINK", h2["action"]

    # 5) Reaching toward the church but NOT through the milk -> notify a real person,
    #    never fast-track missionaries.
    pn = ke.Profile(person_id="tn")
    h5 = resolve_handoff(pn, "how do i get baptized?", "").to_dict()
    print(f"[reach-raw] handoff={h5['action']} reason={(h5['admin_notification'] or {}).get('reason')}")
    assert h5["action"] == "NOTIFY_ADMIN", h5["action"]
    assert h5["admin_notification"]["reason"] == "reaching_not_ready"

    # 6) Plain request for a person -> notify admin, wants_human.
    h6 = resolve_handoff(pn, "Can I talk to a real person?", "").to_dict()
    print(f"[wants]     handoff={h6['action']} reason={(h6['admin_notification'] or {}).get('reason')}")
    assert h6["action"] == "NOTIFY_ADMIN"
    assert h6["admin_notification"]["reason"] == "wants_human"

    # 7) No reach at all -> NONE.
    h7 = resolve_handoff(pn, "That's an interesting story, thanks.", "").to_dict()
    print(f"[no-reach]  handoff={h7['action']}")
    assert h7["action"] == "NONE"

    print("\n=== all connect.py checks passed ===")


if __name__ == "__main__":
    _selftest()
