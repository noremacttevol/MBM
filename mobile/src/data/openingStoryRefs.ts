/**
 * openingStoryRefs — which scripture passages each cold-open story is drawn from.
 *
 * Purpose: the story told on the opening screen must NEVER show up again as a
 * feed card in the same session ("that would be ridiculous" — Cameron, July 5
 * 2026). Every opening story id maps to the chapter prefixes of the passages it
 * retells; buildFeed() in useAppStore filters out any content item whose
 * scriptureRef starts with one of these prefixes for a story seen this session.
 *
 * Matching rule: prefixes end at the chapter colon (e.g. 'Luke 15:') so that
 * 'John 4:' can never accidentally match 'John 14:27'. A few entries are
 * whole-chapter book names without verses (none currently) — keep the colon
 * whenever the source content uses "Book C:V" refs, which content.ts does.
 */

export const OPENING_STORY_REFS: Record<string, string[]> = {
  // The woman who touched his cloak (Mark 5:25–34; Luke 8:43–48; Matt 9:20–22)
  cloak:      ['Mark 5:', 'Luke 8:', 'Matthew 9:'],
  // The Prodigal Son (Luke 15:11–32)
  prodigal:   ['Luke 15:'],
  // Zacchaeus (Luke 19:1–10)
  zacchaeus:  ['Luke 19:'],
  // Nicodemus by night (John 3)
  nicodemus:  ['John 3:'],
  // The bent-over woman healed on the Sabbath (Luke 13:10–17)
  bent_woman: ['Luke 13:'],
  // The parable of the two sons (Matthew 21:28–32)
  two_sons:   ['Matthew 21:'],
  // Peter walks on water (Matthew 14:22–33)
  peter_water: ['Matthew 14:'],
  // The lost coin (Luke 15:8–10) — same chapter as the prodigal
  lost_coin:  ['Luke 15:'],
  // The rich young ruler (Mark 10:17–27; Matt 19:16–26; Luke 18:18–27)
  rich_ruler: ['Mark 10:17', 'Mark 10:18', 'Mark 10:19', 'Mark 10:2', 'Matthew 19:', 'Luke 18:'],
  // The woman at the well (John 4:1–42)
  well:       ['John 4:'],
  // Calming the storm (Mark 4:35–41; Matt 8:23–27; Luke 8:22–25)
  storm:      ['Mark 4:', 'Matthew 8:23', 'Matthew 8:24', 'Matthew 8:25', 'Matthew 8:26', 'Matthew 8:27', 'Luke 8:'],
  // Blind Bartimaeus (Mark 10:46–52; Luke 18:35–43)
  bartimaeus: ['Mark 10:46', 'Mark 10:47', 'Mark 10:48', 'Mark 10:49', 'Mark 10:5', 'Luke 18:'],
  // The paralytic lowered through the roof (Mark 2:1–12; Luke 5:17–26)
  roof:       ['Mark 2:', 'Luke 5:'],
  // The ten lepers (Luke 17:11–19)
  ten_lepers: ['Luke 17:'],
  // The centurion's servant (Matthew 8:5–13; Luke 7:1–10)
  centurion:  ['Matthew 8:5', 'Matthew 8:6', 'Matthew 8:7', 'Matthew 8:8', 'Matthew 8:9', 'Matthew 8:1', 'Luke 7:'],
  // Mary and Martha (Luke 10:38–42)
  mary_martha: ['Luke 10:38', 'Luke 10:39', 'Luke 10:4'],
  // The raising of Lazarus / Jesus wept (John 11)
  lazarus:    ['John 11:'],
  // The road to Emmaus (Luke 24:13–35)
  emmaus:     ['Luke 24:'],
  // Breakfast on the shore — Peter restored (John 21)
  shore:      ['John 21:'],
  // The Good Samaritan (Luke 10:25–37)
  samaritan:  ['Luke 10:25', 'Luke 10:26', 'Luke 10:27', 'Luke 10:28', 'Luke 10:29', 'Luke 10:3'],
};

/**
 * True if a content item's scriptureRef belongs to any of the given opening
 * stories. Prefix match against the ref string ("Luke 15:11-32" starts with
 * "Luke 15:").
 */
export function refBelongsToStories(scriptureRef: string | undefined, storyIds: string[]): boolean {
  if (!scriptureRef) return false;
  for (const id of storyIds) {
    const prefixes = OPENING_STORY_REFS[id];
    if (!prefixes) continue;
    for (const p of prefixes) {
      if (scriptureRef.startsWith(p)) return true;
    }
  }
  return false;
}
