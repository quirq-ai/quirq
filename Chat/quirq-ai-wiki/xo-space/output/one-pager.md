# xo-space

XO Space: one local environment to build, observe and measure work across every coding agent.

| | |
| --- | --- |
| Repository | [quirq-ai/xo-space](https://github.com/quirq-ai/xo-space) |
| Visibility | Public (fork) |
| Main language | Python |
| Default branch | `main` |
| Last commit | 2026-10-27: feat(storm): the storm engine, with the claude and codex runtimes (#283) |

## Purpose

**XO Space: build, observe and measure agentic work, locally, across every coding agent you use.** The environment layer between your machine and your agents: a local server plus a browser UI at `http://localhost:5002/space/` that puts every project, session, todo and cost from Claude Code, Codex, OpenClaw, Hermes and Antigravity on one screen, with one chat API for all of them (Claude Code chats through **storm**, XO's session engine), connections, inbox, terminal, swarm and doctor services, and project backup. It is quirq's main product repo and the first repo onboarded to qq. The GitHub repo is marked as a fork.

## Stack

Python 3.12+ with FastAPI (installed into a uv venv), a vanilla JS and CSS `space_ui`, a Codex and Claude Code plugin (`plugins/quirq`, `.claude-plugin`), Docker. Required check `xo-space-presubmit` through the qq gate, with lkgr and canary channels from release.

## Structure

| Path | What it holds |
| --- | --- |
| `server.py`, `routers/` | FastAPI app and endpoints |
| `services/` | cowork agent, storm, connections, inbox, swarm API, terminal, storage, doctor, decision models |
| `space_ui/` | The browser UI |
| `plugin/`, `plugins/quirq/` | Codex and Claude Code plugins |
| `config/`, `infra/` | Agent and skill configs; qq manifest |
| `install.sh`, `uninstall.sh`, `INSTALLATION.md`, `RELEASING.md` | Install, removal and release docs |
| `tests/` | Pytest suites with fakes and UI previews |

## How to run

```sh
curl -fsSL https://quirq.ai/install | sh     # from your workspace folder
# open http://localhost:5002/space/
```

Or in Codex: `codex plugin marketplace add quirq-ai/xo-space`, install the XO Space plugin, then say "Open XO Space". Needs only `git`; Windows via WSL. Docs at [docs.quirq.dev](https://docs.quirq.dev).

## Status

Very active (storm engine with Claude and Codex runtimes landed 2026-10-27). Canary channel live since 2026-10-05.

## Key links

- Code: https://github.com/quirq-ai/xo-space
- README: https://github.com/quirq-ai/xo-space#readme
- Wiki index: Chat/quirq-ai-wiki/output/one-pager.md
