// MBM content generator — authors the milk/meat corpus into mobile/src/data/content.ts.
// Run from MBM root: node gen_content.js
const fs = require('fs');
const path = require('path');

const bg = (ref) =>
  `https://www.biblegateway.com/passage/?search=${encodeURIComponent(ref)}&version=KJV`;

// Latter-day Saint scripture book codes for churchofjesuschrist.org study links.
const LDS_BOOK = {
  '1 Nephi':'bofm/1-ne','2 Nephi':'bofm/2-ne','Jacob':'bofm/jacob','Enos':'bofm/enos',
  'Jarom':'bofm/jarom','Omni':'bofm/omni','Mosiah':'bofm/mosiah','Alma':'bofm/alma',
  'Helaman':'bofm/hel','3 Nephi':'bofm/3-ne','4 Nephi':'bofm/4-ne','Mormon':'bofm/morm',
  'Ether':'bofm/ether','Moroni':'bofm/moro',
  'Doctrine and Covenants':'dc-testament/dc',
  'Moses':'pgp/moses','Abraham':'pgp/abr','Joseph Smith\u2014History':'pgp/js-h',
  'Articles of Faith':'pgp/a-of-f',
};
const lds = (ref) => {
  // Book + first chapter number (handles "Alma 36", "2 Nephi 2:25", "3 Nephi 12-14").
  const m = ref.match(/^(.*?)\s+(\d+)/);
  if (!m) throw new Error('bad LDS ref: ' + ref);
  const code = LDS_BOOK[m[1]];
  if (!code) throw new Error('no LDS book code for "' + m[1] + '" (ref ' + ref + ')');
  return `https://www.churchofjesuschrist.org/study/scriptures/${code}/${m[2]}`;
};

// ── MILK — 50 verses both traditions love (God is good) ──────────────────────
// [title, ref, description, resonanceStyle, minutes]
const milkCommon = [
  ['Peace I Leave With You','John 14:27',"Not the world's kind of peace — a peace that doesn't depend on circumstances. He said it the night before he died.",'comfort',2],
  ['Come Unto Me','Matthew 11:28-30',"Come unto me, all ye that labour and are heavy laden. The invitation is open and the yoke is easy.",'comfort',2],
  ['The Lord Is My Shepherd','Psalm 23','The most beloved psalm — green pastures, still waters, a table prepared, and goodness following you all your days.','comfort',3],
  ['For God So Loved the World','John 3:16','The whole gospel in one sentence: love so wide it gave everything so that none need perish.','foundational',1],
  ['The Prodigal Son','Luke 15:11-32','While the son was still a long way off, the father ran to him. The picture of how God receives anyone who turns back.','emotional',4],
  ['The Lost Sheep','Luke 15:3-7','He leaves the ninety-nine to find the one. In this story you are not the ninety-nine — you are the one.','emotional',2],
  ['The Woman Caught','John 8:1-11',"Neither do I condemn thee. Mercy that doesn't excuse the sin but refuses to crush the person.",'moral',3],
  ['The Beatitudes','Matthew 5:3-12',"Blessed are the poor in spirit, the mourners, the meek. Jesus turns the world's whole scoreboard upside down.",'devotional',3],
  ['Jesus Wept','John 11:35','The shortest verse in the Bible, and one of the deepest. God stood at a grave and cried.','emotional',1],
  ['The Good Samaritan','Luke 10:25-37','The one who showed mercy was the neighbor — even though he was the outsider. Go and do likewise.','moral',3],
  ["The Lord's Prayer",'Matthew 6:9-13','When the disciples asked how to pray, this is what he said. A window into how he saw God and people.','foundational',2],
  ['Fear Thou Not','Isaiah 41:10','Fear not, for I am with thee; I will strengthen thee; I will uphold thee with my right hand.','comfort',1],
  ['God Is Our Refuge','Psalm 46:1','A very present help in trouble. Not a distant help — a present one.','comfort',1],
  ['Nothing Can Separate Us','Romans 8:38-39','Not death, not life, not anything in all creation can separate you from the love of God in Christ.','comfort',2],
  ['Ask, and It Shall Be Given','Matthew 7:7','Ask, seek, knock. The doors of heaven are not locked against the one who is looking.','devotional',1],
  ['The Good Shepherd','John 10:11','The good shepherd gives his life for the sheep. He does not run when the wolf comes.','comfort',2],
  ['She Touched His Cloak','Mark 5:25-34',"She didn't even ask — she just reached. He turned, found her, and called her daughter.",'emotional',3],
  ['Zacchaeus','Luke 19:1-10','Jesus invited himself to dinner with the most hated man in town. The Son of Man came to seek and save.','emotional',3],
  ['The Woman at the Well','John 4:1-26','He asked a stranger for water and offered her living water. He told her everything she ever did — and stayed.','personal',4],
  ['Peter Walks on Water','Matthew 14:22-33','He did walk — until he looked at the storm. And when he sank, the hand was already there.','personal',3],
  ['The Peace of God','Philippians 4:6-7','Be anxious for nothing. The peace that passes understanding will guard your heart.','comfort',2],
  ['Near the Brokenhearted','Psalm 34:18','The Lord is nigh unto them that are of a broken heart. Nearness, not distance, is his response to pain.','comfort',1],
  ['He Will Wipe Away Every Tear','Revelation 21:4','No more death, sorrow, crying, or pain. The former things will pass away.','comfort',1],
  ['Love Is Patient','1 Corinthians 13:4-7','Love suffers long and is kind. It bears, believes, hopes, and endures all things.','devotional',2],
  ['The Light of the World','Matthew 5:14-16','You are the light of the world. Let it shine — not to be seen, but so others find their way.','devotional',2],
  ['Love One Another','John 13:34-35','A new commandment: love one another as I have loved you. By this all will know you are mine.','moral',2],
  ['Father, Forgive Them','Luke 23:34','From the cross, his first words were mercy for the people killing him. They know not what they do.','emotional',1],
  ['I Am With You Always','Matthew 28:20','Lo, I am with you alway, even unto the end of the world. The last promise he made.','comfort',1],
  ['Be Strong and Courageous','Joshua 1:9','Be not afraid, neither be thou dismayed: the Lord thy God is with thee whithersoever thou goest.','comfort',1],
  ['Plans to Give You Hope','Jeremiah 29:11','Thoughts of peace, and not of evil, to give you an expected end. God\u2019s intentions toward you are good.','comfort',1],
  ['Trust in the Lord','Proverbs 3:5-6','Trust with all your heart and lean not on your own understanding. He will direct your paths.','devotional',1],
  ['Consider the Lilies','Matthew 6:25-34','Take no thought for your life. If he clothes the grass, how much more will he care for you?','comfort',3],
  ['Many Mansions','John 14:1-3',"Let not your heart be troubled. In my Father's house are many mansions; I go to prepare a place for you.",'comfort',2],
  ['The Pharisee and the Publican','Luke 18:9-14','One bragged; one beat his chest and begged for mercy. It was the second man who went home justified.','moral',2],
  ['Seventy Times Seven','Matthew 18:21-22','How often shall I forgive? Not seven times, but seventy times seven. Forgiveness without a ceiling.','moral',1],
  ['Suffer the Little Children','Mark 10:13-16','He was indignant when they shooed the children away. Of such is the kingdom of God.','emotional',2],
  ['She Loved Much','Luke 7:36-50','She washed his feet with tears. Her sins, which are many, are forgiven; for she loved much.','emotional',3],
  ['Greater Love Hath No Man','John 15:13','That a man lay down his life for his friends. The measure of the love he was about to show.','devotional',1],
  ['Whither Shall I Go','Psalm 139:7-10','If I make my bed in hell, thou art there. There is nowhere you can go that he is not already.','comfort',2],
  ['By His Stripes','Isaiah 53:3-5','A man of sorrows, acquainted with grief. He was wounded for our transgressions; with his stripes we are healed.','devotional',2],
  ['Moved With Compassion','Matthew 9:36','He saw the crowds as sheep without a shepherd, and was moved with compassion. What he feels when he sees you.','emotional',1],
  ['Judge Not','Luke 6:37','Judge not, and ye shall not be judged. Forgive, and ye shall be forgiven.','moral',1],
  ['I Have Overcome the World','John 16:33','In the world ye shall have tribulation: but be of good cheer; I have overcome the world.','comfort',1],
  ['My Grace Is Sufficient','2 Corinthians 12:9','My strength is made perfect in weakness. The thorn stayed — but so did the grace.','comfort',2],
  ['I Will Never Leave Thee','Hebrews 13:5','Be content with what you have, for he has said: I will never leave thee, nor forsake thee.','comfort',1],
  ['Joy Cometh in the Morning','Psalm 30:5','Weeping may endure for a night, but joy cometh in the morning. The night is real — and it ends.','comfort',1],
  ['Love Your Enemies','Matthew 5:43-48','Love your enemies, bless them that curse you. The hardest teaching, and the most like him.','moral',2],
  ['Every Hair Numbered','Luke 12:6-7','Not one sparrow is forgotten before God. The very hairs of your head are all numbered. Fear not.','comfort',2],
  ['I Am the Bread of Life','John 6:35','He that cometh to me shall never hunger. The hunger underneath all the other hungers.','devotional',1],
  ['His Mercies Are New','Lamentations 3:22-23',"It is of the Lord's mercies that we are not consumed. They are new every morning; great is thy faithfulness.",'comfort',1],
];

