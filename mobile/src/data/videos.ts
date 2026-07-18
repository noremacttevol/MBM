/**
 * videos.ts — the 200 animated Jesus-story videos that are the spine of Feed 2.0.
 *
 * WHAT THIS IS (and is not):
 *   Each VideoStory is one reverent, animated story clip (painterly storybook /
 *   sacred-art style, 90s–3min, Two-Voice Law: KJV red-letter Jesus voice + a
 *   modern LDS-lens narrator). Every clip is paired with the KJV verse it retells
 *   (`scriptureRef`), shown beneath it and HONORED SEPARATELY (see the page
 *   engine in useAppStore). Every clip carries its Seed question — the quiet
 *   question about God's character it leaves behind. The 200 stay MILK: their one
 *   job is showing Jesus is good.
 *
 * PRODUCTION STATE (2026-07-11): the videos do not exist yet — wave-one
 *   production is blocked on Cameron's generator sign-in (FEED-2.0-SPEC build
 *   order step 4). So every entry ships with `videoUrl: null` for now. The page
 *   engine treats a null videoUrl (or being offline) as "show the verse/text
 *   only" — the feed is fully usable before a single .mp4 exists. As clips are
 *   produced they land in Firebase Hosting at site/story-videos/<id>.mp4 and get
 *   their id added to PRODUCED_VIDEO_IDS below; nothing else has to change.
 *
 * SEEDED SET: entries 1–20 are the in-app story bank (THE-200 packs 01–20, the
 *   only packs written so far) with real KJV refs and Seed questions. Entries
 *   21–200 are written into this list as their packs are produced — the engine
 *   simply cycles whatever exists, exactly like buildFeed cycles the verse pool.
 *   No fabricated stories: only real ones are listed.
 */

// Firebase Hosting project is `milk-b4-meat`; hosting serves the `site/` dir, so
// produced clips live at site/story-videos/<id>.mp4 → this public URL.
const VIDEO_HOST = 'https://milk-b4-meat.web.app/story-videos';

export interface VideoStory {
  /** Matches the THE-200 master catalog number. */
  id:            number;
  title:         string;
  /** Feed-card headline, Cameron's pattern: "A story about ___" (Rev 1 §7). */
  aboutTitle:    string;
  /** The KJV verse paired beneath the video (honored separately from the video). */
  scriptureRef:  string;
  /** The quiet question about God's character the clip leaves behind (MILK). */
  seedQuestion:  string;
  /**
   * Rev 2.2 (Cameron): the one-line, checkbox-confirmable intention of this
   * scripture — what the God-inspired word is for. Tapping it is a traceable
   * "I got something from this" and earns the Get-new/replacement.
   */
  takeaway:      string;
  /**
   * A CONTENT item whose scriptureRef matches, when one exists. Lets the paired
   * verse reuse the bundled inline KJV (kjvText.ts) and the existing ContentCard
   * instead of only linking out. Undefined → the verse links out (Bible Gateway).
   */
  contentId?:    number;
  /** Firebase Hosting stream URL once produced; null until the clip exists. */
  videoUrl:      string | null;
  /** Poster/still shown before playback; null until art exists. */
  poster?:       string | null;
  /** Thumbnail (a frame cut from the video) shown on the feed card; derived. */
  thumbUrl?:     string | null;
}

/**
 * Build the Bible Gateway KJV link for a verse ref — the honor action for a
 * paired verse that isn't in the bundled inline KJV.
 */
export function verseGatewayUrl(ref: string): string {
  return `https://www.biblegateway.com/passage/?search=${encodeURIComponent(ref)}&version=KJV`;
}

/**
 * The stream URL a produced clip WOULD have. Kept separate from `videoUrl` so the
 * data can carry the intended location while `videoUrl` stays null until the file
 * is actually live (isVideoProduced gates playback).
 */
export function videoStreamUrl(id: number): string {
  return `${VIDEO_HOST}/${id}.mp4`;
}

