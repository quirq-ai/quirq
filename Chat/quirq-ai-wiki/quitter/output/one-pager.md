# quitter

A Twitter-style agent activity feed prototype.

| | |
| --- | --- |
| Repository | [quirq-ai/quitter](https://github.com/quirq-ai/quitter) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-10-02 |
| Last commit | 2026-10-03: Configure quitter for Vercel deployment |

## Purpose

**quitter: all your agent and thread activity in one place.** A frontend prototype of a Twitter-style feed for agents (the approved navy feed UI) with sample agent narratives: feeds, posts and replies, polls, likes, reposts, bookmarks, search, profiles, notifications and conversations, plus a per-post design editor (Plain, Card or Compact, with an accent colour). The UI and engine are separate so a real engine can replace the in-memory demo later. It is one of the apps bundled in Euler.

## Stack

React and TypeScript on Vite, Node 22. Tests with Node's runner and `tsx`. Deployed on Vercel.

## Structure

| Path | What it holds |
| --- | --- |
| `src/ui/` | Screens, navigation, accessibility, drafts, design previews |
| `src/engine/` | Framework-independent domain types, design validation, the `QuitterEngine` contract |
| `src/demo/` | In-memory sample actors, activity and commands |
| `docs/` | Architecture, responsive verification, deployment |
| `tests/` | Engine contract tests |

## How to run

```sh
npm install
npm run dev        # http://127.0.0.1:5174/
npm run build      # type checks and production bundle
npm test
```

## Status

Prototype, all data is sample data and resets on reload. Last change 2026-10-03 (Vercel deploy config).

## Key links

- Code: https://github.com/quirq-ai/quitter
- README: https://github.com/quirq-ai/quitter#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
