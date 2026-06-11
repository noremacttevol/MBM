# MBM — Milk Before Meat App Development
**Date:** 2026-06-05 | **Status:** PENDING APPROVAL

## Goal
Build the MVP of the MBM spiritual personalization platform per the white paper at `C:\Brain\MBM\MBM-Whitepaper.md`.

## Stack Decision (MVP — simplified to ship fast)
- **Backend:** Python + FastAPI + SQLite (no DB server needed to start — swap to PostgreSQL later)
- **Frontend:** Web app (React) — get it working in browser first, mobile later
- **ML:** None yet — rule-based tag matching first. Train model once we have real user data.
- **Location:** `C:\Brain\MBM\app\`

---

## Phase 1 — Project Setup
- [ ] Create `C:\Brain\MBM\app\` folder structure (backend + frontend dirs)
- [ ] Initialize git repo in `C:\Brain\MBM\app\`
- [ ] Create Python virtual environment, install FastAPI + SQLAlchemy + Uvicorn + SQLite
- [ ] Create React frontend with Vite (fastest setup)
- [ ] Confirm both backend and frontend boot clean

## Phase 2 — Database Layer
- [ ] Define SQLAlchemy models: users, user_embeddings, content, content_tags, events, reactions, reflections, feed_history
- [ ] Run migration to create SQLite DB and all tables
- [ ] Verify schema matches white paper spec

## Phase 3 — Backend API (FastAPI)
- [ ] `POST /users/register` — create user
- [ ] `POST /users/onboarding` — save 5 profile answers, build initial user vector
- [ ] `GET /users/{id}/profile` — return transparent profile (tags, stage, depth_readiness)
- [ ] `POST /content` — add content to library with tags
- [ ] `GET /feed/{user_id}` — rule-based recommendation feed (tag matching, depth filter)
- [ ] `POST /events` — log views, skips, reactions, reflections
- [ ] `POST /events/feedback-loop` — update user vector based on event signals

## Phase 4 — Seed Content (20 pieces to start)
- [ ] Write and tag 20 seed content pieces across all life themes and depth levels
- [ ] Cover milk (0.0–0.3) and intermediate (0.3–0.6) levels
- [ ] At least one piece per life theme (purpose, loneliness, grief, identity, forgiveness, fear, meaning, relationships)
- [ ] Load into DB via seed script

## Phase 5 — Frontend (React Web)
- [ ] Onboarding flow — 5 screens, one question each, posts to `/users/onboarding`
- [ ] Feed screen — scrollable content cards, tracks view time, reaction buttons
- [ ] Profile page — shows user's tags, journey stage, depth_readiness bar
- [ ] Wire all screens to backend API

## Phase 6 — Verify & Review
- [ ] Test full user journey: register → onboard → see feed → react → profile updates
- [ ] Confirm depth_readiness changes with engagement
- [ ] Confirm feed changes after reactions
- [ ] Add review section here

---

# DSDT Cleanup & Reorganization
**Date:** 2026-06-03 | **Status:** PENDING APPROVAL

## Issues Found
1. `DSDT/assignments/` floating at root level — belongs inside PYT-102 (code already lives there)
2. `MLS-101.../MLS-102-2_ Files_files/` — empty MLS-102 folder buried inside MLS-101 (wrong place)
3. No `MLS-102` folder at DSDT level — but MLS-102 is the active current class
4. `00-DSDT-Index.md` has no MLS-102 section

## Proposed Structure
```
DSDT/
├── 00-DSDT-Index.md
├── dsdt-scraper/
├── PYT-101-Python-Fundamentals/
├── PYT-102-Python-2/
│   └── assignments/
│       └── texas-holdem/   ← Texas-Holdem-V2-Plan.md moved here
├── MLS-101-Machine-Learning-Fundamentals/  ← MLS-102 junk folder removed
└── MLS-102-Machine-Learning-Fundamentals-I/  ← new proper folder
```

## Todos
- [x] Move `DSDT/assignments/texas-holdem/Texas-Holdem-V2-Plan.md` → `PYT-102/assignments/texas-holdem/`
- [x] Delete now-empty `DSDT/assignments/` folder
- [x] Delete `MLS-101.../MLS-102-2_ Files_files/` (empty, just noise)
- [x] Create `DSDT/MLS-102-Machine-Learning-Fundamentals-I/` with starter index
- [x] Update `00-DSDT-Index.md` to add MLS-102 section

## Review
- Texas-Holdem-V2-Plan.md moved into PYT-102/assignments/texas-holdem/ where it belongs
- Root-level DSDT/assignments/ folder deleted
- Empty MLS-102 junk folder removed from inside MLS-101
- MLS-102-Machine-Learning-Fundamentals-I/ created at DSDT level with 00-MLS-102-Index.md
- 00-DSDT-Index.md updated: MLS-101 marked Complete, MLS-102 added as Active

---

# DSDT Automation + Day 5 Notes + Assignments (COMPLETE)
**Date:** 2026-06-03 | **Status:** COMPLETE

## Part 1 — Day 5 Notes + Wiki Pages (from 0602 transcripts)
- [x] Read all 0602_Day-5 transcripts (Parts 1–9 read in session)
- [x] Write MLS-101-Day-5-Notes.md
- [x] Create Correlation-Matrix.md wiki page
- [x] Create VIF-Score.md wiki page
- [x] Create Data-Visualization.md wiki page
- [x] Create Seaborn.md wiki page
- [x] Create Heatmap.md wiki page
- [x] Create Color-Map.md wiki page
- [x] Create Color-Bar-Bounds.md wiki page

## Part 2 — Assignment Answers (DUE TONIGHT Jun 3 11:59pm)
- [x] Correlation Matrices answers
- [x] VIF Scores answers
- [x] Data Visualization answers
- [x] Introduction To Seaborn answers
- [x] Creating A Heatmap answers
- [x] Defining A Color Map answers
- [x] Setting Color Bar Bounds answers

## Part 3 — Automation System
- [x] Create .env with DSDT credentials + Claude API key placeholder
- [x] Write transcript_processor.py (auto-reads transcripts → calls Claude API → writes notes)
- [x] Write dsdt_scraper.py (Playwright → scrapes all Populi lesson pages)
- [x] Write run_transcript_processor.bat launcher
- [x] Write run_dsdt_scraper.bat launcher
- [x] Set up Windows Task Scheduler (1:30pm + 9am — BOTH TASKS REGISTERED AND READY)
- [x] Add ANTHROPIC_API_KEY to .env ✓
- [x] Test transcript_processor.py — runs clean, correctly detects Days 1,2,3,5 all caught up

## Review
All tasks complete as of 2026-06-03.
- Day 5 notes written from actual transcripts
- 7 wiki pages created (Correlation-Matrix, VIF-Score, Data-Visualization, Seaborn, Heatmap, Color-Map, Color-Bar-Bounds)
- 7 assignment answers written and ready to submit (MLS-101-Day-5-Assignment-Answers.md)
- Full automation pipeline live: 9am lesson scraper + 1:30pm transcript processor
- API key installed, processor tested and working

## Review
(added at end)
