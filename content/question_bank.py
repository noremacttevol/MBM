"""
Dialogue question bank.

Every question here is something Jesus would actually ask someone —
written in the spirit of love paying attention, not theology sorting people.

The sequence:
  1. Universal entry questions — warm, anyone can answer honestly,
     no assumptions about what they believe. These reveal who someone is
     without making them feel tested.
  2. Signal-based follow-up questions — unlocked when the person's answers
     have revealed something specific. These deepen the conversation the
     person is already having, not a new one.

The rule behind every question:
  Jesus asked questions FOR the person — to help them hear themselves,
  to invite them to arrive at something true on their own.
  He was never gathering data. He was paying attention.

Questions appear AFTER content — a piece of content creates a feeling,
then a question invites them to name it. The question always follows
an experience. Never cold.

Signals — accumulated from answers, unlock follow-up questions:
  had_spiritual_experience     — something unexplained felt real
  has_history_with_faith       — there's a faith story in their past
  skeptical_of_god             — currently doubtful or disbelieving
  open_to_god                  — God feels warm or plausible
  hurt_by_church               — wounded by an institution or its people
  hurt_by_faith                — the gospel itself has caused pain
  prayed_before                — has done something like prayer
  has_afterlife_belief         — has a framework for what happens after death
  believes_in_moral_truth      — believes in objective right and wrong
  drawn_to_jesus               — feels something toward Jesus personally
  believes_in_jesus            — Jesus is real and significant to them
  skeptical_of_jesus           — doubtful of the Jesus narrative
  doubting_doctrine            — doctrinal questions, not just people
  viewed_content               — has engaged with at least one content item
  carries_grief                — processing loss or death
  struggles_with_habits        — wrestling with addictive or destructive patterns
  family_faith_tension         — family dynamics and faith are in conflict
  searching_for_purpose        — explicitly wants meaning, not just answers
  lonely                       — longing for real community and connection
  open_to_scripture            — curious about reading the Gospels or scripture
  believes_prayer_works        — felt something when they prayed
  open_to_restoration          — open to the idea that God may speak today
  curious_about_book_of_mormon — asked about or is open to the Book of Mormon
  inactive_member              — was LDS, has stepped back
  losing_faith                 — active member whose faith is slipping
  intellectual_doubts          — has specific doctrinal or historical questions
"""

import json


def _opts(*options):
    return json.dumps(list(options))


def _opt(text, value, signals=None, **traits):
    o = {"text": text, "value": value, "trait_signals": traits}
    if signals:
        o["signals"] = signals
    return o


def _sig(**traits):
    return json.dumps(traits)


