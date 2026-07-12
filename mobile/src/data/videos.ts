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
// Wave one (Cameron checked and approved, 2026-07-11): catalog #1–15 and #17.
// #16 (Mary and Martha) is still mid-build — stills 5–6 unrendered, never
// assembled — and joins this list when its final ships.
export const PRODUCED_VIDEO_IDS = new Set<number>([
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17,
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
