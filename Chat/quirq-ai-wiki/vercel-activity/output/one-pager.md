# vercel-activity

Public dashboard of Vercel deployments.

| | |
| --- | --- |
| Repository | [quirq-ai/vercel-activity](https://github.com/quirq-ai/vercel-activity) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-10-23 |
| Last commit | 2026-10-23: Show only workspace projects; add account and domains page |

## Purpose

A small public site showing deployment activity for the Vercel projects deployed from the quirq workspace (deploy state, prod or preview, time, build duration, branch, short SHA, commit title for public repos), plus an `/account` page with the Vercel team and its domains. Only projects linked to a GitHub repo listed in `workspace.json` are shown, and only an allowlist of public-safe fields ever leaves the server.

## Stack

Next.js server components in TypeScript, calling the Vercel REST API with a server-only token, cached for 5 minutes (`"use cache"` and `cacheLife`). Deployed on Vercel.

## Structure

| Path | What it holds |
| --- | --- |
| `src/lib/activity.ts` | Vercel API client and field allowlist |
| `src/app/` | Activity and account pages |
| `src/components/` | UI |
| `workspace.json` | The GitHub repos whose Vercel projects are shown |

## How to run

```sh
npm install
VERCEL_TOKEN=... VERCEL_TEAM_ID=... npm run dev
```

Optional `SHOW_PRIVATE_COMMIT_MESSAGES=true` shows commit titles for private repos.

## Status

Built 2026-10-23. Sister project of github-activity.

## Key links

- Code: https://github.com/quirq-ai/vercel-activity
- README: https://github.com/quirq-ai/vercel-activity#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
