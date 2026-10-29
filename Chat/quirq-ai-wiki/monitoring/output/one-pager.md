# monitoring

Read-only dashboard of the whole org's state.

| | |
| --- | --- |
| Repository | [quirq-ai/monitoring](https://github.com/quirq-ai/monitoring) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-10-05 |
| Last commit | 2026-10-22: infra: qq manifest for the compatibility check (not onboarding) (#22) |
| Website | https://monitoring-lac-chi.vercel.app |

## Purpose

The quirq-ai monitoring dashboard at [monitoring.quirq.dev](https://monitoring.quirq.dev/): one read-only page that says what changed across the org and what state everything is in, on phone or desktop. It reads the state the qq repos already publish (tree status, lkgr, canary channels, gardener ledger, perf, CI, PRs) and shows each value with its state word first (`green`, `red`, `held`, `pending`, `unknown`, `stale`) and a link to its source. Pages: Calendar, Blockers, Board, Release, Health, Gardener, per-repo, Settings, and a JSON snapshot for agents. The Settings editor changes infra settings only as pull requests under your own `gh` login.

## Stack

Next.js and React in TypeScript, Radix UI and Tailwind, smol-toml and Zod, Vitest and Playwright. pnpm 11. Deployed on Vercel.

## Structure

| Path | What it holds |
| --- | --- |
| `app/` | The pages and `/api/snapshot` |
| `lib/sources/`, `lib/model/` | Readers for each published source, and the state model |
| `lib/editor/` | The Settings editor |
| `components/` | UI |
| `tests/` | Unit tests, a fake GitHub, fixtures and e2e |
| `config/`, `infra/` | Dashboard config and qq manifest |

## How to run

```sh
corepack enable
pnpm install --frozen-lockfile
pnpm dev                    # http://localhost:3000
pnpm lint && pnpm typecheck && pnpm test && pnpm build && pnpm e2e
pnpm live                   # read every source once against the real branches
```

## Status

Live. Last change 2026-10-22.

## Key links

- Code: https://github.com/quirq-ai/monitoring
- README: https://github.com/quirq-ai/monitoring#readme
- Live: https://monitoring-lac-chi.vercel.app
- qq plan and v0 items: https://github.com/quirq-ai/infra-config/tree/main/docs
- qq docs: https://docs.quirq.dev/docs
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
