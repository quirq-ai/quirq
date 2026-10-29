# github-activity

Public dashboard of GitHub activity.

| | |
| --- | --- |
| Repository | [quirq-ai/github-activity](https://github.com/quirq-ai/github-activity) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-10-23 |
| Last commit | 2026-10-23: GitHub activity dashboard: public repos, server-side token, 5-min cache |

## Purpose

A small public dashboard of activity across quirq's **public** GitHub repositories: commits per week, a live event feed, and a card per repo (language, CI status, open PRs and issues, latest release, 12-week commit sparkline).

## Stack

Next.js (App Router, Cache Components) and React in TypeScript, deployed on Vercel. All GitHub calls run server-side (`server-only`); data refreshes in the background every 5 minutes.

## Structure

| Path | What it holds |
| --- | --- |
| `src/lib/github.ts` | Server-only GitHub client; filters to public repos and allowed owners |
| `src/app/` | Dashboard and per-repo pages |
| `src/components/` | Charts, feed and repo cards |

## How to run

```sh
cp .env.example .env.local   # GITHUB_TOKEN: fine-grained PAT, public repos read-only
npm install
npm run dev
```

`GITHUB_OWNERS` sets which users and orgs are included (default `quirq-ai,quirq-gates`).

## Status

Built 2026-10-23. Sister project of vercel-activity.

## Key links

- Code: https://github.com/quirq-ai/github-activity
- README: https://github.com/quirq-ai/github-activity#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