// ── MILK — 50 often-skipped passages that raise restored-gospel questions ─────
// [title, ref, description, ldsLens, resonanceStyle, minutes]
const milkRestoration = [
  ['Ye Are Gods','John 10:34',"Accused of blasphemy, Jesus answers by quoting the Psalms: 'Ye are gods.' He doesn't soften it — he leans in.","Jesus cites Psalm 82:6 to defend calling himself God's Son. Why point to a verse about humans being called gods? Latter-day Saints read our divine potential as God's literal children here.",'doctrinal',3],
  ['Baptism for the Dead','1 Corinthians 15:29','Paul asks, almost in passing, why people are baptized for the dead — as if everyone already knew the practice.',"Paul mentions it with no rebuke, as a known practice, to argue for resurrection. What happens to those who died never hearing the gospel? Latter-day Saints see a merciful answer.",'study',2],
  ['Sit With Me in My Throne','Revelation 3:21','To him that overcometh will I grant to sit with me in my throne, even as I overcame and sat with my Father.',"Christ promises the faithful his own throne — the same relationship he has with the Father. A startling picture of what 'joint-heirs' really means.",'doctrinal',2],
  ['Three at the Baptism','Matthew 3:16-17','At his baptism the Son is in the water, the Spirit descends as a dove, and the Father speaks from heaven.',"All three are present and distinct at one moment — Son below, Spirit descending, Father speaking. What does that say about whether they are one being or one in purpose?",'doctrinal',2],
  ['That They May Be One','John 17:20-23','Jesus prays that his followers may be one — as he and the Father are one. The unity he wants for us is the unity he has.',"He defines oneness with the Father by asking for the SAME oneness among believers — clearly unity of heart and purpose, since we stay distinct persons. A key to the Godhead.",'doctrinal',3],
  ['The Offspring of God','Acts 17:28-29','Paul tells the philosophers at Athens: we are the offspring of God. Not his creatures only — his offspring.',"Paul approvingly quotes poets that we are God's offspring, then says we shouldn't picture God as lifeless stone. If we are his offspring, what are we meant to become?",'doctrinal',2],
  ['Heirs of God','Romans 8:16-17','The Spirit witnesses that we are children of God — and if children, then heirs: joint-heirs with Christ.','An heir inherits what the parent has. Paul says we are joint-heirs with Christ. Heirs to WHAT, exactly?','doctrinal',2],
  ['The Father of Spirits','Hebrews 12:9',"We had earthly fathers; shall we not rather be in subjection to the Father of spirits, and live?","The phrase implies our spirits have a Father — a relationship that existed before this life. It opens the question of where we came from.",'doctrinal',2],
  ['If Any Lack Wisdom','James 1:5','If any of you lack wisdom, let him ask of God, that giveth to all men liberally — and it shall be given him.','This single verse sent a 14-year-old named Joseph Smith into a grove to pray. What happens when someone takes the promise literally?','foundational',2],
  ['God Reveals to Prophets','Amos 3:7','Surely the Lord God will do nothing, but he revealeth his secret unto his servants the prophets.',"If God acts through prophets, would he stop having them just when the world needs them most? Latter-day Saints say he didn't.",'doctrinal',1],
  ['Apostles and Prophets','Ephesians 2:19-20','The household of God is built on the foundation of the apostles and prophets, Jesus Christ the chief corner stone.','Paul says the Church\u2019s foundation is apostles and prophets. Can the Church Christ built stand without the foundation he gave it?','doctrinal',2],
  ['Till We All Come to Unity','Ephesians 4:11-14','He gave apostles, prophets, evangelists, pastors and teachers — until we all come to the unity of the faith.',"Their PURPOSE: unity, and to stop us being 'tossed about with every wind of doctrine.' With thousands of denominations today, the question asks itself.",'doctrinal',3],
  ['One God, Many Called Gods','1 Corinthians 8:5-6','There be that are called gods, whether in heaven or in earth — but to us there is but one God, the Father.','Paul names the Father and the Lord Jesus Christ separately while affirming we worship one. A careful reader notices Father and Son listed as distinct.','doctrinal',2],
  ['My Father Is Greater Than I','John 14:28','If ye loved me, ye would rejoice, because I said, I go unto the Father: for my Father is greater than I.','Jesus plainly says the Father is greater than he is. An honest look at the relationship between the Father and the Son.','doctrinal',1],
  ['Degrees of Glory','1 Corinthians 15:40-42','There are bodies celestial and bodies terrestrial; the glory of the sun, the moon, and the stars all differ.','Paul compares the resurrection to differing glories of sun, moon, and stars. Heaven may not be one undifferentiated place — Latter-day Saints see three degrees of glory.','study',2],
  ['The Son Can Do Nothing Alone','John 5:19','The Son can do nothing of himself, but what he seeth the Father do: these also doeth the Son likewise.','Jesus describes watching and following his Father — two persons working in perfect harmony. What does it reveal about the Godhead?','doctrinal',1],
  ['Judged According to Works','Revelation 20:12','The dead were judged out of those things written in the books, according to their works.','Scripture repeatedly ties judgment to works, not faith alone. How do grace and works fit together? Latter-day Saint theology offers a clear answer.','doctrinal',2],
  ['Preached to the Spirits in Prison','1 Peter 3:18-20','Christ, put to death in the flesh but quickened by the Spirit, went and preached unto the spirits in prison.','Between his death and resurrection, Christ preached to the dead. It answers a question that troubles many: what about those who never heard?','study',2],
  ['The Gospel Preached to the Dead','1 Peter 4:6','For this cause was the gospel preached also to them that are dead, that they might live according to God.','Peter says the gospel reaches even the dead, so they can be judged fairly. Read with 1 Corinthians 15:29, a picture of mercy for all generations emerges.','study',1],
  ['Born of Water and Spirit','John 3:5','Except a man be born of water and of the Spirit, he cannot enter into the kingdom of God.','Jesus tells Nicodemus both baptism (water) and the Spirit are required. Is baptism optional or essential?','doctrinal',2],
  ['The Keys of the Kingdom','Matthew 16:18-19','Upon this rock I will build my church; and I will give unto thee the keys of the kingdom of heaven.',"Jesus gives Peter 'keys' — authority to bind on earth and in heaven. Who holds that authority today, and how is it passed on?",'doctrinal',2],
  ['Restitution of All Things','Acts 3:20-21','Heaven must receive him until the times of restitution of all things, spoken by all the holy prophets.',"Peter says before Christ returns there must be a 'restitution' — a restoring. Restoring implies something was lost. What, and when?",'doctrinal',2],
  ['Elijah Shall Come','Malachi 4:5-6','I will send you Elijah the prophet, and he shall turn the heart of the fathers to the children, and the children to the fathers.','The Old Testament closes promising Elijah will return to turn hearts of parents and children to each other. Latter-day Saints connect this to temples and family sealing.','doctrinal',2],
  ['Other Sheep','John 10:16','Other sheep I have, which are not of this fold: them also I must bring, and they shall hear my voice.','Jesus speaks of other sheep, not of the fold at Jerusalem, who would also hear him. Who were they, and did their record survive?','study',2],
  ['Two Sticks, One Hand','Ezekiel 37:15-17','Take the stick of Judah and the stick of Joseph, and join them one to another into one stick in thine hand.','Ezekiel is told to join the record of Judah and the record of Joseph into one. Latter-day Saints read the Bible and the Book of Mormon coming together here.','study',2],
  ['A Voice From the Dust','Isaiah 29:4',"Thou shalt be brought down, and shalt speak out of the ground, and thy voice shall be as one that hath a familiar spirit, out of the dust.","Isaiah describes a fallen people whose words would later whisper out of the dust. What record could speak from the ground centuries later?",'study',2],
  ['The Sealed Book','Isaiah 29:11-14',"The vision is become as a book that is sealed, which men deliver to one that is learned, and he saith, I cannot; for it is sealed.","Isaiah foresees a sealed book and a marvelous work. The story of the learned man who couldn't read it has a striking historical echo Latter-day Saints point to.",'study',3],
  ['Faith Without Works','James 2:17-18','Faith, if it hath not works, is dead, being alone. Shew me thy faith without thy works, and I will shew thee my faith by my works.',"James says faith alone is dead. It sits in tension with 'faith only' teaching and invites a careful look at how salvation actually works.",'doctrinal',2],
  ['The Angel With the Gospel','Revelation 14:6-7','I saw another angel fly in the midst of heaven, having the everlasting gospel to preach unto them that dwell on the earth.','John sees an angel bringing the everlasting gospel back to the earth in the last days. Why would the gospel need to be brought again?','doctrinal',2],
  ['Called of God','Hebrews 5:4','No man taketh this honour unto himself, but he that is called of God, as was Aaron.','Priesthood authority must be given by God — not taken or self-claimed. How is that authority conferred today?','doctrinal',2],
  ['I Have Ordained You','John 15:16','Ye have not chosen me, but I have chosen you, and ordained you, that ye should go and bring forth fruit.',"Jesus says he ordained his apostles — they didn't appoint themselves. It points to authority given by the laying on of hands.",'doctrinal',1],
  ['Not Everyone Who Says Lord','Matthew 7:21',"Not every one that saith unto me, Lord, Lord, shall enter the kingdom; but he that doeth the will of my Father.","Jesus ties entering the kingdom to DOING the Father's will, not merely professing his name. What does that doing include?",'moral',1],
  ['One Body, Many Members','1 Corinthians 12:13-27','The body is not one member, but many. The eye cannot say to the hand, I have no need of thee.','Paul describes Christ\u2019s Church as one ordered body with many offices. Does that organized structure exist today?','doctrinal',2],
  ['Repent and Be Baptized','Acts 2:38-39','Repent, and be baptized every one of you for the remission of sins, and ye shall receive the gift of the Holy Ghost.','Peter lays out the pattern: faith, repentance, baptism, the gift of the Holy Ghost. Does that exact order still matter?','foundational',2],
  ['Signs Follow Believers','Mark 16:15-18','These signs shall follow them that believe; In my name shall they cast out devils; they shall speak with new tongues.','Jesus says signs and spiritual gifts would follow believers. Should those gifts still be present in his Church?','study',2],
  ['The Doctrine of Baptisms','Hebrews 6:1-2',"Leaving the principles of the doctrine of Christ — of the doctrine of baptisms, and of laying on of hands.","Paul lists 'baptisms' (plural) and laying on of hands among the FIRST principles. The plural and the ordinance of hands both invite a closer look.",'doctrinal',2],
  ['Laying On of Hands','Acts 8:14-17','Then laid they their hands on them, and they received the Holy Ghost.','The Samaritans were baptized, but received the Holy Ghost only when apostles laid hands on them. It points to a specific ordinance and authority.','doctrinal',2],
  ['Buried With Him in Baptism','Romans 6:3-5','We are buried with him by baptism into death: that we should walk in newness of life.','Paul describes baptism as a burial and resurrection — fitting immersion, not sprinkling. The symbolism raises the question of the proper mode.','doctrinal',2],
  ['Neither Man Without the Woman','1 Corinthians 11:11',"Neither is the man without the woman, neither the woman without the man, in the Lord.","Paul says man and woman are not complete without each other 'in the Lord.' Latter-day Saints connect this to marriage that continues beyond this life.",'doctrinal',1],
  ['Let Us Make Man','Genesis 1:26-27',"And God said, Let us make man in our image, after our likeness. So God created man in his own image.","God speaks in the plural — 'us,' 'our' — and makes man in his image. Both the plural and the image raise questions about the nature of God and of us.",'doctrinal',2],
  ['Kings and Priests','Revelation 1:6',"And hath made us kings and priests unto God and his Father; to him be glory and dominion for ever.","John says Christ has made believers 'kings and priests unto God.' A striking statement of what the redeemed are meant to become.",'doctrinal',1],
  ['We Shall Reign','Revelation 5:10','And hast made us unto our God kings and priests: and we shall reign on the earth.','The redeemed are promised they will reign — a future of shared glory, not mere survival. It enlarges the picture of salvation.','doctrinal',1],
  ['Many Things Not Written','John 21:25','And there are also many other things which Jesus did, which, if written every one, the world could not contain the books.','The Bible itself says not everything was written. Could God still have more to say?','study',1],
  ['Yet Many Things to Say','John 16:12-13',"I have yet many things to say unto you, but ye cannot bear them now. The Spirit will guide you into all truth.","Jesus held things back his disciples weren't ready for, promising more by the Spirit. It opens the door to continuing revelation.",'doctrinal',2],
  ['A Famine of Hearing','Amos 8:11-12','I will send a famine in the land, not of bread, but of hearing the words of the Lord — they shall run to and fro to seek it.','Amos foresees a famine of revelation — a time the word of the Lord would be hard to find. Did such a famine ever come?','doctrinal',2],
  ['The Broken Covenant','Isaiah 24:5',"The earth is defiled because they have transgressed the laws, changed the ordinance, broken the everlasting covenant.","Isaiah warns of a time when people would change God's ordinances and break the covenant. It points toward an apostasy — and the need for a restoration.",'doctrinal',2],
  ['A Falling Away First','2 Thessalonians 2:1-3',"That day shall not come, except there come a falling away first, and that man of sin be revealed.","Paul warns that before Christ returns there would be a great 'falling away.' When did it happen, and what would set it right?",'doctrinal',2],
  ['Grievous Wolves','Acts 20:29-30','After my departing shall grievous wolves enter in among you; also of your own selves shall men arise speaking perverse things.','Paul predicts that after the apostles, false teachers would rise from within. A sober forecast of how the early Church would lose its way.','doctrinal',2],
  ['A Kingdom That Stands Forever','Daniel 2:44','In the days of these kings shall the God of heaven set up a kingdom, which shall never be destroyed, and shall stand for ever.','Daniel foresees God setting up a final kingdom that fills the earth and never falls. When would that latter-day kingdom begin?','doctrinal',2],
  ['Be Ye Therefore Perfect','Matthew 5:48','Be ye therefore perfect, even as your Father which is in heaven is perfect.','Jesus holds up the Father himself as the standard we are growing toward. Latter-day Saints read a real, gradual becoming here — not a demand for the impossible, but an invitation to grow into the family likeness.','doctrinal',1],
];

