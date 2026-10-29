# innernet

A personal internet made from your folders: search plus Innerpedia.

| | |
| --- | --- |
| Repository | [quirq-ai/innernet](https://github.com/quirq-ai/innernet) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-10-02 |
| Last commit | 2026-10-09: docs: agents never approve pull requests (#49) |
| Website | https://innernet.quirq.dev |

## Purpose

**Innernet: a personal internet, made from your folders.** It indexes the folders on your machine (and optionally public GitHub repos) and gives you a search engine over them plus **Innerpedia**, an encyclopedia article per project (README overview, folder tree, tech, Git history, related projects). It also indexes agent dot-folders (`.claude`, `.codex`, `.cursor`, `.xo`) as articles, keeps a local browsing history, and has an illustrated field guide with a narrated film. A public demo indexes quirq-ai's open repos.

## Stack

Next.js and React in TypeScript, MiniSearch for search, PGlite locally and Neon Postgres when hosted, pnpm. The field-guide film is built with HyperFrames-style scripts in `film/`. Deployed on Vercel.

## Structure

| Path | What it holds |
| --- | --- |
| `app/` | Routes: search, wiki (Innerpedia), sources, activity, guide, API |
| `components/`, `lib/` | UI and the index, search and database code |
| `scripts/` | `build-index`, `build-demo-index`, `db` |
| `innernet.config.json` | Roots to index and depth |
| `data/demo/` | The committed demo index (GitHub URLs only) |
| `film/` | The field guide film: brief, storyboard, scenes, voice |
| `brand/`, `docs/architecture/`, `DESIGN.md` | Brand and design docs |

## How to run

```sh
git clone https://github.com/quirq-ai/innernet.git && cd innernet
pnpm install
# edit innernet.config.json roots (default ~/Programming)
pnpm index
pnpm dev                 # http://localhost:3470
pnpm index:demo && pnpm dev:demo   # the public demo locally
```

Node.js 20.9+ and pnpm.

## Status

Onboarded to qq (has a generated `innernet-presubmit` required check). Public demo live. Last change 2026-10-09.

## Key links

- Code: https://github.com/quirq-ai/innernet
- README: https://github.com/quirq-ai/innernet#readme
- Live: https://innernet.quirq.dev
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
