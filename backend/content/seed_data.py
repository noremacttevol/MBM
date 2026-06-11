"""
Content library.

Four tiers, each a different place on the journey toward Christ and his restored church:

  MILK        — Jesus as humanity's common ground. No tradition required.
  BRIDGE      — For skeptics. Evidence, reason, history.
  RESTORATION — The specific story of what happened after the early church.
                Honest about where it leads before asking anyone to go there.
  MAINTENANCE — For members deepening their discipleship.

Within each tier, items belong to narrative sequences (sequence_group + sequence_order)
so the feed builds a journey rather than serving disconnected pieces.

content_type:
  link    — external article, scripture, video, talk
  prompt  — in-app reflective question (no URL). The feed asks; the user responds.
"""

SEED_CONTENT = [

    # ══════════════════════════════════════════════════════════════════
    # MILK — Jesus as humanity's common ground
    # ══════════════════════════════════════════════════════════════════

    # ── WHO IS JESUS ──────────────────────────────────────────────────
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "who_is_jesus", "sequence_order": 1,
        "title": "For God So Loved the World",
        "description": "The most recognized verse in scripture. One sentence that explains why Christ came.",
        "scripture_ref": "John 3:16-17", "media_type": "scripture",
        "resonance_style": "foundational", "estimated_read_minutes": 2,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/john/3?lang=eng&id=p16-p17#p16",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "who_is_jesus", "sequence_order": 2,
        "title": "In the Beginning Was the Word",
        "description": "John 1:1-14. Christ was present at creation. The Light that lights every person born into this world.",
        "scripture_ref": "John 1:1-14", "media_type": "scripture",
        "resonance_style": "foundational", "estimated_read_minutes": 3,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/john/1?lang=eng&id=p1-p14#p1",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "who_is_jesus", "sequence_order": 3,
        "title": "I Am the Way, the Truth, and the Life",
        "description": "John 14:1-6. He doesn't point to the path — he claims to be it.",
        "scripture_ref": "John 14:1-6", "media_type": "scripture",
        "resonance_style": "foundational", "estimated_read_minutes": 2,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/john/14?lang=eng&id=p1-p6#p1",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "who_is_jesus", "sequence_order": 4,
        "title": "I Am the Light of the World",
        "description": "John 8:12. Two words that changed how humanity understood God's presence in darkness.",
        "scripture_ref": "John 8:12", "media_type": "scripture",
        "resonance_style": "emotional", "estimated_read_minutes": 1,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/john/8?lang=eng&id=p12#p12",
    },

    # ── LOVE AND MERCY ────────────────────────────────────────────────
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "love_and_mercy", "sequence_order": 1,
        "title": "The Prodigal Son",
        "description": "A father runs to meet his returning son. No lecture. No conditions. Just arms open.",
        "scripture_ref": "Luke 15:11-32", "media_type": "scripture",
        "resonance_style": "emotional", "estimated_read_minutes": 4,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/luke/15?lang=eng&id=p11-p32#p11",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "love_and_mercy", "sequence_order": 2,
        "title": "The Lost Sheep",
        "description": "Ninety-nine safe in the fold — and he leaves all of them to find the one that wandered. You are that one.",
        "scripture_ref": "Luke 15:1-7", "media_type": "scripture",
        "resonance_style": "personal", "estimated_read_minutes": 2,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/luke/15?lang=eng&id=p1-p7#p1",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "love_and_mercy", "sequence_order": 3,
        "title": "Woman at the Well",
        "description": "Jesus crosses every social barrier to speak to one person alone. He already knows everything about her — and he comes anyway.",
        "scripture_ref": "John 4:1-30", "media_type": "scripture",
        "resonance_style": "personal", "estimated_read_minutes": 5,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/john/4?lang=eng&id=p1-p30#p1",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "love_and_mercy", "sequence_order": 4,
        "title": "Zacchaeus: He Came to My House",
        "description": "A corrupt tax collector, hated by everyone. Jesus sees him in the tree and says: I'm staying at your house today.",
        "scripture_ref": "Luke 19:1-10", "media_type": "scripture",
        "resonance_style": "personal", "estimated_read_minutes": 3,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/luke/19?lang=eng&id=p1-p10#p1",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "love_and_mercy", "sequence_order": 5,
        "title": "The Good Samaritan",
        "description": "Luke 10:25-37. The definition of neighbor has no boundary. Pure moral goodness in story form.",
        "scripture_ref": "Luke 10:25-37", "media_type": "scripture",
        "resonance_style": "moral", "estimated_read_minutes": 3,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/luke/10?lang=eng&id=p25-p37#p25",
    },

    # ── COMFORT IN DARKNESS ───────────────────────────────────────────
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "comfort_in_darkness", "sequence_order": 1,
        "title": "The Lord Is My Shepherd",
        "description": "Psalm 23. Six verses that have comforted humans in their darkest moments for three thousand years.",
        "scripture_ref": "Psalm 23", "media_type": "scripture",
        "resonance_style": "comfort", "estimated_read_minutes": 2,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/ot/ps/23?lang=eng",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "comfort_in_darkness", "sequence_order": 2,
        "title": "Peace I Leave With You",
        "description": "John 14:27. Not the world's kind of peace — a peace that doesn't depend on circumstances.",
        "scripture_ref": "John 14:27", "media_type": "scripture",
        "resonance_style": "comfort", "estimated_read_minutes": 1,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/john/14?lang=eng&id=p27#p27",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "comfort_in_darkness", "sequence_order": 3,
        "title": "Come Unto Me, All Ye That Labour",
        "description": "Matthew 11:28-30. A direct invitation from Christ to every person who is exhausted.",
        "scripture_ref": "Matthew 11:28-30", "media_type": "scripture",
        "resonance_style": "comfort", "estimated_read_minutes": 2,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/matt/11?lang=eng&id=p28-p30#p28",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "comfort_in_darkness", "sequence_order": 4,
        "title": "Jesus Wept",
        "description": "John 11:35 — the shortest verse in scripture. Lazarus is dead and Jesus stands at the tomb and cries. God is not indifferent to your pain.",
        "scripture_ref": "John 11:1-44", "media_type": "scripture",
        "resonance_style": "emotional", "estimated_read_minutes": 5,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/john/11?lang=eng&id=p1-p44#p1",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "comfort_in_darkness", "sequence_order": 5,
        "title": "Nothing Can Separate Us",
        "description": "Romans 8:38-39. Paul lists everything that could possibly come between you and God's love — and says none of it can.",
        "scripture_ref": "Romans 8:38-39", "media_type": "scripture",
        "resonance_style": "comfort", "estimated_read_minutes": 2,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/rom/8?lang=eng&id=p38-p39#p38",
    },

    # ── MORAL GOODNESS ────────────────────────────────────────────────
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "moral_goodness", "sequence_order": 1,
        "title": "Beatitudes — The Sermon on the Mount",
        "description": "Matthew 5:1-12. The most countercultural speech ever given. Blessed are the poor in spirit. Blessed are the meek.",
        "scripture_ref": "Matthew 5:1-12", "media_type": "scripture",
        "resonance_style": "moral", "estimated_read_minutes": 3,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/matt/5?lang=eng&id=p1-p12#p1",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "moral_goodness", "sequence_order": 2,
        "title": "Love Is Patient, Love Is Kind",
        "description": "1 Corinthians 13. The standard every human already reaches for — the description of what God's love actually looks like.",
        "scripture_ref": "1 Corinthians 13", "media_type": "scripture",
        "resonance_style": "moral", "estimated_read_minutes": 3,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/1-cor/13?lang=eng",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "moral_goodness", "sequence_order": 3,
        "title": "I Was Hungry and You Fed Me",
        "description": "Matthew 25:35-40. Every act of genuine kindness toward another person is an act directly toward Christ.",
        "scripture_ref": "Matthew 25:35-40", "media_type": "scripture",
        "resonance_style": "moral", "estimated_read_minutes": 3,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/matt/25?lang=eng&id=p35-p40#p35",
    },

    # ── PRAYER ────────────────────────────────────────────────────────
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "prayer_and_presence", "sequence_order": 1,
        "title": "The Lord's Prayer",
        "description": "Matthew 6:9-13. When his disciples asked Jesus how to pray, this is exactly what he said.",
        "scripture_ref": "Matthew 6:9-13", "media_type": "scripture",
        "resonance_style": "personal", "estimated_read_minutes": 2,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/matt/6?lang=eng&id=p9-p13#p9",
    },
    {
        "tag": "MILK", "content_type": "link",
        "sequence_group": "prayer_and_presence", "sequence_order": 2,
        "title": "Ask, Seek, Knock",
        "description": "Matthew 7:7-11. Three words — each more active than the last. He promises an answer to all three.",
        "scripture_ref": "Matthew 7:7-11", "media_type": "scripture",
        "resonance_style": "personal", "estimated_read_minutes": 2,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/nt/matt/7?lang=eng&id=p7-p11#p7",
    },

    # ── MILK PROMPTS ──────────────────────────────────────────────────
    {
        "tag": "MILK", "content_type": "prompt",
        "sequence_group": None, "sequence_order": 0,
        "title": "A question for you",
        "description": "Has there ever been a moment in your life that felt too meaningful to be a coincidence — a moment that made you wonder if something more was at work?",
        "scripture_ref": None, "media_type": "prompt",
        "resonance_style": "personal", "estimated_read_minutes": 1,
        "url": None,
    },
    {
        "tag": "MILK", "content_type": "prompt",
        "sequence_group": None, "sequence_order": 0,
        "title": "If you could ask one question",
        "description": "If you knew God was listening right now — really listening — what would you ask him?",
        "scripture_ref": None, "media_type": "prompt",
        "resonance_style": "personal", "estimated_read_minutes": 1,
        "url": None,
    },

    # ══════════════════════════════════════════════════════════════════
    # BRIDGE — For skeptics. Evidence, reason, history.
    # ══════════════════════════════════════════════════════════════════

    # ── THE CASE FOR THE RESURRECTION ────────────────────────────────
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "resurrection_case", "sequence_order": 1,
        "title": "The Minimal Facts Argument",
        "description": "Gary Habermas. Using only facts virtually all historians — secular and religious — accept. The case for the resurrection built from the ground up.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "logical", "estimated_read_minutes": 12,
        "url": "https://www.garyhabermas.com/articles/crj_minimumfacts/crj_minimumfacts.htm",
    },
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "resurrection_case", "sequence_order": 2,
        "title": "The Trilemma: Liar, Lunatic, or Lord",
        "description": "C.S. Lewis's argument that Jesus cannot be merely a 'good teacher.' Every option forces a decision.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "logical", "estimated_read_minutes": 8,
        "url": "https://www.cslewisinstitute.org/resources/what-did-c-s-lewis-mean-by-liar-lunatic-or-lord/",
    },
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "resurrection_case", "sequence_order": 3,
        "title": "Would the Disciples Die for a Lie?",
        "description": "J. Warner Wallace. Why the willingness of the eyewitnesses to die changes the probability calculus entirely.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "historical", "estimated_read_minutes": 10,
        "url": "https://www.coldcasechristianity.com/writings/are-the-gospels-reliable/",
    },
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "resurrection_case", "sequence_order": 4,
        "title": "NT Wright: The Resurrection and History",
        "description": "One of the world's leading New Testament scholars on why the resurrection is the best historical explanation for what happened.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "historical", "estimated_read_minutes": 15,
        "url": "https://ntwrightpage.com/2016/07/12/the-resurrection-of-the-son-of-god/",
    },

    # ── FAITH AND REASON ──────────────────────────────────────────────
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "faith_and_reason", "sequence_order": 1,
        "title": "Can Science and Faith Coexist?",
        "description": "Francis Collins, director of the Human Genome Project, on why he became a Christian scientist.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "logical", "estimated_read_minutes": 8,
        "url": "https://biologos.org/about-us/biologos-story",
    },
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "faith_and_reason", "sequence_order": 2,
        "title": "The Fine-Tuning Argument",
        "description": "The fundamental constants of the universe are calibrated to a precision that defies coincidence. What does that mean?",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "logical", "estimated_read_minutes": 10,
        "url": "https://www.reasonablefaith.org/writings/popular-writings/existence-nature-of-god/the-teleological-argument/",
    },
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "faith_and_reason", "sequence_order": 3,
        "title": "The Kalam Cosmological Argument",
        "description": "William Lane Craig. Everything that begins to exist has a cause. The universe began to exist. Therefore...",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "logical", "estimated_read_minutes": 10,
        "url": "https://www.reasonablefaith.org/writings/popular-writings/existence-nature-of-god/the-kalam-cosmological-argument/",
    },

    # ── ANSWERING OBJECTIONS ──────────────────────────────────────────
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "objections", "sequence_order": 1,
        "title": "Why Does God Allow Suffering?",
        "description": "Tim Keller's answer to the problem of evil — the most common objection to faith. Not dismissive. Actually engaging.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "philosophical", "estimated_read_minutes": 10,
        "url": "https://redeemercitytocity.com/articles-stories/the-problem-of-evil-and-suffering",
    },
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "objections", "sequence_order": 2,
        "title": "If God Is Good, Why Does Hell Exist?",
        "description": "C.S. Lewis. Hell as the door locked from the inside. The most honest answer to the hardest question.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "philosophical", "estimated_read_minutes": 8,
        "url": "https://www.cslewisinstitute.org/resources/c-s-lewis-on-hell/",
    },
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "objections", "sequence_order": 3,
        "title": "Was the New Testament Altered Over Time?",
        "description": "Textual criticism from a secular historian's perspective. The manuscript evidence is stronger than for any other ancient document.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "historical", "estimated_read_minutes": 8,
        "url": "https://www.str.org/w/the-bibliographic-test",
    },
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "objections", "sequence_order": 4,
        "title": "Josephus on Jesus",
        "description": "A first-century Jewish historian with every reason NOT to speak well of Christianity references Jesus in his work. What he said matters.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "historical", "estimated_read_minutes": 6,
        "url": "https://www.history.com/news/did-jesus-exist-historical-evidence",
    },

    # ── CONVERSION STORIES ────────────────────────────────────────────
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "conversion_stories", "sequence_order": 1,
        "title": "C.S. Lewis: The Most Reluctant Convert",
        "description": "A committed atheist who followed the evidence — and was surprised by what he found.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "personal", "estimated_read_minutes": 10,
        "url": "https://www.cslewisinstitute.org/resources/c-s-lewis-conversion/",
    },
    {
        "tag": "BRIDGE", "content_type": "link",
        "sequence_group": "conversion_stories", "sequence_order": 2,
        "title": "Lee Strobel: The Case for Christ",
        "description": "An atheist journalist investigated the resurrection as a legal case, intending to disprove it. This is what he found.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "logical", "estimated_read_minutes": 10,
        "url": "https://www.leestrobel.com/about/",
    },

    # ── BRIDGE PROMPTS ────────────────────────────────────────────────
    {
        "tag": "BRIDGE", "content_type": "prompt",
        "sequence_group": None, "sequence_order": 0,
        "title": "A question for you",
        "description": "What would it actually take for you to believe? Not what someone else says — what would you, personally, need to see or experience?",
        "scripture_ref": None, "media_type": "prompt",
        "resonance_style": "logical", "estimated_read_minutes": 1,
        "url": None,
    },
    {
        "tag": "BRIDGE", "content_type": "prompt",
        "sequence_group": None, "sequence_order": 0,
        "title": "A question for you",
        "description": "Have you ever had an experience your usual worldview couldn't fully account for — something that made you pause?",
        "scripture_ref": None, "media_type": "prompt",
        "resonance_style": "philosophical", "estimated_read_minutes": 1,
        "url": None,
    },

    # ══════════════════════════════════════════════════════════════════
    # RESTORATION — The specific story of what happened after the early church.
    # Honest about where it leads. Introduces the Restoration before full LDS doctrine.
    # ══════════════════════════════════════════════════════════════════

    {
        "tag": "RESTORATION", "content_type": "link",
        "sequence_group": "restoration_story", "sequence_order": 1,
        "title": "Something Was Lost",
        "description": "Christ gave his apostles authority — the power to act in his name. What happened to that authority after they died? History has a clear answer, and it isn't comfortable.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "historical", "estimated_read_minutes": 8,
        "url": "https://www.churchofjesuschrist.org/study/manual/gospel-topics/apostasy?lang=eng",
    },
    {
        "tag": "RESTORATION", "content_type": "link",
        "sequence_group": "restoration_story", "sequence_order": 2,
        "title": "The Great Apostasy — What the Early Church Fathers Said",
        "description": "The apostasy wasn't invented by Joseph Smith. Early Christian writers themselves warned that it was coming.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "historical", "estimated_read_minutes": 10,
        "url": "https://www.churchofjesuschrist.org/study/manual/gospel-topics/apostasy?lang=eng",
    },
    {
        "tag": "RESTORATION", "content_type": "link",
        "sequence_group": "restoration_story", "sequence_order": 3,
        "title": "The World Was Ready",
        "description": "The printing press. The Reformation. The Enlightenment. The American founding. These weren't accidents — they were the conditions required for something new to be built.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "historical", "estimated_read_minutes": 7,
        "url": "https://www.churchofjesuschrist.org/study/manual/gospel-topics/restoration-of-the-gospel?lang=eng",
    },
    {
        "tag": "RESTORATION", "content_type": "link",
        "sequence_group": "restoration_story", "sequence_order": 4,
        "title": "A Boy's Question",
        "description": "1820. A fourteen-year-old in upstate New York wanted to know which church was true. He did what the Bible said to do: he asked God. What happened next is either the most important event since the Resurrection — or nothing at all.",
        "scripture_ref": "Joseph Smith—History 1:1-20", "media_type": "scripture",
        "resonance_style": "personal", "estimated_read_minutes": 8,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/pgp/js-h/1?lang=eng&id=p1-p20#p1",
    },
    {
        "tag": "RESTORATION", "content_type": "link",
        "sequence_group": "restoration_story", "sequence_order": 5,
        "title": "A Second Witness",
        "description": "The Book of Mormon is not a replacement for the Bible — it's a companion to it. A second record of Christ's ministry, from a different continent, arriving at the same conclusion.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "foundational", "estimated_read_minutes": 6,
        "url": "https://www.churchofjesuschrist.org/study/manual/gospel-topics/book-of-mormon?lang=eng",
    },
    {
        "tag": "RESTORATION", "content_type": "link",
        "sequence_group": "restoration_story", "sequence_order": 6,
        "title": "Moroni's Promise",
        "description": "The Book of Mormon comes with an invitation to test it. Ask God if it is true. Sincere heart. Real intent. Faith in Christ. The promise is: you will know.",
        "scripture_ref": "Moroni 10:3-5", "media_type": "scripture",
        "resonance_style": "personal", "estimated_read_minutes": 3,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/bofm/moro/10?lang=eng&id=p3-p5#p3",
    },

    # ── RESTORATION PROMPTS ───────────────────────────────────────────
    {
        "tag": "RESTORATION", "content_type": "prompt",
        "sequence_group": None, "sequence_order": 0,
        "title": "A question for you",
        "description": "Does it matter to you whether the church you attend has the same authority as the one Christ established? Or is sincerity enough?",
        "scripture_ref": None, "media_type": "prompt",
        "resonance_style": "philosophical", "estimated_read_minutes": 1,
        "url": None,
    },
    {
        "tag": "RESTORATION", "content_type": "prompt",
        "sequence_group": None, "sequence_order": 0,
        "title": "A question for you",
        "description": "If God were going to restore his church on earth today, what would you expect it to look like? What would be the signs that it was real?",
        "scripture_ref": None, "media_type": "prompt",
        "resonance_style": "personal", "estimated_read_minutes": 1,
        "url": None,
    },

    # ══════════════════════════════════════════════════════════════════
    # MAINTENANCE — For members deepening their discipleship
    # ══════════════════════════════════════════════════════════════════

    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "restoration", "sequence_order": 1,
        "title": "Joseph Smith — History",
        "description": "The foundational account. A fourteen-year-old boy asks which church to join. What happened next changed the world.",
        "scripture_ref": "Joseph Smith—History 1:1-25", "media_type": "scripture",
        "resonance_style": "foundational", "estimated_read_minutes": 10,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/pgp/js-h/1?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "restoration", "sequence_order": 2,
        "title": "The Articles of Faith",
        "description": "Thirteen sentences that summarize what Latter-day Saints believe. Written by Joseph Smith in 1842.",
        "scripture_ref": "Articles of Faith 1:1-13", "media_type": "scripture",
        "resonance_style": "doctrinal", "estimated_read_minutes": 4,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/pgp/a-of-f/1?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "restoration", "sequence_order": 3,
        "title": "The Living Christ: A Formal Testimony",
        "description": "The First Presidency and Quorum of the Twelve Apostles' written witness of Jesus Christ.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "devotional", "estimated_read_minutes": 5,
        "url": "https://www.churchofjesuschrist.org/study/manual/the-living-christ-the-testimony-of-the-apostles/the-living-christ-the-testimony-of-the-apostles?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "book_of_mormon", "sequence_order": 1,
        "title": "1 Nephi 1 — Where It Begins",
        "description": "The opening of the most correct book on earth. Lehi's vision of the tree of life begins here.",
        "scripture_ref": "1 Nephi 1", "media_type": "scripture",
        "resonance_style": "foundational", "estimated_read_minutes": 5,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/bofm/1-ne/1?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "book_of_mormon", "sequence_order": 2,
        "title": "The Tree of Life Vision",
        "description": "1 Nephi 8. One of the most powerful visions in scripture. The iron rod. The great and spacious building. What it all means.",
        "scripture_ref": "1 Nephi 8", "media_type": "scripture",
        "resonance_style": "emotional", "estimated_read_minutes": 8,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/bofm/1-ne/8?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "book_of_mormon", "sequence_order": 3,
        "title": "Alma 32 — The Experiment on the Word",
        "description": "Faith as a seed. Plant it, nourish it, watch what grows. The most practical guide to building faith in scripture.",
        "scripture_ref": "Alma 32", "media_type": "scripture",
        "resonance_style": "personal", "estimated_read_minutes": 8,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/bofm/alma/32?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "book_of_mormon", "sequence_order": 4,
        "title": "3 Nephi 11 — Christ Appears to the Nephites",
        "description": "The resurrected Christ descends from heaven and invites each person to come forward and feel the wounds in his hands and feet. One at a time.",
        "scripture_ref": "3 Nephi 11", "media_type": "scripture",
        "resonance_style": "emotional", "estimated_read_minutes": 8,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/11?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "book_of_mormon", "sequence_order": 5,
        "title": "Ether 12 — Faith's Hall of Fame",
        "description": "Every miracle in scripture happened because someone acted before they had full certainty.",
        "scripture_ref": "Ether 12", "media_type": "scripture",
        "resonance_style": "foundational", "estimated_read_minutes": 7,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/bofm/ether/12?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "covenant_path", "sequence_order": 1,
        "title": "Preach My Gospel — The Gospel of Jesus Christ",
        "description": "Faith, repentance, baptism, the gift of the Holy Ghost, enduring to the end. The five principles that are the foundation of everything.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "doctrinal", "estimated_read_minutes": 15,
        "url": "https://www.churchofjesuschrist.org/study/manual/preach-my-gospel-2023/04-chapter-3?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "covenant_path", "sequence_order": 2,
        "title": "President Nelson — The Covenant Path",
        "description": "Why covenants matter. How they connect you to Christ's power in daily life. Not rules — access.",
        "scripture_ref": None, "media_type": "talk",
        "resonance_style": "doctrinal", "estimated_read_minutes": 10,
        "url": "https://www.churchofjesuschrist.org/study/general-conference/2022/04/47nelson?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "discipleship", "sequence_order": 1,
        "title": "Elder Holland — Lord, I Believe",
        "description": "For anyone whose faith wavers. One of the most honest General Conference addresses ever given. He doesn't pretend doubt is easy.",
        "scripture_ref": None, "media_type": "talk",
        "resonance_style": "emotional", "estimated_read_minutes": 12,
        "url": "https://www.churchofjesuschrist.org/study/general-conference/2013/04/lord-i-believe?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "discipleship", "sequence_order": 2,
        "title": "Elder Holland — Cast Not Away Therefore Your Confidence",
        "description": "Spiritual opposition is real. The darkness before the dawn is real. This talk is for the moment right before you give up.",
        "scripture_ref": None, "media_type": "talk",
        "resonance_style": "emotional", "estimated_read_minutes": 12,
        "url": "https://www.churchofjesuschrist.org/study/general-conference/1999/04/cast-not-away-therefore-your-confidence?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "discipleship", "sequence_order": 3,
        "title": "Elder Uchtdorf — Come, Join With Us",
        "description": "To everyone who has drifted or been hurt or walked away. The door is open. You are wanted here.",
        "scripture_ref": None, "media_type": "talk",
        "resonance_style": "personal", "estimated_read_minutes": 10,
        "url": "https://www.churchofjesuschrist.org/study/general-conference/2013/10/come-join-with-us?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "discipleship", "sequence_order": 4,
        "title": "President Nelson — Hear Him",
        "description": "The call of our day: learn to recognize the voice of Jesus Christ. Not as a metaphor. As a real, personal relationship.",
        "scripture_ref": None, "media_type": "talk",
        "resonance_style": "devotional", "estimated_read_minutes": 10,
        "url": "https://www.churchofjesuschrist.org/study/general-conference/2020/04/45nelson?lang=eng",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "discipleship", "sequence_order": 5,
        "title": "D&C 121 — Authority Without Compulsion",
        "description": "Written from Liberty Jail. The most important passage on how priesthood authority must be used: by persuasion, by gentleness. Never by force.",
        "scripture_ref": "D&C 121:34-46", "media_type": "scripture",
        "resonance_style": "doctrinal", "estimated_read_minutes": 5,
        "url": "https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/121?lang=eng&id=p34-p46#p34",
    },
    {
        "tag": "MAINTENANCE", "content_type": "link",
        "sequence_group": "discipleship", "sequence_order": 6,
        "title": "Come Follow Me — Weekly Home Study",
        "description": "This week's home-centered gospel study. The primary tool for personal and family conversion.",
        "scripture_ref": None, "media_type": "article",
        "resonance_style": "study", "estimated_read_minutes": 20,
        "url": "https://www.churchofjesuschrist.org/study/come-follow-me?lang=eng",
    },

    # ── MAINTENANCE PROMPTS ───────────────────────────────────────────
    {
        "tag": "MAINTENANCE", "content_type": "prompt",
        "sequence_group": None, "sequence_order": 0,
        "title": "A question for you",
        "description": "When was the last time you felt the Spirit unmistakably? What were the circumstances?",
        "scripture_ref": None, "media_type": "prompt",
        "resonance_style": "devotional", "estimated_read_minutes": 1,
        "url": None,
    },
    {
        "tag": "MAINTENANCE", "content_type": "prompt",
        "sequence_group": None, "sequence_order": 0,
        "title": "A question for you",
        "description": "What part of living the gospel is hardest for you right now — not the part you'd say out loud, but the real one?",
        "scripture_ref": None, "media_type": "prompt",
        "resonance_style": "personal", "estimated_read_minutes": 1,
        "url": None,
    },
]
