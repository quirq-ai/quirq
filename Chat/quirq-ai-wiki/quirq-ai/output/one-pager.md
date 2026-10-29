# quirq_ai

The original cinematic quirq.ai marketing site.

| | |
| --- | --- |
| Repository | [quirq-ai/quirq_ai](https://github.com/quirq-ai/quirq_ai) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-07-24 |
| Last commit | 2026-08-08: new commit |
| Website | https://quirq.ai |

## Purpose

**quirq: work at light speed.** The original marketing and research site for quirq (quirq.ai): a cinematic, data-driven page built as one continuous shot around a procedural glass ribbon. Each section registers as a *beat*, scroll position becomes a fractional beat, and a choreography track blends 14 pose, optics and lighting channels. The pitch: tokens meter what agents consume, quirqs meter what they deliver. It ships a whitepaper (PDF and LLM-readable text) and can render pages from JSON.

## Stack

Next.js 16 and React 19 in strict TypeScript, Three.js with React Three Fiber and drei, Motion, Lenis, Tailwind 4. pnpm.

## Structure

| Path | What it holds |
| --- | --- |
| `app/` | Pages: home beats, what-is-quirq, how-it-works, whitepaper, research, products, registry, dashboard, editor and more |
| `components/` | Stage (the ribbon), beats, story, journey, research, prose, UI |
| `lib/quirq/` | The quirq ledger model and CLI |
| `scripts/` | Sample ledger and git-journey builders |
| `public/` | Assets, research files, whitepaper |
| `_to_delete/` | Content marked for removal |

## How to run

```sh
pnpm install
pnpm dev            # http://localhost:3000
pnpm build && pnpm start
pnpm test
```

Node.js 20.9+ and a browser with WebGL (a still-image fallback is included).

## Status

Older: last commit 2026-08-08. The public site has since moved to the `website` repo; consider archiving this one.

## Key links

- Code: https://github.com/quirq-ai/quirq_ai
- README: https://github.com/quirq-ai/quirq_ai#readme
- Live: https://quirq.ai
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
