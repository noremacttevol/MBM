import { believesGodGood, openToMore, mayReferenceLds, isMember } from '../engine/connect';

export type AnswerType = 'FREE_TEXT' | 'YES_NO' | 'CHOICE';
export type QuestionStage = 'ENTRY' | 'EARLY' | 'MID' | 'DEEP';

export type TraitKey =
  | 'honest_inquiry'
  | 'openness'
  | 'humility'
  | 'hunger'
  | 'compassion'
  | 'courage'
  | 'sincerity';

export type TraitScores = Record<TraitKey, number>;

export const DEFAULT_TRAITS: TraitScores = {
  honest_inquiry: 5.0,
  openness:       5.0,
  humility:       5.0,
  hunger:         5.0,
  compassion:     5.0,
  courage:        5.0,
  sincerity:      5.0,
};

export const TRAIT_MIN = 0.0;
export const TRAIT_MAX = 10.0;

export interface AnswerOption {
  text:         string;
  value:        string;
  signals?:     string[];
  traitSignals?: Partial<TraitScores>;
}

export interface DialogueQuestion {
  id:                  number;
  stage:               QuestionStage;
  topic:               string;
  questionText:        string;
  answerType:          AnswerType;
  answerOptions:       AnswerOption[];
  traitSignals:        Partial<TraitScores>;
  prerequisiteSignals: string[];
  jesusReference:      string;
}

export const STAGE_ORDER: Record<QuestionStage, number> = {
  ENTRY: 0,
  EARLY: 1,
  MID:   2,
  DEEP:  3,
};