// ── MEAT — 100 items from the four standard works (Latter-day Saint depth) ───
// Shown only to meat-ready people (members / the restoration opened to them).
// [title, ref, description, resonanceStyle, minutes]
const meat = [
  // ── Book of Mormon (45) ──────────────────────────────────────────────────
  ['Men Are That They Might Have Joy','2 Nephi 2:25','Adam fell that men might be, and men are, that they might have joy. The plan of happiness in a single line.','doctrinal',2],
  ['Free to Choose','2 Nephi 2:27','Men are free to choose liberty and eternal life, through the great Mediator, or captivity and death. Agency is the heart of the plan.','doctrinal',2],
  ['Press Forward with Steadfastness','2 Nephi 31:20','Press forward with a steadfastness in Christ, having a perfect brightness of hope, feasting upon the word, and endure to the end.','devotional',2],
  ['Line Upon Line','2 Nephi 28:30','The Lord gives line upon line, precept upon precept — to those who receive, more is given. How revelation actually comes.','doctrinal',2],
  ['By Grace, After All We Can Do','2 Nephi 25:23','It is by grace that we are saved, after all we can do. Grace and effort, held together.','doctrinal',2],
  ['We Talk of Christ','2 Nephi 25:26','We talk of Christ, we rejoice in Christ, we preach of Christ, that our children may know to what source they may look.','devotional',2],
  ['All Are Alike unto God','2 Nephi 26:33','He inviteth them all to come unto him — black and white, bond and free, male and female; all are alike unto God.','doctrinal',2],
  ['I Will Go and Do','1 Nephi 3:7','The Lord giveth no commandments save he shall prepare a way for them to accomplish what he commands. Nephi\u2019s answer.','foundational',2],
  ['Liken the Scriptures','1 Nephi 19:23','Nephi likened all scripture unto his people, that it might be for their profit and learning. How to read scripture as your own.','study',2],
  ['Lehi\u2019s Dream','1 Nephi 8','The tree of life, the iron rod, the mists of darkness, and the great and spacious building. A map of the whole journey to God.','doctrinal',4],
  ['The Condescension of God','1 Nephi 11','Nephi sees the tree his father saw — and learns it is the love of God, shown in the condescension of God: Christ come down to us.','doctrinal',4],
  ['In the Service of Your Fellow Beings','Mosiah 2:17','When ye are in the service of your fellow beings ye are only in the service of your God. King Benjamin\u2019s great teaching.','moral',2],
  ['Putting Off the Natural Man','Mosiah 3:19','The natural man is an enemy to God — until he yields to the Spirit and becomes as a child: submissive, meek, patient, full of love.','doctrinal',2],
  ['Watch Yourselves','Mosiah 4:30','Watch yourselves, your thoughts, your words, and your deeds — and continue in the faith of what you have heard.','moral',1],
  ['Children of Christ','Mosiah 5:7','Because of the covenant, ye shall be called the children of Christ, his sons and his daughters; he hath spiritually begotten you.','doctrinal',2],
  ['Bear One Another\u2019s Burdens','Mosiah 18:8-10','The baptismal covenant at the Waters of Mormon: to bear one another\u2019s burdens, mourn with those that mourn, and stand as a witness.','devotional',2],
  ['He Will Take Upon Him Their Infirmities','Alma 7:11-12','He suffered pains, afflictions, and temptations — and took upon him our infirmities — that he might know how to succor his people.','doctrinal',3],
  ['Faith Is Not a Perfect Knowledge','Alma 32:21','Faith is not to have a perfect knowledge; it is to hope for things which are not seen, which are true. A working definition of faith.','doctrinal',2],
  ['Experiment Upon the Word','Alma 32:27-28','If ye will but awake and arouse your faculties, even to an experiment, and plant the seed — if it is good, it will swell within you.','study',3],
  ['Do Not Procrastinate','Alma 34:32-33','This life is the day for men to prepare to meet God; do not procrastinate the day of your repentance.','doctrinal',2],
  ['By Small and Simple Things','Alma 37:6-7','By small and simple things are great things brought to pass; the Lord confounds the wise by the small means.','devotional',2],
  ['Wickedness Never Was Happiness','Alma 41:10','Do not suppose, because it has been spoken concerning restoration, that ye shall be restored from sin to happiness. Wickedness never was happiness.','moral',1],
  ['His Image in Your Countenance','Alma 5:14','Have ye spiritually been born of God? Have ye received his image in your countenances? The question of conversion.','devotional',2],
  ['Alma\u2019s Conversion','Alma 36','Alma was harrowed up by the memory of his sins — then he remembered Christ, and his pain was swallowed up in joy. A pattern of repentance.','emotional',4],
  ['Built Upon the Rock','Helaman 5:12','Remember it is upon the rock of our Redeemer, who is Christ, that ye must build your foundation — a sure foundation against the storm.','doctrinal',2],
  ['The Risen Lord Appears','3 Nephi 11:10-17','At the temple in Bountiful, the resurrected Christ invites the multitude to come, one by one, and feel the prints in his hands and feet.','emotional',3],
  ['Jesus Blesses the Children','3 Nephi 17','He wept, took their little children one by one and blessed them, and angels came down and encircled them with fire. The tenderest chapter.','emotional',4],
  ['What Manner of Men Ought Ye to Be','3 Nephi 27:27','Ye know the things that ye must do; even as I am. The standard he sets, and the help he gives to reach it.','doctrinal',2],
  ['The Sermon at the Temple','3 Nephi 12-14','The Beatitudes and the Sermon on the Mount, given again by the risen Lord to a people on the other side of the world.','doctrinal',5],
  ['Faith, Hope, and the Trial','Ether 12:6','Ye receive no witness until after the trial of your faith. Faith is things hoped for and not seen; dispute not because ye see not.','doctrinal',2],
  ['Weak Things Become Strong','Ether 12:27','I give unto men weakness that they may be humble; my grace is sufficient, and I make weak things become strong unto them.','devotional',2],
  ['Charity, the Pure Love of Christ','Moroni 7:45-47','Charity suffereth long, is kind, envieth not — it is the pure love of Christ, and whoso is found possessed of it at the last day, it is well.','devotional',3],
  ['Moroni\u2019s Promise','Moroni 10:4-5','Ask God, the Eternal Father, in the name of Christ, if these things are not true; and by the power of the Holy Ghost ye may know the truth of all things.','foundational',2],
  ['Come unto Christ, Be Perfected','Moroni 10:32','Come unto Christ, and be perfected in him; deny yourselves of all ungodliness — then is his grace sufficient for you.','devotional',2],
  ['God Is a God of Miracles','Mormon 9:9','God is the same yesterday, today, and forever; he is a God of miracles, and he changeth not — has the day of miracles ceased?','doctrinal',2],
  ['Seek the Kingdom First','Jacob 2:18-19','Before ye seek for riches, seek ye for the kingdom of God — and after, if you seek riches, it will be to do good and clothe the naked.','moral',2],
  ['The Allegory of the Olive Tree','Jacob 5','The Lord of the vineyard labors again and again to save his trees — the long, patient history of God gathering scattered Israel.','doctrinal',6],
  ['Enos\u2019s Wrestle','Enos 1:2-5','Enos\u2019s soul hungered, and he knelt before his Maker in mighty prayer all day and into the night, until his guilt was swept away.','emotional',2],
  ['One Heart, All Things Common','4 Nephi 1:2-3','The people had all things common among them; there were no rich and poor, and they were in one, the children of Christ. A glimpse of Zion.','doctrinal',2],
  ['As Often as They Repented','Mosiah 26:30','As often as my people repent will I forgive them their trespasses against me. The reach of the Lord\u2019s mercy.','devotional',1],
  ['Be Humble, Full of Faith','Alma 7:23-24','Be humble, submissive, gentle, easy to be entreated, full of patience and long-suffering; and have faith, hope, and charity.','moral',2],
  ['The Liahona','Alma 37:38-46','The compass worked by faith; when they were slothful it stopped. So with the words of Christ — small means the Lord uses to guide us.','devotional',2],
  ['Nourished by the Good Word','Moroni 6:4','After baptism they were numbered and nourished by the good word of God, to keep them in the right way — why a covenant people gather and feed each other.','devotional',2],
  ['The Title of Liberty','Alma 46:12-13','Captain Moroni wrote on his coat: In memory of our God, our religion, freedom, peace, our wives, and our children. Faith worth standing for.','historical',2],
  ['Yielded Their Hearts unto God','Helaman 3:35','They did wax stronger in humility, and firmer in the faith, yielding their hearts unto God — the way real strength comes.','devotional',1],

  // ── Doctrine and Covenants (38) ──────────────────────────────────────────
  ['By Mine Own Voice or My Servants','Doctrine and Covenants 1:38','Whether by mine own voice or by the voice of my servants, it is the same. Why the words of living prophets carry the Lord\u2019s authority.','doctrinal',2],
  ['Doubt Not, Fear Not','Doctrine and Covenants 6:36','Look unto me in every thought; doubt not, fear not. A whole discipleship in seven words.','devotional',1],
  ['Revelation by Heart and Mind','Doctrine and Covenants 8:2-3','I will tell you in your mind and in your heart, by the Holy Ghost — how personal revelation actually feels.','doctrinal',2],
  ['The Worth of Souls','Doctrine and Covenants 18:10','Remember the worth of souls is great in the sight of God. The verse that frames how heaven sees every person.','devotional',2],
  ['Joy in One Soul','Doctrine and Covenants 18:15-16','How great shall be your joy if you bring but one soul unto me — and how great if you bring many.','devotional',2],
  ['I Have Suffered These Things for All','Doctrine and Covenants 19:16-19','Christ describes the Atonement in his own voice: suffering that caused himself to tremble, and to bleed, that we might not suffer if we repent.','doctrinal',3],
  ['Learn of Me','Doctrine and Covenants 19:23','Learn of me, and listen to my words; walk in the meekness of my Spirit, and you shall have peace in me.','devotional',1],
  ['An Elect Lady','Doctrine and Covenants 25','The Lord\u2019s words to Emma Smith: lift up thy heart and rejoice, and cleave unto the covenants. A revelation to and about a woman.','devotional',2],
  ['If Ye Are Not One','Doctrine and Covenants 38:27','Be one; and if ye are not one ye are not mine. The unity God requires of a covenant people.','doctrinal',1],
  ['Remembered No More','Doctrine and Covenants 58:42-43','He who has repented of his sins, the same is forgiven, and I, the Lord, remember them no more. The completeness of forgiveness.','devotional',2],
  ['Forgive All Men','Doctrine and Covenants 64:9-10','I, the Lord, will forgive whom I will, but of you it is required to forgive all men. The hardest and most freeing commandment.','moral',2],
  ['The Three Degrees of Glory','Doctrine and Covenants 76','The vision of the celestial, terrestrial, and telestial kingdoms — heaven is not one room, and God\u2019s mercy reaches nearly all.','doctrinal',5],
  ['The Lord Is Bound','Doctrine and Covenants 82:10','I, the Lord, am bound when ye do what I say; but when ye do not, ye have no promise. How blessings are tied to obedience.','doctrinal',1],
  ['The Oath and Covenant','Doctrine and Covenants 84:33-39','The oath and covenant of the priesthood — those who magnify their calling are sanctified, and receive all the Father hath.','doctrinal',3],
  ['Seek Learning by Study and Faith','Doctrine and Covenants 88:118','Seek ye out of the best books words of wisdom; seek learning, even by study and also by faith. The Lord\u2019s charter for education.','study',2],
  ['The Word of Wisdom','Doctrine and Covenants 89','A principle with promise, given for the temporal salvation of the Saints — and a hidden treasure of health and knowledge for those who keep it.','doctrinal',3],
  ['The Glory of God Is Intelligence','Doctrine and Covenants 93:36','The glory of God is intelligence, or, in other words, light and truth — and that light forsakes the evil one.','doctrinal',1],
  ['Truth Is Things as They Are','Doctrine and Covenants 93:24','Truth is knowledge of things as they are, and as they were, and as they are to come. The Lord\u2019s own definition of truth.','philosophical',1],
  ['A Small Moment','Doctrine and Covenants 121:7-8','My son, peace be unto thy soul; thine adversity and afflictions shall be but a small moment. Words to Joseph in Liberty Jail.','devotional',2],
  ['No Power but by Persuasion','Doctrine and Covenants 121:41-46','No power or influence ought to be maintained but by persuasion, long-suffering, gentleness, meekness, and love unfeigned. How God leads.','doctrinal',3],
  ['All These Things Give Experience','Doctrine and Covenants 122:7','If thou art called to pass through tribulation — know thou, my son, that all these things shall give thee experience, and be for thy good.','devotional',2],
  ['Intelligence Rises with Us','Doctrine and Covenants 130:18-19','Whatever principle of intelligence we attain in this life, it rises with us in the resurrection. What we become outlasts us.','doctrinal',1],
  ['Blessings and Law','Doctrine and Covenants 130:20-21','There is a law, irrevocably decreed, upon which all blessings are predicated; and we obtain blessings by obedience to that law.','doctrinal',1],
  ['The Father Has a Body','Doctrine and Covenants 130:22','The Father has a body of flesh and bones as tangible as man\u2019s; the Son also; the Holy Ghost is a personage of Spirit.','doctrinal',1],
  ['The Eternal Covenant of Marriage','Doctrine and Covenants 131:1-4','In the celestial glory there are degrees; to obtain the highest, one must enter the new and everlasting covenant of marriage.','doctrinal',2],
  ['The Vision of the Celestial Kingdom','Doctrine and Covenants 137','Joseph sees his brother Alvin in the celestial kingdom and learns that all who would have received the gospel are heirs of it.','doctrinal',3],
  ['The Redemption of the Dead','Doctrine and Covenants 138','President Joseph F. Smith\u2019s vision of the spirit world: the Savior organized the faithful to carry the gospel to the dead.','doctrinal',4],
  ['Eternal Life, the Greatest Gift','Doctrine and Covenants 14:7','If you keep my commandments and endure to the end you shall have eternal life, which gift is the greatest of all the gifts of God.','doctrinal',1],
  ['Light Groweth Brighter','Doctrine and Covenants 50:24','That which is of God is light; and he that receiveth light, and continueth in God, receiveth more light, brighter and brighter.','doctrinal',1],
  ['Anxiously Engaged','Doctrine and Covenants 58:27','Men should be anxiously engaged in a good cause, and do many things of their own free will — God does not command in all things.','moral',1],
  ['Draw Near unto Me','Doctrine and Covenants 88:63','Draw near unto me and I will draw near unto you; seek me diligently and ye shall find me; ask, and ye shall receive.','devotional',1],
  ['All Things for Your Good','Doctrine and Covenants 98:1-3','Give thanks in all things, wait patiently on the Lord — your prayers have entered into his ears, and all things work together for your good.','devotional',2],
  ['It Shall Be Given You','Doctrine and Covenants 100:5-8','Lift up your voice; it shall be given you in the very hour what ye shall say, and the Holy Ghost shall bear record of the truth.','devotional',2],
  ['Embark in the Service of God','Doctrine and Covenants 4','If ye have desires to serve God ye are called to the work — faith, hope, charity, and love, with an eye single to his glory, qualify you.','devotional',1],
  ['Obtain My Word First','Doctrine and Covenants 11:21','Seek not to declare my word, but first seek to obtain my word — then shall your tongue be loosed and you shall have my Spirit.','study',1],
  ['Treasure Up the Word','Doctrine and Covenants 84:85','Treasure up in your minds continually the words of life, and it shall be given you in the very hour that portion that shall be meted.','study',1],
  ['The Constitution and the Free','Doctrine and Covenants 101:77-80','The Lord declares he established the Constitution by wise men he raised up, that every man might act in moral agency. Liberty as a gospel value.','historical',2],
  ['Whatsoever God Sends','Doctrine and Covenants 121:33','How long can rolling waters remain impure? Truth and revelation cannot be stopped by men — no power can stay the heavens from pouring knowledge.','doctrinal',2],

  // ── Pearl of Great Price (17) ────────────────────────────────────────────
  ['My Work and My Glory','Moses 1:39','This is my work and my glory — to bring to pass the immortality and eternal life of man. God\u2019s own purpose, in his own words.','doctrinal',1],
  ['Worlds Without Number','Moses 1:33','Worlds without number have I created; and by the Son I created them — and all things are present before mine eyes.','doctrinal',2],
  ['Zion, One Heart','Moses 7:18','The Lord called his people Zion, because they were of one heart and one mind, and dwelt in righteousness, with no poor among them.','doctrinal',2],
  ['The God That Weeps','Moses 7:28-31','Enoch beholds the God of heaven weep over his children — proof that God is not distant or unfeeling, but moved by our suffering.','emotional',3],
  ['All Men Must Repent','Moses 6:57','Teach your children that all men must repent and be born again of water and the Spirit, for no unclean thing can dwell in God\u2019s presence.','doctrinal',2],
  ['Noble and Great Ones','Abraham 3:22-23','Abraham sees the intelligences organized before the world was — the noble and great ones, chosen before they were born.','doctrinal',2],
  ['We Will Prove Them','Abraham 3:24-25','We will make an earth whereon these may dwell; and we will prove them, to see if they will do all things the Lord commands.','doctrinal',2],
  ['Those Who Keep Their First Estate','Abraham 3:26','They who keep their first estate shall be added upon; and they who keep their second estate shall have glory added forever.','doctrinal',1],
  ['The Lord Is More Intelligent','Abraham 3:19','The Lord is more intelligent than they all — and his purpose stands above all the noble and great spirits he organized.','doctrinal',1],
  ['The First Vision','Joseph Smith\u2014History 1:16-17','Joseph sees two Personages, whose brightness and glory defy description; one points to the other: This is My Beloved Son. Hear Him.','foundational',3],
  ['The Verse That Sent Him to Pray','Joseph Smith\u2014History 1:11-13','Reading James 1:5, Joseph felt no passage ever came with more power to the heart — and resolved to ask of God.','foundational',2],
  ['We Believe in God','Articles of Faith 1:1','We believe in God, the Eternal Father, and in his Son, Jesus Christ, and in the Holy Ghost. Three distinct members of the Godhead.','doctrinal',1],
  ['Saved by Obedience','Articles of Faith 1:3','We believe that through the Atonement of Christ, all mankind may be saved, by obedience to the laws and ordinances of the gospel.','doctrinal',1],
  ['First Principles and Ordinances','Articles of Faith 1:4','Faith in the Lord Jesus Christ, repentance, baptism by immersion, and the laying on of hands for the gift of the Holy Ghost.','doctrinal',1],
  ['The Bible and the Book of Mormon','Articles of Faith 1:8','We believe the Bible to be the word of God as far as it is translated correctly; we also believe the Book of Mormon to be the word of God.','doctrinal',1],
  ['He Will Yet Reveal','Articles of Faith 1:9','We believe all that God has revealed, all that he does now reveal, and that he will yet reveal many great and important things.','doctrinal',1],
  ['Virtuous, Lovely, of Good Report','Articles of Faith 1:13','If there is anything virtuous, lovely, or of good report or praiseworthy, we seek after these things. A pattern for a whole life.','moral',1],
];

