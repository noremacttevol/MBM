"""
connect.py — the human-relationship ladder and the journey toward Christ.

This encodes the heart of what MBM actually is: not a destination, but a HELPER that
leads a person to Him and then hands them into real human relationships. The AI is the
first, easy door. From there the app's whole job is to move the person — only ever at
their pace and choice — toward people: a human-approved answer, a real conversation
(Cameron, in Phase 1), and finally, when they are genuinely ready and willing, a
missionary referral with a contact form to fill out.

It also measures the real journey: where the person is in becoming more Christlike, with
BAPTISM into His church as the milestone for anyone not yet a member, and ongoing
discipleship for those already baptized. These are OBSERVED milestones — we track them to
serve the person better and to learn what truly helps people come to Him. We never coerce
toward them; agency is sacred. The app leads; people and the Spirit do the converting.

This module reads the per-person Profile produced by knowing_engine.py and adds two things
the brain doesn't: the human-handoff ladder, and the journey/milestone picture.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional

import knowing_engine as ke


# ── Configurable contact points (Cameron sets these once) ───────────────────────
# Phase 1: every "talk to a person" request goes to Cameron. Phases 2/3 add a team
# and real missionaries; this is the one place to widen that without touching logic.
HUMAN_CONTACT = {
    "phase": 1,
    "name": "Cameron",
    "note": "A real person reads this and replies. Not labeled, not gated — always here.",
}

# The official missionary referral form. The app sends this link only when a person is
# ready and willing — never as a push. Set to the real URL when you have it.
MISSIONARY_CONTACT_URL = os.environ.get(
    "MBM_MISSIONARY_URL", "https://www.churchofjesuschrist.org/comeuntochrist/requests/missionaries"
)


# ── The human-relationship ladder ───────────────────────────────────────────────
# Rungs of human connection the app can bridge to. The AI is rung 0; the goal is to
# move people UP toward real humans, always by their own choosing.

CONNECTION_LEVELS = ["AI_ONLY", "HUMAN_APPROVED", "HUMAN_CONVERSATION", "MISSIONARY_REFERRAL"]

# Phrases that show a person asking to move up the ladder (read from their own words).
HUMAN_REQUEST_PHRASES = [
    "talk to a person", "talk to someone", "real person", "a human", "speak to someone",
    "can i talk to", "is there someone", "actual person", "not a bot", "not an ai",
    "who can i talk to", "i want to talk to", "connect me", "someone real",
]
APPROVE_REQUEST_PHRASES = [
    "is that true", "did a person check", "human approved", "can a person confirm",
    "verify that", "is this reviewed", "did someone write this", "fact check",
]
# A person reaching, on their own, toward formally following Christ / His church.
SEEKING_FORMAL_PHRASES = [
    "baptism", "baptized", "get baptized", "join the church", "become a member",
    "how do i follow", "what do i do next", "how do i start", "missionary", "missionaries",
    "learn more about the church", "want to know more", "how do i become", "take the next step",
    "meet with someone from the church", "i want to commit", "give my life to",
]
# A person identifying as an already-baptized Latter-day Saint (member track).
MEMBER_PHRASES = [
    "i'm a member", "im a member", "i am a member", "i'm lds", "im lds", "latter-day saint",
    "latter day saint", "returned missionary", "served a mission", "my ward", "my bishop",
    "temple recommend", "endowed", "i was baptized in the church", "active member",
    "i'm a member of the church", "my calling", "relief society", "elders quorum",
]


# ── The journey toward Christ (observed milestones, never coerced) ───────────────
# Seeker track: how far a not-yet-member has freely traveled toward Him.
SEEKER_STAGES = [
    "UNREACHED",            # no signal yet
    "CURIOUS",              # asking, leaning in
    "BELIEVES_GOD_GOOD",    # the central wound is healing: God is actually good
    "OPEN_TO_RESTORATION",  # open that God still speaks / there may be more (milk->meat opens)
    "SEEKING_TRUTH",        # actively reaching to know how to follow / about the church
    "READY_FOR_MISSIONARIES",  # ready and willing for a missionary referral
    "BAPTISM",              # the milestone — recorded as observed fruit when it happens
]
# Member track: an already-baptized disciple growing in Christ (the MAINTENANCE feed).
MEMBER_STAGES = ["DISCIPLE_GROWING"]


def _has_any(text: str, phrases: List[str]) -> bool:
    low = text.lower()
    return any(p in low for p in phrases)


def _profile_text(profile: ke.Profile) -> str:
    """All of the person's own words so far, lowercased, for scanning."""
    return " ".join(h.get("text", "") for h in profile.history if h.get("role") == "seeker").lower()


