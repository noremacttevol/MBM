/**
 * pageEngine.ts — the prescribed-feed page model for Feed 2.0.
 *
 * A "page" is one prescribed unit of the feed: 2 video+verse pairs, 0–1 rare
 * standalone verse, 1 question, and 1 invitation at the bottom. ~100 pages make
 * the whole prescribed feed (200 videos ÷ 2 per page). Pages accumulate — the
 * newest is HOME; older ones stay re-viewable behind it (wheel navigation).
 *
 * This module is pure: it composes pages and answers "is this honored?" It holds
 * no state and does no I/O. The store (useAppStore) owns the pages array, the
 * honoring transitions, the wait ladder counter, and persistence.
 *
 * HONORING (FEED-2.0-SPEC §2): an item is honored when the user actually
 * experienced it — a video watched to 100%, a verse link opened, a question
 * answered, an invitation acted on. A video and its paired verse honor
 * SEPARATELY, which is why VideoPairItem has two flags.
 */

import { ContentItem } from '../data/content';
import { VideoStory, videoById } from '../data/videos';
import { DialogueQuestion } from '../data/questionBank';
import { SpiritualExercise } from './exercises';

export type PageItemKind = 'videoPair' | 'verse' | 'question' | 'invitation';

/** A video and the KJV verse beneath it. The two honor independently. */
export interface VideoPairItem {
  kind:         'videoPair';
  slotId:       string;
  videoId:      number;
  /** The paired verse. */
  verseRef:     string;
  /** CONTENT id for the verse, when one exists (enables inline KJV). */
  verseContentId?: number;
  videoHonored: boolean;
  verseHonored: boolean;
}

/**
 * A standalone verse slot (0–1 per page). Either drawn from the milk verse pool
 * (`contentId` set) or a verse RECYCLED from a video whose story was watched but
 * whose verse was skipped — resurfaced later as a gentle reminder
 * (`recycledFromVideoId`/`recycledFromTitle` set).
 */
export interface VerseItem {
  kind:      'verse';
  slotId:    string;
  scriptureRef: string;
  contentId?:   number;
  recycledFromVideoId?: number;
  recycledFromTitle?:   string;
  honored:   boolean;
}

export interface QuestionItem {
  kind:       'question';
  slotId:     string;
  questionId: number;
  honored:    boolean;
}

export interface InvitationItem {
  kind:       'invitation';
  slotId:     string;
  exerciseId: string;
  honored:    boolean;
}

export type PageItem = VideoPairItem | VerseItem | QuestionItem | InvitationItem;

export interface Page {
  id:               string;
  /** Display number (0 = the first prescribed page ever). */
  index:            number;
  items:            PageItem[];
  /** Session in which this page was created (for the honored-nothing refresh rule). */
  createdInSession: number;
  /**
   * True once this page has been archived behind a newer home page. Archived
   * pages are the re-viewable history and never auto-refresh.
   */
  archived:         boolean;
  /**
   * True for the "honored history" bucket that honored items slide into when the
   * user leaves the home page. Repeated scroll-aways append to the same bucket so
   * the wheel gains one dot per real page, not one per interaction.
   */
  honorArchive?:    boolean;
}

/** True when an item counts as fully honored (a pair needs BOTH halves). */
export function isItemHonored(it: PageItem): boolean {
  if (it.kind === 'videoPair') return it.videoHonored && it.verseHonored;
  return it.honored;
}

/** True when nothing on the page has been honored at all. */
export function pageHasNoHonoring(page: Page): boolean {
  return page.items.every(it =>
    it.kind === 'videoPair' ? (!it.videoHonored && !it.verseHonored) : !it.honored,
  );
}

// ── Wait ladder (FEED-2.0-SPEC §4) ───────────────────────────────────────────
// Next-page waits per session: 5s for attempts 1–3, 15s for 4–6, 30s for 7–9,
// then 60s, adding 60s for each attempt after that. Resets every app session.
export function waitLadderSeconds(attempt: number): number {
  if (attempt <= 3) return 5;
  if (attempt <= 6) return 15;
  if (attempt <= 9) return 30;
  return 60 * (attempt - 9); // attempt 10 → 60, 11 → 120, 12 → 180, …
}

// ── Composition ──────────────────────────────────────────────────────────────

function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export function makeVideoPair(video: VideoStory, newId: () => string): VideoPairItem {
  return {
    kind:           'videoPair',
    slotId:         newId(),
    videoId:        video.id,
    verseRef:       video.scriptureRef,
    verseContentId: video.contentId,
    videoHonored:   false,
    verseHonored:   false,
  };
}

