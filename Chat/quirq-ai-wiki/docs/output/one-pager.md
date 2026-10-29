# docs

docs.quirq.dev, the qq and xo documentation.

| | |
| --- | --- |
| Repository | [quirq-ai/docs](https://github.com/quirq-ai/docs) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-08-26 |
| Last commit | 2026-10-27: xo docs: pin 6e6d79b, xo gh and xo sh, a page on the quirq hub (#44) |
| Website | https://docs.quirq.dev |

## Purpose

The source of [docs.quirq.dev](https://docs.quirq.dev/), the documentation for **qq**, quirq's build and release infrastructure, and for the `xo` CLI and the quirq hub. It includes an AI chat over the docs, search, OG images and an `llms.txt` route. XO Space docs live separately at docs.xo.builders.

## Stack

Next.js with Fumadocs (MDX content), Tailwind, Biome for lint and format, FlexSearch, the Vercel AI SDK with Anthropic and OpenRouter providers plus the Claude Agent SDK for the chat, PostHog analytics. pnpm.

## Structure

| Path | What it holds |
| --- | --- |
| `content/docs/` | The MDX pages |
| `src/app/docs`, `src/app/api/search`, `src/app/api/chat`, `src/app/og/docs`, `src/app/llms.txt` | Docs layout, search, AI chat, OG images, LLM text |
| `src/journeys/`, `scripts/journeys/` | Guided journeys |
| `public/videos/`, `scripts/videos/` | Demo videos rendered from real qq runs, and the scripts that render them |
| `.claude/skills/`, `.agents/skills/` | Agent skills for maintaining the docs |

## How to run

```sh
pnpm install
pnpm dev            # http://localhost:3100
pnpm lint && pnpm types:check
```

## Status

Active. Recent work documents `xo gh`, `xo sh` and the quirq hub.

## Key links

- Code: https://github.com/quirq-ai/docs
- README: https://github.com/quirq-ai/docs#readme
- Live: https://docs.quirq.dev
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
