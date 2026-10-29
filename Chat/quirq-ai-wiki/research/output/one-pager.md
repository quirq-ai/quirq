# research

Verified research outcomes, published as a hub.

| | |
| --- | --- |
| Repository | [quirq-ai/research](https://github.com/quirq-ai/research) |
| Visibility | Public |
| Main language | HTML |
| Default branch | `main` |
| Created | 2026-10-03 |
| Last commit | 2026-10-14: hub: improve output navigation and embed PDF reader (#62) |
| Website | https://research.quirq.dev |

## Purpose

**Verified, shareable research outcomes from quirq**, published at [research.quirq.dev](https://research.quirq.dev). Not a scratchpad: everything committed has been checked against its sources and is safe to share. Each topic is a top-level folder made from `_template/` with a README, `GOAL.md`, `AGENTS.md` and an `output/` split into `onepager/`, `slide/`, `report/` and `app/`.

## Stack

Node.js with Turborepo; topics build to static HTML, and a hub site (`scripts/build-hub.mjs`) gathers every topic's outputs, including an embedded PDF reader. Shared `packages/present` (slides) and `packages/theme`. Deployed on Vercel.

## Structure

| Path | What it holds |
| --- | --- |
| `claude/`, `design/`, `engineering/`, `infra/`, `marketing/`, `product/` | Research topics, each with `output/` |
| `_template/` | The topic template |
| `packages/present/`, `packages/theme/` | Shared presentation and theme |
| `scripts/` | `new-topic.sh`, `check.mjs`, `build-hub.mjs`, topics table |

## How to run

```sh
npm install
scripts/new-topic.sh <slug>    # start a topic
npm run check
npm run dev                    # build every topic and serve the hub
npm run build
```

## Status

Active through 2026-10-14 (hub navigation and PDF reader).

## Key links

- Code: https://github.com/quirq-ai/research
- README: https://github.com/quirq-ai/research#readme
- Live: https://research.quirq.dev
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