export function videoThumbUrl(id: number): string {
  return `${VIDEO_HOST}/thumbs/${id}.jpg`;
}

// Ids of clips that are actually produced and live on Firebase Hosting. Adding an
// id here is the ONLY switch needed to go live — videoUrl is derived automatically
// below. The locked player only ever plays a produced id.
//
// Wave four (2026-07-18): a FULL RESET to exactly the clips Cameron approved on the
// review page after the approval reset. Source of truth is
// media-production/approvals.json (version-locked to the exact cut, synced from
// Firestore by admin/sync-reviews.mjs). Everything he has not re-approved is OUT —
// those cards fall back to verse-only. #89 is approved but was never assembled
// (build-89-last-supper has no final), so it is held out until it exists.
// Cameron-approved cuts, published as PLACEHOLDERS (2026-07-18). Jesus has a new
// voice, so nearly every story is being completely redone; these approved cuts hold
// the feed until the new-voice versions land and he re-approves them.
export const PRODUCED_VIDEO_IDS = new Set<number>([
  2, 3, 4, 5, 6, 11, 15, 19, 21,
  80, 87, 88, 89, 91, 92, 93, 94, 95, 96,
  100, 101, 102, 103, 104, 105, 106, 107, 108, 111,
  180, 181, 182, 183,
  185, 186, 187, 188, 189,
  190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200,
]);

export function isVideoProduced(id: number): boolean {
  return PRODUCED_VIDEO_IDS.has(id);
}