def is_member(profile: ke.Profile) -> bool:
    """Has the person identified as an already-baptized Latter-day Saint?"""
    return _has_any(_profile_text(profile), MEMBER_PHRASES)


def seeking_formal(profile: ke.Profile) -> bool:
    """Are they reaching, on their own, toward baptism / the church / missionaries?"""
    return _has_any(_profile_text(profile), SEEKING_FORMAL_PHRASES)


def assess_journey(profile: ke.Profile) -> str:
    """
    Where is this person in becoming more Christlike? Observed from their own words —
    never a label shown to them, and never something the app pushes them through.
    """
    if is_member(profile):
        return "DISCIPLE_GROWING"

    believes_good = profile.confident("readiness_good_god") or profile.present("readiness_good_god")
    open_more = profile.may_reference_lds()  # both readiness signals confident
    reaching = seeking_formal(profile)

    if open_more and reaching:
        return "READY_FOR_MISSIONARIES"
    if reaching:
        return "SEEKING_TRUTH"
    if open_more:
        return "OPEN_TO_RESTORATION"
    if believes_good:
        return "BELIEVES_GOD_GOOD"
    if profile.present("curiosity"):
        return "CURIOUS"
    return "UNREACHED"


def missionary_referral_ready(profile: ke.Profile) -> bool:
    """
    A missionary referral may be OFFERED only when both are true:
      - milk-before-meat is satisfied (they believe God is good AND are open to more), and
      - they are reaching, on their own, toward formally following Christ / His church.
    Even then it is an offer the person freely accepts — never a push. Members never get it.
    """
    if is_member(profile):
        return False
    return profile.may_reference_lds() and seeking_formal(profile)


def detect_connection_request(text: str) -> Optional[str]:
    """Read one message: is the person asking to move up the human ladder?"""
    if _has_any(text, HUMAN_REQUEST_PHRASES):
        return "HUMAN_CONVERSATION"
    if _has_any(text, APPROVE_REQUEST_PHRASES):
        return "HUMAN_APPROVED"
    return None


@dataclass
class ConnectionState:
    journey_stage: str
    is_member: bool
    human_available: bool          # ALWAYS true — a person is always one tap away
    requested: Optional[str]        # what the person asked for this turn, if anything
    recommended_level: str          # the rung the app should gently surface now
    missionary_ready: bool
    missionary_url: Optional[str]
    rationale: str

    def to_dict(self) -> Dict:
        return asdict(self)


def assess_connection(profile: ke.Profile, latest_text: str = "") -> ConnectionState:
    """
    The full read of where this person is and what human step to offer next. A real human
    is ALWAYS available; this only decides what to actively surface, by the person's own pace.
    """
    stage = assess_journey(profile)
    member = is_member(profile)
    requested = detect_connection_request(latest_text) if latest_text else None
    mission_ready = missionary_referral_ready(profile)

    if requested == "HUMAN_CONVERSATION":
        level = "HUMAN_CONVERSATION"
        why = "They asked to talk to a real person — connect them to a human (Cameron) now."
    elif requested == "HUMAN_APPROVED":
        level = "HUMAN_APPROVED"
        why = "They want a human to verify — offer a person-reviewed answer."
    elif mission_ready:
        level = "MISSIONARY_REFERRAL"
        why = ("They believe God is good, are open to more, AND are reaching toward the church — "
               "gently offer to connect them with missionaries (send the contact form). Their choice.")
    elif member:
        level = "AI_ONLY"
        why = "Already a member — nourish their discipleship; offer a person if they want one."
    else:
        level = "AI_ONLY"
        why = "Keep ministering gently; a real human stays one tap away and named when it would help."

    return ConnectionState(
        journey_stage=stage,
        is_member=member,
        human_available=True,
        requested=requested,
        recommended_level=level,
        missionary_ready=mission_ready,
        missionary_url=MISSIONARY_CONTACT_URL if level == "MISSIONARY_REFERRAL" else None,
        rationale=why,
    )


def build_human_offer() -> str:
    """A plain, warm line the app can use to surface a real person. Never gated."""
    return ("If you'd like, a real person can step in here — you can talk to someone anytime, "
            "no forms, no waiting room. Just say the word.")


