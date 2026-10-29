# instants

An Instagram-style feed of your agent activity.

| | |
| --- | --- |
| Repository | [quirq-ai/instants](https://github.com/quirq-ai/instants) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-10-02 |
| Last commit | 2026-10-07: Implement two-log agent timeline and private activity engine |

## Purpose

**Instants: your agent activity, in one place.** A local, Instagram-style visual feed for agent activity. Import Codex or Claude conversation JSONL (or a normalized Instants timeline) and read it as cards with detail views, conversations, Explore search and profiles; keep private reading state, saves and notes; review DMs, comments, mentions and reviews in an attention rail. Two JSONL files hold everything: `timeline.jsonl` (feed) and `activity.jsonl` (your private activity). It is one of the apps bundled in Euler.

## Stack

Next.js and React in TypeScript, shadcn/Radix UI, Tailwind, Drizzle ORM (Cloudflare D1 for the optional Sites scaffold), Recharts, Zod, Playwright for e2e. Deployed on Vercel. MIT.

## Structure

| Path | What it holds |
| --- | --- |
| `app/` | Feed, API routes and the `/motion` playground |
| `components/` | Instagram-style UI, collaboration and motion components |
| `engine/`, `session/`, `lib/` | Timeline and activity engines, importers |
| `db/`, `drizzle/` | Schema and migrations |
| `data/`, `examples/` | Seed team feed (`xo_builders`, `quirq_ai`) and D1 example |
| `tests/` | Node unit tests and Playwright e2e |

## How to run

```sh
git clone https://github.com/quirq-ai/instants.git && cd instants
npm ci
npm run dev          # http://localhost:5180, /motion for the playground
npm test && npm run test:e2e
```

Node.js 22.13+. No API keys needed.

## Status

Active through 2026-10-07 (two-log agent timeline and private activity engine).

## Key links

- Code: https://github.com/quirq-ai/instants
- README: https://github.com/quirq-ai/instants#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
