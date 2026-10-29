# xo-cowork-api

The earlier FastAPI control plane for coding agents, superseded by xo-space.

| | |
| --- | --- |
| Repository | [quirq-ai/xo-cowork-api](https://github.com/quirq-ai/xo-cowork-api) |
| Visibility | Public |
| Main language | Python |
| Default branch | `main` |
| Created | 2026-02-04 |
| Last commit | 2026-08-22: fix:missing env keys on workspace restart |

## Purpose

**xo-cowork-api: the local control plane for AI coding agents.** The FastAPI service that powers an XO Cowork workspace: it runs inside every workspace, brokers chat to whichever coding agent runtime is installed (Claude Code, OpenClaw, Codex, Hermes, Antigravity), and owns the on-disk projects, sessions, files, secrets, OAuth flows and usage reporting behind one HTTP and SSE API on port 5002, consumed by the Tauri xo-cowork UI. It is the predecessor of xo-space.

## Stack

Python 3.12+ with FastAPI and Uvicorn, a vanilla JS and CSS `space_ui`, shell scripts to start and update, Docker. MIT.

## Structure

| Path | What it holds |
| --- | --- |
| `server.py` | The FastAPI app |
| `routers/` | Chat, sessions, files, auth, agent and status endpoints |
| `services/` | Agent runtimes and workspace services |
| `config/agents/`, `config/models/`, `config/skills/` | Runtime, model and skill configs |
| `space_ui/` | The built-in web UI |
| `cowork-api.sh`, `cowork-update.sh`, `docs/` | Run and update scripts, docs |

## How to run

```sh
git clone https://github.com/quirq-ai/xo-cowork-api.git && cd xo-cowork-api
pip install -r requirements.txt
cp .env.example .env
claude /login                # or start another runtime
python server.py             # http://localhost:5002
```

## Status

Superseded by xo-space; last commit 2026-08-22.

## Key links

- Code: https://github.com/quirq-ai/xo-cowork-api
- README: https://github.com/quirq-ai/xo-cowork-api#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