// ── assemble ──────────────────────────────────────────────────────────────
const items = [];
let id = 1;
for (const [title, ref, description, resonanceStyle, estimatedMinutes] of milkCommon) {
  items.push({ id: id++, tag:'MILK', track:'MILK', milkTrack:'common', title, description, scriptureRef:ref, url:bg(ref), mediaType:'article', estimatedMinutes, resonanceStyle });
}
for (const [title, ref, description, ldsLens, resonanceStyle, estimatedMinutes] of milkRestoration) {
  items.push({ id: id++, tag:'MILK', track:'MILK', milkTrack:'restoration', title, description, scriptureRef:ref, url:bg(ref), mediaType:'article', estimatedMinutes, resonanceStyle, ldsLens });
}
for (const [title, ref, description, resonanceStyle, estimatedMinutes] of meat) {
  items.push({ id: id++, tag:'MAINTENANCE', track:'MEAT', title, description, scriptureRef:ref, url:lds(ref), mediaType:'article', estimatedMinutes, resonanceStyle });
}

// ── asserts ───────────────────────────────────────────────────────────────
const common = items.filter(i => i.milkTrack === 'common');
const restoration = items.filter(i => i.milkTrack === 'restoration');
const milkItems = items.filter(i => i.track === 'MILK');
const meatItems = items.filter(i => i.track === 'MEAT');
const assert = (c, m) => { if (!c) throw new Error('ASSERT FAILED: ' + m); };
assert(common.length === 50, 'common milk must be 50, got ' + common.length);
assert(restoration.length === 50, 'restoration milk must be 50, got ' + restoration.length);
assert(milkItems.length === 100, 'milk total must be 100, got ' + milkItems.length);
assert(meatItems.length === 100, 'meat total must be 100, got ' + meatItems.length);
assert(items.length === 200, 'grand total must be 200, got ' + items.length);
assert(new Set(items.map(i=>i.id)).size === items.length, 'ids must be unique');
assert(new Set(items.map(i=>i.title)).size === items.length, 'titles must be unique (dupe present)');
for (const i of items) {
  if (i.track === 'MILK') {
    assert(/^https:\/\/www\.biblegateway\.com\/passage\/\?search=.+&version=KJV$/.test(i.url), 'bad bible url: ' + i.url);
    assert(i.milkTrack !== 'restoration' || (i.ldsLens && i.ldsLens.length > 10), 'restoration item missing ldsLens: ' + i.title);
  } else {
    assert(/^https:\/\/www\.churchofjesuschrist\.org\/study\/scriptures\/.+\/\d+$/.test(i.url), 'bad LDS url: ' + i.title + ' -> ' + i.url);
  }
}