export const QUESTION_BANK: DialogueQuestion[] = [

  // ══════════════════════════════════════════
  // ENTRY — Universal. Anyone can answer.
  // ══════════════════════════════════════════

  {
    id: 1, stage: 'ENTRY', topic: 'worth_living',
    questionText: "What's one thing that makes life feel worth it to you — even on the hard days?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { sincerity: 0.3, hunger: 0.2 },
    prerequisiteSignals: [],
    jesusReference: 'John 10:10 — I came that they may have life, and have it abundantly.',
  },
  {
    id: 2, stage: 'ENTRY', topic: 'unseen',
    questionText: "Have you ever had a moment — a place, a person, something you can't quite explain — that made you feel like there's more to this world than what you can see?",
    answerType: 'YES_NO',
    answerOptions: [
      {
        text: "Yes — something has felt real to me that I can't fully explain.",
        value: 'yes',
        signals: ['had_spiritual_experience'],
        traitSignals: { openness: 0.35, honest_inquiry: 0.2, hunger: 0.2 },
      },
      {
        text: 'Not that I can point to.',
        value: 'no',
        traitSignals: { honest_inquiry: 0.25 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: "John 3:8 — The wind blows where it wishes. You hear its sound but cannot tell where it comes from.",
  },
  {
    id: 3, stage: 'ENTRY', topic: 'burden',
    questionText: "What's the heaviest thing you're carrying right now that you wish you could put down?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { courage: 0.3, sincerity: 0.3, hunger: 0.2 },
    prerequisiteSignals: [],
    jesusReference: 'Matthew 11:28 — Come to me, all who are weary and burdened, and I will give you rest.',
  },
  {
    id: 4, stage: 'ENTRY', topic: 'god_feeling',
    questionText: "When you hear the word 'God' — what's the first feeling that comes up? Not what you think. What you feel.",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "Peace — I know him, and I know he's good.",
        value: 'knows_god',
        signals: ['believes_god_good', 'open_to_god'],
        traitSignals: { sincerity: 0.35, courage: 0.25, hunger: 0.2 },
      },
      {
        text: 'Something warm — like coming home.',
        value: 'warm',
        signals: ['open_to_god'],
        traitSignals: { openness: 0.3, hunger: 0.25, sincerity: 0.2 },
      },
      {
        text: "Complicated — there's history there.",
        value: 'complicated',
        signals: ['has_history_with_faith'],
        traitSignals: { honest_inquiry: 0.3, courage: 0.25, humility: 0.2 },
      },
      {
        text: "Distant — like it doesn't apply to me.",
        value: 'distant',
        traitSignals: { honest_inquiry: 0.25, openness: 0.15 },
      },
      {
        text: "Skeptical — I'm not sure there's anything there.",
        value: 'skeptical',
        signals: ['skeptical_of_god'],
        traitSignals: { honest_inquiry: 0.35, courage: 0.2 },
      },
      {
        text: "Honestly — I don't know what I feel.",
        value: 'unknown',
        traitSignals: { honest_inquiry: 0.25, humility: 0.2, openness: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: 'John 4:23 — The Father is seeking people who will worship him in spirit and in truth.',
  },
  {
    id: 5, stage: 'ENTRY', topic: 'unseen_good',
    questionText: "What's something good you've done recently that nobody noticed?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { sincerity: 0.35, compassion: 0.3, humility: 0.2 },
    prerequisiteSignals: [],
    jesusReference: 'Matthew 6:3-4 — When you give to the needy, do not let your left hand know what your right hand is doing.',
  },

  // ══════════════════════════════════════════
  // EARLY — After content. Warm, going deeper.
  // ══════════════════════════════════════════

  {
    id: 6, stage: 'EARLY', topic: 'after_content',
    questionText: "That piece you just read — what did it stir in you? Even if it's hard to name.",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { sincerity: 0.3, honest_inquiry: 0.2, hunger: 0.15 },
    prerequisiteSignals: ['viewed_content'],
    jesusReference: 'Luke 24:32 — Were not our hearts burning within us while he talked with us?',
  },
  {
    id: 7, stage: 'EARLY', topic: 'resonance',
    questionText: "Is there a part of what you've been reading here that keeps coming back to you — something that won't quite leave?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { hunger: 0.3, sincerity: 0.25, openness: 0.2 },
    prerequisiteSignals: ['viewed_content'],
    jesusReference: "John 6:68 — Lord, to whom shall we go? You have words of eternal life.",
  },
  {
    id: 8, stage: 'EARLY', topic: 'prayer',
    questionText: "Have you ever said something out loud — or in your head — that was kind of a prayer, even if you weren't sure anyone was listening?",
    answerType: 'YES_NO',
    answerOptions: [
      {
        text: "Yes — I've done something like that.",
        value: 'yes',
        signals: ['prayed_before'],
        traitSignals: { openness: 0.3, sincerity: 0.25, hunger: 0.2 },
      },
      {
        text: "No — that's not something I've done.",
        value: 'no',
        traitSignals: { honest_inquiry: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: 'Luke 11:2 — When you pray, say: Father...',
  },
  {
    id: 9, stage: 'EARLY', topic: 'afterlife',
    questionText: "What do you think happens after you die? You don't have to have a certain answer — what do you actually think?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "Nothing — consciousness ends and that's it.",
        value: 'nothing',
        traitSignals: { honest_inquiry: 0.3 },
      },
      {
        text: "Something — but I genuinely don't know what.",
        value: 'something_unknown',
        traitSignals: { honest_inquiry: 0.2, hunger: 0.2, openness: 0.2 },
      },
      {
        text: "I believe I'll live again — this life isn't the end.",
        value: 'have_belief',
        signals: ['has_afterlife_belief'],
        traitSignals: { sincerity: 0.3, courage: 0.2, openness: 0.15 },
      },
      {
        text: "I try not to think about it.",
        value: 'avoid',
        traitSignals: { honest_inquiry: 0.2, hunger: 0.1 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: 'John 11:25 — I am the resurrection and the life. Whoever believes in me, though he die, yet shall he live.',
  },
  {
    id: 10, stage: 'EARLY', topic: 'goodness',
    questionText: "Do you think there's such a thing as genuine goodness — something that's actually right, not just what most people agree on?",
    answerType: 'YES_NO',
    answerOptions: [
      {
        text: "Yes — some things are actually right or wrong, not just opinions.",
        value: 'yes',
        signals: ['believes_in_moral_truth'],
        traitSignals: { honest_inquiry: 0.2, humility: 0.15, openness: 0.15 },
      },
      {
        text: "No — right and wrong are just what we agree on collectively.",
        value: 'no',
        traitSignals: { honest_inquiry: 0.25 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: 'Mark 10:18 — Why do you call me good? No one is good except God alone.',
  },
  {
    id: 11, stage: 'EARLY', topic: 'longing',
    questionText: "Is there something you've been looking for — in relationships, in work, in life — that you haven't found yet?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { hunger: 0.35, sincerity: 0.3, courage: 0.2 },
    prerequisiteSignals: [],
    jesusReference: 'John 1:38 — What are you seeking? The first question Jesus asked anyone.',
  },
  {
    id: 12, stage: 'EARLY', topic: 'grief',
    questionText: "Have you lost someone — or something — that left a hole you haven't been able to fill?",
    answerType: 'YES_NO',
    answerOptions: [
      {
        text: "Yes — I'm still carrying that.",
        value: 'yes',
        signals: ['carries_grief'],
        traitSignals: { sincerity: 0.35, courage: 0.3, hunger: 0.2 },
      },
      {
        text: "Not in a way that's still affecting me.",
        value: 'no',
        traitSignals: { honest_inquiry: 0.15 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: 'John 11:35 — Jesus wept. The shortest verse. The most human.',
  },
  {
    id: 13, stage: 'EARLY', topic: 'habits',
    questionText: "Is there anything in your life right now that you keep going back to — that you know isn't good for you, but you can't seem to put down?",
    answerType: 'YES_NO',
    answerOptions: [
      {
        text: "Yes — there's something like that in my life.",
        value: 'yes',
        signals: ['struggles_with_habits'],
        traitSignals: { courage: 0.35, sincerity: 0.3, humility: 0.2 },
      },
      {
        text: "Not really — that's not where I'm at.",
        value: 'no',
        traitSignals: { honest_inquiry: 0.15 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: 'John 8:36 — If the Son sets you free, you will be free indeed.',
  },
  {
    id: 14, stage: 'EARLY', topic: 'community',
    questionText: "Do you have people in your life who actually know you — not just the version you show at work or online?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "Yes — I have a few people like that.",
        value: 'yes',
        traitSignals: { sincerity: 0.2, compassion: 0.15 },
      },
      {
        text: "Sort of — but even they don't see the whole picture.",
        value: 'partial',
        traitSignals: { sincerity: 0.25, hunger: 0.15 },
      },
      {
        text: "Not really — it's lonelier than it looks.",
        value: 'no',
        signals: ['lonely'],
        traitSignals: { hunger: 0.3, sincerity: 0.3, courage: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: 'John 15:15 — I no longer call you servants. I have called you friends.',
  },
  {
    id: 15, stage: 'EARLY', topic: 'purpose',
    questionText: "Do you ever get the feeling that your life is supposed to mean something specific — that there's a purpose you haven't quite found yet?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "Yes — I feel that pull strongly.",
        value: 'yes_strong',
        signals: ['searching_for_purpose'],
        traitSignals: { hunger: 0.35, sincerity: 0.25, openness: 0.2 },
      },
      {
        text: "Sometimes — it comes and goes.",
        value: 'sometimes',
        signals: ['searching_for_purpose'],
        traitSignals: { hunger: 0.2, openness: 0.15 },
      },
      {
        text: "Not really — I think we make our own meaning.",
        value: 'no',
        traitSignals: { honest_inquiry: 0.25 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: 'John 17:4 — I have glorified you on earth, having accomplished the work you gave me to do.',
  },
  {
    id: 16, stage: 'EARLY', topic: 'family_faith',
    questionText: "Did you grow up in a home that had faith in it — and is the relationship you have with that now the same or different?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "Yes — and I'm still in the same place as I grew up.",
        value: 'same',
        traitSignals: { sincerity: 0.2 },
      },
      {
        text: "Yes — but I've moved away from it.",
        value: 'moved_away',
        signals: ['has_history_with_faith', 'family_faith_tension'],
        traitSignals: { honest_inquiry: 0.25, courage: 0.2 },
      },
      {
        text: "Yes — and I've actually gone deeper than my upbringing.",
        value: 'deeper',
        traitSignals: { hunger: 0.3, sincerity: 0.25 },
      },
      {
        text: "No — I wasn't raised in faith.",
        value: 'no_faith_upbringing',
        traitSignals: { honest_inquiry: 0.2, openness: 0.15 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: "Luke 2:49 — Did you not know that I must be in my Father's house?",
  },
  {
    id: 17, stage: 'EARLY', topic: 'pain_response',
    questionText: "When life gets really hard — what's your first instinct? Where do you go, or what do you do?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "I isolate and go inward.",
        value: 'isolate',
        traitSignals: { courage: 0.15, sincerity: 0.2 },
      },
      {
        text: "I talk to someone I trust.",
        value: 'talk',
        traitSignals: { compassion: 0.2, sincerity: 0.2 },
      },
      {
        text: "I distract myself — keep moving, don't think.",
        value: 'distract',
        traitSignals: { honest_inquiry: 0.2 },
      },
      {
        text: "I look for something bigger than myself — prayer, nature, anything.",
        value: 'transcendent',
        signals: ['open_to_god'],
        traitSignals: { openness: 0.3, hunger: 0.25, sincerity: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: 'Mark 1:35 — Very early in the morning, while it was still dark, Jesus got up, left the house, and prayed.',
  },
  {
    id: 18, stage: 'EARLY', topic: 'spiritual_experience_depth',
    questionText: "That experience you mentioned — the one you couldn't explain — did it change something in you, or did you set it aside?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "It changed something — I've never fully explained it but I know it mattered.",
        value: 'changed',
        traitSignals: { openness: 0.35, hunger: 0.3, sincerity: 0.25 },
      },
      {
        text: "I've thought about it but I'm still not sure what it means.",
        value: 'unsure',
        traitSignals: { honest_inquiry: 0.3, openness: 0.2, humility: 0.2 },
      },
      {
        text: "I set it aside — it felt too big to sit with.",
        value: 'set_aside',
        traitSignals: { honest_inquiry: 0.25, courage: 0.2, hunger: 0.15 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['had_spiritual_experience'],
    jesusReference: 'Luke 24:32 — Did not our hearts burn within us while he talked with us on the road?',
  },

  // ══════════════════════════════════════════
  // MID — Deeper. Still warm.
  // ══════════════════════════════════════════

  {
    id: 19, stage: 'MID', topic: 'jesus_feeling',
    questionText: "When you hear about Jesus — not the religion, just the person — what do you feel toward him?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "Something draws me toward him — I'm not sure why.",
        value: 'drawn',
        signals: ['drawn_to_jesus'],
        traitSignals: { openness: 0.35, hunger: 0.3, sincerity: 0.2 },
      },
      {
        text: "I respect him but keep my distance.",
        value: 'respect_distance',
        traitSignals: { honest_inquiry: 0.25, openness: 0.15 },
      },
      {
        text: "I love him — he's real to me.",
        value: 'love',
        signals: ['believes_in_jesus'],
        traitSignals: { sincerity: 0.35, hunger: 0.2, courage: 0.2 },
      },
      {
        text: "I'm skeptical of the whole story.",
        value: 'skeptical',
        signals: ['skeptical_of_jesus'],
        traitSignals: { honest_inquiry: 0.35, courage: 0.2 },
      },
      {
        text: "I used to feel something, but that's complicated now.",
        value: 'complicated',
        signals: ['has_history_with_faith', 'hurt_by_faith'],
        traitSignals: { honest_inquiry: 0.3, courage: 0.3, humility: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: 'Matthew 16:15 — But who do YOU say I am?',
  },
  {
    id: 20, stage: 'MID', topic: 'forgiveness',
    questionText: "Is there someone in your life you've never fully forgiven — or something you haven't forgiven yourself for?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { courage: 0.35, sincerity: 0.35, compassion: 0.2 },
    prerequisiteSignals: [],
    jesusReference: 'Matthew 18:21-22 — How many times shall I forgive? Not seven, but seventy times seven.',
  },
  {
    id: 21, stage: 'MID', topic: 'change',
    questionText: "Is there a version of yourself you want to become — someone you can picture but haven't fully stepped into yet?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { hunger: 0.35, courage: 0.25, humility: 0.2 },
    prerequisiteSignals: [],
    jesusReference: "John 1:42 — You are Simon. You will be called Peter. Jesus named what someone could become.",
  },
  {
    id: 22, stage: 'MID', topic: 'love_received',
    questionText: "What's the most loved you've ever felt by another person — and what made it feel real?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { sincerity: 0.3, compassion: 0.25, hunger: 0.2 },
    prerequisiteSignals: [],
    jesusReference: "John 15:13 — Greater love has no one than this: to lay down one's life for one's friends.",
  },
  {
    id: 23, stage: 'MID', topic: 'trust',
    questionText: "Is there something you believe in deeply — but feel like you can't say out loud without people judging you for it?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { courage: 0.4, sincerity: 0.35, honest_inquiry: 0.2 },
    prerequisiteSignals: [],
    jesusReference: 'John 7:13 — No one would speak openly about him for fear of the Jewish leaders.',
  },
  {
    id: 24, stage: 'MID', topic: 'scripture_openness',
    questionText: "Have you ever actually read the Gospels for yourself — not what someone told you they said, but read them directly?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "Yes — and they've stayed with me.",
        value: 'yes_stayed',
        signals: ['open_to_scripture'],
        traitSignals: { hunger: 0.3, openness: 0.25, sincerity: 0.2 },
      },
      {
        text: "A little — some parts, not all of it.",
        value: 'partial',
        signals: ['open_to_scripture'],
        traitSignals: { openness: 0.2, honest_inquiry: 0.2 },
      },
      {
        text: "No — I haven't gotten there.",
        value: 'no',
        traitSignals: { honest_inquiry: 0.2 },
      },
      {
        text: "I've tried but found it hard to connect with.",
        value: 'tried_failed',
        traitSignals: { honest_inquiry: 0.25, openness: 0.15 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: 'Luke 4:17 — He opened the scroll and found the place where it was written.',
  },
  {
    id: 25, stage: 'MID', topic: 'identity_source',
    questionText: "When everything else is stripped away — what's left that you know for certain about who you are?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { sincerity: 0.4, courage: 0.3, humility: 0.25 },
    prerequisiteSignals: [],
    jesusReference: 'Matthew 3:17 — A voice from heaven said: This is my Son, whom I love. Identity spoken before the work began.',
  },
  {
    id: 26, stage: 'MID', topic: 'sacrifice',
    questionText: "Is there something you'd give up everything for — something you'd sacrifice significantly to protect or pursue?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { courage: 0.35, sincerity: 0.3, compassion: 0.25 },
    prerequisiteSignals: [],
    jesusReference: 'Matthew 13:46 — When he found one pearl of great value, he went and sold everything he had and bought it.',
  },
  {
    id: 27, stage: 'MID', topic: 'doubt_honest',
    questionText: "What do you most wish you could believe, but honestly can't get yourself to believe right now?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { honest_inquiry: 0.4, courage: 0.35, humility: 0.3 },
    prerequisiteSignals: [],
    jesusReference: 'Mark 9:24 — I believe. Help my unbelief.',
  },

  // ══════════════════════════════════════════
  // MID — Signal-gated follow-ups
  // ══════════════════════════════════════════

  {
    id: 28, stage: 'MID', topic: 'what_happened',
    questionText: "It sounds like there's some history with faith for you. Would you be willing to say — what happened?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { honest_inquiry: 0.3, courage: 0.35, sincerity: 0.3 },
    prerequisiteSignals: ['has_history_with_faith'],
    jesusReference: 'John 21:17 — Peter, do you love me? Jesus asked three times — not to shame him, but to make space.',
  },
  {
    id: 29, stage: 'MID', topic: 'hurt_by_faith',
    questionText: "Has a church, or someone in a church, ever hurt you or let you down in a serious way?",
    answerType: 'YES_NO',
    answerOptions: [
      {
        text: "Yes — and I haven't fully resolved it.",
        value: 'yes_unresolved',
        signals: ['hurt_by_church'],
        traitSignals: { honest_inquiry: 0.25, courage: 0.35, sincerity: 0.2 },
      },
      {
        text: "Yes — but I've made peace with it.",
        value: 'yes_resolved',
        traitSignals: { courage: 0.2, humility: 0.2, sincerity: 0.2 },
      },
      {
        text: "No — that hasn't been my experience.",
        value: 'no',
        traitSignals: { honest_inquiry: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['has_history_with_faith'],
    jesusReference: 'Luke 15:4 — What person, having a hundred sheep and losing one, does not go after the one?',
  },
  {
    id: 30, stage: 'MID', topic: 'institution_vs_gospel',
    questionText: "Is it the people — or the institution — that hurt you? Or has the doubt gone deeper, into the actual beliefs?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "Mostly the people — the institution failed me, not the gospel.",
        value: 'people',
        traitSignals: { honest_inquiry: 0.25, sincerity: 0.2 },
      },
      {
        text: "The institution itself — how it operated.",
        value: 'institution',
        traitSignals: { honest_inquiry: 0.3, courage: 0.25 },
      },
      {
        text: "It's gone deeper — I've started doubting what I believed.",
        value: 'doctrine',
        signals: ['doubting_doctrine'],
        traitSignals: { honest_inquiry: 0.35, courage: 0.3, humility: 0.2 },
      },
      {
        text: "All of it — it collapsed together.",
        value: 'all',
        traitSignals: { honest_inquiry: 0.3, courage: 0.35, humility: 0.15 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['hurt_by_church'],
    jesusReference: "John 6:67-68 — Will you also go away? To whom shall we go? You have words of eternal life.",
  },
  {
    id: 31, stage: 'MID', topic: 'skeptic_honest',
    questionText: "What would have to be true for you to take the idea of God seriously — even just as a question worth asking?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { honest_inquiry: 0.35, courage: 0.25, openness: 0.2 },
    prerequisiteSignals: ['skeptical_of_god'],
    jesusReference: 'Acts 17:23 — I even found an altar with the inscription: TO AN UNKNOWN GOD. Paul started where they were.',
  },
  {
    id: 32, stage: 'MID', topic: 'believer_depth',
    questionText: "If Jesus is who you believe he is — is there a part of what he taught that you've found hard to actually live?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { honest_inquiry: 0.3, courage: 0.35, humility: 0.3 },
    prerequisiteSignals: ['believes_in_jesus'],
    jesusReference: 'John 6:60 — This is a hard teaching. Who can accept it?',
  },
  {
    id: 33, stage: 'MID', topic: 'loneliness_depth',
    questionText: "That loneliness you carry — when does it hit the hardest? Is there a specific moment of the day or week when it's loudest?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { courage: 0.35, sincerity: 0.35, hunger: 0.25 },
    prerequisiteSignals: ['lonely'],
    jesusReference: 'Matthew 26:40 — Could you not keep watch with me for one hour?',
  },
  {
    id: 34, stage: 'MID', topic: 'grief_and_god',
    questionText: "Did losing them — or losing that — change the way you think about God? Or was it God you were already angry at?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "Yes — it shook my faith or turned me away.",
        value: 'shook_faith',
        signals: ['hurt_by_faith'],
        traitSignals: { honest_inquiry: 0.3, courage: 0.3, sincerity: 0.2 },
      },
      {
        text: "It actually drew me closer — pain sent me looking.",
        value: 'drew_closer',
        signals: ['open_to_god', 'had_spiritual_experience'],
        traitSignals: { openness: 0.3, hunger: 0.25, sincerity: 0.2 },
      },
      {
        text: "I don't connect the two — loss is just loss.",
        value: 'separate',
        traitSignals: { honest_inquiry: 0.25 },
      },
      {
        text: "I'm honestly still working through it.",
        value: 'working_through',
        traitSignals: { courage: 0.3, sincerity: 0.3, humility: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['carries_grief'],
    jesusReference: 'John 11:33 — When Jesus saw her weeping, he was deeply moved in spirit and troubled.',
  },
  {
    id: 35, stage: 'MID', topic: 'habit_root',
    questionText: "If you could be totally honest — what need is that habit actually filling? What's it doing for you that nothing else does?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { honest_inquiry: 0.4, courage: 0.35, humility: 0.3 },
    prerequisiteSignals: ['struggles_with_habits'],
    jesusReference: 'John 4:13 — Everyone who drinks this water will be thirsty again.',
  },
  {
    id: 36, stage: 'MID', topic: 'family_faith_gap',
    questionText: "Is the gap between you and your family's faith a source of pain — or something that feels like freedom?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "Pain — there's a distance it's created that I don't love.",
        value: 'pain',
        traitSignals: { sincerity: 0.3, courage: 0.25, hunger: 0.2 },
      },
      {
        text: "Freedom — I feel more honest now than I did.",
        value: 'freedom',
        traitSignals: { honest_inquiry: 0.3, courage: 0.3 },
      },
      {
        text: "Both — it's complicated.",
        value: 'both',
        traitSignals: { honest_inquiry: 0.25, sincerity: 0.25, courage: 0.2 },
      },
      {
        text: "I've found a middle ground that works.",
        value: 'middle_ground',
        traitSignals: { humility: 0.2, sincerity: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['family_faith_tension'],
    jesusReference: 'Luke 12:53 — Father against son, mother against daughter. Jesus was honest about what following him costs.',
  },
  {
    id: 37, stage: 'MID', topic: 'purpose_specific',
    questionText: "When you imagine a life that feels fully meaningful — what does it actually look like? Not the Instagram version. The real one.",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { hunger: 0.4, sincerity: 0.35, courage: 0.2 },
    prerequisiteSignals: ['searching_for_purpose'],
    jesusReference: 'John 10:10 — I came that they may have life and have it abundantly.',
  },
  {
    id: 38, stage: 'MID', topic: 'prayer_felt',
    questionText: "That time you prayed — or something close to it — did anything come back? A feeling, a thought, a quiet? Anything at all?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "Yes — something came, even if I don't know what it was.",
        value: 'yes',
        signals: ['believes_prayer_works', 'had_spiritual_experience'],
        traitSignals: { openness: 0.35, hunger: 0.3, sincerity: 0.25 },
      },
      {
        text: "Nothing I could identify — it felt like talking to the ceiling.",
        value: 'nothing',
        traitSignals: { honest_inquiry: 0.3, humility: 0.2 },
      },
      {
        text: "I didn't stay long enough to notice.",
        value: 'left_early',
        traitSignals: { honest_inquiry: 0.2, hunger: 0.15 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['prayed_before'],
    jesusReference: 'Matthew 6:6 — When you pray, go into your room and shut the door. Pray to your Father who is in secret.',
  },
  {
    id: 39, stage: 'MID', topic: 'prayer_willingness',
    questionText: "Would you be willing to try something? Tonight — or whenever it feels right — just sit quietly and say whatever's actually on your mind, like you're talking to someone who already knows everything about you.",
    answerType: 'YES_NO',
    answerOptions: [
      {
        text: "Yes — I think I could try that.",
        value: 'yes',
        signals: ['open_to_god'],
        traitSignals: { openness: 0.35, hunger: 0.25, courage: 0.2 },
      },
      {
        text: "I'm not sure — it would feel strange.",
        value: 'unsure',
        traitSignals: { honest_inquiry: 0.2, openness: 0.15 },
      },
      {
        text: "No — I don't think that's for me.",
        value: 'no',
        traitSignals: { honest_inquiry: 0.3 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['prayed_before'],
    jesusReference: 'Luke 18:1 — He told them a parable about the need to always pray and not give up.',
  },
  {
    id: 40, stage: 'MID', topic: 'jesus_teaching_that_hit',
    questionText: "Of everything Jesus is recorded as teaching — the Sermon on the Mount, the parables, 'love your enemies' — which one sits with you, even if you're not sure what to do with it?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { hunger: 0.3, openness: 0.25, honest_inquiry: 0.2 },
    prerequisiteSignals: ['open_to_scripture'],
    jesusReference: 'Matthew 7:28 — When Jesus had finished these words, the crowds were amazed at his teaching.',
  },
  {
    id: 41, stage: 'MID', topic: 'resurrection_honest',
    questionText: "The resurrection — that Jesus literally rose from the dead — what do you do with that claim? Ignore it, dismiss it, or has it ever made you think?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "It's made me think — I can't fully dismiss it.",
        value: 'think',
        signals: ['drawn_to_jesus', 'open_to_scripture'],
        traitSignals: { honest_inquiry: 0.35, hunger: 0.3, openness: 0.25 },
      },
      {
        text: "I believe it — it's the center of everything.",
        value: 'believe',
        signals: ['believes_in_jesus'],
        traitSignals: { sincerity: 0.35, hunger: 0.25, courage: 0.2 },
      },
      {
        text: "I find it the hardest part of Christianity to accept.",
        value: 'hard',
        signals: ['skeptical_of_jesus'],
        traitSignals: { honest_inquiry: 0.3, courage: 0.25 },
      },
      {
        text: "I set it aside and focus on his teachings.",
        value: 'set_aside',
        traitSignals: { honest_inquiry: 0.25, openness: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['open_to_scripture'],
    jesusReference: '1 Corinthians 15:17 — If Christ has not been raised, your faith is futile.',
  },
  {
    id: 42, stage: 'MID', topic: 'god_still_speaks',
    questionText: "Do you think God spoke to prophets and apostles in the ancient world — and if he did, is there any reason he would have stopped?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "No — I don't think God speaks directly to people.",
        value: 'no',
        traitSignals: { honest_inquiry: 0.3 },
      },
      {
        text: "Maybe — I haven't thought about why he would stop.",
        value: 'maybe',
        signals: ['open_to_restoration'],
        traitSignals: { honest_inquiry: 0.3, openness: 0.25, hunger: 0.2 },
      },
      {
        text: "Yes — I think God still speaks and that matters.",
        value: 'yes',
        signals: ['open_to_restoration', 'open_to_god'],
        traitSignals: { openness: 0.35, hunger: 0.3, sincerity: 0.2 },
      },
      {
        text: "The question itself is interesting — I want to think about it.",
        value: 'curious',
        signals: ['open_to_restoration'],
        traitSignals: { honest_inquiry: 0.35, openness: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['open_to_god'],
    jesusReference: 'Amos 3:7 — Surely the Lord does nothing without revealing his secret to his servants the prophets.',
  },
  {
    id: 43, stage: 'MID', topic: 'restoration_what_if',
    questionText: "What if the original church Jesus established — with apostles, revelation, and priesthood authority — had been restored in our time? What would you want to know about that?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { hunger: 0.35, honest_inquiry: 0.3, openness: 0.25 },
    prerequisiteSignals: ['open_to_restoration'],
    jesusReference: 'Acts 3:21 — Heaven must receive him until the time of the restoration of all things.',
  },
  {
    id: 44, stage: 'MID', topic: 'member_step_back',
    questionText: "What was the thing — or the moment — that made you start stepping back?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { honest_inquiry: 0.35, courage: 0.35, sincerity: 0.3 },
    prerequisiteSignals: ['inactive_member'],
    jesusReference: "Luke 15:17 — When he came to himself, he said: How many of my father's hired servants have more than enough bread?",
  },
  {
    id: 45, stage: 'MID', topic: 'member_what_remains',
    questionText: "Even with the distance, is there anything from your faith you've kept holding onto — maybe quietly?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { sincerity: 0.35, hunger: 0.25, courage: 0.2 },
    prerequisiteSignals: ['inactive_member'],
    jesusReference: 'Revelation 2:4 — You have abandoned the love you had at first. But I remember it.',
  },
  {
    id: 46, stage: 'MID', topic: 'member_missing',
    questionText: "Is there anything you miss about being an active member — even if you don't say it out loud?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "The community — the people who knew me.",
        value: 'community',
        traitSignals: { sincerity: 0.25, compassion: 0.2, hunger: 0.15 },
      },
      {
        text: "The certainty — I miss knowing what I believed.",
        value: 'certainty',
        traitSignals: { sincerity: 0.3, hunger: 0.25 },
      },
      {
        text: "The ordinances or worship — something felt real then.",
        value: 'ordinances',
        traitSignals: { sincerity: 0.3, hunger: 0.3, openness: 0.2 },
      },
      {
        text: "Honestly — not much. I feel freer now.",
        value: 'nothing',
        traitSignals: { honest_inquiry: 0.25, courage: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['inactive_member'],
    jesusReference: 'Luke 15:20 — But while he was still a long way off, his father saw him and was filled with compassion.',
  },
  {
    id: 47, stage: 'MID', topic: 'losing_faith_reason',
    questionText: "Something is pulling you away from the faith you grew up in — can you name what it is? A doubt, a hurt, a question that hasn't been answered?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "A historical or doctrinal question I can't resolve.",
        value: 'intellectual',
        signals: ['intellectual_doubts'],
        traitSignals: { honest_inquiry: 0.4, courage: 0.3 },
      },
      {
        text: "Someone in the church hurt me or failed me.",
        value: 'person',
        signals: ['hurt_by_church'],
        traitSignals: { courage: 0.3, sincerity: 0.3 },
      },
      {
        text: "My life changed in ways the church didn't make room for.",
        value: 'life_change',
        traitSignals: { honest_inquiry: 0.3, courage: 0.3, sincerity: 0.2 },
      },
      {
        text: "I've drifted — there's no single thing, just distance.",
        value: 'drift',
        traitSignals: { honest_inquiry: 0.25, humility: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['losing_faith'],
    jesusReference: 'Luke 22:32 — I have prayed for you that your faith may not fail. And when you have returned, strengthen your brothers.',
  },
  {
    id: 48, stage: 'MID', topic: 'intellectual_doubt_space',
    questionText: "What's the specific question or historical issue that's hardest for you? You don't have to protect anyone's feelings here.",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { honest_inquiry: 0.4, courage: 0.35, humility: 0.2 },
    prerequisiteSignals: ['intellectual_doubts'],
    jesusReference: 'John 20:27 — Put your finger here; see my hands. Stop doubting and believe.',
  },

  // ══════════════════════════════════════════
  // DEEP — Earned by genuine engagement.
  // ══════════════════════════════════════════

  {
    id: 49, stage: 'DEEP', topic: 'who_is_jesus',
    questionText: "Jesus said 'I am the way, the truth, and the life.' Of those three — way, truth, life — which one do you most need from him right now?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "The way — I don't know what direction to go.",
        value: 'way',
        traitSignals: { hunger: 0.3, humility: 0.25, openness: 0.2 },
      },
      {
        text: "The truth — I have too many unanswered questions.",
        value: 'truth',
        traitSignals: { honest_inquiry: 0.35, hunger: 0.25, courage: 0.2 },
      },
      {
        text: "The life — I'm tired of just going through the motions.",
        value: 'life',
        traitSignals: { hunger: 0.35, sincerity: 0.3, courage: 0.2 },
      },
      {
        text: "Honestly, all three.",
        value: 'all',
        traitSignals: { hunger: 0.3, sincerity: 0.25, humility: 0.2, openness: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['drawn_to_jesus'],
    jesusReference: 'John 14:6 — I am the way, the truth, and the life.',
  },
  {
    id: 50, stage: 'DEEP', topic: 'book_of_mormon_curiosity',
    questionText: "There's a book of scripture called the Book of Mormon — a second witness for Jesus Christ, claimed to be ancient but translated in the 1800s. Does that interest you, bother you, or make you want to know more?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "It interests me — I'd want to know the evidence for it.",
        value: 'interested',
        signals: ['curious_about_book_of_mormon'],
        traitSignals: { honest_inquiry: 0.35, hunger: 0.3, openness: 0.25 },
      },
      {
        text: "It makes me skeptical — that's a big claim.",
        value: 'skeptical',
        traitSignals: { honest_inquiry: 0.35, courage: 0.2 },
      },
      {
        text: "I've heard of it but never taken it seriously.",
        value: 'heard_not_serious',
        traitSignals: { honest_inquiry: 0.2, openness: 0.15 },
      },
      {
        text: "I'm open — what makes it credible?",
        value: 'open',
        signals: ['curious_about_book_of_mormon'],
        traitSignals: { openness: 0.35, hunger: 0.25, honest_inquiry: 0.3 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['open_to_restoration'],
    jesusReference: 'John 10:16 — I have other sheep that are not of this sheep pen. I must bring them also.',
  },
  {
    id: 51, stage: 'DEEP', topic: 'joseph_smith_question',
    questionText: "The restoration of the gospel — if it happened — started with a young man who said God spoke to him directly. Does that kind of claim make you more curious, or more skeptical?",
    answerType: 'CHOICE',
    answerOptions: [
      {
        text: "More curious — I want to understand the evidence.",
        value: 'curious',
        traitSignals: { honest_inquiry: 0.4, hunger: 0.3, openness: 0.3 },
      },
      {
        text: "More skeptical — people claim divine experiences all the time.",
        value: 'skeptical',
        traitSignals: { honest_inquiry: 0.35, courage: 0.2 },
      },
      {
        text: "Both — I'm interested but I'd want to test it.",
        value: 'both',
        traitSignals: { honest_inquiry: 0.35, openness: 0.25, courage: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['curious_about_book_of_mormon'],
    jesusReference: 'Matthew 7:20 — By their fruits you will know them.',
  },
  {
    id: 52, stage: 'DEEP', topic: 'restoration_invitation',
    questionText: "If you could find out — really find out — whether the Book of Mormon is true or not, would you want to know? Even if the answer changed what you do next?",
    answerType: 'YES_NO',
    answerOptions: [
      {
        text: "Yes — I'd want to know the truth even if it cost me something.",
        value: 'yes',
        traitSignals: { courage: 0.4, hunger: 0.35, sincerity: 0.3, honest_inquiry: 0.25 },
      },
      {
        text: "I'm not sure I'm ready for that.",
        value: 'not_ready',
        traitSignals: { honest_inquiry: 0.2, humility: 0.15 },
      },
      {
        text: "No — I'm comfortable where I am.",
        value: 'no',
        traitSignals: { honest_inquiry: 0.25 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['curious_about_book_of_mormon'],
    jesusReference: 'Moroni 10:4 — Ask God, the Eternal Father, in the name of Christ, if these things are true.',
  },
  {
    id: 53, stage: 'DEEP', topic: 'member_return_question',
    questionText: "If someone could give you a real answer to the thing that's bothering you — not just 'have more faith' — would you be open to coming back?",
    answerType: 'YES_NO',
    answerOptions: [
      {
        text: "Yes — if the answers were real, I'd want to.",
        value: 'yes',
        traitSignals: { hunger: 0.35, sincerity: 0.3, openness: 0.25, courage: 0.2 },
      },
      {
        text: "I honestly don't know — it's not just intellectual for me.",
        value: 'unsure',
        traitSignals: { honest_inquiry: 0.3, sincerity: 0.25, humility: 0.2 },
      },
      {
        text: "No — I've moved past that point.",
        value: 'no',
        traitSignals: { honest_inquiry: 0.25, courage: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: ['inactive_member'],
    jesusReference: 'John 21:22 — What is that to you? You follow me.',
  },
  {
    id: 54, stage: 'DEEP', topic: 'seeking_honest',
    questionText: "Something in you kept coming back here. What are you actually looking for?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { courage: 0.4, sincerity: 0.4, hunger: 0.3 },
    prerequisiteSignals: [],
    jesusReference: 'John 1:38 — What are you seeking? The first and last question.',
  },
  {
    id: 55, stage: 'DEEP', topic: 'one_question',
    questionText: "If you could ask God one question right now — knowing he would actually answer — what would you ask?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { hunger: 0.4, courage: 0.3, sincerity: 0.3 },
    prerequisiteSignals: [],
    jesusReference: 'Matthew 7:7 — Ask, and it will be given to you. Seek, and you will find.',
  },
  {
    id: 56, stage: 'DEEP', topic: 'cost',
    questionText: "If everything you've been reading here turned out to be true — what would change for you? Be honest.",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { courage: 0.45, sincerity: 0.4, humility: 0.3 },
    prerequisiteSignals: [],
    jesusReference: 'Luke 9:23 — If anyone would come after me, let him deny himself and take up his cross daily.',
  },
  {
    id: 57, stage: 'DEEP', topic: 'next_step',
    questionText: "Is there something you already know you should do — even one small thing — that you've been putting off?",
    answerType: 'FREE_TEXT',
    answerOptions: [],
    traitSignals: { courage: 0.4, humility: 0.35, sincerity: 0.3 },
    prerequisiteSignals: [],
    jesusReference: 'John 5:6 — Do you want to be healed? Jesus asked before he acted.',
  },
  {
    id: 58, stage: 'DEEP', topic: 'ready_to_know',
    questionText: "Some people spend their whole life curious about God and never actually ask him directly. Are you willing to try that — to sincerely ask and wait for an answer?",
    answerType: 'YES_NO',
    answerOptions: [
      {
        text: "Yes — I'm willing to actually try.",
        value: 'yes',
        traitSignals: { courage: 0.45, hunger: 0.4, openness: 0.3, sincerity: 0.3 },
      },
      {
        text: "I want to be — I'm just not there yet.",
        value: 'not_yet',
        traitSignals: { honest_inquiry: 0.25, hunger: 0.2, humility: 0.2 },
      },
      {
        text: "No — I don't think I'll get anything back.",
        value: 'no',
        traitSignals: { honest_inquiry: 0.35, courage: 0.2 },
      },
    ],
    traitSignals: {},
    prerequisiteSignals: [],
    jesusReference: "James 1:5 — If any of you lacks wisdom, let him ask God, who gives generously to all without reproach.",
  },

  // ══════════════════════════════════════════
  // TARGETED MINISTRY ADDITIONS (ported verbatim from the verified reference,
  // mbm-data.js — 0 law violations across 270+ engine-sim trials).
  // ══════════════════════════════════════════

  // id 0 — the confirming question for people whose story tap hinted at faith.
  // Asked FIRST for them. Names no church: the app learns where their faith lives
  // without ever disclosing anything itself (Law 8: one click is never identity).
  {
    id: 0, stage: 'ENTRY', topic: 'faith_home',
    questionText: 'It sounds like faith is already part of your life. Where does that faith live right now?',
    answerType: 'CHOICE',
    answerOptions: [
      { text: "In a church family I'm an active part of.", value: 'churched', signals: ['believes_in_jesus'], traitSignals: { sincerity: 0.25, openness: 0.15 } },
      { text: 'In a faith I grew up in but have drifted from.', value: 'drifted', signals: ['has_history_with_faith'], traitSignals: { honest_inquiry: 0.25, courage: 0.2 } },
      { text: 'Between me and God — no church right now.', value: 'unchurched', signals: ['open_to_god'], traitSignals: { sincerity: 0.2, openness: 0.2 } },
      { text: "Honestly — it's complicated right now.", value: 'complicated', traitSignals: { honest_inquiry: 0.25, humility: 0.2 } },
    ],
    traitSignals: {}, prerequisiteSignals: ['covenant_intent'],
    jesusReference: 'John 4:21-23 — Neither on this mountain nor in Jerusalem… true worshipers worship in spirit and in truth.',
  },
  // id 2.5 — faith tradition. A modern disciple ASKS, openly and warmly, where
  // someone's faith lives (Acts 17). Third question for everyone. Names no church.
  {
    id: 2.5, stage: 'ENTRY', topic: 'faith_tradition',
    questionText: "Do you have a faith tradition today — a church, a practice, something you grew up in or chose? However you'd describe it.",
    answerType: 'CHOICE',
    answerOptions: [
      { text: "Yes — I'm part of a faith community now.", value: 'active', signals: ['active_faith_tradition'], traitSignals: { sincerity: 0.2, openness: 0.15 } },
      { text: "I grew up in one, but I've stepped away.", value: 'stepped_away', signals: ['has_history_with_faith'], traitSignals: { honest_inquiry: 0.25, courage: 0.2 } },
      { text: "No — I've never really had one.", value: 'none', traitSignals: { honest_inquiry: 0.2 } },
      { text: "It's complicated — bits and pieces.", value: 'complicated', traitSignals: { humility: 0.2, honest_inquiry: 0.2 } },
    ],
    traitSignals: {}, prerequisiteSignals: [],
    jesusReference: 'Acts 17:22-23 — I see that in every way you are very religious… Paul began with what they already worshiped.',
  },
  // id 61 — picture of God: what God thinks of you.
  {
    id: 61, stage: 'ENTRY', topic: 'gods_opinion_of_you',
    questionText: 'If God is real — what do you suspect he actually thinks of you, right now, today?',
    answerType: 'CHOICE',
    answerOptions: [
      { text: "That I'm a disappointment to him.", value: 'disappointment', signals: ['pictures_harsh_god'], traitSignals: { courage: 0.3, sincerity: 0.3 } },
      { text: "That he's not really paying attention to someone like me.", value: 'unnoticed', signals: ['pictures_distant_god'], traitSignals: { sincerity: 0.25, honest_inquiry: 0.2 } },
      { text: "That he loves me — even the parts I hide.", value: 'loved', signals: ['believes_god_good'], traitSignals: { sincerity: 0.3, openness: 0.25, courage: 0.2 } },
      { text: "Honestly — I think he might be glad I'm asking.", value: 'glad', signals: ['open_to_god'], traitSignals: { openness: 0.3, hunger: 0.25 } },
      { text: "I can't picture him being real enough to think anything.", value: 'unreal', signals: ['skeptical_of_god'], traitSignals: { honest_inquiry: 0.3, courage: 0.2 } },
    ],
    traitSignals: {}, prerequisiteSignals: [],
    jesusReference: 'Luke 15:20 — While he was still a long way off, his father saw him and was filled with compassion.',
  },
  // id 62 — the God you reject (picture-of-God probe for skeptics).
  {
    id: 62, stage: 'EARLY', topic: 'god_you_reject',
    questionText: "Describe the God you don't believe in. What is he like — the one you walked away from or never could accept?",
    answerType: 'FREE_TEXT', answerOptions: [],
    traitSignals: { honest_inquiry: 0.4, courage: 0.3, sincerity: 0.25 }, prerequisiteSignals: ['skeptical_of_god'],
    jesusReference: 'John 8:19 — You know neither me nor my Father. If you knew me, you would know my Father also.',
  },
  // id 63 — Jesus in your life.
  {
    id: 63, stage: 'MID', topic: 'jesus_in_your_life',
    questionText: 'If you could watch Jesus walk into one situation from your own life — which one would you pick, and what are you afraid he would do?',
    answerType: 'FREE_TEXT', answerOptions: [],
    traitSignals: { courage: 0.35, sincerity: 0.35, hunger: 0.25 }, prerequisiteSignals: [],
    jesusReference: 'John 11:21 — Lord, if you had been here, my brother would not have died. She told him exactly where it hurt.',
  },
  // id 64 — score-keeper vs leaning-in (picture-of-God probe).
  {
    id: 64, stage: 'EARLY', topic: 'who_listens',
    questionText: 'When you pray — or imagine praying — who do you picture listening: someone keeping score, or someone leaning in?',
    answerType: 'CHOICE',
    answerOptions: [
      { text: 'Someone keeping score.', value: 'score', signals: ['pictures_harsh_god'], traitSignals: { courage: 0.25, sincerity: 0.25 } },
      { text: 'Someone leaning in.', value: 'leaning', signals: ['believes_god_good'], traitSignals: { openness: 0.3, sincerity: 0.25 } },
      { text: 'No one. Empty air.', value: 'no_one', signals: ['skeptical_of_god'], traitSignals: { honest_inquiry: 0.3 } },
      { text: 'It depends on the day, honestly.', value: 'depends', traitSignals: { sincerity: 0.25, humility: 0.2 } },
    ],
    traitSignals: {}, prerequisiteSignals: [],
    jesusReference: 'Luke 11:13 — How much more will your Father in heaven give good gifts to those who ask him.',
  },
  // id 66 — faith home named. Their own words → harvested. Where an LDS member
  // self-identifies (Law 3) and a Baptist gets believes_in_jesus.
  {
    id: 66, stage: 'EARLY', topic: 'faith_home_named',
    questionText: "Which church or tradition is home for you — and what's one thing about it you'd never want to lose?",
    answerType: 'FREE_TEXT', answerOptions: [],
    traitSignals: { sincerity: 0.3, openness: 0.2 }, prerequisiteSignals: ['active_faith_tradition'],
    jesusReference: 'Mark 12:34 — You are not far from the kingdom of God. Said to a teacher from another school.',
  },
  // id 67 — one true thing (testimony-eliciting).
  {
    id: 67, stage: 'EARLY', topic: 'one_true_thing',
    questionText: "If you had to tell a child one true thing about God — even if you're not sure you fully believe it yourself — what would you say?",
    answerType: 'FREE_TEXT', answerOptions: [],
    traitSignals: { sincerity: 0.3, courage: 0.2, hunger: 0.2 }, prerequisiteSignals: [],
    jesusReference: 'Matthew 18:3 — Unless you change and become like little children…',
  },
  // id 68 — what you know (testimony-eliciting).
  {
    id: 68, stage: 'MID', topic: 'what_you_know',
    questionText: 'What do you actually KNOW — not hope, not something borrowed from someone else — from your own life, about God or about goodness?',
    answerType: 'FREE_TEXT', answerOptions: [],
    traitSignals: { sincerity: 0.35, courage: 0.3, honest_inquiry: 0.2 }, prerequisiteSignals: [],
    jesusReference: 'John 9:25 — One thing I do know: I was blind, and now I see.',
  },
  // id 69 — tell it as story (testimony-eliciting).
  {
    id: 69, stage: 'MID', topic: 'tell_it_as_story',
    questionText: 'That experience you mentioned — the one you could not explain — tell it like a story. What happened, and what did it leave behind in you?',
    answerType: 'FREE_TEXT', answerOptions: [],
    traitSignals: { openness: 0.3, sincerity: 0.3, hunger: 0.25 }, prerequisiteSignals: ['had_spiritual_experience'],
    jesusReference: 'Mark 5:19 — Go home to your own people and tell them how much the Lord has done for you.',
  },
  // id 70 — faith history named (framework probe). Their words → faithWords.
  {
    id: 70, stage: 'EARLY', topic: 'faith_history_named',
    questionText: "The faith you've been around or stepped away from — which church or tradition was it, and what did it teach you about who God is?",
    answerType: 'FREE_TEXT', answerOptions: [],
    traitSignals: { honest_inquiry: 0.3, courage: 0.25, sincerity: 0.2 }, prerequisiteSignals: ['has_history_with_faith'],
    jesusReference: 'Luke 24:17 — What are you discussing as you walk along? He asked what they already carried.',
  },
  // id 71 — does everyone get a real chance (the Calvinist-revealing question).
  {
    id: 71, stage: 'EARLY', topic: 'who_gets_a_chance',
    questionText: "Here's a question people rarely get asked plainly: do you believe everyone gets a real chance with God — or only some?",
    answerType: 'CHOICE',
    answerOptions: [
      { text: 'Everyone — somehow, a good God reaches everyone.', value: 'everyone', signals: ['rejects_harsh_god'], traitSignals: { openness: 0.3, compassion: 0.25 } },
      { text: "Only some — that's what I was taught, and it troubles me.", value: 'troubled', signals: ['pictures_harsh_god'], traitSignals: { courage: 0.3, sincerity: 0.25, honest_inquiry: 0.2 } },
      { text: "Only some — and I've made peace with that.", value: 'settled', signals: ['pictures_harsh_god', 'reformed_framework'], traitSignals: { sincerity: 0.2 } },
      { text: "I've honestly never let myself ask.", value: 'never_asked', traitSignals: { humility: 0.25, honest_inquiry: 0.2 } },
    ],
    traitSignals: {}, prerequisiteSignals: [],
    jesusReference: '1 Timothy 2:4 — God our Savior, who will have all men to be saved, and to come unto the knowledge of the truth.',
  },
  // id 72 — universal chance (1 Pet 4:6-shaped; gated on pictures_harsh_god).
  {
    id: 72, stage: 'MID', topic: 'universal_chance',
    questionText: 'If it turned out that every soul — living and dead — gets a full, fair chance to know God, would that be better news than what you were taught — or would it break something you need to keep?',
    answerType: 'CHOICE',
    answerOptions: [
      { text: "Better news. I'd want that to be true.", value: 'better', signals: ['rejects_harsh_god', 'open_to_god'], traitSignals: { hunger: 0.3, openness: 0.3 } },
      { text: 'It would contradict what God has decreed.', value: 'decreed', signals: ['reformed_framework'], traitSignals: { sincerity: 0.2 } },
      { text: "I don't know — I've never been allowed to ask that.", value: 'not_allowed', traitSignals: { courage: 0.25, honest_inquiry: 0.25 } },
    ],
    traitSignals: {}, prerequisiteSignals: ['pictures_harsh_god'],
    jesusReference: '1 Peter 4:6 — For this cause was the gospel preached also to them that are dead.',
  },
];

// TARGETED MINISTRY (owner direction, 2026-06-11): ask next what the app most
// needs to learn to lead this person where it is designed to take them.
// Background → picture of God → God still speaks → the reach. Each answer moves
// the person one honest step along the path, never at random. Ported verbatim
// from the verified reference (mbm-data.js).
export function computeNextQuestion(
  answeredIds:   number[],
  signals:       string[],
  openedCount:   number,
): DialogueQuestion | null {
  const activeSignals = new Set(signals);
  if (openedCount >= 1) activeSignals.add('viewed_content');

  // THE MILK-BEFORE-MEAT LAW, applied to the question bank. These are the only
  // questions that NAME the restored gospel — the restored church, the Book of
  // Mormon, Joseph Smith. They are MEAT, and they must never be asked until the
  // person has shown BOTH witnesses on their own: they believe God is good AND
  // they are open to God still speaking. A self-labeled Calvinist who merely
  // tripped 'open_to_restoration' (but whose framework still pictures a harsh
  // God) must NEVER be handed the Book of Mormon — that puts them on guard
  // before they have been won to the good God. mayReferenceLds() is the exact
  // same two-witness gate the chat uses, and it is false for members too.
  const RESTORATION_TIER = new Set([
    'restoration_what_if', 'book_of_mormon_curiosity',
    'joseph_smith_question', 'restoration_invitation',
  ]);
  const meatOk = mayReferenceLds(signals);
  const member = isMember(signals);

  // Questions that only make sense for a SEEKER deciding what they believe. A
  // member already settled these — asking them is theatrics, not ministry — so
  // members never see them even when nothing higher-priority is eligible.
  const SEEKER_ONLY = new Set(['god_still_speaks']);

  const eligible = QUESTION_BANK.filter(q =>
    !answeredIds.includes(q.id) &&
    (q.prerequisiteSignals.length === 0 ||
      q.prerequisiteSignals.every(s => activeSignals.has(s))) &&
    (!RESTORATION_TIER.has(q.topic) || meatOk) &&
    (!member || !SEEKER_ONLY.has(q.topic)),
  );

  if (eligible.length === 0) return null;
  const knowsBackground =
    answeredIds.includes(0) || answeredIds.includes(2.5) ||
    ['active_faith_tradition', 'has_history_with_faith', 'active_member', 'inactive_member'].some(x => activeSignals.has(x));
  const godGood = believesGodGood(signals);
  const openMore = openToMore(signals);
  // A member already holds the restored gospel. They did not come to be quizzed
  // on whether God still speaks or whether the Book of Mormon is true — that is
  // theatrics to them. They came to be fed. Lead them to the deepening, testimony
  // and discipleship questions, never the seeker-restoration ladder.
  const PRIORITY_TOPICS = member
    ? ['believer_depth', 'jesus_in_your_life', 'jesus_teaching_that_hit', 'scripture_openness', 'forgiveness', 'what_you_know', 'one_true_thing', 'jesus_feeling']
    : !knowsBackground
      ? ['faith_home', 'faith_tradition']
      : !godGood
        ? ['gods_opinion_of_you', 'who_listens', 'god_feeling', 'god_you_reject', 'who_gets_a_chance', 'universal_chance', 'faith_history_named', 'one_true_thing', 'what_you_know', 'grief_and_god']
        : !openMore
          ? ['god_still_speaks', 'unseen', 'spiritual_experience_depth', 'prayer', 'prayer_felt']
          : ['book_of_mormon_curiosity', 'restoration_what_if', 'seeking_honest', 'one_question', 'tell_it_as_story'];
  const prioritized = eligible.filter(q => PRIORITY_TOPICS.includes(q.topic));
  const pool = prioritized.length > 0 ? prioritized : eligible;

  pool.sort((a, b) => {
    const stageDiff = (STAGE_ORDER[a.stage] ?? 1) - (STAGE_ORDER[b.stage] ?? 1);
    return stageDiff !== 0 ? stageDiff : a.id - b.id;
  });

  return pool[0];
}
