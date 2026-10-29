# website

quirq home base, the public site at quirq.dev.

| | |
| --- | --- |
| Repository | [quirq-ai/website](https://github.com/quirq-ai/website) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-10-05 |
| Last commit | 2026-10-14: Hide the blob avatar until quirqy is reintroduced (#27) |
| Website | https://quirq.dev |

## Purpose

**quirq home base: everything quirq builds, one little space.** The public site at [quirq.dev](https://quirq.dev): a desktop-style page for the apps, experiments, tools and open-source projects in the quirq-ai org. It has a live catalog of public repos with search and filters, a docs file tree per repo, projects grouped by phase with public build and canary state, and apps that open in their own windows with a floating dock.

## Stack

Gatsby 4, React 18 and Tailwind CSS in TypeScript, with desktop components and artwork adapted from PostHog's site. Node.js 24 and pnpm 10.23.0. Onboarded to qq (generated `website-presubmit` check). Deployed on Vercel.

## Structure

| Path | What it holds |
| --- | --- |
| `src/` | Pages, components, window system, navs, templates |
| `quirq.apps.json`, `quirq.projects.json` | The app catalog and project list |
| `scripts/` | `sync-quirq-apps.mjs`, `sync-quirq-projects.mjs` and tests |
| `docs/` | Development guide, app mapping, repository audit |
| `infra/` | qq manifest |

## How to run

```sh
git clone https://github.com/quirq-ai/website.git && cd website
corepack enable && corepack prepare pnpm@10.23.0 --activate
pnpm install --frozen-lockfile
pnpm start                  # http://127.0.0.1:8001
pnpm apps:check && pnpm projects:check
```

## Status

Live. Last change 2026-10-14 (avatar hidden until quirqy returns).

## Key links

- Code: https://github.com/quirq-ai/website
- README: https://github.com/quirq-ai/website#readme
- Live: https://quirq.dev
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