def build_missionary_referral() -> str:
    """The offer surfaced ONLY when missionary_referral_ready is true. An invitation, not a push."""
    return ("It sounds like you might want to take a real next step. If you're open to it, I can "
            "connect you with people whose whole purpose is to walk with you toward Christ — "
            "missionaries who'd love to meet you, no pressure and entirely your call. "
            f"Here's where you can reach them: {MISSIONARY_CONTACT_URL}")


# ── The smart handoff (the "Talk to a real person" button's brain) ───────────────
# When a person REACHES — for a real person, for a human to verify what the AI said,
# or toward the formal next step — the app must do exactly one of two things, and
# nothing else:
#   1. If they are genuinely READY (both readiness signals + reaching toward the
#      church), hand them the missionary referral link — the door OUT of the app to
#      real ministry.
#   2. Otherwise, notify Cameron and the MBM admin team so a REAL person can step in:
#      either to talk with them, or to verify/correct what the AI told them.
# This is the whole validity metric of the app: did the person logically reach, and
# did the reach get routed to the right kind of real human help?

HANDOFF_MISSIONARY_LINK = "MISSIONARY_LINK"   # give them the referral form/link
HANDOFF_NOTIFY_ADMIN    = "NOTIFY_ADMIN"      # alert Cameron / MBM team to step in
HANDOFF_NONE            = "NONE"              # they didn't reach this turn

# Why the admin is being notified — drives what the human is asked to do.
ADMIN_REASON_VERIFY        = "verify_ai_answer"     # check/correct what the AI said
ADMIN_REASON_WANTS_HUMAN   = "wants_human"          # they asked to talk to a real person
ADMIN_REASON_REACHING_NOT_READY = "reaching_not_ready"  # reaching toward church, not yet through the milk


@dataclass
class HandoffDecision:
    reached: bool                       # did the person reach for real help this turn?
    action: str                         # one of HANDOFF_* above
    missionary_url: Optional[str]        # present only when action == MISSIONARY_LINK
    admin_notification: Optional[Dict]   # present only when action == NOTIFY_ADMIN
    rationale: str

    def to_dict(self) -> Dict:
        return asdict(self)


def _build_admin_notification(reason: str, profile: ke.Profile, latest_text: str,
                              last_ai_answer: str) -> Dict:
    """The structured alert Cameron / the MBM team receives so a real person can act."""
    stage = assess_journey(profile)
    if reason == ADMIN_REASON_VERIFY:
        what_to_do = ("A person wants a real human to confirm what the app told them. "
                      "Read the AI's answer below, verify or correct it, and reply to them.")
    elif reason == ADMIN_REASON_REACHING_NOT_READY:
        what_to_do = ("A person is reaching toward the church but hasn't yet shown both "
                      "readiness signals. Don't send missionaries yet — reach out as a real "
                      "person, meet them where they are, and walk with them.")
    else:  # ADMIN_REASON_WANTS_HUMAN
        what_to_do = ("A person asked to talk to a real person. Reach out to them directly — "
                      "no agenda, no pressure. Just be present.")
    return {
        "to": "MBM admin (Cameron in Phase 1; the team in Phase 2+)",
        "reason": reason,
        "journey_stage": stage,
        "person_said": latest_text,
        "ai_answer_to_verify": last_ai_answer if reason == ADMIN_REASON_VERIFY else None,
        "what_to_do": what_to_do,
    }


def resolve_handoff(profile: ke.Profile, latest_text: str = "",
                    last_ai_answer: str = "") -> HandoffDecision:
    """
    Decide what the "Talk to a real person" button does for THIS person, right now.

    Returns a HandoffDecision that is either:
      - MISSIONARY_LINK  (they're ready — hand them the referral form), or
      - NOTIFY_ADMIN     (alert a real person to talk to them or verify the AI), or
      - NONE             (they didn't reach for real help this turn).

    Members are never "referred" to missionaries; if a member reaches, a real person
    is still notified to be present with them.
    """
    requested = detect_connection_request(latest_text) if latest_text else None
    reaching_formal = seeking_formal(profile) or _has_any(latest_text or "", SEEKING_FORMAL_PHRASES)
    reached = bool(requested) or reaching_formal

    if not reached:
        return HandoffDecision(
            reached=False, action=HANDOFF_NONE, missionary_url=None,
            admin_notification=None,
            rationale="The person hasn't reached for a real person or a next step yet.",
        )

    # READY: both readiness signals + reaching toward the church, and not a member.
    if missionary_referral_ready(profile):
        return HandoffDecision(
            reached=True, action=HANDOFF_MISSIONARY_LINK,
            missionary_url=MISSIONARY_CONTACT_URL, admin_notification=None,
            rationale=("Both readiness signals present and reaching toward the church — "
                       "hand them the missionary referral link. Their choice to use it."),
        )

    # NOT READY (or verifying, or a member): notify a real person to step in.
    if requested == "HUMAN_APPROVED":
        reason = ADMIN_REASON_VERIFY
        why = "They want a human to verify what the app said — alert the team to check it."
    elif reaching_formal:
        reason = ADMIN_REASON_REACHING_NOT_READY
        why = ("Reaching toward the church but not yet through the milk — alert a real person "
               "to walk with them; do NOT fast-track missionaries.")
    else:
        reason = ADMIN_REASON_WANTS_HUMAN
        why = "They asked to talk to a real person — alert the team to reach out."

    return HandoffDecision(
        reached=True, action=HANDOFF_NOTIFY_ADMIN, missionary_url=None,
        admin_notification=_build_admin_notification(reason, profile, latest_text, last_ai_answer),
        rationale=why,
    )


