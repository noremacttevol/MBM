export type FeedTag = 'MILK' | 'BRIDGE' | 'RESTORATION' | 'MAINTENANCE';
export type MediaType = 'article' | 'video' | 'podcast';
export type ResonanceStyle =
  | 'emotional' | 'logical' | 'moral' | 'comfort' | 'historical'
  | 'doctrinal' | 'foundational' | 'personal' | 'philosophical'
  | 'devotional' | 'study';

export interface ContentItem {
  id:               number;
  tag:              FeedTag;
  title:            string;
  description:      string;
  scriptureRef:     string;
  url:              string;
  mediaType:        MediaType;
  estimatedMinutes: number;
  resonanceStyle:   ResonanceStyle;
}

export const CONTENT: ContentItem[] = [

  // ── MILK ─────────────────────────────────────────────────────────────────
  // Foundational Christian content. Comfort, parables, invitation.
  // These meet people exactly where they are with no assumptions.

  {
    id:               1,
    tag:              'MILK',
    title:            'Peace I Leave With You',
    description:      'John 14:27. Not the world\'s kind of peace — a peace that doesn\'t depend on circumstances. Jesus said these words the night before he died, which is the only reason they mean anything at all.',
    scriptureRef:     'John 14:27',
    url:              'https://www.biblegateway.com/passage/?search=John+14%3A27&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 2,
    resonanceStyle:   'comfort',
  },
  {
    id:               2,
    tag:              'MILK',
    title:            'The Lord\'s Prayer',
    description:      'Matthew 6:9-13. When his disciples asked Jesus how to pray, this is exactly what he said. Not a formula — a window into how he thought about God, people, and what actually matters.',
    scriptureRef:     'Matthew 6:9-13',
    url:              'https://www.biblegateway.com/passage/?search=Matthew+6%3A9-13&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 2,
    resonanceStyle:   'foundational',
  },
  {
    id:               3,
    tag:              'MILK',
    title:            'The Lost Sheep',
    description:      'Luke 15:3-7. Ninety-nine safe in the fold — and he leaves all of them to find the one that wandered. You are not the ninety-nine in this story. You are the one.',
    scriptureRef:     'Luke 15:3-7',
    url:              'https://www.biblegateway.com/passage/?search=Luke+15%3A3-7&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 2,
    resonanceStyle:   'emotional',
  },
  {
    id:               4,
    tag:              'MILK',
    title:            'The Prodigal Son',
    description:      'Luke 15:11-32. The son rehearsed his apology the whole walk home. His father never let him finish it. He ran — which was undignified for a man of his age. He didn\'t care.',
    scriptureRef:     'Luke 15:11-32',
    url:              'https://www.biblegateway.com/passage/?search=Luke+15%3A11-32&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 4,
    resonanceStyle:   'emotional',
  },
  {
    id:               5,
    tag:              'MILK',
    title:            'Come to Me, All Who Are Weary',
    description:      'Matthew 11:28-30. He didn\'t say come to me when you have it together. He said come to me weary, burdened, heavy. Come as you are. That\'s the invitation.',
    scriptureRef:     'Matthew 11:28-30',
    url:              'https://www.biblegateway.com/passage/?search=Matthew+11%3A28-30&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 2,
    resonanceStyle:   'comfort',
  },
  {
    id:               6,
    tag:              'MILK',
    title:            'Love Is Patient, Love Is Kind',
    description:      '1 Corinthians 13. The standard every human already reaches for — and almost none of us can sustain. Paul didn\'t write this to make you feel guilty. He wrote it to show you what love actually looks like when it\'s real.',
    scriptureRef:     '1 Corinthians 13',
    url:              'https://www.biblegateway.com/passage/?search=1+Corinthians+13&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 3,
    resonanceStyle:   'moral',
  },
  {
    id:               7,
    tag:              'MILK',
    title:            'Do Not Fear — I Am With You',
    description:      'Isaiah 41:10. Written six centuries before Jesus, to a people who had lost everything. It reads like it was written for right now because some things about human fear never change.',
    scriptureRef:     'Isaiah 41:10',
    url:              'https://www.biblegateway.com/passage/?search=Isaiah+41%3A10&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 2,
    resonanceStyle:   'comfort',
  },
  {
    id:               8,
    tag:              'MILK',
    title:            'The Beatitudes',
    description:      'Matthew 5:3-12. Blessed are the poor in spirit. The mourners. The meek. Jesus opened his most famous sermon by pronouncing blessing on everyone the world had written off. Nobody expected that opening.',
    scriptureRef:     'Matthew 5:3-12',
    url:              'https://www.biblegateway.com/passage/?search=Matthew+5%3A3-12&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 3,
    resonanceStyle:   'foundational',
  },
  {
    id:               9,
    tag:              'MILK',
    title:            'Consider the Lilies',
    description:      'Matthew 6:25-34. He pointed at birds and wildflowers to make his argument: if the Father takes care of them without them doing anything, why do you believe he\'s forgotten you?',
    scriptureRef:     'Matthew 6:25-34',
    url:              'https://www.biblegateway.com/passage/?search=Matthew+6%3A25-34&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 3,
    resonanceStyle:   'comfort',
  },
  {
    id:               10,
    tag:              'MILK',
    title:            'The Woman at the Well',
    description:      'John 4:1-42. She\'d had five husbands and the man she was with wasn\'t her husband. Jesus knew all of it. He didn\'t lead with any of it. He led with "give me a drink" — just a request between two people. The rest followed.',
    scriptureRef:     'John 4:1-42',
    url:              'https://www.biblegateway.com/passage/?search=John+4%3A1-42&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 6,
    resonanceStyle:   'personal',
  },
  {
    id:               11,
    tag:              'MILK',
    title:            'Nothing Can Separate Us',
    description:      'Romans 8:38-39. Paul lists everything that could possibly come between you and God\'s love — death, life, angels, present, future — and says none of it can. Nothing. Not even yourself.',
    scriptureRef:     'Romans 8:38-39',
    url:              'https://www.biblegateway.com/passage/?search=Romans+8%3A38-39&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 2,
    resonanceStyle:   'comfort',
  },
  {
    id:               12,
    tag:              'MILK',
    title:            'The Good Shepherd',
    description:      'John 10:1-18. He knows his sheep by name. Not by number, not by category. By name. And he said he lays down his life for them — voluntarily, not reluctantly.',
    scriptureRef:     'John 10:1-18',
    url:              'https://www.biblegateway.com/passage/?search=John+10%3A1-18&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 4,
    resonanceStyle:   'personal',
  },

  // ── BRIDGE ───────────────────────────────────────────────────────────────
  // Apologetics, evidence, skeptic-friendly.
  // Answers the questions skeptics actually ask without being condescending.

  {
    id:               13,
    tag:              'BRIDGE',
    title:            'The Historical Case for the Resurrection',
    description:      'Historians across the spectrum — including non-Christians — agree that something happened after the crucifixion that caused the disciples to completely change their behavior. The debate is about what. This article lays out the evidence without requiring faith to evaluate it.',
    scriptureRef:     '1 Corinthians 15:3-8',
    url:              'https://www.reasonablefaith.org/writings/popular-writings/jesus-of-nazareth/the-resurrection-of-jesus/',
    mediaType:        'article',
    estimatedMinutes: 8,
    resonanceStyle:   'historical',
  },
  {
    id:               14,
    tag:              'BRIDGE',
    title:            'Lord, Liar, or Lunatic — C.S. Lewis\'s Trilemma',
    description:      'C.S. Lewis was an Oxford atheist before he became a Christian. His argument: Jesus claimed to be God. That leaves only three options — he was lying, he was crazy, or he was telling the truth. Lewis argues you can\'t call him a "good moral teacher" and leave it there.',
    scriptureRef:     'John 8:58',
    url:              'https://www.cslewisinstitute.org/resources/mere-christianity/',
    mediaType:        'article',
    estimatedMinutes: 7,
    resonanceStyle:   'logical',
  },
  {
    id:               15,
    tag:              'BRIDGE',
    title:            'Isaiah 53: Written 700 Years Before the Crucifixion',
    description:      'Isaiah chapter 53 describes a man who is despised, rejected, pierced for our transgressions, buried with the rich, and seen alive again after his death. It was written over 700 years before Jesus was born. The Dead Sea Scrolls confirm the text hasn\'t changed.',
    scriptureRef:     'Isaiah 53',
    url:              'https://www.biblegateway.com/passage/?search=Isaiah+53&version=NIV',
    mediaType:        'article',
    estimatedMinutes: 5,
    resonanceStyle:   'historical',
  },
  {
    id:               16,
    tag:              'BRIDGE',
    title:            'What Historians Actually Say About Jesus',
    description:      'Even secular historians like Bart Ehrman — who does not believe Jesus was divine — agree he existed, was crucified under Pilate, and that his followers genuinely believed they saw him risen. This piece covers what the non-Christian sources say.',
    scriptureRef:     'Acts 26:26',
    url:              'https://ehrmanblog.org/did-jesus-exist/',
    mediaType:        'article',
    estimatedMinutes: 6,
    resonanceStyle:   'historical',
  },
  {
    id:               17,
    tag:              'BRIDGE',
    title:            'The Problem of Suffering: An Honest Response',
    description:      'If God exists and is good, why is there so much pain? This is the most serious objection to faith. This article doesn\'t offer easy answers — it offers the response that actually holds up: what suffering tells us about the kind of world love requires.',
    scriptureRef:     'Romans 8:28',
    url:              'https://www.reasonablefaith.org/writings/popular-writings/existence-nature-of-god/the-problem-of-evil/',
    mediaType:        'article',
    estimatedMinutes: 10,
    resonanceStyle:   'philosophical',
  },
  {
    id:               18,
    tag:              'BRIDGE',
    title:            'Faith and Science Are Not Enemies',
    description:      'Francis Collins led the Human Genome Project and is an evangelical Christian. He argues that science and faith occupy different domains — and that the deeper he went into the genome, the more he saw evidence of design. His story is worth reading.',
    scriptureRef:     'Psalm 19:1',
    url:              'https://biologos.org/about/our-story/',
    mediaType:        'article',
    estimatedMinutes: 7,
    resonanceStyle:   'logical',
  },
  {
    id:               19,
    tag:              'BRIDGE',
    title:            'Near-Death Experiences: What the Research Shows',
    description:      'The AWARE study at the University of Southampton documented verifiable out-of-body experiences during cardiac arrest — patients accurately described events they couldn\'t have observed while clinically dead. The data is hard to dismiss.',
    scriptureRef:     '2 Corinthians 12:2-4',
    url:              'https://www.sciencedirect.com/science/article/pii/S1053810014001245',
    mediaType:        'article',
    estimatedMinutes: 8,
    resonanceStyle:   'historical',
  },
  {
    id:               20,
    tag:              'BRIDGE',
    title:            'The Moral Argument: Why Objective Right and Wrong Points to God',
    description:      'If there is no God, moral statements like "torturing children for fun is wrong" are just preferences — not facts. But we don\'t actually believe that. The moral argument asks: what grounds the moral reality you already believe in?',
    scriptureRef:     'Romans 2:15',
    url:              'https://www.reasonablefaith.org/writings/popular-writings/existence-nature-of-god/the-moral-argument/',
    mediaType:        'article',
    estimatedMinutes: 6,
    resonanceStyle:   'philosophical',
  },
  {
    id:               21,
    tag:              'BRIDGE',
    title:            'The Empty Tomb: Four Facts Every Scholar Agrees On',
    description:      'There are four facts about the aftermath of the crucifixion that virtually all New Testament historians — Christian and non-Christian — accept as established. Gary Habermas has catalogued over 1,400 scholarly sources. This is the minimal facts argument.',
    scriptureRef:     'Mark 16:6',
    url:              'https://www.garyhabermas.com/articles/crj_probablytrue/crj_probablytrue.htm',
    mediaType:        'article',
    estimatedMinutes: 9,
    resonanceStyle:   'historical',
  },
  {
    id:               22,
    tag:              'BRIDGE',
    title:            'Why Did the Disciples Die for This?',
    description:      'People die for things they believe are true. Nobody dies for something they know is a lie. The disciples were not just willing to say they saw Jesus risen — they were willing to be tortured and executed rather than recant. That\'s a different kind of evidence.',
    scriptureRef:     'Acts 7:59-60',
    url:              'https://crossexamined.org/why-did-the-disciples-die-for-their-claims/',
    mediaType:        'article',
    estimatedMinutes: 5,
    resonanceStyle:   'logical',
  },

  // ── RESTORATION ──────────────────────────────────────────────────────────
  // For users who have moved through MILK and BRIDGE.
  // Introduces the specific Latter-day Saint claim honestly.

  {
    id:               23,
    tag:              'RESTORATION',
    title:            'The Apostasy and Why It Matters',
    description:      'After the apostles were killed, something happened to the early church — the authority, the priesthood, the direct revelation. This piece explains what the Great Apostasy means, why it was prophesied, and why the Restoration is the answer to a question Christianity has been sitting with for centuries.',
    scriptureRef:     'Amos 3:7',
    url:              'https://www.churchofjesuschrist.org/study/manual/gospel-topics/apostasy',
    mediaType:        'article',
    estimatedMinutes: 8,
    resonanceStyle:   'doctrinal',
  },
  {
    id:               24,
    tag:              'RESTORATION',
    title:            'Joseph Smith\'s First Vision: What He Said and Why It Matters',
    description:      'A fourteen-year-old boy went into a grove of trees to ask God which church to join. What he said happened next is the founding claim of The Church of Jesus Christ of Latter-day Saints. Here is the account in his own words — and why it demands a verdict.',
    scriptureRef:     'James 1:5',
    url:              'https://www.churchofjesuschrist.org/study/history/topics/first-vision-accounts',
    mediaType:        'article',
    estimatedMinutes: 10,
    resonanceStyle:   'historical',
  },
  {
    id:               25,
    tag:              'RESTORATION',
    title:            'The Book of Mormon: A Second Witness for Jesus Christ',
    description:      'Not a replacement for the Bible — an additional witness. The Book of Mormon was translated by Joseph Smith from ancient plates and covers the ministry of Jesus Christ to people in the ancient Americas. Here is how to read the first chapter with an open mind.',
    scriptureRef:     'John 10:16',
    url:              'https://www.churchofjesuschrist.org/study/scriptures/bofm/1-ne/1',
    mediaType:        'article',
    estimatedMinutes: 12,
    resonanceStyle:   'study',
  },

  // ── MAINTENANCE ──────────────────────────────────────────────────────────
  // For active or returning Latter-day Saints.
  // Discipleship content that deepens existing covenant relationship.

  {
    id:               26,
    tag:              'MAINTENANCE',
    title:            'Walking the Covenant Path',
    description:      'The covenant path isn\'t a checklist — it\'s a relationship. Elder Bednar explains what covenants actually are, how they work, and why staying on the path during hard years is different from white-knuckling through them.',
    scriptureRef:     'Mosiah 18:8-10',
    url:              'https://www.churchofjesuschrist.org/study/general-conference/2021/10/51bednar',
    mediaType:        'article',
    estimatedMinutes: 9,
    resonanceStyle:   'doctrinal',
  },
  {
    id:               27,
    tag:              'MAINTENANCE',
    title:            'Come, Follow Me: Getting More From Your Scripture Study',
    description:      'The Come Follow Me curriculum changed how the Church approaches home-centered learning. This guide explains how to get past surface-level reading into genuine daily study — with your family or alone.',
    scriptureRef:     '2 Timothy 3:16-17',
    url:              'https://www.churchofjesuschrist.org/study/come-follow-me',
    mediaType:        'article',
    estimatedMinutes: 6,
    resonanceStyle:   'study',
  },
  {
    id:               28,
    tag:              'MAINTENANCE',
    title:            'The Temple: Understanding What Happens There',
    description:      'Many members attend the temple for years before they understand why. Elder Anderson\'s talk on the endowment — what it means, what it does, and why it is worth keeping sacred — is the clearest explanation for members who want to go deeper.',
    scriptureRef:     'Doctrine and Covenants 109:22',
    url:              'https://www.churchofjesuschrist.org/study/general-conference/2021/04/34anderson',
    mediaType:        'article',
    estimatedMinutes: 8,
    resonanceStyle:   'doctrinal',
  },
  {
    id:               29,
    tag:              'MAINTENANCE',
    title:            'Ministering: More Than Visiting',
    description:      'The Church replaced home and visiting teaching with Ministering in 2018. President Nelson explained why the change goes deeper than a name swap — it\'s about becoming the kind of disciple who actually knows the people they serve.',
    scriptureRef:     'Moroni 6:4',
    url:              'https://www.churchofjesuschrist.org/study/general-conference/2018/04/ministering',
    mediaType:        'article',
    estimatedMinutes: 7,
    resonanceStyle:   'devotional',
  },
  {
    id:               30,
    tag:              'MAINTENANCE',
    title:            'Strength for the Hard Years: When Faith Feels Thin',
    description:      'Every long-term member has periods where faith feels more like discipline than fire. Elder Holland\'s talk for those years — not a pep talk, but an honest acknowledgment that God knows where you are and what this season costs you.',
    scriptureRef:     'Mark 9:24',
    url:              'https://www.churchofjesuschrist.org/study/general-conference/2013/10/like-a-broken-vessel',
    mediaType:        'article',
    estimatedMinutes: 10,
    resonanceStyle:   'emotional',
  },

  // ── ADDED 2026-06-15: more at every level. Bible refs -> BibleGateway;
  // Restoration/member refs -> stable churchofjesuschrist.org study URLs. ──

  {
    id: 31, tag: 'MILK', title: 'Come Unto Me',
    description: "Matthew 11:28-30. \"Come unto me, all ye that labour and are heavy laden, and I will give you rest.\" The most open invitation Jesus ever gave — no conditions, no test to pass first.",
    scriptureRef: 'Matthew 11:28-30',
    url: 'https://www.biblegateway.com/passage/?search=Matthew+11%3A28-30&version=NIV',
    mediaType: 'article', estimatedMinutes: 2, resonanceStyle: 'comfort',
  },
  {
    id: 32, tag: 'MILK', title: 'The Good Shepherd',
    description: "John 10:11-14. He calls his own by name, and he lays his life down for them. A shepherd who knows you, not a crowd he is managing.",
    scriptureRef: 'John 10:11-14',
    url: 'https://www.biblegateway.com/passage/?search=John+10%3A11-14&version=NIV',
    mediaType: 'article', estimatedMinutes: 2, resonanceStyle: 'emotional',
  },
  {
    id: 33, tag: 'MILK', title: 'Do Not Be Anxious',
    description: "Matthew 6:25-34. Look at the birds; look at the lilies. Jesus on worry — not a scolding, but a Father pointing at how cared-for the smallest things already are.",
    scriptureRef: 'Matthew 6:25-34',
    url: 'https://www.biblegateway.com/passage/?search=Matthew+6%3A25-34&version=NIV',
    mediaType: 'article', estimatedMinutes: 3, resonanceStyle: 'comfort',
  },
  {
    id: 34, tag: 'MILK', title: 'Neither Do I Condemn You',
    description: "John 8:2-11. The woman they were ready to stone. He did not excuse what was wrong — but he did not let them crush her either. Mercy and truth in the same breath.",
    scriptureRef: 'John 8:2-11',
    url: 'https://www.biblegateway.com/passage/?search=John+8%3A2-11&version=NIV',
    mediaType: 'article', estimatedMinutes: 3, resonanceStyle: 'emotional',
  },
  {
    id: 35, tag: 'BRIDGE', title: 'When God Feels Far in Suffering',
    description: "Romans 8:18-28. Not a tidy answer to pain, but the honest claim that nothing — not even the worst of it — is wasted or outside what God can work with.",
    scriptureRef: 'Romans 8:18-28',
    url: 'https://www.biblegateway.com/passage/?search=Romans+8%3A18-28&version=NIV',
    mediaType: 'article', estimatedMinutes: 4, resonanceStyle: 'philosophical',
  },
  {
    id: 36, tag: 'BRIDGE', title: 'The Evidence for the Resurrection',
    description: "1 Corinthians 15:3-8. Paul lists the eyewitnesses — most still alive when he wrote, able to be questioned. The earliest claim, not a later legend.",
    scriptureRef: '1 Corinthians 15:3-8',
    url: 'https://www.biblegateway.com/passage/?search=1+Corinthians+15%3A3-8&version=NIV',
    mediaType: 'article', estimatedMinutes: 4, resonanceStyle: 'historical',
  },
  {
    id: 37, tag: 'BRIDGE', title: 'Lord, I Believe — Help My Unbelief',
    description: "Mark 9:24. The most honest prayer in the Bible. Faith and doubt in the same sentence, and Jesus answered it. You do not have to resolve the doubt before you are welcome.",
    scriptureRef: 'Mark 9:24',
    url: 'https://www.biblegateway.com/passage/?search=Mark+9%3A24&version=NIV',
    mediaType: 'article', estimatedMinutes: 2, resonanceStyle: 'personal',
  },
  {
    id: 38, tag: 'RESTORATION', title: 'Joseph Smith — The First Vision (his own account)',
    description: "Joseph Smith—History 1. A boy asks which church is true and says he saw the Father and the Son. Whatever you conclude, read the claim in his own words first.",
    scriptureRef: 'Joseph Smith—History 1:15-20',
    url: 'https://www.churchofjesuschrist.org/study/scriptures/pgp/js-h/1',
    mediaType: 'article', estimatedMinutes: 8, resonanceStyle: 'historical',
  },
  {
    id: 39, tag: 'RESTORATION', title: "Moroni's Promise",
    description: "Moroni 10:3-5. The Book of Mormon's own invitation: read it, then ask God sincerely whether it is true. It stakes everything on a personal answer, not an argument.",
    scriptureRef: 'Moroni 10:3-5',
    url: 'https://www.churchofjesuschrist.org/study/scriptures/bofm/moro/10',
    mediaType: 'article', estimatedMinutes: 3, resonanceStyle: 'doctrinal',
  },
  {
    id: 40, tag: 'RESTORATION', title: 'Another Testament of Jesus Christ',
    description: "2 Nephi 33. Why a second witness of Christ alongside the Bible — not to replace it, but to testify of the same Jesus to a world that needs more, not less, of him.",
    scriptureRef: '2 Nephi 33:10-11',
    url: 'https://www.churchofjesuschrist.org/study/scriptures/bofm/2-ne/33',
    mediaType: 'article', estimatedMinutes: 4, resonanceStyle: 'doctrinal',
  },
  {
    id: 41, tag: 'RESTORATION', title: 'Why We Are Here — The Plan',
    description: "Alma 40-42. Where we came from, why life is hard, what happens after — the restored gospel's answer to the questions every honest person eventually asks.",
    scriptureRef: 'Alma 42',
    url: 'https://www.churchofjesuschrist.org/study/scriptures/bofm/alma/42',
    mediaType: 'article', estimatedMinutes: 9, resonanceStyle: 'doctrinal',
  },
  {
    id: 42, tag: 'RESTORATION', title: 'God Still Speaks Today',
    description: "Doctrine and Covenants 1:37-38. The claim that revelation did not end with the Bible — that God speaks now, through prophets, the same way he always has.",
    scriptureRef: 'D&C 1:37-38',
    url: 'https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/1',
    mediaType: 'article', estimatedMinutes: 3, resonanceStyle: 'doctrinal',
  },
  {
    id: 43, tag: 'MAINTENANCE', title: 'Feast Upon the Words of Christ',
    description: "2 Nephi 32:3. Not just read — feast. A pattern for daily scripture study that feeds rather than checks a box, and tells you the very things you should do.",
    scriptureRef: '2 Nephi 32:3',
    url: 'https://www.churchofjesuschrist.org/study/scriptures/bofm/2-ne/32',
    mediaType: 'article', estimatedMinutes: 3, resonanceStyle: 'devotional',
  },
  {
    id: 44, tag: 'MAINTENANCE', title: 'The Sacrament — Renewing the Covenant',
    description: "D&C 20:77-79. The prayers, word for word. What you are actually promising each week, and what is promised back — to always have his Spirit with you.",
    scriptureRef: 'D&C 20:77-79',
    url: 'https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/20',
    mediaType: 'article', estimatedMinutes: 4, resonanceStyle: 'devotional',
  },
  {
    id: 45, tag: 'MAINTENANCE', title: "Bear One Another's Burdens",
    description: "Mosiah 18:8-9. The baptismal covenant in plain terms — to mourn with those that mourn, comfort those that need it. Ministering is not a program; it is the covenant.",
    scriptureRef: 'Mosiah 18:8-9',
    url: 'https://www.churchofjesuschrist.org/study/scriptures/bofm/mosiah/18',
    mediaType: 'article', estimatedMinutes: 3, resonanceStyle: 'moral',
  },
  {
    id: 46, tag: 'MAINTENANCE', title: 'Press Forward With a Brightness of Hope',
    description: "2 Nephi 31:20. After baptism — what then? Endure, yes, but with a feast of hope and love, not grim duty. The shape of a life that keeps moving toward Christ.",
    scriptureRef: '2 Nephi 31:20',
    url: 'https://www.churchofjesuschrist.org/study/scriptures/bofm/2-ne/31',
    mediaType: 'article', estimatedMinutes: 3, resonanceStyle: 'devotional',
  },
];

export function getContentByTag(tag: FeedTag): ContentItem[] {
  return CONTENT.filter(item => item.tag === tag);
}

export function getContentById(id: number): ContentItem | undefined {
  return CONTENT.find(item => item.id === id);
}
