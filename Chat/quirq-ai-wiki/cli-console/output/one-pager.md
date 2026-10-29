# cli-console

Turn installed CLIs into a browser workspace.

| | |
| --- | --- |
| Repository | [quirq-ai/cli-console](https://github.com/quirq-ai/cli-console) |
| Visibility | Public |
| Main language | TypeScript |
| Default branch | `main` |
| Created | 2026-10-13 |
| Last commit | 2026-10-14: Add local Next.js CLI console and README |

## Purpose

**cli console** turns the command-line tools installed on your machine into a browser workspace. Pick a program on `PATH`; its console is generated on demand from local `--help` or man pages: command families in the sidebar, subcommands across the top, flags as forms, then a reviewed, explicitly confirmed run with structured output, history and cancellation. Optional AI enrichment improves titles and descriptions but can never change commands or approve a run.

## Stack

Next.js and React in TypeScript, Zod for schemas, the Vercel `ai` SDK (AI Gateway) for optional enrichment. Node.js 22+. Tests use Node's test runner with `tsx`.

## Structure

| Path | What it holds |
| --- | --- |
| `src/app/` | Next.js routes and API handlers |
| `src/components/` | The console UI |
| `src/lib/` | Help and man-page parsers, schema, cache, process runner |
| `test/` | Parser and runner tests |

## How to run

```sh
git clone https://github.com/quirq-ai/cli-console.git && cd cli-console
npm ci
npm run dev        # http://127.0.0.1:4320
```

For AI enrichment, copy `.env.example` to `.env.local` and set `AI_GATEWAY_API_KEY` and `AI_MODEL`. The server binds to loopback only: it is a local, single-user command runner.

## Status

Early: created and first shipped 2026-10-13/14. Tested on macOS.

## Key links

- Code: https://github.com/quirq-ai/cli-console
- README: https://github.com/quirq-ai/cli-console#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