// ── emit content.ts ────────────────────────────────────────────────────────
const esc = (s) => JSON.stringify(s);
const L = [];
L.push("export type FeedTag = 'MILK' | 'BRIDGE' | 'RESTORATION' | 'MAINTENANCE';");
L.push("export type MediaType = 'article' | 'video' | 'podcast';");
L.push("export type ResonanceStyle =");
L.push("  | 'emotional' | 'logical' | 'moral' | 'comfort' | 'historical'");
L.push("  | 'doctrinal' | 'foundational' | 'personal' | 'philosophical'");
L.push("  | 'devotional' | 'study';");
L.push('');
L.push('// The milk/meat standard (Cameron, June 2026):');
L.push('//   MILK = Bible-only; 50 verses both traditions love (milkTrack "common")');
L.push('//   + 50 often-skipped passages that raise restored-gospel questions');
L.push('//   (milkTrack "restoration"). MEAT = Latter-day Saint content from the four');
L.push('//   standard works, shown once a person is meat-ready. Meat-ready people see');
L.push('//   milk AND meat together. ldsLens = a short hint the chat uses to outline the');
L.push('//   Latter-day Saint perspective subtly; never shown raw to the user.');
L.push("export type ContentTrack = 'MILK' | 'MEAT';");
L.push("export type MilkTrack    = 'common' | 'restoration';");
L.push('');
L.push('export interface ContentItem {');
L.push('  id:               number;');
L.push('  tag:              FeedTag;');
L.push('  track:            ContentTrack;');
L.push('  milkTrack?:       MilkTrack;');
L.push('  title:            string;');
L.push('  description:      string;');
L.push('  scriptureRef:     string;');
L.push('  url:              string;');
L.push('  mediaType:        MediaType;');
L.push('  estimatedMinutes: number;');
L.push('  resonanceStyle:   ResonanceStyle;');
L.push('  ldsLens?:         string;');
L.push('}');
L.push('');
L.push('export const CONTENT: ContentItem[] = [');
for (const i of items) {
  const parts = [
    `id: ${i.id}`,
    `tag: ${esc(i.tag)}`,
    `track: ${esc(i.track)}`,
    i.milkTrack ? `milkTrack: ${esc(i.milkTrack)}` : null,
    `title: ${esc(i.title)}`,
    `description: ${esc(i.description)}`,
    `scriptureRef: ${esc(i.scriptureRef)}`,
    `url: ${esc(i.url)}`,
    `mediaType: ${esc(i.mediaType)}`,
    `estimatedMinutes: ${i.estimatedMinutes}`,
    `resonanceStyle: ${esc(i.resonanceStyle)}`,
    i.ldsLens ? `ldsLens: ${esc(i.ldsLens)}` : null,
  ].filter(Boolean);
  L.push('  {');
  for (const p of parts) L.push('    ' + p + ',');
  L.push('  },');
}
L.push('];');
L.push('');
L.push('export function getContentByTag(tag: FeedTag): ContentItem[] {');
L.push('  return CONTENT.filter(item => item.tag === tag);');
L.push('}');
L.push('');
L.push('export function getContentById(id: number): ContentItem | undefined {');
L.push('  return CONTENT.find(item => item.id === id);');
L.push('}');
L.push('');

const out = path.join(__dirname, 'mobile', 'src', 'data', 'content.ts');
fs.writeFileSync(out, L.join('\n'), 'utf8');

// Sidecar JSON for the feed/link test (tools/feed_test.js) so the test reads the
// exact same data the app ships.
const toolsDir = path.join(__dirname, 'tools');
fs.mkdirSync(toolsDir, { recursive: true });
fs.writeFileSync(path.join(toolsDir, 'content.data.json'), JSON.stringify(items, null, 2), 'utf8');

console.log(`Wrote ${items.length} items (${common.length} common + ${restoration.length} restoration) to ${out}`);
console.log(`Wrote tools/content.data.json (${items.length} items)`);