# ── Observed milestones store (baptism + journey movement, as fruit) ─────────────
# We record real milestones when they actually happen — observed fruit, credited to God
# and the person's agency. This is measurement to serve and to learn, NOT a reward signal
# the app optimizes by manufacturing.

MILESTONES = ["first_human_conversation", "missionary_referral_sent", "baptism",
              "member_growth_step"]


@dataclass
class JourneyRecord:
    person_id: str
    stages_reached: List[str] = field(default_factory=list)
    milestones: List[Dict[str, str]] = field(default_factory=list)

    def note_stage(self, stage: str) -> None:
        if stage and (not self.stages_reached or self.stages_reached[-1] != stage):
            self.stages_reached.append(stage)

    def record_milestone(self, milestone: str, when: str = "", note: str = "") -> None:
        if milestone not in MILESTONES:
            raise ValueError(f"Unknown milestone '{milestone}'. Known: {', '.join(MILESTONES)}")
        self.milestones.append({"milestone": milestone, "when": when, "note": note})

    def to_dict(self) -> Dict:
        return asdict(self)


# ── Self-test: prove the ladder and the journey read people correctly ────────────

def _selftest() -> None:
    print("=== connect.py self-test ===\n")

    # 1) A brand-new curious seeker — early on the journey, human always available,
    #    NO missionary push.
    p = ke.Profile(person_id="seek-1")
    ke.update_profile(p, "seeker", "I'm curious, I've wondered about this but I don't really know.")
    cs = assess_connection(p, "I've wondered about all this")
    print(f"[curious]   stage={cs.journey_stage} level={cs.recommended_level} "
          f"missionary={cs.missionary_ready}")
    assert cs.journey_stage == "CURIOUS"
    assert cs.recommended_level == "AI_ONLY"
    assert cs.missionary_ready is False
    assert cs.human_available is True

    # 2) Someone asking to talk to a real person — hand to a human immediately.
    p2 = ke.Profile(person_id="seek-2")
    ke.update_profile(p2, "seeker", "Honestly can I just talk to a real person about this?")
    cs2 = assess_connection(p2, "can I just talk to a real person")
    print(f"[wants human] level={cs2.recommended_level} requested={cs2.requested}")
    assert cs2.recommended_level == "HUMAN_CONVERSATION"

    # 3) Milk-before-meat satisfied AND reaching toward the church -> missionary offer ready.
    p3 = ke.Profile(person_id="seek-3")
    ke.update_profile(p3, "seeker",
                      "I really believe God is good now, full of mercy and grace, a good father.")
    ke.update_profile(p3, "seeker",
                      "And I wonder if God still speaks today, if there's more than I was taught.")
    ke.update_profile(p3, "seeker",
                      "Honestly I think I want to get baptized and learn more about the church.")
    cs3 = assess_connection(p3, "I think I want to get baptized")
    print(f"[ready]     stage={cs3.journey_stage} level={cs3.recommended_level} "
          f"missionary={cs3.missionary_ready}\n            url={cs3.missionary_url}")
    assert cs3.journey_stage == "READY_FOR_MISSIONARIES"
    assert cs3.missionary_ready is True
    assert cs3.recommended_level == "MISSIONARY_REFERRAL"
    assert cs3.missionary_url

    # 3b) Reaching toward baptism but NOT yet believing God is good / open -> NOT ready.
    #     (We never fast-track someone past the milk.)
    p3b = ke.Profile(person_id="seek-3b")
    ke.update_profile(p3b, "seeker", "How do I get baptized? Just tell me the steps.")
    cs3b = assess_connection(p3b, "how do I get baptized")
    print(f"[premature] stage={cs3b.journey_stage} missionary={cs3b.missionary_ready}")
    assert cs3b.missionary_ready is False
    assert cs3b.journey_stage == "SEEKING_TRUTH"

    # 4) An already-baptized member -> discipleship track, never the missionary referral.
    p4 = ke.Profile(person_id="mem-1")
    ke.update_profile(p4, "seeker", "I'm a member of the church and I want to grow closer to Christ.")
    cs4 = assess_connection(p4, "I'm a member and want to grow")
    print(f"[member]    stage={cs4.journey_stage} member={cs4.is_member} "
          f"missionary={cs4.missionary_ready}")
    assert cs4.is_member is True
    assert cs4.journey_stage == "DISCIPLE_GROWING"
    assert cs4.missionary_ready is False

    # 5) Milestones: baptism is recordable as observed fruit; junk is refused.
    jr = JourneyRecord(person_id="seek-3")
    jr.note_stage("CURIOUS"); jr.note_stage("BELIEVES_GOD_GOOD"); jr.note_stage("BAPTISM")
    jr.record_milestone("baptism", when="2026-08-01", note="freely chose; God's work")
    print(f"\n[milestone] stages={jr.stages_reached}")
    print(f"            milestones={jr.milestones}")
    try:
        jr.record_milestone("converted_by_pressure")
        raise AssertionError("should reject unknown milestone")
    except ValueError:
        print("            correctly refused an unknown milestone.")

    # 6) The smart handoff button — the whole validity metric of the app.
    print("\n--- smart handoff (the 'Talk to a real person' button's brain) ---")

    # 6a) A ready person reaching toward the church -> hand them the missionary link.
    h_ready = resolve_handoff(p3, "I think I want to get baptized")
    print(f"[ready->link]   action={h_ready.action} reached={h_ready.reached} "
          f"url={'yes' if h_ready.missionary_url else 'no'}")
    assert h_ready.reached is True
    assert h_ready.action == "MISSIONARY_LINK"
    assert h_ready.missionary_url
    assert h_ready.admin_notification is None

    # 6b) Reaching toward baptism but NOT through the milk -> notify a real person, no link.
    h_premature = resolve_handoff(p3b, "how do I get baptized")
    print(f"[notready->admin] action={h_premature.action} "
          f"reason={h_premature.admin_notification['reason']}")
    assert h_premature.action == "NOTIFY_ADMIN"
    assert h_premature.missionary_url is None
    assert h_premature.admin_notification["reason"] == "reaching_not_ready"

    # 6c) Asking a human to verify what the AI said -> notify admin to check the answer.
    p6 = ke.Profile(person_id="seek-6")
    ke.update_profile(p6, "seeker", "Wait, is that true? Can a real person verify that?")
    h_verify = resolve_handoff(p6, "is that true? can a person verify that",
                               last_ai_answer="God never sends anyone to hell out of cruelty.")
    print(f"[verify->admin] action={h_verify.action} "
          f"reason={h_verify.admin_notification['reason']} "
          f"checks='{h_verify.admin_notification['ai_answer_to_verify'][:32]}...'")
    assert h_verify.action == "NOTIFY_ADMIN"
    assert h_verify.admin_notification["reason"] == "verify_ai_answer"
    assert h_verify.admin_notification["ai_answer_to_verify"]

    # 6d) Plain "can I talk to a real person" with no readiness -> notify admin to reach out.
    p7 = ke.Profile(person_id="seek-7")
    ke.update_profile(p7, "seeker", "Honestly, can I just talk to a real person?")
    h_human = resolve_handoff(p7, "can I just talk to a real person")
    print(f"[wants->admin]  action={h_human.action} reason={h_human.admin_notification['reason']}")
    assert h_human.action == "NOTIFY_ADMIN"
    assert h_human.admin_notification["reason"] == "wants_human"

    # 6e) Someone who hasn't reached at all -> no handoff fires.
    h_none = resolve_handoff(p, "I've wondered about all this")
    print(f"[no reach]      action={h_none.action} reached={h_none.reached}")
    assert h_none.action == "NONE"
    assert h_none.reached is False

    print("\n=== all checks passed ===")


if __name__ == "__main__":
    _selftest()