QUESTION_BANK = [

    # ══════════════════════════════════════════════════════════════════
    # UNIVERSAL ENTRY — Everyone starts here.
    # Warm. Anyone can answer honestly. No wrong answers.
    # These reveal who someone is without making them feel assessed.
    # ══════════════════════════════════════════════════════════════════

    {
        "track": "ANY", "stage": "ENTRY", "topic": "worth_living",
        "question_text": "What's one thing that makes life feel worth it to you — even on the hard days?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(sincerity=0.3, hunger=0.2),
        "prerequisite_signals": "[]",
        "jesus_reference": "John 10:10 — I came that they may have life, and have it abundantly.",
    },
    {
        "track": "ANY", "stage": "ENTRY", "topic": "unseen",
        "question_text": "Have you ever had a moment — a place, a person, something you can't quite explain — that made you feel like there's more to this world than what you can see?",
        "answer_type": "YES_NO",
        "answer_options": _opts(
            _opt("Yes — something has felt real to me that I can't fully explain.",
                 "yes", signals=["had_spiritual_experience"],
                 openness=0.35, honest_inquiry=0.2, hunger=0.2),
            _opt("Not that I can point to.",
                 "no",
                 honest_inquiry=0.25),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "John 3:8 — The wind blows where it wishes. You hear its sound but cannot tell where it comes from.",
    },
    {
        "track": "ANY", "stage": "ENTRY", "topic": "burden",
        "question_text": "What's the heaviest thing you're carrying right now that you wish you could put down?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(courage=0.3, sincerity=0.3, hunger=0.2),
        "prerequisite_signals": "[]",
        "jesus_reference": "Matthew 11:28 — Come to me, all who are weary and burdened, and I will give you rest.",
    },
    {
        "track": "ANY", "stage": "ENTRY", "topic": "god_feeling",
        "question_text": "When you hear the word 'God' — what's the first feeling that comes up? Not what you think. What you feel.",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("Something warm — like coming home.", "warm",
                 signals=["open_to_god"],
                 openness=0.3, hunger=0.25, sincerity=0.2),
            _opt("Complicated — there's history there.", "complicated",
                 signals=["has_history_with_faith"],
                 honest_inquiry=0.3, courage=0.25, humility=0.2),
            _opt("Distant — like it doesn't apply to me.", "distant",
                 honest_inquiry=0.25, openness=0.15),
            _opt("Skeptical — I'm not sure there's anything there.", "skeptical",
                 signals=["skeptical_of_god"],
                 honest_inquiry=0.35, courage=0.2),
            _opt("Honestly — I don't know what I feel.", "unknown",
                 honest_inquiry=0.25, humility=0.2, openness=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "John 4:23 — The Father is seeking people who will worship him in spirit and in truth.",
    },
    {
        "track": "ANY", "stage": "ENTRY", "topic": "unseen_good",
        "question_text": "What's something good you've done recently that nobody noticed?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(sincerity=0.35, compassion=0.3, humility=0.2),
        "prerequisite_signals": "[]",
        "jesus_reference": "Matthew 6:3-4 — When you give to the needy, do not let your left hand know what your right hand is doing.",
    },

    # ══════════════════════════════════════════════════════════════════
    # FEELING QUESTIONS — Appear after specific content items.
    # These tie the question to what the person just experienced.
    # The question invites them to name what the content stirred.
    # ══════════════════════════════════════════════════════════════════

    {
        "track": "ANY", "stage": "EARLY", "topic": "after_content",
        "question_text": "That piece you just read — what did it stir in you? Even if it's hard to name.",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(sincerity=0.3, honest_inquiry=0.2, hunger=0.15),
        "prerequisite_signals": '["viewed_content"]',
        "jesus_reference": "Luke 24:32 — Were not our hearts burning within us while he talked with us?",
    },
    {
        "track": "ANY", "stage": "EARLY", "topic": "resonance",
        "question_text": "Is there a part of what you've been reading here that keeps coming back to you — something that won't quite leave?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(hunger=0.3, sincerity=0.25, openness=0.2),
        "prerequisite_signals": '["viewed_content"]',
        "jesus_reference": "John 6:68 — Lord, to whom shall we go? You have words of eternal life.",
    },

    # ══════════════════════════════════════════════════════════════════
    # EARLY — After entry questions have revealed something.
    # Still warm. Gently going deeper.
    # ══════════════════════════════════════════════════════════════════

    {
        "track": "ANY", "stage": "EARLY", "topic": "prayer",
        "question_text": "Have you ever said something out loud — or in your head — that was kind of a prayer, even if you weren't sure anyone was listening?",
        "answer_type": "YES_NO",
        "answer_options": _opts(
            _opt("Yes — I've done something like that.",
                 "yes", signals=["prayed_before"],
                 openness=0.3, sincerity=0.25, hunger=0.2),
            _opt("No — that's not something I've done.",
                 "no",
                 honest_inquiry=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "Luke 11:2 — When you pray, say: Father...",
    },
    {
        "track": "ANY", "stage": "EARLY", "topic": "afterlife",
        "question_text": "What do you think happens after you die? You don't have to have a certain answer — what do you actually think?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("Nothing — consciousness ends and that's it.",
                 "nothing",
                 honest_inquiry=0.3),
            _opt("Something — but I genuinely don't know what.",
                 "something_unknown",
                 honest_inquiry=0.2, hunger=0.2, openness=0.2),
            _opt("Something I believe in — I have a framework for this.",
                 "have_belief",
                 signals=["has_afterlife_belief"],
                 sincerity=0.25, openness=0.15),
            _opt("I try not to think about it.",
                 "avoid",
                 honest_inquiry=0.2, hunger=0.1),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "John 11:25 — I am the resurrection and the life. Whoever believes in me, though he die, yet shall he live.",
    },
    {
        "track": "ANY", "stage": "EARLY", "topic": "goodness",
        "question_text": "Do you think there's such a thing as genuine goodness — something that's actually right, not just what most people agree on?",
        "answer_type": "YES_NO",
        "answer_options": _opts(
            _opt("Yes — some things are actually right or wrong, not just opinions.",
                 "yes", signals=["believes_in_moral_truth"],
                 honest_inquiry=0.2, humility=0.15, openness=0.15),
            _opt("No — right and wrong are just what we agree on collectively.",
                 "no",
                 honest_inquiry=0.25),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "Mark 10:18 — Why do you call me good? No one is good except God alone.",
    },
    {
        "track": "ANY", "stage": "EARLY", "topic": "longing",
        "question_text": "Is there something you've been looking for — in relationships, in work, in life — that you haven't found yet?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(hunger=0.35, sincerity=0.3, courage=0.2),
        "prerequisite_signals": "[]",
        "jesus_reference": "John 1:38 — What are you seeking? The first question Jesus asked anyone.",
    },
    {
        "track": "ANY", "stage": "EARLY", "topic": "grief",
        "question_text": "Have you lost someone — or something — that left a hole you haven't been able to fill?",
        "answer_type": "YES_NO",
        "answer_options": _opts(
            _opt("Yes — I'm still carrying that.",
                 "yes", signals=["carries_grief"],
                 sincerity=0.35, courage=0.3, hunger=0.2),
            _opt("Not in a way that's still affecting me.",
                 "no",
                 honest_inquiry=0.15),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "John 11:35 — Jesus wept. The shortest verse. The most human.",
    },
    {
        "track": "ANY", "stage": "EARLY", "topic": "habits",
        "question_text": "Is there anything in your life right now that you keep going back to — that you know isn't good for you, but you can't seem to put down?",
        "answer_type": "YES_NO",
        "answer_options": _opts(
            _opt("Yes — there's something like that in my life.",
                 "yes", signals=["struggles_with_habits"],
                 courage=0.35, sincerity=0.3, humility=0.2),
            _opt("Not really — that's not where I'm at.",
                 "no",
                 honest_inquiry=0.15),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "John 8:36 — If the Son sets you free, you will be free indeed.",
    },
    {
        "track": "ANY", "stage": "EARLY", "topic": "community",
        "question_text": "Do you have people in your life who actually know you — not just the version you show at work or online?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("Yes — I have a few people like that.",
                 "yes",
                 sincerity=0.2, compassion=0.15),
            _opt("Sort of — but even they don't see the whole picture.",
                 "partial",
                 sincerity=0.25, hunger=0.15),
            _opt("Not really — it's lonelier than it looks.",
                 "no", signals=["lonely"],
                 hunger=0.3, sincerity=0.3, courage=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "John 15:15 — I no longer call you servants. I have called you friends.",
    },
    {
        "track": "ANY", "stage": "EARLY", "topic": "purpose",
        "question_text": "Do you ever get the feeling that your life is supposed to mean something specific — that there's a purpose you haven't quite found yet?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("Yes — I feel that pull strongly.",
                 "yes_strong", signals=["searching_for_purpose"],
                 hunger=0.35, sincerity=0.25, openness=0.2),
            _opt("Sometimes — it comes and goes.",
                 "sometimes", signals=["searching_for_purpose"],
                 hunger=0.2, openness=0.15),
            _opt("Not really — I think we make our own meaning.",
                 "no",
                 honest_inquiry=0.25),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "John 17:4 — I have glorified you on earth, having accomplished the work you gave me to do.",
    },
    {
        "track": "ANY", "stage": "EARLY", "topic": "family_faith",
        "question_text": "Did you grow up in a home that had faith in it — and is the relationship you have with that now the same or different?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("Yes — and I'm still in the same place as I grew up.",
                 "same",
                 sincerity=0.2),
            _opt("Yes — but I've moved away from it.",
                 "moved_away", signals=["has_history_with_faith", "family_faith_tension"],
                 honest_inquiry=0.25, courage=0.2),
            _opt("Yes — and I've actually gone deeper than my upbringing.",
                 "deeper",
                 hunger=0.3, sincerity=0.25),
            _opt("No — I wasn't raised in faith.",
                 "no_faith_upbringing",
                 honest_inquiry=0.2, openness=0.15),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "Luke 2:49 — Did you not know that I must be in my Father's house?",
    },
    {
        "track": "ANY", "stage": "EARLY", "topic": "pain_response",
        "question_text": "When life gets really hard — what's your first instinct? Where do you go, or what do you do?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("I isolate and go inward.",
                 "isolate",
                 courage=0.15, sincerity=0.2),
            _opt("I talk to someone I trust.",
                 "talk",
                 compassion=0.2, sincerity=0.2),
            _opt("I distract myself — keep moving, don't think.",
                 "distract",
                 honest_inquiry=0.2),
            _opt("I look for something bigger than myself — prayer, nature, anything.",
                 "transcendent", signals=["open_to_god"],
                 openness=0.3, hunger=0.25, sincerity=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "Mark 1:35 — Very early in the morning, while it was still dark, Jesus got up, left the house, and prayed.",
    },

    # ══════════════════════════════════════════════════════════════════
    # MID — For people who've been engaging genuinely.
    # Deeper. Still warm. The question earns its depth by coming late.
    # ══════════════════════════════════════════════════════════════════

    {
        "track": "ANY", "stage": "MID", "topic": "jesus_feeling",
        "question_text": "When you hear about Jesus — not the religion, just the person — what do you feel toward him?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("Something draws me toward him — I'm not sure why.",
                 "drawn",
                 signals=["drawn_to_jesus"],
                 openness=0.35, hunger=0.3, sincerity=0.2),
            _opt("I respect him but keep my distance.",
                 "respect_distance",
                 honest_inquiry=0.25, openness=0.15),
            _opt("I love him — he's real to me.",
                 "love",
                 signals=["believes_in_jesus"],
                 sincerity=0.35, hunger=0.2, courage=0.2),
            _opt("I'm skeptical of the whole story.",
                 "skeptical",
                 signals=["skeptical_of_jesus"],
                 honest_inquiry=0.35, courage=0.2),
            _opt("I used to feel something, but that's complicated now.",
                 "complicated",
                 signals=["has_history_with_faith", "hurt_by_faith"],
                 honest_inquiry=0.3, courage=0.3, humility=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "Matthew 16:15 — But who do YOU say I am?",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "forgiveness",
        "question_text": "Is there someone in your life you've never fully forgiven — or something you haven't forgiven yourself for?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(courage=0.35, sincerity=0.35, compassion=0.2),
        "prerequisite_signals": "[]",
        "jesus_reference": "Matthew 18:21-22 — How many times shall I forgive? Not seven, but seventy times seven.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "change",
        "question_text": "Is there a version of yourself you want to become — someone you can picture but haven't fully stepped into yet?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(hunger=0.35, courage=0.25, humility=0.2),
        "prerequisite_signals": "[]",
        "jesus_reference": "John 1:42 — You are Simon. You will be called Peter. Jesus named what someone could become.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "love_received",
        "question_text": "What's the most loved you've ever felt by another person — and what made it feel real?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(sincerity=0.3, compassion=0.25, hunger=0.2),
        "prerequisite_signals": "[]",
        "jesus_reference": "John 15:13 — Greater love has no one than this: to lay down one's life for one's friends.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "trust",
        "question_text": "Is there something you believe in deeply — but feel like you can't say out loud without people judging you for it?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(courage=0.4, sincerity=0.35, honest_inquiry=0.2),
        "prerequisite_signals": "[]",
        "jesus_reference": "John 7:13 — No one would speak openly about him for fear of the Jewish leaders.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "scripture_openness",
        "question_text": "Have you ever actually read the Gospels for yourself — not what someone told you they said, but read them directly?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("Yes — and they've stayed with me.",
                 "yes_stayed", signals=["open_to_scripture"],
                 hunger=0.3, openness=0.25, sincerity=0.2),
            _opt("A little — some parts, not all of it.",
                 "partial", signals=["open_to_scripture"],
                 openness=0.2, honest_inquiry=0.2),
            _opt("No — I haven't gotten there.",
                 "no",
                 honest_inquiry=0.2),
            _opt("I've tried but found it hard to connect with.",
                 "tried_failed",
                 honest_inquiry=0.25, openness=0.15),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "Luke 4:17 — He opened the scroll and found the place where it was written.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "identity_source",
        "question_text": "When everything else is stripped away — what's left that you know for certain about who you are?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(sincerity=0.4, courage=0.3, humility=0.25),
        "prerequisite_signals": "[]",
        "jesus_reference": "Matthew 3:17 — A voice from heaven said: This is my Son, whom I love. Identity spoken before the work began.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "sacrifice",
        "question_text": "Is there something you'd give up everything for — something you'd sacrifice significantly to protect or pursue?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(courage=0.35, sincerity=0.3, compassion=0.25),
        "prerequisite_signals": "[]",
        "jesus_reference": "Matthew 13:46 — When he found one pearl of great value, he went and sold everything he had and bought it.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "doubt_honest",
        "question_text": "What do you most wish you could believe, but honestly can't get yourself to believe right now?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(honest_inquiry=0.4, courage=0.35, humility=0.3),
        "prerequisite_signals": "[]",
        "jesus_reference": "Mark 9:24 — I believe. Help my unbelief.",
    },

    # ══════════════════════════════════════════════════════════════════
    # SIGNAL-BASED FOLLOW-UPS
    # Only appear when earlier answers have signaled something specific.
    # ══════════════════════════════════════════════════════════════════

    # For people who said God feels "complicated" or who have faith history
    {
        "track": "ANY", "stage": "MID", "topic": "what_happened",
        "question_text": "It sounds like there's some history with faith for you. Would you be willing to say — what happened?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(honest_inquiry=0.3, courage=0.35, sincerity=0.3),
        "prerequisite_signals": '["has_history_with_faith"]',
        "jesus_reference": "John 21:17 — Peter, do you love me? Jesus asked three times — not to shame him, but to make space.",
    },
    # For people hurt by faith or church
    {
        "track": "ANY", "stage": "MID", "topic": "hurt_by_faith",
        "question_text": "Has a church, or someone in a church, ever hurt you or let you down in a serious way?",
        "answer_type": "YES_NO",
        "answer_options": _opts(
            _opt("Yes — and I haven't fully resolved it.",
                 "yes_unresolved",
                 signals=["hurt_by_church"],
                 honest_inquiry=0.25, courage=0.35, sincerity=0.2),
            _opt("Yes — but I've made peace with it.",
                 "yes_resolved",
                 courage=0.2, humility=0.2, sincerity=0.2),
            _opt("No — that hasn't been my experience.",
                 "no",
                 honest_inquiry=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["has_history_with_faith"]',
        "jesus_reference": "Luke 15:4 — What person, having a hundred sheep and losing one, does not go after the one?",
    },
    # For people who signaled they're hurt by church — separate the institution from the gospel
    {
        "track": "ANY", "stage": "MID", "topic": "institution_vs_gospel",
        "question_text": "Is it the people — or the institution — that hurt you? Or has the doubt gone deeper, into the actual beliefs?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("Mostly the people — the institution failed me, not the gospel.",
                 "people",
                 honest_inquiry=0.25, sincerity=0.2),
            _opt("The institution itself — how it operated.",
                 "institution",
                 honest_inquiry=0.3, courage=0.25),
            _opt("It's gone deeper — I've started doubting what I believed.",
                 "doctrine",
                 signals=["doubting_doctrine"],
                 honest_inquiry=0.35, courage=0.3, humility=0.2),
            _opt("All of it — it collapsed together.",
                 "all",
                 honest_inquiry=0.3, courage=0.35, humility=0.15),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["hurt_by_church"]',
        "jesus_reference": "John 6:67-68 — Will you also go away? To whom shall we go? You have words of eternal life.",
    },
    # For people who had a genuine spiritual experience
    {
        "track": "ANY", "stage": "EARLY", "topic": "spiritual_experience_depth",
        "question_text": "That experience you mentioned — the one you couldn't explain — did it change something in you, or did you set it aside?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("It changed something — I've never fully explained it but I know it mattered.",
                 "changed",
                 openness=0.35, hunger=0.3, sincerity=0.25),
            _opt("I've thought about it but I'm still not sure what it means.",
                 "unsure",
                 honest_inquiry=0.3, openness=0.2, humility=0.2),
            _opt("I set it aside — it felt too big to sit with.",
                 "set_aside",
                 honest_inquiry=0.25, courage=0.2, hunger=0.15),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["had_spiritual_experience"]',
        "jesus_reference": "Luke 24:32 — Did not our hearts burn within us while he talked with us on the road?",
    },
    # For skeptics — honor the skepticism before going deeper
    {
        "track": "ANY", "stage": "MID", "topic": "skeptic_honest",
        "question_text": "What would have to be true for you to take the idea of God seriously — even just as a question worth asking?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(honest_inquiry=0.35, courage=0.25, openness=0.2),
        "prerequisite_signals": '["skeptical_of_god"]',
        "jesus_reference": "Acts 17:23 — I even found an altar with the inscription: TO AN UNKNOWN GOD. Paul started where they were.",
    },
    # For people who believe in Jesus
    {
        "track": "ANY", "stage": "MID", "topic": "believer_depth",
        "question_text": "If Jesus is who you believe he is — is there a part of what he taught that you've found hard to actually live?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(honest_inquiry=0.3, courage=0.35, humility=0.3),
        "prerequisite_signals": '["believes_in_jesus"]',
        "jesus_reference": "John 6:60 — This is a hard teaching. Who can accept it?",
    },
    # For people drawn to Jesus — the identity question, earned now
    {
        "track": "ANY", "stage": "DEEP", "topic": "who_is_jesus",
        "question_text": "Jesus said 'I am the way, the truth, and the life.' Of those three — way, truth, life — which one do you most need from him right now?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("The way — I don't know what direction to go.",
                 "way",
                 hunger=0.3, humility=0.25, openness=0.2),
            _opt("The truth — I have too many unanswered questions.",
                 "truth",
                 honest_inquiry=0.35, hunger=0.25, courage=0.2),
            _opt("The life — I'm tired of just going through the motions.",
                 "life",
                 hunger=0.35, sincerity=0.3, courage=0.2),
            _opt("Honestly, all three.",
                 "all",
                 hunger=0.3, sincerity=0.25, humility=0.2, openness=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["drawn_to_jesus"]',
        "jesus_reference": "John 14:6 — I am the way, the truth, and the life.",
    },
    # For people who are lonely
    {
        "track": "ANY", "stage": "MID", "topic": "loneliness_depth",
        "question_text": "That loneliness you carry — when does it hit the hardest? Is there a specific moment of the day or week when it's loudest?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(courage=0.35, sincerity=0.35, hunger=0.25),
        "prerequisite_signals": '["lonely"]',
        "jesus_reference": "Matthew 26:40 — Could you not keep watch with me for one hour?",
    },
    # For people carrying grief
    {
        "track": "ANY", "stage": "MID", "topic": "grief_and_god",
        "question_text": "Did losing them — or losing that — change the way you think about God? Or was it God you were already angry at?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("Yes — it shook my faith or turned me away.",
                 "shook_faith", signals=["hurt_by_faith"],
                 honest_inquiry=0.3, courage=0.3, sincerity=0.2),
            _opt("It actually drew me closer — pain sent me looking.",
                 "drew_closer", signals=["open_to_god", "had_spiritual_experience"],
                 openness=0.3, hunger=0.25, sincerity=0.2),
            _opt("I don't connect the two — loss is just loss.",
                 "separate",
                 honest_inquiry=0.25),
            _opt("I'm honestly still working through it.",
                 "working_through",
                 courage=0.3, sincerity=0.3, humility=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["carries_grief"]',
        "jesus_reference": "John 11:33 — When Jesus saw her weeping, he was deeply moved in spirit and troubled.",
    },
    # For people wrestling with habits
    {
        "track": "ANY", "stage": "MID", "topic": "habit_root",
        "question_text": "If you could be totally honest — what need is that habit actually filling? What's it doing for you that nothing else does?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(honest_inquiry=0.4, courage=0.35, humility=0.3),
        "prerequisite_signals": '["struggles_with_habits"]',
        "jesus_reference": "John 4:13 — Everyone who drinks this water will be thirsty again.",
    },
    # For people with family faith tension
    {
        "track": "ANY", "stage": "MID", "topic": "family_faith_gap",
        "question_text": "Is the gap between you and your family's faith a source of pain — or something that feels like freedom?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("Pain — there's a distance it's created that I don't love.",
                 "pain",
                 sincerity=0.3, courage=0.25, hunger=0.2),
            _opt("Freedom — I feel more honest now than I did.",
                 "freedom",
                 honest_inquiry=0.3, courage=0.3),
            _opt("Both — it's complicated.",
                 "both",
                 honest_inquiry=0.25, sincerity=0.25, courage=0.2),
            _opt("I've found a middle ground that works.",
                 "middle_ground",
                 humility=0.2, sincerity=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["family_faith_tension"]',
        "jesus_reference": "Luke 12:53 — Father against son, mother against daughter. Jesus was honest about what following him costs.",
    },
    # For people searching for purpose
    {
        "track": "ANY", "stage": "MID", "topic": "purpose_specific",
        "question_text": "When you imagine a life that feels fully meaningful — what does it actually look like? Not the Instagram version. The real one.",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(hunger=0.4, sincerity=0.35, courage=0.2),
        "prerequisite_signals": '["searching_for_purpose"]',
        "jesus_reference": "John 10:10 — I came that they may have life and have it abundantly.",
    },

    # ══════════════════════════════════════════════════════════════════
    # PRAYER PATHWAY — For people who've prayed or are open to it.
    # ══════════════════════════════════════════════════════════════════

    {
        "track": "ANY", "stage": "MID", "topic": "prayer_felt",
        "question_text": "That time you prayed — or something close to it — did anything come back? A feeling, a thought, a quiet? Anything at all?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("Yes — something came, even if I don't know what it was.",
                 "yes", signals=["believes_prayer_works", "had_spiritual_experience"],
                 openness=0.35, hunger=0.3, sincerity=0.25),
            _opt("Nothing I could identify — it felt like talking to the ceiling.",
                 "nothing",
                 honest_inquiry=0.3, humility=0.2),
            _opt("I didn't stay long enough to notice.",
                 "left_early",
                 honest_inquiry=0.2, hunger=0.15),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["prayed_before"]',
        "jesus_reference": "Matthew 6:6 — When you pray, go into your room and shut the door. Pray to your Father who is in secret.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "prayer_willingness",
        "question_text": "Would you be willing to try something? Tonight — or whenever it feels right — just sit quietly and say whatever's actually on your mind, like you're talking to someone who already knows everything about you.",
        "answer_type": "YES_NO",
        "answer_options": _opts(
            _opt("Yes — I think I could try that.",
                 "yes", signals=["open_to_god"],
                 openness=0.35, hunger=0.25, courage=0.2),
            _opt("I'm not sure — it would feel strange.",
                 "unsure",
                 honest_inquiry=0.2, openness=0.15),
            _opt("No — I don't think that's for me.",
                 "no",
                 honest_inquiry=0.3),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["prayed_before"]',
        "jesus_reference": "Luke 18:1 — He told them a parable about the need to always pray and not give up.",
    },

    # ══════════════════════════════════════════════════════════════════
    # SCRIPTURE PATHWAY — For people who've read or are curious about it.
    # ══════════════════════════════════════════════════════════════════

    {
        "track": "ANY", "stage": "MID", "topic": "jesus_teaching_that_hit",
        "question_text": "Of everything Jesus is recorded as teaching — the Sermon on the Mount, the parables, 'love your enemies' — which one sits with you, even if you're not sure what to do with it?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(hunger=0.3, openness=0.25, honest_inquiry=0.2),
        "prerequisite_signals": '["open_to_scripture"]',
        "jesus_reference": "Matthew 7:28 — When Jesus had finished these words, the crowds were amazed at his teaching.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "resurrection_honest",
        "question_text": "The resurrection — that Jesus literally rose from the dead — what do you do with that claim? Ignore it, dismiss it, or has it ever made you think?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("It's made me think — I can't fully dismiss it.",
                 "think", signals=["drawn_to_jesus", "open_to_scripture"],
                 honest_inquiry=0.35, hunger=0.3, openness=0.25),
            _opt("I believe it — it's the center of everything.",
                 "believe", signals=["believes_in_jesus"],
                 sincerity=0.35, hunger=0.25, courage=0.2),
            _opt("I find it the hardest part of Christianity to accept.",
                 "hard", signals=["skeptical_of_jesus"],
                 honest_inquiry=0.3, courage=0.25),
            _opt("I set it aside and focus on his teachings.",
                 "set_aside",
                 honest_inquiry=0.25, openness=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["open_to_scripture"]',
        "jesus_reference": "1 Corinthians 15:17 — If Christ has not been raised, your faith is futile.",
    },

    # ══════════════════════════════════════════════════════════════════
    # RESTORATION PATHWAY — For people who are open to the idea
    # that God still speaks and that there's more to the gospel.
    # This is the pathway toward Latter-day Saint teaching,
    # introduced only when the person has shown openness.
    # ══════════════════════════════════════════════════════════════════

    {
        "track": "ANY", "stage": "MID", "topic": "god_still_speaks",
        "question_text": "Do you think God spoke to prophets and apostles in the ancient world — and if he did, is there any reason he would have stopped?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("No — I don't think God speaks directly to people.",
                 "no",
                 honest_inquiry=0.3),
            _opt("Maybe — I haven't thought about why he would stop.",
                 "maybe", signals=["open_to_restoration"],
                 honest_inquiry=0.3, openness=0.25, hunger=0.2),
            _opt("Yes — I think God still speaks and that matters.",
                 "yes", signals=["open_to_restoration", "open_to_god"],
                 openness=0.35, hunger=0.3, sincerity=0.2),
            _opt("The question itself is interesting — I want to think about it.",
                 "curious", signals=["open_to_restoration"],
                 honest_inquiry=0.35, openness=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["open_to_god"]',
        "jesus_reference": "Amos 3:7 — Surely the Lord does nothing without revealing his secret to his servants the prophets.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "restoration_what_if",
        "question_text": "What if the original church Jesus established — with apostles, revelation, and priesthood authority — had been restored in our time? What would you want to know about that?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(hunger=0.35, honest_inquiry=0.3, openness=0.25),
        "prerequisite_signals": '["open_to_restoration"]',
        "jesus_reference": "Acts 3:21 — Heaven must receive him until the time of the restoration of all things.",
    },
    {
        "track": "ANY", "stage": "DEEP", "topic": "book_of_mormon_curiosity",
        "question_text": "There's a book of scripture called the Book of Mormon — a second witness for Jesus Christ, claimed to be ancient but translated in the 1800s. Does that interest you, bother you, or make you want to know more?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("It interests me — I'd want to know the evidence for it.",
                 "interested", signals=["curious_about_book_of_mormon"],
                 honest_inquiry=0.35, hunger=0.3, openness=0.25),
            _opt("It makes me skeptical — that's a big claim.",
                 "skeptical",
                 honest_inquiry=0.35, courage=0.2),
            _opt("I've heard of it but never taken it seriously.",
                 "heard_not_serious",
                 honest_inquiry=0.2, openness=0.15),
            _opt("I'm open — what makes it credible?",
                 "open", signals=["curious_about_book_of_mormon"],
                 openness=0.35, hunger=0.25, honest_inquiry=0.3),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["open_to_restoration"]',
        "jesus_reference": "John 10:16 — I have other sheep that are not of this sheep pen. I must bring them also.",
    },
    {
        "track": "ANY", "stage": "DEEP", "topic": "joseph_smith_question",
        "question_text": "The restoration of the gospel — if it happened — started with a young man who said God spoke to him directly. Does that kind of claim make you more curious, or more skeptical?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("More curious — I want to understand the evidence.",
                 "curious",
                 honest_inquiry=0.4, hunger=0.3, openness=0.3),
            _opt("More skeptical — people claim divine experiences all the time.",
                 "skeptical",
                 honest_inquiry=0.35, courage=0.2),
            _opt("Both — I'm interested but I'd want to test it.",
                 "both",
                 honest_inquiry=0.35, openness=0.25, courage=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["curious_about_book_of_mormon"]',
        "jesus_reference": "Matthew 7:20 — By their fruits you will know them.",
    },
    {
        "track": "ANY", "stage": "DEEP", "topic": "restoration_invitation",
        "question_text": "If you could find out — really find out — whether the Book of Mormon is true or not, would you want to know? Even if the answer changed what you do next?",
        "answer_type": "YES_NO",
        "answer_options": _opts(
            _opt("Yes — I'd want to know the truth even if it cost me something.",
                 "yes",
                 courage=0.4, hunger=0.35, sincerity=0.3, honest_inquiry=0.25),
            _opt("I'm not sure I'm ready for that.",
                 "not_ready",
                 honest_inquiry=0.2, humility=0.15),
            _opt("No — I'm comfortable where I am.",
                 "no",
                 honest_inquiry=0.25),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["curious_about_book_of_mormon"]',
        "jesus_reference": "Moroni 10:4 — Ask God, the Eternal Father, in the name of Christ, if these things are true.",
    },

    # ══════════════════════════════════════════════════════════════════
    # LDS MEMBER PATHWAY — For people who were members or are drifting.
    # These questions meet people who know the church, not newcomers.
    # The tone is gentle, never shaming — the prodigal's father ran.
    # ══════════════════════════════════════════════════════════════════

    {
        "track": "ANY", "stage": "MID", "topic": "member_step_back",
        "question_text": "What was the thing — or the moment — that made you start stepping back?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(honest_inquiry=0.35, courage=0.35, sincerity=0.3),
        "prerequisite_signals": '["inactive_member"]',
        "jesus_reference": "Luke 15:17 — When he came to himself, he said: How many of my father's hired servants have more than enough bread?",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "member_what_remains",
        "question_text": "Even with the distance, is there anything from your faith you've kept holding onto — maybe quietly?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(sincerity=0.35, hunger=0.25, courage=0.2),
        "prerequisite_signals": '["inactive_member"]',
        "jesus_reference": "Revelation 2:4 — You have abandoned the love you had at first. But I remember it.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "member_missing",
        "question_text": "Is there anything you miss about being an active member — even if you don't say it out loud?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("The community — the people who knew me.",
                 "community",
                 sincerity=0.25, compassion=0.2, hunger=0.15),
            _opt("The certainty — I miss knowing what I believed.",
                 "certainty",
                 sincerity=0.3, hunger=0.25),
            _opt("The ordinances or worship — something felt real then.",
                 "ordinances",
                 sincerity=0.3, hunger=0.3, openness=0.2),
            _opt("Honestly — not much. I feel freer now.",
                 "nothing",
                 honest_inquiry=0.25, courage=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["inactive_member"]',
        "jesus_reference": "Luke 15:20 — But while he was still a long way off, his father saw him and was filled with compassion.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "losing_faith_reason",
        "question_text": "Something is pulling you away from the faith you grew up in — can you name what it is? A doubt, a hurt, a question that hasn't been answered?",
        "answer_type": "CHOICE",
        "answer_options": _opts(
            _opt("A historical or doctrinal question I can't resolve.",
                 "intellectual", signals=["intellectual_doubts"],
                 honest_inquiry=0.4, courage=0.3),
            _opt("Someone in the church hurt me or failed me.",
                 "person", signals=["hurt_by_church"],
                 courage=0.3, sincerity=0.3),
            _opt("My life changed in ways the church didn't make room for.",
                 "life_change",
                 honest_inquiry=0.3, courage=0.3, sincerity=0.2),
            _opt("I've drifted — there's no single thing, just distance.",
                 "drift",
                 honest_inquiry=0.25, humility=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["losing_faith"]',
        "jesus_reference": "Luke 22:32 — I have prayed for you that your faith may not fail. And when you have returned, strengthen your brothers.",
    },
    {
        "track": "ANY", "stage": "MID", "topic": "intellectual_doubt_space",
        "question_text": "What's the specific question or historical issue that's hardest for you? You don't have to protect anyone's feelings here.",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(honest_inquiry=0.4, courage=0.35, humility=0.2),
        "prerequisite_signals": '["intellectual_doubts"]',
        "jesus_reference": "John 20:27 — Put your finger here; see my hands. Reach out your hand and put it into my side. Stop doubting and believe.",
    },
    {
        "track": "ANY", "stage": "DEEP", "topic": "member_return_question",
        "question_text": "If someone could give you a real answer to the thing that's bothering you — not just 'have more faith' — would you be open to coming back?",
        "answer_type": "YES_NO",
        "answer_options": _opts(
            _opt("Yes — if the answers were real, I'd want to.",
                 "yes",
                 hunger=0.35, sincerity=0.3, openness=0.25, courage=0.2),
            _opt("I honestly don't know — it's not just intellectual for me.",
                 "unsure",
                 honest_inquiry=0.3, sincerity=0.25, humility=0.2),
            _opt("No — I've moved past that point.",
                 "no",
                 honest_inquiry=0.25, courage=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": '["inactive_member"]',
        "jesus_reference": "John 21:22 — What is that to you? You follow me.",
    },

    # ══════════════════════════════════════════════════════════════════
    # DEEP — For people who've been genuinely engaging over time.
    # The real question. The one Jesus waited to ask.
    # ══════════════════════════════════════════════════════════════════

    {
        "track": "ANY", "stage": "DEEP", "topic": "seeking_honest",
        "question_text": "Something in you kept coming back here. What are you actually looking for?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(courage=0.4, sincerity=0.4, hunger=0.3),
        "prerequisite_signals": "[]",
        "jesus_reference": "John 1:38 — What are you seeking? The first and last question.",
    },
    {
        "track": "ANY", "stage": "DEEP", "topic": "one_question",
        "question_text": "If you could ask God one question right now — knowing he would actually answer — what would you ask?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(hunger=0.4, courage=0.3, sincerity=0.3),
        "prerequisite_signals": "[]",
        "jesus_reference": "Matthew 7:7 — Ask, and it will be given to you. Seek, and you will find.",
    },
    {
        "track": "ANY", "stage": "DEEP", "topic": "cost",
        "question_text": "If everything you've been reading here turned out to be true — what would change for you? Be honest.",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(courage=0.45, sincerity=0.4, humility=0.3),
        "prerequisite_signals": "[]",
        "jesus_reference": "Luke 9:23 — If anyone would come after me, let him deny himself and take up his cross daily.",
    },
    {
        "track": "ANY", "stage": "DEEP", "topic": "next_step",
        "question_text": "Is there something you already know you should do — even one small thing — that you've been putting off?",
        "answer_type": "FREE_TEXT",
        "answer_options": "[]",
        "scale_low": "", "scale_high": "",
        "trait_signals": _sig(courage=0.4, humility=0.35, sincerity=0.3),
        "prerequisite_signals": "[]",
        "jesus_reference": "John 5:6 — Do you want to be healed? Jesus asked before he acted.",
    },
    {
        "track": "ANY", "stage": "DEEP", "topic": "ready_to_know",
        "question_text": "Some people spend their whole life curious about God and never actually ask him directly. Are you willing to try that — to sincerely ask and wait for an answer?",
        "answer_type": "YES_NO",
        "answer_options": _opts(
            _opt("Yes — I'm willing to actually try.",
                 "yes",
                 courage=0.45, hunger=0.4, openness=0.3, sincerity=0.3),
            _opt("I want to be — I'm just not there yet.",
                 "not_yet",
                 honest_inquiry=0.25, hunger=0.2, humility=0.2),
            _opt("No — I don't think I'll get anything back.",
                 "no",
                 honest_inquiry=0.35, courage=0.2),
        ),
        "scale_low": "", "scale_high": "",
        "trait_signals": "{}",
        "prerequisite_signals": "[]",
        "jesus_reference": "James 1:5 — If any of you lacks wisdom, let him ask God, who gives generously to all without reproach.",
    },
]