export function makeVerseFromContent(item: ContentItem, newId: () => string): VerseItem {
  return {
    kind:         'verse',
    slotId:       newId(),
    scriptureRef: item.scriptureRef,
    contentId:    item.id,
    honored:      false,
  };
}

export function makeRecycledVerse(video: VideoStory, newId: () => string): VerseItem {
  return {
    kind:                'verse',
    slotId:              newId(),
    scriptureRef:        video.scriptureRef,
    contentId:           video.contentId,
    recycledFromVideoId: video.id,
    recycledFromTitle:   video.title,
    honored:             false,
  };
}

export function makeQuestionItem(q: DialogueQuestion, newId: () => string): QuestionItem {
  return { kind: 'question', slotId: newId(), questionId: q.id, honored: false };
}

export function makeInvitationItem(ex: SpiritualExercise, newId: () => string): InvitationItem {
  return { kind: 'invitation', slotId: newId(), exerciseId: ex.id, honored: false };
}

export interface ComposeInputs {
  /** Full video spine to draw the 2 pairs from. */
  videoPool:     VideoStory[];
  /** Video ids already placed on a page this cycle (avoid immediate repeats). */
  seenVideoIds:  number[];
  /** Milk verses eligible for the standalone slot. */
  versePool:     ContentItem[];
  /** CONTENT ids already used as a standalone verse this cycle. */
  seenVerseIds:  number[];
  /** Recycled skipped verses (as video ids) to resurface first, newest last. */
  recycledVideoIds: number[];
  question:      DialogueQuestion | null;
  exercise:      SpiritualExercise | null;
  /** How likely a page gets a standalone verse when none is being recycled. */
  standaloneVerseChance?: number;
}

export interface ComposeResult {
  items:                PageItem[];
  usedVideoIds:         number[];
  usedVerseContentIds:  number[];
  /** Recycled video ids that were consumed into this page's standalone verse. */
  consumedRecycledIds:  number[];
}

/**
 * Compose one fresh page. Draws 2 unseen video pairs (cycling once the spine is
 * exhausted), then a standalone verse (a recycled skipped verse first, else a
 * rare pool verse), then the current question and invitation.
 */
export function composePage(inp: ComposeInputs, newId: () => string): ComposeResult {
  const usedVideoIds: number[] = [];
  const usedVerseContentIds: number[] = [];
  const consumedRecycledIds: number[] = [];
  const items: PageItem[] = [];

  // ── 2 video+verse pairs ────────────────────────────────────────────────────
  const seenV = new Set(inp.seenVideoIds);
  const unseen = inp.videoPool.filter(v => !seenV.has(v.id));
  const source = unseen.length >= 2 ? unseen : inp.videoPool; // cycle when exhausted
  const pick = shuffle(source).slice(0, 2);
  for (const v of pick) {
    items.push(makeVideoPair(v, newId));
    usedVideoIds.push(v.id);
  }

  // ── 0–1 standalone verse ────────────────────────────────────────────────────
  // A recycled skipped verse takes priority — its whole point is to come back.
  const recycledId = inp.recycledVideoIds.length > 0 ? inp.recycledVideoIds[0] : null;
  if (recycledId != null) {
    const v = videoById(recycledId);
    if (v) {
      items.push(makeRecycledVerse(v, newId));
      consumedRecycledIds.push(recycledId);
    }
  } else {
    const chance = inp.standaloneVerseChance ?? 0.4;
    if (Math.random() < chance && inp.versePool.length > 0) {
      const seenVerse = new Set(inp.seenVerseIds);
      const unseenVerses = inp.versePool.filter(c => !seenVerse.has(c.id));
      const vsrc = unseenVerses.length > 0 ? unseenVerses : inp.versePool;
      const verse = shuffle(vsrc)[0];
      items.push(makeVerseFromContent(verse, newId));
      usedVerseContentIds.push(verse.id);
    }
  }

  // ── 1 question ──────────────────────────────────────────────────────────────
  if (inp.question) items.push(makeQuestionItem(inp.question, newId));

  // ── 1 invitation (always last) ──────────────────────────────────────────────
  if (inp.exercise) items.push(makeInvitationItem(inp.exercise, newId));

  return { items, usedVideoIds, usedVerseContentIds, consumedRecycledIds };
}
