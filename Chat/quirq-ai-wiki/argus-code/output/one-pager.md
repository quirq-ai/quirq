# argus-code

Local observability for Claude Code and Codex sessions (fork).

| | |
| --- | --- |
| Repository | [quirq-ai/argus-code](https://github.com/quirq-ai/argus-code) |
| Visibility | Public (fork) |
| Main language | Python |
| Default branch | `main` |
| Last commit | 2026-10-05: docs: 0.7.0 screenshots (Claude Code + Codex); agent-aware search label; stricter capture redaction (#56) |

## Purpose

**Argus**, a fork of KrishBhimani/argus-code: a local-first observability console for Claude Code and OpenAI Codex. It tails the session transcripts in `~/.claude/` and `~/.codex/` into a SQLite archive (`~/.argus/argus.db`), prices every turn, and serves a dashboard at `http://localhost:4242` with per-session forensics, cost and token breakdowns, tool health, sub-agent views, alerts from baseline detectors, and optional full-text search. Nothing leaves the machine.

## Stack

Python 3.11+ (FastAPI, Uvicorn, SQLite) for the collector, daemon and API; an Astro + React/TypeScript dashboard prebuilt into `dashboard-dist/`. Published on PyPI as `argus-code` (v0.7.0). MIT.

## Structure

| Path | What it holds |
| --- | --- |
| `python/argus/` | CLI, adapters (Claude Code, Codex), collector, daemon, detectors, pricing, store, server |
| `dashboard/` | Dashboard source (Astro, TSX, e2e tests) |
| `dashboard-dist/` | Built dashboard served by the API |
| `tests/` | Pytest suites per module |
| `ARCHITECTURE.md`, `PRD.md`, `TESTING.md` | Design, product and test docs |

## How to run

```sh
pipx install argus-code     # or: uv tool install argus-code
argus start                 # watcher + ingester + dashboard at :4242
argus daemon start          # keep ingesting in the background
argus indexing enable       # opt in to full-text search
```

## Status

Beta (0.7.0). This is a fork; upstream development happens in KrishBhimani/argus-code.

## Key links

- Code: https://github.com/quirq-ai/argus-code
- README: https://github.com/quirq-ai/argus-code#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