export const VIDEO_STORIES: VideoStory[] = [
  { id: 1,  title: 'The Woman Who Touched His Cloak',
    aboutTitle: 'A story about a woman who reached for his cloak', scriptureRef: 'Mark 5:25-34',    contentId: 17, videoUrl: null,
    seedQuestion: 'If he stopped for one woman in a whole crowd, would he stop for you?',
    takeaway: "This helped me see that he can heal us without even trying." },
  { id: 2,  title: 'The Prodigal Son',
    aboutTitle: 'A story about a father who ran',                scriptureRef: 'Luke 15:11-32',   contentId: 5,  videoUrl: null,
    seedQuestion: "What if God runs toward the one coming home, instead of waiting with his arms folded?",
    takeaway: "This helped me see that God runs to meet us before we finish saying sorry." },
  { id: 3,  title: 'Zacchaeus',
    aboutTitle: 'A story about the most hated man in town',                       scriptureRef: 'Luke 19:1-10',    contentId: 18, videoUrl: null,
    seedQuestion: 'What if grace comes to your table before you have cleaned anything up?',
    takeaway: "This helped me see that God wants to be with us before we've cleaned anything up." },
  { id: 4,  title: 'Nicodemus at Night',
    aboutTitle: 'A story about questions asked in the dark',              scriptureRef: 'John 3:1-17',                    videoUrl: null,
    seedQuestion: 'Is it safe to bring God your hardest questions in the dark?',
    takeaway: "This helped me see that my hardest questions are welcome with God." },
  { id: 5,  title: 'The Bent-Over Woman',
    aboutTitle: 'A story about a woman who belonged before she was healed',             scriptureRef: 'Luke 13:10-17',                  videoUrl: null,
    seedQuestion: 'What if you belonged to him before anything about you was fixed?',
    takeaway: "This helped me see that I belonged to him before anything about me was fixed." },
  { id: 6,  title: 'The Two Sons',
    aboutTitle: 'A story about two sons and one honest turning',                    scriptureRef: 'Matthew 21:28-32',               videoUrl: null,
    seedQuestion: 'Does God measure the turning, or the performance?',
    takeaway: "This helped me see that God cares more about my turning than my talk." },
  { id: 7,  title: 'Peter Walks on Water',
    aboutTitle: 'A story about sinking and the hand already there',            scriptureRef: 'Matthew 14:22-33', contentId: 20, videoUrl: null,
    seedQuestion: 'When you start to sink, is the hand already reaching for you?',
    takeaway: "This helped me see that he catches me the moment I start to sink." },
  { id: 8,  title: 'The Lost Coin',
    aboutTitle: 'A story about a search that would not stop',                   scriptureRef: 'Luke 15:8-10',                   videoUrl: null,
    seedQuestion: 'Would God light a lamp and sweep the whole house for one lost coin — for you?',
    takeaway: "This helped me see how God loves all of us." },
  { id: 9,  title: 'The Rich Young Ruler',
    aboutTitle: 'A story about a man who walked away free',            scriptureRef: 'Mark 10:17-27',                  videoUrl: null,
    seedQuestion: 'What if the God you fear would let you walk away, and still love you?',
    takeaway: "This helped me see that God lets me choose — and loves me either way." },
  { id: 10, title: 'The Woman at the Well',
    aboutTitle: 'A story about being fully known at a well',           scriptureRef: 'John 4:1-26',      contentId: 19, videoUrl: null,
    seedQuestion: 'Could someone know everything you have ever done and stay anyway?',
    takeaway: "This helped me see that being fully known doesn't scare him away." },
  { id: 11, title: 'Calming the Storm',
    aboutTitle: 'A story about a storm told to be still',               scriptureRef: 'Mark 4:35-41',                   videoUrl: null,
    seedQuestion: 'What if God did not send your storm — but can still say peace to it?',
    takeaway: "This helped me see that he speaks peace into the things that scare me." },
  { id: 12, title: 'Blind Bartimaeus',
    aboutTitle: 'A story about a blind man the crowd told to hush',               scriptureRef: 'Mark 10:46-52',                  videoUrl: null,
    seedQuestion: 'When everyone tells you to hush, does God stop for your voice?',
    takeaway: "This helped me see that he stops for the voice everyone else shushes." },
  { id: 13, title: 'Through the Roof',
    aboutTitle: 'A story about friends who went through the roof',                scriptureRef: 'Mark 2:1-12',                    videoUrl: null,
    seedQuestion: 'Whose faith has carried you closer than you could have crawled on your own?',
    takeaway: "This helped me see that my people's faith can carry me to him." },
  { id: 14, title: 'The Ten Lepers',
    aboutTitle: 'A story about ten healed and one who came back',                  scriptureRef: 'Luke 17:11-19',                  videoUrl: null,
    seedQuestion: 'What if healing meets you on the way, before you have any proof?',
    takeaway: "This helped me see that healing can begin while I'm still walking." },
  { id: 15, title: 'The Centurion',
    aboutTitle: 'A story about faith found outside the fold',                   scriptureRef: 'Matthew 8:5-13',                 videoUrl: null,
    seedQuestion: "What if the greatest faith shows up outside the 'right' crowd?",
    takeaway: "This helped me see that he honors faith wherever it comes from." },
  { id: 16, title: 'Mary and Martha',
    aboutTitle: 'A story about the worry underneath the work',          scriptureRef: 'Luke 10:38-42',                  videoUrl: null,
    seedQuestion: 'What if God is more concerned about your worry than your to-do list?',
    takeaway: "This helped me see that he cares about my worry more than my work." },
  { id: 17, title: 'Jesus Wept',
    aboutTitle: 'A story about the day God cried',                      scriptureRef: 'John 11:1-44',     contentId: 9,  videoUrl: null,
    seedQuestion: 'Could the God you picture stand at a grave and weep?',
    takeaway: "This helped me see that God cries with us before he changes things." },
  { id: 18, title: 'The Road to Emmaus',
    aboutTitle: 'A story about a stranger on the road home',            scriptureRef: 'Luke 24:13-35',                  videoUrl: null,
    seedQuestion: 'What if he still walks the road and opens the scriptures — even now?',
    takeaway: "This helped me see that he still walks beside us, even unrecognized." },
  { id: 19, title: 'Breakfast on the Shore',
    aboutTitle: 'A story about breakfast with the one who failed him',  scriptureRef: 'John 21:1-17',                   videoUrl: null,
    seedQuestion: 'What if God hands his work back to the very ones who failed him?',
    takeaway: "This helped me see that failing him doesn't end my place with him." },
  { id: 20, title: 'The Good Samaritan',
    aboutTitle: 'A story about the outsider who stopped',               scriptureRef: 'Luke 10:25-37',    contentId: 10, videoUrl: null,
    seedQuestion: "What if the one who showed God's love was the outsider you would have overlooked?",
    takeaway: "This helped me see that God's love shows up through unexpected people." },
  { id: 21, title: 'The Lost Sheep',
    aboutTitle: 'A story about the one worth leaving ninety-nine for',  scriptureRef: 'Luke 15:1-7',     videoUrl: null,
    seedQuestion: 'Would God really leave the ninety-nine to come looking for just you?',
    takeaway: "This helped me see that he notices when I'm missing, and comes looking." },
  { id: 22, title: 'The Unmerciful Servant',
    aboutTitle: 'A story about a debt too big to repay',                scriptureRef: 'Matthew 18:21-35', videoUrl: null,
    seedQuestion: "If God forgave you a debt you could never pay, what does he hope you'll do with the small ones?",
    takeaway: "This helped me see how much I've already been forgiven." },
  { id: 23, title: 'The Workers in the Vineyard',
    aboutTitle: 'A story about latecomers paid in full',                scriptureRef: 'Matthew 20:1-16',  videoUrl: null,
    seedQuestion: "What if showing up at the last hour still earns the full day's welcome?",
    takeaway: "This helped me see that it's never too late in the day to be wanted." },
  { id: 24, title: 'The Sower',
    aboutTitle: 'A story about seed thrown everywhere',                 scriptureRef: 'Matthew 13:1-9',   videoUrl: null,
    seedQuestion: 'What if God scatters good seed even on ground that might not take it — including yours?',
    takeaway: "This helped me see that God plants generously, even in me." },
  { id: 25, title: 'The Wheat and the Tares',
    aboutTitle: 'A story about weeds left until harvest',               scriptureRef: 'Matthew 13:24-30', videoUrl: null,
    seedQuestion: 'What if God waits to pull the weeds because he refuses to risk the wheat?',
    takeaway: "This helped me see that his patience is protection, not neglect." },
  { id: 26, title: 'The Mustard Seed',
    aboutTitle: 'A story about the smallest seed in the garden',        scriptureRef: 'Matthew 13:31-32', videoUrl: null,
    seedQuestion: 'Could the smallest faith you have still grow into something birds nest in?',
    takeaway: "This helped me see that small beginnings are enough for God." },
  { id: 27, title: 'The Leaven',
    aboutTitle: 'A story about yeast hidden in the dough',              scriptureRef: 'Matthew 13:33',    videoUrl: null,
    seedQuestion: 'What if God works quietly, hidden inside ordinary things, until everything rises?',
    takeaway: "This helped me see that quiet, unseen work still changes everything." },
  { id: 28, title: 'The Hidden Treasure',
    aboutTitle: 'A story about treasure buried in a field',             scriptureRef: 'Matthew 13:44',    videoUrl: null,
    seedQuestion: 'What would you sell everything for — and what if heaven feels that way about you?',
    takeaway: "This helped me see that the kingdom is worth more than everything I'm holding." },
  { id: 29, title: 'The Pearl of Great Price',
    aboutTitle: 'A story about one pearl worth everything',             scriptureRef: 'Matthew 13:45-46', videoUrl: null,
    seedQuestion: 'What if the merchant who gave all he had for one pearl is a picture of how God values you?',
    takeaway: "This helped me see what it looks like to find the one thing worth everything." },
  { id: 30, title: 'The Net',
    aboutTitle: 'A story about a net that gathers every kind',          scriptureRef: 'Matthew 13:47-50', videoUrl: null,
    seedQuestion: 'What if the net gathers every kind first, and the sorting is not your job?',
    takeaway: "This helped me see that gathering comes first and judging isn't mine to do." },
  { id: 31, title: 'The Ten Virgins',
    aboutTitle: 'A story about lamps and long waiting',                 scriptureRef: 'Matthew 25:1-13',  videoUrl: null,
    seedQuestion: 'What if being ready is less about perfection and more about keeping your own lamp filled?',
    takeaway: "This helped me see that no one else can carry my oil for me." },
  { id: 32, title: 'The Talents',
    aboutTitle: 'A story about what was placed in your hands',          scriptureRef: 'Matthew 25:14-30', videoUrl: null,
    seedQuestion: 'What if God is less afraid of your failure than you are of trying?',
    takeaway: "This helped me see that he'd rather I try with what I have than bury it in fear." },
  { id: 33, title: 'The Sheep and the Goats',
    aboutTitle: 'A story about the King hidden in the hungry',          scriptureRef: 'Matthew 25:31-46', videoUrl: null,
    seedQuestion: 'What if every small kindness you gave was received by the King himself?',
    takeaway: "This helped me see that he counts kindness to the least as kindness to him." },
  { id: 34, title: 'The Rich Fool',
    aboutTitle: 'A story about bigger barns and one night',             scriptureRef: 'Luke 12:16-21',    videoUrl: null,
    seedQuestion: 'If tonight were the night, what would your barns be worth?',
    takeaway: "This helped me see that a full barn and an empty soul is a poor trade." },
  { id: 35, title: 'The Great Banquet',
    aboutTitle: 'A story about a feast and empty chairs',               scriptureRef: 'Luke 14:15-24',    videoUrl: null,
    seedQuestion: 'What if the invitation goes out to the streets and hedges — to anyone willing to come?',
    takeaway: "This helped me see that there's a seat with my name on it if I'll come." },
  { id: 36, title: 'The Shrewd Steward',
    aboutTitle: 'A story about using money before it uses you',         scriptureRef: 'Luke 16:1-13',     videoUrl: null,
    seedQuestion: 'What if money is a tool to bless people, not the thing you serve?',
    takeaway: "This helped me see that I can serve God with money, but I can't serve both." },
  { id: 37, title: 'The Rich Man and Lazarus',
    aboutTitle: 'A story about the beggar at the gate',                 scriptureRef: 'Luke 16:19-31',    videoUrl: null,
    seedQuestion: 'Who is lying at your gate that heaven already knows by name?',
    takeaway: "This helped me see that God knows the name of the one everyone steps over." },
  { id: 38, title: 'The Persistent Widow',
    aboutTitle: 'A story about a widow who would not stop knocking',      scriptureRef: 'Luke 18:1-8',      videoUrl: null,
    seedQuestion: 'If even an unjust judge gives in to persistence, how much sooner does a good God hear you?',
    takeaway: "This helped me see that God wants me to keep asking and not lose heart." },
  { id: 39, title: 'The Pharisee and the Publican',
    aboutTitle: 'A story about two prayers in one temple',              scriptureRef: 'Luke 18:9-14',     videoUrl: null,
    seedQuestion: 'Which prayer does God lean closer to hear — the polished one, or the honest one?',
    takeaway: "This helped me see that God is drawn to honesty, not performance." },
  { id: 40, title: 'The Friend at Midnight',
    aboutTitle: 'A story about knocking at midnight',                   scriptureRef: 'Luke 11:1-13',     videoUrl: null,
    seedQuestion: 'What if God wants you to keep knocking — and is a better father than the sleepy neighbor?',
    takeaway: "This helped me see that asking, seeking, and knocking are welcome at any hour." },
  { id: 41, title: 'Counting the Cost',
    aboutTitle: 'A story about towers and honest math',                 scriptureRef: 'Luke 14:25-35',    videoUrl: null,
    seedQuestion: 'What if God would rather have your honest count than a rushed yes?',
    takeaway: "This helped me see that he takes me seriously enough to ask for my whole heart." },
  { id: 42, title: 'The Barren Fig Tree',
    aboutTitle: 'A story about one more year',                          scriptureRef: 'Luke 13:6-9',      videoUrl: null,
    seedQuestion: 'What if the gardener is still saying "give it one more year" over you?',
    takeaway: "This helped me see that he asks for more time for me, and works the soil himself." },
  { id: 43, title: 'The Wedding Garment',
    aboutTitle: 'A story about a feast and what to wear',               scriptureRef: 'Matthew 22:1-14',  videoUrl: null,
    seedQuestion: 'What if the king provides the garment — and all you have to do is put it on?',
    takeaway: "This helped me see that coming to the feast means wearing what he offers." },
  { id: 44, title: 'The Two Debtors',
    aboutTitle: 'A story about two debts and one dinner',               scriptureRef: 'Luke 7:36-50',     videoUrl: null,
    seedQuestion: 'What if the one forgiven most loves most — and that could be you?',
    takeaway: "This helped me see that knowing how much I've been forgiven teaches me how to love." },
  { id: 45, title: 'The Wicked Tenants',
    aboutTitle: 'A story about the son they should have honored',       scriptureRef: 'Mark 12:1-11',     videoUrl: null,
    seedQuestion: 'What kind of owner keeps sending messengers — and then sends his own son?',
    takeaway: "This helped me see how far God will go before he gives up on a vineyard." },
  { id: 47, title: 'Houses on Rock and Sand',
    aboutTitle: 'A story about two houses in one storm',                scriptureRef: 'Matthew 7:24-27',  videoUrl: null,
    seedQuestion: 'When the same storm hits both houses, what decides which one stands?',
    takeaway: "This helped me see that the storm comes to everyone — the foundation is the choice." },

  // ── Wave four: the packs Cameron approved on the review page (2026-07-18).
  // Refs taken from media-production/DRAFTS/row-NNN.md — no invented scripture.
  { id: 80, title: 'Come Unto Me',
    aboutTitle: 'A story about an offer of rest to worn-out people', scriptureRef: 'Matthew 11:28-30', videoUrl: null,
    seedQuestion: 'What if he never meant for you to carry it by yourself?',
    takeaway: "This helped me see that he gets under the load with me instead of adding to it." },
  { id: 100, title: 'The Ascension',
    aboutTitle: 'A story about the day he was lifted into the sky', scriptureRef: 'Acts 1:6-11', videoUrl: null,
    seedQuestion: 'If he left you a mission instead of an answer, what does that say about how much he trusts you?',
    takeaway: "This helped me see that he didn't leave us alone — he left us a promise." },
  { id: 101, title: 'The Still Small Voice',
    aboutTitle: 'A story about a burned-out man alone on a mountain', scriptureRef: '1 Kings 19:9-18', videoUrl: null,
    seedQuestion: 'What if God comes to you quietly, instead of in the loudest thing in the room?',
    takeaway: 'This helped me see that God speaks softly to people who are worn all the way out.' },
  { id: 102, title: "Jacob's Ladder",
    aboutTitle: 'A story about a man asleep on a stone who saw heaven open', scriptureRef: 'Genesis 28:10-17', videoUrl: null,
    seedQuestion: 'What if God was already in the place you thought you were alone in?',
    takeaway: "This helped me see that God meets me while I'm still running." },
  { id: 103, title: "Peter's Confession",
    aboutTitle: 'A story about a fisherman who answered the hardest question', scriptureRef: 'Matthew 16:13-20', videoUrl: null,
    seedQuestion: 'What if the Father tells you who Jesus is himself, instead of leaving you to figure it out?',
    takeaway: 'This helped me see that God gives people the answer himself.' },
  { id: 104, title: 'The Boy Samuel',
    aboutTitle: 'A story about a boy who kept mistaking the voice', scriptureRef: '1 Samuel 3:1-21', videoUrl: null,
    seedQuestion: 'Would God keep calling your name while you were still learning to recognize it?',
    takeaway: "This helped me see that he keeps calling even when I don't know it's him yet." },
  { id: 105, title: 'Face to Face, as a Friend',
    aboutTitle: 'A story about a man who talked with God like a friend', scriptureRef: 'Exodus 33:7-11', videoUrl: null,
    seedQuestion: 'What if God wants to talk with you like a friend, not just be worshipped from a distance?',
    takeaway: 'This helped me see that God speaks to people as a friend.' },
  { id: 106, title: 'God Spake By The Prophets',
    aboutTitle: 'A story about a God who never went quiet', scriptureRef: 'Hebrews 1:1-3', videoUrl: null,
    seedQuestion: 'If he spoke to every generation before yours, why would he go quiet now?',
    takeaway: "This helped me see that God has never stopped speaking to his children." },
  { id: 107, title: "John the Baptist's Doubt",
    aboutTitle: 'A story about the man who doubted from a prison cell', scriptureRef: 'Matthew 11:2-11', videoUrl: null,
    seedQuestion: 'If even the boldest believer had a hard question, is God offended by yours?',
    takeaway: "This helped me see that honest doubt doesn't lower me in his eyes." },
  { id: 108, title: 'My Sheep Hear My Voice',
    aboutTitle: 'A story about a shepherd who calls each one by name', scriptureRef: 'John 10:27-28', videoUrl: null,
    seedQuestion: 'What if God knows your name, not just your face in the crowd?',
    takeaway: "This helped me see that he knows me personally, not just generally." },
  { id: 111, title: 'Lilies and Sparrows',
    aboutTitle: 'A story about birds fed and flowers dressed without trying', scriptureRef: 'Matthew 6:25-34', videoUrl: null,
    seedQuestion: 'If he feeds the sparrows without being asked, how much is he already carrying for you?',
    takeaway: "This helped me see that God is already taking care of what I'm worried about." },
  { id: 185, title: "In My Father's House",
    aboutTitle: 'A story about a room already being made ready for you', scriptureRef: 'John 14:2-3', videoUrl: null,
    seedQuestion: 'What if God is not waiting for you to arrive, but preparing the place himself?',
    takeaway: "This helped me see that there is already room for me in his house." },
  { id: 186, title: 'Heirs of God',
    aboutTitle: 'A story about being family instead of a guest', scriptureRef: 'Romans 8:16-17', videoUrl: null,
    seedQuestion: 'What if God sees you as family, not as a visitor he has to tolerate?',
    takeaway: "This helped me see that I belong at his table as family, not as a guest." },
  { id: 187, title: 'Ye Are Gods',
    aboutTitle: 'A story about what God calls his own children', scriptureRef: 'Psalm 82:6', videoUrl: null,
    seedQuestion: 'What if God thinks higher of you than you have ever thought of yourself?',
    takeaway: "This helped me see that God calls me his child before I ever earn it." },
  { id: 190, title: 'Faith Without Works',
    aboutTitle: 'A story about faith you can hand someone', scriptureRef: 'James 2:14-26', videoUrl: null,
    seedQuestion: 'What if the God you picture cares less about what you say and more about the bread you hand over?',
    takeaway: "This helped me see that my faith becomes real the moment it moves." },
  { id: 191, title: 'The Windows of Heaven',
    aboutTitle: 'A story about a God who dared them to test him', scriptureRef: 'Malachi 3:10', videoUrl: null,
    seedQuestion: 'What kind of God invites you to test his goodness instead of demanding you just trust it?',
    takeaway: "This helped me see that he wants to be tested, because he knows he'll come through." },
  { id: 192, title: 'The Fast God Has Chosen',
    aboutTitle: 'A story about the ropes God wants untied', scriptureRef: 'Isaiah 58:6-12', videoUrl: null,
    seedQuestion: 'What if what God wants from you is not going without, but opening your door?',
    takeaway: "This helped me see that God would rather I feed someone than impress him." },
  { id: 193, title: 'The Comforter',
    aboutTitle: 'A story about the night he promised not to leave them alone', scriptureRef: 'John 14:26', videoUrl: null,
    seedQuestion: 'On his hardest night, would he really be thinking about who would stay with you?',
    takeaway: "This helped me see that I was never meant to remember him alone." },
  { id: 194, title: 'The Fruit of the Spirit',
    aboutTitle: 'A story about what grows in a person quietly', scriptureRef: 'Galatians 5:22-23', videoUrl: null,
    seedQuestion: 'What if God grows the good in you instead of demanding you produce it?',
    takeaway: "This helped me see that the good in me is grown, not forced." },
  { id: 195, title: 'Prove All Things',
    aboutTitle: 'A story about a faith that is allowed to ask questions', scriptureRef: '1 Thessalonians 5:21', videoUrl: null,
    seedQuestion: 'What if God is not nervous about you weighing what you have been told?',
    takeaway: "This helped me see that God isn't afraid of my questions — he expects them." },
  { id: 196, title: "Would God That All The Lord's People Were Prophets",
    aboutTitle: 'A story about two men who prophesied in the camp', scriptureRef: 'Numbers 11:24-29', videoUrl: null,
    seedQuestion: 'What if God is not stingy with what he gives — and never was?',
    takeaway: "This helped me see that God wants to share his gift, not guard it." },
  { id: 197, title: 'Your Sons And Your Daughters Shall Prophesy',
    aboutTitle: 'A story about a promise poured out on everybody', scriptureRef: 'Joel 2:28-29', videoUrl: null,
    seedQuestion: 'What if the promise was never meant for insiders only?',
    takeaway: "This helped me see that God's promise included ordinary people like me." },
  { id: 198, title: 'An Ensign For The Nations',
    aboutTitle: 'A story about a banner raised so people could find their way home', scriptureRef: 'Isaiah 11:10-12', videoUrl: null,
    seedQuestion: 'What if God lifts something up high just so you can find him?',
    takeaway: "This helped me see that God makes himself findable on purpose." },
  { id: 199, title: 'Fishers And Hunters',
    aboutTitle: 'A story about a search that reached every hiding place', scriptureRef: 'Jeremiah 16:16', videoUrl: null,
    seedQuestion: 'What if the one searching for you wants you found, not caught?',
    takeaway: "This helped me see that God searches for me because he wants me home." },
  { id: 200, title: 'The Gospel To All The World',
    aboutTitle: 'A story about good news that was never meant to stay put', scriptureRef: 'Matthew 24:14', videoUrl: null,
    seedQuestion: 'If the news was good enough to send everywhere, what does that say about who it was for?',
    takeaway: "This helped me see that the invitation was always meant to reach everyone." },
];

// Derive the stream URL for every produced clip, so adding an id to
// PRODUCED_VIDEO_IDS is the single go-live switch. Un-produced entries keep
// videoUrl: null and the card shows its verse-only placeholder.
for (const v of VIDEO_STORIES) {
  if (isVideoProduced(v.id)) {
    if (!v.videoUrl) v.videoUrl = videoStreamUrl(v.id);
    if (!v.thumbUrl) v.thumbUrl = videoThumbUrl(v.id);
  }
}

const VIDEO_BY_ID: Record<number, VideoStory> = Object.fromEntries(
  VIDEO_STORIES.map(v => [v.id, v]),
);

export function videoById(id: number): VideoStory | undefined {
  return VIDEO_BY_ID[id];
}
