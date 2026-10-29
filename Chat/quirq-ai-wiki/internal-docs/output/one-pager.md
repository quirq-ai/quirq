# internal-docs

The XO team's internal knowledge base (private).

| | |
| --- | --- |
| Repository | [quirq-ai/internal-docs](https://github.com/quirq-ai/internal-docs) |
| Visibility | Private |
| Main language | MDX |
| Default branch | `main` |
| Created | 2026-10-09 |
| Last commit | 2026-07-22: add: campaign referral operation handbook |

> Private repo. quirq/quirq is public on GitHub, so this page only says what the repo is for and how it is laid out. Its contents stay in the repo.

## Purpose

**XO Internal Docs**: the XO team's internal knowledge base (go-to-market, technical architecture, product roadmap, operations and culture), served as a signed-in docs site. Marked "do not share".

## Stack

Next.js with Fumadocs (MDX), Tailwind, Mermaid and Recharts, Clerk sign-in, Docker.

## Structure

| Path | What it holds |
| --- | --- |
| `content/docs/` | The MDX pages, one folder per section |
| `app/`, `components/`, `lib/` | The site, sign-in and MDX components |
| `public/` | Images for the pages |

## How to run

```sh
npm install
npm run dev        # http://localhost:3000
```

## Status

Quiet: last change 2026-07-22 (migrated from an older repo).

## Key links

- Code: https://github.com/quirq-ai/internal-docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
