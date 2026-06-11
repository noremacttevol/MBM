import sqlite3
import os
import json
from content.seed_data import SEED_CONTENT
from content.question_bank import QUESTION_BANK

DB_PATH = os.path.join(os.path.dirname(__file__), "mbm.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS content (
    id                      INTEGER PRIMARY KEY AUTOINCREMENT,
    tag                     TEXT NOT NULL,
    content_type            TEXT DEFAULT 'link',
    title                   TEXT NOT NULL,
    description             TEXT,
    scripture_ref           TEXT,
    media_type              TEXT,
    resonance_style         TEXT,
    url                     TEXT,
    active                  INTEGER DEFAULT 1,
    upvote_count            INTEGER DEFAULT 0,
    downvote_count          INTEGER DEFAULT 0,
    view_count              INTEGER DEFAULT 0,
    sequence_group          TEXT,
    sequence_order          INTEGER DEFAULT 0,
    estimated_read_minutes  INTEGER DEFAULT 3
);

CREATE TABLE IF NOT EXISTS user_session (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id          TEXT UNIQUE NOT NULL,
    profile             TEXT,
    feed_tag            TEXT,
    resonance_weights   TEXT DEFAULT '{}',
    seen_content        TEXT DEFAULT '[]',
    bookmarked_content  TEXT DEFAULT '[]',
    interaction_count   INTEGER DEFAULT 0,
    onboarding_text     TEXT,
    transparency_shown  INTEGER DEFAULT 0,
    invitation_shown    INTEGER DEFAULT 0,
    created_at          DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_seen           DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS interaction_log (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id      TEXT NOT NULL,
    content_id      INTEGER,
    action          TEXT,
    dwell_seconds   INTEGER DEFAULT 0,
    reflect_text    TEXT,
    logged_at       DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (content_id) REFERENCES content(id)
);

CREATE TABLE IF NOT EXISTS user_question (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id      TEXT NOT NULL,
    question_text   TEXT NOT NULL,
    feed_tag        TEXT,
    asked_at        DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS connection_request (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id  TEXT NOT NULL,
    name        TEXT,
    contact     TEXT,
    message     TEXT,
    feed_tag    TEXT,
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ai_response (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id     INTEGER,
    session_id      TEXT NOT NULL,
    question_text   TEXT NOT NULL,
    feed_tag        TEXT,
    response_text   TEXT NOT NULL,
    is_certain      INTEGER DEFAULT 1,
    context_ids     TEXT DEFAULT '[]',
    human_status    TEXT DEFAULT 'pending',
    human_note      TEXT,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS dialogue_question (
    id                   INTEGER PRIMARY KEY AUTOINCREMENT,
    track                TEXT NOT NULL,
    stage                TEXT DEFAULT 'EARLY',
    topic                TEXT,
    question_text        TEXT NOT NULL,
    answer_type          TEXT DEFAULT 'CHOICE',
    answer_options       TEXT DEFAULT '[]',
    scale_low            TEXT DEFAULT '',
    scale_high           TEXT DEFAULT '',
    trait_signals        TEXT DEFAULT '{}',
    prerequisite_signals TEXT DEFAULT '[]',
    jesus_reference      TEXT,
    active               INTEGER DEFAULT 1,
    created_at           DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_dialogue_response (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id      TEXT NOT NULL,
    question_id     INTEGER NOT NULL,
    answer_value    TEXT,
    answer_text     TEXT,
    trait_deltas    TEXT DEFAULT '{}',
    responded_at    DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

MIGRATIONS = [
    "ALTER TABLE content ADD COLUMN content_type TEXT DEFAULT 'link'",
    "ALTER TABLE content ADD COLUMN upvote_count INTEGER DEFAULT 0",
    "ALTER TABLE content ADD COLUMN downvote_count INTEGER DEFAULT 0",
    "ALTER TABLE content ADD COLUMN view_count INTEGER DEFAULT 0",
    "ALTER TABLE content ADD COLUMN sequence_group TEXT",
    "ALTER TABLE content ADD COLUMN sequence_order INTEGER DEFAULT 0",
    "ALTER TABLE content ADD COLUMN estimated_read_minutes INTEGER DEFAULT 3",
    "ALTER TABLE user_session ADD COLUMN resonance_weights TEXT DEFAULT '{}'",
    "ALTER TABLE user_session ADD COLUMN seen_content TEXT DEFAULT '[]'",
    "ALTER TABLE user_session ADD COLUMN bookmarked_content TEXT DEFAULT '[]'",
    "ALTER TABLE user_session ADD COLUMN interaction_count INTEGER DEFAULT 0",
    "ALTER TABLE user_session ADD COLUMN onboarding_text TEXT",
    "ALTER TABLE user_session ADD COLUMN transparency_shown INTEGER DEFAULT 0",
    "ALTER TABLE user_session ADD COLUMN invitation_shown INTEGER DEFAULT 0",
    "ALTER TABLE interaction_log ADD COLUMN dwell_seconds INTEGER DEFAULT 0",
    "ALTER TABLE interaction_log ADD COLUMN reflect_text TEXT",
    "ALTER TABLE user_session ADD COLUMN trait_scores TEXT DEFAULT '{}'",
    "ALTER TABLE user_session ADD COLUMN question_track TEXT",
    "ALTER TABLE user_session ADD COLUMN answered_question_ids TEXT DEFAULT '[]'",
    "ALTER TABLE user_session ADD COLUMN dialogue_signals TEXT DEFAULT '[]'",
    "ALTER TABLE dialogue_question ADD COLUMN prerequisite_signals TEXT DEFAULT '[]'",
]


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)

    for migration in MIGRATIONS:
        try:
            conn.execute(migration)
            conn.commit()
        except Exception:
            pass

    existing_content = conn.execute("SELECT COUNT(*) FROM content").fetchone()[0]
    if existing_content == 0:
        conn.executemany(
            """INSERT INTO content
               (tag, content_type, title, description, scripture_ref, media_type,
                resonance_style, url, sequence_group, sequence_order, estimated_read_minutes)
               VALUES (:tag, :content_type, :title, :description, :scripture_ref, :media_type,
                :resonance_style, :url, :sequence_group, :sequence_order, :estimated_read_minutes)""",
            SEED_CONTENT,
        )
        conn.commit()

    existing_questions = conn.execute("SELECT COUNT(*) FROM dialogue_question").fetchone()[0]
    if existing_questions == 0:
        for q in QUESTION_BANK:
            conn.execute(
                """INSERT INTO dialogue_question
                   (track, stage, topic, question_text, answer_type, answer_options,
                    scale_low, scale_high, trait_signals, prerequisite_signals, jesus_reference)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (q["track"], q["stage"], q.get("topic", ""),
                 q["question_text"], q["answer_type"],
                 q["answer_options"] if isinstance(q["answer_options"], str) else json.dumps(q["answer_options"]),
                 q.get("scale_low", ""), q.get("scale_high", ""),
                 q["trait_signals"] if isinstance(q["trait_signals"], str) else json.dumps(q["trait_signals"]),
                 q.get("prerequisite_signals", "[]"),
                 q.get("jesus_reference", "")),
            )
        conn.commit()

    conn.close()


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == "__main__":
    init_db()
    print("Database ready at", DB_PATH)
